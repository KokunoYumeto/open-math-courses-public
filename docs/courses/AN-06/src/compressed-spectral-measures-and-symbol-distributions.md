# Compressed spectral measures and symbol distributions

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Does an observable's mean determine its spectral distribution?** The two-point distribution equally supported at \(-1\) and \(1\) has mean zero, as does the point mass at zero, but their second moments differ. A compressed observable therefore needs more than a first trace. Comparing powers of the compressed matrix with compressed powers of the operator, and controlling leakage through the energy cutoff, recovers the full limiting law.

A spectral subspace contains all states below a chosen energy. Compressing an observable to that subspace gives a finite matrix. We will show that the eigenvalue distribution of this matrix approaches the distribution of the observable's principal symbol over a cotangent energy region.

Laptev and Safarov [LS] supply the finite-projection comparison underlying this topic. Guillemin and Sternberg's text [GS] explains the semiclassical interpretation, and the article of Duistermaat and Guillemin [DG] develops the wave-trace setting. We use [Return times and spectral counting](return-times-and-spectral-counting.md) and [Local spectral density and the subprincipal correction](local-spectral-density-and-subprincipal-correction.md). Composition and Sobolev mapping come from [Classical scalar symbols, summation and regularity](../providers/analysis/classical-scalar-calculus.md#finite-symbol-calculus). The complete finite-dimensional spectral, singular-decomposition, trace-duality, ideal and cyclicity proofs are in [Finite-rank traces and the exact ideal bounds](../providers/analysis/finite-trace-ideals.md#finite-trace-ideals), starting from elementary Hilbert-space arguments. Every product requiring those bounds below has a finite-rank factor. Section 5 gives the complete Bernstein polynomial-approximation proof used for continuous tests, as in [Alt]. The bounded scalar spectral measures are supplied by [Self-adjoint spectral calculus with the original domain](../providers/analysis/self-adjoint-spectral-domains.md#self-adjoint-pvm-domain).

As before, \(X\) is compact, connected and without boundary, of dimension \(n\geq2\). The scalar operator \(P\in\Psi^1_{\mathrm{cl}}(X;\Omega^{1/2})\) is positive elliptic and self-adjoint on \(H^1\), with positive principal symbol \(p\). Let \(B\in\Psi^0_{\mathrm{cl}}\) be self-adjoint, with real principal symbol \(b\).

Use the convention
\[
 \begin{gathered}
\Pi_\lambda=\mathbf1_{(-\infty,\lambda]}(P),\\
H_\lambda=\Pi_\lambda L^2,
\\
N(\lambda)=\dim H_\lambda.
 \end{gathered}
 \tag{1}
\]
Every argument also works with the open endpoint. Symplectic volume on \(T^*X\) is denoted by \(dz\).

<a id="compression-finite-measure"></a>

## 1. The finite matrix and its counting measure

Define the compression as an operator on its finite-dimensional space:
\[
B_\lambda=\Pi_\lambda B\Pi_\lambda\big|_{H_\lambda}.
\tag{2}
\]
It is self-adjoint and has norm at most \(\|B\|\). If its eigenvalues, repeated with multiplicity, are \(\beta_{1,\lambda},\ldots,\beta_{N(\lambda),\lambda}\), set
\[
\rho_\lambda=\sum_{\ell=1}^{N(\lambda)}
                   \delta_{\beta_{\ell,\lambda}}.
\tag{3}
\]
Thus \(\rho_\lambda(\mathbb R)=N(\lambda)\), and
\[
\rho_\lambda(f)=\operatorname{Tr}_{H_\lambda}f(B_\lambda).
\tag{4}
\]
Zero eigenvalues inside \(H_\lambda\) are included. The infinite-dimensional orthogonal complement of \(H_\lambda\) is not part of (3).

We will use two finite-rank consequences of the trace-ideal estimates. If \(T\) has rank at most \(r\), then
\[
\|T\|_1\leq \sqrt r\,\|T\|_2,\qquad
\|T\|_1\leq r\|T\|.
\tag{5}
\]
Indeed the trace norm is the sum of the eigenvalues of \(|T|\), while the squared Hilbert–Schmidt norm is the sum of their squares. There are at most \(r\) nonzero terms; Cauchy–Schwarz gives the first bound and the operator norm bounds each term for the second. We also use
\[
 \begin{gathered}
\|ATC\|_1\leq\|A\|\|T\|_1\|C\|,
\\
 |\operatorname{Tr}T|\leq\|T\|_1.
 \end{gathered}
 \tag{6}
\]
These hold for the indicated source and target Hilbert spaces. All products used below have a finite-rank factor, so are trace class. The trace can be taken either on \(H_\lambda\) or on \(L^2\) after extension by zero.

<a id="compression-weighted-moment"></a>

## 2. A weighted first moment

**Proposition 2.1.** For every self-adjoint \(D\in\Psi^0_{\mathrm{cl}}\), with principal symbol \(d\),
\[
\operatorname{Tr}(\Pi_\lambda D)
=(2\pi)^{-n}\lambda^n\int_{p<1}d\,dz
+O(\lambda^{n-1}).
\tag{7}
\]

**Proof.** First arrange positivity. Choose
\[
L>1+\max(\|D\|,\sup|d|).
\]
Then \(D+LI\) is positive and its principal symbol \(d+L\) is strictly positive. The cumulative trace
\[
 \begin{gathered}
\mu(\lambda)=\operatorname{Tr}(\Pi_\lambda(D+LI))
\\
=\sum_{\lambda_j\leq\lambda}
            \langle(D+LI)\phi_j,\phi_j\rangle
 \end{gathered}
 \tag{8}
\]
is increasing, vanishes at zero and is \(O(\lambda^n)\).

