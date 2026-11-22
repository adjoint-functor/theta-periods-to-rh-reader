# SPDX-FileCopyrightText: 2026 The Theta Periods to RH Reading Edition contributors
# SPDX-License-Identifier: MIT

"""Build reading-guide.pdf from tex/article.tex with XeLaTeX."""

import os
from pathlib import Path
import re
import shutil
import subprocess
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parent
AUXILIARY = ("aux", "out", "toc", "lof", "lot")
UNRESOLVED = re.compile(
    r"There were undefined (?:references|citations)|"
    r"(?:Reference|Citation) .+ undefined|"
    r"(?:Object @\S+ already defined|duplicate destination)",
    re.IGNORECASE,
)


def compile_article(directory):
    xelatex = shutil.which("xelatex")
    if xelatex is None:
        raise RuntimeError("XeLaTeX must be on PATH.")
    command = [xelatex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
               "-no-shell-escape", "-jobname=article", "article.tex"]
    # A fixed timestamp keeps repeated builds reproducible with the same TeX installation.
    environment = {**os.environ, "SOURCE_DATE_EPOCH": "1795219200", "FORCE_SOURCE_DATE": "1",
                   "TEXINPUTS": "." + os.pathsep}
    auxiliary = [directory / f"article.{suffix}" for suffix in AUXILIARY]
    previous = None
    for _ in range(5):
        result = subprocess.run(command, cwd=directory, env=environment,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        transcript = result.stdout.decode("utf-8", errors="replace")
        if result.returncode:
            tail = "\n".join(transcript.splitlines()[-22:])
            raise RuntimeError(f"XeLaTeX failed.\n{tail}")
        current = tuple(path.read_bytes() if path.is_file() else None for path in auxiliary)
        if current == previous:
            log = (directory / "article.log").read_text(encoding="utf-8", errors="replace")
            issue = UNRESOLVED.search(log + "\n" + transcript)
            if issue:
                raise RuntimeError(f"Unresolved article reference or destination. {issue[0]}")
            return directory / "article.pdf"
        previous = current
    raise RuntimeError("Article references did not stabilize in five XeLaTeX passes.")


def main():
    output = ROOT / "reading-guide.pdf"
    # Stage the build on the same volume so a completed PDF can replace the old one atomically.
    with TemporaryDirectory(prefix=".reading-guide-", dir=ROOT) as temporary:
        source = Path(temporary) / "tex"
        shutil.copytree(ROOT / "tex", source)
        compile_article(source).replace(output)
    print(f"Built {output.name}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError) as error:
        raise SystemExit(str(error)) from error
