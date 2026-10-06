# Natural duality for specialization and microlocal Hom

Specialization commutes with Verdier duality through a boundary connecting map. Microlocalization adds a Fourier transform, so its duality comparison also reverses the normal covector and retains the relative orientation complex. For microlocal Hom, exchanging the two manifold factors explains both the order of the dual inputs and the cancellation of one antipode.

Use Constructible costalks and Verdier duality for actual evaluation biduality, Perfect operations and finite microlocal coefficients for every constructibility and boundedness assertion below, and Weak constructibility under sheaf operations for the deformation and diagonal definitions. We retain the existing trace-normalized six operations, positive-parameter boundary comparison, full Fourier-duality comparison, and constructible external-Hom evaluation as exact prerequisites. Their proofs are not given here.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## Hypotheses and the four comparisons

Let \(k\) be commutative of finite global dimension. Manifolds and maps are real analytic, finite dimensional with uniform dimension bounds, Hausdorff and countable at infinity. All inputs are globally bounded and \(\mathbb R\)-constructible. No field, Noetherianity, compactness or global orientation is assumed.

Let \(M\) be an analytic embedded submanifold of \(X\), closed in the ambient neighborhood in use. Put \(E=T_MX\), \(E^*=T_M^*X\), and let \(\pi:E^*\to M\) be the projection. If the normal rank is \(c\), then

\[
\omega_{M/X}=\operatorname{or}_{M/X}[-c].
\qquad\text{(1)}
\]

This is a complex on \(M\), not a globally chosen trivialization. Write \(a\) for fibrewise negation on the conormal bundle or on \(T^*X\), as appropriate. Since \(a\) is an involutive diffeomorphism, \(a^{-1}\) and its direct image give canonically equivalent antipodal transport. We use inverse-image notation.

**Theorem.** The following are natural isomorphisms:

\[
\nu_M(D_XF)\simeq D_E(\nu_MF),
\qquad\text{(2)}
\]
\[
\mu_M(D_XF)\simeq
a^{-1}D_{E^*}(\mu_MF)\otimes\pi^{-1}\omega_{M/X},
\qquad\text{(3)}
\]
\[
\mu\operatorname{hom}(F,G)\simeq
a^{-1}\mu\operatorname{hom}(D_XG,D_XF),
\qquad\text{(4)}
\]
\[
D_{T^*X}\bigl(\mu\operatorname{hom}(F,G)\bigr)
\simeq\mu\operatorname{hom}(G,F)\otimes\pi_X^{-1}\omega_X.
\qquad\text{(5)}
\]

Here \(\pi_X:T^*X\to X\). In (4) the two inputs are swapped and dualized. In (5) they are swapped and the base dualizing complex is pulled back. The proof will identify every antipode and shift through actual maps.

## The deformation connecting map

Use the normal deformation \(D=\widetilde X_M\), its positive chamber \(\Omega=\{t>0\}\), and maps

\[
r:\Omega\to X,\qquad j:\Omega\hookrightarrow D,
\qquad s:E\hookrightarrow D.
\qquad\text{(6)}
\]

The whole analytic map \(p:D\to X\) has local formula \(p(v,z,t)=(tv,z)\); \(r=p|_\Omega\). The chamber is canonically \(X\times\mathbb R_{>0}\). The increasing positive parameter fixes
\(r^!F\simeq r^{-1}F[1]\).

Let \(H=r^{-1}F\). Open-complement localization of its open extension gives

\[
R\Gamma_{D\setminus\Omega}(j_!H)
\longrightarrow j_!H\longrightarrow Rj_*H\xrightarrow{+1}.
\qquad\text{(7)}
\]

The first term vanishes on \(\Omega\) and on the open negative chamber. Its support lies in \(E\), so it is \(s_*s^!j_!H\). Ordinary inverse image by \(s\) kills the middle term. The connecting arrow in (7) consequently gives

\[
s^{-1}Rj_*r^{-1}F
\xrightarrow{\sim}s^!j_!r^{-1}F[1]
\xrightarrow{\sim}s^!j_!r^!F.
\qquad\text{(8)}
\]

The second map uses the fixed positive parameter orientation. This is the normalized boundary comparison: it is the localization connecting map followed by the oriented smooth-pullback comparison. Its sign has thus been fixed, and its maps commute with restrictions of adapted charts. The left side is the definition of \(\nu_MF\).