Use the exact small-time model from the counting lesson, Section 3. Write \(K_D(t)=\operatorname{Tr}(e^{-itP}(D+LI))\) as a distribution, and choose an even real \(\chi\in C_c^\infty\), equal to one near zero and supported inside the common small-time construction. Set
\[
 \begin{aligned}
 \nu'(s)&=\frac1{2\pi}\langle\chi(t)K_D(t),e^{its}\rangle,\\
 \nu(\lambda)&=\int_0^\lambda\nu'(s)\,ds.
 \end{aligned}
\]
The distributional pairing is well defined because its first argument has compact support. The tested kernel identity in the counting lesson, Section 2, proves \(\widehat{d\mu}=K_D\). The local coefficient construction, including its smooth time residual, shows that \(\nu\) is smooth and has
\[
\nu(\lambda)=(2\pi)^{-n}\lambda^n
                      \int_{p<1}(d+L)\,dz
                      +O(\lambda^{n-1}).
\tag{9}
\]
It is real because \(K_D(-t)=\overline{K_D(t)}\) and \(\chi\) is even and real; it is normalized at zero by definition. Its derivative has leading coefficient
\(M_0=n(2\pi)^{-n}\int_{p<1}(d+L)\,dz>0\).
The lower homogeneous terms and the negative-energy tail can be absorbed into
\[
|\nu'(\lambda)|\leq M_0(|\lambda|+a_0)^{n-1}
\tag{10}
\]
by increasing \(a_0\), exactly as in the counting lesson.

There is a uniform deleted small-time interval without any base return. Choose a fixed smaller interval \(|t|<T\). The Fourier transform of \(d\mu-d\nu\) is exactly \((1-\chi)K_D\). It vanishes near zero, and away from zero the wavefront inclusion in the counting lesson excludes returns. Multiplication by \(\widehat\varphi(t/T)\) therefore gives a smooth compactly supported function. Repeated integration by parts shows that its inverse transform is Schwartz. Thus the smoothing error is controlled for the actual model, including the smooth residual, rather than only for its homogeneous coefficient expansion.

Apply the bounded-integrable version of the quantitative Tauberian lemma with \(a=1/T\). Its comparison function is the smooth, hence absolutely continuous, representative \(\nu\). We obtain
\[
\mu(\lambda)-\nu(\lambda)=O(\lambda^{n-1}).
\tag{11}
\]
The counting result also gives
\[
N(\lambda)=(2\pi)^{-n}\lambda^n\int_{p<1}dz
                         +O(\lambda^{n-1}),
\tag{12}
\]
since the inverse-period function is bounded. Subtract \(LN(\lambda)\) from (8)–(11), and use (12). This proves (7). Finite-rank trace cyclicity identifies this trace with that of \(\Pi_\lambda D\Pi_\lambda\) on \(H_\lambda\). ∎

In particular (7) applies to \(D=B^j\) for every fixed integer \(j\geq1\): it is self-adjoint, classical of order zero and has principal symbol \(b^j\). What remains is to compare this uncompressed power with the power of the compressed matrix.

<a id="compression-trace-leakage"></a>

## 3. How much can cross an energy cutoff?

Let \(Q_\lambda=I-\Pi_\lambda\). The map \(Q_\lambda B\Pi_\lambda\) measures the part of an observable that moves a low-energy vector out of the low-energy subspace.

The strip-and-gap estimate is Hörmander’s compression lemma [H4, Lemma 29.1.8].

**Lemma 3.1 (trace norm of the leakage).**
\[
\|Q_\lambda B\Pi_\lambda\|_1
=O(\lambda^{n-1/2}).
\tag{13}
\]

**Proof.** The scalar calculus gives
\[
C=[P,B]\in\Psi^0_{\mathrm{cl}},
\tag{14}
\]
so \(C\) is bounded on \(L^2\). The possible order-one leading product cancels because the principal symbols are scalar. Also \(B:H^1\to H^1\), so the commutator identity is valid on each smooth eigenvector.

Choose \(\Lambda=\lambda+\Delta\), with \(1\leq\Delta\leq\lambda\), and split
\[
Q_\lambda B\Pi_\lambda
=(\Pi_\Lambda-\Pi_\lambda)B\Pi_\lambda
+Q_\Lambda B\Pi_\lambda.
\tag{15}
\]
The near term has rank at most \(N(\Lambda)-N(\lambda)\). From (12), for \(\lambda\geq1\) and \(\Lambda\leq2\lambda\),
\[
N(\Lambda)-N(\lambda)
\leq C\lambda^{n-1}(1+\Delta).
\tag{16}
\]
Indeed the difference of the leading volume terms is bounded by \(C\lambda^{n-1}\Delta\), and the two remainders are \(O(\lambda^{n-1})\). Equations (5) and (16) give
\[
\|(\Pi_\Lambda-\Pi_\lambda)B\Pi_\lambda\|_1
\leq C\|B\|\lambda^{n-1}(1+\Delta).
\tag{17}
\]

