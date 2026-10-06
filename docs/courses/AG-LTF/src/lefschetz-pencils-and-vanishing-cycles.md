# Lefschetz pencils and vanishing cycles

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A pencil replaces a smooth projective variety by a family over a projective line. Its singular fibres have one controlled singularity. The difference between a smooth fibre and a singular one is a vanishing cycle, and local inertia acts by a rank-one transformation determined by that cycle.

We prove geometric existence and openness, including degree-two Veronese embeddings in characteristic two. We then calculate the local quadratic stalks, supported generators and full normalized variation, including the odd comparison and mixed-characteristic transfer. Degree-zero local and global theory is proved in every residue characteristic, with the wild characteristic-two conductor kept explicit. Under the canonical higher-dimensional characteristic restriction, we prove tame generation, geometric conjugacy, the sheaf alternatives, invariants and absolute irreducibility of the vanishing quotient. The openness theorem includes the linear algebra and an explicit passage from one-parameter transvections to an open neighbourhood in the symplectic group.

## 1. The pencil and its blow-up

Let \(k\) be algebraically closed of characteristic \(p\), and fix \(\ell\ne p\); characteristic zero is allowed. Let \(X\subset\mathbf P^N_k\) be smooth, projective and connected, of dimension \(n+1\). A pencil is a line \(D\simeq\mathbf P^1\) in the dual projective space. Choose independent hyperplane equations \(h_0,h_1\); its members are
\(H_{[a:b]}=\{ah_0+bh_1=0\}\), and its axis is \(A=\{h_0=h_1=0\}\). Put \(B=A\cap X\).

A **Lefschetz pencil** has the following properties:

- \(A\) cuts \(X\) transversely, so \(B\) is smooth of codimension \(2\), or empty when \(X\) is a curve.
- Outside a finite set \(S\subset D\), the section \(X_t=X\cap H_t\) is smooth.
- For each \(s\in S\), \(X_s\) has exactly one singular point, an ordinary quadratic singularity, and the associated total space is regular.

For \(p\ne2\), an ordinary quadratic singularity is étale locally a hypersurface whose quadratic part is nondegenerate. In characteristic \(2\) one uses the smooth-projective-quadric definition of SGA 7, XVII, §1. The general inputs in §§2 and 4 exclude \(p=2\) with \(n\) even, as in Deligne's summary. Section 3 supplies a separate proof for \(n=0\) in every characteristic. In that dimension an ordinary quadratic special point means the length-two local algebra \(k[z]/(z^2)\); its generic fibre must still be smooth. Higher even dimension in characteristic two is not covered by the general inputs stated here.

### Existence, including characteristic two

**Theorem 1.0 (existence and openness).** Write \(m=\dim X=n+1\). After a degree-\(e\) Veronese embedding, for every \(e\ge2\), the Lefschetz pencils form a nonempty open subset of the Grassmannian of lines in the hyperplane parameter space. This holds in every characteristic. In characteristic zero the same conclusion holds for the original embedding. If the embedding is defined over a finite field, a pencil exists after a finite extension; existence over the original field is not asserted.

Here the quadratic tangent cone of an ordinary singularity must be a **nonzero** quadratic form whose projective zero locus is a smooth quadric of the expected dimension \(m-2\). For \(m=1\), this means a nonzero multiple of \(z^2\), with empty projective zero locus. In characteristic two, an odd-dimensional space of variables has an alternating polar form with a radical, so invertibility of that polar form would be the wrong condition.

**Proof.** We first work over an algebraically closed field. Since a smooth scheme has disjoint irreducible components, connectedness makes \(X\) integral. Set

\[
V_e=H^0(\mathbf P^N,\mathcal O(e)),\qquad
P_e=\mathbf P(V_e),\qquad M=\dim P_e.
\tag{LE.1}
\]

Using ambient forms, rather than assuming that their restrictions give every section of \(\mathcal O_X(e)\), makes this exactly the stated Veronese embedding.

**First and second jets.** At a point \(x=[1:0:\cdots:0]\), choose \(m\) ambient affine coordinates whose differentials are a basis of the cotangent space of \(X\). The forms \(X_0^e\) and \(X_0^{e-1}X_i\) prescribe the value and all first derivatives independently. Thus the map from \(V_e\) to first jets on \(X\) is everywhere surjective, of rank \(m+1\). Its kernel is a vector bundle. The incidence

\[
C_e=\{(x,[h]):h(x)=0,\ d(h|_X)_x=0\}
\subset X\times P_e
\tag{LE.2}
\]

is the projectivization of that kernel, hence smooth and integral of dimension \(M-1\) when nonempty. Its projection is proper. Its image \(\Delta_e\), the parameter set of singular sections, is therefore closed of dimension at most \(M-1\).

For \(e\ge2\), the additional monomials \(X_0^{e-2}X_iX_j\) prescribe any quadratic second jet while keeping the first jet zero. The ordinary quadratic forms are a nonempty open set: the bad set consists of the zero form and forms whose projective quadric has a singular point, and the latter condition is closed by projecting its projective point incidence. Examples of good forms are

\[
\begin{cases}
z_1^2+\cdots+z_m^2,&p\ne2,\\
z_1z_2+\cdots+z_{m-1}z_m,&p=2,\ m\ \text{even},\\
z_1z_2+\cdots+z_{m-2}z_{m-1}+z_m^2,
&p=2,\ m\ \text{odd}.
\end{cases}
\tag{LE.3}
\]

Their derivatives show the required smoothness; in the last case the only possible polar-radical point has nonzero quadratic value and is therefore outside the quadric. Consequently the nonordinary locus in \(C_e\) is closed and has dimension at most \(M-2\). Its proper image \(F_1\) has the same bound.

**Two different singular points.** Fix distinct \(x,y\), and choose coordinates with \(x=[1:0:\cdots:0]\) and \(y=[0:1:0:\cdots:0]\). For \(e\ge3\), the coefficients governing their first jets are the two disjoint blocks

\[
\{X_0^e,X_0^{e-1}X_i:i\ne0\},
\qquad
\{X_1^e,X_1^{e-1}X_i:i\ne1\}.
\tag{LE.4}
\]

After restriction to the two \(m\)-dimensional tangent spaces, the combined map has rank \(2m+2\). Varying the pair in the \(2m\)-dimensional space \(X\times X\setminus\operatorname{diag}(X)\), the incidence of two singular points has dimension at most \(M-2\).

For \(e=2\), the two coefficient blocks overlap only in \(X_0X_1\). Their first-jet condition spaces can have a one-dimensional intersection precisely when the secant line \(xy\) lies in both projective tangent \(m\)-planes. The rank is then \(2m+1\); elsewhere it is \(2m+2\). If \(X\) is not a linear projective subspace, the locus \(y\in T_xX\) is a proper closed subset of the space of distinct pairs. Indeed, if every such pair satisfied that condition, then, for each \(x\), the closed tangent \(m\)-plane would contain the dense subset \(X\setminus\{x\}\), hence all of \(X\). Equality follows from irreducibility and equal dimension, making \(X\) linear. The exceptional pair locus thus has dimension at most \(2m-1\), and its two-point incidence has dimension at most

\[
(2m-1)+M-(2m+1)=M-2.
\tag{LE.5}
\]

The same bound holds on the other rank stratum. Take the closure of the constructible image of this incidence in \(P_e\); closure preserves its dimension. Call it \(F_2\). Therefore \(F=F_1\cup F_2\) is closed of codimension at least two, and every section outside \(F\) is smooth or has exactly one ordinary quadratic point.

**The remaining quadratic linear-space case.** Suppose \(e=2\) and \(X=\mathbf P^m\). Restricting ambient quadrics onto \(X\) is surjective. We prove the assertion for all quadrics on a vector space of dimension \(d=m+1\), and then pull the bad set back along this surjection.

When \(p\ne2\), corank zero gives a smooth quadric and corank one gives one ordinary vertex. Symmetric forms with radical of dimension \(a\) have codimension \(a(a+1)/2\): choose the radical in a Grassmannian of dimension \(a(d-a)\), then a nondegenerate symmetric form on the quotient, of dimension \((d-a)(d-a+1)/2\), and subtract from \(d(d+1)/2\). The bad locus, corank at least two, has codimension at least three.

In characteristic two, the polar form is alternating. Polar forms with radical dimension \(a\) have codimension \(a(a-1)/2\), by the same Grassmannian calculation using alternating forms on the quotient. Passing from polar forms to quadratic forms adds the \(d\) independent diagonal coefficients. If \(d\) is odd, the generic radical is a line. A nonzero restriction of the quadratic form to that line gives a smooth projective quadric; zero restriction gives a single vertex whose local quadratic cone is nondegenerate on the quotient, hence ordinary. The bad locus has radical dimension at least three and codimension at least three.

If \(d\) is even, radical zero is smooth. At radical dimension two, a nonzero restriction of the quadratic form is the square of a nonzero linear form, because the field is perfect. Its projective zero locus in the radical line is one point. At this vertex the local quadratic cone has polar radical dimension one with nonzero square coefficient, which is the odd-variable ordinary form in (LE.3). Zero restriction to the two-dimensional radical imposes two independent conditions on diagonal coefficients; combined with the codimension-one polar rank condition it gives codimension three. Radical dimension at least four has codimension at least six. These bad loci are closed: the higher-radical condition is a matrix-rank condition, and the radical-two zero-restriction locus is closed within that stratum with boundary contained in the higher-radical locus.

Including the zero form in the affine bad cone, its inverse image under ambient restriction has codimension at least three. Projectivizing gives the required closed \(F\) of codimension at least two in \(P_e\), also when \(m=1\). Thus the degree-two case has been covered without replacing it by degree three.

**Choose a line and a transverse axis.** A general line in \(P_e\) avoids \(F\). For \(M\ge2\), lines through a fixed point form a space of dimension \(M-1\), whereas the Grassmannian of all lines has dimension \(2M-2\). The proper incidence of a point of \(F\) on a line has dimension at most \(2M-3\), so its image is a proper closed set. Lines not contained in \(\Delta_e\) also form a nonempty open set.

There is a nonempty open set of pencils with transverse axis. The first-jet calculation shows that a general first section \(H_0\cap X\) is smooth. On that smooth section the same ambient first-jet calculation shows that a general second section is transverse. If \(m=1\), the first section is a finite reduced set and the second can avoid it. Failure of transversality is closed, by the proper incidence where the two equations vanish and their differentials are dependent. It depends only on their two-dimensional span, so descends to a closed condition on the Grassmannian.

The Grassmannian is irreducible: the irreducible group of invertible matrices acts transitively on its points. The three nonempty open conditions therefore intersect. For such a line the singular parameter set is finite, every singular section has one ordinary point, and its axis is transverse. Proposition 1.1 below identifies the total incidence space with the blow-up of the smooth axis and proves that it is regular. Notice also that a singular point cannot lie on the axis, since there the two differentials are independent. This proves existence.

**Why the full Lefschetz locus is open.** We have so far exhibited a nonempty open subset of good pencils. To prove openness of the entire good locus, consider the universal critical scheme of the sections, cut out by their equation and their first derivatives on \(X\). It is proper over \(P_e\). Near a parameter with just one ordinary point it is finite after shrinking the parameter space: remove the proper image of the closed complement of its quasi-finite locus.

The length of its fibre at an ordinary point is \(c=1\), except when \(p=2\) and \(m\) is odd, when it is \(c=2\). For invertible polar Hessian, the derivatives generate the maximal ideal in the completed local ring, giving length one. In the exceptional case, use the \(m-1\) invertible gradient directions to eliminate those variables formally. The remaining equation is \(uz^2+O(z^3)\), with \(u\ne0\); the remaining gradient equation lies in \((z^2)\). Thus the critical algebra is \(k[[z]]/(z^2)\), of length two. Completion preserves this finite length.

Fibre length of a finite scheme is upper semicontinuous: a presentation of its finite module reduces the assertion to ranks of matrices and their minors. Shrink so that total critical-fibre length is at most \(c\), and remove the proper image of its closed nonordinary locus. Every remaining critical point then has length \(c\), so each section has either no critical point or exactly one ordinary point. This proves that the smooth-or-single-ordinary section locus is open. A line avoiding its closed complement, not contained in \(\Delta_e\), and having transverse axis is a Lefschetz pencil; these three conditions are open by the proper point-line and axis incidences just used. Conversely every Lefschetz pencil satisfies them. The entire locus is open.

**The original embedding in characteristic zero.** Apply (LE.2) with \(e=1\), for which first jets are still surjective. If its discriminant has dimension at most \(N-2\), a general line avoids it and all sections in that pencil are smooth. Otherwise the discriminant \(\Delta_1\) is a hypersurface and \(C_1\to\Delta_1\) is generically finite. In characteristic zero this map is generically separable, hence unramified on a nonempty open subset.

The vertical tangent space of this map at \((x,H)\) is the kernel of the Hessian of \(h|_X\): differentiate its gradient equations with the hyperplane held fixed. Generic unramifiedness therefore makes the generic singularity ordinary. There is also only one generic singular point. To see this directly, differentiating the incidence equation \(h(x)=0\) gives \(\dot h(x)=0\), because \(h\) annihilates the tangent space of \(X\). At an unramified point over the smooth locus of \(\Delta_1\), dimension equality identifies its tangent image with \(T_H\Delta_1\). This tangent hyperplane in the hyperplane parameter space is the space of variations annihilating \(x\); it determines the projective point \(x\) uniquely. All unramified points over that same \(H\) consequently have the same \(x\).

Remove the closed images of the ramified locus and the singular locus of \(\Delta_1\); both have dimension at most \(N-2\). Every remaining discriminant section has exactly one ordinary point. A general line avoids these images, and the transverse-axis argument still applies. If \(C_1\) is empty, as for \(X=\mathbf P^N\), no discriminant needs to be avoided. For the sole pencil in \(\mathbf P^1\) this statement is immediate. The openness argument applies unchanged.

Finally, all the constructions and open conditions are defined over the field of definition. A nonempty finite-type open parameter space over a finite field has a closed point, and its residue field is finite by Zariski's lemma. Its pencil is therefore defined over a finite extension. \(\square\)

