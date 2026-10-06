<span id="a-faithful-weight-on-the-gns-commutant"></span>
# A faithful weight on the GNS commutant

<span id="oa-mod-ow-01-setting-domains-and-existing-inputs"></span>
<span id="OA-MOD-OW-01"></span>
<span id="oa-mod-ow-01"></span>
## OA-MOD-OW-01. Setting, domains, and existing inputs

Let \(M\) be an arbitrary von Neumann algebra and let \(\varphi:M_+\to[0,\infty]\) be a **normal semifinite** weight, not necessarily faithful. We use the density convention for semifiniteness:
\[
\mathfrak n_\varphi=\{x\in M:\varphi(x^*x)<\infty\},\qquad
\mathfrak m_\varphi=\operatorname{span}\{y^*x:x,y\in\mathfrak n_\varphi\},
\]
and \(\mathfrak m_\varphi\) is ultraweakly dense in \(M\). Inner products are linear in the first variable. Write
\[
(H,\pi,\Lambda)=(H_\varphi,\pi_\varphi,\Lambda_\varphi),
\qquad N=\pi(M)'\subseteq B(H).
\]
The map \(\Lambda\) has domain exactly \(\mathfrak n_\varphi\). It need not be injective. Every bounded operator on \(H\) has domain all of \(H\); membership in \(N\) means commutation with every \(\pi(a)\), \(a\in M\).

The unit uses these already written course results with their own foundation status retained:

- **WG-003–007:** finite domains and their positive cone, the GNS construction, and normality of \(\pi\) when \(\varphi\) is normal. In particular \(\mathfrak m_\varphi^+=\{a\in M_+:\varphi(a)<\infty\}\).
- **WG-008:** an increasing net of positive contractions \(e_\alpha\in\mathfrak m_\varphi^+\), with \(e_\alpha\uparrow1\). Its convergence is strong and ultraweak. It is not replaced by a sequence or by an asserted increasing net of finite-weight projections.
- **DW-02–04:** bounded factorization inside a von Neumann algebra, the commutant/form correspondence, and the comparison operator with its exact range closure and polar intertwining.
- **NW-11:** for any normal weight, recovery as the pointwise supremum of dominated positive normal functionals; and, for any weight, equivalence of normality with preservation of arbitrary summable positive families. These are weight theorems, not an application of a bounded-map continuity theorem to an infinite-valued function.
- **BK-03–07:** bounded strong-to-ultraweak convergence, bounded monotone nets, inverse order, support cutoffs, and rectangular polar decomposition.
- **NW-DEP-DUAL and WG-001:** the predual is a Banach space, its positive cone is norm closed, a positive normal functional has norm equal to its value at the identity, and normal bounded representations preserve bounded increasing positive suprema. Composition of a normal representation with a vector functional is normal.

The predual norm fact used below can also be read directly from positivity: the bounded-functional Cauchy–Schwarz inequality gives
\(|\omega(a)|^2\leq\omega(a^*a)\omega(1)\leq\|a\|^2\omega(1)^2\), while evaluation at \(1\) gives the reverse norm inequality. Consequently norms add on positive functionals.

<a id="OA-MOD-OW-02"></a>
<span id="oa-mod-ow-02-what-a-comparison-operator-remembers"></span>
<span id="oa-mod-ow-02"></span>
## OA-MOD-OW-02. What a comparison operator remembers

Put
\[
\mathcal E_\varphi
=\{\omega\in M_*^+:\omega\leq c\varphi
\text{ on }M_+\text{ for some finite }c\geq0\},
\qquad
\Phi_\varphi=\{\omega\in M_*^+:\omega\leq\varphi\}.
\]
The extended-value convention is \(0\cdot\infty=0\); hence comparison with \(c=0\) requires \(\omega=0\). Equivalently \(\mathcal E_\varphi\) is the union of the positive scalar multiples of \(\Phi_\varphi\), together with zero. It is an additive cone.

By DW-03, every \(\omega\in\mathcal E_\varphi\) determines a unique
\(h_\omega\in N_+\) such that
\[
\omega(y^*x)=\langle h_\omega\Lambda(x),\Lambda(y)\rangle
\qquad(x,y\in\mathfrak n_\varphi).
\tag{OW1}
\]
This is initially a correspondence with the restriction of \(\omega\) to \(\mathfrak m_\varphi\). The next argument proves the stronger uniqueness needed here.

