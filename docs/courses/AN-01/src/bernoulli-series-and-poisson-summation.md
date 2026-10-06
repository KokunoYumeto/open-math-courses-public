# Bernoulli series and Poisson summation

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied programme foundations retain their stated licences.*

A periodic affine function has a jump at every integer. Its differentiated Fourier series records precisely those jumps as point masses. We use this identity to prove Poisson summation, then construct every periodic Bernoulli polynomial and solve the Schwartz difference equation with an explicit continuous inverse. All formulas below concern the whole distribution, including its lattice contacts.

We use complex bilinear pairings and \(FT(\phi)=T(F\phi)\), with \(F\phi(\xi)=\int e^{-ix\xi}\phi(x)\,dx\). The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves every Schwartz seminorm estimate, Gaussian transform, inversion identity and transposed coordinate rule used here. In particular \(F^2=2\pi R\), where \(R\phi(x)=\phi(-x)\). The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, supplies compactness, calculus, uniform differentiation, trigonometry and smooth cutoffs. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16, supplies convergence, Fubini and substitutions. The right-half-plane logarithm and its derivative are proved in [U017, Lemma H0](complex-powers-at-a-boundary.md). Periodic uniqueness is proved next, rather than assumed from an external reference.

## The sawtooth series and its jumps

For a one-periodic integrable function set \(c_n(v)=\int_0^1v(t)e^{-2\pi int}\,dt\).

**Lemma 0.1 (periodic uniqueness and smooth expansion).** A continuous periodic function is determined by all its coefficients. A smooth periodic function has a Fourier series converging uniformly with every derivative.

**Proof.** Define the finite nonnegative kernel
\[
K_N(t)=\frac1{N+1}\left|\sum_{j=0}^Ne^{2\pi ijt}\right|^2
=\sum_{|n|\le N}\left(1-\frac{|n|}{N+1}\right)e^{2\pi int}.
\]
The last identity follows by counting the pairs \(j-k=n\). Integration of each exponential gives \(\int_0^1K_N=1\). For \(\delta\le t\le1-\delta\), the finite geometric formula bounds \(K_N(t)\) by \(4/((N+1)|1-e^{2\pi it}|^2)\), which tends uniformly to zero there: the continuous denominator has a positive minimum on this compact interval. For continuous periodic \(v\), write
\[
(K_N*v)(x)-v(x)=\int_0^1K_N(t)[v(x-t)-v(x)]\,dt.
\]
Uniform continuity makes the integrand's difference uniformly small near the integer endpoints; away from them the displayed kernel bound makes its integral tend to zero. Thus \(K_N*v\to v\) uniformly. Inserting the finite kernel sum and substituting the periodic variable gives
\[
(K_N*v)(x)=\sum_{|n|\le N}\left(1-\frac{|n|}{N+1}\right)c_n(v)e^{2\pi inx}.
\]
If every coefficient of \(v\) is zero, every convolution is zero, and hence \(v=0\).

For smooth \(v\), integration by parts \(M\) times, with equal endpoint derivatives, gives
\[
|c_n(v)|\le(2\pi|n|)^{-M}\|v^{(M)}\|_{L^1(0,1)}
\quad(n\ne0).
\]
After \(j\) derivatives choose \(M>j+1\); comparison with \(\int_1^\infty t^{-M+j}\,dt\) proves absolute uniform convergence. Uniform convergence of each derivative and the fundamental theorem identify successive derivatives of the sum. Its coefficients equal those of \(v\), by uniform integration and exponential orthogonality, so the preceding uniqueness proof identifies the sum with \(v\). Scaling gives the same conclusions for any positive period. \(\square\)

Let \(B_1(x)=x-\tfrac12\) on \(0<x<1\), extended one-periodically. Assign value zero at integers when discussing its symmetric Fourier series; those values do not change its regular distribution.

