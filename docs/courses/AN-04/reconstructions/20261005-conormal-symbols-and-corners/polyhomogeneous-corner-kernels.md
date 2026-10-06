# Polyhomogeneous corner kernels and the full converse

This component retains AN03-U032, *Totally characteristic operators on the half space*, Proposition 6.8 and all four supporting Lemmas 6.9–6.12. Original author: Claude Opus 5.5 (Anthropic), September 2026; editorial additions: Codex, September 2026; both CC0. Current proof connections and clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, CC0. Every original mathematical display remains unchanged.

The [local resolved-kernel component](../20261005-local-boundary-calculus/resolved-corner-kernels.md) contains Proposition 6.1, Theorem 6.2 and all uniform bounds (6.1)–(6.10). Write \(z=(x',y')\), \(w=(x_n,y_n)\), \(Q=\{x_n\ge0,y_n\ge0\}\), \(t=(x_n+y_n)/2\), \(r=(x_n-y_n)/t\) on its positive corner, and \(\partial_2Q=\{w=0\}\). Formula \(\Phi(t,r)=(t(1+r/2),t(1-r/2))\) extends as a smooth algebraic map for all real \(r\). The zero-dimensional tangential case has the single-point measure one.

The [complete conormal characterization](../20261005-conormal-test-foundations/conormal-amplitudes-and-test-spaces.md) supplies the normal amplitude theorem, all tangent regularity estimates and the exact normalization. The [intrinsic symbol companion](intrinsic-conormal-symbols.md) gives its coordinate law and classical step-one preservation. The [Fourier](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md), [measure](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) and [finite-order distribution](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md) proofs supply the analytic prerequisites. The approved mathematical antecedent is Hörmander III, 2007 eBook, Section 18.3.

## Distributional detail: no hidden term at the corner

We record the exact fact needed to identify an inverse transform with its locally integrable expression. A distribution \(T\) on \(\mathbb R^2\) supported at zero is a finite sum of derivatives of \(\delta_0\). Indeed fix a compact neighborhood and a finite test order \(L\). If a smooth test \(\varphi\) has all derivatives through \(L\) zero at zero, Taylor's remainder gives
\(\partial^\beta\varphi(w)=o(|w|^{L-|\beta|})\) for \(|\beta|\le L\).
Multiply by \(\chi(w/\epsilon)\), with \(\chi=1\) near zero. Support gives \(T\varphi=T(\chi_\epsilon\varphi)\), while the product rule makes every derivative through \(L\) of that product \(o(1)\). The finite-order bound gives \(T\varphi=0\). Subtracting a fixed compactly cut-off Taylor polynomial of an arbitrary test proves
\[
 T\varphi=\sum_{|\alpha|\le L}c_\alpha\,\partial^\alpha\varphi(0).
 \tag{SC1}
\]
Thus its Fourier transform is a polynomial. The same argument with smooth parameters gives smooth coefficients: each is the pairing with one fixed cutoff monomial.

If \(g\in L^1(\mathbb R^2)\), its Fourier transform tends to zero at infinity. Here is the needed proof: the complete compact-smooth density theorem gives \(g_j\in C_c^\infty\) with \(\|g_j-g\|_1\to0\); the Fourier difference is uniformly bounded by this norm. Every \(\widehat g_j\) tends to zero by integration by parts. First choose \(j\), then choose the frequency radius, proving the assertion. Consequently if a tempered distribution agrees off zero with a globally integrable function, and both their Fourier transforms tend to zero at infinity, their difference is zero. Its Fourier transform is a polynomial by (SC1), and a polynomial tending to zero is identically zero: restriction to every ray kills its top homogeneous part, and descending through its degrees kills them all. Fourier inversion finishes the identification.

## Residual kernels are polyhomogeneous conormal distributions

