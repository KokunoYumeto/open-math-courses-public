# Central averaging and maximal ideals

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

In a von Neumann algebra, finite averages of unitary conjugates can approach the centre in norm. They can do so simultaneously for finitely many elements, and successive averages can be arranged to converge. In a finite algebra the central limit is its centre-valued trace. In general the central limits need not be unique, but they still determine the maximal norm-closed ideals.

Prerequisites are [Projections and types](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html), Theorem 5.5 on central comparison, the finite/properly infinite decomposition in Theorem 7.2, and Proposition 15.2 on countable absorption. We use the centre-valued trace already constructed in [Traces on von Neumann algebras, Part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html), Theorem 5.2. We also use spectral projections and [C*-algebra functional calculus](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html), including closed ideals and commutative Gelfand theory. Each of these programme results has a complete proof under its stated background inputs.

Blackadar’s freely accessible corrected manuscript treats Dixmier averaging and its finite-algebra uniqueness form. The proof below develops the spectral-width estimate, simultaneous convergent averages, converse finiteness test and maximal-ideal correspondence in full. The type III argument retains its sigma-finiteness hypothesis, and Lemma 5.1 retains the closure on the central-ideal side.

Let \(M\) be a von Neumann algebra and \(Z=Z(M)\). No separability or sigma-finiteness is assumed until Section 4. Put
\[
D(a)=\overline{\operatorname{co}}^{\,\|\cdot\|}
\{uau^*:u\in\mathcal U(M)\},\qquad
D_{\mathrm w}(a)=\overline{\operatorname{co}}^{\,\sigma\text{-weak}}
\{uau^*:u\in\mathcal U(M)\}.
\tag{0.1}
\]
An **averaging map** is a finite convex combination
\[
F(x)=\sum_{j=1}^r t_j u_jxu_j^*,
\quad t_j\geq0,\quad \sum_jt_j=1.
\tag{0.2}
\]
These maps are positive, unital, contractive and fix \(Z\). Their composites are averaging maps. In particular
\[
\operatorname{dist}(F(x),Z)\leq\operatorname{dist}(x,Z).
\tag{0.3}
\]

## 1. Shrinking the spectral width

For a self-adjoint \(h\) in a nonzero central corner \(Mz\), write
\[
\alpha_z(h)=\min\sigma_{Mz}(hz),\quad
\beta_z(h)=\max\sigma_{Mz}(hz),\quad
w_z(h)=\beta_z(h)-\alpha_z(h).
\]
The zero-width case is already scalar in that corner.

**Lemma 1.1.** For \(h=h^*\in M\), there are a central projection \(z\) and a self-adjoint unitary \(u\) such that \(k=(h+uhu^*)/2\) satisfies
\[
w_z(k)\leq\tfrac34w_1(h),\qquad
w_{1-z}(k)\leq\tfrac34w_1(h)
\tag{1.1}
\]
on every nonzero indicated corner.

**Proof.** Put \(\alpha=\alpha_1(h)\), \(\beta=\beta_1(h)\), \(m=(\alpha+\beta)/2\), and take the lower spectral projection
\[
p=1_{(-\infty,m]}(h),\qquad q=1-p.
\]
Then
\[
\alpha p\leq hp\leq mp,\qquad
mq\leq hq\leq\beta q.
\tag{1.2}
\]
The comparison theorem gives \(z\in\operatorname{Proj}(Z)\) with \(pz\precsim qz\) and \(q(1-z)\precsim p(1-z)\).

On \(Mz\), choose \(v\) with \(v^*v=pz\), \(vv^*=f\leq qz\). The operator
\[
u_z=v+v^*+(qz-f)
\]
is a self-adjoint unitary in the corner: it exchanges \(pz\) and \(f\), and is the identity on their orthogonal complement. Inequality (1.2) implies
\[
hz\geq\alpha pz+m qz,\qquad
u_zhzu_z\geq\alpha f+m(pz+qz-f).
\]
Therefore
\[
\tfrac12(hz+u_zhzu_z)
\geq\tfrac{\alpha+m}{2}(pz+f)+m(qz-f)
\geq\tfrac{\alpha+m}{2}z.
\]
The upper bound is \(\beta z\). Their difference is \(3(\beta-\alpha)/4\).

