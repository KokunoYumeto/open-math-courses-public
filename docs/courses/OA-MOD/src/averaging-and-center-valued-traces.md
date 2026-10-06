# Averaging, central traces and normality

**Self-checked by the writing AI.** The arguments rely on the stated results of earlier lessons.

A finite algebra has a canonical way to replace an operator by an element of its center. There are two useful averaging topologies. Ultraweak compactness constructs this replacement from faithful finite traces. Norm approximation then makes it visible to every bounded trace, even a trace whose normality is not known. Keeping these two steps separate prevents a circular proof of normality.

The classical statements correspond to Takesaki, *Theory of Operator Algebras I*, V.2, Proposition 2.5, Theorem 2.6 and Definition 2.7, printed pp. 311–314 (PDF pp. 319–322 in the approved edition). The existing programme lesson Traces on von Neumann algebras, Lemma 5.1, Theorems 5.2, 5.5 and 5.9, and Lemma 8.1–Theorem 8.2, supplies the canonical earlier treatment. Its author is Claude Opus 5.5 (Anthropic), September–October 2026, CC0. This lesson gives a connected explanatory route through those arguments and additional hypothesis checks. The exact compared revisions and proof selections are recorded in the accompanying course evidence.

Throughout, \(M\subseteq B(H)\) is a unital von Neumann algebra, \(Z=Z(M)\), and neither \(H\) nor \(M\) is assumed separable or sigma-finite. A finite trace means a positive tracial functional with \(\tau(1)<\infty\); its linear extension and cyclicity are proved in Trace axioms and the two finite ideals. Finiteness of the algebra instead means that every isometry in \(M\) is unitary. For the zero algebra all the maps below are the unique zero map.

## A norm averaging mechanism

An averaging map is a linear map \(A:M\to M\) of the form

\[
\begin{gathered}
A(x)=\\
\sum_{j=1}^m t_j u_jxu_j^*,\\
t_j\geq0,\\
\sum_jt_j=1.
\end{gathered}
\tag{CT.1}
\]

where the \(u_j\) are unitaries. Such a map is positive, unital and contractive, fixes every element of \(Z\), and satisfies \(A(ax)=aA(x)\) for \(a\in Z\). Compositions are again averaging maps: multiply the coefficients and the unitaries in their given order. Write \(D(x)\) for the norm-closed convex hull of the unitary conjugates of \(x\).

