# Approximating multiplication without losing its bound

**Self-checked by the writing AI.**

A vector can be close to an algebra vector while its multiplication operator is much larger. We construct approximations that control both quantities. For a vector in the full Hilbert algebra we also control its involution; for a vector that is only left bounded we retain the vector limit and the exact multiplication bound. These different conclusions require different arguments.

Free comparisons are Brent Nelson, [*Tomita–Takesaki Theory*, Proposition 1.25, Proposition 1.26, Lemma 1.27 and Theorem 1.28, pages 12–14](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf), and Jesse Peterson, [*Notes on von Neumann algebras*, Theorem 2.6.4, page 31](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf). The canonical Kaplansky statement belongs to the foundation course, Theorem 7.1(1)–(2); HAP04–05 supplies a complete alternative proof for the nondegenerate algebra used here. The spectral-convergence step invoked by citation in Nelson’s Lemma 1.27 is proved locally in SK09; the approximation below uses real polynomials on each bounded spectral interval and rescales the polynomial algebra vector. Central elements are treated through multiplication domains and uniqueness of polar decomposition.

## Spaces, topologies and prerequisites

Let \(\mathcal A\subseteq H\) be an arbitrary left Hilbert algebra. Inner products are linear in the first variable. Retain the constructions of HA02–05, RD04–07 and FL01–04:

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

WH04 proves the mixed identity also for every right-bounded vector in the displayed domain. Both multiplication assignments are injective. Their ranges

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

The exact bounded-operator inputs are BK01, which proves Riesz representation and continuous functional calculus, BK03 for operator topologies, and BK07 for polar decomposition. The sigma-strong vector tests are proved in CP08. Real Hahn–Banach extension and locally convex separation have complete proofs in NP1–2 of the prerequisite note. HAP-03 and HAP-06 use the arbitrary-net common-core convergence theorem SK09: convergence of self-adjoint operators on a graph core for their self-adjoint limit implies strong convergence of every bounded continuous function of those operators. The approximating operators need not have uniformly bounded norms. For a bounded limit, any Hilbert-dense linear domain is a graph core.

Only HAP-08 uses the polar identities

\[
S=J\Delta^{1/2},\qquad
F=J\Delta^{-1/2},\qquad J^2=I,
\tag{HAP.5}
\]

