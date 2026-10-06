# The predual-valued map of a normal weight

**Self-checked by the writing AI.**

Fixing a normal weight produces more than its GNS representation. Every finite-domain element determines a normal functional on the GNS commutant, and these functionals assemble into a completely positive map. This unit constructs that map, computes its exact norm on self-adjoint elements, and proves the two bounded sequential graph statements needed in the normal-weight argument. The algebra and Hilbert space may be nonseparable; the weight need not be faithful, semifinite, or finite.

The freely accessible comparison for the construction, norm and sequential arguments is Brent Nelson, [*Tomita–Takesaki Theory*, Lemmas 3.8–3.10, pages 22–24](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf). The trace example is reconstructed below from bounded operators and square-summable coordinates, with Jesse Peterson, [*Notes on von Neumann algebras*, §§2.1–2.2, pages 19–23](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf), as a free comparison. The norm proof below repairs the finite-domain problem recorded in Problems with complete solutions: it never infers that \(|h|^{1/2}\) is a finite-energy vector from \(h=h^*\in\mathfrak m_\varphi\). The current reconstruction and added proofs are by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0; earlier exposition and provider licences are retained. References supply comparison material, not substitutes for proofs.

Exact inputs are WG003–006 for the finite domain and GNS construction, WF06 for the full support-factorization lemma, BK01–08 for bounded calculus, adjoints, monotone limits and polar decomposition, and CP06–08 for concrete preduals and the sigma-strong topology. The real sublinear Hahn–Banach proof is NP1. The trace model also uses OW09 for arbitrary-coordinate square-sum completeness and HE05 for the tensor and orthonormal-coordinate construction.

## Domains, predual, and target formula

Let \(M\) be a von Neumann algebra and let \(\varphi:M_+\to[0,\infty]\) be a normal weight. Use the finite domains and GNS construction of OA-MOD-WG:

\[
\mathfrak n_\varphi
=\{x\in M:\varphi(x^*x)<\infty\},
\]

\[
\mathfrak m_\varphi
=\operatorname{span}\{y^*x:x,y\in\mathfrak n_\varphi\}.
\]

\[
\begin{aligned}
\langle\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
&=\varphi(y^*x),\\
\pi_\varphi(a)\Lambda_\varphi(x)
&=\Lambda_\varphi(ax).
\end{aligned}
\tag{PV.1}
\]

Inner products are linear in the first variable. On complex elements of the finite algebra, the weight notation means its finite linear extension from WG004; no extended-real subtraction is involved. Put

\[
N=\pi_\varphi(M)'.
\]

Its concrete predual \(N_*\) contains every vector functional, defined for \(T\in N\) by

\[
\omega_{\xi,\eta}(T)
=\langle T\xi,\eta\rangle,
\tag{PV.2}
\]

and \(\|\omega_{\xi,\eta}\|\leq\|\xi\|\,\|\eta\|\). We will construct one linear map

\[
\Theta_\varphi:\mathfrak m_\varphi\longrightarrow N_*
\tag{PV.3}
\]

characterized, for \(x,y\in\mathfrak n_\varphi\) and \(T\in N\), by the following formula. Write \(\xi_x=\Lambda_\varphi(x)\) and \(\xi_y=\Lambda_\varphi(y)\).

\[
\Theta_\varphi(y^*x)(T)
=\langle T\xi_x,\xi_y\rangle.
\tag{PV.4}
\]

The issue is not the right side for one chosen factorization. An element of \(\mathfrak m_\varphi\) has many product decompositions, so well-definedness and linearity have to be proved before (PV.4) can be used as a definition.

## Construction on the positive cone

For \(c\in\mathfrak m_\varphi^+\), define

\[
\Theta_\varphi(c)
=\omega_{\Lambda_\varphi(c^{1/2}),\Lambda_\varphi(c^{1/2})}|_N.
\tag{PV.5}
\]

This is a positive member of \(N_*\). We prove that the prescription is additive. Given \(c,e\in\mathfrak m_\varphi^+\), set \(d=c+e\) and \(p=s(d)\). The two-term case of WF06(ii), consistent with the factorization in OA-MOD-DW-02, supplies contractions \(v,w\in M\) such that

