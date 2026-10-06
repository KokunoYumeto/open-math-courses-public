# Elementary calculus for infinite products

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Public domain (CC0).*

We work in a real ordered field with the least-upper-bound property, together with ZFC and finite arithmetic. Complex numbers are pairs of reals. Limits and continuity have their epsilon definitions. The arguments below establish the scalar completeness, compactness and polynomial approximation used for one self-adjoint element of a C\*-algebra.

For a real scalar, \(|x|=\max(x,-x)\). Adding the inequalities \(-|x|\le x\le|x|\) proves the real triangle inequality; checking signs proves \(|xy|=|x||y|\). Applying the triangle inequality twice proves \(\big||x|-|y|\big|\le|x-y|\). These finite order facts will be used throughout.

## 1. Limits and scalar cutoffs

<a id="scalar-a"></a>

**Lemma A.** The natural numbers are unbounded in the real field. Every bounded increasing real sequence converges to its supremum. Every real Cauchy sequence converges.

**Proof.** If the natural numbers had supremum \(s\), some natural \(m\) would exceed \(s-1\); then \(m+1>s\), a contradiction. In particular, given \(d>0\) one can choose \(n\) with \(1/n<d\).

For a bounded increasing sequence \(a_n\), let \(a=\sup_n a_n\). For every \(\varepsilon>0\) some \(a_N>a-\varepsilon\), and \(a-\varepsilon<a_n\le a\) for \(n\ge N\). Decreasing sequences converge by negating this assertion.

Let \(x_n\) be Cauchy. It is bounded: all terms after a suitable \(N\) lie within distance one of \(x_N\), and the preceding set is finite. Choose strictly increasing \(n_j\) such that
\[
|x_n-x_{n_j}|<2^{-j}\qquad(n\ge n_j).
\]
Each increment \(d_j=x_{n_{j+1}}-x_{n_j}\) has absolute value at most \(2^{-j}\). Write \(d_j=d_j^+-d_j^-\), where \(d_j^+=\max(d_j,0)\) and \(d_j^-=\max(-d_j,0)\). The finite partial sums of each nonnegative series increase and are bounded by \(\sum_{j=1}^m2^{-j}=1-2^{-m}\le1\). They therefore converge by the assertion just proved. Telescoping shows that \(x_{n_j}\) converges to a real \(x\). For any fixed \(j\), all \(n\ge n_j\) satisfy
\[
|x_n-x|\le 2^{-j}+|x_{n_j}-x|.
\]
The right side tends to zero with \(j\); hence the original sequence converges to \(x\). The estimates \(2^j\ge j+1\) and \(1/(j+1)\to0\) justify every use of \(2^{-j}\to0\). A convergent sequence is Cauchy by the triangle inequality. \(\square\)

<a id="scalar-b"></a>

**Lemma B.** Every \(s\ge0\) has a unique nonnegative square root. The square-root function, absolute value, positive part, minimum and maximum of real scalars are continuous.

**Proof.** For \(s=0\) the square root is zero. For \(s>0\), start with \(b_0=\max(1,s)\) and define
\[
b_{j+1}=\frac12\left(b_j+\frac{s}{b_j}\right).
\]
We have \(b_0^2\ge s\). If \(b_j>0\) and \(b_j^2\ge s\), then
\[
b_{j+1}^2-s=\frac{(b_j^2-s)^2}{4b_j^2}\ge0,
\qquad 0<b_{j+1}\le b_j.
\]
Also \(b_j\ge s/b_0>0\), since \(s\le b_j^2\le b_0b_j\). By Lemma A the decreasing sequence converges to \(b\ge s/b_0\). The elementary identity
\[
u^{-1}-v^{-1}=\frac{v-u}{uv}
\]
shows continuity of inversion at every nonzero real scalar: in a sufficiently small neighbourhood of \(v\), \(|u|\ge|v|/2\). Thus passing to the defining identity gives \(b=(b+s/b)/2\), so \(b^2=s\). Nonnegative roots are unique because \(u^2-v^2=(u-v)(u+v)\).

