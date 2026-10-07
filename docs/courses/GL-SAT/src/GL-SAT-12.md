# Consequences and examples

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The coefficient \(q+1\) in the simplest spherical Hecke product counts intermediate lattices. In the sheaf calculation it comes from the two cohomology groups of a projective line. Passing between these descriptions requires retaining both the perverse shift and the Frobenius action on the top cohomology group. This lesson calculates the point counts and proper-fibre traces explicitly, derives the corresponding IC identifications under a stated purity hypothesis, and proves the general Hall–Littlewood character transition. The remaining IC stalk and Whittaker comparisons are then stated with their hypotheses.

## 1. Frobenius, shifts and half twists

Let \(G\) be split and connected reductive over \(\mathbf F_q\), with a split maximal torus \(T\subset B\). Write \(N\) for the unipotent radical of \(B\), \(L=X_*(T)\), and

\[
d_\lambda=\langle2\rho,\lambda\rangle,
\qquad h_\nu=\langle2\rho,\nu\rangle.
\]

Here \(\lambda\) is dominant, whereas \(\nu\) can be any coweight. Fix \(\ell\ne\operatorname{char}\mathbf F_q\) and a finite extension \(E/\mathbf Q_\ell\) containing a square root \(a\) of \(q\). Choose an embedding of the algebraic numbers involved into \(\mathbf C\) for which \(a=\sqrt q>0\). All Frobenius operators below are **geometric** Frobenius. Thus \(E(1)\) has eigenvalue \(q^{-1}\).

Use the rank-one Weil object with eigenvalue \(a^{-1}\) to define \(E(1/2)\). The notation \((d/2)\) means its \(d\)-th tensor power, including negative powers. This choice concerns the Weil structure; it does not change the underlying geometric sheaf. Define

\[
\mathrm{IC}^{\mathrm{raw}}_\lambda
 =j_{\lambda!*}E[d_\lambda],
\qquad
\mathcal I_\lambda
 =\mathrm{IC}^{\mathrm{raw}}_\lambda(d_\lambda/2).
\tag{1.1}
\]

The first object has the constant Weil structure on its open orbit. The second is the usual weight-zero normalization when the IC purity theorem applies. The phrase “weight zero” means that its degree-\(i\) stalk cohomology has weights at most \(i\), and the corresponding dual inequalities hold; it does not mean that Frobenius is the identity in every degree.

For a Weil complex \(K\) and \(x\in Y(\mathbf F_q)\), put

\[
t_K(x)=\sum_i(-1)^i
 \operatorname{Tr}(F_x;H^i(K_{\bar x})).
\tag{1.2}
\]

We use bounded complexes with finite-dimensional stalks. The shift convention is \(H^i(K[r])=H^{i+r}(K)\).

**Lemma 1.1.** Trace functions are additive on distinguished triangles and multiply on tensor products. Moreover

\
t_{K[r}=(-1)^r a^{-s}t_K.
\tag{1.3}
\]

**Proof.** For an invariant subspace \(U\subset V\), choose a basis of \(U\) and extend it to one of \(V\). The Frobenius matrix is block triangular, so its trace is the sum of the traces on \(U\) and \(V/U\). Apply this to kernels and images in the finite long exact cohomology sequence of a triangle. Adjacent image terms have opposite signs and cancel. This proves additivity. Over a field, the cohomology of the tensor product of two bounded complexes is the direct sum of their cohomology tensor products: split each complex into its cohomology and two-term contractible summands. The trace on \(V\otimes W\) is \(\operatorname{Tr}(F_V)\operatorname{Tr}(F_W)\), as a product basis shows. Multiplying the alternating sums proves the tensor assertion. A shift changes the sign by \((-1)^r\), and the Weil twist multiplies every eigenvalue by \(a^{-s}\). \(\square\)

These calculations agree with Perverse sheaves, D-modules and the function-sheaf dictionary, §§1–2. Its general pushforward formula has an additional trace-theorem premise. In the explicit convolution below we compute every fibre's cohomology, so no all-dimensional trace formula is needed for that product.

On \(\mathrm{Gr}^{\lambda}(\mathbf F_q)\), formula (1.1) gives

\[
t_{\mathcal I_\lambda}=(-1)^{d_\lambda}a^{-d_\lambda}.
\tag{1.4}
\]

It vanishes outside \(\mathrm{Gr}^{\leq\lambda}\). Consequently, whenever these IC objects are defined with finite-dimensional stalks, their trace functions are a basis of the finitely supported spherical functions. Indeed their expansion in orbit indicators is triangular, with nonzero diagonal entries (1.4). Every interval below a dominant coweight is finite, by Orbits and Schubert varieties, §3; inversion of a finite triangular matrix on each such interval proves both spanning and independence.

## 2. The quadratic cone in étale coefficients

The small Schubert surfaces for \(SL_2\) and \(GL_2\) have the same singularity. Their two-stratum geometry, coordinates and resolution are proved in Orbits and Schubert varieties, §§4–5. We now give the IC deduction in étale coefficients under explicit supported-purity comparisons, including the characteristic-two quotient geometry.

The exact finite pushforward and geometric stalk formula are proved in Pushforward, pullback and finite morphisms, Theorem 4.1. Its Theorem 6.2 proves topological invariance. The additional purity comparisons used for the IC and exceptional-curve calculations are the following premise, at finite coefficients \(\Lambda_m=\mathbf Z/\ell^m\):

**Purity premise (P12).** The plane origin has supported orientation
\[
i_{(0,0)}^!\Lambda_{m,\mathbf A^2}
 =\Lambda_m(-2)[-4],
\]
given by the composite of the two coordinate Kummer orientations. For the exceptional curve \(D\) in the smooth cone resolution of §4,
\[
i_D^!\Lambda_m=\Lambda_{m,D}(-1)[-2],
\]
with forget-support map restricting to \(c_1(\mathcal O_D(-2))\). These identifications and their orientation maps commute with reduction in \(m\) and, for the split models, with geometric Frobenius. Their rational realization respects these supported triangles and closed restriction.

The curve calculation in Poincaré duality for curves, Lemma 4.2 gives
\[
i_0^!E_{\mathbf A^1}=E(-1)[-2]
\tag{2.0}
\]
from the punctured strict trait and its Kummer boundary. To pull that localization triangle along \(\mathbf A^2\to\mathbf A^1\), one must additionally compare the complementary open direct image. The curve calculation alone does not establish that comparison, or the line-bundle version used for \(D\). Those comparisons are included in (P12), whose general ground-field proof remains an input. Under (P12), the orientation lines are the reductions of free \(\mathbf Z_\ell\)-lines with surjective transitions, so inverse limit and tensoring with \(E\) give the displayed rational formulas without a derived-limit obstruction.

Let

\[
C=\operatorname{Spec}k[x,y,z]/(xy-z^2),
\qquad
\pi:\mathbf A^2\longrightarrow C,
\quad (u,v)\longmapsto(u^2,v^2,uv),
\tag{2.1}
\]

where \(k\) is algebraically closed of any characteristic different from \(\ell\). The map is finite: its source algebra is generated by the integral elements \(u,v\), satisfying the displayed square equations. The complement of the vertex in \(C\) is smooth. If \(\operatorname{char}k\ne2\), this follows from the derivatives \(y,x,-2z\). If \(\operatorname{char}k=2\), the only point with \(x=y=0\) is the vertex, because \(z^2=xy\).

