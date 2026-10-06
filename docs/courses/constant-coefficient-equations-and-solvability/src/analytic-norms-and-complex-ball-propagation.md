# Analytic norms and propagation on complex balls

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The characteristic Cauchy estimate uses two different kinds of propagation. The norm of a tangential Fourier transform on the negative time axis has exactly the exponential type of its spatial support there. A plurisubharmonic function which is substantially negative on one small ball must also be negative at every interior point of a larger ball. We prove both facts, including the norm endpoints, the zero norm case and a constant independent of the center of the small ball.

Read [Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The normed target and its analytic map

Fix a positive moderate weight \(k\) on \(\mathbb R\), with constants \(C,N\) as in([equation 1 in Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md)), and \(1\le p\le\infty\). Let
\[
\begin{gathered}
Y=\mathcal S(\mathbb R)/\mathcal N,\\
\qquad
 \|[f]\|_Y=\|f\|^-_{p,k},\\
\qquad
 \mathcal N=\{f\in\mathcal S:f(t)=0\text{ for }t<0\}.
\end{gathered}
\tag{1}
\]
[Equation 4 in Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md) proves that this is a norm. The quotient map \(Q:\mathcal S\to Y\) is continuous for the Schwartz topology, because the quotient norm is at most the full-line weighted norm.

Here is a finite seminorm estimate making that continuity precise for functions supported in one fixed time interval \([-T,T]\), \(T>0\). Choose an integer \(J>N+1\). Integration by parts in the time transform, together with the direct integral bound when \(|\xi|\le1\), gives
\[
\begin{gathered}
\|f\|_{p,k}\le A_{p,k,T,J}
        \max_{0\le j\le J}\sup_t|\partial_t^j f(t)|,
 \\
\qquad \operatorname{supp}f\subset[-T,T].
\end{gathered}
\tag{2}
\]
Indeed \[
\begin{gathered}
|\widehat f(\xi)|\\
\le A_{T,J}(1+|\xi|)^{-J}\max_{j\le J}\|\partial_t^j f\|_\infty
\end{gathered}
\]

The weight bound \(k(\xi)\le k(0)(1+C|\xi|)^N\) makes its product integrable in every finite \(L^p\), and bounded at \(p=\infty\). Retain the factor \((2\pi)^{-1/p}\) when forming \(A_{p,k,T,J}\). Every integration by parts has zero boundary terms because \(f\) is smooth and compactly supported. No density assertion at infinity is involved.

Let \(d\ge1\), and write \(x\in\mathbb R^d\) for the spatial variables and \(t\in\mathbb R\) for time. For \(v\in C_c^\infty(\mathbb R^{d+1})\), put
\[
\begin{gathered}
f_z(t)=\int_{\mathbb R^d}e^{-ix\cdot z}v(x,t)\,dx,\\
\qquad
 F(z)=Qf_z,\\
\qquad V(z)=\|F(z)\|_Y,\\
\quad z\in\mathbb C^d.
\end{gathered}
\tag{3}
\]
The functions \(f_z\) have a common compact time support. They form an entire Schwartz-valued map and hence an entire normed-space-valued map into \(Y\). To prove this assertion explicitly, fix \(z_0\). On the compact spatial support, expand each factor of \(e^{-ix\cdot h}\). If \(|x_j|\le S\) there, the coefficient of \(h^\alpha\) has every time derivative bounded by a constant times \(S^{|\alpha|}/\alpha!\). Its time support is fixed, so every Schwartz seminorm has the same bound with its own constant. The series of absolute seminorm bounds is at most a constant times \(\prod_j e^{S|h_j|}\), uniformly on bounded sets of \(h\). Thus
\[
\begin{gathered}
f_{z_0+h}(t)=
 \sum_{\alpha\in\mathbb N^d}\frac{h^\alpha}{\alpha!}
       \\
\int_{\mathbb R^d}(-ix)^\alpha e^{-ix\cdot z_0}v(x,t)\,dx
 \\\text{in }\mathcal S.
\end{gathered}
\tag{4}
\]
Equation(2) passes the series and all its local derivatives into \(Y\). In particular \(F\) is norm-continuous, and every continuous complex-linear functional \(\ell\) on \(Y\) makes \(\ell F\) holomorphic. Completeness of \(Y\) is unnecessary: the limits just used already exist as actual Schwartz functions before passage to the quotient.

## The local subharmonic facts used here

We use the following convention. A subharmonic function is upper semicontinuous, with values in \([-\infty,\infty)\), locally integrable unless it is identically \(-\infty\) on its component, and satisfies the circle-mean inequality on every sufficiently small disk about each point. A plurisubharmonic function is upper semicontinuous and has subharmonic or identically \(-\infty\) restrictions to complex lines. The identically \(-\infty\) case is permitted.

First, \(\log|g|\) is subharmonic for a scalar holomorphic \(g\), with \(\log0=-\infty\). At a nonzero value \(g(a)\), shrink the disk until \(g/g(a)=1+h\) with \(|h|<1\). The convergent series \(L=\sum_{j\ge1}(-1)^{j+1}h^j/j\) is holomorphic there. Differentiating its locally uniformly convergent series gives \(L'=h'/(1+h)\); hence \(e^{-L}(1+h)\) has derivative zero and equals one at the center, where \(h=0\). Thus \(e^L=1+h\), and taking moduli proves \(\operatorname{Re}L=\log|g/g(a)|\). The circle mean of its real part equals its center value by the local Cauchy formula. At a zero, the circle-mean inequality has the left side \(-\infty\). The local factorization \(g(z)=(z-a)^m b(z)\), \(b(a)\ne0\), follows from the first nonzero term of the Cauchy series. It also proves local integrability of \(\log|g|\), since \(\log|z-a|\) is integrable in a disk and on every circle not reduced to that point. If all series coefficients vanish, the identity principle gives the identically zero case on that component. These arguments also prove that \(\log|z-a|\) is harmonic away from \(a\).

**Lemma 1 (logarithm of an analytic norm).** If \(G\) is a continuous analytic map from a complex domain into a complex normed space, in the sense of locally norm-convergent power series, then \(\log\|G\|\) is plurisubharmonic.

**Proof.** Norm-continuity makes this function upper semicontinuous, including at zeros: if \(\|G(z_0)\|=0\), it tends below every finite logarithmic bound near \(z_0\). Fix a complex line. If \(G\) is identically zero on its line component, the restriction is identically \(-\infty\). Otherwise choose a point on that component where \(G\ne0\). The scalar norm test B6 gives a continuous functional \(\ell\) with \(\|\ell\|=1\) and \(|\ell G|=\|G\|\) at that point. The scalar holomorphic function \(\ell G\) is not identically zero. On every compact part of this line,
\[
\begin{gathered}
\log|\ell G(z)|\le\log\|G(z)\|,
 \\
\qquad
 \|y\|=\sup_{\|\ell\|\le1}|\ell(y)|.
\end{gathered}
\tag{5}
\]
The scalar lower bound is locally integrable, and the norm has a locally bounded logarithmic upper bound. Thus the logarithm of the norm is locally integrable on the line.

At any center \(z_0\) with \(G(z_0)\ne0\), choose a norming functional at that center. On a sufficiently small disk its scalar function is nonzero and its logarithm has the exact circle mean just proved. Since \(\log\|G\|\ge\log|\ell G|\) on the circle and equality holds at the center, the circle-mean inequality follows. At a zero the inequality is immediate. This proves subharmonicity on every line and hence the assertion. The Hahn–Banach theorem applies to the normed space itself; no completed quotient or endpoint approximation has been assumed. \(\square\)

We will also use the following maximum comparison. If a subharmonic \(u\) is defined in a bounded plane domain \(D\) and \(\limsup_{z\to b,\ z\in D}u(z)\le0\) at every boundary point \(b\), then \(u\le0\) in \(D\). Here the domain has compact boundary, as in the disks and annuli below. For a proof, add \(\varepsilon|z|^2\). Its circle mean exceeds its center value by \(\varepsilon\rho^2\) on a circle of radius \(\rho\). A positive excess of \(u+\varepsilon|z|^2\) over its boundary supremum would attain an interior maximum: upper semicontinuity gives attainment on a compact interior part, and the boundary upper limits exclude the rest. The strict circle-mean inequality contradicts that maximum. Consequently \(u(z)\le\varepsilon(\sup_{\overline D}|z|^2-|z|^2)\); let \(\varepsilon\downarrow0\). Subtracting a harmonic function preserves the circle-mean inequality, so the same argument compares a subharmonic function to a harmonic boundary majorant. The identically \(-\infty\) case satisfies every such comparison.

## Exact spatial exponential type of the restriction

**Theorem 2.** Suppose \(v\in C_c^\infty(\mathbb R^{d+1})\) and
\[
\begin{gathered}
|x|\le M\\
\quad\text{on }\operatorname{supp}v\cap\{t<0\},
 \\
\qquad M\ge0.
\end{gathered}
\tag{6}
\]
For every moderate \(k\) on the time frequency and every \(1\le p\le\infty\), the function \(\log V\) in(3) is plurisubharmonic, and
\[
\begin{gathered}
V(z)\le e^{M|\operatorname{Im}z|}B,\\
\qquad
 B=\sup_{\xi\in\mathbb R^d}V(\xi)<\infty.
\end{gathered}
\tag{7}
\]

**Proof.** Lemma1 applies to the analytic map \(F\), so it gives the first assertion, including zero restrictions.

There is a subtlety in the support hypothesis: the positive-time portion of \(v\) may have larger spatial support. For each \(\varepsilon>0\), choose a smooth compact spatial cutoff \(\chi_\varepsilon\) equal to one on \(\{|x|\le M\}\), with support in \(\{|x|<M+\varepsilon\}\). Such a cutoff follows from the smooth cutoff construction; it also exists when \(M=0\). Set \(v_\varepsilon=\chi_\varepsilon v\). Its partial Fourier transform has exactly the same restriction to \(t<0\) as \(f_z\), so it gives the same \(F(z)\) and \(V(z)\). All time supports still lie in one fixed \([-T,T]\).

For every integer \(L\ge0\) and each \(j\le J\), tangential integration by parts gives
\[
\begin{gathered}
\sup_t\left|\partial_t^j\int e^{-ix\cdot z}v_\varepsilon(x,t)\,dx\right|
 \\
\le A_{\varepsilon,j,L}(1+|z|)^{-L}
                e^{(M+\varepsilon)|\operatorname{Im}z|}.
\end{gathered}
\tag{8}
\]
For \(|z|\ge1\), choose a coordinate with \(|z_q|\ge |z|/\sqrt d\), and integrate \(L\) derivatives in that coordinate. Its exact factor is \((iz_q)^{-L}\); the derivatives land on \(v_\varepsilon\), and every remaining exponential has modulus at most \(e^{(M+\varepsilon)|\operatorname{Im}z|}\). For \(|z|\le1\), use the direct compact integral bound and enlarge the constant. These are estimates in the full complex norm \(|z|\), not just in \(|\operatorname{Re}z|\). Apply(2) to obtain
\[
 V(z)\le A_{\varepsilon,L}(1+|z|)^{-L}
                 e^{(M+\varepsilon)|\operatorname{Im}z|}.
 \tag{9}
\]
In particular \(B\) is finite.

Fix real \(\xi,\eta\in\mathbb R^d\), with \(\eta\ne0\), and a number \(b>B\). On the upper half-plane define
\[
\begin{gathered}
u(w)\\
=\log V(\xi+w\eta)-\log b
                   \\
-(M+\varepsilon)|\eta|\operatorname{Im}w.
\end{gathered}
\tag{10}
\]
It is subharmonic or identically \(-\infty\): the first term is a complex-line restriction, and the subtracted imaginary part is harmonic. On the real axis its upper limits are at most zero by upper semicontinuity and \(V\le B<b\). On an upper semicircle \(|w|=R\), equation(9), with \(L=1\), gives
\[
\begin{gathered}
u(w)\le \log(A_{\varepsilon,1}/b)
               \\
-\log(1+|\xi+w\eta|),\\|\xi+w\eta|\ge R|\eta|-|\xi|.
\end{gathered}
\tag{11}
\]
Thus its upper boundary values on that arc are at most zero for every sufficiently large \(R\). The maximum comparison on the upper half-disk shows \(u\le0\) at each fixed point of the upper half-plane. At \(w=i\), this gives \(V(\xi+i\eta)\le b e^{(M+\varepsilon)|\eta|}\). Let \(b\downarrow B\), then \(\varepsilon\downarrow0\). This proves(7), even when \(B=0\), since every \(b>0\) was permitted in that case. For \(\eta=0\), the assertion is the definition of \(B\). No constants need to remain bounded as \(\varepsilon\downarrow0\): each cutoff first gives a maximum comparison with the same real-axis bound \(B\). \(\square\)

Dimension \(d=0\) consists of one tangential point, so \(V\) is a constant and the norm estimate is equality. No line argument is needed. When \(M=0\) and \(d\ge1\), a smooth \(v\) supported spatially in a single point at negative times is zero there, so \(V=0\); the proof also covers it directly.

## Moving a negative ball toward the center

**Lemma 3 (centered comparison).** Let \(w\) be plurisubharmonic on \(B(c,R)\subset\mathbb C^d\), \(d\ge1\). If \(w\le0\) on this ball and \(w\le-a\) on \(B(c,r)\), where \(a>0\) and \(0<r<R\), then for \(r<|z-c|<R\),
\[
 w(z)\le a\,\frac{\log(|z-c|/R)}{\log(R/r)}.
 \tag{12}
\]
For all \(z\in B(c,R)\), including \(z=c\), it follows that
\[
\begin{gathered}
w(z)\\
\le \frac{a}{\max(1,\log(R/r))}
                      \left(\frac{|z-c|}{R}-1\right).
\end{gathered}
\tag{13}
\]

**Proof.** Restrict \(w\) to the complex line \(c+\lambda e\), with \(e=(z-c)/|z-c|\) at a point \(z\ne c\). It is subharmonic or identically \(-\infty\). Choose \(0<\rho<r\) and \(|z-c|<R'<R\). On the annulus \(\rho<|\lambda|<R'\), compare it to the harmonic function \(a\log(|\lambda|/R')/\log(R'/\rho)\). On the inner circle that function is \(-a\), and on the outer circle it is zero. The stated bounds on \(w\), and its upper semicontinuity at these circles, permit the maximum comparison. Let \(\rho\uparrow r\) and \(R'\uparrow R\); this proves(12). This limiting argument uses inner circles actually contained in the negative ball and does not assume an extra boundary value on \(|\lambda|=r\).

For \(|z-c|>r\), use \(\log q\le q-1\) for \(q>0\). If \(\log(R/r)\ge1\), this immediately gives(13). If it is less than one, dividing the negative number \(q-1\) by it gives an even smaller number, so the same estimate with denominator one holds. For \(|z-c|<r\), the right side of(13) is at least \(-a\), which is already an upper bound for \(w\). At \(|z-c|=r\), the annular comparisons with \(\rho<r\) give the limiting bound \(-a\). At \(z=c\) use the negative-ball bound. \(\square\)

The case \(r=R\) also has(13), interpreted with denominator one, directly from \(w\le-a\) on the whole ball.

**Theorem 4 (a center-independent propagation constant).** Suppose \(w\) is plurisubharmonic on \(B(0,R)\), \(R>0\), and
\[
\begin{gathered}
w\le0\text{ on }B(0,R),\\
\qquad
 w\le-1\text{ on }B(c,r)\subset B(0,R),\\
\quad 0<r\le R.
\end{gathered}
\tag{14}
\]
There is a number \(\delta(R,r)>0\), depending only on \(r/R\), such that
\[
\begin{gathered}
w(z)\le\delta(R,r)\left(\frac{|z|}{R}-1\right),
               \\
\qquad |z|<R.
\end{gathered}
\tag{15}
\]
One explicit choice is
\[
\begin{gathered}
A=\max(1,\log3),\\\alpha=\frac1{9A},\\K=\min\{k\in\mathbb N_0:\\
(4/3)^k r>2R/3\},\\\delta(R,r)=\frac{\alpha^K}{\max(1,\log(2R/r))}.
\end{gathered}
\tag{16}
\]

**Proof.** Inclusion of the balls implies \(|c|+r\le R\). Track a ball \(B(c_j,r_j)\) on which \(w\le-a_j\), beginning with \(c_0=c\), \(r_0=r\), \(a_0=1\). Its inclusion in \(B(0,R)\) is preserved below.

If \(|c_j|\le r_j/2\), the centered ball \(B(0,r_j/2)\) lies in \(B(c_j,r_j)\), and we stop. Otherwise move the center toward zero by \(r_j/2\):
\[
 c_{j+1}=c_j-\frac{r_j}{2}\frac{c_j}{|c_j|}.
 \tag{17}
\]
The following containments retain the centers and radii:
\[
\begin{gathered}
B(c_{j+1},r_j/2)\subset B(c_j,r_j),\\
\qquad
 B(c_{j+1},3r_j/2)\subset B(0,R).
\end{gathered}
\tag{18}
\]
The first follows from a displacement of \(r_j/2\). For the second,
\(|c_{j+1}|+3r_j/2=|c_j|+r_j\le R\).
Apply Lemma3 to the ball of radius \(3r_j/2\), with inner radius \(r_j/2\) and amplitude \(a_j\). On the ball with radius \(4r_j/3\), its linear bound gives
\[
\begin{gathered}
w\le-\frac{a_j}{9\max(1,\log3)}=-\alpha a_j,\\
\qquad
 r_{j+1}=4r_j/3,\\
\quad a_{j+1}=\alpha a_j.
\end{gathered}
\tag{19}
\]
The strict outer radius yields the indicated weak upper bound throughout this open smaller ball. It is still contained in the original ball, since
\(|c_{j+1}|+r_{j+1}=|c_j|+5r_j/6\le R\).

If we have not stopped after \(K\) moves, then \(r_K=(4/3)^K r>2R/3\). Its inclusion gives \(|c_K|\le R-r_K<r_K/2\), so we stop at that step. There are at most \(K\) moves. At the stopping step \(j\le K\), the centered negative ball has radius \(r_j/2\ge r/2\), and its negative amplitude is \(a_j=\alpha^j\ge\alpha^K\). In particular \(w\le-\alpha^K\) on \(B(0,r/2)\). Apply(13) once more on \(B(0,R)\), with this inner radius and amplitude. The result is exactly(15)–(16). It does not depend on the starting center or on the complex dimension. \(\square\)

For completeness this constant is no worse than a fixed power of the small-ball ratio. Put \(\gamma=\log(1/\alpha)/\log(4/3)>0\). If \(r\le2R/3\), minimality gives \(K\le1+\log(2R/(3r))/\log(4/3)\); if \(r>2R/3\), then \(K=0\). In either case \(\alpha^K\ge\alpha(r/R)^\gamma\). Also \(\max(1,\log(2R/r))\le2R/r\), by \(\log s\le s-1\). Consequently
\[
 \delta(R,r)\ge\frac{\alpha}{2}(r/R)^{\gamma+1}.
 \tag{20}
\]
This estimate keeps every scale and constant explicit; it is a proved lower bound for one valid propagation constant, rather than a claim of optimality.

## Exercises with complete solutions

**Exercise 1 — basic: an analytic vector norm.** For \(G(z)=(1,z)\in\mathbb C^2\) with its Euclidean norm, compute the planar Laplacian of \(\log\|G(z)\|\). Explain how Lemma1 also deals with the zero of \(G_0(z)=z\).

**Solution.** Write \(z=x+iy\). Differentiating \(\tfrac12\log(1+x^2+y^2)\) twice in each real coordinate gives
\[
 \Delta\log\|(1,z)\|=\frac{2}{(1+|z|^2)^2}\ge0.
 \tag{21}
\]
Its strict positive value agrees with the subharmonic norm theorem. For \(G_0(z)=z\), the function is \(\log|z|\), harmonic away from zero. At zero its value is \(-\infty\), which is upper semicontinuous and satisfies the circle-mean inequality there. Local integrability follows from the radial logarithmic integral. Removing that value or replacing it by a positive finite value would fail upper semicontinuity or the circle-mean condition. A zero of an analytic map therefore creates no exception to Lemma1.

**Exercise 2 — intermediate: the exponent comes from the negative-time support.** In spatial dimension one, let \(M>0\) and \(0<\varepsilon<M\). Choose a smooth nonnegative \(g\) supported in \([M-\varepsilon,M]\), positive on its interior, and a nonzero smooth \(h\) supported in a compact interval of negative times. For \(v(x,t)=g(x)h(t)\), calculate \(V\), its real-axis supremum and its exponential rate on the positive imaginary axis.

**Solution.** The written flat cutoff gives such a \(g\) by a product of two flat positive factors, with its endpoints as stated. The partial transform is \(\widehat g(z)h(t)\). Homogeneity of the exact quotient norm and its nondegeneracy give
\[
\begin{gathered}
V(z)=|\widehat g(z)|\,\|h\|^-_{p,k},\\
\qquad
 B=\left(\int g(x)\,dx\right)\|h\|^-_{p,k}>0.
\end{gathered}
\tag{22}
\]
Indeed \(|\widehat g(\xi)|\le\int g\) on the real axis, and equality holds at \(\xi=0\). At \(z=iy\), \(y>0\), the integral is positive and at most \(e^{My}\int g\). For any \(s<M\) sufficiently close to \(M\), the interval \(s<x<M\) contains positive \(g\)-mass, giving \(\widehat g(iy)\ge e^{sy}\int_s^M g(x)\,dx\). Divide logarithms by \(y\), let \(y\to\infty\), and then \(s\uparrow M\). It follows that
\[
 \lim_{y\to\infty}\frac{\log V(iy)}y=M.
 \tag{23}
\]
Thus replacing \(M\) by a smaller constant in this norm estimate fails for this example. Adding a spatially more distant smooth term supported entirely at positive times changes a chosen full-line representative but leaves every \(F(z)\), \(V(z)\) and the sharp rate above unchanged.

**Exercise 3 — advanced: dependence on the small radius is necessary.** On the unit ball in \(\mathbb C^d\), \(d\ge1\), let \(0<r<1/2\). Construct a plurisubharmonic \(w_r\le0\) which is \(-1\) on the centered ball of radius \(r\), but tends to zero at a point of radius \(1/2\) as \(r\downarrow0\). Explain what this says about \(\delta\).

**Solution.** Lemma1, applied to the identity map into \(\mathbb C^d\), shows that \(\log|z|\) is plurisubharmonic, with value \(-\infty\) at zero. Define
\[
\begin{gathered}
w_r(z)=\max\left(-1,\frac{\log|z|}{\log(1/r)}\right),
 \\
\qquad w_r(0)=-1.
\end{gathered}
\tag{24}
\]
A finite maximum of two subharmonic functions is subharmonic: at a center choose the larger branch, use its local circle-mean inequality and bound it by the maximum on the circle. It is upper semicontinuous and locally integrable. Apply this on every complex line; in the identically \(-\infty\) branch case the constant branch suffices. Thus the displayed maximum is plurisubharmonic. It is at most zero for \(|z|<1\), and equals \(-1\) for \(|z|\le r\). At any point of radius \(1/2\), the logarithmic branch is larger than \(-1\), so its value is \(-\log2/\log(1/r)\), which tends to zero. If(15) had one positive constant independent of \(r\), it would require this value to be at most minus half that constant, a contradiction. The theorem's dependence on \(r/R\) is therefore necessary.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
