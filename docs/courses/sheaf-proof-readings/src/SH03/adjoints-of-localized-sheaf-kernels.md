# Adjoints of localized sheaf kernels

A kernel operator integrates along its first projection with proper supports. Its right adjoint uses internal Hom, exceptional inverse image and ordinary direct image. These operations have different variance and different compactness requirements. We will identify the cotangent condition that lets the adjoint retain a chosen input region, then descend the ordinary adjunction itself to localized categories.

Use the notation and forward admissibility condition of Kernels that preserve chosen cotangent directions. The ordinary kernel adjunction, including its unit and counit, is a prerequisite from Composing sheaf operators through an intermediate space. The bounded-Hom and orientation inputs below come from Local orientations, dimension, and integration. We continue to use the general enlarged Hom estimate and the microlocal proper-image theorem, with the exact hypotheses recalled in the preceding lesson.

*Original programme exposition by GPT-6.1 Sol (OpenAI), Ultra, September 2026; source comparison and editorial revision by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently expressed programme text is dedicated under CC0. Human sources retain their own terms.*

## The ordinary adjoint stays bounded

Let \(k\) be an arbitrary commutative unital ring of finite global dimension at most \(g\). Manifolds are smooth, Hausdorff, finite dimensional and countable at infinity. We work with globally bounded complexes of arbitrary sheaves of \(k\)-modules. No constructibility, perfect-stalk, finite-generation or Noetherian hypothesis is imposed.

For the two projections \(q_1:X\times Y\to X\) and \(q_2:X\times Y\to Y\), the ordinary operators are

\[
\Phi_K(G)=Rq_{1!}(K\otimes^Lq_2^{-1}G),
\qquad
\Psi_K(F)=Rq_{2*}R\mathcal Hom(K,q_1^!F).
\tag{1}
\]

The ordinary adjunction \(\Phi_K\dashv\Psi_K\) is imported with its structural maps. It holds on the bounded-below range provided by the ordinary kernel calculus. To use its restriction to bounded categories, we need an additional upper bound for internal Hom.

Here are the precise manifold inputs. On an \(m\)-manifold, bounded complexes \(A\in D^{[a,b]}\), \(B\in D^{[c,d]}\) satisfy

\[
R\mathcal Hom(A,B)
\in D^{[c-b,\ d-a+3m+g+1]}.
\tag{2}
\]

This safe uniform bound applies to arbitrary cohomology sheaves. It is not a perfect-dual tensor formula. Every open subset of an \(m\)-manifold has sheaf cohomological dimension at most \(m\). For a submersion of relative dimension \(n\), exceptional inverse image is tensoring ordinary inverse image with the relative orientation line shifted by \([n]\).

In particular, with \(n_Y=\dim Y\) and \(m=\dim X+\dim Y\),

\[
q_1^!F\simeq q_1^{-1}F\otimes^Lq_2^{-1}\omega_Y,
\qquad \omega_Y=\operatorname{or}_Y[n_Y].
\tag{3}
\]

No orientation of \(Y\) has been chosen. Its orientation line is locally free of rank one, so tensoring with it is exact. In the convention \(H^j(F[s])=H^{j+s}(F)\), a shift by \([n_Y]\) lowers the cohomological interval by \(n_Y\).

**Proposition 1.** Both operators in (1) preserve boundedness. More explicitly, if \(K\in D^{[a,b]}\) and \(F\in D^{[c,d]}\), then

\[
\Psi_K(F)\in
D^{[c-n_Y-b,\ d-n_Y-a+4m+g+1]}.
\tag{4}
\]

**Proof.** Formula (3) places \(q_1^!F\) in \([c-n_Y,d-n_Y]\). Apply (2) on \(X\times Y\): its internal Hom with \(K\) lies in
\([c-n_Y-b,d-n_Y-a+3m+g+1]\).

For every open \(V\subset Y\), its preimage \(X\times V\) is an \(m\)-manifold. The uniform cohomology bound makes \(R^jq_{2*}A=0\) for \(j>m\) for every sheaf \(A\): these sheaves are obtained by sheafifying \(V\mapsto H^j(X\times V;A)\). The finite hypercohomology filtration therefore adds at most \(m\) to the upper bound and preserves the lower bound. This gives (4). The proper-support kernel bound already proves boundedness of \(\Phi_K\). These are deliberately uniform bounds; their numerical size is not asserted optimal. \(\square\)

