# Relative commutants and central cocycles

A crossed product has two distinguished algebras: its coefficients and the algebra generated after adjoining translations. Their relative commutants need not be the center of the same algebra. We prove the precise identities for modular cores and trace-scaling systems, then recover every automorphism that fixes the coefficients from a cocycle in their center.

The analytic argument begins with a Fourier shear. Exponential decay away from zero forces a scalar function to be constant in one variable. A KMS identity and smoothing then turn that fact into an operator-algebra statement. State corners assemble the result over an arbitrary index set.

<a id="rcc-setting"></a>
## Two relative commutants

Let \(Q\ne0\) be a von Neumann algebra, and let \(\varphi\) be a faithful normal semifinite weight. In a faithful normal representation on \(H\), write
\[
 \begin{gathered}
 C_\varphi(Q)=Q\rtimes_{\sigma^\varphi}\mathbb R
       \subset B(L^2(\mathbb R,H)),\\
 \bigl[\pi_\varphi(x)\xi\bigr](r)
       =\sigma_{-r}^\varphi(x)\xi(r),\qquad
 [\lambda_\varphi(t)\xi](r)=\xi(r-t).
 \end{gathered}
 \tag{RCC0.a}
\]
The [normal regular construction](OA-FLOW-NR.md#oa-flow.nr.4) identifies different faithful normal representations by a normal isomorphism with these generator values. There is no restriction on the dimension of \(H\), the predual, or the center.

The first theorem concerns the coefficient algebra *inside its core*:
\[
 \boxed{\ \pi_\varphi(Q)'\cap C_\varphi(Q)=Z(C_\varphi(Q)).\ }
 \tag{RCC0.b}
\]
The second starts with a specified faithful normal semifinite trace \(\tau\) on \(N\ne0\) and a pointwise strongly continuous normal action \(\theta\) such that
\[
 \tau\circ\theta_s=e^{-s}\tau\quad(s\in\mathbb R).
 \tag{RCC0.c}
\]
Put \(P=N\rtimes_\theta\mathbb R\), with normal coefficient embedding \(i:N\to P\) and translations \(u_s\). We prove
\[
 \boxed{\ i(N)'\cap P=i(Z(N)).\ }
 \tag{RCC0.d}
\]
In this formula the center belongs to \(N\), not necessarily to \(P\). We often identify \(N\) with its image under \(i\). Neither theorem assumes that a coefficient algebra or crossed product is a factor or of type III.

Our scalar Fourier convention is
\[
 (\mathcal Ff)(q)=(2\pi)^{-1/2}
               \int_{\mathbb R}e^{-irq}f(r)\,dr.
 \tag{RCC0.e}
\]
The modular dual action has the negative character
\(\widehat{\sigma^\varphi}_s(\lambda_\varphi(t))=e^{-ist}\lambda_\varphi(t)\).
For double crossing we use the paired Haar measures \(dt\) and \(ds/(2\pi)\), as in [normal double duality](OA-FLOW-ND.md#nd-statement). The zero algebra has the corresponding trivial equalities and unique maps.

<a id="rcc-1"></a>
## 1. A scalar Fourier identity forces constancy

We begin with a scalar statement. Let \(H:\mathbb R^2\to\mathbb C\) be bounded and continuous. Suppose that for all \(f,g\in C_c^\infty(\mathbb R)\),
\[
 \begin{aligned}
 &\int_{\mathbb R^2}H(q,s)\overline{g(q)}
       \left(\int_{\mathbb R}e^{is(p-q)}f(p)\,dp\right)dq\,ds\\
 &\quad=
 \int_{\mathbb R^2}H(p,s)f(p)
       \left(\int_{\mathbb R}
          e^{i(s-i)(p-q)}\overline{g(q)}\,dq\right)dp\,ds.
 \end{aligned}
 \tag{RCC1.a}
\]
Then
\[
 H(q,s)=H(q,0)\qquad(q,s\in\mathbb R).
 \tag{RCC1.b}
\]
The orders in (RCC1.a) are part of the hypothesis. On the left integrate \(p\) first, and on the right integrate \(q\) first. The [integration-by-parts Fourier bounds](OA-FLOW-RF.md#oa-flow.rf.1) make the remaining two-variable integrals absolutely convergent. No absolute convergence of the unintegrated three-variable products is assumed.

For a test \(\Phi\in C_c^\infty(\mathbb R^2)\), define
\[
 \begin{aligned}
 L_H(\Phi)
   &=\int_{\mathbb R^2}H(q,s)
      \left(\int_{\mathbb R}e^{is(p-q)}\Phi(p,q)\,dp\right)dq\,ds,\\
 R_H(\Phi)
   &=\int_{\mathbb R^2}H(p,s)
      \left(\int_{\mathbb R}e^{i(s-i)(p-q)}
                                      \Phi(p,q)\,dq\right)dp\,ds.
 \end{aligned}
 \tag{RCC1.c}
\]
These functionals are continuous under uniform convergence of derivatives through order two on a fixed compact support. More explicitly, if \(\operatorname{supp}\Phi\subset[-R,R]^2\), splitting \(|s|\le1\) from \(|s|>1\) and integrating twice by parts in the inner variable gives
\[
 |L_H(\Phi)|+|R_H(\Phi)|
 \le C_R\|H\|_\infty
       \max_{|\gamma|\le2}\|\partial^\gamma\Phi\|_\infty.
 \tag{RCC1.d}
\]
On the right the differentiated compact amplitude is \(e^{p-q}\Phi(p,q)\); its derivatives have the stated bound because \(p,q\) remain in the fixed rectangle. The outer \(s\)-bounds are a constant on \([-1,1]\) and a constant times \(s^{-2}\) outside it.

We need the equality \(L_H=R_H\) for every \(\Phi\), not only product tests. Choose a nonnegative smooth compact bump \(\rho\) of integral one, and set \(\rho_\varepsilon(t)=\varepsilon^{-1}\rho(t/\varepsilon)\), using the [explicit smooth cutoffs](OA-FLOW-RF.md#oa-flow.rf.1). The functions
\[
 \Phi_\varepsilon(p,q)
   =\int_{\mathbb R^2}\Phi(u,v)
         \rho_\varepsilon(p-u)\rho_\varepsilon(q-v)\,du\,dv
 \tag{RCC1.e}
\]
converge with all derivatives of order at most two uniformly to \(\Phi\), with supports in one larger rectangle for \(0<\varepsilon\le1\). This follows by putting the derivatives on \(\Phi\) and using their uniform continuity.

For each fixed \(\varepsilon\), the compact integral in (RCC1.e) is approximated by Riemann sums uniformly in \(p,q\), together with those finitely many derivatives. Uniform continuity on the compact set of the integration variables and the output variables gives this assertion for one common mesh. Each Riemann sum is a finite sum of products of one smooth compact function of \(p\) and one of \(q\), and hence is covered by (RCC1.a). First pass to its integral using (RCC1.d), and then let \(\varepsilon\downarrow0\). Thus \(L_H(\Phi)=R_H(\Phi)\) for all two-variable tests.

Introduce a different functional:
\[
 \mathscr K(h)=
   \int_{\mathbb R^2}H(q,s)
       \left(\int_{\mathbb R}e^{isr}h(r,q)\,dr\right)dq\,ds,
 \qquad h\in C_c^\infty(\mathbb R^2).
 \tag{RCC1.f}
\]
For \(|s|\le1\) use the \(L^1\) norm of \(h\); for \(|s|>1\) integrate twice by parts in \(r\). Since each of these two scalar \(s\)-integrals contributes a factor 2,
\[
 |\mathscr K(h)|
 \le 2\|H\|_\infty
       \bigl(\|h\|_{L^1(\mathbb R^2)}
              +\|\partial_r^2h\|_{L^1(\mathbb R^2)}\bigr).
 \tag{RCC1.g}
\]
This explicit bound is all that will be needed about the functional; no distribution structure theorem is invoked.

Apply \(L_H=R_H\) to \(\Phi(p,q)=h(p-q,q)\). On the left substitute \(r=p-q\) in the inner integral. On the right substitute \(r=p-q\) in its inner \(q\)-integral, and then rename the outer \(p\)-variable \(q\). These are changes of variables inside the prescribed inner integrals. They give
\[
 \begin{gathered}
 \mathscr K(h)=\mathscr K(Th),\\
 (Th)(r,q)=e^r h(r,q-r),\qquad
 (T^{-1}h)(r,q)=e^{-r}h(r,q+r).
 \end{gathered}
 \tag{RCC1.h}
\]
Both maps preserve smooth compact tests. In particular the equality can be iterated in either direction.

For every integer \(m\),
\[
 \begin{aligned}
 T^m h(r,q)&=e^{mr}h(r,q-mr),\\
 \partial_r^2T^m h(r,q)
  &=e^{mr}\bigl(
       m^2h+2mh_r-2m^2h_q+h_{rr}\\
  &\hspace{6em}{}-2mh_{rq}+m^2h_{qq}
       \bigr)(r,q-mr).
 \end{aligned}
 \tag{RCC1.i}
\]
Suppose first that \(h\) is supported where \(r\le-\varepsilon\), with \(\varepsilon>0\). The substitution \(q'=q-nr\) has Jacobian one. The integrable compact derivatives in (RCC1.i) therefore give a constant \(C_h\), independent of \(n\), such that
\[
 \|T^nh\|_1+\|\partial_r^2T^nh\|_1
      \le C_h(1+n)^2e^{-n\varepsilon}\longrightarrow0.
 \tag{RCC1.j}
\]
Equations (RCC1.g)–(RCC1.h) imply \(\mathscr K(h)=0\). If \(h\) is supported where \(r\ge\varepsilon\), use \(m=-n\) instead, obtaining the same estimate for \(T^{-n}h\). A smooth partition into the two half-planes now shows
\[
 \mathscr K(h)=0
 \quad\text{if }\operatorname{supp}h\cap(\{0\}\times\mathbb R)
          =\varnothing.
 \tag{RCC1.k}
\]
The decay is a limiting argument. No finite iterate has been claimed to vanish.

Fix \(\eta\in C_c^\infty(\mathbb R)\), and define the bounded continuous function
\[
 h_\eta(s)=\int_{\mathbb R}\eta(q)H(q,s)\,dq.
\]
For \(\chi\in C_c^\infty(\mathbb R\setminus\{0\})\) and \(b\in\mathbb R\), put \(h(r,q)=e^{-ibr}\chi(r)\eta(q)\) in (RCC1.k). With the exact inverse kernel
\(k_\chi(t)=(2\pi)^{-1}\int e^{-itr}\chi(r)\,dr\), we obtain
\[
 0=2\pi\int_{\mathbb R}k_\chi(b-s)h_\eta(s)\,ds
       =2\pi(k_\chi*h_\eta)(b).
 \tag{RCC1.l}
\]
All integrals here are absolutely convergent after the inner Fourier integral, by the rapid decay of \(k_\chi\).

Regard \(h_\eta\) as an element of \(L^\infty(\mathbb R)\), with translation action
\(\alpha_t h(b)=h(b-t)\). Its predual action is translation on \(L^1\), which is norm continuous; this follows first for continuous compact functions and then by \(L^1\) density and translation isometry. Thus the [normal smooth-filter theorem AL7](OA-FLOW-AL.md#equation-al7) applies. Equation (RCC1.l) puts the spectrum of \(h_\eta\) inside \(\{0\}\), and the [proved singleton conclusion](OA-FLOW-SS.md#ss-3) makes it fixed under every translation. AL uses the positive Fourier convention and SS the negative one; the spectral singleton \(\{0\}\) is unchanged by this reflection.

For each fixed translation parameter, the two continuous functions representing the resulting \(L^\infty\) equality agree everywhere: a nonzero continuous difference would be nonzero on an interval of positive measure. It follows that \(h_\eta\) is constant. No intersection of uncountably many full-measure sets is taken.

Hence, for each fixed \(s\),
\[
 \int_{\mathbb R}\eta(q)\bigl(H(q,s)-H(q,0)\bigr)\,dq=0
       \qquad(\eta\in C_c^\infty(\mathbb R)).
 \tag{RCC1.m}
\]
If the continuous difference were nonzero somewhere, one complex rotation would have positive real part on a smaller interval. A nonnegative smooth bump in that interval would contradict (RCC1.m). This proves (RCC1.b).

<a id="rcc-schwartz"></a>
### The Schwartz topology and the two directions of iteration

The functional in (RCC1.f) also has a precise Schwartz-space interpretation. Define \(\mathcal S(\mathbb R^2)\) to be the smooth functions for which every seminorm
\[
 p_{N,m}(h)=
 \max_{a+b\le m}\ \sup_{r,q\in\mathbb R}
 (1+|r|+|q|)^N|\partial_r^a\partial_q^b h(r,q)|
 \qquad(N,m\in\mathbb N_0)
 \tag{RCC1.n}
\]
is finite. Convergence in the Schwartz topology means convergence in each of these seminorms.

For \(h\in\mathcal S(\mathbb R^2)\), keep the inner Fourier integral first in (RCC1.f). Twice integrating by parts in \(r\) has no boundary terms, because \(h\) and its first derivative vanish at infinity. The same split at \(|s|=1\) therefore proves (RCC1.g). Since
\[
 \int_{\mathbb R^2}(1+|r|+|q|)^{-4}\,dr\,dq=\frac23,
\]
we obtain
\[
 |\mathscr K(h)|
 \le\frac83\|H\|_\infty p_{4,2}(h).
 \tag{RCC1.o}
\]
In particular the two outer integrals are absolutely convergent after the inner Fourier integral. This defines a continuous linear functional on \(\mathcal S(\mathbb R^2)\), which is the meaning of a tempered distribution here.

For completeness, compact smooth tests are dense in this topology. Choose a smooth cutoff \(\chi\) equal to one on \([-1,1]\) and supported in \([-2,2]\), and set
\[
 h_R(r,q)=\chi(r/R)\chi(q/R)h(r,q),\qquad R\ge1.
\]
In the product rule for \(h_R-h\), every nonzero term is supported where \(\max(|r|,|q|)\ge R\). A differentiated cutoff contributes a bounded constant times \(R^{-j}\), and one additional power of decay in \(h\) gives
\[
 p_{N,m}(h_R-h)
 \le C_{\chi,m}(1+R)^{-1}p_{N+1,m}(h).
 \tag{RCC1.p}
\]
Thus \(h_R\to h\) in every seminorm, and the continuous extension of \(\mathscr K\) from compact tests is unique. The finite sum of product-rule constants is independent of \(R\) and \(h\).

We next retain all derivatives and polynomial weights in the iteration estimate. For \(h\in C_c^\infty(\mathbb R^2)\), \(a,b\in\mathbb N_0\), and any integer \(k\), direct differentiation gives
\[
 \partial_r^a\partial_q^b(T^k h)(r,q)
 =e^{kr}\bigl(k+\partial_r-k\partial_q\bigr)^a
            \partial_q^b h(r,q-kr).
 \tag{RCC1.q}
\]
The three operators inside the parentheses commute. On expanding the \(a\)-th power, each coefficient is bounded by a constant times \((1+|k|)^a\), and only derivatives of \(h\) through order \(a+b\) occur.

Take \(R\ge1\) with \(\operatorname{supp}h\subset[-R,R]^2\). Wherever a derivative on the right of (RCC1.q) is nonzero, \(|r|\le R\) and \(|q-kr|\le R\), so
\[
 1+|r|+|q|\le (1+2R)(1+|k|).
\]
If \(\operatorname{supp}h\subset\{r\le-\varepsilon\}\), use \(k=n\ge1\). If it is contained in \(\{r\ge\varepsilon\}\), use \(k=-n\). In the respective cases this proves, for every \(N,m\),
\[
 \begin{aligned}
 p_{N,m}(T^nh)&\le C_{h,N,m}(1+n)^{N+m}e^{-\varepsilon n},
       &&\operatorname{supp}h\subset\{r\le-\varepsilon\},\\
 p_{N,m}(T^{-n}h)&\le C_{h,N,m}(1+n)^{N+m}e^{-\varepsilon n},
       &&\operatorname{supp}h\subset\{r\ge\varepsilon\}.
 \end{aligned}
 \tag{RCC1.r}
\]
Both bounds tend to zero. This is convergence in the full Schwartz topology, including the polynomial weights in the sheared variable \(q\).

For a compact test \(h\) whose support avoids \(\{r=0\}\), choose \(\varepsilon>0\) so that \(h\) vanishes on \(|r|<\varepsilon\), and write \(h=h_-+h_+\), using its restrictions to the negative and positive half-planes, extended by zero. They are smooth because of the intervening zero strip. Put
\[
 g_n=\sum_{k=0}^{n-1}T^k h_-
           -\sum_{k=1}^{n}T^{-k}h_+ .
 \tag{RCC1.s}
\]
Each \(g_n\) is a compact smooth test, although its support may depend on \(n\). The two finite telescoping sums give the exact identity
\[
 (1-T)g_n=h-T^n h_- -T^{-n}h_+
       \longrightarrow h\quad\text{in }\mathcal S(\mathbb R^2).
 \tag{RCC1.t}
\]
Applying the continuous functional \(\mathscr K\), together with (RCC1.h) on each \(g_n\), recovers (RCC1.k). The identity with \(T\) is used on compact tests: multiplication by \(e^r\) need not preserve the entire Schwartz space. Neither remainder in (RCC1.t) is assumed to become zero at a finite stage.

<a id="rcc-point-support"></a>
### Point-supported distributions and the polynomial conclusion

Here is a direct distribution proof of the scalar conclusion, including the finite-order statement. In one variable write
\[
 q_{N,m}(f)=\max_{0\le j\le m}\sup_{r\in\mathbb R}
                   (1+|r|)^N|f^{(j)}(r)|.
 \tag{RCC1.u}
\]
The Schwartz space consists of the smooth functions with every \(q_{N,m}\) finite. A tempered distribution here is a continuous complex-linear functional \(\mathscr T\) on this space. Say that it is supported at zero if \(\mathscr T(f)=0\) for every compact smooth \(f\) whose support avoids zero.

**Finite jets determine the distribution.** We prove that there are an integer \(m\ge0\) and constants \(c_0,\ldots,c_m\) with
\[
 \mathscr T(f)=\sum_{j=0}^{m}c_j f^{(j)}(0)
                  \qquad(f\in\mathcal S(\mathbb R)).
 \tag{RCC1.v}
\]
Continuity at zero first supplies \(C>0\), \(N,m\ge0\) such that
\[
 |\mathscr T(f)|\le Cq_{N,m}(f).
 \tag{RCC1.w}
\]
Indeed a finite collection of the defining seminorm conditions gives a neighborhood on which \(|\mathscr T|<1\). Taking the largest two indices dominates that collection by one seminorm; rescaling each nonzero \(f\) into the neighborhood gives (RCC1.w).

Choose a smooth compact \(\chi\) equal to one on \([-1,1]\) and supported in \([-2,2]\), using [RF1's cutoff construction](OA-FLOW-RF.md#oa-flow.rf.1). The one-variable product-rule estimate corresponding to (RCC1.p) is
\[
 q_{N,m}\bigl(\chi(\,\cdot\,/R)f-f\bigr)
       \le C_{\chi,m}(1+R)^{-1}q_{N+1,m}(f),
       \qquad R\ge1.
 \tag{RCC1.x}
\]
Every nonzero product-rule term lies where \(|r|\ge R\); derivatives of the cutoff contribute \(R^{-k}\), and one additional decay power gives the stated bound. Thus compact tests are dense in \(\mathcal S(\mathbb R)\).

If \(f\in\mathcal S(\mathbb R)\) vanishes near zero, all \(\chi(\,\cdot\,/R)f\) are compact tests with support away from zero. Their convergence and continuity give \(\mathscr T(f)=0\). In particular, for every \(\varepsilon>0\),
\[
 \mathscr T(f)=\mathscr T(\chi_\varepsilon f),
 \qquad \chi_\varepsilon(r)=\chi(r/\varepsilon).
 \tag{RCC1.y}
\]
The difference is a Schwartz function vanishing near zero.

Suppose now that \(f^{(j)}(0)=0\) for \(0\le j\le m\), and let
\[
 \omega_f(t)=\sup_{|r|\le t}|f^{(m)}(r)|.
\]
Continuity gives \(\omega_f(t)\to0\) as \(t\downarrow0\). Repeated integration of the derivative, starting at zero, gives for \(0\le j\le m\) and \(|r|\le2\varepsilon\)
\[
 |f^{(j)}(r)|
       \le \frac{|r|^{m-j}}{(m-j)!}\omega_f(2\varepsilon).
 \tag{RCC1.z}
\]
For \(j=m\) this is the defining bound; for smaller \(j\), integrate the bound for \(j+1\) along the interval from zero to \(r\). This also covers negative \(r\) by absolute values.

In the \(j\)-th derivative of \(\chi_\varepsilon f\), a term with \(k\) derivatives on the cutoff is bounded by a constant times
\[
 \varepsilon^{-k}\varepsilon^{m-(j-k)}
                 \omega_f(2\varepsilon)
       =\varepsilon^{m-j}\omega_f(2\varepsilon).
\]
Every term is supported in \([-2\varepsilon,2\varepsilon]\). For \(0<\varepsilon\le1\), all weights \((1+|r|)^N\) there are at most \(3^N\), and \(m-j\ge0\). Hence
\[
 q_{N,m}(\chi_\varepsilon f)
       \le C_{\chi,N,m}\omega_f(2\varepsilon)\longrightarrow0.
 \tag{RCC1.aa}
\]
Equations (RCC1.w) and (RCC1.y) imply \(\mathscr T(f)=0\). The argument includes \(m=0\).

Put \(b_j(r)=\chi(r)r^j/j!\), \(0\le j\le m\). Because \(\chi=1\) near zero, \(b_j^{(k)}(0)=\delta_{jk}\) for \(0\le k\le m\). The function \(f-\sum_{j=0}^m f^{(j)}(0)b_j\) has all these derivatives zero, so the preceding conclusion proves (RCC1.v) with \(c_j=\mathscr T(b_j)\). Equivalently, with the convention \(\delta_0^{(j)}(f)=(-1)^jf^{(j)}(0)\),
\[
 \mathscr T=\sum_{j=0}^{m}(-1)^jc_j\delta_0^{(j)}.
 \tag{RCC1.ab}
\]
Each functional on the right is continuous and supported at zero, so this is an exact characterization. Translation gives the same statement at any other specified point, with derivatives evaluated there.

**The Fourier transform of a bounded continuous function.** Let \(b:\mathbb R\to\mathbb C\) be bounded and continuous, and define
\[
 \mathscr T_b(f)=\int_{\mathbb R}b(s)
                   \left(\int_{\mathbb R}e^{isr}f(r)\,dr\right)ds.
 \tag{RCC1.ac}
\]
For Schwartz \(f\), two integrations by parts and the split at \(|s|=1\) give
\[
 |\mathscr T_b(f)|
 \le2\|b\|_\infty\bigl(\|f\|_1+\|f''\|_1\bigr)
 \le8\|b\|_\infty q_{2,2}(f).
 \tag{RCC1.ad}
\]
The last inequality uses \(\int_{\mathbb R}(1+|r|)^{-2}\,dr=2\). The outer integral is absolutely convergent after evaluating the inner Fourier integral. Thus \(\mathscr T_b\) is a tempered distribution.

If it is supported at zero, take the coefficients in (RCC1.v). For any \(g\in C_c^\infty(\mathbb R)\), set
\[
 f(r)=\frac1{2\pi}\int_{\mathbb R}e^{-isr}g(s)\,ds.
 \tag{RCC1.ae}
\]
The repeated differentiation and integration-by-parts bounds in [RF1](OA-FLOW-RF.md#oa-flow.rf.1) give \(f\in\mathcal S(\mathbb R)\); its Fourier inversion, proved from [FF2](OA-FLOW-FF.md#oa-flow.ff.3), gives \(\int e^{isr}f(r)\,dr=g(s)\) everywhere. Differentiating the compact integral in (RCC1.ae) therefore yields
\[
 \begin{aligned}
 \int b(s)g(s)\,ds
   &=\mathscr T_b(f)
     =\sum_{j=0}^{m}\frac{c_j}{2\pi}
                         \int(-is)^j g(s)\,ds,\\
 b(s)&=\frac1{2\pi}\sum_{j=0}^{m}c_j(-is)^j
                   \qquad(s\in\mathbb R).
 \end{aligned}
 \tag{RCC1.af}
\]
The second equality follows from the first by continuity: a nonzero difference, rotated by a fixed complex phase, would have positive real part on an interval and could be tested against a nonnegative smooth bump there. It is an everywhere equality, not merely an almost-everywhere representative statement. A polynomial bounded on \(\mathbb R\) is constant: for a nonzero leading coefficient of positive degree, its leading power dominates the finitely many lower powers for large \(|s|\). Consequently \(b\) is constant.

**Recovering every parameter in \(H\).** Return to the bounded continuous \(H\) of (RCC1.a), and let \(v\in C_c^\infty(\mathbb R\setminus\{0\})\). The function
\[
 F_v(q)=\int_{\mathbb R}H(q,s)
               \left(\int_{\mathbb R}e^{isr}v(r)\,dr\right)ds
 \tag{RCC1.ag}
\]
is continuous by dominated convergence: the inner transform is integrable by RF1 and bounds the integrand uniformly in \(q\), up to \(\|H\|_\infty\). For every compact smooth \(\eta(q)\), scalar Fubini gives
\[
 \int_{\mathbb R}\eta(q)F_v(q)\,dq
       =\mathscr K(v\otimes\eta)=0
 \tag{RCC1.ah}
\]
by (RCC1.k), or by the full Schwartz limit (RCC1.t). Its absolute bound is \(\|H\|_\infty\|\eta\|_1\|\widehat v_+\|_1\), where \(\widehat v_+(s)=\int e^{isr}v(r)\,dr\). The continuous bump test makes \(F_v(q)=0\) for every \(q\).

For each fixed \(q\), this says that the tempered distribution (RCC1.ac) associated with \(b(s)=H(q,s)\) is supported at zero. The theorem and (RCC1.af) make it a polynomial, and boundedness makes it constant. Thus \(H(q,s)=H(q,0)\) for every \(q,s\), with no selection of common null sets. This supplies the point-support proof independently of the spectral-singleton argument above.

<a id="rcc-2"></a>
## 2. A KMS test for a continuous multiplier

For this section, let \(Q\) have a faithful normal state \(\omega\), and use its standard GNS representation on \(H_\omega\), with cyclic vector \(\xi_\omega\). No separability of \(H_\omega\) is assumed. Write \(\sigma=\sigma^\omega\), and let
\[
 C=Q\rtimes_\sigma\mathbb R
\]
act on \(L^2(\mathbb R,H_\omega)\) in the regular convention. Let \(\mathcal F\) be the scalar unitary transform
\[
 (\mathcal Ff)(q)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-irq}f(r)\,dr.
 \tag{RCC2.a}
\]
The [full scalar Fourier theorem](OA-FLOW-FF.md#oa-flow.ff.3) proves its normalization and inverse. Its tensor amplification \(\mathscr F=1_{H_\omega}\otimes\mathcal F\) is unitary on the entire Hilbert tensor product: the isometry and the dense onto range are first checked on finite tensors. The [full \(L^2\) tensor identification](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) realizes this as the whole Hilbert-valued function space. Put
\[
 \Pi(x)=\mathscr F\pi_\omega(x)\mathscr F^*.
\]

**Multiplier lemma.** Suppose \(a:\mathbb R\to Q\) is bounded and sigma-strong-star continuous, and multiplication by \(a(q)\) commutes with \(\Pi(Q)\). In particular, \(q\mapsto a(q)\xi\) and \(q\mapsto a(q)^*\xi\) are continuous for every \(\xi\in H_\omega\). Then
\[
 a(q)\in Q_\omega\qquad(q\in\mathbb R).
 \tag{RCC2.b}
\]
The multiplication operator \(M_a\) is defined on all of \(L^2(\mathbb R,H_\omega)\). For each fixed vector its field is continuous with separable image on a countable compact exhaustion. Finite-valued approximation of an arbitrary strongly measurable vector field, and the common bound \(\sup_q\|a(q)\|\), therefore prove strong measurability of its product with \(a\). The same reasoning gives \(M_a^*=M_{a^*}\).

Fix \(x\in Q\) and \(f,g\in C_c^\infty(\mathbb R)\). Throughout, Hilbert inner products are linear in the first variable. Pair \(M_a\Pi(x)=\Pi(x)M_a\) against \(\xi_\omega f,\xi_\omega g\). Fourier inversion gives
\[
 \begin{aligned}
 &\langle\Pi(x)(\xi_\omega f),M_{a^*}(\xi_\omega g)\rangle\\
 &\quad=\frac1{2\pi}\int_{\mathbb R^2}
       \overline{g(q)}\,\omega(a(q)\sigma_{-s}(x))
       \left(\int_{\mathbb R}e^{is(p-q)}f(p)\,dp\right)dq\,ds,\\[2mm]
 &\langle\Pi(x)M_a(\xi_\omega f),\xi_\omega g\rangle\\
 &\quad=\frac1{2\pi}\int_{\mathbb R^2}
       f(p)\,\omega(\sigma_{-s}(x)a(p))
       \left(\int_{\mathbb R}e^{is(p-q)}
                            \overline{g(q)}\,dq\right)dp\,ds .
 \end{aligned}
 \tag{RCC2.c}
\]
For completeness, the integral inverse-Fourier formula for the vector functions used here agrees with the tensor transform. Approximate a strongly measurable \(L^1\cap L^2\) vector function by finite-vector simple functions in both norms. The \(L^1\) error bounds the integral-transform error uniformly, while the tensor transform is an \(L^2\) isometry. An almost-everywhere convergent subsequence of the \(L^2\) approximants identifies the two limits. This applies to the compact continuous fields \(a^*\xi_\omega g\) and \(a\xi_\omega f\).

In the first line of (RCC2.c), the inner \(p\)-transform of \(f\) decays faster than any power of \(s\); the remaining \(q\)-variable has compact support and the coefficient is bounded by \(\|a\|_\infty\|x\|\). In the second line use the inner \(q\)-transform of \(\overline g\). These bounds justify scalar interchange after those inner integrals. They require no derivative of \(a\). The factor \(1/(2\pi)\) is the product of the two inverse-transform factors.

Apply [the state KMS strip and its norm bound](OA-FLOW-KT.md#oa-flow.kt.2) to \(x,a(p)\), with the time variable reversed. It supplies a bounded continuous function on \(-1\le\operatorname{Im}z\le0\), holomorphic in the open strip, such that
\[
 \begin{gathered}
 G(s,p)=\omega(\sigma_{-s}(x)a(p)),\\
 G(s-i,p)=\omega(a(p)\sigma_{-s}(x)),\\
 |G(z,p)|\le\|x\|\,\|a(p)\|.
 \end{gathered}
 \tag{RCC2.d}
\]
Explicitly, if \(G_{x,a(p)}\) is KT's upper-strip function, use \(G(z,p)=G_{x,a(p)}(-z)\). Write \(d=a(p)-a(p')\). Since \(\omega(y)=\langle y\xi_\omega,\xi_\omega\rangle\), Hilbert Cauchy–Schwarz bounds the two horizontal-edge differences by \(\|x\|\|d\xi_\omega\|\) and \(\|x\|\|d^*\xi_\omega\|\), respectively: move the left factor across the inner product in \(\omega(\sigma_{-s}(x)d)\) and in \(\omega(d\sigma_{-s}(x))\). The strip difference is bounded on the whole strip by (RCC2.d), so the earlier [bounded-strip maximum principle AS1](OA-FLOW-AS.md#equation-as1) gives
\[
 \sup_{-1\le\operatorname{Im}z\le0}
     |G(z,p)-G(z,p')|
       \le\|x\|\max\{\|d\xi_\omega\|,\|d^*\xi_\omega\|\}.
 \tag{RCC2.e}
\]
Strong-star continuity makes both vector seminorms tend to zero as \(p'\to p\). Their vector-valued maps are uniformly continuous on each compact set, so the dependence of \(G(z,p)\) on \(p\) is uniformly continuous there throughout the strip.

Put
\[
 b(z)=\int_{\mathbb R}e^{-izq}\overline{g(q)}\,dq.
\]
This is entire. If \(z=s+iy\), \(-1\le y\le0\), integrate by parts against the compact amplitude \(e^{yq}\overline{g(q)}\). For every integer \(m\ge0\), a constant \(B_{g,m}\) gives
\[
 |b(s+iy)|\le B_{g,m}(1+|s|)^{-m}
       \qquad(-1\le y\le0).
 \tag{RCC2.f}
\]
For \(p\) in the compact support of \(f\), the factor \(|e^{i(s+iy)p}|=e^{-yp}\) is uniformly bounded. Thus
\(e^{izp}b(z)G(z,p)\) is bounded by a constant times \((1+|\operatorname{Re}z|)^{-2}\), uniformly in that \(p\)-set and on the closed strip.

Use the [rectangle Cauchy theorem](OA-FLOW-SF.md#oa-flow.sf4.rectangle-cauchy) first between horizontal lines of heights \(-1+\delta\) and \(-\delta\), where \(0<\delta<1/2\), and vertical sides at \(\pm R\). The vertical integrals tend to zero as \(R\to\infty\), by (RCC2.f). The two horizontal integrals therefore agree. Continuity at the strip edges and the same integrable bound permit \(\delta\downarrow0\), giving
\[
 \int_{\mathbb R}e^{isp}b(s)G(s,p)\,ds
  =\int_{\mathbb R}e^{i(s-i)p}b(s-i)G(s-i,p)\,ds.
 \tag{RCC2.g}
\]
The bound is uniform for \(p\in\operatorname{supp}f\), so multiplication by \(f(p)\), integration in \(p\), and the boundary limits are legitimate by scalar dominated convergence.

The two pairings in (RCC2.c) are equal. Replacing their second member by (RCC2.g) gives exactly (RCC1.a), after canceling \(1/(2\pi)\), for
\[
 H(q,s)=\omega(a(q)\sigma_{-s}(x)).
\]
This function is bounded and jointly continuous. For example
\(H(q,s)=\langle\sigma_{-s}(x)\xi_\omega,a(q)^*\xi_\omega\rangle\);
modular strong continuity and strong-star continuity of \(a\) give joint continuity. Section 1 therefore makes it independent of \(s\).

By [whole-positive modular invariance and GNS covariance](OA-FLOW-MW.md#oa-flow.mw.4), the state is invariant under \(\sigma\). Hence
\[
 \omega\bigl((\sigma_s(a(q))-a(q))x\bigr)=0
       \qquad(x\in Q,\ s,q\in\mathbb R).
 \tag{RCC2.h}
\]
The preceding argument applied to every \(x\in Q\). For fixed \(s,q\), take
\(x=(\sigma_s(a(q))-a(q))^*\). Faithfulness gives \(\sigma_s(a(q))=a(q)\), proving (RCC2.b). Both the range of test elements \(x\) and faithfulness are used in this last step.

<a id="rcc-3"></a>
## 3. Recovering an ambient relative commutant by smoothing

Retain the faithful-state setting of Section 2, and write \(H=H_\omega\), \(C=C_\omega\). We will prove
\[
 C'\cap\bigl(Q\overline\otimes B(L^2(\mathbb R))\bigr)=Z(C)
       \quad\text{on }H\otimes L^2(\mathbb R).
 \tag{RCC3.a}
\]
Here \(C'\) is the commutant in the full bounded-operator algebra. The ambient tensor algebra in (RCC3.a) is essential.

Let \(X\) belong to the left side, and put \(S=\mathscr F X\mathscr F^*\). Since \(X\) commutes with every translation \(\lambda(t)\), \(S\) commutes with every scalar multiplier \(e^{-itq}\). The [scalar character-generation theorem](OA-FLOW-ND.md#nd-weyl-proof) says that these multipliers generate \(L^\infty(\mathbb R)\), whose multiplication algebra is [maximal abelian](OA-FLOW-ND.md#nd-multiplication). Thus
\[
 [S,1\otimes M_h]=0\quad(h\in L^\infty(\mathbb R)).
 \tag{RCC3.b}
\]
Moreover \(S\) commutes with \(Q'\otimes1\), by the assumed ambient tensor membership and the scalar Fourier conjugation, and with \(\Pi(Q)\), because \(X\in C'\).

For \(\xi,\eta\in H\), define a scalar operator \(S_{\xi,\eta}\) by
\[
 \langle S_{\xi,\eta}f,g\rangle
       =\langle S(\xi\otimes f),\eta\otimes g\rangle
       \qquad(f,g\in L^2(\mathbb R)).
 \tag{RCC3.c}
\]
The [Hilbert representation argument](OA-FLOW-SF.md#oa-flow.shared-foundations.sf-0), applied to the bounded sesquilinear form, gives this operator and
\(\|S_{\xi,\eta}\|\le\|S\|\|\xi\|\|\eta\|\). Equation (RCC3.b) makes it commute with the scalar multiplication algebra. Its maximal abelianness gives a unique class
\[
 S_{\xi,\eta}=M_{b_{\xi,\eta}},\qquad
 b_{\xi,\eta}\in L^\infty(\mathbb R),\qquad
 \|b_{\xi,\eta}\|_\infty\le\|S\|\|\xi\|\|\eta\|.
 \tag{RCC3.d}
\]
The dependence of these classes on \(\xi,\eta\) is sesquilinear. We keep them as \(L^\infty\) classes; no simultaneous representatives for all pairs of vectors are chosen.

To smooth them, define on the original regular variable \(t\)
\[
 [B_r\zeta](t)=e^{irt}\zeta(t).
\]
These unitaries form a strongly continuous group on the entire \(L^2(\mathbb R,H)\). One can first check this on finite tensors by scalar dominated convergence, and then use their common norm bound and tensor density. Their conjugations fix every \(\pi_\omega(x)\) and send \(\lambda(t)\) to \(e^{irt}\lambda(t)\). They therefore normalize \(C\), \(C'\), and the ambient tensor algebra.

In Fourier coordinates, \(\mathscr F B_r\mathscr F^*=1\otimes L_r\), where
\((L_rf)(q)=f(q-r)\). Put
\[
 \beta_r(Y)=(1\otimes L_r)Y(1\otimes L_r)^*.
\]
On the scalar entries of \(S\), this sends \(b(q)\) to \(b(q-r)\). The action is point-ultraweakly continuous on the full operator algebra: strong-star continuity of the unitaries gives continuity on vector functionals, and the [summable vector-series predual](OA-FLOW-CP.md#oa-flow.cp.6) gives it for every normal functional by a finite-head and uniform-tail estimate.

For \(k\in C_c^\infty(\mathbb R)\), the [normal integrated-action theorem](OA-FLOW-AT.md#oa-flow.at.5) defines
\[
 S_k=\int_{\mathbb R}k(r)\beta_r(S)\,dr,\qquad
 \|S_k\|\le\|k\|_1\|S\|.
 \tag{RCC3.e}
\]
This is a weak-star integral. Passing each bounded commutation relation through the integral shows that \(S_k\) still commutes with \(\Pi(Q)\) and \(Q'\otimes1\). Its conjugate
\(X_k=\mathscr F^*S_k\mathscr F\) still belongs to \(C'\) and the ambient tensor algebra.

For every \(q\in\mathbb R\), the formula
\[
 \langle a_k(q)\xi,\eta\rangle
      =\int_{\mathbb R}k(q-v)b_{\xi,\eta}(v)\,dv
 \tag{RCC3.f}
\]
defines a bounded sesquilinear form, of bound
\(\|S\|\|k\|_1\|\xi\|\|\eta\|\), hence a unique operator \(a_k(q)\in B(H)\). The integral pairs an \(L^\infty\) class with an \(L^1\) function and is independent of its representative, for each \(q\) and each pair of vectors. Sesquilinearity is therefore exact without choosing a common exceptional set.

If \(y'\in Q'\), commutation of \(S\) with \(y'\otimes1\) gives the class identity
\[
 b_{y'\xi,\eta}=b_{\xi,(y')^*\eta}.
\]
Insert this into (RCC3.f). It proves \(a_k(q)y'=y'a_k(q)\) for every \(q\). Since \(Q\) is a von Neumann algebra in its faithful normal GNS representation, \(Q''=Q\), so \(a_k(q)\in Q\). The same form estimate gives
\[
 \begin{gathered}
 \|a_k(q)\|\le\|S\|\|k\|_1,\\
 \|a_k(q)-a_k(q')\|
    \le\|S\|\,\|k(q-\cdot)-k(q'-\cdot)\|_1.
 \end{gathered}
 \tag{RCC3.g}
\]
Translation continuity in \(L^1\) proves that \(a_k\) is norm continuous. Thus Section 2's multiplication construction makes \(M_{a_k}\) a bounded operator on the whole \(L^2\) space.

We now identify that operator, rather than merely its formal field. For \(f,g\in L^2(\mathbb R)\), scalar Fubini gives
\[
 \begin{aligned}
 \langle S_k(\xi\otimes f),\eta\otimes g\rangle
   &=\int_{\mathbb R^2}
        k(r)b_{\xi,\eta}(q-r)f(q)\overline{g(q)}\,dq\,dr\\
   &=\int_{\mathbb R}
        \langle a_k(q)\xi,\eta\rangle f(q)\overline{g(q)}\,dq\\
   &=\langle M_{a_k}(\xi\otimes f),\eta\otimes g\rangle .
 \end{aligned}
 \tag{RCC3.h}
\]
An absolute majorant for the double integral has integral at most
\(\|S\|\|\xi\|\|\eta\|\|k\|_1\|f\overline g\|_1\), which is finite by scalar Cauchy–Schwarz. Elementary tensors span a dense subspace of the entire tensor product, so
\[
 S_k=M_{a_k}.
 \tag{RCC3.i}
\]
This proves the needed multiplier-field realization after smoothing on arbitrary \(H\).

Since \(S_k\) commutes with \(\Pi(Q)\), the multiplier lemma proves
\(a_k(q)\in Q_\omega\) for every \(q\). On \([-n,n]\), choose a finite step function \(a_{k,n}\) taking values of \(a_k\) in \(Q_\omega\), with uniform error at most \(1/n\), and put it equal to zero outside that interval. Uniform continuity on the compact interval supplies the finite partition. If \(B=\|S\|\|k\|_1\), its norm is at most \(B\), and for every \(\zeta\in L^2(\mathbb R,H)\),
\[
 \|(M_{a_{k,n}}-M_{a_k})\zeta\|_2^2
 \le \frac{\|\zeta\|_2^2}{n^2}
       +B^2\int_{|q|>n}\|\zeta(q)\|^2\,dq
 \longrightarrow0.
 \tag{RCC3.j}
\]
Each \(M_{a_{k,n}}\) is a finite sum of tensors \(a_j\otimes M_{1_{E_j}}\). Strong closedness of the generated von Neumann algebra therefore gives
\[
 M_{a_k}\in Q_\omega\overline\otimes L^\infty(\mathbb R).
 \tag{RCC3.k}
\]
The finite partitions approximate one continuous field, not a countable dense set in \(H\).

Returning through \(\mathscr F\), the second tensor factor in (RCC3.k) is the algebra generated by translations, by the scalar character theorem. For \(y\in Q_\omega\), the first tensor factor \(y\otimes1\) is exactly \(\pi_\omega(y)\), since \(\sigma_{-t}(y)=y\). Consequently \(X_k\in C\).

Choose nonnegative \(k_n\in C_c^\infty(\mathbb R)\), of integral one and support in \([-1/n,1/n]\). For each normal functional \(F\) on \(B(L^2(\mathbb R,H))\), point-ultraweak continuity gives
\[
 |F(S_{k_n}-S)|
 \le \sup_{|r|\le1/n}|F(\beta_r(S))-F(S)|
 \longrightarrow0.
 \tag{RCC3.l}
\]
Thus \(X_{k_n}\to X\) ultraweakly. Since each \(X_{k_n}\in C\) and \(C\) is ultraweakly closed, \(X\in C\). It already belongs to \(C'\), so \(X\in Z(C)\).

For the converse inclusion, every regular coefficient field \(\pi_\omega(x)\) commutes with \(Q'\otimes1\), since its values belong to \(Q\), and translations commute with that constant algebra as well. The [full tensor-commutant identity](OA-FLOW-ND.md#nd-tensor) gives
\[
 (Q'\otimes1)'=Q\overline\otimes B(L^2(\mathbb R)).
 \tag{RCC3.m}
\]
Hence \(C\) is contained in this tensor algebra, and every element of \(Z(C)\) belongs to its intersection with \(C'\). This proves (RCC3.a), with both inclusions on the full Hilbert space.

<a id="rcc-strong-smoothing"></a>
### Bounded sigma-strong-star smoothing

The same approximate identity gives a stronger form of density. We prove it on the whole Hilbert space \(K=H\otimes L^2(\mathbb R)\), with no dimension or separability restriction. Write \(W_r=1\otimes L_r\). For \(Y\in B(K)\) and \(\zeta\in K\),
\[
 \begin{aligned}
 \|(\beta_r(Y)-Y)\zeta\|
 &\le \|Y\|\,\|(W_r^*-1)\zeta\|
       +\|(W_r-1)Y\zeta\|
 \longrightarrow0\qquad(r\to0).
 \end{aligned}
 \tag{RCC3.n}
\]
The same estimate for \(Y^*\) proves pointwise strong-star continuity. Strong continuity of the unitaries \(W_r\) was established above.

Use the nonnegative \(k_n\) of integral one supported in \([-1/n,1/n]\), and put \(Y_n=\int k_n(r)\beta_r(Y)\,dr\). For each \(\zeta\), the continuous compactly supported Hilbert-valued function \(r\mapsto k_n(r)(\beta_r(Y)-Y)\zeta\) has a norm integral: uniform continuity makes its Riemann sums Cauchy. Pairing that integral with every vector identifies it with the weak-star operator integral applied to \(\zeta\). Hence
\[
 \begin{gathered}
 (Y_n-Y)\zeta=\int k_n(r)(\beta_r(Y)-Y)\zeta\,dr,\\
 \|(Y_n-Y)\zeta\|
 \le\sup_{|r|\le1/n}\|(\beta_r(Y)-Y)\zeta\|
 \longrightarrow0,\qquad \|Y_n\|\le\|Y\|.
 \end{gathered}
 \tag{RCC3.o}
\]
Since \(k_n\) is real, adjointing the weak-star integral gives \(Y_n^*=\int k_n(r)\beta_r(Y^*)\,dr\). The same argument therefore proves strong convergence of the adjoints as well.

We also check every normal-functional seminorm. The sigma-strong-star topology on bounded operators is generated by
\[
 p_\varphi(A)=\varphi(A^*A)^{1/2},\qquad
 p_\varphi(A^*)=\varphi(AA^*)^{1/2},
 \qquad \varphi\in B(K)_*^+.
 \tag{RCC3.p}
\]
By the [positive vector-series theorem EP1](OA-FLOW-EP.md#oa-flow.ep.1), write
\[
 \varphi(Z)=\sum_{j=1}^{\infty}\langle Z\zeta_j,\zeta_j\rangle,
 \qquad \sum_j\|\zeta_j\|^2=\varphi(1)<\infty.
 \tag{RCC3.q}
\]
For \(A_n=Y_n-Y\), we have \(\|A_n\|\le2\|Y\|\). Consequently, for every \(J\),
\[
 \varphi(A_n^*A_n)
 \le\sum_{j=1}^{J}\|A_n\zeta_j\|^2
           +4\|Y\|^2\sum_{j>J}\|\zeta_j\|^2 .
 \tag{RCC3.r}
\]
The finite sum tends to zero by (RCC3.o); the tail can be made arbitrarily small independently of \(n\). Thus \(p_\varphi(A_n)\to0\). Apply the same estimate to \(A_n^*\) to obtain \(p_\varphi(A_n^*)\to0\). This holds for every \(\varphi\), using the single sequence \(k_n\); no countable family of seminorms or Hilbert-space basis has been selected.

Taking \(Y=S\), and conjugating by \(\mathscr F\), now gives
\[
 \begin{gathered}
 X_{k_n}\longrightarrow X\quad\text{sigma-strong-star},\qquad
 \|X_{k_n}\|\le\|X\|,\\
 X_{k_n}\in C'\cap\bigl(Q\overline\otimes B(L^2(\mathbb R))\bigr).
 \end{gathered}
 \tag{RCC3.s}
\]
Unitary conjugation preserves these seminorms by pulling a normal positive functional back along that conjugation. Each \(X_{k_n}\) is the Fourier conjugate of the norm-continuous multiplier \(a_{k_n}\) already constructed in (RCC3.f)–(RCC3.i). Thus these continuous multipliers give sigma-strong-star density within the original norm ball of the ambient relative commutant. In particular they give the sigma-strong density used in the relative-commutant argument.

<a id="rcc-4"></a>
## 4. The modular conjugation identifies the other commutant

First take the faithful normal GNS representation of an arbitrary faithful normal semifinite \(\varphi\). Denote its modular objects by \(J_\varphi,\Delta_\varphi\), and identify \(Q\) with its GNS image. [MW4](OA-FLOW-MW.md#oa-flow.mw.4) gives
\[
 \varphi\circ\sigma_t^\varphi=\varphi,\qquad
 \Lambda_\varphi(\sigma_t^\varphi(a))
        =\Delta_\varphi^{it}\Lambda_\varphi(a)
        \quad(a\in\mathfrak n_\varphi).
 \tag{RCC4.a}
\]

We need the actual modular conjugation of the dual weight on the entire regular Hilbert space. [GDW3](OA-FLOW-GDW.md#gdw-3) constructs, for a general action, the unitary
\[
 V_r\Lambda_{\psi_r}(a)
      =\Lambda_\varphi(\alpha_{-r}(a)),
 \qquad \psi_r=\varphi\circ\alpha_{-r}.
 \tag{RCC4.b}
\]
For \(\alpha=\sigma^\varphi\), (RCC4.a) makes \(\psi_r=\varphi\) on the whole positive cone and \(V_r=\Delta_\varphi^{-ir}\) on a dense finite ideal, hence on all of \(H_\varphi\). The relative closed involution is now the ordinary \(S_\varphi\); its antiunitary polar factor is \(J_\varphi\). The real group has modular function \(1\). Substituting these facts in [GDW5's full polar formula](OA-FLOW-GDW.md#gdw-5) gives
\[
 [\mathcal J_\varphi\xi](r)
       =\Delta_\varphi^{-ir}J_\varphi\xi(-r).
 \tag{RCC4.c}
\]
This is an everywhere-defined antiunitary on \(L^2(\mathbb R,H_\varphi)\). The measurability and entire graph identification are part of GDW5: its involution is the closure of the full compact graph core, with both domain inclusions proved. [GDW6](OA-FLOW-GDW.md#gdw-6) identifies this graph with the GNS involution of the complete dual weight, including its whole finite ideal. The modular commutant theorem, proved in [MF06](OA-FLOW-MF06.md#oa-flow.mf06.7) and applied to weights in [MW1](OA-FLOW-MW.md#oa-flow.mw.1), therefore implies
\[
 \mathcal J_\varphi C_\varphi(Q)\mathcal J_\varphi
       =C_\varphi(Q)'.
 \tag{RCC4.d}
\]
Thus (RCC4.c) identifies the commutant of the full generated von Neumann algebra.

The antiunitary spectral identity in [CI3](OA-FLOW-CI.md#oa-flow.ci.3) is
\[
 J_\varphi\Delta_\varphi^{it}
       =\Delta_\varphi^{it}J_\varphi .
 \tag{RCC4.e}
\]
The sign follows from \(J_\varphi\Delta_\varphi^zJ_\varphi
=\Delta_\varphi^{-\overline z}\); for \(z=it\), the exponent is \(it\). Hence \(\mathcal J_\varphi^2=I\). To compute a conjugated coefficient, use (RCC4.c) twice:
\[
 \begin{aligned}
 \bigl[\mathcal J_\varphi\pi_\varphi(x)\mathcal J_\varphi\xi\bigr](r)
 &=\Delta_\varphi^{-ir}J_\varphi
        \sigma_r^\varphi(x)\Delta_\varphi^{ir}J_\varphi\xi(r)\\
 &=\Delta_\varphi^{-ir}J_\varphi
        \Delta_\varphi^{ir}x\Delta_\varphi^{-ir}
        \Delta_\varphi^{ir}J_\varphi\xi(r)\\
 &=J_\varphi xJ_\varphi\,\xi(r).
 \end{aligned}
 \tag{RCC4.f}
\]
All modular powers here are bounded imaginary powers. The commutant theorem for \(Q\) now gives
\[
 \mathcal J_\varphi\pi_\varphi(Q)\mathcal J_\varphi
         =Q'\otimes1.
 \tag{RCC4.g}
\]

For a faithful normal **state** \(\omega\), Section 3 has proved
\[
 C_\omega(Q)'\cap
       \bigl(Q\overline\otimes B(L^2(\mathbb R))\bigr)
          =Z(C_\omega(Q)).
 \tag{RCC4.h}
\]
The GNS space is still arbitrary. Conjugation by \(\mathcal J_\omega\) preserves intersections and commutation. By (RCC4.d), (RCC4.g), and the [tensor commutant formula](OA-FLOW-ND.md#nd-tensor),
\[
 \mathcal J_\omega
       \bigl(\pi_\omega(Q)'\cap C_\omega(Q)\bigr)
       \mathcal J_\omega
  =(Q'\otimes1)'\cap C_\omega(Q)'
  =Z(C_\omega(Q)).
 \tag{RCC4.i}
\]
The same conjugation maps the center of \(C_\omega(Q)\) onto the center of its commutant. These centers are equal, both being \(C_\omega(Q)\cap C_\omega(Q)'\). Applying the involution again proves (RCC0.b) for every algebra with a faithful normal state.

<a id="rcc-5"></a>
## 5. Arbitrary state corners and a trace-scaling system

**A diagonal reference weight.** For a general \(Q\), [FR1](OA-FLOW-FR.md#oa-flow.fr.1) constructs pairwise orthogonal nonzero projections \(p_i\), indexed by an arbitrary set \(I\), and faithful normal states \(\omega_i\) on \(p_iQp_i\), such that
\[
 \sum_{i\in I}p_i=1\ \text{strongly},\qquad
 \psi(x)=\sum_{i\in I}\omega_i(p_ixp_i)
       \quad(x\in Q_+)
 \tag{RCC5.a}
\]
is faithful normal semifinite. Both sums mean limits over finite subsets. In particular \(\psi(p_i)=1\). The proof constructs the \(p_i\) as supports of normal vector states in successive orthogonal corners, uses maximality to exhaust \(1\), and proves semifiniteness from the finite compressions. It does not claim a faithful state on all of \(Q\).

For each \(i\), the symmetry \(v_i=1-2p_i\) preserves \(\psi\): in every diagonal corner of \(v_ixv_i\), its two signs cancel. This is an equality on the whole positive cone, including infinite values. The converse unitary test in [CZ0](OA-FLOW-CZ.md#oa-flow.cz.0) puts \(v_i\) in \(Q_\psi\), hence \(p_i=(1-v_i)/2\) is in \(Q_\psi\). The [centralizer-corner theorem](OA-FLOW-CZ.md#oa-flow.cz.5) gives
\[
 \sigma_t^\psi(p_i)=p_i,\qquad
 \sigma_t^{\omega_i}(a)=\sigma_t^\psi(a)
           \quad(a\in p_iQp_i).
 \tag{RCC5.b}
\]

**The entire corner core.** Work in any faithful normal representation of \(Q\), and write \(C=C_\psi(Q)\). Then
\[
 e_i=\pi_\psi(p_i)=p_i\otimes1,\qquad
 e_i\lambda_\psi(t)=\lambda_\psi(t)e_i.
 \tag{RCC5.c}
\]
The corner \(e_iCe_i\), on \(L^2(\mathbb R,p_iH)\), is the regular core of \((p_iQp_i,\omega_i)\). Here is the full algebra equality. Finite products of regular generators reduce, using covariance, to linear combinations of \(\pi_\psi(a)\lambda_\psi(t)\). Since \(e_i\) itself is a coefficient and commutes with translations,
\[
 e_i\pi_\psi(a)\lambda_\psi(t)e_i
    =\pi_\psi(p_iap_i)\lambda_\psi(t)e_i .
 \tag{RCC5.d}
\]
These are exactly the compressed regular generators and their linear combinations. Bounded strong density of the generated algebra, followed by compression, proves that every element of \(e_iCe_i\) is in their von Neumann closure. Conversely each displayed compressed generator is in \(e_iCe_i\), so equality follows. The representation of \(p_iQp_i\) on \(p_iH\) is faithful, normal and unital on that space. [NR4](OA-FLOW-NR.md#oa-flow.nr.4) therefore identifies this whole core, with normal inverse, with the core in the state GNS representation. The state theorem from Section 4 applies.

Take \(X\in\pi_\psi(Q)'\cap C\). It commutes with every \(e_i\), and \(X_i=e_iXe_i\) commutes with the coefficient algebra of the corner. Thus \(X_i\in Z(e_iCe_i)\). In particular it commutes with \(\lambda_\psi(t)e_i\), and
\[
 [X,\lambda_\psi(t)]e_i=0\quad(i\in I,t\in\mathbb R).
 \tag{RCC5.e}
\]
For a finite \(F\subset I\) let \(e_F=\sum_{i\in F}e_i\). Then \(e_F\to1\) strongly; applying the bounded operator \([X,\lambda_\psi(t)]\) to \(e_F\xi\to\xi\) proves \([X,\lambda_\psi(t)]=0\) on every vector. Together with its coefficient commutation, this makes \(X\) central in \(C\). The converse inclusion is immediate. Therefore
\[
 \pi_\psi(Q)'\cap C_\psi(Q)=Z(C_\psi(Q)).
 \tag{RCC5.f}
\]

For the originally chosen \(\varphi\), [CORE5](OA-FLOW-CORE.md#core-5) provides a coefficient-preserving normal isomorphism \(J_{\psi,\varphi}:C_\psi(Q)\to C_\varphi(Q)\) with normal inverse. Such an isomorphism transports centers and relative commutation with the named coefficients. It transports (RCC5.f) to (RCC0.b), proving the first theorem without any cardinality restriction. The \(p_i\) were fixed by the modular action, not assumed central in \(Q\).

**Transfer to a specified trace-scaling system.** Now use (RCC0.c), and set \(Q=N^\theta\), the full fixed algebra. Choose any faithful normal semifinite \(\varphi\) on \(Q\), supplied by FR1. The complete [core recognition theorem](OA-FLOW-L30.md#l30-3) gives a normal equivariant isomorphism
\[
 \kappa:C_\varphi(Q)\longrightarrow N,\qquad
 \kappa(\pi_\varphi(x))=x,\qquad
 \kappa(\lambda_\varphi(t))=H_\varphi^{it}.
 \tag{RCC5.g}
\]
Here \(H_\varphi\) is the positive density constructed in that theorem. Its spectral domains and the trace normalization have already been proved there; recognition is onto the entire \(N\). This result holds for any system satisfying (RCC0.c).

Equivariant relabeling of coefficients extends \(\kappa\) to a normal isomorphism of the second crossed products. To see normality concretely, represent \(N\) faithfully on \(K\); its regular representation for \(\theta\) is exactly the regular representation for the dual action on \(C_\varphi(Q)\) with coefficient representation \(n\mapsto\kappa(n)\). This representation is faithful and normal. NR4 compares it normally with any other faithful normal regular representation and supplies the normal inverse. Thus
\[
 C_\varphi(Q)\rtimes_{\widehat{\sigma^\varphi}}\mathbb R
       \ \cong\ N\rtimes_\theta\mathbb R=P.
 \tag{RCC5.h}
\]

Use [ND's full double-duality map](OA-FLOW-ND.md#nd-statement) on the left. Its target is \(Q\overline\otimes B(L^2(\mathbb R))\), and its copy of \(C_\varphi(Q)\) becomes the *regular* core generated by \(\pi_\varphi(Q)\) and \(\lambda_\varphi(t)\). In particular that copy is not replaced by \(Q\otimes1\). Formula (RCC4.g) and the full first theorem, now valid for this \(\varphi\), give
\[
 \begin{aligned}
 C_\varphi(Q)'\cap
     \bigl(Q\overline\otimes B(L^2(\mathbb R))\bigr)
 &=\mathcal J_\varphi
       \bigl(C_\varphi(Q)\cap\pi_\varphi(Q)'\bigr)
       \mathcal J_\varphi\\
 &=Z(C_\varphi(Q)).
 \end{aligned}
 \tag{RCC5.i}
\]
Transport this equality through (RCC5.h) and the double-duality map. The first core is precisely the distinguished \(N\), so we obtain (RCC0.d). The paired measures \(dt,ds/(2\pi)\) agree with ND. If the second regular model uses \(ds\), the scalar \(L^2\) rescaling in [L30, Section 7](OA-FLOW-L30.md#l30-7) carries the same named algebras and generators to it. This changes neither relative commutant.

<a id="rcc-factor-amplification"></a>
### A state corner and a compatible tensor decomposition

We now give a tensor reduction for **every nonzero factor**, including the identifications that carry relative commutants. Here sigma-finite means admitting a faithful normal state; by [PC7](OA-FLOW-PC.md#oa-flow.pc.7), this is equivalent to countable decomposability of the unit. It does not mean that the predual or a faithful representation is separable.

**A properly infinite state corner.** Let \(A\ne0\) be a factor on \(H\). If \(A\) is finite, [FCT8](OA-FLOW-FCT.md#oa-flow.fct.8) supplies a faithful normal tracial state \(\omega\). Then the required decomposition is \(A=A\bar\otimes\mathbb C\), and we take \(p=1\), \(A_0=A\), \(E=\mathbb C\) and \(\Phi(a\otimes\lambda)=\lambda a\). For the rest of the construction suppose that \(1_A\) is infinite. Since its only nonzero central compression is itself, it is properly infinite.

Choose a unit vector \(\xi\in H\), and let \(s\) be the projection onto \(\overline{A'\xi}\). The support argument in [FR1](OA-FLOW-FR.md#oa-flow.fr.1) proves that \(s\in A\), \(s\xi=\xi\), and the vector state \(\omega_s\) is faithful on \(sAs\). The filling construction in [PC5](OA-FLOW-PC.md#oa-flow.pc.5) provides isometries \(w_n\in A\), \(n\ge0\), with pairwise orthogonal ranges. Put \(u_n=w_ns\), \(p_n=u_nu_n^*\), and \(p=\sum_{n\ge0}p_n\). Then \(u_n^*u_n=s\), the nonzero \(p_n\) are orthogonal, and
\[
 \omega(a)=\sum_{n=0}^{\infty}2^{-n-1}
                      \omega_s(u_n^*au_n)
       \qquad(a\in A_0:=pAp)
 \tag{RCC5.j}
\]
is a faithful normal state. Each summand before its scalar coefficient is a positive normal functional of norm one on \(pAp\); their norm-convergent sum is normal and has value one at \(p\). If \(a\ge0\) has zero value, faithfulness of \(\omega_s\) gives \(u_n^*au_n=0\), hence \(a^{1/2}p_n=0\) for every \(n\). Their strong sum is \(p\), so \(a=0\).

The strong-star sum \(\sum_{n\ge0}u_{n+1}u_n^*\) has initial projection \(p\) and final projection \(p-p_0<p\), by the [orthogonal-sum theorem PC1](OA-FLOW-PC.md#oa-flow.pc.1). Thus \(p\) is infinite. Its central support is \(1\), because \(A\) is a factor, and the [corner-center theorem PC4](OA-FLOW-PC.md#oa-flow.pc.4) gives \(Z(A_0)=\mathbb Cp\). Consequently \(p\) is properly infinite. If \(A\) is type III, finiteness of a projection is intrinsic to its corner by [CDEC2](OA-FLOW-CDEC.md#cdec-2), so \(A_0\) is type III as well.

**Filling the factor with copies of that corner.** Take a maximal orthogonal family \((q_i)_{i\in I}\) of projections in \(A\) equivalent to \(p\), initially with \(q_0=p\). Chain unions and the maximal principle give such a family. Put
\[
 r=1-\sum_{i\in I}q_i .
 \tag{RCC5.k}
\]
The sum is the strong limit over finite subsets. If \(r\ne0\), [factor comparison PC2](OA-FLOW-PC.md#oa-flow.pc.2) gives either \(r\precsim p\) or \(p\precsim r\). The second possibility would provide another copy of \(p\) orthogonal to the whole family. Maximality excludes it, so \(r\precsim p\).

The residual can be absorbed into \(q_0\). Indeed \(p\) is properly infinite by the preceding construction, and [PC5](OA-FLOW-PC.md#oa-flow.pc.5) gives
\[
 p=h_1+h_2,\qquad h_1\perp h_2,\qquad h_1\sim h_2\sim p.
 \tag{RCC5.l}
\]
Map \(p\) onto \(h_1\) and \(r\) into \(h_2\). Their initial projections \(p,r\) are orthogonal, as are their final projections, so their implementing partial isometries add to a subequivalence \(p+r\precsim p\). Inclusion gives \(p\precsim p+r\). [Mutual subequivalence PC3](OA-FLOW-PC.md#oa-flow.pc.3) therefore gives \(p+r\sim p\). Replacing \(q_0\) by \(p+r\) leaves an orthogonal family, every member equivalent to \(p\), whose sum is \(1\). When \(r=0\), no replacement is needed.

Choose \(v_i\in A\) with \(v_i^*v_i=p\) and \(v_iv_i^*=q_i\), using the family after this replacement. Then
\[
 v_i^*v_j=\delta_{ij}p,\qquad
 \sum_{i\in I}v_iv_i^*=1.
 \tag{RCC5.m}
\]
There is no restriction on the cardinality of \(I\).

**The whole tensor algebra and its normal inverse.** Let \(E=\ell^2(I)\), with basis \((e_i)\). On finite-coordinate vectors define
\[
 U:pH\otimes E\longrightarrow H,\qquad
 U\left(\sum_{i\in F}\eta_i\otimes e_i\right)
       =\sum_{i\in F}v_i\eta_i.
 \tag{RCC5.n}
\]
The squared norm of the right side is \(\sum_{i\in F}\|\eta_i\|^2\), by (RCC5.m). Thus \(U\) extends to an isometry. Its range contains every \(q_iH\), and these ranges span \(H\); the isometry is onto. Its inverse has the norm-convergent vector expansion
\[
 U^*\eta=\sum_{i\in I}v_i^*\eta\otimes e_i,\qquad
 \sum_{i\in I}\|v_i^*\eta\|^2=\|\eta\|^2.
 \tag{RCC5.o}
\]
These sums are limits over finite subsets. Each individual vector has countable coordinate support, but a common countable subset of \(I\) is not required.

Write \(E_{ij}=|e_i\rangle\langle e_j|\). Unitary conjugation gives
\[
 \begin{aligned}
 \Phi:A_0\bar\otimes B(E)&\longrightarrow A,
 &\Phi(a\otimes E_{ij})&=v_iav_j^*,\\
 \Phi^{-1}(x)&=U^*xU,
 &(\Phi^{-1}(x))_{ij}&=v_i^*xv_j.
 \end{aligned}
 \tag{RCC5.p}
\]
To check both full ranges, let \(P_F=p\otimes\sum_{i\in F}E_{ii}\) on \(pH\otimes E\). [NCF1](OA-FLOW-NCF.md#ncf-1) proves that \(P_FXP_F\to X\) strongly-star and that membership in \(A_0\bar\otimes B(E)\) is equivalent to having all entries in \(A_0\). Finite tensor matrices have images \(\sum_{i,j\in F}v_iX_{ij}v_j^*\in A\); their bounded strong limits put every \(\Phi(X)\) in \(A\). Conversely \(v_i^*xv_j\in pAp\) for every \(x\in A\), so the matrix criterion puts \(U^*xU\) in the tensor algebra. This proves surjectivity as well as injectivity. Both maps are normal: vector-series functionals pull back by the unitary \(U\) or \(U^*\), preserving their square-summable bounds. We have constructed
\[
 A\cong A_0\bar\otimes B(E),
 \qquad A_0\text{ a sigma-finite factor}.
 \tag{RCC5.q}
\]
The factor \(A_0\) is type III when \(A\) is type III. The finite case above and this infinite construction together prove the statement for every nonzero factor.

**Relative commutants and regular crossed products.** First let \(B\subseteq D\subseteq B(K)\) be unital von Neumann algebras and let \(E\ne0\) be any Hilbert space. Matrix entries give
\[
 \begin{aligned}
 (B\bar\otimes B(E))'\cap(D\bar\otimes B(E))
       &=(B'\cap D)\otimes\mathbb C1_E,\\
 Z(B\bar\otimes B(E))&=Z(B)\otimes\mathbb C1_E.
 \end{aligned}
 \tag{RCC5.r}
\]
Indeed commutation with \(1\otimes E_{ii}\) makes every off-diagonal entry zero. Commutation with \(1\otimes E_{ij}\) makes all diagonal entries equal to one \(d\in D\). The operator is then \(d\otimes1_E\), because all its entries agree with that operator; commutation with \(b\otimes1_E\) is exactly \(d\in B'\). The converse follows by direct multiplication. Taking \(D=B\) gives the center formula. Thus the relative-commutant equality \(B'\cap D=Z(B)\) holds if and only if it holds for the amplified inclusion. Compression to any one diagonal coordinate proves the reverse implication.

Let \(\alpha:\mathbb R\to\operatorname{Aut}(B)\) now be a pointwise strongly continuous normal action. NCF1 defines the normal action \(\beta_t=\alpha_t\bar\otimes\mathrm{id}\) on the tensor algebra. It is point-ultraweakly continuous: on finite-coordinate vectors its pairings are finite sums of continuous matrix-entry pairings, and finite-coordinate approximation followed by the vector-series tail bound treats every normal functional. The common bound \(\|\beta_t(X)\|=\|X\|\) controls both approximations. It is also pointwise strongly-star continuous. Indeed \(\|(\beta_t(X)-X)\zeta\|^2=\langle\beta_t(X^*X)\zeta,\zeta\rangle-2\operatorname{Re}\langle\beta_t(X)\zeta,X\zeta\rangle+\|X\zeta\|^2\to0\); apply the same formula to \(X^*\) and translate the parameter for continuity at every time. The [Hilbert tensor identification](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) gives an onto unitary
\[
 L^2(\mathbb R,K\otimes E)
       \longrightarrow L^2(\mathbb R,K)\otimes E,\qquad
 [r\mapsto f(r)\eta\otimes e]\longmapsto(f\eta)\otimes e.
 \tag{RCC5.s}
\]
The norm identity holds on finite tensors; their density proves the full assertion, including nonseparable \(K,E\). In the regular convention this unitary sends
\[
 \pi_{\alpha\otimes\mathrm{id}}(b\otimes d)
       \longmapsto\pi_\alpha(b)\otimes d,\qquad
 \lambda_{\alpha\otimes\mathrm{id}}(t)
       \longmapsto\lambda_\alpha(t)\otimes1_E.
 \tag{RCC5.t}
\]
Normal tensor extension from NCF1 makes the coefficient formula valid on the entire coefficient algebra. These images generate exactly
\[
 (B\bar\otimes B(E))\rtimes_{\alpha\otimes\mathrm{id}}\mathbb R
       \cong (B\rtimes_\alpha\mathbb R)\bar\otimes B(E).
 \tag{RCC5.u}
\]
For the range assertion, the images contain \(1\otimes B(E)\) and the generators of \((B\rtimes_\alpha\mathbb R)\otimes1\), and each image is in their generated tensor algebra. Conjugation by the displayed unitary gives normal inverse maps; [NR4](OA-FLOW-NR.md#oa-flow.nr.4) transfers them to any named faithful regular models. The isomorphism intertwines the negative-character dual actions: coefficients are fixed and both copies of the translation at \(t\) acquire \(e^{-ist}\). Agreement on the generating algebras extends everywhere by normality.

**Applying the reduction to modular cores.** For (RCC5.q), let
\[
 \Omega(X)=\sum_{i\in I}\omega(X_{ii})
          \quad(X\in(A_0\bar\otimes B(E))_+),\qquad
 \psi=\Omega\circ\Phi^{-1}.
 \tag{RCC5.v}
\]
[TW2](OA-FLOW-TW.md#tw-2) proves that this is the faithful normal semifinite tensor weight on the whole positive cone. The full Tomita-domain calculation in [TW5](OA-FLOW-TW.md#tw-5) gives \(\sigma_t^\Omega=\sigma_t^\omega\otimes\mathrm{id}\). Transport through \(\Phi\) gives \(\sigma_t^\psi=\Phi\sigma_t^\Omega\Phi^{-1}\): the map \(\Lambda_\psi(x)\mapsto\Lambda_\Omega(\Phi^{-1}(x))\) preserves the GNS inner product, is onto on a dense finite ideal, and intertwines the initial involutions and their closures. It therefore intertwines their polar data and modular implementations.

Equations (RCC5.t)–(RCC5.u) consequently identify the entire core inclusion and its dual action:
\[
 \begin{gathered}
 \bigl(\pi_\psi(A)\subseteq C_\psi(A)\bigr)
 \cong
 \bigl(\pi_\omega(A_0)\bar\otimes B(E)
                  \subseteq C_\omega(A_0)\bar\otimes B(E)\bigr),\\
 \widehat{\sigma^\psi}
       \longleftrightarrow \widehat{\sigma^\omega}\otimes\mathrm{id}.
 \end{gathered}
 \tag{RCC5.w}
\]
Section 4 proves the coefficient relative-commutant theorem for the state \(\omega\). Equation (RCC5.r) transfers it to \(\psi\). For any other faithful normal semifinite \(\varphi\) on \(A\), the coefficient-preserving, dual-equivariant normal transition in [CORE5](OA-FLOW-CORE.md#core-5) transfers it to \(\varphi\). This is a tensor reduction of the whole inclusion, with a faithful state required only on \(A_0\).

Finally return to a specified trace-scaling system \((N,\theta,\tau)\), and suppose \(M=N\rtimes_\theta\mathbb R\) is a type III factor. Put \(P=N^\theta\). [L30.7](OA-FLOW-L30.md#l30-7) identifies \(M\) normally with \(P\bar\otimes B(L^2(\mathbb R))\). Equation (RCC5.r) for centers and [CDEC2](OA-FLOW-CDEC.md#cdec-2) show that \(P\) is a type III factor. Apply (RCC5.q) to \(P\), writing
\[
 P\cong P_0\bar\otimes B(E)
 \tag{RCC5.x}
\]
with a faithful normal state \(\omega_0\) on \(P_0\). Use the transported weight \(\psi\) from (RCC5.v). The equivariant core-recognition map in [L30.3](OA-FLOW-L30.md#l30-3), followed by (RCC5.w), gives
\[
 \begin{gathered}
 (N,\theta)\cong(N_0\bar\otimes B(E),\theta^0\otimes\mathrm{id}),\\
 N_0=C_{\omega_0}(P_0),\qquad
 \theta^0=\widehat{\sigma^{\omega_0}}.
 \end{gathered}
 \tag{RCC5.y}
\]
In particular these are identifications of the named coefficient algebras and actions. The core has a faithful normal semifinite scaling trace by [CORE2](OA-FLOW-CORE.md#core-2) and [CORE4](OA-FLOW-CORE.md#core-4).

A second application of (RCC5.u) identifies the full inclusion
\[
 (N\subseteq M)\cong
       (N_0\bar\otimes B(E)\subseteq M_0\bar\otimes B(E)),
 \qquad M_0=N_0\rtimes_{\theta^0}\mathbb R.
 \tag{RCC5.z}
\]
The Haar normalization in the second crossing is the one in L30.7; its explicit scalar unitary covers either \(ds/(2\pi)\) or \(ds\). Double duality identifies \(M_0\) with \(P_0\bar\otimes B(L^2(\mathbb R))\). It is a type III factor by the same center and corner arguments. It is also sigma-finite. With the countable orthonormal basis \((k_n)_{n\ge0}\) constructed in [CDEC1](OA-FLOW-CDEC.md#cdec-1), the formula
\[
 \rho(X)=\sum_{n=0}^{\infty}2^{-n-1}\omega_0(X_{nn})
       \qquad(X\ge0)
 \tag{RCC5.aa}
\]
defines a normal state: the positive normal summands have summable norms and total value one at the identity. If its value on \(X\ge0\) is zero, all \(X_{nn}\) vanish by faithfulness of \(\omega_0\); then \(X^{1/2}\) vanishes on every coordinate vector, so \(X=0\). Thus \(\rho\) is faithful.

Equation (RCC5.r) now proves that \(N'\cap M=Z(N)\) is equivalent to \(N_0'\cap M_0=Z(N_0)\). This establishes both descent and ascent through the sigma-finite factor reduction. The argument preserves the system's action and inclusion; it does not require the originally specified trace \(\tau\) to have a chosen product normalization.

<a id="rcc-tensor-density"></a>
### The specified dual weight in tensor coordinates

We determine the weight as well as the algebra in (RCC5.h). In this subsection write \(M=N\rtimes_\theta\mathbb R\), \(Q=N^\theta\), \(j_N:N\to M\), and \(u_s\) for the outer implementing group. The trace \(\tau\) is the specified trace in (RCC0.c). The modular crossing uses \(dt\), the outer crossing uses \(ds/(2\pi)\), and \(\widetilde\tau\) denotes the actual dual weight of \(\tau\) with these conventions. Let \(\omega\) be any faithful normal semifinite weight on \(Q\). No state or factor hypothesis is needed until the last paragraph.

Put \(K=L^2(\mathbb R,dr)\). Write
\[
 [L_t f](r)=f(r-t),\qquad [R_t f](r)=f(r+t),\qquad
 [Q_s f](r)=e^{-isr}f(r).
 \tag{RCC5.ab}
\]
The \(Q_s\) in this notation are scalar character operators, whereas \(Q\) is the fixed algebra. The Fourier transform (RCC0.e) is unitary by [FF3](OA-FLOW-FF.md#oa-flow.ff.3). Substitution in its integral on compact smooth functions gives
\(\mathcal F R_t\mathcal F^*=M_{e^{itq}}\); density extends this equality to every vector. Define
\[
 \begin{gathered}
 h=\mathcal F^*M_{e^q}\mathcal F,\qquad
 D(h)=\{f\in K:e^q\mathcal Ff(q)\in L^2(dq)\},\\
 D(h^{-1})=\{f\in K:e^{-q}\mathcal Ff(q)\in L^2(dq)\},
 \qquad h^{it}=R_t=L_{-t}.
 \end{gathered}
 \tag{RCC5.ac}
\]
Multiplication by \(e^q\), on this maximal domain, is positive and self-adjoint: its adjoint domain is obtained by testing against functions supported in bounded intervals, where the multiplier is bounded, and then increasing those intervals. The same argument applies to \(e^{-q}\). Functions with bounded frequency support give dense domains; \(e^q>0\) almost everywhere gives a zero kernel. Thus \(h\) is nonsingular. The multiplication spectral projections \(M_{1_{\{e^q\in B\}}}\), transported by \(\mathcal F\), give its spectral calculus and the imaginary-power formula in (RCC5.ac). In particular \(D(h^{1/2})=\{f:e^{q/2}\mathcal Ff\in L^2\}\). All these operators are affiliated with \(B(K)\).

**The whole positive-cone tensor weight.** Let \(\Omega_\omega=\omega\otimes\operatorname{Tr}_K\), with the usual trace assigning value one to a rank-one projection. [TW2](OA-FLOW-TW.md#tw-2) constructs this weight on the entire positive cone, and [TW5](OA-FLOW-TW.md#tw-5) proves
\(\sigma_t^{\Omega_\omega}=\sigma_t^\omega\otimes\mathrm{id}\).
Every spectral projection of \(1\otimes h\) therefore belongs to its centralizer. The spectral construction in [CZ2](OA-FLOW-CZ.md#oa-flow.cz.2) defines the faithful normal semifinite weight
\[
 \begin{aligned}
 \Psi_\omega&=(\Omega_\omega)_{1\otimes h},\\
 \Psi_\omega(X)
   &=\sup_{n\ge1}\Omega_\omega\bigl(
       (1\otimes k_n^{1/2})X(1\otimes k_n^{1/2})\bigr),
       &&X\in(Q\bar\otimes B(K))_+,\\
 k_n&=h\,1_{[1/n,n]}(h).
 \end{aligned}
 \tag{RCC5.ad}
\]
The centralizer perturbation theorem proves that the scalar values in this supremum increase, including when the limit is infinite; it does not require the sandwiched operators themselves to increase. This formula specifies every positive value. On elementary positives it gives
\[
 \Psi_\omega(a\otimes b)
       =\omega(a)\operatorname{Tr}_h(b),\qquad
 \operatorname{Tr}_h(b)
       :=\sup_n\operatorname{Tr}(k_n^{1/2}bk_n^{1/2}),
       \quad a,b\ge0.
 \tag{RCC5.ae}
\]
Indeed TW's diagonal-sum formula gives this product for each cutoff. Increasing \(n\) gives the displayed equality, with the convention \(0\cdot\infty=0\). The functional \(\operatorname{Tr}_h\) is itself the centralizer perturbation of the usual trace and is faithful normal semifinite. We use
\(\omega\otimes\operatorname{Tr}(h\,\cdot)\) for the full weight (RCC5.ad), not merely for its values on elementary tensors. [CZ5–6](OA-FLOW-CZ.md#oa-flow.cz.5) give its modular group and its normalized derivative:
\[
 \begin{gathered}
 \sigma_t^{\Psi_\omega}
       =\sigma_t^\omega\otimes\operatorname{Ad}R_t,\qquad
 (D\Psi_\omega:D\Omega_\omega)_t=1\otimes R_t.
 \end{gathered}
 \tag{RCC5.af}
\]

**Identification with the specified dual weight.** The map in [L30.7](OA-FLOW-L30.md#l30-7) is a normal isomorphism with normal inverse
\[
 \mathscr S_\omega:M\longrightarrow Q\bar\otimes B(K).
 \tag{RCC5.ag}
\]
If \(H_\omega\) is the density in the trace-preserving core recognition theorem, its generator values are
\[
 \begin{aligned}
 [\mathscr S_\omega(j_N(x))\xi](r)
      &=\sigma_{-r}^\omega(x)\xi(r)=:[A_x^\omega\xi](r),
          &&x\in Q,\\
 \mathscr S_\omega(j_N(H_\omega^{it}))&=1\otimes L_t,\\
 \mathscr S_\omega(u_s)&=1\otimes Q_s.
 \end{aligned}
 \tag{RCC5.ah}
\]
These formulas identify the entire map by generation. In particular,
\(\mathscr S_\omega(j_N(N))=\{A_x^\omega,1\otimes L_t:x\in Q,t\in\mathbb R\}''\).
Its coefficient algebra is represented by the modular orbit fields.

We prove the exact weight identity
\[
 \boxed{\quad
 \widetilde\tau\circ\mathscr S_\omega^{-1}
       =(\omega\otimes\operatorname{Tr})_{1\otimes h}
       =\omega\otimes\operatorname{Tr}(h\,\cdot)
       \quad}
 \tag{RCC5.ai}
\]
on the entire positive cone. Write \(C=C_\omega(Q)\), with canonical trace \(\tau_\omega\), first dual weight \(\widetilde\omega\), and core density \(d_\omega^{it}=\lambda_\omega(t)\). These are distinct from the scalar density \(h\). [CORE2](OA-FLOW-CORE.md#core-2) proves
\[
 \widetilde\omega=(\tau_\omega)_{d_\omega},\qquad
 (D\widetilde\omega:D\tau_\omega)_t=\lambda_\omega(t).
 \tag{RCC5.aj}
\]
By [L30.3–4](OA-FLOW-L30.md#l30-4), \(\kappa_\omega:C\to N\) is dual-equivariant and
\(\tau\circ\kappa_\omega=\tau_\omega\) on every positive element. Its outer-crossing extension \(\kappa_\omega^{(2)}\) is the normal map constructed in L30.7.

Here is the needed whole-cone naturality of the outer dual weight. Let \(T_C\) and \(T_N\) be the canonical operator-valued weights of the outer crossings, with values in their coefficient algebras, identified with \(C\) and \(N\). [DA's full average theorem](OA-FLOW-DA.md#da-equality) realizes both as the extended average of the remaining dual action, using its Haar measure \(dt\). The map \(\kappa_\omega^{(2)}\) intertwines those remaining actions: it sends each outer \(u_s\) to the same \(u_s\), on which both actions multiply by \(e^{-its}\), and relabels their fixed coefficients through \(\kappa_\omega\). It therefore intertwines every bounded interval average. Normal positive functional tests, followed by the increasing extended-positive limit of those intervals, give
\[
 T_N\kappa_\omega^{(2)}=\widehat\kappa_\omega T_C,\qquad
 \widetilde\tau\circ\kappa_\omega^{(2)}
       =\widetilde{\tau_\omega}.
 \tag{RCC5.ak}
\]
The hat denotes the extension to the extended positive cone. The second equality follows by composing the first with \(\widehat\tau\) and using the exact trace identity. This includes infinite values.

Apply [GDA9](OA-FLOW-GDA.md#gda-9) to the two weights \(\widetilde\omega,\tau_\omega\) on \(C\), for the same outer dual action. If \(j_C\) denotes its coefficient embedding, (RCC5.aj) gives
\[
 (D\widetilde{\widetilde\omega}:D\widetilde{\tau_\omega})_t
       =j_C(\lambda_\omega(t)).
 \tag{RCC5.al}
\]
This is the normalized cocycle, including its scalar phase. Now \(\omega\) is invariant under its own modular group. The invariant-input case of [L33.6](OA-FLOW-L33.md#l33-6), for the same named double-duality map \(\mathcal D_\omega\) and paired measures \(dt,ds/(2\pi)\), consequently gives
\[
 \widetilde{\widetilde\omega}\circ\mathcal D_\omega^{-1}
       =\Omega_\omega.
 \tag{RCC5.am}
\]
Its usual trace has rank-one value one; there is no unspecified scalar factor.

Set \(\Phi_\omega=\widetilde\tau\circ\mathscr S_\omega^{-1}\). Since
\(\mathscr S_\omega=\mathcal D_\omega(\kappa_\omega^{(2)})^{-1}\),
equations (RCC5.ak)–(RCC5.am), the generator formula for \(\mathcal D_\omega\), and [BC5's normal covariance](OA-FLOW-BC.md#oa-flow.bc.5) yield
\[
 (D\Omega_\omega:D\Phi_\omega)_t=1\otimes L_t.
\]
The [BC4 adjoint identity](OA-FLOW-BC.md#oa-flow.bc.4) gives
\((D\Phi_\omega:D\Omega_\omega)_t=1\otimes R_t\).
This is the same normalized derivative as in (RCC5.af). [Fixed-reference injectivity in GDA7](OA-FLOW-GDA.md#gda-7) therefore gives \(\Phi_\omega=\Psi_\omega\) on every positive element, proving (RCC5.ai). This step determines the actual weight, beyond the modular automorphism group.

The inverse-perturbation identity proved in [CORE2](OA-FLOW-CORE.md#core-2) also gives
\[
 (\Phi_\omega)_{1\otimes h^{-1}}=\Omega_\omega.
 \tag{RCC5.an}
\]
Its hypotheses hold: the spectral projections of \(1\otimes h^{-1}\) are fixed by the group in (RCC5.af). The same complete spectral-sandwich construction includes every infinite value in (RCC5.an).

**The two scalar groups and the fixed core.** Formula (RCC5.af) fixes the orbit fields, since
\[
 \sigma_t^\omega\bigl(\sigma_{-(r+t)}^\omega(x)\bigr)
       =\sigma_{-r}^\omega(x).
 \tag{RCC5.ao}
\]
It fixes \(1\otimes L_a\), since translations commute, and sends the outer character operator to
\[
 (1\otimes R_t)(1\otimes Q_s)(1\otimes R_t)^*
       =e^{-its}(1\otimes Q_s).
 \tag{RCC5.ap}
\]
Thus its restriction to the distinguished \(N\) is trivial and its action on the outer implementer has exactly the trace-scaling phase. Equivalently, it is the transported remaining dual action of L30.7. The positive density satisfies \(h^{it}=R_t\); the canonical outer implementer \(u_s\) has image \(1\otimes Q_s\). These are the two explicitly different groups in this model.

**Choosing a faithful state.** If \(Q\) is sigma-finite, choose a faithful normal state \(\rho\) on \(Q\). Repeating the construction with \(\rho\) gives
\(\widetilde\tau\circ\mathscr S_\rho^{-1}
=(\rho\otimes\operatorname{Tr})_{1\otimes h}\),
with the same specified \(\tau\), the same scalar \(h\), and the same rank-one normalization. The change of coordinates is explicit. Put
\(c_{\omega,\rho}(t)=(D\omega:D\rho)_t\).
[L30.5](OA-FLOW-L30.md#l30-5) proves
\(H_\omega^{it}=c_{\omega,\rho}(t)H_\rho^{it}\) and
\(\kappa_\omega=\kappa_\rho J_{\omega,\rho}\), with a coefficient-preserving, dual-equivariant, trace-preserving normal chart transition \(J_{\omega,\rho}\). Hence the normal isomorphism
\(K_{\omega,\rho}=\mathscr S_\rho\mathscr S_\omega^{-1}\) has values
\[
 \begin{aligned}
 K_{\omega,\rho}(A_x^\omega)&=A_x^\rho,\\
 K_{\omega,\rho}(1\otimes L_t)
      &=A_{c_{\omega,\rho}(t)}^\rho(1\otimes L_t),\\
 K_{\omega,\rho}(1\otimes Q_s)&=1\otimes Q_s .
 \end{aligned}
 \tag{RCC5.aq}
\]
Both sides of its weight identity are the same \(\widetilde\tau\) in the corresponding coordinates, so
\(\Psi_\rho=\Psi_\omega\circ K_{\omega,\rho}^{-1}\) on the entire positive cone. The replacement by a state includes this change of coordinates. The factor reduction (RCC5.x)–(RCC5.aa) supplies the required sigma-finite fixed algebra when that reduction is needed; if \(M\) itself has a faithful normal state, its transport to \(Q\bar\otimes B(K)\) restricts to one on \(Q\otimes1\). Thus the state choice is available in the sigma-finite factor case without a separable-predual assumption.

<a id="rcc-6"></a>
## 6. Recovering coefficient-fixing automorphisms

Keep the specified trace-scaling system and \(P=N\rtimes_\theta\mathbb R\). Write \(Z=Z(N)\). A **central continuous cocycle** is a strongly continuous map \(c:\mathbb R\to\mathcal U(Z)\) satisfying
\[
 c(s+t)=c(s)\theta_s(c(t)).
 \tag{RCC6.a}
\]
Its value at zero is \(1\), by taking \(s=t=0\) and cancelling the unitary. Pointwise multiplication makes these cocycles an abelian group \(Z^1_\theta\): centrality permits the two factors to be reordered in the cocycle equation; pointwise adjoints give inverses. For \(v\in\mathcal U(Z)\), put
\[
 (\partial v)(s)=v\theta_s(v^*),\qquad
 B^1_\theta=\{\partial v:v\in\mathcal U(Z)\},\qquad
 H^1_\theta=Z^1_\theta/B^1_\theta.
 \tag{RCC6.b}
\]
The automorphisms \(\theta_s\) preserve \(Z\). Direct multiplication proves that \(\partial v\) is a cocycle and that \(\partial(vw)=(\partial v)(\partial w)\). Hence \(B^1_\theta\) is a subgroup, and the quotient is defined.

**The full normal automorphism.** In the regular representation on \(L^2(\mathbb R,K)\), let
\[
 [D_c\xi](r)=c(-r)^*\xi(r),\qquad
 [D_c^*\xi](r)=c(-r)\xi(r).
 \tag{RCC6.c}
\]
Here \(N\) acts faithfully and normally on the arbitrary Hilbert space \(K\). Each fixed-vector orbit of either unitary field is continuous. On a compact interval it is a norm-continuous Hilbert-valued map, so step approximations make it strongly measurable. Apply this first to compactly supported elementary sections, then approximate an arbitrary strongly measurable \(L^2\) section in norm. Pointwise norm preservation and the same estimate for the inverse give inverse isometries on the full space. This is also the complete construction in [NR5](OA-FLOW-NR.md#oa-flow.nr.5); no common null set over all vectors is needed.

The field \(D_c\) commutes with every coefficient \(i(x)\), since \(c(-r)\) is central and \([i(x)\xi](r)=\theta_{-r}(x)\xi(r)\). The ordered cocycle identity gives
\[
 c(-r)^*c(s-r)=\theta_{-r}(c(s)).
 \tag{RCC6.d}
\]
Consequently, on every section,
\[
 D_c i(x)D_c^*=i(x),\qquad
 D_c u_sD_c^*=i(c(s))u_s.
 \tag{RCC6.e}
\]
Conjugation therefore maps \(P\) into itself. Its image contains \(i(N)\) and also
\(u_s=i(c(s)^*)D_cu_sD_c^*\), so it contains all generators. Its restriction
\[
 \alpha_c=\operatorname{Ad}(D_c)|_P
 \tag{RCC6.f}
\]
is onto. Spatial conjugation and its inverse are normal, proving a normal automorphism of the entire crossed product. Centrality gives
\(D_cD_d=D_{cd}\), hence \(\alpha_c\alpha_d=\alpha_{cd}\). The generator formula also makes \(c\mapsto\alpha_c\) injective.

**Every coefficient-fixing automorphism arises this way.** Suppose \(\alpha\in\operatorname{Aut}(P)\) fixes \(i(N)\) pointwise. Define in \(P\)
\[
 b_s=\alpha(u_s)u_s^*.
 \tag{RCC6.g}
\]
For \(x\in N\), covariance and pointwise fixation give
\[
 \begin{aligned}
 b_s i(x)b_s^*
 &=\alpha(u_s)i(\theta_{-s}(x))\alpha(u_s)^*\\
 &=\alpha\bigl(u_si(\theta_{-s}(x))u_s^*\bigr)
 =i(x).
 \end{aligned}
 \tag{RCC6.h}
\]
Thus \(b_s\) is a unitary in \(i(N)'\cap P=i(Z)\), by (RCC0.d). Write \(b_s=i(c(s))\). Multiplying \(\alpha(u_su_t)\) and using \(u_si(z)u_s^*=i(\theta_s(z))\) gives exactly (RCC6.a).

The map \(s\mapsto c(s)\) is strongly continuous. Indeed the original translations are strongly continuous unitary fields. A normal isomorphism preserves strong-star convergence on bounded sets, by the positive-functional and vector-series proof in [ST2](OA-FLOW-ST12.md#oa-flow.st.2). Apply this to \(\alpha\), multiply the two unitary fields in (RCC6.g), and then apply the normal inverse of \(i:N\to i(N)\). These steps give continuity in any faithful normal representation of \(N\). Therefore \(c\in Z^1_\theta\). The two normal automorphisms \(\alpha,\alpha_c\) agree on coefficients and translations, and hence on the full generated algebra. We have proved a group isomorphism
\[
 Z^1_\theta
 \ \cong\
 \{\alpha\in\operatorname{Aut}(P):\alpha|_{i(N)}=\mathrm{id}\}.
 \tag{RCC6.i}
\]
This statement specifies the groups, without assigning an additional topology to the cocycle quotient.

**Exactly the central coboundaries give inner automorphisms.** If
\(\alpha_c=\operatorname{Ad}(w)\) with \(w\in\mathcal U(P)\), its coefficient fixation forces \(w\in i(N)'\cap P=i(Z)\). Write \(w=i(v)\), \(v\in\mathcal U(Z)\). On translations,
\[
 \operatorname{Ad}(i(v))(u_s)
    =i(v\theta_s(v^*))u_s.
 \tag{RCC6.j}
\]
Comparison with (RCC6.e) gives \(c=\partial v\). Conversely this equation proves \(\alpha_{\partial v}=\operatorname{Ad}(i(v))\), since both maps agree on all generators.

The inner automorphisms form a normal subgroup: for any \(\beta\in\operatorname{Aut}(P)\),
\(\beta\operatorname{Ad}(w)\beta^{-1}=\operatorname{Ad}(\beta(w))\).
Thus \(\operatorname{Out}(P)=\operatorname{Aut}(P)/\operatorname{Inn}(P)\) is a group. The homomorphism \(c\mapsto[\alpha_c]\) has kernel precisely \(B^1_\theta\), so it induces the injection
\[
 H^1_\theta(\mathbb R,\mathcal U(Z(N)))
       \hookrightarrow\operatorname{Out}(P),
       \qquad[c]\longmapsto[\alpha_c].
 \tag{RCC6.k}
\]
Its image is exactly the outer classes with a representative fixing \(i(N)\) pointwise: the construction supplies such representatives, and (RCC6.i) recovers a cocycle from every one. This characterizes the image for the whole arbitrary-algebra trace-scaling system.

<a id="rcc-7"></a>
## 7. Concrete commutants, finite-corner nets and central phases

These models retain the specified coefficient algebra inside its crossed product. Changing that ambient algebra changes the commutant. We use the negative Fourier transform
\[
 (\mathcal F f)(q)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-irq}f(r)\,dr,
 \qquad (T_tf)(r)=f(r-t).
 \tag{RCC7.a}
\]
The full scalar unitary and its inverse are proved in [FF2](OA-FLOW-FF.md#oa-flow.ff.3). Thus \(\mathcal F T_t\mathcal F^*=M_{e^{-itq}}\). Tensoring this unitary with an identity is onto on any Hilbert tensor product: finite sums of elementary tensors are dense on both sides. The faithful normal defining representations used below give the same regular crossed products, with the same specified generators, by [NR4](OA-FLOW-NR.md#oa-flow.nr.4).

**A trace factor can have a large core center.** Let \(K\ne0\) be any Hilbert space and \(Q=B(K)\). For an orthonormal basis \((e_i)_{i\in I}\), put
\[
 \operatorname{Tr}(a)=\sup_{F\subset I,\ F\ {\rm finite}}
       \sum_{i\in F}\langle ae_i,e_i\rangle,\qquad a\in Q_+.
 \tag{RCC7.b}
\]
The proof of the trace in [MIV6](OA-FLOW-MIV.md#miv-6) applies to this arbitrary basis: normality follows by interchanging increasing suprema, faithfulness by testing \(a^{1/2}e_i\), and the trace identity by interchanging the two nonnegative matrix-entry sums for \(\operatorname{Tr}(x^*x)\) and \(\operatorname{Tr}(xx^*)\). If \(p_F\) is the finite coordinate projection, then \(a^{1/2}p_Fa^{1/2}\uparrow a\), with trace at most \(|F|\|a\|\); this proves semifiniteness. The trace identity gives invariance under unitary changes of basis. No countable basis was assumed.

The full trace GNS proof [TD1](OA-FLOW-TD.md#td-1) gives \(\sigma_t^{\operatorname{Tr}}=\mathrm{id}\). In the defining representation on \(K\), the regular generators are consequently \(x\otimes I\) and \(I\otimes T_t\). After (RCC7.a), the characters generate the entire scalar multiplication algebra by [ND's multiplication and character proof](OA-FLOW-ND.md#nd-multiplication). Both generator inclusions give
\[
 C_{\operatorname{Tr}}(Q)=B(K)\,\overline\otimes\,L^\infty(\mathbb R_q),
 \qquad \pi_{\operatorname{Tr}}(Q)=B(K)\otimes I.
 \tag{RCC7.c}
\]
Here and below such equalities refer to the indicated unitary coordinates. By [the arbitrary-Hilbert-space tensor commutant proof](OA-FLOW-ND.md#nd-tensor), the commutant of \(B(K)\otimes I\) in all of \(B(K\otimes L^2(\mathbb R))\) is \(I\otimes B(L^2(\mathbb R))\). If \(I\otimes A\) also belongs to (RCC7.c), it commutes with the central algebra \(I\otimes L^\infty(\mathbb R)\). The scalar multiplication algebra is its own commutant, by ND's same proof, so \(A\) is a multiplier. Conversely every such multiplier is central in (RCC7.c). Hence
\[
 \pi_{\operatorname{Tr}}(Q)'\cap C_{\operatorname{Tr}}(Q)
 =Z(C_{\operatorname{Tr}}(Q))
 =I\otimes L^\infty(\mathbb R_q).
 \tag{RCC7.d}
\]
Even when \(Q\) is a factor, this relative commutant is not merely the scalars.

**The exact centralizing factor for a nontracial matrix weight.** Take \(Q=M_2(\mathbb C)\),
\[
 h=\begin{pmatrix}1&0\\0&4\end{pmatrix},\qquad
 \varphi(x)=\operatorname{Tr}(hx),\qquad
 \sigma_t^\varphi(x)=h^{it}xh^{-it}.
 \tag{RCC7.e}
\]
The last identity is the full weighted-trace GNS calculation in [BC6](OA-FLOW-BC.md#bc-6); it applies to any positive definite matrix density, including this one with \(\varphi(1)=5\). Work in the defining representation on \(\mathbb C^2\). On the entire space \(L^2(\mathbb R_r,\mathbb C^2)\), set
\[
 \begin{aligned}
 (\pi_\varphi(x)\xi)(r)&=h^{-ir}xh^{ir}\xi(r),&
 (\lambda(t)\xi)(r)&=\xi(r-t),\\
 (F\xi)(r)&=h^{ir}\xi(r),&
 (F^*\eta)(r)&=h^{-ir}\eta(r).
 \end{aligned}
 \tag{RCC7.f}
\]
The matrix fields defining \(F,F^*\) are norm continuous and unitary. They preserve measurability and the pointwise vector norm, and their pointwise products are the identity. Thus they are inverse unitaries on the whole \(L^2\) space. Substitution, also used in [CIM6](OA-FLOW-CIM.md#cim-6), gives
\[
 F\pi_\varphi(x)F^*=x\otimes I,\qquad
 F\lambda(t)F^*=h^{it}\otimes T_t.
 \tag{RCC7.g}
\]
These operators generate all of \(M_2\overline\otimes\{T_t:t\in\mathbb R\}''\): multiplying the second generator by \(h^{-it}\otimes I\) gives \(I\otimes T_t\), and the converse inclusion follows from the displayed formulas. Conjugation by \((I\otimes\mathcal F)F\) therefore identifies the entire core normally with \(M_2\overline\otimes L^\infty(\mathbb R_q)\), with a normal inverse.

In the original coordinates the central group is
\[
 \begin{aligned}
 z_t&=\pi_\varphi(h^{-it})\lambda(t),\\
 Fz_tF^*&=I\otimes T_t,\qquad
 (I\otimes\mathcal F)Fz_tF^*(I\otimes\mathcal F^*)
       =I\otimes M_{e^{-itq}}.
 \end{aligned}
 \tag{RCC7.h}
\]
It is a strongly continuous unitary group, and its generated algebra is the entire center by (RCC7.d) and character generation. This can also be checked against a genuinely noncommuting coefficient. With \(E_{12}\) the upper off-diagonal matrix unit,
\[
 \begin{aligned}
 (\pi_\varphi(E_{12})\xi)(r)&=4^{ir}E_{12}\xi(r),\\
 \lambda(t)\pi_\varphi(E_{12})
      &=4^{-it}\pi_\varphi(E_{12})\lambda(t),\\
 \pi_\varphi(h^{-it})\pi_\varphi(E_{12})
      &=4^{it}\pi_\varphi(E_{12})\pi_\varphi(h^{-it}).
 \end{aligned}
 \tag{RCC7.i}
\]
The two phases cancel in \(z_t\pi_\varphi(E_{12})\). The same follows for \(E_{21}\) by adjoints, and diagonal coefficients commute directly. Since the modular action fixes \(h\), \(z_t\) also commutes with every \(\lambda(s)\). At \(t_0=\pi/(2\log4)\), the phase in the second line is \(-i\): \(\lambda(t_0)\) itself is not central.

**An uncountable family really requires a net.** Let \(I\) be uncountable and let \(Q=\ell^\infty(I)\) act diagonally on \(\ell^2(I)\). Denote its singleton projections by \(p_i\). This is a von Neumann algebra: an operator commuting with every \(p_i\) is diagonal, and every bounded diagonal operator is in \(Q\), so \(Q'=Q\). Define
\[
 \psi(a)=\sum_{i\in I}a_i
 :=\sup_{F\subset I,\ F\ {\rm finite}}\sum_{i\in F}a_i,
 \qquad a\in Q_+,\qquad p_F=\sum_{i\in F}p_i.
 \tag{RCC7.j}
\]
Finite sums are normal vector functionals; interchanging their supremum with an increasing positive supremum proves normality of \(\psi\). It is faithful, additive and homogeneous by the finite-subset definition. Since \(p_Fa\uparrow a\) and \(\psi(p_Fa)\le |F|\|a\|\), it is semifinite. Commutativity gives the trace identity. Its full GNS space is \(\ell^2(I)\), with \(\Lambda_\psi(x)=x\) on the finite left ideal \(\ell^2(I)\subset\ell^\infty(I)\). TD1 gives the trivial modular action. Each corner \(p_iQp_i=\mathbb Cp_i\) has the faithful normal state \(\omega_i(cp_i)=c\). Thus this is a concrete instance of [FR1's arbitrary family of state supports](OA-FLOW-FR.md#fr-1). These particular supports are central because \(Q\) is commutative.

For completeness, the normal functionals on \(Q\) are precisely the \(\ell^1(I)\) pairings. By [CP4–6](OA-FLOW-CP.md#oa-flow.cp.4), a normal functional is a restricted vector series with \(\sum_k\|\xi_k\|_2\|\eta_k\|_2<\infty\). Cauchy–Schwarz and nonnegative finite-subset sums give
\[
 \begin{aligned}
 b_i&=\sum_k\xi_k(i)\overline{\eta_k(i)},&
 \sum_{i\in I}|b_i|
   &\le\sum_k\|\xi_k\|_2\|\eta_k\|_2,\\
 \omega(a)&=\sum_{i\in I}b_i a_i.
 \end{aligned}
 \tag{RCC7.k}
\]
The absolute bound justifies the interchange. Conversely, if \(b\in\ell^1(I)\), take \(\xi_i=\sqrt{|b_i|}\) and \(\eta_i=\overline{b_i}/\sqrt{|b_i|}\), both zero when \(b_i=0\). Then \(\omega(a)=\langle a\xi,\eta\rangle\) is normal and has these coefficients. Every \(\ell^1(I)\) family has countable support: for each positive integer \(m\), the set \(\{i:|b_i|\ge1/m\}\) is finite, and their union contains every nonzero entry. A normal state therefore vanishes on some nonzero \(p_i\); no faithful normal state exists on this \(Q\).

Nevertheless the finite-subset net satisfies
\[
 \|(1-p_F)\xi\|_2^2=\sum_{i\notin F}|\xi_i|^2\longrightarrow0
 \quad(\xi\in\ell^2(I)).
 \tag{RCC7.l}
\]
For any sequence of finite subsets \((F_n)\), choose \(i\notin\bigcup_nF_n\). Then \((1-p_{F_n})e_i=e_i\) for every \(n\). Thus a sequence cannot replace this net.

The Fourier core is the concrete tensor product \(Q\overline\otimes L^\infty(\mathbb R)\). On the Hilbert direct sum \(\bigoplus_{i\in I}L^2(\mathbb R)\), it is exactly
\[
 \mathcal D_I=
 \left\{\bigoplus_{i\in I}M_{f_i}:
      f_i\in L^\infty(\mathbb R),\
      \sup_{i\in I}\|f_i\|_\infty<\infty\right\}.
 \tag{RCC7.m}
\]
The tensor-to-sum unitary is defined on finite coordinate tensors and is onto by their density. To verify the whole-algebra assertion, \(\mathcal D_I\) is a von Neumann algebra: commuting with all coordinate projections makes an operator block diagonal, and requiring each block to commute with all scalar multipliers makes it a multiplier by ND's scalar commutant proof. Equivalently, \(\mathcal D_I\) is the commutant of the coordinate projections together with the operators having a scalar multiplier on one coordinate and zero elsewhere. The tensor generators belong to \(\mathcal D_I\). Conversely, for \(A=\bigoplus_iM_{f_i}\), the finite corners
\[
 A_F=\sum_{i\in F}p_i\otimes M_{f_i},\qquad
 \|(A-A_F)\xi\|^2
 \le \left(\sup_i\|f_i\|_\infty\right)^2
       \sum_{i\notin F}\|\xi_i\|_2^2
 \longrightarrow0
 \tag{RCC7.n}
\]
lie in the algebraic tensor product and converge strongly. This proves the reverse inclusion. These are concrete equalities of von Neumann algebras and hence preserve their normal structures; all coordinates are scalar equivalence classes, so no common choice of measurable representatives is required. Since \(\mathcal D_I\) is abelian,
\[
 \pi_\psi(Q)'\cap C_\psi(Q)=Z(C_\psi(Q))=C_\psi(Q)=\mathcal D_I.
 \tag{RCC7.o}
\]
The argument illustrates finite-corner assembly on an arbitrary index set without a measurable-field assertion on an arbitrary Hilbert space.

**Translation: a large relative commutant inside a factor.** Let
\[
 N=L^\infty(\mathbb R,e^{-q}\,dq),\qquad
 \tau(f)=\int_{\mathbb R}f(q)e^{-q}\,dq,\qquad
 (\theta_sf)(q)=f(q-s).
 \tag{RCC7.p}
\]
The weight is defined on the whole positive cone, with infinity allowed. Its restrictions to \([-n,n]\) are normal vector functionals in the faithful multiplication representation on \(L^2(\mathbb R,dq)\), at vectors \(e^{-q/2}1_{[-n,n]}\). Their increasing supremum is normal, is faithful, and is semifinite by the same interval truncations. Commutativity makes it a trace. Scalar substitution, including infinite integrals by monotone convergence, gives
\[
 \tau(\theta_sf)=e^{-s}\tau(f),\qquad f\in N_+.
 \tag{RCC7.q}
\]
The two measures have the same null sets. Thus the stated Lebesgue multiplication representation is faithful and normal; the predual description in [ND](OA-FLOW-ND.md#nd-multiplication) also verifies this directly. Translation unitaries implement \(\theta\), and are strongly continuous by the scalar \(L^2\) translation proof in [FF1](OA-FLOW-FF.md#oa-flow.ff.2). This gives the required continuous action.

On the full regular space \(L^2(\mathbb R_r\times\mathbb R_q,dr\,dq)\),
\[
 \begin{aligned}
 (\pi(f)\xi)(r,q)&=f(q+r)\xi(r,q),&
 (u_s\xi)(r,q)&=\xi(r-s,q),\\
 (W\xi)(y,z)&=\xi(y-z,z),&
 (W^*\eta)(r,q)&=\eta(q+r,q).
 \end{aligned}
 \tag{RCC7.r}
\]
The coordinate map \((r,q)\mapsto(y,z)=(r+q,q)\) has determinant one and the displayed inverse. Scalar change of variables first on nonnegative simple functions and then by monotone convergence shows that \(W\) and \(W^*\) are inverse unitaries on the entire space. A direct substitution yields
\[
 W\pi(f)W^*=M_f\otimes I,\qquad
 Wu_sW^*=L_s\otimes I,\qquad
 (L_s\eta)(y)=\eta(y-s).
 \tag{RCC7.s}
\]
Multipliers and translations generate \(B(L^2(\mathbb R_y))\) by [ND's concrete Weyl-pair proof](OA-FLOW-ND.md#nd-weyl-proof). Consequently the full crossed product is normally isomorphic to that factor:
\[
 W(N\rtimes_\theta\mathbb R)W^*
    =B(L^2(\mathbb R_y))\otimes I_{L^2(\mathbb R_z)}.
 \tag{RCC7.t}
\]
There is no omitted multiplicity. Amplification \(A\mapsto A\otimes I\) is normal by the summable vector-coefficient expansion in an orthonormal basis of the second factor; its inverse is normal by evaluating coefficients at \(\xi\otimes v,\eta\otimes v\) for one fixed unit vector \(v\). CP's vector-series description extends these tests to every normal functional. The scalar multiplication commutant now gives, with \(P=N\rtimes_\theta\mathbb R\),
\[
 \pi(N)'\cap P=\pi(N)\cong Z(N)=N,\qquad Z(P)=\mathbb C1.
 \tag{RCC7.u}
\]
In particular the first algebra in (RCC7.u) is not \(Z(P)\).

For \(b\in\mathbb R\), the norm-continuous central cocycle \(c_b(s)=e^{ibs}1\) is an exact central coboundary:
\[
 v_b(q)=e^{ibq},\qquad
 v_b\,\theta_s(v_b^*)=e^{ibs}1=c_b(s).
 \tag{RCC7.v}
\]
Indeed the product at \(q\) is \(e^{ibq}e^{-ib(q-s)}\). The inner automorphism \(\operatorname{Ad}\pi(v_b)\) fixes \(\pi(N)\) pointwise and sends \(u_s\) to \(c_b(s)u_s\). In (RCC7.s), this is the identity
\[
 M_{e^{iby}}L_sM_{e^{-iby}}=e^{ibs}L_s.
 \tag{RCC7.w}
\]
The regular spatial multiplier from [Section 6](#rcc-6) is \(D_{c_b}\xi(r,q)=e^{ibr}\xi(r,q)\). Under \(W\) it becomes \(M_{e^{iby}}\otimes M_{e^{-ibz}}\). The second factor is in the commutant of (RCC7.t), so it implements the same automorphism as \(\pi(v_b)\). This explicitly distinguishes a spatial implementer from an implementing unitary inside \(P\).

**A shear has a small limit without a zero finite iterate.** To make [Section 1's](#rcc-1) decay mechanism concrete, use the smooth bump proved in [RF1](OA-FLOW-RF.md#rf-1):
\[
 \rho(t)=
 \begin{cases}\exp[-1/(1-t^2)],&|t|<1,\\0,&|t|\ge1,\end{cases}
 \qquad g(r,q)=\rho(2r+3)\rho(q).
 \tag{RCC7.x}
\]
Thus \(g\in C_c^\infty(\mathbb R^2)\) has closed support \([-2,-1]\times[-1,1]\). For the invertible shear \(Tg(r,q)=e^rg(r,q-r)\),
\[
 \begin{aligned}
 (T^ng)(r,q)&=e^{nr}\rho(2r+3)\rho(q-nr),\\
 \operatorname{supp}(T^ng)
   &=\{(r,q):-2\le r\le-1,\ |q-nr|\le1\},\\
 (T^ng)(-3/2,-3n/2)&=e^{-2-3n/2}>0
       \qquad(n=0,1,2,\ldots).
 \end{aligned}
 \tag{RCC7.y}
\]
The support shears but does not disappear. Differentiating twice, with all derivatives of \(g\) on the right evaluated at \((r,q-nr)\), gives
\[
 \partial_r^2(T^ng)=e^{nr}
 \bigl(n^2g+2ng_r-2n^2g_q+g_{rr}-2ng_{rq}+n^2g_{qq}\bigr).
 \tag{RCC7.z}
\]
Substitute \(q'=q-nr\), whose Jacobian in these coordinates is one. On the support \(r\le-1\), so
\[
 \begin{aligned}
 \|T^ng\|_1+\|\partial_r^2(T^ng)\|_1
    &\le C_g(1+n)^2e^{-n}\longrightarrow0,\\
 C_g&=\|g\|_1+2\|g_r\|_1+2\|g_q\|_1
       +\|g_{rr}\|_1+2\|g_{rq}\|_1+\|g_{qq}\|_1.
 \end{aligned}
 \tag{RCC7.aa}
\]
Every term in \(C_g\) is finite. The elementary exponential series proves the displayed limit, for example by bounding \(e^n\) below by its fourth-degree term for \(n\ge1\). This is a bound on actual norms; a finite drawing of some supports is only an illustration of the limit argument.

![Four exact mechanisms: a decaying Fourier shear, an arbitrary-index finite-corner net, the matrix factor that centralizes the group generator, and a central translation coboundary](../assets/relative-commutants-central-cocycles/rcc-models.png)

The first panel shows the exact closed supports for \(n=0,2,4\) in (RCC7.y), each with a nonzero marked center; the decay estimate is (RCC7.aa). The second shows only four members of the directed family of finite subsets, not an exhaustion of the uncountable set; (RCC7.l) and (RCC7.n) prove the full net limits. The third records the exact \(-i\) phase at \(t_0\) and the centralizing product (RCC7.h). The fourth uses the exact translation sign and coboundary (RCC7.v)–(RCC7.w). The [reproducible drawing source](../assets/relative-commutants-central-cocycles/render.py), [coordinates and identities](../assets/relative-commutants-central-cocycles/data.json), and [SVG](../assets/relative-commutants-central-cocycles/rcc-models.svg) retain the mathematical data. Original figure and source: CC0; font terms are retained separately.

<a id="rcc-8"></a>
## 8. Six solved diagnostics

**Diagnostic A: which commutant is being computed?** For the trace-reference factor \(Q=B(K)\), compare the commutant of the coefficient algebra in all bounded operators with its relative commutant in its core. For the translation system (RCC7.p), compare \(N'\cap P\) with \(Z(P)\).

**Solution.** In Fourier coordinates the first coefficient algebra is \(B(K)\otimes I\). The arbitrary-basis matrix-unit proof in ND gives
\[
 \begin{aligned}
 (B(K)\otimes I)'&=I\otimes B(L^2(\mathbb R)),\\
 (B(K)\otimes I)'\cap
    (B(K)\overline\otimes L^\infty(\mathbb R))
       &=I\otimes L^\infty(\mathbb R).
 \end{aligned}
 \tag{RCC8.a}
\]
The second line follows from scalar maximal abelianness, not from the assertion that \(Q\) is a factor. For the translation system, (RCC7.t) instead places \(N\) as the multiplication algebra inside \(B(L^2(\mathbb R))\), with an identity multiplicity. Therefore \(N'\cap P=N\), while \(Z(P)=\mathbb C1\). The two results have different coefficient algebras and agree with the respective conclusions of [Sections 4–5](#rcc-4).

**Diagnostic B: can a sequence of state corners cover the uncountable example?** Suppose \(I\) is uncountable. Decide whether a faithful normal state on \(\ell^\infty(I)\), or a sequence of finite singleton corners increasing strongly to \(1\), can replace (RCC7.j). Explain how the core is still recovered from these corners.

**Solution.** A normal state has the form \(a\mapsto\sum_i b_i a_i\), where \(b_i\ge0\) and \(\sum_i b_i=1\), by (RCC7.k). Each set \(\{i:b_i\ge1/m\}\) is finite, so the support is countable. A singleton projection outside that support is nonzero and has state value zero. Hence the state cannot be faithful. For a sequence \((F_n)\) of finite sets, an index \(i\) outside \(\bigcup_nF_n\) gives \(\|(1-p_{F_n})e_i\|=1\) for all \(n\); strong convergence fails.

The directed set of all finite subsets avoids both errors. Given any vector \(\xi=(\xi_i)\) in the core Hilbert direct sum and \(\varepsilon>0\), a finite \(F_0\) has \(\sum_{i\notin F_0}\|\xi_i\|_2^2<\varepsilon^2\). For every \(F\supset F_0\), (RCC7.n) then gives
\[
 \|(A-A_F)\xi\|\le\|A\|\varepsilon.
 \tag{RCC8.b}
\]
Each \(A_F\) is in the finite corner, and the bound proves strong convergence of the entire net to every bounded multiplier family \(A\). It does not choose one countable family of corners for all vectors.

**Diagnostic C: is the matrix group generator central?** In (RCC7.e), evaluate the commutation phase of \(\lambda(t_0)\) with \(\pi_\varphi(E_{12})\), where \(t_0=\pi/(2\log4)\). Find a central replacement and its negative-Fourier image.

**Solution.** Since \(4^{-it_0}=-i\), (RCC7.i) gives
\[
 \lambda(t_0)\pi_\varphi(E_{12})
       =-i\,\pi_\varphi(E_{12})\lambda(t_0).
 \tag{RCC8.c}
\]
The right-hand product is nonzero: \(\pi_\varphi(E_{12})\ne0\) and \(\lambda(t_0)\) is unitary. Thus it does not commute. Left multiplication by \(\pi_\varphi(h^{-it_0})\), where \(h^{-it_0}=\operatorname{diag}(1,-i)\), contributes the reciprocal phase \(i\). Their product is one, so \(z_{t_0}=\pi_\varphi(h^{-it_0})\lambda(t_0)\) commutes with both off-diagonal coefficients and with the remaining generators. More generally (RCC7.h) sends \(z_t\) to \(I\otimes M_{e^{-itq}}\). The minus sign follows from the explicit Fourier convention and the translation \(\xi(r)\mapsto\xi(r-t)\); reversing only one of them would change the formula.

**Diagnostic D: why must the coboundary be central?** First show that \(c_b(s)=e^{ibs}1\) for the scalar translation system gives an inner automorphism fixing its coefficients. Then consider \(N_2=M_2(\mathbb C)\overline\otimes L^\infty(\mathbb R)\), with the same translation on the second factor, and
\[
 w(q)=\begin{pmatrix}e^{ibq}&0\\0&1\end{pmatrix},
 \qquad b\ne0.
 \tag{RCC8.d}
\]
Does its coboundary automatically give an automorphism that fixes \(N_2\) pointwise?

**Solution.** In the scalar system every unitary is central. Equation (RCC7.v) shows \(c_b=\partial v_b\), and covariance gives
\(\pi(v_b)u_s\pi(v_b)^*=\pi(v_b\theta_s(v_b^*))u_s=c_b(s)u_s\).
Conjugation by \(\pi(v_b)\) fixes every multiplier, as required.

For the matrix system the trace \(\tau_2(a)=\int e^{-q}\operatorname{Tr}(a(q))\,dq\) is faithful, normal and semifinite: its finite interval restrictions are finite sums of normal vector functionals, they increase to the full weight, and interval cutoffs approximate every positive element with finite weight. The matrix trace identity gives traciality and substitution gives \(\tau_2\theta_s=e^{-s}\tau_2\). Thus it is still a trace-scaling example. Direct multiplication gives
\[
 d_s=w\theta_s(w^*)=
       \begin{pmatrix}e^{ibs}&0\\0&1\end{pmatrix},\qquad
 d_sE_{12}d_s^*=e^{ibs}E_{12}.
 \tag{RCC8.e}
\]
It is a continuous unitary cocycle, but it is noncentral whenever \(bs\notin2\pi\mathbb Z\). Since \(\theta_s(E_{12})=E_{12}\), a proposed map fixing \(N_2\) and replacing \(u_s\) by \(d_su_s\) would change the covariance identity \(u_sE_{12}u_s^*=E_{12}\) into \(d_sE_{12}d_s^*=E_{12}\), which (RCC8.e) disproves. Conjugation by \(\pi(w)\) is of course an inner automorphism, but it sends the coefficient \(E_{12}\) to \(e^{ibq}E_{12}\) and does not fix the coefficient algebra pointwise. The centrality hypothesis in [Section 6](#rcc-6) is doing exactly this work.

**Diagnostic E: does the shear annihilate a test after finitely many steps?** Let \(g\) be (RCC7.x). Suppose a linear functional \(K\) on these smooth compact tests satisfies \(K(Tf)=K(f)\) and
\[
 |K(f)|\le B\bigl(\|f\|_1+\|\partial_r^2f\|_1\bigr)
 \quad(B<\infty).
 \tag{RCC8.f}
\]
Prove \(K(g)=0\), and decide whether the same conclusion follows by declaring a sufficiently high iterate \(T^ng\) to be zero. Which direction is appropriate on positive \(r\)-support?

**Solution.** Every finite iterate is nonzero, since its value at \((-3/2,-3n/2)\) is the positive number in (RCC7.y). Instead use invariance and the derivative estimate:
\[
 |K(g)|=|K(T^ng)|
       \le BC_g(1+n)^2e^{-n}\longrightarrow0.
 \tag{RCC8.g}
\]
The left side is independent of \(n\), so it is zero. This is a limiting argument, not a finite support cancellation.

For an explicit positive-support test take \(g_+(r,q)=g(-r,q)\), supported on \(1\le r\le2\). Then
\[
 \begin{aligned}
 (T^ng_+)(3/2,3n/2)&=e^{-2+3n/2},\\
 (T^{-n}g_+)(r,q)&=e^{-nr}g_+(r,q+nr).
 \end{aligned}
 \tag{RCC8.h}
\]
Forward iteration has a growing marked value. Inverse iteration has the same derivative estimate as (RCC7.aa), with \(g_+\) and \(e^{-nr}\le e^{-n}\). Since \(T^{-1}f(r,q)=e^{-r}f(r,q+r)\) is again a smooth compact test, the assumed invariance applied to \(T^{-1}f\) also gives \(K(T^{-1}f)=K(f)\). Thus inverse iteration proves \(K(g_+)=0\). Negative support uses positive iterates; positive support uses negative iterates. Neither statement turns a finite nonzero test into zero.

<a id="rcc-fixed-tensor"></a>
**Diagnostic F: what does the fixed-tensor argument actually prove?** Realize a faithful normal semifinite \(\varphi\) on \(M\) in standard form, with modular implementers \(U_t=\Delta_\varphi^{it}\), and write
\[
 (\rho_t\xi)(r)=\xi(r+t),\qquad
 C=M\rtimes_{\sigma^\varphi}\mathbb R.
\]
Identify \(C\) inside \(M\overline\otimes B(L^2\mathbb R)\). Then suppose a specified continuous decomposition
\(M=N\rtimes_\beta\mathbb R\) makes \(\varphi\) its dual trace weight. Determine the inclusion needed to prove \(\pi_\varphi(M)'\cap C=Z(C)\), and decide whether it makes \(Z(C)\) the constant copy \(Z(N)\otimes1\).

**Solution.** The full regular commutant theorem [CCM7](OA-FLOW-CCM.md#ccm-7) gives
\[
 C'=\{M'\otimes1,\ U_t\otimes\rho_t:t\in\mathbb R\}''.
\]
Taking its commutant, using the arbitrary-matrix tensor identity [TW1](OA-FLOW-TW.md#tw-1), proves the equality of entire represented algebras
\[
 C=
 \bigl(M\overline\otimes B(L^2\mathbb R)\bigr)^{
          \sigma^\varphi\otimes\operatorname{Ad}\rho}.
 \tag{RCC8.i}
\]
Both inclusions follow from the displayed commutant theorem. Merely checking that the regular generators are fixed would prove only one inclusion. In these coordinates
\[
 [\pi_\varphi(x)\xi](r)=\sigma_{-r}^\varphi(x)\xi(r),
 \qquad \lambda_\varphi(t)=1\otimes\rho_{-t}.
 \tag{RCC8.j}
\]
The minus sign is required by our translation convention. The family
\(\rho(\mathbb R)\) is nevertheless the same as
\(\{\lambda_\varphi(t):t\in\mathbb R\}\) on the scalar factor.
This fixed-tensor realization required no dominant weight.

For the additional decomposition, the given trace satisfies
\(\tau\beta_s=e^{-s}\tau\). The dual-weight modular formula
[L18.1](OA-FLOW-L18.md#l18-1) gives \(M_\varphi=N\);
the distinguished-coefficient theorem (RCC0.d), proved in
[Section 5](#rcc-5), gives \(N'\cap M=Z(N)\).
Thus \(\pi_\varphi(n)=n\otimes1\) for \(n\in N\).
If \(T\in\pi_\varphi(M)'\cap C\), its scalar matrix entries lie in
\(M\) and commute with \(N\), so lie in \(Z(N)\). Finite matrix
compressions converge strongly to \(T\) with a common norm bound,
proving \(T\in Z(N)\overline\otimes B(L^2\mathbb R)\).
The first action in (RCC8.i) is trivial on this algebra. Fixedness
therefore implies
\[
 \begin{aligned}
 T&\in
 \bigl(Z(N)\overline\otimes B(L^2\mathbb R)\bigr)
           \cap\{1\otimes\rho_t:t\in\mathbb R\}'\\
  &=Z(N)\overline\otimes\rho(\mathbb R)' .
 \end{aligned}
 \tag{RCC8.k}
\]
For the last equality, scalar Fourier transform identifies
\(\rho(\mathbb R)'\) with the full multiplication algebra, by
[ND's scalar commutant proof](OA-FLOW-ND.md#nd-multiplication).
The normal slices and dyadic block approximation in
[CORE9](OA-FLOW-CORE.md#core-9), applied to \(Z(N)\), then recover
the entire tensor product; no common measurable operator field
on the coefficient Hilbert space is assumed.
In particular \(T\) commutes with every \(\lambda_\varphi(t)\).
It already commutes with \(\pi_\varphi(M)\), so it commutes with
the algebra these families generate. This is the sufficient
conclusion \(T\in Z(C)\).

It does not follow that \(Z(C)=Z(N)\otimes1\) in these coordinates.
Indeed, if \(z\in Z(N)\) and \(\beta_s(z)\ne z\), the coefficient
\(\pi_\varphi(z)=z\otimes1\) fails to commute with the coefficient
\(\pi_\varphi(u_s)\), since \(u_szu_s^*=\beta_s(z)\).
Such examples occur even with a properly infinite centralizer:
tensor the translation system (RCC7.p) with \(B(\ell^2)\) and its
usual trace. Reordering its regular Hilbert tensor factors gives
\[
 \bigl(L^\infty(\mathbb R)\overline\otimes B(\ell^2)\bigr)
       \rtimes_{\theta\otimes\mathrm{id}}\mathbb R
 \cong B(L^2\mathbb R)\overline\otimes B(\ell^2),
\]
normally and onto, by the generators in (RCC7.t).
The coefficient trace still scales by \(e^{-s}\); its dual
weight has this properly infinite coefficient algebra as
centralizer, by L18.1. The central coefficient
\(z=1_{[0,\infty)}\otimes1\) changes under any nonzero translation.
Consequently it is not central in the core.
The useful inclusion (RCC8.k) must retain the scalar commutant
factor and the remaining commutation with \(\pi_\varphi(M)\).

This is a conditional second proof once a continuous
decomposition is supplied. The state-corner proof in Sections
1–5 already covers every algebra without that premise.
For a finite factor, the tracial chart in [CORE9](OA-FLOW-CORE.md#core-9)
applies directly; a dominant-weight choice is unnecessary.

<a id="rcc-reading"></a>
## Further reading

M. Takesaki, *Theory of Operator Algebras II*, Chapter XII, Theorem 1.7 and Lemmas 1.8–1.9, printed pp. 370–375, develop the relative-commutant argument through KMS and Fourier analysis. Theorem 1.10(i)–(iii), printed pp. 375–377, treats the central-cocycle description of coefficient-fixing automorphisms. Lemma 6.13(i), printed pp. 449–450, concerns the relative commutant in the noncommutative flow of weights. Here the full arbitrary-algebra conclusions are obtained through state corners, a scalar decay estimate, and matrix-coefficient smoothing on arbitrary Hilbert spaces.

The [normal double-duality theorem](OA-FLOW-ND.md#nd-statement) fixes the embedded copy used in Section 5. The [core recognition theorem](OA-FLOW-L30.md#l30-3) provides its trace-scaling interpretation. [Canonical core automorphisms](OA-FLOW-CIM.md#cim-4) characterize maps preserving both the dual action and the specified trace. The explicit models and solved diagnostics above distinguish these commutants and the central-cocycle classification.