\[
\begin{aligned}
c^{1/2}&=vd^{1/2},\\
e^{1/2}&=wd^{1/2},\\
v^*v+w^*w&=p.
\end{aligned}
\tag{PV.6}
\]

Let \(\zeta=\Lambda_\varphi(d^{1/2})\), \(V=\pi_\varphi(v)\), and \(W=\pi_\varphi(w)\). Then \(\pi_\varphi(p)\zeta=\zeta\) and \(Q=V^*V+W^*W=\pi_\varphi(p)\). In the next calculation abbreviate \(\Theta_\varphi\) to \(\Theta\), and denote \(\Theta(c)(T)+\Theta(e)(T)\) by \(S_T\). If \(T\in N\), commutation with \(\pi_\varphi(M)\) gives

\[
\begin{aligned}
S_T
&=\langle TV\zeta,V\zeta\rangle\\
&\quad+\langle TW\zeta,W\zeta\rangle\\
&=\langle TQ\zeta,\zeta\rangle\\
&=\langle T\zeta,\zeta\rangle\\
&=\Theta(d)(T).
\end{aligned}
\tag{PV.7}
\]

Positive homogeneity follows directly from square roots, including the zero scalar. Each square root lies in the GNS domain because the original positive element has finite weight. Since \(\mathfrak m_\varphi^+\) generates the self-adjoint part of \(\mathfrak m_\varphi\), the additive homogeneous map has a unique real-linear extension there and then a unique complex-linear extension to \(\mathfrak m_\varphi\). For the extension step, if \(a-b=c-d\) with all four elements finite and positive, then \(a+d=c+b\). The established additivity gives equality of the two differences of their predual functionals. Addition and real scaling of decompositions prove real linearity; the unique real and imaginary self-adjoint parts then give complex linearity, as in WF03. All operations stay in the vector space \(N_*\). Positivity and the proved norm formula for positive functionals in CP07 give the useful identity

\[
\begin{aligned}
\|\Theta_\varphi(c)\|
&=\Theta_\varphi(c)(1)\\
&=\|\Lambda_\varphi(c^{1/2})\|^2\\
&=\varphi(c).
\end{aligned}
\tag{PV.8}
\]

It remains to identify the extension. If \(x=u|x|\) is the polar decomposition of \(x\in\mathfrak n_\varphi\), then \(u^*u\) fixes \(|x|\), and every \(T\in N_+\) commutes with \(\pi_\varphi(u)\). Put \(\xi=\Lambda_\varphi(x)\). Consequently

\[
\Theta_\varphi(x^*x)(T)
=\langle T\xi,\xi\rangle.
\tag{PV.9}
\]

To spell out (PV.9), put \(q=u^*u\) and \(\eta=\Lambda_\varphi(|x|)\). Then \(\pi_\varphi(q)\eta=\eta\) and \(\xi=\pi_\varphi(u)\eta\). Moving the adjoint across the pairing and commuting \(T\) with the representation gives

\[
 \begin{aligned}
 \langle T\xi,\xi\rangle
 &=\langle\pi_\varphi(u)^*T\pi_\varphi(u)\eta,\eta\rangle\\
 &=\langle T\eta,\eta\rangle.
 \end{aligned}
\]

The equality uses only \(|x|^2=x^*x\), whose weight is finite. Polarization gives (PV.4) first for \(T\geq0\). Every element of \(N\) is a linear combination of positive elements, by taking real and imaginary self-adjoint parts and their positive and negative parts with BK01, so (PV.4) holds for arbitrary \(T\). Products \(y^*x\) span the domain, proving uniqueness.

## Complete positivity

We use the inherited matrix-positive cones on \(M_n(\mathfrak m_\varphi)\). The target convention and its test can be proved explicitly. For \(F=[f_{ij}]\), \(f_{ij}\in N_*\), associate the functional

\[
 \widehat F([T_{ij}])=\sum_{i,j}f_{ij}(T_{ij})
 \quad\text{on }M_n(N).
\]

Entry extraction is ultraweakly continuous: a vector-series test of one entry is the same test on the direct sum Hilbert space with the two vectors in the chosen coordinate positions. The finite sum above is therefore normal. We say \(F\) is positive when this functional is positive; this specifies the matrix-predual convention used here. Positivity is equivalent to

