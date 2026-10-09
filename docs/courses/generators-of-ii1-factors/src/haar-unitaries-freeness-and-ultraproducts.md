# Haar unitaries, freeness and tracial ultraproducts

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This course proves that every factor of type II₁ with separable predual is generated, as a von Neumann algebra, by a single operator. The proof works with unitaries that behave like free group generators relative to a given algebra, and it constructs them in a tracial ultraproduct. This first lesson collects the tools: norm inequalities in a tracial algebra, Haar unitaries and the decay of their correlations, a working criterion for freeness of a unitary from a C\*-algebra with an absorption lemma, and the facts about tracial ultraproducts that the later lessons use.

We use: Theorem 3.2 of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#3-ultraproducts-of-finite-von-neumann-algebras), which shows that a tracial ultraproduct is a von Neumann algebra with a faithful normal tracial state, and Lemma 1.4 of that lesson ([Section 1](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#1-conventions-ultrafilters-the-bimodule-of-normal-functionals--strong-convergence)), completeness of the unit ball for the trace norm; Lemma 55.1 of [Finite Fourier bases produce one small quantized corner](course:OA-SUBFACTORS/html/finite-phase-local-quantization#a-diffuse-diagonal-supplies-exact-scalar-dimensions), a maximal abelian subalgebra of a II₁ factor with projections of every trace; the polar decomposition inside a von Neumann algebra, [The double commutant theorem, Section 7](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#OA-FND-BI-09); the comparison theorem for projections, [Projections and types of von Neumann algebras, Section 5](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-03); Kaplansky's density theorem, [Section 7 of its lesson](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07); and the trace-preserving conditional expectation, Theorem 9.1 of [Integration for a trace](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications#9-conditional-expectations-that-preserve-a-trace).

## 1. Tracial von Neumann algebras

A *tracial von Neumann algebra* \((M,\tau)\) is a von Neumann algebra \(M\) with a faithful normal tracial state \(\tau\). Put
\[
\|x\|_2=\tau(x^*x)^{1/2},\qquad \|x\|_1=\tau(|x|),\qquad \langle a,b\rangle=\tau(b^*a),
\]
and let \(L^2(M)\) be the completion of \(M\) for \(\|\cdot\|_2\); \(M\) acts on it by left multiplication, and \(\|x\|\) denotes the operator norm. A *II₁ factor* is a factor with a faithful normal tracial state and no nonzero abelian projection. For a subset \(S\subseteq M\), \(W^*(S)\) is the smallest von Neumann subalgebra of \(M\) containing \(S\) and \(1\); \(C^*(S)\) is the smallest unital C\*-subalgebra containing \(S\).

**Lemma 1.1.** Let \(a,b,c\in M\).

1. \(|\tau(ab)|\le\|a\|_2\|b\|_2\) and \(\|abc\|_2\le\|a\|\,\|b\|_2\,\|c\|\).
2. \(|\tau(ab)|\le\|a\|\,\|b\|_1\), and \(\|b\|_1=\max\{|\tau(db)|:\|d\|\le1\}\). Consequently \(\|abc\|_1\le\|a\|\,\|b\|_1\,\|c\|\).
3. \(\|b\|_1\le\|b\|_2\). If \(b=bq\) for a projection \(q\), then \(\|b\|_1\le\tau(q)^{1/2}\|b\|_2\).

**Proof.** (1) The first inequality is the Cauchy–Schwarz inequality for the positive form \((a,b)\mapsto\tau(b^*a)\), applied to \(a\) and \(b^*\). For the second, \(a^*a\le\|a\|^21\) gives \(\|ab\|_2^2=\tau(b^*a^*ab)\le\|a\|^2\tau(b^*b)\), and \(\|bc\|_2=\|c^*b^*\|_2\le\|c\|\,\|b^*\|_2=\|c\|\,\|b\|_2\) because \(\tau(bb^*)=\tau(b^*b)\).