On \(M(1-z)\), exchange \(q(1-z)\) with a subprojection of \(p(1-z)\), using a partial isometry in the other comparison. The reversed estimates give
\[
\alpha(1-z)\leq k(1-z)
\leq\tfrac{\beta+m}{2}(1-z).
\]
Its width has the same bound. The sum of the two corner unitaries gives \(u\). Zero corners can be omitted. \(\square\)

**Corollary 1.2.** For every self-adjoint \(h\) and every \(\varepsilon>0\), some averaging map \(F\) and \(c\in Z_{\mathrm{sa}}\) satisfy
\[
\|F(h)-c\|<\varepsilon.
\tag{1.3}
\]

**Proof.** Start with the central partition \(\{1\}\). Apply Lemma 1.1 separately in every nonzero member of the current finite partition, combine the corner unitaries into a global unitary, and refine the partition by the resulting comparison cuts. After \(n\) steps the largest corner width is at most
\[
(3/4)^n w_1(h).
\]
For the final averaged operator, take \(c\) to be the sum of the corner spectral midpoints multiplied by their central projections. The spectral theorem bounds the norm error by half the largest width. Choose \(n\) large enough. \(\square\)

The comparison cut can change at every step. The proof controls a finite central partition, rather than asserting that the global spectral width itself always shrinks.

## 2. Simultaneous averages and an actual central limit

**Lemma 2.1.** Given \(a_1,\ldots,a_m\in M\) and \(\varepsilon>0\), there is one averaging map \(F\) such that
\[
\operatorname{dist}(F(a_i),Z)<\varepsilon\quad(1\leq i\leq m).
\tag{2.1}
\]

**Proof.** List the real and imaginary parts of the \(a_i\). Apply Corollary 1.2 to the first, then to the image of the second under the first average, and continue through the finite list. Once an image is within \(\varepsilon/2\) of \(Z\), subsequent averages preserve this bound by (0.3). The final composite works for every \(a_i\), because distance to \(Z\) is subadditive and invariant under scalar multiplication. \(\square\)

**Theorem 2.2.** For every finite family \(a_1,\ldots,a_m\), there is a sequence of averaging maps \(F_n\) and \(c_1,\ldots,c_m\in Z\) such that
\[
\|F_n(a_i)-c_i\|\longrightarrow0
\quad(1\leq i\leq m).
\tag{2.2}
\]
Every norm-closed convex subset of \(M\) invariant under unitary conjugation, if nonempty, meets \(Z\).

**Proof.** Choose an average \(F_1\) making each distance to \(Z\) less than \(2^{-1}\). Inductively apply Lemma 2.1 to the family \(F_n(a_i)\), with error \(2^{-(n+1)}\), and put
\[
F_{n+1}=G_{n+1}F_n.
\]
Choose \(c_{i,n}\in Z\) with \(\|F_n(a_i)-c_{i,n}\|<2^{-n}\). Since \(G_{n+1}\) fixes the centre,
\[
\begin{aligned}
\|F_{n+1}(a_i)-F_n(a_i)\|
&=\|G_{n+1}(F_n(a_i)-c_{i,n})
-(F_n(a_i)-c_{i,n})\|\\
&<2^{1-n}.
\end{aligned}
\tag{2.3}
\]
The series of these bounds converges, so each image sequence is norm Cauchy. Its limit is central because its distance to \(Z\) tends to zero and \(Z\) is norm closed.

For a nonempty invariant convex set, choose any \(a\) in it. Every averaged image of \(a\) belongs to the set, and its central norm limit belongs by closedness. \(\square\)

In particular \(D(a)\cap Z\ne\varnothing\). An approximate approach to the centre alone would not prove this: the centre need not be norm compact. Estimate (2.3) provides convergence.

## 3. Finite algebras and uniqueness

**Theorem 3.1.** The following are equivalent:

1. \(M\) is finite.
2. \(D(a)\cap Z\) is a singleton for every \(a\in M\).
3. \(D_{\mathrm w}(a)\cap Z\) is a singleton for every \(a\in M\).

In the finite case both singletons are \(\{T_M(a)\}\), where \(T_M\) is the existing centre-valued trace.