\[
 \sum_{i,j}f_{ij}(a_i^*a_j)\geq0
 \quad(a_1,\ldots,a_n\in N).
\]

Necessity tests a positive Gram matrix. For sufficiency, take the positive square root \(C\) of any positive matrix \(T\in M_n(N)\). It exists by BK01 on the finite direct sum Hilbert space, and its entries belong to \(N\) by polynomial approximation. Since \(T_{ij}=\sum_k C_{ki}^*C_{kj}\), sum the assumed inequalities over the finitely many rows. The finite operator matrix algebra is norm closed: norm convergence gives convergence of each entry, and conversely the sum of entry norms bounds the matrix operator norm. Thus the required calculus applies without a separate matrix-algebra existence theorem. For \(x_1,\ldots,x_n\in\mathfrak n_\varphi\), the matrix

\[
\big[\Theta_\varphi(x_i^*x_j)\big]_{i,j}
\tag{PV.10}
\]

is positive in \(M_n(N_*)\). Indeed, the matrix-predual positivity test reduces to arbitrary \(a_1,\ldots,a_n\in N\). Put \(\xi_j=\Lambda_\varphi(x_j)\), and let \(S\) denote the scalar obtained by testing (PV.10) against the Gram matrix \([a_i^*a_j]\). Formula (PV.4) gives

\[
\begin{aligned}
S
&=\sum_{i,j=1}^n
  \langle a_j\xi_j,a_i\xi_i\rangle\\
&=\left\|\sum_{j=1}^n a_j\xi_j\right\|^2\\
&\geq0.
\end{aligned}
\tag{PV.11}
\]

Now let \(H=[h_{ij}]\in M_n(\mathfrak m_\varphi)\) be positive in \(M_n(M)\), and write its positive square root as \(X=[x_{ki}]\). For every \(i\),

\[
h_{ii}=\sum_k x_{ki}^*x_{ki}\in\mathfrak m_\varphi^+.
\]

Hence each \(x_{ki}\) belongs to \(\mathfrak n_\varphi\), and

\[
h_{ij}=\sum_k x_{ki}^*x_{kj}.
\tag{PV.12}
\]

The amplified image \([\Theta_\varphi(h_{ij})]\) is therefore a finite sum of the positive matrices in (PV.10). Thus every amplification of \(\Theta_\varphi\) is positive: \(\Theta_\varphi\) is completely positive. This proves the full predual-valued assertion, rather than only the scalar correspondence of OA-MOD-DW-03.

## The repaired self-adjoint norm formula

For \(h=h^*\in\mathfrak m_\varphi\), put

\[
\begin{aligned}
p_\varphi(h)=\inf\{&\varphi(a)+\varphi(b):\\
                    &h=a-b,\\
                    &a,b\in\mathfrak m_\varphi^+\}.
\end{aligned}
\tag{PV.13}
\]

**Theorem.** For every such \(h\),

\[
\|\Theta_\varphi(h)\|=p_\varphi(h).
\tag{PV.14}
\]

**Proof.** The finite positive cone generates \(\mathfrak m_{\varphi,\mathrm{sa}}\), so the infimum is over a nonempty set. Addition of decompositions and interchange of their two terms show that \(p_\varphi\) is a seminorm. For \(a\in\mathfrak m_\varphi^+\), linearity of the finite extension of \(\varphi\) gives

\[
p_\varphi(a)=\varphi(a).
\tag{PV.15}
\]

Indeed, \(a=a-0\) gives one inequality, while \(a=c-d\) with \(c,d\geq0\) gives \(\varphi(a)=\varphi(c)-\varphi(d)\leq\varphi(c)+\varphi(d)\). Therefore (PV.8) and the triangle inequality imply

\[
\|\Theta_\varphi(h)\|\leq p_\varphi(h).
\tag{PV.16}
\]

Fix \(h_0=h_0^*\). The full real sublinear Hahn–Banach proof in NP1, applied to the seminorm \(p_\varphi\), gives a real-linear \(f\) on \(\mathfrak m_{\varphi,\mathrm{sa}}\) such that

