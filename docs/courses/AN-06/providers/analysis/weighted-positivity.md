# Weighted positivity from Gaussian packets

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

This reading proves the precise positivity estimate used by the near-frequency resolvent argument, including symbols without compact frequency support. The construction uses positive Gaussian-packet quantization, as presented in Nicolas Lerner's freely available [author Chapter 2, Definition 2.4.1 and Proposition 2.4.3(1)–(3), printed pages 101–103](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf). The proof below supplies its own localization and error estimates. It does not import the general metric Gårding theorem or a symbol-composition theorem.

Use $D=-i\partial$, $X=\langle x\rangle=(1+|x|^2)^{1/2}$, and an inner product linear in the first entry. The earlier programme reading [A finite-derivative bound for left quantization](finite-derivative-l2.md#fourier-normalization) proves Fourier inversion, Plancherel, Schwartz density, the Gaussian transform, the packet resolution of the identity and the Schur estimate. Its preceding measure subsection proves the Euclidean interchanges used here. We use those full proofs with the same inverse Fourier factor $(2\pi)^{-n}$.

The [local Hilbert representing-vector and adjoint proofs](finite-trace-ideals.md#elementary-hilbert-tools) provide the Hilbert tools needed here. In particular, if $B(u,v)$ is linear in $u$, conjugate-linear in $v$, and $|B(u,v)|\le C\|u\|\|v\|$, apply the representing-vector theorem to $v\mapsto\overline{B(u,v)}$. It gives a unique $h_u$ with $B(u,v)=(h_u,v)$ and $\|h_u\|\le C\|u\|$. Uniqueness makes $u\mapsto h_u$ linear, hence a bounded operator representing the form. This proves the precise form-to-operator step used in the cutoff limit below, for the stated inner-product convention.

<a id="weighted-positivity"></a>
## The exact estimate

**Theorem 1.** Let $n\ge1$, and let $a(x,\xi)$ be a smooth real nonnegative function satisfying
\[
 |\partial_x^\alpha\partial_\xi^\beta a(x,\xi)|
 \le C_{\alpha\beta}X^{-1-|\alpha|}\langle\xi\rangle^{-|\beta|}
 \quad(\alpha,\beta\in\mathbb N^n).
 \tag{P1}
\]
Then its left operator is bounded on $L^2$ and
\[
 \operatorname{Re}(a(x,D)u,u)
 \ge -C\|X^{-1}u\|_2^2 \qquad(u\in L^2).
 \tag{P2}
\]
The constant uses only finitely many constants in (P1). In particular it is uniform for any family having uniform displayed seminorms. No compact support or extra decay in $\xi$ is assumed. The case $n=0$ is nonnegative scalar multiplication.

We prove two elementary operator estimates before the localization.

<a id="bounded-amplitudes"></a>
## A bound for amplitudes with two position variables

**Lemma 2.** For each dimension there is an integer $k$ such that the operator
\[
 B u(x)=(2\pi)^{-n}\iint e^{i(x-y)\cdot\xi}b(x,y,\xi)u(y)\,dy\,d\xi
 \tag{P3}
\]
is bounded on $L^2$ when all derivatives of $b$ through order $k$ in each of the three variable groups are bounded. Its norm is at most a dimensional constant times their maximum. The integral is the cutoff oscillatory integral. This includes left, right and Weyl quantization and every intermediate evaluation $b(x,y,\xi)=c(\tau x+(1-\tau)y,\xi)$, uniformly for $0\le\tau\le1$.

**Proof.** Take an integer $N>n/2$, $M=2N+n+1$, and, for definiteness, $k=2M+2N+2$. Use the normalized packets
\[
 \phi_{p,\eta}(x)=e^{i\eta\cdot x}\pi^{-n/4}e^{-|x-p|^2/2}.
\]
The cited packet identity gives the isometry $Wu=(2\pi)^{-n/2}(u,\phi_{p,\eta})$ and $W^*W=I$.

First suppose $b$ is compactly supported in all its variables. Its kernel is bounded with compact position support, so $B$ is already bounded and its packet matrix is legitimate. For input packet $(p,\eta)$ and output packet $(q,\zeta)$ put $d=q-p$, $e=\eta-\zeta$, $x=q+v$, $y=p+w$ and $\xi=\eta+\theta$. Apart from a constant phase and a dimensional factor, the matrix element is
\[
 \iiint e^{i(e\cdot v+d\cdot\theta)}e^{i(v-w)\cdot\theta}
 b(q+v,p+w,\eta+\theta)g(v)g(w)\,dv\,dw\,d\theta.
 \tag{P4}
\]
Integrate first by parts in $w$, using $(1-\Delta_w)^M$ on $e^{-iw\cdot\theta}$, to extract $(1+|\theta|^2)^{-M}$. Next use $(1-\Delta_v)^N(1-\Delta_\theta)^N$ on the first exponential in (P4). This extracts
$(1+|e|^2)^{-N}(1+|d|^2)^{-N}$.

The remaining integrand is a finite sum of derivatives of $b$ within the stated orders, derivatives of the two Gaussians, polynomial factors in $v,w$, and a factor bounded by a constant times
$(1+|\theta|)^{-2M+2N}$. Derivatives in $v$ can introduce at most $2N$ factors of $\theta$; derivatives in $\theta$ introduce only polynomial factors in $v-w$ or improve derivatives of its denominator. The Gaussian-polynomial factors are integrable, and $2M-2N>n$ makes the remaining $\theta$ integral finite. Consequently
\[
 |(B\phi_{p,\eta},\phi_{q,\zeta})|
 \le C\mathcal M_k(b)
 (1+|p-q|^2)^{-N}(1+|\eta-\zeta|^2)^{-N},
 \tag{P5}
\]
where $\mathcal M_k$ is the finite derivative maximum. Its row and column integrals are bounded because $2N>n$. The proved Schur estimate bounds $WBW^*$, and $B=W^*(WBW^*)W$ gives the assertion.

For a general amplitude multiply it by fixed smooth cutoffs at radius $L$ in each variable group. Their derivative maxima remain uniformly bounded for $L\ge1$. On two Schwartz test functions the oscillatory pairing has a well-defined limit: integration by parts with $(1-\Delta_y)^M$ supplies $(1+|\xi|^2)^{-M}$; derivatives of the input are integrable in $y$, and the output test is integrable in $x$. This is an absolute majorant independent of $L$, so dominated convergence gives the limiting pairing. The uniform operator bound passes to that pairing and gives a bounded operator by Hilbert-space representation and density. This proves both its existence and the claimed norm estimate. The affine evaluation in the last sentence of the lemma changes these finite derivative bounds by dimensional factors uniform in $\tau$. $\square$

<a id="packet-positivity-at-one-scale"></a>
## Positivity at one spatial scale

**Lemma 3.** Suppose $R\ge1$, $p\ge0$ is smooth, and
\[
 |\partial_x^\alpha\partial_\xi^\beta p(x,\xi)|
 \le A_{\alpha\beta}R^{-1-|\alpha|}.
 \tag{P6}
\]
Then $\operatorname{Re}(p(x,D)v,v)\ge-CR^{-2}\|v\|_2^2$, with $C$ depending on finitely many $A_{\alpha\beta}$ and independent of $R$.

**Proof.** Put $r=R^{1/2}$ and
\[
 g_r(t)=(\pi r^2)^{-n/4}e^{-|t|^2/(2r^2)},\qquad
 \phi^r_{q,\eta}(x)=e^{i\eta\cdot x}g_r(x-q).
\]
Plancherel in $\eta$ followed by integration in $q$ proves, exactly as for the unit-width packets,
$(2\pi)^{-n}\iint|(v,\phi^r_{q,\eta})|^2dq\,d\eta=\|v\|_2^2$.
Thus the bounded operator $Q_r(p)$ defined by
\[
 (Q_r(p)v,v)=(2\pi)^{-n}\iint
 p(q,\eta)|(v,\phi^r_{q,\eta})|^2dq\,d\eta
 \tag{P7}
\]
is nonnegative and has norm at most $\|p\|_\infty$.

Its Weyl symbol is $p*G_r$, where convolution is in both phase-space variables and
\[
 G_r(t,\theta)=\pi^{-n}e^{-|t|^2/r^2-r^2|\theta|^2}.
 \tag{P8}
\]
Here is the normalization check. With $z=(x+y)/2$, $h=x-y$, the two packet factors have product
\[
 g_r(x-q)g_r(y-q)
 =(\pi r^2)^{-n/2}e^{-|z-q|^2/r^2-|h|^2/(4r^2)}.
\]
The Fourier transform in $\theta$ of $\pi^{-n}e^{-r^2|\theta|^2}$ is
$(\pi r^2)^{-n/2}e^{-|h|^2/(4r^2)}$. Substitution in the kernel of (P7) gives exactly the Weyl kernel with symbol $p*G_r$. For bounded symbols the identity is first checked with cutoffs and then paired with Schwartz tests; the packet isometry and the Gaussian majorants justify the limit.

The Gaussian (P8) has mass one, zero first moments, second position moments $r^2/2$, and second frequency moments $1/(2r^2)$ in each coordinate. The mass follows by the Gaussian integral in each variable, and oddness gives the first moments. For the second moments, integration of $\partial_{t_j}(t_j e^{-|t|^2/r^2})$ over the whole space gives $\int t_j^2e^{-|t|^2/r^2}\,dt=(r^2/2)\int e^{-|t|^2/r^2}\,dt$; the boundary term vanishes by Gaussian decay. Applying the same calculation with $r$ replaced by $r^{-1}$ proves the frequency moment. Apply Taylor's formula with its integral second-order remainder separately to convolution in position and in frequency. Convolution does not increase a supremum norm. For every fixed pair of multi-indices this proves
\[
 \|\partial_x^\alpha\partial_\xi^\beta(p*G_r-p)\|_\infty
 \le C_{\alpha\beta}
 \bigl(r^2R^{-3-|\alpha|}+r^{-2}R^{-1-|\alpha|}\bigr)
 \le C'_{\alpha\beta}R^{-2}.
 \tag{P9}
\]
The first-order Taylor terms integrate to zero. Lemma 2, applied to Weyl evaluation, therefore bounds
$Q_r(p)-\operatorname{Op}_W(p)$ by $CR^{-2}$.

We must also account for the choice of quantization. In the difference of left and Weyl kernels,
\[
 p(x,\xi)-p((x+y)/2,\xi)
 =\frac12\sum_{j=1}^n(x_j-y_j)
 \int_0^1\partial_{x_j}p\bigl((x+y)/2+t(x-y)/2,\xi\bigr)dt.
\]
Move $x_j-y_j$ from the exponential by integration by parts in $\xi_j$. The resulting amplitude is
\[
 \frac i2\sum_{j=1}^n\int_0^1
 \partial_{\xi_j}\partial_{x_j}p
 \bigl((x+y)/2+t(x-y)/2,\xi\bigr)dt.
 \tag{P10}
\]
All its derivatives required by Lemma 2 are bounded by $CR^{-2}$, by (P6), uniformly in $t$. This proves
$\|\operatorname{Op}_L(p)-\operatorname{Op}_W(p)\|\le CR^{-2}$.
The identity is also justified by frequency cutoffs: their extra differentiated terms contain a factor tending to zero and have the same bounded-amplitude estimates, while the remaining pairings converge as in Lemma 2. Combining (P7), (P9) and (P10) proves the lemma. $\square$

<a id="weighted-spatial-localization"></a>

## A square partition and the localization error

Choose smooth nonnegative functions $\rho_j$, $j\ge0$, with
\[
 \sum_j\rho_j(x)^2=1,\qquad
 |\partial^\alpha\rho_j|\le C_\alpha R_j^{-|\alpha|},\qquad R_j=2^j,
 \tag{P11}
\]
whose supports have $X$ comparable to $R_j$, with a fixed overlap bound. One explicit construction starts with a radial smooth function $\theta$, equal to one on the unit ball, zero outside the ball of radius two, and nonincreasing on radial lines. Set $\psi_0=\theta$, $\psi_j(x)=\theta(x/2^j)-\theta(x/2^{j-1})$ for $j\ge1$. These functions sum to one and have fixed finite overlap. Divide each by $(\sum_k\psi_k^2)^{1/2}$. The denominator is bounded below by the reciprocal square root of the overlap bound, so differentiation gives (P11). The [smooth cutoff construction](elementary-functions-and-cutoffs.md#smooth-flat-cutoffs) supplies $\theta$ with these properties. Choose $\chi_j\ge0$ equal to one on $\operatorname{supp}\rho_j$, with slightly larger comparable annular support and the same derivative bounds.

The symbols $p_j=\chi_j a$ satisfy (P6), by (P1) and $\langle\xi\rangle^{-|\beta|}\le1$. Since multiplication on the output is exact in left quantization,
\[
 \operatorname{Re}(a(x,D)\rho_j u,\rho_j u)
 =\operatorname{Re}(p_j(x,D)\rho_j u,\rho_j u)
 \ge -CR_j^{-2}\|\rho_j u\|_2^2
 \tag{P12}
\]
by Lemma 3. Summing the error magnitudes gives at most $C\|X^{-1}u\|_2^2$.

It remains to justify the localization with this same weighted error. Let $K_a(x,y)$ denote the off-diagonal left kernel. For $h=x-y\ne0$, apply the same radial telescoping construction as in (P11) to the frequency variable, using the functions $\psi_k$ before square normalization. This frequency partition gives
\[
 |K_a(x,y)|\le C X^{-1}
 \begin{cases}
 |h|^{-n},&0<|h|\le1,\\
 |h|^{-L},&|h|\ge1,
 \end{cases}
 \tag{P13}
\]
for any fixed $L>n$, with a finite-seminorm constant. To verify this, a frequency piece with $|\xi|$ comparable to $\lambda=2^k$ has kernel bounded by
$C X^{-1}\lambda^n(1+\lambda|h|)^{-2N_1}$.
Indeed its derivatives of order $\beta$ are bounded by $CX^{-1}\lambda^{-|\beta|}$, and integration by parts with $(1-\lambda^2\Delta_\xi)^{N_1}$ gives that bound. The low-frequency piece has the same bound with $\lambda=1$. For $|h|\le1$, sum separately over $\lambda\le |h|^{-1}$ and $\lambda>|h|^{-1}$; both geometric sums are $O(|h|^{-n})$ when $2N_1>n$. For $|h|\ge1$, choose $2N_1\ge L>n$ and sum $\lambda^{n-2N_1}|h|^{-2N_1}$. The same bounds hold for every finite partial sum of the frequency partition.

The difference $E=A-\sum_j\rho_j A\rho_j$, initially in Schwartz quadratic forms, has kernel multiplier
\[
 m(x,y)=1-\sum_j\rho_j(x)\rho_j(y)
 =\frac12\sum_j(\rho_j(x)-\rho_j(y))^2.
 \tag{P14}
\]
It satisfies $|m|\le2$. If $|h|\le X/2$, the Lipschitz inequality $|\langle x\rangle-\langle y\rangle|\le|x-y|$ makes all weights along the segment comparable to $X$. Only a fixed number of supports can meet that segment, and (P11) gives
$|m(x,y)|\le C|h|^2X^{-2}$.

Consider the weighted kernel $XK_a(x,y)m(x,y)Y$, with $Y=\langle y\rangle$. For $|h|\le1$ and $|h|\le X/2$, (P13) bounds it by $C|h|^{2-n}$. For $|h|\ge1$ but $|h|\le X/2$, it is bounded by $C|h|^{2-L}$. In the remaining region $|h|>X/2$ one has $X\le2|h|$, $Y\le3|h|$ and $|h|>1/2$. The same kernel is bounded by a fixed constant on $1/2<|h|<1$, and by $C|h|^{1-L}$ on $|h|\ge1$. Choosing $L>n+2$ gives an integrable majorant depending only on $h$. Thus its row and column integrals are uniformly bounded. The proved Schur estimate yields
\[
 |(Eu,u)|\le C\|X^{-1}u\|_2^2.
 \tag{P15}
\]

For completeness there is no unexamined diagonal distribution in this argument. First replace $a$ by a finite partial sum of the frequency partition. Its kernel is an ordinary smooth function, and (P13)–(P15) hold uniformly. The factor (P14) cancels the near-diagonal singularity by two powers of $|h|$. The integrable weighted majorant therefore permits passage to the limit in the error form. The left-operator forms converge on Schwartz inputs by the defining Fourier integral and dominated convergence. The partitioned forms converge too: the finite-derivative $L^2$ bound is uniform in the frequency cutoff, so their tails are bounded by a constant times $\sum_{j>J}\|\rho_j u\|_2^2$, which tends to zero. These facts prove the exact limiting form identity defining $E$ and (P15).

Now sum (P12), add (P15), and use (P11) to obtain (P2) on Schwartz space. The left finite-derivative theorem bounds $A$ on $L^2$ since (P1) bounds all its required derivatives. Schwartz density, and boundedness of multiplication by $X^{-1}$, extend (P2) to all of $L^2$. Every error above uses a fixed finite derivative list once the dimension is fixed, proving the asserted uniformity. This completes Theorem 1.

<a id="rotated-negative-order"></a>
## Fourier form and the exact negative order

For $b(y,\eta)=a(-\eta,y)$, direct insertion of the two unitary Fourier transforms gives
$\mathcal F a(x,D)\mathcal F^{-1}=\operatorname{Op}_{\mathrm{right}}(b)$.
Because $b$ is real, its adjoint is $\operatorname{Op}_{\mathrm{left}}(b)$; the two have the same real quadratic form. Theorem 1 is therefore equivalently
\[
 \operatorname{Re}(\operatorname{Op}_{\mathrm{left}}(b)w,w)
 \ge-C\|w\|_{H^{-1}}^2,
 \quad
 |\partial_y^\beta\partial_\eta^\alpha b|
 \le C_{\alpha\beta}\langle\eta\rangle^{-1-|\alpha|}\langle y\rangle^{-|\beta|}.
 \tag{P16}
\]
Plancherel gives $\|\mathcal Fu\|_{H^{-1}}=\|X^{-1}u\|_2$. The symbol's frequency order here is $-1$ and the error is the square of the $H^{-1}$ norm. These are distinct orders. Theorem 1, rather than an external citation, proves precisely this full rotated class, including the class used in the resolvent lesson's fourth exercise.

<a id="high-frequency-norm"></a>
## A uniform norm when frequency derivatives are small

The same packet construction also proves the precise high-frequency norm estimate needed by the smooth elliptic-domain argument. It permits complex symbols and keeps the leading supremum separate from the derivative constants.

**Theorem 4.** Suppose $R\ge1$, $a$ is a smooth complex scalar symbol, and
\[
 \sup|a|\le M,\qquad
 |\partial_x^\alpha\partial_\xi^\beta a|
      \le A_{\alpha\beta}R^{-|\beta|}.
 \tag{P17}
\]
Then
\[
 \|\operatorname{Op}_L(a)\|_{2\to2}\le M+C/R.
 \tag{P18}
\]
Here $C$ uses only a fixed finite list of the constants $A_{\alpha\beta}$ and is independent of $R$. Consequently a uniformly bounded family of classical order-zero symbols vanishing on $|\xi|<R$ has norm at most $M+C/R$, if their suprema are at most $M$. In particular its norm is at most $M+\sqrt{C'/R}$ for a suitable constant $C'$ and every $R\ge1$.

**Proof.** Use the width $r=R^{-1/2}$ packets of Lemma 3. Their normalized analysis map $W_r$ is an isometry, by the already proved packet identity. For a complex symbol define $Q_r(a)=W_r^*\mathcal M_aW_r$, where $\mathcal M_a$ multiplies a phase-space function by $a$. The definition and $\|W_r\|=\|W_r^*\|=1$ give $\|Q_r(a)\|\le M$; nonnegativity is not needed for this norm bound. The kernel computation (P7)–(P8), which is linear in the symbol, still gives the Weyl symbol $a*G_r$.

Taylor expansion with zero Gaussian first moments, separately in the two variable groups, now gives, for each fixed $\alpha,\beta$,
\[
 \|\partial_x^\alpha\partial_\xi^\beta(a*G_r-a)\|_\infty
 \le C_{\alpha\beta}
       \bigl(r^2R^{-|\beta|}+r^{-2}R^{-|\beta|-2}\bigr)
 \le C'_{\alpha\beta}/R.
 \tag{P19}
\]
The input second position derivatives are bounded by (P17), and the second frequency derivatives gain $R^{-2}$; convolution cannot increase their suprema. Lemma 2 bounds the corresponding Weyl difference by $C/R$. The exact left-minus-Weyl amplitude (P10), with $p$ replaced by $a$, has every required derivative bounded by $C/R$, since it contains one frequency derivative of $a$. Lemma 2 bounds this difference by $C/R$ too. Combining them proves $\|\operatorname{Op}_L(a)-Q_r(a)\|\le C/R$, and hence (P18). The cutoff justification in Lemmas 2–3 applies equally to complex amplitudes.

For the last assertion, the ordinary order-zero bound is $|\partial_x^\alpha\partial_\xi^\beta a|\le C_{\alpha\beta}\langle\xi\rangle^{-|\beta|}$. On the nonzero derivative supports, $|\xi|\ge R$; all derivatives vanish on the open ball and by continuity have the same bound on its boundary. Thus (P17) holds. Increasing the constant if necessary, $C/R\le\sqrt{C^2/R}$ for $R\ge1$, proving the stated square-root version. All constants use finite derivative lists; in particular only $M$ needs to be independent of a separately fixed coefficient approximation. $\square$

## Why the two packet scales differ

In Lemma 3 the position and frequency errors in (P9) are $r^2R^{-3}$ and $r^{-2}R^{-1}$. Equating them gives $r^2=R$ and error $R^{-2}$, which matches the weighted lower bound after spatial localization. In Theorem 4 the corresponding errors are $r^2$ and $r^{-2}R^{-2}$. Their balance gives $r^2=R^{-1}$ and error $R^{-1}$.

In both cases the positive packet operator is controlled directly by the isometry. For real nonnegative symbols this gives the sign; for complex symbols it preserves coefficient one in front of the supremum $M$. The two-position amplitude bound then controls the Gaussian-convolution error and the exact change from Weyl to left quantization at the appropriate scale.
