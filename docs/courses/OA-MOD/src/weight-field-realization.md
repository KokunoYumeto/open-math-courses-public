# The realization boundary in measurable weight fields

**Self-checked by the writing AI.**

The general field comparison in Takesaki II, VIII.4.5 relates the measurable weight definition of VIII.4.4 to the full associated left Hilbert-algebra fields of VI.3.1. There are two realizations involved: the prescribed concrete operator field and the GNS Hilbert field. A fibrewise normal isomorphism does not itself identify their measurable sections. This unit proves that the distinction is substantive, gives the exact compatible reverse implication, and records the remaining obligations. It neither declares the intended source lemma false nor replaces the full course objective by a weaker theorem.

The mathematical antecedents are M. Takesaki, *Theory of Operator Algebras II*, VI.3.1, printed 28/PDF 48, and VIII.4.4–4.5, printed 134–135/PDF 154–155. Those pages have been consulted. The formulas, constructions and proofs below are original. The existing single-fibre weight/GNS and full Hilbert-algebra results WH-09–11 and WG-004,006,007,009,010 retain their current review states. The compatible reverse implication uses DI-04 at its existing measurable-field provider boundary. This unit itself supplies neither the forward construction nor transitive closure. The compatible construction and both operator transports are proved in Exact data, conclusion and prerequisite boundary through The reverse comparison and the realization obstruction; independent review remains separate.

## Two different fields that must not be identified without a map

Let \((Y,\mu)\) be a standard sigma-finite base, with completed measurability when null sets are changed. Let \(M_y\subset B(K_y)\) be the prescribed measurable field of von Neumann algebras. For faithful normal semifinite weights \(\varphi_y\), write

\[
 H_y=H_{\varphi_y},\qquad
 \mathfrak a_y=\mathfrak n_{\varphi_y}\cap\mathfrak n_{\varphi_y}^{*},\qquad
 \mathcal A_y=\Lambda_y(\mathfrak a_y),\qquad
 \pi_y:M_y\longrightarrow B(H_y).
 \tag{MC.1}
\]

The Hilbert inner product is linear in its first argument. Single-fibre results give a faithful normal isomorphism onto \(\pi_y(M_y)\), a full left Hilbert algebra \(\mathcal A_y\), and

\[
 L_{\Lambda_y(x)}=\pi_y(x),\quad
 \Lambda_y(x)^\sharp=\Lambda_y(x^*),\quad
 \|\Lambda_y(x)\|^2+\|\Lambda_y(x^*)\|^2
       =\varphi_y(x^*x+xx^*).
 \tag{MC.2}
\]

Each equation has a fixed fibre as its domain. It does not yet say that \(y\mapsto\pi_y\) transports measurable fields.

An **abstract measurable Hilbert-algebra realization** means a measurable Hilbert field structure on the \(H_y\) with countable algebra sections satisfying the four VI.3.1 conditions: Hilbert fundamentalness, measurable sharp images, pointwise sharp-graph density, and measurable pairwise products. The phrase alone contains no condition on the concrete operator fields in \(B(K_y)\).

A **compatible represented realization** additionally has the following typed inverse transport property. Whenever \(b_y\in\pi_y(M_y)\subset B(H_y)\) is a measurable bounded operator field, the field \(\pi_y^{-1}(b_y)\in M_y\subset B(K_y)\) is measurable in the prescribed realization. The fields are bounded on each fibre; their norms need not have a common essential bound. For uses of arbitrary concrete operators in the GNS realization, the forward transport property is separate: measurable \(a_y\in M_y\) must give measurable \(\pi_y(a_y)\). The maps are typed between two Hilbert fields; an unqualified statement that each \(\pi_y\) is an isomorphism supplies neither property.

The next construction shows that even an isometric star-isomorphism of the full algebras on every fibre can fail to provide that compatibility.

## A full finite-dimensional field with a nonmeasurable concrete frame

Take \(Y=[0,1]\) with Lebesgue measure and choose a set \(A\subset Y\) that is not measurable in the completion. Existence of such a set uses the usual choice-based nonmeasurable-set construction. The example uses its indicator symbolically; it does not pretend that a finite plot or random sample constructs \(A\).

The prescribed concrete field is constant:

\[
 K_y=\mathbb C^2,\qquad M_y=M_2(\mathbb C),\qquad
 P=E_{11},\qquad
 U=\begin{pmatrix}0&1\\
1&0\end{pmatrix},\qquad
 \rho_0=\begin{pmatrix}1&0\\
0&2\end{pmatrix}.
 \tag{MC.3}
\]

