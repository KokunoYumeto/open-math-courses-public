# Laguerre cells and prescribed masses

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The upper bound of the theorem of [Optimal maps of finite affine maxima](optimal-maps-of-finite-affine-maxima.md) is first proved for finite targets. A finite target with sites \(y_1,\dots,y_N\) and masses \(m_1,\dots,m_N\) is the image of \(\rho\) under the gradient of a finite affine maximum, and the problem is to choose intercepts whose cells have the prescribed masses. This lesson computes how the masses and first moments of the cells change when the intercepts and the sites move, and proves that intercepts realizing prescribed positive masses exist, are unique up to normalization, and depend differentiably on the sites.

- The derivatives of cell masses and moments, and the connectivity of the face graph (Proposition 1.1).
- Intercepts for prescribed masses (Proposition 2.1).

The lesson follows [OpenAI-BS, Section 3]. The face-integral formula for the mass derivative and its graph-Laplacian structure are standard in semi-discrete optimal transport [KMT, Theorem 1.3 and Section 5.3]; the calculation below includes the moments and the site variations needed later.

## 1. Cell calculus

Throughout, \(K\) is a compact convex set with nonempty interior, \(\rho=\mathbf 1_K\,dx/|K|\), and the sites \(y_1,\dots,y_N\) are distinct. For intercepts \(c=(c_1,\dots,c_N)\) put
\[
\ell_{ij}(x)=x\cdot(y_i-y_j)+c_i-c_j ,
\]
and define the cells, their masses and their first moments by
\[
\begin{gathered}
P_i=K\cap\bigcap_{j\ne i}\{\ell_{ij}\ge0\},\\
M_i=\rho(P_i),\qquad B_i=\int_{P_i}x\,d\rho(x) .
\end{gathered}
\]
These closed convex cells cover \(K\) and overlap only in the null tie set. Let \(H_{ij}=\{\ell_{ij}=0\}\) and \(F_{ij}=P_i\cap P_j\), the common face, and integrate over \(F_{ij}\) with the surface measure \(dS\) of the hyperplane \(H_{ij}\); a face of lower dimension contributes zero. The symmetric coefficients are
\[
\begin{gathered}
g_{ij}=\frac{1}{|K|\,|y_i-y_j|}\int_{F_{ij}}dS,\\
b_{ij}=\frac{1}{|K|\,|y_i-y_j|}\int_{F_{ij}}x\,dS,\\
\Theta_{ij}=\frac{1}{|K|\,|y_i-y_j|}\int_{F_{ij}}x\,x^{\mathsf T}\,dS ,
\end{gathered}
\]
and \(\Theta_{ij}\) is a symmetric \(d\times d\) matrix. We write \(DM_i[r,v]\) for the derivative of \(M_i\) in the direction of an intercept vector \(r=(r_i)\) and a site vector \(v=(v_i)\), \(v_i\in\mathbb R^d\), and likewise \(DB_i[r,v]\).

**Proposition 1.1** (cell differentials and connectivity; [OpenAI-BS, Proposition 3.1]). On the open set of configurations \((c,y)\) with distinct sites and \(M_i>0\) for every \(i\), the functions \(M_i\) and \(B_i\) are continuously differentiable in \((c,y)\), with
\[
\begin{aligned}
DM_i[r,v]&=\sum_{j\ne i}g_{ij}(r_i-r_j)\\
&\quad+\sum_{j\ne i}b_{ij}\cdot(v_i-v_j),\\
DB_i[r,v]&=\sum_{j\ne i}b_{ij}(r_i-r_j)\\
&\quad+\sum_{j\ne i}\Theta_{ij}(v_i-v_j) .
\end{aligned}
\]
The graph on \(\{1,\dots,N\}\) with an edge \(\{i,j\}\) when \(g_{ij}>0\) is connected. Consequently the symmetric operator
\[
(Gq)_i=DM_i[q,0]=\sum_{j\ne i}g_{ij}(q_i-q_j)
\]
has kernel the constant vectors and range \(\{z\in\mathbb R^N:\sum_iz_i=0\}\).

