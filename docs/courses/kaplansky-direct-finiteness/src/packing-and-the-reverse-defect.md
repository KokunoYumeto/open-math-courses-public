# Packing and the reverse defect

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the incidence criterion, Theorem 1.1 of [The glued group and planar balance](the-glued-group-and-planar-balance.md), from the identities of the two preceding lessons. The rectangular identity \(UT=I_m\) of [Subgroup averages and character twists](subgroup-averages-and-character-twists.md) is turned into square \(m\times m\) matrices \(a_{\rm mat}\), \(b_{\rm mat}\) with \(a_{\rm mat}b_{\rm mat}=I_m\), by packing the \(t\) intermediate coordinates into \(m\) slots with orthogonal character idempotents. The reverse product \(b_{\rm mat}a_{\rm mat}\) is shown to differ from \(I_m\) by a certificate: multiplied on both sides by the packing matrices, the defect becomes a matrix over the subgroup algebra \(K[H]\), and a character of \(H\) sends it to \(X^{\mathsf T}X-I_t\) up to a scalar factor, where \(X\) is the \(m\times t\) matrix of the vectors \(x_v\). Since \(t>m\), this is not zero. Finally a finite group supplies matrix units, which encode the two matrices as two elements of one group algebra.

- Packing into slots (Section 1).
- Square matrices with a one-sided inverse (Section 2).
- The reverse defect (Section 3).
- From matrices to two elements (Section 4).
- Finite presentation and the proof of the criterion (Section 5).

Notation is that of [Subgroup averages and character twists](subgroup-averages-and-character-twists.md): the glued group \(N\), the averages \(P_v\), the matrices \(U\), \(T\) and \(P=\operatorname{diag}(P_v)\) with \(UP=U\), \(PT=T\), \(UT=I_m\) (Proposition 2.1 there), the groups \(H=N\times\langle z\rangle\le L\) (Lemma 3.3), the central idempotent \(e\) (Lemma 4.1), the slots \(s(v)\) and forms \(\alpha_v\), and the twisted averages \(\tau_veP_v\tau_v^{-1}=eQ_{\alpha_v}\) (Lemma 4.3).

## 1. Packing into slots

Define \(C\in\operatorname{Mat}_{m\times t}(K[L])\) and \(J_0\in\operatorname{Mat}_{t\times m}(K[L])\) by
\[
\begin{gathered}
C_{s,v}=\begin{cases}\tau_veP_v,&s=s(v),\\0,&s\ne s(v),\end{cases}\\
(J_0)_{v,s}=\begin{cases}eP_v\tau_v^{-1},&s=s(v),\\0,&s\ne s(v).\end{cases}
\end{gathered}
\]

**Lemma 1.1.** \(J_0C=eP\).

*Proof.* The entry \((v,w)\) of \(J_0C\) is \(eP_v\tau_v^{-1}\tau_weP_w\) if \(s(v)=s(w)\) and zero otherwise. For \(v=w\) it is \(e^2P_v^2=eP_v\), since \(e\) is a central idempotent. For \(v\ne w\) in the same slot, Lemma 4.3 of the previous lesson gives
\[
\begin{aligned}
eP_v\tau_v^{-1}\tau_weP_w&=\tau_v^{-1}\bigl(eQ_{\alpha_v}\bigr)\bigl(eQ_{\alpha_w}\bigr)\tau_w\\
&=0 ,
\end{aligned}
\]
because \(\alpha_v\ne\alpha_w\) and \(Q_{\alpha_v}Q_{\alpha_w}=0\) (Lemma 4.2 there). \(\square\)

## 2. Square matrices with a one-sided inverse

Put
\[
\begin{aligned}
a_{\rm mat}&=UJ_0+(1-e)I_m,\\
b_{\rm mat}&=CT+(1-e)I_m ,
\end{aligned}
\]
\(m\times m\) matrices over \(K[L]\). Every entry of \(C\) and of \(J_0\) contains the central idempotent \(e\) as a factor, so
\[
(1-e)C=0,\qquad J_0(1-e)=0 ,
\]
and the same holds with \(1-e\) on the other side, because it is central.

