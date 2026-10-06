# Weak Lefschetz and complete-intersection ranks

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

This supporting reading retains the completed weak Lefschetz deduction and complete-intersection rank argument from Lesson 11. Both arguments precede its weight theorem and use affine vanishing, smooth duality, Bertini and smooth proper base change. Their use here requires neither the higher-dimensional Riemann hypothesis nor smooth-projective alteration existence. Equation and proposition labels retain the original lesson locators.

## 1. Weak Lefschetz and the actual dual map

The precise affine input is [*Cohomological dimension and the Künneth formula*, Theorem 5.1](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula). Its §§2–5 give the complete simultaneous dimension induction: limits and curve/field bounds, strict-local finite models, closed support approximation, and the two Leray spectral sequences for \(\mathbf A^d\subset\mathbf P^1\times\mathbf A^{d-1}\). The result is
\[
H^r(W,G)=0\quad(r>\dim W)
\tag{1.1}
\]
for **every torsion étale sheaf** \(G\) on an affine finite-type scheme \(W\) over an algebraically closed field. Neither smoothness of \(W\) nor local constancy of \(G\) is required. We consume its prime-to-characteristic constant-coefficient case; the all-torsion assertion does not extend Poincaré duality to characteristic-primary coefficients.

**Proposition 1.2 (weak Lefschetz, with its dual map).** Let \(X/k\) be smooth projective of pure dimension \(d\ge1\), with \(k\) algebraically closed, and let \(i:Y\hookrightarrow X\) be a smooth ample effective Cartier divisor. For any integer \(a\), restriction
\[
i^*:H^r(X,\mathbf Q_\ell(a))\longrightarrow
H^r(Y,\mathbf Q_\ell(a))
\tag{1.2}
\]
is an isomorphism for \(r<d-1\) and injective for \(r=d-1\). Its dual Gysin map
\[
i_*:H^{2d-2-r}(Y,\mathbf Q_\ell(-1))
\longrightarrow H^{2d-r}(X,\mathbf Q_\ell)
\tag{1.3}
\]
is an isomorphism in the first range and surjective at \(r=d-1\). All maps are Frobenius-equivariant when the pair is defined over a finite field.

**Proof.** Put \(U=X-Y\). This complement is affine. Indeed, choose a power \(L^{\otimes b}\) of the ample line bundle \(L=\mathcal O_X(Y)\) which is very ample. Include the nonzero section \(s^b\), whose vanishing support is \(Y\), in a basis of its global sections. The resulting embedding realizes \(U\) as the closed subscheme of the affine chart where that coordinate is nonzero. If a component is disjoint from \(Y\), ampleness would make a positive-dimensional projective component affine, which is impossible; dimension-zero components are excluded by pure dimension \(d\). Thus \(U\) is smooth of pure dimension \(d\).

Work first over \(\Lambda_b=\mathbf Z/\ell^b\mathbf Z\). The affine theorem gives \(H^{2d-t}(U,\Lambda_b(d-a))=0\) for \(t<d\). The finite-coefficient smooth duality theorem in the supporting lesson identifies its exact \(\Lambda_b\)-dual with \(H^t_c(U,\Lambda_b(a))\); hence
\[
H^t_c(U,\Lambda_b(a))=0\quad(t<d).
\tag{1.4}
\]
For these smooth schemes the finite-coefficient groups are finite. Their inverse systems therefore satisfy Mittag–Leffler: the descending images in each fixed finite group stabilize. The Milnor sequence for derived inverse limit consequently has zero \(\varprojlim^1\) term. Taking \(R\varprojlim_b\) in (1.4), then tensoring with \(\mathbf Q_\ell\), gives \(H^t_c(U,\mathbf Q_\ell(a))=0\) for \(t<d\). This also explains why an unexamined ordinary inverse limit of an exact sequence would be insufficient.

The closed-open triangle on proper \(X\) gives
\[
H^r_c(U,\mathbf Q_\ell(a))\longrightarrow H^r(X,\mathbf Q_\ell(a))
\xrightarrow{i^*}H^r(Y,\mathbf Q_\ell(a))
\longrightarrow H^{r+1}_c(U,\mathbf Q_\ell(a)).
\tag{1.5}
\]
Both outer terms vanish when \(r<d-1\); the first vanishes when \(r=d-1\). This proves the restriction assertions, including \(d=1\), where the asserted isomorphism range in nonnegative degrees is empty.

For \(a=0\), the transpose of restriction under the perfect pairings is the map from \(H^{2d-2-r}(Y,\mathbf Q_\ell(d-1))\) to \(H^{2d-r}(X,\mathbf Q_\ell(d))\). It is the Gysin counit, because the supporting lesson's projection formula and trace compatibility give
\(\int_Y i^*x\cup y=\int_Xx\cup i_*y\).
Cancelling the common twist \((d)\) gives exactly (1.3). The dual of an injective map of finite-dimensional spaces is surjective, and the dual of an isomorphism is an isomorphism. The constructions commute with field automorphisms, so the equivariance and the twisted assertions follow. \(\square\)

## 2. Ranks outside the middle for every smooth complete intersection

Let X be a smooth complete intersection of dimension n and fixed positive multidegrees over an algebraically closed field. The proof includes presentations whose intermediate intersections may be singular.

We first justify the cohomology outside the middle, including for a presentation whose intermediate intersections might be singular. Fix the multidegrees \(d_1,\ldots,d_r\). Over the algebraic closure, tuples of defining equations belong to a product of projective coefficient spaces. The locus \(T\) where their intersection is smooth of the expected dimension is open and contains the given tuple. It is an irreducible, hence connected, nonempty open subset. The universal complete intersection over \(T\) is smooth and proper. Smooth proper base change makes each \(R^if_*\mathbf Q_\ell\) lisse, so its rank is constant on \(T\).

There is a tuple for which all successive intersections are smooth: choose each equation generally on the previous smooth intersection, using Bertini for the very ample bundle \(\mathcal O(d_j)\). For that tuple, successive weak Lefschetz and duality give the ranks
\[
\dim H^i(X)=
\begin{cases}
1,&i\ne n,\ 0\le i\le2n,\ i\text{ even},\\
0,&i\ne n,\ i\text{ odd}.
\end{cases}
\tag{7.2}
\]
Rank constancy proves (7.2) for every smooth tuple in \(T\). This deformation argument uses étale smooth proper base change, not a complex lift.

The original human sources retain their own terms; this independently authored proof excerpt retains the stated CC0 dedication.
