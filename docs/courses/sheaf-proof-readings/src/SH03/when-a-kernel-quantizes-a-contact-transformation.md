# When a kernel quantizes a contact transformation

A cotangent correspondence can be a graph even when the corresponding sheaf operator loses information. The missing condition is an identity condition on the kernel's directional endomorphisms. In this lesson we prove that condition sufficient for an equivalence, and explain how the equivalence transports the entire sheaf of directional morphisms.

Use Dual kernels and an unchanged parameter and Directional morphisms through a sheaf kernel. Two additional inputs come from Local models and change of ambient manifold and Local morphisms in cotangent directions: the conormal coefficient model, and the microlocal unit, duality and submanifold formulas. We state exactly what is needed. Their foundational proofs remain prerequisites.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## The correspondence and the identity condition

The coefficient ring \(k\) is commutative with identity and finite global dimension. Manifolds are smooth, Hausdorff, finite dimensional and countable at infinity. Objects are globally bounded complexes of sheaves of \(k\)-modules. Cohomological constructibility has the formal-system and perfect stalk/costalk meaning stated in the dual-kernel lesson; mere boundedness does not imply it.

Write \(P=X\times Y\),
\(p_1(x,y;\xi,\eta)=(x;\xi)\), and
\(p_2^a(x,y;\xi,\eta)=(y;-\eta)\).
Suppose \(\Lambda\subset\Omega_X\times\Omega_Y^a\) is a relatively closed conic correspondence whose two projections

\[
p_1:\Lambda\xrightarrow{\sim}\Omega_X,
\qquad p_2^a:\Lambda\xrightarrow{\sim}\Omega_Y
\tag{1}
\]

are homeomorphisms. Set
\(\chi=p_1\circ(p_2^a|_\Lambda)^{-1}\).
For now only the topology of this graph matters. When \(\Lambda\) is smooth Lagrangian and the two projections are diffeomorphisms, \(\chi\) is a homogeneous symplectic, or contact, transformation.

Let \(K\in D^b(k_P)\) satisfy the following three conditions:

1. \(K\) is cohomologically constructible.
2. In either selected cotangent region, its microsupport is contained in the same graph:

   \[
   \operatorname{SS}(K)\cap
   \bigl(p_1^{-1}\Omega_X\cup(p_2^a)^{-1}\Omega_Y\bigr)
   \subset\Lambda.
   \tag{2}
   \]

3. The **identity-induced** morphism is an isomorphism:

   \[
   e_K:k_\Lambda\xrightarrow{\sim}
   \mu\operatorname{hom}_P(K,K)|_\Lambda.
   \tag{3}
   \]

The map in (3) is obtained from \(\operatorname{id}_K\), using the microlocal unit. An abstract isomorphism with a constant complex is not the stated condition. In particular, the normalization of its identity section is retained.

**Theorem 1.** Under (1)–(3), the localized operators

\[
\Phi_K:\mathcal D_Y(\Omega_Y)\longrightarrow\mathcal D_X(\Omega_X),
\qquad
\Psi_K:\mathcal D_X(\Omega_X)\longrightarrow\mathcal D_Y(\Omega_Y)
\tag{4}
\]

are inverse equivalences. For all bounded \(G_1,G_2\), there is a natural isomorphism

\[
\chi_*\bigl(\mu\operatorname{hom}_Y(G_2,G_1)|_{\Omega_Y}\bigr)
\simeq
\mu\operatorname{hom}_X(\Phi_KG_2,\Phi_KG_1)|_{\Omega_X}.
\tag{5}
\]

The direct image in (5) is by a homeomorphism, so it is exact. Both sides depend only on the indicated localized input objects.

## Detecting a cone supported in a conormal

Here is the exact use of the local coefficient-model prerequisite. If \(S\subset M\) is a closed smooth submanifold and a bounded complex \(C\) has microsupport contained in \(T_S^*M\) near \(p\in T_S^*M\), then

\[
C\simeq A_S\quad\text{in }\mathcal D_M(\{p\})
\tag{6}
\]

