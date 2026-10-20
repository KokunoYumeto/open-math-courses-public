# A tensor budget and a contracting kernel

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lessons 3–9 showed that the normalized transforms \(g_p\) of the supports are *flat*: they correlate with no product of a multiplicative and an additive character. Flatness alone allows \(g_p\) to be very sparse, concentrated on a few frequencies. This lesson and the next show that coverage of every large prime excludes this on a large set of primes. For an absolute \(\delta_0>0\), the balanced primes whose transform has \(L^1\) norm \(\gamma_p=\frac1p\sum_v|g_p(v)|\ge\delta_0\) carry harmonic mass at least \(0.15L\) in the band \(0.05L\le\log\log p\le0.9L\) (Theorem 1.1).

The proof is by contradiction. A sparse spectrum at a prime \(p\) defines a small kernel \(b_p\) on \(\mathbb F_p\), and the product over many such primes defines a nonnegative weight \(W(n)\). Two estimates of the average of \(W(a-d)\) over pairs \(a\in A\), \(d\in D\) conflict. In this lesson, an operator-norm bound for a tensor product of \(2\times2\) block matrices shows that this average is small (Proposition 4.2): each prime contributes a contraction factor \(1-1.6/p\). Lesson 11 evaluates the average of \(W\) over primes, where it is about \(1\), and uses coverage to transfer this to the pairs \((a,d)\).

**Prerequisites.** [*The inverse Goldbach problem*](the-inverse-goldbach-problem.md), Section 2; [*Square-root bounds and collision stability*](square-root-bounds-and-collision-stability.md), Theorem 3.1 and Lemma 4.1; [*Anchor codes and decorrelation of higher characters*](anchor-codes-and-decorrelation-of-higher-characters.md), Section 6 (the transforms \(F_p,g_p\)).

## 1. The statement

Recall from (6.1) of Lesson 9 the functions \(F_p\) and \(g_p\), with
\[
\begin{gathered}
\sum_{x\in\mathbb F_p}|F_p(x)|^2=p,\\
\frac1p\sum_{v\in\mathbb F_p}|g_p(v)|^2=1,\\
g_p(0)=0,\\
g_p(-v)=\overline{g_p(v)},
\end{gathered}
\]
and \(F_p(x)=p^{-1/2}\sum_vg_p(v)e_p(vx)\). Write
\[
\gamma_p=\frac1p\sum_{v\in\mathbb F_p}|g_p(v)|
\]
for the probability \(L^1\) norm of \(g_p\). By Cauchy–Schwarz, \(\gamma_p\le1\).

**Theorem 1.1** (a supply of nonsparse transforms [OpenAI-013, Proposition 5.1]). There is an absolute constant \(\delta_0>0\) such that, for all sufficiently large \(L\),
\[
\begin{aligned}
&\sum_{\substack{0.05L\le\log\log p\le0.9L\\1/3\le\sigma_p\le2/3\\\gamma_p\ge\delta_0}}\frac1p\ \\
&\quad \ge\ 0.15L .\quad(1.1)
\end{aligned}
\]

This theorem uses only the sieve estimates and coverage; it does not use the flatness of Lesson 9. The proof occupies this lesson and Lesson 11.

## 2. Parameters

Throughout this lesson and the next,
\[
\log X=e^L,\qquad R=\sqrt X,
\]
\[
\begin{gathered}
A_0=A\cap(R+N_*,X],\\
D_0=D\cap[-X,-R-N_*),\\
m_A=|A_0|,\\
m_D=|D_0|.
\end{gathered}
\]
For every prime \(p\le R\), the reductions of \(A_0\) lie in \(S_p\) and those of \(D_0\) in \(T_p:=S_p^c\), by Lemma 6.1 of Lesson 1. Put
\[
\begin{gathered}
\kappa_p=\frac{|T_p|}{|S_p|}=\frac{1-\sigma_p}{\sigma_p},\\
\text{so that}\\
\frac1{\sigma_p}+\frac1{1-\sigma_p}-4=\kappa_p+\kappa_p^{-1}-2 .
\end{gathered}
\]

**Lemma 2.1.** For large \(L\),
\[
\begin{gathered}
\sum_{p\le R}\bigl(\kappa_p+\kappa_p^{-1}-2\bigr)\frac{\log p}p\ll L,\\
\sum_{p\le R}\frac{|\log\kappa_p|}p\ll\sqrt L .\quad(2.1)
\end{gathered}
\]

