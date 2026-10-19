# Support normals and analytic singularities

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Original exposition: CC0.*

A distribution cannot stop across a supporting surface while remaining analytically regular in either of its normal directions. The proof first turns regularity in one frequency ray into continuation of a Cauchy transform. Tangential projection then reduces the several-variable assertion to that one-dimensional argument.

We use the bounded compact-support sequence definition of analytic wavefront. Its localization and the analytic coordinate and proper-projection rules are proved in [Pulling back and combining analytic singularities][P], Sections 2, 4, 6 and 7. Analytic multiplication and ordinary-wavefront inclusion are proved in [Analytic directions of holomorphic boundary values][A]. The Cauchy derivative estimates and holomorphic identity theorem are the elementary complex-analysis inputs in [Cauchy bounds and root counts][C]. The normalized simple-pole boundary limit is Theorem 4.1 of [Cauchy kernels and distributional boundary limits][K]. [Schwartz functions and Fourier inversion][F], Sections F1-F5, proves the Fourier estimates and inversion used below. All uses below specify their scope; we do not require an analytic pseudodifferential operator or a preparation theorem.

## 1. A regular frequency ray continues the Cauchy transform

Our Fourier convention in one dimension is
\[
 \widehat v(\xi)=v_t(e^{-it\xi}).
 \tag{SN1}
\]
For a compactly supported distribution \(v\), an exponential or a kernel in a pairing is multiplied by any fixed smooth cutoff equal to one near its support. The pairing is independent of that cutoff.

Suppose \((0,+1)\notin\operatorname{WF}_A(w)\). There are a fixed neighborhood \(J\) of zero and distributions \(w_N\), all supported in one compact set and bounded there with one common distributional order, such that \(w_N=w\) on \(J\) and
\[
 |\widehat w_N(\xi)|
 \le A^{N+1}N^N(1+\xi)^{-N},
 \qquad \xi>0,\quad N\ge1.
 \tag{SN2}
\]
In one dimension the positive open cone is the whole positive ray. A common compact distributional bound also gives a polynomial Fourier bound with fixed constants and order. This is exactly the analytic sequence criterion, not an exponential estimate for one fixed smooth cutoff.

Choose \(v=\chi w\), with \(\chi=1\) on a smaller neighborhood of zero and compact support inside the interval on which \(w\) is defined. Define
\[
 C_v(z)=\frac1{2\pi i}\,v_t\!\left(\frac1{t-z}\right),
 \qquad \operatorname{Im}z\ne0.
 \tag{SN3}
\]
Differentiation of the kernel in a common compact test seminorm shows that this is holomorphic in each half-plane.

**Lemma 1.1.** Under (SN2), the upper-half-plane function \(C_v\) extends holomorphically through zero.

**Proof.** For \(\operatorname{Im}z>0\), elementary integration gives
\[
 \frac1{t-z}=i\int_0^\infty e^{i(z-t)\xi}\,d\xi.
 \tag{SN4}
\]
The exponential decay at positive height allows every finite number of \(t\)-derivatives to pass under the integral. The fixed compact distributional estimate therefore justifies pairing this identity with \(w_N\), first on finite integration intervals and then in the corresponding test seminorm. It follows that
\[
 C_{w_N}^{(k)}(z)
   =\frac1{2\pi}\int_0^\infty
        (i\xi)^k e^{iz\xi}\widehat w_N(\xi)\,d\xi.
 \tag{SN5}
\]
Take \(N=k+2\). Substitution \(s=\xi/(1+\xi)\) proves the exact integral identity
\[
 \int_0^\infty \xi^k(1+\xi)^{-k-2}\,d\xi
   =\int_0^1s^k\,ds=\frac1{k+1}.
 \tag{SN6}
\]
Thus, uniformly for all \(z\) in the upper half-plane,
\[
 |C_{w_{k+2}}^{(k)}(z)|
 \le \frac{A^{k+3}(k+2)^{k+2}}{2\pi(k+1)}
 \le B^{k+1}k!
 \tag{SN7}
\]
with one \(B\). To check the last conversion without an asymptotic assumption, for \(k\ge1\) the increasing function \(\log t\) gives
\[
 \log(k!)\ge\int_1^k\log t\,dt=k\log k-k+1.
 \tag{SN8}
\]
Also \((1+2/k)^k\le e^2\), and any fixed polynomial in \(k\) is bounded by a fixed exponential. These facts bound the ratio in (SN7) by a fixed exponential in \(k\). Increase \(B\) once for \(k=0\).

There is \(a>0\), independent of \(N\), such that \(d_N=v-w_N\) vanishes on \((-a,a)\). The family \(d_N\) has a common compact support and one uniform finite-order estimate, say of order \(m\). For \(|z|<a/4\), insert a smooth compact cutoff equal to one on that support and zero on \((-a/2,a/2)\). On the support of this cutoff the denominator stays a fixed distance from zero. The finite-order estimate and the derivative formula for \((t-z)^{-1}\) give
\[
 |C_{d_N}^{(k)}(z)|
   \le C^{k+1}(k+m)!
   \le D^{k+1}k!,
 \qquad |z|<a/4,
 \tag{SN9}
\]
uniformly in \(N\). Fixed powers of \(k+m\) are again absorbed into \(D^{k+1}\). The cutoff can be used because \(d_N\) vanishes on the excluded interval. Kernel derivatives on the cutoff transition have the same bound.

Since \(C_v=C_{w_{k+2}}+C_{d_{k+2}}\) above the real axis, (SN7)–(SN9) imply
\[
 |C_v^{(k)}(z)|\le E^{k+1}k!,
 \qquad |z|<a/4,\quad \operatorname{Im}z>0.
 \tag{SN10}
\]
Choose a positive \(\delta\) sufficiently small that \(i\delta\) lies in this region and \(4\delta<1/E\). The Taylor series at \(i\delta\) converges on a disk of radius at least \(1/E\). It agrees with \(C_v\) near its center by holomorphic Taylor expansion. The identity theorem makes it agree on the connected intersection with the upper half-plane. That disk contains a neighborhood of zero, proving the extension. No one cutoff has been asserted to have exponentially decreasing Fourier transform. \(\square\)

## 2. One-sided vanishing forces both analytic frequency rays

**Lemma 2.1.** Let \(w\) be a distribution on an interval about zero. If it vanishes on either \((0,b)\) or \((-b,0)\), with \(b>0\), and \((0,+1)\notin\operatorname{WF}_A(w)\), then it vanishes on a neighborhood of zero.

**Proof.** Use the compact localization \(v\) above, chosen equal to \(w\) near zero, and let \(G\) be the extension in Lemma 1.1. On the stated side interval, \(v=0\). Its Cauchy kernel pairing is consequently holomorphic across each point of that interval: its support stays away from a sufficiently small complex disk around the point. On the upper part of that disk it equals \(G\), so the identity theorem identifies its lower part with \(G\) as well. On a small lower half-disk about zero, \(C_v\) and \(G\) are both holomorphic. They agree on the open lower patch just found, hence on that connected half-disk.

The difference of the two Cauchy values at positive height is
\[
 C_v(x+i\epsilon)-C_v(x-i\epsilon)
   =v_t\!\left(\frac{\epsilon}
        {\pi((t-x)^2+\epsilon^2)}\right).
 \tag{SN11}
\]
The sign follows directly by subtracting the two denominators in (SN3). The right side is \(P_\epsilon*v\), where
\[
 P_\epsilon(s)=\frac{\epsilon}{\pi(s^2+\epsilon^2)},
 \qquad P_\epsilon\ge0,\quad\int_{\mathbb R}P_\epsilon=1.
 \tag{SN12}
\]
The normalization follows by the arctangent antiderivative, or from the simple-pole boundary formula. For every compact smooth test \(\phi\), \(P_\epsilon*\phi\to\phi\) uniformly with every fixed finite number of derivatives: write the difference as the integral of \(\phi(x-s)-\phi(x)\); on \(|s|<r\) use uniform continuity, and on \(|s|\ge r\) use
\[
 \int_{|s|\ge r}P_\epsilon(s)\,ds
 \le \frac{2\epsilon}{\pi r}.
 \tag{SN13}
\]
The same argument applies to each test derivative. Pairing in the compact distributional seminorm proves \(P_\epsilon*v\to v\) in distributions. Compactly supported localization in \(t\) justifies all kernel pairings; (SN11) can equivalently be obtained by applying the exact simple-pole limit to the convolved test.

On a smaller real interval both branches in the left side of (SN11) are restrictions of the same holomorphic \(G\). Their difference tends uniformly to zero there, and therefore tends to zero distributionally. Its other limit is \(v\). Hence \(v=0\), and so \(w=0\), near zero. The argument uses only that there is a zero interval on one side; either side works. \(\square\)

**Corollary 2.2.** If \((t,+1)\notin\operatorname{WF}_A(w)\) for every \(t\) in a connected open interval \(I\), and \(w\) vanishes on a nonempty open subinterval, then \(w=0\) on \(I\).

**Proof.** Let \(J\) be the maximal connected open interval on which \(w=0\) and which contains the given zero interval. If an endpoint of \(J\) lies in \(I\), Lemma 2.1 extends vanishing through that endpoint, a contradiction. Thus \(J=I\). This proves uniqueness, not full analyticity of \(w\). \(\square\)

Conjugation changes the frequency sign exactly. For a complex-linear distribution define \(\overline w(\phi)=\overline{w(\overline\phi)}\). Directly,
\[
 \widehat{\overline{w_N}}(\xi)
       =\overline{\widehat w_N(-\xi)},\qquad
 \operatorname{WF}_A(\overline w)
       =\{(x,-\xi):(x,\xi)\in\operatorname{WF}_A(w)\}.
 \tag{SN14}
\]
Indeed, conjugating a bounded compact-support analytic sequence retains all its bounds and its equality on the neighborhood. This proves one inclusion; conjugating twice proves the reverse. Conjugation leaves support unchanged.

## 3. A supporting analytic function produces a singular normal

**Theorem 3.1.** Let \(u\in\mathcal D'(X)\), where \(X\subset\mathbb R^n\) is open. Suppose \(x_0\in\operatorname{supp}u\), \(h\) is real-valued and real analytic near \(x_0\), and
\[
 dh(x_0)\ne0,\qquad h(x)\le h(x_0)
 \quad\hbox{for }x\in\operatorname{supp}u\hbox{ near }x_0.
 \tag{SN15}
\]
Then
\[
 (x_0,dh(x_0)),\ (x_0,-dh(x_0))
          \in\operatorname{WF}_A(u).
 \tag{SN16}
\]
The statement is local. It requires no compact support for \(u\).

**Proof.** Translate \(x_0\) to zero and subtract the constant value \(h(x_0)\). Replace \(h\) by \(h(x)-|x|^2\); this keeps its differential at zero and makes its maximum strict on the nearby support.

Here is the needed analytic coordinate construction. After permuting coordinates let \(a=\partial_{x_n}h(0)\ne0\). The convergent real power series extends holomorphically to a complex polydisk. Reduce it so that \(|\partial_{x_n}h-a|\le |a|/2\). Solving \(h(x',s)=t\) is the fixed-point equation
\[
 s=\frac{t-h(x',0)}a
       -\frac{h(x',s)-h(x',0)-as}{a}.
 \tag{SN27}
\]
On a fixed small closed complex \(s\)-disk the right side has Lipschitz constant at most \(1/2\), by integration of its derivative on line segments. For sufficiently small complex \((x',t)\), its value at zero has modulus at most half the disk radius, so it maps that disk into itself. Starting at zero, the iterates are holomorphic in the parameters and their successive differences are bounded by a geometric series, uniformly on a smaller parameter polydisk. They converge to the unique fixed point. The limit is holomorphic: the iterated Cauchy integral formula passes to the uniform limit and gives its convergent local power series. Real parameters give real iterates and hence a real limit. Thus \(x\mapsto(x',h(x))\) and the constructed inverse are real analytic on neighborhoods of zero.

Use these coordinates \(y=(y',t)\). The analytic coordinate wavefront rule, applied to this map and its inverse, preserves the asserted inclusion of the differential. It suffices to show that the transformed distribution, denoted \(v\), has both signed vertical covectors at zero. Its support satisfies
\[
 t\le0,\qquad
 \operatorname{supp}v\cap\{t=0\}=\{0\}
 \quad\hbox{locally}.
 \tag{SN17}
\]
Choose a small bounded open ball \(Y\) in the \(y'\)-space, with its closure in the coordinate neighborhood. Since the compact side \(\partial Y\times\{0\}\) misses the support, after shrinking an interval \(I\) about zero its entire side \(\partial Y\times I\) misses the support. We can arrange this with a surrounding collar, so projection of the support in \(Y\times I\) to \(I\) is proper: over every compact subinterval, the support stays inside a compact subset of \(Y\). In dimension one the fiber is the singleton \(\mathbb R^0\), and this statement is automatic.

Assume for a contradiction that \((0,dt)\notin\operatorname{WF}_A(v)\). Closedness of analytic wavefront gives a neighborhood of zero free of that vertical direction. By (SN17) and compactness of \(\overline Y\), after reducing \(I\) all support points in \(Y\times I\) lie in this neighborhood. To verify that reduction, any contrary sequence has \(t_j\to0\) and a convergent subsequence of its \(y'_j\); its limit is a support point at \(t=0\), hence zero. Points outside the support have no wavefront in any direction. Consequently there is no positive vertical wavefront covector anywhere in \(Y\times I\).

For each real \(\eta\in\mathbb R^{n-1}\), multiply \(v\) by the entire analytic function \(e^{-i\eta\cdot y'}\) and project:
\[
 v_\eta(t)=\pi_*\bigl(e^{-i\eta\cdot y'}v\bigr),
 \qquad \pi(y',t)=t.
 \tag{SN18}
\]
Analytic multiplication cannot introduce analytic wavefront directions. The proper-projection theorem uses exactly covectors with zero fiber component. It therefore yields
\[
 (t,+1)\notin\operatorname{WF}_A(v_\eta)
 \quad(t\in I).
 \tag{SN19}
\]
Every \(v_\eta\) vanishes for positive \(t\). Corollary 2.2 gives \(v_\eta=0\) on this same interval \(I\) for every \(\eta\). No uniform analytic estimate as \(|\eta|\to\infty\) is being claimed or needed.

These equalities force \(v=0\) in \(Y\times I\). Here is the full separation step. Given \(\psi\in C_c^\infty(Y\times I)\), Fourier inversion in its fiber variables gives
\[
 \psi(y',t)=(2\pi)^{1-n}
       \int_{\mathbb R^{n-1}} e^{iy'\cdot\eta}
                   \widehat\psi(\eta,t)\,d\eta .
 \tag{SN20}
\]
The fiber transform and each of its fixed \(t\)-derivatives decrease faster than every power of \(|\eta|\), by repeated integration by parts. Their \(t\)-supports stay in one compact subinterval of \(I\). Properness supplies one compact fiber cutoff equal to one near the support of \(v\) over that subinterval. Insert it in (SN20) before pairing with \(v\). Differentiating the integrand through the finite distributional order costs only a fixed polynomial in \(\eta\), so the integral converges in that compact test seminorm. Each paired integrand is \(v_{-\eta}(\widehat\psi(\eta,\cdot))=0\). Thus \(v(\psi)=0\). For a zero-dimensional fiber (SN20) is just the original test itself.

This contradicts \(0\in\operatorname{supp}v\), and proves \((0,dt)\in\operatorname{WF}_A(v)\). Applying the same conclusion to \(\overline v\), which has the same support, and using (SN14), proves the negative normal as well. Pulling the two covectors back gives (SN16). \(\square\)

## 4. Smooth supporting functions and nearest points

**Corollary 4.1.** The conclusion (SN16) remains valid if \(h\) in (SN15) is merely \(C^1\).

**Proof.** Work in a small closed ball inside \(X\), write \(F=\operatorname{supp}u\) there, and put \(p=dh(x_0)\ne0\). For large positive integers \(j\), set \(q_j=x_0+p/j\), and choose a point \(z_j\in F\) nearest to \(q_j\). A nearest point exists by compactness. The comparison point \(x_0\) gives
\[
 |z_j-q_j|\le |p|/j,\qquad
 |z_j-x_0|\le2|p|/j.
 \tag{SN21}
\]
Thus the minimizers lie in the interior of the chosen ball for large \(j\), so they are local nearest support points in the original open set. Since
\(h(q_j)=h(x_0)+|p|^2/j+o(1/j)>h(x_0)\),
the point \(q_j\) is outside \(F\) for large \(j\). In particular \(z_j\ne q_j\).

Set \(w_j=z_j-x_0\). Squaring the first comparison in (SN21) gives
\[
 j|w_j|^2\le2p\cdot w_j.
 \tag{SN22}
\]
The supporting inequality and differentiability give
\[
 p\cdot w_j\le o(|w_j|).
 \tag{SN23}
\]
If \(w_j\ne0\), division of (SN22) by \(|w_j|\), followed by (SN23), shows \(j|w_j|\to0\). It is also true along indices with \(w_j=0\). Therefore
\[
 z_j\to x_0,\qquad j(q_j-z_j)=p-jw_j\longrightarrow p.
 \tag{SN24}
\]
The analytic function \(g_j(x)=-|x-q_j|^2\) has a local maximum over the support at \(z_j\), with nonzero differential \(2(q_j-z_j)\). Theorem 3.1 and positive conicity put
\((z_j,\pm j(q_j-z_j))\) in \(\operatorname{WF}_A(u)\).
This wavefront set is closed in the nonzero cotangent bundle. The limit covectors \(\pm p\) are nonzero, so (SN24) proves the assertion. \(\square\)

**Corollary 4.2 (a ball touching the support).** If \(q\notin\operatorname{supp}u\) has a nearest support point \(z\) lying in \(X\), with the nearest-point comparison valid on a neighborhood, then
\[
 (z,\pm(q-z))\in\operatorname{WF}_A(u).
 \tag{SN25}
\]
Indeed \(g(x)=-|x-q|^2\) has its supporting maximum at \(z\), and \(dg(z)=2(q-z)\ne0\). Positive conicity removes the factor two. Local compact minimization is enough; no global minimum on an unbounded set is needed.

Let \(\mathcal N(F)\) consist of both signs of all nonzero differentials of local \(C^1\) supporting functions for \(F\). Then
\[
 \overline{\mathcal N(\operatorname{supp}u)}
       \subset\operatorname{WF}_A(u),
 \tag{SN26}
\]
where the closure is relative to the nonzero cotangent bundle. This follows from Corollary 4.1 and closedness, not from a smooth-wavefront support theorem.

## References

The supporting-normal inclusion is a classical analytic uniqueness theorem. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Theorem 8.5.6 and its normal-set formulation, give the named general context. The proof above supplies the one-frequency-ray uniqueness argument explicitly through Cauchy continuation, uses the exact available analytic coordinate and proper-projection proofs, and includes the \(C^1\) nearest-point limit. Distributional Cauchy boundaries are credited to the classical Sokhotski–Plemelj formula; the linked programme lesson proves the normalization and finite-test convergence used here.

[P]: ../../AN02-L188.html#complete-proof
[A]: ../../AN02-L186.html#complete-proof
[C]: ../../AN02-L045.html
[K]: ../../prerequisites/cauchy-kernels-and-boundary-limits.html#a-real-pole-remembers-the-side-of-approach
[F]: ../../prerequisites/schwartz-fourier-foundations.html
