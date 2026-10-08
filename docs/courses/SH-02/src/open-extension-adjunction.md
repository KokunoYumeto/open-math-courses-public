# Open extensions and ambient supports

An open change of ambient space in supported sections is governed by an exact adjunction. This original supporting lesson proves the comparison used in the convex-open Fourier section formula. Original expression is dedicated under CC0 1.0.

## SH02-OEA-ADJUNCTION — Open extension and supported derived sections

Let $j:U\hookrightarrow X$ be an open inclusion of topological spaces, and let $k$ be a commutative unital ring. No local compactness, dimension bound or finiteness assumption on the coefficient modules is needed for this result.

**Proposition.** For a sheaf $A$ of $k$-modules on $U$ and $F\in D^+(k_X)$ there is a natural isomorphism
\[
R\operatorname{Hom}_{k_X}(j_!A,F)
\xrightarrow{\sim}
R\operatorname{Hom}_{k_U}(A,j^{-1}F).
\tag{OEA1}
\]
It is the derived comparison of the open-extension adjunction, with unit $A\to j^{-1}j_!A$ and counit $j_!j^{-1}G\to G$.

**Proof.** For an open subset $V\subset X$, put $P_A(V)=A(V)$ when $V\subset U$, and put $P_A(V)=0$ otherwise. Use the original restrictions when both opens lie in $U$, and the zero maps in the remaining cases. The sheafification of this presheaf of $k$-modules is $j_!A$. The $k$-linear structure of sheafification can be checked directly: represent two germs on a common smaller open set, add their representatives there, and multiply a representative by the given scalar. Equality of germs makes these operations independent of the representatives. Applying these local operations to locally represented sections gives a sheaf of $k$-modules. A presheaf morphism into a sheaf extends uniquely by gluing its values on such representatives; its extension is $k$-linear because this is checked on the same common open sets. Sheafification leaves each stalk unchanged. For a sheaf $G$ on $X$, a presheaf morphism $P_A\to G$ is determined exactly by its components on opens contained in $U$. On every other open its source is zero; compatibility across a restriction from such an open is automatic. These components are precisely a sheaf morphism $A\to G|_U$. The universal property of sheafification therefore gives the bifunctorial $k$-linear adjunction
\[
\operatorname{Hom}_{k_X}(j_!A,G)
\simeq\operatorname{Hom}_{k_U}(A,j^{-1}G).
\tag{OEA2}
\]
The unit is the identity after restriction. The counit extends the restricted sections by zero where their supports permit this; on stalks it is the identity inside $U$ and the zero-source map outside $U$. These descriptions also fix the triangle identities, either from the displayed adjunction or directly on stalks.

The stalk of $j_!A$ is $A_x$ on $U$ and zero outside $U$. Hence $j_!$ is exact. Open restriction is exact as well. Choose a bounded-below injective resolution $F\to I^\bullet$. Each $j^{-1}I^m$ is injective: applying its Hom functor to a short exact sequence on $U$ is, by OEA2, applying the exact functor $\operatorname{Hom}_{k_X}(-,I^m)$ after the exact functor $j_!$. Thus $j^{-1}I^\bullet$ is an injective resolution computing $j^{-1}F$. Apply OEA2 term by term. Its naturality makes the Hom-complex differentials agree, and gives
\[
\operatorname{Hom}_{k_X}(j_!A,I^\bullet)
\simeq\operatorname{Hom}_{k_U}(A,j^{-1}I^\bullet).
\]
These complexes compute the two sides of OEA1. This proves the stated comparison and its naturality. $\square$

If $C$ is closed in $U$, its locally closed coefficient extension in $X$ is $k_C^X=j_!k_C^U$. Taking $A=k_C^U$ in OEA1 identifies
\[
R\Gamma_C(X;F)\simeq R\Gamma_C(U;j^{-1}F),
\tag{OEA3}
\]
where global supported sections mean derived Hom from the indicated locally closed coefficient sheaf. No assertion that $C$ is closed in $X$ is used. The inverse of OEA3 is the second comparison in CAX3 for the open base-restricted ambient bundle. Empty $U$ or $C$ gives two zero complexes.

The sheaf-level mathematical antecedent is [Stacks Tag 00A7](https://stacks.math.columbia.edu/tag/00A7), whose module-sheaf adjunction proof is omitted. The construction above supplies that verification and its required derived form. Exactness is also the stalkwise specialization of [Tag 01AK](https://stacks.math.columbia.edu/tag/01AK), with the $k$-linear check given in SH02-PRP-E2. The underlying sheafification and stalk facts are [Tags 0080](https://stacks.math.columbia.edu/tag/0080) and [007Z](https://stacks.math.columbia.edu/tag/007Z); the coefficient verification above also supplies the constant-ring case of [Tag 0089](https://stacks.math.columbia.edu/tag/0089). Existence and use of bounded-below injective resolutions are the exact imports SH02-IMP-INJECTIVE and SH02-IMP-DERIVE. No exceptional-image construction enters.
