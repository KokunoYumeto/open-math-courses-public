# Words in free subalgebras

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two von Neumann subalgebras of a tracial von Neumann algebra are *free* when every alternating product of centred elements has trace zero. This condition determines the inner products of all alternating words, so the Hilbert space of the algebra the two subalgebras generate splits into tensor products of their centred \(L^2\)-spaces: the reduced-word model of Ching and of Voiculescu. Freeness and its basic properties are introduced in [Speicher]. The free-product estimates of the next three lessons are computations in this model. This lesson proves the facts they use: the inner product formula for words, the word decomposition, left multiplication by one of the two algebras, conditional expectations, automorphisms acting letter by letter, and freeness of conjugates by a free Haar unitary.

We use: the tracial calculus of Section 1 of [Haar unitaries, freeness and tracial ultraproducts](course:generators-of-ii1-factors/haar-unitaries-freeness-and-ultraproducts#1-tracial-von-neumann-algebras); trace-preserving conditional expectations, [Theorem 9.1 of Integration for a trace](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications#9-conditional-expectations-that-preserve-a-trace); and Kaplansky's density theorem, [Theorem 7.1 of its lesson](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07).

## 1. Freeness and the word decomposition

Throughout, \(L\) is a von Neumann algebra with a faithful normal tracial state \(\tau\), acting on \(L^2(L)\) with \(\langle x,y\rangle=\tau(y^*x)\) and \(\|x\|_2=\tau(x^*x)^{1/2}\). Subalgebras are von Neumann subalgebras containing \(1\). For a subalgebra \(Q\) write \(Q^\circ=\{x\in Q:\tau(x)=0\}\), \(L^2(Q)\) for the closure of \(Q\) in \(L^2(L)\), and \(L^2(Q)^\circ=L^2(Q)\ominus\mathbb C1\); \(Q^\circ\) is dense in \(L^2(Q)^\circ\). Left and right multiplication are \(L_x\xi=x\xi\) and \(R_x\xi=\xi x\).

**Definition 1.1.** Subalgebras \(Q_1,Q_2\subseteq L\) are *free* if \(\tau(x_1x_2\cdots x_n)=0\) whenever \(n\ge1\), \(x_j\in Q_{i_j}^\circ\) and \(i_j\ne i_{j+1}\) for \(1\le j<n\). Such a product is a *centred alternating word* of *type* \((i_1,\dots,i_n)\). The empty word is \(1\), of type \(\emptyset\).

Subalgebras of free subalgebras are free, directly from the definition.

**Lemma 1.2** (inner products of words). Let \(Q_1,Q_2\) be free, and let \(x=x_1\cdots x_n\) and \(y=y_1\cdots y_m\) be centred alternating words of types \((i_1,\dots,i_n)\) and \((k_1,\dots,k_m)\). Then \(\langle x,y\rangle=0\) unless the types are equal, and for equal types
\[
\langle x,y\rangle=\prod_{j=1}^n\tau(y_j^*x_j)=\prod_{j=1}^n\langle x_j,y_j\rangle .
\]

**Proof.** Induction on \(\min(n,m)\). If one word is empty and the other is not, \(\langle x,y\rangle\) is the trace of a nonempty centred alternating word or of its adjoint, hence \(0\). Let \(n,m\ge1\); then \(\langle x,y\rangle=\tau(y_m^*\cdots y_1^*x_1\cdots x_n)\). If \(i_1\ne k_1\), this is the trace of a centred alternating word, so it vanishes. If \(i_1=k_1\), write \(y_1^*x_1=z+\tau(y_1^*x_1)1\) with \(z\in Q_{i_1}^\circ\). The term with \(z\) is the trace of the centred alternating word \(y_m^*\cdots y_2^*\,z\,x_2\cdots x_n\), which is \(0\); the other term is \(\tau(y_1^*x_1)\langle x_2\cdots x_n,y_2\cdots y_m\rangle\). Apply the induction hypothesis. \(\square\)

For an alternating type \(\iota=(i_1,\dots,i_n)\) put
\[
\mathcal H_\iota=L^2(Q_{i_1})^\circ\otimes\cdots\otimes L^2(Q_{i_n})^\circ,\qquad \mathcal H_\emptyset=\mathbb C .
\]

**Theorem 1.3** (word decomposition). Let \(Q_1,Q_2\) be free subalgebras generating \(L\). There is a unique unitary
\[
W:\bigoplus_\iota\mathcal H_\iota\longrightarrow L^2(L),\qquad W(x_1\otimes\cdots\otimes x_n)=x_1x_2\cdots x_n,\quad W(1)=1,
\]
for centred letters \(x_j\in Q_{i_j}^\circ\), the sum running over all alternating types.

**Proof.** By Lemma 1.2, the prescribed map preserves inner products on finite sums of elementary tensors of bounded centred letters, and different types are orthogonal. These sums are dense in \(\bigoplus_\iota\mathcal H_\iota\), because \(Q_i^\circ\) is dense in \(L^2(Q_i)^\circ\); so \(W\) extends uniquely to an isometry. Its range contains the linear span \(\mathcal A\) of \(1\) and the centred alternating words. This span is a \(*\)-algebra: the adjoint of a word is a word, and the product of two words \(x_1\cdots x_n\) and \(y_1\cdots y_m\) is a word if \(x_n\) and \(y_1\) lie in different algebras, while otherwise \(x_ny_1=(x_ny_1-\tau(x_ny_1))+\tau(x_ny_1)1\) reduces it to a word plus a multiple of a shorter product, so induction on \(n+m\) applies. Every \(x\in Q_i\) is \(\tau(x)1+(x-\tau(x)1)\in\mathcal A\). So the weak closure of \(\mathcal A\) is \(L\), and by Kaplansky's density theorem every \(x\in L\) is the strong limit of a bounded net \(x_\alpha\in\mathcal A\); then \(x_\alpha=x_\alpha1\to x1=x\) in \(L^2(L)\). As \(L\) is dense in \(L^2(L)\), so is \(\mathcal A\), and \(W\) is unitary. \(\square\)

From now on we identify \(L^2(L)\) with \(\bigoplus_\iota\mathcal H_\iota\) through \(W\) and write \(\xi_1\otimes\cdots\otimes\xi_n\) for the image of an elementary tensor of arbitrary centred \(L^2\)-letters. For bounded letters this vector is the product \(\xi_1\cdots\xi_n\).

## 2. Multiplication by one of the algebras

Let \(Q_1,Q_2\) be free and generate \(L\). Let \(\mathcal F_1\) be the closed span of \(1\) and of the words of types beginning with \(2\), and \(\mathcal F_1^{\rm r}\) the closed span of \(1\) and of the words of types ending with \(2\).

**Lemma 2.1.** The map \(a\otimes w\mapsto aw\), for \(a\in Q_1\) and \(w\) equal to \(1\) or a bounded word of a type beginning with \(2\), extends to a unitary \(U_1:L^2(Q_1)\otimes\mathcal F_1\to L^2(L)\). For \(x\in Q_1\),
\[
L_xU_1=U_1(\lambda(x)\otimes I),
\]
where \(\lambda(x)\) is left multiplication by \(x\) on \(L^2(Q_1)\). Symmetrically, \(w\otimes a\mapsto wa\) gives a unitary \(\mathcal F_1^{\rm r}\otimes L^2(Q_1)\to L^2(L)\) carrying \(R_x\) to \(I\otimes\rho(x)\), with \(\rho(x)\) right multiplication on \(L^2(Q_1)\).

**Proof.** Split \(a=\tau(a)1+a^\circ\). Then \(aw=\tau(a)w+a^\circ w\), and \(a^\circ w\) is the word \(a^\circ\otimes w\) of a type beginning with \(1\). So, under Theorem 1.3, \(U_1\) is the identity on \(\mathbb C1\otimes\mathcal F_1=\mathcal F_1\) and the natural identification on \(L^2(Q_1)^\circ\otimes\mathcal F_1\), whose image is the closed span of the words beginning with \(1\). These two images are orthogonal and together exhaust all types, so \(U_1\) is unitary. For bounded \(a\) and \(w\), \(L_x(aw)=(xa)w=U_1(\lambda(x)a\otimes w)\); both sides are bounded in \(a\), so the identity extends. The right-hand version is the mirror image. \(\square\)

**Lemma 2.2** (conditional expectations). Let \(E_{Q_1}:L\to Q_1\) be the trace-preserving conditional expectation; on \(L^2(L)\) it extends to the orthogonal projection onto \(L^2(Q_1)\). This projection kills every word whose type contains the index \(2\). Consequently, if \(Q_1'\subseteq Q_1\) is a subalgebra and \(x\) lies in the von Neumann algebra generated by \(Q_1'\) and \(Q_2\), then \(E_{Q_1}(x)=E_{Q_1'}(x)\).

**Proof.** The first statement is Theorem 9.1 of the integration lesson. In the decomposition of Theorem 1.3, \(L^2(Q_1)=\mathcal H_\emptyset\oplus\mathcal H_{(1)}\), and all other types are orthogonal to it. For the last statement, apply Theorem 1.3 to the free pair \(Q_1',Q_2\): the vector \(x\in L^2(W^*(Q_1',Q_2))\) is a limit of combinations of \(1\) and words with letters in \(Q_1'^\circ\) and \(Q_2^\circ\). Its projection onto \(L^2(Q_1)\) therefore lies in the closed span of \(1\) and \(Q_1'^\circ\), which is \(L^2(Q_1')\). Since \(L^2(Q_1')\subseteq L^2(Q_1)\), the projection onto \(L^2(Q_1)\) of \(x\) equals its projection onto \(L^2(Q_1')\), that is, \(E_{Q_1'}(x)\). \(\square\)

## 3. Automorphisms acting letter by letter

**Proposition 3.1.** Let \(Q_1,Q_2\) be free and generate \(L\), and let \(\alpha_i\) be a trace-preserving \(*\)-automorphism of \(Q_i\) (\(i=1,2\)). There is a unitary \(W_\alpha\) on \(L^2(L)\) with
\[
W_\alpha(x_1\otimes\cdots\otimes x_n)=\alpha_{i_1}(x_1)\otimes\cdots\otimes\alpha_{i_n}(x_n),\qquad W_\alpha1=1,
\]
and a unique \(*\)-automorphism \(\alpha\) of \(L\) extending \(\alpha_1\) and \(\alpha_2\); it preserves \(\tau\), and \(W_\alpha L_xW_\alpha^*=L_{\alpha(x)}\) for \(x\in L\).

**Proof.** Each \(\alpha_i\) preserves the trace, hence centred elements and \(L^2\)-inner products, so it extends to a unitary \(V_i\) of \(L^2(Q_i)^\circ\). Put \(W_\alpha=\bigoplus_\iota V_{i_1}\otimes\cdots\otimes V_{i_n}\), a unitary by Theorem 1.3. Let \(x\in Q_1\) and let \(w=x_1\cdots x_n\) be a bounded word. If \(n=0\) or \(i_1=2\), then \(xw=\tau(x)w+x^\circ\otimes w\), and \(W_\alpha(xw)=\tau(x)W_\alpha w+\alpha_1(x^\circ)\otimes W_\alpha w=\alpha_1(x)W_\alpha w\), since \(\tau(\alpha_1(x))=\tau(x)\). If \(i_1=1\), then \(xw=(xx_1)^\circ\otimes x_2\cdots x_n+\tau(xx_1)x_2\cdots x_n\), and the same computation with \(\alpha_1(x)\alpha_1(x_1)=\alpha_1(xx_1)\) gives \(W_\alpha(xw)=\alpha_1(x)W_\alpha w\). Hence \(W_\alpha L_xW_\alpha^*=L_{\alpha_1(x)}\) on the dense span of words, and so everywhere; similarly for \(Q_2\). The same holds for \(W_\alpha^*\), which is the unitary built from \(\alpha_1^{-1},\alpha_2^{-1}\). The normal \(*\)-automorphism \(\operatorname{Ad}W_\alpha\) of \(B(L^2(L))\) therefore maps the von Neumann algebra \(\{L_x:x\in L\}\), generated by \(L_{Q_1}\cup L_{Q_2}\), onto itself, and \(L_{\alpha(x)}=W_\alpha L_xW_\alpha^*\) defines a \(*\)-automorphism \(\alpha\) of \(L\) extending \(\alpha_1,\alpha_2\). It preserves the trace, because \(\tau(\alpha(x))=\langle W_\alpha L_xW_\alpha^*1,1\rangle=\langle x1,1\rangle\) as \(W_\alpha^*1=1\). An automorphism is determined by its values on generators, which gives uniqueness. \(\square\)

## 4. Conjugation by a free Haar unitary

A unitary \(u\in L\) is a *Haar unitary* if \(\tau(u^k)=0\) for every integer \(k\ne0\).

**Lemma 4.1.** Let \(P\subseteq L\) be a subalgebra and \(u\in L\) a Haar unitary such that \(W^*(u)\) and \(P\) are free. For every subalgebra \(B\subseteq P\), the subalgebras \(uBu^*\) and \(P\) are free.

**Proof.** The centred elements of \(uBu^*\) are the \(ubu^*\) with \(b\in B^\circ\), since \(\tau(ubu^*)=\tau(b)\). In a centred alternating word in \(uBu^*\) and \(P\), replace each letter \(ubu^*\) by the three letters \(u,b,u^*\). The result is a product of letters that alternate between \(W^*(u)\) and \(P\): between two letters \(ubu^*\) and \(ub'u^*\) there is a centred letter \(p\in P^\circ\), giving \(\cdots u^*\,p\,u\cdots\), and inside each letter \(u\) and \(u^*\) surround \(b\in P^\circ\). The letters \(u\) and \(u^*\) are centred elements of \(W^*(u)\). So the product is a centred alternating word in \(W^*(u)\) and \(P\), and its trace is \(0\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(Q_1,Q_2\) be free, \(a_1,a_2\in Q_1\) and \(b_1,b_2\in Q_2\). Show that
\[
\tau(a_1b_1a_2b_2)=\tau(a_1a_2)\tau(b_1)\tau(b_2)+\tau(a_1)\tau(a_2)\tau(b_1b_2)-\tau(a_1)\tau(a_2)\tau(b_1)\tau(b_2).
\]

**Exercise 5.2.** Let \(Q_1,Q_2\) be free and \(a_1,a_2\in Q_1^\circ\), \(b\in Q_2^\circ\). Show that \(E_{Q_1}(a_1ba_2)=0\) and \(E_{Q_1}(ba_1b^*)=0\), and that \(E_{Q_1}(b^*ab)=\tau(a)\tau(b^*b)1\) for every \(a\in Q_1\).

**Exercise 5.3.** In Proposition 3.1 take \(\alpha_2=\mathrm{id}\). Show that \(W_\alpha\) fixes \(L^2(Q_2)\) pointwise and commutes with \(L_y\) for every \(y\in Q_2\), and that \(W_\alpha\) commutes with \(L_x\) for every \(x\in Q_1\) only if \(\alpha_1=\mathrm{id}\).

**Exercise 5.4.** Let \(u,v\in L\) be Haar unitaries with \(W^*(u)\) and \(W^*(v)\) free. Show that \(uv\) is a Haar unitary.

## 6. Solutions

**Solution 5.1.** Write \(a_j=\tau(a_j)+a_j^\circ\) and \(b_j=\tau(b_j)+b_j^\circ\) and expand. Terms containing a centred letter isolated between scalars, or forming a centred alternating word, vanish. The surviving terms are: \(\tau(a_1)\tau(a_2)\tau(b_1)\tau(b_2)\) (all scalar), \(\tau(a_1^\circ a_2^\circ)\tau(b_1)\tau(b_2)\) and \(\tau(a_1)\tau(a_2)\tau(b_1^\circ b_2^\circ)\); the term \(\tau(a_1^\circ b_1^\circ a_2^\circ b_2^\circ)\) is a centred alternating word, and terms such as \(\tau(a_1^\circ b_1^\circ a_2^\circ)\tau(b_2)\) vanish for the same reason. Using \(\tau(a_1^\circ a_2^\circ)=\tau(a_1a_2)-\tau(a_1)\tau(a_2)\) and the analogue for the \(b\)'s gives the formula.

**Solution 5.2.** \(a_1ba_2\) is a word of type \((1,2,1)\), so Lemma 2.2 gives \(E_{Q_1}(a_1ba_2)=0\). Since \(\tau(b^*)=\overline{\tau(b)}=0\), \(ba_1b^*\) is a word of type \((2,1,2)\), so its expectation is \(0\). For \(a\in Q_1\), \(b^*ab=\tau(a)b^*b+b^*a^\circ b\); the second term is a word of type \((2,1,2)\), and \(b^*b=\tau(b^*b)1+(b^*b)^\circ\) with \((b^*b)^\circ\in Q_2^\circ\) gives \(E_{Q_1}(b^*b)=\tau(b^*b)1\). So \(E_{Q_1}(b^*ab)=\tau(a)\tau(b^*b)1\).

**Solution 5.3.** \(L^2(Q_2)=\mathcal H_\emptyset\oplus\mathcal H_{(2)}\), on which \(W_\alpha\) acts by \(V_2=I\). By Proposition 3.1, \(W_\alpha L_yW_\alpha^*=L_{\alpha(y)}=L_y\) for \(y\in Q_2\). For \(x\in Q_1\), \(W_\alpha L_xW_\alpha^*=L_{\alpha_1(x)}\); if this equals \(L_x\) for all \(x\), then \(\alpha_1(x)=L_{\alpha_1(x)}1=L_x1=x\).

**Solution 5.4.** For \(k\ge1\), \((uv)^k=uvuv\cdots uv\) is a centred alternating word in \(W^*(u)\) and \(W^*(v)\) (the letters \(u\) and \(v\) are centred because they are Haar unitaries), so \(\tau((uv)^k)=0\); and \(\tau((uv)^{-k})=\overline{\tau((uv)^k)}=0\).

## References

- [OpenAI-288] OpenAI, Kadison's similarity theorem through uniform derivation estimates, preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
- [Speicher] R. Speicher, Lecture notes on "Free probability theory", 2019 (freeness and its basic properties). https://arxiv.org/abs/1908.08125
