# Clearing denominators in a finite diagram

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The diagram \(\mathcal V\) of [A Verdier quotient and an odd double](a-verdier-quotient-and-an-odd-double.md) lives in the Verdier quotient \(Q=K/\mathcal S\), whose morphisms are fractions. To build a tensor functor from it, its objects and arrows must come from honest complexes and chain maps. This lesson clears the denominators: every \(B\)-diagram in \(Q\) is isomorphic to the image of a \(B\)-diagram in the homotopy category \(K\) (Lemma 2.1). Choosing chain maps and homotopies then gives a finite list of chain data (Proposition 3.1) that work for every module \(Y\) at once, because the lifting is done once, before any \(Y\) is chosen. The construction follows [OpenAI-FD, Section 3].

Notation is as in the previous lesson: \(K\) is the homotopy category of bounded complexes of finitely generated projective right \(B\)-modules, \(\Sigma\) the morphisms whose cone lies in \(\mathcal S\), and \(q\colon K\to Q\) the localization.

## 1. Fractions

By Theorem 2.1 of [A Verdier quotient and an odd double](a-verdier-quotient-and-an-odd-double.md), the objects of \(Q\) are those of \(K\); every morphism \(X\to Y\) in \(Q\) has the form \(q(f)q(u)^{-1}\) for some \(u\colon X'\to X\) in \(\Sigma\) and \(f\colon X'\to Y\) in \(K\); and \(q(g)=0\) for \(g\colon X\to Y\) exactly when \(gv=0\) for some \(v\colon X'\to X\) in \(\Sigma\). The functor \(q\) is additive, so it preserves finite direct sums.

**Lemma 1.1** (one denominator for finitely many maps). (a) For finitely many morphisms \(\varphi_b\colon X\to Y_b\) in \(Q\) there are one \(u\colon X'\to X\) in \(\Sigma\) and morphisms \(f_b\colon X'\to Y_b\) in \(K\) with \(\varphi_b=q(f_b)q(u)^{-1}\) for all \(b\). (b) For finitely many morphisms \(g_\rho\colon X\to Y_\rho\) in \(K\) with \(q(g_\rho)=0\) there is one \(v\colon X'\to X\) in \(\Sigma\) with \(g_\rho v=0\) for all \(\rho\).

**Proof.** (a) Write the family as one morphism \(X\to\bigoplus_bY_b\) in \(Q\), represent it as \(q(f)q(u)^{-1}\), and let \(f_b\) be the components of \(f\). (b) Apply the vanishing criterion to the morphism \((g_\rho)_\rho\colon X\to\bigoplus_\rho Y_\rho\). \(\square\)

## 2. Lifting a diagram

Recall that a \(B\)-diagram in a \(k\)-linear additive category consists of objects \(W_0,W_1,W_2\) and morphisms \(t_a\colon W_i\to W_j\) for the arrows \(a\colon i\to j\), with \(\sum_{a,b}\rho_{ba}t_bt_a=0\) for every \(\rho\in\mathcal R\).

**Lemma 2.1** (diagram lifting). Every \(B\)-diagram \((W_i,t_a)\) in \(Q\) is isomorphic to the image under \(q\) of a \(B\)-diagram in \(K\).

**Proof.** *Arrows into vertex \(2\).* Apply Lemma 1.1(a) to the morphisms \(t_b\colon W_1\to W_2\), \(b\in\mathcal A_{12}\): there are \(u_1\colon D_1\to W_1\) in \(\Sigma\) and \(f_b\colon D_1\to W_2\) in \(K\) with \(t_b=q(f_b)q(u_1)^{-1}\). Put \(D_2=W_2\), \(\phi_2=\mathrm{id}\) and \(\phi_1=q(u_1)\colon D_1\to W_1\), an isomorphism in \(Q\). Then \(\phi_2q(f_b)=t_b\phi_1\) for every \(b\in\mathcal A_{12}\).

*Arrows into vertex \(1\).* Apply Lemma 1.1(a) to the morphisms \(\phi_1^{-1}t_a\colon W_0\to D_1\), \(a\in\mathcal A_{01}\): there are \(u_0\colon D'_0\to W_0\) in \(\Sigma\) and \(f'_a\colon D'_0\to D_1\) with \(\phi_1^{-1}t_a=q(f'_a)q(u_0)^{-1}\). Put \(\phi'_0=q(u_0)\). Then the squares (2.1)
\[
\phi_jq(f)=t_a\phi_i\qquad(a\colon i\to j)
\]
commute for every arrow, with \(f=f'_a\) for \(a\in\mathcal A_{01}\), source \(D'_0\) and \(\phi_0=\phi'_0\).

*Relations.* For \(\rho\in\mathcal R\) let \(g_\rho=\sum_{a,b}\rho_{ba}f_bf'_a\colon D'_0\to D_2\) in \(K\). By (2.1) and the relations of \((W_i,t_a)\),
\[
\phi_2q(g_\rho)=\sum_{a,b}\rho_{ba}t_bt_a\phi'_0=0,
\]
so \(q(g_\rho)=0\), since \(\phi_2\) is an isomorphism. By Lemma 1.1(b) there is \(v\colon D_0\to D'_0\) in \(\Sigma\) with \(g_\rho v=0\) for every \(\rho\). Put \(f_a=f'_av\) for \(a\in\mathcal A_{01}\) and \(\phi_0=\phi'_0q(v)\), again an isomorphism. The squares (2.1) still commute, and
\[
\sum_{a,b}\rho_{ba}f_bf_a=g_\rho v=0\qquad\text{in }K .
\]
Every relation of \(B\) is a combination of paths from vertex \(0\) to vertex \(2\), and no further paths can be composed with them, so these are all the conditions: \((D_i,f_a)\) is a \(B\)-diagram in \(K\), and \((\phi_0,\phi_1,\phi_2)\) is an isomorphism from its image to \((W_i,t_a)\). \(\square\)

The lifting is done in two rounds, first for the arrows into vertex \(2\) and then for those into vertex \(1\); the denominator of the second round is placed at vertex \(0\), where no arrow ends, so it does not disturb the first round.

## 3. The chain data

**Proposition 3.1** (fixed lifted diagram). There are bounded complexes \(D_0,D_1,D_2\) of finitely generated projective right \(B\)-modules, chain maps \(f_a\colon D_i\to D_j\) for the arrows \(a\colon i\to j\), and right \(B\)-linear maps \(h_\rho\colon D_0\to D_2\) of degree \(-1\) for \(\rho\in\mathcal R\), such that the equations (3.1)
\[
\begin{gathered}
d_{D_2}h_\rho+h_\rho d_{D_0}=f_\rho,\\
f_\rho=\sum_{a,b}\rho_{ba}f_bf_a,
\end{gathered}
\]
hold, with the following property. For every finite-dimensional left \(R\)-module \(Y\), the diagram in \(\mathrm D^b(k)\) with objects \(D_i\otimes_BM(Y)\) and arrows \(f_a\otimes_B\mathrm{id}_{M(Y)}\) is isomorphic to the diagram with \(eY\oplus(eY)[3]\) at every vertex, identities for \(s\) and \(s'\), and the action of \(\alpha(x_h)\) on both summands for \(a_h\) and \(a'_h\). All complexes, maps and homotopies are chosen before \(Y\).

**Proof.** Apply Lemma 2.1 to the diagram \(\mathcal V\) of Lemma 5.2 of [A Verdier quotient and an odd double](a-verdier-quotient-and-an-odd-double.md). It gives a \(B\)-diagram in \(K\) and an isomorphism \(\phi\) from its image to \(\mathcal V\). Its objects are bounded complexes \(D_i\) of finitely generated projective right modules, and its morphisms are homotopy classes; choose chain maps \(f_a\) representing them. Each relation holds in \(K\), so \(f_\rho\) is null-homotopic; choose a homotopy \(h_\rho\) with (3.1).

Let \(Y\) be given. The functor \(\overline{\operatorname{ev}}_Y\) of Proposition 3.2 of [A Verdier quotient and an odd double](a-verdier-quotient-and-an-odd-double.md) satisfies \(\overline{\operatorname{ev}}_Y\circ q=\operatorname{ev}_Y\), which sends \(D_i\) to \(D_i\otimes_BM(Y)\) and the class of \(f_a\) to the class of \(f_a\otimes\mathrm{id}\). Applying the extension of \(\overline{\operatorname{ev}}_Y\) to \(\operatorname{Kar}(Q)\) to the isomorphism \(\phi\) gives an isomorphism of diagrams from \((D_i\otimes_BM(Y),f_a\otimes\mathrm{id})\) to the evaluation of \(\mathcal V\), which is the asserted diagram by Proposition 5.4 of that lesson. \(\square\)

The construction used only the homomorphism \(\theta\) and the evaluation functors; it never identifies \(Q\) with a derived category of \(R\). The maps \(f_a\) satisfy the relations of \(B\) only up to the homotopies \(h_\rho\). The next lesson packs the complexes, maps and homotopies into one complex of bimodules.

## 4. Exercises

**Exercise 4.1** (easy). Show that if \(u\in\Sigma\) and \(q(f)q(u)^{-1}=0\), then \(fv=0\) for some \(v\in\Sigma\).

**Exercise 4.2** (easy). In Lemma 2.1, why can the lifting not start at vertex \(0\), with the arrows out of vertex \(0\)?

**Exercise 4.3** (medium). Suppose the diagram \((W_i,t_a)\) in Lemma 2.1 already has all \(W_i\) and \(t_a\) in the image of \(K\), and the relations hold in \(K\). Show that the proof can be run with all denominators equal to identities.

**Exercise 4.4** (medium). Show that the homotopies \(h_\rho\) in Proposition 3.1 can be changed by adding \(d_{D_2}k_\rho-k_\rho d_{D_0}\) for arbitrary maps \(k_\rho\) of degree \(-2\), and that (3.1) still holds.

## 5. Solutions

**4.1.** Since \(q(u)\) is invertible, \(q(f)=0\), and the vanishing criterion gives \(v\in\Sigma\) with \(fv=0\).

**4.2.** A fraction \(q(f)q(u)^{-1}\) changes the source of a morphism, not its target. Lifting an arrow \(a\colon i\to j\) replaces the object at the source vertex \(i\) by the source of the denominator. If the arrows out of vertex \(0\) were lifted first, lifting the arrows out of vertex \(1\) would afterwards change the object at vertex \(1\), the target of the arrows already lifted, and they would have to be composed with an inverse fraction. Working from the last vertex backwards, each round changes only the object at a vertex whose outgoing arrows have not been lifted yet.

**4.3.** Take \(D_i=W_i\), \(u_1=\mathrm{id}\), \(u_0=\mathrm{id}\) and \(f_a\) the given morphisms; then \(g_\rho=0\) in \(K\), and \(v=\mathrm{id}\) works.

**4.4.** For a map \(k\) of degree \(-2\), \(d(dk-kd)+(dk-kd)d\) equals \(d^2k-dkd+dkd-kd^2=0\), since \(d^2=0\). So \(h_\rho+(dk_\rho-k_\rho d)\) satisfies the same equation (3.1).

## References

- [OpenAI-FD] OpenAI, *An algebra of infinite little finitistic dimension*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026
