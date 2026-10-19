# Analytic directions of holomorphic boundary values

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Holomorphic extension in an imaginary direction suppresses Fourier covectors that point against that direction. A distributional boundary limit alone does not quantify this suppression. We prove the analytic estimate by combining a compact cutoff family with a finite Taylor extension of each cutoff. The cancellation leaves an integrable remainder even when the holomorphic function grows as a negative power of its imaginary height.

The result applies in every dimension, to every nonempty open convex approach cone, and to every locally uniform polynomial growth exponent. We also prove that analytic differential operators decrease analytic wavefront, and that ordinary wavefront is contained in analytic wavefront. These are separate conclusions from the boundary-existence theorem.

Basic references are Nishiwada [N] for the classical boundary-value description, and Strohmaier and Witten [S], Appendix B, for the bounded-sequence convention. The complete Fourier operations used here are [Schwartz functions and Fourier inversion][F]. The exact boundary limit and its uniform finite-test estimate are [Holomorphic boundaries in convex cones][T], Theorem 2.1 and Corollary 2.2. We reuse that distributional result and supply all the analytic estimates below.

## 1. Analytic regularity requires a controlled sequence

Use the Fourier convention
\[
 \widehat\phi(\xi)=\int e^{-ix\cdot\xi}\phi(x)\,dx,
 \qquad \langle\widehat v,\phi\rangle=\langle v,\widehat\phi\rangle .
 \tag{1}
\]
A sequence \(v_N\) is bounded with common compact support if there are a compact set \(K\), an integer \(m\geq0\), and a constant \(B\) such that every \(v_N\) is supported in \(K\) and
\[
 |v_N(\phi)|\leq B\max_{|\alpha|\leq m}\sup_K|\partial^\alpha\phi|
                   \quad(\phi\in C^\infty(\mathbb R^n)).
 \tag{2}
\]
Compact distributions act on these smooth tests by inserting any fixed cutoff equal to one near their support. Definition (2) also gives the uniform Fourier bound
\[
 |\widehat v_N(\xi)|\leq B'(1+|\xi|)^m.
 \tag{3}
\]
Indeed apply (2) to \(e^{-ix\cdot\xi}\); its derivatives are powers of \(-i\xi\).