This proof supplies the full existence scope of Katz, SGA 7 II, XVII, Theorem 2.5. The jet and tangent-incidence comparisons are with §§3.2–3.7 and 4.1–4.3, printed pp.218–240 in the [freely accessible original exposition](https://web.math.princeton.edu/~nmk/old/pinclef.pdf). The characteristic-two quadratic linear-space case was proved above by rank strata. Existence in that characteristic does not by itself prove the higher-dimensional wild Picard–Lefschetz formula; that remains a distinct local calculation.

Define the incidence variety and its projections by

\[
\widetilde X=\{(x,[a:b])\in X\times D:ah_0(x)+bh_1(x)=0\},
\qquad
\pi:\widetilde X\to X,\quad f:\widetilde X\to D.
\tag{1.1}
\]

**Proposition 1.1.** The map \(\pi\) is the blow-up of \(X\) along \(B\), and \(f^{-1}(t)=X_t\). The morphism \(f\) is proper and flat. If \(n\ge1\), it has a section through every \(b\in B(k)\); in this range \(B\) is nonempty.

**Proof.** Off \(B\), the only admissible parameter is \([-h_1(x):h_0(x)]\). Thus (1.1) is the closure of the graph of that rational map. Near \(B\), transversality makes \(h_0,h_1\) a regular sequence after trivializing the hyperplane line bundle. Its Rees algebra has the single relation \(h_1T_0-h_0T_1=0\): the first syzygy of a two-element regular sequence is generated by \((h_1,-h_0)\), and successively comparing homogeneous degrees gives this presentation of the Rees algebra. Substituting \([T_0:T_1]=[-b:a]\) identifies its Proj with (1.1). The two usual blow-up charts are smooth because \(h_0,h_1\) form part of local smooth coordinates. The fibre assertion follows directly from the incidence equation. If \(B\) is empty, the graph is already a morphism and \(\pi\) is an isomorphism.

The incidence is closed in \(X\times D\), so its projection to \(D\) is proper. Its total space is regular and integral, and the pencil map is dominant. A nonzero local parameter of the smooth curve \(D\) is therefore a nonzero divisor in every local ring of \(\widetilde X\) above it. These rings are torsion-free modules over the base DVR, hence flat; this proves flatness of \(f\).

If \(n\ge1\), the first hyperplane divisor has a positive-dimensional projective component. The second hyperplane meets that component: otherwise its section would trivialize the restricted very ample line bundle, while a trivial line bundle on a positive-dimensional projective integral scheme cannot be very ample, since its global regular functions are constant. Thus \(B\ne\varnothing\). For any \(b\in B(k)\), the incidence contains \(\{b\}\times D\), and its projection is the identity on \(D\); this is the required section. In degree zero no section is asserted: a connected finite flat curve pencil of degree greater than one can have none. \(\square\)

Let \(J=\pi^{-1}(B)=\mathbf P(N_{B/X})\), with \(j:J\hookrightarrow\widetilde X\) and \(g:J\to B\). The exact proof homes are Lesson 5, Theorems 1.3 and 1.10c for the projective-bundle and self-intersection formulas, and Smooth traces, duality and Gysin maps, §§11–12 and Proposition 14.1 for smooth-pair purity, codimension-one Gysin maps and projective-space cohomology. Their divisor normalization is the positive Kummer class. These supply the inputs used below.

**Proposition 1.2 (codimension-two blow-up formula).** For all \(r\),

\[
H^r(\widetilde X,\mathbf Q_\ell)
\simeq H^r(X,\mathbf Q_\ell)
\oplus H^{r-2}(B,\mathbf Q_\ell)(-1).
\tag{1.2}
\]

The maps realizing this are \((\pi^*,j_*g^*)\); the formula is compatible with descent and Frobenius when the data are defined over a finite field.

**Proof.** These maps arise from a map of complexes

\[
\mathbf Q_{\ell,X}\oplus
i_*\mathbf Q_{\ell,B}(-1)[-2]\longrightarrow R\pi_*\mathbf Q_\ell,
\qquad i:B\hookrightarrow X.
\tag{1.3}
\]

We check it on geometric stalks by proper base change. Off \(B\), the fibre of \(\pi\) is a point, and the first summand gives an isomorphism. Over \(b\in B\), the fibre is \(\mathbf P^1\); its cohomology is \(\mathbf Q_\ell\) in degree \(0\) and \(\mathbf Q_\ell(-1)\) in degree \(2\). The first summand gives the degree-zero generator. The second restricts to the degree-two generator with a minus sign: \(j^*j_*\) is multiplication by \(c_1(N_{J/\widetilde X})\), and this normal bundle restricts to \(\mathcal O_{\mathbf P^1}(-1)\). The sign is invertible and the map is an isomorphism in degree \(2\). All other stalk cohomology vanishes. Thus (1.3) is a quasi-isomorphism; global cohomology gives (1.2). Pullback, Gysin and proper base change are natural over the field of definition, which proves equivariance. \(\square\)

The other projection has the Leray spectral sequence

\[
H^a(D,R^bf_*\mathbf Q_\ell)\Longrightarrow
H^{a+b}(\widetilde X,\mathbf Q_\ell).
\tag{1.4}
\]

Only \(a=0,1,2\) can occur. We use the resulting filtration and subquotients; (1.4) alone does not justify a claimed degeneration. In degree \(n+1\), the three relevant terms have \(b=n+1,n,n-1\). The middle sheaf \(R^nf_*\mathbf Q_\ell\) contains the varying part of fibre cohomology.

## 2. Local Picard–Lefschetz theory

Let \(R\) be a henselian DVR with algebraically closed residue field, \(T=\operatorname{Spec}R\), generic point \(\eta\), geometric generic point \(\bar\eta\), and closed point \(s\). Let \(f_T:Z\to T\) be proper and flat, with \(Z\) regular of pure dimension \(n+1\), smooth except at one ordinary quadratic point of \(Z_s\). Put \(m=\lfloor n/2\rfloor\). General local Picard–Lefschetz theory attaches

\[
\delta\in H^n(Z_{\bar\eta},\mathbf Q_\ell)(m),
\tag{2.1}
\]

defined up to sign. Specialization is an isomorphism for degrees other than \(n,n+1\), and gives an exact sequence

\[
\begin{aligned}
0\longrightarrow H^n(Z_s,\mathbf Q_\ell)
&\longrightarrow H^n(Z_{\bar\eta},\mathbf Q_\ell)
\xrightarrow{x\mapsto(x,\delta)}\mathbf Q_\ell(m-n)\\
&\longrightarrow H^{n+1}(Z_s,\mathbf Q_\ell)
\longrightarrow H^{n+1}(Z_{\bar\eta},\mathbf Q_\ell)
\longrightarrow0.
\end{aligned}
\tag{2.2}
\]

The pairing is cup product followed by trace. For \(n\) odd, inertia \(I\) acts on degree \(n\) by

\[
\sigma x=x+s_n\,t_\ell(\sigma)(x,\delta)\delta,
\qquad t_\ell:I\to\mathbf Z_\ell(1),
\tag{2.3}
\]

and trivially in other degrees. The character \(t_\ell\) is defined by compatible prime-to-\(p\) roots of a uniformizer; its \(\ell\)-component is surjective. For \(n\) even and \(p\ne2\), let \(\epsilon:I\to\{\pm1\}\) be the unique nontrivial quadratic character. Then

\[
\sigma x=
\begin{cases}
x,&\epsilon(\sigma)=1,\\
x+s_n(x,\delta)\delta,&\epsilon(\sigma)=-1.
\end{cases}
\tag{2.4}
\]

The sign and norm table is:

| \(n\bmod4\) | \(s_n\) | \((\delta,\delta)\) | action of a basic local monodromy on \(\delta\) |
|---|---|---|---|
| \(0\) | \(-1\) | \(2\) | \(-\delta\) |
| \(1\) | \(-1\) | \(0\) | \(\delta\) |
| \(2\) | \(+1\) | \(-2\) | \(-\delta\) |
| \(3\) | \(+1\) | \(0\) | \(\delta\) |

Thus odd relative dimension gives a symplectic transvection; even relative dimension gives an orthogonal reflection. In (2.3), \((x,\delta)\) lies in \(\mathbf Q_\ell(m-n)\); multiplication by \(t_\ell(\sigma)\in\mathbf Q_\ell(1)\), then by \(\delta\in H^n(m)\), removes the twist because \(2m-n+1=0\). In (2.4), \(2m-n=0\). These factors must be retained before choosing bases for constant Tate lines over \(k\).

The calculations below prove the singular stalks, supported generators, norms and even-dimensional variation in every residue characteristic. In residue characteristic two, the even-dimensional formula uses the specific wild quadratic character of (Q.41)–(Q.43), with the same reflection coefficient; uniqueness of a tame quadratic character is not asserted. Proposition PL.C proves the normalized complex coefficient, and Proposition PL.A compares the actual support maps and transfers that coefficient to every regular henselian trait in odd relative dimension, including residue characteristic two. The odd result also permits a separably closed, possibly imperfect residue field, as explained in the normal-form calculation. The full local statement and sign table correspond to Deligne, *Weil I*, (4.1)–(4.4), printed pp.287–289, and SGA 7 II, XV, Theorem 3.4, printed pp.195–196. We first construct the actual nearby/vanishing-cycle triangle, stalk comparison and supported variation.

### The nearby-cycle triangle and variation

We construct the formalism behind the local statement before computing its singular stalk. Work first with \(\Lambda_r=\mathbf Z/\ell^r\). The henselian trait is strictly henselian because its residue field is algebraically closed. Write \(i:Z_s\hookrightarrow Z\) and \(\bar j:Z_{\bar\eta}\to Z\). Define

\[
R\Psi\Lambda_r=i^*R\bar j_*\Lambda_r,\qquad
R\Phi\Lambda_r=\operatorname{Cone}
\bigl(\Lambda_{r,Z_s}\xrightarrow{\mathrm{sp}}R\Psi\Lambda_r\bigr).
\tag{NC.1}
\]

Here \(\mathrm{sp}\) comes from the restriction adjunction. The geometric generic point, and therefore its direct image, has its natural inertia action; the map from the special-fibre constant sheaf is inertia-equivariant with trivial action on its source. Direct images and these maps may be computed by functorial resolutions, or by filtered finite-extension neighbourhoods. The geometric-stalk and finite-data continuity results in [Pushforward, pullback and finite morphisms](course:ag-etale-cohomology/pushforward-pullback-and-finite-morphisms), §§2–4, justify the latter computation. No assertion of constructibility is needed to define the complexes.

**Lemma NC.1.** At a geometric point \(x\) of \(Z_s\),

\[
(R\Psi\Lambda_r)_x
=R\Gamma(Z_{(x)}\times_T\bar\eta,\Lambda_r),
\tag{NC.2}
\]

where \(Z_{(x)}\) is the strict localization. If \(f_T\) is smooth at \(x\), then \((R\Phi\Lambda_r)_x=0\). Properness gives the inertia-equivariant comparison

\[
R\Gamma(Z_s,R\Psi\Lambda_r)
\simeq R\Gamma(Z_{\bar\eta},\Lambda_r).
\tag{NC.3}
\]

For \(\sigma\in I\) there is a variation map
\(\mathrm{Var}(\sigma):R\Phi\Lambda_r\to R\Psi\Lambda_r\) such that, with \(\mathrm{can}:R\Psi\to R\Phi\),

\[
\sigma-1=\mathrm{Var}(\sigma)\,\mathrm{can},
\qquad
\mathrm{Var}(\sigma\tau)
=\mathrm{Var}(\sigma)+\mathrm{Var}(\tau)
+\mathrm{Var}(\sigma)\,\mathrm{can}\,\mathrm{Var}(\tau).
\tag{NC.4}
\]

If the only nonsmooth point is \(x\), the variation factors through the complex of cohomology supported at \(x\).

**Proof.** A geometric stalk of a derived direct image is the cohomology of the source over strict localization: take the filtered system of étale neighbourhoods defining that stalk and a functorial cohomology resolution. Exact filtered colimits and finite-data continuity identify the resulting complex with (NC.2). Universal local acyclicity of smooth maps, proved in [Smooth base change and local acyclicity, Theorem 9.1](course:ag-etale-cohomology/smooth-base-change-and-local-acyclicity), identifies the specialization map there with \(\Lambda_r\to R\Gamma(Z_{(x)}\times_T\bar\eta,\Lambda_r)\) and makes it an isomorphism. Its cone is zero. Consequently \(R\Phi\) is supported at the nonsmooth points.

For (NC.3), put \(a:Z\to T\), \(a_s:Z_s\to s\), and \(a_{\bar\eta}:Z_{\bar\eta}\to\bar\eta\). Proper base change and composition of derived direct images give

\[
Ra_{s,*}i^*R\bar j_*\Lambda_r
\simeq i_T^*Ra_*R\bar j_*\Lambda_r
=i_T^*Rj_{\bar\eta,*}Ra_{\bar\eta,*}\Lambda_r.
\tag{NC.5}
\]

The last stalk is \(R\Gamma(Z_{\bar\eta},\Lambda_r)\), since the strict localization of \(T\) is \(T\) and its geometric generic fibre is \(\bar\eta\). This proves (NC.3); every map was an adjunction or base-change map and hence commutes with the inertia automorphisms. The proper-base-change theorem used here is the lesson [The proper base change theorem](course:ag-etale-cohomology/the-proper-base-change-theorem).

We check variation on cochains, which also fixes its additive law. Choose a functorial complex \(N^\bullet\) computing \(R\Psi\), with its inertia action and equivariant specialization \(A^\bullet=\Lambda_{r,Z_s}[0]\to N^\bullet\). The cone has terms \(N^q\oplus A^{q+1}\) and differential
\((u,v)\mapsto(d_Nu+\mathrm{sp}(v),-d_Av)\). Set

\[
\mathrm{Var}(\sigma)(u,v)=(\sigma-1)u.
\tag{NC.6}
\]

This is a cochain map because \((\sigma-1)\mathrm{sp}=0\). Composing with the cone inclusion gives \(\sigma-1\) on \(N^\bullet\). Expanding
\(\sigma\tau-1=(\sigma-1)+(\tau-1)+(\sigma-1)(\tau-1)\)
gives the second identity in (NC.4), including the intermediate cone inclusion. Thus this is an actual map of complexes, rather than a conclusion drawn only from the long exact sequence.

Finally let \(b:\{x\}\hookrightarrow Z_s\). Since \(R\Phi\) has support there, it is \(b_*b^*R\Phi\). Closed-support adjunction rewrites a map \(b_*b^*R\Phi\to R\Psi\) as \(b^*R\Phi\to Rb^!R\Psi\). Here \(Rb^!\) is the derived closed-support functor: it is computed by taking the subsheaf of sections supported at \(x\) in an injective resolution and restricting to \(x\). The ordinary closed-support adjunction, applied to those resolutions, gives the derived adjunction just used. Its counit factors (NC.6) through \(b_*Rb^!R\Psi\). On global cohomology this is precisely cohomology supported at \(x\). \(\square\)

Taking global cohomology in (NC.1), using (NC.3), yields the full specialization long exact sequence. To reduce it to (2.2), one must still prove that the singular vanishing stalk is a rank-one module concentrated in degree \(n\), identify its supported dual generator, and compute variation with that normalization. Neither (NC.1) nor smooth local acyclicity establishes those three facts. Once they are proved at the finite levels, the compatible coefficient maps and the bounded perfect-complex passage of Lessons 1–2 give their \(\mathbf Z_\ell\) and \(\mathbf Q_\ell\) versions. This construction corresponds to SGA 7 II, XIII, §§2.1.1–2.1.8, printed pp.98–103 in the [freely accessible original](https://publications.ias.edu/sites/default/files/Number12.pdf).

**Lemma NC.2 (finite levels and trait changes at the isolated point).** Keep the proper family of Lemma NC.1 and its one nonsmooth special point \(x\). The complex
\[
V_r=(R\Phi\Lambda_r)_x
\]
has finite cohomology, is bounded and perfect over \(\Lambda_r\), and is compatible with derived coefficient reduction. Its Tor amplitude is contained in \([-1,2n]\), uniformly in \(r\). This assertion concerns the complex; it does not assume that its individual cohomology modules are free.

Let \(T'\to T\) be a morphism of strictly henselian traits taking generic point to generic point and closed point to closed point. Allow an extension of the separably closed residue field, and compute the fibres at geometric points. Choose compatible geometric generic points and let \(x'\) be the resulting point over \(x\). For the base-changed family the natural map
\[
V_r\longrightarrow V'_r
\tag{NC.7}
\]
is a quasi-isomorphism, compatible with the induced inertia homomorphism, specialization, supported variation and coefficient reduction. This includes ramified trait changes. No smoothness of the base-changed total space at \(x'\) is required.

**Proof.** Put \(A_{s,r}=R\Gamma(Z_s,\Lambda_r)\) and \(A_{\eta,r}=R\Gamma(Z_{\bar\eta},\Lambda_r)\). Proper exchange in (NC.3), followed by the triangle (NC.1), identifies the complex
\[
C_r=\operatorname{Cone}(A_{s,r}\longrightarrow A_{\eta,r})
\tag{NC.8}
\]
with \(R\Gamma(Z_s,R\Phi\Lambda_r)\). The cone convention is the one in the proof of NC.1. Smooth local acyclicity places the support of \(R\Phi\) at \(x\); the closed-point extension \(b_*\) is exact and its global sections are the sections on the algebraically closed point. Consequently \(C_r=V_r\), naturally in every map just used.

Here are the coefficient and finiteness inputs precisely. Both geometric fibres are proper of dimension \(n\). Constant coefficients have finite Tor dimension zero. The compact-support coefficient projection and perfectness proof in Lesson 4, Theorems 4.3–4.4, therefore makes both fibre cohomology complexes perfect; properness identifies their compact-support and ordinary operations. The geometric dimension bound and the arbitrary-right-module projection formula place their Tor amplitudes in \([0,2n]\). The constructibility and central finite-coefficient finiteness foundation used by that proof is explicitly recorded there and in Lesson 7, §1. Taking a cone of finite projective models preserves perfectness. Tensoring its cone triangle with an arbitrary \(\Lambda_r\)-module shows the stated interval \([-1,2n]\). Since \(\Lambda_r\) is finite, its bounded finitely generated cohomology groups are finite sets.

For \(u\le r\), apply the same coefficient projection to each fibre. It identifies
\[
\Lambda_u\otimes_{\Lambda_r}^{\mathbf L} A_{s,r}=A_{s,u},
\qquad
\Lambda_u\otimes_{\Lambda_r}^{\mathbf L} A_{\eta,r}=A_{\eta,u}.
\]
The first subscript in \(A_{s,r}\) designates the special fibre; the second designates its coefficient level. These maps commute with specialization by the naturality of the adjunction and proper-exchange maps in NC.1. Taking their cone proves
\[
\Lambda_u\otimes_{\Lambda_r}^{\mathbf L}V_r=V_u.
\tag{NC.9}
\]
Ordinary reduction of the cohomology modules would not prove (NC.9).

For a trait change, proper base change identifies the cohomology complexes of the special geometric fibres. It also identifies those of the generic geometric fibres after the chosen extension of algebraically closed fields. The natural base-change map for nearby cycles comes from the unit on the geometric generic-point square. Composition compatibility in proper base change gives the commutative square
\[
\begin{matrix}
A_{s,r}&\longrightarrow&A_{\eta,r}\\
\downarrow\wr&&\downarrow\wr\\
A'_{s,r}&\longrightarrow&A'_{\eta,r}.
\end{matrix}
\tag{NC.10}
\]
Its horizontal maps are specialization, not arbitrary maps between the two fibre complexes. Taking the cone of this actual square is a quasi-isomorphism. The new family is smooth away from \(x'\) by base change, so its global vanishing complex is its stalk at \(x'\) by the same support argument. This proves (NC.7), including when the new total space is singular.

The geometric generic-point maps respect the chosen inertia actions, and the units defining specialization respect them as well. In the strict cone model (NC.4), the map of cones commutes with \((u,v)\mapsto(\sigma-1)u\). It therefore commutes with variation. Closed-support adjunction is natural, so the factorization through cohomology supported at the point is compatible too. Applying the coefficient projection to this same diagram proves the remaining compatibility. \(\square\)

Lemma NC.2 supplies the actual finite-level control needed for a later quadratic-stalk calculation. It does not compute that stalk's rank, its distinguished supported generator or its Picard–Lefschetz coefficient. Those are additional geometric calculations. Its proper cone proof is the isolated-point argument corresponding to SGA 7 II, XIII, Theorem 2.4.2 and §§2.4.5–2.4.6, printed pp.112–114; the complete argument used here is written above.

### Kummer extension over a regular surface

**Lemma NC.3 (Kummer control over a regular surface).** Let \(A\) be a strictly henselian regular local ring of dimension two, with separably closed residue field, and let \((s,t)\) be a regular system of parameters. Put \(U=\operatorname{Spec}A[1/t]\). Let \(N\ge1\) be invertible in \(A\), and let \(\mathcal M\) be a locally constant sheaf of finite modules on \(U\). Suppose its inertia at the geometric generic point of the divisor \(t=0\) becomes trivial after adjoining \(t^{1/N}\). Then its representation factors through the cyclic Kummer cover
\[
U'=\operatorname{Spec}A[w,1/w]/(w^N-t)\longrightarrow U.
\tag{NC.11}
\]
In particular its pullback to \(U'\) is constant. No assertion of smoothness of a higher-dimensional base is needed here: the dimension-two extension argument is proved below.

**Proof.** Write \(A'=A[w]/(w^N-t)\). The polynomial is Eisenstein at the DVR \(A_{(t)}\), so \(A'\) is a domain and its fraction field has degree \(N\) over that of \(A\). It is finite free over \(A\). Its closed fibre is \(k[w]/(w^N)\), so it is local, with maximal ideal \((s,w)\). It is Noetherian of dimension two and this maximal ideal has two generators; hence it is regular. Being a finite local algebra over the henselian \(A\), it is henselian, and its separably closed residue field makes it strictly henselian. Every \(N\)-th root of unity lifts uniquely from that residue field, since the derivative \(N\) is a unit. Thus \(\mu_N\subset A\), and (NC.11) is a connected cyclic finite étale cover with group \(\mu_N\).

Take the finite frame cover of \(\mathcal M|_{U'}\); if its module is not free over its coefficient ring, use all isomorphisms from one fixed finite module of its locally constant type. Its automorphism group is still finite, so this is a finite étale cover. Normalize \(\operatorname{Spec}A'\) in each of its separable component function fields. These normalizations are finite, with every component dominant. Here is the finite-module argument, so that no geometric finiteness theorem is being hidden. For a separable field extension \(L/K'\), choose a \(K'\)-basis \(u_i\) integral over the normal Noetherian \(A'\). The trace pairing is nondegenerate. Every integral element \(v\) has \(\operatorname{Tr}_{L/K'}(vu_i)\in A'\); these traces are integral and \(A'\) is integrally closed. The integral closure is therefore a submodule of the trace-dual finite free \(A'\)-module of the basis, and is finite by Noetherianity. Localization of this integral closure recovers the given finite étale cover on \(U'\).

The resulting finite normal algebra \(B\) is étale at every height-one point of \(A'\). For a point outside \(w=0\) this holds because the original frame cover is étale. The remaining height-one point is the generic point of \(w=0\). The hypothesis says precisely that its inertia is trivial there. To check its consequence, pass to the strict henselization of its local DVR: the generic finite separable algebra is then a product of copies of the fraction field, whose integral closure is a product of copies of the DVR. This is a finite étale algebra. Étaleness descends from that faithfully flat local extension, proving the claim at the height-one point.

We now prove that no branch can remain at the closed point. Each local ring \(B_{\mathfrak n}\) over the closed point is a normal ring of dimension two, by going down for the normal domain \(A'\) and incomparability in an integral extension. It is Cohen–Macaulay: normality gives Serre's depth bound \(S_2\), which is full depth in dimension two. Its closed fibre over \(A'\) has dimension zero. The actual miracle-flatness proof in [Flatness criteria, dimension and the flat locus](course:AG-FSE/flatness-criteria), Theorem 4.1, applies, since
\[
\dim B_{\mathfrak n}=2=\dim A'+\dim(B_{\mathfrak n}/\mathfrak m_{A'}B_{\mathfrak n}).
\]
It makes these local algebras flat, and consequently makes the finite \(A'\)-algebra \(B\) flat. Over local \(A'\) it is finite free.

Choose a basis and form its trace discriminant \(\Delta\in A'\). It is nonzero because the generic algebra is separable. A finite free algebra is étale exactly where its trace pairing is perfect: over a field a perfect trace pairing excludes nilpotents and inseparable field factors, and hence gives a product of finite separable fields; the fibre criterion then proves finite étaleness. If \(\Delta\) were a nonunit, a prime minimal over \((\Delta)\) would have height one by the principal ideal theorem in the domain \(A'\). This contradicts the already proved étaleness at every height-one point. Therefore \(\Delta\) is a unit and \(B\) is finite étale everywhere.

Since \(A'\) is strictly henselian, \(B\) is a product of copies of \(A'\). The frame cover is trivial, so \(\mathcal M|_{U'}\) is constant. For the connected cyclic cover (NC.11), the image of \(\pi_1(U')\) is the kernel of \(\pi_1(U)\to\mu_N\), by the finite-cover classification. That kernel now acts trivially, which proves the claimed factorization. \(\square\)

For a finite coefficient level of a proper quadratic family over the strict henselization of \(\mathbf Z[T]\) at \((p,T)\), take \(t=T\) and \(N\) a power of \(\ell\ne p\). Once its characteristic-zero local monodromy is computed and shown killed by that Kummer cover, NC.3 determines the same finite representation over the whole complement of \(T=0\). Applying this lemma still requires the actual comparison, the proper family and its distinguished cycle; it does not supply them. Its extension proof is the regular-surface case of branch purity, rather than an unjustified use of the DVR Abhyankar lemma in dimension two.

### Q.1. Quadratic stalks and supported generators

Let \(R\) be a henselian DVR with algebraically closed residue field \(k\), uniformizer \(\pi\), fraction field \(K\), and residue characteristic \(p\). Thus \(R\) is strictly henselian. Fix \(\ell\ne p\), put \(T=\operatorname{Spec}R\), and choose a geometric generic point \(\bar\eta\). Let \(f:Z\to T\) be flat and of finite presentation near a closed point \(x\in Z_s\), of relative dimension \(n\). Assume that \(Z\) is regular at \(x\), the special fibre has an ordinary quadratic singularity at \(x\), and the generic fibre is smooth in the strict germ at \(x\). All statements below are local at \(x\); global properness is required only when mapping the local supported cycle into the cohomology of a proper family.

Work first with \(\Lambda_a=\mathbf Z/\ell^a\). Define \(N=R\Psi\Lambda_a\) and \(V=R\Phi\Lambda_a\) with the unshifted cone convention of Lemma NC.1. Write
\[
L^i=H^i(N_x),\qquad S^i=H^i_x(Z_s,N).
\tag{Q.1}
\]
The second group is cohomology with support at the closed point, computed in any neighbourhood of that point. It is not ordinary cohomology of the geometric generic strict germ.

For \(n>0\), we will prove
\[
L^i=0\ (i\ne0,n),\quad L^0=\Lambda_a,
\qquad S^i=0\ (i\ne n,2n),\quad S^{2n}(n)=\Lambda_a,
\tag{Q.2}
\]
and \(H^i(V_x)=0\) except for a free rank-one module in degree \(n\). The trace pairing
\[
S^n\times L^n(n)\longrightarrow\Lambda_a
\tag{Q.3}
\]
is perfect. If \(n=2r>0\), there are compatible generators
\[
\delta\in S^n(r),\qquad\delta'\in L^n(r),\qquad
\operatorname{Tr}(\delta\cup\delta')=1,
\tag{Q.4}
\]
defined simultaneously up to sign, with
\[
\varphi(\delta)=(-1)^r2\delta',\qquad
\operatorname{Tr}(\delta\cup\varphi\delta)=(-1)^r2.
\tag{Q.5}
\]
Here \(\varphi:S^n\to L^n\) forgets support. Their inertia action is the character of a specific separable Eisenstein quadratic extension of \(K\), including when \(p=2\).

If \(n=2r+1\), the corresponding generators belong to \(S^n(r)\) and \(L^n(r+1)\), have pairing one after choosing their simultaneous signs, and satisfy \(\varphi(\delta)=0\). Inertia fixes both generators. These facts do not determine the odd-dimensional variation coefficient.

For \(n=0\), \(L^0=S^0=\Lambda_a^2\), whereas \(H^0(V_x)=\Lambda_a^2/\Lambda_a(1,1)\) is rank one. The supported dual of that quotient is the trace-zero line \(\Lambda_a(1,-1)\). Conflating the full nearby stalk with the vanishing quotient would give the wrong rank in this case.

### Q.2. Henselian normal forms without a completion comparison

We use two elementary algebraic facts already supplied by [*Étale neighbourhoods, henselization and quasi-finite morphisms*, §§2–5](course:AG-FSE/etale-neighbourhoods-henselization-and-quasi-finite-morphisms): an unramified pointed branch becomes a closed immersion over the henselian ambient germ, and a quasi-finite pointed branch over a henselian local base is a finite local factor. The latter statement is its Lemma 4.1, proved there from algebraic Zariski's Main Theorem. The argument here never passes to a completed trait or invokes invariance of nearby cycles under completion.

Lift \(n+1\) generators of the special-fibre cotangent space to functions near \(x\). They give a morphism to \(\mathbf A_R^{n+1}\) that is unramified at \(x\): its relative differentials generate the cotangent space, so the relative differential module vanishes at the pointed source. The residue field is \(k\). Isolating its quasi-finite branch over the henselian ambient local ring makes it finite and unramified; the unramified splitting statement makes that branch a closed immersion. Consequently the henselian local ring of \(Z\) has a presentation
\[
R\{z_0,\ldots,z_n\}/(F).
\tag{Q.6}
\]
Here braces mean henselization of the polynomial local ring at \((\pi,z_0,\ldots,z_n)\), not a power-series ring. The ambient ring is regular. The kernel has height one and the quotient is the regular local domain of \(Z\), so the kernel is principal. Regular local rings are factorial, giving the displayed equation. The ordinary quadratic hypothesis says that the degree-two part of \(\bar F\) is an ordinary quadratic form after an invertible linear coordinate change and multiplication by a unit. This statement about its initial form follows equally from the definition using the completion, because completion preserves the cotangent space and its associated degree-two relation.

We need an explicit splitting procedure over a henselian ring. Suppose \(A\) is henselian local, its residue field is algebraically closed, and a quadratic form \(q\) on \(A^{2d}\) has invertible polar form and split residue form. Choose a nonzero residue isotropic vector \(\bar v\). At that vector one derivative of \(q\) is a unit, since its polar form is nonsingular. Hensel's implicit-function theorem lifts it to an isotropic vector \(v\). Choose \(w\) with \(B(v,w)=1\), and replace \(w\) by \(w-q(w)v\); the new vector is isotropic and still pairs to one with \(v\). These two vectors span a hyperbolic plane. Its polar orthogonal complement is a direct summand with invertible polar form. Inductively,
\[
q\simeq\sum_{i=1}^d u_iv_i.
\tag{Q.7}
\]
This uses the identity \(q(w-tv)=q(w)-tB(v,w)\) when \(q(v)=0\). It is valid in characteristic two as well as when two is invertible.

For \(n=2r\), choose the special coordinates so that the quadratic initial form is
\[
z^2+\sum_{i=1}^r u_iv_i.
\tag{Q.8}
\]
Its polar form on the \(2r\) coordinates \(y=(u_1,v_1,\ldots,u_r,v_r)\) is nonsingular in every characteristic. Treat \(z\) as a parameter. The equations \(\partial F/\partial y_i=0\) have invertible Jacobian in the \(y\) variables at the closed point. They therefore have a solution \(y=c(z)\) in the henselian ring \(R\{z\}\). Translate \(y\) by that solution. The translated equation has the form
\[
F=g(z)+\sum_{i\le j}a_{ij}(z,y)y_iy_j.
\tag{Q.9}
\]
Indeed its linear terms in \(y\) vanish, so its class modulo \((y)^2\) is \(g(z)\). The coefficients of the remaining quadratic expression may be functions in the whole henselian ambient ring. Its polar matrix is still invertible. Apply (Q.7) over that ring and replace \(y\) by the resulting matrix times \(y\). The derivative of this coordinate map at the closed point is the invertible residue matrix. It is consequently an étale coordinate change and induces an isomorphism of henselian germs. Thus the equation is exactly
\[
\sum_{i=1}^r u_iv_i+g(z)=0,
\qquad \bar g(z)=z^2\times\text{a unit in }k\{z\}.
\tag{Q.10}
\]
Higher-order terms have been removed by algebraic henselian coordinate changes, not by a merely formal change of power-series variables.

Here is the degree-two preparation needed for the remaining function. Put \(D=R\{z\}/(g)\). Since \(\bar g\ne0\), \(\pi\) is a nonzero divisor in \(D\); for example \(R\{z\}\) is a regular factorial domain and \(g\) is not divisible by \(\pi\). The pointed morphism represented by \(D\) is quasi-finite over \(R\), since its closed local fibre is \(k[z]/(z^2)\). Spread the function and its étale coordinates to a finite-type chart. The finite-part lemma over the henselian base isolates a finite local factor \(C\) at that closed point. A finite local algebra over a henselian ring is henselian; its pointed henselization is itself. Therefore \(D=C\). It is flat over the DVR and its closed fibre has length two, hence it is free of rank two.

The images of \(1,z\) form a residue basis. Nakayama makes them an \(R\)-basis of \(D\). Expressing \(z^2\) in that basis gives
\[
D=R[z]/(P),\qquad P=z^2+bz+c,\quad b,c\in\pi R.
\tag{Q.11}
\]
This equality is an isomorphism, since both algebras have the displayed basis. The monic quotient \(R[z]/(P)\) is local and henselian, so its map from \(R\{z\}\) has kernel \((P)\). Hence \((g)=(P)\) in \(R\{z\}\), and \(g=hP\) with \(h\) a unit. Divide (Q.10) by \(h\) and replace each \(u_i\) by \(u_i/h\). We obtain the exact henselian normal form
\[
\boxed{\quad \sum_{i=1}^r u_iv_i+z^2+bz+c=0.\quad}
\tag{Q.12}
\]
When \(r=0\), multiplication of the defining equation by the unit \(h^{-1}\) alone suffices.

Regularity of the total space forces \(v_R(c)=1\). Otherwise the relation in (Q.12) belongs to the square of the ambient maximal ideal, leaving all \(n+2\) cotangent generators independent in a local ring of dimension \(n+1\). Thus \(P\) is Eisenstein. Its generic quadratic algebra \(L=K[z]/(P)\) is a field. Smoothness of the generic strict germ makes \(P\) separable: if it had a repeated geometric root, setting every \(u_i,v_i\) to zero and \(z\) to that root would give a generic singular point specializing to \(x\). Consequently \(L/K\) is a separable, totally ramified quadratic extension.

For \(n=2r+1\), the special quadratic form has nonsingular polar form on all \(2r+2\) variables, also in characteristic two. Solve all gradient equations by Hensel, translate the solution to the origin, and apply the same coefficient-function splitting (Q.7). The normal form is
\[
\boxed{\quad \sum_{i=0}^r u_iv_i+c=0,\qquad v_R(c)=1.\quad}
\tag{Q.13}
\]
The valuation assertion again follows from regularity. These arguments give precisely the local models used below. SGA 7 II, XV, Corollary 1.3.2, printed pp.175–176, supplies the canonical general statement over a henselian base; its printed proof uses Tougeron–Artin and Elkik, XV §§1.1–1.3. The explicit argument above proves the regular-trait normal form used here.

**Odd normal forms over a separably closed residue field.** For odd relative dimension the same proof allows a separably closed, possibly imperfect residue field. Its quadratic space has even dimension and nonsingular polar form. To see that it splits, choose independent vectors \(v,w\) with \(B(v,w)=1\). If \(q(v)=0\), an isotropic vector is already available. Otherwise solve
\[
q(v)T^2+T+q(w)=0.
\]
In characteristic two its derivative is one, so a root belongs to the separably closed field. In other characteristics the polynomial is separable or has a double root already in the field. The vector \(Tv+w\) is nonzero and isotropic. Nonsingularity gives a vector pairing to one with it; the isotropic correction used above splits a hyperbolic plane. Repeat on its nonsingular orthogonal complement. At every lifted isotropic vector, a partial derivative is a unit, so the same Hensel implicit-function argument works over the trait. Thus the odd model is exactly \(\sum u_iv_i=b\), without adjoining purely inseparable roots or assuming a coefficient field in the trait.

The split quadric cells, ruling classes and primitive quotient in Q.3–Q.7 are defined over this residue field. Their cohomology and traces are computed on geometric fibres, so the same support and localization maps give the free odd lines and their generators. Prime-to-residue-characteristic roots of units, roots of unity and finite étale splitting use separable closure and Hensel lifting. Those are the only residual-field properties used for odd variation. In particular this extension covers the imperfect separably closed field of a generic discriminant trait.

### Q.3. Projective quadrics by an explicit cell induction

Let \(Q^d\) be a smooth split projective quadric of dimension \(d\) over an algebraically closed field of characteristic different from \(\ell\). The quadratic equation contains a hyperbolic pair \(uv\). On \(u\ne0\), setting \(u=1\) and solving for \(v\) identifies the open subset with \(\mathbf A^d\). Its complement \(u=0\) is the projective cone on \(Q^{d-2}\), with vertex a point; after removal of the vertex it is a line bundle over \(Q^{d-2}\). Over each affine cell of that smaller quadric the line bundle is trivial. One can see the trivialization directly by choosing a nonzero homogeneous coordinate on that cell and using it to normalize the cone coordinate.

Starting with the vertex and taking the projective cones over a closed filtration of \(Q^{d-2}\) gives a closed filtration of the complement. Its successive strata are affine spaces whose dimensions are one more than those in the smaller quadric. Finally append the open \(\mathbf A^d\). Thus the multiset of cell dimensions obeys
\[
\mathcal C_d=\{0\}\sqcup\{j+1:j\in\mathcal C_{d-2}\}\sqcup\{d\}.
\tag{Q.14}
\]
The bases are \(Q^0\), two reduced points, and \(Q^1\simeq\mathbf P^1\), with cells of dimensions zero and one. For \(d=1\) in characteristic two the tangent hyperplane may have a nonreduced point as intersection; replacing it by its reduction does not change its étale site. Formula (Q.14) is used only from \(d\ge2\).

The smooth-duality chapter, Proposition 14.1, proves
\[
R\Gamma_c(\mathbf A^j,\Lambda_a)=\Lambda_a(-j)[-2j],\qquad
R\Gamma(\mathbf A^j,\Lambda_a)=\Lambda_a.
\tag{Q.15}
\]
Apply compact localization at each step of the finite cell filtration. Induction gives zero odd cohomology. In even degree the sequence is a short exact sequence of free \(\Lambda_a\)-modules; it splits because its quotient is free. Therefore the even groups are free, with rank equal to the number of cells of the corresponding dimension. Projectivity identifies compact and ordinary cohomology. We have proved, rather than assumed, that
\[
H^{2j}(Q^d,\Lambda_a(j))\text{ has rank }1\quad(0\le j\le d),
\tag{Q.16}
\]
except that \(H^{2r}(Q^{2r},\Lambda_a(r))\) has rank two. This works at every finite coefficient level, including \(\ell=2\).

Let \(h=c_1\mathcal O_Q(1)\), with the positive Kummer/Gysin orientation of the supporting smooth-duality chapter, Lemma 12.2. For \(j<d/2\), \(h^j\) is a generator: pair it with the Gysin class of a linear \(\mathbf P^j\subset Q\); the trace is the degree of \(h^j\) on that projective space, namely one. For \(j>d/2\), the class of a linear \(\mathbf P^{d-j}\subset Q\) is a generator, by pairing with the lower power \(h^{d-j}\). These conclusions use the proved rank-one statements and the trace/Gysin compatibility of Proposition 12.1. The embedding \(Q\hookrightarrow\mathbf P^{d+1}\) is a smooth divisor of degree two. Its Gysin class is \(c_1\mathcal O(2)=2H\) by Lemma 12.2, so trace/Gysin compatibility gives \(\operatorname{Tr}_Q(h^d)=2\operatorname{Tr}_{\mathbf P^{d+1}}(H^{d+1})=2\). In upper degrees the identity \(h^j=2\gamma_j\), where \(\gamma_j\) is the linear-space generator, follows by pairing with \(h^{d-j}\). It is an integral identity, not division by two in \(\Lambda_a\).

Now take \(d=2r>0\) and write the split equation as
\[
\sum_{i=0}^r u_iv_i=0.
\tag{Q.17}
\]
Let \(W_J\) be the maximal isotropic subspace spanned by \(v_i\) for \(i\in J\) and \(u_i\) otherwise. Changing two choices connects the corresponding \(\mathbf P^r\)'s by an explicit family: on those two hyperbolic pairs use the span of
\[
s u_i+t v_j,\qquad s u_j-t v_i,
\qquad [s:t]\in\mathbf P^1,
\tag{Q.18}
\]
and keep the other spanning vectors fixed. The vectors have zero quadratic value and pair to zero. They remain independent also at \(s=0\), when they span the two \(v\)'s. This calculation is valid in characteristic two. The resulting projective-space bundle in \(Q\times\mathbf P^1\) gives the same cohomology class at every parameter: its global Gysin class restricts equally at any two points, by the proved projective-line cohomology and Künneth. Thus the class of \(\mathbf P(W_J)\) depends, among these coordinate planes, only on the parity of \(|J|\). Denote the two classes by \(a\) and \(b\), with \(a\) the class for \(J=\varnothing\). No classification of the entire orthogonal Grassmannian is needed for this calculation.

The same two classes cover all maximal planes. For any maximal isotropic \(W\), choose a basis of \(W_\varnothing\) whose initial vectors span \(W\cap W_\varnothing\), and extend it by the dual hyperbolic vectors. Modulo that intersection, projection of \(W\) to the remaining dual coordinates is an isomorphism. Its remaining vectors can therefore be written as \(v_i+\sum_j A_{ji}u_j\), after subtracting their components in the intersection. Isotropy says \(A_{ii}=0\) and \(A_{ij}=-A_{ji}\), including in characteristic two. Replacing \(A\) by \(tA\) connects this plane to the corresponding coordinate plane. A change of basis in \(W_\varnothing\) lifts by its inverse transpose on the dual summand; these changes form the connected group \(\mathrm{GL}_{r+1}\). Families of the resulting planes have constant cycle class: smooth base change makes the cohomology of the product with the fixed proper quadric constant on a connected parameter scheme. Therefore \(W\)'s class is \(a\) or \(b\) according to the parity of \(\dim W/(W\cap W_\varnothing)\). This also makes the primitive quotient of the tangent quadric used in Q.7 intrinsic up to exchanging \(a,b\).

The plane \(W_{\{0,\ldots,r\}}\) is disjoint from \(W_\varnothing\), while \(W_{\{1,\ldots,r\}}\) meets it transversely in one point. At that point their tangent coordinates are the complementary \(u_i\)'s and \(v_i\)'s for \(i>0\), so the intersection multiplicity is one. The positive Gysin orientation gives
\[
\begin{array}{c|ccc}
 &\operatorname{Tr}(a^2)&\operatorname{Tr}(b^2)&\operatorname{Tr}(ab)\\\hline
r\text{ even}&1&1&0\\
r\text{ odd}&0&0&1.
\end{array}
\tag{Q.19}
\]
The identity for \(b^2\) follows by exchanging one \(u_i,v_i\); this is an isometry interchanging the two classes and preserving the trace. The Gram matrix has determinant \(1\) or \(-1\). Since middle cohomology was proved free of rank two, \(a,b\) are a basis over every \(\Lambda_a\).

Restriction of \(h^r\) to either maximal plane is the top hyperplane power on \(\mathbf P^r\). Thus its pairing with both \(a\) and \(b\) is one. Solving for \(h^r\) in the basis \(a,b\), with the invertible Gram matrix (Q.19), gives
\[
h^r=a+b.
\tag{Q.20}
\]
Together (Q.19)–(Q.20) imply
\[
\operatorname{Tr}((a-b)^2)=(-1)^r2,
\qquad \operatorname{Tr}((a-b)a)=(-1)^r.
\tag{Q.21}
\]
This reproduces SGA 7 II, XII, Theorem 3.3, printed pp.75–77, with an explicit proof of the ranks and the parity families used in the norm calculation.

### Q.4. Smooth affine quadrics and their actual forget-support map

Let \(A=Q^n-Y^{n-1}\) be the complement of a smooth hyperplane quadric in a smooth projective quadric. Compact localization and smooth-pair purity give the two triangles
\[
R\Gamma_c(A)\longrightarrow R\Gamma(Q)\longrightarrow R\Gamma(Y),
\qquad
R\Gamma(Y)(-1)[-2]\longrightarrow R\Gamma(Q)\longrightarrow R\Gamma(A).
\tag{Q.22}
\]
All maps use the same positive hyperplane orientation. The natural forget-support map factors through the middle projective cohomology in these triangles.

For \(n=2r>0\), both middle plane classes \(a,b\in H^{2r}(Q,\Lambda_a(r))\) restrict to the class of a linear \(\mathbf P^{r-1}\) in the odd-dimensional quadric \(Y\). That class is a generator. Hence restriction has kernel \(\Lambda_a(a-b)\). The Gysin map from \(H^{2r-2}(Y,\Lambda_a(r-1))\) sends \(h^{r-1}\) to \(h^r=a+b\). In every other non-top positive even degree, restriction is an isomorphism: below the middle it sends a hyperplane power to the same power, and above the middle it sends a linear-space class to its transverse linear hyperplane section. The corresponding Gysin maps are isomorphisms away from the middle as well. Using the vanishing of odd projective cohomology in (Q.22) proves
\[
\begin{aligned}
&H^i(A)=0\ (i\ne0,n),&&H^0(A)=\Lambda_a,\\
&H^i_c(A)=0\ (i\ne n,2n),&&H^{2n}_c(A)(n)=\Lambda_a,\\
&H^n_c(A)(r)=\Lambda_a(a-b),&&
H^n(A)(r)=\bigl(\Lambda_a a\oplus\Lambda_a b\bigr)/\Lambda_a(a+b).
\end{aligned}
\tag{Q.23}
\]
Write
\[
\delta=a-b,\qquad \delta'=(-1)^r[a].
\tag{Q.24}
\]
The compact-to-projective-to-ordinary map sends \(a-b\) to \(2[a]\). By (Q.21), compactly supported cup product with the ordinary quotient has
\[
\operatorname{Tr}(\delta\delta')=1,\qquad
\varphi\delta=(-1)^r2\delta',\qquad
\operatorname{Tr}(\delta\varphi\delta)=(-1)^r2.
\tag{Q.25}
\]
The trace equality follows from the projective intersection pairing, since localization and extension by zero preserve cup product and trace. These are actual generator and map calculations. In particular no inversion of two is used.

For \(n=2r+1\), \(Q\) has rank-one \(H^{2r}\), and \(Y^{2r}\) has middle basis \(a,b\). Restriction sends \(h^r\) to \(a+b\). Its cokernel is the compact middle group, generated by the image of \(a\). The Gysin map sends both \(a,b\) to the same linear-space generator in \(H^{2r+2}(Q)\), so its kernel is \(\Lambda_a(a-b)\). The triangles give
\[
H^n_c(A)(r)=\bigl(\Lambda_a a\oplus\Lambda_a b\bigr)/\Lambda_a(a+b),
\qquad H^n(A)(r+1)=\Lambda_a(a-b).
\tag{Q.26}
\]
The other groups are again only \(H^0(A)=\Lambda_a\) and \(H^{2n}_c(A)(n)=\Lambda_a\). Smooth Poincaré duality, already proved in the supporting chapter's Theorem 10.1, pairs the two free middle lines perfectly. Take \(\delta\) to be the image of \(a\) under the compact boundary map and choose the sign of the ordinary primitive generator \(\delta'\) to make the pairing one. Forgetting compact support is zero, because that map factors through \(H^n(Q)=0\). Thus the supported norm is zero. The boundary-map sign is included in the choice of \(\delta'\); it is not a computation of the odd-dimensional variation coefficient.

For \(n=0\), the smooth quadric consists of two points. Its compact and ordinary complexes are both \(\Lambda_a^2[0]\), with trace the sum and pairing the dot product.

These calculations correspond to SGA 7 II, XII, §§3.5–3.7, printed pp.78–81.

### Q.5. The model has a smooth boundary in every characteristic

Compactify the even normal form (Q.12) to
\[
\mathcal Q:\quad
\sum_{i=1}^r u_iv_i+z^2+bzw+cw^2=0
\quad\subset\mathbf P_R^{2r+1}.
\tag{Q.27}
\]
Its affine open \(w\ne0\) is \(\mathcal A\). Its boundary is
\[
\mathcal Y:\quad w=0,\qquad
\sum_{i=1}^r u_iv_i+z^2=0.
\tag{Q.28}
\]
For \(r>0\), \(\mathcal Y\) is smooth over \(R\). In residue characteristic two the polar radical is the \(z\)-line, but its nonzero projective vector does not lie on the quadric: its quadratic value is \(z^2\ne0\). At every actual boundary point some \(u_i\) or \(v_i\) is nonzero, so one partial derivative is a unit. This also proves that \(\mathcal Q\) is smooth over \(R\) near \(\mathcal Y\), and that the boundary is a smooth relative Cartier divisor there. The special affine fibre is the quadratic cone with its unique vertex \(x\). The generic projective quadric is smooth because \(P\) is separable. For \(r=0\), the boundary is empty.

For odd \(n=2r+1\), compactify (Q.13) by
\[
\sum_{i=0}^r u_iv_i+cw^2=0
\quad\subset\mathbf P_R^{2r+2}.
\tag{Q.29}
\]
The boundary \(w=0\) is the smooth split even-dimensional quadric. The same derivative check gives smoothness near the boundary in every characteristic. Thus both models satisfy the good-boundary hypotheses, even though the special fibre is singular at the vertex.

### Q.6. Good-boundary exchange from localization, not singular purity

Write \(j:\mathcal A\hookrightarrow\mathcal Q\) and \(i:\mathcal Y\hookrightarrow\mathcal Q\). Proper nearby exchange for \(\mathcal Q\), and smooth local acyclicity on a neighbourhood of \(\mathcal Y\), identify the middle and boundary terms in the generic compact localization triangle
\[
j_{\bar\eta,!}\Lambda_a\longrightarrow\Lambda_{\mathcal Q_{\bar\eta}}
\longrightarrow i_{\bar\eta,*}\Lambda_a.
\tag{Q.30}
\]
Apply nearby cycles on \(\mathcal Q\). Proper exchange for the closed boundary and its smoothness identify the third term with \(i_{s,*}\Lambda_a\). Near that boundary the middle term is \(\Lambda_a\). Off the boundary, the first term is the nearby complex \(N\) on \(\mathcal A_s\). Comparing with the special-fibre localization triangle therefore proves
\[
R\Psi_{\mathcal Q}(j_{\bar\eta,!}\Lambda_a)=j_{s,!}N.
\tag{Q.31}
\]

For ordinary cohomology use the generic support triangle
\[
i_{\bar\eta,*}\Lambda_a(-1)[-2]
\longrightarrow\Lambda_{\mathcal Q_{\bar\eta}}
\longrightarrow Rj_{\bar\eta,*}\Lambda_a.
\tag{Q.32}
\]
This purity assertion concerns the smooth generic pair. On a neighbourhood of \(\mathcal Y_s\), the special nearby complex is constant and the special pair is smooth over \(k\), so its supported term is \(i_{s,*}\Lambda_a(-1)[-2]\). The maps agree with specialization. One can verify their orientation either by the extending line bundle \(\mathcal O(\mathcal Y)\) and its supported Kummer class, or by the relative version of the smooth-duality proof: if \(p_{\mathcal Q}\) and \(p_{\mathcal Y}\) are smooth there, composition of their right adjoints gives
\[
Ri^!Rp_{\mathcal Q}^!\Lambda_a=Rp_{\mathcal Y}^!\Lambda_a,
\quad\text{hence }Ri^!\Lambda_a=\Lambda_a(-1)[-2].
\tag{Q.33}
\]
This is the same proof as the supporting Theorem 11.1 with base \(T\), using its already proved relative Theorem 9.1. Its counits and Kummer orientations commute with the generic and special base changes. Comparing the two support triangles proves
\[
R\Psi_{\mathcal Q}(Rj_{\bar\eta,*}\Lambda_a)=Rj_{s,*}N.
\tag{Q.34}
\]
Outside the boundary the comparison is the defining open restriction. No purity statement at the singular vertex has entered this argument.

Now apply proper nearby exchange on \(\mathcal Q\) to (Q.31) and (Q.34). The resulting comparisons are
\[
R\Gamma(\mathcal A_s,N)\simeq R\Gamma(\mathcal A_{\bar\eta},\Lambda_a),
\qquad
R\Gamma_c(\mathcal A_s,N)\simeq R\Gamma_c(\mathcal A_{\bar\eta},\Lambda_a).
\tag{Q.35}
\]
They preserve specialization, cup products, forget-support maps and trace, since they were obtained from the actual localization maps, base-change maps and trace counits. This proves the constant-coefficient, one-divisor case of SGA 7 II, XIII, Proposition 2.1.9 and Lemmas 2.1.10–2.1.11, printed pp.104–106. The more general tame normal-crossing statement is not needed here.

### Q.7. From the cone to the strict-local stalk and supported stalk

We give both comparisons; they play different roles. Let \(C=\mathcal A_s\), its vertex \(x\), and \(\widehat C=\mathcal Q_s\) its projective cone, with boundary \(Y=\mathcal Y_s\).

First,
\[
R\Gamma(C,\Lambda_a)=\Lambda_a[0].
\tag{Q.36}
\]
Scalar multiplication gives a homotopy \(\mathbf A^1\times C\to C\) between the identity and the vertex map. Smooth base change for the projection to \(\mathbf A^1\) identifies its derived direct image with the constant complex \(R\Gamma(C,\Lambda_a)\) on \(\mathbf A^1\). Since (Q.15) gives \(R\Gamma(\mathbf A^1,\Lambda_a)=\Lambda_a\), restriction to either zero or one induces the same map on the pulled-back constant complex. Thus the two homotopic maps induce equal maps on cohomology. The identity factors through the cohomology of the vertex. It follows that every positive group vanishes and the constants are the degree-zero group. Equivalently this is the connected-parameter argument in SGA 7 II, XV, Lemma 2.1.3, printed pp.178–179. The ordinary cohomology of the strict local cone is also \(\Lambda_a[0]\), by the exact-section property of a strictly henselian local scheme.

Smooth local acyclicity shows that the vanishing complex \(V\) on \(C\) is supported at \(x\). Compare the triangle \(\Lambda_a\to N\to V\) under ordinary global sections and under the stalk functor at \(x\). The constant terms are identified by (Q.36), and the vanishing terms are the same complex \(V_x\), because a complex supported at the closed algebraically closed point is its exact closed extension. Therefore
\[
R\Gamma(C,N)\xrightarrow{\sim}N_x.
\tag{Q.37}
\]
Combining (Q.37) with (Q.35) identifies the ordinary nearby stalk with the ordinary cohomology of the entire smooth affine generic quadric. Lemma NC.1 identifies that very same stalk with the cohomology of the geometric generic strict localization. It is (Q.37), not an assertion that the two spaces are geometrically equal, that permits the affine quadric calculation to compute the strict-local stalk.

Second, the natural comparison from closed support to compact support satisfies
\[
R\Gamma_x(C,\Lambda_a)\xrightarrow{\sim}R\Gamma_c(C,\Lambda_a).
\tag{Q.38}
\]
Indeed \(\widehat C-x\) is a line bundle over \(Y\), with the boundary as a section. Homotopy invariance for this line bundle identifies its cohomology with \(R\Gamma(Y,\Lambda_a)\), and restriction to that section is the identification. Homotopy invariance follows on local trivializations from the same smooth-base-change and affine-line calculation used in (Q.36). Compare the support localization triangle for \(x\subset\widehat C\) with the compact localization triangle for \(C=\widehat C-Y\): both have middle term \(R\Gamma(\widehat C,\Lambda_a)\), and their third terms are identified by that restriction. The induced first-term map is precisely (Q.38). Excision identifies the support computed on \(\widehat C\) with support on \(C\).

For \(V\), the corresponding support-to-compact map is an isomorphism directly, since \(V\) is supported at \(x\). Apply the two functors to the vanishing triangle and use (Q.38). We obtain
\[
R\Gamma_x(C,N)\xrightarrow{\sim}R\Gamma_c(C,N).
\tag{Q.39}
\]
Combining with (Q.35) gives
\[
R\Gamma_x(C,N)\simeq R\Gamma_c(\mathcal A_{\bar\eta},\Lambda_a).
\tag{Q.40}
\]
The maps (Q.37) and (Q.40) identify the forget-support map with the compact-to-ordinary map of the smooth affine quadric, and identify their cup/trace pairings. Hence the generator calculation (Q.25), including its sign and factor two, now computes actual supported and ordinary nearby groups. The support group depends only on the strict germ, by closed-support excision. The henselian normal-form isomorphism in Q.2 therefore transfers these calculations to \(Z\).

For a proper \(Z/T\), map the supported group into global nearby cohomology and then use proper exchange (NC.3). The trace pairing is preserved. To check this compatibility after an étale normal-form chart, take a common pointed étale chart for the two germs. Closed-support excision is an isomorphism there; open restriction and étale trace are mates of the same adjunction, and the smooth trace counits commute with their composition, as proved in the supporting smooth-duality §§8–9,12. Thus the supported class's pairing with a global ordinary class is its local pairing with that class's stalk. In particular the global vanishing cycle obtained from \(\delta\) has self-pairing \((-1)^r2\) in positive even dimension. This is the map-based justification for the dual generator used in the global specialization sequence.

For odd \(n=2r+1\), the supported generator also has an intrinsic description, useful when transporting its normalization. Blow up the vertex of the special affine cone. The blowup is the total space of \(\mathcal O_Y(-1)\); its exceptional divisor is the projectivized tangent quadric \(Y^{2r}\). Away from that divisor it is the punctured cone. Its Gysin localization triangle has first map cup product by \(-h\), since the normal bundle of the zero section is \(\mathcal O_Y(-1)\). Thus degree \(2r\) of the punctured cone is the primitive quotient
\[
H^{2r}(Y,\Lambda_a(r))/\Lambda_a h^r.
\tag{Q.40a}
\]
The same statement holds for the punctured strict-local cone. To see the comparison, pull the blowup back to the strict localization. Proper base change identifies the cohomology of that pulled-back blowup with the cohomology of its exceptional fibre \(Y\). Purity for its zero section is obtained by étale localization and continuity from the smooth total space of \(\mathcal O_Y(-1)\); its normal line bundle and Gysin map remain \(-h\). Compare the two Gysin triangles. The middle and supported terms are identified with the same cohomology of \(Y\), and the third-term comparison is therefore an isomorphism. This is an excision argument, not a purity assertion for the original singular cone.

The localization boundary identifies (Q.40a) with \(H^n_x(C,\Lambda_a(r))\). For \(r=0\), the same assertion means the cokernel of the constants \(\Lambda_a\to H^0(Y,\Lambda_a)=\Lambda_a^2\), and is again the primitive quotient. The map
\[
H^n_x(C,\Lambda_a(r))\longrightarrow S^n(r)
\tag{Q.40b}
\]
is an isomorphism: in the supported vanishing long exact sequence its preceding term is \(H^{n-1}(V_x)=0\), and its succeeding map is \(S^n\to H^n(V_x)\). That succeeding map factors as forgetting support followed by the canonical stalk map, and is zero by (Q.26). Consequently the images of the two ruling classes of the exceptional tangent quadric are the two opposite generators of \(S^n(r)\). This defines the odd supported generator intrinsically, independent of a chosen affine compactification. The comparison with the compact boundary generator in Q.4 differs at most by sign: pull both localization boundaries to the projective line bundle \(\mathbf P(\mathcal O_Y\oplus\mathcal O_Y(-1))\), where the zero and infinity sections have Gysin maps \(-h\) and \(+h\). On the primitive quotient the comparison is the identity, with the possible minus sign from rotating a localization triangle. In particular its coefficient is a unit of magnitude one, not an undetermined multiple. This is the independently spelled-out blowup argument in XV §§2.1.4–2.1.8 and 2.2.7, printed pp.179–181,186–187.

For \(n=0\), the cone comparison is simply the finite rank-two algebra calculation. The nearby stalk is \(\Lambda_a^2\), specialization is the diagonal, and the dot product pairs its vanishing quotient with its trace-zero supported line. This gives \(\delta=(1,-1)\), \(\delta'=[(1,0)]\), norm two, and the same factor-two map into the quotient. The full support group remains rank two.

The two displayed comparisons are the precise content of SGA 7 II, XV, Proposition 2.2.3 and §2.2.5(A)–(E), printed pp.183–185. In particular the ordinary comparison goes to the stalk, while the compact comparison goes to cohomology supported at the vertex. The primary page does not identify those two groups with each other.

### Q.8. The inertia character in every positive even dimension

Let \(\alpha,\beta\in\bar K\) be the distinct roots of the Eisenstein polynomial \(P\) in (Q.11). The homogenized binary term factors as
\[
z^2+bzw+cw^2=(z-\alpha w)(z-\beta w).
\tag{Q.41}
\]
Over \(\bar K\), put \(U=z-\alpha w\) and \(V=z-\beta w\). They are independent linear coordinates because \(\alpha\ne\beta\). The generic projective quadric becomes the split equation
\[
\sum_{i=1}^r u_iv_i+UV=0.
\tag{Q.42}
\]
The two coordinate maximal planes that contain the fixed \(u_i\)'s and respectively the \(U\)-line or the \(V\)-line differ by one hyperbolic-pair choice. Thus they give the two middle classes \(a,b\) used above. An inertia element fixing both roots fixes both classes; an element interchanging them exchanges those classes. Consequently
\[
\sigma\delta=\chi(\sigma)\delta,\qquad
\sigma\delta'=\chi(\sigma)\delta',
\tag{Q.43}
\]
where \(\chi:I\to\{\pm1\}\) is the character of \(L/K\). The twists have no further inertia action: every prime-to-\(p\) root of unity lifts uniquely from \(k\) to the strictly henselian DVR.

The extension is separable and quadratic, hence Galois; it is totally ramified because it is Eisenstein. Its character is therefore nontrivial. If \(p\ne2\), completing the square makes it the extension by a square root of an element of valuation one. Every unit of \(R\) has a square root by Hensel's lemma, so it is the unique nontrivial quadratic character, equivalently that of \(\sqrt\pi\). If \(p=2\), the extension of ramification index two is wild. It is this specific character, without an assertion of uniqueness or a replacement by a tame character. In equal characteristic two, separability requires \(b\ne0\); the second root is then \(\alpha+b\). In mixed characteristic two, the distinct-root condition is again exactly the separability of \(P\). All positive even \(n\) are covered by the same binary factor.

This description agrees with the centre-of-even-Clifford-algebra character in SGA 7 II, XV, §2.2.5(D) and Complement 3.2.2, printed pp.185,189: XII §2 identifies that degree-two cover with the two families of maximal planes. For the model used here, (Q.41)–(Q.42) directly identifies that two-family cover with \(\operatorname{Spec}L\), so computing the Clifford algebra is unnecessary.

For odd \(n\), the boundary in (Q.29) is a smooth split even-dimensional quadric over the trait. Proper smooth base change and its extending coordinate planes fix its middle classes \(a,b\). The primitive quotient and primitive part in (Q.26) are therefore fixed by inertia. The maps in Q.6–Q.7 transfer this conclusion to the supported and ordinary nearby generators.

### Q.9. Finite levels, adic passage, and the even variation coefficient

The cell filtrations and the localization triangles above are finite and consist of perfect coefficient complexes. Their cohomology was proved free at every \(\Lambda_a\)-level, with degrees bounded independently of \(a\). The generator classes, positive Gysin maps, trace and comparisons are compatible with coefficient reduction. Tensoring the localization diagrams with \(\Lambda_b\), \(b\le a\), gives the corresponding diagrams at level \(b\). Equivalently, the coefficient projection theorem and Lemma NC.2 give the derived reductions for nearby/vanishing complexes; freeness makes the associated universal-coefficient maps ordinary reduction on these computed groups. In particular the transitions on every nonzero computed line are surjective.

Taking derived inverse limit introduces no extra cohomology: the towers of these finite free lines satisfy Mittag–Leffler, so their first inverse-limit groups vanish. We obtain the same bounded groups over \(\mathbf Z_\ell\), and tensoring with \(\mathbf Q_\ell\) gives the rational version. All maps, inertia actions and cup/trace formulas pass through this limit. No assertion about arbitrary infinite products of cochains is required.

The compatible even supported generator is independent, up to sign, of the normal-form choices. On its free \(\mathbf Z_\ell\)-line, another such generator is \(u\delta\). Intrinsic trace compatibility and (Q.25) give \(2u^2=2\), hence \(u^2=1\) in the integral domain \(\mathbf Z_\ell\), and \(u=\pm1\). Its finite-level generators are the reductions of this compatible integral choice. At an isolated finite \(2\)-power level the norm condition alone would allow extra square roots of one; coefficient compatibility is part of the normalization.

The even variation coefficient is now forced integrally. For \(n=2r>0\), the canonical map \(L^n\to H^n(V_x)\) is an isomorphism, since the special constant stalk has no positive cohomology. Supported variation from NC.1 therefore has the form
\[
\mathrm{Var}(\sigma)(a)=v_\sigma\,\operatorname{Tr}(\delta\cup a)\,\delta.
\tag{Q.44}
\]
The identity \(\sigma-1=\varphi\,\mathrm{Var}(\sigma)\) on the ordinary stalk and (Q.25),(Q.43) give
\[
(-1)^r2v_\sigma=\chi(\sigma)-1.
\tag{Q.45}
\]
In \(\mathbf Z_\ell\), multiplication by two is injective, also for \(\ell=2\). Thus
\[
v_\sigma=(-1)^r\frac{\chi(\sigma)-1}{2},
\qquad
\frac{\chi(\sigma)-1}{2}\in\{0,-1\}\subset\mathbf Z.
\tag{Q.46}
\]
Reduction gives the formula at every finite level. This is how the formula is justified for finite \(2\)-power coefficients; (Q.45) alone at a single such level would not determine it. The global proper formula follows by the supported factorization and local/global trace compatibility in Q.7. When \(\chi(\sigma)=-1\), the coefficient is \((-1)^{r+1}\), and the global cycle has norm \((-1)^r2\), exactly the reflection sign table.

For \(n=0\), the same formula is already the direct two-point permutation calculation, with supported trace-zero generator. For odd \(n\), inertia on the local ordinary line is trivial and the forget-support map is zero. Accordingly the same equation gives no information on the scalar in the variation map. Proving that scalar requires the independent odd-dimensional normalization, not a rank argument. SGA 7 II, XV, §§3.3.3–3.3.7, printed pp.191–195, obtains it by its separate characteristic-zero comparison and specialization argument. Propositions PL.C and PL.A below supply that normalized comparison and transfer proof.

### The normalized complex quadratic calculation

The following calculation proves the local topological coefficient, including its sign. Transferring it to every algebraic henselian trait is a further comparison and specialization step; that step is not inferred from the calculation.

**Proposition PL.C.** Let \(n\ge1\), let \(q(z)=\sum_{i=0}^n z_i^2\) on \(\mathbf C^{n+1}\), and take positive real numbers \(0<a<b\). The compact local fibre
\[
M=\{q(z)=a^2,\ \lVert z\rVert^2\le b^2\}
\]
has a vanishing sphere \(S^n\). Let \(\delta\in H_c^n(M^\circ,\mathbf Z)\) be its normal Thom class, defined up to sign. Use the complex orientation for compact trace. Positive-loop cohomological continuation gives the variation
\[
\operatorname{Var}(x)
=-(-1)^{n(n-1)/2}\operatorname{Tr}(x\cup\delta)\delta,
\qquad
\operatorname{Tr}(\delta\cup\delta)
=(-1)^{n(n-1)/2}(1+(-1)^n).
\tag{PL.C.1}
\]
Here \(x\in\widetilde H^n(M,\mathbf Z)\), and variation takes values in \(H_c^n(M^\circ,\mathbf Z)\). Both groups are free of rank one. For compact cohomology, define \(\widetilde H_c^i=H_c^i\) when \(i\ne2n\), and \(\widetilde H_c^{2n}=\ker(\operatorname{Tr}:H_c^{2n}\to\mathbf Z)\). With this removal of the top trace class, as in SGA 7 II, XIV, §3.2.9, the reduced ordinary and reduced compact groups in other degrees vanish. The full compact cohomology has its orientation copy of \(\mathbf Z\) in degree \(2n\); it is not a vanishing contribution. Reduction of (PL.C.1) gives the same formula for every \(\mathbf Z/\ell^r\), and passage through these free groups gives the integral and rational \(\ell\)-adic formula for this complex model.

**Proof: the fibre and boundary-fixed geometric transport.** Write \(z=x+iy\) with real vectors. The equations are
\[
\lVert x\rVert^2-\lVert y\rVert^2=a^2,
\qquad x\cdot y=0,
\qquad \lVert x\rVert^2+\lVert y\rVert^2\le b^2.
\]
Set \(c=\sqrt{(b^2-a^2)/2}\), \(X=x/\lVert x\rVert\), and \(u=y/c\). They identify \(M\) diffeomorphically with the unit tangent disk bundle of \(S^n\):
\[
\lVert X\rVert=1,\quad X\cdot u=0,\quad\lVert u\rVert\le1,
\qquad
z=\sqrt{a^2+c^2\lVert u\rVert^2}\,X+ic u.
\tag{PL.C.2}
\]
The zero section is the real sphere. Shrinking \(u\) retracts the fibre onto it. The integral Thom isomorphism computes compact cohomology and its pairing with ordinary cohomology.

Over the positive loop \(a^2e^{2\pi i s}\), multiplication by \(e^{\pi i s}\) trivializes the quadratic fibres and ends at \((X,u)\mapsto(-X,-u)\). To compare boundary frames, first transport radially to the central boundary. Above a nonnegative real \(\rho\le a^2\), the boundary vector is
\(A(\rho)X+iB(\rho)\xi\), where
\(A(\rho)=\sqrt{(b^2+\rho)/2}\),
\(B(\rho)=\sqrt{(b^2-\rho)/2}\),
\(\lVert X\rVert=\lVert\xi\rVert=1\), and \(X\cdot\xi=0\).
Radial transport retains \((X,\xi)\) and ends at
\((b/\sqrt2)(X+i\xi)\). On the ray of argument \(2\pi s\), multiply this construction by \(e^{\pi i s}\). Thus rotating a fibre and comparing its central-boundary frame with the initial frame gives the path
\[
G_s(X,\xi)=
(\cos(\pi s)X-\sin(\pi s)\xi,
\ \sin(\pi s)X+\cos(\pi s)\xi).
\tag{PL.C.3}
\]
This comparison uses the equal-length central frame; it does not identify unequal real and imaginary lengths on a noncentral fibre with unit vectors without radial transport.

Correct the rotating-fibre transport on a collar by \(G_s^{-1}\). Choose a smooth nondecreasing \(\chi:[0,1]\to[0,1]\), zero near zero and one near one. Since \(G_s\) is tangent geodesic flow through angle \(-\pi s\), the resulting boundary-fixed geometric fibre transport is
\[
T(X,u)=
\left(\cos\theta\,X+\sin\theta\,\frac u r,
\ -r\sin\theta\,X+\cos\theta\,u\right),
\quad r=\lVert u\rVert,
\quad\theta=-\pi(1-\chi(r)).
\tag{PL.C.4}
\]
Near \(r=0\) this is \((-X,-u)\), and near the boundary it is the identity. Geodesic flow preserves the tangent-bundle equations and \(r\); the inverse has angle \(-\theta\). These facts establish smoothness and invertibility. It preserves orientation, since it is a diffeomorphism of the connected oriented fibre and equals the identity near its boundary.

The positive-loop operator on cohomology is
\(\mathcal M=(T^{-1})^*\), not \(T^*\). A cohomology class continued along a geometric fibre transport is pulled back by the inverse transport. This also matches the inverse-cover convention of SGA 7 II, XIV, §§1.1.4–1.1.7: the positive generator acts on universal-cover points by the inverse deck translation, and transport of functions gives \(\log t\mapsto\log t+2\pi i\). In a horizontal trivialization of the covered family, that deck map is \((v,s)\mapsto(Tv,s-1)\); transport of cochains therefore acts by \((T^{-1})^*\). This fixes the positive Kummer-loop convention.

**Proof: the supported coefficient and its orientation sign.** First use the tangent-bundle orientation \(e'\) given by the ordered blocks \((x_1,\ldots,x_n,u_1,\ldots,u_n)\). Orient \(S^n\), and give its normal tangent fibres the same orientation to define \(\delta\). Let \(F\) be the disk fibre above \(X_0\), cooriented by the oriented tangent space at \(X_0\). Its ordinary Thom class \(\alpha\) has
\(\operatorname{Tr}_{e'}(\alpha\cup\delta)=1\).
Locally the two Thom forms have orders \(dx_1\wedge\cdots\wedge dx_n\) and \(du_1\wedge\cdots\wedge du_n\), so their product has the block orientation. This proves that \(\alpha\) is the ordinary generator dual to \(\delta\).

Fix the Poincaré-dual convention by
\(\int_M\operatorname{PD}_{e'}(C)\cup\beta=\int_C\beta\).
The disk \(F\), oriented by its positive fibre coordinates, has \(\operatorname{PD}_{e'}(F)=\alpha\). For the oriented zero section, however,
\(\operatorname{PD}_{e'}(S^n)=(-1)^n\delta\): putting the normal Thom form before a base \(n\)-form requires \(n^2\) interchanges. This is the sign that must be retained when converting the disk calculation into the normal Thom class.

Since \(T\) is the identity near the boundary, \(\mathcal M\alpha-\alpha\) has compact support after taking the same representative there. Pullback by \(T^{-1}\) transports the cooriented fibre by its inverse image, namely \(T(F)\). Thus its relative Poincaré-dual cycle is the closed difference \(T(F)-F\), not \(T^{-1}(F)-F\).

Parametrize \(F\) by \(u=r\xi\). The projection of \(T(F)\) to \(S^n\) is
\[
\cos\beta(r)X_0-\sin\beta(r)\xi,
\qquad \beta(r)=\pi(1-\chi(r)).
\tag{PL.C.5}
\]
The collar maps constantly to \(X_0\). After collapsing it, the unreflected map with a plus sign before \(\sin\beta\,\xi\) has degree \(-1\): its polar angle decreases from \(\pi\) to zero, and the sphere volume form is
\(\sin^{n-1}\beta\,d\beta\wedge\omega_{S^{n-1}}\), whereas the disk orientation is \(dr\wedge\omega_{S^{n-1}}\). The actual minus sign in (PL.C.5) precomposes that map with the reflection \(u\mapsto-u\), of degree \((-1)^n\). Hence the actual degree is \((-1)^{n+1}\). This argument also applies for \(n=1\), using the boundary orientation of \(S^0\). One can take \(\chi\) strictly increasing between its constant collars; changing the collars is a homotopy.

The projection of \(F\) itself is constant. Projection retracts the disk bundle onto the zero section, so
\(T(F)-F=(-1)^{n+1}[S^n]\).
Its compact dual class is therefore
\((-1)^{n+1}(-1)^n\delta=-\delta\).
Consequently
\[
\operatorname{Var}(\alpha)=-\delta,
\qquad
\operatorname{Var}(x)=-\operatorname{Tr}_{e'}(x\cup\delta)\delta.
\tag{PL.C.6}
\]
The projection of \(T^{-1}(F)\) does have degree \(-1\) in every dimension, but that disk computes \(T^*\), a different cohomological convention. Using it together with \(\mathcal M\), or dropping the sign in \(\operatorname{PD}_{e'}(S^n)\), would reverse the supported coefficient in odd dimension.

The self-intersection of the zero section is the Euler number of its normal tangent bundle, \(1+(-1)^n\). Projecting a fixed nonzero ambient vector onto the tangent spaces gives a tangent vector field with two simple zeros at the poles; its two local indices are \(1\) and \((-1)^n\). Thus
\(\operatorname{Tr}_{e'}(\delta^2)=1+(-1)^n\).

Finally the complex orientation and block orientation satisfy
\[
e=(-1)^{n(n-1)/2}e'.
\tag{PL.C.7}
\]
At the zero section, (PL.C.2) identifies the real and imaginary tangent directions with positive multiples of the base and fibre coordinates. The complex orientation uses \((x_1,u_1,\ldots,x_n,u_n)\); passing from block order requires \(n(n-1)/2\) interchanges. Thus traces differ by this sign. Combining it with (PL.C.6) and the Euler number proves (PL.C.1). Both \(T\) and \(T^{-1}\) restrict to the antipodal map, so ordinary middle monodromy is \((-1)^{n+1}\), consistent with the formula and norm. The integral groups used are free, so reduction and the indicated coefficient limits are exact. \(\square\)

For \(n=2m+1\), the coefficient in (PL.C.1) is \((-1)^{m+1}\), exactly the odd-dimensional coefficient of (2.3) under the positive Kummer-loop convention. For \(n=2m\), it is \((-1)^{m+1}\), with norm \((-1)^m2\). This geometric calculation follows the disk-bundle method in Deligne, SGA 7 II, XIV, §§3.2.2–3.2.11, printed pp.147–151. It proves the complex model; the following proposition supplies the actual algebraic comparison and mixed-characteristic transfer.
If \(\delta\ne0\), the pairing in (2.2) is surjective by duality, so the degree-\(n\) specialization image is \(\delta^\perp\), and the degree-\(n+1\) specialization is an isomorphism. If \(\delta=0\), the middle arrow is zero: an extra special-fibre class appears in degree \(n+1\). This exceptional case is possible only for odd \(n\).

### The odd coefficient over every regular henselian trait

**Proposition PL.A.** Keep the regular-trait hypotheses of §2, allowing a separably closed residue field as in the odd normal-form extension above, and let \(n=2r+1\). With the supported generator \(\delta\) of Q.7, the local supported variation is
\[
\operatorname{Var}(\sigma)(a)
=(-1)^{r+1}c_b(\sigma)\operatorname{Tr}(a\cup\delta)\delta.
\tag{PL.A.1}
\]
Here \(b\) is the smoothing parameter in the normal form \(\sum u_iv_i=b\), and \(c_b\) is its compatible Kummer character. Regularity makes \(b\) a uniformizer times a unit, so \(c_b=t_\ell\). The formula holds first for the compatible integral coefficient tower and then by reduction and rationalization. Mapping supports into a proper fibre gives (2.3). In particular it holds in residue characteristic two.

The proof has four steps. The explicit blowup resolves the complex nodal fibre, so the needed comparison uses proper comparison and smooth-divisor localization. A separate argument supplies a proper degeneration whose global vanishing class is nonzero. Lemma NC.3 transfers its actual finite representations across a regular surface. Finally the local rank-one calculation permits cancellation of that nonzero global class.

**1. Comparison for a proper complex nodal degeneration.** Let a proper algebraic family over a complex curve be smooth away from one ordinary quadratic point of its central fibre. Work in a sufficiently small analytic disk. For a proper algebraic map \(f\), the natural derived comparison
\[
\epsilon^*Rf_*\Lambda_a\longrightarrow Rf^{\mathrm{an}}_*\Lambda_a
\tag{PL.A.2}
\]
is an isomorphism on that disk. Indeed its stalk at each complex point is the proper finite-coefficient comparison for the corresponding proper fibre: algebraic and analytic proper base change give precisely those two fibre complexes. The supporting comparison chapter, Theorem 7.2, proves the fibre comparison by proper induction. A morphism of sheaf complexes inducing all these stalk isomorphisms is a quasi-isomorphism. The comparison arrow is the adjunction/base-change arrow, so it respects the actual restriction and specialization maps. Riemann existence identifies finite monodromy covers on the punctured complex curve; the positive loop is the positive Kummer generator. Cohomological transport is inverse geometric pullback, as checked in PL.C.

We also need compatibility with the distinguished class, rather than only dimensions. Blow up the node of the central fibre. Locally this is the blowup of the quadratic cone: its resolution is the total space of \(\mathcal O_Y(-1)\), where \(Y\) is the smooth projectivized tangent quadric. Globally the resolution is smooth and proper, and its exceptional divisor is \(Y\). Thus ordinary cohomology of the complement is computed by the smooth-divisor Gysin triangle on this proper resolution. Comparison for both proper terms, together with the positive Kummer/Gysin orientation of the supporting comparison chapter §10, identifies that triangle with the analytic one. Comparing it with the support localization triangle on the original proper central fibre identifies the primitive quotient of \(H^{n-1}(Y)\) and its support boundary on both sides. This is exactly the construction (Q.40a)–(Q.40b); no comparison theorem for an arbitrary singular open variety is invoked.

The two ruling classes of \(Y\) are integral topological cycle classes. Their primitive quotient is an integral free line, by the same cell filtration and Gram calculation as Q.3. The resulting supported class on the local smoothing corresponds to the normal Thom class of the vanishing sphere up to sign: the compact boundary quotient in Q.4 is an integral generator, and the tangent-disk description (PL.C.2) has the integral Thom generator. The support-to-compact comparison of Q.7 identifies these generators; its coefficient is \(\pm1\), not an unspecified \(\ell\)-adic unit. Proper comparison respects their cup products and traces, as follows from its naturality and positive smooth Gysin orientation. Reduction gives this compatibility at every finite coefficient level.

For completeness the local geometric operator computes the global operator as follows. Remove a small Milnor tube around the node. On the remaining compact manifold with boundary, the map is a submersion over the whole disk. A vector-field lift of the two base coordinate fields, made tangent to the boundary in its product collar, gives a trivialization over that contractible disk by integration; compactness ensures existence for the required bounded paths. Match its boundary trivialization to the radial central-boundary trivialization of PL.C by a collar isotopy. The resulting geometric positive-loop operator is the identity outside the local tube and is the boundary-fixed operator \(T\) inside. Its inverse pullback difference on cochains is therefore extension of the supported variation computed in PL.C. Excision and trace compatibility give, on global middle cohomology,
\[
\sigma a=a+(-1)^{r+1}c_b(\sigma)
               \operatorname{Tr}(a\cup\delta)\delta.
\tag{PL.A.3}
\]
The other degrees are fixed. The formula applies to finite coefficients as well as integral and rational coefficients: local middle groups and the supported Thom line are integral free, and the cochain/support maps reduce compatibly. The argument does not assume that the global class \(\delta\) is nonzero.

**2. A nonzero proper class without using global conjugacy.** We claim that a complex Lefschetz pencil of smooth degree-\(N\) hypersurfaces in \(\mathbf P^{n+1}\), \(N\ge3\), has at least one nonzero rational vanishing class. It suffices to take \(N=3\). This claim uses the local support calculation, but neither a global conjugacy theorem nor the higher-dimensional Riemann hypothesis.

Write \(f:\widetilde{\mathbf P}^{n+1}\to\mathbf P^1\) for the pencil and suppose every global class were zero. By NC.1 and Q.7 the canonical map from middle cohomology to each vanishing quotient is cup/trace pairing with that class; it is therefore zero. The factorization \(\sigma-1=\operatorname{Var}(\sigma)\operatorname{can}\) makes local inertia trivial on middle cohomology. Its specialization map is an isomorphism in degree \(n\). Normalizing finite frame covers across the missing points, as in Proposition 3.3, extends the rational middle local system across all of \(\mathbf P^1\). The proved absence of connected nontrivial finite étale covers of \(\mathbf P^1\) makes it constant. Likewise \(R^{n-1}f_*\mathbf Q_\ell\) is constant, with fibre generated by \(h^r\), since vanishing stalks occur only in degree \(n\). Weak Lefschetz proves this description of the even lower fibre group.

In Leray, the only possible outgoing differential from
\(H^0(\mathbf P^1,R^nf_*\mathbf Q_\ell)\) is
\[
d_2:H^0(\mathbf P^1,R^nf_*\mathbf Q_\ell)
       \longrightarrow H^2(\mathbf P^1,R^{n-1}f_*\mathbf Q_\ell).
\tag{PL.A.4}
\]
There is no incoming differential and the base has cohomological dimension two. The global hyperplane class \(h^{r+1}\) is a permanent cycle. Cup product with it sends the source to \(H^0(R^{2n+1}f_*)=0\). The differential's derivation property therefore gives \(d_2(a)h^{r+1}=0\).

This last cup map on the target is injective. To include \(n=1\), where the top direct image may have a punctual extra term, construct its trace instead of assuming it is constant. Both the total space and the base are smooth. Composition of their absolute smooth dualizing formulas gives
\(f^!\mathbf Q_\ell=\mathbf Q_\ell(n)[2n]\): apply \(f^!\) to the base formula \(\mathbf Q_\ell(1)[2]\), use composition of right adjoints and the total-space formula, and cancel that invertible twist/shift. The proper counit gives
\[
R^{2n}f_*\mathbf Q_\ell(n)\longrightarrow\mathbf Q_\ell.
\tag{PL.A.5}
\]
On the smooth open set it is the normalized fibre trace. The composite from the constant \(R^{n-1}\), multiplying by \(h^{r+1}\) and applying (PL.A.5), is multiplication by
\(\int_{X_u}h^n=N\). Equality holds over the whole base because both source and final target are constant and their morphism is determined on the dense open set. Consequently the composite on \(H^2\) is the nonzero scalar \(N\), proving injectivity. It follows that (PL.A.4) is zero.

Thus this nonzero constant middle group would survive into \(H^n(\widetilde{\mathbf P}^{n+1})\). But the complete blowup formula of Proposition 1.2 gives
\[
H^n(\widetilde{\mathbf P}^{n+1})
=H^n(\mathbf P^{n+1})\oplus H^{n-2}(B)(-1)=0.
\tag{PL.A.6}
\]
Here the axis \(B\) is a smooth complete intersection of two degree-\(N\) hypersurfaces, of even dimension \(n-1\). The weak-Lefschetz and complete-intersection deformation proof, §§1–2, whose inputs are affine vanishing and smooth duality and not purity or pencils, gives \(H^{n-2}(B)=0\); for \(n=1\) this is negative-degree cohomology.

The smooth hypersurface middle group is indeed nonzero. Over \(\mathbf C\), projection of the degree-\(N\) Fermat hypersurface to \(\mathbf P^n\) is an \(N\)-sheeted cover off the degree-\(N\) Fermat branch hypersurface and has one point over it. Euler characteristic with compact supports is additive; a finite covering of a finite cell decomposition multiplies it by its number of sheets. Starting with \(\chi_0=N\) therefore gives
\[
\chi_n=N(n+1)-(N-1)\chi_{n-1}
=n+2+\frac{(1-N)^{n+2}-1}{N}.
\tag{PL.A.7}
\]
Weak Lefschetz and duality give the projective-space ranks outside the middle. For odd \(n\),
\[
b_n=n+1-\chi_n
=\frac{(N-1)^{n+2}-(N-1)}{N}>0.
\tag{PL.A.8}
\]
Every smooth degree-\(N\) complex hypersurface has these ranks: its nonempty smooth locus in the projective coefficient space is connected, and smooth proper base change, or its analytic submersion trivialization, gives rank constancy. This contradicts (PL.A.6) and proves the claim.

**3. Transfer across a regular surface.** Fix a residue prime \(p\ne\ell\), including \(p=2\), and let \(S_1\) be the strict henselization of \(\mathbf Z_{(p)}\). Choose a degree-three Lefschetz pencil on \(\mathbf P^{n+1}_{\overline{\mathbf F}_p}\), using the proved Theorem 1.0. Lift its two defining sections to \(S_1\). Its axis and its blown-up total space remain smooth over \(S_1\). The critical scheme is finite étale over \(S_1\). To verify this assertion, use local coordinates \(y_1,\ldots,y_{n+1}\) and pencil parameter \(t\). The equations for a critical point are \(F=0,F_{y_i}=0\). Their Jacobian in \((t,y)\) has determinant \(F_t\det(F_{y_i y_j})\), a unit at every special critical point: regularity gives \(F_t\ne0\), and odd \(n\) gives a nonsingular polar matrix even when \(p=2\). Thus the critical scheme is étale there. It is proper, and its special fibre is finite, so it is finite; the closed bad loci for étaleness, axis smoothness or additional singularities have empty special fibre and hence are empty over the local base. Every critical point is therefore a section over the strictly henselian \(S_1\).

Embed the finite algebraic-number field of a characteristic-zero model in \(\mathbf C\). Step 2 supplies a critical section with nonzero rational global class. Localize the parameter surface at its special point and take its strict henselization \(S\). Completing the square is unnecessary: the all-variable Hensel splitting of Q.2 works over this henselian surface ring because the polar matrix is invertible. The equation of the pointed germ is exactly \(\sum u_iv_i=b\). Since \(F_t\) is a unit, \(b\) is an étale parameter on the surface. Hence
\[
S\simeq\operatorname{Spec}(\mathbf Z[b]_{(p,b)})^{\mathrm{sh}},
\qquad U=S-\{b=0\}.
\tag{PL.A.9}
\]
The pulled-back proper family is smooth on \(U\), and has precisely this one ordinary node over the divisor \(D=\{b=0\}\).

Its distinguished odd class is compatible along \(D\) and extends to a section on \(U\). Here are the maps ensuring this, so that nonvanishing is not merely assumed to survive specialization. Blow up the singular section of \(Z_D\). The resolution and its exceptional quadric are smooth proper over \(D\); the two ruling classes extend, and their primitive quotient is the constant rank-one line. The actual support boundary followed by the global support map defines \(\delta_D\) in \(R^nf_{D,*}\Lambda_a(r)\). The proper blowup-excision triangle expresses \(Rf_{D,*}\Lambda_a\) using the resolution, exceptional quadric and singular section; all these proper smooth terms have coefficient-compatible lisse cohomology. Over the strictly henselian trait \(D\), their specialization isomorphisms commute with the boundary and ruling classes. Thus \(\delta_D\) at its generic point is the specialization of its closed-point value.

A strictly henselian local étale topos has exact global sections: an étale covering of its final object has a branch through the closed point and a section by the henselian finite-branch lemma. Proper base change consequently gives
\(R\Gamma(Z,\Lambda_a)=R\Gamma(Z_s,\Lambda_a)\).
Lift the closed class uniquely through this isomorphism. Restriction to \(Z_D\), and then to \(Z_U\), gives a class whose value along the divisor is the preceding \(\delta_D\), and whose values on \(U\) form a section \(\delta_U\) of the finite lisse direct image. The same constructions commute with coefficient reduction; they define the integral tower. No constancy of the singular direct image on all of \(S\) is assumed.

At the generic point of \(D\), step 1 gives the finite monodromy formula (PL.A.3). Its rank-one nilpotent has square zero because the supported norm is zero. Thus adjoining \(b^{1/\ell^a}\) kills this monodromy on \(R^nf_*\Lambda_a\); it kills the already trivial monodromy in all other degrees. Lemma NC.3 applies to each of these finite lisse modules on \(U\), including modules that are not free. It makes their pullbacks constant on the connected Kummer cover and factors their representations through \(\mu_{\ell^a}\). The matrix of that cyclic representation is determined at the geometric generic divisor point. Its formula there therefore determines it at every geometric point of \(U\), with the same Kummer character.

Cup product, relative smooth trace and the section \(\delta_U\) are morphisms of these local systems. They commute with the constancy identifications, so the transported formula is exactly (PL.A.3), with its pairing and distinguished class, at all those points. Passing through the compatible finite systems gives the rational formula. The chosen class was nonzero in the characteristic-zero rational fibre. It remains nonzero in every rational fibre over \(U\): a nonzero integral class is detected at some finite level, and constancy on each connected Kummer cover preserves that detection and all its compatible multiples. Equivalently choose an étale path between the two geometric fibre functors, together with compatible roots of \(b\); its isomorphisms on all finite systems identify the integral classes and hence their rationalizations.

**4. Determining and transporting the local scalar.** Over any regular strictly henselian trait, Q.7–Q.8 give free integral lines for the local vanishing quotient and its supported dual, with trivial odd inertia. Supported variation is a cocycle by NC.1; on these trivial lines it is an additive homomorphism. At finite level its scalar homomorphism lies in
\[
H^1(K,\Lambda_a(1))=K^\times/K^{\times\ell^a}
=\mathbf Z/\ell^a,
\tag{PL.A.10}
\]
generated by a uniformizer. The first equality is the Kummer sequence; every unit has an \(\ell^a\)-th root by Hensel's lemma and the separably closed residue field, which proves the last equality. Therefore, with the cup order \(a\cup\delta\) used in PL.C, variation has the form
\[
\operatorname{Var}(\sigma)(a)
=\lambda\,c_b(\sigma)\operatorname{Tr}(a\cup\delta)\delta,
\qquad\lambda\in\mathbf Z_\ell.
\tag{PL.A.11}
\]
The compatible scalar exists by coefficient reduction; freeness of the computed local lines ensures ordinary reduction, as proved in Q.9. This statement retains the odd cup-order sign: \(\operatorname{Tr}(\delta\cup a)=-\operatorname{Tr}(a\cup\delta)\).

Map the reference surface family to a trait by sending \(b\) to any uniformizer times a unit and choosing the residue-field embedding. For residue characteristic \(p\), the universal property of strict henselization gives this map from (PL.A.9), because a strictly henselian residue field contains a chosen \(\overline{\mathbf F}_p\). The geometric generic fibre is a point of \(U\). Step 3 supplies the nonzero global \(\delta\) and the global formula (PL.A.3). Map (PL.A.11) into that proper cohomology. The local/global trace compatibility of Q.7 identifies its pairing with the global pairing. Smooth proper rational duality gives a global class pairing nontrivially with \(\delta\), and the Kummer character is surjective. Comparing the two formulas and cancelling that nonzero class determines
\(\lambda=(-1)^{r+1}\).

The pulled-back reference germ and an arbitrary given odd quadratic germ over that trait are isomorphic by the exact henselian normal form Q.2. Étale excision identifies their nearby stalks, supported groups, canonical and variation maps. The intrinsic ruling construction Q.7 identifies their generators up to sign; the formula is unchanged by replacing both occurrences of \(\delta\) by their negatives. The compatibility of these maps with trait change is the actual cone/support naturality of NC.1–NC.2, rather than an identification of named tame generators. It transfers the determined scalar to the given germ.

For residue characteristic zero, choose the reference complex pencil and node over an algebraic-number field. Its local normal form and maps descend to that field. An embedding of its algebraic residue closure in the given separably closed residue field lifts to the henselian trait by the étale Hensel criterion. Send the smoothing coordinate to \(b\). Proper geometric-fibre base change and the same local excision transfer (PL.A.3) and its nonzero class; the cancellation just made applies verbatim. This avoids any assumption that the whole field \(\mathbf C\) embeds in the trait. Finally changing \(b\) by a unit does not change its Kummer character, since those units have compatible prime-to-residue-characteristic roots. This proves (PL.A.1) and the full odd local formula. \(\square\)

This proof reconstructs the comparison/specialization route of SGA 7 II, XV, §§3.3.3–3.3.7, printed pp.191–195. Its two-dimensional Kummer extension is proved in NC.3. Its nonzero-cycle step is supplied above using the actual Leray cup/trace map and the elementary Fermat Euler recurrence; no unproved global conjugacy statement is used to obtain it. The only topological and comparison foundations are those expressly retained in the supporting proper-comparison chapter.

## 3. Degree-zero local and global theory in every characteristic

### A ramified double point

**Proposition 3.1.** Let \(R\) be a henselian DVR with algebraically closed residue field \(k\) of characteristic \(p\), let \(K=\operatorname{Frac}R\), and let \(\ell\ne p\). Suppose \(Z\to\operatorname{Spec}R\) is proper and flat, \(Z\) is regular and pure of dimension \(1\), and the morphism is smooth of relative dimension \(0\) except at one special point. Suppose the local special-fibre algebra at that point has length \(2\) and is \(k[z]/(z^2)\). No restriction on \(p\) is imposed.

The exceptional local factor is

\[
C=R[z]/(z^2+a z+b),\qquad
a,b\in\mathfrak m_R,\quad v_R(b)=1.
\tag{3.1}
\]

Its fraction field \(L/K\) is a separable, totally ramified quadratic extension. Let \(\epsilon:I\to\{\pm1\}\) be the character of this particular extension. The ramified geometric generic fibre has two points, with coordinate functions \(e_+,e_-\). Put \(\delta=e_+-e_-\). Then

\[
(\delta,\delta)=2,\qquad
\sigma x=
\begin{cases}
x,&\epsilon(\sigma)=1,\\
x-(x,\delta)\delta,&\epsilon(\sigma)=-1.
\end{cases}
\tag{3.2}
\]

Every other generic point is fixed. Specialization sends the exceptional special point to \(e_++e_-\), and yields the entire exact sequence

\[
0\longrightarrow H^0(Z_s,\mathbf Q_\ell)
\longrightarrow H^0(Z_{\bar\eta},\mathbf Q_\ell)
\xrightarrow{x\mapsto(x,\delta)}\mathbf Q_\ell
\longrightarrow0.
\tag{3.3}
\]

Both fibres have zero cohomology in all positive degrees. If \(p\ne2\), the character is tame and is the unique nontrivial quadratic character, attached to \(\sqrt t\) for a uniformizer \(t\). If \(p=2\), it is wild; neither its uniqueness nor its description by the tame character is asserted.

**Proof.** First reduce the whole proper family. At a special-fibre point, a uniformizer of \(R\) is a nonzero divisor by flatness. In its one-dimensional regular local ring its quotient has dimension zero. The generic fibre is smooth of relative dimension zero. Thus all fibres are zero-dimensional, the morphism is quasi-finite, and properness makes it finite. Its algebra is finite torsion-free, hence free over the DVR.

Henselian decomposition splits this algebra into local factors indexed by its special-fibre points. Each nonsingular factor is finite étale, and therefore is \(R\): a finite étale algebra over this strictly henselian ring splits into copies of \(R\). The algebraic decomposition criterion and the finite étale equivalence are the written prerequisites in [*Étale neighbourhoods, henselization and quasi-finite morphisms*](course:AG-FSE/etale-neighbourhoods-henselization-and-quasi-finite-morphisms), §2 and Theorem 5.2.

The exceptional factor \(C\) has free rank \(2\), because its reduction has length \(2\). Lift the residue coordinate \(z\) to its maximal ideal. Nakayama makes \(1,z\) an \(R\)-basis of \(C\). Expressing \(z^2\) in this basis gives (3.1) with \(a,b\in\mathfrak m_R\). The monic quotient maps isomorphically to \(C\), since both have that basis. If \(b\in\mathfrak m_R^2\), its defining relation lies in \((t,z)^2\), so the maximal ideal of \(C\) has two independent cotangent generators. That contradicts regularity in dimension one. Hence \(b=t u\) with \(u\) a unit. Write \(a=t c\); the relation gives

\[
t(u+c z)=-z^2.
\tag{3.4}
\]

The factor \(u+c z\) is a unit. Consequently \(C\) is a DVR with uniformizer \(z\), and \(v_C(t)=2\). The polynomial in (3.1) is Eisenstein, so its generic algebra is a field of degree \(2\). Smoothness of the generic fibre makes that extension separable. Every separable quadratic extension is Galois. Since the residue field is algebraically closed, its two embeddings are interchanged by inertia, and it has ramification index \(2\).

When \(2\) is invertible in \(R\), completing the square gives
\((z+a/2)^2=a^2/4-b\). The right side has valuation \(1\). Every unit of \(R\) has a square root by Hensel's lemma, so rescaling gives \(w^2=t\). Every element of \(K^\times\) is a uniformizer power times a unit; therefore \(K^\times/K^{\times2}\) has exactly two classes. This proves the tame character and its uniqueness for \(p\ne2\). For \(p=2\), the ramification index \(2\) is divisible by the residue characteristic, so this quadratic extension is wild. Its character is defined by its two embeddings, without choosing a tame generator. This argument also covers mixed characteristic with residue characteristic \(2\).

Let there be \(r\) nonsingular factors. The special fibre has \(r+1\) geometric points and the geometric generic fibre \(r+2\). The étale site of a finite scheme over an algebraically closed field is that of its reduced finite set: nilpotents do not change étale covers, and each point has only split étale covers. Thus constant-sheaf cohomology is the coordinate module in degree zero and vanishes in positive degrees. A function on a special point pulls back to the same value at every generic point of that factor. This is the specialization map, independently of any higher-dimensional vanishing-cycle theorem. On \(C\) it is the diagonal map, and on the other factors it is the identity.

The trace pairing in degree zero is the dot product. Hence \((x,\delta)\) is the difference of the two ramified coordinates, and (3.3) is exact. Subtracting \((x,\delta)\delta\) interchanges those coordinates. This is precisely the nonidentity inertia permutation, proving (3.2) and the norm. The same coordinate calculation proves (3.2)–(3.3) for constant finite \(\ell\)-power coefficients; in particular it remains valid at \(\ell=2\) when \(p\ne2\). \(\square\)

For \(p\ne2\), \(\operatorname{Spec}R[z]/(z^2-t)\) is a finite proper example. Its special fibre has length \(2\), but one geometric point, whereas its generic fibre has two geometric points. Length and geometric cardinality give different answers here.

### The characteristic-two conductor

**Proposition 3.2.** In equal characteristic \(2\), take \(R=k[[t]]\) and the exceptional factor (3.1). Generic smoothness forces \(a\ne0\). If \(h=v_R(a)\), its quadratic character has Swan conductor \(2h-1\).

**Proof.** In characteristic \(2\), the derivative of the monic polynomial is \(a\), so separability is equivalent to \(a\ne0\). Its other root is \(z+a\), and the nonidentity automorphism satisfies \(\sigma(z)-z=a\). Since \(z\) is a uniformizer and \(v_C(t)=2\), we get

\[
v_C(\sigma(z)-z)=v_C(a)=2h.
\tag{3.5}
\]

For the lower ramification groups, \(G_i\) consists of automorphisms with
\(v_C(\sigma(q)-q)\ge i+1\) for every \(q\in C\). It suffices to test a uniformizer: here completeness identifies \(C=k[[z]]\), and the difference of any power series at \(z+a\) and \(z\) is divisible by \(a\). The test at \(q=z\) attains equality. Thus \(G_i=G\) for \(0\le i\le2h-1\), and \(G_i=1\) afterwards. The Swan conductor is, by definition,
\(\sum_{i\ge1}(|G_i|/|G_0|)\operatorname{codim}(\mathbf Q_\ell(\epsilon)^{G_i})\).
Each of its first \(2h-1\) terms is \(1\), and the rest vanish.

Equivalently, \(y=z/a\) satisfies \(y^2+y=b/a^2\), whose pole has odd order \(2h-1\). The family \(z^2+t^h z+t=0\), for every \(h\ge1\), is regular, has this smooth quadratic generic fibre, and has the same length-two special fibre. These examples prove that the conductor is unbounded even though the vanishing coordinate has dimension \(1\). \(\square\)

The wild reflection therefore has the same matrix and norm as the tame degree-zero reflection, but a different ramification character. Substituting the tame \(t_\ell\) in characteristic \(2\) would lose this action.

### Global monodromy for a pencil on a curve

**Proposition 3.3.** Let \(k\) be algebraically closed of any characteristic, and let \(f:X\to D=\mathbf P^1_k\) be the morphism of an axis-free Lefschetz pencil on a smooth projective connected curve. Let its degree be \(d\), let \(S\) be its singular parameters, and put \(U=D-S\). A smooth fibre is a set \(\Omega\) of \(d\) points. Its geometric monodromy group is the full permutation group \(\operatorname{Sym}(\Omega)\).

Let \(E_0\subset H^0(X_u,\mathbf Q_\ell)=\mathbf Q_\ell^\Omega\) be the span of **all monodromy transports** of the local differences \(\delta_s\). Then

\[
E_0=\left\{(x_i)_{i\in\Omega}:\sum_i x_i=0\right\},\qquad
H^0(X_u,\mathbf Q_\ell)^{\pi_1(U)}
=E_0^\perp=\mathbf Q_\ell(1,\ldots,1).
\tag{3.6}
\]

Its pairing is nondegenerate and, if \(d>1\), \(E_0\) is absolutely irreducible. Furthermore
\[
f_*\mathbf Q_\ell=j_*j^*f_*\mathbf Q_\ell,\qquad
R^qf_*\mathbf Q_\ell=0\quad(q>0).
\tag{3.7}
\]
For \(d=1\), the map is an isomorphism, \(S\) is empty, and \(E_0=0\).

**Proof.** The curve is integral, and \(f\) is finite flat: its nonconstant map has zero-dimensional fibres, and a finite torsion-free module over a smooth curve's local DVR is free. Over \(U\) it is finite étale. Its connected total space gives a transitive action on \(\Omega\), by [*The étale fundamental group*](course:AG-DFG/AG-DFG-05), Theorem 1.3 and §2. Let \(G\subset\operatorname{Sym}(\Omega)\) be its finite image. Proposition 3.1 shows that inertia at each singular parameter has image generated by one transposition, including in characteristic \(2\).

We justify why those images normally generate \(G\); tameness is unnecessary for this step. Let \(N\) be the normal subgroup generated by every local inertia image. The connected finite étale cover of \(U\) with group \(G/N\) extends to a finite étale cover of \(D\). Here is the extension argument. Normalize \(D\) in its function field. This normalization is finite: on a normal affine coordinate ring \(A\), choose an integral field basis \(\alpha_i\) for the finite separable extension. The trace matrix is invertible over \(\operatorname{Frac}A\). Every integral element \(\beta\) has \(\operatorname{Tr}(\beta\alpha_i)\in A\), since traces of integral elements are integral and \(A\) is normal. The integral closure is therefore contained in the finite trace-dual \(A\)-module of the basis; its being a submodule and \(A\)'s being Noetherian prove finiteness. On a strict henselian local DVR at a puncture, trivial inertia makes the generic algebra a product of copies of the fraction field. Its integral closure is the product of copies of the DVR itself. Thus the normalization is étale at every puncture. These local descriptions glue with the original cover over \(U\), as in the normal-scheme description in the same prerequisite, §4.

The written all-characteristic projective-line computation in that prerequisite, Proposition 5.1, proves that \(D\) has no nontrivial connected finite étale cover. Its proof uses
\(\Omega_{Y/k}=g^*\Omega_{D/k}\) for an étale cover \(g:Y\to D\) of degree \(r\), whence \(2g(Y)-2=-2r\), so \(r=1\). Consequently \(G/N=1\), and \(G\) is generated by transpositions.

Make a graph with vertex set \(\Omega\) and an edge for each generating transposition. The orbits of the generated group are exactly the connected components: generators preserve components, and adjacent swaps move a vertex along any path. Transitivity makes the graph connected. Edge transpositions of a connected graph generate all transpositions. Indeed, if swaps \((i,j)\) and \((j,k)\) are available, conjugating the latter by the former gives \((i,k)\); induction along a path gives a swap between any two vertices. All permutations are products of transpositions. Hence \(G=\operatorname{Sym}(\Omega)\).

For \(d>1\) there is at least one singular parameter, since otherwise \(X\to D\) itself would be a nontrivial connected finite étale cover. The symmetric group transports any local difference to every \(e_i-e_j\), up to sign. Those differences span exactly the sum-zero subspace. The fixed coordinate vectors are exactly the constant vectors, giving (3.6). The constant vector has norm \(d\ne0\) in \(\mathbf Q_\ell\), even if \(\ell\mid d\), so its orthogonal complement has nondegenerate pairing.

After any extension of the characteristic-zero coefficient field, a nonzero sum-zero vector \(w\) has two distinct coordinates \(w_i,w_j\). For any stable subspace containing it,
\[
w-(i,j)w=(w_i-w_j)(e_i-e_j)
\]
puts a difference vector in that subspace. Symmetric-group translates then span all of \(E_0\). This proves absolute irreducibility. Finally, at a singular parameter Proposition 3.1 identifies specialization with the inertia-invariant coordinate module. This gives the first assertion of (3.7) on every stalk; proper base change and the positive-degree vanishing for finite geometric fibres give the second. \(\square\)

In this wild statement the span includes all transports, or equivalently all choices of paths. Normal generation by inertia does not say that one fixed inertia group at each parameter generates \(G\). This distinction prevents a tame generator assertion from being used in characteristic \(2\).

**Example.** In characteristic \(2\), the degree-two map
\[
\mathbf P^1_z\longrightarrow\mathbf P^1_t,\qquad t=\frac{z^2}{z+1}
\tag{3.8}
\]
is the axis-free pencil given by the sections \(s^2\) and \(sr+r^2\) of \(\mathcal O_{\mathbf P^1}(2)\). They have no common zero. Its fibre at \(t=0\) is one length-two point, locally \(z^2+t z+t=0\), with Swan conductor \(1\). For finite \(t\ne0\), the derivative of this polynomial with respect to \(z\) is \(t\), so the fibre is reduced. At infinity the two fibre points are \(z=1,\infty\), both simple poles of \(t\). The total curve is smooth, so this is a degree-zero Lefschetz pencil with just one singular parameter. Its group is \(\operatorname{Sym}_2\) and its vanishing line is the sign representation. Such a one-branch-point example is possible because its quadratic inertia is wild.

## 4. Global invariants and the vanishing quotient

Return to the pencil under the general characteristic restriction stated in §1, put \(U=D-S\), and fix a geometric point \(u\in U\). The excluded degree-zero case in characteristic \(2\) has already been treated separately in Proposition 3.3. Write
\[
H=H^n(X_u,\mathbf Q_\ell)(m),\qquad
E_{\mathrm{van}}=\operatorname{span}_{\mathbf Q_\ell}\{\delta_s:s\in S\}.
\tag{4.1}
\]
We use \(E_{\mathrm{van}}\) to distinguish this space from a coefficient field. Its pairing takes values in \(\mathbf Q_\ell(2m-n)\); choose a basis of this constant line for scalar linear algebra over \(k\).

We prove the global statements under the canonical restriction

\[
p\ne2\quad\hbox{or}\quad n\text{ is odd}.
\tag{G.1}
\]

The characteristic-two even-dimensional case is excluded from this tame argument; Proposition 3.3 separately treats degree zero in every characteristic.

### The local operator and its Kummer normalization

The local theorem of §2 is now proved: NC.1–NC.3 construct and compare the actual specialization cone and supported variation, Q.1–Q.9 calculate its generators and even variation, and PL.C–PL.A determine the odd coefficient over regular henselian traits. With \(m=\lfloor n/2\rfloor\), put \(H=H^n(X_u,\mathbf Q_\ell)(m)\). Its perfect cup-and-trace pairing \(b\) takes values in the constant line \(L=\mathbf Q_\ell(2m-n)\), preserved by geometric monodromy. For the fixed sign \(s_n\) of §2, the complete operator identities are

\[
\begin{array}{ll}
n\text{ odd}:&\rho(\sigma)-1=s_n t_\ell(\sigma)
 \bigl(x\mapsto b(x,\delta_s)\delta_s\bigr),\\
n\text{ even},\ p\ne2:&\rho(\sigma)-1=s_n
 \bigl(x\mapsto b(x,\delta_s)\delta_s\bigr)
 \quad\text{when the quadratic character is }-1.
\end{array}
\tag{G.2}
\]

In other degrees the local action is trivial. The odd formula kills wild inertia because \(t_\ell\) factors through tame inertia. The even quadratic character has order two prime to \(p\), so it too kills wild inertia. Thus every finite reduction of a monodromy-stable lattice is tame. Lesson 1 supplies such a lattice for a continuous representation of a profinite group. The following proofs use these operators with their common Kummer normalization and the specialization sequence (2.2).

### The generic discriminant trait has the required local normalization

The strict henselization at the generic discriminant has separably closed, possibly imperfect residue field. It must not be mistaken for an algebraically closed residue field. The following bounded reduction allows us to use the local theorem stated with algebraically closed residues.

**Lemma.** Let \(A\) be a strictly henselian equal-characteristic DVR, with separably closed residue \(k_0\). In positive characteristic there is a henselian DVR extension \(A\subset A_\infty\), with the same uniformizer \(\pi\), whose fraction-field extension is algebraic purely inseparable and whose residue is algebraically closed. Under the resulting isomorphism of absolute Galois groups, inertia and all prime-to-\(p\) Kummer characters of \(\pi\) agree.

**Proof.** If a residue element \(a\) is not a \(p\)-th power, lift it to a unit \(v\in A\), and adjoin \(z\) with \(z^p=v\). The polynomial is irreducible generically: a generic root would be a unit whose residue is a root of \(T^p-a\), a contradiction. Its residue polynomial is irreducible too. The finite free local ring \(A[z]\) has maximal ideal generated by \(\pi\), residue \(k_0(a^{1/p})\), and dimension one; it is a DVR with index one. It is henselian, being a finite local algebra over a henselian ring.

Repeat this construction whenever a residue \(p\)-th root is still missing, and take unions at limit stages. Do not adjoin a unit root when its residue root is already present: that unnecessary extension could introduce ramification. Every stage retains the value group \(\mathbf Z\) and uniformizer \(\pi\). The union valuation ring is again a DVR: every nonzero ideal is generated by an element of its least valuation. It is henselian, since the coefficients and simple residue root of any Hensel problem occur at a finite stage. Its residue is the perfect closure of \(k_0\), which is algebraically closed since \(k_0\) was separably closed. Its fraction-field extension is algebraic purely inseparable.

Finite étale field categories, hence absolute Galois groups, are unchanged by a purely inseparable extension, by AG-DFG's written universal-homeomorphism invariance, Theorem 1.2 of the proper-schemes lesson. Both residue fields are separably closed, so inertia is the entire absolute Galois group on both sides. The equations \(z^e=\pi\), \(e\) prime to \(p\), are unchanged, with the same roots of unity. They identify the Kummer characters and the tame quotient. In characteristic zero a separably closed field is already algebraically closed. \(\square\)

Apply this to the equal-characteristic generic discriminant trait. The proper family's geometric generic and closed fibres are unchanged, using the same algebraic closures. The specialization square, cone and variation are compatible by Lesson 9, Lemma NC.2. The distinguished supported quadric generator is compatible with this field base change by its blow-up and Gysin construction; its remaining ambiguity is the same sign. Regularity of the total family is preserved in the case at hand. Away from the quadratic point it is smooth. At that point the special fibre still has embedding dimension \(n+1\); the base uniformizer lies in the square of the maximal ideal, since its ordinary equation has no linear term. Flatness over the index-one DVR gives dimension \(n+1\) for the total local ring, and quotienting by this uniformizer leaves its embedding dimension \(n+1\). Thus the total local ring is regular. The nonsingular polar form makes the unique critical point rational over the separably closed residue field (its gradient equations are étale there).

The local theorem over \(A_\infty\) therefore gives exactly (G.2) over the original trait, with the same inertia and \(t_\ell\). In particular it kills wild inertia there and implies genuine tame ramification, including separability of the boundary residue extensions. This proves the required normalization at a generic discriminant trait. In odd relative dimension PL.A already applies directly to its separably closed residue field; the index-one extension above also covers the positive even case when the residue characteristic is not two.

### Cover-theoretic prerequisites and their actual proof homes

The following already written programme proofs suffice. No étale fundamental-group Lefschetz theorem for an affine complement is imported.

1. [*Specialization maps and tame ramification*](course:AG-DFG/AG-DFG-07), §5, Theorem 5.1, proves the DVR Abhyankar lemma by writing \(\pi=wq^e\), adjoining a prime-to-\(p\) root of \(\pi\), and replacing the remaining extension by the étale unit-root algebra \(Z^e-w\). Its §§4 and 6 prove the Kummer model and permanence under subextensions, composition and base change.
2. [*Purity of the branch locus*](course:AG-LCL/AG-LCL-07), Theorems 2.2, 3.2 and 4.1, proves that a finite normal dominant cover of a regular scheme, generically étale and étale in codimension one, is étale everywhere. The surface proof uses normality, miracle flatness and the discriminant. The higher-dimensional proof uses the written [local finite-cover Lefschetz theorem](course:AG-LCL/AG-LCL-05), Theorem 3.2, cuts with a regular parameter and inducts. The pointwise branch theorem is then proved by induction. The local full-faithfulness proof uses [Formal geometry](course:AG-LCL/AG-LCL-04), Lemma 3.2. These provider proofs retain their precisely stated henselian-pair equivalence and finite formal-gluing foundations.
3. [*Fundamental groups of proper schemes and the homotopy exact sequence*](course:AG-DFG/AG-DFG-06), Theorem 2.1, proves finite étale lifting over a complete Noetherian local base, with all maps, by nilpotent invariance, coherent existence and the graph argument. Its Theorem 5.1 proves that the component algebra of a proper flat family with geometrically reduced fibres is finite étale and commutes with base change. All lifting schemes below are projective: coherent existence has the full preceding proof in [*Grothendieck's existence theorem*](course:AG-QC/grothendiecks-existence-theorem), §§3–5, Theorem 5.1. A complete mixed-characteristic DVR with residue \(k\) is constructed in [*Coefficient rings and the Cohen structure theorem*](course:AG-CA/AG-CA-19S), Theorem 4.1.

The complex punctured-sphere computation is written in [*Comparison with the topological fundamental group over the complex numbers*](course:AG-DFG/AG-DFG-08), §6.1, and §5 identifies the profinite completion. Its general finite-type Riemann existence equivalence in §4 is expressly a permitted analytic comparison input; it is not reproved here. The component-algebra proof retains general proper henselian finite étale equivalence and perfect proper flat coherent base change, with their exact open Stacks proof locators. The projective lifting here uses the fully written projective existence proof. General Riemann existence is the same expressly stated analytic comparison foundation retained in [Comparison with singular cohomology](course:ag-etale-cohomology/comparison-with-singular-cohomology). These declarations do not claim a recursive proof of every foundational input.

### Local Kummer charts along a smooth divisor

**Lemma.** Let \(V\) be smooth over \(k\), and \(Z\subset V\) a smooth divisor. Let \(E\to V-Z\) be a finite étale cover tame at the generic points of \(Z\). Étale locally on \(V\), its normalization over \(V\) is a disjoint union of maps

\[
\operatorname{Spec}A[w]/(w^e-t)\longrightarrow\operatorname{Spec}A,
\qquad e\text{ prime to }p,
\tag{G.3}
\]

where \(t=0\) defines \(Z\). It is tame on every transverse curve through \(Z\). The same assertion holds over a regular mixed-characteristic base when every relevant index is invertible there.

**Proof.** Work at a strict henselian local ring \(A\) of \(V\), with \(t\) a regular parameter. Choose \(a\), invertible in \(A\), divisible by every generic ramification index. The required roots of unity lie in \(A\). Set \(B=A[z]/(z^a-t)\). It is regular: replacing \(t\) by \(z\) gives a regular system of parameters, or the corresponding smooth local chart over the indicated base. It is finite, local, strictly henselian, with the same residue field as \(A\).

Normalize \(B\) in the reduced generic pullback of the cover. This normalization is finite, by excellence in the present finite-type setting, or the finite separable trace bound in AG-LCL, Proposition 1.2. It is étale at codimension-one points away from \(z=0\). At \(z=0\), DVR Abhyankar makes it unramified, hence étale. Every component dominates \(B\), and its generic field is separable. The finite branch-purity criterion in AG-LCL, §4, makes the normalization finite étale over \(B\). Strict henselianity splits it as a finite set of copies of \(B\).

The group \(\mu_a\) acts on this normalization through \(z\mapsto\zeta z\) and a permutation of its copies. Recover the original normalization by taking invariants. On generic algebras this is finite Galois descent; on finite algebras it is uniqueness of integral closure, since the invariant algebra is normal and integral over \(A\), with the original generic algebra. For an orbit of the copies the invariants are \(B^J\), where \(J\subset\mu_a\) stabilizes one copy. If \(|J|=h\), then \(B^J=A[w]/(w^{a/h}-t)\), with \(w=z^h\). This proves (G.3). The splitting and its finite equations spread from the strict henselization to an ordinary étale neighbourhood. A transverse curve pulls \(t\) back to a unit times a uniformizer; that unit acquires an \(e\)-th root strictly locally, so the same Kummer character occurs. \(\square\)

The orientation is part of this construction. If \(t'=vt\), an \(a\)-th root of the unit \(v\) gives \(z'=v^{1/a}z\). This change commutes with \(\mu_a\). It does not replace the tame character by an arbitrary unit multiple.

### Normal generation and selected generators

**Lemma (ordinary normal generation).** For \(U=\mathbf P^1_k-S\), the closed normal subgroup of \(\pi_1(U,u)\) generated by its boundary inertia groups is the whole group.

**Proof.** A finite quotient killing boundary inertia gives a finite cover unramified at the deleted points. Normalize \(\mathbf P^1\) in its finite covering fields. The strict henselian DVR test extends it étale across each deleted point. [*The étale fundamental group*](course:AG-DFG/AG-DFG-05), Proposition 5.1, makes that cover trivial: a connected degree-\(d\) étale cover has canonical degree \(2g-2=-2d\), so \(d=1\). Every finite quotient of the quotient by the closed normal subgroup is trivial. Finite quotients separate elements of a profinite group. \(\square\)

This proof permits arbitrary conjugates of inertia groups. It does not choose one path at each deleted point whose groups generate as an ordinary closed subgroup. It supplies no tame assertion for the characteristic-two degree-zero example with one wild branch point.

**Proposition (selected tame generators).** There are compatible paths at the points \(s\in S\) such that the images

\[
\widehat{\mathbf Z}^{(p')}(1)\longrightarrow
\pi_1^t(U/\mathbf P^1,u)
\tag{G.4}
\]

generate topologically. The source is the product of \(\mathbf Z_q(1)\) for \(q\ne p\), and is \(\widehat{\mathbf Z}(1)\) in characteristic zero. The target classifies **all** finite covers tame at \(S\); it is not asserted to be the maximal prime-to-\(p\) quotient. Its finite quotients may have order divisible by \(p\).

**Proof in positive characteristic.** If \(|S|\le1\), the differential order of a tame branch of index \(e\) is \(e-1\): writing \(t=vu^e\) gives \(dt=u^{e-1}(ev+uv')du\), whose last factor is a unit. Canonical degrees therefore give the tame Riemann–Hurwitz formula. With no branch point it forces degree \(d=1\). With one branch point and \(r\ge1\) points above it, it gives \(2g-2=-d-r\), again forcing \(d=1\). The tame group is trivial.

Suppose \(|S|=r\ge2\). Put one member at infinity and write the others \(a_1,\ldots,a_{r-1}\). Choose a complete Cohen DVR \(R\) with residue \(k\), lift these points to distinct sections \(\widetilde a_i\), and lift \(u\) to a section avoiding them. For each \(a\) prime to \(p\), normalize \(\mathbf P^1_R\) in

\[
z_i^a=t-\widetilde a_i,\qquad 1\le i<r.
\tag{G.5}
\]

This is a smooth projective curve \(Y_a/R\) with action of \(G_a=\mu_a^{r-1}\). Roots of unity lift uniquely by henselianity. Its degree is \(a^{r-1}\): before adjoining \(z_i\), the earlier unit-root equations are unramified at \(t=\widetilde a_i\); its valuation remains one, so the next equation is Eisenstein at each such DVR and has degree \(a\). Induction proves the degree and connectedness.

Here is the smoothness check. Off the sections the equations are finite étale. At \(\widetilde a_i\), use \(z_i\) as relative parameter; the other unit-root equations are étale. At infinity, put \(q=1/t\) and take \(v^a=q\). The ratios \(z_i/z_1\) satisfy unit-root equations, and \(z_1v\) is a root of the unit \(1-\widetilde a_1q\). These give charts étale over the relative parameter \(v\), with index \(a\). They identify the normalization there. Finiteness of normalization and these monic charts give a finite map to the projective line, hence projectivity; the quotient by \(G_a\) is \(\mathbf P^1_R\).

Take a connected Galois cover \(C\to U\), with group \(G\), tame at \(S\), and compactify by normalization. Choose \(a\) divisible by every index. The normalized pullback \(C'_k\to(Y_a)_k\) is finite étale by DVR Abhyankar and carries commuting actions of \(G\) and \(G_a\). AG-DFG Theorem 2.1 lifts it to a finite étale \(C'_R\to Y_a\). It lifts both actions: lift the relevant isomorphisms, including \(g^*C'_k\simeq C'_k\) for the base automorphisms in \(G_a\); full faithfulness lifts all relations, commutation identities and equivariant maps. The finite quotient \(C_R=C'_R/G_a\) is formed on affine inverse images of \(\mathbf P^1_R\) by invariant algebras. Invariants commute with reduction, since \(|G_a|\) is a unit and averaging is a splitting. Its special fibre is the original normalization, and the \(G\)-action survives.

Strictly locally at a branch section, \(C'_R\) is a set of copies of the Kummer chart. Quotienting an orbit gives the chart with base parameter \(w^e\), \(e\mid a\), as in the local lemma. Thus \(C_R\) is smooth over \(R\), normal, proper and étale off the sections. The finite étale component algebra of a proper smooth family shows that a connected special-fibre cover has connected geometric generic fibre.

Its geometric generic cover is Galois with this same group \(G\). The finite map is flat by the local charts (or miracle flatness for the smooth source over the regular surface), so its degree remains \(|G|\). A deck transformation becoming the identity generically would be the identity on the normal model, hence on the special fibre. The action is faithful; degree \(|G|\) proves the Galois assertion. Off the branch sections, descent from the \(G_a\)-torsor proves étaleness. At those sections the same Kummer charts identify its inertia subgroups with those of \(C\), up to \(G\)-conjugacy.

The geometric generic cover, its \(G\)-action and its finitely many marked branch points descend to one finitely generated characteristic-zero field. Embed that field in \(\mathbf C\). The descended cover is geometrically connected: if it split over an algebraic closure of its field of definition, its extension to the original algebraically closed field would split too. Thus the complex cover is connected and has the same \(G\)-action and local cyclic inertia subgroups. This uses finite-presentation descent of one cover, not a claim that the entire generic field embeds in \(\mathbf C\).

The complex punctured-sphere proof supplies one path per branch point whose meridians generate the finite monodromy group \(G\). Its positive meridian is the Kummer character on \(z^a=t-s\). Hence there are conjugates of the specified special-fibre inertia subgroups, one per \(s\), that generate \(G\). In characteristic zero the same conclusion follows directly by descending the cover and marked points to a finitely generated field and applying the complex computation; no mixed-characteristic lift is required.

Finally one must choose paths **simultaneously for all finite quotients**. Put \(\Gamma=\pi_1^t(U/\mathbf P^1,u)\), and start with any fixed inertia paths and closed images \(J_s\subset\Gamma\). For a finite quotient \(q\colon\Gamma\twoheadrightarrow G\), let

\[
C_G=\{(g_s)_{s\in S}\in\Gamma^S:
 \langle q(g_s)q(J_s)q(g_s)^{-1}:s\in S\rangle=G\}.
\tag{G.6}
\]

It is a clopen, nonempty subset of the compact \(\Gamma^S\), by the finite-cover argument just proved and the ability to lift conjugators from \(G\). A finite collection of these conditions is met by the condition for their common finite quotient. Compactness gives a tuple in every \(C_G\). Change the original path at \(s\) by this \(g_s\). The closed subgroup generated by the resulting inertia images maps onto every finite quotient of \(\Gamma\), hence equals \(\Gamma\): a proper closed subgroup would have a proper image in some finite quotient. These are the compatible paths (G.4), proving the assertion. \(\square\)

Covers with \(p\)-torsion in their groups were lifted as **étale covers of \(Y_a\)**. Only the auxiliary Kummer group had prime-to-\(p\) order. There is no prime-to-\(p\) restriction on the global tame group.

### A transverse line captures tame monodromy

**Proposition.** Let \(\Delta\subset P=\mathbf P^r_k\), \(r\ge2\), be an irreducible reduced hypersurface. Let \(\Delta^\circ\subset\Delta\) be a nonempty smooth open. Suppose a line \(D\subset P\) meets \(\Delta\) only in \(\Delta^\circ\) and transversely. Fix \(u\in D-\Delta\). Let \(\Pi\) classify covers of \(P-\Delta\) tame at the generic point of \(\Delta\). Then

\[
\pi_1^t(D-D\cap\Delta\,/D,u)\twoheadrightarrow\Pi.
\tag{G.7}
\]

**Proof.** Let \(T\subset\mathbf P^{r-1}\) be the open set of lines through \(u\) meeting \(\Delta\) only in \(\Delta^\circ\), transversely. It is nonempty, contains \(D\), and is integral. Its universal line is the restriction of \(B=\operatorname{Bl}_uP\to\mathbf P^{r-1}\), a \(\mathbf P^1\)-bundle whose exceptional divisor is the section \(u\). The relative intersection with \(\Delta\) is finite étale over \(T\): finiteness follows from projectivity and finite fibres; the Jacobian condition is transversality.

Take a connected tame cover \(E\to P-\Delta\), and normalize \(P\) in its field, obtaining a finite normal integral \(\overline E\to P\). Blow up \(\overline E\) at its finite fibre over \(u\), obtaining an integral normal \(\widehat E\). Its map to \(B\) is finite. Away from \(u\) it is the original finite map; near \(u\) the cover is étale, blow-up commutes with flat base change, and the induced map is finite étale. Normality follows on these same opens. Each point of \(E_u\) is \(k\)-rational and gives an exceptional divisor mapping isomorphically to that of \(B\), hence a section of \(\widehat E\to\mathbf P^{r-1}\).

The map \(\widehat E_T\to T\) is smooth and proper. Off the boundary it is étale over the smooth universal line. At the boundary the local Kummer lemma writes its cover as \(w^e=t\) after étale localization. Because the boundary is étale over \(T\), \(t\) is a relative parameter; replacing it by \(w\) gives a smooth relative curve chart. This proves smoothness there too. The finite cover of the proper universal line proves properness.

Let \(K=k(T)\). The generic fibre is integral, since it is the generic localization of the integral total scheme, and is a smooth proper \(K\)-curve. An exceptional section gives it a \(K\)-point. Its global-functions algebra is a finite extension field of \(K\); evaluation at the point embeds it in \(K\), so it equals \(K\). Flat field base change gives \(H^0(\widehat E_{\overline K},\mathcal O)=\overline K\), excluding a nontrivial idempotent. The geometric generic fibre is connected, and smoothness makes it integral.

The proper smooth component theorem makes the component algebra finite étale over the connected \(T\). Its rank is one generically, hence one everywhere. The fibre above \(D\) is smooth and connected, hence integral. Removing its finite boundary leaves the connected nonempty open \(E\times_P(D-D\cap\Delta)\). Every connected tame cover remains connected on the given line. Pullback is tame by the Kummer lemma, so the connected-cover criterion proves (G.7). \(\square\)

This is the required bounded fundamental-group Lefschetz argument for the **given transverse line**, not just a generic line. It uses no lift of \(X\), hard Lefschetz or nondegeneracy condition on the vanishing subspace.

### Oriented inertia homomorphisms are conjugate

**Lemma.** In the preceding setting, identify local tame inertia with \(I^t=\widehat{\mathbf Z}^{(p')}(1)\) using compatible Kummer roots. Its homomorphisms \(I^t\to\Pi\) at any two geometric points of \(\Delta^\circ\) are conjugate, after choices of paths to \(u\). This preserves the Kummer character; it is not only conjugacy of image subgroups.

**Proof.** Pass first to a finite quotient \(G\) and its Galois cover. Choose \(a\) killing its generic boundary indices. Strictly locally on \(\Delta^\circ\), the Kummer lemma trivializes the normalized root pullback. Inertia is a homomorphism \(\mu_a\to G\), determined up to conjugacy by a point of the Galois fibre.

Its conjugacy class is locally constant on \(\Delta^\circ\). The finite étale algebra after the root pullback, its finite components, and its \(G\)- and \(\mu_a\)-actions spread to an étale neighbourhood, where a trivialization gives the same action on every geometric fibre. A different fibre point conjugates the homomorphism in \(G\). A different divisor equation changes its root by a unit root, commuting with \(\mu_a\); it introduces no power automorphism of \(\mu_a\). Thus the finite set of conjugacy classes gives a locally constant function on the connected \(\Delta^\circ\). It is constant.

For each finite quotient \(G\), let \(C_G\subset\Pi\) be the closed set of elements conjugating the two homomorphisms in \(G\). It is nonempty because a conjugator in \(G\) lifts to \(\Pi\). Any finite collection has nonempty intersection by passing to their common finite quotient. Compactness gives a point of \(\bigcap_G C_G\). Finite quotients separate elements, so it conjugates the homomorphisms themselves. \(\square\)

This supplies the compatibility needed in SGA 7 XVIII, Proposition 6.1.2. Irreducibility makes the smooth divisor connected; Kummer charts give the same oriented inertia. Equality of monodromy ranks supplies neither fact.

### Application to the actual discriminant and pencil

Let \(P=(\mathbf P^N)^\vee\), and let \(\Delta\) be its reduced dual discriminant. The conormal incidence is a projective bundle over the integral \(X\), by Lesson 9's first-jet calculation. It is integral, so its proper image \(\Delta\), when nonempty, is irreducible.

Suppose \(S\ne\varnothing\). Restriction (G.1) makes the polar Hessian at each ordinary point invertible: there are \(n+1\) variables, an even number in the allowed characteristic-two case. Its kernel is the vertical tangent space of the conormal incidence over \(P\), hence is zero. Étale locally, the gradient equations solve uniquely for a critical point \(x(H)\). The discriminant equation is

\[
F(H)=h_H(x(H))=0.
\tag{G.8}
\]

Its derivative in a variation \(\dot h\) is \(\dot h(x_s)\); variation of \(x(H)\) contributes zero because it is critical. Some ambient linear form has nonzero value at \(x_s\), so this derivative is nonzero. The discriminant is therefore a hypersurface smooth there. Uniqueness of the critical point persists after shrinking: the proper critical incidence is finite near the given fibre, and the closed complement of the neighbourhood of its unique point has proper image which can be removed. This is the finite critical-scheme argument in the existence proof.

There is consequently a nonempty smooth irreducible open \(\Delta^\circ\), consisting of sections with a unique ordinary point and invertible polar Hessian, containing every \(H_s\). The line \(D\) is transverse at those points: the derivative in the fibre coordinates vanishes, so regularity of the total pencil forces a nonzero derivative in its parameter direction. By (G.8) this is transversality.

The proper universal hyperplane family \(g:\mathcal Y\to P\) is smooth over \(P-\Delta\), and its cohomology local systems restrict to those of the pencil. At the generic point of \(\Delta^\circ\), a transverse strict henselian trait has one ordinary quadratic point and regular total space. Formula (G.2) kills wild inertia. Each finite quotient of rational monodromy, formed with a stable lattice, is therefore tame at the generic point of \(\Delta\), and factors through \(\Pi\). The local Kummer lemma controls it at every point of \(\Delta^\circ\); tameness on one pencil was not silently used as a multidimensional ramification theorem.

The transverse-line proposition makes the pencil tame group surject onto \(\Pi\). The inertia lemma gives conjugators there, which lift to the pencil group. Transversality makes the ambient parameter a unit times the pencil uniformizer, so the characters in (G.2) agree with multiplicity one.

If \(S=\varnothing\), the representation is unramified on all of \(D\simeq\mathbf P^1\), hence trivial at every lattice level by the projective-line calculation. No discriminant argument is needed; conjugacy of an empty set is vacuous.

**Theorem G.1.** Under the canonical restriction, cohomological monodromy is tame. One can choose one compatible path at each \(s\in S\) such that its local inertia images generate the monodromy image topologically. The cycles \(\pm\delta_s\) are conjugate under geometric monodromy; if one is zero, all are zero.

**Proof.** Tameness follows from (G.2), and the selected-generator proposition applies to its tame representation. The ambient argument supplies a monodromy isometry \(g\) conjugating the two local inertia homomorphisms with their characters. In odd dimension use the same nonzero \(t_\ell\)-value at the two ends; in even dimension use the nontrivial quadratic element. Their complete operator formulas give

\[
b(-,\delta_t)\delta_t=b(-,g\delta_s)g\delta_s.
\tag{G.9}
\]

This uses their fixed coefficients, not merely equal ranks. Perfectness makes \(b(-,v)v=0\) exactly when \(v=0\). Otherwise their equal image lines give \(\delta_t=cg\delta_s\). Substitution in (G.9) gives \(c^2=1\), so \(c=\pm1\), including when \(\ell=2\). The constant Tate target is preserved, so there is no similitude factor. \(\square\)

### Sheaves on the complete parameter line

The local exact sequence (2.2) now gives Deligne's two alternatives without another global import. For \(i\notin\{n,n+1\}\), specialization is an isomorphism and inertia is trivial. Strictly locally at \(S\), \(R^if_*\mathbf Q_\ell\) is therefore the constant generic fibre with that specialization isomorphism. It is lisse on all of \(D\), and is constant since \(\pi_1(D)=1\).

For nonzero cycles, perfectness makes \(x\mapsto b(x,\delta_s)\) surjective. The exact sequence makes specialization in degree \(n+1\) an isomorphism, giving constancy there too. In degree \(n\), its image is \(\delta_s^\perp\), exactly the inertia invariants by (G.2). Proper base change identifies the special stalk with it, so adjunction gives

\[
R^nf_*\mathbf Q_\ell=j_*j^*R^nf_*\mathbf Q_\ell.
\tag{G.10}
\]

For zero cycles, conjugacy makes all vanish, and middle-degree specialization is an isomorphism. That sheaf is constant too. In degree \(n+1\) the exact sequence is

\[
0\longrightarrow\mathbf Q_\ell(m-n)
\longrightarrow H^{n+1}(X_s,\mathbf Q_\ell)
\longrightarrow H^{n+1}(X_{\bar\eta_s},\mathbf Q_\ell)
\longrightarrow0.
\]

The generic degree-\(n+1\) system is unramified and has a constant extension \(\mathcal C\) to \(D\). The adjunction map to it is surjective on stalks. Its kernel is supported on the finite set \(S\) with the indicated one-dimensional stalks. A sheaf with that support is the sum of its point pushforwards. Thus

\[
0\longrightarrow\bigoplus_{s\in S}\mathbf Q_\ell(m-n)_s
\longrightarrow R^{n+1}f_*\mathbf Q_\ell
\longrightarrow\mathcal C\longrightarrow0.
\tag{G.11}
\]

The all-zero alternative is impossible for even \(n\), since the proved norm is \(\pm2\). The existing quotient-by-the-radical argument proves absolute irreducibility whenever the vanishing quotient is nonzero. It does not require the vanishing subspace itself nondegenerate.

### Invariants and the radical quotient

**Proposition 4.1.** The space \(E_{\mathrm{van}}\) is monodromy-stable, and
\[
H^{\pi_1(U,u)}=E_{\mathrm{van}}^\perp.
\tag{4.4}
\]

**Proof.** Conjugacy of the cycles gives stability of their span. Alternatively, each local transformation changes any vector by a multiple of its \(\delta_s\), so the span is preserved by the topological generators.

If \(x\) is invariant, a local inertia element with nonzero transvection parameter, or the nontrivial reflection in even dimension, gives
\((x,\delta_s)\delta_s=0\). For nonzero \(\delta_s\), this forces \((x,\delta_s)=0\); a zero cycle imposes no condition. Conversely, orthogonality to all cycles makes every local formula fix \(x\). All monodromy then fixes it because those images generate topologically; the stabilizer of a vector in a continuous finite-dimensional representation is closed. This proves (4.4), also in the all-zero case. \(\square\)

Put
\[
R_{\mathrm{van}}=E_{\mathrm{van}}\cap E_{\mathrm{van}}^\perp,\qquad
V=E_{\mathrm{van}}/R_{\mathrm{van}}.
\tag{4.5}
\]
The restriction of the pairing has exactly this radical, so it descends to a nondegenerate pairing \(\psi\) on \(V\).

**Corollary 4.2.** If \(V\ne0\), its geometric monodromy representation is absolutely irreducible.

**Proof.** Extend coefficients to any field extension. The radical, orthogonal complement and span commute with that extension. Let \(W\subset V\) be a nonzero stable subspace and choose \(0\ne w\in W\). Since the images of the \(\delta_s\) span \(V\) and its pairing is nondegenerate, some \(\psi(w,\bar\delta_s)\ne0\). The local formula shows that a nonzero multiple of \(\bar\delta_s\) lies in \(W\). Conjugacy then places every cycle image in \(W\), so \(W=V\). Apply this to an algebraic closure of \(\mathbf Q_\ell\). \(\square\)

There is no assumption that the pairing on \(E_{\mathrm{van}}\) itself is nondegenerate. SGA 7 XVIII, Corollary 6.7, printed pp.326–327, gives an irreducibility argument under an additional nondegeneracy condition; Deligne's bibliographic note (5.13)(D) explicitly passes to the quotient in the general case. The proof above supplies that general quotient argument.

## 5. A Lie algebra generated by transvections

Let \(K\) be any field of characteristic zero, and let \((V,\psi)\) be a finite-dimensional nondegenerate alternating space. For \(v,w\in V\), define
\[
N_v(x)=\psi(x,v)v,\qquad
S_{v,w}(x)=\psi(x,v)w+\psi(x,w)v.
\tag{5.1}
\]
Both lie in \(\mathfrak{sp}(V,\psi)\), \(N_v^2=0\), and direct composition gives
\[
[N_v,N_w]=\psi(w,v)S_{v,w},\qquad
N_{av+bw}=a^2N_v+abS_{v,w}+b^2N_w.
\tag{5.2}
\]

**Lemma 5.1 (Deligne's linear-algebra lemma).** Suppose
\(\mathfrak L\subset\mathfrak{sp}(V,\psi)\) is generated as a Lie algebra by operators \(N_v\), and \(V\) is a simple \(\mathfrak L\)-module. Then
\(\mathfrak L=\mathfrak{sp}(V,\psi)\).

**Proof.** The assertion is immediate for \(V=0\); assume otherwise and discard zero generating vectors. Let \(\mathcal D\) be their set. Its span is a nonzero invariant subspace, because every \(N_v\) takes it into the line \(Kv\). Simplicity makes \(\operatorname{span}\mathcal D=V\).

Make a graph on \(\mathcal D\), joining vectors when their pairing is nonzero. The span of a connected component is invariant under every generating \(N_v\): vectors from any other component are orthogonal to it. Simplicity makes any such component span \(V\); a nonzero vector in another component would then be orthogonal to \(V\), which is impossible. Thus the graph is connected. Choose finitely many vertices spanning \(V\), and finitely many connecting paths between them. We obtain a finite connected set still spanning \(V\). Order it so that each new vertex pairs nontrivially with an earlier one.

We prove that \(N_x\in\mathfrak L\) for every vector in its successively enlarged span. For a one-dimensional span this follows from \(N_{av}=a^2N_v\). Suppose it holds on a subspace \(W\), and let \(z\) be the next vertex. Some \(w_0\in W\) has \(\psi(w_0,z)\ne0\). Equation (5.2) gives \(S_{w_0,z}\in\mathfrak L\). For any \(w\in W\) with \(\psi(w,z)\ne0\), it also gives \(S_{w,z}\). If \(\psi(w,z)=0\), the vector \(w+w_0\) has nonzero pairing with \(z\), so
\(S_{w,z}=S_{w+w_0,z}-S_{w_0,z}\in\mathfrak L\).
The second identity in (5.2) now gives \(N_x\in\mathfrak L\) for every \(x\in W+Kz\). Induction yields all \(N_x\), \(x\in V\).

Finally, the map \(A\mapsto((x,y)\mapsto\psi(Ax,y))\) identifies \(\mathfrak{sp}(V,\psi)\) with the space of symmetric bilinear forms on \(V\): the symmetry is precisely the symplectic Lie-algebra condition, and nondegeneracy of \(\psi\) makes the map bijective. Under it, \(N_v\) corresponds, up to a fixed minus sign, to the square of the linear form \(x\mapsto\psi(x,v)\). Squares span all symmetric bilinear forms in characteristic zero, since
\((a+b)^2-a^2-b^2=2ab\). Thus the \(N_v\) span \(\mathfrak{sp}\), and the lemma follows. \(\square\)

The graph argument proves the lemma over \(K\) itself; no algebraic-closure hypothesis was silently inserted. Its source formulation is Deligne, *Weil I*, Lemma (5.11), printed pp.293–294.

## 6. Openness of symplectic monodromy

Assume now that \(n\) is odd. The space \(V\) from (4.5) has a nondegenerate alternating form. Geometric monodromy fixes the Tate target over \(k\), so it acts through
\[
\rho:\pi_1(U,u)\longrightarrow\operatorname{Sp}(V,\psi).
\tag{6.1}
\]

**Theorem 6.1 (Kazhdan–Margulis in Deligne's form).** The image of (6.1) is open in \(\operatorname{Sp}(V,\psi)(\mathbf Q_\ell)\).

**Proof.** If \(V=0\), its symplectic group is trivial and the assertion is immediate. Otherwise let \(G\) be the image. It is compact and closed, as the continuous image of a profinite group. For every nonzero cycle image \(v_s=\bar\delta_s\), local inertia contains
\[
1+tN_{v_s}\in G\quad(t\in c_s\mathbf Z_\ell)
\tag{6.2}
\]
for some \(c_s\in\mathbf Q_\ell^\times\). The sign and the choice of a Tate-line basis are absorbed in \(c_s\); \(N_{v_s}^2=0\) makes integer powers add the parameter, and compactness includes their \(\mathbf Z_\ell\)-limits.

Let \(\mathfrak L_0\) be the Lie algebra generated by these \(N_{v_s}\). A subspace invariant under \(\mathfrak L_0\) is invariant under each local transvection and hence under \(G\). Corollary 4.2 makes \(V\) simple for \(\mathfrak L_0\); Lemma 5.1 gives
\(\mathfrak L_0=\mathfrak{sp}(V,\psi)\).

We show directly why this yields an **open** image. Let \(W\) be the linear span of all conjugates \(gN_{v_s}g^{-1}\), \(g\in G\). It is stable under conjugation by \(G\). For \(A\in W\), conjugation by (6.2) gives
\[
(1+tN_{v_s})A(1-tN_{v_s})
=A+t[N_{v_s},A]-t^2N_{v_s}AN_{v_s}\in W.
\tag{6.3}
\]
Evaluating at three distinct admissible \(t\)'s and using the invertible Vandermonde matrix shows \([N_{v_s},A]\in W\). Thus \(W\) contains every iterated Lie bracket of the generators, and \(W=\mathfrak{sp}(V,\psi)\).

Choose a basis \(A_1,\ldots,A_M\) of this Lie algebra consisting of such conjugates. Each has square zero, and \(1+t_jA_j\in G\) for \(t_j\) in a suitable small \(\ell\)-adic ball. Define the analytic map
\[
\Phi(t_1,\ldots,t_M)=\prod_{j=1}^M(1+t_jA_j).
\tag{6.4}
\]
Its derivative at \(0\) is \((t_j)\mapsto\sum_jt_jA_j\), an isomorphism onto the symplectic tangent space.

For an explicit chart, the Cayley transform \(A\mapsto(1-A)^{-1}(1+A)\) maps a neighbourhood of \(0\) in \(\mathfrak{sp}\) to a neighbourhood of \(1\) in \(\operatorname{Sp}\); its inverse is
\(g\mapsto(g-1)(g+1)^{-1}\). The symplectic identity verifies these maps, and their derivatives are multiplication by \(2\) and \(1/2\). They work also for \(\ell=2\), after shrinking the balls, since our scalar field has characteristic zero.

Compose (6.4) with the inverse chart. Its derivative is invertible. The \(\ell\)-adic inverse-function argument now puts a neighbourhood of \(1\) in the image of \(\Phi\): after normalizing its derivative to the identity and shrinking a ball, write the map as \(x+r(x)\) with \(r\) Lipschitz of constant strictly less than \(1\). For each sufficiently small \(b\), the contraction \(x\mapsto b-r(x)\) has a unique fixed point in that complete ball. Thus every such \(b\) has a preimage. All factors in (6.4) lie in \(G\), so this neighbourhood lies in \(G\). Hence \(G\) is open. \(\square\)

This proves the assertion of Deligne, *Weil I*, Theorem (5.10), printed p.293, with the entire rank-one Lie-algebra step supplied. It proves more than Zariski density. A chosen integral lattice is preserved by compact monodromy; openness makes the image finite-index in the corresponding compact symplectic group. In Lesson 10, Zariski density will suffice for a particular coinvariant calculation, but the theorem here is the stronger openness statement.

## 7. Three examples

### Plane curves

Take a Lefschetz pencil of degree-\(d\) curves in \(\mathbf P^2\), with transverse axis and \(d^2\) distinct base points. The base-point count is Bézout. A smooth member has genus \(g=(d-1)(d-2)/2\), as in [Stacks Tag 0BYD](https://stacks.math.columbia.edu/tag/0BYD). Let \(N=\#S\).

The blow-up formula gives \(\chi(\widetilde X)=3+d^2\). The local exact sequence (2.2) for \(n=1\), whether or not \(\delta\) is zero, gives
\(\chi(X_s)=\chi(X_u)+1=3-2g\).
Over \(U\), \(R^jf_*\mathbf Q_\ell\) are lisse and tame, of ranks \(1,2g,1\). The tame Euler formula of Lesson 8, followed by the alternating Euler characteristic of Leray and open–closed localization, yields
\[
\begin{aligned}
\chi(\widetilde X)
&=(2-N)(2-2g)+N(3-2g)\\
&=4-4g+N.
\end{aligned}
\tag{7.1}
\]
Combining the two expressions,
\[
N=d^2-1+4g=3(d-1)^2.
\tag{7.2}
\]
No assertion of multiplicativity for an arbitrarily wild family was used: tameness and its stated Euler formula supply the open contribution. For \(d=1\), \(N=0\); for \(d=2\), \(N=3\); for \(d=3\), \(N=12\).

### The Legendre family and squared transvections

Assume \(p\ne2\).

The family from Lesson 8 has nodal fibres at \(\lambda=0,1\). It is a useful pencil-like elliptic example, with geometric monodromy in \(\operatorname{SL}_2(\mathbf Z_\ell)\), after choosing the Tate-module symplectic lattice. Its given Weierstrass model is **not** a regular Lefschetz total space at these nodes. Locally its smoothing parameter has order \(2\) in \(\lambda\), or \(\lambda-1\).

For example, near \((x,y,\lambda)=(0,0,0)\), the equation is
\(y^2-x(x-1)(x-\lambda)=0\). Its critical \(x\)-coordinate is \(\lambda/2+O(\lambda^2)\); substituting gives critical value \(-\lambda^2/4+O(\lambda^3)\). The henselian Morse normal form therefore has smoothing parameter a unit times \(\lambda^2\). The local formula is a transvection with parameter twice that of an ordinary simple smoothing. The same calculation applies at \(\lambda=1\).

The two vanishing directions are independent. If they coincided, their local operators at \(0,1\) would be commuting unipotents with the same rank-one nilpotent, so their product would have both eigenvalues \(1\). The tame relation among the three local generators would force the same eigenvalues at infinity. But Lesson 8, (6.7), showed that inertia at infinity has both eigenvalues \(-1\), through the quadratic twist of a multiplicative fibre. This is a contradiction.

The two independent rank-one operators generate \(\mathfrak{sl}_2\), either by Lemma 5.1 or Exercise 9.3 below. Their one-parameter closures, with parameters in \(2\mathbf Z_\ell\), give an open monodromy subgroup by the argument of §6. The perfect alternating lattice pairing places this geometric group in \(\operatorname{SL}_2(\mathbf Z_\ell)\); openness implies finite index there, including when \(\ell=2\). The factor \(2\) cannot be dropped when describing integral local operators.

### A pencil of quadric surfaces

Assume \(p\ne2\). Take a pencil of quadratic forms in four variables whose determinant polynomial has four distinct roots. To check the geometry, choose a nonsingular member as the first form. The self-adjoint operator representing the second form has four distinct eigenvalues, so an orthogonal eigenbasis gives forms \(\sum x_i^2\) and \(\sum \lambda_i x_i^2\), with distinct \(\lambda_i\). A dependent pair of gradients at a base point would force at most one \(x_i\) to be nonzero, contradicting \(\sum x_i^2=0\) in projective space. Thus the base is smooth. Each singular member has exactly one zero diagonal coefficient and rank \(3\), hence is a quadric cone with one ordinary double point. The two forms have no common zero at its vertex, which also ensures regularity of the incidence total space there. This is a Lefschetz pencil on the degree-\(2\) Veronese image of \(\mathbf P^3\), with \(n=2\).

A smooth fibre over \(k\) is \(\mathbf P^1\times\mathbf P^1\). In \(H^2(1)\), let \(a,b\) be the two ruling classes. They satisfy
\[
a^2=b^2=0,\qquad(a,b)=1,\qquad
\delta=a-b,\quad(\delta,\delta)=-2.
\tag{7.3}
\]
The \(n=2\) reflection is
\(T(x)=x+(x,\delta)\delta\). It sends \(a\) to \(b\), \(b\) to \(a\), fixes \(a+b\), and sends \(\delta\) to \(-\delta\). Here the vanishing part is a one-dimensional orthogonal representation, not a symplectic transvection representation. The parity of the fibre dimension controls the mechanism.

<a id="8-exercises-and-audited-solutions"></a>

## 8. Exercises and solutions

**Exercise 9.1 (easy).** Count the singular members of a degree-\(d\) Lefschetz pencil of plane curves. Identify precisely where an Euler-characteristic argument needs tameness.

**Solution.** There are \(d^2\) transverse base points, so Proposition 1.2 gives Euler characteristic \(3+d^2\) for the blown-up plane. The smooth fibre has \(2-2g\), with \(g=(d-1)(d-2)/2\). Each ordinary nodal fibre has Euler characteristic one larger, from (2.2). On the open parameter curve, the tame Euler formula applies to each lisse \(R^jf_*\mathbf Q_\ell\), making its Euler characteristic its rank times \(2-N\). Therefore (7.1) holds and \(N=3(d-1)^2\). The step on the open set, not the individual nodal correction, would fail without controlling wild ramification.

**Exercise 9.2 (medium).** Prove the orthogonal-complement invariant statement, allowing a nontrivial radical in the vanishing space.

**Solution.** If \(x\) is invariant, subtract \(x\) from its local Picard–Lefschetz transform. For a nonzero cycle the result is a nonzero scalar parameter times \((x,\delta_s)\delta_s\), so invariance implies \((x,\delta_s)=0\). Zero cycles impose no condition. Conversely all these pairings vanishing makes every local inertia image fix \(x\), hence all geometric monodromy fixes it. This proves \(H^{\pi_1}=E_{\mathrm{van}}^\perp\) before taking any quotient. Its intersection with \(E_{\mathrm{van}}\) is precisely the radical, so quotienting yields a nondegenerate form; it does not justify replacing \(E_{\mathrm{van}}\) by a nondegenerate space without explanation.

**Exercise 9.3 (medium).** Prove Lemma 5.1 directly when \(\dim V=2\).

**Solution.** Simplicity forces the nonzero generating directions to span \(V\); choose two independent ones \(e,f\), rescaling so \(\psi(e,f)=1\). In this basis,
\[
N_e=\begin{pmatrix}0&-1\\0&0\end{pmatrix},\qquad
N_f=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
[N_e,N_f]=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
They span the three-dimensional space of trace-zero matrices,
\(\mathfrak{sp}_2=\mathfrak{sl}_2\). A Lie algebra containing them is therefore the full symplectic algebra. The nonzero scalar multiples arising from squared transvections in the Legendre example give the same Lie algebra over \(\mathbf Q_\ell\).

**Exercise 9.4 (medium).** Compute the cohomology of the blow-up of \(\mathbf P^2\) associated to a pencil of lines. Give its degree-two intersection matrix.

**Solution.** The axis is one point. Formula (1.2) gives \(H^0=\mathbf Q_\ell\), \(H^2=\mathbf Q_\ell(-1)^2\), \(H^4=\mathbf Q_\ell(-2)\), and odd cohomology zero. Let \(h\) be the pulled-back line class and \(e\) the exceptional divisor class. Then \(h^2=1\), \(h e=0\), \(e^2=-1\); the last equality is the degree of \(\mathcal O_{\mathbf P^1}(-1)\). The fibre class is \(h-e\), with square \(0\), as required for distinct fibres of a morphism to \(\mathbf P^1\). The genus is zero and there are no singular fibres, agreeing with (7.2) for \(d=1\).

**Exercise 9.5 (hard).** When the residue characteristic is different from \(2\), prove the degree-zero local formula, including the quadratic character and the specialization map, for a proper regular one-dimensional total space.

**Solution.** The whole-space reduction in Proposition 3.1 makes the map finite flat: there are no vertical components, all fibres are zero-dimensional, and a torsion-free finite module over a DVR is flat. Henselian decomposition splits off the étale branches. At the quadratic point the normal form is \(z^2=b\); regularity forces \(v(b)=1\), and Hensel's lemma removes its unit factor. Thus \(K(\sqrt t)/K\) is the unique quadratic extension, since all units are squares. Its nontrivial inertia element interchanges the two generic embeddings.

The special rank-\(2\) algebra has one geometric point, giving specialization \(1\mapsto e_++e_-\). The difference \(\delta=e_+-e_-\) has dot-product norm \(2\). For a pair of coordinates \((a,b)\), subtracting \((a-b)\delta\) swaps them, which is (3.2); the remaining coordinates are fixed. Higher cohomology of finite geometric fibres is zero, and the cokernel of specialization is the one-dimensional difference coordinate. This verifies every part of (2.2)–(2.4) for \(n=0\) under this characteristic restriction, including the identification \(\epsilon(\sigma)=\sigma(\sqrt t)/\sqrt t\). Exercise 9.7 treats the wild equal-characteristic-two case.

**Exercise 9.6 (medium; openness diagnostic).** Explain why merely proving a Zariski closure is symplectic is not the final step of Theorem 6.1. Give the analytic step used here.

**Solution.** Zariski closure describes polynomial relations on a group; openness concerns an actual \(\ell\)-adic neighbourhood in its image. In this proof, actual local inertia gives the curves \(1+tN_v\) inside the compact image. Their conjugates span the full tangent space, by (6.3) and Lemma 5.1. Taking a finite tangent basis produces the product map (6.4) with invertible derivative. In the Cayley chart, the contraction proof of the inverse-function theorem puts an entire sufficiently small ball in that image. Thus the compact monodromy image contains a neighbourhood of the identity, exactly the required openness.

**Exercise 9.7 (medium; wild reflection).** Over \(k[[t]]\) with \(\operatorname{char}k=2\), compute specialization, inertia and the Swan conductor for \(z^2+t^h z+t=0\), \(h\ge1\). Explain why the number of vanishing coordinates does not determine the conductor.

**Solution.** The equation is Eisenstein and its total local ring is regular, because the coefficient of \(t\) has nonzero linear term. Its generic derivative is \(t^h\ne0\), so it is a separable quadratic extension. There is one special geometric point and two generic ones; specialization is \(c\mapsto(c,c)\). The nonidentity automorphism sends \(z\) to \(z+t^h\), hence interchanges the two embeddings. For \(\delta=(1,-1)\), the matrix is \(x\mapsto x-(x,\delta)\delta\), and \((\delta,\delta)=2\). Since \(z\) is a uniformizer and \(v_C(t)=2\), the difference has valuation \(2h\). The lower ramification groups remain of order two through index \(2h-1\), giving Swan conductor \(2h-1\). The quotient of specialization always has dimension one, whereas that conductor grows with \(h\).

**Exercise 9.8 (medium; the global degree-zero quotient).** Prove that a connected degree-\(d\) pencil on a curve has the vanishing representation (3.6) in every characteristic. Explain the role of all transports in the wild case.

**Solution.** Each local inertia image is a transposition by Proposition 3.1. The quotient by their normal closure extends across the punctures to a finite étale cover of \(\mathbf P^1\), hence is trivial by the written projective-line computation used in Proposition 3.3. Thus the transitive permutation image is generated by transpositions. Their edge graph is connected, and swaps along paths generate every transposition, so the image is \(\operatorname{Sym}_d\). Transporting one local difference gives every \(e_i-e_j\); these span the sum-zero space. The invariant space is the constant line, whose nonzero norm \(d\) makes the sum-zero pairing nondegenerate over \(\mathbf Q_\ell\). The coordinate-swap argument in Proposition 3.3 proves absolute irreducibility after any coefficient-field extension. Normal generation in the wild case requires the conjugate inertia images, and therefore all transported differences; one arbitrarily selected path to each singular parameter does not supply a generator theorem.

## Proof scope and further topics

Theorem 1.0 proves pencil existence and openness in every characteristic after each degree-e Veronese embedding with e at least two, and for the original embedding in characteristic zero. Sections NC, Q and PL prove the isolated quadratic local theory with actual support, comparison, specialization and trace maps, including compatible finite 2-power coefficients. Section 3 treats degree zero in every characteristic, and computes the equal-characteristic-two wild conductor. Section 4 proves the higher tame generator and conjugacy statements under the canonical restriction, the exceptional zero-cycle alternative and the invariant and radical-quotient conclusions. Sections 5–6 prove the Lie-algebra and openness steps.

The cover-theoretic proofs use the exact written providers and expressly retained foundations identified in Section 4. General finite-type Riemann existence and the analytic comparison foundations are declared. The Cohen provider retains its incorporated human component's GNU FDL attribution separately from original AI CC0 exposition.

Leray supplies a filtration without an assumed degeneration. The Legendre model is treated with its order-two smoothing parameters. The weight estimate and higher-dimensional Riemann hypothesis remain the subjects of the next two lessons.

## References and proof locators

- [Deligne, *La conjecture de Weil I*](https://www.numdam.org/item/PMIHES_1974__43__273_0/), §§4–5, printed pp.287–294: (4.1) sign table; (4.2)–(4.4) local specialization and inertia; (5.7) existence; (5.8) the global alternatives; (5.10) openness; (5.11) the Lie lemma; (5.13)(D) the general radical quotient. The original proofs of the central linear and global consequences in this lesson are §§3–6.
- [SGA 7 II, Deligne and Katz](https://publications.ias.edu/sites/default/files/Number12.pdf), *Groupes de monodromie en géométrie algébrique*, Lecture Notes in Mathematics 340 (1973): XIII, §2, nearby and vanishing cycles, printed pp.98–115; XV, §§1.3 and 3, ordinary quadratic normal forms and Picard–Lefschetz, printed pp.175–176 and 187–196; XVII, Theorem 2.5, printed p.217, existence after Veronese embedding; XVIII, Theorems 1.2 and 2.2, printed pp.257–263, projective bundles and blow-ups, and §6, printed pp.312–327, tame generators, conjugacy and irreducibility. Deligne's (5.13) gives the precise relation between these results and his summary.
- [Stacks, local acyclicity, Tags 0GJM, 0GJP, 0GJQ](https://stacks.math.columbia.edu/tag/0GJM): smooth points have no vanishing contribution. [Tag 0BYD](https://stacks.math.columbia.edu/tag/0BYD) gives the plane genus used in §7.
- [Milne, *The Riemann Hypothesis over Finite Fields: From Weil to the Present Day*](https://arxiv.org/abs/1509.00797), “Completion of the proof”: the blow-up and Leray filtration explain how the vanishing quotient enters the later estimate. That survey gives orientation; Deligne and SGA 7 state the local hypotheses and signs used above.
- Lesson 8, §6: the tame Euler formula and Legendre local twist at infinity. Local acyclicity retains the stated foundations; Smooth traces, duality and Gysin maps, §§8–12, proves smooth duality and the cohomological pairings.
- [*Étale neighbourhoods, henselization and quasi-finite morphisms*](course:AG-FSE/etale-neighbourhoods-henselization-and-quasi-finite-morphisms), §2 and Theorem 5.2: finite-algebra decomposition over a henselian ring and the written finite étale residue-field equivalence. [*The étale fundamental group*](course:AG-DFG/AG-DFG-05), Theorem 1.3, §§2 and 4, and Proposition 5.1: finite covers as finite group actions, normal-scheme extension, and the all-characteristic projective-line computation. Section 3 here supplies the quadratic algebra, wild conductor and symmetric-group arguments; it does not derive them from a higher-dimensional Picard–Lefschetz assertion. The projective-line computation's canonical-degree foundation is [Stacks, Tag 0C1A](https://stacks.math.columbia.edu/tag/0C1A).

Linked sources retain their own rights.
