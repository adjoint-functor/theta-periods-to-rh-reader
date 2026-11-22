# SPDX-FileCopyrightText: 2026 The Theta Periods to RH Reading Edition contributors
# SPDX-License-Identifier: MIT

"""Check proof-map.html and regenerate its derived index.

python proof_map.py            check the map against the graph, the paper and the PDF
python proof_map.py --update   regenerate the derived index, PDF hash and no-script outline
python proof_map.py --lean D   also check Lean citations against a checkout of the pinned source
"""

import argparse
import hashlib
from html import escape
from itertools import product
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
MAP = ROOT / "proof-map.html"
README = ROOT / "README.md"
DATA = re.compile(r'(<script type="application/json" id="proof-data"[^>]*>)(.*?)(</script>)', re.S)
OUTLINE = re.compile(r"<noscript>.*?</noscript>", re.S)
LEAN_BASE = ("https://github.com/TomasOrtega/RH/blob/"
             "a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean/src/")
STATUSES = {"connected", "open", "derived", "classical", "lean", "mixed", "checked",
            "granted", "frozen", "antecedent"}
INDEX_KEYS = ("source_links", "ancestors", "export_origins", "routes", "contract_inputs",
              "output_dependencies", "output_proof_context", "article_href", "article_sha256")


def serialize(data):
    # The block sits inside <script>, so "<" is escaped as in the published file.
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = {node["id"]: node for node in graph["nodes"]}
        self.inputs = {f"{n['id']}.{i['id']}": i for n in graph["nodes"] for i in n["inputs"]}
        self.outputs = {f"{n['id']}.{o['id']}": o for n in graph["nodes"] for o in n["outputs"]}
        self.children = {}
        for node in graph["nodes"]:
            if node["parent"]:
                self.children.setdefault(node["parent"], []).append(node["id"])

    def ancestors(self, node_id):
        chain = []
        while node_id:
            chain.append(node_id)
            node_id = self.nodes[node_id]["parent"]
        return chain[::-1]

    def breadth_first(self):
        order = {node_id: position for position, node_id in enumerate(self.nodes)}
        return sorted(self.nodes, key=lambda node_id: (len(self.ancestors(node_id)), order[node_id]))

    def consumer_chain(self, port):
        """The input port preceded by the parent inputs it aliases with "@"."""
        chain = [port]
        while (source := self.inputs[chain[0]].get("from")) and source.startswith("@"):
            parent = self.nodes[chain[0].split(".")[0]]["parent"]
            chain.insert(0, f"{parent}.{source[1:]}")
        return chain

    def producer_chain(self, port):
        """The output port followed by the child outputs that export it."""
        chain = [port]
        while "via" in self.outputs[chain[-1]]:
            chain.append(self.outputs[chain[-1]]["via"])
        return chain

    def resolve(self, node_id, inputs):
        outputs, external = [], []
        for item in inputs:
            top = self.consumer_chain(f"{node_id}.{item['id']}")[0]
            source = self.inputs[top].get("from")
            (outputs if source else external).append(source or top)
        return {"outputs": list(dict.fromkeys(outputs)), "external": list(dict.fromkeys(external))}

    def dependencies(self, port):
        """Direct and proof-context dependencies of an output."""
        output = self.outputs[port]
        node_id = port.split(".")[0]
        if "via" in output:
            return {"outputs": [output["via"]], "external": []}, None
        node = self.nodes[node_id]
        used = output.get("uses") or [item["id"] for item in node["inputs"]]
        items = [self.inputs[f"{node_id}.{key}"] for key in used]
        # Context inputs are dashed only beside a direct input. An optional proof
        # consisting of context inputs alone depends on them directly.
        if all(item.get("context") for item in items):
            return self.resolve(node_id, items), None
        direct = [item for item in items if not item.get("context")]
        context = [item for item in items if item.get("context")]
        return self.resolve(node_id, direct), (self.resolve(node_id, context) if context else None)

    def routes(self):
        aliased = {chain[-2] for port in self.inputs if len(chain := self.consumer_chain(port)) > 1}
        routes = []
        for port in self.inputs:
            if port in aliased:
                continue
            consumer = self.consumer_chain(port)
            source = self.inputs[consumer[0]].get("from")
            routes.append({"producer": self.producer_chain(source) if source else [],
                           "consumer": consumer})
        return routes

    def index(self, source_links, article_sha256):
        # Refined steps come first, so their exported conclusions precede the substeps.
        order = [node_id for node_id in self.nodes if node_id in self.children]
        order += [node_id for node_id in self.nodes if node_id not in self.children]
        ports = [f"{node_id}.{o['id']}" for node_id in order for o in self.nodes[node_id]["outputs"]]
        dependencies = {port: self.dependencies(port) for port in ports}
        return {
            "source_links": source_links,
            "ancestors": {node_id: self.ancestors(node_id) for node_id in self.breadth_first()},
            "export_origins": {port: self.producer_chain(port)[-1] for port in ports},
            "routes": self.routes(),
            "contract_inputs": list(self.inputs),
            "output_dependencies": {port: direct for port, (direct, _) in dependencies.items()},
            "output_proof_context": {port: context for port, (_, context) in dependencies.items() if context},
            "article_href": "reading-guide.pdf",
            "article_sha256": article_sha256,
        }

    def project(self, expanded):
        """Edges drawn by the viewer when the given parents are expanded."""
        visible = {node_id for node_id in self.nodes if node_id not in expanded
                   and all(a in expanded for a in self.ancestors(node_id)[:-1])}

        def shown(node_id):
            return next(a for a in self.ancestors(node_id) if a in visible)

        edges, lost = set(), []
        for route in self.routes():
            if not route["producer"]:
                continue
            start = next((p for p in route["producer"] if p.split(".")[0] in visible), None)
            end = next((p for p in route["consumer"] if p.split(".")[0] in visible), None)
            if start and end:
                if start.split(".")[0] != end.split(".")[0]:
                    edges.add((start.split(".")[0], end.split(".")[0]))
            elif shown(route["producer"][0].split(".")[0]) != shown(route["consumer"][-1].split(".")[0]):
                lost.append(route)
        return visible, edges, lost