For the far term, expand in the orthonormal \(P\)-eigenbasis. If \(\lambda_\mu>\Lambda\) and \(\lambda_\nu\leq\lambda\), then
\[
(\lambda_\mu-\lambda_\nu)
       \langle B\phi_\nu,\phi_\mu\rangle
=\langle C\phi_\nu,\phi_\mu\rangle.
\tag{18}
\]
Thus Parseval yields
\[
\begin{aligned}
\|Q_\Lambda B\Pi_\lambda\|_2^2
&=\sum_{\lambda_\nu\leq\lambda}
  \sum_{\lambda_\mu>\Lambda}
      |\langle B\phi_\nu,\phi_\mu\rangle|^2\\
&\leq\Delta^{-2}\sum_{\lambda_\nu\leq\lambda}
                                    \|C\phi_\nu\|^2\\
&\leq \Delta^{-2}\|C\|^2N(\lambda).
\end{aligned}
\tag{19}
\]
This map has rank at most \(N(\lambda)\). Equations (5) and (19) therefore imply
\[
\|Q_\Lambda B\Pi_\lambda\|_1
\leq\Delta^{-1}\|C\|N(\lambda)
\leq C\Delta^{-1}\lambda^n.
\tag{20}
\]
The inequalities concern a finite-dimensional input, even though the far output space may be infinite-dimensional.

Combine (17) and (20):
\[
\|Q_\lambda B\Pi_\lambda\|_1
\leq C\left[\lambda^{n-1}(1+\Delta)
                  +\lambda^n\Delta^{-1}\right].
\tag{21}
\]
Take \(\Delta=\lambda^{1/2}\). Both varying terms have order \(\lambda^{n-1/2}\), proving (13). This argument uses the full counting bound with \(O(\lambda^{n-1})\) remainder, but needs no measure-zero hypothesis on periodic covectors. ∎

<a id="compression-unit-bands"></a>

## 4. Comparing the two powers

The Hilbert–Schmidt leakage has a sharper bound that controls both crossings of the cutoff in each moment.

**Lemma 4.1.** Put \(L=Q_\lambda B\Pi_\lambda\), \(M=\|B\|\), and \(C=[P,B]\). Then
\[
 \begin{gathered}
\|L\|_2^2
 \\
\le K(1+\lambda)^{n-1}\bigl(M^2+2\|C\|^2\bigr)
 \\
=O(\lambda^{n-1}).
 \end{gathered}
 \tag{21a}
\]

**Proof.** Divide the input into unit bands
\[
 E_r=\mathbf1_{(\lambda-r-1,\lambda-r]}(P),
 \qquad r=0,1,\ldots.
 \tag{21b}
\]
Their ranks satisfy \(\operatorname{rank}E_r\le K(1+\lambda)^{n-1}\), uniformly in \(r\) and \(\lambda\ge2\). For bands whose upper endpoint is at least two, subtract the two Weyl expansions (12): the leading volume term changes by at most \(C(1+\lambda)^{n-1}\), and both remainders have that order. Bands meeting a bounded energy range have uniformly bounded rank by compact resolvent. Bands below the positive spectrum have rank zero. This also handles eigenvalues at the displayed endpoints.

The bands are mutually orthogonal and sum to \(\Pi_\lambda\), with finitely many nonzero terms. At \(r=0\), the squared Hilbert–Schmidt norm of \(Q_\lambda BE_0\) is at most \(M^2\operatorname{rank}E_0\). For \(r\ge1\), every input eigenvalue is at most \(\lambda-r\), and every output eigenvalue is greater than \(\lambda\). The gap is greater than \(r\). The exact commutator identity (18) and Parseval give
\[
 \begin{aligned}
 \|Q_\lambda BE_r\|_2^2
 &\le r^{-2}\sum_{\phi_\nu\in E_rL^2}
                      \|C\phi_\nu\|^2\\
 &\le r^{-2}\|C\|^2\operatorname{rank}E_r.
 \end{aligned}
 \tag{21c}
\]
The output may be infinite-dimensional. Only the input rank enters the bound. Sum over \(r\), and use \(\sum_{r\ge1}r^{-2}\le2\), obtained by comparing the tail with \(\int_1^\infty t^{-2}dt\). This proves (21a). For the open spectral endpoint, change the complementary band endpoints consistently; the same gap and rank bounds apply. ∎

When powers of \(B_\lambda\) are extended by zero to \(L^2\), we write them as \((\Pi_\lambda B\Pi_\lambda)^j\) for \(j\geq1\).

<a id="compression-one-crossing"></a>

**Lemma 4.2.** For each fixed integer \(j\geq1\),
\[
 \begin{gathered}
\left\|\Pi_\lambda B^j\Pi_\lambda
              -(\Pi_\lambda B\Pi_\lambda)^j\right\|_1
\\
\leq (j-1)\|B\|^{j-1}
                  \|Q_\lambda B\Pi_\lambda\|_1.
 \end{gathered}
 \tag{22}
\]
At \(j=1\) the difference is zero.

**Proof.** Abbreviate \(\Pi=\Pi_\lambda\), \(Q=I-\Pi\), and let the difference in (22) be \(F_j\). Inserting \(I=\Pi+Q\) just before the final \(B\) gives the exact recurrence
\[
F_j=F_{j-1}B\Pi+\Pi B^{j-1}QB\Pi,
\qquad F_1=0.
\tag{23}
\]
All terms have finite rank. The ideal bound (6) gives
\[
\|F_j\|_1
\leq\|B\|\|F_{j-1}\|_1
       +\|B\|^{j-1}\|QB\Pi\|_1.
\]
Induction proves (22), including \(B=0\), where all differences vanish. ∎

