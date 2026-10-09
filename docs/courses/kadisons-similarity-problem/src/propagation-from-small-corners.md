# Propagation from small corners

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The word structure of the previous lesson reduces the free corner estimate to a comparison of the operators \(B_k\), which describe the averaged operator \(G\) on the \(k\)th word level, with \(B_0\), which describes it on \(L^2(A_0)\). This lesson shows that on words with a repeated letter the operator \(B_k\) acts like \(B_0\), with an error independent of \(k\) [OpenAI-288, Section 4]. Two ingredients combine. First, on vectors whose right support is a small projection, \(G\) agrees up to \(c_0\varepsilon\) with a right multiplication: the cyclic implementation theorem applied in a corner, then extended by matrix units. Second, a word with a repeated letter \(x_n\), a rescaled power of a Haar unitary of a small corner, carries the error vector \(A_nx_ny\); as \(n\to\infty\), the part of it that is not carried isometrically tends to zero. Assembling orthogonal copies of \(L^2(A_0)\) from all word levels then yields a subspace on which \(G\) acts, up to \(2c_0\varepsilon\), as \(I\otimes B_0\), and a compressed commutator estimate.

We keep the standing hypotheses and notation of [Invariant tensors and the word structure](invariant-tensors-and-the-word-structure.md): \(D\), \(A_0\), \(\mathcal L\), \(\tau\), \(H=L^2(\mathcal L)\), \(E\), \(E^\circ\), \(B\), \(B^\circ\), \(J_k\), the levels \(\mathcal H_k\) and the operators \(B_k\) of its Theorem 7.1, for an operator \(G\) satisfying the hypotheses of its Theorem 1.1 with constants \(t=1/N\) and \(\varepsilon\), and commuting with all \(W_u\) (its Lemma 3.1). We also use Lemma 2.1 there (\(\mathcal L\) is a II\(_1\) factor); Theorem 4.2 of [Row, column and cyclic estimates](row-column-and-cyclic-estimates.md), with \(c_0=4\sqrt2\); Theorem 1.3 of [Words in free subalgebras](words-in-free-subalgebras.md); the commutation theorem, [Theorem 3.1 of Integration for a trace](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications#3-the-commutation-theorem); [Proposition 4.3 of Projections and types](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-07) (left and right supports are equivalent) and its comparison theorem, [Theorem 5.5](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-06); and Haar unitaries of corners of II\(_1\) factors, [Definition 2.1, Lemma 2.3 and Corollary 2.4 of Haar unitaries, freeness and tracial ultraproducts](course:generators-of-ii1-factors/haar-unitaries-freeness-and-ultraproducts#2-haar-unitaries).

For a projection \(r\in\mathcal L\) write \(Hr=\{\xi\in H:\xi r=\xi\}\), the range of the projection \(R_r\); it is invariant under left multiplication. For \(b\in\mathcal L\), \(R_b\) vanishes on \(H(1-r)\) exactly when \(b=rb\), because \(R_bR_r=R_{rb}\) and \(b\mapsto R_b\) is injective.

## 1. Full columns from a small corner

**Lemma 1.1.** For every projection \(r\in\mathcal L\) with \(\tau(r)\le t\) there is \(b\in\mathcal L\) with \(b=rb\) and
\[
\big\|(G-R_b)|_{Hr}\big\|\le c_0\varepsilon .
\tag{1.1}
\]
The same holds for \(G^*\) in place of \(G\).

**Proof.** We may assume \(r\ne0\). Fix a projection \(e\in D\) with \(\tau(e)=t\). Since \(\mathcal L\) is a II\(_1\) factor and \(\tau(r)\le\tau(e)\), the comparison theorem gives a partial isometry \(v\in\mathcal L\) with \(v^*v=r\) and \(vv^*=r'\le e\). Right multiplication by \(v\) is a unitary of \(eHr'\) onto \(eHr\) commuting with left multiplications: \(\|\xi v\|_2^2=\tau(v^*\xi^*\xi v)=\tau(\xi^*\xi r')=\|\xi\|_2^2\) for bounded \(\xi\in eHr'\), and right multiplication by \(v^*\) is its inverse. The vector \(r'\) is cyclic for the left action of \(e\mathcal Le\) on \(eHr'\), because \(e\mathcal Le\,r'=e\mathcal Lr'\) is dense in \(eHr'\). Hence the representation \(\sigma(a)=L_a|_{eHr}\) of the unital C\*-algebra \(e\mathcal Le\) (with unit \(e\)) has a cyclic vector. Let \(\lambda(a)=L_a|_{eH}\).

Since \(G\) commutes with \(L_e\), it maps \(eH\) into itself; let \(G_e:eHr\to eH\) be its restriction. Then \(\Delta(a)=G_e\sigma(a)-\lambda(a)G_e=[G,L_a]|_{eHr}\) is a rectangular derivation for \(\sigma,\lambda\) with \(\|\Delta\|\le\varepsilon\), by (1.1) of the previous lesson. Theorem 4.2 of the cyclic estimates lesson gives \(V:eHr\to eH\) with \(\Delta(a)=V\sigma(a)-\lambda(a)V\) and \(\|V\|\le c_0\varepsilon\). The operator \(T=G_e-V\) satisfies \(T\sigma(a)=\lambda(a)T\) for \(a\in e\mathcal Le\) and \(\|G_e-T\|\le c_0\varepsilon\).

Since \(\tau(e)=1/N\), there are \(v_1,\dots,v_N\in D\) with \(v_i^*v_i=e\) and \(\sum_iv_iv_i^*=1\) (Corollary 2.4 and Lemma 2.3 of the Haar unitary lesson). The map \(\Psi(\xi_1,\dots,\xi_N)=\sum_iv_i\xi_i\) is a unitary of \((eHr)^N\) onto \(Hr\) and of \((eH)^N\) onto \(H\); its inverse is \(\eta\mapsto(v_i^*\eta)_i\). Put \(\widetilde T=\Psi T^{(N)}\Psi^{-1}\) on \(Hr\). Because \(G\) commutes with each \(L_{v_i}\), \(G|_{Hr}=\Psi G_e^{(N)}\Psi^{-1}\), so \(\|G|_{Hr}-\widetilde T\|=\|G_e-T\|\le c_0\varepsilon\). For \(a\in\mathcal L\), \(\Psi^{-1}L_a\Psi\) has matrix entries \(L_{v_i^*av_j}\) with \(v_i^*av_j\in e\mathcal Le\), so the intertwining property of \(T\) gives \(\widetilde TL_a=L_a\widetilde T\) on \(Hr\). Extend \(\widetilde T\) by \(0\) on \(H(1-r)\). The result commutes with every \(L_a\), so by the commutation theorem it is \(R_b\) for some \(b\in\mathcal L\); it vanishes on \(H(1-r)\), so \(b=rb\). This proves (1.1).

For \(G^*\): it commutes with \(L_D\), and \([G^*,L_x]=-[G,L_{x^*}]^*\) with \(x^*\in e\mathcal Le\) for \(x\in e\mathcal Le\), so \(G^*\) satisfies the same hypotheses. \(\square\)

## 2. Propagation along repeated letters

Fix \(s\in A_0\) with \(s=s^*=s^{-1}\) and \(\tau(s)=0\). Then \(s\in B^\circ\), \(\|s\|_2=1\), and \(s^{\otimes k}\otimes v\in J_k\) for \(v\in B\).

**Lemma 2.1** (propagation). For every \(k\ge1\) and \(v\in B\),
\[
\big\|B_k(s^{\otimes k}\otimes v)-s^{\otimes k}\otimes B_0v\big\|\le2c_0\varepsilon\|v\|_2 .
\tag{2.1}
\]
The same holds with \(B_k^*\) and \(B_0^*\) in place of \(B_k\) and \(B_0\).

**Proof.** First let \(v\in A_0\), \(v\ne0\). Let \(q\in D\) be a nonzero projection with \(a=\tau(q)\le t\). The left support of \(qv\) is at most \(q\), and its right support \(r\) is equivalent to the left support (Proposition 4.3 of the projections lesson), so \(\tau(r)\le a\le t\). Lemma 1.1 gives \(b=rb\) with \(\|(G-R_b)|_{Hr}\|\le c_0\varepsilon\). The vector \(qv=q\otimes v\) lies in \(\mathcal H_0\cap Hr\), and Theorem 7.1 of the previous lesson gives \(G(qv)=q\otimes B_0v=qB_0v\). Put
\[
y=qvb-qB_0v .
\]
Then \(qy=y\), and \(\|y\|_2=\|(R_b-G)(qv)\|_2\le c_0\varepsilon\|qv\|_2=c_0\varepsilon\sqrt a\,\|v\|_2\), because \(\|q\otimes v\|=\|q\|_2\|v\|_2\).

Let \(z\) be a Haar unitary of the corner \(qDq\) and \(x_n=a^{-1/2}z^n\) for \(n\ge1\). Then \(x_n\in D^\circ\), \(\|x_n\|_2=1\), \(x_n^*x_n=x_nx_n^*=a^{-1}q\), \(x_nq=x_n\), and \(x_n\to0\), \(x_n^*\to0\) weakly in \(E\), since the \(z^j\), \(j\in\mathbb Z\), are orthogonal of norm \(\sqrt a\). The vector
\[
\xi_n=(sx_n)^kv=1\otimes x_n^{\otimes k}\otimes(s^{\otimes k}\otimes v)\in\mathcal H_k
\]
has norm \(\|v\|_2\) and lies in \(Hr\), because its last \(D\)-letter satisfies \(x_n=x_nq\) and \(qvr=qv\). With \(A_n=(sx_n)^{k-1}s\),
\[
\xi_nb-(sx_n)^kB_0v=A_nx_n(qvb-qB_0v)=A_nx_ny .
\]
By Lemma 1.1, \(\|G\xi_n-\xi_nb\|\le c_0\varepsilon\|v\|_2\), hence
\[
\|G\xi_n-(sx_n)^kB_0v\|\le c_0\varepsilon\|v\|_2+\|A_nx_ny\|_2 .
\tag{2.2}
\]
By Theorem 7.1 of the previous lesson, \(G\xi_n=1\otimes x_n^{\otimes k}\otimes B_k(s^{\otimes k}\otimes v)\), while \((sx_n)^kB_0v=1\otimes x_n^{\otimes k}\otimes(s^{\otimes k}\otimes B_0v)\). Since \(\|1\|_2=\|x_n\|_2=1\), the left side of (2.2) equals \(\|B_k(s^{\otimes k}\otimes v)-s^{\otimes k}\otimes B_0v\|\) for every \(n\).

It remains to show \(\limsup_n\|A_nx_ny\|_2\le c_0\varepsilon\|v\|_2\). By Lemma 4.1 of the previous lesson, \(H=E\otimes\mathcal F\) with \(\mathcal F=\bigoplus_l(E^\circ)^{\otimes l}\otimes J_l\), and left multiplication by elements of \(D\) acts on the first factor. Let \(P_{\rm sc}\) be the projection onto \(\mathbb C1\otimes\mathcal F\). Then
\[
P_{\rm sc}(x_ny)=1\otimes(\ell_n\otimes I_{\mathcal F})y,\qquad \ell_n(\eta)=\langle x_n\eta,1\rangle=\langle\eta,x_n^*\rangle,\quad\|\ell_n\|=1 .
\]
Since \(x_n^*\to0\) weakly, \((\ell_n\otimes I)y\to0\) for finite sums of elementary tensors \(y\), and by uniform boundedness for every \(y\); so \(\|P_{\rm sc}(x_ny)\|\to0\). On \((1-P_{\rm sc})H=E^\circ\otimes\mathcal F\), the closed span of the words beginning with a centred \(D\)-letter, left multiplication by \(A_n\) prefixes the alternating word \(sx_ns\cdots x_ns\), whose letters have \(L^2\)-norm \(1\); by Theorem 1.3 of the free words lesson it acts isometrically there. On \(P_{\rm sc}H\) we use \(\|L_{A_n}\|\le\|A_n\|\le\|x_n\|^{k-1}=a^{-(k-1)/2}\). As \(qy=y\), \(\|x_ny\|_2^2=\langle x_n^*x_ny,y\rangle=a^{-1}\|y\|_2^2\). Therefore
\[
\|A_nx_ny\|_2\le\|(1-P_{\rm sc})x_ny\|_2+a^{-(k-1)/2}\|P_{\rm sc}x_ny\|_2\le a^{-1/2}\|y\|_2+a^{-(k-1)/2}\|P_{\rm sc}x_ny\|_2,
\]
and \(\limsup_n\|A_nx_ny\|_2\le a^{-1/2}\|y\|_2\le c_0\varepsilon\|v\|_2\). The numbers \(q,k,v,b,y\) are fixed while \(n\to\infty\), so the large factor \(a^{-(k-1)/2}\) does no harm. This proves (2.1) for bounded \(v\); both sides are continuous in \(v\in B\), and \(A_0\) is dense in \(B\). For the adjoints, apply the same argument to \(G^*\), using Lemma 1.1 for \(G^*\) and the second identity of Theorem 7.1 of the previous lesson. \(\square\)

## 3. Copies along the word levels and a compressed commutator

Choose a projection \(e\in D\) with \(\tau(e)=t\) and a projection \(p\in D\) with \(e\le p\) and \(\tau(p)=\frac12\); this is possible because \(t\le\frac12\). Put
\[
d=2p-1,\qquad w=ds,\qquad u=2t .
\tag{3.1}
\]
Then \(d\in D\) is a self-adjoint unitary with \(\tau(d)=0\), and \(w^{-1}=sd\). For \(k\ge0\) define
\[
U_k:B\to eH,\qquad U_kv=t^{-1/2}e\,(sd)^kv=(t^{-1/2}e)\otimes d^{\otimes k}\otimes(s^{\otimes k}\otimes v)\in\mathcal H_k .
\tag{3.2}
\]
Each \(U_k\) is an isometry, since \(\|t^{-1/2}e\|_2=\|d\|_2=\|s\|_2=1\), and the ranges lie in different levels, hence are orthogonal. Let \(\mathcal K\) be the closed span of the ranges, \(\iota:\mathcal K\to H\) the inclusion, and identify \(\mathcal K\) with \(\ell^2(\mathbb N_0)\otimes B\) through the \(U_k\), where \(\mathbb N_0=\{0,1,2,\dots\}\). Let \(J=I\otimes B_0\) on \(\mathcal K\).

**Lemma 3.1** (compressed commutator). For every \(h\in e\mathcal Le\),
\[
\big\|[J,\iota^*L_h\iota]\big\|\le(1+4c_0)\,\varepsilon\,\|h\| .
\tag{3.3}
\]

**Proof.** By Theorem 7.1 of the previous lesson, with \(d_0=t^{-1/2}e\) and the repeated letter \(d\in E^\circ\), and by Lemma 2.1,
\[
\|GU_kv-U_kB_0v\|_2=\|B_k(s^{\otimes k}\otimes v)-s^{\otimes k}\otimes B_0v\|\le2c_0\varepsilon\|v\|_2
\]
for \(k\ge1\), and \(GU_0v=U_0B_0v\). The error vectors for different \(k\) lie in different levels, so their squared norms add on finite sums \(\sum_kU_kv_k\). Hence, with the same argument for \(G^*\),
\[
R=G\iota-\iota J,\quad R'=G^*\iota-\iota J^*,\qquad \|R\|\le2c_0\varepsilon,\quad\|R'\|\le2c_0\varepsilon .
\]
Taking adjoints in the second identity gives \(\iota^*G=J\iota^*+R'^*\). With \(T_h=\iota^*L_h\iota\),
\[
\iota^*[G,L_h]\iota=\iota^*GL_h\iota-\iota^*L_hG\iota=[J,T_h]+R'^*L_h\iota-\iota^*L_hR .
\]
The left side has norm at most \(\varepsilon\|h\|\) by (1.1) of the previous lesson, and the last two terms have norms at most \(2c_0\varepsilon\|h\|\) each. \(\square\)

## 4. Exercises

**Exercise 4.1.** Let \(v\in\mathcal L\) be a partial isometry with \(v^*v=r\) and \(vv^*=r'\). Show directly that right multiplication by \(v\) maps \(Hr'\) isometrically onto \(Hr\).

**Exercise 4.2.** Show that a projection \(p\in D\) as in (3.1) exists, and that \(d=2p-1\) is a centred self-adjoint unitary.

**Exercise 4.3.** Using only freeness, compute \(\langle U_kv,U_jv'\rangle\) for \(v,v'\in A_0\) and show that it equals \(\delta_{kj}\langle v,v'\rangle\).

**Exercise 4.4.** In the proof of Lemma 2.1, let \(y=q\otimes f\) with \(f\in\mathcal F\). Compute \(P_{\rm sc}(x_ny)\) and \(\|A_nx_ny\|_2\) exactly.

## 5. Solutions

**Solution 4.1.** For bounded \(\xi\in Hr'\), \(\|\xi v\|_2^2=\tau(v^*\xi^*\xi v)=\tau(\xi^*\xi vv^*)=\tau(r'\xi^*\xi r')=\|\xi\|_2^2\), using \(\xi=\xi r'\). It maps into \(Hr\) because \(v=vr\). Right multiplication by \(v^*\) maps \(Hr\) back, and \(\xi vv^*=\xi r'=\xi\), \(\eta v^*v=\eta r=\eta\). Extend by continuity.

**Solution 4.2.** \(1-e\) is a projection of trace \(1-t\ge\frac12-t\ge0\) in the II\(_1\) factor \(D\), so it has a subprojection \(p'\) of trace \(\frac12-t\) (Corollary 2.4 of the Haar unitary lesson applied in the corner). Put \(p=e+p'\). Then \(d^2=4p-4p+1=1\), \(d^*=d\), and \(\tau(d)=2\cdot\frac12-1=0\).

**Solution 4.3.** \(\langle U_kv,U_jv'\rangle=t^{-1}\tau\big(v'^*(ds)^je(sd)^kv\big)\), and \(e=t1+e^\circ\) with \(e^\circ\in D^\circ\). In the term with \(e^\circ\), the letters between \(v'^*\) and \(v\) form the alternating word \(d\,s\cdots d\,s\,e^\circ\,s\,d\cdots s\,d\) of centred letters; writing \(v'^*\) and \(v\) as scalar plus centred parts turns the product into a combination of centred alternating words, so its trace is \(0\). The scalar term is \(t\,\tau(v'^*(ds)^j(sd)^kv)\). If \(k=j\), \((ds)^j(sd)^j=1\) and the term equals \(t\,\tau(v'^*v)\), so \(\langle U_kv,U_kv'\rangle=\tau(v'^*v)=\langle v,v'\rangle\). If \(k>j\), it equals \(t\,\tau(v'^*(sd)^{k-j}v)\); merge \(v'^*s\in A_0\) into one letter, \(v'^*s=\tau(v'^*s)1+(v'^*s)^\circ\), and centre \(v\): every resulting product is a centred alternating word containing at least one letter \(d\), so the trace is \(0\). The case \(k<j\) is the complex conjugate.

**Solution 4.4.** \(x_ny=x_nq\otimes f=x_n\otimes f\) and \(x_n\) is centred, so \(P_{\rm sc}(x_ny)=\tau(x_n)1\otimes f=0\), and \(x_ny\in E^\circ\otimes\mathcal F\). On this space \(L_{A_n}\) is isometric, so \(\|A_nx_ny\|_2=\|x_n\|_2\|f\|=\|f\|=a^{-1/2}\|y\|_2\).

## References

- [OpenAI-288] OpenAI, Kadison's similarity theorem through uniform derivation estimates, preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