**Proposition 2.1.** \(a_{\rm mat}b_{\rm mat}=I_m\).

*Proof.* The cross terms vanish: \(UJ_0(1-e)=0\) and \((1-e)CT=0\). By Lemma 1.1 and \(PT=T\),
\[
\begin{aligned}
a_{\rm mat}b_{\rm mat}&=U(J_0C)T+(1-e)^2I_m\\
&=eUPT+(1-e)I_m\\
&=eUT+(1-e)I_m ,
\end{aligned}
\]
which is \(eI_m+(1-e)I_m=I_m\) by \(UT=I_m\). \(\square\)

## 3. The reverse defect

Put \(\Delta=b_{\rm mat}a_{\rm mat}-I_m\). The same vanishing of cross terms gives
\[
\begin{aligned}
\Delta&=CTUJ_0+(1-e)I_m-I_m\\
&=CTUJ_0-eI_m .
\end{aligned}
\]

**Lemma 3.1** (the sandwich). \(J_0\Delta C=e(TU-P)\), a \(t\times t\) matrix with entries in \(K[H]\).

*Proof.* By Lemma 1.1, \(J_0\Delta C=(J_0C)TU(J_0C)-eJ_0C\), and this is \((eP)TU(eP)-e^2P\). Since \(e\) is central, this is \(e(PT)(UP)-eP=e(TU-P)\). The entries of \(T\), \(U\) and \(P\) lie in \(K[N]\) and \(e\) lies in \(K[\langle z\rangle]\), so all entries lie in \(K[H]\). \(\square\)

The order of the factors matters here: \(P\) is absorbed into \(T\) on the left and into \(U\) on the right.

Since \(H=N\times\langle z\rangle\), there is a homomorphism of groups \(H\to K^\times\), \(nz^r\mapsto\zeta^r\) for \(n\in N\), and it extends linearly to a homomorphism of \(K\)-algebras
\[
\varepsilon:K[H]\to K,\qquad\varepsilon(nz^r)=\zeta^r .
\]
It is applied only to \(K[H]\); no extension to \(K[L]\) is claimed or needed.

**Proposition 3.2.** \(\Delta\ne0\).

*Proof.* We compute \(\varepsilon\) on the entries of Lemma 3.1. First \(\varepsilon(e)=\ell^{-1}\sum_r\zeta^{-r}\zeta^r=1\) and \(\varepsilon(P_v)=\kappa^{-1}\kappa=1\). Let \(X\in\operatorname{Mat}_{m\times t}(K)\) be the matrix with columns \(x_v\). Then
\[
\begin{gathered}
\varepsilon(U)=-\kappa X,\quad\varepsilon(T)=X^{\mathsf T},\\
\varepsilon(P)=I_t ,
\end{gathered}
\]
so
\[
\varepsilon\bigl(e(TU-P)\bigr)=-\kappa X^{\mathsf T}X-I_t .
\]
Since \(X\) has \(m<t\) rows, there is \(y\in K^t\), \(y\ne0\), with \(Xy=0\), and then \(\bigl(-\kappa X^{\mathsf T}X-I_t\bigr)y=-y\ne0\). So \(e(TU-P)\) is a nonzero matrix over \(K[H]\), hence over \(K[L]\) by Lemma 3.3 of the previous lesson. By Lemma 3.1, \(J_0\Delta C\ne0\), so \(\Delta\ne0\). \(\square\)

So \(a_{\rm mat}\) and \(b_{\rm mat}\) show that \(K[L]\) is not stably finite. The certificate uses only finite-field linear algebra on the vectors \(x_v\); in characteristic two, where \(\kappa=1\) and \(XX^{\mathsf T}=I_m\), a nonzero column of \(I_t-X^{\mathsf T}X\) is an explicit choice of \(y\) (Exercise 6.2).

## 4. From matrices to two elements

A counterexample to stable finiteness becomes a counterexample to direct finiteness after a product with a suitable finite group: this is the reduction of Dykema, Heister and Juschenko [Dykema–Heister–Juschenko, abstract]. Here it is carried out explicitly.

