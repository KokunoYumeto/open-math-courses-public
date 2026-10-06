# Regular representations, Fourier algebra and Fourier–Stieltjes coefficients

*GPT-6 (OpenAI), Codex writing thread, Ultra effort, September 2026. New original prose: CC0. Self-checked by the writing AI.*

An arbitrary locally compact group acts on its own \(L^2\) space from the left and the right. Convolution turns compactly supported functions into a Tomita algebra; its weight measures exactly the \(L^2\) norm of bounded convolution vectors. The same representation also produces functions on the group: its normal coefficients form the Fourier algebra. The group-coordinate unitary connects these facts by turning a left translation into two simultaneous translations. Its group-like equation then reconstructs the original group from the characters of the Fourier algebra. For abelian groups this also gives the Plancherel transform and topological Pontryagin biduality. Returning to general groups, positive convolution functionals become continuous unitary coefficients and finite positive kernels. Full group coefficients form the Fourier–Stieltjes Banach algebra, the regular Fourier algebra is its ideal, and weak* convergence of states is compact-uniform convergence. PF37–44 move to standard Borel groups: derivative versions, invariant measures and modular scale, then reconstruction of a locally compact topology and obstructions in infinite dimensions.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, Chapter VI, §1, Example 1.2, Chapter VII, §3, Proposition 3.1 through Proposition 3.26, printed pp. 65–86, and Exercise VII.3(1)–(7), printed pp. 87–88. Through PF-36 the group is locally compact Hausdorff; the Plancherel and biduality items explicitly specialize to abelian groups. No second-countability, separability, sigma-compactness, unimodularity or finite-Haar-measure assumption is added in those items. PF-37–44 begin with a standard Borel group and the stated measure-class hypotheses; the later items construct a group topology rather than assuming one. The printed Lemma 3.3′ omits a modular factor and makes a false \(C_0\) assertion; the printed Exercise 1(b) makes a version-dependent diagonal claim that is also false as stated. We identify these defects and prove the corrected results.

We use the modular fundamental theorem, the Hilbert-algebra weight construction, the concrete predual, and single-vector representation in standard form. The group-analysis inputs are identified precisely below.

## Group-analysis input at arbitrary cardinality

The preceding programme lessons Haar measure on locally compact groups and The Stone–Weierstrass theorem for functions vanishing at infinity contain the complete group-analysis proofs used here. Both were written by Claude Opus 5.5 (Anthropic), September 2026, under CC0. Their selected proofs were checked against the applications in this lesson by GPT-6.1 Sol (OpenAI), Ultra effort, October 2026.

The Haar-measure lesson proves existence and uniqueness for every locally compact Hausdorff group in **Theorems 8.3 and 9.2**, with the covering-number construction and almost-additivity lemma included. **Theorems 10.1 and 11.1** prove the continuous modular homomorphism and Haar inversion. Its convention \(\mu(Eh)=\Delta(h)\mu(E)\) agrees with (PF.1) when \(\delta=\Delta\). **Proposition 3.1(2),(4)** proves positive continuous Radon densities and \(C_c\)-density in \(L^p\); **Corollary 11.2(5)** supplies the graph core for multiplication by \(\Delta^{1/2}\). **Theorem 14.2(6)** and **Theorem 15.1** prove strong continuity of translations, compactly supported approximate identities indexed by neighborhoods, and the weak-integral convolution formula. None of these group statements assumes second countability or sigma-compactness.

For products, **Section 4 and Theorem 6.2** of the Haar-measure lesson construct the Radon product and prove the onto identification \(L^2(X,\mu)\otimes L^2(Y,\nu)\cong L^2(X\times Y,\mu\hat\times\nu)\) for arbitrary Radon measures on locally compact Hausdorff spaces. The product need not have the same measurable sets as the ordinary measurable product. The Stone–Weierstrass lesson's **Theorem 10.1**, proved through its polynomial, interpolation and lattice lemmas in **Sections 6–10**, applies to self-adjoint subalgebras of \(C_0(X)\) that separate points and vanish nowhere, without a unit or any countability assumption.

