# Effective lower bounds II: proof of Baker's theorem

*Draft. Public domain (CC0).*

A sufficiently small algebraic linear form will force an exact integer relation between its logarithms. The relation has coefficients bounded independently of the varying coefficient height. Once that assertion is proved, eliminating one logarithm gives the effective lower bound by induction. This is the target that determines the polynomial degrees, derivative orders and grid sizes below.

We prove Theorem 4.1 of [*Effective lower bounds I: Baker's theorem and its arithmetic tools*](../TR-BAKER-04.html), including its algebraic constant term, dependent logarithms and arbitrary fixed branches. We use the degree-indexed Matveev polynomials of Lemma 4.7, with their uniform derivative denominator and complex growth bound. A direct pigeonhole argument constructs the integer coefficients. Approximate interpolation extends small derivative values; integer norms then turn sufficiently small algebraic comparison values into exact zeros on a rational grid. A confluent exponential determinant recovers the bounded relation.

Baker's auxiliary-function and extrapolation method, the polynomial refinements of Feldman and Matveev, and Waldschmidt's expositions underlie this argument. The definitions, contour estimates, rational-grid arithmetic and parameter choices needed for the proof are given here. The full induction comes first, conditional on the bounded-relation proposition; the remaining sections prove that proposition.

## 1. Uniform constants and the normalized problem

First omit any zero logarithm: its contribution to the form is zero. In the normalized argument assume that every \(\ell_j\ne0\). Set
\[
T=\log(2A),\qquad M=\max\left(1,\frac{|\ell_1|}{T},\ldots,\frac{|\ell_n|}{T}\right),
\qquad a=\frac1{8n}.
\]
Constants denoted by \(G,D,K\) below are effectively computable from \(n,d,M\). They are independent of \(A,B\) and all varying coefficients. They may be enlarged a finite number of times.

An effective upper bound for \(M\) suffices everywhere. For branches \(\ell_j=\operatorname{Log}\alpha_j+2\pi iq_j\), it follows from \(|\ell_j|\le\log(dA)+\pi+2\pi|q_j|\); one may replace \(M\) by a larger rational bound computed from these integers.

We will choose a sufficiently large integer \(k\), depending on the fixed data, and put
\[
h_0=\lfloor\log(kB)\rfloor,\quad h=h_0+\lceil T\rceil,\quad
L=\lfloor k^{1-2a}\rfloor. \tag{5.1}
\]
The term \(\lceil T\rceil\) ensures \(h\ge T\). It absorbs the logarithm-size costs into the derivative budget while keeping the number of extrapolation stages independent of \(A\). We choose \(k\ge T\), so
\[
h\ge\log k,\qquad h\ge T,\qquad
\frac h{\log B}\le6k. \tag{5.2}
\]
For the upper bound, use \(h\le\log B+\log k+T+1\), \(B\ge2\), and \(\log k,T\le k\).

The elementary root bound gives \(|\beta|\le dB\) for every permitted coefficient and every conjugate. For a nonzero chosen logarithm we also have
\[
e^{-G T}\le|\ell_j|\le MT. \tag{5.3}
\]
Here is the lower bound. If \(\alpha_j=1\), its nonzero logarithms have magnitude at least \(2\pi\). Otherwise Lemma 4.2 bounds the naive height of \(\alpha_j-1\) by \(e^{G T}\) and its degree by \(d^2\). Apply the root bound to its inverse: \(|\alpha_j-1|\ge e^{-G T}\). If \(|\ell_j|\le1/2\), the inequality \(|e^{\ell_j}-1|\le2|\ell_j|\) proves (5.3); outside that disk it follows by enlarging \(G\).

We first prove the following normalized assertion.

**Proposition 5.1.** For fixed bases and branches, an effectively computable \(C\) has this property. If \(\beta_0,\ldots,\beta_{n-1}\) have degree at most \(d\), naive height at most \(B\ge2\), and
\[
|\eta|<B^{-C},\qquad
\eta=\beta_0+\sum_{r=1}^{n-1}\beta_r\ell_r-\ell_n, \tag{5.4}
\]
then there are integers \(b'_1,\ldots,b'_n\), not all zero, such that
\[
|b'_j|\le L,\qquad \sum_jb'_j\ell_j=0. \tag{5.5}
\]
The integer \(L\) depends on the fixed data, never on \(B\).

When \(n=1\), there are no \(r\)-variables or corresponding products. Empty products throughout the proof are \(1\). The proposition then says that a very small normalized form would force \(\ell_1=0\); since we omitted zero logarithms, it gives a direct contradiction.

## 2. How the bounded relation proves the theorem

Assuming Proposition 5.1, we prove Theorem 4.1 by induction on the number \(n\) of logarithms. Include \(n=0\): a nonzero algebraic coefficient of degree at most \(d\) and height at most \(B\) has
\[
|\beta_0|\ge\frac1{dB}>B^{-C_0},\qquad
C_0=2+\frac{\log d}{\log2}.
\]
This is the root bound for \(\beta_0^{-1}\). At \(n>0\), a zero logarithm can be omitted and the induction hypothesis applied. If all logarithmic coefficients are zero, the same \(n=0\) argument applies.

Otherwise relabel so that \(\beta_n\ne0\), and suppose, seeking a contradiction, that
\[
0<|\Lambda|\le B^{-C_{\mathrm{full}}}. \tag{5.41}
\]
Divide by \(-\beta_n\). The normalized coefficients
\[
\beta'_r=-\beta_r/\beta_n\quad(0\le r<n)
\]
have degree at most \(d^2\). Lemma 4.8 gives the explicit common height bound
\[
H(\beta'_r)\le K_dB^{4d^2},\qquad K_d=(1+d^2)^{d^2}.
\]
In particular this is at most \(B^{c_d}\) with
\[
c_d=4d^2+\frac{d^2\log(1+d^2)}{\log2}.
\]
Inversion preserves naive height; the bound controls the quotient without changing the algebraic constant term.

Also \(|\beta_n^{-1}|\le dB\). If \(C_{\mathrm{norm}}\) is the constant of Proposition 5.1 for degree bound \(d^2\), then choosing
\[
C_{\mathrm{full}}>c_d C_{\mathrm{norm}}+1+\frac{\log d}{\log2}
\]
makes the normalized nonzero form satisfy (5.4), with height parameter \(B^{c_d}\). Proposition 5.1 gives a nontrivial integer relation \(\sum b'_j\ell_j=0\), with \(|b'_j|\le L\). Choose an index \(s\) with \(b'_s\ne0\).

Multiply the original form by \(b'_s\) and subtract \(\beta_s\) times the relation. We obtain
\[
\Gamma=b'_s\Lambda
=b'_s\beta_0+\sum_{j\ne s}(b'_s\beta_j-b'_j\beta_s)\ell_j. \tag{5.42}
\]
This form is nonzero and contains at most \(n-1\) logarithms. Its coefficients have degree at most \(d^2\) and height at most
\[
B'=(BL)^{c_d}, \tag{5.43}
\]
after enlarging \(c_d\). Integer scaling preserves the degree of each individual \(\beta_j\); applying Lemma 4.2 to their sums proves (5.43).

Let \(C_{\mathrm{ind}}\) be the induction constant for \(n-1\) logarithms and degree bound \(d^2\), on the remaining branches. Then
\[
|\Gamma|>(B')^{-C_{\mathrm{ind}}},
\]
and therefore
\[
|\Lambda|>L^{-1}(BL)^{-c_d C_{\mathrm{ind}}}
\ge B^{-E}, \tag{5.44}
\]
where
\[
E=c_dC_{\mathrm{ind}}
+(c_dC_{\mathrm{ind}}+1)\frac{\log L}{\log2}.
\]
The last inequality uses \(B\ge2\). Taking \(C_{\mathrm{full}}\ge E\), with a strict margin for normalization, contradicts (5.41). Choose the constants uniformly over the finitely many possible relabelings and omitted indices before the coefficients vary; the bounds in terms of \(n,d,M\) also do this directly. Thus \(C_{\mathrm{full}}\) is independent of the tuple and of \(B\). Once Proposition 5.1 is established, this proves Theorem 4.1, including dependent logarithms and the algebraic constant term.

For a concrete elimination, let \(\ell_1=\log2\), \(\ell_2=\log4=2\ell_1\), and \(\Lambda=1+\ell_1-\ell_2=1-\log2\). The relation \(2\ell_1-\ell_2=0\) has \((b'_1,b'_2)=(2,-1)\). Taking \(s=2\) in (5.42) gives
\[
\Gamma=-\Lambda=-1+\log2.
\]
The constant term survives, the selected logarithm disappears, and the remaining form is still nonzero. In general the integer multiplier is the reason for the factor \(L^{-1}\) in (5.44).

For completeness, the power dependence survives the induction. Equation (5.40) gives the normalized exponent \(16n(9n+4)\), and \(L\le k\le K_1T^{16n}\) gives \(1+\log L\le K_2T\). Thus (5.44) costs at most one additional power of \(T\) over the induction constant. A generous explicit choice is
\[
\kappa(0)=0,\qquad \kappa(n)=200(n+1)^2\quad(n\ge1), \tag{5.45}
\]
since it exceeds \(16n(9n+4)\), and \(\kappa(n-1)+1<\kappa(n)\). Changes \(d\mapsto d^2\) affect only the leading constants. The \(n=0\) constant has no \(A\)-dependence.

We have proved
\[
C_{\mathrm{full}}\le K(n,d,M)\{\log(2A)\}^{\kappa(n)}.
\]
For \(A\ge2\), \(\log(2A)\le2\log A\), so this is the claimed power of \(\log A\). On principal branches,
\[
|\operatorname{Log}\alpha_j|
\le\log(dA)+\pi,
\]
because both \(\alpha_j\) and \(\alpha_j^{-1}\) satisfy the root bound. Hence \(M\) is bounded by a constant depending only on \(d\); the leading constant then depends only on \(n,d\). Arbitrary fixed branches retain their \(M\)-dependence, exactly as required by the quantifiers and the Pell example in the preceding lesson.

## 3. Building an almost-vanishing auxiliary function

Use indices
\[
0\le\lambda_{-1}<h,\qquad 0\le\lambda_0,\ldots,\lambda_n\le L,
\qquad \gamma_r=\lambda_r+\lambda_n\beta_r\quad(1\le r<n).
\]
Put
\[
a_\lambda=h\lambda_0+\lambda_{-1},\qquad
U_\lambda(x)=D_h(x+1;a_\lambda).
\]
As \((\lambda_{-1},\lambda_0)\) varies, \(a_\lambda\) runs through the integers \(0,\ldots,h(L+1)-1\) exactly once. Lemma 4.7 gives
\[
V(h)^k\frac{U_\lambda^{(\mu)}(l)}{\mu!}\in\mathbb Z
\quad(l\in\mathbb Z,\ 0\le\mu\le k),
\]
where \(V(h)=\operatorname{lcm}(1,\ldots,h)\), and
\[
\sum_{\mu=0}^k\binom{k}{\mu}|U_\lambda^{(\mu)}(z)|
\le k!e^{a_\lambda+h}
\left(1+\frac{|z+1|}{h}\right)^{a_\lambda}.
\]
The degree is \(a_\lambda\), with nonzero leading coefficient. Thus these \(h(L+1)\) polynomials form a basis of the polynomials of degree below \(h(L+1)\). The denominator depends on \(h,k\), independently of the node \(l\).

For example, \(h=2,L=1\) gives the four polynomials
\[
1,\quad x+1,\quad\frac{(x+1)(x+2)}2,\quad
\frac{(x+1)^2(x+2)}2.
\]
Their degrees are \(0,1,2,3\); a nonzero coefficient block therefore remains nonzero after collection. For the last polynomial at \(x=0\), the normalized derivatives are \(1,5/2,2,1/2\). Multiplication by the common factor \(V(2)^3=8\) gives the integers \(8,20,16,4\).

For integer coefficients \(p_\lambda\), define the entire function of \(n\) variables
\[
\Phi(z_0,\ldots,z_{n-1})
=\sum_\lambda p_\lambda
U_\lambda(z_0)
e^{\lambda_n\beta_0z_0}
\prod_{r=1}^{n-1}e^{\gamma_r\ell_rz_r}. \tag{5.6}
\]
The polynomial degree and the denominator block size are separate parameters. This separation is essential: raising the degree does not enlarge the derivative denominator beyond the chosen power of \(V(h)\). For a multi-index \(m=(m_0,\ldots,m_{n-1})\), let
\[
f_m(z)=\partial^m\Phi(z,\ldots,z),\qquad
P_m=\prod_{r=1}^{n-1}\ell_r^{m_r}.
\]
Every \(P_m\ne0\). Put
\[
q_{\lambda,m_0}(x)=
\sum_{\mu=0}^{m_0}\binom{m_0}{\mu}
U_\lambda^{(\mu)}(x)
(\lambda_n\beta_0)^{m_0-\mu}. \tag{5.7}
\]
The product rule and (5.4) give the exact diagonal formula
\[
f_m(z)=P_m\sum_\lambda p_\lambda q_{\lambda,m_0}(z)
\prod_{r<n}\gamma_r^{m_r}
\exp\left(z\sum_{j=1}^n\lambda_j\ell_j+\lambda_n\eta z\right). \tag{5.8}
\]
This identity explains the quantitative gain. Although \(\beta_0\) can be large, its exponential combines with the other diagonal exponentials to leave the fixed logarithms and the tiny error \(\eta\).

For \(l=1,\ldots,h\) impose the algebraic equations
\[
Q_m(l):=\sum_\lambda p_\lambda q_{\lambda,m_0}(l)
\prod_{r<n}\gamma_r^{m_r}\prod_{j=1}^n\alpha_j^{\lambda_jl}=0,
\qquad |m|\le k. \tag{5.9}
\]

**Lemma 5.2.** Once \(k\) is sufficiently large and \(LT\le k\), equations (5.9) have a nonzero integer solution with
\[
|p_\lambda|\le e^{Ghk}. \tag{5.10}
\]
If \(C\) in (5.4) is sufficiently large compared with a fixed power of \(k\), then
\[
|f_m(l)|<B^{-C/2}\qquad(1\le l\le h,\ |m|\le k). \tag{5.11}
\]

**Proof of the integer construction.** There are
\[
N=h(L+1)^{n+1}
\]
unknowns. The field generated by the \(n\) bases and \(n\) coefficients has degree at most \(d^{2n}\). We can use the formal spanning products of powers below each minimal-polynomial degree, even if they are linearly dependent. Setting every spanning coefficient equal to zero is sufficient for (5.9). Thus the number of integer scalar equations is at most
\[
M_0=d^{2n}h(k+1)^n.
\]
Since \(L+1>k^{1-1/(4n)}\),
\[
\frac N{M_0}\ge
\frac{k^{(3n-1)/(4n)}}{2^n d^{2n}}, \tag{5.12}
\]
which exceeds \(2\) for an effective choice of \(k\).

We spell out the coefficient bound to avoid an implicit varying-field constant. Let \(a_j\le A\) and \(b_r\le B\) be the leading coefficients of the primitive minimal polynomials of \(\alpha_j\) and \(\beta_r\). Multiplication by
\[
V(h)^k\prod_{j=1}^n a_j^{Lh}
\prod_{r=0}^{n-1}b_r^k \tag{5.13}
\]
clears all rational denominators before expanding in the formal spanning products. Lemma 4.7 clears the normalized derivative values with the first factor. Multiplication by \(\mu!\) recovers the ordinary derivative in (5.7), so it introduces no new denominator. Each base power is at most \(Lh\), and each coefficient power is at most \(k\).

For a root \(\theta\) of a primitive polynomial with leading coefficient \(c\) and height \(H\), the integral expansion of \((c\theta)^j\) in \(1,\theta,\ldots,\theta^{s-1}\) has coefficients at most \((2H)^j\). To verify this bound, multiplication by \(c\theta\) replaces the highest power using
\(c\theta^s=-c_1\theta^{s-1}-\cdots-c_s\); each new coefficient is a sum of at most two terms bounded by \(H\) times the old maximum. The initial coefficient is \(1\). Padding with \(c^{v-j}\) shows that \(c^v\theta^j\), \(j\le v\), has the same bound \((2H)^v\).

The complex growth bound just displayed, at \(l\le h\), gives a polynomial contribution with logarithm at most \(G\{h(L+1)+k\log k\}\). The factorial and binomial factors in (5.7) are covered by this estimate. Equation (4.11) gives \(\log V(h)\le h\log8\). Expansion of the powers of \(\gamma_r\) contributes \(O(k\log(kB))\). All coefficients of the integer equations are therefore bounded by a number \(U\ge1\) with
\[
\log U\le G\{LhT+hk+k\log k+k\log B\}\le Ghk. \tag{5.14}
\]
The last inequality uses \(LT\le k\) and (5.2).

Here is the small-solution argument in the exact form needed. An integer matrix with at most \(M_0\) rows, \(N>2M_0\) columns and entries of magnitude at most \(U\) has a nonzero integer kernel vector of magnitude at most \(5NU\). Let \(Q=\lceil4NU\rceil\), and map the \((Q+1)^N\) integer vectors in \(\{0,\ldots,Q\}^N\) to their row-value vectors. There are at most \((2NUQ+1)^{M_0}\) possible images. Since \(NUQ\ge1\) and \(Q\ge4NU\),
\[
2NUQ+1\le3NUQ<Q^2<(Q+1)^2.
\]
Consequently \((Q+1)^N>(2NUQ+1)^{M_0}\). Two distinct vectors have the same image; their nonzero difference is in the kernel and has magnitude at most \(Q\le5NU\). Redundant or zero rows cause no difficulty. Since \(\log(5N)\le Ghk\), (5.14) proves (5.10).

**Proof of almost vanishing.** At an integer \(l\), the difference between \(P_m^{-1}f_m(l)\) and \(Q_m(l)\) is obtained by replacing \(1\) by \(e^{\lambda_n\eta l}\) in each summand. For \(|m|\le k\), \(l\le hk^{8n}\), (5.3), (5.7), (5.10) and the elementary inequality \(|e^u-1|\le |u|e^{|u|}\) yield
\[
|f_m(l)-P_mQ_m(l)|
\le e^{G(hk+LlT)}Ll|\eta|e^{Ll|\eta|}. \tag{5.15}
\]
The factor counting summands is absorbed in \(Ghk\). Uniformly in this range, \(L\le k,\ T\le k\) and \(h/\log B\le6k\) imply that the logarithm of the prefactor is at most \(Dk^{8n+3}\log B\). For an effective \(C>Dk^{9n+4}\), after enlarging \(D\), the right side of (5.15) is below \(B^{-C/2}\). The same assertion holds after dividing by \(P_m\), because (5.3) contributes at most \(GkT\le Ghk\). Equation (5.9) now proves (5.11). \(\square\)

The construction depends on \(B\), but its constants do not. It also does not depend on an uncomputed integral basis for the varying coefficient field.

## 4. Growth and an arithmetic alternative

**Lemma 5.3.** With the solution of Lemma 5.2 and \(|m|\le k\),
\[
|f_m(z)|\le e^{G(hk+LT|z|)}\qquad(z\in\mathbb C). \tag{5.16}
\]
For every integer \(h<l\le hk^{8n}\), one of the following alternatives holds:
\[
|f_m(l)|<B^{-C/2}, \tag{5.17}
\]
or
\[
|f_m(l)|\ge
\exp\{-G[hk(1+\log(l/h))+LlT]\}. \tag{5.18}
\]
Here and below \(C>Dk^{9n+4}\) can be increased once to satisfy all error estimates.

**Proof.** The complex growth bound for \(U_\lambda\), and \(m_0\le k\), give
\[
|q_{\lambda,m_0}(z)|
\le \max(1,LdB)^k k!e^{a_\lambda+h}
\left(1+\frac{|z+1|}{h}\right)^{a_\lambda}.
\]
Indeed, \(\binom{m_0}{\mu}\le\binom{k}{\mu}\) for \(\mu\le m_0\), and every coefficient power in (5.7) is bounded by \(\max(1,LdB)^k\). With \(a_\lambda<h(L+1)\), the logarithm of the last two factors is at most
\[
G\{h(L+1)+(L+1)(|z|+1)\}.
\]
This follows from \(\log(1+v)\le v\), without division by a polynomial factor at any zero. The other contributions, including \(P_m\), \(\gamma_r^{m_r}\), \(k!\), the coefficient bound and the number of summands, have logarithm at most \(Ghk\). Use \(L\le k\), \(\log k\le h\), \(\log B\le h\), and \(T\le h\). Finally the exponent in (5.8) has absolute real part at most \(nMLT|z|+L|\eta||z|\). Since \(T\ge1\) and \(|\eta|<1\), these estimates prove (5.16).

For (5.18), consider the algebraic comparison value \(Q_m(l)\) in (5.9), now without imposing its vanishing. Its degree is at most \(d^{2n}\), and every conjugate satisfies
\[
|Q_m(l)^{(\sigma)}|\le e^{G(hk+LlT)}. \tag{5.19}
\]
At any integer \(l\), a denominator clearing factor is
\[
q_l=V(h)^k
\prod_{j=1}^n a_j^{Ll}\prod_{r=0}^{n-1}b_r^k
\qquad(l\ge1).
\]
Lemma 4.7 clears every derivative value, and the remaining factors make each monomial in the bases and coefficients integral. Thus
\[
\log q_l\le G(hk+LlT)
\le G\{hk(1+\log(l/h))+LlT\}\quad(l>h). \tag{5.20}
\]
The first inequality is the stronger one: the derivative-denominator cost is independent of \(l\). We use the second, more generous budget in the extrapolation estimates.

Therefore \(q_lQ_m(l)\) is an algebraic integer. To see the norm assertion explicitly, if a nonzero algebraic integer \(\theta\) has monic minimal polynomial of degree \(s\) and constant term \(c_0\in\mathbb Z\setminus\{0\}\), then its norm from a containing field of degree \(D\) is \((-1)^{D}c_0^{D/s}\). It is a nonzero integer. Bounding all conjugates but the chosen one by (5.19), and dividing by \(q_l\), now gives
\[
|Q_m(l)|\ge e^{-G(hk+LlT)}
\ge e^{-G[hk(1+\log(l/h))+LlT]}\quad(l>h).
\]
If \(Q_m(l)=0\), (5.15) gives (5.17). Otherwise the error in (5.15) is less than \(|P_mQ_m(l)|/2\), for \(C>Dk^{9n+4}\). Restore \(P_m\) using (5.3) and absorb the factor \(1/2\) by enlarging \(G\). This proves (5.18). \(\square\)

The same block denominator applies at the initial and extended integer nodes. This is the arithmetic advantage of the Matveev family: the derivative order costs \(k\log V(h)\le hk\log8\), even when \(l/h\) becomes large. The interval-LCM estimate of Lemma 4.4 gives another valid budget, but is not needed for this denominator.

## 5. Interpolation with small derivatives

We record the analytic estimate used twice below. Let \(f\) be entire, and suppose
\[
|f^{(j)}(r)|\le E
\quad(1\le r\le R_0,\ 0\le j<s),
\]
where \(R_0,s\ge1\) are integers. Put
\[
F(z)=\prod_{r=1}^{R_0}(z-r)^s.
\]
For a point \(u\) distinct from those integers, and an outer circle \(|z|=\mathcal R>2(R_0+|u|)\), the residue theorem gives
\[
f(u)=\frac{F(u)}{2\pi i}\int_{|z|=\mathcal R}
\frac{f(z)}{(z-u)F(z)}\,dz-\mathcal E(u). \tag{5.21}
\]
Here \(\mathcal E(u)\) is the sum of the residues at the integers, multiplied by \(F(u)\). At \(r\), replace \(f(z)\) inside that residue by its Taylor polynomial through degree \(s-1\); the difference has no residue, because it has a zero of order at least \(s\).

If \(u\) is an integer outside \(1,\ldots,R_0\), use circles \(|z-r|=1/2\) around the poles. The Taylor polynomial has size at most \(Ee^{1/2}\) there, and \(|z-u|\ge1/2\). Also
\[
|F(z)|\ge
\left[2^{-R_0}(r-1)!(R_0-r)!\right]^s
\ge\left[4^{-R_0}(R_0-1)!\right]^s. \tag{5.22}
\]
The second bound follows from
\(\binom{R_0-1}{r-1}\le2^{R_0-1}\).
Since \(|F(u)|\le(|u|+R_0)^{R_0s}\) and \(v!\ge(v/e)^v\), these estimates give, with an absolute effective \(D\),
\[
|\mathcal E(u)|\le
E\exp\left\{
DR_0s\left(1+\log\left(1+\frac{|u|}{R_0}\right)\right)
+Ds\log(2R_0)+D\log(2R_0)\right\}. \tag{5.23}
\]
For \(R_0=1\), use the first bound in (5.22) directly; (5.23) still follows.

If \(u=t/k\) is nonintegral, use circles of radius \(1/(2k)\). The distance to every integer is at least \(1/k\). In (5.22), only the factor belonging to \(r\) needs the additional factor \(k^{-s}\); the other factors retain their factorial lower bound. Thus (5.23) holds with the additional term
\[
Ds\log(2k)+D\log(2k) \tag{5.24}
\]
in its exponent. These bounds have no term \(R_0s\log R_0\): the factorials cancel that apparent loss. This cancellation keeps the estimate uniform as \(h\) grows.

On the outer circle, \(|F(z)|\ge(\mathcal R-R_0)^{R_0s}\). The integral term in (5.21) is bounded by
\[
\frac{\mathcal R}{\mathcal R-|u|}
\max_{|z|=\mathcal R}|f(z)|
\left(\frac{|u|+R_0}{\mathcal R-R_0}\right)^{R_0s}. \tag{5.25}
\]
All three estimates follow from the displayed contour identities and elementary inequalities; no exact-zero assertion was used.

## 6. Extending the interval of almost zeros

Choose an integer \(J_*\) so large that
\[
\varepsilon=\frac{8n}{J_*}
<\min\left(\frac a2,\frac{a}{128(G+1)}\right). \tag{5.26}
\]
Here \(G\) dominates the constants in both estimates of Lemma 5.3. Thus \(J_*\) and \(\varepsilon\) depend only on \(n,d,M\). Put
\[
R_J=\lfloor hk^{J\varepsilon}\rfloor,\qquad
S_J=\left\lfloor\frac{k}{2^J}\right\rfloor
\quad(0\le J\le J_*).
\]
Choose \(k\ge2^{J_*+2}\). All the derivative budgets are then positive.

**Lemma 5.4.** For every \(0\le J\le J_*\),
\[
|f_m(l)|<B^{-C/2}
\quad(1\le l\le R_J,\ |m|\le S_J). \tag{5.27}
\]

**Proof.** The case \(J=0\) is (5.11). Suppose the result holds at \(J<J_*\), and take \(|m|\le S_{J+1}\). Differentiating along the diagonal gives
\[
f_m^{(j)}(z)=
\sum_{\substack{v_0+\cdots+v_{n-1}=j\\v_r\ge0}}
\binom{j}{v_0,\ldots,v_{n-1}} f_{m+v}(z).
\]
For \(0\le j\le S_{J+1}\), we have
\(|m|+j\le2S_{J+1}\le S_J\), because \(2\lfloor x/2\rfloor\le\lfloor x\rfloor\). Hence at each \(r=1,\ldots,R_J\),
\[
|f_m^{(j)}(r)|\le n^jB^{-C/2}\le n^kB^{-C/2}. \tag{5.28}
\]

Take an integer \(R_J<l\le R_{J+1}\), and apply Section 5 with
\[
R_0=R_J,\quad s=S_{J+1}+1,\quad
\mathcal R=R_{J+1}k^a.
\]
For large \(k\), this radius exceeds \(2(R_J+l)\). Equations (5.23), (5.28), and \(R_J\le hk^{8n}\), \(s\le k+1\), \(R_{J+1}/R_J\le2k^\varepsilon\), show that
\[
|\mathcal E(l)|\le B^{-C/2}e^{Dhk^{8n+2}}. \tag{5.29}
\]
This estimate includes the factors \(n^k\) and \(\log R_J\); use \(\log h\le h\), \(\log k\le k\). In view of (5.2), choose \(C>Dk^{9n+4}\) large enough that (5.29) is less than one quarter of the lower bound in (5.18), uniformly throughout the entire range.

Suppose the large alternative (5.18) holds at \(l\). Write its exponent as
\[
\mathcal N(l)=G[hk(1+\log(l/h))+LlT].
\]
Then \(|f_m(l)|\ge e^{-\mathcal N(l)}\). By (5.16) and (5.25), the outer integral contribution is at most
\[
2\exp\{G(hk+LT\mathcal R)-R_Js(a\log k-\log4)\}. \tag{5.30}
\]
We choose \(k\) so that this is less than \(e^{-\mathcal N(l)}/2\). We now verify that this choice is possible uniformly in \(A,B\).

For \(J=0\), \(R_0=h\) and \(s\ge k/2\). The negative term has size at least
\[
\frac{hk}{2}(a\log k-\log4).
\]
The part \(\mathcal N(l)\) involving the LCM is at most \(Ghk(1+\varepsilon\log k)\); (5.26) makes its logarithmic coefficient strictly smaller than the negative coefficient. The other growing term satisfies
\[
\frac{LT\mathcal R}{hk}
\le Tk^{\varepsilon-a},
\]
and \(LlT/(hk)\le Tk^{\varepsilon-2a}\).

For \(J\ge1\),
\[
R_Js\ge \frac{hk^{1+J\varepsilon}}{2^{J+2}}. \tag{5.31}
\]
After division by this quantity, the LCM part of \(\mathcal N(l)\), and the term \(Ghk\), are at most a fixed multiple of
\[
2^Jk^{-J\varepsilon}(1+(J+1)\varepsilon\log k),
\]
which tends to zero relative to \(\log k\). The remaining ratios are bounded by fixed multiples of
\[
2^JTk^{\varepsilon-a},\qquad
2^JTk^{\varepsilon-2a}. \tag{5.32}
\]
These also become small. Indeed, choose
\[
k\ge K T^{16n}. \tag{5.33}
\]
Since \(\varepsilon<a/2\) and \(1/a=8n\),
\[
Tk^{\varepsilon-a}\le Tk^{-a/2}\le K^{-a/2},
\]
and the second ratio is smaller. The finitely many powers \(2^J\), \(J\le J_*\), are absorbed by increasing \(K\), independently of \(A,B\). For the first ratios, increasing \(K\) also makes \(k^{-J\varepsilon}\) small for every \(J\ge1\). Thus a single effective \(K(n,d,M)\) makes (5.30) less than half the large lower bound for every stage.

Equations (5.21), (5.29)–(5.30) would then give
\[
|f_m(l)|<\frac34 e^{-\mathcal N(l)},
\]
contrary to the assumed large alternative. Therefore the small alternative (5.17) holds. Together with the old interval, it proves (5.27) at \(J+1\). \(\square\)

This is a finite induction. Its number of stages is fixed before \(B\) varies, and \(R_{J_*}=\lfloor hk^{8n}\rfloor\). The arithmetic alternative, rather than an assertion that a small number is zero, permits the error threshold to remain unchanged at every stage.

## 7. From the integer grid to a rational grid

Set
\[
X=\lfloor hk^{8n}\rfloor,\qquad
Y=\left\lfloor\frac{k}{2^{J_*}}\right\rfloor,\qquad
f(z)=\Phi(z,\ldots,z).
\]
The same diagonal chain rule gives
\[
|f^{(j)}(r)|\le n^kB^{-C/2}
\quad(1\le r\le X,\ 0\le j\le Y). \tag{5.34}
\]
We claim that for every integer \(0\le t\le\lfloor hk^{4n}\rfloor\),
\[
Q(t):=\sum_\lambda p_\lambda
U_\lambda(t/k)
\prod_{j=1}^n\alpha_j^{\lambda_jt/k}=0. \tag{5.35}
\]
The fractional powers here have the prescribed determinations
\(\alpha_j^{1/k}=e^{\ell_j/k}\). They are algebraic roots of \(X^k-\alpha_j\).

First bound the analytic value \(f(t/k)\). If \(t/k\) is one of the integer nodes, (5.27) already gives its smallness. Otherwise apply (5.21) with \(R_0=X,\ s=Y+1,\ u=t/k\), and
\[
\mathcal R=Xk^a.
\]
We have \(u\le hk^{4n-1}<X\) for large \(k\). The outer contribution is at most
\[
2\exp\{G(hk+LT\mathcal R)-X(Y+1)(a\log k-\log4)\}.
\]
The ratio \(LT\mathcal R/(XY)\) is bounded by a fixed multiple of
\[
2^{J_*}Tk^{-a},
\]
which can be made as small as needed by (5.33) and a larger \(K\). Also \(hk/(XY)\to0\) as \(k\) increases. Hence the outer contribution is less than \(e^{-2XY}\).

Equations (5.23)–(5.24) bound the residue contribution by
\[
B^{-C/2}e^{Dhk^{8n+2}}.
\]
Choosing \(C>Dk^{9n+4}\) sufficiently large makes this less than \(e^{-2XY}\), uniformly in \(B\). The same conclusion follows directly from (5.27) at an integer node. Consequently
\[
|f(t/k)|<2e^{-2XY}\le e^{-XY}. \tag{5.36}
\]
The last inequality holds since \(XY\ge1\) and \(e>2\).

We now prove an algebraic lower bound for a nonzero \(Q(t)\). Let
\(\rho_j=e^{\ell_j/k}\). The field generated by the \(\rho_j\)'s has degree at most \((dk)^n\). Every conjugate has
\[
|\rho_j^{(\sigma)}|\le(dA)^{1/k}.
\]
Using \(u=t/k\le hk^{4n-1}\), \(h!\ge(h/e)^h\), (5.10), and \(L\le k\), every conjugate of \(Q(t)\) is at most
\[
\exp\{D[hk+h(L+1)\log(2k)+Lhk^{4n-1}T]\}
\le e^{Dhk^{4n+2}}. \tag{5.37}
\]

For the rational polynomial factor, the denominator of \(D_h(1+t/k;a)\) divides \(k^{2a}\). Write \(a=hq+r\), \(0\le r<h\). Before cancellation its denominator is \(k^a(h!)^q r!\), and its numerator is the product of \(q\) blocks
\[
\prod_{j=1}^h(t+kj)
\]
and one block \(\prod_{j=1}^r(t+kj)\). If \(p\nmid k\), each block of length \(b\) contains at least \(\lfloor b/p^v\rfloor\) multiples of \(p^v\), for every \(v\ge1\). It therefore cancels the corresponding factorial valuation. If \(p\mid k\), the remaining denominator exponent is at most
\[
av_p(k)+qv_p(h!)+v_p(r!)
\le av_p(k)+\frac a{p-1}\le2av_p(k).
\]
This proves the claim, including a zero numerator and \(a=0\). Since \(a_\lambda<h(L+1)\), the common factor \(k^{2h(L+1)}\) clears all these rational polynomial values. For instance, \(h=2,a=3,k=3,t=1\) gives \(D_2(4/3;3)=56/27\), whose denominator divides \(3^6\).

Furthermore \(a_j\rho_j\) is an algebraic integer, because \(\rho_j\) is a root of the polynomial obtained from the minimal polynomial of \(\alpha_j\) by substituting \(X^k\), with leading coefficient \(a_j\). Therefore
\[
q_t=k^{2h(L+1)}\prod_{j=1}^n a_j^{Lt}
\]
makes \(q_tQ(t)\) an algebraic integer. Its logarithm is at most \(Dhk^{4n+2}\). If \(Q(t)\ne0\), its norm and (5.37) give
\[
|Q(t)|\ge e^{-Dhk^{6n+2}}. \tag{5.38}
\]
The exponent \(6n+2\) is deliberately generous: multiplying the exponents in (5.37) by the degree \((dk)^n\) needs at most \(5n+2\).

From (5.8), with \(m=0\), the difference \(Q(t)-f(t/k)\) is the sum with the extra factors \(1-e^{\lambda_n\eta t/k}\). The same estimate as (5.15) makes it smaller than \(e^{-2XY}\) for our choice of \(C\). Therefore
\[
|Q(t)|<2e^{-XY}.
\]
But
\[
XY\ge \frac{hk^{8n+1}}{2^{J_*+2}},
\]
and \(8n+1>6n+2\) for every \(n\ge1\). Increasing \(K\) makes \(2e^{-XY}<e^{-Dhk^{6n+2}}\). This contradicts (5.38) whenever \(Q(t)\ne0\), proving (5.35). At \(t=0\), the same algebraic and analytic estimates apply without alteration. \(\square\)

The rational grid step uses a new algebraic field, but its degree is explicitly bounded. It does not import an unquantified constant from that field.

## 8. The determinant produces a bounded relation

For each fixed \((\lambda_1,\ldots,\lambda_n)\), collect the polynomial factors into
\[
P_{\lambda_1,\ldots,\lambda_n}(x)
=\sum_{\lambda_{-1}=0}^{h-1}\sum_{\lambda_0=0}^L
p_\lambda U_\lambda(x).
\]
Their degrees are at most
\[
D_0=h(L+1).
\]
At least one collected polynomial is nonzero: choose a nonzero coefficient block, then the largest degree \(a_\lambda\) with nonzero coefficient in that block. Its leading term cannot be cancelled by any smaller degree. This uses exactly the degree-indexed basis chosen in the construction; no independence assumption on the frequencies has entered.

There is also a useful translated-power basis from Lemma 4.5. For each \(b=0,\ldots,L\), apply it to \(\Delta(x;h)^{b+1}\), of degree \(h(b+1)\), with \(m=h-1\). Its \(h\) translates, together with all polynomials of degree at most \(hb\), form a basis. Starting with \(1\), induction on \(b\) proves that
\[
1,\quad\Delta(x+j;h)^{b+1}
\quad(0\le j<h,\ 0\le b\le L)
\]
form a basis through degree \(D_0\). Thus their nonconstant blocks also survive collection. Both bases expose the same polynomial-rank requirement. The degree-indexed family makes that requirement immediate and supplies the uniform derivative denominator used above.

Write \(P_{\lambda_1,\ldots,\lambda_n}(x)=\sum_{r=0}^{D_0}c_{r,\lambda}x^r\), and set
\[
w_\lambda=\prod_{j=1}^n\rho_j^{\lambda_j}
=\exp\left(\frac1k\sum_{j=1}^n\lambda_j\ell_j\right).
\]
Equation (5.35) now says
\[
\sum_{\lambda_1,\ldots,\lambda_n}
\sum_{r=0}^{D_0} c_{r,\lambda}k^{-r}t^r w_\lambda^t=0
\quad(0\le t\le\lfloor hk^{4n}\rfloor). \tag{5.39}
\]
There are \(R=(L+1)^n\) frequency labels. If all \(w_\lambda\) were distinct, the first
\[
N_1=(D_0+1)(L+1)^n
\]
equations of (5.39) would have the nonsingular matrix of Lemma 4.6, with its parameters \(k_{\mathrm{det}}=D_0+1\) and \(l_{\mathrm{det}}=R\). The factor \(k^{-r}\) is a nonzero column scaling. For large \(k\),
\[
N_1\le 2h(L+1)^{n+1}\le hk^{4n},
\]
because \((n+1)(1-1/(4n))<4n\). There are thus enough grid points. Nonsingularity would force every \(c_{r,\lambda}=0\), contrary to the nonzero collected polynomial.

Consequently two distinct labels \(\lambda,\lambda'\) have \(w_\lambda=w_{\lambda'}\). Put \(b'_j=\lambda_j-\lambda'_j\). These integers are not all zero and have magnitude at most \(L\). Equality of the exponentials gives
\[
\sum_j b'_j\ell_j=2\pi i kq\qquad(q\in\mathbb Z).
\]
But
\[
\left|\sum_jb'_j\ell_j\right|\le nMLT<2\pi k
\]
for a sufficiently large \(K\) in (5.33), since \(LT/k\le Tk^{-2a}\) can be made arbitrarily small uniformly in \(T\). Therefore \(q=0\), proving (5.5) and Proposition 5.1. The logarithmic branches have been retained throughout: the final size comparison is what removes the possible period.

## 9. Choosing all constants effectively

The preceding arguments use “sufficiently large” only in a controlled finite list. Here is a concrete order of choice.

1. From the root, recurrence and norm estimates, choose a common effective \(G(n,d,M)\) for (5.3), (5.10), (5.15), (5.16), (5.18) and (5.19). All these estimates were obtained from displayed inequalities; no compactness or ineffective finiteness result occurs.
2. Choose \(J_*\) and \(\varepsilon=8n/J_*\) by (5.26).
3. Increase \(K(n,d,M)\) so that for every \(k\ge KT^{16n}\): \(N>2M_0\); \(LT\le k\); \(k\ge2^{J_*+2}\); the contour radii have the stated separations; the comparisons (5.30)–(5.32) hold at the finite set of stages; the estimates (5.36), (5.38) are inconsistent when \(Q(t)\ne0\); the determinant count is valid; and \(nMLT<2\pi k\).
4. Take \(k=\lceil KT^{16n}\rceil\), then choose \(C>Dk^{9n+4}\), where \(D(n,d,M)\) covers all error and residue inequalities.

Why can Step 3 be performed uniformly? The potentially height-dependent ratios are \(Tk^{\varepsilon-a}\), \(Tk^{-a}\) and \(Tk^{-2a}\). Under (5.33) they are bounded by fixed negative powers of \(K\), as shown in (5.32). Every remaining ratio is a fixed multiple of \(k^{-\delta}(\log k)^v\), with explicitly positive \(\delta\) and fixed \(v\), or a fixed power comparison such as \(k^{6n+2}/k^{8n+1}\). Beyond an effective threshold these functions decrease to zero. Their thresholds can be found by differentiation and a finite integer search. All constants involving \(2^{J_*}\) are fixed before \(A,B\) vary.

Likewise Step 4 is uniform in \(B\), not a new choice for each coefficient tuple. The worst error exponents above are bounded by \(Dhk^{8n+2}\); (5.2) makes them at most \(6Dk^{8n+3}\log B\). Thus a fixed multiple of \(k^{9n+4}\) covers them with strict margins. One can choose, for example, \(C=2Dk^{9n+4}\) after fixing an enlarged \(D\).

Since \(T\ge1\), the normalized proposition has a constant bounded by
\[
C\le K_1(n,d,M)T^{16n(9n+4)}. \tag{5.40}
\]
This gives a power of \(\log A\), with exponent depending only on \(n\). The padding in (5.1) is what absorbed the quantities \(kT\) into \(hk\), while keeping \(J_*\) independent of \(A\).

Proposition 5.1 is now proved. The induction in Section 2 therefore completes Theorem 4.1, with no independence hypothesis on the original logarithms.

## 10. Consequences and later refinements

Fix a nonzero logarithm \(\ell\) of an algebraic \(\alpha\). Taking coefficients \(-\beta,1\) gives
\[
|\ell-\beta|>B^{-C} \tag{5.45}
\]
for algebraic \(\beta\) of bounded degree and naive height at most \(B\). The form is nonzero by the qualitative theorem. This is an effective transcendence measure: it bounds how closely algebraic numbers of a prescribed complexity can approximate \(\ell\).

For \(\ell=\log2\) and a rational approximation \(p/q\), \(q\ge1\), the useful case is \(|\log2-p/q|\le1\). Then \(|p|\le2q\), so the reduced rational has height at most \(2q\), and
\[
|\log2-p/q|>(2q)^{-C}. \tag{5.46}
\]
The case outside that interval already has a lower bound of \(1\). To approximate \(\pi\), take the base \(-1\), its logarithm \(i\pi\), and the coefficient \(i\). Then \(\beta+i(i\pi)=\beta-\pi\). Enlarge the fixed degree bound to at least \(2\) to include \(i\); (5.45) gives the corresponding measure for \(\pi\).

There is also a multiplicative consequence. Fix positive rational numbers \(a_1,\ldots,a_n\), and put
\[
B=\max(3,|b_1|,\ldots,|b_n|),\quad
P=a_1^{b_1}\cdots a_n^{b_n},\quad \Delta=P-1.
\]
If \(P\ne1\), then \(\Omega=\sum b_j\log a_j\ne0\), because these logarithms are real. Theorem 4.1 gives \(|\Omega|>B^{-C}\). When \(|\Delta|\le1/2\), the local logarithm estimate of the first lesson gives \(|\Omega|\le2|\Delta|\). Otherwise \(|\Delta|>1/2\). In both cases, after increasing \(C\),
\[
|a_1^{b_1}\cdots a_n^{b_n}-1|>B^{-C}. \tag{5.47}
\]
This is the fixed-base polynomial shape historically associated with Feldman's refinement; see the historical discussion in [Waldschmidt 2000]. Its proof follows from the full effective theorem just established.

For \(n=1\), \(\ell=\log2\) and \(\beta=p/q\), the theorem gives (5.46). Thus an effective exponent bounds every rational approximation to \(\log2\) in a fixed bounded interval. Clearing the denominator also gives
\[
|q\log2-p|>2^{-C}q^{1-C}.
\]
The numerical size of \(C\) produced by this proof is enormous. It proves an effective principle; the later explicit two-logarithm and many-logarithm estimates are what make computational applications practical.

Historically, the polynomial dependence on \(B\) was refined into individual-height estimates. For integer coefficients, write
\(\Omega=\prod_j\log A_j\), with \(A_j\ge4\). One historical shape for a nonzero multiplicative form is
\[
|\alpha_1^{b_1}\cdots\alpha_n^{b_n}-1|
>B^{-C(n,d)\Omega\log\Omega}.
\]
The lesson [*Linear forms in many logarithms: the modern estimates and how to use them*](../TR-BAKER-08.html) develops the individual-height product bounds with their hypotheses and proofs. The restriction \(A_j\ge4\) makes \(\Omega>1\), so the displayed exponent has the correct sign. Normalized modern statements usually replace these quantities by maxima including a fixed positive floor.

The bounds of Baker–Wüstholz and Matveev improve the individual-height dependence and the constants, especially their dependence on the number of logarithms. Those improvements require additional arguments; the proof just completed supplies Theorem 4.1 without silently importing them.

## 11. Exercises

1. **Medium.** Starting with a nontrivial bounded relation \(\sum b'_j\ell_j=0\), carry out the elimination in (5.42). Prove the new coefficient degree and height bounds, and derive the exponent \(E\) in (5.44).
2. **Medium.** Verify every exponent in the unknown-to-equation ratio (5.12). Explain why dependent formal spanning products cause no problem for the integer Siegel lemma.
3. **Medium.** Let \(\beta\ne0\) be a fixed algebraic number. For every fixed degree bound \(d\), deduce an effective measure
   \[
   |e^\beta-\gamma|>\exp\{-K_{\beta,d}(\log(2H))^{\kappa(1)}\}
   \]
   for algebraic \(\gamma\) of degree at most \(d\) and naive height at most \(H\ge2\), after increasing the constant. Choose and control the logarithm branch of \(\gamma\).
4. **Hard.** Track the constants to prove a bound \(C=C'(n,d)(\log A)^{\kappa(n)}\) on principal branches. Identify why the padding \(h=h_0+\lceil\log(2A)\rceil\) keeps the number of extrapolation stages independent of \(A\), and check that induction preserves a power of \(\log A\).

## 12. Solutions

**Solution 1.** Pick \(s\) with \(b'_s\ne0\). Subtracting \(\beta_s\sum_jb'_j\ell_j=0\) from \(b'_s\Lambda\) cancels its \(\ell_s\)-coefficient and gives (5.42). Each scaled coefficient \(b'_j\beta_s\) has the same degree as \(\beta_s\), and its height is bounded by a fixed power of \(BL\), by Lemma 4.2 applied to the algebraic number and the integer. The difference of two such numbers has degree at most \(d^2\) and height at most another fixed power \((BL)^{c_d}\); the constant coefficient satisfies the same bound. Since \(\Gamma\ne0\), induction gives \(|\Gamma|>(BL)^{-c_dC_{\mathrm{ind}}}\). Divide by \(|b'_s|\le L\), then use \(L\le B^{\log L/\log2}\). The exponent is exactly
\[
c_dC_{\mathrm{ind}}+(c_dC_{\mathrm{ind}}+1)\log L/\log2.
\]
No independence assumption on the remaining logarithms is needed.

**Solution 2.** There are \(h\) choices for \(\lambda_{-1}\), and \(L+1\) choices for each of \(\lambda_0,\ldots,\lambda_n\), so \(N=h(L+1)^{n+1}\). There are \(h\) interpolation points, at most \((k+1)^n\) derivative multi-indices with total order at most \(k\), and at most \(d^{2n}\) formal spanning products. Hence \(M_0\le d^{2n}h(k+1)^n\). Since \(L+1>k^{1-1/(4n)}\) and \(k+1\le2k\),
\[
\frac N{M_0}\ge\frac{k^{(n+1)(1-1/(4n))-n}}{2^nd^{2n}}
=\frac{k^{(3n-1)/(4n)}}{2^nd^{2n}}.
\]
The exponent is positive, including \(n=1\), where it is \(1/2\). Equating every formal spanning coefficient to zero gives a sufficient system even when those products are dependent. It may contain redundant equations, and the integer Siegel lemma does not require full row rank. The row count therefore remains valid.

**Solution 3.** The qualitative theorem proves that \(w=e^\beta\) is transcendental, since \(\beta\ne0\). In particular it is nonzero and cannot equal \(\gamma\). In the case \(|\gamma-w|\le|w|/2\), put
\[
u=(\gamma-w)/w,\qquad \ell_\gamma=\beta+\operatorname{Log}(1+u).
\]
Then \(e^{\ell_\gamma}=\gamma\), and
\[
|\ell_\gamma-\beta|\le2|u|
=2|\gamma-w|/|w|.
\]
The branch size is uniformly bounded by \(|\beta|+1\). Apply Theorem 4.1 with one base \(\gamma\), degree bound enlarged to include \(\beta\), base height bound \(A=H\), and fixed coefficient-height bound \(B_0=\max(2,H(\beta))\). The form \(\ell_\gamma-\beta\) is nonzero, and the established height dependence gives
\[
|\ell_\gamma-\beta|>\exp\{-K_{\beta,d}(\log(2H))^{\kappa(1)}\}.
\]
Multiplication by \(|w|/2\) is absorbed by increasing \(K_{\beta,d}\), since \(\log(2H)\ge1\). Outside the chosen disk, \(|\gamma-w|>|w|/2\), so the same bound follows after a further fixed increase. The case \(\gamma=0\) belongs to this latter case. To control \(M\), use the uniform bound \(|\ell_\gamma|\le|\beta|+1\), rather than applying an estimate with an unbounded branch parameter.

**Solution 4.** Let \(T=\log(2A)\). Root and inverse-root bounds give principal logarithms of size at most \(\log(dA)+\pi\), so \(M\) is bounded in terms of \(d\). The lower bound (5.3) also has a constant depending only on \(d\). Taking \(h\ge T\) absorbs its derivative prefactor into \(e^{Ghk}\). Choosing \(k=\lceil KT^{16n}\rceil\) gives \(LT\le k\) and the uniformly small ratios
\[
Tk^{\varepsilon-a}\le K^{-a/2},\quad
Tk^{-a}\le K^{-a},\quad Tk^{-2a}\le K^{-2a},
\]
using \(T\ge1\) and \(\varepsilon<a/2\). Thus the constants in Lemma 5.3 and the number \(J_*\) of stages are independent of \(A\). All error estimates are covered by \(C\le K_1k^{9n+4}\), so the normalized exponent is at most \(16n(9n+4)\).

In the full induction, normalization changes \(B\) to \(B^{c_d}\). Elimination changes it to \((BL)^{c_d}\), costing the factor \(1+\log L\le K_2T\). Hence the induction exponent increases by at most one. The choice \(\kappa(n)=200(n+1)^2\) exceeds the normalized exponent and the preceding induction exponent plus one. Finally \(T\le2\log A\) converts the result to \(C'(n,d)(\log A)^{\kappa(n)}\). Arbitrary fixed branches give \(C'(n,d,M)\); a uniform leading constant over all branches is excluded by the preceding lesson's Pell construction.

## Prerequisites and continuation

This lesson completes the effective theorem stated in the preceding lesson. It supplies all its own bridges: the varying-field coefficient construction, the growth and arithmetic alternatives, approximate interpolation, the rational-grid denominator and degree bounds, polynomial collection, the period check, induction and height dependence. The small integer solution is proved by the pigeonhole argument in the construction; the norm bound follows from the minimal polynomial of an algebraic integer. The next two-logarithm lessons replace this broad effective argument by interpolation determinants with explicit constants.

## References

- Michel Waldschmidt, *Diophantine Approximation on Linear Algebraic Groups*, Grundlehren der mathematischen Wissenschaften 326, Springer, 2000. [Author's full text](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/dalag.pdf). Effective linear-independence measures, Matveev's degree-indexed polynomials and Baker's auxiliary-function method.
- Michel Waldschmidt, *Linear Independence Measures for Logarithms of Algebraic Numbers*, Lecture Notes in Mathematics 1819, Springer, 2003. [Author's text](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SpringerLN1819-2003.pdf). Quantitative extrapolation and the determinant approach.

## Editable source

[Markdown source](TR-BAKER-05.md).
