# Hereditary closure and positive duality

Local closure tests and positive linear functionals solve two different problems. A resolvent turns an arbitrary positive approximating net into a bounded one, allowing a corner test to detect relative ultraweak closure. In an ordered locally convex space, subtracting the positive cone identifies exactly which separating functionals are positive. The resulting polar identities also describe functions that take infinite values.

We use the sigma-finite-support ideal and bounded gluing theorem from NW03 and NW07, the equality of convex closures from CP10, and real locally convex separation from NP2. All other arguments below are given here.

## Regularization without a norm bound

Let \(M\) be a von Neumann algebra. For \(t>0\) and \(a\in M_+\), set

\[
\begin{gathered}
 R_t(a)=(1+ta)^{-1},\\
 q_t(a)=a(1+ta)^{-1}.
\end{gathered}
\tag{HC.1}
\]

The bounded continuous calculus of BK01 gives
\(0\le R_t(a)\le1\), \(0\le q_t(a)\le a\), and
\(\|q_t(a)\|\le t^{-1}\). If \(a\) belongs to a two-sided ideal \(J\), then so does \(q_t(a)\), by its product formula.

**Lemma.** If a net \(a_\alpha\in M_+\) converges sigma-strongly to \(a\in M_+\), then \(q_t(a_\alpha)\to q_t(a)\) sigma-strongly for every fixed \(t>0\). No common norm bound on \(a_\alpha\) is required.

**Proof.** Put \(h_\alpha=a_\alpha-a\), \(b=R_t(a)\), and \(R_\alpha=R_t(a_\alpha)\). Write \(d_\alpha=q_t(a_\alpha)-q_t(a)\). The resolvent identity, obtained by multiplying out the two inverses, gives

\[
 d_\alpha=R_\alpha h_\alpha b.
\tag{HC.2}
\]

For a normal positive functional \(\omega\), write
\(p_\omega(x)^2=\omega(x^*x)\), and set
\(\omega_b(x)=\omega(b^*xb)\). Fixed multiplication is ultraweakly continuous by CP07, so \(\omega_b\) is again a normal positive functional. Since \(R_\alpha\) is a contraction,

\[
\begin{gathered}
 p_\omega(d_\alpha)^2\\
 \le p_{\omega_b}(h_\alpha)^2
 \longrightarrow0.
\end{gathered}
\tag{HC.3}
\]

This proves the assertion for every defining seminorm. Finally,
\(a-q_t(a)=ta^2(1+ta)^{-1}\), so

\[
 \begin{gathered}
 \|a-q_t(a)\|\le t\|a\|^2\\
 \longrightarrow0\quad(t\downarrow0).
 \end{gathered}
\tag{HC.4}
\]

Thus the regularizations are uniformly bounded for each fixed \(t\), and recover each fixed \(a\) in norm as \(t\) tends to zero. \(\square\)

## The full relative corner-closure theorem

Let \(\mathcal P\) be the sigma-finite projections of \(M\), including zero, and put
\(J=\bigcup_{p\in\mathcal P}pMp\). NW03 proves that \(J\) is a two-sided star ideal, that its elements have sigma-finite support projections, and that subprojections and countable joins of sigma-finite projections are sigma-finite.

**Theorem.** Let \(F\subseteq J_+\) be convex and hereditary: \(0\le b\le a\in F\) implies \(b\in F\). Then the following are equivalent:

1. \(F\) is closed in the relative ultraweak topology of \(J\).
2. \(F\cap pMp\) is ultraweakly closed in \(pMp\) for every \(p\in\mathcal P\).

The algebra, the net defining a closure, and the family \(\mathcal P\) have no countability restrictions.

**Proof.** The first condition implies the second because \(pMp\subseteq J\) and the corner topology is the inherited ultraweak topology, as proved in CP11.

Assume the second condition. The empty set is already closed, so suppose \(F\ne\varnothing\). Heredity implies \(0\in F\). Take
\(a\in J\cap\overline F^{\,\mathrm{uw}}\). The positive cone is ultraweakly closed by CP07, so \(a\ge0\). By CP10, the convex set \(F\) has the same ultraweak and sigma-strong closures in \(M_{\mathrm{sa}}\). There is therefore a net \(a_\alpha\in F\) converging sigma-strongly to \(a\). This net need not be norm bounded.

