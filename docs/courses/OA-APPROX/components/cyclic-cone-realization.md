# Normal positive functionals in a cyclic natural cone

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original text: public domain (CC0).*

Let \(M\subset B(H)\) have a cyclic separating vector \(\Omega\) in its natural cone \(P\). Every normal positive functional on \(M\) has a unique representing vector in \(P\). The target functional may have a proper support. The Hilbert space need not be separable. We give the positive Fourier averaging, the support-corner domain check, the quantitative correction, and the final norm-density argument.

Inner products are linear in the second variable. Write \(\omega_u(a)=\langle u,au\rangle\), and write \(u\le v\) in the cone when \(v-u\in P\). We use the support, corner, and norm arguments CG01–CG09a, the concrete Hilbert/predual constructions H00–H03, and the real Hahn–Banach proof F01. The scalar exponential and continuous integral proofs are the elementary calculus component, Section 5 and R03–R07. The modular construction used here is NC00, NC04, NC08; its precise output is recorded next.

<a id="cr00"></a>
## CR00. The modular input, with its domains

For every cyclic separating \(\gamma\in P\), including one on a simultaneous support corner, let
\[
 S_\gamma=\overline{a\gamma\mapsto a^*\gamma},\qquad
 F_\gamma=\overline{b'\gamma\mapsto b'^*\gamma}=S_\gamma^*.
\]
NC08 supplies these actual graph cores and
\[
 S_\gamma=J_\gamma\Delta_\gamma^{1/2},\qquad
 F_\gamma=J_\gamma\Delta_\gamma^{-1/2},\qquad
 J_\gamma\Delta_\gamma^zJ_\gamma=\Delta_\gamma^{-\overline z},
 \quad \Delta_\gamma\gamma=\gamma.
 \tag{1}
\]
CG09 identifies \(J_\gamma\) with the given conjugation and \(P_\gamma\) with the given cone. In particular
\[
\begin{gathered}
 a\gamma\in D(\Delta_\gamma^{1/2}),\quad
 \Delta_\gamma^{1/2}a\gamma=Ja^*\gamma,\\
 b'\gamma\in D(\Delta_\gamma^{-1/2}),\quad
 \Delta_\gamma^{-1/2}b'\gamma=Jb'^*\gamma,\\
 P=\overline{\Delta_\gamma^{1/4}M_+\gamma}
   =\overline{\Delta_\gamma^{-1/4}M'_+\gamma},\qquad
 \Delta_\gamma^{it}P=P.
 \tag{2}
\end{gathered}
\]
For a corner these formulas are read on that corner Hilbert space and with its algebra and commutant. A quarter-power expression in (2) is an actual domain value: the preceding half-power membership implies it by the spectral inequality \(t^{1/2}\le1+t\). The operator \(\Delta_\gamma\) is injective, although its spectrum can accumulate at zero and infinity. Its real powers have the spectral domains
\[
 D(\Delta_\gamma^\alpha)
 =\{u:\int_{(0,\infty)}\lambda^{2\alpha}
                 \,d\langle u,E_\gamma(\lambda)u\rangle<\infty\}.
 \tag{3}
\]
The bounded calculus, logarithm, spectral bands, and strong continuity of \(\Delta_\gamma^{it}\) are the concrete NC00 spectral output. Equations (1)–(3) are the only modular analytic input to the construction below. No positive-functional realization theorem is included in that input.

<a id="cr01"></a>
## CR01. A positive Fourier kernel of mass one

With the Fourier convention \(\widehat k(s)=\int_{\mathbb R}e^{its}k(t)\,dt\), we claim
\[
 k(t)=\frac{2}{\cosh(2\pi t)}\ge0,\qquad
 \int_{\mathbb R}k(t)\,dt=1,\qquad
 \widehat k(s)=\frac1{\cosh(s/4)}.
 \tag{4}
\]
To fix the scalar constant without importing trigonometric identities, put \(A=\int_0^1(1+t^2)^{-1}\,dt\) and \(\pi=4A\). Define \(\alpha(t)=\int_0^t(1+s^2)^{-1}\,ds\) for \(t\ge0\). The scalar exponential constructed in the elementary calculus component satisfies
\[
 e^{i\alpha(t)}=\frac{1+it}{\sqrt{1+t^2}}.
\]
Indeed the derivative of the right side is \(i/(1+t^2)\) times that side; multiplication by \(e^{-i\alpha(t)}\) gives derivative zero and value one at zero. For \(t>0\), differentiation shows \(\alpha(t)+\alpha(1/t)=2A\), with the constant obtained at \(t=1\). Hence \(\alpha(t)\uparrow2A\) as \(t\to\infty\), and continuity of the exponential gives \(e^{i2A}=i\), \(e^{i\pi}=-1\). The right-side formula covers the first quadrant as \(\alpha\) increases continuously from zero to \(2A\); multiplication by \(i\) covers the second quadrant. Thus \(\operatorname{Re}e^{iy}\) has exactly one zero on \([0,\pi]\), at \(y=\pi/2\). Conjugation and the exponential addition law give \(|e^{iy}|=1\). Writing \(\cos y=\operatorname{Re}e^{iy}\) and \(\sin y=\operatorname{Im}e^{iy}\) now supplies the identities used below. These arguments use R03–R04's integral and fundamental theorem and the already proved exponential derivative.

Here is the Fourier calculation. For \(u\ge0\), integrate
\(G(z)=e^{iuz}/\cosh z\) around the positively oriented rectangle with vertices \(-R,R,R+i\pi,-R+i\pi\), where \(\cosh z=(e^z+e^{-z})/2\). Its only pole is \(z_0=i\pi/2\): a zero of \(\cosh z\) satisfies \(e^{2z}=-1\), whose modulus first forces \(\operatorname{Re}z=0\), and the preceding quadrant calculation then gives that unique zero in the strip. Since \(\sinh(i\pi/2)=i\), its simple principal-part coefficient is \(e^{-u\pi/2}/i\). The rectangle integral is therefore \(2\pi e^{-u\pi/2}\). The elementary contour fact used in this calculation can be obtained without a general residue theorem: for a continuously differentiable holomorphic function on a rectangle, the four side integrals sum to
\[
 \int\!\!\int(-\partial_yG+i\partial_xG)\,dx\,dy=0,
\]
by R04–R06's one-variable fundamental theorem, continuous rectangular Fubini proof, and the Cauchy–Riemann identity. Remove a small square about a simple pole and subdivide the remaining rectangle into rectangles. Cancellation of common sides reduces the boundary integral to the small-square integral. The remainder is bounded near the pole, so its integral tends to zero with the small-square perimeter. R07 computes the principal-part integral directly along the four sides as \(8iA=2\pi i\) times its coefficient, invariant under positive dilation and translation. This proves the contour fact just used. For the explicit exponential quotient here the bounded remainder follows from its second-order Taylor remainders, obtained directly from the uniformly convergent exponential series.

The vertical sides tend to zero as \(R\to\infty\). Indeed, for \(0\le y\le\pi\),
\[
 |\cosh(R+iy)|^2=\sinh^2R+\cos^2y\ge\sinh^2R,
 \qquad |e^{iu(\pm R+iy)}|=e^{-uy}\le1,
\]
so each side has integral of modulus at most \(\pi/\sinh R\). The top side contributes \(e^{-u\pi}\) times the bottom side, because \(\cosh(x+i\pi)=-\cosh x\) and its orientation is reversed. Absolute convergence follows from \((\cosh x)^{-1}\le2e^{-|x|}\). Consequently
\[
 (1+e^{-u\pi})\int_{\mathbb R}\frac{e^{iux}}{\cosh x}\,dx
       =2\pi e^{-u\pi/2},\qquad
 \int_{\mathbb R}\frac{e^{iux}}{\cosh x}\,dx
       =\frac{\pi}{\cosh(\pi u/2)}.
\]
Changing \(x\) to \(-x\) proves the same formula for negative \(u\). Substitute \(x=2\pi t\), \(u=s/(2\pi)\), to obtain (4). In particular the normalization follows by setting \(s=0\). The bound \(k(t)\le4e^{-2\pi|t|}\) controls every tail integral below.

<a id="cr02"></a>
## CR02. Spectral averaging preserves the cone

Fix a cyclic separating \(\gamma\in P\), abbreviate \(\Delta=\Delta_\gamma\), and put \(B=\log\Delta\), \(U_t=e^{itB}\). Define
\[
 Ku=\int_{\mathbb R}k(t)U_tu\,dt.
 \tag{5}
\]
On a compact interval the integrand is norm continuous, so its vector integral is the limit of Riemann sums in the complete Hilbert space. The tails have norm at most \(\|u\|\int_{|t|>T}k(t)\,dt\). This defines (5) on all of \(H\), with \(\|K\|\le1\). Every Riemann sum with nonnegative weights preserves the closed convex cone, since \(U_tP=P\). Thus
\[
 K(P)\subset P,\qquad K\gamma=\gamma.
 \tag{6}
\]

The exact spectral identity is
\[
 K=f(B),\qquad f(s)=\frac1{\cosh(s/4)}.
 \tag{7}
\]
To justify it without interchanging an unbounded operator and an integral, let \(E_n=1_{[-n,n]}(B)\). On \(E_nH\), \(B\) is bounded and \(U_tE_n\) is norm continuous. Operator Riemann sums for a finite interval are the bounded continuous calculus of the corresponding scalar Riemann sums. Their convergence is uniform for \(s\in[-n,n]\). The discarded tails are bounded uniformly in \(s\) by \(\int_{|t|>T}k(t)\,dt\). The scalar formula (4) therefore proves \(KE_n=f(B)E_n\). Finally \(E_nu\to u\) and both operators have norm at most one, proving (7). This also proves every truncation limit involved in the Fourier average.

<a id="cr03"></a>
## CR03. A linear positive correction in a cyclic corner

Suppose first that \(\xi\in P\) is cyclic and separating and that \(0\le\psi\le\omega_\xi\). The bounded commutant-form proof CG09a supplies a positive contraction \(b'\in M'\) with
\[
 \psi(a)=\langle b'\xi,a\xi\rangle\qquad(a\in M).
 \tag{8}
\]
By (2), \(b'\xi\in D(\Delta_\xi^{-1/2})\). Put
\[
 \zeta=\Delta_\xi^{-1/4}b'\xi.
\]
The second quarter-power description in (2) shows that both \(\zeta\) and \(\xi-\zeta=\Delta_\xi^{-1/4}(1-b')\xi\) belong to \(P\). Thus \(0\le\zeta\le\xi\). Apply CR02 to this cyclic modular operator and define
\[
 \eta=K\zeta
      =2(1+\Delta_\xi^{1/2})^{-1}b'\xi.
 \tag{9}
\]
The second equality includes a domain check. The spectral definition gives \(\zeta\in D(\Delta_\xi^{1/4})\) and \(\Delta_\xi^{1/4}\zeta=b'\xi\). For \(\lambda>0\),
\[
 \frac{2\lambda^{1/4}}{1+\lambda^{1/2}}
 =\frac2{\lambda^{1/4}+\lambda^{-1/4}}
 =f(\log\lambda).
\]
Spectral bands followed by convergence in the stated power domain prove (9). No multiplication of undefined unbounded powers occurs. Equations (6) give \(0\le\eta\le\xi\).

The multiplier \(r(\lambda)=2/(1+\lambda^{1/2})\) satisfies \(\lambda^{1/2}r(\lambda)\le2\), so \(\eta\in D(\Delta_\xi^{1/2})\). Since \(J\eta=\eta\) and \(J\Delta_\xi^{1/2}J=\Delta_\xi^{-1/2}\), it also lies in \(D(\Delta_\xi^{-1/2})\), and
\[
 F_\xi\eta=J\Delta_\xi^{-1/2}\eta
          =\Delta_\xi^{1/2}\eta,
 \qquad b'\xi=\tfrac12(\eta+F_\xi\eta).
 \tag{10}
\]
For the conjugate-linear adjoint, \(\langle Su,v\rangle=\langle S^*v,u\rangle\). Thus for \(a\in M\),
\[
 \langle F_\xi\eta,a\xi\rangle
   =\langle S_\xi(a\xi),\eta\rangle
   =\langle a^*\xi,\eta\rangle
   =\langle\xi,a\eta\rangle.
\]
Combining this with (8)–(10) proves
\[
 \boxed{\psi(a)=\tfrac12\bigl(\langle\eta,a\xi\rangle
                    +\langle\xi,a\eta\rangle\bigr),
          \qquad 0\le\eta\le\xi.}
 \tag{11}
\]
This is a linear correction formula, rather than a claim that the square root of a commutant derivative already belongs to the cone.

<a id="cr04"></a>
## CR04. The correction for a vector with proper support

Formula (11) holds for every \(\xi\in P\) and every normal positive \(\psi\le\omega_\xi\). For \(\xi=0\) take \(\eta=0\). Otherwise let \(p=s_\xi\in M\), \(j(p)=JpJ\), and \(q=pj(p)\). CG01–CG02 give \(\xi=q\xi\), \(s(\psi)\le p\), and \(\psi(a)=\psi(pap)\). CG07 gives the faithful unital order isomorphism
\[
 \theta:pMp\longrightarrow A=qMq\subset B(qH),
 \qquad \theta(x)=x|_{qH},
\]
and the self-dual cone \(P_q=qP=P\cap qH\). Transport the positive functional by \(\psi_q(\theta(x))=\psi(x)\). It satisfies \(0\le\psi_q\le\omega_\xi\) on \(A\).

The vector \(\xi\) is cyclic and separating for \(A\) on \(qH\). Indeed CG02 gives \(\overline{M\xi}=j(p)H\); applying \(q\) gives
\(\overline{A\xi}=qH\), since \(qx\xi=qxq\xi\). If \(x\in pMp\) and \(x\xi=0\), commutation with \(M'\) makes \(x\) vanish on \(M'\xi\), whose closure is \(pH\); hence \(x=0\). Faithfulness of \(\theta\) proves separatingness. The bounded form CG09a, applied on this cyclic space, also proves that \(\psi_q\) is a vector functional there; hence it is normal by H03. No converse between order-normality and ultraweak continuity is needed for this transport.

CG09 identifies the cyclic natural cone on \(qH\) with \(P_q\). Apply CR03 there. It gives \(\eta\in P_q\) with \(\xi-\eta\in P_q\) and the pairing formula for \(\psi_q\). For \(a\in M\),
\[
 \psi(a)=\psi(pap)=\psi_q(qaq),
 \quad\langle\eta,a\xi\rangle=\langle\eta,qaq\xi\rangle,
 \quad\langle\xi,a\eta\rangle=\langle\xi,qaq\eta\rangle.
\]
Thus (11) holds on the original algebra. Every reduction used a projection and a dense orbit; none used a countable ambient Hilbert basis. The target functional may have support strictly below \(p\).

<a id="cr05"></a>
## CR05. Realizing a dominated functional by a geometric correction

Let \(\psi\) be normal and \(0\le\psi\le\omega_{\xi_0}\), with \(\xi_0\in P\). Inductively suppose \(R_n=\omega_{\xi_n}-\psi\ge0\), and put \(E_n=R_n(1)\). Every residual is normal by H03. The norm of a positive functional is its value at one. For completeness, the scalar positive-form Cauchy–Schwarz inequality gives
\(|R_n(a)|^2\le R_n(1)R_n(a^*a)\le R_n(1)^2\|a\|^2\), and equality of the norm is attained at one.

Apply CR04 to \(R_n\le\omega_{\xi_n}\), obtaining \(0\le\eta_n\le\xi_n\) and (11) for \(R_n\). Set
\[
 h_n=\eta_n/2,\qquad \xi_{n+1}=\xi_n-h_n\in P.
 \tag{12}
\]
The cone membership follows from \(\xi_n-h_n=(\xi_n-\eta_n)+\eta_n/2\). Expansion of the vector functional gives the exact residual identity
\[
 \omega_{\xi_{n+1}}=\psi+\omega_{h_n},\qquad
 R_{n+1}=\omega_{h_n}.
 \tag{13}
\]
Self-duality gives \(\langle h_n,\xi_n-2h_n\rangle\ge0\). Since cone pairings are real, (11) at one gives \(E_n=\langle\eta_n,\xi_n\rangle=2\langle h_n,\xi_n\rangle\). Therefore
\[
 E_{n+1}=\|h_n\|^2
       \le\tfrac12\langle h_n,\xi_n\rangle
       =\tfrac14E_n.
 \tag{14}
\]
In particular
\[
 E_n\le4^{-n}E_0,\qquad
 \|\xi_{n+1}-\xi_n\|\le2^{-n-1}\sqrt{E_0},\qquad
 \|\xi_\infty-\xi_n\|\le2^{-n}\sqrt{E_0}.
 \tag{15}
\]
The last bound follows by summing the preceding geometric tail. Hilbert completeness and closedness of \(P\) give \(\xi_\infty\in P\). For arbitrary vectors,
\[
 \|\omega_u-\omega_v\|
 \le\|u-v\|(\|u\|+\|v\|),
 \tag{16}
\]
by adding and subtracting \(\langle v,au\rangle\) and taking the supremum over \(\|a\|\le1\). Thus (13)–(15) show \(\omega_{\xi_\infty}=\psi\). At a zero residual the correction is zero, and the sequence remains constant. The successive vectors are allowed to lose support; CR04 covers every such step.

<a id="cr06"></a>
## CR06. Dominated normal functionals are norm dense

The following real separation argument supplies the density step without a positive vector-series representation. Put \(\varphi=\omega_\Omega\). This is faithful and normal: \(\varphi(a^*a)=\|a\Omega\|^2\), and \(\Omega\) is separating. The orbit \(M'\Omega\) is dense. In fact its closed-span projection \(e\) belongs to \((M')'=M\) by H01; \(e\Omega=\Omega\), so separatingness forces \(e=1\).

Let \(X=(M_*)_{\mathrm{sa}}\) as a real Banach space. The involution \(\chi^*(a)=\overline{\chi(a^*)}\) preserves \(M_*\), as one sees by reversing the two vectors in H03's norm-summable coefficient representation; it is an isometric conjugate-linear involution. Every \(\chi\in M_*\) uniquely decomposes as
\[
 \chi=\frac{\chi+\chi^*}{2}
          +i\frac{\chi-\chi^*}{2i},
\]
with both displayed real components in \(X\). A continuous real-linear \(f:X\to\mathbb R\) extends to the continuous complex-linear functional
\[
 F(\chi)=f\left(\frac{\chi+\chi^*}{2}\right)
            +i f\left(\frac{\chi-\chi^*}{2i}\right).
\]
H03's predual duality makes \(F\) evaluation at some \(a\in M\). The identity \(F(\chi^*)=\overline{F(\chi)}\), and separation of \(M\) by its predual, give \(a=a^*\). Hence the continuous real dual of \(X\) is evaluation by \(M_{\mathrm{sa}}\).

Consider the convex cone
\[
 D=\{\chi\in M_*^+:\chi\le c\varphi
                          \text{ for some finite }c\ge0\}.
 \tag{17}
\]
For \(b'\in M'\), its vector functional is normal and belongs to \(D\), because for \(a\ge0\)
\[
 \omega_{b'\Omega}(a)=\|b'a^{1/2}\Omega\|^2
                    \le\|b'\|^2\varphi(a).
 \tag{18}
\]
If \(a=a^*\in M\) has \(\chi(a)\ge0\) for every \(\chi\in D\), (18) makes its quadratic form nonnegative on the dense space \(M'\Omega\). Continuity makes it nonnegative on all of \(H\), so \(a\ge0\). Conversely every \(a\ge0\) pairs nonnegatively with \(D\).

We include the separation step. For a closed convex cone \(C\) in a real Banach space and \(z\notin C\), choose \(r>0\) such that \(z\notin U=C+B(0,r)\). The open convex set \(U\) contains \(B(0,r)\), and its gauge
\[
 p(w)=\inf\{t>0:w\in tU\}
\]
is finite, nonnegative, positively homogeneous, and at most \(\|w\|/r\). Convexity gives subadditivity: \(w\in sU,v\in tU\) imply \(w+v\in(s+t)U\), after which one takes infima. Openness and convexity give \(U=\{w:p(w)<1\}\): a multiple \(tU\) with \(t<1\) is contained in \(U\), whereas for \(w\in U\) a slightly expanded multiple of \(w\) still lies in \(U\). Thus \(p(z)\ge1\). On \(\mathbb Rz\), define \(g(tz)=tp(z)\); it is dominated by \(p\) for \(t\ge0\) by homogeneity, and for \(t<0\) since then \(g(tz)\le0\le p(tz)\). F01's real Hahn–Banach proof extends \(g\) with \(g\le p\). Applying that bound to \(w\) and \(-w\) gives \(|g(w)|\le\|w\|/r\), hence continuity. Every positive multiple \(\lambda c\), \(c\in C\), lies in \(U\), so \(\lambda g(c)<1\) for every \(\lambda>0\); therefore \(g(c)\le0\). The functional \(-g\) is nonnegative on \(C\) and strictly negative at \(z\).

Apply this to \(C=\overline D\). Positivity is preserved under norm limits, so \(C\subset M_*^+\). If a positive normal \(\nu\) lay outside \(C\), separation and the real dual identification would give a self-adjoint \(a\) nonnegative on \(D\) with \(\nu(a)<0\). The preceding quadratic-form test forces \(a\ge0\), a contradiction. We have proved
\[
 \overline D^{\|\cdot\|}=M_*^+.
 \tag{19}
\]

<a id="cr07"></a>
## CR07. Cyclic realization and uniqueness

Let \(\phi\in M_*^+\). For \(\phi=0\) take zero. Otherwise use CR06 to choose \(\psi_n\in D\) with \(\|\psi_n-\phi\|\le4^{-n}\). Each \(\psi_n\le c_n\omega_\Omega\) is represented by CR05, starting with \(\xi_0=\sqrt{c_n}\Omega\); if \(c_n=0\), use zero. Let its representative be \(u_n\in P\). CG05 gives
\[
 \|u_n-u_m\|^2\le\|\psi_n-\psi_m\|
                           \le4^{-n}+4^{-m}.
\]
Hence \(u_n\) converges in Hilbert norm to \(u\in P\). Equation (16) proves \(\omega_u=\phi\). If \(v\in P\) also represents \(\phi\), the same CG05 bound gives \(\|u-v\|^2\le0\). Thus
\[
 \boxed{M_*^+\longrightarrow P,\qquad
       \phi\longmapsto u_\phi,
       \quad\phi(a)=\langle u_\phi,au_\phi\rangle}
 \tag{20}
\]
is well defined and unique. The estimates include \(\|u_\phi\|^2=\phi(1)\) and \(\|u_\phi-u_\psi\|^2\le\|\phi-\psi\|\). The target functional can be nonfaithful, and the proof places no countability restriction on the ambient Hilbert space. The zero algebra on the zero Hilbert space has only the zero functional and the same conclusion. CG10's support-corner reduction then applies (20) to arbitrary algebras in the constructed standard form.

### An exact two-point iteration

<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="560" viewBox="0 0 1100 560" role="img" aria-labelledby="title desc">
  <title id="title">The positive correction converges to a vector with proper support</title>
  <desc id="desc">Exact two-point diagonal algebra model. Target vector is one comma zero. Starting vector is two comma one. The next vectors are five-fourths comma one-half and forty-one-fortieths comma one-quarter. The iteration is x maps to one-half of x plus one over x, and y maps to y over two. Positive functional residuals have norm four, thirteen-sixteenths, and one hundred eighty-one over sixteen hundred, each shrinking by at most one quarter.</desc>
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker>
    <style>text{font-family:Arial,sans-serif;fill:#183042}.title{font-size:27px;font-weight:700}.body{font-size:22px}.label{font-size:21px;font-weight:600}.small{font-size:18px}.axis{stroke:#577284;stroke-width:2}.vec{stroke-width:3;fill:none;marker-end:url(#arr)}</style>
  </defs>
  <rect width="1100" height="560" fill="white"/>
  <text x="35" y="42" class="title">A nonfaithful target is reached inside the cone</text>
  <text x="35" y="74" class="body">M = C² diagonal on H = C²; P = R²₊; J = conjugation; Δ = 1</text>
  <rect x="80" y="137" width="400" height="293" fill="#eaf5ed"/>
  <path d="M80 255H480M255 137V430M430 137V430" stroke="#d0e4d5" stroke-width="1"/>
  <path d="M55 430H500M80 451V118" class="axis" marker-end="url(#arr)"/>
  <text x="61" y="451" class="small">0</text><text x="246" y="455" class="small">1</text><text x="421" y="455" class="small">2</text><text x="60" y="262" class="small">1</text>
  <text x="433" y="164" class="label">P</text>
  <path d="M80 430L430 255" class="vec" stroke="#28699d"/>
  <path d="M80 430L298.75 342.5" class="vec" stroke="#9764a3"/>
  <path d="M80 430L259.375 386.25" class="vec" stroke="#c87927"/>
  <path d="M430 255L298.75 342.5L259.375 386.25L255 430" fill="none" stroke="#358559" stroke-width="2" stroke-dasharray="6 5"/>
  <circle cx="255" cy="430" r="6" fill="#358559"/>
  <text x="344" y="236" class="label">ξ₀ = (2, 1)</text>
  <text x="323" y="341" class="label">ξ₁ = (5/4, 1/2)</text>
  <path d="M266 383H319" stroke="#c87927" stroke-width="1.5"/>
  <text x="326" y="389" class="label">ξ₂ = (41/40, 1/4)</text>
  <text x="177" y="493" class="label">u = (1, 0)</text>
  <text x="131" y="520" class="small">support s(ωu) = diag(1, 0)</text>
  <g transform="translate(580 140)">
    <text x="0" y="0" class="label">Target functional φ = (1, 0)</text>
    <text x="0" y="40" class="body">R = ωξ − φ = (x² − 1, y²) ≥ 0</text>
    <text x="0" y="88" class="body">η = (x − 1/x, y),   h = η/2</text>
    <text x="0" y="130" class="body">ξnew = ((x + 1/x)/2, y/2)</text>
    <text x="0" y="184" class="label">Exact residuals and proved bounds</text>
    <text x="0" y="226" class="body">E₀ = 4</text>
    <text x="0" y="267" class="body">E₁ = 13/16 ≤ E₀/4 = 1</text>
    <text x="0" y="308" class="body">E₂ = 181/1600 ≤ E₁/4 = 13/64</text>
    <text x="0" y="355" class="small">General mechanism: CR03–CR05, (11)–(15).</text>
  </g>
  <text x="35" y="550" class="small">Exact commutative model; the general proof uses modular averaging and support corners. Hiai 2020 v1, Lemmas 3.17–3.18, p.30.</text>
</svg>

In this figure the target functional is \(\phi=(1,0)\), represented by \(u=(1,0)\). Starting at \(\xi_0=(2,1)\), the modular operator is one and the correction (11) becomes \(\eta=(x-1/x,y)\) for \(\xi=(x,y)\), \(x\ge1,y\ge0\). Thus (12) gives \(\xi_1=(5/4,1/2)\) and \(\xi_2=(41/40,1/4)\). The functional residual norm is \(E=x^2-1+y^2\), giving the exact displayed values \(4,13/16,181/1600\). The target has the proper support \(\operatorname{diag}(1,0)\). This illustrates the support loss allowed by CR04 and the quantitative correction in CR05; the general cone and its modular operator need not be finite dimensional. The iterative method is Hiai's Lemma 3.18, printed page 30; the coordinates are explicit substitutions into (11)–(14).

## Sources and method attribution

The positive modular Fourier correction and its quarter-error iteration are the methods in Fumio Hiai, [*Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383v1](https://arxiv.org/pdf/2004.02383v1), Lemmas 3.17–3.18, printed/PDF page 30, in the proof of Theorem 3.12. CR01 spells out the scalar Fourier formula with the mass-one normalization for the convention used here. CR02–CR04 spell out the spectral bands, vector power domains, and corner transport. CR06 supplies a real Hahn–Banach proof of the density conclusion in Hiai's Lemma 3.19, printed page 30 and proof page 31, so that its positive vector-series representation is not an imported theorem here.

Huzihiro Araki's [*Some properties of modular conjugation operator of von Neumann algebras and a non-commutative Radon–Nikodym theorem with a chain rule*](https://msp.org/pjm/1974/50-2/pjm-v50-n2-p02-p.pdf), Theorem 6, printed pages 335–339, is an earlier primary proof of the cyclic realization conclusion. Its longer affiliated-operator and strip-estimate route is historical attribution, rather than a prerequisite of this proof. The preceding natural-cone construction credits its own free operator and cone antecedents. Credit for these mathematical methods is separate from the original CC0 expression above.
