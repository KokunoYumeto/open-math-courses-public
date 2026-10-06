# Constructing spatial energy from finite observations

**Self-checked by the writing AI.**

A spatial energy starts with bounded vectors for a weight on the commutant. Its coefficient is a positive operator in the original algebra, so a second weight can measure that coefficient. Three issues remain: whether sufficiently many vectors have finite energy, whether completion preserves their Hilbert-space identity, and which directions have zero energy. We prove these assertions directly from normal positive functionals and their vector implementations.

The denominator below is normal, semifinite and faithful. The numerator may be any normal weight. A nonsemifinite numerator produces a closed form on a possibly proper closed subspace; it is not assigned a densely defined self-adjoint operator on the whole Hilbert space. For semifinite numerators the construction supplies the ordinary spatial derivative, its exact square-root core, its support, its order relation and bounded invertible covariance. Modular time covariance, cocycles and the relative modular identification are separate remaining theorems.

The mathematical antecedents include Takesaki, *Theory of Operator Algebras II*, Chapter IX, Section 3, Lemmas 3.3(iii), 3.7 and 3.9, Theorem 3.8(i),(v), and Proposition 3.10(i),(iii),(iv). The argument here uses the concrete predual, finite observations and completion of forms. It does not import the source's linking-algebra proof or its prose.

## Conventions and the actual prerequisites

