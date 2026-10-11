# When pointwise norm continuity becomes uniform

**Reading goal.** Show why a real automorphism group on a von Neumann algebra cannot be norm continuous on every element while retaining large errors on its unit ball.

The main obstruction is an orthogonal family of projections. Phillips's lemma detects errors that move along that family; a finite-cover argument then controls an entire central summand from one small corner. The estimates are independent of the number of covering pieces.

The uniformity argument below follows the programme proof in OA-FLOW, *Multiplier uniformity, analytic measures and positive energy*. The uniform-flow argument is from its *Derivations and flow domains*. Phillips's lemma and the projection structure arguments are from the foundations programme. Those courses retain ownership of their reproduced CC0 proofs. The small-logarithm argument and the connections below are additional OA-MOD exposition. Mathematical context: Masamichi Takesaki, *Theory of Operator Algebras II*, VIII.2, p. 98, and Exercise XI.3(6), p. 361.

## Two continuity conditions and the conclusion

Let \(M\) be an arbitrary von Neumann algebra and let \(\alpha:\mathbb R\to\operatorname{Aut}(M)\) be a group homomorphism. If \(M=0\), the assertions are immediate. Otherwise all automorphisms are unital isometries. Suppose

\[
 \|\alpha_t(x)-x\|\longrightarrow0\quad(t\longrightarrow0,\ x\in M).
\]

We will prove operator-norm continuity of the maps themselves and construct a bounded self-adjoint \(h\in M\) such that

\[
 \alpha_t(x)=e^{ith}xe^{-ith}\qquad(t\in\mathbb R,\ x\in M).
\]

There is no factor, separability, sigma-finiteness or faithful-state assumption. The hypothesis concerns the operator norm of every orbit, and is stronger than pointwise ultraweak continuity.

We use the earlier written bounded-innerness proof and concrete spectral calculus. The full programme projection and type proofs supply Theorem 10.3 and Propositions 13.3–13.4 with Corollary 13.5, at arbitrary cardinality. The only small-automorphism result needed is proved next.

## A logarithm that satisfies the product rule

Let \(A\) be a complex Banach algebra and \(\alpha\) a bounded algebra automorphism with \(c=\|\alpha-I\|<1/4\). Put
\[
 D=\sum_{n\ge1}\frac{(-1)^{n+1}}n(\alpha-I)^n.
\]
The series is absolutely convergent in the Banach algebra of bounded linear maps on \(A\). Its norm satisfies
\[
 \|D\|\le-\log(1-c)\le\frac{c}{1-c}<\frac13,
 \qquad \|D\|\le 2c.
\]
The scalar logarithm and exponential power-series identity, with absolutely convergent substitution in this one-element Banach subalgebra, gives \(e^D=\alpha\). If \(A\) is a Banach star algebra with isometric involution and \(\alpha\) preserves star, each term in the real-coefficient logarithm series preserves star, and so does \(D\).

To prove the Leibniz rule, let \(\mathcal B\) be the Banach space of bounded complex bilinear maps \(A\times A\to A\), with norm \(\|b\|=\sup_{\|x\|,\|y\|\le1}\|b(x,y)\|\). Completeness follows by taking the uniform limit on the product of the two unit balls of a Cauchy sequence, then extending by bilinearity; the uniform norm bound passes to the limit. Multiplication \(m(x,y)=xy\) belongs to \(\mathcal B\).

On \(\mathcal B\), define three commuting bounded operators
\[
 \begin{aligned}
 (L b)(x,y)&=D(b(x,y)),\\
 (R_1 b)(x,y)&=b(Dx,y),\\
 (R_2 b)(x,y)&=b(x,Dy).
 \end{aligned}
\]
Their norms are at most \(\|D\|\). Set \(Q=L-R_1-R_2\), so \(\|Q\|<1\). The binomial identity for commuting bounded operators and absolute convergence of their exponential series give
\[
 (e^Qb)(x,y)=e^D b(e^{-D}x,e^{-D}y).
\]
For \(b=m\), multiplicativity of \(\alpha=e^D\) makes the right side equal \(xy\). Thus \((e^Q-I)m=0\).

