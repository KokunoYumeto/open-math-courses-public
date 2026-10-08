# Finite coefficients and derived realization

A complex with finite cohomology need not visibly have finite terms. This reading proves how finite subcomplexes preserve objects, morphisms and nullhomotopies, and gives the extra injective-module argument needed for constructible sheaves on a fixed stratification. Four exercises have complete solutions.

*Original teaching text and solutions by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0.*

## Setting and earlier comparisons

Bounded derived categories, cohomology truncations, ordinary sheaf adjunctions and the published derived-category foundations linked below are prerequisites. The algebraic comparisons cover arbitrary left Noetherian rings where stated; torsion and the injective construction use commutative Noetherian or finitely generated commutative algebras with their precise hypotheses.

The earlier fixed-stratification reading proves the unrestricted realization criterion. Its equation 31 defines the finite normal stratifications used below: compatible ball-times-cone neighborhoods, connected manifold strata and incident link pieces with finitely many connected components. Its equation 26 is the stalkwise adjunction embedding into a finite sum of stratum direct images. Its equation 35 proves unrestricted realization for the three torus-orbit strata of the projective line. This reading supplies the separate finite-heart argument, and uses those exact earlier results only at the identified applications.

Equations 36–49 retain their locators in the existing derived-constructibility lesson. A union of finite-dimensional monodromy modules is called ind-finite; it may itself have infinite-dimensional stalks.

## Passing from finite cohomology to the finite heart

The fixed-stratification theorem has an unrestricted heart: its stalk modules need not be finite. We now prove the additional comparison for finite stalks. The two mechanisms are different. A Noetherian module calculation produces finite subcomplexes. For constructible sheaves, suitable injectives first make the same finite extraction possible.

The modern reference is Lunts and Schnürer's [*Categories of constructible sheaves*](https://arxiv.org/html/2601.05477v1), including its finite-type variants. The full arguments below retain the distinction between modules annihilated by an ideal and modules annihilated by a power of it. They also spell out faithfulness, where a nullhomotopy must survive the finite replacement.

We use the programme's published [derived-category foundations](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/complexes-cones-and-localization.html#4-fractions-at-quasi-isomorphisms) for roofs and common refinements, and [bounded-below injective comparison](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html#3-complexes-that-admit-comparison-maps). Those foundations retain their stated human attribution and GFDL terms; their expression is not imported here. All derived categories in the new finite-heart comparisons are bounded.

### A finite subcomplex that retains specified data

Let \(\mathcal A\) be an abelian category, and let \(\mathcal F\subset\mathcal A\) be a Serre subcategory of Noetherian objects. Thus subobjects, quotients and extensions of its objects remain in \(\mathcal F\), and ascending chains of subobjects of each such object stabilize. Suppose the terms of a bounded-below complex \(J\) are directed unions of their subobjects in \(\mathcal F\), and the same is true of their subobjects. Assume \(H^n(J)\in\mathcal F\), with only finitely many nonzero cohomology objects.

We require the following detection property: if a directed union maps epimorphically onto an object of \(\mathcal F\), some member does so. For finite modules this follows by lifting a finite set of generators. For finite-stratum, finite-stalk sheaves it follows by stabilization of the images on one stalk in each stratum. Directedness then combines the finitely many choices.

**Finite extraction lemma.** Every bounded subcomplex \(D\subset J\) with terms in \(\mathcal F\) is contained in a bounded subcomplex \(K\subset J\) with terms in \(\mathcal F\) such that

\[
D\subset K\subset J,\qquad H^n(K)\xrightarrow{\sim}H^n(J)
\quad\text{for every }n.
\tag{36}
\]

**Proof.** Choose \(a\) with \(J^n=0\) for \(n<a\), and choose \(b\) at least as large as the top degree of \(D\) and of the nonzero cohomology of \(J\). In degree \(b\), choose a finite subobject of \(Z^b(J)\) surjecting onto \(H^b(J)\), and add \(D^b\). This still lies in \(Z^b(J)\), because \(D^{b+1}=0\).