Let \(B=(\mathbb Z/\ell)^m\) and \(F=B\rtimes S_m\), where the symmetric group \(S_m\) permutes the coordinates: \(\sigma w\sigma^{-1}=\sigma\cdot w\) with \((\sigma\cdot w)_{\sigma(k)}=w_k\). For \(1\le i\le m\) put
\[
p_i=|B|^{-1}\sum_{w\in B}\zeta^{-w_i}w\in K[F] ,
\]
where \(|B|=\ell^m\) is odd, hence invertible in \(K\). No inverse of \(|S_m|\) is needed.

**Lemma 4.1.** The \(p_i\) are nonzero, pairwise orthogonal idempotents, and \(\sigma p_i\sigma^{-1}=p_{\sigma(i)}\) for \(\sigma\in S_m\).

*Proof.* The coefficient of \(w\) in \(p_ip_j\) is \(|B|^{-2}\zeta^{-w_j}\sum_{u\in B}\zeta^{u_j-u_i}\). If \(i=j\), the sum is \(|B|\), giving the coefficient of \(w\) in \(p_i\). If \(i\ne j\), the map \(u\mapsto\zeta^{u_j-u_i}\) is a nontrivial character of \(B\), and translating \(u\) by a vector \(u_0\) with \(\zeta^{u_{0,j}-u_{0,i}}\ne1\) shows that the sum is zero. The identity coefficient of \(p_i\) is \(|B|^{-1}\ne0\). Finally \(\sigma p_i\sigma^{-1}=|B|^{-1}\sum_w\zeta^{-w_i}\,\sigma\cdot w\), and substituting \(w'=\sigma\cdot w\), with \(w'_{\sigma(i)}=w_i\), gives \(p_{\sigma(i)}\). \(\square\)

Let \(\sigma_i\in S_m\) exchange the coordinates \(1\) and \(i\), with \(\sigma_1=1\), and put
\[
p_{ij}=\sigma_ip_1\sigma_j^{-1}\qquad(1\le i,j\le m).
\]

**Lemma 4.2** (matrix units). \(p_{ii}=p_i\), \(p_{ij}p_{kr}=\delta_{jk}\,p_{ir}\), and the \(m^2\) elements \(p_{ij}\) are linearly independent over \(K\).

*Proof.* \(p_{ii}=\sigma_ip_1\sigma_i^{-1}=p_i\) by Lemma 4.1. Also \(p_ip_{ij}p_j=\sigma_ip_1^3\sigma_j^{-1}=p_{ij}\). If \(j\ne k\), then \(p_{ij}p_{kr}=p_{ij}p_jp_kp_{kr}=0\). If \(j=k\), then \(p_{ij}p_{jr}=\sigma_ip_1^2\sigma_r^{-1}=p_{ir}\). Each \(p_{ij}\) is nonzero, being a translate of \(p_1\) on both sides. If \(\sum c_{ij}p_{ij}=0\), multiplying by \(p_k\) on the left and \(p_l\) on the right leaves \(c_{kl}p_{kl}=0\), so \(c_{kl}=0\). \(\square\)

Let \(G=L\times F\). Then \(K[L]\) and \(K[F]\) are commuting subalgebras of \(K[G]\), and the basis \(G=\{(g,h)\}\) identifies \(K[G]\) with \(K[L]\otimes_KK[F]\). Define
\[
\begin{gathered}
f_{\rm blk}=\sum_{i=1}^mp_{ii},\\
\Phi:\operatorname{Mat}_m(K[L])\to K[G],\\
\Phi(Z)=\sum_{i,j}Z_{ij}\,p_{ij} .
\end{gathered}
\]

**Lemma 4.3.** \(\Phi\) is additive, multiplicative and injective, \(\Phi(I_m)=f_{\rm blk}\), and \(f_{\rm blk}\Phi(Z)=\Phi(Z)=\Phi(Z)f_{\rm blk}\).