Thus concrete operator measurability is entrywise measurability in the fixed matrix frame. Define, pointwise without assuming measurability,

\[
 U_y=\begin{cases}I,&y\notin A,\\
U,&y\in A,\end{cases}
 \qquad \rho_y=U_y\rho_0U_y^*,\qquad
 \varphi_y(a)=\operatorname{Tr}(\rho_y a)\quad(a\geq0).
 \tag{MC.4}
\]

Every \(\varphi_y\) is a faithful finite normal weight; \(\varphi_y(I)=3\). Faithfulness follows from \(I\leq\rho_y\leq2I\): for positive \(a\), zero trace against \(\rho_y\) implies \(\operatorname{Tr}(a)=0\), hence \(a=0\). Finiteness implies semifiniteness here. Matrix trace continuity, or a finite sum of vector functionals, proves normality for bounded increasing nets. All finite domains equal \(M_2\), and the associated full left Hilbert algebra is that whole vector space with ordinary multiplication, adjoint, and the GNS inner product.

Identify \(\Lambda_y(x)\) with the matrix \(x\) as a vector, and put

\[
 T_y(x)=U_yxU_y^*.
 \tag{MC.5}
\]

Then \(T_y\) preserves multiplication and adjoint. Cyclicity of finite-dimensional trace gives, for every \(x\),

\[
 \|T_yx\|_{H_y}^2
 =\operatorname{Tr}\bigl(\rho_y(T_yx)^*T_yx\bigr)
 =\operatorname{Tr}(\rho_0x^*x)
 =\|x\|_{H_0}^2.
 \tag{MC.6}
\]

It preserves the sharp graph norm as well, by applying the same equation to \(x^*\). It is consequently an isometric star-isomorphism of the complete, full Hilbert algebras, not merely a Hilbert-space isomorphism.

Give the field \(H_y\) the Hilbert measurable structure transported by these \(T_y\): a section \(\xi_y\) is measurable exactly when \(T_y^{-1}\xi_y\) has measurable coordinates in the fixed finite-dimensional \(H_0\). This definition is legitimate even though \(T_y\), as a map between the prescribed concrete matrix frames, is not measurable. The two structures have different prescribed fundamental sections.

For an orthonormal fundamental system, set \(r_1=1,r_2=2\) and

\[
 h_{ij}(y)=T_y(E_{ij})/\sqrt{r_j},\qquad i,j\in\{1,2\}.
 \tag{MC.7}
\]

Indeed \(\langle E_{ij},E_{kl}\rangle_{H_0}=\delta_{ik}\delta_{jl}r_j\). Adjoin all finite \(\mathbb Q(i)\)-linear combinations of \(T_y(E_{ij})\), and enumerate them as \(a_m(y)\). Under \(T_y^{-1}\), their coordinates are constant. Their sharp images and pairwise products have constant coordinates as well, since \(T_y\) is a star-algebra map. The set is dense in the entire finite-dimensional algebra for the sharp graph norm. All four VI.3.1 conditions therefore hold, including the printed set-density convention, with no missing infinite-dimensional domain or selection step.

This is a measurable field of full associated Hilbert algebras. Its chosen realization is abstractly trivial. The concrete weights in (MC.4) are nevertheless not a measurable weight field in the prescribed constant \(M_2\) realization, as proved next.

## The original weight definition detects the obstruction

We prove nonmeasurability directly from VIII.4.4, without invoking the field comparison or the later weight-evaluation theorem. Let \(\|\cdot\|_2\) denote the matrix Hilbert–Schmidt norm. Since \(I\leq\rho_y\leq2I\), for every \(x\in M_2\),

\[
 2\|x\|_2^2
 \leq\varphi_y(x^*x+xx^*)
 \leq4\|x\|_2^2.
 \tag{MC.8}
\]

Suppose the weights satisfied VIII.4.4 with countably many measurable concrete matrix fields \(x_j(y)\). Their set is pointwise dense in the weight sharp graph norm, so (MC.8) makes it pointwise dense in Hilbert–Schmidt norm. The definition also says that each finite scalar function
\(g_j(y)=\varphi_y(x_j(y)^*x_j(y))\) is measurable.

For each integer \(n\geq1\), select the least index

\[
 j_n(y)=\min\{j:\|x_j(y)-P\|_2<1/n\},\qquad
 b_n(y)=x_{j_n(y)}(y).
 \tag{MC.9}
\]

The set of eligible indices is nonempty at every fibre. For each \(j\), the event \(\{j_n=j\}\) is the measurable event for that inequality minus the finite union of earlier such events. Thus this is an elementary measurable selector over the countable indices; no uncountable selection theorem is used. Each entry of \(b_n\), and each function \(g_{j_n}\), is measurable by countable measurable pasting.

For any matrix \(b\), write
\(b^*b-P=(b-P)^*b+P(b-P)\). The Hilbert–Schmidt product estimate gives
\(\|b^*b-P\|_1\leq\|b-P\|_2(\|b\|_2+\|P\|_2)\), where \(\|\cdot\|_1\) is trace norm. For completeness, \(\|CD\|_1\leq\|C\|_2\|D\|_2\) follows by taking a polar factor in the trace pairing and applying Hilbert–Schmidt Cauchy–Schwarz; the factor is a contraction, so it does not enlarge the second Hilbert–Schmidt norm. Also \(|\operatorname{Tr}(\rho_yX)|\leq\|\rho_y\|\|X\|_1\), by the same trace-norm dual bound. Consequently, using \(\|P\|_2=1\) and \(\|b_n\|_2<1+1/n\),

\[
 \left|\varphi_y(b_n^*b_n)-\varphi_y(P)\right|
 \leq2\|b_n-P\|_2(\|b_n\|_2+1)
 <\frac4n+\frac2{n^2}.
 \tag{MC.10}
\]

The bound is uniform in \(y\). Hence the measurable functions \(g_{j_n(y)}(y)\) converge pointwise to \(\varphi_y(P)\). But (MC.3)–(MC.4) give

\[
 \varphi_y(P)=1+\mathbf1_A(y).
 \tag{MC.11}
\]

That function is not measurable in the completion. This is a contradiction. Therefore there is no family satisfying VIII.4.4 in the prescribed concrete matrix realization.

If the definition is interpreted on one common conull set instead of every point, the conclusion is unchanged. Such a family would make \(\mathbf1_A\) equal to a measurable function off a measurable null set. Subsets of null sets are measurable in the completion, so \(A\) itself would then be measurable. The contradiction survives null-set modifications. Both Gram-order conditions in the source are respected: the argument already contradicts the first diagonal order, so weakening the proof to that order does not weaken the counterexample to the full definition.

Thus the reverse implication from **arbitrarily realized abstract** measurable full Hilbert algebras to measurable weights on a **prescribed concrete** field is false. This is an obstruction to an untyped formalization. It is not a claim that the source's intended comparison, with its associated compatible realization, has been refuted.

## The exact operator transport that fails

The example also isolates the failure as a single operator field. In the transported Hilbert field, the bounded left multiplication field

\[
 b_y=L_{T_y(P)}=\pi_y(T_y(P))
 \tag{MC.12}
\]

is measurable. Under \(T_y:H_0\to H_y\) it is the constant operator \(L_P\), since
\(L_{T_y(P)}T_y=T_yL_P\). It is a projection of norm one. Nevertheless its inverse image in the prescribed concrete field is

\[
 \pi_y^{-1}(b_y)=T_y(P)
 =\begin{cases}E_{11},&y\notin A,\\
E_{22},&y\in A.\end{cases}
 \tag{MC.13}
\]

Its \((1,1)\) matrix coefficient is \(1-\mathbf1_A\), which is not measurable. This directly disproves automatic inverse transport even for uniformly bounded projection fields.

Forward transport fails too. The fixed concrete field \(P\) is measurable, whereas

\[
 T_y^{-1}\pi_y(P)T_y=L_{U_y^*PU_y}
 \tag{MC.14}
\]

is either \(L_{E_{11}}\) or \(L_{E_{22}}\). Pairing its action on the constant vector \(E_{11}\) with that vector in \(H_0\) yields \(1-\mathbf1_A\); \(\|E_{11}\|_{H_0}^2=1\), so there is no normalization ambiguity. Thus \(\pi_y(P)\) is not a measurable operator field in the transported Hilbert structure.

All maps in (MC.5) are unitary as maps \(H_0\to H_y\) and all \(\pi_y\) are faithful normal isomorphisms. The source of failure is solely the mismatch of the two prescribed field structures. No nonfaithful quotient, infinite weight, nonseparable fibre, variable dimension or unbounded operator is needed.

## The full reverse comparison under typed compatibility

Here is the precise reverse implication that the course can prove with the existing multiplier theorem. Let \(\mathcal A_y=\Lambda_y(\mathfrak a_y)\subset H_y\) be the full associated left Hilbert algebras of faithful normal semifinite \(\varphi_y\), and suppose that they form a measurable field in the full four-clause sense. Assume the typed inverse transport property of MC-01 for \(\pi_y\) into the prescribed concrete field \(M_y\subset B(K_y)\). Then the weights form a measurable field in the entire VIII.4.4 sense.

**Proof.** Let \(a_j(y)\) be measurable algebra sections satisfying VI.3.1. If the chosen convention initially gives graph density of their linear span, adjoin all finite \(\mathbb Q(i)\)-linear combinations. This countable family is set dense in the sharp graph norm: approximate the finitely many coefficients of each finite complex combination by rational complex numbers, controlling the finite sum of its graph norms. Sharp images and pairwise products remain measurable under the enlargement, by finite sums and conjugate coefficients. We can therefore assume the printed set-density convention directly.

DI-04, at its existing field-provider input, proves that each \(L_{a_j(y)}\) is a measurable bounded operator field on \(H_y\), with no common norm bound required. The typed inverse transport gives measurable concrete operator fields

\[
 x_j(y)=\pi_y^{-1}(L_{a_j(y)})\in M_y.
 \tag{MC.15}
\]

Since \(a_j(y)\in\mathcal A_y\), there is \(z_j(y)\in\mathfrak a_y\) with \(a_j(y)=\Lambda_y(z_j(y))\). Equation (MC.2) gives \(L_{a_j(y)}=\pi_y(z_j(y))\). Faithfulness of \(\pi_y\) identifies \(x_j=z_j\), so every \(x_j\) belongs to the full finite-adjoint domain and
\(\Lambda_y(x_j)=a_j\), \(\Lambda_y(x_j^*)=a_j^\sharp\).

The two complete Gram orders are

\[
 \varphi_y(x_j^*x_k)=\langle a_k,a_j\rangle_{H_y},\qquad
 \varphi_y(x_jx_k^*)=\langle a_k^\sharp,a_j^\sharp\rangle_{H_y}.
 \tag{MC.16}
\]

Every coefficient is measurable by the Hilbert-field scalar-product rule and the measurable sharp sections. The positions in (MC.16) use the stated convention that the inner product is linear in the first argument.

Finally (MC.2) identifies the full finite-adjoint norm with the sharp graph norm. For every \(x\in\mathfrak a_y\), approximate \(\Lambda_y(x)\) and its sharp image by \(a_j(y)\) in that graph norm. The corresponding \(x_j(y)\) then approximate \(x\) in exactly \(\varphi_y((x-x_j)^*(x-x_j)+(x-x_j)(x-x_j)^*)^{1/2}\). This proves all of VIII.4.4 on the entire finite-adjoint domain. No global square-integrability restriction was introduced. \(\square\)

The typed inverse transport is used at precisely (MC.15). MC-02–04 prove that it cannot be silently removed, even in dimension two. This theorem is consequently a conditional reverse comparison. It does not assert the unconditional source lemma or establish the compatible realization from the source weight definition.

## Source interpretation and the remaining proof obligations

The compatible forward construction is proved in Two Gram fields before measurability of the involution through The same countable generators act measurably in both representations. An intrinsic graph Gram field and a countable concrete resolvent code recover measurable adjoint and product vectors without assuming the absent mixed Gram coefficients. A common countable strong* dense contraction family through Forward and inverse transport by least indices proves both operator transports by a shared countable contraction family and two separately typed strong-star metrics. The reverse comparison and the realization obstruction proves the reverse implication with inverse compatibility. These proofs leave the counterexample MC-02–04 unchanged: an arbitrary abstract measurable realization supplies neither canonical transport.

The source's associated realization remains tied to its prescribed concrete field. GFR constructs precisely that compatible associated realization from the source test fields. The source leaves Lemma VIII.4.5's proof to the reader; interpreting its associated meaning is recorded explicitly, with independent source-interpretation adjudication still pending.

The sole canonical owner is **TT2-VIII-lemma-4.5**, now with an original public author proof at the named inputs; **MW-DEP-GNS-FIELD** remains its noncounting alias. MC-05 remains a conditional reverse theorem; GFR supplies the compatible construction and the two transports that MC-05 alone did not prove.

The MW consumers use precise GFR clauses. MW-04 identifies the two global represented algebras through the actual measurable normal isomorphism, and MW-07 constructs the pulled-back GNS field for the reverse application. Their full transitive and independent closure remains open. The direct finite-dimensional violation of the definition and concrete matrix-coefficient failure in MC-03/04 require no GFR conclusion.
