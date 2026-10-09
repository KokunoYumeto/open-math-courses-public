# The curve inequality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In \(\mathbb C^{m+1}\), with coordinates \(Y,X_1,\dots,X_m\), fix \(K\) points \(a_j=(1,c_{j1},\dots,c_{jm})\) and through each of them the formal logarithmic curves

\[
Y=1+t,\qquad X_i=c_{ji}+\log(1+t),
\]

thickened by transverse variables \(u_i=X_i-c_{ji}-\log Y\). This lesson proves that, for suitable *separated* weights, every algebraic curve has weighted degree larger than its total weighted contact with these logarithmic curves at the points \(a_j\). The proof is a zero estimate: a curve with too much contact would carry an auxiliary polynomial with many vanishing derivatives; the derivatives would vanish on a whole subvariety \(Z\); the multiplicity estimate of [Weighted multiplicity estimates](weighted-multiplicity-estimates.md), combined with the separation of the weights, forces \(Z\) to be tangent to the hyperplanes \(dX_i=dY/Y\); and a residue computation shows that such a \(Z\) lies in \(Y=1\). Inside \(Y=1\) the same argument, now with ordinary partial derivatives, leads to a contradiction. The curve inequality is the input to the interpolation theorem of [Interpolation on logarithmic curves](interpolation-on-logarithmic-curves.md).