\[
\begin{aligned}
f(h_0)&=p_\varphi(h_0),\\
|f(h)|&\leq p_\varphi(h).
\end{aligned}
\tag{PV.17}
\]

When \(p_\varphi(h_0)=0\), the required reverse inequality is immediate; otherwise the functional starts on \(\mathbb Rh_0\) and is extended. Complexify it to a self-adjoint linear functional, still denoted \(f\), on \(\mathfrak m_\varphi\). For \(x\in\mathfrak n_\varphi\),

\[
\begin{aligned}
|f(x^*x)|
&\leq p_\varphi(x^*x)\\
&=\varphi(x^*x)\\
&=\|\Lambda_\varphi(x)\|^2.
\end{aligned}
\tag{PV.18}
\]

Thus

\[
B(\Lambda_\varphi(x),\Lambda_\varphi(y))=f(y^*x)
\tag{PV.19}
\]

is well defined and extends to a bounded Hermitian form on \(H_\varphi\). Here are the quotient and norm details. Before taking the quotient, let \(G(x,y)=\varphi(y^*x)\) and \(F(x,y)=f(y^*x)\). The forms \(G+F\) and \(G-F\) are positive by (PV.18). The scalar Cauchy–Schwarz proof in WG005 applies to any positive semidefinite form. If \(G(x,x)=0\), then both of these forms have zero diagonal at \(x\), hence vanish when paired with any \(y\). Thus \(F(x,y)=F(y,x)=0\), proving independence of the representatives. Their diagonal bounds by \(2G\) give

\[
 |F(x,y)|\leq2\|\Lambda_\varphi(x)\|\,
                    \|\Lambda_\varphi(y)\|.
\]

So the quotient form is bounded and extends by density. BK01 represents it by a bounded self-adjoint operator; the diagonal bound (PV.18) extends to all vectors and says that both the identity plus this operator and the identity minus this operator are positive. The self-adjoint calculus in BK01 then places its spectrum in \([-1,1]\), giving norm at most one. We have therefore obtained a self-adjoint contraction \(A\) with

\[
B(\xi,\eta)=\langle A\xi,\eta\rangle.
\tag{PV.20}
\]

For \(z\in M\) and \(x,y\in\mathfrak n_\varphi\), put \(Z=\pi_\varphi(z)\), \(\xi=\Lambda_\varphi(x)\), and \(\eta=\Lambda_\varphi(y)\). Then

\[
\begin{aligned}
\langle AZ\xi,\eta\rangle
&=f(y^*zx)\\
&=\langle ZA\xi,\eta\rangle.
\end{aligned}
\tag{PV.21}
\]

Density gives \(A\in N\). Formula (PV.4) now says, for every \(h\in\mathfrak m_\varphi\),

\[
f(h)=\Theta_\varphi(h)(A).
\tag{PV.22}
\]

Since \(\|A\|\leq1\),

\[
\begin{aligned}
p_\varphi(h_0)
&=f(h_0)\\
&\leq\|\Theta_\varphi(h_0)\|.
\end{aligned}
\tag{PV.23}
\]

Together with (PV.16), this proves (PV.14). \(\square\)

The argument pairs the Hahn–Banach functional directly with \(\Theta_\varphi(h_0)\). It never takes the square root of \(|h_0|\), which need not have finite weight.

## A bounded positive limit stays in the finite cone

We first record the regulator used in both graph arguments. For \(\alpha>0\) and \(t>-\alpha^{-1}\), put \(s_\alpha(t)=(1+\alpha t)^{-1}\) and set

\[
\begin{aligned}
r_\alpha(t)
&=\frac{t}{1+\alpha t}\\
&=\alpha^{-1}(1-s_\alpha(t)).
\end{aligned}
\tag{PV.24}
\]

Inverse order makes \(s_\alpha\) operator antitone, so \(r_\alpha\) is operator monotone on this interval. On \([0,\infty)\),

\[
\begin{aligned}
0&\leq r_\alpha(t)\leq t,\\
r_\alpha(t)&\leq\alpha^{-1},\\
r_\alpha(t)&\uparrow t\quad(\alpha\downarrow0).
\end{aligned}
\tag{PV.25}
\]

