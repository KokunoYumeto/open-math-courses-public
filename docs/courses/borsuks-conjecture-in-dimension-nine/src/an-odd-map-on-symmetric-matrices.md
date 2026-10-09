# An odd map on symmetric matrices

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An admissible map \(f:\mathbb P(V)\to\Delta^{m-1}\) of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md) is defined on lines. This lesson extends it to all symmetric operators: first to positive semidefinite operators by averaging \(f\) over the directions of the operator's range (Section 2), then to all symmetric operators by subtracting the values on the positive and negative parts (Section 3). Because the ranges of the two parts are orthogonal, admissibility prevents any cancellation, and the result is an odd map between two spheres: the operators of trace norm one, of dimension \(N_k-1\), and the vectors of \(\ell^1\)-norm one in \(\mathbb R^m\), of dimension \(m-1\) (Section 4). The degree theory of [Double covers and odd maps](double-covers-and-odd-maps.md) applies to this map in [Supports at equality](supports-at-equality.md). The preprint [OpenAI-B9] averages over the unit sphere; we average against the Gaussian measure, which removes a dimension factor from the restriction formula.

Throughout, \(V\) is a Euclidean space of dimension \(k\ge2\), \(f:\mathbb P(V)\to\Delta^{m-1}\) is admissible with supports \(S(x)\), and \(\operatorname{Sym}(V)\) carries the Frobenius norm. We write \(Q\succeq0\) for positive semidefinite and \(Q\succ0\) for positive definite operators. From [Local tools for bundles and transport](course:DG-FND/local-tools-for-bundles-and-transport) we use the smooth inverse function theorem (Theorem 1.2) and the smoothness of inversion of invertible operators (Lemma 0.4); from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), dominated convergence and differentiation under the integral sign (Fremlin, Volume 1, 123C and 123D), Fubini's theorem (Volume 2, 251N and 252B) and the invariance of Lebesgue measure under orthogonal maps (Volume 2, 263A).

## 1. Square roots and spectral parts

**Lemma 1.1.** (a) (Spectral theorem.) Every \(A\in\operatorname{Sym}(V)\) has an orthonormal basis of eigenvectors.

(b) Every \(Q\succeq0\) has a unique \(S\succeq0\) with \(S^2=Q\), written \(Q^{1/2}\). It has the same kernel and range as \(Q\). If \(\operatorname{ran}Q\subseteq W\) for a subspace \(W\), then \(Q^{1/2}\) vanishes on \(W^\perp\), maps \(W\) into itself, and its restriction to \(W\) is \((Q|_W)^{1/2}\).

(c) \(Q\mapsto Q^{1/2}\) is continuous on \(\{Q\succeq0\}\) and smooth on the open set \(\{Q\succ0\}\).

*Proof.* (a) The continuous function \(v\mapsto\langle Av,v\rangle\) attains its maximum on the compact unit sphere at some \(u\). For \(w\perp u\), the function \(t\mapsto\langle A(u+tw),u+tw\rangle/(1+t^2|w|^2)\) has a maximum at \(t=0\), and its derivative there is \(2\langle Au,w\rangle\); so \(Au\perp u^\perp\), and \(Au=\lambda u\). Since \(A\) is symmetric it maps \(u^\perp\) into itself, and induction on \(k\) finishes the proof.

(b) Write \(Q=\sum_j\lambda_ju_ju_j^{\mathsf T}\) with an orthonormal eigenbasis and \(\lambda_j\ge0\); then \(S=\sum_j\sqrt{\lambda_j}u_ju_j^{\mathsf T}\) works and has the same kernel and range. If \(S\succeq0\) and \(S^2=Q\), then \(S\) commutes with \(Q\), so it maps each eigenspace \(E_\lambda\) of \(Q\) into itself, and on \(E_\lambda\) it is positive semidefinite with square \(\lambda\); by (a) applied on \(E_\lambda\), its eigenvalues there are all \(\sqrt\lambda\), so \(S=\sqrt\lambda\) on \(E_\lambda\). If \(\operatorname{ran}Q\subseteq W\), then \(W^\perp\subseteq\ker Q=\ker Q^{1/2}\), and \(Q^{1/2}\) maps into \(\operatorname{ran}Q\subseteq W\); its restriction to \(W\) is positive semidefinite with square \(Q|_W\), hence equals \((Q|_W)^{1/2}\) by uniqueness.

