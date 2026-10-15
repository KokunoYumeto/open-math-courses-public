# The null conic and the recovery of the moduli

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For each point \(x\), the comparison field \(G(x,\cdot)\) of [Matching the transports](matching-the-transports.md) is a holomorphic endomorphism field of the bundle \(\mathcal E=H\oplus\mathbb C\) over the null conic \(\mathcal C\). The bundle \(H\) of planes \(H_\theta=\theta^\perp\) has no holomorphic sections other than zero, and together with the transport equation this forces \(G=\mathrm{Id}\) [OpenAI-EL, Section 6]. The two transport equations then coincide. Their last entries determine the ratio \(k/\ell\), and their bottom rows give a second-order equation for \(\log\mu_1-\log\mu_2\) whose solutions are determined by their values on an open set. This proves Theorem 4.1 of The displacement-to-traction map.

- Holomorphic sections over the null conic (Section 1).
- Rigidity of the comparison (Section 2).
- A finite-type uniqueness lemma (Section 3).
- Recovery of the moduli (Section 4).

We keep the notation of [Matching the transports](matching-the-transports.md): the conic \(\mathcal C\), its parametrization \(\theta(z_0,z_1)=(z_0^2-z_1^2,\ i(z_0^2+z_1^2),\ 2z_0z_1)\) and its two charts \(v=z_1/z_0\) and \(v=z_0/z_1\) from Lemma 2.1 there; the bundles \(H\) and \(\mathcal E\) and their holomorphic bases; the transport matrices \(M_{j,\theta}\) of (1.2) there, with entries \(Q_{j,\theta}\) and \(T_{j,\theta}\); and the field \(G\) of Proposition 4.1 there. We write \(\mathcal N\) for the line subbundle of \(H\) with fibers \(\mathbb C\theta\). We use Liouville's theorem from the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50) (Lebl, *Guide to Cultivating Complex Analysis*, [Theorem 3.3.10](https://www.jirka.org/ca/ca.pdf)).

## 1. Holomorphic sections over the null conic

Since \(\theta(cz)=c^2\theta(z)\), we have \(\theta(1,v)=v^2\,\theta(1/v,1)\) for \(v\ne0\): the point \([\theta(1,v)]\) of the first chart is the point \([\theta(1/v,1)]\) of the second.

**Lemma 1.1** (holomorphic functions and sections). 

1. Every holomorphic function on \(\mathcal C\) is constant.
2. The null vectors \(\theta(1,0)=(1,i,0)\), \(\theta(0,1)=(-1,i,0)\) and \(\theta(1,1)=(0,2i,2)\) span \(\mathbb C^3\).
3. A section \(\sigma\) of \(H\), that is, a map with \(\sigma([\theta])\in H_\theta\), is holomorphic exactly when its three components in \(\mathbb C^3\) are holomorphic functions on \(\mathcal C\). Every holomorphic section of \(H\) is zero.

*Proof.* (1) Let \(f\) be holomorphic on \(\mathcal C\). In the first chart, \(F(v)=f([\theta(1,v)])\) is an entire function. As \(v\to\infty\), \(F(v)=f([\theta(1/v,1)])\) tends to \(f([\theta(0,1)])\), because \(f\) is holomorphic, hence continuous, in the second chart. So \(F\) is bounded, and constant by Liouville's theorem. The only point of \(\mathcal C\) outside the first chart is \([\theta(0,1)]\), where \(f\) takes the same value by continuity.

(2) Expanding along the last column, the determinant of the matrix with rows \((1,i,0)\), \((-1,i,0)\), \((0,2i,2)\) is \(2\,(1\cdot i-i\cdot(-1))=4i\ne0\).

(3) Where \(\theta_i\ne0\), the basis of \(H_\theta\) is \(e_j-(\theta_j/\theta_i)e_i\), \(j\ne i\), and \(\sigma=\sum_{j\ne i}\sigma_j\bigl(e_j-(\theta_j/\theta_i)e_i\bigr)\). So the coefficients of \(\sigma\) in this basis are its components \(\sigma_j\), \(j\ne i\), and the remaining component is \(\sigma_i=-\sum_{j\ne i}\sigma_j\theta_j/\theta_i\), with \(\theta_j/\theta_i\) holomorphic. This proves the first assertion. If \(\sigma\) is holomorphic, its components are constant by (1), so \(\sigma\) is a constant vector \(w\) with \(w\cdot\theta=0\) for every null vector \(\theta\). By (2), \(w=0\). \(\square\)

