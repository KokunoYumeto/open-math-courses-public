# The Euler product of the probe

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[*The Poisson probe*](the-poisson-probe.md) expressed the probe through the Dirichlet series \(\mathcal F_u(\xi,w,z)\), one for each frequency class \(u\). This lesson factors each of them as an Euler product,
\[
\begin{aligned}
\mathcal F_u(\xi,w,z)&=\frac{\zeta_F^S(6z)\,L^S\bigl(w,\chi_\bullet(u)\bigr)}{L^S\bigl(\xi,\eta\overline{\chi_\bullet(u)}\bigr)}\\
&\quad \,\mathcal H_u(\xi,w,z),
\end{aligned}
\]
with a correction \(\mathcal H_u\) that is holomorphic and of size \(O(q_u^\epsilon)\) on two explicit regions. The reciprocal \(L\)-function in the denominator comes from one local term: at a prime \(\mathfrak p\) the squarefree theta coefficient \(\gamma_2(\mathfrak p)\vartheta(\mathfrak p)\) meets the Gauss sum \(\tau_1=q_{\mathfrak p}^{1/2}\gamma_1(\mathfrak p)\) produced by Poisson summation, and the identity \(\gamma_1\gamma_2\vartheta=-\eta\) of [*Gauss sums and the correction characters*](gauss-sums-and-the-correction-characters.md) makes this term \(-\eta(\mathfrak p)\overline{\chi_{\mathfrak p}(u)}q_{\mathfrak p}^{-\xi}\). For \(u=1\) the correction is also nowhere zero, which is statement (H) of [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md).

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Sections 1 and 3; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), Section 1, Proposition 2.1 and Lemma 3.2; [*Gauss sums and the correction characters*](gauss-sums-and-the-correction-characters.md), Lemma 1.1, (3.1), Proposition 5.1 and Section 6; [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md), Sections 1 and 5; [*The Poisson probe*](the-poisson-probe.md), Section 5 and Proposition 7.1.

## 1. Incomplete L-functions of ideal characters

For a function \(\lambda\) on exterior primes with \(|\lambda(\mathfrak p)|\le1\), put \(L^S(s,\lambda)=\prod_{\mathfrak p\notin S}(1-\lambda(\mathfrak p)q_{\mathfrak p}^{-s})^{-1}\) for \(\operatorname{Re}s>1\); the factors at \(S\) are omitted and zero values of \(\lambda\) are kept. In particular, with the Kummer character \(\chi_\bullet(u)\) of Lesson 3,
\[
\begin{gathered}
\begin{aligned}
L^S\bigl(w,\chi_\bullet(u)\bigr)&=\prod_{\mathfrak p\notin S}\bigl(1-\chi_{\mathfrak p}(u)q_{\mathfrak p}^{-w}\bigr)^{-1},
\end{aligned}\\
\zeta_F^S(s)=\prod_{\mathfrak p\notin S}\bigl(1-q_{\mathfrak p}^{-s}\bigr)^{-1}.
\end{gathered}
\]

## 2. Factoring the finite expression