The object \(A=j_!r^!F\) is constructible. Indeed it is
\((k_\Omega\otimes p^{-1}F)[1]\) on the whole analytic deformation. Perfect inverse image, tensor closure and the bounded operation contracts establish this assertion. Thus all evaluations used for \(A\) and its exceptional restriction are within the proved constructible biduality scope.

## Specialization duality through that map

For constructible \(B\) and an analytic map \(f:Y\to X\), exceptional duality and actual biduality give the natural pair

\[
f^!D_XB\simeq D_Y(f^{-1}B),\qquad
f^{-1}D_XB\simeq D_Y(f^!B).
\qquad\text{(9)}
\]

The first is the internal exceptional-adjunction formula with
\(f^!\omega_X=\omega_Y\). For the second, apply the first to \(D_XB\), use \(B\to D_XD_XB\), and dualize its constructible output. It is not an inverse-image/internal-Hom assertion for arbitrary weak coefficients.

The ordinary direct-image dual of an open extension is
\(D_D(j_!L)\simeq Rj_*D_\Omega L\), from the normalized internal adjunction. Apply (9) to \(r\), then to \(s\). Together with (8) these give the complete chain

\[
\begin{aligned}
\nu_M(D_XF)
&=s^{-1}Rj_*r^{-1}D_XF\\
&\simeq s^{-1}D_D(j_!r^!F)\\
&\simeq D_E(s^!j_!r^!F)\\
&\simeq D_E(\nu_MF).
\end{aligned}
\qquad\text{(10)}
\]

The final map is the dual of the particular boundary comparison (8), in its contravariant direction. Each earlier map comes from trace-normalized evaluation and adjunction. Hence (10) proves (2) as a natural comparison. There is no residual parameter shift: the connecting rotation and \(r^!\)'s \([1]\) have already combined in (8).

For a locally closed \(M\), restrict to ambient open neighborhoods where it is closed. All comparisons above commute with open restriction, so their local constructions agree and glue. Rank zero uses the same positive parameter boundary map; specialization then gives the identity functor.

## Fourier duality supplies the antipode and relative complex

For a rank-\(c\) bundle \(E\to M\), let \(O\) be its fibre orientation line on \(M\), and set \(W=O[c]\). Positive dual bases identify the fibre orientations of \(E\) and \(E^*\), with \(O\otimes O\simeq k_M\).

Retain the negative-pairing proper-support transform \(T_E:E\to E^*\). The exchanged inverse transform \(I_E=S_{E^*}\) also goes from \(E\) to \(E^*\); it is not \(S_E\), which has the opposite domain. The full Fourier-duality prerequisite is the natural evaluation comparison

\[
I_E R\mathcal Hom(B,\tau^!Q)
\xrightarrow{\sim}
R\mathcal Hom(T_EB,\pi^!Q)
\qquad\text{(11)}
\]

for bounded conic \(B\) and bounded-below \(Q\) on \(M\). Its map uses exceptional internal Hom, composition of the two bundle projections' exceptional inverses, tensor–Hom evaluation and the proper-support trace. Thus it preserves arbitrary coefficient modules in its full prerequisite scope, without replacing a dual by an unjustified dual tensor.

Here the analytic base has finite compact-support cohomological dimension. Take \(Q=\omega_M\). Composition gives \(\tau^!\omega_M=\omega_E\) and \(\pi^!\omega_M=\omega_{E^*}\), so (11) becomes
\(I_ED_EB\simeq D_{E^*}T_EB\).
The signed halfspace comparison identifies

\[
I_EB\simeq a^{-1}T_EB\otimes\pi^{-1}O[c].
\qquad\text{(12)}
\]

The positive halfspace in \(I_E\) becomes the negative halfspace under covector negation; its exceptional projection contributes precisely \(O[c]\). Solve (11)–(12) for \(T_ED_EB\):

\[
T_ED_EB\simeq a^{-1}D_{E^*}T_EB
\otimes\pi^{-1}O[-c].
\qquad\text{(13)}
\]

The last factor is \(W^{-1}\), not \(W\). For the normal bundle it is exactly \(\omega_{M/X}\). Apply (13) to \(B=\nu_MF\), and use (2) and \(\mu_MF=T_E\nu_MF\). This proves (3). All objects are bounded and constructible by the preceding perfect-operations lesson. The map is built from (10)–(12), so both the antipode and orientation are specified by those natural comparisons. Rank zero has identity antipode and orientation complex \(k\), as required.

## Factor exchange reverses the dual inputs

On \(X^2\), with projections \(q_1,q_2\), define

