# Normal products and closed operator graphs

*AI-assisted text by GPT-6.1 Sol and GPT-6 Astra (OpenAI). Original contributions: CC0 1.0.*

The spatial tensor product of von Neumann algebras supports normal maps and normal functionals. A commuting action need not realize that product normally. We will characterize normal factorization by a product functional, then use two-by-two operator matrices to recognize unbounded observables through their graphs.

Prerequisites are [Spatial tensor products of von Neumann algebras](../reader/supplements/spatial-tensor-products.html), [Tensor independence and ideals](../reader/tensor-independence-and-ideals.html), [Completely positive maps](../../foundations-of-von-neumann-algebras/completely-positive-maps.html#OA-FND-CM-05), and [Polar decomposition of functionals](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#OA-FND-PD-02). For the unbounded graph calculation, use the proved [closed-form representation theorem](../reader/supplements/closed-positive-forms.html#OA-MOD-QF-03) and [spectral calculus with exact domains](../reader/supplements/spectral-calculus-kernel.html#OA-MOD-SK-05). Section 3 derives the closed-operator adjoint and polar decomposition from these results before using them. There is no separability or countable-decomposability assumption on the algebras or Hilbert spaces.

Freely readable treatments are Blackadar’s [Operator Algebras](https://bruceblackadar.com/Mathematics/Cycr.pdf), on normal completely positive tensor maps, slices and product states, and Peterson’s [Notes on operator algebras](https://math.vanderbilt.edu/peters10/teaching/spring2015/OperatorAlgebras.pdf), April 6, 2015, on graph adjoints, positive operators, spectral calculus and polar decomposition. The proofs here include the normal preadjoint extension, all four graph entries and the nondense-domain formula. The polar isometry’s initial space is the closure of the range of the absolute value. Further freely readable references include Stinespring on completely positive maps and Rieffel and van Daele on real Hilbert subspaces and modular theory.

## 1. Normal completely positive maps tensor normally

**Theorem 1.1.** Let \(\Phi:M\to P\) and \(\Psi:N\to Q\) be normal completely positive maps of von Neumann algebras. There is a unique normal completely positive map
\[
\Theta:M\bar\otimes N\longrightarrow P\bar\otimes Q,
\qquad \Theta(a\otimes b)=\Phi(a)\otimes\Psi(b).
\]
Its norm is \(\|\Phi\|\|\Psi\|\).

**Proof.** Theorem 4.1 of [Tensor norms and independent systems](../reader/tensor-norms-and-independent-systems.html#4-positive-maps-pass-to-the-appropriate-completion) gives a completely positive map \(\Theta_0:M\otimes_{\min}N\to P\otimes_{\min}Q\) with that norm. On finite sums of normal product functionals define
\[
T\Big(\sum_i\alpha_i\otimes\beta_i\Big)
=\sum_i(\alpha_i\circ\Phi)\otimes(\beta_i\circ\Psi).
\]
This is the Banach adjoint of \(\Theta_0\) on the indicated subspace. In particular it is well defined and bounded by \(\|\Phi\|\|\Psi\|\). Normality of the two factor maps makes every displayed factor functional normal.

The product-predual theorem in *Spatial tensor products* says that these finite sums are norm dense in the predual of each spatial tensor product, and that their norm equals their functional norm on the minimal C\*-product. Hence \(T\) extends to a map \((P\bar\otimes Q)_*\to(M\bar\otimes N)_*\). Its adjoint \(\Theta=T^*\) is normal and agrees with \(\Theta_0\) on algebraic tensors.

To verify complete positivity of the extension, take a positive matrix \(X\) over \(M\bar\otimes N\). Matrix Kaplansky density gives a bounded net \(Y_\lambda\) over the minimal C\*-product converging strongly to \(X^{1/2}\). Use the positive matrices \(Y_\lambda^*Y_\lambda\). For arbitrary vectors \(\xi,\eta\),
\[
 \langle Y_\lambda^*Y_\lambda\xi,\eta\rangle
 =\langle Y_\lambda\xi,Y_\lambda\eta\rangle
 \longrightarrow\langle X\xi,\eta\rangle.
\]
Their norms are uniformly bounded, so vector-series approximation upgrades this weak operator convergence to ultraweak convergence. Their images under \(\Theta^{(k)}\) are positive because \(\Theta\) agrees with the completely positive \(\Theta_0\) on the minimal product. Ultraweak continuity and closedness of the positive cone now give \(\Theta^{(k)}(X)\ge0\). This works for every matrix size. The upper norm bound comes from \(T\), and elementary tensors give the opposite bound. Algebraic tensors are ultraweakly dense, proving uniqueness. \(\square\)

For example, normal states \(\varphi\in M_*\), \(\psi\in N_*\) have a normal product state. Its support is
\[
s(\varphi\otimes\psi)=s(\varphi)\otimes s(\psi).
\]
The support and faithfulness proof is in Theorem 10.1 of *Spatial tensor products*. It covers zero functionals and arbitrary Hilbert spaces.

## 2. When a commuting pair splits normally

Let \(A,B\subseteq M\) be commuting subfactors generating the factor \(M\), with their identities equal to that of \(M\). Multiplication is algebraically injective by the factor–commutant theorem. Its extension to \(A\bar\otimes B\) asks for more than algebraic independence.

**Theorem 2.1.** The following are equivalent.

1. Multiplication extends to a normal \*-isomorphism \(A\bar\otimes B\to M\).
2. There is a nonzero normal functional \(f\in M_*\) with
   \[
   f(ab)=f(a)f(b)\quad(a\in A,b\in B).
   \]
3. There is a nonzero normal bounded linear map \(E:M\to A\) satisfying
   \[
   E(axb)=aE(x)b\quad(a,b\in A,x\in M).
   \]

One may interchange \(A\) and \(B\) in condition 3. No positivity is required in conditions 2 or 3.

**Proof.** If 1 holds, take any normal state \(\beta\) of \(B\). Transport the normal slice \(\mathrm{id}_A\bar\otimes\beta\) to obtain the map in 3. Take a normal state \(\alpha\) of \(A\) and compose with the slice to obtain a product state, proving 2 as well.

Suppose 2 holds. Nonzeroness and the product identity imply \(f(1)=1\). The restrictions \(f_A,f_B\) are nonzero normal functionals. Polar decomposition supplies partial isometries \(v_A\in A,v_B\in B\) such that
\[
\alpha(a)=f_A(v_Aa),\qquad \beta(b)=f_B(v_Bb)
\]
are positive nonzero normal functionals. Define \(g(x)=f(v_Av_Bx)\). On the algebraic span of products, \(g(ab)=\alpha(a)\beta(b)\). Hence \(g\) is positive on algebraic squares. Bounded strong approximation of square roots, followed by normality of \(g\), makes it positive on all of \(M\). Its value at the identity is \(\alpha(1)\beta(1)>0\). Normalize \(g,\alpha,\beta\) to states, retaining the product identity.

The GNS representation of a normal state is normal. For completeness, on cyclic vectors its positive matrix coefficients are \(x\mapsto g(c^*xc)\), which preserve bounded increasing limits; approximation of arbitrary vectors extends that preservation. The same argument gives normality for the two marginal GNS representations. A nonzero normal representation of a factor is faithful: its kernel is an ultraweakly closed ideal, hence is generated by a central projection, and a factor has only the two central projections.

Now define on the dense cyclic subspaces
\[
U\big(\pi_\alpha(a)\xi_\alpha\otimes
\pi_\beta(b)\xi_\beta\big)=\pi_g(ab)\xi_g.
\]
The product identity gives equality of the inner products of every pair of finite sums, so \(U\) extends to an isometry. Its range is dense: the algebraic span of products is strongly dense in \(M\), and bounded strong approximation implies convergence on the GNS cyclic vector by normality. Thus \(U\) is unitary. It intertwines the two factor actions. Their normal weak closures therefore identify \(\pi_g(M)\) with \(\pi_\alpha(A)\bar\otimes\pi_\beta(B)\). All three representations are faithful normal representations, so this is exactly the isomorphism in 1.

Finally suppose 3 holds. For \(b\in B\), bimodularity and commutation show \(aE(b)=E(b)a\) for every \(a\in A\). Since \(A\) is a factor, \(E(b)=\omega(b)1\) for a normal functional \(\omega\in B_*\). It is nonzero: otherwise \(E\) would vanish on every product and normal density would give \(E=0\). Choose \(d\in B\) with \(\omega(d)\ne0\), and set \(E_d(x)=E(xd)/\omega(d)\). It remains normal and bimodular, and \(E_d(1)=1\). With a normal state \(\alpha\) on \(A\), put \(f=\alpha\circ E_d\). Then
\[
f(ab)=\alpha(a)\frac{\omega(bd)}{\omega(d)}=f(a)f(b),
\]
and \(f(1)=1\), proving 2. The same proof works with the factors interchanged. \(\square\)

If a normal map is initially known to satisfy the bimodule identity only for \(x\in B\), it satisfies it for all \(x\in M\). First commute the factors to verify it on finite product sums, then use ultraweak density and normality. Thus the restricted identity suffices in condition 3.

## 3. A graph is a bounded encoding of an unbounded operator

### Adjoints and closure of a graph

First consider a densely defined linear map \(S:D(S)\subseteq H\to L\), where the two Hilbert spaces may differ. Inner products are linear in the first variable. Its adjoint has domain
\[
\begin{aligned}
D(S^*)=\{y\in L:{}&\text{there exists }z\in H\text{ with }\\
&\langle Sx,y\rangle=\langle x,z\rangle\quad(x\in D(S))\}.
\end{aligned}
\]
Density makes \(z\) unique; set \(S^*y=z\). Directly from this definition,
\[
G(S)^\perp=\{(-S^*y,y):y\in D(S^*)\}.
\tag{3.a}
\]
Thus \(S^*\) is closed: if \(y_n\to y\) and \(S^*y_n\to z\), the defining identities pass to the limit and give \(S^*y=z\).

The vertical part of the closed subspace \(\overline{G(S)}=G(S)^{\perp\perp}\) consists precisely of the vectors \((0,y)\) with \(y\perp D(S^*)\), by (3.a). A linear subspace of \(H\oplus L\) is a graph exactly when it has no nonzero vertical vector. Consequently \(S\) is closable exactly when \(D(S^*)\) is dense in \(L\). In that case applying (3.a) to \(S^*\), with the two spaces exchanged, identifies \(\overline{G(S)}\) with \(G(S^{**})\). Therefore the closure is \(S^{**}\). In particular, for a closed densely defined \(T\), the adjoint \(T^*\) is closed and densely defined and \(T^{**}=T\).

### Polar decomposition for closed operators

**Proposition.** Let \(T:D(T)\subseteq H\to L\) be closed and densely defined. Then
\[
\begin{gathered}
A=T^*T,\\
D(A)=\{x\in D(T):Tx\in D(T^*)\}
\end{gathered}
\]
is nonnegative self-adjoint. Its positive square root \(P=A^{1/2}\) satisfies
\[
\begin{aligned}
D(P)&=D(T),\\
\|Px\|&=\|Tx\|\quad(x\in D(T)).
\end{aligned}
\tag{3.b}
\]
There is a unique partial isometry \(v:H\to L\), zero on \(\ker T\), whose initial and final spaces are \((\ker T)^\perp\) and \(\overline{\operatorname{ran}T}\), and for which \(T=vP\) on this exact domain.

**Proof.** On \(D(T)\), put \(q(x,y)=\langle Tx,Ty\rangle\). Its form norm is the graph norm, so \(q\) is a densely defined closed nonnegative form. The [closed-form representation theorem](../reader/supplements/closed-positive-forms.html#OA-MOD-QF-03) supplies a unique nonnegative self-adjoint \(A\), with \(D(A^{1/2})=D(T)\) and (3.b). Its operator-domain criterion says that \(x\in D(A)\) precisely when some \(z\in H\) satisfies \(\langle Tx,Ty\rangle=\langle z,y\rangle\) for every \(y\in D(T)\). Taking conjugates is exactly the condition \(Tx\in D(T^*)\) and \(T^*Tx=z\). This proves the displayed identification of \(A\), rather than presupposing self-adjointness of \(T^*T\).

Define \(v(Px)=Tx\) for \(x\in D(P)\). Equation (3.b) makes this well defined and isometric, so it extends to an isometry from \(\overline{\operatorname{ran}P}\) onto \(\overline{\operatorname{ran}T}\). Since \(P=P^*\), orthogonality to its range is exactly membership in its kernel: a vector orthogonal to all \(Px\) lies in \(D(P^*)\) with \(P^*y=0\). Equation (3.b) also gives \(\ker P=\ker T\). Extend \(v\) by zero on that kernel. The resulting partial isometry has the asserted initial and final spaces and satisfies \(T=vP\). Its values on the dense range of \(P\) and on the kernel determine it uniquely. The positive operator \(P\) itself is uniquely determined by the closed form and (3.b).

The adjoint formula retains its domain:
\[
\begin{gathered}
T^*=Pv^*,\\
D(T^*)=\{y\in L:v^*y\in D(P)\}.
\end{gathered}
\tag{3.c}
\]
Indeed, \(\langle Tx,y\rangle=\langle Px,v^*y\rangle\) for every \(x\in D(P)\), and the defining adjoint criterion and self-adjointness of \(P\) prove both directions. Thus \(TT^*\) is the transport of \(P^2\) to \(\overline{\operatorname{ran}T}\), with zero operator on its orthogonal complement. Finally, the [spectral calculus](../reader/supplements/spectral-calculus-kernel.html#OA-MOD-SK-07) gives \(e_n=1_{[0,n]}(P)\uparrow1\) strongly, \(e_nH\subseteq D(T)\), and \(\|Te_n\|\le n\). No countability of a basis is used. \(\square\)

The graph identities and polar-decomposition proposition above prove the adjoint, self-adjointness and exact-domain facts used below. Their unbounded prerequisites are the linked [closed-form representation theorem](../reader/supplements/closed-positive-forms.html#OA-MOD-QF-03) and [spectral calculus](../reader/supplements/spectral-calculus-kernel.html#OA-MOD-SK-07). If a closed operator has nondense domain, apply the proposition to the densely defined map from \(\overline{D(T)}\) into \(L\); this is the convention used below.

### The graph projection and affiliation

Let \(T:D(T)\subseteq H\to H\) be a closed linear operator. Its domain is allowed to be nondense. The graph
\[
G(T)=\{(\xi,T\xi):\xi\in D(T)\}\subseteq H\oplus H
\]
is closed, so has a bounded orthogonal projection \(p_T\).

We say \(T\) is affiliated with \(M\subseteq B(H)\) when every unitary \(u\in M'\) satisfies \(uD(T)=D(T)\) and \(Tu\xi=uT\xi\) on the domain.

**Theorem 3.1.** A closed operator \(T\) is affiliated with \(M\) exactly when \(p_T\in M_2(M)\).

**Proof.** The domain and commutation conditions say exactly that \(u\oplus u\) takes \(G(T)\) onto itself. A closed subspace is invariant under a unitary and its inverse exactly when its projection commutes with that unitary. Thus affiliation is equivalent to \(p_T\) commuting with every \(u\oplus u\), \(u\in U(M')\). Unitaries linearly span \(M'\), so this means all four matrix entries of \(p_T\) lie in \((M')'=M\). \(\square\)

Affiliation uses the unitaries of the commutant \(M'\). Requiring commutation with the unitaries of \(M\) gives a different condition. For example, with \(M=M_2(\mathbb C)\) and \(T=\operatorname{diag}(1,2)\), the graph projection lies in \(M_2(M)\), but \(T\) does not commute with the swap unitary in \(M\).

**Theorem 3.2.** Suppose first that \(T\) is densely defined. Write
\[
R=(1+T^*T)^{-1},\qquad S=(1+TT^*)^{-1}.
\]
Then
\[
p_T=\begin{pmatrix}
R&T^*S\\
TR&1-S
\end{pmatrix}.
\tag{3.1}
\]
All entries in (3.1) are bounded operators. The off-diagonal expressions denote their everywhere-defined bounded extensions.

**Proof.** In the polar decomposition \(T=v|T|\), put \(r=(1+|T|^2)^{-1}\) and \(c=|T|r\). Functional calculus gives \(\|c\|\le1/2\), \(r^2+c^2=r\), and \(c^2=(1-r)-(1-r)^2\). Also
\[
TR=vc,\qquad T^*S=cv^*,\qquad 1-S=v(1-r)v^*.
\]
The last identity holds on the closure of the range of \(T\); both sides are zero on its orthogonal complement. These identities show that the matrix in (3.1) is self-adjoint and idempotent.

Its range lies in \(G(T)\). For input \((\xi,\eta)\), the first component is \(r\xi+cv^*\eta\), which belongs to \(D(T)\) because both \(|T|r\) and \(|T|c=1-r\) are bounded. Applying \(T\) gives the second component. Conversely it fixes \((\xi,T\xi)\) for \(\xi\in D(T)\), by \(r\xi+cv^*T\xi=r\xi+(1-r)\xi=\xi\) and the corresponding lower identity. Hence this is precisely the graph projection. \(\square\)

For a nondense domain let \(H_0=\overline{D(T)}\), let \(j:H_0\hookrightarrow H\) be inclusion, and view \(T_0\) as a densely defined closed map \(H_0\to H\). Its adjoint is \(T_0^*:D(T_0^*)\subseteq H\to H_0\). The same proof for two different Hilbert spaces gives
\[
p_T=\begin{pmatrix}
j(1+T_0^*T_0)^{-1}j^*&jT_0^*(1+T_0T_0^*)^{-1}\\
T_0(1+T_0^*T_0)^{-1}j^*&1-(1+T_0T_0^*)^{-1}
\end{pmatrix}.
\tag{3.2}
\]
The upper-left entry vanishes on \(H_0^\perp\). If \(T\) is affiliated with \(M\), \(H_0\) is invariant under the commutant, so its projection belongs to \(M\); Theorem 3.1 still applies without change.

## 4. A joint algebra can have no normal product state

An instructive commutative example separates norm closure from weak closure. Let \(a,b>0\) with \(a/b\) irrational. Inside \(L^\infty(\mathbb R)\), let \(A\) and \(B\) consist of the essentially bounded functions of period \(a\) and period \(b\), respectively.

**Proposition 4.1.** These two algebras generate \(L^\infty(\mathbb R)\) as a von Neumann algebra. Their generated C\*-algebra is canonically \(A\otimes_{\min}B\). There is no nonzero normal functional \(f\) on \(L^\infty(\mathbb R)\) satisfying \(f(uv)=f(u)f(v)\) for \(u\in A,v\in B\).

**Proof.** The map
\[
\mathbb R\longrightarrow (\mathbb R/a\mathbb Z)\times(\mathbb R/b\mathbb Z)
\]
is continuous and injective: an equal pair of residues would make a difference simultaneously an integer multiple of both periods. The real line and the two-circle torus are standard Borel spaces. The injective Borel-map theorem gives a Borel inverse on the image. Therefore the two residue maps jointly generate the Borel sigma-algebra of \(\mathbb R\). Their bounded functions generate all of \(L^\infty(\mathbb R)\), including the Lebesgue completion. This uses Theorem 4.3 of [Polish spaces and standard Borel spaces](../../foundations-of-von-neumann-algebras/polish-spaces-and-standard-borel-spaces.html).

To prove the C\*-claim, verify the no-zero-product condition. For a periodic integrable function of period \(c>0\), write
\[
 m_c(F)=\frac1c\int_0^c F(t)\,dt,
 \qquad m_T(F)=\frac1T\int_0^T F(t)\,dt.
\]
Splitting \([0,T]\) into full periods and one remainder shows \(m_T(F)\to m_c(F)\). If \(u,v\) are nonzero bounded periodic functions, put \(F=|u|^2\) and \(G=|v|^2\), with periods \(a,b\). Their period means are positive. We claim
\[
 m_T(FG)\longrightarrow m_a(F)m_b(G).
\tag{4.a}
\]
Choose trigonometric polynomials \(P,Q\) approximating \(F,G\) in the normalized period \(L^2\) norms. Cauchy–Schwarz gives
\[
 \begin{aligned}
 |m_T(FG-PQ)|\le{}&m_T(|F-P|^2)^{1/2}m_T(|G|^2)^{1/2}\\
 &+m_T(|P|^2)^{1/2}m_T(|G-Q|^2)^{1/2}.
 \end{aligned}
\]
The limit superior is at most
\(\|F-P\|_{2,a}\|G\|_{2,b}+\|P\|_{2,a}\|G-Q\|_{2,b}\).
For \(P,Q\), integration of each exponential shows that the mean tends to the product of their constant coefficients: irrationality makes \(n/a+m/b=0\) possible only for \(n=m=0\). Finally \(|m_a(F-P)|\le\|F-P\|_{2,a}\), and similarly for \(G-Q\). Letting both approximation errors tend to zero proves (4.a). Its positive limit rules out \(uv=0\) almost everywhere. Corollary 3.2 of *Tensor independence and ideals* gives the C\*-isomorphism.

Here the trigonometric approximation can be obtained directly. On the circle of length one, interval step functions are dense in \(L^2\); replacing their finitely many jumps by linear transitions on intervals of arbitrarily small total length gives continuous periodic approximations. For completeness, interval approximation follows from the definition of Lebesgue outer measure: a measurable set in a finite interval has an open superset with arbitrarily small excess measure; an open subset of the line is a countable disjoint union of intervals, and a finite subunion loses arbitrarily little of its finite measure. Truncation and approximation of the range by finitely many values then give the asserted density of interval step functions. For a continuous periodic \(g\), let
\[
 K_N(t)=\frac1N\left|\sum_{j=0}^{N-1}e^{2\pi ijt}\right|^2.
\]
It is a nonnegative trigonometric polynomial with integral one. For \(\delta\le t\le1-\delta\), the geometric-sum formula gives \(K_N(t)\le1/(N\sin^2(\pi\delta))\). Thus
\(\int_0^1K_N(t)g(s-t)\,dt\) tends uniformly to \(g(s)\): use uniform continuity for \(t\) within \(\delta\) of an integer, and the displayed bound on the complement. Each convolution is a trigonometric polynomial. Rescaling the circle proves the approximation for either period.

For the last assertion write a normal functional as integration against \(h\in L^1(\mathbb R)\), and put
\[
H(\xi)=\int_{\mathbb R}h(t)e^{2\pi i\xi t}\,dt.
\]
If \(f(1)\ne1\), applying the product identity with either factor equal to \(1\) makes both restrictions zero, and then makes \(f\) zero on all finite product sums. Normality and the generation proved above would give \(f=0\). Hence a nonzero product functional has \(f(1)=1\), so \(H(0)=1\). The identity on periodic exponentials gives
\[
H(n/a+m/b)=H(n/a)H(m/b)
\qquad(n,m\in\mathbb Z).
\tag{4.1}
\]
To obtain the required integer approximations, put \(\theta=b/a\). Divide \([0,1)\) into \(N\) equal intervals and place the \(N+1\) fractional parts of \(0,\theta,\ldots,N\theta\) in them. Two lie in the same interval, giving integers \(1\le q_N\le N\) and \(p_N\) with \(0<|q_N\theta-p_N|<1/N\). The strict lower bound follows from irrationality. For any fixed bound on \(q_N\), the finitely many distances \(\operatorname{dist}(q\theta,\mathbb Z)\) have a positive minimum. Consequently \(q_N\to\infty\), and \(p_N\to\infty\) because \(\theta>0\). Take \(n_N=q_N\), \(m_N=-p_N\); then
\[
 \left|\frac{n_N}{a}+\frac{m_N}{b}\right|
 =\frac{|q_N\theta-p_N|}{b}<\frac1{bN}.
\]
The Riemann–Lebesgue lemma gives \(H(n_N/a),H(m_N/b)\to0\), whereas continuity gives \(H(n_N/a+m_N/b)\to H(0)=1\). This contradicts (4.1).

The two scalar Fourier facts used here follow directly from \(L^1\) approximation by step functions on bounded intervals: their transforms are continuous and tend to zero, and the transform difference is bounded uniformly by the \(L^1\) difference. \(\square\)

## 5. Exercises with solutions

**Exercise 5.1 (first step).** On \(\ell^2(\mathbb N)\), let \(T\xi=(n\xi_n)_n\), with domain \(\sum_n n^2|\xi_n|^2<\infty\). Compute the four graph entries and their norms. Is \(T\) affiliated with the diagonal von Neumann algebra?

**Solution.** The entries are the diagonal multipliers
\[
\frac1{1+n^2},\qquad \frac n{1+n^2},\qquad
\frac n{1+n^2},\qquad \frac{n^2}{1+n^2}.
\]
Their norms are \(1/2,1/2,1/2,1\), respectively; the final supremum is not attained. All entries lie in the diagonal algebra, so Theorem 3.1 proves affiliation. The graph entries are bounded even though \(T\) is unbounded.

**Exercise 5.2 (application).** On \(H=\mathbb C^2\), define a closed operator by \(D(T)=\mathbb Ce_1\) and \(Te_1=2e_2\). Find its graph projection. Why does the densely defined formula require modification?

**Solution.** The graph is the span of \((e_1,2e_2)\). Its projection has blocks
\[
p_T=\frac15\begin{pmatrix}
e_{11}&2e_{12}\\2e_{21}&4e_{22}
\end{pmatrix}.
\]
Formula (3.2) gives this: \(T_0^*T_0=4\) on \(H_0=\mathbb Ce_1\), while \(T_0T_0^*=4e_{22}\) on \(H\). There is no densely defined single-valued adjoint \(T^*\) on the original \(H\) in the sense required by (3.1). In particular the upper-left graph block must be zero on \(e_2\), rather than a resolvent with value one there.

**Exercise 5.3 (further step).** In Theorem 2.1, suppose \(E\) is positive and unital as well as normal and bimodular. Show that its scalar restriction to \(B\) is a normal state and that it is the transported slice for that state.

**Solution.** Write \(E(b)=\omega(b)1\). Positivity of \(E\) makes \(\omega\) positive, and \(E(1)=1\) gives \(\omega(1)=1\). Thus \(\omega\) is a normal state. The normal factorization isomorphism makes \(E(ab)=a\omega(b)\) agree with \(\mathrm{id}_A\bar\otimes\omega\) on the ultraweakly dense algebraic span. Normality gives equality everywhere. The existence of this positive map follows from the normal splitting; it is stronger than the arbitrary normal linear map used in the equivalence.

## 6. The intrinsic product and its concrete realizations

The concrete construction starts with an action on a Hilbert tensor product. There is also a definition using just the two algebras and their preduals. Its central projection records exactly which functionals remain normal in that action.

The additional prerequisite for this section is the universal-bidual and normal-extension theorem: a nondegenerate representation of a C\*-algebra \(C\) extends to a normal surjection from \(C^{**}\), with a central kernel, and the restriction to the complementary central summand has a normal inverse. The complete existing proof is in Sections 3–8 of [Every bounded functional becomes normal in one representation](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#constructing-the-bidual-before-using-it). Section 8 proves normality of that inverse through the preadjoint, without an automatic-normality assumption. This supplies the normal-extension theorem used in Lemma 2.1 of *The universal enveloping von Neumann algebra*. The automatic normality of a von Neumann algebra isomorphism, when needed below, is the result in Sections 2–4 and 6 of [Normal positive maps and their preadjoints](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#positive-maps-and-increasing-suprema). For its bounded scalar-functional step, Lemma 6.3 below gives an alternative using complete additivity. The general normal-weight recovery theorem is unnecessary for that step. The predual, monotone-net and positive-spanning facts remain the stated prerequisites.

Let \(M,N\) be von Neumann algebras. Put
\[
C=M\otimes_{\min}N,\qquad
E=\overline{M_*\odot N_*}^{\,\|\cdot\|_{C^*}}\subseteq C^*.
\tag{6.1}
\]
The product functional \(\varphi\otimes\psi\) on \(C\) is specified by
\((\varphi\otimes\psi)(a\otimes b)=\varphi(a)\psi(b)\).
Here \(\odot\) means the algebraic span, and the closure uses the bounded-functional norm on the minimal C\*-product. No assertion about a Banach projective tensor norm is being made.

**Theorem 6.1.** There is a unique central projection \(z\in U=C^{**}\) such that, under \(U_*=C^*\),
\[
E=U_*z=\{F\in U_*:F(X)=F(zX)\text{ for all }X\in U\}.
\tag{6.2}
\]
The dual \(E^*\) is canonically the von Neumann algebra \(Uz\). The map
\[
\iota:C\longrightarrow Uz,\qquad c\longmapsto z j_C(c)
\tag{6.3}
\]
is an isometric \*-homomorphism with ultraweakly dense range. For any faithful normal nondegenerate representations \(\pi_M,\pi_N\), its product representation extends uniquely to a normal isomorphism
\[
\Theta:Uz\longrightarrow
P=\pi_M(M)\bar\otimes\pi_N(N),
\quad
\Theta\iota(a\otimes b)=\pi_M(a)\otimes\pi_N(b).
\tag{6.4}
\]
Thus \(Uz\), with predual \(E\), is the intrinsic von Neumann tensor product.

**Proof.** Use faithful normal concrete realizations of the two factors and their spatial action. The faithful minimal-product theorem gives an isometric nondegenerate representation \(\pi_0:C\to B(H_M\otimes H_N)\), whose image has bicommutant \(P\). Theorem 10.1(1–3) of *Spatial tensor products* proves that restriction is an isometry
\[
R:P_*\longrightarrow C^*,\qquad R\rho=\rho\pi_0,
\tag{6.5}
\]
and that its range is precisely \(E\). The density assertion follows by approximating both vectors in a normal vector coefficient by finite sums of elementary tensors, then using norm convergence of the coefficient functionals and of the normal vector series. The norm assertion uses bounded Kaplansky approximation in \(\pi_0(C)\). Completeness of \(P_*\) makes its isometric image closed. These arguments apply to arbitrary Hilbert spaces; they do not select a countable set of vectors spanning either space.

By the declared universal-extension theorem, \(\pi_0\) extends to a normal onto \*-homomorphism
\[
\overline\pi_0:U\longrightarrow P,
\quad \ker\overline\pi_0=U(1-z),
\quad \Theta=\overline\pi_0|_{Uz}:Uz\xrightarrow{\cong}P,
\tag{6.6}
\]
where \(z\) is central and \(\Theta^{-1}\) is normal. The pullback of \(\rho\in P_*\) belongs to \(U_*\) and vanishes on \(U(1-z)\). On \(j_C(C)\), it is \(R\rho\). Since this image is ultraweakly dense in \(U\), the canonical identification \(U_*=C^*\) makes the two functionals equal. Thus \(E\subseteq U_*z\).

Conversely, let \(F\in U_*z\). Restrict it to \(Uz\) and put
\(\rho=F|_{Uz}\circ\Theta^{-1}\). Normality of the inverse gives \(\rho\in P_*\), and (6.6) gives \(F=\rho\overline\pi_0\). Its restriction to \(C\) is therefore in \(R(P_*)=E\). This proves (6.2), including the onto isometry between \(P_*\) and \(E\).

There is also a direct dual identification. Define
\[
Q:U=(C^*)^*\longrightarrow E^*,\qquad QX(F)=F(X).
\]
Every bounded functional on the norm-closed subspace \(E\subseteq C^*\) extends to \(C^*\) by Hahn–Banach, so \(Q\) is onto. Equation (6.2) and separation by \(U_*\) show
\(\ker Q=U(1-z)\). On \(Uz\), its norm is exactly the algebra norm: for \(X=zX\), tests \(F\mapsto Fz\) send the unit ball of \(U_*\) into the unit ball of \(E\), and evaluate at \(X\) with unchanged value. The ordinary dual norm formula gives both inequalities. Hence \(Q|_{Uz}\) is an onto isometry, and its evaluation formula identifies the weak-star topologies. This makes \(E^*\) the algebra \(Uz\) with its specified predual.

For uniqueness of \(z\), the annihilator of \(E\) in \(U\) is \(U(1-z)\). Another central projection satisfying (6.2) would give the same ideal. Its identity \(1-z\) determines the ideal's projection uniquely.

Finally, \(\Theta\iota(c)=\pi_0(c)\); faithfulness of \(\pi_0\) and isometry of \(\Theta\) prove that \(\iota\) is isometric. Multiplication by \(z\) is normal, so the ultraweak density of \(j_C(C)\) gives that of \(\iota(C)\) in \(Uz\). Any two normal extensions in (6.4) agree on this dense subalgebra. The same proof for each pair of faithful normal realizations gives the stated canonical realization. \(\square\)

For example, when \(M=M_r(\mathbb C)\) and \(N=M_s(\mathbb C)\), the space \(C\) is already \(M_{rs}(\mathbb C)\), all its functionals are normal, and \(z=1\). In contrast, take \(M=\ell^\infty(\mathbb N)\) with its diagonal action and \(N=\mathbb C\). Then \(C=M\) and \(E=\ell^1(\mathbb N)\). The limit functional on the subspace of convergent sequences has a norm-one Hahn–Banach extension \(F\in C^*\). It satisfies \(F(e_n)=0\) for every coordinate vector and \(F(1)=1\). A functional represented by an \(\ell^1\) sequence and vanishing on every \(e_n\) would be zero. Hence \(F\notin E\), so \(E\ne U_*\) and \(z\ne1\). The intrinsic product is the normal central summand of this larger universal algebra.

**Corollary 6.2.** Isomorphisms \(\alpha:M_1\to M_2\), \(\beta:N_1\to N_2\) of von Neumann algebras induce a unique normal isomorphism
\[
\alpha\bar\otimes\beta:M_1\bar\otimes N_1
\longrightarrow M_2\bar\otimes N_2
\]
with the prescribed elementary-tensor values.

**Proof.** Both leg isomorphisms and their inverses are positive order isomorphisms. They preserve every bounded increasing positive supremum: pull any candidate upper bound back through the inverse and use the least-upper-bound property. The declared positive-map normality criterion therefore makes all four maps normal. Corollary 8.4 of *Spatial tensor products* constructs their normal tensor maps; composing the tensor maps for the legs and their inverses is the identity on algebraic tensors and hence, by normality and density, everywhere. Theorem 6.1 identifies these concrete maps with the intrinsic product. Uniqueness uses the same density. \(\square\)

The amplification and common-corner constructions are proved in Theorem 8.2 and Corollary 8.3 of *Spatial tensor products*. Positive normal functionals are represented there by single vectors after amplification.

### 6.3. The finite scalar normality step

**Lemma 6.3.** Let \(M\subseteq B(H)\) be a von Neumann algebra and \(\omega\in M^*\) a bounded positive functional. Then \(\omega\) is ultraweakly continuous if and only if it preserves suprema of every bounded increasing positive net.

We use the complete-additivity theorem, Corollary 11.5 of [The universal enveloping von Neumann algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-18). Its proof uses the normal–singular splitting in Section 10 and the singular zero-projection theorem in Section 11. The splitting comes from the normal extension of the identity representation to the universal bidual, together with its normal inverse on the complementary central summand. That inverse is supplied by the separate bidual theorem above; no automatic-normality theorem is used to construct it.

**Proof.** A bounded increasing positive net \(a_i\uparrow a\) converges ultraweakly to \(a\), so an ultraweakly continuous positive \(\omega\) has \(\omega(a_i)\uparrow\omega(a)\).

For the converse, let \((p_j)_{j\in J}\) be any orthogonal family of projections, and let \(p=\bigvee_jp_j\). The finite sums \(p_F=\sum_{j\in F}p_j\), indexed by finite subsets \(F\subseteq J\), form a bounded increasing positive net with supremum \(p\). The assumed order continuity gives
\[
 \omega(p)=\sup_{F\subseteq J\text{ finite}}\omega(p_F)
          =\sum_{j\in J}\omega(p_j).
\]
Thus \(\omega\) is completely additive on arbitrary orthogonal projection families. The existing complete-additivity theorem now gives \(\omega\in M_*\). This includes \(\omega=0\), the zero algebra and arbitrary Hilbert-space dimension. \(\square\)

The concrete predual facts are Theorems 9.1(ii) and 9.4 of [Operator spaces and preduals](../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#OA-FND-LT-10): every ultraweakly continuous functional on \(M\) extends normally to \(B(H)\), the quotient norm is its functional norm, and \(M=(M_*)^*\). Proposition 6.3(c) of [the same lesson](../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#OA-FND-LT-07) writes that extension as a combination of four positive normal functionals. Restriction therefore proves that positive normal functionals span \(M_*\). Vector functionals detect positivity in the concrete representation.

Use Lemma 6.3 for each bounded positive scalar functional \(\psi\circ T\) in the positive-map criterion. The preadjoint and positive-spanning arguments in *Normal positive maps and their preadjoints* then apply exactly as written, with the concrete predual facts just identified. Only the scalar step's proof is replaced; no assertion about an infinite-valued weight is needed. In particular, this route justifies the normality used in Corollary 6.2.

### 6.4. States, cyclic vectors and bounded approximation

The universal extension used in Theorem 6.1 starts with three facts about an arbitrary C\*-algebra \(A\).

1. **States and the full bounded dual.** If \(A\ne0\), every \(a\in A_+\) has a state \(\omega\) with \(\omega(a)=\|a\|\). Every bounded functional has the form
   \[
     f=(p_1-p_2)+i(p_3-p_4),\qquad p_j\in A^*_+,
     \qquad \sum_{j=1}^4\|p_j\|\le2\|f\|.
   \]
   Sections 2–7 of [States detect the norm and positive functionals span the dual](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-01) prove both facts. The signed convex hull of the compact unital state set is the real dual unit ball, by Hahn–Banach separation and the state norm formula. The nonunital case passes through a unitization; its state set itself need not be weak-star compact. Proposition 3.4 of [Banach algebras and spectrum](../../foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#OA-FND-BN-05) constructs the needed C\*-unitization from the original norm, without states or a universal representation. Remark 8.4 of [Continuous functional calculus](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-15) identifies the inherited positive cone. For an already unital algebra, the unital proof applies directly. The zero algebra has only the zero functional and is handled separately.
2. **Cyclic vectors without an identity.** Construction 5.1 and Theorems 5.3–5.5 of [Representations and positive functionals](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#OA-FND-GN-05) give, for every bounded positive \(\omega\), a nondegenerate cyclic representation and a vector with
   \[
     \omega(a)=\langle\pi_\omega(a)\xi_\omega,\xi_\omega\rangle,
     \qquad \|\xi_\omega\|^2=\|\omega\|.
   \]
   An approximate identity of positive contractions gives the representing vector as the limit of its quotient vectors. Theorem 11.4 and Corollary 11.5(1) of [Continuous functional calculus](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-19) provide that approximate identity for every C\*-algebra, with no countability assumption. The state representations may therefore be summed over all states. The first fact makes this universal representation faithful and lets every bounded functional extend as a normal vector-functional combination.
3. **Approximation with the norm bound retained.** Theorem 7.1 of [Density theorems](../../foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html#oa-fnd-kd-07) proves strong-star density of the contractions of a \*-subalgebra in the contractions of its weak closure. It includes nonunital and degenerate algebras. For a nondegenerate representation, the double-commutant theorem identifies that weak closure with \(\pi(A)''\). The approximating net is bounded explicitly, so it also converges ultraweakly by Lemma 1.1(3) of the density lesson. This is the approximation used to prove that restriction of the concrete predual is isometric and that the normal extension maps the relevant central-corner unit ball onto the target unit ball.

These facts concern different spaces: positive functionals span the full dual \(A^*\) in the universal construction, while the positive **normal** functionals in Section 6.3 span the specified predual \(M_*\). The normal inverse is then obtained by the preadjoint argument; its construction does not use the scalar automatic-normality criterion.

### 6.5. Corners, supports and normal cyclic representations

The remaining concrete inputs can be read without using a theorem about general normal weights. We record exactly how their existing proofs apply.

**Corner preduals.** Let \(M\subseteq B(H)\) be a von Neumann algebra and \(p\in M\) any projection, including zero. Regard \(N=pMp\) as an algebra on \(pH\). Section 11 of [Concrete preduals from Hilbert tensors](../reader/supplements/concrete-preduals-corners.html#OA-MOD-CP-11) proves that its ultraweak topology is the inherited topology and that
\[
 r:M_*\longrightarrow N_*,\qquad r(f)=f|_N,
 \qquad
 s:N_*\longrightarrow M_*,\qquad s(g)(x)=g(pxp)
\]
are positive contractions with \(rs=1\) and \(s\) isometric. Thus
\[
 N_*\cong M_*/\ker r
 \cong\{f\in M_*:f(x)=f(pxp)\text{ for every }x\in M\}.
\]
The second identification is the map \(s\), rather than an unspecified identification of a quotient with a subspace. The proof extends each square-summable vector series from \(pH\) by zero and compresses both vector sequences when restricting from \(H\). It proves continuity on the entire algebra, with no uniform-bound assumption on an arbitrary convergent net. Centrality of \(p\) is unnecessary. This supplies the corner input in the preadjoint proof of the normal inverse used in Section 6.

**Supports and central kernels.** Section 6 of [Bounded operators needed for comparing weights](../../OA-MOD/OA-MOD-BK.html#supports-from-bounded-resolvent-cutoffs) proves, using only bounded continuous functional calculus and Hilbert-space geometry, that for \(b\in M_+\)
\[
 b(b+\varepsilon1)^{-1}\uparrow s(b)
 \quad\text{strongly and ultraweakly as }\varepsilon\downarrow0,
 \qquad
 s(b)H=\overline{bH}.
\]
Its [Section 4](../../OA-MOD/OA-MOD-BK.html#bounded-increasing-positive-nets-have-strong-suprema) proves bounded increasing-net convergence, including the supremum of arbitrary finite joins of projections. Its [Section 8](../../OA-MOD/OA-MOD-BK.html#testing-commutation-on-unitaries) proves that commutation with all unitaries implies commutation with the entire algebra. These are exactly the support, supremum and centrality inputs in Section 7 of [Every bounded functional becomes normal in one representation](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-05), which identifies an ultraweakly closed two-sided star ideal as \(Mz\) for a central projection \(z\). That proof does not identify the support of a positive functional with the central projection of a representation kernel.

For a bounded positive normal functional \(\omega\), Sections 4–5 of [Finite domains, null directions and support corners](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#state-support-and-continuity-tools) give the largest projection \(q\) with \(\omega(q)=0\). With \(p=1-q\), they prove
\[
 \omega(x)=\omega(pxp)\quad(x\in M),\qquad
 \omega|_{pMp}\text{ is faithful}.
\]
Here the finite-domain projection in that text is \(1\), because every positive element has finite value under a bounded functional. Its finite-domain cutoff construction is therefore unnecessary for this application. The null-projection proof uses the bounded resolvent cutoffs above, finite joins and their increasing net; normality gives zero value on the supremum. The compression identity is first proved on positive elements and then extends by linearity. The functional is normal on the corner by the inherited topology just established. If \(\omega=0\), its support is zero. Otherwise its corner restriction has norm \(\omega(1)=\omega(p)>0\) and can be normalized to a faithful normal state. The support \(p\) need not be central.

**Normality of bounded GNS.** The cyclic construction in Section 6.4 applies to \(\omega\). Section 7 of [General weights: finite domains, GNS spaces and normal representations](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-19) contains the required increasing-net argument. In the bounded case its GNS vectors come from all of \(M\). If \(0\leq a_i\uparrow a\), then for each \(x\in M\)
\[
 \omega(x^*a_i x)\uparrow\omega(x^*a x),
 \qquad
 \|\pi_\omega(a-a_i)\pi_\omega(x)\xi_\omega\|^2
 \leq\|a\|\bigl[\omega(x^*a x)-\omega(x^*a_i x)\bigr]
 \longrightarrow0.
\]
The bound \(\|\pi_\omega(a-a_i)\|\leq\|a\|\) and density extend convergence to every GNS vector. Hence \(\pi_\omega(a_i)\uparrow\pi_\omega(a)\) strongly. No sequence is extracted from the original net.

For this bounded application, the last normal-map criterion in that proof can be supplied by Lemma 6.3. For each vector \(\eta\), the bounded positive functional
\[
 a\longmapsto\langle\pi_\omega(a)\eta,\eta\rangle
\]
preserves bounded increasing suprema, and is therefore ultraweakly continuous by that lemma. Polarization gives the same conclusion for mixed vector coefficients. A square-summable vector-series functional on \(B(H_\omega)\), composed with the contractive \(\pi_\omega\), is a norm-convergent sum of these normal coefficients. The norm-closed predual in Theorem 9.4 of the operator-spaces lesson contains its limit. Testing all such series proves global ultraweak continuity of \(\pi_\omega\). Thus this selected GNS argument uses the finite scalar criterion, rather than a recovery theorem for an extended-valued weight.

On the support corner \(pMp\), this normal GNS representation is faithful: \(\pi_\omega(x)=0\) implies \(\omega(x^*x)=0\), and corner faithfulness gives \(x=0\). It is consequently isometric. Its unit ball is the ultraweakly compact image of the corner unit ball. Contractive density from Section 6.4 then shows that its image equals its bicommutant. The direct preadjoint argument in Section 8 of the universal-extension lesson applies to this onto isometric normal map and proves that its inverse is normal. In particular, a normal functional on the support corner remains normal when transported to this GNS realization. These are the representation and corner facts used when approximating dominated functionals in Lemma 3.2 of the ergodic-projection lesson.

### 6.6. Faithful normal images and positive vector series

The same compact-ball argument applies beyond the cyclic representation. Let \(\pi:M\to B(K)\) be a faithful normal star homomorphism, put \(p=\pi(1)\), and work on \(K_0=pK\). The identity of its image is \(p|_{K_0}=I_{K_0}\). Faithfulness makes \(\pi\) isometric, so \(\pi(M)\) is a norm-closed unital C\*-algebra on \(K_0\).

Banach–Alaoglu makes \(M_1\) ultraweakly compact. Normality makes \(\pi(M_1)\) compact in the ultraweak topology of \(B(K_0)\), hence compact and closed in its Hausdorff weak operator topology. Contractive density from Section 6.4 gives, for each contraction in \(\pi(M)''\) on \(K_0\), a strongly convergent net of contractions in \(\pi(M)\). Isometry says that these are precisely elements of \(\pi(M_1)\). Their weak operator limit remains in that closed set. Thus \(\pi(M)=\pi(M)''\) on \(K_0\): the image is a von Neumann algebra \(N\).

Here is also the normal-inverse argument, in the form needed to transport functionals. The concrete preduals in [Concrete preduals from Hilbert tensors](../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#OA-FND-LT-10) give
\[
 \pi_*:N_*\longrightarrow M_*,\qquad \pi_*f=f\circ\pi.
\]
Since \(\pi\) maps the unit ball onto the unit ball isometrically, \(\pi_*\) is an isometry. Its range is norm closed. An element \(x\in M=(M_*)^*\) annihilating that range satisfies \(f(\pi(x))=0\) for every \(f\in N_*\), hence \(\pi(x)=0\) and \(x=0\). Hahn–Banach therefore makes the range all of \(M_*\). The adjoint of \(\pi_*^{-1}\) is \(\pi^{-1}\), proving global ultraweak continuity of the inverse. This is the direct argument of [the universal-extension proof](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-02). In particular, \(\omega\circ\pi^{-1}\in N_*^+\) whenever \(\omega\in M_*^+\).

Apply the supplied [positive normal vector-series proof](../reader/supplements/spatial-tensor-products.html#3-normal-functionals-and-the-amplification) to this transported functional. It gives \(v_j\in K_0\), for \(j\geq1\), with
\[
 \omega(x)=\sum_{j\geq1}\langle\pi(x)v_j,v_j\rangle,
 \qquad \sum_{j\geq1}\|v_j\|^2=\omega(1).
\]
Every summand is positive normal and is dominated by \(\omega\); the series is absolutely convergent. The existing proof first dominates the functional by a vector sum using Section 8 of the concrete-predual text. On the resulting cyclic subspace it represents the dominated positive form by a positive contraction in the commutant, then applies its square root to the cyclic vector. Thus this particular vector-series input uses bounded forms and continuous functional calculus. It does not require a construction for extended-valued weights. The countable index belongs to one functional; it gives no countable separating family for \(M\), and places no separability condition on \(K\). For \(\omega=0\), take all \(v_j=0\).

The range unit matters throughout. For example, \(\pi:\mathbb C\to B(\mathbb C^2)\), \(\pi(\lambda)=\operatorname{diag}(\lambda,0)\), is faithful and normal. Its image is a von Neumann algebra on \(p\mathbb C^2\), extended by zero on the orthogonal complement. Its bicommutant on all of \(\mathbb C^2\) also contains the ambient identity and is larger. Continuous functional calculus is natural in the image corner with unit \(p\): for the constant function \(g=1\), \(\pi(g(1))=p\). Calculus with the ambient unit would instead give \(I_2\). Accordingly, whenever this lesson uses functional-calculus naturality from the universal-enveloping prerequisite, it uses unital maps or the stated range corner; an ambient degenerate map requires functions vanishing at zero. The zero algebra and zero range are included by the same corner convention.

## 7. Why tensor norms and normal tensor products developed together

### 7.1. A completion records more than the algebraic tensor

The algebraic tensor product specifies how bilinear expressions combine. A norm specifies which infinite limits are admitted. Schatten's paper [Schatten] develops tensor norms for Banach spaces; [Blackadar, I.8.6–I.8.7] treats the dualities between compact, trace-class and bounded operators and the Schatten ideals. Grothendieck's account [Grothendieck] describes topological tensor products and nuclear spaces. The finite-dimensional example below already distinguishes three cross norms, although they define the same topology in each fixed finite dimension. Their definitions and bounds are proved in the linked programme lesson.

For example, on \(\mathbb C^d\odot\mathbb C^d\), with the Euclidean norm on both factors, put \(w_d=\sum_{j=1}^d e_j\otimes e_j\). The injective Banach norm is \(1\): its definition tests \(\sum_j f(e_j)g(e_j)\) over two dual unit balls, and Cauchy–Schwarz gives the upper bound, attained by the first coordinate functionals. The projective Banach norm is \(d\). The displayed decomposition gives the upper bound; the bilinear form \(b(x,y)=\sum_jx_jy_j\) has norm \(1\) and evaluates to \(d\) on \(w_d\), giving the lower bound. The Hilbert tensor norm is \(\sqrt d\), since the \(e_j\otimes e_j\) are orthonormal. Thus the three norms agree on elementary tensors and give different values on their sums. The Banach cross-norm definitions and their bounds are proved in Theorem 2.3 of [Tensor products of Hilbert spaces and operators](../reader/supplements/banach-tensor-cross-norms.html#banach-tensor-cross-norms). No identification of these Banach norms with the minimal or maximal C\*-tensor norms is intended.

### 7.2. Commuting factors need not split normally

A nonzero factor \(M\subseteq B(H)\) admits a spatial decomposition
\[
 H\cong H_1\otimes H_2,\qquad
 M=B(H_1)\otimes1,\qquad M'=1\otimes B(H_2)
\]
exactly when it is of type I. Here is the specialization of [Theorem 11.4, the spatial form of a type I algebra](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-15). In that theorem the factor's centre is scalar, so just one central summand survives. Its abelian matrix-entry algebra must be scalar as well. Since that abelian algebra is maximal abelian on its Hilbert space \(K\), \(B(K)=\mathbb C1\), and \(\dim K=1\). The theorem therefore gives the displayed tensor model. Conversely, \(B(H_1)\otimes1\) is of type I: a rank-one projection in the first leg gives a nonzero abelian corner, and unitary conjugation preserves this property. Proposition 7.1 of *Spatial tensor products* computes its commutant, and Theorem 5.2(5) shows that the two legs generate \(B(H_1\otimes H_2)\).

More generally, suppose a spatial decomposition puts \(M=P\otimes1\) and \(M'=1\otimes Q\) for von Neumann algebras \(P\subseteq B(H_1)\), \(Q\subseteq B(H_2)\). Since \((M\cup M')'=Z(M)=\mathbb C1\), the two legs generate \(B(H_1\otimes H_2)\), so \(P\bar\otimes Q=B(H_1\otimes H_2)\). Slicing \(x\otimes1\), for arbitrary \(x\in B(H_1)\), by a normal state of \(B(H_2)\) gives \(x\in P\); hence \(P=B(H_1)\), and similarly \(Q=B(H_2)\). This proves that separate spatial legs force the same type I model.

For general commuting factors, algebraic injectivity of multiplication still holds, while its extension to the normal spatial product needs the extra condition in Theorem 2.1. The irrational-period example in Section 4 separates the C\*-product from the normal product even for abelian algebras. The free author edition [Blackadar, III.1.5.3–III.1.5.10] discusses the type I and tensor-product setting.

### 7.3. Minimal, maximal and normal products

The minimal product is computed by separate faithful representations on a Hilbert tensor product; the maximal product organizes all pairs of commuting representations. The proofs in *Tensor norms and independent systems* and *States, ideals and the smallest tensor norm* establish their universal properties and minimality, including nonunital algebras. Freely readable early papers include the spatial constructions of Turumaru [Turumaru I; Turumaru III], the maximal construction of Guichardet [Guichardet], and Takesaki's results on cross norms [Takesaki, cross norms]. The free-group example proves that the minimal and maximal norms can differ. A C\*-algebra is called nuclear when these norms agree against every C\*-algebra; nuclearity is a further topic, not an assumption in the proofs here.

Misonou's paper [Misonou] studies tensor products of W\*-algebras. Takeda's representation paper [Takeda] and Sakai's characterization [Sakai, characterization] give related freely readable foundations. Theorem 6.1 describes the intrinsic construction: the closed span of the factor preduals selects the central summand of the universal bidual carrying the normal product functionals. It need not select the whole universal algebra. The amplification and induction theorem in *Spatial tensor products* uses a different projection, in a concrete commutant. The central projection selecting the intrinsic product and this commutant projection have distinct roles.

### 7.4. Positivity and the full commutation theorem

Stinespring's dilation theorem [Stinespring] supplies the representation used for completely positive tensor maps. The transpose examples in *Tensor norms and independent systems* show why positivity alone is insufficient. Theorem 1.1 constructs the normal CP tensor map: its preadjoint preserves the product predual, and bounded matrix approximation proves complete positivity of the normal extension.

The identity \((M\bar\otimes N)'=M'\bar\otimes N'\) requires a further argument. The free author edition [Blackadar, III.4.5.8] gives a modular-theoretic route. Rieffel and van Daele [Rieffel–van Daele] develop the real-subspace viewpoint on operator algebras and their commutants. The proof in [Theorem 11.4 of Spatial tensor products](../reader/supplements/spatial-tensor-products.html#11-the-commutation-theorem-and-its-consequences) uses real-orthogonal cyclic density, a real tensor-density lemma and compression to cyclic corners. The last step tests elementary tensor vectors and polarizes separately in both factors. These compressions allow arbitrary Hilbert spaces without semifiniteness or a countable cyclic decomposition. The intersection, centre and tensor-MASA formulas follow from the commutation theorem.

## References

- [Stinespring] W. F. Stinespring, [“Positive functions on C\*-algebras,”](https://www.ams.org/journals/proc/1955-006-02/S0002-9939-1955-0069403-4/S0002-9939-1955-0069403-4.pdf) *Proceedings of the American Mathematical Society* **6** (1955), 211–216.
- [Schatten] R. Schatten, [“On the direct product of Banach spaces,”](https://www.ams.org/journals/tran/1943-053-02/S0002-9947-1943-0007568-7/S0002-9947-1943-0007568-7.pdf) *Transactions of the American Mathematical Society* **53** (1943), 195–217.
- [Blackadar] B. Blackadar, [*Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*](https://bruceblackadar.com/Mathematics/Cycr.pdf), revised author edition, 8 February 2017.
- [Grothendieck] A. Grothendieck, [“Résumé des résultats essentiels dans la théorie des produits tensoriels topologiques et des espaces nucléaires,”](https://www.numdam.org/item/10.5802/aif.46.pdf) *Annales de l'Institut Fourier* **4** (1952), 73–112.
- [Turumaru I; Turumaru III] T. Turumaru, “On the direct-product of operator algebras,” [I](https://www.jstage.jst.go.jp/article/tmj1949/4/3/4_3_242/_pdf), *Tôhoku Mathematical Journal* **4** (1952), 242–251; [III](https://www.jstage.jst.go.jp/article/tmj1949/6/2-3/6_2-3_208/_pdf), **6** (1954), 208–211.
- [Guichardet] A. Guichardet, [“Tensor products of C\*-algebras,”](https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&paperid=30719&what=fullt&option_lang=eng) *Doklady Akademii Nauk SSSR* **160** (1965), 986–989.
- [Takesaki, cross norms] M. Takesaki, [“A note on the cross-norm of the direct product of operator algebras,”](https://www.jstage.jst.go.jp/article/kodaimath1949/10/3/10_3_137/_pdf) *Kodai Mathematical Seminar Reports* **10** (1958), 137–140; [“On the cross-norm of the direct product of C\*-algebras,”](https://www.jstage.jst.go.jp/article/tmj1949/16/1/16_1_111/_pdf) *Tôhoku Mathematical Journal* **16** (1964), 111–122.
- [Misonou] Y. Misonou, “On the direct product of W\*-algebras,” *Tôhoku Mathematical Journal* **6** (1954), 189–204. [Journal](https://www.jstage.jst.go.jp/article/tmj1949/6/2-3/6_2-3_189/_article/-char/en).
- [Takeda] Z. Takeda, “On the representations of operator algebras, II,” *Tôhoku Mathematical Journal* **6** (1954), 212–219. [Journal](https://www.jstage.jst.go.jp/article/tmj1949/6/2-3/6_2-3_212/_article/-char/en).
- [Sakai, characterization] S. Sakai, [“A characterization of W\*-algebras,”](https://msp.org/pjm/1956/6-4/pjm-v6-n4-p11-s.pdf) *Pacific Journal of Mathematics* **6** (1956), 763–773.
- [Rieffel–van Daele] M. A. Rieffel and A. van Daele, [“A bounded operator approach to Tomita–Takesaki theory,”](https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf) *Pacific Journal of Mathematics* **69** (1977), 187–221.