**Lemma 1.2** (a frame of \(H\) and the quotient by \(\mathcal N\); [OpenAI-EL, Lemma 6.1]). For \(z=(z_0,z_1)\ne0\) put
\[
\begin{gathered}h_1(z)=(z_0,\ iz_0,\ z_1),\\ h_2(z)=(-z_1,\ iz_1,\ z_0).\end{gathered}
\]
Then, with \(\theta=\theta(z)\),
\[
\begin{gathered}\theta\cdot h_1=\theta\cdot h_2=0,\\ h_1\times h_2=i\theta,\\ \theta=z_0h_1+z_1h_2 .\end{gathered}\tag{1.1}
\]
Moreover:

1. \(h_1(z),h_2(z)\) is a basis of \(H_{\theta(z)}\), and \(h_1(1,v),h_2(1,v)\) and \(h_1(v,1),h_2(v,1)\) are holomorphic frames of \(H\) on the two charts.
2. The linear form \(\pi\) on \(H_{\theta(z)}\) that maps \(\xi_1h_1(z)+\xi_2h_2(z)\) to \(-z_1\xi_1+z_0\xi_2\) depends only on the point \([\theta(z)]\), not on \(z\), and its kernel is \(\mathbb C\theta\). On the two charts, the sections \(p_0=h_2(1,v)\) and \(p_0=-h_1(v,1)\) are holomorphic and satisfy \(\pi(p_0)=1\).
3. For \(p\in H_\theta\), \(p\cdot p=\pi(p)^2\).
4. Every holomorphic endomorphism field of \(H\) that vanishes on \(\mathcal N\) is zero.

*Proof.* Direct calculation gives
\[
\begin{aligned}\theta\cdot h_1&=(z_0^2-z_1^2)z_0-(z_0^2+z_1^2)z_0\\&\quad+2z_0z_1^2=0,\\ \theta\cdot h_2&=-(z_0^2-z_1^2)z_1-(z_0^2+z_1^2)z_1\\&\quad+2z_0^2z_1=0,\\ h_1\times h_2&=\begin{pmatrix}i(z_0^2-z_1^2)\\ -(z_0^2+z_1^2)\\ 2iz_0z_1\end{pmatrix}=i\theta,\end{aligned}
\]
and \(z_0h_1+z_1h_2\) is \((z_0^2-z_1^2,\ i(z_0^2+z_1^2),\ 2z_0z_1)=\theta\).

(1) Since \(\theta\ne0\), \(h_1\times h_2\ne0\), so \(h_1\) and \(h_2\) are linearly independent; they lie in \(H_\theta\), which has dimension two. Their components are polynomials in \(v\) on the two charts, so they are holomorphic sections by Lemma 1.1(3).

(2) If \(z\) is replaced by \(cz\), \(c\ne0\), then \(h_j(cz)=c\,h_j(z)\), so the coefficients of a fixed \(p\) become \(\xi_j/c\), and \(-cz_1\xi_1/c+cz_0\xi_2/c=-z_1\xi_1+z_0\xi_2\). By (1.1), \(\pi(\theta)=-z_1z_0+z_0z_1=0\), and \(\pi\ne0\) because \(\pi(h_1)=-z_1\) and \(\pi(h_2)=z_0\) do not both vanish. So the kernel of \(\pi\) is the line \(\mathbb C\theta\). For \(p_0=h_2(1,v)\), the coefficients are \((0,1)\) and \(\pi(p_0)=z_0=1\); for \(p_0=-h_1(v,1)\) they are \((-1,0)\) and \(\pi(p_0)=z_1=1\).