Define
\[
 G=\sum_{n\ge0}\frac{Q^n}{(n+1)!}.
\]
Then \(QG=GQ=e^Q-I\), and
\[
 \|G-I\|\le\sum_{n\ge1}\frac{\|Q\|^n}{(n+1)!}
 \le\sum_{n\ge1}\frac1{(n+1)!}=e-2<1.
\]
The last strict inequality follows directly from the exponential series: \(1/k!\le 1/2^{k-1}\) for \(k\ge2\), with strict inequality for \(k\ge3\), so \(e<3\). The Neumann series makes \(G\) invertible. Therefore \(Qm=0\), which is precisely
\[
 D(xy)=D(x)y+xD(y).
\]
Hence the logarithm is a bounded derivation, and is a star derivation when \(\alpha\) preserves star.

For a von Neumann algebra, the bounded-innerness theorem gives \(D=i[h,\cdot]\) with self-adjoint \(h\) and \(\|h\|\le\|D\|\). The commuting left-right exponential calculation yields \(\alpha=\operatorname{Ad}(e^{ih})\). Spectral calculus gives \(\|e^{ih}-1\|\le\|h\|\le2c\).

## Phillips's lemma detects moving coordinates

For a set \(\Gamma\), a bounded functional \(\mu\) on \(\ell^\infty(\Gamma)\) is a finitely additive set function \(E\mapsto\mu(E)=\mu(1_E)\). The next lemma says that if such functionals tend to zero on every set, their parts on points tend to zero in \(\ell^1\)-norm. We will apply it to normal or nonnormal functionals obtained from projection errors.

**Phillips's lemma.** Let \((\mu_n)\) be a bounded sequence in \(\ell^\infty(\Gamma)^*\) with \(\mu_n(E)\to0\) for every \(E\subseteq\Gamma\). Then
\[
\sum_{\gamma\in\Gamma}|\mu_n(\{\gamma\})|\to0 .
\]

**Proof.** For \(\mu\in\ell^\infty(\Gamma)^*\) and \(E\subseteq\Gamma\) put

\[
 \begin{aligned}
 |\mu|(E)&=\sup\{|\mu(x)|:\\
 &\quad\|x\|\le1,\ x=0\text{ off }E\}.
 \end{aligned}
\]

Three facts:

- (a) If \(E_1,\dots,E_m\) are disjoint, \(\sum_j|\mu|(E_j)\le\|\mu\|\). Choose \(x_j\) supported in \(E_j\) with \(\|x_j\|\le1\) and \(\mu(x_j)\ge|\mu|(E_j)-\varepsilon\); then \(x=\sum_jx_j\) has \(\|x\|\le1\).
- (b) \(\sum_{\gamma\in E}|\mu(\{\gamma\})|\le|\mu|(E)\), by testing on \(\sum_{\gamma\in F}\overline{\operatorname{sgn}\mu(\{\gamma\})}\,1_{\{\gamma\}}\) for finite \(F\subseteq E\). In particular \(a_\mu(\gamma)=\mu(\{\gamma\})\) defines \(a_\mu\in\ell^1(\Gamma)\).
- (c) For finite \(F\) and any \(x\), \(\mu(x1_F)=\sum_{\gamma\in F}x(\gamma)\mu(\{\gamma\})\), by finite additivity.

Let \(c=\sup_n\|\mu_n\|\) and \(a_n=a_{\mu_n}\). Suppose the lemma fails. Passing to a subsequence, which keeps the hypotheses, we may assume \(\|a_n\|_1\ge5\varepsilon\) for all \(n\), for some \(\varepsilon>0\). By hypothesis \(a_n(\gamma)\to0\) for each \(\gamma\), so \(\sum_{\gamma\in D}|a_n(\gamma)|\to0\) for every finite \(D\).

