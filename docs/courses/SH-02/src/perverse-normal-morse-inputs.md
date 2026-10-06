# SH02-PNM-UNIT — Perverse degrees and normal Morse complexes

The finite holomorphic microsupport argument uses perversity only after passing to a field. This lesson identifies the exact two inputs, checks the dimension shifts, and proves the functorial consequences needed there. The geometric existence of normal Morse models and the construction of the perverse t-structure retain explicit external prerequisite contracts.

## SH02-PNM-CONTRACT — Coefficients, ranges and external theorems

Let $K$ be an arbitrary field, of any characteristic. Let $X$ be a finite-dimensional complex analytic space, locally equipped with a finite complex Whitney stratification $\mathcal S$. Globally the stratification need only be locally finite. Work in $D^b_{\mathcal S,c}(X;K)$, the bounded derived category of complexes with finite-dimensional locally constant cohomology sheaves on its strata. The arguments about degrees also apply to the weakly constructible bounded category when finite-dimensionality is not used.

The mathematical supplier is the 2 June 2021 version of Maxim–Schürmann, [*Constructible sheaf complexes in complex geometry and applications*](https://people.math.wisc.edu/~lmaxim/handbook.pdf). Page numbers below are its printed page numbers. It works with commutative noetherian coefficient rings of finite global dimension; every field satisfies that assumption.

| External contract | Exact statement used | Source location |
| --- | --- | --- |
| Perverse existence | The middle-perverse halves defined by support and cosupport dimensions form a t-structure, also for a fixed Whitney stratification | Definition 2.16 and the gluing paragraph before Theorem 2.18, pp.12–13 |
| Pointwise characterization | On a stratum of complex dimension $d$, the stalk upper bound is $-d$ and the point-costalk lower bound is $d$ | Theorem 2.18, p.13 |
| Normal Morse models | Generic conormal points have normal Morse objects represented by supported normal-slice data, independent up to isomorphism of the allowed local choices | Theorem 3.12 and (26), pp.28–29 |
| Normal Morse bounds | Each perverse half is characterized by its normal Morse objects shifted by minus the complex stratum dimension | Corollary 3.25, pp.35–36; Example 3.26, p.36 |

The perverse-existence argument cites Beilinson–Bernstein–Deligne, *Faisceaux pervers*, Astérisque 100 (1982), Corollary 2.1.4 and Proposition 2.1.14, for gluing t-structures. The normal-Morse bound is proved in the supplier through Theorem 3.19 and (35), pp.32–33, using its complex-link triangles, transverse restriction and real stratified Morse approximation. Those further prerequisites are not proved in this lesson. The table is not a proof of their analytic or categorical foundations.

## SH02-PNM-POINTS — Keeping point costalks distinct from stratum costalks

For $x\in S\in\mathcal S$, put $d=\dim_{\mathbb C}S$ and let $i_x:\{x\}\hookrightarrow X$. The pointwise contract says

$$
\begin{aligned}
F\in{}^pD^{\leq0}
&\Longleftrightarrow F_x\in D^{\leq-d}(K)
\quad\text{for all }x\in S,\ S\in\mathcal S,\\
F\in{}^pD^{\geq0}
&\Longleftrightarrow i_x^!F\in D^{\geq d}(K)
\quad\text{for all }x\in S,\ S\in\mathcal S.
\end{aligned}
\tag{PNM1}
$$

The opposite signs in PNM1 are necessary. Let $i_S:S\hookrightarrow X$ and $j_x:\{x\}\hookrightarrow S$. Composition gives $i_x^!=j_x^!i_S^!$. Since $i_S^!F$ has locally constant cohomology along $S$, the local orientation calculation in manifold duality gives

$$
j_x^!i_S^!F\simeq (i_S^!F)_x[-2d].
\tag{PNM2}
$$

Here the complex manifold supplies its real orientation. Thus the point-costalk bound $d$ is equivalent to the stratum-costalk bound $-d$. Substituting $-d$ directly for the point-costalk bound would lose the real dimension shift $2d$.

The support-dimension formulation makes these conditions intrinsic. Refining the coefficient stratification does not change the two subcategories: both are the perverse halves specified by the external existence contract, rather than new categories defined for each refinement.

## SH02-PNM-BOUNDED — Boundedness from ordinary cohomological bounds

**Lemma.** Suppose $\dim_{\mathbb C}X\leq n$ and $F$ has ordinary cohomology in degrees $[a,b]$. Then

$$
F\in{}^pD^{\geq a-n}\cap{}^pD^{\leq b+n}.
\tag{PNM3}
$$

**Proof.** Every stalk belongs to $D^{\leq b}(K)$. On a stratum of dimension $d\leq n$, this implies the bound required for membership in ${}^pD^{\leq b+n}$, namely ordinary stalk degree at most $b+n-d$.

For the other half, sections with support form a left exact functor. Its right derived functor sends complexes in $D^{\geq a}$ into $D^{\geq a}$. Taking the stalk of the corresponding supported sheaf shows that $i_x^!F\in D^{\geq a}(K)$. This is at least the required lower bound $a-n+d$ on every stratum. The shifted version of PNM1 therefore gives $F\in{}^pD^{\geq a-n}$. $\square$

The estimates are deliberately uniform rather than optimal. They prove boundedness of the perverse t-structure in the finite-dimensional setting used here. Only the dimension bound and the ordinary boundedness of $F$ enter; no global finite partition is required.

## SH02-PNM-NORMAL — The normal Morse object and its shift

Fix a generic covector on a conormal component associated with a stratum $S$ of complex dimension $d$. Choose an allowed normal slice and a normal Morse model. Write $N_S(F)$ for the unnormalized normal Morse complex. It is a supported local complex on that slice; a finite relative-pair model, when supplied by the normal-Morse prerequisite, computes the same object.

The perverse normalization is

$$
\mu_S(F)=N_S(F)[-d].
\tag{PNM4}
$$

The normal-Morse bound contract states, for either choice of inequality,

$$
F\in{}^pD^{\leq0}\ \Longrightarrow\ \mu_S(F)\in D^{\leq0}(K),
\qquad
F\in{}^pD^{\geq0}\ \Longrightarrow\ \mu_S(F)\in D^{\geq0}(K).
\tag{PNM5}
$$

Its converse holds when these conditions are checked on all strata, but only the forward implications are needed for t-exactness below. For a perverse sheaf, $N_S(F)$ is concentrated in degree $-d$; it is $\mu_S(F)$ which is concentrated in degree zero.

The shift comes from the complex dimension of the stratum, not from the dimension of the normal slice or the real dimension of the ambient manifold. In a holomorphic stratified Morse test, the tangential real Morse index is $d$. The tangential contribution shifts the unnormalized normal Morse complex by $[-d]$, giving precisely PNM4. This identifies the convention used in the isolated-test argument of finite holomorphic microsupport.

## SH02-PNM-EXACT — Exactness of the fixed normal Morse functor

**Proposition.** With a fixed allowed normal Morse model, $\mu_S$ is an exact functor of triangulated categories and is t-exact from the perverse t-structure to the ordinary t-structure on $D^b(K)$.

**Proof.** Restriction to the normal slice is an exact derived functor. Derived sections with support, followed by a stalk, is exact as a functor of triangulated categories. Alternatively, in a fixed relative-pair model $(A,B)$ one takes the fibre of the natural restriction map

$$
R\Gamma(A;F|_A)\longrightarrow R\Gamma(B;F|_B).
\tag{PNM6}
$$

The relative derived-sections functor carries distinguished triangles to distinguished triangles, as follows from the localization triangle, or from the cone construction on complexes computing this fixed restriction. Applying a fixed shift preserves exactness. Thus PNM4 is an exact functor, including its action on morphisms.

The two implications PNM5 show that it preserves the nonpositive and nonnegative halves. This is the definition of t-exactness. $\square$

The proof fixes one model, so it does not manufacture functorial identifications by choosing unrelated pair representatives for each object. The allowed model's existence, stabilization and comparison with the supported local complex remain the normal-Morse prerequisite.

## SH02-PNM-COHOMOLOGY — Commutation with perverse cohomology

**Corollary.** For every integer $j$ there is a natural isomorphism

$$
\mu_S({}^pH^jF)\simeq H^j(\mu_SF),
\tag{PNM7}
$$

where the right side is placed in ordinary degree zero.

**Proof.** Apply the exact functor $\mu_S$ to a perverse truncation triangle. Its first term lands in the required ordinary nonpositive range and its third term in the required ordinary positive range, by t-exactness. The resulting triangle is therefore the ordinary truncation triangle of $\mu_SF$, by the uniqueness property of a t-structure. This gives natural comparisons with truncation. Taking the two adjacent truncations defining cohomology gives PNM7. $\square$

In particular, because the complexes and the perverse t-structure are bounded,

$$
\mu_SF\simeq0
\quad\Longleftrightarrow\quad
\mu_S({}^pH^jF)\simeq0\text{ for every }j.
\tag{PNM8}
$$

Indeed an ordinary bounded complex is zero exactly when all its cohomology groups vanish; PNM7 applies degree by degree. No splitting of $F$ into its perverse cohomology objects is asserted, and no semisimplicity of the perverse category is needed.

If one additionally imports the normal-Morse detection theorem that closed conormal components occur in microsupport exactly when their generic normal Morse objects are nonzero, PNM8 yields

$$
\operatorname{SS}(F)=\bigcup_j\operatorname{SS}({}^pH^jF).
\tag{PNM9}
$$

This last statement is conditional on that detection theorem. It is the component-by-component deduction used in FH21, and does not prove the geometric detection theorem itself.

## SH02-PNM-EXAMPLES — Checking the degrees on a smooth stratum

Let $X$ be a smooth complex $d$-manifold and $L$ a finite-dimensional $K$-local system. Then $P=L[d]$ satisfies PNM1: its stalk lies in degree $-d$, while its point costalk, by PNM2, lies in degree $d$. Thus $P$ is perverse.

With the single smooth stratum, a normal slice is a point. Its normal Morse object is $N_X(P)=L_x[d]$. Applying PNM4 gives $\mu_X(P)=L_x$ in degree zero, as required.

On a point stratum $d=0$, all three conventions coincide: ordinary cohomological degree, perverse degree and normalized Morse degree. These two examples verify both endpoints of the dimension normalization.

## SH02-PNM-STATUS — What this lesson supplies

PNM3 proves boundedness from ordinary bounds. PNM4–PNM7 fix the normal Morse shift and prove t-exactness and its functorial cohomology comparison relative to the exact listed inputs. PNM8 is the nonvanishing deduction needed to inspect one perverse cohomology object at a time.

The original coefficient ring in the finite-map theorem can be more general than a field. This lesson applies only after the specified derived extension to a residue field; no perverse truncation over the original ring is introduced. The finite normal-pair and coefficient arguments must still supply the bounded finite-dimensional objects to which this lesson applies.

In particular, this lesson does not infer a general interchange of tensor product with nearby-cycle limits, or invoke the nonisolated vanishing-cycle route retained as an alternative in the finite-map lesson.