<a id="compression-two-crossings"></a>

**Lemma 4.3.** For every integer \(j\ge2\),
\[
 \|F_j\|_1
 \le \frac{j(j-1)}2 M^{j-2}\|L\|_2^2
 =O_j(\lambda^{n-1}).
 \tag{23a}
\]
At \(j=1\) the difference is zero. If \(B=0\), all differences vanish directly.

**Proof.** Set \(R_a=QB^a\Pi\). Inserting \(\Pi+Q=I\) immediately before the last \(B\) gives
\[
 \begin{gathered}
 R_a=R_{a-1}B\Pi+QB^{a-1}Q\,L,\\
 \|R_a\|_2\le aM^{a-1}\|L\|_2.
 \end{gathered}
 \tag{23b}
\]
The second line follows by induction from the Hilbert–Schmidt ideal inequality and \(R_1=L\). Self-adjointness identifies the second term in (23) as \(R_{j-1}^*L\). Products of two Hilbert–Schmidt maps obey
\[
 \begin{gathered}
\|R_{j-1}^*L\|_1
 \le \|R_{j-1}\|_2\|L\|_2
 \\
\le (j-1)M^{j-2}\|L\|_2^2.
 \end{gathered}
 \tag{23c}
\]
Here every input rank is finite. To see the first inequality directly, trace-norm duality tests the product against a contraction \(A\); the absolute trace is the Hilbert–Schmidt pairing of \(R_{j-1}A^*\) with \(L\), bounded by the product of their norms. Finite-dimensional singular-value decomposition proves this duality for these finite-rank products.

The recurrence therefore gives
\(\|F_j\|_1\le M\|F_{j-1}\|_1+(j-1)M^{j-2}\|L\|_2^2\).
Induction sums \(1+\cdots+(j-1)=j(j-1)/2\), proving (23a). Both cutoff crossings contribute a Hilbert–Schmidt factor. ∎

Taking traces and using (21a) and (23a),
\[
\left|
\operatorname{Tr}_{H_\lambda}B_\lambda^j
                -\operatorname{Tr}(\Pi_\lambda B^j\Pi_\lambda)
\right|
=O_j(\lambda^{n-1}).
\tag{24}
\]
Together with (7), this gives every moment:
\[
 \begin{gathered}
\lambda^{-n}\rho_\lambda(s^j)
\\
\longrightarrow (2\pi)^{-n}\int_{p<1}b(z)^j\,dz,
 j=0,1,2,\ldots.
 \end{gathered}
 \tag{25}
\]
For \(j=0\) the left side is \(\lambda^{-n}N(\lambda)\); the zeroth power is the identity on \(H_\lambda\). Equation (12) proves that case.

<a id="compression-symbol-law"></a>

## 5. The limiting distribution

Define the finite positive measure
\[
\rho=b_*\!\left((2\pi)^{-n}\mathbf1_{\{p<1\}}\,dz\right).
\tag{26}
\]
The homogeneous symbol \(b\) is defined off the zero section; the zero section has volume zero, so its value there is irrelevant. Equivalently,
\[
\rho(f)=(2\pi)^{-n}\int_{p<1}f(b(z))\,dz.
\tag{27}
\]

The symbol-distribution limit is Hörmander’s Szegö-type theorem [H4, Theorem 29.1.7].

**Theorem 5.1 (the distribution of a compressed observable).** For every \(f\in C(\mathbb R)\),
\[
\lambda^{-n}\rho_\lambda(f)\longrightarrow\rho(f).
\tag{28}
\]
For each fixed polynomial \(q\), the difference in (28) is \(O_q(\lambda^{-1})\). No assumption about the measure of periodic trajectories is required.

**Proof.** Choose
\[
R>\max(\|B\|,\sup|b|).
\]
Both measures are supported in the common compact interval \([-R,R]\). Their masses are bounded after the required normalization:
\[
 \begin{gathered}
\lambda^{-n}\rho_\lambda(\mathbb R)
=\lambda^{-n}N(\lambda)=O(1),\\
\rho(\mathbb R)=(2\pi)^{-n}\int_{p<1}dz<\infty.
 \end{gathered}
 \tag{29}
\]

<a id="compression-bernstein"></a>

