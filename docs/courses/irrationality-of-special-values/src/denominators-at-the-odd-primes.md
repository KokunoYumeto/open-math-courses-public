# Denominators at the odd primes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the arithmetic lower bound for the determinants \(\Delta_N\) of [Chebyshev rows and mixed moments](chebyshev-rows-and-mixed-moments.md). Assuming that Catalan's constant \(G\) is rational, it proves

\[
\liminf_{N\to\infty}\Bigl(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\Bigr)\ge-\frac{8609}{4608}-\Bigl(\frac12+\frac{505}{4608}\Bigr)\log2>-2.29084
\]

along every sequence of \(N\) with \(\Delta_N\ne0\), where \(n=48N\). The prime \(2\) was treated in [Denominators at the prime two](denominators-at-the-prime-two.md). At an odd prime \(p\) between \(2\sqrt H\) and \(H=65N\), every raw entry has at most \(p^2\) in its denominator. Writing indices in base \(p\), the entries multiplied by \(p^2\) reduce modulo \(p\) to a much smaller version of the same arrays. This identifies the leading residues of the columns, and shows that certain sums of two columns, and certain combinations of the columns near \(p\), have smaller denominators. Counting how many columns must keep the full denominator gives a loss function of \(p/N\), and the prime number theorem converts the sum of the losses into an integral.