(2) Write \(b=w|b|\) with \(w\in M\) a partial isometry and \(w^*w|b|=|b|\). Traciality gives \(\tau(ab)=\tau(|b|^{1/2}aw|b|^{1/2})\). The functional \(x\mapsto\tau(|b|^{1/2}x|b|^{1/2})\) is positive with norm \(\tau(|b|)\), so \(|\tau(ab)|\le\|aw\|\,\tau(|b|)\le\|a\|\,\|b\|_1\). The choice \(d=w^*\) gives \(\tau(w^*b)=\tau(|b|)\), so the maximum is attained. Finally \(\|abc\|_1=\max_{\|d\|\le1}|\tau((cda)b)|\le\|a\|\,\|c\|\,\|b\|_1\).

(3) By (1), \(\tau(|b|)=\tau(|b|\cdot1)\le\||b|\|_2\|1\|_2=\|b\|_2\). If \(b=bq\), then \(b^*b=qb^*bq\); \(|b|\) is a norm limit of polynomials in \(b^*b\) without constant term, so \(|b|=|b|q\), and \(\tau(|b|)=\tau(|b|q)\le\|b\|_2\|q\|_2=\tau(q)^{1/2}\|b\|_2\). \(\square\)

By (1), products and adjoints are continuous for \(\|\cdot\|_2\) on bounded sets: if \(\sup_i\|x_i\|\) and \(\sup_i\|y_i\|\) are finite, \(x_i\to x\) and \(y_i\to y\) in \(2\)-norm, then
\[
\|x_iy_i-xy\|_2\le\|x_i\|\,\|y_i-y\|_2+\|x_i-x\|_2\,\|y\|,\qquad\|x_i^*-x^*\|_2=\|x_i-x\|_2 .
\]
Hence a product of finitely many bounded letters depends continuously on the letters, and so does its trace. A \(2\)-norm limit of a bounded net of unitaries (projections) is a unitary (projection). The closed unit ball of \(M\) is complete for \(\|\cdot\|_2\) (Lemma 1.4 of the ultraproduct lesson, where \(\|x\|^\sharp=\sqrt2\|x\|_2\) for a trace).

For a von Neumann subalgebra \(N\subseteq M\) with \(1\in N\), the trace-preserving conditional expectation \(E_N\colon M\to N\) is the unique map with \(\tau(E_N(x)y)=\tau(xy)\) for \(x\in M\), \(y\in N\) (Theorem 9.1 of the integration lesson; a finite trace is semifinite on every subalgebra). The identity says that \(x-E_N(x)\) is orthogonal to \(N\) in \(L^2(M)\), so \(E_N\) is the restriction to \(M\) of the orthogonal projection \(e_N\) of \(L^2(M)\) onto the closure \(L^2(N)\) of \(N\).

## 2. Haar unitaries

**Definition 2.1.** Let \(q\in M\) be a nonzero projection. A *unitary of the corner* \(qMq\) is an \(h\in qMq\) with \(h^*h=hh^*=q\); its powers are \(h^0=q\), \(h^{j+1}=h^jh\) and \(h^{-j}=(h^*)^j\) for \(j\ge1\), so that \(h^ih^j=h^{i+j}\) for all \(i,j\in\mathbb Z\). It is a *Haar unitary of* \(qMq\) if \(\tau(h^j)=0\) for every \(j\ne0\). A Haar unitary of \(M\) is one of the corner \(1M1\).

**Lemma 2.2.** Let \(A\subseteq M\) be an abelian von Neumann subalgebra and \(e\in A\) a nonzero projection such that, for every projection \(f\le e\) of \(A\) and every \(0\le c\le\tau(f)\), there is a projection \(f'\le f\) in \(A\) with \(\tau(f')=c\). Then \(Ae\) contains a Haar unitary of \(eMe\).