Smoothness of the resolved kernel \(F\) has an invariant meaning: it says precisely that \(K\) is a polyhomogeneous conormal distribution of order \(-n/2\) with respect to \(\partial_2Q\). We prove this now.

**The class.** Conormal distributions \(I^\mu(X,Y)\) are defined by tangential regularity. A compactly supported \(u\in I^\mu\) has, in coordinates, the normal form \(u=\int e^{i\langle t,\tau\rangle}b(z,\tau)\,d\tau\) with \(b\in S^{\mu+(N-2k)/4}\), where \(N=\dim X\), \(k\) is the codimension, and \(b\) is \((2\pi)^{-k}\) times the Fourier transform of \(u\) in the normal variables; conversely every such \(u\) is conormal. (These are the complete conormal-characterization proofs linked above.) The polyhomogeneous class \(I^\mu_{\mathrm{phg}}\) requires in addition that these amplitudes be polyhomogeneous with step one. Step one is needed here, because a term of degree \(-\tfrac32\) in \(\tau\) would put a factor \(t^{1/2}\) into \(F\). For \(X=\mathbb R^{2n}\), \(Y=\partial_2Q\) we have \(N=2n\), \(k=2\), normal variables \(w=(x_n,y_n)\), tangential variables \(z=(x',y')\), and \(\mu=-n/2\) gives amplitude degree \(-1\). So \(K\in I^{-n/2}_{\mathrm{phg}}(\mathbb R^{2n},\partial_2Q)\) means: \(K\) is smooth off \(\partial_2Q\), and for all \(\phi\in C_0^\infty(\mathbb R^{2n-2}_z)\), \(\psi\in C_0^\infty(\mathbb R^2_w)\),
\[
(2\pi)^{-2}\widehat{\phi\psi K}(z,\tau)\sim\sum_{j\geq0}b_j(z,\tau),\qquad b_j\ \text{homogeneous of degree }-1-j\text{ in }\tau\text{ for }|\tau|\geq1,
\tag{6.11}
\]
in the sense that every finite truncation has the next stated symbol order; the Fourier transform is taken in \(w\).

**Proposition 6.8** (Residual kernels are conormal). Let \(K\in L^1_{\mathrm{loc}}(\mathbb R^{2n})\) with \(\operatorname{supp}K\subset Q\), and let \(F(z,t,r)=tK(x',t(1+r/2),y',t(1-r/2))\) for \(t>0\). Then \(K\in I^{-n/2}_{\mathrm{phg}}(\mathbb R^{2n},\partial_2Q)\) if and only if \(F\) agrees almost everywhere with a function in \(C^\infty(\{t\geq0\}\times\mathbb R_r\times\mathbb R^{2n-2}_z)\); such a function vanishes for \(|r|\geq2\). In particular \(K_a\in I^{-n/2}_{\mathrm{phg}}(\mathbb R^{2n},\partial_2Q)\) for every \(a\in S^{-\infty}_{\mathrm{la}}\).

The global decay (6.5) is not a conormal property. So Theorem 6.2 and Proposition 6.8 together say: residual kernels are exactly the kernels supported in \(Q\), polyhomogeneous conormal of order \(-n/2\) at \(\partial_2Q\), with the uniform decay (6.5).

We need four lemmas. In them \(z\) ranges over \(\mathbb R^{m}\), all functions have compact \(z\)-support, and every estimate holds with \(z\)-derivatives, uniformly in \(z\).

**Lemma 6.9** (Homogeneous pieces). Let \(h\in C^\infty(\mathbb R^m\times\mathbb R_r)\) vanish for \(|r|\geq2\), let \(d>-2\), and let \(k(z,w)=t^dh(z,r)\) on \(Q\setminus\{0\}\), \(k=0\) off \(Q\). Then \(k\) is smooth off \(w=0\), homogeneous of degree \(d\) in \(w\), and locally integrable. If \(\psi\in C_0^\infty(\mathbb R^2)\) equals 1 near 0, then \(\widehat{\psi k}=g+e\), where \(g\) is smooth on \(\mathbb R^m\times(\mathbb R^2\setminus0)\) and homogeneous of degree \(-2-d\) in \(\tau\), and \(e\) is smooth with all derivatives \(O(|\tau|^{-N})\) for \(|\tau|\geq1\). In particular \(\widehat{\psi k}\in S^{-2-d}\).

