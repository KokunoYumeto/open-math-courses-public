# Rank-two systems and their congruences

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The deck group \(\mu_n\) of the cover \(C_n\to B_t\) splits the cohomology of \(C_n\) into pieces indexed by the characters \(\theta\) of \(\mu_n\). This lesson shows that each piece \(V_\theta\) looks like the cohomology of an elliptic curve: it is two-dimensional, with determinant the inverse cyclotomic character and Hodge–Tate weights \(0\) and \(1\), and it forms a compatible system as the coefficient prime varies. The pieces for the trivial character and for a character of order three are the cohomology of genuine elliptic curves, the twist \(B_t\) and an elliptic curve \(A_t\). Finally, because the first cohomology of \(C_n\) is free over the integral group ring, two characters that agree modulo \(\ell\) give the same residual representation at \(\ell\). This produces the chain of congruences along which automorphy is moved in Lesson 8.

**Prerequisites.** The first four lessons of this course, in particular Proposition 5.1 of [*Cyclic covers of an elliptic curve with two branch points*](cyclic-covers-of-an-elliptic-curve-with-two-branch-points.md) (the involution and the rotations) and Corollary 3.2 of [*Integral homology and Picard–Lefschetz transvections*](integral-homology-and-picard-lefschetz-transvections.md) (freeness over the group ring). From *Galois representations*: [*Frobenius elements and determination by traces*](course:LG-GAL/frobenius-elements-and-determination-by-traces) and [*p-adic Hodge theory and the Fontaine–Mazur conjecture*](course:LG-GAL/p-adic-hodge-theory-and-the-fontaine-mazur-conjecture).

## 1. The standing choices

For the rest of the course, \(K\) is an imaginary quadratic field and \(E\colon y^2=h(x)\) is an elliptic curve over \(K\) without complex multiplication. We use Serre's theorem on the images of Galois representations on torsion points.