Radon measures, Haar measure and Radon product measures on locally compact spaces are also treated in D. H. Fremlin, [*Measure Theory*](https://www1.essex.ac.uk/maths/people/fremlin/mtcont.htm), Volume 4, §§416–417 and 441–443. The existing programme Theorem 6.2 supplies the full generality required here. The following compact-support calculation is retained as a worked specialization of those programme proofs.

For completeness, \(C_c(X)\) is dense in \(L^2(X,\mu)\) for any Radon measure on a locally compact Hausdorff space. It suffices to approximate the indicator of a Borel set \(E\) of finite measure. Given \(\varepsilon>0\), outer regularity gives an open \(U\supset E\) with \(\mu(U\setminus E)<\varepsilon\); then \(\mu(U)<\infty\), and inner regularity on \(U\) gives a compact \(K\subset U\) with \(\mu(U\setminus K)<\varepsilon\). Choose \(h\in C_c(X)\), \(0\le h\le1\), equal to one on \(K\) and supported in \(U\). Then \(\|1_E-h\|_2^2\le\mu(U\setminus E)+\mu(U\setminus K)<2\varepsilon\). Finite-measure simple functions approximate every \(L^2\) vector. This applies both to Haar measure and to the Radon measure \((1+\delta)\,dg\) used in the graph-core argument below.

Write \(m=dg\boxtimes dg\) for the Radon product on \(G\times G\). On finite sums of elementary compactly supported functions, its defining integral gives

\[
 \left\|\sum_i f_i(s)k_i(t)\right\|_{L^2(m)}^2
 =\sum_{i,j}\langle f_i,f_j\rangle_{L^2(G)}
                 \langle k_i,k_j\rangle_{L^2(G)}.
\]

Thus \(f\otimes k\mapsto[(s,t)\mapsto f(s)k(t)]\) extends to an isometric embedding \(L^2(G)\otimes L^2(G)\to L^2(G\times G,m)\). It is onto without a sigma-finiteness assumption. Indeed, the algebraic span of \(C_c(G)\otimes C_c(G)\) separates points and vanishes nowhere in \(G\times G\), so the nonunital Stone–Weierstrass theorem makes it uniformly dense in \(C_0(G\times G)\). For \(F\in C_c(G\times G)\), choose compactly supported cutoffs \(a(s),b(t)\), between zero and one, whose product is one on \(\operatorname{supp}F\). Multiply a uniform approximant to \(F\) by \(a(s)b(t)\). The result is still a finite sum of elementary tensors, all such approximants have support in the fixed compact set \(\operatorname{supp}a\times\operatorname{supp}b\), and uniform convergence there implies \(L^2(m)\) convergence. The preceding \(C_c\)-density argument now proves surjectivity. Folland's Appendix A.17, pp. 282–283, gives a related tensor identification only for sigma-finite measures; the compact-support argument here is the bridge needed for arbitrary \(G\).

The same nonunital Stone–Weierstrass statement applies to the Fourier algebra in PF-08 once its point separation, nonvanishing and self-adjointness have been established.

## Convolution, Tomita structure and the regular commutants

Fix a left Haar measure \(dg\) on \(G\), and let \(\delta:G\to(0,\infty)\) be its continuous modular homomorphism in the convention

\[
 \int_G F(th)\,dt=\delta(h)^{-1}\int_G F(t)\,dt,\qquad
 \int_G F(t^{-1})\,dt=\int_G F(t)\delta(t)^{-1}\,dt.
 \tag{PF.1}
\]

Let \(H=L^2(G,dg)\), with inner product linear in the first variable. The left and right regular representations are

\[
 (\lambda(g)\xi)(t)=\xi(g^{-1}t),\qquad
 (\rho(g)\xi)(t)=\delta(g)^{1/2}\xi(tg).
 \tag{PF.2}
\]

Haar invariance makes the first unitary, and (PF.1) makes the second unitary. Left and right translations commute. They are strongly continuous on \(C_c(G)\) by compact-support uniform continuity, then on \(H\) by density and unitarity. A net of identity neighborhoods suffices; the proof does not select a countable dense family.

On \(\mathcal K=C_c(G)\), put

\[
 (f*k)(t)=\int_G f(s)k(s^{-1}t)\,ds,\qquad
 f^\sharp(t)=\delta(t)^{-1}\overline{f(t^{-1})}.
 \tag{PF.3}
\]

Both operations preserve \(C_c(G)\). Left multiplication extends to the bounded operator

\[
 L_f=\int_G f(s)\lambda(s)\,ds,\qquad
 \|L_f\|\le\|f\|_1,\qquad
 L_fL_k=L_{f*k},\quad L_f^*=L_{f^\sharp}.
 \tag{PF.4}
\]

The integral is weakly defined by bounded continuous matrix coefficients. The product and adjoint formulas follow by Fubini and the inversion identity in (PF.1). Thus
\(\langle f*k,h\rangle=\langle k,f^\sharp*h\rangle\).

Let \(u_U\in C_c(G)_+\) have integral one and support in a shrinking identity neighborhood \(U\). Strong continuity yields

\[
 \|u_U*\xi-\xi\|_2
 \le\sup_{s\in U}\|\lambda(s)\xi-\xi\|_2\longrightarrow0.
 \tag{PF.5}
\]

For \(\xi\in C_c(G)\), each \(u_U*\xi\) is a product of two members of \(\mathcal K\). Hence the products span a dense subspace of \(H\).

Let \(D\) be multiplication by \(\delta\) on its maximal positive spectral domain, and define

\[
 (J\xi)(t)=\delta(t)^{-1/2}\overline{\xi(t^{-1})}.
 \tag{PF.6}
\]

Haar inversion shows that \(J\) is antiunitary and \(J^2=1\). On \(\mathcal K\), \(JD^{1/2}f=f^\sharp\). The graph norm of \(D^{1/2}\) is the \(L^2\) norm for the Radon measure \((1+\delta)dg\); density of \(C_c(G)\) for that measure makes \(\mathcal K\) a graph core. Therefore the closure of the algebraic involution is exactly \(S=JD^{1/2}\), and its modular operator is \(D\).

For \(z\in\mathbb C\), the vector \(U_zf=\delta^{iz}f\) remains in \(\mathcal K\) and depends entirely on \(z\), because \(\log\delta\) is bounded on the support of \(f\). The homomorphism law gives

\[
 U_z(f*k)=(U_zf)*(U_zk),\qquad
 U_z(f^\sharp)=(U_{\bar z}f)^\sharp.
 \tag{PF.7}
\]

Direct multiplication and Haar inversion give the analytic pairings

\[
 \langle U_zf,k\rangle=\langle f,U_{-\bar z}k\rangle,\qquad
 \langle f^\sharp,k^\sharp\rangle=\langle Dk,f\rangle.
 \tag{PF.8}
\]

These verify the Tomita-algebra criterion on its actual closed involution, rather than merely naming a formal modular action.

Write \(M_l=\lambda(G)''\) and \(M_r=\rho(G)''\). Formula (PF.4) puts every \(L_f\) in \(M_l\). Conversely, translating the approximate identity in (PF.5) gives \(L_{f_U}=\lambda(g)L_{u_U}\to\lambda(g)\) strongly for \(f_U(s)=u_U(g^{-1}s)\), so \(L(\mathcal K)''=M_l\). For right multiplication by \(k\in\mathcal K\), substitution and Haar inversion give

\[
 (\xi*k)(t)=\int_G k(u)\delta(u)^{-1/2}
             (\rho(u^{-1})\xi)(t)\,du.
 \tag{PF.9}
\]

For each compactly supported \(k\in\mathcal K\), the coefficient \(k(u)\delta(u)^{-1/2}\) is integrable. Formula (PF.9) therefore defines the bounded right convolution operator \(R_k\in M_r\), with norm at most the integral of that coefficient's absolute value. Thus \(R(\mathcal K)''\subseteq M_r\). The Tomita-algebra commutant theorem, The opposite structure of a Tomita algebra, applies directly to \(\mathcal K\), whose Tomita axioms were checked in (PF.3–8); it identifies \(R(\mathcal K)''=L(\mathcal K)'=M_l'\). This proves \(M_l'\subseteq M_r\). Commutation of the regular translations gives the reverse inclusion \(M_r\subseteq M_l'\), and taking commutants yields

\[
 M_l'=M_r,\qquad M_r'=M_l.
 \tag{PF.10}
\]

Commuting translations alone would supply only one inclusion in (PF.10). The theorem also puts every bounded right multiplier of the full right Hilbert algebra in \(M_l'=M_r\). This conclusion uses the commutant identification; the compact-kernel integral (PF.9) is asserted only for \(k\in C_c(G)\).

## The Plancherel weight

Take the full left Hilbert algebra completion of \(\mathcal K\). The Hilbert-algebra-to-weight theorem assigns to it a faithful normal semifinite weight \(\psi_G\) on \(M_l\). This is the **Plancherel weight**. Its GNS Hilbert space identifies with \(H\) by Recovering the representation and the full algebra. The construction still works when \(G\) is noncompact, \(H\) is nonseparable, and \(\psi_G(1)=\infty\). A vector \(\xi\in H\) has a bounded left multiplier \(L_\xi\) only when it is left bounded relative to the associated right Hilbert algebra; the weight's finite-square identity uses precisely that domain.

## Left coefficients vanish at infinity

For \(\xi,\eta\in H\), define \(c^l_{\xi,\eta}(g)=\langle\lambda(g)\xi,\eta\rangle\). Let \(f^\vee(t)=f(t^{-1})\), a **linear inversion without conjugation or modular factor**. Direct substitution gives

\[
 c^l_{\xi,\eta}(g)
 =(\overline\eta*\xi^\vee)(g)
 =\int_G\overline{\eta(t)}\,\xi(g^{-1}t)\,dt.
 \tag{PF.11}
\]

The scalar integral is absolutely convergent by Cauchy–Schwarz. For \(\xi,\eta\in C_c(G)\), strong continuity makes the coefficient continuous, and it vanishes outside the compact set \(\operatorname{supp}(\eta)\operatorname{supp}(\xi)^{-1}\). For arbitrary \(H\) vectors, approximate both by compactly supported continuous vectors. Unitarity gives the uniform estimate

\[
 \sup_g|c^l_{\xi,\eta}(g)-c^l_{\xi_j,\eta_j}(g)|
 \le\|\xi-\xi_j\|_2\|\eta\|_2
     +\|\xi_j\|_2\|\eta-\eta_j\|_2\longrightarrow0.
 \tag{PF.12}
\]

Thus \(c^l_{\xi,\eta}\in C_0(G)\). This is the full left-coefficient statement of VII.3 Lemma 3.3.

## The right coefficient needs a modular factor

For \(\xi,\eta\in H\), define \(c^r_{\xi,\eta}(g)=\langle\rho(g)\xi,\eta\rangle\). The pointwise scalar meaning of the convolution below is fixed by Haar inversion:

\[
 (\eta^\sharp*\xi)(g)
 :=\int_G\xi(tg)\overline{\eta(t)}\,dt,\qquad
 c^r_{\xi,\eta}(g)=\delta(g)^{1/2}(\eta^\sharp*\xi)(g).
 \tag{PF.13}
\]

At fixed \(g\), Cauchy–Schwarz bounds the integral by
\(\delta(g)^{-1/2}\|\xi\|_2\|\eta\|_2\).
The right coefficient lies in \(C_0(G)\): for compactly supported vectors it is a continuous compactly supported function, and \(L^2\) approximation is uniform in \(g\) because \(\rho(g)\) is unitary. No such uniform argument applies after multiplying it by the unbounded function \(\delta^{-1/2}\).

The printed Lemma 3.3′ claims the equality in (PF.13) **without** \(\delta(g)^{1/2}\), and claims the unscaled convolution is in \(C_0(G)\). Both assertions fail on a nonunimodular group. To see the coefficient discrepancy already with compact supports, take \(g\) with \(\delta(g)\ne1\), choose nonzero \(\eta\in C_c(G)\), and put \(\xi=\rho(g^{-1})\eta\). Then \(c^r_{\xi,\eta}(g)=\|\eta\|_2^2\), whereas the unscaled convolution is \(\delta(g)^{-1/2}\|\eta\|_2^2\).

For the \(C_0\) failure, use the affine group

\[
 G=\{(a,b):a>0,\ b\in\mathbb R\},\quad
 (a,b)(a',b')=(aa',b+ab'),\quad
 dg=a^{-2}\,da\,db,\quad\delta(a,b)=a^{-1}.
 \tag{PF.14}
\]

Choose \(\eta\in C_c(G)\) of norm one, supported where \(1\le a\le1.1\). Let \(g_n=(4^n,0)\) and
\(\xi=\sum_{n\ge1}2^{-n}\rho(g_n^{-1})\eta\).
The summands have disjoint supports in the \(a\)-coordinate, so \(\xi\in H\). They also give

\[
 c^r_{\xi,\eta}(g_n)=2^{-n},\qquad
 \delta(g_n)^{1/2}=2^{-n},\qquad
 (\eta^\sharp*\xi)(g_n)=1.
 \tag{PF.15}
\]

The sequence \(g_n\) leaves every compact set. Hence the unscaled function does not vanish at infinity. The corrected coefficient in (PF.13) does. At the identity \(\delta(e)=1\), so the source's next theorem is not damaged by this printed error.

## The finite-square identity

If \(\xi\in H\) is left bounded relative to the Tomita algebra's associated right algebra, its convolution multiplier \(L_\xi\in M_l\) exists. The exact finite-ideal theorem gives

\[
 \psi_G(L_\xi^*L_\xi)=\|\xi\|_2^2.
 \tag{PF.16}
\]

In particular, this holds for \(\xi\in C_c(G)\). It does not assert bounded convolution for every \(L^2\) vector. The other scalar in the printed Theorem 3.4 can be defined without such an assertion:

\[
 (\xi^\sharp*\xi)(e)
 :=\int_G\delta(s)^{-1}|\xi(s^{-1})|^2\,ds
 =\int_G|\xi(t)|^2\,dt.
 \tag{PF.17}
\]

The last equality is Haar inversion. It needs neither \(\xi^\sharp\in L^2\) nor a bounded operator \(L_{\xi^\sharp}\). For the stated left-bounded vectors, (PF.16) and (PF.17) give
\(\psi_G(L_\xi^*L_\xi)=(\xi^\sharp*\xi)(e)=\|\xi\|_2^2\).

## The structure operator is unitary

On \(H\otimes H\simeq L^2(G\times G)\), set

\[
 (W_G\zeta)(s,t)=\zeta(s,st),\qquad
 (W_G^*\zeta)(s,t)=\zeta(s,s^{-1}t).
 \tag{PF.18}
\]

For a fixed \(s\), left invariance in the second variable makes these inverse isometries. Check the inner products of finite sums of elementary tensors, then extend by their density in \(H\otimes H\); this establishes unitarity without a separability assumption. The operator \(W_G\) is the **structure operator** of Definition 3.5. The map behind it is \(T(s,t)=(s,st)\); no modular correction appears because \(t\mapsto st\) is left translation.

## One translation becomes two

The fiber of \(W_G\) at \(s\) is \(\lambda(s^{-1})\). To prove its von Neumann tensor membership explicitly, fix finitely many test tensors with first factors supported in a compact \(K\). Strong continuity of \(s\mapsto\lambda(s^{-1})\) on their second factors permits a finite Borel partition \(K=\bigsqcup E_j\) with sample points \(s_j\) whose unitary actions approximate every test vector uniformly. The piecewise-unitary operators

\[
 \sum_j m(1_{E_j})\otimes\lambda(s_j^{-1})
   +m(1_{G\setminus K})\otimes1
 \tag{PF.19}
\]

belong to \(L^\infty(G)\bar\otimes M_l\) and converge strongly to \(W_G\) as the test sets and accuracy vary. Strong closure proves \(W_G\in L^\infty(G)\bar\otimes M_l\).

Direct substitution into (PF.18) gives, first on elementary tensors and then on all of \(H\otimes H\),

\[
 W_G^*(\lambda(g)\otimes1)W_G
   =\lambda(g)\otimes\lambda(g).
 \tag{PF.20}
\]

Indeed, the left side sends \(\zeta(s,t)\) to \(\zeta(g^{-1}s,g^{-1}t)\). Equivalently, for coordinate maps \(L_g(s,t)=(g^{-1}s,t)\) and \(D_g(s,t)=(g^{-1}s,g^{-1}t)\), one has \(T\circ L_g\circ T^{-1}=D_g\). Both clauses of VII.3 Lemma 3.6 follow.

Consequently

\[
 \Gamma:M_l\to M_l\bar\otimes M_l,\qquad
 \Gamma(x)=W_G^*(x\otimes1)W_G
 \tag{PF.21}
\]

is a normal injective unital *-homomorphism. The codomain follows because the span of \(\lambda(G)\) is ultraweakly dense and (PF.20) sends each generator into \(M_l\bar\otimes M_l\). On generators, \(\Gamma(\lambda(g))=\lambda(g)\otimes\lambda(g)\).

## Fourier coefficients form a dense self-adjoint algebra

For \(\phi\in(M_l)_*\), set \(u_\phi(g)=\phi(\lambda(g))\). The map \(\phi\mapsto u_\phi\) is injective by ultraweak density of the linear span of \(\lambda(G)\). To identify its range, start with a The concrete predual and its intrinsic norm series
\(\phi(x)=\sum_n\langle x\xi_n,\eta_n\rangle\)
with both vector sequences square summable. The positive normal functional
\(\omega(x)=\sum_n\langle x\xi_n,\xi_n\rangle\)
has a single vector \(\zeta\in H\) by Recovering the representation and the full algebra and Every normal positive functional has a cone vector. Thus

\[
 \sum_n\|x\xi_n\|^2=\|x\zeta\|^2,\qquad
 |\phi(x)|\le
 \Bigl(\sum_n\|\eta_n\|^2\Bigr)^{1/2}\|x\zeta\|.
 \tag{PF.22}
\]

The bounded functional \(x\zeta\mapsto\phi(x)\) extends to \(\overline{M_l\zeta}\). Hilbert-space Riesz supplies \(\theta\in H\) with
\(\phi(x)=\langle x\zeta,\theta\rangle\).
Hence every normal functional is one left coefficient, even when \(H\) is nonseparable.

For \(\alpha=\overline\theta\) and \(\beta=\zeta\), (PF.11) gives

\[
 u_\phi(g)=(\alpha*\beta^\vee)(g)
 =\int_G\alpha(s)\beta(g^{-1}s)\,ds.
 \tag{PF.23}
\]

The integral is scalar and absolutely convergent by Cauchy–Schwarz. The inverted function \(\beta^\vee\) need not belong to \(L^2(G)\) in a nonunimodular group. Conversely every such pair defines a normal vector coefficient. Therefore the source's set

\[
 A(G)=\{\alpha*\beta^\vee:\alpha,\beta\in L^2(G)\}
     =\{u_\phi:\phi\in(M_l)_*\}
 \tag{PF.24}
\]

lies in \(C_0(G)\) by PF-03.

The tensor functional \(\phi\otimes\psi\) is normal on \(M_l\bar\otimes M_l\). Applying it to (PF.21) gives another normal functional \(\chi=(\phi\otimes\psi)\circ\Gamma\), and on each \(g\),

\[
 u_\chi(g)=u_\phi(g)u_\psi(g).
 \tag{PF.25}
\]

Thus \(A(G)\) is closed under pointwise multiplication. Pointwise complex conjugation preserves it because the antiunitary \(C\xi=\overline\xi\) commutes with every \(\lambda(g)\), so
\(\overline{c^l_{\xi,\eta}}=c^l_{C\xi,C\eta}\).

At each \(g\in G\), choose any nonzero \(\xi\in C_c(G)\) and put \(\eta=\lambda(g)\xi\). Then \(c^l_{\xi,\eta}(g)=\|\xi\|_2^2>0\), so the algebra vanishes nowhere, including when \(G\) has only one element. It also separates points. Given \(g\ne h\), choose a relatively compact identity neighborhood \(U\) with \(gU\cap hU=\varnothing\), nonzero \(\xi\in C_c(U)\), and \(\eta=\lambda(g)\xi\). Then \(c^l_{\xi,\eta}(g)=\|\xi\|_2^2\) and \(c^l_{\xi,\eta}(h)=0\). The nonunital Stone–Weierstrass theorem gives

\[
 \overline{A(G)}^{\|\cdot\|_\infty}=C_0(G).
 \tag{PF.26}
\]

This is **uniform density** and not equality of the two norms.

## The predual Banach norm

Transport the intrinsic norm of \((M_l)_*\) through the injective identification (PF.24):

\[
 \|u_\phi\|_{A(G)}=\|\phi\|_{(M_l)_*}.
 \tag{PF.27}
\]

The predual is complete. Its projective vector-series quotient description in The concrete predual and its intrinsic norm shows
\(\|\phi\otimes\psi\|\le\|\phi\|\|\psi\|\):
tensor near-minimal series representatives and take the infimum of their product costs. Since \(\Gamma\) is contractive, (PF.25) now yields
\(\|uv\|_A\le\|u\|_A\|v\|_A\).
Pointwise conjugation is isometric: \(x\mapsto CxC\) is a conjugate-linear isometric normal symmetry of \(M_l\) fixing \(\lambda(g)\). Finally

\[
 \|u_\phi\|_\infty
 =\sup_g|\phi(\lambda(g))|
 \le\|\phi\|=\|u_\phi\|_A.
 \tag{PF.28}
\]

So \(A(G)\) is the commutative Banach algebra called the **Fourier algebra** of \(G\), with pointwise multiplication and predual norm. It is self-adjoint as a subalgebra of \(C_0(G)\).

For a finite group with counting Haar measure, \(c^l_{\delta_e,\delta_g}\) is the point mass at \(g\). Hence \(A(G)=\mathbb C^G\) as a set, while (PF.27), not the supremum norm, specifies its Fourier-algebra norm.

**Problem 1.** Explain why the two regular representations commuting does not by itself prove \(M_l'=M_r\).

**Solution.** Commutation yields \(M_r\subseteq M_l'\), but gives no description of all operators in \(M_l'\). Formula (PF.9) places the compact-kernel right convolution generators \(R_k\), \(k\in C_c(G)\), in \(M_r\). MF-11 identifies their generated von Neumann algebra \(R(C_c(G))''\) with \(M_l'\), so \(M_l'\subseteq M_r\). Only after this equality is established do we locate every full-algebra bounded right multiplier in \(M_r\).

**Problem 2.** Why does \(\alpha*\beta^\vee\) in (PF.23) make sense even if \(\beta^\vee\notin L^2(G)\)?

**Solution.** For fixed \(g\), read it as \(\int\alpha(s)\beta(g^{-1}s)\,ds\). Both displayed factors are in \(L^2(G)\), since left translation is unitary. Cauchy–Schwarz bounds the absolute integral by \(\|\alpha\|_2\|\beta\|_2\); no \(L^2\) norm of the inverted function is needed.

## Group-like operators and Fourier characters

Put \(M=M_l\) and retain \(H\), \(W\) and \(\Gamma\) from PF-01 and PF-06–07. For nonzero \(x\in B(H)\), call \(x\) **group-like** when \(W^*(x\otimes1)W=x\otimes x\). We prove the following three conditions equivalent:

1. \(x\) is group-like.
2. \(x\in M\), and \(\chi_x(u_\varphi)=\varphi(x)\) is a nonzero character of \(A(G)\).
3. \(x=\lambda(g)\) for a unique \(g\in G\).

This is Takesaki II VII.3 Theorem 3.9. The proof below replaces the source's measure-gluing route by a compact-support tensor approximation and an \(L^2\) power estimate. Lemma 3.10 and Remark 3.11 supply the pairing; all seven clauses of Lemma 3.12 follow after the reconstruction. The later structural clauses are not premises of the hard implication.

The operator \(W\in L^\infty(G)\bar\otimes M\) commutes with \(1\otimes\rho(g)\). Consequently \(\Gamma(x)\) commutes with this operator for every \(x\in B(H)\). If \(\Gamma(x)=x\otimes x\) and \(x\ne0\), then

\[
 x\otimes[x,\rho(g)]=0.
\]

Take a matrix-element slice of the first tensor factor that is nonzero on \(x\). It follows that \([x,\rho(g)]=0\), hence \(x\in M\).

Write \(f_\varphi=u_\varphi\) for the normal coefficient in PF-08. For \(a\in M\), the Fourier product satisfies

\[
 (\varphi\cdot\psi)(a)=(\varphi\otimes\psi)(\Gamma(a)).
 \tag{PF.29}
\]

Thus \(\Gamma(x)=x\otimes x\) makes \(\varphi\mapsto\varphi(x)\) multiplicative and nonzero. Conversely, multiplicativity gives equal pairings of \(\Gamma(x)\) and \(x\otimes x\) with every elementary normal product functional. These functionals separate \(M\bar\otimes M\): their vector-functional pairings include all matrix elements between elementary Hilbert tensors, whose spans are dense. Therefore conditions 1 and 2 are equivalent. Condition 3 implies condition 1 by \(\Gamma(\lambda(g))=\lambda(g)\otimes\lambda(g)\).

Let \(C\xi=\overline{\xi}\) and set

\[
 \widehat x=Cx^*C.
 \tag{PF.30}
\]

The conjugation \(C\) commutes with every \(\lambda(g)\), so \(CMC=M\). On \(H\otimes H\), the structure unitary commutes with \(C\otimes C\). Taking adjoints and then tensor conjugates in the group-like equation proves

\[
 \Gamma(\widehat x)=\widehat x\otimes\widehat x
 \quad\hbox{whenever}\quad
 \Gamma(x)=x\otimes x.
 \tag{PF.31}
\]

No claim that \(x\) is real or unitary has been made at this stage.

## The structure pairing and integrated duality

For \(a\in L^1(G)\), define \(\lambda(a)=\int a(s)\lambda(s)\,ds\) weakly; it is bounded with norm at most \(\|a\|_1\). Directly from \(W\), for \(f,\xi,\eta,\zeta\in H\),

\[
 \langle W(f\otimes\xi),\eta\otimes\zeta\rangle
 =\int f(s)\overline{\eta(s)}
       \langle\lambda(s^{-1})\xi,\zeta\rangle\,ds
 =\langle\xi,\lambda(\overline f\,\eta)\zeta\rangle .
 \tag{PF.32}
\]

The scalar integral is absolutely bounded by
\(\|f\|_2\|\eta\|_2\|\xi\|_2\|\zeta\|_2\). Prove the identity on compactly supported continuous vectors using the Radon-product integral, then extend by this bound and Hilbert tensor density. This gives all the variables of source Lemma 3.10 at their stated \(L^2\) generality. The complex conjugation in the final integrated argument is fixed here explicitly by the linear-first inner-product convention.

The function in the integrand is

\[
 \langle\lambda(s^{-1})\xi,\zeta\rangle
 =(\xi*\zeta^b)(s),\qquad
 \zeta^b(t)=\overline{\zeta(t^{-1})},
\]

where the convolution means its absolutely convergent scalar coefficient formula; \(\zeta^b\) need not itself be an \(L^2\) vector. The displayed function is \(\overline{c^l_{\zeta,\xi}(s)}\), so it belongs to \(A(G)\) by PF-08, and \(f\overline\eta\in L^1(G)\) by Cauchy–Schwarz. This proves both membership assertions in the source's coefficient form of (PF.32).

For every \(a\in L^1(G)\) and \(\varphi\in M_*\), weak integration and the normal vector-series expansion give

\[
 \varphi(\lambda(a))
 =\int_G a(s)f_\varphi(s)\,ds.
 \tag{PF.33}
\]

Absolute summability is justified by
\(\sum_j\|\xi_j\|_2\|\eta_j\|_2<\infty\) and the uniform coefficient bound. With \(m(f_\varphi)\) denoting pointwise multiplication, the same identity is \(\langle m(f_\varphi),a\rangle=\langle\lambda(a),\varphi\rangle\) under the \(L^\infty\)–\(L^1\) pairing. Formula (PF.33) is precisely the \(L^1\)-\(L^\infty\) / \(M\)-\(M_*\) duality of Remark 3.11. It does not require a Bochner integral in the operator norm.

## Two actions on compact coefficients

Let \(E\) be the linear span of

\[
 c_{\xi,\eta}(s)=\langle\lambda(s)\xi,\eta\rangle,
 \qquad \xi,\eta\in C_c(G).
\]

Every member of \(E\) is in \(A(G)\cap C_c(G)\), and \(E\) is dense in \(A(G)\) in its norm: approximate finite vector-series representatives by \(C_c\) vectors and use the vector-functional estimate. This uses individual norm approximations, not a countable basis for \(H\).

For \(x\in M\), define a bounded normal-module map \(\Theta_x:A(G)\to A(G)\) by

\[
 (\Theta_x f_\varphi)(s)=\varphi(\widehat x\,\lambda(s)),
 \qquad \|\Theta_x\|\le\|x\|.
 \tag{PF.34}
\]

It agrees on \(E\) with the ordinary action of \(x\) on the \(L^2\) function:

\[
 x f=\Theta_x f\quad\hbox{in }L^2(G),\qquad f\in E.
 \tag{PF.35}
\]

Indeed, put \(\xi^\vee(t)=\xi(t^{-1})\). The coefficient formula is
\(c_{\xi,\eta}=\overline\eta*\xi^\vee\). Right convolution by the compactly supported function \(\xi^\vee\) is a bounded operator in \(M'=\rho(G)''\), so it commutes with \(x\). Hence

\[
 x c_{\xi,\eta}
 =(xC\eta)*\xi^\vee
 =c_{\xi,CxC\eta}.
\]

The last coefficient is continuous and vanishes at infinity, and at \(s\) it equals

\[
 \langle\lambda(s)\xi,CxC\eta\rangle
 =\langle\widehat x\,\lambda(s)\xi,\eta\rangle .
 \tag{PF.36}
\]

This proves (PF.35), including its pointwise continuous representative.

If \(x\) is group-like, then \(\widehat x\lambda(s)\) is group-like for every \(s\). Formula (PF.29) therefore implies, for every \(f,h\in A(G)\),

\[
 \Theta_x(fh)=(\Theta_x f)(\Theta_x h).
 \tag{PF.37}
\]

This multiplicativity comes from the tensor equation; it has not yet been inferred from a translation formula.

## Fixed compact support in two norms

For \(f\in E\) and an integer \(n\ge1\), there are \(f_k\in E\) with a common compact support such that

\[
 \|f_k-f^n\|_A+\|f_k-f^n\|_2\longrightarrow0.
 \tag{PF.38}
\]

Here is the needed support control. First treat a product of \(n\) compact vector coefficients. On \(H^{\otimes n}=L^2(G^n)\), set

\[
 (U_nF)(s,r_2,\ldots,r_n)
 =F(s,sr_2,\ldots,sr_n).
 \tag{PF.39}
\]

Left Haar invariance in each \(r_j\) makes \(U_n\) unitary, and direct substitution gives

\[
 U_n\lambda(g)^{\otimes n}U_n^*
 =\lambda(g)\otimes1.
 \tag{PF.40}
\]

For \(n=1\), the second tensor factor is \(\mathbb C\). Iterating the Radon-product tensor bridge above identifies \(H^{\otimes n}\) with \(L^2(G^n)\); its proof applies to each finite product, which is again locally compact. The coordinate map is a homeomorphism. Thus it sends the tensor products of \(C_c\) vectors to compactly supported continuous vectors on \(G^n\). Approximate each transformed vector by finite elementary tensors in
\(C_c(G)\odot C_c(G^{n-1})\), choosing cutoffs equal to one on its support projections. The Radon-product density argument gives \(L^2\) convergence while all first tensor factors remain supported in fixed compact sets \(K\) and \(L\) for the two vectors.

Their coefficients for \(\lambda(g)\otimes1\) are finite sums in \(E\); all have support in the fixed compact set \(LK^{-1}\). Vector-functional norm bounds give convergence in \(\|\cdot\|_A\), and hence uniform convergence. With the fixed support and finite Haar measure of \(LK^{-1}\), this also gives \(L^2\) convergence. Since \(f^n\) expands as a finite sum of such products when \(f\in E\), finite unions of these support sets prove (PF.38).

The maps \(x:H\to H\) and \(\Theta_x:A(G)\to A(G)\) are bounded. Apply them to (PF.38), use (PF.35), and compare the \(L^2\) and uniform limits. Choose a subsequence whose squared \(L^2\) errors have finite sum. Sequential monotone convergence applied to the sum of their squared pointwise errors gives convergence almost everywhere on the whole measure space, even when it is not sigma-finite. The uniform limit of the continuous representatives is \(\Theta_x(f^n)\), so the two limits agree almost everywhere. Consequently

\[
 x(f^n)=\Theta_x(f^n)\quad\hbox{in }L^2(G),\qquad f\in E.
 \tag{PF.41}
\]

No arbitrary net version of dominated convergence is used.

## The character space is the original group

Let \(x\ne0\) be group-like and \(f\in E\). Set \(h=\Theta_x f=xf\). Then \(h\in A(G)\cap L^2(G)\). From (PF.37) and (PF.41),

\[
 h^n=x(f^n),\qquad
 \|h^n\|_2\le\|x\|\,\|f^n\|_2
 \le\|x\|\,\|f\|_\infty^{n-1}\|f\|_2.
 \tag{PF.42}
\]

It follows that \(\|h\|_\infty\le\|f\|_\infty\). To check this implication without a finite-total-measure assumption, suppose \(a>\|f\|_\infty\) and the set \(\{|h|>a\}\) has positive measure. Its measure is finite since \(h\in L^2\). The lower bound \(a^n\mu(\{|h|>a\})^{1/2}\) for \(\|h^n\|_2\) contradicts (PF.42) as \(n\to\infty\). The case \(f=0\) is immediate. Since \(h\) is continuous and Haar measure is positive on every nonempty open set, its essential supremum is its pointwise supremum.

At the identity, (PF.34) therefore gives

\[
 |\chi_{\widehat x}(f)|
 =|(\Theta_x f)(e)|
 \le\|f\|_\infty,\qquad f\in E.
 \tag{PF.43}
\]

The \(A\)-norm density of \(E\) and \(\|\cdot\|_\infty\le\|\cdot\|_A\) extend (PF.43) to all \(A(G)\). Thus the nonzero character \(\chi_{\widehat x}\) extends, by the uniform density of \(A(G)\), to a nonzero bounded character of \(C_0(G)\).

For clarity, every such character is evaluation at one point of \(G\), with no metrizability hypothesis. Let \(G^+\) be the one-point compactification, taking an isolated extra point when \(G\) is compact. Extend the character unitally to \(C(G^+)=C_0(G)+\mathbb C1\). Its value on any function lies in that function's range, since a nowhere-zero continuous function is invertible. It therefore respects complex conjugation. If its kernel had no common zero, compactness would give finitely many kernel functions whose sum of squared moduli is positive everywhere, invertible and still in the kernel, a contradiction. At a common zero \(g\), applying this to \(F-\chi(F)1\) gives \(\chi(F)=F(g)\) for every \(F\). The point cannot be the added infinity because the original character is nonzero on \(C_0(G)\).

We have proved \(\varphi(\widehat x)=\varphi(\lambda(g))\) for every \(\varphi\in M_*\), so

\[
 \widehat x=\lambda(g),\qquad x=\lambda(g^{-1}).
 \tag{PF.44}
\]

This proves condition 1 implies condition 3, and completes Theorem 3.9. Uniqueness of the group element follows from point separation by \(A(G)\).

Conversely, every nonzero character of the Banach algebra \(A(G)\) is automatically bounded. Extend it algebraically to the unitization. If \(|\chi(a)|>\|a\|_A\), the element \(1-a/\chi(a)\) is invertible by its norm-convergent Neumann series but has character value zero, contradicting the multiplicative identity for it and its inverse. Thus \(|\chi(a)|\le\|a\|_A\). Since \(A(G)^*=M\), condition 2 applies. Therefore the complete character space of \(A(G)\) consists exactly of the evaluations at \(G\).

## Structural clauses and operator topology

We may now write every group-like operator as \(x=\lambda(g)\). This proves each clause of Lemma 3.12 without feeding it back into PF-14:

1. Adjoints, pointwise conjugates and transposes preserve the group-like set:
\(x^*=\lambda(g^{-1})\), \(CxC=x\), and \(\widehat x=x^*\).
2. Products are \(\lambda(g)\lambda(h)=\lambda(gh)\); in fact they are always nonzero.
3. The polar factors are \(u=x\) and \(|x|=1=\lambda(e)\).
4. For \(f,\xi\in L^2(G)\cap L^\infty(G)\), direct translation gives the exact source identity

\[
 m(f)x\xi=x\,m(\xi)\widehat x f.
 \tag{PF.45}
\]

Both sides are in \(L^2\); no multiplication by a general unbounded vector is treated as a bounded operator.

5. A nonzero group-like projection is a unitary projection and hence equals \(1\).
6. The group-like set is a group of unitaries in \(M\) commuting with \(C\).
7. Each member preserves \(L^2\cap L^\infty\), acts multiplicatively there, and satisfies

\[
 \lambda(g)(\xi\eta)=(\lambda(g)\xi)(\lambda(g)\eta),\qquad
 m(\lambda(g)f)=\lambda(g)m(f)\lambda(g)^*.
 \tag{PF.46}
\]

Left Haar invariance preserves both norms.

The source's operator-topology assertion also follows directly. The injective map \(g\mapsto\lambda(g)\) is strongly continuous. For an identity neighborhood \(U\), choose a relatively compact neighborhood \(V\) with \(VV^{-1}\subset U\) and nonzero \(\xi\in C_c(V)\). Then \(c_{\xi,\xi}(e)=\|\xi\|_2^2\) and its support is contained in \(VV^{-1}\). If \(\lambda(g_i)\to1\) weakly, this coefficient is eventually nonzero, so \(g_i\in U\). Translating the argument proves inverse continuity at every \(g\). Thus \(\lambda\) is a homeomorphism from \(G\) onto the group-like set in the weak operator topology. Weak and strong operator topologies agree on unitaries when the limit is unitary, by the norm-square identity; multiplication and inversion are then continuous. The group-like set is locally compact with exactly the original group topology.

The same identification is a homeomorphism from \(G\) onto the character space with its weak-* topology. Each \(f\in A(G)\) is continuous, so evaluation is continuous. Conversely the compact coefficients used above detect every identity neighborhood, and hence give continuity of the inverse. Equivalently, on the norm-one regular unitaries, normal vector-series pairings are uniform limits of finite vector pairings, so the weak operator and weak-* topologies agree.

**Problem 3.** Why does a bound in the Fourier-algebra norm alone not identify a character as evaluation on \(G\)?

**Solution.** Although \(\|f\|_\infty\le\|f\|_A\), a bound by the larger norm does not permit extension through uniform density to \(C_0(G)\). The fixed-support bridge and power estimate prove the stronger bound \(|\chi_{\widehat x}(f)|\le\|f\|_\infty\). This is the step that permits the extension and point identification.

## The abelian convolution algebra and its spectrum

The remainder specializes to a locally compact Hausdorff **abelian** group \(G\), with fixed Haar measure \(dg\). Then \(\delta=1\). Put \(M=\lambda(G)''\) and retain its Plancherel weight \(\psi_G\). No countability or finite-measure assumption is introduced.

The spectrum \(Y\) of the group C*-algebra consists of continuous unitary characters \(p:G\to\mathbb T\). We retain the source's coupling and Fourier convention:

\[
 \langle g,p\rangle=\overline{p(g)},\qquad
 (\mathcal F f)(p)=\int_Gp(g)f(g)\,dg,\qquad
 (p+q)(g)=p(g)q(g).
 \tag{PF.47}
\]

We prove the complete statements of Takesaki II VII.3.13–3.17: the induced Radon measure, the onto Parseval unitary, the entire multiplication von Neumann algebra, the inverse integral on \(L^1(Y)\cap L^2(Y)\), the dual compact-uniform/weak-* topology, Haar invariance and topological Pontryagin biduality. The dual measure is named the Plancherel measure and \(Y=\widehat G\) is the dual group. The proof follows these implications in order; biduality is not a premise of Haar invariance or regular faithfulness.

The existing programme lesson C*-algebras: continuous functional calculus, **Theorem 2.1**, contains the complete unital and nonunital Gelfand proof used here. Its **Theorem 1.3** identifies the norm of a normal element with its spectral radius; the Banach-algebra lesson, **Propositions 10.2–10.3 and Theorem 11.1**, supplies the character space and the Gelfand norm formula. Thus the transform is isometric and has closed range. Characters preserve the involution, and the range separates characters and vanishes nowhere. The nonunital Stone–Weierstrass theorem then makes that range all of \(C_0(Y)\); no identity or countability assumption is needed.

The existing Haar-measure lesson, **Definition 2.1, Theorem 2.2 and Proposition 2.3**, contains the full locally compact Hausdorff Riesz representation proof needed in PF-18. Its Radon convention is finite measure on compact sets, outer regularity on Borel sets, and inner regularity on open sets. Inner regularity on sigma-finite Borel sets follows from Proposition 2.3; it is not asserted for every Borel set of an arbitrary non-sigma-compact space. **Section 13** proves the local Haar completion used in PF-21.

These are existing programme proof owners, written by Claude Opus 5.5 (Anthropic), September 2026, under CC0. GPT-6.1 Sol (OpenAI), Ultra effort, checked the selected complete proofs and their applications here in October 2026. Fremlin's *Measure Theory*, Volume 4, §§416–417 and 436, and the earlier pinned Mathlib comparison remain references; the current proof-provider bindings are to the written programme lessons.

For \(f\in L^1(G)\), use \(f^*(g)=\overline{f(g^{-1})}\). Define

\[
 \|f\|_u=\sup_U\left\|\int_G f(g)U(g)\,dg\right\|\le\|f\|_1,
 \tag{PF.48}
\]

over strongly continuous unitary representations. Quotient its zero kernel and complete in this C*-norm to obtain \(C^*(G)\). Left convolution on \(L^2(G)\) is one such representation.

For completeness, the usual correspondence with nondegenerate bounded *-representations of \(L^1(G)\) has an elementary approximate-identity proof. If \(\pi\) is such a representation, it is contractive for the \(L^1\) norm: spectra decrease under its unital extension, so

\[
 \|\pi(f)\|^2=r(\pi(f^* * f))\le r(f^* * f)\le\|f\|_1^2.
\]

For a positive compact approximate identity \(e_i\) of \(L^1\)-norm one, \(\pi(e_i)\to1\) strongly. On the dense span of \(\pi(f)\xi\), the uniformly bounded operators \(\pi(\lambda(g)e_i)\) converge to the map

\[
 U(g)\pi(f)\xi=\pi(\lambda(g)f)\xi.
 \tag{PF.49}
\]

The convolution identity \((\lambda(g)e_i)*f=\lambda(g)(e_i*f)\) proves existence of the limit. Applying the same construction at \(g^{-1}\), or multiplying on this dense span, gives \(U(g)U(h)=U(gh)\) and inverse \(U(g^{-1})\). Since each map and inverse are contractions, \(U(g)\) is unitary. Translation continuity in \(L^1\) gives strong continuity. Integrating (PF.49), first for compact continuous \(f\) and then by \(L^1\) approximation, recovers \(\pi(f)\). Degenerate representations restrict to this construction on their essential subspace and vanish on its orthogonal complement. Hence (PF.48) is also the universal norm over bounded *-representations.

The algebra is commutative because \(G\) is abelian. The Gelfand theorem identifies

\[
 C^*(G)\cong C_0(Y),\qquad Y=\operatorname{Sp}(C^*(G)).
 \tag{PF.50}
\]

Each spectrum point is a nonzero scalar *-representation; (PF.49) produces a continuous unitary character \(p\). Conversely every such character integrates to a spectrum point. Equality of their integrals on \(L^1\) implies equality of the continuous characters: a nonzero difference is detected by a compact continuous test function and Haar full support. Thus \(Y\) is exactly the set of continuous unitary characters and the Gelfand transform on \(L^1\) is (PF.47). This supplies Definition 3.13, including its source sign convention.

## Regular faithfulness by finite translation averages

We prove the regular representation faithful on \(C^*(G)\), rather than assuming full and reduced norms coincide. Given compact \(K\subset G\) and \(\varepsilon>0\), choose \(a\in C_c(G)_+\), \(\int a=1\). Translation continuity gives an identity neighborhood \(V\) with
\(\|\lambda(v)a-a\|_1<\varepsilon/2\) for \(v\in V\). Cover \(K\) by finitely many \(g_jV\), \(1\le j\le r\). Let

\[
 P_{j,n}=\frac1n\sum_{k=0}^{n-1}\lambda(g_j)^k,\qquad
 a_n=P_{1,n}\cdots P_{r,n}a.
 \tag{PF.51}
\]

These commuting contractions preserve positivity and integral one; \(a_n\in C_c(G)\). The telescoping bound
\(\|\lambda(g_j)a_n-a_n\|_1\le2/n\), and commutation with \(\lambda(v)\), give

\[
 \sup_{g\in K}\|\lambda(g)a_n-a_n\|_1
 \le2/n+\varepsilon/2.
 \tag{PF.52}
\]

Choose \(n\) large. This is a directed compact-set/accuracy construction, not a countable exhaustion of \(G\).

Put \(\xi_n=\sqrt{a_n}\), so \(\|\xi_n\|_2=1\). The elementary inequality
\(|\sqrt{s}-\sqrt{t}|^2\le|s-t|\) gives uniform almost invariance on \(K\) in \(L^2\). For a character \(p\), put \(\xi_{p,n}(t)=\overline{p(t)}\xi_n(t)\). Then

\[
 \|\lambda(g)\xi_{p,n}-p(g)\xi_{p,n}\|_2
 =\|\lambda(g)\xi_n-\xi_n\|_2.
 \tag{PF.53}
\]

For \(f\in L^1(G)\), choose a compact set capturing its \(L^1\) mass up to any prescribed error and use (PF.53) on that set. The remaining integral is bounded by twice the \(L^1\) tail. Consequently

\[
 |(\mathcal F f)(p)|\le\|\lambda(f)\|.
 \tag{PF.54}
\]

The Gelfand norm is the supremum over \(p\), while \(\|\lambda(f)\|\le\|f\|_u\). Hence \(\|\lambda(f)\|=\|f\|_u\). We may therefore regard \(\lambda:C_0(Y)\to M\) as a faithful nondegenerate representation. Nondegeneracy follows already from the regular compact approximate identity. This proof does not use Pontryagin duality.

There is no nonzero kernel on \(L^1\) itself: if \(\lambda(f)=0\), apply it to compact approximate-identity vectors \(e_i\in L^1\cap L^2\). Then \(f*e_i=0\), while \(f*e_i\to f\) in \(L^1\), so \(f=0\). Thus (PF.48) is a norm before completion.

## The measure induced by the Plancherel weight

Set \(\mathcal B=\mathcal F(L^1(G)\cap L^2(G))\). It is a self-adjoint algebra: Young's inequality puts convolutions in \(L^1\cap L^2\), and inversion preserves \(L^2\) because \(G\) is unimodular. It is uniformly dense in \(C_0(Y)\), since \(L^1\cap L^2\) is \(L^1\)-dense and (PF.50) is the C*-completion. PF-05 gives

\[
 \psi_G(\lambda(|\mathcal F f|^2))=\|f\|_2^2,
 \qquad f\in L^1(G)\cap L^2(G).
 \tag{PF.55}
\]

Here \(f\) is genuinely left bounded, because convolution by \(f\) has operator norm at most \(\|f\|_1\).

For compact \(K\subset Y\), choose \(h\in C_c(Y)_+\), equal to one on \(K\). Uniformly approximate \(\sqrt h\) by \(b\in\mathcal B\) so closely that \(|b|^2\ge1/4\) on \(K\). Formula (PF.55) makes \(\lambda(|b|^2)\) finite for the weight. For \(u\in C_c(Y)_+\) supported in \(K\),

\[
 0\le u\le4\|u\|_\infty |b|^2,\qquad
 \psi_G(\lambda(u))<\infty.
 \tag{PF.56}
\]

Thus the weight is finite on every positive compact continuous function; no norm-density-to-\(L^2\)-density inference has been made. Its linear extension on finite elements defines a positive complex-linear functional on \(C_c(Y)\). Apply the programme Haar-measure lesson's Theorem 2.2 directly to that functional. Equivalently, its restriction to real functions is positive and real-linear, and the representing integral extends to complex functions by real and imaginary parts. The theorem requires no sigma-compactness. There is a unique Radon measure \(dp\) with

\[
 \psi_G(\lambda(u))=\int_Y u(p)\,dp,\qquad u\in C_c(Y).
 \tag{PF.57}
\]

Here Radon has the convention just stated: finite on compact sets, outer regular on Borel sets, and inner regular on open sets. For a nonempty open set \(V\), choose a nonzero \(v\in C_c(Y)_+\) supported in \(V\). Faithfulness of both \(\lambda\) and \(\psi_G\) gives \(\int v\,dp>0\), hence \(dp(V)>0\). This also proves full support.

For all \(u\in C_0(Y)_+\), (PF.57) still holds, allowing infinity. Direct the compact cutoffs \(0\le\chi\le1\) by pointwise order, closed under finite maxima. Nondegeneracy makes \(\lambda(\chi)\) increase strongly to \(1\). Normality gives
\(\psi_G(\lambda(u))=\sup_\chi\psi_G(\lambda(u\chi))\).
Radon integration of a nonnegative continuous function is the same supremum. This extends (PF.57) and fixes the measure uniquely by the original normalization of \(dg\). It is the Plancherel measure of Definition 3.15.

## An onto Plancherel transform

Equations (PF.55)–(PF.57) give

\[
 \int_G|f(g)|^2\,dg=\int_Y|(\mathcal F f)(p)|^2\,dp.
 \tag{PF.58}
\]

Since \(L^1\cap L^2\) is Hilbert dense, \(\mathcal F\) extends to an isometry
\(U:L^2(G)\to L^2(Y,dp)\). Its closed range \(R\) is the \(L^2\)-closure of \(\mathcal B\).

For \(b\in\mathcal B\), multiplication by \(b\) and by \(\overline b\) preserve \(\mathcal B\), hence \(R\). Uniform density then makes \(R\) a reducing module for all \(C_0(Y)\). If \(u\in C_c(Y)\) with compact support \(K\), choose finitely many \(b_j\in\mathcal B\) nonzero on neighborhoods covering \(K\). Their sum \(q=\sum_j|b_j|^2\) belongs to \(\mathcal B\subset R\) and is strictly positive near \(K\). Define \(v=u/q\) near \(K\), extended by zero; this is a compactly supported continuous function. Therefore \(u=vq\in R\). Since \(C_c(Y)\) is dense in \(L^2(Y,dp)\) by the arbitrary-Radon bridge, \(R=L^2(Y,dp)\). This proves surjectivity, not merely isometry.

Convolution intertwines on its actual dense domain:

\[
 U\lambda(f)U^*=m(\mathcal F f),\qquad f\in L^1(G).
 \tag{PF.59}
\]

Indeed apply it to \(L^1\cap L^2\), using \(\mathcal F(f*k)=(\mathcal Ff)(\mathcal Fk)\), then extend by boundedness. Thus \(U\lambda(C^*(G))U^*=m(C_0(Y))\).

## Dual topology and Haar invariance

The spectrum topology equals weak-* convergence of characters on \(L^1(G)\). Restriction gives one direction; uniformly bounded character functionals and the C*-density of \(L^1\) give the other. For each \(p\), the multiplier \(D_p=m(p(\cdot))\) on \(L^2(G)\) is unitary. Every \(L^1\) function factors as \(\xi\overline\eta\), with \(\xi,\eta\in L^2\), so weak-* convergence of characters is equivalent to weak operator convergence of \(D_p\). On unitary limits, weak and strong operator convergence agree. Products and inverses are consequently continuous. Thus the already locally compact spectrum \(Y\) is a locally compact abelian group.

This topology is exactly uniform convergence on compact subsets of \(G\). Compact-uniform convergence implies convergence on \(L^1\) by compact approximation and \(|p|\le1\). Conversely suppose \(p_i\to p\) weak-*. Choose \(f\in L^1\) with \((\mathcal Ff)(p)\ne0\). For compact \(K\subset G\), the translations \(\{\lambda(g)f:g\in K\}\) form a norm-compact subset of \(L^1\). Norm-one functionals converging pointwise converge uniformly on each norm-compact set by a finite-net argument. Since

\[
 \mathcal F(\lambda(g)f)(p_i)=p_i(g)(\mathcal Ff)(p_i),
 \tag{PF.60}
\]

and the scalar factor tends to a nonzero value, \(p_i(g)\to p(g)\) uniformly on \(K\). The same statement holds for the conjugated coupling. This proves the neighborhood assertion in source (34) with its exact compact sets and positive tolerances. Joint evaluation \((g,p)\mapsto p(g)\) is continuous: use compact-uniform control on a relatively compact neighborhood of \(g\), together with continuity of the limiting character.

Explicitly, for compact \(K\subset G\) and \(\varepsilon>0\), the neighborhoods are

\[
 U(p,K,\varepsilon)=
 \{q\in Y:|\langle g,p\rangle-\langle g,q\rangle|<\varepsilon
                  \text{ for every }g\in K\}.
 \tag{PF.60a}
\]

For fixed \(p\in Y\), multiplication by \(p(\cdot)\) preserves \(L^1\cap L^2\), is unitary on \(H\), and satisfies

\[
 \mathcal F(pf)(q)=(\mathcal Ff)(q+p).
 \tag{PF.61}
\]

The corresponding shift is therefore unitary on the dense range \(\mathcal B\), hence on \(L^2(Y,dp)\). To identify it with the pointwise shift on every \(C_c(Y)\), approximate a compact continuous \(u\) by \(b_n\in\mathcal B\) in both uniform and \(L^2\) norms. Such approximants exist: write \(u=vq\) as in PF-19, approximate \(v\in C_c\) uniformly by \(a_n\in\mathcal B\), and put \(b_n=a_nq\); the \(L^2\) error is at most \(\|a_n-v\|_\infty\|q\|_2\). Uniform convergence survives the shift, and a summable-error \(L^2\) subsequence identifies its Hilbert limit. Hence
\(\int|u(q+p)|^2\,dq=\int|u(q)|^2\,dq\).
Apply this to the continuous square root of each \(C_c\) nonnegative function; uniqueness of Radon measures makes \(dp\) translation invariant. It is a nonzero Haar measure on \(Y\), as asserted in Theorem 3.16(ii). This step uses no biduality.

The source's \(\mu(p)\) in (35) is \(m(p(\cdot))=D_p=m(\overline{\langle\cdot,p\rangle})\). Thus its transformed shift is \(q\mapsto q+p\), exactly as printed. The conjugate multiplier \(D_{-p}\) instead gives \(q\mapsto q-p\). These two conventions must not be confused; there is no source error in (35) or its shift calculation.

## The full multiplication algebra and local measure convention

For arbitrary non-sigma-compact Haar spaces, \(L^\infty\) here has the usual local Haar completion: bounded measurable functions modulo local null sets, represented on \(L^2\). This retains the Radon integrals of compact continuous functions and the \(L^p\) spaces for finite \(p\); it permits bounded measurable representatives to be patched over open sigma-compact cosets.

Here is the relevant multiplication proof. Choose a relatively compact symmetric identity neighborhood in \(Y\). Its finite powers generate an open sigma-compact subgroup \(Y_0\); the disjoint open cosets \(Y_j\) have sigma-finite Haar measure. Compact sets meet only finitely many cosets, so \(C_c\)-density identifies

\[
 L^2(Y)=\bigoplus_j L^2(Y_j),\qquad
 L^\infty(Y)=\prod_j L^\infty(Y_j)
 \quad\hbox{with a uniform essential bound}.
 \tag{PF.62}
\]

This states the local completion explicitly and imposes no countability on the coset index.

Precisely, a set is locally Borel when its intersection with each finite-measure Borel set is Borel, and locally null when every such intersection has measure zero. In completed spaces replace Borel by completed measurability. A function is locally measurable when all inverse images of Borel scalar sets are locally measurable. Each coset has a countable finite-measure exhaustion. Every finite-measure Borel set is contained in countably many cosets by Proposition 2.22. Consequently these local conditions are equivalent to componentwise measurability and componentwise nullity. A uniformly bounded component family patches to a locally measurable function, giving the product in (PF.62). Conversely local measurability and the component exhaustions give the component representatives and their uniform essential bound.

Finite-p functions have at most countably many nonzero components: for each positive threshold only finitely many components can contribute more than that threshold to their finite norm. Their completed component representatives patch on a countable union of cosets and can be chosen zero elsewhere. This gives the same finite-p spaces as the ordinary completed Haar construction. It does not assert that the raw Haar measure of every Borel set is the sum of its coset measures; The transversal \(\{0\}\times\mathbb R_d\) in \(\mathbb R\times\mathbb R_d\) shows that this assertion can fail for sets meeting uncountably many cosets.

On a sigma-finite coset, bounded continuous functions are strongly dense among multiplication operators: approximate each finite-measure indicator in \(L^2\) by compact continuous functions between zero and one; an almost-everywhere subsequence and dominated convergence give strong convergence of their multipliers. Then use simple functions and increasing finite-measure cutoffs. If an operator \(T\) commutes with these multipliers, choose a disjoint countable finite-measure partition \(E_n\) of the coset. On \(E_n\), set \(b_n=T1_{E_n}\). Commutation with indicators gives \(T1_F=1_F b_n\) for every measurable \(F\subset E_n\). The norm estimate on \(1_F\) implies \(|b_n|\le\|T\|\) almost everywhere. Finite-measure simple-function density proves that \(T\) is multiplication by the patched bounded function. Thus the multiplication algebra is maximal abelian on each coset.

The coset projections themselves are strong limits of compact continuous multipliers supported in the coset. Finite sums of these projections increase strongly to \(1\) in the Hilbert direct sum. Applying the preceding component proof and the local patching in (PF.62) shows that the von Neumann algebra generated by \(C_0(Y)\) is exactly the multiplication algebra \(L^\infty(Y)\). From (PF.59) and PF-01,

\[
 UMU^*=L^\infty(Y),\qquad
 U\lambda(g)U^*=m(p\mapsto p(g)).
 \tag{PF.63}
\]

The last equality follows either from translating the integral on \(L^1\cap L^2\), or from the regular approximate identity. This proves all of Theorem 3.14(ii).

## The inverse Fourier integral

For \(\varphi\in L^1(Y,dp)\cap L^2(Y,dp)\), define

\[
 v(g)=\int_Y\overline{p(g)}\varphi(p)\,dp.
 \tag{PF.64}
\]

It is absolutely convergent, bounded by \(\|\varphi\|_1\), and continuous: first use joint evaluation and a compactly supported approximation to \(\varphi\) in \(L^1\), then use the uniform bound for the tail.

For \(f\in C_c(G)\), absolute integrability of \(|f(g)\varphi(p)|\) gives

\[
 \langle Uf,\varphi\rangle
 =\int_G f(g)\overline{v(g)}\,dg.
 \tag{PF.65}
\]

This Fubini step is justified on sigma-finite supports: \(L^1\) compact approximation supplies a countable union of compact supports up to the local null convention, on which the Radon product is the ordinary completed sigma-finite product. Alternatively approximate both factors by compact continuous functions and use the product \(L^1\) bound. No unrestricted non-sigma-finite Fubini assertion is needed.

The right side is bounded by \(\|\varphi\|_2\|f\|_2\). Choose \(f=\chi v\), with \(0\le\chi\le1\) compact continuous. Since \(v\) is continuous, this is an allowed test. Then

\[
 \int_G\chi|v|^2\le
 \|\varphi\|_2\left(\int_G\chi^2|v|^2\right)^{1/2}
 \le\|\varphi\|_2\left(\int_G\chi|v|^2\right)^{1/2}.
 \tag{PF.66}
\]

Thus all such integrals are at most \(\|\varphi\|_2^2\). Radon integration of the continuous \(|v|^2\) is their supremum, so \(v\in L^2(G)\). The density of \(C_c(G)\) and (PF.65) now give \(U^*\varphi=v\) globally in \(L^2\). This proves the inverse formula in Theorem 3.14(iii) without assembling uncountably many local null statements.

## The shear and topological Pontryagin biduality

Let \(W_G F(s,t)=F(s,st)\) as in PF-06. The tensor Fourier transform is unitary by the Haar Radon tensor bridge. On elementary compact continuous functions, change variables \(u=st\) to obtain

\[
 T=(U\otimes U)W_G(U\otimes U)^*,\qquad
 (T\Phi)(p,q)=\Phi(p-q,q).
 \tag{PF.67}
\]

The scalar kernel calculation gives
\(p(s)q(s^{-1}u)=(p-q)(s)q(u)\).
Elementary tensors are dense in the joint \(L^1\)-and-\(L^2\) norm on compact supports, so their Fourier kernels agree with the tensor transform on this dense calculation domain. Both operators in (PF.67) are unitary: for the right side use Haar invariance on \(Y\). Hence the equality extends to all \(L^2(Y\times Y)\).

The source's (37), printed p. 77, has \(p+q\) in this formula; with the fixed conventions (12), (29), (30) the correct sign is \(p-q\). In contrast, conjugation of a first-factor multiplier is

\[
 T^*(m(r)\otimes1)T=m((p,q)\mapsto r(p+q)).
 \tag{PF.68}
\]

These are different operations; the plus sign in (PF.68) is correct.

If \(r:Y\to\mathbb T\) is any continuous character, put \(x=U^*m(r)U\in M\). Equation (PF.68) and \(r(p+q)=r(p)r(q)\) make \(x\) nonzero and group-like for \(W_G\). PF-14 reconstructs \(x=\lambda(g)\) for a unique \(g\in G\). Equation (PF.63) gives \(r(p)=p(g)\) almost everywhere. Both sides are continuous and Haar has full support, so they agree everywhere. Equivalently \(r(p)=\langle g^{-1},p\rangle\). Therefore the source's canonical map

\[
 j:G\longrightarrow\widehat Y,\qquad j(g)(p)=\langle g,p\rangle=\overline{p(g)}
 \tag{PF.69}
\]

is surjective. It is injective: \(j(g)=1\) implies \(U\lambda(g)U^*=1\), hence \(\lambda(g)=1\), and PF-08 separates group points.

It is a homeomorphism, not just a bijection. Apply PF-20 to the locally compact abelian group \(Y\); its character topology is weak-* on \(L^1(Y)\) and compact-uniform. If \(g_i\to g\), strong continuity of \(\lambda\) and (PF.63) give weak operator convergence of the corresponding character multipliers, hence weak-* convergence of \(j(g_i)\). Conversely that weak-* convergence gives weak operator convergence of \(\lambda(g_i^{-1})\) to \(\lambda(g^{-1})\), and the inverse continuity proved in PF-15 gives \(g_i\to g\). This proves Theorem 3.16(iii) including its topology. Definition 3.17 names \(Y=\widehat G\) the dual group.

Finally (PF.63) identifies \(M_*\) with \(L^1(Y)\): on each sigma-finite coset the normal vector-series density is an integrable scalar function, and the Hilbert direct sum yields the summable component family. For \(u,v\in L^1(Y)\), (PF.68) gives

\[
 \Gamma_*(u\otimes v)=u*v,\qquad
 (u*v)(p)=\int_Yu(p-q)v(q)\,dq.
 \tag{PF.70}
\]

Absolute product integration and the same sigma-finite support argument justify this formula. Thus the Fourier algebra \(A(G)\) becomes the convolution Banach algebra \(L^1(\widehat G)\), with its actual predual norm and product, as in the final source argument.

## Haar normalization and a finite example

Rescaling \(dg\) by \(c>0\) rescales the transform by \(c\). Equation (PF.58) therefore rescales the Plancherel measure by \(c^{-1}\), fixing its Haar constant. For a finite abelian group of order \(N\), with \(dg=c\) times counting measure,

\[
 (\mathcal F f)(p)=c\sum_g p(g)f(g),\qquad
 dp=\frac1{cN}\text{ times counting measure on }\widehat G.
 \tag{PF.71}
\]

Character orthogonality proves (PF.58) and (PF.64) directly. The finite cyclic check uses \(N=5\) and \(c=2.3\), so both the shear sign and the reciprocal Haar normalization are observable.

## Abelian norm equality and Fourier normalization on the real line

The next results return to an arbitrary locally compact Hausdorff group \(G\) with fixed left Haar \(dg\), except for the initial abelian and real-line specialization. Inner products remain linear in the first variable. On \(A=L^1(G)\),

\[
 (a*b)(t)=\int_G a(s)b(s^{-1}t)\,ds,\qquad
 a^*(t)=\delta(t)^{-1}\overline{a(t^{-1})}.
 \tag{PF.72}
\]

The arbitrary-cardinality Haar, local \(L^\infty=L^1{}^*\), translation and Radon-product conventions are those of PF-01, PF-21 and OA-MOD-PF-DEP-GROUP. Hilbert completion and the exact arbitrary-Hilbert Riesz import are OA-MOD-DEP-HILBERT and OA-MOD-OPEN-HILBERT-RIESZ. The proof supplies its own bounded nonunital GNS and kernel constructions; independent review of the transitive Hilbert/Haar/scalar providers remains open. No separability, sigma-compactness, unimodularity or finite-total-measure hypothesis is introduced.

The six source statements are Takesaki II VII.3 Remark 3.18 through Proposition 3.23, printed pp. 78–81. They cover full/reduced equality and real-line normalization, the two-way representation correspondence, the positive-convolution definition and coefficient theorem, continuous representatives and the finite-matrix characterization. The source's Proposition 3.19 proof treats *-representations as nondegenerate; that convention is retained.

For abelian \(G\), PF-17 already proves

\[
 \|a\|_{C^*(G)}=\|\lambda(a)\|,\qquad C^*(G)=C_r^*(G).
 \tag{PF.73}
\]

Equivalently, PF-19–21 represent \(\lambda(a)\) by multiplication by its Fourier transform on a dual Haar measure of full support, whose essential supremum for a continuous function is its supremum. This supplies the first assertion of Remark 3.18.

For \(G=\mathbb R\) with \(dg=ds\), put \(p_t(s)=e^{-2\pi ist}\). HA-LCA-02, Theorem 3.1 proves that \(u\mapsto[s\mapsto e^{2\pi ius}]\) is a topological group isomorphism \(\mathbb R\to\widehat{\mathbb R}\). Composing it with the real-line reflection \(t\mapsto-t\) gives exactly \(t\mapsto p_t\): these are all continuous characters, and their compact-uniform topology is the usual topology of \(t\). Thus the coupling is \(e^{2\pi ist}\), the Fourier kernel is \(e^{-2\pi ist}\), and dual Haar measure is \(c\,dt\) for a positive constant \(c\).

We determine \(c\) by one direct integral, without invoking Euclidean Plancherel. Set \(h(s)=e^{-\pi s^2}\) and \(J(t)=\int h(s)e^{-2\pi ist}\,ds\). Differentiation under an integrable majorant and integration by parts give

\[
 J'(t)=-2\pi tJ(t),\qquad J(0)=1,\qquad J(t)=e^{-\pi t^2}.
 \tag{PF.74}
\]

For the middle equality, the positive square of the Gaussian integral is the integral of \(e^{-\pi(x^2+y^2)}\) on \(\mathbb R^2\); polar coordinates give \(2\pi\int_0^\infty re^{-\pi r^2}\,dr=1\). Boundary terms in integration by parts vanish by Gaussian decay. Apply the already proved group Parseval identity to \(h\). The two unscaled squared integrals are the same nonzero finite number, so \(c=1\). Therefore

\[
 \int_{\mathbb R}|f(s)|^2\,ds
 =\int_{\mathbb R}\left|\int_{\mathbb R}e^{-2\pi ist}f(s)\,ds\right|^2dt,
 \qquad f\in L^1(\mathbb R)\cap L^2(\mathbb R).
 \tag{PF.75}
\]

This checks the entire normalization clause of Remark 3.18.

## Integrated representations of the group algebra

A *-representation here is nondegenerate, as the source's proof specifies. Degenerate representations have an essential subspace and a zero summand; no unitary representation integrates to that zero summand.

Every *-homomorphism \(\pi:A\to B(K)\) is \(L^1\)-contractive. Extend it to the unitizations. Invertibility is preserved, so spectral inclusion and the C*-identity give

\[
 \|\pi(a)\|^2=r(\pi(a^**a))
 \le r_A(a^**a)\le\|a^**a\|_1\le\|a\|_1^2.
 \tag{PF.76}
\]

No prior boundedness of \(\pi\) is needed for this algebraic spectral-inclusion argument.

Let \(e_i\) be a compact continuous approximate identity with \(e_i\ge0\), \(\|e_i\|_1=1\), and supports shrinking to the identity. Then \(\pi(e_i)\to1\) strongly, first on \(\pi(A)K\) and then by the common bound. For fixed \(g\), the contractions \(\pi(\lambda(g)e_i)\) converge strongly on this dense span, because

\[
 (\lambda(g)e_i)*a=\lambda(g)(e_i*a)\longrightarrow\lambda(g)a
 \quad\text{in }L^1.
 \tag{PF.77}
\]

Their limit satisfies \(U(g)\pi(a)\eta=\pi(\lambda(g)a)\eta\). Thus it is defined on all \(K\). On the dense span, translation composition gives \(U(g)U(h)=U(gh)\) and \(U(g^{-1})U(g)=1\). Each map and its inverse are contractions, hence are unitaries. \(L^1\) translation continuity gives strong continuity on the same dense span and then on all \(K\).

For \(f,a\in A\), the \(L^1\)-valued convolution integral gives

\[
 \left(\int_Gf(g)U(g)\,dg\right)\pi(a)\eta
 =\pi(f*a)\eta=\pi(f)\pi(a)\eta.
 \tag{PF.78}
\]

Boundedness and density prove \(\pi(f)=\int f(g)U(g)\,dg\). Uniqueness follows from the dense-span formula for \(U\).

Conversely, for a strongly continuous unitary representation \(U\), define that integral on each vector. It has norm at most \(\|f\|_1\). The group law and absolute product integration prove multiplicativity. Haar inversion gives

\[
 \pi(f)^*=\int_G\overline{f(g)}U(g^{-1})\,dg
 =\int_G\delta(h)^{-1}\overline{f(h^{-1})}U(h)\,dh
 =\pi(f^*).
 \tag{PF.79}
\]

Shrinking compact approximate identities give \(\pi(e_i)\to1\) strongly, so this representation is nondegenerate. Equation (PF.77) recovers \(U\), proving both directions of Proposition 3.19.

These vector integrals do not require a separable \(K\). Compact approximation of \(f\) restricts it to a countable union of compact supports up to its \(L^1\) class. The continuous vector orbit on each compact has compact, hence separable, image in the Hilbert metric. The resulting vector integrand has an essentially separable range and integrable norm. Likewise product/convolution calculations localize to sigma-finite supports as in the preceding Haar bridge.

## A bounded GNS construction for positive convolution functionals

For \(\omega\in L^\infty(G)\) in the completed local convention, set \(F_\omega(a)=\int a(g)\omega(g)\,dg\). It is bounded, with norm \(\|\omega\|_\infty\). Definition 3.20 says

\[
 F_\omega(f^**f)
 =\int_G\int_G\overline{f(g)}f(h)\omega(g^{-1}h)\,dg\,dh\ge0
 \quad(f\in A).
 \tag{PF.80}
\]

The product integrand is absolutely integrable, bounded in integral by \(\|\omega\|_\infty\|f\|_1^2\). The formula follows from convolution, Haar inversion and left translation; the modular factor in (PF.72) cancels with inversion. It holds first on compact continuous factors and then by \(L^1\) approximation. The local measurable convention is harmless on their sigma-finite supports.

We now prove the needed positive-functional theorem. Let \(F\) be any bounded linear functional on \(A\) with \(F(a^**a)\ge0\). Define

\[
 (a\mid b)_F=F(b^**a),\qquad
 N=\{a:F(a^**a)=0\}.
 \tag{PF.81}
\]

Polarization of the nonnegative quadratic polynomial makes this form Hermitian and gives Cauchy–Schwarz. Consequently \(N\) is a vector subspace, its vectors pair to zero with every vector, and \(A/N\) is a pre-Hilbert space.

Left multiplication has the exact norm bound needed for completion. Fix \(a\in A\) and \(\rho>\|a\|_1\). In the unitization, the real binomial series

\[
 d=(1-\rho^{-2}a^**a)^{1/2}
 =\sum_{n\ge0}{1/2\choose n}(-\rho^{-2}a^**a)^n
 \tag{PF.82}
\]

converges absolutely, is self-adjoint and squares to its argument. For \(b\in A\), \(d*b\) is in \(A\), so positivity gives

\[
 0\le F((d*b)^**(d*b))
 =F(b^**b)-\rho^{-2}F((a*b)^**(a*b)).
 \tag{PF.83}
\]

Let \(\rho\downarrow\|a\|_1\). Thus \(N\) is a left ideal and \(\pi(a)[b]=[a*b]\) has norm at most \(\|a\|_1\) on the Hilbert completion \(K_F\). Associativity and the form show that \(\pi\) is a *-representation. It is nondegenerate: \([e_i*b]\to[b]\), since \(\|[c]\|^2\le\|F\|\|c\|_1^2\).

The cyclic vector also requires proof in this nonunital algebra. As \(e_i^**b\to b\), Cauchy–Schwarz gives

\[
 |F(b)|=\lim_i|F(e_i^**b)|
 \le\sqrt{\|F\|}\,\|[b]\|.
 \tag{PF.84}
\]

Here \(F(e_i^**e_i)\le\|F\|\), because \(\|e_i\|_1=1\). Thus \([b]\mapsto F(b)\) is well-defined and bounded. Hilbert Riesz representation gives \(\xi\in K_F\) with \(F(b)=\langle[b],\xi\rangle\) and \(\|\xi\|^2\le\|F\|\). For every \(b\),

\[
 \langle\pi(a)\xi,[b]\rangle
 =\langle\xi,[a^**b]\rangle
 =\overline{F(a^**b)}=F(b^**a)
 =\langle[a],[b]\rangle.
 \tag{PF.85}
\]

Therefore \(\pi(a)\xi=[a]\), the vector is cyclic, and

\[
 F(a)=\langle\pi(a)\xi,\xi\rangle,\qquad
 \|\xi\|^2=\|F\|.
 \tag{PF.86}
\]

The reverse norm inequality follows from \(\|\pi(a)\|\le\|a\|_1\). If \(F=0\), the zero Hilbert construction, or the zero vector in a trivial one-dimensional representation, handles the same assertion. This proves the bounded GNS input without a weak-compactness or unitization-positive-extension shortcut.

## Positive classes as diagonal unitary coefficients

Apply PF-27 to \(F_\omega\), then PF-26 to its nondegenerate representation. For all \(a\in A\),

\[
 \int_Ga(g)\omega(g)\,dg
 =\langle\pi(a)\xi,\xi\rangle
 =\int_Ga(g)\langle U(g)\xi,\xi\rangle\,dg.
 \tag{PF.87}
\]

The exact \(L^1\)–local-\(L^\infty\) duality gives

\[
 \omega(g)=\langle U(g)\xi,\xi\rangle
 \quad\text{as an }L^\infty\text{ class},\qquad
 \|\xi\|^2=\|\omega\|_\infty.
 \tag{PF.88}
\]

Conversely, such a coefficient is bounded, and its integrated representation gives \(F_\omega(f^**f)=\|\pi(f)\xi\|^2\ge0\). This proves both parts of Proposition 3.21.

At arbitrary cardinality equality of local \(L^\infty\) classes means locally almost everywhere, as in PF-21. For sigma-compact groups this is ordinary completed Haar almost-everywhere equality. Do not infer global raw-Haar nullity for arbitrary representatives from \(L^1\)-test equality: on \(\mathbb R\times\mathbb R_d\), the closed transversal \(\{0\}\times\mathbb R_d\) is locally null but has infinite raw Haar measure. Equation (PF.88) uses precisely the already declared class convention; it does not assert that its two arbitrarily chosen representatives differ on a globally Haar-null set.

## The continuous positive-definite representative

Strong continuity of \(U\) makes \(g\mapsto\langle U(g)\xi,\xi\rangle\) continuous. The converse in PF-28 makes it positive definite. Thus every positive class has a continuous positive-definite representative, as Corollary 3.22 asserts.

It is unique among continuous representatives. If a continuous difference is nonzero at a point, it is bounded away from zero on a nonempty relatively compact open set. Haar full support gives that set positive finite measure; the difference cannot be locally null. In particular its value at the identity is intrinsic, and

\[
 \omega_c(e)=\|\xi\|^2=\|\omega\|_\infty,\qquad
 \omega_c(g^{-1})=\overline{\omega_c(g)}.
 \tag{PF.89}
\]

For a continuous positive input, its original values equal this representative at every point, not merely in the \(L^\infty\) class.

## Finite positive matrices and the exact kernel model

For a continuous function \(w:G\to\mathbb C\), Proposition 3.23's finite criterion is

\[
 K_{ij}=w(g_i^{-1}g_j),\qquad
 \sum_{i,j}\overline{c_i}c_jK_{ij}\ge0
 \quad\text{for all finite families }(g_i,c_i).
 \tag{PF.90}
\]

If \(w(g)=\langle U(g)\xi,\xi\rangle\), the quadratic form is

\[
 \sum_{i,j}\overline{c_i}c_jw(g_i^{-1}g_j)
 =\left\|\sum_jc_jU(g_j)\xi\right\|^2.
 \tag{PF.91}
\]

PF-28–PF-29 therefore prove the forward direction for every continuous positive-definite input.

Conversely suppose (PF.90). The \(1\times1\) and \(2\times2\) tests give \(w(e)\ge0\), \(w(g^{-1})=\overline{w(g)}\), and

\[
 |w(g)|\le w(e).
 \tag{PF.92}
\]

Thus a mere continuous function satisfying the criterion is automatically bounded; no hidden \(L^\infty\) hypothesis is added to this direction.

On the vector space of finite formal sums of symbols \(\varepsilon_g\), set

\[
 \left\langle\sum_jc_j\varepsilon_{g_j},
               \sum_id_i\varepsilon_{h_i}\right\rangle
 =\sum_{i,j}c_j\overline{d_i}\,w(h_i^{-1}g_j).
 \tag{PF.93}
\]

Condition (PF.90), polarization and Cauchy–Schwarz give a positive semidefinite form. Quotient the null space and complete. Left translation \(V(s)\varepsilon_g=\varepsilon_{sg}\) preserves the form because \((sh)^{-1}(sg)=h^{-1}g\); its inverse is \(V(s^{-1})\), so it is unitary.

The representation is strongly continuous, not merely an abstract representation of the underlying group. For each symbol,

\[
 \|V(s)\varepsilon_g-\varepsilon_g\|^2
 =2w(e)-2\operatorname{Re}w(g^{-1}sg)\longrightarrow0
 \quad(s\to e).
 \tag{PF.94}
\]

Finite sums and then density and the common unitary bound extend this continuity to every vector. Put \(\xi=\varepsilon_e\). Then \(w(s)=\langle V(s)\xi,\xi\rangle\); PF-26 and PF-28 give positive convolution integrals for every \(L^1\) function. This proves the full reverse direction with no incomplete Riemann-sum premise. If \(w(e)=0\), (PF.92) gives \(w=0\) and the null construction covers it.

The two constructions have their expected universal identification: any cyclic unitary realization of the same continuous \(w\) sends \(\varepsilon_g\) to \(U(g)\xi\). Equation (PF.93) proves it is isometric on the finite span; cyclicity gives dense range, hence a unitary intertwiner. Conversely a cyclic PF-27 construction is cyclic for \(U\): the closure of the span of \(U(g)\xi\) contains every integrated vector \(\pi(a)\xi\). This identification explains what the positive kernel is measuring.

## Full group coefficients and their exact dual norm

The final three numbered results in VII.3 concern the full group dual and its state space. The group is again an arbitrary locally compact Hausdorff \(G\) with fixed left Haar measure; inner products are linear in the first variable. Write \(B(G)=C^*(G)^*\), identified below with continuous coefficients, and retain \(A(G)=(M_l)_*\) from PF-08–09. The coefficient-norm proof uses the universal-bidual restriction isometry, the concrete vector-series predual, and the integrated group-representation correspondence. The state proof also uses unit-vector GNS. The exact source is Takesaki II VII.3 Proposition 3.24, Definition 3.25 and Proposition 3.26, printed pp. 82–86 / supplied PDF pp. 102–106. No separability, countability or unimodularity is added.

We first make the identification \(B(G)\subset C_b(G)\) and its norm quantitative. Let \(\Lambda\in C^*(G)^*\). Under UB-04 it is the restriction of a unique normal functional \(\widetilde\Lambda\in M_*\), \(M=\pi_u(C^*(G))''\), with \(\|\widetilde\Lambda\|=\|\Lambda\|\). CP-06 identifies \(M_*\) with a quotient of the Hilbert projective tensor completion. Its quotient norm and the summable-series construction in CP-04 imply that for every \(\varepsilon>0\) there are vectors \(x_n,y_n\in H_u\) such that

\[
 \widetilde\Lambda(T)=\sum_{n\ge1}\langle T x_n,y_n\rangle
 \quad(T\in M),\qquad
 \sum_{n\ge1}\|x_n\|\|y_n\|<\|\Lambda\|+\varepsilon .
 \tag{PF.95}
\]

Indeed choose a quotient representative within \(\varepsilon/2\) of its infimum and then a series representation within \(\varepsilon/2\) of that representative's projective norm. The series is absolutely and uniformly convergent on the operator unit ball. Zero pairs can be omitted. For each remaining pair multiply \(x_n\) by \(\sqrt{\|y_n\|/\|x_n\|}\) and \(y_n\) by the reciprocal positive scalar. This leaves its coefficient unchanged and makes both squared norms \(\|x_n\|\|y_n\|\). Collect the balanced vectors as \(X=(x_n)\), \(Y=(y_n)\) in \(H_u\otimes\ell^2\). Then

\[
 \widetilde\Lambda(T)=\langle(T\otimes1)X,Y\rangle,\qquad
 \|X\|\|Y\|=\sum_n\|x_n\|\|y_n\|<\|\Lambda\|+\varepsilon .
 \tag{PF.96}
\]

If \(\Lambda=0\), use zero vectors.

Let \(U_u\) be the strongly continuous unitary representation integrating \(\pi_u|_{L^1(G)}\), from PF-26. Set

\[
 b_\Lambda(g)=\langle(U_u(g)\otimes1)X,Y\rangle .
 \tag{PF.97}
\]

For every \(f\in L^1(G)\), the vector-integral identity and (PF.96) give

\[
 \Lambda(f)=\int_G f(g)b_\Lambda(g)\,dg .
 \tag{PF.98}
\]

The continuous function \(b_\Lambda\) is independent of the choice of near-minimal vectors: two such functions agreeing against all \(L^1\) tests agree at every point. To justify that last step, their continuous difference, if nonzero at a point, stays bounded away from zero on a relatively compact open neighborhood with positive finite Haar measure; a suitable compact continuous test has nonzero integral. Thus \(\Lambda\mapsto b_\Lambda\) is an injective linear map into \(C_b(G)\). Equation (PF.96) gives \(\|b_\Lambda\|_\infty\le\|\Lambda\|\) after \(\varepsilon\downarrow0\).

Conversely, if \(U:G\to\mathcal U(K)\) is strongly continuous and \(b(g)=\langle U(g)x,y\rangle\), integration gives a bounded functional on \(L^1(G)\) whose absolute value on \(f\) is at most \(\|U(f)\|\|x\|\|y\|\). By the definition of the full group norm, \(\|U(f)\|\le\|f\|_{C^*(G)}\); hence the functional extends uniquely to \(C^*(G)\) with norm at most \(\|x\|\|y\|\). The two directions prove

\[
 \|b\|_{B(G)}
 =\inf\{\|x\|\|y\|:\ b(g)=\langle U(g)x,y\rangle
       \text{ for a strongly continuous unitary }U\}.
 \tag{PF.99}
\]

The infimum need not be asserted to be attained. In particular the \(B\)-norm is the dual \(C^*\)-norm, not the supremum norm on \(C_b(G)\).

## The Fourier–Stieltjes Banach algebra

Let \(b,c\in B(G)\). Choose coefficient representations \(b(g)=\langle U(g)x,y\rangle\) and \(c(g)=\langle V(g)z,w\rangle\) with costs arbitrarily close to their respective \(B\)-norms. The representation \(g\mapsto U(g)\otimes V(g)\) is strongly continuous: verify continuity first on finite elementary tensors, use unitarity for a uniform bound, and pass to the Hilbert tensor completion. Its elementary coefficient is

\[
 b(g)c(g)=\langle(U(g)\otimes V(g))(x\otimes z),y\otimes w\rangle .
 \tag{PF.100}
\]

Equation (PF.99), followed by the two infima, yields

\[
 \|bc\|_{B(G)}\le\|b\|_{B(G)}\|c\|_{B(G)}.
 \tag{PF.101}
\]

The same reasoning includes zero coefficients. Pointwise addition and scalar multiplication come from the Banach dual. Since \(C^*(G)^*\) is complete, this makes \(B(G)\) a commutative Banach algebra. The trivial one-dimensional representation gives the constant unit \(1\), with \(\|1\|_B=1\).

For conjugation, let \(\overline K\) be the conjugate Hilbert space and let \(J:K\to\overline K\) denote its canonical conjugate-linear isometry. The group action \(\overline U(g)Jx=JU(g)x\) is a strongly continuous unitary representation, and by the conjugate inner-product definition

\[
 \overline{b(g)}
 =\langle\overline U(g)Jx,Jy\rangle_{\overline K}.
 \tag{PF.102}
\]

Thus \(\overline b\in B(G)\) and \(\|\overline b\|_B\le\|b\|_B\). Apply this twice for equality. This proves the full self-adjoint Banach-algebra clause of Proposition 3.24(i), including its inherited pointwise product and the specific dual norm.

## Regular absorption and the Fourier-algebra ideal

Let \(a\in A(G)\), identified with \(\rho\in(M_l)_*\) by PF-08–09. CP-04–06, now for the concrete algebra \(M_l\subset B(L^2(G))\), give for each \(\varepsilon>0\) a balanced vector series

\[
 a(g)=\sum_n\langle\lambda(g)\xi_n,\eta_n\rangle
      =\langle(\lambda(g)\otimes1)P,Q\rangle ,
 \quad P,Q\in L^2(G)\otimes\ell^2,\quad
 \|P\|\|Q\|<\|a\|_A+\varepsilon .
 \tag{PF.103}
\]

The sum is uniformly absolutely convergent in \(g\), by Cauchy–Schwarz. Let \(b(g)=\langle U(g)x,y\rangle\) be a coefficient representation of \(b\in B(G)\) with \(\|x\|\|y\|<\|b\|_B+\varepsilon\). Their product is a coefficient of \(\lambda\otimes1_{\ell^2}\otimes U\) on \(L^2(G;\ell^2\otimes K)\).

Define on compact continuous simple vectors and extend by isometry

\[
 (TF)(t)=(1_{\ell^2}\otimes U(t))F(t).
 \tag{PF.104}
\]

Its inverse is obtained with \(U(t)^*\). Continuity of \(U(t)\) on each fixed vector, compact support, and the dense simple-vector construction make this a well-defined unitary without assuming that \(K\) is separable. A direct calculation on the dense simple vectors gives

\[
 T(\lambda(g)\otimes1)T^*
      =\lambda(g)\otimes1_{\ell^2}\otimes U(g).
 \tag{PF.105}
\]

Indeed, at \(t\), the left side applies \(U(t)U(g^{-1}t)^*=U(g)\) to \(F(g^{-1}t)\). No modular factor enters because these are left translations with left Haar measure.

Put \(P'=T^*(P\otimes x)\) and \(Q'=T^*(Q\otimes y)\). By (PF.105),

\[
 a(g)b(g)=\langle(\lambda(g)\otimes1)P',Q'\rangle .
 \tag{PF.106}
\]

For clarity, why is the last coefficient in \(A(G)\) at arbitrary Hilbert cardinality? Choose any orthonormal basis of \(\ell^2\otimes K\). The two vectors \(P',Q'\) have coordinate families \((p_j),(q_j)\) in \(L^2(G)\) with at most countably many nonzero coordinates, and

\[
 \Theta(S)=\sum_j\langle Sp_j,q_j\rangle,\qquad S\in M_l,
 \tag{PF.107}
\]

converges absolutely, since \(\sum_j\|p_j\|\|q_j\|
\le\|P'\|\|Q'\|\). Each finite partial sum is normal, and the tail tends to zero in functional norm; CP-06 makes the predual norm closed. Hence \(\Theta\in(M_l)_*\), its group coefficient is \(ab\), and

\[
 \|ab\|_A\le\|\Theta\|\le\|P'\|\|Q'\|
 =\|P\|\|Q\|\|x\|\|y\| .
 \tag{PF.108}
\]

Let \(\varepsilon\downarrow0\), to obtain

\[
 A(G)B(G)\subset A(G),\qquad
 \|ab\|_{A(G)}\le\|a\|_{A(G)}\|b\|_{B(G)}.
 \tag{PF.109}
\]

This proves Proposition 3.24(ii), with the module norm estimate that the source's ideal statement leaves implicit. Definition 3.25 calls \(B(G)\), with the just-proved structure, the **Fourier–Stieltjes algebra** of \(G\).

For a noncompact \(G\), the ideal can be proper: \(1\in B(G)\), while \(A(G)\subset C_0(G)\) by PF-08, and \(1\notin C_0(G)\). This example distinguishes the two algebras without confusing their norms.

## Two modulus bounds for state coefficients

Let \(\varphi\) be a state of \(C^*(G)\). Its cyclic GNS representation from BG/UB-03 has a unit vector \(x\); PF-26 integrates it to \(U\), so \(\varphi(g)=\langle U(g)x,x\rangle\). In particular \(\varphi(e)=1\), \(|\varphi(g)|\le1\), and \(\varphi(g^{-1})=\overline{\varphi(g)}\). Cauchy–Schwarz and unitarity give

\[
 \begin{aligned}
 |\varphi(g)-\varphi(h)|
 &\le\|U(g)x-U(h)x\|\\
 &=\sqrt{2-2\operatorname{Re}\varphi(g^{-1}h)}.
 \end{aligned}
 \tag{PF.110}
\]

The squared norm initially gives \(\operatorname{Re}\varphi(h^{-1}g)\); its real part equals that of \(\varphi(g^{-1}h)\) by the inverse identity. Apply (PF.110) to \(g^{-1},h^{-1}\), and use that inverse identity again:

\[
 |\varphi(g)-\varphi(h)|
 \le\sqrt{2-2\operatorname{Re}\varphi(gh^{-1})}.
 \tag{PF.111}
\]

Taking the minimum proves exactly both alternatives in Proposition 3.26(i). The two radicands are nonnegative because the coefficients have modulus at most one.

## Compact-uniform state convergence implies weak-star convergence

Suppose a net of states \((\varphi_i)\) converges to a state \(\varphi_0\) uniformly on every compact subset of \(G\). For \(f\in L^1(G)\) and \(\epsilon>0\), choose \(f_0\in C_c(G)\) with \(\|f-f_0\|_1<\epsilon\); the compactly supported approximation is available for arbitrary locally compact \(G\). Each coefficient is bounded by one, so

\[
 |\varphi_i(f)-\varphi_0(f)|
 \le\|f_0\|_1\sup_{\operatorname{supp}f_0}
                   |\varphi_i(g)-\varphi_0(g)|
    +2\|f-f_0\|_1 .
 \tag{PF.112}
\]

First let \(i\) advance and then \(\epsilon\downarrow0\). Thus the net converges on \(L^1(G)\). This algebra is norm dense in \(C^*(G)\), and \(\|\varphi_i-\varphi_0\|\le2\); a second three-term approximation proves convergence on every element of \(C^*(G)\), precisely weak* convergence in its dual. No compactness claim about the state space of the possibly nonunital \(C^*(G)\) is needed.

## Weak-star state convergence implies compact-uniform convergence

Conversely let \(\varphi_i\to\varphi_0\) weak* in \(C^*(G)^*\), and fix a compact \(K\subset G\). The following positive averaged-defect argument avoids any assumption of pointwise convergence of \(\varphi_i(g)\).

Choose \(\eta>0\). Continuity of \(\varphi_0\) at \(e\) and \(\varphi_0(e)=1\) give a relatively compact identity neighborhood \(V\) with \(1-\operatorname{Re}\varphi_0(v)<\eta\) on \(V\). Choose \(q\in C_c(G)\), \(q\ge0\), supported in \(V\), with \(\int q(v)\,dv=1\). Define

\[
 d_i=\int_Gq(v)\bigl(1-\operatorname{Re}\varphi_i(v)\bigr)\,dv
    =1-\operatorname{Re}\varphi_i(q).
 \tag{PF.113}
\]

Every integrand is nonnegative, \(d_0<\eta\), and weak* convergence at the fixed \(L^1\) element \(q\) implies \(d_i\to d_0\). Eventually \(d_i<2\eta\). Define the right-smoothed coefficient

\[
 S_i(g)=\int_Gq(v)\varphi_i(gv)\,dv
       =\varphi_i(\lambda(g)q),
 \qquad(\lambda(g)q)(t)=q(g^{-1}t).
 \tag{PF.114}
\]

The last identity uses \(t=gv\) and left Haar invariance. By (PF.110), Jensen's inequality for the probability density \(q(v)\,dv\), and (PF.113),

\[
 \sup_{g\in G}|S_i(g)-\varphi_i(g)|
 \le\int q(v)\sqrt{2-2\operatorname{Re}\varphi_i(v)}\,dv
 \le\sqrt{2d_i}.
 \tag{PF.115}
\]

The same bound for \(i=0\) is \(<\sqrt{2\eta}\), while eventually the bound for \(i\) is \(<2\sqrt\eta\). This is a uniform-in-\(g\) approximation.

The map \(g\mapsto\lambda(g)q\) is norm continuous into \(L^1(G)\) by the group-analysis input. Therefore
\(\mathcal Q_K=\{\lambda(g)q:g\in K\}\)
is norm compact in \(L^1(G)\), and its image is norm compact in \(C^*(G)\) because the full group norm is at most the \(L^1\)-norm. Bounded weak* convergence of the functionals is uniform on this compact test set. Explicitly, for any tolerance cover \(\mathcal Q_K\) by finitely many norm balls; weak* convergence at their centers and \(\|\varphi_i-\varphi_0\|\le2\) control all points in the balls. Hence

\[
 \sup_{g\in K}|S_i(g)-S_0(g)|\longrightarrow0.
 \tag{PF.116}
\]

Combining (PF.115)–(PF.116) gives eventually

\[
 \sup_{g\in K}|\varphi_i(g)-\varphi_0(g)|
 <2\sqrt\eta
  +\sup_{g\in K}|S_i(g)-S_0(g)|
  +\sqrt{2\eta}.
 \tag{PF.117}
\]

Given \(\epsilon>0\), choose \(\eta\) first so that the first and third terms total less than \(\epsilon/2\), then advance the net until the middle term is less than \(\epsilon/2\). This proves compact-uniform convergence. Both directions hold for arbitrary nets, so the weak* topology on the state space agrees with the topology of uniform convergence on compact subsets of \(G\). That is Proposition 3.26(ii), in full topological strength.

The source proof on printed p. 85 has a complex-versus-real inequality and places the absolute value inside an integral where weak* convergence only controls the absolute value of the integral. It also switches from \(\varphi_i\) to \(f_i\); printed p. 86 omits a plus sign in its last three-term estimate. The original proof above uses the nonnegative real defect (PF.113), for which the needed inference is valid, and gives all three terms in (PF.117). These source slips are not new hypotheses or counterexamples to the proposition.

PF-37–40 address VII.3(1)–(3), including the printed derivative-version defect; PF-41–44 give qualified treatments of VII.3(4)–(7). The exact qualifications are stated after PF-44.

## Borel measure classes and derivative versions

The earlier PF results use a locally compact group and its Haar measure. Here we begin with only a standard Borel group and a σ-finite Borel measure class. No group topology is assumed until the later converse-to-Haar obligations. The source is Takesaki, Theory of Operator Algebras II, Exercise VII.3(1)–(3), printed p. 87 / supplied PDF p. 107. The necessary scalar inputs are the Radon–Nikodym theorem for σ-finite measures, σ-finite product Fubini/Tonelli, Borel parameter integration, and a countable Borel generator. These scalar inputs are not proved in this lesson. The joint derivative selection and finite-partition convergence needed below are proved here. The printed exercise contains a version-dependent pointwise claim; we exhibit the defect and prove the invariant-measure theorem with a strict replacement.

Let G be a standard Borel group: multiplication and inversion are Borel. Let μ be a nonzero σ-finite Borel measure whose null sets are preserved by every left translation. For each fixed a, choose a Borel Radon–Nikodym representative χ(a,·) such that

\[
\mu(aE)=\int_E\chi(a,x)\,d\mu(x)
\tag{PF.118}
\]

for Borel E. For each fixed a, χ(a,·) is finite and strictly positive μ-almost everywhere, but the choice may be arbitrary on an a-dependent null set. The printed hypotheses do not require joint Borel measurability in (a,x).

### Fixed-parameter cocycle

For fixed a,b and every Borel E, the weighted transport form of (PF.118) gives

\[
\begin{aligned}
\mu(abE)
 &=\int_{bE}\chi(a,t)\,d\mu(t)\\
 &=\int_E\chi(a,bx)\chi(b,x)\,d\mu(x).
\end{aligned}
\tag{PF.119}
\]

The second equality follows first for indicators in the transport identity for b, then for nonnegative Borel functions by monotone convergence. Comparing (PF.119) with (PF.118) for ab proves

\[
\chi(ab,x)=\chi(a,bx)\chi(b,x)
\quad\text{for μ-almost every }x
\tag{PF.120}
\]

for each *fixed* pair (a,b). Also χ(e,x)=1 μ-almost everywhere. A representative may be normalized on the row a=e to make the latter identity pointwise, but (PF.118) alone does not imply it pointwise.

### A jointly Borel counterexample to the printed diagonal step

Take the additive group \(\mathbb R\) with Borel Lebesgue measure. Define a positive, finite, jointly Borel function

\[
\chi(a,b)=
\begin{cases}
2,&a\ne0,\quad b>0,\quad a+b=1,\\
1,&\text{otherwise}.
\end{cases}
\tag{PF.121}
\]

For each fixed \(a\), the set where \(\chi(a,b)\) differs from 1 contains at most the single point \(b=1-a\). Consequently (PF.118) holds for *every* a and E, because Lebesgue measure is translation invariant. The row \(\chi(0,b)\) is identically 1, so even the printed normalization is met. For each fixed \(a,c\), both sides of (PF.120) differ from 1 at at most finitely many \(x\), so (PF.120) holds.

The expression requested in the next subpart, evaluated at g=1, is

\[
R_1(k)=\frac{\chi(1-k,k)}{\chi(-k,k)}
 =
\begin{cases}
2,&k>0,\ k\ne1,\\
1,&k\le0\ \text{or}\ k=1.
\end{cases}
\tag{PF.122}
\]

The denominator equals 1 for every k because its two arguments sum to 0. Thus \(R_1\) is not almost everywhere constant. Both \(V=[-1,0]\) and \(V=[1/2,3/2]\) have finite positive measure and the integrand is bounded, yet the proposed average yields respectively 1 and 2. The issue persists after joint measurability, positivity, and identity-row normalization are added: one cannot substitute \(b=k^{-1}\) into (PF.120), because the exceptional set for \((a,b)\) may depend on \(b\) and can cover that diagonal.

### Valid strict-cocycle repair and conditional invariant measure

A sufficient additional hypothesis is a positive jointly Borel *strict* cocycle: a Borel function \(c:G\times G\to(0,\infty)\) satisfying \(c(ab,x)=c(a,bx)c(b,x)\) for all triples. Define \(f(g)=c(g,e)\). It is positive and Borel. Setting \(x=e\) in the strict identity gives

\[
c(a,b)=\frac{f(ab)}{f(b)}
\quad\text{for all }a,b.
\tag{PF.123}
\]

It follows at once that \(c(e,x)=1\); alternatively this follows from strict cocycle and positivity. The printed diagonal quotient is then \(f(g)/f(e)\), which is constant (and \(f(e)=1\) under normalization).

The following conclusion needs only a positive finite Borel f and the relation

\[
\chi(a,x)=f(ax)/f(x)\quad\text{for μ-almost every }x
\tag{PF.124}
\]

for each fixed \(a\). Define \(\nu(E)=\int_E f(x)^{-1}\,d\mu(x)\). It is equivalent to \(\mu\) and σ-finite: intersect a \(\mu\)-finite countable cover with the Borel sets \(\{1/m\le f\le m\}\). For fixed a, weighted transport and (PF.124) yield

\[
\nu(aE)
 =\int_E f(ax)^{-1}\chi(a,x)\,d\mu(x)
 =\int_E f(x)^{-1}\,d\mu(x)
 =\nu(E).
\tag{PF.125}
\]

These equalities hold for infinite values as nonnegative extended integrals. The next construction supplies such an f from the original quasi-invariant measure, without making the invalid diagonal substitution in the printed argument.

## An invariant measure from quasi-invariance

First replace μ by an equivalent Borel probability π. Take a disjoint Borel cover \(G=\bigsqcup_j C_j\) with \(\mu(C_j)<\infty\), give \(C_j\) the positive density \(2^{-j}/(1+\mu(C_j))\), and divide by its finite nonzero integral. The resulting Borel density is positive and finite everywhere, so equivalence preserves quasi-invariance. For each \(a\), the probability kernel \(K_a(E)=\pi(aE)\) is equivalent to \(\pi\). For fixed Borel \(E\), the map \(a\mapsto K_a(E)\) is Borel, since

\[
K_a(E)=\int_G {\bf1}_E(a^{-1}x)\,d\pi(x).
\tag{PF.126}
\]

Here is a direct jointly Borel Radon–Nikodym selection. Let \(\mathcal P_n\) be increasing finite Borel partitions whose union generates the Borel σ-algebra. On a cell \(C\) of \(\mathcal P_n\) with \(\pi(C)>0\), set \(D_n(a,x)=\pi(aC)/\pi(C)\) for \(x\in C\); set \(D_n=1\) on \(\pi\)-null cells. Each \(D_n\) is jointly Borel, finite and positive because \(\pi\) is quasi-invariant. For fixed \(a\), \(D_n(a,\cdot)\) is the conditional expectation, relative to \(\mathcal P_n\), of the Radon–Nikodym derivative of \(K_a\) with respect to \(\pi\).

The required almost-everywhere convergence can be proved directly here. For any nonnegative integrable \(u\), the first-crossing cells of the finite partitions are disjoint and each satisfies \(\int_C u\,d\pi>\epsilon\pi(C)\) when its conditional average first exceeds \(\epsilon\). Summing gives \(\pi(\sup_n E[u\mid\mathcal P_n]>\epsilon)\le\|u\|_1/\epsilon\). Since the union of the finite partition algebras generates the Borel σ-algebra, its simple functions are dense in \(L^1(\pi)\) by the monotone-class theorem. Approximate a given density \(\rho\) by \(\mathcal P_{N_m}\)-measurable simple functions \(\rho_m\) with \(\|\rho-\rho_m\|_1\le 2^{-2m}\). For \(n\ge N_m\), \(E[\rho_m\mid\mathcal P_n]=\rho_m\). Markov's inequality controls \(|\rho-\rho_m|>2^{-m}\) by \(2^{-m}\), and \( |E[v\mid\mathcal P_n]|\le E[|v|\mid\mathcal P_n]\) for \(v=\rho-\rho_m\); the same first-crossing bound therefore controls \(\sup_{n\ge N_m}|E[\rho-\rho_m\mid\mathcal P_n]|>2^{-m}\) by \(2^{-m}\). Borel–Cantelli then gives \(E[\rho\mid\mathcal P_n]\to\rho\) almost everywhere. Apply this separately to each fixed a; no uniform null set in a is asserted or needed. Take the jointly Borel limsup of D_n and replace any zero or infinite value by 1. The result is a jointly Borel function

\[
D:G\times G\longrightarrow(0,\infty)
\tag{PF.127}
\]

whose row \(D(a,\cdot)\) represents \(K_a\) for every \(a\). The fixed-parameter argument (PF.119)–(PF.120), now followed by Tonelli in the first two variables under \(\pi\otimes\pi\), gives its cocycle relation for \(\pi^{\otimes3}\)-almost every \((a,b,x)\).

We need one measure-class fact before changing variables in that triple relation. On \(G^2\) let \(S(x,y)=(x,xy)\) and \(R(x,y)=(y,x)\). The swap \(R\) preserves \(\pi\otimes\pi\) exactly. Both \(S\) and \(S^{-1}\) preserve its *measure class*: for each fixed x, left translation by x maps π-null sets to π-null sets in both directions, and Fubini identifies product-null sets by their sections. Thus the composition

\[
T=S^{-1}\circ R\circ S\circ R,\qquad T(x,y)=(yx,x^{-1})
\tag{PF.128}
\]

preserves the product measure class. If \(N\) is \(\pi\)-null, apply this property to \(G\times N\). Its inverse image under T is \(\{x:x^{-1}\in N\}\times G\), so inversion preserves π-null sets. Inversion is an involution, hence it preserves the class in both directions. Every right translation is a composition of inversion, left translation, and inversion, since \(x h=(h^{-1}x^{-1})^{-1}\); therefore every right translation also preserves the π-measure class.

Now the Borel bijection

\[
\Phi(a,g,h)=(a,gh^{-1},h)
\tag{PF.129}
\]

preserves the \(\pi^{\otimes3}\) measure class, by Fubini over \(h\) and right-translation quasi-invariance in \(g\). Pull back the \(\pi^{\otimes3}\)-conull cocycle relation along \(\Phi\). The result is

\[
D(agh^{-1},h)=D(a,g)D(gh^{-1},h)
\quad\text{for π³-almost every }(a,g,h).
\tag{PF.130}
\]

Choose \(h_0\) by Fubini so that (PF.130) holds for \(\pi^{\otimes2}\)-almost every \((a,g)\) when \(h=h_0\), and set

\[
F(g)=D(gh_0^{-1},h_0)>0.
\tag{PF.131}
\]

The function \(F\) is finite and Borel everywhere, and \(F(ag)=D(a,g)F(g)\) for \(\pi^{\otimes2}\)-almost every \((a,g)\). Consequently there is a Borel \(\pi\)-conull set \(A\) of parameters for which this relation holds for \(\pi\)-almost every \(g\). Define \(\nu(E)=\int_E F(g)^{-1}d\pi(g)\). It is σ-finite and equivalent to π. By weighted transport, \(\nu(aE)=\nu(E)\) for every Borel \(E\) and every \(a\in A\).

Let \(H\) be the subgroup of all \(a\) for which left translation by \(a\) preserves \(\nu\). It contains \(A\). For arbitrary \(t\in G\), the sets \(A\) and \(tA\) are both \(\pi\)-conull, so they intersect. Choose \(u\in A\cap tA\) and write \(u=tv\) with \(v\in A\). Then \(t=uv^{-1}\in H\). Hence \(H=G\): the measure \(\nu\) is left invariant under every translation, not just almost every one.

Finally choose a positive finite Borel version \(w=d\mu/d\pi\). Then \(\mu=w\pi=(wF)\nu\). Put \(f_0=wF\), \(c=f_0(e)>0\), \(f=f_0/c\), and \(\widetilde\nu=c\nu\). Thus \(f(e)=1\), \(\mu=f\widetilde\nu\), and \(\widetilde\nu(E)=\int_E f^{-1}d\mu\) is left invariant. For every fixed a, left invariance of \(\widetilde\nu\) yields

\[
\mu(aE)
 =\int_E f(ax)\,d\widetilde\nu(x)
 =\int_E \frac{f(ax)}{f(x)}\,d\mu(x).
\tag{PF.132}
\]

Radon–Nikodym uniqueness shows that the *original supplied* \(\chi(a,x)\) equals \(f(ax)/f(x)\) for \(\mu\)-almost every \(x\), for each fixed \(a\). The replacement \(\chi^\ast(a,x)=f(ax)/f(x)\) is jointly Borel, positive, strict-cocyclic for all triples, and normalized at \(e\). For this replacement, the diagonal quotient is exactly \(f(g)\) for every \(k\). The printed claim about that quotient for an arbitrary supplied χ remains false by (PF.121)–(PF.122); the invariant-measure and coboundary conclusions are nevertheless proved under the original measure-class hypothesis.

## Uniqueness of invariant measures

The argument uses only measurable multiplication and inversion, not local compactness. Let \(\mu\) and \(\nu\) be σ-finite left-invariant Borel measures. If one is zero, it is the zero multiple of the other; assume both are nonzero for a positive proportionality constant. Put \(\lambda=\mu+\nu\). This is σ-finite: if \(\mu\) is finite on \(A_n\) and \(\nu\) finite on \(B_m\), the sets \(A_n\cap B_m\) cover \(G\) and have finite \(\lambda\)-measure. It is left invariant. Choose a Borel version \(p=d\mu/d\lambda\) with \(0\le p\le1\) everywhere.

For any fixed a and Borel E, left invariance of μ and λ yields

\[
\int_E p(ax)\,d\lambda(x)
 =\int_{aE}p(t)\,d\lambda(t)
 =\mu(aE)=\mu(E)=\int_Ep(x)\,d\lambda(x).
\tag{PF.133}
\]

Thus \(p(ax)=p(x)\) for \(\lambda\)-almost every \(x\), for each fixed \(a\). Since \(p\) and multiplication are jointly Borel and \(\lambda\) is σ-finite, Tonelli/Fubini upgrades this to

\[
p(xy)=p(y)
\quad\text{for }(\lambda\otimes\lambda)\text{-almost every }(x,y).
\tag{PF.134}
\]

The naive variable swap gives \(p(yx)=p(x)\), which does not combine with (PF.134) in a noncommutative group. Use instead the measurable product shear \(S(x,y)=(x,xy)\) and coordinate swap \(R(x,y)=(y,x)\). The shear \(S\) preserves \(\lambda\otimes\lambda\) because for each fixed \(x\), the map \(y\mapsto xy\) preserves \(\lambda\). Its inverse \(S^{-1}(x,z)=(x,x^{-1}z)\) and \(R\) also preserve \(\lambda\otimes\lambda\). Their composition

\[
T=S^{-1}\circ R\circ S\circ R,\qquad T(x,y)=(yx,x^{-1})
\tag{PF.135}
\]

therefore preserves \(\lambda\otimes\lambda\). Pull back the full-measure identity (PF.134) by \(T\). Since \((yx)x^{-1}=y\), it becomes

\[
p(y)=p(x^{-1})
\quad\text{for }(\lambda\otimes\lambda)\text{-almost every }(x,y).
\tag{PF.136}
\]

Choose a Borel set \(A\) with \(0<\lambda(A)<\infty\). Fubini supplies \(x\in A\) for which (PF.136) holds for \(\lambda\)-almost every \(y\). Then \(p(y)=c:=p(x^{-1})\) for \(\lambda\)-almost every \(y\), with \(0\le c\le1\). Hence \(\mu=c\lambda\) and \(\nu=(1-c)\lambda\). Because both measures are nonzero, \(0<c<1\) and \(\mu=[c/(1-c)]\nu\).

The only product-measure step that can fail without σ-finiteness is the Fubini upgrade; no right-translation quasi-invariance was assumed.

## The Borel modular homomorphism

Let \(\mu\) be a nonzero σ-finite left-invariant Borel measure on \(G\). For \(g\in G\), define \(\mu_g(E)=\mu(Eg)\). Right multiplication is a Borel bijection with Borel inverse. The measure \(\mu_g\) is σ-finite: if \(G=\bigcup_n F_n\) with \(\mu(F_n)<\infty\), then \(G=\bigcup_n F_n g^{-1}\) and \(\mu_g(F_n g^{-1})=\mu(F_n)\). It is nonzero, and for every \(a\in G\),

\[
\mu_g(aE)=\mu(aEg)=\mu(Eg)=\mu_g(E).
\tag{PF.137}
\]

PF-39 therefore gives a unique \(\delta(g)>0\) such that \(\mu_g=\delta(g)\mu\). In particular \(\mu(Eg)=\delta(g)\mu(E)\) for every Borel \(E\), including infinite-measure sets.

For any Borel \(E\) with \(0<\mu(E)<\infty\), the scale has the concrete formula

\[
\delta(g)=\frac{\mu(Eg)}{\mu(E)}
=\frac{1}{\mu(E)}\int_G {\bf1}_E(xg^{-1})\,d\mu(x).
\tag{PF.138}
\]

The integrand is Borel on \(G\times G\) because multiplication and inversion are Borel. Its nonnegative parameter integral is Borel by σ-finiteness and the monotone-class/Tonelli theorem. Thus δ is Borel. Finally,

\[
\mu(Egh)=\delta(h)\mu(Eg)
        =\delta(h)\delta(g)\mu(E),
\tag{PF.139}
\]

so \(\delta(gh)=\delta(g)\delta(h)\), \(\delta(e)=1\), and \(\delta(g^{-1})=\delta(g)^{-1}\). If \(\mu=0\), the source conclusion is trivially satisfied by \(\delta\equiv1\); uniqueness then has no content.

The remaining VII.3 exercises start with a standard Borel group and a nonzero sigma-finite invariant measure; no topology is assumed. The regular representation will produce a compatible locally compact topology. Only after that step do we apply PF-10–15 to the group-like operators. Exercise 6 starts instead with a nonzero quasi-invariant measure and uses PF-38. Exercise 7 compares the reconstructed topology with specified Polish topologies. The source is Takesaki II, Exercise VII.3(4)–(7), printed p. 88 / PDF p. 108. The scalar, descriptive-set, compact-group and other course prerequisites used below are not proved in this lesson. The printed omission of nonzero measure and the unstated unitary-group topology are discussed below; literal versions with zero measure are false.

## A compact neighborhood from a measured Borel group

Put \(H=L^2(G,\mu)\) and

\[
(\lambda(a)\xi)(x)=\xi(a^{-1}x).
\tag{PF.140}
\]

Left invariance makes each \(\lambda(a)\) unitary and \(a\mapsto\lambda(a)\) a homomorphism. Standard Borel sigma-algebras have countable separating generators. Choose a countable separating family \((A_n)\) of Borel sets and a countable cover \((F_m)\) by sets of finite \(\mu\)-measure. The family

\[
\mathcal C=\{A_n\cap F_m:n,m\ge1\}\cup\{F_m:m\ge1\}
\tag{PF.141}
\]

consists of finite-measure Borel sets and separates the points of \(G\). Its indicator functions, after taking finite Boolean combinations and the finite-measure cover, span a dense subspace of \(H\). In particular \(H\) is separable.

For \(C,D\in\mathcal C\), the coefficient

\[
\langle\lambda(a)1_C,1_D\rangle
=\int_G1_C(a^{-1}x)1_D(x)\,d\mu(x)
\tag{PF.142}
\]

is Borel in \(a\) by Borel parameter integration; it is finite since \(\mu(D)<\infty\). Approximating arbitrary vectors by the countable simple-function core shows that \(a\mapsto\lambda(a)\) is Borel into \(U(H)\) with its strong operator topology. More explicitly, for any core vector \(\xi\), squared distances from \(\lambda(a)\xi\) to a countable dense family in \(H\) are Borel by (PF.142); those distance functions test Borelness of the \(H\)-valued map.

The map is injective. If \(\lambda(a)=1\), then for every \(C\in\mathcal C\),

\[
1_C(a^{-1}x)=1_C(x)\quad\text{for \(\mu\)-almost every }x.
\tag{PF.143}
\]

Intersect the countably many conull sets. At every point of their intersection, \(a^{-1}x\) and \(x\) have the same \(\mathcal C\)-membership and hence are equal. The intersection is nonempty because \(\mu\ne0\); left multiplication is free, so \(a=e\).

For separable \(H\), \(U(H)\) in the strong operator topology is Polish. One may use a dense sequence \((\xi_j)\) and a bounded sum of both \(\|(u-v)\xi_j\|\) and \(\|(u^*-v^*)\xi_j\|\) as a complete compatible metric. A Cauchy sequence has mutually inverse strong limits of its operators and adjoints, so its limit remains unitary. Separability follows from the embedding into a countable product of copies of \(H\). By the Lusin–Souslin theorem, the injective Borel image

\[
G_\lambda=\lambda(G)\subset U(H)
\tag{PF.144}
\]

is Borel and \(\lambda:G\to G_\lambda\) is a Borel isomorphism. Endow \(G_\lambda\) with its relative strong operator topology. It is a second-countable Hausdorff topological group; on unitaries, inversion and multiplication are strongly continuous.

### The compact-neighborhood step

Transport \(\mu\) to a sigma-finite left-invariant Borel measure \(\bar\mu\) on \(G_\lambda\). Choose a Borel \(E\subset G_\lambda\) with \(0<\bar\mu(E)<\infty\). Extend \(\bar\mu|_E\) by zero to a finite Borel measure on the Polish ambient space \(U(H)\). Since \(E\) is Borel, inner regularity of finite Borel measures on Polish spaces supplies a compact

\[
K\subset E,\qquad 0<\bar\mu(K)<\infty.
\tag{PF.145}
\]

Write \(A=\lambda^{-1}(K)\), so \(1_A\in H\). For \(u=\lambda(a)\in G_\lambda\),

\[
F(u)=\langle u1_A,1_A\rangle
=\bar\mu(uK\cap K).
\tag{PF.146}
\]

The first expression is strong-operator continuous on \(G_\lambda\), and \(F(1)=\bar\mu(K)>0\). Hence \(V=\{u:F(u)>0\}\) is an open identity neighborhood. If \(u\in V\), then \(uK\cap K\ne\varnothing\), so \(u=k_1k_2^{-1}\) for some \(k_1,k_2\in K\). Thus

\[
1\in V\subset KK^{-1},\qquad KK^{-1}\text{ compact in }G_\lambda.
\tag{PF.147}
\]

The closure of \(V\) is compact, proving \(G_\lambda\) locally compact.

This argument uses the strong topology *defined by the regular representation*, not a topology assumed on the original Borel group. In particular, it does not import the locally compact Theorem 3.9 to establish local compactness.

Because \(G_\lambda\) is second-countable and locally compact, it is sigma-compact; its left Haar measure \(m\) is sigma-finite. Both \(m\) and \(\bar\mu\) are nonzero sigma-finite left-invariant Borel measures on the same standard Borel group. The noncommutative shear proof of VII.3(2), recorded in PF-39, therefore gives

\[
\bar\mu=c\,m\quad\text{for a unique }c>0.
\tag{PF.148}
\]

Consequently the transported original measure is locally finite and Radon. This is proved *after* local compactness, not assumed in (PF.145).

## Group-like reconstruction after local compactness

Let \(\delta:G\to(0,\infty)\) be the Borel homomorphism from VII.3(3), with \(\mu(Ea)=\delta(a)\mu(E)\). On \(H\), define

\[
(\rho(a)\xi)(x)=\delta(a)^{1/2}\xi(xa).
\tag{PF.149}
\]

This is unitary because \(\int|\xi(xa)|^2\,d\mu(x)=\delta(a)^{-1}\|\xi\|_2^2\); it commutes with \(\lambda(G)\). The Borel shear \((g,h)\mapsto(g,gh)\) and its Borel inverse preserve \(\mu\otimes\mu\) by left invariance in the second variable. Thus

\[
(W\zeta)(g,h)=\zeta(g,gh)
\tag{PF.150}
\]

is unitary on \(H\otimes H=L^2(G^2,\mu\otimes\mu)\), and direct substitution gives

\[
W^*(\lambda(a)\otimes1)W=\lambda(a)\otimes\lambda(a).
\tag{PF.151}
\]

Now (PF.147) has already supplied a locally compact topology with Borel structure unchanged, and (PF.148) says \(\mu\) is a positive scalar multiple of Haar measure for it. The scalar rescaling \(L^2(G,\mu)\to L^2(G,m)\) intertwines both regular representations and \(W\). Therefore the previously proved locally compact group-like reconstruction, PF-10–15 (Takesaki VII.3 Theorem 3.9), applies with no circularity. It gives

\[
\mathfrak G
=\{x\in B(H)\setminus\{0\}:W^*(x\otimes1)W=x\otimes x\}
=\lambda(G).
\tag{PF.152}
\]

Thus the group-like set is a locally compact group containing the copy of \(G\) requested in Exercise 4, and Exercise 5 sharpens containment to equality. Equip \(\mathfrak G\) with the weak operator topology specified by the source's Theorem 3.9. Weak and strong operator topologies coincide on the unitary set when the limit is unitary, since

\[
\|(u_i-u)\xi\|^2
=2\|\xi\|^2-2\operatorname{Re}\langle u_i\xi,u\xi\rangle.
\tag{PF.153}
\]

Hence the topology of \(\mathfrak G\) is the locally compact topology obtained in (PF.147).

This route differs from the printed hint for Exercise 5: it constructs local compactness directly from the measured regular image, then invokes the already independent Theorem 3.9. It does not assert concentration of a Haar measure on an unknown larger character group before its equality with \(G\) is proved.

## Compatible topology from quasi-invariance

For a nonzero sigma-finite Borel measure \(\mu\) whose class is left-translation invariant, VII.3(1d) as corrected in PF-38 constructs an equivalent nonzero sigma-finite **invariant** Borel measure \(\nu\). Apply PF-41–42 to \(\nu\). Pulling the relative strong topology on \(\lambda_\nu(G)\) back along its Borel isomorphism gives the desired locally compact second-countable Hausdorff group topology on \(G\), with precisely its supplied Borel sigma-algebra. The original \(\mu\) is equivalent to Haar measure in this topology. The zero measure would make the printed conclusion false for an arbitrary standard Borel group; nonzero is essential.

### Comparison with a given Polish topology

We will use the following Borel automatic-continuity fact to interpret Exercise 7. A Borel group isomorphism between Polish groups whose inverse is Borel is a homeomorphism. Here is the category proof. Let \(f:P\to Q\) be a surjective Borel homomorphism, and let \(V\) be an identity neighborhood in \(Q\). Choose symmetric open \(W\) with \(WW^{-1}\subset V\). Separability of \(Q\) gives countably many translates of \(W\) covering \(Q\). Their inverse images cover the Baire space \(P\), so \(A=f^{-1}(W)\) is nonmeagre. A Borel set has the Baire property. The Pettis category argument says \(AA^{-1}\) contains an identity neighborhood: on some nonempty open \(O\), \(A\) is comeagre; for \(g\) sufficiently near the identity, \(O\cap gO\) is nonempty open and its two comeagre subsets \(A\) and \(gA\) meet. Then \(f(AA^{-1})\subset WW^{-1}\subset V\), proving continuity. Apply the same argument to \(f^{-1}\).

The reconstructed \(G_\lambda\) is locally compact and second-countable, hence Polish; the inverse \(\lambda^{-1}\) is Borel by Lusin–Souslin. If an original group topology is Polish and has the supplied Borel sets, the identity between it and the reconstructed topology is a Borel isomorphism and therefore a homeomorphism. Thus a nonzero sigma-finite quasi-invariant Borel measure on a Polish group forces its *original* topology to be locally compact.

## Infinite-dimensional obstructions

Let \(\mathcal H\) be an infinite-dimensional separable Hilbert space with its norm topology and norm-Borel sets. It is a Polish additive group but is not locally compact: every neighborhood of zero contains a closed ball of some positive radius, and that ball contains a scaled orthonormal sequence without any convergent subsequence. If a nonzero sigma-finite Borel measure on \(\mathcal H\) were quasi-invariant under every translation, PF-43 would make this norm topology locally compact, a contradiction.

For a nonseparable Hilbert space the norm-Borel structure is not the standard Borel premise of VII.3(1)–(6); the source must specify a measurable structure and topology before the same inference can be made. The zero measure remains a literal counterexample unless excluded.

### The unitary group of a factor

Let \(M\) be an infinite-dimensional factor with separable predual, represented faithfully normally on a separable Hilbert space. Give \(U(M)\) the strong operator topology; on unitaries this equals the strong-star group topology. It is a Polish group: \(U(H)\) is Polish by the metric argument in PF-41, and \(U(M)=U(H)\cap M\) is closed in it. Its Borel sets are the intended standard Borel structure.

We prove it is not locally compact. An infinite-dimensional factor contains mutually orthogonal nonzero projections \(q_1,q_2,\ldots\). Here is a direct reason. If no countably infinite orthogonal family existed, every nonzero projection would contain a minimal subprojection: otherwise recursively split a nonzero remainder and retain a nonzero orthogonal piece at each step. A maximal family of orthogonal minimal projections would then be finite and sum to \(1\), since any nonzero complement would contain another minimal projection. For minimal projections \(e_i,e_j\), every corner \(e_iMe_j\) has dimension at most one: any nonzero element has polar part a partial isometry between the two minimal ranges, and comparison with that part makes any other element a scalar multiple. The finite corner decomposition \(M=\sum_{i,j}e_iMe_j\) would make \(M\) finite-dimensional, a contradiction. Set \(p_k=\bigvee_{n\ge k}q_n\). Then \(p_k\downarrow0\) strongly, while every corner \(p_kMp_k\) is an infinite-dimensional factor because it contains all the \(q_n\) for \(n\ge k\).

Take any basic strong identity neighborhood determined by \(\xi_1,\ldots,\xi_r\) and \(\varepsilon>0\). Choose \(k\) so that \(2\|p_k\xi_j\|<\varepsilon\) for all \(j\). Every \(v\in U(p_kMp_k)\) extends to \(u=v+(1-p_k)\in U(M)\) and satisfies

\[
\|(u-1)\xi_j\|\le2\|p_k\xi_j\|<\varepsilon.
\tag{PF.154}
\]

The embedded corner unitary group is closed in \(U(M)\). If the latter had a compact identity neighborhood, the former would be compact in the strong topology.

The strong-topology unitary group of an infinite-dimensional factor cannot be compact. The factor argument in PF47, using the exact RT-CPT-01 compact-representation theorem, applies to every faithful normal representation, without a separability assumption: a compact unitary group produces a nonzero compact operator in the commutant, whose finite-dimensional eigenspace gives a faithful normal representation of the factor. The factor would therefore be finite dimensional. An alternative proof goes through the decomposition of compact-group representations; the current course uses PF47 for this implication.

Consequently \(U(M)\) is not locally compact. PF-43 excludes a nonzero sigma-finite Borel measure quasi-invariant under all left translations. The statement requires this strong/strong-star Polish group convention (or another specified Polish group topology) and excludes the zero measure; neither qualification is explicit in the printed Exercise 7(ii).

The arbitrary-derivative claim in printed Exercise 1(b) is refuted; Exercises 4, 6 and 7 require a nonzero measure, and Exercise 7(ii) is proved here for the strong-topology Polish unitary group of a factor with separable predual. Neither the zero-measure versions nor a version with an unspecified unitary-group topology is proved here.
## The regular predual is a closed isometric ideal

Let \(G\) be an arbitrary locally compact Hausdorff group, with the Haar conventions of PF-01 and PF-21. Put \(D=C^*(G)\), \(N=M_l\), and \(W=D^{**}\). PF-26 gives the nondegenerate integrated regular representation \(q:D\to B(L^2(G))\). Its bicommutant is \(N\), since \(q(D)\) is the norm closure of the integrated left translations.

Extension of a representation by its coefficient functionals through Surjectivity uses a compact ball and the exact density theorem provide its normal extension and exact central carrier:

\[
\begin{gathered}
\bar q:W\longrightarrow N,\\
\ker\bar q=(1-z)W,\\
V=\bar q|_{zW}:zW\xrightarrow{\;\cong\;}N,\\
\kappa=V^{-1}.
\end{gathered}
\tag{PF.155}
\]

The projection \(z\) is central; \(V\) and \(\kappa\) are normal and isometric. Thus \(\bar q\) maps the unit ball of \(W\) onto the unit ball of \(N\), with contractive lift \(\kappa(y)\). This requires no contractive lift in \(D\).

For \(\rho\in N_*\), the composite \(\rho\bar q\) is normal on \(W\). The canonical predual of \(W\) is \(D^*\), by UB-04–05. Hence \(R\rho=\rho q\in D^*\), and

\[
\begin{gathered}
\|R\rho\|_{D^*}=\|\rho\bar q\|_{W_*},\\
\|\rho\bar q\|_{W_*}=\|\rho\|_{N_*}.
\end{gathered}
\tag{PF.156}
\]

The first equality is UB-04's canonical restriction isometry. For the last, contractivity proves one inequality, and evaluation on every \(\kappa(y)\), \(\|y\|\le1\), proves the reverse.

For \(f\in L^1(G)\), we have \(R\rho(f)=\int f(g)\rho(\lambda(g))\,dg\). Indeed, CP-04–06 give a summable vector-series representation of \(\rho\); PF-26 integrates each coefficient, and the sum is dominated by
\(\|f\|_1\sum_n\|\xi_n\|\|\eta_n\|\).
PF-31's uniqueness of the continuous coefficient representing a \(D^*\) functional identifies \(R\rho\) with \(u_\rho\). Therefore

\[
\begin{gathered}
\|u_\rho\|_{B(G)}=\|\rho\|_{N_*},\\
\|u_\rho\|_{A(G)}=\|\rho\|_{N_*}.
\end{gathered}
\tag{PF.157}
\]

Here \(\rho\) evaluates \(\lambda(g)\) in \(N\); the group unitary need not belong to the nonunital algebra \(q(D)\).

This inclusion \(A(G)\to B(G)\) is an isometry with closed range: a \(B\)-norm convergent net in the image pulls back to a norm Cauchy net in the complete space \(N_*\), whose limit maps to the given limit. PF-33 and the conjugation statements of PF-09 and PF-32 now make \(A(G)\) a closed self-adjoint ideal of \(B(G)\) with its inherited norm. This norm closedness does not assert closedness for the supremum norm on \(C_0(G)\).

There is an exact carrier characterization. For \(\Lambda\in D^*\), let \(\widehat\Lambda\in W_*\) be its canonical normal extension. Then

\[
\begin{gathered}
\Lambda\in R(N_*)\quad\Longleftrightarrow\\
\widehat\Lambda(X)=\widehat\Lambda(zX)\\
\text{for every }X\in W.
\end{gathered}
\tag{PF.158}
\]

The forward direction uses \(\bar q((1-z)X)=0\). Conversely define
\(\rho(y)=\widehat\Lambda(\kappa(y))\). It is normal, and
\(\rho(\bar q(X))=\widehat\Lambda(zX)=\widehat\Lambda(X)\), since
\(\kappa\bar q(X)=zX\). Restriction gives \(R\rho=\Lambda\). No equality of the full and reduced group C*-algebras is assumed.

The classical closed-ideal theorem is also stated in [Jesse Peterson, *Notes on operator algebras*](https://math.vanderbilt.edu/peters10/teaching/spring2015/OperatorAlgebras.pdf), Theorem 5.5.3, printed p. 128. The argument here uses the exact existing local bidual providers to prove the norm comparison and carrier characterization.

## Positive coefficient convergence and its mass condition

Let \((\omega_i)\) be a net of bounded positive functionals on \(C^*(G)\), with another such functional \(\omega\), and continuous positive-definite coefficients \(w_i,w\). PF-27–29 and bounded positive-functional GNS give

\[
\begin{gathered}
m_i=\|\omega_i\|=w_i(e),\\
m=\|\omega\|=w(e),\\
\|w_i\|_\infty=m_i.
\end{gathered}
\tag{PF.159}
\]

Zero is included. Write \(\xrightarrow{\mathrm{uc}}\) for uniform convergence on each compact subset of \(G\). We claim

\[
\begin{gathered}
w_i\xrightarrow{\mathrm{uc}}w\\
\Longleftrightarrow\\
\omega_i\longrightarrow\omega\ \text{weak*}\\
\text{and }m_i\longrightarrow m.
\end{gathered}
\tag{PF.160}
\]

**Reverse implication.** If \(m=0\), positivity gives \(\omega=0\) and \(w=0\), so

\[
\sup_{g\in G}|w_i(g)-w(g)|=m_i\longrightarrow0.
\tag{PF.161}
\]

If \(m>0\), then eventually \(m_i>0\). On that tail,
\(\sigma_i=\omega_i/m_i\) and \(\sigma=\omega/m\) are states. Weak* convergence and convergence of the nonzero denominators give \(\sigma_i(a)\to\sigma(a)\) for every \(a\in C^*(G)\). PF-36 applies to this net. Thus, for every compact \(K\),

\[
\begin{gathered}
\sup_K|w_i-w|
\le m_i\sup_K|w_i/m_i-w/m|+|m_i-m|
\longrightarrow0.
\end{gathered}
\tag{PF.162}
\]

Here \(|w/m|\le1\) and \(m_i\) is eventually bounded.

**Forward implication.** Apply convergence to \(\{e\}\), obtaining \(m_i\to m\) and eventual norm boundedness. For \(f\in L^1(G)\) and \(f_0\in C_c(G)\),

\[
\begin{gathered}
|\omega_i(f)-\omega(f)|
\le \|f_0\|_1\sup_{\operatorname{supp}f_0}|w_i-w|\\
+(m_i+m)\|f-f_0\|_1.
\end{gathered}
\tag{PF.163}
\]

Choose \(f_0\) in \(L^1\)-norm first, then advance the net. This proves convergence on \(L^1(G)\). Its norm-dense image in \(C^*(G)\), together with the eventual bound on \(\|\omega_i-\omega\|\), proves weak* convergence on every C*-test. This proof uses nets and adds no separability assumption. \(\square\)

The state case is PF-35–36. Peterson's Theorem 5.4.10, printed pp. 125–126, is a second source for that normalized statement. A weak* limit with smaller mass is outside its normalized premise.

**Problem 1: compare the norms.** Take \(G=\{e,s\}\), \(s^2=e\), with counting Haar measure, and set \(b(e)=1\), \(b(s)=i\). Compute its \(A\)-, \(B\)- and supremum norms.

**Solution.** PF-17 gives \(C^*(G)=C_r^*(G)\cong\mathbb C\oplus\mathbb C\). For \(a=\alpha_e\delta_e+\alpha_s\delta_s\), the character coordinates are \(a_\pm=\alpha_e\pm\alpha_s\). The coefficient functional is

\[
\begin{gathered}
\Lambda_b(a)=\alpha_e+i\alpha_s=\beta_+a_++\beta_-a_-,\\
\beta_\pm=(1\pm i)/2.
\end{gathered}
\tag{PF.164}
\]

The algebra norm is \(\max(|a_+|,|a_-|)\). Thus
\(\|\Lambda_b\|=|\beta_+|+|\beta_-|\): the triangle inequality is sharp at
\(a_\pm=\overline{\beta_\pm}/|\beta_\pm|\).
Both \(|\beta_\pm|=1/\sqrt2\). Every functional is normal on this finite-dimensional algebra, so PF-45 yields

\[
\begin{gathered}
\|b\|_A=\|b\|_B=\sqrt2,\\
\|b\|_\infty=1.
\end{gathered}
\tag{PF.165}
\]

The inherited \(B\)-norm equals the predual norm while exceeding the supremum norm.

**Problem 2: loss of mass.** On \(G=\mathbb R\), put

\[
w_n(t)=e^{-2\pi int},\qquad n=1,2,\ldots.
\tag{PF.166}
\]

Show that the associated states tend weak* to zero, but their coefficients fail compact-uniform convergence to zero.

**Solution.** Each \(w_n\) is a continuous unitary character. Its one-dimensional unit-vector representation integrates nondegenerately by PF-26, defining a positive functional \(\omega_n\) of norm one. For \(f\in C_c^1(\mathbb R)\), integration by parts gives

\[
\begin{gathered}
\omega_n(f)=\frac1{2\pi in}\int_{\mathbb R}f'(t)e^{-2\pi int}\,dt,\\
|\omega_n(f)|\le\frac{\|f'\|_1}{2\pi n}.
\end{gathered}
\tag{PF.167}
\]

The boundary term vanishes by compact support. Density of \(C_c^1(\mathbb R)\) in \(L^1(\mathbb R)\), with \(|\omega_n(f)|\le\|f\|_1\), extends convergence to every \(L^1\) test. Density of its image in \(C^*(\mathbb R)\), with \(\|\omega_n\|=1\), extends convergence to every C*-test. Hence \(\omega_n\to0\) weak*.

Nevertheless

\[
\begin{gathered}
\sup_{\{0\}}|w_n-0|=1,\\
\|\omega_n\|=1,\qquad\|0\|=0.
\end{gathered}
\tag{PF.168}
\]

The obstruction already appears on a compact singleton. The positive zero limit is not a state and has smaller mass. PF-36 explicitly requires a state limit, so this example does not contradict it.

## A compact unitary group forces a factor to be finite dimensional

Here is a direct proof of the compact-group implication used in PF44. Let \(N\subset B(H)\) be a nonzero unital von Neumann factor in a faithful normal representation. The Hilbert space may have arbitrary dimension. Give \(U(N)\) its relative strong operator topology. Then

\[
\begin{gathered}
U(N)\text{ is compact}\\
\Longleftrightarrow\\
\dim N<\infty.
\end{gathered}
\tag{PF.169}
\]

This statement concerns the strong topology. Compactness in another topology is a separate question.

Assume \(K=U(N)\) is compact. It is a compact Hausdorff topological group: multiplication and inversion are strongly continuous on unitaries. The programme Haar theorem identified in the group-analysis input supplies a left Haar measure; compactness makes its total mass finite, and positivity makes that mass nonzero. Normalize it to a probability \(m\). Every nonempty open subset of \(K\) has positive \(m\)-measure. For the last assertion, the translates of such an open set cover \(K\), and finitely many suffice; if the set were null, their union would have probability zero.

**Imported result (RT-CPT-01).** [Lemma 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/representations-of-compact-groups/reader/courses/representations-of-compact-groups/representations-of-compact-groups-unitarity-complete-reducibility-and-finite-dimension.html#result-lemma-2-2) and [Proposition 2.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/representations-of-compact-groups/reader/courses/representations-of-compact-groups/representations-of-compact-groups-unitarity-complete-reducibility-and-finite-dimension.html#result-proposition-2-5) prove that every strongly continuous unitary representation of a compact Hausdorff group on a nonzero complex Hilbert space has a nonzero finite-dimensional invariant subspace. The Hilbert space may have arbitrary dimension, and the group need not be metrizable. The general averaging and compact-eigenspace proofs belong to that lesson; only their specialization to the factor is needed here.

Apply these results to the inclusion representation \(u\mapsto u\) of \(K=U(N)\) on \(H\), which is strongly continuous by the definition of the topology. Since \(N\) is nonzero and unital, \(H\ne0\). The following short recap of the imported result specifies the objects used below and in the examples. For a unit vector \(\xi\), write \(P_\xi\eta=\langle\eta,\xi\rangle\xi\). Lemma 2.2 supplies the operator-norm integral

\[
\begin{gathered}
T=\int_KP_{u\xi}\,dm(u),\\
0\le T\le1.
\end{gathered}
\tag{PF.172}
\]

It is compact, nonzero, and commutes with every \(u\in K\). The proof of Proposition 2.5 supplies a positive eigenvalue \(c\) for which \(E=\ker(T-c1)\) is a nonzero finite-dimensional invariant subspace.

The remaining step uses the operator algebra \(N\). By the unitary test BK08, commutation of \(T\) with all of \(U(N)\) gives \(T\in N'\). Each unitary and its inverse preserves \(E\), so the orthogonal projection onto \(E\) commutes with every unitary of \(N\). Applying BK08 once more shows that it commutes with \(N\); hence \(E\) reduces \(N\).

Compression now defines a nonzero unital normal representation

\[
\begin{gathered}
\pi_E:N\longrightarrow B(E),\\
\pi_E(x)=x|_E.
\end{gathered}
\tag{PF.175}
\]

Normality follows from its matrix coefficients \(\langle x\eta,\zeta\rangle\), with \(\eta,\zeta\in E\): these are normal vector functionals on the concrete algebra \(N\). The kernel is an ultraweakly closed two-sided *-ideal. By the complete central-ideal proof UB07 it equals \(Np\) for a central projection \(p\). Since \(N\) is a factor, \(p\) is zero or one; unitality excludes one. Thus \(\pi_E\) is injective. Its target is finite dimensional, proving \(\dim N\le(\dim E)^2<\infty\).

Conversely, if \(N\) is finite dimensional, its unitary group is a closed bounded subset of that finite-dimensional space and hence norm compact. The inclusion into \(B(H)\) is norm-to-strong continuous, so its image \(U(N)\) is strongly compact in every faithful representation. This proves (PF.169).

PF44's tail-corner argument now uses this direct theorem. A compact strong identity neighborhood in an infinite-dimensional factor would contain a closed copy of the unitary group of an infinite-dimensional corner; that group would be compact, contradicting (PF.169). The proof of this implication no longer needs a decomposition into irreducible compact-group representations. The decomposition of compact-group representations remains an alternative route. The Haar existence input remains precisely the programme theorem named above.

### Solved example: a matrix average

Take \(N=M_2(\mathbb C)\) on \(\mathbb C^2\), \(\xi=(1,0)\), and normalized Haar probability on \(U(2)\). The operator \(T\) commutes with every unitary matrix. Commuting with diagonal phase matrices first makes it diagonal; commuting with the coordinate swap makes its two diagonal entries equal. Also its trace is one, because trace is a continuous linear functional here and every \(P_{u\xi}\) has trace one. Therefore

\[
T=\frac12 I_2.
\tag{PF.176}
\]

The same value is obtained by the explicit four-term average of \(P_\xi\) conjugated by \(I,X,Z,XZ\), where
\(X=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) and
\(Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\).
Two conjugates are \(\operatorname{diag}(1,0)\) and two are \(\operatorname{diag}(0,1)\). Here \(E=\mathbb C^2\), \(c=1/2\), and compression is the original faithful representation.

### Solved example: why the factor hypothesis matters

Let \(D=\ell^\infty(\mathbb N)\) act diagonally on \(\ell^2(\mathbb N)\). Its unitary group consists of all sequences \(z=(z_n)\) with \(|z_n|=1\). The strong operator topology is exactly the product topology on \(\mathbb T^{\mathbb N}\). Strong convergence implies coordinate convergence by testing the standard basis. Conversely, for every \(\eta\in\ell^2\), put \(b_r=\sum_{n\le r}|z_n-w_n|^2|\eta_n|^2\) and \(t_r=\sum_{n>r}|\eta_n|^2\). The bound \(|z_n-w_n|\le2\) gives

\[
\begin{gathered}
\|(z-w)\eta\|^2\\
\le b_r+4t_r.
\end{gathered}
\tag{PF.177}
\]

First make the tail small, then control the finitely many coordinates. The argument handles nets as well as sequences.

The countable product of circles is compact and Polish. One explicit compatible metric is
\(d(z,w)=\sum_{n\ge1}2^{-n}|z_n-w_n|\).
It is complete because Cauchy sequences converge in every circle coordinate and the uniformly bounded tail controls the metric limit. It is totally bounded by a finite cover of finitely many coordinates and the same tail bound. Thus it is compact; sequences with finitely many coordinates chosen from countable dense circle subsets give separability. Haar probability on this compact group is a nonzero finite Borel measure invariant under every left translation.

In this example \(\xi=e_1\) has \(P_{u\xi}=P_{e_1}\) for every diagonal unitary, so \(T=P_{e_1}\), \(E=\mathbb Ce_1\), and

\[
\begin{gathered}
\pi_E:D\longrightarrow\mathbb C,\\
\pi_E((a_n))=a_1.
\end{gathered}
\tag{PF.178}
\]

Its kernel is the nonzero central ideal of sequences with \(a_1=0\). Compactness has produced a finite-dimensional normal representation, but that representation is not faithful. This pinpoints the factor step in (PF.175). Infinite dimension alone does not exclude a compact strong unitary group or an invariant finite Borel measure on it.