(c) By (b), squaring is a continuous bijection of \(\{S\succeq0\}\). For \(R>0\) the set \(\{S\succeq0:\|S\|_F\le R\}\) is compact, and squaring maps it onto \(\{Q\succeq0:\operatorname{tr}Q\le R^2\}\) because \(\|S\|_F^2=\operatorname{tr}S^2\). A continuous bijection from a compact space onto a Hausdorff space is a homeomorphism, so the square root is continuous on each of these sets, hence everywhere. For smoothness, the map \(S\mapsto S^2\) on \(\operatorname{Sym}(V)\) has derivative \(X\mapsto SX+XS\). If \(S\succ0\) has eigenvalues \(s_i>0\) in an orthonormal eigenbasis, then \((SX+XS)_{ij}=(s_i+s_j)X_{ij}\), so the derivative is injective, hence invertible. By the smooth inverse function theorem, squaring maps a neighbourhood of \(S\) inside \(\{S\succ0\}\) diffeomorphically onto a neighbourhood of \(S^2\); the inverse sends \(Q\) to a positive definite square root of \(Q\), which is \(Q^{1/2}\) by uniqueness. \(\square\)

For \(A\in\operatorname{Sym}(V)\) put \(|A|=(A^2)^{1/2}\) and \(A_\pm=\frac12(|A|\pm A)\). In an orthonormal eigenbasis with eigenvalues \(\alpha_j\), \(|A|=\sum_j|\alpha_j|u_ju_j^{\mathsf T}\) and \(A_\pm=\sum_j\max(\pm\alpha_j,0)u_ju_j^{\mathsf T}\). So \(A_\pm\succeq0\), \(A=A_+-A_-\), the ranges of \(A_+\) and \(A_-\) are the *positive* and *negative spectral subspaces* (spanned by eigenvectors with positive, respectively negative, eigenvalue), they are orthogonal, and \(\ker A\) is orthogonal to both. Also \((-A)_\pm=A_\mp\) and \((tA)_\pm=tA_\pm\) for \(t\ge0\). The *trace norm* \(\operatorname{tr}|A|=\sum_j|\alpha_j|\) is positive for \(A\ne0\) and satisfies \(\operatorname{tr}|tA|=|t|\operatorname{tr}|A|\). By Lemma 1.1(c), \(A\mapsto|A|\), \(A_\pm\) and \(\operatorname{tr}|A|\) are continuous.

**Lemma 1.2** (Nonsingular operators). On the open set of nonsingular \(A\in\operatorname{Sym}(V)\):

(a) \(\operatorname{tr}|A|\) and the orthogonal projections \(\Pi_\pm(A)=\frac12\bigl(I\pm A|A|^{-1}\bigr)\) onto the positive and negative spectral subspaces are smooth, and the dimensions \(r_\pm\) of these subspaces are locally constant;

(b) near each nonsingular \(A_0\) there are smooth maps \(A\mapsto T_\pm(A)\), with \(T_\pm(A):\mathbb R^{r_\pm}\to V\) isometric with range \(\operatorname{ran}\Pi_\pm(A)\), and then \(A_\pm=T_\pm C_\pm T_\pm^{\mathsf T}\) with \(C_\pm=\pm T_\pm^{\mathsf T}AT_\pm\succ0\) depending smoothly on \(A\).

