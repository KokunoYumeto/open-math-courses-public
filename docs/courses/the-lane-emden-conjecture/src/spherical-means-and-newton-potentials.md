# Spherical means and Newton potentials

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This course proves a Liouville theorem for a coupled pair of nonlinear elliptic equations, obtained by OpenAI in 2026 [OpenAI-LE]:

**Theorem** (OpenAI 2026). Let \(n\ge2\) be an integer, \(p,q>0\) and \(A,B\in\mathbb R\), and suppose
\[
\frac{n+A}{p+1}+\frac{n+B}{q+1}>n-2 .
\]
Then there are no functions \(u,v\), continuous and positive on \(\mathbb R^n\) and twice continuously differentiable on \(\mathbb R^n\setminus\{0\}\), such that
\[
-\Delta u=|x|^Av^p,\qquad-\Delta v=|x|^Bu^q\qquad\text{on }\mathbb R^n\setminus\{0\}.
\]

For \(A=B=0\) this is the *Lane–Emden conjecture*: for \(n\ge3\) and \(\frac1{p+1}+\frac1{q+1}>\frac{n-2}n\), the system \(-\Delta u=v^p\), \(-\Delta v=u^q\) has no positive solution on \(\mathbb R^n\). The scalar case \(u=v\), \(p=q\), is the Liouville theorem of Gidas and Spruck. For systems, Mitidieri introduced Rellich-type identities; Serrin and Zou proved the conjecture in dimension three for solutions of polynomial growth, Poláčik, Quittner and Souplet removed the growth condition [PQS], Souplet settled dimension four, and Li, Li and Wei found a further region in every dimension \(n\ge5\) [LLW]. With the weights \(|x|^A\), \(|x|^B\) (the Hénon–Lane–Emden system), Phan formulated the conjecture for \(A,B>-2\) [Phan], Fazly and Ghoussoub proved bounded and stable cases [FG], Li and Zhang proved dimension three, and Huang and Zou stated the version above for all real weights [HZ]. No symmetry, boundedness, integrability, or condition at infinity is assumed.

The proof (lessons 2–5) controls a localized energy by a virial identity for Newton potentials and a one-dimensional comparison along lines, and then rescales. This first lesson collects the potential theory it uses, with proofs: polar coordinates and an identity on annuli (Section 1), spherical means and the Green representation in a ball (Section 2), the fundamental solution and Liouville's theorem for nonnegative harmonic functions (Section 2), and mollification with the representation of a nonnegative supersolution as a constant plus a Newton potential (Section 3).

Throughout, \(n\ge2\) unless stated, \(S\) is the unit sphere of \(\mathbb R^n\), \(\sigma\) its surface measure and \(|S|=\sigma(S)\), \(B_R(z)\) is the open ball of radius \(R\) about \(z\) and \(B_R=B_R(0)\). Integrals without a measure are Lebesgue integrals. For \(n\ge3\) the *Newton kernel* is
\[
K(x)=c_n|x|^{2-n},\qquad c_n=\frac1{(n-2)|S|}.
\]

## 1. Polar coordinates and an identity on annuli

**Fact 1.1** (polar coordinates). For every Borel function \(F\ge0\) on \(\mathbb R^n\), and every integrable \(F\), and every \(z\in\mathbb R^n\),
\[
\int_{\mathbb R^n}F\,dx=\int_0^\infty r^{n-1}\int_SF(z+r\theta)\,d\sigma(\theta)\,dr .
\]
This is proved in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) ([Fremlin, *Measure Theory*, Volume 2, Theorem 265G and Corollary 265H](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm), where the sphere of radius \(r\) carries \(r^{n-1}\) times the measure of \(S\)). Integration by parts on \(\mathbb R^n\) is also used in its simplest form: if \(G\) is a continuously differentiable vector field with compact support, then \(\int\operatorname{div}G\,dx=0\), since each \(\int\partial_iG_i\,dx\) vanishes by Fubini's theorem and the fundamental theorem of calculus in the variable \(x_i\).

