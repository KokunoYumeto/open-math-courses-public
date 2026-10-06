# Descent along proper surjective morphisms

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A singular variety \(X\) is the image of its resolution \(R(X)\), which is smooth. To build a finite étale cover of \(X\) from one of \(R(X)\), we need to know when a cover of \(R(X)\) comes from \(X\). The answer is descent: a cover of \(R(X)\) together with an identification of its two pull-backs to \(R(X)\times_XR(X)\), satisfying a cocycle condition, comes from a unique cover of \(X\). This lesson proves this for every proper surjective morphism of noetherian schemes, and the analogous, easier, statement for covering spaces.

The algebraic proof reduces in three steps to a statement over a field, where descent along faithfully flat morphisms applies. It uses the equivalence between finite étale covers of a proper scheme over a henselian local ring and those of its closed fibre, proved in the AI Integrated Stacks Project, and descent of affine schemes along faithfully flat morphisms. We use [Connectedness and full faithfulness](connectedness-and-full-faithfulness.md) for the description of morphisms by graphs.

## 1. Descent data

Let \(g:S'\to S\) be a morphism of schemes, \(S''=S'\times_SS'\) and \(S'''=S'\times_SS'\times_SS'\), with projections \(p_1,p_2:S''\to S'\) and \(p_{12},p_{13},p_{23}:S'''\to S''\). For a finite étale \(Y'\to S'\), a *descent datum* is an isomorphism \(\varphi:p_1^*Y'\to p_2^*Y'\) over \(S''\) with

\[
p_{13}^*\varphi=p_{23}^*\varphi\circ p_{12}^*\varphi\qquad\text{over }S'''.
\]