*Proof.* (a) \(A^2\succ0\), so \(|A|\) is smooth by Lemma 1.1(c) and \(|A|^{-1}\) by the smoothness of inversion; \(A|A|^{-1}=\sum_j\operatorname{sign}(\alpha_j)u_ju_j^{\mathsf T}\) gives the formula for \(\Pi_\pm\). The dimension of the range of a projection is its trace, a continuous integer-valued function. (b) Choose a basis \(b_1,\dots,b_{r_+}\) of \(\operatorname{ran}\Pi_+(A_0)\). The vectors \(\Pi_+(A)b_l\) depend smoothly on \(A\), lie in \(\operatorname{ran}\Pi_+(A)\), and are linearly independent near \(A_0\); since \(r_+\) is locally constant they span \(\operatorname{ran}\Pi_+(A)\), and the Gram–Schmidt process, smooth on independent tuples, gives \(T_+(A)\). Then \(\Pi_+=T_+T_+^{\mathsf T}\) commutes with \(A\), and \(A_+=A\Pi_+=T_+(T_+^{\mathsf T}AT_+)T_+^{\mathsf T}\), where \(T_+^{\mathsf T}AT_+\) represents \(A\) on its positive spectral subspace and is positive definite. The negative part is the same with \(-A\). \(\square\)

## 2. The positive extension

Let \(\gamma_V\) be the standard Gaussian measure on \(V\): in an orthonormal basis, the measure with density \((2\pi)^{-k/2}e^{-|v|^2/2}\). It does not depend on the orthonormal basis, because orthogonal maps preserve Lebesgue measure and the density depends only on \(|v|\). It gives positive mass to nonempty open sets, \(\int\langle a,v\rangle\langle b,v\rangle\,d\gamma_V(v)=\langle a,b\rangle\), and for an orthogonal decomposition \(V=W\oplus W^\perp\) it is the product \(\gamma_W\otimes\gamma_{W^\perp}\), so \(\int\phi(\pi_Wv)\,d\gamma_V(v)=\int_W\phi\,d\gamma_W\) for every integrable \(\phi\) on \(W\), \(\pi_W\) being the orthogonal projection (Fubini).

Define \(H:V\to\mathbb R^m\) by \(H(v)=|v|^2f([v])\) for \(v\neq0\) and \(H(0)=0\). It is continuous, because \(\|H(v)\|_1=|v|^2\); smooth on \(V\setminus\{0\}\), because \(v\mapsto[v]\) is smooth there; and \(H(tv)=t^2H(v)\) for real \(t\). For \(Q\succeq0\) put
\[
E_V(Q)=\int_VH(Q^{1/2}v)\,d\gamma_V(v)\in\mathbb R^m . \tag{2.1}
\]

**Lemma 2.1** (Positive extension). The map \(E_V\) is continuous on \(\{Q\succeq0\}\), and for \(Q\succeq0\):

(a) \(E_V(tQ)=tE_V(Q)\) for \(t\ge0\), \(E_V(Q)_i\ge0\), and \(\sum_iE_V(Q)_i=\operatorname{tr}Q\);

(b) \(\{i:E_V(Q)_i>0\}=\bigcup_{x\in\mathbb P(\operatorname{ran}Q)}S(x)\), the empty set if \(Q=0\);

(c) \(E_V(P_x)=f(x)\) for every line \(x\);

(d) if \(\operatorname{ran}Q\subseteq W\) for a subspace \(W\ne0\), then \(E_V(Q)=E_W(Q|_W)\), where \(E_W\) is built from \(f|_{\mathbb P(W)}\) and \(\gamma_W\);

(e) let \(\Lambda\) be an open subset of a Euclidean space, and let \(T_\lambda:\mathbb R^r\to V\) (isometric) and \(C_\lambda\succ0\) (an \(r\times r\) matrix) depend smoothly on \(\lambda\in\Lambda\), \(r\ge1\). Then \(\lambda\mapsto E_V(T_\lambda C_\lambda T_\lambda^{\mathsf T})\) is smooth.

*Proof.* The integrand of (2.1) is continuous in \((Q,v)\) and bounded in \(\ell^1\)-norm by \(\|Q^{1/2}v\|^2\le\operatorname{tr}(Q)|v|^2\), which is integrable uniformly for \(Q\) in bounded sets; dominated convergence (Fremlin 123C) gives continuity.