Suppose \(K^n\) has been chosen. The object \(K^n\cap B^n(J)\) is finite, by the Serre property. Its preimage under \(J^{n-1}\to B^n(J)\) is a union of finite subobjects. The detection property supplies one whose differential maps onto that intersection. Separately choose a finite subobject of \(Z^{n-1}(J)\) mapping onto \(H^{n-1}(J)\). Add both choices and \(D^{n-1}\) inside the preimage of \(K^n\). Their finite sum is \(K^{n-1}\). The inclusion of \(D^{n-1}\) is allowed because \(dD^{n-1}\subset D^n\subset K^n\).

The new boundaries of \(K\) in degree \(n\) are exactly \(K^n\cap B^n(J)\). Thus the cohomology map in that degree is injective. The previously chosen cycle representatives make it surjective. Descend through the finite interval \(b,b-1,\ldots,a\). In degree \(a\), there are no ambient boundaries, because \(J^{a-1}=0\); surjectivity from the chosen cycles is therefore also injectivity there. Put \(K^n=0\) outside the interval. Above \(b\), both cohomologies vanish. This proves (36). \(\square\)

A useful relative form needs no finite preimage under a quotient: add the specified finite data at each step of this construction. In particular, images of maps from bounded finite complexes, and images of a specified homotopy, can all be retained.

### Finitely generated modules inside all modules

**Proposition.** For a left Noetherian ring \(A\), writing \(\operatorname{mod}_{fg}(A)\) for its finitely generated left modules, inclusion induces

\[
D^b(\operatorname{mod}_{fg}(A))
\xrightarrow{\sim}
D^b_{fg}(\operatorname{Mod}(A)).
\tag{37}
\]

No finite global dimension is required.

**Proof.** Every module is the directed union of its finitely generated submodules. Submodules of finitely generated modules are finitely generated because \(A\) is left Noetherian. Apply (36) to a bounded representative \(C\) with finitely generated cohomology, taking \(D=0\). It gives a bounded finite subcomplex \(K\to C\) that is a quasi-isomorphism, proving essential surjectivity.

For fullness, an ambient morphism between bounded finite complexes is a left roof \(F\leftarrow C\to G\), whose left arrow is a quasi-isomorphism. Its middle complex has finite cohomology. Replace \(C\) by the finite \(K\subset C\) just constructed and restrict both maps. The resulting roof is entirely finite and represents the same morphism.

For faithfulness, take a finite roof whose ambient morphism is zero. The common-refinement and cancellation criterion in the linked foundations supplies a bounded quasi-isomorphism into its middle complex on which its numerator is nullhomotopic. That new middle complex again has finite cohomology. Replace it by a finite subcomplex and restrict the maps and homotopy. The left composite remains a quasi-isomorphism, and the restricted homotopy still kills the numerator. This is a finite witness that the source roof is zero. Differences of two roofs reduce to this case. \(\square\)

### The quotient criterion in its full abelian generality

**Proposition.** Let \(\mathcal B\) be a strictly full abelian subcategory of an abelian category \(\mathcal A\), with exact inclusion, closed under extensions. Suppose every \(M\in\mathcal A\) has a subobject \(N\) such that \(M/N\in\mathcal B\) and \(N\) has no nonzero subobject belonging to \(\mathcal B\). Then

\[
D^b(\mathcal B)\xrightarrow{\sim}D^b_{\mathcal B}(\mathcal A).
\tag{38}
\]

**Proof.** Take a bounded complex \(C\) with cohomology in \(\mathcal B\). Beginning at its lowest degree, let \(t\) be the first degree whose term is not yet in \(\mathcal B\). The boundaries and cycles through this degree belong to \(\mathcal B\). Indeed the bottom boundary is zero; if \(B^i(C)\in\mathcal B\), its extension by \(H^i(C)\) gives \(Z^i(C)\in\mathcal B\), and for \(i<t\) the cokernel of \(Z^i(C)\to C^i\), a map between objects of \(\mathcal B\), gives \(B^{i+1}(C)\in\mathcal B\). Thus \(Z^t(C)\in\mathcal B\).

