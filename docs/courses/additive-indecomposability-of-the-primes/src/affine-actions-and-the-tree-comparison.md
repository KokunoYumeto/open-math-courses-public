# Affine actions and the tree comparison

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lesson 12 reduced the tree comparison (Lemma 1.2 of Lesson 12) to local estimates for a single bottom quartet: majorants \(B_\rho(y)\) for the squared Mellin coefficients of the quartet value in a moving coordinate, small for every single character \(\rho\) and summable over all \(\rho\). This lesson constructs them and proves the lemma. The key input is a uniform Mellin estimate (Proposition 1.1). A sum over all multiplicative characters of squared Fourier coefficients of the bottom-pair autocorrelations is small, because it is the norm of an average of the unitary operators \(F(t)\mapsto F(r-r^2t)\), and these affine maps of \(\mathbb F_q\) are spread out: each nonidentity affine map arises in at most two ways. The quartet estimates then split into cases according to which leaves move, and the hardest case is handled by a fourth-moment count of collisions among products \((a-b_1)(a-b_2)\).

**Prerequisites.** [*Diagrams, densities and cycles over a finite field*](diagrams-densities-and-cycles-over-a-finite-field.md).

The notation of Lesson 12 is in force: \(q\), \(U=\mathbb F_q^\times\), \(g\), \(\epsilon_q\), the bottom-pair functions \(h(d,t)\), \(R_*\), the coefficients \(P_\chi(d)\), \(w_\chi(a)=\widehat{P_\chi}(a)\ge0\), \(r_\chi\), and the bounds (4.5) of Lesson 12.

## 1. A uniform Mellin estimate

For a character \(\eta\in\widehat U\) and a function \(P\) on \(\mathbb F_q\), \(P\chi\eta\) denotes the function \(d\mapsto P(d)\chi(d)\eta(d)\), with the value \(0\) at \(d=0\) even when \(\chi\eta\) is principal.

**Proposition 1.1** ([OpenAI-013, (6.14)]). For every \(\eta\in\widehat U\) and \(a\in\mathbb F_q\),
\[
\begin{aligned}
&\sum_{\chi\in\widehat U}\bigl|\widehat{P_\chi\chi\eta}(a)\bigr|^2\\
&\quad \le\frac q{q-1}\bigl(\epsilon_q^4+\sqrt3\,q^{-1/2}\bigr).\quad(1.1)
\end{aligned}
\]

*Proof.* *A Parseval identity.* For \(d\ne0\), \(h(d,t)=\sum_\chi P_\chi(d)\chi(t)\), so \(h(d,\lambda d)=\sum_\chi P_\chi(d)\chi(d)\chi(\lambda)\) for \(\lambda\in U\). Multiplying by \(\eta(d)e_q(-ad)\), averaging over \(d\in\mathbb F_q\), and applying Parseval in \(\lambda\in U\),
\[
\begin{aligned}
&\sum_\chi\bigl|\widehat{P_\chi\chi\eta}(a)\bigr|^2\\
&\quad =\mathbb E_{\lambda\in U}\Bigl|\mathbb E_{d\in\mathbb F_q}h(d,\lambda d)\,\eta(d)\\
&\qquad \,e_q(-ad)\Bigr|^2,\quad(1.2)
\end{aligned}
\]
where arguments with \(d=0\) or \(\lambda d=1\) contribute zero.