\[
K_{F,G}=R\mathcal Hom(q_2^{-1}F,q_1^!G),
\qquad\mu\operatorname{hom}(F,G)=\mu_{\Delta_X}K_{F,G}.
\qquad\text{(14)}
\]

The two inputs of this kernel are constructible. Natural internal-Hom reversal and (9) give

\[
\begin{aligned}
K_{F,G}
&\simeq R\mathcal Hom(D_{X^2}q_1^!G,D_{X^2}q_2^{-1}F)\\
&\simeq R\mathcal Hom(q_1^{-1}D_XG,q_2^!D_XF)\\
&=\sigma^{-1}K_{D_XG,D_XF},
\end{aligned}
\qquad\text{(15)}
\]

where \(\sigma(x_1,x_2)=(x_2,x_1)\). Its map on the diagonal conormal sends
\((x,x;\xi,-\xi)\) to \((x,x;-\xi,\xi)\).
Under our identification with \(T^*X\), \((\xi,-\xi)\mapsto\xi\), this is exactly \(a\).

The action on the functor is also explicit. Factor exchange lifts to the diagonal normal deformation, fixes its positive parameter and negates the normal vector. Its base-change maps for the diffeomorphism commute with \(j\), \(s\) and their adjunctions. In Fourier incidence, simultaneous normal-vector and normal-covector negation preserves the pairing and its negative inequality. Therefore

\[
\mu_{\Delta_X}(\sigma^{-1}K)
\simeq a^{-1}\mu_{\Delta_X}K.
\qquad\text{(16)}
\]

Applying (16) to (15) proves (4). This explains the antipode through the actual normal and Fourier maps, and preserves the exceptional projection in the defining kernel.

## The cotangent dual has one base dualizing factor

The constructible external-Hom evaluation identifies

\[
K_{F,G}\simeq G\boxtimes D_XF.
\qquad\text{(17)}
\]

Its hypotheses hold because \(F\) is cohomologically constructible. The underlying theorem tests product rectangles with its represented perfect compact-section system, then uses finite-projective evaluation; (17) is not a general stalkwise-Hom substitution.

We can calculate the dual kernel without assuming an external dual formula. Tensor–Hom currying first gives
\(K_{F,G}\simeq D_{X^2}(D_{X^2}q_1^!G\otimes q_2^{-1}F)\).
The tensor input is constructible, so its actual bidual evaluation yields

\[
D_{X^2}K_{F,G}\simeq
q_1^{-1}D_XG\otimes q_2^{-1}F
=D_XG\boxtimes F.
\qquad\text{(18)}
\]

Apply (3) along the diagonal and solve for the cotangent dual:

\[
D_{T^*X}\mu_{\Delta_X}K
\simeq a^{-1}\mu_{\Delta_X}(D_{X^2}K)
\otimes\pi_X^{-1}\omega_{\Delta_X/X^2}^{-1}.
\qquad\text{(19)}
\]

The trace-compatible relative complex on the diagonal is
\(\omega_{\Delta_X/X^2}=\omega_{\Delta_X}\otimes
\omega_{X^2}|_{\Delta_X}^{-1}\simeq\omega_X^{-1}\).
Indeed the restricted product complex is \(\omega_X\otimes\omega_X\); evaluation with the diagonal's \(\omega_X\) leaves its inverse, including shift \([-\dim X]\). Tensor factors are evaluated in that displayed product order, and any permutation uses the Koszul symmetry. This is the relative-composition identification, not a choice to trivialize the normal orientation.

Factor exchange sends (18) to \(F\boxtimes D_XG\), which (17) with exchanged inputs identifies with \(K_{G,F}\). Its conormal action in (16) cancels the antipode in (19). The relative inverse complex in (19) becomes \(\omega_X\). Thus the result is precisely (5), with no remaining antipode. All maps used to cancel it arise from the same factor-exchange diffeomorphism and the involution \(a^2=1\).

## Examples and exercises with solutions

### A ray tests both the antipode and the normal shift

*Difficulty: Intermediate.*

On the increasing oriented line \(X=\mathbb R\), let \(M=\{0\}\) and \(F=k_{[0,\infty)}\). Compute both sides of (2) and (3), including the zero covector.

**Solution.** In the positive deformation chamber \(p(v,t)=tv\), the condition \(tv\geq0\) is \(v\geq0\). Hence \(\nu_MF=k_{[0,\infty)}\) on the normal line. The ambient dual is \(D_XF=k_{(0,\infty)}[1]\); its specialization is \(k_{(0,\infty)}[1]\), also the dual of the closed normal ray. This verifies (2).

