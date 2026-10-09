# Tensor wavefront and the exact projection converse

This companion retains the complete Section 18.4, equations WF8–WF10, from AN03-U012, *Detecting regularity without choosing coordinates*, in *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Its mathematical body is unchanged.

Principal author entity: AN-03 course-writing task, 2026. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. This extract with exact prerequisite bindings was prepared by the AN-04 course-writing task and OpenAI Codex, 5 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## Exact current prerequisite bindings

The tensor product and exact support formula used in WF8–WF9 are the full iterated-pairing and support proofs GK25 in [Scalar kernels and strong topology, Section 13.6](../20261005-restored-analytic-composition/scalar-kernels-and-strong-topology.md). Their displayed order is output then input; WF8 uses the stated input-coordinate order and the actual coordinate permutation.

The compact finite-order estimate, polynomial Fourier bound and cutoff convolution estimate called WF2 in the retained text are proved in [Coordinate transport and directional localization, T0 and W1](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md). In particular, W1 allows a smaller product cutoff after any original cutoff nonzero at the point and shrinks the frequency cone correctly. The underlying Fourier inversion and distributional compatibility are [L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md). Smooth product integration is [M4](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md), with the exact compact parameter derivative rule in the FTC contract.

Thus all inputs of the retained proof are actual included earlier programme proofs. The [proof map](proof-map.json) gives exact locators, source hashes and transitive dependencies. WF10 proves equality for the constant factor; no equality for two arbitrary singular factors is inferred.

### 18.4. Products and the exact projection converse

For compact localizations \(v\) on \(\mathbb R^a\) and \(w\) on \(\mathbb R^b\), their already constructed tensor product has

\[
\widehat{v\otimes w}(\xi,\eta)=\widehat v(\xi)\widehat w(\eta).
\tag{WF8}
\]

Here the order of the two factors is input-coordinate order, as indicated by the variables; converting to the geometric chapter's output-then-input notation requires that actual permutation. The equality follows by its two original iterated test pairings and the factored exponential.

Write \(Z_u=\{(x,0):x\in\operatorname{supp}u\}\). Then

\[
\operatorname{WF}(u\otimes v)
\subset
\bigl((\operatorname{WF}(u)\cup Z_u)
      \times(\operatorname{WF}(v)\cup Z_v)\bigr)
          \setminus\{(\xi,\eta)=(0,0)\}.
\tag{WF9}
\]

Outside the product support the tensor distribution vanishes, by the proved exact support formula. At a point inside it but outside the displayed covector set, at least one nonzero component is a regular direction for its factor. Near that pair direction its length is at least a fixed positive fraction of the total frequency length. Its factor in WF8 decreases to every order, while the other has its original polynomial bound. Their product therefore decreases to every order in that product cone. Product spatial cutoffs are equal to one near the base point, so this proves the claimed inclusion with the correct original Fourier definition. WF2 then handles all smaller nonproduct cutoffs. No general equality for two arbitrary singular factors is asserted.

For the original projection \(\pi(x,y)=x\), define \(\pi^*u=u\otimes1\) by
\(\langle\pi^*u,f\rangle=\langle u,x\mapsto\int f(x,y)dy\rangle\). The integral test is smooth with compact support and every \(x\)-derivative is its actual integrated derivative, so this is a continuous distribution. The constant factor is smooth, and WF9 gives one inclusion in

\[
\operatorname{WF}(\pi^*u)
 =\{(x,y;\xi,0):(x,\xi)\in\operatorname{WF}(u)\}.
\tag{WF10}
\]

For the converse suppose \(\pi^*u\) is regular at \((x_0,y_0;\xi_0,0)\). By WF2 choose product cutoffs \(\alpha(x),\beta(y)\) supported in that regular base neighborhood, both equal to one near their respective points, with \(\beta\geq0\) and \(\int\beta>0\). Their full transform is
\(\widehat{\alpha u}(\xi)\widehat\beta(\eta)\). The regular cone contains \((\xi,0)\) for all \(\xi\) in a smaller cone about \(\xi_0\). Its restriction at \(\eta=0\) is the original nonzero scalar \((\int\beta)\widehat{\alpha u}(\xi)\). Division by that scalar proves rapid decrease of the original factor, contradicting singularity at \((x_0,\xi_0)\). This proves the exact converse, not only the forward inclusion.