*Humps.* Choose indices \(m_1<m_2<\cdots\) and disjoint finite sets \(E_1,E_2,\dots\) as follows. Given \(E_1,\dots,E_{k-1}\), with union \(D\), choose \(m_k>m_{k-1}\) with \(\sum_{\gamma\in D}|a_{m_k}(\gamma)|<\varepsilon/2\); then \(\sum_{\gamma\notin D}|a_{m_k}(\gamma)|>4\varepsilon\), so there is a finite \(E_k\) disjoint from \(D\) with \(\sum_{\gamma\in E_k}|a_{m_k}(\gamma)|\ge4\varepsilon\).

*Thinning.* Fix an integer \(p>c/\varepsilon\). If \(L\) is an infinite set of indices and \(\mu\) a functional, split \(L\) into \(p\) disjoint infinite sets \(L_1,\dots,L_p\). The sets \(\bigcup_{l\in L_r}E_l\) are disjoint, so by (a) some \(r\) has \(|\mu|(\bigcup_{l\in L_r}E_l)\le c/p<\varepsilon\). Starting from \(L_0=\mathbb N\), define \(k_j=\min L_{j-1}\) and apply this to \(\mu=\mu_{m_{k_j}}\) and \(L=L_{j-1}\setminus\{k_j\}\), to get an infinite \(L_j\subseteq L_{j-1}\setminus\{k_j\}\) with \(|\mu_{m_{k_j}}|\big(\bigcup_{l\in L_j}E_l\big)<\varepsilon\). Then \(k_1<k_2<\cdots\), and \(k_i\in L_j\) for \(i>j\).

*Test function.* Let \(\nu_j=\mu_{m_{k_j}}\) and define \(x\in\ell^\infty(\Gamma)\) by \(x(\gamma)=\overline{\operatorname{sgn}a_{m_{k_i}}(\gamma)}\) for \(\gamma\in E_{k_i}\), \(i\ge1\), and \(x=0\) elsewhere; \(\|x\|\le1\). Fix \(j\) and split \(x=x1_{P}+x1_{E_{k_j}}+x1_{T}\), where \(P=\bigcup_{i<j}E_{k_i}\) and \(T=\bigcup_{i>j}E_{k_i}\). By (c) and the choice of \(m_{k_j}\) (the set \(P\) lies in the \(D\) used at that step), \(|\nu_j(x1_P)|<\varepsilon/2\). By (c), \(\nu_j(x1_{E_{k_j}})=\sum_{\gamma\in E_{k_j}}|a_{m_{k_j}}(\gamma)|\ge4\varepsilon\). And \(T\subseteq\bigcup_{l\in L_j}E_l\), so \(|\nu_j(x1_T)|\le|\nu_j|(T)<\varepsilon\). Hence \(|\nu_j(x)|>2\varepsilon\) for every \(j\).

*Contradiction.* The function \(x\) is a uniform limit of finite linear combinations of indicator functions (cut the unit disc into finitely many small pieces). Each \(\nu_j(1_E)\to0\) and \(\sup_j\|\nu_j\|\le c\), so \(\nu_j(x)\to0\). \(\square\)

## Orthogonal projections and corners

Let \(\beta_n\) be automorphisms of \(M\) such that \(\|\beta_n(x)-x\|\to0\) for every \(x\in M\). We prove

\[
 \|\beta_n-I\|\longrightarrow0.
 \tag{UW.1}
\]

Write \(T_n=\beta_n-\operatorname{id}_M\). Then \(\|T_n\|\le2\). Suppose \((f_j)\) is an orthogonal sequence of projections and \(n_j\) increases to infinity. We claim

\[\|T_{n_j}(f_j)\|\longrightarrow0. \tag{UW.2}\]

Otherwise pass to a subsequence for which these norms exceed some \(\varepsilon>0\). Choose functionals \(\omega_j\in M^*\) with \(\|\omega_j\|\le1\) and

\[|\omega_j(T_{n_j}(f_j))|>\varepsilon/2.\]

