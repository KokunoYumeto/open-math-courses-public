# Horrocks' theorem and the Quillen–Suslin theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Serre asked in 1955 whether every finitely generated projective module over a polynomial ring \(k[x_1,\ldots,x_r]\) over a field is free. Quillen and Suslin proved in 1976 that the answer is yes. This lesson gives a complete proof. The local ingredient is Horrocks' theorem: over a local ring \(A\), a projective \(A[X]\)-module which becomes free after inverting all monic polynomials is free. Its proof here is elementary: the rank is lowered one step at a time by a well-chosen element, and the rank-one case reduces to a characteristic polynomial. With Quillen's patching theorem of the previous lesson this gives Horrocks' theorem over every ring, and an induction on the number of variables, passing through the field \(k(y)\), proves the Quillen–Suslin theorem.

We use [Patching extended modules](patching-extended-modules.md) (Theorem 4.1 and Corollary 4.2); from [Localization, local properties and support](course:AG-CA/localization-local-properties-and-support#4-finite-generators-near-a-point) Theorem 2.2 (localizing \(\operatorname{Hom}\)), Theorem 4.2 (Nakayama's lemma) and Theorem 5.1 (local detection); and Schanuel's lemma, Lemma 1.1 of [Projective dimension and the Auslander–Buchsbaum formula](course:AG-CA/projective-dimension-and-the-auslander-buchsbaum-formula). Rings are commutative with \(1\). For a ring \(A\), \(S\subset A[X]\) denotes the set of monic polynomials; it is multiplicative and consists of nonzerodivisors, and \(A\langle X\rangle=S^{-1}A[X]\).

## 1. Projective modules

**Lemma 1.1.** Let \(B\) be a ring.

1. A finitely generated projective module over a local ring is free.
2. A finitely presented \(B\)-module \(P\) such that \(P_{\mathfrak q}\) is a free \(B_{\mathfrak q}\)-module for every prime \(\mathfrak q\) is projective.
3. If \(S,U\subseteq B\) are multiplicative sets with \(sB+uB=B\) for all \(s\in S\), \(u\in U\), and \(P\) is a finitely presented \(B\)-module with \(S^{-1}P\) and \(U^{-1}P\) projective, then \(P\) is projective.

**Proof.** (1) Let \((B,\mathfrak n)\) be local and \(P\) finitely generated projective. Lift a basis of \(P/\mathfrak nP\) to \(e_1,\ldots,e_r\in P\); by Nakayama's lemma they generate \(P\), so \(\pi\colon B^r\to P\) is onto. It splits, \(B^r=K\oplus P'\) with \(K=\ker\pi\) finitely generated, and modulo \(\mathfrak n\) the map \(\pi\) is a surjection of \(r\)-dimensional vector spaces, hence injective; so \(K/\mathfrak nK=0\) and \(K=0\).

(2) Let \(N\to N''\) be surjective. By Theorem 2.2 of the localization lesson, the localization of \(\operatorname{Hom}_B(P,N)\to\operatorname{Hom}_B(P,N'')\) at a maximal ideal \(\mathfrak m\) is \(\operatorname{Hom}(P_{\mathfrak m},N_{\mathfrak m})\to\operatorname{Hom}(P_{\mathfrak m},N''_{\mathfrak m})\), which is surjective because \(P_{\mathfrak m}\) is free. By Theorem 5.1 there, the cokernel is zero. So \(\operatorname{Hom}_B(P,-)\) preserves surjections.

(3) If a prime \(\mathfrak q\) met both \(S\) and \(U\), say \(s,u\in\mathfrak q\), then \(B=sB+uB\subseteq\mathfrak q\). So \(\mathfrak q\) misses \(S\) or \(U\), and \(P_{\mathfrak q}\) is a localization of \(S^{-1}P\) or of \(U^{-1}P\). A localization of a projective module is projective, hence free over the local ring \(B_{\mathfrak q}\) by (1). Apply (2). \(\square\)

**Lemma 1.2.** Let \(D\) be a principal ideal domain.

1. Every submodule of \(D^n\) is free of rank at most \(n\). In particular, finitely generated projective \(D\)-modules are free.
2. If \(v\in D^n\) has coordinates generating the unit ideal, then \(v\) is part of a basis of \(D^n\).
3. Every \(y\in D^n\) can be written \(y=cv\) with \(c\in D\) and \(v\) as in (2).

**Proof.** (1) Induction on \(n\), the case \(n=0\) being empty. For \(N\subseteq D^n\), the last coordinate maps \(N\) onto an ideal \((a)\), with kernel \(N\cap D^{n-1}\), free of rank at most \(n-1\) by induction. If \(a=0\) we are done; otherwise choose \(x\in N\) with last coordinate \(a\), and then \(N=(N\cap D^{n-1})\oplus Dx\) with \(Dx\cong D\). A finitely generated projective module is a submodule of some \(D^n\).

