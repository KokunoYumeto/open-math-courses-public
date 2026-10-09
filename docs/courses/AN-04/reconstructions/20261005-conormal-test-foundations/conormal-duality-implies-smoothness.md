# When conormal regularity and duality force smoothness

This is the complete smoothness argument of AN03-U034, *Global boundary operators, compressed wave fronts, and normal extension*, Section 7.1 and Sections 8.1–8.6 through (SP15). Original author credit: Codex, September 2026, CC0. Current prerequisite connections and the final identification of the supported representative: AN-04 course-writing task and OpenAI Codex, 5 October 2026, CC0.

The [conormal amplitude and Besov proofs](conormal-amplitudes-and-test-spaces.md) supply (C2) and (C16). The supported test spaces, approximation, full dual pairing and intrinsic trace supply (GA1)–(GA2), (GD1)–(GD12) and their actual topologies. The full [Fourier Sobolev embedding](../20261005-restored-first-order-cauchy/spacetime-symbol-composition.md), [Hölder inequality](../20261005-cauchy-foundations/integration-and-duality.md) supply the elementary analytic entries. The exact interpolation identity (SP11) is also proved directly below.

The mathematical antecedent is the approved Hörmander III, 2007 eBook, Section 18.3. The same distribution is used throughout the argument.

## 1. The weighted norm with its complete order shift