On a common bounded spectral interval, bounded sigma-strong convergence passes through \(r_\alpha\). To verify the precise instance needed here, suppose the self-adjoint operators \(z_i,z\) lie in a common interval on which \(1+\alpha t\geq\delta>0\), and \(z_i\to z\) sigma-strongly. Their inverse norms are at most \(\delta^{-1}\) by BK01. The inverse identity gives

\[
 \begin{aligned}
 r_\alpha(z_i)-r_\alpha(z)
 &=s_\alpha(z_i)(z_i-z)s_\alpha(z).
 \end{aligned}
\]

Its rightmost factor is fixed, and its leftmost factors are uniformly bounded, so the right side tends strongly to zero on each vector. The common spectral interval gives a common bound on the regulators themselves. CP08 upgrades this bounded strong convergence to sigma-strong convergence. For a fixed positive \(z\), scalar calculus also gives \(\|z-r_\alpha(z)\|\leq\alpha\|z\|^2\), proving the stated increasing convergence to \(z\).

**Theorem.** Let \((x_n)\subseteq\mathfrak m_\varphi^+\) be bounded in operator norm. If \(x_n\to x\) sigma-strongly and \(\Theta_\varphi(x_n)\) converges in \(N_*\)-norm, then \(x\in\mathfrak m_\varphi^+\).

**Proof.** The sigma-strong limit is positive. Fix \(\varepsilon>0\), and pass to a subsequence \((y_n)\) such that

\[
\|\Theta_\varphi(y_{n+1}-y_n)\|<\varepsilon 2^{-n}.
\tag{PV.26}
\]

The strict gap in (PV.26) and the definition of the infimum in the norm formula give \(a_n,b_n\in\mathfrak m_\varphi^+\) with

\[
\begin{aligned}
y_{n+1}-y_n&=a_n-b_n,\\
\varphi(a_n)+\varphi(b_n)&<\varepsilon 2^{-n}.
\end{aligned}
\tag{PV.27}
\]

In particular,

\[
y_{n+1}\leq y_1+\sum_{k=1}^n a_k=:A_n.
\tag{PV.28}
\]

For fixed \(\alpha>0\), the sequence \(r_\alpha(A_n)\) is increasing and bounded above by \(\alpha^{-1}1\). Let its sigma-strong supremum be \(c_\alpha\). Functional-calculus continuity in (PV.28) and \(y_n\to x\) give

\[
r_\alpha(x)\leq c_\alpha.
\tag{PV.29}
\]

Normality of \(\varphi\), followed by (PV.25), yields the next estimate. Here
\(s_a=\sum_{k\geq1}\varphi(a_k)<\varepsilon\).

\[
\begin{aligned}
\varphi(r_\alpha(x))
&\leq\varphi(c_\alpha)\\
&=\sup_n\varphi(r_\alpha(A_n))\\
&\leq\sup_n\varphi(A_n)\\
&=\varphi(y_1)+s_a\\
&<\varphi(y_1)+\varepsilon.
\end{aligned}
\tag{PV.30}
\]

Finally \(r_\alpha(x)\uparrow x\) as \(\alpha\downarrow0\). A second use of normality proves

\[
\varphi(x)\leq\varphi(y_1)+\varepsilon<\infty.
\]

Thus \(x\in\mathfrak m_\varphi^+\). \(\square\)

## A norm-convergent image of a strong-null sequence is zero

**Theorem.** Let \((x_n)\subseteq\mathfrak m_\varphi^+\) be bounded in operator norm. If \(x_n\to0\) sigma-strongly and \(\Theta_\varphi(x_n)\) converges in \(N_*\)-norm, write

\[
\Theta_\varphi(x_n)\longrightarrow\Psi,
\tag{PV.31}
\]

then \(\Psi=0\).

**Proof.** Fix \(\varepsilon>0\). Choose a subsequence \((y_n)\) satisfying both

\[
\|\Psi-\Theta_\varphi(y_n)\|<\varepsilon 2^{-n-1}
\tag{PV.32}
\]

