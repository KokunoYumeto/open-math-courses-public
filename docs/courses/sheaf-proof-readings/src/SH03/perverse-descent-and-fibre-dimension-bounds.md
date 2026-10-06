# Perverse descent and fibre dimension bounds

Perverse objects glue because their degree-zero morphisms form a sheaf. A countable construction gives the glued complex, and the ordinary bounds on the perverse heart keep it globally bounded. Functorial degree bounds come from a different mechanism: an analytic inverse image can increase a support dimension by at most the largest fibre dimension. Point exceptional composition gives the same geometric estimate for cosupport. Adjunction then gives conditional bounds for the two direct images.

*Original programme exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026; source comparison and editorial revision by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently expressed programme text is dedicated under CC0. Human sources retain their own terms.*

Use Perverse support, costalks and truncation triangles for the real perverse t-structure, support and cosupport tests, negative internal Hom, and the Hom sheaf. Use T-exact functors and adjoints between hearts for restricted adjoint tests with their separate membership hypotheses, and Constructible costalks and Verdier duality for the actual dual pairings and evaluation.

Throughout, \(k\) is commutative of finite global dimension. Manifolds and maps are real analytic, Hausdorff and countable at infinity, with uniform finite dimension bounds. Weak constructibility allows arbitrary modules; \(D^b\) always imposes a single global cohomology interval. The strong perverse heart additionally uses the Noetherian hypothesis of the preceding truncation theorem. Verdier duality between the perverse cuts below is stated over a field on the strong category.

Keep \(p^*(s)=-p(s)-s\), \(pa=p(a+s)\), and
\({}^pD^{\le r}={}^pD^{\le0}[-r]\), with analogous lower cuts. A constant degree change satisfies

\[
 {}^{p+a}D^{\le0}={}^pD^{\le a},\qquad
 {}^{p+a}D^{\ge0}={}^pD^{\ge a}.
 \tag{1}
\]

Here \((p+a)(s)=p(s)+a\), whereas \(p[a]\) changes the dimension argument.

## Restrictions and morphisms descend

Both perverse cuts are local on an ambient open cover. For the upper cut, a subanalytic support has dimension less than an integer \(r\) exactly when it does locally at every point. Its global dimension is the supremum of its local dimensions, all integers in one finite range. The same argument applies to the point cosupport test for the lower cut. Ordinary restriction to an open set retains point costalks. Thus open restriction preserves the two cuts and their intersection, and local membership implies global membership once the object is globally bounded and weakly constructible.

Write \(\mathcal P_p(U)={}^pD^{\le0}(U)\cap{}^pD^{\ge0}(U)\). For \(F,G\in\mathcal P_p(U)\), the preceding Hom theorem identifies, including restriction maps,

\[
 V\longmapsto\operatorname{Hom}_{D(V)}(F|_V,G|_V)
       =\Gamma\bigl(V,H^0R\mathcal Hom(F,G)\bigr)
       \quad(V\subset U).
 \tag{2}
\]

Therefore compatible local morphisms glue uniquely. If they are locally invertible, their local inverses also agree and glue, so the resulting global morphism is invertible. In particular, two objects realizing the same marked descent data have a unique isomorphism compatible with those markings. This does not eliminate the automorphisms of an unmarked object.

## Glue two objects by an actual overlap map

Let \(X=U\cup V\), \(W=U\cap V\), and let \(F_U,F_V\) be perverse heart objects with an isomorphism \(\alpha:F_U|_W\to F_V|_W\). Denote the three open inclusions into \(X\) by \(j_U,j_V,j_W\). Form the map whose components are the open counits and the specified overlap isomorphism:

\[
 j_{W!}(F_U|_W)
   \xrightarrow{\ (u,-v\alpha)\ }
 j_{U!}F_U\oplus j_{V!}F_V
   \longrightarrow F\longrightarrow.
 \tag{3}
\]

This triangle is formed in the ambient derived category. The open sets need not be subanalytic, so its intermediate extensions need not be constructible.