We use one exact earlier projection result: [Projections and types of von Neumann algebras, Theorem 5.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html#oa-fnd-ty-03). For projections \(p,q\in M\), it gives a central projection \(z\) with \(zp\precsim zq\) and \((1-z)q\precsim(1-z)p\). Its proof matches maximal orthogonal families of equivalent subprojections and uses the central orthogonality of their unmatched remainders. No trace is an input to that comparison theorem.

**One-step estimate.** If \(h=h^*\) and \(\|h\|\leq1\), there are a self-adjoint unitary \(u\) and \(c=c^*\in Z\) such that, with \(b=(h+uhu)/2\),

\[
\begin{gathered}
\|c\|\leq\tfrac14,\\
\|b-c\|\leq\tfrac34.
\end{gathered}
\tag{CT.2}
\]

**Proof.** Let \(p=1_{(0,\infty)}(h)\). Bounded spectral calculus, The bounded prerequisite boundary, gives \(-(1-p)\leq h\leq p\). Apply projection comparison to \(p,1-p\), and choose partial isometries \(v,w\in M\) with

\[
\begin{gathered}
v^*v=pz,\\
vv^*\leq(1-p)z,\\
w^*w\\
=(1-p)(1-z),\\
ww^*\leq p(1-z).
\end{gathered}
\tag{CT.3}
\]

The initial and final projections of \(v\) are orthogonal in \(Mz\); those of \(w\) are orthogonal in \(M(1-z)\). Add the two unused remainders and put

\[
\begin{gathered}
r=(1-p)z-vv^*,\\
s=p(1-z)-ww^*,\\
u=v+v^*+r\\
{}+w+w^*+s.
\end{gathered}
\tag{CT.4}
\]

These are two orthogonal exchange blocks with identity on their complements. Multiplication gives \(u=u^*\), \(u^2=1\), \(u(pz)u=vv^*\), and \(u((1-p)(1-z))u=ww^*\).

For \(b=(h+uhu)/2\), the inequalities for \(h\) now give

\[
\begin{gathered}
-z\leq bz\leq\tfrac12z,\\
-\tfrac12(1-z)\\
\leq b(1-z)\leq1-z.
\end{gathered}
\tag{CT.5}
\]

Indeed the first upper bound is \((pz+vv^*)/2\leq z/2\), and the second lower bound is the negative half of \((1-p)(1-z)+ww^*\), which is at least \(-(1-z)/2\); the remaining bounds follow from \(-1\leq h\leq1\). Set \(c=(1-2z)/4\). Subtracting its two central components gives \(-3/4\leq b-c\leq3/4\), proving the estimate. \(\square\)

**Norm averaging theorem.** For every \(x\in M\), \(D(x)\cap Z\neq\varnothing\).

**Proof for self-adjoint elements.** Starting from \(h_0=h\), scale the one-step estimate to choose an averaging map \(A_{n+1}\), a central self-adjoint \(c_{n+1}\), and a remainder

\[
\begin{gathered}
h_{n+1}=A_{n+1}(h_n)\\
{}-c_{n+1},\\
\|h_{n+1}\|\\
\leq(3/4)\|h_n\|,\\
\|c_{n+1}\|\leq\|h_n\|/4.
\end{gathered}
\tag{CT.6}
\]

For \(h_n=0\) take the identity averaging map and \(c_{n+1}=0\). If \(B_n=A_n\cdots A_1\), central elements are fixed, so induction gives \(B_n(h)=h_n+\sum_{j=1}^n c_j\). The remainder tends to zero and the central series converges absolutely in norm. Thus the averaging maps send \(h\) in norm to a central element.

**Passage to complex elements.** Given \(x=h+ik\), with \(h,k\) self-adjoint, and \(\varepsilon>0\), first average \(h\) within \(\varepsilon/2\) of a central self-adjoint element \(a\). Then average the resulting image of \(k\) within \(\varepsilon/2\) of a central self-adjoint element \(b\). The second averaging map fixes \(a\) and is contractive, so their composition sends \(x\) within \(\varepsilon\) of \(a+ib\).

Approximation by central elements alone needs a convergence argument. Choose \(B_1,c_1\) with \(\|B_1(x)-c_1\|\leq2^{-1}\). If \(\|B_n(x)-c_n\|\leq2^{-n}\), apply the preceding approximation to this remainder with error \(2^{-n-1}\), obtaining an averaging map \(A\) and central \(d_n\). Set \(B_{n+1}=AB_n\) and \(c_{n+1}=c_n+d_n\). Writing \(e_{n+1}=B_{n+1}(x)-c_{n+1}\), contractivity gives

\[
\begin{gathered}
\|e_{n+1}\|\\
\leq2^{-n-1},\\
\|d_n\|\\
\leq2^{-n}+2^{-n-1}.
\end{gathered}
\tag{CT.7}
\]

Consequently \(c_n\) converges in \(Z\), and \(B_n(x)\) has the same norm limit. Every \(B_n(x)\) is a convex combination of unitary conjugates of \(x\), so this limit belongs to \(D(x)\). \(\square\)

## Constructing the central value on a faithful finite block

Assume for this section that \(M\) has a faithful normal finite trace \(\tau\). Let \(K(x)\) be the ultraweakly closed convex hull of the unitary conjugates of \(x\). It is nonempty and compact: it is a closed subset of the radius-\(\|x\|\) ball, which is ultraweakly compact by The concrete predual and its intrinsic norm and Dual-ball compactness and the bidual criterion. The positive cone is ultraweakly closed by Positive functionals, closed cones and norm closure.

Put \(N(y)=\tau(y^*y)\). This function is ultraweakly lower semicontinuous. To see it directly, if \(y_i\to y\) ultraweakly, multiplication by the fixed \(y^*\) and normality of \(\tau\) give \(\tau(y^*y_i)\to N(y)\). Cauchy–Schwarz gives \(|\tau(y^*y_i)|^2\leq N(y)N(y_i)\). If \(N(y)>0\), division followed by a lower limit proves \(N(y)\leq\liminf_iN(y_i)\); if \(N(y)=0\), positivity proves it. The normal functional and multiplication facts are The concrete predual and its intrinsic norm through The sigma-strong seminorms are vector seminorms and The scalar normality criterion.

The closed sublevel sets at \(\inf_{K(x)}N+1/n\) have the finite intersection property. Compactness therefore gives a minimizer. The parallelogram identity implies that two minimizers \(y_1,y_2\) satisfy \(N(y_1-y_2)=0\); faithfulness makes them equal. Unitary conjugation preserves both \(K(x)\) and \(N\), so the unique minimizer commutes with every unitary. By Testing commutation on unitaries, it is central. Denote it by \(T_\tau(x)\).

For every \(a\in Z\), the normal functional \(y\mapsto\tau(ay)\) is constant on the unitary orbit, hence on its ultraweakly closed convex hull. Thus

\[
\begin{gathered}
\tau(aT_\tau(x))=\tau(ax),\\
a\in Z.
\end{gathered}
\tag{CT.8}
\]

Conversely, at most one central element satisfies these equations: for two of them take \(a\) to be the adjoint of their difference and use faithfulness. This characterization proves complex linearity, \(Z\)-linearity, and \(T_\tau(a)=a\) for \(a\in Z\). It also proves

\[
\begin{gathered}
T_\tau(x^*x)\\
=T_\tau(xx^*)\geq0.
\end{gathered}
\tag{CT.9}
\]

For positivity, the hull of a positive element lies in the positive cone. For the equality, first take \(a\in Z_+\) and use the trace identity on \(xa^{1/2}\) in (CT.8), then write a general central element as a linear combination of positive ones. Finally \(T_\tau(x^*x)=0\) implies \(\tau(x^*x)=0\), hence \(x=0\). Membership in \(K(x)\) gives \(\|T_\tau(x)\|\leq\|x\|\).

Normality can be proved here without any assertion about nonnormal traces. If \(0\leq x_i\uparrow x\), the bounded increasing net \(T_\tau(x_i)\) has a supremum \(c\in Z_+\) by Bounded increasing positive nets have strong suprema. For \(a\in Z_+\), multiplication by \(a\) preserves these increasing suprema, and

\[
\begin{gathered}
\tau(ac)\\
=\sup_i\tau(aT_\tau(x_i))\\
=\sup_i\tau(ax_i)\\
=\tau(ax).
\end{gathered}
\tag{CT.10}
\]

Here \(\tau(a\,\cdot\,)\) is the normal positive functional \(\tau(a^{1/2}(\cdot)a^{1/2})\). Extend the equality by linearity to every \(a\in Z\); uniqueness in (CT.8) gives \(c=T_\tau(x)\). The positive-map theorem The positive-map equivalence then gives ultraweak continuity of the linear map \(T_\tau:M\to Z\).

## Arbitrary finite algebras and the converse

**Existence theorem.** If \(M\) is finite, there is a normal linear map \(T:M\to Z\) with

\[
\begin{gathered}
T(x^*x)\\
=T(xx^*),\\
T(x^*x)\geq0,\\
T(ax)=aT(x),\\
a\in Z,\\
T(1)=1,\\
T(x^*x)=0\\
\Longrightarrow x=0.
\end{gathered}
\tag{CT.11}
\]

It is contractive, fixes \(Z\) pointwise, and is onto \(Z\). Conversely, existence of such a map forces \(M\) to be finite.

**Construction and return from the blocks.** First, central summands of a finite algebra are finite: if \(v\in Mz\) satisfies \(v^*v=z\) for a central projection \(z\), then \(v+(1-z)\) is an isometry of \(M\). Its unitarity gives \(vv^*=z\). The exact earlier separating-trace theorem is Separating traces and the support of the selected trace, importing Theorem 4.7 of the programme trace lesson. It says that finite normal traces separate the positive elements of any finite algebra. The complete proof uses its stated predual compactness and group fixed-point inputs; we do not replace that theorem by the minimization argument of CT-02, which already needs a faithful trace.

Choose by Zorn's lemma a maximal family \((\tau_j)_{j\in J}\) of nonzero finite normal traces with mutually orthogonal supports \(z_j\). These supports are central, and restriction to \(Mz_j\) is faithful, by Null support is a different central projection. Their sum is \(1\): otherwise the finite summand \(M(1-\sum_jz_j)\) has a nonzero finite normal trace by the separating-trace theorem, which extends by the central compression to a trace with support orthogonal to all \(z_j\). That contradicts maximality.

CT-02 supplies \(T_j:Mz_j\to Zz_j\). For \(x\in M\) the elements \(T_j(xz_j)\) act on orthogonal subspaces and have norms at most \(\|x\|\). Their finite sums therefore converge strongly to an operator of norm at most \(\|x\|\): the squared norm of each tail on a vector is bounded by \(\|x\|^2\) times the squared norm of the corresponding orthogonal tail of that vector. Strong closure of \(M\) and commutation with all its elements put the limit in \(Z\). Define

\[
\begin{gathered}
T(x)z_j=T_j(xz_j),\\
j\in J.
\end{gathered}
\tag{CT.12}
\]

These equalities uniquely determine \(T(x)\), since \(\sum_jz_j=1\). They prove linearity, central linearity, normalization and positivity. They also transfer the trace identity, because \((xz_j)^*(xz_j)=x^*xz_j\) and \((xz_j)(xz_j)^*=xx^*z_j\). If \(T(x^*x)=0\), every \(xz_j=0\), so \(x=0\). If \(x_i\uparrow x\), their central images have supremum \(c\leq T(x)\), and normality on each block gives \(cz_j=T(x)z_j\); hence \(c=T(x)\). Again NP-04 gives ultraweak continuity. Finally central linearity and \(T(1)=1\) imply \(T(a)=a\), so the map is onto. No countability of \(J\) was used.

**Converse.** If \(v^*v=1\), the trace identity gives \(T(1-vv^*)=0\). The positive element \(1-vv^*\) is a projection, so faithfulness in (CT.11) makes it zero. Thus every isometry is unitary, which is finiteness. Only the trace identity and faithfulness are needed in this direction. \(\square\)

## Uniqueness and the exact normality criterion

Let \(M\) be finite and let \(T\) be the map just constructed. It is constant on unitary orbits: for \(x\geq0\), apply its trace identity to \(ux^{1/2}\), and extend by linearity to all \(x\). Since it is norm continuous, it is constant on \(D(x)\). CT-01 gives a central element \(c\in D(x)\), and therefore \(c=T(c)=T(x)\). In particular,

\[
\begin{gathered}
D(x)\cap Z\\
=\{T(x)\}.
\end{gathered}
\tag{CT.13}
\]

Every finite scalar trace \(\sigma\), without a normality assumption, is bounded and constant on unitary orbits by TB-01. Norm continuity and (CT.13) give

\[
\begin{gathered}
\sigma(x)=\sigma(T(x)),\\
x\in M.
\end{gathered}
\tag{CT.14}
\]

This proves that restriction to \(Z\) is a bijection between finite traces on \(M\) and positive functionals on \(Z\). Its inverse sends \(\psi\) to \(\psi\circ T\): positivity and the trace identity follow from those of \(T\), and its central restriction is \(\psi\).

Suppose now that \(S:M\to Z\) is linear, positive, has the trace identity, is \(Z\)-linear, and satisfies \(S(1)=1\). Neither faithfulness nor normality is assumed. Positivity and unitality give \(\|S(h)\|\leq\|h\|\) for self-adjoint \(h\); decomposition into real and imaginary parts gives \(\|S(x)\|\leq2\|x\|\), which suffices for continuity. The trace identity gives constancy on unitary orbits as above, while central linearity gives \(S(c)=c\) for \(c\in Z\). Taking a norm approximation to \(T(x)\) from \(D(x)\), we obtain \(S(x)=S(T(x))=T(x)\). Thus the map in (CT.11) is unique; it is called the **canonical center-valued trace**. Its faithfulness and ultraweak continuity are automatic even for a proposed competitor with only the first three properties of (CT.11).

For a finite algebra, (CT.14) already proves that \(\sigma\) is normal if and only if \(\sigma|_Z\) is normal. The forward implication restricts increasing nets. For the reverse implication use the composition of the normal maps \(T\) and \(\sigma|_Z\).

**Arbitrary-algebra theorem.** A finite scalar trace \(\sigma\) on any von Neumann algebra \(M\) is normal exactly when its central restriction is normal. In particular every finite trace on a factor is normal.

**Proof with the exact reduction.** [The programme projection lesson, Theorem 7.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html#oa-fnd-ty-10), applied to the unit, supplies central projections \(z_f,z_\infty\) with sum \(1\), such that \(Mz_f\) is finite and \(Mz_\infty\) is properly infinite. [Proposition 13.4 there](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html#oa-fnd-ty-17) supplies \(p\leq z_\infty\) with \(p\sim z_\infty-p\sim z_\infty\). Consequently

\[
\sigma(z_\infty)=2\sigma(z_\infty).
\tag{CT.15}
\]

The value is finite, so it is zero. Cauchy–Schwarz then gives \(\sigma(xz_\infty)=0\) for every \(x\in M\). On the finite summand use (CT.14) to obtain

\[
\begin{gathered}
\sigma(x)\\
=\sigma\bigl(T_f(xz_f)\bigr).
\end{gathered}
\tag{CT.16}
\]

where \(T_f:Mz_f\to Zz_f\) is its canonical trace. If \(z_f=0\) this equation simply says \(\sigma=0\). Otherwise central compression \(M\to Mz_f\), the map \(T_f\), and restriction of a normal central functional to \(Zz_f\) are all normal; their composition is \(\sigma\). Conversely normality restricts to the center. For a factor the center is \(\mathbb C1\), on which every finite positive functional is normal. A finite factor has the unique normalized scalar trace determined by \(T\); an infinite factor has only the zero finite trace. \(\square\)

## Checks on the hypotheses

**Matrices over an abelian algebra.** For an abelian von Neumann algebra \(A\), the center of \(M_n(A)\) consists of scalar matrices: commuting with the diagonal matrix units kills off-diagonal entries, and commuting with all matrix units equates the diagonal entries. Thus

\[
\begin{gathered}
T(x)=a1_n,\\
a=\frac1n\sum_{j=1}^n x_{jj}.
\end{gathered}
\tag{CT.17}
\]

To check the trace identity, expand the diagonal sums of \(x^*x\) and \(xx^*\); they agree because all entries lie in the abelian algebra \(A\). The same expansion proves positivity. If their sum is zero, each positive summand \(x_{ij}^*x_{ij}\) is zero, so every entry vanishes. Central linearity and normalization are immediate; CT-03 and CT-04 identify this as the canonical trace, and also prove finiteness without assuming it in advance.

**Finite algebras can have nonnormal finite traces.** Let \(A=\ell^\infty(\mathbb N)\). The limit functional on the subspace of convergent sequences has norm one and sends \(1\) to \(1\). The complete complex Hahn–Banach theorem in NP1 extends it to a norm-one functional \(L\) on \(A\) with \(L(1)=1\). This extension is positive. Indeed, for self-adjoint \(h\), the norm-convergent exponential series gives \(L(e^{ith})=1+itL(h)+O(t^2)\). The inequality \(|L(e^{ith})|\leq1\) for both signs of small real \(t\) forces \(L(h)\) to be real: the linear term of its squared modulus is \(-2t\operatorname{Im}L(h)\). Then, for \(0\leq a\leq1\), \(|1-L(a)|=|L(1-a)|\leq1\) forces \(L(a)\geq0\). Scaling covers all positives.

The algebra is abelian, so \(L\) is tracial. Finite-coordinate projections \(p_k\uparrow1\) have \(L(p_k)=0\), whereas \(L(1)=1\). Thus \(L\) is not normal. Here \(T=\mathrm{id}\), and its central restriction is precisely the same nonnormal functional. The criterion diagnoses the failure rather than asserting that all finite traces are normal.

**Why the scalar trace must be finite.** On \(B(\ell^2(\mathbb N))\) define a weight \(\rho\) by the usual matrix trace on positive finite-rank operators and by \(\infty\) on all other positive operators. Positive finite-rank operators are closed under addition, and a positive summand of a finite-rank positive operator has support inside its finite-dimensional range. This proves additivity including infinite values. Homogeneity uses \(0\cdot\infty=0\). Polar decomposition identifies the nonzero spectral parts of \(x^*x\) and \(xx^*\), so either both have infinite rank, or both are finite rank with equal matrix trace. Hence \(\rho\) is a trace. On the center it takes value \(\infty\) at every positive scalar multiple of \(1\), so it preserves increasing suprema there. But for

\[
\begin{gathered}
d=\operatorname{diag}(d_j),\\
d_j=2^{-j},\\
 j\geq1.
\end{gathered}
\tag{CT.18}
\]

the finite-coordinate truncations increase to \(d\), their traces tend to \(1\), and \(\rho(d)=\infty\). Thus normality of the central restriction alone does not suffice for an infinite-valued trace. The finite-rank matrix trace and its basis independence are the special case of Matrix amplification without a countable basis with scalar coefficient algebra.

**No hidden sigma-finiteness.** For uncountable \(I\), the algebra \(\ell^\infty(I)\) is finite and its canonical trace is the identity. It has uncountably many orthogonal nonzero coordinate projections, so it has no faithful normal state by Projection countability recovers the observations. The block construction in CT-03 still works, using all coordinate evaluations. A single faithful finite trace on the whole algebra was never part of its conclusion.
