# Orthogonal assembly and modular halving

A small square-zero partial isometry occupies only part of an algebra. To fill the identity, one must find further intertwiners in the remaining corner and control the errors accumulated while adjoining them. Errors of disjoint operators do not automatically have orthogonal vector supports. We therefore keep track of the off-diagonal pieces removed from the positive vectors as well as the operators themselves.

The resulting assembly theorem applies to arbitrary standard forms under an explicit hypothesis in every corner. For a countably decomposable type III factor, that hypothesis follows from approximate modular intertwining in the whole factor. Full support then gives a lower bound on the initial functional mass, allowing both squared and unsquared relative error estimates.

We use the standard-form axioms, positive representatives of normal functionals, strong suprema of bounded increasing nets, and the complete square-zero extraction argument. The type III application also uses the earlier programme proof of equivalence of infinite projections in a countably decomposable factor: [Projections and types, Proposition 15.2(4)](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/foundations-of-von-neumann-algebras/src/projections-and-types-of-von-neumann-algebras.md).

## 1. Removing off-diagonal vector components

Fix a standard form \((M,H,J,P)\), where \(M\ne0\), and a number \(0<c<1\). Inner products are linear in the first variable, and right multiplication is \(\eta x=Jx^*J\eta\). For a finite family \(\boldsymbol\eta=(\eta_1,\ldots,\eta_n)\), with \(n\geq1\), write


\[
\|\boldsymbol\eta\|_2^2=\sum_j\|\eta_j\|^2,
\qquad
D_{\boldsymbol\eta}(x)^2
=\sum_j\|\eta_jx-cx\eta_j\|^2.
\]


Left and right multiplication by a projection are commuting orthogonal projections on \(H\). We write \(qHq\) for their common range. If \(\eta\in P\), then \(q\eta q\in P\), because the standard-form axiom \(aJaJ(P)\subset P\) applies with \(a=q\).

For a projection \(g\) and \(\eta\in P\), put


\[
b=g\eta(1-g).
\]


Since \(J\eta=\eta\), we have \(Jb=(1-g)\eta g\), and hence


\[
\begin{aligned}
\eta-b-Jb&=g\eta g+(1-g)\eta(1-g)\in P,\\
\|g\eta-\eta g\|^2&=2\|b\|^2.
\end{aligned}
\tag{1}
\]


The second identity holds because \(b\) and \(Jb\) have orthogonal left supports and equal norms. The vector in the first line commutes with \(g\).

We also need a bound for the support of a square-zero partial isometry. Suppose \(v^2=0\), and put \(e=v^*v\), \(f=vv^*\). Then \(ef=0\): indeed \(ev=v^*v^2=0\), whence \(ef=evv^*=0\). Thus \(g=e+f\) is a projection. For \(\eta\in P\), let \(d=\eta v-cv\eta\). Direct multiplication gives


\[
\begin{aligned}
\eta f-f\eta&=dv^*-vJd,\\
c(\eta e-e\eta)&=v^*d-(Jd)v.
\end{aligned}
\]


Both actions of \(v\) are contractions. Therefore, with


\[
K_c=2(1+c^{-1}),
\]


we have


\[
\sum_j\|g\eta_j-\eta_jg\|^2
\leq K_c^2D_{\boldsymbol\eta}(v)^2.
\tag{2}
\]


Equation (1) will convert this commutator bound into control of the removed vector components. In particular, we may use \(\sum_j\|g\eta_j(1-g)\|^2\leq K_c^2D_{\boldsymbol\eta}(v)^2\); the factor of two in (1) allows a better constant but is not needed.

## 2. The corner hypothesis and admissible partial assemblies

Assume the following local property for the fixed \(c\): for every nonzero projection \(q\), every finite family \(\eta_j\in P\cap qHq\), and every \(t>0\), there is a nonzero partial isometry \(v\in qMq\) such that


\[
v^2=0,\qquad
D_{\boldsymbol\eta}(v)^2
\leq t\sum_j\|v\eta_j\|^2.
\tag{3}
\]


The mass on the right is permitted to be zero. Section 6 will verify this property in the type III setting.

Fix positive vectors \(\xi_1,\ldots,\xi_n\), and define the normal positive functional


\[
\rho(x)=\sum_j\langle x\xi_j,\xi_j\rangle.
\]


It need not be faithful. Fix also \(\delta>0\). A partial assembly consists of a square-zero partial isometry \(u\) and vectors \(\alpha_j\), with


