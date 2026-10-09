# The GL_1 case as an equivalence of categories

*Draft. Self-checked by the writing AI. Public domain (CC0).*

The rank-one categorical correspondence matches three different phenomena. Connections on the Jacobian match the smooth moduli of rigidified flat lines. Automorphisms of a bundle contribute a derived spectral direction. The disconnected bundle degrees match the character weights of the spectral automorphism group. Keeping only the Jacobian and the set of local systems loses two of these factors.

The theorem statements and examples depending on §1's derived splitting or §4's geometric Lemma G remain conditional until the exact proof obligations in §9 are closed.

Let \(X/k\) be a smooth projective connected curve of genus \(g\), over an algebraically closed field of characteristic zero. Put \(J=\operatorname{Pic}^0(X)\), and choose \(x_0\in X(k)\). All categories below are presentable DG categories; tensor products of categories are presentable tensor products, and complexes are cohomologically graded. We use the trivial normalized half root for a torus: its adjoint bundle is constant, so its normalized determinant line is trivial.

For connections on smooth schemes we use the ordinary-local-system normalization fixed in [Geometric class field theory](geometric-class-field-theory.md). When converting to right crystals, the fixed shifts are those of [Sheaves and D-modules on Bun_G](sheaves-and-d-modules-on-bun-g.md). In particular the normalized fibre functor on \(B\mathbb G_m\) is \(p^![-2]\) over \(\mathbb C\). Fourier functors will be normalized by their inverse universal-line kernel, so a flat line on \(J\) corresponds to a skyscraper in degree zero. We specify separately the ordinary coherent Fourier–Mukai transform, which has a different shift.

## 1. The three automorphic and spectral factors

The family-and-arrow argument of [Sheaves and D-modules on Bun_G](sheaves-and-d-modules-on-bun-g.md) gives
\[
\operatorname{Bun}_{\mathbb G_m}
 \simeq J\times B\mathbb G_m\times\underline{\mathbb Z}.
                                                               \tag{1.1}
\]
Here \(J\) has degree zero. A family \(L\) of degree \(d\) is recovered from its rigidified degree-zero part, its base line and \(\mathcal O_X(dx_0)\). The factor \(B\mathbb G_m\) records scalar automorphisms; \(\underline{\mathbb Z}\) records the locally constant degree.

Using the differential trace proved in §§1.1.8–1.1.16 and the classical Picard/cohomology foundations specified in §1.1, \(J^\natural\) is the smooth moduli scheme of degree-zero flat lines on \(X\), rigidified at \(x_0\). Its connection torsor gives the exact sequence below. Sections 4.2.8–4.2.9 identify it with the constructed universal vector extension under Abel-normalized self-duality. Sections 4.2.22–4.2.29 construct the effective theta divisor and prove its ampleness and conventional polarization sign within the stated geometric foundations:
\[
0\longrightarrow H^0(X,\Omega_X^1)_{\mathrm{add}}
 \longrightarrow J^\natural\longrightarrow J\longrightarrow0.
                                                               \tag{1.2}
\]
The fibre over a degree-zero line is the torsor of its connections under the indicated vector space. In positive genus this torsor presentation does not give a preferred product \(J\times\mathbb A^g\).

Set
\[
B=k[\epsilon]/(\epsilon^2),\quad |\epsilon|=-1,\quad d\epsilon=0,
\qquad
Z_{\mathrm{der}}=\operatorname{Spec}B
 =\operatorname{Spec}k\times^{\mathbf R}_{\mathbb A^1}\operatorname{Spec}k,
                                                               \tag{1.3}
\]
where both maps to \(\mathbb A^1\) land at zero. The rank-one spectral stack has the factorization
\[
\operatorname{LocSys}_{\mathbb G_m}(X)
 \simeq J^\natural\times Z_{\mathrm{der}}\times B\mathbb G_m.
                                                               \tag{1.4}
\]
Equation (1.4) uses the differential-duality/residue trace chain proved in §§1.1.8–1.1.16 and remains conditional on the complete recursive classical foundations specified below. Sections 1.1.1–1.1.6 prove the two derived bridges from their exact ordinary Picard inputs. The calculation below constructs the connection torsor and separates the derived zero equation using that trace. The chosen linear splitting of curve cohomology is an additional choice; the displayed product need not be canonical. [Arinkin–Gaitsgory §11.2](https://arxiv.org/abs/1201.6343) and [Frenkel §4.4](https://arxiv.org/abs/hep-th/0512172) provide human-source comparisons.

### 1.1. The connection obstruction and the derived degree equation

Let \(X/k\) be smooth, connected and projective of dimension one, with \(k\) algebraically closed of characteristic zero. Choose \(x_0\in X(k)\). Put \(J=\operatorname{Pic}^0(X)\), \(V=H^0(X,\Omega_X^1)\), and let \(J^\natural_X\) classify degree-zero lines with a relative connection and a rigidification at \(x_0\).

The exact earlier Picard-functor construction and deformation results used are [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) and [The structure of the Picard scheme](../../AG-HP/src/the-structure-of-the-picard-scheme.md): \(J\) is a smooth representing scheme, the normalized universal line exists after choosing the section \(x_0\), and the Picard stack splits into its rigidified part and the base line. Coherent cohomology/base change and curve Serre duality are the earlier AG-QC proofs used below. Their actual proof anchors and revisions are recorded, while their recursive classical foundations remain explicit proof obligations.

**Differential trace.** Sections 1.1.8–1.1.16 prove the trace-preserving identification of the constructed dualizing sheaf with \(\Omega_X^1\), its global residue formula and its fixed-curve base change, relative to the exact earlier foundations recorded there. With ordered Čech differential \((\delta\alpha)_{01}=\alpha_1-\alpha_0\), normalize the projective-line trace by \(\operatorname{tr}[t^{-1}dt]=1\). For the corresponding principal-parts connecting map \(\partial\), the required normalization is
\[
\operatorname{tr}(\partial\beta)=-\sum_p\operatorname{Res}_p(\beta_p).
\]
The proof below compares the actual globally constructed representing pair with differential trace and proves its compatibility on every ordinary and connective DG parameter.

**Proposition (relative to the specified classical foundations).** The functor \(J^\natural_X\) is a \(V_{\mathrm{add}}\)-torsor whose projection to \(J\) is affine and smooth, with a commutative group structure, and there is an exact sequence of group schemes
\[
0\longrightarrow V_{\mathrm{add}}\longrightarrow
J^\natural_X\longrightarrow J\longrightarrow0.
\tag{D1}
\]
Relative to the complete classical foundations just specified, choosing a linear splitting of the fixed curve cohomology complex in addition to \(x_0\) gives a global derived-stack equivalence
\[
\operatorname{LocSys}_{\mathbb G_m}(X)
\simeq J^\natural_X\times B\mathbb G_m
       \times\operatorname{Spec}(k[\epsilon]),\qquad
|\epsilon|=-1,\ d\epsilon=0.
\tag{D2}
\]
In particular (D2) is a statement about all test families, not an inference from tangent dimensions. Its presentation need not be canonical under changes of the chosen cohomology splitting.

**Proof.** We first construct the connection obstruction and its entire derived fibre. On affine trivializing opens \(U_i\) of a line \(L\), write the transition functions as \(g_{ij}\). Connection forms \(A_i\) must satisfy
\[
A_j-A_i=d_X\log g_{ij}.
\tag{D3}
\]
The right side is a Čech one-cocycle with values in \(\Omega_X^1\), because logarithmic differentiation sends multiplication to addition. Changing the frames changes this cocycle by a Čech boundary. It therefore defines the relative Atiyah-class map
\[
\operatorname{Pic}(X)\longrightarrow
\mathbb V(R\Gamma(X,\Omega_X^1)[1]).
\tag{D4}
\]
Here \(\mathbb V\) denotes the additive derived stack associated to the cochain complex. Its zero fibre consists of choices of a nullhomotopy of this cocycle: precisely the \(A_i\) in (D3), with their descent homotopies. Thus its homotopy fibre over zero is the derived stack of line bundles with connection.

For ordinary test algebras this is the connection descent calculation: choose two affine opens covering \(X\), with affine intersection, and further affine frame covers. Quasicoherent descent is computed by the Čech complex, and (D3) is its differential equation. On a curve the relative curvature vanishes because \(\Omega_X^2=0\). For arbitrary derived test algebras, §§1.1.3–1.1.6 construct (D4) from the intrinsic principal-parts triangle on the entire infinity-groupoid of lines and identify its full splitting space with rank-one de Rham crystals. The proof uses the pointed operator algebra and the actual coherent free bar; an ordinary Čech groupoid alone would not supply it.

By the trace-preserving duality in R7, \(H^1(X,\Omega_X^1)\simeq k\), dual to \(1\in H^0(X,\mathcal O_X)\). The ordered cocycle \(d\log g_{ij}\) has trace \(\deg L\). Indeed choose a nonzero rational section \(\sigma=e_i f_i\). Then \(f_i=g_{ij}f_j\), so for \(\beta_i=d\log f_i\),
\[
d\log g_{ij}=\beta_i-\beta_j=-(\delta\beta)_{ij}.
\]
At a zero or pole of order \(m\), the principal part of \(\beta_i\) has residue \(m\). Thus \(\operatorname{at}(L)=-\partial(\beta)\), and the specified connecting-map sign gives
\[
\operatorname{tr}(\operatorname{at}(L))
=-\operatorname{tr}(\partial\beta)
=\sum_p\operatorname{Res}_p(\beta_p)
=\deg L.
\]
Changing the rational section changes its Atiyah representative by a boundary. The family assertion uses the actual trace chain map (B3)–(B4), its fixed-curve base change and the F3–F4 factorization through the ordinary smooth Picard scheme. Sections 1.1.8–1.1.16 supply the global compatibility proof.

Choose a \(k\)-linear quasi-isomorphism
\[
R\Gamma(X,\Omega_X^1)[1]\simeq
     V[1]\oplus k[0].
\tag{D5}
\]
It exists because a complex of vector spaces splits into its cohomology and contractible summands; explicitly choose complements to its cycles and boundaries, then identify the induced differential on the remaining complement with the boundaries. The trace fixes the second summand. Tensoring this chosen quasi-isomorphism with any derived test algebra preserves it. The additive stack in (D4) is consequently
\[
BV_{\mathrm{add}}\times\mathbb A^1.
\tag{D6}
\]
The \(\mathbb A^1\) component of the Atiyah map is the locally constant degree just computed.

A connection can exist only in degree zero: in characteristic zero an integer degree is zero in \(k\) only when the integer is zero. On the degree-zero component, the Picard stack is \(J\times B\mathbb G_m\). The Atiyah map is unchanged by tensoring with a base line, since \(d_X\) of its transition functions is zero. It therefore factors through \(J\). Its \(\mathbb A^1\) component is the zero map. This is an equality of the map, not only a fibrewise obstruction check: the represented scheme \(J\) is classical and smooth, and its regular function given by the trace is identically zero.

The remaining map \(J\to BV_{\mathrm{add}}\) classifies a \(V_{\mathrm{add}}\)-torsor. Its fibre at the trivial torsor is exactly the ordinary moduli of rigidified connections, by (D3). This torsor is locally nonempty on \(J\): on an affine base chart, the relative Atiyah class has zero image in
\[
H^1(X,\Omega_X^1)\otimes\mathcal O_J
\]
and affine base acyclicity eliminates the other base cohomology contribution, so the cocycle admits a solution. Two solutions differ by a section of \(V\otimes\mathcal O_J\). Gluing these affine torsors represents \(J^\natural_X\), proving affine smoothness and dimension \(2g\). Tensor product of lines and the sum of their connection forms give its group law; the trivial line with its trivial connection is the unit, and dualizing gives the inverse. Its kernel over \(\mathcal O_X\) is exactly the connections \(d+A\), \(A\in V\), proving (D1). No principal polarization is needed for this torsor assertion.

It remains to retain the derived \(\mathbb A^1\) equation. With (D5), the fibre of the map
\[
(J\times B\mathbb G_m)\longrightarrow
BV_{\mathrm{add}}\times\mathbb A^1
\]
over \((0,0)\) is the product of its \(BV_{\mathrm{add}}\) fibre and
\[
\operatorname{Spec}k\times^{\mathbf R}_{\mathbb A^1}
                         \operatorname{Spec}k.
\]
The first is \(J^\natural_X\times B\mathbb G_m\); the second has algebra
\[
k\otimes^{\mathbf R}_{k[z]}k\simeq k[\epsilon],
\qquad |\epsilon|=-1.
\]
Indeed the Koszul resolution \(k[z][e]\), \(de=z\), becomes the exterior algebra on the degree-\(-1\) generator after setting \(z=0\). Together with the derived bridges proved below, this proves (D2) globally using the proved differential trace within the remaining recursive classical foundations. The infinitesimal check \(R\Gamma_{\mathrm{dR}}(X,k)[1]\) follows from the linearization of (D3), but it is a consequence and a check of the construction, not the argument establishing it. \(\square\)

#### 1.1.1. Fixed-curve cohomology, affine lines and nilcompleteness

In the following proofs \(S\) denotes a connective parameter algebra; it is distinct from the exterior algebra \(B\) in (1.3). Put \(P=\operatorname{Pic}(X,x_0)\), the ordinary rigidified Picard scheme, and \(W=H^1(X,\mathcal O_X)\). A line means a module locally equivalent to the structure sheaf in degree zero. Shifted invertible complexes are excluded.

The classical inputs are the actual rigidification, chart and universal-line arguments in [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md), Theorem 2.1 and §§4–7, and the transition-cocycle tangent calculation in [The structure of the Picard scheme](../../AG-HP/src/the-structure-of-the-picard-scheme.md), Theorem 3.1. Their recursive scheme, relative-Cartier, symmetric-power, cohomology and duality foundations retain the proof obligations stated below. The arguments here extend these specified classical inputs to all connective parameters; those recursive foundations remain explicit premises.

Use nonpositive commutative DG algebras over \(k\), with cohomological shifts \(M[1]^i=M^{i+1}\). For a complex \(C\), write
\[
\Omega^\infty C=\operatorname{Map}(k,C),\qquad
\pi_i(\Omega^\infty C)=H^{-i}(C)\quad(i\geq0).
\]
Modules are localized at quasi-isomorphisms, and their mapping spaces come from derived Hom complexes. Applying a mapping space to an exact triangle gives a fibre sequence. Positive cohomological degrees remain in the complexes and the derived equations they define.

Quasicoherent modules on a derived scheme are the limit of its affine module categories with derived restriction. A line is an object whose restrictions are locally free of rank one. The subgroupoid of lines therefore commutes with this limit: local freeness and equivalence of two modules are detected locally. These limits include paths and all higher homotopies.

Derived tensors and mapping complexes can be computed with semifree resolutions. Adjoin free generators to hit the cohomology classes of a complex, then generators one degree lower to kill the kernel, and repeat. Each class and relation is handled at a finite stage; the resulting filtered free complex is a quasi-isomorphic resolution. The corresponding module and algebra bars retain the full coherent action spaces. Their augmented underlying module bars have the extra degeneracy inserting the unit; its alternating contraction preserves finite support in their direct-sum realizations.

Choose two hyperplane sections \(D,D'\) with disjoint support in a projective embedding of \(X\). After the first finite section, a hyperplane avoiding its support exists over the infinite field \(k\). The complements \(U,V\) are affine, and their intersection is a principal affine open, cut out by the ratio of the two hyperplane equations. They cover \(X\). For a quasicoherent sheaf \(\mathcal F\) and any complex \(M\) over \(k\), including an unbounded one,
\[
R\Gamma(X,\mathcal F\otimes_k M)
\simeq
\bigl[\Gamma(U,\mathcal F)\oplus\Gamma(V,\mathcal F)
 \longrightarrow\Gamma(U\cap V,\mathcal F)\bigr]\otimes_k M.
\tag{F0.1}
\]
Here the two terms of the Čech complex have degrees zero and one. Its augmented sheaf complex is exact: on an open contained in either member of the cover it has the contraction supplied by that member. Quasicoherent sections on the affine intersections are exact module evaluation. The acyclic-cover comparison thus computes derived sections by this complex, as in the actual argument of Čech cohomology, Theorems 2.1 and 3.2. Applying it degree by degree has a finite Čech direction, so each total degree uses finite sums. This proves (F0.1) without an unbounded convergence claim. In particular
\[
\begin{aligned}
R\Gamma(X,\mathcal O_X\otimes_k M)
 &\simeq R\Gamma(X,\mathcal O_X)\otimes_k M,\\
R\Gamma(X,\Omega_X^1\otimes_k M)
 &\simeq R\Gamma(X,\Omega_X^1)\otimes_k M.
\end{aligned}
\tag{F0.2}
\]
The fixed classical inputs give \(H^0(X,\mathcal O_X)=k\), and (F0.1) gives \(H^i(X,\mathcal F)=0\) for \(i>1\). The identification of the differential line with the dualizing sheaf and its trace is a separate foundation; it is not inferred from (F0.2).

For a connective algebra \(S\), components of \(\operatorname{Line}(S)\) are ordinary projective rank-one modules over \(H^0(S)\). The automorphism space of each line is \(\operatorname{GL}_1(S)\), the unit components of \(\Omega^\infty S\).

To prove the component assertion, write a finite projective \(H^0(S)\)-module as the image of an idempotent matrix \(e\). Lift it to a chain endomorphism of a finite free \(S\)-module, with a homotopy \(e^2\simeq e\). Form its telescope: the cofiber of \(1-\operatorname{shift}(e)\) on the direct sum of its free-module copies. Its cohomology is the image of the induced idempotent on \(H^*(S)\). Putting \(e\) on each summand gives a map from this cofiber to the original free module: its composite with \(1-\operatorname{shift}(e)\) is nullhomotopic by the chosen homotopy. Do the same for \(1-e\). The sum of these two maps is an isomorphism on every cohomology group, hence an equivalence. The telescope is consequently a retract of the finite free module. For rank one, its restriction to the classical frame cover is \(S\).

Conversely a locally free rank-one module \(L\) has, on that cover,
\[
H^*(L)=H^*(S)\otimes_{H^0(S)}H^0(L).
\]
A map from the constructed projective lift to \(L\) lifting the identity of \(H^0(L)\) exists: the source is a retract of a finite free module, so degree-zero cohomology of its mapping complex is the ordinary Hom on these projective \(H^0\)-modules. That map is an isomorphism on all cohomology groups locally, hence an equivalence. Tensoring \(L\) with its dual gives \(\operatorname{RHom}_S(L,L)\simeq S\); an endomorphism is invertible precisely when its \(H^0\)-class is a unit. This proves the automorphism assertion, including higher homotopies, compatibly with localization and base change.

Put \(S_n=\tau_{\geq-n}S\). Then
\[
\operatorname{Line}(S)\simeq
\lim_n\operatorname{Line}(S_n).
\tag{F1.1}
\]
Components are independent of \(n\). On a fixed component the automorphism groups have \(\pi_i=H^{-i}(S)\) once \(n\geq i\), and constant \(\pi_0\). The algebra \(S\) is the inverse limit of its truncations, degree by degree, so its unit space is their inverse limit. The same holds after delooping on each line component: the homotopy-group systems are eventually constant, giving no additional component or derived inverse-limit term. Equivalently compatible based loops and higher simplices give exactly those in the limit unit space. This proves (F1.1).

Apply (F1.1) on every intersection of an affine cover of \(X\). Its coordinate rings satisfy
\[
\tau_{\geq-n}(R\otimes_k S)=R\otimes_k S_n.
\]
The line descent limit commutes with the truncation limit. Thus the entire Picard space, including its morphisms, is nilcomplete:
\[
\operatorname{Pic}_X(S)\simeq
\lim_n\operatorname{Pic}_X(S_n).
\tag{F1.2}
\]

The derived extension of a smooth ordinary scheme \(Y\) is nilcomplete too. Cover \(Y\) by affine charts étale over affine spaces. Polynomial coordinate maps to \(S\) are tuples in \(\Omega^\infty S\), which commute with truncation limits. For an étale equation with invertible derivative, the derived lifting fibre at a fixed \(H^0\)-root has contractible extra choices: its linearized map is multiplication by that invertible derivative on each higher homotopy group. For several equations use the invertible Jacobian. On \(H^0\), lifts across a nilpotent ideal are the finite Newton correction; a general nil ideal is handled by the nilpotent ideal generated by the finitely many errors involved. This identifies components and every higher homotopy group at each truncation. Charts and their overlaps are determined by \(H^0\) and glue by limits. Hence \(Y(S)=\lim_nY(S_n)\), in particular for \(P,J\). Equation (F1.1) handles \(B\mathbb G_m\).

#### 1.1.2. Nonsplit lifting and the full derived Picard comparison

Let \(S\) be a connective commutative DG algebra and \(M\) a connective \(S\)-module. The split square-zero algebra \(S\oplus M\) has the usual graded product
\[
(b,m)(b',m')=(bb',bm'+mb').
\]
The kernel of its unit-space map over the identity is the additive space \(\Omega^\infty M\): the map is \(u\mapsto1+u\), and the product of two such elements is \(1+u+u'\) because \(M^2=0\). This assertion holds on the complexes presenting the higher unit spaces. Delooping and taking line descent on \(X\) therefore give, for every line \(L\) on \(X_S\),
\[
\operatorname{fib}_L\!\left(
 \operatorname{Pic}_X(S\oplus M)\longrightarrow
 \operatorname{Pic}_X(S)\right)
\simeq
\Omega^\infty\!\left(
 R\Gamma(X,\mathcal O_X)\otimes_k M[1]\right).
\tag{F2.1}
\]
Pullback along the splitting supplies its basepoint. Tensoring with \(L^{-1}\) identifies its endomorphism complex with \(\mathcal O_{X_S}\). The finite affine Čech complex of F0 computes the displayed complex for unbounded \(M\), as well as its paths and higher paths.

We next construct the actual square used for a Postnikov extension. This construction supplies a strict square-zero model, rather than just proving vanishing products on cohomology.

Represent \(S\) by a nonpositive commutative DG algebra. For \(n\geq1\), let \(E=\tau_{\geq-n}S\) be its smart truncation:
\[
E^i=
\begin{cases}
S^i,&i>-n,\\
S^{-n}/d(S^{-n-1}),&i=-n,\\
0,&i<-n.
\end{cases}
\]
It is a DG algebra. Multiplication descends because every coefficient has nonpositive degree and the differential obeys Leibniz. Its bottom cycles form the ideal
\[
I=Z^{-n}(E)=H^{-n}(S),
\]
placed in degree \(-n\). They form an actual ideal: multiplication by degree-zero coefficients preserves these cycles, while multiplication by negative-degree coefficients lands below the truncation. They have zero product with one another, since \(-2n<-n\). Hence
\[
E\longrightarrow C:=E/I
\]
is a strict square-zero extension by \(I\). The quotient \(C\) is quasi-isomorphic to \(\tau_{\geq-(n-1)}S\) via the natural truncation map. Indeed \(E\) has no cohomology below \(-n\), the inclusion of \(I\) is an isomorphism on that sole bottom cohomology group, and the quotient removes exactly that group. Thus this extension represents the actual arrow \(S_n\to S_{n-1}\). Its differential and its k-invariant have not been changed.

Here is a model computing its derivation square. Resolve \(C\) by a semifree commutative DG algebra \(Q\to C\), and take the strict pullback \(E'=E\times_C Q\). The projection \(E'\to Q\) is surjective with square-zero kernel \(I\), with its pulled-back \(Q\)-module structure. The map \(E'\to E\) is a quasi-isomorphism: compare the two exact sequences with common kernel \(I\) and quotient map \(Q\to C\).

Since the underlying graded algebra of \(Q\) is free, lift its generators through \(E'\to Q\). This gives a graded algebra section \(s:Q\to E'\). Its differential error is
\[
\delta(q)=d_{E'}s(q)-s(d_Qq)\in I.
\]
It is a degree-one derivation. The square-zero kernel makes its coefficient action independent of the chosen graded lifts, and \(d^2=0\) gives
\[
d_I\delta+\delta d_Q=0.
\]
Consequently \(\delta\), viewed in \(I[1]\) with the standard shifted module signs, defines the derived derivation section
\[
\kappa:Q\longrightarrow Q\oplus I[1].
\]
In the graded identification \(E'=Q\oplus I\), its differential is
\[
d(q,i)=\bigl(d_Qq,\ d_Ii+\delta(q)\bigr).
\]
This explicitly records the possibly nonzero k-invariant.

To verify the homotopy pullback, use the acyclic \(Q\)-module
\[
K=\operatorname{Cone}(\operatorname{id}_I).
\]
In coordinates \(K^m=I^m\oplus I^{m+1}\), its differential is
\[
d_K(v,u)=(d_Iv+u,-d_Iu).
\]
Projection \((v,u)\mapsto u\) is a surjective chain map \(K\to I[1]\). The square-zero algebra \(Q\oplus K\) gives a factorization of the zero section
\[
Q\ \xrightarrow{\;\simeq\;}\ Q\oplus K\
\longrightarrow Q\oplus I[1],
\]
whose second arrow is a fibration in the semifree DG model. Its strict pullback along \(\kappa\) consists of \((q,v,u)\) with \(u=\delta(q)\). The displayed differential then becomes exactly
\[
(q,v)\longmapsto(d_Qq,d_Iv+\delta(q)),
\]
so that this pullback is \(E'\). Therefore, after replacing \(Q\) by its equivalent algebra \(S_{n-1}\), the actual Postnikov arrow fits into
\[
\begin{array}{ccc}
S_n&\longrightarrow&S_{n-1}\\
\downarrow&&\downarrow\kappa\\
S_{n-1}&\xrightarrow{\ 0\ }&S_{n-1}\oplus I[1]
\end{array}
\qquad\text{a homotopy pullback.}
\tag{F2.2}
\]
If a graded section is changed by a degree-zero derivation \(\beta:Q\to I\), then its differential error changes by \(d_I\beta-\beta d_Q\). This is the corresponding derivation homotopy. The pullback construction takes that homotopy and all its higher paths to equivalences of the same derived extension. The construction is an argument in DG algebras and their derived mapping spaces; it does not discard these paths.

The Picard functor preserves this square:
\[
\operatorname{Pic}_X(S_n)\simeq
\operatorname{Pic}_X(S_{n-1})
\mathop{\times}_{\operatorname{Pic}_X(S_{n-1}\oplus I[1])}
\operatorname{Pic}_X(S_{n-1}).
\tag{F2.3}
\]
On each affine intersection of \(X\), unit spaces preserve the algebra pullback because underlying mapping spaces preserve limits and invertibility is detected in \(H^0\). Both sections into the split algebra induce an isomorphism on \(\pi_0\) of units: \(I[1]\) is concentrated in degree \(-n-1\). On a fixed line component the fibre product of the delooped unit spaces is connected, since these maps on \(\pi_0\) are surjective. Its loop space is their unit-space pullback. It is therefore the delooping of the units of the pullback algebra. The classical projective rank-one components agree as well, by F1 and the common \(H^0\). This proves the affine line assertion on full spaces. Tensoring the fixed affine coordinate rings over \(k\) preserves the finite algebra pullback. Taking the full Čech limits and commuting the two limits proves F2.3.

Smooth schemes and \(B\mathbb G_m\) preserve the same square. For schemes this is the mapping-space universal property of a homotopy pullback of affine algebras; the common \(H^0\)-point allows an affine target chart to be chosen on both sides. For \(B\mathbb G_m\) it is the preceding unit/delooping argument. They can therefore be compared across the actual nonsplit square.

For a smooth scheme \(Y\), the split-extension fibre at \(y\) is
\[
\Omega^\infty\!\left(y^*T_Y\otimes_S M\right).
\tag{F2.4}
\]
In an étale coordinate chart it is the full space of coordinate increments in \(M\). The invertible Jacobian gives the unique coherent étale lift. All quadratic terms vanish, so coordinate changes act by their Jacobian on the entire module complex. This proves the formula on spaces, including all higher paths, and glues it.

These formulas will compare every split-extension fibre in F3. The actual nonsplit square (F2.2) supplies its Postnikov induction, and F1 supplies the truncation limit.

The normalized universal line and a base line give the natural map
\[
\Phi:P\times B\mathbb G_m\longrightarrow\operatorname{Pic}_X.
\tag{F3.1}
\]
It respects tensor product, with the coherent normalized identifications supplied by the representing rigidified functor. On ordinary schemes its inverse pulls back at \(x_0\) and normalizes; this is the family-and-arrow rigidification proof in [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md), Theorem 2.1.

Compare full split-extension fibres. Translation in \(P\) identifies its tangent bundle with \(W\otimes\mathcal O_P\). At the identity, the transition-function calculation of [The structure of the Picard scheme](../../AG-HP/src/the-structure-of-the-picard-scheme.md) writes first-order transitions as \(1+u_{ij}\); these are Čech cocycles in \(\mathcal O_X\), and frame changes add boundaries. Differentiating the normalized universal line, and including base units, gives the chain map
\[
W[0]\oplus k[1]\longrightarrow R\Gamma(X,\mathcal O_X)[1].
\tag{F3.2}
\]
It induces the identity on \(H^0=W\) and on \(H^{-1}=k\), with no other cohomology by (F0.1); it is a quasi-isomorphism.

On a split extension by any connective module \(M\), transition increments are \(1+u\) in the full module complex. Their products add and their frame changes are its Čech boundary. Thus the map on the entire split-extension fibre is (F3.2) tensored with \(M\), including paths and higher paths; (F2.1) and (F2.4) identify its source and target. Tensor product translates every derived point to the identity, so this comparison holds over every point, not only the trivial line.

Induct on the truncation index. At \(n=0\), (F3.1) is the ordinary rigidification equivalence. For \(n>0\), use the actual nonsplit square (F2.2), with its derivation and ideal \(I=H^{-n}(S)\) in degree \(-n\). The comparison on \(S_{n-1}\oplus I[1]\) is an equivalence: it is so on the base by induction and on each fibre by the full split calculation. Naturality includes the actual derivation section and all its homotopies. Both functors preserve the square by (F2.3). Their pullbacks are therefore equivalent, proving the induction step with its obstruction paths and possible lifts. Independent nilcompleteness in F1 gives
\[
\operatorname{Pic}_X(S)\simeq P(S)\times B\mathbb G_m(S)
\tag{F3.3}
\]
for every connective \(S\), bounded or unbounded. All transformations are natural, so this is an equivalence of derived functors. Degree is detected on \(H^0\); restricting to its zero component gives
\[
\operatorname{Pic}_X^0\simeq J\times B\mathbb G_m.
\tag{F3.4}
\]
Framing at \(x_0\) takes the fibre of the second projection. This gives the derived extension of \(J\), whose value on a derived algebra can have higher homotopies.

#### 1.1.3. Principal parts and the coherent Atiyah map

Let \(Z=X\times\operatorname{Spec}S\). Let \(Z_1\) be the first infinitesimal neighbourhood of its relative diagonal, with projections \(p_1,p_2\), and define
\[
P^1(L)=(p_1)_*\bigl(\mathcal O_{Z_1}\otimes_{p_2,\mathcal O_Z}^{L}L\bigr).
\]
The diagonal is the base extension of the fixed smooth-curve diagonal. Its conormal bundle is \(\Omega_X^1\otimes_k S\). Its first-neighbourhood bimodule sequence is finite locally free on either side, so arbitrary base extension and derived tensor give the natural exact triangle
\[
L\otimes\Omega_X^1\longrightarrow P^1(L)\longrightarrow L
 \longrightarrow L\otimes\Omega_X^1[1].
\tag{F4.1}
\]
Tensor the connecting map with \(L^{-1}\), using its canonical evaluation. It gives
\[
\operatorname{at}(L)\in
\Omega^\infty R\Gamma(X,\Omega_X^1\otimes_k S)[1].
\tag{F4.2}
\]
Functoriality of the triangle and evaluation gives a map on isomorphisms, paths between them and every higher simplex. Using (F0.2), this is the coherent derived map
\[
\operatorname{at}:\operatorname{Pic}_X
\longrightarrow\mathbb V\bigl(R\Gamma(X,\Omega_X^1)[1]\bigr).
\tag{F4.3}
\]
Applying \(\operatorname{Map}_Z(L,-)\) to (F4.1) identifies its sections over \(\operatorname{id}_L\) with nullhomotopies of the connecting map. Consequently
\[
\operatorname{fib}_L\bigl(\operatorname{Pic}_X
\times_{\operatorname{at},\mathbb V}\{0\}\to\operatorname{Pic}_X\bigr)
\simeq\{\text{splittings of (F4.1), with all their homotopies}\}.
\tag{F4.4}
\]
The splitting defines a connection by subtracting it from the tautological first jet. The second-projection coefficient action gives its Leibniz identity. For frames \(e_j=e_i g_{ij}\) and \(\nabla e_i=e_iA_i\), this is
\[
A_j-A_i=g_{ij}^{-1}d_Xg_{ij}.
\tag{F4.5}
\]
Thus the ordered Čech representative is \(d\log g\). Its higher data come from the intrinsic triangle; limits on refinements give the same splitting space. Base lines have the canonical constant relative splitting. Tensoring by one leaves the Atiyah map unchanged with this specified homotopy. Tensor product adds line Atiyah classes and their splittings. These assertions include derived base lines, since the relative differential kills \(S\).

#### 1.1.4. The pointed operator algebra and its entire action space

On an étale coordinate chart \(\operatorname{Spec}R\subset X\), choose \(t\) with derivation \(\delta(t)=1\), and put \(A=R\otimes_k S\). The first-order bimodule \(E\) has left basis \(q,\partial\), with
\[
qf=fq,\qquad \partial f=f\partial+\delta(f)q.
\tag{F5.1}
\]
Here \(\delta\) kills the parameter algebra. A module for the derived free tensor algebra \(T_A(E)\), with underlying module \(L\) specified, is a coherent action \(E\otimes_A^LL\to L\), by the free-algebra adjunction and its bar resolution. Requiring the pointed \(q\)-action to be the identity takes a homotopy fibre. A model for that pointed algebra is
\[
C=T_A(E\oplus Ah),\qquad |h|=-1,\qquad dh=q-1,
\qquad hf=(-1)^{|f|}fh.
\tag{F5.2}
\]
The following resolved free-cell construction proves this model statement on full action spaces.

Regard \(E\) and the inclusion \(Aq\hookrightarrow E\) as DG \(A\)-bimodules. Resolve this inclusion jointly by the two-sided bimodule bars:
\[
P\longrightarrow \widetilde E,\qquad
P\simeq A,\qquad \widetilde E\simeq E.
\]
The inclusion is a relative semifree inclusion. To check this, each bar term has free outer \(A\)-actions, and the quotient is the bar on \(E/Aq\). Resolve its coefficient complexes by free \(k\)-complexes if necessary. The bar filtration then presents the inclusion by successive free \(A\)-bimodule cells. Its augmentations commute with the inclusion and its unit map \(\varepsilon:P\to A\). This resolves the whole pointed diagram, rather than its objects independently.

The free-algebra diagram is
\[
T_A(\widetilde E)\ \longleftarrow\ T_A(P)\
\xrightarrow{\;\varepsilon\;} A.
\]
Replace the right-hand arrow by the relative free-cell algebra
\[
T_A(P\oplus sP),\qquad |sp|=|p|-1,\qquad
d(sp)=p-\varepsilon(p)-s(dp).
\]
Its augmentation to \(A\) is a quasi-isomorphism. Translate the free generator to \(p'=p-\varepsilon(p)\); the generating complex is then the cone of the identity of \(P\). It has its explicit \(A\)-bimodule contraction, and every positive tensor word is contracted on its first cone factor, with the preceding-degree sign. Direct sums of those contractions prove the augmentation assertion even for unbounded \(A\). The inclusion \(T_A(P)\) is a free-cell inclusion, hence is a cofibration: lifts against a surjective quasi-isomorphism are constructed successively on these free generators and their differential boundaries.

The homotopy pushout is consequently represented by
\[
C_{\mathrm{res}}=T_A(\widetilde E\oplus sP),\qquad
d(sp)=i(p)-\varepsilon(p)-s(dp).
\]
The augmentation of bimodule bars gives a map to the displayed algebra
\[
C=T_A(E\oplus Ah),\qquad |h|=-1,\qquad dh=q-1.
\]
Here \(Ah\) is the shifted regular bimodule, so for homogeneous \(f\in A\) its relation is
\[
hf=(-1)^{|f|}fh.
\]
Filter both algebras by total word length. The scalar term \(-\varepsilon(p)\) lowers length. On associated graded, the comparison is the free tensor algebra on the quasi-isomorphism of cones
\[
(\widetilde E\oplus sP,\ d(sp)=i(p)-s(dp))
\longrightarrow
(E\oplus Ah,\ dh=q).
\]
Every generating cone is \(K\)-flat on both sides over \(A\): the bars are semifree, and the displayed cone is the cone of the map \(Aq\to E\), whose two terms are free as left and right modules. Thus each tensor word comparison is a quasi-isomorphism. The associated-graded comparison is a quasi-isomorphism. For the total comparison, take a cycle in its mapping cone, remove its finite highest word length using the associated-graded boundary, and repeat. The process terminates at length zero. This proves that \(C_{\mathrm{res}}\to C\) is a quasi-isomorphism without any completeness or boundedness assumption.

It follows that the displayed \(C\) really computes the homotopy pushout imposing a path from the pointed \(q\)-action to the identity. The free-algebra adjunction and the bimodule/module bar give, on the full underlying-module fibre at \(L\), exactly the homotopy fibre of
\[
\operatorname{Map}_A(E\otimes_A^L L,L)
\longrightarrow \operatorname{Map}_A(L,L)
\]
over the identity. Its path is the \(h\)-action. The model comparison above retains the coherent coefficient action; it does not enforce an unproved ordinary equality \(q=1\). The operator-filtration argument below shows \(C\simeq D_S\). Finite first-jet duality then identifies this full action fibre with the splitting space of the principal-parts triangle, as claimed in F5.4.

Map \(C\) to the relative Ore algebra
\[
D_S=A\langle\partial\rangle/
 (\partial f-f\partial-\delta(f))
\tag{F5.3}
\]
by \(q\mapsto1,\ h\mapsto0\). Filter \(C\) by its number of \(\partial\)-symbols. Coefficient rewriting lowers this filtration in its error term, and its only coefficient overlap is resolved by \(\delta(ff')=\delta(f)f'+f\delta(f')\). In associated graded, coefficients commute with \(\partial,q\), with graded commutation for \(h\). Put \(q'=q-1\). The pair \(h\mapsto q'\) is contractible. In each tensor word containing this pair, contract its first pair factor with the preceding-degree sign. Words containing only \(\partial\) give \(A[\partial]\). Thus the associated-graded map to \(\operatorname{gr}D_S=A[\partial]\) is a quasi-isomorphism.

Every cycle in the mapping cone has a finite largest \(\partial\)-degree. Remove that leading degree by the displayed contraction, subtract a boundary, and repeat down to degree zero. This finite procedure proves that \(C\to D_S\) is a quasi-isomorphism. All contractions are \(S\)-linear, so unbounded negative parameter cohomology introduces no convergence assumption.

The Ore algebra is the relative differential-operator algebra on this chart. Coefficient rewriting gives its left normal forms \(\sum_i f_i\partial^i\). Commuting a proposed zero relation of largest order \(n\) with \(t\) exactly \(n\) times gives \(n!f_n=0\). Characteristic zero makes \(n!\) invertible, proving independence by descent on the order. Conversely the principal-part pairing identifies the highest symbol of an order-\(n\) operator with \(R(dt)^n\). Subtract its coefficient multiple of \(\partial^n\), then descend on the order. The finite Taylor principal parts in F6 verify this pairing explicitly. Hence these normal forms describe the intrinsic operator sheaf.

A quasi-isomorphism of DG algebras gives equivalence of their derived module categories: resolve by free modules using the split bar; termwise extension of scalars is an equivalence, and its augmented realization is the original module. Extension and restriction therefore compose to the identity, including the underlying-module functor here. Apply this to \(C\to D_S\). Its pointed free-algebra property identifies the space of \(D_S\)-structures on \(L\) with coherent first-order actions having prescribed identity on \(q\).

Finite locally free first-jet duality identifies these actions with splittings of (F4.1): (F5.1) becomes Leibniz, and the \(q\)-condition becomes the identity on the diagonal. Tensor–Hom duality is an equivalence of mapping complexes, so this includes all paths and higher homotopies:
\[
\{\text{relative derived }D_S\text{-structures on }L\}
\simeq\{\text{splittings of (F4.1)}\}.
\tag{F5.4}
\]
Intrinsic jets and operators agree on coordinate overlaps. Taking their full descent limits gives this equivalence globally. The rank-one tangent bundle is essential: higher-dimensional pointed tensor algebras also need the commutator and curvature relations.

#### 1.1.5. The formal diagonal on all derived tests

Define \(X_{\mathrm{dR}}(Q)=X(H^0(Q)_{\mathrm{red}})\). A relative rank-one de Rham local system over \(S\) is a line on \(X_{\mathrm{dR}}\times\operatorname{Spec}S\); the parameter direction is retained.

The map \(X\to X_{\mathrm{dR}}\) has local lifts on every derived test. Lift coordinate values from \(H^0(Q)_{\mathrm{red}}\) to \(H^0(Q)\), choose representatives in \(Q\), and lift the étale coordinate chart by its invertible Jacobian. The finite nil-error correction and derived coordinate lifting in F1 give these lifts. Pulling back coordinate charts covers \(\operatorname{Spec}H^0(Q)\), hence the derived test. This proves local surjectivity.

The Čech nerve \(N_r\) is the formal completion of \(X^{r+1}\) along its main diagonal: tuples lie in the nerve precisely when their reductions are the same point. Over a chosen local lift the augmented nerve has the extra degeneracy inserting that lift; this contracts its fibre. Two choices compare on their common nerve, so sheafifying its realization gives \(X_{\mathrm{dR}}\). Mapping it into the line sheaf yields
\[
\operatorname{Line}(X_{\mathrm{dR}}\times\operatorname{Spec}S)
\simeq \operatorname{Tot}_{r\geq0}
 \operatorname{Line}(N_r\times\operatorname{Spec}S).
\tag{F6.1}
\]
Line descent is the full module descent of F0; equivalently its additive Postnikov layers and ordinary line descent, with F1 nilcompleteness, give the same sheaf. Thus this totalization retains all higher units.

On an étale chart, differences \(\xi_1,\ldots,\xi_r\) from the first point give the finite boxes
\[
R[\xi_1,\ldots,\xi_r]/(\xi_1^{m+1},\ldots,\xi_r^{m+1}),
\tag{F6.2}
\]
finite free over \(R\) and cofinal with powers of the diagonal ideal. Their Koszul resolutions have \(|a_i|=-1,\ da_i=\xi_i^{m+1}\); the one-variable mapping cone and induction prove exactness of this regular sequence. A derived test point with nilpotent difference classes factors through a box up to homotopy by choosing nullhomotopies of these powers.

The extra choices become contractible in the filtered union. Increasing \(m\) to \(m'\) sends \(a_i\) to \(\xi_i^{m'-m}a_i\). On each homotopy group it eventually kills the choice: a sufficiently high power of \(\xi_i\) is a boundary, and multiplication by its primitive supplies the chain nullhomotopy on the full test complex. Each simplex or fixed homotopy group uses finitely many generators and homotopies, so one larger bound suffices. Surjectivity and injectivity on all homotopy groups identify this union with the formal-diagonal functor, including arbitrarily negative test cohomology.

The other-vertex action on its jet bimodule is
\[
f(t+\xi)=\sum_{a\geq0}\frac{\delta^a(f)}{a!}\xi^a.
\tag{F6.3}
\]
Each box makes this sum finite. Leibniz and the binomial identity prove multiplicativity. The étale equation is respected by its unique Jacobian lift, extending the polynomial formula to the chart. This constructs the intrinsic bimodule actions and composition without analytic convergence.

#### 1.1.6. Every DG module and the full crystal nerve

Work on an étale coordinate chart \(U=\operatorname{Spec}R\) of the fixed smooth curve, with coordinate \(t\), derivation \(\delta(t)=1\), and any connective parameter algebra \(S\). Put \(A=R\otimes_k S\), and let
\[
D=D_S=A\langle\partial\rangle/
  (\partial f-f\partial-\delta(f)).
\]
The derivation kills \(S\). The PBW normal forms in F5 show that \(D\) is free as both a left and a right \(A\)-module, with basis the powers of \(\partial\); its DG differential acts only on \(S\). In particular these bimodules are \(K\)-flat, even when \(S\) is unbounded.

Let \(G_p\) be the \(p\)-th infinitesimal groupoid term over this chart and over the unchanged parameter \(S\). Use adjacent displacements \(h_j=t_j-t_{j-1}\). Its finite boxes have rings
\[
S_{p,n}=A[h_1,\ldots,h_p]/(h_1^n,\ldots,h_p^n),
\qquad n\geq1.
\]
Each vertex map \(q_j:G_{p,n}\to U_S\) is finite free. Taylor expansion changes from one vertex coordinate to another. Its coefficient transformation has the inverse given by the opposite displacement. The formal boxes of F6, their derived Koszul presentations, and these adjacent boxes are cofinal; a finite triangular coordinate substitution only requires an increased bound. Faces and degeneracies are therefore maps of these filtered formal objects after increasing bounds when necessary.

Write
\[
\mathcal C_S=
\operatorname{Tot}_{p\geq0}
\left(\lim_n S_{p,n}\text{-}\operatorname{Mod}\right).
\]
By F6 this is \(\operatorname{QCoh}(U_{\mathrm{dR}}\times\operatorname{Spec}S)\). Evaluation at \(p=0\) is conservative: every component of a cartesian descent object is identified with a vertex pullback of that component. It preserves colimits, including realizations. The finite-stage restriction functors are derived tensor functors, hence preserve colimits; colimits of cartesian diagrams are computed componentwise, and remain cartesian. This proves the assertion on the defining category, rather than inferring it from a heart.

For a single finite box \(P_n=S_{1,n}\), denote its two \(A\)-actions by \(A_0,A_1\). Its left-vertex dual is
\[
D_n=\operatorname{Hom}_{A_0}(P_n,A_0).
\]
Its left \(A_0\)-action is multiplication on the output, and its right \(A_1\)-action is precomposition with the other-vertex action:
\[
(f\lambda)(p)=f\lambda(p),\qquad
(\lambda g)(p)=\lambda(g(t+h)p).
\]
The functional dual to \(h^a\) is \(\partial^a/a!\), through order \(n-1\). Consequently
\[
\partial f=f\partial+\delta(f),
\qquad \operatorname*{colim}_nD_n=D.
\]
The factorial is essential: evaluation of \(\partial^a\) on \(h^a\) is \(a!\). Finite tensor–Hom duality, with these specified actions, gives
\[
\operatorname{RHom}_{A_0}
 (D_n\otimes_{A_1}^{L}M,N)
\simeq
\operatorname{RHom}_{S_{1,n}}
 (q_1^*M,q_0^*N).
\tag{F7.1}
\]
Indeed the right side is
\(\operatorname{RHom}_{A_1}(M,P_n\otimes_{A_0}^{L}N)\);
dualizing the finite free left-vertex module gives the left side. This is an equality of derived mapping complexes, for arbitrary DG modules.

Pass to the inverse limit of the finite-box mapping complexes. Mapping out of the filtered union \(D\) gives their inverse limit, so
\[
\operatorname{RHom}_{G_1}(q_1^*M,q_0^*N)
\simeq
\operatorname{RHom}_A(D\otimes_A^L M,N).
\]
Repeating this in \(p\) adjacent slots gives
\[
\operatorname{RHom}_{G_p}(q_p^*M,q_0^*N)
\simeq
\operatorname{RHom}_A(T^pM,N),\qquad
T=D\otimes_A^L-.
\tag{F7.2}
\]
Completed coefficients on the formal side mean the inverse limit of the finite tensor pullbacks; no tensor is exchanged with an infinite product. The finite coefficient restrictions form degreewise surjective product towers, whose homotopy limit is the actual product complex. This can be checked by the cone of \(1-\mathrm{shift}\) on the product of the tower: that map is surjective, and its kernel is the compatible product. This remains true for all complexes.

Under F7.2, adding two adjacent displacements is multiplication of the two differential-operator distributions. On a coefficient \(f\), the coefficient of \(h^a h'^b\) in
\(f(t+h+h')\) is \(\delta^{a+b}(f)/(a!b!)\).
Translation of an intermediate coefficient gives precisely the Leibniz commutator displayed above. Repetition of a vertex restricts a displacement to zero and dualizes to the operator unit. These are identities of chain maps; the differential of \(S\) commutes with every coefficient operation. Therefore the mapping-complex equivalences commute with all faces and degeneracies, including their paths and higher paths.

For a strict DG \(D\)-module \(P\), finite Taylor transport is
\[
q_1^*P_0\longrightarrow q_0^*P_0,\qquad
1\otimes m\longmapsto
\sum_{a=0}^{n-1}\frac{h^a}{a!}\otimes\partial^a m,
\]
where \(P_0\) is its underlying \(A\)-module. The Leibniz rule makes it balanced for the two vertex actions. The binomial identity gives the cocycle; the inverse uses the opposite displacement with the vertex also changed. It commutes with the DG differential. These transports define a functor
\[
\Phi_S:D\text{-}\operatorname{Mod}\longrightarrow\mathcal C_S.
\]
It preserves colimits because its finite-box components are derived tensor pullbacks. These formulas can be computed after a free DG \(D\)-resolution, so they define the functor on the derived category.

We first prove full faithfulness on all objects. For \(D\)-modules \(P,Q\), use the transport of \(P\) to identify its source vertex with the last vertex in each nerve term. F7.2 identifies their complete crystal mapping complex with
\[
\operatorname{Tot}_{p\geq0}
 \operatorname{RHom}_A(T^pP_0,Q_0).
\tag{RF7.a}
\]
The outside cofaces use the actions on \(P,Q\), the intermediate cofaces multiply adjacent copies of \(D\), and the codegeneracies insert the unit. These are exactly the bar mapping-complex maps, by the preceding coefficient calculations.

Form the augmented simplicial \(D\)-module
\[
\mathcal S_p(P)=D\otimes_A^L T^pP_0,\qquad p\geq0.
\]
After restriction to \(A\), insertion of \(1\in D\) at the first position is an extra degeneracy of the augmented bar. It contracts its direct-sum realization to \(P_0\). For strict DG models, the extra degeneracy with the internal-degree sign is a contracting homotopy on the augmented normalized total complex. It preserves finite support in the simplicial direct sum. Thus
\[
|\mathcal S_\bullet(P)|\simeq P
\]
without boundedness or spectral-sequence convergence assumptions. Derived tensor–Hom adjunction and the universal property of a realization now give
\[
\operatorname{RHom}_D(P,Q)
\simeq
\operatorname{Tot}_{p\geq0}
\operatorname{RHom}_A(T^pP_0,Q_0).
\]
Comparison with RF7.a proves full faithfulness, including all derived mapping complexes.

We next resolve an arbitrary derived descent object; this is the step that a mapping totalization alone does not supply. Let \(\mathcal N\in\mathcal C_S\), with evaluated module \(M\). Its full transport
\[
\varphi:q_1^*M\xrightarrow{\ \simeq\ }q_0^*M
\]
has its actual triangle cocycle and all higher cocycle homotopies. Its mate under F7.2 is
\[
\alpha:TM\longrightarrow M.
\tag{RF7.b}
\]
The diagonal condition gives the unit homotopy. On two adjacent differences the comparison using their sum mates to \(\alpha\mu_M:T^2M\to M\); the comparison through the middle vertex mates to \(\alpha T(\alpha)\). The supplied triangle cocycle therefore mates to their actual associative homotopy. On \(G_p\), every string of vertex compositions mates to the corresponding string of multiplications and actions on \(T^pM\). The higher cocycle paths mate to the higher paths between those strings. F7.2 identifies their full mapping complexes and every structural map, so this operation retains all coherences. We have not reconstructed them from the first derivative.

There is a free-to-descent counit
\[
\varepsilon_{\mathcal N}:
\Phi_S(D\otimes_A^L M)\longrightarrow\mathcal N.
\tag{RF7.c}
\]
At the evaluated vertex it is \(\alpha\). Its full horizontality is constructed as follows. Pair the transport \(\varphi\) with a finite-order distribution in one difference; this sends \(\partial^a\otimes m\) to its coefficient \(\alpha(\partial^a\otimes m)\). Pair the actual triangle cocycle with the same distribution on a triple neighborhood. Its two endpoints are exactly transport followed by that map and that map followed by free Taylor transport. It therefore supplies the horizontality homotopy. Pair every higher cocycle with the finite distribution in the same way; the mapping-complex adjunction sends these to the higher naturality homotopies. The distributions form the filtered union \(D\), so these constructions fit together. They give a morphism in the entire descent totalization, not just a map at its zeroth vertex.

Take the augmented simplicial crystal with terms
\[
\mathcal S_p(\mathcal N)=
\Phi_S(D\otimes_A^L T^pM),\qquad p\geq0.
\tag{RF7.d}
\]
Its first and intermediate faces use multiplication, its last face uses RF7.b by free induction, and RF7.c supplies its augmentation. The unit gives degeneracies. The transposed higher cocycles give the higher simplicial identities, so this is a full coherent simplicial object. After evaluation it is the augmented monad bar with terms \(T^{p+1}M\), with its coherent extra degeneracy inserting the unit.

A split augmented simplicial object realizes to its augmentation even with coherent identities. One direct verification inserts the extra vertex and uses barycentric coordinates
\[
(t_0,\ldots,t_p)\longmapsto
(1-\lambda,\lambda t_0,\ldots,\lambda t_p),
\qquad 0\leq\lambda\leq1.
\]
The extra-degeneracy identities identify its endpoints with the augmentation and the original simplex and identify its restrictions on faces and degeneracies. Their provided higher identities give the same compatibility in the coherent realization. This is a contraction of the realization, on every mapping space. In strict DG models it is the normalized-bar contraction already described. Consequently the evaluated augmentation of RF7.d is an equivalence to \(M\). Evaluation preserves this realization and is conservative, so
\[
|\mathcal S_\bullet(\mathcal N)|\simeq\mathcal N.
\tag{RF7.e}
\]

Every term of RF7.d is in the image of \(\Phi_S\). The full faithfulness already proved lifts the entire coherent simplicial diagram to \(D\)-modules. Continuity of \(\Phi_S\) puts its realization in the image. RF7.e therefore proves essential surjectivity:
\[
\Phi_S:D_S\text{-}\operatorname{Mod}
\xrightarrow{\;\simeq\;}
\operatorname{QCoh}(U_{\mathrm{dR}}\times\operatorname{Spec}S).
\tag{RF7.f}
\]
Under this equivalence evaluation is restriction of scalars, induction is \(D_S\otimes_A^L-\), the unit is \(m\mapsto1\otimes m\), the counit is RF7.c, and the derived monad is \(D_S\otimes_A^L-\) with its operator multiplication. The proof includes every DG module and every coherent morphism, not only lines or bounded objects.

Restrict RF7.f to the objects whose evaluated module is a line. Their formal components are all vertex pullbacks of that line and hence are lines. Conversely a line crystal has such an evaluated line. Since the equivalence commutes with evaluation, its homotopy fibre over any specified line is exactly the full space of \(D_S\)-module structures on that line. F5's pointed-algebra proof and finite first-jet duality identify this with the entire principal-parts splitting space.

The formal transport is invertible in this comparison. For a strict line in a local frame its finite jet matrix is \(1+K\), where \(K\) belongs to the nilpotent difference ideal, and its inverse is the finite geometric series. For coherent transport with diagonal identity specified by a path, its cone restricts to zero on the diagonal. Filter the finite jet ring by its nilpotent diagonal ideal. Each subquotient is a diagonal module; its derived tensor with the cone factors through the zero diagonal restriction. The finite exact triangles then show the cone is zero. This proves invertibility for all complexes without any connectivity bound on that cone.

All comparisons use intrinsic finite principal parts, their vertex actions, their composition and their dual distribution multiplication. A change of étale coordinate preserves these objects and maps. The explicit coefficients verify those intrinsic maps, so the entire comparisons, counits and free bars agree on overlaps. Taking their full module-descent limits on \(X\) gives the equivalence for the fixed curve and its unchanged parameter \(S\). Combining it with F4's coherent triangle and F5's pointed comparison proves
\[
\operatorname{LocSys}_{\mathbb G_m}(X)
\simeq
\operatorname{Pic}_X
\mathop{\times}_{\mathbb V(R\Gamma(X,\Omega_X^1)[1])}
\{0\}.
\tag{F7.4}
\]
This is the global derived Atiyah fibre on every connective test algebra. The two infinite operations used above are separate: the formal coefficient limit is the inverse limit of finite free jets, while the mapping totalization is derived Hom out of an actually split free-bar realization. There is no exchange of an infinite tensor product and product, no inference from an equivalence of hearts, and no boundedness assumption on \(S\) or on the modules.

#### 1.1.7. The exact boundary of the derived splitting

Equations (F3.3)–(F3.4) prove the derived Picard comparison from the specified ordinary Picard inputs. Equation (F7.4) proves the coherent Atiyah/crystal fibre on every connective parameter algebra, retaining the parameter direction and all mapping-space coherences. In particular these are full derived bridges; a tangent-space computation is not their proof.

For the product (D2), §§1.1.8–1.1.16 supply the trace-preserving differential identification, global residue formula and fixed-curve base change. The actual constructed representing-pair theorem Dualizing sheaves and Serre duality for projective schemes, Theorem 4.1, is used at its precise boundary; its later imported smooth-canonical identification is replaced by the proof here. Its recursive Ext and local-algebra foundations remain explicit.

Using that trace chain, (D5) splits the target into \(BV_{\mathrm{add}}\times\mathbb A^1\). The base-line invariance of F4 and (F3.4) make the degree-zero map factor through the derived extension of the ordinary smooth \(J\). Its trace is the actual zero function on \(J\), hence the zero map on every derived family. The \(BV_{\mathrm{add}}\)-fibre is the ordinary connection torsor constructed above, as a derived functor: it is the pullback of the universal vector-group torsor. The remaining zero equation has the explicit Koszul algebra \(k[\epsilon]\) of (1.3).

Thus, within the specified recursive classical foundations, framing at \(x_0\) gives \(J_X^\natural\times Z_{\mathrm{der}}\). It removes \(B\mathbb G_m\) and retains the derived factor. In genus zero the framed stack is still \(\operatorname{Spec}k[\epsilon]\). These assertions concern full derived mapping spaces.

The identification of \(J_X^\natural\) with the universal vector extension of the dual Jacobian, the principal polarization, abelian biduality and the identity class of the Poincaré connection torsor use the geometric Lemma G and its stated foundations. They do not follow from the connection torsor or the framed derived factor alone.

Free human-source comparisons for these definitions are Jacob Lurie's [Derived Algebraic Geometry, §§3.3 and 8.2](https://www.math.ias.edu/~lurie/papers/DAG.pdf), and Gaitsgory–Rozenblyum's [Crystals and D-modules, §§3.1, 3.4 and 5.4–5.5](https://people.mpim-bonn.mpg.de/gaitsgde/GL/Crystalstext.pdf), in the author manuscript dated 1 October 2014. The explicit constructions above supply the derived bridge arguments.

#### 1.1.8. Local differentials and an intrinsic residue

We now prove the differential trace used above. Let \(k\) be algebraically closed of characteristic zero and let \(X\) be a smooth connected projective curve over \(k\). Put \(K=k(X)\). All differentials in this argument are relative to \(k\).

We use the ordered Čech convention

\[
(\delta a)_{ij}=a_j-a_i.
\tag{R0}
\]

For line-bundle frames, our convention is \(e_j=e_i g_{ij}\), and the Atiyah class is \([d\log g_{ij}]\). On \(\mathbf P^1\), with \(t=T_1/T_0\), the trace is normalized by

\[
\operatorname{tr}_{\mathbf P^1}([t^{-1}dt])=1.
\tag{R1}
\]

With these conventions the principal-part connecting map has a **minus** sign:

\[
\operatorname{tr}_X(\partial\beta)
=-\sum_{p\in X(k)}\operatorname{Res}_p(\beta_p),
\qquad
\operatorname{tr}_X(\operatorname{at}(L))=\deg L.
\tag{R2}
\]

Both formulas are proved globally below. Replacing \(\partial\) by its negative reverses the first displayed sign; it must not silently reverse the convention for the Atiyah class.

The earlier programme inputs used below are actual written proofs: [Noetherian and Artinian rings](../../AG-CA/src/noetherian-and-artinian-rings.md), Theorem 4.2 and Theorem 6.1; [The Nullstellensatz and Jacobson rings](../../AG-CA/src/the-nullstellensatz-and-jacobson-rings.md), Theorems 1.3 and 2.1–2.2; [Kähler differentials](../../AG-CA/src/kahler-differentials.md), Lemma 6.1 and Theorem 6.2; [Smooth algebras over a field and the Jacobian criterion](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md), Theorem 2.1 and Proposition 3.1; [Cohomology of sheaves on ringed spaces](../../AG-QC/src/cohomology-of-sheaves-on-ringed-spaces.md), Theorem 2.3 and Corollary 2.4; Čech cohomology, Theorems 2.1, 3.2 and 4.1; and Dualizing sheaves and Serre duality for projective schemes, Proposition 1.1 and Theorem 4.1. The one-dimensional local-ring argument, the elementary affine module comparison needed for Čech computations, the finite projection, the differential trace pairing, and the projective-line Hom duality are proved here. In particular, neither the smooth-canonical-bundle assertion in the bibliography of Dualizing sheaves and Serre duality for projective schemes nor a residue theorem from an external source is being substituted for this argument.

The smooth local-ring theorem of [Smooth algebras over a field and the Jacobian criterion](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md) gives regular local rings. Its rational-point cotangent calculation identifies \(\mathfrak m_p/\mathfrak m_p^2\) with \(\Omega^1_{X/k}\otimes k(p)\). Closed points have residue field \(k\), by [The Nullstellensatz and Jacobson rings](../../AG-CA/src/the-nullstellensatz-and-jacobson-rings.md). At a closed point, the local dimension and the cotangent dimension are both one. Nakayama therefore gives \(\mathfrak m_p=(u)\). The elementary Nakayama argument used here is this: if a finite module \(M\) satisfies \(M=\mathfrak mM\), write a finite generating column as its product with a matrix having entries in \(\mathfrak m\). The determinant of the identity minus that matrix is a unit and annihilates every generator, so \(M=0\). Apply this to the quotient by lifts of a cotangent basis.

We can prove the required domain and DVR assertions directly in dimension one. In \(A=\mathcal O_{X,p}\), the element \(u\) is not nilpotent, since otherwise every prime would contain \((u)=\mathfrak m_p\) and \(A\) would have dimension zero. Krull intersection, proved in [Noetherian and Artinian rings](../../AG-CA/src/noetherian-and-artinian-rings.md), gives \(\bigcap_nu^nA=0\). A nonzero \(a\in A\) therefore has a largest \(m\) with \(a\in u^mA\), and may be written \(a=u^mv\), where \(v\notin\mathfrak m_p\) is a unit. The product of two nonzero such expressions is nonzero, because no power of \(u\) is zero. Thus \(A\) is a domain and a DVR. A zero-dimensional regular local ring is a field, by the same Nakayama argument. All local rings of this curve are consequently domains. Distinct irreducible components cannot meet: at an intersection their local ring would have two minimal primes. There are finitely many components, each open and closed; connectedness makes \(X\) integral.

The Jacobian differential presentation in the proof of [Smooth algebras over a field and the Jacobian criterion](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md), Theorem 2.1, also proves that \(\Omega^1_{X/k}\) is a line bundle: in a standard smooth presentation, the invertible Jacobian minor solves for the relation differentials, leaving exactly one free differential generator. The cotangent calculation and Nakayama show that \(du\) generates its stalk at \(p\). Iteratively subtracting residue-field constants and dividing by \(u\) identifies the completion of \(A\) with \(k[[u]]\): the expansion is unique by separatedness, and its partial sums give every element of the complete ring. Thus

\[
\widehat A\simeq k[[u]],
\qquad
\Omega^1_{X/k,p}\otimes_A\widehat A\simeq k[[u]]\,du.
\tag{R3.1}
\]

Here the completed differential is the continuous derivative. We are completing the finite differential line on \(X\); we are not claiming that the ordinary algebraic module \(\Omega^1_{k[[u]]/k}\) is this line. For elements of \(A\), differentiation agrees with termwise differentiation after completion: differentiation sends \(u^nA\) into \(u^{n-1}A\,du\), so the identity follows by taking the limit of the polynomial partial sums.

Every rational differential has a Laurent expansion with finitely many negative terms. Define

\[
\operatorname{Res}_p\left(\sum_{n\gg-\infty}a_nu^n\,du\right)=a_{-1}.
\tag{R3.2}
\]

This definition does not depend on the parameter. Indeed, in characteristic zero such a differential can be written

\[
a_{-1}\,\frac{du}{u}+dh,
\qquad
h=\sum_{n\ne-1}\frac{a_n}{n+1}u^{n+1}\in k((u)).
\tag{R3.3}
\]

In another parameter \(v\), write \(u=v c(v)\), where \(c(v)\in k[[v]]^*\). Then \(du/u=dv/v+dc/c\), and \(dc/c\) is regular. A termwise derivative of a Laurent series in \(v\) has no \(v^{-1}dv\) term. Substitution in \(h\) is a well-defined Laurent series, so (R3.3) proves coordinate independence.

The principal-part space is

\[
\operatorname{PP}_p(\Omega_X)
=\Omega^1_{K/k}/\Omega^1_{X/k,p}
\simeq k((u))\,du/k[[u]]\,du.
\tag{R3.4}
\]

For the asserted isomorphism, injectivity follows from the valuation criterion for membership in the DVR. Every finite polar part is represented by a finite \(k\)-linear combination of \(u^{-m}du\), which is already a rational differential. Thus completion introduces no new principal parts. Residue factors through (R3.4).

#### 1.1.9. A finite flat projection, constructed explicitly

Choose a projective embedding \(X\subset\mathbf P^N\), with homogeneous coordinate domain \(S\) generated in degree one. Choose a closed point \(p_0\). A hyperplane through \(p_0\) can be chosen not to contain \(X\): the intersection of all hyperplanes through that point is the point itself, whereas \(X\) has dimension one. Let \(s_0\in S_1\) define such a hyperplane. Its zero set \(D_0\) on \(X\) is nonempty and finite. This uses only that a proper closed subset of a Noetherian integral one-dimensional scheme has finitely many irreducible components, all points.

Choose \(s_1\in S_1\) nonzero at every point of \(D_0\). This is possible because \(k\) is infinite and a finite union of proper linear subspaces cannot exhaust \(S_1\). The pair \((s_0,s_1)\) has no common zero and defines a morphism

\[
f:X\longrightarrow\mathbf P^1,
\qquad x\longmapsto[s_0(x):s_1(x)].
\tag{R4.1}
\]

Here is a direct finiteness proof. Write the degree-one generators of \(S\) as \(x_0,\ldots,x_N\). The projective scheme of \(S/(s_0,s_1)\) is empty. Hence every \(x_i\) has a power in \((s_0,s_1)\). To see the implication, if the image of \(x_i\) were not nilpotent, the degree-zero part of its homogeneous localization would be a nonzero ring, and its spectrum would give a nonempty standard open of that projective scheme. Choose powers \(x_i^{n_i}\in(s_0,s_1)\). Every monomial of degree greater than \(\sum_i(n_i-1)\) contains one of these powers and lies in \((s_0,s_1)\). Writing it as \(s_0a+s_1b\), with homogeneous \(a,b\) of one smaller degree, and inducting on degree shows that finitely many monomials generate \(S\) as a \(k[s_0,s_1]\)-module.

The forms \(s_0,s_1\) are algebraically independent. A relation can be taken homogeneous. Over an algebraically closed field, a nonzero homogeneous polynomial in two variables is a product of linear forms. Since \(S\) is a domain, a relation would imply a proportionality between \(s_0\) and \(s_1\). This is excluded by their values at \(p_0\). Therefore \(k[s_0,s_1]\) is a polynomial ring in these two generators.

On the first standard chart, the degree-zero localization \((S[s_0^{-1}])_0\) is finite over \(k[t]\), where \(t=s_1/s_0\). If \(h\) is a homogeneous module generator of degree \(d\), its degree-zero generator is \(h/s_0^d\). These finitely many elements give the asserted finiteness. The second chart is the same argument over \(k[w]\), with \(w=t^{-1}\). Consequently (R4.1) is finite and dominant.

Each of these finite coordinate modules is torsion-free over the polynomial PID, since it is a subring of \(K\). A finite torsion-free module over a PID is free: choose a basis after tensoring with the fraction field, clear the denominators of finitely many module generators, and regard a scalar multiple of the module as a submodule of \(R^r\). Such a submodule is free by induction on \(r\). Its first-coordinate image is a principal ideal; lifting its generator splits off that ideal, and its kernel lies in \(R^{r-1}\). Thus \(f\) is finite flat.

Put \(F=k(t)\). The extension \(K/F\) is finite separable, because the characteristic is zero. [Kähler differentials](../../AG-CA/src/kahler-differentials.md), Lemma 6.1, proves that derivations extend uniquely across finite separable extensions, by differentiating the separable minimal polynomial. Consequently

\[
\Omega^1_{K/k}=K\,dt.
\tag{R4.2}
\]

No proper-quasifinite theorem or normalization theorem is needed for this projection.

#### 1.1.10. The differential trace is an integral perfect pairing

For a rational differential \(\omega=b\,dt\), define

\[
T_f(\omega)=\operatorname{Tr}_{K/F}(b)\,dt.
\tag{R5.1}
\]

Changing the rational coordinate on the base preserves this definition: if \(dt=c\,dz\), then \(c\in F\), and field trace is \(F\)-linear. We will show that (R5.1) takes regular differentials to regular differentials and induces a perfect pairing over the finite algebra \(f_*\mathcal O_X\).

Fix a closed point \(q\in\mathbf P^1\), and let \(R=\mathcal O_{\mathbf P^1,q}\), with parameter \(z\). Let \(C=(f_*\mathcal O_X)_q\), a finite free \(R\)-algebra. Its special fibre has finitely many maximal ideals, corresponding to the points \(p\) above \(q\). The Artinian product decomposition of [Noetherian and Artinian rings](../../AG-CA/src/noetherian-and-artinian-rings.md), Theorem 4.2, applied to \(C/z^nC\), and then its inverse limit, gives

\[
C\otimes_R k[[z]]
\simeq\prod_{p\mid q}\widehat{\mathcal O}_{X,p}
\simeq\prod_{p\mid q} k[[u_p]].
\tag{R5.2}
\]

The factors are the local completions because localization selects the corresponding Artinian factor at every level. In each DVR, \(z\) has some positive valuation \(e_p\), so its powers define the same completion as powers of the local parameter. For a finite free \(R\)-module, tensoring with \(k[[z]]\) is precisely this inverse limit. Thus (R5.2) does not depend on an interchange involving an infinite non-finite module.

On one factor, initially write \(z=u_0^e v(u_0)\), with \(v\) a unit. Its constant term has an \(e\)-th root in \(k\). The binomial series for the remaining unit has an \(e\)-th root because \(e\) is invertible in \(k\). Replacing \(u_0\) by the formal parameter \(u=u_0v(u_0)^{1/e}\), we get

\[
z=u^e,
\qquad dz=e u^{e-1}du.
\tag{R5.3}
\]

The substitution is invertible, since its linear term is nonzero. It is used in the completed differential line, where the derivative is continuous as specified in R3.

The ring \(k[[u]]\) is free over \(k[[z]]\), with basis \(1,u,\ldots,u^{e-1}\). Multiplication on the corresponding fraction-field basis gives, for every integer \(m\),

\[
\operatorname{Tr}_{k((u))/k((z))}(u^m)
=\begin{cases}
e z^{m/e},&e\mid m,\\
0,&e\nmid m.
\end{cases}
\tag{R5.4}
\]

For a Laurent differential, the resulting trace formula is

\[
T\left(\sum_n a_nu^n\,du\right)
=\sum_{\ell}a_{e\ell+e-1}z^\ell\,dz.
\tag{R5.5}
\]

The series has a finite negative tail. Formula (R5.5) follows first for Laurent polynomials from (R5.3)–(R5.4), and for series by expressing them in the finite basis and using the \(z\)-adic continuous matrix trace. It proves both integrality and residue compatibility:

\[
T(k[[u]]\,du)\subset k[[z]]\,dz,
\qquad
\operatorname{Res}_z(T\omega)=\operatorname{Res}_u(\omega).
\tag{R5.6}
\]

The integral pairing

\[
k[[u]]\times k[[u]]\,du\longrightarrow k[[z]]\,dz,
\qquad (a,\omega)\longmapsto T(a\omega)
\tag{R5.7}
\]

is perfect. In the bases \(u^i\) and \(u^jdu\), for \(0\le i,j<e\), its coefficient matrix is

\[
T(u^{i+j}du)/dz
=\begin{cases}1,&i+j=e-1,\\0,&i+j\ne e-1.
\end{cases}
\tag{R5.8}
\]

Indeed, the trace exponent \(i+j-e+1\) lies strictly between \(-e\) and \(e\); the only possible multiple of \(e\) is zero. Thus the matrix is the invertible anti-diagonal identity matrix. On the product (R5.2) the pairing is the product of these perfect pairings, followed by addition.

Field trace commutes with this finite base change: it is the trace of a multiplication matrix in a finite basis, and matrix entries may be extended to \(k((z))\). The product splitting therefore implies the local global-form identity

\[
\operatorname{Res}_q(T_f\omega)
=\sum_{p\mid q}\operatorname{Res}_p(\omega).
\tag{R5.9}
\]

To descend the integral pairing before completion, note that \((f_*\Omega_X^1)_q\) is a finite torsion-free \(R\)-module, hence free. The target \(\operatorname{Hom}_R(C,\Omega^1_{\mathbf P^1,q})\) is free of the same rank. Choose an \(R\)-basis of the first module. The entries of its generic trace matrix lie in \(k[[z]]\) by (R5.5) on every completed factor. They lie in \(F\) as well; \(F\cap k[[z]]=R\), by the valuation criterion, so they already belong to \(R\). The completed matrix is invertible by (R5.8); its determinant has valuation zero, so it is a unit of \(R\). This proves, without an unproved descent assertion, the isomorphism

\[
f_*\Omega_X^1
\xrightarrow{\ \sim\ }
\mathcal H om_{\mathbf P^1}(f_*\mathcal O_X,\Omega^1_{\mathbf P^1}),
\qquad
\omega\longmapsto\bigl(a\mapsto T_f(a\omega)\bigr).
\tag{R5.10}
\]

It respects the finite-algebra action, where \((a\varphi)(b)=\varphi(ab)\). Evaluation at \(1\) in (R5.10) is exactly \(T_f\).

#### 1.1.11. The cohomology and duality used on the projective line

We give the affine prerequisite explicitly, since a planned affine-module lesson cannot serve as its proof. First, for any module \(N\), the rule \(D(g)\mapsto N_g\) is a sheaf on the principal-open basis. For a finite principal cover, an element zero in every localization is zero: appropriate powers of the cover elements annihilate it and still generate the unit ideal. Given compatible local fractions \(x_i\in N_{f_i}\), choose one \(N_0\) sufficiently large that \(f_i^{N_0}x_i\) belongs to \(N\) for every \(i\), and that \(f_i^{N_0}(x_i-x_j)=0\) in \(N_{f_j}\) for every pair. The latter is possible by compatibility on \(D(f_if_j)\). Choose \(a_i\) with \(\sum_i a_if_i^{N_0}=1\). Then \(\sum_i a_if_i^{N_0}x_i\in N\) restricts to \(x_j\) on every chart. The same proof applies after any localization. Every principal-open cover has a finite subcover, so it gives the full basis sheaf condition. Its associated sheaf \(\widetilde N\) therefore has sections \(N_g\) on \(D(g)\), including sections \(N\) on the whole affine.

Now let a quasi-coherent sheaf \(\mathcal F\) on \(\operatorname{Spec}R\) be associated to modules on a finite principal cover \(D(f_i)\), and put \(M_i=\Gamma(D(f_i),\mathcal F)\). On intersections its sections are the indicated localizations, by the preceding calculation. By the sheaf condition,

\[
M=\Gamma(\operatorname{Spec}R,\mathcal F)
=\ker\left(\prod_i M_i\longrightarrow\prod_{i,j} (M_i)_{f_j}\right).
\tag{R6.1}
\]

Localization is exact and commutes with these finite products. Localizing (R6.1) at \(f_j\), the resulting equalizer is the gluing equalizer for the cover of \(D(f_j)\) by \(D(f_if_j)\). Hence \(M_{f_j}\simeq M_j\), and \(\widetilde M\simeq\mathcal F\). Conversely the same localization-and-gluing calculation proves \(\Gamma(\operatorname{Spec}R,\widetilde M)=M\). This proves the affine module equivalence needed here and its exactness. Over a Noetherian ring, locally finite modules are globally finite: lift finitely many generators from each \(M_{f_i}\) to numerators in \(M\); their finite span has zero quotient after every localization, hence zero quotient. Kernels and cokernels of maps of finite modules remain finite.

For completeness, the positive Čech cohomology of \(\widetilde M\) on a finite principal cover is zero. For a cocycle, choose one common power \(f_i^N\) clearing its \(i\)-th denominators in all its finitely many components. Since the \(D(f_i)\) cover, the \(f_i^N\) generate the unit ideal; choose \(a_i\) with \(\sum_i a_if_i^N=1\). The contraction obtained by prepending \(i\), multiplying by \(a_if_i^N\), and summing over \(i\), is defined after denominator clearing. The alternating deletion identity gives \(\delta h(c)=c\) for the cocycle. Principal opens form a basis, and any cover of one has a finite principal refinement. The proved basis criterion of Čech cohomology, Theorem 4.1, therefore gives affine acyclicity. The proved acyclic-cover comparison of its Theorem 3.2 gives ordinary sheaf cohomology from any finite affine cover with affine intersections.

Use the ordered two-open cover of \(\mathbf P^1\) by \(U_0=\operatorname{Spec}k[t]\) and \(U_1=\operatorname{Spec}k[w]\), with \(w=t^{-1}\). It has affine overlap. In degree one,

\[
H^1(\mathbf P^1,\Omega^1)
=\frac{k[t,t^{-1}]\,dt}
{k[t]\,dt+k[t^{-1}]\,t^{-2}dt}
=k\,[t^{-1}dt].
\tag{R6.2}
\]

The local frames of \(\mathcal O(-2)\) map to \(dt\) on \(U_0\) and to \(-dw\) on \(U_1\); their transition is \(t^{-2}\). This specifies the isomorphism \(\mathcal O(-2)\simeq\Omega^1_{\mathbf P^1}\), including its scalar. With it, the coefficient trace of (R6.2) is the normalized projective-space trace of Ext sheaves and Serre duality on projective space, §3. The minus in the second frame is essential when differential residues are compared with that normalization.

For every integer \(d\), the Čech calculation gives

\[
H^1(\mathbf P^1,\mathcal O(d))
=\frac{k[t,t^{-1}]}{k[t]+t^d k[t^{-1}]},
\qquad
\operatorname{Hom}(\mathcal O(d),\Omega^1)
=H^0(\mathbf P^1,\mathcal O(-d-2)).
\tag{R6.3}
\]

When \(d\le-2\), representatives of the first space are \(t^{d+1},\ldots,t^{-1}\), and the second has polynomial basis \(1,t,\ldots,t^{-d-2}\). Multiplication followed by the coefficient of \(t^{-1}\) pairs these bases in reverse order. When \(d\ge-1\), both spaces are zero. Thus

\[
\operatorname{Hom}(\mathcal O(d),\Omega^1)
\xrightarrow{\ \sim\ }H^1(\mathbf P^1,\mathcal O(d))^\vee,
\qquad
u\longmapsto\operatorname{tr}_{\mathbf P^1}\circ H^1(u).
\tag{R6.4}
\]

The construction is compatible with all morphisms of sums of twists, since those maps act by multiplication with the same local polynomial entries on each side.

Every coherent \(\mathcal F\) on \(\mathbf P^1\) has a presentation by finite sums of twists. To prove this directly, take finite module generators on \(U_0\) and \(U_1\). A section \(m\) on \(U_0\), expressed on the overlap in the module on \(U_1\), extends as a section of \(\mathcal F(N)\) once multiplication by \(w^N\) clears its denominator; the coefficient on \(U_0\) is still \(m\). Similarly, a generator on \(U_1\) extends after clearing its \(t\)-denominator. A common \(N\) works for the finite list. These global sections generate on each chart, giving \(Q_0\twoheadrightarrow\mathcal F\), where \(Q_0\) is a finite sum of \(\mathcal O(-N)\). Its kernel is coherent by (R6.1) and the Noetherian module theorem. Repeat the construction for that kernel to obtain

\[
Q_1\longrightarrow Q_0\longrightarrow\mathcal F\longrightarrow0.
\tag{R6.5}
\]

Every quasi-coherent sheaf on this two-affine cover has zero cohomology in degree at least two. The two short exact sequences implicit in (R6.5) consequently give

\[
H^1(\mathcal F)=\operatorname{coker}(H^1(Q_1)\to H^1(Q_0)),
\qquad
\operatorname{Hom}(\mathcal F,\Omega^1)
=\ker(\operatorname{Hom}(Q_0,\Omega^1)\to\operatorname{Hom}(Q_1,\Omega^1)).
\tag{R6.6}
\]

Taking the dual of the cokernel and using (R6.4) proves, for every coherent \(\mathcal F\), the natural isomorphism

\[
\operatorname{Hom}_{\mathbf P^1}(\mathcal F,\Omega^1_{\mathbf P^1})
\simeq H^1(\mathbf P^1,\mathcal F)^\vee,
\qquad
u\longmapsto\operatorname{tr}_{\mathbf P^1}\circ H^1(u).
\tag{R6.7}
\]

This is a proof of the needed projective-line Hom duality; no splitting theorem for vector bundles is used.

#### 1.1.12. Identification with the constructed dualizing pair

For an \(R\)-algebra \(C\), an \(R\)-module \(N\), and a \(C\)-module \(M\), there is the elementary coinduction isomorphism

\[
\operatorname{Hom}_C(M,\operatorname{Hom}_R(C,N))
\simeq\operatorname{Hom}_R(M,N).
\tag{R7.1}
\]

It sends a map to its evaluation at \(1\); its inverse sends \(v\) to \(m\mapsto(a\mapsto v(am))\). These formulas are inverse and respect restriction, so they also give the sheaf statement for \(C=f_*\mathcal O_X\). The affine module comparison in R6 identifies modules over this finite algebra with sheaves on the affine inverse images. A morphism of such sheaves corresponds to a finite-algebra-linear map; the local comparisons glue.

For a coherent sheaf \(\mathcal F\) on \(X\), its direct image under \(f\) is coherent, by restriction of scalars for a finite algebra. The inverse images of \(U_0,U_1\) and of their overlap are affine. Their Čech section complexes are literally the section complexes for \(f_*\mathcal F\) on \(\mathbf P^1\). Thus

\[
H^1(X,\mathcal F)=H^1(\mathbf P^1,f_*\mathcal F).
\tag{R7.2}
\]

Combine (R5.10), (R7.1), (R6.7) and (R7.2). The result is

\[
\operatorname{Hom}_X(\mathcal F,\Omega_X^1)
\xrightarrow{\ \sim\ }H^1(X,\mathcal F)^\vee,
\qquad
u\longmapsto t_\Omega\circ H^1(u),
\tag{R7.3}
\]

where

\[
t_\Omega
=\operatorname{tr}_{\mathbf P^1}\circ H^1(T_f):
H^1(X,\Omega_X^1)\longrightarrow k.
\tag{R7.4}
\]

The formula for (R7.3) follows from evaluation at \(1\) in coinduction; it is not an independently chosen scalar multiple of the representing map.

Dualizing sheaves and Serre duality for projective schemes, Theorem 4.1, constructs a dualizing sheaf \(\omega_X^\circ\) with trace \(t_X^\circ\), by ambient sheaf Ext and the actual ambient duality proof. It proves the same natural representation

\[
\operatorname{Hom}_X(\mathcal F,\omega_X^\circ)
\simeq H^1(X,\mathcal F)^\vee.
\tag{R7.5}
\]

Its Proposition 1.1 is the Yoneda uniqueness proof for a representing pair: evaluate each representation on the other representing object, and naturality forces the two resulting maps to compose to the identities. Applying that proof to (R7.3) and (R7.5) gives the unique trace-preserving isomorphism

\[
\iota:\Omega_X^1\xrightarrow{\ \sim\ }\omega_X^\circ,
\qquad
t_X^\circ\circ H^1(\iota)=t_\Omega.
\tag{R7.6}
\]

This proves the required identification with the already constructed dualizing pair. It does not assume the unproved smooth identification recorded at the end of Dualizing sheaves and Serre duality for projective schemes. The normalization is fixed by the representing trace, so there is no unspecified nonzero scalar in (R7.6).

One can also see directly that the trace space is one-dimensional. A global function \(h\) on \(X\) acts on the finite locally free algebra \(f_*\mathcal O_X\). The coefficients of its characteristic polynomial glue to global functions on \(\mathbf P^1\), hence belong to \(k\), by the two-chart calculation \(k[t]\cap k[t^{-1}]=k\). The characteristic polynomial annihilates \(h\); as \(k\) is algebraically closed and \(K\) is a field, \(h\in k\). Thus \(H^0(X,\mathcal O_X)=k\). Applying (R7.3) to \(\mathcal F=\Omega_X^1\) gives \(H^1(X,\Omega_X^1)^\vee=k\), so \(t_\Omega\) is an isomorphism onto \(k\).

#### 1.1.13. Global residues and the connecting-map sign

Let \(\Omega_K\) be the sheaf with value \(\Omega^1_{K/k}\) on every nonempty open of \(X\), and zero on the empty open. Its restrictions between nonempty opens are identities, so it is flasque. Let

\[
\operatorname{PP}(\Omega_X)
=\bigoplus_{p\in X(k)}i_{p*}\operatorname{PP}_p(\Omega_X).
\tag{R8.1}
\]

Sections on an open are finite-support tuples. Indeed, a locally finite support on a Noetherian quasi-compact open is finite. This sheaf is flasque: a finite tuple extends to a larger open by zero at the new points. A rational differential has only finitely many poles, and the map taking its local polar parts fits into the exact sequence

\[
0\longrightarrow\Omega_X^1\longrightarrow\Omega_K
\longrightarrow\operatorname{PP}(\Omega_X)\longrightarrow0.
\tag{R8.2}
\]

Exactness is checked on stalks using (R3.4). The preceding sheaf cohomology foundations, proved in [Cohomology of sheaves on ringed spaces](../../AG-QC/src/cohomology-of-sheaves-on-ringed-spaces.md), imply

\[
H^1(X,\Omega_X^1)
=\operatorname{coker}\left(
\Omega^1_{K/k}\longrightarrow
\bigoplus_{p\in X(k)}\operatorname{PP}_p(\Omega_X)
\right).
\tag{R8.3}
\]

In particular the connecting map \(\partial\) is surjective. Choosing local rational lifts \(\alpha_i\) of a principal-part tuple, its class is represented by \(\alpha_j-\alpha_i\), with the convention (R0).

First prove the global residue theorem on \(\mathbf P^1\). Partial fractions write a rational differential as a polynomial times \(dt\), plus terms \(c_{a,n}(t-a)^{-n}dt\). Polynomial terms have residue zero at infinity. For \(n=1\), substitution \(t=w^{-1}\) shows residue \(-c_{a,1}\) at infinity; for \(n\ge2\), the form is regular at infinity or has no \(w^{-1}dw\) coefficient. Its only finite residue is \(c_{a,1}\) when \(n=1\). Therefore

\[
\sum_{q\in\mathbf P^1(k)}\operatorname{Res}_q(\eta)=0
\quad\text{for every rational differential }\eta.
\tag{R8.4}
\]

Apply (R8.4) to \(T_f\omega\), and then use (R5.9). This proves the algebraic global residue theorem on \(X\):

\[
\sum_{p\in X(k)}\operatorname{Res}_p(\omega)=0
\quad\text{for every }\omega\in\Omega^1_{K/k}.
\tag{R8.5}
\]

We next determine the trace of a connecting class on the projective line, rather than inferring it from a local coefficient rule. A principal part supported at infinity is a finite sum

\[
\beta_\infty=\sum_{m\ge1}c_m w^{-m}dw.
\tag{R8.6}
\]

Lift it by zero on \(U_0\) and by \(-\sum_m c_m t^{m-2}dt\) on \(U_1\). The latter rational form is regular at every finite point of \(U_1\), so it has exactly the prescribed principal parts there. Its Čech boundary is the latter form minus zero. By (R6.2),

\[
\operatorname{tr}_{\mathbf P^1}(\partial\beta_\infty)
=-c_1=-\operatorname{Res}_\infty(\beta_\infty).
\tag{R8.7}
\]

For a tuple supported at a finite point \(a\), choose the rational differential

\[
\eta_a=\sum_{n\ge1}c_n(t-a)^{-n}dt
\tag{R8.8}
\]

having that polar part at \(a\). It has no other finite poles. Its full principal-part tuple \(\beta_a+\gamma_\infty\) is the image of a global rational differential, and hence has zero connecting class. Equations (R8.4) and (R8.7) give

\[
\operatorname{tr}_{\mathbf P^1}(\partial\beta_a)
=-\operatorname{tr}_{\mathbf P^1}(\partial\gamma_\infty)
=\operatorname{Res}_\infty(\eta_a)
=-\operatorname{Res}_a(\beta_a).
\tag{R8.9}
\]

By additivity, (R8.7)–(R8.9) prove the projective-line version of the first formula in (R2) for every tuple.

Finally, the differential trace gives a morphism from (R8.2), after finite direct image, to the analogous projective-line sequence. This direct-image sequence is exact: on the inverse image of an affine base chart, \(\Omega_X^1\) has zero \(H^1\) by R6, so (R8.2) is onto on principal-part sections there. Its maps on the regular and rational terms were constructed in R5; on principal parts it is their induced quotient map. On completion at \(q\), this quotient map is the sum of the branch trace maps in (R5.5). Integrality ensures that regular representatives map to regular representatives. The connecting maps therefore commute, and (R5.9) gives

\[
\begin{aligned}
t_\Omega(\partial\beta)
&=\operatorname{tr}_{\mathbf P^1}(\partial(T_{\operatorname{PP}}\beta))\\
&=-\sum_q\operatorname{Res}_q(T_{\operatorname{PP}}\beta)\\
&=-\sum_p\operatorname{Res}_p(\beta_p).
\end{aligned}
\tag{R8.10}
\]

This is the global trace formula for the constructed dualizing pair under (R7.6). The principal-part boundary is onto by (R8.3), so (R8.10) determines the trace on all of \(H^1\), and shows that it is independent of the auxiliary finite projection. The residue theorem (R8.5) proves directly that the functional descends through the quotient in (R8.3).

#### 1.1.14. The Atiyah class has trace equal to degree

Let \(L\) be a line bundle. The first-principal-parts sequence

\[
0\longrightarrow\Omega_X^1\otimes L
\longrightarrow\mathcal P^1(L)\longrightarrow L\longrightarrow0
\tag{R9.1}
\]

has, in a frame \(e_i\), the \(\mathcal O_X\)-linear splitting \(s_i(ae_i)=a\,j(e_i)\). The universal first-jet map satisfies \(j(ae_i)=a\,j(e_i)+da\otimes e_i\). With \(e_j=e_i g_{ij}\), it follows that

\[
s_j(e_i)-s_i(e_i)
=g_{ij}^{-1}j(e_j)-j(e_i)
=d\log g_{ij}\otimes e_i.
\tag{R9.2}
\]

Thus the extension class, with (R0), is precisely \(\operatorname{at}(L)=[d\log g_{ij}]\in H^1(X,\Omega_X^1)\). Equivalently, (R9.1) can be constructed directly by gluing the local modules \((\Omega_X^1\otimes L)\oplus L\) with off-diagonal entry \(d\log g_{ij}\); the cocycle equation follows from \(d\log(gh)=d\log g+d\log h\). This construction also proves the stated sign without any convention for an unnamed jet extension.

Choose a nonzero rational section \(\sigma\) of \(L\), and write \(\sigma=f_i e_i\). On an overlap,

\[
f_j=f_i/g_{ij},
\qquad
\alpha_i=d\log f_i,
\qquad
\alpha_j-\alpha_i=-d\log g_{ij}.
\tag{R9.3}
\]

The principal parts of the \(\alpha_i\) form a global tuple \(q\), since their differences are regular. At a closed point write \(f_i=u^{m_p}v\), where \(v\) is a unit of the DVR. Then

\[
d\log f_i=m_p\,\frac{du}{u}+\frac{dv}{v},
\qquad
\operatorname{Res}_p(q_p)=m_p=\operatorname{ord}_p(\sigma).
\tag{R9.4}
\]

The second term is regular. Equations (R9.3) and the definition of \(\partial\) give

\[
\operatorname{at}(L)=-\partial q.
\tag{R9.5}
\]

The divisor of the rational section has finite support. Define its degree as \(\sum_p m_p\); all residue-field degrees equal one here. Changing the rational section multiplies it by a rational function \(h\). Its degree changes by \(\sum_p\operatorname{ord}_p(h)\), which is zero: apply (R8.5) to \(d\log h\), whose residue is \(\operatorname{ord}_p(h)\). Thus this is the well-defined degree of \(L\). Combining (R9.5) with (R8.10) proves

\[
\boxed{\operatorname{tr}_X(\operatorname{at}(L))=\sum_p\operatorname{ord}_p(\sigma)=\deg L.}
\tag{R9.6}
\]

For an explicit sign test, on \(\mathbf P^1\) the line \(\mathcal O_{\mathbf P^1}([0])\) associated to the point \(t=0\) has frames \(e_0=t^{-1}\), \(e_1=1\), hence \(g_{01}=t\). Its Atiyah class is \([t^{-1}dt]\), of trace \(+1\). A principal part \(t^{-1}dt\) supported at zero has connecting trace \(-1\). These are compatible because the rational-section computation uses the extra minus sign in (R9.5).

#### 1.1.15. Foundations of the differential trace

The trace-preserving identification \(\omega_X^\circ\simeq\Omega_X^1\), its global principal-part residue formula and (R9.6) follow from the arguments above. They use the representing-pair theorem Dualizing sheaves and Serre duality for projective schemes, Theorem 4.1, and its uniqueness. The differential identification and its trace compatibility are supplied by §§1.1.8–1.1.14.

Using the derived Picard and obstruction descent arguments in §§1.1.1–1.1.6, together with the fixed-curve base change proved in §1.1.16, this proves that the traced obstruction on a degree component is the actual constant map \(d\). Namely it is a regular function on the classical smooth rigidified Picard scheme \(P^d\). Its value at every closed point is \(d\) by (R9.6). The scheme is reduced, locally of finite type over the algebraically closed field; on every affine open the strong Nullstellensatz of [The Nullstellensatz and Jacobson rings](../../AG-CA/src/the-nullstellensatz-and-jacobson-rings.md) implies that a regular function vanishing at all closed points is zero. Hence the function is identically \(d\). Pulling this equality back gives the equality for every derived parameter algebra, including its coherent homotopies, using the actual descent to \(P^d\) proved in F3–F4. Pointwise values on a nonreduced or derived parameter space alone would not justify this conclusion.

This last application uses the separate Picard/derived-descent arguments; it is not a proof of those arguments. No universal-vector-extension class, coherent Fourier–Mukai kernel identity, presentable Fourier equivalence, or Beilinson–Drinfeld factorization theorem is claimed here. Those wider foundations retain their own exact proof obligations. No characteristic-positive, singular-curve, non-algebraically-closed, or higher-dimensional extension is asserted.

#### 1.1.16. Fixed-curve duality and trace on every parameter

The following proof applies to every ordinary \(k\)-algebra and every connective commutative DG \(k\)-algebra \(A\), including those with unbounded negative cohomology and without Noetherian or finite-type hypotheses. Higher module/line/crystal descent is the separate F0–F7 input; the calculation here gives its actual fixed coefficients and trace.

##### 1.1.16.1. Two-affine section complexes and arbitrary tensors

Fix the finite projection in R4, and write
\[
U_0=\operatorname{Spec}k[t],\quad
U_1=\operatorname{Spec}k[t^{-1}],\quad
V_i=f^{-1}U_i,\quad V_{01}=V_0\cap V_1.
\]
All three \(V\)'s are affine, since \(f\) is finite. For a fixed quasi-coherent \(\mathcal E\) on \(X\), define
\[
C_X(\mathcal E)=
\left[\Gamma(V_0,\mathcal E)\oplus\Gamma(V_1,\mathcal E)
\xrightarrow{\ \delta\ }\Gamma(V_{01},\mathcal E)\right],
\qquad \delta(a_0,a_1)=a_1-a_0,
\tag{B1}
\]
in Čech degrees \(0,1\).

The affine-module calculation R6 is valid for arbitrary modules; its Noetherian hypothesis was needed only for finite-generation assertions. Hence on each derived base-changed affine the section module of the fixed pullback is the original section module tensored with \(A\). The augmented sheaf Čech resolution is exact on stalks: at a point choose a cover member containing it and use its extra-vertex contraction. The affine restrictions are exact module evaluation. The separate derived module-descent construction of F0 identifies these affine complexes and their actual mapping-space compatibilities. The ordered two-member complex, by the actual Čech cohomology contraction, has only the two degrees in (B1).

Every acyclic complex over the field \(k\) is contractible, by splitting its cycles and boundaries. Tensoring its contraction with any complex gives a contraction with the usual tensor signs. Thus every \(k\)-complex is K-flat. Tensoring the stalkwise augmented Čech contraction with \(A\) preserves it. Each total degree has only two Čech contributions; it uses no infinite product of Čech terms. Consequently there is a natural quasi-isomorphism
\[
R\Gamma(X_A,\mathcal E_A)
\simeq C_X(\mathcal E)\otimes_k A
\simeq R\Gamma(X,\mathcal E)\otimes_k^L A.
\tag{B2}
\]
Here \(X_A=X\times\operatorname{Spec}A\) and \(\mathcal E_A\) is the fixed derived pullback. For a map \(A\to A'\), both base-change comparisons are the literal associative tensor comparison with \(A'\). They act on full DG mapping spaces, and compose with the tensor/bar coherences already used in F0. This is the required fixed-curve statement; it does not claim a cohomology/base-change theorem for arbitrary varying coherent sheaves.

##### 1.1.16.2. An actual trace chain map

The sheaf trace \(T_f:f_*\Omega_X^1\to\Omega_{\mathbf P^1}^1\) gives a map of the two Čech complexes, because it respects restriction. Define
\[
\lambda:k[t,t^{-1}]\,dt\longrightarrow k,\qquad
\lambda\left(\sum_j c_jt^jdt\right)=c_{-1}.
\]
Define a chain map from \(C_{\mathbf P^1}(\Omega^1)\) to \(k[-1]\) by zero in Čech degree zero and \(\lambda\) in degree one. It is a chain map: the \(U_0\)-forms contain only powers \(t^jdt\) with \(j\ge0\), while \(U_1\)-forms contain only powers with \(j\le-2\), so \(\lambda\delta=0\). Composing with \(C(T_f)\) gives
\[
\mathsf{Tr}_X:C_X(\Omega_X^1)\longrightarrow k[-1].
\tag{B3}
\]
Its \(H^1\)-map is exactly R7.4. This is an actual chain morphism, not a functional specified only on individual cohomology classes.

Tensoring (B3) gives
\[
\mathsf{Tr}_{X,A}:
C_X(\Omega_X^1)\otimes_k A\longrightarrow A[-1],
\quad\text{or}\quad
R\Gamma(X_A,\Omega_{X_A/A}^1)[1]\longrightarrow A.
\tag{B4}
\]
The map in degree one is the fixed coefficient map \(T_f\) followed by \(\lambda\), tensored with the identity of \(A\). It commutes with the internal DG differential and with any parameter map, including all its higher homotopies through the derived tensor functor. No series completion is involved.

The residue calculation proves independence of \(f\) on the trace functional. It also gives the needed field-level chain independence: for the bounded complex \(R\Gamma(X,\Omega_X^1)\) in degrees \(0,1\),
\(\operatorname{RHom}_k(R\Gamma\Omega,k[-1])\)
has no negative cohomology. Thus its degree-zero mapping space is discrete and determined by the map on \(H^1\). Comparison on a common refinement identifies all trace constructions in that discrete space, with contractible comparison homotopies. Tensoring these fixed comparisons transports their coherence to all parameters. One must not instead infer uniqueness of a derived trace from ordinary point values over an arbitrary \(A\).

##### 1.1.16.3. The finite-flat pairing commutes with every base change

On either polynomial base chart, let \(R\) be its coordinate ring, \(B\) the finite free algebra of the inverse image, and \(N=\Omega_{\mathbf P^1}^1(U)\). R5.10 is the actual \(B\)-linear isomorphism
\[
M=\Omega_X^1(f^{-1}U)
\xrightarrow{\sim}\operatorname{Hom}_R(B,N).
\tag{B5}
\]
Because \(B\) is finite projective, its Hom is \(B^\vee\otimes_RN\). For \(R_A=R\otimes_k A\), therefore,
\[
\operatorname{RHom}_{R_A}(B\otimes_k A,N\otimes_k A)
\simeq\operatorname{Hom}_R(B,N)\otimes_k A.
\tag{B6}
\]
One can check (B6) in a finite basis, or with a finite projective summand of a free module; no flatness of a general parameter change \(A\to A'\) is required. The pairing matrix, its inverse and evaluation at \(1\) base change as actual matrices. Finite-algebra multiplication traces are traces of these same finite multiplication matrices. Hence the differential trace, coinduction action and every restriction map commute with arbitrary ordinary or DG base change. The trace-preserving isomorphism \(\iota:\Omega_X^1\to\omega_X^\circ\) likewise gives its actual fixed pullback \(\iota_A\).

The completed-DVR calculation is used to prove (B5) over the original field and curve. It need not be repeated after scalar extension. In particular no equality \(k[[u]]\otimes_k A=A[[u]]\), and no commutation of tensor with an infinite inverse limit, is asserted or required. Fixed finite polar-part coefficient maps and the descended finite matrices are the base-changing objects.

##### 1.1.16.4. Global residue maps, perfectness, and the application boundary

The two-term flasque principal-part resolution in R8 also consists of fixed sheaves on the original space X. In the following tensor calculation these are sheaves of parameter-valued coefficients on that fixed space; they are not being asserted to be flasque on every open of the total space X_A. Equation (B2), using the actual affine pullbacks and their descent, compares their resulting fixed cohomology maps with derived global sections on X_A. Tensoring it over \(k\) with \(A\) preserves exactness degreewise and all connecting maps. On every nonempty open, the rational-differential sheaf has its fixed rational vector space of sections; the principal-part sheaf has the direct sum of its stalk vector spaces over the closed points in that open. Noetherian opens are quasi-compact, so the finite-support description persists on them after tensoring. These restriction maps are surjective vector-space maps and remain surjective after tensoring. Thus the tensor resolution remains termwise flasque, its section complexes are the original complexes tensored with \(A\), and its two-term totalization has no unbounded product issue. Residue is a fixed coefficient functional on each finite polar part. Thus the actual equality of morphisms induced by R8.10 base changes to (B4), compatibly with the principal-part connecting map.

These are the base changes of the **fixed** rational and polar-part sheaves. They are sufficient for the residue/trace map used in the Atiyah obstruction. They are not an assertion that all rational functions on a nonreduced total family have a field of fractions, nor that every relative rational section over \(A\) has the classical divisor description.

For clarity, this also supplies the perfect complex duality actually needed for the fixed cohomology target. R6's presentations give finite \(H^1\) for every coherent sheaf on \(\mathbf P^1\). Its short exact presentation and finite \(H^1\) of the coherent kernel then give finite \(H^0\). Finite direct image transfers this to \(\mathcal O_X\) and \(\Omega_X^1\). Their Čech complexes are bounded with finite cohomology, hence perfect over \(k\): splitting cycles and boundaries replaces each by its finite-dimensional cohomology complex.

Use the ordered Alexander–Whitney cup with the differential factor first:
\[
C_X(\Omega_X^1)[1]\otimes_k C_X(\mathcal O_X)
\longrightarrow C_X(\Omega_X^1)[1]
\xrightarrow{\mathsf{Tr}_X[1]}k.
\tag{B7}
\]
On Čech degrees \(0,1\), it is componentwise multiplication in degree zero, \(a_0b_{01}\) for degrees \(0,1\), and \(a_{01}b_1\) for degrees \(1,0\); the \(1,1\) term is zero. The identity
\[
a_1b_1-a_0b_0=(a_1-a_0)b_1+a_0(b_1-b_0)
\]
is the chain Leibniz rule. The conventional tensor/shift signs handle internal DG degrees. Putting the shifted differential factor first avoids introducing an unstated sign by commuting it past the first factor.

R7.3 applied to \(\mathcal F=\mathcal O_X\) and to \(\mathcal F=\Omega_X^1\) proves perfectness on the two cohomology pairs of (B7). Indeed the first pairs global differentials with \(H^1(\mathcal O_X)\), and the second pairs \(H^1(\Omega_X^1)\) with global functions through its trace. There are no other degrees. Adjunction therefore gives a quasi-isomorphism
\[
C_X(\Omega_X^1)[1]
\xrightarrow{\sim}\operatorname{RHom}_k(C_X(\mathcal O_X),k).
\tag{B8}
\]
Tensor with any \(A\) preserves it. The finite perfect model for \(C_X(\mathcal O_X)\) identifies the right side after base change with
\(\operatorname{RHom}_A(C_X(\mathcal O_X)\otimes_k A,A)\).
This proves the fixed complex duality and trace compatibility on all such parameters, rather than merely fibrewise nondegeneracy.

Finally, a variable line \(L\) on \(X_A\) has the actual coherent Atiyah map from the separate F4 principal-parts triangle. Its target is the fixed complex in (B4), because tensoring with \(L^{-1}\) identifies its endomorphism coefficients with \(\Omega_{X_A/A}^1\). F0–F7 supply the Picard comparison, base-line invariance, refinements, paths and higher descent. Composing that supplied map with (B4) is therefore the full coherent traced obstruction. The ordinary R9 calculation gives its values, but the reduction to the actual regular function on the smooth rigidified \(P^d\) still uses F3–F4. Once that factorization is supplied, the strong Nullstellensatz identifies that function with \(d\), and pulling the equality back gives the result for every parameter. B1–B8 do not replace that factorization by a pointwise argument.

The representing-pair theorem used in R7 retains its ambient Ext, local algebra and injective/derived-category prerequisites. The smooth local theorem used in R3 retains its standard-smooth, conormal, regular-parameter and dimension prerequisites. The ordinary Picard and full descent constructions in §§1.1.1–1.1.6 retain their own exact recursive proof obligations. The arguments here supply the differential identification, global residue signs and fixed-curve base change within those foundations; those ambient Ext, local-algebra and Picard-descent foundations remain explicit inputs.

For the trace normalization, a freely readable human comparison is Ravi Vakil's [*The Rising Sea*, public draft of 27 July 2024, §§29.1.3–29.1.11](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf). The finite projection, finite trace pairing, projective-line duality, global connecting-map calculation and degree argument are proved above.

### 1.2. Tangent and Koszul checks

Nevertheless its tangent check explains all three factors. At a flat line \(E\), its adjoint connection is the trivial one, and the derived deformation complex is
\[
T_E\operatorname{LocSys}_{\mathbb G_m}(X)
   =R\Gamma_{\mathrm{dR}}(X,k)[1].
                                                               \tag{1.5}
\]
Thus its cohomology in degrees \(-1,0,1\) has dimensions \(1,2g,1\). In (1.4), \(B\mathbb G_m\) contributes the scalar automorphisms in degree \(-1\), \(J^\natural\) contributes the \(2g\) ordinary deformation dimensions, and \(Z_{\mathrm{der}}\) contributes degree \(1\). Indeed its cotangent complex at its augmentation is \(k[1]\), so its tangent is \(k[-1]\). A pointwise description sees the automorphism group and \(J^\natural(k)\), but not this last obstruction direction.

For (1.3) the algebra computation is direct. Resolve \(k\) over \(k[t]\) by the Koszul DG algebra \(k[t][\eta]\), with \(|\eta|=-1\), \(d\eta=t\). Tensor with \(k\) at \(t=0\). This gives \(B\) and proves the derived fibre-product formula. The ordinary fibre product is just a point and has no \(\epsilon\).

## 2. Bundle degrees are spectral weights

**Proposition 2.1.** There is an equivalence
\[
\operatorname{Dmod}(\underline{\mathbb Z})
 \simeq \operatorname{QCoh}(B\mathbb G_m).
                                                               \tag{2.1}
\]
In the downward Hecke normalization used below, the component \(d\) is assigned spectral weight \(d\). Both sides allow every integer, with no finite-support requirement on a general object.

**Proof.** A D-module on a disjoint union of points is a family of complexes \(M_d\), with componentwise morphisms. Thus its category is \(\prod_{d\in\mathbb Z}\operatorname{Vect}_k\).

On the other side, quasicoherent descent from \(\operatorname{Spec}k\to B\mathbb G_m\) gives a comodule for \(k[z,z^{-1}]\). Such a comodule is exactly a graded vector space. For a vector \(v\), its coaction is a finite sum \(\sum_n v_n\otimes z^n\); coassociativity makes the \(v_n\) its weight components and the counit gives \(v=\sum_n v_n\). Hence
\[
M=\bigoplus_{n\in\mathbb Z}M_n,\qquad
\rho(v_n)=v_n\otimes z^n.
\]
Conversely these formulas define a comodule for any family of weight spaces. Equivariant maps preserve weights. Applied degreewise to complexes, the argument gives the derived equivalence: differentials preserve weights and exactness is tested weightwise.

The direct sum in the underlying representation does not impose finite weight support on the object. It only says that each individual vector has finitely many components. Thus families \((M_n)\) with infinitely many nonzero weights are allowed, and the category is the same product of vector-space categories as on the automorphic side. Sending \(M_d\) to weight \(d\) proves (2.1). \(\square\)

An object is compact precisely when it has finitely many weights, each a perfect complex of \(k\)-vector spaces. Finite such objects are compact by the mapping formula. Conversely, write any family as the filtered union of its finite-weight parts. Compactness makes its identity factor through one such part; the other components must vanish. Testing a single weight then proves perfectness there. This is the same finite-degree compactness argument as in [Sheaves and D-modules on Bun_G](sheaves-and-d-modules-on-bun-g.md).

Tensoring a spectral representation with the weight-\(m\) line shifts its components by
\[
(N\otimes k(m))_d=N_{d-m}.
                                                               \tag{2.2}
\]
At \(x_0\), the downward degree operator also takes its input from \(d-m\). This checks the degree/weight sign for the final normalized correspondence.

## 3. The stabilizer gives the derived factor

**Proposition 3.1 (conditional on the categorical descent and base-change foundations).** In the normalized-fibre convention there is an equivalence
\[
\operatorname{Dmod}(B\mathbb G_m)
  \simeq\operatorname{Mod}_B
  =\operatorname{QCoh}(Z_{\mathrm{der}}).
                                                               \tag{3.1}
\]
The ordinary constant local system corresponds to the augmentation module \(k=B/(\epsilon)\); the normalized compact-support atlas generator corresponds to the free module \(B\).

**Proof.** Let \(p:\operatorname{Spec}k\to B\mathbb G_m\) be the atlas. Let \(F\) take its ordinary local-system fibre, so \(F=p^![-2]\) in the complex right-crystal realization. Smooth descent makes \(F\) conservative, and exceptional pullback with its fixed shift preserves colimits. Its left adjoint \(L\) is the corresponding shifted compact-support atlas pushforward.

The self-fibre product of the atlas is \(\mathbb G_m\). Exceptional base change identifies the monad \(FL\) with tensoring by its de Rham homology, with multiplication induced by group multiplication. Its algebra is calculated from
\[
k[t,t^{-1}]\xrightarrow{d}
 k[t,t^{-1}]\,d\log t .
\]
Every nonzero Laurent mode is exact, since its integer exponent is invertible in \(k\). Thus the complex has the Hopf model \(k\oplus k\,d\log t\), with the latter in cohomological degree \(1\). The identity
\[
\operatorname{mult}^*(d\log t)=d\log t_1+d\log t_2
\]
gives the primitive coproduct. Its homological dual is \(B\), with the degree-\(-1\) primitive \(\epsilon\); its Pontryagin square vanishes. Therefore \(FL=B\otimes-\), as a monad, not merely as a complex.

The adjunction bar construction proves monadicity explicitly. For a \(B\)-module, realize its standard simplicial free-module resolution using \(L\). Applying \(F\) recovers that resolution and its realization, hence the module. For an object of \(\operatorname{Dmod}(B\mathbb G_m)\), the corresponding adjunction bar realization maps to the object. \(F\) makes this an equivalence, and conservativity makes it an equivalence before applying \(F\). This also identifies morphisms and proves (3.1).

The constant local system has trivial homological action, giving the augmentation. For \(Q=L(k)\), \(\operatorname{RHom}(Q,M)=F(M)\), so \(Q\) is compact and generates by conservativity. It corresponds to the free module \(B\). \(\square\)

The generator is explicitly normalized. In the complex convention \(L(k)=p_!k[2]\). The unshifted \(p_!k\) is still a compact generator but differs by that shift. This keeps the atlas shifts visible when comparing the terse generator statement in AG §11.2 with our ordinary-fibre convention.

**Proposition 3.2.** The augmentation \(k\) is coherent but not perfect, and
\[
\operatorname{Ext}_B^*(k,k)=k[u],\qquad |u|=2.
                                                               \tag{3.2}
\]

**Proof.** Consider the semifree resolution
\[
P=\bigoplus_{j\ge0}Be_j,\quad |e_j|=-2j,\quad
de_0=0,\quad de_j=\epsilon e_{j-1}\ (j\ge1).
                                                               \tag{3.3}
\]
The differential has degree \(+1\). Its only cohomology is \(ke_0\): every \(\epsilon e_j\) is the boundary of \(e_{j+1}\), whereas each \(e_j\), \(j>0\), has nonzero differential. Thus \(P\to k\) is a resolution. Applying \(\operatorname{Hom}_B(-,k)\) gives a copy of \(k\) in every nonnegative even degree and zero differential. The degree-two chain map \(e_j\mapsto e_{j-1}\), with \(e_0\mapsto0\), has nonzero iterates in every even degree and supplies the Yoneda products, proving (3.2).

The module \(k\) has bounded finite-dimensional cohomology, so it is coherent. A perfect \(B\)-module is a retract of a finite cell module; its derived Hom to \(k\) is bounded, by induction on finite cells and passage to retracts. Equation (3.2) is unbounded, so \(k\) is not perfect. \(\square\)

This is a **derived** thickening of a point: \(H^0(B)=k\) is reduced, while \(H^{-1}(B)\ne0\). Calling it an ordinary nonreduced point would miss the grading. The support of both \(B\) and \(k\) is the same classical point; their perfectness differs.

## 4. The abelian Fourier kernels and their normalization

We now calculate the two composition kernels on all quasicoherent complexes. The calculation is conditional on the explicit geometric Lemma G and exact earlier foundations below. In this section \(Y=A^\natural\) denotes the classical smooth moduli of rigidified flat lines on the abelian variety \(A\); the letter \(B\) continues to denote the exterior DG algebra of §1.

All constructions are over an algebraically closed field of characteristic zero. They are algebraic: the proof does not use Riemann–Hilbert, analytic character varieties, or comparison with a topological torus. Complexes use cohomological indexing. Write
\[
\operatorname{DR}^{0}_{Y/S}(M)
 =[M\longrightarrow\Omega^1_{Y/S}\otimes M\longrightarrow\cdots
       \longrightarrow\Omega^r_{Y/S}\otimes M]
\]
in degrees \(0,\ldots,r\), with its connection differential. When \(M\) is a complex, tensor products and totalizations are derived.

### 4.1. The geometric datum required by the Fourier calculation

**Lemma G (geometric statement with explicit recursive foundations).** Let \(A\) be an abelian variety of dimension \(g\). Its rigidified degree-zero Picard functor is represented by a smooth projective abelian variety \(\widehat A\) of dimension \(g\). There is a normalized Poincaré line \(P\) on \(A\times\widehat A\), and evaluation gives biduality
\[
A\xrightarrow{\sim}\operatorname{Pic}^0(\widehat A).
\tag{G.1}
\]
Put \(V=H^0(A,\Omega_A^1)\). Rigidified degree-zero lines on \(A\) with integrable connection are represented by a smooth algebraic group \(Y=A^\natural\), an affine \(V_{\mathrm{add}}\)-torsor over \(\widehat A\):
\[
0\longrightarrow V_{\mathrm{add}}\longrightarrow Y
   \xrightarrow{\pi}\widehat A\longrightarrow0.
\tag{G.2}
\]
The underlying line of its universal relative connection \(\mathcal P\) is
\((1_A\times\pi)^*P\). We define its class by the degree-one affine-function extension for the positive action \(\nabla\mapsto\nabla+\omega\). That class in
\(H^1(\widehat A,\mathcal O_{\widehat A})\otimes V\), identified using
the differential of evaluation with \(V^*\otimes V\), is the identity. Ordered differences of local connection sections have the negative class, as proved in (G5.1)–(G5.3).
The line and connection are multiplicative in both group variables, with the rigidified unit, associativity, and symmetry identifications.

Sections 4.2.1–4.2.9 prove the represented dual, its dimension, normalized family line, actual universal connection and affine-function identity class, relative to the earlier foundations recorded there. Sections 4.2.12–4.2.20 prove general biduality (G.1) over every characteristic-zero field: character descent identifies the whole Picard kernel on every ordinary parameter scheme, multiplication ranks put every character line in the identity component, and equality of dual-isogeny degrees forces evaluation to have degree one. Sections 4.2.22–4.2.29 prove the effective theta divisor, ampleness and conventional sign. Their recursive foundations remain the obligations in §§4.2.10 and 4.2.21. The first-order tangent identification
\[
T_0Y=H^1_{\mathrm{dR}}(A)
\tag{G.3}
\]
is proved directly in F.3 from the moduli interpretation; it need not be imported separately.

The sign convention is that \(\mathcal P|_{A\times\{e\}}\) is the actual connection represented by \(e\), rather than its dual. Thus the two positive kernels have inversion in their composite. Every occurrence of \(Y\) below denotes this classical smooth moduli scheme; it does not denote the unrigidified derived local-system stack on a curve.

### 4.2. The exact earlier foundations used

The argument uses the following earlier mathematical results at the stated hypotheses.

* [Cohomology of affine schemes and Serre's criterion](../../AG-QC/src/affine-cohomology-and-serres-criterion.md): affine acyclicity and finite affine-cover computations of quasicoherent cohomology. Its use here is only on separated finite-type schemes.
* [Euler characteristics and Hilbert polynomials](../../AG-QC/src/euler-characteristics-and-hilbert-polynomials.md), Theorems 3.1 and 4.2: a nonzero coherent sheaf has a nonzero ample Hilbert polynomial, and the fibre Hilbert polynomial in a flat projective family is locally constant.
* [Base change and the Grothendieck complex](../../AG-QC/src/base-change-and-the-grothendieck-complex.md), Lemma 3.1 and Theorem 3.2: a proper family with a flat coherent sheaf has a finite projective complex computing every derived base change. Its proof constructs the model from a bounded flat Čech complex and finite cohomology.
* [The theorem on formal functions](../../AG-QC/src/the-theorem-on-formal-functions.md), Theorem 5.1: coherent cohomology on a projective \(g\)-dimensional scheme vanishes in degrees above \(g\). The use is over a field, with a coherent sheaf; it does not ask for an unproved dimension bound for arbitrary complexes.
* Dualizing sheaves and Serre duality for projective schemes, Theorem 4.2: projective Cohen–Macaulay Serre duality. For a smooth variety the regular-immersion Koszul construction identifies its dualizing sheaf with its top differential forms; consequently its trace is a trace on \(H^g(\Omega_A^g)\).
* [Direct images and the relative de Rham complex](../../GL-DMOD/src/direct-images-and-the-relative-de-rham-complex.md), Theorem 2.1 and Proposition 3.1: the relative Spencer complex and the normal-derivative description of a closed-embedding direct image. Its relative direct-image convention is \(Rp_*\operatorname{DR}^0[g]\); we retain the unshifted \(\operatorname{DR}^0\) explicitly here.
* [Regular local rings](../../AG-CA/src/regular-local-rings.md), Theorem 2.2 and the regular-parameter Koszul calculation: finite free resolutions over smooth local rings. We also give the particular completion and Koszul argument needed below, rather than invoking a formal inverse-function theorem for complexes.
* [Completion](../../AG-CA/src/completion.md), Theorems 3.1–3.3: completion of a finite module over a Noetherian local ring is exact and the completed local ring is faithfully flat. The completion arguments below have these Noetherian finite-module hypotheses.

To spell out the smooth canonical-bundle identification used for the trace, embed the smooth projective variety in \(\mathbb P^N\). Locally its regular-immersion Koszul resolution gives
\[
\mathcal E xt^c_{\mathbb P^N}(\mathcal O_A,\omega_{\mathbb P^N})
 =\det(I/I^2)^*\otimes i^*\omega_{\mathbb P^N}.
\]
The cotangent exact sequence of the smooth regular immersion identifies the right side with \(\det\Omega_A^1\). Changes of the regular equations transform the Koszul determinant by the inverse determinant, so these local identifications glue. Dualizing sheaves and Serre duality for projective schemes's representing trace then supplies the required trace on \(H^g(\Omega_A^g)\). The local Koszul and cotangent comparisons give the differential identification here.

The earlier results have the stated hypothesis boundaries. Their remaining local-algebra, affine-sheaf and proper-cohomology foundations are explicit premises; the conditional theorem below retains those premises.

#### 4.2.1. Scope and the actual imported arguments (G0)

Let \(k\) be any field of characteristic zero. An abelian variety is a smooth projective geometrically integral commutative \(k\)-group. Write \(0\) for its identity, \(g=\dim A\), and
\[
V=0^*\Omega^1_{A/k},\qquad W=V^*=\operatorname{Lie}(A).
\]
Invariant translation identifies \(\Omega^1_A\) with \(V\otimes_k\mathcal O_A\). The proof is the shear
\((a,b)\mapsto(a+b,b)\), followed by pullback along \(b\mapsto(0,b)\); it is the actual [The structure of the Picard scheme](../../AG-HP/src/the-structure-of-the-picard-scheme.md) Lemma 4.2 argument. Constants below are relative constants on every ordinary \(k\)-scheme, including nonreduced and non-Noetherian ones.

Actual [Relative divisors and the existence of the Picard scheme](../../AG-HP/src/relative-divisors-and-the-existence-of-the-picard-scheme.md) §§1–8 constructs the separated locally finite type Picard scheme for a projective flat family with geometrically integral fibres. Its construction uses positive divisor charts, the proper flat relation, the Hilbert scheme of whole equivalence classes and effective descent of its invariant graph ideal. It does not assume an abelian dual. Applied to \(A/k\), it supplies \(Q=\operatorname{Pic}_{A/k}\) on all test schemes. Actual [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) Theorem 2.1 identifies this sheaf with line bundles rigidified at \(0\): normalize a bundle by its fibre at \(0\); an automorphism preserving that fibre is the identity, since functions on \(A_T\) come from \(T\). Its descent argument therefore gives the normalized universal line on \(A\times Q\).

Actual AG-GS, *Group schemes over a field*, Theorem 2.3 supplies the open, geometrically irreducible, quasi-compact identity subgroup \(D=Q^0\). Since \(Q\) is locally of finite type, \(D\) is of finite type. The same actual proof supplies compatibility with field extension. We use the whole component scheme, including its possible nilpotents at this stage.

Actual Coherent sheaves on projective schemes: Serre's theorems §§1–2 proves finite coherent cohomology and ample generation by denominator extension and descending induction through coherent kernels. Actual [Cohomology of affine schemes and Serre's criterion](../../AG-QC/src/affine-cohomology-and-serres-criterion.md) Lemma 2.1 and Theorem 2.2 supplies affine acyclicity by a localized contraction and the actual Čech cohomology basis criterion; Čech cohomology Theorems 2.1 and 3.2 supply the finite ordered Čech comparison. Actual [Base change and the Grothendieck complex](../../AG-QC/src/base-change-and-the-grothendieck-complex.md) §2 proves flat base change from those section complexes. For the fixed varieties here every \(k\)-algebra is flat over \(k\).

In particular \(\Gamma(A,\mathcal O_A)=k\). After algebraic closure, coherent finiteness gives a finite-dimensional domain, hence the algebraically closed field; finite Čech tensoring descends this equality. The same tensoring gives
\[
(p_T)_*\mathcal O_{A_T}=\mathcal O_T
\quad\text{for every ordinary }T.
\tag{G0.1}
\]
Products \(A^n\) have the same property. These statements retain nilpotents in \(T\).

All geometry through G8 concerns ordinary parameter schemes. The finite constructions pull back to derived parameters, but they are **not** a claim that the full derived local-system stack of a higher-dimensional abelian variety is this smooth classical connection scheme. The separate F0–F7 proofs retain the curve's higher mapping-space statement.

#### 4.2.2. The dimension bound without abelian duality (G1)

Choose a projective embedding of \(A\). Successively choose \(g\) hyperplanes avoiding the irreducible components left by the preceding cuts. A proper closed subset of a finite-dimensional irreducible component has strictly smaller dimension: prepend that component to every strict chain of irreducible closed subsets of the proper subset. Thus each nonempty cut drops dimension. Choose one final hyperplane avoiding the resulting finite set. Over the infinite field \(k\) these choices are possible. Work with the finitely many geometric components at each stage; the \(k\)-linear forms vanishing identically on any one impose a proper \(k\)-linear condition, since some projective coordinate is nonzero on it. Finitely many proper linear subspaces do not fill the space of forms over an infinite field. Thus \(g+1\) hyperplane complements cover \(A\). Each is affine and every intersection is a principal affine open. The ordered Čech complex has length \(g\), proving
\[
H^i(A,\mathcal O_A)=0\quad(i>g).
\tag{G1.1}
\]
This is a direct finite-cover proof; it does not import the general topological cohomological-dimension theorem.

For two such covers the product affine cover is computed by the double Čech resolution. Each augmentation is stalkwise contracted on its cover members, and products of the affine members are affine. The double section complex is the tensor product of the two section complexes. Splitting complexes over \(k\) proves the Künneth isomorphism.

The product and the sign used here have an explicit cochain model. For ordered Čech cochains \(a\) and \(b\) of degrees \(p,q\), set
\[
(a\smile b)_{i_0\ldots i_{p+q}}
=a_{i_0\ldots i_p}b_{i_p\ldots i_{p+q}},
\]
restricting both factors to the displayed intersection. Expanding the alternating deletion differential gives
\(\delta(a\smile b)=\delta a\smile b+(-1)^p a\smile\delta b\): deletions before the common index belong to the first factor, those after it to the second, and the two common-index terms cancel. The same formula is associative and commutes with restriction and pullback after a common affine refinement. In the double resolution the total product uses
\[
(a\otimes b)(a'\otimes b')=(-1)^{|b||a'|}(a\smile a')\otimes(b\smile b').
\]
This is the sign making the total differential a derivation. It induces the displayed Künneth product. In the only skew-commutativity case required below, degree-one cocycles satisfy \(a_{ik}=a_{ij}+a_{jk}\) and similarly for \(b\). Therefore the degree-one cochain \(h_{ij}=a_{ij}b_{ij}\) has
\(\delta h=-(a\smile b+b\smile a)\).
Thus degree-one cohomology elements anticommute. These formulas supply the multiplicativity and signs needed in the cohomology bialgebra
\[
H=H^\bullet(A,\mathcal O_A),\qquad
\Delta=m^*:H\longrightarrow H\otimes_k H.
\]
Every \(u\in H^1\) is primitive: the only total-degree-one components are \(H^1\otimes k\) and \(k\otimes H^1\), and restriction to the two identity axes makes both coefficients \(u\).

If \(u_1,\ldots,u_r\) are linearly independent in \(H^1\), the component of the iterated coproduct of \(u_1\cdots u_r\) in \((H^1)^{\otimes r}\) is
\[
\sum_{\sigma\in S_r}\operatorname{sgn}(\sigma)
u_{\sigma(1)}\otimes\cdots\otimes u_{\sigma(r)}.
\tag{G1.2}
\]
It is nonzero: extend these vectors to a basis and inspect the coefficient of \(u_1\otimes\cdots\otimes u_r\), which is \(1\). Thus \(u_1\cdots u_r\ne0\). Equation (G1.1) implies \(r\le g\), so
\[
h^1(A,\mathcal O_A)\le g.
\tag{G1.3}
\]
No structure theorem for graded Hopf algebras or Hodge theory is used.

#### 4.2.3. The ample kernel and the constructed dual (G2)

Choose a very ample line \(N\) on \(A\), and normalize the line on \(A\times A\)
\[
M_N=m^*N\otimes p_1^*N^{-1}\otimes p_2^*N^{-1}
\otimes (N_0)_{\mathrm{const}}.
\]
It is canonically trivial on both identity axes. Its family in the first variable defines
\(\phi_N:A\to Q\). Since \(A\) is connected and \(\phi_N(0)=0\), its image lies in \(D\). The actual relative cube of AG-GS, *Abelian varieties*, Theorem 4.1, shows that \(\phi_N\) is a homomorphism on all test schemes: pulling the cube along the two translating parameters gives the additive class identity with all constant fibre factors retained.

Let \(K=\ker\phi_N\), a closed proper finite type subgroup of \(A\). Over \(A\times K\), the rigidified line \(M_N\) is the trivial line, by the represented rigidified Picard functor itself. Hence translation of \(N\) over \(K\) differs from \(N\) by a line from \(K\). Pushing sections forward gives projective linear automorphisms of the fixed very ample embedding. Explicitly the isomorphism
\[
t^*N\simeq p_A^*N\otimes p_K^*(N|_K\otimes N_0^{-1})
\]
identifies their bundles of sections up to the displayed scalar line. Local trivializations of that scalar line produce invertible matrices differing by scalar matrices on overlaps. They therefore give a morphism \(K\to\operatorname{PGL}(H^0(A,N))\).

The target is affine: invertible projective matrices form the standard Proj open \(D_+(\det)\), whose ring is the degree-zero part of the determinant localization. Work over an algebraic closure, and take the reduced identity subgroup \(K_{\mathrm{red}}^0\). Reduced groups over a perfect field are subgroups; the actual group-component argument makes this one proper and geometrically integral. Its functions are constants by G0. Any map from it to that affine target is therefore constant, and its value at the identity is the identity matrix.

Consequently its translations act trivially on the embedding of \(A\). Since the embedding is a closed immersion, its action on \(A\) is trivial as a morphism. Evaluating at \(0\) identifies its inclusion in \(A\) with the constant zero map. A positive-dimensional closed subgroup cannot have this inclusion, so \(\dim K_{\mathrm{red}}^0=0\). The geometric components of \(K\) are translates of its identity component; hence \(\dim K=0\). A zero-dimensional proper finite type scheme is finite, by the actual [The theorem on formal functions](../../AG-QC/src/the-theorem-on-formal-functions.md) Theorem 5.2 proof (or its zero-dimensional affine specialization). Thus \(K\) is finite over \(k\).

Fibres of \(\phi_N\), after extending the residue field and choosing a point in a nonempty fibre, are translates of \(K\). They are zero-dimensional. The map has closed image since \(A\) is proper and \(D\) separated; give that image its reduced structure \(Z\). Since \(A\) is reduced, its morphism factors through \(Z\). On a dominating affine source chart the generic fibre over \(k(Z)\) is a zero-dimensional finite-type domain, hence a field finite over \(k(Z)\) by the actual Zariski lemma. Its fraction field is \(k(A)\). Actual [Krull dimension and Noether normalization](../../AG-CA/src/krull-dimension-and-noether-normalization.md) Theorem 4.2, using Noether normalization, identifies dimensions of these finite-type varieties with their function-field transcendence degrees. The finite extension therefore proves
\(\dim Z=g\).
This calculation uses no smoothness or prior abelian-variety assertion for \(D\). On the other hand the actual dual-number transition calculation of [The structure of the Picard scheme](../../AG-HP/src/the-structure-of-the-picard-scheme.md) Proposition 2.1 gives
\[
T_0D=H^1(A,\mathcal O_A).
\]
For the dimension comparison work first over \(\bar k\). A maximal chain of irreducible closed subsets in \(D_{\bar k}\) ends at a closed point: otherwise a closed point in its last member would extend it. Translation carries its endpoint to the identity and identifies its local prime chain there. Thus local dimension at the identity is the global dimension; no smoothness assumption is being used in this equality. Actual [Dimension theory of Noetherian local rings](../../AG-CA/src/dimension-theory-of-noetherian-local-rings.md) Proposition 4.2 proves local dimension is at most embedding dimension, by Nakayama and its proved local dimension theorem. Consequently
\[
g\le\dim D\le\dim T_0D=h^1(A,\mathcal O_A)\le g.
\tag{G2.1}
\]
All are equal over \(\bar k\). The local ring at the identity is regular; its point is smooth, by the actual smooth local/Jacobian criterion. Translations carry smoothness to every closed point. The nonsmooth locus is closed and would have a closed point if nonempty. Thus \(D_{\bar k}\) is smooth; the geometric smooth criterion gives the assertion over the perfect field \(k\). Smoothness and geometric connectedness make it geometrically integral. The coherent and tangent vector spaces in (G2.1) commute with field extension by the actual Čech and Picard calculations, so their dimensions and the equality descend to \(k\).

The closed image of \(\phi_N\) has the full dimension of \(D\), so is all \(D\). It remains surjective after base change. To prove \(D\) proper, for any \(T\) pull a closed subset of \(D_T\) back to \(A_T\). Its image in \(T\) is closed by properness of \(A\), and is the original subset's image by surjectivity. Thus \(D\) is universally closed; it is separated and finite type, so proper.

Finally actual AG-GS, *Group schemes over a field*, Theorem 6.2 constructs an ample line on every finite type group scheme. Its line-bundle prerequisites remain the recursive boundaries in G10. The proper locally closed immersion it supplies is closed, by the graph argument. Hence \(D\) is projective. We have constructed the smooth projective dual of dimension \(g\), without using the stated abelian-duality theorem:
\[
\widehat A=D=\operatorname{Pic}^0_{A/k},\qquad
\dim D=h^1(A,\mathcal O_A)=g.
\tag{G2.2}
\]
The proof descends from algebraic closure and commutes with field extension through the actual Picard and component constructions. For \(g=0\), \(A\), \(D\), and all vector groups below are the point and the zero group.

#### 4.2.4. Normalized biextension, evaluation and its present boundary (G3)

Restrict the actual normalized universal line to \(P\) on \(A\times D\). Its restrictions on \(0\times D\) and \(A\times0\) have compatible trivializations. Apply the actual relative cube with \(X=Y=A\), parameter \(Z=D\), to
\[
m_A^*P\otimes p_{13}^*P^{-1}\otimes p_{23}^*P^{-1}
\quad\text{on }A\times A\times D.
\]
It is trivial on both \(A\)-identity slices and on the fibre \(D=0\). The parameter is connected. The cube proves actual triviality over \(D\), retaining all its scheme structure. Normalize the trivialization along \(A\times0\times D\). Any two such isomorphisms differ by a unit on \(A^2\times D\); by G0 that unit comes from \(D\), and normalization makes it \(1\). This gives unique multiplication in the \(A\)-variable.

Multiplication in \(D\) comes from the represented tensor-product identity: the two normalized lines on \(A\times D^2\) classify the same map \(D^2\to D\), so have a unique rigidified isomorphism. The unit, associativity, symmetry and interchange diagrams commute. Each compares normalized isomorphisms of the same lines; their ratio is a base unit equal to \(1\) on the identity slice. Pullback therefore gives these identities on every ordinary parameter scheme.

Applying G2 to \(D\) constructs \(D^\vee=\operatorname{Pic}^0(D)\). The family \(P\), with the factors interchanged, gives
\[
\kappa_A:A\longrightarrow D^\vee,\qquad
a\longmapsto P|_{\{a\}\times D},
\tag{G3.1}
\]
and the normalized comparison
\((1_D\times\kappa_A)^*P_D=\operatorname{swap}^*P\).
The map is a homomorphism by biextension multiplicativity.

The symmetry of \(M_N\) gives the actual all-family identity
\[
\phi_N=\phi_N^\vee\circ\kappa_A.
\tag{G3.2}
\]
Indeed pullback of the normalized line \(P_D\) along \(\phi_N^\vee\) classifies pullback of lines by \(\phi_N\); (G3.1) and the symmetry of \(M_N\) identify the resulting line with \(M_N\). The rigidified representing functor detects equality.

The map \(\phi_N\) is an isogeny by its finite kernel and equal-dimensional source and target. Any isogeny between these smooth varieties in characteristic zero is étale: its finite function-field extension is separable, so the Jacobian criterion gives a nonempty open with invertible differential; translation in source and target propagates it to every geometric point. Its finite kernel is consequently étale. Over algebraic closure it is an ordinary finite group, killed by its order; equality with the zero morphism descends to \(k\).

Its dual is also an isogeny. Here the proof needs only the actual reverse-isogeny mechanism, not biduality: choose such a nonzero integer \(n\) killing the finite kernel and descend \([n]_A\) through its faithfully flat torsor quotient to \(\psi:D\to A\). Then \(\psi\phi_N=[n]_A\) and \(\phi_N\psi=[n]_D\). Dual pullback reverses composition and sends \([n]\) to \([n]\), by the Poincaré tensor identity. The two dual compositions are therefore multiplication by \(n\). Its actual finite-surjective multiplication proof shows that \(\phi_N^\vee\) is surjective with finite kernel.

Equation (G3.2) now makes \(\ker\kappa_A\) finite and its image full-dimensional and closed; hence \(\kappa_A\) is an isogeny. In characteristic zero a dominant map of these smooth varieties has a nonempty locus with invertible differential, since its function-field extension is finite separable. Translation in source and target propagates that locus to every geometric point for a homomorphism. Thus this isogeny is étale and
\[
d\kappa_A:W\xrightarrow{\sim}H^1(D,\mathcal O_D).
\tag{G3.3}
\]

**The degree-one conclusion needs the whole character kernel.** Equal dimensions and an invertible differential alone do not remove a finite étale kernel. Sections 4.2.12–4.2.20 prove
\(\ker(f^\vee)=\underline{\operatorname{Hom}}(\ker f,\mathbb G_m)\), including membership of every character-descended line in the identity Picard component on all ordinary families. They then apply (G3.2) to prove degree one. The Cais and Milne notes listed below give further reading; the character-kernel and degree arguments are given here.

#### 4.2.5. The actual connection scheme from first jets at the identity (G4)

Let \(A_1\) be the first infinitesimal neighbourhood of \(0\) in \(A\). Smoothness gives
\[
\mathcal O_{A_1}=k\oplus V,\qquad V^2=0.
\]
For a rigidified family \(L\) on \(A_T\) classified by \(T\to D\), define the finite locally free module
\[
Q_L=(p_T)_*(L|_{A_1\times T}).
\]
Restriction to \(0\) and the rigidification give
\[
0\longrightarrow V\otimes_k\mathcal O_T
\longrightarrow Q_L\longrightarrow\mathcal O_T\longrightarrow0.
\tag{G4.1}
\]
For the actual \(P\), this is a rank-\(g+1\) vector bundle sequence on \(D\). Finite restriction and pushforward here commute with every base change, as one checks in the finite free algebra \(k\oplus V\).

The shear \((x,y)\mapsto(x,y-x)\) identifies the first neighbourhood of the diagonal of \(A_T\) with \(A_T\times_T(A_1\times T)\). The normalized \(A\)-multiplication of \(L\) identifies its principal parts with
\[
P^1_{A_T/T}(L)
\simeq L\otimes_{\mathcal O_{A_T}}p_T^*Q_L.
\tag{G4.2}
\]
The quotient to \(L\) is the quotient in (G4.1). Thus a section \(q\in Q_L\) mapping to \(1\) defines an \(\mathcal O_{A_T}\)-linear splitting \(s_q\) of the first-principal-parts sequence, and
\(\nabla_q=j-s_q\) is a relative connection. Conversely a connection gives that splitting. Cancelling \(L\), its splitting is a global section of \(p_T^*Q_L\) over \(A_T\), which comes uniquely from \(Q_L\) by (G0.1). These constructions are inverse on families and their isomorphisms.

Changing \(q\) to \(q+v\) changes the connection to \(\nabla_q-v\), with \(v\) regarded as the invariant differential. Define \(Y\) to be this splitting scheme, with vector action fixed by
\[
\nabla\longmapsto\nabla+\omega.
\tag{G4.3}
\]
It is therefore the opposite of the direct splitting action \(q\mapsto q+\omega\). Locally splitting (G4.1) identifies \(Y\) with affine \(g\)-space over \(D\); its coordinate transitions are affine translations. It is an affine \(V_{\mathrm{add}}\)-torsor, represented on all ordinary test schemes, and is smooth of dimension \(2g\). Its universal line is exactly \((1_A\times\pi)^*P\), with the universal splitting and actual connection just constructed.

Every such connection is integrable and multiplicative in \(A\). To verify this on a possibly nonreduced \(T\), transport the induced connection on
\(m_A^*L\otimes p_1^*L^{-1}\otimes p_2^*L^{-1}\)
through its normalized trivialization. Its connection form is a global relative one-form on \(A_T^2\), zero on both identity axes. Invariant trivialization of differentials and (G0.1) identify these forms with
\((V\oplus V)\otimes\mathcal O_T\); restriction to the two axes is injective, so the form is zero. This is equality of actual sections over \(T\).

The curvature is consequently a primitive global two-form. Invariant differentials satisfy \(m^*\alpha=p_1^*\alpha+p_2^*\alpha\): this follows by translation from the addition map on the tangent spaces at the identity. A global two-form has coefficients in \(\bigwedge^2V\otimes\mathcal O_T\). Its mixed component after pullback by \(m\) is the injective map
\[
\alpha\wedge\beta\longmapsto
\alpha\otimes\beta-\beta\otimes\alpha
\quad\text{in }V\otimes V.
\]
It vanishes for a primitive two-form, so the curvature is zero. This injectivity holds over every \(k\)-algebra by a basis calculation, retaining nilpotents. Hence the constructed connection is flat.

Tensoring connections gives a morphism \(Y^2\to Y\) over addition in \(D\). The trivial line with \(d\) is its identity, and dual connection is inverse. These are actual principal-parts/tensor constructions, so satisfy the group identities on every parameter. The Poincaré comparison in both group variables is horizontal by the preceding calculation and by this tensor definition. Their unit, associativity, symmetry and interchange coherences are the unique normalized line comparisons. This proves the classical family assertion (G.2) and its universal connection.

#### 4.2.6. Extension class and the sign convention (G5)

Take an affine cover \(U_i\) of \(D\) trivializing the restriction of \(P\) to \(A_1\times D\), with frames \(e_i\) equal to \(1\) at \(0\). On overlaps write
\[
e_j=e_i(1+c_{ij}),\qquad
c_{ij}\in V\otimes\mathcal O_D(U_i\cap U_j).
\tag{G5.1}
\]
The products contain no quadratic terms. Thus \(c_{ij}+c_{jk}=c_{ik}\), and changes of frames change \(c\) by the ordered coboundary \(b_j-b_i\). This is a cocycle in \(H^1(D,\mathcal O_D)\otimes V\).

The family \(P|_{A_1\times D}\), now viewed as an infinitesimal family of lines on \(D\), is precisely the restriction of (G3.1). The actual Picard tangent calculation glues transitions \(1+\epsilon a_{ij}\), so evaluation on \(w\in W\) gives
\[
[c(w)]=d\kappa_A(w).
\tag{G5.2}
\]
This proves the representing tensor from the **actual universal family**, not from a count of tangent dimensions. Under (G3.3), the class \([c]\) is the coevaluation, or identity, in \(W\otimes W^*\).

We distinguish the ordered connection-section class from the affine-function extension class:

* The normalized first jets \(e_i\) define local splittings \(q_i\), with \(q_j-q_i=c_{ij}\). For the local connections \(\nabla_i=j-s_{q_i}\), the vector action (G4.3) gives
  \(\nabla_j-\nabla_i=-c_{ij}\).
  Thus the class defined as the ordered differences of local connection sections is \(-[c]\).
* Let \(F_1=(\pi_*\mathcal O_Y)_{\le1}\) be affine functions of degree at most one along the vector fibres. The leading coefficient is defined by the actual action (G4.3). This gives
  \[
  0\longrightarrow\mathcal O_D\longrightarrow F_1
  \longrightarrow W\otimes\mathcal O_D\longrightarrow0.
  \tag{G5.3}
  \]
  For \(\ell\in W\), let \(f_i^\ell(\nabla_i+\omega)=\ell(\omega)\).
  Since \(\nabla_j=\nabla_i-c_{ij}\),
  \(f_j^\ell-f_i^\ell=\ell(c_{ij})\).
  Therefore the extension class of (G5.3) is \(+[c]\), which is the identity.

The second is the explicit affine-function extension used in Laumon's native §2.3, equations (2.3.2)–(2.3.3). Its “identity class” is valid here by (G5.1)–(G5.2), independently of the cited universal-extension theorem. Lemma G uses this affine-function extension convention. With the ordered local-section convention, the class is its negative. Neither change requires dualizing the actual universal connection or altering the positive Fourier kernel.

The calculation commutes with every ordinary parameter change: its square-zero algebra, finite jet module, transition coefficients, action and affine-function maps are actual pullbacks. It does not assert the equality by evaluating only reduced fibres.

#### 4.2.7. Every vector extension and the universal one (G6)

Here \(B/k\) is any abelian variety and \(U\) a finite-dimensional \(k\)-vector space. Define the class of a \(U_{\mathrm{add}}\)-torsor using its degree-one affine-function extension and the leading coefficient of its positive action, as in (G5.3). Then commutative algebraic-group extensions satisfy
\[
\operatorname{Ext}^1_{\mathrm{groups}}(B,U_{\mathrm{add}})
\simeq H^1(B,\mathcal O_B)\otimes_k U.
\tag{G6.1}
\]
We prove the whole assertion used here, including existence of the group law.

An additive torsor on an affine scheme is Zariski trivial. An fppf trivializing cover can locally be replaced by a faithfully flat affine cover: its finite presentation and quasi-compact affine base let one take finitely many affine members. Its translation cocycle is a one-cocycle in the additive Amitsur complex. The actual proof in *Quotients and torsors*, lines 13–59, tensors that complex with the faithfully flat algebra and contracts it by multiplying the extra scalar into the first ordinary scalar; faithful flatness descends exactness. Thus that cocycle is a coboundary. Affine scheme descent in the same actual proof descends the torsor's polynomial algebra. It follows that additive torsors are represented affine morphisms, Zariski locally trivial, with their isomorphism classes computed by ordinary quasi-coherent \(H^1\).

Under local sections \(s_i\), the usual ordered translation cocycle is \(s_j-s_i\); the affine-function extension class is its negative, by the calculation in G5. Either convention gives the same bijective classification after recording this sign.

Let \(c\in H^1(B,\mathcal O_B)\otimes U\), and construct its affine-function torsor \(Z\). The fibre at \(0\) has a \(k\)-point, since an additive torsor on \(\operatorname{Spec}k\) is trivial; choose one as origin. By the double Čech calculation of G1,
\[
H^1(B^2,\mathcal O)=
H^1(B,\mathcal O)\oplus H^1(B,\mathcal O).
\]
Restricting to the two axes identifies these summands. Addition has identity restriction on each axis, so
\[
m^*c=p_1^*c+p_2^*c.
\tag{G6.2}
\]
The pullback \(m^*Z\) is therefore isomorphic to the Baer sum of \(p_1^*Z\) and \(p_2^*Z\). Baer sum is the quotient of the pair torsor by \((u,-u)\); local translation coordinates glue this quotient as an affine torsor. Such an isomorphism defines a multiplication \(Z^2\to Z\) lifting \(m\) and respecting addition in its vector coordinates.

Any two choices differ by a \(U\)-valued function on \(B^2\), hence a constant by G0. There is a unique choice sending the pair of origins to the origin. The left and right unit comparisons differ by a function on \(B\), zero at \(0\); hence are the identity. Associativity and commutativity differ by functions on \(B^3\) and \(B^2\), respectively, zero at their origins; hence hold as morphism identities. In local coordinates the multiplication is \((u,v)\mapsto u+v+h(x,y)\). Its inverse is \((x,u)\mapsto(-x,-u-h(x,-x))\); uniqueness of the inverse makes these local formulas glue. Thus \(Z\) is a commutative group extension.

The normalized multiplication is forced by its torsor and origin. Any comparison of torsors preserving origin becomes a group comparison by the same constant-function argument. Its ambiguity is a function \(B\to U\), constant and zero at \(0\), so is zero. This proves (G6.1), both surjectivity and injectivity, and the absence of hidden automorphisms. Baer sum and scalar maps of vector groups act by addition and the corresponding linear maps on the displayed cohomology tensors.

Put \(H=H^1(B,\mathcal O_B)\). The class corresponding to the identity of \(H\), viewed in \(H\otimes H^*\), therefore gives an actual extension
\[
0\longrightarrow H^*_{\mathrm{add}}\longrightarrow E_B
\longrightarrow B\longrightarrow0.
\tag{G6.3}
\]
For every \(U\), pushout by a linear map \(H^*\to U\) gives all extensions uniquely, since
\(\operatorname{Hom}_k(H^*,U)=H\otimes U\).
In characteristic zero morphisms of vector groups are linear: an additive polynomial has no term of degree at least two, by expanding \(f(x+y)=f(x)+f(y)\) and comparing mixed coefficients. This also holds over every \(k\)-algebra, since nonzero rational integers are invertible. Thus (G6.3) has the required universal property in algebraic groups, not only in a chosen category of vector-space maps.

The argument retains families. For an affine ordinary parameter \(T=\operatorname{Spec}R\), finite Čech tensoring gives
\[
H^1(B_R,\mathcal O)=H\otimes_k R,\quad
H^1(B_R^2,\mathcal O)=(H\oplus H)\otimes_k R,\quad
\Gamma(B_R^n,\mathcal O)=R.
\]
All normalized existence and uniqueness arguments therefore work over \(R\) itself, retaining nilpotents. They commute with every map \(R\to R'\), including nonflat ones: the fixed complexes and maps were tensored over the field. For a general ordinary \(T\), perform this construction on affine opens. Normalized uniqueness glues its group laws, comparison maps and pushouts. This is the family assertion for the base extension of the fixed abelian variety; it is not a theorem about arbitrary moving abelian schemes.

Apply this to \(B=D\). Equations (G3.3) and (G5.2) identify the affine-function class of \(Y\) with the coevaluation for \(H=H^1(D,\mathcal O_D)\), and identify \(H^*\) with \(V\). Thus **the actual connection extension \(Y\) is the universal vector extension of \(D\)**. This conclusion requires only the proved isogeny differential (G3.3), not the unproved degree-one assertion for \(\kappa_A\).

#### 4.2.8. The pointed Jacobian and its actual Abel self-duality (G7)

Let \(X/k\) be a smooth projective geometrically connected curve, with \(x_0\in X(k)\), and \(g=h^1(X,\mathcal O_X)\). Here is the passage from the actual separably closed construction of [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) to arbitrary characteristic-zero \(k\). Apply the actual general Picard construction of [Relative divisors and the existence of the Picard scheme](../../AG-HP/src/relative-divisors-and-the-existence-of-the-picard-scheme.md) to \(X/k\), and normalize its universal line at \(x_0\) by [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) Theorem 2.1. After extension to \(\bar k\), the represented functor is exactly the functor of [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) Theorem 6.2: both classify the same rigidified lines on every \(\bar k\)-scheme, so Yoneda identifies the schemes. Its actual symmetric-power charts prove smoothness and dimension \(g\). The degree pieces are open and closed by the actual Euler-characteristic/degree argument of [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) §7. Their degree-zero piece is geometrically connected by Theorem 7.2, hence equals the identity component \(J\); the component construction commutes with field extension. Smoothness over the perfect field \(k\) follows from this geometric smoothness by the same local smooth criterion as G2.

The high-degree Abel projective bundle is constructed over \(k\) itself, rather than merely asserted to descend. For \(n\ge\max(0,2g-1)\), twist the actual universal line on \(X\times J\) by \(\mathcal O_X(nx_0)\). The Riemann–Roch and differential-duality calculation in the actual [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) Proposition 7.1 gives zero \(H^1\) and constant \(h^0=n+1-g>0\) on every geometric fibre. Its actual proper flat cohomology/base-change argument therefore gives a locally free pushforward of that rank on \(J\), commuting with arbitrary ordinary base change. Evaluation identifies its projective bundle with \(X^{(n)}\): a line of sections nonzero on every fibre gives a relative effective Cartier zero divisor; conversely that divisor and the represented rigidified Picard identity give the line of sections. Those inverse constructions are the actual all-family proof in lines 323–343, and work over \(k\) once the represented universal line exists.

Consequently \(X^{(n)}\to J\) is a positive-rank projective bundle over \(k\), with its asserted arbitrary-parameter interpretation. Its proper geometrically irreducible source makes \(J\) finite type, proper and geometrically integral by the actual universally-closed image proof in [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) Theorem 7.2. The dimension is \(n-(n-g)=g\). The actual quasi-projectivity argument used in G2 makes this proper group projective. This constructs the pointed Jacobian and Abel projective bundle over every characteristic-zero field from actual earlier arguments. Their symmetric-power, Riemann–Roch, relative Cartier and proper cohomology foundations remain recursive obligations in G10.

Write \(j:X\to J\), \(x\mapsto\mathcal O_X(x-x_0)\), and \(D_J=\operatorname{Pic}^0(J)\), constructed by G2. Pullback gives a homomorphism
\[
r=j^*:D_J\longrightarrow J.
\tag{G7.1}
\]
We prove its injectivity on all ordinary test schemes. Suppose a rigidified family \(M\) on \(J_T\) has trivial rigidified pullback on \(X_T\). G3 gives its normalized multiplicative structure. Consequently its pullback along the sum
\[
s_n:X_T^n\longrightarrow J_T,\qquad
(x_1,\ldots,x_n)\longmapsto\sum_i j(x_i)
\]
is canonically trivial, with the ordinary permutation equivariance.

Take \(n\ge\max(0,2g-1)\). Factor \(s_n=a_nq_n\), where
\(q_n:X^n\to X^{(n)}\) is the finite symmetric quotient and
\(a_n:X^{(n)}\to J\) is Abel followed by tensoring with \(\mathcal O_X(-nx_0)\).
The symmetric quotient geometry is an explicit earlier foundation, retained in G10. For its quotient map the structure sheaf is the invariant direct image. This equality commutes with every ordinary parameter base change: every \(k\)-algebra is \(k\)-flat and invariants are the kernel of finitely many maps. For a line \(N\) on the quotient, local trivialization and the projection formula give
\[
(q_{n,*}q_n^*N)^{S_n}=N.
\]
The trivialization of \(s_n^*M\) is equivariant. Indeed the ratio between it and any permutation is a unit on \(X_T^n\), hence from \(T\), and its value on \((x_0,\ldots,x_0)\) is \(1\). It therefore descends by the displayed invariant identity to a trivialization of \(a_n^*M\).

Actual [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) identifies \(a_n\) with a positive-rank projective bundle. On arbitrary affine bases the standard projective-space Čech calculation gives \(p_*\mathcal O=\mathcal O\): the degree-zero common homogeneous polynomials are exactly the base ring. Thus \(a_n^*\) is fully faithful on line-bundle homomorphisms by adjunction and the projection formula. The trivialization descends to \(M\), respecting its origin frame. This proves that the sheaf kernel of \(r\) is zero, including nilpotent parameter tests.

Both varieties in (G7.1) are smooth projective of dimension \(g\). The kernel calculation includes dual-number tests, so the differential of \(r\) at the identity is injective, hence an isomorphism. Translation makes it étale everywhere. Its proper closed image has dimension \(g\), hence is all of the geometrically integral target. Its fibres have at most one geometric point by the kernel calculation. The actual proper-finite-fibre theorem makes it finite. It is finite étale of rank one and hence an isomorphism: on local rings the unit identifies a finite free rank-one algebra with its base. Therefore
\[
r=j^*:D_J\xrightarrow{\sim}J,\qquad
\lambda_{\mathrm{Abel}}=r^{-1}:J\xrightarrow{\sim}D_J.
\tag{G7.2}
\]
This is a proof of the Abel-normalized self-duality, not a stated principal-polarization theorem.

It also proves biduality for \(J\). Let \(P_X\) be the normalized universal line on \(X\times J\). Representability gives
\[
(j\times1_{D_J})^*P_J=(1_X\times r)^*P_X.
\tag{G7.3}
\]
Put \(H=\mathcal O_X(-x_0)|_{x_0}\), the one-dimensional conormal space at \(x_0\). The pullback of \(P_X\) along \(1_X\times j\) is the normalized diagonal correspondence
\[
\mathcal O_{X^2}(\Delta)\otimes
p_1^*\mathcal O_X(-x_0)\otimes p_2^*\mathcal O_X(-x_0)
\otimes H_{\mathrm{const}}^{-1},
\tag{G7.4}
\]
with the first-axis divisor-cancellation trivialization and the unique second-axis trivialization agreeing with it at \((x_0,x_0)\). Restriction of the first three factors to either slice is the constant line \(H\); the displayed inverse constant factor cancels it. Compatibility at their intersection matters: if \(u,v\) are the same local parameter in the first and second factors, the local diagonal generator is \((v-u)^{-1}\). Its restrictions are \(v^{-1}\) and \(-u^{-1}\), so the two raw divisor-cancellation frames differ by a minus sign. Multiply the raw second-axis trivialization by \(-1\) to make them agree. The represented rigidified neutral line forces exactly this compatibility. This construction follows on families from the relative Cartier divisor given by the diagonal: its fibre at \(y\) is \(\mathcal O_X(y-x_0)\), with the specified rigidification.

The underlying correspondence is symmetric. In the displayed local generator the natural divisor-swap comparison contributes \(-1\); its negative is the normalized comparison preserving the compatible axis trivializations. The latter is also obtained by comparing the two normalized rigidified families, so is independent of the chosen parameter. Its square is the identity by normalized uniqueness. This unit normalization changes no line-bundle class and does not change the Abel/theta distinction below.

Put \(B=(1_J\times\lambda_{\mathrm{Abel}})^*P_J\). Equations (G7.3)–(G7.4) show that \((j\times j)^*B\) is symmetric. This detects symmetry of \(B\) itself: the ratio with its swapped line is a normalized biextension. Apply the all-family injectivity of \(j^*\) first to its families with parameter \(X\), then to those with parameter \(J\). Triviality on \(X^2\) forces triviality on \(X\times J\) and then on \(J^2\). Normalized uniqueness also detects the symmetry isomorphism and its coherences.

The transpose of the biextension classified by \(\lambda_{\mathrm{Abel}}\) is classified by
\(\lambda_{\mathrm{Abel}}^\vee\kappa_J\), by the definition (G3.1) of evaluation. Symmetry therefore gives
\[
\lambda_{\mathrm{Abel}}^\vee\kappa_J=\lambda_{\mathrm{Abel}}.
\tag{G7.5}
\]
Dual pullback sends an isomorphism to an isomorphism by pulling back its inverse. Equation (G7.5) makes \(\kappa_J\) an isomorphism. This special proof uses the actual Abel detecting family; it does not assert biduality for a general abelian variety.

For the conventional ample theta polarization, the translation convention is \(\phi_L(a)=t_a^*L\otimes L^{-1}\). The determinant comparison in §4.2.26 proves
\[
\phi_{\Theta}=-\lambda_{\mathrm{Abel}}.
\tag{G7.6}
\]
The minus sign is produced by the inverse determinant defining the effective theta line. Sections 4.2.22–4.2.28 prove the divisor construction, ampleness and this equality. The positive Abel comparison \(\lambda_{\mathrm{Abel}}\) continues to classify the positive universal line used below. Further reading with this translation convention is Milne, [*Jacobian Varieties*, Lemma 6.9 and Remark 6.10(c)](https://www.jmilne.org/math/xnotes/JVs.pdf).

#### 4.2.9. Connections on the Jacobian and on the curve (G8)

Pullback along \(j\) defines a map from the actual \(Y_J\) of G4 to rigidified degree-zero connections on \(X\). The base map is the isomorphism \(r\) in (G7.2). Its vector-kernel map is
\[
j^*:H^0(J,\Omega_J^1)\longrightarrow H^0(X,\Omega_X^1).
\tag{G8.1}
\]
It is injective. If an invariant differential \(\alpha\) pulls back to zero on \(X\), its pullback by \(s_n\) is \(\sum_i p_i^*j^*\alpha=0\). The map \(s_n\) is dominant, since \(q_n\) and the Abel projective bundle are surjective. In characteristic zero its extension of function fields is separably generated; the extension-of-derivations argument, with a transcendence basis followed by the actual finite-separable calculation of [Kähler differentials](../../AG-CA/src/kahler-differentials.md), shows that pullback of differentials is injective at the generic point. Hence \(\alpha=0\).

The source of (G8.1) has dimension \(g\) by invariant trivialization. After extension to \(\bar k\), the target has dimension \(g\) by the actual curve differential-duality proof R3–R9. Finite coherent Čech tensoring commutes with that field extension for both \(\mathcal O_X\) and \(\Omega_X^1\), so their cohomology dimensions are unchanged and this equality descends to \(k\). This uses the actual residue proof at its algebraically closed field boundary; it does not assert that its completed-DVR formula with residue field \(k\) applies verbatim over a nonclosed field. Thus (G8.1) is an isomorphism, commuting with every ordinary parameter change by the same fixed-coefficient tensor calculation.

This also constructs the curve's degree-zero connection torsor over \(k\), independently of extending the traced obstruction formula beyond its written field boundary. For an arbitrary ordinary \(T\), a rigidified degree-zero line \(L\) on \(X_T\) defines \(T\to J\). Via the isomorphism \(r\), it defines a unique normalized line \(M\) on \(J_T\). The pullback identity (G7.3) gives a specified \(j^*M=L\). Locally on affine opens of \(T\), the represented torsor \(Y_J\) gives a connection on \(M\), hence one on \(L\). Any other relative connection on \(L\) differs by a global relative one-form on \(X_T\). Finite Čech tensoring identifies those forms with \(H^0(X,\Omega_X^1)\otimes\mathcal O_T\). The isomorphism (G8.1) therefore lifts that difference uniquely to \(M\). Since \(\Omega_{X_T/T}^2=0\), every such curve connection is integrable. Normalization eliminates scalar arrows. These inverse transformations commute with restriction and every base change, so glue on arbitrary \(T\). They prove the actual torsor comparison, retaining nilpotent parameters.

A morphism of torsors whose base and vector-kernel maps are isomorphisms is an isomorphism: locally choose sections and it is the corresponding affine translation composed with the invertible linear map. These local inverses agree on overlaps. Hence
\[
j^*:Y_J\xrightarrow{\sim}J_X^\natural
\tag{G8.2}
\]
on every ordinary parameter scheme, with the actual universal lines and connections.

At the actual algebraically closed characteristic-zero field scope of [Geometric class field theory](geometric-class-field-theory.md), its positive class-field line \(C_E^0\), actual Theorem 4.1 and multiplication/unit proof give
\(j^*C_E^0=E\otimes E_{x_0}^{-1}\).
After rigidification this is \(E\). G7–G8 show that the inverse comparison is unique on these rigidified lines and connections. Thus the point \(e\in Y_J\) corresponding to \(E\) has
\[
\mathcal P_e=C_E^0.
\tag{G8.3}
\]
This is exactly the positive universal-line identification needed in §4.8. The downward line is its inverse, \(C_{E^{-1}}^0\), as the existing [Geometric class field theory](geometric-class-field-theory.md) convention states. The actual universal biextension identities supply its unit and tensor coherences. Over a general characteristic-zero \(k\), (G8.2) itself constructs the corresponding Abel-normalized multiplicative line and connection; it does not silently extend an unproved field version of [Geometric class field theory](geometric-class-field-theory.md).

For connective DG parameter algebras, (G8.2) is the classical torsor comparison and its base extension. It does not discard the curve's derived degree equation or \(B\mathbb G_m\). Their higher mapping-space and Koszul factors remain the separate proved F0–F7/R/B constructions in §1. No equivalence between a higher-dimensional abelian variety's entire derived local-system stack and this classical \(Y_J\) is claimed.

#### 4.2.10. Exact remaining obligations (G10)

**General degree-one evaluation.** Sections 4.2.12–4.2.20 construct the whole character-descended Picard kernel, prove its identity-component membership on all ordinary families and obtain equal dual-isogeny degrees. Consequently (G3.2) gives \(\deg\kappa_A=1\). These deductions retain the recursive foundations listed below.

**The theta divisor and its sign.** G7 proves Abel self-duality and symmetric normalized correspondence. Sections 4.2.22–4.2.29 additionally construct the geometrically reduced irreducible effective theta divisor for \(g\geq1\), prove its ampleness and identify \(\phi_\Theta=-\lambda_{\mathrm{Abel}}\). Their determinant comparisons hold on every ordinary parameter scheme. For \(g=0\), the empty divisor gives the trivial ample line on the point Jacobian. The geometric and local-algebra foundations of these arguments remain explicit below.

**The actual programme imports retain their recursive boundaries.** In particular:

* [Relative divisors and the existence of the Picard scheme](../../AG-HP/src/relative-divisors-and-the-existence-of-the-picard-scheme.md)'s general Picard argument retains the Hilbert/Quot construction, relative Cartier criterion, perfect proper flat cohomology, positive-twist generation and finite-presentation descent foundations. Those earlier Hilbert, Cartier and coherent-descent foundations are not proved in this lesson.
* The AG-GS component and quasi-projectivity arguments retain their stated general component-structure, regular-local factoriality, Cartier affine-complement, line-bundle homotopy and ample field-descent foundations. The three explicit line-bundle prerequisites in Theorem 6.2 are not proved here.
* Sections GB1–GB2 supply finite étaleness and multiplication rank in characteristic zero without miracle flatness, and GB6 supplies the required reverse-isogeny descent. Their cube, coherent Hilbert-polynomial, dimension and proper-finite-fibre/formal-functions foundations remain explicit. Unused finite-quotient and miracle-flatness routes are not required by these new deductions.
* The curve Abel projective-bundle argument retains its relative symmetric-power/Cartier construction, Riemann–Roch, proper coherent base change and the Picard chart foundations. G7 supplies the passage to arbitrary characteristic-zero fields using the represented universal line and the actual all-family evaluation argument; it does not reconstruct those prerequisite constructions.
* Fixed coherent Čech arguments retain the actual affine-module, injective-resolution and acyclic-cover foundations. The function-field dimension calculation retains [Krull dimension and Noether normalization](../../AG-CA/src/krull-dimension-and-noether-normalization.md)'s integral-extension/Noether-normalization and Zariski-lemma foundation chain; the local embedding-dimension inequality retains [Dimension theory of Noetherian local rings](../../AG-CA/src/dimension-theory-of-noetherian-local-rings.md)'s Hilbert–Samuel growth, prime-avoidance and Nakayama chain. G1 supplies the cup multiplication and the degree-one/Koszul sign used in its primitive calculation directly. The residue and F0–F7 arguments retain their local-algebra and derived-descent foundations. Ordinary groupoids and tangent dimensions have not been substituted for higher descent.

These foundational obligations concern every characteristic-zero pointed curve and every ordinary parameter scheme. The theta and general biduality deductions below retain that full scope, together with the recursive premises just listed.

#### 4.2.11. Further reading

Further reading is Gérard Laumon, [*Transformation de Fourier généralisée*, §§2.1–2.3](https://arxiv.org/abs/alg-geom/9603004v1); Bryden Cais, [*Abelian Varieties*, notes of 17 December 2004, pp. 8–13](https://math.stanford.edu/~conrad/vigregroup/vigre04/abvaralg.pdf); J. S. Milne, [*Abelian Varieties*, author edition of 2 January 2022, §§9–11](https://www.jmilne.org/math/xnotes/AVs.pdf), and [*Jacobian Varieties*, author edition of 12 June 2021, §6](https://www.jmilne.org/math/xnotes/JVs.pdf). General degree-one evaluation is proved in §§4.2.12–4.2.20, theta geometry in §§4.2.22–4.2.29, and the universal connection and its affine-function class in §§4.2.5–4.2.7.

#### 4.2.12. Scope, conventions and actual inputs (GB0)

Let \(k\) be an arbitrary field of characteristic zero. Let \(A,B\) be abelian varieties over \(k\), meaning smooth projective geometrically integral commutative groups. All isogenies are fixed over \(k\); parameter schemes \(T\) range over **every ordinary \(k\)-scheme**, including nonreduced and non-Noetherian ones. An isogeny initially means a finite surjective homomorphism. Nothing here assumes \(k\) algebraically closed or containing roots of unity. We do not assert this proof for arbitrary varying abelian schemes or identify an entire derived mapping stack with a classical scheme.

Write
\[
Q_C=\operatorname{Pic}_{C/k},\qquad
D_C=Q_C^0.
\]
We use the actual rigidified Picard construction and the already proved G0–G2: \(Q_C(T)\) is the group of lines on \(C_T\) rigidified at \(0_T\), \(D_C\) is a smooth projective geometrically integral group, and
\[
\dim D_C=\dim C,\qquad
(p_T)_*\mathcal O_{C_T}=\mathcal O_T.
\tag{GB0.2}
\]
The second assertion also holds for products \(C^r\). Its proof is finite affine Čech tensoring over the field, not a reduced-parameter shortcut. Actual [Relative divisors and the existence of the Picard scheme](../../AG-HP/src/relative-divisors-and-the-existence-of-the-picard-scheme.md) §§1–8 and [The Picard functor and the Picard scheme of a curve](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md) Theorem 2.1 provide the rigidified representing functor; actual AG-GS component and projectivity arguments supply the scheme foundations used in G2. Their explicit recursive boundaries remain in GB9.

We also use the actual G3 normalized universal Poincaré line, its two multiplication isomorphisms, and their uniquely normalized coherences. In particular, for every \(T\to D_C\), the classified line \(L\) satisfies the normalized identity
\[
[n]^*L\simeq L^{\otimes n}.
\tag{GB0.3}
\]
Indeed its pullback along the sum of \(n\) identical arguments is the tensor of the \(n\) pullbacks, by G3 multiplication in the \(C\)-variable. The identity is compatible with every \(T'\to T\). Its proof does not use the assertion that the evaluation map has degree one.

Here and below \(\deg h\) is the locally free rank of a finite surjective homomorphism. GB1 proves this local freeness in characteristic zero. The proof uses the earlier cube, coherent Hilbert-polynomial, dimension, proper finite-fibre and module-descent arguments at their stated hypotheses. GB3–GB8 give the character-component and degree deductions explicitly.

#### 4.2.13. Finite homomorphisms in characteristic zero are finite étale (GB1)

Let \(h:C\to E\) be a finite surjective homomorphism of abelian varieties. Their dimensions agree: a finite dominant map induces a finite extension of function fields, and actual [Krull dimension and Noether normalization](../../AG-CA/src/krull-dimension-and-noether-normalization.md) Theorem 4.2 identifies dimensions with transcendence degrees. We prove directly that \(h\) is finite étale.

First work over an algebraic closure. The generic function-field extension is separable in characteristic zero. Explicitly the derivative of an irreducible nonconstant polynomial in characteristic zero is nonzero and has smaller degree, so it is coprime to that polynomial. For every algebraic generator \(\alpha\), its minimal-polynomial relation therefore gives \(p'(\alpha)d\alpha=0\) with \(p'(\alpha)\) invertible; through a finite tower this proves that the relative field differentials vanish. This agrees with the actual [Kähler differentials](../../AG-CA/src/kahler-differentials.md) separability argument. On a nonempty affine open of \(E\), the finite module \(h_*\mathcal O_C\) is free after one localization: choose a basis in the generic field, put its elements in the module after clearing denominators, and clear denominators again to kill the finite torsion cokernel. Relative differentials vanish generically, so after further localization their finite module is zero. Finite presentation, flatness, and vanishing differentials imply étaleness by the actual square-zero/Jacobian proof of [Smooth algebras over a field and the Jacobian criterion](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md) Theorem 6.2. The nonempty open has a geometric closed point by the actual [The Nullstellensatz and Jacobson rings](../../AG-CA/src/the-nullstellensatz-and-jacobson-rings.md) Nullstellensatz. Its fibre consists of \(r\) reduced points, where \(r\) is the generic rank.

Every geometric fibre of \(h\) is isomorphic as a scheme to \(K=\ker h\): choose a point \(c\) above the geometric point \(e\), and translation by \(c\) identifies \(K\) with the fibre. The fibre just found shows that \(K\) is reduced and has \(r\) points. Consequently **every** geometric fibre is reduced with \(r\) points.

Here is the needed flatness deduction without a Cohen–Macaulay or miracle-flatness input. On an affine open of the reduced target write a finite presentation
\[
R^b\xrightarrow{M}R^a\longrightarrow h_*\mathcal O_C\longrightarrow0.
\]
At every geometric point the matrix has rank \(a-r\). All its \((a-r+1)\)-minors therefore vanish at every prime of \(R\), hence vanish in \(R\), since \(R\) is reduced. At any given point an \((a-r)\)-minor is a unit on a neighbourhood. Row and column operations there put the matrix in the form
\[
\begin{pmatrix}I_{a-r}&0\\0&M'\end{pmatrix}.
\]
Every entry of \(M'\) is, up to a unit, a minor of size \(a-r+1\), so \(M'=0\). The cokernel is free of rank \(r\). This proves local freeness on the whole target. The case \(a-r=0\) says that all entries vanish; the same conclusion holds.

The finite module \(\Omega^1_{C/E}\) has zero fibre at every geometric point because the geometric fibres are products of copies of the algebraically closed field. Nakayama makes it zero. [Smooth algebras over a field and the Jacobian criterion](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md) Theorem 6.2 now proves étaleness everywhere. Alternatively all the matrix equalities and differential vanishing can be tested after the faithful field extension \(\bar k/k\), so the same conclusion holds over \(k\).

Thus \(h\) is finite étale of constant rank \(r\), its kernel is finite étale of rank \(r\), and these assertions survive **every** ordinary base change. The scheme isomorphism
\[
C\times K\xrightarrow{\sim}C\times_E C,\qquad
(c,u)\longmapsto(c,c+u),
\tag{GB1.1}
\]
has inverse \((c,c')\mapsto(c,c'-c)\). It proves that \(h\) is a \(K\)-torsor and an fpqc cover, with its actual scheme structure on every \(T\).

#### 4.2.14. The degree of multiplication (GB2)

For any abelian variety \(C\) of dimension \(g\) and \(n\ge1\), we prove
\[
[n]_C\text{ is finite étale of degree }n^{2g}.
\tag{GB2.1}
\]
Choose a very ample line \(H\). The symmetric line
\[
N=H\otimes[-1]^*H
\]
is very ample: the product of the two closed projective embeddings followed by the Segre embedding has this line as its pullback of \(\mathcal O(1)\). Its positive powers are very ample by the Veronese embedding.

Here the two elementary embedding facts need no further theorem of abelian varieties. In Segre coordinates \(z_{ij}=x_i y_j\), the two-by-two minors vanish. On \(z_{ij}\ne0\), those equations give
\[
\frac{z_{ab}}{z_{ij}}=
\frac{z_{aj}}{z_{ij}}\frac{z_{ib}}{z_{ij}},
\]
with coordinates \(x_a/x_i=z_{aj}/z_{ij}\), \(y_b/y_j=z_{ib}/z_{ij}\). These charts recover exactly the product of the projective charts, so the closed minor scheme is that product. The map from \(C\) to the product is closed because its first factor is a closed immersion and its second factor is a graph into a separated projective space. The chart transition functions give pullback \(\mathcal O(1)=H\otimes[-1]^*H\). For the \(m\)-th Veronese, the map from the polynomial ring in all degree-\(m\) monomials onto the Veronese graded subring is surjective, hence gives a closed Proj immersion. On its chart \(x_i^m\ne0\), the degree-zero localization is \(k[x_j/x_i]\): these ratios equal \((x_jx_i^{m-1})/(x_i^m)\), and every degree-zero monomial fraction is a product of them. These charts cover, since every degree-\(m\) monomial has a power divisible by some \(x_i^m\). They identify that Proj with the original projective space and identify the pulled-back line with \(\mathcal O(m)\). Thus all the positive powers used above really are very ample.

For completeness the exact cube deduction of actual AG-GS *Abelian varieties* §5 is as follows. In the group of line classes set \(F_j=[j]^*[N]\). Pull the proved cube first along \(x\mapsto(x,x,-x)\), and then along \(x\mapsto(x,x,[j-1]x)\). With \(l=[N]\), \(i=[-1]^*[N]=l\), the resulting equations are
\[
F_2=3l+i,\qquad
F_{j+1}-2F_j+F_{j-1}=l+i=2l.
\]
Together with \(F_0=0,F_1=l\), this recurrence has solution \(F_j=j^2l\), by checking the initial conditions and second differences. Hence
\[
[n]^*N\simeq N^{n^2}.
\tag{GB2.2}
\]
No Picard identity-component or biduality theorem occurs in this cube calculation.

Every geometric fibre of \([n]\) is zero-dimensional. Otherwise a reduced integral positive-dimensional projective component \(Z\) of a fibre has trivial restriction of \([n]^*N\), since the map on it is constant. But \(N^{n^2}|_Z\) is very ample. Actual coherent finiteness gives \(\Gamma(Z,\mathcal O_Z)\) a finite-dimensional domain over the algebraically closed field, so it is that field. A trivial line on \(Z\) therefore has only a one-dimensional space of sections; its sections cannot give a closed embedding of a positive-dimensional \(Z\) into any projective space. This contradicts very ampleness. This argument needs no auxiliary hyperplane-curve existence or curve-degree theorem.

The map is proper by the graph argument for morphisms between proper schemes with separated target. The actual proper finite-fibre proof, [The theorem on formal functions](../../AG-QC/src/the-theorem-on-formal-functions.md) Theorem 5.2, makes it finite. Its closed image has dimension \(g\), by the actual finite-function-field dimension argument of [Krull dimension and Noether normalization](../../AG-CA/src/krull-dimension-and-noether-normalization.md); it is therefore all the geometrically integral target. GB1 makes it finite étale of rank \(r\).

We compute \(r\) with the actual Euler-polynomial theorems of [Euler characteristics and Hilbert polynomials](../../AG-QC/src/euler-characteristics-and-hilbert-polynomials.md) Theorems 2.1 and 3.1. Set
\[
P(m)=\chi(C,N^m).
\]
Those actual proofs give a polynomial of degree \(g\) with positive leading coefficient \(c\); a coherent sheaf with support of dimension less than \(g\) contributes degree less than \(g\). Finite pushforward and its projection formula give
\[
\chi(C,N^{n^2m})
=\chi\bigl(C,[n]_*\mathcal O_C\otimes N^m\bigr).
\tag{GB2.3}
\]
This equality can also be checked directly: a finite affine cover of the target pulls back to an affine cover of the source, its Čech terms agree with those for finite pushforward, and tensoring a line commutes with the finite affine section modules.

If \(E\) is a vector bundle of rank \(r\) on the integral projective \(C\), actual ample generation, Coherent sheaves on projective schemes: Serre's theorems §§1–2, supplies a \(t\) for which \(E\otimes N^t\) is globally generated. Choose \(r\) of its global generating sections that form a basis at the generic point. They give
\[
0\longrightarrow (N^{-t})^{\oplus r}\longrightarrow E
\longrightarrow F\longrightarrow0,\qquad
\dim\operatorname{Supp}F<g.
\]
Injectivity follows because the source is torsion-free and the map is injective at the generic point. Additivity of Euler characteristic and the degree bound show that the leading coefficient of \(\chi(E\otimes N^m)\) is \(rc\); replacing \(m\) by \(m-t\) leaves the leading coefficient unchanged.

Apply this to \(E=[n]_*\mathcal O_C\). In (GB2.3) the leading coefficients are \(c n^{2g}\) and \(rc\). Since \(c>0\), \(r=n^{2g}\). If \(g=0\), \(C\) is the point: the cokernel above is zero and the same formula is \(r=1=n^0\). The kernel \(C[n]\) inherits this finite étale rank under base change to the identity. This completes (GB2.1) with no use of abelian biduality, an abelian Riemann–Roch formula, Néron–Severi torsion-freeness, or intersection-theory degree calculations.

#### 4.2.15. The character scheme and its exact rank (GB3)

Let \(K\) be a finite commutative étale \(k\)-group of rank \(d\). We construct its character scheme instead of importing a general Cartier-duality theorem.

Put \(H=\mathcal O(K)\), a \(d\)-dimensional Hopf algebra. Its linear dual \(H^*=\operatorname{Hom}_k(H,k)\) is a Hopf algebra: transpose the multiplication, comultiplication, unit, counit and antipode. The algebra multiplication of \(H^*\) is commutative since the group law of \(K\) is commutative. Define
\[
K^D=\operatorname{Spec}H^*.
\]
For every ordinary \(k\)-algebra \(R\), the finite-dimensional tensor pairing identifies an \(R\)-algebra homomorphism \(H^*\to R\) with an element \(u\in H\otimes R\) satisfying
\[
\Delta u=u\otimes u,\qquad \epsilon(u)=1.
\]
The antipode gives \(u\,S(u)=1\). Thus \(u\) is precisely the invertible function that defines a homomorphism \(K_R\to\mathbb G_{m,R}\). These identifications commute with every \(R\to R'\), and glue on arbitrary schemes. Hence
\[
K^D(T)=\operatorname{Hom}_{T\text{-groups}}(K_T,\mathbb G_{m,T}).
\tag{GB3.1}
\]

Over \(\bar k\), \(K\) is the constant finite abelian group \(F\) of order \(d\), and \(H^*_{\bar k}=\bar k[F]\). Here is a direct proof that this algebra is \(\bar k^d\). In the regular representation of \(\bar k[F]\), multiplication by every element of \(F\) has finite order. Its minimal polynomial divides \(X^m-1\), which has distinct roots in characteristic zero. These operators are therefore diagonalizable, and they commute. Successively splitting into eigenspaces makes them simultaneously diagonal; each eigenspace is invariant under the remaining operators because the operators commute, and their restrictions again have square-free minimal polynomials. The regular representation is faithful because an algebra element acting as zero kills \(1\). Its \(d\)-dimensional algebra therefore embeds into the \(d\)-dimensional algebra of all diagonal endomorphisms of a \(d\)-dimensional space. The embedding is an equality by dimension. Consequently \(H^*_{\bar k}\simeq\bar k^d\).

The algebra \(H^*\) is finite free over \(k\); its relative differentials vanish after the faithful field extension, hence vanish before it. Actual [Smooth algebras over a field and the Jacobian criterion](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md) Theorem 6.2 proves it is finite étale. We have thus proved
\[
K^D\text{ is finite étale of rank }d
\tag{GB3.2}
\]
and its all-family representing property, without assuming any comparison with a Picard component.

#### 4.2.16. Character descent gives the whole rigidified Picard kernel (GB4)

Let \(f:A\to B\) be an isogeny, \(K=\ker f\). GB1 proves that \(f\) is a finite étale fpqc cover. We prove on every ordinary \(T\)
\[
\ker\bigl(f^*:Q_B(T)\to Q_A(T)\bigr)
\simeq \operatorname{Hom}(K_T,\mathbb G_{m,T}).
\tag{GB4.1}
\]
At this point **no assertion about \(D_B\) is used**.

Suppose \(L\) is a rigidified line on \(B_T\) and \(f^*L\) is trivial as a rigidified line. Its normalized trivialization is unique: an automorphism of \(\mathcal O_{A_T}\) is a unit from \(T\), by (GB0.2), and rigidification makes that unit \(1\). Transport the canonical descent isomorphism of \(f^*L\) through this trivialization. Under
\[
A_T\times K_T\simeq A_T\times_{B_T}A_T
\]
it is multiplication by an invertible function \(u\). Since functions on \(A_T\times_T K_T\) come from \(K_T\), again by (GB0.2), it is a unit on \(K_T\). Fix its direction from the first copy of the trivial line to the second: at \((a,h)\), it sends \(v\) to \(u(h)v\). The cocycle identity on \(A_T\times K_T\times K_T\) says
\[
u(h+h')=u(h)u(h'),\qquad u(0)=1.
\]
Thus \(u=\chi\) is a character. Tensor product of lines gives multiplication of characters. This orientation is a convention for this descent isomorphism; it makes no alteration to the connection-cocycle signs of G5.

Conversely, a character \(\chi\) supplies exactly this descent datum on \(\mathcal O_{A_T}\). To see its effectivity on arbitrary ordinary \(T\), cover \(B_T\) by affines. Their inverse images under finite \(f_T\) are affine. On such a pair, write its faithfully flat algebra map \(R\to S\). The actual AG-GS *Quotients and torsors*, lines 13–43, proves module descent: with the displayed cocycle its invariant module \(P\) satisfies
\[
S\otimes_R P\simeq S.
\]
The proof there identifies this tensor product with the kernel of the two descent maps using flatness and the cocycle, and proves descent of every compatible homomorphism. We explain the needed finiteness consequence, including non-Noetherian bases.

First \(P\) is finitely generated. Express a finite set of generators of \(S\otimes P\) as finite sums \(s_i\otimes p_i\); the finitely many \(p_i\) generate \(P\), because the quotient tensors to zero and \(S\) is faithfully flat. Choose a surjection \(R^m\to P\), with kernel \(J\). Flatness of \(S\) identifies \(S\otimes J\) with the kernel of \(S^m\to S\otimes P\simeq S\). That surjection splits over \(S\); its kernel is a finite projective \(S\)-module. The preceding finite-generation argument gives \(J\) finitely generated. Hence \(P\) is finitely presented. It is flat: tensor any injection of \(R\)-modules with \(P\), then with \(S\); the resulting map is injective since \(S\otimes P\simeq S\), and faithful flatness detects the original kernel.

At a prime of \(R\), \(P\) has fibre rank one, since this is so after a faithfully flat extension. Choose one element lifting a basis of that fibre. Nakayama gives a surjection \(R_{\mathfrak p}\to P_{\mathfrak p}\). Its kernel is finitely generated because \(P\) is finitely presented. Flatness makes reduction of this kernel inject into the residue field; the displayed map on the one-dimensional fibres is an isomorphism, so the reduced kernel is zero. Nakayama kills the kernel. Thus \(P_{\mathfrak p}\) is free of rank one. Finite presentation extends this isomorphism to a neighbourhood of the prime. Therefore the descended modules are invertible. Uniqueness of compatible descended homomorphisms glues them to a line on \(B_T\). Restriction of the normalized trivialization at \(0_{A_T}\) supplies its rigidification on \(0_{B_T}\).

These constructions are inverse by the actual full faithfulness of module descent. They commute with **arbitrary**, possibly nonflat, changes \(T'\to T\): the pullback of the descended line has exactly the pulled-back descent datum, so uniqueness identifies it with the line constructed from the pulled-back character. We do not claim that taking the invariant kernel of a module commutes with arbitrary tensoring without this effectivity argument.

Thus (GB4.1) is an isomorphism of all-family group functors, represented by
\[
\ker(f^*:Q_B\to Q_A)\simeq K^D.
\tag{GB4.2}
\]
The scheme kernel here can equally be read as the represented fpqc kernel. Rigidification removes scalar automorphisms; no assertion about higher derived mapping spaces is made.

#### 4.2.17. The entire multiplication kernel lies in the identity component (GB5)

Apply GB4 to \(f=[n]_B\), with \(g=\dim B\). It gives
\[
\ker([n]^*:Q_B\to Q_B)\simeq B[n]^D.
\tag{GB5.1}
\]
On \(D_B\), the same pullback is \([n]_{D_B}\), by the actual normalized identity (GB0.3). Hence the open subgroup inclusion \(D_B\hookrightarrow Q_B\) induces a monomorphism
\[
D_B[n]\longrightarrow B[n]^D.
\tag{GB5.2}
\]
GB2 applied to the already constructed \(D_B\), whose dimension is \(g\) by G2, says its source is finite étale of rank \(n^{2g}\). GB2 applied to \(B\), followed by GB3, says the same about its target. Over \(\bar k\), (GB5.2) is an injection between the point sets of two split finite étale schemes with exactly \(n^{2g}\) points. It is therefore bijective, and the corresponding map of product algebras is an isomorphism. Tensoring with \(\bar k\) is faithfully flat, so the original algebra map is an isomorphism over \(k\). This proves (GB0.1).

This is a comparison of finite schemes with independently computed ranks. It is neither a tangent-dimension argument nor an assumed torsion-free Néron–Severi statement. In particular, it proves the component assertion also for maps from nonreduced schemes into that kernel. The equality survives every \(T\) because it is a scheme isomorphism, or directly because (GB4.1) and (GB0.3) were proved on all \(T\).

#### 4.2.18. A reverse isogeny by explicit morphism descent (GB6)

Let \(f:A\to B\) be any fixed isogeny of degree \(d\), with finite étale kernel \(K\). The morphism \([d]\) kills \(K\). Indeed over \(\bar k\) its points form a finite abelian group \(F\) of order \(d\). For \(h\in F\), translation permutes its elements, so
\[
\sum_{x\in F}x=\sum_{x\in F}(x+h)
=\sum_{x\in F}x+d h.
\]
Thus \(d h=0\). Since \(K_{\bar k}\) is reduced, equality at all its points is equality of morphisms. It descends by faithful field extension. This proves scheme-theoretic vanishing, not merely a statement about \(k\)-rational points.

The map \([d]_A\) is invariant on the relation (GB1.1). We descend it to a morphism \(\psi:B\to A\), spelling out this use of descent rather than presuming arbitrary-scheme effectivity. For an affine open \(U\subset A\), its inverse image \(V'\) under \([d]_A\) is saturated for the \(K\)-relation. Since the finite map \(f\) is closed,
\[
V=B\setminus f(A\setminus V')
\]
is open. All geometric fibres are translates of \(K\), so saturation gives \(f^{-1}(V)=V'\); equality of these opens is checked on geometric points. Cover \(V\) by affines \(W\). The finite inverse image \(f^{-1}(W)\) is affine. Every function pulled back from \(U\) has equal pullbacks along the two projections of the relation, so the actual faithfully flat ring equalizer
\[
\mathcal O(W)=
\{s\in\mathcal O(f^{-1}W):s\otimes1=1\otimes s\}
\]
of AG-GS *Quotients and torsors*, lines 51–59, descends its algebra map. This defines \(W\to U\). Uniqueness glues these maps on overlaps and across the target cover. Consequently
\[
\psi f=[d]_A.
\]
Its homomorphism identity is checked after the fpqc cover \(f\times f\), and its identity value after \(f\), so \(\psi\) is a group homomorphism. Finally
\[
f\psi f=f[d]_A=[d]_B f
\]
and fpqc cancellation give
\[
\psi f=[d]_A,\qquad f\psi=[d]_B.
\tag{GB6.1}
\]
These are morphism identities over \(k\), and remain identities on every ordinary \(T\).

#### 4.2.19. Every character line is in Picard degree zero; dual degrees agree (GB7)

Let \(\chi:K_T\to\mathbb G_{m,T}\) be any character on **any** ordinary \(T\). GB4 constructs its normalized descended line \(L_\chi\) on \(B_T\), with a normalized trivialization of \(f_T^*L_\chi\). Equation (GB6.1) gives
\[
[d]_{B_T}^*L_\chi
=\psi_T^*f_T^*L_\chi
\simeq\mathcal O_{B_T}
\]
as a rigidified line. Thus its class belongs to the **whole** multiplication kernel. GB5 identifies that kernel with \(D_B[d]\). We have proved the precise previously missing assertion:
\[
L_\chi\in D_B(T)\quad
\text{for every ordinary }T\text{ and every character }\chi.
\tag{GB7.1}
\]
No reduction of \(T\), extension of its points, or Néron–Severi assertion is needed. In particular the universal character over \(T=K^D\) gives an actual factorization of its classifying morphism through \(D_B\).

Pullback by \(f\) carries \(D_B\) into \(D_A\): the image of the connected source under the group homomorphism of Picard schemes contains the identity, hence lies in its open identity component. Define \(f^\vee:D_B\to D_A\) by this pullback. Since GB7.1 puts all of GB4's character kernel in \(D_B\), (GB4.2) now restricts to the full all-family equality
\[
\ker f^\vee=K^D
=\underline{\operatorname{Hom}}(\ker f,\mathbb G_m).
\tag{GB7.2}
\]

Dual pullback reverses the identities in (GB6.1). Using (GB0.3) gives
\[
\psi^\vee f^\vee=[d]_{D_B},\qquad
f^\vee\psi^\vee=[d]_{D_A}.
\]
The second equation makes \(f^\vee\) surjective, by GB2. Its kernel is finite by (GB7.2). Every geometric fibre is a translate of that kernel. Its source is proper and its target separated, so the actual proper finite-fibre theorem makes \(f^\vee\) finite; GB1 makes it finite étale. The fibre at the identity has rank \(d\) by GB3, so
\[
\deg(f^\vee)=\operatorname{rank}K^D
=\operatorname{rank}K=\deg f.
\tag{GB7.3}
\]
This proves equality of degrees with the actual character-component assertion and its families, rather than deriving it from a quoted dual-isogeny theorem.

#### 4.2.20. The normalized evaluation isomorphism (GB8)

For an arbitrary abelian \(A\), G2 constructs \(D_A\) and \(D_{D_A}\), and G3 constructs
\[
\kappa_A:A\to D_{D_A}
\]
by evaluation of the normalized Poincaré line. Choose the very ample \(N\) of G2. Its actual homomorphism \(\phi_N:A\to D_A\) has finite kernel and full image. The actual proper finite-fibre proof makes it an isogeny; GB1 supplies finite étaleness. The normalized line comparison of G3 gives, on all ordinary families,
\[
\phi_N=\phi_N^\vee\kappa_A.
\tag{GB8.1}
\]

We can recheck the finite-isogeny assertion for \(\kappa_A\) here without presuming its degree-one conclusion. Its kernel is a closed subgroup of \(\ker\phi_N\), hence finite. Its image is closed by properness, and (GB8.1) makes its image under the finite \(\phi_N^\vee\) all of \(D_A\). The finite-function-field dimension argument implies this image has dimension \(\dim A=\dim D_{D_A}\); since the target is geometrically integral, the image is the entire target. The finite-fibre proof then makes \(\kappa_A\) finite surjective. GB1 makes it finite étale.

Ranks of the finite étale maps here multiply: over a geometric point, the first map has \(s\) reduced points in its fibre, and the next has \(r\) reduced points over each of them; the composite has \(rs\) reduced points. The composite is locally free, also directly because a finite projective module over a finite projective algebra is finite projective over the base (split it as a summand of a finite free module over that algebra). Thus (GB8.1) and (GB7.3), applied to \(\phi_N\), imply
\[
\deg\phi_N=\deg(\phi_N^\vee)\deg\kappa_A,
\qquad
\deg(\phi_N^\vee)=\deg\phi_N,
\qquad
\deg\kappa_A=1.
\tag{GB8.2}
\]
A finite locally free algebra of rank one is the base algebra: its unit map is an isomorphism at every residue field (the unit is nonzero), and Nakayama between rank-one free modules makes it an isomorphism locally. Therefore \(\kappa_A\) is an isomorphism.

We have proved general biduality over every characteristic-zero field:
\[
A\xrightarrow[\ \kappa_A\ ]{\sim}
\operatorname{Pic}^0_{\operatorname{Pic}^0_{A/k}/k}.
\tag{GB8.3}
\]
Its actual normalized universal-line identity remains the one in G3:
\[
(1_{D_A}\times\kappa_A)^*P_{D_A}
\simeq\operatorname{swap}^*P_A.
\tag{GB8.4}
\]
Both rigidifications and all multiplication coherences are the uniquely normalized ones already proved there. They pull back to every ordinary \(T\); no sign choice is introduced by (GB8.2). Consequently the G5 identity affine-function extension class can now be read through the differential of a proved scheme isomorphism. Its signs remain: ordered local connection cocycle \(-c\), degree-one affine-function extension cocycle \(+c\).

#### 4.2.21. Mathematical foundations of biduality and theta

The degree-one evaluation argument proves whole rigidified character descent, character-line membership in \(D_B\) on every ordinary parameter, dual-kernel equality and equality of degrees. GB1 proves finite étaleness in characteristic zero, and GB2 proves the multiplication rank. These arguments use the following mathematical foundations, which are not all proved here.

* G0–G2 use the Hilbert/Picard construction, relative Cartier criteria and coherent proper-family results. Group-scheme projectivity uses regular-local factoriality, affine Cartier complements, line-bundle homotopy and ample field descent. The dimension and smooth local criteria retain their commutative-algebra premises.
* GB2 uses the cube theorem, ample generation and coherent finiteness, coherent filtrations and the Hilbert-polynomial dimension bound. GB1 and GB3 use the separability and étale criteria. Their regular-local, localization and dimension foundations remain required.
* GB2, GB7 and GB8 use Theorem 5.2 of [The theorem on formal functions](../../AG-QC/src/the-theorem-on-formal-functions.md). Its affine, completion and cohomological-dimension premises remain required. GB4 and GB6 use the ring and module descent arguments in [Quotients and torsors](../../AG-GS/src/quotients-and-torsors.md), with their faithfully flat and affine-sheaf foundations.
* The theta proof in §§4.2.22–4.2.29 supplies the curve Euler formula, determinant section and its comparisons, a simple theta point, reducedness, the exact sign and ampleness. It retains represented Picard/symmetric-product geometry, trace duality, perfect proper-cohomology complexes, regular-local and Cohen–Macaulay algebra, and projective dimension and proper finite-fibre foundations.
* The F0–F7 constructions retain derived mapping-space descent and the curve degree equation and scalar-automorphism factor. Ordinary family identities do not alone imply an equivalence of full derived stacks.

The arguments cover all characteristic-zero fields and arbitrary ordinary parameter schemes. For additional reading on reverse isogenies and multiplication degrees, see Milne, [*Abelian Varieties*, §8](https://www.jmilne.org/math/xnotes/AVs.pdf).

#### 4.2.22. The determinant section on the pointed Jacobian

Let \(k\) be a field of characteristic zero, let \(X/k\) be a smooth projective geometrically connected curve, and fix \(x_0\in X(k)\). Put
\[
g=\dim_k H^1(X,\mathcal O_X),\qquad J=\operatorname{Pic}^0(X),\qquad
M=\mathcal O_X((g-1)x_0).
\]
Use the smooth projective geometrically integral Jacobian and normalized universal line \(P\) constructed in §4.2.8, and write
\[
p:X\times J\longrightarrow J,\qquad Q=p_X^*M\otimes P.
\]
Thus \(Q_a=M\otimes P_a\) has degree \(g-1\). All parameter schemes in this construction are ordinary schemes; they need not be reduced or Noetherian.

The prerequisites are the represented rigidified Picard functor, effective descent of lines, the symmetric-product construction, coherent cohomology on a projective curve, and the Noetherian local-algebra results specified below. Section 4.2.8 gives the passage from the geometrically closed Picard construction to every characteristic-zero field. Its recursive representability, scheme-descent and symmetric-product prerequisites remain premises. The argument here constructs the theta section and proves its divisor properties within those foundations.

**Lemma TH.C1 (the curve Euler calculation).** For every line \(L\) on \(X\),
\[
\chi(L)=\deg L+1-g,\qquad \deg\Omega^1_X=2g-2.
\tag{TH.C1}
\]
Moreover, over an algebraically closed extension, a line of negative degree has no nonzero section.

Here is the calculation, including the portion of Riemann–Roch needed below. Smoothness gives regular local rings by [*Smooth algebras over a field and the Jacobian criterion*, Theorem 2.1](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md); its standard-smooth differential presentation makes \(\Omega_X^1\) a line. The one-dimensional regular rings are DVRs by the uniformizer proof of [*Regular local rings*, Solution 7.2](../../AG-CA/src/regular-local-rings.md), with no restriction on their residue fields. Over an algebraic closure these are also the local constructions in §1.1.8.

The two-affine calculation of §1.1.1 gives cohomology only in degrees zero and one. Over \(\bar k\), the finite projection and twist presentations in §§1.1.9–1.1.11 give finite \(H^1\) for every coherent sheaf. A presentation \(0\to K\to Q_0\to F\to0\) on \(\mathbf P^1\), with \(Q_0\) a finite sum of twists, then gives finite \(H^0(F)\): it is an extension of a quotient of finite \(H^0(Q_0)\) by a subspace of finite \(H^1(K)\). Finite direct image transfers this to \(X_{\bar k}\). Section 1.1.12 gives \(H^0(\mathcal O_{X_{\bar k}})=\bar k\). A finite affine-cover complex commutes with extension of the ground field, since that extension is flat. Faithful flatness therefore descends the finiteness assertions and gives \(H^0(X,\mathcal O_X)=k\), and \(\chi(\mathcal O_X)=1-g\).

Choose a nonzero generic section of \(L\). The frame construction in [*Effective Cartier divisors and invertible sheaves*, Theorem 4.1](../../AG-MO/src/effective-cartier-divisors-and-invertible-sheaves.md) writes \(L=\mathcal O_X(A)\). In a DVR each local meromorphic coefficient is a unit times an integral power of its parameter. Only finitely many points have nonzero order: on a finite trivializing cover their zeros and poles form proper closed subsets of the Noetherian curve. Thus \(A=\sum_p n_p p\). For any closed point \(p\), the exact sequence
\[
0\longrightarrow L\longrightarrow L(p)\longrightarrow L(p)|_p
\longrightarrow0
\]
has last term a one-dimensional \(k(p)\)-space. Its higher cohomology vanishes, so
\(\chi(L(p))-\chi(L)=[k(p):k]\). Adding or subtracting the finitely many points proves the first formula. It also proves that the weighted degree is independent of the generic section: a principal divisor gives the trivial line and hence degree zero.

The natural trace pairing proved over the algebraically closed field in §1.1.12, equation (R7.3), is
\[
H^1(X_{\bar k},L)^*
\simeq H^0(X_{\bar k},\Omega^1_X\otimes L^{-1}),
\]
with evaluation given by multiplication and the differential trace. For \(L=\mathcal O_X\) it gives \(h^0(\Omega_X^1)=g\); for \(L=\Omega_X^1\) it gives \(h^1(\Omega_X^1)=1\). The first formula now gives \(\deg\Omega_X^1=2g-2\). The degrees descend by the same Euler calculation. Finally a nonzero regular section has an effective Cartier zero divisor, by the local frame proof of Theorem 2.1 in the same divisor lesson. Its degree is nonnegative. This proves the assertion for a line of negative degree. Thus the needed curve Riemann–Roch formula follows from divisor sequences and the constructed trace pairing.

**Construction TH.C2 (a universal two-term model).** Choose \(n\geq\max(1,g)\) and \(D=nx_0\). The degree of \(Q_a(D)\) is \(g-1+n>2g-2\). Lemma TH.C1 and the trace duality therefore give
\[
H^1(X_K,Q_a(D))=0,\qquad h^0(X_K,Q_a(D))=n
\]
at every geometric point \(a:\operatorname{Spec}K\to J\).

The projective model in [*Base change and the Grothendieck complex*, Lemma 3.1 and Theorem 3.2](../../AG-QC/src/base-change-and-the-grothendieck-complex.md) applies on every affine open of the Noetherian scheme \(J\): \(p\) is projective and \(Q(D)\) is coherent and flat over the base. It supplies a nonnegative finite projective complex computing every algebra base change. To see the consequence of the fibre vanishing, trivialize that complex near a point and split off every invertible differential entry as a contractible pair. This is the actual matrix construction of [*Semicontinuity and Grauert's theorem*, Lemma 2.1](../../AG-QC/src/semicontinuity-and-grauerts-theorem.md). The remaining differentials vanish over the residue field. Each remaining positive-degree term is consequently its fibre cohomology in that degree, and is zero. Those terms have rank zero and vanish on a neighborhood. The remaining degree-zero term is finite locally free of rank \(n\). All the cancellations survive arbitrary tensor product. Thus
\[
E^0=p_*Q(D)
\]
is a vector bundle of rank \(n\), its higher direct images vanish, and these statements commute with every ordinary base change, including a nonflat one.

The divisor \(D\) is finite over \(k\) of length \(n\): its local algebra at \(x_0\) has successive quotients \((u^i)/(u^{i+1})=k\), for \(0\leq i<n\). Hence \(D\times J\to J\) is finite locally free of rank \(n\). The direct image of its line \(Q(D)|_{D\times J}\) is
\[
E^1=p_*\bigl(Q(D)|_{D\times J}\bigr),
\]
also finite locally free of rank \(n\). Indeed an invertible module over a finite locally free algebra is a finite projective module over the base; its fibre dimension is \(n\). Its sections and base changes are ordinary finite-algebra tensor products.

The sequence
\[
0\longrightarrow Q\longrightarrow Q(D)
\longrightarrow Q(D)|_{D\times J}\longrightarrow0
\]
now represents \(Rp_*Q\) by
\[
K_D=[E^0\xrightarrow{\,d_D\,}E^1],
\qquad \deg E^0=0,\quad \deg E^1=1.
\tag{TH.C2}
\]
The comparison is the one induced by this exact sequence and the acyclic terms, and commutes with parameter maps. Define
\[
\mathcal L_\Theta
=\det(E^1)\otimes\det(E^0)^{-1}
=(\det Rp_*Q)^{-1},
\qquad
\theta_D=\det(d_D)\in H^0(J,\mathcal L_\Theta).
\tag{TH.C3}
\]
Here the determinant of a two-term projective complex is, by definition,
\(\det(E^0)\otimes\det(E^1)^{-1}\). The wedge of its equal-rank differential gives the displayed section of the inverse line.

**Lemma TH.C3 (independence and coherence).** The pair \((\mathcal L_\Theta,\theta_D)\) is independent of the sufficiently large effective divisor \(D\), under canonical compatible comparisons.

Suppose \(D'\geq D\) and both twists are acyclic in positive degree. Put \(C=D'-D\) and \(V=p_*(Q(D')|_{C\times J})\). Comparing the two exact sequences above gives a commutative diagram whose rows are
\[
0\longrightarrow E_D^i\longrightarrow E_{D'}^i
\longrightarrow V\longrightarrow0,\qquad i=0,1,
\tag{TH.C4}
\]
and whose differential on the common quotient \(V\) is the identity. For \(i=0\), surjectivity uses \(R^1p_*Q(D)=0\); for \(i=1\), it is the quotient sequence for \(Q(D')/Q\). Every term is locally free, so both rows split locally.

For an exact sequence \(0\to A\to B\to C\to0\), the wedge map
\(\det B\simeq\det A\otimes\det C\) puts a basis of \(A\) first and lifts a basis of \(C\) afterwards. Changing the lifts adds columns from \(A\) and leaves the wedge unchanged. Applying this construction to both rows of (TH.C4) cancels the two factors \(\det V\). In local splittings the differential is block upper triangular with diagonal blocks \(d_D\) and \(1_V\). Its determinant is exactly \(\det(d_D)\). The comparison therefore carries \(\theta_{D'}\) to \(\theta_D\).

For \(D\leq D'\leq D''\), putting the three successive groups of basis vectors in that order proves that these comparisons compose to the direct comparison. Any two admissible divisors have an admissible common upper divisor, for example their sum. Passing to a further common upper divisor and using this composition identity proves independence of that choice and the cocycle identity. This constructs the determinant line and its section without a choice of bases or of splittings.

For every ordinary \(S\to J\), the same two-term complex is obtained by pulling back \(K_D\); its wedge line and determinant section are \((\mathcal L_\Theta,\theta)|_S\). This remains true for nonreduced and non-Noetherian \(S\): on an affine of \(S\) use the arbitrary-algebra comparison of the original finite projective complex on \(J\), and glue its natural comparisons. Thus the section, its zero scheme and the divisor comparisons commute with all such parameter changes. The pullback zero scheme need not be Cartier: if \(S\to J\) factors through its zero scheme, the pulled-back section is zero. The Cartier assertion below concerns \(J\), and remains Cartier under flat pullback.

#### 4.2.23. A nonvanishing point and the irreducible support

Work temporarily over \(\bar k\), and assume \(g\geq1\). Write \(\omega=\Omega^1_{X_{\bar k}}\).

**Lemma TH.C4 (two degree-\(g-1\) lines).** There are lines \(L_-\) and \(L_+\) of degree \(g-1\) with
\[
h^0(L_-)=h^1(L_-)=0,\qquad
h^0(L_+)=h^1(L_+)=1.
\tag{TH.C5}
\]

Choose distinct points \(p_1,\ldots,p_g\) inductively. If the subspace of \(H^0(\omega)\) vanishing at the previously chosen points is nonzero, choose a nonzero form in it. Its zero set is a finite proper closed subset of the integral curve. A point outside that set and outside the previously chosen points makes evaluation nonzero on the subspace. Its kernel has dimension one less, since the target differential fibre is one-dimensional. After \(g\) choices,
\[
H^0\bigl(\omega(-D_g)\bigr)=0,\qquad D_g=p_1+\cdots+p_g.
\tag{TH.C6}
\]
Duality gives \(h^1(\mathcal O(D_g))=0\), and Lemma TH.C1 gives \(h^0(\mathcal O(D_g))=1\). This space is generated by the canonical rational section \(1\), whose zero divisor is \(D_g\).

Choose \(q\) outside that divisor. Evaluation of this section at \(q\) is nonzero, so
\[
L_-=\mathcal O(D_g-q)
\]
has no section. Conversely the canonical section vanishes at \(p_g\), so
\[
L_+=\mathcal O(D_g-p_g)
\]
has exactly one section: its section space embeds in the already one-dimensional space \(H^0(\mathcal O(D_g))\). Both lines have Euler characteristic zero, proving (TH.C5). The corresponding points of \(J_{\bar k}\) are the classes of \(L_\pm\otimes M^{-1}\). No point chosen in this argument is being asserted to be \(k\)-rational.

**Proposition TH.C5 (the effective irreducible divisor).** For \(g\geq1\), the zero scheme \(\Theta=Z(\theta)\) is a nonempty proper effective Cartier divisor on \(J\), with geometrically irreducible support. On every geometric fibre its support is the locus \(h^0(Q_a)>0\).

The complex (TH.C2) has kernel \(H^0(Q_a)\) and cokernel \(H^1(Q_a)\) after passage to a field. The two ranks agree, so its determinant vanishes exactly when that kernel is nonzero. Lemma TH.C4 therefore supplies a nonvanishing point and a vanishing point.

The support over \(\bar k\) is the image of the Abel morphism
\[
a:\operatorname{Sym}^{g-1}X_{\bar k}\longrightarrow J_{\bar k},
\qquad
B\longmapsto[\mathcal O(B)\otimes M^{-1}].
\tag{TH.C7}
\]
A section of a degree-\(g-1\) line gives its effective zero divisor of that degree; conversely the canonical section of an effective divisor gives a section. This proves equality on all geometric points.

The finite symmetric quotient and its universal divisor are constructed in [*Hilbert and Quot schemes*, Theorem 7.1](../../AG-HP/src/hilbert-and-quot-schemes.md); the projective Hilbert construction there makes this symmetric power projective for projective \(X\). Its Abel morphism is the represented-family morphism of [*The Picard functor and the Picard scheme of a curve*, §7 and Proposition 7.1](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md). Thus (TH.C7) is proper and its image is closed.

Its source is irreducible. One can check the product assertion before taking the symmetric quotient: \(X_{\bar k}^r\) is smooth, so its local rings are domains and its irreducible components are disjoint. It is connected by induction using the proper projection \(X_{\bar k}^r\to X_{\bar k}^{r-1}\), whose fibres are geometrically connected. A disconnection upstairs would partition each connected fibre; its two closed images would then be disjoint closed subsets partitioning the connected base, which is impossible. Hence the product is integral, and its surjective finite symmetric quotient is irreducible. For \(r=0\) the source is a point. The image in (TH.C7) is consequently irreducible, and is proper because it misses the point defined by \(L_-\).

Finally \(J\) is integral. A line section nonzero at its generic point has a nonzero local coefficient in every trivializing domain, and that coefficient is a nonzerodivisor. The geometric nonvanishing point proves that \(\theta\) is such a section. Multiplication therefore identifies \(\mathcal L_\Theta^{-1}\) with its invertible zero ideal. This is the local equation proof of [*Effective Cartier divisors and invertible sheaves*, Theorems 1.1 and 2.1](../../AG-MO/src/effective-cartier-divisors-and-invertible-sheaves.md). In particular
\[
\mathcal O_J(\Theta)\simeq\mathcal L_\Theta.
\tag{TH.C8}
\]

#### 4.2.24. The determinant derivative and a simple theta point

**Lemma TH.C6 (the first-order obstruction).** At a geometric point with fibre \(L\), identify the Picard tangent space with \(H^1(\mathcal O_X)\). For \(v\) in that space the induced first-order map
\[
H^0(L)\longrightarrow H^1(L)
\]
of the cohomology complex is \(s\mapsto v\cup s\).

The tangent identification is the transition-cocycle proof of [*The structure of the Picard scheme*, Proposition 2.1 and equation (2.5)](../../AG-HP/src/the-structure-of-the-picard-scheme.md). Explicitly use frames \(e_j=e_i g_{ij}\), and deform them to transitions \(g_{ij}(1+\epsilon v_{ij})\). Products add the \(v_{ij}\), changes of frames add coboundaries, and every class gives a rigidified deformation after normalizing at \(x_0\). This verifies both the existence of the tangent direction and its linear convention.

If \(s=e_i s_i=e_j s_j\), then \(s_i=g_{ij}s_j\). Lift it locally using the same coefficients in the deformed frames. With the ordered differential \(\delta=\text{second}-\text{first}\), their difference on an overlap is
\[
e_i^\epsilon\bigl(g_{ij}(1+\epsilon v_{ij})s_j-s_i\bigr)
=\epsilon e_i^\epsilon v_{ij}s_i.
\]
Thus the connecting class of
\(0\to L\xrightarrow{\epsilon}L_\epsilon\to L\to0\)
is precisely \([v_{ij}s]=v\cup s\). It vanishes exactly when the local lifts can be corrected to glue.

This also identifies the map in (TH.C2). Trivialize the pulled-back vector bundles over the dual numbers and write \(d_\epsilon=d_0+\epsilon d_1\). A cycle \(s\in\ker d_0\), lifted with its original coordinates, has differential \(\epsilon d_1s\). The connecting class of the complex sequence is \([d_1s]\in\operatorname{coker}d_0\). The universal cohomology comparison is induced by the sheaf exact sequence and respects connecting maps, so \([d_1s]=v\cup s\). Changing the lift adds \(d_0t\) and leaves this class unchanged.

**Lemma TH.C7 (the determinant linearization).** If \(h^0(L)=h^1(L)=1\), the first derivative of \(\theta\), under the determinant-line identification
\[
\mathcal L_{\Theta,[L\otimes M^{-1}]}
\simeq H^1(L)\otimes H^0(L)^*,
\]
is the linear map \(v\mapsto(s\mapsto v\cup s)\).

Choose splittings of the source and target of \(d_0\), putting the one-dimensional kernel and cokernel first and the complementary, isomorphically mapped \((n-1)\)-spaces second. Choose compatible bases on those complementary spaces. In these bases,
\[
d_\epsilon=
\begin{pmatrix}
\epsilon\alpha&\epsilon\beta\\
\epsilon\gamma&I+\epsilon B
\end{pmatrix},
\qquad
\det d_\epsilon=\epsilon\alpha.
\tag{TH.C9}
\]
Indeed any determinant term involving both off-diagonal blocks contains \(\epsilon^2\), and the lower diagonal determinant is \(1\) modulo \(\epsilon\). The coefficient \(\alpha\) is exactly the induced map from kernel to cokernel. Cancelling the complementary determinant factors gives the stated line identification. Lemma TH.C6 proves the assertion. An arbitrary choice of frame for \(\mathcal L_\Theta\) changes the scalar derivative by a unit; the intrinsic linear map above records its normalization.

Apply this at the line \(L_+\) of Lemma TH.C4. Choose nonzero
\[
s\in H^0(L_+),\qquad
\omega'\in H^0(\Omega_X^1\otimes L_+^{-1}).
\]
The second space has dimension one by duality. Their product \(s\omega'\) is a nonzero global differential: at the generic point it is a product of two nonzero elements of one-dimensional function-field spaces. Perfect duality for \(\mathcal O_X\) supplies \(v\in H^1(\mathcal O_X)\) with
\[
\operatorname{tr}_X\bigl((s\omega')\cup v\bigr)\ne0.
\]
Naturality of (R7.3) for the morphism \(L_+\xrightarrow{\omega'}\Omega_X^1\), or the componentwise ordered cup calculation in §1.1.16, gives
\[
\bigl\langle v\cup s,\omega'\bigr\rangle
=\operatorname{tr}_X\bigl((s\omega')\cup v\bigr).
\tag{TH.C10}
\]
The differential factor has degree zero in this cohomology pairing, so this multiplication introduces no interchange sign. The right side is nonzero. Lemma TH.C7 therefore proves that \(\theta\) has a nonzero derivative at \([L_+\otimes M^{-1}]\).

#### 4.2.25. Multiplicity one, reducedness and descent

**Proposition TH.C8 (geometric reducedness).** For \(g\geq1\), the effective divisor \(\Theta\) is geometrically reduced and geometrically irreducible, and has multiplicity one along its unique geometric component.

Let \(z=[L_+\otimes M^{-1}]\) over \(\bar k\), and let \(f\) be a local equation for \(\theta\) in
\(A=\mathcal O_{J_{\bar k},z}\), with maximal ideal \(\mathfrak m\). The ring \(A\) is regular local because \(J_{\bar k}\) is smooth; this implication and the rational-point cotangent identification are proved in [*Smooth algebras over a field and the Jacobian criterion*, Theorem 2.1 and Proposition 3.1](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md). A nonzero tangent derivative means
\[
f\in\mathfrak m\setminus\mathfrak m^2.
\]
Extend its linear class to a basis of \(\mathfrak m/\mathfrak m^2\). Nakayama makes the lifts a minimal generating list of \(\mathfrak m\); quotienting by its first member gives a regular local domain of dimension \(g-1\). This is the actual parameter proof of [*Regular local rings*, Theorem 1.1 and Corollary 1.2](../../AG-CA/src/regular-local-rings.md). Thus \(A/(f)\) is a domain.

Let \(\eta\) be the generic point of the irreducible support proved in Proposition TH.C5. It specializes to \(z\). Localizing \(A/(f)\) at its minimal prime gives the local ring \(\mathcal O_{\Theta_{\bar k},\eta}\), which is a field because \(A/(f)\) is a domain. This proves generic reducedness. Equivalently, the ambient ring at \(\eta\) is a one-dimensional regular local ring: the principal ideal theorem bounds its dimension by one, and a nonzero Cartier equation excludes dimension zero. Its DVR equation is a unit times \(\pi^m\). Its quotient being a field forces \(m=1\), which is the asserted multiplicity.

Generic reducedness must now be promoted to reducedness everywhere. The exact algebra required is as follows. At any point \(y\) of the divisor, its local ring has the form \(B=A_y/(f_y)\), where \(A_y\) is Noetherian regular local and \(f_y\) is a nonzero nonunit. [*Regular sequences, depth and Cohen–Macaulay modules*, Theorem 6.1 and Corollary 6.2](../../AG-CA/src/regular-sequences-depth-and-cohen-macaulay-modules.md) prove that \(A_y\) is a domain and Cohen–Macaulay and that its hypersurface quotient \(B\) is Cohen–Macaulay of dimension \(\dim A_y-1\). Their proof uses the polynomial associated graded ring, Krull separation, and the one-equation drops of dimension and depth. Theorem 4.1 in that same lesson proves
\(\operatorname{Ass}(B)=\min\operatorname{Spec}B\), so there are no embedded associated primes.

For completeness, a Noetherian ring with no embedded associated primes and reduced localizations at its minimal primes is reduced. Suppose its nilradical \(N\) is nonzero. A maximal annihilator of a nonzero element of \(N\) is prime: if \(ab\) kills that element and \(b\) does not, the annihilator of its nonzero multiple by \(b\) must be the same maximal annihilator, so \(a\) belongs to it. This is the proof of Lemma 1.1 in [*Associated primes and primary decomposition*](../../AG-CA/src/associated-primes-and-primary-decomposition.md). The resulting prime \(\mathfrak p\) is associated to \(N\), hence to the ambient ring, since an element of a submodule has the same annihilator. It is therefore minimal. The element remains nonzero at \(\mathfrak p\): no denominator outside its annihilator can kill it. But every element of \(N_{\mathfrak p}\) is nilpotent and that localization is reduced, a contradiction.

Apply this argument to each \(B\). Its minimal point is the localization of \(\eta\), where the preceding field calculation gives reducedness. Every local ring of \(\Theta_{\bar k}\) is therefore reduced. Together with its irreducible support, this proves Proposition TH.C8.

The absence of embedded associated primes is essential in this step. For example
\[
\bar k[u,\epsilon]/(\epsilon^2,u\epsilon)
\]
has irreducible support the affine \(u\)-line and becomes reduced after inverting \(u\), yet \(\epsilon\ne0\). Its nonzero class is visible in the vector-space basis \(1,u,u^2,\ldots,\epsilon\), and is killed by the maximal ideal \((u,\epsilon)\). Generic multiplicity one alone would miss that embedded nilpotent. The hypersurface Cohen–Macaulay argument excludes precisely this failure here.

The pair \((\mathcal L_\Theta,\theta)\) was constructed over \(k\), using only \(nx_0\). Its base change is the pair just studied over \(\bar k\). Faithfully flat scalar extension detects vanishing and injectivity of a local equation; it also detects nilpotents, since a local algebra injects into its scalar extension. Hence the effective Cartier divisor is reduced over \(k\), with geometrically irreducible and geometrically reduced support as asserted. Every further field extension has the same conclusion: the algebraically closed argument above applies over an algebraic closure of that extension, and the determinant complex commutes with the extension. The auxiliary points \(p_i,q\) were used only for these geometric checks; they were never required over \(k\).

**The genus-zero case TH.C9.** If \(g=0\), the smooth geometrically connected zero-dimensional Jacobian is a point: over an algebraic closure it has one reduced point, and the identity section identifies it with \(\operatorname{Spec}k\) by faithful flatness. The line \(Q=M=\mathcal O_X(-x_0)\) has degree \(-1\), so \(h^0(Q)=0\); Lemma TH.C1 gives \(h^1(Q)=0\). The two-term model is consequently acyclic and its differential is an isomorphism. Its determinant section is invertible, and \(\Theta\) is the empty effective Cartier divisor on that point.

The construction and reducedness mechanism can be read in this diagram.

\[
\begin{array}{c}
Q=\mathcal O((g-1)x_0)\otimes P\\
\downarrow\quad\text{TH.C1--TH.C2}\\
[E^0\xrightarrow{d}E^1],\quad\operatorname{rank}E^0=\operatorname{rank}E^1=n\\
\downarrow\quad\text{TH.C3--TH.C5}\\
\theta=\det(d),\quad |\Theta|=\operatorname{im}(\operatorname{Sym}^{g-1}X\to J)\\
\downarrow\quad\text{TH.C6--TH.C7}\\
d\theta(v)(s)=v\cup s\ne0\quad\text{at a simple theta point}\\
\downarrow\quad\text{TH.C8}\\
\text{generic multiplicity one + no embedded primes}\ \Longrightarrow\ \Theta\text{ reduced}
\end{array}
\]

*The case \(g\geq1\). The determinant is formed on the Jacobian itself. The nonzero derivative occurs at the explicitly constructed geometric line \(L_+\); Cohen–Macaulay local algebra extends its generic reducedness to the entire divisor.*

The ordinary Picard and symmetric-product foundations retained in §4.2.10, the cohomological derived-section and affine-cover foundations underlying the Grothendieck model and trace, and the Hilbert–Samuel, dimension, Ext and localization prerequisites underlying the stated local-algebra theorems remain their precise recursive premises. The section comparisons, curve Euler calculation, two geometric lines, determinant derivative, multiplicity and reducedness arguments above do not supply those separate foundations.

#### 4.2.26. Translation of the determinant line and the polarization sign

Continue with the pointed curve and Jacobian of G7. Put \(M=\mathcal O_X((g-1)x_0)\), let \(P_X\) be the universal degree-zero line rigidified at \(x_0\), and set \(Q=M\otimes P_X\) on \(X\times J\). For \(g\geq1\), the preceding construction gives the effective reduced irreducible divisor \(\Theta\) with
\[
L=\mathcal O_J(\Theta)=(\det R\pi_*Q)^{-1},
\tag{TH.S1}
\]
where the right side means the inverse of the determinant of the complex \(R\pi_*Q\). The Euler characteristic of every fibre is zero. All determinant comparisons below are comparisons of the actual finite complexes computing arbitrary ordinary base changes.

For a line \(N\) on an abelian variety, rigidify the family
\[
t_a^*N\otimes N^{-1}
\tag{TH.S2}
\]
at the origin. Its represented map is denoted \(\phi_N\). The cube theorem in Abelian varieties, Theorem 4.1, used in G2–G3, proves that \(\phi_N\) is a homomorphism. More explicitly, apply the cube identity to \(N\) in the three variables \(z,a,b\). The four factors depending on \(z\) give
\[
t_{a+b}^*N\otimes N\otimes (t_a^*N)^{-1}\otimes(t_b^*N)^{-1};
\]
the remaining factors form a line pulled back from the parameter pair \((a,b)\). Rigidifying at \(z=0\) cancels that parameter line. The result is the normalized identity
\(\phi_N(a+b)=\phi_N(a)+\phi_N(b)\), on the entire parameter scheme, with its unit and associativity comparisons. The family starts at the neutral line and the parameter abelian variety is geometrically connected, so its map lies in \(\operatorname{Pic}^0\).

We compute \(\phi_L\) by restricting its parameter to \(j:X\to J\). Use \(z\) for the curve coordinate, \(y\) for this parameter, and \(b\) for the Jacobian coordinate. On \(X_z\times X_y\times J_b\), translation \(b\mapsto b+j(y)\) replaces \(Q\), up to a parameter line enforcing its \(x_0\)-frame, by
\[
Q(y-x_0)=Q\otimes\mathcal O(\Gamma_y-X_0).
\]
Here \(\Gamma_y\) is the relative diagonal and \(X_0\) is the fixed \(x_0\)-section. Both are relative Cartier divisors, including where they meet. A parameter line \(B\) changes the determinant of a perfect complex \(K\) by \(B^{\chi(K)}\): in a finite locally free model, its exponent is the alternating sum of the ranks. Since \(\chi(Q_b)=0\), the normalization line makes no change to this determinant.

The two exact sequences with common first term are
\[
0\longrightarrow Q(-x_0)\longrightarrow Q
 \longrightarrow Q|_{X_0}\longrightarrow0,
\]
\[
0\longrightarrow Q(-x_0)\longrightarrow Q(y-x_0)
 \longrightarrow Q(y-x_0)|_{\Gamma_y}\longrightarrow0.
\tag{TH.S3}
\]
Determinants of these sequences cancel the determinant of the common term. Their quotient is
\[
\frac{\det R\pi_*Q(y-x_0)}{\det R\pi_*Q}
 =P_y\otimes K_y,
\quad
P_y=P_X|_{\{y\}\times J},
\tag{TH.S4}
\]
where \(K_y\) is pulled back from \(X_y\). It consists of the \(M\)-fibres and the restriction of \(\mathcal O(\Gamma_y-X_0)\) to the diagonal, divided by the \(x_0\)-fibre. We retain this line rather than treating the diagonal restriction as a chosen scalar. At \(b=0\), \(P_y\) has its neutral rigidification. Normalizing (TH.S4) at \(b=0\) therefore cancels precisely \(K_y\). Taking the inverse determinant in (TH.S1) gives the normalized family \(P_y^{-1}\).

The symmetry and all-family detection in G7 identify \(P_y\), as a line on \(J_b\), with the point \(\lambda_{\mathrm{Abel}}(j(y))\) of \(D_J\). This can also be checked by pulling back along \(j\): both lines become the normalized diagonal correspondence (G7.4); the all-family injectivity of \(j^*\) then identifies them on \(J\). Thus
\[
\phi_L\circ j=-\lambda_{\mathrm{Abel}}\circ j.
\tag{TH.S5}
\]
This is an equality over \(X\), not only on its rational points. It survives every ordinary parameter change.

Both sides extend to homomorphisms on \(J\). Their difference vanishes on \(j(X)\), hence on the sum map \(X^n\to J\). For \(n\geq\max(1,2g-1)\), this sum factors through the finite symmetric quotient and the surjective Abel projective bundle of G7. The quotient's invariant structure-sheaf identity descends the equality to \(X^{(n)}\); faithfully flat descent along the projective bundle descends it to \(J\). Consequently
\[
\boxed{\phi_\Theta=-\lambda_{\mathrm{Abel}}:J\xrightarrow{\sim}D_J.}
\tag{TH.S6}
\]
The minus sign comes from the inverse determinant defining the effective theta line. It changes neither the positive Poincaré kernel nor the connection-action convention in G4–G8.

#### 4.2.27. Degree on an integral projective curve

We need a degree argument on a curve in \(J\), which may be singular. Work first over an algebraically closed field. For an integral projective curve \(C\), define
\[
\deg_C N=\chi(C,N)-\chi(C,\mathcal O_C)
\tag{TH.A1}
\]
for a line \(N\). The coherent finiteness used throughout §4 makes these Euler characteristics finite. Here is the required additivity proof.

Choose a very ample line \(H\) and a nonzero hyperplane section. Its zero divisor is a finite effective Cartier divisor \(E\), and \(H=\mathcal O_C(E)\). For any line \(B\) and any finite effective Cartier divisor \(D\), the exact sequence
\[
0\longrightarrow B\longrightarrow B(D)
 \longrightarrow B(D)|_D\longrightarrow0
\]
gives
\[
\chi(B(D))-\chi(B)=\operatorname{length}(D).
\tag{TH.A2}
\]
The final sheaf has no higher cohomology: it is a finite sum of finite-length modules supported at closed points. Tensoring such a module by a line changes no length.

Ample generation, used already in GB2, supplies a nonzero section of \(N\otimes H^m\) for sufficiently large \(m\). Since \(C\) is integral, this section has a finite effective Cartier zero divisor \(D\); thus \(N=\mathcal O_C(D)\otimes H^{-m}\). Repeatedly use (TH.A2), both forward and backward, to obtain
\[
\chi(B\otimes N)-\chi(B)
 =\operatorname{length}(D)-m\operatorname{length}(E)
 =\deg_C N.
\]
Taking \(B=N'\) proves
\[
\deg_C(N\otimes N')=\deg_C N+\deg_C N'.
\tag{TH.A3}
\]
In particular, \(N^{\otimes2}\simeq\mathcal O_C\) implies \(\deg_C N=0\). A nonzero section of a degree-zero line has no zeros, by (TH.A2). This proof uses no smoothness or normalization of \(C\).

For a line on \(C\times T\) and a connected parameter scheme \(T\) of finite type over the field, the proper flat cohomology-complex calculation used in G7 makes the fibre Euler characteristic locally constant: it is the alternating rank of that complex. Applied to the translates of a fixed line on \(J\), it proves
\[
\deg_C(t_a^*N|_C)=\deg_C(N|_C)
\quad(a\in J).
\tag{TH.A4}
\]
Thus the degree calculation retains the entire connected translation family; it is not an assumption of numerical invariance.

#### 4.2.28. The theta line is ample

**Theorem TH.A.** For \(g\geq1\), the line \(L=\mathcal O_J(\Theta)\) constructed above is ample. Together with (TH.S6), it gives the conventional principal polarization with its exact Abel sign.

**Proof.** First work over \(\bar k\). The homomorphism identity for \(\phi_L\) gives, for every point \(a\),
\[
t_a^*L\otimes t_{-a}^*L\simeq L^{\otimes2}.
\tag{TH.A5}
\]
At a fixed \(a\), choose a frame of the harmless constant line if needed to write this as an unrigidified line isomorphism. Multiply the two translated theta sections. At a point \(z\), choose \(a\) outside the two proper closed subsets
\(\Theta-z\) and \(z-\Theta\). Their union cannot fill the irreducible variety \(J\). The resulting product section of \(L^2\) is nonzero at \(z\). Hence \(L^2\) is globally generated.

Let
\[
f:J\longrightarrow\mathbf P(H^0(J,L^2)^*)
\quad\text{with}\quad f^*\mathcal O(1)=L^2
\tag{TH.A6}
\]
be its complete linear-system map. Suppose a geometric fibre contains an integral projective curve \(C\). Restriction of \(L^2\) to \(C\) is trivial, so (TH.A3) gives \(\deg_C(L|_C)=0\). Equation (TH.A4) makes the same degree zero for every translated theta line.

Write \(\Theta_a=t_a^{-1}(\Theta)\). If \(C\) is not contained in \(\Theta_a\), its defining section restricts to a nonzero section of \(t_a^*L|_C\). That section has degree zero and therefore no zeros. Thus
\[
\Theta_a\cap C\ne\varnothing
\quad\Longrightarrow\quad C\subseteq\Theta_a.
\tag{TH.A7}
\]
For any geometric points \(x,y\in C\), this gives
\(x+a\in\Theta\Longleftrightarrow y+a\in\Theta\) for every \(a\). Consequently
\[
\Theta-x=\Theta-y.
\tag{TH.A8}
\]
The divisor is reduced, so equality of these supports is equality of the effective Cartier divisors on the smooth reduced \(J\). Their associated lines are equal, implying \(\phi_L(x-y)=0\). But (TH.S6) identifies \(\phi_L\) with an isomorphism. Hence \(x=y\), which is impossible for the geometric points of a positive-dimensional integral curve.

Every positive-dimensional projective fibre has such a curve, by successively taking hyperplane sections of a positive-dimensional irreducible component. The projective dimension and Cartier hyperplane arguments used in GB2 apply to this reduced component. It follows that all geometric fibres of \(f\) are zero-dimensional. Theorem 5.2 of [The theorem on formal functions](../../AG-QC/src/the-theorem-on-formal-functions.md), used in GB8, makes \(f\) finite.

The construction descends to \(k\). Finite coherent field base change identifies \(H^0(J,L^2)\otimes_k\bar k\) with the space just used. Surjectivity of the evaluation map descends by faithful flatness, so (TH.A6) is defined over \(k\). Its geometric fibres remain zero-dimensional, and the same proper finite-fibre theorem makes it finite over \(k\).

Finally, we prove ampleness using affine section opens. The standard affine opens of projective space pull back under the finite map \(f\) to affine opens \(J_{s_i}\), where the \(s_i\) are the corresponding sections of \(L^2\). These opens cover \(J\). The affine assertion is the local definition of a finite morphism: over \(\operatorname{Spec}R\), its inverse image is \(\operatorname{Spec}S\) for a finite \(R\)-algebra \(S\).

These section opens give an affine basis after taking further powers. Given a point \(x\) and an open neighbourhood \(U\), choose \(J_{s_i}\) containing \(x\). A principal open \(D(u)\) in this affine scheme contains \(x\) and is contained in \(U\). The denominator-extension argument in Lemma 1.1 of Coherent sheaves on projective schemes: Serre's theorems extends \(u\), after multiplying by \(s_i^r\), to a global section \(t\) of \(L^{2r}\). Multiply once more by \(s_i\). The resulting section \(t s_i\) of \(L^{2(r+1)}\) vanishes off \(J_{s_i}\), and its nonvanishing open there is precisely \(D(u)\). Thus its nonvanishing open is affine, contains \(x\), and lies in \(U\). This is the affine-section definition of ampleness for \(L^2\). The same sections are positive powers of \(L\), so they prove directly that \(L\) is ample. \(\square\)

#### 4.2.29. Genus, families and the Fourier convention

For \(g=1\), \(M=\mathcal O_X\) and the theta divisor is the origin of \(J\). Translation pulls that point back to \(-a\), so
\(t_a^*\mathcal O_J(0)\otimes\mathcal O_J(0)^{-1}\)
represents \(-a\) under positive Abel self-duality. This directly checks the sign in (TH.S6). For \(g=0\), \(J\) and its dual are points. The zero divisor gives the trivial ample line on that point, and the zero homomorphism is the unique isomorphism between these zero groups. No nonempty theta divisor is required.

For a general ordinary parameter scheme \(T\), the determinant line, its section and the comparisons (TH.S3)–(TH.S6) are pulled back as actual lines and morphisms. The finite cohomology complexes and the rigidified Picard interpretation establish their compatibility even for nonreduced or non-Noetherian \(T\). The ampleness assertion concerns this fixed Jacobian over \(k\); it is not an unproved statement about an arbitrary moving singular-curve family.

The positive normalized Poincaré line of G7–G8 is still classified by \(\lambda_{\mathrm{Abel}}\), while the ample theta polarization is \(-\lambda_{\mathrm{Abel}}\). Hence the positive Fourier kernels still compose with inversion, and the downward Hecke convention in §4.8 still uses the inverse class-field line. The theta sign does not authorize changing either convention.

The proof uses the represented Jacobian and its Abel projective bundle from G7, curve duality and Riemann–Roch, the finite perfect proper-cohomology complexes, the cube identity, coherent ample generation and denominator extension, and the projective dimension and proper finite-fibre theorems used in GB2 and GB8. Their explicit recursive algebraic and sheaf foundations remain required. The theta divisor, its ampleness and its sign are established by the displayed argument at those same mathematical foundations.

### 4.3. Algebraic cohomology and vanishing

**Lemma F.2.1.** Using the geometric dimension calculation (G2.1)–(G2.2), relative to its stated earlier foundations,
\[
H^*(A,\mathcal O_A)=\bigwedge^*H^1(A,\mathcal O_A),\qquad
H^*_{\mathrm{dR}}(A)=\bigwedge^*H^1_{\mathrm{dR}}(A).
\tag{F.1}
\]
The degree-one dimensions are \(g\) and \(2g\), respectively.

**Proof.** The derivative of translation trivializes the cotangent bundle:
\(\Omega_A^1=V\otimes\mathcal O_A\), with \(\dim V=g\).
Translation-invariant one-forms are closed, because the formula
\(d\alpha(u,v)=u\alpha(v)-v\alpha(u)-\alpha([u,v])\) is zero for invariant
vector fields on a commutative group. Rigidified first-order line bundles
have transition functions \(1+\varepsilon f_{ij}\), modulo changes
\(1+\varepsilon f_i\). Hence \(T_0\widehat A=H^1(A,\mathcal O_A)\),
and smoothness and dimension in Lemma G give \(h^1(\mathcal O_A)=g\).

The group law and product Čech covers make \(H^*(A,\mathcal O_A)\) a
finite-dimensional connected graded commutative and cocommutative Hopf
algebra. Here Künneth is a calculation: the two finite affine covers give
the tensor product of their complexes over the field; taking cohomology
commutes with this tensor product because every vector-space complex
splits as its cohomology and contractible summands. The unit, group law,
and inversion supply the counit, coproduct, and antipode.

For completeness, such a finite Hopf algebra in characteristic zero is
exterior on its primitive elements. In the convolution algebra of its
endomorphisms set
\(e=\log^\star(\mathrm{id})\), using the augmentation ideal. Each
homogeneous degree uses a finite sum. Cocommutativity and
\(\Delta\mathrm{id}=(\mathrm{id}\otimes1)\star(1\otimes\mathrm{id})\)
show that \(\Delta e=e\otimes1+1\otimes e\). Thus the image of \(e\) is
primitive. Conversely \(\mathrm{id}=\exp^\star(e)\) expresses every
positive-degree element as a sum of products of primitives. The map from
the graded symmetric algebra on the primitive space is injective: a
nonzero homogeneous relation of least degree has zero reduced coproduct,
so is primitive; the primitive polynomials in a graded symmetric algebra
over a characteristic-zero field are its linear generators. This would
contradict inclusion of the primitive space. An even positive-degree
primitive would therefore supply a polynomial subalgebra, contrary to
finite dimension. All primitive generators are odd and their algebra is
exterior.

Degree-one cohomology is primitive. Its \(g\) generators already produce
nonzero degree \(g\), while coherent cohomology vanishes above the
dimension \(g\). Any additional positive-degree primitive would produce
a nonzero product in degree above \(g\). This proves the first identity.

The Hodge-to-de Rham spectral sequence has
\[
E_1^{p,q}=\bigwedge^p V\otimes H^q(A,\mathcal O_A).
\]
For an integer \(n>1\), \([n]^*\) acts as \(n\) on invariant one-forms
and on \(H^1(\mathcal O_A)\), the latter by the primitive coproduct and
iterated addition. It therefore acts by \(n^{p+q}\) on \(E_1^{p,q}\).
Every spectral-sequence differential raises total degree by one and
commutes with \([n]^*\); it is zero since \(n^{p+q}\ne n^{p+q+1}\).
The same argument works on successive pages. Hence
\(\dim H^1_{\mathrm{dR}}(A)=2g\).
The de Rham Čech product gives the same finite Hopf algebra structure.
Applying the preceding primitive argument, now with maximum degree
\(2g\), proves the second identity. No Hodge splitting has been chosen.
\(\square\)

**Lemma F.2.2.** A nontrivial rigidified degree-zero line \(L\) on \(A\)
has \(H^*(A,L)=0\). A nontrivial rigidified degree-zero flat line \(E\)
has \(H^*_{\mathrm{dR}}(A,E)=0\).

**Proof.** For the first assertion, a nonzero section of \(L\) defines
\(0\to\mathcal O_A\to L\to Q\to0\). The normalized Picard family is a
flat projective family on the connected scheme \(\widehat A\).
[Euler characteristics and Hilbert polynomials](../../AG-QC/src/euler-characteristics-and-hilbert-polynomials.md) Theorem 4.2 gives identical ample Hilbert polynomials for
\(L\) and \(\mathcal O_A\). Additivity therefore gives zero Hilbert
polynomial for \(Q\). Theorem 3.1 of that lesson forces \(Q=0\).
Thus a nonzero section would trivialize \(L\), and \(H^0(A,L)=0\).

A nonzero horizontal section of a line with connection is nowhere zero:
if it vanished at a point, the lowest nonzero term of its local Taylor
expansion would have positive degree, whereas the equation
\(ds+\alpha s=0\) has a derivative term of one smaller degree, an
impossibility in characteristic zero. Faithfully flat completion makes
this local argument valid in the local ring. Such a section trivializes
the connection. Hence \(H^0_{\mathrm{dR}}(A,E)=0\) for a nontrivial
flat line.

In either case let \(H\) be the relevant cohomology of the nontrivial
line, and \(H_A\) the cohomology of the unit. Multiplicativity and the
shear automorphism \((a,b)\mapsto(a,a+b)\) give
\[
H\otimes H\simeq H_A\otimes H.
\tag{F.2}
\]
For coherent cohomology use the Poincaré multiplicative identification;
for de Rham cohomology use its flat identification. These are identities
of complexes before taking cohomology, by the same product Čech
calculation as above. If the first nonzero degree of \(H\) were \(r>0\),
the left side would vanish in degree \(r\), while the right side would
have \(H_A^0\otimes H^r=k\otimes H^r\ne0\) there. This is a
contradiction. Thus all degrees vanish. \(\square\)

### 4.4. The universal family gives a Koszul complex, not merely matching dimensions

Let \(p:A\times Y\to Y\) and \(q:A\times Y\to A\). Set
\[
K_{\mathrm{dR}}=Rp_*\operatorname{DR}^{0}_{A\times Y/Y}(\mathcal P).
\]
For the coherent family on \(A\times\widehat A\), write
\(K_{\mathrm{coh}}=Rp_{\widehat A,*}P\).

**Lemma F.3.1 (universal cohomology kernels).**
\[
K_{\mathrm{dR}}\simeq k_{0_Y}[-2g],\qquad
K_{\mathrm{coh}}\simeq
 k_{0_{\widehat A}}\otimes H^g(A,\mathcal O_A)[-g].
\tag{F.3}
\]
Both statements include the length-one scheme structure at the origin.

**Proof.** Properness of the projection and the finite projective
replacement in [Base change and the Grothendieck complex](../../AG-QC/src/base-change-and-the-grothendieck-complex.md) make these bounded perfect complexes. For
the de Rham complex this follows termwise, retaining the
\(\mathcal O_Y\)-linear connection maps between the proper cohomology
complexes. Equivalently, take the bounded relative Čech–de Rham complex:
its terms are flat over the base, and its cohomology is finite by the
bounded spectral sequence of its proper coherent terms. Lemma 3.1 of
[Base change and the Grothendieck complex](../../AG-QC/src/base-change-and-the-grothendieck-complex.md) supplies a finite projective replacement preserving arbitrary
derived base change. Lemma F.2.2 and derived base change show that the
complexes vanish away from the respective origins.

We compute the completed local complex at an origin. In the coherent
case set \(r=g\) and \(W=H^1(A,\mathcal O_A)\); in the de Rham case
set \(r=2g\) and \(W=H^1_{\mathrm{dR}}(A)\). A first-order flat line
has transition functions and connections
\[
1+\varepsilon f_{ij},\qquad d+\varepsilon\alpha_i,
\]
where
\(\alpha_j-\alpha_i=df_{ij}\) and \(d\alpha_i=0\), modulo the changes
of frame \(1+\varepsilon f_i\). This is exactly degree-one Čech–de Rham
cohomology. It proves (G.3), and proves that the Kodaira–Spencer map of
the universal family is the identity \(T_0B\to W\). In the coherent
case the same calculation omits \(\alpha_i\) and gives the identity
\(T_0\widehat A\to W\).

After a basis choice the smooth completed base is
\(R=k[[t_1,\ldots,t_r]]\). Split every unit entry in a finite free
complex into a contractible pair. Its minimal representative has
\(R\otimes\bigwedge^iW\) in degree \(i\), because its derived fibre
is the exterior cohomology in Lemma F.2.1. All differential matrices
lie in \(\mathfrak m\).
The first-order differential is
\[
d_1(\beta)=\sum_{j=1}^r t_j w_j\wedge\beta,
\tag{F.4}
\]
with \(w_j\) dual to the coordinates \(t_j\).
Here is the verification of the map, as opposed to its ranks. Twist a
Čech cocycle by the transition \(1+\varepsilon f_{ij}\), and, in the
flat case, change the connection by \(\varepsilon\alpha_i\).
The obstruction to lifting a cocycle is multiplication by the total
degree-one cocycle \((f_{ij},\alpha_i)\). Thus the connecting map on
cohomology is cup product with the universal first-order class. Lemma
F.2.1 identifies that cup product with exterior multiplication, giving
(F.4).

The linear complex (F.4) is the cochain Koszul complex of the regular
parameters \(t_1,\ldots,t_r\). It has only
\(k\otimes\det W\) in degree \(r\). Higher-order entries in the
minimal differential do not change this conclusion. To see this without
an unsupported formality claim, filter degree \(i\) by
\(\mathfrak m^{a+i}\), putting negative powers equal to \(R\).
The associated graded differential is (F.4). A closed vector in a
degree below \(r\) has a leading homogeneous term which is a Koszul
boundary. Subtract a lift of that boundary; its order strictly increases.
Iterating converges in the complete finite free terms and produces an
actual boundary. In top degree every term of positive order can be
removed in the same way, while a constant top vector is never a
boundary, since the complex is minimal. Hence the completed complex has
exactly the residue field, tensored with \(\det W\), in degree \(r\).
This also rules out a length greater than one or an infinitesimal
thickening of the support.

Completion is faithfully flat on the Noetherian local ring, so the same
cohomology statement holds before completion. Since there is no
cohomology away from the origin, it holds globally.
In the coherent case \(\det W=H^g(A,\mathcal O_A)\).
In the de Rham case the top trace identifies
\(\det W=H^{2g}_{\mathrm{dR}}(A)\) with \(k\). This trace is the
Serre trace on \(H^g(A,\Omega_A^g)\): the Hodge spectral sequence
degenerates as above. It gives the normalized isomorphism in (F.3),
without choosing a volume form. \(\square\)

### 4.5. The second universal kernel

Let \(\delta_0=i_{+,A}k\) be the ordinary left D-module direct image
of the origin of \(A\). Its underlying \(\mathcal O_A\)-module is
infinite-dimensional; it is not the coherent skyscraper \(k_0\).

**Lemma F.4.1 (cohomology of the universal vector extension).**
\[
R\Gamma(Y,\mathcal O_Y)=k.
\tag{F.5}
\]

**Proof.** Because \(\pi\) is affine, put
\(S=\pi_*\mathcal O_Y\). Polynomial degree along the vector fibres
gives an exhaustive filtration \(F_nS\), with
\[
F_0S=\mathcal O_{\widehat A},\qquad
\operatorname{gr}_nS=\operatorname{Sym}^n(V^*)\otimes
                      \mathcal O_{\widehat A}.
\]
Choose local connection sections \(\nabla_i\) with
\(\nabla_j=\nabla_i-c_{ij}\), and define the vector coordinate by
\(\nabla=\nabla_i+z_i\). Then \(z_j=z_i+c_{ij}\).
The affine-function extension therefore has cocycle \(+c_{ij}\),
as in (G5.1)–(G5.3). Its leading polynomial connecting map is
\[
d_1=\sum_i e_i\wedge\frac{\partial}{\partial z_i}
\quad\hbox{on}\quad
\bigwedge^qH^1(\widehat A,\mathcal O)\otimes
\operatorname{Sym}^n(V^*),
\tag{F.6}
\]
where the identity torsor class in Lemma G identifies \(e_i\) with
the basis of \(V^*\). This formula follows by expanding
\(f(z+c)-f(z)\) to its term of polynomial degree \(n-1\).
It determines the differential, including its multiplicities, rather
than treating the graded sheaf as a split algebra.

For fixed \(N=n+q\), put
\(h=\sum_i z_i\iota_{e_i}\). Direct application to a monomial form
gives
\(d_1h+hd_1=N\,\mathrm{id}\). Thus every positive-weight complex is
contractible, since \(N\) is invertible in characteristic zero. Only the
weight-zero copy of \(k\) survives.
There is no hidden convergence assumption. On a finite affine Čech
cover, split the vector-space complex for \(\mathcal O_{\widehat A}\)
into its cohomology and contractible summands. Local torsor
trivializations identify the associated graded Čech complex with this
complex tensored with polynomials. The perturbation terms in the actual
transition maps strictly lower polynomial degree, so the homotopy
transfer series on any polynomial is finite. The transferred
differential on \(H^*(\widehat A,\mathcal O)\otimes\operatorname{Sym}(V^*)\)
has leading part (F.6); every further term lowers \(n+q\) strictly.
The contracting homotopy \(N^{-1}h\) preserves \(n+q\). Its
perturbation series therefore terminates on every vector of finite
total weight. This contracts all the positive weights onto the
weight-zero term, proving (F.5) for the polynomial algebra itself,
rather than just for a completed algebra. The surviving map is the
unit \(k\to R\Gamma(Y,\mathcal O_Y)\). \(\square\)

**Lemma F.4.2 (point support for all D-modules).** If a quasicoherent
left D-module complex \(Q\) on a smooth \(g\)-dimensional scheme is
set-theoretically supported at a smooth point \(i\), there is a complex
of vector spaces \(U\) such that
\[
Q=i_+U,
\qquad Li^*(Q_{\mathcal O})=U[g].
\tag{F.7}
\]
The assertion applies to arbitrary quasicoherent complexes, without a
holonomicity or coherence restriction.

**Proof.** Choose étale parameters \(x_1,\ldots,x_g\) at the point.
On a point-supported module, each \(x_i\) is locally nilpotent: each
individual section generates a finite structure-sheaf submodule with
support at the point. For one parameter put
\[
e(m)=\sum_{j\ge0}\frac{\partial^jx^j m}{j!}.
\]
Every sum on a given vector is finite. The relation
\(x\partial^j=\partial^jx-j\partial^{j-1}\) gives \(xe(m)=0\), and
\(e\) is the identity on \(\ker x\). Also
\[
m=\sum_{j\ge0}\frac{(-1)^j}{j!}\partial^j e(x^j m).
\tag{F.8}
\]
For independence, apply the largest power of \(x\) appearing to a
relation among the \(\partial^ju\): it gives a nonzero factorial times
its highest coefficient. Thus the module is freely generated in normal
derivatives by \(\ker x\). Repeat in the commuting parameters. This
gives \(k[\partial_1,\ldots,\partial_g]\otimes U\), with the density
factor \(\det T_i\) prescribed by the left transfer module. Functions
act by their finite Taylor expansion; hence the argument works in étale
coordinates and glues intrinsically as \(i_+U\).
The projectors show that the kernel-space functor is exact on these
ordinary point-supported modules. Here is the additional argument for
an arbitrary unbounded D-module complex whose cohomology is
point-supported. Put \(\Delta=D/(Dx_1+\cdots+Dx_g)\), retaining its
transfer density. The Koszul complex of right multiplication by the
\(x_i\) on free left \(D\)-modules is a finite free resolution of
\(\Delta\). The normal-order basis identifies its associated graded
with the ordinary regular-parameter Koszul resolution, so it is exact.
Thus \(R\operatorname{Hom}_D(\Delta,Q)\) is the finite cochain Koszul
complex of the \(x_i\)-actions on \(Q\).

For an ordinary point-supported module the normal-derivative
description above makes each \(x_i\) a negative polynomial
derivative. Its Koszul cohomology is the joint kernel in degree zero
and is zero in positive degrees, by successive polynomial integration.
The finite-column spectral sequence for the same Koszul complex on an
unbounded \(Q\) therefore has only this column and gives
\[
H^jR\operatorname{Hom}_D(\Delta,Q)
 =\bigcap_i\ker(x_i:H^j(Q)\longrightarrow H^j(Q)).
\]
The sequence converges without a boundedness restriction because the
Koszul direction has only \(g+1\) columns.

Set \(U=R\operatorname{Hom}_D(\Delta,Q)\), with the inverse density
identification. The evaluation counit
\(\Delta\otimes_k U\to Q\) is an isomorphism on every cohomology
module by the explicit ordinary formula above; hence it is a
quasi-isomorphism. Conversely the corresponding unit is a
quasi-isomorphism on every complex of vector spaces, by the same
finite Koszul calculation. This proves the derived equivalence,
including derived morphism complexes. The coordinate changes give
the intrinsic point transfer \(i_+\), so the construction glues.

The Koszul complex for \(Li^*\) has differential given by the
\(x_i=-\partial/\partial\partial_i\) actions. In characteristic zero
these derivatives are surjective and their joint kernel consists of
constants. Its only cohomology is in Koszul degree \(-g\). The factors
\(\det T_i\) from the transfer and \(\det T_i^*\) from the Koszul
resolution cancel. This is exactly \(U[g]\), proving (F.7).
\(\square\)

**Lemma F.4.3 (the universal D-module kernel).**
\[
Rq_*(\mathcal P,\nabla_A)=\delta_0[-g].
\tag{F.9}
\]
The pushforward here is the ordinary sheaf pushforward along the
spectral variable, with its remaining \(A\)-connection. It does not
perform de Rham integration along \(Y\).

**Proof.** Forget the connection and factor through \(\pi\). Its
underlying complex is the coherent integral transform on
\(\widehat A\times A\) applied to \(S=\pi_*\mathcal O_Y\).
Each \(F_nS\) is obtained by finitely many extensions of copies of
\(\mathcal O_{\widehat A}\). Apply the coherent identity in (F.3) with
\(\widehat A\) as the abelian variety and (G.1) as its duality.
Each such transform is supported at the origin of \(A\). Ordinary
quasicoherent pushforward commutes with the union \(S=\operatorname{colim}
F_nS\), as follows directly from its finite affine Čech model.
Consequently the entire underlying complex is supported there.

Derived pullback to that origin gives
\[
Li^*Rq_*\mathcal P=R\Gamma(Y,\mathcal O_Y)=k.
\tag{F.10}
\]
This base-change calculation also needs no properness for \(q\): cover
\(Y\) by finitely many affines. Their products with an affine chart of
\(A\) are affine over that chart; the line \(\mathcal P\) is flat
over \(A\), and the resulting bounded Čech complex tensors to the
special-fibre complex. Lemma F.4.1 gives its value.
Lemma F.4.2 now writes the connection complex as \(i_+U\); (F.10)
gives \(U[g]=k\), so \(U=k[-g]\). This proves (F.9), including its
D-module structure and shift. \(\square\)

### 4.6. The two composition calculations

Define functors on arbitrary quasicoherent complexes by
\[
F_0(M)=Rp_*\operatorname{DR}^{0}_{A\times Y/Y}
             (\mathcal P\otimes q^*M),
\qquad
\Psi(N)=Rq_*(\mathcal P\otimes p^*N).
\tag{F.11}
\]
The pullback of a D-module in the first formula is the ordinary
connection pullback, rather than dimension-shifted exceptional pullback.
The second formula retains the connection along \(A\). These formulas
are functors of DG categories, obtained from complexes and derived
tensor products; they retain maps and their homotopy coherences.

**Proposition F.5.1.** Assuming Lemma G,
\[
F_0\Psi=\operatorname{inv}_Y^*[-2g],\qquad
\Psi F_0=\operatorname{inv}_A^*[-2g].
\tag{F.12}
\]

**Proof.** On \(A\times Y_b\times Y_c\), multiplicativity gives
\(\mathcal P_b\otimes\mathcal P_c=\mathcal P_{b+c}\).
After integration along \(A\), Lemma F.3.1 makes the coherent
composition kernel
\[
(\operatorname{add}_Y)^*k_{0_Y}[-2g].
\]
Addition is smooth, so this is the structure sheaf of the graph
\(c=-b\), with its stated shift, rather than an underived fibre
calculation. Restrict \(p_c^*N\) to that graph and push to \(b\);
its projection is an isomorphism. The result is
\(\operatorname{inv}_Y^*N[-2g]\), proving the first formula.

For the other composition use \(A_a\times Y\times A_b\).
Multiplicativity in \(A\) gives
\(\mathcal P_a\otimes\mathcal P_b=\mathcal P_{a+b}\).
Ordinary pushforward along \(Y\), by Lemma F.4.3, gives
\[
(\operatorname{add}_A)^*\delta_0[-g]
\tag{F.13}
\]
as a relative left D-module. This is the delta module along the
antidiagonal with the ordinary connection pullback convention.
Tensoring with \(M_a\) is its closed-embedding transfer applied to the
restriction of \(M_a\) to that graph. To verify this for arbitrary
modules, filter the normal-derivative transfer by order: its graded
pieces are \(\mathcal O_{\mathrm{graph}}\otimes\operatorname{Sym}^nN\).
The graph projects isomorphically to the input \(A_a\), so these
pieces, and the exhaustive transfer, are flat over that input. Thus
no uncomputed derived tensor term occurs. The connection actions are
exactly the chain-rule actions in the transfer module.

Standard D-module pushforward of this graph transfer along \(a\)
is \(\operatorname{inv}_A^*M\), because the composite of the graph
embedding and the output projection is inversion. This transfer
composition, with its proof by Spencer resolutions, is [Direct images and the relative de Rham complex](../../GL-DMOD/src/direct-images-and-the-relative-de-rham-complex.md)
Theorem 4.1. That theorem's standard projection pushforward is
\(Rp_*\operatorname{DR}^0[g]\), as its Theorem 2.1 proves. We use
\(Rp_*\operatorname{DR}^0\) here, so the result is
\(\operatorname{inv}_A^*M[-g]\). Locally the same shift is visible
in the cochain Koszul complex of the normal derivative variables:
its coefficient quotient is in degree \(g\); the top-form and
normal-transfer densities cancel. Combined with the \([-g]\) already
in (F.13), this gives the second formula in (F.12).

All exchanges of integrations in this argument can be checked with
finite Čech covers, finite relative Spencer complexes, and K-flat
resolutions. There is a bounded finite number of integration degrees.
Consequently no unbounded product totalization or holonomicity
assumption enters. The group-law identities of the universal line are
identities of kernels, so the resulting isomorphisms are natural on all
objects, not only on geometric flat lines. \(\square\)

### 4.7. The precise normalization and presentable scope

**Theorem F.6.1 (subject to closure of Lemma G).** The unshifted
universal-line functor
\[
\Psi:\operatorname{QCoh}(Y)\longrightarrow\operatorname{Dmod}(A)
\]
is an equivalence of stable presentable DG categories, with inverse
\[
\Phi_+(M)=\operatorname{inv}_Y^*F_0(M)[2g].
\tag{F.14}
\]
For the degree-zero skyscraper \(k_e\) at a flat line \(e\),
\[
\Psi(k_e)=\mathcal P_e,\qquad \Phi_+(\mathcal P_e)=k_e.
\tag{F.15}
\]

**Proof.** Inversion on \(A\) or \(Y\) dualizes the universal line.
It follows by a change of variables that
\(\Psi\operatorname{inv}_Y^*=\operatorname{inv}_A^*\Psi\).
Both compositions in (F.12) therefore make (F.14) a two-sided inverse
of \(\Psi\). This proves full faithfulness and essential surjectivity
on the stated DG categories.
For \(k_e\), the support of the inverse kernel is \(A\times\{e\}\),
and its projection to \(A\) is the identity. Its tensor restriction is
the flat line \(\mathcal P_e\). This proves the first equality in
(F.15), and the two-sided inverse proves the second.

The functors are continuous. Pullbacks and tensor products preserve
colimits. The projection pushforwards are computed locally by finite
affine Čech covers; the relative de Rham complex has finitely many
terms. Sections on an affine commute with sums and filtered colimits
of quasicoherent modules. Thus these computations commute with direct
sums. They are exact functors between stable categories and therefore
preserve arbitrary colimits: coproducts and geometric realizations
generate them, and a realization is a colimit of finite skeleta.
The constructions consequently establish a presentable equivalence
directly. We have not inferred it from a bounded coherent theorem,
from a list of point objects, or from a claimed generating family of
rank-one connections.
\(\square\)

For comparison, Laumon's relative de Rham complex in §3.1 is in degrees
\(-g,\ldots,0\). In that convention \(F_{\mathrm L}=F_0[g]\), and
(F.12) says that its positive-kernel compositions are inversion followed
by \([-g]\). Formula (F.14) is the further normalization required by
this lesson's degree-zero point-image convention. This convention check
can be consulted in the freely readable [Laumon preprint, §§3.1–3.2](https://arxiv.org/html/alg-geom/9603004); the proof above supplies the kernel arguments itself.

### 4.8. Integration into the downward Hecke convention

For the Jacobian \(A=J\), use the identification of \(Y\) with
rigidified flat lines on \(X\) proved in (G8.1)–(G8.2), together with the §1 derived factors and the class-field construction in [Geometric class field theory](geometric-class-field-theory.md). With its positive Abel
line \(C_E^0\), that identification means
\(\mathcal P_e=C_E^0\). The downward line is
\(A_E^0=C_{E^{-1}}^0\). Multiplicativity therefore gives
\[
\operatorname{inv}_J^*A_E^0=C_E^0,
\qquad
\Phi_{\mathrm{down}}=\Phi_+\operatorname{inv}_J^*,
\qquad
\Phi_{\mathrm{down}}(A_E^0)=k_e.
\tag{F.16}
\]
The inversion in the last formula has a Poincaré sign purpose. The
\([2g]\) in (F.14) has a separate cohomological purpose. Neither can
be removed by saying that a point-to-line restriction is formal.

For translation \(t_a\) on \(J\), the identity
\(\mathcal P_{y+a,e}=\mathcal P_{y,e}\otimes\mathcal P_{a,e}\)
and the change of variables \(z=y+a\) in the explicit \(F_0\) formula
give
\[
F_0(t_a^*M)=F_0(M)\otimes\mathcal P_a^{-1}.
\tag{F.17}
\]
Spectral inversion in (F.14) turns that factor into
\(\mathcal P_a\). Hence the point-image normalization has the rule
\[
\boxed{\ \Phi_+(t_a^*M)=\Phi_+(M)\otimes\mathcal P_a\ }.
\tag{F.18}
\]
Under automorphic inversion,
the downward pullback translation \(a=-m j(x)\) becomes
\(+m j(x)\); (F.18) gives the rigidified spectral fibre
\((E_x\otimes E_{x_0}^{-1})^{\otimes m}\). Combining its scalar
weight line \(E_{x_0}^{\otimes m}\), from the degree/weight calculation,
gives \(E_x^{\otimes m}\). This is a kernel identity on all objects;
the unit and tensor coherences follow from the universal multiplicative
line identities.

For the elliptic exercise, (F.3) in the coherent case gives
\(k_0\otimes H^1(J,\mathcal O_J)[-1]\) canonically. A chosen
nonzero identification of the one-dimensional space
\(H^1(J,\mathcal O_J)\) with \(k\) yields the customary
\(k_0[-1]\). In the de Rham case its canonical top trace eliminates
the determinant line, and (F.14) gives
\(\Phi_+(\mathcal O_J,d)=k_{e_0}\) in degree zero.

The positive Fourier equivalence in the preceding conditional theorem is the factor denoted \(\Phi_+\) in the rest of the lesson:
\[
\Phi_+:\operatorname{Dmod}(J)\xrightarrow{\sim}\operatorname{QCoh}(J^\natural).
\tag{4.1}
\]
Its raw de Rham complex has degrees \(0,\ldots,g\); the explicit inverse calculation requires the spectral inversion and \([2g]\) in (F.14). With [Geometric class field theory](geometric-class-field-theory.md)'s downward eigenline, the full automorphic convention is
\[
\Phi_{\mathrm{down}}=\Phi_+\operatorname{inv}_J^*,
\qquad\Phi_{\mathrm{down}}(A_E^0)=k_e.
\tag{4.2}
\]
The two inversions have different roles: spectral inversion and the shift normalize the positive two-kernel inverse, while automorphic inversion corrects the downward Hecke sign. Both have been checked as kernel identities above.

For the full bundle stack, the positive universal-line transform pairs component \(d\) with spectral weight \(-d\): a weight-\(w\) line pairs with the universal \(C_E^d\), of scalar weight \(d\), when \(w+d=0\). Automorphic inversion reverses \(d\), so the downward normalization gives weight \(d\), as in Proposition 2.1. On the stabilizer homology, inversion sends \(\epsilon\) to \(-\epsilon\) and preserves the free and augmentation objects up to their corresponding identifications.

Human credit for this Fourier construction belongs to the free author editions of [Laumon, *Transformation de Fourier généralisée*](https://arxiv.org/abs/alg-geom/9603004) and [Rothstein, *Sheaves with connection on abelian varieties*, v1](https://arxiv.org/abs/alg-geom/9602023v1). The kernel proof is given above; Lemma G retains its explicit recursive geometric foundations, and the earlier categorical and cohomological foundations remain required.

## 5. The equivalence, Hecke action and the meaning of a point

**Theorem 5.1 (conditional on the remaining foundations).** Given the geometric splitting (1.4), the geometric Lemma G, the earlier categorical descent/base-change foundations of §3 and the conditional Fourier proof of §4, the three factor equivalences give
\[
\mathbb L_{\mathbb G_m}:
\operatorname{Dmod}(\operatorname{Bun}_{\mathbb G_m})
\xrightarrow{\sim}
\operatorname{QCoh}(\operatorname{LocSys}_{\mathbb G_m}(X)).
                                                               \tag{5.1}
\]
It admits the downward Hecke normalization in which weight \(m\) acts spectrally by tensoring with the \(m\)-th power of the universal local-system fibre at the modification point.

**Proof.** [Sheaves and D-modules on Bun_G](sheaves-and-d-modules-on-bun-g.md)'s coefficient-monad and degree decomposition give
\[
\operatorname{Dmod}(\operatorname{Bun}_{\mathbb G_m})
 \simeq
\operatorname{Dmod}(J)\otimes\operatorname{Mod}_B
          \otimes\prod_{d\in\mathbb Z}\operatorname{Vect}_k .
                                                               \tag{5.2}
\]
For clarity, the \(B\)-module calculation can be made with coefficients in \(\operatorname{Dmod}(J)\): the atlas of \(J\times B\mathbb G_m\) has self-fibre \(J\times\mathbb G_m\), and the same monad is \(B\otimes-\) on those coefficients. Its bar argument gives the first two factors. Disjoint-degree descent gives the product factor.

On the spectral side, the affine \(Z_{\mathrm{der}}\) factor supplies \(B\)-modules with coefficients in \(\operatorname{QCoh}(J^\natural)\). Descent along the \(B\mathbb G_m\) atlas decomposes them by integer weight, with no finite-support condition. Hence (1.4) gives
\[
\operatorname{QCoh}(\operatorname{LocSys}_{\mathbb G_m}(X))
 \simeq
\operatorname{QCoh}(J^\natural)\otimes\operatorname{Mod}_B
          \otimes\prod_{d\in\mathbb Z}\operatorname{Vect}_k.
                                                               \tag{5.3}
\]
The tensor-factor description is valid on quasicoherent charts and glues by descent. Apply (4.2), (3.1) with the inversion convention, and (2.1) to (5.2). They identify it with (5.3), proving the equivalence.

Here is the Hecke comparison, including its sign. Write
\[
j(x)=\mathcal O_X(x-x_0)\in J.
\]
At a fixed \(x\), the input to weight \(m\) has degree \(d-m\), and its Jacobian coordinate is translated by \(-m j(x)\). The universal multiplicative line in (4.1) identifies pullback by this translation, after the inversion in (4.2), with tensoring by the rigidified spectral fibre
\((E_x\otimes E_{x_0}^{-1})^{\otimes m}\).
This follows from its multiplication identity: at a spectral parameter \(E\), translation of \(C_E\) multiplies it by the fibre of \(C_E\) at the translating point. The same identity is an identity of the universal kernel, so it intertwines the functors on all objects, rather than only comparing rank-one eigenvectors.

The degree shift \(d-m\) is tensoring with spectral weight \(m\), by (2.2). That weight is the scalar line \(E_{x_0}^{\otimes m}\) from the spectral \(B\mathbb G_m\) factor. Multiplying the two lines gives \(E_x^{\otimes m}\). The local derived \(B\)-factor is unchanged by this representation-labelled Hecke operation. This proves fixed-point Hecke compatibility. The universal multiplication, unit and symmetry provide the same tensor and collision coherences as in [Hecke functors and Hecke eigensheaves](hecke-functors-and-hecke-eigensheaves.md). The moving version includes its declared \(X\)-dualizing factor. \(\square\)

The phrase “the skyscraper at \(E\)” requires an actual map. A flat line with a choice of its fibre trivialization determines a point
\[
s_E:\operatorname{Spec}k\longrightarrow
       J^\natural\times Z_{\mathrm{der}}\times B\mathbb G_m .
\]
Put \(\delta_E=(s_E)_*k\). Changing that trivialization gives an isomorphic map and the corresponding isomorphic object. The \(Z_{\mathrm{der}}\) part of \(\delta_E\) is the augmentation \(k\). The atlas pushforward \(\operatorname{Spec}k\to B\mathbb G_m\) is the regular representation
\[
k[z,z^{-1}]=\bigoplus_{d\in\mathbb Z}k(d).
                                                               \tag{5.4}
\]
Indeed that pushforward is coinduction from vector spaces, and its comodule is the Laurent-coordinate coalgebra; each power \(z^d\) is a weight line.

Consequently
\[
\delta_E\simeq k_e\boxtimes k_B
                       \boxtimes\bigoplus_{d\in\mathbb Z}k(d),
\qquad
\mathbb L_{\mathbb G_m}(q^*A_E)\simeq\delta_E,
                                                               \tag{5.5}
\]
with the fibre trivialization used to identify \(A_E^d\) with its degree-zero factor. Before choosing a basis, the constant degree lines are \(E_{x_0}^{-d}\), as in [Geometric class field theory](geometric-class-field-theory.md); the chosen frame identifies them with the lines in (5.4). Their coherent Hecke structure is retained by the universal kernel.

There is a different object: push the trivial line on the residual gerbe
\[
i_E:B\mathbb G_m\hookrightarrow
       J^\natural\times Z_{\mathrm{der}}\times B\mathbb G_m.
\]
Its image is \(k_e\boxtimes k_B\boxtimes k(0)\), with only weight zero. Under (5.1) it is supported only in bundle degree zero. It cannot be the all-degree strong eigenobject, because a nonzero weight-one Hecke translation moves that support. Thus (5.5) uses the framed point pushforward, not an unspecified trivial sheaf on the residual gerbe.

The full \(\delta_E\) is not compact: its augmentation factor is not perfect and its weight support is infinite. Nor is it coherent on the full product stack, because its underlying regular representation is infinite-dimensional. A skyscraper on the smooth rigidified scheme \(J^\natural\) is coherent and perfect; the full stack point has additional behaviour. These distinctions do not contradict the equivalence.

For a torus \(T\), choose a basis of its cocharacter lattice, giving \(T\simeq\mathbb G_m^r\). Both its bundle stack and its local-system stack are the corresponding products. Tensor the rank-one equivalences to obtain
\[
\operatorname{Dmod}(\operatorname{Bun}_T)
 \simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check T}(X)).
                                                               \tag{5.6}
\]
A character-labelled operation is a product of the rank-one operations, so the proof gives its Hecke and tensor compatibilities. This proves the torus deduction conditional on the same remaining geometric and categorical foundations. The basis-independent canonical normalization is given by the Poincaré pairing of the dual lattices; changing basis acts by the inverse dual matrix on the spectral lattice, leaving the pairing invariant. The enhanced Poincaré construction in GLC I §1.5 is the canonical version of this description.

Finally the invariant-zero-fibre nilpotent scheme of a torus is the origin: its coadjoint action is trivial and all linear coordinates are invariant. In the derived local-system model of §1, the spectral global nilpotent cone is therefore the zero section. Sections 5.1.1–5.1.8 prove the categorical comparison below, including its arbitrary-rank exterior algebra, smooth factor and scalar automorphism stack:
\[
\operatorname{IndCoh}_{\operatorname{Nilp}}
       (\operatorname{LocSys}_{\check T})
 \simeq\operatorname{QCoh}(\operatorname{LocSys}_{\check T}).
                                                               \tag{5.7}
\]
This is a spectral statement; it does not assert that every automorphic D-module on a positive-dimensional Picard scheme is a flat connection. The Fourier transform includes arbitrary D-modules.


### 5.1. Zero singular support on the full torus stack

#### 5.1.1. Exterior generators and the actual central operators

Let \(k\) have characteristic zero and let \(R\) be a smooth finite-type commutative \(k\)-algebra. The zero ring gives zero module categories and satisfies every assertion vacuously; assume \(R\ne0\) for the calculations. Fix
\[
B=R[\epsilon_1,\ldots,\epsilon_r]
=\Lambda_R(R^r),\qquad |\epsilon_i|=-1,\quad d_B=0,
\qquad
S=R[u_1,\ldots,u_r],\quad |u_i|=2,\quad d_S=0.
\]
All module categories below contain arbitrary unbounded DG modules. Write \(\operatorname{Coh}_B\) for the full DG category of modules with bounded, finite \(R\)-module cohomology, and set
\[
\mathcal C_B=\operatorname{Ind}(\operatorname{Coh}_B).
\]
Thus \(\operatorname{IndCoh}\) means this specified Ind-category. We use the usual stable DG module foundations: localization at quasi-isomorphisms, the connective-module cohomological truncations, derived tensor–Hom, idempotent completion, and the DG Ind-construction with its mapping formula. These constructions are categorical prerequisites. The free resolutions, generation, equivalence and support calculations needed here are proved below.

The one-generator resolution already used in [*The GL_1 case as an equivalence of categories*, Proposition 3.2](the-gl-1-case-as-an-equivalence-of-categories.md) is the starting point. We give the complete tensor calculation, including its DG algebra and diagonal maps.

**Lemma ZS.A1 (a semifree augmentation resolution).** For \(\alpha=(\alpha_1,\ldots,\alpha_r)\in\mathbf N^r\), let \(e_\alpha\) have degree \(-2|\alpha|\). Put
\[
P=\bigoplus_{\alpha\in\mathbf N^r}Be_\alpha,\qquad
d(e_\alpha)=\sum_{\alpha_i>0}\epsilon_i e_{\alpha-\mathbf e_i},
\qquad
q(e_0)=1,\quad q(e_\alpha)=0\ \ (\alpha\ne0).
\tag{ZS.A1}
\]
Here \(q:P\to R\) uses the augmentation \(B\to R\). For homogeneous \(b\),
\(d(be_\alpha)=(-1)^{|b|}b\,d(e_\alpha)\). The two terms for \(i\ne j\) in \(d^2\) cancel by \(\epsilon_i\epsilon_j=-\epsilon_j\epsilon_i\), and the repeated-index terms vanish. Hence \(P\) is a complex.

For one generator its underlying \(R\)-complex is the direct sum of \(Re_0\) and the pairs
\[
Re_j\xrightarrow{\;1\;}R\epsilon e_{j-1},\qquad j\geq1.
\]
The degree-\(-1\) contraction sends \(\epsilon e_j\) to \(e_{j+1}\) and all \(e_j\) to zero. It contracts the augmentation kernel. The displayed \(r\)-generator complex is the tensor product over \(R\) of these \(r\) resolutions, with the tensor differential signs. Tensoring the contractions gives a contraction onto \(R\): for deformation retractions of two factors, use \(h_1\otimes1+(i_1q_1)\otimes h_2\), with the graded tensor sign. Induction proves that \(q\) is a quasi-isomorphism.

Filtering by \(|\alpha|\) makes \(P\) semifree, since each differential uses only earlier cells. It computes derived Hom into every unbounded target. Indeed, for an acyclic target \(N\), a cycle in \(\operatorname{Hom}_B(P,N)\) can be written as a Hom boundary by choosing its homotopy values successively on \(e_\alpha\). After the values on lower cells are fixed, the remaining required value is a cycle in \(N\), and acyclicity supplies a preimage. Every differential has finitely many predecessors. The resulting assignment defines a Hom element even if \(N\) is unbounded; no limit of finite truncations is assumed. Thus \(P\) is K-projective.

Define degree-two \(B\)-linear maps
\[
U_i(e_\alpha)=
\begin{cases}
e_{\alpha-\mathbf e_i},&\alpha_i>0,\\
0,&\alpha_i=0.
\end{cases}
\]
They commute with \(d\) and with one another. Consequently they define a DG algebra map
\[
\rho:S\longrightarrow\operatorname{End}_B(P),\qquad u_i\longmapsto U_i.
\tag{ZS.A2}
\]
Postcomposition with \(q\) is a quasi-isomorphism of complexes
\(\operatorname{End}_B(P)\to\operatorname{Hom}_B(P,R)\), by K-projectivity. The latter Hom has zero differential, and in degree \(2m\) its basis is dual to the finitely many \(e_\alpha\) with \(|\alpha|=m\). The composite of \(\rho\) with this map sends \(u^\alpha\) to that dual basis element. Thus \(\rho\) is a quasi-isomorphism of DG algebras:
\[
\operatorname{REnd}_B(R)\simeq S.
\]
This proves the multiplication and DG formality by actual operators. Although the endomorphism complex itself can contain products, each degree of \(\operatorname{Hom}_B(P,R)\) has finitely many cells. The answer is the polynomial algebra, with no power-series completion.

**Lemma ZS.A2 (diagonal classes and singular directions).** The operators \(u_i\) are the complete-intersection diagonal operators for the odd directions.

For the relative bimodule algebra \(B_R^e=B\otimes_RB^{\mathrm{op}}\), identify the graded opposite algebra with \(B\) and put
\(\delta_i=\epsilon_i^L-\epsilon_i^R\). The diagonal resolution is
\[
Q=\bigoplus_{\alpha\in\mathbf N^r}B_R^e e_\alpha,\qquad
d(e_\alpha)=\sum_{\alpha_i>0}\delta_i e_{\alpha-\mathbf e_i},
\qquad
Q\longrightarrow B.
\tag{ZS.A3}
\]
Set \(z_i=(\epsilon_i^L+\epsilon_i^R)/2\). This invertible change of odd generators writes \(B_R^e=\Lambda_R(\delta_1,\ldots,\delta_r)\otimes_R\Lambda_R(z_1,\ldots,z_r)\). Lemma ZS.A1 on the \(\delta\)-factor proves that \(Q\) resolves the diagonal, with \(z_i\) mapping to \(\epsilon_i\).

The lowering maps on \(Q\) therefore give degree-two diagonal endomorphism classes. Restricting bimodule scalars along \(B\otimes_kB^{\mathrm{op}}\to B_R^e\) gives actual absolute diagonal classes as well: their roofs consist of the same maps and quasi-isomorphism \(Q\to B\). Tensoring such a roof over the right copy of \(B\) with a module gives a natural endomorphism of that module. The semifree bimodule filtration computes this derived tensor on unbounded modules. These even endomorphisms commute, and their naturality is precisely the central action. On the augmentation \(R\), tensoring (ZS.A3) gives (ZS.A1), and the action is exactly \(U_i\).

The cotangent calculation identifies their directions. The free relative extension has \(L_{B/R}=B\otimes_R R^r[1]\), generated by \(d\epsilon_i\). At the classical augmentation, the absolute cotangent complex has degree-zero smooth contribution \(\Omega^1_{R/k}\) and degree-\(-1\) contribution \(R^r\). To verify the smooth contribution locally, take a standard smooth presentation: its regular-equation Koszul resolution gives the cotangent model \([I/I^2\to\Omega^1_{\mathrm{poly}/k}|_R]\); the invertible Jacobian minor splits this injection. Thus only \(\Omega^1_{R/k}\) survives in degree zero. The standard smooth/regular-parameter premises here are those of [*Smooth algebras over a field and the Jacobian criterion*, Theorem 2.1](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md), together with the usual semifree cotangent construction.

Consequently
\[
H^1(T_{\operatorname{Spec}B})|_{\operatorname{Spec}R}=(R^r)^*,
\qquad
\operatorname{Sing}(\operatorname{Spec}B)
=\operatorname{Spec}_R\operatorname{Sym}_R((R^r)^*).
\tag{ZS.A4}
\]
In the cohomological-operator convention, its linear coordinates have degree two. A dual vector lowers the corresponding divided-power cell in (ZS.A3), so its coordinate is exactly the corresponding \(u_i\). This identifies the central action with the odd singular directions; an abstract equality of Ext dimensions would not provide this identification. Here support means the support defined by these diagonal operators. The construction of singular support and its descent on general derived stacks remains a separate geometric foundation.

#### 5.1.2. Coherent generation, Morita and the structure object

**Lemma ZS.A3 (finite resolutions over the coefficient ring).** Every finite \(R\)-module has a finite resolution by finite projective \(R\)-modules.

The ring \(R\) is Noetherian and has finite dimension \(d\). Finiteness of dimension can be seen directly from [*Krull dimension and Noether normalization*, Lemma 4.1](../../AG-CA/src/krull-dimension-and-noether-normalization.md): in a finite-type domain each strict prime specialization loses a transcendence parameter. A finite-type algebra with \(n\) generators has transcendence degree at most \(n\) after quotient by the first prime of a chain, so all chains have length at most \(n\).

Smoothness makes every \(R_{\mathfrak p}\) regular. The actual regular-local bound is [*Projective dimension and the Auslander–Buchsbaum formula*, Corollary 4.3](../../AG-CA/src/projective-dimension-and-the-auslander-buchsbaum-formula.md): its proof resolves the residue field by the regular-parameter Koszul complex and uses the residue-field test of Theorem 2.3. Hence a finite module over \(R_{\mathfrak p}\) has projective dimension at most \(\dim R_{\mathfrak p}\leq d\).

For a finite \(R\)-module \(N\), successively take finite free surjections to obtain a partial resolution of length \(d\); every syzygy is finite by Noetherianity. The final syzygy \(K_d\) localizes to a projective module at every prime, by the Ext/syzygy criterion in Theorem 1.3 of that same lesson. It is finite free at each local ring. For any tensor injection, its kernel therefore vanishes after every prime localization, hence is zero. This is the proof of the local flatness test in [*Tor and flat modules*, Theorem 3.3](../../AG-CA/src/tor-and-flat-modules.md). Thus \(K_d\) is flat. It is finitely presented because \(R\) is Noetherian, so Theorem 5.3 there supplies a splitting of a finite free surjection, making it finite projective. Truncate the resolution at \(K_d\). When \(d=0\), the same argument makes \(N\) itself finite projective.

It follows that
\[
\operatorname{Coh}_B=\operatorname{thick}(R),\qquad
\mathcal C_B=\operatorname{Ind}(\operatorname{thick}(R)).
\tag{ZS.A5}
\]
Indeed every coherent DG module has a finite cohomological Postnikov filtration. Its layers are shifts of finite modules over \(H^0(B)=R\), with the augmentation action. Lemma ZS.A3 builds each layer from finite projective \(R\)-modules, which are retracts of finite sums of \(R\). Conversely \(R\) is coherent, and bounded finite cohomology is preserved by finite cones and retracts.

**Proposition ZS.A4 (Morita on the whole Ind-category).** There is an equivalence
\[
\Phi:\mathcal C_B\xrightarrow{\ \sim\ }\operatorname{Mod}_S,\qquad
\Phi(M)=\operatorname{Maps}_{\mathcal C_B}(R,M).
\tag{ZS.A6}
\]
Use right endomorphism modules by precomposition; the even commutative algebra \(S\) identifies them with left \(S\)-modules.

Here is the construction and proof. By the defining Ind-mapping formula, \(R\) is compact in \(\mathcal C_B\), and its endomorphism algebra is the derived endomorphism algebra in \(\operatorname{Coh}_B\), calculated in (ZS.A2). Exactness and compactness make \(\Phi\) preserve arbitrary sums: a sum is a filtered colimit of its finite partial sums. They also make it preserve geometric realizations, which are filtered colimits of their finite skeleta.

Construct its left adjoint \(U\) by derived tensor with the object \(R\) and its endomorphism action. Concretely take a free DG resolution, or the free bar, of an \(S\)-module and replace its free \(S\)-cells by the corresponding copies of \(R\) in \(\mathcal C_B\). The endomorphism action supplies the differentials and structure maps. Evaluation gives the counit \(U\Phi(M)\to M\); the identity endomorphism and free-resolution augmentation give the unit \(N\to\Phi U(N)\). Tensor–Hom adjunction is verified on free cells and hence on their bars. The triangle identities are the evaluation identities on free cells and extend through the same realizations.

The unit is an equivalence for the free generator \(S\), because \(\Phi(R)=S\). Both its functors preserve sums, cones and the free-resolution realizations, so it is an equivalence for every unbounded \(S\)-module. Applying \(\Phi\) to the counit makes it an equivalence by the triangle identities. The functor \(\Phi\) is conservative: if maps from all shifts of \(R\) to an object vanish, they vanish from every object of \(\operatorname{thick}(R)\), and then from every Ind-object by the Ind-mapping formula. In particular that object's identity is zero. Conservativity now makes every counit an equivalence. This proves (ZS.A6), including its unit and counit on the whole categories.

On coherent objects, \(\Phi\) is ordinary \(\operatorname{RHom}_B(R,-)\). On general Ind-objects it is the continuous Ind-mapping functor just constructed. These must be distinguished: for \(r>0\), \(R\) is not compact in \(\operatorname{Mod}_B\), since (ZS.A2) gives its unbounded self-Ext, whereas a finite perfect \(B\)-module has bounded Hom to \(R\). Ordinary QCoh Hom on arbitrary objects cannot be substituted for \(\Phi\).

**Lemma ZS.A5 (the Koszul image of \(B\)).** In the chosen basis,
\[
\Phi(B)\simeq R[r],\qquad u_i\text{ acts through }S\to R.
\tag{ZS.A7}
\]
Since \(B\) is bounded, each degree of \(\operatorname{Hom}_B(P,B)\) contains finitely many cells. Identify its graded module with \(S\otimes_R\Lambda_R(\epsilon_1,\ldots,\epsilon_r)\). If a Hom element has degree \(q\), its differential is \(-(-1)^q f\,d_P\), while \(f(\epsilon_i e_\alpha)=(-1)^q\epsilon_i f(e_\alpha)\). Hence the differential is exactly
\[
d_{\mathrm{Hom}}=-\sum_i u_i\,(\epsilon_i\wedge-).
\tag{ZS.A8}
\]
Precomposition with \(U_i\) is multiplication by \(u_i\).

For one variable this pairs \(u_i^m\) with \(-u_i^{m+1}\epsilon_i\), leaving only \(\epsilon_i\) in degree \(-1\). Tensor these split \(R\)-complexes with their tensor signs. Their only cohomology is
\(R\epsilon_1\cdots\epsilon_r\) in degree \(-r\). There is an \(S\)-linear quasi-isomorphism onto it: set every \(u_i\) to zero and project onto the top exterior coefficient. It kills the differential in (ZS.A8), and the paired-complex calculation proves it is a quasi-isomorphism. This proves (ZS.A7) as an \(S\)-module statement, not only as a graded vector-space calculation.

#### 5.1.3. Zero support for arbitrary unbounded objects

Let \(I=(u_1,\ldots,u_r)\). For an \(S\)-module \(N\), restriction to the principal support open \(D(u_i)\) is the localization telescope
\[
N[u_i^{-1}]
=\operatorname*{colim}_{m\geq0}
\bigl(N\longrightarrow N[2]\longrightarrow N[4]\longrightarrow\cdots\bigr),
\tag{ZS.A9}
\]
whose arrows multiply by \(u_i\). Filtered colimits of complexes are exact, so its cohomology is \(H^*(N)[u_i^{-1}]\). Under \(\Phi\), the diagonal operators act by these same multiplications: naturality of a diagonal class gives \(u_M f=f[2]u_R\), and \(u_R\) is the operator in (ZS.A2).

Thus zero singular support means restriction to the complement of the zero section vanishes, and that complement is covered by the \(D(u_i)\). Explicitly,
\[
\operatorname{SS}(M)\subseteq V(I)
\quad\Longleftrightarrow\quad
\Phi(M)[u_i^{-1}]=0\ \text{for every }i.
\tag{ZS.A10}
\]
For coherent objects, \(\Phi(M)\) is perfect over \(S\), hence its cohomology is a finite graded \(S\)-module and this is its usual closed cohomological-operator support. For arbitrary objects the displayed vanishing is the localizing support condition. It does not require a common annihilating power for the whole object.

**Lemma ZS.A6 (the multivariable telescope).** For arbitrary unbounded \(N\),
\[
N[u_i^{-1}]=0\ \text{for all }i
\quad\Longleftrightarrow\quad
N\in\operatorname{Loc}_S(R).
\tag{ZS.A11}
\]
Here \(\operatorname{Loc}\) permits shifts, cones and all colimits.

Put \(\Gamma_iS=\operatorname{fib}(S\to S[u_i^{-1}])\), and
\(\Gamma_iN=(\Gamma_iS)\otimes_S^LN\). Exactness of tensor gives the corresponding localization fibre for \(N\). Finite fibres commute with filtered colimits in the stable module category, so
\[
\Gamma_iS
\simeq\operatorname*{colim}_{m\geq1}
\operatorname{fib}(S\xrightarrow{u_i^m}S[2m])
\simeq\operatorname*{colim}_{m\geq1}(S/(u_i^m))[2m-1].
\]
The last identity follows from injectivity of \(u_i^m\) in the graded polynomial ring. The transition maps are those induced by the localization telescope, with their displayed shifts.

The tensor factors \(\Gamma_iS\) commute. Their product therefore gives
\[
\Gamma_I N
:=\Gamma_1\cdots\Gamma_rN
\simeq\operatorname*{colim}_{(m_1,\ldots,m_r)}
\left(S/(u_1^{m_1},\ldots,u_r^{m_r})\right)
\otimes_S^LN\,[\,\textstyle\sum_i(2m_i-1)\,].
\tag{ZS.A12}
\]
To justify the quotient identification, tensor the one-variable two-term resolutions. Each \(u_i^{m_i}\) is a nonzerodivisor after the earlier powers are imposed: the remaining polynomial monomials give a free module over the ring in the other variables. Induction on the list, using the mapping-cone exact sequence, proves Koszul exactness. Equivalently its DG exterior generators have degree \(2m_i-1\) and differential \(u_i^{m_i}\); the two contributions to the squared differential cancel. The regular-sequence proof with these signs is also the argument of [*Projective dimension and the Auslander–Buchsbaum formula*, Theorem 4.1](../../AG-CA/src/projective-dimension-and-the-auslander-buchsbaum-formula.md).

The quotient in (ZS.A12) has a finite filtration by total monomial degree. Its layers are finite sums of shifts of \(R\), because multiplication by any \(u_i\) increases that degree and is zero on each layer. Tensoring the filtration with \(N\) therefore builds its derived tensor from shifts of \(R\otimes_S^LN\). This is an \(R\)-module with augmentation \(S\)-action, and every unbounded \(R\)-module is built from free \(R\)-cells. Thus each term and then \(\Gamma_I N\) lie in \(\operatorname{Loc}_S(R)\).

If all localizations vanish, every counit \(\Gamma_iN\to N\) is an equivalence. Composing these equivalences with the commuting tensor factors gives \(\Gamma_IN\simeq N\), proving the forward implication of (ZS.A11). Conversely \(R\) localizes to zero at each \(u_i\), and localization preserves all colimits and exact triangles; it vanishes throughout \(\operatorname{Loc}_S(R)\).

Elementwise, the condition says that for each \(x\in H^*(N)\) and each \(i\), some \(u_i^{a_i}\) kills \(x\). Then every monomial of total degree \(\sum_i(a_i-1)+1\) kills \(x\), so a power of \(I\) kills that element. The power can depend on \(x\). For example the direct sum \(\bigoplus_{m\geq1}S/(u_1^m,\ldots,u_r^m)\), for \(r>0\), has zero support yet no common power of \(u_1\) annihilates it. The telescope proof covers precisely this unbounded-colimit behavior.

**Theorem ZS.A7 (the affine zero-support comparison).** The comparison extending the finite-perfect inclusion is fully faithful and identifies
\[
\Xi:\operatorname{Mod}_B\simeq\operatorname{Ind}(\operatorname{Perf}_B)
\ \longrightarrow\ \mathcal C_B
\]
with the zero-support subcategory:
\[
\operatorname{im}\Xi=\operatorname{Loc}_{\mathcal C_B}(B)
=\mathcal C_{B,V(I)}.
\tag{ZS.A13}
\]

First, \(B\) is a compact generator of its DG module category: mapping from \(B\) is the underlying complex and commutes with colimits, and its vanishing detects zero modules. Every module is obtained from free cells. One construction uses the augmented free bar over \(k\), whose extra degeneracy inserts the unit and contracts the augmentation as a complex; its direct-sum realization uses no boundedness assumption. Alternatively a semifree resolution adjoins cells for all cycles and then for all relations. Each cell differential involves finitely many earlier cells. Their finite predecessor closures are finite, since a finitely branching infinite predecessor tree would give an infinite strictly descending sequence in the well-order of cells. Thus the resolution is a filtered colimit of finite cell submodules. A compact object's identity factors through a finite cell stage, making it a retract of a finite cell module. This proves \(\operatorname{Mod}_B=\operatorname{Ind}(\operatorname{Perf}_B)\).

Finite perfect modules are coherent, since \(B\) has bounded finite \(R\)-cohomology and \(R\) is Noetherian. Their inclusion in \(\operatorname{Coh}_B\) is fully faithful. For filtered diagrams of perfect objects \(P_a,Q_b\), both Ind-categories have the mapping complex
\[
\operatorname{Maps}\bigl(\operatorname*{colim}_aP_a,
\operatorname*{colim}_bQ_b\bigr)
=\lim_a\operatorname*{colim}_b\operatorname{RHom}_B(P_a,Q_b).
\]
This proves full faithfulness of the Ind-extension. Its essential image is exactly \(\operatorname{Loc}(B)\), since finite perfects are the thick subcategory generated by \(B\).

By Lemma ZS.A5, \(\Phi(B)=R[r]\), so \(\Phi(\operatorname{Loc}(B))=\operatorname{Loc}_S(R)\). Lemma ZS.A6 and the identified diagonal action now prove (ZS.A13). The augmentation \(R\), in contrast, maps to the free \(S\)-module and has the whole singular cone as support for \(r>0\).

#### 5.1.4. Localization, generator bundles and rank zero

**Proposition ZS.A8 (compatibility with coefficient localization).** For \(f\in R\), put \(R'=R_f\), \(B'=B\otimes_RR'\), and \(S'=S\otimes_RR'\). Coefficient localization on coherent modules extends continuously to their Ind-categories, and
\[
\Phi_{R'}(M|_{R'})\simeq S'\otimes_S^L\Phi_R(M).
\tag{ZS.A14}
\]
The comparison and all central operators commute with these maps.

On a coherent module, choose its cohomological truncation model with underlying complex in a finite interval. In each degree of \(\operatorname{Hom}_B(P,M)\), only finitely many \(e_\alpha\) then occur. Flat localization commutes with these finite products and with their differentials. Also \(P\otimes_RR'\) is exactly the displayed augmentation resolution for \(B'\). This proves (ZS.A14) on coherent objects. Both sides are continuous on Ind-objects, so the comparison extends to every object. Composition of localizations gives the literal associative tensor comparison. The diagonal resolution and lowering maps likewise localize term by term. This argument uses the Ind-mapping functor on general objects; it does not interchange localization with arbitrary products in ordinary QCoh Hom.

Now let \(V\) be a finite projective \(R\)-module of constant rank \(r\), placed in degree \(-1\), and set
\[
B=\Lambda_RV,\qquad S=\operatorname{Sym}_R(V^*),\quad |V^*|=2.
\]
The resolution is intrinsic: adjoin even variables from \(V\) in degree \(-2\), with differential the identity into the odd copy of \(V\). In a basis its divided monomials \(t^\alpha/\alpha!\) give (ZS.A1). Characteristic zero makes these factorials invertible. Its graded cell quotients are finite projective over \(B\); the acyclic-target lifting proof still works, since Hom from a finite projective coefficient module is exact. A dual vector acts by the corresponding directional derivative in these even variables. Hence the DG algebra map \(S\to\operatorname{End}_B(P)\), the diagonal construction and their central action are independent of a basis.

The Koszul calculation must retain its determinant line:
\[
\Phi(B)\simeq\det(V)[r].
\tag{ZS.A15}
\]
The unpaired top exterior coefficient is \(\Lambda^rV\) in degree \(-r\). Changes of odd basis multiply it by the determinant of the change, so (ZS.A15), rather than a chosen trivialization of it, is canonical. An invertible \(R\)-line and \(R\) generate the same localizing subcategory of \(S\)-modules with augmentation action: the line is a retract of a finite sum of \(R\), and tensoring it with its finite-projective dual makes \(R\) a retract of a finite sum of that line.

For clarity the relative dualizing module in this algebra model is
\[
\omega_{B/R}:=\operatorname{Hom}_R(B,R)
\simeq B\otimes_R\det(V)^*[-r],
\qquad
\Phi(\omega_{B/R})\simeq R.
\tag{ZS.A16}
\]
The line in the tensor factor is in cohomological degree \(r\). The isomorphism is the perfect exterior pairing: for homogeneous \(b\) and \(\lambda\in\det(V)^*\), send \(b\otimes\lambda\) to
\[
c\longmapsto(-1)^{r|b|}\lambda\bigl((bc)_{\mathrm{top}}\bigr).
\]
With the dual action \((a\varphi)(c)=(-1)^{|a||\varphi|}\varphi(ac)\), graded commutativity proves \(B\)-linearity. In a local exterior basis complementary subsets pair by signed units, proving the map is an isomorphism; these top-wedge formulas glue. Tensoring (ZS.A15) with \(\det(V)^*[-r]\) gives the last assertion. This is an \(R\)-relative statement; additional absolute geometric dualizing data are not inferred from it.

The support proof also glues over coefficient localizations. Choose a finite principal cover \(D(f_j)\) trivializing \(V\). The frame criterion and (ZS.A14) identify zero support on each member with \(\operatorname{Loc}_{S_{f_j}}(R_{f_j})\). As \(S\)-modules, \(R_{f_j}\) lies in \(\operatorname{Loc}_S(R)\) by the degree-zero multiplication telescope for \(f_j\). Restriction of scalars is continuous and exact, so every localized zero-support object lies in \(\operatorname{Loc}_S(R)\).

The augmented finite Čech localization complex for this cover recovers any unbounded \(S\)-module. At every prime some \(f_j\) is invertible; that cover vertex contracts the localized augmented complex. Its finite Čech direction makes its totalization acyclic in every degree, without an infinite-product convergence issue. Local detection then proves the augmentation is a quasi-isomorphism. It builds the original module from the finitely many intersections of its localized modules by finite cones. Therefore local zero support implies membership in \(\operatorname{Loc}_S(R)\) globally on this affine ring. The converse follows from localization of the generator \(R\). This proves Theorem ZS.A7 for a finite projective odd-generator bundle.

For \(r=0\), \(B=S=R\). Lemma ZS.A3 and finite Postnikov filtrations give \(\operatorname{Coh}_R=\operatorname{Perf}_R\); hence \(\mathcal C_R=\operatorname{Mod}_R\) and \(\Phi\) and \(\Xi\) are the identity comparisons. The localization conditions form an empty list, \(\Gamma_\varnothing S=S\), and the zero section is the entire smooth base. Formulas (ZS.A15)–(ZS.A16) have determinant \(R\) and shift zero.

The four categories and comparison maps are displayed below.
\[
\begin{array}{ccc}
\operatorname{Mod}_B=\operatorname{Ind}(\operatorname{Perf}_B)
&\xrightarrow{\quad\Xi\ \text{fully faithful}\quad}&
\operatorname{Ind}(\operatorname{Coh}_B)\\
{\scriptstyle\Phi\Xi}\,\downarrow&&
\downarrow\,{\scriptstyle\Phi\ \text{equivalence}}\\
\operatorname{Loc}_S(R)
&\xrightarrow{\qquad\text{inclusion}\qquad}&
\operatorname{Mod}_S .
\end{array}
\]

*The square commutes by the definition of \(\Phi\Xi\). The top inclusion extends finite perfect modules; the bottom inclusion is characterized by the simultaneous localization criterion. The determinant line is essential when the odd generators form a bundle.*

The theorem is confined to these affine exterior-algebra charts and ordinary coefficient localizations. The stable DG and Ind-category constructions, the smooth/cotangent local presentations, and the recursive Noetherian, localization, regular-parameter, Ext and flat-module foundations of the exact earlier algebra proofs remain their explicit premises. Product support, natural geometric comparisons, complete-intersection chart existence and descent for general derived schemes or Artin stacks are separate inputs.

#### 5.1.5. Dualizing lines and the comparison on smooth charts

Let \(U=\operatorname{Spec}R\) be a smooth affine scheme over the characteristic-zero field, of pure dimension \(d\). Allow a finite projective odd-generator module \(V\) of rank \(r\), and write \(B=\operatorname{Sym}_R(V[1])\). Locally this is the exterior algebra on \(r\) generators of degree \(-1\). Put \(Z_U=\operatorname{Spec}B\). The affine comparison proved above is denoted
\[
\Xi_U:\operatorname{QCoh}(Z_U)\longrightarrow\operatorname{IndCoh}(Z_U).
\tag{ZS.G1}
\]
It extends the inclusion of finite perfect \(B\)-modules into coherent \(B\)-modules. Its essential image is exactly zero singular support. In particular this is an assertion about every unbounded object of these presentable categories.

The dualizing object on this explicit chart is
\[
\omega_{Z_U}
 =\operatorname{Hom}_R(B,\omega_U)
 \simeq B\otimes_R\det(V)^*\otimes_R\Omega_R^d[d-r],
\qquad \omega_U=\Omega_R^d[d].
\tag{ZS.G2}
\]
Here the first equality is the finite-algebra dualizing construction. Its elementary adjunction sends a \(B\)-linear map to evaluation at \(1\), giving
\[
\operatorname{RHom}_B(M,\operatorname{Hom}_R(B,\omega_U))
 \simeq\operatorname{RHom}_R(M,\omega_U).
\tag{ZS.G3}
\]
The algebra \(B\) is a bounded finite projective \(R\)-complex. Thus a finite projective resolution over \(R\), or its coinduced injective comparison, gives the derived identity as well. The Frobenius pairing on \(B\) is wedge product followed by its top exterior coefficient. It pairs \(\bigwedge^i V\) perfectly with \(\bigwedge^{r-i}V\) into \(\det(V)\). This proves the second equality of (ZS.G2), including its line and shift. It does not discard the determinant line after a change of frame.

Every coherent \(B\)-module has a bounded underlying coherent \(R\)-complex, which is perfect over this regular \(R\) by the finite-resolution argument above. Consequently
\[
\mathbb D_U(M)=\operatorname{RHom}_R(M,\omega_U)
\]
is a duality on coherent \(B\)-modules. Evaluation gives \(M\simeq\mathbb D_U^2(M)\): this is the ordinary finite-projective double-dual calculation, tensored with a line and a shift. The \(B\)-action on the dual is the one prescribed by evaluation, with the usual graded signs.

Tensoring with (ZS.G2) is an autoequivalence of \(\operatorname{IndCoh}(Z_U)\), since that object is an invertible \(B\)-module up to shift. Define
\[
\Upsilon_U(F)=\Xi_U(F)\otimes_B\omega_{Z_U}.
\tag{ZS.G4}
\]
It is fully faithful and has the same zero-support image as \(\Xi_U\). To verify that last assertion directly, a line is locally free of rank one. In a frame, tensoring it and shifting changes none of the vanishing localizations by the cohomological operators \(u_i\). The affine torsion characterization therefore applies before and after that tensor operation. Local frames detect the assertion globally on the chart.

The distinction between the two comparisons concerns their normalization. \(\Xi\) extends the perfect-object inclusion on a scheme. \(\Upsilon\), with the dualizing twist, is the comparison compatible with \(!\)-pullbacks on the stack charts used below. Their essential images agree on these Gorenstein charts; the functors themselves need not agree.

#### 5.1.6. Compatibility under changes of chart

Consider a map of smooth affine bases \(f:U'\to U\), and pull the generator bundle back to \(V'\). Thus \(B'=R'\otimes_R B\). The coherent pullback of a module is \(R'\otimes_R^{\mathbf L}M\). It is again bounded coherent over \(R'\), because the underlying \(R\)-complex of \(M\) has a finite projective resolution. On these charts the coherent \(!\)-pullback is the duality construction
\[
f^!M=\mathbb D_{U'}\bigl(R'\otimes_R^{\mathbf L}\mathbb D_U M\bigr).
\tag{ZS.G5}
\]
It extends continuously to the Ind-category. Computing with that finite resolution gives
\[
f^!M\simeq
 (R'\otimes_R^{\mathbf L}M)\otimes_{R'}\omega_f,
\qquad
\omega_f=\omega_{U'}\otimes_{R'}(f^*\omega_U)^{-1}.
\tag{ZS.G6}
\]
Indeed the tensor–Hom comparison for a finite projective complex is termwise evaluation; tensoring by the two invertible dualizing complexes gives precisely the displayed factor. This computation is valid for the smooth face maps, open restrictions and regular-immersion degeneracy maps of the torus nerve. For a smooth map of relative dimension \(e\), the cotangent exact sequence identifies \(\omega_f=\det\Omega^1_{U'/U}[e]\). For a regular immersion of codimension \(c\), the Koszul resolution of its regular equations gives \(\omega_f=\det(N)[-c]\), where \(N\) is its normal bundle. The latter formula follows by dualizing the finite exterior Koszul complex: its last coefficient is \(\det(N)\) and its last degree is \(-c\). Both calculations are compatible with changes of equations or frames.

In particular (ZS.G2) and (ZS.G6) give
\[
f^!\omega_{Z_U}=\omega_{Z_{U'}}.
\tag{ZS.G7}
\]
For a perfect \(B\)-module \(F\), distribute its finite free cells through (ZS.G5), or use the same finite-projective tensor–Hom comparison. This gives
\[
f^!\Upsilon_U(F)
 \simeq\Upsilon_{U'}(f^*F).
\tag{ZS.G8}
\]
Both sides are continuous in \(F\). The free-cell and augmented-bar construction expresses every \(B\)-module as a colimit of such cells, so (ZS.G8) holds on the full unbounded category.

These comparisons are natural comparisons of complexes, rather than equalities of dimensions at points. For two consecutive maps, composing the finite-projective evaluation comparisons is the associative tensor comparison, and the two \(\omega_f\)-factors cancel the intermediate \(\omega_U\). Thus their composite is the comparison for the composite map. The unit comparison is identity evaluation. The same associativity and evaluation maps supply the coherent higher comparisons in the DG construction. This proves compatibility with the entire chart diagram, including its degeneracies.

Support in the zero section also glues on this diagram. Localization by a \(u_i\) commutes with derived extension of coefficients, and the additional factor in (ZS.G6) is invertible. The local theorem therefore carries zero support to zero support. Under a change of odd-generator frame, the operators change by the dual invertible matrix. Their ideal is the augmentation ideal of the symmetric algebra of the dual bundle, independently of that frame. For a finite affine open cover, coefficient localization is faithfully flat after taking the product of the covering rings. A localized operator module is zero if it becomes zero on that cover: its cohomology modules have that same faithful-flat detection property. Thus zero support is both preserved and detected on the cover.

#### 5.1.7. Smooth factors and the torus automorphism stack

Let \(Y\) be a smooth finite-type scheme over \(k\), let \(Z_V=\operatorname{Spec}\operatorname{Sym}_k(V[1])\), and let \(T\) be a split torus. The action of \(T\) on \(Y\times Z_V\) is trivial. On affine opens of \(Y\), the preceding calculation applies with their smooth coordinate rings. It gives an equivalence of the entire descent diagrams
\[
\operatorname{QCoh}(Y\times Z_V)
 \xrightarrow{\ \Upsilon\ }
\operatorname{IndCoh}_{\{0\}}(Y\times Z_V).
\tag{ZS.G9}
\]
Here the scheme and stack categories use their affine and smooth descent constructions, with \(*\)-pullbacks for QCoh and \(!\)-pullbacks for IndCoh. These categorical constructions remain the explicit foundations of the lesson. To obtain (ZS.G9), take the limit of the compatible local equivalences (ZS.G8). The local inverses are compatible as well: their compatibility is obtained by applying the fully faithful local equivalences to the displayed comparison. Their composites are the identities on every chart and hence on the limit. This proves the descent deduction; it does not assume a global zero-support comparison theorem.

For \(\mathcal S=Y\times Z_V\times BT\), use the atlas
\(Y\times Z_V\to\mathcal S\). Its Čech terms are
\[
(Y\times T^n)\times Z_V,\qquad n\geq0.
\tag{ZS.G10}
\]
Every \(Y\times T^n\) is smooth of finite type. The faces are projections or multiplication in torus coordinates; the latter is projection after an invertible change of coordinates. The degeneracies insert the identity, a regular immersion in smooth torus coordinates. Thus (ZS.G5)–(ZS.G8) apply after affine refinement to every map in this nerve. The dualizing twists, including the relative shifts of the atlas, are retained throughout the diagram. Taking its limit proves
\[
\boxed{\Upsilon_{\mathcal S}:\operatorname{QCoh}(\mathcal S)
 \xrightarrow{\sim}\operatorname{IndCoh}_{\{0\}}(\mathcal S).}
\tag{ZS.G11}
\]
The subscript \(\{0\}\) denotes the zero section over the full classical stack. It permits arbitrary ordinary support in \(Y\) and arbitrary character weights in \(BT\).

Write \(s=\operatorname{rank}T\) and \(d=\dim Y\). The shifted dualizing line on this product stack, regarded as an invertible QCoh object, is
\[
\omega_{\mathcal S}
 =\Omega_Y^d\otimes\det(V)^*\otimes\det(\mathfrak t)[d-r-s].
\tag{ZS.G11a}
\]
The first two factors were computed in (ZS.G2). For the final factor, the atlas to \(BT\) is smooth of relative dimension \(s\), with relative determinant \(\det(\mathfrak t^*)[s]\). Its \(!\)-pullback takes the dualizing object of \(BT\) to that of the point. Cancelling that relative determinant gives \(\det(\mathfrak t)[-s]\). The torus acts trivially on its Lie algebra, so this line is in character weight zero. This verifies (ZS.G11a) and its atlas shift.

Untwisting gives the scheme-normalized comparison on this stack:
\[
\Xi_{\mathcal S}(F)=\Upsilon_{\mathcal S}(F\otimes\omega_{\mathcal S}^{-1}).
\tag{ZS.G11b}
\]
It has the same fully faithful zero-support image because the untwist is an autoequivalence of QCoh. For a smooth atlas map \(a:W\to\mathcal S\), the formulas above give the precise chart comparison
\(a^!\Xi_{\mathcal S}(F)=\Xi_W(a^*F\otimes\omega_a)\), where
\(\omega_a=\omega_W\otimes(a^*\omega_{\mathcal S})^{-1}\). Thus its \(!\)-chart formula retains the relative line and shift. The \(s\) in this coherent dualizing calculation is the relative dimension of the atlas; the D-module normalized fibre functor remains the one specified in §3.

The character factor can be checked explicitly. If \(\Lambda=X^*(T)\), write its coordinate Hopf algebra as \(k[\Lambda]\). A comodule element has a finite coaction expression \(\sum_\lambda m_\lambda\otimes e^\lambda\). Coassociativity and the counit give the unique decomposition into weight submodules. The differential preserves each weight. This proof is valid degree by degree for unbounded complexes. Conversely the direct sum of any family of weight complexes has this coaction because every element belongs to only finitely many summands. Mapping complexes between such decomposed objects are the products of their weightwise mapping complexes. Hence the category permits every family of weights; no bounded or finite-weight condition has been imposed on its arbitrary objects.

On coherent objects only finitely many weights occur: finitely many module generators have finite coactions, and multiplying by the weight-zero coefficients cannot introduce a new weight. Coherent objects can therefore be Ind-completed with finite-weight compact stages. This is consistent with (ZS.G10) and with the unrestricted family of weights after taking colimits. Since the central operators act in weight zero, an object has zero singular support precisely when its operator localizations vanish weight by weight. This gives the same condition as (ZS.G11).

#### 5.1.8. The local-system stack of any torus

Return to the pointed smooth projective curve of the lesson and a torus of rank \(r\). Over the algebraically closed characteristic-zero field choose its lattice basis. The derived family-and-arrow construction of §1, applied to each factor, identifies its local-system stack with
\[
\operatorname{LocSys}_{T}(X)
 \simeq (J_X^\natural)^r\times Z_r\times BT,
\qquad
Z_r=\operatorname{Spec}\Lambda(\varepsilon_1,\ldots,\varepsilon_r).
\tag{ZS.G12}
\]
Each \(\varepsilon_i\) has degree \(-1\). The factor \((J_X^\natural)^r\) is smooth once the Picard and connection constructions in §1 and Lemma G are supplied; it is a scheme of finite type, covered by the smooth affine charts used above. The splitting of curve cohomology used to exhibit this product is one of the specified choices in §1. It is not being asserted to be a canonical product.

The Lie calculation for nilpotence is elementary. The torus coadjoint action is trivial, so every linear coordinate on \(\mathfrak t^*\) is an invariant polynomial of positive degree. Those linear coordinates generate the maximal ideal of the origin. The invariant-zero-fibre nilpotent scheme is therefore exactly the origin. In the product (ZS.G12), the complete-intersection operators give its obstruction directions and the global nilpotent condition is their zero section. This is a scheme-theoretic equation, not just a statement about geometric points.

Apply (ZS.G11) to (ZS.G12). It proves the torus comparison required in (5.7):
\[
\boxed{\operatorname{QCoh}(\operatorname{LocSys}_{T}(X))
 \xrightarrow{\ \Upsilon\ }\operatorname{IndCoh}_{\mathrm{Nilp}}
              (\operatorname{LocSys}_{T}(X)).}
\tag{ZS.G13}
\]
It applies to every genus and every rank, to all unbounded objects and all character weights. If \(g=0\), the smooth factor is a point but the derived factor and scalar automorphisms remain. If \(r=0\), there are no odd directions and the local theorem reduces to the smooth comparison; the nilpotent condition imposes no additional direction.

Changing the lattice basis induces the dual linear change on the odd generators and their cohomological operators. It preserves their augmentation ideal. The comparison \(\Upsilon\) is defined by the dualizing object and the natural tensor–Hom maps (ZS.G3)–(ZS.G8), so it is transported by the resulting stack isomorphism. The equations for composition of basis changes are the same tensor and evaluation comparisons already proved. Thus the essential-image assertion is independent of the lattice basis and the chosen presentation of (ZS.G12).

One object distinction is essential here. The coherent augmentation module on an exterior chart is a compact object of IndCoh, and its compact-generator transform is a free polynomial module with full singular support. The augmentation regarded as a QCoh object has a free-cell resolution of infinite length. Its image under the continuous comparison is the colimit of the corresponding perfect objects, and has zero support by the theorem. The two IndCoh objects are therefore different, even though the forgetful QCoh calculation of the augmentation has the same ordinary module. The framed-point QCoh object of §5 uses this continuous comparison when it is viewed in the nilpotent IndCoh category. Its nonperfectness does not turn it into the coherent full-support augmentation object.

The proof establishes the zero-support comparison on this full torus stack from its explicit exterior/smooth/automorphism model. It retains the geometric premises of the actual derived local-system product, regular affine and coherent-duality foundations, and the constructed affine/smooth stack descent categories. It does not prove the general zero-support theorem for every quasi-smooth derived Artin stack or any general reductive Eisenstein theorem. Those broader mathematical obligations remain explicit elsewhere in the programme.

## 6. Genus zero, genus one, and Whittaker normalization

For \(X=\mathbb P^1\), \(J=J^\natural=\operatorname{Spec}k\). Therefore
\[
\operatorname{Bun}_{\mathbb G_m}
 \simeq B\mathbb G_m\times\underline{\mathbb Z},
\qquad
\operatorname{LocSys}_{\mathbb G_m}
 \simeq Z_{\mathrm{der}}\times B\mathbb G_m,
\]
and both categories in (5.1) are \(\prod_{d\in\mathbb Z}\operatorname{Mod}_B\). Conditional on the categorical descent foundations, this computes the genus-zero case including its nonclassical direction. The unique geometric flat line produces the augmentation module in every degree, corresponding to \(k_B\boxtimes k[z,z^{-1}]\), rather than to the structure sheaf \(B\) in one weight.

For an elliptic curve \(J=X\), \(J^\natural\to J\) is its one-dimensional vector extension, so \(J^\natural\) has dimension two. At the trivial flat line, the spectral tangent cohomology has dimensions \(1,2,1\) in degrees \(-1,0,1\). Over \(\mathbb C\), a character with monodromies \(u,v\) gives the rigidified point \(e\) on \(J^\natural\); the automorphic line has the inverse monodromies on the Jacobian in the downward convention, and inversion before \(\Phi_+\) restores \(u,v\). The \(B\)-augmentation and the full Laurent representation then restore its stabilizer and all degrees exactly as in (5.5).

For a point \(e\) of \(J^\natural\), the object \(k_e\boxtimes B\boxtimes k(d)\) is compact: \(J^\natural\) is smooth, so \(k_e\) is perfect; \(B\) is free; and the weight support is finite. Its inverse has the normalized compact atlas generator on the automorphic stabilizer and is supported only in degree \(d\). Replacing \(B\) by \(k_B\) makes it coherent but not compact. Adding every weight gives the global eigenobject and removes finite-weight coherence. This supplies explicit objects for each distinction.

The torus has no nontrivial maximal unipotent subgroup or Whittaker character. This simplifies the Whittaker datum, but does not remove the bundle automorphisms or the Fourier sign. In [GLC I §1.2](https://arxiv.org/abs/2405.03599), the vacuum Poincaré object is the compact-support pushforward from \(\operatorname{Bun}_{N,\rho(\omega_X)}\), with the exponential and its normalization. For \(T\), \(N=1\), \(\rho=0\), and that stack is a point mapping to the trivial \(T\)-bundle with its identification. The coefficient is the corresponding exceptional fibre, rather than a quotient that forgets its stabilizer.

GLC I §1.5 identifies the normalized torus functor explicitly as
\[
\mathbb L_T=\operatorname{FM}^{\mathrm{enh}}\circ\tau_T,
\qquad \tau_T(t)=t^{-1}.                               \tag{6.1}
\]
It also records the compatibility with right D-module forgetting and the projection from local systems to bundles. This is the Cartan inversion used above. Thus “trivial Whittaker normalization” means the absence of the unipotent character; it does not license deleting the inversion, the half-root convention, or the fixed atlas shifts.

## 7. The elliptic Fourier–Mukai calculation

There are two natural readings of “the Fourier–Mukai image of the structure sheaf.” We compute both, specifying the input category.

Let \(J\) be an elliptic curve, \(\widehat J\) its dual, and \(\mathcal P\) the normalized coherent Poincaré line on \(J\times\widehat J\). The ordinary coherent transform is
\[
\operatorname{FM}_{\mathrm{coh}}(M)
 =Rp_{\widehat J,*}(\mathcal P\otimes p_J^*M).
                                                               \tag{7.1}
\]
**Proposition 7.1.** In this unshifted coherent-transform convention,
\[
\operatorname{FM}_{\mathrm{coh}}(\mathcal O_J)
       \simeq k_0[-1].
                                                               \tag{7.2}
\]

**Proof.** A nontrivial degree-zero line on \(J\) has no nonzero section: a section would have an effective divisor of degree zero and hence trivialize it. Its \(H^1\) is also zero by Serre duality, since \(\omega_J\simeq\mathcal O_J\). Therefore the perfect complex in (7.1) is supported at the origin of \(\widehat J\).

Complete its local base at that origin, writing \(R=k[[a]]\). Proper cohomology and base change identify its derived special fibre with \(R\Gamma(J,\mathcal O_J)\), whose dimensions are one in degrees zero and one. The family cohomology has perfect amplitude \([0,1]\). A minimal free model over \(R\) therefore has one free term in each of these degrees:
\[
[\,R\xrightarrow{f(a)}R\,],\qquad f(a)\in(a).
                                                               \tag{7.3}
\]
The linear coefficient of \(f\) is nonzero. To verify it, restrict the Poincaré family to \(k[a]/a^2\). Its tangent class is the nonzero universal class in \(H^1(J,\mathcal O_J)\). The connecting map that attempts to lift the section \(1\) of the special fibre is cup product with that class, hence is nonzero. In the model (7.3) that connecting map is exactly the coefficient of \(a\) in \(f\). Thus \(f=a\) times a unit. Rescale one basis to make \(f=a\). The kernel is zero and the cokernel is \(k\), in degree one.

Faithfully flat completion gives a length-one skyscraper in cohomological degree one on the original smooth base. There is no cohomology away from the origin, so the entire transform is \(k_0[-1]\), proving (7.2). \(\square\)

As a check, its derived fibre at zero has a copy of \(k\) in degrees zero and one, because the derived pullback of \(k_0\) has its additional \(\operatorname{Tor}_1\). Taking only an ordinary stalk of (7.2) would miss \(H^0(J,\mathcal O_J)\).

For the de Rham correspondence (4.2), the input is instead the D-module \((\mathcal O_J,d)\) with its trivial flat connection. Its point-image normalization gives
\[
\Phi_{\mathrm{down}}(\mathcal O_J,d)=k_{e_0}
\quad\text{on }J^\natural,                            \tag{7.4}
\]
in degree zero, where \(e_0\) is the trivial flat line. Inversion preserves this line, so (7.4) follows from the inverse-kernel calculation of §4. Equations (7.2) and (7.4) live on different spectral spaces and use different source categories and functor normalizations; both are needed to make the exercise unambiguous.

## 8. Exercises and complete solutions

**Exercise 8.1 (easy).** Compute the full rank-one spectral stack and its tangent complex for a genus-zero curve over \(k\). Explain why its classical point set is insufficient.

**Solution 8.1.** The degree-zero Picard scheme of \(\mathbb P^1\) is a point, and \(H^0(\Omega^1)=0\), so \(J^\natural\) is a point. Equation (1.4) gives \(Z_{\mathrm{der}}\times B\mathbb G_m\), with function DG algebra \(k[\epsilon]\), \(|\epsilon|=-1\), on its derived factor. The de Rham cohomology of \(\mathbb P^1\) is \(k\) in degrees zero and two and zero in degree one. After shifting by one, the tangent has \(k\) in degrees \(-1\) and \(1\). The automorphism stack supplies the former and the derived factor supplies the latter. Every field-valued flat line is trivial, but neither the scalar automorphisms nor the obstruction direction disappears from the moduli problem.

**Exercise 8.2 (easy).** Prove the degree/weight equivalence and identify its compact objects. Explain why an infinite weight family is permitted.

**Solution 8.2.** A sheaf of crystals on \(\coprod_d\operatorname{Spec}k\) is a family \(M_d\) of complexes. A quasicoherent sheaf on \(B\mathbb G_m\) is a Laurent-coalgebra comodule, whose coaction uniquely decomposes it into weight subcomplexes. These descriptions identify morphisms and quasi-isomorphisms weightwise and yield \(\prod_d\operatorname{Vect}_k\) on both sides. An infinite family becomes an underlying direct sum of representations; every vector, rather than the whole object, has finite weight support. Compactness forces the identity to factor through a finite-weight truncation, so only finitely many components survive; each must be a perfect complex. Conversely finite support and perfect components make the mapping functor commute with colimits.

**Exercise 8.3 (medium).** Prove the stabilizer/derived-factor equivalence, including the algebra multiplication and the constant object's image.

**Solution 8.3.** The normalized atlas fibre \(F=p^![-2]\) is conservative and continuous, with shifted compact-support left adjoint \(L\). Its self-fibre is \(\mathbb G_m\). Base change identifies \(FL\) with tensoring by de Rham homology. The Laurent de Rham differential kills all modes except the constant and \(d\log t\); the group pullback makes \(d\log t\) primitive. Dualizing the Hopf model gives the exterior homology algebra \(B=k[\epsilon]\), with \(|\epsilon|=-1\) and primitive Pontryagin generator. The adjunction bar realization is an equivalence after applying \(F\), hence before applying it by conservativity; realizing free \(B\)-module resolutions gives the inverse. Thus the category is \(\operatorname{Mod}_B\). Independently the two-term Koszul resolution at zero of \(k[t]\) gives \(k\otimes^{\mathbf L}_{k[t]}k=B\), proving that this is \(\operatorname{QCoh}(Z_{\mathrm{der}})\). Trivial monodromy sends the constant object to the augmentation \(k\), while \(L(k)\) gives \(B\).

**Exercise 8.4 (medium).** Show that the constant stabilizer object is coherent but not perfect. Distinguish this assertion from the coherence of the full framed-point skyscraper on the local-system stack.

**Solution 8.4.** Its augmentation module has one-dimensional degree-zero cohomology, so it is coherent over \(B\). The resolution (3.3) has generators \(e_j\) of degree \(-2j\) and differentials \(\epsilon e_{j-1}\). After applying \(\operatorname{Hom}_B(-,k)\), it gives nonzero self-Ext in every even degree. A finite cell \(B\)-module, or its retract, has bounded Hom to \(k\); thus \(k\) is not perfect. On the full spectral stack, the framed-point pushforward also has the regular \(B\mathbb G_m\) representation, containing every weight. That representation is infinite-dimensional, so the full point object is not coherent. The coherent nonperfect statement refers to the derived factor, or to an object with finitely many spectral weights, rather than to that full point pushforward.

**Exercise 8.5 (hard).** Compute the Fourier–Mukai image of the structure sheaf of an elliptic curve, stating the source category and shifts. Also compute the trivial connection's image under the de Rham rank-one equivalence.

**Solution 8.5.** For the coherent kernel (7.1), nontrivial degree-zero lines have both \(H^0=0\) and \(H^1=0\), so the transform is supported at the origin of the dual elliptic curve. Its completed perfect model has ranks one in degrees zero and one, because its derived special fibre has those dimensions. The universal first-order Picard deformation obstructs the lift of the section \(1\), giving a nonzero connecting map in \(H^1(\mathcal O)\). Hence the minimal differential is the local parameter \(a\) times a unit. Its only cohomology is the residue field in degree one, so the answer is \(k_0[-1]\). The extra degree-zero fibre cohomology is the derived Tor term and agrees with the cohomology of \(\mathcal O_J\).

For \((\mathcal O_J,d)\) as a D-module, the inverse universal flat-line transform sends the degree-zero point \(k_{e_0}\) to this trivial connection. Its normalized inverse, including the harmless inversion on this particular object, therefore sends the connection to \(k_{e_0}\) in degree zero on \(J^\natural\). This is the answer for the de Rham transform, rather than the coherent transform on \(\widehat J\).

## 9. Proof status and human sources

We proved the degree/weight equivalence, the stabilizer homology algebra and its monadic category, the derived fibre-product algebra, the coherent/nonperfect augmentation calculation, the full categorical matching given the Fourier theorem and geometric splitting, the Hecke compatibility from the universal multiplicative kernel, the framed-point versus residual-gerbe distinction, and the elliptic coherent-transform calculation. The examples and all five exercises are complete.

The full categorical equivalence remains conditional on the following unproved mathematical foundations: recursive Picard/Hilbert and symmetric-product constructions; group projectivity and its line-bundle premises; affine sheaf and coherent cohomology foundations; the local-algebra and ambient Ext premises of trace duality; categorical descent and base change; and the regular-ring, coherent-duality, DG-category and affine/smooth-descent foundations of the torus comparison in §§5.1.1–5.1.8. The algebraic Fourier proof gives universal cohomology, both composition kernels, shifts, arbitrary point-supported D-module complexes and the presentable two-sided inverse within those foundations. Lemma G constructs the dual variety, normalized Poincaré family, universal integrable connection, its identity affine-function class and universal-extension property. It proves Abel self-duality, curve-connection comparison and general abelian biduality over every characteristic-zero field with ordinary-family identities. Sections 4.2.22–4.2.29 add the effective reduced theta divisor, ampleness and \(\phi_\Theta=-\lambda_{\mathrm{Abel}}\), using the explicitly retained geometric and local-algebra premises. The derived Picard and Atiyah/connection/crystal constructions in §§1.1.1–1.1.6 use nonsplit Postnikov squares, nilcompleteness, resolved pointed algebras, finite derived jets and coherent free-bar generation. Sections 1.1.8–1.1.16 identify the dualizing pair with differential forms and give the residue signs, trace chain map, finite-flat pairing and perfect-complex duality on ordinary and connective DG parameters. Sections 5.1.1–5.1.8 supply the full torus zero-support argument on every genus and rank, for all unbounded objects and all character weights, including the dualizing twists in stack descent. Their recursive classical, derived and categorical foundations remain as just listed.

Further reading is [Arinkin–Gaitsgory §11.2](https://arxiv.org/abs/1201.6343), including its torus remark; [Frenkel §§4.4–4.5](https://arxiv.org/abs/hep-th/0512172); [GLC I §1.5](https://arxiv.org/abs/2405.03599), with §1.2 for the vacuum normalization; and [Ben-Zvi §2.4, “Geometric class field theory, or GLC for \(GL_1\)”](https://arxiv.org/abs/2605.23167). The latter survey explicitly suppresses scalar automorphisms in its introductory character-variety picture; we restore them here. The notation “Pic” in the torus product must mean \(J=\operatorname{Pic}^0\), since degrees are already a separate factor.

The dualizing comparison conventions used in §§5.1.5–5.1.7 are also discussed in Gaitsgory, [*Ind-coherent sheaves*, §§5.7, 10.3 and 11.7](https://arxiv.org/abs/1105.4857v7), and Arinkin–Gaitsgory, [*Singular support of coherent sheaves, and the geometric Langlands conjecture*, Theorem 4.2.6, §5.7 and Corollary 8.2.8](https://arxiv.org/abs/1201.6343v4).
