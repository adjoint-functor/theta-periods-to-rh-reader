# Working on the reading edition

Reconstruct the classical Riemann hypothesis (RH) argument in ordinary mathematical language so readers can check it from the exposition and primary references. Reduce reliance on Lean as direct proofs become available. Identify advances over the mathematics available before the original announcement.

## Refine the proof and map together

Choose a step from the coarse proof map, refine it as needed and write its proof while updating the map. Whenever a mathematical dependency of the classical RH argument changes, update the paper and the interactive `proof-map.html` in the same revision at every affected resolution.

The map opens on **Weighted square-scale route**, which follows the argument in Part I. Select **Earlier window route** for the six thematic sections in Part II. Those sections may cross-reference one another. Keep every view of both routes acyclic and ordered by implication. Trace backward from classical RH through the conclusions actually used. For the Dirichlet extension, state its target and additional inputs.

Give each step exact hypotheses, named inputs and suppliers, precise conclusions, dependency links and links to the corresponding passages. Check that its suppliers jointly give every input on the same objects, witnesses and data, with the required constants, normalizations and quantifier order. Check where each premise is discharged. Show in the collapsed view that the child results recover the parent conclusion under the original hypotheses for the same objects. Recheck the consumers and all affected collapsed, expanded and mixed views.

## Use the result each step needs

Start from public primary sources. Cite the exact version and passage of a known result, check its hypotheses on the actual objects and state the conclusion used downstream. Give direct derivations where possible and identify each input still taken from the pinned Lean release at its point of use. Use the announcement and public reconstruction linked in the README for orientation.

Check the stronger claim *S* against the pinned Lean proof. Use a weaker *W* in the paper and map wherever it has a simpler proof independent of *S* and supplies every required input on the same data. Label a verified *S* as a strengthening where *W* suffices. Withdraw a misattributed or refuted *S*. If neither suffices, mark the missing input and recheck the enclosing step.

## Check proofs and assess candidates

Have an independent subagent check every new or revised proof against its exact statement, actual objects and affected applications. Attribute those checks as AI checks.

Send each suspected new result to a separate Astra reviewer in a fresh context containing only the precise statement and necessary mathematical background. Compare it with earlier human mathematics and assess its intrinsic significance. Use earlier results where they supply the needed implication, and narrow or remove candidates accordingly. A substantive idea, extension of uniformity or new connection can merit candidacy with a short proof. Keep routine calculations, restatements and straightforward corollaries at their points of use.

Support priority claims with dated primary evidence of equivalent scope and record the sources checked. Track proof status, priority, intrinsic value and human specialist assessment separately. Label the list in both languages as AI-proposed candidates for new mathematics and group it by topic. Preserve candidate provenance and review history in working notes.

## Keep the window data consistent

Fix the target, precision, family and common threshold before choosing a window. At each real scale, check the weights and uniform replacement error at every tied translate. Supply the signed mean that Fourier inversion needs on that same set. For classical zeta, trace it through the local gains, selected seed and wordwise height bounds. A pointwise excess bound supplies the mean when its hypotheses hold. Use the same base Artin data, sampling degrees, weights, cutoff and centering in the lattice estimate and the Fourier calculation.

## Maintain the portable edition

Keep the paper, map and `AGENTS.md` in English and `README.md` in English and Chinese. Append dated entries to both README progress sections in chronological order, preserving the initial edition entry, earlier entries and their attributions. Reflect each candidate’s change in scope or status in the paper’s opening, at its point of use and in both languages of the README. Include the PDF, standalone editable map, sources and build files. Keep working notes, review records and build intermediates local.

Start with `tex/article.tex` and follow the README’s build instructions. When a claim, dependency or referenced passage changes, rebuild `reading-guide.pdf` and check the paired map. Preserve their relative filenames and stable PDF destinations. Verify a clean build and test the affected views and passage links offline after moving the PDF and HTML together.