Choose \(P\subset C^t\) as in the hypothesis. The intersection \(P\cap Z^t(C)\) is the kernel of the map \(Z^t(C)\to C^t/P\). Both its source and target belong to \(\mathcal B\); exact abelian inclusion puts its kernel in \(\mathcal B\). The hypothesis on \(P\) makes that kernel zero. Consequently \(d:P\to dP\) is an isomorphism. Quotient out the acyclic subcomplex

\[
P\xrightarrow{\,d\,}dP
\quad\text{in degrees }t,t+1.
\tag{39}
\]

The quotient has its term of degree \(t\) in \(\mathcal B\), changes no earlier terms, and has the same cohomology. Repeat through the finite degree interval. At the final degree the same argument forces \(P=0\) if it would have a zero outgoing differential. We obtain a quasi-isomorphism \(C\to C'\) with all terms in \(\mathcal B\).

Represent morphisms by right roofs \(F\to C\leftarrow G\). Compose both maps with this quotient replacement. This proves fullness and essential surjectivity. For faithfulness, the right-fraction cancellation criterion represents an ambient zero by a quasi-isomorphism out of the roof's middle complex on which its numerator is nullhomotopic. Apply the same quotient replacement to that complex and compose the homotopy with the quotient. All maps and that homotopy then have terms in \(\mathcal B\), because both their sources and targets do. The resulting right roof is zero already in \(D^b(\mathcal B)\). \(\square\)

This proof does not require arbitrary subobject closure of \(\mathcal B\). The intersection is controlled by a kernel between two of its own objects. That distinction retains the full abelian and extension-closed form of the criterion.

### Ideal-power torsion retains the extensions

Let \(A\) now be commutative Noetherian, let \(J\subset A\) be an ideal, and let \(\mathcal T_J\) consist of finitely generated modules killed by some power of \(J\). This is a Serre subcategory of \(\operatorname{mod}_{fg}(A)\). In an extension, if powers \(J^r\) and \(J^s\) kill the outer terms, then \(J^{r+s}\) kills the middle term.

We reuse the full Artin–Rees proof. That reading proves the statement for every ideal of every commutative Noetherian ring; it is not restricted to analytic local rings.

For a finite module \(M\), put \(T=\{m:J^rm=0\text{ for some }r\}\). It is a submodule and is finite. A single power \(J^r\) kills it, by taking the maximum of the exponents for finitely many generators. Artin–Rees supplies \(c\) such that

\[
T\cap J^nM=J^{n-c}(T\cap J^cM)=0
\qquad(n\geq c+r).
\tag{40}
\]

Choose \(N=J^nM\) at such a degree. Its quotient is in \(\mathcal T_J\); it has no nonzero \(\mathcal T_J\)-subobject, because every element of such a subobject would lie in \(T\cap N\). Apply (38), then (37), to obtain

\[
D^b(\mathcal T_J)
\xrightarrow{\sim}
D^b_{\mathcal T_J}(\operatorname{Mod}(A)).
\tag{41}
\]

This result is about power torsion. Replacing \(\mathcal T_J\) by the modules annihilated by \(J\) gives a different, generally false assertion, as the earlier \(k[t]\) exercise proves. The extension \(k[t]/(t^2)\) is retained in (41).

### Zero-dimensional support gives a second finite subcategory

For any commutative Noetherian \(A\), let \(\mathcal C\) be the finite modules whose support has dimension zero. Equivalently these are the modules of finite length. Here is the equivalence without an Artinian-ring theorem. Every nonzero finite module has a nonzero element with prime annihilator: choose an annihilator maximal among annihilators of nonzero elements, using the ascending-chain condition. If \(ab\) annihilates the element and \(b\) does not, the nonzero element obtained by multiplication by \(b\) has a larger annihilator containing \(a\); maximality proves primality. Apply this observation successively to quotients to build a prime cyclic filtration. The ascending-chain condition on submodules makes the filtration finite. With zero-dimensional support every prime in it is maximal, so its cyclic factors are simple. Conversely a finite filtration by simple modules has support in its finitely many maximal ideals.

The finite-length modules form a Serre subcategory. In a finite module \(M\), the sum \(T\) of all its finite-length submodules is finite length: the increasing finite sums stabilize by Noetherianity. If \(T=0\), choose \(N=M\) in (38). Otherwise take a composition series of \(T\), and let \(J\) be the product of the annihilator maximal ideals of its factors. The product ideal kills \(T\), by applying the successive annihilators along the filtration. The quotient \(A/J\) has finite length. Indeed, for the successive products, each ideal-layer quotient is a finite module over one of those residue fields, and the ring is Noetherian.

Every \(A/J^n\) has finite length too, by its finite filtration with layers \(J^i/J^{i+1}\), finite over \(A/J\). Artin–Rees gives \(T\cap J^nM=0\) for sufficiently large \(n\). Thus \(N=J^nM\) has finite-length quotient and no nonzero finite-length subobject. Equations (38) and (37) prove

\[
D^b(\mathcal C)\xrightarrow{\sim}
D^b_{\mathcal C}(\operatorname{Mod}(A)).
\tag{42}
\]

This supplies the full zero-dimensional-support comparison, including roofs and their equality, rather than just an object replacement.

### Injectives that remain unions of finite-dimensional modules

Fix a field \(k\). An \(A\)-module is **ind-finite** if it is the union of its finite-dimensional \(A\)-submodules. The required embedding condition says that every ind-finite module embeds in an injective \(A\)-module that is itself ind-finite. We prove this condition for every finitely generated commutative \(k\)-algebra.

**Proposition.** Let \(A\) be a finitely generated commutative \(k\)-algebra. For any injective \(A\)-module \(E\), the submodule

\[
\Gamma_{ft}(E)=\{e\in E:\dim_k(Ae)<\infty\}
\tag{43}
\]

is injective. Consequently the required ind-finite injective embeddings exist.

**Proof.** A sum of two finite-dimensional cyclic submodules is finite, so (43) is a submodule and is ind-finite. The Hilbert basis theorem, proved in the linked Artin–Rees component, makes \(A\) Noetherian.

Use [Baer's criterion](https://kokunoyumeto.github.io/open-math-courses-public/courses/derived-categories-and-sheaf-operations/injective-modules-and-bounded-below-derived-functors.html#2-functorial-injective-embeddings), with its full ideal-extension proof. Let \(L\subset A\) be an ideal and \(f:L\to\Gamma_{ft}(E)\) a map. The ideal has finitely many generators; their images lie in a single finite-dimensional submodule. Hence the image of \(f\) is annihilated by a finite-codimensional ideal \(J\): take its annihilator, since its action factors through its finite-dimensional endomorphism algebra. Artin–Rees for \(L\subset A\) gives, for some \(n\),

\[
L\cap J^n\subset JL\subset\ker f.
\tag{44}
\]

The map therefore descends to \((L+J^n)/J^n\subset A/J^n\). Injectivity of \(E\) extends it to \(A/J^n\to E\). If \(y\) is the image of one, then \(J^ny=0\), and multiplication by \(y\) extends \(f\) to \(A\).

This extension lands in (43): \(A/J^n\) is finite-dimensional. To check that assertion, \(J\) is finitely generated, and every layer \(J^i/J^{i+1}\) is a finite module over the finite-dimensional algebra \(A/J\). A finite filtration of \(A/J^n\) by those layers proves the assertion. Baer's criterion now proves injectivity.

For an ind-finite module \(M\), take the coinduced injective \(E=\operatorname{Hom}_k(A,M)\), with \((a\varphi)(b)=\varphi(ba)\). The adjunction \(\operatorname{Hom}_A(-,E)=\operatorname{Hom}_k(-,M)\) makes it injective because vector spaces are injective. The map

\[
M\longrightarrow E,\qquad m\longmapsto (b\longmapsto bm)
\tag{45}
\]

is linear and monic, as evaluation at one recovers \(m\). Its image is ind-finite, so it lies in \(\Gamma_{ft}(E)\). This gives the required embedding. \(\square\)

This is a direct Artin–Rees and Baer proof of the needed condition. It avoids requiring a classification of indecomposable injective modules as an additional prerequisite. The classical torsion-injectivity comparison is also present in the [AI Integrated Stacks Project](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/dualizing.tex#L335); that mathematical reference retains the Stacks project authors' credit and its own reuse terms.

### Finite extraction for constructible sheaves

Let \((Y,\mathcal S)\) have a finite normal stratification as in (31): connected manifold strata, compatible ball-cone neighborhoods, and finitely many connected components in each incident link piece. Work over a field \(k\). Write \(\mathcal A=\operatorname{Cons}_k(Y,\mathcal S)\), \(\mathcal F=\operatorname{Cons}_{ft,k}(Y,\mathcal S)\), and let \(\mathcal I\) be the objects whose stratum monodromy modules are ind-finite. Assume each group algebra \(k[\pi_1(S)]\) has the ind-finite injective embedding condition.

The finite-stalk category \(\mathcal F\) is Serre inside \(\mathcal A\): restriction is exact, kernels and quotients of finite-dimensional vector spaces are finite, and an extension adds the two dimensions. Its objects are Noetherian: an ascending sequence of constructible subobjects stabilizes on a chosen stalk in each of the finitely many connected strata, hence everywhere.

For a stratum inclusion \(s:S\hookrightarrow Y\), ordinary \(s_*\) carries finite local systems to finite-stalk sheaves. The boundary stalk is \(H^0(L_{x,S};L)\); its dimension is at most the sum of the stalk dimensions over the finitely many connected link components. For an ind-finite local system, this stalk is a union of the \(H^0\) groups of finite sub-local-systems. A section is determined by an invariant vector on each component, and finitely many such vectors lie together in a finite-dimensional monodromy submodule. Invariance is preserved inside that submodule. Consequently \(s_*\) carries an ind-finite local system to a union of finite-stalk constructible subsheaves.

Every \(G\in\mathcal I\) is itself a union of finite-stalk subsheaves. The adjunction diagonal embeds it into \(\bigoplus_Ss_*(G|_S)\), by the same stalkwise argument as (26). Each summand is a directed union of finite-stalk sheaves by the preceding calculation. Intersect \(G\) with those finite stages. Each intersection is constructible and finite-stalk, and their union is \(G\). This argument supplies actual lifts across the attachments; merely declaring that a quotient has smaller support would not supply them.

The embedding condition on the group algebras gives injective ind-finite local systems \(I_S\) containing \(G|_S\). Therefore

\[
G\hookrightarrow \bigoplus_{S\in\mathcal S}s_*I_S
\quad\text{is an embedding into an injective object of }\mathcal A
\text{ belonging to }\mathcal I.
\tag{46}
\]

Adjunction to exact restriction makes each summand injective; the sum is finite. Ind-finite monodromy modules are closed under submodules and quotients. The embedding condition also proves extension closure: embed the submodule of an extension into an ind-finite injective, extend that map across the middle module, and combine it with the quotient map. This embeds the middle module in the sum of that injective and the ind-finite quotient. Thus \(\mathcal I\) is a Serre subcategory and (46) can be iterated on cokernels.

The published bounded-below resolution construction applies within \(\mathcal I\) while keeping the terms injective in \(\mathcal A\). In its one-degree pushout step, direct sums and quotients remain in \(\mathcal I\). Each degree stabilizes after finitely many steps, so no additional infinite-limit assertion is required. Every bounded complex in \(\mathcal I\) therefore has a quasi-isomorphism to a bounded-below complex of \(\mathcal A\)-injectives in \(\mathcal I\).

**Finite-heart theorem.** Under these conditions, inclusion induces

\[
D^b(\mathcal F)\xrightarrow{\sim}D^b_{ft}(\mathcal A).
\tag{47}
\]

**Proof.** First consider \(F,G\in\mathcal F\) and all their shifts. Choose a bounded-below injective resolution \(G[m]\to J\) as above. Its cohomology is bounded and finite-stalk. Every morphism \(F\to G[m]\) in the ambient derived category is represented by a chain map \(f:F\to J\), using the published K-injective comparison.

The images of \(f\) and \(G[m]\to J\) form a bounded finite subcomplex \(D\subset J\). The hypotheses of (36) hold: all terms and subobjects are unions of finite-stalk subsheaves, as proved above, and a finite-stalk quotient is detected at finitely many stratum stalks. Obtain a finite bounded \(K\subset J\) containing \(D\). The resulting right roof \(F\to K\leftarrow G[m]\) realizes the prescribed morphism. This proves fullness on shifted heart objects.

For faithfulness, take a finite right roof \(F\to K\leftarrow G[m]\) with ambient value zero. Resolve its finite middle complex by \(q:K\to J\) with \(J\) as above. The numerator into \(J\) is nullhomotopic, by the K-injective comparison. Include in \(D\) the images of \(q(K)\) and of every component of that homotopy. Close under the differential. There are only finitely many such degrees because \(F\) and \(K\) are bounded; all these images and their finite sums are finite-stalk. Apply (36) retaining this \(D\). The map \(K\to K'\subset J\) is a quasi-isomorphism, and the same homotopy has values in \(K'\). Thus the roof is zero in \(D^b(\mathcal F)\). This proves injectivity of Hom, rather than just lifting its elements.

Finite cohomology truncation triangles generate all bounded objects from shifted heart objects. Apply the two long exact Hom sequences and finite induction on their amplitudes: the heart Hom comparison just proved implies full faithfulness on every bounded pair. Essential surjectivity follows by the same finite truncation induction. Realize each cohomology object in \(\mathcal F\); lift the connecting morphism using full faithfulness; its cone realizes the next truncation. The finite number of cohomological degrees terminates the construction. \(\square\)

If the unrestricted fixed-stratification realization criterion also holds, compose (47) with its finite-cohomology restriction to obtain the ambient finite-stalk sheaf equivalence. Equation (47) itself does not assume that boundary comparison.

### Finitely generated abelian monodromy and the finite projective-line theorem

For a finitely generated abelian group \(G\), the algebra \(k[G]\) is a finitely generated commutative \(k\)-algebra: use finitely many group generators and their inverses as algebra generators. Equations (43)–(45) verify the embedding condition. Thus for a finite normal stratification with such stratum groups,

\[
D^b(\operatorname{Cons}_{ft,k}(Y,\mathcal S))
\xrightarrow{\sim}
D^b_{ft}(\operatorname{Cons}_k(Y,\mathcal S)).
\tag{48}
\]

No semisimplicity of \(k[G]\) or finite global dimension of that algebra is required.

For the three torus-orbit strata of \(\mathbb P^1(\mathbb C)\), the groups are \(\mathbb Z,0,0\). The unrestricted realization was proved in (35). Combining it with (48) now proves the previously separate finite-heart statement:

\[
D^b(\operatorname{Cons}_{ft,k}(\mathbb P^1,\{\mathbb C^*,0,\infty\}))
\xrightarrow{\sim}
D^b_{\{\mathbb C^*,0,\infty\},ft}(\mathbb P^1;k).
\tag{49}
\]

It holds over every field. The general normal toric-variety application still needs its full orbit-star cone geometry and link-map calculation, beyond the explicit projective line. The finite-heart step for its finitely generated abelian stratum groups is now supplied by (48).

## Further exercises on finite terms and derived equality

### Two nilpotent extensions retain a degree-two class

*Difficulty: Advanced.*

Let \(A=k[x,y]\), \(J=(x,y)\), \(M_x=A/(x^2,y)\), \(M_y=A/(x,y^2)\). Show that the sequence \(0\to k\to M_x\to M_y\to k\to0\), whose middle map sends \(1\) to \(y\), represents a nonzero ambient degree-two class. Explain why ideal-power torsion retains it while modules annihilated by \(J\) lose it.

**Solution.** The first map sends \(1\) to \(x\); the last is the residue quotient. The middle map is linear because \(x^2y=0\) and \(y^2=0\) in \(M_y\). Its kernel is \(kx\) and image is \(ky\), proving exactness. The Koszul free resolution of \(k\) has differentials \(A^2\to A\), \((a,b)\mapsto xa+yb\), and \(A\to A^2\), \(c\mapsto(-yc,xc)\). Exactness follows because a relation \(xa+yb=0\) has \(b=xc\) and \(a=-yc\) in the polynomial ring. Applying Hom into \(k\) gives zero differentials, so \(\operatorname{Ext}^2_A(k,k)=k\).

Lift \(1\in A\) to \(1\in M_y\). The first Koszul differential then has values \(0,y\). Lift those through \(M_x\to M_y\) by \(0,1\). On the second differential this lift gives \(-y\cdot0+x\cdot1=x\), which is the image of \(1\in k\). Thus the extension represents the nonzero scalar \(1\), including the chosen sign. Both middle terms are killed by \(J^2\), so the entire two-extension belongs to \(\mathcal T_J\). Modules annihilated by \(J\) are vector spaces over \(A/J=k\) and have no degree-two extensions. The power-torsion category in (41) retains the actual middle terms.

### Finite coefficients may need infinite injective resolutions

*Difficulty: Intermediate.*

Prove that no nonzero finite-dimensional \(k[t,t^{-1}]\)-module is injective in the category of all modules. Explain how this is compatible with (48).

**Solution.** A finite-dimensional module \(V\) has a nonzero annihilating polynomial \(p(t)\), because the powers of its endomorphism \(t\) are linearly dependent. In the Laurent ring this polynomial is nonzero. A nonzero injective module over this domain is divisible by \(p\): for any \(v\), the map from the ideal \(pA\) sending \(pa\) to \(av\) extends to \(A\), and its value \(w\) at one satisfies \(pw=v\). On \(V\), however, multiplication by \(p\) is zero. Surjectivity then forces \(V=0\). Equations (46) and (47) use injectives that are unions of finite-dimensional submodules, usually infinite-dimensional themselves. Finite extraction retains the bounded object, its morphisms and homotopies; it does not require finite-dimensional injective terms.

### A nullhomotopy requires more than the image of its map

*Difficulty: Intermediate.*

Let \(J\) be \(k\xrightarrow{\mathrm{id}}k\) in degrees \(-1,0\), and let \(F=k[0]\). The map \(F\to J\) is identity in degree zero. Show why retaining only its image cannot witness its ambient vanishing, and construct the finite witness.

**Solution.** The image alone is the subcomplex \(k[0]\subset J\), with nonzero \(H^0\). The map to that image is identity, so is not zero in its derived category. The homotopy into \(J\) has component \(h^0:F^0\to J^{-1}\) equal to identity; then \(dh+hd\) is the original map. Add that degree-\(-1\) image. The resulting finite subcomplex is all of \(J\), contractible by this same homotopy. Thus the map vanishes there. This is why faithfulness in (47) explicitly retains homotopy images, rather than stopping after fullness.

### Abelian monodromy does not imply a semisimple group algebra

*Difficulty: Advanced.*

Let \(\operatorname{char}k=p>0\) and \(G=C_p\). Compute the positive self-extensions of its trivial representation. Does the algebraic embedding argument for (48) require their vanishing?

**Solution.** Write \(A=k[G]=k[z]/(z^p)\), with \(z=g-1\). A free resolution of \(k=A/(z)\) alternates multiplication by \(z\) and \(z^{p-1}\). Their kernels are respectively \(z^{p-1}A\) and \(zA\), so the resolution is exact, including \(p=2\), when both maps are \(z\). Applying \(\operatorname{Hom}_A(-,k)\) makes every differential zero. Hence \(\operatorname{Ext}^n_A(k,k)=k\) for all \(n\geq0\). The algebra is nevertheless finitely generated and commutative, so (43)–(45) apply. The finite-heart comparison preserves these classes; it does not assert their vanishing. This example concerns the algebraic embedding condition, without asserting that this group occurs as an aspherical finite-dimensional manifold's fundamental group.

## Sources and reuse

Lunts and Schnürer's [Categories of constructible sheaves](https://arxiv.org/html/2601.05477v1), January 2026, supplies the modern finite-type comparison questions and theorems. The Stacks project authors are credited for the algebra and derived foundations in the linked AI Integrated Stacks edition. Guillaume Valette is credited for the results of the linked analytic finiteness reading, which supplies the full Artin–Rees proof. The published derived-sheaf course retains its GFDL terms. Their expression is not imported or relicensed here. This original exposition, four complete solutions and reader code are CC0. Self-checked by the writing AI.

[Reading index](../index.html) · [Reuse terms](../LICENSE.txt) · Provenance