and decompositions as in (PV.27). Indeed choose increasing subsequence indices satisfying (PV.32); norm convergence permits this recursively. The triangle inequality makes the norm of each successive image difference less than \(3\varepsilon2^{-n-2}<\varepsilon2^{-n}\), leaving the strict room required to choose (PV.27). Then

\[
y_1-y_{n+1}\leq\sum_{k=1}^n b_k=:B_n.
\tag{PV.33}
\]

Put \(K=\sup_n\|y_n\|\). The case \(K=0\) is immediate. Otherwise choose \(0<\alpha<K^{-1}\). Since

\[
-K1\leq y_1-y_{n+1}\leq K1,
\]

both sides of the next comparison lie in the domain of the operator-monotone regulator:

\[
r_\alpha(y_1-y_{n+1})\leq r_\alpha(B_n).
\tag{PV.34}
\]

The right side increases to a bounded positive operator \(d_\alpha\). The left side converges sigma-strongly to \(r_\alpha(y_1)\), so

\[
r_\alpha(y_1)\leq d_\alpha.
\tag{PV.35}
\]

Normality and (PV.25) give

\[
\begin{aligned}
\varphi(r_\alpha(y_1))
&\leq\varphi(d_\alpha)\\
&=\sup_n\varphi(r_\alpha(B_n))\\
&\leq\sup_n\varphi(B_n)\\
&=\sum_{k\geq1}\varphi(b_k)\\
&<\varepsilon.
\end{aligned}
\tag{PV.36}
\]

Letting \(\alpha\downarrow0\) shows \(\varphi(y_1)\leq\varepsilon\). By (PV.8) and (PV.32),

\[
\begin{aligned}
\|\Psi\|
&\leq\|\Psi-\Theta_\varphi(y_1)\|\\
&\quad+\|\Theta_\varphi(y_1)\|\\
&<\frac{\varepsilon}{4}+\varepsilon.
\end{aligned}
\tag{PV.37}
\]

The choice of \(\varepsilon\) was arbitrary, hence \(\Psi=0\). \(\square\)

The operator-norm boundedness in PV-05–06 fixes a common spectral interval for the sigma-strong functional-calculus limits. No sequence is substituted for an arbitrary net in the definition of a normal weight.

## Trace model, necessity of norm convergence, and scope

Let \(M=B(K)\) for an arbitrary Hilbert space and let \(\varphi=\operatorname{Tr}\) be the usual faithful normal semifinite trace. The GNS space is the Hilbert–Schmidt class \(S_2(K)\), \(\pi_\varphi\) acts by left multiplication, and its commutant acts by right multiplication \(R_b(X)=Xb\). The finite algebra is \(S_1(K)\). For \(h\in S_1(K)\) and \(b\in B(K)\), (PV.4) gives

\[
\Theta_\varphi(h)(R_b)
=\operatorname{Tr}(hb).
\tag{PV.38}
\]

Thus PV-04 becomes the familiar self-adjoint trace-norm formula. If

\[
\mathcal D_h
=\{(a,b)\in S_1(K)_+^2:h=a-b\},
\]

then

\[
\begin{aligned}
\|h\|_1
&=\inf_{(a,b)\in\mathcal D_h}\\
&\qquad\bigl(\operatorname{Tr}(a)+\operatorname{Tr}(b)\bigr).
\end{aligned}
\tag{PV.39}
\]

If \((e_n)\) is an orthonormal sequence and \(p_n\) is the projection onto \(\mathbb Ce_n\), then \(p_n\to0\) strongly while \(\varphi(p_n)=1\). Put \(F_n=\Theta_\varphi(p_n)\). Then

\[
\begin{aligned}
\|F_n-F_m\|
&=\|p_n-p_m\|_1\\
&=2\quad(n\ne m).
\end{aligned}
\tag{PV.40}
\]

This example shows why strong convergence alone cannot replace the predual-norm convergence in PV-06.

**Proof of the arbitrary-Hilbert-space trace model.** Fix an orthonormal basis \((e_j)_{j\in J}\). All nonnegative sums below mean suprema over finite subsets; exchanging two such sums is valid because both iterated suprema equal the supremum over finite subsets of the product index set. The coordinate and completeness proofs in HE05 and OW09 apply without countability of \(J\). The zero Hilbert space has only zero operators and satisfies every assertion directly.

