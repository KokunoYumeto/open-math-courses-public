# Local L-factors and epsilon factors

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A local L-factor uses the Frobenius action on inertia-fixed vectors. An epsilon factor also records ramification, an additive character and a measure. We prove the formal properties of the first, reconstruct the existence and uniqueness of the second, and derive its transformation formulas. The normalization matters: an unnormalized epsilon constant need not have absolute value one.

We assume Conductors of Weil-group representations, with the actual earlier analytic and finite-group proofs identified in the dependency paragraph at the end. Section 2 proves the nonarchimedean character equation in either characteristic; §3 proves the dimension-zero refinement of integer Brauer induction. Representations are smooth and finite-dimensional over \(\mathbb C\), with geometric reciprocity and \(\|\Phi_F\|=q_F^{-1}\). Write \(\omega_s=\|\cdot\|^s\). For a nontrivial continuous unitary additive character \(\psi:F\to\mathbb C^\times\), put
\[
n_F(\psi)=\max\{m\in\mathbb Z: \psi\text{ is trivial on }\mathfrak p_F^{-m}\}.
\tag{1}
\]
Thus a character trivial on \(\mathcal O_F\) but not on \(\mathfrak p_F^{-1}\) has \(n_F(\psi)=0\). Haar measures are positive. Fourier transforms use the kernel \(\psi(xy)\). The measure dual to \(dx\), denoted \(dx'\), is the one making the second transform send \(f(x)\) to \(f(-x)\). A self-dual measure is denoted \(dx_\psi\).

## 1. Local L-factors

For a nonarchimedean field define
\[
L_F(s,V)=\det(1-q_F^{-s}\rho(\Phi_F)\mid V^{I_F})^{-1}.
\tag{2}
\]
Frobenius preserves \(V^{I_F}\) because it normalizes inertia. Another geometric lift differs by an inertia element and has the same action on that space. Thus the definition is independent of the lift. If the fixed space is zero, the determinant of the zero-dimensional space is one, and so is the L-factor.

**Theorem 1.1.** L-factors are multiplicative in exact sequences. For every finite separable extension \(E/F\),
\[
L_F(s,\operatorname{Ind}_{W_E}^{W_F}V)=L_E(s,V).
\tag{3}
\]

**Proof of multiplicativity.** Inertia has finite image on the representations in an exact sequence. Its invariants are exact by averaging, so the Frobenius matrix on the middle fixed space is block upper triangular with diagonal blocks the two outer Frobenius matrices. The determinant in (2) is their product. Direct-sum multiplicativity follows in particular. \(\square\)

**Proof of induction.** Let \(f=f(E/F)\) and \(q_E=q_F^f\). In the finite-index tensor model of induction, the left cosets of \(W_E\) fall into \(f\) inertia orbits, represented by
\(1,\Phi_F,\ldots,\Phi_F^{f-1}\). This is because their images in the residue-degree quotient are \(\mathbb Z/f\mathbb Z\). Invariants on the orbit of \(1\) identify with \(V^{I_E}\): a vector on one coset determines an invariant sum over that orbit, and the stabilizer of the base coset is \(I_E=I_F\cap W_E\). Transport gives the same identification on every orbit. Thus the full inertia-fixed space is a sum of \(f\) copies of \(V^{I_E}\).

Frobenius cycles these copies. Write \(\Phi_F^f=i h\), with \(i\in I_F\) and \(h\in W_E\) of degree one over \(E\); this is possible since \(\Phi_F^f\in I_FW_E\). On returning to the first copy the action is \(A=\rho(h)|_{V^{I_E}}\), the geometric Frobenius action for \(E\). The factor \(i\) acts trivially on the induced inertia invariants. With transported identifications the other transition maps are identities.

A cyclic block operator of this form satisfies
\[
\det(1-tT)=\det(1-t^f A).
\tag{4}
\]
To verify (4), triangularize \(A\). Its preserved flag gives a flag of cyclic-block spaces; on the successive quotients the cyclic scalar operator has characteristic polynomial \(X^f-\alpha\), where \(\alpha\) is the corresponding diagonal entry of \(A\). Multiplying their determinants gives (4), even when \(A\) has Jordan blocks. Substituting \(t=q_F^{-s}\) gives \(t^f=q_E^{-s}\), which proves (3). \(\square\)

For an unramified character with \(\chi(\Phi)=c\),
\[
L_F(s,\chi)=(1-cq_F^{-s})^{-1}.
\]
A ramified character has no inertia-fixed vector and has factor one. These are the one-dimensional factors in Tate's local theory when characters are transported by geometric reciprocity.

At infinity set
\[
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),
\qquad \Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s).
\]
For the real character \(\operatorname{sgn}^\epsilon|\cdot|^t\), the factor is \(\Gamma_{\mathbb R}(s+t+\epsilon)\). For
\(\omega_{a,n}(re^{i\theta})=r^a e^{in\theta}\) on \(W_{\mathbb C}\), it is
\[
L_{\mathbb C}(s,\omega_{a,n})
=\Gamma_{\mathbb C}\!\left(s+\frac{a+|n|}{2}\right).
\tag{5}
\]
The factor of the irreducible real induction of \(\omega_{a,n}\), \(n\ne0\), is the same expression. The character gamma integrals and functional equations are actually proved in the earlier programme lesson *Archimedean local factors* (NT-ADL-08), Proposition 8.2 and Theorem 8.1, using its Gaussian tests and two-variable Fourier argument. Products define the factor for a semisimple representation; for a general one use its composition factors. Theorem 5.1 of the preceding lesson proves that this covers all constituents.

The induction identity when \(n=0\) follows from
\[
\Gamma_{\mathbb R}(z)\Gamma_{\mathbb R}(z+1)=\Gamma_{\mathbb C}(z),
\]
which is proved by the beta-integral computation in NT-ADL-08, Proposition 8.4, equations (30)–(33), after substituting the displayed definitions. Indeed the reducible induction has the two real characters \(|\cdot|^{a/2}\) and \(\operatorname{sgn}|\cdot|^{a/2}\). No arithmetic/geometric Frobenius choice is involved at infinity; the character parametrization is the one of the preceding lesson.

## 2. The character functional equation

For a quasi-character \(\chi\) of \(F^\times\), Tate's functional equation gives a nonzero constant \(\epsilon_F(\chi,\psi,dx)\). We use the convention characterized by
\[
\frac{Z(\widehat f,\chi^{-1}|\cdot|)}{L_F(1,\chi^{-1})}
=\epsilon_F(\chi,\psi,dx)
\frac{Z(f,\chi)}{L_F(0,\chi)},
\tag{6}
\]
where \(Z(f,\chi)=\int_{F^\times}f(x)\chi(x)d^\times x\); equivalently one may move the \(s\)-parameter into \(\chi|\cdot|^s\). Equation (6) is interpreted by meromorphic continuation where the initial integrals or displayed denominators do not define an ordinary number. We prove it below. The freely readable IAS author text of Deligne, §§3.3–3.4, fixes the same convention.