For a continuous vector field \(V\) near the sphere of radius \(r\) let
\[
\Phi_V(r)=r^{n-1}\int_SV(r\theta)\cdot\theta\,d\sigma(\theta),
\]
the outward flux of \(V\) through that sphere.

**Lemma 1.2** (annuli). Let \(0<r_1<r_2<\infty\) and let \(V\) be a continuously differentiable vector field on an open set containing \(\{r_1\le|x|\le r_2\}\). Then
\[
\int_{r_1<|x|<r_2}\operatorname{div}V\,dx=\Phi_V(r_2)-\Phi_V(r_1).
\]
If \(V\) is continuously differentiable on \(\{|x|>r_1-\epsilon\}\) for some \(\epsilon>0\) and vanishes outside a bounded set, then \(\int_{|x|>r_1}\operatorname{div}V\,dx=-\Phi_V(r_1)\).

**Proof.** Let \(0<\epsilon<(r_2-r_1)/2\), and let \(\chi\colon\mathbb R\to[0,1]\) be continuously differentiable, equal to \(0\) outside \((r_1,r_2)\) and to \(1\) on \([r_1+\epsilon,r_2-\epsilon]\), nondecreasing on \([r_1,r_1+\epsilon]\) and nonincreasing on \([r_2-\epsilon,r_2]\). The field \(G(x)=\chi(|x|)V(x)\), extended by \(0\), is continuously differentiable with compact support, and \(\operatorname{div}G=\chi(|x|)\operatorname{div}V+\chi'(|x|)V(x)\cdot x/|x|\). Integration by parts and polar coordinates give
\[
\int\chi(|x|)\operatorname{div}V\,dx=-\int_0^\infty\chi'(r)\,\Phi_V(r)\,dr .
\]
As \(\epsilon\to0\), the left side tends to the integral over the annulus by dominated convergence. On the right, \(\chi'\ge0\) on \([r_1,r_1+\epsilon]\) with integral \(1\), \(\chi'\le0\) on \([r_2-\epsilon,r_2]\) with integral \(-1\), and \(\Phi_V\) is continuous; so the right side tends to \(\Phi_V(r_2)-\Phi_V(r_1)\). For the exterior statement use \(\chi\) equal to \(0\) on \((-\infty,r_1]\) and to \(1\) on \([r_1+\epsilon,\infty)\). \(\square\)

## 2. Spherical means

For a function \(w\) continuous on \(\mathbb R^n\setminus\{z\}\) and \(r>0\), the *spherical mean* about \(z\) is
\[
M_zw(r)=\frac1{|S|}\int_Sw(z+r\theta)\,d\sigma(\theta),
\]
and \(\overline w=M_0w\).

**Lemma 2.1** (flux of spherical means). Let \(w\) be twice continuously differentiable on \(\mathbb R^n\setminus\{z\}\). Then \(M_zw\) is continuously differentiable on \((0,\infty)\), and \(r\mapsto r^{n-1}(M_zw)'(r)\) is continuously differentiable with
\[
\bigl(r^{n-1}(M_zw)'(r)\bigr)'=r^{n-1}M_z(\Delta w)(r)\qquad(r>0).
\]

**Proof.** Take \(z=0\). Differentiating under the integral sign, which is legitimate because \(\nabla w\) is continuous, \(\overline w\,'(r)=\frac1{|S|}\int_S\nabla w(r\theta)\cdot\theta\,d\sigma\), so \(|S|\,r^{n-1}\overline w\,'(r)=\Phi_{\nabla w}(r)\), which is continuous in \(r\). By Lemma 1.2 with \(V=\nabla w\) and by polar coordinates,
\[
|S|\bigl(r_2^{n-1}\overline w\,'(r_2)-r_1^{n-1}\overline w\,'(r_1)\bigr)=\int_{r_1<|x|<r_2}\Delta w\,dx=|S|\int_{r_1}^{r_2}r^{n-1}\,\overline{\Delta w}(r)\,dr,
\]
and the integrand on the right is continuous in \(r\). \(\square\)

**Lemma 2.2** (Green representation in a ball). Let \(n\ge3\), let \(w\) be twice continuously differentiable on \(\mathbb R^n\), and let \(z\in\mathbb R^n\) and \(R>0\). Then
\[
w(z)=M_zw(R)+\int_{B_R(z)}G_R(z,y)\,\bigl(-\Delta w(y)\bigr)\,dy,\qquad G_R(z,y)=c_n\bigl(|z-y|^{2-n}-R^{2-n}\bigr).
\]

**Proof.** Let \(F(r)=r^{n-1}(M_zw)'(r)\). Since \(\nabla w\) is bounded near \(z\), \(F(r)\to0\) as \(r\downarrow0\), so Lemma 2.1 and polar coordinates give \(F(r)=\int_0^rs^{n-1}M_z(\Delta w)(s)\,ds=\frac1{|S|}\int_{B_r(z)}\Delta w\,dy\). Since \(M_zw(r)\to w(z)\) as \(r\downarrow0\),
\[
M_zw(R)-w(z)=\int_0^Rr^{1-n}F(r)\,dr=\frac1{|S|}\int_{B_R(z)}\Delta w(y)\int_{|y-z|}^Rr^{1-n}\,dr\,dy=\int_{B_R(z)}G_R(z,y)\,\Delta w(y)\,dy,
\]
where Fubini's theorem applies because \(\Delta w\) is bounded on \(B_R(z)\) and \(\int_0^Rr^{1-n}|B_r|\,dr<\infty\). \(\square\)

**Corollary 2.3** (fundamental solution). Let \(n\ge3\). For every twice continuously differentiable \(\varphi\) with compact support and every \(z\),
\[
\int_{\mathbb R^n}K(y-z)\bigl(-\Delta\varphi(y)\bigr)\,dy=\varphi(z).
\]

**Proof.** Apply Lemma 2.2 with \(R\) so large that the support of \(\varphi\) lies in \(B_R(z)\). Then \(M_z\varphi(R)=0\), and \(\int\Delta\varphi\,dy=0\) by integration by parts, so the term \(c_nR^{2-n}\) of \(G_R\) contributes nothing. \(\square\)

In the language of distributions, \(-\Delta K=\delta_0\).

**Corollary 2.4** (mean values; Liouville). Let \(n\ge3\) and let \(H\) be twice continuously differentiable on \(\mathbb R^n\) with \(\Delta H=0\). Then \(H(z)=M_zH(R)=\frac1{|B_R|}\int_{B_R(z)}H\) for all \(z\) and \(R\). If moreover \(H\ge0\), then \(H\) is constant.

**Proof.** The sphere means come from Lemma 2.2, and the ball mean from polar coordinates and \(|B_R|=R^n|S|/n\). If \(H\ge0\) and \(b=|x-z|\), then \(B_R(x)\subseteq B_{R+b}(z)\), so
\[
H(x)=\frac1{|B_R|}\int_{B_R(x)}H\le\frac1{|B_R|}\int_{B_{R+b}(z)}H=\Bigl(\frac{R+b}R\Bigr)^nH(z).
\]
Letting \(R\to\infty\) gives \(H(x)\le H(z)\), and exchanging \(x\) and \(z\) gives equality. \(\square\)

## 3. Mollification and nonnegative supersolutions

Fix a smooth \(\zeta\ge0\) supported in \(B_1\) with \(\int\zeta=1\), and let \(\zeta_\rho(x)=\rho^{-n}\zeta(x/\rho)\). For a locally integrable \(h\) put \(h_\rho(x)=\int h(y)\zeta_\rho(x-y)\,dy\). We say that \(-\Delta h=g\) *in distributions* on an open set \(\Omega\) if \(\int h(-\Delta\varphi)=\int g\varphi\) for every smooth \(\varphi\) with compact support in \(\Omega\).

**Lemma 3.1.** Let \(h\) be locally integrable.

1. \(h_\rho\) is smooth, and its derivatives are obtained by differentiating \(\zeta_\rho\) under the integral sign.
2. If \(h\) is continuous at \(x\), then \(h_\rho(x)\to h(x)\) as \(\rho\to0\).
3. If \(-\Delta h=g\) in distributions on \(\mathbb R^n\), with \(g\) locally integrable, then \(-\Delta h_\rho=g_\rho\) at every point.
4. If \(h\ge0\), then \(h_\rho\ge0\).

**Proof.** 1. On every ball, the derivatives of \((x,y)\mapsto\zeta_\rho(x-y)\) are bounded and vanish unless \(y\) lies in a fixed larger ball, where \(h\) is integrable; so differentiation under the integral sign is justified by dominated convergence. 2. \(h_\rho(x)-h(x)=\int(h(x-y)-h(x))\zeta_\rho(y)\,dy\), and only \(|y|<\rho\) contributes. 3. By part 1, \(-\Delta h_\rho(x)=\int h(y)\,(-\Delta_y)\bigl[\zeta_\rho(x-y)\bigr]\,dy=\int g(y)\zeta_\rho(x-y)\,dy\), using the test function \(y\mapsto\zeta_\rho(x-y)\). 4 is clear. \(\square\)

**Lemma 3.2** (a removable point). Let \(n\ge3\), let \(h\) be continuous on \(\mathbb R^n\) and twice continuously differentiable on \(\mathbb R^n\setminus\{0\}\), and let \(g\) be locally integrable on \(\mathbb R^n\) with \(-\Delta h=g\) on \(\mathbb R^n\setminus\{0\}\). Then \(-\Delta h=g\) in distributions on \(\mathbb R^n\).

**Proof.** Let \(\varphi\) be smooth with compact support, and let \(\xi\) be smooth, equal to \(1\) on \(B_{1/2}\) and supported in \(B_1\). For \(0<\rho<1\) the function \(\varphi_\rho=\varphi\,(1-\xi(\cdot/\rho))\) is smooth with compact support in \(\mathbb R^n\setminus\{0\}\). Integration by parts, applied to the field \(h\nabla\varphi_\rho-\varphi_\rho\nabla h\), gives \(\int h(-\Delta\varphi_\rho)=\int g\varphi_\rho\). Now
\[
\Delta\varphi_\rho=(1-\xi(\cdot/\rho))\Delta\varphi-\tfrac2\rho\nabla\varphi\cdot(\nabla\xi)(\cdot/\rho)-\tfrac1{\rho^2}\varphi\,(\Delta\xi)(\cdot/\rho),
\]
and \(h\) is bounded near \(0\), so the integrals of \(h\) against the last two terms are \(O(\rho^{n-1})\) and \(O(\rho^{n-2})\), which tend to \(0\) because \(n\ge3\). The remaining terms converge by dominated convergence. \(\square\)

For a locally integrable \(g\ge0\), the *Newton potential* is \(K*g(x)=\int K(x-y)g(y)\,dy\in[0,\infty]\).

**Proposition 3.3** (nonnegative supersolutions). Let \(n\ge3\), let \(u\ge0\) be continuous on \(\mathbb R^n\) and twice continuously differentiable on \(\mathbb R^n\setminus\{0\}\), and let \(g\ge0\) be locally integrable on \(\mathbb R^n\) and continuous on \(\mathbb R^n\setminus\{0\}\), with \(-\Delta u=g\) on \(\mathbb R^n\setminus\{0\}\). Then:

1. \(K*g(x)\le u(x)\) for every \(x\);
2. \(-\Delta(K*g)=g\) in distributions on \(\mathbb R^n\);
3. \(K*g\) is continuously differentiable on \(\mathbb R^n\setminus\{0\}\), with \(\nabla(K*g)(x)=\int\nabla K(x-y)g(y)\,dy\), absolutely convergent, where \(\nabla K(z)=-(n-2)\,z\,K(z)/|z|^2\);
4. there is a constant \(c\ge0\) with \(u=c+K*g\) on \(\mathbb R^n\setminus\{0\}\).

**Proof.** By Lemma 3.2, \(-\Delta u=g\) in distributions on \(\mathbb R^n\).

1. By Lemma 3.1, \(u_\rho\ge0\) is smooth with \(-\Delta u_\rho=g_\rho\ge0\). Lemma 2.2 at the point \(x\) gives \(u_\rho(x)\ge\int_{B_R(x)}G_R(x,y)g_\rho(y)\,dy\), since the sphere mean of \(u_\rho\) is nonnegative. As \(R\to\infty\), the nonnegative functions \(G_R(x,\cdot)\mathbf 1_{B_R(x)}\) increase to \(K(x-\cdot)\), so \(K*g_\rho(x)\le u_\rho(x)\) by monotone convergence. As \(\rho\to0\), \(u_\rho(x)\to u(x)\) and \(g_\rho(y)\to g(y)\) for \(y\neq0\) (Lemma 3.1), and Fatou's lemma gives \(K*g(x)\le u(x)\).

2. For a smooth \(\varphi\) with compact support, \(\int g(y)\int K(x-y)|\Delta\varphi(x)|\,dx\,dy=\int(K*g)|\Delta\varphi|\le\int u|\Delta\varphi|<\infty\) by part 1. So Fubini's theorem and Corollary 2.3 give \(\int(K*g)(-\Delta\varphi)=\int g\varphi\).

3. Fix \(x_0\neq0\), let \(r_0=|x_0|/4\), and let \(\chi\) be continuous with \(0\le\chi\le1\), equal to \(1\) on \(B_{r_0}(x_0)\) and supported in \(B_{2r_0}(x_0)\). Put \(g_1=\chi g\), bounded with compact support, and \(g_2=(1-\chi)g\). For \(|x-x_0|<r_0/2\) and \(g_2(y)\neq0\) we have \(|x-y|\ge|x_0-y|/2\), hence \(K(x-y)\le2^{n-2}K(x_0-y)\) and \(|\nabla K(x-y)|\le C(r_0)K(x_0-y)\); since \(K*g(x_0)<\infty\) by part 1, dominated convergence shows that \(K*g_2\) is continuously differentiable near \(x_0\) with the stated gradient. For \(K*g_1\): for every \(y\) off the segment from \(x\) to \(x+te_i\), \(K(x+te_i-y)-K(x-y)=\int_0^t\partial_iK(x+se_i-y)\,ds\); since \(|\nabla K|\) is locally integrable and \(g_1\) is bounded with compact support, Fubini's theorem gives \(K*g_1(x+te_i)-K*g_1(x)=\int_0^tP_i(x+se_i)\,ds\) with \(P_i=(\partial_iK)*g_1\). The function \(P_i\) is continuous: write \(\partial_iK=k_\epsilon+(\partial_iK-k_\epsilon)\), where \(k_\epsilon=\partial_iK\cdot\theta(|\cdot|/\epsilon)\) for a continuous \(\theta\) vanishing near \(0\) and equal to \(1\) on \([1,\infty)\); then \(k_\epsilon*g_1\) is continuous by dominated convergence, while \(|(\partial_iK-k_\epsilon)*g_1|\le\sup|g_1|\int_{B_\epsilon}|\nabla K|\le C\epsilon\sup|g_1|\). So \(P_i\) is a uniform limit of continuous functions, and \(\partial_i(K*g_1)=P_i\).

4. By parts 1–3, \(h=u-K*g\) is nonnegative, locally integrable, continuous on \(\mathbb R^n\setminus\{0\}\), and \(\int h\,\Delta\varphi=0\) for every test function \(\varphi\). By Lemma 3.1, each \(h_\rho\) is a smooth nonnegative function with \(\Delta h_\rho=0\), hence a constant \(c_\rho\ge0\) by Corollary 2.4. For \(x\neq0\), \(c_\rho=h_\rho(x)\to h(x)\); so the limit \(c=\lim c_\rho\) exists, and \(h=c\) on \(\mathbb R^n\setminus\{0\}\). \(\square\)

## 4. Exercises

**Exercise 4.1** (easy). Show that \(K\) is harmonic on \(\mathbb R^n\setminus\{0\}\) and that \(\Phi_{\nabla K}(r)=-1\) for every \(r>0\). Explain how this agrees with Corollary 2.3.

**Exercise 4.2** (easy). Show that Corollary 2.4 fails without the sign condition: give a nonconstant harmonic function on \(\mathbb R^n\).

**Exercise 4.3** (medium). Let \(n=2\), and let \(w\ge0\) be twice continuously differentiable on \(\mathbb R^2\setminus\{0\}\) with \(\Delta w\le0\). Show that \(r\,\overline w\,'(r)\) is nonincreasing in \(r\), and deduce that \(r\,\overline w\,'(r)\ge0\) for every \(r>0\).

**Exercise 4.4** (medium). Show that the constant \(c\) in Proposition 3.3(4) can be positive: take \(u=1+K*g\) for a smooth \(g\ge0\) with compact support.

## 5. Solutions

**4.1.** Since \(\nabla|x|^{2-n}=(2-n)|x|^{-n}x\), we get \(\Delta|x|^{2-n}=(2-n)\operatorname{div}(|x|^{-n}x)=(2-n)\bigl(n|x|^{-n}-n|x|^{-n}\bigr)=0\). On the sphere of radius \(r\), \(\nabla K\cdot\theta=-(n-2)c_nr^{1-n}\), so \(\Phi_{\nabla K}(r)=-(n-2)c_n|S|=-1\). The total flux \(-1\) through every sphere is the point mass \(-\delta_0\) of \(\Delta K\).

**4.2.** \(H(x)=x_1\).

**4.3.** By Lemma 2.1, which holds for \(n=2\), \((r\,\overline w\,')'=r\,\overline{\Delta w}\le0\), so \(r\,\overline w\,'\) is nonincreasing. If \(s\,\overline w\,'(s)=-\kappa<0\), then \(\overline w\,'(r)\le-\kappa/r\) for \(r\ge s\), and \(\overline w(r)\le\overline w(s)-\kappa\log(r/s)\to-\infty\), contradicting \(w\ge0\).

**4.4.** Write \(K*g(x)=\int K(y)g(x-y)\,dy\). Differentiating under the integral sign, \(K*g\) is smooth with derivatives \(K*\partial^\alpha g\), and \(-\Delta(K*g)(x)=\int K(y)(-\Delta g)(x-y)\,dy=g(x)\) by Corollary 2.3. So \(u=1+K*g\ge0\) satisfies the hypotheses with \(-\Delta u=g\), and \(u-K*g=1\).

## References

- [OpenAI-LE] OpenAI, *The subcritical Hénon–Lane–Emden conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026
- [PQS] P. Poláčik, P. Quittner and Ph. Souplet, *Singularity and decay estimates in superlinear problems via Liouville-type theorems. Part I: Elliptic equations and systems*, Duke Mathematical Journal 139 (2007), 555–579; author's copy. https://www-users.cse.umn.edu/~polacik/Publications/pqs1.pdf
- [LLW] K. Li, M. Li and J. Wei, *On a new region for the Lane–Emden conjecture in higher dimensions*, 2025. https://arxiv.org/abs/2510.06613
- [Phan] Q. H. Phan, *Liouville-type theorems and bounds of solutions for Hardy–Hénon elliptic systems*, Advances in Differential Equations 17 (2012), 605–634. https://arxiv.org/abs/1108.1312
- [FG] M. Fazly and N. Ghoussoub, *On the Hénon–Lane–Emden conjecture*, Discrete and Continuous Dynamical Systems 34 (2014), 2513–2533. https://arxiv.org/abs/1107.5611
- [HZ] L.-H. Huang and W. Zou, *Liouville-type theorems for stable solutions of the Hénon–Lane–Emden system*, Journal of the London Mathematical Society, to appear. https://arxiv.org/abs/2512.16566
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, author's edition. https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