For a bounded scalar sequence \(a\), the strong sum \(\rho(a)=\sum_j a_jf_j\) exists and defines a contractive star homomorphism \(\ell^\infty(\mathbb N)\to M\). To see existence, the orthogonal subspaces \(f_jK\) give a bounded diagonal operator of norm at most \(\sup_j|a_j|\) on their sum, extended by zero on its orthogonal complement; finite partial sums converge strongly to this operator, so it belongs to \(M\). Define

\[\mu_j(a)=\omega_j(T_{n_j}(\rho(a))).\]

These functionals have norm at most two. For every subset \(E\subseteq\mathbb N\), \(\rho(1_E)\) is one fixed projection in \(M\), and point-norm convergence gives \(\mu_j(1_E)\to0\). Phillips's lemma therefore gives \(\sum_i|\mu_j(1_{\{i\}})|\to0\). Its \(i=j\) term is greater than \(\varepsilon/2\), a contradiction. This proves (UW.2). The functionals need not be normal: no interchange of a functional with an infinite projection sum was used.

There is also a uniform consequence for orthogonal *corners*. If \((p_k)\) is an orthogonal sequence, put

\[d_k=\limsup_{n\to\infty}\|T_n|_{p_kMp_k}\|. \tag{UW.3}\]

Then \(d_k\to0\). Indeed a bounded linear map \(T\) on a von Neumann corner satisfies

\[\|T\|\le4\sup\{\|T(e)\|:e\text{ is a projection in the corner}\}. \tag{UW.4}\]

For a positive contraction \(x\), its spectral step approximants are positive combinations of spectral projections with coefficient sum at most one: for example \(m^{-1}\sum_{j=1}^{m}1_{[j/m,1]}(x)\) differs from \(x\) by at most \(1/m\). Thus the projection supremum bounds \(\|T(x)\|\). Split a selfadjoint contraction into its positive and negative parts, and then split an arbitrary contraction into its real and imaginary parts, to obtain the factor four. If \(d_k\not\to0\), choose distinct increasing \(k_j\) with \(d_{k_j}\ge\varepsilon\), increasing \(n_j\), and projections \(f_j\le p_{k_j}\) with \(\|T_{n_j}(f_j)\|>\varepsilon/8\), using (UW.4). These \(f_j\) are orthogonal, contradicting (UW.2).

## The centre is eventually fixed

First consider an abelian von Neumann algebra \(B\) and point-norm convergent automorphisms \(\gamma_n\to\operatorname{id}_B\). For each projection \(r\), \(\gamma_n(r)=r\) eventually: distinct commuting projections have distance one. We show that \(\gamma_n\) is the identity on all of \(B\) eventually.

Suppose it is not. Starting with \(r_0=1\), maintain a projection \(r_j\) on whose corner infinitely many \(\gamma_n\) act nontrivially. Choose \(n_j\) greater than the preceding indices, with \(\gamma_{n_j}(r_{j-1})=r_{j-1}\) and nontrivial action on \(r_{j-1}B\). Since spectral step functions span that corner densely, choose \(e\le r_{j-1}\) with \(\gamma_{n_j}(e)\ne e\). The complementary projection \(r_{j-1}-e\) is also changed by \(\gamma_{n_j}\).

For sufficiently large \(n\), both \(e\) and \(r_{j-1}-e\) are fixed. At least one of their corners still has nontrivial action for infinitely many \(n\); otherwise the action on \(r_{j-1}B\), the direct sum of these two corners, would eventually be the identity. Retain such a corner as \(r_j\) and denote the discarded projection by \(f_j\). Then \((f_j)\) is orthogonal and \(\|\gamma_{n_j}(f_j)-f_j\|=1\). Applying (UW.2), whose proof only required point-norm convergence and boundedness, gives a contradiction.

Apply this result to \(B=Z(M)\) and \(\gamma_n=\beta_n|_{Z(M)}\). After discarding finitely many indices we may therefore assume

\[\beta_n(z)=z\qquad(z\in Z(M),\ n\ge1). \tag{UW.5}\]