*Proof.* *Geometry.* Since \(M_i>0\), the cell \(P_i\) contains a point of \(\operatorname{int}K\) at which \(i\) is the only maximizing index: remove from the positive-measure cell the null set \(\partial K\) (Lemma 1.1 of the first lesson) and the finitely many tie hyperplanes. Call such points *strictly active* for \(i\). At a strictly active point for \(i\), \(\ell_{ij}>0\), and at one for \(j\), \(\ell_{ij}<0\); the segment between them lies in \(\operatorname{int}K\), so \(H_{ij}\) meets \(\operatorname{int}K\). By Lemma 1.1(3) of the first lesson, \(\partial K\cap H_{ij}\) is null in \(H_{ij}\).

Next, \(H_{ij}\ne H_{ik}\) for distinct \(i,j,k\). Otherwise the nonconstant affine functions \(\ell_{ij}\) and \(\ell_{ik}\) would be proportional, \(\ell_{ik}=\kappa\ell_{ij}\) with \(\kappa\ne0,1\), and with \(f_m(x)=x\cdot y_m+c_m\) this says \(f_k=(1-\kappa)f_i+\kappa f_j\). If \(0<\kappa<1\), \(f_k\) is a strict convex combination of \(f_i\) and \(f_j\); if \(\kappa>1\), so is \(f_j\) of \(f_k\) and \(f_i\); if \(\kappa<0\), so is \(f_i\) of \(f_k\) and \(f_j\). A strict convex combination of two other affine functions is never strictly maximal, which contradicts the positivity of all masses. Hence \(H_{ij}\cap H_{ik}\) is empty or of dimension at most \(d-2\), and null in \(H_{ij}\).

*Derivatives.* For a continuous \(f\) let
\[
I_i^f=\frac1{|K|}\int_Kf(x)\prod_{j\ne i}\mathbf 1_{\{\ell_{ij}(x)\ge0\}}\,dx .
\]
Replace \((c,y)\) by \((c+hr,y+hv)\) and write the change of the product of indicators as a telescoping sum, changing one factor at a time. In the term where the \(j\)-th factor changes, use coordinates \(x=z+ht\,n_{ij}\) with \(z\in H_{ij}\), \(t\in\mathbb R\) and \(n_{ij}=(y_i-y_j)/|y_i-y_j|\), so that \(dx=h\,dt\,dS(z)\). Since \(\ell_{ij}(z+htn_{ij})=ht|y_i-y_j|\) and the perturbed function is \(\ell_{ij}+h\bigl(x\cdot(v_i-v_j)+r_i-r_j\bigr)\), the changed factor converges, for almost every \((z,t)\), to
\[
\mathbf 1_{\{|y_i-y_j|t+r_i-r_j+z\cdot(v_i-v_j)\ge0\}}-\mathbf 1_{\{t\ge0\}} ,
\]
whose integral in \(t\) is \(w_{ij}(z)/|y_i-y_j|\), where \(w_{ij}(z)=r_i-r_j+z\cdot(v_i-v_j)\). The factor \(h\) of the volume element cancels the factor \(1/h\) of the difference quotient. Off the null set \((\partial K\cap H_{ij})\cup\bigcup_{k\ne i,j}(H_{ik}\cap H_{ij})\), all other indicators converge to their values at \(z\), and their product is the indicator of \(F_{ij}\) there: if \(z\in H_{ij}\cap P_i\), then \(\ell_{jk}(z)=\ell_{ik}(z)-\ell_{ij}(z)=\ell_{ik}(z)\ge0\), so \(z\in P_j\). The integrands are bounded with \(z\) and \(t\) in bounded sets, so dominated convergence gives
\[
\begin{aligned}
DI_i^f[r,v]&=\frac1{|K|}\sum_{j\ne i}\frac1{|y_i-y_j|}\\
&\quad\times\int_{F_{ij}}f(z)\,w_{ij}(z)\,dS(z) ,
\end{aligned}
\]
for \(h\downarrow0\), and the same argument with \(-h\) gives the two-sided derivative. The functions \(f=1\) and \(f=x_1,\dots,x_d\) give the two formulas.

