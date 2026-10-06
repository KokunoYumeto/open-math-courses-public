# A faithful weight on the GNS commutant

**Self-checked by the writing AI.**

For a normal semifinite weight, each dominated normal functional produces a bounded positive operator in the GNS commutant. We now turn the norm of that functional into a weight on the commutant. The construction produces a faithful weight even when the original weight is not faithful. Its essential issue is uniqueness: a comparison operator remembers values on the finite domain, so that domain must be large enough to determine the normal functional.

All proofs below are relative to the exact earlier course results listed in OW-01. No faithful state, separable representation, countable exhaustion, modular conjugation, or unbounded spectral theorem is assumed. Semifiniteness is a stated hypothesis for the norm formula (OW5); OW-11 explains why deleting it makes that formula ambiguous. OW-14 separately proves a corrected construction for an arbitrary normal input, using the finite-domain projection and a different defining value.

## Setting, domains, and existing inputs

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

The free comparison is Brent Nelson, [*Tomita–Takesaki Theory*, pages 30–32, Theorem 3.18 and Definition 3.19](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf). OW13 explains the hypothesis correction required by its displayed norm formula. The proof here uses these exact preceding programme results:

- **WG003, WG004, WG005, WG006 and WG007:** finite domains and their positive cone, the GNS construction, and normality of \(\pi\) when \(\varphi\) is normal. In particular \(\mathfrak m_\varphi^+=\{a\in M_+:\varphi(a)<\infty\}\).
- **WG008:** an increasing net of positive contractions \(e_\alpha\in\mathfrak m_\varphi^+\), with \(e_\alpha\uparrow1\). Its convergence is strong and ultraweak. It is not replaced by a sequence or by an asserted increasing net of finite-weight projections.
- **DW02, DW03 and DW04:** bounded factorization inside a von Neumann algebra, the commutant/form correspondence, and the comparison operator with its exact range closure and polar intertwining.
- **NW11:** for any normal weight, recovery as the pointwise supremum of dominated positive normal functionals; and, for any weight, equivalence of normality with preservation of arbitrary summable positive families. These are weight theorems, not an application of a bounded-map continuity theorem to an infinite-valued function.
- **BK03, BK04, BK05, BK06 and BK07:** bounded strong-to-ultraweak convergence, bounded monotone nets, inverse order, support cutoffs, and rectangular polar decomposition. Square roots and positive-operator norm estimates are proved in BK01.
- **CP06 and CP07:** the predual is a Banach space, its positive cone is norm closed, and a positive normal functional has norm equal to its value at the identity. WG007 proves that the GNS representation preserves bounded increasing positive suprema and is ultraweakly continuous. Vector functionals are ultraweakly continuous by BK03, so composing one with this representation gives a normal functional.

The predual norm fact used below can also be read directly from positivity: the bounded-functional Cauchy–Schwarz inequality gives
\(|\omega(a)|^2\leq\omega(a^*a)\omega(1)\leq\|a\|^2\omega(1)^2\), while evaluation at \(1\) gives the reverse norm inequality. Consequently norms add on positive functionals.

## What a comparison operator remembers

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

## The vector implementing a finite observation

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

## A hereditary cone in the commutant

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

## Defining the opposite weight and its finite domains

For \(h\in N_+\), set

\[
\varphi^{\mathrm{opp}}(h)=
\begin{cases}
\|\omega\|,&h=h_\omega\in P_\varphi,\\
\infty,&h\notin P_\varphi.
\end{cases}
\tag{OW5}
\]

**Proposition.** Formula (OW5) defines a weight on \(N\). Its positive finite domain is exactly \(P_\varphi\), and

\[
\mathfrak n_{\mathrm{opp}}=
\{v\in N:v^*v=h_\omega\text{ for some }\omega\in\mathcal E_\varphi\},
\]

\[
\mathfrak m_{\mathrm{opp}}
=\operatorname{span}_{\mathbb C}P_\varphi
=\operatorname{span}_{\mathbb C}
\{w^*v:v,w\in\mathfrak n_{\mathrm{opp}}\},
\qquad
\mathfrak m_{\mathrm{opp}}\cap N_+=P_\varphi.
\tag{OW6}
\]

No norm-closedness is asserted for either finite domain.

**Proof.** On the finite cone, the weight axioms hold by OW-04. If \(h+k\) were finite, heredity would make both \(h\) and \(k\) finite. Thus if either summand has value infinity, so does the sum. This proves additivity with extended values. For \(t>0\), membership of \(th\) in the cone is equivalent to membership of \(h\), and the finite values scale by \(t\). For \(t=0\), both sides are zero using \(0\cdot\infty=0\). Finally \(h_0=0\), so the value at zero is zero. This proves the weight axioms and its stated positive finite cone. Apply WG-003 to this weight on \(N\) to get (OW6). ∎

The formula is intrinsic to the specified GNS triple. Under its canonical unitary equivalence with another GNS triple, both \(h_\omega\) and their finite cone are conjugated by that unitary, so the weights correspond; a proof is included among the exercises.

## Normality with arbitrary summable families

**Theorem.** The weight \(\varphi^{\mathrm{opp}}\) is normal. More precisely, if \((h_i)_{i\in I}\subseteq N_+\) has bounded finite partial sums and

\[
h=\sum_{i\in I}h_i
\]

is their strong supremum, then

\[
\varphi^{\mathrm{opp}}(h)
=\sum_{i\in I}\varphi^{\mathrm{opp}}(h_i).
\tag{OW7}
\]