In particular all the central summands used next are invariant. No faithful normal state or countability condition on the centre is required.

## A corner estimate independent of the cover size

Let \(p\le q\) be projections, with \(q\) central, and suppose that \(q\) is a finite sum of orthogonal projections \(q_i=v_iv_i^*\), where

\[v_i^*v_i=a_i\le p. \tag{UW.6}\]

The number of \(v_i\) is fixed in this paragraph. Assume (UW.5) and put \(d=\limsup_n\|T_n|_{pMp}\|\). We prove

\[d<\tfrac14\quad\Longrightarrow\quad
\limsup_n\|T_n|_{qMq}\|\le4d. \tag{UW.7}\]

The constant does not depend on the number of covering projections. This independence is needed when the matrix sizes are unbounded.

If \(p=0\), (UW.6) forces \(q=0\) and the assertion is immediate. Assume \(p\ne0\) in the construction that follows.

Because \(\beta_n(p)\to p\) in norm, put

\[b_n=\beta_n(p)p+(q-\beta_n(p))(q-p)\in qMq.\]

It satisfies \(\|b_n-q\|=\|\beta_n(p)-p\|\to0\) and \(b_np=\beta_n(p)b_n\). For large \(n\), \(b_n\) is invertible in \(qMq\). Its polar unitary \(s_n=b_n(b_n^*b_n)^{-1/2}\) tends to \(q\) in norm, by continuous functional calculus. Moreover \(b_n^*b_n\) commutes with \(p\), so \(s_nps_n^*=\beta_n(p)\). Extend \(s_n\) by \(1-q\) and set

\[\eta_n=\operatorname{Ad}(s_n^*+1-q)\circ\beta_n.\]

Then \(\eta_n(p)=p\), \(\eta_n(q)=q\), and \(\|\eta_n-\beta_n\|\to0\). The restriction \(\eta_n|_{pMp}\) is an automorphism and has norm distance \(c_n\) from the identity with \(\limsup_n c_n=d\).

Since \(d<1/4\), eventually \(c_n<1/4\). The small-logarithm proof above applies to \(\eta_n|_{pMp}\) and makes its logarithm a bounded star derivation. The norm-convergent series for the logarithm gives

\[
\|\operatorname{Log}(\eta_n|_{pMp})\|
\le\sum_{j\ge1}\frac{c_n^j}{j}
=-\log(1-c_n)\le2c_n.
\tag{UW.8}
\]

Bounded innerness, including its normalized implementer bound, supplies \(h_n=h_n^*\in pMp\) of norm at most \(2c_n\) with this derivation equal to \(i[h_n,\cdot]\). Hence \(w_n=e^{ih_n}\) implements \(\eta_n\) on \(pMp\) and \(\|w_n-p\|\le2c_n\). The exponential is taken in the corner with unit \(p\).

Define

\[u_n=\sum_i\eta_n(v_i)w_nv_i^*\in qMq. \tag{UW.9}\]

The final projections \(\eta_n(q_i)\) are orthogonal, as are the \(q_i\). Since \(\eta_n(a_i)=w_na_iw_n^*\), multiplication gives

\[u_n^*u_n=\sum_i v_iw_n^*\eta_n(a_i)w_nv_i^*=q,
\qquad
u_nu_n^*=\sum_i\eta_n(q_i)=q.\]

For \(x\in qMq\), expand \(x=\sum_{i,j}v_i(v_i^*xv_j)v_j^*\). The middle entries lie in \(a_iMa_j\subset pMp\). Applying \(\operatorname{Ad}u_n\) to this expansion shows that it equals \(\eta_n(x)\), because \(w_n\) implements \(\eta_n\) on every middle entry. Thus \(u_n\) implements \(\eta_n\) throughout \(qMq\).

Finally,

\[u_n-q
=\sum_i(\eta_n(v_i)-v_i)w_nv_i^*
+\sum_i v_i(w_n-p)v_i^*. \tag{UW.10}\]

