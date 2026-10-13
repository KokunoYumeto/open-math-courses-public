# Continuous outer actions of locally compact groups

*Written by GPT-6.1 Sol (OpenAI), Ultra. Original programme exposition: CC0-1.0 to the extent of rights held. Human-source notices retain their separate terms.*

A displaced vector in the regular representation, copied into infinitely many orthogonal summands, gives a continuous outer action on the tracial CAR factor. The copies prevent a Hilbert–Schmidt perturbation of the identity; the complete complex CAR criterion turns that obstruction into outerness.

Here \(G\) is a locally compact Hausdorff group with a countable base. The full CO0–5 inputs supply compact cutoffs, the exact complete Haar-measure route, the entire regular Hilbert space, the completed tracial CAR algebra, full normal extension and point-predual continuity, the whole Hilbert–Schmidt innerness proof and topology transport. The target is every separable AFD factor of type \(\mathrm{II}_1\). Neither amenability nor connectedness nor unimodularity is assumed.

<a id="1-a-faithful-continuous-regular-representation"></a>

## Start with a genuinely displaced vector

CO1's complete compact-content/Borel construction gives left Haar measure \(m\), finite on compact sets and positive on nonempty open sets. CO0's compact-neighborhood proof and the countable base give a countable relatively compact open cover, hence sigma-finiteness. Set \(H_0=L^2(G,m)\), with pairing \(\langle f,h\rangle=\int\overline f h\,dm\), and define
\[
(\lambda(g)f)(t)=f(g^{-1}t).
\tag{1}
\]
Left invariance proves unitarity on indicators, simple functions and their whole Hilbert completion. Substitution gives the representation law.

**Lemma 1.1.** The Hilbert space \(H_0\) is separable, and \(\lambda\) is strongly continuous and faithful.

**Proof.** CO2 gives the complete \(L^2\) measure and convergence arguments. On each finite-measure cover member, approximate a Borel set from within by a compact set and from outside by an open set. A finite union of countable-base members fits between them and approximates its indicator in \(L^2\). Rational complex combinations of these countably many indicators are dense, by simple approximation and truncation to the cover. Thus \(H_0\) is separable. Completion of the measure introduces no new \(L^2\) classes: its functions have the Borel representatives proved in CO1.

CO0's compactly supported cutoff gives \(C_c(G)\)-density by the indicator estimate in CO2.1. For \(f\in C_c(G)\), and \(g\) near \(e\) in a compact neighborhood \(C\), all translated supports lie in the compact set \(C\operatorname{supp}f\). Joint continuity and a finite product-neighborhood cover give uniform convergence of \(f(g^{-1}t)-f(t)\) to zero on that set. Its finite measure gives \(L^2\) convergence. The common unitary bound and \(C_c\)-density prove convergence on every vector, for parameter nets. The group law gives continuity at every parameter.

For \(g\ne e\), choose disjoint neighborhoods of \(e\) and \(g\), and then a nonempty relatively compact open \(V\) with
\[
V\cap gV=\varnothing.
\tag{2}
\]
Continuity of left multiplication and the compact-neighborhood shrinking proof permit this choice. Haar positivity and compact finiteness give \(0<m(V)<\infty\). Therefore
\[
\xi=m(V)^{-1/2}1_V,\qquad
\|\lambda(g)\xi-\xi\|^2=2.
\tag{3}
\]
The two supports are disjoint and their measures agree. This proves faithfulness. All claims use the full constructed measure and Hilbert space. \(\square\)

**Exercise 1.** Verify the law for (1) and the absence of a modular multiplier.

*Solution.* At \(f\in L^2\),
\[
(\lambda(g)\lambda(h)f)(t)
=f(h^{-1}g^{-1}t)=f((gh)^{-1}t).
\]
The formulas hold on Borel representatives and then on their classes. Left translation preserves the chosen left Haar measure, so its change of variables preserves the whole \(L^2\) norm. This uses left translation, not right translation against left Haar measure; the latter would need the modular correction.

**Exercise 5.** For \(G=\mathbb R\), find an explicit displaced unit vector for each nonzero \(s\).

*Solution.* Lebesgue measure is left Haar measure by its complete interval outer-measure construction in the linked tools lesson. Take \(V=(0,r)\) with \(0<r<|s|\). Its translate \(s+V\) is disjoint, and \(\xi=r^{-1/2}1_V\) has norm one. For \((\lambda(s)f)(t)=f(t-s)\), both squared norms are one and the mixed inner product is zero, giving distance \(\sqrt2\). The infinitely repeated representation below therefore yields a continuous real action with every nonzero time outer.

<a id="2-repetition-removes-hilbertschmidt-perturbations"></a>
<a id="2-repetition-removes-hilbert-schmidt-perturbations"></a>
<a id="4-why-countably-many-copies-matter"></a>

## Repeat the displacement while retaining continuity

