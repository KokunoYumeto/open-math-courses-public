# SH02-RR — From directional tests to further microlocal theories

Original English lesson for SH-02, released under GFDL-1.2-or-later with no invariant sections or cover texts. The calculations below use the cited course results with their individual prerequisite status; the research projects do not import the later theorems they ask the reader to study.

A useful research question identifies which part of a construction survives a change of setting. Here the changes are concrete: deleting a zero section, replacing a positive real parameter by a complex one, imposing constructibility, transporting a cotangent relation, or recognizing a sheaf as the solutions of an operator system. Each route begins with a calculation available in this course and specifies what further theorem would be needed.

## SH02-RR-START — Choose the object before choosing the application

The standing sheaf coefficients are a commutative unital ring $k$ of finite global dimension. Bounded sheaf complexes may have arbitrary modules as stalks. A field, perfect stalks, a complex analytic manifold, or a coherent operator module enters only where explicitly stated below.

For a first pass, take the routes in the order written. They connect the following prerequisites:

| Start with | Then use | Question it makes precise |
|---|---|---|
| Orientation and trace | Fourier halfspaces | Which boundary and shift does a transform retain? |
| The deformation manifold | Specialization section tests | Which limiting neighborhoods define the new sheaf? |
| Between-level cohomology | Finite critical complexes | When do local directional obstructions produce numerical invariants? |
| Localized morphisms | Kernel composition | Which correspondence carries an actual equivalence? |
| [Involutivity](involutivity.md#SH02-INV-THEOREM) | [Directed propagation](involutivity.md#SH02-INV-MICROLOCAL-FLOW) | What extra identification turns a sheaf result into an analytic result? |

The categorical foundations are taught in *Categorical and derived tools for analytic sheaves*; contact transformations, constructible sheaves and characteristic cycles in *Constructible and perverse sheaves*. A project may isolate a needed supporting lemma from another theory; it must specify that lemma without claiming the surrounding theory has been completed.

## SH02-RR-BOUNDARIES — Keep the zero section visible

Begin with SH02-FS-CONE, SH02-SP-ZERO, and the [direction-space comparisons](conic-and-trace-applications.md#SH02-CTA-RADIAL). On the oriented line, let $T$ be the Fourier functor defined by the nonpositive pairing $x\xi\leq0$. For the constant coefficient sheaf $k$ these calibrations are

$$
\begin{aligned}
T k_{\{0\}}&\simeq k_{\mathbb R},&
T k_{\mathbb R}&\simeq k_{\{0\}}[-1],\\
T k_{[0,\infty)}&\simeq k_{(0,\infty)},&
T k_{(0,\infty)}&\simeq k_{(-\infty,0]}[-1].
\end{aligned}
$$

**Check.** The zero input fibre integrates a point, and the whole-line input has nonzero compactly supported fibre cohomology only at $\xi=0$. The other two identities are the closed and open cone formulas. The orientation of the line identifies its orientation local system with $k$; the compact-support degree contributes $[-1]$. Thus changing a closed endpoint to an open endpoint changes both the output support and its degree.

**Project.** For a real vector bundle $E\to B$, compare a conic sheaf with the sheaf it induces on $(E\setminus0)/\mathbb R_{>0}$. Recover separately the data measured by zero-section inverse image and exceptional inverse image. Use the displayed line examples to test the difference between extending punctured data by $Rj_*$ and by $j_!$. Then write the two sphere-transform comparisons with the radial-first orientation convention of SH02-MD-SPHERE.

The output should be a diagram containing the extension maps and the zero-section localization triangle. An equivalence on the sphere of directions alone cannot recover which extension was chosen. Over a nonorientable bundle, retain its orientation local system in the diagram rather than selecting unrelated local generators. The algebraic Fourier transforms mentioned in the antecedents live in other coefficient categories; this project provides a geometric calibration for a future comparison, not an identification with them.

## SH02-RR-DEFORMATION — Compare parameters as well as central fibres

Use SH02-NG-FUNCTORIALITY, SH02-NG-CONE-SEQUENCES, and SH02-SP-HOMOGENEOUS. In an adapted chart $(u,z)$ with center $u=0$, the real deformation has coordinates $(v,z,t)$ and map

$$
u=tv.
$$

At $t=0$ the coordinate $v$ runs through the entire normal vector space. Positive time selects the one-sided limit used to define specialization. The parameter orientation records the relative determinant factor even where the deformation map is not submersive.

There is a small algebraic chart calculation that makes the comparison concrete. Let $K$ be any field, used here for coordinate algebras independently of the sheaf coefficient ring $k$. With $u=(u_1,\ldots,u_r)$, form

$$
A=K[u,z,t,v]/(u_1-tv_1,\ldots,u_r-tv_r).
$$

Eliminating the $u_i$ identifies $A$ with $K[z,t,v]$. Its central quotient is $K[z,v]$, and after inverting $t$ one may instead eliminate $v_i=t^{-1}u_i$, obtaining $K[u,z,t,t^{-1}]$. This verifies the full normal fibre and the unchanged nonzero fibres in this coordinate model. It does not choose a sheaf theory on the corresponding algebraic spaces.

**Project.** First carry out the chart calculation for a map of pairs whose normal differential has a kernel. Compare the coordinate map with the clean-embedding criterion in SH02-NG-CLEAN-EMBEDDING. Next choose a holomorphic function $f:X\to\mathbb C$ on a complex manifold and study the nearby- and vanishing-cycle construction of [Nearby cycles, monodromy and specialization](https://kokunoyumeto.github.io/open-math-courses-public/courses/nearby-cycles-monodromy-and-specialization/). The definitions start with $F\in D^b(k_X)$. For the regular section comparison, take $df\ne0$ along $Y=f^{-1}(0)$ and a weakly $\mathbb C$-constructible $F$. Record the choice of a lift in the universal cover of $\mathbb C^*$, the monodromy, and the shifted triangles before comparing nearby and vanishing cycles with normal specialization and microlocalization. General cycle constructions and these particular section comparisons have different hypotheses.

The positive real parameter is contractible; a punctured complex parameter has loops. Consequently a comparison must explain what happens to monodromy, as well as to the central fibre. A completed project should calculate both sides in one nonsingular local model and identify the extra theorem required to extend that calculation to a singular function. The algebraic deformation and any etale or coherent-sheaf version require their own exact sources and operation theorems. The complex nearby-cycle route belongs to SH-03. For a holomorphic map $f$ to a one-dimensional complex manifold, a bounded $\mathbb C$-constructible complex $G$ on its source and a compact subset $K$ of a fibre $f^{-1}(x)$, Proposition 8.6.2 of Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf) gives open neighbourhoods $U$ of $x$ and $V\subset f^{-1}(U)$ of $K$ such that the direct images of $G|_V$ by $f|_V:V\to U$, with and without proper supports, are $\mathbb C$-constructible, and bounds their microsupports by the image of $\operatorname{SS}(G)$ under the cotangent correspondence of $f$; the memoir notes that the statement fails when the target has dimension other than one. Determine which step of the nearby-cycle construction this statement can supply.

## SH02-RR-MORSE — Turn local tests into finite information

Start with SH02-MO-RELATIVE-CUTOFF and SH02-MO-FIELD-BOUNDARY. The local datum at a possible critical level is a complex,

$$
J_x=\bigl(R\Gamma_{\{\varphi\geq\varphi(x)\}}F\bigr)_x.
$$

Its degree, its module structure, and the side of the inequality all matter. Numerical Morse inequalities follow in the course when $k$ is a field, every support sublevel is compact, the graph of $d\varphi$ meets microsupport in finitely many points, and the resulting $J_x$ have finite-dimensional bounded cohomology. These hypotheses do not impose constructibility on every sheaf in the course.

**Project.** Separate the following two extensions of that calculation.

1. For a smooth function with a nondegenerate critical point, compute $J_x$ in Morse coordinates and track the orientation line of its negative Hessian space. Then apply the finite-jump theorem to a function with finitely many such points and compact sublevels. The local calculation and the passage to the global Euler formula are part of the assigned SH-02 mathematical obligations; a project proposal does not count as their solution.
2. On a real analytic manifold, choose a sheaf adapted to a finite local stratification with one singular stratum. Determine the additional control on limiting conormals that makes the stratumwise tests compatible. Compare ordinary addition with the asymptotic sum, and examine the constructibility criteria in Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Chapter 8, and in Stéphane Guillermou's [*Sheaves and symplectic geometry of cotangent bundles*](https://arxiv.org/abs/1905.07341v3), §1.2.3.

For the second project, use the $\mu$-stratification condition (Guillermou, Definition 1.2.19) when invoking the conormal criterion (Guillermou, Proposition 1.2.20); an arbitrary decomposition into strata is insufficient. Distinguish local constancy on strata from perfectness of stalk complexes, and distinguish either condition from the cohomological constructibility condition used for duality. State which version is used by the particular later theorem. The stratification and constructibility theory belongs to SH-03; the local critical complexes and endpoint conventions remain visible prerequisites here.

A useful first test is to replace a halfspace sheaf by the extension from its open interior. Compute the two $J_x$ using the localization triangle before taking Euler characteristics. This catches an endpoint error that a calculation of the underlying support set would miss.

## SH02-RR-CONTACT — Ask which dilation a transformation respects

The starting results are the Fourier cotangent map, its two dilation actions, and localized kernel composition. In bundle coordinates the map is

$$
\Phi_E(z,x;\zeta,\xi)=(z,\xi;\zeta,-x),
\qquad
\Phi_E^*\alpha_{E^*}=\alpha_E-d\langle x,\xi\rangle.
$$

It preserves the symplectic form. On components of positive bundle rank it does not commute with ordinary cotangent dilation: scaling a nonzero $\xi$ changes the target base coordinate. On a rank-zero component, $E=Z$ and $\Phi_E$ is the identity on $T^*Z$, so it does commute with that dilation. Its square is the cotangent lift of the vector-bundle antipode, which fixes $\zeta$. These are useful tests before attempting to pass to a space of directions.

**Project.** Choose open conic cotangent domains and a homogeneous symplectomorphism between them. Describe its signed graph in the product cotangent bundle. Find the conditions on a sheaf kernel that would make its two convolution composites the diagonal kernels in the appropriate localized categories. Check the unit and counit maps, the restriction on supports, and the compatibility with $\mu hom$; use SH02-MH-COMPOSITION to specify the last requirement.

Theorem 6.3.4 of Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), stated for a commutative coefficient ring of finite weak global dimension, takes open conic sets $\Omega_X\subset T^*X$ and $\Omega_Y\subset T^*Y$, a closed Lagrangian submanifold $\Lambda$ of $\Omega_X^a\times\Omega_Y$, where $a$ is the antipodal map, and $K\in D^b(k_{X\times Y})$. It assumes that the maps $(x,y;\xi,\eta)\mapsto(x;-\xi)$ from $\Lambda$ to $\Omega_X$ and $(x,y;\xi,\eta)\mapsto(y;\eta)$ from $\Lambda$ to $\Omega_Y$ are diffeomorphisms, that $\operatorname{SS}(K)\cap(\Omega_X^a\times T^*Y)$ and $\operatorname{SS}(K)\cap(T^*X\times\Omega_Y)$ are contained in $\Lambda$, that $K$ is cohomologically constructible, and that the natural morphism $k_\Lambda\to\mu hom(K,K)|_\Lambda$ is an isomorphism. It concludes that the functors $G\mapsto Rq_{1*}R\mathcal Hom(K,q_2^!G)$ and $F\mapsto Rq_{2!}(K\otimes q_1^{-1}F)$, where $q_1,q_2$ are the projections of $X\times Y$, are quasi-inverse equivalences between $D^+(Y;\Omega_Y)$ and $D^+(X;\Omega_X)$. Determine whether your candidate satisfies every condition, and whether the conclusion persists when the two maps from $\Lambda$ are only homeomorphisms. Then study the local realization and shift calculations in the same memoir, Theorem 6.3.5 and §7.4. The existence of a kernel for a contact transformation, the purity conditions along a Lagrangian, and the inertia-index shift are SH-03 results. The Fourier coordinate exchange above supplies a controlled model with two actions; it is not, by that fact alone, a map of ordinary cosphere quotients.

A concrete deliverable is a diagram with three panels: the geometric signed graph, the two kernel composites, and the induced map on microlocal Hom. Mark every shift in the second panel and every antipode in the first. If the projection rank of a Lagrangian changes, determine exactly which later shift theorem is needed instead of assigning a constant degree from a regular point.

## SH02-RR-OPERATORS — Identify the solution object before using its microsupport

Begin with [SH02-INV-THEOREM](involutivity.md#SH02-INV-THEOREM), SH02-MH-HOM, and SH02-MC-IDENTITY. The analytic route changes both the coefficient field and the category of inputs. On a complex manifold $X$, the operator sheaf $\mathcal D_X$ and the holomorphic function sheaf $\mathcal O_X$ lead to

$$
\operatorname{Sol}(\mathcal M)
=R\mathcal Hom_{\mathcal D_X}(\mathcal M,\mathcal O_X).
$$

The external bridge to study is **Theorem 10.1.1** of Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf): for a coherent $\mathcal D_X$-module, it identifies the microsupport of this solution complex with the characteristic variety, using the memoir's identification of complex and underlying real cotangent bundles. Holonomicity is not a hypothesis of this particular theorem. Its proof and the required analytic and operator-module foundations belong to SH-03. In the convention of §8.5.1 of the memoir, a real covector $a\,dx+b\,dy$ corresponds to $\zeta\,dz$ with $\zeta=(a-ib)/2$; thus the inverse map is $2\operatorname{Re}(\zeta\,dz)$. The normalization is part of the comparison, even though a positive scalar preserves a conic set.

**Project.** On a complex coordinate disk, take the operator $\partial_z$ and the module $\mathcal D/\mathcal D\partial_z$. Compute its solution complex from the two-term operator resolution. Local holomorphic primitives should account for the positive-degree term, and the surviving solutions should agree with the microsupport test for a constant sheaf. Compute the characteristic set from the order filtration as an independent check. Write down the real-cotangent identification explicitly; do not compare a complex cotangent set and a real one without that map.

Next compare a coherent module with a holonomic one. Determine which dimension condition on the characteristic variety is added by holonomicity, and which further result relates it to constructible solutions. Involutivity by itself does not impose the half-dimension condition: a whole symplectic manifold is involutive and has twice its Lagrangian dimension.

There is a second, distinct project at the microlocal level. On a complex manifold $X$, Proposition 10.6.2 of Kashiwara and Schapira's [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf) gives canonical morphisms $\mathcal E_X^{\mathbb R}\to\mu hom(\mathcal O_X,\mathcal O_X)$ and $(\mathcal E_X^{\mathbb R})^a\to\mu hom(\Omega_X,\Omega_X)$, and Corollary 10.6.3 gives, for $p\in T^*X$, a natural morphism of rings $\mathcal E^{\mathbb R}_{X,p}\to\operatorname{Hom}_{D^+(X;p)}(\mathcal O_X,\mathcal O_X)$. Determine whether these morphisms yield actions on the cohomology sheaves of $\mu hom(F,\mathcal O_X)$ for every $F\in D^b(\mathbb C_X)$. The holomorphic top-form coefficient object $\Omega_X$ carries right actions, whereas $\mathcal O_X$ gives left actions. Identify the acting sheaf $\mathcal E_X^{\mathbb R}$, the composition law producing the action, and the module side before comparing it with SH02-MH-COMPOSITION. Distinguish such a cohomology-level structure from placing the entire complex in a derived category of $\mathcal E_X^{\mathbb R}$-modules. A successful comparison must respect that distinction.

## SH02-RR-HYPERBOLIC — Separate propagation from the analytic interpretation

Use SH02-LFI-ESCAPE, SH02-LFI-INVERSE, and [SH02-INV-MICROLOCAL-FLOW](involutivity.md#SH02-INV-MICROLOCAL-FLOW). There are two different questions: whether restriction across a map preserves a microlocal object, and whether a section propagates along a Hamiltonian trajectory.

For the second question let $U\subset T^*X$ be open, $\phi\in C^2(U;\mathbb R)$, and suppose

$$
\operatorname{SS}(F)\cap U\subset\{\phi\geq0\},
\qquad
\operatorname{SS}(G)\cap U\subset\{\phi\leq0\}.
$$

The course result concerns each section of $\mathcal H^j\mu hom(G,F)$ and positive maximal Hamiltonian time inside $U$. Interchanging $F$ and $G$ changes the ordered cone and the propagation direction. At a critical point of $\phi$ the trajectory is stationary; no global completeness of the Hamiltonian flow is assumed.

**Project.** Choose a map of pairs $(Y,N)\to(X,M)$ and a conormal region on which to compare microlocalizations. Verify separately the escaping-covector exclusion, the noncharacteristic condition on the induced conormal map, and the ambient-lift condition in SH02-LFI-ESCAPE. Produce the two inverse-image comparisons with their relative orientation factors, and show where proper support becomes ordinary support. Then choose a Hamiltonian separating the two relevant microsupports and determine which ordered microlocal Hom can propagate forward.

To interpret the result for differential equations, supply the solution-complex identification from the preceding route and the precise microhyperbolic result required from §10.5 of *Microlocal study of sheaves*, in particular the setting of Theorems 10.5.1 and 10.5.4. For Theorem 10.5.4, start with a real analytic map of real analytic manifolds, a holomorphic extension between chosen complexifications, a coherent left $\mathcal D_X$-module, and an open region in the source conormal bundle. Check ordinary noncharacteristicity and the two additional normal-cone and ambient-lift conditions in that theorem; its full cotangent differential and its restricted conormal differential have distinct roles. Theorem 10.5.1 uses the normal cone $C_{T_M^*X}(\operatorname{char}(\mathcal M))$ to control microfunction solutions. Thus avoiding only the original characteristic set is not the microhyperbolic test. The function, hyperfunction, or microfunction coefficient object must also be specified.

A related product project starts from the noncharacteristic tensor and Hom estimates and the asymptotic estimates. Compare $k_{\{x\geq0\}}$ and $k_{\{x\leq0\}}$ on the line: their tensor product exists and is $k_{\{0\}}$, although their boundary directions violate the no-cancellation hypothesis. Then investigate a proposed multiplication of distributions. State its wavefront convention and its exact analytic multiplication theorem separately. Sheaf tensor product, smooth wavefront, analytic wavefront, and the microsupport of an associated solution sheaf are different inputs until an explicit comparison connects them.

## SH02-RR-SHEAR — A transported conormal and an exact viscous wave

The cotangent correspondence gives an explicit connection to fluid transport. Work on $0,\infty)\times\mathbb R^3$ in Cartesian coordinates $x=(x_1,x_2,x_3)$, with viscosity $\nu>0$. Choose real constants $\gamma,a,b,c$ with $a\ne0$, and set

$$
\begin{aligned}
B(x)&=(\gamma x_2,0,0),&
\Phi_t(y)&=(y_1+\gamma ty_2,y_2,y_3),\\
\xi(t)&=(a,b-\gamma at,0),&
\phi(t,x)&=\xi(t)\cdot x,\\
J(t)&=(a^2+b^2)t-\gamma abt^2+\frac{\gamma^2a^2}{3}t^3,&
w(t,x)&=c e^{-\nu J(t)}\cos\phi(t,x)\,e_3.
\end{aligned}
\tag{RRS1}
$$

Here $\Phi_t$ is the flow of the shear $B$. The velocity $u=B+w$, with pressure $p=0$ and force $f=0$, is an exact smooth solution of

$$
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f,
\qquad\operatorname{div}u=0.
\tag{RRS2}
$$

**Proof.** Both summands are divergence-free. Since $w$ points along $e_3$ and has no $x_3$ dependence, $(w\cdot\nabla)B=(w\cdot\nabla)w=0$. Also $(B\cdot\nabla)B=\Delta B=0$. Finally,

$$
(\partial_t+B\cdot\nabla)\phi=0,
\qquad J'(t)=|\xi(t)|^2,
\qquad\Delta w=-|\xi(t)|^2w.
\tag{RRS3}
$$

Thus $(\partial_t+B\cdot\nabla)w=-\nu|\xi(t)|^2w$ cancels $-\nu\Delta w$. This proves the nonlinear equation, including its pressure and divergence constraints. $\square$

The changing spatial frequency is exactly the cotangent image of the initial normal:

$$
\xi(t)=(D\Phi_t)^{-T}(a,b,0),\qquad
\kappa_t(y,\eta)=\bigl(\Phi_t(y),(D\Phi_t)^{-T}\eta\bigr).
\tag{RRS4}
$$

The inverse transpose follows by differentiating $\phi(t,\Phi_t(y))=ay_1+by_2$. It preserves the tautological one-form because $((D\Phi_t)^{-T}\eta)\cdot D\Phi_t\,dy=\eta\cdot dy$.

For the sheaf calculation retain the standing coefficient ring and assume $k\ne0$. Let $H_t=\{x:\phi(t,x)=0\}$ and extend the constant sheaf $k$ from this closed plane by zero. The diffeomorphism identifies sections on the two planes, so $(\Phi_t)_*k_{H_0}\simeq k_{H_t}$. The [closed-embedding equality, applied to the constant sheaf on $H_t$, gives

$$
\operatorname{SS}(k_{H_t})=N^*H_t
=\{(x;s\xi(t)):x\in H_t,\ s\in\mathbb R\}
=\kappa_t(N^*H_0).
\tag{RRS5}
$$

This includes zero covectors over the plane and both normal directions. No antipodal map or cohomological shift occurs.

The same normal controls the viscous decay. Completing the square yields

$$
J(t)=a^2t+t\left(b-\frac{\gamma at}{2}\right)^2+
\frac{\gamma^2a^2}{12}t^3,
\qquad
\|w(t)\|_\infty\le |c|
e^{-\nu a^2t-\nu\gamma^2a^2t^3/12}.
\tag{RRS6}
$$

When $\gamma\ne0$, the normal's norm grows linearly as $t\to\infty$, giving cubic-in-time damping of this mode. The normal need not grow monotonically at earlier times. The nontrivial solution has infinite kinetic energy on $\mathbb R^3$ and persists smoothly for all $t\ge0$.

**Project.** On open spacetime $t>0$, compute the conormal to $\phi=0$. It is $s(-\gamma ax_2,\xi(t))$, and hence lies in the zero set of the transport symbol $\tau+B\cdot\xi$. At a nonzero spatial frequency the viscous symbol $i(\tau+B\cdot\xi)+\nu|\xi|^2$ has positive real part. Explain why the phase-plane sheaf in (RRS5) has not thereby been identified with a sheaf of viscous solutions. In particular, the actual function $w$ is smooth and has no nonzero distributional wavefront covectors.

**Research context.** The phase and polarization discussion in OpenAI's [*Finite Time Blowup for Navier-Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), Sections 3.3 and 7.1, prompted this independently written calculation. The cited copy has 166 pages, was retrieved on 8 September 2026, and has SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. Its claimed finite-energy blowup theorem is not used here. Related forced Euler work is attributed to Levent Alpöge and Tristan Buckmaster in [Buckmaster's primary statement](https://cims.nyu.edu/~tristanb/statement.pdf), which credits the preceding program to Diego Córdoba and Luis Martínez-Zoroa. These antecedents do not supply a theorem equating the phase sheaf with a PDE solution object.

## SH02-RR-DELIVERABLE — Make the next theorem assessable

For one chosen route, prepare a short mathematical note with four parts:

1. Specify the objects, coefficient category, bounds, ambient geometry, and support conditions.
2. Draw the comparison with its actual arrows. Name the units, counits, restriction maps, and orientation identifications that define them.
3. Work through a local model and an exceptional case, such as an open endpoint, a zero vector, a rank change, or a stationary trajectory.
4. State the exact additional theorem needed for the external step, its source and the conclusion it would add.

The local model tests a proposed theorem; it does not prove its full generality. Within SH-02, Fourier normalization and the exact remaining trace comparison retain their owning proof obligations. The general fibre-product Hom comparison is constructed in SH02-MHPC-FIBRE-PRODUCT, conditional on its named operation and Fourier prerequisites. A route that uses one of those comparisons must retain that dependency rather than selecting an arbitrary isomorphism with the same endpoints.

## SH02-RR-REFERENCES — Antecedents and further reading

The primary reference for these routes is M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), with the survey of P. Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) (2016). Its Chapters 1–6 cover the present course's mathematical targets; Chapters 7–9 lead to the topics of *Constructible and perverse sheaves*.

This lesson introduces no imported theorem from algebraic Fourier theory, etale sheaves, distribution products, or a derived category of microdifferential modules. An exact comparison in one of those settings would need an additional source and proof package. The license grant covers this original lesson, not the cited books.