The first sum tends to zero in norm: it is finite, the \(v_i\) are fixed, and \(\eta_n(v_i)\to v_i\). The second sum is block diagonal on the mutually orthogonal \(q_i\), and every block has norm at most \(\|w_n-p\|\). Its norm is therefore at most \(2c_n\), with no factor equal to the number of blocks. The elementary bound \(\|\operatorname{Ad}u_n-\operatorname{id}\|\le2\|u_n-q\|\), followed by \(\|\eta_n-\beta_n\|\to0\), proves (UW.7).

The small-automorphism and bounded-derivation theorems used here do not assume the point-norm upgrade being proved: the former starts from an operator-norm inequality, and the latter starts from an already bounded derivation and its norm-continuous exponential. Thus the argument is not circular.

## Cover the large matrix summands and pass to uniformity

Use Theorem 10.3 of the preceding programme projection lesson to write \(M\) as the central sum of its part \(M_c\) with no type I summand, its properly infinite type I part \(M_\infty\), and its finite homogeneous parts

\[M_m\cong M_m(Z_m),\qquad m=1,2,\ldots, \tag{UW.11}\]

where \(Z_m\) is abelian and zero summands are allowed. Write their central units as \(z_c,z_\infty,z_m\).

In \(M_c\), repeatedly halve the unused projection using Proposition 13.3. This gives orthogonal \(p_k^c\), \(k\ge1\), such that \(z_c\) is the sum of \(2^k\) projections equivalent to \(p_k^c\): after the \(k\)th halving, its two equal halves can be transported into each of the \(2^{k-1}\) equal pieces obtained at the preceding stage. In \(M_\infty\), Corollary 13.5, division of the properly infinite unit by \(\aleph_0\), gives orthogonal \(p_k^\infty\sim z_\infty\).

In \(M_m(Z_m)\) choose fixed standard matrix units. For \(k\ge1\) set \(N_k=2^{k+1}\) and let \(p_k^{(m)}\) be a diagonal projection of rank

\[r_k(m)=\lfloor m/N_k\rfloor.\]

Choose its diagonal slots just after all the slots used at earlier stages. This is possible because \(\sum_{k\ge1}r_k(m)\le m/2\). These projections are orthogonal as \(k\) varies. If \(m\ge N_k\), then \(r_k(m)\ge m/(2N_k)\), so the \(m\) diagonal slots can be partitioned into at most \(2N_k\) groups of size at most \(r_k(m)\). Each group's projection is equivalent, by a fixed matrix partial isometry, to a subprojection of \(p_k^{(m)}\).

Now form the strong central sums

\[
p_k=p_k^c+p_k^\infty+\sum_{m\ge N_k}p_k^{(m)},
\qquad
q_k=z_c+z_\infty+\sum_{m\ge N_k}z_m.
\tag{UW.12}
\]

The \(p_k\) are orthogonal. For each fixed \(k\), \(q_k\) is a sum of at most \(2N_k\) orthogonal projections equivalent to subprojections of \(p_k\). To assemble the partial isometries, pad the finite lists on each central summand by zeros and take their strong sums across the orthogonal central units. These sums are bounded by one, their initial and final projections are the corresponding strong sums, and they belong to \(M\). Thus (UW.6) holds exactly, even with arbitrary multiplicities and a non-countably decomposable \(M\).

### Completing the sequential theorem and the flow implication

Let \(d_k\) be (UW.3) for these \(p_k\). We proved \(d_k\to0\). For every sufficiently large \(k\), (UW.7) gives

\[\limsup_n\|T_n|_{q_kMq_k}\|\le4d_k. \tag{UW.13}\]

The complementary algebra has only finitely many finite homogeneous sizes \(m<N_k\). On each of them, (UW.5) makes \(\beta_n\) linear over \(Z_m\). Writing \(x=\sum_{i,j}a_{ij}E_{ij}\) with \(a_{ij}\in Z_m\) and \(\|a_{ij}\|\le\|x\|\) gives