*A parametrization.* In the variables of (4.1) of Lesson 12, \(x-z=\sigma d\) and \(x/z=\lambda d\). Solving for \(d\) and \(x\) in terms of \(z\),
\[
d=\frac z{\lambda z-\sigma},\qquad x=\frac{z^2}{z-\sigma/\lambda}.
\]
The map \(z\mapsto d\) is a fractional linear bijection of \(\mathbb P^1(\mathbb F_q)\) sending \(0,\sigma/\lambda,\infty\) to \(0,\infty,1/\lambda\), so \(z\in U\setminus\{\sigma/\lambda\}\) corresponds exactly to the valid \(d\in U\setminus\{1/\lambda\}\). Put \(t=\sigma/\lambda\) and \(r'=1/z\); then \(1/x=r'-tr'^2\). Define
\[
\begin{gathered}
\begin{aligned}
G(r)&=(g_*\eta)(1/r)\\
&\quad \,e_q(-a\sigma/r)\quad(r\in U),
\end{aligned}\\
G(0)=0 .
\end{gathered}
\]
Since \(\eta(d)=\overline{\eta(\lambda)}\eta(x/z)\) and \(e_q(-ad)=e_q(-a\sigma x)e_q(a\sigma z)\), the inner average in (1.2) is
\[
\begin{gathered}
\overline{\eta(\lambda)}\;TG(t),\\
\begin{aligned}
TF(t)&=\frac1q\sum_{r\in U}\overline{G(r)}\,F(r-r^2t).
\end{aligned}\quad(1.3)
\end{gathered}
\]
The excluded value \(z=\sigma/\lambda\), that is \(r=1/t\), gives \(F(0)\), and \(G(0)=0\), so the convention matches. Since inversion permutes \(U\), \(\mathbb E_{\mathbb F_q}|G|^2\le\mathbb E|g|^2\le1\), and by (1.1) of Lesson 12, \(|\mathbb EG|=|\mathbb E_xg_*(x)\eta(x)e_q(-a\sigma x)|\le\epsilon_q\).

*Affine maps.* For \(r\in U\) let \(U_rF(t)=F(r-r^2t)\), a unitary operator on \(L^2(\mathbb F_q)\) with probability measure. Then \(T=\frac1q\sum_r\overline{G(r)}U_r\), and \(U_r^{-1}U_s\) is the operator of composition with
\[
t\longmapsto\Bigl(\frac sr\Bigr)^2t+s-\frac{s^2}r .
\]
For a prescribed slope, \(z=s/r\) has at most two values. If \(z=1\) the map is the identity and \(r=s\). Otherwise \(z\ne0,1\), and the translation \(r(z-z^2)\) determines \(r\). So every nonidentity affine map \(t\mapsto\alpha t+\beta\) has at most two representations as \(U_r^{-1}U_s\). Write \(T^*T=\sum_{\alpha,\beta}c(\alpha,\beta)A_{\alpha,\beta}\), where \(A_{\alpha,\beta}F(t)=F(\alpha t+\beta)\). The identity coefficient is \(q^{-2}\sum_r|G(r)|^2\le1/q\), and Cauchy–Schwarz on the at most two representations of each other map gives
\[
\begin{aligned}
&\sum_{\alpha,\beta}|c(\alpha,\beta)|^2\\
&\quad \le\frac1{q^2}+\frac2{q^4}\Bigl(\sum_{r\in U}|G(r)|^2\Bigr)^2\\
&\quad \le\frac3{q^2}.\quad(1.4)
\end{aligned}
\]

*The operator bound.* The characters \(e_q(\xi t)\), \(\xi\in U\), form an orthonormal basis of the mean-zero subspace, and \(A_{\alpha,\beta}\) sends \(e_q(\xi t)\) to \(e_q(\xi\beta)\,e_q(\alpha\xi t)\). So the squared Hilbert–Schmidt norm of \(T^*T\) on this subspace is
\[
\begin{aligned}
&\sum_{\xi\in U}\sum_{\alpha\in U}\Bigl|\sum_\beta c(\alpha,\beta)e_q(\xi\beta)\Bigr|^2\\
&\quad \le q\sum_{\alpha,\beta}|c(\alpha,\beta)|^2\le\frac3q,
\end{aligned}
\]
by Parseval in \(\beta\). Hence \(\|T^*T\|\le\sqrt3\,q^{-1/2}\) on the mean-zero subspace. Affine maps preserve the constants and the mean-zero subspace, and \(T\mathbf 1=\overline{m_G}\) with \(m_G=\mathbb EG\). Writing \(G=m_G+G_0\) with \(\mathbb EG_0=0\), \(TG=|m_G|^2+TG_0\) with \(TG_0\) of mean zero, so
\[
\begin{aligned}
&\mathbb E_{t\in\mathbb F_q}|TG(t)|^2\\
&\quad =|m_G|^4+\langle T^*TG_0,G_0\rangle\\
&\quad \le\epsilon_q^4+\sqrt3\,q^{-1/2}.
\end{aligned}
\]
Restricting the average to \(t\in U\) costs a factor \(q/(q-1)\), and \(\lambda\mapsto\sigma/\lambda\) permutes \(U\). With (1.2) and (1.3) this proves (1.1). \(\square\)

The estimate is a concrete instance of the mixing of convolutions in groups with large minimal representations studied by Gowers [Gow] and by Babai, Nikolov and Pyber [BNP]; here the group is the affine group of \(\mathbb F_q\), and the bound is computed directly in the additive Fourier basis.

## 2. Quartet majorants: both moving leaves in one pair

Fix a bottom quartet with its product and ancestor data, as in Section 3 of Lesson 12. Let \(d,e\) be the arguments of its two bottom pairs, so \(d-e=y\) by Lemma 1.1 of Lesson 12. In each pair, orient one leaf as *free* and the other as *held*; the pair's value is \(h(d,t)\) of (4.1) of Lesson 12, with \(\sigma\) recording the orientation and \(g_*\) the conjugation of the free leaf, \(t\) being the ratio of the free leaf's argument to the held one's.

Suppose both moving leaves lie in the left pair. At a fixed left-pair product, the ratio of the left pair is a fixed unit times the inverse square of the moving coordinate (Section 2 of Lesson 12). By Lemma 4.2 of Lesson 12, the squared Mellin coefficient at \(\rho\) is at most
\[
2\sum_{\chi^2=\rho^{\pm1}}|P_\chi(d)|^2\times|\text{right-pair value}|^2 ;
\]
the sign in the exponent depends on the coordinate convention, and summing both signs is allowed. Average the two held leaves, which here form the right pair, by first exposing their product and then their split. The first exposure makes \(d/e\) uniform on a coset of the squares, since \(d/e\) is a fixed unit times the square of the right-pair product divided by the quartet product; the second makes the right-pair ratio uniform on a coset of the squares. Dominate both by twice the uniform measure on \(U\) (Lemma 4.2 of Lesson 12), and note that \(d/e\in U\setminus\{1\}\) corresponds bijectively to the pairs \((d,e)\in U^2\) with \(d-e=y\). A majorant is a constant times
\[
\begin{aligned}
B_\rho(y)&=\frac1{q-1}\\
&\quad \sum_{\substack{d,e\in U\\d-e=y}}\Bigl(\sum_{\chi^2=\rho^{\pm1}}|P_\chi(d)|^2\Bigr)\\
&\quad R_*(e).\quad(2.1)
\end{aligned}
\]
Its mean over \(y\in U\) is at most \(\mathbb E_{d\in U}\bigl(\sum_{\chi^2=\rho^{\pm1}}|P_\chi(d)|^2\bigr)\cdot\mathbb E_{e\in U}R_*(e)\), after dropping the restriction \(d\ne e\). Since \(\mathbb E_{d\in U}|P_\chi(d)|^2\le\frac q{q-1}r_\chi\), (4.5) and (4.2) of Lesson 12 give both assertions of (3.3) of Lesson 12: the supremum over \(\rho\) is \(O(\epsilon_q^2)\), and the sum over \(\rho\) is \(O(\sum_\chi r_\chi)=O(1)\), each \(\chi\) occurring for at most two values of \(\rho\).

A quartet off the cycle has the analogous majorant \(B_0(y)=\frac1{q-1}\sum_{d-e=y}R_L(d)R_R(e)\), with the functions \(R_*\) of its two pairs, and so has bounded mean.

## 3. Quartet majorants: one moving leaf in each pair

Label the quartet as follows. Its root has argument \(y\) and current entries \((A,B)\); its left child has argument \(d\) and current entries \((p_*,A)\), and its right child argument \(e\) and current entries \((p_*,B)\), where \(p_*\) is the entry reconstructed at the quartet root. The four leaves carry \(M_1,M_2\) (left pair) and \(M_3,M_4\) (right pair), with the factors \(H\) before the bottom reconstructions equal to
\[
\begin{gathered}
p_*C_1M_1,\\
AC_2M_2,\\
p_*C_3M_3,\\
BC_4M_4 .
\end{gathered}
\]
Here \(A,B\) are fixed local units, unrelated to the summands of the course. Holding \(M_2\) or \(M_4\) uses a residual entry \(A\) or \(B\); holding \(M_1\) or \(M_3\) uses the reconstructed entry \(p_*\).

Orient the moving leaf of each pair as free. Dividing the formulas (1.2) of Lesson 12 gives
\[
\begin{gathered}
\frac{t_L}d=\text{(a fixed unit)}\cdot H_{\mathrm{held},L}^2,\\
\frac{t_R}e=\text{(a fixed unit)}\cdot H_{\mathrm{held},R}^2,\quad(3.1)
\end{gathered}
\]
where \(t_L,t_R\) are the ratios in the two pairs and \(H_{\mathrm{held}}\) is the factor of the held leaf. For instance, if the free leaf is the first leaf of the left pair, the unit is \(D's_{\mathrm{free}}/(s_{\mathrm{held}}s_{\mathrm{pair}})\). At the quartet root, (1.2) of Lesson 12 also gives
\[
p_*^2=\frac{s_+s_-}{s_nD'u_n^2}\cdot\frac y{de}.
\tag{3.2}
\]
If the held factor is \(AC_2M_2\) or \(BC_4M_4\), (3.1) gives the first form below; if it contains \(p_*\), (3.2) gives the second:
\[
\begin{gathered}
t_L=\lambda_Ld\ \ \text{or}\ \ \lambda_L/e,\\
t_R=\lambda_Re\ \ \text{or}\ \ \lambda_R/d .\quad(3.3)
\end{gathered}
\]
Call the first choice on either side *friendly* and the second *bad*. The parameters \(\lambda_L,\lambda_R\) are fixed unit multiples of the squares of the two held leaf variables; the multiples may depend on the parent data and on \(y\), not on the held variables. Given the quartet product and the moving coordinate, the held variables are independent and uniform, so \(\lambda_L,\lambda_R\) are independent and uniform on cosets of the squares.

For fixed held variables, \(d/e\) is a fixed unit times the inverse square of the moving coordinate. The quartet value depends only on \(d/e\): replacing the moving coordinate by its negative changes \(p_*\) to \(-p_*\), but (3.3) uses only \(p_*^2\), and the arguments in each pair are determined by their difference and ratio. Apply Lemma 4.2 of Lesson 12, dominate the laws of \(\lambda_L,\lambda_R\) by independent uniform laws on \(U\) (cost at most \(4\)), and pass from \(d/e\) to the pairs with \(d-e=y\) (cost \(q/(q-1)\)). A majorant is a constant times
\[
\begin{aligned}
B_\rho(y)&=\sum_{\nu^2=\rho^{\pm1}}\mathbb E_{\lambda_L,\lambda_R\in U}\Bigl|\frac1q\\
&\quad \sum_{\substack{d,e\in U\\d-e=y}}h_L(d,t_L)\\
&\quad \,h_R(e,t_R)\,\nu(d/e)\Bigr|^2 .\quad(3.4)
\end{aligned}
\]
Invalid ratios are encoded by the zero conventions of \(h\); in particular \(d/e=1\) has no solution with \(d-e=y\ne0\).

**The sum over \(\rho\).** It suffices to sum over all \(\nu\). For \(y\ne0\), \(t=d/e\) is a bijection from \(U\setminus\{1\}\) onto the unit solutions of \(d-e=y\), with \(d=yt/(t-1)\) and \(e=y/(t-1)\). Mellin Parseval in \(t\), followed by the averages over \(\lambda_L,\lambda_R\), under which \(t_L\) and \(t_R\) are uniform on \(U\) for fixed \(d,e\), bounds the sum by a constant times \(\frac1{q-1}\sum_{d-e=y}R_L(d)R_R(e)\), whose mean over \(y\) is bounded by (4.2) of Lesson 12.

**The supremum over \(\rho\).** Fix \(\nu\). Extend the nonnegative average over \(y\) to all of \(\mathbb F_q\), at a cost \(q/(q-1)\). Expand both \(h\) factors in Mellin characters, \(h_L(d,t)=\sum_\chi P^L_\chi(d)\chi(t)\) and \(h_R(e,t)=\sum_\psi P^R_\psi(e)\psi(t)\). Orthogonality in the independent parameters \(\lambda_L,\lambda_R\) separates the squared coefficients, and the Parseval identity for an additive convolution, \(\mathbb E_y|\frac1q\sum_dA(d)B(d-y)|^2\)\(=\sum_a|\widehat A(a)|^2|\widehat B(-a)|^2\), reduces the mean of (3.4) to
\[
\sum_{a,\chi,\psi}\bigl|\widehat{P_\chi\alpha}(a)\bigr|^2\bigl|\widehat{P_\psi\beta}(-a)\bigr|^2,
\tag{3.5}
\]
where each pair uses its own \(\sigma,g_*\) in its \(P\), and the twists, all zero at zero, are:

| choices | \(\alpha\) (on \(d\)) | \(\beta\) (on \(e\)) |
|---|---|---|
| friendly, friendly | \(\nu\chi\) | \(\overline\nu\psi\) |
| friendly, bad | \(\nu\chi\overline\psi\) | \(\overline\nu\) |
| bad, friendly | \(\nu\) | \(\overline\nu\psi\overline\chi\) |
| bad, bad | \(\nu\overline\psi\) | \(\overline\nu\,\overline\chi\) |

For example, the left friendly term contributes \(\chi(t_L)=\chi(\lambda_L)\chi(d)\), and the left bad term contributes \(\chi(\lambda_L/e)=\chi(\lambda_L)\overline\chi(e)\).

*A friendly side.* If the left choice is friendly, \(\beta\) does not depend on \(\chi\), and \(\alpha=\chi\eta\) with \(\eta=\nu\) or \(\eta=\nu\overline\psi\) independent of \(\chi\). Proposition 1.1 bounds the sum over \(\chi\) of the first factor by \(O(\epsilon_q^4+q^{-1/2})\), uniformly in \(a\) and \(\psi\). The remaining sum is bounded, since by Parseval and \(|\beta|\le1\),
\[
\begin{aligned}
&\sum_{\psi,a}\bigl|\widehat{P_\psi\beta}(a)\bigr|^2\\
&\quad \le\sum_\psi\mathbb E_{e\in\mathbb F_q}|P_\psi(e)|^2=\sum_\psi r_\psi\le3,
\end{aligned}
\]
even when \(\beta\) depends on \(\psi\). So (3.5) is \(O(\epsilon_q^4+q^{-1/2})\). A friendly right side is symmetric.

## 4. The case of two bad choices

It remains to bound (3.5) when \(\alpha=\nu\overline\psi\) and \(\beta=\overline\nu\,\overline\chi\).

**Gauss convolutions.** For a nonprincipal character \(\alpha\) of \(U\), extended by zero, \(\widehat\alpha(0)=0\) and \(|\widehat\alpha(b)|=q^{-1/2}\) for \(b\ne0\). Indeed \(\sum_x\alpha(x)e_q(bx)=\overline\alpha(b)\sum_x\alpha(x)e_q(x)\) for \(b\ne0\), and
\[
\begin{aligned}
&\Bigl|\sum_x\alpha(x)e_q(x)\Bigr|^2\\
&\quad =\sum_{u\in U}\alpha(u)\sum_{z\in U}e_q((u-1)z)\\
&\quad =(q-1)-\sum_{u\ne1}\alpha(u)=q .
\end{aligned}
\]
Since \(\widehat{P_\chi\alpha}=\widehat{P_\chi}*\widehat\alpha\) and \(\widehat{P_\chi}=w_\chi\), up to unit factors and a reflection of the frequency,
\[
\begin{aligned}
&\bigl|\widehat{P_\chi\alpha}(a)\bigr|=q^{-1/2}\Bigl|\\
&\qquad \sum_bw_\chi(b)\,\overline\alpha(a-b)\Bigr| .\quad(4.1)
\end{aligned}
\]

**Lemma 4.1** (a fourth moment [OpenAI-013, (6.24)]). Let \(w\ge0\) be weights on \(\mathbb F_q\) of total mass \(J\), and \(r_w=\sum_bw(b)^2\). Then
\[
\begin{aligned}
&\frac1{q-1}\\
&\qquad \sum_{\alpha\in\widehat U}\sum_{a\in\mathbb F_q}\Bigl|\sum_bw(b)\,\alpha(a-b)\Bigr|^4\\
&\quad \le2qr_w^2+J^4,
\end{aligned}
\]
and the principal character alone contributes at least \(J^4-3J^4/(q-1)\).

*Proof.* Expand the fourth power and average over \(\alpha\): orthogonality leaves the quadruples \((b_1,b_2,b_3,b_4)\) and \(a\) with
\[
(a-b_1)(a-b_2)=(a-b_3)(a-b_4)\ne0,
\]
each with weight \(w(b_1)w(b_2)w(b_3)w(b_4)\). If \(\{b_1,b_2\}=\{b_3,b_4\}\) as multisets, the weight is at most \(2r_w^2\) for each \(a\), and there are \(q\) values of \(a\). Otherwise the two monic quadratic polynomials in \(a\) are different, so their difference is a nonzero polynomial of degree at most \(1\), with at most one root; the total weight of these quadruples is at most \(J^4\). For the principal character, \(\sum_bw(b)\mathbf 1_U(a-b)=J-w(a)\), and \(\frac1{q-1}\sum_a(J-w(a))^4\)\(\ge\frac{qJ^4-4J^3\sum_aw(a)}{q-1}=J^4-\frac{3J^4}{q-1}\). \(\square\)

Apply Lemma 4.1 to \(w=w_\chi\), whose mass \(P_\chi(0)\) is bounded, subtract the principal contribution, and use (4.1):
\[
\begin{aligned}
&\sum_{\alpha\ne1}\sum_a\bigl|\widehat{P_\chi\alpha}(a)\bigr|^4\\
&\quad \le\frac1{q^2}\Bigl(2q(q-1)r_\chi^2+3J^4\Bigr)\\
&\quad \le2r_\chi^2+O(q^{-2}).
\end{aligned}
\]
Summing over \(\chi\) and using (4.5) of Lesson 12,
\[
\begin{aligned}
&\sum_{\chi}\sum_{\alpha\ne1}\sum_a\bigl|\widehat{P_\chi\alpha}(a)\bigr|^4\\
&\quad \ll\epsilon_q^2+q^{-1}.\quad(4.2)
\end{aligned}
\]
When both twists are nonprincipal, Cauchy–Schwarz bounds (3.5) by the geometric mean of two sums of this form: for fixed \(\nu\), \((\chi,\psi)\mapsto(\chi,\nu\overline\psi)\) is a bijection, and likewise for the other factor.

**Principal twists.** Since the principal character \(\mathbf 1_U\) is zero at zero, \(\widehat{P_\chi\mathbf 1_U}(a)=w_\chi(a)-P_\chi(0)/q\); its maximum over \(a\) is \(O(\epsilon_q^2+q^{-1})\), and its squared Fourier norm is at most \(r_\chi\). If \(\alpha\) is principal, then \(\psi=\nu\) is fixed. If moreover \(\beta\) is nonprincipal, (4.1) and the bounded mass of \(w_\psi\) bound the second factor by \(O(q^{-1})\) uniformly, and the sum of the first factor over \(\chi,a\) is \(O(1)\); this part is \(O(q^{-1})\). The case with the roles exchanged is the same. If both twists are principal, both indices are fixed; the small Fourier maximum on one factor and the bounded squared norm on the other give \(O(\epsilon_q^4+q^{-2})\).

So the two-bad case of (3.5) is \(O(\epsilon_q^2+q^{-1})\). With the friendly cases and Section 2, this proves (3.3) of Lesson 12, with
\[
\begin{gathered}
\sup_\rho\mathbb E_yB_\rho(y)\ll\epsilon_q^2+q^{-1/2},\\
\sum_\rho\mathbb E_yB_\rho(y)\ll1,
\end{gathered}
\]
after adding the finitely many majorants for the orientation and conjugation choices.

## 5. Completion of the tree comparison

Return to the projection \(\mathcal P\) of Section 3 of Lesson 12, conditioning on the products of all bottom quartets. Orthogonality in the independent moving coordinates expresses \(\|\mathcal PW_1\|_2^2\) as the expectation of a sum, over the tuples \((\rho_j)\) satisfying (3.2) of Lesson 12, of \(\prod_j|a_{j,\rho_j}|^2\) times the squared values of the quartets off the cycle. Averaging the held variables, this is at most
\[
\sum_{\prod_j\rho_j^{\delta_j}=1}\ \prod_{j=1}^tB_{\rho_j}(y_j)\prod_{j\notin\text{cycle}}B_0(y_j).
\]
On valid ancestor points, the joint law of the quartet arguments \(y_j\) is at most a constant depending only on \(l\) times the independent uniform law on \(U\) (Proposition 2.1 of Lesson 12, at level \(2\)). Since the last display is nonnegative, this domination applies without any pointwise control of \(g\). Put \(b_\rho=\mathbb E_{y\in U}B_\rho(y)\) and \(b_0=\mathbb E_{y\in U}B_0(y)\). In the relation (3.2) of Lesson 12 one character is determined by the others, so
\[
\begin{aligned}
\|\mathcal PW_1\|_2^2&\le C_l\Bigl(\sup_\rho b_\rho\Bigr)\Bigl(\sum_\rho b_\rho\Bigr)^{t-1}\\
&\quad b_0^{\,r/4-t}\ll_l\epsilon_q^2+q^{-1/2}.
\end{aligned}
\]
If the cycle is a pair of parallel edges, \(t=1\) and the only character is principal; the same inequality holds with \(b_{\mathbf 1}\le\sup_\rho b_\rho\). By Proposition 3.1 of Lesson 12,
\[
\begin{aligned}
\bigl|\mathbb E\,W_1\overline{W_2}\bigr|&\le3^{r/2}\|\mathcal PW_1\|_2\\
&\ll_l\epsilon_q+q^{-1/4},
\end{aligned}
\]
which proves Lemma 1.2 of Lesson 12. \(\square\)

**Application.** The normalized transforms \(g_p\) of the residue supports satisfy \(g_p(0)=0\) and \(\mathbb E|g_p|^2=1\), and by Theorem 6.1 of Lesson 9 their correlation parameters \(\epsilon_p\) tend to zero uniformly on a set of primes of nearly full harmonic mass in every band. Lesson 17 applies Lemma 1.2 of Lesson 12 at every *spectator* prime, once the bulk variables have been replaced by independent uniform units; the zero convention of the diagrams retains the requirement that every reconstructed entry be a unit at that prime.

## 6. Exercises

**6.1.** Show directly that the operators \(U_r\), \(r\in U\), are unitary on \(L^2(\mathbb F_q)\) and that \(U_r^{-1}U_s\) is composition with \(t\mapsto(s/r)^2t+s-s^2/r\).

**6.2.** For \(q=7\), list the representations of the affine map \(t\mapsto4t+3\) as \(U_r^{-1}U_s\).

**6.3.** In Lemma 4.1, check that two monic quadratics \((a-b_1)(a-b_2)\) and \((a-b_3)(a-b_4)\) coincide as polynomials exactly when \(\{b_1,b_2\}=\{b_3,b_4\}\).

**6.4.** Verify the convolution Parseval identity \(\mathbb E_y\bigl|\frac1q\sum_dA(d)B(d-y)\bigr|^2\)\(=\sum_a|\widehat A(a)|^2|\widehat B(-a)|^2\).

## 7. Solutions

**6.1.** For \(r\in U\), \(t\mapsto r-r^2t\) is a bijection of \(\mathbb F_q\), so composition with it preserves the uniform measure and is unitary. With \(\phi_r(t)=r-r^2t\), \(U_rF=F\circ\phi_r\) and \(U_r^{-1}F=F\circ\phi_r^{-1}\), \(\phi_r^{-1}(t)=(r-t)/r^2\). Then \(U_r^{-1}U_sF=F\circ\phi_s\circ\phi_r^{-1}\), and \(\phi_s(\phi_r^{-1}(t))=s-s^2(r-t)/r^2\)\(=(s/r)^2t+s-s^2/r\).

**6.2.** The slope \(4=(s/r)^2\) gives \(z=s/r\in\{2,5\}\) in \(\mathbb F_7\). The translation is \(r(z-z^2)\). For \(z=2\): \(z-z^2=-2=5\), so \(5r=3\), \(r=3\cdot3=9=2\) (since \(5^{-1}=3\)), \(s=4\). For \(z=5\): \(z-z^2=5-25=-20=1\), so \(r=3\), \(s=15=1\). Check: \(r=2,s=4\): \(t\mapsto4t+4-16/2=4t-4=4t+3\). \(r=3,s=1\): \(t\mapsto t/9+1-1/3\); with \(9=2\), \(1/2=4\), \(1/3=5\): \(4t+1-5=4t-4=4t+3\). Two representations.

**6.3.** The polynomials are \(a^2-(b_1+b_2)a+b_1b_2\) and \(a^2-(b_3+b_4)a+b_3b_4\). They coincide iff the sums and products agree, iff \(b_1,b_2\) and \(b_3,b_4\) are the roots of the same quadratic, iff the multisets agree.

**6.4.** Expand \(A=\sum_a\widehat A(a)e_q(a\cdot)\) and \(B=\sum_b\widehat B(b)e_q(b\cdot)\). Then \(\frac1q\sum_dA(d)B(d-y)=\sum_{a,b}\widehat A(a)\)\(\widehat B(b)e_q(-by)\,\mathbb E_de_q((a+b)d)\)\(=\sum_a\widehat A(a)\widehat B(-a)e_q(ay)\), and Parseval in \(y\) gives the claim.

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 6: a uniform Mellin estimate (6.14), quartet coefficient majorants, the case of two bad choices, and completion of the cycle estimate. https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
- [Gow] W. T. Gowers, *Quasirandom groups*, Combin. Probab. Comput. 17 (2008), 363–387; numbering of arXiv:0710.3877v1. https://arxiv.org/abs/0710.3877v1
- [BNP] L. Babai, N. Nikolov and L. Pyber, *Product growth and mixing in finite groups*, Proceedings of the Nineteenth Annual ACM–SIAM Symposium on Discrete Algorithms (2008), 248–257. https://people.cs.uchicago.edu/~laci/papers/bnp-soda08.pdf
