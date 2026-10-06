# Finite free actions: fixed centers, invariant corners, and exact coboundaries

Let a finite group act freely on a von Neumann algebra. The fixed algebra has exactly the fixed ambient center. A projection finite in the fixed algebra is finite in the ambient algebra, and every unitary one-cocycle is a coboundary with the specified orientation. We prove these assertions for arbitrary von Neumann algebras, including nonfactors and algebras that have no faithful normal state.

The proof combines finite crossed-product calculations with projection comparison and a finite-corner trace argument. Takesaki, *Theory of Operator Algebras II*, Proposition XI.2.26 records the standard theorem and remains part of its scholarly history. The construction is written out here, with the projection proofs in Section 2 and the public standard-form and tracial-representation prerequisites linked below. The theorem is proved relative to the exact foundations stated next.

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. Newly written original expression is dedicated under CC0. Historical sources retain their own terms; no source text or page image is included as a CC0 component. Source and proof revision by GPT-6 Astra (OpenAI), Ultra, October 2026.*

## 1. Foundations and theorem — B1–B3

We use these general von Neumann algebra foundations.

1. Polar decomposition, the bicommutant theorem, bounded ultraweak compactness, spectral calculus, and normal positive functionals separating positive elements. A faithful normal representation preserves the ultrastrong topology on bounded sets. The tracial GNS representation of a faithful normal semifinite trace is faithful and normal, with the bounded elements of finite square norm dense in its Hilbert space.
2. A standard form \(P,\mathcal H,J,\mathcal P\) exists for every von Neumann algebra. Each normal automorphism has a unique canonical unitary implementer preserving this form; these implementers commute with \(J\), and their uniqueness makes the implementers of an action a representation. Also \(JPJ=P'\). A faithful normal state gives the corresponding cyclic, separating standard representation.
3. Projection comparison after a central split, the projection Cantor–Bernstein theorem, the finite/properly infinite central decomposition, and recursive splitting of a properly infinite projection into countably many orthogonal copies of itself. For a projection \(h\) of central support \(c\), the map \(z\mapsto hz\) identifies \(Z(P)c\) with \(Z(hPh)\). Orthogonal families of partial isometries with orthogonal initial and final projections have bounded strong sums.
4. Every finite von Neumann algebra \(R\) has a unique normalized faithful normal center-valued trace \(T_R:R\to Z(R)\). It is tracial and a center-module map. A countably decomposable finite algebra has a faithful normal tracial state. No scalar trace state on an arbitrary finite algebra is assumed.

Section 2 proves the projection prerequisites locally: NP1–NP6 cover orthogonal sums, central support and comparison, Cantor–Bernstein, the finite/properly infinite central split, properly infinite splitting and finite joins; its full-corner-center proof gives the required center identification. The finite-join result NP6 supplies stability of finiteness under finite orthogonal sums and the matrix amplification used in Section 10. For finite groups, the crossed-product coefficient and relative-commutant arguments are proved directly in Section 3.

For standard form, [Haagerup, *The standard form of von Neumann algebras*](https://journals.msp.org/mscand/article/view/2067) gives existence in Theorem 1.6, printed page 275 / PDF page 5; uniqueness and the unrestricted increasing-corner construction in Theorem 2.3, statement on printed page 276 / PDF page 6 and proof on printed pages 279–280 / PDF pages 9–10; and canonical automorphism implementation in Theorem 3.2, printed page 281 / PDF page 11. Lemma 2.10, printed pages 278–279 / PDF pages 8–9, supplies the unique natural-cone vector representing a normal positive functional. The canonical-coordinate part of Proposition 3.7, printed page 282 / PDF page 12, supplies the invariant faithful-state representation used in Section 7. These proofs have arbitrary von Neumann algebra scope. The [primary PDF](https://journals.msp.org/mscand/article/download/2067/2066/2098) is publicly readable; its earlier modular-theory and natural-cone prerequisites retain their stated source scope.

The local prerequisite [Bounded topology and tracial representations](bounded-topology-and-tracial-representations.md) proves preservation of bounded ultrastrong topology by faithful normal representations in Theorem 3.1, normal-inclusion transport in Corollary 3.2, and the faithful normal semifinite tracial representation with dense bounded square-integrable vectors in Sections 4–6 and Theorem 6.1. Its Section 7 gives the exact return to the bounded-adjoint and finite-corner argument used in Sections 6 and 7 here. These proofs use arbitrary Hilbert-space cardinality and arbitrary indexing nets; no factor or faithful-state assumption is added. The general finite trace source and its fixed-point proof are specified next. No scalar trace state on an arbitrary finite algebra is assumed.

### 1.1. The general finite trace source

F. J. Yeadon, [*A new proof of the existence of a trace in a finite von Neumann algebra*](https://www.ams.org/journals/bull/1971-77-02/S0002-9904-1971-12708-8/), *Bulletin of the American Mathematical Society* 77 (1971), 257–260, proves existence and uniqueness of the positive normalized center-valued map on an arbitrary finite von Neumann algebra, its normality and center-module property. Unitary-conjugation invariance gives its tracial identity because every element is a linear combination of unitaries.

The unitary-conjugation affine isometries on the nonempty weakly compact convex orbit hull in the predual have a common fixed point. Yeadon obtains this fixed point from the Ryll-Nardzewski theorem. Its exact publicly readable primary proof is [Namioka–Asplund, *A geometric proof of Ryll-Nardzewski’s fixed point theorem*](https://www.ams.org/journals/bull/1967-73-03/S0002-9904-1967-11779-8/S0002-9904-1967-11779-8.pdf#page=2), printed pages 444–445 / PDF pages 2–3. Section 14 writes out the complete Banach-space affine-isometry specialization and verifies this predual action without a separability assumption. It also proves the compact-generator and averaged-map steps used by that specialization; Krein–Milman, Baire category and basic weak compactness remain stated background. Projection comparison and finite cancellation, Akemann's weak-compactness criterion for subsets of the predual, the Krein–Šmulian theorem, the polar decomposition of normal functionals and the earlier predual/normality results are also prerequisites of Yeadon's proof. Akemann's criterion is Theorem II.2 of [C. A. Akemann, *The dual space of an operator algebra*](https://www.ams.org/journals/tran/1967-126-02/S0002-9947-1967-0206732-8/). Dixmier averaging gives a second proof of the uniqueness: [Peterson, Lemma 4.8.1, Theorem 4.8.2 and Corollary 4.8.3](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf#page=74).

### 1.2. Faithfulness and the scalar tracial-state consequence

Here is the faithfulness consequence at that center-valued interface. Let \(R\) be finite and let \(T:R\to Z(R)\) be the positive normal normalized center-module map of Yeadon's theorem. From \(T(u^*Au)=T(A)\), apply the identity to \(A=ux\) to get \(T(xu)=T(ux)\). Linear combinations of unitaries give \(T(xy)=T(yx)\) for all \(x,y\).

Put \(I=\{x\in R:T(x^*x)=0\}\). For every normal positive functional \(\omega\) on the center, \(\omega\circ T\) is normal and positive. Its null left ideal is weak-operator closed: a positive trace-class representation writes the functional as a sum of vector functionals, and the null ideal is the intersection of the conditions that \(x\) annihilate those vectors. This representation is [Peterson, Proposition 4.2.2](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf#page=60), printed/PDF page 60. Normal positive functionals separate the center, so \(I\) is a weak-operator-closed linear left ideal. The estimate \(0\le T((yx)^*(yx))\le\|y\|^2T(x^*x)\) gives left ideal membership; traciality gives \(T(xx^*)=0\) and then \(\begin{gathered}T((xy)^*(xy))=T(xyy^*x^*)\\ \le\|y\|^2T(xx^*)=0\end{gathered}\). Thus \(I\) is two sided. By [Peterson, Lemma 4.3.1](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf#page=61), printed/PDF page 61, \(I=Rz\) for a central projection \(z\). Since \(z\in I\), \(T(z)=0\); normalization on the center gives \(T(z)=z\). Hence \(z=0\) and \(T\) is faithful. This argument uses the normal-functional representation and closed-ideal result, with no monic-projection or type-decomposition assumption. Section 15 proves the support and closed-ideal facts directly from spectral projections, and gives an alternative faithfulness proof avoiding approximate identities and positive trace-class extensions.

If \(R\) is countably decomposable, its center is too. [Peterson, Proposition 4.5.2](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf#page=67), printed/PDF page 67, gives a faithful normal state \(\omega\) on \(Z(R)\), with no separable-predual hypothesis. Then \(\tau=\omega\circ T\) is a normal positive unital tracial functional. If \(\tau(x^*x)=0\), faithfulness of \(\omega\) and \(T\) gives \(x=0\), so it is a faithful normal tracial state. Its central restriction is the specified \(\omega\); uniqueness of the center-valued trace does not assert uniqueness of a scalar trace on a nonfactor.

### 1.3. The free-action theorem — B1–B3

A normal automorphism \(\sigma\) of \(P\ne0\) is **free** if

\[
c x=\sigma(x)c\quad(x\in P)\quad\Longrightarrow\quad c=0.
\tag{B1}
\]

Equivalently, \(x c=c\sigma(x)\) for all \(x\) forces \(c=0\): take adjoints. An action \(\delta:K\to\operatorname{Aut}(P)\) is free when every \(\delta_s\), \(s\ne e\), is free. This is the intertwiner definition, without a factor assumption.

**Theorem.** Let \(M\ne0\), let \(G\) be finite, and let \(\alpha:G\to\operatorname{Aut}(M)\) be free. Then:

- \(Z(M^\alpha)=Z(M)^\alpha\).
- If \(h\in M^\alpha\) is a finite projection there, it is finite in \(M\). If it is properly infinite in \(M\), it is properly infinite in \(M^\alpha\).
- For every \(u:G\to\mathcal U(M)\) satisfying \(u_{st}=u_s\alpha_s(u_t)\) and \(u_e=1\), there is \(v\in\mathcal U(M)\) with

\[
u_s=v^*\alpha_s(v)\qquad(s\in G).
\tag{B2}
\]

Consequently \(a=v^*\) satisfies \(u_s=a\alpha_s(a^*)\), and \(\beta_s=\operatorname{Ad}(u_s)\alpha_s\) satisfies

\[
\beta_s=\operatorname{Ad}(v^*)\circ\alpha_s\circ\operatorname{Ad}(v).
\tag{B3}
\]

No separability, countable-decomposability, finite-trace, or factor hypothesis is added.

## 2. Projection comparison, splitting and full corners — NP1–NP6

The projection arguments in this section are reproduced from OA-FLOW, *Removing noncentral cocycles from a trace-scaling action*, subsection “Basic projection comparison and support,” together with its full-corner-center proof. The source records the following authorship and terms:

*Written in Codex (OpenAI), September 2026. Self-checked by the writing AI. Any rights held in newly written original expression in this revision are dedicated under CC0; earlier components retain their recorded terms.*

Only the projection arguments are reused here. Their four local result interfaces are:

1. Central comparison, mutual subequivalence, and the finite/properly infinite central split for projections.
2. Splitting a properly infinite projection into two equivalent orthogonal projections, and recursively into countably many copies of itself.
3. Identifying the center of a full corner by compression and extension.
4. Finiteness of a join of two finite projections and of a finite orthogonal sum.

These arguments work in an arbitrary von Neumann algebra \(B\) on an
arbitrary Hilbert space. They use the bicommutant theorem and polar
decomposition, with the bounded spectral calculus already stated among
the analytic foundations.

### 2.1. Joins and orthogonal sums — NP1

The intersection of the ranges of any
family of projections in \(B\) is invariant under all unitaries of \(B'\).
Its orthogonal projection therefore belongs to \(B\) by the bicommutant
theorem. This gives arbitrary meets, and complements give arbitrary joins.
If \((v_i)\) are partial isometries whose initial projections \((a_i)\)
and final projections \((b_i)\) are separately orthogonal, finite sums satisfy

\[
\left\|\sum_{i\in J}v_i\xi\right\|^2
=\sum_{i\in J}\|a_i\xi\|^2\leq\|\xi\|^2.
\tag{NP1}
\]

The tails converge to zero for each vector, over the net of finite
subsets of the index set. The same argument applies to the adjoints.
Thus the sum is a bounded strong-star limit in \(B\), with initial
projection \(\sum_i a_i\) and final projection \(\sum_i b_i\).
No countable index set or basis is required.

### 2.2. Central support detects a bridge

For a projection \(a\), the join
\(c(a)=\bigvee_{u\in\mathcal U(B)}uau^*\) is fixed by every unitary
conjugation, hence is central. It is the least central projection above
\(a\). If \(aBb=\{0\}\), then \(au^*b=0\) for every unitary \(u\), so every
\(uau^*\) is orthogonal to \(b\). Hence \(c(a)b=0\) and
\(c(a)c(b)=0\). The converse follows by moving the orthogonal central
supports through any \(x\in B\). If \(aBb\ne\{0\}\), polar
decomposition of a nonzero \(x=axb\) gives nonzero equivalent
projections below \(a\) and \(b\). This proves the central-support and
partial-isometry bridge rule used in the maximality arguments.

### 2.3. Comparison after a central split — NP2

Choose a maximal family of
partial isometries with separately orthogonal initial projections below
\(a\) and final projections below \(b\), and let \(v\) be their sum.
Put \(a_0=a-v^*v\) and \(b_0=b-vv^*\). A nonzero element of
\(b_0Ba_0\) would, by polar decomposition, add another member.
Thus \(c(a_0)c(b_0)=0\). With \(z=c(b_0)\) we have
\(a_0z=0\) and \(b_0(1-z)=0\), and the partial isometry \(vz\)
and its complementary compression give

\[
\begin{gathered}
az\sim v^*vz\precsim bz,\\
\qquad
b(1-z)\sim vv^*(1-z)\precsim a(1-z).
\end{gathered}
\tag{NP2}
\]

This proves precisely the orientation of the central comparison used
in item 1.

### 2.4. Mutual subequivalence — NP3

Suppose \(a\precsim b\) and \(b\precsim a\).
Replace \(a\) by an equivalent subprojection of \(b\), so \(a\leq b\)
and there is \(w\in bBb\) with \(w^*w=b\) and \(ww^*\leq a\).
Set \(d=b-a\), \(d_n=w^n d(w^*)^n\) for \(n\geq0\), and
\(D=\sum_{n\geq0}d_n\). Since \(dw=0\), these are orthogonal
projections, and \(wDw^*=D-d\). The two summands in
\(u=wD+(b-D)\) have orthogonal initial and final projections. Therefore

\[
\begin{gathered}
u^*u=b,\\
\qquad uu^*=(D-d)+(b-D)=a.
\end{gathered}
\tag{NP3}
\]

Thus \(a\sim b\), including the zero case. This proves the projection
Cantor--Bernstein rule from an actual partial isometry.

### 2.5. The join-difference identity — NP4

The operator \((1-a)b\) has initial
support \(b-(a\wedge b)\) and final support \((a\vee b)-a\):
its kernel on \(b\mathcal H\) is \(a\mathcal H\cap b\mathcal H\),
and its range closes to the part of \((a\vee b)\mathcal H\)
orthogonal to \(a\mathcal H\). Its polar part gives

\[
(a\vee b)-a\sim b-(a\wedge b).
\tag{NP4}
\]

### 2.6. Finite and properly infinite central pieces

A subprojection of a
finite projection is finite: a strict equivalence in the subprojection,
extended by the identity on its orthogonal complement inside the
larger projection, would give a strict equivalence of the larger one.
Finiteness is also preserved by partial-isometry equivalence.
In a corner with unit \(e\), choose a maximal family of orthogonal
central projections \(z_i\) whose corners are finite. Their sum \(z_f\)
is finite. Indeed, an equivalence of \(z_f\) with a subprojection restricts
on each \(z_i\) to equality by finiteness, and the orthogonal sum
then forces equality on \(z_f\). The complementary projection
\(z_\infty=e-z_f\) has no nonzero finite central compression, by
maximality. This is exactly proper infiniteness under the definition
in Takesaki I, V.1.15--1.16. The decomposition is unique: a nonzero
intersection of a finite central piece with a properly infinite
central piece would be both finite and infinite.
Apply this in each projection corner, using the full-corner center
identification proved below, to obtain the ambient central split
of any projection.

Two consequences of comparison are used later at arbitrary cardinality. We give their arguments here; they are Takesaki I, Proposition V.1.34 and Proposition V.1.39.

### 2.7. Filling homogeneous families after central restriction

Work in a corner with unit \(p\). Suppose \((e_i)_{i\in I}\) is an infinite orthogonal family of equivalent projections, each of central support \(p\) in that corner. Extend it by maximality to such a family \((e_j)_{j\in J}\), and put \(q=\sum_{j\in J}e_j\), \(r=p-q\). Central comparison gives a central projection \(z\) with \(rz\precsim e_{j_0}z\) and \(e_{j_0}(p-z)\precsim r(p-z)\). The projection \(z\) cannot be zero: otherwise another copy of \(e_{j_0}\) could be placed in \(r\), contradicting maximality. On this nonzero piece, the infinite family absorbs the residual projection. Map \(rz\) into \(e_{j_0}z\), and map the original family bijectively into the family indexed by \(J\setminus\{j_0\}\). Orthogonal strong sums of the partial isometries give \(pz\precsim qz\). Since \(qz\le pz\), mutual subequivalence gives \(qz\sim pz\). Transporting the family along this equivalence makes it fill \(pz\); its members remain equivalent to \(e_i z\). This transport may move the original members. Applying the argument inside any remaining nonzero central corner and taking a maximal disjoint collection of such corners exhausts \(p\).

### 2.8. Properly infinite splitting — NP5

Work in a corner with properly
infinite unit \(e\). In every nonzero central piece \(z\leq e\),
choose an isometry \(w\) of the corner with \(w^*w=z\) and
\(ww^*<z\). The nonzero projection \(d=z-ww^*\) gives the
infinite orthogonal family \(w^n d(w^*)^n\), \(n\geq0\).
Restrict first to \(c(d)\) so its members have full central support.
The preceding homogeneous-family construction supplies, on a
nonzero central subpiece \(z'\), an infinite homogeneous family
filling \(z'\). Split its index set into two sets of the same
cardinality as the whole set. Matching the equivalent members and
summing their partial isometries gives projections \(r',s'\) with
\(r'+s'=z'\) and \(r'\sim s'\sim z'\).
Choose a maximal orthogonal family of central pieces with this
property. It fills \(e\), because the same construction would work
on any nonzero remainder. Orthogonal sums now give

\[
e=r+s,\qquad r\sim s\sim e.
\tag{NP5}
\]

The two-piece split also gives a countable decomposition that fills the corner. Repeatedly split the remaining copy of \(e\) to obtain orthogonal \(e_n\sim e\), and put \(q=\sum_{n\ge1}e_n\le e\). A remainder may survive this recursion. Since \(e\sim e_1\le q\le e\), Cantor–Bernstein gives \(q\sim e\). Choose \(v\) with \(v^*v=q\) and \(vv^*=e\); the projections \(ve_nv^*\) are orthogonal copies of \(e\) whose sum is \(e\).

This proves the splitting used here, with no state or cardinality bound on the corner. Its two-piece source locator is V.1.36.

### 2.9. Finite joins remain finite — NP6

Let \(a,b\) be finite and put
\(e=a\vee b\). Equation (NP4) makes \(e-a\) equivalent to a
subprojection of \(b\), so \(e-a\) is finite.
If \(e\) were infinite, its finite/properly infinite central
decomposition would have a nonzero properly infinite piece.
Work on that piece with unit \(1\), writing \(1=p+q\) with
both \(p\) and \(q\) finite. Equation (NP5) gives
\(1=r+s\) with \(r\sim s\sim1\).
Central comparison splits the center so that, on one piece,
\(p\wedge r\precsim q\wedge s\), and on the other piece the
reverse subequivalence holds.
On the first piece, (NP4) and orthogonal addition give

\[
\begin{gathered}
r=(p\wedge r)+(r-p\wedge r)
\\
\precsim(q\wedge s)+((p\vee r)-p)\leq q.
\end{gathered}
\tag{NP6}
\]

The last sum is orthogonal: \(q\wedge s\) is orthogonal to both
\(p\) and \(r\), hence to \(p\vee r\), while the other term lies
below \(q=1-p\). On the second central piece, interchange
\((p,r)\) with \((q,s)\) in the same argument to obtain
\(s\precsim p\). A nonzero central compression of either \(r\)
or \(s\) is properly infinite, because each is equivalent to the
properly infinite unit. It cannot be subequivalent to a finite
projection. Both central pieces must therefore be zero, a
contradiction. Consequently \(a\vee b\) is finite, and induction
gives the finite-sum consequence in item 4. This is the
finite-lattice part of V.1.37, printed pages 303--304;
the separate modular-lattice identity is not needed or claimed here.

### 2.10. The center of a full corner

For a projection \(a\) with \(c(a)=1\), compression identifies \(Z(B)\) normally with \(Z(aBa)\). Here is the needed extension argument. Take a maximal orthogonal family \((q_i)\) of projections subequivalent to \(a\), including \(q_0=a\). Full central support and the polar-decomposition argument above make its sum \(1\). Choose \(v_i\) with \(v_i^*v_i\le a\), \(v_iv_i^*=q_i\), and \(v_0=a\). For \(h\in Z(aBa)\) the bounded orthogonal strong sum

\[\widehat h=\sum_i v_i h v_i^*\]

extends \(h\). Its norm is at most \(\|h\|\), because \(h\) commutes with each \(v_i^*v_i\). For \(x\in B\), the element \(v_i^*xv_j\) is in \(aBa\), so it commutes with \(h\). Comparing all \(q_i,q_j\) matrix corners gives \(\widehat h x=x\widehat h\). Thus \(\widehat h\) is central. Conversely, a central element is determined by its compression to \(a\), since \(a\) is full. The extension and compression preserve products, adjoints and bounded increasing positive suprema, as checked in these same corners. They are therefore inverse normal star isomorphisms. In particular, central spectral projections of \(h\) correspond to projections \(az\) with \(z\in Z(B)\).

## 3. Finite Fourier sums can be read as matrices — R1–R5

First take any finite-group action \(\delta:K\to\operatorname{Aut}(P)\), and represent \(P\) faithfully and normally on \(\mathcal H\). On \(\ell^2(K)\otimes\mathcal H\), define

\[
\begin{gathered}
(\pi(x)\xi)(t)=\delta_{t^{-1}}(x)\xi(t),
\\
\qquad (\lambda_s\xi)(t)=\xi(s^{-1}t).
\end{gathered}
\tag{R1}
\]

Then \(\lambda_s\pi(x)\lambda_s^*=\pi(\delta_s(x))\). The finite sums

\[
X=\sum_{s\in K}\pi(x_s)\lambda_s
\tag{R2}
\]

form a unital \(*\)-algebra. Its matrix entry in row \(t\), column \(r\), is \(\delta_{t^{-1}}(x_{tr^{-1}})\). In particular the row \(e\), column \(s^{-1}\) entry is exactly \(x_s\). Thus each coefficient is unique, normal, and contractive as a function of \(X\).

The space of these sums is ultraweakly closed. It is exactly the set of operator matrices whose entries lie in \(P\) and satisfy \(X_{t,r}=\delta_{t^{-1}}(X_{e,rt^{-1}})\) for every \(t,r\). These finitely many linear conditions are ultraweakly closed because the automorphisms and entry maps are normal. Conversely they reconstruct the sum (R2) by setting \(x_s=X_{e,s^{-1}}\). Hence (R2) is the entire von Neumann crossed product \(P\rtimes_\delta K\), with no infinite Fourier convergence issue. Write its coefficient unitaries as \(\lambda_s\) and identify \(P\) with \(\pi(P)\).

The coefficient map \(E_P(X)=x_e\) is a normal unital completely positive map: it is compression to the \(e\)-diagonal entry. It is \(P\)-bimodular and fixes \(P\). For a positive \(X\), all diagonal entries are \(\delta_{t^{-1}}(E_P(X))\). If \(E_P(X)=0\), positivity forces every matrix entry to vanish: the inequality \(\left|\langle X\xi,\eta\rangle\right|^2\le\langle X\xi,\xi\rangle\langle X\eta,\eta\rangle\), first on vectors supported in single coordinates, proves this. Therefore \(E_P\) is faithful.

If \(X\) commutes with \(P\), comparison of the \(s\)-coefficients gives

\[
x x_s=x_s\delta_s(x)\qquad(x\in P).
\tag{R3}
\]

When \(\delta\) is free, (B1), in its adjoint orientation, makes \(x_s=0\) for \(s\ne e\). At \(e\), it makes \(x_e\in Z(P)\). We have proved

\[
\begin{gathered}
P'\cap(P\rtimes_\delta K)=Z(P),\\
\qquad
Z(P\rtimes_\delta K)=Z(P)^\delta.
\end{gathered}
\tag{R4}
\]

For the second equality, an element of the center first belongs to \(Z(P)\) by the first equality; commuting with each \(\lambda_s\) is exactly invariance under \(\delta_s\).

Suppose \(\rho:P\to B(\mathcal L)\) is a normal unital \(*\)-representation and \(V\) is a unitary representation with \(V_s\rho(x)V_s^*=\rho(\delta_s(x))\). The formula

\[
\Theta(X)=\sum_{s\in K}\rho(x_s)V_s
\tag{R5}
\]

defines a bounded normal map: \(\|\Theta(X)\|\le|K|\|X\|\) follows from the coefficient bounds. The finite sum and covariance check multiplication and adjoints, so \(\Theta\) is a normal unital \(*\)-homomorphism. Its kernel is an ultraweakly closed two-sided ideal, hence has the form \((P\rtimes K)z\) for a central projection \(z\). To see the ideal statement directly, spectral cuts away from zero of \(|x|\), for \(x\) in the ideal, also belong to the ideal. Their finite joins and then their supremum belong to it by ultraweak closedness. This supremum \(z\) is invariant under every unitary conjugation, so is central, and is the support unit of the ideal. Removing that central kernel makes the representation faithful and isometric. Its unit-ball image is ultraweakly compact; Kaplansky density therefore makes its range precisely \((\rho(P)\cup V(K))''\). If \(\delta\) is free and \(\rho\) is faithful, (R4) gives \(z\in Z(P)\), and \(\Theta(z)=\rho(z)=0\) forces \(z=0\).

This proves the finite-group integrated representation and its faithfulness before they are used in a standard representation. It does not invoke a universal normal representation assertion without checking it.

## 4. Put the cocycle in an actual linking algebra — M1–M3

For the theorem's cocycle put

\[
\begin{gathered}
A=M\overline\otimes M_2(\mathbb C),\\
\quad
d_s=\begin{pmatrix}1&0\\0&u_s\end{pmatrix},\\
\quad
\gamma_s=\operatorname{Ad}(d_s)(\alpha_s\otimes\operatorname{id}),
\\
\quad F=A^\gamma.
\end{gathered}
\tag{M1}
\]

The cocycle equation gives \(d_{st}=d_s(\alpha_s\otimes\operatorname{id})(d_t)\). Therefore \(\gamma_s\gamma_t=\gamma_{st}\). Both \(p=1\otimes e_{11}\) and \(q=1\otimes e_{22}\) are fixed.

A partial isometry \(w\in pFq\) with \(ww^*=p\) and \(w^*w=q\) has sole nonzero matrix entry \(w_{12}=v\), where \(vv^*=v^*v=1\). On that entry,

\[
\gamma_s(w)_{12}=\alpha_s(v)u_s^*.
\tag{M2}
\]

Thus fixedness is \(\alpha_s(v)u_s^*=v\), equivalently \(u_s=v^*\alpha_s(v)\). We must obtain equivalence in \(F\), not just the evident ambient equivalence through \(1\otimes e_{12}\).

Freeness of \(\gamma\) also follows by entries. If \(s\ne e\) and \(C X=\gamma_s(X)C\) for all \(X\in A\), set \(D=d_s^*C\). Then

\[
D X=(\alpha_s\otimes\operatorname{id})(X)D.
\tag{M3}
\]

For \(X=1\otimes b\), \(D\) commutes with every scalar matrix. Commutation with \(e_{11},e_{22}\) first makes the off-diagonal entries zero; commutation with \(e_{12}\) makes the diagonal entries equal. Hence \(D=c\otimes1_2\). Taking \(X=x\otimes e_{11}\) gives \(cx=\alpha_s(x)c\). By freeness, \(c=0\), so \(C=0\). This proves freeness of the specified matrix cocycle action, with no condition on \(Z(M)\).

## 5. The standard commutant action gives the exact fixed center — C1–C4

This argument applies to any free finite action \(\delta\) on \(P\). Represent \(P\) in standard form, and let \(U_s\) be its canonical implementers. They form a representation and commute with \(J\). The action \(\delta'_s=\operatorname{Ad}(U_s)|_{P'}\) is free as well.

Here is the product-order check. The map \(\kappa:P'\to P\), \(\kappa(b)=Jb^*J\), is a linear \(*\)-anti-isomorphism, and \(\kappa\delta'_s=\delta_s\kappa\). If \(bY=\delta'_s(Y)b\) for all \(Y\in P'\), put \(c=\kappa(b)\). Applying \(\kappa\) reverses the products and gives

\[
\begin{gathered}
Xc=c\delta_s(X),\\
\qquad c^*X=\delta_s(X)c^*
\quad(X\in P).
\end{gathered}
\tag{C1}
\]

Freeness of \(\delta_s\) forces \(c^*=0\), hence \(b=0\).

Let \(B=P^\delta\). In this actual Hilbert space,

\[
\begin{gathered}
B=P\cap U(K)'=(P'\cup U(K))',\\
\qquad
B'=(P'\cup U(K))''.
\end{gathered}
\tag{C2}
\]

The representation (R5) for \(P'\rtimes_{\delta'}K\) is faithful. Apply (R4) to its coefficient algebra \(P'\). Because \((P')'=P\) and \(Z(P')=Z(P)\) in this representation, it gives

\[
B'\cap P=Z(P).
\tag{C3}
\]

Intersect with \(B\):

\[
Z(B)=B\cap B'=Z(P)^\delta.
\tag{C4}
\]

Applied to \(P=A\), this is \(Z(F)=Z(A)^\gamma\). Every ambient central projection annihilating \(p\) or \(q\) is zero, since \(Z(A)=Z(M)\otimes1_2\). Equation (C4) therefore makes both diagonal projections full in \(F\) as well.

## 6. The two bounded-adjoint tests used in finiteness transfer — L1–L2

These are the local replacements for the two topology consequences used in the transfer proof. Let \(R\) carry a faithful normal semifinite trace \(\rho\), let \(a\in R\) with \(\rho(a^*a)<\infty\), and let the bounded net \(x_i\) tend ultrastrongly to zero. In the tracial GNS space, \(a^*\) is a square-integrable vector. Traciality gives

\[
\begin{gathered}
\|a x_i^*\|_{2,\rho}=\|x_i a^*\|_{2,\rho}\longrightarrow0,
\\
\qquad
\|(a x_i^*)b\|_{2,\rho}\le\|b\|\,\|a x_i^*\|_{2,\rho}.
\end{gathered}
\tag{L1}
\]

For the second bound, move \(bb^*\) inside the trace and use \(bb^*\le\|b\|^21\). Apply it to bounded square-integrable \(b\). Those vectors are dense, and \(\|a x_i^*\|\) is uniformly bounded. Hence left multiplication by \(a x_i^*\) tends strongly to zero on the whole GNS space. Its faithful normal representation transports bounded ultrastrong convergence, so \(a x_i^*\to0\) ultrastrongly in \(R\). The local topology prerequisite proves these representation and density facts in full in Sections 3–7.

Conversely, an infinite projection \(h\) admits \(w\in hRh\) with \(w^*w=h\), \(ww^*<h\). Set \(d=h-ww^*\ne0\), and, for \(n\ge1\), put

\[
\begin{gathered}
d_n=w^n d(w^*)^n,\qquad y_n=d(w^*)^n.
\\
\quad y_n^*y_n=d_n,\quad y_ny_n^*=d.
\end{gathered}
\tag{L2}
\]

The \(d_n\) are orthogonal: \(dw=0\), so any product with different exponents vanishes after cancellation. Every normal positive functional takes summable values on them. Thus \(y_n\to0\) ultrastrongly, while a normal positive functional nonzero on \(d\) shows \(y_n^*\not\to0\) ultrastrongly. Bounded ultrastrong continuity of the adjoint therefore forces finiteness. This is precisely (T18b), proved by an actual sequence in an infinite corner.

## 7. A finite fixed algebra forces a finite ambient algebra — F1–F7

For a free finite action \(\delta\) on \(P\), set \(B=P^\delta\), \(n=|K|\), and

\[
E(x)=\frac1n\sum_{s\in K}\delta_s(x).
\tag{F1}
\]

This is a normal unital completely positive \(B\)-bimodular expectation, and is faithful since \(E(x)\ge x/n\) for \(x\ge0\). In fact \(nE-\operatorname{id}=\sum_{s\ne e}\delta_s\) is completely positive at every matrix level. No conclusion about complete positivity is inferred merely from an order inequality.

Suppose first that \(B\) is finite and countably decomposable. Choose a faithful normal tracial state \(\tau\) on \(B\). Then \(\varphi=\tau\circ E\) is a faithful normal state on \(P\). In its standard representation the canonical implementers \(U_s\) fix \(\Omega_\varphi\). Indeed \(\varphi\) is invariant, and the unitary \(x\Omega_\varphi\mapsto\delta_s(x)\Omega_\varphi\) is its canonical implementer.

By (R5) and freeness,

\[
\begin{gathered}
Q=(P\cup U(K))''\cong P\rtimes_\delta K,\\
\qquad
e_B=\frac1n\sum_s U_s,\qquad \Phi=nE_P.
\end{gathered}
\tag{F2}
\]

The averaging operator \(e_B\) is the orthogonal projection onto invariant vectors. On the dense set \(P\Omega_\varphi\), it sends \(x\Omega_\varphi\) to \(E(x)\Omega_\varphi\), so its range is \(\overline{B\Omega_\varphi}\). Direct coefficient calculations give

\[
\begin{gathered}
e_Bxe_B=E(x)e_B,\quad e_B U_s=U_se_B=e_B,
\\
\quad e_BQe_B=Be_B\cong B,
\quad \Phi(xe_By)=xy,
\\
\quad\Phi(1)=n1.
\end{gathered}
\tag{F3}
\]

The corner identification is faithful: \(be_B=0\) implies \(b\Omega_\varphi=0\), hence \(b=0\). It is normal, and every element of the corner is such a \(be_B\) because the Fourier sum has finitely many terms. Moreover \(e_B\) is full in \(Q\). If \(z\in Z(Q)\) annihilates it, (R4) puts \(z\in Z(P)^\delta\), and \(E_P(ze_B)=z/n\) makes \(z=0\).

For completeness, construct the needed trace on \(Q\) from that full finite corner. Choose partial isometries \(v_i\) with initial projections at most \(e_B\), orthogonal final projections summing to \(1\), and one member \(v_0=e_B\). Such a family exists by maximality: if its range sum has nonzero complement \(k\), fullness gives \(kQe_B\ne0\); the polar part of a nonzero element adds a member. On positive \(x\), set

\[
\operatorname{Tr}(x)=\sum_i\tau(v_i^*xv_i),
\tag{F4}
\]

where \(\tau\) is read through \(e_BQe_B\cong B\), and a positive sum over an arbitrary index set is the supremum of finite subsums. This weight is normal and faithful. Inserting \(\sum_jv_jv_j^*=1\) yields

\[
\begin{gathered}
\operatorname{Tr}(x^*x)
=\sum_{i,j}\tau((v_j^*xv_i)^*(v_j^*xv_i))
\\
=\sum_{i,j}\tau((v_j^*xv_i)(v_j^*xv_i)^*)
=\operatorname{Tr}(xx^*).
\end{gathered}
\tag{F5}
\]

All summands lie in the finite corner; positivity permits interchanging the sums. Finite sums \(h\) of final projections have \(\operatorname{Tr}(h)\le\#\{i\text{ used}\}\). For bounded \(x\ge0\), the elements \(x^{1/2}h x^{1/2}\) increase strongly to \(x\) and have trace at most \(\|x\|\operatorname{Tr}(h)\), by traciality. This proves semifiniteness. The distinguished member and orthogonality give \(\operatorname{Tr}(e_B)=\tau(e_B)=1\).

Let a bounded net \(x_i\in P\) tend ultrastrongly to zero. The inclusion in \(Q\) is normal, so it has the same convergence in the normal representation of \(Q\). Apply (L1) to \(a=e_B\). Then \(e_Bx_i^*\to0\) ultrastrongly and \(x_i e_Bx_i^*\to0\) ultraweakly. Since \(\Phi/n=E_P\) is unital completely positive, its Schwarz inequality gives

\[
\begin{gathered}
x_i x_i^*
=\Phi(e_Bx_i^*)^*\Phi(e_Bx_i^*)
\\
\le n\Phi(x_i e_Bx_i^*)\longrightarrow0
\quad\hbox{ultraweakly}.
\end{gathered}
\tag{F6}
\]

Here \(\Phi(e_Bx_i^*)=x_i^*\) comes from (F3). Normality of \(\Phi\), followed by testing positive normal functionals, justifies the last implication. It says \(x_i^*\to0\) ultrastrongly. The explicit obstruction (L2) makes \(P\) finite.

Now let \(B\) be an arbitrary finite algebra. Split \(Z(B)\) into orthogonal central projections \(z_a\) such that each \(Bz_a\) has a faithful normal tracial state. To obtain this split, take supports of nonzero normal positive functionals on every remaining central corner, compose their restrictions with its center-valued trace, and use maximality. Normal positive functionals separate the center, so the sum fills \(1\). By (C4), each \(z_a\) is also central in \(P\) and \(\delta\)-invariant. The action on \(Pz_a\) is free: an intertwiner there extends by zero to one in \(P\). The preceding proof makes every \(Pz_a\) finite. Their central direct sum is finite, since an isometry is unitary after compression by every \(z_a\). Thus

\[
P^\delta\text{ finite}\quad\Longrightarrow\quad P\text{ finite}.
\tag{F7}
\]

This is an explicitly proved specialization and central extension of the mechanism in [Jolissaint, Theorem 1.6(1), printed pages 227–228](https://doi.org/10.7146/math.scand.a-12359). His source setup is countably decomposable. We use its trace/Schwarz mechanism, give the concrete finite crossed-product map (F3), prove the two bounded-adjoint facts locally, and use (C4) for the unrestricted assembly. That article alone is not cited as a proof of the full fixed-center or coboundary theorem.

## 8. Freeness and finiteness pass to the needed invariant corners — I1–I2

Let \(h\in B=P^\delta\) be a projection, and let \(c\) be its central support in \(P\). Invariance of \(h\) makes \(c\) invariant. Equation (C4) therefore puts \(c\in Z(B)\). Its central support in \(B\) is also \(c\): every \(B\)-central projection is \(P\)-central, and the two minimal-support tests coincide.

The action on \(hPh\) is free. For \(s\ne e\), suppose \(b x=\delta_s(x)b\) for \(x\in hPh\). Choose partial isometries \(w_j\) with initial projections \(\le h\), orthogonal final projections filling \(c\), and \(w_0=h\), as in the fullness construction above. The sum

\[
C=\sum_j\delta_s(w_j)b w_j^*
\tag{I1}
\]

is bounded and converges strongly: its terms have orthogonal initial containing projections \(w_jw_j^*\) and orthogonal final containing projections \(\delta_s(w_jw_j^*)\), with norm at most \(\|b\|\). To check \(Cy=\delta_s(y)C\), insert \(\sum_jw_jw_j^*=c\) on both sides and use \(w_i^*yw_j\in hPh\):

\[
b(w_i^*yw_j)=\delta_s(w_i^*yw_j)b.
\tag{I2}
\]

The resulting matrix entries agree, so the two bounded operators agree on the central corner \(Pc\), and both vanish on its complement. Freeness on \(P\) gives \(C=0\); its \(h,h\)-entry is \(b\), so \(b=0\).

If \(h\) is finite in \(B\), then \(hBh=(hPh)^\delta\) is finite. Apply (F7) to the restricted free action to see that \(hPh\) is finite. Hence \(h\) is finite in \(P\).

If \(h\) is properly infinite in \(P\) but fails to be properly infinite in \(B\), the finite/properly infinite central decomposition of \(hBh\) has a nonzero finite part. The full-corner center identification writes its unit as \(hz\) for a nonzero \(z\in Z(B)c\subseteq Z(P)c\). The preceding result makes \(hz\) finite in \(P\), contradicting proper infiniteness of \(h\). We have proved exactly the invariant-corner transfer needed by OA-CLASSIFY.

## 9. A faithful expectation controls arbitrary cardinal size — K1–K4

We need one comparison lemma beyond the countably decomposable case.

**Lemma.** Suppose \(B\subseteq P\) has a faithful normal expectation and \(Z(B)\subseteq Z(P)\). If properly infinite \(r,t\in B\) have the same \(B\)-central support and \(r\sim_Pt\), then \(r\sim_Bt\).

A projection \(f\in B\) is countably decomposable in \(B\) exactly when it is countably decomposable in \(P\). A faithful normal state on \(fBf\), composed with the compressed expectation, is faithful and normal on \(fPf\); the reverse implication is restriction.

First, in a countably decomposable algebra \(R\), every full properly infinite projection \(r\) is equivalent to \(1\). Split \(r\) into countably many orthogonal copies \(r_n\) of itself. Choose a maximal orthogonal family \(k_j\) of nonzero projections subequivalent to \(r\). Its sum is \(1\), since a nonzero remainder \(k\) has \(kRr\ne0\), and polar decomposition would add a member. A faithful normal state makes this family countable. Matching its members into distinct \(r_n\) gives

\[
1=\sum_jk_j\precsim r\le1,
\tag{K1}
\]

and Cantor–Bernstein gives \(r\sim1\).

We also need a local homogeneous-family construction. Take a nonzero countably decomposable projection \(f\) in a corner \(R\), restrict to its central support \(c\), and extend a prescribed family of orthogonal copies of \(f\) to a maximal one \(g_i\), \(i\in I\). Set \(h=\sum_i g_i\), \(d=c-h\). Central comparison gives a central split on which \(dz\precsim fz\) or \(f(c-z)\precsim d(c-z)\). The first piece can be chosen nonzero: otherwise \(f\precsim d\) would add a copy to the maximal family. All \(g_i z\) are nonzero, because \(f\) has central support \(c\).

If \(I\) is infinite, choose \(i_0\in I\) and match \(I\) bijectively to \(I\setminus\{i_0\}\). This makes \(hz\) equivalent to \(\sum_{i\ne i_0}g_i z\); its complement slot receives \(dz\precsim g_{i_0}z\). Thus

\[
z=dz+hz\precsim hz\precsim z.
\tag{K2}
\]

An equivalence \(z\sim hz\) transfers the entire homogeneous family to one filling \(z\). A prescribed subfamily survives up to equivalence of its sum. If \(I\) is finite or countable, \(z\) is countably decomposable: the residual \(dz\) is subequivalent to the small \(fz\), and normal faithful states on the countably many corners combine with positive summable coefficients. Therefore, if the unit has no nonzero countably decomposable central compression, the index set in this construction must be uncountable, and (K2) removes the residual.

Now prove the lemma. Central comparison in \(B\) reduces it, on each of two central pieces, to \(r\le t\), by interchanging the projections on one piece and replacing the smaller by an equivalent subprojection. Work in \(tBt\). All central compressions used here correspond, through its full-corner center, to projections of \(Z(B)\), and therefore of \(Z(P)\). The ambient equivalence persists after every such compression.

On a central piece where \(r\) is countably decomposable, ambient equivalence makes \(t\) countably decomposable in \(P\), and the expectation makes it countably decomposable in \(B\). Then (K1) compares the two full properly infinite projections.

On a central piece where no nonzero central compression of \(r\) is countably decomposable, take a nonzero countably decomposable \(f\le r\). Such a projection exists: the support of a nonzero normal positive functional in \(rBr\) has a faithful restriction. Apply (K2) in \(rBr\). On a smaller nonzero central piece, it gives an uncountable homogeneous family \(g_j\), \(j\in J\), of countably decomposable projections filling \(r\). Extend that family to a maximal family in \(tBt\), and apply (K2) once more. After a further central compression \(z\ne0\), the transferred family \(f_i\), \(i\in I\), satisfies

\[
\sum_{i\in I}f_i=tz,\qquad
\sum_{j\in J}f_j\sim_Brz,\qquad J\subseteq I.
\tag{K3}
\]

The second formula is equivalence because the residual-absorption equivalence can move the original subfamily. Every member remains countably decomposable; compressing by a nonzero central piece does not remove any member, since each has full central support in the current corner.

Ambient equivalence transports the \(J\)-family to a countably decomposable orthogonal family \(h_j\) filling \(tz\) in \(P\). Choose a faithful normal state on each \(h_jPh_j\), and extend it to \(tzPtz\) by compression; denote it by \(\psi_j\). Each \(\psi_j\) is nonzero on at most countably many of the orthogonal \(f_i\): for every positive integer \(m\), only finitely many can have value at least \(1/m\). Their union over \(m\) contains all positive values. These states jointly detect every nonzero \(f_i\). Indeed, if \(\psi_j(f_i)=0\) for every \(j\), faithfulness gives \(h_jf_i h_j=0\), hence \(f_i h_j=0\) for every \(j\), and \(\sum_jh_j=tz\) would give \(f_i=0\). Consequently

\[
|I|\le\aleph_0|J|=|J|,
\tag{K4}
\]

because \(J\) is uncountable. The inclusion \(J\subseteq I\) gives equality. A bijection between the homogeneous filling families, followed by the strong sum of their partial isometries, proves \(rz\sim_Btz\).

Every nonzero central remainder either has a nonzero piece with countably decomposable \(r\), or has a piece of the second kind. We have found an equivalence on a nonzero subpiece of each remainder. A maximal orthogonal family of such central pieces fills the common central support. Its bounded strong sum gives \(r\sim_Bt\) globally. This proves the lemma without a global countable hypothesis.

## 10. Finish both central types of the linking algebra — D1–D4

Let \(z_\infty\) be the maximal properly infinite central summand of \(A\), and put \(z_f=1-z_\infty\). Their defining properties are preserved by automorphisms, so they are \(\gamma\)-fixed and belong to \(Z(F)\) by (C4).

In \(Az_\infty\), both diagonal corners are isomorphic to \(Mz_\infty\), and \(pz_\infty,qz_\infty\) are properly infinite, full, and ambient-equivalent. Invariant-corner transfer makes them properly infinite in \(Fz_\infty\). Averaging is a faithful normal expectation, and (C4) gives the required center inclusion. The comparison lemma therefore gives

\[
pz_\infty\sim_{Fz_\infty}qz_\infty.
\tag{D1}
\]

The finite algebra \(Az_f\) has normalized center-valued trace \(T\). Its automorphism naturality follows from uniqueness: \(\gamma_s^{-1}\circ T\circ\gamma_s\) is another normalized faithful normal center-valued trace. Hence

\[
T(\gamma_s(x))=\gamma_s(T(x)).
\tag{D2}
\]

For \(x\in Fz_f\), (D2) makes \(T(x)\) fixed, so \(T(Fz_f)\subseteq Z(F)z_f\). Traciality gives \(T(pz_f)=T(qz_f)\), using the ambient partial isometry \(e_{12}z_f\); their sum is \(z_f\), so both values are \(z_f/2\).

We can derive the needed finite comparison directly, without adding a trace-comparison black box. Central comparison in \(Fz_f\) gives a split on which one diagonal projection is subequivalent to the other. On a piece \(z\) where \(pz\precsim qz\), take \(w^*w=pz\), \(ww^*=q'\le qz\). Traciality and the center-module property give

\[
T(qz-q')=T(qz)-T(pz)=0.
\tag{D3}
\]

Faithfulness forces \(q'=qz\), so these projections are equivalent. The other piece is identical with the roles reversed. Sum the resulting partial isometries to obtain \(pz_f\sim_{Fz_f}qz_f\). This argument works for finite nonfactors and an arbitrary center; no finite total scalar trace is used.

Choose the orientation of the partial isometries in (D1) and in the finite part so that their initial projections are \(qz_\infty,qz_f\) and their final projections are \(pz_\infty,pz_f\). Their sum belongs to \(pFq\), with initial projection \(q\) and final projection \(p\). Formula (M2) gives the single unitary \(v\) in (B2). Finally

\[
u_s\alpha_s(x)u_s^*
=v^*\alpha_s(vxv^*)v,
\tag{D4}
\]

which is exactly (B3). All parts of the theorem are proved relative to the declared general foundations.

## 11. The exact OA-CLASSIFY specializations

For a factor \(P\), (C4) makes \(P^\delta\) a factor. If \(P\) is countably decomposable, restricting a faithful normal state to the fixed algebra makes it countably decomposable too. Every infinite projection in a factor is properly infinite, and (K1) then makes any two nonzero infinite projections in this fixed factor equivalent.

In the finite-factor case, an ambient normalized trace is invariant under automorphisms by uniqueness and restricts to the fixed factor's normalized trace. Thus fixed projections of equal ambient trace are equivalent inside the fixed factor, by the comparison proof (D3).

The Weyl-pair consumer assumes a strongly stable factor with separable predual, \(\theta^p=\mathrm{id}\), and outer period \(p\). Its nonidentity cyclic powers are outer, which in a factor is exactly freeness in (B1): a nonzero intertwiner has polar part implementing the automorphism because its two absolute values are central. Applied to its cyclic tensor-absorption model, (C4) supplies the fixed factor and the invariant-corner section supplies transfer of finite fixed projections. Therefore the consumer's nonzero spectral projections of equal finite trace are equivalent in the finite case; in its type \(\mathrm{II}_\infty\) or type \(\mathrm{III}\) cases, the stated ambient infiniteness and transfer make them infinite in the countably decomposable fixed factor, where (K1) compares them. This does not change the consumer's assumptions or Weyl phase \(\lambda=e^{2\pi i/p}\).

The general coboundary assertion inherited through exact-implementer prerequisites remains (B2), with arbitrary nonfactor and arbitrary-cardinal scope. The consumer's separable-factor specialization is not substituted for that general assertion.

## 12. Exercises with complete solutions

**Exercise 12.1. Check the opposite cocycle orientation.** If \(w\in pFq\) has entry \(v\), show why fixedness gives \(u_s=v^*\alpha_s(v)\), rather than \(v\alpha_s(v^*)\).

*Solution.* Matrix multiplication in (M1) gives \(\gamma_s(w)_{12}=\alpha_s(v)u_s^*\). Equate it to \(v\), multiply on the right by \(u_s\), and then on the left by \(v^*\). This gives \(u_s=v^*\alpha_s(v)\). Setting \(a=v^*\) converts it to \(a\alpha_s(a^*)\); the two letters must not be identified. The entry of \(w^*\in qFp\) is \(v^*\), and carries the reversed corner orientation.

**Exercise 12.2. Find the crossed-product coefficient.** In (R1)–(R2), which matrix entry is \(x_s\), and what coefficient equation expresses commutation with \(P\)?

*Solution.* The row \(e\), column \(s^{-1}\) entry is \(x_s\), since \(e=s(s^{-1})\). The products \(xX\) and \(Xx\) have respective \(s\)-coefficients \(xx_s\) and \(x_s\delta_s(x)\). Equality is (R3), the adjoint form of freeness. Its adjoint gives a genuine identity-to-automorphism intertwiner, so all nonidentity coefficients vanish.

**Exercise 12.3. Justify the commutant action.** Explain why \(\kappa(b)=Jb^*J\) reverses the intertwiner equation rather than preserving its product order.

*Solution.* The adjoint reverses order, while the two conjugations by the antilinear \(J\) together make the map linear: \(\kappa(bY)=\kappa(Y)\kappa(b)\). Since canonical implementers commute with \(J\), \(\kappa(\delta'_s(Y))=\delta_s(\kappa(Y))\). The image equation is \(Xc=c\delta_s(X)\); taking adjoints and replacing \(X^*\) by \(X\) gives \(c^*X=\delta_s(X)c^*\), to which (B1) applies.

**Exercise 12.4. Why is finite central assembly legitimate?** Let \(B=P^\delta\) be finite but have no faithful normal state. Show why a central decomposition into state-bearing finite pieces can be used in \(P\).

*Solution.* Supports of normal positive functionals on \(Z(B)\), followed by its normalized center-valued trace, produce faithful normal tracial states on their supported central pieces. A maximal orthogonal family fills \(1\), since normal functionals detect every remaining nonzero central projection. Equation (C4) puts each piece in \(Z(P)^\delta\). Thus each is an ambient invariant central projection, the action restricts freely, and (F7)'s countable case applies. Central summation then proves ambient finiteness. No nonexistent global trace state is chosen.

**Exercise 12.5. Show why cardinality is indispensable.** Let \(I\) be uncountable. Compare the identity in \(B(\ell^2(I))\) with the projection onto a separable infinite-dimensional subspace.

*Solution.* Both are properly infinite and have central support one, since the ambient algebra is a factor. Equivalence would give a unitary isomorphism between their ranges, contradicting their different Hilbert dimensions. To test the comparison lemma, take \(B=P=B(\ell^2(I))\), let the expectation be the identity, and let \(r\) be the separable-range projection and \(t=1\). Both projections belong to the same unital inclusion and satisfy the other hypotheses. The missing hypothesis is precisely \(r\sim_Pt\); removing it would give the false conclusion \(r\sim_Bt\). In (K3)–(K4), the expectation preserves countably decomposable projections and ambient equivalence supplies the filling family whose cardinality detects the difference.

**Exercise 12.6. A free nonfactor model.** Let \(P=\prod_{t\in K}R\), let \(\delta_s(x)(t)=x(s^{-1}t)\), and let \(u\) be a cocycle for this action. Prove freeness and give \(v\) explicitly.

*Solution.* Central projections of the individual coordinates are moved by every \(s\ne e\). If \(cx=\delta_s(x)c\), choosing a coordinate central projection makes the \(t\)-coordinate of \(c\) zero; varying \(t\) gives \(c=0\). Put \(v(t)=u_t(t)^*\). The cocycle equation at \(t=s(s^{-1}t)\), evaluated in coordinate \(t\), gives \(u_t(t)=u_s(t)u_{s^{-1}t}(s^{-1}t)\). Rearranging gives \(u_s(t)=v(t)^*v(s^{-1}t)=v(t)^*\delta_s(v)(t)\). This finite product model verifies the sign without a factor or trace assumption.

**Exercise 12.7. Freeness is a real hypothesis.** Give a finite-group action with a unitary cocycle that is not a coboundary.

*Solution.* Let \(G=C_2\) act trivially on \(\mathbb C\), and set \(u_e=1\), \(u_s=-1\) for its nonidentity element. This is a unitary cocycle, since \(u_s^2=1\). Every expression \(v^*\alpha_s(v)\) equals \(1\), so this cocycle cannot be a coboundary. The action fails (B1), since every nonzero scalar intertwines the identity with itself.

## 13. Sources and prerequisite roles

Masamichi Takesaki, *Theory of Operator Algebras II*, Encyclopaedia of Mathematical Sciences 125, Springer, 2003, Proposition XI.2.26, printed pages 347–348 ([publisher record](https://doi.org/10.1007/978-3-662-10451-4)), records the standard finite free-action theorem. It remains scholarly credit for the theorem and the earlier construction consultation. That proof explicitly assumes countable decomposability to avoid cardinal arguments and leaves the general extension to the reader; Section 9 supplies the required extension here. The finite regular-matrix coefficient argument, invariant-corner extension, trace-naturality comparison and cardinal detection are proved here, with their exact orientations retained. The general projection arguments in Section 2 are reused from the CC0 OA-FLOW lesson credited there. Their locators in Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979, first-edition reprint ([publisher record](https://doi.org/10.1007/978-1-4612-6188-9)), are V.1.1–1.8; the projection part of V.1.19; V.1.34; V.1.36; V.1.37's finite-lattice part; and V.1.39. The proofs included here establish the consumed projection results without adding the unrelated weight-theory prerequisites of that source lesson.

Further exact locators in that 1979 edition are Lemmas V.2.27–2.28 for the bounded-adjoint mechanism in Section 6, and Lemma V.3.17 for the normal-state cardinal detection in (K4). The proof of (L1) retains the classical square-norm argument after the local tracial representation has been constructed. The proof of (L2) uses an explicit isometry-defect sequence. Section 9 combines homogeneous-family filling, the faithful expectation and this cardinal detection to obtain its stated comparison lemma.

Uffe Haagerup, [*The standard form of von Neumann algebras*](https://journals.msp.org/mscand/article/view/2067), *Mathematica Scandinavica* 37 (1975), 271–283, DOI [10.7146/math.scand.a-11606](https://doi.org/10.7146/math.scand.a-11606), is the public primary source for the standard-form prerequisite. The exact existence, uniqueness, canonical implementation and state-vector proof locations are given in Section 1. Its proofs use basic Tomita–Takesaki representation theory and earlier natural-cone results, whose source roles remain explicit. The automorphism-topology conclusions elsewhere in that paper are not needed for a finite-group action.

F. J. Yeadon, [*A new proof of the existence of a trace in a finite von Neumann algebra*](https://www.ams.org/journals/bull/1971-77-02/S0002-9904-1971-12708-8/), *Bulletin of the American Mathematical Society* 77 (1971), 257–260, gives the general finite center-valued existence, uniqueness, normality and center-module proof. Its weak-compactness lemma uses Theorem II.2 of C. A. Akemann, [*The dual space of an operator algebra*](https://www.ams.org/journals/tran/1967-126-02/S0002-9947-1967-0206732-8/), *Transactions of the American Mathematical Society* 126 (1967), 286–302. Jesse Peterson, [*Notes on von Neumann algebras*](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf), April 5, 2013, supplies the normal positive-functional, closed-ideal and faithful-state interfaces used in Section 1.2. The faithfulness and scalar trace deductions are written there explicitly. The fixed-point proof and the other prerequisites of Yeadon's proof are identified in Section 1.1.

Paul Jolissaint, [*Indice d'espérances conditionnelles et algèbres de von Neumann finies*](https://doi.org/10.7146/math.scand.a-12359), *Mathematica Scandinavica* 68 (1991), 221–246, Theorem 1.6(1) supplies the finite-corner trace and Schwarz-transfer mechanism used in Section 7. Its source setup is countably decomposable. The fixed-center argument and central assembly written here supply the unrestricted scope; the article alone is not a source for the entire coboundary theorem.

The bounded representation transport and semifinite tracial representation are proved in the local [Bounded topology and tracial representations](bounded-topology-and-tracial-representations.md) prerequisite at the locators given in Section 1. Section 14 proves its precise fixed-point prerequisite, and Section 15 proves the support and closed-ideal foundations used in the faithfulness supplement. Public access to scholarly sources does not change their copyright or license terms. The original expression written for this lesson and the reused projection proofs retain their respective recorded CC0 dedications; primary source text and page images are not included as CC0 components.

## 14. Common fixed points for affine isometries

This is an independently written Banach-space specialization of the geometric proof of I. Namioka and E. Asplund, _A geometric proof of Ryll-Nardzewski's fixed point theorem_, Bull. Amer. Math. Soc. **73** (1967), 443–445, [publisher PDF](https://www.ams.org/journals/bull/1967-73-03/S0002-9904-1967-11779-8/S0002-9904-1967-11779-8.pdf). The geometric lemma is on pp. 443–444; the theorem and complete proof are on pp. 444–445.

**Theorem.** Let \(X\) be a Banach space and let \(Q\subset X\) be nonempty, convex, and compact for the weak topology \(\sigma(X,X^*)\). Suppose a group acts on \(Q\) by affine norm isometries. Then some \(q\in Q\) is fixed by every group element.

The space, set, and group may all be nonseparable. Affine isometries of a convex subset are weakly continuous: choose \(q_0\in Q\), extend the affine difference map to the real linear span of \(Q-q_0\), and then its norm closure. Every vector in that span has the form \(t(x-y)\), with \(t\ge0\) and \(x,y\in Q\); preservation of affine relations makes the extension well defined, and the isometry identity makes it bounded. Hahn–Banach identifies the induced weak topology on this subspace with its own weak topology. Translation then gives weak continuity on \(Q\). Complex spaces can be regarded as real spaces, with the same weak topology. In Yeadon's application the maps already are bounded linear isometries of the whole predual, so this extension step is unnecessary.

The proof below retains two classical general results: the Krein–Milman theorem and the Baire category theorem for compact Hausdorff spaces. It also uses basic weak topology facts: a weakly compact set in a Banach space is norm bounded, norm-closed convex sets are weakly closed, and the norm is weakly lower semicontinuous. It proves the compact-generator fact used in the source and replaces the source's imported single-map fixed-point result by averaging.

### 14.1. A compact generator contains the extreme points

Let \(K\) be a weakly compact convex set, \(F\subset K\) weakly compact, and \(K=\overline{\operatorname{co}}^{\,w}F\). Then every extreme point of \(K\) lies in \(F\).

To prove this, suppose an extreme point \(z\) lies outside \(F\). Choose real continuous linear functionals \(f_1,\ldots,f_m\) and \(a>0\) such that the weak neighborhood
\[
\{x:|f_j(x-z)|<a\text{ for all }j\}
\tag{FP1}
\]
does not meet \(F\). The finitely many compact sets
\[
\begin{gathered}
F_{j,+}=\{x\in F:f_j(x-z)\ge a\},\\
\qquad
F_{j,-}=\{x\in F:f_j(x-z)\le-a\}
\end{gathered}
\tag{FP2}
\]
cover \(F\). Ignore empty pieces and take the weakly closed convex hull of each remaining piece. These hulls are compact subsets of \(K\); none contains \(z\), by the corresponding functional inequality. The convex hull of their finite union is compact, because it is the continuous image of their product and a finite-dimensional simplex. It therefore is closed, contains \(F\), and equals \(K\). Expressing \(z\) as a convex combination of points of these hulls contradicts extremality: each point with positive coefficient must equal \(z\). This proves the claim.

The compact-generator step needed by the Namioka–Asplund argument is therefore proved within this lesson.

### 14.2. A small complement in a separable compact convex set

Let \(K\subset X\) be nonempty, weakly compact, convex, and norm separable. For every \(\varepsilon>0\), there is a proper weakly closed convex subset \(C\subset K\) such that
\[
\operatorname{diam}_{\|\cdot\|}(K\setminus C)\le\varepsilon.
\tag{FP3}
\]
The empty set is permitted as \(C\). If \(\operatorname{diam}K\le\varepsilon\), it already works. Assume henceforth \(d=\operatorname{diam}K>\varepsilon\).

Let \(D\) be the weak closure of the extreme points of \(K\). It is nonempty and weakly compact. A countable family of translates of the closed norm ball of radius \(\varepsilon/4\) covers \(K\), hence \(D\). These sets are weakly closed. Baire category gives a weakly open set \(W\) and a center \(k\in K\) such that
\[
\varnothing\ne D\cap W\subset k+(\varepsilon/4)B_X.
\tag{FP4}
\]
Set
\[
\begin{gathered}
K_1=\overline{\operatorname{co}}^{\,w}(D\setminus W),\\
\qquad
K_2=\overline{\operatorname{co}}^{\,w}(D\cap W).
\end{gathered}
\tag{FP5}
\]
Then \(\operatorname{diam}K_2\le\varepsilon/2\). Both sets are compact, \(K_2\ne\varnothing\), and \(K_1\ne K\): if \(K_1=K\), the compact-generator result would put every extreme point in \(D\setminus W\), whereas \(W\cap D\ne\varnothing\) implies \(W\) meets the dense set of extreme points in \(D\). Also \(K_1\ne\varnothing\), since otherwise Krein–Milman would give \(K=K_2\), contradicting \(d>\varepsilon\).

Krein–Milman and compactness now give
\[
K=\operatorname{co}(K_1\cup K_2).
\tag{FP6}
\]
For \(r=\varepsilon/(4d)\in(0,1)\), define
\[
\begin{gathered}
C=\{\lambda a+(1-\lambda)b:\\
a\in K_1,\ b\in K_2,\ r\le\lambda\le1\}.
\end{gathered}
\tag{FP7}
\]
This is compact and convex. It is proper: if \(C=K\), every extreme point \(z\) would have such a representation with \(\lambda>0\), forcing \(a=z\), hence all extreme points into \(K_1\). Krein–Milman would then give \(K=K_1\), a contradiction.

For \(y\in K\setminus C\), a representation \(y=\lambda a+(1-\lambda)b\) must have \(\lambda<r\). Consequently \(\|y-b\|\le rd\). Two such points are at distance at most
\[
2rd+\operatorname{diam}K_2\le2\frac{\varepsilon}{4d}d+\frac\varepsilon2=\varepsilon.
\tag{FP8}
\]
This proves the lemma, including the zero-diameter and large-\(\varepsilon\) cases that are implicit in the original proof.

### 14.3. One affine map has a fixed point

Let \(A:Q\to Q\) be weakly continuous and affine. Choose \(z\in Q\) and set
\[
z_n=\frac1n\sum_{j=0}^{n-1}A^jz\in Q.
\tag{FP9}
\]
Affinity gives
\[
\begin{gathered}
Az_n-z_n=\frac{A^nz-z}{n},
\\
\qquad
\|Az_n-z_n\|\le\frac{\operatorname{diam}Q}{n}\longrightarrow0.
\end{gathered}
\tag{FP10}
\]
Weak compactness gives a weakly convergent subnet, with limit \(z_0\in Q\). Weak continuity of \(A\) then gives \(Az_0=z_0\). This avoids an additional Schauder–Tychonoff fixed-point import for the present Banach-space interface.

### 14.4. From one averaged map to a finite family

Take finitely many acting isometries \(g_1,\ldots,g_m\), and let
\[
A=\frac1m\sum_{i=1}^m g_i.
\tag{FP11}
\]
The preceding step gives \(x_0\in Q\) with \(Ax_0=x_0\). Suppose some \(g_i\) moves \(x_0\). Delete the indices fixing \(x_0\) and average only the remaining maps. Their average still fixes \(x_0\), because the deleted summands each were \(x_0\). Relabel the remaining maps \(g_1,\ldots,g_r\), and put
\[
\delta=\min_{1\le i\le r}\|g_ix_0-x_0\|>0,
\qquad \varepsilon=\delta/2.
\tag{FP12}
\]
Let \(S\) be the semigroup generated by these maps and the identity, and set
\[
K=\overline{\operatorname{co}}^{\,\|\cdot\|}\{s x_0:s\in S\}.
\tag{FP13}
\]
There are only countably many finite words, so \(K\) is norm separable. It is a weakly closed convex subset of \(Q\), hence weakly compact. Step 2 gives a proper closed convex \(C\subset K\) with \(\operatorname{diam}(K\setminus C)\le\varepsilon\).

Some \(s x_0\) lies outside \(C\), since otherwise the closed convex hull of the orbit would be contained in \(C\). Since the remaining average fixes \(x_0\), affinity of \(s\) gives
\[
s x_0=\frac1r\sum_{i=1}^r s g_i x_0.
\tag{FP14}
\]
At least one \(s g_i x_0\) also lies outside \(C\). Both points belong to \(K\), so their distance is at most \(\varepsilon\); but \(s\) is an isometry, and therefore
\[
\|s g_i x_0-s x_0\|=\|g_i x_0-x_0\|\ge\delta>\varepsilon.
\tag{FP15}
\]
This contradiction proves that \(x_0\) fixes the entire finite family. Notice that only this finitely generated orbit hull is made separable; no separability was imposed on \(X\) or \(Q\).

### 14.5. The whole group

For every group element \(g\), its fixed-point set in \(Q\) is weakly closed. Step 4 shows that these sets have the finite intersection property. Compactness of \(Q\) gives a point in their total intersection. This proves the theorem.

### 14.6. Interface to Ringrose's trace proof

In the proof of Yeadon's theorem, take \(X=R_*\) and let \(Q=Q_\rho\) be the norm-closed convex hull of the orbit of a normal functional \(\rho\) under the maps
\[
(L_U\omega)(A)=\omega(U^*AU).
\tag{FP16}
\]
Yeadon's Lemma 2 gives weak compactness of \(Q_\rho\), which is nonempty and convex by construction. Each \(L_U\) is a bounded linear norm isometry, has inverse \(L_{U^*}\), and preserves \(Q_\rho\). Thus the theorem gives an invariant normal functional in \(Q_\rho\). All hypotheses are verified by Yeadon's Lemmas 1 and 2 (the second uses Akemann's weak-compactness criterion) and by predual theory.

For the original paper's more general formulation, equip \(E\) with its **norm topology**. Its noncontracting hypothesis is then verified by
\[
\begin{gathered}
\inf_U\|L_U\omega-L_U\eta\|=\|\omega-\eta\|>0\\
\quad(\omega\ne\eta).
\end{gathered}
\tag{FP17}
\]
The compactness hypothesis remains compactness for the associated weak topology. This is norm noncontraction; substituting the weak topology for the original locally convex topology would be a different hypothesis.

## 15. Support projections and trace faithfulness

The freely accessible primary lecture provider is Jesse Peterson, _Notes on von Neumann algebras_, April 5, 2013: [Lemma 4.3.1 and its following support paragraph, printed/PDF p. 61](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf#page=61). The source proves the WOT-closed ideal classification using the positive contractive approximate identity of Theorem 1.4.9, p. 15. Both bodies were read. Proposition 4.5.2, p. 67, uses these supports to produce faithful normal states in countably decomposable algebras.

Here is a separately written proof using spectral supports. It works directly for **ultraweakly closed** ideals, which is sufficient for the trace kernel. It also fills the null-ideal closure step instead of requiring a positive trace-class extension theorem.

Retained background consists of the spectral calculus in a von Neumann algebra, existence of joins of projections, bounded strong convergence implying ultraweak convergence, positivity/Cauchy–Schwarz for positive functionals, the fact that normal functionals form a bimodule, and normal functionals separating positive elements. There is no projection comparison, monic-projection theorem, finite type decomposition, or countability assumption in the faithfulness argument.

### 15.1. Ultraweakly closed left ideals

Let \(M\) be a von Neumann algebra and \(I\subset M\) an ultraweakly closed linear left ideal. For \(x\in I\), the positive element \(h=x^*x\) lies in \(I\). For \(t>0\),
\[
a_t=h(h+t1)^{-1}=(h+t1)^{-1}h\in I.
\tag{SP1}
\]
As \(t\downarrow0\), these positive contractions tend strongly to the support projection \(p_x=1_{(0,\infty)}(x^*x)\). The convergence is bounded, hence ultraweak. Therefore \(p_x\in I\), and spectral calculus gives \(x=xp_x\).

Let \(p=\bigvee_{x\in I}p_x\). Finite joins belong to \(I\): the join of finitely many \(p_x\)'s is the support of their positive sum, so the same preceding argument applies. The net of finite joins converges strongly and boundedly to \(p\), hence \(p\in I\). Every \(x\in I\) satisfies \(xp=x\). Conversely, \(Mp\subset I\) by the left-ideal property. Thus
\[
I=Mp.
\tag{SP2}
\]
The zero ideal corresponds to \(p=0\).

If \(I\) is also a right ideal, then for every \(y\in M\), \(py\in I=Mp\), so \(py=pyp\). Apply this to \(y^*\) and take adjoints to obtain \(yp=pyp\). Hence \(p\) is central. This proves the needed closed-ideal classification without an approximate-identity import.

### 15.2. A normal positive functional has a support corner

For a normal positive functional \(\varphi\), define
\[
N_\varphi=\{x\in M:\varphi(x^*x)=0\}.
\tag{SP3}
\]
Cauchy–Schwarz gives the identity
\[
N_\varphi=\bigcap_{y\in M}\ker\bigl(x\mapsto\varphi(y^*x)\bigr).
\tag{SP4}
\]
Each functional in this intersection is normal. This follows from the bimodule property of the predual; concretely, multiplying one argument of an ultraweak vector-coefficient series by the bounded operator \(y\) preserves absolute summability. Therefore \(N_\varphi\) is an ultraweakly closed linear subspace. Positivity gives
\[
\varphi((ax)^*(ax))\le\|a\|^2\varphi(x^*x),
\tag{SP5}
\]
so it is a left ideal. Step 1 gives \(N_\varphi=Mp_0\) for a projection \(p_0\). Put \(s(\varphi)=1-p_0\).

Because \(\varphi(p_0)=0\), Cauchy–Schwarz gives \(\varphi(xp_0)=\varphi(p_0x)=0\) for all \(x\). Thus
\[
\varphi(x)=\varphi(s(\varphi)x s(\varphi)).
\tag{SP6}
\]
On the corner \(s(\varphi)Ms(\varphi)\), this functional is faithful: if \(x\) in the corner satisfies \(\varphi(x^*x)=0\), then \(x=xp_0\), while \(xp_0=0\). Hence \(x=0\).

These are exactly the support properties used in Peterson's Proposition 4.5.2. A nonzero corner always has a nonzero normal positive functional, for example a vector state in a concrete faithful representation. Passing to its nonzero support corner gives a faithful normal state after normalization.

### 15.3. Faithfulness of the normal center-valued trace

Suppose \(T:M\to Z(M)\) is positive, normal, equal to the identity on the center, and unitary invariant. These are the properties in Yeadon's theorem; no scalar trace is presumed.

First \(T(xy)=T(yx)\). For a unitary \(u\), substitute \(A=ux\) into unitary invariance to get \(T(xu)=T(ux)\), then use the linear span of unitaries to allow arbitrary \(u\). Define
\[
I=\{x\in M:T(x^*x)=0\}.
\tag{SP7}
\]
Normal positive functionals \(\omega\) on the center separate its positive elements, so
\[
I=\bigcap_{\omega\in Z(M)_*^+}N_{\omega\circ T}.
\tag{SP8}
\]
Step 2 shows that \(I\) is an ultraweakly closed linear left ideal. For \(x\in I\), positivity and traciality give
\[
\begin{gathered}
T((xy)^*(xy))
=T(y^*x^*xy)\\
=T(xyy^*x^*)\\
\le\|y\|^2T(xx^*)=\|y\|^2T(x^*x)=0.
\end{gathered}
\tag{SP9}
\]
Thus \(I\) is also a right ideal. Step 1 gives \(I=Mz\) for a central projection \(z\). Since \(z\in I\), \(T(z)=T(z^*z)=0\); since \(T\) fixes the center, \(T(z)=z\). Therefore \(z=0\), so \(I=0\). This proves faithfulness.

This removes the monic-projection and type-decomposition imports from the faithfulness supplement. It does not remove the finite projection-comparison facts used in Yeadon's trace **existence** proof.

### 15.4. The countably decomposable scalar consequence

Suppose now \(M\) is countably decomposable. Its center is countably decomposable too. To obtain a faithful normal central state, take a maximal orthogonal family of nonzero support corners with faithful normal states \(\omega_j\). Such corners exist in every nonzero remainder by Step 2, so their projections sum to one. The family is finite or countable. With positive weights \(c_j\) summing to one,
\[
\omega(z)=\sum_jc_j\omega_j(p_jzp_j)
\tag{SP10}
\]
is normal by convergence in predual norm, and faithful because \(\omega(z^*z)=0\) forces \(zp_j=0\) for every \(j\). This is Peterson's Proposition 4.5.2, with finite and countable weights both normalized explicitly.

Then \(\tau=\omega\circ T\) is a normal tracial state, and is faithful by Step 3 and faithfulness of \(\omega\). No separable-predual or factor assumption has been added. The state is unique after its central restriction \(\omega\) is fixed, by part (1) of Yeadon's theorem; there is no assertion of a unique scalar trace for a nontrivial center.