\[\|T_n|_{M_m(Z_m)}\|
\le m^2\max_{i,j}\|\beta_n(E_{ij})-E_{ij}\|
\longrightarrow0. \tag{UW.14}\]

There are finitely many such summands, so \(\|T_n|_{(1-q_k)M}\|\to0\). Since \(q_k\) is central and fixed, \(T_n\) preserves the two central blocks and its norm is the maximum of the two restricted norms. Consequently \(\limsup_n\|T_n\|\le4d_k\) for every sufficiently large \(k\). Letting \(k\to\infty\) proves the sequential assertion \(\|\beta_n-I\|\to0\). If \(M\) has only bounded finite homogeneous sizes, the same conclusion follows directly from (UW.14); zero \(p_k\) and \(q_k\) present no exception.

For the real flow, failure of operator-norm continuity would give \(\varepsilon>0\) and a sequence \(t_n\to0\) with \(\|\alpha_{t_n}-\operatorname{id}_M\|\ge\varepsilon\). The pointwise norm-continuity hypothesis says that the automorphisms \(\beta_n=\alpha_{t_n}\) converge pointwise in norm. Applying the sequential assertion is a contradiction. We have therefore proved

\[
\bigl[\ \forall x\in M,\ \|\alpha_t(x)-x\|\to0\ \bigr]
\quad\Longrightarrow\quad
\|\alpha_t-\operatorname{id}_M\|\to0. \tag{UW.15}
\]

This is a sequential argument for the first-countable real parameter. It introduces no factor, separability, sigma-finiteness or faithful-state hypothesis. The uniform boundedness principle alone would only bound the already isometric \(\alpha_t\); the orthogonal-projection and cover-independent estimates supply the decay.

## Recover a bounded internal generator

**Uniform-flow theorem.** Bounded star derivations on a C*-algebra \(A\) correspond exactly to automorphism groups \(T_t\) satisfying \(\|T_t-I\|\to0\) as \(t\to0\), through \(T_t=e^{td}\).

**Proof.** For a bounded derivation, induction gives

\[d^n(xy)=\sum_{j=0}^n\binom nj d^j(x)d^{n-j}(y).\]

The induction applies one more product rule and combines adjacent coefficients by Pascal's identity. The operator exponential converges absolutely in norm. The double series for \((e^{td}x)(e^{td}y)\) is absolutely bounded by \(e^{2|t|\|d\|}\|x\|\|y\|\), so regrouping it by total degree and using the displayed formula gives \(e^{td}(xy)=(e^{td}x)(e^{td}y)\). The exponential group law and inverse follow by the same absolutely convergent power-series multiplication. For real \(t\), the coefficients are real and \(d\) preserves star, so the maps are star automorphisms. The bound \(\|e^{td}-I\|\leq e^{|t|\|d\|}-1\) proves the required continuity.

For the converse we give a bounded-generator argument rather than assume differentiability. Regard the group as bounded operators on the Banach space \(A\). Its operator-norm continuity allows a norm integral. Here is the elementary construction used below. A continuous function \(f:[a,b]\to E\) into a Banach space is uniformly continuous. Two tagged Riemann sums with sufficiently fine meshes differ by at most \(2(b-a)\omega_f(\delta)\), by passing to a common refinement, where \(\omega_f(\delta)=\sup_{|s-t|\le\delta}\|f(s)-f(t)\|\to0\). Thus the sums converge in the complete space \(E\), independently of tags and partitions. Their limit has norm at most \((b-a)\sup\|f\|\); additivity, translation of the interval and passage of bounded linear maps through the integral follow from the sums. For signed intervals,
\[
 \left\|\frac1h\int_a^{a+h}f(r)\,dr-f(a)\right\|
 \le\sup_{|r-a|\le |h|}\|f(r)-f(a)\|\longrightarrow0.
\]
Apply this construction to the Banach space of bounded operators on \(A\), and set

\[S_\varepsilon=\frac1\varepsilon\int_0^\varepsilon T_s\,ds.\]