**Proof.** If \(M\) is finite, the imported trace is normal, bounded, fixes \(Z\), and satisfies \(T_M(uau^*)=T_M(a)\). It is therefore constant on both hulls in (0.1). Any central point in either hull equals its own trace and hence equals \(T_M(a)\). Theorem 2.2 supplies a central point in the smaller hull, proving all the finite-case assertions.

Clearly condition 3 implies condition 2. We prove the converse to finiteness by an explicit witness. If \(M\) is not finite, the imported central decomposition gives a nonzero central projection \(z\) with \(Mz\) properly infinite. In that corner choose orthogonal \(p,r\), both equivalent to \(z\). Then \(p\sim z\), and \(z-p\sim z\) as well: it contains \(r\sim z\) and is at most \(z\), so projection Schröder–Bernstein applies.

For every \(n\geq2\), partition \(z=q_1+\cdots+q_n\) with \(q_j\sim z\). To construct such a finite partition, put \(n\) orthogonal copies of \(z\) inside \(z\), and absorb the remainder into the last copy by Schröder–Bernstein. For each \(j\), both \(q_j\) and \(z-q_j\) are equivalent to \(z\). The equivalences \(p\sim q_j\) and \(z-p\sim z-q_j\) combine into a unitary of \(Mz\) carrying \(p\) to \(q_j\). Extending by \(1-z\) gives a unitary in \(M\). Their average sends \(p\) to \(z/n\), so
\[
0\in D(p).
\]
Also \(p\) and \(z-p\) are unitarily conjugate. Thus
\[
D(p)=D(z-p)=z-D(p),
\]
and \(z\in D(p)\) as well. Two different central points contradict condition 2. \(\square\)

The quantifier “for every \(a\)” matters. Even an infinite algebra has singleton central hulls for its central elements.

**Corollary 3.2.** For every norm-closed two-sided ideal \(I\) of a finite \(M\),
\[
T_M(I)=I\cap Z.
\tag{3.1}
\]

**Proof.** If \(a\in I\), all its unitary conjugates, averages and norm limits lie in \(I\). Theorem 3.1 therefore gives \(T_M(a)\in I\cap Z\). Conversely \(T_M\) fixes \(I\cap Z\). \(\square\)

Finite factors are simple, as already proved in the prerequisite projection lesson, Exercise 15.5(f). Formula (3.1) gives the same conclusion directly for closed ideals by faithfulness of \(T_M\); the algebraic-ideal statement follows by the invertible-element argument in that existing exercise.

## 4. A nonzero central point in the type III case

**Theorem 4.1.** If \(M\) is sigma-finite of type III and \(a\ne0\), then
\[
D(a)\cap Z\ne\{0\}.
\tag{4.1}
\]

**Proof.** Choose either \(h=\operatorname{Re}a\) or \(h=\operatorname{Im}a\), nonzero. After changing sign and scaling this component, it suffices to work with a self-adjoint \(h\) of norm at most one and a nonzero spectral projection
\[
e=1_{[\delta,1]}(h),\qquad \delta>0.
\]
Let \(z=c(e)\). On the central corner \(Mz\),
\[
hz\geq\delta e-(z-e).
\tag{4.2}
\]
If \(z_0=z-c(z-e)\ne0\), then \(e\geq z_0\), so \(hz_0\geq\delta z_0\). This positive lower bound on a central corner is preserved by every averaging map. A central limit of \(a\) supplied by Theorem 2.2 has a nonzero corresponding real or imaginary component on \(z_0\).

Otherwise \(c(z-e)=z=c(e)\). In a sigma-finite type III algebra, every nonzero projection is properly infinite. Proposition 15.2(4) of the projection lesson, applied in \(Mz\), gives
\[
e\sim z-e\sim z.
\]
Partition \(e\) into \(N-1\) orthogonal projections each equivalent to \(z\), where \(N\) is chosen so that
\[
(N-1)\delta>1.
\]
Together with \(z-e\) these form \(N\) equivalent projections summing to \(z\). Choose matrix units connecting them; their cyclic shift is a unitary \(u\) in \(Mz\), with \(u^N=z\). Average over the cyclic group, extending its unitaries by \(1-z\). Inequality (4.2) becomes
\[
\frac1N\sum_{j=0}^{N-1}u^jhz\,u^{-j}
\geq\frac{(N-1)\delta-1}{N}z>0.
\tag{4.3}
\]
Apply Theorem 2.2 to the corresponding average of \(a\). The strictly positive lower bound for the chosen real or imaginary component survives all subsequent averages because \(z\) is central. The resulting central point is nonzero. \(\square\)