for some bounded complex \(A\) of \(k\)-modules. This is local at the conormal point. It permits arbitrary modules and makes no assertion about an ordinary neighborhood of the original sheaf.

The submanifold formula and specialization of a supported coefficient complex give

\[
\mu\operatorname{hom}_M(k_S,C)=\mu_SC,
\qquad \mu_S(A_S)\simeq\pi^{-1}A
\quad\text{on }T_S^*M.
\tag{7}
\]

The second formula has no codimension shift: specialization of \(A_S\) is supported on the zero section of the normal bundle, and its negative Fourier transform is the coefficient complex on the whole dual normal bundle. The first formula uses the specified conormal identification and the closed-embedding comparison.

Consequently \((\mu_SC)_p=0\) implies \(C=0\) in the localization at \(p\), whenever the conormal-containment hypothesis holds. Indeed microlocal Hom inverts denominators in its second argument by its support bound, so (6) and (7) identify this stalk with \(A\). If it is zero, the coefficient model is zero and so is \(C\) at \(p\).

We will apply this to the cone of a map of diagonal kernels. It would be false to treat ordinary cotangent projection recovery as conservative on every conic sheaf; the conormal hypothesis is what makes this particular detection work.

## The adjunction in the presence of a parameter

Condition (2) and the two homeomorphisms in (1) make \(K\) both forward and reverse admissible. Each relevant restricted relation is a relatively closed subset of a graph whose two projections are proper homeomorphisms. Thus both operators descend, and \(\Phi_K\dashv\Psi_K\).

Let \(Z\) be another manifold. The parameter kernel \(\Theta_ZK\) acts between \(Y\times Z\) and \(X\times Z\), on regions \(\Omega_Y\times T^*Z\) and \(\Omega_X\times T^*Z\). Its relation is contained in the graph of
\(\chi_Z=\chi\times\operatorname{id}_{T^*Z}\).
It is admissible in both directions. Apply the two microlocal Hom comparisons to this kernel. Their common intermediate sheaf is supported on that graph, because the first input of its microlocal Hom is \(\Theta_ZK\). Projection along the two sides of a graph is then just transport by \(\chi_Z\). We obtain

\[
\chi_{Z*}\mu\operatorname{hom}(G,\Psi_{\Theta_ZK}F)
\simeq
\mu\operatorname{hom}(\Phi_{\Theta_ZK}G,F)
\tag{8}
\]

on \(\Omega_X\times T^*Z\).

To justify the support argument without losing ordinary direct-image information, let \(i\) be the closed graph embedding inside the selected cotangent correspondence. A complex with closed support in this graph equals \(i_*i^{-1}\) of that complex by the open–closed triangle. The two restricted projections composed with \(i\) are homeomorphisms. Applying their ordinary direct images therefore produces (8), even if the original cotangent projections are not globally proper.

We also need to identify the operator on the left. With

\[
K_R=\mathrm tR\mathcal Hom(K,q_2^{-1}\omega_Y),
\tag{9}
\]

the dual-kernel theorem and parameter identity give

\[
\Psi_{\Theta_ZK}(F)\simeq K_R\circ_XF.
\tag{10}
\]

Here the constructibility of \(K\) is essential. For completeness, relative duality commutes with this parameter identity with no added \(Z\)-shift. The ordinary coefficient dual of the diagonal factor is its constant sheaf tensored by the relative orientation complex of the diagonal, of degree \(-\dim Z\). The right relative dual also tensors by the input factor \(\omega_Z\), of degree \(\dim Z\). These cancel, together with their inverse orientation lines. External constructible duality and the tensor symmetry then identify the right dual of \(\Theta_ZK\) with \(\Theta_ZK_R\). This computation also proves its required constructibility from that of \(K\) and of a smooth closed diagonal. Apply the dual-kernel theorem and then the parameter convolution identity to obtain (10).

