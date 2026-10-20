# Lagrangian planes, Gaussian lines and reduction

This route connects the linear geometry of Lagrangian planes to Gaussian symbols, symplectic reduction and the integer Maslov index. The proofs are developed in three programme lessons:

| Lesson | Mathematical role | Solved exercises |
| --- | --- | --- |
| [Gaussian lines, densities and invariant symbols](../../reconstructions/20261005-restored-gaussian-symbols/gaussian-lines-and-invariant-symbols.html) | Symmetric graph charts, the Gaussian solution line, critical densities and the signature cocycle | Five |
| [Reducing Gaussian symbols and composing linear relations](../../reconstructions/20261005-restored-linear-reduction/reduction-and-linear-symbol-composition.html) | Radical densities, the invariant reduction map and clean linear composition | Six |
| [Maslov index, crossings and global phase](../../reconstructions/20261005-restored-maslov-topology/maslov-index-crossings-and-global-phase.html) | Integer classification of loops, signed crossings and ordered line transport | Fourteen |

The [reading map](reading-map.json) gives the precise proof locators and source versions for this route. All results below have their proofs in those lessons.

## 1. Symmetric matrices describe nearby planes

Let \(S\) be a real symplectic space of dimension \(2n\). Use
\[
 \omega=\sum_jd\xi_j\wedge dx_j,\qquad
 \lambda_0=\{x=0\},\qquad D=-i\partial.
\]
A plane transverse to \(\lambda_0\) is a graph \(\xi=Cx\), where \(C\) is real symmetric. The set of these planes is an affine space modelled on symmetric matrices. The graph charts give the Lagrangian Grassmannian dimension \(n(n+1)/2\). Their transitions are rational on the domains where the required graph projection is invertible.

The stratum with intersection dimension \(k\) with a fixed plane has codimension \(k(k+1)/2\). The corank-one stratum is a hypersurface; intersection dimension at least two has codimension at least three. Compact graph covers prove the relevant null-volume assertion and give a common complement to any countable collection of planes.

Read Gaussian Sections 1–2, proofs **GS:Z0–GS:Z3**. Their distribution argument also characterizes the Gaussian line by every linear equation \(\ell(x,D)u=0\) whose symbol vanishes on the plane.

## 2. The Gaussian coefficient separates into two factors

Choose a horizontal plane \(H\) transverse to both \(\lambda_0\) and \(\lambda\). Write \(\lambda=\{(B\xi,\xi)\}\), with \(B=B^T\). Its normalized Gaussian is
\[
 u_B(x)=c(2\pi)^{-3n/4}
 \int e^{i(x\cdot\xi-\xi^TB\xi/2)}\,d\xi\ |dx|^{1/2}.
\]
Singular \(B\) is included: its kernel contributes a delta layer, and its nonsingular part gives an ordinary Fresnel factor. The proof first determines all distributional solutions with compact tests, establishes temperedness and then applies Fourier inversion.