(3) From \(h_1\cdot h_1=z_1^2\), \(h_2\cdot h_2=z_0^2\) and \(h_1\cdot h_2=-z_0z_1\), for \(p=\xi_1h_1+\xi_2h_2\),
\[
\begin{aligned}p\cdot p&=\xi_1^2z_1^2-2\xi_1\xi_2z_0z_1+\xi_2^2z_0^2\\&=(-z_1\xi_1+z_0\xi_2)^2 .\end{aligned}
\]
(4) Let \(\varphi\) be such a field. At each point choose \(p\in H_\theta\) with \(\pi(p)=1\) and put \(\sigma=\varphi(p)\). Two choices differ by an element of \(\ker\pi=\mathbb C\theta\), on which \(\varphi\) vanishes, so \(\sigma\) is well defined. On each chart \(\sigma=\varphi(p_0)\), a holomorphic section, so \(\sigma=0\) by Lemma 1.1(3). Every \(p\in H_\theta\) is \(\pi(p)p_0+\bigl(p-\pi(p)p_0\bigr)\), with the second term in \(\ker\pi\), so \(\varphi(p)=\pi(p)\sigma=0\). \(\square\)

In the language of line bundles over \(\mathbb C\mathrm P^1\): with the tautological line bundle \(\mathcal O(-1)\), whose fiber over \([z]\) is \(\mathbb Cz\), the map \((\xi_1z,\xi_2z)\mapsto\xi_1h_1(z)+\xi_2h_2(z)\) is well defined and identifies \(\mathcal O(-1)\oplus\mathcal O(-1)\) with \(H\); the map \(\xi\,z\otimes z\mapsto\xi\,\theta(z)\) identifies \(\mathcal O(-2)\) with \(\mathcal N\); and \(\pi\) identifies \(H/\mathcal N\) with the trivial line bundle. The resulting sequence \(0\to\mathcal N\to H\to\mathbb C\to0\) has no holomorphic splitting, since a splitting would be a holomorphic section \(p\) of \(H\) with \(\pi(p)=1\). Holomorphic endomorphism fields of \(H\) need not be multiples of the identity (Exercise 5.2), so holomorphy of \(G\) alone does not give \(G=\mathrm{Id}\); the proof below uses the transport equation as well.

## 2. Rigidity of the comparison

**Proposition 2.1** (rigidity; [OpenAI-EL, Proposition 6.3]). The field \(G\) of Proposition 4.1 of [Matching the transports](matching-the-transports.md) is the identity. Consequently, for every \(x\in\mathbb R^3\) and every nonzero null vector \(\theta\),
\[
\begin{gathered}M_{1,\theta}(x)=M_{2,\theta}(x)\\ \text{on }\mathcal E_\theta .\end{gathered}\tag{2.1}
\]

*Proof.* Fix \(x\). Relative to \(\mathcal E_\theta=H_\theta\oplus\mathbb C\) write
\[
G(x,[\theta])=\begin{pmatrix}F&\sigma\\ A&f\end{pmatrix},
\]
with \(F\in\operatorname{End}(H_\theta)\), \(\sigma\in H_\theta\), \(A\) a linear form on \(H_\theta\) and \(f\in\mathbb C\). In holomorphic frames of \(\mathcal E\) these blocks are blocks of a holomorphic matrix, so \(\sigma\) is a holomorphic section of \(H\), \(f\) is a holomorphic function on \(\mathcal C\), and \(F\) is a holomorphic endomorphism field of \(H\). By Lemma 1.1, \(\sigma=0\) and \(f\) does not depend on the direction: \(f=f(x)\), a smooth function of \(x\), because \(G\) is smooth.

With \(M_{j,\theta}=\begin{pmatrix}0&\theta\\ Q_{j,\theta}\cdot&T_{j,\theta}\end{pmatrix}\),
\[
\begin{aligned}M_{2,\theta}G&=\begin{pmatrix}\theta A&f\theta\\ Q_{2,\theta}\cdot F+T_{2,\theta}A&fT_{2,\theta}\end{pmatrix},\\ GM_{1,\theta}&=\begin{pmatrix}0&F\theta\\ fQ_{1,\theta}\cdot&A(\theta)+fT_{1,\theta}\end{pmatrix},\end{aligned}
\]
where \(\theta A\) is the map \(p\mapsto A(p)\,\theta\). The upper-right block of \(D_\theta G=M_{2,\theta}G-GM_{1,\theta}\) gives \(0=f\theta-F\theta\). So the holomorphic endomorphism field \(F-f\,\mathrm{Id}_H\) vanishes on \(\mathcal N\), and \(F=f\,\mathrm{Id}_H\) by Lemma 1.2(4).

