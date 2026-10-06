# Perverse support, costalks and truncation triangles

A perversity assigns a degree to each possible stratum dimension. Ordinary restrictions impose the upper bound; exceptional restrictions impose the lower bound. The construction below turns these dimension-dependent bounds into a t-structure by extending a truncation triangle across one closed dimensional layer at a time. Its closed-layer correction uses an exceptional restriction, and an octahedron gives the ordinary restriction of the new lower object.

*Original programme exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026; source comparison and editorial revision by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently expressed programme text is dedicated under CC0. Human sources retain their own terms.*

Let \(k\) be a commutative ring of finite global dimension. Let \(X\) be a finite-dimensional real analytic manifold, with the usual Hausdorff and countability hypotheses for the sheaf operations. Write \(n=\dim X\), initially constant on components; the same argument works componentwise with a uniform dimension bound. Our category is the globally bounded category \(D^b_{\mathrm{w}\text{-}\mathbb R\mathrm c}(X;k)\). Weak constructibility permits arbitrary stalk modules. Strong constructibility requires perfect stalk complexes; the strong version of the truncation theorem below additionally assumes that \(k\) is Noetherian.

The fixed-stratification microsupport criterion, dimensional filtration, bounded weak sheaf operations, and flat cellular dualizing model supply the geometric and coefficient prerequisites. The abstract truncation theorem supplies uniqueness, functoriality and the abelian heart once the t-structure axioms have been proved here. Their recorded foundational dependencies retain their own status.

## The line-heart extension poses the problem

Begin on the real line with its two open halves and the origin, and choose \(p(s)=-s\). The open-layer heart degree is \(-1\); at the origin the upper stalk bound and the lower costalk bound are both zero. These are the stratum tests proved below. The interval attachment calculation already computes both restrictions without invoking the perverse existence theorem.

Over a field, consider \(i_*k\), \(j_!k_{I\setminus\{0\}}[1]\), and \(k_I[1]\). Their origin stalks are respectively \(k\), zero, and \(k[1]\). Their origin costalks are respectively \(k\), \(k\oplus k\), and \(k\), all in degree zero. To obtain the latter two, take the fibre of \(0\to k\oplus k\) or of the diagonal \(k\to k\oplus k\), then shift by \([1]\). Both open restrictions of either nonsupported object have degree \(-1\). Thus all three satisfy the two stratum bounds.

The localization triangle, shifted by one, is
\[
 j_!k[1]\longrightarrow k_I[1]\longrightarrow i_*k[1]
          \longrightarrow j_!k[2].
 \tag{P1}
\]
After the general theorem below proves the t-structure, its heart sequence is
\[
 0\longrightarrow i_*k\longrightarrow j_!k[1]
       \longrightarrow k_I[1]\longrightarrow0.
 \tag{P2}
\]
The injection is the connecting map of (P1). It cannot split: ordinary restriction at the origin would identify the zero stalk of its middle term with \(k\oplus k[1]\). The complete exercise below also checks this heart sequence. This is the motivating question: how can the truncation construction preserve the extension arrows when ordinary stalks do not even detect this epimorphism?

## Calculate the origin correction before the induction

Keep the same perversity and now use the integral sheaf \(E\) from the fixed interval diagram. Its attachments are \(2q\) and \(q\), where \(q(a,b)=a+2b\), and \(u=(-2,1)\). Its point stalk is \(\mathbb Z^2\). Its exceptional restriction is the actual fibre
\[
 i^!E=[\,\mathbb Z^2\xrightarrow{\ (2q,q)\ }\mathbb Z^2\,]
       \quad\text{in degrees }0,1,
 \tag{P3}
\]
whose cohomology is \(\mathbb Zu\) in degree zero and \(\mathbb Z\) in degree one. The target quotient is identified by \((x,y)\mapsto x-2y\).

Here is every arrow of the closed-layer construction (15)–(18), before its general induction. On \(U=I\setminus\{0\}\), ordinary degree zero lies strictly above \(p(1)=-1\). Thus \(A_U=0\) and \(B_U=E|_U\). The first triangle is \(0\to E\xrightarrow{1}G\), with \(G=E\). Its closed correction is
\[
 C=\tau^{\le p(0)}i^!G=\mathbb Zu,\qquad
 i_*C\xrightarrow{\ \epsilon\ }G\longrightarrow B.
 \tag{P4}
\]
The counit \(\epsilon\) is zero on the open halves and is \(z\mapsto(-2z,z)\) at the origin. Both attachments kill that vector, so this is a morphism of diagrams. It is a monomorphism at every stalk. Its cone \(B\) is therefore represented by the ordinary quotient diagram
\[
 \mathbb Z\xleftarrow{\ 2\ }\mathbb Z\xrightarrow{\ 1\ }\mathbb Z,
 \qquad E\longrightarrow B=(\,1,q,1\,).
 \tag{P5}
\]
The new lower object is \(A=i_*C\), and the other triangle is \(A\to E\to B\). The octahedral triangle \(j_!A_U\to A\to i_*C\) is \(0\to i_*C\xrightarrow{1}i_*C\).