*Proof.* Apply Lemma 4.1 of Lesson 2 at \(Y=X(\log X)^{40}\), with the uniform measures on \(A\cap(\sqrt Y+N_*,Y]\) and \(D\cap[-Y,-\sqrt Y-N_*)\). By Theorem 3.1 of Lesson 2 their point masses are at most \((\log Y)^4/\sqrt Y\), so \(b=4\), and the prime cutoff \(\sqrt Y/(\log Y)^5\) exceeds \(R\). The first bound follows since \(\log\log Y\ll L\). For the second, \((\log t)^2\le t+t^{-1}-2\) for \(t>0\) (with \(t=e^y\) this is \(y^2\le2\cosh y-2\)), and Cauchy–Schwarz gives
\[
\begin{aligned}
\sum_{p\le R}\frac{|\log\kappa_p|}p&\le\Bigl(\sum_{p\le R}\frac{(\log\kappa_p)^2\log p}p\Bigr)^{1/2}\\
&\quad \Bigl(\sum_p\frac1{p\log p}\Bigr)^{1/2},
\end{aligned}
\]
and the last series converges. \(\square\)

## 3. A budget for centred tensor coordinates

Let \(\mathbf e_x\) be the standard basis vector of \(x\) in \(\mathbb C^{\mathbb F_p}\), with the counting inner product. Let \(Q_{S_p}\) be the orthogonal projection onto
\[
\begin{aligned}
\mathcal H_{S_p}&=\Bigl\{f\in\mathbb C^{\mathbb F_p}:\operatorname{supp}f\subseteq S_p,\\
&\quad \ \sum_xf(x)=0\Bigr\},
\end{aligned}
\]
and define \(Q_{T_p}\), \(\mathcal H_{T_p}\) likewise. Explicitly \(Q_{S_p}f=\mathbf 1_{S_p}\bigl(f-\mathbb E_{S_p}f\bigr)\). For a squarefree \(t\) whose prime factors are at most \(R\), define
\[
\begin{gathered}
\begin{aligned}
&B_A(t)\\
&\quad=\Bigl\|\frac1{m_A}\sum_{a\in A_0}\bigotimes_{p\mid t}Q_{S_p}\mathbf e_{a\bmod p}\Bigr\|^2,
\end{aligned}\\
B_A(1)=1,
\end{gathered}
\]
and \(B_D(t)\) with \(D_0\) and \(T_p\).

**Lemma 3.1** (the primitive energy identity). For squarefree \(q\le R\),
\[
\begin{aligned}
&\sum_{\substack{h\bmod q\\ (h,q)=1}}\Bigl|\frac1{m_A}\sum_{a\in A_0}e_q(ha)\Bigr|^2\\
&\quad =\sum_{t\mid q}t\,B_A(t)\prod_{p\mid q/t}\kappa_p,\quad(3.1)
\end{aligned}
\]
and the same holds for \(D_0\) with \(B_D\) and \(\kappa_p^{-1}\). All terms on the right are nonnegative.

