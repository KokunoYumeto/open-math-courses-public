# The Rørdam–Winter criterion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The finite theorem of [Central sequences and the character criterion](central-sequences-and-the-character-criterion.md) (Theorem 2.2 there) asks for a unital homomorphism from the dimension-drop algebra \(I(2,3)\). This lesson proves a criterion of Rørdam and Winter for the existence of such a homomorphism (Proposition 1.1). Its hypothesis is a pair of orthogonal positive elements \(a_1=w^*w\) and \(a_2=ww^*\), together with a Cuntz comparison: the remainder \(1-a_1-a_2\) is dominated by a cut-down of \(a_1\). The proof constructs maps on \(M_3\) and \(M_2\) as in Lemma 4.1 of [Cuntz comparison and order-zero maps](cuntz-comparison-and-order-zero-maps.md). It works in every unital C\*-algebra; support projections and polar decompositions are taken in the bidual.

- The criterion (Proposition 1.1).
- Exact relations (Lemmas 2.1 to 2.3).
- Two orthogonal copies of the defect (Lemmas 3.1 and 3.2).
- Section algebras and a unitary in the bidual (Lemmas 4.1 to 4.3).
- The weighted flip and the proof (Lemmas 5.1 to 5.4).

The lesson follows [OpenAI-KRC, Proposition 2.1 and Section 3]. The notation is that of [Cuntz comparison and order-zero maps](cuntz-comparison-and-order-zero-maps.md): \(B\) is a unital C\*-algebra, \(B^{**}\) its universal enveloping von Neumann algebra acting on the Hilbert space \(H_u\) of the universal representation, \(s(T)\) the support projection of a positive \(T\in B^{**}\), and \(\operatorname{Her}(b)\) the norm closure of \(b^{1/2}Bb^{1/2}\), a C\*-subalgebra of \(B\).

*Facts used.* \(B^{**}\) is the closure of \(B\) in the strong operator topology of \(B(H_u)\), because \(B\) contains the identity operator ([The double commutant theorem](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem), Theorem 4.4); so a strong limit of elements of \(B\) lies in \(B^{**}\). Every \(*\)-homomorphism between C\*-algebras is contractive, and the continuous functional calculus commutes with \(*\)-homomorphisms for functions vanishing at \(0\) ([Order, local units and quotients of C\*-algebras](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones), Theorem 4.2 and Corollary 5.4). If \(x\in B^{**}\) commutes with every term of a sequence converging strongly to \(y\), then \(x\) commutes with \(y\); in particular \(s(T)\), the strong limit of \(T(T+\tau)^{-1}\), commutes with every element commuting with \(T\).

## 1. The criterion

**Proposition 1.1** (Rørdam–Winter; [RW, Proposition 5.1, (ii)\(\Rightarrow\)(iv), with \(n=2\)]; [OpenAI-KRC, Proposition 2.1]). Let \(B\) be a unital C\*-algebra and \(a_1,a_2\in B\) orthogonal positive contractions with \(a_1=w^*w\) and \(a_2=ww^*\) for some \(w\in B\). If, for some \(\varepsilon>0\),
\[
1_B-a_1-a_2\precsim(a_1-\varepsilon)_+,
\]
then there is a unital \(*\)-homomorphism \(I(2,3)\to B\).

Rørdam and Winter state their Proposition 5.1 for algebras of stable rank one and note that this hypothesis is used only in another implication; the proof below uses no such hypothesis.

Since \(a_1a_2=0=a_2a_1\), the elements \(1,a_1,a_2\) generate a commutative C\*-algebra, which is \(C(X)\) for a compact space \(X\) by Gelfand's theorem. There \(a_1,a_2\) are functions with values in \([0,1]\) whose product vanishes, so at each point at most one of them is nonzero. Hence \(a_1+a_2\le1\), and
\[
c=1-a_1-a_2
\]
is positive. The same pointwise reasoning is used below for continuous functions of \(a_1\) and \(a_2\).

*The idea of the proof.* The elements \(s_1,s_2\) of Lemma 2.2 behave like the two diagonal positions of a copy of \(M_2\). Their map \(\rho\) on \(M_2\) has the unit \(d=1-a\), where the *defect* \(a\) is a cut-down of \(c\). The comparison moves the defect, through an element \(v\), under \(s_1\), and two copies \(r_1,r_2\) of the defect appear inside the range of \(\rho\) (Lemma 3.1). The defect and its two copies give three orthogonal positions of an \(M_3\), hence a map \(\alpha\) on \(M_3\); the map \(\beta\) on \(M_2\) is \(\rho\) cut down to the rest \(1-\alpha(1)\). A path of unitaries from \(1\) to the flip of \(M_2\otimes M_2\), applied where both maps are partly present, makes their ranges commute (Lemma 5.4).

## 2. Exact relations

