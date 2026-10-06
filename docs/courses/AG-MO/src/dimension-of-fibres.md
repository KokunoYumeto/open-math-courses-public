# Dimension of fibres

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A family can acquire a larger fibre at a special parameter. To measure this correctly, we must distinguish the dimension of a fibre near a point from the dimension of its local ring. The first counts parameters on components through that point; the second counts specializations ending there. Residue fields account for the difference. We will then prove that large local fibres form a closed subset of the source, and that properness carries this closedness to the parameter space.

Our prerequisites are Quasi-finite morphisms and Chevalley's theorem, Krull dimension and Noether normalization, especially Theorems 4.2, 4.3, 5.1 and 6.1, and Dimension theory of Noetherian local rings, Theorem 5.1. The last theorem says that a local map of Noetherian local rings satisfies

\[
\dim B\leq\dim A+\dim(B/\mathfrak m_A B),
\tag{0.1}
\]

with equality for a flat map. The empty scheme has dimension \(-\infty\). All fields below are arbitrary; points need not be closed or rational.

## 1. Two dimensions at one point

For a scheme locally of finite type over a field and a point \(x\), define

\[
\dim_x X=\inf_{x\in U\text{ open}}\dim U.
\tag{1.1}
\]

This infimum is a finite nonnegative integer and is attained: take a finite-type affine neighbourhood, which is Noetherian and finite-dimensional. Removing its finitely many components not containing \(x\) leaves a neighbourhood whose dimension is the largest dimension of a component through \(x\). Every smaller neighbourhood still has that dimension. Indeed, a nonempty affine open in an integral finite-type component has its original function field, so has the same dimension by the dimension–transcendence-degree theorem. This description is local and therefore also applies when the whole scheme is not quasi-compact.

For \(f:X\to S\) locally of finite type, write \(s=f(x)\),
\(X_s=X\times_S\operatorname{Spec}\kappa(s)\), and

\[
\delta_f(x)=\dim_x X_s.
\tag{1.2}
\]

The point of the fibre corresponding to \(x\) has residue field \(\kappa(x)\). If an affine chart is given by \(A\to B\), with primes \(\mathfrak q\) above \(\mathfrak p\), the fibre's local ring is
\(B_{\mathfrak q}/\mathfrak p B_{\mathfrak q}\). Inverting \(A\setminus\mathfrak p\), reducing modulo \(\mathfrak p\), and localizing at the fibre prime gives precisely this ring.

**Theorem 1.1 (local fibre dimension).** For every such \(f\) and \(x\),

\[
\delta_f(x)=\dim\mathcal O_{X_s,x}
+\operatorname{trdeg}_{\kappa(s)}\kappa(x).
\tag{1.3}
\]

**Proof.** Restrict to a finite-type affine neighbourhood of \(x\) in \(X_s\), say \(\operatorname{Spec}C\), and let \(\mathfrak r\) represent \(x\). Let \(\mathfrak a_i\subset\mathfrak r\) be its minimal primes through that point. Set \(d_i=\dim(C/\mathfrak a_i)\) and \(e=\operatorname{trdeg}_{\kappa(s)}\kappa(\mathfrak r)\). The component description gives \(\dim_x X_s=\max_i d_i\). The height formula in each domain \(C/\mathfrak a_i\) gives

\[
\operatorname{ht}(\mathfrak r/\mathfrak a_i)=d_i-e.
\]

Every prime chain in \(C_{\mathfrak r}\) lies over one of its minimal primes. Its dimension is consequently \(\max_i\operatorname{ht}(\mathfrak r/\mathfrak a_i)=\max_i d_i-e\). Rearrangement proves (1.3). This is also exactly the field-algebra theorem in the prerequisite's Theorem 6.1. \(\square\)

Compare [Stacks, Tag 02FX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-dimension-fibre-at-a-point). For \(\mathbb A^1_k\to\operatorname{Spec}k\), the generic point has local ring \(k(t)\), of dimension zero, and residue transcendence degree one. Its geometric local dimension is one. At a closed point the local ring has dimension one and the residue extension is finite, giving the same answer. Using only local-ring dimension would incorrectly call the generic part of the line zero-dimensional.

