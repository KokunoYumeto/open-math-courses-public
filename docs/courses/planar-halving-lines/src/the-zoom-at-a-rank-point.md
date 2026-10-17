# The zoom at a rank point

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Rank coordinates are compact labels, but a small disk in the rank square could correspond to a hugely distorted region of the plane. This lesson recovers Euclidean control at the points of the good set \(E\) of [Independent gradients and tangent directions](independent-gradients-and-tangent-directions.md) [OpenAI-HL, Section 5]. Zooming into the rank chart at such a point, the three sweep directions with single tangent directions become three families of lines whose images have limiting directions, and the theorem of [Three transverse foliations](three-transverse-foliations.md) shows that the zoomed maps converge to a nonsingular linear map. A comparison with one normalization common to all points then gives the output used in [A spatial measure](a-spatial-measure.md): at every point of \(E\), the inverse rank map distorts circles of small radius by a bounded factor, with the radius fixed before the configuration.

We keep the notation of the previous lessons: the windows \(A,B\), the chart \((r_A,r_B)\), the set \(E\) and the times \(t_1<t_2<t_3\) and \(\tau_1<\tau_2<\tau_3\) of Proposition 6.1 there, and the direction \(\varsigma(t)\) of lines of direction \(t\).

## 1. A linear normalization

**Lemma 1.1.** Let \(d_1,d_2,d_3\) be pairwise non-parallel vectors of the plane and \(e_1,e_2,e_3\) also. There is an invertible linear map \(B\) with \(Bd_i\in\mathbb Re_i\) for \(i=1,2,3\).

*Proof.* Write \(d_3=\alpha d_1+\beta d_2\) and \(e_3=\alpha'e_1+\beta'e_2\); all four coefficients are nonzero, since no two of the vectors are parallel. Let \(B\) map \(\alpha d_1\) to \(\alpha'e_1\) and \(\beta d_2\) to \(\beta'e_2\). Then \(Bd_3=e_3\). \(\square\)

In each late configuration the slopes \(\varsigma(t_1),\varsigma(t_2),\varsigma(t_3)\) are distinct. Fix the target lines \(\mathbb Rv_1,\mathbb Rv_2,\mathbb Rv_3\), with \(v_1=(1,0)\), \(v_2=(0,1)\), \(v_3=(1,1)\), and let \(T_n\) be a linear map, given by Lemma 1.1, sending the lines of slopes \(\varsigma(t_i)\) to them. The *common normalization* of configuration \(n\) is
\[
L_n=T_n\circ(r_A,r_B)^{-1}:(0,1)^2\longrightarrow\mathbb R^2 ,
\]
a homeomorphism onto the plane. It does not depend on any label. For a closed disk \(\bar B(p,h)\subseteq(0,1)^2\) put
\[
\begin{gathered}
U_n(p,h)=\max_{|u-p|=h}|L_n(u)-L_n(p)|,\\
V_n(p,h)=\min_{|u-p|=h}|L_n(u)-L_n(p)|.
\end{gathered}
\]

## 2. The zoom converges to a linear map

Fix \(z\in E\) and \(p=p(z)\), with the times \(\tau_i\) and unit directions \(d_i\), \(D_p(\tau_i)=\{d_i\}\). By Lemma 1.1 fix an invertible \(B\) with \(Bd_i\in\mathbb Rv_i\). Let \((h_j,n_j)\) be a fast diagonal (Section 4 of [Independent gradients and tangent directions](independent-gradients-and-tangent-directions.md)).

In configuration \(n_j\), let \(X_j\) be the point with \((r_A,r_B)(X_j)=p\), and let \(L_j^\tau\) be a linear map sending the lines of slopes \(\varsigma(\tau_i)\) to \(\mathbb Rv_i\). For a scale \(c>0\) put \(Y(x)=X_j+c\,(L_j^\tau)^{-1}x\) and consider
\[
F_j(x)=\frac1{h_j}B\bigl((r_A,r_B)(Y(x))-p\bigr).
\]
On the ray \(\{cv_1\}\) the norm \(|F_j(v_1)|\), as a function of \(c\), is continuous, zero at \(c=0\), and larger than \(1\) for large \(c\): as \(c\to\infty\) the point leaves every compact set of the plane, so its rank image approaches the boundary of the square, at distance from \(p\) larger than \(h_j\|B^{-1}\|\) once \(h_j\) is small. Choose \(c=c_j\) with \(|F_j(v_1)|=1\).

**Proposition 2.1.** Along a subsequence, \(F_j\to\sigma\,\mathrm{id}\) and \(F_j^{-1}\to\sigma\,\mathrm{id}\) uniformly on compact sets, for some \(\sigma\in\{-1,1\}\).