For \(a\geq0\), define its trace by \(\sum_j\langle ae_j,e_j\rangle\). If \((f_k)\) is another orthonormal basis, Parseval for \(a^{1/2}\) in the two bases gives

\[
 \begin{aligned}
 \sum_j\|a^{1/2}e_j\|^2
 &=\sum_{j,k}|\langle a^{1/2}e_j,f_k\rangle|^2\\
 &=\sum_k\|a^{1/2}f_k\|^2.
 \end{aligned}
\]

Here the second equality uses self-adjointness of the square root. This proves basis independence. The same coefficient calculation for any bounded \(X\) proves

\[
 \begin{aligned}
 \operatorname{Tr}(X^*X)
 &=\sum_{i,j}|\langle Xe_j,e_i\rangle|^2\\
 &=\operatorname{Tr}(XX^*).
 \end{aligned}
\]

Finite sums and homogeneity prove the weight axioms. For an increasing bounded positive net, interchange its supremum with the finite-coordinate supremum; BK04 identifies each diagonal limit. Thus this weight is normal. A zero trace forces every \(a^{1/2}e_j=0\), hence \(a=0\), proving faithfulness. Finite-coordinate projections have finite trace and increase strongly to the identity, so WG008 proves semifiniteness.

Let \(S_2(K)\) consist of bounded \(X\) with \(\|X\|_2^2=\operatorname{Tr}(X^*X)<\infty\). The coefficient map identifies this space with the full square-sum space on \(J\times J\). For completeness of this claim, a square-summable array \((c_{ij})\) defines a bounded operator on finite-support vectors: Cauchy–Schwarz gives

\[
 \begin{aligned}
 &\sum_i\left|\sum_jc_{ij}v_j\right|^2\\
 &\quad\leq\left(\sum_{i,j}|c_{ij}|^2\right)
           \sum_j|v_j|^2.
 \end{aligned}
\]

Extend it by density using BK01. Its matrix coefficients are exactly the prescribed array, giving surjectivity. OW09 supplies completeness and density of finite arrays. Consequently the matrix units form an orthonormal basis for \(S_2(K)\), finite-rank operators are dense, and \(\|X\|\leq\|X\|_2\). The coefficient formulas also show that adjoint is an isometry of this space. The order inequality \((aX)^*(aX)\leq\|a\|^2X^*X\) gives the left multiplication bound; applying it to adjoints gives the right multiplication bound

\[
 \|aXb\|_2\leq\|a\|\,\|X\|_2\,\|b\|.
\]

The GNS domain is exactly \(S_2(K)\), its null ideal is zero, and the inner product is the coefficient inner product by polarization. Thus its completion is this same Hilbert space and its representation is left multiplication.

Right multiplication has adjoint \(R_b^*=R_{b^*}\). Check the pairing on two rank-one operators by their matrix coefficients, where it is a finite-rank computation, then extend by the preceding bounds and density. The bound \(\|R_b\|\leq\|b\|\) is sharp: for a unit vector \(u\) and \(X(\zeta)=\langle\zeta,v\rangle u\), one has \(\|X\|_2=\|v\|\) and \(\|Xb\|_2=\|b^*v\|\). Taking the supremum over unit \(v\) gives equality.

To identify the entire commutant, let \(T\) commute with all left multiplications and choose one basis vector \(e_{i_0}\). The projection of left multiplication by its rank-one projection picks out the closed space of operators with range in \(\mathbb C e_{i_0}\). Identifying that space with \(\overline K\) by \(v\mapsto(\zeta\mapsto\langle\zeta,v\rangle e_{i_0})\), the restriction of \(T\) is an arbitrary bounded operator on \(\overline K\). It has the form \(\overline v\mapsto\overline{b^*v}\) for a unique bounded \(b\) on \(K\), by conjugating to \(K\) and taking the bounded adjoint. Commutation with the left matrix unit carrying \(e_{i_0}\) to \(e_i\) gives the same right action on every row. Finite arrays are dense, so \(T=R_b\) everywhere. Conversely each right multiplication commutes with every left multiplication. This proves the asserted commutant description for arbitrary dimension.

