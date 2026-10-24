# Suspension, shifts and unbounded modules over a simplicial ring

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

For a simplicial ring \(R\) of a topos with normalization \(A=NR\), this lesson proves five results.
- Normalization carries the suspension of simplicial modules to the shift of differential graded modules, through a natural isomorphism defined by a cone.
- The suspension is fully faithful on \(D_\bullet(R)\).
- The stable Ext groups of simplicial modules are the Ext groups of \(D(A)\).
- Formally inverting the suspension gives \(D^-(A)\), and every differential graded module is a telescope of finite shifts of normalizations.
- The derived category of complexes in the abelian category of simplicial modules is a different object: total normalization is not full on it.

**Prerequisites.** [*Normalization of modules over a simplicial ring*](normalization-of-modules-over-a-simplicial-ring.md) (Theorem 4.1, Corollary 4.2); [*Triangles and Ext groups of simplicial modules*](triangles-and-ext-groups-of-simplicial-modules.md) (Conventions, 1.1); [*Differential graded modules in a topos*](differential-graded-modules-in-a-topos.md) (Lemma 1.1, Proposition 1.2); AI-integrated Stacks project: homotopic maps and normalized complexes [[Tag 019S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-s-N)], maps out of bounded above complexes of projectives [[Tag 064B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-from-projective-complex)].

## Conventions

As in the lesson on normalization. For an \(R\)-module \(E\), put \(\gamma E=\gamma_{\mathbb Z}\otimes E\) and \(\sigma E=\sigma_{\mathbb Z}\otimes E\), degreewise, with \(R\) acting on \(E\). By 1.1 of the lesson on triangles, \(\mathsf c_E\colon0\to E\xrightarrow{i}\gamma E\xrightarrow{v}\sigma E\to0\) is exact. The contraction of \(\gamma_{\mathbb Z}\) is induced by a map of simplicial sets, so \(\gamma E\) is homotopy equivalent to \(0\) and \(N\gamma E\) is acyclic [Tag 019S].

For a left module \(M\) over \(A\), put
\[
M[r]^i=M^{i+r},\quad d_{M[r]}=(-1)^rd_M,
\]
with action \(a\cdot m=(-1)^{r|a|}am\); this is again a module.

For a map \(f\colon X\to Y\) of modules, the cone \(C(f)\) has \(C(f)^i=Y^i\oplus X^{i+1}\) and \(d(y,x)=(dy+f(x),-dx)\), with action \(a(y,x)=(ay,(-1)^{|a|}ax)\).

## 1. Suspension and shift

**Proposition 1.1.** For an \(R\)-module \(E\), let \(s\colon C(Ni)\to N\sigma E\) be \((y,x)\mapsto v(y)\) and \(q\colon C(Ni)\to NE[1]\) be \((y,x)\mapsto x\). Both are \(A\)-linear quasi-isomorphisms, natural in \(E\). So \(\theta_E=[q][s]^{-1}\colon N\sigma E\to NE[1]\) is an isomorphism of \(D(A)\), natural in \(E\). Moreover:
- \(\sigma\) preserves quasi-isomorphisms;
- \(\sigma\colon D_\bullet(R)\to D_\bullet(R)\) is fully faithful, and \(\theta(N\sigma a)\theta^{-1}=N(a)[1]\) for every morphism \(a\).