**Proposition 1.2 (composition).** If \(X\xrightarrow fY\xrightarrow gS\) are locally of finite type, with images \(x,y,s\), then

\[
\dim_x X_s\leq\dim_x X_y+\dim_y Y_s.
\tag{1.4}
\]

Equality holds when \(\mathcal O_{X_s,x}\) is flat over \(\mathcal O_{Y_s,y}\), in particular when \(f\) is flat at \(x\).

**Proof.** The indicated fibre local rings are Noetherian. Apply (0.1) to their local map. Its local closed fibre is \(\mathcal O_{X_y,x}\). Add
\(\operatorname{trdeg}_{\kappa(s)}\kappa(x)=\operatorname{trdeg}_{\kappa(y)}\kappa(x)+\operatorname{trdeg}_{\kappa(s)}\kappa(y)\)
and use (1.3) three times. Flatness gives equality in (0.1); flatness at \(x\) passes to this fibre map by base change and localization. \(\square\)

This is [Stacks, Tag 02JS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-dimension-fibre-at-a-point-additive). No global equidimensionality is assumed.

## 2. Small fibres form an open subset of the source

We first specify the algebraic neighbourhood result that works over an arbitrary ring.

**Lemma 2.1 (relative parameters).** Let \(A\to B\) be finite type, let \(\mathfrak q\) contract to \(\mathfrak p\), and suppose the fibre has geometric local dimension \(r\) at \(\mathfrak q\). There are \(h\notin\mathfrak q\) and an \(A\)-algebra map

\[
A[T_1,\ldots,T_r]\longrightarrow B_h
\tag{2.1}
\]

that is quasi-finite everywhere.

The exact complete open proof is [Stacks, Tag 00QE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-quasi-finite-over-polynomial-algebra). Here is the mechanism and the supporting proof it uses. First shrink a basic neighbourhood of \(\mathfrak q\) so that its entire \(\kappa(\mathfrak p)\)-fibre has dimension \(r\): remove components not containing the chosen point, using Section 1. Normalize that fibre by \(r\) polynomial parameters. The polynomial coordinate changes in Noether normalization can be taken in the integer subalgebra generated by the original algebra generators. Thus these parameters lift to \(B\), even when the fibre field contains fractions that do not lift as coefficients to \(A\). The resulting map from the polynomial algebra is quasi-finite at the chosen point. Finally shrink its quasi-finite locus.

The last step has the complete independent algebraic proof at [Stacks, Tag 00QA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-quasi-finite-open), using the algebraic [Zariski Main Theorem, Tag 00Q9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-main-theorem). At a quasi-finite prime that theorem supplies an integral subalgebra agreeing with \(B\) after localization. A finite integral subalgebra containing the finitely many necessary generators still agrees after localization, so the neighbourhood is a localization of a finite algebra. Theorem 3.1 of Zariski's Main Theorem also proves this step in the course, starting from the independent algebraic theorem. These proofs supply Lemma 2.1 without assuming a Noetherian base or using the semicontinuity theorem we are about to prove. The linked source text retains GNU FDL 1.2 and is not reproduced.