Both sums use finite subsets of the possibly uncountable index set \(I\).

**Proof.** First suppose the scalar sum on the right is finite, say \(L<\infty\). Every \(h_i=h_{\omega_i}\) for a unique \(\omega_i\in\mathcal E_\varphi\), and \(\sum_i\|\omega_i\|=L\). The finite partial sums of these functionals form a norm Cauchy net in \(M_*\). Indeed, given \(\varepsilon>0\), choose a finite set \(F_0\) whose scalar subsum exceeds \(L-\varepsilon\); every finite subsum over indices outside \(F_0\) is at most \(\varepsilon\). The norm of a difference of two functional partial sums containing \(F_0\) is at most the scalar sum over their symmetric difference, hence at most \(\varepsilon\). To spell out the use of completeness, choose increasing finite sets \(F_n\) whose scalar subsums exceed \(L-2^{-n}\). Their functional partial sums are a Cauchy sequence, hence have a limit \(\omega\in M_*\) by CP06–07. For every finite \(F\supseteq F_n\), the difference between the sums over \(F\) and \(F_n\) has norm at most \(2^{-n}\). The sequence limit has the same bound from the sum over \(F_n\), by taking the limit of that estimate. Thus every such \(F\) is within \(2^{1-n}\) of \(\omega\). This proves convergence of the whole net, without asserting that the sets \(F_n\) are cofinal. Positivity survives the norm limit by evaluation on each positive element. We have a limit \(\omega\in M_*^+\), with

\[
\|\omega\|=\omega(1)=\sum_i\omega_i(1)=L.
\]

For \(x\in\mathfrak n_\varphi\), evaluate the norm-convergent functional sums and the strongly convergent operator sums to get

\[
\omega(x^*x)
=\sum_i\langle h_i\Lambda(x),\Lambda(x)\rangle
=\langle h\Lambda(x),\Lambda(x)\rangle
\leq\|h\|\varphi(x^*x).
\]

The finite-positive-domain test used in OW-04 shows \(\omega\in\mathcal E_\varphi\); a constant \(1+\|h\|\) suffices globally and avoids an implicit multiplication of infinity by zero. Equation (OW1) then gives \(h_\omega=h\). Therefore \(\varphi^{\mathrm{opp}}(h)=L\), proving (OW7) whenever the right side is finite.

Next suppose \(\varphi^{\mathrm{opp}}(h)<\infty\). Heredity puts each finite partial sum \(h_F=\sum_{i\in F}h_i\) in \(P_\varphi\). Finite additivity and monotonicity give

\[
\sum_{i\in F}\varphi^{\mathrm{opp}}(h_i)
=\varphi^{\mathrm{opp}}(h_F)
\leq\varphi^{\mathrm{opp}}(h).
\]

Taking the supremum over finite \(F\) shows that the right side of (OW7) is finite. The preceding case gives equality. Thus either side being finite forces equality. If neither is finite, both are infinity. This proves (OW7) in all cases, including an empty family.

By NW-11, complete additivity for these positive operator families implies normality on the arbitrary von Neumann algebra \(N\). In particular, for every bounded increasing net \(k_\alpha\uparrow k\) in \(N_+\),

\[
\varphi^{\mathrm{opp}}(k)=\sup_\alpha\varphi^{\mathrm{opp}}(k_\alpha).
\]

No sequence is substituted for that net. ∎

The predual sum in this proof converges in norm, whereas the commutant sum converges strongly. Keeping those topologies separate permits us to pass both limits through their respective pairings.

## Faithfulness and a net proving semifiniteness