*Continuity.* For nearby \((c,y)\), write a perturbed hyperplane \(H_{ij}\) as an affine graph over the fixed one in the direction \(n_{ij}\). The graph maps and their surface Jacobians converge uniformly on a common bounded region, the indicators of the faces converge off the same null sets, and the denominators \(|y_i-y_j|\) converge. By dominated convergence every coefficient of the derivative, including those with \(z_kz_l\), is continuous. So all partial derivatives exist and are continuous, and \(M_i\), \(B_i\) are continuously differentiable. The admissible set is open, since the masses are continuous by dominated convergence.

*Connectivity.* Fix two cells and strictly active points \(p\) and \(q\) for them, with \(p\) off all hyperplanes \(H_{kl}\), and \(q\) off all \(H_{kl}\) and off the affine spans of \(p\) with the sets where three affine functions tie. These are finitely many proper affine subsets, which cannot cover the open set of strictly active points of a cell. The segment \([p,q]\) lies in \(\operatorname{int}K\) and meets no triple tie. Where the active index changes along it, exactly two affine functions are maximal and all other inequalities are strict, so a small relatively open disc in their tie hyperplane belongs to the common face, which therefore has positive area: an edge of the graph. The successive active indices give a path between the two cells.

*The operator \(G\).* By symmetry of \(g_{ij}\), \(q\cdot Gq=\sum_{i<j}g_{ij}(q_i-q_j)^2\). If this vanishes, \(q\) is constant along edges, hence constant by connectivity. As \(G\) is symmetric, its range is the orthogonal complement of its kernel. \(\blacksquare\)

## 2. Prescribed masses

**Proposition 2.1** (prescribed cell masses; [OpenAI-BS, Proposition 3.2]). Fix positive weights \(m_1,\dots,m_N\) with \(\sum_im_i=1\). For every configuration of distinct sites there is exactly one vector of intercepts \(c\) with
\[
\begin{gathered}
M_i=m_i\quad(1\le i\le N),\\
\sum_im_ic_i=0 .
\end{gathered}
\]
With the weights fixed, this vector is a continuously differentiable function of the sites on the open set of configurations of distinct sites.

*Proof.* For \(N=1\), \(c_1=0\). Let \(N\ge2\), and on \(H_m=\{c:\sum_im_ic_i=0\}\) consider the convex function
\[
\begin{aligned}
\mathcal F_y(c)&=\int_K\max_i(x\cdot y_i+c_i)\,d\rho(x)\\
&\quad-\sum_im_ic_i .
\end{aligned}
\]
*Existence.* Let \(|x|\le R\) on \(K\) and \(S=\max_i|y_i|\). On \(H_m\), \(\mathcal F_y(c)\ge\max_ic_i-RS\). If \(\max_ic_i\le A\) on \(H_m\), then each \(c_k=-\sum_{i\ne k}m_ic_i/m_k\) is at least \(-A(1-m_k)/m_k\), so \(c\) is bounded; hence \(\max_ic_i\to\infty\) as \(|c|\to\infty\) in \(H_m\). So \(\mathcal F_y\) is coercive and continuous on \(H_m\), and has a minimum. The difference quotients of \(c\mapsto\max_i(x\cdot y_i+c_i)\) in the direction of the \(i\)-th unit vector lie in \([0,1]\) and converge, off the tie set, to the indicator of the cell \(P_i\). By dominated convergence,
\[
\nabla_c\mathcal F_y=(M_i-m_i)_{i=1}^N .
\]
At a minimum on \(H_m\) this gradient is orthogonal to \(H_m\), that is a multiple \(\kappa m\) of \(m\). Its coordinates sum to zero, because both the masses and the weights sum to one, so \(\kappa=0\) and \(M_i=m_i\). Conversely, every normalized solution has zero gradient and is a minimizer, by convexity.