Thus the ordinary adjunction restricts to \(D^b(k_Y)\) and \(D^b(k_X)\), without replacing arbitrary sheaves by constructible ones.

## Reversing the cotangent condition

Let \(\Omega_X\subset T^*X\) and \(\Omega_Y\subset T^*Y\) be open; they may contain zero covectors and need not be conic. The relation relevant to the right adjoint is

\[
\mathcal R_K=
\{((x,\xi),(y,\alpha)):
(x,y;\xi,-\alpha)\in\operatorname{SS}(K),\ (y,\alpha)\in\Omega_Y\}.
\tag{5}
\]

We impose the **reverse condition**

\[
\mathcal R_K\subset\Omega_X\times\Omega_Y,
\qquad \mathcal R_K\longrightarrow\Omega_Y
\quad\text{proper}.
\tag{6}
\]

It controls the \(X\) point and covector over a compact set of \(Y\) covectors. The forward condition controls the other projection. Neither condition implies the other.

For a comparison with factor transposition, write \(\mathrm tK=r_*K\) for \(r(x,y)=(y,x)\). A covector \((x,y;\xi,-\alpha)\) becomes \((y,x;-\alpha,\xi)\). With the twisted input convention on \(Y\times X\), its output is \((y,-\alpha)\) and its input is \((x,-\xi)\). Consequently (6) is precisely forward admissibility of \(\mathrm tK\) from \(\Omega_X^a\) to \(\Omega_Y^a\), where \(a\) negates covectors. Transposition by itself does not turn the right adjoint into a tensor-kernel transform.

## Internal Hom has no escaping covectors in the reverse region

The mechanism in Lemma 2 and Theorem 3 is the proper-covector argument of Kashiwara and Schapira, *Microlocal Study of Sheaves*, Proposition 6.3.1 and its proof, printed pp. 108–109. A convergent covector in the chosen region places the kernel covector in a compact inverse image; the remaining summand is then bounded by subtraction. The proof below writes this argument for the reverse relation, the exceptional orientation coefficient and the ordinary right adjoint. Its compact neighborhoods also explain why conicity of the chosen open region is unnecessary here.

Set \(J=R\mathcal Hom(K,q_1^!F)\). By (3), tensoring ordinary inverse image with an invertible shifted local system does not change microsupport. Hence

\[
\operatorname{SS}(q_1^!F)
=\{(x,y;\lambda,0):(x,\lambda)\in\operatorname{SS}(F)\}.
\tag{7}
\]

The general internal-Hom estimate gives

\[
\operatorname{SS}(J)
\subset\operatorname{SS}(q_1^!F)\widehat+
\operatorname{SS}(K)^a.
\tag{8}
\]

The antipodal map in (8) negates **both** components of the kernel covector. It comes from contravariance in the first argument of internal Hom, and is distinct from the convention that negates just the input when defining a relation.

**Lemma 2.** Under (6), on the region where the \(Y\) covector belongs to \(\Omega_Y\), the enlarged sum in (8) is the ordinary sum.

**Proof.** A sequence for that enlarged sum has covector components

\[
(\lambda_n,0)+(-\xi_n,-\eta_n)
\longrightarrow(\nu_0,\alpha_0),
\qquad (y_0,\alpha_0)\in\Omega_Y.
\]

Its two base sequences approach \((x_0,y_0)\). In particular, the kernel's input covectors \((y_n,-\eta_n)\) tend to \((y_0,\alpha_0)\). Put them, from some point onward, in a compact neighborhood \(E\subset\Omega_Y\). Condition (6) puts the corresponding kernel covectors in a compact set. Thus \(\xi_n\) is bounded. Since \(\lambda_n-\xi_n\to\nu_0\), \(\lambda_n\) is bounded too. The \(Y\) component was already convergent. Passing to a subsequence and using closedness gives actual same-base covectors whose sum is \((\nu_0,\alpha_0)\). Constant sequences prove the reverse inclusion. The weighted-distance condition introduces no new point, because both summands are bounded. \(\square\)

This proves the concrete estimate

\[
\begin{split}
\operatorname{SS}(J)\cap(T^*X\times\Omega_Y)
\subset\{(x,y;\lambda-\xi,\alpha):\
(x,\lambda)\in\operatorname{SS}(F),\\
((x,\xi),(y,\alpha))\in\mathcal R_K\}.
\end{split}
\tag{9}
\]

## The right transform descends

**Theorem 3.** If \(K\) satisfies the reverse condition, the canonical comparison

\[
Rq_{2!}R\mathcal Hom(K,q_1^!F)
\longrightarrow\Psi_K(F)
\tag{10}
\]

is an isomorphism in \(\mathcal D_Y(\Omega_Y)\). Moreover,

\[
\operatorname{SS}(\Psi_KF)\cap\Omega_Y
\subset\{v\in\Omega_Y:\exists u\in\operatorname{SS}(F)\cap\Omega_X,
\ (u,v)\in\mathcal R_K\}.
\tag{11}
\]

Thus \(\Psi_K\) defines an exact functor \(\mathcal D_X(\Omega_X)\to\mathcal D_Y(\Omega_Y)\).

**Proof.** For a compact \(E\subset\Omega_Y\), its preimage in \(\mathcal R_K\) is compact. Project that preimage to \(X\), obtaining a compact \(B_E\). Formula (9) shows that every covector of \(J\) whose \(Y\) component lies in \(E\) has its \(X\) base point in \(B_E\). This holds for every \(X\) covector \(\lambda-\xi\), not just zero. It is the all-fibre-covector compact-control hypothesis of the microlocal proper-image theorem for \(q_2\), with \(X\) now the integrated fibre. Equivalently, the closure of the projection of \(\operatorname{SS}(J)\), after forgetting the \(X\) covector, is proper over \(\Omega_Y\).

That theorem proves (10), for the canonical arrow. In its microsupport estimate, the \(X\) covector in (9) must be zero, so \(\lambda=\xi\). Condition (6) already places \((x,\xi)\) in \(\Omega_X\). This gives (11).

If the microsupport of \(F\) misses \(\Omega_X\), the right side is empty. Since \(\Psi_K\) is exact, it takes the cone of every denominator in the input category to an invisible cone in the output category. The quotient's universal property therefore gives the stated exact functor. \(\square\)

The conclusion is an isomorphism in the chosen cotangent region. It does not identify proper and ordinary direct image globally.

## Descending the adjunction maps

Assume now that \(K\) satisfies **both** the forward and reverse conditions. The previous lesson gives localized \(\Phi_K\), and Theorem 3 gives localized \(\Psi_K\).

**Theorem 4.** These localized functors are adjoint:

\[
\operatorname{Hom}_{\mathcal D_X(\Omega_X)}(\Phi_KG,F)
\simeq
\operatorname{Hom}_{\mathcal D_Y(\Omega_Y)}(G,\Psi_KF).
\tag{12}
\]

The adjunction uses the images of the ordinary kernel unit and counit.

**Proof.** Denote those ordinary maps by

\[
\eta:\mathrm{id}\longrightarrow\Psi_K\Phi_K,
\qquad
\epsilon:\Phi_K\Psi_K\longrightarrow\mathrm{id}.
\tag{13}
\]

They satisfy the two triangle identities. Both functors take the respective null subcategory into the other one, as their microsupport estimates proved. Their composites therefore do so too. Applying the quotient functors to (13) defines transformations between the descended functors.

Naturality holds for an ordinary arrow before localization. It also holds for the inverse of every denominator: the two sides of the naturality square for that denominator can be multiplied by its inverse and the inverse of its image. A localized morphism is a composite of ordinary arrows and inverted denominators. Thus these transformations are natural for all localized morphisms. Their triangle identities remain true because localization preserves compositions and identities.

For completeness, the descended maps give explicit inverse Hom maps. Send \(u:\Phi_KG\to F\) to \(\Psi_K(u)\eta_G\). Send \(v:G\to\Psi_KF\) to \(\epsilon_F\Phi_K(v)\). For the first composite, naturality of \(\epsilon\) and its triangle identity give

\[
\epsilon_F\Phi_K\Psi_K(u)\Phi_K(\eta_G)
=u\epsilon_{\Phi_KG}\Phi_K(\eta_G)=u.
\]

For the other composite, naturality of \(\eta\) and its triangle identity give

\[
\Psi_K(\epsilon_F)\Psi_K\Phi_K(v)\eta_G
=\Psi_K(\epsilon_F)\eta_{\Psi_KF}v=v.
\]

The maps are natural in \(G,F\), establishing (12). This proof concerns quotient Hom sets and does not assume that they equal the global sections of microlocal Hom. \(\square\)

## The order of a composite right adjoint