Countability enters through equivalence of full-central-support properly infinite projections in Proposition 15.2. The assertion is not extended here to arbitrary non-sigma-finite type III algebras.

## 5. Closure and central intersection of ideals

We need a closure statement that also applies to algebraic, possibly nonclosed, two-sided ideals.

**Lemma 5.1.** For any two-sided ideal \(J\subseteq M\),
\[
\overline J^{\,\|\cdot\|}\cap Z
=\overline{J\cap Z}^{\,\|\cdot\|}.
\tag{5.1}
\]
If \(J\cap Z\) is already norm closed, its closure can be omitted.

**Proof.** Only the left-to-right inclusion requires work. Let \(c\in\overline J\cap Z\). A norm-closed two-sided C*-ideal is self-adjoint, so \(|c|\in\overline J\). For \(\varepsilon>0\), the central spectral projection
\[
e_\varepsilon=1_{[\varepsilon,\infty)}(|c|)
\]
belongs to \(\overline J\), since it is \(|c|\,b_\varepsilon(|c|)\) for a bounded Borel function \(b_\varepsilon\). Approximate it by \(b\in J\) with \(\|b-e_\varepsilon\|<1\). The central compression \(be_\varepsilon\) is in \(J\cap Me_\varepsilon\) and is invertible in the unital corner \(Me_\varepsilon\). Multiplying by its inverse gives \(e_\varepsilon\in J\cap Z\). Consequently \(ce_\varepsilon\in J\cap Z\), and
\[
\|c-ce_\varepsilon\|\leq\varepsilon.
\]
This proves (5.1). The zero spectral corner requires no approximation. \(\square\)

The right side in (5.1) must be closed. For example, the finitely supported sequences form a nonclosed ideal in \(M=Z=\ell^\infty\); its closure is \(c_0\).

For a norm-closed ideal \(L\subseteq Z\), define
\[
J_L=\{x\in M:
D(axb)\cap Z\subseteq L
\ \hbox{for every }a,b\in M\}.
\tag{5.2}
\]

**Lemma 5.2.** \(J_L\) is a norm-closed two-sided ideal, \(J_L\cap Z=L\), and it contains every norm-closed ideal \(I\subseteq M\) satisfying \(I\cap Z\subseteq L\).

**Proof.**

*Addition and scalar multiplication.* Multiplication on either side follows immediately by changing the labels \(a,b\) in (5.2). Scalar multiplication follows from \(D(\lambda x)=\lambda D(x)\), with zero handled separately. To prove addition, take \(x,y\in J_L\), \(a,b\in M\), and \(c\in D(a(x+y)b)\cap Z\). For \(\varepsilon>0\), choose an averaging map \(F\) with
\[
\|F(a(x+y)b)-c\|<\varepsilon.
\]
Apply Theorem 2.2 simultaneously to \(F(axb)\) and \(F(ayb)\). Their central limits \(c_1,c_2\) lie in \(D(axb)\cap Z\) and \(D(ayb)\cap Z\), hence in \(L\). Subsequent averages fix \(c\) and are contractions, so
\[
\|c_1+c_2-c\|\leq\varepsilon.
\]
Closedness of \(L\), as \(\varepsilon\downarrow0\), gives \(c\in L\).

*Central intersection.* If \(x\in J_L\cap Z\), take \(a=b=1\) to get \(x\in L\). Conversely let \(x\in L\). Identify \(Z=C(S)\) by commutative Gelfand theory, and let \(F\subseteq S\) be the common zero set of \(L\). A closed ideal of \(C(S)\) consists exactly of the functions vanishing on \(F\). One elementary justification is this: away from \(F\), finitely many squared absolute values of elements of \(L\) have a strictly positive sum on any specified compact set; division by that sum and a cutoff approximates every function vanishing on \(F\).