The two summand maps induce \(\beta_U:F_U\to F|_U\) and \(\beta_V:F_V\to F|_V\). They are isomorphisms. For example, on \(U\) the second summand is the extension from \(W\) of \(F_V|_W\). The second component of the first arrow identifies its source with this summand, with a minus sign. A triangular automorphism of the middle object removes its first component. Its cone is consequently \(F_U\), with \(\beta_U\) as that identification. The same calculation works on \(V\).

On \(W\), composition of the first and second arrows of (3) is zero, so

\[
 \beta_U|_W=\beta_V|_W\circ\alpha.
 \tag{4}
\]

These are the desired actual overlap maps. Local identification with \(F_U,F_V\) gives local weak constructibility and perverse membership. The finite cone is globally bounded; the local microsupport criterion gives global weak constructibility. Hence \(F\in\mathcal P_p(X)\). Perfectness of stalks is also local, so the construction realizes strong descent data when the strong heart is defined.

Inductively this proves effective descent for a finite open cover. Uniqueness and all compatible identifications at each step come from (2), rather than a purported functorial choice of cones.

## Countable gluing retains one global bound

There are two distinct steps in descent. Orthogonality in the glued t-structure makes degree-zero morphisms local, but it does not itself produce a single bounded complex on an infinite union. The construction below chooses injective representatives with the same lower bound before taking the stalkwise exact filtered colimit. Local identifications then preserve constructibility, while the common upper bound returns the colimit to the bounded category. This is the part of the argument for which an unrestricted statement that objects glue would leave a real gap.

**Theorem.** The categories \(U\mapsto\mathcal P_p(U)\), with all their morphisms, form a stack on the open subsets of \(X\). The same holds for the strong perverse hearts over a Noetherian coefficient ring.

**Proof.** The morphism part and uniqueness were proved in (2). Let a possibly arbitrary open cover carry objects and isomorphisms satisfying the cocycle condition. Our manifold convention gives a countable subcover: cover each compact set of a countable compact exhaustion by finitely many members of the given cover. Enumerate the resulting subcover \(V_1,V_2,\ldots\), and put \(U_m=V_1\cup\cdots\cup V_m\). Finite descent gives marked heart objects \(F_m\) on \(U_m\), with compatible isomorphisms
\(\alpha_m:F_m\to F_{m+1}|_{U_m}\).

If \(n\) is the uniform dimension bound, the ordinary bounds on every heart object are

\[
 F_m\in D^{[a,b]}(U_m),\qquad
 a=\min_{0\le s\le n}p(s),\quad
 b=\max_{0\le s\le n}p(s).
 \tag{5}
\]

Choose ordinary lower-cut representatives and bounded-below injective resolutions \(I_m\) with terms zero below this same \(a\). These injective complexes need not have an upper term bound. The exact foundational inputs are the same-lower-bound injective construction used in the preceding t-exact lesson and the current programme proof of bounded-below K-injectivity. For an open inclusion restriction of an injective sheaf is injective, since restriction is right adjoint to exact extension by zero. Thus \(I_{m+1}|_{U_m}\) is K-injective. Each \(\alpha_m\) is represented by an actual chain map
\(I_m\to I_{m+1}|_{U_m}\).

Adjunction gives chain maps on \(X\), and we take a termwise sheaf colimit:

\[
 j_{m!}I_m\longrightarrow j_{m+1,!}I_{m+1},\qquad
 L^\bullet=\mathop{\mathrm{colim}}_m j_{m!}I_m.
 \tag{6}
\]

For these sheaves of modules, colimits commute with stalks and filtered colimits are exact; the precise open foundational proof is [Stacks, Lemma 17.3.2, parts 2–3](https://stacks.math.columbia.edu/tag/01AH), using [Lemma 10.8.8](https://stacks.math.columbia.edu/tag/00DB) for the module homology comparison. Those sources retain their GNU Free Documentation License; only the prerequisite links and their mathematical statements are used here.

At \(x\in U_m\) the later chain maps are all quasi-isomorphisms on stalks. Exactness of the colimit gives the canonical identifications

\[
 H^r(L)_x
   =\mathop{\mathrm{colim}}_{q\ge m}H^r((I_q)_x)
   \simeq H^r((I_m)_x).
 \tag{7}
\]

Consequently the actual map \(I_m\to L|_{U_m}\) is a quasi-isomorphism. All its identifications with the next such map satisfy (4) in the derived category, because the transition chain maps represent the chosen \(\alpha_m\).

Formula (5) and stalkwise detection imply \(H^r(L)=0\) outside the one interval \([a,b]\) on all of \(X\). Ordinary smart cuts give a bounded representative of this object; no bounded injective-resolution claim was needed. The local identifications also give weak constructibility: microsupport is locally the closed subanalytic isotropic microsupport of one \(F_m\), so the global microsupport criterion applies. Perfectness of stalks follows locally in the strong case. Locality of both cuts therefore puts \(L\) in the required heart.

For a cover member not in the countable subcover, its prescribed maps to the subcover objects determine isomorphisms on its intersections with all \(U_m\). The cocycle condition makes these agree. Apply the morphism sheaf (2) to glue them on that member. This supplies every original marking and proves effectiveness for the original cover. Uniqueness is already supplied by (2). \(\square\)

The existing programme provider proves the exact open extension, injective restriction and K-injective interfaces in [Sheaves of modules and their derived categories, §5.2, §5.4–5.5 and §6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/sheaves-of-modules-and-their-derived-categories.html). Resolution existence in its §6.1 is explicitly source-referred; use the full linked Stacks construction recorded in the preceding t-exact lesson. The ordinary derived foundation lane is reused.

## Two ambient support operations

Let \(i:T\hookrightarrow X\) be locally closed subanalytic, possibly singular. On the ambient manifold define \(F_T=i_!i^{-1}F\) and \(R\Gamma_TF=Ri_*i^!F=R\mathcal Hom(k_T,F)\). Then

\[
 F\in{}^pD^{\le0}\Longrightarrow F_T\in{}^pD^{\le0},
 \qquad
 F\in{}^pD^{\ge0}\Longrightarrow R\Gamma_TF\in{}^pD^{\ge0}.
 \tag{8}
\]

Extension by zero and ordinary inverse restriction are exact. Their cohomology has the original stalk on \(T\) and zero stalk elsewhere, so its support dimension can only decrease. This proves the upper assertion.

For the lower assertion, point exceptional adjunction gives, for any \(H\) on \(T\),
\(i_x^!Ri_*H=R\operatorname{Hom}(i^{-1}k_{\{x\}},H)\).
If \(x\notin T\) the first argument is zero. If \(x\in T\), it is the point sheaf on \(T\), so exceptional composition, with \(H=i^!F\), gives \(i_x^!Ri_*i^!F=i_x^!F\). Hence

\[
 \operatorname{cosupp}^r(R\Gamma_TF)
   =T\cap\operatorname{cosupp}^rF.
 \tag{9}
\]

Its dimension does not increase, and the cosupport criterion proves (8). Both operations stay globally bounded weakly constructible: \(k_T\) is a bounded weak coefficient, and the established internal-Hom theorem applies to \(R\Gamma_TF\). The extension has weak constructibility by the subanalytic support operation theorem. These are ambient assertions and do not presuppose a perverse t-structure on a singular space \(T\).

Thus the first operation is right t-exact and the second left t-exact. These adjectives alone do not say that either functor preserves the heart.

## The dimension of an analytic inverse image

Let \(f:Y\to X\) be analytic and assume
\(\dim f^{-1}(x)\le d\) for every \(x\in X\). The dimensions here are real dimensions. For every subanalytic \(A\subset X\),

\[
 \dim f^{-1}(A)\le\dim A+d.
 \tag{10}
\]

Here is a local proof relative to the stated subanalytic stratification prerequisites. Stratify \(A\) into analytic smooth pieces and stratify their inverse images compatibly. On a connected source piece, analytic differential minors give an open locus of its maximal rank; its complement has smaller dimension. Stratify that complement and repeat. There are finitely many dimension stages, so one obtains source pieces on which \(f\) has constant rank and takes values in one target piece. All constructions are local; they assert no global subanalyticity for a nonproper image.

On a source piece of dimension \(s\) and rank \(r\), the constant-rank theorem makes its fibre dimension \(s-r\). This fibre lies in an actual fibre of \(f\), hence \(s-r\le d\). Since its image lies in a target piece of dimension at most \(\dim A\), \(r\le\dim A\). Therefore \(s\le\dim A+d\). Taking the supremum of the local piece dimensions proves (10). If \(A\) is empty, both sides use the empty-dimension convention.

This proof retains the analytic stratification, rank-minor and set-operation prerequisites from Subanalytic sets and limiting tangent directions. It does not certify their unfinished lower foundations. When \(Y\ne\varnothing\), the fibre hypothesis forces \(d\ge0\); for empty \(Y\) all assertions below are vacuous.

## Inverse images shift the dimension argument

The exact bounds are

\[
\begin{aligned}
 f^{-1}:{}^pD^{\le0}(X)&\longrightarrow{}^{p[-d]}D^{\le0}(Y),\\
 f^!:{}^pD^{\ge0}(X)&\longrightarrow{}^{p[-d]}D^{\ge-d}(Y).
\end{aligned}
\tag{11}
\]

The existing analytic weak-operation theorem supplies globally bounded weak membership for both outputs, with their full arbitrary-coefficient contracts.

For the upper statement, ordinary inverse image is exact and its stalk at \(y\) is the stalk at \(f(y)\). Thus the degree-\(j\) nonzero locus is exactly \(f^{-1}\operatorname{supp}H^jF\). If \(j>p(r-d)\), its source locus has dimension less than \(r-d\). Formula (10) makes its inverse image have dimension less than \(r\), as required.

For the lower statement, let \(y\in Y\), \(x=f(y)\). Exceptional composition gives \(i_y^!f^!F=i_x^!F\), with no extra point-degree shift. Therefore

\[
 \operatorname{cosupp}^j(f^!F)
       =f^{-1}\operatorname{cosupp}^jF.
 \tag{12}
\]

Put \(q(s)=p(s-d)-d\), so \({}^qD^{\ge0}={}^{p[-d]}D^{\ge-d}\). If \(j<q(r)+r=p(r-d)+(r-d)\), the original cosupport has dimension less than \(r-d\). Its inverse image again has dimension less than \(r\). This proves the second line of (11). Ordinary cohomology of \(f^!F\) may have dimension shifts even though its point costalk identity (12) has none.

## Direct images need actual output membership

For the complex middle perversity, Massey's *Notes on Perverse Sheaves and Vanishing Cycles*, §5, states the corresponding four fibre-dimension bounds with the direct-image constructibility conditions explicit. Here the real perversity translation is obtained from the dimension estimate and the actual adjunctions already established. Thus this step proves a degree inequality for outputs in the stated category; it does not turn a nonproper analytic map into a constructibility theorem. The zero-dimensional-fibre and countable-space examples below test that distinction separately.

Suppose \(G\) is globally bounded weakly constructible on \(Y\). The two statements are

\[
\begin{aligned}
 G\in{}^pD^{\le0}(Y),\
 Rf_!G\in D^b_{\mathrm w\text{-}\mathbb R\mathrm c}(X)
 &\Longrightarrow Rf_!G\in{}^{p[d]}D^{\le d}(X),\\
 G\in{}^pD^{\ge0}(Y),\
 Rf_*G\in D^b_{\mathrm w\text{-}\mathbb R\mathrm c}(X)
 &\Longrightarrow Rf_*G\in{}^{p[d]}D^{\ge0}(X).
\end{aligned}
\tag{13}
\]

The image-membership clauses retain both weak constructibility and global boundedness. A fibre-dimension inequality supplies neither of them automatically.

For the first assertion put \(q(s)=p(s+d)+d\). Apply (11) to \(q\): \(f^!\) sends the \(q\)-lower cut on \(X\) into the \(p\)-lower cut on \(Y\), because \(q[-d]-d=p\). For \(H\in{}^qD^{\ge1}(X)\), adjunction gives
\[
 \operatorname{Hom}(Rf_!G,H)
       =\operatorname{Hom}(G,f^!H)=0.
\]
The actual membership of \(Rf_!G\) permits the orthogonal cut criterion inside that category. It gives \(Rf_!G\in{}^qD^{\le0}={}^{p[d]}D^{\le d}\).

For the second put \(q=p[d]\). Then \(q[-d]=p\), and \(f^{-1}\) sends the \(q\)-upper cut on \(X\) into the \(p\)-upper cut on \(Y\). For \(H\in{}^qD^{\le-1}(X)\),
\(\operatorname{Hom}(H,Rf_*G)=\operatorname{Hom}(f^{-1}H,G)=0\).
Again the separate output membership permits the orthogonal criterion, giving the second line of (13). These are precisely the restricted adjoint arguments, with their actual source and target t-structures.

## Field duality exchanges a perversity and its dual

Now let \(k\) be a field and \(F\) strongly constructible. The proved local pairings identify

\[
 (D_XF)_x\simeq R\operatorname{Hom}_k(i_x^!F,k),
 \qquad
 i_x^!D_XF\simeq R\operatorname{Hom}_k(F_x,k).
 \tag{14}
\]

Perfect stalks and costalks are retained. Field dualization is exact, so \(H^j(P^\vee)=(H^{-j}P)^\vee\), and the latter is nonzero exactly when \(H^{-j}P\) is nonzero. Consequently
\(\operatorname{supp}H^jD_XF=\operatorname{cosupp}^{-j}F\) and
\(\operatorname{cosupp}^jD_XF=\operatorname{supp}H^{-j}F\).
Since \(p^*(r)+r=-p(r)\), the support and cosupport inequalities give

\[
 D_X:{}^pD^{\le0}_{\mathbb R\mathrm c}(X)
        \longrightarrow{}^{p^*}D^{\ge0}_{\mathbb R\mathrm c}(X),
 \qquad
 D_X:{}^pD^{\ge0}_{\mathbb R\mathrm c}(X)
        \longrightarrow{}^{p^*}D^{\le0}_{\mathbb R\mathrm c}(X).
 \tag{15}
\]

For example the first target condition is
\(j<p^*(r)+r=-p(r)\), equivalently \(-j>p(r)\), exactly the original upper support test. The other is \(j>p^*(r)\), equivalently \(-j<p(r)+r\), exactly the original lower cosupport test.

The actual bidual evaluation is an isomorphism on the strong category. Applying it and \(p^{**}=p\) gives the reverse implications and a contravariant equivalence between the two hearts. On a triangle its arrows reverse with the derived shift convention; the heart short exact sequence therefore reverses to a short exact sequence in the dual heart. The coefficient-ring and perfectness assumptions have not been replaced by a claim about arbitrary infinite coefficients.

## A closed submanifold separates the two tests

Let \(i:Z\hookrightarrow X\) be a closed analytic submanifold and \(j:X\setminus Z\hookrightarrow X\) its open complement. For any globally bounded weakly constructible \(F\),

\[
\begin{aligned}
 F\in{}^pD^{\le0}(X)
 &\Longleftrightarrow
 j^{-1}F\in{}^pD^{\le0}(X\setminus Z),\
 i^{-1}F\in{}^pD^{\le0}(Z),\\
 F\in{}^pD^{\ge0}(X)
 &\Longleftrightarrow
 j^{-1}F\in{}^pD^{\ge0}(X\setminus Z),\
 i^!F\in{}^pD^{\ge0}(Z).
\end{aligned}
\tag{16}
\]

Use the same function \(p\) on each manifold's intrinsic dimensions. No codimension shift has been inserted.

For the upper assertion the degree-\(r\) nonzero stalk locus is partitioned by its intersections with \(Z\) and its open complement. Each is the support locus of the stated ordinary restriction. Dimension of the finite union is the maximum of their dimensions, so all upper tests are equivalent.

For the lower assertion point exceptional composition identifies the costalk on \(Z\) with the ambient point costalk of \(F\). On the complement ordinary open restriction retains that same costalk. Thus the degree-wise cosupport has exactly the corresponding partition; the cosupport test proves the second assertion. The operations have the required weak bounded membership by the existing analytic operation theorem. In particular, ordinary restriction cannot replace exceptional restriction in the lower test.

## Exercises with complete solutions

### Two overlap components retain monodromy

*Difficulty: Intermediate.*

Cover a circle by two open arcs \(U,V\), with overlap components \(A,B\). Glue constant rank-one field coefficients by \(\alpha=1\) on \(A\) and \(\alpha=t\ne0\) on \(B\). Orient a traversal so it first passes from \(U\) to \(V\) through \(B\), then returns through \(A\). Compute its monodromy and global cohomology, and explain the sign in (3).

**Solution.** Transport across \(B\) multiplies by \(t\), and the return across \(A\) multiplies by \(1^{-1}=1\), so the monodromy is \(t\). Formula (3) imposes the relation \(\beta_U=\beta_V\alpha\); the minus sign makes it an equality rather than its negative. A one-vertex, one-edge cellular model for the circle with this local coefficient is \(k\xrightarrow{t-1}k\) in degrees zero and one, since the two edge ends are identified by transport \(t\). If \(t\ne1\), the differential is invertible and both groups vanish. If \(t=1\), both are \(k\). The local object is always rank one; global acyclicity does not mean that the glued sheaf is zero.

### Derived morphisms outside the heart can fail descent

*Difficulty: Intermediate.*

For \(p=0\) on a circle, consider \(F=k_X\) and \(G=k_X[1]\) in the ambient derived category. Show that a nonzero global morphism \(F\to G\) can vanish on every sufficiently small arc. Explain why this does not contradict (2).

**Solution.** \(\operatorname{Hom}(k_X,k_X[1])=H^1(X;k)=k\). One explicit computation uses the two-arc cover: its acyclic-cover cochain complex is \(k^2\to k^2\), with \((a,b)\mapsto(b-a,b-a)\), whose cokernel is \(k\). On a contractible arc \(H^1=0\), so every such global morphism restricts to zero. The morphism presheaf is therefore not separated. Here \(G\) has ordinary degree \(-1\) and is outside the \(p=0\) heart. Indeed \(R\mathcal Hom(F,G)=k_X[1]\) has negative cohomology. The Hom sheaf theorem for heart objects excludes this example.

### The support operations have only one guaranteed side

*Difficulty: Intermediate.*

Take \(X=\mathbb R\) and \(Z=\{0\}\). First use \(p(s)=-s\) and \(F=k_X[1]\). Then use \(p=0\) and \(G=k_X\). Show respectively that \(F_Z\) can leave the lower cut and \(R\Gamma_ZG\) can leave the upper cut.

**Solution.** The smooth-stratum tests put \(F=k_X[1]\) in the \(p=-s\) heart; its point costalk is \(k[-1][1]=k\). But \(F_Z=i_*k[1]\), whose point costalk has degree \(-1<p(0)=0\). It is in the upper cut and outside the lower cut. For \(p=0\), \(G=k_X\) is in the ordinary heart. Its supported object is \(R\Gamma_ZG=i_*i^!k_X=i_*k[-1]\), with cohomology in degree one. This is in the lower cut but outside the upper cut. Thus (8) cannot generally be upgraded to two fully t-exact functors.

### The fibre shifts are attained

*Difficulty: Intermediate.*

Let \(f:\mathbb R^d\to\{\mathrm{pt}\}\), \(d>0\), with the usual orientation and \(p=0\). Compute \(f^!k\), its point costalks, and \(Rf_!k_{\mathbb R^d}\). Check the sharp degree boundaries in (11) and (13).

**Solution.** The manifold orientation formula gives \(f^!k=k_{\mathbb R^d}[d]\), with ordinary degree \(-d\). Thus the lower target in (11) must allow degree \(-d\). At a point \(y\), its costalk is \(k[d][-d]=k\), agreeing with (12) and the costalk at the target point. Compact cohomology of the oriented \(d\)-space is \(k[-d]\), in degree \(d\); this follows from its one-point compactification sphere's relative top class. Hence \(Rf_!k_{\mathbb R^d}\) attains the upper target \(d\) in (13). Ordinary \(Rf_*k_{\mathbb R^d}=k\) lies at its lower target zero. These calculations distinguish ordinary degrees from point costalk degrees.

### Zero-dimensional fibres do not ensure constructible images

*Difficulty: Advanced.*

Let \(Y=\mathbb N\) be a discrete zero-manifold, \(X=\mathbb R\), and \(f(m)=1/m\), with \(m\ge1\). Take \(G=k_Y\) over a field, and \(p=0\). Verify the fibre bound and show that the output membership in (13) cannot be dropped.

**Solution.** The map is analytic on every zero-dimensional component. Each nonempty fibre is one point, so \(d=0\). The input is a globally bounded strong heart object with stalk \(k\). Since \(Y\) is discrete, \(G\) is the sheaf coproduct of its point coefficients. Proper-support image commutes with that coproduct, giving
\(Rf_!G=\bigoplus_{m\ge1}k_{\{1/m\}}\) in degree zero. Its stalks are \(k\) at \(1/m\), and zero elsewhere, including zero; this also follows from the point-fibre proper-support comparison. Its nonzero-stalk locus \(\{1/m\}\) is not subanalytic near zero: a one-dimensional subanalytic set has a locally finite analytic partition, so a zero-dimensional locus there cannot contain infinitely many distinct points accumulating at an ambient point.

Thus \(Rf_!G\) is globally bounded but not weakly \(\mathbb R\)-constructible. The actual support is not proper over the compact interval \([0,1]\), whose inverse image is the noncompact discrete set \(Y\). The fibre dimension bound has not supplied the omitted category-membership clause.

### Duality retains a nontrivial orientation line

*Difficulty: Intermediate.*

Let \(M=\mathbb{RP}^2\), take a field of characteristic different from two, and \(p(s)=-\lfloor s/2\rfloor\). Determine the Verdier dual of \(k_M[1]\), its perverse degree, and the role of orientation.

**Solution.** The manifold has real dimension two, with \(p(2)=p^*(2)=-1\). Its constant complex \(k_M[1]\) is in the \(p\)-heart by the smooth-stratum tests. With \(\omega_M=\mathrm{or}_M[2]\), its dual is
\(R\mathcal Hom(k_M[1],\mathrm{or}_M[2])=\mathrm{or}_M[1]\).
This has ordinary degree \(-1\), so belongs to the \(p^*\)-heart. The orientation line on the projective plane has monodromy \(-1\) on its fundamental loop. In the stated characteristic it is not the constant line, and the answer cannot be replaced by \(k_M[1]\). Duality exchanges the dual coefficient and retains the manifold orientation.

### Integral torsion and infinite biduals keep the hypotheses visible

*Difficulty: Advanced.*

At a point, first use \(k=\mathbb Z\), \(p(0)=0\), and \(F=\mathbb Z/2\). Then use a field and \(V=\bigoplus_{\mathbb N}k\). Explain respectively why the field assertion (15) does not extend as stated and why perfectness matters to its heart equivalence.

**Solution.** The finite free resolution \([\mathbb Z\xrightarrow{2}\mathbb Z]\) in degrees \(-1,0\) has derived Hom into \(\mathbb Z\) in degrees zero and one, with differential multiplication by \(2\), up to the harmless dual basis sign. Its only cohomology is \(\mathbb Z/2\) in degree one. Hence \(D F=\mathbb Z/2[-1]\). The input is in the ordinary lower cut, but its dual is outside the dual upper cut zero at this point. The ring is Noetherian and has finite global dimension, and \(F\) is perfect; the missing condition is that coefficient dualization be exact as over a field.

For the second example choose the standard basis of \(V\). Then \(V^\vee=k^{\mathbb N}\). A functional on this product that vanishes on its finite-support subspace but is nonzero on the constant sequence \((1,1,\ldots)\) exists: define it on the span of that sequence modulo the finite-support subspace, and extend a basis. It belongs to \(V^{\vee\vee}\) and is not evaluation by a finite-support vector of \(V\), since vanishing on every basis vector would force all of that vector's coordinates to be zero. Thus the actual evaluation \(V\to V^{\vee\vee}\) is not surjective. The perfect-stalk condition is essential to the asserted contravariant equivalence.

### Countable gluing and nonproper strong images

*Difficulty: Intermediate.*

On \(X=\mathbb N\) let \(U_m=\{1,\ldots,m\}\), with \(p=0\) and compatible coefficients \(F_m=k_{U_m}\) in degree zero over a field. Carry out (6)–(7). For \(a:X\to\{\mathrm{pt}\}\), compare \(Ra_!F\) and \(Ra_*F\) and their strong membership.

**Solution.** On a discrete space all coefficient vector spaces are injective, so \(I_m=F_m\) in degree zero is an allowed model. Extension by zero gives the first \(m\) point coefficients and the transition includes them into the first \(m+1\). Their sheaf colimit has stalk \(k\) at every point and no other cohomology, so \(F=k_X\), with the uniform interval \([0,0]\). Its global ordinary sections are all sequences, \(\prod_{\mathbb N}k\); compact subsets of this discrete space are finite, so compact sections are the finite-support sequences, \(\bigoplus_{\mathbb N}k\). Both section functors are exact here, so these are also \(Ra_*F\) and \(Ra_!F\) in degree zero.

Both outputs satisfy the weak perverse bounds for \(d=0\), but neither is a finite-dimensional coefficient or a perfect complex at the target point. Thus the strong input and the zero-dimensional fibre bound do not imply strong direct-image membership. Countable descent itself kept perfect stalks because it was locally identified with one \(F_m\), rather than taking this nonproper direct image.

## References and the next section

Beilinson, Bernstein and Deligne's [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), §1.4.1–1.4.10, printed pp. 43–49, supplies the open/closed gluing framework behind the preceding t-structure. This lesson uses that proved t-structure and its negative-Hom vanishing, then gives the marked overlap cone and the uniformly bounded countable descent construction explicitly. The formal gluing theorem is not a substitute for that infinite-cover construction. David Massey's [*Notes on Perverse Sheaves and Vanishing Cycles*, arXiv:math/9908107v13](https://arxiv.org/abs/math/9908107v13), §5, records the four holomorphic fibre-dimension bounds and their direct-image membership hypotheses for finite complex-constructible coefficients. Its field duality statement retains the finite coefficient condition. The real dimension estimate, translated general perversity, orientation line and arbitrary weak coefficients here have their own proofs and prerequisite conditions above. Massey's reference notes state these dimension bounds without proofs, so their statements serve as a precise comparison rather than as a claimed proof of this larger result.

The general sheaf prerequisites are reused: the current derived programme's proved open extension, enough injectives, injective restriction and K-injectivity interfaces; the exact open same-lower-bound Stacks injective construction already recorded; the exact filtered stalk-colimit proofs linked above; and the SH-02 exceptional composition, adjunction and projection-formula proofs. These providers retain their prerequisite status. The source passages have not been followed through all their own onward references. Human sources retain their terms; the programme dedication applies only to independently expressed exposition.

Complex middle perversity, its microlocal consequences and the later holomorphic solution and differential-system applications remain subsequent teaching. This lesson proves the stated descent and degree bounds relative to its precise prerequisites; it makes no full-course or transitive-closure claim.