*Proof.* Since the entries commute with the \(p_{ij}\), Lemma 4.2 gives \(\Phi(Z)\Phi(Z')=\sum Z_{ij}Z'_{kr}p_{ij}p_{kr}\), which is \(\sum_{i,j,r}Z_{ij}Z'_{jr}p_{ir}=\Phi(ZZ')\). Then \(\Phi(I_m)=f_{\rm blk}\), and the last identities are \(\Phi(I_m)\Phi(Z)=\Phi(Z)=\Phi(Z)\Phi(I_m)\). If \(\Phi(Z)=0\), write \(Z_{ij}=\sum_{g\in L}c_{ij,g}\,g\); collecting the terms with first coordinate \(g\) gives \(\sum_{i,j}c_{ij,g}\,p_{ij}=0\) for each \(g\), so all \(c_{ij,g}=0\) by Lemma 4.2. \(\square\)

Now put
\[
\begin{aligned}
a&=1-f_{\rm blk}+\Phi(a_{\rm mat}),\\
b&=1-f_{\rm blk}+\Phi(b_{\rm mat}).
\end{aligned}
\]

**Proposition 4.4.** \(ab=1\) and \(ba\ne1\).

*Proof.* \(f_{\rm blk}\) is an idempotent, and \(1-f_{\rm blk}\) annihilates every \(\Phi(Z)\) on both sides by Lemma 4.3. Hence
\[
\begin{aligned}
ab&=(1-f_{\rm blk})+\Phi(a_{\rm mat}b_{\rm mat})\\
&=1-f_{\rm blk}+\Phi(I_m)=1 ,
\end{aligned}
\]
by Proposition 2.1, and in the same way \(ba-1=\Phi(b_{\rm mat}a_{\rm mat})-f_{\rm blk}=\Phi(\Delta)\), which is nonzero by Proposition 3.2 and injectivity. \(\square\)

The elements \(a\) and \(b\) are finite sums: \(a_{\rm mat}\) and \(b_{\rm mat}\) have finitely many entries, each a finite sum, and \(f_{\rm blk}\) and the \(p_{ij}\) lie in the finite-dimensional algebra \(K[F]\).

## 5. Finite presentation and the proof of the criterion

**Lemma 5.1.** The group \(G=L\times F\) is finitely presented and contains an element of order \(\ell\).

*Proof.* \(N\) has a finite presentation by Lemma 2.2 of [The glued group and planar balance](the-glued-group-and-planar-balance.md). Adding the generator \(z\) with the relators \(z^\ell\) and \([z,s]=zsz^{-1}s^{-1}\) for each generator \(s\) of \(N\) presents \(H=N\times\langle z\rangle\). Every element of \(K_v\) and \(K_*\) is a generator \(s_{f,c}\) or the identity, so Definition 3.1 of the previous lesson adds \(|V|\) generators \(\tau_v\) and at most \(|V|\ell^3\) relators, one for each \(v\), \(u\in K_v\) and \(r\in\mathbb Z/\ell\); so \(L\) is finitely presented. The finite group \(F\) is presented by its multiplication table. A presentation of \(L\times F\) consists of the presentations of the two factors on disjoint generators together with the commutators of each generator of \(L\) with each generator of \(F\). Finally, \(K_v\le N\le H\le L\le G\) by Lemma 4.1 of [The glued group and planar balance](the-glued-group-and-planar-balance.md) and Lemma 3.3 of the previous lesson, and the nonidentity elements of \(K_v\cong\mathbb F_\ell^2\) have order \(\ell\). \(\square\)

*Proof of Theorem 1.1 of [The glued group and planar balance](the-glued-group-and-planar-balance.md).* Lemma 4.1 there embeds the local groups, the previous lesson and Sections 1 to 4 here construct \(a,b\in K[G]\) with \(ab=1\) and \(ba\ne1\), and Lemma 5.1 shows that \(G\) is finitely presented with an element of order \(\ell\). \(\square\)

The proof shows failure of direct finiteness by exhibiting the two elements; it does not deduce it from the failure of stable finiteness in an arbitrary ring. The ingredients that remain are the finite data: the incidence system and the vectors \(x_v\), supplied in [Polynomial pairings on punctured spaces](polynomial-pairings-on-punctured-spaces.md) and the following lessons.