(a) \((tQ)^{1/2}=\sqrt tQ^{1/2}\) and \(H\) is homogeneous of degree two. Nonnegativity is clear, and \(\sum_iH(w)_i=|w|^2\) gives \(\sum_iE_V(Q)_i=\int\langle Qv,v\rangle\,d\gamma_V=\operatorname{tr}Q\).

(b) Every nonzero \(Q^{1/2}v\) lies in \(\operatorname{ran}Q^{1/2}=\operatorname{ran}Q\), so a positive coordinate \(E_V(Q)_i\) requires \(f_i([Q^{1/2}v])>0\) for some such \(v\). Conversely, if \(f_i(x)>0\) for a line \(x\subseteq\operatorname{ran}Q\), then \(x=[Q^{1/2}v_0]\) for some \(v_0\), because \(Q^{1/2}\) maps \(V\) onto \(\operatorname{ran}Q\). By continuity \(H(Q^{1/2}v)_i>0\) on an open neighbourhood of \(v_0\), which has positive Gaussian measure.

(c) \(P_x^{1/2}=P_x\), and \(H(P_xv)=\langle u,v\rangle^2f(x)\) for a unit \(u\in x\), whose integral is \(f(x)\).

(d) By Lemma 1.1(b), \(Q^{1/2}=(Q|_W)^{1/2}\circ\pi_W\), and the integral of a function of \(\pi_Wv\) against \(\gamma_V\) is its integral against \(\gamma_W\).

(e) By (d) and the isometry \(T_\lambda\) onto its range,
\[
E_V(T_\lambda C_\lambda T_\lambda^{\mathsf T})=\int_{\mathbb R^r}H(T_\lambda C_\lambda^{1/2}w)\,d\gamma_r(w)=\int_{\mathbb R^r}\langle C_\lambda w,w\rangle\,\Phi(\lambda,w)\,d\gamma_r(w),
\]
where \(\Phi(\lambda,w)=f([T_\lambda C_\lambda^{1/2}w])\) for \(w\ne0\). The map \((\lambda,w)\mapsto T_\lambda C_\lambda^{1/2}w\) is smooth on \(\Lambda\times(\mathbb R^r\setminus0)\) with nonzero values (Lemma 1.1(c)), so \(\Phi\) is smooth there, and \(\Phi(\lambda,w)=\Phi(\lambda,w/|w|)\). On \(K\times(\mathbb R^r\setminus0)\), for \(K\subseteq\Lambda\) compact, every \(\lambda\)-derivative of \(\Phi\) is therefore bounded (by its maximum on \(K\times S^{r-1}\)), and every \(\lambda\)-derivative of the integrand is bounded by \(c(1+|w|^2)\). Differentiation under the integral sign (Fremlin 123D), applied repeatedly in each coordinate of \(\lambda\), together with dominated convergence for the continuity of the derivatives, shows that the integral is smooth. \(\square\)

## 3. The signed extension

For \(A\in\operatorname{Sym}(V)\) define
\[
F_V(A)=E_V(A_+)-E_V(A_-)\in\mathbb R^m . \tag{3.1}
\]

**Proposition 3.1** (The odd extension). \(F_V\) is continuous and odd, \(F_V(tA)=tF_V(A)\) for \(t\ge0\), and

(a) \(\{i:F_V(A)_i>0\}=\bigcup_{x\subseteq\operatorname{ran}A_+}S(x)\) and \(\{i:F_V(A)_i<0\}=\bigcup_{x\subseteq\operatorname{ran}A_-}S(x)\), unions over lines;

(b) \(\|F_V(A)\|_1=\operatorname{tr}|A|\) and \(\sum_iF_V(A)_i=\operatorname{tr}A\);

(c) if every coordinate of \(F_V(A)\) is nonzero, then \(A\) is nonsingular; if every coordinate is negative, then \(A\) is negative definite (and positive definite if every coordinate is positive);

(d) \(F_V\) is smooth on the open set of nonsingular operators;

(e) if \(A\) vanishes on a line \(x\) and maps \(x^\perp\) into itself, then \(F_V(A)=F_{x^\perp}(A|_{x^\perp})\), where \(F_{x^\perp}\) is built from \(f|_{\mathbb P(x^\perp)}\).