For nonarchimedean \(F\), the character formulas needed are
\[
\begin{aligned}
\epsilon_F(\chi,\psi,b\,dx)&=b\epsilon_F(\chi,\psi,dx),\\
\epsilon_F(\chi,\psi_a,dx)&=\chi(a)|a|_F^{-1}\epsilon_F(\chi,\psi,dx),\\
\epsilon_F(\chi\omega_s,\psi,dx)&=
\epsilon_F(\chi,\psi,dx)q_F^{-(a_F(\chi)+n_F(\psi))s},
\end{aligned}
\tag{7}
\]
with \(b>0\), \(a\in F^\times\), and \(\psi_a(x)=\psi(ax)\). Fourier inversion also gives
\[
\epsilon_F(\chi,\psi,dx)
\epsilon_F(\chi^{-1}\omega_1,\psi_{-1},dx')=1.
\tag{8}
\]
For an unramified \(\chi\), its constant is
\[
\epsilon_F(\chi,\psi,dx)=
\chi(\varpi_F)^{n_F(\psi)}q_F^{n_F(\psi)}\operatorname{vol}_{dx}(\mathcal O_F).
\tag{9}
\]
In particular it is one if \(n_F(\psi)=0\) and \(\operatorname{vol}(\mathcal O_F)=1\).

**Lemma 2.1 (Fourier inversion and the character equation).** Equations (6)–(9) hold for every nonarchimedean local field, in either characteristic. If \(c=a_F(\chi)>0\), \(m=\operatorname{vol}_{dx}(\mathcal O_F)\), \(n=n_F(\psi)\), and \(v_F(b)=c+n\), then
\[
\epsilon_F(\chi,\psi,dx)
=m q_F^n\chi(b)
\sum_{u\in(\mathcal O_F/\mathfrak p_F^c)^\times}
\chi(u)^{-1}\psi(u/b).
\tag{9A}
\]

**Proof.** For a coset of an additive ideal, translation invariance and the sum of a nontrivial finite character give
\[
\widehat{1_{a+\mathfrak p^r}}(y)
=m q^{-r}\psi(ay)1_{\mathfrak p^{-r-n}}(y).
\tag{9B}
\]
Indeed the integral of a character on the compact group \(\mathfrak p^r\) is zero unless the character is trivial: translate by an element on which it is nontrivial. Its annihilator is \(\mathfrak p^{-r-n}\), by the definition of \(n\). Every locally constant compactly supported function is a finite linear combination of these indicators. Applying (9B) twice proves Fourier inversion, with dual integral-ring volume \(m'=q^{-n}/m\); in particular self-duality means \(m=q^{-n/2}\).

Normalize \(d^\times x\) by unit volume one. Write \(\chi=\eta|\cdot|^s\) with \(\eta\) unitary, moving any real growth on a uniformizer into \(s\). Splitting \(F^\times\) into valuation shells shows that \(Z(f,\chi)\) is a finite Laurent polynomial in \(q^{-s}\), plus a geometric tail near zero when \(\eta\) is unramified. Dividing by the corresponding L-factor removes that tail. If \(\eta\) is ramified, the tail is zero by averaging units. Thus the normalized integral is a Laurent polynomial, and a normalized test with value one exists: use \(1_{\mathcal O}\) in the unramified case and \(\eta^{-1}1_{\mathcal O^\times}\) in the ramified case.

For \(0<\operatorname{Re}s<1\), the following cross identity proves proportionality of the two normalized integrals:
\[
Z(f,\chi)Z(\widehat g,\chi^{-1}|\cdot|)
=Z(g,\chi)Z(\widehat f,\chi^{-1}|\cdot|).
\tag{9C}
\]
To check it, write \(d^\times x=\kappa\,dx/|x|\). In the product on the left put \(y=xz\). Apart from \(\kappa^2\), the resulting integral is
\(\int \chi(z)^{-1}\int f(x)\widehat g(zx)dx\,dz\).
The inner integral equals \(\int\widehat f(zt)g(t)dt\), by expanding the transform and interchanging the two compact additive integrals. Substitution back gives the right side. The original double integrals converge absolutely in the indicated strip; equivalently the substituted integrals are absolutely integrable by the same change of variables. Rational continuation in \(q^{-s}\) proves (9C) everywhere. A test with normalized value one now defines (6). Applying Fourier inversion shows that its coefficient is nonzero and gives (8).

The transform of \(1_{\mathcal O}\) in (9B), followed by its geometric shell sum, gives (9). In the ramified case transform \(f=\chi^{-1}1_{\mathcal O^\times}\). Averaging over unit translates shows that its transform vanishes unless \(v(y)=-c-n\). For \(v(y)>-c-n\), translate by an element of \(U^{c-1}\) on which \(\chi\) is nontrivial; the additive factor is unchanged. For \(v(y)<-c-n\), average over the additive cosets of \(\mathfrak p^c\) on which \(f\) is constant and use (9B). At \(y=w/b\), \(w\) a unit, the transform is
\(m q^{-c}\chi(w)\sum_u\chi(u)^{-1}\psi(u/b)\).
Its dual zeta integral therefore equals the right side of (9A), since \(|b|^{-1}=q^{c+n}\), whereas its original zeta integral is one. This proves (9A), including the nonvanishing of its sum.

Scaling \(dx\) scales the transform. For \(\psi_a\), the transform is \(\widehat f(ay)\), and substitution in its zeta integral supplies \(\chi(a)|a|^{-1}\). These prove the first two lines of (7). Formula (9A), or (9) when \(c=0\), supplies the third, because an unramified twist evaluates on \(b\) by \(q^{-(c+n)s}\). Double Fourier inversion proves (8); the reflection \(f(-x)\) accounts for its negative additive character. No characteristic-zero assumption entered this proof. \(\square\)

At infinity the earlier NT-ADL-08 proof has negative trace character. Replacing it by its negative multiplies its real phase by \((-1)^\epsilon\) and its complex phase by \((-1)^n\), by the same substitution just used. For the positive characters \(e^{2\pi ix}\) on \(\mathbb R\) and \(e^{4\pi i\operatorname{Re}z}\) on \(\mathbb C\), with self-dual measures, the phases are consequently \(i^\epsilon\) and \(i^{|n|}\). Proposition 8.3 there and its Fourier-inversion proof also give (8) at infinity. Arbitrary nontrivial additive characters and positive measures follow by scaling.

**Lemma 2.2 (trace conductor).** For finite separable \(E/F\), with different exponent \(d_{E/F}\),
\[
n_E(\psi\circ\operatorname{Tr}_{E/F})=e(E/F)n_F(\psi)+d_{E/F}.
\tag{9D}
\]
Moreover \(\operatorname{Tr}_{E/F}(\mathfrak p_E^r)=
\mathfrak p_F^{\lfloor(r+d_{E/F})/e\rfloor}\).

**Proof.** The trace dual (1D) in the preceding lesson is \(\mathfrak p_E^{-d}\). Thus \(\operatorname{Tr}(\mathfrak p_E^r)\subseteq\mathfrak p_F^t\) exactly when \(\mathfrak p_E^r\subseteq\mathfrak p_F^t\mathfrak p_E^{-d}\), or \(r\ge et-d\). Trace of an ideal is an ideal: it is an \(\mathcal O_F\)-module and a finite lattice. Its largest possible exponent is therefore the displayed floor. The largest fractional ideal on which \(\psi\) is trivial is \(\mathfrak p_F^{-n_F}\). Applying the trace formula, or the same trace-dual inclusion with \(t=-n_F\), proves that the annihilator of \(\mathcal O_E\) under \(\psi\operatorname{Tr}(xy)\) is \(\mathfrak p_E^{-e n_F-d}\). This is (9D). \(\square\)

## 3. Existence and uniqueness of local constants

**Theorem 3.0 (Langlands–Deligne existence).** There is a family of nonzero constants \(\epsilon_F(V,\psi,dx)\), for all local fields and representations, with the following four properties.

1. For \(0\to V'\to V\to V''\to0\), the constant is \(\epsilon(V')\epsilon(V'')\).
2. Scaling the Haar measure by \(b>0\) multiplies it by \(b^{\dim V}\).
3. If \(U\) is a virtual representation of \(W_E\) of dimension zero, then
   \(\epsilon_F(\operatorname{Ind}U,\psi)=\epsilon_E(U,\psi\circ\operatorname{Tr}_{E/F})\).
4. In dimension one the constant is the character constant from Tate's theory, using geometric reciprocity.

Multiplicativity allows virtual representations by taking quotients of constants. Property 2 makes their constants independent of measure when their virtual dimension is zero, so the omitted measure in property 3 is justified. These properties concern a family over extensions of the field, not a function at just one fixed field. The proof below checks every relation between Brauer decompositions; this is the substantive existence step.

We first prove **dimension-zero Brauer induction**: for a finite group \(G\), every virtual representation \(Y\) of dimension zero over \(\mathbb C\) is an integer sum
\[
Y=\sum_j m_j\operatorname{Ind}_{H_j}^G(\chi_j-1),
\tag{10}
\]
where \(\chi_j\) is one-dimensional.

**Proof of (10).** The actual earlier integer theorem is *Brauer's induction theorem* (RT-FIN-11), Theorem 5.1, with its local induction proof in §§3–4. In particular \(1_G=\sum_E\operatorname{Ind}_E^G z_E\), where the \(E\) are elementary, hence nilpotent. Its projection formula gives
\(Y=\sum_E\operatorname{Ind}_E^G(\operatorname{Res}_E Y\,z_E)\), and every expression inside parentheses has dimension zero. It remains to prove (10) for a nilpotent group \(N\).

We strengthen the weight-space proof of nilpotent monomiality in RT-FIN-11, Theorem 1.2: if an irreducible \(\rho\) is induced from a line on \(H\), we may require \(Z(N)\subseteq H\). Here are the extra details. The construction there can keep any prescribed central scalar subgroup in every inducing subgroup. When passing through the kernel, its image remains central; pulling the inducing subgroup back preserves it. In the faithful nonabelian step, choose the normal abelian subgroup containing the centre in Lemma 1.1 there. The stabilizer of a weight contains that centre, and the weight space carries it by scalars. Induction on the smaller stabilizer therefore preserves the prescribed subgroup. The abelian stopping case is already a line. This proves the strengthened assertion.

Induct on \(|N|\). For an irreducible \(\rho=\operatorname{Ind}_H^N\chi\), of dimension \(d=[N:H]\), write
\[
\rho-d1=\operatorname{Ind}_H^N(\chi-1)
 +\bigl(\operatorname{Ind}_H^N1-[N:H]1\bigr).
\tag{10A}
\]
The second term has dimension zero and factors through \(N/Z(N)\), since the centre is contained in \(H\). A nontrivial nilpotent group has nontrivial centre, as proved by the central-series argument in RT-FIN-11 §1, so this quotient has smaller order. Inflate its induction decomposition, using the identical coset models for inverse images of subgroups. If \(N\) is abelian, each irreducible is a line and there is nothing to reduce. Finally write an arbitrary virtual dimension-zero character as a sum of the differences \(\rho-(\dim\rho)1\). This proves (10). \(\square\)

### 3A. A finite relation criterion

Fix a finite Galois extension \(L/F\), with group \(G\), and a character \(\alpha\) of \(F^\times\). For \(H\leq G\), put \(E_H=L^H\) and \(\alpha_H=\alpha\circ N_{E_H/F}\). Let \(P_0(G)\) be the free abelian group on symbols \((H,\chi-1)\), for all one-dimensional characters of \(H\). Its map
\[
b:P_0(G)\longrightarrow R_0(G),\qquad
(H,\chi-1)\longmapsto\operatorname{Ind}_H^G(\chi-1)
\tag{10B}
\]
is onto by (10). Define its formal character product
\[
C_\alpha(r)=\prod_j
\left(\frac{\epsilon_{E_{H_j}}(\chi_j\alpha_{H_j},\psi\operatorname{Tr})}
{\epsilon_{E_{H_j}}(\alpha_{H_j},\psi\operatorname{Tr})}\right)^{m_j}
\quad\text{for }r=\sum_jm_j(H_j,\chi_j-1).
\tag{10C}
\]
Each quotient is independent of measure. An \(\alpha\)-theory on all subgroups of \(G\), with rank-one value \(\epsilon(\chi\alpha_H)\), exists if and only if
\[
C_\alpha(r)=1\quad(r\in\ker b).
\tag{10D}
\]
Necessity follows by induction and multiplicativity. For sufficiency, lift \(V-(\dim V)1\) through (10B), take (10C), and multiply by \(\epsilon(\alpha_H)^{\dim V}\) when constructing the theory over \(E_H\). Two lifts differ by a kernel relation. A kernel relation for \(H\) induces to one for \(G\), so (10D) works simultaneously over every subgroup. Induction in stages on the symbols proves the rank-zero induction property. A character \(\chi\) has the lift \((H,\chi-1)\) over its own field, giving exactly its required character value. The resulting homomorphism on each representation group is multiplicative and has measure degree \(\dim V\). This proves the criterion, including all its subgroup compatibilities.

The criterion is unchanged on replacing \(\alpha\) by an unramified twist \(\alpha\beta\), or on replacing \(\psi\) by \(\psi_a\). Indeed the formal quotient for \(\beta\) is
\(\beta(\varpi_F)^{a_F(b(r)\otimes\alpha)}\), by (7) and the dimension-zero induction formula in the preceding lesson, Theorem 4.1. It is one when \(b(r)=0\). The additive change is \(\det(b(r)\otimes\alpha)(a)\), by the determinant/transfer calculation in the preceding Weil lesson, Theorem 4.1; it too is one. The calculation applies to every smooth character \(\alpha\), since that conductor formula was proved for arbitrary smooth representations. Thus no finite-order assumption on an unramified twist is hidden here.

### 3B. A local theory after a sufficiently ramified twist

**Lemma 3.0a (a bounded stationary-phase calculation).** Suppose a character \(\alpha\) has conductor \(c>0\), and for some \(r\geq\lceil c/2\rceil\) and \(y\) of value \(-c-n_F(\psi)\),
\[
\alpha(1+z)=\psi(yz)\quad(z\in\mathfrak p_F^r).
\tag{10E}
\]
If \(a_F(\eta)\leq c-r\), then
\[
\epsilon(\eta\alpha,\psi,dx)=\eta(y)^{-1}\epsilon(\alpha,\psi,dx).
\tag{10F}
\]

**Proof.** Its conductor is still \(c\), since \(a_F(\eta)<c\). Formula (9A), converted from a unit sum to an additive integral, is
\(\epsilon(\alpha)=\int_{v(x)=-c-n}\alpha(x)^{-1}\psi(x)dx\).
Average this integral under the measure-preserving unit substitutions \(x\mapsto x(1+z)\), \(z\in\mathfrak p^r\). The factor inserted is \(\psi((x-y)z)\). Finite-character orthogonality therefore kills the integral off
\(v(x-y)\geq-r-n\), or \(x/y\in1+\mathfrak p^{c-r}\). On that set \(\eta(x)=\eta(y)\); the same averaging works for \(\eta\alpha\), since \(\eta\) is trivial on \(1+\mathfrak p^r\). Taking this constant factor outside proves (10F). All integrals are finite sums on compact shells, so the averaging introduces no convergence issue. \(\square\)

There are characters of arbitrarily high conductor: the quotient \(U^{m-1}/U^m\simeq(k_F,+)\) for \(m\geq2\) has a nontrivial character. Extend it to the finite abelian unit quotient, and set a value on a uniformizer. The extension assertion is elementary: a character of a subgroup of a finite abelian group extends on adjoining a generator by choosing a root of its prescribed power; repeat until the group is exhausted.

Choose \(\alpha\) of very large conductor \(m\). On \(1+\mathfrak p^{\lceil m/2\rceil}\), multiplication reduces to addition modulo \(\mathfrak p^m\). The resulting additive character has the form \(\psi(yz)\), with \(v_F(y)=-m-n_F\). To see both existence and this value, the annihilator calculation in (9B) identifies the dual of \(\mathfrak p^r/\mathfrak p^m\) with \(\mathfrak p^{-m-n}/\mathfrak p^{-r-n}\); the two finite groups have the same order and that pairing is nondegenerate. Nontriviality on the last layer forces the asserted valuation.

For each of the finitely many subfields \(E=L^H\), write \(e=e(E/F)\), \(d=d_{E/F}\). If \(z\in\mathfrak p_E^r\), expansion of the norm as a product of conjugates gives
\[
N_{E/F}(1+z)=1+\operatorname{Tr}_{E/F}z+R,
\qquad v_F(R)\geq 2r/e.
\tag{10G}
\]
Every term in \(R\) is a product of at least two conjugates, all of extended base value at least \(r/e\). Choose \(r_E=\lceil em/2\rceil\). For large \(m\) the trace is integral and the error lies in \(\mathfrak p_F^m\); hence
\(\alpha_E(1+z)=\psi(\operatorname{Tr}(yz))\) on \(\mathfrak p_E^{r_E}\). Its conductor is exactly \(m_E=em-d\). Indeed apply (10G) also at the deeper exponents \(em-d\) and \(em-d-1\); Lemma 2.2 says their traces are respectively \(\mathfrak p_F^m\) and \(\mathfrak p_F^{m-1}\). The error is still killed, so the first layer is trivial and the second is not. Also \(v_E(y)=-m_E-n_E\), by (9D).

Take \(m\) so large that \(m_E-r_E\) exceeds the conductors of every character of every subgroup of \(G\). There are only finitely many such characters. Lemma 3.0a now proves, simultaneously over all \(E_H\),
\(\epsilon(\chi\alpha_H)=\chi(y)^{-1}\epsilon(\alpha_H)\).
Consequently
\[
\epsilon_{\alpha,H}(V)
=\det V(y)^{-1}\epsilon_{E_H}(\alpha_H)^{\dim V}
\tag{10H}
\]
is an \(\alpha\)-theory: its rank-zero induction property is exactly determinant transfer evaluated on \(y\in F^\times\). This proves (10D) for a sufficiently ramified \(\alpha\), by an actual local calculation. This qualitative bound is enough for existence; it does not assert the sharp half-break theorem of §7.

### 3C. Globalization and the relation check

We need two concrete globalization facts. First, every finite Galois local extension \(L/F\) occurs as the completion of a finite Galois extension \(M/K\), whose whole Galois group is its decomposition group at the specified place, with \(K_v=F\). Here is a construction. In characteristic zero, approximate the separable primitive polynomial of \(F/\mathbb Q_p\) by a polynomial over \(\mathbb Q\). Root approximation and Krasner's inequality, proved in Lemma 1.0b of Frobenius elements and determination by traces, put a root in \(F\) that generates \(F\) over \(\mathbb Q_p\). Its global field \(K_0\subset F\) has completion \(F\). In equal characteristic, Hensel lifts the roots of \(X^{q}-X\) to a coefficient field \(k_F\); successively removing the residue of each uniformizer coefficient proves \(F=k_F((\pi))\). Take \(K_0=k_F(t)\), embedded by \(t\mapsto\pi\).

Approximate the primitive separable polynomial of \(L/F\) by a polynomial over the dense field \(K_0\), sufficiently closely that every root is a perturbation in \(L\) of one of the original distinct roots, and each generates \(L\). The Newton and Krasner proofs just cited use only separability, a complete discrete valuation, and the unique valuation on a finite extension, so the identical inequalities apply in equal characteristic too. The normal closure \(M/K_0\) has completion exactly \(L\): all of its polynomial roots lie in \(L\), and any one generates \(L/F\). Let \(D\) be its decomposition group and replace \(K_0\) by \(K=M^D\). The finite completion/decomposition proof in Lemma 1.0a of that earlier lesson gives \(K_v=F\), \(\operatorname{Gal}(M/K)=D=\operatorname{Gal}(L/F)\), and a unique place of \(M\) above \(v\). This construction realizes all the intermediate fields and their local subgroup inclusions, not just an abstract copy of the group.

Second, given a finite set \(S\) of finite places disjoint from \(v\), there is a unitary Hecke character \(\alpha\) unramified at \(v\) and outside \(S\), with arbitrarily large conductors at every place of \(S\). We give the character extension detail, since it is needed here. Assign sufficiently ramified characters on the unit factors at \(S\), and the trivial character on all other finite unit factors. In a number field let \(U_f=\prod\mathcal O_w^\times\). Corollary 3.4 of NT-ADL-03 actually proves \(\mathcal O_K^\times=\mu_K\times\mathbb Z^{r_1+r_2-1}\) and that its logarithms are a full lattice in the sum-zero hyperplane. Choose an angular character at infinity whose restriction to \(\mu_K\) is the inverse of the assigned finite-unit character: a cyclic group of roots embeds in one complex circle, or is the real sign group. Choose real arguments for its required values on a free unit basis, and solve the linear equations on their independent logarithms. Multiplying the angular character by \(\exp(i\ell(\log|x_w|_w))\) for this real linear functional \(\ell\) makes the product character trivial on every global unit. It descends to
\((K_\infty^\times U_f)/\mathcal O_K^\times\), an open subgroup of finite index in \(C_K\), since the same Corollary 3.4 proves class-group finiteness. Extend across that finite quotient by choosing roots, one generator at a time. The extension is continuous because its original subgroup is open, and it is unitary because the roots can be chosen on the unit circle.

In a function field, choose the high-conductor unit characters trivial on the constant roots of unity; the prime-to-\(p\) residue factor splits from principal units by Hensel, so this imposes no restriction on large conductors. The image of \(U_f\) is open in \(C_K\), and its kernel is exactly the finite constant group: an element having neither zeros nor poles is a constant, by the compact-support/unit argument in NT-CFT-14 §2. Its character extends algebraically to \(C_K\), because adjoining any new cyclic generator only requires a root in \(S^1\); a maximal extension therefore has the whole group as domain. This extension is again continuous because the original subgroup is open. Thus the required unitary character exists in both characteristics.

The analytic inputs are rank-one global functional equations, already actually proved in NT-ADL-09, Theorem 9.2, and NT-ADL-10, Theorem 10.1 and equations (3), (5)–(8), for number fields; and NT-CFT-21 §6, equations (27)–(34), for function fields. The latter writes a finite-order character, but its proof extends verbatim to unitary characters: the convergence bound uses only absolute value one, the compact-fibre average uses only character orthogonality, and the correction is a geometric series in its value on a generator of the norm image. These are all the steps (28)–(32), so the same normalized equation follows for our unitary extension. For every intermediate global field, a finite Galois character becomes a Hecke character by composing it with \(c\mapsto\operatorname{rec}_{\mathrm{arith}}(c)^{-1}\), where the arithmetic map is proved in NT-CFT-16, Theorem 16.4, equation (13). Its actually written §6 proves comparison at every completion in both characteristics, so the local characters are precisely our geometric-reciprocity characters. The preceding Weil lesson, Proposition 6.1, also proves the number-field character correspondence; its number-field hypothesis is not needed for the finite-character argument just given. No higher-dimensional local epsilon constant occurs in these rank-one analytic inputs.

Now let \(r\in\ker b\). Globalize \(L/F\) as above, identify its finite group with \(\operatorname{Gal}(M/K)\), and let \(S\) be the finite ramified places other than \(v\). Choose the global \(\alpha\) so ramified at each \(w\in S\) that §3B applies to \(M_w/K_w\). Take a nontrivial global additive character trivial on \(K\), and its trace characters on the intermediate fields; use their local self-dual measures. Multiply the rank-one global functional equations for all the signed pairs in \(r\), twisted by \(\alpha\). Their L-products are identical to those of the zero representation: this follows place by place from Theorem 1.1, including the gamma identity at infinity, and from \(b(r)\otimes\alpha=0\). Their dual products are also one, by the same coset pairing and induction identity. Comparing the two nonzero meromorphic products therefore gives
\[
\prod_w C_{\alpha_w}(r_w)=1.
\tag{10I}
\]
Here \(r_w\) is the restriction of the formal relation to the local decomposition group. In detail, the cosets of each \(H\) break into orbits under that group; choosing orbit representatives identifies each orbit with the induction from its stabilizer and restricts the two character lines. Thus \(b(r_w)=\operatorname{Res}_{D_w} b(r)=0\). This is the required local decomposition of (10I), including places at which an intermediate field splits.

Every factor of (10I) other than the one at \(v\) is one. At \(S\), §3B supplies a theory and the relation criterion applies. At an unramified finite place all subextensions and finite characters are unramified. Normalize \(n=0\) and unit volume one: their constants are one by (9), so the criterion holds; §3A transports it to the actual additive character and any measure. The archimedean criterion holds by the explicit theory in §3D below. Consequently \(C_{\alpha_v}(r)=1\). The character \(\alpha_v\) is unramified; the invariance in §3A removes it and allows any prescribed local additive character. This proves (10D) for \(\alpha=1\), for every \(r\in\ker b\). Section 3A now constructs the finite-image local theory and proves its independence from every Brauer relation.

### 3D. Arbitrary smooth representations and infinity

The same criterion supplies a theory for every unramified \(\alpha\), by §3A. For a finite-image \(V_0\) and unramified \(\eta\), define its value on \(V_0\otimes\eta\) using that \(\eta\)-theory. This definition is independent of the finite quotient: compare the two constructions in a common finite quotient, where the relation criterion and (10) imply uniqueness. It is also independent of the finite-image/unramified presentation. If an irreducible has two such presentations, choose a power \(\Phi^N\) centralizing both finite images. Its scalar values in those images are roots of unity; hence the ratio of the two unramified characters has root-of-unity Frobenius value, so is a finite-order unramified character. Absorb that finite character in a common finite quotient. The two \(\eta\)-theories agree on its rank-one generators, and the criterion gives equality on the representation. Theorem 2.2 of the preceding Weil lesson supplies such a presentation for every irreducible. Define the value of a general smooth representation by the product over its composition factors; Jordan–Hölder is proved in Lemma 0A.2 of the first lesson.

Here is the induction check across different unramified types. Every unramified \(\eta_E\) extends to an unramified \(\eta_F\), by choosing an \(f(E/F)\)-th root of its Frobenius value. For a finite-image \(U_0\), the \(\eta_F\)-theory gives full induction with the correction
\[
\lambda_{\eta_F}(E/F)=
\frac{\epsilon_F((\operatorname{Ind}1)\otimes\eta_F)}
{\epsilon_E(\eta_F|_{W_E})}.
\tag{10J}
\]
The quotient is independent of \(\eta_F\). To check this without anticipating Theorem 4.1 here, character formula (7), (10), and the preceding conductor induction theorem give the unramified-twist exponent for every finite-image representation by its rank-zero induced-character expression. The exponent in (10J) is zero: with \(N=[E:F]=ef\),
\[
a_F(\operatorname{Ind}1)+Nn_F-f n_E
=fd+ef n_F-f(en_F+d)=0.
\]
The same formula covers all unramified twists, since their values on a uniformizer can be any nonzero complex number. Thus full induction for a constituent has correction \(\lambda(E/F)^{\dim U_0}\), independent of its type. Exactness of finite-index induction and multiplication over composition factors prove the same identity for every \(U\). In virtual dimension zero these corrections cancel. This proves property 3 in its full original smooth generality; it does not restrict it to finite image or Frobenius semisimplicity.

Finally, at infinity take the positive trace characters and self-dual measures of §2. Set the character constants equal to their proved Tate phases, and on an irreducible real induction set
\[
\epsilon_{\mathbb R}(\operatorname{Ind}\omega_{a,n})=i^{|n|+1}\quad(n\ne0).
\tag{10K}
\]
For \(n=0\) the induction splits into the two real characters of opposite parity, whose product is \(i\), the same formula. The classification in the preceding lesson identifies the inducing characters only by \(n\leftrightarrow-n\), so (10K) is well defined. The ratio of a real induced character constant to its complex constant is always \(i\); hence it cancels for any virtual dimension-zero induction. Products over composition factors prove multiplicativity and every archimedean induction relation. For arbitrary measures multiply by their scalar to the power of dimension. For an additive change \(\psi_a\), multiply by \(\det V(a)|a|^{-\dim V}\). The character substitution in §2 and the rank-zero determinant/transfer identity show that these changes preserve induction; all nontrivial real or complex unitary additive characters are such changes of the chosen trace characters. This proves all four properties at infinity. Together with §§3A–3C and the smooth extension above, it completes the proof of Theorem 3.0. \(\square\)

**Lemma 3.1 (the smooth version).** The Grothendieck group of smooth representations of \(W_F\) is generated by the trivial character and induced virtual differences of two one-dimensional quasi-characters of finite-index Weil subgroups.

**Proof.** It is enough to consider an irreducible \(V\). Write \(V=V_0\otimes\eta\), where \(\eta\) is unramified and \(V_0\) has finite image, using Theorem 2.2 of *Representations of Weil groups*. Apply (10) to \([V_0]-d[1]\), \(d=\dim V\), in a finite Galois quotient through which \(V_0\) factors. The subgroups correspond to finite extensions \(E_j/F\), and their inverse images are \(W_{E_j}\). Twisting and commuting the twist with induction gives
\[
[V]-d[\eta]=\sum_j m_j
\operatorname{Ind}_{W_{E_j}}^{W_F}
\bigl([\chi_j\eta|_{W_{E_j}}]-[\eta|_{W_{E_j}}]\bigr).
\tag{11}
\]
Each difference on the right has dimension zero. The remaining \(d[\eta]\) is a one-dimensional term, or \(d[1]+d([\eta]-[1])\) if a uniform list of generators is wanted. A composition series and additivity handle arbitrary \(V\). \(\square\)

**Theorem 3.2 (uniqueness).** At most one family of local constants satisfies the four properties above.

**Proof.** Suppose two families exist. Their ratio \(R_F(V,\psi,dx)\) is multiplicative on virtual representations, equals one on one-dimensional representations, and is independent of measure in dimension zero. Property 3 identifies its value on an induced rank-zero difference with its value on that difference over the extension. Both of its one-dimensional terms have ratio one, so the induced difference does too. Lemma 3.1 now makes the ratio one on every smooth nonarchimedean Weil representation. Over \(\mathbb C\) all irreducibles are characters; over \(\mathbb R\), the classification gives characters and inductions from \(\mathbb C\). For an induced character, subtract an induced trivial character to apply degree-zero induction. The latter is the sum of the trivial and sign real characters, already known. This proves uniqueness at infinity as well. \(\square\)

The proof explains the correction needed after an unramified twist: the terms in (11) are differences of quasi-characters, not necessarily \(\chi_j-1\) with finite-order \(\chi_j\).

## 4. Exponents, measures and additive characters

For nonarchimedean \(F\), define \(\epsilon_F(s,V,\psi,dx)=\epsilon_F(V\otimes\omega_s,\psi,dx)\).

**Theorem 4.1 (the exponent).** With \(d=\dim V\),
\[
\epsilon_F(s,V,\psi,dx)
=\epsilon_F(0,V,\psi,dx)
q_F^{-(a_F(V)+d n_F(\psi))s}.
\tag{12}
\]

**Proof.** Form the quotient of the left side by the right side. It is multiplicative in \(V\), since conductors and dimensions add, and it equals one on characters by (7). For a virtual \(U\) of dimension zero over \(E\), degree-zero induction applies to both numerator constants. Since \(\omega_{F,s}|_{W_E}=\omega_{E,s}\), it identifies their ratio with the corresponding ratio over \(E\). The induction conductor formula of the preceding lesson gives
\(a_F(\operatorname{Ind}U)=f(E/F)a_E(U)\); the discriminant term vanishes in virtual dimension zero. Since \(q_E=q_F^f\), the exponential terms agree too. Thus the quotient is one on all induced differences in Lemma 3.1, and on the remaining character term. This proves (12). \(\square\)

The measure-scaling property is already one of the axioms. Additive-character scaling is
\[
\epsilon_F(V,\psi_a,dx)=
\det V(\operatorname{Art}_F(a))\,|a|_F^{-d}
\epsilon_F(V,\psi,dx).
\tag{13}
\]
Here and below \(\det V(a)\) abbreviates evaluation after \(\operatorname{Art}_F\).

**Proof of (13).** Take the ratio of its two sides. It equals one for characters by (7) and is multiplicative. For a dimension-zero representation induced from \(E\), property 3 transports \(\psi_a\) to \((\psi\circ\operatorname{Tr})_a\). The determinant formula for induction gives \(\det(\operatorname{Ind}U)(a)=\det U(a)\), since the permutation determinant is raised to virtual dimension zero and transfer corresponds to \(F^\times\subset E^\times\). The absolute-value powers also vanish in dimension zero. The ratio is therefore compatible with degree-zero induction, and Lemma 3.1 makes it one for every representation. The same argument with the real classification applies at infinity. \(\square\)

Self-dual measures satisfy \(dx_{\psi_a}=|a|_F^{1/2}dx_\psi\), by a change of variable in Fourier inversion. Combining this with (13) gives the familiar normalized version
\[
\epsilon_F(s,V,\psi_a,dx_{\psi_a})
=\det V(a)|a|_F^{(s-1/2)d}
\epsilon_F(s,V,\psi,dx_\psi).
\tag{14}
\]
Equations (13) and (14) use different measure conventions. In particular the absolute-value factor in (13) must not be copied into a formula that silently changes to a self-dual measure.

## 5. Duality and unitary normalization

**Theorem 5.1.** With \(dx'\) dual to \(dx\),
\[
\epsilon_F(V,\psi,dx)
\epsilon_F(V^\vee\otimes\omega_1,\psi_{-1},dx')=1.
\tag{15}
\]
Equivalently, using the same additive character in both factors,
\[
\epsilon_F(V,\psi,dx)
\epsilon_F(V^\vee\otimes\omega_1,\psi,dx')=\det V(-1).
\tag{16}
\]

**Proof.** The product in (15) is multiplicative in \(V\) and equals one on characters by Fourier inversion, (8). Duality commutes with finite-index induction, as follows either from the perfect pairing of the coset tensor spaces or from the function model. The norm character restricts as \(\omega_{F,1}|_{W_E}=\omega_{E,1}\). Thus on a dimension-zero induced difference the two epsilon constants are those of the difference and its dual over \(E\), with additive characters \(\psi\circ\operatorname{Tr}\) and its negative. Measures can be omitted in that virtual dimension, so their choices do not interfere with the induction argument. Lemma 3.1 proves (15) nonarchimedeanly. The real induced-character subtraction used in Theorem 3.2 gives the archimedean case.

Apply (13) with \(a=-1\) to the second constant. Its scaling factor is
\(\det(V^\vee\otimes\omega_1)(-1)=\det V(-1)^{-1}\), since \(|-1|=1\). Rearranging (15) gives (16). \(\square\)

For a unitary \(V\) put
\[
W_F(V,\psi)=\epsilon_F(1/2,V,\psi,dx_\psi).
\tag{17}
\]
It has absolute value one. Here is the conjugation input that makes the assertion rigorous. Character constants satisfy
\(\overline{\epsilon(\chi,\psi,dx)}=\epsilon(\bar\chi,\psi_{-1},dx)\), as follows by conjugating the character integrals; the statement for all representations follows from the uniqueness argument and the same four axioms. A unitary representation has \(\bar V\simeq V^\vee\). Apply (15) to \(V\otimes\omega_{1/2}\) with a self-dual measure. Its second representation is \(V^\vee\otimes\omega_{1/2}\), and its second constant is the complex conjugate of the first. Hence their product is \(|W_F(V,\psi)|^2=1\). Self-duality of the representation alone, without this conjugation and measure information, would not justify the absolute-value assertion.

## 6. The induction constant

For fixed measures \(dx_F,dx_E\), set \(\psi_E=\psi\circ\operatorname{Tr}_{E/F}\) and
\[
\lambda(E/F,\psi;dx_F,dx_E)=
\frac{\epsilon_F(\operatorname{Ind}1,\psi,dx_F)}
{\epsilon_E(1,\psi_E,dx_E)}.
\tag{18}
\]
Subtracting \(d[1]\) from \(V\) in degree-zero induction gives
\[
\epsilon_F(\operatorname{Ind}V,\psi,dx_F)
=\lambda(E/F,\psi;dx_F,dx_E)^d
\epsilon_E(V,\psi_E,dx_E).
\tag{19}
\]
This follows by multiplying the equality for \(V-d[1]\) by the \(d\) trivial-character factors on both sides. When both measures are self-dual we abbreviate the constant to \(\lambda(E/F,\psi)\).

**Example 6.1 (unramified quadratic extension).** If \(E/F\) is unramified quadratic, \(\operatorname{Ind}1=1\oplus\omega_{E/F}\), where \(\omega(\varpi_F)=-1\). The different is trivial, so \(n_E(\psi_E)=n_F(\psi)=n\). For a self-dual measure, \(\operatorname{vol}(\mathcal O_F)=q_F^{-n/2}\): the annihilator of \(\mathcal O_F\) is \(\mathfrak p_F^{-n}\), and the product of their volumes is one. Formula (9) then gives
\[
\epsilon_F(1)=q_F^{n/2},\qquad
\epsilon_F(\omega)=(-1)^nq_F^{n/2},\qquad
\epsilon_E(1)=q_E^{n/2}=q_F^n.
\]
Their quotient is
\[
\lambda(E/F,\psi)=(-1)^n.
\tag{20}
\]
This computation keeps the measure and additive-character exponents until they cancel.

## 7. Sharp twisting and orthogonal root numbers

These results require additional ramification and real-representation arguments; they do not follow from the four axioms alone. We prove the sharp twisting identity below, with its endpoint ambiguity made explicit, and then prove the orthogonal root formula by real induction and a two-dimensional Fourier calculation.

For a virtual Weil representation \(A\), its constituents mean the irreducibles with nonzero signed multiplicity. Let \(\alpha(A)\) and \(\beta(A)\) be respectively their smallest and largest upper breaks, assigning break zero to an unramified or tame constituent. For \(t\ge0\), write \(U_F(t)=\{u\in\mathcal O_F^\times:v_F(u-1)>t\}\).

**Theorem 7.1 (Deligne–Henniart twisting identity).** Suppose \(B\) has no tame constituent, so \(\alpha(B)>0\). There is an element \(\gamma(B,\psi)\in F^\times\) such that, for every virtual \(A\) of dimension zero with \(\beta(A)<\alpha(B)/2\),
\[
\epsilon_F(A\otimes B,\psi)=\det A(\gamma(B,\psi)).
\tag{21}
\]
It has valuation \(a_F(B)+\dim(B)n_F(\psi)\). Put \(h=\alpha(B)/2\) and \(T_F(h)=1+\mathfrak p_F^{\lceil h\rceil}\). The identities characterize its class modulo \(T_F(h)\); any lift of this class to \(F^\times/U_F(h)\) gives the originally displayed identity. When \(h\) is not an integer these two unit groups agree. When \(h\) is an integer, the strict break inequality determines only the coarser quotient. The freely accessible Deligne–Henniart text, Theorem 4.6 and Lemma 4.7, supplies the sharp identity; its printed uniqueness wording must be read with this endpoint distinction.

**Lemma 7.2 (Herbrand slopes and bounded induction).** For a finite separable \(E/F\), let \(\Psi_{E/F}\) be its upper-parameter change. It is convex, starts at zero, and has slope \(e(E/F)\) beyond the last break \(b_{E/F}\) of its permutation representation. It satisfies
\[
G_E^{\Psi_{E/F}(u)}=G_F^u\cap G_E,
\qquad
\Psi_{E/F}(u)=e(u+1)-d_{E/F}-1\quad(u>b_{E/F}).
\tag{21A}
\]
If a virtual dimension-zero \(A\) has largest break \(b<h\), it has a decomposition into \(\operatorname{Ind}_{W_E}^{W_F}(\eta-1)\) with \(b_{E/F}<h\) and \(\beta(\eta)<\Psi_{E/F}(h)\). If an irreducible \(B\) has break \(t>0\), it has an integer decomposition into \(\operatorname{Ind}_{W_E}^{W_F}\chi\), where
\[
b_{E/F}<t,\qquad \beta(\chi)=\Psi_{E/F}(t).
\tag{21B}
\]

**Proof.** In a finite normal closure \(N/F\), put \(G=\operatorname{Gal}(N/F)\), \(H=\operatorname{Gal}(N/E)\), and
\(\Psi_{E/F}=\varphi_{N/E}\circ\psi_{N/F}\). The subgroup identity \(H_j=H\cap G_j\) and the upper quotient theorem in the preceding lesson, Lemma 1.6, prove independence of the normal closure and the first equality in (21A). Its slope is
\(e/[G^u:H\cap G^u]\).
The denominator decreases as \(u\) increases: since \(G^u\) is normal, it is the index of \(H\) in \(HG^u\). Thus the slopes increase and do not exceed \(e\). They equal \(e\) precisely after the permutation representation has become trivial on the upper group. The tail intercept follows without an additional norm theorem: characters of arbitrarily large conductor \(m\) were constructed in §3B, where their norm pullbacks have conductor \(em-d\). Above the permutation break the first equality in (21A) preserves their last nontrivial group, so \(\Psi(m-1)=em-d-1\). The slope is already \(e\), giving the displayed affine formula.

For \(A\), choose any \(u\) with \(b<u<h\) and apply (10) in a finite quotient killed by \(G_F^u\); handle unramified twists as in Lemma 3.1. Expand each twisted difference \(\chi\eta_E-\eta_E\) as \((\chi\eta_E-1)-(\eta_E-1)\), and include the residual unramified differences over \(F\). Thus the terms really have the asserted form even when constituents have different unramified twists. Its inducing subgroups contain that upper group and its character lines are trivial on it. Hence the permutation break is less than \(u\), and the character breaks are less than \(\Psi(u)<\Psi(h)\). This proves the first decomposition.

For the second, remove an unramified twist from \(B\) and take its faithful finite quotient. Its last nontrivial upper group \(D=G^t\) is abelian. Here is the commutator detail. If \(\sigma\in G_i\), \(i\ge1\), expansion in a uniformizer with coefficients in the maximal unramified ring shows
\(v((\sigma-1)x)\ge v(x)+i\) for integral \(x\) of positive value; subtract powers by telescoping and pass to convergent series. The coefficients are fixed by inertia. Consequently \((\sigma-1)(\tau-1)-(\tau-1)(\sigma-1)\) raises value by at least \(i+j\) for \(\tau\in G_j\). Multiplying by the inverse of \(\tau\sigma\) gives \([G_i,G_j]\subseteq G_{i+j}\). The last positive lower group is therefore abelian.

We prove the required refinement of ordinary Brauer induction. If a normal abelian subgroup \(D\) is central, project an ordinary Brauer expression onto a fixed \(D\)-character \(\theta\). For a term induced from \(H\), induction in stages through \(HD\) shows that its \(\theta\)-part is zero unless its line agrees with \(\theta\) on \(H\cap D\); when they agree it is induced from the unique line on \(HD\) extending both. Uniqueness and existence follow by writing an element as \(hd\) and checking the intersection relation. Thus the inducing subgroups may contain \(D\), and the lines restrict to \(\theta\). For normal abelian \(D\), split into its weight orbits. The stabilizer of a weight \(\theta\) acts on that weight space, and \(D/\ker\theta\) is central in its quotient by \(\ker\theta\). The preceding central argument applies there; induction in stages returns to \(G\). The orbit/weight-space isomorphism is explicit: the sum of the translates of a weight space identifies with its induced coset space. If \(B^D=0\), every occurring weight is nontrivial, so every resulting line is nontrivial on \(D\). In our case the single-break proof in the preceding lesson gives \(B^D=0\). The inducing subgroup contains \(G^t\), so its permutation break is less than \(t\); its line is nontrivial on that group and trivial on every later one, giving (21B). Restore the unramified twist, which changes no break. \(\square\)

**Lemma 7.3 (the parameter under a norm).** Let \(\chi\) be a wild character of break \(t=c-1>0\). With \(E_p(z)=\sum_{j=0}^{p-1}z^j/j!\), choose \(a\) by
\(\chi(E_p(z))=\psi(az)\) for \(v_F(z)>t/p\).
Its value is \(v_F(a)=-c-n_F\). If \(b_{E/F}<t/2\), and \(a_E\) is the corresponding parameter for \(\chi\circ N_{E/F}\) and \(\psi\operatorname{Tr}\), then every character \(\eta\) with \(\beta(\eta)<\Psi_{E/F}(t/2)\) satisfies \(\eta(a_E)=\eta(a)\).

**Proof.** In the polynomial identity
\(\prod_j E_p(z_j)-E_p(\sum_jz_j)\), every term has total degree at least \(p\): coefficients in lower degrees agree by the multinomial formula and are integral because the factorials below \(p\) are units. Thus \(\chi(E_p(z))\) is additive on the ideal \(v(z)>t/p\). The map \(z\mapsto E_p(z)-1=z+O(z^2)\) bijects that ideal with itself, by unit-derivative Hensel lifting and the least-value calculation for the difference of two arguments. Nondegeneracy of the finite additive pairing in (9B) supplies \(a\), and nontriviality of the last conductor layer forces its value. The same argument works over \(E\), where the character break is \(t_E=\Psi(t)\), by (21A) and \(t>b_{E/F}\).

Norm expansion of the polynomial identity gives
\[
N_{E/F}(E_p(z))=E_p(\operatorname{Tr}z)+R,
\qquad v_F(R)\ge p\,v_E(z)/e.
\tag{21C}
\]
Take \(r=\lfloor et/p\rfloor+1\). For \(z\in\mathfrak p_E^r\) the error is killed by \(\chi\), since its value is greater than \(t\). The trace has value greater than \(t/p\). Indeed \(d_{E/F}\ge e-1\): an Eisenstein uniformizer polynomial over the maximal unramified field has derivative value at least \(e-1\), by Lemmas 1.1 and 1.3 of the preceding lesson, and the unramified different is trivial. Lemma 2.2 therefore gives \(v_F(\operatorname{Tr}z)\ge\lceil r/e\rceil>t/p\). Also \(r>t_E/p\), since convexity and the slope bound give \(\Psi(t)\le et\). Hence
\(\psi\operatorname{Tr}((a_E-a)z)=1\) on \(\mathfrak p_E^r\).
Its annihilator gives
\[
v_E((a_E-a)/a_E)\ge t_E+1-r
=\Psi(t)-\lfloor et/p\rfloor.
\tag{21D}
\]
The affine tail in (21A), applied beyond \(b_{E/F}<t/2\), identifies
\(\Psi(t)-et/p=\Psi((1-1/p)t)\ge\Psi(t/2)\).
Thus the relative difference has value strictly greater than \(\beta(\eta)\). By the unit/upper character correspondence actually proved in the preceding lesson, Lemma 2.4, \(\eta\) is trivial on that difference. This proves the claimed equality. \(\square\)

**Proof of Theorem 7.1.** First take \(B=\chi\), of break \(t\). The polynomial parameter in Lemma 7.3 also satisfies \(\chi(1+z)=\psi(az)\) for \(v(z)>t/2\): the quotient of \(E_p(z)\) by \(1+z\) differs from one in value at least \(2v(z)>t\), and is killed by \(\chi\). Lemma 3.0a therefore gives
\(\epsilon((\eta-1)\chi)=\eta(a)^{-1}\) whenever \(\beta(\eta)<t/2\).

For an arbitrary dimension-zero \(A\) with that break bound, use its decomposition from Lemma 7.2. On a term \(\operatorname{Ind}(\eta-1)\), the projection formula and rank-zero induction reduce the epsilon constant to \(\epsilon((\eta-1)(\chi\circ N),\psi\operatorname{Tr})\). Convexity gives
\(\beta(\eta)<\Psi(t/2)\le\Psi(t)/2\),
so the character calculation applies over \(E\) and gives \(\eta(a_E)^{-1}\). Lemma 7.3 replaces this by \(\eta(a)^{-1}\), and determinant transfer identifies it with \(\det\operatorname{Ind}(\eta-1)(a^{-1})\). Multiplication over the decomposition proves (21) with \(\gamma=a^{-1}\) for a character \(B\).

For irreducible \(B\) of break \(t\), use (21B), writing \(B=\sum_i n_i\operatorname{Ind}\chi_i\). The restriction of \(A\) to each inducing field has largest break at most \(\Psi_i(\beta(A))\), by (21A), hence less than \(\Psi_i(t/2)\le\Psi_i(t)/2\). Its dimension is still zero. Projection and rank-zero induction, followed by the character case, give (21) with
\[
\gamma=\prod_i N_{E_i/F}(a_i^{-1})^{n_i}.
\tag{21E}
\]
Restriction of a determinant corresponds to the norm, by the reciprocity diagram in the preceding Weil lesson. For virtual \(B\), multiply these elements over its signed constituents. Every constituent break is at least \(\alpha(B)\), so the same strict bound on \(A\) works for all of them. Negative multiplicities simply invert the constants and the elements.

Each factor of (21E) has value \(f_i(c_i+n_{E_i})\). Equations (9D) and the preceding conductor induction theorem identify this with
\(a_F(\operatorname{Ind}\chi_i)+[E_i:F]n_F\).
Adding signed terms proves the asserted valuation. Finally the determinant of every allowed \(A\) has break at most \(\beta(A)<h\), hence character conductor at most \(\lceil h\rceil\), by the same unit/upper correspondence. Its value is therefore unchanged on \(T_F(h)\). Conversely all unit characters of conductor at most \(\lceil h\rceil\), and all unramified characters, occur as \(A=\eta-1\). Finite abelian character duality separates \(F^\times/T_F(h)\), so these identities determine exactly that quotient. This proves both existence and the stated ambiguity. \(\square\)

The endpoint distinction is substantive. Over \(\mathbb Q_2\), take the conductor-three character with values \(1,-1,-1,1\) on the odd residue classes \(1,3,5,7\pmod8\). Its break is two. Every allowed determinant for \(\beta(A)<1\) is unramified, since the residue unit group is trivial and a character of positive break has integral break at least one. Thus \(\gamma\) and \(3\gamma\) give identical identities, although \(3\notin U_F(1)=1+4\mathbb Z_2\). For the standard conductor-zero additive character, both \(a=1/8\) and \(a=3/8\) satisfy \(\chi(1+y)=\psi(ay)\) for \(v(y)>1\). Claiming that this condition uniquely determines a class modulo \(U_F(1)\) would therefore be false.

In particular take a wildly ramified character \(\chi\) of conductor \(c\), so its break is \(c-1>0\). If the largest break \(b\) of an actual \(V\), with zero allowed for tame constituents, satisfies \(2b<c-1\), apply (21) to \(A=V-d[1]\), \(B=\chi\). It gives
\[
\epsilon_F(V\otimes\chi,\psi,dx)
=\epsilon_F(\chi,\psi,dx)^d\det V(\gamma(\chi,\psi)).
\tag{22}
\]
For the explicit sign, the character calculation in the proof chooses \(a\in F^\times\) by
\[
\chi\!\left(\sum_{j=0}^{p-1}\frac{y^j}{j!}\right)=\psi(ay)
\quad\text{when }v_F(y)>(c-1)/2,
\qquad\gamma(\chi,\psi)=a^{-1}.
\tag{23}
\]
Here \(p\) is the residue characteristic, and the polynomial is the truncated exponential; its denominators are units. One may choose the stronger parameter from Lemma 7.3. The determinant in (22) is trivial even on the full endpoint ambiguity \(T_F((c-1)/2)\), by the break hypothesis. Thus the factor is \(\det V(a)^{-1}\), with this definition of \(a\) and our geometric reciprocity. Formula (23) fixes the sign; it does not assert the incorrect endpoint uniqueness just discussed.

**Theorem 7.4 (Deligne's orthogonal formula).** Let \(A\) be a virtual finite-image real representation of \(G_F\) with virtual dimension zero and determinant one. Its second Stiefel–Whitney class gives a class \(w_2(A)\in H^2(G_F,\mathbb Z/2)\). Inflate from its finite quotient, map \(1\in\mathbb Z/2\) to \(-1\in\bar F^\times\), and take the local Brauer invariant \(\operatorname{inv}_F\in\mathbb Q/\mathbb Z\). Then
\[
\epsilon_F(1/2,A,\psi,dx)
=\exp\!\left(2\pi i\operatorname{inv}_F(w_2(A))\right).
\tag{24}
\]
The left side is independent of \(\psi\) and \(dx\) by its dimension and determinant hypotheses. In characteristic different from two its values are \(1\) or \(-1\); in characteristic two the coefficient map to \(\bar F^\times\) is trivial and the value is one. For an actual orthogonal representation with nontrivial determinant, first remove that determinant and the excess rank, or keep its one-dimensional root factor. Omitting either qualification changes the assertion.

The Brauer invariant and its corestriction law are the actually proved earlier NT-CFT-24, Theorem 24.2, including both characteristics and the infinite places. We prove the required real induction and degree-two class identities next. This avoids importing a real induction theorem solely from a citation in the free Deligne paper.

**Lemma 7.5 (odd real induction).** For any finite group \(G\), an odd integer \(q\) times \(1_G\) is a sum of inductions of real virtual representations of groups having a nilpotent subgroup of index at most two.

**Proof.** Write \(R_{\mathbb R}(G)\) for the real representation ring, and let \(I\) be the subgroup generated by the indicated inductions. It is an ideal, by the coset projection formula. We prove that \(R_{\mathbb R}(G)/I=2(R_{\mathbb R}(G)/I)\). The same determinant argument as in the earlier integer Brauer proof will then give an odd annihilator.

Use the cyclotomic local ring \(D=\mathbb Z[\zeta]_{\mathfrak m}\) at a maximal ideal above two, as in RT-FIN-11 §3, with residue field \(k\). Complexifying real representations gives an injective character map, also after tensoring with \(D\): Proposition 3.2 of the actually written RT-FIN-04 gives the distinct complexifications, namely an orthogonal irreducible, a conjugate pair, or twice a quaternionic irreducible. Their disjoint character supports are linearly independent. Thus \(D\otimes R_{\mathbb R}(G)\) is a subring of \(D^c\), with diagonal constants, where \(c\) is the number of conjugacy classes. The proof of RT-FIN-11, Lemma 3.1, applies unchanged: \(D^c\) is a finite faithful module; the adjugate contradiction excludes a maximal ideal generating the whole module; a maximal ideal of \(D^c\) selects one coordinate and reduces it to \(k\). Consequently every maximal ideal is a reduced evaluation. Its value on \(g\) equals that on the odd-order part \(a\) of \(g\), since every two-power eigenvalue reduces to one. This eigenvalue argument is Lemma 3.2 there and applies to real complexifications as well.

We must detect every such evaluation by a real induction. For \(a=1\), induction of the trivial line from a Sylow two-subgroup has odd dimension, so detects it. For \(a\ne1\), put \(C=\langle a\rangle\), of odd order \(d\), and
\(N^\pm=\{g:gag^{-1}\in\{a,a^{-1}\}\}\).
Choose a Sylow two-subgroup \(P\) of \(N^\pm\), and set \(H=CP\). It acts on \(C\) by identity or inversion. The kernel \(P_0\) of that action gives the nilpotent subgroup \(C\times P_0\) of index at most two. The quotient by \(P_0\) is cyclic or dihedral. Its real plane characters restrict to \(C\) as \(\zeta_d^{j}\!+\zeta_d^{-j}\); use their inflations to \(H\).

Here is the evaluation calculation, including the possible cancellation at two. Write \(S=\{s\pmod d:a^s\text{ is conjugate to }a\}\). If inversion occurs in \(N^\pm\), then \(S=-S\) and \(|C_G(a)|/(d|P|)\) is an odd integer divided by two. The induction formula for the real plane of exponent \(j\) is therefore an odd integer times \(\sum_{s\in S}\zeta_d^{js}\), because its two character terms give twice that sum. If inversion does not occur, \(S\) and \(-S\) are disjoint, the coefficient \(|C_G(a)|/(d|P|)\) is odd, and the evaluation is that odd integer times \(\sum_{s\in S\cup(-S)}\zeta_d^{js}\). In both cases the coefficient vector on this cyclic group is nonzero modulo two. The cyclic Fourier matrix is invertible over \(k\): \(d\) is odd and its roots remain distinct. Hence some \(j\) gives a nonzero reduced evaluation. The inductions in \(I\) therefore escape every maximal ideal, proving \(D\otimes I=D\otimes R_{\mathbb R}(G)\).

For \(M=R_{\mathbb R}(G)/I\), reduction to \(k\) gives \(k\otimes_{\mathbb F_2}(M/2M)=0\), hence \(M=2M\). Choose finitely many abelian-group generators \(m_i\) and write \(m_i=2\sum_j a_{ij}m_j\), with integers \(a_{ij}\). The adjugate of \(I-2(a_{ij})\) shows that the odd integer \(q=\det(I-2(a_{ij}))\) annihilates \(M\). In particular \(q1_G\in I\). This is the claimed induction statement. \(\square\)

**Lemma 7.6 (real generators in the required subgroup).** If \(G\) has a normal nilpotent subgroup \(G'\) of index at most two, every real virtual representation of dimension zero and determinant one is a sum of realifications of complex virtual representations of dimension zero and inductions of
\[
r(\chi)=\operatorname{Ind}_{C}^{D}(\chi-1)
\tag{24A}
\]
from dihedral quotients \(D=C\rtimes\{1,s\}\), where \(s\) inverts the cyclic group \(C\).

**Proof.** First prove, by induction on \(|G|\), that an arbitrary real representation is a sum of realifications, inductions of (24A), and real lines. An irreducible whose complexification is reducible is already a realification, by RT-FIN-04, Proposition 3.2, whose conjugate-linear proof explicitly includes quaternionic irreducibles. A nonfaithful irreducible reduces to its smaller quotient. A representation induced from a proper real subgroup reduces to that subgroup; induction commutes with realification and with induction of (24A). Induced real lines require the following separate index argument.

For a line \(\epsilon\) on \(H\), put \(H'=H\cap G'\). If \([G:H]\le2\), its real dimension is at most two. Every real orthogonal plane has a cyclic rotation subgroup and, if orientation is reversed, a dihedral image; it is thus a realification or a sum of (24A), the trivial line and the determinant line. For a larger index, the ascending central series of \(G'\) supplies \(J\) such that \(H'J/H'\) is nontrivial abelian and normalized by \(H\): take the first central-series term not contained in \(H'\). In its prime-torsion part choose a line stable under \(H/H'\), whose order is at most two. In odd characteristic an involution has its two eigenspaces; in characteristic two it has a nonzero fixed vector. Let \(I'\) be its inverse image and \(I=I'H\). Then \(I'/H'\) has prime order \(\ell\), \(H'\triangleleft I'\), and induction in stages reduces the line step to \(\operatorname{Ind}_H^I\epsilon\).

If \(\ell=2\), this is a real plane. If \(\ell\) is odd, \(I'\) normalizes \(\epsilon|_{H'}\). To check this, finite nilpotent groups have commuting Sylow factors. An elementary proof is useful here: every proper subgroup has a larger normalizer, by the first ascending central-series term outside it; if the normalizer of a Sylow subgroup were proper, its own larger normalizer would preserve its unique normal Sylow subgroup and contradict that definition. Thus all Sylow subgroups are normal and distinct ones commute. The odd quotient \(I'/H'\) consequently cannot act nontrivially on a sign character, which depends only on the two-primary factor. It follows that \(I'/\ker\epsilon\) is cyclic of order \(\ell\) or \(2\ell\). Restriction of \(\operatorname{Ind}_H^I\epsilon\) to \(I'\) is the sum of its distinct character extensions. The outside involution acts on this cyclic quotient by identity or inversion. Pairing conjugate characters decomposes the representation into real summands of dimension at most two, already handled. The remaining induced real lines in \(G\) have index \([G:I]<[G:H]\), completing the index induction.

It remains to treat a faithful absolutely irreducible real representation not induced from a proper real subgroup. Choose a maximal abelian subgroup \(B\triangleleft G\) contained in \(G'\). Its character weights occur in conjugate pairs; the stabilizer of one pair would induce the representation from a real weight-pair space if proper. Hence that stabilizer is \(G\). Let \(G''\) stabilize one of the two weights. Faithfulness makes that weight faithful on \(B\), so \(B\) is central in \(G''\). Put \(T=G'\cap G''\). If \(B<T\), the centre of \(T/B\) has a prime-torsion subspace stable under \(G/T\), an elementary two-group of rank at most two. It has a stable line: odd-characteristic commuting involutions diagonalize together, and a two-group in characteristic two has a fixed vector, by induction on a central involution. The inverse image \(B'\) of that line is abelian because \(B\) is central in \(T\), and is normal in \(G\), contradicting maximality. Thus \(B=T\). Now \(G''/B\) has order at most two and \(B\) is central, so \(G''\) is abelian. Its index in \(G\) is at most two. The weight-space argument bounds the irreducible dimension by two, a case already treated. This completes the order induction.

For a virtual rank-zero determinant-one representation, subtract the ranks from the realification terms; these remain realifications of complex rank-zero terms. Terms (24A) already have rank zero and determinant one. What remains is a signed sum of real lines of rank zero and product character one. Repeated use of
\(\alpha\beta-1=(\alpha-1)+(\beta-1)+(\alpha-1)(\beta-1)\)
expresses it as a sum of \((\alpha-1)(\beta-1)\), with sign characters \(\alpha,\beta\). If they agree the term is \(-2(\alpha-1)\), a realification. If they are distinct and nontrivial, pass to their Klein-four quotient, viewed as a dihedral group: its term \(r(\beta|_{\ker\alpha})\) equals \(\alpha\beta+\beta-\alpha-1\), and subtracting \(2(\beta-1)\) gives the desired product. Thus it is a dihedral term plus a realification. Trivial characters give zero. This proves the lemma. \(\square\)

**Lemma 7.7 (the degree-two class calculations).** For real virtual \(V\), put \(w_1(V)=\det V\), viewed as a \(\mathbb Z/2\)-character. The degree-two class satisfies
\[
w_2(V+U)=w_2(V)+w_2(U)+w_1(V)\smile w_1(U).
\tag{24B}
\]
For virtual dimension zero and determinant one,
\[
w_2(\operatorname{Ind}_H^G V)=\operatorname{Cor}_H^G w_2(V).
\tag{24C}
\]
For a complex virtual \(U\), the class of its realification is the obstruction to taking a square root of its determinant character. For a dihedral plane, the class of (24A) is the obstruction to lifting its rotation character through the double rotation cover, with a reflection lift of order two.

**Proof.** These degree-two assertions can be proved directly by central-extension cocycles. Form the Euclidean Clifford algebra with generators \(e_i^2=1\) and \(e_ie_j=-e_je_i\) for \(i\ne j\). Ordered monomials are a basis: they span by these relations and are independent in the creation-plus-contraction action on the exterior algebra. Products of unit vectors map to orthogonal products of reflections by twisted conjugation. Reflections generate the orthogonal group: a reflection carries one unit vector to another, after which induction applies to their perpendicular space. The kernel of this map is \(\{1,-1\}\), as is seen by commuting an ordered-monomial expansion with every vector and using the norm-one condition. Its even part is the spin double cover of the special orthogonal group. Choose lifts of the matrices of a finite representation; their multiplication errors are a \(\{1,-1\}\)-valued two-cocycle. This is \(w_2\). A real line has zero such cocycle, since its reflection lift has square one. In an orthogonal sum, lifts from the two summands commute with sign \((-1)^{\text{parity product}}\); parity is the determinant character. Multiplying their lifts therefore gives (24B), and inversion extends the identity to virtual representations. This construction is also the usual second Stiefel–Whitney class: for an oriented representation it is exactly the pullback of the spin cover, and the line and sum formulas give its degree-two extension.

For (24C), first take an oriented actual representation of dimension \(n\) divisible by four. The induced matrices are a permutation of the coset blocks followed by the original block matrices. Their spin lifts multiply the block cocycles over the cosets, the cochain definition of corestriction. The block-permutation obstruction is zero: its representation is \(n\) copies of the coset permutation representation \(Q\), and (24B) gives
\(w_2(nQ)=n w_2(Q)+\binom n2 w_1(Q)^2=0\), with \(w_1(nQ)=0\), when \(4\mid n\). Hence its lifts can be chosen multiplicatively. There are no cross terms from the oriented blocks, proving (24C) in this case. For \(V=A-B\) of rank zero and determinant one, the two actual determinants agree. Add their common determinant line to both to orient them, then add the same number of trivial lines to make their equal ranks divisible by four. The actual result applies to both; subtraction and (24B) give (24C) for \(V\).

For a unitary complex matrix, the spin cover on its underlying real space pulls back as
\(\{(g,z):z^2=\det g\}\).
Here is an explicit verification. Diagonalize \(g\) by a unitary orthonormal basis. A rotation of angle \(\theta_j\) in its \(j\)-th real plane lifts to \(\exp(\theta_j e_{2j-1}e_{2j}/2)\); changing the sum of the chosen angles by \(2\pi\) changes the lift by \(-1\). In the exterior-algebra spin model its operator is \(z^{-1}\bigwedge g\), with \(z^2=\prod_j e^{i\theta_j}\). This conjugates the Clifford vector operators by \(g\), and multiplication of these operators proves the cover identification for products, not just diagonal matrices. Thus its cocycle is the determinant square-root obstruction, and virtual subtraction preserves that assertion. In a real plane the same rotation cover and a unit-vector reflection lift give \(O(2)\)'s double cover with reflection square one. The split plane \(\operatorname{Ind}1=1+\det\) has \(w_2=0\); the two planes have the same \(w_1\), so (24B) makes \(w_2(r(\chi))\) exactly that rotation/reflection lifting obstruction. \(\square\)

**Lemma 7.8 (the dihedral Fourier calculation).** Let \(E/F\) be separable quadratic, \(\chi:E^\times\to\mathbb C^\times\) finite-order and trivial on \(F^\times\), and \(0\ne\Delta\in E\) have trace zero. Then
\[
W_F(\operatorname{Ind}(\chi-1))=\chi(\Delta).
\tag{24D}
\]

**Proof.** At an infinite place the only quadratic extension is \(\mathbb C/\mathbb R\), and a continuous finite-order character of the connected group \(\mathbb C^\times\) is trivial, so the assertion is immediate. Now suppose \(F\) is nonarchimedean. Choose \(\beta\in E\) with trace one; the trace pairing is nondegenerate, so it exists. The line \(Fx\Delta\) is perpendicular to \(F\bar x\) for \(\operatorname{Tr}(uv)\), because \(x\bar x=Nx\). In the coordinates \(y=x(s\Delta+t\beta)\), additive measure is \(J|Nx|_F ds\,dt\), for a fixed positive \(J\) and the self-dual \(F\)-measure. Integration of the Fourier transform along \(F\bar x\) then gives
\[
\int_F\widehat f(a\bar x)da=J\int_F f(a x\Delta)da.
\tag{24E}
\]
For complete justification, average the integral in the Fourier variable over growing compact additive ideals. Character orthogonality (9B) restricts \(t\) to a shrinking annihilator. A locally constant compactly supported function is constant on that sufficiently small subgroup, so the integrals stabilize at its restriction to \(t=0\). The factor \(|Nx|\) cancels the inverse factor from this Fourier substitution. This proves (24E) without a distributional interchange.

The quotient \(E^\times/F^\times\) is compact: its valuation quotient is finite and its unit quotient is compact. Unfold the central zeta integral along this quotient. Since \(|a|_E^{1/2}=|a|_F\) for \(a\in F^\times\), its fibre integral is \(\int_F f(ax)da\). For the dual character use \(x\mapsto\bar x\): \(\chi(\bar x)=\chi(x)^{-1}\). Equation (24E) and then translation \(x\mapsto x\Delta\) on the compact quotient show that the dual central integral is
\(J|\Delta|_E^{-1/2}\chi(\Delta)^{-1}\) times the original. Here \(\chi(\Delta)^2=1\), since \(\Delta^2\in F\) in characteristic different from two, and \(\Delta\in F\) in characteristic two. Thus the inverse equals the value. The two L-factors agree: a ramified character has both factors one, while an unramified character is conjugation-invariant and hence equals its inverse on a uniformizer. Equation (6), with any test whose original integral is nonzero, gives
\(\epsilon_E(1/2,\chi)=J|\Delta|_E^{-1/2}\chi(\Delta)\).
For \(\chi=1\) the same calculation gives the identical scalar without the character value. Their quotient and rank-zero induction prove (24D). \(\square\)

**Proof of Theorem 7.4.** Write \(J(G)\) for virtual real representations of rank zero and determinant one. The determinant tensor formula
\(\det(V\otimes U)=(\det V)^{\dim U}(\det U)^{\dim V}\)
follows by triangularizing the two matrices; it shows that \(J(G)\) is an ideal. Induction preserves it by the determinant/transfer formula. On this ideal, \(W\) is multiplicative and \(w_2\) additive, by (24B). Both are preserved by induction: for \(W\) use rank-zero induction at \(s=1/2\), and for the right side use (24C) and the proved invariant/corestriction law, NT-CFT-24, Theorem 24.2. Duality also gives \(W(A)^2=1\), since a real finite-image representation is unitary and self-dual and has determinant one.

Apply Lemma 7.5 to a finite quotient through which \(A\) factors and multiply its odd induction expression for \(1\) by \(A\). Each restricted tensor term is in the corresponding ideal. Its subgroup has a normal nilpotent subgroup of index at most two, so Lemma 7.6 reduces it to realifications of complex rank-zero terms and dihedral terms. Because both sides of (24) are signs, proving it for these terms proves it for the odd multiple \(qA\), and hence for \(A\) itself.

For a realification of complex rank-zero \(U\), put \(\xi=\det U\). Its complexification is \(U+U^\vee\). Equation (16) at the centre gives \(W=\xi(-1)\). Lemma 7.7 identifies its degree-two class with the obstruction to a continuous square root of \(\xi\). Such a root exists precisely when \(\xi(-1)=1\). Here is the character-extension check. For a compact abelian unit group \(K\), a character trivial on its two-torsion defines a character on \(2K\) by \(2x\mapsto\xi(x)\). This is continuous since \(K/\ker2\to2K\) is a compact-to-Hausdorff isomorphism. Choose an open subgroup of \(K\) whose intersection with \(2K\) is killed by that character, descend to the finite quotient and extend by choosing roots. The resulting character squares to \(\xi\). The uniformizer factor can be treated independently by choosing its square root. The only element of order two in \(F^\times\), in characteristic different from two, is \(-1\); the necessity is immediate. Finite image can be retained throughout these extensions, so the resulting character extends to \(G_F\) by the actual reciprocity and finite-quotient proofs in the preceding Weil lesson.

In characteristic different from two, the coefficient map \(H^2(G_F,\{\pm1\})\to\operatorname{Br}(F)\) is injective. To see this directly, if a sign cocycle is a coboundary of a \(\bar F^\times\)-cochain \(t\), its square is a one-cocycle. The actually proved Hilbert 90, NT-CFT-03, Theorem 3.1, writes \(t(g)^2=g(b)/b\). Choose a square root of \(b\) in the separable closure and divide \(t\) by its coboundary; this makes \(t\) sign-valued. The original sign cocycle was therefore already a sign coboundary. All these continuous cochains pass through a finite extension. The local invariant theorem now says that the obstruction has invariant zero or one-half according as the root exists or does not exist. Its exponential is exactly \(\xi(-1)\). In characteristic two the coefficient map is trivial and \(\xi(-1)=1\), so the formula still holds.

For a dihedral term, reciprocity and transfer identify it with \(\operatorname{Ind}(\chi-1)\) for a quadratic \(E/F\), with \(\chi\) trivial on \(F^\times\). Indeed transfer of an outside element in a cyclic-by-two group is its square; inversion and a reflection square one make that transfer trivial. Lemma 7.8 gives its root number \(\chi(\Delta)\). Its obstruction in Lemma 7.7 vanishes exactly when \(\chi\) has a continuous square root trivial on \(F^\times\). To verify this equivalence, a lift through the rotation cover restricts to that square-root character on \(G_E\); its reflection square-one relation makes its transfer to \(F^\times\) trivial. Conversely a square-root character trivial there has conjugation equal to its inverse and outside-square value one; its induced plane supplies the required lift.

The compact group \(E^\times/F^\times\) has just one nontrivial element of order two when the characteristic is not two, represented by \(\Delta\). For if \(x^2\in F\) and \(x\notin F\), its two conjugates are \(x,-x\), so its trace is zero and its class is that of \(\Delta\). In characteristic two a separable extension contains no new purely inseparable square root, so this quotient has no two-torsion. The compact character-extension argument above shows that its square-root obstruction is nonzero precisely when \(\chi(\Delta)=-1\); in characteristic two it is always zero and \(\chi(\Delta)=1\). The same coefficient injection and invariant theorem prove (24) for the dihedral terms. At a complex place the Galois group is trivial. At a real place, \(A=m(\operatorname{sgn}-1)\) with even \(m\); its root is \(i^m=(-1)^{m/2}\), while the Whitney formula gives \(w_2(A)=\binom m2 x^2\), whose coefficient is \(m/2\pmod2\). The nonzero real Brauer class has invariant one-half by NT-CFT-24, Theorem 24.2, giving the same sign. This covers all local fields and completes the proof. \(\square\)

## 8. Exercises with solutions

**Exercise 8.1 (easy).** Compute \(L_F(s,\operatorname{Ind}_{W_E}^{W_F}1)\) for an unramified quadratic extension and compare it with \(L_F(s,1)L_F(s,\omega_{E/F})\).

**Solution.** The Frobenius matrix exchanges the two cosets and has eigenvalues \(1,-1\). Inertia is trivial. Hence its factor is \((1-q_F^{-2s})^{-1}\). The two one-dimensional factors are \((1-q_F^{-s})^{-1}\) and \((1+q_F^{-s})^{-1}\); their product is the same. Since \(q_E=q_F^2\), it also equals \(L_E(s,1)\), checking induction and multiplicativity simultaneously.

**Exercise 8.2 (medium).** Compute the unramified quadratic \(\lambda\)-constant for a general additive conductor, specifying the measures.

**Solution.** Use self-dual measures on \(F\) and \(E\). Write \(n=n_F(\psi)\). Unramified trace preserves this conductor and \(q_E=q_F^2\). Formula (9) and self-dual volumes give \(\epsilon_F(1)=q_F^{n/2}\), \(\epsilon_F(\omega)=(-1)^nq_F^{n/2}\), and \(\epsilon_E(1)=q_F^n\). Substitution in (18) gives \((-1)^n\). In particular the answer is one when \(n=0\), and minus one when \(n=1\). With arbitrary measures one must retain their volume ratio in (18); it is not legitimate to suppress it while asserting the same normalized answer.

**Exercise 8.3 (medium).** Show that \(|\epsilon_F(1/2,V,\psi,dx_\psi)|=1\) for unitary \(V\).

**Solution.** Conjugating the character functional equation gives \(\overline{\epsilon(\chi,\psi,dx)}=\epsilon(\bar\chi,\psi_{-1},dx)\). Its extension to representations follows from uniqueness, because the conjugated family obeys the same multiplicativity, measure scaling and degree-zero induction. For unitary \(V\), \(\bar V\simeq V^\vee\). Since \(\omega_{1/2}\) is real-valued, the conjugate of \(\epsilon(V\otimes\omega_{1/2},\psi,dx_\psi)\) is \(\epsilon(V^\vee\otimes\omega_{1/2},\psi_{-1},dx_\psi)\). Formula (15), applied to \(V\otimes\omega_{1/2}\), makes the product of these two constants one. That product is the required absolute-value square.

**Exercise 8.4 (hard).** Prove uniqueness of the local constants. Show explicitly how an unramified twist affects the dimension-zero Brauer decomposition.

**Solution.** For an irreducible \(V=V_0\otimes\eta\) with finite-image \(V_0\), decompose \([V_0]-d[1]\) as in (10). Tensoring gives (11), where each difference is \(\chi_j\eta|_{W_{E_j}}-\eta|_{W_{E_j}}\). The equality of two proposed theories on one-dimensional characters, followed by degree-zero induction, makes their ratio one on each of these terms. Their ratio is also one on \(d[\eta]\). Thus it is one on \(V\); multiplicativity through a composition series proves the assertion for every smooth representation. At a real place, subtract the induction of the trivial complex character from an induced character; degree-zero induction treats that difference, while the trivial induction is the sum of the two known real characters. This covers the complete real classification and finishes the uniqueness proof. No choice-independence for a newly defined product is asserted here: that is the existence theorem.

## Proof dependencies and free reading materials

The character equation, Fourier inversion, Gauss calculation and trace conductor are proved in Lemmas 2.1–2.2. The earlier archimedean Mellin, Gaussian and gamma proofs are NT-ADL-08, Theorem 8.1 and Propositions 8.2–8.4; their Fourier prerequisites are the actual Gaussian and Euclidean inversion proofs in NT-ADL-05. Integer complex Brauer induction is the actually written RT-FIN-11, Theorem 5.1, with the nilpotent and local induction arguments in §§1–4. Its dimension-zero refinement is proved here in (10A). The smooth, reciprocity, transfer and real-classification inputs have exact proofs in the preceding Weil lesson, Propositions 1.1–1.2, Theorems 1.3, 2.2, 4.1 and 5.1, and Proposition 6.1. Conductors, upper groups and trace duals use the preceding conductor lesson, Lemmas 1.1–1.6 and 2.4, Theorems 2.1, 2.6 and 4.1.

Sections 3A–3D prove existence, including every Brauer relation and all smooth unramified twists. Their global analytic inputs are solely the rank-one proofs NT-ADL-09, Theorem 9.2; NT-ADL-10, Theorem 10.1, equations (3) and (5)–(8); and NT-CFT-21 §6, equations (27)–(34). The finite-character reciprocity map and its comparison at all completions, in both characteristics, are actually proved in NT-CFT-16 §6 and Theorem 16.4. Number-field unit and class-group structure is proved in NT-ADL-03, Corollary 3.4; the function-field compactness and unit support used in the character extension are actually written in NT-CFT-14 §§1–2. Local field realization uses the earlier Frobenius lesson, Lemmas 1.0a–1.0b, whose complete-valuation hypotheses are available in either characteristic from the first lesson.

Lemma 7.5 supplies its own real induction proof. The real/complex/quaternionic classification used there is the actual conjugate-linear proof in RT-FIN-04, Theorems 2.1 and 3.1 and Proposition 3.2. Lemmas 7.6–7.8 prove the real generator, Clifford class and dihedral Fourier assertions. Hilbert 90 is NT-CFT-03, Theorem 3.1. The Brauer invariant and corestriction law are NT-CFT-24, Theorem 24.2. Theorem 7.4 then proves the orthogonal formula, including characteristic two. No monodromy operator is included in these L-factors yet.

These locators refer to actual inspected earlier programme proofs. Their present public editions and transitive free-source provenance remain subject to the programme revision; a locally retained or privately fetched source does not certify public accessibility. The new proof reconstruction also requires the programme's integration review before any claim of complete compliance. This paragraph records those limits rather than treating a bibliography or a future lesson title as a proof provider.

The following human-authored materials are freely readable. They were used to verify conventions and the original theorem scopes; the arguments and exact earlier proof providers above carry the proof obligations.

- **Pierre Deligne**, [*Les constantes des équations fonctionnelles des fonctions L*, free IAS author text](https://publications.ias.edu/sites/default/files/Number20.pdf), §1.5 for virtual induction, §§3.3–3.4 for character constants, and §§4.2–4.16 for the existence relation argument. The arithmetic and geometric reciprocity conventions are fixed in its §2.3.
- **Pierre Deligne and Guy Henniart**, [*Sur la variation, par torsion, des constantes locales d'équations fonctionnelles de fonctions L*, free IAS author text](https://publications.ias.edu/sites/default/files/Number43.pdf), §§0–1 for truncated exponentials, §2 for induction with an abelian normal subgroup, §§3.2–3.7 for norm parameters, and §§4.6–4.8 for sharp twisting. The endpoint distinction is proved and illustrated here.
- **Pierre Deligne**, [*Les constantes locales de l'équation fonctionnelle de la fonction L d'Artin d'une représentation orthogonale*, free IAS author text](https://publications.ias.edu/sites/default/files/Number26.pdf), §§1.3–1.5 for the class and theorem, §§2.1–2.9 for its real-group reduction, and §§3.1–3.3 for realification and dihedral calculations. Lemma 7.5 independently supplies the needed real induction step.
- **Jayce R. Getz and Heekyoung Hahn**, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*, free author draft of 22 April 2022](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §12.2, equations (12.9)–(12.13), for a further presentation of these conventions. All section numbers refer to this free draft.