def topological(nodes, edges):
    incoming = {node: 0 for node in nodes}
    for _, end in edges:
        incoming[end] += 1
    ready = [node for node in nodes if not incoming[node]]
    ordered = []
    while ready:
        node = ready.pop(0)
        ordered.append(node)
        for start, end in sorted(edges, key=lambda edge: nodes.index(edge[1])):
            if start == node:
                incoming[end] -= 1
                if not incoming[end]:
                    ready.append(end)
    return ordered if len(ordered) == len(nodes) else None


def pdf_destinations(pdf):
    if shutil.which("pdfinfo") is None:
        return None
    result = subprocess.run(["pdfinfo", "-dests", str(pdf)], capture_output=True, text=True, check=False)
    if result.returncode:
        return None
    return {line.rsplit(None, 1)[-1].strip('"') for line in result.stdout.splitlines()[1:] if line.strip()}


def tex_anchors():
    anchors = set()
    for path in (ROOT / "tex").glob("*.tex"):
        anchors.update(re.findall(r"\\(?:teamanchor|hypertarget)\{([^}]+)\}", path.read_text(encoding="utf-8")))
    return anchors


def check(data, html, lean_root):
    errors, notes = [], []
    graph = Graph(data["graph"])
    nodes, index = graph.nodes, data["index"]

    if len(nodes) != len(data["graph"]["nodes"]):
        errors.append("Duplicate node identifiers.")
    groups = {group["id"] for group in data["graph"]["groups"]}
    for node in data["graph"]["nodes"]:
        where = node["id"]
        if node["parent"] and node["parent"] not in nodes:
            errors.append(f"{where}: unknown parent {node['parent']}.")
        if node["group"] not in groups:
            errors.append(f"{where}: unknown group {node['group']}.")
        for field in ("interface", "proof", "review"):
            if node[field]["status"] not in STATUSES:
                errors.append(f"{where}: unknown {field} status {node[field]['status']}.")
        for side in ("inputs", "outputs"):
            keys = [item["id"] for item in node[side]]
            if len(keys) != len(set(keys)):
                errors.append(f"{where}: duplicate {side}.")
        for item in node["inputs"]:
            status = item.get("receipt", {}).get("status")
            if status and status not in STATUSES:
                errors.append(f"{where}.{item['id']}: unknown receipt status {status}.")
            source = item.get("from")
            if not source:
                continue
            if source.startswith("@"):
                parent = node["parent"]
                if not parent or f"{parent}.{source[1:]}" not in graph.inputs:
                    errors.append(f"{where}.{item['id']}: alias {source} has no parent input.")
            elif source not in graph.outputs:
                errors.append(f"{where}.{item['id']}: unknown source {source}.")
            elif source.split(".")[0] in graph.ancestors(where):
                errors.append(f"{where}.{item['id']}: consumes an output of its own ancestor.")
        inputs = {item["id"] for item in node["inputs"]}
        for output in node["outputs"]:
            missing = set(output.get("uses", [])) - inputs
            if missing:
                errors.append(f"{where}.{output['id']}: uses unknown inputs {sorted(missing)}.")
            via = output.get("via")
            if via and (via not in graph.outputs or nodes[via.split(".")[0]]["parent"] != where):
                errors.append(f"{where}.{output['id']}: via {via} is not an output of a child.")
            if where in graph.children and not via:
                errors.append(f"{where}.{output['id']}: a refined step must export each conclusion from a substep.")
    if errors:
        return errors, notes

    for parent in graph.children:
        for item in nodes[parent]["inputs"]:
            port = f"{parent}.{item['id']}"
            if not any(graph.consumer_chain(other)[:-1].count(port) for other in graph.inputs if other != port):
                notes.append(f"{port}: no substep uses this input of the refined step.")
    for focus in data["graph"]["focus"]:
        if focus not in graph.children:
            errors.append(f"Focus step {focus} has no substeps.")

    # Every combination of expanded steps is a view the reader can reach.
    parents = list(graph.children)
    for flags in product((False, True), repeat=len(parents)):
        expanded = {parent for parent, flag in zip(parents, flags) if flag}
        visible, edges, lost = graph.project(expanded)
        label = ", ".join(sorted(expanded)) or "overview"
        if topological(sorted(visible, key=list(nodes).index), edges) is None:
            errors.append(f"View [{label}] contains a cycle.")
        for route in lost:
            errors.append(f"View [{label}] drops the dependency {route['producer'][0]} -> {route['consumer'][-1]}.")
    visible, edges, _ = graph.project(set())
    overview = topological(sorted(visible, key=list(nodes).index), edges)
    if overview and overview[-1] != "rh":
        errors.append(f"The overview does not end at classical RH: {overview}.")
    for node_id in visible - {"rh"}:
        if not any(start == node_id for start, _ in edges):
            errors.append(f"Overview step {node_id} supplies no later step.")

    pdf = ROOT / index["article_href"]
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    expected = graph.index(index["source_links"], digest)
    if list(index) != list(INDEX_KEYS):
        errors.append("The index keys differ from the published layout.")
    for key in INDEX_KEYS:
        if key == "article_sha256":
            if index[key] != digest:
                errors.append(f"article_sha256 {index[key][:12]}… does not match {pdf.name} ({digest[:12]}…).")
        elif serialize(index.get(key)) != serialize(expected[key]):
            errors.append(f"The derived index entry {key} is stale. Run python proof_map.py --update.")

    destinations = pdf_destinations(pdf)
    if destinations is None:
        notes.append("pdfinfo is unavailable, so PDF destinations were not checked.")
    anchors = tex_anchors()
    if set(index["source_links"]) != set(nodes):
        errors.append("source_links must have one entry per step.")
    for node_id, links in index["source_links"].items():
        for link in links:
            if "anchor" in link:
                anchor = link["anchor"]
                if link["href"] != f"reading-guide.pdf#nameddest={anchor}":
                    errors.append(f"{node_id}: link {anchor} has href {link['href']}.")
                if anchor not in anchors:
                    errors.append(f"{node_id}: anchor {anchor} is not defined in tex/.")
                if destinations is not None and anchor not in destinations:
                    errors.append(f"{node_id}: anchor {anchor} is not a destination in {pdf.name}.")
            elif "lean" in link:
                if link["href"] != f"{LEAN_BASE}{link['lean']}#L{link['line']}":
                    errors.append(f"{node_id}: Lean link {link['lean']} has href {link['href']}.")
                if lean_root:
                    path = Path(lean_root) / link["lean"]
                    if not path.is_file():
                        errors.append(f"{node_id}: missing Lean file {link['lean']}.")
                    elif link["line"] > len(path.read_text(encoding="utf-8").splitlines()):
                        errors.append(f"{node_id}: {link['lean']} has no line {link['line']}.")
            elif not link.get("url") or not link.get("known_result"):
                errors.append(f"{node_id}: link {link.get('label')} has no target.")

    readme = README.read_text(encoding="utf-8")
    for anchor in sorted(set(re.findall(r"reading-guide\.pdf#nameddest=([A-Za-z0-9.:-]+)", readme))):
        if anchor not in anchors or (destinations is not None and anchor not in destinations):
            errors.append(f"README links to the missing destination {anchor}.")

    if lean_root:
        for path in sorted((ROOT / "tex").glob("*.tex")):
            text = path.read_text(encoding="utf-8")
            for cited, line in re.findall(r"\\releasecite\{([^}]+)\}\{(\d+)\}", text):
                source = Path(lean_root) / cited
                if not source.is_file():
                    errors.append(f"{path.name}: \\releasecite names the missing Lean file {cited}.")
                elif int(line) > len(source.read_text(encoding="utf-8").splitlines()):
                    errors.append(f"{path.name}: \\releasecite cites {cited} at line {line}, past its end.")

    if outline(data) not in html:
        errors.append("The no-script outline is stale. Run python proof_map.py --update.")
    return errors, notes


