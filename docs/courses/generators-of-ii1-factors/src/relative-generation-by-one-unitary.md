# Relative generation by one unitary

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(P\subseteq M\) be an irreducible inclusion of II₁ factors, with \(M\) of separable predual. This lesson proves that for most unitaries \(u\) of \(M\), in the sense of Baire category for the trace norm, \(P\) and \(u\) generate \(M\). The proof is by contradiction at a point where many distance functions are continuous. If \(W^*(P,u)\) were a proper subalgebra, a vector \(\xi\) orthogonal to it would be detected by words in \(P\) and in a nearby unitary: a small perturbation of \(u\), spread evenly over its \(\ell\) occurrences in a long word, produces a correlation with \(\xi\) of fixed size. The size of the perturbation tends to zero as \(\ell\) grows, while the nonlinear error stays bounded independently of \(\ell\). The bound comes from comparing all the coefficients of the error with a single element of a free group algebra and from Haagerup's inequality for words of length one.

We use: [Haar unitaries, freeness and tracial ultraproducts](haar-unitaries-freeness-and-ultraproducts.md) (Lemma 1.1, the continuity remarks and the conditional expectation of Section 1, Lemmas 3.2, 3.3, and the ultraproduct facts of Section 4); [Free independence in ultraproducts](free-independence-in-ultraproducts.md) (Corollary 4.4 and the remark after it); the double commutant theorem, [Section 4 of its lesson](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#OA-FND-BI-06); Kaplansky's density theorem, [Section 7 of its lesson](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07); the Baire category theorem, [Section 3 of its lesson](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-03); the Banach–Alaoglu theorem with metrizability of the ball for a separable predual, [Section 3 of its lesson](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian#OA-FND-WT-03); and the identification of a von Neumann algebra with the dual of its \(\sigma\)-weakly continuous functionals, with the \(\sigma\)-weak topology as weak\* topology, [Sections 6](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-07) and [9](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10) of the lesson on preduals and operator topologies.

## 1. Haagerup's inequality for words of length one

Let \(\mathbb F\) be a free group with a free basis \(\mathcal S\), let \(\mathcal L=\mathcal S\cup\mathcal S^{-1}\), and let \(\lambda\) be the left regular representation on \(\ell^2(\mathbb F)\) with standard basis \((\delta_g)\). Every element \(g\ne e\) is a unique reduced word, and its first letter lies in \(\mathcal L\).

**Lemma 1.1.** For every finitely supported family \((b_\gamma)_{\gamma\in\mathcal L}\) of complex numbers,
\[
\Bigl\|\sum_{\gamma\in\mathcal L}b_\gamma\lambda(\gamma)\Bigr\|\le2\Bigl(\sum_{\gamma\in\mathcal L}|b_\gamma|^2\Bigr)^{1/2}.
\]

**Proof.** For \(\gamma\in\mathcal L\) let \(B_\gamma\) be the orthogonal projection onto the closed span of the \(\delta_g\) with \(g\) a reduced word beginning with \(\gamma\). These projections are mutually orthogonal. If a reduced word \(g\) does not begin with \(\gamma^{-1}\), then \(\gamma g\) is reduced and begins with \(\gamma\); this includes \(g=e\). Hence \(\lambda(\gamma)(1-B_{\gamma^{-1}})\) maps into the range of \(B_\gamma\). Split \(\lambda(\gamma)=\lambda(\gamma)(1-B_{\gamma^{-1}})+\lambda(\gamma)B_{\gamma^{-1}}\). For \(\eta\in\ell^2(\mathbb F)\), orthogonality of the ranges gives
\[
\Bigl\|\sum_\gamma b_\gamma\lambda(\gamma)(1-B_{\gamma^{-1}})\eta\Bigr\|^2=\sum_\gamma|b_\gamma|^2\|(1-B_{\gamma^{-1}})\eta\|^2\le\Bigl(\sum_\gamma|b_\gamma|^2\Bigr)\|\eta\|^2 ,
\]
and the Cauchy–Schwarz inequality, with \(\sum_\gamma\|B_{\gamma^{-1}}\eta\|^2\le\|\eta\|^2\), gives
\[
\Bigl\|\sum_\gamma b_\gamma\lambda(\gamma)B_{\gamma^{-1}}\eta\Bigr\|\le\sum_\gamma|b_\gamma|\,\|B_{\gamma^{-1}}\eta\|\le\Bigl(\sum_\gamma|b_\gamma|^2\Bigr)^{1/2}\|\eta\| .
\]
Adding the two bounds proves the lemma. \(\square\)

## 2. Comparison of coefficients in a group algebra

For an element \(f=\sum_gf(g)g\) of the group algebra \(\mathbb C[\mathbb F]\) write \(|f|=\sum_g|f(g)|g\), and write \(f\le f'\) for elements with real coefficients if \(f(g)\le f'(g)\) for every \(g\). Identify \(f\) with the vector \(\sum_gf(g)\delta_g=\lambda(f)\delta_e\) of \(\ell^2(\mathbb F)\). Then
\[
|ff'|\le|f|\,|f'|,\qquad\text{and}\qquad\|f\|_{\ell^2}\le\|f'\|_{\ell^2}\ \text{ if }\ |f|\le f' ,
\]
the first because \((ff')(g)=\sum_{ab=g}f(a)f'(b)\).

**Lemma 2.1.** Let \(B_1,\dots,B_\ell\in\mathbb C[\mathbb F]\) and \(A_1,\dots,A_\ell\) with nonnegative coefficients satisfy \(|B_k|\le A_k\), and put \(A=A_1+\dots+A_\ell\). For every \(d\ge0\),
\[
\Bigl|\sum_{m_1+\dots+m_\ell=d}\frac{B_1^{m_1}\cdots B_\ell^{m_\ell}}{m_1!\cdots m_\ell!}\Bigr|\le A^d .
\]

**Proof.** By the two rules above, the left side is at most \(\sum A_1^{m_1}\cdots A_\ell^{m_\ell}\), the sum over \(m_1+\dots+m_\ell=d\), and the factorials only decrease it. Expanding \(A^d=(A_1+\dots+A_\ell)^d\) gives one product \(A_{k_1}\cdots A_{k_d}\) for each sequence \((k_1,\dots,k_d)\); the nondecreasing sequences give exactly the products \(A_1^{m_1}\cdots A_\ell^{m_\ell}\), and all other products have nonnegative coefficients. No commutation of the \(A_k\) is used. \(\square\)

## 3. A perturbation with uniform correlation

Throughout this section \(P\subseteq M\) is an irreducible inclusion of II₁ factors with trace \(\tau\), \(\omega\) a free ultrafilter, and \(M\subseteq M^\omega\), \(P^\omega\subseteq M^\omega\) as in the first lesson. Products \(\prod_{k=1}^\ell\) are taken in increasing order from left to right.

**Proposition 3.1.** Let \(u,z\) be unitaries of \(M\), \(\xi\in M\), \(0<\alpha<1/2\) and \(\ell\ge1\). There are a unitary \(\tilde u\in M\) and unitaries \(\tilde t_0,\dots,\tilde t_\ell\in P\) such that \(\tilde W=\tilde t_0\prod_{k=1}^\ell(\tilde u\tilde t_k)\) satisfies
\[
\|\tilde u-u\|_2\le\frac{\alpha}{\sqrt{2\ell}}+\frac1\ell,\qquad\Bigl|\tau(\xi^*\tilde W)-\frac\alpha2\tau(\xi^*z)\Bigr|\le\|\xi\|_2\,\frac{4\alpha^2}{1-2\alpha}+\frac1\ell .
\]

The proof occupies the rest of this section. Fix \(u,z,\xi,\alpha,\ell\).

*Free letters.* Let \(D_0=C^*(u,z,\xi)\subseteq M^\omega\), a norm-separable unital C\*-algebra. By Corollary 4.4 of the second lesson and the remark after it, there are Haar unitaries \(t_0,\dots,t_\ell\in P^\omega\), each with a representing sequence of unitaries of \(P\), such that \(t_j\) is free from \(D_j=C^*(D_0,t_0,\dots,t_{j-1})\). Put
\[
s_1=t_0,\qquad s_{j+1}=ut_j\ (1\le j\le\ell),\qquad g_k=s_1s_2\cdots s_k\ (1\le k\le\ell+1),\qquad W=g_{\ell+1}=t_0\prod_{k=1}^\ell(ut_k).
\]
Then \(s_1,\dots,s_j\in D_j\), and \(g_k\) is the part of \(W\) that precedes the \(k\)th occurrence of \(u\).

**Lemma 3.2.** (a) Each \(s_{j+1}\), \(0\le j\le\ell\), is a Haar unitary free from \(D_j\).
(b) Every reduced word \(\ne e\) in \(s_1,\dots,s_\ell\) has trace \(0\). Hence \(s_1,\dots,s_\ell\) are free generators of a free group \(G\subseteq\mathcal U(D_\ell)\), and every \(p\in G\setminus\{e\}\) is centred.
(c) \(W\) and \(y=zW^*\) are Haar unitaries free from \(D_\ell\).
(d) For \(p\in G\) put \(Y_p=pyp^{-1}\). Let \(S\subseteq G\) be finite, \(F_S\) the free group on generators \(T_p\), \(p\in S\), and \(\Phi\colon\mathbb C[F_S]\to M^\omega\) the algebra homomorphism with \(\Phi(T_p)=Y_p\). Then \(\tau(\Phi(g))=0\) for \(g\in F_S\setminus\{e\}\), and \(\|\Phi(f)\|_2=\|f\|_{\ell^2}\) for \(f\in\mathbb C[F_S]\).

**Proof.** (a) \(s_1=t_0\) is free from \(D_0\), and \(s_{j+1}=ut_j\) with \(u\in\mathcal U(D_j)\), so Lemma 3.3 of the first lesson applies.

(b) Induction on the largest index \(r\) occurring in the word. For \(r=1\) the word is \(s_1^n\), \(n\ne0\). In general the word is \(c_0s_r^{n_1}c_1\cdots s_r^{n_q}c_q\), where each interior \(c_i\) is a nonempty reduced word in \(s_1,\dots,s_{r-1}\), centred by induction, and \(c_0,c_q\in D_{r-1}\). Since \(s_r\) is a Haar unitary free from \(D_{r-1}\), (3.1) of the first lesson gives trace \(0\). A nontrivial reduced word is therefore \(\ne1\), so the homomorphism from the free group onto the group generated by the \(s_j\) is injective.

(c) \(W=(g_\ell u)t_\ell\) with \(g_\ell u\in\mathcal U(D_\ell)\), and \(y=zW^*\) with \(z\in\mathcal U(D_\ell)\); apply Lemma 3.3 of the first lesson twice.

(d) A reduced word \(g=T_{p_1}^{a_1}\cdots T_{p_r}^{a_r}\ne e\), with successive labels distinct and \(a_i\ne0\), maps to
\[
\Phi(g)=p_1y^{a_1}(p_1^{-1}p_2)y^{a_2}\cdots(p_{r-1}^{-1}p_r)y^{a_r}p_r^{-1}.
\]
The interior letters \(p_i^{-1}p_{i+1}\) are elements of \(G\setminus\{e\}\), centred by (b), and the outer letters lie in \(D_\ell\). By (c) and (3.1) of the first lesson, \(\tau(\Phi(g))=0\). For \(g\ne h\) in \(F_S\), \(\langle\Phi(g),\Phi(h)\rangle=\tau(\Phi(h^{-1}g))=0\), and \(\|\Phi(g)\|_2=1\). So \(\Phi\) maps the basis of \(\ell^2(F_S)\) to an orthonormal family. \(\square\)

*The perturbation.* Put \(\operatorname{Im}(b)=(b-b^*)/(2i)\) and
\[
h=\frac\alpha\ell\sum_{j=1}^\ell\operatorname{Im}(g_j^{-1}yg_j),\qquad u'=e^{ih}u,\qquad W'=t_0\prod_{k=1}^\ell(u't_k).
\]
Here \(h=h^*\) and \(\|h\|\le\alpha\). The elements \(g_j^{-1}\), \(1\le j\le\ell\), are distinct, so by Lemma 3.2(d) the \(2\ell\) unitaries \(Y_{g_j^{-1}}=g_j^{-1}yg_j\) and their inverses are orthonormal. Hence \(\|\sum_j\operatorname{Im}(Y_{g_j^{-1}})\|_2^2=2\ell/4\), and
\[
\|h\|_2=\frac{\alpha}{\sqrt{2\ell}} .
\tag{3.1}
\]

*Moving the perturbations to the front.* Put \(H_k=g_khg_k^{-1}\). Then
\[
W'=\Bigl(\prod_{k=1}^\ell e^{iH_k}\Bigr)W .
\tag{3.2}
\]
Indeed, \(t_0\prod_{k\le m}(u't_k)=\bigl(\prod_{k\le m}e^{iH_k}\bigr)g_{m+1}\) for \(m=0\) because \(g_1=t_0\), and if it holds for \(m\), then
\[
t_0\prod_{k\le m+1}(u't_k)=\Bigl(\prod_{k\le m}e^{iH_k}\Bigr)g_{m+1}e^{ih}ut_{m+1}=\Bigl(\prod_{k\le m+1}e^{iH_k}\Bigr)g_{m+1}ut_{m+1},
\]
using \(g_{m+1}e^{ih}=e^{iH_{m+1}}g_{m+1}\) and \(g_{m+1}ut_{m+1}=g_{m+2}\). With \(p_{kj}=g_kg_j^{-1}\) and \(c=\alpha/(2\ell)\),
\[
iH_k=\frac{\alpha}{\ell}\sum_{j=1}^\ell i\operatorname{Im}(Y_{p_{kj}})=c\sum_{j=1}^\ell\bigl(Y_{p_{kj}}-Y_{p_{kj}}^{-1}\bigr).
\tag{3.3}
\]

*Multiplicities.* Let \(S=\{p_{kj}:1\le k,j\le\ell\}\) and \(n_p=\#\{(k,j):p_{kj}=p\}\). The diagonal gives \(p_{kk}=e\), so \(n_e=\ell\). For \(k\ne j\), the word \(p_{kj}=s_1\cdots s_ks_j^{-1}\cdots s_1^{-1}\) is reduced, because its only junction of a positive and a negative letter is \(s_ks_j^{-1}\) with \(k\ne j\). Its maximal initial segment of positive letters, \(s_1\cdots s_k\), determines \(k\), and its final segment determines \(j\). So the off-diagonal pairs give \(\ell(\ell-1)\) distinct elements \(\ne e\), and
\[
\sum_{p\in S}n_p^2=\ell^2+\ell(\ell-1)=2\ell^2-\ell .
\tag{3.4}
\]

*The first-order term.* Put \(C_1=\sum_{k=1}^\ell iH_k=c\sum_{p\in S}n_p(Y_p-Y_p^{-1})\). We show
\[
\tau\bigl(\xi^*(1+C_1)W\bigr)=\frac\alpha2\tau(\xi^*z).
\tag{3.5}
\]
First, \(\tau(\xi^*W)=0\) by (3.1) of the first lesson for \(W\) and \(D_\ell\), with one power of \(W\) and outer letters \(\xi^*\in D_\ell\) and \(1\). Next, \(Y_eW=yW=z\), so the \(n_e=\ell\) diagonal terms contribute \(c\ell\,\tau(\xi^*z)=\frac\alpha2\tau(\xi^*z)\). For \(p\ne e\),
\[
\tau(\xi^*Y_pW)=\tau(\xi^*pz\,W^{-1}\,p^{-1}\,W)=0,
\]
because the interior letter \(p^{-1}\) is centred. For every \(p\in G\), \(\tau(\xi^*Y_p^{-1}W)=\tau(\xi^*p\,W\,(z^*p^{-1})\,W)\); writing \(z^*p^{-1}=\tau(z^*p^{-1})1+d^\circ\), the centred part gives \(\tau(\xi^*pWd^\circ W)=0\) and the scalar part gives a multiple of \(\tau(\xi^*pW^2)=0\), both by (3.1). This proves (3.5).

*The remainder.* Expanding each exponential in (3.2) and grouping by total degree,
\[
\prod_{k=1}^\ell e^{iH_k}=\sum_{d\ge0}C_d,\qquad C_d=\sum_{m_1+\dots+m_\ell=d}\frac{(iH_1)^{m_1}\cdots(iH_\ell)^{m_\ell}}{m_1!\cdots m_\ell!};
\]
the grouping is legitimate because \(\sum_d\|C_d\|\le\prod_k\sum_m\|H_k\|^m/m!\le e^{\ell\alpha}\). The terms \(C_0=1\) and \(C_1\) are as above. We show
\[
\Bigl\|\prod_{k=1}^\ell e^{iH_k}-1-C_1\Bigr\|_2\le\frac{4\alpha^2}{1-2\alpha}.
\tag{3.6}
\]
In \(\mathbb C[F_S]\), with \(\Phi\) from Lemma 3.2(d), put
\[
B_k=c\sum_{j=1}^\ell\bigl(T_{p_{kj}}-T_{p_{kj}}^{-1}\bigr),\qquad A_k=c\sum_{j=1}^\ell\bigl(T_{p_{kj}}+T_{p_{kj}}^{-1}\bigr),\qquad A=\sum_kA_k=c\sum_{p\in S}n_p\bigl(T_p+T_p^{-1}\bigr).
\]
Then \(\Phi(B_k)=iH_k\) by (3.3), \(|B_k|\le A_k\), and \(C_d=\Phi(\mathcal C_d)\) with \(\mathcal C_d=\sum B_1^{m_1}\cdots B_\ell^{m_\ell}/(m_1!\cdots m_\ell!)\). By Lemma 3.2(d) and Lemma 2.1,
\[
\|C_d\|_2=\|\mathcal C_d\|_{\ell^2}\le\|A^d\|_{\ell^2}=\|\lambda(A)^d\delta_e\|\le\|\lambda(A)\|^d .
\]
Lemma 1.1, for the free group \(F_S\) with \(b_{T_p}=b_{T_p^{-1}}=cn_p\), and (3.4) give
\[
\|\lambda(A)\|\le2\Bigl(2c^2\sum_{p\in S}n_p^2\Bigr)^{1/2}=\frac{\alpha}{\ell}\bigl(4\ell^2-2\ell\bigr)^{1/2}\le2\alpha<1 .
\]
So \(\|C_d\|_2\le(2\alpha)^d\). The series \(\sum_dC_d\) converges in operator norm, hence in \(2\)-norm, and (3.6) follows from \(\sum_{d\ge2}(2\alpha)^d=4\alpha^2/(1-2\alpha)\). Only the coefficient isometry of Lemma 3.2(d) relates \(\mathbb C[F_S]\) to \(M^\omega\); no comparison of operator norms between the two is needed.

*The correlation in the ultrapower.* By (3.2), (3.5), (3.6), Lemma 1.1(1) of the first lesson and \(\|xW\|_2=\|x\|_2\),
\[
\Bigl|\tau(\xi^*W')-\frac\alpha2\tau(\xi^*z)\Bigr|=\Bigl|\tau\Bigl(\xi^*\Bigl(\prod_ke^{iH_k}-1-C_1\Bigr)W\Bigr)\Bigr|\le\|\xi\|_2\frac{4\alpha^2}{1-2\alpha}.
\tag{3.7}
\]

*Choosing one coordinate.* Let \(t_{j,n}\in\mathcal U(P)\) represent \(t_j\), and use the constant sequences for \(u,z,\xi\). Define \(g_{k,n},W_n,y_n,h_n,u_n',W_n'\) by the formulas above. They are bounded sequences that represent \(g_k,W,y,h,u',W'\): the quotient map is a \(*\)-homomorphism, and the exponential series converges uniformly because \(\|h_n\|\le\alpha\). Each \(h_n\) is self-adjoint, so \(u_n'\) is a unitary of \(M\). Moreover
\[
\lim_\omega\|h_n\|_2=\|h\|_2=\frac\alpha{\sqrt{2\ell}},\qquad\lim_\omega\tau(\xi^*W_n')=\tau(\xi^*W'),
\]
and \(\|u_n'-u\|_2=\|e^{ih_n}-1\|_2\le\|h_n\|_2\), by \(|e^{ir}-1|\le|r|\) and functional calculus. The sets of \(n\) with \(\|h_n\|_2<\alpha/\sqrt{2\ell}+1/\ell\) and with \(|\tau(\xi^*W_n')-\tau(\xi^*W')|<1/\ell\) belong to \(\omega\); choose \(n\) in both. Then \(\tilde u=u_n'\) and \(\tilde t_j=t_{j,n}\) satisfy the proposition, by (3.7). This completes the proof of Proposition 3.1. \(\square\)

## 4. Relative generation

For a unitary \(u\in M\) write \(N_u=W^*(P\cup\{u\})\) and \(e_u\) for the orthogonal projection of \(L^2(M)\) onto \(L^2(N_u)\). For \(\xi\in L^2(M)\) put
\[
f_\xi(u)=\|e_u\xi\|_2,\qquad d_\xi(u)=\operatorname{dist}\bigl(\xi,L^2(N_u)\bigr)=\bigl(\|\xi\|_2^2-f_\xi(u)^2\bigr)^{1/2}.
\]
The unitary group \(\mathcal U(M)\) carries the metric \(d(u,v)=\|u-v\|_2\).

**Lemma 4.1.** Let \(M\) be a tracial von Neumann algebra with separable predual. Then \(L^2(M)\) is separable, and \((\mathcal U(M),d)\) is a complete metric space.

**Proof.** The unit ball of \(M\) is the unit ball of the dual of the separable predual, with the \(\sigma\)-weak topology as weak\* topology. It is compact and metrizable, hence separable; let \(S\) be a countable dense subset. For \(\xi\in L^2(M)\), the functional \(x\mapsto\langle x1,\xi\rangle\) is a vector functional of the representation on \(L^2(M)\), hence \(\sigma\)-weakly continuous. If \(\xi\perp S\), it vanishes on the closure of \(S\), the whole unit ball, so \(\xi\perp M\) and \(\xi=0\). Hence rational combinations of \(S\) are dense in \(L^2(M)\). A \(d\)-Cauchy sequence of unitaries converges in the unit ball of \(M\), which is complete for \(\|\cdot\|_2\), and the limit is a unitary by the continuity remarks of the first lesson. \(\square\)

**Lemma 4.2.** For \(\xi,\eta\in L^2(M)\), the function \(d_\xi\) is upper semicontinuous and \(f_\xi\) is lower semicontinuous on \((\mathcal U(M),d)\), \(0\le f_\xi\le\|\xi\|_2\), and \(|f_\xi(u)-f_\eta(u)|\le\|\xi-\eta\|_2\).

**Proof.** Let \(\mathcal P\) be the set of finite sums of products \(a_0X^{\epsilon_1}a_1\cdots X^{\epsilon_r}a_r\) with \(a_i\in P\) and \(X^{\epsilon}\in\{X,X^*\}\), and \(b(u)\) the value at \(X=u\). For a unitary \(u\), \(\{b(u):b\in\mathcal P\}\) is the unital \(*\)-algebra generated by \(P\) and \(u\). By the double commutant and Kaplansky density theorems, every element of \(N_u\) is a strong limit of a bounded net of such \(b(u)\), hence a \(2\)-norm limit; so these elements are dense in \(L^2(N_u)\), and
\[
d_\xi(u)=\inf_{b\in\mathcal P}\|\xi-b(u)\|_2 .
\]
For fixed \(b\), \(u\mapsto b(u)\) is \(d\)-continuous: by Lemma 1.1(1) of the first lesson, a product as above changes by at most \(r\,\|a_0\|\cdots\|a_r\|\,\|u-v\|_2\) when \(u\) is replaced by a unitary \(v\), since \(\|u^*-v^*\|_2=\|u-v\|_2\). An infimum of continuous functions is upper semicontinuous, so \(d_\xi\) is, and \(f_\xi^2=\|\xi\|_2^2-d_\xi^2\) is lower semicontinuous. The last two claims hold because \(e_u\) is a contraction. \(\square\)

**Lemma 4.3.** A bounded lower semicontinuous function \(f\) on a complete metric space \(X\) is continuous at every point of a dense \(G_\delta\) subset.

**Proof.** For \(\varepsilon>0\) let \(G_\varepsilon\) be the union of all open sets on which the oscillation \(\sup f-\inf f\) is less than \(\varepsilon\); it is open. It is dense: given a nonempty open \(O\), let \(s=\sup_Of\), choose \(x\in O\) with \(f(x)>s-\varepsilon/3\), and by lower semicontinuity an open \(V\subseteq O\) containing \(x\) on which \(f>f(x)-\varepsilon/3\); the oscillation on \(V\) is at most \(2\varepsilon/3\). By the Baire category theorem, \(\bigcap_{n\ge1}G_{1/n}\) is a dense \(G_\delta\), and \(f\) is continuous at each of its points. \(\square\)

**Theorem 4.4** (relative generation). Let \(P\subseteq M\) be an irreducible inclusion of II₁ factors with \(M\) of separable predual. The set
\[
\mathcal G=\{u\in\mathcal U(M):W^*(P\cup\{u\})=M\}
\]
is a dense \(G_\delta\) subset of \((\mathcal U(M),d)\).

**Proof.** Let \((\eta_j)\) be dense in \(L^2(M)\) (Lemma 4.1). By Lemma 4.3, applied to each \(f_{\eta_j}\) on the complete space \(\mathcal U(M)\), and the Baire category theorem, there is a dense \(G_\delta\) set \(\mathcal C\) at whose points every \(f_{\eta_j}\) is continuous. By the Lipschitz bound of Lemma 4.2, every \(f_\xi\) is continuous at every point of \(\mathcal C\): for \(u\in\mathcal C\) and \(v\in\mathcal U(M)\), \(|f_\xi(v)-f_\xi(u)|\le2\|\xi-\eta_j\|_2+|f_{\eta_j}(v)-f_{\eta_j}(u)|\).

Let \(u\in\mathcal C\) and suppose \(N_u\ne M\). The unitaries span \(M\), so there is a unitary \(z\notin N_u\). Put \(\xi=z-E_{N_u}(z)\in M\) and \(s=\|\xi\|_2>0\). Since \(E_{N_u}\) is the restriction of \(e_u\), \(e_u\xi=0\) and \(f_\xi(u)=0\); and \(\tau(\xi^*z)=\tau(\xi^*\xi)=s^2\) because \(\xi\perp E_{N_u}(z)\). Fix \(0<\alpha<\min(1/4,s/32)\). For each \(\ell\ge1\), Proposition 3.1 gives a unitary \(u_\ell\) and a unitary \(W_\ell=t_{0,\ell}\prod_k(u_\ell t_{k,\ell})\in N_{u_\ell}\) with
\[
\|u_\ell-u\|_2\le\frac{\alpha}{\sqrt{2\ell}}+\frac1\ell,\qquad\Bigl|\tau(\xi^*W_\ell)-\frac{\alpha s^2}2\Bigr|\le\frac{4s\alpha^2}{1-2\alpha}+\frac1\ell .
\]
Since \(\alpha<1/4\) and \(\alpha<s/32\), \(4s\alpha^2/(1-2\alpha)<8s\alpha^2<\alpha s^2/4\), so \(|\tau(\xi^*W_\ell)|\ge\alpha s^2/4-1/\ell\ge\alpha s^2/8\) for large \(\ell\). On the other hand \(\|W_\ell\|_2=1\) and \(W_\ell\in N_{u_\ell}\), so
\[
|\tau(\xi^*W_\ell)|=|\langle W_\ell,\xi\rangle|=|\langle W_\ell,e_{u_\ell}\xi\rangle|\le f_\xi(u_\ell).
\]
As \(u_\ell\to u\), continuity at \(u\) gives \(f_\xi(u_\ell)\to f_\xi(u)=0\), a contradiction. So \(\mathcal C\subseteq\mathcal G\), and \(\mathcal G\) is dense.

Finally,
\[
\mathcal G=\bigcap_{j,n\ge1}\{v\in\mathcal U(M):d_{\eta_j}(v)<1/n\},
\]
an intersection of open sets by Lemma 4.2. Indeed, all \(d_{\eta_j}(v)\) vanish exactly when \(L^2(N_v)\) contains a dense set, i.e. \(L^2(N_v)=L^2(M)\); and if \(N_v\ne M\), a unitary \(z\notin N_v\) gives the nonzero vector \(z-E_{N_v}(z)\) orthogonal to \(L^2(N_v)\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(\gamma\) be one of the free generators. Show that \(\|\lambda(\gamma)+\lambda(\gamma^{-1})\|=2\), while Lemma 1.1 gives the bound \(2\sqrt2\).

**Exercise 5.2.** For \(\ell=2\), list the four elements \(p_{kj}\) and check (3.4).

**Exercise 5.3.** Show that the set \(\mathcal G\) of Theorem 4.4 satisfies \(a\mathcal Gb=\mathcal G\) for unitaries \(a,b\in P\), and \(\mathcal G^*=\mathcal G\).

**Exercise 5.4.** Show that every element of a von Neumann algebra is a linear combination of four unitaries, as used in the proof of Theorem 4.4.

## 6. Solutions

**5.1.** The right cosets \(\langle\gamma\rangle g\) partition \(\mathbb F\), and \(\lambda(\gamma)\) shifts each \(\ell^2(\langle\gamma\rangle g)\cong\ell^2(\mathbb Z)\). So \(\lambda(\gamma)+\lambda(\gamma)^*\) is a direct sum of copies of \(S+S^*\) on \(\ell^2(\mathbb Z)\), \(S\) the bilateral shift, which the Fourier transform turns into multiplication by \(2\cos\theta\) on \(L^2\) of the circle; its norm is \(2\). Lemma 1.1 with \(b_\gamma=b_{\gamma^{-1}}=1\) gives \(2\sqrt2\).

**5.2.** \(p_{11}=p_{22}=e\), \(p_{12}=s_1s_2^{-1}s_1^{-1}\), \(p_{21}=s_1s_2s_1^{-1}\). So \(n_e=2\) and the two other elements have multiplicity \(1\): \(\sum n_p^2=6=2\cdot2^2-2\).

**5.3.** \(W^*(P\cup\{aub\})=W^*(P\cup\{u\})\) because \(a,b\in P\), and \(W^*(P\cup\{u^*\})=W^*(P\cup\{u\})\) because generated von Neumann algebras contain adjoints.

**5.4.** A self-adjoint \(x\) with \(\|x\|\le1\) is \(\frac12(w+w^*)\) with the unitary \(w=x+i(1-x^2)^{1/2}\). A general element is \(\operatorname{Re}x+i\operatorname{Im}x\), and each part is a multiple of a self-adjoint contraction.

## References

- [OpenAI-Gen] OpenAI, Relative generation and the generator problem for finite factors, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Relative-generation-and-the-generator-problem-for-finite-factors-September-23-2026
- [Popa-Ind] S. Popa, Independence properties in subalgebras of ultraproduct II₁ factors, Journal of Functional Analysis 266 (2014), 5818–5846. https://arxiv.org/abs/1308.3982