For \(u\in\mathcal D'(X)\), \(X\subset\mathbb R^n\) open, say that \((x_0,\xi_0)\), \(\xi_0\ne0\), is absent from \(\operatorname{WF}_A(u)\) if there are a neighborhood \(U\) of \(x_0\), an open cone \(\Gamma\) containing \(\xi_0\), a sequence as in (2) with \(v_N=u\) on \(U\), and a constant \(A\) such that
\[
 |\widehat v_N(\xi)|
       \leq A^{N+1}N^N(1+|\xi|)^{-N},
            \qquad \xi\in\Gamma,\quad N\geq1 .
 \tag{4}
\]
This is the bounded-sequence definition of analytic wavefront in Euclidean coordinates. Replacing \(1+|\xi|\) by \(|\xi|\), or \(N\) by \(N+1\), gives the same condition. For \(|\xi|\geq1\), the weights differ by at most \(2^N\); \((1+1/N)^N\leq e\). For \(|\xi|\leq1\), the common bound (3) is absorbed by increasing \(A\). Thus those conventional choices do not change the set.

For ordinary wavefront, the corresponding absence condition is a single \(\chi\in C_c^\infty(X)\), equal to one near \(x_0\), and a cone \(\Gamma\) on which \(\widehat{\chi u}\) decreases faster than every inverse power. A sequence with no common finite-order bound is insufficient for (4).

Both wavefront sets are closed and conic in the nonzero cotangent space. Every absence witness works on the product of its smaller spatial neighborhood and its frequency cone; the complement is open and invariant under positive covector scaling.

**Lemma 1.1 (cutoffs with two kinds of derivative bounds).** Given a point \(x_0\) and an open neighborhood \(V\) with compact closure in \(X\), there are a smaller neighborhood \(U\), a compact \(K\subset V\), and cutoffs \(0\leq\chi_N\leq1\) supported in \(K\), equal to one on \(U\), such that for every fixed multi-index \(\beta\),
\[
 \|\partial^{\alpha+\beta}\chi_N\|_\infty
       \leq C_\beta(CN)^{|\alpha|}
                   \quad(|\alpha|\leq N).
 \tag{5}
\]
In addition, every fixed-order derivative of \(\chi_N\) is bounded independently of \(N\).

**Proof.** Choose \(U\) and a number \(d>0\) so that the closed \(4d\)-neighborhood of \(U\) lies in \(V\). Choose \(\chi_0\in C_c^\infty(V)\), between zero and one, equal to one on the closed \(d\)-neighborhood of \(U\), with support inside its open \(2d\)-neighborhood. Its support is then at distance greater than \(d\) from \(V^c\). Choose a nonnegative smooth bump \(\rho\) supported in the unit ball and normalize its positive integral to one. Let
\[
 \rho_N(x)=(N/d)^n\rho(Nx/d),\qquad
 \chi_N=\chi_0*\underbrace{\rho_N*\cdots*\rho_N}_{N\ \mathrm{factors}} .
 \tag{6}
\]
The sum of the \(N\) support radii is \(d\). Thus all supports lie in one compact subset of \(V\), and every convolution averages only values equal to one when its final argument is in \(U\). Nonnegativity and total mass one give \(0\leq\chi_N\leq1\).

For a fixed \(\beta\), put all those derivatives on \(\chi_0\). For a multi-index \(\alpha\) with total order at most \(N\), put each of its coordinate derivatives on a different convolution factor. Differentiating under the finite compact integrals gives
\[
 \partial^{\alpha+\beta}\chi_N
       =(\partial^\beta\chi_0)*(\partial_{j_1}\rho_N)*\cdots*
         (\partial_{j_{|\alpha|}}\rho_N)*
         \rho_N*\cdots*\rho_N .
 \tag{7}
\]
Each differentiated factor has \(L^1\)-norm at most
\((N/d)\max_j\|\partial_j\rho\|_1\); each remaining factor has norm one. The elementary convolution estimate
\(\|h*g\|_\infty\leq\|h\|_\infty\|g\|_1\), applied repeatedly, proves (5). For any fixed derivative order, put every derivative on \(\chi_0\) instead; the other factors have norm one. This gives the asserted uniform low-order bounds. \(\square\)

For a unit vector \(y\), the same construction gives, for fixed \(q\),
\[
 \|D_y^{N+q}\chi_N\|_\infty\leq C_q(CN)^N,
 \qquad D_y=y\cdot\nabla.
 \tag{8}
\]
Put \(q\) directional derivatives on \(\chi_0\), and one on each of the \(N\) factors. The \(L^1\)-bound for a directional derivative is at most the sum of the coordinate bounds times \(\sum|y_j|\leq\sqrt n\). This fixes the constants in (8), uniformly over unit \(y\).

## 2. Analytic coefficients preserve the directional estimate

We first record the exact multiplication calculation. If \(v\) is a compact distribution and \(g\) is compact smooth, then
\[
 \widehat{gv}(\xi)
     =(2\pi)^{-n}\int\widehat g(\xi-\eta)\widehat v(\eta)\,d\eta .
 \tag{9}
\]
For a proof, inverse Fourier transformation of \(g\) gives
\[
 g(x)e^{-ix\cdot\xi}
       =(2\pi)^{-n}\int\widehat g(\xi-\eta)e^{-ix\cdot\eta}\,d\eta .
 \tag{10}
\]
Insert a fixed cutoff in \(x\) equal to one near \(\operatorname{supp}v\). Every \(x\)-derivative of the integrand adds a polynomial in \(\eta\), while \(\widehat g\) decreases rapidly. The integral and its tails therefore converge in every compact-test seminorm, on one common support. The finite-order bound permits applying \(v\) to the integral, proving (9) and absolute convergence. Fourier inversion and the rapid estimates used here are proved in [F], Sections 2–5.

**Lemma 2.1 (analytic cutoff multipliers).** If \(a\) is real analytic on a neighborhood of the compact set \(K\) in Lemma 1.1 and \(g_L=a\chi_L\), then
\[
 |\widehat g_L(\eta)|
       \leq C(CL)^j(1+|\eta|)^{-j}
                  \quad(0\leq j\leq L),
 \qquad
 \|\widehat g_L\|_1\leq C .
 \tag{11}
\]
The last constant is independent of \(L\).

**Proof.** Real analyticity gives on \(K\) a uniform factorial derivative bound
\(\|\partial^\beta a\|_\infty\leq A B^{|\beta|}|\beta|!\).
Here is its local justification. In a power-series neighborhood, choose a polyradius \(r>0\) for which the absolute coefficient sum is finite. Each coefficient is bounded by \(M r^{-|\gamma|}\). On the half-radius polydisk, termwise differentiation and the product identity
\[
 \sum_{\ell\geq0}\binom{\ell+b}{b}2^{-\ell}=2^{b+1}
 \tag{12}
\]
give \(|\partial^\beta a|\leq M\,2^n(2/r)^{|\beta|}\beta!\).
Identity (12) follows by differentiating the convergent geometric series \(b\) times, or by multiplying \(b+1\) copies and counting the compositions of \(\ell\). The differentiated series are absolutely convergent on each smaller polydisk. A finite such cover of \(K\) gives the stated uniform bound.

For \(|\beta|\leq L\), \(|\beta|!\leq L^{|\beta|}\). Leibniz's rule and (5) with no extra derivatives thus bound every derivative of \(g_L\) of total order \(j\leq L\) by \(C(CL)^j\). The binomial sums are absorbed by replacing \(C\) with \(B+C\). Integrate by parts \(j\) times in the unit direction \(\eta/|\eta|\); compact support leaves no boundary term. The support volume and these derivative bounds give \(|\widehat g_L(\eta)|\leq C(CL)^j|\eta|^{-j}\) for \(|\eta|\geq1\), with dimension constants absorbed in \(C\). The uniform \(L^1\)-norm of \(g_L\) handles \(|\eta|\leq1\), and replacing \(|\eta|\) by \(1+|\eta|\) only costs \(2^j\).

For the last assertion, choose one fixed derivative order greater than \(n\). The uniform low-order part of Lemma 1.1, together with the fixed derivatives of \(a\) on \(K\), gives a rapid bound of that order for \(\widehat g_L\) uniformly in \(L\), by the same integration-by-parts calculation. Its integral is finite and independent of \(L\). \(\square\)

**Theorem 2.2 (analytic multiplication).** For real analytic \(a\) on \(X\),
\[
 \operatorname{WF}_A(au)\subseteq\operatorname{WF}_A(u).
 \tag{13}
\]

**Proof.** Take the sequence \(u_L\), common order \(m\), and cone \(\Gamma\) of (2)–(4) at an absent point for \(u\). Choose cutoffs of Lemma 1.1 supported inside the neighborhood where \(u_L=u\). On a smaller neighborhood they equal one. Let \(b=m+n+2\), \(L=N+b\), and set
\[
 v_N=g_Lu_L,\qquad g_L=a\chi_L .
 \tag{14}
\]
These distributions agree with \(au\) on that smaller neighborhood. Their supports are in the fixed cutoff support. Leibniz's rule and the uniform fixed-order derivatives of \(g_L\) show that they have a common finite-order bound, independently of \(N\).

Shrink to a cone \(\Gamma'\) whose spherical closure lies inside \(\Gamma\). There is \(c>0\) such that
\[
 |\xi-\eta|\geq c(|\xi|+|\eta|)
          \quad(\xi\in\Gamma',\ \eta\notin\Gamma).
 \tag{15}
\]
Otherwise normalize a contradicting sequence by \(|\xi|+|\eta|\). Compactness gives equal nonzero limiting directions, one in the closed smaller cone and one outside the larger cone, a contradiction. Zero or unequal limiting lengths cannot make the difference zero.

Use (9) and write \(r=|\xi|\). On \(\eta\in\Gamma\), \(|\eta|\geq r/2\), (4) and the uniform \(L^1\)-bound in (11) give
\[
 \left|\int_{\mathrm{this\ region}}\widehat g_L(\xi-\eta)\widehat u_L(\eta)\,d\eta\right|
       \leq C^{L+1}L^L(1+r)^{-L}.
 \tag{16}
\]
The factor \(2^L\) from \(r/2\) is included in \(C^{L+1}\).

On the complement, either (15) applies or \(|\eta|<r/2\), which itself gives \(|\xi-\eta|\geq(r+|\eta|)/3\). Use the \(j=L\) estimate in (11) and the common polynomial bound (3). The absolute integral is at most
\[
 \begin{aligned}
 C^{L+1}L^L\int(1+r+|\eta|)^{-L}(1+|\eta|)^m\,d\eta
 &\leq C^{L+1}L^L(1+r)^{m+n-L}.
 \end{aligned}
 \tag{17}
\]
For the last estimate put \(\eta=(1+r)z\). The remaining integral is bounded by \(\int(1+|z|)^{m-b}\,dz\), a fixed finite constant, since \(L\geq b\).

For \(r\geq N\), \(L=N+b\) satisfies \(L^L\leq C_b^{N+1}N^{N+b}\): expand \((1+b/N)^{N+b}\) and bound it by a constant times \(e^b\), absorbing the finitely many small \(N\). Equation (16) is therefore at most \(C^{N+1}N^N(1+r)^{-N}\). Equation (17) has the same bound with the extra factor at most \(N^{m+n}\), because \(b=m+n+2\); this fixed polynomial is absorbed in a larger \(C^{N+1}\), using \(\log N\leq N\).

For \(r<N\), the common finite-order bound on \(v_N\) gives \(C(1+r)^m\). This also satisfies (4) with a larger constant: \((1+r)\leq N+1\leq2^N\) and \(N/(1+r)\geq1/2\). Thus all frequencies in \(\Gamma'\) satisfy the required analytic estimate. This proves (13). \(\square\)

**Corollary 2.3 (analytic differential decrease and analytic functions).** If
\(P=\sum_{|\alpha|\leq q}a_\alpha(x)\partial^\alpha\) has real analytic coefficients, then
\[
 \operatorname{WF}_A(Pu)\subseteq\operatorname{WF}_A(u).
 \tag{18}
\]
Every real analytic function has empty analytic wavefront.

**Proof.** For a constant derivative \(\partial^\alpha\), of order \(j\), use \(\partial^\alpha u_{N+j}\). The sequence has a common compact support and order at most \(m+j\). Its Fourier multiplier is \((i\xi)^\alpha\). The estimate (4) at index \(N+j\) implies the estimate at index \(N\), after increasing its constant: the extra frequency factor is absorbed by the extra \(j\) decay powers, and the remaining \(N^j\) is absorbed exponentially as in Theorem 2.2. It agrees with \(\partial^\alpha u\) on the same neighborhood. Apply Theorem 2.2 to each coefficient.

For a finite sum, intersect its finitely many neighborhoods and cones. Add the finitely many regular sequences, extend their compact supports to their finite union, and take the maximum of their finite orders. Their Fourier estimates add and are absorbed by one larger constant in (4). This proves (18).

For the constant function one, take the cutoffs \(\chi_N\). The integration-by-parts calculation of Lemma 2.1 with \(a=1,j=N\) proves (4) on all nonzero frequency directions; their zeroth-order bounds are uniform. Thus \(\operatorname{WF}_A(1)\) is empty. Theorem 2.2 applied to \(a\cdot1\) gives the assertion for any analytic function \(a\). \(\square\)

If \(a\) is analytic and nowhere zero locally, its reciprocal is analytic by the convergent geometric series in a sufficiently small power-series neighborhood. Applying Theorem 2.2 twice gives equality of the analytic wavefront sets of \(au\) and \(u\) there.

## 3. Ordinary wavefront is contained in analytic wavefront

**Theorem 3.1.** For every distribution on \(X\),
\[
 \operatorname{WF}(u)\subseteq\operatorname{WF}_A(u).
 \tag{19}
\]

**Proof.** At an analytically absent point, let \(u_N\) be the sequence in (2)–(4). Choose a fixed compact smooth \(\chi\), equal to one near the point, with support inside the neighborhood where every \(u_N=u\). Thus \(\chi u_N=\chi u\) for every \(N\). Apply (9), now with the single multiplier \(\chi\).

Fix a smaller cone \(\Gamma'\) as in (15) and any desired inverse-power order \(p\). Choose one fixed index \(N>p+n\). On \(\eta\in\Gamma\), use (4) at this index and
\[
 1+|\xi|\leq(1+|\xi-\eta|)(1+|\eta|).
 \tag{20}
\]
The weighted integral in (9) is bounded by the \(L^1\)-norm of
\((1+|\zeta|)^p\widehat\chi(\zeta)\) times the finite constant
\(\sup_{\eta\in\Gamma}(1+|\eta|)^p|\widehat u_N(\eta)|\).
Both are finite. The potentially large \(A^{N+1}N^N\) is fixed for this \(p\), which is exactly what ordinary rapid decay allows.

On \(\eta\notin\Gamma\), use (15), the common polynomial bound (3), and a rapid-decay order \(\ell>p+m+n\) for \(\widehat\chi\). The absolute integral is at most
\[
 C(1+|\xi|)^{-p}
       \int(1+|\eta|)^{m-\ell+p}\,d\eta ,
 \tag{21}
\]
which is finite. To see the factorization, both \(1+|\xi|\) and \(1+|\eta|\) are bounded by a constant times \(1+|\xi-\eta|\) on this region; distributing the exponent \(\ell\) as \(p\) and \(\ell-p\) gives (21).

Thus \(\widehat{\chi u}\) decreases with every desired order on \(\Gamma'\), using the same \(\chi\). The point is ordinarily absent. Taking complements proves (19). \(\square\)

## 4. The holomorphic tube selects the positive polar

Let \(Y\subset\mathbb R^n\) be a nonempty open convex cone, invariant under every positive dilation. Its positive polar is
\[
 Y^*=\{\xi:y\cdot\xi\geq0\text{ for every }y\in Y\}.
 \tag{22}
\]
This convention determines the sign of the conclusion.

**Theorem 4.1 (analytic wavefront of a polynomially bounded tube boundary).** Let \(f\) be holomorphic in
\[
 \{x+iy:x\in X,\ y\in Y,\ |y|<h\},
 \tag{23}
\]
and suppose every slightly larger compact real neighborhood has constants \(C\), an integer \(M\geq0\), and a positive height for which
\[
 |f(x+iy)|\leq C|y|^{-M}
 \tag{24}
\]
holds uniformly for all sufficiently small nonzero \(y\in Y\). Its full cone boundary \(u\), supplied by [T], satisfies
\[
 \operatorname{WF}_A(u)\subseteq X\times(Y^*\setminus\{0\}).
 \tag{25}
\]

**Proof.** Fix \(x_0\in X\) and \(\xi_0\notin Y^*\), \(\xi_0\ne0\). By (22), choose a unit \(y\in Y\) with \(y\cdot\xi_0<0\). A conic neighborhood \(\Gamma\) of \(\xi_0\) has, after shrinking,
\[
 y\cdot\xi\leq-c|\xi|\quad(\xi\in\Gamma)
 \tag{26}
\]
for some \(c>0\). Choose the cutoff family of Lemma 1.1 on a compact real neighborhood where (24) has one exponent \(M\). Choose a fixed height \(\tau>0\) within that bound and the tube. Set \(u_N=\chi_Nu\). The common low-order cutoff bounds and the finite order of \(u\) on that compact set prove (2) for \(u_N\).

For each \(N\geq1\), put \(L=N+M-1\geq0\) and use the finite extension
\[
 E_N(x,t)=\sum_{j=0}^{L}\frac{(it)^j}{j!}D_y^j\chi_N(x),\qquad
 I_N(t,\xi)=\int f(x+ity)e^{-i(x+ity)\cdot\xi}E_N(x,t)\,dx.
 \tag{27}
\]
All real supports stay in one fixed compact subset of \(X\). For \(t>0\), holomorphy of the product \(f(z)e^{-iz\cdot\xi}\) gives \(\partial_t=iD_y\). Compact integration by parts gives the exact cancellation
\[
 I_N'(t,\xi)
   =-\frac{i(it)^L}{L!}
       \int f(x+ity)e^{-i(x+ity)\cdot\xi}D_y^{L+1}\chi_N(x)\,dx .
 \tag{28}
\]
Only the last derivative of the Taylor polynomial survives.

For fixed \(N,\xi\), the uniform finite-test bound of [T], Theorem 2.1, makes the terms with \(t^j\), \(j\geq1\), tend to zero as \(t\downarrow0\), and its boundary limit gives
\[
 I_N(0,\xi)=\widehat u_N(\xi).
 \tag{29}
\]
This step concerns a fixed finite test family and does not use the pointwise growth estimate to multiply \(t^j\) by a possibly divergent scalar integral.

Equations (24), (26), (28) and (8) bound the integrated remainder by
\[
 \begin{aligned}
 \int_0^\tau|I_N'(t,\xi)|\,dt
 &\leq
 \frac{C(CN)^N}{(N+M-1)!}
             \int_0^\tau t^{N-1}e^{-c|\xi|t}\,dt\\
 &\leq
 C(CN)^N(c|\xi|)^{-N}
          \frac{(N-1)!}{(N+M-1)!}\\
 &\leq C(C'N)^N|\xi|^{-N}.
 \end{aligned}
 \tag{30}
\]
The scalar integral over the whole positive half-line is
\((N-1)!/(c|\xi|)^N\), by substitution and \(N-1\) integrations by parts. The factorial ratio is at most one, including \(M=0\). The precise choice \(L=N+M-1\) leaves the integrable exponent \(N-1\) and exactly \(N\) derivatives assigned to the \(N\) convolution factors.

For the top face at \(\tau\), Lemma 1.1 bounds each derivative through \(L\) by \(C_M(CN)^j\): for \(j>N\), put the extra at most \(M-1\) derivatives on \(\chi_0\). Hence
\[
 |E_N(x,\tau)|\leq C_Me^{C\tau N},\qquad
 |I_N(\tau,\xi)|\leq C e^{C\tau N}e^{-c\tau|\xi|}.
 \tag{31}
\]
For \(r>0\), \(r^N e^{-c\tau r}\) is maximized at \(r=N/(c\tau)\), with value \((N/(ec\tau))^N\), as follows by differentiating its logarithm. Thus (31) is bounded by \(C(C'N)^N|\xi|^{-N}\).

Integrate (28) from zero to \(\tau\), using (29) and the integrable majorant in (30). The two bounds give (4) on \(\Gamma\) for \(|\xi|\geq1\), after replacing \(|\xi|\) by \(1+|\xi|\) and increasing its constant. For \(|\xi|\leq1\), the common finite-order bound on \(u_N\) gives (4) as explained after its definition. Therefore \((x_0,\xi_0)\) is analytically absent.

Every covector outside \(Y^*\) has such a separating direction. This proves (25). If \(0\in Y\), openness and scaling imply \(Y=\mathbb R^n\). The tube then already contains real points, and its trace is analytic, so Corollary 2.3 gives the same conclusion, with no nonzero polar covectors. \(\square\)

The proof also gives this useful extension: if a common distributional boundary \(u\) is already known and every chosen interior direction belongs to some smaller open cone on which (24) holds uniformly, apply Theorem 4.1 on each smaller cone. Their directions cover \(Y\), so the intersection of their positive polars is \(Y^*\). The same bound (25) follows. This permits growth constants that vary as the direction approaches the edge, provided the common boundary has been established separately.

## 5. The three inputs for a contour argument

For a separated holomorphic tube contribution, Theorem 4.1 gives the positive-polar analytic-wavefront bound at every polynomial growth exponent, including zero. Corollary 2.3 applies to its analytic differential operators and to the explicitly analytic interior contributions. Theorem 3.1 then passes every resulting analytic exclusion to ordinary wavefront.

These conclusions are proved here at the exact distributional boundary and Fourier inputs stated in the introduction. Noncharacteristic analytic regularity for an Euler operator, general analytic pullback/product/projection estimates, and homogeneous Fourier-wavefront interchange are further results. Differential decrease in (18) alone does not imply those converse regularity or operation theorems.

## References

[N] Kimimasa Nishiwada, *On Local Characterization of Wave Front Sets in Terms of Boundary Values of Holomorphic Functions*, Publications of the Research Institute for Mathematical Sciences **14** (1978), 309–320. [Primary article](https://www.jstage.jst.go.jp/article/kyotoms1969/14/2/14_2_309/_article/-char/en).

[S] Alexander Strohmaier and Edward Witten, *Analytic States in Quantum Field Theory on Curved Spacetimes*, Annales Henri Poincaré **25** (2024), 4543–4590, Appendix B. [Open-access primary article](https://link.springer.com/article/10.1007/s00023-024-01419-0). Its bounded-sequence convention is named for comparison; the arguments used here are supplied above. The article retains its CC BY 4.0 terms.

[F] [Schwartz functions and Fourier inversion][F], Sections 1–5.

[T] [Holomorphic boundaries in convex cones][T], Theorem 2.1, formula (2.9), and Corollary 2.2.

Original exposition is CC0. The linked internal proofs retain their provenance and stated CC0 notices; external article prose and figures are not reproduced.

[F]: https://github.com/KokunoYumeto/open-math-courses-public/blob/4a02a9a0de3d65bf22315884bba61878280a88b0/docs/courses/AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md
[T]: ../../prerequisites/holomorphic-boundaries-in-convex-cones.html
