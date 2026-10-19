# A bundle glued along three graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson constructs the rank-two bundle \(G\) of the theorem of [Hermitian metrics and Griffiths positivity](hermitian-metrics-and-griffiths-positivity.md). It is obtained from \(\mathcal O_S(24,0)\oplus\mathcal O_S(0,24)\) on \(S=\mathbb P^1\times\mathbb P^1\) by keeping the pairs of sections that agree, along three graphs of projective transformations, under prescribed identifications. Two properties of the transformations matter. Their linear lifts and the relative lift have finite order, which makes the identifications agree where the graphs meet. Their product is hyperbolic, which will rule out a common invariant measure in [An invariant measure and the proof](an-invariant-measure-and-the-proof.md).

- The two matrices (Lemma 1.1).
- The three graphs and their six intersection points (Lemma 2.1).
- The gluing, the bundle \(G\), its two quotient sequences and the two line subbundles of its dual (Proposition 3.1).

The lesson follows [OpenAI-GP, Section 2]. We view \(\mathbb P^1\) as the set of lines in \(\mathbb C^2\), with the tautological line bundle \(\mathcal O_{\mathbb P^1}(-1)\) whose fiber at a line is the line itself; a matrix \(M\in\operatorname{SL}_2(\mathbb C)\) acts on \(\mathbb P^1\), and maps the line \(x\) linearly onto the line \(Mx\).

## 1. Two matrices

Put
\[
a=e^{i\pi/3},\qquad s=\frac12-\frac{i(1+2\sqrt2)}{2\sqrt3},
\]
\[
\begin{gathered}
A=\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix},\\
B=\begin{pmatrix}s&1\\\sqrt2/3&1-s\end{pmatrix}.
\end{gathered}
\]

**Lemma 1.1** ([OpenAI-GP, Lemma 2.1]).

1. \(A,B\in\operatorname{SL}_2(\mathbb C)\), \(\operatorname{tr}A=\operatorname{tr}B=1\), \(\operatorname{tr}(A^{-1}B)=-\sqrt2\) and \(\operatorname{tr}(AB)=1+\sqrt2\).
2. \(A\) and \(B\) have order \(6\), and \(A^{-1}B\) has order \(8\); \(A^3=B^3=-I\), so \(A\) and \(B\) act on \(\mathbb P^1\) with order \(3\).
3. \(AB\) has two positive real eigenvalues \(\lambda>1>\lambda^{-1}\).
4. \(A\) and \(B\) have no common eigenline.

**Proof.** *Part 1.* \(\det A=1\). With \(\beta=\frac{1+2\sqrt2}{2\sqrt3}\), \(s=\frac12-i\beta\) and
\[
\begin{aligned}
s(1-s)&=\tfrac14+\beta^2=\tfrac14+\tfrac{9+4\sqrt2}{12}\\
&=1+\tfrac{\sqrt2}3 ,
\end{aligned}
\]
so \(\det B=s(1-s)-\frac{\sqrt2}3=1\), and \(\operatorname{tr}B=1\). Further \(a^{-1}-a=-i\sqrt3\), so
\[
\begin{aligned}
\operatorname{tr}(A^{-1}B)&=a^{-1}s+a(1-s)\\
&=a-i\sqrt3\,s\\
&=\tfrac12-\sqrt3\beta=-\sqrt2 .
\end{aligned}
\]
By the Cayley–Hamilton theorem, \(A^2-A+I=0\), so \(A+A^{-1}=I\), and multiplying by \(B\), \(\operatorname{tr}(AB)=\operatorname{tr}B-\operatorname{tr}(A^{-1}B)=1+\sqrt2\).

*Part 2.* The characteristic polynomial of \(A\) and of \(B\) is \(t^2-t+1\), with the distinct roots \(e^{\pm i\pi/3}\), primitive sixth roots of unity; that of \(A^{-1}B\) is \(t^2+\sqrt2t+1\), with the roots \(e^{\pm3i\pi/4}\), primitive eighth roots of unity. A matrix with distinct eigenvalues is diagonalizable, so the orders are \(6\), \(6\) and \(8\), and \(A^3=B^3=-I\) acts trivially on \(\mathbb P^1\) while \(A\) and \(B\) do not.

*Part 3.* \(\det(AB)=1\) and \(\operatorname{tr}(AB)=1+\sqrt2>2\), so the eigenvalues are the real roots of \(t^2-(1+\sqrt2)t+1\), positive with product one and distinct.

*Part 4.* The eigenlines of \(A\) are the two coordinate lines, and \(B\) maps neither to itself, since both off-diagonal entries of \(B\) are nonzero. \(\blacksquare\)

## 2. Three graphs

For \(M\in\{I,A,B\}\) let \(\Gamma_M=\{(x,Mx):x\in\mathbb P^1\}\subset S\), and let \(D=\Gamma_I\cup\Gamma_A\cup\Gamma_B\) with the reduced structure. Write \(\mathcal O_S(r,t)\) as in the first lesson. For \(M=\begin{pmatrix}p&q\\u&v\end{pmatrix}\), \(\Gamma_M\) is the zero set of the form \(w_0(uz_0+vz_1)-w_1(pz_0+qz_1)\) of bidegree \((1,1)\); so \(\mathcal O_S(D)=\mathcal O_S(3,3)\).

**Lemma 2.1** ([OpenAI-GP, Lemma 2.2]). The three graphs are smooth. Two of them meet in exactly two points, transversally, and no point lies on all three. So \(D\) has exactly six singular points, each an ordinary node.

**Proof.** A graph is isomorphic to \(\mathbb P^1\). A point of \(\Gamma_M\cap\Gamma_N\) is \((x,Mx)\) with \(Mx=Nx\), that is, a fixed point \(x\) of \(M^{-1}N\) on \(\mathbb P^1\), which is an eigenline. The relative matrices for the three pairs are \(A\), \(B\) and \(A^{-1}B\) (up to inversion), each with two distinct eigenvalues, so each pair meets in exactly two points. In an affine coordinate the graphs of \(M\) and \(N\) near a common point are the graphs of two holomorphic functions, and they meet transversally exactly when the derivatives differ, that is, when the multiplier of \(M^{-1}N\) at its fixed point is not \(1\). The multiplier at either fixed point is the ratio of the two eigenvalues in one order or the other, which is not \(1\). A point on all three graphs would be a common fixed point of \(A\) and \(B\), excluded by Lemma 1.1. \(\blacksquare\)

## 3. The gluing

Put
\[
\begin{gathered}
b=24,\\
L_1=\mathcal O_S(b,0),\qquad L_2=\mathcal O_S(0,b) .
\end{gathered}
\]
The fiber of \(L_1^{-1}=p_1^*\mathcal O(-b)\) at \((x,y)\) is \(x^{\otimes b}\), and that of \(L_2^{-1}\) is \(y^{\otimes b}\). On \(\Gamma_M\), where \(y=Mx\), the linear map \(M\colon x\to Mx\) induces the isomorphism \(M^{\otimes b}\colon x^{\otimes b}\to(Mx)^{\otimes b}\), an isomorphism \(\alpha_M\colon L_1^{-1}|_{\Gamma_M}\to L_2^{-1}|_{\Gamma_M}\) of line bundles on \(\Gamma_M\). The number \(24\) is the least common multiple of the orders \(6\), \(6\), \(8\) of Lemma 1.1.