**Theorem 2.2 (Chevalley's semicontinuity on the source).** For \(f:X\to S\) locally of finite type and any integer \(n\geq0\),

\[
U_n=\{x\in X:\delta_f(x)\leq n\}
\tag{2.2}
\]

is open.

**Proof.** Choose \(x\in U_n\), an affine base neighbourhood and a finite-type affine source neighbourhood, given by \(A\to B\). Set \(r=\delta_f(x)\leq n\) and use Lemma 2.1. Quasi-finiteness survives base change, by the quasi-finite lesson. For every base point \(\mathfrak p'\), the new fibre is therefore quasi-finite over
\(\mathbb A^r_{\kappa(\mathfrak p')}\).

Any finite-type scheme \(Z\) quasi-finite over \(\mathbb A^r_K\) has dimension at most \(r\). To check this, take a generic point \(z\) of an irreducible component and its image \(w\). Quasi-finiteness gives a finite residue extension \(\kappa(w)\subset\kappa(z)\). Consequently

\[
\dim\overline{\{z\}}=\operatorname{trdeg}_K\kappa(z)
=\operatorname{trdeg}_K\kappa(w)\leq r.
\]

There are finitely many components, so their maximum bounds \(\dim Z\). Apply this to each fibre of \(\operatorname{Spec}B_h\). At every point of this neighbourhood the local fibre dimension is at most \(r\), hence at most \(n\). Geometric local dimension is unchanged by passing to an open neighbourhood, so this proves \(\operatorname{Spec}B_h\subset U_n\). Such neighbourhoods cover \(U_n\). \(\square\)

This is [Stacks, Tag 02FZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-openness-bounded-dimension-fibres). It is a statement on \(X\). It does not yet assert openness or closedness of any subset of \(S\).

**Corollary 2.3.** If \(f\) is of finite type and \(S\) is quasi-compact, the dimensions of its nonempty fibres have a common finite bound.

**Proof.** Then \(X\) is quasi-compact. Each point lies in some \(U_n\), and these opens increase with \(n\). A finite subcover gives \(X=U_N\) for one \(N\). Each fibre is a finite-type scheme over a field, so its dimension is the maximum of its local dimensions, and is at most \(N\). \(\square\)

Compare [Stacks, Tag 0A3V](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-morphism-finite-type-bounded-dimension).

## 3. Properness moves semicontinuity to the base

**Theorem 3.1.** For a proper morphism \(f:X\to S\), the function
\(s\mapsto\dim X_s\), including the value \(-\infty\) on empty fibres, is upper semicontinuous. Thus

\[
\{s\in S:\dim X_s\geq n\}
\tag{3.1}
\]

is closed for every integer \(n\).

**Proof.** Suppose first \(n\geq1\). By Theorem 2.2,
\(C_n=X\setminus U_{n-1}=\{x:\delta_f(x)\geq n\}\)
is closed. A proper map is closed, so \(f(C_n)\) is closed. A fibre is of finite type over its residue field, and its dimension is the largest dimension of its finitely many components. It has dimension at least \(n\) exactly when some point has geometric local dimension at least \(n\). Hence (3.1) equals \(f(C_n)\).

For \(n\leq0\), (3.1) is the set of nonempty fibres, which is \(f(X)\) and is closed as well. Its complement consists of the empty fibres. These closed upper-level sets are the required upper semicontinuity. \(\square\)

The same proof applies to any closed morphism locally of finite type whose fibres are finite type; properness supplies these conditions automatically. For example, a projective family of homogeneous equations has closed parameter loci where its solution space has dimension at least \(n\). The assertion concerns dimension, and does not claim that reducedness, multiplicity or the number of components is constant there.

## 4. Dominant families of varieties

**Theorem 4.1.** Let \(f:X\to Y\) be a dominant morphism of integral schemes of finite type over \(k\), and put

\[
d=\dim X-\dim Y
=\operatorname{trdeg}_{K(Y)}K(X).
\tag{4.1}
\]

Every irreducible component of every nonempty fibre has dimension at least \(d\). There is a dense open \(V\subset Y\) over which the fibres are nonempty and every component has dimension exactly \(d\).

**Proof of the lower bound.** Let \(z\) be the generic point of a component of \(X_s\). The fibre local ring at \(z\) has dimension zero, even if it has nilpotents. Inequality (0.1) for
\(\mathcal O_{Y,s}\to\mathcal O_{X,z}\)
therefore gives \(\dim\mathcal O_{X,z}\leq\dim\mathcal O_{Y,s}\). The field height formula yields

\[
\dim X-\operatorname{trdeg}_k\kappa(z)
\leq\dim Y-\operatorname{trdeg}_k\kappa(s).
\]

The tower rule for transcendence degree identifies the difference on the right after rearrangement with
\(\operatorname{trdeg}_{\kappa(s)}\kappa(z)\). This is precisely the dimension of that component. It is at least \(d\). The argument includes nonclosed \(s\).

**Proof of generic equality.** Write \(\eta\) for the generic point of \(Y\). Dominance gives an inclusion of function fields. The generic fibre is a nonempty integral finite-type \(K(Y)\)-scheme with function field \(K(X)\), so has dimension \(d\). Every point on it has geometric local dimension \(d\).

The closed subset \(C=\{x:\delta_f(x)\geq d+1\}\) consequently misses the generic fibre. By Chevalley's theorem its image is constructible. The morphism here is of finite type: on affine charts a finite tuple of \(k\)-algebra generators also generates over the target algebra, and quasi-compactness follows because the source is Noetherian. The closed restriction is still finite type. In an irreducible Noetherian space, a dense constructible subset contains a nonempty open and hence the generic point, as proved in the constructibility lesson. Since \(\eta\notin f(C)\), its closure is a proper closed subset. On its open complement every local fibre dimension is at most \(d\).

Likewise \(f(X)\) is constructible and contains \(\eta\), so it contains a dense open \(V'\). Intersect these two dense opens. Over the resulting \(V\), every fibre is nonempty and all its component dimensions are at most \(d\); the lower bound makes them exactly \(d\). \(\square\)

No properness or flatness was needed. Properness would instead ensure nonemptiness everywhere for this dominant map, because its closed image contains \(\eta\). The equality concerns the dense open just constructed; special fibres may be larger.

## 5. The dimension formula over a Noetherian base

A Noetherian ring is **universally catenary** if every finite-type algebra over it is catenary: all saturated prime chains between two specified comparable primes have the same finite length. A locally Noetherian scheme is universally catenary if its affine coordinate rings are. Fields are universally catenary by Theorem 5.1 of the dimension prerequisite. The extra hypothesis permits subtracting heights along a prime interval.

**Theorem 5.1 (dimension formula).** Suppose \(X,S\) are integral, \(S\) is locally Noetherian, and \(f:X\to S\) is dominant and locally of finite type. Set \(t=\operatorname{trdeg}_{K(S)}K(X)\). For \(x\mapsto s\),

\[
\dim\mathcal O_{X,x}
\leq\dim\mathcal O_{S,s}+t
-\operatorname{trdeg}_{\kappa(s)}\kappa(x).
\tag{5.1}
\]

Equality holds when \(S\) is universally catenary.

**Proof.** On nonempty affine charts this is a statement about an injective finite-type map of Noetherian domains \(A\subset B\). Write \(B=A[b_1,\ldots,b_m]\) and induct on the generators; intermediate domains are finite type over \(A\). For one transcendental generator the map is \(A\to A[T]\). If \(Q\) contracts to \(\mathfrak p\), the flat case of (0.1) says

\[
\operatorname{ht}Q=\operatorname{ht}\mathfrak p+
\dim\bigl(\kappa(\mathfrak p)[T]_{\bar Q}\bigr).
\]

The last dimension is zero at the zero prime and one at a nonzero prime. It is therefore
\(1-\operatorname{trdeg}_{\kappa(\mathfrak p)}\kappa(Q)\).
This proves equality for the polynomial case over every Noetherian domain.

For an algebraic generator, write \(B=A[T]/N\), where \(N\ne0\) is prime and \(N\cap A=0\). Every prime below \(N\) also contracts to zero. Localizing by \(A\setminus\{0\}\) identifies their interval with the interval below a nonzero prime in \(\operatorname{Frac}(A)[T]\). That polynomial ring is a PID, so \(\operatorname{ht}N=1\).

Let \(Q\supset N\) be the inverse image of the chosen prime \(\mathfrak q\) of \(B\), and let \(\mathfrak p=Q\cap A\). A chain from \(N\) to \(Q\), preceded by \((0)\subsetneq N\), has length at most \(\operatorname{ht}Q\). Hence

\[
\operatorname{ht}_B\mathfrak q\leq\operatorname{ht}_{A[T]}Q-1
=\operatorname{ht}_A\mathfrak p
-\operatorname{trdeg}_{\kappa(\mathfrak p)}\kappa(\mathfrak q).
\]

This is (5.1), since the fraction-field extension has transcendence degree zero. If \(A\) is universally catenary, \(A[T]\) is catenary. A saturated chain from zero to \(Q\) through the height-one prime \(N\) shows that the interval from \(N\) to \(Q\) has length \(\operatorname{ht}Q-1\); thus equality holds. Heights here are finite, because the localized rings are Noetherian local rings.

For several generators apply these one-generator statements along the contracted primes in the intermediate domains. Add the inequalities. Transcendence degrees of fraction fields and residue fields both add in towers, giving (5.1). Under universal catenarity every intermediate domain is universally catenary: an algebra finite type over it is still finite type over \(A\). All the component inequalities are then equalities. Finally local dimensions equal heights, and the charts have the schemes' function fields, proving the scheme statement. \(\square\)

These are [Stacks, Tags 02JU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-dimension-formula) and [02IJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-formula). Noetherian alone does not justify the equality. Combining the equality with (1.3) gives

\[
\delta_f(x)=\dim\mathcal O_{X_s,x}+\dim\mathcal O_{S,s}
+t-\dim\mathcal O_{X,x}.
\tag{5.2}
\]

This comparison uses both the local fibre ring and the local rings of source and base; the dimension difference of the entire schemes alone does not determine a special fibre.

## 6. Three families to compute

**A plane mapping to a plane.** Consider
\(f:\mathbb A^2_k\to\mathbb A^2_k\), \((x,y)\mapsto(a,b)=(x,xy)\).
For a target point with residue field \(K\), its fibre algebra is

\[
K[y]/(ay-b).
\tag{6.1}
\]

| Condition in \(K\) | Fibre | Dimension |
| --- | --- | --- |
| \(a\ne0\) | one \(K\)-point, \(y=b/a\) | \(0\) |
| \(a=b=0\) | \(\mathbb A^1_K\) | \(1\) |
| \(a=0,\ b\ne0\) | empty | \(-\infty\) |

On the source, \(\delta_f\) is one on \(V(x)\) and zero on \(D(x)\). The small-fibre locus is open, exactly as Theorem 2.2 predicts. On the target, the nonempty-fibre locus is \(D(a)\cup\{(0,0)\}\), which is dense and not closed. Thus this map is not proper, and its target dimension function fails upper semicontinuity at level zero. The dimension difference of the integral source and target is zero, so the line fibre respects the lower bound of Theorem 4.1.

**The exceptional line.** In \(\mathbb A^2_k\times\mathbf P^1_k\), with homogeneous coordinates \([s:t]\), put

\[
W=V(xt-ys).
\tag{6.2}
\]

On \(s\ne0\), write \(u=t/s\); its equation is \(y=xu\), giving the affine chart \(\operatorname{Spec}k[x,u]\). On \(t\ne0\), write \(v=s/t\); the chart is \(\operatorname{Spec}k[y,v]\), with \(x=yv\). On the overlap, \(v=u^{-1}\). Away from the origin the direction \([s:t]=[x:y]\) is unique, so the projection is an isomorphism there. Over the origin it is the whole \(\mathbf P^1_k\). This is the blow-up whose universal property will be proved in this course's planned lesson *Blowing up*.

The projection is projective and hence proper, since (6.2) is a closed subscheme of \(\mathbf P^1_{\mathbb A^2}\). Its fibre dimension is one at the origin and zero elsewhere. Its positive-dimensional-fibre locus on the target is the closed origin; on the source it is the closed exceptional line. The two affine charts already verify these assertions without appealing to the future universal property.

**A missing fibre.** Projection \(V(xy-1)\to\mathbb A^1_x\) identifies the hyperbola with \(D(x)\). Every fibre over \(D(x)\) is one point, and the fibre over zero is empty. Its source function \(\delta_f\) is constantly zero. Its target function takes zero on \(D(x)\) and \(-\infty\) at zero, so its level set \(\{s:\dim X_s\geq0\}=D(x)\) is not closed. Keeping the empty-fibre convention exposes precisely why the target assertion needs a closedness hypothesis.

## 7. Exercises with solutions

**Exercise 7.1 (easy).** Compute every fibre of (6.1), and compute both terms of (1.3) at the generic and at a closed point of the exceptional line.

**Solution.** Substitution gives the three cases in the table. The exceptional fibre is \(\operatorname{Spec}k[y]\). At its generic point the local ring is \(k(y)\), of dimension zero, and residue transcendence degree is one. At a closed point, corresponding to an irreducible polynomial in \(k[y]\), the local ring is a one-dimensional localization of this PID and its residue field is finite over \(k\). The two sums are respectively \(0+1\) and \(1+0\), both one. Closed points need not be \(k\)-rational.

**Exercise 7.2 (medium).** For a finite-type \(K\)-algebra \(C\) and prime \(\mathfrak r\), prove the local dimension formula even when \(C\) is reducible or nonreduced.

**Solution.** Nilpotents change neither prime chains nor residue fields. List the minimal primes \(\mathfrak a_i\subset\mathfrak r\). Removing other components gives \(\dim_{\mathfrak r}\operatorname{Spec}C=\max_i\dim C/\mathfrak a_i\). Localizing gives \(\dim C_{\mathfrak r}=\max_i\operatorname{ht}(\mathfrak r/\mathfrak a_i)\). The domain height formula says each latter term is \(\dim C/\mathfrak a_i-e\), with the same \(e=\operatorname{trdeg}_K\kappa(\mathfrak r)\). Taking the maximum proves (1.3), without any equidimensionality assumption.

**Exercise 7.3 (medium).** Prove upper semicontinuity on the target for a proper morphism, and specify the subset of the source whose image is each upper-level set.

**Solution.** For \(n\geq1\), use the closed subset \(X\setminus U_{n-1}\). Its image is closed because the morphism is proper. A finite-type fibre has dimension at least \(n\) exactly when one of its components, and therefore a point on it, has geometric local dimension at least \(n\). Thus this image is the required upper-level set. For \(n\leq0\), use \(X\) itself: its image is the nonempty-fibre locus. This also proves upper semicontinuity at empty fibres, which must not be silently discarded.

**Exercise 7.4 (medium).** Explain the hyperbola counterexample without assuming \(k\) is algebraically closed. Why does it not contradict source semicontinuity?

**Solution.** The coordinate algebra is \(k[x,x^{-1}]\), so projection is the open immersion \(D(x)\hookrightarrow\operatorname{Spec}k[x]\). At any point in that open, tensoring with its residue field gives that field; at \((x)\), inverting the zero element gives the zero ring. Thus the dimensions are zero and \(-\infty\). The upper-level set for zero is the nonclosed dense open \(D(x)\), over every field. All source fibres at their source points are zero-dimensional, so \(U_0=X\) is open. The two semicontinuity statements concern different spaces.

**Exercise 7.5 (hard).** For a dominant morphism of integral finite-type \(k\)-schemes, prove generic equality of fibre dimensions and ensure the fibres on your chosen open are nonempty.

**Solution.** Its generic fibre has function field \(K(X)\) over \(K(Y)\), so dimension \(d=\dim X-\dim Y\). Theorem 2.2 makes \(C=\{\delta_f\geq d+1\}\) closed. Chevalley's theorem makes \(f(C)\) constructible. It misses the generic point, so cannot be dense; remove its proper closure. Chevalley also makes \(f(X)\) constructible, and dominance puts the generic point in that image, so it contains a dense open. Intersect the two opens to get nonempty fibres with all component dimensions at most \(d\). For a component's generic point \(z\), (0.1) bounds \(\dim\mathcal O_{X,z}\) by \(\dim\mathcal O_{Y,s}\), because its local fibre ring has dimension zero. The field height formula then gives \(\operatorname{trdeg}_{\kappa(s)}\kappa(z)\geq d\). Hence every component has dimension exactly \(d\).

## References and proof providers

The Stacks project, read in the AI Integrated Stacks Project edition, provides the exact local fibre, composition, semicontinuity and dimension formulas linked above. The arbitrary-base relative-parameter lemma uses the complete open proofs at Tags 00QE, 00QA and 00Q9; their statements and their role in the argument are specified in Section 2. These linked sources retain GNU FDL 1.2. Their text is not reproduced here.

Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), draft of 27 July 2024, §12.4, treats generic fibre dimension and the distinction between source and target semicontinuity. T. J. Ford, [*Commutative Algebra*](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf), version of 23 September 2026, Chapter 7, Section 6.4, treats the local base–fibre inequality. The complete internal proof of that inequality is the local-dimension prerequisite named at the start.