For \(s\ge t\ge0\), put \(u=\sqrt s\) and \(v=\sqrt t\). Squaring preserves order on nonnegative scalars, so \(u\ge v\), and
\[
(u-v)^2\le(u-v)(u+v)=s-t.
\]
Consequently \(|\sqrt s-\sqrt t|\le\sqrt{|s-t|}\); taking \(|s-t|<\varepsilon^2\) proves continuity even at zero. The real triangle inequality gives \(\big||s|-|t|\big|\le|s-t|\). Finally
\[
\max(s,t)=\frac{s+t+|s-t|}{2},\qquad
\min(s,t)=\frac{s+t-|s-t|}{2}
\]
and \(s^+=\max(s,0)\), so these functions are continuous. Addition and multiplication pass to limits by the triangle inequality and the identity \(uv-u'v'=u(v-v')+v'(u-u')\), using the boundedness of convergent scalars. \(\square\)

<a id="scalar-c"></a>

**Lemma C.** Complex addition is componentwise: \((x,y)+(u,v)=(x+u,y+v)\), with additive identity \((0,0)\), multiplicative identity \((1,0)\) and \(i=(0,1)\). With
\[
(x,y)(u,v)=(xu-yv,xv+yu),\qquad
\overline{(x,y)}=(x,-y),\qquad |(x,y)|=\sqrt{x^2+y^2},
\]
the complex field is complete. Its modulus is multiplicative and satisfies the triangle inequality. Polynomial and rational functions are continuous wherever their denominators are nonzero.

**Proof.** The field identities follow by expansion in the real field. The inverse of a nonzero \(z=(x,y)\) is \(\bar z/(x^2+y^2)\). Expansion gives \(|zw|^2=|z|^2|w|^2\); uniqueness of the nonnegative root gives multiplicativity. Since \(|\operatorname{Re}z|\le|z|\),
\[
|z+w|^2=|z|^2+2\operatorname{Re}(z\bar w)+|w|^2
\le (|z|+|w|)^2.
\]
This proves the triangle inequality. Real and imaginary coordinate distances are bounded by the complex distance, while the complex distance is at most their sum. A complex Cauchy sequence therefore has two real Cauchy coordinate sequences; their limits from Lemma A give its complex limit. The preceding inequalities, the product identity in Lemma B and the reciprocal identity prove the asserted limit and continuity rules. Composition preserves continuity directly from its epsilon definition. \(\square\)

## 2. Compact sets and continuous functions

Use the maximum-coordinate metric \(d(x,y)=\max_j|x_j-y_j|\) on \(\mathbb R^d\). An open cover of a subset of \(\mathbb R^d\) is a family of ambient-open sets whose union contains it. Open means that each point has a small open coordinate box lying in the set. A set open relative to \(K\) has the form \(K\cap O\) with \(O\) ambient-open. A set is closed when its complement is ambient-open; it is compact when every ambient-open cover has a finite subcover. In a general metric target use the same definitions with metric-open balls. Empty sets satisfy the finite-cover, boundedness and uniform-continuity assertions without further choices.

<a id="scalar-d"></a>

**Lemma D.** Every closed bounded subset of \(\mathbb R^d\) has a finite subcover from each open cover. A continuous map from such a set into any metric space is uniformly continuous; its image is bounded. A real continuous function on a nonempty such set attains its minimum and maximum.

**Proof.** First consider a closed interval \([a,b]\) and an open cover. If \(a=b\), one cover member suffices. Otherwise let \(S\) consist of the points \(t\in[a,b]\) for which \([a,t]\) has a finite subcover. An open cover member at \(a\) shows that \(S\) is nonempty and extends a positive distance past \(a\). Let \(c=\sup S\). A cover member containing \(c\) contains \((c-\eta,c+\eta)\) for some \(\eta>0\). Choose \(t\in S\) with \(t>c-\eta/2\). Adding that member to a finite cover of \([a,t]\) covers \([a,\min(b,c+\eta/2)]\). If \(c<b\), this contradicts the definition of \(c\). If \(c=b\), it gives a finite cover of all \([a,b]\).

Finite products of intervals also have the finite-cover property. Here is an induction proof. Assume a compact box \(K\) has that property and cover \(K\times[a,b]\) by open sets. For fixed \(x\in K\), compactness of \([a,b]\) supplies finitely many open product neighbourhoods \(U_j\times V_j\), each lying in one cover member, whose \(V_j\)'s cover \([a,b]\). Their finitely many \(U_j\)'s have an open intersection \(U_x\) containing \(x\); the chosen cover members then cover \(U_x\times[a,b]\). Finitely many of these \(U_x\)'s cover \(K\), giving finitely many members of the original cover. Degenerate coordinate intervals cause no change. A closed subset \(F\) of a compact box is compact: add its open complement to an open cover of \(F\), take a finite cover of the box, and discard the complement. Bounded sets lie in a finite box, proving the first assertion.

Let \(f:K\to Y\) be continuous, where \(Y\) is metric. For \(\varepsilon>0\), choose for every \(x\in K\) a radius \(r_x>0\) such that
\[
d(y,x)<2r_x,\quad y\in K\quad\Longrightarrow\quad
d_Y(f(y),f(x))<\varepsilon/2.
\]
Finitely many balls \(B(x_j,r_{x_j})\) cover \(K\). Put \(\delta=\min_j r_{x_j}>0\). If \(d(y,z)<\delta\), choose a covering ball containing \(y\). Both \(y\) and \(z\) lie within \(2r_{x_j}\) of its centre, and the image triangle inequality gives \(d_Y(f(y),f(z))<\varepsilon\). This proves uniform continuity. Continuity similarly gives a finite collection of image balls of radius one covering \(f(K)\); their distances to any fixed one of their centres have a finite maximum, proving boundedness.

Continuous images preserve the finite-cover property by pulling back a cover. To justify the relative-domain step, if \(V\) is open in the metric target, continuity at each \(x\in f^{-1}(V)\) gives an ambient-open ball \(B_x\) with \(K\cap B_x\subseteq f^{-1}(V)\). The union \(O_V=\bigcup_{x\in f^{-1}(V)}B_x\) is ambient-open and \(K\cap O_V=f^{-1}(V)\). Thus a target cover pulls back to an ambient-open cover of \(K\), to which its finite-cover property applies. A compact subset \(E\) of a metric space is closed: for \(y\notin E\), the balls \(B(x,d(x,y)/3)\), \(x\in E\), have a finite subcover; a sufficiently small ball about \(y\), using the minimum of these finitely many positive distances, misses all of them. A closed set contains the limit of every convergent sequence in it: otherwise an open ball in its complement about the limit would contain all sufficiently late terms, a contradiction. A nonempty bounded closed subset of \(\mathbb R\) contains its supremum and infimum. Indeed, the supremum can be approached by elements within \(1/n\); a closed set contains that limit, and likewise for the infimum. Apply these facts to the compact image of a real continuous function. Norms of continuous normed-space-valued functions are continuous by \(|\|u\|-\|v\||\le\|u-v\|\), so they attain maxima as well. \(\square\)

<a id="scalar-e"></a>

**Lemma E.** A continuous complex-valued function on a nonempty closed subset \(K\) of a compact real interval extends continuously to that interval, with unchanged supremum norm, by constant extension past the extreme points of \(K\) and linear interpolation on each intervening gap.

**Proof.** By Lemma D, \(K\) has a minimum \(a\) and maximum \(b\). If \(a=b\), use the constant value. For \(y\in(a,b)\setminus K\), the sets of points of \(K\) to its left and right have supremum \(l\) and infimum \(u\); closedness puts \(l,u\) in \(K\), with \(l<y<u\). There is no point of \(K\) between them, and define
\[
\widetilde f(y)=\frac{u-y}{u-l}f(l)+\frac{y-l}{u-l}f(u).
\]
This is well-defined, affine on a whole gap, and bounded in modulus by \(M=\max_K|f|\).

It remains to prove continuity at \(x\in K\). Given \(\varepsilon>0\), choose \(\eta>0\) such that \(|f(v)-f(x)|<\varepsilon/2\) for \(v\in K\) with \(|v-x|<2\eta\). Suppose \(|y-x|<\eta\) and \(y\) lies in a gap. Since \(x\) does not lie strictly between its endpoints, the endpoint \(v\) on the same side of the gap as \(x\) lies between \(x\) and \(y\), so \(|v-x|\le|y-x|\). If the other endpoint \(w\) satisfies \(|w-x|<2\eta\), both endpoint errors are less than \(\varepsilon/2\). Otherwise \(|w-v|\ge\eta\), and the weight of \(f(w)\) is \(|y-v|/|w-v|\le|y-x|/\eta\). Therefore
\[
|\widetilde f(y)-f(x)|\le\varepsilon/2+2M|y-x|/\eta.
\]
Taking \(|y-x|<\min(\eta,\varepsilon\eta/[4(M+1)])\) proves continuity. Points in \(K\) and the outer constant pieces satisfy the same conclusion directly. The norm is unchanged because the extension agrees on \(K\) and never exceeds \(M\). \(\square\)

## 3. Polynomial approximation from finite coin products

For \(t\in[0,1]\), assign to each binary string \(\omega=(\omega_1,\ldots,\omega_n)\) the weight
\[
q_t(\omega)=\prod_{j=1}^n
\begin{cases}t,&\omega_j=1,\\1-t,&\omega_j=0.\end{cases}
\]
This definition includes \(t=0,1\) and uses only finite sums and products. Write \(E_t g=\sum_\omega q_t(\omega)g(\omega)\) and \(Y(\omega)=n^{-1}\sum_j\omega_j\).

<a id="scalar-f"></a>

**Lemma F.** For \(n\ge1\),
\[
E_t1=1,\qquad E_tY=t,\qquad
E_t(Y-t)^2=\frac{t(1-t)}n\le\frac1{4n}.
\]
The total weight of strings with \(|Y-t|\ge\delta>0\) is at most \(1/(4n\delta^2)\).

**Proof.** Summing separately over every coordinate factors \(E_t1\) into \(n\) copies of \(t+(1-t)=1\). The same factorization gives \(E_t\omega_j=t\) and \(E_t(\omega_j-t)^2=t(1-t)\). If \(j\ne k\), summing first over those two coordinates gives
\[
E_t[(\omega_j-t)(\omega_k-t)]
=[t(1-t)+(1-t)(-t)]^2=0.
\]
Expanding the finite square of the sum therefore yields
\[
E_t(Y-t)^2=n^{-2}\sum_{j=1}^n t(1-t)=t(1-t)/n.
\]
The bound \(t(1-t)\le1/4\) is \((t-1/2)^2\ge0\). On the indicated set each squared deviation is at least \(\delta^2\), and all weights are nonnegative; summing gives the last assertion. \(\square\)

<a id="scalar-g"></a>

**Theorem G.** Every continuous complex function on a nonempty compact subset of the real line is uniformly approximable by complex polynomials.

**Proof.** First let \(f\) be continuous on \([0,1]\). By Lemma D it is bounded, say by \(M\), and uniformly continuous. Define the polynomial
\[
P_n(t)=E_t f(Y)=\sum_{\omega\in\{0,1\}^n}q_t(\omega)f(Y(\omega)).
\]
Group strings with \(k\) ones. Their number is \({n\choose k}\), since choosing the \(k\) positions determines the string (equivalently, Pascal's recursion with its endpoint counts proves this number). Thus
\[
P_n(t)=\sum_{k=0}^n{n\choose k}t^k(1-t)^{n-k}f(k/n).
\]
Given \(\varepsilon>0\), choose \(\delta>0\) such that \(|u-t|<\delta\) implies \(|f(u)-f(t)|<\varepsilon/2\). Splitting the finite sum into \(|Y-t|<\delta\) and its complement, Lemma F gives, uniformly in \(t\),
\[
|P_n(t)-f(t)|\le\varepsilon/2+\frac{2M}{4n\delta^2}.
\]
The Archimedean property makes the second term smaller than \(\varepsilon/2\) for all sufficiently large \(n\). This proves uniform approximation, without differentiation of binomial expressions or infinite-dimensional probability.

An affine change of variable treats every nondegenerate compact interval; a singleton needs only constants. For an arbitrary nonempty compact \(K\subset\mathbb R\), the open intervals \((-m,m)\), \(m\ge1\), cover it by the Archimedean property. A finite subcover makes \(K\) bounded. It is closed by the compact-metric-set argument in Lemma D. Lemma E therefore extends \(f\) to its bounding interval. Approximate the extension there and restrict the polynomials to \(K\). \(\square\)

The Bernstein probability viewpoint is discussed in Tiangang Cui and Friedrich Pillichshammer, [*Bernstein approximation and beyond: proofs by means of elementary probability theory*](https://arxiv.org/abs/2307.11533v1), Section 1. The finite product calculation above supplies its moments directly and applies to arbitrary continuous complex functions.

## 4. Intermediate values and scalar roots

<a id="scalar-h"></a>

**Lemma H.** A continuous real function on a compact interval takes every value between its endpoint values. Every \(c>0\) has a unique positive \(n\)-th root for \(n\ge1\), and \(c^{1/n}\to1\).

**Proof.** Subtract the desired value and, if necessary, negate the function, so \(f(a)<0<f(b)\); endpoint equalities already supply that value. Let \(S=\{t\in[a,b]:f(t)<0\}\) and \(s=\sup S\). Continuity at \(a\) puts elements of \(S\) strictly past \(a\), and continuity at \(b\) keeps \(S\) a positive distance below \(b\); thus \(a<s<b\). There are \(t_j\in S\) with \(s-1/j<t_j\le s\), so continuity gives \(f(s)\le0\). If \(f(s)<0\), continuity would put some \(t>s\) in \(S\), contradicting the supremum. Hence \(f(s)=0\).

The nonnegative \(n\)-th root of zero is zero, since a positive scalar has positive \(n\)-th power. The polynomial \(t^n\) is continuous by Lemma C. On nonnegative scalars it is strictly increasing: if \(v>u\ge0\), then
\[
v^n-u^n=(v-u)\sum_{j=0}^{n-1}v^{n-1-j}u^j>0.
\]
Apply the intermediate-value assertion on \([0,\max(1,c)]\) to obtain the unique positive root. For \(c\ge1\), its root is at least one. For every \(\varepsilon>0\), induction gives \((1+\varepsilon)^n\ge1+n\varepsilon\), which exceeds \(c\) for sufficiently large \(n\). Strict monotonicity gives \(1\le c^{1/n}<1+\varepsilon\). For \(0<c<1\), apply that conclusion to \(c^{-1}>1\) and use continuity of scalar inversion. \(\square\)

<a id="scalar-exponential"></a>

## 5. Exponential, logarithm and scalar powers

We construct the scalar functions used for the exponential germ and for the imaginary powers of positive eigenvalues. [Lemmas A–C](#1-limits-and-scalar-cutoffs) supply the Archimedean property, convergence of bounded monotone real sequences, complex Cauchy completeness and the elementary modulus inequalities. All series and limit arguments needed here are proved below.

<a id="exp-series"></a>

**Exponential series.** Set \(0!=1\), \(n!=1\cdot2\cdots n\) for \(n\ge1\), and
\[
P_N(z)=\sum_{n=0}^{N}\frac{z^n}{n!}.
\]
For every \(R>0\), choose an integer \(J\ge1\) with \(J>2R\). Writing \(b_n=R^n/n!\), we have
\[
b_{n+1}\le\tfrac12 b_n\quad(n\ge J),\qquad
b_{J+k}\le2^{-k}b_J\quad(k\ge0).
\]
The finite geometric identity gives \(\sum_{k=0}^{m}2^{-k}\le2\). Thus the partial sums of \(\sum b_n\) increase and are bounded by \(\sum_{n<J}b_n+2b_J\); Lemma A gives a finite limit, denoted \(B_R\). Moreover \(2^{-k}\to0\), because \(2^k\ge k+1\), and for \(M\ge J\)
\[
\sum_{n=M+1}^{\infty}\frac{R^n}{n!}
\le 2b_{M+1}\le2b_J2^{-(M+1-J)}\longrightarrow0. \tag{E1}
\]
Here each infinite nonnegative sum means the limit of its increasing finite partial sums; the inequality first holds for every finite sum and then passes to that limit.

For \(|z|\le R\), the complex triangle inequality bounds any finite tail of \(P_N(z)\) by the corresponding tail in (E1). Complex completeness therefore gives
\[
E(z)=\lim_{N\to\infty}P_N(z)=\sum_{n=0}^{\infty}\frac{z^n}{n!}.
\]
The error is bounded by (E1) uniformly for \(|z|\le R\); also \(\sum |z|^n/n!\le B_R\). This proves absolute convergence and uniform absolute convergence on every bounded disc. The disc of radius zero is the singleton \(\{0\}\), where \(E(0)=1\).

The function \(E\) is continuous. To verify the limit step explicitly at \(z_0\), fix \(R>|z_0|\). Given \(\varepsilon>0\), choose \(N\) so that \(|E(z)-P_N(z)|<\varepsilon/3\) throughout that disc. Polynomial continuity from Lemma C gives \(\delta>0\), reduced if necessary to keep \(|z|\le R\), such that \(|P_N(z)-P_N(z_0)|<\varepsilon/3\) when \(|z-z_0|<\delta\). The triangle inequality then gives \(|E(z)-E(z_0)|<\varepsilon\).

<a id="exp-law"></a>

**Addition, conjugation and differentiation.** For fixed \(z,w\), the finite binomial identity yields
\[
P_N(z+w)=\sum_{k+l\le N}\frac{z^kw^l}{k!l!}. \tag{E2}
\]
For clarity, that identity follows by induction: multiplying \((z+w)^n\) by \(z+w\) combines the coefficients according to \({n\choose k}+{n\choose k-1}={n+1\choose k}\), which is the factorial identity after taking a common denominator. Its endpoint coefficients are one.

The rectangular product \(P_N(z)P_N(w)\) differs from the finite triangular sum in (E2) only in terms with \(0\le k,l\le N\) and \(k+l>N\). Put \(m=\lfloor N/2\rfloor\). Every such term has \(k>m\) or \(l>m\). If \(B_z=\sum_{k\ge0}|z|^k/k!\) and \(B_w=\sum_{l\ge0}|w|^l/l!\), already proved finite, then
\[
|P_N(z)P_N(w)-P_N(z+w)|
\le B_w\sum_{k>m}\frac{|z|^k}{k!}
   +B_z\sum_{l>m}\frac{|w|^l}{l!}
\longrightarrow0. \tag{E3}
\]
This estimate uses only finite sums and their nonnegative majorants. Passing to the limits, using the elementary product limit rule of Lemma C, proves
\[
E(z+w)=E(z)E(w). \tag{E4}
\]
Conjugating each finite polynomial gives \(\overline{P_N(z)}=P_N(\bar z)\). Since conjugation preserves distances, passage to limits gives
\[
\overline{E(z)}=E(\bar z).
\]
Taking \(w=-z\) in (E4) gives \(E(z)E(-z)=E(0)=1\); hence \(E(z)\ne0\) and \(E(-z)=E(z)^{-1}\). Repeated addition and this inverse identity give \(E(nz)=E(z)^n\) for every integer \(n\), positive, zero or negative.

We can differentiate without a theorem on differentiation of infinite series. For \(n\ge1\), the inequality \(n!\ge2^{n-1}\) follows by induction, since every added factor is at least two. The finite geometric sums consequently give \(\sum_{n\ge2}1/n!\le1\). For \(|h|\le1\), taking limits in the finite remainder bounds gives
\[
|E(h)-1-h|\le\sum_{n\ge2}\frac{|h|^n}{n!}\le |h|^2. \tag{E5}
\]
Thus \((E(h)-1)/h\to1\) as the nonzero complex increment \(h\to0\). By (E4),
\[
\frac{E(z+h)-E(z)}h
=E(z)\frac{E(h)-1}h\longrightarrow E(z).
\]
Therefore \(E\) is complex differentiable everywhere and \(E'=E\); its derivative is continuous because \(E\) is continuous. Restricting increments to the real line proves the corresponding real derivative. We write \(e^z=E(z)\).

The derivative also characterizes the normalized real-parameter exponential. We first justify the elementary zero-derivative step. For a real continuous \(u\) on \([a,b]\), differentiable on \((a,b)\) with \(a<b\), subtract the chord joining its endpoint values. The resulting function has equal zero endpoint values and attains its maximum and minimum by [Lemma D](#2-compact-sets-and-continuous-functions). If it is not identically zero, one nonzero extreme is attained in the interior; if it is zero, any interior point suffices. The derivative at an interior maximum is zero: the difference quotient is nonpositive for positive increments and nonnegative for negative increments, so its common limit is zero. Negating treats a minimum. Restoring the chord proves that some interior derivative equals \((u(b)-u(a))/(b-a)\). In particular, if \(u'=0\), the endpoint values are equal. Applying this on every compact interval shows that \(u\) is constant.

Now let \(f:\mathbb R\to\mathbb C\) be differentiable with \(f'=f\) and \(f(0)=1\). Differentiability implies continuity directly: \(f(x+h)-f(x)\) is \(h\) times a difference quotient with finite limit, and hence tends to zero. For \(g(x)=f(x)E(-x)\), split its difference quotient as
\[
\frac{f(x+h)-f(x)}h E(-x-h)
+f(x)\frac{E(-x-h)-E(-x)}h.
\]
The second quotient tends to \(-E(-x)\), by the already proved derivative with increment \(-h\). The first term tends to \(f'(x)E(-x)\), so \(g'=0\). Taking real and imaginary parts preserves these derivative limits, and the zero-derivative result makes both parts constant. Thus \(g(x)=g(0)=1\), and the inverse identity gives \(f(x)=E(x)\).

<a id="real-logarithm"></a>

**The real exponential and its inverse.** Conjugation shows that \(E(x)\) is real for real \(x\). If \(x\ge0\), its partial sums are nonnegative and \(E(x)\ge1+x>0\). If \(x<0\), then \(E(x)=1/E(-x)>0\). For \(y>x\), (E4) and \(E(y-x)\ge1+(y-x)>1\) give
\[
E(y)=E(x)E(y-x)>E(x).
\]
Hence the real exponential is strictly increasing. The bound \(E(x)\ge1+x\) for \(x\ge0\) proves \(E(x)\to\infty\) as \(x\to\infty\). Its reciprocal identity gives
\[
0<E(-x)\le\frac1{1+x}\longrightarrow0\quad(x\to\infty). \tag{E6}
\]
The last limit follows directly from the Archimedean property: for \(\varepsilon>0\), choose \(x>1/\varepsilon\).

We prove that every \(q>0\) occurs. Choose \(b>\max(q,q^{-1},1)\). Then \(E(-b)<q<E(b)\). Let
\[
S=\{x\in[-b,b]:E(x)\le q\},\qquad s=\sup S.
\]
The set is nonempty and bounded. For each \(n\ge1\), the definition of supremum gives \(x_n\in S\) with \(s-1/n<x_n\le s\). Then \(x_n\to s\), and continuity gives \(E(s)\le q\); a limit larger than \(q\) would put all sufficiently late values above \(q\), contrary to \(x_n\in S\). In particular \(s<b\). If \(E(s)<q\), continuity gives a small \(h>0\), with \(s+h\le b\), for which \(E(s+h)<q\). This places \(s+h\) in \(S\) and contradicts its supremum. Thus \(E(s)=q\). Strict increase gives uniqueness.

Define \(\log q\) to be this unique real \(s\). It is strictly increasing and continuous on \((0,\infty)\). Indeed, let \(x=\log q\) and \(\varepsilon>0\). The positive number
\[
\delta=\min\{q-E(x-\varepsilon),\ E(x+\varepsilon)-q\}
\]
has the property that \(r>0\) and \(|r-q|<\delta\) imply
\(E(x-\varepsilon)<r<E(x+\varepsilon)\). Strict increase then gives
\(|\log r-\log q|<\varepsilon\). This proves continuity directly, without an inverse-function theorem.

The inverse identities and (E4) give, by uniqueness,
\[
\log1=0,\qquad \log(qr)=\log q+\log r,
\qquad \log(q^{-1})=-\log q. \tag{E7}
\]
For example \(E(\log q+\log r)=qr\), so the left input is exactly \(\log(qr)\).

<a id="scalar-powers"></a>

**Positive and imaginary scalar powers.** For \(\lambda>0\) and real \(s,t\), set
\[
\lambda^s=E(s\log\lambda),\qquad
\lambda^{it}=E(it\log\lambda).
\]
Real positivity gives \(\lambda^s>0\). The addition law and (E7) give
\[
\lambda^{s+u}=\lambda^s\lambda^u,
\quad (\lambda^s)^u=\lambda^{su},
\quad (\lambda\mu)^s=\lambda^s\mu^s,
\quad (\lambda^{-1})^s=\lambda^{-s} \tag{E8}
\]
for real \(s,u\) and \(\mu>0\). In the second identity use
\(\log(\lambda^s)=s\log\lambda\), which follows by the uniqueness defining the logarithm. For integer \(s\), these powers agree with ordinary repeated products and their inverses, since \(\lambda^0=1\) and \(\lambda^1=\lambda\). The value \(\lambda^{1/2}\) is positive and squares to \(\lambda\), so it is the unique positive square root proved in [Lemma B](#1-limits-and-scalar-cutoffs).

For imaginary powers, conjugation and (E4) show
\[
\overline{\lambda^{it}}=\lambda^{-it},\qquad
|\lambda^{it}|^2=E(it\log\lambda)E(-it\log\lambda)=1.
\]
The modulus is nonnegative, hence \(|\lambda^{it}|=1\). The same identities prove
\[
\lambda^{i(t+u)}=\lambda^{it}\lambda^{iu},\qquad
\lambda^{i0}=1,\qquad
(\lambda^{-1})^{it}=\lambda^{-it},\qquad
(\lambda\mu)^{it}=\lambda^{it}\mu^{it}. \tag{E9}
\]
The map \(t\mapsto\lambda^{it}\) is continuous, since its input \(it\log\lambda\) is continuous and \(E\) is continuous. An explicit estimate, useful for these groups, follows from (E5): if \(|h\log\lambda|\le1\), then
\[
|\lambda^{i(t+h)}-\lambda^{it}|
=|E(ih\log\lambda)-1|
\le |h\log\lambda|+|h\log\lambda|^2. \tag{E10}
\]
This also covers \(\lambda=1\), when every term is constant. For \(\lambda\ne1\), dividing the addition-law difference by \(h\) and using the proved derivative at zero gives
\(\frac{d}{dt}\lambda^{it}=i\log\lambda\,\lambda^{it}\); for \(\lambda=1\) both sides are zero. Continuity in the positive base follows from the continuity of \(\log\), scalar multiplication and \(E\). Thus the scalar powers used in diagonal modular formulas have their group, modulus, reciprocal and continuity properties with no operator spectral input.

<a id="r00"></a>

## R00. Setting and notation

We work in ZFC over an ordered field of real numbers in which every nonempty bounded above set has a least upper bound, and use its complex extension `C = R + iR`, with `i² = -1`. A complex Banach space is a complex normed vector space complete for its norm metric. A unital complex Banach algebra is such a space with associative multiplication, a nonzero identity, a submultiplicative norm, and `||1|| = 1`.

An oriented line integral below means a sum of ordinary continuous Banach valued integrals on finitely many line segments. A positively oriented rectangle is traversed along its bottom edge from left to right, right edge from bottom to top, top edge from right to left, and left edge from top to bottom. All rectangles have positive side lengths. Every contour in this provider is a finite list of these axis parallel segments; a list can contain more than one boundary component. Equality of contours used here means equality after cancellation of oppositely oriented identical segments, with subdivisions of a segment permitted.

For clarity we use the name **complex differentiable with continuous derivative** for a function `f` from an open subset of `C` to a complex Banach space for which the norm limit

\[
 f'(z)=\lim_{h\to0,\ h\in\mathbb C}\frac{f(z+h)-f(z)}h
\]

exists at every point and is norm continuous. The proof never assumes that an arbitrary complex differentiable function automatically has a continuous derivative. The actual functions used later have continuous derivatives by explicit algebraic estimates.

<a id="r01"></a>

## R01. Real limits, roots and the complex modulus

**Archimedean property and rational approximation.** The positive integers are unbounded. Otherwise their supremum `s` would satisfy `n <= s-1` for every integer `n`, because `n+1 <= s`; this contradicts minimality of `s`. Therefore `1/n -> 0`, and for any positive real `epsilon` there is an integer `n` with `1/n < epsilon`. The same fact supplies rational approximations: for real `u < v`, choose `n` with `n(v-u)>1`; among integers greater than `nu`, the smallest exists by translating to a nonempty subset of the nonnegative integers. Call it `m`. Then `nu < m <= nu+1 < nv`, so `m/n` lies strictly between `u` and `v`.

**Monotone limits and completeness.** A bounded increasing sequence converges to its supremum: for any positive `epsilon` one term exceeds `s-epsilon`, and all subsequent terms lie between that term and `s`. The decreasing case follows by negation. A real Cauchy sequence is bounded. For its tail let `u_N = sup {x_n:n>=N}` and `l_N = inf {x_n:n>=N}`. These exist, `u_N` decreases, `l_N` increases, and the Cauchy condition gives `u_N-l_N -> 0`. Their limits therefore agree, and `l_N <= x_n <= u_N` for `n>=N` proves convergence. Consequently `C`, with its coordinate metric, is complete as well.

**Geometric series.** If `0 <= q < 1`, then `q^n -> 0`. For `q>0`, put `d=1/q-1>0`; induction gives `(1+d)^n >= 1+nd`, hence `q^n <= 1/(1+nd) -> 0`. The case `q=0` is immediate for `n>=1`. The finite identity `(1-q) sum_{j=0}^N q^j = 1-q^{N+1}` now gives

\[
 \sum_{j=0}^{\infty}q^j=(1-q)^{-1},\qquad
 \sum_{j=N+1}^{\infty}q^j=q^{N+1}(1-q)^{-1}.
\]

**Positive roots.** For `a>=0` and integer `n>=1`, there is a unique nonnegative number `b` with `b^n=a`. For `a=0` take `b=0`. Otherwise take the supremum of `{t>=0:t^n<=a}`, a nonempty set bounded above, for example by `a+1`. Finite multiplication is continuous, because the identity

\[
 u^n-v^n=(u-v)\sum_{j=0}^{n-1}u^{n-1-j}v^j
\]

shows continuity locally on a bounded interval. If `b^n<a`, a sufficiently small positive increment keeps the power below `a`, contradicting the supremum. If `b^n>a`, a sufficiently small positive decrement still has power above `a`; then every member of the set is below that decrement, again contradicting the supremum. Strict increase of positive powers proves uniqueness and root order. In particular square roots exist.

For every fixed `K>0`, `K^(1/n) -> 1`. If `K>=1`, then for every `epsilon>0`, `(1+epsilon)^n >= 1+n epsilon > K` eventually, so `1 <= K^(1/n)<1+epsilon`. If `0<K<1`, apply this conclusion to `1/K` and take reciprocals. All limit operations just used follow from the identities for sums, products and reciprocals and the defining epsilon estimates; a reciprocal limit requires its limit to be nonzero.

For `z=u+iv` set `|z|=(u²+v²)^(1/2)`. Expansion gives `|zw|=|z||w|`. The identity

\[
 (u^2+v^2)(s^2+t^2)-(us+vt)^2=(ut-vs)^2\ge0
\]

gives `us+vt <= |u+iv||s+it|`; expanding `|z+w|²` and using root order proves the triangle inequality. Thus this modulus is a norm, equivalent to the coordinate metric: each coordinate is bounded by `|z|`, and `|z|` is at most the sum of their absolute values. In particular a square of side `h` has diameter at most `sqrt(2) h`, and the distance from any point of the boundary of the square `[-S,S]+i[-S,S]` to zero is at least `S` and at most `sqrt(2) S`.

<a id="r02"></a>

## R02. Compact intervals and rectangles

A nested sequence of nonempty closed intervals whose lengths tend to zero has exactly one common point. Indeed the left endpoints increase and are bounded by every right endpoint. Their supremum lies in all the intervals; the decreasing right endpoints have the same limit because the lengths tend to zero. Uniqueness follows from those lengths.

Every bounded sequence of real numbers has a convergent subsequence. Start with a closed interval containing all its terms. Bisect it and choose one half containing infinitely many terms; repeat. Choose successively increasing indices with terms in the selected nested halves. Their distance to the unique common point is at most the interval length, so this subsequence converges. Applying this twice to the coordinates proves the same assertion for a bounded sequence in a closed rectangle in `C`. Limits remain in the rectangle because its defining coordinate inequalities are closed. The corresponding assertion for any finite product of real intervals follows by successively taking subsequences in each coordinate.

A closed interval has the finite open cover property. If an open cover had no finite subcover, bisect the interval and retain a half with no finite subcover. Its nested halves have a common point. One open member containing that point also contains a small interval around it, and hence contains a sufficiently small retained half. This is a contradiction. Replacing bisection by subdivision into four equal subrectangles proves the finite open cover property for a closed rectangle: if all four subrectangles had finite subcovers so would their union; the chosen nested subrectangles have a unique common point by the coordinate result. The same argument works for finite boxes.

Let `f` be a continuous function from such a compact interval or rectangle to a normed space. It is bounded: otherwise choose points with `||f||` tending to infinity, take a convergent subsequence of the points, and use continuity to obtain bounded values on that subsequence. It is uniformly continuous: failure would give `epsilon>0` and pairs of points of distance tending to zero with image distance at least `epsilon`; a convergent subsequence of the first points makes both sequences converge to the same point, contradicting continuity. Every real continuous function on such a domain attains its supremum and infimum. For the supremum, take points with values tending to the finite supremum and use a convergent subsequence. The proof for the infimum is the same. A closed bounded subset of `C` has these sequential consequences, because it lies in a rectangle and contains the limits of its convergent sequences.

These arguments also justify every maximum of a continuous norm on a segment or on finitely many segments used below. No infinite dimensional closed bounded set is claimed compact.

<a id="r03"></a>

## R03. Continuous tagged integrals in a Banach space

Let `E` be a real or complex Banach space and `f:[a,b]->E` continuous, with `a<b`. For a partition `a=t_0<...<t_m=b` and tags `xi_j in [t_{j-1},t_j]`, its tagged sum is

\[
 S(f;P,\xi)=\sum_{j=1}^{m}(t_j-t_{j-1})f(\xi_j).
\]

Its mesh is the largest subinterval length. Put `omega(delta)=sup {||f(s)-f(t)||:|s-t|<=delta}`. Boundedness makes this finite, and uniform continuity gives `omega(delta)->0` as `delta` decreases to zero.

If a tagged partition is refined, choose arbitrary tags on the refined intervals. Each old tag and corresponding new tag are in one old subinterval, so the difference between the old sum and the refined sum has norm at most `(b-a) omega(mesh(P))`. For two tagged partitions, pass to their common refinement. Their sums therefore differ in norm by at most

\[
 (b-a)\bigl(\omega(\operatorname{mesh}(P))+
                    \omega(\operatorname{mesh}(Q))\bigr).
\]

Tagged dyadic sums have mesh tending to zero and are Cauchy. Completeness gives their limit `I`. The displayed estimate against a sufficiently fine dyadic sum then proves that all tagged sums tend to `I` as their mesh tends to zero. This defines `integral_a^b f`. Set the integral on a zero length interval to zero and reverse its sign when the limits are reversed.

Addition, scalar multiplication, and application of a bounded linear map commute with this integral: each assertion holds for every tagged sum, and the map or operation preserves norm limits. The triangle inequality gives

\[
 \left\|\int_a^b f(t)\,dt\right\|\le(b-a)\sup_{[a,b]}\|f(t)\|.
\]

Splitting a partition at `c` and adding the two resulting sums proves interval additivity. Constant functions have integral `(b-a)v`. If real `f>=0`, its tagged sums and its integral are nonnegative; hence `f>=d` gives integral at least `(b-a)d`. A uniform difference bound gives

\[
 \left\|\int_a^b f-\int_a^b g\right\|
       \le(b-a)\sup\|f-g\|.
\]

In particular uniformly convergent sequences of continuous functions can be integrated term by term, and a uniformly convergent series of continuous functions has integral equal to the sum of its term integrals. The uniform limit is continuous: fix an approximating continuous function whose uniform error is below one third of the desired tolerance, and apply continuity to that one function.

For an affine change `t=u+vs` with `v>0`, transformed partitions and tags give

\[
 \int_{\alpha}^{\beta} f(u+vs)v\,ds
       =\int_{u+v\alpha}^{u+v\beta}f(t)\,dt.
\]

Their meshes scale by `v`, so this equality follows directly from the sum definition. The case `v<0` follows by reversing the partition and the limits. These observations prove all real substitutions used below. For a directed segment from `z_0` to `z_1`, define

\[
 \int_{[z_0,z_1]}f(z)\,dz
    =\int_0^1 f(z_0+t(z_1-z_0))(z_1-z_0)\,dt.
\]

The segment estimate is its length times the supremum norm. Subdivision and reversal follow from the affine substitution rule. Translation and positive dilation of a closed polygon give the corresponding substitutions directly on its segments.

<a id="r04"></a>

## R04. The continuous fundamental theorem of calculus

If `f:[a,b]->E` is continuous, then `G(t)=integral_a^t f(s) ds` is differentiable at each interior point and has derivative `f(t)`. Indeed for nonzero real `h` with `t+h` in the interval,

\[
 \left\|\frac{G(t+h)-G(t)}h-f(t)\right\|
       \le\sup_{s\text{ between }t\text{ and }t+h}\|f(s)-f(t)\|\to0.
\]

The same estimate gives one sided derivatives at endpoints. In particular the derivative is continuous.

We also need the converse, for which a direct norm argument suffices. Let `H:[a,b]->E` be continuous and have derivative zero at every interior point. Suppose that for some `s` with `a<s<b` the number `D=||H(s)-H(a)||` is positive. Choose `epsilon>0` with `epsilon(s-a)<D`, for example `epsilon=D/(2(s-a))`. The continuous real function

\[
             F(t)=\|H(t)-H(a)\|-\epsilon(t-a)\quad(a\le t\le s)
\]

attains its maximum by R02. Its value at `s` is positive, while `F(a)=0`, so a maximizing point `c` lies in `(a,s]`. In particular `c` is an interior point of `[a,b]`, even if `c=s`. The derivative zero at `c`, taken through negative increments, gives for every sufficiently small positive `h` with `h<c-a`

\[
                \|H(c)-H(c-h)\|<\epsilon h/2.
\]

The norm triangle inequality now yields

\[
 \begin{aligned}
 F(c)-F(c-h)
 &=\|H(c)-H(a)\|-\|H(c-h)-H(a)\|-\epsilon h\\
 &\le\|H(c)-H(c-h)\|-\epsilon h
 <-\epsilon h/2<0.
 \end{aligned}
\]

This contradicts maximality of `F(c)`. Thus `H(s)=H(a)` at every interior `s`. Continuity at `b`, using interior points tending to `b`, gives `H(b)=H(a)` as well. The argument never differentiates a norm and never uses a norming functional, a scalar mean value theorem, or Hahn–Banach.

Let `G:[a,b]->E` be continuous with a continuous derivative on the interior that extends continuously to the closed interval. Subtract its integral primitive: `H(t)=G(t)-integral_a^t G'(u)du`. The first part of R04 shows that `H'=0` on the interior, and R03 shows that `H` is continuous at the endpoints. The just proved constant conclusion gives

\[
                  G(b)-G(a)=\int_a^bG'(t)\,dt.
\]

This argument works for real or complex Banach spaces. For a function with a complex primitive `P` whose derivative is continuous on an open neighborhood of a segment, it gives

\[
 \int_{[z_0,z_1]}P'(z)\,dz=P(z_1)-P(z_0).
\]

The chain rule along a segment follows from the definition of the complex derivative: divide the increment in `P` by the complex segment increment and multiply by its constant velocity. At a zero velocity both sides are zero. Consequently the integral of a derivative around a closed finite polygon is zero whenever the single valued primitive is defined and has a continuous derivative on open neighborhoods of its edges.

<a id="r05"></a>

## R05. Fubini for a continuous function on a rectangle

Let `F:[a,b] x [c,d]->E` be continuous. R02 makes it bounded and uniformly continuous. The function `y -> integral_a^b F(x,y) dx` is continuous, because its change in norm is at most `(b-a) sup_x ||F(x,y)-F(x,y')||`, tending to zero as `y'->y`. The corresponding assertion holds for integration first in `y`.

To compare the two iterated integrals, choose partitions and tags in both variables. Write the product sum

\[
 T=\sum_{j,k}\Delta x_j\Delta y_k F(\xi_j,\eta_k).
\]

For each fixed `y`, the inner `x` integral differs from its tagged `x` sum by at most `(b-a) omega(mesh_x)`, uniformly in `y`, where `omega` is the uniform modulus on the rectangle with the maximum coordinate distance. Integrating this error over `y` gives at most `(b-a)(d-c) omega(mesh_x)`. Replacing the outer integral of the finite `x` sum by its tagged `y` sum gives error at most `(b-a)(d-c) omega(mesh_y)`. Thus the `x` first iterated integral differs from `T` by a bound tending to zero when both meshes tend to zero. Exactly the same reasoning gives this bound for the `y` first iterated integral. Hence

\[
 \int_c^d\int_a^b F(x,y)\,dx\,dy
      =\int_a^b\int_c^d F(x,y)\,dy\,dx.
\]

This is the continuous Banach valued Fubini assertion actually used here; no measurable integration theorem is invoked.

<a id="r06"></a>

## R06. Rectangle cancellation from the fundamental theorem

Let `f` be complex differentiable with continuous derivative on an open neighborhood of a closed rectangle `Q=[a,b]+i[c,d]`. Regarding `f(x+iy)` as a two variable function, the definition of its complex derivative along real and imaginary increments gives

\[
 f_x(x,y)=f'(x+iy),\qquad f_y(x,y)=i f'(x+iy).
\]

These partial derivatives are continuous. The sum of the bottom and top edge integrals is

\[
 \int_a^b\bigl(f(x+ic)-f(x+id)\bigr)\,dx
     =-\int_a^b\int_c^d f_y(x,y)\,dy\,dx
\]

by R04 on each vertical interval. The sum of the right and left edge integrals is

\[
 i\int_c^d\bigl(f(b+iy)-f(a+iy)\bigr)\,dy
     =i\int_c^d\int_a^b f_x(x,y)\,dx\,dy.
\]

R05 and `f_y=i f_x` make these two expressions cancel. Therefore

\[
                  \int_{\partial Q}f(z)\,dz=0.
\]

For a finite collection of such rectangles the sum of their boundary integrals is zero. On common sides in a rectangular subdivision, opposite orientations cancel by R03. If one side is subdivided by the adjacent rectangles, interval additivity gives the same cancellation. This proves every deformation by a finite rectangular subdivision used below. We do not invoke a general contour deformation theorem.

<a id="r07"></a>

## R07. The nonzero square integral and the other integer powers

Let `Gamma_S` be the positively oriented square with vertices `-S-iS`, `S-iS`, `S+iS`, `-S+iS`, where `S>0`. Set

\[
 A=\int_0^1\frac{dt}{1+t^2},\qquad c=8iA.
\]

The integrand is continuous, and on `[0,1]` it is at least `1/2`, so `A>=1/2` and `c!=0` (in fact `|c|>=4`). The function is even; by the affine substitution rule its integral on `[-1,1]` is `2A`. Any odd continuous real function has zero integral on that symmetric interval, by the same rule and reversal.

Compute the unit square explicitly. On its right edge, `z=1+it`, `-1<=t<=1`, and

\[
 dz/z=(t+i)(1+t^2)^{-1}dt,
\]

whose integral is `2iA`. On its top edge, `z=t+i`, with `t` going from `1` to `-1`, and `dz/z=(t-i)(1+t²)^(-1)dt`; reversal gives `2iA`. On the left edge, `z=-1+it`, with `t` going from `1` to `-1`, and `dz/z=(t-i)(1+t²)^(-1)dt`; this again gives `2iA`. On the bottom edge, `z=t-i`, with `t` going from `-1` to `1`, and `dz/z=(t+i)(1+t²)^(-1)dt`, giving the last `2iA`. Adding gives

\[
                   \int_{\Gamma_1}\frac{dz}{z}=c.
\]

Positive dilation `z=Sw` cancels its factors in `dz/z`, so the integral on `Gamma_S` is the same `c`. Translation gives the same result for `dz/(z-w)` around a square centered at `w`. No value or definition of pi is needed.

For every integer `k!=-1`, the scalar function `z^(k+1)/(k+1)` is a primitive of `z^k` on `C\{0}`; for `k>=0` it is defined on all of `C`. For nonnegative powers the derivative follows by the finite power identity. For reciprocal, the identity

\[
 (z+h)^{-1}-z^{-1}=-h\bigl(z(z+h)\bigr)^{-1}
\]

gives derivative `-z^(-2)`, continuous off zero. Here is the complete product estimate used for this and later functions. If `Phi` is a bilinear product satisfying `||Phi(u,v)||<=D||u||||v||`, and `u,v` are complex differentiable, write `Delta u=u(z+h)-u(z)` and likewise for `v`. The product difference divided by `h` is

\[
 \Phi(\Delta u/h,v(z))+\Phi(u(z),\Delta v/h)
                         +\Phi(\Delta u/h,\Delta v).
\]

The first two terms converge to `Phi(u'(z),v(z))` and `Phi(u(z),v'(z))`. The norm of the third is at most `D||Delta u/h||||Delta v||`, which tends to zero because the first factor is bounded and the second tends to zero. When the derivatives are continuous, the displayed derivative is continuous as well. This covers scalar products, scalar multiplication of vectors, and Banach algebra products. Induction using this rule proves the derivative for every negative integer power. For a nowhere zero differentiable scalar function `p`, the difference identity

\[
 \frac{p(z+h)^{-1}-p(z)^{-1}}h
      =-\frac{(p(z+h)-p(z))/h}{p(z+h)p(z)}
\]

proves the derivative `-p'(z)/p(z)²` and its continuity when `p'` is continuous. No general unproved differentiation rule for reciprocals or composites is needed. R04 therefore gives

\[
 \int_{\Gamma_S}z^k\,dz=
       \begin{cases}c,&k=-1,\\0,&k\in\mathbb Z,\ k\ne-1.\end{cases}
\]

All negative integers are included. The same primitive proof works on every closed polygon whose edges avoid zero.

<a id="r08"></a>

## R08. Resolvent regularity and a direct nonempty spectrum proof

Let `B!=0` be a unital complex Banach algebra with `||1||=1`, and let `x in B`. If `||y||<1`, the series `sum_{j>=0} y^j` converges: differences of partial sums have norm at most the corresponding tails of the scalar geometric series from R01. Completeness supplies a limit. Multiplying the finite sums by `1-y` on either side gives `1-y^(N+1)`; the norm of the last power tends to zero. Multiplication is continuous by the submultiplicative norm, so the limit is a two sided inverse of `1-y`.

If `v` is invertible and `||v^(-1)h||<1`, then

\[
 (v+h)^{-1}=(1+v^{-1}h)^{-1}v^{-1}.
\]

The Neumann tail gives the bound

\[
 \|(v+h)^{-1}-v^{-1}\|
       \le \frac{\|v^{-1}\|^2\|h\|}{1-\|v^{-1}\|\|h\|}
\]

whenever the denominator is positive. Thus invertibility is open and inversion is continuous. Define

\[
 \sigma(x)=\{z\in\mathbb C:z1-x\text{ is not invertible}\},
 \qquad r_x(z)=(z1-x)^{-1}
\]

on the complement of the spectrum. There, for small complex `h`,

\[
 r_x(z+h)=r_x(z)-h r_x(z)^2+
                     \sum_{j\ge2}(-h)^j r_x(z)^{j+1}.
\]

After division by `h`, the tail has norm at most

\[
 \frac{|h|\|r_x(z)\|^3}{1-|h|\|r_x(z)\|}\longrightarrow0.
\]

Consequently `r_x'(z)=-r_x(z)^2`, a norm continuous derivative. Finite powers of `z` times `r_x(z)` have continuous complex derivative by the product rule. A bounded complex linear functional also preserves these derivatives, although our contour proofs operate directly in `B` and do not need to scalarize them.

For `|z|>||x||`, another Neumann series gives

\[
 r_x(z)=\sum_{j\ge0}x^j z^{-j-1},\qquad
 \|r_x(z)\|\le(|z|-\|x\|)^{-1}.
\]

Thus the spectrum is closed and bounded. To prove that it is nonempty, suppose it were empty. The resolvent would have continuous complex derivative on all of `C`. R06 on the whole square would give `integral_Gamma_S r_x(z) dz=0` for every `S>0`. Choose `S>||x||`. The displayed Neumann series converges uniformly on this boundary because `|z|>=S` and the series of norm bounds `||x||^j/S^(j+1)` converges. R03 permits termwise integration. R07 leaves only the term `j=0`, giving

\[
                \int_{\Gamma_S}r_x(z)\,dz=c1.
\]

Since `c!=0` and `1!=0`, this is a contradiction. Therefore `sigma(x)` is a nonempty closed bounded subset of `C`. The sequential compactness proved in R02 makes its continuous modulus attain a maximum; denote it by `r=max_{z in sigma(x)}|z|`. This proof uses neither Liouville's theorem nor a scalar circle mean.

<a id="r09"></a>

## R09. Polynomial roots from four rectangles

We first prove the only auxiliary scalar consequence required for polynomial spectral mapping. Let `g` be complex differentiable with continuous derivative everywhere, and suppose `g(z)->0` as `|z|->infinity`. Then `g` is identically zero.

Fix `w in C` and `0<s<S`. On the square annulus centered at `w`, the function `h(z)=g(z)/(z-w)` has continuous complex derivative by the product and reciprocal rules, because `z!=w` there. Tile the annulus by four rectangles: the full width top and bottom strips, and the left and right middle strips. Their interiors are disjoint; each is a closed rectangle on which `h` is defined in an open neighborhood. R06 and cancellation show that its integral on the outer square equals its integral on the inner square.

On the inner square, write `g(z)=g(w)+(g(z)-g(w))`. R07 gives the integral of the first term divided by `z-w` as `c g(w)`. The second integral has absolute value at most

\[
 8s\,s^{-1}\sup_{|z-w|\le\sqrt2s}|g(z)-g(w)|\longrightarrow0
\]

as `s` decreases to zero, by continuity. For each fixed `S` it follows that

\[
 c g(w)=\int_{\text{square centered at }w\text{ of halfside }S}
                    \frac{g(z)}{z-w}\,dz.
\]

The outer integral has absolute value at most `8 sup_boundary |g(z)|`, since its length is `8S` and `|z-w|>=S`. On that boundary `|z|>=S-|w|`, so the supremum tends to zero as `S` tends to infinity. Therefore `c g(w)=0`; `c!=0` proves the claim. The displayed value formula has been derived only for the specific globally regular functions in this argument, through the four rectangle proof; it is not an assumed Cauchy formula.

Now let `p(z)=a_d z^d+...+a_0`, with `d>=1` and `a_d!=0`. For `|z|>=1`,

\[
 \sum_{j<d}|a_j||z|^j
          \le\Bigl(\sum_{j<d}|a_j|\Bigr)|z|^{d-1}.
\]

For `|z|` sufficiently large this is at most `|a_d||z|^d/2`; the triangle inequality then gives `|p(z)|>=|a_d||z|^d/2`. If `p` had no root, `g=1/p` would be defined everywhere, have continuous complex derivative `-p'/p²` by the algebraic rules, and tend to zero at infinity. The previous paragraph would give `g=0`, impossible. Thus every nonconstant complex polynomial has a root. For a root `lambda`, the finite identity `z^k-lambda^k=(z-lambda) sum_{j=0}^{k-1} z^{k-1-j}lambda^j` shows explicitly that `p(z)=(z-lambda)q(z)` with `q` of degree one less. Induction factors `p` into its leading coefficient and linear factors.

<a id="r10"></a>

## R10. Polynomial spectral mapping, including constants

If `a` and `b` commute in a unital algebra and `ab` has inverse `d`, then each of `a,b` commutes with `d`. For example `a(ab)=(ab)a`; multiplication on both sides by `d` gives `da=ad`. Then `bd` is both a left and a right inverse of `a`, and `ad` is both a left and a right inverse of `b`. Conversely the product of commuting invertible factors is invertible by multiplying their inverses in reverse order. Induction gives this assertion for any finite list of commuting factors.

For a nonconstant polynomial `p` and scalar `mu`, R09 factors `p(z)-mu` as its nonzero leading coefficient times linear factors. Evaluate at `x`; these factors `x-lambda_j 1` commute. The previous paragraph shows that `p(x)-mu 1` is invertible exactly when every `x-lambda_j 1` is invertible. It fails to be invertible exactly when some `lambda_j in sigma(x)`, which is equivalent to `mu in p(sigma(x))`. Therefore

\[
                     \sigma(p(x))=p(\sigma(x)).
\]

For a constant `p(z)=a`, its value is `a1` and its spectrum is exactly `{a}`: when `mu!=a` the scalar inverse exists, whereas at `mu=a` the element is zero and cannot be invertible since `1!=0`. Since `sigma(x)` is nonempty, its image under the constant polynomial is also `{a}`. This proves the formula for every polynomial, including the zero polynomial.

In particular, applying this to `p(z)=z^n` and using the bound `sigma(x^n) subset {|z|<=||x^n||}` from R08 gives

\[
                    r^n\le\|x^n\|\quad(n\ge1).
\]

<a id="r11"></a>

## R11. An enclosing contour arbitrarily close to the spectral radius

Fix real numbers `r<a<R`. All are nonnegative and `a>0`. Choose a positive rational grid spacing `h` with `sqrt(2)h<R-a`; existence follows from R01. For integers `j,k`, put

\[
 Q_{jk}=[jh,(j+1)h]+i[kh,(k+1)h].
\]

Select precisely the closed cells meeting the closed disk `D_a={z:|z|<=a}`. This is a finite nonempty selection. Indeed a selected cell contains a point `w` of modulus at most `a`, and every point of that cell has distance at most `sqrt(2)h` from `w`, hence modulus at most `a+sqrt(2)h`. Only finitely many grid cells can lie in this bounded coordinate region. At least one cell contains zero, so at least one is selected.

Form a finite directed edge list `C` by taking the positively oriented boundaries of all selected cells and cancelling each shared edge. Each surviving edge separates a selected cell from an unselected grid cell. For a point `z` of such an edge, `|z|>a`: if `|z|<=a`, the adjacent unselected **closed** cell would meet `D_a` at `z`, contrary to its definition. On the other hand the selected cell supplies the bound `|z|<=a+sqrt(2)h<R`. Thus all exposed edges, including their endpoints, satisfy

\[
                         a<|z|<R.
\]

This edge list need not be identified with a parametrized simple polygon. It is enough that it is finite, consists of oriented segments, and arises by the exact cancellation just described. Let `L` be its finite total length after cancellation.

Choose an integer `N` so large that `S=Nh` is greater than `a+sqrt(2)h` and `||x||`. All selected cells lie inside the square `[-S,S]+i[-S,S]`, and this large square is the union of a finite grid of cells. Every unselected cell in this large grid is disjoint from `D_a`; in particular all its points lie outside `sigma(x)`, whose moduli are at most `r<a`. The function `z^n r_x(z)` has continuous complex derivative on an open neighborhood of each such cell, by R08 and the product rule. Apply R06 to each unselected cell and sum. Cancellation of the full grid boundaries, followed by cancellation among selected boundaries, gives exactly

\[
 \int_{\Gamma_S}z^n r_x(z)\,dz
                   =\int_C z^n r_x(z)\,dz\qquad(n\ge0).
\]

There is no integration through a singularity: R06 was applied only to unselected cells. Integrals on the selected cells' internal edges serve only as a formal cancellation in the edge list; the final integral on `C` is defined on its exposed resolvent edges. The equality can equivalently be obtained by summing only the boundaries of the unselected cells, which avoids even assigning values on internal selected edges. More precisely the boundary chain of the unselected cells is `Gamma_S-C`, and its every segment lies in the resolvent set. This is the meaning of the displayed equality.

On the large square, the Neumann series from R08 is uniformly convergent. Multiplying it by `z^n` preserves uniform convergence: on the boundary, `|z^n| <= (sqrt(2)S)^n`, a fixed finite constant for this `n`. Its terms are `x^j z^(n-j-1)`. R03 and R07 give

\[
 \int_{\Gamma_S}z^n r_x(z)\,dz
       =\sum_{j\ge0}x^j\int_{\Gamma_S}z^{n-j-1}\,dz
       =c x^n.
\]

All exponents `n-j-1`, positive, zero, and negative, are covered by R07. Hence

\[
                              c x^n=\int_C z^n r_x(z)\,dz.
\]

The resolvent norm is bounded on `C`: it is norm continuous on each compact segment, and there are finitely many of them. Let `M` be any finite common bound. The segment estimates from R03 and `|z|<R` give

\[
                    \|x^n\|\le |c|^{-1} L M R^n\qquad(n\ge0).
\]

The constants `C,L,M` are fixed once `R,a,h,x` have been chosen and do not depend on `n`. This is what removes the diagonal radius loss associated with using the large square itself for the estimate.

<a id="r12"></a>

## R12. The complete spectral radius formula

Choose `K=max(1, |c|^(-1) L M)`. R11 gives `||x^n|| <= K R^n` for every `n>=1` and for every fixed `R>r`, after choosing any `a` strictly between `r` and `R` and then its grid. R10 and root order give the two sided estimate

\[
              r\le\|x^n\|^{1/n}\le K^{1/n}R.
\]

R01 proves `K^(1/n)->1`. Given `epsilon>0`, choose `R=r+epsilon/2>r`. The fixed bound on the right is then less than `r+epsilon` for all sufficiently large `n`, while the bound on the left is always `r`. Consequently

\[
        \boxed{\displaystyle r(x)=\max_{z\in\sigma(x)}|z|
                       =\lim_{n\to\infty}\|x^n\|^{1/n}.}
\]

This includes `r=0`, `x=0`, and nilpotent elements. There is no assumption that `x` is normal, selfadjoint, invertible, or contained in a C* algebra. Nonunital and zero algebras are not silently inserted into the theorem: its exact hypothesis is a nonzero unital complex Banach algebra with normalized identity. Applications to unitizations, quotients, or other algebras must verify that hypothesis.