Let
\[
K=H_0\otimes\ell^2(\mathbb N)=\bigoplus_{n\ge1}H_0,\qquad
U(g)=\lambda(g)\otimes1.
\tag{4}
\]
The equality is the complete Hilbert tensor/direct-sum identification on elementary coordinates. It is separable, and it is infinite dimensional even when \(G\) is finite or trivial: \(H_0\ne0\), and a fixed nonzero vector in its separate summands gives infinitely many orthogonal vectors.

**Lemma 2.1.** For every \(g\ne e\),
\[
U(g)-1\notin\mathcal L^2(K).
\tag{5}
\]
In fact \(U(g)-1\) is not compact.

**Proof.** At \(g\ne e\), choose \(\xi\) as in (3). The vectors \(\eta_n=\xi\otimes e_n\) are orthonormal and
\[
\|(U(g)-1)\eta_n\|^2=2.
\tag{6}
\]
Extend them to an orthonormal basis. Basis independence and the whole square-sum Hilbert–Schmidt construction in CO4 show that these infinitely many contributions already make the sum infinite. Their images lie in distinct summands, are orthogonal and have norm \(\sqrt2\). They have no convergent subsequence, proving noncompactness. \(\square\)

The representation law holds on the complete direct sum. Strong continuity follows by retaining a finite prefix of any vector and estimating the remaining tail by the common unitary bound, as the next full solution shows. More generally any faithful strongly continuous representation on a nonzero separable space has a vector with some nonzero displacement \(c\); repeating it gives infinitely many squared contributions \(c^2\).

**Exercise 4.** Prove whole strong continuity of (4), with an explicit tail estimate.

*Solution.* Write \(\eta=(\eta_n)\). Then
\[
\|(U(g)-U(g_0))\eta\|^2
=\sum_n\|(\lambda(g)-\lambda(g_0))\eta_n\|^2.
\]
Given \(\varepsilon>0\), choose \(N\) with \(4\sum_{n>N}\|\eta_n\|^2<\varepsilon^2/2\). Strong continuity on the finitely many prefix vectors makes their sum less than \(\varepsilon^2/2\) in one parameter neighborhood. Each tail difference has norm at most \(2\|\eta_n\|\), so the whole squared norm is less than \(\varepsilon^2\). This works for every vector and for nets.

**Exercise 3.** Prove that a nonzero bounded \(T\) has a non-Hilbert–Schmidt, noncompact repetition \(T\otimes1_{\ell^2}\).

*Solution.* Choose a unit \(\xi\) with \(\|T\xi\|=c>0\). The orthonormal \(\xi\otimes e_n\)'s have images in different summands, all of norm \(c\). An orthonormal basis containing them contributes \(\sum_n c^2=\infty\) to the Hilbert–Schmidt sum. The mutually orthogonal images stay at distance \(\sqrt2c\) from each other, so no subsequence converges. This also proves noncompactness and applies in particular to \(T=\lambda(g)-1\).

**Exercise 2.** Compute the Hilbert–Schmidt square norm for a finite group's nonidentity regular permutation, and on \(N\) copies.

*Solution.* Use counting measure and its orthonormal \(\delta_h\)'s. If \(g\ne e\), left multiplication fixes none of them: \(gh=h\) would imply \(g=e\). Thus \(\lambda(g)\delta_h\) and \(\delta_h\) are distinct orthonormal vectors, with squared difference two. The whole finite basis gives
\[
\|\lambda(g)-1\|_{\mathrm{HS}}^2=2|G|.
\]
On \(N\) summands it is \(2N|G|\). Infinitely many summands give divergence, while one finite summand remains a Hilbert–Schmidt perturbation.

## The tracial CAR action on the entire factor

CO3 builds the norm-complete CAR algebra on the actual \(K\), with conjugate-linear annihilation \(a(f)\) and \(\|a(f)\|=\|f\|\). Its trace representation is the complete tracial matrix product \(R_K\), a separable AFD \(\mathrm{II}_1\) factor. Its finite CAR algebras and arbitrary overlapping mode maps are proved explicitly. Define
\[
\beta_g(a(f))=a(U(g)f).
\tag{7}
\]
CO3 extends this prescription to a trace-preserving automorphism of the whole norm algebra, then normally to the entire \(R_K\), with full normal inverse. Its vector-series argument proves point-predual norm continuity for every normal functional. CO4 proves the entire complex-linear factor criterion: \(\beta_g\) is inner exactly when \(U(g)-1\) is Hilbert–Schmidt, using the complete tracial product criterion, bounded logarithm, dyadic diagonal perturbation and normal group law.

<a id="3-the-outer-action"></a>

**Theorem 3.1.** The map
\[
\beta:G\longrightarrow\operatorname{Aut}(R_K)
\tag{8}
\]
is a continuous injective homomorphism, preserves the normalized trace, and satisfies
\[
\beta_g\text{ is inner}\quad\Longleftrightarrow\quad g=e.
\tag{9}
\]
For any separable AFD factor \(R_0\) of type \(\mathrm{II}_1\), transporting (8) along a normal isomorphism gives such an action on \(R_0\).