The negative-pairing ray calculation gives \(\mu_MF=k_{(0,\infty)}\) on the conormal line. Its absolute dual is \(k_{[0,\infty)}[1]\). Covector negation gives \(k_{(-\infty,0]}[1]\), and \(\omega_{M/X}=k[-1]\) changes it to \(k_{(-\infty,0]}\). Independently, specializing \(D_XF\) and transforming the open positive normal ray gives \(k_{(-\infty,0]}[-1][1]=k_{(-\infty,0]}\). At the zero covector \(\mu_MF\) is zero, while \(\mu_M(D_XF)\) has coefficient \(k\). The antipode determines which half-line is closed; the relative shift removes the dual line's degree minus one.

### A point coefficient has no extra normal integration degree

*Difficulty: Introductory.*

In an oriented \(c\)-dimensional real vector space, take \(M=\{0\}\) and \(F=k_{\{0\}}\). Compute the two duality comparisons and also check \(c=0\).

**Solution.** Specialization is the sheaf at the zero normal vector. Its Fourier transform is the constant coefficient on the whole conormal vector space: the incidence restricted to the zero vector has pairing zero and projects identically to every covector. Thus \(\mu_MF=k_{E^*}\). The dual of the original closed point coefficient is again that point coefficient, since its intrinsic dualizing complex is \(k\). The same statement holds for its specialized point coefficient, verifying (2).

On the dual normal space, \(D_{E^*}k_{E^*}=\operatorname{or}_{E^*}[c]\). The antipode preserves the underlying orientation local-system type, and positive dual bases pair it with \(\omega_{M/X}=\operatorname{or}_{E}[-c]\). The orientation evaluation and opposite shifts give the constant coefficient \(k\), exactly \(\mu_M(D_XF)\). No additional normal shift remains. When \(c=0\), both vector spaces are points, both orientation factors are \(k\), and every displayed operation is the identity.

### A Möbius normal line retains its sign monodromy

*Difficulty: Advanced.*

Work over \(\mathbb Z\). Let \(X\) be the total space of the real analytic Möbius line bundle \(L\to S^1\), let \(M=S^1\) be its zero section, and let \(F=\mathbb Z_M\). Calculate (3) without trivializing the normal orientation globally.

**Solution.** The normal bundle is \(E=L\). Its fibre orientation line \(O\) on \(S^1\) has monodromy \(-1\): traversing the base once reverses a fibre basis. The dual line bundle has the same orientation monodromy. The circle itself is oriented and has \(\omega_M=\mathbb Z_M[1]\).

The coefficient is supported on the zero section, so \(\nu_MF\) is its zero-section coefficient on \(L\). The zero-vector Fourier calculation gives \(\mu_MF=\pi^{-1}\mathbb Z_M\) on \(L^*\). Closed-embedding duality gives \(D_XF=i_*\omega_M=\mathbb Z_M[1]\); hence its microlocalization is \(\pi^{-1}\mathbb Z_M[1]\).

The dual of the constant coefficient on \(L^*\) is its total-space dualizing complex \(\pi^{-1}O[2]\): one circle dimension and one fibre dimension contribute the shift two, while the fibre contributes the sign local system. The antipode covers the identity of the base, so its transported orientation line still has monodromy \(-1\). The relative embedding complex is \(\omega_{M/X}=O[-1]\). Their tensor product is
\(\pi^{-1}(O\otimes O)[1]\simeq\pi^{-1}\mathbb Z_M[1]\), as required. Omitting \(O[-1]\) would leave both the wrong degree and the wrong integral monodromy.

### The positive parameter fixes the boundary degree

*Difficulty: Intermediate.*

Take the constant coefficient on the oriented line and specialize at its origin. Use (7) to compute the boundary map and the degrees in the two middle expressions of (10).

**Solution.** The deformation is the \((v,t)\)-plane, with \(\Omega=\{t>0\}\). Its ordinary chamber pullback is constant. At a central point, its open extension has ordinary stalk zero, and ordinary direct image from the positive chamber has stalk \(k\) in degree zero: the small chamber intersection is a product of intervals with ordinary coefficient \(k\). Restricting (7) therefore gives a triangle
\(C\to0\to k\to C[1]\).
The last arrow is the actual localization connecting isomorphism, so \(C=s^!j_!r^{-1}k=k[-1]\), with its generator fixed by increasing \(t\).

The smooth inverse \(r^!k=r^{-1}k[1]\) shifts this costalk back: \(s^!j_!r^!k=k\). Thus specialization has coefficient \(k\) in degree zero. In the oriented deformation plane, duality sends \(j_!r^!k=k_{\{t>0\}}[1]\) to \(k_{\{t\geq0\}}[1]\). Its central ordinary restriction is \(k_E[1]\), the dual of the constant coefficient on the normal line. This is also the specialization of \(D_Xk_X=k_X[1]\). The two appearances of \([1]\) have distinct origins; (8) fixes their cancellation before the normal Verdier shift is calculated.

### A zero-section morphism coefficient uses the base dimension

*Difficulty: Intermediate.*

Let \(X\) be an oriented \(n\)-manifold, and \(P,Q\) perfect coefficient complexes, constant on \(X\). Calculate (4) and (5) for their microlocal Hom, using finite-projective evaluation.

**Solution.** Put \(A=R\operatorname{Hom}_k(P,Q)=P^\vee\otimes^LQ\). The exceptional projection in (14) contributes its fibre orientation and \([n]\). Specialization of that constant kernel adds no degree; the normal Fourier transform contributes the matching inverse orientation and \([-n]\). Their actual trace pairings cancel, giving
\(\mu\operatorname{hom}(P_X,Q_X)=i_*A_X\), with \(i:X\hookrightarrow T^*X\) the zero section.

The dual inputs on \(X\) are \(Q^\vee_X[n]\) and \(P^\vee_X[n]\). Their equal shifts cancel inside coefficient Hom. Finite-projective evaluation gives
\(R\operatorname{Hom}(Q^\vee,P^\vee)\simeq R\operatorname{Hom}(P,Q)\), so (4) has the same coefficient \(A\); the antipode fixes the zero section.

Closed-embedding duality calculates
\(D_{T^*X}i_*A_X=i_*D_XA_X=i_*(A^\vee_X[n])\).
Again finite-projective evaluation gives
\(A^\vee\simeq Q^\vee\otimes^LP=R\operatorname{Hom}(Q,P)\).
This is exactly \(\mu\operatorname{hom}(Q_X,P_X)\otimes\pi_X^{-1}\omega_X\). The degree is the intrinsic base dimension \(n\); directly inserting the cotangent total-space dimension \(2n\) would miss the closed-embedding costalk adjustment.

### Integral torsion keeps both dual morphism degrees

*Difficulty: Advanced.*

On the increasing oriented line, take \(P=\mathbb Z/m\), \(Q=\mathbb Z/n\), \(m,n>1\). Find the cohomology degrees of the absolute cotangent dual of \(\mu\operatorname{hom}(P_X,Q_X)\), and verify (5).

**Solution.** Write \(d=\gcd(m,n)\). A two-term finite-free resolution of \(P\) gives
\(A=R\operatorname{Hom}_{\mathbb Z}(P,Q)\) with \(\mathbb Z/d\) in degrees zero and one. The whole complex is perfect. Microlocal Hom is its zero-section extension by the preceding calculation.

To compute \(A^\vee\), the two-column integral hyper-Ext sequences give \(\mathbb Z/d\) in degrees zero and one: the degree-zero group comes from \(\operatorname{Ext}^1(H^1(A),\mathbb Z)\), and the degree-one group from \(\operatorname{Ext}^1(H^0(A),\mathbb Z)\). The Hom terms vanish since these groups are torsion. Its zero-section ambient dual is therefore \(i_*(A^\vee[1])\), with those groups in degrees minus one and zero.

On the right of (5), \(R\operatorname{Hom}_{\mathbb Z}(Q,P)\) has the same gcd torsion in degrees zero and one. Tensoring its zero-section extension with \(\pi_X^{-1}\omega_X=k[1]\) gives degrees minus one and zero, agreeing exactly. Finite-projective tensor–Hom evaluation identifies the full complexes and their natural pairing, not merely their cohomology groups. The integral Ext degree cannot be discarded in this duality comparison.

## References

- M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Chapters 2 and 5: specialization, microlocalization and the functor \(\mu hom\), with the normal-deformation boundary comparison and Fourier duality.
- The existing specialization proof fixes the connecting map and positive-parameter orientation in (8). The existing Fourier-duality proof fixes the variable-test evaluation, exchanged-transform domains, positive dual orientations and signed halfspace comparison in (11)–(13).
- Constructible internal and external Hom, trace-compatible relative dualizing composition and actual evaluation biduality supply the remaining prerequisites. The application proofs above retain their natural maps and do not certify their transitive foundations by reference.
