# Exact counts and a quadratic estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The comparison theorem of [Finite quotients and the comparison theorem](finite-quotients-and-the-comparison-theorem.md) labels the edges of a generator graph by unit quaternions and compares the products of the labels along the words of a list \(\mathcal D\) with the products along the relators of a presentation. The aligned presentation of [Aligned presentations of the cycle module](aligned-presentations-of-the-cycle-module.md) has, for every word \(z\in\mathcal D\), a distinguished relator \(\rho_z\) with the same chain as \(z\), but not with the same letters in the same order, and unit quaternions do not commute. This lesson shows that the two products nevertheless agree to second order [OpenAI-EG, Section 3.2]. Behind this is an exact identity of chains: in an expression of \(z\) as a product of conjugates of relators, the signed number of occurrences of each relator at each translate is prescribed, and it is \(1\) for \(\rho_z\) at the starting point and \(0\) for everything else. Since unit quaternions near \(1\) commute up to a quadratic error, the product along \(z\) differs from the product along \(\rho_z\) by a quadratic error. At the end, two numbers \(\delta\) and \(\eta\) are fixed for which the products along the distinguished relators can never have distance exactly \(\delta\) from \(1\) while the labels of the original letters stay within \(\eta\) of \(1\).

- Labels and products along words (Section 1).
- Exact counts (Section 2).
- The uniform estimate (Section 3).
- A forbidden value (Section 4).

We use, from [Aligned presentations of the cycle module](aligned-presentations-of-the-cycle-module.md), chains of words (Lemma 1.1), presentations with the basis property (Section 2) and the aligned presentation (Lemma 4.1); from [Word maps on unit quaternions and degree](word-maps-on-unit-quaternions-and-degree.md), the group \(H\) of unit quaternions with the distance \(|a-b|\) and the estimates of its Lemma 1.1.

## 1. Labels and products along words

Throughout the lesson, \(\Gamma\), its finite generating alphabet \(S\), the finite list \(\mathcal D\) of words on \(S\) and the presentation
\[
\Gamma=\bigl\langle S,\mathcal T\bigm|(\rho_z)_{z\in\mathcal D},\ (r)_{r\in\mathcal R}\bigr\rangle
\]
are those of Lemma 4.1 of the lesson on aligned presentations: it has the basis property, every letter of \(\mathcal T\) has value \(1\), and \([\rho_z]=[z]\) for every \(z\in\mathcal D\). Write \(A=S\amalg\mathcal T\), \(\Lambda=\mathbb Z\Gamma\), and \(\bar w\in\Gamma\) for the value of a word \(w\) on the letters of \(A\) and their inverses. Relators are indexed: \(r\) denotes both an index in \(\mathcal D\amalg\mathcal R\) and the word with that index, and \(\rho_z\) has the index \(z\).

A *quotient* of \(\Gamma\) is either \(\Gamma\) itself or a finite group \(F=\Gamma/N\) for a normal subgroup \(N\) of finite index; write \(\pi\colon\Gamma\to F\) for the quotient map, the identity when \(F=\Gamma\). The *generator graph over \(F\)* has vertex set \(F\) and, for every \(f\in F\) and \(a\in A\), an edge \((f,a)\) from \(f\) to \(f\pi(\bar a)\). Distinct letters give distinct edges even when their values in \(F\) coincide, and the edges of the letters of \(\mathcal T\) are loops.

A *labelling* is a map \(\ell\) from the edges to \(H\). For a word \(w\) and a vertex \(v\in F\), the *product along \(w\) from \(v\)*, \(L(w,v)\in H\), is defined by induction on the length: \(L(\varnothing,v)=1\), and for a letter \(a\) and a word \(w'\),
\[
L(aw',v)=\ell(v,a)\,L\bigl(w',v\pi(\bar a)\bigr),\qquad L(a^{-1}w',v)=\ell\bigl(v\pi(\bar a)^{-1},a\bigr)^{-1}L\bigl(w',v\pi(\bar a)^{-1}\bigr).
\]
So \(L(w,v)\) is the product, in the order of traversal, of the labels along the path that reads \(w\) from \(v\), an edge traversed backwards contributing the inverse of its label. Which edges the path traverses depends only on the values of the letters, not on the labels.

**Lemma 1.1** (products along words). Let \(u,w,w_1,\ldots,w_n\) be words and \(v\in F\).

1. \(L(uw,v)=L(u,v)\,L\bigl(w,v\pi(\bar u)\bigr)\).
2. \(L(u^{-1},v)=L\bigl(u,v\pi(\bar u)^{-1}\bigr)^{-1}\).
3. \(L(w,v)\) depends only on the element of the free group on \(A\) represented by \(w\).
4. If \(\bar r=1\) and \(\sigma\in\{1,-1\}\), then \(L(ur^\sigma u^{-1},v)=L(u,v)\,L\bigl(r,v\pi(\bar u)\bigr)^\sigma\,L(u,v)^{-1}\).
5. If \(\bar w_1=\cdots=\bar w_n=1\), then \(L(w_1\cdots w_n,v)=L(w_1,v)\cdots L(w_n,v)\).

*Proof.* (1) By induction on the length of \(u\), directly from the definition.

(2) By induction on the length of \(u\). For a letter, \(L(a^{-1},v)=\ell(v\pi(\bar a)^{-1},a)^{-1}=L(a,v\pi(\bar a)^{-1})^{-1}\). If \(u=u'a\), then by (1), the case of a letter and the induction hypothesis,
\[
L(u^{-1},v)=L(a^{-1},v)\,L\bigl(u'^{-1},v\pi(\bar a)^{-1}\bigr)=L\bigl(a,v\pi(\bar a)^{-1}\bigr)^{-1}L\bigl(u',v\pi(\bar u)^{-1}\bigr)^{-1},
\]
and this is the inverse of \(L(u',x)L(a,x\pi(\bar u'))=L(u,x)\) for \(x=v\pi(\bar u)^{-1}\), since \(x\pi(\bar u')=v\pi(\bar a)^{-1}\). If \(u=u'a^{-1}\), the same computation applies with \(a^{-1}\) in place of \(a\).

(3) By (1) and (2), \(L(aa^{-1},x)=L(a,x)L(a,x)^{-1}=1\) and \(L(a^{-1}a,x)=L(a,x\pi(\bar a)^{-1})^{-1}L(a,x\pi(\bar a)^{-1})=1\) for every vertex \(x\). By (1), inserting or deleting \(aa^{-1}\) or \(a^{-1}a\) anywhere in a word therefore does not change the product.

(4) By (1) and (2), \(L(ur^\sigma u^{-1},v)=L(u,v)\,L(r^\sigma,v\pi(\bar u))\,L(u^{-1},v\pi(\bar u))\), since \(\bar r^\sigma=1\); the last factor is \(L(u,v)^{-1}\) by (2). For \(\sigma=-1\), (2) gives \(L(r^{-1},x)=L(r,x\pi(\bar r)^{-1})^{-1}=L(r,x)^{-1}\).

(5) By (1), since every prefix \(w_1\cdots w_k\) has value \(1\). \(\square\)

## 2. Exact counts

Every word \(z\in\mathcal D\) has value \(1\), so it lies in the kernel of the map from the free group on \(A\) to \(\Gamma\), which is the normal closure of the relators. For every \(z\in\mathcal D\) we choose an expression
\[
z=\prod_{j=1}^{n_z}u_{z,j}\,r_{z,j}^{\sigma_{z,j}}\,u_{z,j}^{-1}\tag{2.1}
\]
in the free group on \(A\), with words \(u_{z,j}\), relator indices \(r_{z,j}\in\mathcal D\amalg\mathcal R\) and signs \(\sigma_{z,j}\in\{1,-1\}\). The relators occurring may be distinguished or ordinary. Let \(\Lambda^{(\mathcal D\amalg\mathcal R)}\) be the free module on all relator indices, with basis vectors \(e_r\), and let
\[
\partial_2\colon\Lambda^{(\mathcal D\amalg\mathcal R)}\to\Lambda^{(A)},\qquad e_r\mapsto[r],
\]
be the relator boundary map; by the basis property it is injective.

**Lemma 2.1** (exact counts; [OpenAI-EG, Lemma 3.3]). For every \(z\in\mathcal D\),
\[
\sum_{j=1}^{n_z}\sigma_{z,j}\,\bar u_{z,j}\,e_{r_{z,j}}=e_{\rho_z}\qquad\text{in }\Lambda^{(\mathcal D\amalg\mathcal R)}.\tag{2.2}
\]

*Proof.* Write \(c_j=u_{z,j}r_{z,j}^{\sigma_{z,j}}u_{z,j}^{-1}\). By Lemma 1.1 (3) of the lesson on aligned presentations, \([z]\) is the chain of the product \(c_1\cdots c_{n_z}\). Each \(c_j\) has value \(1\), so by Lemma 1.1 (1) there the chain of the product is \(\sum_j[c_j]\), and by Lemma 1.1 (2) there \([c_j]=\sigma_{z,j}\bar u_{z,j}[r_{z,j}]\). Hence \(\partial_2\) maps the left side of (2.2) to \([z]\). It maps the right side to \([\rho_z]=[z]\). Since \(\partial_2\) is injective, the two sides agree. \(\square\)

The word \(z\) uses only letters of \(S\); its chain in the generator graph of \(A\) has the coordinates of its chain in the generator graph of \(S\) on the \(S\)-edges and \(0\) on the \(\mathcal T\)-edges. Comparing the coefficients of each basis vector in (2.2), and mapping them to a quotient, gives the counts in the form used below.

**Corollary 2.2** (counts on quotients). Let \(F\) be a quotient of \(\Gamma\), \(z\in\mathcal D\), \(r\in\mathcal D\amalg\mathcal R\) and \(f\in F\). Then
\[
\sum_{\substack{1\le j\le n_z\\ r_{z,j}=r,\ \pi(\bar u_{z,j})=f}}\sigma_{z,j}=\begin{cases}1&\text{if }r=\rho_z\text{ and }f=1,\\0&\text{otherwise.}\end{cases}
\]

*Proof.* The coefficient of \(e_r\) on the left of (2.2) is \(\sum_{j:\,r_{z,j}=r}\sigma_{z,j}\bar u_{z,j}\in\mathbb Z\Gamma\), and on the right it is \(1\) if \(r=\rho_z\) and \(0\) otherwise. Apply the ring homomorphism \(\mathbb Z\Gamma\to\mathbb ZF\) induced by \(\pi\) and read off the coefficient of \(f\). \(\square\)

Two further finite choices complete the data. Let \(\mathcal T_0\subseteq\mathcal T\) be the finite set of letters of \(\mathcal T\) that occur in the words \(u_{z,j}\). Every \(t\in\mathcal T_0\) has value \(1\), so we may choose an expression
\[
t=\prod_{k=1}^{m_t}u'_{t,k}\,r'^{\,\sigma'_{t,k}}_{t,k}\,u'^{-1}_{t,k}\tag{2.3}
\]
of the same kind. Let \(\mathcal A\subseteq\mathcal R\) be the finite set of the ordinary relators that occur in the expressions (2.1) and (2.3). The expressions (2.1) and (2.3), the set \(\mathcal T_0\) and the set \(\mathcal A\) are fixed for the rest of the course.

## 3. The uniform estimate

**Lemma 3.1** (uniform estimate; [OpenAI-EG, Lemma 3.4]). There is a constant \(C\ge1\), depending only on the choices of Section 2, with the following property. Let \(F\) be a quotient of \(\Gamma\), \(\ell\) a labelling of the generator graph over \(F\), and \(\epsilon\ge0\), such that

- (a) \(|\ell(f,s)-1|\le\epsilon\) for every \(f\in F\) and \(s\in S\), and
- (b) \(L(r,f)=1\) for every \(r\in\mathcal A\) and \(f\in F\).

Let \(h=\sup_{z\in\mathcal D,\ f\in F}|L(\rho_z,f)-1|\), with \(h=0\) if \(\mathcal D\) is empty. Then for every \(z\in\mathcal D\) and every \(v\in F\),
\[
\begin{aligned}
|L(z,v)-L(\rho_z,v)|&\le C(h+\epsilon)h,\\
|L(z,v)-1|&\le C\epsilon.
\end{aligned}\tag{3.1}
\]

*Proof.* If \(\mathcal D\) is empty there is nothing to prove. We use the estimates of Lemma 1.1 of the lesson on word maps: for unit quaternions,
\[
\Bigl|\prod_{j=1}^na_j-\prod_{j=1}^nb_j\Bigr|\le\sum_{j=1}^n|a_j-b_j|,\qquad|ab-ba|\le2|a-1|\,|b-1|,\qquad|a^{-1}-1|=|a-1|=|gag^{-1}-1|.\tag{3.2}
\]

*Step 1: the loop labels.* Let \(t\in\mathcal T_0\) and \(x\in F\). The edge \((x,t)\) is a loop, so \(\ell(x,t)=L(t,x)\), and by Lemma 1.1 (3), (5) and (4), applied to (2.3),
\[
\ell(x,t)=\prod_{k=1}^{m_t}L(u'_{t,k},x)\,L\bigl(r'_{t,k},x\pi(\bar u'_{t,k})\bigr)^{\sigma'_{t,k}}\,L(u'_{t,k},x)^{-1}.
\]
A factor whose relator is ordinary is \(1\) by (b). A factor whose relator is distinguished is a conjugate of an element at distance at most \(h\) from \(1\), or of its inverse, and so has distance at most \(h\) from \(1\) by (3.2). By the first estimate of (3.2), \(|\ell(x,t)-1|\le Mh\), where \(M\) is the largest number \(m_t\), \(t\in\mathcal T_0\) (or \(M=0\) if \(\mathcal T_0\) is empty).

*Step 2: the conjugators.* The words \(u_{z,j}\) use letters of \(S\amalg\mathcal T_0\) only. The product along \(u_{z,j}\) from any vertex is a product of labels of such letters and their inverses, so by Step 1, (a) and (3.2),
\[
|L(u_{z,j},x)-1|\le K(\epsilon+h)\qquad(x\in F),
\]
where \(K\) is \(\max(1,M)\) times the largest length of the words \(u_{z,j}\).

*Step 3: removing the conjugations.* Fix \(z\in\mathcal D\) and \(v\in F\), and write \(u_j=u_{z,j}\), \(r_j=r_{z,j}\), \(\sigma_j=\sigma_{z,j}\) and \(n=n_z\). By Lemma 1.1 (3), (5) and (4), applied to (2.1),
\[
L(z,v)=\prod_{j=1}^na_jb_ja_j^{-1},\qquad a_j=L(u_j,v),\quad b_j=L\bigl(r_j,v\pi(\bar u_j)\bigr)^{\sigma_j}.
\]
If \(r_j\) is ordinary, then \(r_j\in\mathcal A\) and \(b_j=1\) by (b), so the factor is \(1\). Let \(J\) be the set of the indices \(j\) with \(r_j\) distinguished; for them \(|b_j-1|\le h\), and by (3.2) and Step 2,
\[
|a_jb_ja_j^{-1}-b_j|=|a_jb_j-b_ja_j|\le2|a_j-1|\,|b_j-1|\le2K(\epsilon+h)h .
\]
By the first estimate of (3.2), \(\bigl|L(z,v)-\prod_{j\in J}b_j\bigr|\le2nK(\epsilon+h)h\), the product taken in increasing order of \(j\).

*Step 4: sorting.* Call \(\bigl(r_j,\pi(\bar u_j)\bigr)\) the *type* of the index \(j\in J\). Reorder the product \(\prod_{j\in J}b_j\) by interchanges of adjacent factors until the factors of each type are adjacent; at most \(n(n-1)/2\) interchanges are needed. By bi-invariance and (3.2), interchanging two adjacent factors \(x,y\) changes the product by \(|xy-yx|\le2|x-1|\,|y-1|\le2h^2\). After sorting, the factors of the type \((\rho,f)\) all equal \(L(\rho,v f)^{\pm1}\), with the signs \(\sigma_j\), so they multiply to \(L(\rho,vf)^{c}\), where \(c\) is the sum of the \(\sigma_j\) over the indices of that type. By Corollary 2.2, \(c=1\) for the type \((\rho_z,1)\) and \(c=0\) for every other type. So the sorted product is \(L(\rho_z,v)\), and
\[
|L(z,v)-L(\rho_z,v)|\le2nK(\epsilon+h)h+n(n-1)h^2\le\bigl(2nK+n(n-1)\bigr)(h+\epsilon)h .
\]

*Step 5: the second inequality.* The word \(z\) uses letters of \(S\) only, so by (a) and (3.2), \(|L(z,v)-1|\le|z|\epsilon\), where \(|z|\) is the length of \(z\).

Both inequalities of (3.1) hold with \(C=\max\bigl(1,\ \max_{z}(2n_zK+n_z(n_z-1)),\ \max_z|z|\bigr)\), which depends only on the choices of Section 2. \(\square\)

The constant does not depend on the quotient \(F\), on the labelling or on \(\epsilon\). This uniformity is what the next lesson needs: it applies the estimate on infinitely many finite quotients, and on \(\Gamma\) itself.

## 4. A forbidden value

Fix, for the rest of the course, numbers \(0<\delta<1\) and \(0<\eta<1\) with
\[
C(\delta+\eta)<\tfrac12,\qquad C\eta<\tfrac\delta2,\tag{4.1}
\]
for the constant \(C\) of Lemma 3.1; for example \(\delta=1/(4C)\) and \(\eta=1/(16C^2)\) (Exercise 5.3).

**Corollary 4.1** (a forbidden value; [OpenAI-EG, Section 3.2]). Under the hypotheses of Lemma 3.1, with \(\epsilon\le\eta\), the number \(h\) is different from \(\delta\). If \(h<\delta\), then moreover \(h\le2C\epsilon\).

*Proof.* For every \(z\in\mathcal D\) and \(v\in F\), the two inequalities (3.1) give
\[
|L(\rho_z,v)-1|\le|L(\rho_z,v)-L(z,v)|+|L(z,v)-1|\le C(h+\epsilon)h+C\epsilon .
\]
Taking the supremum over \(z\) and \(v\), \(h\le C(h+\epsilon)h+C\epsilon\). If \(h=\delta\), this gives \(\delta\le C(\delta+\eta)\delta+C\eta<\frac\delta2+\frac\delta2=\delta\), which is impossible. If \(h<\delta\), then \(C(h+\epsilon)\le C(\delta+\eta)<\frac12\), so \(h\le\frac h2+C\epsilon\), that is, \(h\le2C\epsilon\). \(\square\)

The supremum \(h\) need not be attained. On a finite quotient it is a maximum of finitely many products, which depend continuously on the labels. The next lesson moves labels continuously, starting from the labelling with all labels \(1\), where \(h=0\); since the value \(\delta\) can never be taken, \(h\) stays below \(\delta\), and by the corollary the products along the distinguished relators then stay within \(2C\epsilon\) of \(1\).

## 5. Exercises

**5.1** (easy). Verify Lemma 1.1 (2) directly for the word \(u=ab\) of two letters, by writing out the path that reads \(b^{-1}a^{-1}\).

**5.2** (medium). For a letter \(a\in A\) define the *Fox derivative* \(\partial w/\partial a\in\mathbb ZF(A)\) of an element \(w\) of the free group \(F(A)\) by \(\partial a/\partial a=1\), \(\partial b/\partial a=0\) for letters \(b\ne a\), and \(\partial(uw)/\partial a=\partial u/\partial a+u\,\partial w/\partial a\). Show that \(\partial a^{-1}/\partial a=-a^{-1}\), and that the coefficient of \(e_a\) in the chain \([w]\) is the image of \(\partial w/\partial a\) under the ring homomorphism \(\mathbb ZF(A)\to\mathbb Z\Gamma\) induced by the values.

**5.3** (easy). Show that \(\delta=1/(4C)\) and \(\eta=1/(16C^2)\) satisfy (4.1) for every \(C\ge1\).

**5.4** (medium). Let \(0<\theta<\pi/2\), \(a=\cos\theta+i\sin\theta\) and \(b=\cos\theta+j\sin\theta\). Compute \(|ab-ba|\) and \(2|a-1|\,|b-1|\), and show that their ratio tends to \(1\) as \(\theta\to0\). Conclude that the sorting step of Lemma 3.1 cannot do better than an error of order \(h^2\) for each interchange.

**5.5** (medium). In Lemma 3.1, suppose that the presentation has no letters \(\mathcal T\) and no ordinary relators, and that every word \(z\in\mathcal D\) is one of the relators, \(z=\rho_z\). Show that the expression \(z=\rho_z\) (one factor, empty conjugator, sign \(1\)) gives \(|L(z,v)-L(\rho_z,v)|=0\), and find the constant \(C\) produced by the proof.

## 6. Solutions

**5.1.** The path reading \(b^{-1}a^{-1}\) from \(v\) first traverses the edge \((v\pi(\bar b)^{-1},b)\) backwards and then the edge \((v\pi(\bar b)^{-1}\pi(\bar a)^{-1},a)\) backwards, so \(L(b^{-1}a^{-1},v)=\ell(v\pi(\bar b)^{-1},b)^{-1}\ell(x,a)^{-1}\) with \(x=v\pi(\bar a\bar b)^{-1}\). On the other hand \(L(ab,x)=\ell(x,a)\ell(x\pi(\bar a),b)\), and \(x\pi(\bar a)=v\pi(\bar b)^{-1}\); so \(L(ab,x)^{-1}\) is the same product.

**5.2.** From \(0=\partial(a^{-1}a)/\partial a=\partial a^{-1}/\partial a+a^{-1}\) we get \(\partial a^{-1}/\partial a=-a^{-1}\). Both sides of the claim are additive in the same way: \([uw]=[u]+\bar u[w]\) by Lemma 1.1 (1) of the lesson on aligned presentations, and the product rule of the Fox derivative has the same form. They agree on letters, \([b]=e_b\), and on inverse letters, \([a^{-1}]=-\bar a^{-1}e_a\), so by induction on the length they agree on all words, and both depend only on the element of the free group.

**5.3.** \(C(\delta+\eta)=\frac14+\frac1{16C}\le\frac14+\frac1{16}<\frac12\), and \(C\eta=\frac1{16C}<\frac1{8C}=\frac\delta2\).

**5.4.** \(ab=\cos^2\theta+(i+j)\sin\theta\cos\theta+k\sin^2\theta\) and \(ba=\cos^2\theta+(i+j)\sin\theta\cos\theta-k\sin^2\theta\), since \(ji=-k\). So \(|ab-ba|=2\sin^2\theta\). Further \(|a-1|^2=(1-\cos\theta)^2+\sin^2\theta=4\sin^2(\theta/2)\), so \(2|a-1|\,|b-1|=8\sin^2(\theta/2)\). The ratio is \(\sin^2\theta/(4\sin^2(\theta/2))=\cos^2(\theta/2)\to1\). With \(h=|a-1|=|b-1|\), one interchange of \(a\) and \(b\) costs \(\cos^2(\theta/2)\cdot2h^2\).

**5.5.** Here \(n_z=1\), the conjugator is empty, so \(\mathcal T_0\) is empty, \(M=0\), \(K=\max(1,0)\cdot0=0\), and Steps 3 and 4 give the error \(2\cdot1\cdot0+0=0\). The proof gives \(C=\max(1,\max_z|z|)\), the largest length of a word of \(\mathcal D\) (or \(1\)).

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 3.2. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