(2) Choose \(d_i\) with \(\sum d_iv_i=1\) and let \(\lambda(y)=\sum d_iy_i\). Then \(D^n=Dv\oplus\ker\lambda\), and \(\ker\lambda\) is projective, hence free by (1); a basis of it together with \(v\) is a basis of \(D^n\).

(3) If \(y=0\), take \(c=0\) and \(v\) any basis vector. Otherwise let \(c\) generate the ideal spanned by the coordinates of \(y\); then \(y=cv\) and the coordinates of \(v\) generate the unit ideal. \(\square\)

## 2. Monic polynomials over a local ring

Throughout this section \((A,\mathfrak m)\) is a local ring with residue field \(k\), \(B=A[X]\), and \(U=1+\mathfrak m[X]\), the polynomials congruent to \(1\) modulo \(\mathfrak m\); it is multiplicative.

**Lemma 2.1.** For every monic \(f\) and every \(g\in U\), \(fB+gB=B\).

**Proof.** Let \(n=\deg f\). The ring \(C=B/fB\) is a free \(A\)-module with basis \(1,X,\ldots,X^{n-1}\). Let \(\mu\) be multiplication by \(g\) on \(C\) and \(\chi(Y)=\det(Y-\mu)\in A[Y]\). By the Cayley–Hamilton theorem \(\chi(\mu)=0\); since \(\chi(\mu)\) is multiplication by \(\chi(g)\), we get \(\chi(g)\in fB\). Writing \(\chi(Y)=\chi(0)+Y\chi_1(Y)\) gives \(\pm\det\mu=\chi(0)\in fB+gB\). Reducing modulo \(\mathfrak m\), \(C\otimes_Ak=k[X]/(\bar f)\) with the same basis and \(\mu\) becomes multiplication by \(\bar g=1\); so \(\det\mu\equiv1\) modulo \(\mathfrak m\) is a unit of \(A\). \(\square\)

The Jacobson radical of \(U^{-1}B\) contains \(\mathfrak mU^{-1}B\): if \(a\in\mathfrak m[X]\), \(b\in B\) and \(u_1,u_2\in U\), then \(1+(a/u_1)(b/u_2)=(u_1u_2+ab)/(u_1u_2)\) has numerator in \(U\), so it is a unit.

**Lemma 2.2** (rank one). Let \(P\) be a finitely generated projective \(B\)-module with \(S^{-1}P\cong S^{-1}B\). Then \(P\cong B\).

**Proof.** Since \(P\) is a direct summand of a free module and \(S\) consists of nonzerodivisors, \(P\to S^{-1}P\) is injective. Fix an isomorphism \(\varphi\colon S^{-1}P\to S^{-1}B\). The image of \(P\) is generated by finitely many elements, hence contained in \(s^{-1}B\) for one \(s\in S\), and \(I=s\varphi(P)\subseteq B\) is an ideal isomorphic to \(P\). As \(S^{-1}I=S^{-1}B\), there is a monic \(f\in I\). So \(fB\subseteq I\subseteq B\).

*The quotient \(B/I\) is a free \(A\)-module of finite rank.* Consider the exact sequences of \(A\)-modules
\[
0\to B\xrightarrow{\ \cdot f\ }I\to I/fB\to0,\qquad 0\to fB/fI\to I/fI\to I/fB\to0 .
\]
The \(B\)-module \(I\) is projective and \(B\) is a free \(A\)-module, so \(I\) is a projective \(A\)-module. The \(B/fB\)-module \(I/fI\) is projective and \(B/fB\) is a free \(A\)-module, so \(I/fI\) is a projective \(A\)-module. By Schanuel's lemma, \(B\oplus I/fI\cong fB/fI\oplus I\); hence \(fB/fI\) is a direct summand of a projective \(A\)-module. Multiplication by \(f\) is an isomorphism \(B/I\to fB/fI\), since \(f\) is a nonzerodivisor. So \(B/I\) is projective over \(A\), and finitely generated, as a quotient of \(B/fB\). By Lemma 1.1, it is free of some rank \(d\).

*The ideal \(I\) is principal.* Let \(\xi\) be the \(A\)-linear endomorphism of \(B/I\) given by multiplication by \(X\), and \(\chi(Y)=\det(Y-\xi)\), monic of degree \(d\). By Cayley–Hamilton, \(\chi(\xi)=0\), so \(\chi(X)\cdot1=0\) in \(B/I\), i.e. \(\chi\in I\). The induced map \(B/\chi B\to B/I\) is a surjection of free \(A\)-modules of rank \(d\). It splits, so its determinant is a unit and it is an isomorphism. Hence \(I=\chi B\cong B\). \(\square\)