A morphism of descent data \((Y'_1,\varphi_1)\to(Y'_2,\varphi_2)\) is a morphism \(u:Y'_1\to Y'_2\) over \(S'\) with \(\varphi_2\circ p_1^*u=p_2^*u\circ\varphi_1\). Every finite étale \(Y\to S\) gives the descent datum \((g^*Y,\mathrm{can})\), where \(\mathrm{can}\) is the identification of both pull-backs with the pull-back of \(Y\) to \(S''\). This defines a functor

\[
\operatorname{F\acute Et}(S)\longrightarrow\operatorname{DD}(S'/S).
\]

We say \(g\) is a *descent morphism* for finite étale covers if this functor is fully faithful, and an *effective descent morphism* if it is an equivalence. A descent datum in the essential image is called *effective*.

## 2. Universally submersive morphisms

A morphism is *submersive* if it is surjective and its target carries the quotient topology, and *universally submersive* if every base change of it is submersive.

**Lemma 2.1.** A proper surjective morphism is universally submersive.

**Proof.** Base changes of proper surjective morphisms are proper and surjective ([Stacks, Tags 01W4 and 01S1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-proper)). A proper morphism is closed, and a closed continuous surjection is a quotient map: a set whose inverse image is closed is the image of that inverse image, hence closed. \(\square\)

**Proposition 2.2.** Let \(g:S'\to S\) be universally submersive, and let \(X,Y\) be finite étale over \(S\), with pull-backs \(X',Y'\) to \(S'\) and \(X'',Y''\) to \(S''\). Then

\[
\operatorname{Hom}_S(X,Y)\longrightarrow\operatorname{Hom}_{S'}(X',Y')\rightrightarrows\operatorname{Hom}_{S''}(X'',Y'')
\]

is an equalizer. In particular \(g\) is a descent morphism for finite étale covers.

**Proof.** As in [Connectedness and full faithfulness, Corollary 3.1](connectedness-and-full-faithfulness.md#3-full-faithfulness), \(S\)-morphisms \(X\to Y\) correspond to their graphs, the open and closed subschemes \(\Gamma\) of \(Z=X\times_SY\) for which the first projection \(\Gamma\to X\) is an isomorphism; the same holds over \(S'\) and \(S''\), with \(Z'=Z\times_SS'\) and \(Z''=Z\times_SS''=Z'\times_ZZ'\). The map \(Z'\to Z\) is surjective and submersive, being a base change of \(g\).

Let \(f':X'\to Y'\) have graph \(\Gamma'\subset Z'\), and assume its two pull-backs to \(S''\) agree. The two inverse images of \(\Gamma'\) in \(Z''\) are the graphs of these pull-backs, so they are equal. Then \(\Gamma'\) is saturated for \(Z'\to Z\): if \(z'_1,z'_2\in Z'\) have the same image in \(Z\), there is a point of \(Z''=Z'\times_ZZ'\) over \((z'_1,z'_2)\) ([Stacks, Tag 01JT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-points-fibre-product)), and it lies in the first inverse image of \(\Gamma'\) if and only if it lies in the second. So \(\Gamma'\) is the inverse image of its image \(T\subset Z\). The inverse images of \(T\) and of \(Z\setminus T\) are open, so \(T\) is open and closed, because \(Z'\to Z\) is submersive. Let \(\Gamma\) be the open subscheme of \(Z\) on \(T\); then \(\Gamma\times_SS'=\Gamma'\). The morphism \(\Gamma\to X\) is finite étale, and its degree at a point of \(X\) equals the degree of \(\Gamma'\to X'\) at any point above it. Since \(X'\to X\) is surjective, \(\Gamma\to X\) has degree \(1\) everywhere, so it is an isomorphism, and \(\Gamma\) is the graph of a morphism \(f\) with \(g^*f=f'\). Uniqueness holds because \(\Gamma\) is determined by its inverse image in \(Z'\), the map \(Z'\to Z\) being surjective. \(\square\)

**Corollary 2.3 (effectivity is Zariski local).** Let \(g\) be universally submersive and \(S=\bigcup_iS_i\) an open cover. A descent datum relative to \(g\) is effective if and only if its restriction to each \(S_i\), relative to \(g^{-1}(S_i)\to S_i\), is effective.

**Proof.** Let \(Y_i\) over \(S_i\) represent the restrictions. By Proposition 2.2 for the universally submersive morphisms over \(S_i\cap S_j\) and \(S_i\cap S_j\cap S_k\), the identifications of the pull-backs of \(Y_i\) and \(Y_j\) with the given cover over \(g^{-1}(S_i\cap S_j)\) come from unique isomorphisms \(Y_i|_{S_i\cap S_j}\cong Y_j|_{S_i\cap S_j}\), which satisfy the cocycle condition. The \(Y_i\) glue. \(\square\)

## 3. Reduction to a henselian base

**Lemma 3.1 (spreading out from a local ring).** Let \(S\) be noetherian, \(g:S'\to S\) proper surjective, \((Y',\varphi)\) a descent datum, and \(s\in S\). If the descent datum becomes effective after base change to \(\operatorname{Spec}\mathcal O_{S,s}\), then it is effective over an open neighbourhood of \(s\).

**Proof.** The local ring \(\mathcal O_{S,s}\) is the filtered colimit of the rings of the affine open neighbourhoods \(U\) of \(s\), and all schemes involved are of finite presentation over \(S\), since \(S\) is noetherian. A finite étale scheme over \(\operatorname{Spec}\mathcal O_{S,s}\) comes from a finite étale scheme over some \(U\) ([Stacks, Tags 01ZO and 07RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-etale)). An isomorphism between schemes of finite presentation over the base change comes from an isomorphism over some smaller \(U\), and two morphisms that agree over \(\operatorname{Spec}\mathcal O_{S,s}\) agree over some \(U\) ([Stacks, Tags 01ZM and 081E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-isomorphism)). Apply this to the descended cover, to the isomorphism of its pull-back with \(Y'\), and to the equality expressing compatibility with \(\varphi\). \(\square\)

**Lemma 3.2 (faithfully flat base change).** Let \(g:S'\to S\) be universally submersive, \(S_1\to S\) faithfully flat and quasi-compact, and \(g_1:S'_1=S'\times_SS_1\to S_1\) the base change. If the pull-back to \(S'_1\) of a descent datum \((Y',\varphi)\) relative to \(g\) is effective relative to \(g_1\), then \((Y',\varphi)\) is effective.

**Proof.** Let \(Y_1\) be finite étale over \(S_1\), with an isomorphism \(\psi_1:g_1^*Y_1\to Y'_1\) compatible with the descent data, where \(Y'_1\) is the pull-back of \(Y'\). On \(S_2=S_1\times_SS_1\), with projections \(q_1,q_2\), the covers \(q_1^*Y_1\) and \(q_2^*Y_1\) both pull back to \(S'\times_SS_2\) as covers identified, through \(\psi_1\), with the pull-back of \(Y'\). These identifications are compatible with the descent data relative to the universally submersive morphism \(S'\times_SS_2\to S_2\), because \(\varphi\) itself is pulled back. By Proposition 2.2 there is a unique isomorphism \(\chi:q_1^*Y_1\to q_2^*Y_1\) inducing them, and by uniqueness \(\chi\) satisfies the cocycle condition over \(S_1\times_SS_1\times_SS_1\). Affine schemes descend along faithfully flat quasi-compact morphisms ([Stacks, Tag 0245](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-affine)), so \((Y_1,\chi)\) comes from a scheme \(Y\) affine over \(S\), which is finite and étale over \(S\) because these properties descend ([Stacks, Tags 02LA and 02VN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-descending-property-etale)). The isomorphism \(\psi_1\) between the pull-backs of \(g^*Y\) and of \(Y'\) to \(S'_1\) is compatible with the descent data relative to the faithfully flat quasi-compact \(S'_1\to S'\), so it descends to an isomorphism \(g^*Y\to Y'\) ([Stacks, Tag 023Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/descent.html#descent-lemma-fpqc-universal-effective-epimorphisms)). Its compatibility with \(\varphi\) is an equality of two morphisms, which holds after the faithfully flat base change, hence holds. \(\square\)

**Lemma 3.3 (henselian local base).** Let \(S=\operatorname{Spec}A\) with \(A\) a henselian local ring with residue field \(\kappa\), and \(g:S'\to S\) proper surjective. Then every descent datum for finite étale covers relative to \(g\) is effective.

**Proof.** For a scheme \(T\) proper over \(S\), with closed fibre \(T_0=T\times_S\operatorname{Spec}\kappa\), restriction is an equivalence \(\operatorname{F\acute Et}(T)\to\operatorname{F\acute Et}(T_0)\) ([Stacks, Tag 0A48](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-finite-etale-on-proper-over-henselian)), compatible with pull-back along \(S\)-morphisms. This applies to \(T=S,S',S'',S'''\). So descent data relative to \(g\) correspond to descent data relative to \(g_0:S'_0\to\operatorname{Spec}\kappa\), compatibly with the functors from \(\operatorname{F\acute Et}(S)\cong\operatorname{F\acute Et}(\kappa)\). The morphism \(g_0\) is surjective and quasi-compact, and flat because every module over a field is flat; so it is faithfully flat and quasi-compact, and descent data relative to it are effective by Tags 0245, 02LA and 02VN, as in the proof of Lemma 3.2. \(\square\)

**Theorem 3.4.** Let \(S\) be a noetherian scheme and \(g:S'\to S\) a proper surjective morphism. Then \(g\) is an effective descent morphism for finite étale covers: \(\operatorname{F\acute Et}(S)\to\operatorname{DD}(S'/S)\) is an equivalence.

**Proof.** The morphism \(g\) is universally submersive (Lemma 2.1), so the functor is fully faithful (Proposition 2.2). Let \((Y',\varphi)\) be a descent datum and \(s\in S\). The henselization \(A\) of \(\mathcal O_{S,s}\) is a henselian local ring, faithfully flat over \(\mathcal O_{S,s}\) ([Stacks, Tag 0AGU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-flat)). The base change of \(g\) to \(\operatorname{Spec}A\) is proper and surjective, so by Lemma 3.3 the pulled-back descent datum is effective there. By Lemma 3.2 it is effective over \(\operatorname{Spec}\mathcal O_{S,s}\), by Lemma 3.1 over an open neighbourhood of \(s\), and by Corollary 2.3 over \(S\). \(\square\)

## 4. Covering spaces

**Proposition 4.1.** Let \(p:M'\to M\) be a proper surjective continuous map of locally compact Hausdorff spaces, and \(M''=M'\times_MM'\) with projections \(p_1,p_2\). Let \(E_1,E_2\) be finite coverings of \(M\), and \(\alpha':p^*E_1\to p^*E_2\) an isomorphism over \(M'\) with \(p_1^*\alpha'=p_2^*\alpha'\) under the canonical identifications over \(M''\). Then \(\alpha'=p^*\alpha\) for a unique isomorphism \(\alpha:E_1\to E_2\) over \(M\).

**Proof.** The projection \(\mathrm{pr}:p^*E_1=M'\times_ME_1\to E_1\) is surjective, and it is proper, being a base change of a proper map of locally compact Hausdorff spaces. So it is closed, hence a quotient map. For \(e\in E_1\) over \(x\in M\), choose \(m'\in p^{-1}(x)\) and put \(\alpha(e)=\mathrm{pr}\bigl(\alpha'(m',e)\bigr)\). For a second choice \(m''\), the point \((m',m'')\in M''\) and the equality \(p_1^*\alpha'=p_2^*\alpha'\) show that the value is the same. Then \(\alpha\circ\mathrm{pr}=\mathrm{pr}\circ\alpha'\) is continuous, so \(\alpha\) is continuous. The same construction applied to \(\alpha'^{-1}\) gives the inverse. Uniqueness holds because \(\mathrm{pr}\) is surjective. \(\square\)

## 5. Examples

**Example 5.1 (the nodal cubic).** Let \(X\) be the nodal cubic of Example 5.3 of the first lesson and \(g:\mathbf A^1\to X\) its normalization, a finite, hence proper, surjective morphism identifying \(t=1\) with \(t=-1\). The scheme \(\mathbf A^1\times_X\mathbf A^1\) is the diagonal copy of \(\mathbf A^1\) together with the two points \((1,-1)\) and \((-1,1)\). A descent datum on the trivial double cover \(\mathbf A^1\times\{a,b\}\) is therefore a permutation \(\sigma\) of \(\{a,b\}\) attached to the point \((1,-1)\), the identity on the diagonal, and \(\sigma^{-1}\) at \((-1,1)\); the cocycle condition holds automatically. For \(\sigma=\mathrm{id}\) the descended cover is trivial, and for the transposition it is the connected double cover of that example. Theorem 3.4 says that these are all the double covers of \(X\) that become trivial on \(\mathbf A^1\).

**Example 5.2 (why properness matters).** The morphism \(g:(\mathbf A^1\setminus\{0\})\sqcup\{0\}\to\mathbf A^1\) given by the inclusions of the punctured line and of the origin is bijective and quasi-finite but not proper, and it is not submersive: the image of the open set \(\mathbf A^1\setminus\{0\}\), whose inverse image is open and closed, is not closed in \(\mathbf A^1\). Descent fails: the nontrivial double cover \(w^2=z\) of \(\mathbf A^1\setminus\{0\}\) together with the trivial cover of the origin carries a descent datum (here \(S''=S'\)), but it does not come from a finite étale cover of \(\mathbf A^1\).

## 6. Exercises

**Exercise 6.1.** In Example 5.1, verify the description of \(\mathbf A^1\times_X\mathbf A^1\) on complex points.

*Solution.* A pair \((t,u)\) lies in the fibre product when \(g(t)=g(u)\), that is, \(t=u\), or \(\{t,u\}=\{1,-1\}\). So the complex points are the diagonal and the two points \((1,-1)\), \((-1,1)\).

**Exercise 6.2.** Show that a finite étale \(Y\to S\) whose pull-back along a universally submersive \(g\) is trivial of degree \(d\), with the canonical descent datum equal to the trivial one, is itself trivial.

*Solution.* The trivial cover \(S\times\{1,\ldots,d\}\) pulls back to the same descent datum, so by full faithfulness (Proposition 2.2) the identification of the pull-backs comes from an isomorphism \(Y\cong S\times\{1,\ldots,d\}\).

**Exercise 6.3.** Where in the proof of Theorem 3.4 is it used that the descent datum lives on finite étale covers, rather than on arbitrary étale ones?

*Solution.* In Lemma 3.3: the equivalence with the closed fibre holds for finite étale covers of proper schemes over a henselian local ring, and fails in general for étale ones, for example for open subschemes.

## References

- [SGA 1] A. Grothendieck et al., *Revêtements étales et groupe fondamental (SGA 1)*, Exposé IX, Proposition 3.2, Corollary 3.3, Corollaries 4.2–4.6 and Theorem 4.12; free re-edition arXiv:math/0206203. This lesson reduces to a henselian local ring rather than a complete one, using the treatment in the AI Integrated Stacks Project. <https://arxiv.org/abs/math/0206203>
