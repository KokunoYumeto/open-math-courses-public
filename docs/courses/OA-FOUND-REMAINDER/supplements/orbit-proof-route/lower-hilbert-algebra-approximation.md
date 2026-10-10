<span id="approximating-multiplication-without-losing-its-bound"></span>
# Approximating multiplication without losing its bound

<span id="oa-mod-hap-01--spaces-topologies-and-prerequisites"></span>
<span id="OA-MOD-HAP-01"></span>
<span id="oa-mod-hap-01"></span>
## OA-MOD-HAP-01 — Spaces, topologies and prerequisites

Let \(\mathcal A\subseteq H\) be an arbitrary left Hilbert algebra. Inner products are linear in the first variable. Retain the constructions of HA, RD and WH:
\[
M=L(\mathcal A)'',\qquad S=\overline{\sharp},\qquad F=S^*,
\]
\[
\mathcal A_r=\mathcal B_r\cap D(F),\qquad
\mathcal A_l=\mathcal B_l\cap D(S).
\tag{HAP.1}
\]
Here \(\mathcal A_l\) is the full left completion, and \(\lambda_\xi\in M\) is left multiplication for \(\xi\in\mathcal B_l\). The original algebra embeds in \(\mathcal A_l\), with \(\lambda_a=L_a\). The defining identities include
\[
\lambda_\xi\eta=R_\eta\xi
\quad(\xi\in\mathcal B_l,\ \eta\in\mathcal B_r),
\qquad
\lambda_{S\xi}=\lambda_\xi^*
\quad(\xi\in\mathcal A_l).
\tag{HAP.2}
\]
Both multiplication assignments are injective. Their ranges
\[
\mathfrak n_l=\lambda(\mathcal B_l)\subseteq M,\qquad
\mathfrak n_r=R(\mathcal B_r)\subseteq M'
\]
are left ideals, with covariance
\[
\lambda_{x\xi}=x\lambda_\xi,\qquad
R_{y\eta}=yR_\eta
\quad(x\in M,\ y\in M'),
\tag{HAP.3}
\]
and
\[
\lambda(\mathcal A_l)=\mathfrak n_l\cap\mathfrak n_l^*,
\qquad R(\mathcal A_r)=\mathfrak n_r\cap\mathfrak n_r^*.
\tag{HAP.4}
\]
The spaces \(\mathcal A\) and \(\mathcal A_l\) are graph cores for \(S\), and \(\mathcal A_r\) is a graph core for \(F\).

Strong convergence of bounded operators means convergence on each vector; strong* convergence additionally requires convergence of the adjoints. Neither assertion about an arbitrary net supplies a uniform operator-norm bound unless one is proved. Sigma-strong convergence uses square-summable vector families as tests; sigma-strong* includes the adjoints. These topologies imply their corresponding strong topologies.

The exact prerequisites are HA-02–05, RD-04–07 and WH-03–04 for these domains and multiplication identities; BK for bounded continuous functional calculus, polar decomposition and bicommutants; real Hahn–Banach extension and locally convex separation in [Hahn–Banach, Baire and the basic theorems on Banach spaces](../../../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html); and the Hilbert Riesz theorem. HAP-03 and HAP-06 use the arbitrary-net common-core convergence theorem SK-09: convergence of self-adjoint operators on a graph core for their self-adjoint limit implies strong convergence of every bounded continuous function of those operators. The approximating operators need not have uniformly bounded norms. For a bounded limit, any Hilbert-dense linear domain is a graph core.

Only HAP-08 uses the polar identities
\[
S=J\Delta^{1/2},\qquad
F=J\Delta^{-1/2},\qquad J^2=I,
\tag{HAP.5}
\]
including exact domains, from HA-04 and TC, together with their spectral prerequisites. No identification \(JMJ=M'\), modular automorphism theorem, faithful state or countability restriction is an input to this unit.

<span id="oa-mod-hap-02--closed-graphs-in-the-appropriate-ambient-spaces"></span>
<span id="OA-MOD-HAP-02"></span>
<span id="oa-mod-hap-02"></span>
## OA-MOD-HAP-02 — Closed graphs in the appropriate ambient spaces

**Proposition.** The graph
\[
\{(\xi,\lambda_\xi):\xi\in\mathcal B_l\}
\subseteq H\times M
\tag{HAP.6}
\]
is closed for Hilbert norm on \(H\) and the strong operator topology on \(M\). Consequently it is closed when the latter topology is replaced by the sigma-strong topology.

The graph of \(\lambda|_{\mathcal A_l}\) is closed in
\[
D(S)\times M
\tag{HAP.7}
\]
when \(D(S)\) has the topology induced by the Hilbert norm and \(M\) has the strong topology. In particular it is closed for that domain topology and the sigma-strong* topology in the range.

**Proof.** Suppose \(\xi_i\in\mathcal B_l\), \(\xi_i\to\xi\) in Hilbert norm, and \(\lambda_{\xi_i}\to x\in M\) strongly. For every \(\eta\in\mathcal A_r\),
\[
R_\eta\xi=\lim_i R_\eta\xi_i
=\lim_i\lambda_{\xi_i}\eta=x\eta.
\tag{HAP.8}
\]
Thus \(\|R_\eta\xi\|\leq\|x\|\|\eta\|\). This is exactly the criterion for \(\xi\in\mathcal B_l\), and it identifies \(\lambda_\xi=x\). This argument treats every convergent net, proving (HAP.6).

For (HAP.7), the limiting first coordinate is, by the specified ambient space, already in \(D(S)\). The first assertion puts it in \(\mathcal B_l\), hence in \(\mathcal A_l\). Alternatively the graph in (HAP.7) is the intersection of (HAP.6) with \(D(S)\times M\). Strengthening the operator topology preserves closedness. \(\square\)

The induced Hilbert topology on \(D(S)\) is not its graph-norm topology. Nor does this proposition assert that the \(\mathcal A_l\) graph is closed in \(H\times M\). A later example shows that even operator-norm convergence in the second coordinate does not justify that larger ambient space.

<span id="oa-mod-hap-03--two-quadratic-products-from-one-block-operator"></span>
<span id="OA-MOD-HAP-03"></span>
<span id="oa-mod-hap-03"></span>
## OA-MOD-HAP-03 — Two quadratic products from one block operator

**Lemma.** Let \((x_i)\) be a net of bounded operators on \(H\), and let \(x\in B(H)\). Suppose dense linear subspaces \(D_1,D_2\subseteq H\) satisfy
\[
x_i\xi\longrightarrow x\xi\quad(\xi\in D_1),\qquad
x_i^*\eta\longrightarrow x^*\eta\quad(\eta\in D_2).
\tag{HAP.9}
\]
For every bounded continuous \(f:[0,\infty)\to\mathbb C\),
\[
f(x_i^*x_i)\longrightarrow f(x^*x),\qquad
f(x_i x_i^*)\longrightarrow f(xx^*)
\quad\hbox{strongly}.
\tag{HAP.10}
\]
No bound on \(\sup_i\|x_i\|\) is assumed.

Each dense test set may be replaced by its complex linear span, because convergence in its half of (HAP.9) extends through finite linear combinations. The two subspaces may be different; no common dense intersection is required.

**Proof.** On \(H\oplus H\) form the bounded self-adjoint operators
\[
h_i=\begin{pmatrix}0&x_i^*\\x_i&0\end{pmatrix},
\qquad
h=\begin{pmatrix}0&x^*\\x&0\end{pmatrix}.
\tag{HAP.11}
\]
For \(\zeta=(\xi,\eta)\in D_1\oplus D_2\), the two limits in (HAP.9) give \(h_i\zeta\to h\zeta\). This product subspace is dense in \(H\oplus H\), hence is a graph core for the bounded operator \(h\). Apply SK-09 to the bounded continuous function \(g(t)=f(t^2)\). It gives \(g(h_i)\to g(h)\) strongly.

Since \(h_i^2=\operatorname{diag}(x_i^*x_i,x_i x_i^*)\), the composition and direct-sum properties of bounded functional calculus give
\[
g(h_i)=
\begin{pmatrix}f(x_i^*x_i)&0\\0&f(x_i x_i^*)\end{pmatrix}.
\]
Those properties also follow by uniformly approximating \(f\) by polynomials on an interval containing the spectrum of the individual \(h_i^2\); the interval may depend on \(i\). Testing the two coordinate subspaces proves (HAP.10). \(\square\)

Boundedness of \(f\) is essential. Knowing both first-order limits on a dense domain does not alone provide convergence of the unrestricted quadratic products.

<span id="oa-mod-hap-04--why-self-adjoint-weak-density-gives-strong-density"></span>
<span id="OA-MOD-HAP-04"></span>
<span id="oa-mod-hap-04"></span>
## OA-MOD-HAP-04 — Why self-adjoint weak density gives strong density

We need an approximation theorem for the original multiplication algebra, which need not contain an identity or be norm closed. We first prove its topological ingredient.

Let \(\mathcal C\subseteq B(K)\) be a nondegenerate *-subalgebra, and write \(N=\mathcal C''\). HA-03 gives
\[
\overline{\mathcal C}^{\,\mathrm{WOT}}
=\overline{\mathcal C}^{\,\mathrm{SOT}}=N.
\tag{HAP.12}
\]
Its proof uses nondegeneracy in place of a unit. In particular, it does not put an unproved bound on its approximants.

**Lemma.** The self-adjoint part \(\mathcal C_{\mathrm{sa}}\) is strongly dense in \(N_{\mathrm{sa}}\).

**Proof.** Regard \(V=N_{\mathrm{sa}}\) as a real vector space. A strongly continuous real-linear functional \(\ell\) on \(V\) is bounded by finitely many strong seminorms. More explicitly, continuity at zero and homogeneity give \(\xi_1,\ldots,\xi_n\in K\) and \(C<\infty\) with
\[
|\ell(a)|\leq C\left(\sum_{j=1}^n\|a\xi_j\|^2\right)^{1/2}
\quad(a\in V).
\tag{HAP.13}
\]
If the seminorm on the right vanishes, homogeneity forces \(\ell(a)=0\). Thus \(\ell\) factors through the real-linear map
\[
a\longmapsto(a\xi_1,\ldots,a\xi_n)\in K^n.
\]
The induced bounded real functional on its range extends to the underlying real Hilbert space \(K^n_{\mathbb R}\), by real Hahn–Banach. Real Riesz representation supplies \(\eta_1,\ldots,\eta_n\in K\) such that
\[
\ell(a)=\operatorname{Re}\sum_{j=1}^n\langle a\xi_j,\eta_j\rangle.
\tag{HAP.14}
\]
This is weak-operator continuous. Conversely every weak-operator continuous functional is strongly continuous, since the strong topology is finer.

It follows directly from real locally convex separation that a convex subset of \(V\) has the same strong and weak-operator closures. Indeed, a point outside its strong closed convex closure is separated from that closure by a strongly continuous real functional, which by (HAP.14) is weak-operator continuous. Such a point is also outside its weak closure; the opposite closure inclusion follows from the relative strength of the topologies.

Finally, if \(a=a^*\in N\), (HAP.12) supplies \(c_i\in\mathcal C\) with \(c_i\to a\) weakly. Adjoint is weak-operator continuous, so
\((c_i+c_i^*)/2\to a\) weakly. Hence \(\mathcal C_{\mathrm{sa}}\) is weakly dense in \(V\). It is convex, and the preceding paragraph proves strong density. \(\square\)

<span id="oa-mod-hap-05--contractive-approximation-from-a-nonunital-algebra"></span>
<span id="OA-MOD-HAP-05"></span>
<span id="oa-mod-hap-05"></span>
## OA-MOD-HAP-05 — Contractive approximation from a nonunital algebra

**Theorem.** For the algebra \(\mathcal C\) in HAP-04, every contraction \(x\in N\) is the strong* limit of a net of contractions from \(\mathcal C\). If \(x=x^*\), the approximants may also be chosen self-adjoint.

**Proof for self-adjoint contractions.** Define by bounded continuous functional calculus
\[
y=x\bigl(I+(I-x^2)^{1/2}\bigr)^{-1},
\qquad
f(t)=\frac{2t}{1+t^2}\quad(t\in\mathbb R).
\tag{HAP.15}
\]
The inverse exists because its positive denominator is at least \(I\). The operator \(y\) is self-adjoint. The scalar identity
\[
f\left(\frac{t}{1+\sqrt{1-t^2}}\right)=t
\quad(-1\leq t\leq1)
\]
gives \(f(y)=x\). Also \(|f(t)|\leq1\) for every real \(t\).

Choose \(c_i\in\mathcal C_{\mathrm{sa}}\) with \(c_i\to y\) strongly, by HAP-04. For \(z=i\) and \(z=-i\), the resolvent identity is
\[
(c_i-zI)^{-1}-(y-zI)^{-1}
=(c_i-zI)^{-1}(y-c_i)(y-zI)^{-1}.
\tag{HAP.16}
\]
The first factor has norm at most one, by the continuous calculus of the bounded self-adjoint \(c_i\). Applying strong convergence to the fixed vector \((y-zI)^{-1}\xi\) proves strong convergence of these resolvents. Consequently
\[
f(c_i)=(c_i-iI)^{-1}+(c_i+iI)^{-1}
\longrightarrow f(y)=x
\quad\hbox{strongly}.
\tag{HAP.17}
\]
This argument has not assumed uniform bounds on the \(c_i\).

Each \(d_i=f(c_i)\) is a self-adjoint contraction in the norm closure of \(\mathcal C\). To check the last assertion in the nonunital case, approximate \(f\) by real polynomials \(p_k\) on a compact interval containing \(\sigma(c_i)\) and \(0\). Since \(f(0)=0\), the polynomials \(p_k(t)-p_k(0)\) still approximate \(f\) uniformly and have zero constant term. Their values at \(c_i\) belong to \(\mathcal C_{\mathrm{sa}}\).

For \(0<\varepsilon<1\), choose \(b_{i,\varepsilon}\in\mathcal C_{\mathrm{sa}}\) with
\(\|b_{i,\varepsilon}-d_i\|<\varepsilon\), and set
\[
a_{i,\varepsilon}=(1+\varepsilon)^{-1}b_{i,\varepsilon}.
\tag{HAP.18}
\]
Then \(\|a_{i,\varepsilon}\|\leq1\), and
\(\|a_{i,\varepsilon}-d_i\|<2\varepsilon\).
The product net, directed by increasing \(i\) and decreasing \(\varepsilon\), converges strongly to \(x\). All its terms and its limit are self-adjoint, so it also converges strongly*.

**Proof for arbitrary contractions.** The algebra \(M_2(\mathcal C)\) is nondegenerate on \(K\oplus K\). Its weak closure is \(M_2(N)\): weak operator convergence of these finite matrices is exactly entrywise weak convergence, and (HAP.12) approximates each entry, with the finite product of the indexing sets handling simultaneous approximation. Thus its generated von Neumann algebra is \(M_2(N)\).

Apply the self-adjoint result to
\[
X=\begin{pmatrix}0&x\\x^*&0\end{pmatrix}\in M_2(N),
\qquad \|X\|=\|x\|\leq1.
\tag{HAP.19}
\]
Let \(A_i\in M_2(\mathcal C)\) be self-adjoint contractions converging strongly to \(X\). If \(b_i=(A_i)_{12}\), then \(b_i\in\mathcal C\), \(\|b_i\|\leq1\), and \((A_i)_{21}=b_i^*\). Coordinate-vector tests give both \(b_i\to x\) and \(b_i^*\to x^*\) strongly. \(\square\)

This is the needed Kaplansky density theorem, proved with bounded functional calculus and real separation. It applies to \(\mathcal C=L(\mathcal A)\), not merely to its norm closure. It requires neither SK-09 nor modular theory. Scaling gives the corresponding approximation bound \(\|b_i\|\leq\|x\|\) for every \(x\in N\), with the zero case handled by the constant zero net.



<span id="oa-mod-hap-08--central-elements-preserve-both-involution-domains"></span>
<span id="OA-MOD-HAP-08"></span>
<span id="oa-mod-hap-08"></span>
## OA-MOD-HAP-08 — Central elements preserve both involution domains

**Proposition.** Every \(z\in Z(M)=M\cap M'\) preserves \(D(S)\) and \(D(F)\), and
\[
S(z\xi)=z^*S\xi\quad(\xi\in D(S)),\qquad
F(z\eta)=z^*F\eta\quad(\eta\in D(F)).
\tag{HAP.33}
\]
For the polar data in (HAP.5),
\[
JzJ=z^*,\qquad
\Delta^{it}z\Delta^{-it}=z\quad(t\in\mathbb R).
\tag{HAP.34}
\]

**Proof of the domain assertions.** If \(\xi\in\mathcal A_l\), then \(z\lambda_\xi\in\mathfrak n_l\). Its adjoint equals
\[
(z\lambda_\xi)^*=\lambda_\xi^*z^*=z^*\lambda_{S\xi}\in\mathfrak n_l,
\]
where centrality permits the middle interchange. By covariance and (HAP.4), \(z\xi\in\mathcal A_l\), and injectivity gives
\[
S(z\xi)=z^*S\xi.
\tag{HAP.35}
\]
For \(\xi\in D(S)\), take a graph-approximating sequence \(\xi_n\in\mathcal A_l\). Boundedness of \(z,z^*\) gives \(z\xi_n\to z\xi\) and \(S(z\xi_n)=z^*S\xi_n\to z^*S\xi\). Closedness of \(S\) proves the first half of (HAP.33).

The element \(z\) is also central in \(M'\): it belongs to \(M'\), and every element of \(M'\) commutes with it because \(z\in M\). The same argument with \(\mathfrak n_r\), \(R\), \(\mathcal A_r\) and \(F\) proves the other half. This uses the right ideal-intersection identity and the graph core \(\mathcal A_r\).

**Proof of the polar assertions.** First let \(u\in Z(M)\) be unitary. Equation (HAP.33), applied also to \(u^*\), gives \(uD(S)=D(S)\) and the exact operator identity
\[
uSu=S.
\tag{HAP.36}
\]
Write \(A=\Delta^{1/2}\). Then
\[
S=uJAu=(uJu)(u^*Au).
\]
The second factor is positive self-adjoint with its unitary-transported domain, and the first factor is antiunitary. Since \(A\) has zero kernel and dense range, uniqueness of the polar decomposition from TC gives
\[
J=uJu,\qquad A=u^*Au.
\tag{HAP.37}
\]
Therefore \(JuJ=u^*\). The second identity says that \(u\) commutes with \(A\) on its domain; unitary covariance of the spectral calculus gives commutation with every bounded Borel function of \(A\), in particular with \(\Delta^{it}\).

Finally, every central element is a finite complex linear combination of central unitaries. For completeness, if \(h=h^*\in Z(M)\), scale to a self-adjoint contraction and put \(v=h+i(I-h^2)^{1/2}\); this is a central unitary with \(h=(v+v^*)/2\). Real and imaginary parts treat a general element, with the zero case immediate. The conjugate-linearity of \(J\) then extends \(JuJ=u^*\) to \(JzJ=z^*\), and linearity extends the commutation relation with \(\Delta^{it}\). \(\square\)

These central identities follow before the fundamental modular theorem. The use of the full completion above is legitimate for every original \(\mathcal A\), because its closed involution and generated algebra remain \(S\) and \(M\).