The upper-left block now reads
\[
(D_\theta f)\,\mathrm{Id}_{H_\theta}=\theta A .
\tag{2.2}
\]
The right side has rank at most one, and \(H_\theta\) has dimension two, so \(D_\theta f=0\); then \(\theta A=0\), and \(A=0\) because \(\theta\ne0\). This holds at every \(x\) and for every null \(\theta\), and null vectors span \(\mathbb C^3\) by Lemma 1.1(2), so \(\nabla f=0\) and \(f\) is constant on \(\mathbb R^3\). As \(G=\mathrm{Id}\) for \(|x|>2r\), \(f=1\). Thus \(G=\mathrm{Id}\), and the equation \(D_\theta G=M_{2,\theta}G-GM_{1,\theta}\) becomes (2.1). \(\square\)

## 3. A finite-type uniqueness lemma

**Lemma 3.1** (finite-type uniqueness; [OpenAI-EL, Lemma 6.4]). Let \(U\subset\mathbb R^n\), \(n\ge2\), be open and connected, and let \(\eta\), \(q\) and \(B_{ij}^{\ a}\) (\(1\le i,j,a\le n\)) be smooth real or complex functions on \(U\) with
\[
\begin{gathered}\partial_i\partial_j\eta=\sum_{a=1}^nB_{ij}^{\ a}\,\partial_a\eta+\delta_{ij}\,q\\ (1\le i,j\le n).\end{gathered}\tag{3.1}
\]
Then \(w=(\nabla\eta,q)\) satisfies a linear system \(\partial_sw=\mathfrak B_sw\), \(1\le s\le n\), with smooth matrices \(\mathfrak B_s\). If \(\eta\) vanishes on a nonempty open subset of \(U\), then \(\eta=0\) and \(q=0\) on \(U\).

*Proof.* Put \(v_a=\partial_a\eta\). By (3.1) with \((i,j)=(a,s)\),
\[
\partial_sv_a=\sum_{b=1}^nB_{as}^{\ b}v_b+\delta_{as}\,q .
\tag{3.2}
\]
For each \(s\) choose an index \(i=i(s)\ne s\); here \(n\ge2\) is used. Third derivatives commute, so \(\partial_i(\partial_s\partial_i\eta)=\partial_s(\partial_i\partial_i\eta)\). By (3.1), \(\partial_s\partial_i\eta=\sum_aB_{si}^{\ a}v_a\), with no term in \(q\) because \(s\ne i\), and \(\partial_i\partial_i\eta=\sum_aB_{ii}^{\ a}v_a+q\). Therefore
\[
\begin{aligned}\partial_sq&=\partial_i\Bigl(\sum_aB_{si}^{\ a}v_a\Bigr)-\partial_s\Bigl(\sum_aB_{ii}^{\ a}v_a\Bigr)\\&=\sum_a\bigl(\partial_iB_{si}^{\ a}-\partial_sB_{ii}^{\ a}\bigr)v_a\\&\quad+\sum_a\bigl(B_{si}^{\ a}\,\partial_iv_a-B_{ii}^{\ a}\,\partial_sv_a\bigr).\end{aligned}
\]
Substituting (3.2) for \(\partial_iv_a\) and \(\partial_sv_a\) gives
\[
\begin{aligned}\partial_sq&=\sum_{b=1}^nC_s^{\ b}v_b+d_s\,q,\\ C_s^{\ b}&=\partial_iB_{si}^{\ b}-\partial_sB_{ii}^{\ b}\\&\quad+\sum_{a=1}^nB_{si}^{\ a}B_{ai}^{\ b}\\&\quad-\sum_{a=1}^nB_{ii}^{\ a}B_{as}^{\ b},\\ d_s&=B_{si}^{\ i}-B_{ii}^{\ s}.\end{aligned}\tag{3.3}
\]
Together, (3.2) and (3.3) are the claimed system.