**Theorem 2.3** (Horrocks, local form). Let \((A,\mathfrak m)\) be a local ring and \(P\) a finitely generated projective \(A[X]\)-module such that \(S^{-1}P\) is a free \(A\langle X\rangle\)-module. Then \(P\) is free.

**Proof.** Induction on the rank \(n\) of \(S^{-1}P\). If \(n=0\), then \(P=0\), since \(P\to S^{-1}P\) is injective. The case \(n=1\) is Lemma 2.2. Let \(n\ge2\).

*Residue module.* \(\bar P=P/\mathfrak mP\) is a finitely generated projective module over the principal ideal domain \(k[X]\), hence free (Lemma 1.2). Every nonzero polynomial over \(k\) is a unit times a monic one, so inverting the images of monic polynomials turns \(k[X]\) into \(k(X)\), and \(\bar P\otimes k(X)\cong(S^{-1}P)/\mathfrak m(S^{-1}P)\) has dimension \(n\). So \(\bar P\) has rank \(n\).

*A good element.* Choose \(y_1,\ldots,y_n\in P\) forming a basis of \(S^{-1}P\) (clear denominators of a basis). By Lemma 1.2, \(\bar y_1=c\,\bar v\) with \(\bar v\) part of a basis; choose a basis \(\bar w_1,\ldots,\bar w_n\) of \(\bar P\) with \(\bar w_2=\bar v\), and lift it to \(w_1,\ldots,w_n\in P\). In \(S^{-1}P\), \(w_1\) is a combination of the \(y_i\): \(sw_1=\sum_ib_iy_i\) with \(s\in S\) and \(b_i\in B\), and this holds in \(P\) because \(P\to S^{-1}P\) is injective. Put \(z=w_1+X^ry_1\) with \(r>\deg b_1\). Then
\[
sz=(b_1+sX^r)\,y_1+\sum_{i\ge2}b_iy_i ,
\]
and \(b_1+sX^r\) is monic. So \(z,y_2,\ldots,y_n\) is a basis of \(S^{-1}P\). Modulo \(\mathfrak m\), \(\bar z=\bar w_1+X^rc\,\bar w_2\), so \(\bar z,\bar w_2,\ldots,\bar w_n\) is a basis of \(\bar P\).

*Splitting off \(z\).* By Nakayama's lemma over \(U^{-1}B\), whose Jacobson radical contains \(\mathfrak mU^{-1}B\), the elements \(z,w_2,\ldots,w_n\) generate \(U^{-1}P\), because they generate \(U^{-1}P/\mathfrak mU^{-1}P=\bar P\) (elements of \(U\) act as \(1\) on \(\bar P\)). The surjection \((U^{-1}B)^n\to U^{-1}P\) splits; its kernel \(K\) is finitely generated, and \(K/\mathfrak mK=0\), because modulo \(\mathfrak m\) the map becomes the isomorphism \(k[X]^n\to\bar P\) given by a basis. So \(K=0\) and \(U^{-1}P\) is free on \(z,w_2,\ldots,w_n\).

Let \(P'=P/Bz\). It is finitely presented. The element \(z\) has zero annihilator, since its image is part of a basis of \(S^{-1}P\); so \(Bz\cong B\). The module \(S^{-1}P'\) is free on the images of \(y_2,\ldots,y_n\), and \(U^{-1}P'\) is free on the images of \(w_2,\ldots,w_n\). By Lemma 2.1, \(S\) and \(U\) satisfy the hypothesis of Lemma 1.1(3), so \(P'\) is projective. Then \(P\cong B\oplus P'\), and \(P'\) is a finitely generated projective module with \(S^{-1}P'\) free of rank \(n-1\). By induction \(P'\) is free, hence so is \(P\). \(\square\)

## 3. Horrocks' theorem over any ring, and Serre's problem

**Theorem 3.1** (Horrocks, affine form). Let \(A\) be a ring, \(P\) a finitely generated projective \(A[X]\)-module and \(Q\) a finitely generated projective \(A\)-module with \(S^{-1}P\cong Q\otimes_AA\langle X\rangle\). Then \(P\) is extended from \(A\): \(P\cong(P/XP)[X]\).

**Proof.** Let \(\mathfrak m\) be a maximal ideal of \(A\). By Lemma 1.1, \(Q_{\mathfrak m}\) is free, so the localization of \(P_{\mathfrak m}\) at the monic polynomials of \(A[X]\) is free; a fortiori so is its localization at all monic polynomials of \(A_{\mathfrak m}[X]\). By Theorem 2.3, \(P_{\mathfrak m}\) is free. By Corollary 4.2 of the patching lesson, \(P\cong(P/XP)[X]\). \(\square\)

**Theorem 3.2** (Quillen–Suslin). Let \(F\) be a field. Every finitely generated projective module over \(F[x_1,\ldots,x_r]\) is free.

