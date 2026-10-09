# Two-weight Hilbert spaces and exact boundary traces

This selected and modified edition retains the definitions and complete multiplier/Hilbert-space proofs from Sections2–4, and the full trace proof from Section9, of AN03-U030, *Mixed symbols on every real two-parameter Sobolev scale*. Its broader mixed-symbol composition and mapping theorem is not imported: the receiving higher-order Cauchy lesson needs the precise coefficient and integer-normal tangential bounds proved in the separate half-space companion. All real two-weight indices and the trace constants are retained.

Principal author entity: AN-03 course-writing task, 2026. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. Selection and current prerequisite connections: AN-04 course-writing task and OpenAI Codex,5 October2026; publisher: AN-04 local course project.

Original text: CC0.

## Exact prerequisites and coordinates

The included [measure and L2 proofs M0–M8](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) give completeness, domination, product integration and simultaneous smooth density. The full [Fourier proofs L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) give the inversion and Plancherel conventions below, distributional compatibility and measurable multipliers. Real powers and their derivative rule are P14.2. The actual quotient-completeness proof is H1 in the companion; it uses only the Hilbert construction in Section4 below. The trace in Section9 uses that quotient proof after the whole-space Hilbert construction, so the dependency order has no cycle.

This retained text puts the normal coordinate last, \((x',x_n)\), and uses dimension \(n\). The Cauchy receiver writes \((t,x)\), with \(t=x_n\); its spatial dimension is therefore \(n-1\). The literal coordinate permutation preserves Lebesgue measure, the Fourier coefficient, \(R_0\), and all pairings. There is no rescaling. In the isolated discussion of left quantization below, \(\operatorname{Op}(a)u=(2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi\); no general mixed-symbol boundedness is inferred from the multiplier estimates.

The mathematical antecedents are the approved Hörmander III,2007 eBook ISBN978-3-540-49938-1, Lemma20.1.9 and AppendixB.2. Source citations provide credit; the used programme proofs are included here and in the companion.

## Retained definitions

Fix \(n\geq1\) and finite-dimensional complex Hermitian spaces \(E,F\). Inner products are linear in their first argument; matrix norms are the induced operator norms. Write
\[
 \xi=(\xi',\xi_n)\in\mathbb R^{n-1}\times\mathbb R,
 \quad R=1+|\xi|,\quad T=1+|\xi'|,
 \quad R_0=(1+|\xi|^2)^{1/2},\quad T_0=(1+|\xi'|^2)^{1/2}.
 \tag{MSB1}
\]
When \(n=1\), \(\xi'\) has no coordinates and \(T=T_0=1\). Set
\[
 w_{p,q}(\xi)=R_0(\xi)^pT_0(\xi')^q\qquad(p,q\in\mathbb R).
 \tag{MSB2}
\]
The Fourier convention, including its coefficient, is
\[
 \widehat u(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}u(x)\,dx,
 \qquad u(x)=(2\pi)^{-n}\int_{\mathbb R^n}e^{ix\cdot\xi}\widehat u(\xi)\,d\xi,
 \qquad D_j=-i\partial_j.
 \tag{MSB3}
\]
For a smooth \(a(x,\xi)\in\operatorname{Hom}(E,F)\), define
\[
 p_{m,m',L}(a)=
 \max_{|\alpha|+|\beta|\leq L}\sup_{x,\xi}
 \frac{\|\partial_x^\beta\partial_\xi^\alpha a(x,\xi)\|}
 {R^{m-\alpha_n}T^{m'-|\alpha'|}}.
 \tag{MSB4}
\]
The class \(S^{m,m'}\) consists exactly of those smooth symbols for which every displayed seminorm is finite. There is no restriction of \(x\) to a compact set. Matrix factors are multiplied in their given order.

For \(p,q\in\mathbb R\), define \(H_{(p,q)}(\mathbb R^n;E)\) to be the tempered distributions whose Fourier transform is represented by a locally square-integrable function and for which
\[
 \|u\|_{(p,q)}^2=(2\pi)^{-n}
    \int_{\mathbb R^n}R_0^{2p}T_0^{2q}\|\widehat u(\xi)\|_E^2\,d\xi<\infty.
 \tag{MSB5}
\]
The proof below shows directly that these are complete Hilbert spaces, that Schwartz functions are dense, and that this definition is equivalent to requiring \(w_{p,q}\widehat u\in L^2\) distributionally. The density and distributional conditions therefore do not hide an additional domain assumption.

For the reference to left quantization in Section2, its exact definition on Schwartz inputs is
\[
 \operatorname{Op}(a)u(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi.
 \tag{MSB6}
\]

## 2. Exact bracket correspondence, including negative orders

For \(r\geq0\),
\(1+r^2\leq(1+r)^2\leq2(1+r^2)\). The second difference is \((r-1)^2\). Hence \(R/R_0,T/T_0\in[1,\sqrt2]\). Put \(z_+=\max(z,0)\), \(z_-=\max(-z,0)\). For arbitrary real \(u,v\), taking positive powers or reciprocals as appropriate proves
\[
 2^{-(u_-+v_-)/2}R_0^uT_0^v
 \leq R^uT^v
 \leq2^{(u_++v_+)/2}R_0^uT_0^v.
 \tag{MSB9}
\]
For a derivative \(\alpha\), use exactly \(u=m-\alpha_n\), \(v=m'-|\alpha'|\). Dividing by these positive weights gives the two continuous identity maps between the original symbol seminorms and the bracket seminorms:
\[
 \begin{split}
 p^{R,T}_{m,m';\alpha,\beta}(a)
 &\leq2^{((m-\alpha_n)_-+(m'-|\alpha'|)_-)/2}
       p^{R_0,T_0}_{m,m';\alpha,\beta}(a),\\
 p^{R_0,T_0}_{m,m';\alpha,\beta}(a)
 &\leq2^{((m-\alpha_n)_++(m'-|\alpha'|)_+)/2}
       p^{R,T}_{m,m';\alpha,\beta}(a).
 \end{split}
 \tag{MSB10}
\]
They are identity maps on the actual smooth functions. They preserve the derivatives, base and frequency coordinates, matrix products, and left operator (MSB6); no operation is conjugated or rescaled in this correspondence.

There is an equally exact statement for Sobolev norms. On distributions whose Fourier transform has the function representative in (MSB5), define the additional norm
\[
 \|u\|_{(p,q);R,T}^2=(2\pi)^{-n}\int R^{2p}T^{2q}\|\widehat u\|^2\,d\xi.
\]
Multiplication of (MSB9), with \(u=p,v=q\), by \(\|\widehat u\|\), followed by the squared integral and square root, gives
\[
 2^{-(p_-+q_-)/2}\|u\|_{(p,q)}
 \leq\|u\|_{(p,q);R,T}
 \leq2^{(p_++q_+)/2}\|u\|_{(p,q)}.
 \tag{MSB11}
\]
Thus the two norm presentations have exactly the same vectors. The norm with the original weights does not require multiplying an arbitrary distribution by the nonsmooth function \(1+|\xi|\): it is defined on the already identified Fourier function representatives. The smooth bracket multipliers used below provide the distributional construction. When \(n=1\), all constants from \(q\), \(m'\), or tangential derivative weights in (MSB9)–(MSB11) may be omitted because the corresponding ratio is one.

## 3. Smooth multiplier symbols with finite explicit bounds

We first prove a derivative formula valid for every real exponent. In dimension \(d\geq1\), put \(h_d(\zeta)=(1+|\zeta|^2)^{1/2}\), \(z=\zeta/h_d(\zeta)\). For each multiindex \(\gamma\) and real \(p\), there is a polynomial \(P_{\gamma,p}^{(d)}(z)\) such that
\[
 \partial_\zeta^\gamma h_d(\zeta)^p
 =h_d(\zeta)^{p-|\gamma|}P_{\gamma,p}^{(d)}(\zeta/h_d(\zeta)).
 \tag{MSB12}
\]
Here is a finite, exact construction, which also supplies constants. Start with \(P_{0,p}^{(d)}=1\), and choose a fixed coordinate order for the \(|\gamma|\) differentiations, with each coordinate repeated its specified number of times. Given the polynomial after \(k\) derivatives, differentiation in coordinate \(j\) replaces it by
\[
 P\longmapsto(p-k)z_jP
       +\sum_{\ell=1}^d(\delta_{j\ell}-z_jz_\ell)\partial_{z_\ell}P.
 \tag{MSB13}
\]
Indeed \(\partial_jh_d=z_j\), and
\(\partial_jz_\ell=h_d^{-1}(\delta_{j\ell}-z_jz_\ell)\). The product and chain rules therefore prove (MSB12) at the next step, including its coefficient \(p-k\). This inductive construction works for negative, zero, and nonintegral \(p\) without alteration. Different orders of differentiation give the same value on the displayed arguments because the actual smooth mixed derivatives commute; a single fixed construction is enough for the bounds.

Let \(C^{(d)}_{p,\gamma}\) be the sum of the absolute values of all coefficients of this polynomial. Since every coordinate of \(z\) has modulus at most one,
\[
 |\partial^\gamma h_d^p|
 \leq C^{(d)}_{p,\gamma}h_d^{p-|\gamma|}.
 \tag{MSB14}
\]
For \(d=0\), define \(h_0=1\), take the sole empty multiindex, and set \(C^{(0)}_{p,0}=1\). This states exactly what happens to the tangential factor when \(n=1\).

Leibniz differentiation of \(w_{p,q}=R_0^pT_0^q\) has only terms where all normal derivatives fall on \(R_0^p\). Thus
\[
 \partial_\xi^\alpha w_{p,q}
 =\sum_{\gamma'\leq\alpha'}
    \binom{\alpha'}{\gamma'}
    (\partial_\xi^{(\gamma',\alpha_n)}R_0^p)
    (\partial_{\xi'}^{\alpha'-\gamma'}T_0^q).
 \tag{MSB15}
\]
Using (MSB14) on both factors, each term is bounded by its coefficient constant times
\[
 R_0^{p-\alpha_n-|\gamma'|}
 T_0^{q-|\alpha'|+|\gamma'|}
 =R_0^{p-\alpha_n}T_0^{q-|\alpha'|}
       (T_0/R_0)^{|\gamma'|}
 \leq R_0^{p-\alpha_n}T_0^{q-|\alpha'|}.
\]
The inequality uses \(1\leq T_0\leq R_0\) and does not depend on signs of \(p,q\). Set
\[
 K_{p,q,\alpha}=
 \sum_{\gamma'\leq\alpha'}\binom{\alpha'}{\gamma'}
 C^{(n)}_{p,(\gamma',\alpha_n)}
 C^{(n-1)}_{q,\alpha'-\gamma'},
\]
and
\[
 K_{p,q,L}^{R,T}=
 \max_{|\alpha|\leq L}
 2^{((p-\alpha_n)_-+(q-|\alpha'|)_-)/2}K_{p,q,\alpha}.
 \tag{MSB16}
\]
Equations (MSB10), (MSB15), and the vanishing base derivatives now prove
\[
 w_{p,q}I_E\in S^{p,q}(\operatorname{End}E),
 \qquad p_{p,q,L}(w_{p,q}I_E)\leq K_{p,q,L}^{R,T}.
 \tag{MSB17}
\]
The same proof holds with \(E\) replaced by \(F\), and all real orders, including \((-p,-q)\), are covered. These are explicit finite derivative constants, not merely a formal assertion that order-reducing multipliers belong to a symbol class.

Every derivative of \(w_{p,q}\) and its reciprocal grows at most polynomially. For example the bracket estimate just proved is bounded above by \(K_{p,q,\alpha}R_0^{|p|+|q|+|\alpha|}\), a deliberately nonsharp bound sufficient here. Leibniz differentiation then proves that multiplication by either function preserves Schwartz space continuously: for a fixed seminorm \(\sup_\xi|\xi^\nu\partial^\alpha(w_{p,q}v)|\), finitely many derivatives of \(v\), with finitely increased polynomial weights, bound every term. Both multipliers consequently act continuously on tempered distributions by transposition. Their pointwise product is one, so those operations are inverse maps there as well as on Schwartz space.

## 4. Hilbert spaces, exact multiplier domains, and density

Define the Fourier multiplier
\[
 J_{p,q}u=\mathcal F^{-1}(w_{p,q}\widehat u).
 \tag{MSB18}
\]
The preceding proof makes it a continuous automorphism of both \(\mathcal S\) and \(\mathcal S'\), with inverse \(J_{-p,-q}\). Products satisfy
\[
 J_{p,q}J_{r,v}=J_{p+r,q+v}\quad\hbox{on all of }\mathcal S'.
 \tag{MSB19}
\]
This identity follows from the literal product of the two smooth positive Fourier multipliers, so no unbounded-operator product on an unstated \(L^2\) domain is being taken.

If \(u\in H_{(p,q)}\), Plancherel in the convention (MSB3) gives
\[
 \|J_{p,q}u\|_{L^2}^2=(2\pi)^{-n}\int|w_{p,q}|^2\|\widehat u\|^2
                         =\|u\|_{(p,q)}^2.
 \tag{MSB20}
\]
Conversely, given \(v\in L^2\), the measurable function
\(f=w_{-p,-q}\widehat v\) is locally in \(L^2\) and defines a tempered distribution. In fact \(w_{-p,-q}\leq R_0^{|p|+|q|}\); hence, for any Schwartz function \(\psi\),
\[
 \left|\int\langle f(\xi),\psi(\xi)\rangle\,d\xi\right|
 \leq\|\widehat v\|_2\|R_0^{|p|+|q|}\psi\|_2.
 \tag{MSB21}
\]
The right side is bounded by a Schwartz seminorm: choose any integer \(M>|p|+|q|+n/2\), factor out \(\sup R_0^M\|\psi\|\), and integrate \(R_0^{-2(M-|p|-|q|)}\). That integral is finite, as follows by splitting into the unit ball and dyadic shells with volumes at most a fixed dimensional constant times \(2^{kn}\). Taking the inverse Fourier transform gives \(u=J_{-p,-q}v\in H_{(p,q)}\). Thus
\[
 J_{p,q}:H_{(p,q)}\longrightarrow L^2
 \quad\hbox{is an onto isometry with inverse }J_{-p,-q}.
 \tag{MSB22}
\]
It follows from the completeness of \(L^2\) that the normed space in (MSB5) is complete. The weighted Fourier integral with the Hermitian pairing defines its inner product and is positive definite. The same estimate (MSB21), with \(v=J_{p,q}u\), proves continuous embedding \(H_{(p,q)}\to\mathcal S'\). In particular its vector is uniquely determined by its distribution, not just by an unspecified completion class.

There is no ambiguity in the alternative distributional definition. If a tempered distribution \(u\) satisfies \(w_{p,q}\widehat u=g\in L^2\), multiplication by the smooth inverse gives \(\widehat u=w_{-p,-q}g\); this is the locally square-integrable representative just used. The weighted integral is finite. Conversely the function representative in (MSB5) immediately gives such an \(L^2\) product.

For density, use density of Schwartz functions in \(L^2\), one of the explicitly stated Fourier-analysis entry results in the included [measure companion M7](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md). If \(v_j\in\mathcal S\) tends to \(J_{p,q}u\) in \(L^2\), put \(u_j=J_{-p,-q}v_j\). The multiplier bounds prove \(u_j\in\mathcal S\), and (MSB20) proves
\[
 \|u_j-u\|_{(p,q)}=\|v_j-J_{p,q}u\|_2\longrightarrow0.
 \tag{MSB23}
\]
This proves density for every pair of real orders without assuming a nonnegative exponent. More generally, (MSB19)–(MSB20) give the full-domain isometric isomorphism
\[
 J_{a,b}:H_{(p,q)}\longrightarrow H_{(p-a,q-b)},
 \qquad\|J_{a,b}u\|_{(p-a,q-b)}=\|u\|_{(p,q)}.
 \tag{MSB24}
\]
In each case its domain is the entire displayed input space and its inverse is \(J_{-a,-b}\).

## 9. Boundary traces with the two weights retained

Later collar arguments require a trace theorem in these spaces, in addition
to operator continuity. Let \(k\geq0\) be an integer, \(s>k+1/2\), and
\(t\in\mathbb R\). For a Schwartz vector define
\(\gamma_{k,a}u=(D_n^ku)|_{x_n=a}\), where \(a\in\mathbb R\). Then

\[
 \gamma_{k,a}:H_{(s,t)}(\mathbb R^n;E)
       \longrightarrow H^{s+t-k-1/2}(\mathbb R^{n-1};E),
 \qquad
 \|\gamma_{k,a}u\|^2
       \leq \frac{c_{s,k}}{2\pi}\|u\|_{(s,t)}^2,
 \tag{MSB44}
\]

uniformly in \(a\), with the finite, positive constant

\[
 c_{s,k}=\int_{\mathbb R}\lambda^{2k}(1+\lambda^2)^{-s}\,d\lambda.
 \tag{MSB45}
\]

The target norm uses the Fourier coefficient \((2\pi)^{-(n-1)}\).
For \(n=1\), the target is \(E\), with its given norm.
The resulting \(E\)-valued boundary section depends continuously on \(a\)
in the displayed target space.

**Proof.** Write \(\xi=(\eta,\zeta)\) and
\(h=(1+|\eta|^2)^{1/2}=T_0(\eta)\). Fourier inversion in the normal
coordinate gives exactly

\[
 \widehat{\gamma_{k,a}u}(\eta)
   =(2\pi)^{-1}\int_{\mathbb R}
          e^{ia\zeta}\zeta^k\widehat u(\eta,\zeta)\,d\zeta.
 \tag{MSB46}
\]

The power \(\zeta^k\) has this sign because \(D_n=-i\partial_n\).
Cauchy--Schwarz with the original factors
\((h^2+\zeta^2)^{s/2}h^t\) yields

\[
 \begin{aligned}
 \|\widehat{\gamma_{k,a}u}(\eta)\|^2
 &\leq (2\pi)^{-2}
   \left(\int_{\mathbb R}
      \zeta^{2k}(h^2+\zeta^2)^{-s}h^{-2t}\,d\zeta\right)
   \left(\int_{\mathbb R}
      (h^2+\zeta^2)^sh^{2t}
          \|\widehat u(\eta,\zeta)\|^2\,d\zeta\right),\\
 \int_{\mathbb R}\zeta^{2k}(h^2+\zeta^2)^{-s}h^{-2t}\,d\zeta
 &=h^{2k+1-2s-2t}
   \int_{\mathbb R}\lambda^{2k}(1+\lambda^2)^{-s}\,d\lambda,
 \qquad \zeta=h\lambda,\quad d\zeta=h\,d\lambda.
 \end{aligned}
 \tag{MSB47}
\]

The last integral is finite near zero since \(k\geq0\), and on the
two real tails since \(2k-2s<-1\). Multiply the first bound by
the exact target weight \(h^{2(s+t-k-1/2)}\) and integrate with
coefficient \((2\pi)^{-(n-1)}\). The factor in the second line
cancels that target weight, and the remaining coefficient is
\((2\pi)^{-(n+1)}c_{s,k}\). Comparing it with the input coefficient
\((2\pi)^{-n}\) proves (MSB44), retaining the constant \(c_{s,k}/(2\pi)\).
When \(n=1\), \(h=1\) and the tangential integral is over the singleton
\(\mathbb R^0\) with mass one; the same calculation proves the stated case.

Schwartz density from (MSB23) extends every \(\gamma_{k,a}\) uniquely.
For a general input its Fourier representative satisfies (MSB46) for
almost every \(\eta\): (MSB47) proves absolute integrability of the
normal integral by Cauchy--Schwarz. If \(a\to b\), apply that same bound
with \(|e^{ia\zeta}-e^{ib\zeta}|^2\) in the first integral. For each
\(\eta\), dominated convergence makes that integral tend to zero;
it is bounded by four times the first integral in (MSB47).
After multiplication by the target weight, its product with the second
integral is dominated by four times \(c_{s,k}\) times the integrable
input Fourier density. A second dominated-convergence application
proves norm continuity in \(a\).

To pass to the half-space, define the restriction space with its
actual quotient norm,

\[
 \begin{aligned}
 \bar H_{(s,t)}(\mathbb R^n_+;E)
 &=\{r^+U:U\in H_{(s,t)}(\mathbb R^n;E)\},\\
 \|u\|_{\bar H_{(s,t)}}&=
    \inf_{r^+U=u}\|U\|_{(s,t)} .
 \end{aligned}
 \tag{MSB48}
\]

The kernel of \(r^+\) is closed in the whole-space Hilbert space.
Indeed, convergence in that Hilbert norm implies distributional convergence
by (MSB21), so vanishing on every test function supported in the open
half-space persists under the limit. The closed-subspace quotient theorem
in the half-space companion, H1
therefore makes (MSB48) a complete normed restriction space.

If \(r^+W=0\), then \(\gamma_{k,a}W=0\) for \(a>0\).
Here is the distributional justification. Pair (MSB46) with an arbitrary
Schwartz tangential test vector. Its continuous function of \(a\),
integrated against a compactly supported smooth normal test function,
is exactly the pairing of \(D_n^kW\) with the product test function,
by the Fourier formula and the weighted Cauchy--Schwarz bound.
If the normal test function is supported in \(a>0\), this is zero
because \(W\) vanishes on that open half-space. A continuous scalar
function giving zero against all such tests is zero there; otherwise
one small neighborhood of a nonzero value, after multiplication by
its conjugate phase, would give a nonzero integral against a
nonnegative test function. All tangential pairings therefore vanish.
Norm continuity as \(a\downarrow0\) gives \(\gamma_{k,0}W=0\).

Consequently \(\gamma_ku=\gamma_{k,0}U\) is independent of the chosen
whole-space extension \(U\), and taking the infimum in (MSB44) gives

\[
 \gamma_k:\bar H_{(s,t)}(\mathbb R^n_+;E)
        \longrightarrow H^{s+t-k-1/2}(\mathbb R^{n-1};E),
 \qquad
 \|\gamma_ku\|^2\leq\frac{c_{s,k}}{2\pi}
                      \|u\|_{\bar H_{(s,t)}}^2 .
 \tag{MSB49}
\]

For smooth inputs this is the original normal derivative at the boundary.
Restrictions of the dense whole-space Schwartz subspace are dense in
(MSB48), since each extension can be approximated before restriction.
Thus the theorem defines the same trace by density, without taking the
boundary value of an arbitrary distribution. The strict condition
\(s>k+1/2\), both real weights, the normal derivative convention, and
the full restriction domain remain part of the assertion.