**Theorem 1.1.** The coefficients are
\[
c_0=0,\qquad c_n=-\frac1{2\pi in}\quad(n\ne0).
\tag{1.1}
\]
The symmetric series
\[
B_1(x)=-\sum_{n\ne0}\frac{e^{2\pi inx}}{2\pi in}
=-\frac1\pi\sum_{n\ge1}\frac{\sin(2\pi nx)}n
\tag{1.2}
\]
converges pointwise to the stated representative, uniformly on compact sets disjoint from the integers, in \(L^p(0,1)\) for every \(1\le p<\infty\), and strongly in \(\mathcal S'(\mathbb R)\). Here strong convergence means uniform convergence of pairings over every bounded Schwartz test set. Its whole derivatives give
\[
B_1'=1-\sum_{k\in\mathbb Z}\delta_k,\qquad
\sum_{k\in\mathbb Z}\delta_k=\sum_{n\in\mathbb Z}e^{2\pi inx}.
\tag{1.3}
\]
For \(a>0\), put \(C_a=\sum_k\delta_{ak}\). Then
\[
FC_a=\frac{2\pi}{a}C_{2\pi/a},\qquad FC_{2\pi}=C_1.
\tag{1.4}
\]
For every \(f\in\mathcal S(\mathbb R)\),
\[
\sum_{k\in\mathbb Z}f(x+ak)
=\frac1a\sum_{n\in\mathbb Z}Ff(2\pi n/a)e^{2\pi inx/a}.
\tag{1.5}
\]
Both series and every derivative converge absolutely and uniformly on every compact interval. The frequency series converges uniformly on the whole line; the physical series need not do so. Its limit is periodic, but its finite symmetric partial sums are not. For example, a nonnegative compact smooth function, positive at zero and supported in a sufficiently short interval about zero gives a nonzero periodic sum, while each finite physical partial sum vanishes far enough from the origin.

**Proof: ordinary and strong sawtooth convergence.** Integrating \(x-\tfrac12\) over a period gives zero. For \(n\ne0\), one integration by parts gives the boundary contribution \(-1/(2\pi in)\); the remaining integral is a constant multiple of the zero integral of \(e^{-2\pi inx}\). This proves (1.1).

For \(0<\theta<2\pi\), every sum \(\sum_{n=M}^Le^{in\theta}\) has modulus at most \(2/|1-e^{i\theta}|\). If \(A_j=\sum_{n=M}^je^{in\theta}\), the exact summation-by-parts identity
\[
\sum_{n=M}^L\frac{e^{in\theta}}n
=\frac{A_L}{L}+\sum_{j=M}^{L-1}A_j\left(\frac1j-\frac1{j+1}\right)
\]
bounds the sum by \(2/(M|1-e^{i\theta}|)\). This proves convergence and uniform tails away from \(2\pi\mathbb Z\). To determine its value, integrate the uniformly convergent geometric series on each \(0\le r\le r_0<1\). Lemma H0 and the value at \(r=0\) give
\[
\sum_{n\ge1}\frac{r^ne^{in\theta}}n
=-\operatorname{Log}(1-re^{i\theta}).
\tag{1.6}
\]
The argument stays in the right half-plane. For \(0<x<1\),
\(1-e^{2\pi ix}=2\sin(\pi x)e^{i(\pi x-\pi/2)}\); its argument is \(\pi x-\pi/2\). The imaginary part of (1.6) consequently tends to \(\pi/2-\pi x\).

This radial limit equals the already convergent ordinary sum. Indeed, if \(S_m=\sum_{n=1}^mb_n\to S\), then absolute summation, using boundedness of \(S_m\), gives
\[
\sum_{n\ge1}r^nb_n=(1-r)\sum_{m\ge1}r^mS_m.
\]
The weights have total mass \(r\), every fixed weight tends to zero, and \(S_m-S\) is uniformly small in the tail. Splitting into a finite initial part and that tail proves convergence to \(S\). This identifies (1.2) off the integers. At an integer every sine term vanishes.

There is also a bound on the sine partial sums independent of both \(x\) and truncation. Reduce the angle by periodicity and sign to \(0<\theta\le\pi\). For \(\theta\le1\), split at \(M=\lfloor1/\theta\rfloor\): the first \(M\) terms have absolute sum at most \(M\theta\le1\), since \(|\sin(n\theta)|\le n\theta\). The remaining finite tail is bounded by \(2/((M+1)|1-e^{i\theta}|)\), which is uniformly bounded because \(|1-e^{i\theta}|=2\sin(\theta/2)\ge2\theta/\pi\). If the truncation is below \(M\), the first estimate alone suffices. For \(1<\theta\le\pi\), use the geometric bound with \(M=1\), whose denominator is bounded away from zero. Dominated convergence on a period now gives every asserted finite \(L^p\) convergence.

For a Schwartz test \(\phi\), the sum \(\sum_k|\phi(t+k)|\) is bounded on \(0\le t\le1\) by \(C\sup_x(1+|x|)^2|\phi(x)|\). To verify this, use \(|t+k|\ge|k|-1\) for \(|k|\ge2\) and compare the resulting square tail with its integral. Thus a periodic error \(e\) obeys
\[
|\langle e,\phi\rangle|
\le C\|e\|_{L^1(0,1)}
\sup_x(1+|x|)^2|\phi(x)|.
\]
The \(L^1\) convergence just established proves strong tempered convergence, and finite partial-sum pairings give
\[
B_1(\phi)=\sum_{n\ne0}c_nF\phi(-2\pi n).
\tag{1.7}
\]
This paired series is absolutely convergent, with tails uniformly small on bounded Schwartz sets, because Fourier foundation F2 bounds every weighted supremum of \(F\phi\) by finitely many seminorms of \(\phi\).

**A second proof of the strong limit.** The original periodized-test argument also remains valid, now using the proved Lemma 0.1. For \(\phi\in\mathcal S\), its smooth periodization \(P\phi(t)=\sum_k\phi(t+k)\) has coefficient \(F\phi(2\pi n)\), by absolute unfolding. Lemma 0.1 expands it absolutely with every derivative. Pairing that expansion on one period with bounded \(B_1\), and replacing \(n\) by \(-n\), gives (1.7). More explicitly, two integrations by parts give \(|F\phi(\xi)|\le |\xi|^{-2}\|\phi''\|_1\) for nonzero \(\xi\). A fixed weighted Schwartz supremum bounds this \(L^1\) norm, so the paired tail is at most that seminorm times \(C\sum_{|n|>N}|n|^{-3}\). This proves convergence uniformly on bounded test sets independently of the preceding periodic \(L^1\)-error estimate.

**Proof: differentiation, combs and sampling.** Each comb is tempered: for \(M>1\), its absolute test pairing and tail are bounded by a constant times \(\sup_x(1+|x|)^M|\phi(x)|\sum_k(1+|k|)^{-M}\). The same argument applies to each fixed derivative of its atoms. Periodwise integration by parts gives
\[
-\int_{\mathbb R}B_1(t)\phi'(t)\,dt
=\int_{\mathbb R}\phi(t)\,dt-\sum_{k\in\mathbb Z}\phi(k).
\tag{1.8}
\]
At each joining point the left affine trace is \(1/2\) and the right trace is \(-1/2\), producing \(-\phi(k)\). The integrals and boundary series are absolute by Schwartz decay, which justifies summation over all periods.

A continuous map of the Schwartz space sends bounded sets to bounded sets; its transpose therefore preserves strong convergence. Apply this to differentiation of (1.2). The resulting exponential series also converges strongly directly, since its pairings are the rapidly decreasing samples \(F\phi(-2\pi n)\). Comparing its derivative with (1.8) gives (1.3), including the zero mode.

The pullback \(x\mapsto x/a\) sends \(\delta_k\) to \(a\delta_{ak}\), by substituting in its test pairing. Hence \(C_a=a^{-1}\sum_ne^{2\pi inx/a}\). Fourier inversion gives
\(\int e^{ibx}F\phi(x)\,dx=2\pi\phi(b)\), so \(F(e^{ibx})=2\pi\delta_b\). Fourier continuity through the strong series proves (1.4). Pairing its \(a=2\pi\) case with \(g\in\mathcal S\) gives
\[
\sum_{k\in\mathbb Z}g(k)=\sum_{n\in\mathbb Z}Fg(2\pi n).
\tag{1.9}
\]
Take \(g(t)=f(x+at)\). Substitution gives \(Fg(\xi)=a^{-1}e^{ix\xi/a}Ff(\xi/a)\), which proves (1.5) with its scale and phase. On \(0\le x\le a\), every physical derivative series is bounded termwise by \(C_{a,M}p_{M,j}(f)(1+|k|)^{-M}\), where \(p_{M,j}\) is defined below. Each frequency derivative adds only a fixed power of \(n\), absorbed by the arbitrary rapid decrease of \(Ff\). Taking \(M>1\), and larger after frequency differentiation, proves the asserted convergence.

We will also use the exact coefficient identity
\[
\frac1a\int_0^a\left(\sum_kf(x+ak)\right)e^{-2\pi inx/a}\,dx
=\frac1aFf(2\pi n/a).
\]
Absolute Fubini unfolds the intervals \([ak,a(k+1)]\); the exponential is unchanged by their integer shifts. This proves the identity directly. \(\square\)

## Every higher Bernoulli polynomial and its whole derivative

For the polynomial recurrence, use \(B_1(t)=t-\tfrac12\) on the closed interval. Its endpoint values differ from the symmetric series representative, but define the same regular distribution.

**Theorem 1.2.** For \(m\ge2\), define
\[
B_m(x)=m\int_0^xB_{m-1}(t)\,dt-c_m,\qquad
c_m=m\int_0^1\int_0^sB_{m-1}(t)\,dt\,ds.
\tag{B1}
\]
This uniquely specifies a polynomial with \(B_m'=mB_{m-1}\) and zero mean on \([0,1]\). Its endpoints agree. Its periodic extension has series
\[
B_m(x)=-\frac{m!}{(2\pi i)^m}\sum_{n\ne0}\frac{e^{2\pi inx}}{n^m},
\qquad m\ge2,\quad x\in\mathbb R.
\tag{B2}
\]
This series and its derivatives through order \(m-2\) converge absolutely uniformly; the periodic function is \(C^{m-2}\). Its next piecewise derivative has jump \(-m!\) at each integer. The symmetric series for that derivative has midpoint value zero there, with all the pointwise, compact-away, finite-\(L^p\) and strong convergence in Theorem 1.1. The whole identities are
\[
D^{m-1}B_m=m!B_1,\qquad D^mB_m=m!(1-C_1),\qquad
D^{m+r}B_m=-m!D^rC_1\quad(r\ge1).
\tag{B3}
\]
Every fixed distributionally differentiated Fourier series converges strongly. Moreover,
\[
\begin{gathered}
B_m(1-x)=(-1)^mB_m(x),\\
B_{2r+1}(0)=B_{2r+1}(1)=0,\\
B_{2r}(0)=\frac{(-1)^{r+1}2(2r)!}{(2\pi)^{2r}}
\sum_{n\ge1}n^{-2r}\qquad(r\ge1).
\end{gathered}
\tag{B4}
\]

**Proof.** Integrating a polynomial and subtracting its mean proves existence in (B1); the difference of two choices has derivative and mean zero, hence is zero. Since every preceding polynomial has mean zero, \(B_m(1)-B_m(0)=m\int_0^1B_{m-1}=0\). Equal traces cancel all boundary terms in the first distributional derivative, so \(DB_m=mB_{m-1}\). Repeating until \(B_1\), and then applying (1.3), proves (B3). For \(0\le j\le m-2\), the piecewise derivative is \(m!B_{m-j}/(m-j)!\) and its endpoints agree. Successive derivatives therefore glue continuously. The next traces are \(m!/2\) on the left and \(-m!/2\) on the right. Their nonzero jump also shows that no additional ordinary derivative exists globally.

Integration by parts over one period gives
\[
2\pi in\,c_n(B_m)=m\,c_n(B_{m-1}),\qquad
c_n(B_m)=-\frac{m!}{(2\pi in)^m}\quad(n\ne0);
\]
the zero coefficient is zero. The coefficient series is absolutely uniformly convergent for \(m\ge2\), so its sum is continuous with exactly those coefficients. Lemma 0.1 identifies it with \(B_m\). Through \(j=m-2\), derivative coefficients have summable bound \(C_m|n|^{-m+j}\); the fundamental theorem applied successively to uniformly convergent derivative series justifies ordinary differentiation. At order \(m-1\), the symmetric sums equal \(m!\) times the sawtooth sums, proving every asserted convergence and endpoint value. At any fixed higher order their coefficients grow at most polynomially; pairing with \(F\phi(-2\pi n)\) gives an absolutely summable tail controlled by finitely many Schwartz seminorms. Thus all the distributional derivatives are strong limits with the contacts in (B3).

For reflection, the base polynomial satisfies \(B_1(1-x)=-B_1(x)\). If the assertion holds at order \(m-1\), then \(Q(x)=(-1)^mB_m(1-x)\) has derivative \(mB_{m-1}(x)\) and zero mean. The uniqueness already proved gives \(Q=B_m\). At odd orders at least three, equal endpoints and reflection force zero. At order \(2r\), evaluate the uniformly convergent series at zero, pair the positive and negative indices, and use \(i^{2r}=(-1)^r\). This yields (B4). \(\square\)

## A cancelled periodization has one Schwartz difference primitive

Define
\[
P_af(x)=\sum_{k\in\mathbb Z}f(x+ak),\qquad
\Delta_ag(x)=g(x)-g(x+a),\qquad a>0.
\tag{D1}
\]
For periodic \(h\), use \(q_j(h)=\max_{\ell\le j}\sup_{[0,a]}|h^{(\ell)}|\). For Schwartz functions use
\[
p_{N,j}(f)=\sup_x(1+|x|)^N|f^{(j)}(x)|,\qquad N,j\ge0.
\tag{D2}
\]
These are equivalent to the seminorms in Fourier foundation F1.

**Theorem 1.3.** The continuous linear map \(\Delta_a\) is a bijection from \(\mathcal S\) onto \(\ker P_a\). Its continuous inverse is
\[
I_af(x)=\sum_{k\ge0}f(x+ak)=-\sum_{k<0}f(x+ak)
\quad(P_af=0),
\tag{D3}
\]
with locally uniform convergence of every derivative and the explicit bound
\[
p_{N,j}(I_af)\le\left(1+\frac1{a(N+1)}\right)p_{N+2,j}(f).
\tag{D4}
\]
Consequently,
\[
P_af=0
\ \Longleftrightarrow\
Ff(2\pi n/a)=0\text{ for all }n
\ \Longleftrightarrow\
f=\Delta_ag\text{ for a unique }g\in\mathcal S.
\tag{D5}
\]
The map \(P_a\) is continuous and onto \(C^\infty(\mathbb R/a\mathbb Z)\), with a continuous linear right inverse. Thus the following sequence is exact and splits:
\[
0\longrightarrow\mathcal S
\xrightarrow{\Delta_a}\mathcal S
\xrightarrow{P_a}C^\infty(\mathbb R/a\mathbb Z)
\longrightarrow0.
\tag{D6}
\]

**Proof: inverse and continuity.** On every compact \(x\)-interval, \(1+|x+ak|\ge c(1+|k|)\) for all sufficiently large \(|k|\), with \(c>0\) depending on the interval and \(a\). Arbitrary rapid decay therefore proves local uniform convergence of each derivative of either series in (D3). Their equality follows from \(P_af=0\), also after differentiation.

For \(X\ge0\), comparison of a decreasing function with its integral gives
\[
\sum_{k\ge0}(1+X+ak)^{-N-2}
\le(1+X)^{-N-2}
+\frac{(1+X)^{-N-1}}{a(N+1)}.
\tag{D7}
\]
Indeed each term \(k\ge1\) is at most the integral over \(k-1\le t\le k\) of \((1+X+at)^{-N-2}\); integrate its elementary power primitive. For \(x\ge0\), multiply this inequality with \(X=x\) by \(p_{N+2,j}(f)(1+x)^N\), using the positive series. For \(x\le0\), put \(X=-x\) and use the negative series, whose terms have \(|x-ak|=X+ak\) for \(k\ge1\). Its bound is no larger than the same sum beginning at zero. Since the two remaining powers of \(1+X\) are at most one, (D4) follows. This proves that \(I_af\) is Schwartz and that \(I_a\) is continuous on the kernel.

Subtracting the positive series at \(x+a\) from the one at \(x\) leaves \(f(x)\), hence \(\Delta_aI_af=f\). For \(g\in\mathcal S\), the finite periodization telescopes to
\[
\sum_{k=-K}^K\Delta_ag(x+ak)=g(x-aK)-g(x+a(K+1)).
\tag{D8}
\]
Both terms tend to zero uniformly with every derivative on a period; thus \(P_a\Delta_ag=0\). If \(\Delta_ag=0\), then \(g(x)=g(x+ka)\) for every positive integer \(k\); Schwartz decay makes this common value zero. This proves injectivity and uniqueness. Translation obeys
\[
p_{N,j}(g(\,\cdot+a))\le(1+a)^Np_{N,j}(g),
\tag{D9}
\]
because \(1+|x|\le(1+a)(1+|x+a|)\). Thus \(\Delta_a\) is continuous. The coefficient identity after (1.9), or the complete series (1.5), proves the equivalence with the vanishing samples in (D5).

**Proof: compact-window splitting.** Use the supplied flat bump construction to choose \(\chi\ge0\), smooth, supported in \([-a,a]\), and positive on \([-a/2,a/2]\). The locally finite sum \(s(x)=\sum_k\chi(x+ak)\) is smooth and periodic. For every \(x\), some shift lies in that central interval, so \(s(x)>0\). Compactness gives a positive minimum on a period. Therefore
\[
\rho=\frac{\chi}{s},\qquad P_a\rho=1,\qquad
E_ah=\rho h,\qquad P_aE_ah=h.
\tag{D10}
\]
The reciprocal \(1/s\) is smooth by repeated product and chain rules and the positive lower bound. The support of \(E_ah\) is fixed and compact; Leibniz's rule bounds each \(p_{N,j}(E_ah)\) by \(C_{\rho,N,j}q_j(h)\). The lattice bound following (1.9) similarly gives \(q_j(P_af)\le C_{a,M}\max_{\ell\le j}p_{M,\ell}(f)\) for \(M>1\). These prove continuity of both maps.

Set
\[
Q_a=1-E_aP_a,\qquad Q_a^2=Q_a,\qquad
f=\Delta_a I_aQ_af+E_aP_af.
\tag{D11}
\]
The relation \(P_aE_a=1\) proves the projection identity and \(P_aQ_a=0\); the inverse identity proves the decomposition. If another decomposition has a difference term and a term in the range of \(E_a\), applying \(P_a\) fixes the latter and injectivity of \(\Delta_a\) fixes its primitive. This proves exactness, continuity and uniqueness for the chosen window. \(\square\)

## Exercises

**Exercise 1 (foundation: a shifted sawtooth).** For \(a>0\), \(h\in\mathbb R\), set \(B_{a,h}(x)=B_1((x-h)/a)\). Find its derivative and whole Fourier transform, including the exact atomic coefficients.

**Exercise 2 (intermediate: integrate the sawtooth once).** Let \(B_2(x)=x^2-x+1/6\) for \(0\le x\le1\), extended periodically. Prove its complete uniformly convergent Fourier series and deduce \(\sum_{n\ge1}n^{-2}=\pi^2/6\).

**Exercise 3 (intermediate: alternate the Gaussian samples).** For \(b>0\) and \(h\in\mathbb R\), derive a rapidly convergent half-frequency series for
\[
\sum_{k\in\mathbb Z}(-1)^k e^{-b(k+h)^2}.
\]

**Exercise 4 (advanced: a comb with phases).** Let
\[
\begin{gathered}
T_{\alpha,a,h}=\sum_{k\in\mathbb Z}
e^{i\alpha(h+ak)}\delta_{h+ak},\\
a>0,\qquad\alpha,h\in\mathbb R.
\end{gathered}
\]
Find its whole transform and the corresponding phase-weighted Schwartz sampling formula.

**Exercise 5 (intermediate: the periodic interval indicator).** For \(0<c<1\), let \(g_c\) be one-periodic and equal to \(1\) on \((0,c)\), zero on \((c,1)\). Determine its Fourier series, symmetric endpoint values and distributional derivative.

**Exercise 6 (advanced: differentiate the sampled Gaussian identity).** Prove
\[
\begin{gathered}
\sum_{k\in\mathbb Z}k^2e^{-bk^2}\\
=\frac{\sqrt\pi}{2b^{3/2}}\sum_{n\in\mathbb Z}
\left(1-\frac{2\pi^2n^2}{b}\right)e^{-\pi^2n^2/b},\\
b>0.
\end{gathered}
\]
Justify every parameter derivative.

**Exercise 7 (advanced: solve a mean-zero periodic point-source equation).** Find the unique mean-zero periodic distribution \(G\) satisfying \(-G''=C_1-1\). For \(0<c<1\), find the continuous mean-zero solution \(u\) of \(-u''=C_1-C_{c+\mathbb Z}\), with an explicit formula on one period.

**Exercise 8 (intermediate: exact cancellation of a periodization).** For Schwartz \(f\), prove that \(\sum_k f(x+ak)\) vanishes identically if and only if \(Ff(2\pi n/a)=0\) for every integer \(n\). Give a nonzero Schwartz example for each \(a>0\).

**Exercise 9 (intermediate: the next exact endpoint sums).** Starting with (B1), compute \(B_4\) and \(B_6\), including all constants. Deduce the sums of \(n^{-4}\) and \(n^{-6}\). Find the complete fourth derivative of periodic \(B_4\) and the jump in its third derivative.

**Exercise 10 (advanced: retain the scale in every contact term).** Let \(m\ge2\), \(a>0\), \(h\in\mathbb R\), and \(b(x)=B_m((x-h)/a)\). Find its complete Fourier transform, its \(m\)-th and every higher whole derivative, and the jump of its \((m-1)\)-st piecewise derivative. Specify the convergence and the exact atom coefficients.

**Exercise 11 (intermediate: a second difference retains a second moment).** Let \(a>0\), \(v(x)=e^{-x^2}\), and \(f=\Delta_a^2v\). Find its unique Schwartz difference primitive, its full Fourier transform, and the exact order of every sampling-lattice zero of that transform. Compute \(\int f\), \(\int xf(x)\,dx\) and \(\int x^2f(x)\,dx\), with every translation sign retained.

**Exercise 12 (advanced: a compact window separates a periodic signal).** Fix the window \(\rho\) of (D10), set \(h(x)=1+2\cos(2\pi x/a)\), and let \(f=\rho h+\Delta_a(e^{-x^2})\). Determine \(P_af\), all samples \(Ff(2\pi n/a)\), and both components and the primitive in (D11). For a second admissible window \(\sigma\), prove that the changed primitive is still Schwartz and give its exact difference from the first primitive.

## Solutions

**Solution 1.** Substitute \((x-h)/a\) in (1.2):
\[
B_{a,h}(x)=-\sum_{n\ne0}\frac{e^{-2\pi inh/a}}{2\pi in}e^{2\pi inx/a}.
\]
An affine change carries bounded Schwartz sets to bounded Schwartz sets by its finite chain rule and weight comparison, so the series remains strongly convergent. Periodwise integration by parts gives ordinary slope \(1/a\) and jump \(-1\), hence
\[
B_{a,h}'=\frac1a-\sum_k\delta_{h+ak},\qquad
FB_{a,h}=-\sum_{n\ne0}\frac{e^{-2\pi inh/a}}{in}\delta_{2\pi n/a}.
\]
The Fourier formula follows by transforming each plane wave, whose multiplier is \(2\pi\). Rapid test decay proves strong absolute convergence of the atom series. This also checks that the scale changes locations without adding an extra coefficient \(1/a\).

**Solution 2.** Direct integration gives mean zero for \(x^2-x+1/6\), and its derivative is \(2B_1\). The equal endpoint values make its periodic extension continuous. It is therefore precisely the polynomial in (B1) at \(m=2\). Formula (B2), already proved with uniform convergence and uniqueness, gives
\[
B_2(x)=\sum_{n\ne0}\frac{e^{2\pi inx}}{2\pi^2n^2}
=\frac1{\pi^2}\sum_{n\ge1}\frac{\cos(2\pi nx)}{n^2}.
\]
Evaluation at zero is legitimate by uniform convergence; \(B_2(0)=1/6\) proves \(\sum_{n\ge1}n^{-2}=\pi^2/6\).

**Solution 3.** Apply (1.9) to \(g(t)=e^{i\pi t}e^{-b(t+h)^2}\). The substitution \(y=t+h\) and Fourier foundation F3 give
\[
Fg(\xi)=\sqrt{\pi/b}\,e^{ih(\xi-\pi)}e^{-(\xi-\pi)^2/(4b)}.
\]
Consequently
\[
\begin{aligned}
\sum_k(-1)^ke^{-b(k+h)^2}
&=\sqrt{\pi/b}\sum_n e^{2\pi i(n-1/2)h}e^{-\pi^2(n-1/2)^2/b}\\
&=2\sqrt{\pi/b}\sum_{m\ge0}
e^{-\pi^2(m+1/2)^2/b}\cos(2\pi(m+1/2)h).
\end{aligned}
\]
The second line pairs opposite half-integers. Gaussian decay gives absolute convergence, uniform for \(h\) in compact intervals and \(b\) in compact subsets of \((0,\infty)\). Both sides change sign when \(h\) is increased by one, as also follows by reindexing the physical sum.

**Solution 4.** Unit-modulus coefficients and the lattice bound make \(T_{\alpha,a,h}\) tempered. Translation of \(C_a\) multiplies its transform by \(e^{-ih\xi}\); modulation by \(e^{i\alpha x}\) replaces \(\xi\) with \(\xi-\alpha\). Both rules follow by substitution in the Schwartz integral and then transposition. Evaluating the resulting phase at each shifted atom gives
\[
FT_{\alpha,a,h}
=\frac{2\pi}{a}\sum_ne^{-2\pi inh/a}\delta_{\alpha+2\pi n/a}.
\]
For the sampling identity use \(g(t)=e^{i\alpha(h+at)}f(h+at)\). Substitution gives \(Fg(\xi)=a^{-1}e^{ih\xi/a}Ff(\xi/a-\alpha)\), so
\[
\sum_ke^{i\alpha(h+ak)}f(h+ak)
=\frac1a\sum_ne^{2\pi inh/a}Ff(2\pi n/a-\alpha).
\]
Both sums are absolute by Schwartz decay. The positive phase here comes from the change of variables in the transformed test; the negative atomic phase above comes from translating the distribution.

**Solution 5.** On the two open subintervals, direct substitution of the fractional coordinates gives
\[
g_c(x)=c+B_1(x-c)-B_1(x)
=c+\sum_{n\ne0}\frac{1-e^{-2\pi inc}}{2\pi in}e^{2\pi inx}.
\]
At \(x=0\), the right side's symmetric value is \(c+(1/2-c)-0=1/2\); at \(x=c\) it is \(c+0-(c-1/2)=1/2\). Theorem 1.1 gives its value at every other point, all compact-away convergence, finite-\(L^p\) convergence and strong convergence. Differentiating the two whole sawtooth identities yields
\[
g_c'=C_1-\sum_k\delta_{c+k}.
\]
Thus each upward jump contributes \(+1\) and each downward jump contributes \(-1\).

**Solution 6.** Gaussian transformation and (1.9) give
\[
\sum_ke^{-bk^2}=\sqrt{\pi/b}\sum_ne^{-\pi^2n^2/b}.
\]
For \(b_0\le b\le b_1\), every fixed parameter derivative on the left is bounded by \(C(1+|k|)^Le^{-b_0k^2}\); on the right it is bounded by \(C(1+|n|)^Le^{-\pi^2n^2/b_1}\). These majorants are summable: the exponential series bounds any polynomial by a constant times half the Gaussian decay, and a Gaussian tail is bounded by a summable inverse square. Uniform differentiation is therefore justified to every finite order. Taking minus one derivative gives
\[
\sum_kk^2e^{-bk^2}
=\frac{\sqrt\pi}{2b^{3/2}}
\sum_n\left(1-\frac{2\pi^2n^2}{b}\right)e^{-\pi^2n^2/b}.
\]
Both the derivative of \(b^{-1/2}\) and that of the exponential are retained.

**Solution 7.** Since \(B_2''=2(1-C_1)\), the first solution is \(G=B_2/2\), with mean zero and coefficients \(1/(4\pi^2n^2)\) at \(n\ne0\). Uniqueness can be proved directly for distributions. If \(T'=0\), fix a compact smooth \(\eta\) with integral one. For any compact test \(\psi\), the function \(\psi-(\int\psi)\eta\) has a compact smooth primitive \(\Psi(x)=\int_{-\infty}^x[\psi(t)-(\int\psi)\eta(t)]\,dt\). Therefore \(T(\psi)-T(\eta)\int\psi=T(\Psi')=-T'(\Psi)=0\), so \(T\) is constant. If \(T''=0\), apply this to \(T'\), then subtract the corresponding linear function and apply it again; \(T=cx+d\). Periodicity forces \(c=0\), and mean zero forces \(d=0\). This proves uniqueness without assuming a distributional Fourier expansion.

For the second equation take \(u(x)=G(x)-G(x-c)\). It is continuous, periodic and mean zero. On a period its explicit form is
\[
u(x)=
\begin{cases}
(c-1)x+c(1-c)/2,&0\le x\le c,\\
cx-c(c+1)/2,&c\le x\le1.
\end{cases}
\]
Expansion of the two quadratic pieces of \(G\), using \(x-c+1\) in the first interval, proves this formula. Its values match at \(c\) and at the period endpoints. The derivative jumps by \(+1\) at \(c\) and by \(-1\) at the integers, so \(-u''=C_1-C_{c+\mathbb Z}\). The same uniqueness argument applies.

**Solution 8.** Absolute unfolding after (1.9) gives \(c_n(P_af)=a^{-1}Ff(2\pi n/a)\). If the periodization vanishes, its coefficients vanish. If all samples vanish, (1.5), or Lemma 0.1, makes the periodization zero. For each \(a>0\), let \(v(x)=e^{-x^2}\) and \(f(x)=v(x)-v(x+a)\). Then \(f(0)=1-e^{-a^2}>0\), while
\[
Ff(\xi)=(1-e^{ia\xi})\sqrt\pi e^{-\xi^2/4}
\]
vanishes at every \(2\pi n/a\). Absolute reindexing of the physical periodization gives the same cancellation.

**Solution 9.** Integrate \(mB_{m-1}\) successively and subtract its mean, as required by (B1). The resulting polynomials are
\[
\begin{aligned}
B_2&=x^2-x+\tfrac16,\\
B_3&=x^3-\tfrac32x^2+\tfrac12x,\\
B_4&=x^4-2x^3+x^2-\tfrac1{30},\\
B_5&=x^5-\tfrac52x^4+\tfrac53x^3-\tfrac16x,\\
B_6&=x^6-3x^5+\tfrac52x^4-\tfrac12x^2+\tfrac1{42}.
\end{aligned}
\tag{B5}
\]
Every derivative has the required factor \(m\). Integrating the versions with zero constant term gives respectively the means \(-1/6,0,1/30,0,-1/42\), by \(\int_0^1x^j=1/(j+1)\). This verifies every displayed integration constant. In particular (B4) gives
\[
-\frac1{30}=-\frac{48}{(2\pi)^4}\sum_{n\ge1}n^{-4},\qquad
\frac1{42}=\frac{1440}{(2\pi)^6}\sum_{n\ge1}n^{-6},
\]
\[
\sum_{n\ge1}n^{-4}=\frac{\pi^4}{90},\qquad
\sum_{n\ge1}n^{-6}=\frac{\pi^6}{945}.
\tag{B6}
\]
These endpoint evaluations use absolute uniform series. Periodic \(B_4\) is \(C^2\), its third piecewise derivative is \(24B_1\) with jump \(-24\), and its whole fourth derivative is \(24-24C_1\).

**Solution 10.** Substitute the affine coordinate into (B2), then transform the absolutely uniformly convergent series using the full plane-wave rule:
\[
Fb=-\frac{2\pi m!}{(2\pi i)^m}
\sum_{n\ne0}\frac{e^{-2\pi inh/a}}{n^m}\delta_{2\pi n/a}.
\tag{B7}
\]
The physical series and derivatives through order \(m-2\) are uniformly convergent; order \(m-1\) has the rescaled sawtooth convergence. Every higher derivative series and the displayed atom series converge strongly, since the corresponding coefficients have at most polynomial growth and every Schwartz test has arbitrarily rapid lattice decay.

The piecewise \((m-1)\)-st derivative is \(m!a^{-(m-1)}B_1((x-h)/a)\), with jump \(-m!a^{-(m-1)}\). Periodwise integration by parts, or the chain rule with \(\delta_k((x-h)/a)=a\delta_{h+ak}\), now gives
\[
D^mb=\frac{m!}{a^m}-\frac{m!}{a^{m-1}}\sum_k\delta_{h+ak},
\qquad
D^{m+r}b=-\frac{m!}{a^{m-1}}\sum_k\delta_{h+ak}^{(r)}
\quad(r\ge1).
\tag{B8}
\]
There is no additional power of \(a\) on further derivatives of atoms at fixed physical locations: \(\delta_y^{(r)}(\phi)=(-1)^r\phi^{(r)}(y)\). This pairing also proves the strong absolute convergence of every atom-derivative series. In (B7) the factor \(2\pi\) comes from the plane wave itself, so no extra factor \(1/a\) appears in its coefficients.

**Solution 11.** Direct expansion and Theorem 1.3 give
\[
f(x)=v(x)-2v(x+a)+v(x+2a),\qquad
I_af=v-v(\,\cdot+a).
\tag{D12}
\]
The latter is Schwartz and has difference \(f\), proving that it is the unique primitive. Gaussian transformation gives
\[
Ff(\xi)=(1-e^{ia\xi})^2\sqrt\pi e^{-\xi^2/4}.
\tag{D13}
\]
At \(\xi=2\pi n/a\), the unsquared factor has derivative \(-ia\ne0\), and the Gaussian factor is nonzero. Thus every lattice zero has exactly order two. These are its only real zeros because \(e^{ia\xi}=1\) exactly on this lattice.

For a translated term use \(t=x+ja\). Its first three moments are \(\sqrt\pi\), \(-ja\sqrt\pi\), and \(\int t^2e^{-t^2}\,dt+j^2a^2\sqrt\pi\), since the odd Gaussian moment is zero. With coefficients \(1,-2,1\), the constant and linear terms in \(j\) cancel, while \(0^2-2+4=2\). Therefore
\[
\int f=0,\qquad \int xf(x)\,dx=0,\qquad
\int x^2f(x)\,dx=2a^2\sqrt\pi.
\tag{D14}
\]
All integrals are absolute. Differentiating (D13) twice at zero gives \(-2a^2\sqrt\pi=-\int x^2f\), an independent sign check.

**Solution 12.** Periodicity of \(h\) and \(P_a\rho=1\) give \(P_a(\rho h)=h\); the difference term periodizes to zero by (D8). The Fourier coefficients of \(h=1+e^{2\pi ix/a}+e^{-2\pi ix/a}\) and the unfolded coefficient identity therefore give
\[
P_af=h,\qquad
Ff(2\pi n/a)=
\begin{cases}a,&n=0,1,-1,\\0,&\text{otherwise}.\end{cases}
\tag{D15}
\]
The components for the original window are \(E_aP_af=\rho h\), \(Q_af=\Delta_av\), and \(I_aQ_af=v\). Modulation gives the full compact-component transform
\[
F(\rho h)(\xi)=F\rho(\xi)+F\rho(\xi-2\pi/a)+F\rho(\xi+2\pi/a).
\tag{D16}
\]
Indeed \(P_a\rho=1\) gives the samples \(F\rho(2\pi n/a)=a\) for \(n=0\), zero otherwise, which independently verifies (D15).

For another compact smooth window \(\sigma\) with \(P_a\sigma=1\), the compact component is \(\sigma h\), and \(Q_a^\sigma f=\Delta_av+(\rho-\sigma)h\). The last term is compact smooth and periodizes to zero. Consequently its primitive is Schwartz by the full estimate (D4), and linearity and uniqueness give the exact change
\[
I_aQ_a^\sigma f-v=I_a[(\rho-\sigma)h].
\tag{D17}
\]
Both one-sided sums in (D3) represent this difference and satisfy every bound (D4). The periodic signal and all its Fourier samples are unchanged.

## References

- Peter Woit, [*Fourier Analysis Notes, Spring 2020*](https://www.math.columbia.edu/~woit/fourier-analysis/fouriernotes.pdf), 3 September 2020, §2.1, pp. 9–10: periodization, Fourier coefficients and Poisson summation. The source uses the exponent \(-2\pi ix\xi\); the present lesson proves every convergence step and fixes its own normalization.
- NIST, [*Digital Library of Mathematical Functions*, §24.8(i)](https://dlmf.nist.gov/24.8), formulas 24.8.1–24.8.3 and their real endpoint domains. These free scalar formulas are a comparison source; Lemma 0.1 and Theorems 1.1–1.3 supply the proofs, convergence, contacts and difference estimates.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), §7.2, pp. 177–181, DOI 10.1007/978-3-642-61497-2: Poisson summation and periodic distributions. Its subgroup-support proof and cotangent-boundary argument differ from the sawtooth and finite-kernel proofs given here; no book proof or exercise is incorporated by reference.
- Programme connection: the bundled [closed-subgroup Poisson theorem](../prerequisites/HA-LCA-724d1a8/src/the-poisson-summation-formula.md#ha-lca-11-theorem-1-1), [convolution tests](../prerequisites/HA-LCA-724d1a8/src/the-poisson-summation-formula.md#ha-lca-11-proposition-1-2), [classical formula](../prerequisites/HA-LCA-724d1a8/src/the-poisson-summation-formula.md#ha-lca-11-corollary-2-1) and [Euclidean-lattice formula](../prerequisites/HA-LCA-724d1a8/src/the-poisson-summation-formula.md#ha-lca-11-corollary-2-2) preserve the broader route. The Haar, quotient, inversion and Plancherel proofs are supplied in the same bundle. On an arbitrary locally compact abelian group, averaging first defines an integrable class. Actual coset integration uses the stated Borel representative supported in an open sigma-compact subgroup; every completed-measurable representative is permitted when the group is sigma-compact. An everywhere absolutely convergent continuous average agrees with the inverse-transform formula everywhere. The provider uses cycles per unit length; its frequency is the angular frequency here divided by two pi, and the lattice coefficient is the reciprocal covolume. The complete one-dimensional Schwartz proof above is retained independently. [Edition and exact proof scope](../prerequisites/HA-LCA-724d1a8/AN01-INTEGRATION.md).
- All programme proof providers are linked above and supplied with the lesson. External research PDFs are not reproduced. Licensed prerequisite components retain their required original source packages and notices. Bibliographical cross-references alone are not used as proof inputs.
