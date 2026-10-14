# A Hirzebruch–Kummer surface

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By [The numerical obstruction](the-numerical-obstruction.md), the completed cone \(R(X,H)\) has no small Cohen–Macaulay module as soon as \(K_X^2-2c_2(X)>6H^2\) for an ample and globally generated \(H\). This lesson constructs such a surface: a cover of the plane blown up at four points, branched along the six lines through the four points and the four exceptional curves, obtained by taking \(n\)th roots of ratios of the linear forms. For \(n=7\) it has \(K_X^2-2c_2(X)=13377\) and a polarization with \(6H^2=10290\). This proves the main theorem of the course.

- Two named hypotheses: the blown-up plane, and Euler numbers (Section 1).
- The branch divisor (Lemma 2.1).
- The cover, its degree and its local form (Lemma 3.1, Proposition 3.3).
- The canonical class and the Chern numbers (Proposition 4.3).
- The polarization (Proposition 5.3).
- The counterexample and its uncompleted form (Theorem 6.1, Corollary 6.2).

The lesson follows [OpenAI-SCM, Sections 6 and 7]. The cover is an instance of the line-arrangement covers of Hirzebruch [Hirzebruch]; this complete-quadrangle polarization appears in [Anghel, Section 7.2].

## 1. Two named hypotheses

**Hypothesis (BL)** (the plane blown up at four points). Let \(p_1,\dots,p_4\in\mathbb P^2_{\mathbb C}\) be four points, no three on a line, and \(\sigma\colon B\to\mathbb P^2\) the blowup of the four points, with exceptional curves \(e_1,\dots,e_4\) and \(\ell=\sigma^*(\text{line})\). Then:

1. \(B\) is a smooth integral projective surface, \(\sigma\) is an isomorphism over \(\mathbb P^2\setminus\{p_1,\dots,p_4\}\), and each \(e_i\cong\mathbb P^1\);
2. \(\operatorname{Pic}B\) has the basis \(\ell,e_1,\dots,e_4\), with \(\ell^2=1\), \(\ell\cdot e_i=0\), \(e_i\cdot e_j=-\delta_{ij}\), and \(K_B=-3\ell+\sum_ie_i\);
3. the total transform of a line through \(p_i\) and \(p_j\) is \(L+e_i+e_j\), where the strict transform \(L\cong\mathbb P^1\) meets \(e_i\) transversally in the point given by the direction of the line at \(p_i\), and meets no other exceptional curve; the total transform of a line through no \(p_i\) is isomorphic to the line;
4. the topological Euler number of \(B\) is \(7\).

These are standard facts on blowups of points of a smooth surface ([Reid, Chapter 1, Section 1.10]); they are not proved in the programme.

**Hypothesis (EU)** (Euler numbers). For a complex algebraic variety \(Y\), let \(e_c(Y)\) be the Euler characteristic of \(Y(\mathbb C)\) with compact supports. Then:

1. if \(Z\subseteq Y\) is closed, \(e_c(Y)=e_c(Z)+e_c(Y\setminus Z)\);
2. if \(Y'\to Y\) is finite étale of degree \(d\), then \(e_c(Y')=d\,e_c(Y)\);
3. \(e_c(\text{point})=1\), \(e_c(\mathbb P^1)=2\), and \(e_c(Y)\) is the topological Euler number when \(Y\) is smooth and projective.

See [Behrend, Section 1.3]; these facts are not proved in the programme. With (NF) of the lesson on the obstruction, \(c_2(X)\) denotes this Euler number.

## 2. The branch divisor

Let \(p_1,\dots,p_4\) and \(B\) be as in (BL). Number the six lines joining two of the points \(1,\dots,6\), with linear forms \(l_1,\dots,l_6\). Let \(L_a\) be the strict transform of line \(a\) and \(T_a=\sigma^*(\text{line }a)\), so \(T_a=L_a+e_i+e_j\sim\ell\) if line \(a\) joins \(p_i\) and \(p_j\). Two lines are *opposite* if their pairs of endpoints are disjoint; there are three opposite pairs. Let \(I_i\) be the set of the three lines through \(p_i\). Put
\[
\Delta=\sum_{a=1}^6L_a+\sum_{i=1}^4e_i .
\]

**Lemma 2.1.**

1. \(\Delta\) is a reduced divisor with ten smooth rational components and simple normal crossings: every point lies on at most two components, which meet transversally there.
2. Each component meets the union of the others in exactly three points; there are fifteen such points (nodes): twelve of the form \(L_a\cap e_i\) with \(a\in I_i\), and three of the form \(L_a\cap L_b\) with \(a,b\) opposite.
3. \(\Delta\sim6\ell-2\sum_ie_i=-2K_B\), and \(K_B^2=5\).