Ordinary restriction gives \(i^{-1}A=C\). Exceptional restriction of (P5) gives \([\,\mathbb Z\xrightarrow{(2,1)}\mathbb Z^2\,]\), whose only cohomology is \(\mathbb Z\) in degree one. This is exactly \(\tau^{\ge1}i^!G\). On the open layer, \(B|_U\) has degree zero, which is \(p(1)+1\); at the origin its costalk starts in degree \(p(0)+1=1\). The supported object \(A\) satisfies both point bounds and has zero open restrictions. These explicit tests are the local instance of the complete stratum criterion proved next.

Replacing \(i^!G\) by \(i^{-1}G=\mathbb Z^2\) would instead select all of \(\mathbb Z^2\). It supplies no arrow \(i_*\mathbb Z^2\to E\) with identity at the origin: naturality would require both nonzero attachment maps to vanish. The ordinary adjunction supplies \(G\to i_*i^{-1}G\), in the opposite direction. For \(G=k_I\), the original exercise makes the obstruction even sharper:
\(\operatorname{Hom}(i_*k,k_I)=\operatorname{Hom}(k,k[-1])=0\).
The required counit, cutoff and costalk bound therefore all point to the exceptional restriction.

The calculation used a ring of finite global dimension and retained all maps. It supplies no substitute for the arbitrary-module singular-subset estimate, dimensional filtration, microlocal adaptation and finite-stage argument below. Those are the obligations that extend this origin calculation to the full theorem.

## Perversities and degree conventions

For \(p:\mathbb Z\to\mathbb Z\), put

\
 p^*(s)=-p(s)-s,\qquad p[a=p(a+s).
 \tag{1}
\]

A **perversity** has both \(p\) and \(p^*\) nonincreasing. Taking the difference between consecutive arguments proves

\[
 p(s)-p(s+1)\in\{0,1\},\qquad
 0\le p(s)-p(t)\le t-s\quad(s<t).
 \tag{2}
\]

Conversely the first condition makes both maps nonincreasing, and summing it gives the second. Dualizing the translated dual gives

\[
 \bigl(p^*[a]\bigr)^*(s)=p(a+s)+a.
 \tag{3}
\]

This translation of the dimension argument differs from adding a constant to all degrees. We retain the convention that \([1]\) lowers cohomological degree. Thus a module \(M[-r]\) has cohomology in degree \(r\).

For a constructible cohomology sheaf, its nonzero-stalk locus and its closed carrier have the same dimension: on a locally finite compatible stratification the carrier is the union of the closures of the occupied strata, and frontier strata have smaller dimension. Either gives the support dimension below. The empty locus has dimension \(-\infty\).

Define the two cuts by

\[
\begin{aligned}
F\in{}^pD^{\le0}
 &\Longleftrightarrow
 \dim\operatorname{supp}H^jF<a
       \text{ whenever }j>p(a),\\
F\in{}^pD^{\ge0}
 &\Longleftrightarrow
 H^j(i_T^!F)=0
       \text{ whenever }j<p(\dim T),
       \text{ for every locally closed subanalytic }T\subset X.
\end{aligned}
\tag{4}
\]

The first line is equivalently the bound on the support of \(\tau^{>p(a)}F\), since there are only finitely many cohomology degrees. Set \({}^pD^{\le r}={}^pD^{\le0}[-r]\) and similarly for the lower cut.

Only \(p(0),\ldots,p(n)\) matter. In the upper test arguments \(a>n\) give an automatic dimension bound. If \(a<0\), then \(p(a)\ge p(0)\), and the \(a=0\) test already eliminates every degree in question. Nonempty subsets in the lower test have dimension between zero and \(n\); the empty test is vacuous.

If \(p\le q\) on those arguments, (4) gives \({}^pD^{\le0}\subset{}^qD^{\le0}\) and \({}^pD^{\ge0}\supset{}^qD^{\ge0}\). For \(a\le p(s)\le b\) throughout \(0\le s\le n\),

\[
 D^{\le a}\subset{}^pD^{\le0}\subset D^{\le b},
 \qquad
 D^{\ge b}\subset{}^pD^{\ge0}\subset D^{\ge a}.
 \tag{5}
\]

For the upper inclusions use the degree bound and then the support test at zero. For the lower inclusions use that \(i_T^!\), a right derived support/restriction operation, preserves every ordinary lower bound; for the last inclusion take \(T=X\). These arguments also show directly that \(p=0\) gives the ordinary t-structure.

The origin model only tested two smooth pieces and a point. To justify the lower test for every locally closed subanalytic subset, we now use the flat cellular dualizing model. Its finite free cochains retain torsion and arbitrary modules; a field-only duality shortcut would not supply this estimate.

## A costalk bound with arbitrary coefficients

We need a lower bound on a singular subset, including nonflat and infinitely generated coefficients. Let \(M\) be an \(m\)-manifold, \(L\) a bounded complex with locally constant cohomology on \(M\), and \(T\subset M\) locally closed subanalytic of dimension \(t\). Then

\[
 L\in D^{\ge r}(M)
       \quad\Longrightarrow\quad
 i_T^!L\in D^{\ge r+m-t}(T).
 \tag{6}
\]

Here is the coefficient argument. Locally on a small contractible neighborhood \(L\) is a constant bounded derived coefficient \(P\). One way to see this without splitting its cohomology is to peel its finite Postnikov tower: local systems are constant there, and the higher extension groups of constant coefficients are computed by module Ext, since the contractible neighborhood has no higher constant-sheaf cohomology. The extension maps and their cones therefore also come from coefficients.

Exceptional tensor comparison gives a natural map
\(i_T^!k_M\otimes^L P_T\to i_T^!P_M\). It is an isomorphism for these coefficients. To check this assertion, make \(T\) closed in the local ambient open set and use a compatible locally finite triangulation, also compatible with a chosen point. A small star has only finitely many incident simplices. The complement of the closed subcomplex retracts onto its barycentric complement, so the relative pair computing the supported stalk has a bounded finite free cochain model. Tensoring that relative model with any bounded coefficient complex computes the same pair with those coefficients. The comparison is the relative-cochain tensor map, hence is an isomorphism on every stalk. This uses the triangulation prerequisite, with its recorded lower geometric dependencies.

Exceptional composition, the manifold orientation formula, and that comparison give

\[
 i_T^!L\simeq
 \omega_T\otimes^L i_T^{-1}L
       \otimes i_T^{-1}\mathrm{or}_M^{-1}[-m].
 \tag{7}
\]

The actual cellular model for \(\omega_T\) has terms in \([-t,0]\): in degree \(-d\) it has locally finite sums of constant orientation lines on closed \(d\)-simplices, extended by zero. Each term is flat, as is checked on stalks. This bounded flat complex is K-flat. Represent \(L\) with terms zero below \(r\), using an ordinary smart lower cut. The tensor in (7) then has terms zero below \(r-t\); the shift \([-m]\) raises the lower bound to \(r+m-t\). Orientation lines are invertible flat coefficients. This proves (6). Merely knowing the cohomological degrees of \(\omega_T\) would not justify this tensor bound.

In particular, \(L\in D^{\ge p(m)}\) satisfies every lower perverse test inside \(M\), because
\(p(m)+m-t\ge p(t)\) by (2).

For a point in an \(s\)-dimensional smooth stratum \(S\), the same relative cochain calculation is the orientation generator of a ball relative to its puncture:

\[
 i_x^!F\simeq
 \mathrm{or}_{S,x}\otimes(i_S^!F)_x[-s]
 \quad\text{if }i_S^!F\text{ has locally constant cohomology}.
 \tag{8}
\]

The degree of its \(j\)th cohomology is therefore \(j-s\) in \(i_S^!F\), with the orientation line retained.

## Lower bounds reconstructed through a closed filtration

Let \(\varnothing=T_{-1}\subset T_0\subset\cdots\subset T_N=T\) be a finite closed filtration, with layers \(V_m=T_m\setminus T_{m-1}\). For a bounded-below \(H\) on \(T\), suppose all \(i_{V_m,T}^!H\) lie in \(D^{\ge r}(V_m)\). Then \(H\in D^{\ge r}(T)\).

Indeed the exact coefficient sequence
\(0\to k_{V_m}\to k_{T_m}\to k_{T_{m-1}}\to0\)
and derived internal Hom into \(H\) give

\[
 R\Gamma_{T_{m-1}}H\longrightarrow
 R\Gamma_{T_m}H\longrightarrow
 Ri_{V_m,T*}i_{V_m,T}^!H\longrightarrow.
 \tag{9}
\]

The last object retains the ordinary lower bound \(r\): ordinary derived direct image is left t-exact, as proved for right derived left exact functors in the preceding lesson. Starting with zero, the long exact cohomology sequence inductively gives the same bound for every supported object. At \(T_N=T\) this object is \(H\). The proof is finite even when each layer has infinitely many locally finite components.

## Ordinary and exceptional restrictions on strata

Take a locally finite subanalytic stratification \(X=\bigsqcup_\alpha S_\alpha\) with equidimensional strata of dimension \(s_\alpha\). The respective local constancy hypotheses give

\[
\begin{aligned}
 F\in{}^pD^{\le0}
 &\Longleftrightarrow i_\alpha^{-1}F\in D^{\le p(s_\alpha)}
       &&\text{if all }i_\alpha^{-1}F\text{ are locally constant},\\
 F\in{}^pD^{\ge0}
 &\Longleftrightarrow i_\alpha^!F\in D^{\ge p(s_\alpha)}
       &&\text{if all }i_\alpha^!F\text{ are locally constant}.
\end{aligned}
\tag{10}
\]

For the first line the dimension of a support is the largest dimension of an occupied stratum. If a stratum of dimension \(s\) violates its degree bound, the test at \(a=s\) fails. Conversely a nonzero degree \(j>p(a)\) on a stratum with \(s\ge a\) would also satisfy \(j>p(s)\), which is impossible.

Necessity in the second line follows by taking \(T=S_\alpha\) in (4). For sufficiency fix locally closed subanalytic \(T\) of dimension \(t\), and make it closed in an ambient open neighborhood. Intersect it with the closed dimensional filtration of the stratification. On an \(m\)-dimensional layer the disjoint strata are open and closed within that layer, and their exceptional restrictions are locally constant in degrees at least \(p(m)\). For the intersection \(V\) with \(T\), of dimension \(v\le t\), (6) gives a bound \(p(m)+m-v\ge p(v)\ge p(t)\). Exceptional composition identifies this object with \(i_{V,T}^!i_T^!F\). Apply (9) to \(H=i_T^!F\) with lower bound \(p(t)\). This proves the test for every \(T\), including singular \(T\).