Fix \(u\in\mathcal U\). In (7.2) of Lesson 11 use, for \(s\), \(A=cn^3\) and \(r\), the products of the allowed generators of the primes; another allowed choice differs by an element of \(U_S^6\), which changes nothing. At an exterior prime \(\mathfrak p\) with allowed generator \(p\) and norm \(Q\), write
\[
\begin{gathered}
e_0=v_{\mathfrak p}(\mathfrak c)\in\{0,1\},\\
l=v_{\mathfrak p}(\mathfrak n),\\
t=e_0+3l,\\
k=v_{\mathfrak p}(\mathfrak s),\\
j=v_{\mathfrak p}(u),\\
m'=v_{\mathfrak p}(\mathfrak r),\\
J=j+6m',
\end{gathered}
\]
and \(s=p^ks_p\), \(A=p^tA_p\), \(ur^6=p^Jh_p\), so that \(s_p,A_p,h_p\) are units at \(\mathfrak p\). Put \(\psi^\circ_{\mathfrak p}(x)=\psi_{\mathfrak p}(-x)\); for \(x\in F\), the product formula for \(\psi\) gives \(\mathrm e(x)=\prod_{\mathfrak p\notin S}\psi^\circ_{\mathfrak p}(x)\), a finite product. Define the **local sum**
\[
\begin{aligned}
C_{t,k}(J)&=\sum_{\substack{d\bmod p^k\\ p^J\equiv p^td\ (p^k)}}\chi_{\mathfrak p}(d)^k\\
&\quad \sum_{x\bmod p^t}\chi_{\mathfrak p}(x)^t\\
&\quad \,\psi^\circ_{\mathfrak p}\Bigl(\frac{(p^J-p^td)x}{p^{k+t}}\Bigr),\quad(2.1)
\end{aligned}
\]
where a modulus \(p^0\) means one residue with character value \(1\), and a positive modulus keeps the unit mask even when the exponent is divisible by \(6\).

**Lemma 2.1** (local factorization [OpenAI-029, (7.11)–(7.12)]). With \(F(s,A,h)\) as in (5.1) of Lesson 11,
\[
\begin{aligned}
F(s,A,ur^6)&=\prod_{\mathfrak p\notin S}\chi_{\mathfrak p}(h_p)^{k-t}\\
&\quad \,\chi_{\mathfrak p}(s_p)^t\\
&\quad \,\chi_{\mathfrak p}(A_p)^{t-k}\\
&\quad \,C_{t,k}(J),\quad(2.2)
\end{aligned}
\]
where all but finitely many factors are \(1\), and \(\chi_{\mathfrak p}(h_p)=\chi_{\mathfrak p}(u/p^j)\).

*Proof.* Expand the Gauss sum in (5.1) of Lesson 11. By the Chinese remainder theorem the residues \(d\) modulo \(\mathfrak s\) and \(x\) modulo \(\mathfrak A\) correspond to independent families of local residues, the congruence \(h\equiv Ad\pmod{\mathfrak s}\) splits into local congruences, and \(\chi_{\mathfrak s}(d)\chi_{\mathfrak A}(x)=\prod_{\mathfrak p}\chi_{\mathfrak p}(d)^k\chi_{\mathfrak p}(x)^t\). The additive factor is \(\prod_{\mathfrak p}\psi^\circ_{\mathfrak p}\bigl((h-Ad)x/(sA)\bigr)\), and the factor at \(\mathfrak p\) depends only on the local residues of \(d\) and \(x\), because \(h-Ad\in\mathfrak p^k\). So \(F\) is the product of the local sums
\[
\begin{aligned}
&\sum_{\substack{d\bmod p^k\\ p^Jh_p\equiv p^tA_pd\ (p^k)}}\chi_{\mathfrak p}(d)^k\\
&\quad \sum_{x\bmod p^t}\chi_{\mathfrak p}(x)^t\\
&\quad \,\psi^\circ_{\mathfrak p}\Bigl(\frac{(p^Jh_p-p^tA_pd)x}{p^{k+t}s_pA_p}\Bigr),
\end{aligned}
\]
which are \(1\) at the primes not dividing \(\mathfrak s\mathfrak A\). The substitutions \(d=(h_p/A_p)d'\) and \(x=(s_pA_p/h_p)x'\) are bijections of the residue rings, preserve units, turn the congruence into \(p^J\equiv p^td'\pmod{p^k}\) and the additive argument into \((p^J-p^td')x'/p^{k+t}\), and remove the factor \(\chi_{\mathfrak p}(h_p/A_p)^k\chi_{\mathfrak p}(s_pA_p/h_p)^t\), which is the unit factor in (2.2). Finally \(h_p=(u/p^j)(r/p^{m'})^6\), and \(\chi_{\mathfrak p}\) is trivial on sixth powers of units. \(\square\)