**Proposition 3.1** ([OpenAI-GP, Proposition 2.3]). (1) The three isomorphisms \(\alpha_M\) glue to an isomorphism of line bundles on \(D\),
\[
\alpha\colon L_1^{-1}|_D\to L_2^{-1}|_D ,\qquad\alpha|_{\Gamma_M}=M^{\otimes b} .
\]
(2) Let \(\beta=(\alpha^\vee)^{-1}\colon L_1|_D\to L_2|_D\). The subsheaf
\[
\begin{aligned}
G=\bigl\{(u_1,u_2)&\in L_1\oplus L_2:\\
&u_2|_D=\beta(u_1|_D)\bigr\}
\end{aligned}
\]
is a vector bundle of rank two. (3) Both projections \(\rho_i\colon G\to L_i\) are surjective, and for \(\{i,j\}=\{1,2\}\) there are exact sequences
\[
0\to L_i(-D)\to G\xrightarrow{\ \rho_j\ }L_j\to0 .
\]
(4) Let \(F=G^\vee\) and \(\iota_i=\rho_i^\vee\colon L_i^{-1}\to F\). The line subbundles \(\iota_1(L_1^{-1})\) and \(\iota_2(L_2^{-1})\) span every fiber of \(F\) over \(S\setminus D\), and \(\iota_2\circ\alpha=\iota_1\) on \(D\).

**Proof.** *Agreement at the nodes.* At a point \((x,Mx)=(x,Nx)\) of \(\Gamma_M\cap\Gamma_N\), let \(v\) span the line \(x\). Then \(M^{-1}Nv=\lambda v\) for an eigenvalue \(\lambda\) of \(M^{-1}N\), so \(Nv=\lambda Mv\), and \(\lambda^{24}=1\) by Lemma 1.1. Hence \((Nv)^{\otimes b}=\lambda^b(Mv)^{\otimes b}=(Mv)^{\otimes b}\): the two isomorphisms agree on the fiber over the node.

*Part 1.* Away from the nodes there is nothing to glue. Let \(R\) be the local ring of \(S\) at a node, and \((d_1),(d_2)\) the ideals of the two branches. Since the branches are transverse, \(d_1,d_2\) are a regular system of parameters, \((d_1)\cap(d_2)=(d_1d_2)\) in the factorial ring \(R\), and the sequence
\[
\begin{aligned}
&0\to R/(d_1d_2)\to R/(d_1)\oplus R/(d_2)\\
&\quad\to R/(d_1,d_2)\to0 ,
\end{aligned}
\]
whose last map is the difference of the values at the node, is exact. Tensoring with the stalk of the invertible sheaf \(\mathcal Hom(L_1^{-1},L_2^{-1})\), a pair of sections on the two branches with the same value at the node comes from a unique section over \(D\) near the node. The glued section is a unit, since its value at the node is nonzero. This gives \(\alpha\).

*Part 2.* Near a point of \(D\), choose frames of \(L_1\) and \(L_2\) and a local equation \(d\) of \(D\), and lift the function that represents \(\beta\) on \(D\) to a function \(h\), a unit after shrinking. A pair \((u_1,u_2)\) lies in \(G\) exactly when \(d\) divides \(u_2-hu_1\). So every element is uniquely \(u_1e+kf\) with
\[
e=(1,h),\qquad f=(0,d),
\]
and \(k=(u_2-hu_1)/d\); \(e,f\) is a basis. Away from \(D\), \(G=L_1\oplus L_2\). So \(G\) is locally free of rank two.

*Part 3.* \(\rho_1(e)=1\) and \(\rho_2(e)=h\), a unit, so both projections are surjective. The kernel of \(\rho_j\) consists of the pairs with \(u_j=0\); for such pairs the condition reads \(\beta(u_i|_D)=0\) or \(u_i|_D=0\), since \(\beta\) is an isomorphism, so the kernel is \(L_i(-D)\).

*Part 4.* Since \(\rho_i\) is surjective, \(\iota_i\) is an injection onto a line subbundle. Off \(D\), \(G=L_1\oplus L_2\) and the two lines are the two summands of \(F=L_1^{-1}\oplus L_2^{-1}\). On \(D\), for \(v\in L_1^{-1}\) and \((u_1,u_2)\in G\),
\[
\begin{aligned}
&\bigl(\iota_2(\alpha v)\bigr)(u_1,u_2)=(\alpha v)(u_2)\\
&\quad=(\alpha v)(\beta u_1)=v(\alpha^\vee\beta u_1)\\
&\quad=v(u_1)=\bigl(\iota_1(v)\bigr)(u_1,u_2) .
\end{aligned}
\]
\(\blacksquare\)