Here and below the finite closed dimensional filtration is provided by the frontier condition: union of the strata of dimension at most \(m\) is closed. Its layers can have arbitrarily many locally finite components.

The stratum criterion has now identified the degree obligations. To perform the closed-layer correction we also need every cone and boundary extension to remain on one adapted stratification; the bounded weak sheaf-operation proof and fixed-stratification criterion supply this next obligation.

## Keeping the chosen microlocal stratification

Fix a \(\mu\)-stratification \(\Sigma\) adapted to \(F\), and write \(\Lambda_\Sigma=\bigcup_\alpha T^*_{S_\alpha}X\). The fixed-stratification criterion gives locally constant ordinary restrictions from \(\operatorname{SS}(F)\subset\Lambda_\Sigma\). Exceptional restrictions also have locally constant cohomology on these same strata.

To verify the latter assertion, make \(S\) closed in a local ambient open set. Then
\(i_*i^!F=R\mathcal Hom(k_S,F)\).
The full limiting-sum Hom estimate gives

\[
 \operatorname{SS}(i_*i^!F)
 \subset \operatorname{SS}(F)\widehat{+}T_S^*X.
 \tag{12}
\]

Above \(S\) this set is contained in \(T_S^*X\), by the defining \(\mu\)-condition. This includes the witnesses with unbounded covectors. Indeed the second summand is already conormal to \(S\); cancellation with covectors of any approaching stratum can contribute only a conormal to \(S\). A covector limit outside that conormal would violate that condition. The exact closed-embedding microsupport formula now gives zero intrinsic microsupport for \(i^!F\). The local constancy criterion on \(S\) proves the assertion for arbitrary coefficients.

We also need the boundary extension assertion from the fixed-stratification proof: extension by zero from the complement of a closed dimensional layer preserves the bound \(\operatorname{SS}\subset\Lambda_\Sigma\). Its boundary estimate uses the same approaching-stratum \(\mu\)-condition, including the limiting covectors. Closed pushforward of a locally constant object on the new smooth layer has conormal microsupport. Shifts and finite cones preserve the bound. Ordinary smart cuts of a locally constant derived object have locally constant cohomology. These facts show that every object used in the construction below remains adapted to \(\Sigma\).

## Negative internal Hom vanishes

If \(F\in{}^pD^{\le0}\) and \(G\in{}^pD^{\ge0}\), then

\[
 R\mathcal Hom(F,G)\in D^{\ge0}(X),\qquad
 U\longmapsto\operatorname{Hom}_{D(U)}(F|_U,G|_U)
       \text{ is a sheaf}.
 \tag{13}
\]

**Proof.** Put \(Q=R\mathcal Hom(F,G)\). The bounded weak-constructibility theorem puts \(Q\) in a globally bounded weak category, also with arbitrary stalk coefficients. Suppose it has negative cohomology, and let \(\ell<0\) be its lowest nonzero degree. Choose a top-dimensional smooth piece \(S\) of the support of \(H^\ell Q\), of dimension \(t\), open in that support. Locally at a generic point make \(S\) closed in the ambient open set. The support of each \(H^jF\) with \(j>p(t)\) has dimension less than \(t\); the union is finite. Avoid its closure on this top-dimensional piece and shrink again. We now have
\(i_S^{-1}F\in D^{\le p(t)}\) and \(i_S^!G\in D^{\ge p(t)}\).

The exact exceptional internal-Hom comparison is
\[
 i_S^!Q\simeq R\mathcal Hom(i_S^{-1}F,i_S^!G).
 \tag{14}
\]
Its ordinary lower bound is zero. The comparison is the bounded first-argument theorem, proved from projection formula and the evaluation adjunction; it does not require \(F\) to be perfect.

On the other hand \(i_S^!\) preserves ordinary lower bounds. Apply it to the lowest-degree truncation triangle
\(H^\ell Q[-\ell]\to Q\to\tau^{\ge\ell+1}Q\).
It identifies
\(H^\ell(i_S^!Q)=i_S^{-1}\Gamma_S H^\ell Q\).
Locally the sheaf on the right is \(H^\ell Q|_S\), nonzero by our choice of \(S\). This contradicts the lower bound zero. Hence \(Q\in D^{\ge0}\).

Ordinary derived global sections preserve this lower bound, and their degree zero is \(\Gamma(U,H^0Q)\). The internal-Hom/global-Hom identification therefore identifies the presheaf in (13), including its restriction maps, with the sheaf \(H^0Q\). This proves both assertions. \(\square\)

For \(G\in{}^pD^{\ge1}\), write \(G=G_0[-1]\) with \(G_0\in{}^pD^{\ge0}\). The shift of (13) gives \(R\mathcal Hom(F,G)\in D^{\ge1}\) and thus \(\operatorname{Hom}(F,G)=0\).

We have the two inputs needed for the construction: the degree tests and preservation of its adapted strata. Negative Hom gives uniqueness once the triangles exist. The finite dimensional filtration now makes the origin calculation into a finite sequence of corrections, using the same counit and octahedral arrows.

## Building the truncation triangle across a closed layer