## 6. Exercises

**6.1** (easy). Check \(\Delta=CTUJ_0-eI_m\) in detail, writing out all four products in \(b_{\rm mat}a_{\rm mat}\).

**6.2** (medium). Suppose \(K\) has characteristic two and \(XX^{\mathsf T}=I_m\) with \(X\in\operatorname{Mat}_{m\times t}(K)\), \(m<t\). Show that \(X(I_t-X^{\mathsf T}X)=0\) and \(I_t-X^{\mathsf T}X\ne0\), so a nonzero column of \(I_t-X^{\mathsf T}X\) lies in the kernel of \(X\).

**6.3** (easy). Let \(R\) be a ring, \(f\in R\) an idempotent and \(x,y\in fRf\) with \(xy=f\) and \(yx\ne f\). Show that \(a=1-f+x\) and \(b=1-f+y\) satisfy \(ab=1\) and \(ba\ne1\).

**6.4** (medium). Show that the \(p_{ij}\) span a subalgebra of \(K[F]\) isomorphic to \(\operatorname{Mat}_m(K)\), with identity \(f_{\rm blk}\), and that \(f_{\rm blk}\ne1\) when \(m\ge1\).

## 7. Solutions

**6.1.** \(b_{\rm mat}a_{\rm mat}\) is the sum of the four terms \(CTUJ_0\), \(CT(1-e)\), \((1-e)UJ_0\) and \((1-e)^2I_m\). The second term is \(C(1-e)T=0\) and the third is \(U(1-e)J_0=0\), since \(1-e\) is central and kills the entries of \(C\) and \(J_0\). The last is \((1-e)I_m\). Subtracting \(I_m\) leaves \(CTUJ_0-eI_m\).

**6.2.** \(X(I_t-X^{\mathsf T}X)=X-(XX^{\mathsf T})X\), which is \(X-X=0\). The matrix \(X^{\mathsf T}X\) has rank at most \(m<t\), so it is not \(I_t\). A nonzero column \(y\) of \(I_t-X^{\mathsf T}X\) then satisfies \(Xy=0\).

**6.3.** As in Exercise 8.4 of [Directly finite group algebras](directly-finite-group-algebras.md), \((1-f)x=x(1-f)=0\) and the same for \(y\), so \(ab=(1-f)+xy=1\) and \(ba=(1-f)+yx\ne(1-f)+f=1\).

**6.4.** By Lemma 4.2 the linear map \(\operatorname{Mat}_m(K)\to K[F]\) sending the matrix unit \(E_{ij}\) to \(p_{ij}\) is multiplicative and injective, so its image, the span of the \(p_{ij}\), is a subalgebra isomorphic to \(\operatorname{Mat}_m(K)\), with identity \(\sum_ip_{ii}=f_{\rm blk}\). For each \(c\in B\) put \(e_c=|B|^{-1}\sum_{w\in B}\zeta^{-c\cdot w}w\), with \(c\cdot w=\sum_kc_kw_k\). The computation of Lemma 4.1 shows that these \(\ell^m\) elements are nonzero, pairwise orthogonal idempotents, hence linearly independent (multiply a relation by one of them), and the computation of Exercise 5.2 of the previous lesson shows \(\sum_ce_c=1\). Here \(p_i=e_c\) for the unit vector \(c\) in coordinate \(i\). If \(f_{\rm blk}=1\), the remaining \(\ell^m-m\ge1\) idempotents \(e_c\) would add up to zero, contradicting linear independence. So \(f_{\rm blk}\ne1\).

## References

- [OpenAI-DF2] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, OpenAI Math Release preprint, 23 September 2026, Sections 4.3 to 4.6. https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026
- [Dykema–Heister–Juschenko] K. Dykema, T. Heister and K. Juschenko, *Finitely presented groups related to Kaplansky's Direct Finiteness Conjecture*, arXiv:1112.1790. https://arxiv.org/abs/1112.1790