**Proof.** Put \(s=\tau(e)\). Choose projections \(p_{m,k}\in A\), \(m\ge0\), \(0\le k<2^m\), with \(p_{0,0}=e\), \(p_{m,k}=p_{m+1,2k}+p_{m+1,2k+1}\) and \(\tau(p_{m,k})=2^{-m}s\): given \(p_{m,k}\), take \(p_{m+1,2k}\le p_{m,k}\) of trace \(2^{-m-1}s\) and let \(p_{m+1,2k+1}\) be the rest. Put
\[
h_m=\sum_{k=0}^{2^m-1}k2^{-m}p_{m,k}.
\]
Then \(h_{m+1}-h_m=\sum_k2^{-m-1}p_{m+1,2k+1}\), so \(0\le h_{m+1}-h_m\le2^{-m-1}e\), and \(h_m\) converges in norm to a self-adjoint \(x\in Ae\) with \(0\le x\le e\). For a continuous \(g\) on \([0,1]\) with \(g(0)=0\), \(g(h_m)=\sum_kg(k2^{-m})p_{m,k}\) because the \(p_{m,k}\) are orthogonal projections, so
\[
\tau(g(x))=\lim_m\tau(g(h_m))=\lim_m\sum_{k=0}^{2^m-1}g(k2^{-m})2^{-m}s=s\int_0^1g(r)\,dr .
\]
Let \(h=\exp(2\pi ix)e\), the functional calculus of \(r\mapsto e^{2\pi ir}\) in the corner \(eMe\) (with unit \(e\)). Then \(h\) is a unitary of \(eMe\), and for \(j\ne0\), \(h^j-e\) is \(g_j(x)\) with \(g_j(r)=e^{2\pi ijr}-1\), so \(\tau(h^j)=\tau(e)+s\int_0^1(e^{2\pi ijr}-1)\,dr=s-s=0\). \(\square\)

**Lemma 2.3.** In a factor \(Q\) with a faithful tracial state \(\tau\), two projections \(e,f\) with \(\tau(e)=\tau(f)\) are equivalent: there is \(v\in Q\) with \(v^*v=e\), \(vv^*=f\).