Here is the complete polynomial-approximation step. Put \(g(x)=f(2Rx-R)\) on \([0,1]\). A sequence in this interval has a convergent subsequence by nested bisection, as in the finite compactness proof in the trace provider. If \(g\) were unbounded, a sequence with \(|g(x_j)|>j\) would have such a subsequence, contradicting continuity at its limit. If \(g\) were not uniformly continuous, there would be \(\varepsilon_0>0\) and pairs \(x_j,y_j\) with \(|x_j-y_j|\to0\) but \(|g(x_j)-g(y_j)|\ge\varepsilon_0\). A convergent subsequence of \(x_j\) makes both points tend to the same limit, again contradicting continuity. Write \(M_g=\sup|g|\) and
\[
 \omega_g(\delta)=\sup_{|x-y|\le\delta}|g(x)-g(y)|,
 \qquad\omega_g(\delta)\longrightarrow0.
\]
For an integer \(m\ge1\), form the Bernstein polynomial
\[
 \begin{gathered}
 w_{m,k}(x)=\binom mk x^k(1-x)^{m-k},\\
 \mathcal B_mg(x)=\sum_{k=0}^m g(k/m)w_{m,k}(x).
 \end{gathered}
\]
The weights are nonnegative and sum to one by the binomial formula. The identities
\(k\binom mk=m\binom{m-1}{k-1}\) and
\(k(k-1)\binom mk=m(m-1)\binom{m-2}{k-2}\), followed by the binomial formula again, give
\[
 \begin{aligned}
 \sum_k(k/m)w_{m,k}(x)&=x,\\
 \sum_k(k/m)^2w_{m,k}(x)&=x^2+x(1-x)/m,\\
 \sum_k(k/m-x)^2w_{m,k}(x)&=x(1-x)/m\le1/(4m).
 \end{aligned}
\]
For \(m=1\) the second factorial moment is zero and these formulas follow directly; the endpoint values are the continuous polynomial values. The total weight of indices with \(|k/m-x|>\delta\) is at most \(1/(4m\delta^2)\). Splitting the approximation error into this set and its complement gives
\[
 \sup_{0\le x\le1}|\mathcal B_mg(x)-g(x)|
 \le\omega_g(\delta)+\frac{M_g}{2m\delta^2}.
\]
First choose \(\delta>0\) small, then \(m\) large. Composing with \(x=(s+R)/(2R)\) produces a polynomial \(q(s)\) with \(\sup_{[-R,R]}|f-q|<\varepsilon\). This proof works for complex-valued \(f\) as well, and gives real coefficients when \(f\) is real. This is the Bernstein construction [Alt, §3, equation (3.5) and Theorem 3.6], with an explicit error bound. Now
\[
\begin{aligned}
|\lambda^{-n}\rho_\lambda(f)-\rho(f)|
&\leq \varepsilon\left[\lambda^{-n}N(\lambda)+\rho(\mathbb R)\right]\\
&\quad+|\lambda^{-n}\rho_\lambda(q)-\rho(q)|.
\end{aligned}
\tag{30}
\]
The last term tends to zero by (25). Taking the upper limit and then \(\varepsilon\downarrow0\) proves (28). For a fixed polynomial, (7) and (24) give the stated rate, by summing its finitely many coefficients. Continuous approximation asserts convergence without a universal rate for arbitrary \(f\). ∎

<a id="compression-normalization"></a>

There is also a probability version. The coefficient
\[
c_P=(2\pi)^{-n}\int_{p<1}dz
\]
is positive. Dividing (28) by \(N(\lambda)/\lambda^n\to c_P\) gives
\[
\frac{\rho_\lambda}{N(\lambda)}
\ \longrightarrow\ \frac{\rho}{c_P}.
\tag{31}
\]
The right side samples \(b\) using normalized symplectic volume on the energy region.
For a fixed polynomial, this probability-normalized convergence also has error \(O_q(\lambda^{-1})\): its numerator is \(\lambda^n\rho(q)+O_q(\lambda^{n-1})\), and (12) gives the denominator \(c_P\lambda^n+O(\lambda^{n-1})\), with \(c_P>0\). Continuous tests retain convergence without a universal rate.

All conclusions remain valid for a lower-bounded \(P\) with the same positive principal symbol. To see this, choose \(c\) such that \(P+c>0\). Its projection at \(\lambda+c\) is exactly \(\Pi_\lambda\), and its commutator with \(B\) is still \([P,B]\). Its principal symbol is unchanged. Since \((\lambda+c)^n/\lambda^n\to1\), applying the positive results at energy \(\lambda+c\) proves (28) and (31). The weighted first-moment error and leakage estimates retain their stated orders under this fixed translation.


<a id="compression-smooth-tests"></a>

## 5A. Smooth tests, compression error and stable distributions