*Local structure.* At a solution all masses are positive, and Proposition 1.1 applies. The map \(c\mapsto(M_i-m_i)_i\) sends \(H_m\) into \(H_0=\{z:\sum_iz_i=0\}\), and its derivative at the solution is the restriction \(G\colon H_m\to H_0\). This is injective, since the only constant vector in \(H_m\) is zero, and both spaces have dimension \(N-1\), so it is an isomorphism. The implicit function theorem ([Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20); [Lebl, Basic Analysis II, Theorem 8.5.6](https://www.jirka.org/ra/html/sec_svinvfuncthm.html#thm_implicit)) gives, near each solution, a unique solution for nearby sites, depending continuously differentiably on them.

*Uniqueness.* In particular each solution is isolated for its sites. If there were two, the segment between them would consist of minimizers of the convex function \(\mathcal F_y\) on \(H_m\), hence of solutions, contradicting isolation. So the solution is unique, the local branches agree on overlaps, and they define one continuously differentiable function of the sites. \(\blacksquare\)

Only the invertibility of \(G\) on \(H_m\) is used here; no quantitative bound on its inverse is needed, and none would be uniform as cells become small or faces become thin. The next lesson supplies the estimate that replaces such a bound.

## 3. Exercises

**3.1.** For \(K=[0,1]\times[-1,1]\) and three sites \(y_1=(0,0)\), \(y_2=(1,0)\), \(y_3=(2,0)\), find the intercepts with \(\sum_im_ic_i=0\) that give the masses \(m=(\frac14,\frac12,\frac14)\).

**3.2.** Show that \(\sum_iDM_i[r,v]=0\) for all directions, directly from the formulas of Proposition 1.1.

**3.3.** Show that \(\sum_iq_i\,DM_i[r,v]\) is symmetric in \(q\) and \(r\) when \(v=0\), and compute its site part \(\sum_iq_i\sum_{j\ne i}b_{ij}\cdot(v_i-v_j)\) as a sum over unordered pairs.

**3.4.** Give an example with \(N=3\) where the face graph is a path and not a triangle.

**3.5.** Show that the normalization \(\sum_im_ic_i=0\) is needed for uniqueness, and that without it the intercepts are unique up to adding a common constant.

## 4. Solutions

**3.1.** The cells are vertical strips. Cell 1 is \(\{x_1\le c_1-c_2\}\), cell 3 is \(\{x_1\ge c_2-c_3\}\), and \(\rho\) of a strip of width \(w\) is \(w\). So \(c_1-c_2=\frac14\) and \(c_2-c_3=\frac34\). With \(c_2=s\): \(c_1=s+\frac14\), \(c_3=s-\frac34\), and \(\frac14(s+\frac14)+\frac12s+\frac14(s-\frac34)=0\) gives \(s=\frac18\), so \(c=(\frac38,\frac18,-\frac58)\).

**3.2.** The terms \(g_{ij}(r_i-r_j)\) and \(g_{ji}(r_j-r_i)\) cancel, and so do \(b_{ij}\cdot(v_i-v_j)\) and \(b_{ji}\cdot(v_j-v_i)\), since \(g\) and \(b\) are symmetric. This expresses \(\sum_iM_i=1\).

**3.3.** \(\sum_iq_i\sum_{j\ne i}g_{ij}(r_i-r_j)\) equals \(\sum_{i<j}g_{ij}(q_i-q_j)(r_i-r_j)\), which is symmetric. Likewise the site part is \(\sum_{i<j}(q_i-q_j)\,b_{ij}\cdot(v_i-v_j)\).

**3.4.** In Exercise 3.1 the cells 1 and 3 do not touch: \(g_{13}=0\), and the graph is the path \(1-2-3\).

**3.5.** Adding a constant to all intercepts changes no cell, so without a normalization uniqueness fails; with \(\sum_im_ic_i=0\) imposed, Proposition 2.1 applies, and two solutions differing by a constant \(\kappa\) have \(\kappa\sum_im_i=0\), that is \(\kappa=0\).

## References

- [OpenAI-BS] OpenAI, *Sharp one-third stability of Brenier maps*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026
- [KMT] J. Kitagawa, Q. Mérigot and B. Thibert, *Convergence of a Newton algorithm for semi-discrete optimal transport*, J. Eur. Math. Soc. 21 (2019), Theorem 1.3 and Section 5.3. https://arxiv.org/abs/1603.05579