**Proof.** By the comparison theorem, one is equivalent to a subprojection of the other, say \(e\sim f'\le f\). Then \(\tau(f')=\tau(e)=\tau(f)\) because \(\tau(v^*v)=\tau(vv^*)\), so \(\tau(f-f')=0\) and \(f'=f\) by faithfulness. \(\square\)

**Corollary 2.4.** Let \(Q\) be a II₁ factor with trace \(\tau\) and \(q\in Q\) a nonzero projection. Then \(qQq\) has a Haar unitary, and \(Q\) has projections of every trace in \([0,1]\).

**Proof.** Lemma 55.1 of the quantization lesson gives a maximal abelian subalgebra \(A\subseteq Q\) in which every projection \(f\) has subprojections of every trace in \([0,\tau(f)]\); in particular \(A\) has projections of every trace in \([0,1]\). Take \(e\in A\) with \(\tau(e)=\tau(q)\) and \(v\in Q\) with \(v^*v=e\), \(vv^*=q\) (Lemma 2.3). Lemma 2.2 gives a Haar unitary \(h'\) of \(eQe\) in \(Ae\). Then \(h=vh'v^*\) satisfies \(h^*h=hh^*=q\), \(h^j=vh'^jv^*\) and \(\tau(h^j)=\tau(h'^jv^*v)=\tau(h'^j)=0\) for \(j\ne0\). \(\square\)

**Lemma 2.5** (decay of correlations). Let \(h\) be a Haar unitary of \(qMq\) and \(b\in M\). Then
\[
\sum_{j\in\mathbb Z}|\tau(h^jb)|^2\le\tau(q)\|b\|_2^2 ;
\]
in particular \(\tau(h^jb)\to0\) as \(|j|\to\infty\).

**Proof.** For \(i,j\in\mathbb Z\), \(\langle h^j,h^i\rangle=\tau(h^{-i}h^j)=\tau(h^{j-i})\), which is \(\tau(q)\) for \(i=j\) and \(0\) otherwise. So the vectors \(\tau(q)^{-1/2}h^j\) are orthonormal in \(L^2(M)\), and \(\tau(h^jb)=\tau(bh^j)=\langle h^j,b^*\rangle\). Bessel's inequality gives the claim. \(\square\)

## 3. Freeness of a unitary from a C*-algebra

**Definition 3.1.** Let \(D\subseteq M\) be a unital C\*-subalgebra and \(t\in M\) a unitary. Call \(t\) *free from* \(D\) if \(\tau(c_1c_2\cdots c_r)=0\) whenever \(r\ge1\), each \(c_i\) has trace zero and lies in \(C^*(t)\) or in \(D\), and consecutive letters \(c_i,c_{i+1}\) come from different ones of these two algebras.

Elements of trace zero are called *centred*. If \(t\) is a Haar unitary, every power \(t^n\), \(n\ne0\), is a centred element of \(C^*(t)\). The next lemma replaces the outer letters of an alternating word by arbitrary elements of \(D\); this is the form used throughout the course.

**Lemma 3.2.** Let \(t\) be a Haar unitary of \(M\) and \(D\subseteq M\) a unital C\*-subalgebra. Then \(t\) is free from \(D\) if and only if
\[
\tau(d_0t^{n_1}d_1t^{n_2}\cdots t^{n_j}d_j)=0
\tag{3.1}
\]
for every \(j\ge1\), all \(n_1,\dots,n_j\in\mathbb Z\setminus\{0\}\) and all \(d_0,\dots,d_j\in D\) with \(\tau(d_i)=0\) for \(1\le i\le j-1\). The outer letters \(d_0,d_j\) are arbitrary.

**Proof.** Suppose \(t\) is free from \(D\). Write \(d_0=\tau(d_0)1+d_0^\circ\) and \(d_j=\tau(d_j)1+d_j^\circ\) and expand (3.1) into four words. In each of them the letters \(t^{n_i}\) are centred elements of \(C^*(t)\), they are separated by the centred letters \(d_1,\dots,d_{j-1}\) of \(D\), and the outer letters are either absent or the centred \(d_0^\circ,d_j^\circ\). So each word is alternating and centred, and has trace \(0\).

Conversely assume (3.1). The Laurent polynomials in \(t\) are norm dense in \(C^*(t)\). If \(c\in C^*(t)\) is centred and Laurent polynomials \(L_k\) converge to \(c\) in norm, then \(L_k-\tau(L_k)1\to c\), and \(L_k-\tau(L_k)1\) is a combination of powers \(t^n\) with \(n\ne0\), since \(\tau(t^n)=0\) for \(n\ne0\). The trace of a word depends multilinearly and norm continuously on its letters, so in an alternating centred word it suffices to treat letters \(c_i=t^{n_i}\) from \(C^*(t)\). Such a word has the form (3.1), with \(d_0=1\) if it begins with a power of \(t\), \(d_j=1\) if it ends with one, and centred interior letters from \(D\). Its trace is \(0\). A word without letters from \(C^*(t)\) is a single centred element of \(D\), and has trace \(0\) as well. \(\square\)

**Lemma 3.3** (absorption). Let \(t\) be a Haar unitary free from \(D\), and let \(a,b\) be unitaries of \(D\). Then \(t^*\) and \(atb\) are Haar unitaries free from \(D\).

**Proof.** For \(t^*\), (3.1) for \(t^*\) is (3.1) for \(t\) with the exponents negated. Put \(v=atb\) and consider a word \(d_0v^{n_1}d_1\cdots v^{n_j}d_j\) as in (3.1). For \(n>0\) and \(n<0\) respectively,
\[
v^n=at(ba)t(ba)\cdots(ba)tb,\qquad v^{n}=b^*t^*(a^*b^*)t^*\cdots(a^*b^*)t^*a^*,
\]
with \(|n|\) letters \(t^{\pm1}\). Substituting, the word becomes \(e_0t^{\sigma_1}e_1t^{\sigma_2}\cdots t^{\sigma_N}e_N\) with \(\sigma_r=\pm1\) and \(e_r\in D\). Inside one power all letters have the same sign. A separator between letters of opposite signs therefore sits at a junction of \(v^{n_i}\) and \(v^{n_{i+1}}\), and equals \(bd_ib^*\) (from \(t\) to \(t^*\)) or \(a^*d_ia\) (from \(t^*\) to \(t\)); it is centred, since \(\tau(bd_ib^*)=\tau(d_i)=0\). Write every separator between letters of equal sign as \(\tau(e_r)1+e_r^\circ\) and expand. In each resulting word, the letters joined by scalar separators combine into a power \(t^m\) with \(m\ne0\), because they have equal signs, and successive powers are separated by centred elements of \(D\). The outer letters \(e_0,e_N\) lie in \(D\). By (3.1) for \(t\), every term has trace \(0\). Thus (3.1) holds for \(v\). With \(j=1\) and \(d_0=d_1=1\) it says \(\tau(v^n)=0\) for \(n\ne0\), so \(v\) is a Haar unitary, and Lemma 3.2 shows that \(v\) is free from \(D\). \(\square\)

## 4. Tracial ultraproducts

Fix a free ultrafilter \(\omega\) on \(\mathbb N\) and tracial von Neumann algebras \((M_n,\tau_n)\). The ultraproduct \(\mathbf M=\prod_\omega M_n\) is the quotient of the C\*-algebra of bounded sequences \((x_n)\), \(x_n\in M_n\), by the ideal of sequences with \(\lim_\omega\|x_n\|_2=0\), with trace \(\tau((x_n))=\lim_\omega\tau_n(x_n)\). By Theorem 3.2 of the ultraproduct lesson, \((\mathbf M,\tau)\) is a tracial von Neumann algebra. A bounded sequence mapping to \(x\) is a *representing sequence* of \(x\). Because the quotient map is a \(*\)-homomorphism, a word in elements of \(\mathbf M\) is represented by the same word in representing sequences, and \(\tau(x)=\lim_\omega\tau_n(x_n)\) for every representing sequence. In particular a sequence of projections (unitaries, partial isometries \(w_n\) with \(w_n^*w_n=w_nw_n^*\)) represents a projection (a unitary, a partial isometry \(w\) with \(w^*w=ww^*\)). When all \(M_n\) equal \(M\), we write \(M^\omega\) and regard \(M\subseteq M^\omega\) through constant sequences.

**Lemma 4.1.** Let \(N_n\subseteq M_n\) be von Neumann subalgebras with \(1\in N_n\). The classes in \(\mathbf M\) of bounded sequences \((y_n)\) with \(y_n\in N_n\) form a von Neumann subalgebra of \(\mathbf M\), identified with \(\prod_\omega N_n\).

**Proof.** A bounded sequence in \(\prod N_n\) has the same \(2\)-norms in \(N_n\) and in \(M_n\), so the map \(\prod_\omega N_n\to\mathbf M\) is a well-defined, injective, trace-preserving unital \(*\)-homomorphism. Its image \(\mathcal N\) is a unital \(*\)-subalgebra. An injective \(*\)-homomorphism of C\*-algebras is isometric, so the unit ball of \(\mathcal N\) is the image of the unit ball of \(\prod_\omega N_n\), which is complete for \(\|\cdot\|_2\) by Theorem 3.2 and Lemma 1.4 of the ultraproduct lesson. Let \(\mathbf M\) act on \(L^2(\mathbf M)\) and let \(x\) be in the unit ball of \(\mathcal N''\). By Kaplansky's density theorem there is a net \(x_i\) in the unit ball of \(\mathcal N\) converging strongly to \(x\); applied to the vector \(1\), this says \(\|x_i-x\|_2\to0\). So \((x_i)\) is Cauchy for \(\|\cdot\|_2\), converges in the unit ball of \(\mathcal N\), and its limit is \(x\). Hence \(\mathcal N=\mathcal N''\). \(\square\)

**Lemma 4.2** (unitaries lift). If every \(N_n\) is a factor, every unitary \(U\in\prod_\omega N_n\) has a representing sequence of unitaries \(U_n\in N_n\).

**Proof.** Let \((b_n)\) be a bounded representing sequence with \(b_n\in N_n\), and \(b_n=w_n|b_n|\) its polar decompositions in \(N_n\). Since \(\tau_n(w_n^*w_n)=\tau_n(w_nw_n^*)\), Lemma 2.3 gives \(y_n\in N_n\) with \(y_n^*y_n=1-w_n^*w_n\) and \(y_ny_n^*=1-w_nw_n^*\). Then \(U_n=w_n+y_n\) is a unitary (the cross terms vanish because \(w_n^*(1-w_nw_n^*)=0\) and \(w_n(1-w_n^*w_n)=0\)), and \(U_n|b_n|=b_n\) because \(w_n^*w_n\) is the support of \(|b_n|\). Hence \(b_n-U_n=U_n(|b_n|-1)\). For \(r\ge0\), \(|\sqrt r-1|\le|r-1|\), so functional calculus gives
\[
\|b_n-U_n\|_2=\||b_n|-1\|_2\le\|b_n^*b_n-1\|_2 .
\]
The right side tends to \(\|U^*U-1\|_2=0\) along \(\omega\), so \((U_n)\) represents \(U\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Show that a unitary \(u\) of \(M\) is a Haar unitary if and only if \(\tau(g(u))=\int_0^1g(e^{2\pi ir})\,dr\) for every continuous function \(g\) on the unit circle.

**Exercise 5.2.** Show that a finite-dimensional tracial von Neumann algebra has no Haar unitary.

**Exercise 5.3.** Let \(h\) be a Haar unitary of \(M\). Show that the class of the sequence \((h^n)_{n\ge1}\) in \(M^\omega\) is a unitary orthogonal to \(M\) in \(L^2(M^\omega)\). Conclude that \(M^\omega\ne M\) when \(M\) has a Haar unitary.

**Exercise 5.4.** Let \(t\) be a Haar unitary free from \(D\) and \(k\ne0\). Show that \(t^k\) is a Haar unitary free from \(D\).

**Exercise 5.5.** Show that every projection of \(\prod_\omega N_n\) has a representing sequence of projections \(p_n\in N_n\). (Hint: \(|\chi_{[1/2,\infty)}(r)-r|\le2|r^2-r|\) for real \(r\).)

## 6. Solutions

**5.1.** The identity holds for \(g(z)=z^j\) exactly when \(\tau(u^j)=0\) for \(j\ne0\) (for \(j=0\) both sides are \(1\)). Both sides are linear and continuous in \(g\) for the supremum norm, and trigonometric polynomials are dense in the continuous functions on the circle.

**5.2.** If \(M\) is finite-dimensional, \(u\) has finitely many spectral projections \(p_1,\dots,p_r\) with eigenvalues \(\lambda_i\), and \(\tau(g(u))=\sum_ig(\lambda_i)\tau(p_i)\). Choose a continuous \(g\ge0\) vanishing at every \(\lambda_i\) and positive elsewhere: the left side of Exercise 5.1 is \(0\), the right side is positive. So \(u\) is not Haar.

**5.3.** The class \(x\) of \((h^n)\) is a unitary, and for \(y\in M\), \(\langle x,y\rangle=\lim_\omega\tau(y^*h^n)=0\) by Lemma 2.5. If \(M^\omega=M\), then \(x\in M\) would be orthogonal to itself, while \(\|x\|_2=1\).

**5.4.** \(\tau((t^k)^n)=\tau(t^{kn})=0\) for \(n\ne0\), and (3.1) for \(t^k\) with exponents \(n_i\) is (3.1) for \(t\) with exponents \(kn_i\ne0\). Lemma 3.2 applies.

**5.5.** Take a self-adjoint representing sequence \((y_n)\) of the projection \(p\) (replace \(y_n\) by \((y_n+y_n^*)/2\)), and \(p_n=\chi_{[1/2,\infty)}(y_n)\). The scalar inequality and functional calculus give \(\|p_n-y_n\|_2\le2\|y_n^2-y_n\|_2\), which tends to \(\|p^2-p\|_2=0\) along \(\omega\). (For \(r\ge\frac12\) the inequality reads \(|1-r|\le2r|r-1|\); for \(r<\frac12\) it reads \(|r|\le2|r|\,|r-1|\).)

## References

- [OpenAI-Gen] OpenAI, Relative generation and the generator problem for finite factors, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Relative-generation-and-the-generator-problem-for-finite-factors-September-23-2026
- [Popa-Ind] S. Popa, Independence properties in subalgebras of ultraproduct II₁ factors, Journal of Functional Analysis 266 (2014), 5818–5846. https://arxiv.org/abs/1308.3982
- [DSSW] K. Dykema, A. Sinclair, R. Smith, S. White, Generators of II₁ factors, Operators and Matrices 2 (2008), 555–582. https://arxiv.org/abs/0706.1953