\[
p=u^*u+uu^*,\qquad
\zeta_j=\xi_j-\alpha_j-J\alpha_j,
\]


satisfying


\[
\begin{gathered}
p\alpha_j=\alpha_j,\qquad
\zeta_j\in P,\qquad p\zeta_j=\zeta_jp,\\
D_{\boldsymbol\zeta}(u)^2\leq\delta\rho(p),\qquad
\sum_j\|\alpha_j\|^2\leq\delta\rho(p).
\end{gathered}
\tag{4}
\]


The zero operator with all \(\alpha_j=0\) is an assembly.

An assembly \((u,\boldsymbol\alpha)\) is below \((w,\boldsymbol\beta)\), with support \(r=w^*w+ww^*\), when


\[
\begin{gathered}
p\leq r,\qquad
w-u\in(r-p)M(r-p),\\
p(\beta_j-\alpha_j)=0,\qquad
\sum_j\|\beta_j-\alpha_j\|^2\leq\delta\rho(r-p).
\end{gathered}
\tag{5}
\]


This is a partial order. Reflexivity is immediate. In both directions the support projections agree, and (5) forces both operators and all vectors to agree, proving antisymmetry. For transitivity, successive vector increments have left supports in successive orthogonal projection differences. Their squared norms therefore add. The corresponding bounds in (5) add to \(\delta\rho(r-p)\). The operator increments also lie in the required larger corner. This proves transitivity.

## 3. Every chain has an upper bound

Let \((u_i,\boldsymbol\alpha_i)\) be a nonempty chain of partial assemblies, directed by its order, and put


\[
p_i=u_i^*u_i+u_iu_i^*,\qquad p=\sup_i p_i.
\]


The projections increase strongly to \(p\). If \(i\leq k\), the difference \(u_k-u_i\) lies in \((p_k-p_i)M(p_k-p_i)\). It is a partial isometry or zero: the two summands have orthogonal supports, and the identities for the initial and final projections of \(u_k\) show that the corresponding projections of the difference are projections. Hence, for every \(h\in H\),


\[
\begin{aligned}
\|(u_k-u_i)h\|&\leq\|(p_k-p_i)h\|,\\
\|(u_k^*-u_i^*)h\|&\leq\|(p_k-p_i)h\|.
\end{aligned}
\]


The two operator nets are strongly Cauchy and uniformly bounded by one. They converge strongly to \(u\) and \(u^*\), respectively, with \(u\in M\). Strong convergence of products of uniformly bounded strongly convergent nets shows that \(u^2=0\), that \(u^*u\) and \(uu^*\) are the increasing limits of their counterparts for \(u_i\), and that


\[
u^*u+uu^*=p.
\]


In particular, \(u\) is a partial isometry. Taking limits in the extension identities also gives
\(u-u_i\in(p-p_i)M(p-p_i)\).

For the vector corrections, (5) gives


\[
\|\boldsymbol\alpha_k-\boldsymbol\alpha_i\|_2^2
\leq\delta\rho(p_k-p_i).
\]


Normality and finiteness of \(\rho\) imply \(\rho(p_i)\uparrow\rho(p)\). Thus the corrections converge in \(H^{\oplus n}\) to a family \(\boldsymbol\alpha\), and


\[
\|\boldsymbol\alpha-\boldsymbol\alpha_i\|_2^2
\leq\delta\rho(p-p_i),\qquad
p_i\alpha_j=\alpha_{i,j},\qquad p\alpha_j=\alpha_j.
\tag{6}
\]


The positive vectors \(\zeta_{i,j}=\xi_j-\alpha_{i,j}-J\alpha_{i,j}\) converge in norm to \(\zeta_j=\xi_j-\alpha_j-J\alpha_j\). The cone is norm closed, so \(\zeta_j\in P\). Passing to the limit in \(p_i\zeta_{i,j}=\zeta_{i,j}p_i\) gives \(p\zeta_j=\zeta_jp\). The right actions converge strongly too, since they are obtained from the strongly convergent adjoints by conjugating with \(J\). Consequently all vector defects converge in norm, and (4) passes to the limit.

The limit is therefore an assembly, and (6) makes it an upper bound for the chain. The empty chain has the zero assembly as an upper bound. Zorn's lemma supplies a maximal assembly. This proof did not require a countable chain or a faithful \(\rho\).