**Proof.** \(h\) vanishes to infinite order at \(r=\pm2\), so \(k\) is smooth across the faces of \(Q\); it is smooth elsewhere off \(w=0\) by Proposition 6.1. Also \(|k|\leq C|w|^d\), so \(k\) is locally integrable and tempered, and its Fourier transform \(\widehat k\) is homogeneous of degree \(-2-d\) (compare \(k(\lambda\cdot)=\lambda^dk\) with \(\widehat{k(\lambda\cdot)}=\lambda^{-2}\widehat k(\cdot/\lambda)\)). Write \(\widehat k=\widehat{\psi k}+\widehat f\), \(f=(1-\psi)k\). The first term is smooth. The function \(f\) is smooth, with \(|\partial^\beta_wf|\leq C_\beta|w|^{d-|\beta|}\) for \(|w|\geq1\). If \(|\beta|>d+2+|\gamma|\), then \(D^\beta_w(w^\gamma f)\) is integrable, so \(\tau^\beta\partial_\tau^\gamma\widehat f\) is a bounded continuous function. Hence \(\widehat f\) is smooth on \(\tau\neq0\) and all its derivatives are \(O(|\tau|^{-N})\) for \(|\tau|\geq1\). So \(g=\widehat k|_{\tau\neq0}\) is smooth and homogeneous, and \(e=-\widehat f\) on \(\tau\neq0\) (with \(\widehat{\psi k}=g+e\) there). The symbol estimates follow from homogeneity on \(|\tau|\geq1\) and smoothness on \(|\tau|\leq1\). \(\square\)

**Lemma 6.10** (Remainders). Let \(R\in C^\infty(\{t\geq0\}\times\mathbb R_r\times\mathbb R^m)\) vanish for \(|r|\geq2\), let \(J\geq1\), and let \(E=t^{J-1}R(z,t,r)\) on \(Q\setminus0\), \(E=0\) off \(Q\). Then \(\widehat{\psi E}\in S^{-J-1}(\mathbb R^m\times\mathbb R^2)\).

**Proof.** By Proposition 6.1(5), each \(w\)-derivative of \(t\) or \(r\) costs at most \(C|w|^{-1}\), and \(t\) is comparable to \(|w|\) on \(Q\). So \(f=\psi E\) satisfies \(|\partial_w^\beta f|\leq C_\beta|w|^{J-1-|\beta|}\), and \(g_\gamma=w^\gamma f\) satisfies \(|\partial^\beta g_\gamma|\leq C|w|^{\nu-|\beta|}\) with \(\nu=J-1+|\gamma|\geq0\). Fix \(|\tau|\geq1\) and \(\chi_0\in C_0^\infty(\{|w|<2\})\) equal to 1 on \(|w|\leq1\). The Fourier transform of \(\chi_0(|\tau|w)g_\gamma\) is at most \(\int_{|w|\leq2/|\tau|}C|w|^\nu dw\leq C'|\tau|^{-\nu-2}\). For the rest, \(e^{-iw\cdot\tau}=(i|\tau|^{-2}\tau\cdot\nabla_w)e^{-iw\cdot\tau}\); integrating by parts \(L>\nu+2\) times, and noting that derivatives of \(\chi_0(|\tau|w)\) are \(O(|w|^{-k})\) where they do not vanish, gives the bound \(C|\tau|^{-L}\int_{1/|\tau|\leq|w|\leq R}|w|^{\nu-L}dw\leq C'|\tau|^{-\nu-2}\). Since \(\partial_\tau^\gamma\widehat f=\widehat{(-iw)^\gamma f}\), we get \(|\partial^\gamma_\tau\widehat f(\tau)|\leq C|\tau|^{-J-1-|\gamma|}\). \(\square\)