Fix \(t>0\). Heredity and HPC01 give \(q_t(a_\alpha)\in F\), with
\(\|q_t(a_\alpha)\|\le t^{-1}\), and
\(q_t(a_\alpha)\to q_t(a)\) sigma-strongly. Also \(q_t(a)\in J\).
The bounded gluing theorem NW07 now applies to this regularized net and yields \(q_t(a)\in F\).

If \(a=0\), the conclusion is immediate. Otherwise let \(p=s(a)\in\mathcal P\). All \(q_t(a)\) lie in \(pMp\). By (HC.4) they converge in norm, hence ultraweakly, to \(a\). The assumed closedness of \(F\cap pMp\) gives \(a\in F\). Thus

\[
 \overline F^{\,\mathrm{uw}}\cap J=F,
\tag{HC.5}
\]

which is precisely relative ultraweak closedness. \(\square\)

The bounded gluing argument is sufficient after regularization. It does not impose a bounded-net hypothesis on the final theorem or require a faithful normal state on all of \(M\).

## What the positive polar detects

Let \(A\) be a real locally convex space with a generating positive cone \(C\): \(A=C-C\). Write \(x\le y\) when \(y-x\in C\), let \(A'\) be the continuous real linear dual, and set

\[
\begin{gathered}
 \ell\in C'\quad\Longleftrightarrow\\
 \ell\in A',\quad\ell|_C\ge0.
\end{gathered}
\tag{HC.6}
\]

For \(F\subseteq C\) and \(E\subseteq C'\), define their positive polars \(F^\triangle\subseteq C'\) and \(E^\triangle\subseteq C\) by the following membership conditions, for \(\ell\in C'\) and \(x\in C\):

\[
\begin{gathered}
 \ell\in F^\triangle\quad\Longleftrightarrow\\
 \ell|_F\le1,\\
 x\in E^\triangle\quad\Longleftrightarrow\\
 \sup_{\ell\in E}\ell(x)\le1.
\end{gathered}
\tag{HC.7}
\]

For a subset \(D\subseteq A\), its ordinary one-sided polar is
\(D^\circ=\{\ell\in A':\ell(d)\le1\text{ for all }d\in D\}\).
The same notation in the other direction denotes an intersection of half-spaces in \(A\), without a restriction to \(C\).

**Lemma.** If \(F\subseteq C\) is nonempty, convex and hereditary, then

\[
\begin{gathered}
 (F-C)^\circ=F^\triangle,\\
 \overline{F-C}=(F^\triangle)^\circ,\\
 \overline{F-C}\cap C=F^{\triangle\triangle}.
\end{gathered}
\tag{HC.8}
\]

The closure is taken in \(A\). No closedness of \(F\) or of \(C\) is needed for this lemma.

**Proof.** We have \(0\in F\), hence \(-C\subseteq F-C\). A functional bounded above by one on \(-C\) must be nonnegative on \(C\), since all \(-sc\), \(s>0\), belong to \(-C\). Testing also on \(F\) proves one inclusion in the first identity. Conversely, if \(\ell\ge0\) on \(C\) and \(\ell\le1\) on \(F\), then \(\ell(f-c)\le\ell(f)\le1\). This proves the polar identity directly.

Every \(\ell\in F^\triangle\) is at most one on the closure of \(F-C\), so that closure is contained in \((F^\triangle)^\circ\). For the reverse inclusion, suppose \(x\notin\overline{F-C}\). This is a closed convex set containing zero. Real locally convex separation NP2 supplies \(\ell\in A'\) with
\(\ell(x)>c=\sup_{d\in F-C}\ell(d)\), where \(0\le c<\infty\).
The inclusion \(-C\subseteq F-C\) forces \(\ell\ge0\) on \(C\).
If \(c>0\), divide \(\ell\) by \(c\); if \(c=0\), multiply it by a positive number large enough that its value at \(x\) exceeds one. The resulting functional belongs to \(F^\triangle\) and excludes \(x\) from \((F^\triangle)^\circ\). Intersecting with \(C\) proves the last identity. \(\square\)

**A distinction between sets and their polars.** In \(A=\mathbb R^2\), take \(C=[0,\infty)^2\) and \(F=[0,1]\times\{0\}\). The point \((1,-1)\) belongs to \(F-C\), but not to \(\operatorname{conv}(F\cup(-C))\). Indeed, writing a convex combination as \(sf+(1-s)(-c)\), its first coordinate can equal one only when \(s=1\) and \(f_1=1\), which forces its second coordinate to be zero. Thus those two sets need not coincide. Their polars do coincide: both equal \(F^\triangle\), by direct testing on \(F\) and on \(-C\). The proof of (HC.8) uses this valid identity, not an equality of the original sets.

## Gauges with zero and infinite values

Keep \(A,C\) as above. Let \(F\subseteq C\) be nonempty, convex, hereditary and closed in the relative topology of \(C\). It need not absorb \(C\). Define

\[
\begin{gathered}
 g_F(x)=\inf\\
 \{r>0:x\in rF\},
\end{gathered}
\tag{HC.9}
\]

where the infimum of the empty set is \(\infty\).

**Lemma.** The gauge \(g_F:C\to[0,\infty]\) is lower semicontinuous, monotone, subadditive and positively homogeneous, with \(g_F(0)=0\). Moreover, for every \(r>0\) and \(x\in C\),

\[
 \begin{gathered}
 g_F(x)\le r\\
 \Longleftrightarrow\quad x\in rF.
 \end{gathered}
\tag{HC.10}
\]

**Proof.** Since \(0\in F\), admissible dilations are upward closed: if \(x\in sF\) and \(r\ge s>0\), convexity with zero gives \(x\in rF\). Thus, whenever \(g_F(x)<r\), we have \(x\in rF\).

If \(g_F(x)\le r\), then \(x/(r+1/n)\in F\) for every positive integer \(n\). These vectors converge in \(C\) to \(x/r\); relative closedness gives \(x\in rF\). The other inclusion in (HC.10) follows from the definition. These positive sublevel sets are relatively closed. The zero sublevel is their intersection at \(r=1/n\), proving lower semicontinuity also at zero.

Monotonicity follows from heredity of every \(rF\). Positive homogeneity for a scalar \(s>0\) follows by replacing an admissible \(r\) with \(sr\), and \(g_F(0)=0\) follows from \(0\in rF\) for every \(r>0\).
To prove subadditivity, only finite values require an argument. Choose \(r>g_F(x)\) and \(s>g_F(y)\). Then
\((x+y)/(r+s)\) is a convex combination of \(x/r\in F\) and \(y/s\in F\). Hence \(g_F(x+y)\le r+s\). Let \(r,s\) decrease to the two gauge values. If either value is infinite, the subadditive inequality is automatic. \(\square\)

The positive continuous linear minorants of this gauge are exactly \(F^\triangle\). A minorant is at most one on \(F\) by (HC.10). Conversely, if \(\ell\in F^\triangle\) and \(g_F(x)<\infty\), then \(\ell(x)\le r\) for every \(r>g_F(x)\), so \(\ell(x)\le g_F(x)\). At an infinite value the inequality needs no argument.

For later use, let \(g:C\to[0,\infty]\) be monotone, subadditive, positively homogeneous for positive scalars, lower semicontinuous, and satisfy \(g(0)=0\). Its unit sublevel \(F=\{g\le1\}\) contains zero, is relatively closed by lower semicontinuity, and is hereditary by monotonicity. If \(x,y\in F\) and \(0<s<1\), subadditivity and homogeneity give \(g(sx+(1-s)y)\le s g(x)+(1-s)g(y)\le1\); the endpoint cases are immediate. Thus \(F\) is convex. Furthermore \(g_F=g\): for \(g(x)=0\), all positive dilations are admissible; for \(0<g(x)<\infty\), precisely the dilations \(r\ge g(x)\) are admissible; for \(g(x)=\infty\), none are. This proves the equality in every case.

## Three equivalent positive-duality properties

**Theorem.** For a generating ordered real locally convex space \(A=C-C\), the following conditions are equivalent.

1. Every relatively closed hereditary convex \(F\subseteq C\) satisfies \(\overline{F-C}\cap C=F\).
2. Every nonempty relatively closed hereditary convex \(F\subseteq C\) satisfies \(F^{\triangle\triangle}=F\).
3. Every lower semicontinuous monotone subadditive positively homogeneous \(g:C\to[0,\infty]\) with \(g(0)=0\) satisfies, for \(x\in C\),

\[
 g(x)=\sup_{\ell\in\Phi_g}\ell(x).
\tag{HC.11}
\]

Here \(\Phi_g\) consists of the functionals \(\ell\in C'\) satisfying \(\ell|_C\le g\).

These are equivalent properties of the ordered topological space. The theorem does not assert them for every choice of cone and topology. No absorbing-sublevel, normability, metrizability or finite-value hypothesis is imposed.

**Proof.** HPC03 proves the equivalence of conditions 1 and 2 for nonempty sets. For \(F=\varnothing\), condition 1 holds immediately.

Assume condition 2 and let \(g\) satisfy condition 3's hypotheses. By HPC04, \(F=\{g\le1\}\) is nonempty, relatively closed, convex and hereditary, with \(g_F=g\) and \(\Phi_g=F^\triangle\). Put \(h(x)=\sup_{\ell\in\Phi_g}\ell(x)\). The zero functional belongs to \(\Phi_g\), so \(0\le h\le g\).
If \(0<r<g(x)\), then \(x/r\notin F=F^{\triangle\triangle}\). Some \(\ell\in\Phi_g\) therefore satisfies \(\ell(x/r)>1\), whence \(h(x)>r\). Letting \(r\) increase to \(g(x)\), including arbitrarily large \(r\) when \(g(x)=\infty\), proves \(h(x)=g(x)\). When \(g(x)=0\), equality already follows from \(0\le h\le g\).

Conversely, assume condition 3 and take a nonempty \(F\) from condition 2. HPC04 supplies the gauge \(g_F\), whose positive continuous minorants are \(F^\triangle\). Condition 3 and (HC.10) give
\(F=\{g_F\le1\}=F^{\triangle\triangle}\). This proves condition 2 and completes the equivalence. \(\square\)

**The zero conventions matter.** Every positive bipolar contains zero, so the empty set cannot equal its positive bipolar. That is why condition 2 specifies nonempty sets. Also a supremum of linear functionals is zero at zero. If positive homogeneity is imposed only for strictly positive scalars and \(g(0)=0\) is omitted, the function \(g\equiv\infty\) is a counterexample to (HC.11). It is the only extra zero-value case: homogeneity gives \(g(0)=2g(0)\), so \(g(0)\) is zero or infinity; in the latter case monotonicity makes \(g\) identically infinite. Thus the formulation covers the full nontrivial class and identifies both exceptional cases explicitly.

## Applications and solved checks

**Positive sublinear functions on a von Neumann algebra.** Take \(A=M_{\mathrm{sa}}\) with its ultraweak topology and \(C=M_+\). This cone is closed and generating. NW09 proves condition 1 of HPC05. Every ultraweakly lower semicontinuous monotone sublinear positively homogeneous function \(g:M_+\to[0,\infty]\) with \(g(0)=0\) is therefore the pointwise supremum of its normal positive linear minorants. A continuous real functional on \(M_{\mathrm{sa}}\) extends uniquely to a normal complex linear functional on \(M\), by CP10; positivity on \(M_+\) is unchanged. This applies to weights and also to functions which are only subadditive.

**A nonabsorbing unit sublevel.** For the segment \(F=[0,1]\times\{0\}\) in HPC03, compute its gauge and positive polar.

*Solution.* On \(C=[0,\infty)^2\), the gauge equals \(x\) at \((x,0)\), and equals \(\infty\) whenever the second coordinate is positive. Positive linear functionals have the form \(\ell(x,y)=ax+by\), with \(a,b\ge0\). Belonging to \(F^\triangle\) means exactly \(a\le1\), with no upper bound on \(b\). Their supremum gives precisely the stated gauge, including its infinite values and its value zero at the origin.

**A sublinear function which is not a weight.** On the same cone, let \(g(x,y)=\max\{x,y\}\). Find all positive linear minorants.

*Solution.* They are exactly \(\ell(x,y)=ax+by\) with \(a,b\ge0\) and \(a+b\le1\). Necessity follows by testing \((1,1)\); sufficiency follows from \(ax+by\le(a+b)\max\{x,y\}\). The two coordinate functionals attain the required supremum. The function is not additive: its values at \((1,0)\) and \((0,1)\) sum to two, while its value at \((1,1)\) is one.

**Why the regularization parameter stays fixed first.** Explain the order of limits in HPC02.

*Solution.* For each fixed \(t>0\), the entire regularized net has norm at most \(t^{-1}\), which is exactly the hypothesis needed in NW07. That argument proves \(q_t(a)\in F\) for every \(t\). Only then is \(t\) sent to zero inside the one closed corner \(s(a)Ms(a)\). Allowing \(t\) to vary with the original net would remove the common norm bound and would not justify that application of NW07.

The classical statements compared here are Masamichi Takesaki, *Theory of Operator Algebras II* (2003), §VII.1, Lemmas 1.15–1.16, printed pp. 50–54. HPC02 gives the unrestricted relative-closure conclusion. HPC03–05 give the ordered-space equivalence with explicit zero conventions and the corrected polar argument; the counterexample in HPC03 explains the set-equality error in the printed proof.