The categorical mechanism is the gluing theorem of Beilinson, Bernstein and Deligne, *Faisceaux pervers*, §1.4.1–1.4.10, printed pp. 43–49. Its two closed tests differ: ordinary restriction controls the upper cut, exceptional restriction controls the lower cut. The source constructs a truncation using an adjunction arrow and an octahedron. Here the dual form of that two-step construction starts with extension by zero and then removes the low exceptional closed-layer part. The finite dimensional filtration and the uniform cohomological interval are the extra ingredients that keep this construction inside the present globally bounded weakly constructible category. The formal gluing theorem alone does not prove those geometric or boundedness facts.

**Theorem.** The pair \(({}^pD^{\le0},{}^pD^{\ge0})\) is a bounded t-structure on \(D^b_{\mathrm{w}\text{-}\mathbb R\mathrm c}(X;k)\). If \(k\) is Noetherian, it restricts to a bounded t-structure on \(D^b_{\mathbb R\mathrm c}(X;k)\).

**Proof.** The shifts in (4) give the required inclusions
\({}^pD^{\le0}\subset{}^pD^{\le1}\) and
\({}^pD^{\ge1}\subset{}^pD^{\ge0}\).
Orthogonality was proved after (13). It remains to construct, for every \(F\), an actual triangle \(A\to F\to B\to A[1]\) with \(A\in{}^pD^{\le0}\), \(B\in{}^pD^{\ge1}\).

Choose the finite closed \(\mu\)-filtration
\(\varnothing=X_{-1}\subset X_0\subset\cdots\subset X_n=X\),
where \(M_m=X_m\setminus X_{m-1}\) is an \(m\)-manifold, possibly disconnected, and the chosen restrictions of \(F\) are locally constant. This is the increasing version of the written negative-index filtration: \(X_m=F_{-m}\). Its approaching-layer condition is retained by this reindexing.

Start with the zero triangle on \(X\setminus X_n=\varnothing\). Suppose a suitable adapted triangle \(A_U\to F|_U\to B_U\to\) has been constructed on \(U=X\setminus X_m\). Put \(E=X\setminus X_{m-1}\). Its new layer \(i:M_m\hookrightarrow E\) is closed, and \(j:U\hookrightarrow E\) is its open complement. Use the counit to form

\[
 j_!A_U\longrightarrow F|_E\longrightarrow G\longrightarrow,
 \qquad C=\tau^{\le p(m)}i^!G.
 \tag{15}
\]

Use the actual ordinary truncation arrow and the closed counit for the map
\(i_*C\to i_*i^!G\to G\). Complete it to a triangle, and take the fibre of the composite from \(F|_E\):

\[
 i_*C\longrightarrow G\longrightarrow B\longrightarrow,
 \qquad A\longrightarrow F|_E\longrightarrow B\longrightarrow.
 \tag{16}
\]

The octahedral axiom applied to \(F|_E\to G\to B\) and the first triangle of (15) gives

\[
 j_!A_U\longrightarrow A\longrightarrow i_*C
       \longrightarrow j_!A_U[1].
 \tag{17}
\]

The relevant restrictions of these actual triangles are

\[
\begin{aligned}
 j^{-1}A&\simeq A_U,& j^{-1}B&\simeq B_U,\\
 i^{-1}A&\simeq C,&
 i^!B&\simeq\tau^{\ge p(m)+1}i^!G.
\end{aligned}
\tag{18}
\]

For the first row use \(j^{-1}i_*=0\) and \(j^{-1}G=B_U\). For \(i^{-1}A=C\) use (17), \(i^{-1}j_!=0\), and \(i^{-1}i_*=\mathrm{id}\). For the last identity apply \(i^!\) to the first triangle of (16); \(i^!i_*=\mathrm{id}\), and its first arrow is exactly the smart truncation arrow. Notice that \(i^{-1}G\) was not used to define \(C\).

All the objects remain adapted to the chosen filtration. The boundary extension assertion puts \(j_!A_U\) in the required microlocal bound; the first cone does the same for \(G\). By (12), \(i^!G\) is locally constant on \(M_m\), so its smart cut \(C\) is also locally constant. Closed pushforward and the two remaining cones preserve the microlocal bound. Their ordinary and exceptional restrictions on every stratum are consequently locally constant. The tests (10) and (18) now prove \(A\in{}^pD^{\le0}(E)\) and \(B\in{}^pD^{\ge1}(E)\).

Descending through \(m=n,\ldots,0\) ends on \(X\). Every operation is globally bounded: open extension and closed pushforward are exact, exceptional restrictions have the finite uniform amplitude of the weak-constructibility theorem, and a finite number of ordinary cuts, shifts and cones preserves a finite interval. There are \(n+1\) stages, regardless of how many components the layers have. Thus the constructed triangle lies in the stated globally bounded category.

For the strong version start with perfect stalks. Exceptional restriction preserves them by the proved perfect-operation theorem. On a locally constant perfect complex, a smart cut has bounded finitely generated cohomology over a Noetherian ring. Finite global dimension then makes that cut perfect, by the coefficient criterion in the fixed-stratification lesson. Extensions by zero and closed pushforward have the original or zero stalks, and finite cones of perfect stalks are perfect. The induction therefore stays strong.

Finally (5) proves boundedness of the t-structure. If \(F\in D^{[u,v]}\) and \(a\le p(s)\le b\), then
\(F\in{}^pD^{\le v-a}\cap{}^pD^{\ge u-b}\).
These are finite perverse bounds. This finishes the proof. \(\square\)

The abstract uniqueness theorem now identifies \(A={}^p\tau^{\le0}F\) and \(B={}^p\tau^{\ge1}F\), with their truncation arrows, independently of the choices of cones and filtration. It also gives natural truncation functors and the abelian heart \({}^pD^{\le0}\cap{}^pD^{\ge0}\). Formula (5) places the ordinary cohomology of a heart object inside \([a,b]\).

The induction used finitely many dimensions, not finitely many strata or connected components. Noetherianity enters only the stated strong perfect-stalk truncation assertion.

## Point cosupport and its dimension threshold

Define the degree-wise point cosupport by
\(\operatorname{cosupp}^jF=\{x:H^j(i_x^!F)\ne0\}\).
Choose a stratification with locally constant exceptional restrictions; the fixed microlocal argument in the next section supplies one for our objects. Formula (8) yields

\[
 \operatorname{cosupp}^jF
  =\bigcup_\alpha
     \operatorname{supp}_{S_\alpha}
          H^{j-s_\alpha}(i_\alpha^!F),
 \qquad
 F\in{}^pD^{\ge0}
  \Longleftrightarrow
 \dim\operatorname{cosupp}^jF<a
       \text{ whenever }j<p(a)+a.
 \tag{11}
\]

These loci are subanalytic: each support is a union of open and closed stratum components, and the family is locally finite. To prove the equivalence, note that \(p(s)+s\) is nondecreasing. A cosupport stratum of dimension \(s\ge a\) would have \(j\ge p(s)+s\ge p(a)+a\), a contradiction. Conversely a stratum violating its lower bound gives \(j-s<p(s)\), and the cosupport test fails at \(a=s\). The threshold \(j<p(a)+a\) is exactly \(-j>p^*(a)\).

Over a field, a perfect stalk identifies \(i_x^{-1}D_XF\) with the dual of \(i_x^!F\), so its degree \(-j\) support is the degree \(j\) cosupport. The criterion (11) itself uses arbitrary weak coefficients and needs no such finite-dual identification.

## Transverse restriction with its codimension and orientations

The target perversities must be calculated from the dimension of the intersected stratum and the relative orientation shift. Formula (19) gives that calculation. Exercise 7 tests the tempting dimension-based targets against constant sheaves on a three-manifold and a transverse line; both tests fail. The codimension and orientation calculation supplies the formulas used here with the same arbitrary coefficients as above.

Let \(Y\subset X\) be a real analytic \(d\)-manifold transverse to every stratum of a \(\mu\)-stratification adapted to \(F\), and put \(c=n-d\). Write \(h:Y\hookrightarrow X\) and \(N=\mathrm{or}_{Y/X}\), the relative orientation line. For \(q=p[c]\), the correct implications are

\[
 F\in{}^pD^{\ge0}(X)\ \Longrightarrow\
     h^{-1}F\in{}^{q}D^{\ge0}(Y),
 \qquad
 F\in{}^pD^{\le0}(X)\ \Longrightarrow\
     h^!F\in{}^{q+c}D^{\le0}(Y).
 \tag{19}
\]

Here \((q+c)(r)=p(r+c)+c=(p^*[c])^*(r)\); it is a perversity. Transversality makes \(h\) noncharacteristic, and the canonical orientation comparison gives

\[
 h^!F\simeq h^{-1}F\otimes N[-c].
 \tag{20}
\]

This is the bounded noncharacteristic comparison, with its specified evaluation/trace map, from the existing sheaf-operation programme. A transverse intersection \(T=S\cap Y\) has dimension \(r=s-c\), and the pullback conormal estimate makes the restrictions adapted to the induced strata.

For the lower implication compose exceptional inclusions:
\(i_{T,Y}^!h^!F=i_{T,S}^!i_{S,X}^!F\).
The right side is \(i_{S,X}^!F|_T\otimes\mathrm{or}_{T/S}[-c]\), by the smooth-subset case of (7). Apply (20) to the left side. The two shifts \([-c]\) cancel, giving
\[
 i_{T,Y}^!h^{-1}F
  \simeq i_{S,X}^!F|_T
       \otimes\mathrm{or}_{T/S}\otimes N|_T^{-1}.
\]
The invertible orientation factors do not change degrees. The bound is therefore \(p(s)=p(r+c)=q(r)\); (10) proves the assertion. For the upper implication ordinary restriction of (20) has its top degree at \(p(s)+c\), which is \((q+c)(r)\). Apply the upper stratum test. This proves (19), including the nonoriented case.

## Exercises with complete solutions

### Consecutive steps and dual translation

*Difficulty: Introductory.*

Show that \(p(s)=-\lfloor s/2\rfloor\) is a perversity on all integers. Compute \(p^*\) and \((p^*[2])^*\). Explain why a dimension translation need not equal a degree shift.

**Solution.** Consecutive differences of \(\lfloor s/2\rfloor\) are zero or one, including negative integers. Hence (2) applies. The identity \(s-\lfloor s/2\rfloor=\lceil s/2\rceil\) gives \(p^*(s)=-\lceil s/2\rceil\). Formula (3) gives \((p^*[2])^*(s)=-\lfloor(s+2)/2\rfloor+2=1-\lfloor s/2\rfloor\). A translation by one changes \(p\) by zero on one parity and by minus one on the other, whereas a degree shift adds the same integer at every argument.

### Infinite coefficients on a smooth stratum

*Difficulty: Intermediate.*

On an oriented connected three-manifold take the preceding perversity and a nonzero constant module \(L=\bigoplus_{\mathbb N}k\). Determine the perverse degree-zero object associated to \(L\), its point costalk degree, and the equality case in (11).

**Solution.** With the single smooth stratum, (10) requires ordinary degree \(p(3)=-1\) for the heart. Thus \(L[1]\) belongs to the weak heart. Formula (8) gives \(i_x^!L[1]=L[1-3]=L[-2]\), so its point costalk is in degree two. The degree-two cosupport is the whole three-manifold. The threshold at \(a=3\) is \(p(3)+3=2\); it is a strict inequality, so degree two is allowed. For \(a\le3\), \(p(a)+a\le2\), and for \(a>3\) the required dimension bound is automatic. Infinite generation does not affect the calculation; this object generally fails the strong perfect-stalk condition.

### A singular subset and a nonflat coefficient

*Difficulty: Advanced.*

Let \(M=\mathbb R^2\), \(T=[0,\infty)\times\{0\}\), and \(L\) be the constant module \(\bigoplus_{\mathbb N}\mathbb Z/2\) in degree zero, with coefficient ring \(\mathbb Z\). Compute \(i_T^!L\), including the endpoint, and compare with (6).

**Solution.** The flat closed-edge cellular model of the half-ray dualizing complex has \(\omega_T=\mathbb Z_{(0,\infty)}[1]\): the endpoint stalk is an acyclic edge-to-vertex complex with differential a unit, while an interior stalk is \(\mathbb Z[1]\). Formula (7), with the plane oriented, gives \(i_T^!L=L_{(0,\infty)}[-1]\), extended by zero to \(T\). Interior cohomology is \(L\) in degree one; the endpoint stalk is zero. The uniform lower bound is \(0+2-1=1\), attained in the interior. The endpoint cancellation remains valid after tensoring because its differential is a unit; no flatness of \(L\) was assumed. By contrast restricting exceptionally straight to the endpoint in the plane gives \(L[-2]\) in degree two. These are different inclusions and different calculations.

### A nonsplit exact sequence in the real perverse heart

*Difficulty: Advanced.*

Work over a field on \(X=\mathbb R\), stratified by its two half-lines and the origin. Let \(p(s)=-s\), \(j:X\setminus\{0\}\hookrightarrow X\), \(i:\{0\}\hookrightarrow X\). Show that \(i_*k\), \(j_!k[1]\), and \(k_X[1]\) are in the heart, and derive a nonsplit short exact sequence among them.

**Solution.** The open restrictions of the last two objects have degree \(-1=p(1)\); their point restrictions have degree \(-1\) or are zero, satisfying the upper bound \(p(0)=0\). The costalk of \(k_X[1]\) at zero is \(k[-1][1]=k\). The supported localization triangle for \(j_!k\) has zero stalk at zero and punctured-neighborhood cohomology \(k\oplus k\) in degree zero; thus \(i^!j_!k=(k\oplus k)[-1]\). After \([1]\) its costalk has degree zero. The skyscraper has ordinary and exceptional point restriction \(k\), and zero open restrictions. Both stratum tests now hold for all three.

Shift the localization triangle \(j_!k\to k_X\to i_*k\to\) by \([1]\). Its third object is \(i_*k[1]\), which has perverse cohomology \(i_*k\) in degree \(-1\) and zero in degree zero. The long exact heart sequence gives
\[
 0\longrightarrow i_*k\longrightarrow j_!k[1]
       \longrightarrow k_X[1]\longrightarrow0.
\]
The first map is the connecting arrow of that localization triangle. If the sequence split, ordinary restriction to zero would identify \(0=i^{-1}j_!k[1]\) with \(k\oplus k[1]\), which has nonzero cohomology in two degrees. Hence it is nonsplit. An epimorphism in this heart can have zero ordinary source stalk at the point; the perverse lower bound concerns costalks.

### Why the closed correction uses an exceptional restriction

*Difficulty: Intermediate.*

Keep the line stratification and \(p(s)=-s\), but take \(F=k_X\) in ordinary degree zero. Perform (15)–(18) at the origin. Explain why replacing \(i^!G\) by \(i^{-1}G\) cannot give the same construction.

**Solution.** On the open one-dimensional layer \(F\) is above the perverse cutoff \(-1\), so \(A_U=0\) and \(B_U=k_U\). Consequently \(G=k_X\). Its exceptional point restriction is \(k[-1]\), in ordinary degree one. Since \(p(0)=0\), \(C=\tau^{\le0}k[-1]=0\). We obtain \(A=0\) and \(B=k_X\). This is correct: its open exceptional restriction has degree zero, at least \(p(1)+1=0\), and its point costalk has degree one, at least \(p(0)+1=1\).

The ordinary point restriction is instead \(k\), whose cut at zero is nonzero. There is no counit \(i_*i^{-1}G\to G\); the ordinary adjunction has its unit in the other direction. Indeed \(\operatorname{Hom}(i_*k,k_X)=\operatorname{Hom}(k,i^!k_X)=\operatorname{Hom}(k,k[-1])=0\). The attempted correction has neither the required arrow nor the costalk bound of (18).

