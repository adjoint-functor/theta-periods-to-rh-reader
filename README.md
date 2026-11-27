<a name="readme-en"></a>

# From Theta Periods to the Riemann Hypothesis

[<kbd>简体中文</kbd>](#readme-zh)

## How to contribute

- **AI4Math practitioners** can start with the [method in this README](#method) and the repository’s [AGENTS.md](AGENTS.md). Choose a step in the proof map and fill in a derivation or shorten its proof with a theorem from the literature. Update the paper and the map together, checking that the upstream conclusions still supply every input needed downstream.
- **Mathematicians** can go straight to the [AI-proposed candidates for new mathematics](#ai-proposed-candidates-for-new-mathematics). We collect these statements in one place so specialists can judge their mathematical value. Which parts already follow from the literature? If the remaining step introduces a new idea, reveals a connection or gives a stronger uniform estimate, why does that advance matter?

To suggest an improvement or share a review, [open a GitHub issue](https://github.com/adjoint-functor/theta-periods-to-rh-reader/issues/new) and point to the relevant step in the proof map or passage in the paper.

## About the reading edition

Our two goals are to reconstruct and check Levent Alpöge’s announced argument for the classical Riemann hypothesis in ordinary mathematical language and to identify its genuinely new mathematical contributions. The paper follows iterated theta lifts to a one-sided estimate for a centered prime-power sum and shows how that estimate excludes nontrivial zeta zeros off the critical line. Section 6 also gives the Mellin sign-change argument for primitive Dirichlet characters, assuming the corresponding window estimate for each target.

**[Open the interactive proof map online](https://adjoint-functor.github.io/theta-periods-to-rh-reader/)** · **[Read the paper online (825-page PDF)](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf)** · **[Download the offline reading edition (ZIP)](https://github.com/adjoint-functor/theta-periods-to-rh-reader/archive/refs/heads/main.zip)** · [View the proof map source](https://github.com/adjoint-functor/theta-periods-to-rh-reader/blob/main/proof-map.html)

For offline reading, extract the ZIP and open `proof-map.html` in your browser with `reading-guide.pdf` in the same folder.

## Method

The directed acyclic graph (DAG) tracks the actual dependencies of the classical RH proof in this reading edition at every level of detail. AI agents choose a step in the overview, refine it as needed and write its proof in the paper. Each substep records its precise inputs, conclusions and links to the paper. At each level the stated premises and upstream conclusions must jointly supply every downstream input. The objects, witnesses, data, normalizations and order of quantifiers must agree. The substeps must recover the parent conclusion on the same data under the original hypotheses. When a mathematical dependency changes, update the paper and the affected parts of the graph together and check the arrows at every affected level.

Where an earlier result applies, we check its hypotheses on the objects at hand and verify that its conclusion supplies the needed input. We then cite the precise result in the original literature. For the remaining steps we give mathematical derivations and consult the pinned Lean release where needed. We aim to reconstruct a proof that can be checked from the exposition and its primary references independently of Lean, and to identify results that go beyond previously established mathematics. Alpöge’s announcement and Sahibzada Allahyar’s public reconstruction guided the initial reading. [Alpöge’s announcement](https://alpo.ge/remark.pdf) · [Allahyar’s public reconstruction](https://github.com/sahibzada-allahyar/math/blob/rh-exposition-2026-11-20-r2/preprint/alpoge-riemann/reconstruction.pdf) · [Pinned Lean source](https://github.com/TomasOrtega/RH/tree/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean)

A result can merit a separate entry if it introduces a substantive idea, establishes a new connection or extends the range of a uniform estimate, even when its proof is short. Routine calculations, restatements and immediate corollaries belong at their point of use.

An independent agent checks each new or revised proof. A separate Astra reviewer assesses each proposed candidate against earlier mathematics in a fresh context.

### The S/W principle

Let $`S`$ be a stronger statement attributed to the original argument and $`W`$ a weaker statement proposed for one step of the classical proof.

1. **Establish what the source proves.**
2. **Check sufficiency and independent proof.**
3. **Use $`W`$ on the verified route.**
4. **Record unfinished proofs and review candidacy.**
5. **Withdraw an unsupported or refuted $`S`$.**
6. **Recheck the enclosing step if both routes fail.**

## Reading the proof map

The map opens on **Weighted square-scale route**, the argument in Part I. Select **Earlier window route** to follow the six sections of Part II. Part III of the paper collects the nineteen AI-proposed candidates. Select a step to see its inputs and conclusions. Use **+** to expand it, **Article** to open the relevant passage, and **Known results** to find the classical theorems used there. The **weighted proof map** link on the first page of the PDF returns to the map. [Weighted route](https://adjoint-functor.github.io/theta-periods-to-rh-reader/proof-map.html#weighted) · [Earlier window route](https://adjoint-functor.github.io/theta-periods-to-rh-reader/proof-map.html#window)

## Progress to date

### 22 November 2026 · Initial edition

We began by organizing the argument into a proof map that readers can expand step by step. At the levels shown in the map, we checked whether upstream conclusions and stated premises supply all the inputs needed downstream on the same data, with compatible normalizations and the required order of quantifiers. We then worked to fill in the arguments surrounding the candidates, giving direct derivations and citing the precise results from the primary literature wherever they apply. For example, Section 2 computes the auxiliary theta lift on the arithmetic columns, expressing each image in the prescribed basis of cusp forms. The resulting 448-page edition groups nineteen AI-proposed candidates by mathematical topic. [First public edition (v2026.11.22)](https://github.com/adjoint-functor/theta-periods-to-rh-reader/tree/v2026.11.22)

### 25 November 2026 · Revised edition

The 485-page revision addresses DavetheSlayer’s questions about the window argument and zero exclusion, draws on josephuniverse01-create’s coefficient-field and local-index arguments and foocker’s elementary-divisor comparison for the integral ramified kernel, and uses 仿射变换’s AI-assisted assessment of all nineteen candidates to check their scope. [Issue #1](https://github.com/adjoint-functor/theta-periods-to-rh-reader/issues/1) · [PR #2](https://github.com/adjoint-functor/theta-periods-to-rh-reader/pull/2) · [PR #3](https://github.com/adjoint-functor/theta-periods-to-rh-reader/pull/3)

The revision identifies both auxiliary section systems and the undivided ramified period lattice on one selected family. Under the S/W principle, the required lower slope bound follows directly from a quotient-lattice estimate. Fourier inversion uses the signed mean and the sampling estimates on the same translates at each real scale of the interval. These derivations simplify the proof of classical RH in the reading edition and narrow the remaining gaps in the natural-language proof. The paper marks the inputs that still come from the pinned Lean proof. [The two section systems](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.section-run-family-identification) · [Lower slope bound](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.ramified-kernel-lower-mean) · [Signed mean](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.classical-signed-mean)

### 26–27 November 2026 · The weighted prime-power argument

On 26 November we adopted the Lean revision of Alpöge’s argument by Luke Sernau and collaborators. On 27 November we completed the natural-language reconstruction of its weighted route. After fixing the precision and choosing an auxiliary quadratic character for the zero test, the argument needs an arithmetic estimate at just one square in each covering interval. At that square, the period and relative trace estimates enter a volume comparison on the same rows, giving a one-sided bound for the remainder in a weighted prime-power sum. Maximality and interpolation extend the estimates to all sufficiently large real scales, giving the bound used to exclude nontrivial zeta zeros off the critical line. [Formal source](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207)

The argument now forms Part I of the 825-page reading edition. Readers can check its derivations from the text and the cited primary literature. The Lean references identify their formal sources. Independent AI readers reviewed the key deductions, and we checked at each level of the map that the upstream conclusions and stated premises together supply every downstream input. Part II retains the earlier window argument. Both routes can be explored in the same map. The originality and mathematical significance of the nineteen AI-proposed candidates in Part III still await assessment by human specialists.

## AI-proposed candidates for new mathematics

The linked passages give the precise statements and their role in the argument. The list gives the statements in their current scope. Their priority and independent mathematical significance remain open to specialist assessment.

### Arithmetic windows and Galois cohomology

- **Uniform higher fine Selmer bounds.** The pinned Lean release gives a window for every primitive target. Fix the target, precision $`0\lt \varepsilon\lt 1/52`$ and dyadic profile. Choose $`J`$ before the auxiliary primes. For sufficiently large $`X`$ and each admissible pair at $`Z=X^{1/J}`$, one interval $`[W,W^2]\subseteq[Z,X]`$ works at every real $`y`$ in it. On the prescribed CM fields, sum the localization-kernel lengths over twists $`(-r)`$ with $`1\le r\lt \lfloor y^{401}\rfloor`$, weighting each coefficient prime $`\ell`$ by $`\log\ell`$. The bound is $`\exp(y^\varepsilon/2)`$ for every finite set of coefficient primes. Duality and $`K`$-theory give bounds at fixed field and twist. For classical zeta, the auxiliary quadratic prime sums are controlled by published estimates and the explicit formula. The Selmer input to integral division only ranges up to $`\lfloor x^{400}\rfloor`$ on the selected fields. Mizusawa’s class-group calculation and the two parity formulas control the dyadic contribution throughout this range. A separate estimate covers odd-primary terms with $`r[E_s:\mathbf Q]\le x^{\varepsilon/8}`$, where $`s`$ is the first layer through which the character factors. The remaining odd-prime plus sum on the same window still uses the release. [Classical residual](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.selmer-classical-residual) · [Dyadic bound](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.selmer-classical-all-layers) · [General statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.family)

- **Lifting integral finite cohomology classes with separated Hodge jumps.** Let $`T_1\twoheadrightarrow T_2`$ be a surjection of crystalline lattices at an unramified field of degree $`n`$ over $`\mathbf Q_\ell`$, $`\ell\ge11`$. The local question asks how much of $`H_f^1(T_2)`$ lifts integrally. Along the Frobenius cycle the large signed Hodge jumps may occur singly or in pairs, with at least $`j`$ small labels between successive groups. For target rank $`r`$, height $`H`$ bounding the full prescribed intervals and combined small width $`g`$, the bound on the cokernel length, normalized by the absolute ramification index of the coefficient field, is $`O((n+1)r[H/(\ell-1)^{j+1}+(g+1)(j+1)+\log_\ell\max(1,H)])`$. The dependence on cyclic spacing is the substantive point. The estimate supplies one inert-place contribution to the Hecke lattice comparison. Section 4 proves the estimate by lifting classes over each group of jumps, treating both orders of opposite signs and gluing without a loss for the number of groups. [Proof of the lifting bound](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.crystalline-cluster-lifting) · [Full hypotheses and application](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.crystalline-rows) · [Zhu, Theorem B](https://arxiv.org/pdf/0807.1078v3#page=3) · [Čoupek–Gazaki–Marmora, Corollary 3.16](https://arxiv.org/pdf/2603.26035v3#page=30)

- **Which torsion extensions come from fixed crystalline endpoints?** Let $`K/\mathbf Q_\ell`$ be unramified, $`\ell\ge5`$. Fix a crystalline $`\mathcal O`$-lattice $`T`$ for $`G_K`$ and crystalline characters $`\chi_c=\chi_1\varepsilon_\ell^{1-c}`$. The theorem prescribes their labelled Hodge jumps and separates the other jumps from explicit residue intervals. Let $`\lambda`$ be a uniformizer and $`X`$ a finite coefficient module. For all sufficiently large $`a`$ with $`\lambda^aX=0`$, require the extension of $`(\mathcal O/\lambda^a)(\chi_1)`$ by $`T\otimes X`$ to occur as a quotient of nested stable lattices. The ambient space is a finite direct sum of crystalline representations, each with the prescribed full jumps and residual characteristic polynomials. The classes passing this test are exactly the image of $`H_f^1(K,T(\chi_1^{-1}))\otimes X`$. For the higher character slots the image is zero, and for the first it is the unramified subgroup. Consequently congruent crystalline lattices of this labelled type have the same finite image modulo the congruence, even for some weight intervals wider than the Fontaine–Laffaille range. This supplies the zero local loss at the qualifying large primes. An earlier short crystalline result over $`\mathbf Q_\ell`$ constructs suitable endpoint lifts of residue-field extensions. [Statement and hypotheses](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.residual-crystalline-admissibility) · [Atobe et al., Lemma 7.6](https://arxiv.org/pdf/2306.07582v4#page=25)

- **Lifting integral finite classes at a prime of tame type.** For a surjection of stable lattices in potentially crystalline representations of $`G_{\mathbf Q_p}`$, assume that both tame inertial types use at most $`N`$ distinct characters in one Frobenius-stable set containing $`1`$. The signed filtration jumps lie in a common set of at most $`N+1`$ integers in $`[-\eta,H]`$ containing zero. Write $`q`$ for the largest Frobenius orbit of a ratio of the characters. For $`N\ge2`$, $`1\le\eta\lt H`$ and $`p\gt 40(HN^2+N^3)`$, the cokernel on integral $`H_f^1`$ is killed by $`p^{7(Nq+\eta(N+q))}`$. Once the prime meets this threshold, the exponent is independent of $`H`$, the tame splitting degree and the multiplicities. The two type primes in the argument require only $`q\le\lfloor N^2/4\rfloor`$ and the resulting rank-dependent length bound. Earlier Breuil–Kisin exactness gives an unspecified annihilator for the underlying module cokernel. The uniform bound for lifting finite classes is the candidate. [Local statement and proof](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.tame-type-lifting) · [Čoupek–Gazaki–Marmora, Proposition 3.4](https://arxiv.org/pdf/2603.26035v3#page=24)

- **Integral Selmer bounds for tame anticyclotomic twists.** Fix a place where the preliminary twist label differs from the base label. Take the finite collection of good cuspidal signatures there, with their prescribed odd-rank lattices, polarizations, Hodge gaps and local conditions. One tame character, anticyclotomic and trivial at every place over $`\ell`$, must work for all lattices and every power prime to $`\ell`$. The sum of the excesses of their normalized Selmer lengths above $`\nu_\ell`$ and the total tame inertia cost can both be made arbitrarily small. Here $`\nu_\ell=0`$ at odd primes and $`\nu_2=1`$ on the classical family. Section 4 obtains the required bounded-degree coefficients in the integral Selmer determinants on the same split prime pairs for the prescribed Galois representations. Simultaneous specialization gives the common character. The determinant computes the length for its prescribed Selmer condition. At an actual good Hecke point an injection gives the required upper bound. Section 4 identifies the common phase of the marked theta evaluations on all auxiliary covers and realizes the specialized columns in the prescribed twisted lattice. Its congruence index also uses estimates for local Galois cohomology. [Full statement and derivation](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.tame-selmer) · [Mazur–Rubin, Proposition 9.17 and Remark 10.4](https://arxiv.org/pdf/1503.04642v3) · [Smith, Theorem 2.14](https://arxiv.org/pdf/2207.05143v2#page=10)

### Theta and Bessel periods

- **Comparison of the prescribed tests across words.** At one selected translate, one finite adelic central element and one row isometry serve all lift words. Each word has a unitary column change and a nonzero scalar that work for every twisting tuple on the ramified columns and projected top rows. A positive power of the relative normalization ratio is rational and supported on the tuple’s twisting primes. For the prescribed finite-order twists the two level indices cancel, leaving a root of unity. Seesaw identities compare matched kernels, and the squared Bessel period formula applies to a fixed everywhere-tempered cuspidal representation with discrete Hermitian weak base change. The simultaneous comparison gives rank transfer through one row dual over the coefficient field and preserves valuations at the places avoided by the twists. [Precise statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.periods) · [Fixed-representation period formula](https://doi.org/10.1017/fmp.2025.8)

- **Complementary-frame transfer at a split place.** A prescribed integral test on one path around a theta-grid square gives a test on the other path by partial Fourier transforms and integration over complementary primitive frames. The transferred test has the required lattice support, congruence depth and level-character conditions, and its normalized local zeta section agrees with the complementary section with its determinant twist. Seesaw supplies the principle of comparing matched kernels. This local identification gives the matching needed for changing paths in the integral row tests. [Precise statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.transfer)

- **Detecting a smaller-group cusp form at the prescribed principal level.** Fix the precision and depth constant. Beyond one threshold for the admissible grids, let $`Y`$ be the bottom Hermitian space and $`V=Y\perp\langle1\rangle`$. Every nonzero cuspidal multiplicity map $`t`$ on $`U(Y)`$ of the prescribed real type at principal level $`(g_0g_1)`$ and every nonzero smooth real vector $`w`$ admits a test cusp form $`a`$ on $`U(V)`$ with a nonzero bilinear period against $`t(w)`$. The larger real type is specified, the testing vector is $`K_\infty`$-finite, and $`a`$ must have fixed vectors for the one principal level prescribed before $`t,w`$ vary. Both level characters are trivial. The substantive point is the uniform depth when the fields, ranks and weights vary together. Section 2 gives the proof on the prescribed grids. At a point where the row is large, it bounds the other terms of a Poincaré period by less than the stabilizer contribution. Compact averaging gives a test vector of the prescribed kind. The paper then proves that the descending lifts span the core tests and that the pairing survives ascent on the core tower. [Statement and argument](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.fixed-level-period) · [Global GGP comparison](https://www.numdam.org/articles/10.1007/s10240-021-00129-1/)

### Relative traces and automorphic multiplicities

Fix the selected family. At each selected translate the normalized Bessel Poincaré operators $`L_w`$ on the full columns have one Petersson target. Write $`d_w`$ for the full column dimension, $`D_\star`$ for the reference row dimension and $`b=\exp(x^\varepsilon)`$.

- **Mixed Gram estimate.** Beyond a common threshold the bound $`\lVert L_w^*L_v\rVert_{\mathrm{HS}}^2\le(1+b^{-6})d_wd_v/D_\star`$ holds for every distinct pair at every selected translate. Relative trace unfolding reindexes the terms by orbits, and local densities give the primitive counts. The uniform estimate uses the signed scalar main term and the signed sum over corank-one pairs failing local generation. The rank calculation uses their weighted sum over distinct pairs. [Precise statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.trace)

- **Same-word Gram defect.** For every word the mean-square defect $`\lVert L_w^*L_w-I\rVert_{\mathrm{HS}}^2/d_w`$ is at most $`e_0`$, with $`\sqrt{e_0}\le\exp(-x^{\varepsilon/8})`$ beyond a common threshold. Schur orthogonality supplies the identity term, and the other degenerate and nondegenerate orbits require uniform bounds. This controls the kernel and, with the ramified-column dimension, gives a nonzero reference pairing. [Precise statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.diagonal)

- **Uniform automorphic multiplicity count.** For the specified finite projector $`e`$ and discrete-series weights on $`U(p,q)`$ with $`q^2\le r=p+q`$, the reference count is the product of formal degrees, the adelic quotient volume and $`\Re e(1)`$. The relative error is at most $`\exp(-rf\log r/16)`$ as the unitary rank $`r`$ and the totally real base-field degree $`f`$ vary, within the prescribed level and weight-gap range. Known fixed-group estimates give precedents. For the rank argument, the full Gram moments supply a lower dimension bound. Upper bounds for the total and the two bad projectors, with their respective local masses, control the distinguished rows. [Precise statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.count)

### Integral lattices and divisibility

- **A short window for a perturbed determinant jet.** For a prime $`p\ge5`$, odd Frobenius distance $`h`$, matrix size $`r`$ and the stated perturbation bounds, every interval of $`\lceil64r^2(h+3+3\log_p(r+1))\rceil`$ consecutive nonnegative orders contains a jet whose valuation is at most zero after normalization by the specified power of $`p`$ and Cayley factorial. Cayley’s identity gives the factorial normalization, and finite differences use the bound on the perturbed Newton coefficients. The resulting short window gives an available integral-germ test for an odd Frobenius block. [Precise statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.jet)

- **Realizing Frobenius gains by division.** At a sufficiently large scale with the prescribed Artin data, weights and period maps, lower valuation bounds for the period values on the actual integral tests allow division by fractional ideals. The gap between the inertia-weighted ramp sum and the gains retained after restriction, and the allowance for lattice indices, satisfy the same uniform loss bound. Height, slope and CM-period comparisons then give the centered inequality $`D(u)\le E_x`$ at every tied translate with cutoff $`N=\lceil2a_E\rceil`$. Fourier inversion uses the signed mean of these quantities at one scale. On the classical family the local gain estimates and selected sampling data supply that mean directly. In §6 one family supplies the hypotheses throughout full intervals for use in the published Mellin sign-change argument. [Precise statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.gain)

- **Integral Weyl lattices at a single weight and prime.** Let $`\lambda=(a^t,\kappa)`$ be a dominant polynomial weight and use the same primitive highest vector for the Weyl lattice $`\Delta`$ and its contravariant dual $`\nabla`$. At grade $`i`$ form the monic least common multiple $`D_i(T)`$ of the content polynomials of the allowed $`i`$-box skew shapes that survive at $`T=a`$. If $`p^{e_L}`$ clears the quotient of the second-block dual Weyl lattice by the Weyl lattice at all weights up to a fixed integral depth cutoff measured with weakly decreasing integer coefficients, then $`p^{e_L+v_p(D_i(a))}\nabla(\lambda)_v\subseteq\Delta(\lambda)_v`$ at each weight of that grade within the same cutoff. The bound holds at singular specializations and at primes dividing $`i!`$. Even in a two-dimensional weight space, two distinct factors can each contribute a power of the same prime. Nakahama gives the rational scalars. The candidate concerns their denominators on the integral lattice. The weaker bound summed over primes that classical RH uses follows from the rational formula with ordinary integral bounds for its projectors. Historical priority for the sharper statement is open. [Precise weightwise bound and proof](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.integral-weyl-content) · [Nakahama, Theorem 1.2](https://arxiv.org/pdf/1506.05919#page=5)

- **Determinant divisibility in a formal group of mixed signature.** Let $`p`$ be odd. Over the valuation ring of an algebraically closed valued field of characteristic zero, let a commutative formal group have logarithmic characters $`\zeta\mapsto\zeta^{p^s}`$ for the action of $`\mu_{p^h-1}`$, with $`h\gt 0`$ even and each odd type of dimension at most $`j`$. Choose any integral frame of rank $`i`$ with a unit minor in one even type. For each $`c\ge1`$ the $`c`$-th power of the determinant of the invariant derivatives, one column per copy of the group, takes every integral germ at the origin to a value of valuation at least $`(i-r)cp/(p^2-1)-i^2(1+\log_p c)`$, where $`0\le r\le\min(i,j(3+\log_p c)/2)`$ and $`v(p)=1`$. The scalar height-two coefficient is classical. The candidate controls the number of directions that can lose that gain in an arbitrary mixed-type frame. On the arithmetic family a bounded number of stages suffices for the comparison at the small inert primes. Historical priority for the mixed-type bound is open. [Local statement and proof](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.mixed-determinant-depth) · [Katz, §V](https://www.numdam.org/article/AST_1977__41-42__55_0.pdf#page=9) · [Schneider–Teitelbaum, Appendix (c)](https://arxiv.org/pdf/math/0102012#page=33)

- **A Frobenius pairing on two prescribed tangent planes.** Take $`p\ge5`$ in the alternating cases of Section 4 with unramified CM action. Use the Raynaud chart with its biextension from the principally polarized abelian part and its $`p`$-unit level scalar $`G`$. The tangent ranks alternate between $`n+j`$ and $`j'`$. Fix two integral direct summands of rank $`n`$ in the paired large types $`a`$ and $`\overline{a+i}`$, for one odd $`0\lt i\lt D`$ in the full Frobenius cycle of length $`D`$. There are saturated subplanes of common rank at least $`\max(0,n-(i+1)j'-j)`$. In their formal logarithm coordinates, the bidegree $`(q,1)`$ component of the additive gauge $`Gh`$, with $`q=p^i`$, reduces to a perfect Frobenius pairing after multiplication by $`p^{1+(q-p)/(p^2-1)}`$. The weighted bound on the remainder on these same subplanes supplies an input to the determinant estimate. The residue of this scaled component is invariant under integral changes of rigidification. The pairing also gives exact valuations for the matched mixed derivatives in the normalized chart. Zink constructs the biextension from displays, and Weinstein finds related Frobenius terms in the reduced determinant on the height-two Lubin–Tate universal cover. The candidate concerns the joint rank, scaling and remainder estimates on the two prescribed planes. Historical priority remains open. [Local statement and proof](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.marked-frobenius-pairing) · [Zink, §4.3](https://www.numdam.org/article/AST_2002__278__127_0.pdf#page=113) · [Weinstein, Proposition 5.3.1](https://arxiv.org/pdf/1010.4241v3#page=44)

### Heights, section lattices and Fourier–Jacobi coefficients

- **Finite-degree bound for an adjoint section lattice.** On a nonterminal cover component $`Z`$, the lower bound for the degree of the actual adjoint section lattice in the prescribed metrics has leading Chow-height term $`q_Z\ell h_Z`$ at the specified degree $`\ell`$. It uses the rank comparison $`(1-z)r_Z\le q_Z\le r_Z`$, where $`q_Z=\binom{\ell-1}{s}d_Z`$ for the flag dimension $`s`$ and moving degree $`d_Z`$, $`r_Z`$ is the rank of the actual cusp lattice, and the prescribed loss $`z`$ is at most $`1/2`$. David–Philippon and Chen give earlier finite-degree determinant estimates using the Chow form. The narrower comparison concerns this selected degree and rank, with uniform control of the norm and index losses in transferring to the actual lattice. Descent and truncation turn the component bounds into covolume estimates for cusp sections in the indefinite tower. These enter the division estimates. A separate calculation gives the reference slopes of the definite column lattices. [Precise statement](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.height)

- **Arithmetic height of the full flag at a finite cutoff.** Fix an abelian CM field $`E`$ of degree $`2f`$, $`f\ge2`$, with $`E/E^+`$ unramified at every finite prime. Fix $`k_0=\mathbf Q(\sqrt{-d_0})\subset E`$ with $`d_0`$ prime and $`d_0\equiv7\pmod{16}`$, and choose the root with $`(1+\sqrt{-d_0})/2\in\mathcal O_E`$. Use the type induced by one embedding of $`k_0`$ and a nonterminal unitary cover of constant signature $`(p,q)`$ with $`q\ge1`$ and $`N=p+q\ge3q+1`$. Fix the good level $`M'`$ with $`A=1`$ and the compatible integral models before choosing the weight $`u`$ and cutoff $`B`$. Vary the integral flags at the exceptional primes and the primes up to $`B`$. The exceptional primes are the divisors of $`2\lvert\mathrm{disc}(E)\rvert M'`$ and number at most $`4fN^2`$. Take a strictly decreasing integral weight of arbitrary signs. Each of the last $`q`$ weights at a label must be separated from every other weight there by at least $`g\gt 0`$. The cutoff satisfies

  <div align="center">

  $$\displaystyle B+1 \gt 4fN^2 \left(1+\frac{\lVert u\rVert_\infty}{g}\right).$$

  </div>

  Write $`\Delta_\tau=\max_i u_{\tau i}-\min_i u_{\tau i}`$ for the spread of the weights at $`\tau`$. The mean height, weighted by the component volumes, satisfies

  <div align="center">

  $$\displaystyle H_B(u) \ge -C\left(\Lambda_B\lVert u\rVert_1 + q\sum_\tau \Delta_\tau\right),$$

  </div>

  where $`\chi_{d_0}`$ is the quadratic character of $`k_0`$, $`\mathrm{rd}(E)`$ is the root discriminant of $`E`$, and

  <div align="center">

  $$\displaystyle \Lambda_B = \log(B\cdot\mathrm{rd}(E)) + \left|\Re\frac{L'(1,\chi_{d_0})}{L(1,\chi_{d_0})}\right|.$$

  </div>

  This supplies a geometric input to the finite-degree estimate for sections. The paper computes the change on the common finite model when a good prime is added, including its toroidal boundary, and bounds the resulting prime tail. On these same components it compares mixed intersections for the limiting Hodge metric. Testing weights on the walls of the dominant chamber and calibrating the two surviving determinant terms gives the bound at the original cutoff. The application to the section lattice also uses a finite-place trace and section norms. Historical priority is open. [Statement and mathematical status](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.flag-height)

- **Detecting a prescribed low Fourier–Jacobi coefficient at a CM boundary.** Fix a rank-one cusp direction on either nonterminal principal-level unitary cover and a positive frequency of trace at most the cutoff. If the coefficient of a cusp section there is nonzero, a one-parameter degeneration with CM abelian part and torsion extension data detects it. One Laurent coefficient and one monomial in the tangent-frame variables define a linear test that kills every section with zero coefficient at the specified frequency and direction. The torsion denominator and the lengths of the CM tangent generators are controlled uniformly as the field, rank, level, cutoff and weight vary. The same test controls finite denominators and complex norms. This gives a lower bound for the first minimum after quotienting by the sections with all low coefficients zero. Earlier work uses Heegner points to estimate integral differentials on Shimura curves and torsion specializations to test Siegel Jacobi forms. [Statement, sizes and proof](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.cm-boundary-fourier-jacobi) · [Pasten, §§13–14](https://arxiv.org/pdf/1705.09251v4#page=58) · [Richter–Westerholt-Raum, proof of Proposition 2.4](https://arxiv.org/pdf/1501.07733v1#page=5)

## Rebuilding the PDF

Run `python build.py` in this folder to compile `tex/article.tex` into `reading-guide.pdf`. The build uses Python 3.9 or later and TeX Live with XeLaTeX, Libertinus, `libertinust1math` and PGF/TikZ.

## License and attribution

Future revisions to the paper and proof map will appear on `main`. Cite the first edition of this reconstruction as *From Theta Periods to the Riemann Hypothesis*, by the Theta Periods to RH Reading Edition contributors (22 November 2026). [Dated first edition](https://github.com/adjoint-functor/theta-periods-to-rh-reader/tree/v2026.11.22)

The reading edition’s original paper, TeX sources and figures, the prose in `README.md` and `AGENTS.md`, and the mathematical graph and index content in the `proof-data` block of `proof-map.html` are available under Creative Commons Attribution 4.0 International (CC BY 4.0). The original code in `build.py`, the static entry page `index.html`, and the proof map’s HTML, CSS and JavaScript viewer are available under the MIT License. [CC BY 4.0 legal code](LICENSES/CC-BY-4.0.txt) · [MIT License](LICENSES/MIT.txt)

These licenses apply to the extent the contributors hold rights to license the material. Third-party sources, quotations and fonts remain subject to their respective terms. [License scope](LICENSE)

<a name="readme-zh"></a>

# 从 theta 周期到黎曼猜想

[<kbd>English</kbd>](#readme-en)

## 如何参与

- **AI4Math 工作者**可参照本 README 的[工作方法](#method-zh)和仓库中的 [AGENTS.md](AGENTS.md)，选取证明图中的一步，补全推导，或用文献中适用的定理简化证明。请同步更新正文和证明图，并核对上游结论是否仍能给出下游所需的全部输入。
- **数学同行**可以直接评议 [AI 建议的新数学候选](#candidates-zh)。我们把这些命题从整套论证中单列出来，方便同行按专长判断其数学价值。哪些部分可由已有文献推出？若余下的一步引入了新思路、揭示了新的联系，或给出了更强的一致估计，这一进展为何重要？

欢迎[新建 GitHub Issue](https://github.com/adjoint-functor/theta-periods-to-rh-reader/issues/new) 分享改进建议或评议意见，并注明对应的证明图节点或正文段落。

## 关于本阅读版

我们的两个目标是用通常的数学语言重构并核查 Levent Alpöge 公布的经典黎曼猜想论证，以及辨认其中真正新增的数学结果。正文从迭代 theta 提升推到中心化素数幂和的单侧估计，再说明如何用这个估计排除临界线外的非平凡 ζ 零点。第 6 节也给出本原 Dirichlet 特征的 Mellin 变号论证，对每个特征都以相应的区间估计为前提。

**[在线打开交互式证明图](https://adjoint-functor.github.io/theta-periods-to-rh-reader/)** · **[在线阅读英文论文（PDF，825 页）](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf)** · **[下载离线阅读版（ZIP）](https://github.com/adjoint-functor/theta-periods-to-rh-reader/archive/refs/heads/main.zip)** · [查看证明图源码](https://github.com/adjoint-functor/theta-periods-to-rh-reader/blob/main/proof-map.html)

离线阅读时，解压 ZIP 后用浏览器打开 `proof-map.html`，并将 `reading-guide.pdf` 留在同一目录。

<a name="method-zh"></a>

## 工作方法

有向无环图（DAG）在每一层都按本阅读版中经典黎曼猜想证明的实际依赖绘制。AI 智能体先从总览中选取一步，按需细化，在正文写出证明。图中列出各子步骤的确切输入、结论及正文链接。无论展开到哪一层，所列前提与上游结论合起来都须给出下游所需的全部输入。所用对象、具体选取、数据、归一化及量词顺序须相符。细化后的子步骤须使用相同数据，在原假设下推出原结论。数学依赖发生变化时，同步修订正文和证明图中相应的部分，并核对各个受影响层级上的推导关系。

可用已有定理时，先核对所用对象满足其假设，并确认它的结论给出了所需的输入，再引用原始文献中的确切结论。其余步骤给出数学推导，必要时查阅固定版本的 Lean 源码。我们的目标是重构一份可凭正文和所引原始文献独立于 Lean 核查的证明，并辨认哪些结果超出了已有的数学。初读时参考了 Alpöge 的公告和 Sahibzada Allahyar 的公开重构稿。[Alpöge 的公告](https://alpo.ge/remark.pdf) · [Allahyar 的公开重构稿](https://github.com/sahibzada-allahyar/math/blob/rh-exposition-2026-11-20-r2/preprint/alpoge-riemann/reconstruction.pdf) · [固定版本的 Lean 源码](https://github.com/TomasOrtega/RH/tree/a6ac91a412dcbaab31801355ec5707024a71bf65/extracted/lean)

一个结果即使推导简短，只要引入有分量的新思路、建立新的数学联系，或扩大一致估计的适用范围，就可以单列为候选。例行计算、改述和直接推论放在用到它们的地方。

新增或改写的证明由独立智能体复核。每项新数学候选另由 Astra 在没有项目记忆的新上下文中对照已有数学评议。

### S/W 原则

设 $`S`$ 是归于原论证的较强命题， $`W`$ 是拟在经典黎曼猜想证明的某一步采用的较弱命题。

1. **核对原论证证明了什么。**
2. **核对 $`W`$ 是否够用，以及能否独立推出。**
3. **在核实的推导中采用 $`W`$。**
4. **记录待补的证明，另行评议候选。**
5. **撤下缺乏依据或已被反例否定的 $`S`$。**
6. **两种命题都无法给出所需输入时，复查上一级推导。**

## 阅读证明图

证明图默认打开 **Weighted square-scale route**，对应正文第一部分的加权路线。选择 **Earlier window route**，可阅读第二部分的六个窗口论证专题。第三部分汇集此前由 AI 提出的十九项新数学候选。点开图中的一步可查看输入与结论。用 **+** 展开推导，点 **Article** 跳到正文，**Known results** 栏列出这一步用到的经典定理。PDF 首页的 **weighted proof map** 链接可返回证明图。[加权路线](https://adjoint-functor.github.io/theta-periods-to-rh-reader/proof-map.html#weighted) · [原有窗口路线](https://adjoint-functor.github.io/theta-periods-to-rh-reader/proof-map.html#window)

## 当前进展

### 2026 年 11 月 22 日 · 首版

我们先把论证整理成可逐层展开的证明图，在目前展示的各层核对上游结论与所列前提能否在同一组数据下给出下游所需的全部输入，并检查归一化与量词顺序是否相符。随后，我们着重补写候选命题以外的推导，对可由已有定理给出的步骤注明原始文献中的确切出处。例如，第 2 节逐列计算辅助 theta 提升，以指定的尖点形式为基写出各算术列向量经提升后的坐标。这份阅读版共 448 页，按数学主题列出 AI 提出的十九项候选。 [公开首版（v2026.11.22）](https://github.com/adjoint-functor/theta-periods-to-rh-reader/tree/v2026.11.22)

### 2026 年 11 月 25 日 · 修订版

485 页版回应了 DavetheSlayer 关于区间估计和零点排除的疑问，采用了 josephuniverse01-create 关于系数域和局部指数的论证、foocker 对分歧整核所作的初等因子比较，并参考了仿射变换借助 AI 对全部十九项候选所作的评议，核对各命题的适用范围。[Issue #1](https://github.com/adjoint-functor/theta-periods-to-rh-reader/issues/1) · [PR #2](https://github.com/adjoint-functor/theta-periods-to-rh-reader/pull/2) · [PR #3](https://github.com/adjoint-functor/theta-periods-to-rh-reader/pull/3)

修订稿在同一个选定的算术族上确定了两套辅助截面和除法前用于周期配对的分歧格。按照 S/W 原则，所需的斜率下界可直接由商格估计推出。对区间内每个实尺度，Fourier 反演在同一组平移上使用带符号均值和采样估计。这些推导简化了阅读版中的经典黎曼猜想证明，进一步缩小了自然语言证明中尚存的缺口。正文标明了仍由固定版本的 Lean 证明给出的输入。[两套辅助截面](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.section-run-family-identification) · [斜率下界](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.ramified-kernel-lower-mean) · [带符号均值](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.classical-signed-mean)

### 2026 年 11 月 26–27 日 · 加权素数幂和路线

11 月 26 日，我们引入 Luke Sernau 等人对 Alpöge 论证的 Lean 改写，27 日完成了加权主线的自然语言重构。给定精度后，先选定零点检验所用的辅助二次特征，再在每个覆盖区间选一个平方数作算术估计。在这个平方点上，周期与相对迹的估计通过同一组行进入体积比较，给出加权素数幂和余项的单侧上界。利用选点的极大性和插值，可将估计推广到所有充分大的实数尺度，进而排除临界线外的非平凡 ζ 零点。[形式化来源](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207)

这条论证现列在 825 页综合阅读版的第一部分，读者可以凭正文和所引原始数学文献逐段核查。Lean 引用标明形式化来源。独立的 AI 审读者复核了关键推导，我们也逐层核对了证明图中上游结论和已列明的前提能否共同给出下游所需的全部输入。第二部分保留原有的窗口路线，两条路线可在同一张互动图中切换阅读。第三部分列出的十九项新数学候选由 AI 提出，其原创性和数学价值仍待人工审核。

<a name="candidates-zh"></a>

## AI 建议的新数学候选

各条链接指向命题的精确陈述及其在论证中的用处。名单采用本版核定的命题范围。文献优先性和独立数学价值仍待同行评议。

### 算术区间与 Galois 上同调

- **高阶细 Selmer 群的一致界。** 固定版本的 Lean 给出了对每个本原特征都适用的窗口。固定目标、精度 $`0\lt \varepsilon\lt 1/52`$ 和二次幂层的选择规则，再于选取辅助素数前确定 $`J`$。 $`X`$ 充分大时，在 $`Z=X^{1/J}`$ 处给定任一对符合要求的辅助素数，都有一个区间 $`[W,W^2]\subseteq[Z,X]`$，其中每个实数 $`y`$ 都适用同一结论。在指定的 CM 域上，对 $`1\le r\lt \lfloor y^{401}\rfloor`$ 的 Tate 扭曲 $`(-r)`$ 求局部化核长度之和，再对任意有限组系数素数 $`\ell`$ 按 $`\log\ell`$ 加权求和，总和至多为 $`\exp(y^\varepsilon/2)`$。对偶与 $`K`$ 理论给出固定数域和固定扭曲下的界。对经典 ζ，辅助二次特征的素数和由已有估计与显式公式控制。整除步骤所需的 Selmer 估计只用到选定数域上的 $`\lfloor x^{400}\rfloor`$ 截断。Mizusawa 的类群计算和两种奇偶情形的公式给出这整个范围内的 $`2`$-主估计。若特征标首次经过第 $`s`$ 层分解，且 $`r[E_s:\mathbf Q]\le x^{\varepsilon/8}`$，相应的奇素数项也有独立估计。同一窗口上余下的奇素数正特征空间之和仍调用原 Lean 结果。[剩余估计](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.selmer-classical-residual) · [逐层估计](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.selmer-classical-all-layers) · [一般陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.family)

- **Hodge 跳跃分隔时整有限上同调类的提升。** 设 $`K/\mathbf Q_\ell`$ 为 $`n`$ 次非分歧扩张， $`\ell\ge11`$，给定晶体表示的稳定格满射 $`T_1\twoheadrightarrow T_2`$。问题是 $`H_f^1(K,T_2)`$ 中有多少类能整地提升。沿 Frobenius 的循环顺序，大的带符号 Hodge 跳跃可单独或成对出现，相邻两组之间至少有 $`j`$ 个小指标。设目标格的秩为 $`r`$，所有指定区间端点的绝对值上界为 $`H`$，三个小宽度参数之和为 $`g`$。余核长度除以系数域的绝对分歧指数后，至多为 $`O((n+1)r[H/(\ell-1)^{j+1}+(g+1)(j+1)+\log_\ell\max(1,H)])`$。值得单列的是，指标在 Frobenius 循环上的间隔能压低大跳跃的代价。第 4 节给出这项惰性位估计的证明。论证逐组提升上同调类，分别处理正、负跳跃的两种次序，再拼合各组的提升，所得界不随组数累加。[提升估计的证明](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=proof.crystalline-cluster-lifting) · [完整假设与用法](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.crystalline-rows) · [Zhu 的定理 B](https://arxiv.org/pdf/0807.1078v3#page=3) · [Čoupek–Gazaki–Marmora 的推论 3.16](https://arxiv.org/pdf/2603.26035v3#page=30)

- **哪些挠扩张来自指定的晶体表示格？** 设 $`K/\mathbf Q_\ell`$ 为非分歧扩张， $`\ell\ge5`$。固定 $`G_K`$ 的晶体表示及其稳定 $`\mathcal O`$-格 $`T`$，并固定一列晶体特征标 $`\chi_c=\chi_1\varepsilon_\ell^{1-c}`$。定理对每个嵌入的 Hodge 跳跃及其模 $`\ell`$ 的剩余类给出明确的分离条件。取 $`\mathcal O`$ 的素元 $`\lambda`$ 和有限 $`\mathcal O`$-模 $`X`$。一个上同调类给出短正合列 $`0\to T\otimes X\to E_a\to(\mathcal O/\lambda^a)(\chi_1)\to0`$。要求对一切充分大且满足 $`\lambda^a X=0`$ 的 $`a`$，中间项 $`E_a`$ 都能写成两个相嵌的稳定格之商。这些格位于晶体表示的直和里，每个直和项均须具有指定的全部跳跃和剩余特征多项式。满足条件的扩张类恰为 $`H_f^1(K,T(\chi_1^{-1}))\otimes X`$ 的像。把 $`T`$ 换成较高的特征标时，所得群为零。对首个特征标，所得群是非分歧子群。因此，同一 Hodge 型的两个晶体格若模某个素元幂同余，它们的有限子群在该精度下也有相同的像。结论覆盖某些超出 Fontaine–Laffaille 范围的权，并使符合条件的大素数处的局部损失为零。此前 Atobe 等人在 $`\mathbf Q_\ell`$ 上的短晶体范围内，为剩余域上的扩张选取了适当的两端提升。[精确条件和命题](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.residual-crystalline-admissibility) · [Atobe 等，引理 7.6](https://arxiv.org/pdf/2306.07582v4#page=25)

- **温和惯性型下整有限上同调类的提升。** 给定 $`G_{\mathbf Q_p}`$ 的潜在晶体表示之间的稳定格满射。设两端的惯性型都取自同一个 Frobenius 稳定的温和特征标集合，该集合含平凡特征标，大小至多为 $`N`$。两端的滤过跳跃均取自 $`[-\eta,H]`$ 中同一个含零的整数集，其大小至多为 $`N+1`$。设 $`q`$ 是任意两个特征标之商的 Frobenius 轨道长度的最大值。若 $`N\ge2`$、 $`1\le\eta\lt H`$ 且 $`p\gt 40(HN^2+N^3)`$，则 $`p^{7(Nq+\eta(N+q))}`$ 消去整 $`H_f^1`$ 映射的余核。一旦素数达到阈值，这一指数与正端点 $`H`$、温和分裂域的次数以及特征标和跳跃的重数无关。论证在指定惯性型的两个素数处只用到 $`q\le\lfloor N^2/4\rfloor`$ 及由此得到的依赖目标秩的长度界。已有的 Breuil–Kisin 函子正合性结果给出底层模余核的某个零化子。这里单列的候选是对有限上同调类整提升的一致定量控制。[局部命题与证明](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.tame-type-lifting) · [Čoupek–Gazaki–Marmora，命题 3.4](https://arxiv.org/pdf/2603.26035v3#page=24)

- **温和分歧的反循环扭曲下，整 Selmer 群的长度上界。** 固定一个预备扭曲标记有别于基准标记的位。取该位上符合条件的有限组尖点表示，以及指定的奇数秩格、极化、Hodge 跳跃间隙和局部条件。要找到一个温和分歧的反循环特征标，使它在 $`\ell`$ 上方每个分解群上平凡，并使同一个特征标对这组格及所有素于 $`\ell`$ 的幂次都适用。各个 Selmer 群归一化长度超出 $`\nu_\ell`$ 的部分之和，以及所有分歧点的惯性代价，都可以任意小。在经典 ζ 所用的数域上，奇素数处 $`\nu_\ell=0`$，而 $`\nu_2=1`$。第 4 节对满足所列假设的 Galois 表示，在同一批成对的分裂素点上取得每个整 Selmer 行列式所需的低赋值有界次数系数，同时特化便给出共同特征标。行列式给出指定局部条件下的 Selmer 长度，实际 Hecke 计算所需的上界由一个单射得到。第 4 节比较了各辅助覆盖上带标记的 theta 取值，得到同一个归一化相位，并用指定扭曲格的整向量实现了特化后的列。这个格的同余指数还用到局部 Galois 上同调的估计。[完整命题与推导](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.tame-selmer) · [Mazur–Rubin，命题 9.17 与注 10.4](https://arxiv.org/pdf/1503.04642v3) · [Smith，定理 2.14](https://arxiv.org/pdf/2207.05143v2#page=10)

### Theta 与 Bessel 周期

- **不同提升序列的指定测试数据比较。** 在同一个选定平移处，对所有提升序列可用同一个有限阿代尔中心元和同一个行空间等距映射。每个序列有各自的酉列变换和非零标量，对所有扭曲元组、分歧列与投影后的顶层行都适用。相对归一化比值的某个正整数幂为有理数，其非零素赋值只出现在该元组的扭曲素数处。对指定的有限阶扭曲，两个层级指数恰好抵消，比值是单位根。Seesaw 恒等式比较匹配的核，Bessel 周期模平方公式适用于固定的处处柔曼尖点表示，条件是它具有离散 Hermitian 弱基变换。上述同时比较可在系数域上通过同一个行对偶转移秩，并在扭曲素数避开的有限位保持赋值。[固定表示的周期公式](https://doi.org/10.1017/fmp.2025.8) [精确陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.periods)

- **分裂位的互补标架转移。** 在 theta 提升网格的一个方格中，给定一条路径上的整测试函数，通过局部部分 Fourier 变换及对互补本原标架积分，构造另一条路径上的测试函数。它满足所需的格上支撑、同余深度、水平和特征标条件，其归一化局部 zeta 截面等于经行列式扭曲的互补小截面。Seesaw 提供比较匹配核的原理。这里的局部识别给出整行测试改变路径所需的具体匹配。 [精确陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.transfer)

- **在预定的主同余水平上检测较小酉群的尖点形式。** 固定精度和深度常数。对超过同一阈值的所有容许网格，设 $`Y`$ 为底层 Hermitian 空间， $`V=Y\perp\langle1\rangle`$。在 $`U(Y)`$ 上，任取指定实型、主同余水平 $`(g_0g_1)`$ 的非零尖点重数映射 $`t`$，以及该实表示空间的任一非零光滑向量 $`w`$，都能在 $`U(V)`$ 上找到尖点形式 $`a`$，使它与 $`t(w)`$ 的双线性周期非零。较大群的实型已经指定，测试向量须为 $`K_\infty`$-有限，且 $`a`$ 在选取 $`t,w`$ 之前确定的主同余子群下不变。两边的水平特征标均平凡。这里值得单列的是数域、秩与权同时变化时，所需的水平深度仍能一致控制。第 2 节给出适用于指定网格的证明。在底层形式取值较大的一点，估计表明 Poincaré 周期中其余项之和的绝对值严格小于稳定子项的绝对值。再对极大紧子群作平均，就得到所需的测试向量。正文随后证明下降提升张成核心测试空间，并把非零配对沿核心塔传递。[命题与推导](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.fixed-level-period) · [与整体 GGP 定理的比较](https://www.numdam.org/articles/10.1007/s10240-021-00129-1/)

### 相对迹与自守重数

固定所选族。在每个选定平移处，定义在完整列空间上的归一化 Bessel–Poincaré 算子 $`L_w`$ 有同一个 Petersson 目标空间。记 $`d_w`$ 为完整列空间的维数， $`D_\star`$ 为参考行维数，且 $`b=\exp(x^\varepsilon)`$。

- **不同提升序列之间的 Gram 估计。** 过了同一个阈值，任一选定平移处的不同序列都满足 $`\lVert L_w^*L_v\rVert_{\mathrm{HS}}^2\le(1+b^{-6})d_wd_v/D_\star`$。相对迹展开按轨道重排，局部密度给出本原计数。一致估计用到带符号的标量主项，以及未满足局部生成条件的余秩一配对的带符号和。秩估计使用的是对不同序列对求和得到的加权混合项。 [精确陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.trace)

- **同一提升序列的 Gram 偏差。** 过了同一个阈值，每个序列的均方偏差 $`\lVert L_w^*L_w-I\rVert_{\mathrm{HS}}^2/d_w`$ 都至多为 $`e_0`$，其中 $`\sqrt{e_0}\le\exp(-x^{\varepsilon/8})`$。Schur 正交关系给出恒等项，其余退化与非退化轨道需要一致估计。所得界控制核的维数，与分歧列空间的维数合用可给出非零的参考配对。 [精确陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.diagonal)

- **自守重数的一致计数。** 对 $`U(p,q)`$ 上指定的有限位投影 $`e`$ 和离散系列权，设 $`q^2\le r=p+q`$。参考计数是形式度、阿代尔商的体积与 $`\Re e(1)`$ 的乘积。在所规定的水平和权间距范围内，酉群的秩 $`r`$ 和全实基域的次数 $`f`$ 可同时变化，相对误差至多为 $`\exp(-rf\log r/16)`$。固定群的已有估计提供了先例。秩论证从完整 Gram 矩得到维数下界，再用总维数和两个例外投影各自的上界及相应局部质量控制指定行。 [精确陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.count)

### 整格与整除性

- **扰动行列式射流的短区间。** 对素数 $`p\ge5`$、奇 Frobenius 距离 $`h`$、矩阵维数 $`r`$ 以及满足所列系数界的扰动，每段长为 $`\lceil64r^2(h+3+3\log_p(r+1))\rceil`$ 的连续非负整数阶中，都有一个射流在用规定的 $`p`$ 的幂和 Cayley 阶乘归一后，赋值至多为零。Cayley 恒等式给出阶乘归一化，有限差分法用到扰动后的 Newton 系数界。这个短区间为奇 Frobenius 块提供一个可用的整芽测试。 [精确陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.jet)

- **通过除法实现 Frobenius 增益。** 在充分大的尺度上，使用指定的 Artin 数据、权重和周期映射，在实际整测试格上给出周期值的赋值下界，从而可以按分式理想作除法。按惯性群加权的分段线性项之和与限制后保留的增益之差，以及格指数所致的损失，都满足同一个一致误差界。结合高度、斜率和 CM 周期的比较，可在共用截断 $`N=\lceil2a_E\rceil`$ 下对每个相配平移推出中心化不等式 $`D(u)\le E_x`$。Fourier 反演实际使用同一尺度上这些量的带符号平均。对经典 ζ 族，局部增益估计和选定的采样数据可直接给出这个平均的上界。第 6 节选取同一个族，使所需假设在整个区间上成立，再用于已发表的 Mellin 变号论证。 [精确陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.gain)

- **单个素数、单个权空间上的整 Weyl 格。** 设 $`\lambda=(a^t,\kappa)`$ 是占优多项式权，Weyl 格 $`\Delta`$ 和逆变对偶格 $`\nabla`$ 采用同一个本原最高权向量。对第 $`i`$ 层，取所有在 $`T=a`$ 处仍有贡献的允许斜形，每个斜形含 $`i`$ 个方格。设其内容多项式的首一最小公倍式为 $`D_i(T)`$。取由弱递减整数组给出的深度及一个整数截断。若 $`p^{e_L}`$ 能消去第二块在截断以内各权上的对偶 Weyl 格对 Weyl 格的商，则在该层同一深度截断内的每个权 $`v`$ 上，有 $`p^{e_L+v_p(D_i(a))}\nabla(\lambda)_v\subseteq\Delta(\lambda)_v`$。奇异特化和整除 $`i!`$ 的素数也适用。即使权空间只有二维，两个不同的多项式因子也可能各贡献一次同一素数。Nakahama 已给出各等型分量上范数之比的公式。这里的候选是对整格分母的逐权控制。经典 RH 论证仅需对素数求和的较弱界，由该有理公式和投影算子的常规整分母估计即可得到。较强结论的文献优先性尚待考证。[逐权命题及证明](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.integral-weyl-content) · [Nakahama，定理 1.2](https://arxiv.org/pdf/1506.05919#page=5)

- **带奇偶分型的形式群上不变微分算子行列式的整除性。** 设 $`p`$ 为奇素数，在特征零代数闭赋值域的赋值环上取一个交换形式群。设它带有 $`\mu_{p^h-1}`$ 的作用， $`h\gt 0`$ 为偶数。在对数坐标中，第 $`s`$ 型上的特征标为 $`\zeta\mapsto\zeta^{p^s}`$，其中 $`s\bmod h`$。各奇数型的切空间维数至多为 $`j`$。在任一偶数型中选取 $`i`$ 个整切向量，要求它们有一个 $`i`$ 阶子式是单位。在形式群的 $`i`$ 个副本上，把沿这些向量的不变微分算子排成矩阵，每个副本对应一列。对每个 $`c\ge1`$，其行列式的 $`c`$ 次幂作用于任一整函数芽，在原点得到的值满足赋值下界 $`(i-r)cp/(p^2-1)-i^2(1+\log_p c)`$。这里 $`0\le r\le\min(i,j(3+\log_p c)/2)`$，且 $`v(p)=1`$。一维高度二形式群的系数 $`p/(p^2-1)`$ 已有经典结果。候选的内容是对任意这样的混合型标架，一致控制可能损失这部分整除性的方向数。在选定的算术族上，较小惰性素数处的比较只需有界个步骤。该混合型结论的文献优先性尚待考证。[局部命题及证明](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.mixed-determinant-depth) · [Katz，第五节](https://www.numdam.org/article/AST_1977__41-42__55_0.pdf#page=9) · [Schneider–Teitelbaum，附录 (c)](https://arxiv.org/pdf/math/0102012#page=33)

- **两个给定切平面上的 Frobenius 配对。** 在第 4 节 CM 型交替的情形下，考虑 $`p\ge5`$ 处的非分歧 CM 作用。在 Raynaud 坐标邻域上使用由主极化阿贝尔部分给出的双扩张，水平标量 $`G`$ 为 $`p`$-单位。切空间维数交替为 $`n+j`$ 和 $`j'`$。在长为 $`D`$ 的 Frobenius 轨道上固定一个奇数 $`0\lt i\lt D`$，并在相配的两个大维数型 $`a`$ 与 $`\overline{a+i}`$ 中各给定一个秩 $`n`$ 的整直和因子。从两个给定平面中可以各选一个饱和子平面，两者同秩，且秩至少为 $`\max(0,n-(i+1)j'-j)`$。在形式群对数坐标中，令 $`q=p^i`$。将双扩张的加性函数乘以 $`G`$，再将双次数 $`(q,1)`$ 的部分乘以 $`p^{1+(q-p)/(p^2-1)}`$，约化后得到完美的 Frobenius 半线性配对。在这两个子平面上还得到余项的加权系数界，可用于行列式估计。这个归一化分量的剩余类在整刚化变换下不变。配对还给出归一化坐标中相配方向上混合导数的精确赋值。Zink 已用 display 构造这一类双扩张。Weinstein 在高度二 Lubin–Tate 形式模的普适覆盖上，将行列式约化后得到过形状相近的 Frobenius 项。这里列为候选的是两个给定切平面上的秩下界、整归一化与余项估计合在一起的结论，首创性尚待考证。[局部命题及证明](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.marked-frobenius-pairing) · [Zink，第 4.3 节](https://www.numdam.org/article/AST_2002__278__127_0.pdf#page=113) · [Weinstein，命题 5.3.1](https://arxiv.org/pdf/1010.4241v3#page=44)

### 高度、截面格与 Fourier–Jacobi 系数

- **伴随线丛截面格的有限次数界。** 在覆盖的非终端分量 $`Z`$ 上，取指定的次数 $`\ell`$ 和度量，实际伴随线丛截面格的度下界以 Chow 高度项 $`q_Z\ell h_Z`$ 为主项。这里 $`q_Z=\binom{\ell-1}{s}d_Z`$，其中 $`s`$ 是旗簇维数， $`d_Z`$ 是动线性系的次数。记实际尖点截面格的秩为 $`r_Z`$，则须有 $`(1-z)r_Z\le q_Z\le r_Z`$，其中给定的相对秩损失 $`z\le1/2`$。David–Philippon 与 Chen 已用 Chow 形给出有限次数的行列式估计。这里较窄的比较要求在选定次数与秩下，一致控制转到实际格时的范数和指数损失。经下降和截断后，各分量上的界给出不定酉群塔中尖点截面格的余体积估计，供除法估计使用。定号酉群一侧列格的参考斜率另行计算。 [精确陈述](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.height)

- **有限截断下全旗簇的算术高度。** 取 $`2f`$ 次阿贝尔 CM 数域 $`E`$，要求 $`f\ge2`$，且 $`E/E^+`$ 在所有有限素位均非分歧。固定虚二次数域 $`k_0=\mathbf Q(\sqrt{-d_0})\subset E`$，其中 $`d_0`$ 是满足 $`d_0\equiv7\pmod{16}`$ 的素数，并选定平方根，使 $`(1+\sqrt{-d_0})/2\in\mathcal O_E`$。取由 $`k_0`$ 的一个嵌入诱导的 CM 型及各无穷位符号均为 $`(p,q)`$ 的非终端酉群覆盖，要求 $`q\ge1`$ 且 $`N=p+q\ge3q+1`$。先固定辅助参数为 $`A=1`$ 的好水平 $`M'`$ 和相容的整模型，再选权 $`u`$ 与截断值 $`B`$。在例外素数与不超过 $`B`$ 的素数处更换整旗。例外素数是 $`2\lvert\mathrm{disc}(E)\rvert M'`$ 的素因子，其数目至多为 $`4fN^2`$。取各分量严格递减的整权，分量可为正、零或负。每一标号下最后 $`q`$ 个权中的任一个与同一标号下其余每个权的间距至少为 $`g\gt 0`$。截断值满足

  <div align="center">

  $$\displaystyle B+1 \gt 4fN^2 \left(1+\frac{\lVert u\rVert_\infty}{g}\right).$$

  </div>

  记 $`\Delta_\tau=\max_i u_{\tau i}-\min_i u_{\tau i}`$ 为标号 $`\tau`$ 处最大权与最小权之差。以各分量的几何体积加权得到的平均高度满足

  <div align="center">

  $$\displaystyle H_B(u) \ge -C\left(\Lambda_B\lVert u\rVert_1 + q\sum_\tau \Delta_\tau\right),$$

  </div>

  这里用 $`\chi_{d_0}`$ 表示 $`k_0`$ 的二次特征标，用 $`\mathrm{rd}(E)`$ 表示 $`E`$ 的根判别式，并取

  <div align="center">

  $$\displaystyle \Lambda_B = \log(B\cdot\mathrm{rd}(E)) + \left|\Re\frac{L'(1,\chi_{d_0})}{L(1,\chi_{d_0})}\right|.$$

  </div>

  这给出了有限次数截面估计需要的一项几何输入。正文已算出加入一个好素数给共同有限整模型的交数带来的改变，涵盖环面边界，并由此控制了其余素数的可求和尾项。正文在同一批分量上比较了极限 Hodge 度量的混合交数，再由优势室壁上的权和两项行列式高度得到原截断处的下界。用于截面格时还要计入有限处的迹和截面范数。首创性尚待考证。[完整命题与证明进展](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.flag-height)

- **在 CM 边界检测一个指定的低阶 Fourier–Jacobi 系数。** 在非终端阶段的任一主同余水平酉群覆盖上，固定一个秩一尖点方向和一个迹不超过截断值的正频率。若尖点截面在这里的系数非零，就能选取一个单参数退化，使其阿贝尔部分有复乘、扩张数据为挠元，并从中读出这个系数的非零性。具体做法是取一个 Laurent 系数，再取切标架变量的一个单项式系数。这样得到的线性泛函在所有指定系数为零的截面上消失。即使数域、秩、水平、截断和权同时变化，仍可一致控制挠元的分母与 CM 切向生成元的长度。用同一泛函估计有限处的分母和无穷处的范数，可给出商格的第一极小值下界，其中取商时除去所有低阶系数均为零的截面。已有的相关工作包括以 Heegner 点估计志村曲线上的整微分，以及用挠点特化检测 Siegel 理论中的 Jacobi 形式。[精确陈述、参数范围及证明](https://adjoint-functor.github.io/theta-periods-to-rh-reader/reading-guide.pdf#nameddest=candidate.cm-boundary-fourier-jacobi) · [Pasten，第 13–14 节](https://arxiv.org/pdf/1705.09251v4#page=58) · [Richter 与 Westerholt-Raum，命题 2.4 的证明](https://arxiv.org/pdf/1501.07733v1#page=5)

## 重新编译 PDF

在本目录运行 `python build.py`，即可将 `tex/article.tex` 编译为 `reading-guide.pdf`。需要 Python 3.9 或以上版本，以及配有 XeLaTeX、Libertinus、`libertinust1math` 和 PGF/TikZ 的 TeX Live。

## 许可与署名

论文和证明图的后续修订将发布在 `main` 分支。引用本阅读版首版时，请著录为 *From Theta Periods to the Riemann Hypothesis*, by the Theta Periods to RH Reading Edition contributors（2026 年 11 月 22 日）。[首版（2026 年 11 月 22 日）](https://github.com/adjoint-functor/theta-periods-to-rh-reader/tree/v2026.11.22)

本阅读版的原创论文、TeX 源文件和图表、`README.md` 与 `AGENTS.md` 的说明文字，以及 `proof-map.html` 中 `proof-data` 数据块里的数学证明图与索引内容，采用知识共享署名 4.0 国际许可协议（CC BY 4.0）。`build.py` 中的原创代码、静态入口页 `index.html` 及证明图查看器的 HTML、CSS 和 JavaScript 实现采用 MIT 许可证。[CC BY 4.0 许可原文](LICENSES/CC-BY-4.0.txt) · [MIT 许可证](LICENSES/MIT.txt)

上述许可适用于贡献者有权许可的原创材料。第三方来源、引文和字体仍适用各自的权利与许可条款。[许可范围](LICENSE)
