# Working on the reading edition

Reconstruct the full argument for classical RH in ordinary mathematical language and identify its genuinely new mathematics. Gradually reduce reliance on Lean so that readers can ultimately check the entire argument from the exposition and its primary references alone.

## Refine the proof and map together

AI agents select a step from the proof map, refine it to the level needed and write its proof. Update the map as the proof develops. Give the new substeps exact hypotheses, named inputs, precise conclusions, dependency links and links to the corresponding passages.

Keep the default **Proof overview** acyclic, with an explicit order of implications through classical RH. The paper’s six sections group the mathematics by topic and may refer to one another in either direction. In the Dirichlet extension, state its target and the additional inputs it uses. Recheck all affected coarse, fine and mixed views. Follow each upstream conclusion forward to its uses and trace each required input backward to its supplier or stated premise. Check where premises are discharged. At every join, verify that the upstream conclusions jointly supply all inputs for the same witnesses and data, with the required normalizations and quantifier order. Identify any missing or incompatible input at the affected step.

Verify that the substeps recover the parent conclusion under the original hypotheses for the same objects. The collapsed view must display that implication. If the parent statement changes, update the paper, its consumers and every affected view.

## Sources and independent checks

Start with public primary sources. When a step recovers known mathematics, locate the precise theorem or proof passage and cite its version. State the usable special case with its hypotheses and conclusion. Verify that the actual objects meet its hypotheses and that its conclusion supplies the input required downstream, then cite it as the named supplier. For the rest, give direct mathematical derivations and consult the pinned Lean statement, proof and application where helpful. Use ai agent’s announcement and Allahyar’s public reconstruction for orientation. At the point of use, record how much of the proof has been checked and state any residual implication precisely.

Have an independent subagent check every proof added or revised in this workflow. Give the checker the precise statement, the proof on the actual objects and the affected applications. For every suspected new result, give a fresh-context Astra reviewer the exact statement and necessary mathematical background, with no project memory or earlier verdicts. Ask for a comparison with mathematics established before the announcement and an assessment of the result’s intrinsic significance. A substantive idea, extension of uniformity or connection can merit candidacy even with a short proof. Use routine calculations, restatements and straightforward corollaries in the arguments they support.

Use an earlier result wherever it supplies the required implication. Narrow or remove a candidate accordingly, and state the remaining claim for a partial match. A new candidate used in the reconstruction still requires a proof. A claim of priority requires dated primary evidence of equivalent scope. A literature search records evidence about the sources checked. Label the list in both languages as AI-proposed candidates for new mathematics and organize it by mathematical topic. Keep candidate provenance and review history in the local records. Record independent subagent checks as AI checks and track proof status, priority and human specialist assessment separately.

## Keep the window data consistent

At the window application, fix the target, precision, family and common threshold before choosing an interval. At each real scale, supply the Fourier input from the lattice bound at every tied translate at that same scale. Use the same base Artin data, sampling degrees, weights and cutoff in both calculations.

## Maintain the portable edition

Keep the paper, proof map and editing instructions in English and the README in English and Chinese. When a candidate’s scope or status changes, update the paper’s opening, its point of use and both languages of the README. Keep `reading-guide.pdf`, the standalone editable `proof-map.html`, `README.md` and `AGENTS.md` with the sources and build files needed to regenerate the edition. Keep working notes, review records and build intermediates local.

Start with `tex/article.tex` and follow the README’s portable build instructions. Update `reading-guide.pdf` and `proof-map.html` together when changing a claim, dependency or passage. After either changes, run `python proof_map.py --update` and then `python proof_map.py`, and fix every reported error. Preserve their relative filenames and stable named destinations. Verify a clean rebuild and check the affected views and links offline after moving the PDF and HTML together.