We use Lemmas 1.1–1.4 of [Denominators at the prime two](denominators-at-the-prime-two.md) (Legendre's formula, Cauchy–Binet, minors and their transfer), the arrays and Propositions 5.4, 5.5 and 6.1 of [Chebyshev rows and mixed moments](chebyshev-rows-and-mixed-moments.md), and the prime number theorem in the form \(\theta(y)=\sum_{p\le y}\log p\sim y\), Theorem 3.1 of [The prime number theorem](course:NT-ZETA/NT-ZETA-09#3-from-an-average-to-the-number-of-primes). A basic reference is [OpenAI-Catalan].

## 1. Setting and a polynomial of degree p−1

Throughout, \(G\) is assumed rational, the parameters \(n,a,b,g=q,h,L,C,H,A\) are those of the rows lesson, and \(p\) is an odd prime with

\[
2\sqrt H<p\le H,\qquad p\nmid\operatorname{den}(G).
\]

As \(N\to\infty\), every prime factor of the fixed denominator of \(G\) eventually lies below \(2\sqrt H\). Note \(H<p^2/4\), so every index \(0\le z<H\) has exactly two base-\(p\) digits, \(z=Pp+r\) with \(0\le r<p\) and \(P<H/p<p/4\). Reduction modulo \(p\) always means reduction of an element of \(\mathbb Z_{(p)}\), the rationals with denominator prime to \(p\); a congruence below includes the assertion that both sides lie in \(\mathbb Z_{(p)}\).

In \(\mathbf F_p[t]\) put

\[
E(t)=(1-t^2)^{(p-1)/2}=\sum_{d=0}^{p-1}E_dt^d,\qquad\epsilon=(-1)^{(p-1)/2},
\]

and \(E_d=0\) outside \(0\le d<p\).

**Lemma 1.1.** For \(0\le d<p\), \(E_d\equiv c_{d/2}\pmod p\) if \(d\) is even and \(E_d=0\) if \(d\) is odd. Moreover \(E_{p-1-d}=\epsilon E_d\), and \(c_j\equiv(-1)^j\binom{(p-1)/2}j\pmod p\) for \(0\le j\le(p-1)/2\).

**Proof.** \(E_{2k}=(-1)^k\binom{s}k\) with \(s=(p-1)/2\). Modulo \(p\), \(\binom sk=\prod_{i<k}(s-i)/k!\equiv\prod_{i<k}(-\frac12-i)/k!=(-1)^k\frac{1\cdot3\cdots(2k-1)}{2^kk!}=(-1)^k\frac{(2k)!}{4^k(k!)^2}\), all denominators being units. This gives both congruences. Reversing coefficients, \(t^{p-1}E(1/t)=(t^2-1)^s=\epsilon E(t)\). \(\square\)

**Lemma 1.2** (Lucas). If \(x=x_1p+x_0\) and \(y=y_1p+y_0\) with digits \(0\le x_i,y_i<p\), then \(\binom xy\equiv\binom{x_1}{y_1}\binom{x_0}{y_0}\pmod p\).

**Proof.** In \(\mathbf F_p[X]\), \((1+X)^x=(1+X^p)^{x_1}(1+X)^{x_0}\), since \((1+X)^p=1+X^p\). Compare the coefficients of \(X^{y_1p+y_0}\); the base-\(p\) expansion of the exponent is unique. \(\square\)

## 2. Base-p digits of the moment arrays

Recall \(c_l=4^{-l}\binom{2l}l\), \(m_{z-1}=2H^*_z\) for odd \(z\) and \(m_{z-1}=0\) for even \(z\ge2\), and

\[
H^*_z=c_{z/2}\ (z\text{ even}),\qquad H^*_z=\frac1{zc_{(z-1)/2}}\ (z\text{ odd}),\qquad\frac{H^*_{z+2}}{H^*_z}=\frac{z+1}{z+2}.
\]

At an odd prime every \(c_l\) is \(p\)-integral, and \(c_l\) is a \(p\)-adic unit when \(2l<p\). In particular all quantities with indices below \(p/4\), such as \(H^*_P\), \(m_{P-1}\), \(k^\pm_P\) and \(M^0(i',j')\) with \(i',j'<p/4\), lie in \(\mathbb Z_{(p)}\); the arrays \(H^*\) at such indices are units.

**Lemma 2.1** (digits of \(H^*\)). Let \(0\le z<H\), \(z=Pp+r\).

1. If \(z\) is even and \(r\) is even, then \(H^*_z\equiv H^*_P\,c_{r/2}\pmod p\).
2. If \(z\) is even and \(r\) is odd, then \(v_p(H^*_z)=1\). Consequently, for even \(z\ge2\), \(v_p(zH^*_z)\in\{0,1\}\), and it equals \(1\) exactly when \(r=0\) or \(r\) is odd.
3. If \(z\) is odd, then \(1/H^*_z\in\mathbb Z_{(p)}\), and \(pH^*_z\equiv\epsilon\,c_{r/2}H^*_P\) if \(r\) is even, \(pH^*_z\equiv0\) if \(r\) is odd.

**Proof.** (1) Here \(P\) is even, and \(z/2=\frac P2p+\frac r2\) in base \(p\). Lucas gives \(\binom z{z/2}\equiv\binom P{P/2}\binom r{r/2}\), and Fermat gives \(4^{-z/2}\equiv4^{-P/2}4^{-r/2}\). (2) Here \(P\) is odd and \(z/2=\frac{P-1}2p+\frac{p+r}2\). Legendre's formula gives \(v_p\binom z{z/2}=\lfloor z/p\rfloor-2\lfloor z/(2p)\rfloor=P-(P-1)=1\), the terms with \(p^2\) vanishing since \(z<p^2\). For the consequence: if \(r\) is even and nonzero, \(z\) and \(H^*_z\) are units; if \(r=0\), \(v_p(z)=1\) and \(H^*_z\equiv H^*_P\) is a unit by (1).

(3) \(1/H^*_z=zc_{(z-1)/2}\) is \(p\)-integral. If \(r\) is odd, then \(P\) is even, \(p\nmid z\), and \((z-1)/2=\frac P2p+\frac{r-1}2\) has digits whose doubles do not carry, so \(c_{(z-1)/2}\) is a unit by Legendre's formula; hence \(H^*_z\) is a unit and \(pH^*_z\equiv0\). If \(r\) is even, then \(P\) is odd. At \(z=Pp\), Lucas applied to \(Pp-1=(P-1)p+(p-1)\) and \((Pp-1)/2=\frac{P-1}2p+\frac{p-1}2\) gives \(c_{(Pp-1)/2}\equiv c_{(P-1)/2}\,c_{(p-1)/2}\), and \(c_{(p-1)/2}\equiv\binom{p-1}{(p-1)/2}\equiv(-1)^{(p-1)/2}=\epsilon\) (as \(4^{(p-1)/2}\equiv1\)). So \(pH^*_{Pp}=1/(Pc_{(Pp-1)/2})\equiv\epsilon H^*_P\). Moving up by twos, \(pH^*_{Pp+r}=pH^*_{Pp}\prod_{0\le s<r,\ s\text{ even}}\frac{Pp+s+1}{Pp+s+2}\equiv\epsilon H^*_P\prod\frac{s+1}{s+2}=\epsilon H^*_Pc_{r/2}\), the factors being units since \(s+2\le r<p\). \(\square\)

**Lemma 2.2** (digits of the moments). For \(0\le z<H\) with \(z=Pp+r\),

\[
p\,m_{z-1}\equiv E_{p-1-r}\,m_{P-1}\pmod p.
\]

**Proof.** For odd \(z\), \(m_{z-1}=2H^*_z\) and \(m_{P-1}=2H^*_P\) (here \(P\) is odd when \(r\) is even). Lemma 2.1(3) gives \(pm_{z-1}\equiv2\epsilon c_{r/2}H^*_P=\epsilon E_rm_{P-1}=E_{p-1-r}m_{P-1}\) for even \(r\), and \(0\equiv E_{p-1-r}m_{P-1}\) for odd \(r\), since then \(p-1-r\) is odd. For even \(z\), \(m_{z-1}=0\), and either \(r\) is odd (so \(E_{p-1-r}=0\)) or \(P\) is even (so \(m_{P-1}=0\)). For \(z=0\) both sides vanish. \(\square\)

In particular \(v_p(m_x)\ge-1\) for \(0\le x<H\).

**Lemma 2.3** (digits of the boundary arrays). For \(0\le u<H\), \(u=Pp+r\),

\[
p^2k^-_u\equiv E_{p-1-r}\,k^-_P,\qquad p^2k^+_{u+1}\equiv E_r\,k^+_{P+1}\pmod p.
\]

**Proof.** We use the explicit formulas of Proposition 5.5 of the rows lesson.

*\(k^-\), \(u\) odd.* \(p^2k^-_u=(pH^*_u)\sum_{z\le u,\ z\text{ odd}}2p/z\). Both factors are \(p\)-integral, by Lemma 2.1(3) and since \(p^2\nmid z\). In the sum only \(z=mp\) with \(m\) odd survive modulo \(p\), contributing \(2/m\), and \(mp\le u\) means \(m\le P\). If \(r\) is odd, the prefactor vanishes and so does \(E_{p-1-r}\). If \(r\) is even, \(P\) is odd and \(pH^*_u\equiv\epsilon c_{r/2}H^*_P=E_{p-1-r}H^*_P\), so \(p^2k^-_u\equiv E_{p-1-r}H^*_P\sum_{m\le P,\ m\text{ odd}}2/m=E_{p-1-r}k^-_P\).

*\(k^-\), \(u\) even.* Write \(p^2k^-_u=H^*_u\sum_{2\le z\le u,\ z\text{ even}}2\bigl(p/(zH^*_z)\bigr)^2\). By Lemma 2.1(2) each \(p/(zH^*_z)\) is \(p\)-integral, and it is \(0\) modulo \(p\) unless \(z\bmod p\) is \(0\) or odd. These surviving even \(z\) are exactly the numbers \(z=mp-\lambda\) with \(m\) even and \(\lambda\in\{0,2,\dots,p-1\}\): an even \(z\) with odd residue lies just below the even multiple \(mp\), at an even distance \(\lambda\in\{2,\dots,p-1\}\), and the multiple itself gives \(\lambda=0\). If \(r\) is odd, then \(v_p(H^*_u)=1\) and \(E_{p-1-r}=0\), so both sides vanish. If \(r\) is even, then \(P\) is even, \(H^*_u\equiv H^*_Pc_{r/2}=H^*_PE_r\), and the surviving \(z\le u\) form the complete blocks \(m=2,4,\dots,P\): the block of \(m=P\) ends at \(Pp\le u\), and the next block starts at \((P+1)p+1>u\). Within a block, \(p/(mpH^*_{mp})\equiv1/(mH^*_m)\) by Lemma 2.1(1), and each step from \(z\) to \(z-2\) multiplies \(p/(zH^*_z)\) by \((z-1)/(z-2)\equiv(\lambda+1)/(\lambda+2)\), where \(z=mp-\lambda\). Hence \(p/(zH^*_z)\equiv c_{\lambda/2}/(mH^*_m)\), and the block contributes \(\frac{2}{m^2(H^*_m)^2}\sum_{j=0}^{(p-1)/2}c_j^2\). By Lemma 1.1 and Vandermonde's identity, \(\sum_jc_j^2\equiv\sum_j\binom{(p-1)/2}j^2=\binom{p-1}{(p-1)/2}\equiv\epsilon\). Therefore \(p^2k^-_u\equiv E_rH^*_P\cdot\epsilon\sum_{m\le P\text{ even}}\frac2{m^2(H^*_m)^2}=E_{p-1-r}k^-_P\).

*\(k^+\), \(u\) even.* \(p^2k^+_{u+1}=H^*_u\sum_{z\le u,\ z\text{ even}}2p^2/(z^2H^*_z)\). Since \(v_p(H^*_z)\le1\), terms with \(p\nmid z\) vanish modulo \(p\); at \(z=mp\) (\(m\) even) the term is \(2/(m^2H^*_{mp})\equiv2/(m^2H^*_m)\). With \(H^*_u\equiv E_rH^*_P\) for even \(r\), and \(v_p(H^*_u)=1\), \(E_r=0\) for odd \(r\), this gives \(E_rk^+_{P+1}\).

*\(k^+\), \(u\) odd.* \(p^2k^+_{u+1}=(pH^*_u)\sum_{z\le u,\ z\text{ odd}}2p/(z^2H^*_z)\). Since \(1/H^*_z\) is integral, only \(z=mp\) (\(m\) odd) survive, contributing \(2/(m^2\,pH^*_{mp})\equiv2\epsilon/(m^2H^*_m)\). With \(pH^*_u\equiv\epsilon c_{r/2}H^*_P\) for even \(r\) (and \(0\) for odd \(r\)), the factors \(\epsilon\) cancel and we obtain \(E_rk^+_{P+1}\). \(\square\)

## 3. The digit reduction

**Proposition 3.1** (digit reductions). For \(0\le i,j<H\) put

\[
\ell=j\bmod p,\quad d=(j-i-1)\bmod p,\quad i'=\frac{i+1+d-\ell}p-1,\quad j'=\Bigl\lfloor\frac jp\Bigr\rfloor,
\]

with \(0\le\ell,d<p\). Then \(i'\ge-1\), and with the convention \(M^0(-1,j')=k^+_{j'+1}\),

\[
p^2M^0(i,j)\equiv E_d\,M^0(i',j')\pmod p,\qquad
p^2Z^0(i,j)\equiv\begin{cases}Z^0(\lfloor i/p\rfloor,j'),&i\equiv j\pmod p,\\0,&i\not\equiv j\pmod p.\end{cases}
\]

**Proof.** *Case \(i\ge j\).* Put \(u=i-j=Pp+r\). Then \(d=p-1-r\) and \(i'=j'+P\). By diagonal reduction, \(M^0(i,j)=k^-_u-\sum_{k=1}^jm_{u+k-1}/k\). After multiplication by \(p^2\), a term with \(p\nmid k\) vanishes modulo \(p\) because \(v_p(m_x)\ge-1\). For \(k=mp\), Lemma 2.2 with \(z=u+mp=(P+m)p+r\) gives \(p^2m_{u+mp-1}/(mp)\equiv E_{p-1-r}m_{P+m-1}/m\), and \(mp\le j\) means \(m\le j'\). With Lemma 2.3,

\[
p^2M^0(i,j)\equiv E_{p-1-r}\Bigl(k^-_P-\sum_{m=1}^{j'}\frac{m_{P+m-1}}m\Bigr)=E_dM^0(j'+P,j').
\]

*Case \(i<j\).* Put \(u=j-i-1=Pp+r\). Then \(d=r\) and \(i'=j'-P-1\). Now \(M^0(i,j)=k^+_{u+1}-\sum_{k=u+2}^jm_{k-u-2}/k\). For \(k=mp\), Lemma 2.2 with \(z=mp-u-1=(m-P-1)p+(p-1-r)\) gives the reduced term \(E_rm_{m-P-2}/m\); the possible first multiple \(m=P+1\) contributes \(m_{-1}=0\), so the reduced sum runs over \(P+2\le m\le j'\). With Lemma 2.3 this is \(E_r\) times the diagonal reduction of \(M^0(j'-P-1,j')\). If \(i'=-1\), then \(j'=P\), the sum is empty, and the value is \(E_rk^+_{P+1}=E_rM^0(-1,j')\). In both cases \(i'=\lfloor(i-\ell)/p\rfloor\ge-1\), and the reduced indices are below \(p/4\), so the right side is integral.

*The array \(Z^0\).* Put \(I=\lfloor i/p\rfloor\), \(J'=j'\). Since \(i,j<p^2\), the harmonic sums satisfy \(pB^{(1)}_i\equiv B^{(1)}_I\) and \(p^2B^{(2)}_i\equiv B^{(2)}_I\): only the terms \(k=mp\) survive. The diagonal case follows. If \(i\not\equiv j\), then \(i-j\) is a unit and \(p^2Z^0(i,j)=p\cdot p(B^{(1)}_i-B^{(1)}_j)/(i-j)\equiv0\). If \(i\equiv j\) and \(i\ne j\), then \(i-j=p(I-J')\) with \(0<|I-J'|<p\), and \(p^2Z^0(i,j)=p(B^{(1)}_i-B^{(1)}_j)/(I-J')\equiv Z^0(I,J')\). \(\square\)

## 4. Leading residues and paired columns

For a residue \(0\le\ell<p\) define, for the rows \(r\), the vectors over \(\mathbf F_p\)

\[
P'_u=\bigl([t^{(u+1)p+\ell}]\,tP_r(t)E(t)\bigr)_r\ (u\ge-1),\qquad D'_u=\bigl([t^{up+\ell}]\,D_r(t)\bigr)_r\ (u\ge0).
\]

**Proposition 4.1** (leading layer). Every raw column lies in \(p^{-2}\mathbb Z_{(p)}^n\), and for \(j=kp+\ell\) in the range of raw columns,

\[
X_j:=p^2F_j\bmod p=\sum_{u\ge-1}P'_u\,M^0(u,k)-\frac32\sum_{u\ge0}D'_u\,Z^0(u,k).
\]

**Proof.** By Proposition 6.1 of the rows lesson, \(F_j(r)=\sum_i[t^i]P_r\bigl(M^0(i,j)+4Gc_{(i-j)/2}\bigr)-\frac32\sum_i[t^i]D_rZ^0(i,j)\). The \(G\) term is \(p\)-integral, since the \(c\)'s are and \(p\nmid\operatorname{den}G\), so it disappears after multiplication by \(p^2\). In the \(M^0\) term, Proposition 3.1 attaches to each row degree \(i\) the unique pair \((d,i')\) with \(i+1+d=(i'+1)p+\ell\); collecting by \(i'\) gives \(\sum_{d}E_d[t^{(i'+1)p+\ell-1-d}]P_r=[t^{(i'+1)p+\ell}]{}(tP_rE)\). In the \(Z^0\) term only \(i=up+\ell\) survive, giving \(D'_u\). \(\square\)

When \(\ell\ge H-2p\), the degree bounds \(\deg(tP_rE)\le H+p-1\) and \(\deg D_r<H\) show that \(P'_u\) and \(D'_u\) vanish for \(u>1\). The arrays at small indices are

\[
M^0(u,0)=0,\,0,\,2\quad(u=-1,0,1),\qquad M^0(u,1)=2,\,0,\,-2,\qquad Z^0(u,0)=0,\,1\quad(u=0,1),\qquad Z^0(u,1)=1,\,-1,
\]

as one reads off from \(k^-_0=k^+_1=0\), \(k^-_1=k^+_2=2\), \(m_0=2\) and the definition of \(Z^0\). Hence, putting

\[
V_\ell=2P'_1-\frac32D'_1,\qquad U_\ell=2P'_{-1}-\frac32D'_0,
\]

we get, whenever the columns exist and \(\ell\ge H-2p\),

\[
X_\ell=V_\ell,\qquad X_{p+\ell}=U_\ell-V_\ell.
\tag{4.1}
\]

Since \(tP_r\) and \(D_r\) have no monomials below degree \(A+1\), \(U_\ell=0\) for \(\ell\le A\).

**Proposition 4.2** (paired columns). If \(2\sqrt H<p\le H/2\), put \(d_0=\bigl(\min(p,L-p,A)-\max(b,H-2p)\bigr)_+\). Then

\[
v_p(\Delta_N)\ge-2n+(d_0-q)_+,
\]

and the same bound holds for every full minor of the raw matrix.

**Proof.** For each \(\ell\) with \(\max(b,H-2p)\le\ell<\min(p,L-p,A)\), both \(F_\ell\) and \(F_{p+\ell}\) are raw columns, and by (4.1) the sum \(F_{p+\ell}+F_\ell\) has leading residue \(U_\ell=0\), so it lies in \(p^{-1}\mathbb Z_{(p)}^n\). Replacing each \(F_{p+\ell}\) by this sum is an integral column operation with integral inverse, and the \(d_0\) pairs are disjoint because \(\ell<p\). In the new pool, \(d_0\) columns lie in \(p^{-1}\mathbb Z_{(p)}^n\) and all others in \(p^{-2}\mathbb Z_{(p)}^n\). A choice of \(n\) of the \(n+q\) columns omits at most \(q\) of the improved ones, so every full minor of the new pool has valuation at least \(-2n+(d_0-q)_+\), by Lemma 1.3 of the previous lesson. Lemma 1.4 there transfers this to the raw matrix and to \(\Delta_N\). \(\square\)

## 5. Primes above H/2: the central layer

Now let \(H/2<p\le H\), and put \(K=L-p\) and \(J=H-p\), so \(K<J<p\). Call a raw column \(F_j\) **central** if \(b\le j<\min(p,L)\) and \(j\ge J\).

**Lemma 5.1** (central layer). For every central column, \(pF_j\in\mathbb Z_{(p)}^n\) and

\[
pF_j\equiv-\sum_{0\le\ell<J}\frac{V_\ell}{j-\ell}\pmod p,
\]

where \(V_\ell\) is the vector of (4.1) for the residue \(\ell\); all denominators \(j-\ell\) are units.

**Proof.** For a row degree \(0\le i<H\) we have \(i-j\le H-1-J=p-1\) and \(j-i<p\), so the starting value \(k^-_{i-j}\) or \(k^+_{j-i}\) of the diagonal reduction has index below \(p\) and is \(p\)-integral. Both cases of diagonal reduction can be written as the starting value minus \(\sum_{0\le\ell<\min(i,j)}m_{i-\ell-1}/(j-\ell)\), with \(1\le j-\ell<p\). By Lemma 2.2, \(p\,m_{i-\ell-1}\not\equiv0\) requires \(p\le i-\ell<2p\), and then \(p\,m_{i-\ell-1}\equiv2E_{2p+\ell-1-i}\). Such \(\ell\) satisfy \(\ell\le i-p<J\le j\), so the sum is never truncated, and collecting over \(i\) gives \(p\,M^0(P_r,j)\equiv-\sum_{\ell<J}2[t^{2p+\ell}]{}(tP_rE)/(j-\ell)=-\sum_\ell2P'_1/(j-\ell)\). For \(Z^0(i,j)\), the harmonic sums have a pole only when \(i\ge p\), that is \(i=p+\ell\) with \(0\le\ell<J\); then \(i-j\equiv\ell-j\) is a unit (as \(j\ge J>\ell\)), and \(pZ^0(p+\ell,j)\equiv1/(\ell-j)\). This gives \(-\frac32\sum_\ell D'_1/(\ell-j)\). The \(G\) term is again integral. Adding, \(pF_j\equiv-\sum_\ell(2P'_1-\frac32D'_1)/(j-\ell)\). \(\square\)

**Lemma 5.2** (elimination over the local integers). For \(H/2<p\le H\) define

\[
R=K_++(K-A)_++\bigl(J-\max(b,K)\bigr)_+,\qquad S=\bigl(\min(A,K)-b\bigr)_++\bigl(\min(b,J)-\max(0,K)\bigr)_+.
\]

Then every full raw minor, and hence \(\Delta_N\), satisfies \(v_p\ge-\min(2n,\ n+R,\ 2R+S)\).

**Proof.** The noncentral raw columns are the **high** columns \(F_{p+\ell}\), \(0\le\ell<K\), and the **low** columns \(F_\ell\), \(b\le\ell<J\). For a low column, (4.1) applies (as \(H-2p<0\)): its leading residue is \(V_\ell\). For a high column it is \(U_\ell-V_\ell\).

*Pairs.* For \(b\le\ell<\min(A,K)\), keep the low column and replace the high one by \(F_{p+\ell}+F_\ell\), whose leading residue is \(U_\ell=0\); there are \(B=(\min(A,K)-b)_+\) such pair sums, in \(p^{-1}\mathbb Z_{(p)}^n\). All other noncentral columns are kept as they are, in \(p^{-2}\mathbb Z_{(p)}^n\); their number is \(K_++(J-b)_+-B\), which equals \(R\) (check the four cases \(K\le0\), \(0<K\le b\), \(b<K\le A\), \(K>A\), using \(K<J\): the values are \((J-b)_+\), \(K+(J-b)_+\), \(J\) and \(K+J-A\)).

*Representatives.* These kept columns supply a representative of \(\pm V_\ell\) for every \(0\le\ell<J\) outside

\[
\mathcal E=\{\ell:\max(0,K)\le\ell<\min(b,J)\},\qquad e=|\mathcal E|.
\]

Indeed, for \(b\le\ell<J\) the low column has residue \(V_\ell\); for \(0\le\ell<\min(b,K)\) the unpaired high column has residue \(U_\ell-V_\ell=-V_\ell\), since \(\ell<b<A\). Choose such a column \(Y_\ell\) and \(\sigma_\ell=\pm1\) with \(p^2Y_\ell\equiv\sigma_\ell V_\ell\).

*Shear.* For each central \(j\), choose \(a_{\ell j}\in\mathbb Z_{(p)}\) reducing to \(\sigma_\ell/(j-\ell)\), and replace \(F_j\) by \(C_j=F_j+p\sum_{\ell<J,\ \ell\notin\mathcal E}a_{\ell j}Y_\ell\). This integral shear has an integral inverse and fixes all other columns. Since \(p^2Y_\ell\in\mathbb Z_{(p)}^n\), the new column lies in \(p^{-1}\mathbb Z_{(p)}^n\), and by Lemma 5.1

\[
pC_j\equiv-\sum_{\ell\in\mathcal E}\frac{V_\ell}{j-\ell}\pmod p.
\]

*Rank.* Let \(c\) be the number of central columns, and \(\varphi:\mathbf F_p^c\to\mathbf F_p^n\) the map sending a coefficient vector to the combination of the residues \(pC_j\bmod p\). Its image lies in the span of the \(e\) vectors \(V_\ell\), \(\ell\in\mathcal E\), so its rank \(d\) is at most \(\min(c,e)\). Choose a basis of \(\mathbf F_p^c\) whose last \(c-d\) vectors span \(\ker\varphi\), and lift its matrix to \(W\) with entries in \(\mathbb Z_{(p)}\); \(\det W\) is a unit, so \(W\) is invertible over \(\mathbb Z_{(p)}\). Changing the central columns by \(W\) leaves at most \(d\) of them in \(p^{-1}\mathbb Z_{(p)}^n\); the others have residue \(0\) after multiplication by \(p\), so they are integral.

*Count.* The final pool has \(R\) columns with possible denominator \(p^2\), at most \(B+d\le B+e=S\) with possible denominator \(p\), and integral remaining columns. A full minor using \(r\) columns of the first kind and \(s\) of the second has valuation at least \(-(2r+s)\), and \(2r+s\le\min(2n,n+R,2R+S)\) because \(r+s\le n\), \(r\le R\), \(s\le S\). Lemma 1.4 of the previous lesson transfers the bound back to the raw minors and to \(\Delta_N\). \(\square\)

## 6. The finite-place lower bound

**Proposition 6.1.** Assume \(G\) rational. Along every sequence \(N\to\infty\) with \(\Delta_N\ne0\),

\[
\liminf_{N\to\infty}\Bigl(\frac{\log|\Delta_N|}{n^2}-\frac12\log2\Bigr)\ge-\frac{8609}{4608}-\Bigl(\frac12+\frac{505}{4608}\Bigr)\log2>-2.29084.
\]

**Proof.** *The loss function.* Put \(x=p/N\). For \(p\le H/2\), i.e. \(x\le65/2\), Proposition 4.2 gives \(v_p(\Delta_N)\ge-N\,\mathrm d(x)\) with \(\mathrm d(x)=96-\bigl(d_0/N-4\bigr)_+\), where

\[
\frac{d_0}N=\bigl(\min(x,59-x,19)-\max(7,65-2x)\bigr)_+=\begin{cases}0,&0\le x\le23,\\2x-46,&23\le x\le29,\\12,&29\le x\le65/2.\end{cases}
\]

For \(x>65/2\), Lemma 5.2 gives \(v_p\ge-N\,\mathrm d(x)\) with \(\mathrm d(x)=\min(96,48+R/N,2R/N+S/N)\), where \(K/N=59-x\), \(J/N=65-x\), and

\[
\begin{array}{c|cc}
x&R/N&S/N\\\hline
[65/2,40]&105-2x&12\\
[40,52]&65-x&52-x\\
[52,58]&117-2x&x-52\\
[58,59]&59-x&6\\
[59,65]&0&65-x
\end{array}
\]

Combining, \(\mathrm d\) is continuous, vanishes for \(x\ge65\), and is given piecewise by

\[
\begin{array}{c|c|c}
x&\mathrm d(x)&\int\mathrm d\\\hline
[0,25]&96&2400\\
[25,29]&146-2x&368\\
[29,65/2]&88&308\\
[65/2,69/2]&153-2x&172\\
[69/2,40]&222-4x&803/2\\
[40,58]&182-3x&630\\
[58,59]&124-2x&7\\
[59,65]&65-x&18
\end{array}
\qquad\int_0^{65}\mathrm d(x)\,dx=\frac{8609}2.
\]

*Small and large primes.* At any odd prime, Lemma 1.1 of the previous lesson gives \(0\le v_p\binom{2l}l\le1+\log H/\log p\) for \(2l\le H\). The explicit formulas for \(H^*_z\), \(m_i\), \(k^\pm_d\), \(Z^0\) and diagonal reduction then give, with an absolute constant \(C_0\),

\[
v_p\bigl(F_j(r)\bigr)\ge-C_0\Bigl(1+\frac{\log H}{\log p}\Bigr)-v_p(\operatorname{den}G),
\]

since each entry is built from boundedly many factors with such valuations, and sums cause no further loss. Hence \(v_p(\Delta_N)\ge-n\bigl(C_0(1+\log H/\log p)+v_p(\operatorname{den}G)\bigr)\), and the total over odd \(p\le2\sqrt H\), weighted by \(\log p\), is \(O(n\sqrt H\log H+n\log\operatorname{den}G)=o(n^2)\). For \(p>H\), all denominators involve only primes at most \(H\) and the fixed primes of \(\operatorname{den}G\), so \(v_p(\Delta_N)\ge0\) for large \(N\).

*The prime number theorem.* We claim

\[
\frac1N\sum_{p\le65N}\mathrm d(p/N)\log p\longrightarrow\int_0^{65}\mathrm d(x)\,dx.
\]

For a partition \(0=x_0<\dots<x_k=65\), the prime number theorem gives \((\theta(Nx_i)-\theta(Nx_{i-1}))/N\to x_i-x_{i-1}\). The sum lies between the corresponding lower and upper step sums of \(\mathrm d\), up to \(O(k\log N/N)\) for primes at partition points, and the difference of these step sums tends to zero with the mesh because \(\mathrm d\) is uniformly continuous. Removing \(p=2\) and \(p\le2\sqrt H\) from this sum costs \(o(1)\), as \(\mathrm d\le96\) and \(\theta(2\sqrt H)=O(\sqrt N\log N)\).

*Conclusion.* By the product formula (1.1) of the previous lesson,

\[
\log|\Delta_N|=\sum_pv_p(\Delta_N)\log p\ge-N^2\Bigl(\frac{8609}2+o(1)\Bigr)+v_2(\Delta_N)\log2-o(n^2).
\]

With \(n^2=2304N^2\) and Proposition 4.1 of the previous lesson, \(\log|\Delta_N|/n^2\ge-\frac{8609}{4608}-\frac{505}{4608}\log2-o(1)\). Subtract \(\frac12\log2\). For the numerical comparison, the series \(\log2=2\sum_{j\ge0}3^{-(2j+1)}/(2j+1)\) with its positive geometric tail gives

\[
\log2\le2\sum_{j=0}^5\frac{3^{-(2j+1)}}{2j+1}+\frac{2\cdot3^{-13}}{13(1-3^{-2})}<0.693149,
\]

so the constant exceeds \(-\frac{8609}{4608}-\frac{2809}{4608}\cdot0.693149=-\frac{10556055541}{4608000000}>-2.29084\). \(\square\)

## 7. Exercises

**Exercise 7.1 (easy).** For \(p=7\), compute \(E(t)=(1-t^2)^3\) modulo \(7\) and check Lemma 1.1.

**Exercise 7.2 (easy).** Verify \(\int_{25}^{29}(146-2x)\,dx=368\) and \(\int_{69/2}^{40}(222-4x)\,dx=803/2\), and add up the table.

**Exercise 7.3 (medium).** Check the formula \(d_0/N\) of Section 6 on the three ranges, and explain why only \((d_0/N-4)_+\) improves a full minor.

**Exercise 7.4 (medium).** Prove the congruence \(\sum_{j=0}^{(p-1)/2}c_j^2\equiv(-1)^{(p-1)/2}\pmod p\) for \(p=5\) and \(p=7\) by direct computation.

**Exercise 7.5 (hard).** Explain why, at a prime \(p>L\) with \(p\le H\), all raw columns are central, and compute \(R\) and \(S\) in that case. What happens at \(p=H\)?

## 8. Solutions

**7.1.** \((1-t^2)^3=1-3t^2+3t^4-t^6\), with coefficients \(1,4,3,6\pmod7\). Modulo \(7\): \(c_1=\frac12\equiv4\); \(c_2=\frac38\equiv3\), since \(8\equiv1\); \(c_3=\frac5{16}\equiv5\cdot2^{-1}\equiv5\cdot4\equiv6\), since \(16\equiv2\). These match. Also \(\epsilon=(-1)^3=-1\), and indeed \(E_{6-d}=-E_d\): \(E_6=-1=-E_0\) and \(E_4=3=-E_2\).

**7.2.** \(\int_{25}^{29}(146-2x)dx=146\cdot4-(29^2-25^2)=584-216=368\). \(\int_{34.5}^{40}(222-4x)dx=222\cdot5.5-2(1600-1190.25)=1221-819.5=401.5\). The total is \(2400+368+308+172+401.5+630+7+18=4304.5=8609/2\).

**7.3.** For \(x\le23\): \(\max(7,65-2x)\ge19\ge\min(x,59-x,19)\), so \(d_0=0\). For \(23\le x\le29\): \(\min=19\) (as \(x\ge19\) and \(59-x\ge30\)) and \(\max=65-2x\), giving \(2x-46\). For \(29\le x\le32.5\): \(\max=7\) and \(\min=19\), giving \(12\). A full minor omits at most \(q=4N\) of the \(n+q\) raw columns, so it contains at least \(d_0-q\) improved columns.

**7.4.** \(p=5\): \(c_0+c_1^2+c_2^2=1+\frac14+\frac9{64}\); modulo \(5\), \(\frac14\equiv4\) and \(\frac9{64}\equiv4\cdot4^{-1}=1\), total \(6\equiv1=(-1)^2\). \(p=7\): \(c_1\equiv4\), \(c_2\equiv3\), \(c_3\equiv6\), so \(1+16+9+36=62\equiv6\equiv-1=(-1)^3\).

**7.5.** If \(p\ge L\), there are no raw columns \(j\ge p\), so no high columns; \(K=L-p\le0\). Every raw column \(j\in[b,L)\) has \(j<p\), and \(j\ge J=H-p\) because \(H-p\le H-L=6N<b=7N\). So all \(n+q\) raw columns are central, \(R=(J-\max(b,K))_+=0\) and \(S=(\min(b,J)-0)_+=J=H-p\). Lemma 5.2 gives the loss \(\min(2n,\,n+R,\,2R+S)=\min(2n,\,n,\,H-p)=H-p\), since \(H-p\le6N<n\). At \(p=H\) the loss is \(0\): every raw column is integral.

## References

- [OpenAI-Catalan] OpenAI, Catalan's constant is irrational, preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf
