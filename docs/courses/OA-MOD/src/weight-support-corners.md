# Finite domains, null directions, and support corners

**Self-checked by the writing AI. Original arguments and one explicitly marked licensed adaptation.**

A general normal weight has two potentially different obstructions: some directions have no finite-weight approximation, while others have weight zero. Separating these obstructions explains why the support convention for an arbitrary normal weight needs two projections. For a semifinite normal weight the first obstruction disappears, and the usual faithful support-corner reduction follows.

Free comparisons are Brent Nelson, [*Tomita–Takesaki Theory*, the support paragraph after Definition 3.19, page 32](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf), and François Combes, [*Poids associé à une algèbre hilbertienne à gauche*, the opening paragraph of printed page 51](https://www.numdam.org/item/CM_1971__23_1_49_0.pdf). Nelson uses \(e-f\); Combes uses \(1-f\). Here both projections are constructed and distinguished, and each asserted corner property is proved. They coincide for a semifinite weight. The separately attributed Daws component below provides an additional compression criterion. Central support results for traces and support results for bounded normal functionals are separate specializations.

## Conventions and exact inputs

Let \(M\subseteq B(H)\) be a concrete unital von Neumann algebra on any Hilbert space. Use the definitions of a weight \(\varphi\), its finite cone \(F_\varphi\), its finite left ideal \(\mathfrak n_\varphi\), its definition algebra \(\mathfrak m_\varphi\), and its null left ideal \(N_\varphi\) from WG002, WG003, WG004 and WG005. Inner products are linear in the first variable.

OA-MOD-WS-02 and the corner-restriction proposition in OA-MOD-WS-03 allow an arbitrary weight. The separately marked compression criterion in WS-03 assumes normality and uses NW-11. All later weight assertions explicitly assume normality, in the sense of preservation of bounded increasing positive suprema.

The written inputs are WG003 for the finite-domain algebra, BK01 for square roots and positive-operator estimates, BK03 for bounded strong and ultraweak convergence, BK04 for monotone nets, BK05 for inverse order, BK06 for support cutoffs, and WG008 for the finite-cutoff characterization of semifiniteness. The compression criterion alone additionally uses NW11. These proofs apply in arbitrary Hilbert dimension; no modular theorem or spatial derivative is used.

For clarity, the concrete sigma-strong topology is given by the seminorms

\[
x\longmapsto\left(\sum_{n\geq1}\|x\xi_n\|^2\right)^{1/2},
\qquad \sum_n\|\xi_n\|^2<\infty.
\]

A norm-bounded strongly convergent net converges in this topology: make the tail uniformly small by the common norm bound, and use strong convergence for the remaining finitely many vectors. This does not assume that \(H\) has a countable basis. We use the corresponding square-summable vector-pair definition of the ultraweak topology from BK-03.

## The projection of the finite domain

**Theorem.** For every weight \(\varphi\), there is a unique projection \(e\in M\) such that

\[
\overline{\mathfrak n_\varphi}^{\,\mathrm{SOT}}
=\overline{\mathfrak n_\varphi}^{\,\sigma\text{-strong}}
=\overline{\mathfrak n_\varphi}^{\,\mathrm{ultraweak}}
=M e.
\]

Moreover,

\[
\overline{\mathfrak m_\varphi}^{\,\mathrm{SOT}}
=\overline{\mathfrak m_\varphi}^{\,\sigma\text{-strong}}
=\overline{\mathfrak m_\varphi}^{\,\mathrm{ultraweak}}
=eMe.
\]

The closures are taken inside \(M\). Every \(a\in F_\varphi\) satisfies \(a=eae\). In particular, \(\varphi\) is semifinite if and only if \(e=1\).

**Proof.** Direct \(F_\varphi\) by its positive order; addition gives a common upper bound. For each \(a\in F_\varphi\), put

\[
u_a=a(1+a)^{-1}.
\]

As in WG-008, these are increasing finite positive contractions. Let \(e\in M\) be their strong supremum. At this stage \(e\) is only known to be a positive contraction.

Fix \(a\in F_\varphi\). All \(t a\), \(t>0\), are indices, and the bounded support-cutoff theorem gives

\[
u_{ta}\uparrow s(a).
\]

Thus \(e\geq s(a)\). A positive contraction dominating a projection acts as the identity on its range: if \(q\leq e\leq1\), then

\[
q(1-e)q=0,\qquad (1-e)^{1/2}q=0,
\]

so \(eq=q\).

Let \(K\) be the closed linear span of the ranges of all \(a\in F_\varphi\). The preceding observation shows that \(e\) is the identity on \(K\). Every \(u_a\) vanishes on \(K^\perp\), and therefore its strong limit \(e\) does as well. Hence \(e=P_K\) is a projection. It follows that \(a=eae\) for every finite positive \(a\).

If \(x\in\mathfrak n_\varphi\), then \(x^*x\in F_\varphi\), and

\[
\|x(1-e)\xi\|^2
=\langle x^*x(1-e)\xi,(1-e)\xi\rangle=0.
\]

Thus \(x=xe\). Conversely, if \(x=xe\), then \(u_a\in\mathfrak n_\varphi\), since \(u_a^2\leq u_a\) and its weight is finite. The left-ideal property gives \(x u_a\in\mathfrak n_\varphi\). These operators are norm bounded and converge strongly to \(xe=x\), hence sigma-strongly and ultraweakly as well.

The set \(Me=\{x\in M:x=xe\}\) is closed in each stated topology: fixed right multiplication is continuous in each, and the defining equality is closed. This proves the three left-ideal closure identities. Uniqueness also follows: \(Me=Me'\) for projections implies \(e=ee'\) and \(e'=e'e\), and taking adjoints yields both projection inequalities.

Since \(\mathfrak m_\varphi=\operatorname{span}_{\mathbb C}F_\varphi\), it lies in \(eMe\). For \(x\in eMe\),

\[
u_a x u_a=u_a^*(x u_a)\in\mathfrak m_\varphi.
\]

Both factors in the last product belong to \(\mathfrak n_\varphi\). The operators \(u_a x u_a\) are norm bounded and converge strongly to \(exe=x\). The same topology arguments prove all three definition-algebra closure identities. Semifiniteness, defined by ultraweak density of \(\mathfrak m_\varphi\), is consequently equivalent to \(eMe=M\), or \(e=1\). \(\square\)

The projection \(e\) need not be central. The proof does not turn the finite left ideal into a two-sided ideal.

## A semifinite restriction exists before normality

**Proposition.** With \(e\) as above, the restriction of \(\varphi\) to \((eMe)_+\) is a semifinite weight. If \(\varphi\) is normal, so is this restriction. For \(a\in M_+\),

\[
a\ne eae\quad\Longrightarrow\quad\varphi(a)=+\infty.
\]

**Proof.** Every finite positive element of \(M\) belongs to \(eMe\), by WS-02. Hence the finite cone of the restricted weight is exactly \(F_\varphi\), now viewed inside the corner. Its complex span is ultraweakly dense in \(eMe\), again by WS-02. This is precisely semifiniteness of the restriction. Increasing positive suprema in the corner agree with those in \(M\), so normality is inherited. Finally, if \(\varphi(a)<\infty\), then \(a\in F_\varphi\) and \(a=eae\); taking the contrapositive gives the assertion. \(\square\)

The implication is about all finite elements. It does not say that every positive element of \(eMe\) has finite weight.

### Compression detects semifiniteness: an adapted proof by Matt Daws

**Separate component: CC BY-NC-SA 4.0.** The following criterion and proof are adapted from **Matt Daws, *Some notes on weights*, September 2024, Section 2.1, proposition labelled `prop:semifinitequiv`**, in [the exact source version a2d54776](https://github.com/MatthewDaws/Mathematics/blob/a2d54776c75fc99f12d8e317e3e3c3fd34c813f9/Weights/weights.tex). The [repository licence notice](https://github.com/MatthewDaws/Mathematics/blob/a2d54776c75fc99f12d8e317e3e3c3fd34c813f9/README.md) grants [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), which also covers this adaptation and its added teaching bridges. GPT-6.1 Sol (OpenAI), Ultra effort, October 2026, converted the notation, specified positive contractive norm approximate units, supplied their existence and corner-limit arguments from WS-02, and made the finite-value and subnet steps explicit. No endorsement by the source author is implied. This marked component is excluded from the surrounding original-prose licence.

The arbitrary-weight cutoff theorem WG-008 remains in force. The criterion below additionally assumes **normality**, using its ultraweak lower semicontinuity from The full characterization. It tests compressions; it does not assert that they increase or lie below the element being tested.

Put \(A_\varphi=\overline{\mathfrak m_\varphi}^{\|\cdot\|}\subseteq eMe\), with the finite-domain projection \(e\) of WS-02. A **positive contractive approximate unit** here means a net \(a_i\in F_\varphi\), \(0\leq a_i\leq1\), such that \(a_i z\to z\) and \(z a_i\to z\) in norm for every \(z\in A_\varphi\). In the zero algebra the constant zero net qualifies. This definition concerns norm approximation in the finite-domain algebra, rather than monotone convergence to \(1\) in \(M\).

Such nets exist without normality. Use the net \(u_a=a(1+a)^{-1}\) from WS-02. For \(b\in F_\varphi\), whenever \(a\geq tb\), inverse order and \((1-u_a)^2\leq1-u_a\) give

\[
\|(1-u_a)b\|^2
\leq\|b(1-u_a)b\|
\leq\|b(1+tb)^{-1}b\|
\leq\frac{\|b\|}{t}.
\]

Taking adjoints gives the right-sided estimate. Since \(\mathfrak m_\varphi=\operatorname{span}_{\mathbb C}F_\varphi\) and the contractions are uniformly bounded, these estimates extend by norm density to \(A_\varphi\).

Every approximate unit in the stated sense converges strongly to \(e\), hence sigma-strongly and ultraweakly. Indeed, \(a_i=ea_i e\), and \(a_i b\to b\) in norm for every \(b\in F_\varphi\). WS-02 identifies \(eH\) as the closed span of their ranges. Uniform boundedness gives convergence to the identity on \(eH\); the operators vanish on \((1-e)H\).

**Proposition.** For a normal weight \(\varphi\), the following conditions are equivalent:

1. \(\varphi\) is semifinite, so \(e=1\).
2. For every such approximate unit and every \(x\in M_+\),

\[
\varphi(x)\leq\liminf_i\varphi(a_i x a_i).
\]

3. For every such approximate unit and every \(x\in M_+\) with \(\varphi(x)=+\infty\), the net \(\varphi(a_i x a_i)\) tends to \(+\infty\).
4. For every such approximate unit and every \(x\in M_+\) with \(\varphi(x)=+\infty\), one has \(\sup_i\varphi(a_i x a_i)=+\infty\).

Each compression has finite weight: \(a_i x a_i\leq\|x\|a_i^2\leq\|x\|a_i\). Thus condition 3 asserts eventual escape above every finite bound; it does not involve subtracting infinities.

**Proof.** If condition 1 holds, the corner-limit argument gives \(a_i\to1\) strongly. The uniformly bounded positive compressions converge strongly, hence ultraweakly, to \(x\). Lower semicontinuity proves condition 2.

Conversely, under condition 2 take \(x=1-e\). Every compression is zero, so \(\varphi(1-e)=0\). Therefore \(1-e\in F_\varphi\subseteq eMe\), which forces \(1-e=0\). This proves condition 1.

Condition 2 implies condition 3, since a nonnegative extended-valued net whose liminf is infinite tends to infinity. For the converse, elements of infinite weight are covered by condition 3. If \(\varphi(x)<\infty\), then \(x\in F_\varphi\subseteq A_\varphi\), and the norm approximate-unit property gives \(a_i x a_i\to x\) in norm. Lower semicontinuity again gives the inequality in condition 2. This finite-value argument applies before semifiniteness is known.

Condition 3 immediately implies condition 4. Suppose condition 4 holds but condition 3 fails for an approximate unit and an element of infinite weight. Some finite \(K\geq0\) then has a cofinal index set

\[
J=\{i:\varphi(a_i x a_i)\leq K\}.
\]

With its inherited order, a cofinal subset of a directed set is directed: find a common upper bound in the original set and then an element of \(J\) above it. The inclusion is cofinal and order preserving, so \((a_j)_{j\in J}\) is a subnet and remains a positive contractive norm approximate unit. Its compressed weights have supremum at most \(K\), contradicting condition 4 for this approximate unit. All four conditions are equivalent. \(\square\)

Normality cannot be dropped from this criterion. For the semifinite nonnormal weight \(\theta\) in WS-08, Problem 4, the finite-domain algebra is \(c_0(\mathbb N)\). Its finite-support coordinate projections \(q_n\) form a norm approximate unit, but \(\theta(q_n1q_n)=0\) while \(\theta(1)=+\infty\). This does not contradict WG-008, which characterizes semifiniteness without normality by strong cutoffs.

**End of the separately licensed Daws adaptation.** The original support-corner lesson resumes below.

## Normality produces a largest null projection

Assume from now on that \(\varphi\) is normal.

**Theorem.** There is a largest projection \(f\in M\) with \(\varphi(f)=0\). It satisfies \(f\leq e\), and

\[
N_\varphi=M f.
\]

For \(a\in M_+\), the following are equivalent:

\[
\varphi(a)=0,\qquad s(a)\leq f,\qquad a=faf.
\]

**Proof.** If \(a\geq0\) and \(\varphi(a)=0\), its cutoff

\[
v_t=t a(1+t a)^{-1}
\]

satisfies \(0\leq v_t\leq t a\), and hence \(\varphi(v_t)=0\). The cutoffs increase to \(s(a)\). Normality yields \(\varphi(s(a))=0\).

If projections \(q_1,q_2\) have weight zero, then \(q_1+q_2\) has weight zero, so \(s(q_1+q_2)\) does also. This support is their join: its kernel is \(\ker q_1\cap\ker q_2\), as follows from

\[
\langle(q_1+q_2)\xi,\xi\rangle
=\|q_1\xi\|^2+\|q_2\xi\|^2.
\]

Therefore finite joins of null projections are null. Their increasing net has a strong supremum \(f\in M\). A bounded strong limit of increasing projections is a projection: it fixes the range of every net member and vanishes on the orthogonal complement of the closed union of their ranges. Normality gives \(\varphi(f)=0\). By construction every null projection lies below \(f\), so it is the largest one.

If \(\varphi(a)=0\), the first paragraph gives \(s(a)\leq f\), or equivalently \(a=faf\). Conversely, \(a=faf\geq0\) implies \(a\leq\|a\|f\), hence \(\varphi(a)=0\). This proves the positive-cone assertions. Since \(f\) itself is finite, WS-02 gives \(f=efe\), so \(f\leq e\).

If \(x\in N_\varphi\), apply the positive-cone assertion to \(x^*x\). It gives \(x(1-f)=0\), or \(x=xf\). Conversely, \(x=xf\) implies \(x^*x\leq\|x\|^2f\), so \(x\in N_\varphi\). Hence \(N_\varphi=Mf\). \(\square\)

The resulting null ideal is ultraweakly and strongly closed. Normality is essential to this conclusion; WS-08 contains a nonnormal counterexample.

## Removing null directions without subtracting infinities

Put \(r=1-f\).

**Theorem.** For every \(a\in M_+\),

\[
\varphi(a)=\varphi(rar).
\]

The restriction of \(\varphi\) to \(rMr\) is faithful and normal. It is not automatically semifinite.

**Proof.** We first record an inequality that remains valid for infinite energies. For arbitrary \(x,y\in M\) and \(\varepsilon>0\),

\[
(x+y)^*(x+y)
\leq(1+\varepsilon)x^*x+(1+\varepsilon^{-1})y^*y.
\]

It follows by expanding the positivity of
\((\varepsilon^{1/2}x-\varepsilon^{-1/2}y)^*
(\varepsilon^{1/2}x-\varepsilon^{-1/2}y)\).
If \(y\in N_\varphi\), monotonicity and additivity imply

\[
\varphi((x+y)^*(x+y))
\leq(1+\varepsilon)\varphi(x^*x).
\]

Applying the same inequality to \(x=(x+y)-y\) gives the reverse comparison with the same factor. If either weight is infinite, the comparisons force both to be infinite. If they are finite, letting \(\varepsilon\) decrease to zero proves equality. No difference of infinite numbers is taken.

For a positive \(a\), choose \(x=a^{1/2}r\) and \(y=a^{1/2}f\). Since \(y\in Mf=N_\varphi\), the preceding equality gives

\[
\varphi(a)=\varphi((x+y)^*(x+y))
=\varphi(x^*x)=\varphi(rar).
\]

If \(a\in(rMr)_+\) has weight zero, WS-04 gives \(a=faf\). Because also \(a=rar\) and \(fr=0\), we obtain \(a=0\). This is faithfulness. Normality is inherited under restriction. No semifiniteness conclusion follows solely from removing the null ideal; the everywhere-infinite example in WS-08 has \(r=1\) and is not semifinite. \(\square\)

We call \(r\) the **null-carrier projection** to keep it distinct from the support convention in the next statement.

## The faithful semifinite support corner

**Theorem.** Let \(\varphi\) be a normal weight, let \(e,f\) be the projections constructed above, and put

\[
p=e-f.
\]

Then \(p\) is a projection, and the restriction \(\varphi_p\) to \(pMp\) is normal, semifinite and faithful. On all of \(M_+\), the exact reconstruction rule is

\[
\varphi(a)=
\begin{cases}
\varphi_p(pap),&a=eae,\\
+\infty,&a\ne eae.
\end{cases}
\]

For a normal semifinite weight, \(e=1\), so \(p=1-f\) and

\[
\varphi(a)=\varphi_p(pap)\qquad(a\in M_+).
\]

**Proof.** We know \(f\leq e\), hence \(p=e-f=e(1-f)=(1-f)e\) is a projection. It lies under \(r=1-f\), so the restriction is faithful by WS-05 and normal by restriction.

Use the increasing finite positive contractions \(u_a\) from WS-02. The compressions \(p u_a p\) increase strongly to \(p\), are positive contractions in the corner, and have finite weight. Indeed, \(u_a=e u_a e\), so

\[
p u_a p=r u_a r,\qquad
\varphi(pu_ap)=\varphi(u_a)<\infty
\]

by WS-05. WG-008 applied inside \(pMp\), whose identity is \(p\), proves semifiniteness. This argument also covers the zero corner.

For \(a=eae\), one has \(rar=pap\), so WS-05 gives the finite-corner formula, whether its value is finite or infinite. For \(a\ne eae\), WS-03 gives the other line. Finally, semifiniteness is equivalent to \(e=1\), by WS-02. \(\square\)

We use **support of the normal weight** for \(p=e-f\), the finite-domain convention stated above. If a discussion instead defines support as the complement of the maximal null projection, its projection is \(r\). The convention must be checked before treating results about arbitrary normal weights as identical. For the normal semifinite numerator in spatial derivative theory, the two conventions agree and WS-06 supplies the required support-corner reduction.

## Order information from domination

**Proposition.** Let \(\varphi,\psi\) be normal weights and suppose

\[
\psi(a)\leq c\varphi(a)\qquad(a\in M_+)
\]

for some finite \(c>0\). Denote their finite-domain projections by \(e_\varphi,e_\psi\), their null projections by \(f_\varphi,f_\psi\), and their null carriers by \(r_\varphi,r_\psi\). Then

\[
e_\varphi\leq e_\psi,\qquad
f_\varphi\leq f_\psi,\qquad
r_\psi\leq r_\varphi.
\]

If both weights are semifinite, their support projections satisfy \(p_\psi\leq p_\varphi\).

**Proof.** Finiteness of \(\varphi(a)\) implies finiteness of \(\psi(a)\), so \(F_\varphi\subseteq F_\psi\). The description of the ranges of the finite-domain projections in WS-02 gives \(e_\varphi\leq e_\psi\). A \(\varphi\)-null projection is \(\psi\)-null by domination, so maximality gives \(f_\varphi\leq f_\psi\). Taking complements gives the null-carrier inequality. When both weights are semifinite, \(p_\varphi=r_\varphi\) and \(p_\psi=r_\psi\), proving the final statement. \(\square\)

For arbitrary normal weights, the last support conclusion cannot be inferred from domination alone: their finite-domain projections can differ. For example, any nonzero bounded normal positive functional is dominated by the everywhere-infinite weight, but the latter has effective support zero under the \(e-f\) convention.

## Problems with complete solutions

**Problem 1: a faithful weight with effective support zero.** On a nonzero von Neumann algebra define \(\varphi_\infty(0)=0\) and \(\varphi_\infty(a)=+\infty\) for every nonzero \(a\in M_+\). Determine all three projections \(e,f,p\) and the null carrier \(r\).

**Solution.** A sum of positive elements is zero exactly when both are zero. This proves additivity, and positive homogeneity is immediate with \(0\cdot\infty=0\). The weight is normal: if an increasing positive net has nonzero supremum, at least one member is nonzero, so the supremum of its weights is infinite. Its only finite positive element is zero, giving \(e=0\). Its only null positive element is zero, giving \(f=0\). Thus \(p=e-f=0\) while \(r=1-f=1\). The weight is faithful and normal but not semifinite. There is no contradiction: effective support and null carrier record different domain information.

**Problem 2: a noncentral support and a faithful GNS representation.** Let \(M=M_3(\mathbb C)\) and \(\varphi(a)=a_{22}\) for \(a\geq0\). Compute \(e,f,p\), and determine whether the semicyclic representation is faithful.

**Solution.** This is a bounded normal positive functional. Every positive element is finite, so \(e=1\). Its null ideal consists of matrices whose second column is zero, since

\[
\varphi(x^*x)=\sum_{j=1}^3|x_{j2}|^2.
\]

Consequently \(f=1-E_{22}\) and \(p=E_{22}\), a noncentral projection. The GNS quotient is isometric to \(\mathbb C^3\) via the second-column map, which is surjective. Left multiplication by \(a\) becomes the usual action \(v\mapsto av\), so the representation is faithful. Thus the support projection of a weight is not the complement of the kernel of its GNS representation; the latter kernel is a two-sided ideal, while the null ideal here is only a left ideal.

**Problem 3: a noncentral finite-domain projection.** In \(M_3(\mathbb C)\), fix \(e_0=E_{11}+E_{22}\) and define

\[
\varphi(a)=
\begin{cases}
\operatorname{Tr}(a),&a=e_0ae_0,\\
+\infty,&a\ne e_0ae_0
\end{cases}
\qquad(a\geq0).
\]

Show that this is a faithful normal weight and compute its projections.

**Solution.** For positive \(a,b\), the sum is supported in \(e_0\) if and only if both are. To prove the nontrivial direction, compress \(a+b\) by \(1-e_0\): positivity forces each compressed diagonal to vanish, and the square-root identity then makes \(a(1-e_0)=b(1-e_0)=0\). Additivity follows using finite trace inside the corner and infinite values elsewhere. Homogeneity follows by rescaling.

For normality, if the supremum of an increasing positive net belongs to the corner, every member does, and finite-dimensional trace preserves the supremum. Here is the needed trace argument: write \(a_i\uparrow a\). By BK04 the net converges strongly, so for each standard basis vector \(v_j\), the numbers \(\langle a_i v_j,v_j\rangle\) increase to \(\langle a v_j,v_j\rangle\). A finite sum commutes with this supremum: for any positive error choose an index for each of the three summands, then a common upper bound for those indices. Therefore

\[
 \sup_i\operatorname{Tr}(a_i)
 =\sum_{j=1}^{3}\langle a v_j,v_j\rangle
 =\operatorname{Tr}(a).
\] If the supremum is outside the corner, some member is outside it, since the corner is strongly closed. In that case both sides of the normality identity are infinite. The only positive zero of the weight is zero, so it is faithful. Its finite cone is \((e_0Me_0)_+\); hence \(e=e_0\), \(f=0\), \(p=e_0\), and \(r=1\). In particular, \(e\) need not be central even in a factor. The weight is not semifinite on \(M\), although its restriction to \(e_0Me_0\) is a faithful finite trace.

**Problem 4: why normality was used.** On \(\ell^\infty(\mathbb N)\), set \(\theta(a)=0\) for \(a\in c_0(\mathbb N)_+\) and \(\theta(a)=+\infty\) for other positive \(a\). Prove that it is a semifinite nonnormal weight without a largest null projection.

**Solution.** The positive cone of \(c_0\) is additive, closed under nonnegative scaling, and hereditary in \(\ell^\infty_+\). The auxiliary-cone construction in WG-003 therefore gives a weight. The finite-support coordinate projections \(q_n\), equal to one in the first \(n\) coordinates, have finite weight and increase to \(1\). WG-008 makes the weight semifinite. But \(\theta(q_n)=0\) while \(\theta(1)=+\infty\), so it is not normal.

Every coordinate projection is null. A projection dominating them all must be \(1\), which is not null. Thus no largest null projection exists. Equivalently, its null ideal is \(c_0\), which is not ultraweakly closed. Indeed, for a bounded sequence \(x=(x_k)\), the condition \(x^*x\in c_0\) says \(|x_k|^2\to0\), which is equivalent to \(x_k\to0\). The null projections \(q_n\) converge strongly and ultraweakly to \(1\), outside this ideal. This shows precisely why the null-projection construction in WS-04 required normality.

## The spatial support contract now supplied

For a normal semifinite weight \(\varphi\), this unit proves the existence of its support \(p\), the identity \(\varphi(a)=\varphi(pap)\) on all positive elements, and the normal semifinite faithful restriction to \(pMp\). These are the assertions required by SD-DEP-SUPPORT. They use no countable-decomposability hypothesis and do not require the original representation to contain a cyclic vector.

The result concerns this particular support corner. Semifiniteness of the restriction to every projection corner is a different assertion and is false in general, as the infinite-weight rank-one corner in WG013 shows. Nor does this support reduction establish any spatial form's density, closability, core property, or modular covariance.

