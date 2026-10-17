# A finite lattice identity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

From this lesson to the eighth, the tensor condition of [Ramsey sets and the tensor criterion](ramsey-sets-and-the-tensor-criterion.md) is assumed, and the aim is to show that the set is Ramsey. The first step turns the tensor equations, which live in the enormous space \(\mathbb R\otimes_{\mathbb Q}\mathbb R\), into a finite combinatorial object: rational weights on finitely many points of a lattice, whose sums vanish on every fibre of every evaluation, and whose second moment is a prescribed matrix. The proof passes through formal power series and uses one theorem of commutative algebra, the flatness of completion.

## 1. The data

Keep \(A=\{a_1,\dots,a_s\}\subset\mathbb R^d\) with \(s\ge2\) and affine span \(\mathbb R^d\), \(W=\mathbb R\times\mathbb R^d\) over \(\mathbb Q\), and \(e_i(v,u)=v+a_i\cdot u\). Let \(T\in W\otimes W\) be a symmetric tensor with
\[
\begin{gathered}
(e_i\otimes e_i)(T)=0\quad(1\le i\le s),\\
G(T)=I_d .
\end{gathered}
\]
A tensor involves finitely many vectors. Choose a basis \(w_1,\dots,w_k\) over \(\mathbb Q\) of a finite-dimensional subspace of \(W\) containing them, and write
\[
\begin{gathered}
T=\sum_{a,b=1}^kC_{ab}\,w_a\otimes w_b,\\
C\in\mathrm{Mat}_k(\mathbb Q).
\end{gathered}
\]
By (T1) of the first lesson the coefficients are unique, so \(C=C^{\mathsf T}\) because \(T\) is symmetric. For \(\lambda\in\mathbb Q^k\) put \(w(\lambda)=\sum_j\lambda_jw_j\). Write \(w_j=(v_j,u_j)\) and let \(U\) be the real \(d\times k\) matrix with columns \(u_1,\dots,u_k\). The gradient equation \(G(T)=I_d\) says
\[
UCU^{\mathsf T}=I_d .
\]
Let \(\Gamma=\mathbb Z^k\), and define the *evaluation lattices* and their spans
\[
\begin{gathered}
\Lambda_i=\{\lambda\in\Gamma:e_i(w(\lambda))=0\},\\
V_i=\mathrm{span}_{\mathbb Q}\Lambda_i .
\end{gathered}
\]
The map \(\phi_i:\mathbb Q^k\to\mathbb R\), \(\lambda\mapsto e_i(w(\lambda))\), is \(\mathbb Q\)-linear, and clearing denominators shows that \(V_i=\ker\phi_i\). So \(\phi_i\) induces an injection \(\mathbb Q^k/V_i\to\mathbb R\). With \(\varepsilon_1,\dots,\varepsilon_k\) the standard basis of \(\mathbb Q^k\),
\[
\begin{aligned}
&(e_i\otimes e_i)(T)\\
&\quad=(\phi_i\otimes\phi_i)\Bigl(\sum_{a,b}C_{ab}\,\varepsilon_a\otimes\varepsilon_b\Bigr)\\
&\quad=0 .
\end{aligned}
\]
By (T2) of the first lesson, the map \((\mathbb Q^k/V_i)\otimes(\mathbb Q^k/V_i)\to\mathbb R\otimes\mathbb R\) induced by the injection is injective. Hence the image of \(\sum_{a,b}C_{ab}\,\varepsilon_a\otimes\varepsilon_b\) in \((\mathbb Q^k/V_i)\otimes(\mathbb Q^k/V_i)\) is zero, for every \(i\).