**Proposition.** The map \(\omega\mapsto h_\omega\) is additive, positively homogeneous, injective, and reflects order on \(\mathcal E_\varphi\). Furthermore
\[
\omega\leq c\varphi\quad\Longleftrightarrow\quad h_\omega\leq cI_H
\qquad(c\geq0),
\tag{OW2}
\]
so the least possible comparison constant is \(\|h_\omega\|\).

**Proof.** Additivity and homogeneity follow from (OW1) and density of \(\Lambda(\mathfrak n_\varphi)\). Suppose \(h_\omega\leq h_\rho\). For every \(a\in\mathfrak m_\varphi^+\), substitute \(x=y=a^{1/2}\) into (OW1) to obtain \(\omega(a)\leq\rho(a)\).

To extend this inequality, let \(a\in M_+\) be arbitrary. The cutoffs of WG-008 satisfy
\[
0\leq e_\alpha a e_\alpha\leq\|a\|e_\alpha^2
\leq\|a\|e_\alpha.
\]
Thus \(e_\alpha a e_\alpha\in\mathfrak m_\varphi^+\). This norm-bounded net converges strongly and ultraweakly to \(a\), although it need not be increasing. Normality of the bounded functionals gives
\[
\omega(a)=\lim_\alpha\omega(e_\alpha a e_\alpha)
\leq\lim_\alpha\rho(e_\alpha a e_\alpha)=\rho(a).
\]
Hence the map reflects order. The forward order implication follows directly from quadratic forms in (OW1). Applying order reflection in both directions proves injectivity.

The forward implication of (OW2) is the operator bound in DW-03. Conversely, \(h_\omega\leq cI_H\) gives \(\omega(a)\leq c\varphi(a)\) whenever \(\varphi(a)<\infty\), by taking \(x=a^{1/2}\). For \(c>0\), the remaining infinite-weight values impose no restriction. For \(c=0\), one has \(h_\omega=0=h_0\), so injectivity gives \(\omega=0\); the required global inequality then holds with the stated convention. This proves (OW2), including the zero constant. The norm of a positive operator is its least scalar upper bound. ∎

There are two different norms in this construction. The operator norm \(\|h_\omega\|\) measures how strongly \(\omega\) is dominated by \(\varphi\). The functional norm \(\|\omega\|=\omega(1)\) will be the value of the opposite weight at \(h_\omega\). They are generally unequal.

<a id="OA-MOD-OW-03"></a>
<span id="oa-mod-ow-03-the-vector-implementing-a-finite-observation"></span>
<span id="oa-mod-ow-03"></span>
## OA-MOD-OW-03. The vector implementing a finite observation

Let \((H_\omega,\pi_\omega,\Omega_\omega)\) be the bounded-functional GNS construction for \(\omega\in\mathcal E_\varphi\). The vector has norm \(\|\Omega_\omega\|^2=\omega(1)\), including \(H_0=\{0\}\). DW-04 supplies the bounded map
\[
C_\omega:H\to H_\omega,
\qquad C_\omega\Lambda(x)=\pi_\omega(x)\Omega_\omega,
\quad x\in\mathfrak n_\varphi,
\]
with \(C_\omega^*C_\omega=h_\omega\) and
\(C_\omega\pi(a)=\pi_\omega(a)C_\omega\) for \(a\in M\).

**Proposition.** The range of \(C_\omega\) is dense in \(H_\omega\). If
\[
C_\omega=U_\omega h_\omega^{1/2},\qquad
\eta_\omega=U_\omega^*\Omega_\omega,
\]
then
\[
\|\eta_\omega\|^2=\|\omega\|,\qquad
h_\omega^{1/2}\Lambda(x)=\pi(x)\eta_\omega
\quad(x\in\mathfrak n_\varphi).
\tag{OW3}
\]
The vector \(\eta_\omega\) is the unique vector satisfying the second identity. It also implements the whole functional:
\[
\omega(a)=\langle\pi(a)\eta_\omega,\eta_\omega\rangle
\qquad(a\in M).
\tag{OW4}
\]

**Proof.** Every cutoff \(e_\alpha\) belongs to \(\mathfrak n_\varphi\). Since \(\omega\) is normal,
\[
\|\pi_\omega(e_\alpha)\Omega_\omega-\Omega_\omega\|^2
=\omega((1-e_\alpha)^2)
\leq\omega(1-e_\alpha)\longrightarrow0.
\]
Thus \(\Omega_\omega\) belongs to the closure of the range of \(C_\omega\). That closed subspace is invariant under \(\pi_\omega(M)\) by the intertwining identity. Since \(\Omega_\omega\) is cyclic, the subspace is all of \(H_\omega\).