Define \(S_1(K)=\{h:\operatorname{Tr}|h|<\infty\}\), with \(|h|=(h^*h)^{1/2}\) and \(\|h\|_1=\operatorname{Tr}|h|\). We next prove that it is exactly the finite algebra, without assuming it is already a linear space. Let \(h=\sum_{k=1}^mY_k^*X_k\) with \(X_k,Y_k\in S_2(K)\), and take its bounded polar decomposition \(h=u|h|\). For each basis vector, \(\langle|h|e_j,e_j\rangle=\langle he_j,ue_j\rangle\). Summing absolute values of the expanded right side and applying Cauchy–Schwarz to the coordinate families yields

\[
 \begin{aligned}
 \operatorname{Tr}|h|
 &\leq\sum_{k=1}^m\|X_k\|_2\|Y_ku\|_2\\
 &\leq\sum_{k=1}^m\|X_k\|_2\|Y_k\|_2<\infty.
 \end{aligned}
\]

Conversely, if \(h\in S_1(K)\), set \(t=|h|^{1/2}\). Then \(t\in S_2(K)\) and \(t u^*\in S_2(K)\), while \(h=(t u^*)^*t\). Thus \(S_1(K)=\mathfrak m_{\operatorname{Tr}}\), so its linear and star-algebra properties follow from WG003.

For a product \(h=Y^*X\), the diagonal series \(\sum_j\langle he_j,e_j\rangle\) is absolutely convergent, bounded in absolute value by \(\|X\|_2\|Y\|_2\). The same holds for finite sums of products. It defines a linear functional on \(S_1(K)\) agreeing with the original trace on positive elements. The uniqueness of the finite extension in WG004 proves that it is basis independent. In particular its value at \(Y^*X\) is the Hilbert–Schmidt pairing \(\langle X,Y\rangle_2\).

Now \(h b=Y^*(Xb)\) is again in \(S_1(K)\), and

\[
 \begin{aligned}
 \Theta_{\operatorname{Tr}}(h)(R_b)
 &=\langle Xb,Y\rangle_2\\
 &=\operatorname{Tr}(h b).
 \end{aligned}
\]

Linear combinations give (PV.38) on the whole domain. To compute its norm, take the balanced factorization \(h=(t u^*)^*t\) above. The identity for the traces of \(X^*X\) and \(XX^*\), applied to \(u t\), gives

\[
 \|t u^*\|_2^2=\|t\|_2^2=\operatorname{Tr}|h|.
\]

It follows that \(|\operatorname{Tr}(hb)|\leq\|b\|\operatorname{Tr}|h|\). For the reverse bound, choose \(b=u^*\), a contraction. Then \(hu^*=u|h|u^*\) is positive and the same trace identity gives \(\operatorname{Tr}(hu^*)=\operatorname{Tr}|h|\). Since every commutant operator is one of the \(R_b\) and has norm \(\|b\|\), we have proved \(\|\Theta_{\operatorname{Tr}}(h)\|=\|h\|_1\). This is a norm: definiteness follows from faithfulness and \(|h|=0\Rightarrow h=0\), and the other norm axioms follow from the functional norm. Applying PV04 proves (PV.39).

Finally, for any orthonormal sequence, \(\|p_n\xi\|^2=|\langle\xi,e_n\rangle|^2\to0\), since these nonnegative coefficients have bounded finite sums. Hence the projections are strongly null and, by CP08 and their norm bound, sigma-strongly null. For distinct indices, \((p_n-p_m)^2=p_n+p_m\), so uniqueness of positive square roots gives \(|p_n-p_m|=p_n+p_m\). Its trace is two. The proved norm identification now gives (PV.40), including the failure of image-norm convergence.

The trace model, including its full commutant and norm, is proved above. The unit proves exactly the predual-valued map, its complete positivity, the repaired self-adjoint norm formula, and the two bounded sequential conclusions. It does not assert that \(\Theta_\varphi\) is operator-norm bounded on \(\mathfrak m_\varphi\), that the finite algebra is closed under absolute values, or that these sequential statements replace the arbitrary-net definition of normality.