including exact domains, from TC08–10, together with SK08. No identification \(JMJ=M'\), modular automorphism theorem, faithful state or countability restriction is an input to this unit.

## Closed graphs in the appropriate ambient spaces

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

## Two quadratic products from one block operator

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

## Why self-adjoint weak density gives strong density

We need an approximation theorem for the original multiplication algebra, which need not contain an identity or be norm closed. We first prove its topological ingredient.

Let \(\mathcal C\subseteq B(K)\) be a nondegenerate *-subalgebra, and write \(N=\mathcal C''\). HA03, the nonunital proof, gives

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

## Contractive approximation from a nonunital algebra

**Foundation theorem and alternative proof.** The canonical programme statement is Theorem 7.1(1)–(2) of *Kaplansky’s density theorem and its consequences*, in *Foundations of von Neumann algebras*. It allows degenerate as well as nondegenerate subalgebras and does not require norm closure. HAP04 identifies the weak closure in the present nondegenerate setting; the complete proof below is an alternative for that setting. Peterson’s free Theorem 2.6.4 provides a comparison. The proof explicitly returns from the norm closure to the original algebra, which need not contain an identity.

**Theorem.** For the algebra \(\mathcal C\) in HAP-04, every contraction \(x\in N\) is the strong* limit of a net of contractions from \(\mathcal C\). If \(x=x^*\), the approximants may also be chosen self-adjoint.

**Alternative proof for self-adjoint contractions.** Define by bounded continuous functional calculus

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

**Alternative proof for arbitrary contractions.** The algebra \(M_2(\mathcal C)\) is nondegenerate on \(K\oplus K\). Its weak closure is \(M_2(N)\): weak operator convergence of these finite matrices is exactly entrywise weak convergence, and (HAP.12) approximates each entry, with the finite product of the indexing sets handling simultaneous approximation. Thus its generated von Neumann algebra is \(M_2(N)\).

Apply the self-adjoint result to

\[
X=\begin{pmatrix}0&x\\x^*&0\end{pmatrix}\in M_2(N),
\qquad \|X\|=\|x\|\leq1.
\tag{HAP.19}
\]

Let \(A_i\in M_2(\mathcal C)\) be self-adjoint contractions converging strongly to \(X\). If \(b_i=(A_i)_{12}\), then \(b_i\in\mathcal C\), \(\|b_i\|\leq1\), and \((A_i)_{21}=b_i^*\). Coordinate-vector tests give both \(b_i\to x\) and \(b_i^*\to x^*\) strongly. \(\square\)

This alternative proves the canonical Kaplansky statement in the present nondegenerate case by bounded functional calculus and real separation. It applies to \(\mathcal C=L(\mathcal A)\), not merely to its norm closure. It requires neither SK-09 nor modular theory. Scaling gives the corresponding approximation bound \(\|b_i\|\leq\|x\|\) for every \(x\in N\), with the zero case handled by the constant zero net.

## Approximation in the full involution graph

**Theorem.** For every \(\xi\in\mathcal A_l\), there exists a sequence \(a_n\in\mathcal A\) such that

\[
a_n\longrightarrow\xi,\qquad a_n^\sharp\longrightarrow S\xi
\quad\hbox{in Hilbert norm},\qquad
\|L_{a_n}\|\leq\|\lambda_\xi\|\quad(n\geq1).
\tag{HAP.20}
\]

Consequently \(L_{a_n}\to\lambda_\xi\) strongly*.

**Proof.** If \(\lambda_\xi=0\), injectivity gives \(\xi=0\), and choose \(a_n=0\). Otherwise scale \(\xi\) by the positive number \(\|\lambda_\xi\|\); it suffices to prove the result when \(\|\lambda_\xi\|=1\).

Since \(\mathcal A\) is a graph core for \(S\), choose \(v_n\in\mathcal A\) with

\[
v_n\to\xi,\qquad v_n^\sharp\to S\xi.
\]

Put \(T_n=L_{v_n}\), \(T=\lambda_\xi\). For \(\eta\in\mathcal A_r\), (HAP.2) gives

\[
T_n\eta=R_\eta v_n\to R_\eta\xi=T\eta,\qquad
T_n^*\eta=R_\eta v_n^\sharp\to R_\eta S\xi=T^*\eta.
\tag{HAP.21}
\]

The subspace \(\mathcal A_r\) is dense. Apply HAP-03 to

\[
k(t)=
\begin{cases}
1,&0\leq t\leq1,\\
t^{-1/2},&t\geq1.
\end{cases}
\tag{HAP.22}
\]

This is bounded and continuous. Since \(T\) is a contraction,

\[
k(T_nT_n^*)\to I,\qquad k(T_n^*T_n)\to I
\quad\hbox{strongly}.
\tag{HAP.23}
\]

Define vectors

\[
w_n=k(T_nT_n^*)v_n,\qquad
z_n=k(T_n^*T_n)v_n^\sharp.
\tag{HAP.24}
\]

Both lie in \(\mathcal B_l\) by covariance. Continuous functional calculus and polynomial intertwining give

\[
T_n^*k(T_nT_n^*)=k(T_n^*T_n)T_n^*.
\tag{HAP.25}
\]

For this identity it is enough to approximate \(k\) uniformly on the compact interval \([0,\|T_n\|^2]\); polynomial intertwining follows by induction. Thus \(\lambda_{w_n}^*=\lambda_{z_n}\). The ideal-intersection identity (HAP.4) puts \(w_n\) in \(\mathcal A_l\) and gives \(Sw_n=z_n\).

Since \(\|k(T_nT_n^*)\|\leq1\), equation (HAP.23) yields

\[
\|w_n-\xi\|
\leq\|v_n-\xi\|+\|(k(T_nT_n^*)-I)\xi\|\longrightarrow0.
\]

The same reasoning gives \(z_n\to S\xi\). Moreover

\[
\|\lambda_{w_n}\|^2
=\|k(T_nT_n^*)T_nT_n^*k(T_nT_n^*)\|
\leq\sup_{t\geq0}t\,k(t)^2=1.
\tag{HAP.26}
\]

It remains to return from \(\mathcal A_l\) to the original algebra. Choose a real polynomial \(p_n\) satisfying

\[
\sup_{0\leq t\leq\|T_n\|^2}|p_n(t)-k(t)|
\leq\delta_n,\qquad
\delta_n=\frac{1}{n(1+\|v_n\|+\|v_n^\sharp\|+\|T_n\|)}.
\tag{HAP.27}
\]

Only this compact interval is involved. Let

\[
b_n=p_n(v_nv_n^\sharp)v_n\in\mathcal A.
\tag{HAP.28}
\]

The formula means the corresponding finite sum of products; its constant term is a scalar multiple of \(v_n\), so no identity in \(\mathcal A\) is needed. Real coefficients and algebraic intertwining give

\[
b_n=p_n(T_nT_n^*)v_n,\qquad
b_n^\sharp=p_n(T_n^*T_n)v_n^\sharp,\qquad
L_{b_n}=p_n(T_nT_n^*)T_n.
\]

Equations (HAP.24–27) imply

\[
\|b_n-w_n\|\leq n^{-1},\qquad
\|b_n^\sharp-z_n\|\leq n^{-1},\qquad
\|L_{b_n}\|\leq1+n^{-1}.
\tag{HAP.29}
\]

Set \(a_n=(1+n^{-1})^{-1}b_n\). Then \(\|L_{a_n}\|\leq1\), and both vector limits in (HAP.20) persist, because the scalar factor tends to one and \(b_n,b_n^\sharp\) converge.

Finally (HAP.2) gives strong convergence of \(L_{a_n}\) and \(L_{a_n}^*\) on the dense domain \(\mathcal A_r\). Their uniform bounds extend it to all of \(H\): for uniformly bounded \(Q_n,Q\), approximate a fixed vector by \(\eta\in\mathcal A_r\) in

\[
\|(Q_n-Q)v\|\leq(\sup_n\|Q_n\|+\|Q\|)\|v-\eta\|+\|(Q_n-Q)\eta\|.
\]

This proves the final assertion. Undoing the initial positive scaling proves the general case. \(\square\)

The sequence is chosen for one vector in the Hilbert graph. It supplies no countable dense set for \(H\). The strong* conclusion is stronger than the strong conclusion alone and follows from the explicit second vector limit.

## Approximation of every left-bounded vector

**Theorem.** If \(\xi\in\mathcal B_l\), there is a sequence \(a_n\in\mathcal A\) with

\[
a_n\to\xi\quad\hbox{in Hilbert norm},\qquad
\|L_{a_n}\|\leq\|\lambda_\xi\|,\qquad
L_{a_n}\to\lambda_\xi\quad\hbox{strongly}.
\tag{HAP.30}
\]

No membership of \(\xi\) in \(D(S)\) is required.

**Proof.** Put \(T=\lambda_\xi\). The case \(T=0\) is again trivial. Take the bounded polar decomposition \(T=u|T|\) in \(M\), and set

\[
\zeta=u^*\xi.
\]

Covariance gives \(\zeta\in\mathcal B_l\) and \(\lambda_\zeta=|T|\). Because this multiplier is self-adjoint, (HAP.4) gives \(\zeta\in\mathcal A_l\), with \(S\zeta=\zeta\). The final support \(q=uu^*\) satisfies \(qT=T\); injectivity of \(\lambda\) gives \(q\xi=\xi\). Thus \(u\zeta=\xi\).

Use HAP-06 to choose \(v_n\in\mathcal A\) with

\[
\|v_n-\zeta\|<(2n)^{-1},\qquad
\|L_{v_n}\|\leq\||T|\|=\|T\|.
\tag{HAP.31}
\]

HAP-05, applied to the contraction \(u\in M\) and \(\mathcal C=L(\mathcal A)\), supplies a contraction \(L_{b_n}\), \(b_n\in\mathcal A\), with

\[
\|(L_{b_n}-u)v_n\|<(2n)^{-1}.
\tag{HAP.32}
\]

This is one vector test for each \(n\); choosing its witness from the approximating net does not replace that global net by a globally convergent sequence.

Set \(a_n=b_nv_n\). Then

\[
\|a_n-\xi\|
\leq\|(L_{b_n}-u)v_n\|+\|u(v_n-\zeta)\|<n^{-1},
\qquad
\|L_{a_n}\|\leq\|L_{b_n}\|\,\|L_{v_n}\|\leq\|T\|.
\]

On \(\mathcal A_r\), (HAP.2) now gives \(L_{a_n}\eta=R_\eta a_n\to R_\eta\xi=T\eta\). The uniform bound extends convergence to every vector as in HAP-06. \(\square\)

The statement supplies no limit for \(a_n^\sharp\). In particular it must not be used to put a merely left-bounded vector in the closed involution domain.

## Central elements preserve both involution domains

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

## A block model that separates the domains

On the algebra of finite-support sequences of \(2\times2\) matrices, use componentwise product, matrix adjoint, and

\[
\langle a,b\rangle
=\sum_{n\geq1}\operatorname{Tr}(D_n b_n^*a_n),
\qquad D_n=\operatorname{diag}(1,n^4).
\tag{HAP.38}
\]

The sum is finite on the original algebra \(\mathcal A\). Its Hilbert completion consists of sequences with

\[
\sum_n\|a_nD_n^{1/2}\|_{\mathrm{HS}}^2<\infty.
\]

The completion is justified by OW09: index the matrix entries by triples \((n,i,j)\), where \(n\geq1\) and \(i,j\in\{1,2\}\), and use the positive column weights from \(D_n\). Its square-sum completeness and finite-support density proof identifies exactly the Hilbert space displayed above. The finite matrix identities and multiplication norm tests used below are proved in OW10.

Left multiplication by a sequence \(x\) has operator norm \(\sup_n\|x_n\|_{\mathrm{op}}\), whenever that supremum is finite. Indeed the map \(a_n\mapsto a_nD_n^{1/2}\) changes each block norm to the Hilbert–Schmidt norm while preserving left multiplication. Testing one block and a rank-one matrix gives the lower bound, and summing the block upper bounds gives the reverse inequality.

The adjoint identity follows by matrix multiplication and the trace. Involution is closable because convergence in the Hilbert space implies convergence in every finite-dimensional block. Products are dense since a finite-support vector is its product with the block identity on its finite support. These verify the Hilbert algebra axioms.

Finite block truncations identify the exact closed involution:

\[
D(S)=\left\{a\in H:\sum_n\|a_n^*D_n^{1/2}\|_{\mathrm{HS}}^2<\infty\right\},
\qquad (Sa)_n=a_n^*.
\tag{HAP.39}
\]

Necessity follows from coordinate convergence of a graph limit; sufficiency follows by truncating both square-summable sums. Here the left-bounded space and full algebra are

\[
\mathcal B_l=\{a\in H:\sup_n\|a_n\|_{\mathrm{op}}<\infty\},
\qquad
\mathcal A_l=\mathcal B_l\cap D(S).
\tag{HAP.40}
\]

First verify the asserted finite vectors in the right algebra. Right multiplication by a finite-support vector \(\eta\), in the Hilbert–Schmidt coordinate \(X_n=a_nD_n^{1/2}\), is

\[
 X_n\longmapsto X_nD_n^{-1/2}\eta_nD_n^{1/2}.
\]

Only finitely many blocks are nonzero, so the maximum of their matrix operator norms gives a finite bound for this map on the completed Hilbert space. Thus \(\eta\) is right bounded. It also belongs to \(D(F)\): the pairing of \(Sa\) with \(\eta\) uses only those finitely many coordinates, and adjoint on each finite-dimensional block is bounded. Hence that pairing is bounded by a constant times \(\|a\|\), which is exactly the adjoint-domain criterion of TC03. This proves \(\eta\in\mathcal A_r\).

To verify the bounded-space statement, test the defining left-boundedness inequality on these finite block vectors in the right algebra. It forces the stated block multiplier bound. Conversely a uniformly bounded left multiplier gives the defining inequality first on those finite vectors; arbitrary right-bounded vectors act blockwise by their continuous extension, giving \(\lambda_a\eta=R_\eta a\) and the same bound on all of \(\mathcal A_r\). Thus these spaces agree with (HAP.1), rather than merely being proposed extensions.

In this example the approximants in HAP-06 and HAP-07 can be the finite block truncations. Their multiplication norms do not increase. For \(\xi\in\mathcal A_l\), both \(\xi\) and \(S\xi\) have square-summable tails, giving the two limits in (HAP.20). For \(\xi\in\mathcal B_l\), only the first tail condition is automatic.

## Problems with complete solutions

**Problem 1: a limit outside the involution domain.** In HAP-09 let

\[
\xi_n=n^{-2}E_{21},\qquad
a^{(N)}_n=
\begin{cases}\xi_n,&n\leq N,\\0,&n>N.\end{cases}
\]

Show that \(a^{(N)}\to\xi\) in Hilbert norm and \(L_{a^{(N)}}\to\lambda_\xi\) in operator norm, but \(\xi\notin D(S)\). Explain which ambient space in HAP-02 matters.

**Solution.** The squared Hilbert norm of \(E_{21}\) in the \(n\)-th block is \(1\). Hence
\(\|\xi\|^2=\sum_n n^{-4}<\infty\), and the tail sums prove the vector convergence. The left multiplication norm of the tail is
\(\sup_{n>N}n^{-2}=(N+1)^{-2}\), which tends to zero. In particular \(\xi\in\mathcal B_l\).

The convergence of the first scalar series can be checked without an integral test. In the block \(2^k\leq n<2^{k+1}\),

\[
 \sum_{n=2^k}^{2^{k+1}-1}n^{-4}\leq2^{-3k}.
\]

The finite geometric-sum identity gives \(\sum_{k=K}^{\infty}2^{-3k}=(8/7)2^{-3K}\), tending to zero. This proves convergence and the required vanishing tails.

The squared norm of \(E_{12}\) in that block is \(n^4\). Thus the proposed adjoint sequence has total squared norm

\[
\sum_n\|n^{-2}E_{12}\|_n^2=\sum_n1=\infty.
\]

Equation (HAP.39) gives \(\xi\notin D(S)\); also \(\|(a^{(N)})^\sharp\|^2=N\). The \(\mathcal A_l\) graph therefore is not closed in \(H\times M\), even with operator norm on \(M\). HAP-02 places its first coordinate in \(D(S)\), and this limit is outside that ambient space.

**Problem 2: the global density theorem still needs nets.** Let \(I\) be uncountable and let \(\mathcal C=c_{00}(I)\) act diagonally on \(\ell^2(I)\). Verify the hypotheses of HAP-05 and show that no sequence in \(\mathcal C\) converges strongly to the identity.

**Solution.** This is a nondegenerate *-algebra: every single-coordinate vector is in the range of its coordinate projection. Its weak closure is the full diagonal algebra \(\ell^\infty(I)\). One may see this directly by finite-coordinate truncation nets for each bounded diagonal function, whose norms do not increase and which converge strongly by the square-summable tails of each vector. Conversely commuting with the coordinate projections forces an operator to be diagonal, so the bicommutant is precisely that diagonal algebra.

The union of the finite supports of any sequence from \(\mathcal C\) is countable. Choose a coordinate outside it. Every sequence member annihilates the corresponding unit vector, whereas the identity fixes it. Thus there is no such strong limit. The sequences in HAP-06–07 approximate a single vector and do not contradict this fact about simultaneous convergence on every vector.

**Problem 3: why the multiplier cutoff also controls the adjoint.** In HAP-06, derive (HAP.25) first for monomials and explain why using complex polynomial coefficients in (HAP.28) would require changing the displayed adjoint formula.

**Solution.** For \(k\geq0\), induction gives

\[
T^*(TT^*)^k=(T^*T)^kT^*.
\]

Linearity proves the intertwining identity for every polynomial. Uniform approximation on the compact interval containing both positive spectra gives (HAP.25) for the real continuous cutoff. If \(p(t)=\sum_j c_jt^j\), taking adjoints conjugates the coefficients, so

\[
\bigl(p(vv^\sharp)v\bigr)^\sharp
=\overline p(v^\sharp v)v^\sharp,
\qquad \overline p(t)=\sum_j\overline{c_j}t^j.
\]

Choosing real coefficients lets the same polynomial occur in the two graph estimates. The order of the two quadratic products still differs and cannot be suppressed.

## Exact conclusions and remaining scope

HAP-02 supplies both source closed-graph statements, with a slightly weaker operator topology sufficient for each proof. HAP-03 gives the full arbitrary-net functional-calculus lemma. HAP-06 proves the original-algebra approximation of every vector in the full completion, with simultaneous graph-norm and strong* convergence; HAP-07 gives the exact bound and strong convergence for every left-bounded vector. HAP-08 supplies the two central domain identities and both polar consequences.

The algebra need not be unital, the Hilbert space need not be separable, and the bounded-vector limit need not lie in the involution domain. The global density theorem is a net theorem; the two vector approximation theorems are sequence theorems with separately stated conclusions. No uniform polynomial approximation on an unbounded interval is used.

The block model makes the domain distinction explicit: bounded multiplication controls the vector approximation, while the adjoint vector requires a separate square-sum condition. The central identities follow from graph domains and polar uniqueness, before any modular commutant theorem.