*Proof.* We check the hypotheses of Theorem 2.1 of [Three transverse foliations](three-transverse-foliations.md). The map \(F_j\) is a homeomorphism of the plane onto \(\Omega_j=h_j^{-1}B((0,1)^2-p)\), and these sets eventually contain every compact set, since \(p\) is interior and \(h_j\to0\). A line of type \(i\) in the domain of \(F_j\) corresponds to a line of direction \(\tau_i\) in configuration \(n_j\). Both coordinates of \(B^{-1}F_j\), which are \(r_A\) and \(r_B\) up to translation and scaling, are monotone along lines of direction \(\tau_i\), with a sign that is the same for all such lines, by Section 5 of [Independent gradients and tangent directions](independent-gradients-and-tangent-directions.md); the orientation induced by \(v_i\) may differ from the forward orientation, but along a subsequence it is fixed for each \(i\). So the first hypothesis holds with \(P=B^{-1}\).

Let \(x_j,y_j\) lie on a line of type \(i\) with \(F_j(x_j)\to a\) and \(F_j(y_j)\to b\ne a\). The zoom coordinates of the corresponding points are \(B^{-1}F_j(x_j)\to B^{-1}a\) and \(B^{-1}F_j(y_j)\to B^{-1}b\), and they lie on one line of direction \(\tau_i\). By Lemma 5.1 there, the unit vector of \(\pm B^{-1}(b-a)\), the sign given by the forward order, lies in \(D_p(\tau_i)=\{d_i\}\). So \(b-a\in\mathbb RBd_i=\mathbb Rv_i\). This holds along every subsequence, since subsequences of fast diagonals are fast diagonals. The third hypothesis holds by the choice of \(X_j\) and \(c_j\). \(\square\)

## 3. Comparison with the common normalization

Let \(A_j=T_{n_j}\circ(L_j^\tau)^{-1}\), the linear map from the \(\tau\)-normalized plane to the common one. It sends the lines \(\Xi_{i,j}=L_j^\tau(\text{lines of slope }\varsigma(t_i))\) to \(\mathbb Rv_i\).

**Lemma 3.1.** Along a further subsequence, \(\Xi_{i,j}\) converges to a line \(\Xi_i\) with \(B^{-1}\Xi_i\) spanned by a vector of \(D_p(t_i)\). The three lines \(\Xi_1,\Xi_2,\Xi_3\) are distinct, and the angle between any two of them is at least a constant \(\theta_p>0\) depending only on \(p\) and \(B\).

*Proof.* Pass to a subsequence along which the lines \(\Xi_{i,j}\) converge, and let \(u_j\) be a unit vector on \(\Xi_{i,j}\), oriented forward, with \(u_j\to u\). The segment from \(0\) to \(u_j\) in the \(\tau\)-normalized plane corresponds to a segment on a line of direction \(t_i\) in configuration \(n_j\). By Proposition 2.1 its endpoints have images \(F_j(0)=0\) and \(F_j(u_j)\to\sigma u\ne0\), uniformly. Their zoom coordinates are \(0\) and \(B^{-1}F_j(u_j)\to\sigma B^{-1}u\), so by Lemma 5.1 of [Independent gradients and tangent directions](independent-gradients-and-tangent-directions.md) the unit vector of \(\sigma B^{-1}u\) lies in \(D_p(t_i)\). The arcs \(D_p(t_1),D_p(t_2),D_p(t_3)\) are pairwise disjoint compact subsets of one closed quadrant, which contains no two opposite unit vectors; so the lines they span form three pairwise disjoint compact sets of lines, at mutual angle at least some \(\theta'>0\). Applying \(B\) changes angles by a bounded factor. \(\square\)

**Lemma 3.2.** The matrices \(A_j/\|A_j\|\) have, along a subsequence, a limit \(A\), and \(A\) is invertible, with condition number bounded by a constant depending only on \(\theta_p\).

*Proof.* A subsequence converges, to \(A\) with \(\|A\|=1\). If \(A\) were singular, it would have rank one, with a kernel line and an image line. At most one of the three distinct lines \(\Xi_i\) is the kernel; for the other two, say \(\Xi_a\) and \(\Xi_b\), \(A\) maps them onto the image line. But \(A_j\Xi_{a,j}=\mathbb Rv_a\) and \(A_j\Xi_{b,j}=\mathbb Rv_b\), and passing to the limit gives \(A\Xi_a=\mathbb Rv_a\) and \(A\Xi_b=\mathbb Rv_b\), two different lines. So \(A\) is invertible. The same argument applies to every sequence of matrices of norm one mapping three lines with mutual angles at least \(\theta_p\) to the three fixed lines, so by compactness their condition numbers are bounded. \(\square\)

**Proposition 3.3.** Let \(K_p\) be the bound of Lemma 3.2 times the condition number of \(B\). Along every fast diagonal there is a subsequence along which, for some scalars \(\kappa_j>0\), the maps
\[
w\longmapsto\kappa_j\bigl(L_{n_j}(p+h_jw)-L_{n_j}(p)\bigr)
\]
converge uniformly on compact sets to an invertible linear map with condition number at most \(K_p\).

*Proof.* Write \(X=X_j+c_j(L_j^\tau)^{-1}x\). Then \(L_{n_j}((r_A,r_B)(X))-L_{n_j}(p)\) equals \(T_{n_j}(X-X_j)=c_jA_jx\), and \((r_A,r_B)(X)=p+h_jB^{-1}F_j(x)\). So for \(w\) in a compact set, with \(x=F_j^{-1}(Bw)\),
\[
\begin{aligned}
&\frac1{c_j\|A_j\|}\bigl(L_{n_j}(p+h_jw)-L_{n_j}(p)\bigr)\\
&\quad=\frac{A_j}{\|A_j\|}F_j^{-1}(Bw)\longrightarrow\sigma ABw ,
\end{aligned}
\]
uniformly, by Proposition 2.1 and Lemma 3.2. \(\square\)

## 4. Radial comparison

**Proposition 4.1** (radial comparison; OpenAI). For every \(z\in E\), with \(p=p(z)\), there is \(C_p<\infty\) with the following property. For every integer \(T\ge2\) there is \(h_{p,T}>0\) such that for every fixed \(h\in(0,h_{p,T})\), in all sufficiently late configurations \(n\),
\[
\begin{gathered}
V_n(p,h/T)\ge\frac{U_n(p,h)}{C_pT},\\
U_n(p,h/T)\le\frac{C_pV_n(p,h)}T .
\end{gathered}
\]

*Proof.* Take any \(C_p>K_p\). Suppose the statement fails for some \(T\). Then there are \(h_k\to0\) and, for each \(k\), configurations as late as we like in which one of the inequalities fails for \(h=h_k\). Choose such a configuration \(n_k\) so late that \((h_k,n_k)\) is a fast diagonal. By Proposition 3.3, along a subsequence and after positive rescaling, \(w\mapsto L_{n_k}(p+h_kw)-L_{n_k}(p)\) converges uniformly on the closed unit disk to an invertible linear map \(\Lambda\) of condition number \(\kappa\le K_p<C_p\). Rescaling does not change the two ratios. On the circles \(|w|=1/T\) and \(|w|=1\),
the ratio \(V_{n_k}(p,h_k/T)/U_{n_k}(p,h_k)\) tends to
\[
\frac{\min_{|w|=1/T}|\Lambda w|}{\max_{|w|=1}|\Lambda w|}=\frac1{T\kappa},
\]
and \(U_{n_k}(p,h_k/T)/V_{n_k}(p,h_k)\) tends to \(\kappa/T\). Since \(1/(T\kappa)>1/(C_pT)\) and \(\kappa/T<C_p/T\), both inequalities hold for large \(k\), contradicting the choice of \(n_k\). \(\square\)

The order of quantifiers is essential: the radius \(h\) is fixed first, and only then is the configuration taken late. No rate uniform in \(p\) or in the configuration is claimed.

## 5. Exercises

**5.1** (easy). Find a linear map \(B\) with \(B(1,1)\in\mathbb R(1,0)\), \(B(1,-1)\in\mathbb R(0,1)\) and \(B(1,0)\in\mathbb R(1,1)\).

**5.2** (medium). Show that for an invertible linear map \(\Lambda\) of condition number \(\kappa\), \(\min_{|w|=r}|\Lambda w|/\max_{|w|=R}|\Lambda w|=r/(R\kappa)\).

**5.3** (medium). Why can Proposition 4.1 not be proved with a single fast diagonal fixed in advance?

## 6. Solutions

**5.1.** \((1,0)=\frac12(1,1)+\frac12(1,-1)\). With the proof of Lemma 1.1 (\(\alpha=\beta=\frac12\), \(\alpha'=\beta'=1\)), \(B\) maps \(\frac12(1,1)\) to \((1,0)\) and \(\frac12(1,-1)\) to \((0,1)\): \(B(x,y)=(x+y,\,x-y)\), and \(B(1,0)=(1,1)\).

**5.2.** \(\min_{|w|=r}|\Lambda w|=r\,s_{\min}\) and \(\max_{|w|=R}|\Lambda w|=R\,s_{\max}\), with the singular values \(s_{\min},s_{\max}\) and \(\kappa=s_{\max}/s_{\min}\).

**5.3.** A fixed diagonal says nothing about radii \(h\) not in the sequence \((h_j)\), nor about configurations other than \(n_j\). The proposition concerns every small fixed radius and all late configurations; the proof argues by contradiction and builds a fast diagonal out of the failing pairs.

## References

- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