Let \(L\) be a kernel on \(Y\times Z\) satisfying the reverse condition from \(\Omega_Y\) to \(\Omega_Z\), while \(K\) satisfies it from \(\Omega_X\) to \(\Omega_Y\). Then

\[
\Psi_{K\circ_YL}\simeq\Psi_L\Psi_K:
\mathcal D_X(\Omega_X)\longrightarrow\mathcal D_Z(\Omega_Z).
\tag{14}
\]

Here is why the composite has the required reverse condition even without assuming the forward conditions. The transposed kernels \(\mathrm tL\) and \(\mathrm tK\) are forward admissible on the antipodal regions. Ordinary convolution, with its tensor symmetry, gives

\[
\mathrm t(K\circ_YL)\simeq(\mathrm tL)\circ_Y(\mathrm tK).
\tag{15}
\]

Its right side is forward admissible by the composition theorem. Thus the untransposed composite satisfies the reverse condition. Formula (15) includes the Koszul symmetry; no sign-free exchange of two arbitrary complexes is asserted.

At the ordinary level, \(\Psi_L\Psi_K\) and \(\Psi_{K\circ_YL}\) are right adjoints to the same composite left operator, by ordinary convolution. The unique isomorphism respecting their adjunctions supplies (14) before localization. The reverse-condition estimates let this natural isomorphism descend. When all forward conditions also hold, it is the corresponding isomorphism between the localized right adjoints from Theorem 4. Reversing the order is essential: an arrow returning from \(X\) to \(Z\) passes through \(Y\).

## Exercises with solutions

### A shifted change of coordinates

*Difficulty: Intermediate.*

Let \(f:Y\to X\) be a diffeomorphism, \(K=k_{\Gamma_f}[s]\), and let the two cotangent regions correspond under the cotangent lift. Identify \(\Psi_K\), check both properness conditions, and determine its action on a nonzero degree-zero sheaf.

**Solution.** The graph relation is \(((f(y),\xi),(y,df_y^t\xi))\). Its two projections onto the corresponding regions are homeomorphisms, so both are proper. The forward functor is \(f_*[s]\). Since \(f_*\) is an equivalence with inverse \(f^{-1}\), its right adjoint is \(f^{-1}\); the right adjoint of \([s]\) is \([-s]\). Hence \(\Psi_K=f^{-1}[-s]\). A nonzero degree-zero sheaf is sent to degree \(s\). A graph's positive-dimensional ambient embedding does not add a dimension correction to the operator of a diffeomorphism.

### A torsion kernel at a point

*Difficulty: Introductory.*

Take \(X=Y=\{\mathrm{pt}\}\), \(k=\mathbb Z\), and \(K=\mathbb Z/7\) in degree zero. Find \(\Psi_K(\mathbb Z)\). Explain why degree-zero ordinary Hom gives the wrong answer.

**Solution.** Both cotangent conditions are automatic on the one-point cotangent spaces. The right operator is derived module Hom. A two-term free resolution gives \(\operatorname{Hom}(\mathbb Z/7,\mathbb Z)=0\), \(\operatorname{Ext}^1(\mathbb Z/7,\mathbb Z)=\mathbb Z/7\), and zero higher Ext. Thus \(\Psi_K(\mathbb Z)\simeq\mathbb Z/7[-1]\), with nonzero cohomology in degree one. Ordinary Hom would erase this object. Neither replacing coefficients by a field nor omitting the derived Hom is legitimate.

### One projection condition without the other

*Difficulty: Advanced.*

Let \(f(y)=y^2\) on the real line, \(K=k_{\Gamma_f}\), and \(k\ne0\). Choose \(\Omega_X=T^*\{x>0\}\), \(\Omega_Y=T^*\{y>0\}\), as open subsets of the cotangent bundles of the full lines. Show that the reverse condition holds but the forward condition fails. Test the proposed forward descent with a skyscraper at \(y=-1\).

**Solution.** The twisted relation is \(x=y^2\), \(\alpha=2y\xi\). Over \(y>0\), its output lies in \(x>0\). A compact set of inputs in \(\Omega_Y\) bounds \(y\) away from zero and bounds \(y,\alpha\); hence it bounds \(x=y^2\) and \(\xi=\alpha/(2y)\). The relation above it is closed and compact. This proves the reverse condition.

