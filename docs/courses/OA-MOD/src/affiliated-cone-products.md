# Unbounded products in the standard positive cone

For a bounded operator \(a\in M\), the standard-form axioms put \(aJaJ\alpha\) in the positive cone whenever \(\alpha\) is in that cone. Extending this observation to an unbounded operator requires two separate domain conditions. It also requires different spectral cutoffs on its initial and final spaces. After proving that extension and giving explicit model constructions, we obtain every cone vector from a positive self-adjoint affiliated operator when \(\alpha\) is cyclic. A comparison of quadratic forms supplies the vector-domain argument.

**Self-checked by the writing AI.** Write \((M,H,J,P)\) for a standard form. Inner products are linear in the first variable. PZ01–03 impose no separability or faithfulness assumption. The existence constructions require a cyclic vector \(\alpha\in P\); PZ07–11 treat every von Neumann algebra under that hypothesis, without a separability assumption on \(H\) or faithfulness of the target vector.

The source problem is Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(13). Hideki Kosaki proves the general existence assertion in [his 1982 paper](https://www.ams.org/journals/proc/1982-084-02/S0002-9939-1982-0637170-5/S0002-9939-1982-0637170-5.pdf), Theorem 2.3 and Lemmas 3.1–3.3, and the positive self-adjoint refinement in [his 1983 sequel](https://www.ams.org/journals/proc/1983-087-02/S0002-9939-1983-0681835-7/S0002-9939-1983-0681835-7.pdf), §§2–3. Both journal editions are freely readable. Our argument retains their strip estimate and positive-extension strategy, while proving the quarter-domain bridge by equality of forms on an explicit core. It does not assume a general adjoint identity for products of spatial \(L^p\) operators. The exposition here is independently written.

## Conjugation and the actual product domain

A closed densely defined linear operator \(T\) is **affiliated with \(M\)** if every unitary \(v\in M'\) preserves its domain and \(Tv\zeta=vT\zeta\) there. In fact every \(b\in M'\) has

\[
 \begin{gathered}
 bD(T)\subseteq D(T),\\
 Tb\zeta=bT\zeta\\
 (\zeta\in D(T)).
 \end{gathered}
 \tag{PZ.1}
\]

Indeed, BK08 expresses \(b\) as a finite linear combination of unitaries in \(M'\). Domain linearity and the defining commutation identities prove both claims. In particular every commutant projection reduces the graph of \(T\); no invariance of the domain under arbitrary operators is being assumed.

Define

\[
 \begin{gathered}
 T'=JTJ,\\
 D(T')=JD(T),\\
 T'(J\zeta)=JT\zeta\\
 (\zeta\in D(T)).
 \end{gathered}
 \tag{PZ.2}
\]

This is a linear closed densely defined operator: anti-linearity occurs twice, and applying the isometry \(J\) to both coordinates transports the closed graph. Since \(JMJ=M'\) by SF05, conjugating the affiliation identities shows that \(T'\) is affiliated with \(M'\).

For \(\alpha\in P\), the same standard-form theorem gives \(J\alpha=\alpha\). Thus \(\alpha\in D(T)\) implies \(\alpha\in D(T')\) and \(T'\alpha=JT\alpha\). The expression we shall use has the following exact meaning:

\[
 \begin{gathered}
 \xi=TT'\alpha\\
 =TJTJ\alpha,\\
 \alpha\in D(T),\\
 JT\alpha\in D(T).
 \end{gathered}
 \tag{PZ.3}
\]

The second condition puts \(\alpha\) in the composition domain of \(TT'\). Neither taking a closure of that product nor assuming that the product is densely defined is part of this notation.

## Initial and final cutoffs

Let \(T\) be as in PZ01. The closed-operator polar decomposition in RD02 gives

\[
 \begin{gathered}
 T=uh,\qquad h\ge0,\\
 D(h)=D(T),\\
 p=u^*u=s(h),\\
 q=uu^*,\\
 u,p,q\in M.
 \end{gathered}
 \tag{PZ.4}
\]

All spectral projections of \(h\) lie in \(M\). For integers \(n\ge1\), put

\[
 \begin{gathered}
 e_n=1_{[0,n]}(h),\\
 g_n=ue_nu^*,\\
 a_n=Te_n\\
 =u(he_n)\in M.
 \end{gathered}
 \tag{PZ.5}
\]

Here \(e_nH\subseteq D(T)\), and \(he_n\) is the bounded spectral function \(t1_{[0,n]}(t)\), of norm at most \(n\). Its membership in \(M\) follows from SK08. Since \(e_n\) commutes with \(p\), direct multiplication shows \(g_n^2=g_n=g_n^*\). Spectral convergence in SK09 gives

\[
 \begin{gathered}
 e_n\longrightarrow I,\\
 g_n\longrightarrow q\\
 \text{strongly},\\
 Te_n\zeta\longrightarrow T\zeta\\
 (\zeta\in D(T)).
 \end{gathered}
 \tag{PZ.6}
\]

On this domain the cutoffs also satisfy

\[
 \begin{gathered}
 g_nT\zeta=ue_np h\zeta\\
 =uh e_n\zeta\\
 =Te_n\zeta.
 \end{gathered}
 \tag{PZ.7}
\]

In the middle equality we used \(ph=h\) on \(D(h)\) and the spectral commutation of \(e_n\) with \(h\). Although \(e_n\) includes the kernel of \(h\), \(g_n\) converges to the final support \(q\), which need not be the identity.

Conjugate these identities by \(J\), writing \(e_n'=Je_nJ\), \(g_n'=Jg_nJ\), \(q'=JqJ\), and \(a_n'=Ja_nJ\). They give

\[
 \begin{gathered}
 a_n'=T'e_n',\\
 a_n'\zeta=g_n'T'\zeta\\
 (\zeta\in D(T')),\\
 g_n'\longrightarrow q'\\
 \text{strongly}.
 \end{gathered}
 \tag{PZ.8}
\]

The first equality is an equality of bounded operators on all of \(H\). The second is asserted on the indicated domain. For a general \(T\), replacing the final cutoff \(g_n'\) by the initial cutoff \(e_n'\) in that second identity would be unjustified.

## Every admissible product is positive

**Theorem.** If \(\alpha\in P\) and the affiliated operator \(T\) satisfies both conditions in PZ.3, then \(TJTJ\alpha\in P\). The operator need not be positive, self-adjoint, injective or surjective, and \(\alpha\) need not be cyclic.

**Proof.** Put \(v=T'\alpha\) and \(\xi=Tv\). These are defined by PZ.3. The range of \(T'\) is contained in \(q'H\), so \(q'v=v\). As \(q'\in M'\), PZ.1 gives

\[
 \begin{gathered}
 q'\xi=q'Tv\\
 =Tq'v\\
 =Tv=\xi.
 \end{gathered}
 \tag{PZ.9}
\]

By PZ.8, \(a_n'\alpha=g_n'v\). Since \(g_n'\in M'\) commutes with the bounded operator \(a_n\in M\),

\[
 \begin{gathered}
 a_nJa_nJ\alpha\\
 =a_ng_n'v\\
 =g_n'Te_nv.
 \end{gathered}
 \tag{PZ.10}
\]

All products on this line are defined: \(e_nH\subseteq D(T)\), and every other operator used in the calculation is bounded. The estimate

\[
 \begin{gathered}
 \|g_n'Te_nv-\xi\|\\
 \le \|Te_nv-Tv\|\\
 +\|(g_n'-q')\xi\|.
 \end{gathered}
 \tag{PZ.11}
\]

tends to zero by PZ.6, PZ.8 and PZ.9. Each left-hand vector in PZ.10 belongs to \(P\) by the bounded standard-cone invariance in SF05. The cone is norm closed, so its limit \(\xi\) belongs to \(P\). \(\square\)

The support identity PZ.9 is essential to this argument: the strong limit of the final cutoffs is \(q'\), not necessarily \(I\). This proof never exchanges two unbounded factors.

## Multiplication operators and a missing-domain example

Consider the standard multiplication form \(M=L^\infty(X,\mu)\) on \(H=L^2(X,\mu)\), with \(Jf=\overline f\) and \(P=L^2(X,\mu)_+\). Assume this is a standard representation and that \(\alpha\in P\) is strictly positive almost everywhere. The latter condition makes it cyclic: for \(f\in L^2\), truncate \(f/\alpha\) to where its absolute value is at most \(n\); multiplication of \(\alpha\) by these bounded functions converges to \(f\) in \(L^2\). Dominated convergence here is the written scalar theorem MCT/DCT, Theorems 2.1–2.2.

Given any \(\xi\in P\), let \(D(T)\) consist of the functions \(f\in L^2\) for which \(tf\in L^2\), where

\[
 \begin{gathered}
 t=\sqrt{\xi/\alpha},\\
 Tf=tf.
 \end{gathered}
 \tag{PZ.12}
\]

All functions are understood almost everywhere, so arbitrary values on the null exceptional set do not matter. The real function \(t\) is finite and nonnegative almost everywhere.

Here are the operator details. The projections \(r_n=1_{\{t\le n\}}\) increase strongly to \(I\), and \(r_nH\subseteq D(T)\); thus the domain is dense. If \(f_k\to f\) and \(Tf_k\to g\) in \(L^2\), bounded multiplication on each cutoff gives \(r_ng=tr_nf\). Letting \(n\) increase shows \(g=tf\) almost everywhere, so \(T\) is closed. The reality of \(t\) makes it symmetric. If \(f\in D(T^*)\), test the adjoint identity against all vectors supported in \(\{t\le n\}\). It gives \(r_nT^*f=tr_nf\); hence \(tf=T^*f\in L^2\). This proves self-adjointness, and its quadratic form is nonnegative. Finally every unitary in \(M'=JMJ=M\) is multiplication by a function of modulus one, and preserves the displayed domain while commuting with \(T\). Thus \(T\) is affiliated.

Cauchy–Schwarz in \(L^2\), proved in BK01, gives

\[
 \begin{gathered}
 \|T\alpha\|_2^2\\
 =\int_X\xi\alpha\,d\mu\\
 \le\|\xi\|_2\|\alpha\|_2,\\
 JT\alpha=T\alpha\\
 =\sqrt{\xi\alpha},\\
 T(JT\alpha)=\xi\in L^2.
 \end{gathered}
 \tag{PZ.13}
\]

These are exactly the two domain checks in PZ.3. Together with PZ03, they prove the full parametrization in this multiplication model.

The second domain condition cannot be omitted even here. On \(\ell^2(\mathbb N)\), with indices \(n\ge1\), take

\[
 \begin{gathered}
 \alpha_n=2^{-2n},\\
 (Tf)_n=2^nf_n.
 \end{gathered}
 \tag{PZ.14}
\]

on its maximal domain. The preceding argument makes \(T\) positive self-adjoint and affiliated with the diagonal algebra, and \(\alpha\) is cyclic. But \(T\alpha=(2^{-n})\) is square summable whereas \(T(JT\alpha)\) would be the constant sequence \(1\). Therefore \(\alpha\in D(T)\) and \(JT\alpha\notin D(T)\).

## The positive Hilbert–Schmidt model

Let \(K\ne0\), let \(\alpha\) be a positive injective Hilbert–Schmidt operator on \(K\), and represent \(B(K)\) on \(\mathcal S_2(K)\) by left multiplication \(L_aZ=aZ\). The finite-trace spectral argument in KL09, applied to \(\alpha^2\), gives an orthonormal basis \((e_j)\) with

\[
 \begin{gathered}
 \alpha e_j=\alpha_j e_j,\\
 \alpha_j>0,\\
 \sum_j\alpha_j^2<\infty.
 \end{gathered}
 \tag{PZ.15}
\]

The index set is finite or countable. Separability is a consequence of this faithful vector, not an extra hypothesis on a type-I factor. The same spectral argument, without injectivity, diagonalizes any positive Hilbert–Schmidt operator on its support; adjoining a basis of its kernel completes an orthonormal basis of \(K\).

For clarity we identify the natural cone in this realization. Use the faithful finite functional with density \(h=\alpha^2\). KL09 identifies its GNS space with \(\mathcal S_2(K)\), its cyclic vector with \(\alpha\), and its modular conjugation with \(JZ=Z^*\). Its modular operator on matrix coefficients is

\[
 (\Delta Z)_{ij}
 =\frac{\alpha_i^2}{\alpha_j^2}Z_{ij}.
 \tag{PZ.16}
\]

The square generators in SF04 are \(\Delta^{1/4}(xx^*\alpha)\), for \(x\in B(K)\). Every finite principal compression of this vector is
\(p\alpha^{1/2}xx^*\alpha^{1/2}p\), by PZ.16, and hence positive. Hilbert–Schmidt convergence implies operator-norm convergence, since rowwise Cauchy–Schwarz gives \(\|Z\|\le\|Z\|_2\). Positivity of all these compressions therefore makes each generator a positive operator, and their closed cone is contained in the positive Hilbert–Schmidt operators.

Conversely, on a finite spectral coordinate subspace \(pK\), write \(\alpha_p=\alpha|_{pK}\). Every positive matrix \(r=prp\) is such a generator: take

\[
 \begin{gathered}
 x=\alpha_p^{-1/2}r^{1/2},
 \end{gathered}
 \tag{PZ.17}
\]

defined on \(pK\) and extended by zero. Direct multiplication gives \(\alpha^{1/2}xx^*\alpha^{1/2}=r\). For any positive \(Z\in\mathcal S_2(K)\), increasing finite coordinate projections have \(pZp\to Z\) in Hilbert–Schmidt norm, by the tails of \(\sum_{i,j}|Z_{ij}|^2\). Thus

\[
 \begin{gathered}
 P=\mathcal S_2(K)_+,\\
 JZ=Z^*.
 \end{gathered}
 \tag{PZ.18}
\]

Matrix units show cyclicity of \(\alpha\): \(E_{ij}=\alpha_j^{-1}E_{ij}\alpha\). Its range is dense, so \(a\alpha=0\) forces \(a=0\), proving separation. Conversely, if a positive Hilbert–Schmidt \(\alpha\) had a nonzero kernel vector, its entire left orbit would annihilate that vector. The continuous evaluation map \(Z\mapsto Zk\) then shows that this orbit could not be dense. This proves that the cyclic positive vectors in the model are exactly the injective ones.

## Existence for every type-I factor with a cyclic vector

Work in PZ05, and let \(\xi\in\mathcal S_2(K)_+\) be arbitrary. Diagonalize it in a complete orthonormal basis \((f_j)\), including its kernel:

\[
 \begin{gathered}
 \xi f_j=\beta_j f_j,\\
 \beta_j\ge0.
 \end{gathered}
 \tag{PZ.19}
\]

Choose any bijection between this basis and the basis in PZ.15, and let \(Ue_j=f_j\). Define the finite scalars

\[
 \begin{gathered}
 d_j=\sqrt{\beta_j/\alpha_j},\\
 De_j=d_je_j.
 \end{gathered}
 \tag{PZ.20}
\]

with the maximal diagonal domain. No uniform bound on \(d_j\) is required. On the Hilbert–Schmidt space define \(A\) on precisely those \(Z\in\mathcal S_2(K)\) for which \(Q(Z)<\infty\), and set

\[
 \begin{gathered}
 Q(Z)\\
 =\sum_{i,j}d_i^2|Z_{ij}|^2,\\
 (AZ)_{ij}=d_iZ_{ij},\\
 T=L_UA,\\
 D(T)=D(A).
 \end{gathered}
 \tag{PZ.21}
\]

The diagonal spectral theorem SK05 makes \(A\) positive self-adjoint. Its spectral projections are left multiplication by the corresponding diagonal projections on \(K\), so \(A\) is affiliated with \(L(B(K))\) by SK08. Multiplication by the unitary \(L_U\) preserves closedness and density of the domain. Every commutant unitary commutes with both \(L_U\) and \(A\) on that domain; hence \(T\) is closed, densely defined and affiliated with the represented algebra.

Set \(C e_j=\sqrt{\alpha_j\beta_j}\,e_j\). Cauchy–Schwarz for the two square-summable eigenvalue sequences gives

\[
 \begin{gathered}
 \sum_j\alpha_j\beta_j\\
 \le\|\alpha\|_2\|\xi\|_2<\infty,\\
 T\alpha=UC,\\
 JT\alpha=CU^*.
 \end{gathered}
 \tag{PZ.22}
\]

In particular \(\alpha\in D(T)\). The second domain check uses the row norms of the unitary matrix \(U^*\):

\[
 \begin{gathered}
 \sum_{i,j}d_i^2|(CU^*)_{ij}|^2\\
 =\sum_i d_i^2\alpha_i\beta_i\\
 =\sum_i\beta_i^2<\infty.
 \end{gathered}
 \tag{PZ.23}
\]

All summands are nonnegative, so passing between the iterated and double sums is justified by their finite-subsum definition. Thus \(JT\alpha\in D(T)\), and the coefficient calculation gives

\[
 \begin{gathered}
 T(JT\alpha)\\
 =U\operatorname{diag}(\beta_j)U^*\\
 =\xi.
 \end{gathered}
 \tag{PZ.24}
\]

These are identities of vectors in \(\mathcal S_2(K)\); no closure of a formal operator product has replaced either domain check. PZ03 proves the reverse containment. This proves the full parametrization for the stated type-I model.

To obtain the assertion for an arbitrary standard representation of a type-I factor, identify the algebra with \(B(K)\). A cyclic cone vector is separating: if \(a\alpha=0\), then \(JaJ\alpha=0\), and commutation with \(M\) makes \(JaJ\) vanish on the dense set \(M\alpha\). Its vector functional is therefore faithful, and it is normal by CP07. It assigns strictly positive masses to the rank-one projections of any orthonormal basis of \(K\). Every finite sum of these masses is at most \(\|\alpha\|^2\), so there are only countably many: for each positive integer \(m\), only finitely many can be at least \(1/m\). Thus \(K\) is separable. Choose any positive injective Hilbert–Schmidt diagonal density to construct the standard model of PZ05. The standard-form unitary in SE10 sends the given cyclic cone vector to a cyclic positive Hilbert–Schmidt vector, hence an injective one by PZ05. Apply the construction above to that vector and the transported target. Conjugation back by this unitary transports the closed graph, affiliation and both product-domain conditions.

In finite dimension there is also a positive choice, which need not diagonalize \(\alpha\) and \(\xi\) in the same basis. Put \(c=\alpha^{1/2}\), and set

\[
 \begin{gathered}
 r=(c\xi c)^{1/2},\\
 b=c^{-1}rc^{-1}.
 \end{gathered}
 \tag{PZ.25}
\]

Positive square roots exist by BK01. Direct multiplication gives \(b\alpha b=\xi\), and \(b\ge0\). Taking \(T=L_b\) works because \(JL_bJ\) is right multiplication by \(b\). Every domain is the full finite-dimensional Hilbert–Schmidt space. In infinite dimension \(\alpha^{-1/2}\) may be unbounded; PZ25 alone is not a definition or a proof of an admissible operator there. The construction PZ20–24 supplies one without that assumption.

The model arguments remain useful even after the general construction below: they display the domains directly and give a different choice of factor. The formal inverse expression in PZ.25 will not be used in the general proof.

## A positive functional between two cone vectors

Assume \(\alpha\in P\) is cyclic and fix \(\xi\in P\). As proved in PZ06, \(\alpha\) is separating. Its faithful finite vector functional has GNS space \(H\), modular conjugation \(J\), and modular operator \(\Delta>0\), by SE06. Put

\[
 \begin{gathered}
 \sigma_t(x)=\Delta^{it}x\Delta^{-it},\\
 \tau_t(b)=\Delta^{it}b\Delta^{-it}\\
 (x\in M,\ b\in M').
 \end{gathered}
 \tag{PZ.26}
\]

Here \(\tau\) is the action on the commutant with this displayed sign convention. Both actions have norm-entire subalgebras, supplied by CZ02 and MA16. Gaussian smoothing gives uniformly bounded strong-star approximants. Write \(M_{\rm an}\) and \(M'_{\rm an}\) for these subalgebras.

We need relative operators for positive functionals which need not be faithful. The precise finite version of the SF13 relative graph, including its zero part, is as follows. For each \(\beta\in P\), there is a positive self-adjoint \(A_\beta\), supported by \(p_\beta=s_M(\omega_\beta)\), such that

\[
 \begin{gathered}
 M\alpha\text{ is a core}\\
 \text{for }A_\beta^{1/2},\\
 A_\beta^{1/2}x\alpha=Jx^*\beta,\\
 A_\beta^{it}b=\tau_t(b)A_\beta^{it}.
 \end{gathered}
 \tag{PZ.27}
\]

Imaginary powers in the last line are zero on \((1-p_\beta)H\), including \(A_\beta^0=p_\beta\); positive powers have the full zero-operator summand there. Moreover \(A_\beta^{it}\Delta^{-it}\in M\) is a contraction.

Here is the support reduction, to avoid using a faithful theorem with an omitted kernel. Complete \(\omega_\beta\) by
\(\rho(x)=\omega_\beta(x)+\omega_\alpha(qxq)\), where \(q=1-p_\beta\). This is a faithful finite normal functional: vanishing at a positive \(x\) makes \(x^{1/2}p_\beta=x^{1/2}q=0\). Also \(\rho(p_\beta x)=\rho(xp_\beta)\), so CZ05 fixes \(p_\beta\) under its modular group. The two summand vectors have orthogonal left and right supports, by SF06; hence the cone vector of \(\rho\) is their sum and \(Jp_\beta J\beta_\rho=\beta\). Let \(R=\Delta_{\rho,\omega_\alpha}\). SF13 and SI08/12 give its relative graph, its two modular actions, and its common conjugation. The projection \(p_\beta\) reduces \(R\).

Take \(A_\beta=R|_{p_\beta H}\oplus0|_{qH}\). To verify the core, approximate an arbitrary \(q\)-component by \(q1_{[1/n,n]}(R)\) applied to it; this changes no \(A_\beta^{1/2}\)-image. The resulting vector is in \(D(R^{1/2})\), where the SF13 core \(M\alpha\) approximates in the stronger graph norm. On that core,
\(JA_\beta^{1/2}x\alpha=Jp_\beta Jx^*\beta_\rho=x^*\beta\).
The commutant identity follows from SI08's second action, transported by SI12, since \(p_\beta\in M\). Finally SI14 gives \(R^{it}\Delta^{-it}\in M\); multiplication by \(p_\beta\) proves the last assertion. None of this reduction requires \(\omega_\beta\le c\omega_\alpha\).

The same core may be restricted to \(M_{\rm an}\alpha\): bounded strong-star smoothing of \(x\) makes both \(x\alpha\) and \(Jx^*\beta\) converge. We will use that graph core, not merely its Hilbert-space density.

By QO01–02, \(\Theta(x)=\Delta^{1/4}x\alpha\) is defined on all of \(M\), is positive into \(P\), and has norm at most \(\|\alpha\|\). Define

\[
 \begin{gathered}
 \psi(x)=\langle\Theta(x),\xi\rangle,\\
 x\in M.
 \end{gathered}
 \tag{PZ.28}
\]

It is a bounded positive functional by self-duality of \(P\). It is normal as well. Indeed, if \(0\le x_i\uparrow x\), put \(v_i=(x-x_i)\alpha\). Then \(v_i\to0\) and
\(\Delta^{1/2}v_i=J(x-x_i)\alpha\to0\).
The spectral inequality
\(\|\Delta^{1/4}v_i\|^2\le\|v_i\|\|\Delta^{1/2}v_i\|\)
therefore gives \(\psi(x_i)\to\psi(x)\). This is the positive normality criterion of CP07.
Let \(\zeta\in P\) be its unique implementing vector, supplied by SF10. Set

\[
 \begin{gathered}
 A=A_\xi,\\
 B=A_\zeta^{1/2}.
 \end{gathered}
 \tag{PZ.29}
\]

Thus \(B\alpha=\zeta\). Our next task is to prove, rather than assume, that \(\zeta\) lies in both quarter-power domains of \(\Delta\).

## A mixed quarter-power estimate on the full finite core

For every \(x\in M\),

\[
 \begin{gathered}
 A^{1/4}x\alpha\\
 \in D(\Delta^{1/4}),\\
 \|\Delta^{1/4}A^{1/4}x\alpha\|\\
 \le \|x\|\sqrt{\|\alpha\|\,\|\xi\|}.
 \end{gathered}
 \tag{PZ.30}
\]

If \(\xi=0\), \(A=0\) and the assertion is immediate. Otherwise fix \(y\in M\) and, on \(0\le\operatorname{Re}z\le1\), put \(v_z=\Delta^{(1-\bar z)/2}y\alpha\) and consider

\[
 \begin{gathered}
 f(z)\\
=\langle A^{z/2}x\alpha,v_z\rangle.
 \end{gathered}
 \tag{PZ.31}
\]

At the imaginary boundary the first power uses the supported convention in PZ.27. Spectral integration on the positive support gives a continuous bounded function on the closed strip and a holomorphic function inside it. Specifically, the squared norms of the two vector factors are bounded by their domain norms at exponents \(0\) and \(1/2\); dominated spectral integration proves continuity and holomorphy. Those domain norms are finite by PZ.27 and the ordinary Tomita graph. Conjugation of \(z\) in the second factor makes \(f\) holomorphic under our first-variable-linear convention.

For real \(t\), put \(C_t=\Delta^{-it/2}A^{it/2}\). The last assertion of PZ07, applied at \(-t/2\) and then adjointed, puts \(C_t\) in \(M\) with norm at most one. Since \(\Delta^{1/2}y\alpha=Jy^*\alpha\),

\[
 \begin{gathered}
 |f(it)|\\
 =|\langle C_t x\alpha,Jy^*J\alpha\rangle|\\
 =|\langle C_t xJyJ\alpha,\alpha\rangle|\\
 \le\|x\|\,\|\alpha\|\,\|y\alpha\|.
 \end{gathered}
 \tag{PZ.32}
\]

Only bounded operators in the mutually commuting algebras were interchanged. At the other boundary, PZ.27 gives

\[
 \begin{gathered}
 |f(1+it)|\\
 \le\|A^{1/2}x\alpha\|\,\|y\alpha\|\\
 \le\|x\|\,\|\xi\|\,\|y\alpha\|.
 \end{gathered}
 \tag{PZ.33}
\]

For completeness, the geometric boundary estimate follows from the constant-bound strip theorem MA08. If the two positive bounds in PZ.32 and PZ.33 are \(m_0,m_1\), apply that theorem, after rotating the strip, to
\(f(z)m_0^{z-1}m_1^{-z}\), whose boundary bounds are one. At \(z=1/2\) this gives \(|f(1/2)|\le\sqrt{m_0m_1}\). If \(x=0\) or \(y=0\), the scalar function is zero and the same conclusion is immediate.

To pass from this scalar estimate to an actual domain statement, \(M\alpha\) is a core for \(\Delta^{1/4}\). Here are the core details. A graph core for a positive self-adjoint \(h\) is a core for \(h^r\), \(0<r<1\): first approximate a vector in \(D(h^r)\) by bounded spectral truncations lying in \(D(h)\), then use the given graph core and \(\lambda^{2r}\le1+\lambda^2\). Apply this with \(h=\Delta^{1/2}\), \(r=1/2\). The bound on
\(\langle A^{1/4}x\alpha,\Delta^{1/4}y\alpha\rangle\)
therefore extends to all of \(D(\Delta^{1/4})\), bounded by the Hilbert norm of the test vector. Self-adjointness identifies the adjoint domain with \(D(\Delta^{1/4})\) and proves both assertions of PZ.30.

## Identify a polar operator by equality of forms

On \(\mathcal E=M_{\rm an}\alpha\), define a linear map

\[
 \begin{gathered}
 K_0(x\alpha)\\
 =A^{1/4}\Delta^{1/4}x\alpha.
 \end{gathered}
 \tag{PZ.34}
\]

This composition is defined there: \(\Delta^{1/4}x\alpha=\sigma_{-i/4}(x)\alpha\), which lies in \(D(A^{1/2})\). Put \(z=\sigma_{-i/4}(x)\). PZ.27 and the ordinary analytic Tomita identity give

\[
 \begin{gathered}
 \|K_0(x\alpha)\|^2\\
 =\langle A^{1/2}z\alpha,z\alpha\rangle\\
 =\langle Jz^*\xi,z\alpha\rangle\\
 =\langle zJzJ\alpha,\xi\rangle\\
 =\langle\Delta^{1/4}xx^*\alpha,\xi\rangle\\
 =\psi(xx^*)\\
 =\|Bx\alpha\|^2.
 \end{gathered}
 \tag{PZ.35}
\]

For the fourth equality, \(JzJ\alpha=\Delta^{1/2}z^*\alpha
=\sigma_{-i/2}(z^*)\alpha\), and
\(z^*=\sigma_{i/4}(x^*)\); hence
\(zJzJ\alpha=\sigma_{-i/4}(xx^*)\alpha\).
All elements involved are entire, so these are identities on actual spectral domains.

Polarization of PZ.35 makes

\[
 \begin{gathered}
 U(Bx\alpha)\\
 =K_0(x\alpha)\\
 (x\in M_{\rm an})
 \end{gathered}
 \tag{PZ.36}
\]

a well-defined isometry on \(B\mathcal E\). The core established in PZ07 makes this subspace dense in \(\overline{\operatorname{Ran}B}=p_\zeta H\). Extend \(U\) isometrically there and set it equal to zero on \((1-p_\zeta)H\). Thus \(U^*U=p_\zeta\). The operator \(K=UB\), with domain \(D(B)\), is closed: convergence of its graph gives convergence of \(B\)-images after applying \(U^*\). The identical graph norms and the same core imply

\[
 \begin{gathered}
 \overline{K_0}=UB,\\
 |K|=B.
 \end{gathered}
 \tag{PZ.37}
\]

This constructs the polar operator from the core; it makes no assertion about the closure of a product on a larger, unexamined domain.

We now prove \(U\in M\). We use this consequence of PZ.27: for \(b\in M'_{\rm an}\) and \(r>0\),

\[
 \begin{gathered}
 bD(A_\beta^r)\\
 \subset D(A_\beta^r),\\
 A_\beta^r b v\\
 =\tau_{-ir}(b)A_\beta^r v\\
 (v\in D(A_\beta^r)).
 \end{gathered}
 \tag{PZ.38}
\]

To justify the complex time, restrict to \(p_\beta H\), where the imaginary powers are a unitary group. The function
\(\tau_z(b)A_\beta^{iz}v\) is bounded and continuous on the closed strip \(-r\le\operatorname{Im}z\le0\), holomorphic inside, and equals \(A_\beta^{it}bv\) on the real boundary. Bounds reduce to the compact imaginary segment for the first factor and the two spectral endpoint norms for the second. The spectral-domain strip criterion MA09 identifies its endpoint with \(A_\beta^rbv\). On the kernel both sides vanish, since \(p_\beta\in M\). This proves PZ.38; the same proof applies to \(\Delta\).

The subspace \(\mathcal E\) is invariant under every \(b\in M'_{\rm an}\). Indeed write \(b=JcJ\) with \(c\in M_{\rm an}\); then
\(b\alpha=\sigma_{-i/2}(c^*)\alpha\), and \(b\) commutes with \(M\). Two applications of PZ.38, at \(r=1/4\), and one at \(r=1/2\), give on \(\mathcal E\)

\[
 \begin{gathered}
 K_0 b=\tau_{-i/2}(b)K_0,\\
 B b=\tau_{-i/2}(b)B.
 \end{gathered}
 \tag{PZ.39}
\]

Consequently \(U\) commutes with \(\tau_{-i/2}(b)\) on \(B\mathcal E\), hence on \(p_\zeta H\). It also commutes on the complement, where it vanishes and which \(M'\) preserves. Complex translation is a bijection of \(M'_{\rm an}\), so \(U\) commutes with that entire subalgebra. Strong density and boundedness give \(U\in(M')'=M\).

Only one adjoint inclusion is now needed. For

\[
 \begin{gathered}
 v\in D(Q)\\
 \iff v\in D(A^{1/4})\\
 \text{and }A^{1/4}v\in D(\Delta^{1/4}),\\
 Qv=\Delta^{1/4}A^{1/4}v.
 \end{gathered}
\]

self-adjoint pairing on the two domains gives
\(\langle K_0w,v\rangle=\langle w,Qv\rangle\), \(w\in\mathcal E\).
Thus \(Q\subset K_0^*=K^*\). PZ08 applies to \(x=U\), so \(U\alpha\in D(Q)\). Since \(K=UB\),

\[
 \begin{gathered}
 \zeta=B\alpha\\
 =Bp_\zeta\alpha\\
 =K^*U\alpha\\
 =\Delta^{1/4}A^{1/4}U\alpha.
 \end{gathered}
 \tag{PZ.40}
\]

Here \(p_\zeta\) is a spectral support of \(B\), so it preserves its domain. Injectivity of \(\Delta\) identifies \(\operatorname{Ran}\Delta^{1/4}\) with \(D(\Delta^{-1/4})\). Equation PZ.40 therefore proves

\[
 \begin{gathered}
 \eta:=\Delta^{-1/4}\zeta\\
 =A^{1/4}U\alpha.
 \end{gathered}
 \tag{PZ.41}
\]

Because \(J\zeta=\zeta\) and \(J\Delta^{1/4}J=\Delta^{-1/4}\), spectral transport also gives

\[
 \begin{gathered}
 \zeta\in D(\Delta^{1/4})\\
 \cap D(\Delta^{-1/4}),\\
 J\eta=\Delta^{1/4}\zeta,\\
 \|\eta\|^2\le\|\alpha\|\,\|\xi\|.
 \end{gathered}
 \tag{PZ.42}
\]

For the last inequality apply spectral Cauchy–Schwarz to
\(A^{1/4}U\alpha\): its squared norm is at most
\(\|U\alpha\|\|A^{1/2}U\alpha\|\le\|\alpha\|\|U^*\xi\|\),
by PZ.27 and \(\|U\|\le1\).

## Build the positive symmetric operator on a specified domain

In this finite GNS representation the multiplication cones from SF03 are

\[
 \begin{gathered}
 C_l=\overline{M_+\alpha},\\
 C_r=\overline{M'_+\alpha},\\
 C_l=C_r^\vee.
 \end{gathered}
 \tag{PZ.43}
\]

Indeed the finite left ideal is all of \(M\), so its square vectors are \(xx^*\alpha\), exhausting \(M_+\alpha\); the same argument in the commutant gives the other cone. SF03 also gives \(C_r\subset D(\Delta^{-1/2})\), while SF04 gives \(\Delta^{-1/4}C_r\subset P\). For \(v\in C_r\), the pairing of the two quarter-power domains consequently yields

\[
 \langle\eta,v\rangle
 =\langle\zeta,\Delta^{-1/4}v\rangle\ge0.
\]

Thus \(\eta\in C_l\).

Define

\[
 \begin{gathered}
 D(a_0)=M'\alpha,\\
 a_0(b\alpha)=b\eta\\
 (b\in M').
 \end{gathered}
 \tag{PZ.44}
\]

The vector \(\alpha\) is separating for \(M'\), so the map is well-defined. It is cyclic for \(M'\), so its domain is dense. Positivity follows from

\[
 \langle a_0(b\alpha),b\alpha\rangle
 =\langle\eta,b^*b\alpha\rangle\ge0.
\]

Polarization makes \(a_0\) symmetric; its adjoint contains its dense domain, so it is closable. Let \(a=\overline{a_0}\). Graph limits preserve positivity and symmetry. Each unitary in \(M'\), together with its inverse, preserves \(D(a_0)\) and commutes with \(a_0\). Passing to graph closures proves that \(a\) is affiliated with \(M\).

We need one more vector in its adjoint domain. In the following computation put \(h=\Delta^{1/4}\). For \(b\in M'_{\rm an}\), PZ.41–42 give

\[
 \begin{gathered}
 \langle J\eta,b\eta\rangle\\
 =\langle h\zeta,bh^{-1}\zeta\rangle\\
 =\langle\zeta,\tau_{-i/4}(b)\zeta\rangle\\
 =\psi\bigl(\sigma_{i/4}(JbJ)\bigr)\\
 =\langle JbJ\alpha,\xi\rangle\\
 =\langle\xi,b\alpha\rangle.
 \end{gathered}
 \tag{PZ.45}
\]

The second line is legitimate because \(\eta\in D(\Delta^{1/4})\), with \(\Delta^{1/4}\eta=\zeta\), and PZ.38 preserves this domain under \(b\). For the third line, antiunitarity and \(J\zeta=\zeta\) give
\(J\tau_{-i/4}(b)J=\sigma_{i/4}(JbJ)\); the sign changes because \(J\) is antilinear. The fourth line is PZ.28 and the entire-vector identity
\(\Delta^{1/4}\sigma_{i/4}(JbJ)\alpha=JbJ\alpha\).

Uniformly bounded strong Gaussian approximation extends PZ.45 to every \(b\in M'\), by convergence on the two fixed vectors \(\eta,\alpha\). Taking conjugates of that equality is exactly the adjoint test for \(a_0\). Therefore

\[
 \begin{gathered}
 J\eta\in D(a_0^*),\\
 D(a_0^*)=D(a^*),\\
 a^*J\eta=\xi.
 \end{gathered}
 \tag{PZ.46}
\]

An adjoint domain is not automatically the domain of the closure. The next step proves the required stronger assertion.

## Promote the adjoint identity to the graph closure

Set \(L=Ja^*J\). Adjoint graph orthogonality shows that the adjoint of a closed densely defined affiliated operator is again affiliated: conjugate its graph identity by any commutant unitary and take orthogonal complements. Thus \(L\) is a closed densely defined operator affiliated with \(M'\). Since \(a_0\subset a\subset a^*\), \(a^*\alpha=\eta\). PZ.46 and \(J\xi=\xi\) consequently give the two actual domain identities

\[
 \begin{gathered}
 L\alpha=J\eta,\\
 L\eta=\xi.
 \end{gathered}
 \tag{PZ.47}
\]

Take the spectral projections \(e_n=1_{[0,n]}(|L|)\) and the bounded cutoffs \(b_n=Le_n\in M'\). The polar and spectral facts proved in PZ02, now in the commutant, imply

\[
 \begin{gathered}
 b_n\alpha\longrightarrow J\eta,\\
 b_n\eta\longrightarrow\xi.
 \end{gathered}
 \tag{PZ.48}
\]

Both limits use vectors in \(D(L)\), established in PZ.47. By the defining domain of \(a_0\),
\(a_0(b_n\alpha)=b_n\eta\).
Thus the pairs in PZ.48 belong to its graph and converge to \((J\eta,\xi)\). We have proved

\[
 \begin{gathered}
 J\eta\in D(a),\\
 aJ\eta=\xi.
 \end{gathered}
 \tag{PZ.49}
\]

Apply the positive-extension theorem SF02 to \(a\). It constructs a positive self-adjoint extension \(T\) from the closed positive form and proves its affiliation with \(M\). Since \(a_0\subset a\subset T\), PZ.44 and PZ.49 give

\[
 \begin{gathered}
 \alpha\in D(T),\\
 T\alpha=\eta,\\
 JT\alpha=J\eta,\\
 J\eta\in D(T),\\
 TJTJ\alpha=\xi.
 \end{gathered}
 \tag{PZ.50}
\]

If \(\xi=0\), the choice \(T=0\) supplies the same conclusion directly. The zero standard form is also immediate. No invertibility of \(\xi\), semifiniteness of \(M\), or separability of \(H\) was imposed.

Combining this construction with PZ03 proves the full product characterization: for cyclic \(\alpha\in P\), every cone vector is an admissible affiliated product, and every such product lies in the cone. The factor may be chosen positive self-adjoint, with
\(\|T\alpha\|^2\le\|\alpha\|\,\|\xi\|\).
The existence of this choice does not assert that every positive self-adjoint factor is the same operator. The finite matrix formula and the independent model constructions remain valid alternatives.