So over \(D\) the two line subbundles of \(F\) coincide, and are identified with each other through \(\alpha\), that is, through the lifts \(M^{\otimes24}\) of the three transformations. This identification is what the quadratic limit of the last lesson will remember.

In the notation of the first lesson, \(L_1(-D)=\mathcal O_S(21,-3)\) and \(L_2(-D)=\mathcal O_S(-3,21)\), and both sequences give \(\det G=\mathcal O_S(21,21)\). The bundle \(G\) is an elementary transformation of \(L_1\oplus L_2\) along \(D\) in the sense of Maruyama [OpenAI-GP, Section 2].

## 4. Exercises

**4.1.** Verify \(s(1-s)=1+\frac{\sqrt2}3\) and \(\operatorname{tr}(A^{-1}B)=-\sqrt2\) numerically, and find the two eigenvalues of \(AB\).

**4.2.** Find the six nodes of \(D\) explicitly for the pair \(\Gamma_I,\Gamma_A\), and show that the other four nodes lie off the coordinate points of \(\mathbb P^1\times\mathbb P^1\).

**4.3.** Show that the gluing of Proposition 3.1 fails for \(b=12\): at some node the two isomorphisms differ by a sign.

**4.4.** Compute \(c_1(G)\) and \(c_2(G)\), using that the intersection number of bidegrees \((a,b)\) and \((c,d)\) on \(\mathbb P^1\times\mathbb P^1\) is \(ad+bc\).

**4.5.** Show that \(\iota_1(L_1^{-1})\) and \(\iota_2(L_2^{-1})\) are different line subbundles of \(F\) at every point off \(D\) and equal at every point of \(D\).

## 5. Solutions

**4.1.** \(\beta=(1+2\sqrt2)/(2\sqrt3)\approx1.1052\), so \(s(1-s)=0.25+\beta^2\), which equals \(1+\sqrt2/3\approx1.4714\). The eigenvalues of \(AB\) are \(\frac{1+\sqrt2\pm\sqrt{(1+\sqrt2)^2-4}}2=\frac{1+\sqrt2\pm\sqrt{2\sqrt2-1}}2\), approximately \(1.883\) and \(0.531\).

**4.2.** The fixed points of \(A\) are the coordinate lines \(0=[1:0]\) and \(\infty=[0:1]\), so \(\Gamma_I\cap\Gamma_A=\{(0,0),(\infty,\infty)\}\). The fixed points of \(B\) and of \(A^{-1}B\) are eigenlines of matrices with nonzero off-diagonal entries, hence not coordinate lines; the corresponding nodes are \((x,x)\) and \((x,Ax)\) with \(x\ne0,\infty\).

**4.3.** The eigenvalues of \(A^{-1}B\) are \(e^{\pm3i\pi/4}\), and \((e^{3i\pi/4})^{12}=e^{9i\pi}=-1\). At a node of \(\Gamma_A\cap\Gamma_B\), \((Bv)^{\otimes12}=-(Av)^{\otimes12}\).

**4.4.** From \(0\to\mathcal O(21,-3)\to G\to\mathcal O(0,24)\to0\): \(c_1(G)=(21,21)\), and \(c_2(G)=(21,-3)\cdot(0,24)\), which is \(21\cdot24+(-3)\cdot0=504\).

**4.5.** Off \(D\) they are the two summands \(L_1^{-1}\) and \(L_2^{-1}\) of \(F\). On \(D\), \(\iota_1(v)=\iota_2(\alpha v)\) with \(\alpha\) an isomorphism, so the images coincide.

## References

- [OpenAI-GP] OpenAI, *Ample rank-two bundles on the quadric surface without Griffiths-positive metrics*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026
