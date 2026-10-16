# Principal logarithms and small automorphisms

An automorphism close to the identity has a canonical logarithm. The difficult point is not defining the logarithm as a bounded operator: it is proving that this operator still satisfies the Leibniz rule on the original C*-algebra. We prove that result by passing to the universal atomic representation, choosing implementing unitaries with one uniform branch gap, computing the logarithm by commuting left and right multiplication, and descending the answer.

Two different hypotheses lead to the theorem:

$$r(\alpha-\operatorname{id})<\sqrt3
\qquad\text{or}\qquad
\|\alpha-\operatorname{id}\|<2. \tag{1}$$

Here $r$ is spectral radius in the Banach algebra $B(A)$. The first inequality is not an abbreviation for the second. Each has its own geometric proof. The strict constants also matter: an order-three rotation reaches both boundary values and is outer.

Throughout, \(A\) is a complex C*-algebra, possibly nonunital and nonseparable. If \(A=\{0\}\), the zero map is the required derivation and all conclusions are immediate; hence assume \(A\ne\{0\}\). A von Neumann algebra automorphism is normal: it is an order isomorphism, so it preserves every existing supremum of a bounded increasing family of selfadjoint elements.

The earlier proofs used below are [Banach spectrum and spectral radius](OA-FLOW-CF.md#oa-flow.cf.2), [continuous functional calculus](OA-FLOW-CF.md#oa-flow.cf.6), [selfadjoint spectral calculus](OA-FLOW-SF.md#oa-flow.sf.sb4) and [membership in the von Neumann algebra](OA-FLOW-SF.md#oa-flow.sf.sb6), [inner-automorphism spectra in a factor](OA-FLOW-L122.md#oa-flow.innersp.factor), [singleton-spectrum rigidity](OA-FLOW-L90.md#oa-flow.isom.rigidity), and [innerness of bounded von Neumann derivations](OA-FLOW-L35.md#oa-flow.gi.innerness). The programme's [holomorphic calculus, Theorem 6.7 and Theorem 6.10](../../foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#6-the-holomorphic-functional-calculus) proves the contour homomorphism, spectral mapping and composition identities. We give the additional spectral geometry and atomic construction where they enter the proof.

*New expression is dedicated under CC0 to the extent of rights held; inherited component terms remain in force.*

<a id="smallaut.branch"></a>

## The principal branch and the two strict thresholds

Put

$$\Omega=\mathbb C\setminus(-\infty,0],$$

and let $\operatorname{Log}:\Omega\to\mathbb C$ be the branch satisfying $\operatorname{Log}(1)=0$ and $-\pi<\operatorname{Im}\operatorname{Log}z<\pi$. If an invertible element $T$ of a unital Banach algebra has $\operatorname{Sp}(T)\subset\Omega$, define

$$\operatorname{Log}T=
\frac{1}{2\pi i}\int_\Gamma
\operatorname{Log}z\,(z-T)^{-1}\,dz, \tag{2}$$

where $\Gamma$ is a positively oriented contour in $\Omega$ surrounding the spectrum. Holomorphic functional calculus makes (2) independent of the contour and gives

$$\exp(\operatorname{Log}T)=T. \tag{3}$$

Regard $\alpha$ as a surjective linear isometry of the Banach space $A$. Since $\|\alpha^n\|=1$ for every $n\in\mathbb Z$, the spectral-radius formula applied to $\alpha$ and $\alpha^{-1}$ gives

$$\operatorname{Sp}(\alpha)\subset\mathbb T. \tag{4}$$

Spectral translation gives

$$\operatorname{Sp}(\alpha-\operatorname{id})
=\{\lambda-1:\lambda\in\operatorname{Sp}(\alpha)\}. \tag{5}$$

If the first inequality in (1) holds, every $\lambda\in\operatorname{Sp}(\alpha)$ satisfies $|\lambda-1|<\sqrt3$. If the second holds, then $|\lambda-1|\leq r(\alpha-\operatorname{id})\leq\|\alpha-\operatorname{id}\|<2$. In either case $-1$ is absent from the spectrum. By (4), it is the only point of the negative real axis that could occur. Thus the principal logarithm

$$\delta=\operatorname{Log}\alpha \tag{6}$$

is a well-defined bounded operator on $A$. Formula (3) already proves $\exp\delta=\alpha$. The rest of the lesson proves the stronger conclusion

$$\delta(xy)=\delta(x)y+x\delta(y),
\qquad \delta(x^*)=\delta(x)^*. \tag{7}$$

Defining (6) alone does not prove (7): a holomorphic function of a multiplicative map need not visibly be a derivation. The atomic implementation below supplies the missing algebraic argument.

<a id="smallaut.groups"></a>

## Continuous groups and exponential product limits

The logarithm also connects small increments to continuous groups and product formulas. Here use a nonzero unital complex Banach algebra \(B\), without a C*- or involution assumption. We may work in a norm with \(\|1\|=1\): the left multiplication norm \(\|b\|_u=\|L_b\|_{B(B)}\) is an equivalent algebra norm, since \(\|b\|/\|1\|\le\|L_b\|\le\|b\|\). Changing to this equivalent norm changes neither continuity nor any norm limit below.

### A continuous group has a bounded generator

Suppose \(T:\mathbb R\to G(B)\) is a norm-continuous homomorphism. For a small fixed \(r>0\), put

$$S_r=\frac1r\int_0^rT_s\,ds.$$

Norm continuity gives \(\|S_r-1\|<1\), so \(S_r\) is invertible. For nonzero real \(h\), the group law gives

$$\frac{T_h-1}{h}S_r
=\frac1r\left(\frac1h\int_r^{r+h}T_v\,dv
-\frac1h\int_0^hT_v\,dv\right)
\longrightarrow\frac{T_r-1}{r}.$$

The integrals are oriented when \(h<0\). Continuity proves the same limit from both sides. Multiplying by \(S_r^{-1}\) therefore gives the norm derivative \(a=T'_0\in B\). The group law implies \(T'_t=T_ta=aT_t\). Consequently \(e^{-ta}T_t\) has zero derivative and value \(1\) at zero, so

$$T_t=e^{ta}\qquad(t\in\mathbb R).$$

The generator is unique because it is the derivative at zero. Conversely the absolutely convergent exponential series defines this continuous group for every \(a\in B\).

### The component generated by exponentials

The identity component \(G(B)_0\) consists exactly of finite products of exponentials. Let \(E\) be the set of those products, including the empty product. Inverses reverse the factors and replace their exponents by their negatives, so \(E\) is a subgroup. If \(\|b-1\|<1\), the absolutely convergent series
\[
\ell(b)=\sum_{n\ge1}\frac{(-1)^{n+1}}{n}(b-1)^n
\]
satisfies \(\exp\ell(b)=b\). Indeed the scalar power-series identity remains valid after absolute series substitution in the commutative closed algebra generated by \(b-1\). Hence \(E\) contains a neighborhood of \(1\). Its translates are open, making \(E\) open and its complement, a union of cosets, open as well. Every product \(\prod_{j=1}^m e^{a_j}\) is joined to \(1\) by the path \(t\mapsto\prod_{j=1}^m e^{ta_j}\). Thus \(E\) is path connected and contained in \(G(B)_0\). Conversely a connected set containing \(1\) cannot meet both \(E\) and its open complement, so \(G(B)_0\subset E\). This proves the assertion for the entire group of invertible elements, without imposing multiplicativity or star preservation on operators.

### The sum product formula

For \(x,y\in B\), we prove

$$e^{x+y}=\lim_{n\to\infty}(e^{x/n}e^{y/n})^n.$$

Absolute multiplication of the exponential series gives, uniformly for real \(|h|\le1\),

$$e^{hx}e^{hy}=1+h(x+y)+O(h^2),\qquad
e^{h(x+y)}=1+h(x+y)+O(h^2).$$

Here \(O(h^j)\) means an element whose norm is at most a fixed constant times \(|h|^j\), with constants depending only on \(x,y\). For example, the sum of the norms of all total-degree at least two terms in the first product is at most \(e^{|h|(\|x\|+\|y\|)}-1-|h|(\|x\|+\|y\|)\). Put \(u_n=e^{x/n}e^{y/n}\) and \(v_n=e^{(x+y)/n}\). Their difference has norm at most \(C/n^2\), while \(\|u_n\|,\|v_n\|\le e^{(\|x\|+\|y\|)/n}\). The exact noncommutative telescoping identity is

$$u^N-v^N=\sum_{k=0}^{N-1}u^{N-1-k}(u-v)v^k.$$

Taking \(N=n\) gives \(\|u_n^n-v_n^n\|\le Ce^{\|x\|+\|y\|}/n\to0\), and \(v_n^n=e^{x+y}\). This proves the formula without assuming \(xy=yx\).

### The commutator product formula

Write \([x,y]=xy-yx\). The corresponding limit is

$$e^{[x,y]}=\lim_{n\to\infty}
\left(e^{-x/n}e^{-y/n}e^{x/n}e^{y/n}\right)^{n^2}.$$

To verify both the sign and the scale, multiply the four power series through degree two. The linear terms cancel. After the first three factors, the quadratic coefficient is \(y^2/2+xy-yx\); multiplication by the last factor cancels the remaining \(y^2\) term. Thus

$$c(h)=e^{-hx}e^{-hy}e^{hx}e^{hy}
=1+h^2[x,y]+O(|h|^3).$$

The total-degree at least three remainder is bounded by the scalar exponential tail with parameter \(2|h|(\|x\|+\|y\|)\), and hence by a constant times \(|h|^3\) on \(|h|\le1\). Also \(d(h)=e^{h^2[x,y]}=1+h^2[x,y]+O(h^4)\). Consequently

$$\|c(1/n)-d(1/n)\|\le C/n^3,\qquad
\max(\|c(1/n)\|,\|d(1/n)\|)\le1+C'/n^2.$$

The second bound uses cancellation in the product itself; multiplying the four separate exponential norm bounds would lose that scale. Apply the telescoping identity with \(N=n^2\). It gives

$$\|c(1/n)^{n^2}-d(1/n)^{n^2}\|
\le \frac Cn(1+C'/n^2)^{n^2-1}
\le\frac Cn e^{C'}\longrightarrow0.$$

Since \(d(1/n)^{n^2}=e^{[x,y]}\), the commutator formula follows. The order of the four factors determines the positive sign of \([x,y]\).

These arguments prove the four norm-group and product-limit assertions of Takesaki I, Chapter I, exercise 4, printed page 57. They concern bounded elements and norm limits in a Banach algebra; they do not assert product limits for unbounded operator generators.


<a id="smallaut.arc"></a>

## Spectral-radius geometry and a common short arc

We first isolate the circle geometry needed for the spectral-radius hypothesis.

**Short-arc lemma.** Let $S\subset\mathbb T$ be nonempty and compact, and suppose

$$|z\overline w-1|\leq r<\sqrt3
\qquad(z,w\in S). \tag{8}$$

Set $\gamma=2\arcsin(r/2)$, so $0\leq\gamma<2\pi/3$. Then some rotation of $S$ is contained in

$$\{e^{it}:|t|\leq\gamma/2\}. \tag{9}$$

In particular, the rotated set lies in the half-plane

$$\operatorname{Re}z\geq\cos(\gamma/2)>\tfrac12. \tag{10}$$

**Proof.** Rotate one point of $S$ to $1$. Every other point then has a unique argument in $[-\gamma,\gamma]$, because its chord distance from $1$ is at most $r$. Let $p\geq0$ and $-q\leq0$ be the largest and smallest arguments that occur, allowing either to be zero. Compactness supplies the extrema.

The chord bound between $e^{ip}$ and $e^{-iq}$ gives the alternatives $p+q\leq\gamma$ or $p+q\geq2\pi-\gamma$. But $p+q\leq2\gamma<4\pi/3$, whereas $2\pi-\gamma>4\pi/3$, so the second alternative is impossible. Thus $p+q\leq\gamma$. The original set lies in the arc $[-q,p]$, whose length is at most $\gamma$. Rotating its midpoint to $1$ gives (9), and (10) follows. $\square$

For a type-I factor automorphism $\beta=\operatorname{Ad}u$, the factor spectrum formula gives

$$\operatorname{Sp}(\beta)
=\operatorname{Sp}(u)\operatorname{Sp}(u)^{-1}. \tag{11}$$

Consequently $r(\beta-\operatorname{id})\leq r<\sqrt3$ implies (8) for $S=\operatorname{Sp}(u)$. Multiplying $u$ by a scalar does not change $\operatorname{Ad}u$, so the short-arc lemma supplies an implementer with the uniform gap (10).

The pairwise chord hypothesis is essential. The weaker condition

$$-1\notin\operatorname{Sp}(\operatorname{Ad}u) \tag{12}$$

by itself does not put $\operatorname{Sp}(u)$ in an open semicircle. Let $\omega=e^{2\pi i/3}$ and take

$$u=\operatorname{diag}(1,\omega,\omega^2)\quad\text{on }\mathbb C^3. \tag{13}$$

Then $\operatorname{Sp}(u)=\{1,\omega,\omega^2\}$ is not contained in any open semicircle, while (11) gives the same three-point set for $\operatorname{Sp}(\operatorname{Ad}u)$, which excludes $-1$. The strict $\sqrt3$ bound, through all pairwise chords in (8), is the needed additional information. The example (13) lies exactly at the excluded boundary.

<a id="smallaut.numerical"></a>

## The norm bound gives a uniform numerical-range gap

We first prove the spectral and Hilbert-space facts needed for this argument.

**Boundary spectrum gives approximate eigenvectors.** Let \(T\in B(X)\) and let \(\lambda\) lie on the boundary of \(\operatorname{Sp}(T)\). Choose resolvent points \(\lambda_n\to\lambda\), and write \(R_n=(\lambda_n-T)^{-1}\). The Neumann series shows that the open disc of radius \(\|R_n\|^{-1}\) about \(\lambda_n\) is contained in the resolvent set. Therefore
\[
\|R_n\|\ge|\lambda_n-\lambda|^{-1}\longrightarrow\infty.
\]
Choose a unit \(y_n\) with \(\|R_ny_n\|\ge\|R_n\|/2\), and put \(x_n=R_ny_n/\|R_ny_n\|\). Then
\[
\|(T-\lambda)x_n\|
\le 2/\|R_n\|+|\lambda_n-\lambda|\longrightarrow0.
\]
This proves the boundary assertion on any nonzero complex Banach space.

**Rank-one distance.** For unit vectors \(\xi,\eta\), changing the phase of \(\eta\) does not change \(P_\eta\); thus arrange \(\langle\eta,\xi\rangle=t\in[0,1]\). If \(t=1\), the projections coincide. Otherwise put \(q=\sqrt{1-t^2}\) and \(\eta=t\xi+q\zeta\), where \(\zeta\) is a unit vector perpendicular to \(\xi\). On their two-dimensional span,
\[
P_\eta-P_\xi=
\begin{pmatrix}-q^2&tq\\tq&q^2\end{pmatrix},
\qquad (P_\eta-P_\xi)^2=q^2 I.
\]
The difference vanishes on the orthogonal complement, so
\[
\|P_\eta-P_\xi\|=\sqrt{1-|\langle\eta,\xi\rangle|^2}.
\]

**The closed numerical range of a unitary.** Let \(u\) be unitary on a nonzero Hilbert space. Write \(S=\operatorname{Sp}(u)\) and \(K=\overline{\operatorname{conv}}S\). This is compact: it is closed and bounded in the finite-dimensional plane. For every complex \(a\), continuous functional calculus gives
\[
\operatorname{Re}(au)\ge\min_{z\in S}\operatorname{Re}(az)\,I.
\]
Hence every \(\langle u\xi,\xi\rangle\), with \(\|\xi\|=1\), belongs to all closed half-planes containing \(S\), and thus to \(K\). To justify the last implication, a point outside the compact convex set \(K\) has a closest point in \(K\); differentiation along segments gives a real linear functional strictly separating the outside point from \(K\).

Conversely, choose distinct \(z_1,\ldots,z_m\in S\) and nonnegative weights \(t_j\) with sum \(1\). Since \(S\subset\mathbb T\), every \(z_j\) is a boundary spectral point. The preceding lemma supplies unit vectors \(\xi_{j,n}\) with
\[
u\xi_{j,n}-z_j\xi_{j,n}\longrightarrow0.
\]
Preservation of inner products by \(u\) gives
\[
(1-z_i\overline{z_j})\langle\xi_{i,n},\xi_{j,n}\rangle\longrightarrow0.
\]
Thus distinct sequences are asymptotically orthogonal. For \(v_n=\sum_j\sqrt{t_j}\xi_{j,n}\), we have
\[
\|v_n\|^2\longrightarrow1,\qquad
\langle uv_n,v_n\rangle\longrightarrow\sum_jt_jz_j.
\]
Normalizing \(v_n\) shows that each finite convex combination of \(S\) lies in the closure of the numerical range. Taking closures proves
\[
\overline{W(u)}=\overline{\operatorname{conv}}\operatorname{Sp}(u)=K.
\]
In particular the closed numerical range is compact and convex. This proof uses neither a dimension assumption nor a general numerical-range convexity theorem.

The operator-norm hypothesis in (1) requires a different argument. Let $u$ be unitary on a nonzero Hilbert space $H$, write $\beta=\operatorname{Ad}u$, and suppose

$$c=\|\beta-\operatorname{id}\|<2. \tag{14}$$

For a unit vector $\xi$, let $P_\xi$ be the projection onto $\mathbb C\xi$ and put $s_\xi=2P_\xi-1$. This is a selfadjoint unitary. The distance formula for rank-one projections gives

$$
\begin{aligned}
c
&\geq\|\beta(s_\xi)-s_\xi\| \\
&=2\|P_{u\xi}-P_\xi\|
=2\sqrt{1-|\langle u\xi,\xi\rangle|^2}.
\end{aligned} \tag{15}$$

Therefore, with

$$\varepsilon=\sqrt{1-c^2/4}>0, \tag{16}$$

every unit vector satisfies

$$|\langle u\xi,\xi\rangle|\geq\varepsilon. \tag{17}$$

Let $K=\overline{W(u)}$ be the closed numerical range. If $0$ were within distance less than $\varepsilon$ of $K$, numerical values would approach a point of modulus less than $\varepsilon$, contradicting (17). Thus

$$\operatorname{dist}(0,K)\geq\varepsilon. \tag{18}$$

The preceding proof shows that $K$ is compact and convex and equals the closed convex hull of $\operatorname{Sp}(u)$. Let $z_0\in K$ minimize modulus. The nearest-point inequality in the Euclidean plane says

$$\operatorname{Re}(\overline{z_0}z)\geq|z_0|^2
\qquad(z\in K). \tag{19}$$

Indeed, the derivative at zero of $|(1-t)z_0+tz|^2$ is nonnegative for $0\leq t\leq1$. After multiplying $u$ by the scalar $\overline{z_0}/|z_0|$, equations (18)–(19) give

$$\operatorname{Sp}(u)\subset
\{z\in\mathbb T:\operatorname{Re}z\geq|z_0|\}
\subset\{z:\operatorname{Re}z\geq\varepsilon\}. \tag{20}$$

Thus every type-I factor automorphism satisfying (14) has an implementer whose spectrum has a gap from the imaginary axis depending only on $c$. This uniformity is what permits an arbitrary bounded product of factors later. Merely choosing a separate open semicircle for each factor would not provide it.

<a id="smallaut.center"></a>

## The bidual automorphism fixes the center

Let \(M=A^{**}\) and \(\widetilde\alpha=\alpha^{**}\). The programme's [bidual construction](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#constructing-the-bidual-before-using-it) identifies \(A^{**}\) with its enveloping von Neumann algebra. The [second-adjoint extension proof](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-02) shows that \(\widetilde\alpha\) is a normal star homomorphism. Applying it also to \(\alpha^{-1}\) shows that the two extensions are inverse, so \(\widetilde\alpha\) is an automorphism. For clarity, these extensions preserve both quantities in (1). If a bounded operator \(S\) is invertible, so is its Banach adjoint \(S^*\). Conversely suppose \(S^*\) is invertible. For every unit functional \(\varphi\), write \(\varphi=S^*\psi\) with \(\|\psi\|\le\|(S^*)^{-1}\|\). Hahn–Banach duality gives
\[
\|x\|\le\|(S^*)^{-1}\|\,\|Sx\|.
\]
Thus \(S\) is bounded below and has closed range. Injectivity of \(S^*\) says that no nonzero functional annihilates that range, so Hahn–Banach makes it dense. Therefore \(S\) is bijective with bounded inverse. Apply the equivalence to \(S=\lambda-T\), then once more to its adjoint: \(T,T^*,T^{**}\) have the same spectrum. Duality also gives \(\|T^*\|=\|T\|\), and applying it twice gives \(\|T^{**}\|=\|T\|\). Consequently

$$\operatorname{Sp}(\widetilde\alpha)=\operatorname{Sp}(\alpha),
\quad
r(\widetilde\alpha-\operatorname{id})=r(\alpha-\operatorname{id}),
\quad
\|\widetilde\alpha-\operatorname{id}\|
=\|\alpha-\operatorname{id}\|. \tag{21}$$

We claim that either inequality in (1) forces

$$\widetilde\alpha(z)=z\qquad(z\in Z(M)). \tag{22}$$

**The norm case.** If $e$ is a central projection, then $e$ and $\widetilde\alpha(e)$ commute and

$$
\begin{aligned}
2\|e-\widetilde\alpha(e)\|
&=\|(1-2e)-(1-2\widetilde\alpha(e))\| \\
&\leq\|\widetilde\alpha-\operatorname{id}\|<2.
\end{aligned} \tag{23}$$

Two commuting projections are equal whenever their distance is less than $1$: in the commutative algebra they generate, a nonzero difference would take one of the values $1$ or $-1$. Thus every central projection is fixed. Every central selfadjoint element is a norm limit of finite linear combinations of its central spectral projections, by [SB4–SB6](OA-FLOW-SF.md#oa-flow.sf.sb4). Splitting a central element into real and imaginary parts gives (22).

**The spectral-radius case.** Put $\beta=\widetilde\alpha|_{Z(M)}$. It is an invertible isometry, so $\operatorname{Sp}(\beta)\subset\mathbb T$. Every point $\lambda$ of this spectrum lies on its boundary, since a subset of the circle has empty planar interior. The boundary lemma proved above therefore makes it an approximate eigenvalue. Choose $x_k\in Z(M)$ with $\|x_k\|=1$ and

$$\|\beta(x_k)-\lambda x_k\|\longrightarrow0. \tag{24}$$

The center is commutative, so $x_k$ is normal and $\|x_k^n\|=1$. A telescoping product estimate yields

$$\|\beta(x_k^n)-\lambda^n x_k^n\|
\leq n\|\beta(x_k)-\lambda x_k\|. \tag{25}$$

All these approximate eigenvectors remain in the center, so \(\lambda^n\) belongs to both the central and the full approximate point spectrum. Taking adjoints in (24) gives unit approximate eigenvectors \(x_k^*\) for \(\overline\lambda=\lambda^{-1}\); applying (25) to these vectors gives every negative power as well. The zeroth power \(1\) is an eigenvalue because the unit is fixed. Thus all integer powers belong to both spectra. In particular, \(\lambda^n\) belongs to the approximate point spectrum of the full operator \(\widetilde\alpha\) for every positive integer \(n\). It follows from (21) that

$$|\lambda^n-1|
\leq r(\widetilde\alpha-\operatorname{id})<\sqrt3
\qquad(n\geq1). \tag{26}$$

If \(\lambda\ne1\), choose its argument \(t\) with \(0<|t|\le\pi\). If \(|t|\ge2\pi/3\), then \(|\lambda-1|\ge\sqrt3\). Otherwise choose the least positive integer \(n\) for which \(n|t|\ge2\pi/3\). It satisfies
\[
2\pi/3\le n|t|<2\pi/3+|t|<4\pi/3,
\]
so \(|\lambda^n-1|\ge\sqrt3\). Either case contradicts (26). Since the spectrum is nonempty, \(\operatorname{Sp}(\beta)=\{1\}\). The already proved [singleton-spectrum isometry theorem](OA-FLOW-L90.md#oa-flow.isom.rigidity) gives \(\beta=\operatorname{id}\), proving (22).

Notice why (24)–(25) are present. Spectrum does not automatically pass from an arbitrary invariant Banach subspace to the ambient operator. Central approximate eigenvectors are also vectors in $M$, so their powers establish exactly the ambient spectral information used in (26).

<a id="smallaut.atomic"></a>

## Uniform implementers in the universal atomic representation

Here is the construction of the atomic algebra, including the faithfulness needed for descent. The programme's [pure-state theorem, Theorems 8.3 and 8.5](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#enough-irreducible-representations) proves that pure states have irreducible, nondegenerate GNS representations and that these representations separate every C*-algebra, including a nonunital one. More precisely, every nonzero positive \(a\in A\) has a pure state \(\varphi\) with \(\varphi(a)=\|a\|>0\).

For such a representation \(\pi:A\to B(H_\pi)\), irreducibility means \(\pi(A)'=\mathbb C I\). Indeed a nonscalar selfadjoint element of the commutant would have a nontrivial spectral projection defining a reducing subspace; real and imaginary parts then give the assertion for the full commutant. Thus \(\pi(A)''=B(H_\pi)\). The [normal representation extension, Lemma 2.1](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-02) supplies an onto normal star homomorphism
\[
q_\pi:M=A^{**}\longrightarrow B(H_\pi),
\qquad q_\pi|_A=\pi,
\]
whose kernel is \(M(1-z_\pi)\) for a central projection \(z_\pi\). Its restriction to \(Mz_\pi\) is a normal star isomorphism. Since \(B(H_\pi)\) is a factor, \(z_\pi\) is a minimal nonzero central projection: a smaller central projection would map to a nontrivial central projection of \(B(H_\pi)\).

Two minimal central projections are either equal or orthogonal. Select one GNS representation \(\pi_j\) for each distinct \(z_\pi\), and write its support as \(z_j\). Repeated supports have the same kernel in \(M\), so making this selection does not lose the separating property on \(A\). Let \(z_0=\bigvee_j z_j\). The map
\[
Mz_0\longrightarrow\prod_j Mz_j,\qquad x\longmapsto(xz_j)_j
\]
is an isometric star isomorphism onto the bounded product. For the onto assertion, given \(\sup_j\|x_j\|\le C\) with \(x_j\in Mz_j\), finite sums \(\sum_{j\in E}x_j\) converge strongly: for every vector \(\xi\), their squared tail norm is at most \(C^2\sum_{j\in E'\setminus E}\|z_j\xi\|^2\), and the sum over \(j\) is bounded by \(\|\xi\|^2\). The adjoint sums converge in the same way. Strong closedness places the limit in \(Mz_0\), with coordinates \(x_j\) and norm at most \(C\). The reverse norm inequality follows by compression. Injectivity follows from the strong sum \(\sum_jz_j=z_0\).

Composing the factor isomorphisms therefore gives

$$M_0=Mz_0\cong\prod_{j\in J}B(H_j). \tag{27}$$

The product in (27) is the von Neumann algebra of bounded families, not an algebraic direct sum. Let

$$\pi_0=\bigoplus_{j\in J}\pi_j:A\longrightarrow M_0 \tag{28}$$

be the resulting representation, with \(\pi_0(a)=(\pi_j(a))_j\), equivalently the image of \(az_0\) under (27). If \(\pi_0(a)=0\), every pure-state GNS representation kills \(a\), because its support occurs among the \(z_j\). Applied to \(a^*a\), the separating statement above forces \(a=0\). Thus \(\pi_0\) is faithful, and the C*-norm identity makes it isometric. Since (22) fixes every central projection, $\widetilde\alpha$ preserves $z_0$ and each factor summand. Write its restriction as

$$\alpha_0=\widetilde\alpha|_{M_0}
=\prod_{j\in J}\alpha_j,
\qquad \alpha_j\in\operatorname{Aut}(B(H_j)). \tag{29}$$

The covariance relation is

$$\alpha_0\pi_0=\pi_0\alpha. \tag{30}$$

For completeness, every automorphism \(\gamma\) of \(B(H)\) is implemented by a unitary, also for arbitrary nonseparable \(H\). Fix an orthonormal basis \((\xi_i)_{i\in I}\) and its matrix units \(e_{ij}\), and choose an index \(o\). The projection \(\gamma(e_{oo})\) is minimal, hence rank one; choose a unit vector \(\eta_o\) in its range and put \(\eta_i=\gamma(e_{io})\eta_o\). The matrix-unit relations make these an orthonormal family. Normality of \(\gamma\) and the increasing finite sums \(\sum_{i\in E}e_{ii}\uparrow1\) show that their images sum strongly to \(1\), so the family is complete. The unitary \(v\xi_i=\eta_i\) implements \(\gamma\) on every matrix unit. For arbitrary \(x\), the finite compressions \(p_E x p_E\), \(p_E=\sum_{i\in E}e_{ii}\), converge ultraweakly to \(x\); normality then extends \(\gamma=\operatorname{Ad}v\) to all of \(B(H)\).

Apply this to each \(\alpha_j\), choosing \(v_j\) with \(\alpha_j=\operatorname{Ad}v_j\). We now normalize these implementers.

If $r(\alpha-\operatorname{id})<\sqrt3$, choose $r$ strictly between this radius and $\sqrt3$. For each fixed central projection \(z_j\), the decomposition \(M=Mz_j\oplus M(1-z_j)\) is invariant in both directions under \(\widetilde\alpha\). A bounded block diagonal operator on this two-summand decomposition is invertible exactly when both blocks are invertible. Thus the spectrum of \(\alpha_j-\operatorname{id}\) is contained in that of \(\widetilde\alpha-\operatorname{id}\), and (21) bounds its spectral radius by the global one. Equations (8)–(11) allow a scalar rotation $u_j$ of $v_j$ such that

$$\operatorname{Sp}(u_j)\subset
\{e^{it}:|t|\leq\theta\},
\qquad \theta=\arcsin(r/2)<\pi/3. \tag{31}$$

If $\|\alpha-\operatorname{id}\|=c<2$, restriction to each summand and (15)–(20) allow a scalar rotation with

$$\operatorname{Sp}(u_j)\subset
\{e^{it}:|t|\leq\theta\},
\qquad \theta=\arccos\sqrt{1-c^2/4}<\pi/2. \tag{32}$$

The same $\theta<\pi/2$ works for every $j$ in either case. Therefore

$$u=(u_j)_{j\in J}\in\mathcal U(M_0),
\qquad \alpha_0=\operatorname{Ad}u, \tag{33}$$

and the spectrum of \(u\) remains in the common arc \(|\arg z|\le\theta\). Indeed outside that closed arc each \(\lambda-u_j\) has inverse norm at most the reciprocal of the distance from \(\lambda\) to the arc, by continuous functional calculus. These inverses form a bounded family, hence an inverse to \(\lambda-u\) in the product. The principal logarithm may be taken in the bounded product:

$$h=\frac1i\operatorname{Log}u=h^*,
\qquad \|h\|\leq\theta,
\qquad u=e^{ih}. \tag{34}$$

The global angle in (31) or (32), rather than factorwise membership in unspecified semicircles, ensures that $(\operatorname{Log}u_j)_j$ is bounded and belongs to $M_0$.

<a id="smallaut.productlog"></a>

## The branch-controlled left-right logarithm

For $a\in M_0$, let $L_a$ and $R_a$ denote left and right multiplication on the Banach space $M_0$. These representations commute, and (33) becomes

$$\alpha_0=L_uR_{u^*}. \tag{35}$$

We will prove the exact identity

$$\operatorname{Log}\alpha_0
=\operatorname{Log}L_u+\operatorname{Log}R_{u^*}
=i(L_h-R_h)
=i\operatorname{ad}h. \tag{36}$$

This is not an unrestricted rule $\operatorname{Log}(ab)=\operatorname{Log}a+\operatorname{Log}b$. Its validity comes from the common spectral arc.

Indeed, if $s,t\in[-\theta,\theta]$, then

$$-\pi<-2\theta\leq s-t\leq2\theta<\pi. \tag{37}$$

Consequently the principal scalar branch satisfies

$$\operatorname{Log}(e^{is}e^{-it})
=is-it
=\operatorname{Log}(e^{is})+\operatorname{Log}(e^{-it}). \tag{38}$$

Here is the required operator argument using only one-variable holomorphic calculus. Put $P=L_u$ and $Q=R_{u^*}$. Choose bounded Jordan neighborhoods $U,V$ of their spectral arcs, small enough that their closures and every product $zw$, with $z\in\overline U$ and $w\in\overline V$, lie in $\Omega$ and satisfy $\operatorname{Log}(zw)=\operatorname{Log}z+\operatorname{Log}w$. Such neighborhoods exist because $2\theta<\pi$: slightly enlarge the angular intervals in (37) and restrict the radial coordinates near $1$.

For a scalar function $f$ holomorphic near $\overline U\times\overline V$, define the norm-convergent iterated contour integral

$$\mathcal H[f]=\frac{1}{(2\pi i)^2}
\int_{\partial U}\int_{\partial V}
f(z,w)(z-P)^{-1}(w-Q)^{-1}\,dw\,dz. \tag{36a}$$

The resolvents commute. One-variable Cauchy calculus gives $\mathcal H[1]=I$, $\mathcal H[\operatorname{Log}z]=\operatorname{Log}P$ and $\mathcal H[\operatorname{Log}w]=\operatorname{Log}Q$.

Let $K=\{zw:z\in\overline U,\ w\in\overline V\}$. For $\xi\notin K$, multiplying $\mathcal H[(\xi-zw)^{-1}]$ by $\xi-PQ$ on either side gives $I$. To check this directly, use

$$\xi-PQ=(\xi-zw)I+(z-P)Q+z(w-Q). \tag{36b}$$

The first term integrates to $I$. In the second term, cancellation of $(z-P)^{-1}$ leaves an integrand holomorphic in $z$ on $U$, so its $z$ integral is zero. In the third term, cancellation of $(w-Q)^{-1}$ leaves an integrand holomorphic in $w$ on $V$, so its $w$ integral is zero. Norm Fubini permits either integration order. Thus $\sigma(PQ)\subset K$ and this double integral is $(\xi-PQ)^{-1}$.

Choose a contour $\Gamma\subset\Omega$ surrounding $K$, disjoint from it. Such a contour exists inside a slightly larger annular sector with arguments strictly between $-\pi$ and $\pi$. Insert the double-integral resolvent into the one-variable Cauchy formula for $\operatorname{Log}(PQ)$. Norm Fubini and the scalar Cauchy formula in $\xi$ give $\operatorname{Log}(PQ)=\mathcal H[\operatorname{Log}(zw)]$. Applying the scalar identity on $U\times V$ now proves $\operatorname{Log}(PQ)=\operatorname{Log}P+\operatorname{Log}Q$. No separate joint-calculus theorem is assumed. Left multiplication is a unital homomorphism. Right multiplication reverses products, but on the commutative algebra generated by one element and its resolvents it is a homomorphism as well. In particular \((z-R_{u^*})^{-1}=R_{(z-u^*)^{-1}}\); integrating that identity and the corresponding left identity gives

$$\operatorname{Log}L_u=L_{\operatorname{Log}u}=iL_h,
\qquad
\operatorname{Log}R_{u^*}=R_{\operatorname{Log}u^*}=-iR_h. \tag{39}$$

Equations (38)–(39) prove (36). In particular, $\operatorname{Log}\alpha_0$ is a bounded star derivation of $M_0$.

<a id="smallaut.descent"></a>

## Descent proves that the logarithm is a derivation

We now return to \(A\). Both spectra are compact subsets of \(\Omega\): this was proved for \(\alpha\) at (4)–(6) and for \(\alpha_0\) by (36a)–(36b). Choose a common annular-sector neighborhood \(D\), with positively oriented piecewise smooth boundary \(\Gamma\), such that
\[
\operatorname{Sp}(\alpha_0)\cup\operatorname{Sp}(\alpha)
\subset D\Subset\Omega,\qquad
\Gamma\cap(\operatorname{Sp}(\alpha_0)\cup\operatorname{Sp}(\alpha))=\varnothing.
\tag{40}
\]
The spectra lie on the unit circle and avoid \(-1\), so a thin annular sector whose end angles stay strictly between \(-\pi\) and \(\pi\) provides such \(D\).

The intertwining relation (30) implies
\[
(\lambda-\alpha_0)\pi_0=\pi_0(\lambda-\alpha).
\]
For each \(\lambda\in\Gamma\), both factors are invertible. Multiplying on the left and right gives the resolvent identity
\[
(\lambda-\alpha_0)^{-1}\pi_0
=\pi_0(\lambda-\alpha)^{-1}.
\tag{41}
\]
For \(x\in A\), multiply by \(\operatorname{Log}\lambda\) and integrate around \(\Gamma\):
\[
\frac1{2\pi i}\int_\Gamma
\operatorname{Log}\lambda\,(\lambda-\alpha_0)^{-1}\pi_0(x)\,d\lambda
=
\pi_0\!\left(
\frac1{2\pi i}\int_\Gamma
\operatorname{Log}\lambda\,(\lambda-\alpha)^{-1}x\,d\lambda
\right).
\tag{42}
\]
These are norm integrals of continuous functions on a compact contour. The bounded linear map \(\pi_0\) commutes with them, first for Riemann sums and then by norm limits. Formula (2) therefore gives
\[
(\operatorname{Log}\alpha_0)(\pi_0(x))
=\pi_0\bigl((\operatorname{Log}\alpha)(x)\bigr).
\tag{43}
\]
This establishes descent directly, without assuming that a polynomial approximation on an operator spectrum controls operator norm.

Thus the logarithm on the atomic von Neumann algebra preserves the faithful copy of $A$ and restricts to the logarithm already defined in (6). Combining (36) and (43), for $x,y\in A$ we obtain

$$
\begin{aligned}
\pi_0(\delta(xy))
&=(\operatorname{Log}\alpha_0)(\pi_0(x)\pi_0(y)) \\
&=(\operatorname{Log}\alpha_0)(\pi_0(x))\pi_0(y)
+\pi_0(x)(\operatorname{Log}\alpha_0)(\pi_0(y)) \\
&=\pi_0(\delta(x)y+x\delta(y)).
\end{aligned} \tag{44}$$

Faithfulness of $\pi_0$ proves the Leibniz identity. The same restriction of the star derivation $i\operatorname{ad}h$ proves $\delta(x^*)=\delta(x)^*$. We have therefore proved the small-automorphism theorem:

$$
\boxed{
r(\alpha-\operatorname{id})<\sqrt3
\ \text{or}\ 
\|\alpha-\operatorname{id}\|<2
\quad\Longrightarrow\quad
\operatorname{Log}\alpha\text{ is a bounded star derivation of }A.}
\tag{45}$$

No unit, separability, or von Neumann hypothesis on $A$ was used.

<a id="smallaut.inner"></a>

## Small von Neumann automorphisms and the identity component

Let $M$ now be a nonzero von Neumann algebra and let $\alpha\in\operatorname{Aut}(M)$ satisfy either strict inequality in (45). The preceding theorem gives a bounded star derivation $\delta=\operatorname{Log}\alpha$. The [general innerness theorem](OA-FLOW-L35.md#oa-flow.gi.innerness), with the projection, spectral and analysis foundations stated there, supplies $k=k^*\in M$ such that

$$\delta=i\operatorname{ad}k. \tag{46}$$

Since \(L_k\) and \(R_k\) commute, multiplication of the absolutely convergent exponential series gives \(e^{i(L_k-R_k)}=e^{iL_k}e^{-iR_k}=L_{e^{ik}}R_{e^{-ik}}\). Exponentiating inside \(B(M)\) therefore gives

$$\alpha=e^\delta
=e^{i\operatorname{ad}k}
=\operatorname{Ad}(e^{ik}). \tag{47}$$

The final symbol in (47) is uppercase $\operatorname{Ad}$: it denotes conjugation by a unitary, whereas lowercase $\operatorname{ad}$ in (46) denotes a commutator derivation. Thus every von Neumann automorphism in either strict neighborhood is inner.

Consider $\operatorname{Aut}(M)$ with its operator-norm topology. Equation (47) shows that

$$\{\alpha:\|\alpha-\operatorname{id}\|<2\}
\subset\operatorname{Int}(M). \tag{48}$$

Translating (48) by group multiplication makes $\operatorname{Int}(M)$ an open subgroup. Its complement is a union of open cosets, so it is closed as well.

Every unitary \(u\in M\) has a bounded selfadjoint logarithm. One can construct it using only the selfadjoint spectral calculus already proved in [SB4–SB6](OA-FLOW-SF.md#oa-flow.sf.sb4). Put
\[
x=(u+u^*)/2,\qquad y=(u-u^*)/(2i).
\]
These commuting selfadjoint elements satisfy \(x^2+y^2=1\). Let \(p=1_{(-\infty,0)}(y)\), let \(a=\arccos x\) by continuous calculus, and set \(s=1-2p\), \(h=sa\). The spectral projection \(p\) commutes with \(x\) and \(a\): here \(p\) is the strong limit of the continuous functions \(\min(1,n(-y)_+)\), by bounded pointwise spectral convergence, and multiplication by a fixed bounded operator preserves those strong limits. We have \(s=s^*\), \(s^2=1\), \(sy=|y|\), and \(s|y|=y\). Power series and commutation show
\[
\cos h=\cos a=x,\qquad
\sin h=s\sin a=s\sqrt{1-x^2}=s|y|=y.
\]
Thus \(h=h^*\), \(\|h\|\le\pi\), and \(e^{ih}=x+iy=u\). Hence

$$[0,1]\ni t\longmapsto\operatorname{Ad}(e^{ith}) \tag{49}$$

is a norm-continuous path from the identity to $\operatorname{Ad}u$. Indeed its values at $t,s$ differ in operator norm by at most $2\|e^{ith}-e^{ish}\|\le2|t-s|\|h\|$, by integrating the norm derivative of the exponential. The inner automorphism group is therefore path connected. Since a connected component containing the identity lies in every clopen subgroup containing the identity, (48)–(49) prove

$$\operatorname{Aut}(M)_0=\operatorname{Int}(M), \tag{50}$$

where the left side is the principal norm-connected component.

<a id="smallaut.sharp"></a>

## The order-three rotation proves sharpness

Let $\omega=e^{2\pi i/3}$ and define an automorphism of $L^\infty(\mathbb T)$ by

$$ (\rho f)(z)=f(\omega z). \tag{51}$$

For the circle character $\chi_n(z)=z^n$,

$$\rho(\chi_n)=\omega^n\chi_n. \tag{52}$$

All three cube roots of unity are therefore eigenvalues of $\rho$. Since $\rho^3=\operatorname{id}$, there can be no others:

$$\operatorname{Sp}(\rho)=\{1,\omega,\omega^2\}. \tag{53}$$

It follows that

$$r(\rho-\operatorname{id})
=\max\{|\omega-1|,|\omega^2-1|\}
=\sqrt3. \tag{54}$$

Also $\|\rho-\operatorname{id}\|\leq2$. For the reverse inequality, choose a measurable arc $E$ of positive measure so small that $E$, $\omega E$, and $\omega^2E$ are pairwise disjoint, and set

$$g=1_E-1_{\omega E}. \tag{55}$$

Then $\|g\|_\infty=1$, while for almost every $z\in E$,

$$((\rho-\operatorname{id})g)(z)
=g(\omega z)-g(z)=-1-1=-2. \tag{56}$$

Thus

$$\|\rho-\operatorname{id}\|=2. \tag{57}$$

Finally, every inner automorphism of an abelian algebra is the identity, whereas $\rho\neq\operatorname{id}$. Hence $\rho$ is outer. Equations (54) and (57) show that both constants in (45) are sharp and that both inequalities must remain strict.

The mathematical sources are M. Takesaki, *Theory of Operator Algebras II*, Theorem XI.3.6, Lemma XI.3.7, Corollary XI.3.8 and Remark XI.3.9, printed pages 355–356, with the principal branch introduced on page 354 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)); and *Theory of Operator Algebras I*, first edition, Chapter I, exercise 4, printed page 57. The proofs above treat arbitrary C*-algebras, bounded Banach-algebra groups and arbitrary von Neumann algebras with their stated norms and topologies.