The maps in (8) preserve the adjunction's units. More precisely, the image of
\(\eta_G:G\to\Psi_{\Theta_ZK}\Phi_{\Theta_ZK}G\)
under the directional adjunction is the identity of \(\Phi_{\Theta_ZK}G\). Here is the map check being used. Before specialization, represent a morphism by its diagonal Hom kernel. Its adjoint is obtained by inserting the kernel unit, then applying the given morphism inside the right operator. Applying the inverse construction evaluates against the kernel and its proper-support counit. In the fourfold comparison these are the same evaluation and counit, after the exceptional repeated-coordinate restriction. The inserted unit followed by that counit is the identity by the triangle identity. Specialization and Fourier transformation send this equality of actual kernel maps to equality of the directional maps. The orientation cancellations are the ones displayed in the preceding lesson; the remaining maps are the specified adjunction mates. Thus the identity here is checked before normal limits, not inferred from equality after ordinary cotangent recovery.

## The kernel unit is invertible

Take \(Z=Y\), \(G=k_{\Delta_Y}\), and \(F=K\) in (8). The parameter identity gives
\(\Phi_{\Theta_YK}(k_{\Delta_Y})=K\), and (10) gives
\(\Psi_{\Theta_YK}(K)\simeq K_R\circ_XK\).
The unit at the diagonal is therefore the actual kernel morphism

\[
\alpha:k_{\Delta_Y}\longrightarrow K_R\circ_XK
\tag{11}
\]

in the localization on \(\Omega_Y\times T^*Y\). By the map check above, (8) sends its microlocalized section to the identity section of \(K\).

One can also construct (11) directly. On \(X\times Y_1\times Y_2\), the operator's Hom kernel is
\(R\mathcal Hom(K_{XY_1},K_{XY_2}\otimes\omega_{Y_1})\).
Let \(j(x,y)=(x,y,y)\). Exceptional restriction changes this kernel to
\(R\mathcal Hom(K,K)\): the repeated-coordinate relative orientation cancels \(\omega_{Y_1}\). The identity of \(K\) thus gives a morphism from the diagonal-supported constant sheaf into the Hom kernel by closed-embedding adjunction. Push it ordinarily along \(X\) and use the identification (10). This is (11). It is the unit because its ordinary adjoint is \(\operatorname{id}_K\). This direct construction retains the exceptional cancellation and specifies the same map used in (8).

Restrict (8) to

\[
\{(y,y;\alpha,-\alpha):(y;\alpha)\in\Omega_Y\}
\subset T^*_{\Delta_Y}(Y^2).
\tag{12}
\]

The right side is the self microlocal Hom of \(K\) on \(\Lambda\). The left side is the microlocal Hom from \(k_{\Delta_Y}\) to the target of (11) on (12). Formula (7) identifies it with diagonal microlocalization. Under this identification, \(\mu_{\Delta_Y}\alpha\) is exactly (3), transported by the graph homeomorphism. It is therefore an isomorphism.

The convolution microsupport estimate gives

\[
\operatorname{SS}(K_R\circ_XK)
\cap(\Omega_Y\times T^*Y)
\subset T^*_{\Delta_Y}(Y^2).
\tag{13}
\]

Indeed the twisted relation of \(K_R\) is the reciprocal graph, so its composition with the graph of \(K\) is the identity relation. The same containment holds for \(k_{\Delta_Y}\). The microsupport triangle bound puts the cone \(C\) of (11) in this conormal on the selected region. Its diagonal microlocalization is zero on (12). The detection argument (6)–(7) makes \(C\) invisible at every point of (12). At every other point in the selected region it is already invisible by (13). Hence (11) is an isomorphism in the full selected kernel localization.

Convolving this isomorphism with any localized input and using associativity shows that the unit
\(G\to\Psi_K\Phi_KG\)
is an isomorphism. Thus \(\Phi_K\) is fully faithful. Notice that a single objectwise test on ordinary stalks would not have established the kernel isomorphism (11); the conormal cone and the parameter variable are both used.

## Full faithfulness of the other adjoint