**Proof.** Induction on \(r\), simultaneously for all fields. For \(r=0\) the module is a vector space. Let \(r\ge0\), assume the theorem for \(r\) variables over every field, and let \(P\) be a finitely generated projective module over \(B=F[x,y]\), where \(x=(x_1,\ldots,x_r)\) and \(y\) is one more variable.

Let \(T\subset F[y]\) be the set of monic polynomials in \(y\). Every nonzero element of \(F[y]\) is a unit times an element of \(T\), so \(T^{-1}B=F(y)[x]\), a polynomial ring in \(r\) variables over the field \(F(y)\). By the induction hypothesis, \(T^{-1}P\) is free, say of rank \(n\).

Now regard \(B\) as \(A[y]\) with \(A=F[x]\), and let \(S\subset A[y]\) be the set of polynomials in \(y\) with leading coefficient \(1\). Then \(T\subseteq S\), so \(S^{-1}P\) is a localization of \(T^{-1}P\) and is free of rank \(n\) over \(A\langle y\rangle\). Thus \(S^{-1}P\cong A^n\otimes_AA\langle y\rangle\), and Theorem 3.1 shows \(P\cong(P/yP)[y]\). The module \(P/yP\) is finitely generated and projective over \(A=F[x]\), hence free by the induction hypothesis. So \(P\) is free. \(\square\)

**Corollary 3.3.** Over \(F[x_1,\ldots,x_r]\), every finitely generated projective module \(P\) with \(P\oplus F[x]^m\) free is free, and every row \((f_1,\ldots,f_n)\) with \(\sum g_if_i=1\) for some \(g_i\) is the first row of an invertible \(n\times n\) matrix.

**Proof.** The first claim is a special case of Theorem 3.2. For the second, the map \(B^n\to B\), \(e_i\mapsto f_i\), is surjective and split by \(1\mapsto\sum g_ie_i\), so \(B^n=Bg\oplus K\) with \(g=(g_1,\ldots,g_n)\) and \(K\) the kernel. By Theorem 3.2, \(K\) is free, of rank \(n-1\) (compare ranks over the fraction field). The matrix whose columns are \(g\) and a basis of \(K\) is invertible, and the row \((f_1,\ldots,f_n)\) times it is \((1,0,\ldots,0)\). The inverse matrix therefore has first row \((f_1,\ldots,f_n)\). \(\square\)

## 4. Exercises

**Exercise 4.1.** Let \(A\) be a local domain and \(a\in\mathfrak m\), \(a\ne0\). Deduce from Lemma 2.1 that every monic \(f\) and \(1+aX\) generate the unit ideal of \(A[X]\), and show that \(1+aX\) is nevertheless not a unit of \(A\langle X\rangle\).

**Exercise 4.2.** Show that the kernel of the map \(k[x,y]^2\to k[x,y]\), \((a,b)\mapsto ax+by\), is free of rank one, and find a basis.

**Exercise 4.3.** Complete the row \((x,\ y,\ 1-xy)\) over \(k[x,y]\) to an invertible \(3\times3\) matrix.

**Exercise 4.4.** Explain why the inductive step in the proof of Theorem 2.3 needs \(n\ge2\).

## 5. Solutions

**4.1.** The first claim is Lemma 2.1, since \(1+aX\in U\). A unit of \(A\langle X\rangle\) divides a monic polynomial in \(A[X]\). If \(h\ne0\) has degree \(d\) and leading coefficient \(h_d\), then \((1+aX)h\) has degree \(d+1\) and leading coefficient \(ah_d\ne0\), which lies in \(\mathfrak m\); so \((1+aX)h\) is never monic.

**4.2.** The kernel consists of the \((a,b)\) with \(ax=-by\). Since \(x\) and \(y\) are coprime in the factorial ring \(k[x,y]\), \(y\) divides \(a\); writing \(a=cy\) gives \(b=-cx\). So the kernel is free with basis \((y,-x)\).

**4.3.** The matrix with rows \((x,\ y,\ 1-xy)\), \((0,\ 1,\ 0)\), \((-1,\ 0,\ y)\) has determinant \(x\cdot y+(1-xy)\cdot1=1\), expanding along the second row.

**4.4.** The good element \(z\) is obtained by modifying \(w_1\) by \(X^ry_1\), and the reduction \(\bar z\) stays part of a basis because \(\bar y_1\) is a multiple of a second basis vector \(\bar w_2\). With \(n=1\) there is no second basis vector, and the rank-one case requires the different argument of Lemma 2.2.

## References

- [Quillen] D. Quillen, Projective modules over polynomial rings, Inventiones Mathematicae 36 (1976), 167–171. https://gdz.sub.uni-goettingen.de/id/PPN356556735_0036
- [Lombardi–Quitté] H. Lombardi, C. Quitté, Commutative algebra: constructive methods, Springer 2015. https://arxiv.org/abs/1605.04832