Fix a concrete unital von Neumann algebra \(M\subseteq B(H)\), put \(N=M'\), and let \(\psi\) be a normal semifinite faithful weight on \(N\). Both \(H\) and the algebras are arbitrary. Inner products are linear in the first variable. Write

\[
(H_\psi,\pi_\psi,\Lambda_\psi),\qquad
\mathfrak n_\psi=\{x\in N:\psi(x^*x)<\infty\}
\]

for the semicyclic construction. We use the direct commutant convention: the denominator is a weight on \(M'\), not on an unnamed opposite algebra.

For \(\xi\in H\), say \(\xi\in D_\psi\) when

\[
\|x\xi\|\le C_\xi\|\Lambda_\psi(x)\|
\qquad(x\in\mathfrak n_\psi)
\tag{SC.1}
\]

for some finite constant. Then \(R(\xi):H_\psi\to H\) is the bounded extension of \(\Lambda_\psi(x)\mapsto x\xi\), and

\[
\theta(\xi,\eta)=R(\xi)R(\eta)^*\in M.
\tag{SC.2}
\]

The extension, the intertwining identity, and \(M\)-covariance are proved in Which vectors define bounded intertwiners?. In particular \(D_\psi\) is linear and invariant under \(M\), and \(R(a\xi)=aR(\xi)\). The coefficient ideal and its positive cone are proved in **SD-04**; the finite energy polarization is **SD-05**.

Here are the further exact inputs.

- The concrete predual and its intrinsic norm through The sigma-strong seminorms are vector seminorms: the concrete Banach predual; its identification with ultraweakly continuous functionals; the positive norm formula; and domination of a positive normal functional by a square-summable vector sum. The exact positive vector-sum representation needed here is proved in SC-02 below.
- The full characterization: every normal weight \(\chi\) satisfies \(\chi(a)=\sup_{\omega\in N_*^+,\,\omega\le\chi}\omega(a)\) on its whole positive cone. Its independent proof retains the convex-analysis foundations stated in NW-01. This use does not close those foundations by itself.
- **Domain algebra and its positive cone through The GNS construction for an arbitrary weight and Finite positive cutoffs characterize semifiniteness:** finite-domain algebra, GNS construction, and finite positive contraction nets for semifinite weights. **WS-02–06** provide the finite-domain projection \(e_\varphi\), the largest null projection \(f_\varphi\le e_\varphi\), and their exact corner conventions for a normal numerator \(\varphi\).
- **Finite-vector approximation and the bicommutant through Supports from bounded resolvent cutoffs:** bicommutants, bounded monotone nets, bounded strong-to-ultraweak convergence, continuous functional calculus, inverse order and support cutoffs. The positive-operator square root, bounded-form representation, completion and orthogonal projection inputs are the course's stated Hilbert and bounded-calculus prerequisites.
- The completion test and canonical closure through Cores determine the domain, not just a dense set of vectors: the completion test for closability, relative lower semicontinuity and exact form cores. Representation with the exact square-root domain represents a closed positive form on the closure of its domain. The required arbitrary-dimensional spectral calculus is supplied by Bounded Borel functions and the spectral measure through Convergence and cutoffs, including exact integral domains, square roots and spectral transport. These lessons depend in turn on their stated scalar, Hilbert-space and bounded-calculus inputs, which are not proved here.

No standard form, modular conjugation, relative Tomita map, normal-representation image theorem or weight on a GNS commutant is used in the proof. In particular, the bounded normal-map criterion is not substituted for NW's infinite-valued weight theorem. All mathematical assertions below are relative to these specified prerequisites.

## Positive observations can be implemented by vector sums

**Lemma.** If \(A\subseteq B(L)\) is a concrete unital von Neumann algebra and \(\omega\in A_*^+\), there are vectors \(v_j\in L\), indexed by positive integers, such that

\[
\sum_j\|v_j\|^2=\omega(1),\qquad
\omega(a)=\sum_j\langle av_j,v_j\rangle
\quad(a\in A).
\tag{SC.3}
\]

The series is absolutely convergent. Every component functional \(\omega_{v_j}\) is positive normal and satisfies \(\omega_{v_j}\le\omega\). No separability hypothesis on \(L\) is needed.

**Proof.** CP-08 gives square-summable vectors \(\zeta=(\zeta_j)\in\ell^2(\mathbb N,L)\) such that

\[
\omega(a)\le\vartheta(a):=
\sum_j\langle a\zeta_j,\zeta_j\rangle
\qquad(a\ge0).
\]

Let \(\rho(a)=\operatorname{diag}(a,a,\ldots)\), a bounded *-representation on \(\ell^2(\mathbb N,L)\), and put \(K=\overline{\rho(A)\zeta}\). The subspace is invariant under \(\rho(A)\) and its adjoints, so it reduces this representation. Also \(\zeta\in K\), because \(A\) is unital.

On the dense subspace \(\rho(A)\zeta\subseteq K\), define

\[
B(\rho(a)\zeta,\rho(b)\zeta)=\omega(b^*a).
\]

The inequality \(\omega(a^*a)\le\vartheta(a^*a)=\|\rho(a)\zeta\|^2\), together with the positive-functional Cauchy–Schwarz inequality, proves that this rule is well-defined and

\[
|B(\rho(a)\zeta,\rho(b)\zeta)|
\le\|\rho(a)\zeta\|\,\|\rho(b)\zeta\|.
\]

It extends to a positive bounded sesquilinear form on \(K\). The bounded-form theorem gives a unique positive contraction \(h\in B(K)\) with \(B(u,v)=\langle hu,v\rangle\).

For \(c\in A\), the equality

\[
B(\rho(c)\rho(a)\zeta,\rho(b)\zeta)
=B(\rho(a)\zeta,\rho(c^*)\rho(b)\zeta)
\]

holds because both sides equal \(\omega(b^*ca)\). Extension from the dense cyclic subspace shows that \(h\) commutes with \(\rho(c)|_K\). Its square root commutes as well. Set \(v=h^{1/2}\zeta\in K\), and write its components as \(v_j\in L\). For every \(a\in A\),

\[
\omega(a)=B(\rho(a)\zeta,\zeta)
=\langle\rho(a)v,v\rangle
=\sum_j\langle av_j,v_j\rangle.
\]

Evaluation at \(1\) gives the asserted sum of squared norms. Absolute convergence follows from \(|\langle av_j,v_j\rangle|\le\|a\|\|v_j\|^2\). For positive \(a\), each nonnegative summand is at most the sum, proving \(\omega_{v_j}\le\omega\). Single-vector functionals are ultraweakly continuous by CP. If \(\omega=0\), the construction may be replaced by the zero sequence. ∎

The use of a countable series concerns one predual functional. The family of all normal functionals can be arbitrarily large. We have not chosen a countable family which detects the entire algebra.

## The exact closure of bounded vectors

For this result alone let \(\chi\) be any normal weight on a concrete unital von Neumann algebra \(A\subseteq B(L)\). Do not assume semifiniteness or faithfulness. Define \(D_\chi(L)\) by the estimate (SC.1), using \(\chi\), its finite left ideal, and the original action on \(L\). Let \(f_\chi\) be the largest \(\chi\)-null projection from WS-04.

**Theorem.**

\[
\overline{D_\chi(L)}^{\,\|\cdot\|}
=(1-f_\chi)L.
\tag{SC.4}
\]

In particular, a faithful normal weight has dense bounded vectors. For a normal semifinite weight, \(1-f_\chi\) is its support in the WS-06 convention.

**Proof.** The bounded-vector space is linear. If \(b\in A'\) and \(\xi\) is bounded, then

\[
\|x b\xi\|=\|b x\xi\|
\le\|b\|C_\xi\chi(x^*x)^{1/2},
\]

so \(b\xi\) is bounded. The closed subspace \(\overline{D_\chi(L)}\) therefore reduces \(A'\), and its projection \(P\) lies in \(A''=A\).

Since \(\chi(f_\chi)=0\), the projection \(f_\chi\) lies in \(\mathfrak n_\chi\). Testing the bounded-vector estimate with \(x=f_\chi\) gives \(f_\chi\xi=0\). Consequently \(P\le1-f_\chi\).

For the reverse inequality, let \(\omega\in A_*^+\) satisfy \(\omega\le\chi\), and implement it by the vector sum in SC-02. For every \(x\in\mathfrak n_\chi\),

\[
\|xv_j\|^2=\omega_{v_j}(x^*x)
\le\omega(x^*x)\le\chi(x^*x).
\]

Thus each \(v_j\in D_\chi(L)\), with constant one. Hence

\[
\omega(1-P)=\sum_j\|(1-P)v_j\|^2=0.
\]

NW-11, applied at the positive element \(1-P\), gives \(\chi(1-P)=0\). Maximality of \(f_\chi\) implies \(1-P\le f_\chi\), or \(1-f_\chi\le P\). Combining the inequalities proves (SC.4). ∎

Faithfulness gives \(f_\chi=0\), so the denominator \(\psi\) of SC-01 has \(D_\psi\) dense in \(H\). Semifiniteness is still needed elsewhere: it makes the bounded-vector map \(\xi\mapsto R(\xi)\) injective by finite cutoffs. SC-03 alone does not assert that injectivity for an arbitrary normal weight.

## A coefficient ideal with an explicit approximate identity

Return to the setting of SC-01, and set

\[
\mathcal J=\operatorname{span}\{\theta(\xi,\eta):\xi,\eta\in D_\psi\}.
\]

By SD-04 this is an algebraic two-sided *-ideal of \(M\), and

\[
\mathcal J_+=\mathcal J\cap M_+
=\left\{\sum_{j=1}^m\theta(\xi_j,\xi_j):
          \xi_j\in D_\psi,\ m<\infty\right\}.
\tag{SC.5}
\]

**Proposition.** The ideal is ultraweakly dense. More precisely, direct \(\mathcal J_+\) by the usual positive order and put

\[
u_a=a(1+a)^{-1}\qquad(a\in\mathcal J_+).
\tag{SC.6}
\]

Then \(u_a\in\mathcal J_+\), \(0\le u_a\le1\), and \(u_a\uparrow1\) strongly. For any \(x\in M_+\),

\[
x^{1/2}u_a x^{1/2}\in\mathcal J_+,
\qquad x^{1/2}u_a x^{1/2}\uparrow x.
\tag{SC.7}
\]

**Proof.** Addition makes the index set directed. Functional calculus and the ideal property put \(u_a\) in \(\mathcal J_+\). Inverse order gives \(a\le b\Rightarrow u_a\le u_b\), so there is a positive contraction \(u\in M\) which is their strong supremum.

For every fixed \(a\in\mathcal J_+\), all \(ta\), \(t>0\), are indices, and the support-cutoff theorem gives \(u_{ta}\uparrow s(a)\). Thus \(u\ge s(a)\), and a positive contraction dominating a projection is the identity on its range.

These support ranges span \(H\). Indeed, a vector \(v\) orthogonal to all of them is annihilated by every \(\theta(\xi,\xi)\). Therefore \(R(\xi)^*v=0\). Choose the finite positive contraction net \(e_i\uparrow1\) for \(\psi\). Each \(e_i\in\mathfrak n_\psi\), and

\[
\langle e_i\xi,v\rangle
=\langle R(\xi)\Lambda_\psi(e_i),v\rangle=0.
\]

Strong convergence gives \(v\perp\xi\) for every \(\xi\in D_\psi\); SC-03 gives \(v=0\). Thus \(u\) acts as the identity on a dense subspace, and \(u=1\).

The ideal property gives \(xu_a\in\mathcal J\) for every \(x\in M\). This norm-bounded net converges strongly and ultraweakly to \(x\), proving density. Finally, compression of the increasing net by \(x^{1/2}\) preserves positivity and order, gives the strong limit in (SC.7), and stays in the ideal. ∎

This proof supplies actual increasing positive approximants. Ultraweak density of a linear space, by itself, would not supply (SC.7) for passing limits through an infinite-valued normal weight.

## Finite energy and its Hilbert-space closure

Let \(\varphi\) be any normal weight on \(M\). Write \(e=e_\varphi\) and \(f=f_\varphi\) for its finite-domain and null projections, so \(f\le e\). Define

\[
F_\varphi(\xi)=\varphi(\theta(\xi,\xi))
\quad(\xi\in D_\psi),\qquad
E_\varphi=\{\xi\in D_\psi:F_\varphi(\xi)<\infty\}.
\tag{SC.8}
\]

SD-05 proves that \(E_\varphi\) is linear and that

\[
q_\varphi^0(\xi,\eta)
=\widetilde\varphi(\theta(\xi,\eta))
\quad(\xi,\eta\in E_\varphi)
\tag{SC.9}
\]

is a nonnegative sesquilinear form. Here \(\widetilde\varphi\) is the finite linear extension on \(\mathfrak m_\varphi\); its argument is in that domain by SD-05. The proof there needs no semifiniteness of the numerator, so it applies with the present hypotheses.

**Proposition.**

\[
\overline{E_\varphi}^{\,\|\cdot\|}=eH.
\tag{SC.10}
\]

Consequently this form is densely defined on \(H\) exactly when \(\varphi\) is semifinite.

**Proof.** If \(\xi\in E_\varphi\), the positive operator \(\theta(\xi,\xi)\) has finite weight. WS-02 therefore gives \(\theta(\xi,\xi)=e\theta(\xi,\xi)e\). For every \(v\in H\),

\[
\|R(\xi)^*(1-e)v\|^2
=\langle\theta(\xi,\xi)(1-e)v,(1-e)v\rangle=0.
\]

Thus \((1-e)R(\xi)=0\). Testing at \(\Lambda_\psi(e_i)\), with the finite denominator cutoffs \(e_i\uparrow1\), gives \((1-e)e_i\xi=0\). Since \(e\in M\) commutes with \(e_i\in N\), passage to the strong limit gives \(\xi=e\xi\). Hence \(E_\varphi\subseteq eH\).

Conversely, let \(a\in M_+\) have finite \(\varphi\)-weight, and let \(\xi\in D_\psi\). Covariance and the bound \(\theta(\xi,\xi)\le\|R(\xi)\|^2 1\) give

\[
0\le\theta(a^{1/2}\xi,a^{1/2}\xi)
=a^{1/2}\theta(\xi,\xi)a^{1/2}
\le\|R(\xi)\|^2a.
\]

Its weight is finite, so \(a^{1/2}\xi\in E_\varphi\). Density of \(D_\psi\) shows that the closure of \(E_\varphi\) contains \(a^{1/2}H\), and hence its closure \(s(a)H\). By WS-02, the ranges of all these finite positive elements span \(eH\). This proves the reverse inclusion and (SC.10). Finally \(e=1\) is exactly semifiniteness by WS-02. ∎

No invariance of \(E_\varphi\) under arbitrary elements of \(M\) has been asserted. The displayed estimate uses a finite positive element on the outside of a bounded coefficient; a general weight does not satisfy a tracial conjugation bound.

## Lower semicontinuity on bounded vectors

**Theorem.** The function \(F_\varphi:D_\psi\to[0,\infty]\) is lower semicontinuous for the topology inherited from the Hilbert norm of \(H\). The form \(q_\varphi^0\) on \(E_\varphi\) is closable.

**Proof.** For each \(\omega\in M_*^+\) with \(\omega\le\varphi\), choose a representation (SC.3). Since \(R(\xi)\) is bounded,

\[
\omega(\theta(\xi,\xi))
=\sum_j\|R(\xi)^*v_j\|^2
\qquad(\xi\in D_\psi).
\tag{SC.11}
\]

For a fixed vector \(v\in H\), the norm of \(R(\xi)^*v\) has the variational description

\[
\|R(\xi)^*v\|^2
=\sup_{x\in\mathfrak n_\psi}
\left(2\operatorname{Re}\langle v,x\xi\rangle
                         -\|\Lambda_\psi(x)\|^2\right).
\tag{SC.12}
\]

Indeed, the expression equals \(2\operatorname{Re}\langle R(\xi)^*v,\Lambda_\psi(x)\rangle-\|\Lambda_\psi(x)\|^2\), and \(\Lambda_\psi(\mathfrak n_\psi)\) is dense in \(H_\psi\). Completing the square gives the supremum of the squared norm.

Each expression inside the supremum in (SC.12) is norm continuous in \(\xi\) on all of \(H\): \(x\) is one fixed bounded operator. Thus this squared norm is lower semicontinuous on \(D_\psi\). Finite sums of these nonnegative lower semicontinuous functions are lower semicontinuous. Their increasing supremum over finite initial segments is (SC.11), so that function is also lower semicontinuous.

Finally NW-11 gives, including infinite values,

\[
F_\varphi(\xi)
=\sup_{\omega\in M_*^+,\,\omega\le\varphi}
             \omega(\theta(\xi,\xi)).
\tag{SC.13}
\]

A supremum of lower semicontinuous functions is lower semicontinuous. Restricting to \(E_\varphi\) proves relative lower semicontinuity of the diagonal of \(q_\varphi^0\); FC-04 then proves closability. ∎

There is no assumption that \(\|R(\xi_n)\|\) stays bounded when \(\xi_n\to\xi\). Formula (SC.12) was used precisely to make every test continuous without such a bound. Also, the normal-functionals supremum need not be a directed or countable supremum.

## Completion gives the exact core and energy formula

Let \(q_\varphi\) be the canonical closure of \(q_\varphi^0\), constructed by completing its form norm as in FC-02. Write \(V_\varphi=D(q_\varphi)\subseteq eH\).

**Theorem.** The form \(q_\varphi\) is closed and densely defined on \(eH\). Its original domain is exactly

\[
E_\varphi=D_\psi\cap V_\varphi.
\tag{SC.14}
\]

It is a form core: every \(\xi\in V_\varphi\) is the limit of a sequence \(\xi_n\in E_\varphi\) in the norm \((\|\xi\|^2+q_\varphi[\xi])^{1/2}\). On all bounded vectors the exact extended energy identity is

\[
\varphi(\theta(\xi,\xi))=
\begin{cases}
q_\varphi[\xi],&\xi\in V_\varphi,\\
+\infty,&\xi\notin V_\varphi,
\end{cases}
\qquad\xi\in D_\psi.
\tag{SC.15}
\]

These properties determine the closed form uniquely.

**Proof.** Closability is SC-06. FC-02 supplies the closed extension and makes \(E_\varphi\) a form core by construction. Hilbert limits of its form-Cauchy sequences stay in \(eH\) by SC-05, and its domain contains \(E_\varphi\), which is dense there. Thus it is densely defined on \(eH\).

The inclusion \(E_\varphi\subseteq D_\psi\cap V_\varphi\) and equality of its old and new energies follow from extension. Conversely, let \(\xi\in D_\psi\cap V_\varphi\), and choose the core sequence \(\xi_n\in E_\varphi\). Its energies converge to \(q_\varphi[\xi]\). One way to see this is to apply Cauchy–Schwarz for the form to the difference: \(|q_\varphi[\xi_n]^{1/2}-q_\varphi[\xi]^{1/2}|\le q_\varphi[\xi_n-\xi]^{1/2}\). Relative lower semicontinuity from SC-06 gives

\[
\varphi(\theta(\xi,\xi))
\le\liminf_n\varphi(\theta(\xi_n,\xi_n))
=q_\varphi[\xi]<\infty.
\]

Therefore \(\xi\in E_\varphi\). This proves (SC.14); agreement of the extension then gives equality, rather than merely the preceding inequality. The remaining bounded vectors have infinite original energy by the definition of \(E_\varphi\), proving (SC.15).

If another closed form has the same diagonal on \(E_\varphi\) and has \(E_\varphi\) as a form core, polarization gives the same form there. Both forms are the completion of that same form norm with the same inclusion into \(H\), so FC-02 identifies them. ∎

The sequence in this statement approximates one vector in a Hilbert norm. It does not impose a countable exhaustion of \(M\) or a separable Hilbert space. The core condition is necessary for the uniqueness statement; agreement on a merely Hilbert-dense subspace is insufficient.

## All and only the null directions survive at zero energy

**Theorem.**

\[
\{\xi\in V_\varphi:q_\varphi[\xi]=0\}=fH.
\tag{SC.16}
\]

**Proof of the inclusion from the null projection.** For \(\xi\in D_\psi\), covariance gives

\[
\theta(f\xi,f\xi)=f\theta(\xi,\xi)f.
\]

This positive element has \(\varphi\)-weight zero by WS-04. Thus \(fD_\psi\subseteq E_\varphi\) and its energy vanishes. Since \(D_\psi\) is dense, \(fD_\psi\) is dense in \(fH\). For any \(\eta\in fH\), a Hilbert-norm approximating sequence from this space is also form-Cauchy, because all its differences have zero energy. The closure construction puts \(\eta\) in \(V_\varphi\) with zero energy.

**Proof that there are no further null directions.** Choose one vector-sum implementation \((v_{\omega,j})_j\) for every \(\omega\in M_*^+\) dominated by \(\varphi\), and let

\[
L=\overline{\operatorname{span}}
\{y v_{\omega,j}:y\in N,\ j\ge1,\ \omega\le\varphi\}.
\]

This space reduces \(N\), so its projection \(g\) lies in \(M\). For every such \(\omega\),

\[
0\le\omega(f)\le\varphi(f)=0,
\qquad \omega(f)=\sum_j\|fv_{\omega,j}\|^2.
\]

Thus every implementing vector is in \((1-f)H\), and this space is \(N\)-invariant because \(f\in M\). Hence \(g\le1-f\). On the other hand, all implementing vectors lie in \(gH\), so \(\omega(1-g)=0\) for every dominated \(\omega\). NW-11 gives \(\varphi(1-g)=0\), hence \(1-g\le f\). Therefore

\[
L=(1-f)H.
\tag{SC.17}
\]

Now let \(\xi\in V_\varphi\) have zero energy. Choose \(\xi_n\in E_\varphi\) converging to it in form norm. Then \(q_\varphi^0[\xi_n]\to0\). For fixed \(\omega,j\) and \(x\in\mathfrak n_\psi\), (SC.11) gives

\[
|\langle x\xi_n,v_{\omega,j}\rangle|
\le\|\Lambda_\psi(x)\|\,
          \|R(\xi_n)^*v_{\omega,j}\|
\le\|\Lambda_\psi(x)\|\,q_\varphi^0[\xi_n]^{1/2}
\longrightarrow0.
\]

The fixed bounded operator \(x\) preserves Hilbert-norm convergence, so \(\langle x\xi,v_{\omega,j}\rangle=0\). For any \(y\in N\), the denominator's finite cutoffs satisfy \(ye_i\in\mathfrak n_\psi\) and \(ye_i\xi\to y\xi\). It follows that \(\langle y\xi,v_{\omega,j}\rangle=0\) for all \(y\in N\). Replacing \(y\) by its adjoint shows that \(\xi\) is orthogonal to every generator of \(L\). Equation (SC.17) gives \(\xi\in fH\), as required. ∎

The argument uses \(1-f\) as a null-carrier projection during testing. The effective support of the closed form on its actual Hilbert space \(eH\) is \(e-f\). Equating these two projections before imposing semifiniteness would lose the infinite-energy directions.

## The representing operator and its domains

Apply QF-03 to \(q_\varphi\) on \(K=eH\). There is a unique nonnegative self-adjoint operator \(A_\varphi\) on \(K\) such that

\[
D(A_\varphi^{1/2})=V_\varphi,
\qquad q_\varphi(\xi,\eta)
=\langle A_\varphi^{1/2}\xi,A_\varphi^{1/2}\eta\rangle.
\tag{SC.18}
\]

Its operator domain is exactly

\[
\begin{split}
D(A_\varphi)=\{\xi\in V_\varphi:\ &\text{there is }z\in K\text{ with}\\
&q_\varphi(\xi,\eta)=\langle z,\eta\rangle
\text{ for every }\eta\in V_\varphi\},
\end{split}
\qquad A_\varphi\xi=z.
\tag{SC.19}
\]

Uniqueness of \(z\) follows from density in \(K\). The initial finite-energy domain \(E_\varphi\) is an operator core for \(A_\varphi^{1/2}\), because its graph norm is exactly the form norm. Thus the restriction of \(A_\varphi^{1/2}\) to \(E_\varphi\) is essentially self-adjoint on \(K\).

The kernel of \(A_\varphi\) is \(fH\), and its support, viewed as a projection on \(H\), is \(e-f\). To verify the kernel without confusing the two domains, if \(q_\varphi[\xi]=0\), form Cauchy–Schwarz gives \(q_\varphi(\xi,\eta)=0\) for every \(\eta\); (SC.19) then gives \(\xi\in D(A_\varphi)\) and \(A_\varphi\xi=0\). Conversely, an operator-null vector has zero form by (SC.18), or by pairing (SC.19) with itself. Now apply SC-08. For a self-adjoint operator on \(K\), the closure of its range is the orthogonal complement in \(K\) of its kernel, which gives \((e-f)H\).

When \(\varphi\) is semifinite, \(e=1\). We denote this operator on all of \(H\) by

\[
A_\varphi=\frac{d\varphi}{d\psi}.
\tag{SC.20}
\]

Equations (SC.14)–(SC.19) give its full finite-coefficient construction and exact square-root core. Its support is \(1-f=s(\varphi)\), and if \(\varphi\) is also faithful, it has zero kernel. These conclusions do not assert that \(A_\varphi\) is affiliated with \(M\); a spatial derivative generally is not.

When \(e\ne1\), retain the pair \((eH,A_\varphi)\), or equivalently the closed form extended by infinity outside \(V_\varphi\). Adding the zero operator on \((1-e)H\) would give finite zero energy there and violate (SC.15). We make no such extension. This construction for arbitrary normal numerators is stronger in domain generality than the ordinary semifinite-numerator operator statement, while its relative modular identification remains a separate obligation.

## Weight order is exactly closed-form order

For any normal numerator, extend the diagonal of \(q_\varphi\) by \(+\infty\) off \(V_\varphi\). For two such forms, write \(q_\varphi\le q_\rho\) when

\[
V_\rho\subseteq V_\varphi,
\qquad q_\varphi[\xi]\le q_\rho[\xi]
\quad(\xi\in V_\rho).
\tag{SC.21}
\]

This is the order of these extended diagonals on \(H\).

**Theorem.** For arbitrary normal weights \(\varphi,\rho\) on \(M\), with the same denominator \(\psi\),

\[
\varphi\le\rho\quad\Longleftrightarrow\quad q_\varphi\le q_\rho.
\tag{SC.22}
\]

For semifinite numerators this is the usual form order of their spatial derivatives.

**Proof of the forward implication.** Pointwise weight order gives \(E_\rho\subseteq E_\varphi\) and \(q_\varphi^0[\xi]\le q_\rho^0[\xi]\) on \(E_\rho\). Let \(\xi\in V_\rho\), and approximate it by \(\xi_n\in E_\rho\) in the \(q_\rho\)-norm. The inequality applied to differences shows that this sequence is Cauchy in the closed form norm of \(q_\varphi\). Completeness gives a limit in \(V_\varphi\), whose Hilbert-space image must be \(\xi\). Passing to the limits of the two energies proves \(q_\varphi[\xi]\le q_\rho[\xi]\), and also proves the needed domain inclusion.

**Proof of the reverse implication.** Let \(\xi\in D_\psi\). If \(\rho(\theta(\xi,\xi))\) is finite, (SC.14) puts \(\xi\in V_\rho\). The form-order assumption and (SC.15) give

\[
\varphi(\theta(\xi,\xi))\le\rho(\theta(\xi,\xi)).
\]

If the right side is infinite, this inequality holds automatically. Thus it holds for every bounded vector. The positive-cone identity (SC.5) and finite additivity of weights extend it to every element of \(\mathcal J_+\), including infinite values. For \(a\in M_+\), use the increasing approximants (SC.7) and normality:

\[
\begin{aligned}
\varphi(a)
&=\sup_b\varphi(a^{1/2}u_ba^{1/2})\\
&\le\sup_b\rho(a^{1/2}u_ba^{1/2})
=\rho(a).
\end{aligned}
\]

This proves the weight inequality on the whole positive cone. ∎

The construction is therefore injective on normal weights: equal closed spatial forms imply equal weights. An energy comparison on a smaller test set would need an additional core or positive approximation argument; that requirement is met here by SC-04 and SC-07.

## Bounded invertible change of the numerator

Let \(b\in M\) be bounded and invertible, and define

\[
\varphi_b(a)=\varphi(b^*ab)\qquad(a\in M_+).
\tag{SC.23}
\]

This definition fixes the side of each adjoint. The resulting function is a normal weight: conjugation preserves positive addition and increasing positive suprema. We first state the result for arbitrary normal \(\varphi\) as a closed-form identity:

\[
V_{\varphi_b}=(b^*)^{-1}V_\varphi,
\qquad q_{\varphi_b}(\xi,\eta)=q_\varphi(b^*\xi,b^*\eta).
\tag{SC.24}
\]

**Proof.** Invariance of \(D_\psi\) under \(M\), applied to both \(b^*\) and its inverse, makes \(b^*:D_\psi\to D_\psi\) a bijection. Coefficient covariance gives

\[
\varphi_b(\theta(\xi,\xi))
=\varphi(\theta(b^*\xi,b^*\xi)).
\]

Thus \(E_{\varphi_b}=(b^*)^{-1}E_\varphi\), with equality of the corresponding sesquilinear forms by polarization.

Define a form on \((b^*)^{-1}V_\varphi\) by the right side of (SC.24). The norms

\[
\bigl(\|\xi\|^2+q_\varphi[b^*\xi]\bigr)^{1/2}
\quad\text{and}\quad
\bigl(\|b^*\xi\|^2+q_\varphi[b^*\xi]\bigr)^{1/2}
\]

are equivalent, because \(b^*\) and its inverse are bounded. Under \(b^*\), the second is the complete \(q_\varphi\)-norm. The new form is therefore closed. The same norm equivalence and the core property of \(E_\varphi\) make \((b^*)^{-1}E_\varphi\) a core. Uniqueness in SC-07 identifies this closed form with \(q_{\varphi_b}\), proving (SC.24). ∎

In particular the closure of its domain is \((b^*)^{-1}(eH)\). If \(\varphi\) is semifinite, this is all of \(H\), so SC-05 proves that \(\varphi_b\) is also semifinite. In this case the representing operator has the precise formula and domain

\[
\frac{d\varphi_b}{d\psi}
=bA_\varphi b^*,
\qquad
D(bA_\varphi b^*)=(b^*)^{-1}D(A_\varphi).
\tag{SC.25}
\]

The right side is a positive self-adjoint operator on this domain, and its square-root form domain is \((b^*)^{-1}D(A_\varphi^{1/2})\).

To verify the operator assertion directly from the form, a vector \(\xi\in(b^*)^{-1}V_\varphi\) represents a bounded Hilbert functional \(\eta\mapsto q_\varphi(b^*\xi,b^*\eta)\) precisely when there is \(z\in H\) with

\[
q_\varphi(b^*\xi,\zeta)=\langle b^{-1}z,\zeta\rangle
\qquad(\zeta\in V_\varphi),
\]

where \(\eta=(b^*)^{-1}\zeta\) was substituted. By (SC.19), this is equivalent to \(b^*\xi\in D(A_\varphi)\) and \(A_\varphi b^*\xi=b^{-1}z\). Thus \(z=bA_\varphi b^*\xi\). Closed-form representation proves positivity and self-adjointness of this exact operator. For a nonsemifinite numerator we retain (SC.24) on its stated Hilbert subspace; (SC.25) is not asserted as an operator on all of \(H\).

## A coordinate model with infinite directions

Let \(I\) be any set, \(H=\ell^2(I)\), and \(M=N=\ell^\infty(I)\) in its diagonal representation. Choose \(0<v_i<\infty\) for every \(i\), and let

\[
\psi(a)=\sum_{i\in I}v_i a_i\qquad(a\ge0).
\]

The sum is the supremum over finite subsets of \(I\). This weight is normal, semifinite and faithful. Normality follows by interchanging two suprema of nonnegative finite sums, and finite coordinate projections show semifiniteness. Its GNS space is \(\ell^2(I)\), with \(\Lambda_\psi(x)_i=\sqrt{v_i}x_i\); finite-support vectors verify density of this image.

Testing one coordinate and then summing shows

\[
D_\psi=\left\{\xi\in\ell^2(I):
       \sup_{i\in I}\frac{|\xi_i|^2}{v_i}<\infty\right\},
\qquad
R(\xi)=\operatorname{diag}\left(\frac{\xi_i}{\sqrt{v_i}}\right).
\tag{SC.26}
\]

Choose \(w_i\in[0,\infty]\), and define the normal numerator

\[
\varphi(a)=\sum_{i\in I}w_i a_i,
\qquad 0\cdot\infty=0.
\]

Its finite-domain projection is \(e=1_{\{w_i<\infty\}}\), and its null projection is \(f=1_{\{w_i=0\}}\). Indeed, finite positive elements vanish at infinite coordinates, finite coordinate elements span the finite-coordinate corner strongly, and zero weight means that all positive-weight coordinates vanish.

The initial energy is

\[
F_\varphi(\xi)=\sum_{i\in I}\frac{w_i}{v_i}|\xi_i|^2
\qquad(\xi\in D_\psi).
\tag{SC.27}
\]

Its closed domain consists exactly of the vectors vanishing at \(w_i=\infty\) and satisfying

\[
\sum_{\{i:w_i<\infty\}}\frac{w_i}{v_i}|\xi_i|^2<\infty.
\tag{SC.28}
\]

To check closedness explicitly, its energy extended by infinity to \(H\) is

\[
\sup_{\substack{F\subseteq\{w_i<\infty\},\ G\subseteq\{w_i=\infty\}\\
                 F,G\text{ finite},\ t>0}}
\left(\sum_{i\in F}\frac{w_i}{v_i}|\xi_i|^2
      +t\sum_{i\in G}|\xi_i|^2\right).
\]

Each test is continuous. The supremum enforces zero at every infinite-weight coordinate and sums the remaining nonnegative energies, so it is lower semicontinuous. FC-03 gives a closed form. Finite-coordinate truncations at finite-weight coordinates belong to \(E_\varphi\); their squared form-norm error is the corresponding tail of

\[
\sum_{\{i:w_i<\infty\}}
\left(1+\frac{w_i}{v_i}\right)|\xi_i|^2.
\]

Since this sum is finite, its tails outside suitable finite subsets are arbitrarily small, proving the core property. Each vector has at most countably many nonzero coordinates, even when \(I\) is uncountable, so one can choose a sequence of such finite-coordinate truncations. This identifies the displayed form with the closure constructed above.

The representing operator on \(eH\) multiplies by \(w_i/v_i\), with exact operator domain

\[
\left\{\xi\in eH:
\sum_{\{i:w_i<\infty\}}
\left(\frac{w_i}{v_i}\right)^2|\xi_i|^2<\infty\right\}.
\tag{SC.29}
\]

Its null space is \(fH\). Infinite coordinates are outside the form's Hilbert domain; zero coordinates are inside its kernel. If all \(w_i<\infty\), this is the ordinary spatial derivative on \(H\).

## Problems with complete solutions

**1. A noncentral finite-domain projection.** Let \(H=\mathbb C^3\), \(M=B(H)\), \(N=\mathbb C1\), and \(\psi(\lambda1)=\lambda\) for \(\lambda\ge0\). Put \(e=E_{11}+E_{22}\), \(h=2E_{11}\), and define

\[
\varphi(a)=
\begin{cases}
\operatorname{Tr}(ha),&a=eae,\\
+\infty,&a\ne eae
\end{cases}
\quad(a\ge0).
\]

Determine the bounded vectors, the finite-energy domain, and the representing operator.

**Solution.** A positive sum lies in \(eMe\) exactly when both summands do: compression by \(1-e\), positivity and the square-root identity prove this. Thus the formula defines a weight. It is normal because increasing suprema inside this finite-dimensional corner preserve the finite functional, while a supremum outside the strongly closed corner has some net member outside it. The finite cone is all of \((eMe)_+\), and the largest null projection is \(f=E_{22}\).

The denominator GNS space is \(\mathbb C\), every \(\xi\in H\) is bounded, and \(R(\xi)z=z\xi\). Thus \(\theta(\xi,\xi)\) is the rank-one operator \(z\mapsto\langle z,\xi\rangle\xi\). It is supported in \(e\) exactly when \(\xi\in eH\), and then its weight is \(\langle h\xi,\xi\rangle=2|\xi_1|^2\). Hence \(E_\varphi=V_\varphi=eH\), and the operator on \(eH\) is \(\operatorname{diag}(2,0)\). Its kernel is \(\mathbb Ce_2\), while \(\mathbb Ce_3\) has infinite energy. The projection \(e\) is noncentral in \(M\).

**2. Why a faithful denominator still needs semifiniteness.** On a nonzero concrete unital von Neumann algebra \(N\subseteq B(H)\), let \(\chi(0)=0\) and \(\chi(a)=\infty\) for every nonzero positive \(a\). Compute \(D_\chi\), \(H_\chi\), and \(R_\chi\).

**Solution.** This weight is faithful and normal: an increasing positive net with a nonzero supremum has a nonzero member, so its weight supremum is infinite. But \(\mathfrak n_\chi=\{0\}\) and \(H_\chi=\{0\}\). The bounded-vector estimate has only the test \(x=0\), and therefore \(D_\chi=H\). Every \(R_\chi(\xi)\) is the zero map from the zero space. Density in SC-03 still holds, whereas injectivity and a nondegenerate coefficient ideal fail. A coefficient construction with this denominator cannot recover arbitrary numerator weights. The semifiniteness assumption in SC-01 excludes this case.

**3. A form core need not consist of operator-domain vectors.** In the coordinate model take \(I=\mathbb N\), \(v_n=1\), and \(w_n=n^2\). Show that \(D_\psi=H\) but \(E_\varphi=D(A_\varphi^{1/2})\ne D(A_\varphi)\).

**Solution.** Every square-summable sequence is bounded, so (SC.26) gives \(D_\psi=\ell^2\). The finite-energy domain is \(\{\xi:\sum n^2|\xi_n|^2<\infty\}\), while the operator domain is \(\{\xi:\sum n^4|\xi_n|^2<\infty\}\). The vector \(\xi_n=n^{-2}\) lies in the first and not the second. Thus \(E_\varphi\) is the full square-root domain in this example. Calling it a core for \(A_\varphi^{1/2}\) does not put it in \(D(A_\varphi)\).

**4. Recovering a weight from all its coefficient energies.** Suppose \(\varphi,\rho\) are normal weights and \(\varphi(\theta(\xi,\xi))=\rho(\theta(\xi,\xi))\) for every \(\xi\in D_\psi\), with infinity included. Prove \(\varphi=\rho\) without first constructing their representing operators.

**Solution.** By (SC.5), each positive coefficient-ideal element is a finite sum of diagonal coefficients. Weight additivity therefore gives equality on \(\mathcal J_+\). For any \(a\in M_+\), (SC.7) gives increasing positive approximants from that cone. Normality gives equality of the two suprema of their values, hence equality at \(a\). This recovers the whole weight using positive approximation; linear ultraweak density alone would not justify an infinite-valued limit.

## What the construction exports

SC-03 proves bounded-vector density at arbitrary representation size, including the null-support version for every normal weight. SC-04 completes the coefficient-ideal density and supplies an increasing positive approximate identity. SC-05–09 prove the finite-energy domain closure, closability, exact square-root core, existence and uniqueness of the represented closed form, and its complete finite-domain/null-support description. For a normal semifinite numerator this is a nonnegative self-adjoint spatial derivative on \(H\), with support equal to the weight support. SC-10 proves weight/form order equivalence, and SC-11 proves bounded invertible numerator covariance with its actual operator domain.

These results supply the construction and support portions of the earlier **SD-07** and **SD-08** contracts relative to the prerequisites listed in SC-01. The direct/opposite GNS dictionary in SD-07 remains conditional on its stated standard-form input. One approximation works for every normal weight through Increasing weights, finite energy and resolvents now supplies simultaneous bounded-vector approximation, arbitrary normal sums and increasing-weight limits with exact finite-energy domains; its spectral-power conclusion retains the stated semifiniteness and faithful-tail hypotheses. Any bounded change of the numerator through Ordering the denominator reverses energy order supplies bounded numerator form pullbacks, invertible denominator transport and denominator order. These are downstream uses of this construction, not prerequisites of its proofs. Identifying the constructed operator with a relative modular operator, proving modular time covariance and reciprocal derivatives, and proving cocycle formulas and the converse reconstruction theorem remain open. The source automorphism-topology convergence also remains open. In particular, this unit does not claim the full statements of Theorem 3.8, Proposition 3.10 or the later source results as completed packages.

The positive-functional argument and the form-completion argument are independent of modular covariance. This gives a usable analytic construction while preserving the exact obligations needed to connect it to modular dynamics.
