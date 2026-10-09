# Chebyshev rows and mixed moments

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds the determinants used in this course to prove that Catalan's constant

\[
G=\sum_{j\ge0}\frac{(-1)^j}{(2j+1)^2}
\]

is irrational, and proves their first property: if \(G\) were rational, every one of them would be a rational number. Each entry is a double integral against one of two kernels, and each such integral is a rational combination of \(1\), \(G\) and \(\zeta(2)\). The rows are polynomials made from Chebyshev polynomials. They are chosen so that two power series built from each row agree up to a high order at the origin; this agreement makes the \(\zeta(2)\) part of every entry cancel. The later lessons estimate the size of these determinants at every prime and at the real place.

We use the monomial integrals of Proposition 2.3 of [Small linear forms and Apéry's theorem](small-linear-forms-and-aperys-theorem.md), power series, and dominated convergence. A basic reference is [OpenAI-Catalan].

## 1. Parameters

Throughout, \(N\) is a positive integer, and we put

\[
n=48N,\quad a=11N,\quad b=7N,\quad g=q=4N,\quad h=2N,
\]
\[
L=n+a=n+b+q=59N,\quad C=L+g=63N,\quad H=C+h=65N,\quad A=a+2g=19N.
\]

The determinants will have size \(n\). The numbers \(b\) and \(q\) describe the columns, \(g\), \(h\) and \(C\) the rows, \(L\) is the order of agreement that cancels \(\zeta(2)\), and all row polynomials will have their monomials in degrees \(A\) to \(H-1\). Every one of these quantities is a fixed multiple of \(N\); the arithmetic of later lessons depends on these exact ratios.

## 2. Chebyshev polynomials and a half-angle variable

The **Chebyshev polynomials** \(T_d\) and \(U_d\) are defined by \(T_0=1\), \(T_1=x\), \(U_{-1}=0\), \(U_0=1\), and the common recurrence

\[
S_{d+1}(x)=2xS_d(x)-S_{d-1}(x).
\]

They have integer coefficients; \(T_d\) and \(U_d\) have degree \(d\) for \(d\ge0\), with leading coefficients \(2^{d-1}\) (for \(d\ge1\)) and \(2^d\).

**Lemma 2.1.** For every complex \(w\ne0\) and every \(d\ge0\), with \(x=(w+w^{-1})/2\),

\[
T_d(x)=\frac{w^d+w^{-d}}2,\qquad U_{d-1}(x)\,\frac{w-w^{-1}}2=\frac{w^d-w^{-d}}2.
\]

**Proof.** Both right sides satisfy the recurrence in \(d\), because \((w+w^{-1})(w^d\pm w^{-d})=(w^{d+1}\pm w^{-d-1})+(w^{d-1}\pm w^{-(d-1)})\), and they agree with the left sides for \(d=0,1\). \(\square\)

Write \(f(t)=\sqrt{1-t^2}\), with the positive root for \(-1<t<1\); near \(t=0\) it is the power series with \(f(0)=1\). Put

\[
w=\frac t{1+f}.
\]

Using \(f^2+t^2=1\) one checks \(1+w^2=2/(1+f)\), and then

\[
t=\frac{2w}{1+w^2},\qquad f=\frac{1-w^2}{1+w^2},\qquad \frac{w+w^{-1}}2=\frac1t,\qquad\frac{w^{-1}-w}2=\frac ft.
\tag{2.1}
\]

As a power series, \(w=t/2+O(t^3)\). The substitution \(w\mapsto w^{-1}\), which we write as a star, fixes \(t\) and changes the sign of \(f\), by (2.1).

Finally recall the binomial series

\[
\frac1{f(t)}=\sum_{l\ge0}c_lt^{2l},\qquad c_l=\frac1{4^l}\binom{2l}l,
\tag{2.2}
\]

valid for \(|t|<1\). We write \(c_z=0\) when \(z\) is not a nonnegative integer.

## 3. The rows

For \(0\le r<n\) put \(d=|r-g|\) and

\[
R_r=(1-t)^ht^{C-1}w^{r-g},\qquad P_r=\frac{R_r+R_r^*}2,\qquad D_r=\frac{t\,(R_r^*-R_r)}{2f}.
\tag{3.1}
\]

**Proposition 3.1** (the rows are integer polynomials). For \(0\le r<n\),

\[
P_r=(1-t)^ht^{C-1}T_d(1/t),\qquad D_r=\operatorname{sgn}(r-g)\,(1-t)^ht^{C-1}U_{d-1}(1/t).
\]

These are polynomials with integer coefficients, \(D_g=0\), and their monomials lie in the degrees

\[
\operatorname{supp}P_r\subseteq\{A,\dots,H-1\},\qquad\operatorname{supp}D_r\subseteq\{A+1,\dots,H-1\}.
\]

**Proof.** By (2.1) and Lemma 2.1, \((w^{r-g}+w^{g-r})/2=T_d(1/t)\). For \(r\ge g\), \((w^{g-r}-w^{r-g})/2=(w^{-d}-w^d)/2=U_{d-1}(1/t)\cdot(w^{-1}-w)/2=U_{d-1}(1/t)\,f/t\); for \(r<g\) the sign is reversed. This gives both formulas. The polynomial \(t^{C-1}T_d(1/t)\) has monomials in degrees \(C-1-d\) to \(C-1\), and \(t^{C-1}U_{d-1}(1/t)\) in degrees \(C-d\) to \(C-1\). Since \(0\le r\le n-1\) and \(g\le n-1-g\), we have \(d\le n-1-g\), so \(C-1-d\ge C-n+g=A\). Multiplication by \((1-t)^h\) raises the top degree to \(C-1+h=H-1\). \(\square\)

**Lemma 3.2** (Taylor contact). As power series in \(t\),

\[
\frac{tP_r}f-D_r=\frac{tR_r}f=O\bigl(t^{C+r-g}\bigr)=O(t^L).
\]

**Proof.** The first equality is (3.1). Since \(w=\frac t2(1+O(t^2))\), every integer power satisfies \(w^{r-g}=(t/2)^{r-g}(1+O(t^2))\), so \(tR_r/f\) starts in degree \(1+(C-1)+(r-g)\). As \(r\ge0\), this is at least \(C-g=L\). \(\square\)

## 4. Moments of an arcsine weight

On \((-1,1)\) consider the measure \(d\mu(t)=|t|\,dt/f(t)\), of total mass \(2\), and its moments

\[
m_i=\int_{-1}^1t^i\,d\mu(t)\qquad(i\ge0),\qquad m_{-1}=0.
\]

**Lemma 4.1.** \(m_i=0\) for odd \(i\), and \(m_i=2/((i+1)c_{i/2})\) for even \(i\). Equivalently \(m_0=2\) and \((i+1)m_i=i\,m_{i-2}\) for \(i\ge1\). In particular \(m_i\to0\).

**Proof.** For odd \(i\) the integrand is odd. For \(i\ge1\), integration by parts on \((0,1)\), with \(t(1-t^2)^{-1/2}=-\frac d{dt}\sqrt{1-t^2}\), gives

\[
\int_0^1\frac{t^{i+1}}{\sqrt{1-t^2}}\,dt=i\int_0^1t^{i-1}\sqrt{1-t^2}\,dt=i\int_0^1\frac{t^{i-1}}{\sqrt{1-t^2}}\,dt-i\int_0^1\frac{t^{i+1}}{\sqrt{1-t^2}}\,dt,
\]

which is the recurrence; \(m_0=2\int_0^1t(1-t^2)^{-1/2}dt=2\). The closed form satisfies the same recurrence because \(c_l/c_{l-1}=(2l-1)/(2l)\). Finally \(c_l\ge1/(2\sqrt l)\) for \(l\ge1\), by induction from the same ratio, so \(m_i\to0\). \(\square\)

## 5. Mixed moments

For integers \(i,j\ge0\) define

\[
M(i,j)=\int_{-1}^1\int_0^1\frac{t^is^j}{1-ts}\,ds\,d\mu(t),\qquad
Z(i,j)=\int_0^1\int_0^1\frac{t^is^j}{1-ts}\,ds\,dt,
\]

and extend both bilinearly to polynomial arguments: for polynomials \(P(t)\) and \(S(s)\), \(M(P,S)=\sum_{i,j}[t^i]P\,[s^j]S\,M(i,j)\), where \([t^i]P\) is the coefficient of \(t^i\).

**Lemma 5.1** (convergence and series). Both integrals converge absolutely, and

\[
M(i,j)=\sum_{u\ge0}\frac{m_{i+u}}{j+u+1},\qquad M(i,j)-M(i+1,j+1)=\frac{m_i}{j+1}.
\]

**Proof.** For \(0<v<1\), \(\int_0^1ds/(1-vs)=-\log(1-v)/v\), and \(-\log(1-v)/\sqrt{1-v^2}\) is integrable on \((0,1)\). Hence \(\iint(1-|t|s)^{-1}\,ds\,d\mu(t)<\infty\), and this dominates \(|t^is^j/(1-ts)|\) as well as every partial sum of \(\sum_u|t|^us^u\). Expanding \(1/(1-ts)=\sum_u(ts)^u\) and integrating termwise (dominated convergence) gives the series, and the second identity follows by comparing the series term by term. The assertion for \(Z\) is Proposition 2.3 of the first lesson. \(\square\)

Write \(K^-_d=M(d,0)\) and \(K^+_d=M(0,d)\) for the moments on the two boundary lines.

**Lemma 5.2** (boundary recurrences). For \(d\ge2\),

\[
dK^-_d=(d-1)K^-_{d-2}+m_{d-2}+m_{d-1},\qquad (d-1)K^+_d=(d-2)K^+_{d-2}+\frac2{d-1},
\]

and \(K^-_1=2\).

**Proof.** By Lemma 4.1, \(m_{k}=\frac k{k+1}m_{k-2}\) for every \(k\ge1\). For the first recurrence, the series of Lemma 5.1 gives

\[
dK^-_d-(d-1)K^-_{d-2}=\sum_{u\ge0}\frac{d\,m_{d+u}-(d-1)m_{d+u-2}}{u+1}=\sum_{u\ge0}\frac{m_{d+u-2}}{d+u+1}=\sum_{u\ge0}\bigl(m_{d+u-2}-m_{d+u}\bigr),
\]

where both steps use \(m_{d+u}=\frac{d+u}{d+u+1}m_{d+u-2}\). The last sum telescopes to \(m_{d-2}+m_{d-1}\), since \(m_v\to0\). The same computation with \(d=1\), without the term \((d-1)K^-_{d-2}\), gives \(K^-_1=m_{-1}+m_0=2\). For the second recurrence, shift the series of \(K^+_d\) by two:

\[
(d-1)K^+_d-(d-2)K^+_{d-2}=\sum_{u\ge2}\frac{(d-1)m_{u-2}-(d-2)m_u}{d+u-1}-(d-2)\Bigl(\frac{m_0}{d-1}+\frac{m_1}d\Bigr).
\]

Each summand equals \(m_{u-2}/(u+1)=m_{u-2}-m_u\), so the sum is \(m_0+m_1=2\), and the subtracted term is \(2(d-2)/(d-1)\). The difference \(2-2(d-2)/(d-1)\) is \(2/(d-1)\). \(\square\)

**Lemma 5.3** (the two transcendental starting values).

\[
K^-_0=K^+_0=M(0,0)=4G,\qquad K^+_1=M(0,1)=\frac{\pi^2}4=\frac32\zeta(2).
\]

**Proof.** Integrating in \(s\), \(M(0,0)=\int_{-1}^1(|t|/f)(-\log(1-t)/t)\,dt\). Splitting the interval and substituting \(t\mapsto-t\) on the negative half gives \(\int_0^1\log\frac{1+t}{1-t}\,\frac{dt}{\sqrt{1-t^2}}\). With \(t=\sin\theta\) and \(\frac{1+\sin\theta}{1-\sin\theta}=\tan^2(\frac\pi4+\frac\theta2)\), this becomes \(4\int_{\pi/4}^{\pi/2}\log\tan\phi\,d\phi=-4\int_0^{\pi/4}\log\tan v\,dv\). Finally, with \(x=\tan v\) and the geometric series of \(1/(1+x^2)\),

\[
\int_0^{\pi/4}\log\tan v\,dv=\int_0^1\frac{\log x}{1+x^2}\,dx=\sum_{k\ge0}(-1)^k\int_0^1x^{2k}\log x\,dx=-\sum_{k\ge0}\frac{(-1)^k}{(2k+1)^2}=-G;
\]

termwise integration is justified because the partial sums of the alternating series are bounded by \(1\) in absolute value.

For the second value, Lemma 5.1, Lemma 4.1 and \((2k+1)c_k=2(k+1)c_{k+1}\) give \(K^+_1=\sum_{k\ge0}m_{2k}/(2k+2)=\sum_{k\ge1}1/(2k^2c_k)\). The function \(y=(\arcsin x)^2\) satisfies \((1-x^2)y''-xy'=2\) with \(y(0)=y'(0)=0\). Substituting \(y=\sum_ka_kx^{2k}\) gives \(a_1=1\) and \((2k+2)(2k+1)a_{k+1}=4k^2a_k\), whose solution is \(a_k=1/(2k^2c_k)\); the series has radius of convergence \(1\) and, by uniqueness of the analytic solution of this initial value problem on \((-1,1)\), equals \((\arcsin x)^2\) there. Its coefficients are positive, so letting \(x\uparrow1\) gives \(\sum_k a_k=(\pi/2)^2\) by monotone convergence.

It remains to show \(\zeta(2)=\pi^2/6\). For \(0<\rho<1\) and \(0<x<\pi\),

\[
\sum_{k\ge1}\frac{\rho^k\sin kx}k=\operatorname{Im}\bigl(-\log(1-\rho e^{ix})\bigr),
\]

with the principal logarithm; the right side lies in \((-\pi/2,\pi/2)\), and as \(\rho\uparrow1\) it tends to \(-\arg(1-e^{ix})=(\pi-x)/2\), because \(1-e^{ix}=-2i\sin(x/2)\,e^{ix/2}\). Integrating over \((0,\pi)\), termwise for fixed \(\rho\), gives \(\sum_k\rho^k(1-\cos k\pi)/k^2=2\sum_{k\text{ odd}}\rho^k/k^2\); dominated convergence on the left and monotone convergence on the right give \(2\sum_{k\text{ odd}}k^{-2}=\int_0^\pi\frac{\pi-x}2\,dx=\frac{\pi^2}4\). Since \(\sum_{k\text{ odd}}k^{-2}=\frac34\zeta(2)\), we get \(\zeta(2)=\pi^2/6\). \(\square\)

The other moments follow from the recurrences. Let \(k^-_d\) and \(k^+_d\) be the rational numbers defined by the recurrences of Lemma 5.2 with the starting values

\[
k^-_0=k^+_0=k^+_1=0,\qquad k^-_1=2,
\]

and define \(M^0(i,j)\) by **diagonal reduction**:

\[
M^0(i,j)=\begin{cases}
k^-_{i-j}-\displaystyle\sum_{k=1}^j\frac{m_{i-j+k-1}}k,&i\ge j,\\[8pt]
k^+_{j-i}-\displaystyle\sum_{k=j-i+1}^j\frac{m_{k-(j-i)-1}}k,&i<j.
\end{cases}
\tag{5.1}
\]

With \(B^{(d)}_i=\sum_{k=1}^ik^{-d}\) and \(B^{(d)}_0=0\), put

\[
Z^0(i,j)=\begin{cases}-B^{(2)}_i,&i=j,\\[2pt] \dfrac{B^{(1)}_i-B^{(1)}_j}{i-j},&i\ne j.\end{cases}
\]

**Proposition 5.4** (decomposition of the moments). For all \(i,j\ge0\),

\[
M(i,j)=M^0(i,j)+4G\,c_{(i-j)/2}+\frac32\zeta(2)\,c_{(j-i-1)/2},\qquad Z(i,j)=Z^0(i,j)+[i=j]\,\zeta(2),
\]

where \([i=j]\) is \(1\) if \(i=j\) and \(0\) otherwise.

**Proof.** Iterating the diagonal identity of Lemma 5.1 \(\min(i,j)\) times moves \(M(i,j)\) to the boundary and produces exactly the sums in (5.1), with \(K^-_{i-j}\) or \(K^+_{j-i}\) in place of \(k^\mp\). It remains to compare \(K^\pm_d\) with \(k^\pm_d\). The differences \(K^\pm_d-k^\pm_d\) satisfy the homogeneous recurrences \(dy_d=(d-1)y_{d-2}\) and \((d-1)y_d=(d-2)y_{d-2}\). For the first, the solution with \(y_0=1\), \(y_1=0\) is \(y_d=c_{d/2}\), since \(c_{l}/c_{l-1}=(2l-1)/(2l)\); and the starting differences are \(K^-_0-k^-_0=4G\) and \(K^-_1-k^-_1=0\). For the second, the even chain dies at once (\(d=2\) gives \(y_2=0\)), while the odd chain with \(y_1=1\) is \(y_d=c_{(d-1)/2}\); the starting differences are \(4G\) at \(d=0\) and \(\frac32\zeta(2)\) at \(d=1\). Since diagonal reduction preserves \(i-j\), this gives the formula for \(M\); at \(i=j=0\) the two expressions for \(M(0,0)\) agree. The formula for \(Z\) is Proposition 2.3 of the first lesson, written with \(B^{(1)}\) and \(B^{(2)}\). \(\square\)

For the valuation estimates of the next lessons we record the boundary arrays explicitly. Put

\[
H^*_z=\begin{cases}c_{z/2},&z\ge0\text{ even},\\ \dfrac1{z\,c_{(z-1)/2}},&z\ge1\text{ odd},\end{cases}\qquad\text{so that}\qquad\frac{H^*_{z+2}}{H^*_z}=\frac{z+1}{z+2}.
\]

**Proposition 5.5** (explicit boundary arrays). For \(u\ge0\),

\[
k^-_u=\begin{cases}H^*_u\displaystyle\sum_{\substack{2\le z\le u\\ z\text{ even}}}\frac2{z^2(H^*_z)^2},&u\text{ even},\\[10pt]
H^*_u\displaystyle\sum_{\substack{1\le z\le u\\ z\text{ odd}}}\frac2z,&u\text{ odd},\end{cases}
\qquad
k^+_{u+1}=H^*_u\sum_{\substack{1\le z\le u\\ z\equiv u\ (2)}}\frac2{z^2H^*_z}.
\]

**Proof.** The ratio \(H^*_{z+2}/H^*_z\) follows from \(c_{l+1}/c_l=(2l+1)/(2l+2)\) in both parities. Dividing \(dk^-_d=(d-1)k^-_{d-2}+m_{d-2}+m_{d-1}\) by \(dH^*_d\) gives \(k^-_d/H^*_d=k^-_{d-2}/H^*_{d-2}+(m_{d-2}+m_{d-1})/(dH^*_d)\). By Lemma 4.1 the increment is \(2/(d^2(H^*_d)^2)\) for even \(d\) (only \(m_{d-2}\) survives) and \(2/d\) for odd \(d\) (only \(m_{d-1}\) survives). Summing from \(k^-_0/H^*_0=0\), respectively \(k^-_1/H^*_1=2\), gives the formula for \(k^-\). Similarly, with \(u=d-1\), dividing the plus recurrence by \(uH^*_u\) gives \(k^+_{u+1}/H^*_u=k^+_{u-1}/H^*_{u-2}+2/(u^2H^*_u)\), started from \(k^+_1=0\) and \(k^+_2=2=2/(1^2H^*_1)\). \(\square\)

## 6. The determinant and the cancellation of \(\zeta(2)\)

For \(0\le r<n\) and an integer \(j\ge0\), the **raw entry** is

\[
F_j(r)=M(P_r,j)-\frac32\,Z(D_r,j),
\]

where \(j\) stands for the monomial \(s^j\). The **filtered entries** use the polynomials \(s^{b+k}(1-s)^q\), \(0\le k<n\), and the determinant studied in this course is

\[
\Delta_N=\det_{0\le r,k<n}\Bigl(M\bigl(P_r,s^{b+k}(1-s)^q\bigr)-\frac32Z\bigl(D_r,s^{b+k}(1-s)^q\bigr)\Bigr).
\tag{6.1}
\]

Expanding \((1-s)^q\), the matrix in (6.1) is \(\mathcal F\mathcal T\), where \(\mathcal F\) is the \(n\times(n+q)\) matrix of raw columns \(F_j\), \(b\le j<L\), and \(\mathcal T\) is the integer matrix

\[
\mathcal T_{j,k}=(-1)^{j-b-k}\binom q{j-b-k}\qquad(b\le j<L,\ 0\le k<n).
\]

Indeed the raw indices used are \(j=b+k+v\) with \(0\le v\le q\), which range over \(b\le j\le b+n-1+q=L-1\).

**Proposition 6.1** (rationality). For \(b\le j<L\), every raw entry \(F_j(r)\) lies in \(\mathbb Q+\mathbb QG\). More precisely,

\[
F_j(r)=\sum_i[t^i]P_r\bigl(M^0(i,j)+4G\,c_{(i-j)/2}\bigr)-\frac32\sum_i[t^i]D_r\,Z^0(i,j).
\]

Consequently, if \(G\) is rational, then \(\Delta_N\) is rational for every \(N\).

**Proof.** By Proposition 5.4, the coefficient of \(\zeta(2)\) in \(F_j(r)\) is

\[
\frac32\Bigl(\sum_i[t^i]P_r\,c_{(j-i-1)/2}-[t^j]D_r\Bigr)=\frac32\,[t^j]\Bigl(\frac{tP_r}f-D_r\Bigr),
\]

because \(t/f=\sum_lc_lt^{2l+1}\) by (2.2), so that \([t^j]{}(tP_r/f)=\sum_i[t^i]P_r\,c_{(j-1-i)/2}\). By Lemma 3.2 this coefficient vanishes for \(j<L\). The remaining terms are the displayed ones, and \(\Delta_N\) is a polynomial with integer coefficients in the entries of \(\mathcal F\). \(\square\)

The point of the construction is visible here: without the contact of Lemma 3.2, each entry would also contain a multiple of \(\zeta(2)=\pi^2/6\), which is irrational, and rationality of \(G\) would not make \(\Delta_N\) rational. The next lessons show that, if \(G\) were rational, \(|\Delta_N|\) would be too large to be compatible with an upper bound obtained from (6.1) as an integral.

## 7. Exercises

**Exercise 7.1 (easy).** Compute \(T_2,T_3,U_1,U_2\) and verify Lemma 2.1 for \(d=2\).

**Exercise 7.2 (easy).** Compute \(m_0,m_2,m_4\) from Lemma 4.1, and check \(m_2=\int_{-1}^1t^2|t|(1-t^2)^{-1/2}dt\) directly with \(t=\sin\theta\).

**Exercise 7.3 (medium).** Compute \(k^-_2,k^-_3,k^+_2,k^+_3\) from the recurrences and from Proposition 5.5, and deduce \(M(2,0)=1+2G\) and \(M(0,3)=\frac12+\frac34\zeta(2)\).

**Exercise 7.4 (medium).** Show from (3.1) that \(P_r^2-\frac{f^2}{t^2}D_r^2=R_rR_r^*\), and compute \(R_rR_r^*\).

**Exercise 7.5 (hard).** Suppose the row exponent \(C-1\) in (3.1) were replaced by a smaller number \(C'-1\). Determine the largest raw index \(j\) for which the \(\zeta(2)\) part of \(F_j(r)\) vanishes for every row, and explain why the parameters must satisfy \(L\le C-g\).

## 8. Solutions

**7.1.** \(T_2=2x^2-1\), \(T_3=4x^3-3x\), \(U_1=2x\), \(U_2=4x^2-1\). With \(x=(w+w^{-1})/2\): \(2x^2-1=\frac{(w+w^{-1})^2}2-1=\frac{w^2+w^{-2}}2\).

**7.2.** \(m_0=2\), \(m_2=2/(3c_1)=4/3\), \(m_4=2/(5c_2)=16/15\). With \(t=\sin\theta\), \(m_2=2\int_0^{\pi/2}\sin^3\theta\,d\theta=2\cdot\frac23\).

**7.3.** From the recurrences: \(2k^-_2=k^-_0+m_0+m_1=2\), so \(k^-_2=1\); \(3k^-_3=2k^-_1+m_1+m_2=4+\frac43\), so \(k^-_3=\frac{16}9\); \(k^+_2=2\); \(2k^+_3=k^+_1+1=1\), so \(k^+_3=\frac12\). Proposition 5.5 agrees: \(H^*_2=c_1=\frac12\) gives \(k^-_2=\frac12\cdot\frac2{4\cdot\frac14}=1\); \(H^*_3=1/(3c_1)=\frac23\) gives \(k^-_3=\frac23(2+\frac23)=\frac{16}9\); \(k^+_3=H^*_2\cdot\frac2{4H^*_2}=\frac12\). Then \(M(2,0)=k^-_2+4Gc_1=1+2G\) and \(M(0,3)=k^+_3+\frac32\zeta(2)c_1=\frac12+\frac34\zeta(2)\).

**7.4.** \(P_r\pm\frac ftD_r\) equals \(R_r^*\) and \(R_r\) respectively, by (3.1); multiply. Then \(R_rR_r^*=(1-t)^{2h}t^{2C-2}\), since \(w^{r-g}w^{g-r}=1\).

**7.5.** The contact order becomes \(C'-g\), so the \(\zeta(2)\) part vanishes for \(j<C'-g\) and in general not at \(j=C'-g\) (row \(r=0\) has \(tR_0/f\) starting exactly there, with nonzero coefficient \(2^{g}\)). The filter uses raw indices up to \(L-1\), so cancellation for all of them requires \(L\le C'-g\).

## References

- [OpenAI-Catalan] OpenAI, Catalan's constant is irrational, preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf
