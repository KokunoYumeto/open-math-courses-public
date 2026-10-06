# The critical two-dimensional multiplication obstruction

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="critical-multiplication"></a>
## Critical multiplication

There are a real nonnegative $a\in L^2(\mathbb R^2)$ and a real $w\in H^1(\mathbb R^2)$, both compactly supported, for which $aw\notin L^2(\mathbb R^2)$. The equivalence between its weak-derivative condition and the Fourier definition of \(H^1\) is proved in [the integer Sobolev reading, formula (A9)](euclidean-approximation-and-convolution.md#integer-sobolev-density). This is the precise obstruction used in the critical coefficient case; it does not deny multiplication estimates with a strictly larger finite coefficient exponent.

Choose a smooth radial cutoff $\chi$ equal to one for $0\leq r\leq e^{-2}$ and zero for $r\geq e^{-1}$. For $0<r=|x|<e^{-1}$ put $t=\log(1/r)$ and
\[
 a(x)=\frac{\chi(r)}{r\,t^{3/4}},\qquad
 w(x)=\chi(r)t^{1/3}.
\]
Set both functions equal to zero outside the support and assign arbitrary values at $x=0$, a set of measure zero. Away from zero and the inner disk their values and derivatives are bounded. Polar integration on the inner disk, with $dr/r=-dt$, gives
\[
 \int_{|x|<e^{-2}}|a|^2\,dx
 =2\pi\int_2^\infty t^{-3/2}\,dt<\infty,
 \qquad
 \int_{|x|<e^{-2}}|w|^2\,dx
 =2\pi\int_2^\infty e^{-2t}t^{2/3}\,dt<\infty.
\]
On that disk the classical radial derivative is $w'(r)=-\frac13r^{-1}t^{-2/3}$. Consequently
\[
 \int_{|x|<e^{-2}}|\nabla w|^2\,dx
 =\frac{2\pi}{9}\int_2^\infty t^{-4/3}\,dt<\infty.
\]
These classical derivatives are also the distributional derivatives across the puncture. Take a smooth radial function \(\eta_\varepsilon\) that is zero on \(r\le\varepsilon\), one on \(r\ge2\varepsilon\), and satisfies \(|\nabla\eta_\varepsilon|\le C/\varepsilon\). Such cutoffs follow from [the explicit smooth cutoff construction](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs). The function \(\eta_\varepsilon w\) is smooth and compactly supported. Coordinatewise integration by parts therefore gives, for every compact smooth test \(\varphi\),
\[
 \int \eta_\varepsilon w\,\partial_j\varphi
 =-\int \eta_\varepsilon(\partial_jw)\varphi
   -\int w(\partial_j\eta_\varepsilon)\varphi.
\]
The last term has absolute value at most
\(C\varepsilon(\log(1/\varepsilon))^{1/3}\|\varphi\|_\infty\): its support is the annulus \(\varepsilon<r<2\varepsilon\), whose area is \(3\pi\varepsilon^2\). This bound tends to zero; writing \(\varepsilon=e^{-t}\), the exponential series bounds \(e^{-t}t^{1/3}\) by a constant times \(t^{-5/3}\). The other two integrals converge by the already proved \(L^2\) bounds and Cauchy–Schwarz on the fixed test support. Their limits prove the weak derivative identity. Thus \(w\in H^1\), including the smooth cutoff terms.

Their product on the inner disk satisfies
\[
 \int_{|x|<e^{-2}}|aw|^2\,dx
 =2\pi\int_2^\infty t^{-5/6}\,dt=\infty.
\]
This proves the claim in full. For a ball \(B(x_0,R)\), take \(0<\lambda<eR\) and use \(a_\lambda(x)=a((x-x_0)/\lambda)\), \(w_\lambda(x)=w((x-x_0)/\lambda)\). Their support lies inside that ball; their squared \(L^2\) norms acquire the factor \(\lambda^2\), the squared gradient norm of \(w_\lambda\) is unchanged, and the product integral remains infinite. The only inputs are the polar-coordinate integration formula, elementary improper integrals, smooth cutoffs and the definition of the weak $H^1$ derivative.
