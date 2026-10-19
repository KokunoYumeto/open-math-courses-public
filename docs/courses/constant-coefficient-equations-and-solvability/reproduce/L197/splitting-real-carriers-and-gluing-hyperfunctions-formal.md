# Splitting real carriers and gluing hyperfunctions

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. CC0.*

An analytic functional cannot be multiplied by an arbitrary smooth cutoff. We instead cut off its harmonic potential and correct the resulting Laplace error. This gives decomposition among real carriers, genuine restriction of hyperfunctions and gluing on every open cover. A separate convergent correction series handles infinitely many compatible pieces.

Basic references are Mikio Sato's *Theory of Hyperfunctions, I* and *II*, André Martineau's *Supports des fonctionnelles analytiques*, and Lars Hörmander's *The Analysis of Linear Partial Differential Operators I*. The available proofs used here are [Harmonic potentials and real carriers][A], especially Theorems 4.2 and 5.1, the [Poisson ball formula][P], and [seminorm Hahn–Banach and separation][H], Propositions 1.1-1.2. The smooth partition construction is the partition lemma in [Boundary flux and weak identities][F]. All pairings are complex linear.

Write \(\mathcal A'(K)\) for the analytic functionals carried by a compact real set \(K\subset\mathbb R^n\), with the every-complex-neighborhood bounds proved in [Harmonic potentials and real carriers][A]. They have unique local holomorphic germ action and smallest real carriers, called their supports. No finite distributional order or convexity is assumed. Put \(d=n+1\geq2\), write \(X=(x,t)\), and set \(K^\flat=K\times\{0\}\). The harmonic representation identifies these functionals with odd harmonic functions off \(K^\flat\), modulo odd harmonic functions on the full real space. We use its naturality: enlarging a real carrier simply restricts the same potential to a smaller complement. This follows either from the kernel definition or from its injective residue formula.

## 1. Harmonic approximation with every finite derivative

Let \(E_d\) be the positive-Laplacian fundamental solution proved in Section 2 of [Harmonic potentials and real carriers][A]:
\[
 E_2(X)=\frac{\log|X|}{2\pi},\qquad
 E_d(X)=\frac{|X|^{2-d}}{(2-d)\sigma_d}\quad(d\geq3),
 \qquad \Delta E_d=\delta_0.
 \tag{HG1}
\]
Here \(\sigma_d\) is the unit sphere's area. Let \(\mathcal H(\Omega)\) denote the complex-valued smooth harmonic functions on an open set \(\Omega\subset\mathbb R^d\).

**Theorem 1.1 (harmonic Runge approximation).** Let \(L\subset\Omega\) be compact. Suppose every bounded connected component of \(\mathbb R^d\setminus L\) meets \(\mathbb R^d\setminus\Omega\). If \(h\) is harmonic near \(L\), then for every nonnegative integer \(m\) and every \(\varepsilon>0\) there is \(v\in\mathcal H(\Omega)\) with
\[
 \max_{|\alpha|\leq m}\sup_L|\partial^\alpha(h-v)|<\varepsilon.
 \tag{HG2}
\]

*Proof.* First recall an interior estimate that follows directly from the ball Poisson formula. On concentric balls of radii \(r\) and \(2r\), differentiating the kernel after scaling gives
\[
 \sup_{B(a,r)}|\partial^\alpha q|
       \leq C_{d,\alpha}r^{-|\alpha|}
                           \sup_{B(a,2r)}|q|
 \tag{HG3}
\]
for every harmonic \(q\) near the larger closed ball. The denominators are separated from zero on the smaller ball times the boundary sphere, so every fixed derivative is uniformly bounded. The representation and its uniqueness are [Poisson extension and subharmonic comparison][P], Theorem P3. The same argument proves smooth convergence of locally uniformly convergent harmonic functions and real analyticity, as recorded in Section 2 of [Harmonic potentials and real carriers][A].

If approximation failed, apply Hahn–Banach separation to the finite jet vectors on \(L\), with the maximum norm on the finite product of spaces \(C(L)\). This gives a compact distribution \(T\) of order at most \(m\), supported in \(L\), which kills every member of \(\mathcal H(\Omega)\) but not \(h\). Explicitly the separating functional on the product acts on \((\partial^\alpha\phi|_L)_{|\alpha|\leq m}\). It obeys the displayed finite derivative bound, so is a distribution supported in \(L\). No measure representation theorem is needed. A smooth cutoff equal to one near \(L\) makes its action on local smooth functions unambiguous. The normed and seminorm extension steps are proved in [Continuous functionals, test families and compact limits][H], Propositions 1.1-1.2.

Consider \(W=E_d*T\). It is harmonic off \(L\), is a distribution on the full space, and satisfies \(\Delta W=T\). The construction in [Proper convolution and compact support][U] applies because the second factor is compact. Transferring test derivatives through that factor and using (HG1) gives the asserted equation; off \(L\), the formula is simply
\[
 W(Y)=T_X(E_d(Y-X)).
 \tag{HG4}
\]
For \(Y\notin\Omega\), every source derivative \(\partial_Y^\beta E_d(Y-\cdot)\) is harmonic on \(\Omega\). Thus all derivatives of \(W\) vanish at \(Y\). Harmonic analyticity makes \(W\) zero throughout every component of \(\mathbb R^d\setminus L\) meeting the complement of \(\Omega\).

It is zero in the unbounded component too. Indeed \(T\) kills every entire harmonic polynomial. For \(|Y|\) larger than twice a ball containing \(L\), the homogeneous expansion of \(E_d(Y-X)\) in \(X\) consists of harmonic polynomials and converges with every derivative required by \(T\). The expansion, including the logarithmic case, is proved in Lemma 4.1 of [Harmonic potentials and real carriers][A]. Its uniform convergence on a slightly larger real ball implies convergence of all finite derivatives on the smaller ball by (HG3), since its partial sums are harmonic. Therefore (HG4) is zero there. Analytic continuation gives zero in the whole unbounded component.

The hypothesis accounts for every other component, so \(\operatorname{supp}W\subset L\). Choose a compact smooth \(\chi=1\) near \(L\), supported where \(h\) is harmonic. Distributional integration by parts gives
\[
 T(h)=\langle\Delta W,\chi h\rangle
      =\langle W,\Delta(\chi h)\rangle=0,
 \tag{HG5}
\]
since the last test vanishes near \(L\). This contradicts separation and proves the theorem. \(\square\)

If \(\Omega,L,h\) are invariant under reflection \(R(x,t)=(x,-t)\), with \(h\) odd, replace an approximant by \((v-v\circ R)/2\). Reflection permutes the relevant derivative bounds with signs, so the same error estimate holds and the approximant is odd.

## 2. Solve the Laplace error off a real compact set

**Lemma 2.1 (a suitable exhaustion).** For compact real \(S\), including the empty set, put
\[
 \Omega_S=\mathbb R^d\setminus S^\flat,\qquad
 L_j=\{X:|X|\leq j,\ \operatorname{dist}(X,S^\flat)\geq1/j\}.
 \tag{HG6}
\]
Use infinite distance when \(S\) is empty. These are reflection-invariant compact sets, \(L_j\subset\operatorname{int}L_{j+1}\), exhausting \(\Omega_S\). Every bounded component of \(\mathbb R^d\setminus L_j\) meets \(S^\flat\).

*Proof.* The strict radius and distance inequalities prove the compactness, nesting and exhaustion statements. The complement is the union of the exterior of the radius-\(j\) ball and the open radius-\(1/j\) neighborhood of \(S^\flat\). A point in that neighborhood joins a nearest point of \(S^\flat\) by a segment within the same neighborhood. A component meeting the exterior is unbounded; any other component therefore contains such a nearest point. This also proves the assertion for an empty \(S\), when only the unbounded exterior remains. \(\square\)

**Theorem 2.2 (global smooth Laplace solvability on this complement).** For every \(f\in C^\infty(\Omega_S)\) there is \(v\in C^\infty(\Omega_S)\) with \(\Delta v=f\). If \(f\) is odd, \(v\) can be chosen odd. No bound near \(S^\flat\) or at infinity is imposed on \(f\).

*Proof.* Choose \(\chi_j\in C_c^\infty(\Omega_S)\), equal to one near \(L_j\), with support in \(\operatorname{int}L_{j+1}\), and put \(\chi_0=0\). The smooth cutoff construction is the one linked in [Boundary flux and weak identities][F]. Set
\[
 f_j=(\chi_j-\chi_{j-1})f,\qquad v_j=E_d*f_j.
 \tag{HG7}
\]
Each \(f_j\), extended by zero, is compact smooth on the full space. Thus \(v_j\) is globally smooth and \(\Delta v_j=f_j\). The sources sum locally finitely to \(f\). For \(j\geq3\), \(f_j\) vanishes near \(L_{j-1}\), so \(v_j\) is harmonic near \(L_{j-2}\). By Theorem 1.1 and Lemma 2.1 choose \(h_j\in\mathcal H(\Omega_S)\) such that
\[
 \|v_j-h_j\|_{C^j(L_{j-2})}<2^{-j}.
 \tag{HG8}
\]
Empty compact sets require no condition. The series
\[
 v=v_1+v_2+\sum_{j=3}^\infty(v_j-h_j)
 \tag{HG9}
\]
converges with every derivative on every compact subset of \(\Omega_S\). For fixed \(L_N\) and derivative order \(m\), all terms with \(j\geq\max(N+2,m,3)\) satisfy the summable bound (HG8). Hence termwise Laplacians are legitimate and give \(\Delta v=f\). If \(f\) is odd, the odd part of \(v\) solves the same equation. \(\square\)

## 3. Decompose among compact real carriers

**Theorem 3.1 (finite carrier decomposition).** If \(K_1,\ldots,K_r\subset\mathbb R^n\) are compact and \(u\in\mathcal A'(K_1\cup\cdots\cup K_r)\), then
\[
 u=u_1+\cdots+u_r,\qquad u_i\in\mathcal A'(K_i).
 \tag{HG10}
\]

*Proof.* It suffices to prove the two-set case and iterate. Put \(S=K_1\cap K_2\) and take an odd harmonic representative \(U\) of \(u\) off \((K_1\cup K_2)^\flat\). In \(\Omega_S\), the sets \(K_1^\flat\setminus S^\flat\) and \(K_2^\flat\setminus S^\flat\) are disjoint relatively closed sets. Choose a smooth \(\theta\), equal to one near the first and zero near the second, on this open space. Here is the precise separation construction. Apply the smooth partition lemma to the two open complements of these closed sets. The partition factors subordinate to the complement of the second set sum to one near the first and zero near the second, by local finiteness and the support containment. Their sum is a smooth separating function. Reflect and average it to make it even in \(t\).

The function \(\Delta(\theta U)\), initially off both carriers, extends smoothly by zero across their portions outside \(S^\flat\): there \(\theta\) is constant and \(U\) is harmonic off the carrier. It is an odd smooth function on \(\Omega_S\). By Theorem 2.2 choose odd smooth \(v\) on this space with
\[
 \Delta v=\Delta(\theta U).
 \tag{HG11}
\]
Then
\[
 U_1=\theta U-v,\qquad U_2=(1-\theta)U+v
 \tag{HG12}
\]
extend as odd harmonic functions off \(K_1^\flat\) and \(K_2^\flat\), respectively. For instance the first product is zero near the second carrier's portion outside the first, while its Laplacian is canceled everywhere it is defined; the other extension is identical with the roles exchanged. The harmonic representation theorem gives \(u_i\in\mathcal A'(K_i)\). The sum of the representatives is \(U\), so naturality and injectivity give \(u_1+u_2=u\). Empty carriers and empty intersections are covered by the same proof, with \(\Omega_\varnothing=\mathbb R^d\). \(\square\)

The split need not be unique when the carriers overlap. If two two-set splits have the same sum, the difference of their first terms is carried by both \(K_1\) and \(K_2\), hence by \(K_1\cap K_2\). This follows from Theorem 5.1 of [Harmonic potentials and real carriers][A]. It is the exact ambiguity.

## 4. A compatible sequence modulo decreasing real carriers

**Theorem 4.1 (completeness for decreasing real carriers).** Let \(K\) be compact real and \(K_j\subset K\) compact decreasing, with intersection \(S\). Suppose \(u_j\in\mathcal A'(K)\) and
\[
 u_k-u_j\in\mathcal A'(K_j)\quad(k\geq j).
 \tag{HG13}
\]
There is \(u\in\mathcal A'(K)\) with
\[
 u-u_j\in\mathcal A'(K_j)\quad\hbox{for every }j.
 \tag{HG14}
\]
It is unique modulo \(\mathcal A'(S)\).

*Proof.* If \(S\) is empty, compactness and decreasingness imply some \(K_j\) is empty. The sequence is then constant from that index and the assertion follows. Assume \(S\ne\varnothing\). Let \(U_j\) be the normalized odd harmonic potential of \(u_j\). Its differences extend harmonically off \(K_j^\flat\), by (HG13) and the harmonic representation.

Choose strictly increasing indices \(a_j\) such that \(K_{a_j}^\flat\) lies in the open radius-\(1/(2j)\) neighborhood of \(S^\flat\). Such indices exist: otherwise a subsequence of points in the nested compact sets, outside that fixed neighborhood, would have a limit in their intersection. In the exhaustion (HG6), the odd harmonic extension of \(U_{a_{j+1}}-U_{a_j}\) is defined near \(L_j\). Choose odd \(h_j\in\mathcal H(\Omega_S)\) with
\[
 \|U_{a_{j+1}}-U_{a_j}-h_j\|_{C^j(L_j)}<2^{-j}.
 \tag{HG15}
\]
The series
\[
 V=U_{a_1}+\sum_{j=1}^\infty
                       (U_{a_{j+1}}-U_{a_j}-h_j)
 \tag{HG16}
\]
defines an odd harmonic function off \(K^\flat\). All derivatives converge on every compact there, by the same summable-tail argument as in Theorem 2.2. Let \(u\in\mathcal A'(K)\) be its harmonic class.

For fixed \(p\), telescoping rewrites
\[
 V-U_{a_p}=-\sum_{j<p}h_j+
                   \sum_{j\geq p}(U_{a_{j+1}}-U_{a_j}-h_j).
 \tag{HG17}
\]
Every term on the right is harmonic off \(K_{a_p}^\flat\), and the series converges with every derivative on compact subsets there. It therefore extends the left side to that whole complement. Naturality of harmonic reconstruction proves \(u-u_{a_p}\in\mathcal A'(K_{a_p})\). For arbitrary \(j\), choose \(a_p\geq j\); adding (HG13) and using \(K_{a_p}\subset K_j\) proves (HG14). Two answers differ by a functional carried by every \(K_j\), and the least-real-carrier theorem places the difference in \(\mathcal A'(S)\). Conversely adding such a functional preserves (HG14). \(\square\)

This theorem concerns real carriers and has exact membership for every index. It is the completeness statement needed for countable localization below.

## 5. Quotient classes and restriction

For bounded open \(X\subset\mathbb R^n\), including disconnected or empty sets, define
\[
 \mathcal B(X)=\mathcal A'(\overline X)/\mathcal A'(\partial X).
 \tag{HG18}
\]
These are hyperfunctions in the analytic-functional model. For a representative \(a\), define its class support in \(X\) by \(X\cap\operatorname{supp}_{\mathcal A}a\). This is independent of the representative: adding a functional supported on \(\partial X\) adds a potential harmonic across every point of \(X\), so changes none of the singular extension points there.

**Theorem 5.1 (restriction and its zero criterion).** If \(Y\subset X\) are bounded open sets, there is a canonical linear restriction \(r_{XY}:\mathcal B(X)\to\mathcal B(Y)\). Choose, using Theorem 3.1,
\[
 a=b+c,\qquad b\in\mathcal A'(\overline Y),\quad
             c\in\mathcal A'(\overline X\setminus Y),
 \qquad r_{XY}[a]=[b].
 \tag{HG19}
\]
It is independent of all choices, composes under nested restriction, and satisfies
\[
 r_{XY}[a]=0\quad\Longleftrightarrow\quad
                 Y\cap\operatorname{supp}_{\mathcal A}a=\varnothing.
 \tag{HG20}
\]

*Proof.* The two compact sets in (HG19) cover \(\overline X\). If a representative or split changes, the two resulting \(b\)'s differ by a functional carried by \(\overline Y\) and by \(\overline X\setminus Y\): the original representative difference is on \(\partial X\), which lies in the latter set. The real intersection theorem places that difference in \(\mathcal A'(\partial Y)\). Thus the class is well-defined.

The same argument gives a useful characterization: any \(b\in\mathcal A'(\overline Y)\) for which \(a-b\) has compact real support disjoint from \(Y\) represents the restriction. For \(Z\subset Y\subset X\), the two successive discarded pieces are both supported outside \(Z\). This characterization proves \(r_{YZ}r_{XY}=r_{XZ}\) and also \(r_{XX}=1\). If the class of \(b\) is zero, it is carried by \(\partial Y\), so both terms of (HG19) are supported outside \(Y\). Conversely, if \(a\)'s support misses \(Y\), the choice \(b=0,c=a\) is valid. This proves (HG20). \(\square\)

Consequently a hyperfunction's support is exactly the complement of the largest open set on which its restriction vanishes. In particular, vanishing on every member of a cover implies vanishing on the union, with no finiteness requirement.

## 6. Gluing and the local differential equation

**Theorem 6.1 (gluing on every open cover).** If \(X=\bigcup_{i\in I}X_i\) is any open cover in \(\mathbb R^n\) and \(q_i\in\mathcal B(X_i)\) agree on all overlaps, there is a unique \(q\in\mathcal B(X)\) with these restrictions. For unbounded open sets, \(\mathcal B(X)\) means compatible classes on all bounded open subsets of \(X\); this agrees with (HG18) when \(X\) is bounded.

*Proof.* First assume a bounded union and two sets. Choose representatives \(a_i\in\mathcal A'(\overline X_i)\), and put \(K=\overline X_1\cup\overline X_2\). By (HG20), the difference \(a_1-a_2\) is supported in
\[
 K\setminus(X_1\cap X_2)=(K\setminus X_1)\cup(K\setminus X_2).
 \tag{HG21}
\]
Theorem 3.1 writes it as \(c_1+c_2\), with \(c_i\) carried by \(K\setminus X_i\). Then
\[
 a=a_1-c_1=a_2+c_2
 \tag{HG22}
\]
has the required restrictions, by the characterization after (HG19). It is carried by \(K=\overline{X_1\cup X_2}\). Uniqueness for any cover already follows from the support zero criterion: a difference zero on every member has empty support in the union. Iterating the two-set construction handles every finite cover.

For a countable cover of bounded \(X\), let \(Y_j=X_1\cup\cdots\cup X_j\). Finite gluing gives compatible classes on the \(Y_j\); choose representatives \(a_j\in\mathcal A'(\overline Y_j)\subset\mathcal A'(\overline X)\). For \(k\geq j\), their difference restricts to zero on \(Y_j\), so it is carried by
\[
 K_j=\overline X\setminus Y_j,\qquad
                 \bigcap_jK_j=\partial X.
 \tag{HG23}
\]
Theorem 4.1 gives \(a\in\mathcal A'(\overline X)\) with \(a-a_j\) carried by \(K_j\). Its class in \(\mathcal B(X)\) restricts to the prescribed class on every \(Y_j\), and hence on each original member.

Every open cover in Euclidean space has a countable subcover. To see this, use the countable basis of balls with rational centers and radii, selecting for each basis ball contained in some cover member one such member. These selected members cover every point. Glue on this countable subcover. On any unselected member, the resulting class and the prescribed one agree on its intersections with the selected members; uniqueness by the support criterion gives agreement on that whole member. This proves arbitrary gluing for a bounded union.

For general open \(X\), define a class as a compatible family over all its bounded open subsets, using Theorem 5.1's restriction maps. A bounded \(X\) itself is one of those subsets, so this definition agrees exactly with (HG18). Given data on a cover of any \(X\), glue on each bounded open \(V\subset X\) using the cover \(V\cap X_i\) and the bounded-union case. Uniqueness makes these glued classes compatible as \(V\) varies. They therefore give the desired class on \(X\). The same argument proves uniqueness and restriction to arbitrary open subsets. \(\square\)

**Theorem 6.2 (compact carriers, distributions and operations).** Every compact-real-carrier analytic functional defines a hyperfunction with exactly the same support. For compact \(K\subset X\), the hyperfunctions supported in \(K\) are canonically \(\mathcal A'(K)\). Ordinary distributions embed injectively into hyperfunctions with the same supports. Constant-coefficient derivatives commute with every restriction and with gluing, and the Dirac functional is the ordinary point evaluation functional.

*Proof.* For an analytic functional \(a\) with compact carrier, and bounded open \(V\), choose bounded \(Z\) containing both that carrier and \(\overline V\). Restrict its class from \(Z\) to \(V\). Two choices agree after restriction from a larger such set, by Theorem 5.1. These classes form a hyperfunction. Its support is exactly the least real carrier, by (HG20), so the map is injective.

If a class on bounded \(X\) has compact support \(K\subset X\), any representative has support contained in \(K\cup\partial X\). Theorem 3.1 splits it into a functional carried by \(K\) and one carried by \(\partial X\). The first is unique, since a difference carried by the disjoint sets \(K\) and \(\partial X\) is zero. For unbounded \(X\), choose a bounded relatively compact neighborhood of \(K\) inside \(X\), apply that argument there, and compare with zero outside \(K\) using gluing uniqueness.

Derivatives preserve analytic carriers by Cauchy's inequalities, as proved in Section 5 of [Harmonic potentials and real carriers][A]. They therefore descend to (HG18). If \(a-b\) is supported outside \(Y\), the same holds of its derivative. The restriction characterization proves commutation. This also proves commutation with gluing by uniqueness. With \(D_j=-i\partial_j\), the bilinear transpose convention is
\[
 (P(D)a)(g)=a(P(-D)g).
 \tag{HG24}
\]
For an ordinary distribution on arbitrary open \(X\), choose relatively compact neighborhoods covering \(X\) and ordinary smooth cutoffs equal to one on their closures. Each cutoff distribution is compact, so gives an analytic functional with the same support by Theorem 5.1 of [Harmonic potentials and real carriers][A]. Different cutoffs have differences supported outside the smaller neighborhood; hence their hyperfunction restrictions agree. Gluing gives the embedding. The same local support statement proves its injectivity and exact support. On these compact pieces, differentiation differs from differentiation before cutoff only by terms supported off the smaller neighborhood. Therefore this embedding respects derivatives too. In particular \(\delta_a(g)=g(a)\), with support \(\{a\}\), has its ordinary meaning. \(\square\)

**Corollary 6.3 (realizing compatible local equations).** Suppose for every relatively compact open \(V\) there is a compact-real-carrier analytic functional \(a_V\), and the support of \(a_V-a_W\) misses \(V\cap W\). Their restrictions define a unique global hyperfunction. If their supports lie in a fixed closed set \(F\), so does that hyperfunction. If, for a constant-coefficient polynomial, \(P(D)a_V-\delta_0\) has support disjoint from \(V\), then its global realization solves \(P(D)q=\delta_0\).

*Proof.* The zero criterion gives compatibility. Theorem 6.1 glues, and Theorem 6.2 commutes the differential operator with the restrictions. Both the support conclusion and the equation hold on the whole relatively compact open cover, hence globally. The same proof works with any already defined compatible right side in place of the Dirac functional. \(\square\)

The analytic functional estimates and cutoff commutators in [Small Gevrey fundamental solutions in the principal polar cone][E] verify precisely these hypotheses. The result applies to those functionals even when they are not distributions.

## References

- Mikio Sato, *Theory of Hyperfunctions, I* and *II*, Journal of the Faculty of Science, University of Tokyo, Section I, 8 (1959-1960). [Part I](https://repository.dl.itc.u-tokyo.ac.jp/records/39927), [Part II](https://repository.dl.itc.u-tokyo.ac.jp/record/39925/file_preview/jfs080207.pdf).
- André Martineau, *Supports des fonctionnelles analytiques*, Séminaire d'analyse, 5 (1962-1963), exposé 4. [Original article](https://www.numdam.org/item/SL_1962-1963__5__A4_0/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990; 2003 reprint. Reference for analytic-functional carrier decomposition and the quotient model of hyperfunctions.
- The linked preceding lessons contain the harmonic representation, real support theorem, Poisson formula, smooth partitions and Hahn–Banach extension used here. The harmonic approximation and global smooth Laplace correction are proved in Sections 1-2 above.

[A]: ../../AN02-L196.html#complete-proof
[P]: ../../AN02-L132.html#the-unit-ball-poisson-operator
[H]: ../../AN02-L042.html#from-normed-extension-to-seminorm-bounds
[F]: ../../prerequisites/boundary-flux-and-weak-identities.html
[E]: ../../AN02-L052.html#from-the-functional-to-a-hyperfunction
[U]: ../../prerequisites/proper-convolution-and-compact-support.html