## 4. Enlarging an assembly in the remaining corner

Let \((u,\boldsymbol\alpha)\) be an assembly with support \(p\), and suppose \(q=1-p\ne0\). Put


\[
\eta_j=q\zeta_jq=q\xi_jq.
\tag{7}
\]


The equality follows from \(q\alpha_j=0\) and \((J\alpha_j)q=J(q\alpha_j)=0\). Each \(\eta_j\) belongs to \(P\cap qHq\). Apply (3) with \(t=\delta/K_c^2\), obtaining a nonzero \(v\in qMq\). Let


\[
g=v^*v+vv^*,\qquad
b_j=g\zeta_j(1-g),\qquad
w=u+v,\qquad \beta_j=\alpha_j+b_j.
\]


Since \(\zeta_j\) commutes with \(p\) and \(g\leq q\),


\[
b_j=g\eta_j(q-g),\qquad gb_j=b_j.
\]


The compression in (7) gives the crucial comparison with the original functional:


\[
\sum_j\|v\eta_j\|^2
=\sum_j\|v\xi_jq\|^2
\leq\sum_j\|v\xi_j\|^2
=\rho(v^*v)\leq\rho(g).
\tag{8}
\]


Equations (1)–(3) now imply


\[
\sum_j\|b_j\|^2
\leq K_c^2D_{\boldsymbol\eta}(v)^2
\leq\delta\rho(g).
\tag{9}
\]


The operators \(u\) and \(v\) live in orthogonal corners, so \(w\) is a square-zero partial isometry with support \(p+g\). The new positive vectors are


\[
\theta_j=\xi_j-\beta_j-J\beta_j
=g\zeta_jg+(1-g)\zeta_j(1-g).
\tag{10}
\]


They belong to \(P\) and commute with \(g\) and with \(p\), hence with \(p+g\). Also \((p+g)\beta_j=\beta_j\). The old and new corrections have orthogonal left supports, so


\[
\sum_j\|\beta_j\|^2
=\sum_j\|\alpha_j\|^2+\sum_j\|b_j\|^2
\leq\delta\rho(p+g).
\]


To check the defect, direct multiplication in (10) gives


\[
\begin{aligned}
\theta_ju-cu\theta_j
&=(1-g)(\zeta_ju-cu\zeta_j)(1-g),\\
\theta_jv-cv\theta_j
&=g(\eta_jv-cv\eta_j)g.
\end{aligned}
\]


These two vectors lie in the orthogonal subspaces \(pHp\) and \(gHg\), respectively. Compression is contractive. Since \(K_c>1\), we obtain


\[
\begin{aligned}
D_{\boldsymbol\theta}(w)^2
&\leq D_{\boldsymbol\zeta}(u)^2+D_{\boldsymbol\eta}(v)^2\\
&\leq\delta\rho(p)+\frac\delta{K_c^2}\rho(g)\\
&\leq\delta\rho(p+g).
\end{aligned}
\]


All conditions (4) hold for the new assembly. Conditions (5) follow from \(v\in gMg\), the left support of \(b_j\), and (9). Since \(v\ne0\), we have \(g\ne0\), so the extension is strict. This is true even if \(\rho(g)=0\); in that case (9) and the local defect bound simply give zero errors.

## 5. The assembly theorem

**Theorem.** Under the corner property (3), for every finite family \(\xi_j\in P\) and every \(a>0\), there is a partial isometry \(u\in M\) such that


\[
u^2=0,\qquad u^*u+uu^*=1,\qquad
D_{\boldsymbol\xi}(u)\leq a.
\tag{11}
\]


More quantitatively, for each \(\delta>0\) the preceding construction gives


\[
D_{\boldsymbol\xi}(u)
\leq (3+2c)\sqrt{\delta\rho(1)}.
\tag{12}
\]


**Proof.** Take a maximal assembly from Section 3. Section 4 shows that its support must be one. By (4),


\[
D_{\boldsymbol\zeta}(u)\leq\sqrt{\delta\rho(1)},
\qquad \|\boldsymbol\alpha\|_2\leq\sqrt{\delta\rho(1)}.
\]


Since \(\boldsymbol\xi-\boldsymbol\zeta=\boldsymbol\alpha+J\boldsymbol\alpha\), the triangle inequality and the contractivity of both actions of \(u\) give