**Proof.** *The map \(s\).* It is a chain map since \(vi=0\), and it is onto. Its kernel \(\{(i x',x)\}\) is isomorphic to the cone of the identity of \(NE\), which is contractible by the homotopy \((y,x)\mapsto(0,y)\).

*The map \(q\).* It is a chain map since \(d_{NE[1]}=-d\), and it is \(A\)-linear by the action rules. Its kernel \(N\gamma E\) is acyclic.

*Consequences.* Naturality is clear. Then \(H^{k}(N\sigma f)\cong H^{k+1}(Nf)\) naturally, so \(\sigma\) preserves quasi-isomorphisms. Naturality of \(\theta\) extends to the localization. By Theorem 4.1 of the lesson on normalization, \(a\mapsto N(a)\) is bijective, and \(N(a)\mapsto N(a)[1]\) is bijective. Hence \(a\mapsto\sigma a\) is bijective on morphism sets. \(\square\)

Put \(\Theta_0=1\) and \(\Theta_{k+1,X}=\) \(\Theta_{k,X}[1]\circ\theta_{\sigma^kX}\colon\) \(N\sigma^{k+1}X\to\) \(NX[k+1]\). Naturality of \(\theta\) gives, for \(a\colon\sigma^nE\to\sigma^{n+p}F\),
\[
\begin{aligned}
&\Theta_{n+p+1}N(\sigma a)\Theta_{n+1}^{-1}\\
&\quad=(\Theta_{n+p}N(a)\Theta_n^{-1})[1].
\end{aligned}\tag{1.2}
\]

**Theorem 1.3 (stable Ext groups).** For \(p\in\mathbb Z\) put
\[
\begin{aligned}
&\operatorname{Ext}^p(E,F)=\\
&\varinjlim_{n\geq\max(0,-p)}
\operatorname{Hom}(\sigma^nE,\sigma^{n+p}F),
\end{aligned}
\]
the morphisms being those of \(D_\bullet(R)\) and the transition maps \(a\mapsto\sigma a\). The maps \(a\mapsto(\Theta_{n+p}N(a)\Theta_n^{-1})[-n]\) induce an isomorphism, natural in \(E\) and \(F\),
\[
\operatorname{Ext}^p(E,F)\cong\operatorname{Hom}_{D(A)}(NE,NF[p]).
\]
For commutative \(R\), these are the Ext groups of Definition 2.1 of the lesson on triangles.

**Proof.** Each stage map is bijective, by Theorem 4.1 of the lesson on normalization and because shifts are automorphisms. By (1.2), these maps commute with the transition maps. \(\square\)

**Proposition 1.4 (inverting the suspension).** Let \(\operatorname{SW}\) be the category whose objects are pairs \((E,n)\), with \(E\in D_\bullet(R)\) and \(n\geq0\), and whose morphisms are
\[
\begin{aligned}&\operatorname{Hom}((E,n),(F,m))=\\&\varinjlim_{k\geq n,m}\operatorname{Hom}(\sigma^{k-n}E,\sigma^{k-m}F),\end{aligned}
\]
with composition at a common \(k\). Then \((E,n)\mapsto NE[-n]\) is an equivalence from \(\operatorname{SW}\) onto the full subcategory \(D^-(A)\) of \(D(A)\) of objects with bounded above cohomology.

**Proof.** The transition maps are bijective (Proposition 1.1), so composition is well defined. The maps
\[
a\mapsto(\Theta_{k-m}N(a)\Theta_{k-n}^{-1})[-k]
\]
are bijections onto \(\operatorname{Hom}_{D(A)}(NE[-n],NF[-m])\). By (1.2) they are compatible with the transitions, and they are compatible with composition. Every \(NE[-n]\) has \(H^i=0\) for \(i>n\). Conversely, if \(H^iM=0\) for \(i>n\geq0\), then \(M[n]\cong NE\) for some \(E\) by Theorem 4.1 of the lesson on normalization, so \(M\cong NE[-n]\). \(\square\)

## 2. Telescopes

**Proposition 2.1.** Let \(M\) be a left \(A\)-module and \(M_n=\tau^{\leq n}M\) for \(n\geq0\), a submodule by Lemma 1.1 of the lesson on differential graded modules. Put \(B=\bigoplus_nM_n\), and let \(s\colon B\to B\) send the summand \(n\) to the summand \(n+1\) by inclusion. Then the map \(C(1-s)\to M\), \((y,x)\mapsto\sum_ny_n\), is an \(A\)-linear quasi-isomorphism. Each \(M_n\) is isomorphic in \(D(A)\) to \(NE_n[-n]\) for an \(R\)-module \(E_n\).

**Proof.** *The exact sequence.* In degree \(i\), \(M_n^i=M^i\) for \(n>i\). The sequence
\[
0\to B\xrightarrow{1-s}B\xrightarrow{\Sigma}M\to0
\]
is exact on presheaf sums, by inspecting the first nonzero component and the standard description of a sequential colimit. It stays exact after sheafification.

*The quasi-isomorphism.* The map \(C(1-s)\to M\) is a chain map because \(\Sigma(1-s)=0\). It is onto, and its kernel is \(\{(y,x)\colon y\in\operatorname{Im}(1-s)\}\), which is isomorphic to the cone of the identity of \(B\). That cone is contractible by the homotopy \((z,x)\mapsto(0,z)\), so the map is a quasi-isomorphism.

*The pieces.* The module \(M_n[n]\) has no positive cohomology. Theorem 4.1 of the lesson on normalization gives \(M_n[n]\cong NE_n\). \(\square\)

## 3. Complexes of simplicial modules

**Proposition 3.1.** Let \(T\) be the topos of sets and \(D^b_{\mathrm{out}}\) the bounded derived category of the abelian category \(s\mathrm{Ab}\) of simplicial abelian groups. For a bounded complex \(E^\bullet\) put \(B^{p,q}=N_{-q}E^p\) for \(q\leq0\). Let \(\operatorname{Tot}NE\) be its total complex, with differential \(d_{\mathrm{out}}+(-1)^pd_{\mathrm{in}}\) on \(B^{p,q}\). Then:
1. \(\operatorname{Tot}N\) induces a functor \(D^b_{\mathrm{out}}\to D(\mathbb Z)\);
2. this functor is not full.

**Proof.** (1) Let \(E^\bullet\) be acyclic and \(z\) a total cocycle of degree \(r\), with outer support in \([a,b]\).
- The component of \(z\) with \(p=b\) is an outer cocycle, so it equals \(d_{\mathrm{out}}w\), the rows \(B^{\bullet,q}\) being exact because \(N\) is exact.
- Subtracting \(d w\) moves the remaining components to \(p<b\). Repeating down to \(a\) shows that \(z\) is a boundary.

The total complex of an outer cone is the cone of the total complexes. So outer quasi-isomorphisms go to quasi-isomorphisms.

(2) The constant group \(c\mathbb Z\) is projective, because \(\operatorname{Hom}(c\mathbb Z,V)=V_0\) is exact in \(V\). Let \(K\) be the nerve of the group \(\mathbb Z\), so that \(NK=\mathbb Z\) in degree \(-1\) and \(K_0=0\). Put \(X=c\mathbb Z\) in outer degree \(-1\) and \(Y=K\) in outer degree \(0\). The Hom complex from \(X\) to \(Y\) is built from \(\operatorname{Hom}(c\mathbb Z,K)=K_0=0\), so \(\operatorname{Hom}(X,Y)=0\) [Tag 064B]. Both totalizations are \(\mathbb Z\) in degree \(-1\), with endomorphism group \(\mathbb Z\) [Tag 064B]. \(\square\)

## 4. Exercises

**Exercise 4.1.** Show that for \(R=\mathbb Z\) in the topos of sets, \(\operatorname{Ext}^p(\mathbb Z,\mathbb Z)\) is \(\mathbb Z\) for \(p=0\) and \(0\) otherwise.

## 5. Complete solutions

**4.1.** By Theorem 1.3, \(\operatorname{Ext}^p(\mathbb Z,\mathbb Z)=\operatorname{Hom}_{D(\mathbb Z)}(\mathbb Z,\mathbb Z[p])\). Since \(\mathbb Z\) is a bounded complex of projectives, this is computed by homotopy classes of chain maps [Tag 064B]. The result is \(\mathbb Z\) for \(p=0\) and zero otherwise.

## Sources

Stable Ext groups of simplicial modules and their comparison with differential graded modules are due to Illusie, in his work on the cotangent complex. The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