The constructible microlocal duality input is

\[
\mu\operatorname{hom}(A,B)
\simeq a^{-1}\mu\operatorname{hom}(D B,D A),
\tag{14}
\]

for cohomologically constructible \(A,B\). It is induced by external Hom exchange, bidual evaluation and exchanging the two diagonal factors. The exchange supplies the antipode. Applied to the same object in both arguments, it sends the identity to the dual identity; the bidual evaluation is the specified one.

Relative coefficient duality differs from Verdier duality by an invertible locally constant complex. Simultaneously tensoring both Hom inputs by such a complex cancels it. Factor transposition in (9) then changes the graph into its reciprocal. It follows from (14) that \(K_R\), on \(Y\times X\), satisfies all three conditions (1)–(3) for \(\chi^{-1}\). Its identity-induced morphism is invertible, with the dual identity normalization. It is cohomologically constructible, and its two selected microsupport containments are exactly the reciprocals of (2).

Apply the unit argument just proved to \(K_R\). It shows that \(\Phi_{K_R}=\Psi_K\) is fully faithful. We have now shown that both functors in the adjoint pair (4) are fully faithful. To see explicitly that the counit is invertible, write \(L=\Phi_K\), \(R=\Psi_K\). The unit at \(RF\) is invertible, and the triangle identity gives
\(R(\epsilon_F)\eta_{RF}=1_{RF}\).
Therefore \(R(\epsilon_F)\) is invertible. A fully faithful functor reflects isomorphisms: lift the inverse through its Hom bijection and use faithfulness to check the two composites. Hence \(\epsilon_F:LRF\to F\) is invertible too. This proves that (4) consists of inverse equivalences.

Finally take \(Z\) to be a point, \(G=G_2\), and \(F=\Phi_KG_1\) in (8). The now-invertible unit identifies \(\Psi_K\Phi_KG_1\) with \(G_1\). The resulting natural isomorphism is (5). All comparison maps invert input denominators by the previously proved support/cone bounds. The isomorphism therefore holds for localized inputs as stated. \(\square\)

## The geometric word “contact”

If the graph in (1) is smooth Lagrangian, the two physical cotangent factors carry opposite signs because the input covector has been negated. Pulling the product symplectic form back to the graph says
\(\chi^*d\theta_X=d\theta_Y\), where \(\theta\) is the tautological one-form. Conicity makes \(\chi\) commute with positive fiber scaling. Its derivative carries the fiber Euler vector field \(E_Y\) to \(E_X\). Since \(\iota_Ed\theta=\theta\), contraction of the symplectic identity gives
\(\chi^*\theta_X=\theta_Y\).
Thus the sheaf equivalence lies above the homogeneous symplectic transformation with the exact input sign used throughout. The theorem itself used the graph homeomorphisms and the kernel identity condition; smooth geometric realization is an additional question.

## Exercises with complete solutions

### A graph with a doubled coefficient

*Difficulty: Introductory.*

Let \(k\) be a field, \(f:Y\to X\) a diffeomorphism, and \(K=(k\oplus k)_{\Gamma_f}\). Its relation is the graph of the cotangent lift and has proper projections. Which condition fails, and why is the transform not an equivalence?

**Solution.** The kernel is constructible. Along its conormal, self microlocal Hom has fiber \(\operatorname{End}_k(k^2)\), in degree zero. The identity-induced map sends a scalar to the corresponding scalar matrix. This is not an isomorphism: its target has dimension four. Thus (3) fails. The transform sends \(G\) to \(f_*(G\oplus G)\). At a point, the map on endomorphisms of \(k\) is \(k\to M_2(k)\), so this functor is not fully faithful. Even the exact graph relation and perfect coefficients do not replace the identity condition.

### An orientation line on the graph

*Difficulty: Intermediate.*

Let \(f:Y\to X\) be a diffeomorphism and let \(L\) be a locally free rank-one \(k\)-local system on \(Y\). For \(K=L_{\Gamma_f}[s]\), determine the two inverse operators and verify (3) without choosing a global trivialization of \(L\).