**Theorem 1.1 (named result N4: Serre's open image theorem).** Let \(E\) be an elliptic curve without complex multiplication over a number field \(K\). For all but finitely many primes \(p\), the image of \(G_K\) acting on \(E[p](\overline K)\) is \(\mathrm{GL}_2(\mathbb F_p)\).

This is Théorème 2 of Section 4.2 of [Ser72]; the course uses it without proof. Fix a prime \(p>100\) such that the image of \(G_K\) on \(E[p]\) contains \(\mathrm{SL}_2(\mathbb F_p)\), and put
\[
n=3p,\qquad F=K(\mu_n).
\tag{1.1}
\]
By Exercise 6.1 of Lesson 1, \(F\) is a CM field, abelian over \(\mathbb Q\), and \(\zeta_5\notin F\). Let \(U\subset\mathbb A^1_K\) be the parameter set of Lemma 1.1 of Lesson 2 for this \(n\), shrunk by finitely many points whenever convenient. Until Lesson 7 the parameter \(t\in U(K)\) is arbitrary, and we write \(C_m=C_{m,t}\) for \(m\mid n\) and \(B=B_t\). All rotations and the involution \(w\) are defined over \(F\), because \(\mu_n\subset F\).

## 2. Character spaces

Fix an embedding \(\overline{\mathbb Q}\hookrightarrow\mathbb C\) and let \(M=\mathbb Q(\mu_n)\subset\overline{\mathbb Q}\). For each prime \(\ell\) choose an embedding \(j_\ell\colon\overline{\mathbb Q}\hookrightarrow\overline{\mathbb Q}_\ell\) and an isomorphism \(\iota_\ell\colon\overline{\mathbb Q}_\ell\to\mathbb C\) with \(\iota_\ell\circ j_\ell\) equal to the fixed complex embedding. A *rotation character* is a homomorphism
\[
\theta\colon\mu_n(F)\longrightarrow M^\times;
\]
since \(\mu_n(F)\subset\overline{\mathbb Q}\), every such \(\theta\) has the form \(u\mapsto u^a\) for a unique \(a\in\mathbb Z/n\mathbb Z\). For \(u\in\mu_n(F)\) we also write \(u\) for the deck transformation \(Y\mapsto uY\) of \(C_n\).

**Definition 2.1.** For a rotation character \(\theta\) and a prime \(\ell\),
\[
\begin{aligned}
&V_{\theta,\ell}=\bigl\{x\in H^1(C_n):\ u^*x=j_\ell(\theta(u))\,x\\
&\qquad\text{for all }u\in\mu_n(F)\bigr\},\quad(2.1)
\end{aligned}
\]
where \(H^1(C_n)=H^1(C_n)\otimes\overline{\mathbb Q}_\ell\) is defined through the Tate module of the Jacobian, as in Lesson 1. The rotations commute with \(G_F\), so \(V_{\theta,\ell}\) is a representation of \(G_F\). We write \(V_\theta\) for the family of these representations as \(\ell\) varies.

When two characters are compared at \(\ell\), both use the same embedding \(j_\ell\). This convention matters for the congruences of Section 6.

## 3. Results on abelian varieties used without proof

Two groups of standard facts are used in this lesson. The first is algebraic.

**Theorem 3.1 (named result N10: abelian varieties).** Let \(A\) be an abelian variety of dimension \(g\) over a field \(k\), and \(\ell\) a prime different from the characteristic of \(k\).

1. For every endomorphism \(\alpha\) of \(A\), the characteristic polynomial of \(\alpha\) on \(V_\ell A=T_\ell A\otimes\mathbb Q_\ell\) is a monic polynomial of degree \(2g\) with integer coefficients, independent of \(\ell\) [Milne, I, Theorem 10.9 and Proposition 10.20].
2. A polarization \(\lambda\colon A\to A^\vee\) defines a skew-symmetric pairing \(e^\lambda\colon T_\ell A\times T_\ell A\to\mathbb Z_\ell(1)\), compatible with the action of \(\operatorname{Gal}(k^{\mathrm{sep}}/k)\), and perfect when \(\lambda\) is an isomorphism. If \(\mathcal L\) is a line bundle defining \(\lambda\) and \(\phi\) is an endomorphism, then \(e^{\phi^*\mathcal L}(a,a')=e^{\mathcal L}(\phi a,\phi a')\), and \(e^{\mathcal L}\) depends only on the algebraic equivalence class of \(\mathcal L\) [Milne, I, Section 13, Proposition 13.2].
3. Let \(k\) be a number field and \(v\) a finite place not dividing \(\ell\). If a smooth projective curve over \(k\) has good reduction at \(v\), so does its Jacobian [Milne, IV, Proposition 4.1]; if an abelian variety \(A\) has good reduction at \(v\), then \(V_\ell A\) is unramified at \(v\), and reduction identifies \(T_\ell A\), as a representation of the decomposition group, with \(T_\ell\) of the reduction, on which an arithmetic Frobenius element acts as the Frobenius endomorphism of the reduction [Milne, IV, Theorem 3.5 and its proof].

The second group concerns \(p\)-adic Hodge theory.

**Theorem 3.2 (named result N7, first part: Hodge–Tate decomposition and semistability).** Let \(L\) be a finite extension of \(\mathbb Q_\ell\) and \(A/L\) an abelian variety.

1. There is a \(G_L\)-equivariant isomorphism
\[
\begin{aligned}
&H^1(A)\otimes_{\mathbb Q_\ell}\mathbb C_\ell\\
&\quad\cong\bigl(H^0(A,\Omega^1)\otimes_L\mathbb C_\ell(-1)\bigr)\\
&\qquad\oplus\bigl(H^1(A,\mathcal O_A)\otimes_L\mathbb C_\ell\bigr),
\end{aligned}
\]
functorial for endomorphisms of \(A\). Consequently, for an embedding \(\tau\colon L\to\overline{\mathbb Q}_\ell\), the multiplicity of the Hodge–Tate weight \(1\) on the \(\tau\)-component is \(\dim H^0(A,\Omega^1)\otimes_{L,\tau}\overline{\mathbb Q}_\ell\), and that of the weight \(0\) is \(\dim H^1(A,\mathcal O_A)\otimes_{L,\tau}\overline{\mathbb Q}_\ell\).
2. If \(A\) has semistable reduction, then \(H^1(A)\) is semistable; if \(A\) has good reduction, it is crystalline. Every abelian variety acquires semistable reduction over a finite extension of \(L\) (Grothendieck), so \(H^1(A)\) is potentially semistable.

Part (1) is Faltings' Hodge–Tate decomposition [BC, Theorem 2.2.3], proved by Tate for abelian varieties with good reduction. Part (2) is the semistable comparison theorem of Tsuji, with the crystalline case due to Faltings, Fontaine–Messing and others; for abelian varieties Coleman–Iovita and Breuil also proved the converse statements. These results and their references are surveyed in [Ber, Section II.5.1]. Grothendieck's semistable reduction theorem is recorded in [Milne, I, Theorem 17.3]. The course uses all of them without proof.

## 4. Properties of the character spaces

**Lemma 4.1.** Let \(C\) be a smooth projective connected curve over a field \(k\), of genus \(g\ge1\), with Jacobian \(J\) and canonical principal polarization \(\lambda\). Every automorphism \(\alpha\) of \(C\) over \(k\) satisfies \(e^\lambda(\alpha_*a,\alpha_*a')=e^\lambda(a,a')\) on \(T_\ell J\).

**Proof.** Over \(\bar k\), choose a point \(P_0\) and let \(\Theta\subset J\) be the image of \(D\mapsto[D-(g-1)P_0]\) on effective divisors of degree \(g-1\); its line bundle defines \(\lambda\). The automorphism \(\alpha_*\) of \(J\) maps \([D-(g-1)P_0]\) to \([\alpha D-(g-1)P_0]+(g-1)[P_0-\alpha P_0]\), so \(\alpha_*(\Theta)=\Theta+c\) with \(c=(g-1)[P_0-\alpha P_0]\), a translate. Hence \(\alpha_*^*\mathcal O(\Theta)\) is a translate of \(\mathcal O(\Theta)\) by \(\pm c\), which is algebraically equivalent to \(\mathcal O(\Theta)\). By Theorem 3.1(2), \(e^{\mathcal O(\Theta)}(\alpha_*a,\alpha_*a')\)\(=e^{\alpha_*^*\mathcal O(\Theta)}(a,a')\)\(=e^{\mathcal O(\Theta)}(a,a')\). \(\square\)

Dualizing \(e^\lambda\) gives a perfect skew-symmetric pairing \(\langle\ ,\ \rangle\) on \(H^1(C,\mathbb Z_\ell)\) with values in \(\mathbb Z_\ell(-1)\), compatible with \(G_k\) and invariant under \(\alpha^*\) for every automorphism \(\alpha\) of \(C\). Over \(\mathbb C\) it is, up to sign, the cup product.

**Proposition 4.2.** For every \(t\in U(K)\) and every rotation character \(\theta\):

1. \(V_{\theta,\ell}\) has dimension two and \(\det V_{\theta,\ell}=\epsilon_\ell^{-1}\);
2. at every place of \(F\) above \(\ell\), \(V_{\theta,\ell}\) is potentially semistable with labelled Hodge–Tate weights \(\{0,1\}\) at every embedding;
3. there is a finite set \(S\) of places of \(F\), independent of \(\ell\), such that \(V_{\theta,\ell}\) is unramified at every \(v\notin S\) with \(v\nmid\ell\), and the characteristic polynomial of \(\operatorname{Frob}_v\) on \(V_{\theta,\ell}\) is the image under \(j_\ell\) of a polynomial in \(M[T]\) that does not depend on \(\ell\).

**Proof.** (1) By Corollary 3.2 of Lesson 4, \(H^1(C_n,\mathbb Z_\ell)\) is free of rank two over \(\mathbb Z_\ell[\mu_n]\). After extending scalars to \(\overline{\mathbb Q}_\ell\), the group algebra is a product of copies of \(\overline{\mathbb Q}_\ell\), one for each character, and the \(\theta\)-factor of \(\overline{\mathbb Q}_\ell[\mu_n]^2\) has dimension two.

For the determinant, let \(\langle\ ,\ \rangle\) be the pairing on \(H^1(C_n)\) described after Lemma 4.1. Invariance under the rotations gives \(\langle u^*x,u^*y\rangle=\langle x,y\rangle\), so the \(\theta\)-space pairs to zero with the \(\theta'\)-space unless \(\theta\theta'=1\); since the pairing is perfect, it pairs \(V_\theta\) perfectly with \(V_{\theta^{-1}}\). The involution \(w\) satisfies \(wuw=u^{-1}\) (Lesson 2, (5.2)), so for \(x\in V_\theta\),
\[
\begin{aligned}
u^*w^*x&=(w\circ u)^*x=(u^{-1}\circ w)^*x\\
&=w^*(u^{-1})^*x=\theta(u)^{-1}w^*x,
\end{aligned}
\]
and \(w^*\) maps \(V_\theta\) to \(V_{\theta^{-1}}\). Put
\[
[x,y]_\theta=\langle x,w^*y\rangle,\qquad x,y\in V_{\theta,\ell}.
\]
This is a perfect \(G_F\)-equivariant pairing on \(V_{\theta,\ell}\) with values in \(\overline{\mathbb Q}_\ell(-1)\), because \(w\) is defined over \(F\). It is alternating:
\[
\begin{aligned}
[y,x]_\theta&=\langle y,w^*x\rangle=\langle w^*y,w^*w^*x\rangle\\
&=\langle w^*y,x\rangle=-\langle x,w^*y\rangle\\
&=-[x,y]_\theta,
\end{aligned}
\]
using invariance under \(w^*\), \(w^2=1\) and skew-symmetry. A perfect alternating pairing on a two-dimensional space identifies \(\wedge^2V_{\theta,\ell}\) with the target, so \(\det V_{\theta,\ell}=\epsilon_\ell^{-1}\).

(2) Embed \(F\) into \(\mathbb C\) and let \(a_\theta\) be the dimension of the \(\theta\)-eigenspace of the rotations on \(H^0(C_n,\Omega^1)\otimes\mathbb C\). Since \(w\) maps the \(\theta\)-eigenspace of holomorphic differentials to the \(\theta^{-1}\)-eigenspace, \(a_\theta=a_{\theta^{-1}}\). By the Hodge decomposition, \(H^1(C_n(\mathbb C),\mathbb C)=H^{1,0}\oplus H^{0,1}\) with \(H^{0,1}=\overline{H^{1,0}}\), and complex conjugation maps the \(\theta\)-eigenspace to the \(\bar\theta=\theta^{-1}\)-eigenspace, because the rotations act on \(H^1(C_n(\mathbb C),\mathbb R)\). So the \(\theta\)-eigenspace of \(H^1(C_n(\mathbb C),\mathbb C)\) has dimension \(a_\theta+a_{\theta^{-1}}=2a_\theta\). By (1) and Proposition 1.1 of Lesson 4 this dimension is two, so \(a_\theta=1\), for every complex embedding and every character. The same holds for the \(\theta\)-eigenspace of \(H^1(C_n,\mathcal O)\), whose dimension is \(a_{\theta^{-1}}\) by Serre duality. Theorem 3.2(1), applied to the Jacobian over \(F_v\), with the functoriality for the rotations, shows that on \(V_{\theta,\ell}\) each embedding carries the Hodge–Tate weights \(1\) and \(0\) once each. Potential semistability passes from \(H^1(C_n)\), by Theorem 3.2(2), to its direct summand \(V_{\theta,\ell}\).

(3) The curve \(C_n\), its rotations and its involution extend to a smooth projective curve with automorphisms over \(\mathcal O_{F}[1/N]\) for some integer \(N\); let \(S\) be the set of places dividing \(N\). For \(v\notin S\), \(v\nmid\ell\), the Jacobian \(J\) of \(C_n\) has good reduction \(\widetilde J\) at \(v\), \(V_\ell J\) is unramified at \(v\), and an arithmetic Frobenius acts on \(T_\ell J\cong T_\ell\widetilde J\) as the Frobenius endomorphism \(\pi_v\) of \(\widetilde J\), by Theorem 3.1(3). The rotations extend to \(\widetilde J\) and commute with this identification. The geometric Frobenius therefore acts on \(H^1=\operatorname{Hom}(T_\ell J,\overline{\mathbb Q}_\ell)\) as the transpose of \(\pi_v\), and \(u^*\) acts as the transpose of \(u_*\). Hence, for \(k\ge1\),
\[
\begin{aligned}
&\operatorname{tr}\bigl(\operatorname{Frob}_v^k\,u^*\mid H^1(C_n)\bigr)\\
&\quad=\operatorname{tr}\bigl(u_*\pi_v^k\mid T_\ell\widetilde J\bigr),
\end{aligned}
\]
which is an integer independent of \(\ell\) by Theorem 3.1(1), applied to the endomorphism \(u_*\pi_v^k\) of \(\widetilde J\). The projector onto \(V_{\theta,\ell}\) is
\[
e_\theta=\frac1n\sum_{u\in\mu_n(F)}j_\ell\bigl(\theta(u)\bigr)^{-1}u^* ,
\]
used here in characteristic zero only, so \(\operatorname{tr}(\operatorname{Frob}_v^k\mid V_{\theta,\ell})=\operatorname{tr}(\operatorname{Frob}_v^ke_\theta\mid H^1)\) is \(j_\ell\) of an element of \(M\) independent of \(\ell\). A two-dimensional representation has characteristic polynomial \(T^2-\operatorname{tr}(\operatorname{Frob}_v)T+\det(\operatorname{Frob}_v)\), and \(\det(\operatorname{Frob}_v)=\epsilon_\ell^{-1}(\operatorname{Frob}_v)=Nv\) by (1), since \(\operatorname{Frob}_v\) is geometric. \(\square\)

**Remark 4.3.** The representations \(V_{\theta,\ell}\) are in fact semisimple, by Faltings' theorem on \(\ell\)-adic representations of abelian varieties over number fields. The course does not use this. Each time Lesson 8 compares \(V_{\theta,\ell}\) with an automorphic Galois representation, the residual representation of \(V_{\theta,\ell}\) at that \(\ell\) is absolutely irreducible by the choices of Lesson 7, so \(V_{\theta,\ell}\) is irreducible there by Lemma 1.1 of Lesson 1, and the comparison of Frobenius traces gives an isomorphism directly.

## 5. The two elliptic-curve realizations

For a finite morphism \(\pi\colon C\to C'\) of smooth projective connected curves, pushforward of divisors gives a homomorphism \(\pi_*\colon J_C\to J_{C'}\) and pullback gives \(\pi^\star\colon J_{C'}\to J_C\). On divisors \(\pi_*\pi^\star D=(\deg\pi)D\); if \(\pi\) is the quotient by a finite group \(H\) of automorphisms of \(C\), then also \(\pi^\star\pi_*D=\sum_{h\in H}h_*D\), because the fibre of \(\pi\) over \(\pi(P)\), counted with ramification, is the orbit \(HP\) counted with stabilizers. On cohomology we write \(\pi^*\colon H^1(C')\to H^1(C)\) for \(x\mapsto x\circ\pi_*\).

**Lemma 5.1.** If \(\pi\colon C\to C'=C/H\) is the quotient by a finite group \(H\) of automorphisms, then \(\pi^*\) is an isomorphism of \(H^1(C')\) onto the \(H\)-invariants \(H^1(C)^H\), equivariant for every Galois action for which \(\pi\) and \(H\) are defined over the ground field.

**Proof.** The identity \(\pi_*\pi^\star=\deg\pi\) on \(J_{C'}\) shows that \(\pi_*\colon V_\ell J_C\to V_\ell J_{C'}\) is surjective, so \(\pi^*\) is injective. For \(h\in H\), \(\pi\circ h=\pi\), so \((\pi^*x)\circ h_*=x\circ\pi_*\circ h_*=\pi^*x\): the image is invariant. Conversely, if \(y\in H^1(C)\) is \(H\)-invariant, then \(y\circ\pi^\star\circ\pi_*=y\circ\sum_hh_*=|H|\,y\), so \(y=\pi^*\bigl(|H|^{-1}y\circ\pi^\star\bigr)\). \(\square\)

**Proposition 5.2.** Let \(t\in U(K)\).

1. If \(\theta\) has order \(m>1\), then \(V_\theta\) is the image under pullback of the corresponding character space of \(H^1(C_m)\), where \(\theta\) is regarded as a character of the rotation group \(\mu_m\) of \(C_m\).
2. \(V_{1,\ell}\cong H^1(B)\) as representations of \(G_F\).
3. Let \(D=C_3/\langle w\rangle\) and \(A=\operatorname{Jac}(D)\). Then \(D\) has genus one, \(A\) is an elliptic curve over \(F\), and for each of the two characters \(\eta\) of order three there is a \(G_F\)-equivariant isomorphism \(V_{\eta,\ell}\cong H^1(A)\) for every \(\ell\).

**Proof.** (1) The map \(C_n\to C_m\), \(Y\mapsto Y^{n/m}\), is the quotient by the kernel \(H\) of \(\mu_n\to\mu_m\), \(u\mapsto u^{n/m}\), and it intertwines the rotation \(u\) of \(C_n\) with the rotation \(u^{n/m}\) of \(C_m\). By Lemma 5.1, pullback identifies \(H^1(C_m)\) with \(H^1(C_n)^H\), the sum of the character spaces of the characters trivial on \(H\), that is, of order dividing \(m\). A character \(\theta\) of order \(m\) factors through \(\mu_n\to\mu_m\), and pullback carries the \(\theta\)-space of \(H^1(C_m)\) onto \(V_\theta\).

(2) The same argument for the quotient \(C_n\to B\) by all of \(\mu_n\) identifies \(H^1(B)\) with \(H^1(C_n)^{\mu_n}=V_1\), compatibly with \(G_F\), since the quotient map is defined over \(K\).

(3) By (1) and (2), \(H^1(C_3)=V_1\oplus V_\eta\oplus V_{\eta^{-1}}\), each of dimension two, where \(V_1=H^1(B)\) and \(\eta,\eta^{-1}\) are the two characters of order three. The involution \(w\) covers \([-1]\) on \(B\), which acts on \(H^1(B)\) by \(-1\); and \(w^*\) exchanges \(V_\eta\) and \(V_{\eta^{-1}}\), as shown in the proof of Proposition 4.2. Hence
\[
H^1(C_3)^{w=1}=\{x+w^*x:\ x\in V_\eta\},
\]
of dimension two. By Lemma 5.1 for the quotient \(C_3\to D\), \(H^1(D)\cong H^1(C_3)^{w=1}\) has dimension two, so \(D\) has genus one; this agrees with Proposition 5.2 of Lesson 2, which computes the genus \((3-1)/2=1\) from the four fixed points of \(w\). The Jacobian of a curve of genus one is an elliptic curve, whether or not the curve has a rational point. The projection of \(x+w^*x\) to \(V_\eta\), along \(V_{\eta^{-1}}\), is \(x\). It is \(G_F\)-equivariant, because \(G_F\) commutes with \(w\) and with the rotations and so preserves both \(V_\eta\) and \(V_{\eta^{-1}}\). So \(V_{\eta,\ell}\cong H^1(C_3)^{w=1}\cong H^1(D)=H^1(A)\). \(\square\)

## 6. Evaluation of the integral group ring

A character projector has the denominator \(n\), so it cannot by itself compare residual representations at \(\ell=3\) or \(\ell=p\). The integral freeness of Lesson 4 can.

**Lemma 6.1.** Fix \(t\in U(K)\) and a prime \(\ell\). Let \(L\) be a finite extension of \(\mathbb Q_\ell\) containing \(j_\ell(M)\), with ring of integers \(\mathcal O\), maximal ideal \(\mathfrak m\) and residue field \(\kappa\). For a rotation character \(\theta\) put
\[
\mathcal T_\theta=H^1(C_n,\mathbb Z_\ell)\otimes_{\mathbb Z_\ell[\mu_n],\,j_\ell\theta}\mathcal O ,
\]
where \(\mathbb Z_\ell[\mu_n]\to\mathcal O\) sends \(u\) to \(j_\ell(\theta(u))\). Then \(\mathcal T_\theta\) is a free \(\mathcal O\)-module of rank two with a continuous action of \(G_F\), and \(\mathcal T_\theta\otimes_{\mathcal O}\overline{\mathbb Q}_\ell\cong V_{\theta,\ell}\). If \(j_\ell\theta\) and \(j_\ell\theta'\) have the same reduction as characters \(\mu_n\to\kappa^\times\), then
\[
\mathcal T_\theta/\mathfrak m\mathcal T_\theta\cong\mathcal T_{\theta'}/\mathfrak m\mathcal T_{\theta'}
\]
as \(\kappa[G_F]\)-modules.

**Proof.** By Corollary 3.2 of Lesson 4, \(H^1(C_n,\mathbb Z_\ell)\cong\mathbb Z_\ell[\mu_n]^2\), so \(\mathcal T_\theta\cong\mathcal O^2\). The action of \(G_F\) commutes with the group ring, because the rotations are defined over \(F\), so it passes to \(\mathcal T_\theta\). After inverting \(\ell\) the group algebra \(L[\mu_n]\) is a product of fields, and the quotient by the evaluation at \(j_\ell\theta\) is the \(\theta\)-isotypic part, which for a semisimple action of the commutative group \(\mu_n\) is the same as the eigenspace (2.1). Reducing modulo \(\mathfrak m\),
\[
\mathcal T_\theta/\mathfrak m\mathcal T_\theta=H^1(C_n,\mathbb Z_\ell)\otimes_{\mathbb Z_\ell[\mu_n],\,\overline{j_\ell\theta}}\kappa,
\]
which depends only on the reduced character \(\overline{j_\ell\theta}\). No assumption that \(\ell\) is prime to \(n\) is needed. \(\square\)

Choose a character \(\chi\) of order \(n=3p\) and write it uniquely as
\[
\begin{gathered}
\chi=\psi\eta,\\
\operatorname{ord}(\psi)=p,\qquad\operatorname{ord}(\eta)=3.\quad(6.1)
\end{gathered}
\]
For a system \(V_\theta\) write \(\overline V_{\theta,\ell}\) for the semisimplified reduction of a stable lattice in \(V_{\theta,\ell}\), with scalars extended to \(\overline{\mathbb F}_\ell\); it is independent of the lattice (Lesson 1, Section 1).

**Corollary 6.2 (the congruence chain).** For every \(t\in U(K)\),
\[
\begin{gathered}
\overline V_{\eta,p}\cong\overline V_{\chi,p},\qquad
\overline V_{\chi,3}\cong\overline V_{\psi,3},\\
\overline V_{\psi,p}\cong\overline V_{1,p},\quad(6.2)
\end{gathered}
\]
and \(\overline V_{\eta,p}\cong\overline{H^1(A)}\), \(\overline V_{1,p}\cong\overline{H^1(B)}\).

**Proof.** In residue characteristic \(\ell\), a root of unity of \(\ell\)-power order reduces to \(1\). So \(j_p\chi=j_p\psi\cdot j_p\eta\) and \(j_p\eta\) have the same reduction, \(j_3\chi\) and \(j_3\psi\) have the same reduction, and \(j_p\psi\) and the trivial character have the same reduction. Lemma 6.1 gives isomorphic reductions of the lattices \(\mathcal T\), hence isomorphic semisimplifications. The isomorphisms of Proposition 5.2 are isomorphisms of rational representations, so they preserve semisimplified reductions, even where the natural integral pullback maps have index divisible by \(\ell\). \(\square\)

The direction of propagation is fixed by (6.2): automorphy will pass from \(V_\eta=H^1(A)\) to \(V_\chi\) at \(p\), then to \(V_\psi\) at \(3\), and finally to \(V_1=H^1(B)\) at \(p\). The congruences impose no condition on \(t\). The conditions needed to apply the lifting theorem at each step are arranged in Lessons 6 and 7.

## 7. Exercises

**7.1.** Compute the genus of \(C_m/\langle w\rangle\) for each divisor \(m>1\) of \(n=3p\) (Lesson 2, Proposition 5.2), and conclude that among these quotients only \(C_3/\langle w\rangle\) is an elliptic curve.

**7.2.** Let \(\ell\nmid n\). Show that the reduction of \(\mathcal T_\theta\) is, up to semisimplification, the \(\bar\theta\)-eigenspace of the rotations on \(H^1(C_n,\overline{\mathbb F}_\ell)\), and that for distinct \(\theta,\theta'\) the reductions of \(j_\ell\theta\) and \(j_\ell\theta'\) are distinct.

**7.3.** Let \(\Gamma=\mu_n\) and \(\theta\) a character with values in \(\mathcal O\). In the free module \(\mathcal O[\Gamma]\), compare the eigen-submodule \(\{x:\ ux=\theta(u)x\ \text{for all }u\}\) with the quotient \(\mathcal O[\Gamma]/(u-\theta(u))\): show that the natural map from the first to the second is injective, with image \(n\) times the quotient. Conclude that the two lattices agree when \(\ell\nmid n\), and that for \(\ell\mid n\) only the quotient has a reduction that depends on \(\theta\) through its reduction alone.

**7.4.** Write \(\theta=u\mapsto u^a\). For which \(a\) is \(V_\theta\) defined by the curve \(C_m\) of smallest degree, and how many characters of each order \(1,3,p,3p\) are there?

## 8. Solutions

**7.1.** By Lesson 2, Proposition 5.2, \(C_m/\langle w\rangle\) has genus \((m-1)/2\). The divisors \(m>1\) of \(3p\) are \(3\), \(p\) and \(3p\), with genera \(1\), \((p-1)/2\) and \((3p-1)/2\). Since \(p>100\), the last two are at least \(50\). So only \(C_3/\langle w\rangle\) is an elliptic curve. The systems \(V_\chi\) and \(V_\psi\) are therefore not realized by this construction as cohomology of elliptic curves, and they are reached through automorphy lifting instead.

**7.2.** If \(\ell\nmid n\), then \(n\) is invertible in \(\mathcal O\) and the group ring \(\mathcal O[\mu_n]\) is a product of copies of \(\mathcal O\) (after enlarging \(\mathcal O\)), one for each character, with idempotents \(e_\theta\) defined over \(\mathcal O\). The tensor product with \(\kappa\) along \(\bar\theta\) picks out the factor \(e_{\bar\theta}\), which is the \(\bar\theta\)-eigenspace. Distinct characters of \(\mu_n\) have distinct reductions modulo \(\mathfrak m\), because reduction is injective on roots of unity of order prime to \(\ell\).

**7.3.** Put \(e'_\theta=\sum_{g\in\Gamma}\theta(g)^{-1}g\). Then \(ue'_\theta=\sum_g\theta(g)^{-1}ug\)\(=\theta(u)\sum_g\theta(ug)^{-1}ug\)\(=\theta(u)e'_\theta\). Conversely, let \(x=\sum_gx_gg\) satisfy \(ux=\theta(u)x\) for all \(u\). The coefficient of \(h\) in \(ux\) is \(x_{u^{-1}h}\), so \(x_{u^{-1}h}=\theta(u)x_h\) for all \(u,h\). Taking \(h=1\) and \(u=g^{-1}\) gives \(x_g=\theta(g)^{-1}x_1\), so \(x=x_1e'_\theta\). The eigen-submodule is therefore \(\mathcal Oe'_\theta\), free of rank one. The quotient \(\mathcal O[\Gamma]/(u-\theta(u))\) is identified with \(\mathcal O\) by \(g\mapsto\theta(g)\). Under this identification \(e'_\theta\mapsto\sum_g\theta(g)^{-1}\theta(g)=n\). So the natural map is multiplication by \(n\) on \(\mathcal O\): injective, an isomorphism exactly when \(n\) is a unit in \(\mathcal O\), that is, when \(\ell\nmid n\). Modulo \(\mathfrak m\), the quotient \(\kappa[\Gamma]/(u-\bar\theta(u))\) depends only on \(\bar\theta\), while for \(\ell\mid n\) the image of the eigen-submodule reduces to zero in it. This is why Lemma 6.1 uses the quotient.

**7.4.** The character \(u\mapsto u^a\) has order \(n/\gcd(a,n)\), and \(V_\theta\) is already defined on \(C_m\) with \(m\) equal to this order (Proposition 5.2(1)). There is \(1\) character of order \(1\), \(2\) of order \(3\), \(p-1\) of order \(p\) and \(2(p-1)\) of order \(3p\), in total \(3p=n\), one for each character space.

## Sources

- [OpenAI-030] OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI Math Release preprint, 4 October 2026, Section 5 (rank-two systems and integral congruences). https://github.com/openai/math/tree/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026
- [Ser72] J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15 (1972), 259–331, Section 4.2, Théorème 2. Digitized by the Göttingen State and University Library: https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0015/LOG_0024.pdf
- [Milne] J. S. Milne, *Abelian Varieties* (version 2.00, 2008), Chapter I, Theorem 10.9, Proposition 10.20, Section 13 (Proposition 13.2) and Theorem 17.3; Chapter IV, Theorem 3.5 and Proposition 4.1. https://www.jmilne.org/math/CourseNotes/AV.pdf
- [BC] O. Brinon and B. Conrad, *CMI Summer School notes on p-adic Hodge theory*, Theorem 2.2.3 (Faltings' Hodge–Tate decomposition). https://math.stanford.edu/~conrad/papers/notes.pdf
- [Ber] L. Berger, *An introduction to the theory of p-adic representations*, Section II.5.1 (comparison theorems). https://arxiv.org/abs/math/0210184