**Theorem.** The weight \(\varphi^{\mathrm{opp}}\) is faithful and semifinite. Therefore (OW5) is a faithful normal semifinite weight on \(\pi_\varphi(M)'\), even when \(\varphi\) is not faithful.

**Proof of faithfulness.** If \(\varphi^{\mathrm{opp}}(h)=0\), then \(h=h_\omega\) with \(\|\omega\|=0\). Thus \(\omega=0\) and \(h=h_0=0\).

**Proof of semifiniteness.** By (OW2), \(\omega\in\Phi_\varphi\) is equivalent to \(0\leq h_\omega\leq I_H\). NW-11 applied to \(\varphi\) gives, for every \(x\in\mathfrak n_\varphi\),

\[
\|\Lambda(x)\|^2
=\varphi(x^*x)
=\sup_{\omega\in\Phi_\varphi}\omega(x^*x)
=\sup_{\omega\in\Phi_\varphi}
\|h_\omega^{1/2}\Lambda(x)\|^2.
\tag{OW8}
\]

Set \(q(\xi)=\sup_{\omega\in\Phi_\varphi}\|h_\omega^{1/2}\xi\|\). Since these square roots are contractions,

\[
|q(\xi)-q(\zeta)|\leq\|\xi-\zeta\|.
\]

Density of GNS vectors and (OW8) imply \(q(\xi)=\|\xi\|\) for every \(\xi\in H\). Consequently the only vector annihilated by all \(h_\omega\), \(\omega\in\Phi_\varphi\), is zero. The closed linear span of their support ranges is all of \(H\).

Here is an explicit increasing finite-weight net. Direct the cone \(P_\varphi\) by operator order; it is directed because \(a+b\) is a common upper bound for \(a,b\). For every index \(a\in P_\varphi\), put

\[
f_a=a(I_H+a)^{-1}.
\]

Functional calculus gives \(0\leq f_a\leq I_H\) and \(f_a\leq a\), so heredity puts \(f_a\) in \(P_\varphi\). Inverse order from BK-05 gives \(a\leq b\Rightarrow f_a\leq f_b\). Let \(f\leq I_H\) be the strong supremum of this net.

For fixed \(a\in P_\varphi\), all \(ta\), \(t>0\), are indices, and BK-06 gives

\[
ta(I_H+ta)^{-1}\uparrow s(a)\quad(t\to\infty).
\]

Thus \(f\geq s(a)\). A positive contraction dominating a projection acts as the identity on its range, by BK-06. Hence \(f\) is the identity on every support range of every \(h_\omega\), \(\omega\in\Phi_\varphi\). These ranges span a dense subspace, so \(f=I_H\).

We have exhibited finite-weight positive contractions \(f_a\uparrow I_H\). WG-008, applied to the weight \(\varphi^{\mathrm{opp}}\), proves that \(\mathfrak m_{\mathrm{opp}}\) is ultraweakly dense in \(N\). This is precisely semifiniteness. ∎

If \(H=\{0\}\), then \(N=\{0\}\), the opposite weight is zero, and faithfulness and semifiniteness hold vacuously. In this situation injectivity of OW-02 forces \(\mathcal E_\varphi=\{0\}\), so no norm ambiguity occurs. The nonsemifinite counterexample in OW-11 has a different finite-domain hypothesis despite having the same zero Hilbert space.

## Recognizing finite positive operators without choosing a functional

**Proposition.** For \(h\in N_+\), the following are equivalent:

1. \(\varphi^{\mathrm{opp}}(h)<\infty\).
2. There exists \(\eta\in H\) such that

   \[
   h^{1/2}\Lambda(x)=\pi(x)\eta
   \quad\text{for every }x\in\mathfrak n_\varphi.
   \tag{OW9}
   \]

When these conditions hold, \(\eta\) is unique and

\[
\varphi^{\mathrm{opp}}(h)=\|\eta\|^2,
\qquad
\omega_h(a)=\langle\pi(a)\eta,\eta\rangle
\]

is the unique functional in \(\mathcal E_\varphi\) with \(h_{\omega_h}=h\).

**Proof.** Finiteness gives \(h=h_\omega\), and OW-03 supplies \(\eta_\omega\), its norm, and uniqueness. Conversely, suppose (OW9) holds and define the displayed vector functional \(\omega_h\). It is normal because \(\pi\) is normal. For \(x\in\mathfrak n_\varphi\),

\[
\omega_h(x^*x)=\|h^{1/2}\Lambda(x)\|^2
\leq\|h\|\varphi(x^*x).
\]

The same finite-positive-domain argument as before gives \(\omega_h\in\mathcal E_\varphi\); polarization gives \(h_{\omega_h}=h\). Its norm is \(\|\eta\|^2\), since \(\pi(1)=I_H\). Uniqueness of the functional follows from OW-02, and uniqueness of the vector follows by applying \(\pi(e_\alpha)\uparrow I_H\) to the difference of two vectors satisfying (OW9). ∎

This criterion records a boundedness condition on the module equation with its exact domain. It is not an assertion that right multiplication by an arbitrary element of \(M\) is bounded in GNS norm.

## An arbitrary-coordinate example with a nonfaithful input

Let \(I\) be any set, let \(0\leq w_i<\infty\), and put \(S=\{i:w_i>0\}\). On \(M=\ell^\infty(I)\), define

\[
\varphi(a)=\sum_{i\in I}w_i a_i\qquad(a\geq0).
\]

Sums mean suprema over finite subsets. The finite-subset arguments in WG011 show normality and semifiniteness; coordinates of zero weight do not affect either proof. The weight is faithful exactly when \(S=I\).

Its GNS space is \(\ell^2(S,w)\), with \(\Lambda(x)=x|_S\) on the domain where \(\sum_i w_i|x_i|^2<\infty\). The representation acts by coordinate multiplication. Its commutant is again \(\ell^\infty(S)\): an operator commuting with every coordinate projection preserves each one-dimensional coordinate space, and is therefore a bounded diagonal operator. This argument also applies when \(S\) is uncountable.

Here are the completion and density details. The map \(x_i\mapsto \sqrt{w_i}x_i\) on \(S\) identifies the GNS norm with the ordinary square-sum norm. This square-sum space is complete: for a Cauchy sequence \(z^{(n)}\), every coordinate converges to some \(z_i\). If \(\|z^{(n)}-z^{(m)}\|\leq\varepsilon\) for \(n,m\geq N\), passing to the coordinate limit in any finite subsum gives

\[
 \begin{gathered}
 \sum_{i\in F}|z_i^{(n)}-z_i|^2\leq\varepsilon^2,\\
 F\subseteq S\text{ finite},\qquad n\geq N.
 \end{gathered}
\]

The scalar inequality \(|z_i|^2\leq2|z_i-z_i^{(N)}|^2+2|z_i^{(N)}|^2\), followed by finite-subsum suprema, proves that \(z\) has finite square sum. Taking the same suprema in the displayed estimate proves norm convergence to \(z\). A finite subsum within \(\varepsilon^2\) of the total leaves a tail of norm at most \(\varepsilon\), so finite-support vectors are dense. Every such vector is the restriction of a bounded finite-support element of \(M\) in the GNS domain. This proves the asserted completion, including \(S=\varnothing\).

For the commutant assertion, use the normalized coordinate vectors as an orthonormal family. A commuting operator acts on each by a scalar of modulus at most its norm. Its action on their dense finite span is therefore the corresponding bounded diagonal action, which determines it on the whole completion. Conversely every bounded diagonal action commutes with all coordinate multipliers.

Every positive normal functional on \(\ell^\infty(I)\) has the form

\[
\omega_v(a)=\sum_i v_i a_i,
\qquad v_i\geq0,\quad\sum_i v_i<\infty.
\]

Indeed its coordinate masses have sum \(\omega_v(1)\) by normality of the increasing finite coordinate projections; applying the same argument to finite truncations of \(a\geq0\) gives the formula. Conversely such a summable family defines a normal functional by interchanging finite-subset and increasing-net suprema.

Domination \(\omega_v\leq c\varphi\) is equivalent to \(v_i\leq c w_i\) for every \(i\), by testing individual coordinates and then summing. In particular \(v_i=0\) outside \(S\). Formula (OW1) shows that \(h_{\omega_v}\) is multiplication by \(v_i/w_i\) on \(S\). Therefore, for \(h=(h_i)\in\ell^\infty(S)_+\),

\[
\varphi^{\mathrm{opp}}(h)=\sum_{i\in S}w_i h_i.
\tag{OW10}
\]

For a finite sum value, choose \(v_i=w_i h_i\); it is summable and dominated with constant \(\|h\|\), and gives the required comparison operator. For an infinite sum value no normal functional of finite norm can have those coordinate masses, so (OW5) gives infinity. This proves (OW10) directly in both cases.

The resulting weight is faithful on \(\ell^\infty(S)\). The zero-weight coordinates have disappeared through the GNS quotient, rather than being made positive by an unstated faithfulness assumption. If \(S\) is uncountable, this example cannot be replaced by a faithful normal state on that commutant: a summable family of nonnegative coordinate masses has at most countable support, since for each positive integer \(n\) only finitely many masses can be at least \(1/n\).

## Matrix calculation: operator size and weight size

Let \(M=M_d(\mathbb C)\) and \(D>0\) be an invertible positive matrix. Set \(\varphi(a)=\operatorname{Tr}(Da)\). Realize its GNS space as the Hilbert space of \(d\times d\) matrices with

\[
\langle z,w\rangle=\operatorname{Tr}(w^*z),\qquad
\Lambda(x)=xD^{1/2},\qquad \pi(a)z=az.
\]

Right multiplication \(R_b(z)=zb\) gives the whole commutant: an operator \(T\) commuting with every left multiplication satisfies \(T(z)=zT(1)\). The map \(b\mapsto R_b\) reverses products, since \(R_bR_c=R_{cb}\), and preserves involution and positivity.

All matrix facts used in this calculation follow from finite sums. Cyclicity of trace follows from

\[
 \begin{aligned}
 \operatorname{Tr}(AB)&=\sum_{j,k}A_{jk}B_{kj}\\
 &=\sum_{k,j}B_{kj}A_{jk}\\
 &=\operatorname{Tr}(BA).
 \end{aligned}
\]

Also \(\operatorname{Tr}(z^*z)=\sum_{j,k}|z_{jk}|^2\), so the stated inner product is positive definite. Completeness follows by taking the entrywise limits of a Cauchy sequence, then taking the finite sum of the squared entry errors. For \(C\geq0\), cyclicity gives

\[
 \operatorname{Tr}(Ca)
 =\sum_j\langle a C^{1/2}v_j,C^{1/2}v_j\rangle,
\]

where \(v_j\) are the standard basis vectors. Hence it is a positive normal functional, as a finite sum of vector functionals. In particular this applies to \(D\), and the displayed GNS identification is a surjective isometry since \(D^{1/2}\) is invertible.

Conversely, if \(\omega\) is positive, set \(C_{jk}=\omega(E_{kj})\). Expansion in the matrix units gives \(\omega(a)=\operatorname{Tr}(Ca)\), and testing \(a=vv^*\) gives \(v^*Cv\geq0\) for every column \(v\). Polarization then makes \(C\) self-adjoint and positive. For positive matrices \(C,D\), domination of the associated functionals by a constant \(c\) is equivalent to \(C\leq cD\): rank-one tests prove necessity; the positive square-root formula above proves sufficiency. When \(D\) is invertible, congruence by \(D^{-1/2}\) supplies a finite such constant for every \(C\geq0\).

Cyclicity also gives \(R_b^*=R_{b^*}\). For \(b\geq0\),

\[
 \begin{aligned}
 \langle R_bz,z\rangle&=\operatorname{Tr}(z^*zb)\\
 &=\|zb^{1/2}\|_{\mathrm{HS}}^2\geq0.
 \end{aligned}
\]

Conversely, positivity of \(R_b\) tested on \(z=uv^*\), with \(u\) a unit column, gives \(v^*bv\geq0\) for every \(v\), hence \(b\geq0\). The operator norm is \(\|R_b\|=\|b\|\): the upper bound follows by applying \(\|b^*v\|\leq\|b\|\|v\|\) to each row \(v^*\) of \(z\) and summing squares. For the lower bound, matrices with a single unit row give the supremum \(\|b^*\|=\|b\|\), the adjoint-norm identity proved in BK01. These arguments also prove that the positive square root of \(R_b\) is \(R_{b^{1/2}}\).

For \(\omega_C(a)=\operatorname{Tr}(Ca)\), \(C\geq0\), define

\[
b=D^{-1/2}CD^{-1/2}.
\]

Then

\[
\langle R_b\Lambda(x),\Lambda(y)\rangle
=\operatorname{Tr}(D^{1/2}bD^{1/2}y^*x)
=\omega_C(y^*x).
\]

Thus \(h_{\omega_C}=R_b\), and every positive element of the commutant arises this way. Its opposite-weight value and implementing vector are

\[
\varphi^{\mathrm{opp}}(R_b)=\operatorname{Tr}(Db),
\qquad \eta_b=D^{1/2}b^{1/2}.
\]

Indeed \(R_b^{1/2}\Lambda(x)=xD^{1/2}b^{1/2}=\pi(x)\eta_b\), and \(\|\eta_b\|^2=\operatorname{Tr}(Db)\). The matrices \(D\) and \(b\) need not commute.

For example, take

\[
D=\begin{pmatrix}2&0\\0&5\end{pmatrix},\qquad
b=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
\]

The best domination constant is \(\|h_{\omega_C}\|=\|b\|=3/2\), whereas \(\varphi^{\mathrm{opp}}(h_{\omega_C})=\operatorname{Tr}(Db)=7\). This separates the operator bound from the functional norm used in the new weight. To check the numerical values directly, the orthogonal vectors \((1,1)\) and \((1,-1)\) form a basis and are eigenvectors of \(b\) with eigenvalues \(3/2\) and \(1/2\). Expanding any vector in this basis proves the operator norm is \(3/2\); summing the two diagonal entries of \(Db\) gives \(2+5=7\).

## Why unrestricted normal weights do not support formula (OW5)

Take the nonzero algebra \(M=\mathbb C\) and define

\[
\varphi_\infty(0)=0,\qquad
\varphi_\infty(t)=\infty\quad(t>0).
\]

It is normal and faithful: an increasing positive net with a positive supremum has a positive term, and only zero has weight zero. Its finite domain is \(\{0\}\), so it is not semifinite and its GNS Hilbert space is zero.

For every \(c\geq0\), the normal positive functional \(\omega_c(z)=cz\) belongs to \(\mathcal E_{\varphi_\infty}\); for example it is dominated by \(\varphi_\infty\). Its comparison operator is always the unique zero operator on the zero Hilbert space. Nevertheless

\[
\|\omega_c\|=c.
\]

Hence assigning \(\varphi^{\mathrm{opp}}(h_{\omega_c})=\|\omega_c\|\) would assign every nonnegative value to the same input zero. It is not a function.

This diagnoses a missing hypothesis in the unrestricted formula, not a failure of the bounded comparison theorem DW-03: that theorem compares operators with forms on the finite domain, which are all zero here. Nor does it invalidate NW-11: all the functionals \(\omega_c\) together recover the infinite values as a pointwise supremum. It is the additional claim that the finite-domain comparison operator determines the full normal functional that fails.

The theorem through OW-08 assumes normality and semifiniteness before making that claim. An arbitrary-normal-weight construction requires a changed functional class or a specified support reduction. OW-14 supplies such a repair explicitly; it does not make the unrestricted norm formula valid.

## Exercises and solutions

**Problem 1: positive rescaling.** Let \(r>0\) and \(\psi=r\varphi\). Identify the GNS spaces by the unitary \(V:H_\psi\to H_\varphi\) defined on GNS vectors by
\(V\Lambda_\psi(x)=\sqrt r\,\Lambda_\varphi(x)\). Determine the relation between the two opposite weights under this identification.

**Solution.** Both finite domains agree, and the displayed norm identity proves that \(V\) is an isometry with dense range, hence a unitary. It intertwines the representations, so it identifies the commutants. The dominated-functional cones agree because a finite comparison constant can be divided or multiplied by \(r\). From the pairing definition,

\[
Vh^{\psi}_\omega V^*=r^{-1}h^{\varphi}_\omega.
\]

For an operator \(h\) in the identified commutant, finiteness for \(\psi^{\mathrm{opp}}\) is therefore equivalent to finiteness of \(rh\) for \(\varphi^{\mathrm{opp}}\), and their values agree there. Homogeneity of the weight gives

\[
\psi^{\mathrm{opp}}(V^*hV)=r\,\varphi^{\mathrm{opp}}(h)
\quad(h\geq0),
\]

including infinite values. Rescaling the original weight rescales its opposite by the same scalar; it does not take the reciprocal of the weight.

**Problem 2: GNS independence.** Suppose \((\widetilde H,\widetilde\pi,\widetilde\Lambda)\) is another GNS semicyclic triple for the same weight, and let \(W\Lambda(x)=\widetilde\Lambda(x)\) be the canonical unitary. Prove that the opposite weights are conjugate by \(W\).

**Solution.** The uniqueness theorem in WG-006 gives \(W\pi(a)W^*=\widetilde\pi(a)\), so conjugation identifies the commutants. For every dominated functional, its pairing on the dense GNS vectors is represented by both \(Wh_\omega W^*\) and \(\widetilde h_\omega\). Uniqueness of the bounded representing operator gives their equality. Thus conjugation sends the finite cone bijectively to the new finite cone and preserves its value \(\|\omega\|\). It also sends the complement of the finite cone to its complement. Hence
\(\widetilde\varphi^{\mathrm{opp}}(WhW^*)=\varphi^{\mathrm{opp}}(h)\) for every \(h\geq0\).

**Problem 3: finite norm does not mean finite weight.** In the coordinate model with \(I=\mathbb N\) and \(w_i=1\), compute the opposite-weight value of the identity and of the projections \(p_F\) onto finite subsets. Explain why this is consistent with normality and semifiniteness.

**Solution.** Formula (OW10) gives \(\varphi^{\mathrm{opp}}(I)=\infty\) and \(\varphi^{\mathrm{opp}}(p_F)=|F|\), although \(\|I\|=\|p_F\|=1\) for nonempty \(F\). The projections \(p_F\uparrow I\) strongly, and their values increase without bound, which is exactly normality at this infinite value. They are finite-weight positive contractions tending to the identity, which proves semifiniteness. Boundedness as an operator is unrelated to finiteness of this weight.

**Problem 4: a nonfaithful state gives a faithful opposite.** On \(M_d(\mathbb C)\), let \(\varphi(a)=\langle av,v\rangle\) for a unit vector \(v\), with \(d\geq2\). Compute the opposite weight.

**Solution.** The GNS space is \(\mathbb C^d\), \(\Lambda(x)=xv\), and \(\pi\) is the usual action. The commutant is \(\mathbb CI\). A normal positive functional \(\omega_C(a)=\operatorname{Tr}(Ca)\) is dominated by a multiple of \(\varphi\) exactly when \(0\leq C\leq c\,vv^*\) for some \(c\); positivity forces \(C=t vv^*\), \(t\geq0\). Indeed its quadratic form vanishes on \(v^\perp\), so its positive square root annihilates that subspace and its range is contained in \(\mathbb Cv\). Hence \(\omega_C=t\varphi\), \(h_{\omega_C}=tI\), and

\[
\varphi^{\mathrm{opp}}(tI)=t.
\]

This is faithful on the scalar commutant. The input state is not faithful on the full matrix algebra, because it vanishes on any projection onto a nonzero subspace of \(v^\perp\).

**Problem 5: distinguish a zero input from an infinite input.** On a nonzero von Neumann algebra let \(\varphi_0\) be the zero weight. Compare its construction with OW-11.

**Solution.** For \(\varphi_0\), both finite domains are all of \(M\); the weight is normal and semifinite, but not faithful. Its GNS space and commutant are zero. A positive functional dominated by any finite multiple of \(\varphi_0\) must be zero. Thus \(\mathcal E_{\varphi_0}=\{0\}\), formula (OW5) assigns the unique value zero at the unique positive operator, and the opposite weight is well-defined. For \(\varphi_\infty\), the finite domain is zero, every positive normal functional is dominated, and the same zero comparison operator carries incompatible functional norms. The Hilbert space alone does not distinguish those situations; the finite-domain hypothesis does.

## Free comparison and scope of the construction

Nelson’s free notes, pages 30–32, give the comparison operator, polar implementing vector and opposite-weight construction. Theorem 3.18 uses the unrestricted normal-weight setup of page 30, but its displayed functional-norm prescription needs the semifiniteness hypothesis used in OW02–03. OW11 gives a counterexample to the unrestricted prescription; OW14 supplies the corrected arbitrary-normal construction. Thus the free source’s statement is checked against the proof, rather than imported as an assertion.

In [*Tomita–Takesaki Theory*, Theorem 3.18 and Definition 3.19](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf), the heredity argument corresponds to OW04 and the complete-additivity argument to OW06. OW03 explicitly proves that the polar factor is a coisometry, the step needed for equality of the vector and functional norms. OW07 supplies an increasing finite-weight net directly, filling the directedness step left unresolved on page 32. OW09–12 give fully calculated examples and solutions. No modular commutant theorem is used to construct the new weight.

The unit exports the faithful normal semifinite weight (OW5), its exact positive finite cone and algebraic domains, its implementing-vector criterion, and invariance under the canonical GNS unitary. The following final item proves the separate arbitrary-normal repair. The unit does not identify these weights by a modular conjugation, prove a double-opposite theorem, construct a spatial derivative, or prove Connes cocycle formulas. Those remain distinct course obligations. The distinction between the two finite-domain hypotheses is part of the theorem, not a choice of notation.

## A corrected construction for an arbitrary normal input

This item changes the standing hypothesis: \(\varphi\) is now **any normal weight**, with no semifiniteness or faithfulness assumption. Let \(e\) be its finite-domain projection from WS02. The exact additional input is

\[
\mathfrak n_\varphi\subseteq Me,
\qquad\overline{\mathfrak m_\varphi}^{\,\mathrm{uw}}=eMe,
\qquad u_\alpha\uparrow e,
\]

where \(u_\alpha\) is an increasing net of positive contractions of finite \(\varphi\)-weight. Every finite positive element is supported in \(e\); the restriction to \(eMe\) is normal and semifinite by WS03. Neither \(e\) nor \(\pi_\varphi(e)\) is assumed central or equal to an identity.

Keep \(H,\pi,\Lambda,N,\mathcal E_\varphi\), and the bounded comparison operator \(h_\omega\) as before; its existence uses DW-03 and remains valid without semifiniteness. For a functional \(\omega\), write

\[
\omega_e(a)=\omega(eae),\qquad
\mathcal E_\varphi^e
=\{\rho\in\mathcal E_\varphi:\rho=\rho_e\}.
\]

**Theorem.** The rule

\[
\widehat\varphi^{\mathrm{opp}}(h)=
\begin{cases}
\omega(e),&h=h_\omega\text{ for some }\omega\in\mathcal E_\varphi,\\
\infty,&h\text{ is not of this form}
\end{cases}
\qquad(h\in N_+)
\tag{OW11}
\]

is well-defined and is a faithful normal semifinite weight. Its finite cone is still \(\{h_\omega:\omega\in\mathcal E_\varphi\}\), but the finite value is \(\omega(e)\), not generally \(\|\omega\|\). Equivalently, each finite operator has a unique representing functional \(\rho\in\mathcal E_\varphi^e\), and its value is \(\|\rho\|\). When \(e=1\), this recovers (OW5).

**Proof: removing the invisible part of a functional.** If \(\omega\in\mathcal E_\varphi\), then \(\omega_e\) is normal and positive. On every finite positive \(a\), one has \(a=eae\), so \(\omega_e(a)=\omega(a)\leq c\varphi(a)\). For the other positive elements, either their weight is infinite and a strictly positive comparison constant suffices, or they are already in the finite case. Thus \(\omega_e\in\mathcal E_\varphi^e\). Moreover

\[
\|\omega_e\|=\omega_e(1)=\omega(e),\qquad
h_{\omega_e}=h_\omega,
\tag{OW12}
\]

because every \(y^*x\), \(x,y\in\mathfrak n_\varphi\subseteq Me\), lies in \(eMe\).

For \(\rho,\tau\in\mathcal E_\varphi^e\), the inequality \(h_\rho\leq h_\tau\) implies \(\rho(a)\leq\tau(a)\) on the finite positive cone. For any positive \(b\in eMe\), the elements \(u_\alpha b u_\alpha\) are finite, since they are at most \(\|b\|u_\alpha\), and converge ultraweakly to \(b\). Normality gives the inequality on all of \((eMe)_+\). For arbitrary \(a\in M_+\), apply this to \(eae\) and use supportedness. Hence the map \(\rho\mapsto h_\rho\) reflects order on \(\mathcal E_\varphi^e\), and in particular is injective there. Equations (OW12) now prove that the value in (OW11) is independent of the original choice of \(\omega\). They also show that this finite value is additive, positively homogeneous, and increasing on the finite cone, once heredity is established below.

**Proof: a vector in the correct subspace.** Fix \(\rho\in\mathcal E_\varphi^e\) and form the comparison map \(C_\rho:H\to H_\rho\) from DW-04. Its range closure contains \(\Omega_\rho\). Indeed \(\rho(1-e)=0\) gives \(\pi_\rho(e)\Omega_\rho=\Omega_\rho\), and

\[
\|\pi_\rho(u_\alpha)\Omega_\rho-\Omega_\rho\|^2
=\rho((e-u_\alpha)^2)
\leq\rho(e-u_\alpha)\longrightarrow0.
\]

The range closure is invariant under \(\pi_\rho(M)\), so cyclicity gives \(\overline{\operatorname{ran}C_\rho}=H_\rho\). If \(C_\rho=U_\rho h_\rho^{1/2}\), its polar factor is therefore a coisometry. The vector \(\eta_\rho=U_\rho^*\Omega_\rho\) satisfies

\[
\|\eta_\rho\|^2=\|\rho\|,\qquad
\pi(e)\eta_\rho=\eta_\rho,\qquad
h_\rho^{1/2}\Lambda(x)=\pi(x)\eta_\rho
\quad(x\in\mathfrak n_\varphi).
\tag{OW13}
\]

The first and third equalities follow from the coisometry and polar intertwining calculations of OW-03. For the second, intertwining gives
\(\pi(e)U_\rho^*\Omega_\rho
=U_\rho^*\pi_\rho(e)\Omega_\rho=U_\rho^*\Omega_\rho\).
The same calculation as (OW4) shows that \(\eta_\rho\) implements \(\rho\) on all of \(M\).

This vector is unique **in \(\pi(e)H\)** with its displayed module identity: if two such vectors differ by \(\zeta\), then \(\pi(u_\alpha)\zeta=0\); normality of \(\pi\) gives \(\pi(u_\alpha)\uparrow\pi(e)\) strongly and hence \(\zeta=\pi(e)\zeta=0\). Uniqueness on all of \(H\) would be wrong in general, since \(\pi(x)\) for \(x=xe\) annihilates \((1-\pi(e))H\).

**Proof: heredity and the weight axioms.** If \(0\leq h\leq h_\rho\), take \(s\in N\), \(\|s\|\leq1\), with \(h^{1/2}=s h_\rho^{1/2}\). Define
\(\tau(a)=\langle\pi(a)s\eta_\rho,s\eta_\rho\rangle\).
It is normal. Since \(s\) commutes with \(\pi(e)\), its implementing vector belongs to \(\pi(e)H\), so \(\tau(a)=\tau(eae)\). Equation (OW13) gives

\[
\tau(x^*x)=\|s h_\rho^{1/2}\Lambda(x)\|^2
=\langle h\Lambda(x),\Lambda(x)\rangle
\leq\|h\|\varphi(x^*x).
\]

Testing finite positive elements with their square roots and using a strictly positive domination constant for infinite values gives \(\tau\in\mathcal E_\varphi^e\). Polarization gives \(h_\tau=h\). The finite cone is therefore hereditary. Its finite value is \(\|\tau\|\), and order reflection proves monotonicity. Addition of supported functionals and additivity of their norms prove finite additivity. If a positive sum is finite, heredity makes both summands finite; this proves additivity when one value is infinite as well. Positive scalar multiplication preserves the cone, and the value at zero is zero. With \(0\cdot\infty=0\), these facts prove all weight axioms for (OW11).

**Proof: normality.** Let \((h_i)_{i\in I}\subseteq N_+\) have bounded finite partial sums and strong sum \(h\). If \(L=\sum_i\widehat\varphi^{\mathrm{opp}}(h_i)<\infty\), write \(h_i=h_{\rho_i}\) with the unique \(\rho_i\in\mathcal E_\varphi^e\). The functional partial sums are norm Cauchy: outside a finite set whose scalar subsum is within \(\varepsilon\) of \(L\), every finite sum of their norms is at most \(\varepsilon\). Let \(\rho\in M_*^+\) be the limit. It remains supported in \(e\), because for each \(a\in M\) the equality of each partial sum's evaluations on \(a\) and \(eae\) passes to the norm limit. Its norm is \(L\). For \(x\in\mathfrak n_\varphi\),

\[
\rho(x^*x)=\lim_F\sum_{i\in F}\rho_i(x^*x)
=\langle h\Lambda(x),\Lambda(x)\rangle
\leq\|h\|\varphi(x^*x).
\]

As before this yields global domination by \((1+\|h\|)\varphi\), so \(\rho\in\mathcal E_\varphi^e\) and \(h_\rho=h\). Thus \(\widehat\varphi^{\mathrm{opp}}(h)=L\).

If instead the value at \(h\) is known to be finite, heredity and monotonicity bound each scalar finite subsum by that value. Hence \(L<\infty\), and the preceding argument again gives equality. If neither side is finite they both equal infinity. Complete additivity follows for all such families, and NW-11 proves normality.

**Proof: faithfulness and semifiniteness.** A finite value zero corresponds to a supported functional of norm zero, hence to the zero operator, proving faithfulness. For semifiniteness, let
\(\Phi_\varphi^e=\{\rho\in\mathcal E_\varphi^e:\rho\leq\varphi\}\).
For each \(\omega\in\Phi_\varphi\), compression gives \(\omega_e\in\Phi_\varphi^e\) with the same values on the finite positive cone. Thus NW-11 gives

\[
\|\Lambda(x)\|^2
=\sup_{\rho\in\Phi_\varphi^e}\rho(x^*x)
=\sup_{\rho\in\Phi_\varphi^e}
\|h_\rho^{1/2}\Lambda(x)\|^2
\quad(x\in\mathfrak n_\varphi).
\]

Each \(h_\rho\leq I_H\). The supremum of the norms of these contractions is a Lipschitz function of the vector, so density extends this identity to every vector of \(H\). Their common kernel is consequently zero, and their support ranges span \(H\).

Index the entire finite cone by its directed operator order and use the positive contractions \(f_a=a(I_H+a)^{-1}\). Heredity makes them finite; inverse order makes the net increasing. Its strong supremum \(f\leq I_H\) dominates \(s(a)\) for every finite \(a\), because \(ta(I_H+ta)^{-1}\uparrow s(a)\). Therefore \(f\) acts as the identity on the dense span of the preceding support ranges, and \(f=I_H\). WG-008 proves semifiniteness. The zero Hilbert space is included: all these identities are identities of zero operators, and the unique weight on the zero algebra is faithful, normal, and semifinite. ∎

For a supported representative \(\rho\in\mathcal E_\varphi^e\), the attained least domination constant is still \(\|h_\rho\|\). For an unrestricted \(\omega\in\mathcal E_\varphi\), the finite-domain test proves \(\omega\leq c\varphi\) if and only if \(h_\omega\leq cI_H\) for \(c>0\); the zero-constant assertion must not be inferred. In OW-11, every \(c>0\) dominates a fixed nonzero \(\omega\) by \(c\varphi_\infty\), but \(c=0\) does not. Thus its comparison constants have infimum zero without a minimum. For supported representatives, injectivity supplies the missing zero case.

**Example with a proper noncentral finite-domain projection.** In \(M_2(\mathbb C)\), let \(e=E_{11}\) and define \(\varphi(te)=t\) for \(t\geq0\), with value infinity on positive matrices not supported in \(e\). The positive-cone and normality argument of WS08, Problem 3, with two matrix coordinates, applies. Its GNS space is \(\mathbb C^2\), with \(\Lambda(x)=x e_1\) on \(\mathfrak n_\varphi=Me\), and \(\pi\) the usual matrix action. Hence \(N=\mathbb CI\), but \(\pi(e)=e\neq I\).

Every normal positive functional \(\omega_C(a)=\operatorname{Tr}(Ca)\), \(C\geq0\), is dominated by some finite positive multiple of \(\varphi\): on finite elements it is enough to bound \(C_{11}\), and elsewhere the weight is infinite. The comparison operator is \(h_{\omega_C}=C_{11}I\). Formula (OW11) gives

\[
\widehat\varphi^{\mathrm{opp}}(tI)=t,
\]

whereas the erroneous unrestricted norm rule would assign \(\operatorname{Tr}(C)\) to \(C_{11}I\). The unique supported representative is \(a\mapsto C_{11}a_{11}\). Its implementing vector is \(\sqrt{C_{11}}e_1\in\pi(e)H\); adding any vector in \(\mathbb Ce_2\) leaves the module identity on \(Me\) unchanged. This explicitly verifies the restricted uniqueness condition in the theorem.
