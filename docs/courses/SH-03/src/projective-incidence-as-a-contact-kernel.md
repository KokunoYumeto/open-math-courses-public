# Projective incidence as a contact kernel

A point of a projective space is a line. A point of its dual projective space is a hyperplane. Incidence between them defines a sheaf kernel. We will calculate its cotangent relation, including the input sign, and prove that it gives an equivalence after localization away from the zero covectors. We will also calculate its inverse kernel without discarding the real orientation line.

Use When a kernel quantizes a contact transformation and Dual kernels and an unchanged parameter. Their exact prerequisites include the closed-submanifold microsupport and microlocal Hom formulas and constructible relative duality. Here the projective geometry is calculated directly.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## Lines, hyperplanes and cotangent vectors

Let \(\mathbb F\) be \(\mathbb R\) or \(\mathbb C\), and let \(V\) have dimension \(N\geq2\) over \(\mathbb F\). Put

\[
X=\mathbb P(V),\qquad Y=\mathbb P(V^*),\qquad
Z=\{(\ell,m):m(\ell)=0\}\subset X\times Y.
\qquad\text{(1)}
\]

Here \(m\) is a line of covectors; the notation \(m(\ell)=0\) means that every member of \(m\) vanishes on \(\ell\). In the real case these are ordinary projective lines, with no choice of a positive ray. Let
\(\Omega_X=\dot T^*X\) and \(\Omega_Y=\dot T^*Y\), where a dot removes the zero section.

The coefficient ring \(k\) is commutative with identity and finite global dimension. All sheaf objects are bounded derived complexes of \(k\)-modules. Complex manifolds are regarded as real manifolds for these operations. We identify a complex cotangent vector with a real covector by taking the real part of its pairing; using this convention on both factors preserves the formulas below.

The omitted smaller vector-space dimensions are vacuous for this selected-region assertion. If \(N=0\), both projective spaces are empty. If \(N=1\), both are points, their punctured cotangent spaces are empty, and incidence is empty. The localized categories on an empty cotangent region are zero: every object is null there. All graph and identity conditions on that region hold vacuously. We calculate the nonempty correspondence for \(N\geq2\).

For a line \(\ell\subset V\), differentiation of the graph of a linear map gives

\[
T_\ell X=\operatorname{Hom}_{\mathbb F}(\ell,V/\ell),\qquad
T_\ell^*X=\operatorname{Hom}_{\mathbb F}(V/\ell,\ell).
\qquad\text{(2)}
\]

The second identification uses the trace pairing with the first. Regard a covector in (2) as an endomorphism \(A\) of \(V\). It has image in \(\ell\) and kills \(\ell\). A nonzero such endomorphism has rank one, image exactly \(\ell\), and \(A^2=0\). Conversely a nonzero rank-one square-zero endomorphism determines its base line by its image. Thus

\[
\dot T^*X=\{A\in\operatorname{End}_{\mathbb F}(V):
\operatorname{rank}A=1,\ A^2=0\}.
\qquad\text{(3)}
\]

This description includes the base point; it does not forget it. There is a corresponding description of \(\dot T^*Y\) by endomorphisms \(B\) of \(V^*\).

## The conormal relation and its minus sign

Choose nonzero \(v\in\ell\) and \(\lambda\in m\) at an incident pair, so \(\lambda(v)=0\). In local projective charts, the equation of \(Z\) is \(f(v,\lambda)=\lambda(v)=0\). Its derivative in the \(v\) direction is nonzero: \(\lambda\) induces a nonzero functional on \(V/\ell\). Its derivative in the \(\lambda\) direction is nonzero for the same reason, with \(v\) and \(\lambda\) exchanged. Consequently \(Z\) is a closed smooth submanifold of real codimension
\(c=1\) for \(\mathbb F=\mathbb R\), and \(c=2\) for \(\mathbb F=\mathbb C\).

For a nonzero conormal parameter \(t\in\mathbb F\), the two **physical** cotangent components of \(t\,df\) are

\[
A=t\,v\otimes\lambda,\qquad B_{\mathrm{physical}}=t\,\lambda\otimes v.
\qquad\text{(4)}
\]

For complex \(t\), this means the real covector \(\operatorname{Re}(t\,df)\). These are all the real conormals. Changing projective representatives changes \(t\) inversely to their product, so (4) defines intrinsic covectors. The kernel's input component is the negative of the physical component. Therefore its relation has

\[
B=-t\,\lambda\otimes v,\qquad A=-B^{\mathsf t}.
\qquad\text{(5)}
\]

Here transpose means the canonical dual endomorphism, using \(V^{**}=V\); no inner product or complex conjugation is involved.

Every nonzero rank-one square-zero \(B\) has the form \(-t\lambda\otimes v\). Its image determines \(m\), the image of \(B^{\mathsf t}\) determines \(\ell\), and square-zero says \(\lambda(v)=0\). This proves existence and uniqueness of its point in (4). Recovering these lines is smooth: locally choose a nonzero column of a rank-one matrix to represent its image. These local recovery formulas agree on overlaps. The two nonzero conormal projections are therefore diffeomorphisms, and the kernel transformation is