Fix \(a,b\) and \(c\in D(axb)\cap Z\). At \(s\in F\), \(x(s)=0\). The central positive contraction
\[
f_\varepsilon=\max\{0,1-|x|/\varepsilon\}
\]
satisfies \(f_\varepsilon(s)=1\) and \(\|f_\varepsilon x\|\leq\varepsilon\). Multiplying every average converging to \(c\) by \(f_\varepsilon\) gives
\[
|c(s)|\leq\|f_\varepsilon c\|
\leq\varepsilon\|a\|\,\|b\|.
\]
Thus \(c(s)=0\), so \(c\in L\). This proves \(L\subseteq J_L\) and therefore \(J_L\cap Z=L\).

*Largest ideal and closedness.* If \(I\) is norm closed and \(I\cap Z\subseteq L\), then \(axb\in I\) for \(x\in I\), and \(D(axb)\subseteq I\). Hence \(x\in J_L\). To apply this to \(\overline{J_L}\), first use Lemma 5.1:
\[
\overline{J_L}\cap Z
=\overline{J_L\cap Z}=L.
\]
The largest-ideal property gives \(\overline{J_L}\subseteq J_L\). Thus \(J_L\) is norm closed. \(\square\)

## 6. Maximal ideals are parametrized by the centre

**Theorem 6.1.** Intersection with the centre gives a bijection
\[
\{\text{maximal proper two-sided ideals of }M\}
\longleftrightarrow
\{\text{maximal proper ideals of }Z\}.
\tag{6.1}
\]
Its inverse sends \(L\) to \(J_L\) from (5.2). In particular a factor has exactly one maximal proper two-sided ideal.

**Proof.** Maximal proper ideals in a unital C*-algebra are norm closed. Indeed, a dense ideal contains an element within distance less than one of the identity, hence an invertible element, so it cannot be proper. The closure of a proper ideal is therefore proper, and maximality makes the ideal equal to its closure.

If \(L\) is maximal in \(Z\), then \(J_L\) is proper since its central intersection is \(L\). Let \(I\) be a proper closed ideal containing \(J_L\). Its central intersection contains \(L\) and is proper, because it does not contain \(1\). Hence \(I\cap Z=L\), and Lemma 5.2 gives \(I\subseteq J_L\). Any larger proper algebraic ideal would have a proper closed ideal as its closure, so \(J_L\) is maximal.

Conversely, for a maximal proper ideal \(I\) of \(M\), choose a maximal ideal \(L\) of the unital commutative algebra \(Z\) containing \(I\cap Z\). Lemma 5.2 gives \(I\subseteq J_L\), and \(J_L\) is proper. Thus \(I=J_L\), with \(I\cap Z=L\). The inverse is unique by this construction.

For a factor, \(Z=\mathbb C1\) has only the maximal proper ideal \(\{0\}\), yielding exactly one maximal ideal of \(M\). That maximal ideal need not itself be zero. \(\square\)

**Corollary 6.2.** For a finite \(M\), let \(S\) be the spectrum of \(Z\). The maximal ideal at \(s\in S\) is
\[
I_s=\{x\in M:T_M(x^*x)(s)=0\}.
\tag{6.2}
\]

**Proof.** The functional \(\tau_s(x)=T_M(x)(s)\) is a tracial state. It need not be normal. By Theorem 3.1, \(x\in J_{\ker s}\) implies \(T_M(x^*x)(s)=0\), by taking \(a=x^*,b=1\).

Conversely, suppose \(\tau_s(x^*x)=0\). For every \(a,b\),
\[
\begin{aligned}
\tau_s((axb)^*(axb))
&\leq\|a\|^2\tau_s(b^*x^*xb)\\
&=\|a\|^2\tau_s(x^*xbb^*)\\
&\leq\|a\|^2\|b\|^2\tau_s(x^*x)=0.
\end{aligned}
\]
The middle expression is real and nonnegative by the trace identity, or by writing it as the trace of a positive sandwich. Cauchy–Schwarz gives \(\tau_s(axb)=0\). Since the central hull of \(axb\) is its trace, every such hull lies in \(\ker s\). Thus \(x\in J_{\ker s}=I_s\). \(\square\)

## 7. Graded exercises with complete solutions

### Exercise 7.1 — An exact matrix average (basic)

Let \(h=\operatorname{diag}(5,1,-2)\in M_3(\mathbb C)\). Average it over the three powers of the cyclic basis permutation. Compute the result and identify the central point of \(D(h)\). Explain what happens for an arbitrary matrix \(a\).