Consequently the polar partial isometry satisfies \(U_\omega U_\omega^*=I_{H_\omega}\); it is not asserted that \(U_\omega^*U_\omega=I_H\). The latter is \(s(h_\omega)\). Polar intertwining from DW-04 gives
\[
U_\omega^*\pi_\omega(a)=\pi(a)U_\omega^*.
\]
It follows that
\[
\begin{aligned}
\pi(x)\eta_\omega
&=U_\omega^*\pi_\omega(x)\Omega_\omega
=U_\omega^*C_\omega\Lambda(x)\\
&=s(h_\omega)h_\omega^{1/2}\Lambda(x)
=h_\omega^{1/2}\Lambda(x).
\end{aligned}
\]
Also
\(\|\eta_\omega\|^2
=\langle U_\omega U_\omega^*\Omega_\omega,\Omega_\omega\rangle
=\|\Omega_\omega\|^2\).
The same coisometry and intertwining identities give (OW4):
\[
\langle\pi(a)U_\omega^*\Omega_\omega,U_\omega^*\Omega_\omega\rangle
=\langle\pi_\omega(a)\Omega_\omega,\Omega_\omega\rangle.
\]

For uniqueness, if \(\pi(x)\eta=\pi(x)\zeta\) for all \(x\in\mathfrak n_\varphi\), apply it to \(e_\alpha\). Since \(\pi\) is normal, \(\pi(e_\alpha)\uparrow I_H\) strongly. Passing to this strong limit gives \(\eta=\zeta\). ∎

The density of \(C_\omega\)'s range is where semifiniteness repairs a potential loss of norm. Without that density, the polar factor only gives \(\|U_\omega^*\Omega_\omega\|\leq\|\Omega_\omega\|\), which is insufficient to define a weight by \(\|\omega\|\).

<a id="OA-MOD-OW-04"></a>
<span id="oa-mod-ow-04-a-hereditary-cone-in-the-commutant"></span>
<span id="oa-mod-ow-04"></span>
## OA-MOD-OW-04. A hereditary cone in the commutant

Define
\[
P_\varphi=\{h_\omega:\omega\in\mathcal E_\varphi\}\subseteq N_+.
\]

**Proposition.** This is an additive hereditary cone: if \(0\leq h\leq k\) and \(k\in P_\varphi\), then \(h\in P_\varphi\). The assignment
\[
f(h_\omega)=\|\omega\|
\]
is well-defined, additive, positively homogeneous, and increasing on \(P_\varphi\).

**Proof.** Injectivity in OW-02 makes \(f\) well-defined. Additivity and positive homogeneity of the correspondence, together with \(\|\omega\|=\omega(1)\), prove the analogous properties of \(f\).

Suppose \(0\leq h\leq h_\omega\). Apply the bounded factorization DW-02 inside the von Neumann algebra \(N\) to obtain a contraction \(s\in N\) such that
\[
h^{1/2}=s h_\omega^{1/2}.
\]
Define the positive functional
\[
\rho(a)=\langle\pi(a)s\eta_\omega,s\eta_\omega\rangle
\qquad(a\in M).
\]
It is bounded, and normality of \(\pi\) makes it normal. For \(x\in\mathfrak n_\varphi\), commutation with \(s\) and (OW3) give
\[
\begin{aligned}
\rho(x^*x)
&=\|\pi(x)s\eta_\omega\|^2
=\|s h_\omega^{1/2}\Lambda(x)\|^2\\
&=\|h^{1/2}\Lambda(x)\|^2
\leq\|h\|\varphi(x^*x).
\end{aligned}
\]
Testing finite-weight \(a\geq0\) with \(x=a^{1/2}\), and taking any strictly positive constant at least \(\|h\|\) for the remaining infinite values, proves \(\rho\in\mathcal E_\varphi\). Polarizing the equality of quadratic forms proves \(h_\rho=h\). Thus \(P_\varphi\) is hereditary.

Finally OW-02 reflects order, so \(h_\rho\leq h_\omega\) implies \(\rho\leq\omega\), and evaluation at \(1\) gives \(f(h_\rho)\leq f(h_\omega)\). Alternatively the construction gives \(\|\rho\|=\|s\eta_\omega\|^2\leq\|\omega\|\). ∎

This proof constructs the functional for a smaller commutant operator. An assertion that positive operators have square roots would not by itself prove that the finite cone is hereditary.

<a id="OA-MOD-OW-05"></a>