\[
\chi:\dot T^*Y\longrightarrow\dot T^*X,
\qquad B\longmapsto -B^{\mathsf t}.
\qquad\text{(6)}
\]

The inverse has the same negative-transpose formula with the spaces exchanged. In particular each projection is a proper homeomorphism, even though its domain is not compact.

To verify the symplectic normalization, take a tangent vector to the incidence relation. On it the sum of the physical tautological forms is \(t\,d(\lambda(v))=0\), or its real part in the complex case. Negating the input covector changes this equality to
\(\theta_X-\theta_Y=0\). Since both projections are diffeomorphisms,

\[
\chi^*\theta_X=\theta_Y,\qquad
\chi^*d\theta_X=d\theta_Y.
\qquad\text{(7)}
\]

Formula (6) commutes with positive cotangent dilation. It is a homogeneous symplectic transformation with exactly the sign required for a sheaf kernel.

## Verifying the sheaf criterion

Let \(K=k_Z\), extended by zero to \(X\times Y\). Its smooth closed support and locally perfect constant coefficients give cohomological constructibility in the sense required by the contact-kernel theorem. This also follows locally from the closed-submanifold model: its stalks and costalks are finite shifts of rank-one free modules, with the intrinsic normal orientation line retained.

The exact closed-submanifold prerequisite gives
\(\operatorname{SS}(k_Z)\subset T_Z^*(X\times Y)\). In (4), one cotangent component is nonzero if and only if \(t\ne0\), if and only if the other component is nonzero. Hence the union of the two selected cotangent regions meets this microsupport only in the graph calculated above. This checks the theorem's union condition, rather than checking only the intersection of the regions.

The remaining condition concerns the actual identity. The exact submanifold microlocal Hom formula gives

\[
\mu\operatorname{hom}(k_Z,k_Z)
\simeq\mu_Zk_Z\simeq k_{T_Z^*(X\times Y)}.
\qquad\text{(8)}
\]

For the second comparison, specialization of a sheaf supported on \(Z\) is the constant coefficient sheaf on the zero section of its normal bundle. Negative Fourier transformation of this zero-supported sheaf is constant on the whole dual normal bundle: the fibre integral is over a single point. It has no codimension shift. In each local coefficient chart the identity-induced map sends \(1\) to \(\operatorname{id}_k\), hence to \(1\) in (8). Changing a chart conjugates this endomorphism and fixes its identity. These comparisons glue; no choice of a normal orientation generator enters (8). Thus the identity-induced map is an isomorphism on the selected graph.

All three conditions of the contact-kernel theorem now hold. We obtain inverse localized equivalences

\[
\Phi_{k_Z}:\mathcal D_Y(\dot T^*Y)\rightleftarrows
\mathcal D_X(\dot T^*X):\Psi_{k_Z},
\qquad\text{(9)}
\]

and, for arbitrary bounded inputs \(G_1,G_2\), the theorem's actual natural comparison gives

\[
\chi_*\mu\operatorname{hom}_Y(G_2,G_1)
\simeq\mu\operatorname{hom}_X(\Phi_{k_Z}G_2,\Phi_{k_Z}G_1)
\quad\text{on }\dot T^*X.
\qquad\text{(10)}
\]

The support \(Z\) is compact, so its ordinary support projections are proper too. Properness of the selected conormal projections, used in (9), was proved separately by their homeomorphism property. The result concerns the indicated localizations; it does not assert an equivalence of the full ordinary sheaf categories.

## The inverse kernel retains an orientation line

Write \(P=X\times Y\), let \(q_Y:P\to Y\), and let \(\mathrm t\) exchange the two factors. Put \(D=\dim_{\mathbb R}Y\). Closed-embedding duality gives

\[
R\mathcal Hom_P(k_Z,k_P)
\simeq k_Z\otimes\operatorname{or}_{Z/P}[-c].
\qquad\text{(11)}
\]

Here \(\operatorname{or}_{Z/P}\) is the normal orientation local system, with its exceptional degree written separately. The right relative dual is consequently

\[
K_R=\mathrm t\bigl(k_Z\otimes\operatorname{or}_{Z/P}
\otimes q_Y^{-1}\operatorname{or}_Y\bigr)[D-c].
\qquad\text{(12)}
\]

Convolution with (12) realizes \(\Psi_{k_Z}\) in (9). The dual-kernel theorem identifies the operators by its specified adjunction comparison, so this inverse is normalized by that adjunction.

In the complex case both orientation systems are canonically trivial. Since \(D=2N-2\) and \(c=2\), the inverse is
\(k_{Z^{\mathsf t}}[2N-4]\).
In the real case its degree is \(N-2\), but its line need not be trivial. To see the line precisely, let \(O_\ell\) and \(O_m\) denote the sign orientation systems of the tautological real lines on the two projective factors. The normal equation is a section of \(\ell^*\otimes m^*\), so
\(\operatorname{or}_{Z/P}=O_\ell\otimes O_m\).
Also (2) gives
\(\det TY\simeq\det V^*\otimes m^{-N}\).
Thus the line before transposition in (12) is