Two lattice points have the same evaluation at \(a_i\) exactly when they differ by an element of \(\Lambda_i\): \(e_i(w(\gamma))=e_i(w(\gamma'))\) if and only if \(\gamma-\gamma'\in\Lambda_i\).

## 2. The lemma

For a function \(\nu:\Gamma\to\mathbb Q\) with finite support and a subgroup \(\Lambda\subseteq\Gamma\), the *pushforward* of \(\nu\) to \(\Gamma/\Lambda\) assigns to each coset \(q\) the sum \(\sum_{\gamma\in q}\nu(\gamma)\).

**Lemma 2.1** (finite lattice identity). Let \(k,s\ge1\), let \(\Lambda_1,\dots,\Lambda_s\) be subgroups of \(\Gamma=\mathbb Z^k\) with \(\mathbb Q\)-spans \(V_i\), and let \(C\in\mathrm{Mat}_k(\mathbb Q)\) be symmetric. Suppose that for every \(i\) the image of \(\sum_{a,b}C_{ab}\,\varepsilon_a\otimes\varepsilon_b\) in \((\mathbb Q^k/V_i)\otimes(\mathbb Q^k/V_i)\) is zero. Then there is a finitely supported \(\nu:\Gamma\to\mathbb Q\) whose pushforward to every \(\Gamma/\Lambda_i\) is zero and which satisfies
\[
\begin{gathered}
\sum_\gamma\nu(\gamma)=0,\qquad\sum_\gamma\nu(\gamma)\gamma=0,\\
\sum_\gamma\nu(\gamma)\gamma\gamma^{\mathsf T}=C .
\end{gathered}
\]

Applied to the data of Section 1, the lemma gives rational weights \(\nu\) on finitely many lattice points such that, for every \(i\) and every real value \(x\), the weights of the points \(\gamma\) with \(e_i(w(\gamma))=x\) add up to zero: positive and negative weights cancel separately at every evaluation value. Their second moment is \(C\), and \(UCU^{\mathsf T}=I_d\).

## 3. Proof of the lemma

**Step 1: Laurent polynomials.** Let \(R=\mathbb Q[X_1^{\pm1},\dots,X_k^{\pm1}]\), with monomials \(X^\gamma=\prod_jX_j^{\gamma_j}\) for \(\gamma\in\Gamma\); it is the group algebra of \(\Gamma\). A finitely supported \(\nu\) is the same as the Laurent polynomial \(\sum_\gamma\nu(\gamma)X^\gamma\). The quotient map \(\Gamma\to\Gamma/\Lambda_i\) induces a ring homomorphism from \(R\) to the group algebra of \(\Gamma/\Lambda_i\), and \(\nu\) has zero pushforward to \(\Gamma/\Lambda_i\) exactly when its polynomial lies in the kernel. We claim that this kernel is the ideal
\[
J_i=(X^h-1:h\in\Lambda_i).
\]
Each \(X^h-1\) with \(h\in\Lambda_i\) lies in the kernel. Conversely, a polynomial in the kernel is a sum of its parts supported on single cosets, each with coefficient sum zero. On a coset with a chosen point \(\gamma_0\), such a part equals \(\sum_\gamma c_\gamma(X^\gamma-X^{\gamma_0})\), that is, \(\sum_\gamma c_\gamma X^{\gamma_0}(X^{\gamma-\gamma_0}-1)\), which lies in \(J_i\).

So the lemma asks for a Laurent polynomial \(f=\sum\nu(\gamma)X^\gamma\) in
\[
I=J_1\cap\dots\cap J_s
\]
whose behaviour near the point \(X=(1,\dots,1)\) is prescribed to second order. To see this, write \(X_j=e^{Y_j}\): then \(X^\gamma=e^{\gamma\cdot Y}\), which is \(1+\gamma\cdot Y+\frac12(\gamma\cdot Y)^2+\dots\), so the three moment conditions say exactly that
\[
\begin{gathered}
f(e^{Y_1},\dots,e^{Y_k})\equiv\tfrac12Y^{\mathsf T}CY\\
\pmod{(Y_1,\dots,Y_k)^3}
\end{gathered}
\]
in the formal power series ring \(\mathbb Q[[Y_1,\dots,Y_k]]\). Steps 2 to 5 make this precise.

**Step 2: completion.** Put \(Z_j=X_j-1\) and \(\mathfrak m=(Z_1,\dots,Z_k)\subseteq R\). The ring \(R\) is obtained from the polynomial ring \(\mathbb Q[Z_1,\dots,Z_k]\) by inverting the elements \(1+Z_j\), so it is Noetherian, by the Hilbert basis theorem with its corollary on localizations (Theorem 2.1 of [Noetherian and Artinian rings](course:AG-CA/noetherian-and-artinian-rings)). Each \(1+Z_j\) is already invertible modulo \((Z)^n\), with inverse \(\sum_{m<n}(-Z_j)^m\). So \(R/\mathfrak m^n=\mathbb Q[Z]/(Z)^n\), and the completion \(\widehat R=\varprojlim R/\mathfrak m^n\) is the formal power series ring \(\mathbb Q[[Z_1,\dots,Z_k]]\). Since \(R\) is Noetherian, the map \(R\to\widehat R\) is flat (Theorem 3.2 of [Completion](course:AG-CA/completion)).

**Step 3: logarithmic coordinates.** The substitutions \(Z_j=e^{Y_j}-1\) and \(Y_j=\log(1+Z_j)\), with the usual exponential and logarithm series, are inverse to each other and identify \(\mathbb Q[[Z]]\) with \(\mathbb Q[[Y]]\); they carry the ideal \((Z_1,\dots,Z_k)\) to \((Y_1,\dots,Y_k)\), because each \(Z_j\) is \(Y_j\) times a unit and conversely. For \(h\in\Gamma\),
\[
\begin{aligned}
X^h-1&=e^{h\cdot Y}-1\\
&=(h\cdot Y)\sum_{n\ge0}\frac{(h\cdot Y)^n}{(n+1)!},
\end{aligned}
\]
and the last factor is a unit. Hence
\[
J_i\widehat R=(h\cdot Y:h\in\Lambda_i)\,\widehat R .
\]

**Step 4: the quadratic form lies in every \(J_i\widehat R\).** Let \(Q_2=\frac12Y^{\mathsf T}CY\). Fix \(i\), choose a basis \(g_1,\dots,g_m\) of \(V_i\), and extend it to a basis \(g_1,\dots,g_k\) of \(\mathbb Q^k\); let \(\Gamma_g\) be the invertible matrix with these columns. The linear forms \(\hat Y_c=g_c\cdot Y\) are new coordinates, with \(Y^{\mathsf T}CY=\hat Y^{\mathsf T}C'\hat Y\) for \(C'=\Gamma_g^{-1}C\,\Gamma_g^{-\mathsf T}\). In the basis \((g_c)\), the tensor \(\sum_{a,b}C_{ab}\,\varepsilon_a\otimes\varepsilon_b\) equals \(\sum_{c,e}C'_{ce}\,g_c\otimes g_e\). The classes of \(g_{m+1},\dots,g_k\) form a basis of \(\mathbb Q^k/V_i\) and the classes of \(g_1,\dots,g_m\) vanish, so by (T1) the hypothesis of the lemma says \(C'_{ce}=0\) whenever \(c>m\) and \(e>m\). Therefore every monomial of \(\hat Y^{\mathsf T}C'\hat Y\) contains a factor \(\hat Y_c\) with \(c\le m\), and
\[
\begin{aligned}
Q_2&\in(g_1\cdot Y,\dots,g_m\cdot Y)\\
&\subseteq(h\cdot Y:h\in\Lambda_i),
\end{aligned}
\]
the last inclusion because each \(g_c\) is a rational combination of elements of \(\Lambda_i\). By Step 3, \(Q_2\in J_i\widehat R\) for every \(i\).

**Step 5: from the completion back to \(R\).** The map \(R/I\to\bigoplus_{i=1}^sR/J_i\) is injective. Since \(\widehat R\) is flat over \(R\), it stays injective after tensoring with \(\widehat R\); as \((R/J)\otimes_R\widehat R=\widehat R/J\widehat R\), this says
\[
I\widehat R=J_1\widehat R\cap\dots\cap J_s\widehat R .
\]
Hence \(Q_2\in I\widehat R\), that is, \(Q_2=\sum_{a=1}^Nf_a\alpha_a\) with \(f_a\in I\) and \(\alpha_a\in\widehat R\). Truncate each \(\alpha_a\), written as a power series in \(Z\), after degree two; this gives a polynomial \(b_a\in\mathbb Q[Z]\subseteq R\) with \(\alpha_a-b_a\in(Z)^3\widehat R\). Then \(f=\sum_af_ab_a\) lies in \(I\), and \(f-Q_2=\sum_af_a(b_a-\alpha_a)\) lies in \((Z)^3\widehat R=(Y)^3\widehat R\).

Write \(f=\sum_\gamma\nu(\gamma)X^\gamma\) with finitely many terms. Since \(f\in J_i\), the pushforward of \(\nu\) to every \(\Gamma/\Lambda_i\) is zero (Step 1). Modulo \((Y)^3\),
\[
\begin{aligned}
f&=\sum_\gamma\nu(\gamma)\Bigl(1+\gamma\cdot Y+\tfrac12(\gamma\cdot Y)^2\Bigr)\\
&\equiv\tfrac12Y^{\mathsf T}CY ,
\end{aligned}
\]
and comparing the constant, linear and quadratic parts gives the three moment identities. \(\square\)

## 4. Exercises

**4.1** (medium). Take \(A=\{0,1\}\subset\mathbb R\), \(w_1=(0,1)\) and \(w_2=(1,0)\), and the tensor of Exercise 4.2 of the first lesson, which is \(T=w_1\otimes w_1-\frac12(w_1\otimes w_2+w_2\otimes w_1)\). Determine \(C\), \(\Lambda_1\) and \(\Lambda_2\), and check that
\[
\nu=\tfrac12\bigl(-\delta_{(0,0)}+\delta_{(1,0)}+\delta_{(-1,1)}-\delta_{(0,1)}\bigr)
\]
satisfies the conclusion of Lemma 2.1.

**4.2** (easy). Show that the moment conditions of Lemma 2.1 are unchanged when \(\nu\) is replaced by its translate \(\gamma\mapsto\nu(\gamma-\beta)\), for any \(\beta\in\Gamma\).

**4.3** (medium). Show that the flatness of \(\widehat R\) is really needed in Step 5 in the following sense: give two ideals \(J_1,J_2\) of a ring \(S\) and an \(S\)-module \(M\) for which \((J_1\cap J_2)\otimes M\to(J_1\otimes M)\cap(J_2\otimes M)\) is not onto, with the intersection taken in \(M\). (Take \(S=\mathbb Q[x,y]\), \(J_1=(x)\), \(J_2=(y)\) and \(M=S/(x-y)\).)

## 5. Solutions

**4.1.** Here
\[
\begin{aligned}
T=\tfrac12\bigl[{}&w_1\otimes w_1\\
&+(w_2-w_1)\otimes(w_2-w_1)\\
&-w_2\otimes w_2\bigr],
\end{aligned}
\]
which expands to the given form, so \(C=\begin{pmatrix}1&-1/2\\-1/2&0\end{pmatrix}\). Since \(e_1(w_1)=0\), \(e_1(w_2)=1\), \(e_2(w_1)=1\), \(e_2(w_2)=1\), we get \(e_1(w(\lambda))=\lambda_2\) and \(e_2(w(\lambda))=\lambda_1+\lambda_2\), so \(\Lambda_1=\mathbb Z\times\{0\}\) and \(\Lambda_2=\{\lambda_1+\lambda_2=0\}\). The four points \((0,0),(1,0),(-1,1),(0,1)\) have second coordinates \(0,0,1,1\) and coordinate sums \(0,1,0,1\); in both cases the weights \(-\frac12,\frac12,\frac12,-\frac12\) cancel in pairs. The total weight and the first moment vanish, and the second moment is
\[
\begin{aligned}
&\tfrac12\Bigl[\begin{pmatrix}1&0\\0&0\end{pmatrix}+\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\\
&\qquad-\begin{pmatrix}0&0\\0&1\end{pmatrix}\Bigr]=C .
\end{aligned}
\]

**4.2.** The pushforwards are translated by the class of \(\beta\), so they stay zero. With \(\gamma'=\gamma+\beta\), the total weight is unchanged, the first moment becomes \(\sum\nu(\gamma)(\gamma+\beta)=0+0\cdot\beta=0\), and the second moment becomes \(\sum\nu(\gamma)(\gamma+\beta)(\gamma+\beta)^{\mathsf T}\), which is \(C+0+0+0=C\).

**4.3.** In \(M=S/(x-y)\cong\mathbb Q[x]\), both images \(J_1M\) and \(J_2M\) equal \(xM\), so their intersection is \(xM\ne0\). But \(J_1\cap J_2=(xy)\), whose image is \(x^2M\), which does not contain \(x\). So intersecting ideals does not commute with extension to a module that is not flat.

## References

- [OpenAI-ER] OpenAI, *A classification of finite Euclidean Ramsey configurations*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026
- [Stacks] The Stacks Project Authors, *The Stacks Project*, Tag 00MB (completion of a Noetherian ring is flat). https://stacks.math.columbia.edu/tag/00MB