**Lemma 2.2** (the cross-prime factors cancel [OpenAI-029, (7.13)]). The product over \(\mathfrak p\) of \(\chi_{\mathfrak p}(s_p)^t\chi_{\mathfrak p}(A_p)^{t-k}\), multiplied by the factors \(\chi_{\mathfrak c_1}(c_2)^2\chi_{\mathfrak c_2}(c_1)^2\) by which \(\gamma_2(\mathfrak c)\) differs from \(\prod_{\mathfrak p\mid\mathfrak c}\gamma_2(\mathfrak p)\) ((5.2) of Lesson 4), is \(1\).

*Proof.* All factors are products, over unordered pairs of distinct primes \(\mathfrak p,\mathfrak p'\), of powers of \(\zeta=\chi_{\mathfrak p}(p')=\chi_{\mathfrak p'}(p)\) (Proposition 2.1 of Lesson 3), with the exponents \(t,k,e_0\) at \(\mathfrak p\) and \(t',k',e_0'\) at \(\mathfrak p'\). Since \(s_p\) contains \(p'^{k'}\) and \(A_p\) contains \(p'^{t'}\), the first product contributes the exponent \(tk'+(t-k)t'+t'k+(t'-k')t=2tt'\), and (5.2) of Lesson 4 contributes \(4e_0e_0'\). With \(t=e_0+3l\), \(t'=e_0'+3l'\),
\[
\begin{aligned}
&2tt'+4e_0e_0'=6e_0e_0'\\
&\qquad +6(e_0l'+e_0'l)+18ll'\\
&\quad \equiv0\pmod6 .
\end{aligned}
\]
Shared prime powers of \(\mathfrak s\) and \(\mathfrak A\) were kept inside the local sums, so no coprimality is needed. \(\square\)

Write \(\theta_{\mathfrak p}=\chi_{\mathfrak p}(u/p^j)\in\mu_6\) and \(\gamma_2(\mathfrak p)\) for the normalized prime Gauss sum of Lesson 4. By Lemmas 2.1 and 2.2, and absolute convergence on the lines of Proposition 7.1 of Lesson 11, \(\mathcal F_u=\prod_{\mathfrak p\notin S}\mathcal F_{u,\mathfrak p}\) with
\[
\begin{gathered}
\begin{aligned}
&\mathcal F_{u,\mathfrak p}(\xi,w,z)\\
&\quad =\sum_{\substack{e_0\in\{0,1\}\\ l,k,m'\ge0}}\gamma_2(\mathfrak p)^{e_0}\vartheta(\mathfrak p)^{t}\\
&\qquad \,\theta_{\mathfrak p}^{\,k-t}\,C_{t,k}(j+6m')\\
&\qquad \,Q^{-e_0(1/2+\xi)-l(1+3\xi)-kw-6m'z},
\end{aligned}\\
t=e_0+3l .\quad(2.3)
\end{gathered}
\]

## 3. The local sums

For \(v\in\mathbb Z\) and \(y\in\mathcal O_{\mathfrak p}\) put
\[
\begin{gathered}
\begin{aligned}
T_v(y)&=\sum_{x\bmod p}\chi_{\mathfrak p}(x)^v\,\psi^\circ_{\mathfrak p}(yx/p),
\end{aligned}\\
\tau_v=T_v(1),
\end{gathered}
\]
with the unit mask also for \(6\mid v\). Then \(T_v(y)=\overline{\chi_{\mathfrak p}(y)}^{\,v}\tau_v\) if \(p\nmid y\), and for \(p\mid y\), \(T_v(y)=Q-1\) if \(6\mid v\) and \(0\) otherwise. Moreover \(|\tau_v|=Q^{1/2}\) for \(6\nmid v\), \(\tau_0=-1\), \(\tau_1\tau_5=Q\), and \(\tau_1=Q^{1/2}\gamma_1(\mathfrak p)\), because \(\mathrm e(x/p)=\psi^\circ_{\mathfrak p}(x/p)\) ((3.1) of Lesson 4 and the remark after it).

**Lemma 3.1** (values of the local sums [OpenAI-029, (7.15)]). \(C_{0,0}(J)=1\), and \(C_{0,k}(J)=\mathbf 1_{J=0}\) for \(k\ge1\). For \(t\ge1\),
\[
\begin{aligned}
C_{t,0}(J)&=\mathbf 1_{J\ge t-1}\,Q^{t-1}\,T_t\bigl(p^{J-t+1}\bigr),\\
C_{t,1}(J)&=\mathbf 1_{J\ge t}\,\tau_1\,Q^{t-1}\,T_{t-1}\bigl(p^{J-t}\bigr),\\
C_{t,k}(J)&=0\qquad(k\ge2).\quad(3.1)
\end{aligned}
\]
In particular \(|C_{t,0}(J)|\le Q^t\) and \(|C_{t,1}(J)|\le Q^{t+1/2}\).

*Proof.* The facts about \(T_v\) follow from the substitution \(x\mapsto y^{-1}x\) for \(p\nmid y\), from orthogonality for \(p\mid y\), from Lemma 1.1 of Lesson 4, and from \(\chi_{\mathfrak p}(-1)=1\).

*\(t=0\).* The inner sum is \(1\). If \(k=0\) the outer sum is \(1\). If \(k\ge1\), the congruence picks \(d=p^J\), and \(\chi_{\mathfrak p}(p^J)^k\) is \(1\) for \(J=0\) and \(0\) for \(J\ge1\) by the unit mask.

*\(t\ge1\), \(k=0\).* The sum is \(\sum_{x\bmod p^t}\chi_{\mathfrak p}(x)^t\psi^\circ_{\mathfrak p}(x/p^{t-J})\). Write \(x=x_0+p\lambda\) with \(x_0\) modulo \(p\) and \(\lambda\) modulo \(p^{t-1}\); the character depends on \(x_0\) only. The sum over \(\lambda\) of \(\psi^\circ_{\mathfrak p}(\lambda/p^{t-J-1})\) is \(0\) if \(1\le t-J-1\le t-1\) and \(Q^{t-1}\) otherwise, that is, for \(J\ge t-1\). Then the sum over \(x_0\) is \(T_t(p^{J-t+1})\).

*\(t\ge1\), \(k=1\).* The congruence \(p^J\equiv p^td\pmod p\) needs \(J\ge1\) and then holds for every \(d\). For a unit \(x\), the sum over \(d\) of \(\chi_{\mathfrak p}(d)\psi^\circ_{\mathfrak p}(-dx/p)\) is \(\overline{\chi_{\mathfrak p}(x)}\tau_1\), by \(d\mapsto-x^{-1}d\) and \(\chi_{\mathfrak p}(-1)=1\). What remains is \(\tau_1\sum_{x\bmod p^t}\chi_{\mathfrak p}(x)^{t-1}\psi^\circ_{\mathfrak p}(p^Jx/p^{t+1})\) over units \(x\), and the same lifting argument gives \(\mathbf 1_{J\ge t}Q^{t-1}T_{t-1}(p^{J-t})\).

*\(t\ge1\), \(k\ge2\).* Replacing \(d\) by \(d+p^{k-1}\lambda\) preserves the congruence (as \(t\ge1\)) and the character, and multiplies the additive factor by \(\psi^\circ_{\mathfrak p}(-\lambda x/p)\), whose sum over \(\lambda\) modulo \(p\) is \(0\) for a unit \(x\).

The bounds follow from \(|T_v|\le Q-1\) and \(|\tau_1|=Q^{1/2}\). \(\square\)

## 4. The factor at a prime not dividing u

Let \(\mathfrak p\nmid uR\), so \(j=0\), \(J=6m'\) and \(\theta_{\mathfrak p}=\chi_{\mathfrak p}(u)\). Put
\[
\begin{gathered}
V=Q^{-6z},\\
W=\chi_{\mathfrak p}(u)Q^{-w},\\
D_1=\eta(\mathfrak p)\overline{\chi_{\mathfrak p}(u)}Q^{-\xi},\\
E_1=\vartheta(\mathfrak p)^6Q^{4-6\xi}V .
\end{gathered}
\]

**Proposition 4.1** (the good local factor [OpenAI-029, (7.16)]). In absolute convergence,
\[
\begin{aligned}
&\mathcal F_{u,\mathfrak p}=\frac1{1-V}+\frac W{1-W}\\
&\quad+\frac{E_1}{1-E_1}\Bigl(\frac{1-Q^{-1}}{1-V}+W\Bigr)\\
&\quad-\frac{D_1}{1-E_1}\Bigl(1+\frac{(Q-1)WV}{1-V}\Bigr).\quad(4.1)
\end{aligned}
\]

*Proof.* Evaluate (2.3) with Lemma 3.1.

*\(t=0\).* The terms with \(k=0\) give \(\sum_{m'}V^{m'}=(1-V)^{-1}\). For \(k\ge1\) only \(J=0\), that is \(m'=0\), survives, giving \(\sum_{k\ge1}W^k=W/(1-W)\).

*\(t\ge1\).* By (3.1) with \(J=6m'\), a term with \(k=0\) needs \(J=t-1\), possible only for \(t\equiv1\pmod6\), where \(T_t(1)=\tau_1\), or \(J\ge t\) with \(6\mid t\), where \(T_t(p^{\ge1})=Q-1\). A term with \(k=1\) needs \(J=t\) with \(6\mid t\), where \(T_{t-1}(1)=\tau_5\), or \(J>t\) with \(t\equiv1\pmod6\), where \(T_{t-1}(p^{\ge1})=Q-1\). So only \(t=6d\) (\(e_0=0\), \(l=2d\)) and \(t=6d+1\) (\(e_0=1\), \(l=2d\)) occur. In each case the power \(Q^{6d}\) coming from \(C_{t,k}\) and \(Q^{-l(1+3\xi)}=Q^{-2d-6d\xi}\) combine to \(Q^{4d-6d\xi}\), which with \(V^d\) and \(\vartheta(\mathfrak p)^{6d}\) is \(E_1^d\); and \(\theta_{\mathfrak p}^{6d}=1\).

- \(t=6d\), \(d\ge1\), \(k=0\): \(Q^{6d-1}(Q-1)\sum_{m'\ge d}V^{m'}\) gives \(E_1^d(1-Q^{-1})/(1-V)\).
- \(t=6d\), \(k=1\), \(m'=d\): \(\theta_{\mathfrak p}\tau_1\tau_5Q^{6d-1}Q^{-w}\) gives \(E_1^dW\), since \(\tau_1\tau_5=Q\).
- \(t=6d+1\), \(d\ge0\), \(k=0\), \(m'=d\): the factor \(\gamma_2(\mathfrak p)\vartheta(\mathfrak p)\overline{\theta_{\mathfrak p}}\,\tau_1Q^{-1/2-\xi}\) times \(E_1^d\). Since \(\tau_1=Q^{1/2}\gamma_1(\mathfrak p)\) and \(\gamma_1\gamma_2\vartheta=-\eta\) at primes (Section 6 of Lesson 4), this is \(-D_1E_1^d\).
- \(t=6d+1\), \(k=1\), \(m'\ge d+1\): the same factor with \(\theta_{\mathfrak p}^{0}\) in place of \(\overline{\theta_{\mathfrak p}}\), times \((Q-1)Q^{-w}\sum_{m'\ge d+1}V^{m'-d}E_1^d\), gives \(-(Q-1)D_1E_1^dWV/(1-V)\).

Summing over \(d\) gives (4.1). \(\square\)

The proof shows why only theta exponents \(t\equiv0,1\pmod6\) contribute at a prime prime to \(u\): for \(t\equiv3,4\pmod6\) the admissible valuations \(J=t-1\) and \(J=t\) have the wrong residue modulo \(6\), and the remaining character sums vanish.

## 5. The correction and statement (H)

Define at every exterior prime
\[
\mathcal H_{u,\mathfrak p}=(1-V)\,\frac{1-W}{1-D_1}\,\mathcal F_{u,\mathfrak p},
\]
with \(W=D_1=0\) when \(\mathfrak p\mid uR\), and \(\mathcal H_u=\prod_{\mathfrak p\notin S}\mathcal H_{u,\mathfrak p}\). Consider the two regions where \(\operatorname{Re}\xi\ge0.998\) and, respectively,
\[
\begin{gathered}
\operatorname{Re}w\ge0.003,\quad\operatorname{Re}z\ge0.4,\\
\operatorname{Re}w\ge0.95,\quad\operatorname{Re}z\ge0.16,\quad(5.1)
\end{gathered}
\]
and their open neighbourhoods obtained by lowering each of the three bounds by \(10^{-5}\).

**Proposition 5.1** (the Euler product [OpenAI-029, Proposition 7.3]). For every \(u\in\mathcal U\),
\[
\begin{aligned}
&\mathcal F_u(\xi,w,z)\\
&\quad =\frac{\zeta_F^S(6z)\,L^S\bigl(w,\chi_\bullet(u)\bigr)}{L^S\bigl(\xi,\eta\overline{\chi_\bullet(u)}\bigr)}\\
&\qquad \,\mathcal H_u(\xi,w,z),\quad(5.2)
\end{aligned}
\]
first in absolute convergence and then as an identity of meromorphic functions on the two neighbourhoods. On them \(\mathcal H_u\) is holomorphic and \(|\mathcal H_u|\le C_\epsilon q_u^\epsilon\) for every \(\epsilon>0\), uniformly in all heights. If \(S\) contains every prime of norm at most a fixed constant \(N_0\), then \(\mathcal H_1\) is bounded and nowhere zero on both neighbourhoods.

*Proof.* *Primes not dividing \(u\).* On the neighbourhoods, \(|V|=Q^{-6\operatorname{Re}z}\), \(|W|=Q^{-\operatorname{Re}w}\), \(|D_1|=Q^{-\operatorname{Re}\xi}\) and \(|E_1|=Q^{4-6\operatorname{Re}\xi-6\operatorname{Re}z}\) are bounded away from \(1\) once \(Q\) exceeds a fixed constant. By (4.1), with \(\frac1{1-V}+\frac W{1-W}=\frac{1-WV}{(1-V)(1-W)}\),
\[
\begin{aligned}
&\mathcal H_{u,\mathfrak p}\big|_{E_1=0}-1\\
&\quad=\frac1{1-D_1}\bigl(D_1(W+V-WV)\\
&\qquad-WV-(Q-1)D_1(1-W)WV\bigr),
\end{aligned}
\]
and the terms with \(E_1\) change \(\mathcal H_{u,\mathfrak p}\) by \(O(|E_1|)\). Hence
\[
\begin{gathered}
\begin{aligned}
|\mathcal H_{u,\mathfrak p}-1|&\le C\bigl(|VW|+|D_1V|+|D_1W|\\
&\qquad+Q|D_1WV|+|E_1|\bigr)\\
&\le C\,Q^{-1-\delta},
\end{aligned}\\
\delta=\frac1{4000}.\quad(5.3)
\end{gathered}
\]
The exponents of \(Q\) are as follows. On the first region \(|D_1W|\le Q^{-1.001}\), and every other term is smaller; on the union of the two regions \(1-\operatorname{Re}\xi-\operatorname{Re}w-6\operatorname{Re}z\le-1.908\) and \(4-6\operatorname{Re}\xi-6\operatorname{Re}z\le-2.948\), the worst cases being in the second region. Lowering the bounds by \(10^{-5}\) leaves the margins \(0.00098\), \(0.90792\) and \(1.94788\) beyond the exponent \(-1\), each larger than \(\delta\).

*Primes dividing \(u\).* Here \(1\le j\le5\) and \(J\ge1\). The terms with \(t=0\) give \((1-V)^{-1}\), since \(k\ge1\) needs \(J=0\). The term \(t=1\), \(k=0\) vanishes, since \(T_1(p^J)=0\). By Lemma 3.1 the terms \(t=1\), \(k=1\) have total absolute value at most \(Q^{1-\operatorname{Re}\xi-\operatorname{Re}w}/(1-|V|)\), with exponent \(-0.001\) on the first region and \(-0.948\) on the second. For \(l\ge1\), apart from the factor \(V^{m'}\), the terms are bounded by a constant times \(Q\) to the power
\[
\begin{aligned}
&(2-3\operatorname{Re}\xi)\,l+(1/2-\operatorname{Re}\xi)\,e_0\\
&\quad +\max(0,1/2-\operatorname{Re}w),
\end{aligned}
\]
which is at most \(-0.497\) for \(l=1\), \(e_0=0\) on the first region, decreases by at least \(0.994\) with each further \(l\), and is smaller on the second region. After lowering the bounds by \(10^{-5}\) the savings remain above \(0.49\) and \(0.00098\). Summing the geometric series and multiplying by \(1-V\),
\[
\begin{gathered}
\mathcal H_{u,\mathfrak p}=1+O(Q^{-\delta})\\
(\mathfrak p\mid uR).\quad(5.4)
\end{gathered}
\]

*The product.* By (5.3) and \(\sum_{\mathfrak p}q_{\mathfrak p}^{-1-\delta}<\infty\), the product over \(\mathfrak p\nmid uR\) converges normally, to a bounded holomorphic function. By (5.4), the product over \(\mathfrak p\mid uR\) is at most \(\prod_{\mathfrak p\mid uR}(1+Cq_{\mathfrak p}^{-\delta})\le C_\epsilon q_u^\epsilon\): for \(q_{\mathfrak p}\) large each factor is at most \(q_{\mathfrak p}^\epsilon\), and the finitely many small primes contribute a constant. Multiplying the local factors, \(\prod_{\mathfrak p}(1-V)^{-1}=\zeta_F^S(6z)\), \(\prod_{\mathfrak p}(1-W)^{-1}=L^S(w,\chi_\bullet(u))\) and \(\prod_{\mathfrak p}(1-D_1)=L^S(\xi,\eta\overline{\chi_\bullet(u)})^{-1}\), which gives (5.2) where everything converges absolutely, and then on the neighbourhoods by analytic continuation.

*The case \(u=1\).* Every prime satisfies (5.3). The constant \(C\) there depends only on the regions, so there is \(N_0\) with \(CQ^{-1-\delta}\le\frac12\) for \(Q>N_0\). If \(S\) contains all primes of norm at most \(N_0\), every factor \(\mathcal H_{1,\mathfrak p}\) has a logarithm of absolute value at most \(2CQ^{-1-\delta}\); the sum of these logarithms converges absolutely and uniformly, and its exponential \(\mathcal H_1\) is bounded and nowhere zero. \(\square\)

The primes of norm at most \(N_0\) form the set reserved for this lesson in the definition of \(S\) in Lesson 2. Put
\[
\mathcal H_\eta(s)=\mathcal H_1\bigl(s,1,\tfrac16\bigr).
\tag{5.5}
\]

**Corollary 5.2** (statement (H) of Lesson 5). \(\mathcal H_\eta\) is holomorphic, bounded and nowhere zero on an open neighbourhood of the closed half-plane \(\operatorname{Re}s\ge0.998\), uniformly in the height.

*Proof.* The point \((w,z)=(1,1/6)\) lies in the second region of (5.1), and Proposition 5.1 applies. \(\square\)

At \(u=1\) the Euler product (5.2) contains \(\zeta_F^S(6z)\zeta_F^S(w)/L^S(\xi,\eta)\): the poles at \(z=1/6\) and \(w=1\) produce, after the contour shifts of Lessons 13 and 14, the main term \(c_0f_\eta(Z)\) of (P2) with \(f_\eta\) built from \(\mathcal H_\eta(s)/L^S(s,\eta)\).

## 6. Exercises

**6.1.** Compute \(C_{1,0}(J)\) and \(C_{1,1}(J)\) for all \(J\ge0\) directly from (2.1).

**6.2.** Verify \(\tau_1\tau_5=Q\) from Lemma 1.1 of Lesson 4.

**6.3.** Expand (4.1) to first order in \(V,W,D_1\) (with \(E_1=0\)) and identify the three Euler factors of (5.2).

**6.4.** At a prime \(\mathfrak p\mid uR\), show that \(\mathcal F_{u,\mathfrak p}\) has no term of first order in \(Q^{-\xi}\), and explain why \(L^S(\xi,\eta\overline{\chi_\bullet(u)})\) has the factor \(1\) at such a prime.

**6.5.** Check the numerical claims in the proof of Proposition 5.1: the exponents \(-1.001\), \(-1.908\), \(-2.948\), \(-0.497\), and the margins \(0.00098\), \(0.90792\), \(1.94788\).

## 7. Solutions

**6.1.** For \(t=1\), \(k=0\): \(C_{1,0}(J)=\sum_x\chi_{\mathfrak p}(x)\psi^\circ_{\mathfrak p}(p^Jx/p)\), which is \(\tau_1\) for \(J=0\) and \(T_1(p^J)=0\) for \(J\ge1\). For \(k=1\): \(J\ge1\) is needed, and \(C_{1,1}(J)=\tau_1T_0(p^{J-1})\), which is \(-\tau_1\) for \(J=1\) and \((Q-1)\tau_1\) for \(J\ge2\).

**6.2.** \(\tau_5=\sum_x\chi_{\mathfrak p}(x)^5\psi^\circ(x/p)=G(\overline{\chi_{\mathfrak p}})\), and Lemma 1.1 of Lesson 4 gives \(G(\chi)G(\overline\chi)=\chi(-1)Q=Q\).

**6.3.** To first order, (4.1) is \(1+V+W-D_1\), and \((1-V)^{-1}(1-W)^{-1}(1-D_1)\)\(=1+V+W-D_1+\dots\); these are the local factors of \(\zeta_F^S(6z)\), \(L^S(w,\chi_\bullet(u))\) and \(1/L^S(\xi,\eta\overline{\chi_\bullet(u)})\).

**6.4.** The only candidate is \(t=1\), \(k=0\), \(m'=0\), and it vanishes because \(J=j\ge1\) gives \(T_1(p^J)=0\). The character \(\eta\overline{\chi_\bullet(u)}\) vanishes at \(\mathfrak p\mid u\) by the unit mask, so its Euler factor there is \(1\).

**6.5.** On the first region \(-\operatorname{Re}\xi-\operatorname{Re}w\le-1.001\). On the second, \(1-0.998-0.95-0.96=-1.908\) and \(4-5.988-0.96=-2.948\); on the first, the same expressions are \(-2.401\) and \(-4.388\). For \(l=1\), \(2-2.994+0.497=-0.497\). Lowering the three bounds by \(10^{-5}\) raises the exponents by \(2\cdot10^{-5}\), \(8\cdot10^{-5}\) and \(12\cdot10^{-5}\), leaving \(1.00098-1\), \(1.90792-1\) and \(2.94788-1\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 7.3. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