def outline(data):
    graph = Graph(data["graph"])
    visible, edges, _ = graph.project(set())
    shown = sorted(visible, key=list(graph.nodes).index)
    steps = topological(shown, edges) or shown
    links = data["index"]["source_links"]
    rows = []
    for node_id in steps:
        node = graph.nodes[node_id]
        anchor = next((link for link in links[node_id] if "anchor" in link), None)
        passage = (f' <a href="{escape(anchor["href"])}">{escape(anchor["label"])}</a>.'
                   if anchor else "")
        rows.append(f"            <li><strong>{escape(node['title'])}.</strong> "
                    f"{escape(node['summary'])}{passage}</li>")
    return ("<noscript>\n"
            "          <div class=\"static-outline\">\n"
            "            <p>The interactive diagram requires JavaScript. "
            "The proof overview has these steps in implication order.</p>\n"
            "            <ol>\n" + "\n".join("  " + row for row in rows) + "\n"
            "            </ol>\n"
            "          </div>\n"
            "        </noscript>")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--update", action="store_true", help="regenerate the derived parts of the map")
    parser.add_argument("--lean", metavar="DIR", help="extracted/lean/src of the pinned Lean source")
    arguments = parser.parse_args()

    html = MAP.read_text(encoding="utf-8")
    match = DATA.search(html)
    data = json.loads(match.group(2))
    if arguments.update:
        graph = Graph(data["graph"])
        digest = hashlib.sha256((ROOT / data["index"]["article_href"]).read_bytes()).hexdigest()
        data["index"] = graph.index(data["index"]["source_links"], digest)
        html = html[:match.start(2)] + serialize(data) + html[match.end(2):]
        html = OUTLINE.sub(lambda _: outline(data), html, count=1)
        MAP.write_text(html, encoding="utf-8")
        print(f"Updated {MAP.name}")

    errors, notes = check(data, html, arguments.lean)
    for note in notes:
        print(f"note: {note}")
    for error in errors:
        print(f"error: {error}")
    if errors:
        return 1
    print(f"{MAP.name}: {len(data['graph']['nodes'])} steps, {2 ** len(Graph(data['graph']).children)} views checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