*Proof.* Continuity, homogeneity and oddness follow from Lemma 2.1 and the properties of \(A_\pm\). (a), (b): every line of \(\operatorname{ran}A_+\) is orthogonal to every line of \(\operatorname{ran}A_-\), so by admissibility and Lemma 2.1(b) the vectors \(E_V(A_+)\) and \(E_V(A_-)\) have disjoint sets of positive coordinates. There is no cancellation in (3.1), which gives (a), and summing absolute values or values gives \(\operatorname{tr}A_++\operatorname{tr}A_-=\operatorname{tr}|A|\) and \(\operatorname{tr}A_+-\operatorname{tr}A_-=\operatorname{tr}A\) by Lemma 2.1(a).

(c) If \(\ker A\) contains a line \(x\), pick \(i\in S(x)\). The line \(x\) is orthogonal to both spectral subspaces, so \(i\) belongs to no support of a line in them, and \(F_V(A)_i=0\) by (a). If all coordinates are negative, then \(E_V(A_+)=0\), so \(\operatorname{tr}A_+=0\) and \(A_+=0\); with nonsingularity, \(A\) is negative definite. Oddness gives the positive case.

(d) Near a nonsingular \(A_0\), Lemma 1.2(b) writes \(A_\pm=T_\pm C_\pm T_\pm^{\mathsf T}\) with smooth data, and Lemma 2.1(e) (or \(E_V(0)=0\) if \(r_\pm=0\)) shows that \(E_V(A_\pm)\) is smooth.

(e) Then \(A_\pm\) vanish on \(x\) and have range in \(x^\perp\), with \((A_\pm)|_{x^\perp}=(A|_{x^\perp})_\pm\); apply Lemma 2.1(d) with \(W=x^\perp\). \(\square\)

## 4. Two spheres

Put
\[
\Sigma(V)=\{A\in\operatorname{Sym}(V):\operatorname{tr}|A|=1\},\qquad\Sigma_m=\{y\in\mathbb R^m:\|y\|_1=1\}.
\]
By Proposition 3.1(b), \(F_V\) maps \(\Sigma(V)\) into \(\Sigma_m\), and it commutes with \(A\mapsto-A\) and \(y\mapsto-y\). Radial projection \(\rho_V(A)=A/\|A\|_F\) is a homeomorphism from \(\Sigma(V)\) onto the unit sphere of \(\operatorname{Sym}(V)\), a copy of \(S^{N_k-1}\), with inverse \(B\mapsto B/\operatorname{tr}|B|\); likewise \(\rho_m(y)=y/|y|\) identifies \(\Sigma_m\) with \(S^{m-1}\). Both commute with negation. So
\[
\widehat F=\rho_m\circ F_V\circ\rho_V^{-1}:S^{N_k-1}\longrightarrow S^{m-1}
\]
is an odd continuous map.

**Lemma 4.1** (Smooth points). (a) Near a nonsingular operator, \(\Sigma(V)\) is a smooth hypersurface of \(\operatorname{Sym}(V)\), and \(\rho_V\) is a diffeomorphism from a neighbourhood of it in \(\Sigma(V)\) onto an open subset of the unit sphere.