**Proof.** By (BL)(3), \(e_i\) meets exactly the three \(L_a\) with \(a\in I_i\), in the points given by their three distinct directions at \(p_i\), transversally. Two lines through a common point \(p_i\) meet only at \(p_i\), so their strict transforms are disjoint (they meet \(e_i\) in different points). Two opposite lines meet in one point of \(\mathbb P^2\) different from the \(p_i\), transversally, and over this point \(\sigma\) is an isomorphism. The three points obtained from the three opposite pairs are distinct: if two of them coincided, two lines with a common endpoint would meet a second time. No point lies on three components: three of the \(L_a\) contain two lines with a common endpoint, and \(e_i\) meets only lines through \(p_i\). Exceptional curves are disjoint. This gives parts 1 and 2; each \(L_a\) meets two exceptional curves and its opposite line, each \(e_i\) meets three strict transforms. For part 3, each \(p_i\) lies on three lines, so \(\sum_aL_a=6\ell-3\sum_ie_i\), and \(\Delta=6\ell-2\sum_ie_i=-2K_B\) by (BL)(2). Finally \(K_B^2=9-4=5\). \(\blacksquare\)

## 3. The cover

Fix a prime \(n\ge3\). Let \(K=\mathbb C(B)=\mathbb C(\mathbb P^2)\), and in an algebraic closure choose \(y_1,\dots,y_5\) with
\[
y_a^n=r_a:=\frac{l_a}{l_6}\qquad(1\le a\le5) .
\]
Let \(K'=K(y_1,\dots,y_5)\), and let \(\pi\colon X\to B\) be the normalization of \(B\) in \(K'\): over an affine open \(\operatorname{Spec}C\subseteq B\) it is \(\operatorname{Spec}\) of the integral closure of \(C\) in \(K'\). This integral closure is finite over \(C\) (Theorem 5.1 of [Normalization](course:AG-MO/normalization), course *Morphisms of schemes*), so \(X\) is an integral normal projective surface and \(\pi\) is finite.

**Lemma 3.1.** \([K':K]=n^5\), and \(K'/K\) is Galois with group \((\mathbb Z/n)^5\).

**Proof.** *The valuations.* The divisor of the rational function \(r_a\) on \(B\) is \(T_a-T_6\). So its order along \(L_b\) is \(\delta_{ab}-\delta_{b6}\). If \(\prod_ar_a^{c_a}\) with integers \(c_a\) is an \(n\)th power in \(K\), its order along each \(L_b\), \(b\le5\), which is \(c_b\), is divisible by \(n\). So the classes of \(r_1,\dots,r_5\) in \(K^*/K^{*n}\) are independent over \(\mathbb Z/n\).

*Kummer theory.* \(K\) contains the \(n\)th roots of unity, so \(K'\) is the splitting field of the \(T^n-r_a\), hence Galois over \(K\), and \(\sigma\mapsto(\sigma(y_a)/y_a)_a\) embeds its group into \(\mu_n^5\cong(\mathbb Z/n)^5\). If the image were a proper subgroup, a nonzero linear form \(c\) on \((\mathbb Z/n)^5\) would vanish on it, since \(n\) is prime; then \(z=\prod_ay_a^{c_a}\) would be fixed by the group, so \(z\in K\) and \(\prod_ar_a^{c_a}=z^n\in K^{*n}\), contrary to independence. \(\blacksquare\)

**Lemma 3.2** (valuation vectors). Let \(U_n=\mathbb F_n^6/\langle(1,\dots,1)\rangle\), with the images \(\varepsilon_1,\dots,\varepsilon_6\) of the standard vectors, and identify \(U_n\) with \(\mathbb F_n^5\) by \(\varepsilon_1,\dots,\varepsilon_5\). The vector of orders modulo \(n\) of \(r_1,\dots,r_5\) along a component of \(\Delta\) is \(\varepsilon_a\) along \(L_a\) (\(1\le a\le6\)) and \(w_i=\sum_{a\in I_i}\varepsilon_a\) along \(e_i\). All these vectors are nonzero, and at each of the fifteen nodes the two vectors of the components through it are linearly independent.

**Proof.** Along \(L_b\), the order of \(r_a\) is \(\delta_{ab}-\delta_{b6}\); for \(b\le5\) this is the standard vector \(\varepsilon_b\), and for \(b=6\) it is \((-1,\dots,-1)\), which is \(\varepsilon_6=-\sum_{a\le5}\varepsilon_a\) in \(U_n\). Along \(e_i\), the order of \(l_a\) (as a section of \(\sigma^*\mathcal O(1)\)) is \(1\) if \(a\in I_i\) and \(0\) otherwise, so the vector is the image of the indicator vector of \(I_i\), which is \(w_i\). A vector \(\sum_{a\in J}\varepsilon_a\) with \(J\subseteq\{1,\dots,6\}\) is zero in \(U_n\) only if \(J\) is empty or everything, so all vectors are nonzero. At a node \(L_a\cap L_b\), \(a\ne b\), the vectors \(\varepsilon_a,\varepsilon_b\) are independent. At a node \(L_a\cap e_i\), \(a\in I_i\): suppose \(\lambda\varepsilon_a+\mu w_i=0\) in \(U_n\), that is, \(\lambda e_a+\mu\mathbf 1_{I_i}\) is a constant vector in \(\mathbb F_n^6\). A coordinate outside \(I_i\) shows that the constant is \(0\); a coordinate in \(I_i\setminus\{a\}\) then gives \(\mu=0\), and the coordinate \(a\) gives \(\lambda=0\). \(\blacksquare\)

**Proposition 3.3** (local form). \(X\) is smooth and \(\pi\) has degree \(d=n^5\). Let \(b\in B\) be a closed point that lies on exactly \(s\in\{0,1,2\}\) components of \(\Delta\). There are an étale neighbourhood \(U\to B\) of \(b\) with coordinates \(u_1,u_2\), the branches of \(\Delta\) through \(b\) pulling back to \(u_1=0,\dots,u_s=0\), such that \(X\times_BU\) is a disjoint union of \(n^{5-s}\) copies of
\[
\operatorname{Spec}\mathcal O(U)[t_1,\dots,t_s]/\bigl(t_j^n-u_j\bigr)_{j\le s} .
\]
In particular \(\pi\) is étale over \(B\setminus\Delta\), and over every point of a component of \(\Delta\) it has ramification index \(n\) along that component.

**Proof.** *Coordinates.* By Lemma 2.1 there are regular parameters \(u_1,u_2\) at \(b\) with the branches of \(\Delta\) through \(b\) equal to \(u_j=0\), \(j\le s\). On an affine neighbourhood \(\operatorname{Spec}C\) of \(b\) meeting no other component of \(\Delta\), the parameters define an étale map to \(\mathbb A^2\), and each radicand is \(r_a=\epsilon_a\prod_{j\le s}u_j^{\alpha_{aj}}\) with a unit \(\epsilon_a\in C^\times\) and integers \(\alpha_{aj}\), the orders of \(r_a\) along the branches.

*Removing the units.* \(C''=C[\eta_1,\dots,\eta_5]/(\eta_a^n-\epsilon_a)\) is étale over \(C\), since \(n\) and the \(\epsilon_a\) are units. Over a connected component \(\operatorname{Spec}C_1\) of \(\operatorname{Spec}C''\) containing a point over \(b\), the elements \(y'_a=y_a/\eta_a\) satisfy \(y_a'^n=\prod_ju_j^{\alpha_{aj}}\).

*Changing generators.* By Lemma 3.2, the \(s\) columns \((\alpha_{aj})_a\) are linearly independent modulo \(n\). Choose a matrix in \(\operatorname{GL}_5(\mathbb F_n)\) that maps them to the first \(s\) standard vectors, lift it to an integer matrix, and form the corresponding monomials \(Y_k=\prod_ay_a'^{\,g_{ka}}\), divided by monomials in the \(u_j\) to remove exponents divisible by \(n\). Since the matrix is invertible modulo \(n\), the \(y'_a\) are in turn monomials in the \(Y_k\) times monomials in the \(u_j\), so the \(Y_k\) generate the same algebra over the fraction field, and
\[
\begin{gathered}
Y_j^n=u_j\quad(j\le s),\\
Y_k^n=1\quad(k>s) .
\end{gathered}
\]
The equations \(Y_k^n=1\) split completely, since \(\mathbb C\) contains the roots of unity, and \(Y_j^n=u_j\), \(j\le s\), generate a field extension of degree \(n^s\), by the orders along \(u_j=0\). So \(K'\otimes_K\operatorname{Frac}C_1\) is a product of \(n^{5-s}\) copies of one field of degree \(n^s\).

*The normalization.* The algebra \(C_1[t_1,\dots,t_s]/(t_j^n-u_j)\) is finite and free over \(C_1\), and it is étale over \(\mathbb A^2\): it is the base change of the étale map \(\operatorname{Spec}C_1\to\mathbb A^2\) along the map \(\mathbb A^2\to\mathbb A^2\) raising the first \(s\) coordinates to the \(n\)th power. So it is smooth over \(\mathbb C\), hence normal, and it is the integral closure of \(C_1\) in its fraction field, the field of degree \(n^s\). On the other hand, normalization commutes with the étale base change \(C\to C_1\): the base change of the integral closure of \(C\) in \(K'\) is finite over \(C_1\), normal by Theorem 5.1 of [Étale morphisms and their local structure](course:AG-FSE/etale-morphisms-and-their-local-structure) (course *Flat, smooth and étale morphisms*), and has the total ring of fractions \(K'\otimes_K\operatorname{Frac}C_1\), so it is the integral closure of \(C_1\) there. Hence \(X\times_BU\), with \(U=\operatorname{Spec}C_1\), is the disjoint union of \(n^{5-s}\) copies of the displayed scheme. Each copy is smooth; smoothness descends along étale surjections (Theorem 5.1 of the same lesson), so \(X\) is smooth. The degree of \(\pi\) is \([K':K]=n^5\) by Lemma 3.1. \(\blacksquare\)

## 4. The canonical class and the Chern numbers

**Lemma 4.1** (projection formula). Let \(\pi\colon X\to B\) be a finite surjective morphism of degree \(d\) between smooth integral projective surfaces. Assume (CS) of [Elementary modifications and a variance inequality](elementary-modifications-and-a-variance-inequality.md). Then \(\pi^*D\cdot\pi^*E=d\,(D\cdot E)\) for all divisor classes \(D,E\) on \(B\).

**Proof.** \(V=\pi_*\mathcal O_X\) is a coherent sheaf of rank \(d\), and \(\chi(X,\pi^*L)=\chi(B,V\otimes L)\) for line bundles \(L\) by the projection formula. By (HI.1) of the lesson on cycle classes, \(\pi^*D\cdot\pi^*E\) is the alternating sum
\[
\begin{aligned}
&\chi(V(D+E))-\chi(V(D))\\
&\quad-\chi(V(E))+\chi(V) .
\end{aligned}
\] By (CS),
\[
\begin{aligned}
\chi(V(M))&=d\chi(\mathcal O_B)+\operatorname{ch}_2(V)\\
&\quad+c_1(V)\cdot M+\tfrac d2M^2\\
&\quad-\tfrac12\bigl(c_1(V)+dM\bigr)\cdot K_B .
\end{aligned}
\]
In the alternating sum the terms independent of \(M\) and the terms linear in \(M\) cancel, and the quadratic terms give \(\tfrac d2\bigl((D+E)^2-D^2-E^2\bigr)=d\,D\cdot E\). \(\blacksquare\)

**Lemma 4.2** (the canonical class). Let \(\Delta_1,\dots,\Delta_{10}\) be the components of \(\Delta\), and \(\widetilde\Delta_c=\pi^{-1}(\Delta_c)_{\mathrm{red}}\). Then \(\pi^*\Delta_c=n\widetilde\Delta_c\), and
\[
K_X=\pi^*K_B+(n-1)\sum_c\widetilde\Delta_c .
\]

**Proof.** In the local form of Proposition 3.3, \(\pi^*u_j=t_j^n\), and \(t_j=0\) defines \(\widetilde\Delta_c\) for the corresponding branch. Since \(X\) and \(B\) are smooth surfaces, the canonical bundles are the top exterior powers of the cotangent bundles, and \(\pi\) induces a map \(\pi^*\omega_B\to\omega_X\) that is an isomorphism over \(B\setminus\Delta\), where \(\pi\) is étale. Étale maps identify cotangent bundles, so the map can be computed in the coordinates of Proposition 3.3: for \(s=1\), \(\pi^*(du_1\wedge du_2)=n\,t_1^{n-1}\,dt_1\wedge du_2\), and for \(s=2\), \(\pi^*(du_1\wedge du_2)=n^2t_1^{n-1}t_2^{n-1}\,dt_1\wedge dt_2\). So the divisor of zeros of the map is \((n-1)\sum_c\widetilde\Delta_c\). \(\blacksquare\)

**Proposition 4.3** (Chern numbers; [OpenAI-SCM, Section 6.3]). Assume (BL), (EU) and (CS). With \(d=n^5\),
\[
\begin{aligned}
K_X^2&=5d\Bigl(1-\frac2n\Bigr)^2,\\
c_2(X)&=d\Bigl(2-\frac{10}n+\frac{15}{n^2}\Bigr),\\
K_X^2-2c_2(X)&=d\Bigl(1-\frac{10}{n^2}\Bigr) .
\end{aligned}
\]

**Proof.** *Canonical class.* By Lemma 4.2, as classes with rational coefficients,
\[
\begin{aligned}
K_X&=\pi^*\Bigl(K_B+\bigl(1-\tfrac1n\bigr)\Delta\Bigr)\\
&=\pi^*\Bigl(K_B-2\bigl(1-\tfrac1n\bigr)K_B\Bigr)\\
&=\Bigl(1-\frac2n\Bigr)\pi^*(-K_B),
\end{aligned}
\]
using \(\Delta\sim-2K_B\). Lemma 4.1 and \(K_B^2=5\) give \(K_X^2\).

*Euler number.* Stratify \(B\) into \(B\setminus\Delta\), the one-branch part \(\Delta^\circ\) (the components minus the nodes) and the fifteen nodes. By (EU) and (BL)(4): each component is a \(\mathbb P^1\) minus three nodes, of Euler number \(-1\), so \(e_c(\Delta^\circ)=-10\); \(e_c(\Delta)=-10+15=5\); and \(e_c(B\setminus\Delta)=7-5=2\). By Proposition 3.3, over a stratum with \(s\) branches the reduced preimage is finite étale of degree \(n^{5-s}=d/n^s\). By (EU),
\[
c_2(X)=e_c(X)=2d-\frac{10\,d}n+\frac{15\,d}{n^2} .
\]

*Difference.*
\[
\begin{aligned}
&5\bigl(1-\tfrac2n\bigr)^2-2\bigl(2-\tfrac{10}n+\tfrac{15}{n^2}\bigr)\\
&\quad=5-\tfrac{20}n+\tfrac{20}{n^2}-4+\tfrac{20}n-\tfrac{30}{n^2}\\
&\quad=1-\tfrac{10}{n^2} .
\end{aligned}
\] \(\blacksquare\)

## 5. The polarization

Put, as divisors on the smooth surface \(X\),
\[
R_a=\widetilde L_a,\qquad F_i=\widetilde e_i,\qquad E=\sum_iF_i ,
\]
and \(J_a=\frac1n\pi^*T_a=R_a+F_i+F_j\) if line \(a\) joins \(p_i,p_j\) (Lemma 4.2), and \(J=J_6\).

**Lemma 5.1.**

1. \(\operatorname{div}(y_a)=J_a-J\) for \(a\le5\); so all \(J_a\) are linearly equivalent to \(J\), and there are sections \(z_1,\dots,z_6\) of \(\mathcal O_X(J)\) with zero divisors \(J_1,\dots,J_6\). They have no common zero.
2. For an opposite pair \(a,b\), \(J_a+J_b=R_a+R_b+E\), and \(z_az_b\) divided by the canonical section of \(\mathcal O_X(E)\) is a section of \(\mathcal O_X(2J-E)\) with zero divisor \(R_a+R_b\). The three sections so obtained have no common zero.
3. \(H=3J-E\) is globally generated, and \(nH\sim\pi^*(-K_B)\).

**Proof.** *Part 1.* \(n\operatorname{div}(y_a)=\operatorname{div}(r_a)\), and \(\operatorname{div}(r_a)=\pi^*(T_a-T_6)=n(J_a-J)\) as divisors, and divisors form a free abelian group. On \(B\), the six total transforms \(T_a\) have no common point: off the exceptional curves, no point lies on all six lines; on \(e_i\), the total transform of a line not through \(p_i\) does not meet \(e_i\). So the supports of the \(J_a\), which are the preimages of the supports of the \(T_a\), have no common point.

*Part 2.* For opposite \(a,b\), the four endpoints are \(p_1,\dots,p_4\), so \(J_a+J_b=R_a+R_b+E\). For different opposite pairs, \(L_a\cup L_b\) and \(L_{a'}\cup L_{b'}\) are disjoint on \(B\): each line of one pair has a common endpoint with each line of the other pair, so their strict transforms are disjoint (proof of Lemma 2.1). So the three zero divisors \(R_a+R_b\) have no common point.

*Part 3.* \(H=J+(2J-E)\) is a sum of globally generated divisors, hence globally generated. Since \(T_6\sim\ell\),
\[
\begin{aligned}
nH&=3\pi^*T_6-\pi^*\Bigl(\sum_ie_i\Bigr)\\
&\sim\pi^*\Bigl(3\ell-\sum_ie_i\Bigr)=\pi^*(-K_B) .
\end{aligned}
\] \(\blacksquare\)

For an integral curve \(\Gamma\) on a smooth projective surface and a line bundle \(L\), put \(\deg(L|_\Gamma)=\chi(L|_\Gamma)-\chi(\mathcal O_\Gamma)\). By Theorem 2.1 of [Euler characteristics and Hilbert polynomials](course:AG-QC/euler-characteristics-and-hilbert-polynomials), \(\chi(L^t|_\Gamma)\) is a polynomial of degree at most one in \(t\), so \(\deg\) is additive in \(L\). By surface Riemann–Roch (HI.17), the pairing (HI.1) also equals
\[
\begin{aligned}
L\cdot M&=\chi(\mathcal O)-\chi(-L)\\
&\quad-\chi(-M)+\chi(-L-M) .
\end{aligned}
\] For \(M=\mathcal O(\Gamma)\), the ideal sequences \(0\to\mathcal O(-\Gamma)\to\mathcal O\to\mathcal O_\Gamma\to0\) and \(0\to L^{-1}(-\Gamma)\to L^{-1}\to L^{-1}|_\Gamma\to0\) give \(L\cdot\Gamma=\chi(\mathcal O_\Gamma)-\chi(L^{-1}|_\Gamma)=\deg(L|_\Gamma)\). If \(L|_\Gamma\) has a nonzero section, \(\deg(L|_\Gamma)\ge0\): the section gives \(0\to\mathcal O_\Gamma\to L|_\Gamma\to Q\to0\) with \(Q\) of finite length. If \(L|_\Gamma\) is trivial, \(\deg(L|_\Gamma)=0\).

**Lemma 5.2.** Assume (BL). \(-K_B\) is ample on \(B\).

**Proof.** *Global generation.* \(\ell\) is globally generated. For an opposite pair \(a,b\), the conic \(l_al_b\) passes through the four points, and its total transform is \(T_a+T_b=L_a+L_b+\sum_ie_i\); so \(2\ell-\sum_ie_i\) has a section with zero divisor \(L_a+L_b\). By part 2 of the proof of Lemma 5.1, the three such divisors have no common point, so \(2\ell-\sum_ie_i\) is globally generated, and so is \(-K_B=\ell+(2\ell-\sum_ie_i)\).

*Positivity on curves.* Let \(\Gamma\subseteq B\) be an integral curve. Both summands are globally generated, so their restrictions to \(\Gamma\) have nonzero sections and nonnegative degree. If \(\Gamma\) is not one of the \(e_j\), then \(\sigma\) restricted to \(\Gamma\) is proper with finite fibers, hence finite, and \(\ell|_\Gamma\) is the pullback of the ample \(\mathcal O(1)\) along it, hence ample (cohomological criterion, as below); so \(\ell\cdot\Gamma=\deg(\ell|_\Gamma)>0\) by Theorem 3.1 of the lesson on Euler characteristics. If \(\Gamma=e_j\), then \((2\ell-\sum_ie_i)\cdot e_j=1\) by (BL)(2). So \(-K_B\cdot\Gamma>0\) for every integral curve.

*Ampleness.* The morphism \(\varphi\colon B\to\mathbb P^M\) defined by a basis of global sections of \(-K_B\) satisfies \(\varphi^*\mathcal O(1)=\mathcal O_B(-K_B)\). If a fiber had positive dimension, it would contain an integral curve \(\Gamma\) on which \(\mathcal O_B(-K_B)\) is trivial, so \(-K_B\cdot\Gamma=0\), which is excluded. So \(\varphi\) is proper and quasi-finite, hence finite (Theorem 5.1 of [Zariski's main theorem](course:AG-MO/zariskis-main-theorem)). For a coherent sheaf \(F\) on \(B\), \(H^q(B,F\otimes\varphi^*\mathcal O(m))\) equals \(H^q(\mathbb P^M,\varphi_*F(m))\), which vanishes for \(q>0\) and large \(m\); by the cohomological criterion (Theorem 4.1 of [Serre's theorems on projective schemes](course:AG-QC/serres-theorems-on-projective-schemes)), \(-K_B\) is ample. \(\blacksquare\)

**Proposition 5.3** (the polarization; [OpenAI-SCM, Proposition 6.1]). Assume (BL), (EU) and (CS). \(H=3J-E\) is ample and globally generated, and
\[
\begin{gathered}
H^2=5n^3,\\
K_X^2-2c_2(X)=n^3(n^2-10) .
\end{gathered}
\]

**Proof.** Global generation is Lemma 5.1. The pullback of an ample line bundle along the finite morphism \(\pi\) is ample, by the same cohomological argument as in Lemma 5.2; so \(nH\sim\pi^*(-K_B)\) is ample, and so is \(H\) (Proposition 1.2 of [Ample invertible sheaves](course:AG-MO/ample-invertible-sheaves)). By Lemma 4.1, \(n^2H^2=d\,K_B^2=5n^5\). The second formula is Proposition 4.3 with \(d=n^5\). \(\blacksquare\)

## 6. The counterexample

**Theorem 6.1** ([OpenAI-SCM, Theorem 1.1]). Assume (CS), (NF), (BI), (BL) and (EU). For \(n=7\), the completed cone \(R=R(X,H)\) is a three-dimensional complete Noetherian normal local domain containing \(\mathbb C\), with residue field \(\mathbb C\), and no nonzero finitely generated \(R\)-module has depth three.

**Proof.** For \(n=7\), Proposition 5.3 gives \(H^2=5\cdot343=1715\) and \(K_X^2-2c_2(X)=343\cdot39=13377\), while \(6H^2=10290\). So \(K_X^2-2c_2(X)>6H^2\), and Corollary 3.4 of [The numerical obstruction](the-numerical-obstruction.md) applies. \(\blacksquare\)

For \(n=3\) and \(n=5\), \(n^2-10\) is negative or \(15\), and \(15\le30\); the obstruction needs \(n^2-10>30\), so \(n=7\) is the smallest prime that works (Exercise 7.1).

**Corollary 6.2** ([OpenAI-SCM, Corollary 7.1]). Under the same hypotheses, let \(T=T(X,H)\) and \(\mathfrak n=T_{>0}\). Then \(T_{\mathfrak n}\) is a three-dimensional local domain essentially of finite type over \(\mathbb C\), with residue field \(\mathbb C\), without a nonzero finitely generated module of depth three.

**Proof.** By Proposition 3.1 of [Completed cones over surfaces](completed-cones-over-surfaces.md), \(T\) is a domain finite over a polynomial ring in three variables, hence a finitely generated \(\mathbb C\)-algebra; \(\mathfrak n\) is maximal since \(T_0=\mathbb C\); and the completion of \(R_0=T_{\mathfrak n}\) is \(R\), so \(\dim R_0=\dim R=3\). Let \(M\) be a nonzero finite \(R_0\)-module with an \(M\)-regular sequence \(z_1,z_2,z_3\) in the maximal ideal. The completion \(R_0\to R\) is faithfully flat (Theorem 3.2 of [Completion](course:AG-CA/completion), and its spectrum map is surjective, Theorem 2.1 of [Faithful flatness and the local criterion for flatness](course:AG-CA/faithful-flatness-and-the-local-criterion-for-flatness)), and \(\widehat M=M\otimes_{R_0}R\). Put \(M_i=M/(z_1,\dots,z_i)M\). The exact sequences \(0\to M_i\xrightarrow{z_{i+1}}M_i\to M_{i+1}\to0\) stay exact after \(\otimes_{R_0}R\), and \(M_i\otimes_{R_0}R=\widehat M/(z_1,\dots,z_i)\widehat M\), which is nonzero by faithful flatness (Theorem 2.2 there) since \(M_i\ne0\) by Nakayama's lemma. So \(z_1,z_2,z_3\) is \(\widehat M\)-regular, and \(\widehat M\) is a nonzero finite \(R\)-module of depth three, contradicting Theorem 6.1. \(\blacksquare\)

## 7. Exercises

**7.1.** Compute \(H^2\), \(K_X^2-2c_2(X)\) and \(6H^2\) for \(n=3,5,7,11\), and decide in which cases Theorem 3.3 of the lesson on the obstruction excludes small Cohen–Macaulay modules.

**7.2.** Check that the Euler number formula of Proposition 4.3 is an integer for every \(n\), and compute \(\chi(\mathcal O_X)\) from (NF).

**7.3.** How many points does \(X\) have over a node of \(\Delta\), over a point of \(\Delta\) that is not a node, and over a point of \(B\setminus\Delta\)? Check that the Euler number in Proposition 4.3 is the sum, over the three strata, of these counts times the Euler numbers of the strata.

**7.4.** Verify that each component of \(\Delta\) meets exactly three others, by drawing the incidence graph: its vertices are the ten components and its edges the fifteen nodes. Show that it is the Petersen graph.

**7.5.** Show that \(\pi^*(-K_B)\) is divisible by \(n\) in \(\operatorname{Pic}X\), but \(-K_B\) is not divisible in \(\operatorname{Pic}B\).

## 8. Solutions

**7.1.** \(H^2=5n^3\) and \(K_X^2-2c_2(X)=n^3(n^2-10)\). For \(n=3\): \(135\) and \(-27\le810\). For \(n=5\): \(625\) and \(1875\le3750\). For \(n=7\): \(1715\) and \(13377>10290\). For \(n=11\): \(6655\) and \(147741>39930\). The obstruction applies when \(n^2-10>30\), that is, for the primes \(n\ge7\).

**7.2.** \(c_2(X)=2n^5-10n^4+15n^3\), an integer. \(K_X^2=5n^3(n-2)^2\). By (NF),
\[
\begin{aligned}
\chi(\mathcal O_X)&=\tfrac1{12}\bigl(5n^3(n-2)^2\\
&\qquad+2n^5-10n^4+15n^3\bigr)\\
&=\tfrac{n^3}{12}\bigl(7n^2-30n+35\bigr) .
\end{aligned}
\] For \(n=7\) this is \(\frac{343\cdot168}{12}=4802\).

**7.3.** By Proposition 3.3, \(n^5\) points over \(B\setminus\Delta\), \(n^4\) over a point of \(\Delta\) that is not a node, and \(n^3\) over a node. The strata have Euler numbers \(2\), \(-10\) and \(15\), and \(2n^5-10n^4+15n^3=n^5\bigl(2-\frac{10}n+\frac{15}{n^2}\bigr)\).

**7.4.** By Lemma 2.1 every component meets three others; the graph has ten vertices of degree three and fifteen edges. Write \(L_{ij}\) for the strict transform of the line through \(p_i,p_j\); it is adjacent to \(e_i\), \(e_j\) and the opposite \(L_{kl}\), where \(\{k,l\}=\{1,2,3,4\}\setminus\{i,j\}\). Send \(L_{ij}\) to the pair \(\{k,l\}\) and \(e_i\) to the pair \(\{i,5\}\). This is a bijection onto the ten two-element subsets of \(\{1,\dots,5\}\), and adjacent components go to disjoint pairs: \(\{k,l\}\) is disjoint from \(\{i,5\}\), \(\{j,5\}\) and \(\{i,j\}\). Conversely, \(L_{ij}\) and \(e_k\) go to \(\{k,l\}\) and \(\{k,5\}\), two lines with a common endpoint \(p_i\) go to pairs sharing an element, and two exceptional curves go to pairs containing \(5\). So the graph is the graph of two-element subsets of a five-element set with disjoint subsets adjacent: the Petersen graph.

**7.5.** \(\pi^*(-K_B)\sim nH\) by Lemma 5.1. On \(B\), \(-K_B=3\ell-\sum_ie_i\) has coefficient \(3\) on \(\ell\) and \(-1\) on each \(e_i\) in a basis of \(\operatorname{Pic}B\), so it is not a multiple \(mD\) with \(m\ge2\).

## References

- [OpenAI-SCM] OpenAI, *A Complete Local Domain without a Small Cohen–Macaulay Module*, OpenAI Math Release preprint, 23 September 2026, Sections 6 and 7. https://github.com/openai/math/tree/main/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026
- [Hirzebruch] F. Hirzebruch, *Arrangements of lines and algebraic surfaces*, in: Arithmetic and Geometry, Vol. II, 1983. https://hirzebruch.mpim-bonn.mpg.de/id/eprint/244/
- [Anghel] C. Anghel, *Smooth counterexamples to the Eisenbud–Schreyer–Weyman Ulrich existence problem*, arXiv:2609.02718, version 1, Section 7.2. https://arxiv.org/abs/2609.02718
- [Reid] M. Reid, *Chapters on algebraic surfaces*, in: Complex Algebraic Geometry (Park City, 1993), Chapter 1, Section 1.10. https://arxiv.org/abs/alg-geom/9602006
- [Behrend] K. Behrend, *Donaldson–Thomas type invariants via microlocal geometry*, Ann. of Math. 170 (2009), Section 1.3. https://arxiv.org/abs/math/0507523
