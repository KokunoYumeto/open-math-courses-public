# Self-adjoint spectral calculus with the original domain

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

The bounded input is the complete local [Unitary spectral foundation](unitary-spectral-foundation.md#unitary-pvm): finite norm control of Laurent polynomials, Fejér density, a full compact-metric positive measure construction, cyclic representations and an arbitrary-cardinality reducing direct sum. That proof requires no normal spectral theorem or general C*-algebra representation. The bounded-normal spectral theorem is a compatible CC0 comparison, with original credit to Claude Opus 5.5 and GPT-6.1 Sol. The active proof input is the checked local unitary construction, including its proof of integration against an arbitrary PVM by finite simple sums. That full domain passage is the following argument.

<a id="self-adjoint-pvm-domain"></a>

For further reading, Gerald Teschl's [*Mathematical Methods in Quantum Mechanics*, second author edition, 2014](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), Theorem 2.26, printed pp.91–92, gives the Cayley correspondence, and Section 3.1, pp.100–110, gives bounded and unbounded spectral multipliers. The construction below supplies every domain equality it uses. The local unitary foundation proves the arbitrary-cardinality cyclic decomposition; the countable decomposition in Teschl's separable setting is not assumed for an arbitrary Hilbert space.

## The precise theorem

Let $H$ be any complex Hilbert space and $A:D(A)\subset H\to H$ be densely defined and self-adjoint. No separability or lower bound is assumed. There is a unique strongly countably additive orthogonal projection-valued measure $E$ on the Borel sets of $\mathbb R$, with $E(\mathbb R)=I$, such that, for $\mu_u(B)=\|E(B)u\|^2$,
\[
 D(A)=\left\{u\in H:\int_{\mathbb R}t^2\,d\mu_u(t)<\infty\right\},
 \qquad Au=\lim_{k\to\infty}\int_{[-k,k]}t\,dE(t)u.
 \tag{1}
\]
For each finite-valued complex Borel function $f$, its spectral operator has the exact maximal domain
\[
 D(f(A))=\left\{u:\int|f|^2\,d\mu_u<\infty\right\},
 \qquad \|f(A)u\|^2=\int|f|^2\,d\mu_u.
 \tag{2}
\]
Bounded Borel functions act everywhere, form a unital star homomorphism, and satisfy strong bounded-pointwise convergence. Formula (1) is equality with the given domain, not a new closure or an extension of $A$. The zero Hilbert space has the unique zero measure and zero operators, so assume $H\ne0$ below. Inner products are linear in the first variable.

<a id="selfadjoint-cayley"></a>
## Cayley transform of the original operator

An adjoint is closed: if $u_j\to u$ and $A^*u_j\to v$, its defining identity against each vector in $D(A)$ passes to the limit and gives $u\in D(A^*)$, $A^*u=v$. Thus our self-adjoint $A$ is closed. For $u\in D(A)$,
\[
 \|(A\pm i)u\|^2=\|Au\|^2+\|u\|^2,
 \tag{3}
\]
since $\langle Au,u\rangle$ is real. These operators are injective and have closed range: a convergent sequence of their images makes both the vectors and their $A$-images Cauchy by (3), and closedness supplies the limiting preimage. The orthogonal complement of each range is $\ker(A\mp i)$, by the definition of the adjoint, so is zero by (3). A closed dense range is all of $H$. Consequently
\[
 R_+=(A+i)^{-1},\quad R_-=(A-i)^{-1}
\]
are everywhere-defined bounded operators of norm at most one, with ranges exactly $D(A)$, and $R_+^*=R_-$ by the adjoint pairing identity. Direct multiplication on the original domains gives
\[
 R_+-R_-=-2iR_+R_-=-2iR_-R_+.
\]
For example apply both sides to a vector and use $(A+i)R_-=I+2iR_-$; the reversed identity follows in the same way. The bounded operator
\[
 U=I-2iR_+=(A-i)(A+i)^{-1}
\]
is unitary: $U^*=I+2iR_-$ and the displayed resolvent identity cancels the cross terms in both products. Also $\ker(I-U)=\ker R_+=0$.

Apply the local unitary spectral foundation to $U$ and denote its PVM by $F$. Its spectrum is contained in the unit circle: for $|z|>1$ the usual convergent geometric series in $U/z$ gives an inverse, and for $|z|<1$ use the series in $zU^*$. This proves that support assertion directly. The squared-norm formula for $(1-z)(U)=I-U$ shows that $F(\{1\})$ projects onto $\ker(I-U)$: its range is killed by $I-U$, while a vector killed by $I-U$ has scalar spectral measure supported on $\{1\}$. Hence $F(\{1\})=0$.

<a id="selfadjoint-real-measure"></a>
## Push the bounded measure to the real line

The maps
\[
 c(t)=\frac{t-i}{t+i},\qquad
 \tau(z)=i\frac{1+z}{1-z}
\]
are inverse homeomorphisms between $\mathbb R$ and the unit circle minus $1$. Indeed $|t-i|=|t+i|$ for real $t$, $c(t)\ne1$, and for $|z|=1$, $z\ne1$, replacing $\bar z$ by $z^{-1}$ shows $\overline{\tau(z)}=\tau(z)$. Direct substitution gives both inverse identities. Their denominators never vanish on their respective domains, so the maps are continuous. Define
\[
 E(B)=F(c(B))\qquad(B\subset\mathbb R\text{ Borel}).
 \tag{4}
\]
Homeomorphisms preserve Borel sets, since their inverse maps are continuous and inverse images respect complements and countable unions. A Borel subset of the punctured circle is also Borel in the circle, because the punctured circle is open. This gives orthogonal projections, intersection products and strong countable additivity from $F$; the omitted point has zero projection, so $E(\mathbb R)=I$. For bounded Borel $f$, define $f(E)$ by the bounded $F$-calculus of $f\circ\tau$ on the punctured circle, with any chosen value at $1$. That value changes no operator. The proved unitary foundation therefore gives the full bounded calculus, including
\[
 \|f(E)u\|^2=\int|f|^2\,d\mu_u,
 \qquad f(E)^*=\overline f(E).
 \tag{5}
\]
The change-of-variable identity for the scalar spectral integrals follows first for indicators from (4), then for simple functions by linearity, and for nonnegative functions by increasing simple approximation; real and imaginary parts give integrable complex functions. The finite-simple-sum proof at the end of the local unitary reading works on any measurable base, including $\mathbb R$: disjoint projections give the norm identity, and uniform simple approximation gives every bounded Borel multiplier. This is also the comparison in Proposition 4.3 of the pinned bounded programme theorem.

For every bounded Borel $h$ and Borel set $B$, bounded multiplicativity gives the useful identity
\[
 \begin{gathered}
 \mu_{h(E)u}(B)=\|(1_Bh)(E)u\|^2\\
 =\int_B|h|^2\,d\mu_u.
 \end{gathered}
 \tag{S1}
\]
In particular $\mu_{E(B)u}=1_B\mu_u$. The associated identity for integrating nonnegative functions follows by simple approximation and monotone convergence.

<a id="selfadjoint-maximal-multipliers"></a>
## Unbounded multipliers, their domains and adjoints

For a finite-valued Borel $f$ put $Q_k=E(\{|f|\leq k\})$ and $f_k=f1_{\{|f|\leq k\}}$. On the domain in (2), (5) makes $f_k(E)u$ Cauchy, because the squared norm of a tail difference is the integral of $|f|^2$ over that tail. The moment domain is a linear subspace: $\mu_{\alpha u}=|\alpha|^2\mu_u$ and $\mu_{u+v}(B)\leq2\mu_u(B)+2\mu_v(B)$, by the squared triangle inequality for $E(B)u+E(B)v$. Integration of nonnegative simple functions and then monotone convergence transfer this inequality to $|f|^2$. Define $T_fu$ to be the limit of the bounded truncations. Their linearity makes $T_f$ linear on that domain. Monotone convergence in (5) gives exactly (2). This domain is dense: $Q_ku\to u$ for every $u$, since $f$ is finite-valued and $\mu_u(\mathbb R)=\|u\|^2$, and $Q_ku\in D(T_f)$ by (S1).

All spectral projections preserve the domain by (S1), since restricting the finite $|f|^2$ integral can only decrease it. Passing their bounded commutation identity to the defining limit proves that they commute with $T_f$ on its domain. Moreover
\[
 Q_kT_fu=f_k(E)u.
 \tag{6}
\]
This also proves that $T_f$ is closed. If $u_j\to u$ and $T_fu_j\to v$, then $Q_kv=f_k(E)u$ for every $k$. Hence $\|f_k(E)u\|\leq\|v\|$. Monotone convergence gives $u\in D(T_f)$; letting $k$ increase in (6) gives $T_fu=v$.

The exact adjoint is $T_f^*=T_{\overline f}$. One inclusion follows by taking limits of the bounded adjoint identity on their common domain $D(T_f)=D(T_{\bar f})$. Conversely let $v\in D(T_f^*)$ with $w=T_f^*v$. Test its defining identity against vectors in $Q_kH\subset D(T_f)$. It gives
\[
 Q_kw=\overline f_k(E)v.
\]
The right-hand side has norm at most $\|w\|$ for every $k$. Formula (5) and monotone convergence give $v\in D(T_{\bar f})$, and then $T_{\bar f}v=w$. In particular $T_f$ is self-adjoint for real $f$.

For later domain calculations, the spectral measure of $T_gu$ satisfies
\[
 \mu_{T_gu}(B)=\int_B|g|^2\,d\mu_u\qquad(u\in D(T_g)).
 \tag{7}
\]
Indeed $E(B)T_gu$ is the limit of $(1_Bg_k)(E)u$, so (5) proves (7). Consequently the *ordered product* has exactly
\[
 D(T_fT_g)=\{u:\int|g|^2d\mu_u<\infty,
                    \ \int|fg|^2d\mu_u<\infty\},
 \quad T_fT_gu=T_{fg}u.
 \tag{8}
\]
To verify the action equality, put $D_k=\{|f|\leq k,|g|\leq k\}$ and $P_k=E(D_k)$. For $u$ in the displayed product domain, (7) gives $T_gu\in D(T_f)$, and bounded multiplication on $P_kH$ gives
\[
 \begin{gathered}
 P_kT_fT_gu=(fg1_{D_k})(E)u\\
 =P_kT_{fg}u.
 \end{gathered}
 \tag{S2}
\]
Here $T_f,T_g,T_{fg}$ commute with $P_k$, and all multipliers restricted to this range are bounded. The projections $P_k$ increase strongly to $I$ because $f,g$ are finite-valued. Taking the limit proves the equality of the two fixed vectors, without presuming convergence in an unproved product graph norm. The extra $g$-domain condition is retained. Thus (8) never replaces an ordered product domain by a larger maximal multiplier domain without justification. Likewise $T_f+T_g=T_{f+g}$ on $D(T_f)\cap D(T_g)$: the inequality $|f+g|^2\leq2|f|^2+2|g|^2$ puts this intersection in $D(T_{f+g})$, and the same $P_k$ applied to the three fixed vectors gives their equality. That intersection is not asserted to be the maximal domain of the sum. Finally Cauchy–Schwarz for the finite measure $\mu_u$ shows $f\in L^1(\mu_u)$ on $D(T_f)$. The bounded pairing identity and dominated convergence therefore give $\langle T_fu,u\rangle=\int f\,d\mu_u$.

<a id="selfadjoint-original-domain"></a>
## Recover the exact original domain

Set $r(t)=(t+i)^{-1}$. The bounded $F$-calculus gives
\[
 r(E)=\frac{I-U}{2i}=R_+.
 \tag{9}
\]
For $u=R_+v$, bounded multiplication and (5) give
\[
 \mu_u(B)=\int_B|r(t)|^2\,d\mu_v(t),\qquad
 \int t^2d\mu_u\leq\|v\|^2.
\]
Thus $D(A)=\operatorname{Ran}R_+\subset D(T_t)$, and
\[
 T_tR_+v=(tr)(E)v=(1-ir)(E)v=v-iR_+v=AR_+v.
 \tag{10}
\]
The multiplier $tr$ is bounded, so this limit follows directly from (5), or from (8). Conversely if $u\in D(T_t)$, put $v=(T_t+i)u$. The bounded multiplier $r$ and the proved product identity give
\[
 R_+v=r(E)(T_t+i)u=u,
\]
since $r(t)(t+i)=1$. Hence $u\in\operatorname{Ran}R_+=D(A)$ and (10) gives $Au=T_tu$. This proves both statements of (1) for the original operator. Truncation by $[-k,k]$ is the same construction used to define $T_t$.

For every nonreal $z$, the bounded Borel function $r_z(t)=(t-z)^{-1}$ satisfies $|r_z|\leq|\operatorname{Im}z|^{-1}$ and $|tr_z|\leq1+|z|/|\operatorname{Im}z|$. Formula (7) thus places $r_z(E)H$ in $D(A)$. The exact product rule proves $(A-z)r_z(E)=I$ on $H$ and $r_z(E)(A-z)=I$ on $D(A)$. Hence
\[
 \begin{gathered}
 (A-z)^{-1}=r_z(E),\\
 \|(A-z)^{-1}\|\leq|\operatorname{Im}z|^{-1},\\
 ((A-z)^{-1})^*=(A-\bar z)^{-1}.
 \end{gathered}
 \tag{S3}
\]
Its range is exactly $D(A)$, as both inverse identities show.

<a id="selfadjoint-uniqueness"></a>
## Uniqueness

Suppose $G$ is any PVM satisfying the exact domain and operator identities (1) for this same $A$. Construct its bounded and maximal unbounded multiplier calculus by the simple-sum and truncation arguments already given. The bounded operator $r(G)$ is the inverse of $A+i$: $(t+i)r(t)=1$ and $|t r(t)|\leq1$ show its range lies in the moment domain and $(A+i)r(G)=I$; on $D(A)$ the opposite identity is the same multiplier computation. Thus $r(G)=R_+$ and $c(G)=I-2iR_+=U$.

Push $G$ forward along $c$ to a PVM on the unit circle, assigning zero mass to $1$. Its integral of the coordinate function is $U$. Uniqueness in the local *unitary spectral foundation* makes it equal to $F$. Pulling back through the inverse homeomorphism gives $G=E$. No uniqueness theorem for an unbounded operator was assumed.

<a id="selfadjoint-groups-and-powers"></a>
## Groups, powers and lower-bound specializations

For real $s$, $e^{isA}=(e^{ist})(E)$ is unitary and its group law follows from bounded multiplicativity. Dominated convergence in (5) proves strong continuity. For $u\in D(A)$,
\[
 \frac{e^{isA}u-u}{s}\longrightarrow iAu,
\]
because scalar differentiation and the fundamental theorem give $(e^{ist}-1)/s=it\int_0^1e^{i\theta st}\,d\theta$. Its absolute value is at most $|t|$, its pointwise limit is $it$, and the difference from $it$ is dominated by $2|t|$. Formula (2) and dominated convergence apply because the squared-integral domain is finite. The exponential, its derivative and the scalar fundamental theorem have their complete proofs in the [elementary reading](elementary-functions-and-cutoffs.md#scalar-exponential) and the [continuous scalar integral](hilbert-valued-integration.md#continuous-primitives). Conversely, if this quotient has a strong limit as $s\to0$, its norms are bounded along a sequence $s_j\to0$. Fatou in (5) gives $\int t^2d\mu_u<\infty$, so $u\in D(A)$ and the limit is $iAu$. Thus the full generator criterion has exactly the original domain.

For every integer $m\geq1$, induction using (8) gives
\[
 D(A^m)=\{u:\int|t|^{2m}d\mu_u<\infty\},\qquad A^m=T_{t^m}.
\]
The lower moments needed at each step follow from $|t|^{2j}\leq1+|t|^{2m}$ for $j\leq m$. If $A\geq aI$, its measure is supported on $[a,\infty)$: on a bounded spectral interval contained in $(-\infty,a-\varepsilon]$, vectors in its projection range lie in $D(A)$ and (1) would give $\langle Au,u\rangle\leq(a-\varepsilon)\|u\|^2$. Such a projection must vanish; a countable union of these bounded intervals covers $(-\infty,a)$. This is a specialization of the full result and never a lower-bound assumption in its construction.