(b) Near a vector \(y\) with all coordinates nonzero, \(\Sigma_m\) is an open subset of the affine hyperplane \(\{\sum_i\operatorname{sign}(y_i)y'_i=1\}\), and \(\rho_m\) is a diffeomorphism from a neighbourhood of \(y\) in \(\Sigma_m\) onto an open subset of \(S^{m-1}\).

(c) Consequently, if \(A\in\Sigma(V)\) is nonsingular, then \(\widehat F\) is smooth near \(\rho_V(A)\), and if moreover \(F_V(A)\) has all coordinates nonzero, the derivative of \(\widehat F\) at \(\rho_V(A)\) is invertible exactly when the derivative of \(F_V:\Sigma(V)\to\Sigma_m\) at \(A\), between these hypersurfaces, is invertible.

*Proof.* (a) \(\operatorname{tr}|\cdot|\) is smooth on nonsingular operators (Lemma 1.2(a)), and its derivative at \(A\) in the direction \(A\) is \(\frac d{dt}\operatorname{tr}|tA|\big|_{t=1}=\operatorname{tr}|A|\ne0\); so \(1\) is a regular value near \(A\), and Proposition 3.1 of [Regular values and degree modulo two](regular-values-and-degree-modulo-two.md) gives the hypersurface. The maps \(\rho_V\) and \(B\mapsto B/\operatorname{tr}|B|\) are smooth there and inverse to each other. (b) In the open orthant of \(y\), \(\|y'\|_1=\sum_i\operatorname{sign}(y_i)y'_i\) is linear. (c) Combine (a), (b) and Proposition 3.1(d). \(\square\)

## 5. Exercises

**5.1.** Let \(f\) be any smooth map \(\mathbb P(V)\to\Delta^{m-1}\), not necessarily admissible. Which parts of Lemma 2.1 and Proposition 3.1 remain true? Show by an example with \(k=2\) that \(\|F_V(A)\|_1<\operatorname{tr}|A|\) can happen.

**5.2.** For \(k=2\), identify \(\mathbb P(\mathbb R^2)\) with the angles \(\theta\in\mathbb R/\pi\mathbb Z\) of lines. Construct an admissible map \(\mathbb P(\mathbb R^2)\to\Delta^2\) by covering \(\mathbb R/\pi\mathbb Z\) with three open arcs of length less than \(\pi/2\). Show that \(F_V(P_x)\) is a vertex of the simplex for every line \(x\) that lies in only one of the arcs.

**5.3.** Show that \(t\mapsto t^{1/2}\) on \([0,\infty)\) is not differentiable at \(0\), so Lemma 1.1(c) cannot be improved to smoothness on all of \(\{Q\succeq0\}\). Compute the derivative of \(Q\mapsto Q^{1/2}\) at \(Q=I\).

**5.4.** Show that \(F_V(\lambda P_x-\mu P_y)=\lambda f(x)-\mu f(y)\) for orthogonal lines \(x,y\) and \(\lambda,\mu\ge0\).

## 6. Solutions

**5.1.** Continuity, homogeneity, (a)–(e) of Lemma 2.1 and oddness of \(F_V\) do not use admissibility. Proposition 3.1(a)–(c) do: they need disjoint positive supports of \(E_V(A_+)\) and \(E_V(A_-)\). For \(k=2\), \(m=1\) and \(f\equiv1\), \(F_V(A)=\operatorname{tr}A_+-\operatorname{tr}A_-=\operatorname{tr}A\), and \(A=\operatorname{diag}(1,-1)\) gives \(0<2=\operatorname{tr}|A|\).

**5.2.** Lines at angles \(\theta\) and \(\theta+\pi/2\) are orthogonal, so an arc of length less than \(\pi/2\) contains no orthogonal pair. Take the arcs of length \(\pi/3+2\delta\) centred at \(0,\pi/3,2\pi/3\), with small \(\delta>0\), and a smooth partition of unity subordinate to them, as in Lemma 2.3 of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md). If \(x\) lies only in the \(i\)-th arc, that is, \(\theta\) is within \(\pi/6-\delta\) of its centre, then the functions assigned to the other two arcs vanish at \(x\), because their supports lie in those arcs; so \(F_V(P_x)=f(x)=e_i\) by Lemma 2.1(c).

**5.3.** \((t^{1/2}-0)/t=t^{-1/2}\to\infty\). Near \(I\), \((I+X/2)^2=I+X+X^2/4\), so the derivative of squaring at \(I\) is \(X\mapsto2X\) and the derivative of the square root at \(I\) is \(X\mapsto X/2\).

**5.4.** For \(A=\lambda P_x-\mu P_y\), \(A_+=\lambda P_x\) and \(A_-=\mu P_y\); use Lemma 2.1(a), (c).

## References

- [OpenAI-B9] OpenAI, *A nine-dimensional counterexample to Borsuk's covering assertion*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf
