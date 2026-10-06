# Recognizing a weight by its fixed density

The question here is a converse: which weights arise from the centralizer-affiliated densities already constructed in CZ? A modular-invariant weight can vanish on a noncentral projection. We therefore identify a density first for faithful weights, using a normalized matrix cocycle, and then pass through the exact support corner. The trace case follows without turning the density into a bounded or measurable operator prematurely.

The antecedent for the faithful equivalence is Takesaki, *Theory of Operator Algebras II*, VIII.3, Corollary 3.6. The application in IX.2, Lemma 2.12 also needs normal semifinite weights which are not faithful. PT-06 proves that extension explicitly. The unit neither presumes nor establishes the other integration assertions of IX.2.12.

## The fixed algebra and the objects being compared

Let \(M\subseteq B(H)\) be a faithful, nondegenerate concrete von Neumann algebra, with no restriction on the Hilbert-space dimension. Fix a faithful normal semifinite weight \(\varphi\). The zero algebra is allowed; its identity, unique weight and unique operator are all zero. Write

\[
 \sigma_t=\sigma_t^\varphi,\qquad
 N=M_\varphi=\{a\in M:\sigma_t(a)=a\text{ for every }t\in\mathbb R\}.
 \tag{PT.1}
\]

A positive self-adjoint operator affiliated with \(N\) means a densely defined positive self-adjoint operator on \(H\) whose spectral projections belong to \(N\). It can have a kernel, have unbounded inverse on its support, and fail every trace-measurability condition.

For such an operator \(h\), CZ-06–08 define

\[
 h_\varepsilon=h(1+\varepsilon h)^{-1}\in N_+,\qquad
 \varphi_h(x)=\sup_{\varepsilon>0}
        \varphi(h_\varepsilon^{1/2}x h_\varepsilon^{1/2}),
 \quad x\in M_+.
 \tag{PT.2}
\]

The supremum is the increasing limit as \(\varepsilon\downarrow0\). It is a normal semifinite weight, with support
\(s(h)=1-1_{\{0\}}(h)\). Thus it is faithful precisely when \(h\) has zero kernel. Scalar arithmetic uses \(0\cdot\infty=0\).

We use these exact previously proved interfaces.

- Recognize exactly the fixed observations gives the centralizer criterion and invariance under its unitaries on all of \(M_+\), including infinite values. CZ-08 constructs (PT.2); CZ-09 identifies restrictions to centralizer corners, including their modular groups; CZ-11 computes the supported modular group of (PT.2).
- The balanced-matrix cocycle is independent of the reference defines the intrinsic balanced-matrix cocycle and proves its spatial formula, cocycle law and strong* continuity for pairs of faithful normal semifinite weights.
- An analytic unitary core determines all powers identifies the positive generator of a strongly continuous unitary group from its full analytic-vector core. Its averaging corollary applies with the entire Hilbert space as the invariant ambient vector space. CX-10 proves fixed-reference cocycle injectivity on every positive element, including infinite weight values.
- Coordinate changes and positive scalar multiples proves modular transport under a von Neumann algebra isomorphism. SK-05, SK-07 and SK-08 supply spectral domains, powers and unitary transport.
- Normality produces a largest null projection through The faithful semifinite support corner give the maximal null projection and faithful support restriction of a normal semifinite weight. CW-04–07 give the corresponding corner lifts, their extended-positive evaluations and centralizer compression.
- Infinite energies have bounded spectral tests through Evaluating a normal weight on every extended positive specify the whole extended positive cone and evaluation of normal weights on it. MT supplies the spectral-tail criterion for trace measurability; its exact use is isolated in PT-09.

In particular no equality of modular groups is being used as a substitute for equality of weights.

## Naturality fixes the normalization of the cocycle

Let \(\alpha\) be an automorphism of \(M\), and let \(\varphi,\psi\) both be faithful normal semifinite. Then

\[
 [D(\psi\circ\alpha):D(\varphi\circ\alpha)]_t
       =\alpha^{-1}([D\psi:D\varphi]_t).
 \tag{PT.3}
\]

**Proof.** On \(M_2(M)\), set

\[
 \Theta([x_{ij}])=\varphi(x_{11})+\psi(x_{22}).
\]

It is faithful normal semifinite by the diagonal-weight construction SI-05. Let \(\widetilde\alpha\) act entry by entry. Then
\(\Theta\circ\widetilde\alpha
   =(\varphi\circ\alpha)\oplus(\psi\circ\alpha)\).
KM-06 gives equality of the actual modular groups

\[
 \sigma_t^{\Theta\circ\widetilde\alpha}
   =\widetilde\alpha^{-1}\sigma_t^\Theta\widetilde\alpha.
\]

The scalar matrix unit \(E_{21}\) is fixed by \(\widetilde\alpha\). Apply the preceding identity to it. By the defining identity SI-14, the left side is the left side of (PT.3) times \(E_{21}\), whereas the right side is its right side times \(E_{21}\). Equality of that matrix entry proves (PT.3). No choice of a spatial denominator, implementing unitary or scalar phase remains. \(\square\)

Suppose now that \(\psi\circ\sigma_s=\psi\) for every \(s\). Since \(\varphi\) is also invariant, (PT.3) implies, for
\(u_t=[D\psi:D\varphi]_t\),

\[
 \sigma_s(u_t)=u_t \qquad(s,t\in\mathbb R).
 \tag{PT.4}
\]

The cocycle law consequently becomes

\[
 u_{s+t}=u_su_t.
 \tag{PT.5}
\]

Conversely, if this cocycle is an ordinary group, comparison of (PT.5) with
\(u_{s+t}=u_s\sigma_s(u_t)\), followed by left multiplication by \(u_s^*\), gives (PT.4). This observation alone does not yet identify the second weight.

## A unitary group inside the fixed algebra has a unique density

**Lemma.** Let \(V_t\) be a strongly continuous unitary group contained in a von Neumann algebra \(R\subseteq B(K)\). There is a unique positive injective self-adjoint operator \(h\), affiliated with \(R\), such that

\[
 V_t=h^{it}\qquad(t\in\mathbb R).
 \tag{PT.6}
\]

The equality is of bounded unitary operators. Every unbounded real or complex power of \(h\) has its spectral-calculus domain.

**Proof.** Take the invariant vector space \(\mathcal F=K\) in the averaging corollary of CX-02. Its invariance under the integrals
\(V(f)\xi=\int_\mathbb R f(t)V_t\xi\,dt\), \(f\in L^1(\mathbb R)\), is automatic. The integrals are Hilbert-norm integrals for each vector; their boundedness does not assert operator-norm continuity of \(V_t\).

For clarity, the dense analytic space used there consists of all vectors with an entire Hilbert-norm orbit. It is dense because

\[
 \xi_r(z)=\sqrt{r/\pi}\int_{\mathbb R}
                e^{-r(t-z)^2}V_t\xi\,dt
 \tag{PT.7}
\]

is entire and \(\xi_r(0)\to\xi\) in norm. Its entire translates are again entire vectors. Scalar uniqueness of holomorphic continuation makes the complex translations an algebraic group on this space. CX-02 therefore supplies the positive injective self-adjoint operator
\(P=\overline{V_{-i/2}|_{\mathcal F_{\rm an}}}\),
with \(V_t=P^{2it}\). Put \(h=P^2\), with its full spectral domain. Then \(h^{it}=P^{2it}\).

Let \(w\) be a unitary in \(R'\). It commutes with every \(V_t\). Thus it carries an entire orbit to the entire orbit of \(w\xi\), and uniqueness gives
\(wV_z\xi=V_z w\xi\) on the analytic space. The same holds for \(w^*\). Taking graph closures yields \(wP w^*=P\), including equality of domains. Spectral transport SK-08 now gives commutation with every spectral projection of \(P\) and \(h\). Those projections belong to \((R')'=R\), which proves affiliation.

For uniqueness, if \(h,k\) satisfy (PT.6), use their self-adjoint logarithms. Their bounded resolvents obey

\[
 (\log h-iI)^{-1}
       =i\int_0^\infty e^{-t}h^{-it}\,dt
       =i\int_0^\infty e^{-t}k^{-it}\,dt
       =(\log k-iI)^{-1}.
 \tag{PT.8}
\]

This is the scalar Laplace integral passed through bounded spectral calculus, exactly as in CX-10. The common resolvent determines its range, which is the logarithm's domain, and the logarithm on that range. Thus \(\log h=\log k\), and spectral exponentiation gives \(h=k\) with their full domains. On \(K=0\), the unique operator satisfies the statement; injectivity means that its kernel is the zero vector space. \(\square\)

## A density has exactly the prescribed cocycle

**Theorem.** If \(h\) is positive, injective and affiliated with \(M_\varphi\), then

\[
 [D\varphi_h:D\varphi]_t=h^{it}\qquad(t\in\mathbb R).
 \tag{PT.9}
\]

**Proof.** First consider
\(\Theta_0=\varphi\oplus\varphi\) on \(M_2(M)\).
SI-05 identifies its modular restrictions to the two diagonal corners with \(\sigma^\varphi\). SI-14 applied to identical weights gives
\(\sigma_t^{\Theta_0}(E_{21})=E_{21}\); taking adjoints gives the same assertion for \(E_{12}\). Multiplying diagonal entries by these fixed matrix units shows that \(\sigma_t^{\Theta_0}\) acts entry by entry as \(\sigma_t^\varphi\).

On \(H\oplus H\), define

\[
 D=I\oplus h,\qquad D(D)=H\oplus D(h).
\]

Its spectral projections are diagonal matrices formed from scalar multiples of \(I\) in the first entry and spectral projections of \(h\) in the second. They are fixed by \(\sigma^{\Theta_0}\). Hence \(D\) is positive injective and affiliated with the centralizer of \(\Theta_0\).

We check the perturbed weight before using any modular formula. For \(X=[x_{ij}]\geq0\),

\[
 \begin{split}
 (\Theta_0)_D(X)
 &=\lim_{\varepsilon\downarrow0}
       \left[(1+\varepsilon)^{-1}\varphi(x_{11})
                  +\varphi(h_\varepsilon^{1/2}x_{22}
                                          h_\varepsilon^{1/2})\right]\\
 &=\varphi(x_{11})+\varphi_h(x_{22})
   =(\varphi\oplus\varphi_h)(X).
 \end{split}
 \tag{PT.10}
\]

The two scalar quantities increase, so their limits add also at infinity. The equality therefore identifies the whole weight, not merely a finite linear domain.

Apply CZ-11 to \(\Theta_0\) and \(D\). Its modular formula, evaluated on \(E_{21}\), gives

\[
 \sigma_t^{\varphi\oplus\varphi_h}(E_{21})
 =D^{it}E_{21}D^{-it}=h^{it}E_{21}.
\]

By the balanced-matrix definition, this is precisely (PT.9). The spectral powers are bounded unitaries even though \(D\), \(h\), or their inverses may be unbounded. \(\square\)

## The faithful invariant-weight equivalence

**Theorem.** For faithful normal semifinite weights \(\varphi,\psi\) on \(M\), the following conditions are equivalent.

1. \(\psi\circ\sigma_t^\varphi=\psi\) for every real \(t\).
2. \([D\psi:D\varphi]_t\) belongs to \(M_\varphi\) for every real \(t\).
3. The map \(t\mapsto[D\psi:D\varphi]_t\) is an ordinary one-parameter unitary group.
4. There is a positive injective self-adjoint \(h\) affiliated with \(M_\varphi\) for which \(\psi=\varphi_h\) on \(M_+\).
5. \(\varphi\circ\sigma_t^\psi=\varphi\) for every real \(t\).

In condition 4, \(h\) is unique, and its exact normalized cocycle is (PT.9). All weight identities include infinite values.

**Proof.** PT-02 proves \(1\Rightarrow2\), and comparison with the cocycle identity proves \(2\Leftrightarrow3\). Under either condition 2 or 3, the group is strongly continuous by SI-14 and lies in \(M_\varphi\). PT-03 gives a unique positive injective affiliated \(h\) with \(u_t=h^{it}\). PT-04 shows that \(\varphi_h\) has this same cocycle relative to \(\varphi\). Fixed-reference injectivity CX-10 then proves \(\psi=\varphi_h\) on every positive element. This proves \(2\Rightarrow4\), and also establishes uniqueness in 4.

For \(4\Rightarrow1\), the bounded regularizations of \(h\) are fixed by \(\sigma^\varphi\). Therefore, for \(x\geq0\),

\[
 \varphi(h_\varepsilon^{1/2}\sigma_t^\varphi(x)h_\varepsilon^{1/2})
 =\varphi\bigl(\sigma_t^\varphi(
                h_\varepsilon^{1/2}x h_\varepsilon^{1/2})\bigr)
 =\varphi(h_\varepsilon^{1/2}x h_\varepsilon^{1/2}).
\]

Taking the increasing supremum gives condition 1 at all energies.

Under condition 4, CZ-11 gives
\(\sigma_t^\psi(x)=h^{it}\sigma_t^\varphi(x)h^{-it}\).
The unitary \(h^{it}\) belongs to \(M_\varphi\), and CZ-05 makes conjugation by it preserve \(\varphi\) on all positive elements. Invariance under \(\sigma^\varphi\) now gives condition 5. Finally, apply the already proved implication \(1\Rightarrow5\) with the two faithful weights interchanged: condition 5 implies condition 1. This completes the equivalence without identifying weights merely from their modular groups. \(\square\)

The density is also reversible. CZ-09 places its spectral projections in \(M_\psi\), so \(h^{-1}\) is affiliated with \(M_\psi\). The spatial formula SI-14 gives

\[
 [D\varphi:D\psi]_t=[D\psi:D\varphi]_t^*=h^{-it}.
\]

PT-04, now relative to \(\psi\), and CX-10 imply

\[
 \varphi=(\varphi_h)_{h^{-1}}.
 \tag{PT.11}
\]

Here \(D(h^{-1})=\operatorname{ran}h\); no bounded inverse is assumed.

## The complete extension through a possibly noncentral support

**Theorem.** Fix faithful normal semifinite \(\varphi\), and let \(\psi\) be any normal semifinite weight on \(M\), possibly zero or nonfaithful. Then

\[
 \psi\circ\sigma_t^\varphi=\psi\quad(t\in\mathbb R)
 \quad\Longleftrightarrow\quad
 \psi=\varphi_h
 \tag{PT.12}
\]

for a unique positive self-adjoint \(h\) affiliated with \(M_\varphi\). Its support is exactly the support of \(\psi\). In particular \(\psi=0\) corresponds precisely to \(h=0\).

**Proof of existence.** Assume invariance. Let \(f\) be the maximal \(\psi\)-null projection and \(p=1-f\). WS-04–06 apply because \(\psi\) is normal and semifinite. Thus

\[
 \psi(x)=\psi_p(pxp),\quad x\in M_+,
 \qquad \psi_p=\psi|_{pMp}
 \tag{PT.13}
\]

is faithful normal semifinite on \(pMp\).

For every \(t\), \(\sigma_t^\varphi(f)\) is again \(\psi\)-null. Maximality gives
\(\sigma_t^\varphi(f)\leq f\). Applying the same assertion at \(-t\) and transporting it by \(\sigma_t^\varphi\) gives the reverse inequality. Thus \(f,p\in M_\varphi\). This proves fixedness, not centrality in \(M\).

CZ-09 supplies the faithful normal semifinite reference
\(\varphi_p=\varphi|_{pMp}\), whose modular group is the restriction of \(\sigma^\varphi\). The weight \(\psi_p\) is invariant under that restricted group by (PT.13). If \(p=0\), (PT.13) gives \(\psi=0=\varphi_0\), and we are done.

For \(p\ne0\), apply PT-05 inside \(pMp\). It supplies a positive injective operator \(k\), affiliated with

\[
 (pMp)_{\varphi_p}=pM_\varphi p,
 \tag{PT.14}
\]

such that \(\psi_p=(\varphi_p)_k\). Equality (PT.14) follows directly from the equality of the restricted modular groups. Apply PT-05 in the faithful, nondegenerate representation of the corner on \(pH\); its intrinsic cocycle and affiliated generator are therefore obtained directly on that Hilbert space. No transfer between different Hilbert-space domains is needed.

Extend \(k\) by zero:

\[
 h=k\oplus0,\qquad D(h)=D(k)\oplus(1-p)H
 \quad\text{on }H=pH\oplus(1-p)H.
 \tag{PT.15}
\]

This is densely defined positive self-adjoint. Its nonzero spectral projections lie in \(pM_\varphi p\), and its kernel projection is \(1-p\in M_\varphi\). Thus it is affiliated with \(M_\varphi\), with support \(p\). Its regularization is \(k_\varepsilon\oplus0\). Consequently, for every \(x\geq0\),

\[
 \begin{split}
 \varphi_h(x)
 &=\sup_{\varepsilon>0}
          \varphi_p(k_\varepsilon^{1/2}(pxp)k_\varepsilon^{1/2})\\
 &=(\varphi_p)_k(pxp)
   =\psi_p(pxp)=\psi(x).
 \end{split}
 \tag{PT.16}
\]

Every equality is an equality of nonnegative extended values. No density, finite-domain argument or subtraction of infinities is needed to extend it off the corner.

**Converse and uniqueness.** Every density in (PT.2) gives a normal semifinite invariant weight: its normality, semifiniteness and support are CZ-08, while the regularization argument in PT-05 proves invariance with or without a kernel.

If \(\varphi_h=\varphi_\ell=\psi\), CZ-08 gives \(s(h)=s(\ell)=p\). When \(p=0\), both operators are zero. Otherwise their restrictions to \(pH\) are positive injective and affiliated with \(pM_\varphi p\), and both give the same faithful weight relative to \(\varphi_p\). Uniqueness in PT-05 gives equality of these restrictions, including their domains. Both operators vanish on \((1-p)H\), so (PT.15) gives \(h=\ell\) on all of \(H\). \(\square\)

For an invariant \(\psi\), one may record its normalized supported unitary family as

\[
 w_t=[D\psi_p:D\varphi_p]_t
       \ \text{on }pH,\qquad w_t=0\ \text{on }(1-p)H.
 \tag{PT.17}
\]

Then \(w_t=h^{it}\) on the support, \(w_t^*w_t=w_tw_t^*=p\), \(w_0=p\), and
\(w_{s+t}=w_sw_t=w_s\sigma_s^\varphi(w_t)\). At \(p=0\) the family is identically zero. Formula (PT.17) specifies the corner and weights exactly; it does not assert that a nonfaithful weight has a unitary cocycle or modular automorphism group on all of \(M\).

## The same density identity on every extended positive

For \(a\in M\) and \(H\in\widehat M_+\), define the bounded sandwich by

\[
 (a^*Ha)(\omega)=H(\omega_a),\qquad
 \omega_a(x)=\omega(a^*xa),\qquad \omega\in M_*^+.
 \tag{PT.18}
\]

This convention agrees with the usual bounded positive sandwich. The map \(\omega\mapsto\omega_a\) is positive linear and norm continuous. Hence (PT.18) is additive, nonnegatively homogeneous and lower semicontinuous, so it belongs to the extended positive cone. In particular it remains defined when its finite form domain is not dense.

If \(H_n\) are the bounded increasing spectral tests of CW-02, then
\(a^*H_na\uparrow a^*Ha\) pointwise on the positive predual. For bounded \(a=h_\varepsilon^{1/2}\), the definition of \(\varphi_{h_\varepsilon}\) on \(M_+\), followed by CW-03's preservation of increasing suprema, therefore gives

\[
 \widehat{\varphi_{h_\varepsilon}}(H)
      =\widehat\varphi(h_\varepsilon^{1/2}Hh_\varepsilon^{1/2}).
 \tag{PT.19}
\]

Interchanging the two suprema over \(n\) and \(\varepsilon\), all of whose terms are nonnegative, proves

\[
 \widehat{\varphi_h}(H)
   =\sup_{\varepsilon>0}
          \widehat\varphi(h_\varepsilon^{1/2}Hh_\varepsilon^{1/2}).
 \tag{PT.20}
\]

The weighted values on the right increase as \(\varepsilon\downarrow0\). The sandwiches themselves need not increase in operator order; the argument does not claim that they do.

For the support \(p=s(h)\), CW-04 gives in addition

\[
 \widehat{\varphi_h}(H)
      =\widehat{(\varphi_p)_{h|_{pH}}}(pHp).
 \tag{PT.21}
\]

Thus the characterization determines the weight on every positive energy, including the infinite part of an extended positive. Equations (PT.20–21) do not abbreviate an unchecked product of densely defined unbounded operators.

## Radon–Nikodym densities relative to a semifinite trace

Let \(\tau\) be a faithful normal semifinite trace on \(M\). Then every normal semifinite weight \(\psi\) on \(M\) has a unique positive self-adjoint affiliated density \(h\) such that

\[
 \psi(x)=\tau_h(x)
       =\sup_{\varepsilon>0}
          \tau(h_\varepsilon^{1/2}x h_\varepsilon^{1/2}),
 \qquad x\in M_+.
 \tag{PT.22}
\]

Its support is \(s(h)=s(\psi)\). The assertion includes arbitrary kernels and the zero weight; it places no measurability or finite-integral condition on \(h\).

**Proof.** The trace condition is \(\tau(a^*a)=\tau(aa^*)\) for every bounded \(a\). It makes the finite left ideal self-adjoint. Polarizing this equality on that ideal gives
\(\tau(xy)=\tau(yx)\) whenever the finite-star products are used in KM's strip condition. Both products lie in the finite linear domain by WG. The identity automorphism group preserves \(\tau\), and the constant function \(\tau(xy)\) is its bounded continuous holomorphic KMS strip function, with upper boundary \(\tau(yx)\). KM uniqueness therefore proves

\[
 \sigma_t^\tau=\operatorname{id}_M,\qquad M_\tau=M.
 \tag{PT.23}
\]

Every \(\psi\) is invariant under this group. PT-06 applies and proves the claim. \(\square\)

There is a useful form interpretation which retains all infinite values. For \(x\in M_+\), define

\[
 x^{1/2}hx^{1/2}
     =\sup_{\varepsilon>0}x^{1/2}h_\varepsilon x^{1/2}
       \quad\text{in }\widehat M_+.
 \tag{PT.24}
\]

This is a positive form whose energy at a vector \(\xi\) is
\(\|h^{1/2}x^{1/2}\xi\|^2\) when \(x^{1/2}\xi\in D(h^{1/2})\), and infinity otherwise. Its finite domain may be nondense, so (PT.24) is an extended positive, not an assertion of dense definition for an operator product. At every bounded regularization the trace identity, applied to \(x^{1/2}h_\varepsilon^{1/2}\), gives

\[
 \tau(h_\varepsilon^{1/2}xh_\varepsilon^{1/2})
     =\tau(x^{1/2}h_\varepsilon x^{1/2}).
\]

Taking suprema and applying CW-03 yields the all-positive formula

\[
 \tau_h(x)=\widehat\tau(x^{1/2}hx^{1/2}).
 \tag{PT.25}
\]

In particular

\[
 \tau_h(1)=\widehat\tau(h).
 \tag{PT.26}
\]

The general extension (PT.20) also applies for every \(H\in\widehat M_+\). These identities concern actual extended-positive evaluation and do not depend on finite GNS multiplier sandwiches.

## Finite mass identifies the trace predual density

Let \(\tau\) be faithful normal semifinite and let \(h\) be the density of a normal semifinite weight \(\psi\) obtained in PT-08. Then the following are equivalent:

\[
 \psi(1)<\infty,\qquad
 \widehat\tau(h)<\infty,\qquad
 h\in L^1(M,\tau)_+.
 \tag{PT.27}
\]

When these conditions hold, \(\psi\) extends uniquely to a bounded normal positive functional on \(M\), and

\[
 \psi(a)=\tau(ha)\quad(a\in M),\qquad
 \|\psi\|=\psi(1)=\|h\|_1 .
 \tag{PT.28}
\]

The product and complex trace in (PT.28) are the measurable product and continuous trace from TI-05–06. In particular the PT density and the TI predual density are the same affiliated operator, including its domain.

**Proof.** PT-08 gives \(\psi(1)=\widehat\tau(h)\) before any measurability assumption. Suppose this value is \(C<\infty\). For \(r>0\), spectral calculus and order preservation in CW-03 give

\[
 r\,\tau(1_{(r,\infty)}(h))\leq\widehat\tau(h)=C .
 \tag{PT.29}
\]

This order comparison is first an inequality of spectral energies; all evaluations are of nonnegative extended values. Hence the traces of the high spectral tails tend to zero. The full spectral-tail criterion MT-11 applies to the already densely defined positive self-adjoint \(h\), and proves that \(h\) is \(\tau\)-measurable. For a measurable positive operator, the spectral integral in MT-13 and the extension in CW-03 agree: both are suprema of the traces of the bounded spectral truncations. Thus \(\tau(h)=C\), so \(h\in L^1_+\). Conversely, \(h\in L^1_+\) gives \(\widehat\tau(h)=\tau(h)<\infty\), proving (PT.27).

For completeness, \(\psi(a)\leq C\|a\|\) on bounded positives. Every element of \(M\) is a linear combination of four positives, so the finite linear extension from WG-003–004 is defined on all of \(M\). Its positive-functional Cauchy–Schwarz inequality gives \(|\psi(a)|\leq C\|a\|\), with equality of the norm at \(a=1\); normality is the normality of the original weight.

The bounded regularizations \(h_\varepsilon\) are integrable and

\[
 \|h-h_\varepsilon\|_1
 =\int_{[0,\infty)}
       \left(s-\frac{s}{1+\varepsilon s}\right)
                       d(\tau\circ E_h)(s)\longrightarrow0 .
 \tag{PT.30}
\]

Indeed the nonnegative integrands tend pointwise to zero and are dominated by the integrable function \(s\); any infinite mass at zero contributes zero. This is also TI-05's regularization estimate. For \(a\geq0\), bounded trace cyclicity gives

\[
 \tau(h_\varepsilon^{1/2}a h_\varepsilon^{1/2})
       =\tau(h_\varepsilon a).
\]

TI-05–06 and (PT.30) let the right side tend to \(\tau(ha)\); the left side increases to \(\psi(a)\) by PT-08. Linear extension gives (PT.28) for all \(a\). TI-06 identifies this as the unique positive predual density. Its norm identity is exactly \(C=\tau(h)\). \(\square\)

This proof uses no sequence of finite projections exhausting the algebra. The spectral cutoffs of one operator suffice. If \(C=\infty\), the density still exists by PT-08, but (PT.29) yields no measurability conclusion; PT-10 gives a counterexample.

## Models separating the hypotheses

**An arbitrary counting algebra.** Let \(I\) be any set, let \(M=\ell^\infty(I)\) act diagonally on \(\ell^2(I)\), and set

\[
 \tau(a)=\sum_{i\in I}a_i,\qquad
 \psi(a)=\sum_{i\in I}c_i a_i,\qquad a\in M_+,
 \tag{PT.31}
\]

where each \(c_i\) is a finite nonnegative real number. Every sum denotes the supremum of its finite subsums. Both weights are normal: for a bounded increasing net of positive functions, each finite sum commutes with its coordinatewise supremum, and then the two suprema commute. Finite-coordinate projections increase to \(1\) and have finite weight. WG-008 proves semifiniteness. The reference \(\tau\) is faithful.

The density is the multiplication operator

\[
 (h\xi)_i=c_i\xi_i,\qquad
 D(h)=\left\{\xi\in\ell^2(I):
                   \sum_i c_i^2|\xi_i|^2<\infty\right\}.
 \tag{PT.32}
\]

Finite-coordinate vectors form a dense domain. The real multiplication operator with this maximal square-summability domain is self-adjoint by spectral calculus, is positive, and has diagonal spectral projections. Thus it is affiliated with \(M\). Its support is the indicator of \(\{i:c_i>0\}\). Its regularizations multiply by \(c_i/(1+\varepsilon c_i)\); interchanging the supremum over finite sets with the increasing regularization limit verifies (PT.31) directly.

Taking \(I=\mathbb N\) and \(c_n=n\) gives a faithful normal semifinite weight whose density is not \(\tau\)-measurable: every high spectral tail has infinite counting trace. Taking \(c_n=2^{-n}\) gives a faithful bounded normal functional of norm one. More generally, for arbitrary \(I\), if \(\sum_i c_i<\infty\), each set \(\{i:c_i\geq1/m\}\) is finite. Hence the support is countable. This is a consequence of finite mass in this model, not a countability assumption in the theorem.

**An invariant weight with noncentral support.** On \(M_3(\mathbb C)\), put

\[
 \rho=\operatorname{diag}(1,1,3),\quad
 v=2^{-1/2}(1,1,0),\quad p=vv^*,\quad h=2p,\quad
 \varphi(a)=\operatorname{Tr}(\rho a).
 \tag{PT.33}
\]

The finite-dimensional weight is faithful, normal and semifinite. Its modular group is \(\rho^{it}a\rho^{-it}\). To check the formula, diagonalize \(\rho\); each matrix entry has an entire exponential orbit, and
\(\operatorname{Tr}(\rho x\,\sigma_{-i}(y))
=\operatorname{Tr}(\rho yx)\). Together with trace cyclicity and finite-dimensional boundedness on the KMS strip, this is the KM-01 boundary condition; KM uniqueness identifies the group. The projection \(p\) commutes with \(\rho\), so it lies in \(M_\varphi\), while it is a nonzero proper projection in a factor and therefore is not central.

Here \(\rho h=h\). For \(a\geq0\), regularization and bounded cyclicity give

\[
 \varphi_h(a)=\operatorname{Tr}(ha)=2\langle av,v\rangle .
 \tag{PT.34}
\]

Its support is \(p\). The normalized supported family from PT-06 is \(2^{it}p\), with value \(p\) at zero; it is not a unitary on the three-dimensional ambient space. This calculation displays exactly why fixed support and central support are different requirements.

**Why semifiniteness of the numerator is necessary.** On the scalar algebra define \(\chi(0)=0\) and \(\chi(s)=\infty\) for \(s>0\). This is a normal weight: a positive increasing net with nonzero supremum has a positive member, so both sides of the normality identity are infinite; at supremum zero both are zero. It is invariant under the trivial reference modular group. Its finite positive cone is \(\{0\}\), so it is not semifinite. Every densely defined self-adjoint operator on the one-dimensional Hilbert space is a finite scalar. Such a density has finite value at \(1\), and cannot represent \(\chi\). An infinite extended positive could encode \(\chi\), but it is not the densely defined self-adjoint density asserted in PT-06.

## Problems with complete solutions

**Problem 1: normalization detects a scalar multiple.** Let \(c>0\) and let \(\varphi\) be faithful normal semifinite. Compute \([D(c\varphi):D\varphi]_t\) and compare the two modular groups.

**Solution.** The density \(h=c1\) lies in the centralizer. Its regularizations are \(c/(1+\varepsilon c)\,1\), so \(\varphi_h=c\varphi\), on all positives including those of infinite weight. PT-04 gives the cocycle \(c^{it}1\). CZ-11 shows the modular groups are equal because this unitary is scalar. If \(M\ne0\), faithfulness and semifiniteness provide some nonzero finite positive element of strictly positive weight. Thus \(c\varphi=\varphi\) forces \(c=1\). Equality of modular groups alone loses the normalization which the cocycle retains. In the zero algebra all weights and operators coincide.

**Problem 2: ordered weights do not require ordered sandwiches.** On \(M_2(\mathbb C)\), let the reference be the usual trace and put

\[
 h=\begin{pmatrix}1&0\\0&4\end{pmatrix},
 \qquad A=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

Show that the sandwiches for \(\varepsilon=1\) and \(\varepsilon=1/4\) are not ordered, even though their trace values increase as \(\varepsilon\) decreases.

**Solution.** They are \(ww^*\) and \(zz^*\), where

\[
 w=(1/\sqrt2,\,2/\sqrt5),\qquad
 z=(2/\sqrt5,\,\sqrt2).
\]

For two real two-dimensional vectors,
\(\det(zz^*-ww^*)=-(z_1w_2-z_2w_1)^2\).
Here it is \(-(4/5-1)^2=-1/25\), so the difference has one negative and one positive eigenvalue. It is neither positive nor negative. Its trace nevertheless is
\((4/5+2)-(1/2+4/5)=3/2>0\).
Thus increasing evaluated weights in PT-07 do not imply monotonicity of the sandwiched operators.

**Problem 3: the measurable density is the same operator.** Suppose \(\psi\in M_*^+\), and let \(h\) be its density from PT-08 and \(k\in L^1_+\) its density from TI-06. Prove \(h=k\) as closed operators.

**Solution.** A bounded positive normal functional is a normal semifinite weight because its finite cone is all of \(M_+\). PT-09 therefore applies to \(h\), and proves both \(h\in L^1_+\) and \(J(h)=\psi\) for the isometry \(J\) in TI-06. Since also \(J(k)=\psi\), its injectivity gives equality in the measurable algebra. MT-08–11 identify its elements with actual closed operators, so the equality includes domains. No hypothesis of faithfulness of \(\psi\) is needed; the zero functional yields \(h=k=0\).

**Problem 4: inverse density on the actual support.** Let \(\psi=\varphi_h\) be invariant with support \(p\ne0\), possibly \(p\ne1\). Recover the reference restricted to \(pMp\) from \(\psi|_{pMp}\), and explain what remains unrecovered on \(M\).

**Solution.** The operator \(k=h|_{pH}\) is positive and injective. PT-05 inside \(pMp\) gives

\[
 \varphi_p=(\psi_p)_{k^{-1}},\qquad
 D(k^{-1})=\operatorname{ran}k\subseteq pH .
\]

The range is dense because \(k\) is self-adjoint and injective; the inverse need not be bounded. Extending \(k^{-1}\) by zero and lifting the recovered weight gives the compressed weight \(x\mapsto\varphi(pxp)\), supported on \(p\). If \(p\ne1\), the original faithful \(\varphi\) has \(\varphi(1-p)>0\), possibly infinite, whereas the lift has value zero there. Thus inversion recovers the exact reference corner, not the lost complementary weight. The zero-support case contains only the zero corner and has no nontrivial inverse density.

## Where the characterization enters the course

The main equivalence is assembled in an order that keeps its normalization visible: PT-02 proves naturality from the balanced matrix cocycle; PT-03 identifies its affiliated positive generator; PT-04 computes the exact cocycle of the regularized density; PT-05 uses fixed-reference injectivity to identify the weight on every positive element. The inputs are SI-05/14, CX-02/10, KM-06 and CZ-05–11, with spectral domains supplied by SK-05/07/08. PT-06 then uses WS-04–06 and the centralizer-corner restriction in CZ-09. PT-07 applies CW-02–04 to retain all extended positive energies.

The trace specialization PT-08 supplies the arbitrary normal semifinite weight density used in Takesaki II, IX.2.12. PT-09 shows exactly when this density is the measurable integrable operator in TI-06: finite mass at the identity. The TI proof of the predual theorem does not depend on this characterization, so this comparison creates no circular proof route. The nonmeasurable model in PT-10 explains why the unbounded-weight statement is a strictly different assertion from the bounded-functional predual theorem.

Two natural next questions are to transport these supported densities through a correspondence, and to replace a scalar-valued weight by an operator-valued one. The first requires the still separate fusion and spatial-domain arguments; the second requires an extended-positive target together with normality, composition and domain proofs. An equality of scalar weights does not supply either construction automatically. OA-FLOW imports the centralizer-affiliated density interface for its crossed-product work and retains ownership of dual weights and action cocycles.

The characterization proved here assumes a faithful normal semifinite reference and a normal semifinite numerator. It permits zero and nonfaithful numerators, noncentral support, unbounded densities and unbounded inverses on support, arbitrary Hilbert spaces, and infinite positive evaluations. It does not assign a whole-algebra modular group to a nonfaithful numerator or assert a densely defined density for an arbitrary nonsemifinite weight. The scalar counterexample makes the latter boundary substantive.