**Proof.** The whole CAR construction and normal extension just described give the trace-preserving normal automorphisms. Their generator law gives \(\beta_g\beta_h=\beta_{gh}\) on the norm algebra and then normally on all \(R_K\). Strong continuity of (4), composed with CO3.4's whole vector-pair-series estimate, proves point-predual norm continuity.

By CO4's full factor criterion and Lemma 2.1, every \(g\ne e\) gives an outer automorphism; \(g=e\) gives the identity. If \(\beta_g=\beta_h\), the homomorphism law makes \(\beta_{h^{-1}g}\) the identity and hence inner, so \(g=h\). This proves injectivity.

AF5's complete separable AFD \(\mathrm{II}_1\) uniqueness proof supplies a normal isomorphism \(\theta:R_K\to R_0\), with whole normal inverse. Put
\[
\gamma_g=\theta\beta_g\theta^{-1}.
\tag{10}
\]
CO5's predual isometries prove both directions of the topology homeomorphism. The same normal identification transports the normalized trace, by the full canonical trace uniqueness proof. An implementing unitary is transported or pulled back by \(\theta\), so innerness and outerness are preserved. Thus every stated conclusion holds on the whole \(R_0\). \(\square\)

**Exercise 7.** Verify the full point-predual topology and outerness transport in (10).

*Solution.* For \(\rho\in(R_0)_*\) and \(\beta,\beta'\in\operatorname{Aut}(R_K)\),
\[
\|\rho\theta\beta\theta^{-1}-\rho\theta\beta'\theta^{-1}\|
=\|(\rho\theta)\beta-(\rho\theta)\beta'\|.
\]
Precomposition by the normally onto isomorphism \(\theta^{-1}\) is an isometry on the whole unit-ball functional norm. These identities for every \(\rho\) give continuity; those for \(\theta^{-1}\) give the inverse continuity. If \(v\in R_0\) implements the transported map, then the unitary \(\theta^{-1}(v)\in R_K\) implements the original map. Pushing an original implementer forward proves the converse. Thus outerness is preserved in both directions.

**Exercise 6.** Does a faithful one-particle representation by itself guarantee an outer CAR action?

*Solution.* A nontrivial finite group has its faithful finite-dimensional regular representation. Its differences from the identity have finite rank and are Hilbert–Schmidt. After adjoining an infinite-dimensional trivial summand, the differences still have finite rank; the full complex-linear criterion makes every resulting CAR automorphism inner, even though the representation is faithful and its Hilbert space is now infinite dimensional. Repeating the nontrivial representation creates infinitely many displaced modes. Merely adding unused modes does not do so.

**Exercise 8.** Treat the trivial group and the resulting factor type.

*Solution.* For \(G=\{e\}\), \(H_0\) is one dimensional. Its countable repetition \(K=H_0\otimes\ell^2\) is separable infinite dimensional, and CO3's entire tracial product proof makes \(R_K\) a factor of type \(\mathrm{II}_1\). The only element acts as the identity. The group map is injective and its nonidentity-outerness statement is vacuous. Without repetition the one-mode CAR algebra would instead be \(M_2\). This endpoint is part of the same construction.

<a id="5-exercises-with-complete-solutions"></a>
<a id="references"></a>

## Countability and the exact free comparisons

The second-countable hypothesis is retained throughout. Countable density by itself does not supply it. For instance, if a compact group acts through a continuous injective map into the Hausdorff Polish \(\operatorname{Aut}(R_K)\), the map is a homeomorphism onto its image: compact closed sets have compact, hence closed, images. Its domain is therefore metrizable, as a subspace of that metric group. The complete automorphism-topology proof is in the central-sequence foundations. A compact nonmetrizable group cannot be covered by silently replacing second countability with separability.

Robert J. Blattner, [*Automorphic group representations*](https://msp.org/pjm/1958/8-4/pjm-v8-n4-p03-s.pdf), Section 6, printed pp.673–675, Definition 3 and the full corollary, compares the repeated regular representation and explicitly assumes second countability. It uses real Clifford generators and point-weak continuity. CO3–4 supply the complete complex tracial CAR argument and whole point-predual norm continuity here.

A. L. Carey, [*Inner automorphisms of hyperfinite factors and Bogoliubov transformations*](https://numdam.org/item/AIHPA_1984__40_2_141_0.pdf), Proposition 3.1 and the preceding paragraph, printed p.148, compares repeated regular representations with a displayed type III parameter \(0<\lambda<1/2\). That proposition is not used to infer the current tracial factor type. CO3 constructs the actual half-trace matrix factor; CO4 proves its complex-linear criterion and explains the excluded negative real-Clifford branch.

D. H. Fremlin's author-supplied [2013 §441C(b–f), §441E](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt441.tex) is the compact-cover Haar method comparison. The linked programme content proof supplies every Borel-conversion step, while CO0–2 supply compact cutoffs, whole \(L^2\) approximation and regular-representation continuity. Human-source terms are retained; free access is not treated as a grant to relabel human expression.