**Proposition 2.1 (conditional cone calculation).** Under the plane-origin part of (P12), for rational étale coefficients,

\[
\mathrm{IC}_C=E_C[2].
\tag{2.2}
\]

Under its Frobenius-compatible form, the equality also respects the constant Weil structure over \(\mathbf F_q\).

**Proof.** First suppose the characteristic is odd. The involution \(\sigma(u,v)=(-u,-v)\) has quotient (2.1). To see the invariant algebra directly, a monomial \(u^iv^j\) is invariant exactly when \(i+j\) is even. If both exponents are even it is a monomial in \(x,y\); if both are odd, factor out \(z\). The sole relation is \(z^2=xy\), as the resulting even and odd monomial lists are linearly independent in \(k[u,v]\).

The natural map

\[
E_C\longrightarrow(\pi_*E_{\mathbf A^2})^{\sigma}
\tag{2.3}
\]

is an isomorphism on geometric stalks. Off the vertex, the two points of a fibre are exchanged; at the vertex, its reduced fibre is a single point. In both cases the invariant locally constant functions are one copy of \(E\), and (2.3) sends a scalar to that constant function. Since \(2\) is invertible in \(E\), taking invariants is the direct summand given by \((1+\sigma)/2\).

Let \(i\) be the vertex and \(i'\) its closed inverse image. The latter is the thickened origin \(\operatorname{Spec}k[u,v]/(u^2,v^2,uv)\). Its étale topos is that of its reduced point, by topological invariance, and sections with support depend only on that closed complement. Thus its exceptional restriction can be computed at the reduced origin. Finite pushforward is exact. Its costalk comparison is

\[
i^!\pi_*E\simeq\pi_{0*}i'^!E.
\tag{2.4}
\]

Here \(\pi_0\) is the finite map of the fibres at the origin, whose étale site is that of a point. For completeness, test (2.4) by an arbitrary complex \(M\) on that point. Closed extension and inverse image satisfy \(\pi^*i_*M=i'_*\pi_0^*M\), checked on geometric stalks. The two adjunctions then give

\[
\operatorname{Hom}(M,i^!\pi_*E)
 =\operatorname{Hom}(\pi^*i_*M,E)
 =\operatorname{Hom}(M,\pi_{0*}i'^!E).
\]

Yoneda proves the comparison, including its equivariance.

The plane-origin hypothesis gives \(i'^!E=E(-2)[-4]\). The involution acts as the identity on this one-dimensional orientation space. One can check this without a degree convention: the origin's orientation is the composite of the two supported Kummer orientations of the coordinate divisors. Replacing a coordinate \(u\) by \(-u\) changes its Kummer class by that of the constant \(-1\); the latter has an \(\ell^n\)-th root in \(k\) and hence zero Kummer class. Each orientation, and therefore their composite, is fixed. Taking the summand in (2.3) and (2.4) gives

\[
i^*E_C=E,
\qquad i^!E_C=E(-2)[-4].
\tag{2.5}
\]

In characteristic two, (2.1) is a universal homeomorphism. For every algebraically closed extension field a point of \(C\) has a unique lift: take the unique square roots of \(x,y\); their product is the unique square root of \(z^2\), hence equals \(z\). The map is finite and universally bijective, so it is integral, radicial and surjective. Topological invariance makes \(\pi^*\) and \(\pi_*\) inverse exact equivalences. Thus \(E_C=\pi_*E\), and (2.4) again gives (2.5).

Now put \(K=E_C[2]\). On the smooth open surface it is perverse. At the vertex its stalk has only degree \(-2\), and its costalk has only degree \(2\). These satisfy the perverse conditions, with strict inequalities at the boundary. They also exclude any perverse quotient or subobject supported at the vertex, respectively. The intermediate-extension characterization proved in Intermediate extensions and intersection complexes, §1 therefore identifies \(K\) with \(j_{!*}E[2]\). All maps and the averaging projector are defined over \(\mathbf F_q\), and the isomorphism is the identity on the open stratum. Uniqueness of intermediate extension makes it Frobenius compatible. \(\square\)

This proof uses characteristic-zero coefficients even when the ground field has characteristic two. With coefficients of characteristic two, the averaging projector in the odd-characteristic quotient calculation is unavailable; the assertion is not an integral IC calculation.

## 3. Point counts and the two smallest IC functions

The point counts in this section are unconditional. The quadratic-cone IC function uses Proposition 2.1 under (P12). The minuscule projective-line and central-point functions need only the curve and point calculations.

For \(SL_2\), the quasi-minuscule Schubert variety has one vertex and an open stratum which is an affine-line bundle over \(\mathbf P^1\). An affine-line bundle over an \(\mathbf F_q\)-point has \(q\) rational points: its fibre is an affine line, since the one-dimensional vector space and its translation torsor over a field are trivial. Thus

\[
\#\mathrm{Gr}_{SL_2}^{\leq\alpha^\vee}(\mathbf F_q)
 =1+q(q+1)=q^2+q+1.
\tag{3.1}
\]

Equivalently the three cells in Orbits and Schubert varieties, §4 have \(q^2,q,1\) points. Counting the whole closure includes the vertex.

For \(GL_2\), write \(c_{ab}\) for the indicator of the double coset with dominant coweight \((a,b)\). Normalize Haar measure by \(\operatorname{vol}GL_2(\mathbf F_q[[t]])=1\). The Satake transform \(\mathcal S\) is the one proved and computed in Spherical Hecke algebras as functions on the affine Grassmannian, §§4–5:

\[
\begin{aligned}
\mathcal S(c_{10})&=a(x_1+x_2),\\
\mathcal S(c_{20})&=q(x_1^2+x_2^2)+(q-1)x_1x_2,\\
\mathcal S(c_{11})&=x_1x_2.
\end{aligned}
\tag{3.2}
\]

The first closure is \(\mathbf P^1\), so \(\mathcal I_{10}=E_{\mathbf P^1}1\). The second closure has open orbit \((2,0)\) and closed central point \((1,1)\), with the cone chart (2.1) at that point. Proposition 2.1 and the smooth open chart identify its IC with the shifted constant sheaf. The central point has dimension zero. Consequently

\[
\begin{aligned}
t_{\mathcal I_{10}}&=-a^{-1}c_{10},\\
t_{\mathcal I_{20}}&=q^{-1}(c_{20}+c_{11}),\\
t_{\mathcal I_{11}}&=c_{11}.
\end{aligned}
\tag{3.3}
\]

Applying (3.2) proves

\[
\begin{aligned}
\mathcal S(t_{\mathcal I_{10}})&=-(x_1+x_2),\\
\mathcal S(t_{\mathcal I_{20}})&=x_1^2+x_1x_2+x_2^2,\\
\mathcal S(t_{\mathcal I_{11}})&=x_1x_2.
\end{aligned}
\tag{3.4}
\]

These are the negative standard character, the symmetric-square character, and the determinant character. Their representation interpretation is also proved by the rank-one and minuscule calculations in Identifying the dual group, §§3–4. The minus sign in the first line comes from \([1]\).

## 4. Recovering the lattice-chain product

Consider the two-step modification with both relative positions \((1,0)\). Its source \(\widetilde Y\) is a smooth projective surface, an iterated \(\mathbf P^1\)-bundle, and the convolution map

\[
m:\widetilde Y\longrightarrow Y=\mathrm{Gr}_{GL_2}^{\leq(2,0)}
\tag{4.1}
\]

is an isomorphism over the open orbit. Its fibre over the central point is \(\mathbf P^1\). Indeed an index-two quotient lattice of type \((2,0)\) has a unique intermediate colength-one lattice; for type \((1,1)\), the quotient is a two-dimensional \(\mathbf F_q\)-space, and intermediate lattices are its lines. These are the actual chain fibres computed in Convolution and rigidity, §§2–3.

The normalized convolution is

\
\mathcal I_{10}*\mathcal I_{10}
 =Rm_*E_{\widetilde Y}[2.
\tag{4.2}
\]

At an open-orbit point its stalk has trace \(q^{-1}\). At the central point the stalk is \(R\Gamma(\mathbf P^1,E)2\). The projective-line computation, with its Kummer generator, gives

\[
H^0(\mathbf P^1,E)=E,
\qquad H^2(\mathbf P^1,E)=E(-1),
\qquad H^i=0\quad(i\ne0,2).
\tag{4.3}
\]

The two Frobenius eigenvalues before the twist are \(1,q\). After the shift and twist their trace sum is \(q^{-1}+1\). Formula (4.3) is proved by the curve computation used in Torsion sheaves on curves, §4, and its Frobenius convention in Frobenius morphisms and their action on cohomology, §6. Thus direct fibre computation proves

\[
t_{\mathcal I_{10}*\mathcal I_{10}}
 =q^{-1}c_{20}+(q^{-1}+1)c_{11}
 =t_{\mathcal I_{20}}+t_{\mathcal I_{11}}.
\tag{4.4}
\]

It also proves trace compatibility with function convolution here. The trace on the source object is constantly \(q^{-1}\). Summing it over the unique rational intermediate lattice in the first case or the \(q+1\) rational lines in the second case gives exactly the two stalk traces just calculated. The chain model is the function convolution model because every right \(K\)-coset has measure one, as proved in Lesson 1.

Under the exceptional-curve part of (P12), there is a corresponding sheaf decomposition, whose Frobenius normalization matters:

\[
\mathrm{IC}^{\mathrm{raw}}_{10}*
\mathrm{IC}^{\mathrm{raw}}_{10}
 \simeq\mathrm{IC}^{\mathrm{raw}}_{20}
 \oplus E_{(1,1)}(-1).
\tag{4.5}
\]

To verify (4.5) without a general decomposition theorem, use the exceptional curve \(D\). Its normal line bundle in the cone resolution is \(\mathcal O_{\mathbf P^1}(-2)\), computed from the lattice-chain charts in Convolution and rigidity, §10. The exceptional-curve hypothesis in (P12) supplies \(i_D^!E=E_D(-1)[-2]\) with its specified orientation. Pushing the exceptional-support localization triangle along \(m\), which is an isomorphism off \(D\), gives, for \(A=Rm_*E[2]\) and the vertex inclusion \(i\),

\[
i^*A=R\Gamma(D,E)[2],
\qquad i^!A=R\Gamma(D,E(-1)).
\tag{4.8}
\]

The first comparison is proper base change. For the second, the pushed localization triangle is the localization triangle at the vertex: the open terms agree because \(m\) is an isomorphism there, and composition of direct image identifies their maps. The closed term is therefore the stated supported complex.

Let \(P=E_{(1,1)}(-1)\). The inclusion of the degree-zero group in \(i^!A\) and the projection to the degree-zero group of \(i^*A\) define adjunction maps \(v:P\to A\) and \(u:A\to P\). Their composite is multiplication by \(-2\). To check it, the supported divisor orientation restricts to the Kummer class of its normal line bundle. In local divisor parameters the ratios of the parameters on overlaps are the transition functions of \(\mathcal O(D)\); their Kummer boundary is exactly that Chern class. Restricting to \(D\) gives \(c_1(\mathcal O(-2))\). The projective-line trace sends \(c_1(\mathcal O(1))\) to \(+1\), so it sends this class to \(-2\). This checks the scalar from the orientation specified in (P12); the supported purity comparison is still its hypothesis.

Replace \(u\) by \(-u/2\) to get a retraction. Its complement agrees with \(E[2]\) on the open orbit. Equations (4.3) and (4.8) show that \(i^*A\) has groups \(E\) in degree \(-2\) and \(E(-1)\) in degree zero; \(i^!A\) has groups \(E(-1)\) in degree zero and \(E(-2)\) in degree two. The nonzero composite removes exactly the degree-zero group on each side. The complementary stalk and costalk therefore have only degrees \(-2\) and \(2\), respectively. The strict boundary inequalities make the complement perverse and exclude a subobject or quotient on the closed point. It is \(\mathrm{IC}^{\mathrm{raw}}_{20}\), by intermediate extension. This proves (4.5). All coordinates, orientations, trace maps and the scalar \(-2\) are defined over \(\mathbf F_q\), so the decomposition is Frobenius compatible. The two half twists then give the total twist \((1)\).

Twisting (4.5) by \((1)\) yields

\[
\mathcal I_{10}*\mathcal I_{10}
 \simeq\mathcal I_{20}\oplus\mathcal I_{11}.
\tag{4.6}
\]

The twist on the central raw summand is essential. Dropping it would incorrectly replace its Frobenius eigenvalue \(q\) by \(1\).

Finally insert (3.3) in (4.4), or take traces in (4.6):

\[
q^{-1}(c_{10}*c_{10})
 =q^{-1}(c_{20}+c_{11})+c_{11}.
\]

Multiplication by \(q\) proves the indicator relation

\[
\boxed{\ c_{10}*c_{10}=c_{20}+(q+1)c_{11}.\ }
\tag{4.7}
\]

Thus one copy of the determinant representation corresponds to the normalized point sheaf, while the indicator coefficient remains \(q+1\).

## 5. The general character formula and its arithmetic input

The formal passage from weights to functions is short once its arithmetic hypotheses are specified. They are stronger than a bound on the absolute values of Frobenius eigenvalues.

**Proposition 5.1 (conditional trace comparison).** Fix a dominant \(\lambda\). Suppose that, for every \(\nu\), the following three statements hold for \(\mathcal I_\lambda\):

1. The compact-support trace identity holds on the supported finite-type intersection \(S_\nu\cap\mathrm{Gr}^{\leq\lambda}\).
2. Its compact cohomology is zero except in degree \(h_\nu\).
3. Frobenius acts on that remaining group as the scalar \(a^{h_\nu}\), and its dimension is \(\dim V_\lambda(\nu)\), the \(\nu\)-weight multiplicity of the dual-group representation.

Then, with the Satake normalization of Lesson 1,

\[
\mathcal S(t_{\mathcal I_\lambda})
 =(-1)^{d_\lambda}\operatorname{ch}V_\lambda.
\tag{5.1}
\]

**Proof.** The coefficient of \(e^\nu\) in the Satake transform is

\[
a^{-h_\nu}\sum_{x\in S_\nu(\mathbf F_q)}t_{\mathcal I_\lambda}(x).
\tag{5.2}
\]

There are finitely many nonzero terms. By the three premises the sum is \((-1)^{h_\nu}a^{h_\nu}\dim V_\lambda(\nu)\). Every nonzero weight satisfies \(\lambda-\nu\in\mathbf Z\Phi^\vee\); each simple coroot pairs to \(2\) with \(2\rho\). Therefore \(h_\nu\equiv d_\lambda\pmod2\). Substitute in (5.2) to obtain \((-1)^{d_\lambda}\dim V_\lambda(\nu)\). Summing over the weights proves (5.1). \(\square\)

The classical concentration and full representation calculations are proved in Semi-infinite orbits and weight functors and Identifying the dual group, Theorem 8.3, without a general IC parity hypothesis. Their complex-topological proofs do not by themselves supply the finite-field scalar-Frobenius premise in Proposition 5.1. Likewise, purity alone permits eigenvalues of the form \(a^{h_\nu}\zeta\); it does not force \(\zeta=1\). A split Tate calculation, including its Weil structure, supplies the stated scalar premise. The general arithmetic IC theorem is stated here, rather than used to establish the explicit products of §§3–4.

With these hypotheses, (5.1) gives the usual geometric interpretation of the classical Satake character basis. This normalization is discussed in Edward Frenkel's free [Lectures on the Langlands program and conformal field theory, §5.3](https://arxiv.org/abs/hep-th/0512172). If the half twist is instead defined using \(-a\), the trace of \(\mathcal I_\lambda\) is multiplied by \((-1)^{d_\lambda}\), and (5.1) has no sign. Equivalently one may multiply functions by the parity character of \(L/\mathbf Z\Phi^\vee\). This is well-defined because the coroot pairings just computed are even; under convolution the component parities add.

For a split torus, all the premises can be checked directly. A supported constructible sheaf ignores the nilpotent directions of its Grassmannian; its reduced support is a finite subset of \(L\), by Loop groups and the affine Grassmannian, §6. Every IC is the untwisted point object, all \(h_\nu\) and \(d_\lambda\) are zero, and its sole weight space is \(E\) with Frobenius one. Point convolution adds labels. Thus \(c_\lambda*c_\mu=c_{\lambda+\mu}\) and \(\mathcal S(c_\lambda)=e^\lambda\) follow directly.

## 6. A polynomial that remembers stalk degrees

Use the dual root system: its positive roots are the positive coroots of \(G\). Define \(P_u(\gamma)\in\mathbf Z[u]\) by the formal expansion

\[
\prod_{\beta\in\widehat\Phi^+}(1-u e^\beta)^{-1}
 =\sum_\gamma P_u(\gamma)e^\gamma.
\tag{6.1}
\]

For a fixed \(\gamma\), its coefficient is a finite sum. Indeed every positive root has positive height in the simple-root basis, so the sum of the multiplicities in a partition of \(\gamma\) is bounded by its height. A term with \(r\) roots contributes \(u^r\). Put \(\widehat\rho=\frac12\sum_{\beta\in\widehat\Phi^+}\beta\) and define

\[
m^\mu_\lambda(u)
 =\sum_{w\in W}(-1)^{\ell(w)}
 P_u\bigl(w(\lambda+\widehat\rho)-(\mu+\widehat\rho)\bigr).
\tag{6.2}
\]

The variable \(u\) in this definition is formal. It will be evaluated at the cardinality \(q\) only after the grading convention is fixed. The stalk theorem concerns **dominant** \(\lambda,\mu\) with \(\mu\leq\lambda\). It is not a positivity assertion about (6.2) for every nondonominant \(\mu\).

The correctly normalized stalk identity, stated for the classical characteristic-zero IC stalks, is

\[
m^\mu_\lambda(u)
 =u^{\langle\rho,\lambda-\mu\rangle}
 \sum_{j\geq0}
 \dim_E\mathcal H^{-d_\lambda+2j}
   (i_\mu^*\mathrm{IC}^{\mathrm{raw}}_\lambda)\,u^{-j}.
\tag{6.3}
\]

Here \(i_\mu\) is the geometric point \(t^\mu\); the sum uses stalk cohomological degrees, not the global IC degrees. The theorem also asserts the relevant parity and vanishing, so the right side is a polynomial with nonnegative exponents. Equation (6.3) is stated, with a free source locator given below; its general proof is not used in this lesson's calculations.

Equivalently the right side is \(\sum_{r\geq0}\dim\mathcal H^{-h_\mu-2r}(i_\mu^*\mathrm{IC}^{\mathrm{raw}}_\lambda)u^r\): set \(r=\langle\rho,\lambda-\mu\rangle-j\). The integer prefactor in (6.3) is integral because \(\lambda-\mu\) is a sum of coroots. George Lusztig's freely accessible [author copy of Singularities, character formulas, and a q-analogue of weight multiplicities](https://math.mit.edu/~gyuri/papers/ast.pdf), equations (9.3)–(9.4) and §11(c), printed pp. 225–227, gives the polynomial and IC conventions. The equation in (9.4) is presented there as a conjecture, followed by the note that Kato proved it. Dmitri Panyushev's free [On Lusztig's q-analogues of all weight multiplicities of a representation, §1, equation (1.1)](https://arxiv.org/abs/1406.1453), gives (6.1)–(6.2) with the positive powers used here. These specify the stalk conventions. The algebraic transition is proved below; the general geometric equality (6.3) remains unproved here.


### 6.1. A finite Hall–Littlewood polynomial

We now prove an algebraic interpretation of (6.2). Keep the dual positive roots \(\widehat\Phi^+\), the coweight lattice \(L\), and its Weyl group \(W\). Thus the roots in this calculation are the coroots of \(G\). The lattice can contain nonprimitive roots, and \(\widehat\rho\) need not belong to it. Central directions, on which \(W\) is trivial, are retained.

Work over \(F=\mathbf Q(u)\). Set
\[
Q_u=\prod_{\beta\in\widehat\Phi^+}
       \frac{1-e^{-\beta}}{1-u e^{-\beta}},\qquad
W_\nu(u)=\sum_{w\nu=\nu}u^{\ell(w)},
\]
and, for dominant \(\nu\), define initially in the fraction field
\[
H_\nu(u)=\frac1{W_\nu(u)}
       \sum_{w\in W}w\left(\frac{e^\nu}{Q_u}\right).
\tag{6.5}
\]
The stabilizer polynomial has constant term one, so is nonzero. We shall prove that \(H_\nu(u)\) is a finite \(W\)-invariant Laurent polynomial, supported in weights at most \(\nu\), with coefficient one on its top orbit. These are the Hall–Littlewood polynomials in the normalization (6.5).

The root and chamber arguments are proved in Root systems and their Weyl groups. The finite highest-weight characters and their support are proved in Weights, Verma modules and the theorem of the highest weight. We use the complete Weyl character proof in Weyl's character formula and the multiplicity formulas, Theorem 2.1 and Corollary 2.2.

Temporarily enlarge \(L\) to \(L'=L+\mathbf Z\widehat\rho\). It is a \(W\)-stable free lattice, because \(w\widehat\rho-\widehat\rho\) is in the root lattice. Put
\[
D=e^{\widehat\rho}\prod_{\beta>0}(1-e^{-\beta}),\qquad
A_\eta=\sum_w(-1)^{\ell(w)}e^{w\eta}.
\]
For a simple reflection, its changed root factor and changed \(\widehat\rho\) monomial give \(wD=(-1)^{\ell(w)}D\). Consequently
\[
W_\nu(u)D H_\nu(u)
 =\sum_{S\subset\widehat\Phi^+}(-u)^{|S|}
       A_{\nu+\widehat\rho-\beta_S},
\qquad \beta_S=\sum_{\beta\in S}\beta.
\tag{6.6}
\]
This is a finite expansion.

Each alternant divided by \(D\) is a Laurent polynomial in the original lattice. If \(\eta\) lies on a reflection wall, pair \(w\) with \(ws\), where \(s\eta=\eta\); their signs cancel, so \(A_\eta=0\). Otherwise choose \(v\) taking \(\eta\) into the open dominant chamber, with image \(\eta^+\). Its simple-coroot pairings are positive integers. Thus \(\eta^+-\widehat\rho\) is dominant integral and
\[
\eta^+-\widehat\rho
 =v\nu+(v\widehat\rho-\widehat\rho)-v\beta_S\in L.
\]
The proved Weyl character formula gives
\[
\frac{A_\eta}{D}
 =(-1)^{\ell(v)}\operatorname{ch}
       V_{\eta^+-\widehat\rho}.
\tag{6.7}
\]
For a reductive lattice, apply that formula to the semisimple restriction and retain the central monomial. All weight differences are in the root lattice, so its character remains in \(\mathbf Z[L]\). Equation (6.6) now proves \(H_\nu(u)\in F[L]^W\). In particular no divisibility argument requiring a primitive root in \(L\) is needed.

To prove triangular support, expand downward, in translates of the negative cone generated by the simple dual roots. A fixed coefficient of any expansion has finitely many terms, because positive height bounds all root exponents. If \(w\) sends a root to a positive root, its factor in \(w(Q_u^{-1})\) is a downward geometric series. If it sends it to \(-\beta\), the factor is
\[
\frac{1-u e^{\beta}}{1-e^{\beta}}
 =u+(u-1)\frac{e^{-\beta}}{1-e^{-\beta}}.
\tag{6.8}
\]
Thus each \(w\)-summand is supported in \(w\nu-\widehat Q^+\), where \(\widehat Q^+\) is the nonnegative integral simple-root cone. For dominant \(\nu\), the reduced-word calculation gives \(\nu-w\nu\in\widehat Q^+\): telescope along a reduced expression for \(w\); the resulting inversion roots are positive and their coefficients are the nonnegative pairings of \(\nu\) with simple coroots. It follows that every weight of \(H_\nu\) is at most \(\nu\). Its dominant orbit representative also has this property, by \(W\)-invariance.

### 6.2. The exact dual coefficient

For dominant \(\mu\) and a \(W\)-invariant Laurent polynomial \(f\), define
\
\mathfrak l_\mu(f)=[e^\mu.
\]
The product is read in the downward completion just specified. We prove
\[
\mathfrak l_\mu(H_\nu)=\delta_{\mu\nu}.
\tag{6.9}
\]

Let \(N(w)=\{\beta>0:w^{-1}\beta<0\}\). Factors that remain positive cancel in \(Q_u/wQ_u\). A changed factor, with \(x=e^{-\beta}\), is \((u-x)/(1-ux)\). Hence
\[
\frac{Q_u}{wQ_u}
 =\prod_{\beta\in N(w)}
      \frac{u-e^{-\beta}}{1-u e^{-\beta}}.
\tag{6.10}
\]
It is a downward series with constant term \(u^{\ell(w)}\). A contribution of the \(w\)-summand of \(H_\nu Q_u\) at \(\mu\) can therefore occur only if
\[
\mu=w\nu-\sum_{\beta\in N(w)}n_\beta\beta,
\qquad n_\beta\ge0.
\]
Applying \(w^{-1}\) gives
\[
w^{-1}\mu=\nu+
       \sum_{\beta\in N(w)}n_\beta(-w^{-1}\beta)\ge\nu.
\]
Dominance of \(\mu\) also gives \(\mu\ge w^{-1}\mu\). On the other hand, polynomial triangularity from §6.1 and the negative support of \(Q_u\) imply \(\mu\le\nu\) for every nonzero coefficient of their product. The simple-root cone is pointed. Thus \(\mu=\nu\), and every \(n_\beta\) is zero. The remaining terms have \(w\nu=\nu\), and their constant terms sum to \(W_\nu(u)\). Division by that sum proves (6.9). Using the triangularity of the sum here is legitimate: its polynomiality was established first, so a nonzero coefficient has that bound irrespective of cancellations between summands.

Only the coefficient of \(e^\nu\) in \(H_\nu\) can contribute to the coefficient of \(e^\nu\) in \(H_\nu Q_u\). Equation (6.9) therefore proves that this coefficient is one. Weyl invariance proves the same statement on the entire top orbit.

### 6.3. The character transition formula

**Theorem 6.1.** For every dominant coweight \(\lambda\),
\[
\operatorname{ch}V_\lambda
 =\sum_{\substack{\mu\text{ dominant}\\\mu\le\lambda}}
       m^\mu_\lambda(u)H_\mu(u).
\tag{6.11}
\]
This is a finite algebraic identity. Its coefficients are exactly the polynomials (6.2), for every reduced root datum and its coweight lattice.

**Proof.** There are finitely many dominant \(\mu\le\lambda\). Their central components are fixed. On the root span take a positive definite \(W\)-invariant inner product. Dominance gives
\[
\|\lambda\|^2-\|\mu\|^2
 =(\lambda+\mu,\lambda-\mu)\ge0,
\]
since \(\lambda-\mu\) is a nonnegative integral sum of simple roots, each having nonnegative inner product with \(\lambda+\mu\). Thus their root components lie in a bounded ball of a discrete lattice, which has finitely many points: bound their integer coordinates in any lattice basis.

The orbit sums \(\sum_{\eta\in W\mu}e^\eta\) are a basis of the invariant Laurent polynomials supported on these orbits. The proved triangularity and top coefficient one show that the \(H_\mu\) are another basis. Indeed, order this finite set by a linear extension of dominance; its change matrix is triangular with diagonal one and can be inverted by finitely many subtractions. Equation (6.9) supplies the exact dual basis. The highest-weight support theorem places \(\operatorname{ch}V_\lambda\) in this space, so its coefficient at \(H_\mu\) is \(\mathfrak l_\mu(\operatorname{ch}V_\lambda)\).

Multiply the proved Weyl character formula by \(Q_u\). It gives
\[
\operatorname{ch}V_\lambda Q_u
 =\sum_{w\in W}(-1)^{\ell(w)}
     e^{w(\lambda+\widehat\rho)-\widehat\rho}
     \prod_{\beta>0}(1-u e^{-\beta})^{-1}.
\tag{6.12}
\]
The negative-exponent version of (6.1) has coefficient \(P_u(\gamma)\) at \(e^{-\gamma}\), by the same finite partition count. Extraction of \(e^\mu\) in (6.12) is therefore exactly (6.2). This proves (6.11), including its finite support. Although the \(H_\mu\) were defined over \(\mathbf Q(u)\), every transition coefficient is in \(\mathbf Z[u]\). \(\square\)

At \(u=1\), \(Q_u=1\) and \(W_\mu(1)\) is the size of the stabilizer, so \(H_\mu(1)\) is its orbit sum. Thus (6.11) recovers the ordinary weight multiplicities. At \(u=0\), the alternant calculation makes \(H_\mu(0)=\operatorname{ch}V_\mu\). These specializations are defined: the only denominator in the finite polynomial expression is \(W_\mu(u)\), which is nonzero at both values.

Theorem 6.1 proves the algebraic transition underlying the weight polynomial. The full stalk formula (6.3) additionally needs the all-root spherical-Hecke comparison
\[
\mathcal S(c_\mu)=q^{\langle\rho,\mu\rangle}H_\mu(q^{-1})
\tag{6.13}
\]
and the graded IC stalk comparison. Those general comparisons remain unproved here. The variable in (6.13) is \(q^{-1}\), whereas the positive-power stalk polynomial in (6.3) uses \(u=q\); the shifts and grading account for the difference. No IC stalk identity follows solely from the character transition.

### 6.4. The rank-one check

For \(SL_2\), let \(\beta=\alpha^\vee\), the positive root of its dual \(PGL_2\). Then \(\widehat\rho=\beta/2\). Since the positive root system consists of \(\beta\),

\[
P_u(r\beta)=u^r\quad(r\geq0),
\qquad P_u(r\beta)=0\quad(r<0).
\]

For \(\lambda=\beta\) and \(\mu=0\), the identity Weyl element contributes \(P_u(\beta)=u\); the reflection contributes \(P_u(-2\beta)=0\). Thus

\[
m^0_{\alpha^\vee}(u)=u.
\tag{6.4}
\]

In the same rank-one lattice,
\[
H_\beta(u)=e^\beta+e^{-\beta}+1-u,\qquad H_0(u)=1.
\tag{6.14}
\]
Indeed put \(x=e^{-\beta}\) in (6.5). Its two summands are \(x^{-1}(1-ux)/(1-x)\) and \(x(x-u)/(x-1)\); their sum is \(x^{-1}+x+1-u\). For label zero their sum is \(1+u\), which is divided by \(W_0(u)=1+u\). Hence \(\operatorname{ch}V_\beta=H_\beta+uH_0\). The explicit \(SL_2\) Satake calculation in The Satake isomorphism and spherical representations, §6 verifies (6.13) in this example: multiplying (6.14) at \(u=q^{-1}\) by \(q\) gives \(q(e^\beta+e^{-\beta})+q-1\).

The cone calculation proves the same value directly: \(d_\lambda=2\), \(\langle\rho,\lambda\rangle=1\), and the stalk of \(E[2]\) has only \(\mathcal H^{-2}=E\). Hence the sum in (6.3) is \(1\), but its required prefactor is \(u\). At \(u=1\) the multiplicity is one; at \(u=q\) the polynomial is \(q\). These are different questions.

## 7. The Whittaker character and the Casselman–Shalika statement

We first specify the finite-characteristic statement. Work over an algebraic closure of a finite field, with \(\overline{\mathbf Q}_\ell\)-coefficients and \(\ell\ne p\). Choose a pinning, so that the simple-root coordinates \(u_i\) identify the abelianization of \(N\) with the product of its simple-root additive groups. Choose a nontrivial additive character \(\psi:\mathbf F_p\to\overline{\mathbf Q}_\ell^\times\) and its Artin–Schreier rank-one sheaf \(\mathcal L_\psi\) on \(\mathbf A^1\). Define the conductor-zero loop character

\[
\chi_0(n)=\sum_i\operatorname{Res}(u_i(n)\,dt),
\qquad
\chi_\mu(n)=\chi_0(t^\mu n t^{-\mu}).
\tag{7.1}
\]

The simple-root coordinates of a commutator vanish, so (7.1) is an additive group homomorphism. Its nonzero coefficient on every simple-root factor is the genericity condition.

On \(S_\nu=N((t))t^\nu\), the expression \(\chi_\mu(n)\), normalized to zero at \(t^\nu\), descends to a function \(\chi_\mu^\nu\) exactly when \(\mu+\nu\) is dominant. Indeed the simple-root coordinate of the stabilizer is \(t^{\langle\alpha_i,\nu\rangle}O\); conjugation by \(t^\mu\) multiplies it by \(t^{\langle\alpha_i,\mu\rangle}\). Residue is identically zero on that ideal exactly when \(\langle\alpha_i,\mu+\nu\rangle\geq0\). If the inequality fails, its \(t^{-1}\) coefficient can be nonzero, so descent fails. Coordinates for nonsimple roots do not affect the character. This proves the descent criterion.

The geometric Casselman–Shalika cohomology statement is the following, here stated without its general proof. For dominant \(\lambda\) and for \(\mu,\nu\) such that \(\mu+\nu\) is dominant,

\[
H_c^r\left(\mathrm{Gr}^{\leq\lambda}\cap S_\nu,
 \mathrm{IC}^{\mathrm{raw}}_\lambda\otimes
 (\chi_\mu^\nu)^*\mathcal L_\psi\right)
 \cong
\begin{cases}
\operatorname{Hom}_{\widehat G}
 (V_\lambda\otimes V_\mu,V_{\mu+\nu}),
 &r=h_\nu\text{ and }\mu\text{ dominant},\\
0,&\text{otherwise}.
\end{cases}
\tag{7.2}
\]

The displayed isomorphism concerns geometric coefficient spaces; it does not assign a Weil twist to its right side. For example \(E[d]\) on \(\mathbf A^d\) has compact cohomology \(E(-d)[-d]\), so omission of the twist would change its Frobenius trace.

Formula (7.2) is [Frenkel–Gaitsgory–Vilonen, Whittaker patterns in the geometry of moduli spaces of bundles on curves, Theorem 1, equation (1.7)](https://arxiv.org/pdf/math/9907133v5). The support is the **closed** Schubert variety. With \(\mu=0\) and dominant \(\nu\), the right side is one-dimensional only for \(\nu=\lambda\), and otherwise zero. Thus the complex has its surviving group in degree \(h_\lambda\), or is zero. In derived notation the nonzero geometric complex is \(E[-h_\lambda]\). This negative shift is consistent with the cohomological convention in §1.

There is also a categorical version. Its characteristic-zero incarnation requires exponential D-modules rather than ordinary complex local systems. On complex \(\mathbf A^1\), a rank-one local system is constant because the line is simply connected; it cannot provide the nontrivial additive character needed for Whittaker equivariance.

Here is the precise derived statement used in the 2024 geometric Langlands work. For a connected reductive group over an algebraically closed field of characteristic zero and a smooth curve \(X\), use the \(\rho(\omega_X)\)-twisted Grassmannian. The residue character is nonzero on every simple-root factor. Form the cocomplete derived category

\[
\operatorname{Whit}^{!}(G)
 =D\text{-}\mathrm{mod}_{1/2}
 (\mathrm{Gr}_{G,\rho(\omega_X)})^
 {L(N)_{\rho(\omega_X)},\chi}.
\tag{7.3}
\]

The superscript denotes character-twisted invariants, not ordinary invariant sheaves. With the half-twist and factorization structures specified there, there is a canonical equivalence of factorization categories

\[
\operatorname{CS}_G:
 \operatorname{Whit}^{!}(G)\xrightarrow{\sim}
 \operatorname{Rep}(\widehat G),
\qquad \Delta_\lambda\longmapsto V_\lambda.
\tag{7.4}
\]

In (7.4), the representation category is the derived cocomplete category in the source's convention. This is [Arinkin and collaborators, Proof of the geometric Langlands conjecture II, Theorem 1.4.2, §1.4.4 and Remark 1.4.6](https://arxiv.org/pdf/2405.03648v3). Sections 1.3–1.4 define the invariants and coinvariants and distinguish the local Grassmannian theorem from the global statement on \(\mathrm{Bun}_G\). The equivalence (7.4) is stated here; no proof of it is inferred from the classical Satake equivalence of Lesson 11.

For a torus the categorical assertion in the perverse setting has a complete elementary proof. There is no \(N\), no residue character and no shift. For \(T=\mathbf G_m\), a bounded supported perverse sheaf is a finite family \((V_n)_{n\in\mathbf Z}\) of finite-dimensional coefficient spaces. Multiplication of lattices gives

\[
(V*W)_r=\bigoplus_{m+n=r}V_m\otimes W_n.
\tag{7.5}
\]

The unit is \(E\) at zero. The dual places \(V_n^*\) at \(-n\); evaluation and coevaluation are the usual vector-space maps. Associativity and symmetry are those of vector spaces, and their coherence identities hold on each summand.

To identify this category with \(\operatorname{Rep}_E(\mathbf G_m)\), assign \(v\in V_n\) the coaction \(v\mapsto v\otimes z^n\). Conversely, expand the coaction of a finite-dimensional representation as \(\delta(v)=\sum_n p_n(v)\otimes z^n\). Coassociativity and counit give

\[
p_np_m=\delta_{nm}p_n,\qquad\sum_np_n=1.
\tag{7.6}
\]

A finite basis makes the sum finite. Therefore \(V=\bigoplus_n\operatorname{im}p_n\), and the two constructions are inverse, including on morphisms. The product coaction gives precisely (7.5). This proves the torus equivalence directly. The proof for a higher-dimensional split torus replaces \(\mathbf Z\) by its character lattice.

## 8. Factorization over finite sets of points

Let \(X\) be a smooth curve, and let \(I\) be a finite set. Its Beilinson–Drinfeld Grassmannian classifies a \(G\)-bundle together with a trivialization away from the graphs of \(I\) labeled points. Over the open subset \(X^{I,\circ}\) where all points are distinct, modifications at different discs are independent. The torsor-gluing proof and its compatibility with arbitrary parameter rings are in Beauville–Laszlo gluing and Fusion and the commutativity constraint, §§1–3. For a partition of \(I\) into disjoint blocks, the corresponding block-disjoint open has the analogous product description.

Along a diagonal the labels merge. Already for two points, the restriction of the canonical fusion extension to the diagonal gives the convolution of the two objects. Under a tensor equivalence with dual-group representations, this corresponds to

\[
\operatorname{Rep}(\widehat G\times\widehat G)
 \xrightarrow{\operatorname{Res}_{\mathrm{diag}}}
\operatorname{Rep}(\widehat G),
\qquad V\boxtimes W\longmapsto V\otimes W.
\tag{8.1}
\]

Indeed the diagonal element \(g\) acts as \(g\) on both factors. Lesson 8 proves the classical fusion extensions, the comparisons on every partial diagonal, and their associativity. These are statements about the specified equivariant, universally locally acyclic relative sheaves and their canonical extensions. They do not identify every constructible sheaf on \(X^I\) with a representation of a fixed product group.

The corresponding arithmetic theorem has further hypotheses. [Fargues–Scholze, Geometrization of the local Langlands correspondence, Definition VI.9.1 and VI.9–VI.11](https://arxiv.org/pdf/2102.13459v4) works on the local Hecke stack over \((\operatorname{Div}_X^1)^I\) for a nonarchimedean local field \(E_0\). Its coefficient ring \(\Lambda\) is killed by an integer prime to the residue characteristic. The Satake objects are ULA, flat, relative perverse sheaves. Proposition VI.9.2 retains the continuous \(W_{E_0}^I\)-action; VI.9.3–VI.9.4 give restriction and coherent fusion; VI.10.2–VI.10.3 reconstruct the product Hopf algebra internal to Weil representations. The dual-group identification and its cyclotomic pinning action are in VI.11.1. This arithmetic statement is not used as a proof of a classical equivalence on arbitrary \(X^I\).

The Ran space organizes points with varying finite label sets. Its finite-set data consist of the spaces \(X^I\), maps of diagonals induced by surjections of label sets, and product identifications over disjoint configurations. The preceding collision rule describes how Satake objects fit those maps. Constructing a full sheaf category on that colimit, with descent and an equivalence of categories, requires an additional theorem. The finite-set fusion statements above specify the part needed for the convolution category in this course.

## 9. The Hecke correspondence on bundles

The same modification geometry supplies the kernels of Hecke functors. Fix \(x\in X\). The Hecke correspondence at \(x\) classifies

\[
(\mathcal E,\mathcal E',\beta),
\qquad
\beta:\mathcal E|_{X-\{x\}}
 \xrightarrow{\sim}\mathcal E'|_{X-\{x\}}.
\tag{9.1}
\]

Its projections \(h_1,h_2\) forget \(\mathcal E'\) and \(\mathcal E\), respectively. Trivializing \(\mathcal E\) on the formal disc identifies the possible modifications with \(\mathrm{Gr}_G\). A change of disc trivialization acts by \(L^+G\), so an equivariant Satake object \(A\) descends to a kernel \(\mathcal K_{A,x}\) on this correspondence. The independence of such choices is exactly the torsor descent of Lesson 3 and the coordinate comparison of Lesson 8.

In a sheaf or D-module theory on \(\mathrm{Bun}_G\) with the indicated operations, the fixed-point Hecke transform is written

\[
\mathsf H_{A,x}(\mathcal F)
 =h_{2!}(h_1^*\mathcal F\otimes\mathcal K_{A,x}).
\tag{9.2}
\]

One fixes the shifts and, for D-modules, the choices of \(*\) and \(!\) according to that theory. Formula (9.2) records the geometric kernel convention; it does not assert that a six-functor theory on these stacks has been constructed in this lesson.

If those operations satisfy base change, the projection formula and composition, two successive transforms are represented by the stack of two successive modifications. Pushforward under composition of the modifications is the kernel convolution of Lesson 7. This explains the action relation \(\mathsf H_{A,x}\mathsf H_{B,x}\simeq\mathsf H_{A*B,x}\) in that formalism: the two sides integrate the same tensor product on the same chain correspondence. At distinct points the modifications are independent, as in §8. A Hecke eigensheaf for a dual-group local system has, for each representation \(V\), the associated local system as its parameter in these transforms. The global existence theorem and the categorical geometric Langlands equivalence are separate from this local kernel construction.

For \(\mathbf G_m\) the underlying operation is explicit even without a derived formalism. The bundle is a line bundle \(\mathcal L\). With the lattice convention \(t^nO\), a modification of index \(n\) produces \(\mathcal L(-nx)\): its local sections vanish to order \(n\). Applying index \(m\) next gives \(\mathcal L(-(n+m)x)\). This is the geometric counterpart of the point convolution (7.5).

## 10. Exercises with solutions

**Exercise 12.1 (easy).** Count the rational points of the \(SL_2\) quasi-minuscule Schubert closure, including its singular point.

**Solution.** Its open orbit is an affine-line bundle over \(\mathbf P^1\). There are \(q+1\) rational base points and \(q\) points over each one, so the open orbit has \(q(q+1)\) points. The remaining stratum consists of the vertex. The result is \(q^2+q+1\). This also agrees with the cell sizes \(q^2,q,1\).

**Exercise 12.2 (easy).** For the positive square root \(a\), compute the trace of the minuscule \(GL_2\) object and its Satake transform. Explain what changes if the negative square root defines the half twist.

**Solution.** The minuscule closure is \(\mathbf P^1\), and \(\mathcal I_{10}=E1\). Its sole stalk group is in degree \(-1\), with Frobenius \(a^{-1}\). Thus \(t_{\mathcal I_{10}}=-a^{-1}c_{10}\). Since \(\mathcal S(c_{10})=a(x_1+x_2)\), its transform is \(-(x_1+x_2)\). Replacing the half-twist eigenvalue by \((-a)^{-1}\) multiplies this trace by \(-1\), and the transform becomes \(x_1+x_2\).

**Exercise 12.3 (medium).** Under (P12), recover \(c_{10}*c_{10}=c_{20}+(q+1)c_{11}\) from the normalized IC convolution. Give the raw central summand and its Frobenius eigenvalue.

**Solution.** The normalized decomposition is \(\mathcal I_{10}*\mathcal I_{10}=\mathcal I_{20}\oplus\mathcal I_{11}\). Here \(t_{\mathcal I_{10}}=-a^{-1}c_{10}\), \(t_{\mathcal I_{20}}=q^{-1}(c_{20}+c_{11})\), and \(t_{\mathcal I_{11}}=c_{11}\). Trace compatibility for this map was proved by the point and projective-line fibre calculations in §4. Hence

\[
q^{-1}c_{10}*c_{10}=q^{-1}c_{20}+(q^{-1}+1)c_{11}.
\]

Multiply by \(q\). Before half twists, the central summand is \(E_{(1,1)}(-1)\), with eigenvalue \(q\), supplied by \(H^2(\mathbf P^1,E)\). The total twist \((1)\) cancels that \((-1)\), giving eigenvalue one in the normalized decomposition.

**Exercise 12.4 (medium).** Using the complex-topological IC calculation, or (P12) for the étale one, compute \(m^0_{\alpha^\vee}(u)\) for \(SL_2\) from (6.2), the transition (6.11), and the IC stalk. Explain why the stalk's dimension is not itself the polynomial.

**Solution.** The dual positive root is \(\beta=\alpha^\vee\), and \(\widehat\rho=\beta/2\). The identity term in (6.2) is \(P_u(\beta)=u\); the reflection term has argument \(-2\beta\) and is zero. Therefore \(m^0_\beta(u)=u\). Equation (6.14) gives \(\operatorname{ch}V_\beta=e^\beta+1+e^{-\beta}=H_\beta+uH_0\), so Theorem 6.1 gives the same coefficient. The raw IC stalk at the cone vertex is \(E[2]\), with only its degree \(-2\) group nonzero. In (6.3) it contributes \(1\) to the sum, multiplied by \(u^{\langle\rho,\beta\rangle}=u\). Its dimension and the ordinary weight multiplicity are one, the value at \(u=1\); its cohomological position gives the polynomial \(u\).

**Exercise 12.5 (hard).** State the character and support needed for (7.2), and prove the cohomology formula and the perverse Whittaker equivalence for \(\mathbf G_m\).

**Solution.** The character is the conductor-zero sum of residues in the pinned simple-root coordinates, conjugated by \(t^\mu\). It descends to \(S_\nu\) when \(\mu+\nu\) is dominant. The complex is restricted to the closed support \(\mathrm{Gr}^{\leq\lambda}\cap S_\nu\) and tensor-multiplied by the pullback of the chosen nontrivial Artin–Schreier character sheaf. Formula (7.2) places its surviving cohomology in degree \(h_\nu\) and identifies that space with \(\operatorname{Hom}(V_\lambda\otimes V_\mu,V_{\mu+\nu})\) if \(\mu\) is dominant; otherwise all groups vanish.

For a torus there are no roots, so every integer is dominant, the character is zero, and \(h_\nu=0\). The intersection is a point when \(\lambda=\nu\) and empty otherwise. Its compact cohomology is consequently \(E\) in degree zero in the first case and zero in the second. The representation Hom space is

\[
\operatorname{Hom}_{\mathbf G_m}
(E_\lambda\otimes E_\mu,E_{\mu+\nu})
 =\begin{cases}E,&\lambda=\nu,\\0,&\lambda\ne\nu,\end{cases}
\]

because a morphism between two one-dimensional weight representations is zero unless their weights agree. Thus the full cohomology statement holds here. Whittaker equivariance imposes no condition because \(N=1\). Its perverse category is the category of finite supported families \((V_n)\), with convolution (7.5). The coaction construction and the mutually orthogonal projections (7.6) give inverse tensor equivalences with \(\operatorname{Rep}_E(\mathbf G_m)\). Evaluation and coevaluation, associativity and symmetry were checked summandwise in §7, completing the categorical assertion in this case.

## 11. What this lesson does not prove

The general finite-field IC parity, split Tate structure and scalar-Frobenius assertion needed for Proposition 5.1 are not proved here. That proposition proves the implication from its three specified premises. The \(GL_2\) indicator product is proved by lattice-chain counts and the bounded proper-fibre trace calculation, and the torus case is proved directly. The identification of the quadratic-cone étale IC with a shifted constant sheaf, and the exceptional-curve IC splitting, remain conditional on (P12). In particular the trait Kummer calculation does not by itself prove plane or relative-divisor purity. The all-ground-field proof of those supported comparisons and their rational finite-system compatibility remains unfinished.

The algebraic character transition (6.11) is proved for every dual root datum and lattice in §§6.1–6.3. The general stalk identity (6.3), the general Whittaker cohomology theorem (7.2), the derived D-module factorization equivalence (7.4), and the arithmetic Fargues–Scholze equivalence are stated with their hypotheses and free locators. They are not used in the proofs of the rank-one or torus calculations. A full Ran-category construction and a six-functor theory on \(\mathrm{Bun}_G\) also remain unfinished.

## References

- Edward Frenkel, [Lectures on the Langlands program and conformal field theory](https://arxiv.org/abs/hep-th/0512172), §§5.3–5.6: normalized functions, geometric Satake and Hecke kernels.
- George Lusztig, [Singularities, character formulas, and a q-analogue of weight multiplicities, free author copy](https://math.mit.edu/~gyuri/papers/ast.pdf), equations (9.3)–(9.4), §11(c), printed pp. 225–227: polynomial and IC conventions.
- Dmitri Panyushev, [On Lusztig's q-analogues of all weight multiplicities of a representation](https://arxiv.org/abs/1406.1453), §1, equation (1.1): the positive-power partition formula.
- Edward Frenkel, Dennis Gaitsgory and Kari Vilonen, [Whittaker patterns in the geometry of moduli spaces of bundles on curves](https://arxiv.org/pdf/math/9907133v5), Theorem 1, equation (1.7); Definition 4.2.2, Theorems 3–4 and §5.4.4: the twisted cohomology theorem and the globalized abelian Whittaker category.
- Dima Arinkin and collaborators, [Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE](https://arxiv.org/pdf/2405.03648v3), §§1.3–1.4, especially Theorem 1.4.2 and Remark 1.4.6: the derived half-twisted factorization statement.
- Laurent Fargues and Peter Scholze, [Geometrization of the local Langlands correspondence](https://arxiv.org/pdf/2102.13459v4), VI.9–VI.11: relative arithmetic fusion, Weil actions and the reconstructed dual group.