### Internal Hom remembers the direction of the map

*Difficulty: Intermediate.*

For \(F=i_*k\) and \(G=k_X[1]\) in the same heart, compute \(R\mathcal Hom(F,G)\) and \(R\mathcal Hom(G,F)\). Check (13), its strict-cut consequence, and the sheaf restriction maps.

**Solution.** Closed exceptional adjunction gives
\(R\mathcal Hom(i_*k,k_X[1])=i_*R\operatorname{Hom}(k,i^!k_X[1])=i_*k\).
In the other direction a constant rank-one first argument gives
\(R\mathcal Hom(k_X[1],i_*k)=i_*k[-1]\).
The first object has degree zero and the second degree one; neither has negative cohomology. Replacing \(G\) by \(G[-1]\in{}^pD^{\ge1}\) shifts the first Hom to \(i_*k[-1]\), with no degree-zero global Hom. On an open set containing zero the degree-zero Hom for the original direction is \(k\); on one avoiding zero it is zero. Its restriction maps are precisely those of the skyscraper sheaf \(H^0R\mathcal Hom(F,G)\).

### Check the transverse corollary on constant sheaves

*Difficulty: Advanced.*

Test the proposed targets \(p[d]\) for \(h^{-1}F\) in the lower cut and \(p[-d]\) for \(h^!F\) in the upper cut, when \(Y\) is \(d\)-dimensional. Use \(X=\mathbb R^3\), \(Y\) a line, and a single ambient stratum. Verify the corrected targets (19) in both tests.

**Solution.** First take \(p(s)=-s\) and \(F=k_X[3]\). Its exceptional restriction to the sole three-dimensional stratum has degree \(-3=p(3)\), so (10) puts it in the lower cut. On the line \(h^{-1}F=k_Y[3]\) has degree \(-3\), below the proposed lower bound \(p1=p(2)=-2\). Thus that assertion fails.

Second take \(p=0\) and \(F=k_X\), in the ordinary upper cut. The relative orientation line is constant here and \(h^!F=k_Y[-2]\), with cohomology in degree two. The proposed perversity \(p[-1]\) is still zero, so the proposed upper cutoff zero fails.

In (19) the codimension is \(c=2\). In the first test \(q(1)=p(3)=-3\), exactly the actual lower degree. In the second \(q+c=2\), exactly the actual upper degree. The examples disprove the proposed dimension-based targets under definitions (1) and (4). The derivation of (19) supplies the valid codimension-based targets, with arbitrary coefficients and the relative orientation line.

### Infinitely many components still require one global bound

*Difficulty: Intermediate.*

Let \(X=\mathbb N\) with its discrete zero-manifold structure. Compare the complexes with stalks \(F_m=k[-m]\) and \(G_m=\bigoplus_{\mathbb N}k\) in degree zero. Explain which enters the weak bounded theorem and how its truncation is obtained.

**Solution.** Every stalk of \(F\) is a bounded locally constant complex, but \(H^mF\ne0\) for arbitrarily large \(m\). Thus \(F\) is not in the globally bounded category of the theorem. For \(G\), the same interval \([0,0]\) works at all points, so it is weakly constructible and bounded, despite its infinite coefficients and infinitely many components. The dimensional filtration has one layer, \(M_0=X\), and the construction is the ordinary smart cut at \(p(0)\): \(C=\tau^{\le p(0)}G\), \(A=C\), \(B=\tau^{\ge p(0)+1}G\). If \(p(0)\ge0\), then \(A=G,B=0\); if \(p(0)<0\), then \(A=0,B=G\). Finite stages and a uniform degree interval, rather than a finite number of components, are the boundedness requirements. Infinite generation prevents a strong claim for \(G\).

## References and the remaining programme

Beilinson, Bernstein and Deligne's [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), §1.4.1–1.4.10, printed pp. 43–49, supplies the open/closed categorical gluing framework and its octahedral proof. David Massey's [*Notes on Perverse Sheaves and Vanishing Cycles*, arXiv:math/9908107v13](https://arxiv.org/abs/math/9908107v13), §2 and §5, records the complex support/cosupport conventions and truncation tests for finite constructible coefficients over a regular Noetherian ring of finite Krull dimension. Those notes give these comparison statements without full proofs. Neither source passage is used as a blanket theorem for the arbitrary-rank real cuts here. The singular-subset estimate, finite closed reconstruction, uniform bounds, microlocal membership and transverse orientation calculation are the particular supplied arguments that establish that larger scope. The locally closed subanalytic-space variant still needs its ringed-space and dualizing prerequisites and remains a separate programme target.

The exact SH-02 prerequisites are Exceptional operations, EX-HOM, Manifold duality, MD-SUBMERSION, and Characteristic estimates, CHE-005, the bounded noncharacteristic orientation comparison. Their coefficient ranges, maps and lower foundational obligations remain part of the dependency claim. Ordinary derived foundations are reused. Human source material retains its own terms; the CC0 dedication covers the programme's independently expressed text and examples.

Continue with perverse descent and fibre-dimension bounds, then complex middle perversity and exterior products. These written lessons use the truncation constructed here; later differential-system applications remain part of the active programme. The subanalytic-space extension, finer source atomization, lower geometric foundations and independent review also remain open. 
