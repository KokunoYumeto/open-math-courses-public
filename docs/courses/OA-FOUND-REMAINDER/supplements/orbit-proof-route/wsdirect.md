<span id="finite-domains-null-directions-and-support-corners"></span>
# Finite domains, null directions, and support corners

<span id="oa-mod-ws-01--conventions-and-exact-inputs"></span>
<span id="OA-MOD-WS-01"></span>
<span id="oa-mod-ws-01"></span>
## OA-MOD-WS-01 — Conventions and exact inputs

Let \(M\subseteq B(H)\) be a concrete unital von Neumann algebra on any Hilbert space. Use the definitions of a weight \(\varphi\), its finite cone \(F_\varphi\), its finite left ideal \(\mathfrak n_\varphi\), its definition algebra \(\mathfrak m_\varphi\), and its null left ideal \(N_\varphi\) from OA-MOD-WG-002 through OA-MOD-WG-005. Inner products are linear in the first variable.

OA-MOD-WS-02 and OA-MOD-WS-03 allow an arbitrary weight. All later weight assertions explicitly assume normality, in the sense of preservation of bounded increasing positive suprema.

The proofs use the finite-domain algebra from WG-003, bounded inverse order, monotone nets, support cutoffs and topology facts from OA-MOD-BK-03 through OA-MOD-BK-06, and the finite-cutoff characterization of semifiniteness from WG-008. These are bounded-operator and Hilbert prerequisites; no modular theorem or spatial derivative is used.

For clarity, the concrete sigma-strong topology is given by the seminorms
\[
x\longmapsto\left(\sum_{n\geq1}\|x\xi_n\|^2\right)^{1/2},
\qquad \sum_n\|\xi_n\|^2<\infty.
\]
A norm-bounded strongly convergent net converges in this topology: make the tail uniformly small by the common norm bound, and use strong convergence for the remaining finitely many vectors. This does not assume that \(H\) has a countable basis. We use the corresponding square-summable vector-pair definition of the ultraweak topology from BK-03.

<span id="oa-mod-ws-02--the-projection-of-the-finite-domain"></span>
<span id="OA-MOD-WS-02"></span>
<span id="oa-mod-ws-02"></span>
## OA-MOD-WS-02 — The projection of the finite domain

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

<span id="oa-mod-ws-03--a-semifinite-restriction-exists-before-normality"></span>
<span id="OA-MOD-WS-03"></span>
<span id="oa-mod-ws-03"></span>
## OA-MOD-WS-03 — A semifinite restriction exists before normality

**Proposition.** With \(e\) as above, the restriction of \(\varphi\) to \((eMe)_+\) is a semifinite weight. If \(\varphi\) is normal, so is this restriction. For \(a\in M_+\),
\[
a\ne eae\quad\Longrightarrow\quad\varphi(a)=+\infty.
\]

**Proof.** Every finite positive element of \(M\) belongs to \(eMe\), by WS-02. Hence the finite cone of the restricted weight is exactly \(F_\varphi\), now viewed inside the corner. Its complex span is ultraweakly dense in \(eMe\), again by WS-02. This is precisely semifiniteness of the restriction. Increasing positive suprema in the corner agree with those in \(M\), so normality is inherited. Finally, if \(\varphi(a)<\infty\), then \(a\in F_\varphi\) and \(a=eae\); taking the contrapositive gives the assertion. \(\square\)

The implication is about all finite elements. It does not say that every positive element of \(eMe\) has finite weight.

<span id="oa-mod-ws-04--normality-produces-a-largest-null-projection"></span>
<span id="OA-MOD-WS-04"></span>
<span id="oa-mod-ws-04"></span>
## OA-MOD-WS-04 — Normality produces a largest null projection

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

<span id="oa-mod-ws-05--removing-null-directions-without-subtracting-infinities"></span>
<span id="OA-MOD-WS-05"></span>
<span id="oa-mod-ws-05"></span>
## OA-MOD-WS-05 — Removing null directions without subtracting infinities

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

<span id="oa-mod-ws-06--the-faithful-semifinite-support-corner"></span>
<span id="OA-MOD-WS-06"></span>
<span id="oa-mod-ws-06"></span>
## OA-MOD-WS-06 — The faithful semifinite support corner

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

We use **support of the normal weight** for \(p=e-f\) when following the stated Takesaki convention. If a discussion instead defines support as the complement of the maximal null projection, its projection is \(r\). The convention must be checked before treating results about arbitrary normal weights as identical. For the normal semifinite numerator in spatial derivative theory, the two conventions agree and WS-06 supplies the required support-corner reduction.