We use Theorem 3.1 and the frame (1.1) of [Weighted multiplicity estimates](weighted-multiplicity-estimates.md); that a nonzero rational function on a normal projective curve has as many zeros as poles, and a nonconstant one has a zero or a pole, Corollary 3.3 of [Intersection numbers of line bundles](course:intersection-numbers-and-positivity/intersection-numbers-of-line-bundles#3-pullback-and-positivity); that normalization of an integral projective curve is finite, with discrete valuation rings as local rings at closed points, [Normalization](course:AG-MO/normalization#5-finiteness-over-fields-including-inseparability) and [Discrete valuation rings, normal rings and Serre's criterion](course:AG-CA/discrete-valuation-rings-normal-rings-and-serres-criterion). Varieties are complex; a *curve* is an integral closed algebraic curve.

## 1. Data and separated weights

Fix integers \(m,K\ge1\) and positive rational numbers \(w_0,v_0,\theta\) with

\[
0<\theta<1,\qquad K\theta^m<1,\qquad K\frac{w_0}{v_0}\theta^m<1 .
\tag{1.1}
\]

Choose a positive rational \(\sigma\) so small that

\[
(1+3\sigma)^{m+1}K\frac{w_0}{v_0}\theta^m<1,\qquad(1+3\sigma)^mK\theta^m<1,\qquad(1+\sigma)\theta<1,
\tag{1.2}
\]

and put \(L_0=m+2\) and \(C_*=\max_{1\le k\le m}k!\,(L_0/\sigma)^k\). For positive rational *degree weights* \(w_1,\dots,w_m\) we always set the *order weights*

\[
v_i=w_i/\theta\qquad(1\le i\le m),
\]

so the order weight \(v_0\) is given while \(v_1,\dots,v_m\) follow the \(w_i\). Write \(W=(w_0,\dots,w_m)\) and \(V=(v_0,\dots,v_m)\).

**Definition 1.1.** The weights \(w_1,\dots,w_m\) are *separated* if for every pair of subsets \(A,B\subseteq\{0,1,\dots,m\}\) with \(|A|=|B|\in\{1,\dots,m\}\) whose symmetric difference contains a positive index, and whose largest positive index in \(A\triangle B\) belongs to \(A\),

\[
\prod_{a\in A}w_a>C_*\prod_{b\in B}v_b .
\tag{1.3}
\]

**Lemma 1.2.** There are thresholds \(T_1,T_2(w_1),\dots,T_m(w_1,\dots,w_{m-1})\), depending only on \(m,w_0,v_0,\theta,\sigma\) and the previously chosen weights, such that any choice with \(w_i>T_i\) for all \(i\) is separated.

**Proof.** Consider a pair \((A,B)\) whose largest positive differing index is \(i\in A\setminus B\). Every index \(l>i\) lies in both sets or in neither, and in the first case contributes \(w_l/v_l=\theta\) to the ratio \(\prod_Aw_a/\prod_Bv_b\). So this ratio equals \(w_i\) times a positive number depending only on \(\theta\), \(w_0\), \(v_0\) and \(w_1,\dots,w_{i-1}\). Let \(T_i\) be the largest of the finitely many values \(C_*\) divided by these numbers. \(\square\)

The thresholds do not depend on the points \(a_j\). This is what will allow the weights \(w_i=\lceil\log q_i\rceil\) to be chosen from rational approximations before the centres \(2ijp_i/q_i\) are known.

The *centres* are points \(a_j=(1,c_{j1},\dots,c_{jm})\in\mathbb C^{m+1}\), \(0\le j<K\), such that for each \(i\) the numbers \(c_{0i},\dots,c_{K-1,i}\) are pairwise distinct. At \(a_j\), the completed local ring of \(\mathbb C^{m+1}\) is \(\mathbb C[[Y-1,X-c_j]]\), and

\[
t=Y-1,\qquad u_i=X_i-c_{ji}-\log(1+t),\qquad\log(1+t)=\sum_{n\ge1}\frac{(-1)^{n+1}t^n}n,
\]

form a regular system of parameters, hence formal coordinates. The *\(V\)-weight* of \(t^su^\beta\) is \(v_0s+\sum_iv_i\beta_i\), and a series has *\(V\)-order* at least \(T\) if all monomials in its expansion have \(V\)-weight at least \(T\).

## 2. Degree and contact of a curve

Let \(C\subseteq\mathbb C^{m+1}\) be a curve. Its closure in \(\mathbf P^{m+1}\) is an integral projective curve; let \(\widetilde C\) be its normalization, the *smooth projective model* of \(C\). The local rings of \(\widetilde C\) at its points are discrete valuation rings; write \(\operatorname{ord}_P\) for the valuation at \(P\) on the function field \(\mathbb C(C)\), and \(\widehat{\mathcal O}_{\widetilde C,P}=\mathbb C[[s]]\) for a uniformizer \(s\). Points of \(\widetilde C\) over a point \(a\in C\) are called *branches* of \(C\) at \(a\).

**Definition 2.1.** The *\(W\)-degree* of \(C\) is

\[
\deg_WC=\sum_{P\in\widetilde C}M_P,\qquad M_P=\max\Bigl\{0,-\frac{\operatorname{ord}_PY}{w_0},-\frac{\operatorname{ord}_PX_1}{w_1},\dots,-\frac{\operatorname{ord}_PX_m}{w_m}\Bigr\},
\]

with the convention \(\operatorname{ord}_P0=+\infty\). Only the finitely many points over infinity contribute. For a branch \(P\) at a centre \(a_j\), the morphism \(\widetilde C\to\mathbb C^{m+1}\) induces \(\mathbb C[[t,u]]\to\mathbb C[[s]]\), and the *contact* of \(P\) is

\[
h_P=\min\Bigl\{\frac{\operatorname{ord}_Pt}{v_0},\frac{\operatorname{ord}_Pu_1}{v_1},\dots,\frac{\operatorname{ord}_Pu_m}{v_m}\Bigr\}.
\]

All these orders are positive, since \(t\) and the \(u_i\) vanish at \(a_j\). They are not all infinite: otherwise \(Y\) and the \(X_i\) would be constant on the branch, hence on \(C\). So \(0<h_P<\infty\). For branches at other points put \(h_P=0\).

**Lemma 2.2.**

1. If \(F\) is a polynomial of \(W\)-degree at most \(N\), then \(F|_C\), as a rational function on \(\widetilde C\), has total pole order at most \(N\deg_WC\).
2. If a series in \(\mathbb C[[t,u]]\) has \(V\)-order at least \(T\) at \(a_j\), its image in \(\mathbb C[[s]]\) at a branch \(P\) at \(a_j\) has order at least \(Th_P\).

**Proof.** (1) At \(P\), a monomial \(Y^hX^\alpha\) has order \(h\operatorname{ord}_PY+\sum\alpha_i\operatorname{ord}_PX_i\ge-(w_0h+\sum w_i\alpha_i)M_P\ge-NM_P\), and the order of a sum is at least the minimum. (2) A monomial \(t^su^\beta\) has order \(s\operatorname{ord}_Pt+\sum\beta_i\operatorname{ord}_Pu_i\ge(v_0s+\sum v_i\beta_i)h_P\ge Th_P\). The image of the series is the \(s\)-adically convergent sum of the images of its monomials, since \(h_P>0\) and the weights of the monomials tend to infinity. \(\square\)

## 3. Auxiliary polynomials

**Lemma 3.1** (counting). Let \(\Lambda\) be a set of \(n\) positive rational weights. The number of multi-indices \(\alpha\in\mathbb N^n\) with \(\sum_i\lambda_i\alpha_i\le T\) (or \(<T\)) is \(T^n/(n!\prod_i\lambda_i)\cdot(1+o(1))\) as \(T\to\infty\).

**Proof.** The unit cubes \(\alpha+[0,1)^n\) over the admissible \(\alpha\) cover the simplex of size \(T\) and lie in the simplex of size \(T+\sum_i\lambda_i\). \(\square\)

**Lemma 3.2.** For every sufficiently large \(N\) there is a nonzero polynomial \(F_N(Y,X)\) of \(W\)-degree at most \(N\) whose expansion at every centre \(a_j\) has \(V\)-order at least \((1+3\sigma)N\).

**Proof.** The coefficients of \(F_N\) are unknowns; their number is the count of exponents \((h,\alpha)\) with \(w_0h+\sum w_i\alpha_i\le N\). Each condition "the coefficient of \(t^su^\beta\) at \(a_j\) vanishes" is linear in them, and there are \(K\) times the number of \((s,\beta)\) with \(v_0s+\sum v_i\beta_i<(1+3\sigma)N\). By Lemma 3.1, the ratio of the number of conditions to the number of unknowns tends to \(K(1+3\sigma)^{m+1}\prod_aw_a/\prod_av_a=K(1+3\sigma)^{m+1}(w_0/v_0)\theta^m<1\), by (1.2). For large \(N\) there are more unknowns than conditions. \(\square\)

The commuting frame (1.1) of the multiplicity lesson,

\[
D_0=Y\partial_Y+\sum_{i=1}^m\partial_{X_i},\qquad D_i=\partial_{X_i},
\]

on \(U=\{Y\ne0\}\), maps polynomials of \(W\)-degree at most \(N\) to polynomials of \(W\)-degree at most \(N\): \(D_0(Y^hX^\alpha)=hY^hX^\alpha+\sum_i\alpha_iY^hX^{\alpha-e_i}\). In the formal coordinates at a centre, \(D_0t=Y=1+t\), \(D_0u_i=1-D_0t/(1+t)=0\), \(D_it=0\) and \(D_iu_l=\delta_{il}\), so

\[
D_0=(1+t)\partial_t,\qquad D_i=\partial_{u_i}.
\tag{3.1}
\]

Hence \(D_a\) lowers the \(V\)-order by at most \(v_a\). Give \(D_a\) the *cost* \(v_a\), and \(D^\gamma\) the cost \(\sum_av_a\gamma_a\).

## 4. The curve inequality

**Theorem 4.1** (curve inequality). Let the weights \(w_1,\dots,w_m\) be separated. Then every curve \(C\subseteq\mathbb C^{m+1}\) satisfies

\[
\deg_WC\ge(1+\sigma)\sum_{P}h_P ,
\tag{4.1}
\]

the sum running over all branches of \(C\) at the centres.

**Proof.** If \(C\) misses the centres, the right side is zero. Suppose that \(C\) meets a centre and that (4.1) fails: \(\deg_WC<(1+\sigma)\sum_Ph_P\).

*Step 1: derivatives vanish on \(C\).* Take \(F_N\) from Lemma 3.2, \(N\) large. If \(\gamma\) has cost at most \(\sigma N\), the polynomial \(D^\gamma F_N\) has \(W\)-degree at most \(N\) and \(V\)-order at least \((1+2\sigma)N\) at every centre. Suppose \(D^\gamma F_N|_C\ne0\). By Lemma 2.2 its zeros at the branches over the centres have total order at least \((1+2\sigma)N\sum_Ph_P\), which exceeds \(N\deg_WC\) (if \(\deg_WC>0\) because \((1+2\sigma)/(1+\sigma)>1\), and if \(\deg_WC=0\) because \(\sum h_P>0\)), while its poles have total order at most \(N\deg_WC\). This contradicts the equality of the numbers of zeros and poles. So

\[
D^\gamma F_N\big|_C=0\qquad\text{for every }\gamma\text{ of cost at most }\sigma N .
\]

*Step 2: a persistent component.* Put \(\delta=\sigma N/L_0\), and for \(0\le r\le L_0\) let \(V_r\subseteq U\) be the common zero set of the \(D^\gamma F_N\) of cost at most \(r\delta\). These form a decreasing chain, and \(C^\circ=C\cap U\), which is nonempty since \(C\) meets a centre, lies in \(V_{L_0}\). Choose an irreducible component \(Z_{L_0}\supseteq C^\circ\) of \(V_{L_0}\), and successively irreducible components \(Z_{r}\supseteq Z_{r+1}\) of \(V_r\). Each \(Z_r\) contains a curve and lies in the hypersurface \(V(F_N)\cap U\), so \(1\le\dim Z_r\le m\). A chain of \(L_0+1=m+3\) irreducible closed sets with dimensions in \([1,m]\) has two equal neighbours: \(Z_{r+1}=Z_r=:Z\) for some \(r\). Let \(k\) be the codimension of \(Z\) in \(\mathbb C^{m+1}\), \(1\le k\le m\).

*Step 3: comparison of normal bases.* The polynomials \(f=D^\gamma F_N\), cost\((\gamma)\le r\delta\), have \(W\)-degree at most \(N\), and \(Z\) is an irreducible component of their common zero set in \(U\). For \(\gamma'\) of cost less than \(\delta\), \(D^{\gamma'}f=D^{\gamma+\gamma'}F_N\) has cost at most \((r+1)\delta\), so it vanishes on \(V_{r+1}\supseteq Z\). Theorem 3.1 of the multiplicity lesson, with degree weights \(W\), costs \(V\) and \(\varepsilon=\sigma/L_0\), gives

\[
\prod_{a\in A}w_a\le k!\,(L_0/\sigma)^k\prod_{b\in B}v_b\le C_*\prod_{b\in B}v_b
\tag{4.2}
\]

for every coordinate normal basis \(A\) and every frame normal basis \(B\) of \(Z\) (index \(0\) standing for \(Y\), resp. \(D_0\)).

*Step 4: \(Y\) is constant on \(Z\).* Suppose first that some positive coordinate direction \(\partial_{X_i}\) is not tangent to \(Z\) at a general point, and let \(i\) be the largest such index. For \(l>i\), \(\partial_{X_l}=D_l\) is tangent at general points, so \(l\) belongs to no normal basis of either kind. Extending \(\partial_{X_i}\) by coordinate vectors gives a coordinate normal basis \(A\ni i\). If a frame normal basis \(B\) omitted \(i\), the largest positive index of \(A\triangle B\) would be \(i\in A\), and (1.3) would contradict (4.2). So every frame normal basis contains \(i\). Consequently, at a general point \(x\) of \(Z\), the vectors \(D_\beta(x)\), \(\beta\ne i\), do not span \(T_x\mathbb C^{m+1}\) modulo \(T_xZ\); otherwise \(k\) of them would form a frame normal basis without \(i\). Their span is the hyperplane

\[
H_x=\ker\bigl(dX_i-dY/Y\bigr)_x ,
\]

because \(D_0\) and the \(D_l\), \(l\ne i\), are annihilated by \(dX_i-dY/Y\) and are \(m\) independent vectors. A hyperplane fails to span modulo \(T_xZ\) exactly when it contains \(T_xZ\). Hence the form \(\omega=dX_i-dY/Y\) vanishes on \(T_xZ\) for \(x\) in a dense open subset \(Z^\circ\) of the smooth locus of \(Z\).

Suppose \(Y\) is not constant on \(Z\). Then \(dY|_{T_xZ}\ne0\) at some \(x\in Z^\circ\), since a function with zero differential on a smooth irreducible complex variety is constant. Let \(e=\dim Z\). Choose a line \(\ell\subseteq T_xZ\) with \(dY(\ell)\ne0\), and affine-linear functions \(\lambda_1,\dots,\lambda_{e-1}\) vanishing at \(x\) whose differentials, restricted to \(T_xZ\), cut out \(\ell\). These restrictions are part of a regular system of parameters of \(\mathcal O_{Z,x}\), so near \(x\) the set \(Z\cap\{\lambda=0\}\) is a smooth curve germ with tangent \(\ell\); let \(\Gamma\) be the irreducible component of \(Z\cap\{\lambda=0\}\) containing it, a curve through \(x\) on which \(Y\) is not constant, and which meets \(Z^\circ\) in a dense open subset. On \(\Gamma\), the tangent lines at the points of \(\Gamma\cap Z^\circ\) lie in \(\ker\omega\), so the rational functions \(y=Y|_\Gamma\) and \(\xi=X_i|_\Gamma\) satisfy \(d\xi=dy/y\) as rational differentials on \(\Gamma\). By the zeros-and-poles corollary, \(y\) has a zero or a pole at some point \(P\) of the smooth projective model \(\widetilde\Gamma\), say \(\operatorname{ord}_Py=n\ne0\). In \(\mathbb C((s))\), with \(s\) a uniformizer at \(P\), write \(y=s^nv\) with \(v\) a unit; then \(dy/y=(n/s+v'/v)\,ds\) has \(s^{-1}ds\)-coefficient \(n\), whereas \(d\xi=\xi'(s)\,ds\) has \(s^{-1}ds\)-coefficient \(0\), because the derivative of a Laurent series has no \(s^{-1}\) term. So \(n=0\), a contradiction.

If instead every \(\partial_{X_i}\) is tangent to \(Z\) at general points, then \(\dim Z\ge m\), so \(\dim Z=m\) and \(T_xZ\) is spanned by the \(\partial_{X_i}\); then \(dY\) vanishes on \(T_xZ\), and again \(Y\) is constant on \(Z\).

Since \(C^\circ\subseteq Z\) meets a centre, where \(Y=1\), we get \(Y=1\) on \(C\).

*Step 5: the fibre \(Y=1\).* Now \(C\subseteq\{Y=1\}\cong\mathbb C^m\), with coordinates \(X_i\), degree weights \(w_i\) and order weights \(v_i\) in \(u_i=X_i-c_{ji}\) (since \(\log Y=0\) on the fibre). On \(C\), \(t=0\), so \(h_P=\min_i\operatorname{ord}_P(X_i-c_{ji})/v_i\), and \(Y\) contributes nothing to \(\deg_WC\). As in Lemma 3.2, the ratio of conditions to unknowns for a polynomial \(G_N(X)\) of weighted degree at most \(N\) and order at least \((1+3\sigma)N\) at the \(K\) points \(c_j\) tends to \(K(1+3\sigma)^m\prod_iw_i/\prod_iv_i=K(1+3\sigma)^m\theta^m<1\), so such a nonzero \(G_N\) exists for large \(N\). Its partial derivatives \(\partial_X^\gamma G_N\) of cost \(\sum v_i\gamma_i\le\sigma N\) have weighted degree at most \(N\) and order at least \((1+2\sigma)N\) at the points; the argument of Step 1 shows that they vanish on \(C\).

If \(m=1\), the fibre is a line, \(C\) is that line, and the nonzero polynomial \(G_N\) cannot vanish on it. Let \(m\ge2\). Define \(U_r\subseteq\{Y=1\}\) as the common zero set of the \(\partial_X^\gamma G_N\) of cost at most \(r\delta\), and choose as in Step 2 a persistent component \(Z'\supseteq C\), with \(1\le\dim Z'\le m-1\). Theorem 3.1 of the multiplicity lesson, now for the frame \(\partial_{X_1},\dots,\partial_{X_m}\) with costs \(v_i\), gives (4.2) for the normal bases of \(Z'\) in the fibre. Here coordinate and frame normal bases are the same index sets. There is only one: if \(A\ne B\) were normal bases, then, naming them so that the largest index of \(A\triangle B\) lies in \(A\), (1.3) would contradict (4.2). Let \(A\) be the unique normal basis and \(i\in A\). The vectors \(\partial_{X_l}\), \(l\ne i\), do not span the normal space at general points (otherwise there would be a normal basis without \(i\)); they span \(\ker dX_i\), so \(T_xZ'\subseteq\ker dX_i\) at general points, and \(X_i\) is constant on \(Z'\). Since the \(c_{ji}\), \(0\le j<K\), are distinct, \(Z'\supseteq C\) contains at most one centre.

*Step 6: the final contradiction.* Let \(a_j\) be the centre on \(C\), and choose \(l\) with \(X_l\) not constant on \(C\). The nonzero rational function \(X_l-c_{jl}\) on \(\widetilde C\) has total pole order at most \(w_l\deg_WC\) (its pole order at \(P\) is at most \(w_lM_P\)), and at each branch \(P\) at \(a_j\) a zero of order at least \(v_lh_P=(w_l/\theta)h_P\). Equality of zeros and poles gives \((w_l/\theta)\sum_Ph_P\le w_l\deg_WC\), so

\[
\deg_WC\ge\theta^{-1}\sum_Ph_P>(1+\sigma)\sum_Ph_P
\]

by (1.2), contradicting the assumption. \(\square\)

The two halves of the proof use the two kinds of weights differently. Off the fibre \(Y=1\), the separation forces the persistent component to be tangent to \(dX_i=dY/Y\), which is impossible for a non-constant \(Y\) because \(dY/Y\) has nonzero residues and an exact differential has none. In the fibre, separation forces a coordinate \(X_i\) to be constant, and then a single centre with contact weights \(v_l=w_l/\theta\) beats the degree.

## 5. Exercises

**Exercise 5.1.** For \(m=1\), \(K=1\) and the centre \((1,0)\), compute \(\deg_WC\) and \(h_P\) for the line \(C=\{X_1=\lambda(Y-1)\}\), and check (4.1) when \(\lambda\ne1\) and when \(\lambda=1\).

**Exercise 5.2.** Show that the logarithmic curve itself is not algebraic: there is no curve \(C\) with \(u_1|_C=0\) at a branch through \((1,0)\) in the case \(m=1\). (Use Step 4.)

**Exercise 5.3.** Show that the separation condition (1.3) cannot be dropped: for \(m=K=1\), \(\theta=1/2\), \(w_0=1\), \(v_0=3/5\) (which satisfy (1.1)) and \(w_1=3/5\), find a line through the centre \((1,0)\) that violates (4.1).

**Exercise 5.4.** Explain why the auxiliary polynomial \(F_N\) is constructed for each large \(N\), and why the proof does not need any bound on \(N\) in terms of \(C\).

## 6. Solutions

**5.1.** On \(C\), \(X_1=\lambda(Y-1)\), so \(t\) is a coordinate on the branch at \((1,0)\), with \(\operatorname{ord}t=1\), and \(u_1=\lambda t-\log(1+t)=(\lambda-1)t+t^2/2-\dots\) has order \(1\) if \(\lambda\ne1\) and \(2\) if \(\lambda=1\). So \(h_P=\min(1/v_0,1/v_1)\) or \(\min(1/v_0,2/v_1)\). At the point at infinity of \(\widetilde C\cong\mathbf P^1\), \(Y\) and \(X_1\) have simple poles (if \(\lambda\ne0\)), so \(\deg_WC=\max(1/w_0,1/w_1)\). Inequality (4.1) reads \(\max(1/w_0,1/w_1)\ge(1+\sigma)h_P\). For separated weights \(w_1\) is very large, so \(h_P\le2/v_1=2\theta/w_1\) is tiny and (4.1) holds with room to spare.

**5.2.** If \(u_1\) vanished identically on a branch of an algebraic curve through \((1,0)\), then \(dX_1=dY/Y\) on that curve, and the residue argument of Step 4 shows that \(Y\) is constant, so \(Y=1\) and then \(X_1=\log Y=0\): the "curve" is a point.

**5.3.** Here \(K\theta=1/2<1\) and \(K(w_0/v_0)\theta=5/6<1\). Take the line \(X_1=Y-1\), that is \(\lambda=1\) in Exercise 5.1. With \(v_1=w_1/\theta=6/5\), \(h_P=\min(5/3,\,2\cdot5/6)=5/3\) and \(\deg_WC=\max(1,5/3)=5/3\), so (4.1) would require \(5/3\ge(1+\sigma)\,5/3\), false for every \(\sigma>0\). Separation, with \(A=\{1\}\) and \(B=\{0\}\), demands \(w_1>C_*v_0\), far from \(w_1=v_0\).

**5.4.** The contradiction in Step 1 comes from comparing \((1+2\sigma)N\sum h_P\) with \(N\deg_WC\); both scale with \(N\), so any \(N\) for which \(F_N\) exists works. The multiplicity estimate is also uniform in \(N\).

## References

- [OpenAI-Pi] OpenAI, The irrationality exponent of π is 2, preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026
- [Philippon] P. Philippon, Lemmes de zéros dans les groupes algébriques commutatifs, Bulletin de la Société Mathématique de France 114 (1986). https://www.numdam.org/articles/10.24033/bsmf.2060/
- [Farhi] B. Farhi, Un lemme de Roth sur les groupes algébriques commutatifs, arXiv:math/0603257 (2006). https://arxiv.org/abs/math/0603257