For a positive \(x\), the full graph relation has both \(y=\sqrt x\) and \(y=-\sqrt x\). The latter is outside \(\Omega_Y\), so forward containment fails. Indeed \(k_{\{-1\}}\) is zero in \(\mathcal D_Y(\Omega_Y)\), while its proper image is \(k_{\{1\}}\), nonzero in \(\mathcal D_X(\Omega_X)\). Thus the forward functor cannot descend for this choice. The right functor does descend; on the selected positive branch, \(f\) is a diffeomorphism and its exceptional inverse image agrees with ordinary inverse image there. This does not assert an unshifted inverse-image formula at the critical point zero, which is outside these base regions.

### The orientation factor survives an adjoint

*Difficulty: Intermediate.*

Let \(X=\{\mathrm{pt}\}\), let \(Y\) be a compact \(n\)-manifold, and let \(K=k_Y\). Take the full cotangent regions. Identify \(\Phi_K\) and \(\Psi_K\), and specialize to \(Y=\mathbb{RP}^2\), \(k=\mathbb Z\).

**Solution.** The relation is the zero section of \(T^*Y\) paired with the point. Its projection to the point is proper because \(Y\) is compact; its projection to \(T^*Y\) is a closed embedding and is proper. Both conditions hold. The left functor is \(R\Gamma_c(Y;-)=R\Gamma(Y;-)\). Since \(q_2\) is the identity and internal Hom from \(k_Y\) is the identity, the right functor is \(F\mapsto\omega_Y\otimes^LF_Y\), with \(\omega_Y=\operatorname{or}_Y[n]\).

For the real projective plane it is \(\operatorname{or}_Y[2]\otimes F_Y\). With integral coefficients the orientation line has monodromy \(-1\) on the nontrivial loop. It cannot be discarded by choosing local coordinates, and the shift places a degree-zero coefficient module in degree \(-2\). This is the adjoint to integration, not the unshifted constant-sheaf functor.

## References

**Sources and the proof they supply.** Kashiwara and Schapira's [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Theorem 4.4.2 and proof, printed pp. 75–76, compare proper and ordinary image under properness after forgetting the integrated fibre covector. This is why Theorem 3 controls all such covectors, rather than only the zero fibre covector used in the final image estimate. Proposition 6.3.1, pp. 108–109, combines that theorem with boundedness of summand covectors; Remark 6.3.2 gives the tensor variant. The source works with bounded kernels, bounded-below targets and conic open regions at this point. This lesson proves its stated bounded restriction and uses compact neighborhoods in arbitrary open regions, including regions meeting the zero section.

The ordinary right-adjoint formula comes from exceptional adjunction, tensor–Hom adjunction and ordinary inverse/direct-image adjunction. Pierre Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), edition dated 01/08/2026, Theorem 4.6.1 and Propositions 4.6.5–4.6.9, pp. 94–97, give the exceptional and internal-Hom maps; Definition 5.1.4 and Proposition 5.1.9, pp. 107–108, give the orientation complex and the submersion formula by a local product calculation. The existence theorem invokes Brown representability. That invocation remains a foundation input, and these passages do not establish this lesson's numerical bound for arbitrary internal Hom. The exact supplier of that bound is the bounded-Hom proof in Local orientations, dimension, and integration.

Astérisque 128, §6.1, pp. 103–105, constructs the quotient by microsupport-invisible objects and states its triangulated universal property. It also distinguishes quotient morphisms from sections of microlocal Hom on an open region. Theorem 4 therefore descends the actual unit and counit, proves their naturality for inverted denominators, and checks both Hom-map composites. It does not use an identification with sections of microlocal Hom. Proposition 6.3.3, pp. 110–111, supplies the classical composition framework; here the reversed order of right adjoints is identified by the ordinary adjunction and transported through the quotient.

The proofs are organized around the adjoint's successive obligations: an upper cohomological bound, reverse compact control, invisibility of denominator cones, and the structural adjunction maps. The four solved tests distinguish a shift, a derived torsion Hom, one-sided properness, and a nontrivial orientation line. The general enlarged-Hom estimate, microlocal proper-image theorem, ordinary kernel calculus and bounded-Hom theorem remain the named prerequisites used in the text. The passages compared here do not provide a new proof of every transitive foundation. Their onward references have not been followed for this lesson, and no source expression or source figure is reproduced or relicensed.

- Masaki Kashiwara and Pierre Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985), §4.4, §6.1 and §6.3, at the locators above.
- Pierre Schapira, *An Introduction to Sheaves on Grothendieck Topologies*, edition dated 01/08/2026, §§4.6–4.7 and §5.1, at the locators above.