\[
\operatorname{or}_{V^*}\otimes O_\ell\otimes O_m^{\otimes(N+1)}
\quad\text{on }Z.
\qquad\text{(13)}
\]

The orientation of the fixed vector space \(V^*\) is a constant line. Orientation sign systems are their own inverses, which explains why the negative tensor powers from the determinant formula give the positive powers in (13). A coordinate choice can trivialize a constant line; it cannot erase nontrivial monodromy in \(O_\ell\) or \(O_m\).

## Exercises with complete solutions

### Recovering the input sign

*Difficulty: Introductory.*

For \(V=\mathbb R^3\), take \(v=e_1\), \(\lambda=e_2^*\) and \(t=2\). Write the physical conormal pair and the input endomorphism. Check square-zero and the formula for \(\chi\).

**Solution.** The physical pair is \((2e_1\otimes e_2^*,2e_2^*\otimes e_1)\). The input is \(B=-2e_2^*\otimes e_1\). The first endomorphism sends \(e_2\) to \(2e_1\) and kills \(e_1\); the input sends \(e_1^*\) to \(-2e_2^*\) and kills \(e_2^*\). Both have square zero and rank one. Finally \(-B^{\mathsf t}=2e_1\otimes e_2^*\), the required output. Using the physical second component without the antipode would give the opposite sign.

### Incidence on a real projective line

*Difficulty: Intermediate.*

When \(V=\mathbb R^2\), show that incidence is the graph of a diffeomorphism between the two projective lines. Explain why the inverse kernel has degree zero and a trivial total orientation line.

**Solution.** A nonzero covector has a one-dimensional kernel. Thus \(m\mapsto\ker m\) is a bijection \(Y\to X\); its inverse sends a line to its annihilator line. Both maps are smooth in projective coordinate charts. Hence \(Z\) is its graph and the transform is pushforward along this diffeomorphism. The graph has real codimension one in the two-dimensional product, and \(Y\) has dimension one, so \(D-c=0\). Its normal orientation is the pullback of the orientation of \(Y\); tensoring it with that same orientation in (12) cancels it canonically. The inverse is the unshifted sheaf of the transposed graph, as ordinary graph calculus also shows.

### A complex projective plane

*Difficulty: Intermediate.*

For \(V=\mathbb C^3\), calculate the inverse degree. Explain why complex codimension must be converted before applying (11).

**Solution.** The dual projective plane has complex dimension two and real dimension four. Incidence has complex codimension one and real codimension two. The inverse degree is \(4-2=2\), so the right relative dual is \(k_{Z^{\mathsf t}}[2]\). A closed complex hypersurface has exceptional degree \(-2\) in real sheaf theory. Substituting complex codimension one into the real formula would give degree three and would use the wrong duality normalization. Complex orientations canonically trivialize the two orientation lines.

### Why zero covectors are excluded

*Difficulty: Intermediate.*

Assume \(N\geq3\). Show directly that the conormal relation does not have a graph projection over a zero covector of \(X\). Relate this to ordinary constant sheaves.

**Solution.** At \((\ell;0)\), parameter \(t=0\) is possible for every hyperplane containing \(\ell\). These hyperplanes form \(\mathbb P((V/\ell)^*)\), of positive dimension \(N-2\). Thus the projection has more than one point in this fibre. The nonzero recovery argument cannot be extended to it. A locally constant bounded sheaf has microsupport in the zero section and becomes zero in the selected localization. Hence (9) omits precisely such ordinary information; it does not prove an equivalence before localization. For \(N=2\) the incidence graph has the separate ordinary equivalence calculated in the previous exercise.

### A real orientation that cannot be dropped

*Difficulty: Advanced.*

Let \(V=\mathbb R^3\) and take \(k\) to be a field of characteristic different from two. Fix \(m\in Y\). Determine the monodromy of the inverse line along the fibre \(\{\ell\subset\ker m\}\simeq\mathbb R\mathbb P^1\) of \(Z\to Y\).

**Solution.** In (13), \(N+1=4\), so the fourth tensor power of \(O_m\) is trivial. On the specified fibre it is constant in any case. The fixed line \(\operatorname{or}_{V^*}\) is also constant. The remaining factor is \(O_\ell\), the tautological sign system on \(\mathbb R\mathbb P^1\). A lift of one circuit in the projective line changes a unit vector representing \(\ell\) to its negative; transport on this orientation line is multiplication by \(-1\). It is nontrivial over the stated field. The inverse degree is one, but replacing (12) by \(k_{Z^{\mathsf t}}[1]\) would lose this monodromy. In characteristic two this particular sign obstruction disappears, which is why the coefficient hypothesis matters for the example.