**Lemma 6.11** (Inverse transforms of homogeneous terms). Let \(j\geq0\), let \(b^{\mathrm{hom}}\) be smooth on \(\mathbb R^m\times(\mathbb R^2\setminus0)\) and homogeneous of degree \(-1-j\) in \(\tau\), let \(\chi\in C_0^\infty(\mathbb R^2)\) equal 1 near 0, and put \(b=(1-\chi)b^{\mathrm{hom}}\) and \(k(z,w)=\int e^{i\langle w,\tau\rangle}b(z,\tau)\,d\tau\). Then \(k\) is smooth off \(w=0\), rapidly decreasing with all derivatives as \(|w|\to\infty\), locally integrable, and on \(0<|w|<1\)
\[
k=h-P\log|w|+s,
\tag{6.12}
\]
where \(h\) is smooth off \(w=0\) and homogeneous of degree \(j-1\), \(P\) is a homogeneous polynomial of degree \(j-1\) in \(w\) with coefficients smooth in \(z\) (\(P=0\) when \(j=0\)), and \(s\) is smooth on \(\{|w|<1\}\).

**Proof.** \(b\in S^{-1-j}\). For \(|\gamma|\) large, \(w^\gamma\partial^\beta_wk\) is the absolutely convergent integral of \(e^{i\langle w,\tau\rangle}\) against a constant times \(D^\gamma_\tau(\tau^\beta b)\); this gives smoothness off 0 and rapid decay. Put \(\theta=(\tau\cdot\partial_\tau+1+j)b=-(\tau\cdot\partial_\tau\chi)\,b^{\mathrm{hom}}\), which is smooth with compact support in \(\mathbb R^2\setminus0\) (Euler's relation kills \(b^{\mathrm{hom}}\)), and \(\Theta=\int e^{i\langle w,\tau\rangle}\theta\,d\tau\in\mathcal S(\mathbb R^2)\). Since \(\int e^{i\langle w,\tau\rangle}\tau\cdot\partial_\tau f\,d\tau=-(2+w\cdot\partial_w)\int e^{i\langle w,\tau\rangle}f\,d\tau\) for tempered \(f\),
\[
\big(w\cdot\partial_w-(j-1)\big)k=-\Theta .
\tag{6.13}
\]
On a ray \(w=\sigma\omega\), \(|\omega|=1\), this says \(\frac d{d\sigma}[\sigma^{1-j}k(\sigma\omega)]=-\sigma^{-j}\Theta(\sigma\omega)\). Since \(\sigma^{1-j}k(\sigma\omega)\to0\) as \(\sigma\to\infty\), \(k(\sigma\omega)=\sigma^{j-1}\int_\sigma^\infty s^{-j}\Theta(s\omega)\,ds\). For \(j=0\), the degree-minus-one Taylor polynomial below is the empty polynomial, and the sole remainder is \(r_0=\Theta\). Write \(\Theta=T+\sum_{|\alpha|=j}w^\alpha r_\alpha\), where \(T\) is the Taylor polynomial of \(\Theta\) of degree \(j-1\) at 0 and the \(r_\alpha\) are smooth. For \(\sigma<1\) split \(\int_\sigma^\infty=\int_1^\infty+\int_\sigma^1\):

* \(\sigma^{j-1}\int_1^\infty s^{-j}\Theta(s\omega)ds\) is homogeneous of degree \(j-1\) and smooth off 0.
* For the degree-\(\ell\) part \(T_\ell\) of \(T\), \(\ell<j-1\): \(\sigma^{j-1}\int_\sigma^1s^{\ell-j}T_\ell(\omega)ds=(T_\ell(w)-\sigma^{j-1}T_\ell(\omega))/(j-1-\ell)\), a polynomial minus a homogeneous function of degree \(j-1\). For \(\ell=j-1\): \(\sigma^{j-1}T_{j-1}(\omega)\int_\sigma^1s^{-1}ds=-T_{j-1}(w)\log|w|\). So \(P=T_{j-1}\).
* \(\sigma^{j-1}\int_\sigma^1s^{-j}\sum_\alpha(s\omega)^\alpha r_\alpha(s\omega)ds=\sum_\alpha\sigma^{j-1}\omega^\alpha\big(\int_0^1-\int_0^\sigma\big)r_\alpha(s\omega)ds\). The first part is homogeneous of degree \(j-1\). In the second, \(\sigma^{j-1}\omega^\alpha=\sigma^{-1}w^\alpha\) and \(\sigma^{-1}\int_0^\sigma r_\alpha(s\omega)ds=\int_0^1r_\alpha(uw)du\), which is smooth in \(w\).

Collecting terms gives (6.12) off zero. Its expression is locally
integrable because \(j-1>-2\), including the logarithmic term.
Together with the proved rapid decrease at infinity this gives an
\(L^1\) function \(k_{\rm loc}\) agreeing with the inverse-transform
distribution off zero. That distribution has Fourier transform
\((2\pi)^2b\), which tends to zero since \(b\in S^{-1-j}\).
The Fourier transform of \(k_{\rm loc}\) also tends to zero by the
preceding \(L^1\) proof. The no-hidden-term result (SC1) therefore
identifies the two distributions. Thus (6.12) gives the actual
locally integrable inverse transform, including at the corner.
This holds after every \(z\)-derivative as well, with the same
compact-parameter estimates. \(\square\)

**Lemma 6.12** (Uniqueness of expansions). If \(\sum_{i=-1}^L(\alpha_i+\beta_i\log\lambda)\lambda^i=o(\lambda^L)\) as \(\lambda\to0+\), then all \(\alpha_i\) and \(\beta_i\) vanish.

**Proof.** Multiply by \(\lambda\): \(\alpha_{-1}+\beta_{-1}\log\lambda\) tends to a finite limit (namely 0), so \(\beta_{-1}=0\) and then \(\alpha_{-1}=0\). Repeat with the next power. \(\square\)

**Proof of Proposition 6.8.** (\(\Leftarrow\)) Off \(\partial_2Q\), \(K=F/t\) is smooth in the interior of \(Q\), smooth across its faces because \(F\) is flat at \(r=\pm2\), and zero outside \(Q\). Near \(\partial_2Q\), first fix cutoffs
\(\phi(z)\), \(\psi(w)\) with \(\psi=1\) near zero. This suffices
for the stated arbitrary-cutoff definition: multiply \(F\) by any
additional smooth \(\psi_1(\Phi(t,r))\), which preserves smoothness
and side flatness, and apply the same argument. Cutoff pieces away
from zero are smooth with compact normal support and have rapidly
decreasing normal Fourier transform. Taylor's formula in \(t\) gives \(F=\sum_{j<J}t^jF_j(z,r)+t^JR_J(z,t,r)\), with \(F_j\) and \(R_J\) smooth and vanishing for \(|r|\geq2\). Hence \(\phi\psi K=\sum_{j<J}\phi\psi\,t^{j-1}F_j+\phi\psi\,t^{J-1}R_J\). By Lemma 6.9, \((2\pi)^{-2}\widehat{\phi\psi t^{j-1}F_j}\) equals a function homogeneous of degree \(-1-j\) for \(|\tau|\geq1\), up to \(S^{-\infty}\); by Lemma 6.10 the last term has transform in \(S^{-J-1}\). As \(J\) is arbitrary, (6.11) holds.

(\(\Rightarrow\)) Off \(\partial_2Q\), \(K\) is smooth, so \(F\) is smooth on \(t>0\), and \(F=0\) for \(|r|>2\) because \(\operatorname{supp}K\subset Q\). Fix \(z_0\) and choose \(\phi=1\) near \(z_0\) and \(\psi=1\) on \(|w|\leq2\delta\). Take \(J\ge4\), eventually as large as required. Let \(b=(2\pi)^{-2}\widehat{\phi\psi K}\sim\sum b_j\), with \(b_j=(1-\chi)b_j^{\mathrm{hom}}\). Let \(k_j\) be the inverse transforms of Lemma 6.11 and \(\rho_J=\int e^{i\langle w,\tau\rangle}(b-\sum_{j<J}b_j)d\tau\). Since \(b-\sum_{j<J}b_j\in S^{-1-J}\) in two variables, \(\rho_J\in C^{J-2}\). So for \(z\) near \(z_0\) and \(0<|w|<\delta\),
\[
K=\sum_{j<J}\big(h_j-P_j\log|w|\big)+S_J,\qquad S_J=\rho_J+\sum_{j<J}s_j\in C^{J-2}.
\]
Let \(U=\mathbb R^2\setminus Q\), an open cone on which \(K=0\). For \(w\in U\), \(|w|<\delta\), and \(0<\lambda\leq1\) we have \(K(z,\lambda w)=0\). Insert homogeneity, \(\log|\lambda w|=\log\lambda+\log|w|\), and Taylor's formula \(S_J(\lambda w)=\sum_{i\leq J-3}\lambda^iS_{J,i}(w)+o(\lambda^{J-3})\) with homogeneous polynomials \(S_{J,i}\) of degree \(i\). The term \(j=J-1\) is \(O(\lambda^{J-2}|\log\lambda|)=o(\lambda^{J-3})\). Lemma 6.12 gives, for \(j\leq J-2\): \(P_j=0\) on \(U\), hence \(P_j\equiv0\); and \(h_j=-S_{J,j-1}\) on \(U\) (with \(S_{J,-1}=0\)). Thus \(\tilde h_j=h_j+S_{J,j-1}\) is homogeneous of degree \(j-1\), smooth off 0, and supported in \(Q\), and
\[
K=\sum_{j\leq J-2}\tilde h_j+R_J,\qquad R_J=\Big(S_J-\sum_{i\leq J-3}S_{J,i}\Big)+\big(h_{J-1}-P_{J-1}\log|w|\big).
\]
All derivatives of \(R_J\) of order \(\leq J-3\) are continuous and tend to 0 at \(w=0\), so \(R_J\in C^{J-3}\). Now \(t\tilde h_j(\Phi(t,r))=t^j\tilde F_j(z,r)\) with \(\tilde F_j(z,r)=\tilde h_j(z,1+r/2,1-r/2)\), which is smooth and vanishes for \(|r|\geq2\). Hence, for small \(t\) and \(|r|\leq3\), \(F=\sum_{j\leq J-2}t^j\tilde F_j+t\,R_J\circ\Phi\) is \(C^{J-3}\), and \(F=0\) for \(|r|\geq2\). All statements include arbitrary \(z\)-derivatives:
the normal integral for the remainder is absolutely convergent
after each such derivative at the same order, and its first
\(J-2\) normal derivatives are integrable since their frequency
degree is at most \(-3\) in dimension two. The homogeneous-log
term of degree \(J-2\), after at most \(J-3\) normal derivatives,
is \(O(|w|(1+|\log|w||))\), and so extends with zero jets.
Consequently \(tR_J\circ\Phi\) is \(C^{J-3}\) jointly for
bounded \(r\), including both faces. The extensions obtained for
different \(J\) agree on the dense set \(t>0\) and hence have
the same continuous jets at zero. Since \(J\) is arbitrary,
\(F\) is smooth. The last assertion of the proposition follows from Theorem 6.2(c). \(\square\)