**Solution.** The left operator is \(G\mapsto f_*(L\otimes G)[s]\). Its inverse and right adjoint is \(F\mapsto L^{-1}\otimes f^{-1}F[-s]\). All coefficients are locally perfect, and the relation is the same proper graph as for \(k_{\Gamma_f}\). Locally trivialize \(L\). The submanifold formula reduces self microlocal Hom on the graph conormal to \(R\operatorname{Hom}_k(k[s],k[s])=k\). Its identity is one. Changing trivialization multiplies source and target by inverse units, which cancel in self Hom; these local identity maps glue to exactly (3). Monodromy affects the operator but does not obstruct this identity condition. The kernel and its inverse shifts have opposite signs.

### Why the parameter variable is needed

*Difficulty: Advanced.*

In the proof of (11), replace the choice \(Z=Y\), \(G=k_{\Delta_Y}\) by a point parameter and one input sheaf \(G\). Explain what information the latter test yields and why it does not by itself prove a kernel inverse.

**Solution.** The point-parameter comparison describes the directional map
\(G\to\Psi_K\Phi_KG\) through morphisms to \(\Phi_KG\). It concerns that particular input. It does not produce or detect a map on \(Y\times Y\), nor does it put its cone in the diagonal conormal. With \(Z=Y\), the diagonal is the identity kernel and its transform is the original kernel \(K\). Its unit is the universal map (11); (13) confines the whole cone to a conormal, where (7) detects it. Associativity then gives invertibility of every input unit from one kernel isomorphism. A single chosen input may have zero directional data, so its unit can be invertible even for a kernel whose operator is not fully faithful.

### Two fully faithful adjoints

*Difficulty: Intermediate.*

Let \(L\dashv R\) be an adjoint pair of additive categories. Assume its unit is an isomorphism and \(R\) is fully faithful. Prove that the counit is an isomorphism. Apply this to the two relative-dual steps in Theorem 1.

**Solution.** For any \(F\), the triangle identity is
\(R\epsilon_F\circ\eta_{RF}=1_{RF}\).
Since \(\eta_{RF}\) is invertible, \(R\epsilon_F=(\eta_{RF})^{-1}\) is invertible. Fullness lifts its inverse to a map \(F\to LRF\); faithfulness shows that the two composites with \(\epsilon_F\) are identities. Thus \(\epsilon_F\) is invertible. In Theorem 1 the first kernel-unit argument makes \(\Phi_K\) fully faithful, so its unit is invertible. Constructible microlocal duality transfers the identity condition to \(K_R\), whose kernel-unit argument makes \(\Phi_{K_R}=\Psi_K\) fully faithful. Both hypotheses of the categorical calculation are now satisfied. No claim that the left and right relative dual kernels were identical was needed.

## References

Kashiwara and Schapira, *Microlocal study of sheaves*, Proposition 6.2.2 and Theorem 6.3.4 with its proof, printed 106 and 111–113, supplies the readable conormal coefficient model and contact-equivalence theorem. The graph condition, the two cotangent-region conditions, cohomological constructibility and the identity on microlocal endomorphisms are essential hypotheses. Schapira’s 2016 review, Theorem 5.11, restates the contact equivalence; it does not prove the entire foundational kernel calculus.

## Readable source and dependency account

The argument written here retains a parameter when proving that the kernel unit is invertible, detects its cone through the conormal model, and uses both adjunction maps. A doubled coefficient on the same graph fails the identity condition, as the retained example shows. Adjunction and localization are supplied by the named programme proofs, not by an unread categorical book. Their exact functor ranges and transitive foundational obligations remain in force.

Checked editions: [Kashiwara–Schapira, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf); [Schapira, sheaf lecture notes](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf); [Schapira, microlocal review (2016)](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf). The locators above identify the passages used; these links do not claim that all three works prove every statement or every prerequisite of this lesson. Original programme exposition remains CC0; the human works retain their own rights.