Localize in a compact boundary product chart. An element
\(u\in\mathcal A^m\) has, modulo a smooth term, the exact
normal conormal oscillatory representation
\[
 u(x',t)=(2\pi)^{-1}\int_{\mathbb R}
         e^{it\tau}a(x',\tau)\,d\tau,
 \qquad
 |D_{x'}^\beta\partial_\tau^j a(x',\tau)|
     \le C_{\beta j}\langle\tau\rangle^{\mu-j},
 \quad \mu=m+\frac{n-2}{4}.
 \tag{HS1}
\]
This is the *original* codimension-one shift, including the
ambient dimension. The inverse coefficient and \(D=-i\partial\)
convention are retained. For a normal derivative of order
\(a\ge0\), the amplitude is \(\tau^aD_{x'}^\beta a\), of
order \(\mu+a\). Split its integral at \(|\tau|=t^{-1}\),
\(0<t<1\). The low-frequency absolute integral is bounded by
\(Ct^{-\mu-a-1}\) when \(\mu+a>-1\), by
\(C(1+|\log t|)\) at equality, and by \(C\) below it.
On the high-frequency part integrate by parts in \(\tau\)
\(N>\mu+a+1\) times, including the derivatives of a smooth
cutoff at \(|\tau|=t^{-1}\). Each resulting term is bounded
by \(Ct^{-\mu-a-1}\). The same estimate holds for every
tangential derivative, uniformly on a smaller compact chart.
Thus the complete safe weighted \(L^2\) implication is
\[
 \int_{K_0}\int_0^c
     t^{2\nu}|D'^\beta D_n^a u(x',t)|^2
                       \,dt\,dx'<\infty
 \quad\text{whenever }
 \nu\ge0,\quad \nu>m+\frac n4+a.
 \tag{HS2}
\]
The strict inequality covers the logarithmic case. Equation
(HS2) states the weight *inside the norm* as \(t^\nu\);
the power inside the squared integral is \(2\nu\). 
## 2. Smoothness from the dual conormal condition

### 2.1. Every boundary delta jet and its precise conormal order

For a compact smooth tangential density \(h(x')\), the normal
delta derivative has the original Fourier representation
\[
 h(x')\otimes\delta^{(j)}(t)
  =(2\pi)^{-1}\int e^{it\tau}(i\tau)^j h(x')\,d\tau,
 \qquad
 m_j=\frac{2-n}{4}+j=\frac12-\frac n4+j.
 \tag{SP1}
\]
The exponent \(m_j\) follows from the *unmodified*
codimension-one order relation in (C16): the amplitude has
order \(j=m_j+(n-2)/4\). The factor \((2\pi)^{-1}\) and
\(i^j\) have not been absorbed. Formula (GA1) gives the
same order by dyadic estimation, including every tangent
derivative. For \(u\in\mathcal A'\) define
\(g_j=(\nabla_n^{\mathrm{int},j}u)|_{t=0}\) by (GD8)–(GD9).
These are tangential distributions at this stage. For a smooth
boundary \(u\), direct differentiation and the distributional
delta sign give
\[
 u(h\otimes\delta^{(j)})=(-1)^j
       \langle\partial_t^ju|_{t=0},h\rangle
       =(-i)^j\langle g_j,h\rangle.
 \tag{SP2}
\]
Both sides are weakly continuous on \(\mathcal A'\): the left
is one of its defining conormal-test pairings by (SP1), and
the right is a composition of the weakly continuous corrected
derivative and trace maps (GD8)–(GD9). Smooth functions are
weakly dense by (GD5), so (SP2) holds for *every*
\(u\in\mathcal A'\), with no assertion that the ambient
uncorrected derivative has the same trace.

### 2.2. Quantitative scaled test expansion in the actual topology

Fix \(J=[1,2]\) and a compact tangential chart set. For
\(\psi\in C_c^\infty(X_0\times(1,2))\), put
\[
 v_\varepsilon(x',t)=\varepsilon^{-1}
                 \psi(x',t/\varepsilon),\qquad
 M_j(x')=\int_1^2s^j\psi(x',s)\,ds.
 \tag{SP3}
\]
The test is smooth and supported in the interior for each
\(\varepsilon>0\). Taylor's formula at the *actual* boundary
gives the distributional expansion
\[
 v_\varepsilon
  =\sum_{j=0}^{N-1}
      \frac{(-1)^j\varepsilon^j}{j!}
          M_j(x')\otimes\delta^{(j)}(t)
       +R_{N,\varepsilon}.
 \tag{SP4}
\]
We need its quantitative conormal topology, not only
distributional convergence. For every integer \(N\ge1\),
real \(M>m_\delta+N\) with \(m_\delta=(2-n)/4\), compact output
set \(K\), and finite tangent seminorm index \(L\), there
are finite \(L'\), \(C\) such that
\[
 p_{M,K,L}(R_{N,\varepsilon})
       \le C\varepsilon^N
             \sum_{|\gamma|\le L'}
                   \|D_{x',s}^\gamma\psi\|_{L^\infty},
       \qquad0<\varepsilon\le1.
 \tag{SP5}
\]
Here the original Besov index is \(\kappa=-M-n/4\);
the strict condition is exactly \(\kappa+N+1/2<0\).

For completeness, Fourier transform (SP4) in \(t\). Its
normal factor is
\[
 \int_1^2e^{-i\varepsilon s\tau}\psi(x',s)\,ds
   -\sum_{j=0}^{N-1}
       \frac{(-i\varepsilon\tau)^j}{j!}M_j(x').
 \tag{SP6}
\]
For \(\varepsilon|\tau|\le1\), Taylor's integral
remainder bounds (SP6), with every tangential derivative,
by \(C\varepsilon^N|\tau|^N\); for
\(\varepsilon|\tau|\ge1\), the Schwartz integral and all
retained polynomial terms bound it by
\(C(\varepsilon|\tau|)^{N-1}\). The tangential Fourier
transform decays faster than any power of \(|\xi'|\), with
constants controlled by finitely many displayed \(\psi\)
derivatives. On a full dyadic block \(|(\xi',\tau)|\asymp2^l\),
the \(L^2\) size in the normal frequency contributes
\(2^{l/2}\). For \(2^l\le\varepsilon^{-1}\), multiplying
by \(2^{l\kappa}\) gives
\(C\varepsilon^N2^{l(\kappa+N+1/2)}\), bounded by
\(C\varepsilon^N\). For \(2^l\ge\varepsilon^{-1}\), it
gives
\(C\varepsilon^{N-1}2^{l(\kappa+N-1/2)}\), whose
maximum is \(C\varepsilon^{-\kappa-1/2}\le
C\varepsilon^N\) under the same strict condition.
The low block is bounded directly by the Taylor remainder.
Tangentially dominant blocks gain arbitrary decay from the
\(x'\)-Fourier transform and obey the same inequality.
Applying \(D'\) differentiates \(\psi\). Applying
\(tD_t\) to (SP4) rescales the same test and acts on each
\(\delta^{(j)}\) by its exact eigenvalue
\(tD_t\delta^{(j)}=i(j+1)\delta^{(j)}\); the Taylor
remainder still has the two bounds above. The triangular
identity (GA2) therefore supplies every weighted derivative
seminorm, proving (SP5) with all lower terms retained.

The dual estimate (GD3), used at this freely chosen high
order \(M\), turns (SP5) into
\[
 |u(R_{N,\varepsilon})|
       \le C_{u,N,K}\varepsilon^N
              \sum_{|\gamma|\le L'}
                     \|D_{x',s}^\gamma\psi\|_\infty.
 \tag{SP7}
\]
This is an estimate of distributions in \((x',s)\) of a
finite negative Sobolev order, since a sufficiently high
Sobolev norm controls the finite smooth-test seminorm.

### 2.3. The scaled Taylor series in distributions

An element \(u\in\mathcal A'\) is smooth in the open collar
only when it also lies in \(\mathcal A\). Assume that
intersection from now on, and set
\(F_\varepsilon(x',s)=u(x',\varepsilon s)\) for \(s\in J\).
For every \(\psi\) in (SP3), the change of variables gives
\(\langle F_\varepsilon,\psi\rangle=u(v_\varepsilon)\).
Insert (SP4), then use the exact sign (SP2). The two
\((-1)^j\) factors cancel, leaving
\[
 F_\varepsilon(x',s)
  =\sum_{j=0}^{N-1}
      \frac{i^j\varepsilon^j s^j}{j!}g_j(x')
        +O_{H^{-L_N}(K_0\times J)}(\varepsilon^N)
 \quad\text{for every }N\ge1.
 \tag{SP8}
\]
The remainder means (SP7) uniformly on compact tangential
sets; \(L_N\) is finite but may depend on \(N\). Formula
(SP8) is an *all-order distribution-valued* boundary Taylor
series, with the original \(i^j\) from \(D=-i\partial\).
No smoothness of \(g_j\) has been assumed.

### 2.4. One fixed conormal growth exponent for every derivative

Let \(u\in\mathcal A^m\), with the original normal amplitude
order \(\mu=m+(n-2)/4\). The frequency split in (HS1)–(HS2)
gives, after enlarging a fixed exponent slightly to absorb a
possible logarithm, a number
\(A>\max(\mu+1,0)\) such that for *every* normal derivative
order \(a\), tangential multiindex \(\beta\), and compact
subchart there is a constant \(C_{a\beta}\) with
\[
 \sup_{(x',s)\in K_0\times J}
  |D_{x'}^\beta\partial_s^a F_\varepsilon(x',s)|
       \le C_{a\beta}\varepsilon^{-A}.
 \tag{SP9}
\]
Indeed \(\partial_s^a F_\varepsilon
=\varepsilon^a\partial_t^au(x',\varepsilon s)\);
the conormal amplitude order rises by exactly \(a\), so
its high-frequency bound contains
\(\varepsilon^a\varepsilon^{-\mu-a-1}
=\varepsilon^{-\mu-1}\). The low-frequency and logarithmic
cases satisfy the same enlarged \(A\). Crucially the exponent
\(A\) is independent of \(a\) and \(\beta\), although the
constants depend on them. Thus for every integer \(K\),
\(\|F_\varepsilon\|_{H^K(K_0\times J)}
\le C_K\varepsilon^{-A}\).

We record the precise smoothing inference used below. Suppose
smooth \(h_\varepsilon\) on a fixed compact coordinate box obey
\(\|h_\varepsilon\|_{H^K}\le C_K\varepsilon^{-A}\)
for all \(K\), and for every \(N\) obey
\(\|h_\varepsilon-h\|_{H^{-L_N}}
\le C_N\varepsilon^N\), where \(h\) is a distribution.
Then \(h\) is smooth. Fix any one positive integer \(N\), and
retain its finite negative order \(L_N\). On a compact subbox insert
a fixed smooth cutoff before using full Fourier blocks; multiplication
preserves the displayed Sobolev bounds. For any \(a>0\), choose
\(\varepsilon=2^{-al}\). The low- and high-Sobolev block bounds give
\[
 \|\Delta_l h\|_2
 \le C_N 2^{l(L_N-aN)}
           +C_K2^{l(aA-K)}.
 \tag{SP10}
\]
For any requested \(r\ge0\), choose \(a>(L_N+r+2)/N\),
then an integer \(K>aA+r+2\). Both exponents in (SP10) are
strictly less than \(-r-2\), so it gives
\(\|\Delta_l h\|_2\le C_r2^{-l(r+2)}\) for every
\(r\). Summing their squared \(H^r\) weights proves membership
in every local Sobolev space, and the Fourier Sobolev estimate proves
smoothness. This argument uses the actual \(L_N\); it does not assert
one negative order valid for all Taylor degrees. The single positive
degree \(N=1\) would suffice for this smoothing inference.

### 2.5. Smoothness of every boundary coefficient

The expansion (SP8) includes lower powers of \(\varepsilon\),
so apply an exact finite scale cancellation. For any integer
\(N\ge1\), take distinct positive scales
\(\lambda_1,\ldots,\lambda_N\), for example \(1,\ldots,N\),
and the Lagrange interpolation coefficients at zero
\[
 c_l=\prod_{r\ne l}
          \frac{-\lambda_r}{\lambda_l-\lambda_r},
 \qquad
 \sum_{l=1}^{N}c_l\lambda_l^j
          =\begin{cases}1,&j=0,\\0,&1\le j<N.
            \end{cases}
 \tag{SP11}
\]
To verify the identity for every displayed degree, the polynomials
\(L_l(z)=\prod_{r\ne l}(z-\lambda_r)/(\lambda_l-\lambda_r)\)
equal one at their own node and zero at the others. For a polynomial of degree less than \(N\), subtract its interpolation sum: the difference has those \(N\) distinct roots and degree less than \(N\), so it is zero, by successive division by its linear factors. Evaluation at zero gives (SP11), with every sign shown. This also covers \(N=1\).

For \(g_0\), set
\(G_{N,\varepsilon}=\sum_lc_lF_{\lambda_l\varepsilon}\).
Equations (SP8) and (SP11) make
\(G_{N,\varepsilon}=g_0+O_{H^{-L_N}}(\varepsilon^N)\).
Equation (SP9) gives every high Sobolev norm bounded by
\(C_{K,N}\varepsilon^{-A}\). The dyadic argument (SP10),
with the adjustable scale specified there, proves
\(g_0\in C^\infty\).

Proceed by induction. If \(g_0,\ldots,g_{j-1}\) are smooth,
define on \(s\in J\)
\[
 H_{j,\varepsilon}(x',s)
  =j!i^{-j}s^{-j}\varepsilon^{-j}
      \left[F_\varepsilon(x',s)
       -\sum_{k=0}^{j-1}
          \frac{i^k\varepsilon^ks^k}{k!}g_k(x')\right].
 \tag{SP12}
\]
The factor \(s^{-j}\) is smooth on \(J\), and every
term is a smooth function there. Formula (SP8), taken to
order \(N+j\), gives
\(H_{j,\varepsilon}=g_j+\sum_{l=1}^{N-1}
\varepsilon^l h_l(x',s)+O_{H^{-L}}(\varepsilon^N)\),
where the \(h_l\) may still be distributions. The same
Lagrange weights (SP11) cancel all intermediate powers.
The high derivative bound (SP9), the smooth already-known
coefficients and (SP12) give
\(\|H_{j,\varepsilon}\|_{H^K}
\le C_{jK}\varepsilon^{-(A+j)}\). The dyadic
argument proves \(g_j\in C^\infty\). Induction proves
\[
 g_j\in C^\infty(\partial X)
       \quad\text{for every }j\ge0.
 \tag{SP13}
\]
The argument uses the same original \(u\) at every step;
it neither assumes nor constructs an unrelated boundary
extension.

### 2.6. Upgrading the whole series and removing the weight

Now every coefficient in (SP8) is smooth. Fix a desired
integer \(N\) and a smooth seminorm order \(r\). Expand (SP8)
through some \(N'>N\), so the remainder is
\(O_{H^{-L_{N'}}}(\varepsilon^{N'})\). Its high
\(H^K\) norm is at most \(C_K\varepsilon^{-A}\) by (SP9)
and the smooth polynomial terms. Interpolation between
\(H^{-L_{N'}}\) and \(H^K\) gives the required bound as follows.
Choose an integer \(d>r+n/2\), then \(N'>N+A\), retaining its
actual finite \(L=L_{N'}\). With \(K>d\), Fourier Hölder gives
the \(H^d\) exponent
\(\theta N'-(1-\theta)A\), where
\(\theta=(K-d)/(K+L)\). Choose \(K\) so large that
\(\theta>(N+A)/(N'+A)\); the exponent is then greater than
\(N\). The Fourier Sobolev bound \(H^d\hookrightarrow C^r\)
proves \(O_{C^r}(\varepsilon^N)\). The discarded coefficients
of degrees \(N,\ldots,N'-1\) contribute the same
\(O_{C^r}(\varepsilon^N)\). Hence the full exact Taylor
statement is
\[
 u(x',\varepsilon s)
  =\sum_{j=0}^{N-1}
       \frac{i^j\varepsilon^js^j}{j!}g_j(x')
       +O_{C^r(K_0\times J)}(\varepsilon^N)
 \quad\text{for every }N,r.
 \tag{SP14}
\]
Taking any fixed interior value, for example \(s=3/2\)
and \(\varepsilon=2t/3\), then differentiating in \(s\)
and \(x'\) before that restriction, shows that every ordinary mixed
derivative of \(u\) has a continuous boundary limit with
the precise Taylor coefficient in (SP14). This proves
\(u\in C^\infty(X)\). Conversely a smooth boundary function
belongs to \(\mathcal A\) by (GD1)–(GD2), and to
\(\mathcal A'\) by the smooth pairing and (GD3). Therefore,
as spaces of their actual supported representatives,
\[
 \mathcal A'(X)\cap\mathcal A(X)=C^\infty(X).
 \tag{SP15}
\]

## 3. Identification of the actual supported representative

The preceding bounds give an interior smooth function whose derivatives of every order extend continuously to the boundary. To check the derivative interpretation there, apply the fundamental theorem of calculus on \(t>0\) and pass to zero using the uniform limits. Repeating it for each tangential and normal derivative proves smoothness up to the boundary with precisely the jets in (SP14). In passing from a scaled \(s\)-derivative of order \(a\) to an ordinary \(t\)-derivative, the remainder acquires \(\epsilon^{-a}\); choose its Taylor degree \(N>a\) before taking the limit. Thus that step retains every ordinary derivative, not just the scaled ones.

Let \(v\) be this smooth boundary function, represented by zero extension. It belongs to \(\mathcal A'\) by the smooth-pairing proof and to \(\mathcal A\) by (GD1)–(GD2). The original distribution \(u-v\) belongs to \(\mathcal A'\) and has zero interior restriction. Injectivity (GD4) makes it zero. This proves (SP15) for the actual supported distributions as stated, including the absence of an unnoticed boundary-delta summand.