Fix the data of Proposition 1.1. We may assume \(0<\varepsilon<1\). Indeed, for \(0<\varepsilon'<\varepsilon\), the element \(b=(a_1-\varepsilon')_+\) satisfies \((b-(\varepsilon-\varepsilon'))_+=(a_1-\varepsilon)_+\). With the continuous function \(k\) given by \(k(t)=(t-\varepsilon+\varepsilon')_+/t\) for \(t>0\) and \(k(0)=0\), the element \(x=k(b)^{1/2}\) satisfies \(x^*bx=(a_1-\varepsilon)_+\). So \(c\precsim(a_1-\varepsilon')_+\) by Lemma 1.2(1) of [Cuntz comparison and order-zero maps](cuntz-comparison-and-order-zero-maps.md).

Define continuous functions on \([0,\infty)\) by
\[
\begin{gathered}
f(t)=\min\{t/\varepsilon,1\},\\
q(t)=\varepsilon^{-1/2}\ (t\le\varepsilon),\\
q(t)=t^{-1/2}\ (t\ge\varepsilon).
\end{gathered}
\]
Then \(f(0)=0\), \(f=1\) on \([\varepsilon,\infty)\), and \(tq(t)^2=f(t)\) for all \(t\ge0\).

**Lemma 2.1** (intertwining). For every continuous function \(r\) on \([0,1]\),
\[
\begin{gathered}
w^*r(a_2)=r(a_1)w^*,\\
wr(a_1)=r(a_2)w,\\
w^*r(a_1)=r(0)w^*,\\
wr(a_2)=r(0)w.
\end{gathered}
\]

*Proof.* \(w^*a_2=w^*ww^*=a_1w^*\), so \(w^*P(a_2)=P(a_1)w^*\) for polynomials \(P\), and for continuous \(r\) by uniform approximation on \([0,1]\), which contains both spectra. The second identity is the adjoint of the first, applied to \(\bar r\). Next, \(\|w^*a_1\|^2=\|a_1ww^*a_1\|=\|a_1a_2a_1\|=0\), so \(w^*a_1=0\) and \(w^*P(a_1)=P(0)w^*\) for polynomials. Similarly \(\|wa_2\|^2=\|a_2w^*wa_2\|=\|a_2a_1a_2\|=0\). Approximate again. \(\blacksquare\)

**Lemma 2.2** (exact relations). Put
\[
\begin{gathered}
s_1=f(a_1)^{1/2},\qquad s_2=w^*q(a_2),\\
d=f(a_1)+f(a_2),\qquad a=1-d.
\end{gathered}
\]
Then:

1. \(s_is_j^*=\delta_{ij}f(a_1)\) for \(i,j\in\{1,2\}\), and \(s_1^*s_1+s_2^*s_2=d\);
2. \(0\le d\le1\) and \(a=\varepsilon^{-1}(c-(1-\varepsilon))_+\);
3. \(s_id=ds_i=f(a_1)s_i\) for \(i=1,2\); hence \(d\) and \(a\) commute with \(s_1,s_2,s_1^*,s_2^*\);
4. there is \(v\in B\) with \(v^*v=a\), \(s_1v=v\), \(s_2v=0\), \(dv=v\) and \(av=0\).

*Proof.* By Lemma 2.1, \(s_2=q(a_1)w^*\) and \(s_2^*=wq(a_1)\).

(1) \(s_1s_1^*=f(a_1)\) and \(s_2s_2^*=q(a_1)w^*wq(a_1)\), which is \(q(a_1)a_1q(a_1)=f(a_1)\). Next, \(f(a_1)^{1/2}w=(w^*f(a_1)^{1/2})^*=0\) by Lemma 2.1, since \(f^{1/2}\) vanishes at \(0\); so \(s_1s_2^*=f(a_1)^{1/2}wq(a_1)=0\), and \(s_2s_1^*=(s_1s_2^*)^*=0\). Finally \(s_1^*s_1=f(a_1)\) and
\[
\begin{aligned}
s_2^*s_2&=wq(a_1)^2w^*\\
&=q(a_2)^2ww^*=f(a_2).
\end{aligned}
\]

(2) Compute pointwise in \(C^*(1,a_1,a_2)\). Where \(a_2=0\), \(d=f(a_1)\le1\), and
\[
\begin{aligned}
1-d&=\varepsilon^{-1}(\varepsilon-a_1)_+\\
&=\varepsilon^{-1}(c-(1-\varepsilon))_+,
\end{aligned}
\]
since \(c=1-a_1\) there. The points where \(a_1=0\) are treated symmetrically.

(3) \(f(a_1)^{1/2}f(a_2)=0\), since both functions vanish at \(0\); so \(s_1d=ds_1=f(a_1)s_1\). For \(s_2\): by Lemma 2.1, \(f(a_2)w^*=(wf(a_2))^*=0\) and \(w^*f(a_1)=0\). Hence \(ds_2=f(a_1)s_2\), and, since the first term below vanishes,
\[
\begin{aligned}
s_2d&=q(a_1)w^*f(a_1)+w^*q(a_2)f(a_2)\\
&=w^*f(a_2)q(a_2)=f(a_1)w^*q(a_2)\\
&=f(a_1)s_2 .
\end{aligned}
\]
Taking adjoints, \(d\) commutes with \(s_i^*\) as well, and so does \(a=1-d\).

(4) Apply the exact cut ([Cuntz comparison and order-zero maps](cuntz-comparison-and-order-zero-maps.md), Lemma 2.1) to \(c\precsim(a_1-\varepsilon)_+\) with \(\delta=1-\varepsilon\). It gives \(z\in B\) with \(zz^*\in\operatorname{Her}((a_1-\varepsilon)_+)\) and
\[
z^*z=(c-(1-\varepsilon))_+=\varepsilon a .
\]
Put \(v=\varepsilon^{-1/2}z\), so \(v^*v=a\). As \(f^{1/2}=1\) on \([\varepsilon,\infty)\), \(s_1(a_1-\varepsilon)_+^{1/2}=(a_1-\varepsilon)_+^{1/2}\); hence \(s_1y=y\) for all \(y\in\operatorname{Her}((a_1-\varepsilon)_+)\), and in particular \(s_1vv^*=vv^*\). Then \((1-s_1)vv^*(1-s_1)=0\), so \((1-s_1)v=0\). Next \(s_2v=s_2s_1^*v=0\) by (1), \(dv=s_1^2v+s_2^*s_2v=v\), and \(av=0\). \(\blacksquare\)

**Lemma 2.3** (the map \(\rho\)). The family \((s_1,s_2)\) satisfies the hypotheses of Lemma 3.1 of [Cuntz comparison and order-zero maps](cuntz-comparison-and-order-zero-maps.md) with \(h=f(a_1)\). Its Gram map \(\rho\colon M_2\to B\), \(\rho(e_{ij})=s_i^*s_j\), has \(\rho(1_2)=d\), and its supporting homomorphism \(\sigma\colon M_2\to B^{**}\) satisfies
\[
\begin{gathered}
\rho(x)=d\sigma(x)=\sigma(x)d,\\
\sigma(1_2)=p:=s(d).
\end{gathered}
\]
Every continuous function of \(d\) commutes with \(\sigma(M_2)\) and with \(p\), and \((1-p)g(d)=g(0)(1-p)\) for every \(g\in C([0,1])\).

*Proof.* \(\|s_i\|^2=\|s_is_i^*\|=\|f(a_1)\|\le1\), and Lemma 2.2(1) gives the relations \(s_is_j^*=\delta_{ij}f(a_1)\). Lemma 3.1 of the previous lesson gives \(\rho\), \(\sigma\) and the displayed identities, with \(\rho(1_2)=s_1^*s_1+s_2^*s_2=d\). So \(d\) commutes with \(\sigma(M_2)\), and so do polynomials in \(d\) and their norm limits; \(p\) commutes with them as a strong limit of functions of \(d\). Since \(p\) is the projection onto the closure of the range of \(d\), \((1-p)d=0\), so \((1-p)P(d)=P(0)(1-p)\) for polynomials \(P\), and the last claim follows by approximation. \(\blacksquare\)

## 3. Two orthogonal copies of the defect

Let \(v=ua^{1/2}\) be the polar decomposition of \(v\) in \(B^{**}\), so \(|v|=(v^*v)^{1/2}=a^{1/2}\), and put \(e=u^*u=s(a)\).

**Lemma 3.1.** Put \(r_i=s_i^*u\in B^{**}\) for \(i=1,2\) and \(R=r_1r_1^*+r_2r_2^*\). Then:

1. \(u=ue\), \(s_1u=du=u\) and \(au=eu=0\); \(e\) commutes with \(s_i\), \(s_i^*\), \(d\) and \(\sigma(M_2)\);
2. \(r_i=\sigma(e_{i1})u\) and \(\sigma(e_{jk})r_i=\delta_{ki}r_j\);
3. \(r_i^*r_j=\delta_{ij}e\), \(r_ie=r_i\), \(dr_i=pr_i=r_i\) and \(er_i=0\);
4. \(R\) is a projection with \(R\le p\) and \(Re=eR=0\), and \(R\) commutes with \(\sigma(M_2)\).

*Proof.* (1) \(u=ue\) holds for the partial isometry of a polar decomposition. From \(s_1v=v\), \((s_1u-u)a^{1/2}=0\), so \(s_1u-u\) vanishes on the range of \(a^{1/2}\), which is dense in the range of \(e\); with \(u=ue\) this gives \(s_1u=u\). In the same way \(dv=v\) and \(av=0\) give \(du=u\) and \(au=0\). As \(e\) is the strong limit of \(a(a+\tau)^{-1}\), \(eu=0\), and \(e\) commutes with every element commuting with \(a\): with \(s_i,s_i^*\) (Lemma 2.2(3)), with \(d\), and with \(\sigma(M_2)\) (Lemma 2.3).

(2) By (1) and Lemma 2.3, \(r_i=s_i^*s_1u=\rho(e_{i1})u\), and this is \(\sigma(e_{i1})du=\sigma(e_{i1})u\). Then \(\sigma(e_{jk})r_i=\sigma(e_{jk}e_{i1})u=\delta_{ki}r_j\).

(3) \(r_i^*r_j=u^*s_is_j^*u=\delta_{ij}u^*s_1^2u\), which is \(\delta_{ij}u^*u=\delta_{ij}e\), and \(r_ie=s_i^*ue=r_i\). Next \(dr_i=s_i^*du=r_i\), and \((1-p)r_i=(1-p)dr_i=0\). Finally \(er_i=s_i^*eu=0\).

(4) By (3), \((r_ir_i^*)^2=r_ier_i^*=r_ir_i^*\), and \(r_1r_1^*r_2r_2^*=r_1(r_1^*r_2)r_2^*=0\); so \(R\) is a projection. \(pR=R\) by (3), so \(R\le p\). \(eR=\sum_ier_ir_i^*=0\) and \(Re=(eR)^*=0\). By (2),
\[
\begin{gathered}
\sigma(e_{jk})R=\sum_i\sigma(e_{jk})r_ir_i^*=r_jr_k^*,\\
R\sigma(e_{jk})=\sum_ir_i\bigl(\sigma(e_{kj})r_i\bigr)^*=r_jr_k^* .
\end{gathered}
\]
\(\blacksquare\)

**Lemma 3.2** (the copy map). Every \(b\in\operatorname{Her}(a)\) satisfies \(eb=be=b\), and \(ubu^*\) and \(ub\) belong to \(B\). The formula
\[
\varphi(b)=r_1br_1^*+r_2br_2^*
\]
defines a \(*\)-homomorphism \(\varphi\colon\operatorname{Her}(a)\to B\), and for \(b,b'\in\operatorname{Her}(a)\) and \(i=1,2\):

1. \(\varphi(b)r_i=r_ib\);
2. \(d\varphi(b)=\varphi(b)d=\varphi(b)\) and \(R\varphi(b)=\varphi(b)R=\varphi(b)\);
3. \(\varphi(b)\) commutes with \(\sigma(M_2)\);
4. \(\varphi(b)b'=b'\varphi(b)=0\).

*Proof.* \(ea^{1/2}=a^{1/2}=a^{1/2}e\), so \(eb=be=b\) for \(b\in a^{1/2}Ba^{1/2}\), and by continuity on \(\operatorname{Her}(a)\). For \(b=a^{1/2}b_0a^{1/2}\) with \(b_0\in B\), \(ubu^*=vb_0v^*\) and \(ub=vb_0a^{1/2}\) lie in \(B\); by continuity this holds on \(\operatorname{Her}(a)\). So \(\varphi(b)=\sum_is_i^*(ubu^*)s_i\in B\). The map \(\varphi\) is linear and preserves adjoints, and by Lemma 3.1(3)
\[
\begin{aligned}
\varphi(b)\varphi(b')&=\sum_{i,j}r_ibr_i^*r_jb'r_j^*\\
&=\sum_ir_ibeb'r_i^*=\varphi(bb').
\end{aligned}
\]
(1) \(\varphi(b)r_i=\sum_jr_jbr_j^*r_i=r_ibe=r_ib\). (2) \(dr_i=r_i\) gives \(d\varphi(b)=\varphi(b)\), and \(\varphi(b)d=(d\varphi(b^*))^*=\varphi(b)\). \(Rr_i=\sum_jr_jr_j^*r_i=r_ie=r_i\) gives \(R\varphi(b)=\varphi(b)\), and \(\varphi(b)R=(R\varphi(b^*))^*=\varphi(b)\). (3) By Lemma 3.1(2), \(\sigma(e_{jk})\varphi(b)=r_jbr_k^*\) and \(\varphi(b)\sigma(e_{jk})=\sum_ir_ib(\sigma(e_{kj})r_i)^*=r_jbr_k^*\). (4) \(r_i^*b'=r_i^*eb'=(er_i)^*b'=0\), so \(\varphi(b)b'=0\), and \(b'\varphi(b)=(\varphi(b^*)b'^*)^*=0\). \(\blacksquare\)

## 4. Section algebras and a unitary in the bidual

Let
\[
\begin{aligned}
D_1=\{F\in{}&C([0,1],M_2):\\
&F(0)\in\mathbb C1_2,\ F(1)=0\},
\end{aligned}
\]
and write \(F(0)=c_F1_2\). For \(f\in C([0,1])\) and \(x\in M_2\), \(fx\) denotes the section \(t\mapsto f(t)x\).

**Lemma 4.1** (the map \(\lambda\)). The formula
\[
\lambda(F)=\sum_{i,j}F_{ij}(d)\sigma(e_{ij})+c_F(1-p)
\]
defines a \(*\)-homomorphism \(\lambda\colon D_1\to\operatorname{Her}(a)\). If \(f\in C([0,1])\) and \(f(1)=0\), then \(\lambda(f1_2)=f(d)\); if moreover \(f(0)=0\), then \(\lambda(fx)=f(d)\sigma(x)\) for \(x\in M_2\).

*Proof.* \(g\mapsto g(d)\) is a \(*\)-homomorphism \(C([0,1])\to B\), since the spectrum of \(d\) lies in \([0,1]\), and its range commutes with \(\sigma(M_2)\) (Lemma 2.3). Hence \(\bar\lambda(F)=\sum_{i,j}F_{ij}(d)\sigma(e_{ij})\) defines a \(*\)-homomorphism \(\bar\lambda\colon C([0,1],M_2)\to B^{**}\):
\[
\begin{aligned}
\bar\lambda(F)\bar\lambda(G)&=\sum_{i,j,l}(F_{ij}G_{jl})(d)\sigma(e_{il})\\
&=\bar\lambda(FG),
\end{aligned}
\]
and \(\bar\lambda(F)^*=\bar\lambda(F^*)\). Since \(\sigma(e_{ij})=p\sigma(e_{ij})p\) and \(p\) commutes with functions of \(d\), \(\bar\lambda(F)=p\bar\lambda(F)p\). As \(F\mapsto c_F\) is a character of \(D_1\), the cross terms vanish, and \(\lambda\) is a \(*\)-homomorphism. If \(f(1)=0\), then \(\lambda(f1_2)=f(d)p+f(0)(1-p)=f(d)\) by Lemma 2.3. If also \(f(0)=0\), then \(\lambda(fx)=\sum_{i,j}x_{ij}f(d)\sigma(e_{ij})=f(d)\sigma(x)\).

It remains to see \(\lambda(D_1)\subseteq\operatorname{Her}(a)\). The C\*-algebra \(G\) generated by \((1-t)1_2\) and the sections \(t(1-t)x\), \(x\in M_2\), is \(D_1\). Indeed, \(G\) contains \(P(1-t)1_2\) for polynomials \(P\) with \(P(0)=0\), hence, by the Weierstrass theorem, \(f1_2\) for every \(f\in C([0,1])\) with \(f(1)=0\). It then contains the products \(f(t)\,t(1-t)x\). Every continuous function with compact support in \((0,1)\) has the form \(f(t)\,t(1-t)\) with such an \(f\), and these functions are uniformly dense among the continuous functions vanishing at \(0\) and \(1\). So \(G\) contains every section vanishing at both endpoints, and every \(F\in D_1\) is \(c_F(1-t)1_2\) plus such a section. Now
\[
\begin{aligned}
\lambda((1-t)1_2)&=1-d=a,\\
\lambda(t(1-t)x)&=d(1-d)\sigma(x)\\
&=a^{1/2}\rho(x)a^{1/2},
\end{aligned}
\]
because \(a\) commutes with \(\rho(x)=d\sigma(x)\). Both lie in \(\operatorname{Her}(a)\). Since \(\lambda\) is contractive and \(\operatorname{Her}(a)\) is a C\*-subalgebra, \(\lambda(D_1)\subseteq\operatorname{Her}(a)\). \(\blacksquare\)

Let
\[
\begin{aligned}
D_2=\{F\in{}&C([0,1],M_2\otimes M_2):\\
&F(0)\in\mathbb C1_4,\ F(1)=0\},
\end{aligned}
\]
and \(F(0)=c_F1_4\). Write \(F=\sum_{j,k}F_{jk}\otimes e_{jk}\) with \(F_{jk}\in C([0,1],M_2)\): the first tensor factor carries the values of sections of \(D_1\), and the second is a copy index. For \(F\in D_2\), every \(F_{jk}\) lies in \(D_1\), with \(c_{F_{jk}}=\delta_{jk}c_F\).

**Lemma 4.2** (the map \(\gamma\)). The formula
\[
\gamma(F)=\sum_{j,k}\varphi\bigl(\lambda(F_{jk})\bigr)\sigma(e_{jk})
\]
defines a \(*\)-homomorphism \(\gamma\colon D_2\to B\) with the following properties.

1. \(\gamma(F)=R\gamma(F)=\gamma(F)R\) for \(F\in D_2\).
2. \(\gamma(f1_4)=\varphi(f(d))\) for \(f\in C([0,1])\) with \(f(1)=0\).
3. For \(f\in C([0,1])\) with \(f(0)=f(1)=0\) and \(y\in M_2\), \(\gamma(f(1_2\otimes y))=\varphi(f(d))\sigma(y)\) and \(\gamma(f(y\otimes1_2))=\varphi(f(d)\sigma(y))\).
4. For \(g_n(t)=\min\{1,n(1-t)\}\), \(\gamma(g_n1_4)\to R\) strongly as \(n\to\infty\).

*Proof.* Write \(\kappa=\varphi\circ\lambda\colon D_1\to B\), a \(*\)-homomorphism whose range commutes with \(\sigma(M_2)\) (Lemma 3.2(3)). Then
\[
\begin{aligned}
&\gamma(F)\gamma(G)\\
&\quad=\sum_{j,k,l,m}\kappa(F_{jk})\kappa(G_{lm})\sigma(e_{jk}e_{lm})\\
&\quad=\sum_{j,k,m}\kappa(F_{jk}G_{km})\sigma(e_{jm})=\gamma(FG),
\end{aligned}
\]
since \((FG)_{jm}=\sum_kF_{jk}G_{km}\), and \(\gamma(F)^*=\sum_{j,k}\kappa(F_{jk}^*)\sigma(e_{kj})=\gamma(F^*)\), since \((F^*)_{kj}=F_{jk}^*\). By Lemma 3.2(2), \(\kappa(F_{jk})\sigma(e_{jk})=\kappa(F_{jk})d\sigma(e_{jk})\), which is \(\kappa(F_{jk})\rho(e_{jk})\in B\).

(1) follows from Lemma 3.2(2) and Lemma 3.1(4). (2) \(f1_4=\sum_jf1_2\otimes e_{jj}\), so \(\gamma(f1_4)=\varphi(f(d))p=\varphi(f(d))\), because \(\varphi(b)(1-p)=\varphi(b)d(1-p)=0\). (3) \(f(1_2\otimes y)=\sum_{j,k}y_{jk}f1_2\otimes e_{jk}\) gives \(\sum_{j,k}y_{jk}\varphi(f(d))\sigma(e_{jk})=\varphi(f(d))\sigma(y)\), and \(f(y\otimes1_2)=\sum_jfy\otimes e_{jj}\) gives \(\varphi(\lambda(fy))p=\varphi(f(d)\sigma(y))\) by Lemma 4.1.

(4) With \(m_n(t)=\min\{1,nt\}\), \(g_n(d)=m_n(1-d)=m_n(a)\), so \(\gamma(g_n1_4)=\varphi(m_n(a))=\sum_ir_im_n(a)r_i^*\) by (2). For \(t\ge0\), \(t/(t+1/n)\le m_n(t)\le1\), and \(m_n(0)=0\); so \(m_n(a)=m_n(a)e\le e\), and
\[
0\le e-m_n(a)\le e-a(a+1/n)^{-1},
\]
which tends to \(0\) strongly. For an operator \(0\le X\le1\), \(\|X\xi\|^2=\langle X^2\xi,\xi\rangle\le\langle X\xi,\xi\rangle\). Hence \(e-m_n(a)\to0\) strongly, and \(\gamma(g_n1_4)\to\sum_ir_ier_i^*=R\) strongly. \(\blacksquare\)

Let \(E\) be the set of \(F\in C([0,1],M_2\otimes M_2)\) with \(F(0)\in\mathbb C1_4\). It is a unital C\*-algebra, and \(D_2\) is a closed two-sided ideal of \(E\) (Exercise 6.5).

**Lemma 4.3** (a unitary in the bidual). For every unitary \(U\in E\) there is a unitary \(W\in B^{**}\) with \(W(1-R)=(1-R)W=1-R\) and, for \(F\in D_2\),
\[
\begin{gathered}
W\gamma(F)=\gamma(UF),\quad\gamma(F)W=\gamma(FU),\\
W^*\gamma(F)=\gamma(U^*F),\\
\gamma(F)W^*=\gamma(FU^*).
\end{gathered}
\]

*Proof.* Put \(e_n=g_n1_4\in D_2\) with \(g_n\) as in Lemma 4.2(4). For \(F\in D_2\), \(g_n=1\) on \([0,1-1/n]\) and \(F(1)=0\), so
\[
\|e_nF-F\|\le\sup_{t\ge1-1/n}\|F(t)\|\longrightarrow0 .
\]
Hence \(\gamma(Ue_n)\gamma(F)\xi=\gamma(Ue_nF)\xi\to\gamma(UF)\xi\) for \(\xi\in H_u\). Also \(\gamma(Ue_n)(1-R)=0\) by Lemma 4.2(1). The vectors \(\gamma(F)\xi\) and \((1-R)\xi\) span a dense subspace of \(H_u\), because \(R\xi=\lim_n\gamma(e_n)\xi\) (Lemma 4.2(4)). The operators \(\gamma(Ue_n)\) have norm at most \(1\) and converge on this dense subspace; so they converge strongly: if \(\|\zeta-\zeta'\|<\eta\) with \(\zeta'\) in the subspace, then
\[
\begin{aligned}
&\|\gamma(Ue_n)\zeta-\gamma(Ue_m)\zeta\|\\
&\quad\le2\eta+\|\gamma(Ue_n)\zeta'-\gamma(Ue_m)\zeta'\| .
\end{aligned}
\]
The strong limit \(w_0\) lies in \(B^{**}\).

By construction \(w_0\gamma(F)=\gamma(UF)\) and \(w_0=Rw_0=w_0R\). For \(\zeta=\sum_k\gamma(F_k)\xi_k\),
\[
\begin{aligned}
\|w_0\zeta\|^2&=\sum_{k,l}\langle\gamma(F_l^*U^*UF_k)\xi_k,\xi_l\rangle\\
&=\|\zeta\|^2 .
\end{aligned}
\]
These vectors are dense in \(RH_u\), so \(w_0\) is isometric on \(RH_u\), and \(w_0^*w_0=R\). The range of \(w_0\) contains \(\gamma(UF)\xi\) for all \(F\in D_2\), hence all \(\gamma(F')\xi\), since \(F'=U(U^*F')\) with \(U^*F'\in D_2\). As the range of the isometry \(w_0|_{RH_u}\) is closed, it is \(RH_u\), and \(w_0w_0^*=R\). So \(W=w_0+1-R\) is unitary, because \(w_0^*(1-R)=0=(1-R)w_0\). Then \(W\gamma(F)=w_0\gamma(F)=\gamma(UF)\). Applying \(w_0^*\) to \(w_0\gamma(U^*F)=\gamma(F)\) gives \(\gamma(U^*F)=w_0^*\gamma(F)=W^*\gamma(F)\), because \((1-R)\gamma(F)=0\). The other two identities are the adjoints of these two, applied to \(F^*\). \(\blacksquare\)

## 5. The weighted flip and the proof

Let \(S\in M_2\otimes M_2\) be the flip, \(S(\xi\otimes\eta)=\eta\otimes\xi\); it is a self-adjoint unitary with \(S(x\otimes y)S=y\otimes x\). Choose a continuous \(\theta\colon[0,1]\to[0,1]\) with \(\theta=0\) on \([0,1/3]\) and \(\theta=1\) on \([2/3,1]\), and put
\[
U(t)=\tfrac12(1+S)+e^{i\pi\theta(t)}\tfrac12(1-S).
\]
As \(\frac12(1\pm S)\) are complementary projections, each \(U(t)\) is unitary; \(U(t)=1\) for \(t\le1/3\) and \(U(t)=S\) for \(t\ge2/3\). So \(U\) is a unitary of \(E\). From now on \(W\) is the unitary of Lemma 4.3 for this \(U\), and \(W=w_0+1-R\) as in its proof.

Let \(g(t)=1\) for \(0\le t\le2/3\) and \(g(t)=3(1-t)\) for \(2/3\le t\le1\), and put
\[
\begin{gathered}
h=g(d),\qquad k=\varphi(h),\\
l=1-h-k .
\end{gathered}
\]
Since \(g(1)=0\), \(h=\lambda(g1_2)\in\operatorname{Her}(a)\) (Lemma 4.1), so \(k\) is defined.

**Lemma 5.1.**

1. \(h,k,l\) are positive elements of \(B\) with \(hk=kh=0\), \(h+k+l=1\) and \(l\le d\); they commute with \(d\) and with \(\sigma(M_2)\).
2. \(Rh=hR=0\), \(Wh^{1/2}=h^{1/2}\) and \(h^{1/2}r_i=0\) for \(i=1,2\).
3. \(kW=Wk\), and \(k^\beta W=\gamma(g^\beta U)\in B\) for every \(\beta>0\).
4. Let \(j(t)=\min\{1/t,3/2\}\) for \(t>0\) and \(j(0)=3/2\). Then \(l=lj(d)d\), \(lp=pl=l\), and \(l\sigma(y)=lj(d)\rho(y)\in B\) for \(y\in M_2\).

*Proof.* (1) \(h\) is a function of \(d\), \(k=\varphi(h)\ge0\), and \(hk=kh=0\) by Lemma 3.2(4). They commute with \(d\) and \(\sigma(M_2)\) by Lemma 2.3 and Lemma 3.2(2),(3). \(h\) and \(k\) are commuting orthogonal positive contractions (\(\varphi\) is contractive), so \(h+k\le1\), computed pointwise in the commutative C\*-algebra they generate; hence \(l\ge0\). As \(g(t)\ge1-t\) on \([0,1]\), \(h\ge1-d=a\), and \(l\le1-h\le1-a=d\).

(2) \(h\) and \(h^{1/2}\) lie in \(\operatorname{Her}(a)\), as \(g^{1/2}(1)=0\). So \(Rh^{1/2}=Reh^{1/2}=0\) by Lemma 3.2 and Lemma 3.1(4), and likewise \(Rh=0\) and \(hR=(Rh)^*=0\). Hence \(Wh^{1/2}=w_0Rh^{1/2}+(1-R)h^{1/2}=h^{1/2}\). Since \(dr_i=r_i\), \(P(d)r_i=P(1)r_i\) for polynomials, hence for continuous functions, and \(h^{1/2}r_i=g(1)^{1/2}r_i=0\).

(3) By Lemma 4.2(2), \(\gamma(g1_4)=\varphi(g(d))=k\), and for \(\beta>0\), \(\gamma(g^\beta1_4)=\varphi(h^\beta)=\varphi(h)^\beta=k^\beta\). Since \(g^\beta U\in D_2\), Lemma 4.3 gives \(k^\beta W=\gamma(g^\beta1_4)W=\gamma(g^\beta U)\in B\). The scalar function \(g\) commutes with \(U\), so \(kW=\gamma(gU)=\gamma(Ug)=Wk\).

(4) The function \(m(t)=tj(t)=\min\{1,3t/2\}\) is continuous, \(m(0)=0\), and \(m=1\) on \([2/3,1]\). Now \((1-h)(1-m(d))\) is \(((1-g)(1-m))(d)=0\), since \(1-g\) vanishes on \([0,2/3]\) and \(1-m\) on \([2/3,1]\). Also \(k(1-m(d))=(1-m(1))k=0\), because \(kd=k\) (Lemma 3.2(2)) gives \(kP(d)=P(1)k\). So \(l(1-m(d))=0\), that is, \(l=lm(d)=lj(d)d\). Since \(m(0)=0\), \(m(d)p=m(d)\) by Lemma 2.3, so \(lp=l\), and \(pl=(lp)^*=l\). Finally \(l\sigma(y)=lj(d)d\sigma(y)=lj(d)\rho(y)\). \(\blacksquare\)

Define
\[
\begin{gathered}
x_i=h^{1/2}r_i^*W\quad(i=1,2),\\
x_3=h^{1/2}.
\end{gathered}
\]

**Lemma 5.2** (the map \(\alpha\)). \(x_1,x_2,x_3\) are contractions in \(B\) with \(x_ix_j^*=\delta_{ij}h\). Their Gram map \(\alpha\colon M_3\to B\), \(\alpha(e_{ij})=x_i^*x_j\), satisfies \(\alpha(1_3)=h+k\), and for \(i=1,2\)
\[
C_i:=\alpha(e_{i3})=W^*r_ih=kW^*r_i .
\]

*Proof.* By Lemma 3.2(1), \(r_ib=\varphi(b)r_i\) for \(b\in\operatorname{Her}(a)\); with \(b=h^{1/2}\) and \(b=h^{1/4}\) this gives \(r_ih^{1/2}=k^{1/2}r_i\) and \(r_ih^{1/4}=k^{1/4}r_i\). So, for \(i=1,2\),
\[
x_i=r_i^*k^{1/2}W=(r_i^*k^{1/4})(k^{1/4}W).
\]
Here \(r_i^*k^{1/4}=(r_ih^{1/4})^*=(s_i^*uh^{1/4})^*\) lies in \(B\) by Lemma 3.2, and \(k^{1/4}W\in B\) by Lemma 5.1(3). So \(x_i\in B\). For \(i,j\le2\), \(x_ix_j^*=h^{1/2}r_i^*WW^*r_jh^{1/2}\), which is \(\delta_{ij}h^{1/2}eh^{1/2}=\delta_{ij}h\). For \(i\le2\), by Lemma 5.1(2),
\[
\begin{aligned}
x_ix_3^*&=h^{1/2}r_i^*Wh^{1/2}\\
&=h^{1/2}\bigl(h^{1/2}r_i\bigr)^*=0 .
\end{aligned}
\]
Also \(x_3x_3^*=h\), and \(\|x_i\|^2=\|x_ix_i^*\|=\|h\|\le1\). So Lemma 3.1 of [Cuntz comparison and order-zero maps](cuntz-comparison-and-order-zero-maps.md) applies, and
\[
\begin{aligned}
\alpha(1_3)&=\sum_{i\le2}W^*r_ihr_i^*W+h\\
&=W^*kW+h=k+h
\end{aligned}
\]
by Lemma 5.1(3). Finally \(C_i=x_i^*x_3=W^*r_ih=W^*kr_i=kW^*r_i\), since \(W^*k=kW^*\). \(\blacksquare\)

**Lemma 5.3** (the map \(\beta\)). The formula \(\beta(y)=l\sigma(y)\) defines a linear map \(\beta\colon M_2\to B\) preserving adjoints, with \(\beta(1_2)=l\), \(\beta(x)\beta(y)=\beta(1_2)\beta(xy)\), and \(\alpha(1_3)+\beta(1_2)=1_B\).

*Proof.* \(\beta(y)\in B\) by Lemma 5.1(4). As \(l\) is self-adjoint and commutes with \(\sigma(M_2)\), \(\beta(y)^*=\beta(y^*)\). Next \(\beta(1_2)=lp=l\), and \(\beta(x)\beta(y)=l^2\sigma(xy)=\beta(1_2)\beta(xy)\). Finally \(\alpha(1_3)+\beta(1_2)=h+k+l=1\). \(\blacksquare\)

**Lemma 5.4** (the weighted flip). Let \(Q=g(1-g)\). Then \(Q(d)=h(1-h)\), and for \(y\in M_2\)
\[
\begin{aligned}
&k(1-k)\sigma(y)W^*\\
&\quad=W^*\varphi\bigl(Q(d)\sigma(y)\bigr).
\end{aligned}
\]

*Proof.* \(Q\) vanishes on \([0,2/3]\), where \(g=1\), and at \(1\), where \(g=0\); on \([2/3,1]\), \(U(t)=S\). Since \(S(1\otimes y)S=y\otimes1\) and \(S=S^*\),
for \(0\le t\le1\)
\[
\begin{aligned}
&Q(t)(1\otimes y)U(t)^*\\
&\quad=U(t)^*Q(t)(y\otimes1),
\end{aligned}
\]
and both sides are elements of \(D_2\). Apply \(\gamma\). By Lemma 4.3 and Lemma 4.2(3), the left side gives \(\gamma(Q(1\otimes y))W^*=\varphi(Q(d))\sigma(y)W^*\), and the right side gives \(W^*\gamma(Q(y\otimes1))=W^*\varphi(Q(d)\sigma(y))\). Finally \(Q(d)=h-h^2\) and \(\varphi(Q(d))=k-k^2\). \(\blacksquare\)

*Proof of Proposition 1.1.* The maps \(\alpha\) and \(\beta\) preserve adjoints, \(\alpha(1_3)\) and \(\beta(1_2)\) are positive with sum \(1_B\), and both satisfy \(\psi(x)\psi(y)=\psi(1)\psi(xy)\) (Lemma 3.1(3) of the previous lesson and Lemma 5.3). It remains to show that their ranges commute. For \(y\in M_2\) and \(i=1,2\), Lemmas 5.1, 5.2, 5.4 and 3.2(1) give
\[
\begin{aligned}
\beta(y)C_i&=l\sigma(y)kW^*r_i\\
&=(k-k^2)\sigma(y)W^*r_i\\
&=W^*\varphi\bigl(Q(d)\sigma(y)\bigr)r_i\\
&=W^*r_iQ(d)\sigma(y)\\
&=W^*r_ih(1-h-k)\sigma(y)\\
&=C_i\beta(y).
\end{aligned}
\]
In the second line, \(l\) and \(k\) commute with \(\sigma(y)\) and \(lk=k-hk-k^2=k-k^2\); the fourth line uses \(Q(d)\sigma(y)=\lambda(Qy)\in\operatorname{Her}(a)\) (Lemma 4.1); the fifth uses \(hk=0\). Replacing \(y\) by \(y^*\) and taking adjoints gives \(C_i^*\beta(y)=\beta(y)C_i^*\). So \(\beta(M_2)\) commutes with the unital C\*-algebra \(\mathcal C\) generated by \(C_1,C_2\).

\(\mathcal C\) contains \(\alpha(M_3)\). Indeed, \(C_1^*C_1=hr_1^*WW^*r_1h=heh=h^2\), so \(\alpha(e_{33})=x_3^*x_3=h\in\mathcal C\). For \(i=1,2\), \(\alpha(e_{ii})=W^*r_ihr_i^*W\ge0\) and
\[
\begin{aligned}
\alpha(e_{ii})^2&=W^*r_iheh\,r_i^*W\\
&=W^*r_ih^2r_i^*W=C_iC_i^*,
\end{aligned}
\]
so \(\alpha(e_{ii})\in\mathcal C\) and \(A_0:=\alpha(1_3)\in\mathcal C\). Also \(\alpha(e_{i3})=C_i\) and \(\alpha(e_{3i})=C_i^*\). For \(i,j\le2\), \(C_iC_j^*=\alpha(e_{i3})\alpha(e_{3j})=A_0\alpha(e_{ij})\) by Lemma 3.1(3) of the previous lesson. Its supporting homomorphism \(\bar\alpha\) gives \(\alpha(e_{ij})=A_0\bar\alpha(e_{ij})\), so for \(\tau>0\)
\[
\begin{aligned}
&\bigl\|\alpha(e_{ij})-(A_0+\tau)^{-1}C_iC_j^*\bigr\|\\
&\quad=\bigl\|\tau(A_0+\tau)^{-1}A_0\bar\alpha(e_{ij})\bigr\|\le\tau ,
\end{aligned}
\]
and \((A_0+\tau)^{-1}C_iC_j^*\in\mathcal C\). Hence \(\alpha(e_{ij})\in\mathcal C\). So the ranges of \(\alpha\) and \(\beta\) commute, and Lemma 4.1 of [Cuntz comparison and order-zero maps](cuntz-comparison-and-order-zero-maps.md) gives a unital \(*\)-homomorphism \(I(2,3)\to B\). \(\blacksquare\)

## 6. Exercises

**6.1.** In \(B=M_5\), let \(w=e_{31}+e_{42}\), \(a_1=w^*w\) and \(a_2=ww^*\). Verify the hypothesis of Proposition 1.1 with \(\varepsilon=1/2\), and write down a unital \(*\)-homomorphism \(I(2,3)\to M_5\) directly.

**6.2.** Show that the hypothesis of Proposition 1.1 never holds in \(B=\mathbb C\), and explain why this is consistent with the conclusion.

**6.3.** Follow the proof when \(a_1+a_2=1_B\). Show that \(v=0\), \(R=0\), \(W=1\), \(h=k=0\), \(l=1\), \(\alpha=0\), and that \(\beta=\sigma\) is a unital \(*\)-homomorphism \(M_2\to B\).

**6.4.** Why can Section 5 not use the constant function \(U=S\) in place of the path \(U(t)\)?

**6.5.** Show that \(E\) is a unital C\*-algebra and that \(D_2\) is a closed two-sided ideal of \(E\).

## 7. Solutions

**6.1.** \(a_1=e_{11}+e_{22}\) and \(a_2=e_{33}+e_{44}\) are orthogonal projections, \(c=e_{55}\) and \((a_1-1/2)_+=\frac12(e_{11}+e_{22})\). The element \(x=\sqrt2\,e_{15}\) gives \(x^*(a_1-1/2)_+x=e_{55}\). A homomorphism: write \(F(0)=X\otimes1_3\) and \(F(1)=1_2\otimes Y\); then \(F\mapsto\operatorname{diag}(X,Y)\) is a unital \(*\)-homomorphism \(I(2,3)\to M_2\oplus M_3\subseteq M_5\).

**6.2.** In \(\mathbb C\), \(a_1a_2=|w|^4=0\) forces \(w=0\), so \(a_1=a_2=0\), \(c=1\) and \((a_1-\varepsilon)_+=0\); but \(x^*0x=0\) cannot approximate \(1\). The conclusion would compose with the identity character of \(\mathbb C\) to give a character of \(I(2,3)\), which has none (Lemma 4.1 of [Central sequences and the character criterion](central-sequences-and-the-character-criterion.md)).

**6.3.** \(c=0\) gives \(a=\varepsilon^{-1}(c-(1-\varepsilon))_+=0\), so \(v=0\), \(d=1\), \(p=1\), \(e=0\), \(u=0\), \(r_i=0\), \(R=0\) and \(\operatorname{Her}(a)=0\). Then \(\gamma=0\), \(w_0=0\) and \(W=1\); \(h=g(1)=0\), \(k=0\), \(l=1\), all \(x_i=0\), so \(\alpha=0\), and \(\beta(y)=\sigma(y)\) with \(\sigma(1_2)=p=1\).

**6.4.** \(S\) is not a scalar matrix, so for \(F\in D_2\) with \(c_F\ne0\) the value \((SF)(0)=c_FS\) is not in \(\mathbb C1_4\): \(SF\notin D_2\), and \(\gamma(SF)\) is not defined. Lemma 4.3 needs a unitary of \(E\); the path starts at the scalar \(1\) and reaches \(S\) only on \([2/3,1]\), where the weight \(Q\) lives.

**6.5.** \(E\) is closed in \(C([0,1],M_4)\) under sums, products, adjoints and uniform limits, and contains \(1\). For \(G\in E\) and \(F\in D_2\), \((GF)(0)=G(0)F(0)\in\mathbb C1_4\) and \((GF)(1)=0\), and similarly for \(FG\); \(D_2\) is closed under uniform limits.

## References

- [OpenAI-KRC] OpenAI, *The Kirchberg–Rørdam character criterion*, OpenAI Math Release preprint, 25 September 2026, Proposition 2.1 and Section 3. https://github.com/openai/math/tree/main/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026
- [RW] M. Rørdam and W. Winter, *The Jiang–Su algebra revisited*, author manuscript, 27 January 2009, Proposition 5.1. https://web.math.ku.dk/~rordam/manus/jiang-su-revisited.pdf