[Laptev and Safarov, *Szegö type limit theorems*](https://www.ma.ic.ac.uk/~alaptev/Papers/sz.pdf), Section 1, Theorem 1.2, relates smooth functional calculus to leakage through an orthogonal projection. Here is a direct proof of its bounded-operator, finite-rank case, followed by a stability consequence. It keeps distinct the compression error and the asymptotic symbol calculation.

**Proposition 5.2 (a smooth-test compression bound).** Let \(B=B^*\) be bounded, let \(\Pi\) be a finite-rank orthogonal projection, put \(Q=I-\Pi\), and let \(A=\Pi B\Pi|_{\operatorname{ran}\Pi}\). If \(f\) is real and \(C^2\) on an interval containing \([-\|B\|,\|B\|]\), then

\[
 \begin{gathered}
 D_f=\operatorname{Tr}_{\operatorname{ran}\Pi}
       \bigl(\Pi f(B)\Pi-f(A)\bigr),\\
 |D_f|\le \frac12\|f''\|_\infty\|QB\Pi\|_{\mathrm{HS}}^2.
 \end{gathered}
\]

The trace on the left is nonnegative when \(f\) is convex.

The same statement holds for \(f\in C^{1,1}\), with \(\operatorname{Lip}(f')\) in place of \(\|f''\|_\infty\). This includes the continuously differentiable representative of a real \(W^{2,\infty}\) function on the interval, which is the regularity used in [LS, Theorem 1.2].

**Proof.** Choose an orthonormal eigenbasis \(e_1,\ldots,e_d\) of \(A\), with eigenvalues \(\mu_j\). The scalar spectral calculus for the bounded self-adjoint \(B\) supplies probability measures \(\sigma_j\) with

\[
 \begin{gathered}
 \langle f(B)e_j,e_j\rangle=\int f(t)\,d\sigma_j(t),\\
 \int t\,d\sigma_j(t)=\mu_j,\\
 \int(t-\mu_j)^2d\sigma_j(t)=\|(B-\mu_j)e_j\|^2.
 \end{gathered}
\]

The scalar spectral measures come from [Self-adjoint spectral calculus with the original domain](../providers/analysis/self-adjoint-spectral-domains.md#self-adjoint-pvm-domain). Only its bounded-operator restriction is needed here. Taylor's formula with integral remainder gives

\[
 |f(t)-f(\mu_j)-f'(\mu_j)(t-\mu_j)|
 \le\frac12\|f''\|_\infty(t-\mu_j)^2.
\]

For convex \(f\), apply its defining inequality at \(\mu_j+\theta(t-\mu_j)\), subtract \(f(\mu_j)\), divide by \(\theta>0\), and let \(\theta\downarrow0\). Differentiability gives \(f(t)-f(\mu_j)\geq f'(\mu_j)(t-\mu_j)\), so the expression before the absolute value is nonnegative. Its linear term integrates to zero. Since \(\Pi Be_j=\mu_je_j\), one has \((B-\mu_j)e_j=QBe_j\). Sum over \(j\); the sum of these squared norms is exactly \(\|QB\Pi\|_{\mathrm{HS}}^2\). This proves both assertions. \(\square\)

For the stated \(C^{1,1}\) extension, the fundamental theorem of calculus gives
\[
 f(t)-f(\mu)-f'(\mu)(t-\mu)
 =\int_\mu^t\bigl(f'(r)-f'(\mu)\bigr)\,dr.
\]
Its absolute value is at most \(\operatorname{Lip}(f')|t-\mu|^2/2\), for either order of the two endpoints. The preceding spectral-measure argument therefore applies unchanged. The constant \(1/2\) and the convex sign require no approximation of operators or differentiation of their spectral projections.

<a id="compression-weak-representative"></a>

Here is the asserted weak-Sobolev representative. On a bounded interval write the distributional derivatives as \(g=f'\in L^\infty\) and \(h=g'\in L^\infty\). Fix an interior point \(a\) and put \(G(t)=\int_a^t h(r)\,dr\). The scalar primitive identity in [Hilbert-valued integration, Section 3](../providers/analysis/hilbert-valued-integration.md) gives \(G'=h\) distributionally, and \(|G(t)-G(s)|\leq\|h\|_\infty|t-s|\). Thus \(g-G\) has zero distributional derivative. A locally integrable function with this property is a constant distribution: subtract a fixed integral-one test from any other test to make its integral zero, and use the compactly supported primitive of that difference. Consequently \(g\) has a Lipschitz representative \(\widetilde g\). Applying the same argument to \(f-\int_a^t\widetilde g(r)\,dr\) gives a \(C^1\) representative \(\widetilde f\), with \(\widetilde f'=\widetilde g\) and \(\operatorname{Lip}(\widetilde f')\leq\|f''\|_\infty\). Both representatives extend continuously to the endpoints. This proves the claimed \(W^{2,\infty}\) case with the same constant.

For \(f(t)=t^2\) equality holds with the positive sign:

\[
 \operatorname{Tr}(\Pi B^2\Pi-A^2)=\|QB\Pi\|_{\mathrm{HS}}^2.
\]

For the spectral cutoff of this lesson, the sharper squared Hilbert–Schmidt bound in Lemma 4.1 is \(\|Q_\lambda B\Pi_\lambda\|_{\mathrm{HS}}^2=O(\lambda^{n-1})\). Proposition 5.2 therefore gives a normalized compression defect \(O_f(\lambda^{-1})\) for every fixed \(C^2\) test. This controls the difference between the two operator traces. A rate for either trace against the classical symbol law still requires its separate symbol estimate; the defect bound does not create such an estimate.

<a id="compression-stability"></a>

**Theorem 5.3 (a limit law survives small trace-norm changes).** Let \(A_k,C_k\) be self-adjoint matrices of the same dimension \(d_k\geq1\), with \(\|A_k\|,\|C_k\|\le M<\infty\), and suppose

\[
 \varepsilon_k=d_k^{-1}\|A_k-C_k\|_1\longrightarrow0.
\]

If the probability eigenvalue measures of \(A_k\) converge to \(\nu\), then those of \(C_k\) converge to the same \(\nu\), against every continuous function. In particular, bounded changes of rank \(r_k=o(d_k)\) preserve the law. Counts in an interval also converge whenever \(\nu\) assigns zero mass to both endpoints.

**Proof.** For every integer \(m\ge1\), telescoping in the given order gives

\[
 A_k^m-C_k^m=\sum_{j=0}^{m-1}A_k^{m-1-j}(A_k-C_k)C_k^j.
\]

The trace-ideal inequality gives

\[
 d_k^{-1}|\operatorname{Tr}(A_k^m-C_k^m)|
 \le mM^{m-1}\varepsilon_k.
\]

For a fixed polynomial \(p(t)=\sum a_mt^m\), sum these bounds. Approximate a continuous \(f\) uniformly on \([-M,M]\) by such a polynomial, using the Bernstein approximation already used in Theorem 5.1. The two probability masses are one, so the approximation contributes at most \(2\|f-p\|_\infty\). First take \(k\to\infty\), then the approximation error to zero. This proves the common law without assigning a universal rate to a continuous test.

If \(A_k-C_k\) has rank at most \(r_k\), then \(\|A_k-C_k\|_1\le2Mr_k\), proving the rank assertion. For a closed interval \([a,b]\), bound its indicator above and below by continuous piecewise linear functions which change from zero to one only within distance \(\delta\) of its endpoints. The difference of their limiting integrals is bounded by \(\nu([a-\delta,a+\delta]\cup[b-\delta,b+\delta])\). This tends to zero when the endpoints have no atoms. The same argument covers open or half-open conventions. \(\square\)

As a worked application, take \(A_\lambda=\Pi_\lambda B\Pi_\lambda\) and add a uniformly bounded self-adjoint matrix \(E_\lambda\) with rank \(o(N(\lambda))\). Theorem 5.1 and Theorem 5.3 give the same symbol distribution for \(A_\lambda+E_\lambda\), even when the matrix modification has no pseudodifferential symbol. This is a statement about the fraction of states, not about the location of every eigenvalue: a rank-one change can leave a persistent outlier. For example \(A_k=0\) and \(C_k=\operatorname{diag}(1,0,\ldots,0)\) have a common limit \(\delta_0\), while their largest eigenvalues remain zero and one.

### Use the conclusion

Check the cutoff-crossing estimate before taking higher moments. Identify the compact interval on which polynomial approximation is used, and then recover the distribution of the principal symbol rather than only its mean.

<a id="compression-solutions"></a>

## 6. Exercises and complete solutions

**Exercise 6.1 (what is being counted; introductory).** Let \(B=cI\), with real \(c\). Find \(\rho_\lambda\) and its limit. Explain why counting all eigenvalues of \(\Pi_\lambda B\Pi_\lambda\) on ambient \(L^2\) would give a different, unsuitable object.

**Solution 6.1.** On \(H_\lambda\), the compression is \(cI_{H_\lambda}\), so
\[
\rho_\lambda=N(\lambda)\delta_c,\qquad
\lambda^{-n}\rho_\lambda\longrightarrow c_P\delta_c.
\]
Its symbol is the constant \(c\), and (26) gives exactly the same measure. On the orthogonal complement, the ambient operator is zero. That complement is infinite-dimensional, so counting its zero eigenvalue would add an infinite mass at zero. When \(c=0\), the intended measure still has just \(N(\lambda)\) zeros, whereas the ambient zero operator has infinitely many. The finite spectral subspace in (2) is part of the definition.

**Exercise 6.2 (balancing a strip and a gap; intermediate).** In (21), choose \(\Delta=\lambda^\theta\), \(0\leq\theta\leq1\). Determine the best exponent supplied by this family of choices.

**Solution 6.2.** The two varying exponents are \(n-1+\theta\) and \(n-\theta\); the fixed term has exponent \(n-1\). Hence the estimate has exponent
\[
\max(n-1+\theta,n-\theta).
\]
The first increases with \(\theta\), the second decreases. Their intersection is \(\theta=1/2\), with value \(n-1/2\). At either endpoint the maximum is \(n\). Thus the square-root gap is optimal for this particular trace-norm bound. If \([P,B]=0\), leakage vanishes exactly and the gap argument is unnecessary.

**Exercise 6.3 (a finite-rank change of observable; intermediate).** Let \(K=K^*\) have finite rank. Compare the moments of the compressions of \(B+K\) and \(B\), after division by \(N(\lambda)\). Prove directly that their normalized empirical distributions have the same limit whenever one of them converges.

**Solution 6.3.** The compressed difference is \(K_\lambda=\Pi_\lambda K\Pi_\lambda|_{H_\lambda}\), with \(\|K_\lambda\|_1\leq\|K\|_1\). Let \(A_\lambda=B_\lambda+K_\lambda\) and choose a constant \(M\) bounding both operator norms. For \(j\geq1\), the noncommutative identity
\[
A_\lambda^j-B_\lambda^j
=\sum_{r=0}^{j-1}A_\lambda^{j-1-r}
                       K_\lambda B_\lambda^r
\]
gives trace norm at most \(jM^{j-1}\|K\|_1\), uniformly in \(\lambda\). Since \(N(\lambda)\sim c_P\lambda^n\to\infty\), the normalized moment differences tend to zero. The zeroth moments are both one. Both empirical probability measures have support in a fixed interval, so polynomial approximation and the argument of (30) give the claim for every continuous test function. This direct argument does not require \(K\) to be pseudodifferential.

**Exercise 6.4 (a stronger estimate for the second moment; advanced).** Show
\[
\operatorname{Tr}(\Pi_\lambda B^2\Pi_\lambda)
              -\operatorname{Tr}_{H_\lambda}B_\lambda^2
=\|Q_\lambda B\Pi_\lambda\|_2^2\geq0.
\tag{32}
\]
First use the strip/gap decomposition to bound this difference by \(O(\lambda^{n-2/3})\). Then use the unit input bands to obtain \(O(\lambda^{n-1})\). Explain how the squared leakage controls every higher fixed power.

**Solution 6.4.** Self-adjointness gives
\[
\begin{gathered}
\Pi_\lambda B^2\Pi_\lambda
              -(\Pi_\lambda B\Pi_\lambda)^2
\\
=\Pi_\lambda BQ_\lambda B\Pi_\lambda
\\
=(Q_\lambda B\Pi_\lambda)^*(Q_\lambda B\Pi_\lambda).
\end{gathered}
\]
Taking the finite trace proves (32). The near and far terms in (15) have orthogonal output spaces, so their squared Hilbert–Schmidt norms add. The near term has squared norm at most
\(\|B\|^2[N(\Lambda)-N(\lambda)]\); use a basis in its finite-dimensional output space and adjoint equality of the Hilbert–Schmidt norm to see this. Formula (19) bounds the far term. Thus
\[
\|Q_\lambda B\Pi_\lambda\|_2^2
\leq C\left[\lambda^{n-1}(1+\Delta)
                      +\lambda^n\Delta^{-2}\right].
\]
Choose \(\Delta=\lambda^{1/3}\). The two varying terms are both \(O(\lambda^{n-2/3})\), while the fixed term is smaller. The unit input bands of Lemma 4.1 instead bound the squared leakage by (21a), namely \(O(\lambda^{n-1})\). Each nonzero band uses its input rank and the inverse-square gap, whose sum is finite. Finally the second crossing in the recurrence (23) is \(R_{j-1}^*L\); (23b)–(23c) bound its trace norm by \((j-1)M^{j-2}\|L\|_2^2\). Summing the recurrence gives (23a) for every fixed higher power. The one-sided trace-norm bound (13) remains a separate valid estimate.

**Exercise 6.5 (an angular observable on a flat torus; advanced).** On the two-dimensional torus \((\mathbb R/2\pi\mathbb Z)^2\), let \(P\) be a positive Fourier multiplier with high-frequency symbol \(|\eta|\). Let \(B\) be a self-adjoint Fourier multiplier with high-frequency symbol \(b(\eta)=\eta_1/|\eta|\). Find the limiting probability measure in (31), and explain why leakage is zero.

**Solution 6.5.** Section 6 of [Local spectral density and the subprincipal correction](local-spectral-density-and-subprincipal-correction.md) proves the classical torus multiplier construction and completeness of the Fourier basis. It applies both to the smooth order-one symbol of \(P\) and to the smooth order-zero extension of \(\eta_1/|\eta|\) away from the finitely many small modes. The two multipliers are diagonal in this same basis, so \(B\) preserves every \(P\)-spectral subspace. Thus \(Q_\lambda B\Pi_\lambda=0\), and compressed and uncompressed powers agree exactly.

The torus volume is \((2\pi)^2\), canceling the Fourier factor in (27). In polar coordinates \(\eta=r(\cos\theta,\sin\theta)\),
\[
 \begin{gathered}
\rho(f)=\int_0^1r\,dr\int_0^{2\pi}f(\cos\theta)\,d\theta
\\
=\int_{-1}^1\frac{f(s)}{\sqrt{1-s^2}}\,ds.
 \end{gathered}
 \tag{33}
\]
The last equality follows by splitting the angular integral into the two half-circles and substituting \(s=\cos\theta\) in each. The radial integral is \(1/2\). Consequently \(c_P=\pi\) and the limiting probability measure has density
\[
\frac{1}{\pi\sqrt{1-s^2}}\mathbf1_{\{-1<s<1\}}\,ds.
\tag{34}
\]
Its endpoint singularities are integrable and give no endpoint atoms. Finitely many choices of small Fourier modes do not affect the limit, as can also be seen from Exercise 6.3. The limiting measure comes from angular volume, even though each finite compression has a discrete spectrum.

## References

[LS, §1, Theorems 1.2, 1.3 and 1.5–1.6; Appendix A] proves the compression inequality and the separated-band estimates. Its closed-manifold application [LS, §2, Theorem 2.2 and Lemma 2.3] uses an additional weighted spectral asymptotic and a smooth functional calculus. Here Proposition 2.1 supplies the weighted asymptotic from the preceding course proofs, while the moment argument supplies all continuous tests without invoking that additional smooth calculus. Zelditch [Z, §0] discusses the law of a single Zoll cluster; [Z, §4] computes its geometric band invariant. Those are different spectral subspaces from the cumulative cutoff in (1).

- [LS] Ari Laptev and Yuri Safarov, [“Szegö type limit theorems,” freely accessible author manuscript](https://www.ma.ic.ac.uk/~alaptev/Papers/sz.pdf), §§1–2 and Appendix A, manuscript pages 3–5, 8 and 11–12. The published article appeared in *Journal of Functional Analysis* 138 (1996), 544–559.
- [Alt] Francesco Altomare, [“Korovkin-type Theorems and Approximation by Positive Linear Operators,” free arXiv version 1](https://arxiv.org/pdf/1009.2601v1), §3 especially the Bernstein polynomials in (3.5) and Theorems 3.6–3.7. *Surveys in Approximation Theory* 6 (2010), 92–164.
- [GS] Victor Guillemin and Shlomo Sternberg, [*Semi-classical Analysis*, freely accessible author text](https://people.math.harvard.edu/~shlomo/docs/Semi_Classical_Analysis_Start.pdf), Introduction §0.5, printed pages xi–xii, for the semiclassical spectral interpretation.
- [DG] Johannes J. Duistermaat and Victor W. Guillemin, “The spectrum of positive elliptic operators and periodic bicharacteristics,” *Inventiones Mathematicae* 29 (1975), 39–79. [Freely accessible digitized full article](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0029/LOG_0010.pdf), Introduction for the relation between elliptic spectra and periodic flow.
- [Z] Steve Zelditch, “Fine structure of Zoll spectra,” *Journal of Functional Analysis* 143 (1997), 415–460. [Elsevier open archive](https://doi.org/10.1006/jfan.1996.2981), §0 and §4. 
- [H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, Theorem 29.1.7 and Lemma 29.1.8, pp. 259–261. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