\[
\begin{aligned}
D_{\boldsymbol\xi}(u)
&\leq D_{\boldsymbol\zeta}(u)
+(1+c)\|\boldsymbol\alpha+J\boldsymbol\alpha\|_2\\
&\leq\sqrt{\delta\rho(1)}
+2(1+c)\sqrt{\delta\rho(1)}.
\end{aligned}
\]


This is (12). If \(\rho(1)>0\), choose
\(\delta=a^2/((3+2c)^2\rho(1))\). If \(\rho(1)=0\), every \(\xi_j\) vanishes and the same construction has zero defect for any \(\delta>0\). In either case (11) follows. \(\square\)

The condition \(u^*u+uu^*=1\) says that the initial and final projections are complementary and equivalent. We call such a \(u\) a *halving partial isometry*. Its norm is one because \(M\ne0\).

## 6. Passing approximate intertwining to corners

Suppose now that \(M\) is a countably decomposable type III factor. Assume that, for every finite family \(\xi_j\in P\) and every \(s>0\), there is a nonzero \(x\in M\) such that


\[
D_{\boldsymbol\xi}(x)^2
\leq s\sum_j\|x\xi_j\|^2.
\tag{13}
\]


We prove the corner property (3), including the nonfaithful cases. The qualitative condition (13) is unchanged if it is stated as an individual inequality for each squared defect: sum those inequalities after dividing the prescribed tolerance by \(n\), as in the extraction lemma's comparison of tolerances.

Fix \(q\ne0\). Both \(q\) and \(1\) are infinite projections. The projection-equivalence theorem cited in the introduction gives an isometry \(s_q\in M\) with


\[
s_q^*s_q=1,\qquad s_qs_q^*=q.
\]


The map \(x\mapsto s_qxs_q^*\) is a normal unital isomorphism from \(M\) to \(qMq\). Its standard-form transport is explicit:


\[
T_q:H\longrightarrow qHq,\qquad T_q\xi=s_q\xi s_q^*.
\tag{14}
\]


Left multiplication by \(s_q\) and right multiplication by \(s_q^*\) are isometries, since \(s_q^*s_q=1\). The inverse of (14), on \(qHq\), is \(\eta\mapsto s_q^*\eta s_q\). Thus \(T_q\) is unitary onto this corner space. The standard-form cone axiom applied to \(s_q\) and \(s_q^*\) shows


\[
T_q(P)=P\cap qHq,
\qquad T_qJ=JT_q.
\]


It intertwines both algebra actions under the corner isomorphism. These identities also verify the standard form of the corner by transport of all four standard-form axioms.

Given positive vectors \(\eta_j\in qHq\), apply (13) to \(T_q^{-1}\eta_j\). For the resulting nonzero \(x\), put \(y=s_qxs_q^*\ne0\). Unitarity and the intertwining identities give


\[
D_{\boldsymbol\eta}(y)
=D_{T_q^{-1}\boldsymbol\eta}(x),
\qquad
\sum_j\|y\eta_j\|^2
=\sum_j\|xT_q^{-1}\eta_j\|^2.
\]


Hence (13) holds in \(qMq\) for arbitrary tolerances. This corner has no nonzero abelian projection, because \(M\) is type III. The nonfaithful square-zero extraction theorem therefore proves (3). Its proof uses the positive-mass extraction theorem if the total functional is faithful, and a square-zero partial isometry in the common null corner otherwise. No replacement of a nonfaithful functional by a faithful one is needed.

We conclude that (13) implies the full-support conclusion (11).

For completeness, separable predual implies the countable decomposability used here. Given mutually orthogonal nonzero projections \(p_i\), choose a normal state supported on each \(p_i\) by normalizing a nonzero vector functional in that corner. Two of these states have distance two: evaluate their difference on \(p_i-p_j\), which has norm one. A separable metric space has only countably many points separated by distance two, as a countable cover by balls of radius less than one shows. Thus the orthogonal family is countable.

## 7. Full support supplies positive mass and the unsquared bound

Let \(\varphi_j=\omega_{\xi_j}\), \(\Phi=\sum_j\varphi_j\), and \(m=\Phi(1)\). For a halving partial isometry \(u\), put


\[
A^2=\Phi(u^*u),\qquad B^2=\Phi(uu^*),\qquad
d=D_{\boldsymbol\xi}(u).
\]


Full support and the reverse triangle inequality give