For sufficiently small positive \(\varepsilon\), \(\|S_\varepsilon-I\|<1\), so \(S_\varepsilon\) is invertible by the Neumann series. The group law and the change of variable in this norm integral give

\[\frac{(T_h-I)S_\varepsilon}{h}
=\frac1\varepsilon\left(\frac1h\int_\varepsilon^{\varepsilon+h}T_r\,dr-\frac1h\int_0^hT_r\,dr\right)
\longrightarrow\frac{T_\varepsilon-I}{\varepsilon}\]

in operator norm, for positive or negative \(h\). Right multiplication by \(S_\varepsilon^{-1}\) gives a norm derivative \(d\) of \(T_h\) at zero. The group law then gives \(T'_t=T_t d\). Differentiating \(T_hT_t=T_tT_h\) at \(h=0\) also gives \(dT_t=T_t d\). Thus differentiating \(e^{-td}T_t\) shows it is constant, so \(T_t=e^{td}\). Differentiating \(T_t(xy)=T_t(x)T_t(y)\) and \(T_t(x^*)=T_t(x)^*\) at zero proves that \(d\) is a star derivation. \(\square\)

Apply this theorem to the action on \(M\). By bounded innerness, its bounded star derivation is \(d=i[h,\cdot]\) for a bounded self-adjoint \(h\in M\). Left multiplication by \(ih\) and right multiplication by \(-ih\) commute. Multiplying their absolutely convergent exponential series gives \(e^{td}(x)=e^{ith}xe^{-ith}\). This proves the asserted internal implementation.

## Two weaker hypotheses that do not suffice

Let \(M=\prod_{m\ge2}M_m(\mathbb C)\), the algebra of bounded matrix families. Define \(\theta_n\) to act only on the \(n\)th factor, \(n\ge2\), by conjugation with \(\operatorname{diag}(-1,1,\ldots,1)\). Its norm distance from the identity is two: the matrix unit \(E_{12}\) in that factor is sent to \(-E_{12}\), and two is the general upper bound for the difference of isometries. The bounded family \(x=(E_{12}^{(m)})_{m\ge2}\) lies in \(M\) and satisfies \(\|\theta_n(x)-x\|=2\) for every \(n\). Thus this sequence cannot satisfy the point-norm hypothesis of (UW.1).

On the C*-algebra \(A=\bigoplus_{m\ge2}^{c_0}M_m(\mathbb C)\), the same automorphisms do converge pointwise in norm: \(\|\theta_n(a)-a\|\le2\|a_n\|\to0\) for each \(a\in A\). They still have norm distance two from the identity. The test family \(x\) belongs to the von Neumann product and is excluded from the \(c_0\) sum; it detects precisely the error that point-norm convergence on the smaller algebra misses.

The same counterexample works on the unitization of the \(c_0\) sum: extend each automorphism to fix the scalar unit. The error of a scalar-plus-\(c_0\) element is still bounded by twice the norm of its \(n\)th \(c_0\) coordinate, while the operator-norm distance remains two.

Ultraweak continuity on a von Neumann algebra is also insufficient. On \(\ell^2(\mathbb N)\), put \(U_te_n=e^{itn}e_n\). These unitaries form a strongly continuous group: first test a finite linear combination of basis vectors, then use their common norm one to approximate an arbitrary vector. Consequently \(\alpha_t(x)=U_txU_t^*\) is pointwise ultraweakly continuous, by finite vector-functional tests and their norm-dense sums in the predual.

Let \(Ve_n=e_{n^2}\). The images form an orthonormal family, so \(V\) is an isometry in \(B(\ell^2)\), and

\[
 \alpha_t(V)e_n=e^{it(n^2-n)}e_{n^2}.
\]

For \(n\ge2\), take \(t_n=\pi/(n^2-n)\). Then \(t_n\to0\) but \(\|(\alpha_{t_n}(V)-V)e_n\|=2\), so \(\|\alpha_{t_n}(V)-V\|=2\). This group fails the pointwise norm hypothesis. Its unbounded diagonal generator therefore creates no contradiction with the bounded-generator theorem.