**Solution.** Each diagonal entry occurs once in every coordinate, so the average is
\[
\frac{5+1-2}{3}1_3=\frac43\,1_3.
\]
The centre-valued trace of \(M_3\) is \(\operatorname{Tr}(a)1_3/3\), and Theorem 3.1 makes it the unique central hull point. For a general matrix, cyclic permutation alone need not remove the off-diagonal entries. First average conjugation by the three diagonal unitaries
\[
\operatorname{diag}(1,\omega^j,\omega^{2j}),\qquad
j=0,1,2,\quad \omega=e^{2\pi i/3}.
\]
The geometric sums kill every off-diagonal entry. A subsequent cyclic-permutation average yields exactly \(\operatorname{Tr}(a)1_3/3\).

### Exercise 7.2 — The unique maximal ideal of \(B(\ell^2)\) (intermediate)

Use Theorem 6.1 to show that the Calkin algebra is simple. Do not assume its simplicity in applying the theorem. Identify the maximal ideal of \(B(\ell^2)\).

**Solution.** The nonzero unital Calkin algebra has a maximal proper ideal: apply Zorn's lemma, observing that a union of a chain of proper ideals cannot contain the identity. Its inverse image under the quotient map is a maximal ideal of \(B(\ell^2)\) containing the compact operators. Theorem 6.1 says that this factor has only one maximal ideal, say \(I\).

Every proper ideal of \(B(\ell^2)\) consists of compact operators. Indeed, if it contains a noncompact \(a\), then for some \(\varepsilon>0\) the spectral projection \(p=1_{[\varepsilon,\infty)}(|a|)\) has infinite rank. Otherwise cutting \(|a|\) by these finite-rank projections would approximate it in norm, making \(|a|\), and hence \(a\), compact. Since the norm-closed ideal generated by \(a\) contains \(|a|\), the projection \(p\) belongs to it by bounded Borel division. On the separable infinite-dimensional space \(p\sim1\), so that closed ideal contains \(1\). It follows that the original ideal is dense and hence contains an invertible element. It is the whole algebra. Therefore the proper maximal ideal \(I\) is contained in \(\mathcal K\), and its known containment of \(\mathcal K\) gives \(I=\mathcal K\).

Now every proper ideal of the quotient has proper inverse image containing \(\mathcal K\), so its inverse image equals \(\mathcal K\). The quotient ideal is zero. Thus the Calkin algebra is simple. The normality corollary in [Proper infiniteness and automatic normality](../reader/proper-infiniteness-and-automatic-normality.html) also explains why the quotient cannot be represented nontrivially on a separable Hilbert space.

### Exercise 7.3 — A maximal ideal at infinity in a finite matrix product (advanced)

Let \(M=\prod_{n\geq1}M_n(\mathbb C)\), and fix a free ultrafilter \(\mathcal V\) on \(\mathbb N\). Write \(\operatorname{tr}_n=\operatorname{Tr}/n\). Identify the maximal ideal associated with the central character \(\lim_{\mathcal V}\). Show that the coordinate rank-one projections form an element of that ideal with norm one. Does the ideal contain the identity?

**Solution.** \(M\) is finite, with
\[
T_M((a_n))=(\operatorname{tr}_n(a_n))_n.
\]
Corollary 6.2 gives
\[
I_{\mathcal V}=
\{(a_n):\lim_{\mathcal V}\operatorname{tr}_n(a_n^*a_n)=0\}.
\]
Choose a rank-one projection \(p_n\) in every coordinate. Then \(\|(p_n)\|=1\), while
\[
\lim_{\mathcal V}\operatorname{tr}_n(p_n)=
\lim_{\mathcal V}\frac1n=0.
\]
Thus \((p_n)\in I_{\mathcal V}\). On the other hand \(T_M(1)=1\), so the identity is not in the ideal. This maximal quotient detects normalized trace size, rather than requiring coordinate operator norms to tend to zero.

## References

- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, freely accessible corrected manuscript. [Author’s PDF](https://bruceblackadar.com/Mathematics/Cycr.pdf).
- The projection and trace lessons linked above supply the comparison, type and centre-valued-trace results, with proofs and their historical attributions.