\[
A^2+B^2=m,\qquad |B-cA|\leq d.
\tag{15}
\]


In particular,


\[
\left|A^2-\frac{m}{1+c^2}\right|
\leq\frac{1+c}{1+c^2}\sqrt m\,d.
\tag{16}
\]


Indeed, \(|B^2-c^2A^2|\leq d(B+cA)\leq(1+c)\sqrt m\,d\); substitute \(B^2=m-A^2\). Thus approximate intertwiners with full support have initial mass approaching \(m/(1+c^2)\). Their mass cannot disappear when \(m>0\).

Here is a convenient bound without a limiting argument. From \(\sqrt m\leq A+B\leq(1+c)A+d\), we obtain


\[
d\leq\frac{\sqrt m}{2}
\quad\Longrightarrow\quad
\Phi(u^*u)\geq\frac{m}{4(1+c)^2}.
\tag{17}
\]


**Unsquared relative estimate.** Under the corner property (3), for every \(\varepsilon>0\) and every finite family \(\varphi_j\in M_*^+\), there is a halving partial isometry \(u\) such that


\[
\|\xi_j u-cu\xi_j\|
\leq\varepsilon\sum_k\varphi_k(u^*u)
\qquad(1\leq j\leq n).
\tag{18}
\]


If \(m>0\), use the assembly theorem to make


\[
d\leq\min\left\{
\frac{\sqrt m}{2},\frac{\varepsilon m}{4(1+c)^2}
\right\}.
\]


Each individual defect is at most \(d\), and (17) proves (18). If \(m=0\), all functionals and vectors vanish, and any halving partial isometry supplied by the theorem satisfies (18).

This is the extra step needed to pass from the squared estimate in the extraction lemma to an unsquared estimate with the initial mass on the right. Taking a square root of the extraction estimate alone would yield the square root of that mass instead. The proof of (18) uses only the squared local bound (3), so it does not assume (18) during assembly.

## 8. Vector and predual forms of modular halving

For a countably decomposable type III factor and \(0<c<1\), the following three properties are equivalent:

1. The approximate vector condition (13) holds for every finite family and every tolerance.
2. For every finite family \(\xi_j\in P\) and every \(a>0\), there is a halving partial isometry \(u\) with \(D_{\boldsymbol\xi}(u)\leq a\).
3. For every finite family \(\varphi_j\in M_*^+\) and every \(a>0\), there is a halving partial isometry \(u\) such that


\[
\|\varphi_j u-c^2u\varphi_j\|\leq a
\qquad(1\leq j\leq n).
\tag{19}
\]


We use \((\varphi u)(x)=\varphi(ux)\) and \((u\varphi)(x)=\varphi(xu)\).

**Proof.** Sections 2–6 prove 1 implies 2. The two-functional coefficient estimate gives


\[
\|\varphi_j u-c^2u\varphi_j\|
\leq(1+c)\sqrt{\varphi_j(1)}
\,\|\xi_j u-cu\xi_j\|.
\]


Choosing a sufficiently small vector tolerance proves 2 implies 3, including zero functionals.

For 3 implies 1, fix the finite family and choose halving partial isometries \(u_k\) with all functional defects at most \(1/k\). They are uniformly bounded. The proved bounded-family intertwining equivalence, applied to the pair \((\varphi_j,c^2\varphi_j)\), gives


\[
d_k=D_{\boldsymbol\xi}(u_k)\longrightarrow0.
\]


If \(m=\sum_j\varphi_j(1)>0\), (16) gives


\[
\sum_j\|u_k\xi_j\|^2
\longrightarrow\frac{m}{1+c^2}>0.
\]


For any prescribed \(s>0\), a sufficiently large \(k\) therefore satisfies (13), with \(x=u_k\ne0\). If \(m=0\), both sides of (13) vanish for any of these nonzero operators. This proves 1. \(\square\)

Writing \(\lambda=c^2\), the vector scalar is \(\sqrt\lambda\) and the functional scalar is \(\lambda\). For an exact halving intertwiner, (16) gives


\[
\Phi(u^*u)=\frac{\Phi(1)}{1+\lambda},\qquad
\Phi(uu^*)=\frac{\lambda\Phi(1)}{1+\lambda}.
\]


These weights agree with the explicit two-dimensional model in the square-zero lesson. The argument above proves the approximate halving equivalence and its mass estimates. A tensor-product absorption theorem requires additional work beyond this equivalence.