The symbol attached to this expression is \(c|d\xi|^{1/2}\) on the plane. Under a new horizontal reference \(H'=\{\xi=Ax\}\), the positive determinant change belongs to the half density. The remaining factor is
\[
 c_{H'}=i^\sigma c_H,\qquad
 \sigma=\frac12\operatorname{sgn}
 \begin{pmatrix}-A&I\\I&-B\end{pmatrix}.
\]
These integers satisfy an exact cocycle identity. They define the Maslov line \(M\) and the identification
\[
 \mathcal I(\lambda)\simeq
 M(\lambda)\otimes\Omega^{1/2}(\lambda).
\]
Here \(\Omega(V)\) is the line of translation-invariant densities on \(V\).

Read Gaussian Sections 2–4, proofs **GS:Z2–GS:Z6**. Section 5, **GS:Z7–GS:Z9**, treats general quadratic phases, critical densities and the signature difference between representations, including changes in the number of phase variables.

## 3. A phase radical retains a density

For a quadratic phase \(Q(x,\theta)\), its pure phase radical is
\[
 R=\{r:Q_{x\theta}r=0,\ Q_{\theta\theta}r=0\}.
\]
The critical map has kernel \(R\). Quotienting its critical space by \(R\) gives the same Lagrangian as any complementary nondegenerate phase.

The Gaussian therefore takes values in \(\mathcal I(\lambda)\otimes\Omega(R)\). A compact test on \(R\) gives a finite pairing. Translations along \(R\) and the density exact sequence prove independence of the projection and complement. If the integral keeps its original number of phase variables, removing an \(e\)-dimensional radical leaves a scalar normalization \((2\pi)^{-e/2}\).

Read Reduction Section 1, **LR:R0–LR:R1**, and Exercise 9.1 for an explicit coupled phase and its radical density.

## 4. Reduce the plane, density and phase together

Let \(\Delta\subset S\) be isotropic. Put
\[
 d=\dim\Delta,\qquad
 k=\dim(\Delta\cap\lambda_0),\qquad
 K=\lambda\cap\Delta,\qquad e=\dim K.
\]
The reduced symplectic space and plane are
\[
 S_\Delta=\Delta^\omega/\Delta,\qquad
 \lambda_\Delta=(\lambda\cap\Delta^\omega)/K.
\]
Two exact sequences and the perfect symplectic quotient pairing give the positive geometric map
\[
 \Omega^{1/2}(\lambda)\longrightarrow
 \Omega^{1/2}(\lambda_\Delta)\otimes
 \Omega(K)\otimes\Omega^{-1/2}(\Delta).
\]
Gaussian reduction has the same density Jacobians and the additional positive factor
\[
 (2\pi)^{(d-2k-2e)/4}.
\]
Its unit-modulus factor transports the Maslov line.

In the adapted coordinates \(x=(x',y,z)\), \(\xi=(\xi',\eta,\zeta)\), the constraint has coordinates \((\xi',z)\); its orthogonal is \(x'=\zeta=0\). The operation sets \(x'=0\) and treats \((z,\theta)\) as phase variables. Its pure radical is exactly the geometric intersection \(K\).

The construction is smooth on families of constant \(e\), including changes in the rank of the pure phase Hessian. Direct and staged reductions agree for every isotropic flag, with all density identifications and normalization ratios retained.

Read Reduction Sections 2–6, **LR:R2–LR:R9**. Exercises 9.2–9.4 compute vertical, horizontal, coupled and staged reductions.

## 5. The middle diagonal gives clean composition

For linear canonical relations \(G_1\subset S_1\times S_2\) and \(G_2\subset S_2\times S_3\), use the symplectic signs \(\omega_1-\omega_2\) and \(\omega_2-\omega_3\). In their product the constraint is the middle diagonal. Its intersection with \(G_1\times G_2\) is the excess space
\[
 N=\{s_2:(0,s_2)\in G_1,\ (s_2,0)\in G_2\}.
\]
Here \(d=2n_2\), \(k=n_2\) and \(e=\dim N\). The reduction factor becomes \((2\pi)^{-e/2}\), and the output retains a full density on \(N\). The middle symplectic volume specifies the contraction intrinsically.

A graph factor has zero excess. Its density contraction transports the other relation's half density, and the identity Gaussian preserves its density and Maslov unit.

Read Reduction Sections 7–8, **LR:R10–LR:R11**, with the excess-one and identity examples in Exercises 9.5–9.6. Analytic composition adds the estimates and support hypotheses developed in the programme's analytic-composition lessons.

## 6. A loop carries an integer

For \(n\ge1\), use the compatible complex coordinate \(z=x-i\xi\). If \(U\) is a unitary real frame for a Lagrangian plane, the determinant square \(\det_{\mathbb C}(U)^2\) is independent of the chosen frame. Its winding classifies the entire fundamental group:
\[
 \pi_1(\mathcal L(S))\simeq\mathbb Z.
\]
The positive generator is
\[
 \gamma_+(t)=\operatorname{span}(\cos\pi t,-\sin\pi t)
 \oplus\mathbb R_x^{\,n-1}.
\]
Its determinant square makes one positive full turn. In dimension zero the plane space is a point.

The topology proof supplies smoothing with fixed base point, compact submersion lifting and the connected, simply connected fiber \(SU(n)/SO(n)\). Read Maslov Sections 2–4, **MT:T0–MT:T3**, **MT:G0–MT:G4** and **MT:W0–MT:W6**.

## 7. Crossings compute the integer

At a crossing with a reference plane, extend \(v\) to a differentiable section \(v(t)\) of the moving Lagrangian. The intrinsic crossing form is \(q(v)=\omega(v,\dot v)\). In the graph \(x=A(t)\xi\), it is \(A'(t)\) restricted to \(\ker A(t)\).

Every continuous loop has a smooth representative with finitely many simple crossings. Their signs sum to its integer index \(\nu\). A regular multiple crossing contributes its crossing-form signature. The complete Schur-complement derivative fixes the sign even when the normal determinant is negative.

Read Maslov Sections 1, 5 and 6, **MT:C0–MT:C1**, **MT:P0** and **MT:B0–MT:B7**. The proof uses the full phase-branch jump and a supported common-complement shear. Exercises 9.3–9.8 give exact derivative, splitting, winding and noncommuting-matrix calculations.

## 8. Fix the transport direction

With the coefficient transition \(c_{H'}=i^\sigma c_H\), forward flat transport keeps coefficients constant on each chart segment and applies that transition at each switch. Its loop multiplier and the reciprocal values are
\[
 \operatorname{Hol}_{M}=i^{-\nu},\qquad
 \operatorname{Hol}_{M^*}=i^\nu,\qquad
 e_{H'}=i^{-\sigma}e_H.
\]
For \(\gamma_+\), the two ordered coefficient switches have exponents \(-1,0\), giving \(-i\). The ordered reciprocal frame changes give \(i\). These formulas specify the meaning of each multiplier.

Read Maslov Section 7, **MT:I0–MT:I4**, and Exercise 9.9. Sections 8–9 include direct sums, an index-four loop with trivial fourth-root transport, and an ordinary Lagrangian curve whose tangent-plane loop has index two.

## Sources and editable material

The primary mathematical source for this route is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, Springer eBook ISBN 978-3-540-49938-1, 2007, Section 21.6, printed pages 328–346. The Gaussian-symbol lesson also develops the principal-symbol construction of Hörmander IV, Section 25.1.

Editable sources: [Gaussian symbols](../../reconstructions/20261005-restored-gaussian-symbols/gaussian-lines-and-invariant-symbols.md), [linear reduction](../../reconstructions/20261005-restored-linear-reduction/reduction-and-linear-symbol-composition.md), [Maslov topology](../../reconstructions/20261005-restored-maslov-topology/maslov-index-crossings-and-global-phase.md), and [this guide](guide.md). The linked lessons retain their original illustrations, reproducible figure sources and component notices.

Guide text: GPT-6.1 Sol (OpenAI). Independent guide expression is CC0-1.0 to the extent rights exist. Linked components retain their own terms.