*Proof.* By the Chinese remainder theorem, \(\sum_{(h,q)=1}e_q(hn)=\prod_{p\mid q}\bigl(p\mathbf 1_{p\mid n}-1\bigr)\). For \(x,y\in S_p\), \(Q_{S_p}\mathbf e_x=\mathbf e_x-\mathbf 1_{S_p}/|S_p|\), so \(\langle Q_{S_p}\mathbf e_x,Q_{S_p}\mathbf e_y\rangle=\mathbf 1_{x=y}-1/|S_p|\), and since \(p/|S_p|=1+\kappa_p\),
\[
p\mathbf 1_{x=y}-1=\kappa_p+p\,\langle Q_{S_p}\mathbf e_x,Q_{S_p}\mathbf e_y\rangle .
\]
Expand the left side of (3.1) over two independent uniform elements \(a,a'\) of \(A_0\), multiply out the product of these identities over \(p\mid q\), and collect the terms with a centred factor exactly at the primes of \(t\): their average is \(t\,\|\frac1{m_A}\sum_a\bigotimes_{p\mid t}Q_{S_p}\mathbf e_a\|^2\prod_{p\mid q/t}\kappa_p\). For \(D_0\), \(p/|T_p|=1+\kappa_p^{-1}\). \(\square\)

Let \(\mathcal B_L=\{p : 0.05L\le\log\log p\le0.9L\}\), and for fixed \(C_*>0\) let \(\mathcal T_{C_*}\) be the set of products of at most \(C_*L\) distinct primes of \(\mathcal B_L\), including \(1\).

**Proposition 3.2** (the tensor budget [OpenAI-013, (5.4)]). For each fixed \(C_*\),
\[
\begin{gathered}
\sum_{t\in\mathcal T_{C_*}}B_A(t)\le e^{o(L)}\frac R{m_A},\\
\sum_{t\in\mathcal T_{C_*}}B_D(t)\le e^{o(L)}\frac R{m_D}.\quad(3.2)
\end{gathered}
\]
In particular, from the term \(t=1\),
\[
m_A,\ m_D\le Re^{o(L)}.
\tag{3.3}
\]

*Proof.* For \(t\in\mathcal T_{C_*}\), \(\log t\le C_*Le^{0.9L}=o(\log X)\), so \(t<R\) and \(U=R/t=X^{1/2-o(1)}\), uniformly. Among the positive integers \(u\le U\): the proportion that are not squarefree is at most \(\sum_pp^{-2}<\frac12\); the proportion not coprime to \(t\) is at most \(\sum_{p\mid t}1/p\le C_*L\exp(-e^{0.05L})=o(1)\); and, by (2.1),
\[
\begin{aligned}
&\frac1{\lfloor U\rfloor}\sum_{u\le U}\sum_{p\mid u}|\log\kappa_p|\\
&\quad \le\sum_{p\le U}\frac{|\log\kappa_p|}p\ll\sqrt L,
\end{aligned}
\]
so by Markov's inequality only a proportion \(O(L^{-1/4})\) has inner sum above \(L^{3/4}\). Hence at least \(cU\) integers \(u\le U\), with an absolute \(c>0\), are squarefree, coprime to \(t\), and satisfy
\[
\prod_{p\mid u}\kappa_p\ge e^{-L^{3/4}},\qquad\prod_{p\mid u}\kappa_p^{-1}\ge e^{-L^{3/4}}.
\]
The large sieve (2.1) of Lesson 1, with \(a_n=\mathbf 1_{A_0}(n)/m_A\) on at most \(X+1\) integers and \(Q=R\), bounds the sum of the left side of (3.1) over squarefree \(q\le R\) by \(2X/m_A=2R^2/m_A\). Writing \(q=tu\) and keeping, on the right of (3.1), only the term with the given \(t\in\mathcal T_{C_*}\) and \(u\) as above,
\[
\begin{aligned}
\frac{2R^2}{m_A}&\ge\sum_{t\in\mathcal T_{C_*}}tB_A(t)\\
&\quad \sum_{\substack{u\le R/t\\ u\ \text{squarefree},\ (u,t)=1}}\prod_{p\mid u}\kappa_p\\
&\ge cRe^{-L^{3/4}}\sum_{t\in\mathcal T_{C_*}}B_A(t).
\end{aligned}
\]
The pairs \((t,u)\) are distinct for distinct terms, and all terms are nonnegative. The bound for \(D_0\) is the same with \(\kappa_p^{-1}\). \(\square\)

## 4. A contracting local kernel

Fix a sufficiently small absolute \(\epsilon_0>0\), and let \(0<\delta_0\le\epsilon_0^2\). Suppose, for a sequence of arbitrarily large \(L\), that (1.1) fails. Let
\[
\begin{gathered}
\begin{aligned}
\mathcal S&=\Bigl\{p\in\mathcal B_L:\tfrac13\le\sigma_p\le\tfrac23,\ \gamma_p\\
&<\delta_0\Bigr\},
\end{aligned}\\
H=\sum_{p\in\mathcal S}\frac1p .
\end{gathered}
\]
Mertens' estimate gives \(\sum_{p\in\mathcal B_L}1/p=0.85L+o(1)\). Outside the balanced range \(\kappa_p+\kappa_p^{-1}-2\ge\frac12\), and \(\log p\ge e^{0.05L}\) on \(\mathcal B_L\), so by (2.1) the unbalanced primes of \(\mathcal B_L\) have harmonic mass \(O(Le^{-0.05L})=o(1)\). Since (1.1) fails, \(H\ge0.70L-o(L)\), and in particular
\[
H\ge0.68L,
\tag{4.1}
\]
also after the deletion of any one prime from \(\mathcal S\).

**The sparse spectrum.** For \(p\in\mathcal S\) put \(E_p=\{v\in\mathbb F_p:|g_p(v)|>1\}\). It is symmetric and avoids \(0\), and
\[
\begin{gathered}
|E_p|\le\epsilon_0p,\\
\sum_{v\in E_p}|g_p(v)|^2\ge(1-\epsilon_0^2)p .\quad(4.2)
\end{gathered}
\]
Indeed \(|E_p|\le\sum_v|g_p(v)|=p\gamma_p<\delta_0p\), and off \(E_p\), \(|g_p(v)|^2\le|g_p(v)|\), so \(\sum_{v\notin E_p}|g_p|^2<\delta_0p\le\epsilon_0^2p\).

Put \(t_0=0.85\) and
\[
b_p(x)=\frac{t_0}p\sum_{h\in E_p}e_p(hx),
\]
a real function because \(E_p\) is symmetric. Let \(\Pi_p\) be the orthogonal projection of \(\mathbb C^{\mathbb F_p}\) onto the span of the additive characters \(e_p(h\,\cdot)\), \(h\in E_p\). The matrix with entries \(b_p(x-y)\) is \(t_0\Pi_p\). Since \(0\notin E_p\) and \(F_p=\sum_v(g_p(v)/\sqrt p)\,e_p(v\,\cdot)\), Parseval and (4.2) give
\[
\begin{gathered}
\Pi_p\mathbf 1=0,\\
\|\Pi_pF_p-F_p\|\le\epsilon_0\sqrt p,\\
\|\Pi_pF_p\|^2\ge(1-\epsilon_0^2)p .\quad(4.3)
\end{gathered}
\]
Let \(B_p^{(2)}\) be the matrix with entries \(b_p(x-y)^2\). Its eigenvalue at the additive character \(s\) is \(\frac{t_0^2}p\#\{(h,h')\in E_p^2:h+h'=s\}\)\(\le t_0^2|E_p|/p\), so
\[
\begin{gathered}
\|B_p^{(2)}\|\le t_0^2\epsilon_0,\\
|b_p(x)|\le t_0\epsilon_0 .\quad(4.4)
\end{gathered}
\]
With \(e_p^*=|E_p|/p\), direct summation gives
\[
\begin{gathered}
\frac1{p-1}\sum_{x\ne0}b_p(x)=-\frac{t_0e_p^*}{p-1},\\
\begin{aligned}
&\frac1{p-1}\sum_{x\ne0}b_p(x)^2\\
&\quad =\frac{t_0^2\bigl(e_p^*-(e_p^*)^2\bigr)}{p-1},
\end{aligned}\quad(4.5)
\end{gathered}
\]
because \(\sum_xb_p(x)=0\), \(b_p(0)=t_0e_p^*\), and \(\sum_xb_p(x)^2=t_0^2|E_p|/p\). Both means are \(O(\epsilon_0/p)\).

**Block coordinates.** Put \(u_S=\mathbf 1_{S_p}/|S_p|\) and \(u_T=\mathbf 1_{T_p}/|T_p|\). For \(x\in S_p\), \(\mathbf e_x=u_S+Q_{S_p}\mathbf e_x\), and for \(y\in T_p\), \(\mathbf e_y=u_T+Q_{T_p}\mathbf e_y\). So for a kernel \(h(x-y)\), with matrix also denoted \(h\), the map
\[
\begin{aligned}
L_p[h]&=
\begin{pmatrix}
u_S^*hu_T&u_S^*hQ_{T_p}\\
Q_{S_p}hu_T&Q_{S_p}hQ_{T_p}
\end{pmatrix}\\
&\quad \colon\ \mathbb C\oplus\mathcal H_{T_p}\to\mathbb C\oplus\mathcal H_{S_p}
\end{aligned}
\]
represents \(h\) in the coordinates \((1,Q_{S_p}\mathbf e_x)\) and \((1,Q_{T_p}\mathbf e_y)\): \(h(x-y)=(1,Q_{S_p}\mathbf e_x)^*L_p[h](1,Q_{T_p}\mathbf e_y)\). For complex \(u,v\) define
\[
\begin{gathered}
\begin{aligned}
L_p(u,v)&=L_p\bigl[(1+ub_p)(1+vb_p)\bigr],
\end{aligned}\\
\begin{aligned}
U_p(u,v)&=\frac1{p-1}\sum_{x\ne0}\bigl(1\\
&\quad +ub_p(x)\bigr)\bigl(1\\
&\quad +vb_p(x)\bigr).
\end{aligned}
\end{gathered}
\]

**Lemma 4.1** (local contraction [OpenAI-013, Lemma 5.2]). For \(\epsilon_0\) small enough, uniformly for \(p\in\mathcal S\) and \(|u|,|v|\le1.03\),
\[
\begin{gathered}
\|L_p(u,v)\|\le1+\frac Cp,\\
|U_p(u,v)|\le1+\frac Cp,
\end{gathered}
\]
and for all large \(p\in\mathcal S\),
\[
\begin{gathered}
\begin{aligned}
\|L_p(1,1)\|&\le U_p(1,1)\Bigl(1-\frac{1.6}p\Bigr),
\end{aligned}\\
U_p(1,1)=1+O\Bigl(\frac{\epsilon_0}p\Bigr).\quad(4.6)
\end{gathered}
\]
All constants are absolute.

*Proof.* The constant kernel \(1\) has \(L_p[1]=\begin{pmatrix}1&0\\0&0\end{pmatrix}\), because \(u_S\) and \(u_T\) are probability vectors and vectors of \(\mathcal H_{T_p}\) have sum zero. In \(\mathbb C^{\mathbb F_p}\),
\[
\begin{gathered}
u_S=\frac{\mathbf 1+\sqrt{\kappa_p}F_p}p,\\
u_T=\frac{\mathbf 1-F_p/\sqrt{\kappa_p}}p,
\end{gathered}
\]
as one checks on \(S_p\) and \(T_p\). Since \(\Pi_p\) is self-adjoint and kills constants, \(u_S^*\Pi_pu_T=-p^{-2}\|\Pi_pF_p\|^2\). Since \(F_p\) is constant on \(S_p\) and on \(T_p\), \(Q_{S_p}F_p=Q_{T_p}F_p=0\), so for example \(Q_{S_p}\Pi_pu_T=-p^{-1}\kappa_p^{-1/2}Q_{S_p}(\Pi_pF_p-F_p)\), which has norm \(O(\epsilon_0/\sqrt p)\) by (4.3); the balance bounds \(\kappa_p^{\pm1/2}\) absolutely, and the other side block is the same. The supports are disjoint, so \(Q_{S_p}Q_{T_p}=0\) and
\[
\begin{aligned}
\|Q_{S_p}\Pi_pQ_{T_p}\|&=\|Q_{S_p}(\Pi_p-\tfrac12I)Q_{T_p}\|\\
&\le\tfrac12 .
\end{aligned}
\]
By (4.4) and \(\|u_S\|,\|u_T\|=O(p^{-1/2})\), the square kernel contributes \(O(\epsilon_0/p)\) to the scalar block, \(O(\epsilon_0/\sqrt p)\) to the side blocks, and \(O(\epsilon_0)\) to the lower-right block.

Since \((1+ub_p)(1+vb_p)\)\(=1+(u+v)b_p+uvb_p^2\), the scalar block of \(L_p(u,v)\) is \(s_p(u,v)=1+O(1/p)\), the side blocks are \(O(\epsilon_0/\sqrt p)\), and the lower-right block has norm at most \(2\cdot1.03\cdot t_0\cdot\frac12+O(\epsilon_0)<0.95\). At \(u=v=1\) the scalar block is real and, by (4.3),
\[
\begin{aligned}
s_p(1,1)&=1-\frac{2t_0}{p^2}\|\Pi_pF_p\|^2+O\Bigl(\frac{\epsilon_0}p\Bigr)\\
&\le1-\frac{1.7-O(\epsilon_0)}p .
\end{aligned}
\]
The norm of a \(2\times2\) block operator is at most the norm of the \(2\times2\) matrix of the block norms, here at most the largest eigenvalue of \(\begin{pmatrix}|s_p|&C\epsilon_0/\sqrt p\\ C\epsilon_0/\sqrt p&0.95\end{pmatrix}\). Since \(|s_p|-0.95\ge0.04\) for large \(p\), this eigenvalue is at most \(|s_p|+O(\epsilon_0^2/p)\). This gives the first bound and \(\|L_p(1,1)\|\le1-(1.7-O(\epsilon_0))/p\). By (4.5), \(U_p(u,v)=1+O(\epsilon_0/p)\) on the polydisc. Decreasing \(\epsilon_0\), \(1-(1.7-O(\epsilon_0))/p\)\(\le U_p(1,1)(1-1.6/p)\). \(\square\)

**Tensoring.** Choose a large fixed \(C_K\) and put \(K=\lceil C_KL\rceil\). Define the nonnegative weight
\[
\begin{aligned}
&W(n)\\
&\quad=\Bigl(\sum_{\substack{I\subseteq\mathcal S\\|I|\le K}}\prod_{p\in I}b_p(n)\Bigr)^2 .\quad(4.7)
\end{aligned}
\]
For a polynomial \(\mathsf P(u,v)\), scalar or operator valued, let \(\mathcal R_K\mathsf P\) be the sum of its Taylor coefficients of degree at most \(K\) in each variable, evaluated at \(u=v=1\). Put
\[
\begin{gathered}
\mathcal L(u,v)=\bigotimes_{p\in\mathcal S}L_p(u,v),\\
\mathcal U(u,v)=\prod_{p\in\mathcal S}U_p(u,v),\\
U=\mathcal U(1,1).
\end{gathered}
\]
Expanding \(\prod_p(1+ub_p(n))(1+vb_p(n))\)\(=\sum_{I,J}u^{|I|}v^{|J|}\prod_{p\in I}b_p(n)\)\(\prod_{p\in J}b_p(n)\) shows that \(\mathcal R_K\mathcal L\) represents the kernel \(W(x-y)\) in the full tensor coordinates, and that \(\mathcal R_K\mathcal U\) is the mean of \(W\) over independent uniform unit residues at the primes of \(\mathcal S\).

**Proposition 4.2** (the pair average is small [OpenAI-013, (5.13)]). For large \(L\) in the sequence,
\[
\begin{aligned}
&\frac1{m_Am_D}\sum_{a\in A_0}\sum_{d\in D_0}W(a-d)\\
&\quad \le U\exp\bigl(-1.6H\\
&\qquad +o(L)\bigr)\Bigl(\frac{R^2}{m_Am_D}\Bigr)^{1/2},\quad(4.8)
\end{aligned}
\]
and \(U=e^{O(\epsilon_0L)}\). The same holds after deleting one prime from \(\mathcal S\).

*Proof.* *Truncation.* Let \(r_0=1.03\). By Lemma 4.1 and \(\sum_{p\in\mathcal S}1/p\le0.85L+o(L)\), both \(\mathcal L\) and \(\mathcal U\) have norm at most \(e^{C_0L}\) on \(|u|,|v|\le r_0\), with an absolute \(C_0\). Cauchy's coefficient formula applies to polynomials with values in finite-dimensional operator spaces: the coefficient of \(u^iv^j\) has norm at most \(e^{C_0L}r_0^{-i-j}\). Summing the geometric series over \(i>K\) or \(j>K\),
\[
\begin{aligned}
&\|\mathcal R_K\mathcal L-\mathcal L(1,1)\|+|\mathcal R_K\mathcal U-U|\\
&\quad \ll e^{C_0L}r_0^{-K}.
\end{aligned}
\]
By Lemma 4.1, \(U=e^{O(\epsilon_0L)}\) and \(\|\mathcal L(1,1)\|\le U\prod_{p\in\mathcal S}(1-1.6/p)\)\(\le Ue^{-1.6H}\). Choose \(C_K\) so large that \(e^{C_0L}r_0^{-K}\le e^{-5L}\), which is \(o(Ue^{-1.6H})\) since \(H\le0.85L+o(L)\) and \(\epsilon_0\) is small.

*The coordinates actually used.* Let
\[
\begin{gathered}
\begin{aligned}
V_A&=\frac1{m_A}\sum_{a\in A_0}\bigotimes_{p\in\mathcal S}\bigl(1,\\
&\quad Q_{S_p}\mathbf e_{a\bmod p}\bigr),
\end{aligned}\\
\begin{aligned}
V_D&=\frac1{m_D}\sum_{d\in D_0}\bigotimes_{p\in\mathcal S}\bigl(1,\\
&\quad Q_{T_p}\mathbf e_{d\bmod p}\bigr).
\end{aligned}
\end{gathered}
\]
The tensor space is the orthogonal sum of the *subset modes* \(\bigotimes_{p\in I}\mathcal H_{S_p}\), and the squared norm of the component of \(V_A\) in the mode \(I\) is \(B_A(\prod_{p\in I}p)\). Every monomial kept in \(\mathcal R_K\mathcal L\) involves at most \(2K\) primes, and at every other prime the local factor is \(L_p[1]\), which has only a scalar block. So \(\mathcal R_K\mathcal L=P_A(\mathcal R_K\mathcal L)P_D\), where \(P_A,P_D\) keep only the modes with at most \(2K\) centred factors. Proposition 3.2 with any fixed \(C_*>2C_K\) gives \(\|P_AV_A\|^2\le e^{o(L)}R/m_A\) and \(\|P_DV_D\|^2\le e^{o(L)}R/m_D\).

*Conclusion.* The left side of (4.8) equals \(V_A^*(\mathcal R_K\mathcal L)V_D=(P_AV_A)^*(\mathcal R_K\mathcal L)(P_DV_D)\), which is at most \(\|\mathcal R_K\mathcal L\|\,\|P_AV_A\|\,\|P_DV_D\|\). Every step is uniform under the deletion of one prime from \(\mathcal S\). \(\square\)

The dimension of the tensor space plays no role: only the modes with few centred factors are seen by the truncated kernel, and their total weight is controlled by the large sieve through Proposition 3.2.

## 5. Exercises

**5.1.** Show that \((\log t)^2\le t+t^{-1}-2\) for all \(t>0\).

**5.2.** Let \(\Pi\) be an orthogonal projection on a Hilbert space and \(Q_1,Q_2\) orthogonal projections with \(Q_1Q_2=0\). Show that \(\|Q_1\Pi Q_2\|\le\frac12\), and give an example with equality.

**5.3.** Show that the norm of a block operator \(\begin{pmatrix}A&B\\C&D\end{pmatrix}\) is at most the norm of the real \(2\times2\) matrix \(\begin{pmatrix}\|A\|&\|B\|\\\|C\|&\|D\|\end{pmatrix}\).

**5.4.** Verify the formulas for \(u_S\) and \(u_T\) in terms of \(F_p\) and \(\kappa_p\).

## 6. Solutions

**5.1.** Put \(t=e^y\). The claim is \(y^2\le e^y+e^{-y}-2=2(\cosh y-1)\), which holds because \(\cosh y-1=\sum_{n\ge1}y^{2n}/(2n)!\ge y^2/2\).

**5.2.** Since \(Q_1Q_2=0\), \(Q_1\Pi Q_2=Q_1(\Pi-\frac12I)Q_2\), and \(\Pi-\frac12I\) is self-adjoint with eigenvalues \(\pm\frac12\), so its norm is \(\frac12\). Equality: in \(\mathbb C^2\), \(Q_1,Q_2\) the projections onto the two coordinate axes and \(\Pi\) the projection onto the diagonal line; then \(Q_1\Pi Q_2\mathbf e_2=\frac12\mathbf e_1\).

**5.3.** For a vector \((x,y)\), \(\|(Ax+By,Cx+Dy)\|^2\)\(\le(\|A\|\|x\|+\|B\|\|y\|)^2\)\(+(\|C\|\|x\|+\|D\|\|y\|)^2\), which is the squared norm of the real matrix applied to \((\|x\|,\|y\|)\), and \(\|(\|x\|,\|y\|)\|=\|(x,y)\|\).

**5.4.** \(\sqrt{\kappa_p}F_p=\sqrt{\frac{1-\sigma}\sigma}\cdot\frac{\mathbf 1_S-\sigma}{\sqrt{\sigma(1-\sigma)}}=\frac{\mathbf 1_S-\sigma}\sigma\), so \(\mathbf 1+\sqrt{\kappa_p}F_p=\mathbf 1_S/\sigma\) and \((\mathbf 1+\sqrt{\kappa_p}F_p)/p=\mathbf 1_S/|S|\). Similarly \(F_p/\sqrt{\kappa_p}=(\mathbf 1_S-\sigma)/(1-\sigma)\), so \(\mathbf 1-F_p/\sqrt{\kappa_p}=\mathbf 1_T/(1-\sigma)\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 5: Proposition 5.1, a budget for centred tensor coordinates (5.2)–(5.4), a contracting local kernel from a sparse transform, Lemma 5.2, and tensoring and truncating the kernel (5.13). https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