Suppose \(\eta=0\) on a nonempty open set \(V\subset U\), and fix \(x_0\in V\). On \(V\), \(v=\nabla\eta=0\), and (3.1) with \(i=j=1\) gives \(q=0\). Let \(x\in U\). The points of \(U\) that can be joined to \(x_0\) by a polygonal path in \(U\) form an open set, and so do the remaining points of \(U\), because balls are convex; as \(U\) is connected, there is a polygonal path from \(x_0\) to \(x\). On one of its segments \(t\mapsto x_1+t\,e\), \(0\le t\le1\), the function \(w(t)=w(x_1+t\,e)\) satisfies \(w'(t)=\sum_se_s\mathfrak B_s(x_1+t\,e)\,w(t)\), with a coefficient bounded by some \(C\). If \(w(0)=0\), then \(|w(t)|\le C\int_0^t|w|\), so \(W(t)=\int_0^t|w|\) satisfies \(W'\le CW\) and \(W(0)=0\); hence \(\bigl(e^{-Ct}W\bigr)'\le0\), \(W\le0\), and \(W=0\), so \(w=0\) on the segment. Segment by segment, \(w(x)=0\). Thus \(\nabla\eta=0\) and \(q=0\) on \(U\), \(\eta\) is constant on the connected set \(U\), and its value is zero because \(\eta=0\) on \(V\). \(\square\)

## 4. Recovery of the moduli

*Proof of Theorem 4.1 of The displacement-to-traction map.* Let the two pairs satisfy the hypotheses of that theorem with \(\Lambda_{\lambda_1,\mu_1}=\Lambda_{\lambda_2,\mu_2}\). Lemma 3.1 of [Boundary jets and the transfer of solutions](boundary-jets-and-the-transfer-of-solutions.md) extends them to \(\mathbb R^3\), equal outside \(\Omega\) and constant outside a ball, and all constructions of the course apply to these extensions. By Proposition 4.1 of [Matching the transports](matching-the-transports.md) and Proposition 2.1, (2.1) holds for every \(x\) and every nonzero null \(\theta\).

*The ratio \(k/\ell\).* The bottom-right entries of (2.1) give \(T_{1,\theta}=T_{2,\theta}\), that is, \(\theta\cdot\nabla\bigl(\log(k_1/\ell_1)-\log(k_2/\ell_2)\bigr)=0\) for every null \(\theta\). By Lemma 1.1(2) the gradient vanishes, so the difference is constant on \(\mathbb R^3\), and it is zero outside \(\Omega\). Hence \(k_1/\ell_1=k_2/\ell_2\). As \(m_j/\ell_j=1-k_j/\ell_j\) and \(k_j/m_j=(k_j/\ell_j)/(1-k_j/\ell_j)\), the functions
\[
\begin{gathered}c=\frac{m_1}{\ell_1}=\frac{m_2}{\ell_2},\\ b_*=\log\frac{k_1}{m_1}=\log\frac{k_2}{m_2}\end{gathered}\tag{4.1}
\]
are well defined and smooth; \(0<c<1\) because \(m_j>0\) and \(k_j>m_j/3>0\).

*The bottom-left entries.* For \(p\in H_\theta\), (2.1) gives \((Q_{1,\theta}-Q_{2,\theta})\cdot p=0\). By (1.3) of [Matching the transports](matching-the-transports.md), with \(D_\theta\log k=(\nabla\log k)^T\theta\), \(\theta\cdot g=g^T\theta\) and \(D_\theta g=(\nabla^2\log m)\,\theta\), we have \(Q_{j,\theta}=K_j\theta\) with the matrices
\[
\begin{aligned}2K_j&=c\,g_j(\nabla\log k_j)^T-\frac12\,g_jg_j^T\\&\quad-c\,\nabla^2\log m_j,\qquad g_j=\nabla\log m_j .\end{aligned}
\]
Put \(K=K_1-K_2\). Then \(K\theta\cdot p=0\) for all \(p\) in \(H_\theta=\{p\in\mathbb C^3:\theta\cdot p=0\}\), a plane. The vectors orthogonal to this plane for the nondegenerate bilinear form form a line, which contains \(\theta\); so \(K\theta\in\mathbb C\theta\) for every null \(\theta\).

*\(K\) is scalar.* Fix \(x\). On a chart with its holomorphic representative \(\theta(v)\), and near a point where the component \(\theta_a(v)\) does not vanish, put \(\phi=(K\theta(v))_a/\theta_a(v)\), a holomorphic function. As \(K\theta=\phi\,\theta\), \(\phi\) does not depend on the choice of \(a\), nor on the representative of the direction, so it is a holomorphic function on \(\mathcal C\), constant by Lemma 1.1(1): \(\phi=\kappa(x)\). Then \((K-\kappa\,\mathrm{Id})\theta=0\) for every null \(\theta\), and Lemma 1.1(2) gives
\[
K=\kappa\,\mathrm{Id},\qquad\kappa=\tfrac13\operatorname{tr}K ,
\tag{4.2}
\]
so \(\kappa\) is smooth.

*A Hessian equation.* Put
\[
\begin{gathered}\eta=\log m_1-\log m_2,\\ v=\nabla\eta=g_1-g_2,\\ \beta=\nabla b_*,\qquad\alpha=\frac{c-1/2}c .\end{gathered}
\]
By (4.1), \(\log k_j=\log m_j+b_*\), so \(\nabla\log k_j=g_j+\beta\) and
\[
\begin{aligned}2K_j&=\Bigl(c-\frac12\Bigr)g_jg_j^T+c\,g_j\beta^T\\&\quad-c\,\nabla^2\log m_j .\end{aligned}
\]
Subtracting, using \(g_1g_1^T-g_2g_2^T=g_1v^T+vg_2^T\) and (4.2), dividing by \(c\) and putting \(q=-2\kappa/c\),
\[
\nabla^2\eta=\alpha\bigl(g_1v^T+vg_2^T\bigr)+v\beta^T+q\,\mathrm{Id}.
\]
In coordinates, with \(v_a=\partial_a\eta\),
\[
\begin{aligned}\partial_i\partial_j\eta&=\sum_{a=1}^3B_{ij}^{\ a}\,\partial_a\eta\\&\quad+\delta_{ij}\,q,\\ B_{ij}^{\ a}&=\alpha(g_1)_i\delta_{ja}\\&\quad+\bigl(\alpha(g_2)_j+\beta_j\bigr)\delta_{ia},\end{aligned}\tag{4.3}
\]
with coefficients smooth on \(\mathbb R^3\).

*Conclusion.* The pairs agree on the nonempty open set \(\mathbb R^3\setminus\overline\Omega\), so \(\eta=0\) there. Lemma 3.1, applied to (4.3) on \(U=\mathbb R^3\), gives \(\eta=0\) on \(\mathbb R^3\), that is, \(m_1=m_2\). By (4.1), \(k_1=m_1e^{b_*}=m_2e^{b_*}=k_2\). Hence \(\mu_1=m_1=m_2=\mu_2\) and \(\lambda_1=k_1-m_1=k_2-m_2=\lambda_2\) on \(\mathbb R^3\), in particular on \(\overline\Omega\). \(\square\)

Theorem 4.1 of The displacement-to-traction map is thereby proved from four named results of the literature: Hypotheses (BD) and (ER) of [Boundary jets and the transfer of solutions](boundary-jets-and-the-transfer-of-solutions.md), Hypothesis (CE) of An augmented system and a Carleman estimate and Hypothesis (HF) of [Planar transport equations](planar-transport-equations.md). All other steps are proved in this course and in the lessons it names.

## 5. Exercises

**5.1.** Let \(\theta\ne0\) be null. Show that the null vectors \(p\) with \(\theta\cdot p=0\) are exactly the multiples of \(\theta\).

**5.2.** Show that \(\psi\bigl(\xi_1h_1(z)+\xi_2h_2(z)\bigr)=\xi_1h_1(z)\) defines a holomorphic endomorphism field of \(H\) which is not a multiple of the identity at any point. Where does it vanish on \(\mathcal N\)?

**5.3.** Give a proof of (4.2) without holomorphic functions: let \(K\) be a complex \(3\times3\) matrix with \(K\theta\in\mathbb C\theta\) for every null vector \(\theta\). Show that \(K\) is a multiple of the identity, using that a plane in \(\mathbb C^3\) contains at most two lines of null vectors.

**5.4.** Show that the conclusion of Lemma 3.1 fails for \(n=1\).

**5.5.** Show that the positivity conditions \(\mu>0\), \(3\lambda+2\mu>0\) give \(\frac14<k/\ell<1\) and \(0<c<\frac34\), where \(k/\ell=(\lambda+\mu)/(\lambda+2\mu)\) and \(c=\mu/(\lambda+2\mu)\). Show that \(\mu\) and \(k/\ell\) together determine \(\lambda\).

## 6. Solutions

**5.1.** Such \(p\) lies in \(H_\theta\), and by Lemma 1.2(3), \(0=p\cdot p=\pi(p)^2\), so \(p\in\ker\pi=\mathbb C\theta\). Conversely \(\theta\cdot\theta=0\). Geometrically, the plane \(H_\theta\) meets the null cone only along the line \(\mathbb C\theta\): it is the tangent plane of the cone along that line.

**5.2.** Replacing \(z\) by \(cz\) replaces \(\xi_1\) by \(\xi_1/c\) and \(h_1(z)\) by \(c\,h_1(z)\), so \(\psi\) is well defined; in the frames \(h_1,h_2\) of Lemma 1.2(1) its matrix is \(\begin{pmatrix}1&0\\0&0\end{pmatrix}\), so it is holomorphic, of rank one, and not a multiple of the identity. By (1.1), \(\psi(\theta)=z_0h_1(z)\), which vanishes only at \(z_0=0\), the point \([\theta(0,1)]\). So \(\psi\) does not vanish on \(\mathcal N\), and Lemma 1.2(4) does not apply to it.

**5.3.** If \(\Pi\) is a plane and every vector of \(\Pi\) were null, then for \(p,p'\in\Pi\) the product \(2p\cdot p'\) equals \((p+p')\cdot(p+p')-p\cdot p-p'\cdot p'=0\), so \(\Pi\subset\Pi^\perp\); but \(\Pi^\perp\) has dimension one. So the bilinear form restricted to \(\Pi\) is a nonzero quadratic form in two variables, whose zero set is at most two lines. Now every null \(\theta\ne0\) is an eigenvector of \(K\), so the null cone lies in the union of the eigenspaces of \(K\). If \(K\) is not a multiple of the identity, there are at most three eigenspaces, each of dimension at most two, so the null vectors lie on at most six lines. But by Lemma 2.1 of [Matching the transports](matching-the-transports.md), the vectors \(\theta(1,v)\), \(v\in\mathbb C\), lie on infinitely many distinct lines. So \(K\) is a multiple of the identity.

**5.4.** Take \(U=\mathbb R\), \(B=0\), a smooth \(\eta\) with \(\eta=0\) on \((-\infty,0]\) and \(\eta(1)=1\) (for instance \(\eta(x)=e^{1-1/x}\) for \(x>0\)), and \(q=\eta''\). Then (3.1) holds, \(\eta\) vanishes on an open set, and \(\eta\ne0\). The proof breaks down because there is no index \(i\ne s\): for \(n=1\), (3.1) is a single equation that defines \(q\) and does not constrain \(\eta\).

**5.5.** \(k/\ell=1-\mu/(\lambda+2\mu)\), and \(\lambda+2\mu=\frac13(3\lambda+2\mu)+\frac43\mu>\frac43\mu>0\), so \(0<\mu/(\lambda+2\mu)<\frac34\). This gives \(\frac14<k/\ell<1\) and \(0<c=1-k/\ell<\frac34\). Given \(\mu\) and \(\rho=k/\ell\), the equation \(\lambda+\mu=\rho(\lambda+2\mu)\) gives \(\lambda=\mu(2\rho-1)/(1-\rho)\), as \(\rho<1\).

## References

- [OpenAI-EL] OpenAI, *Global uniqueness for the smooth isotropic elasticity inverse problem*, OpenAI Math Release preprint, 24 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026
