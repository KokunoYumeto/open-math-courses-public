# Powers of mixed objects and diagonal maps when n! is invertible

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

For complexes with terms of both signs, the derived powers \(L\mathbf T^n\) are computed through the mixed simplicial–cosimplicial objects \(\Gamma\,iX\). The termwise tensor product \(\Gamma\,iP\otimes\Gamma\,iQ\) of two such objects is a mixed object, but it is not of the form \(\Gamma\,iX\). The diagonal maps of the lesson on diagonal maps of symmetric and exterior powers are constructed for complexes concentrated in degrees \(\leq0\) only.

This lesson assumes that \(n!\) is invertible in the ring \(A\). It proves that \(\mathbf T^n=S^n\) or \(\Lambda^n\), applied termwise to any mixed object \(M\) bounded in the cosimplicial direction, computes the symmetric, resp. exterior, tensor power of the complex \(\operatorname{Tot}NM\). That tensor power is the image of the symmetrizer, resp. antisymmetrizer, in \((\operatorname{Tot}NM)^{\otimes n}\). The comparison is a zigzag of natural \(\Sigma_n\)-equivariant quasi-isomorphisms built from shuffle and coshuffle maps. Consequences:

- for a second-quadrant double complex \(D\) of flat modules bounded in the vertical direction, \(\operatorname{Tot}N\mathbf T^n(\Gamma D)\cong L\mathbf T^n(\operatorname{Tot}D)\);
- for bounded above complexes \(P\), \(Q\) of flat modules, \(\operatorname{Tot}N\mathbf T^n(\Gamma\,iP\otimes\Gamma\,iQ)\cong\) \(L\mathbf T^n(P\otimes Q)\);
  - for \(P\), \(Q\) in degrees \(\leq0\) the inverse of this isomorphism is induced by the shuffle comparison;
  - the same holds for \(\Gamma^n\);
- the diagonal maps \(\varphi^n\), \(\psi^n\) exist on all of \(D^-(A)\), extending those of the lesson on diagonal maps;
- for a \(\mathbf Q\)-algebra \(A\), L-series of endomorphisms with coefficients in \(D^-(A)\) are defined.

**Prerequisites.**
- [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md): Lemma 1.1, Example 1.3, Proposition 2.1 and its cosimplicial form, Section 2.2, Proposition 2.3, Lemmas 4.1, 4.2, Theorem 4.4, Example 4.7, Section 5 with the map (5.1).
- [*Diagonal maps of symmetric and exterior powers*](diagonal-maps-of-symmetric-and-exterior-powers.md): Conventions, Proposition 1.2, Construction 2.1, Propositions 2.2 and 2.3 (1), Remark 2.5.
- [*Koszul complexes and the shift formulas*](koszul-complexes-and-the-shift-formulas.md): Theorem 3.2.
- [*Filtered and graded powers of complexes*](filtered-and-graded-powers-of-complexes.md): Propositions 2.2 (4), 2.4 and 2.8.
- [*L-series of endomorphisms of perfect complexes*](l-series-of-endomorphisms-of-perfect-complexes.md): Definitions 1.1, 3.1, Propositions 1.2 (1), 3.2.
- [*Traces and cup products of perfect filtered complexes*](traces-and-cup-products-of-perfect-filtered-complexes.md): Definition 2.1, Lemma 1.2.
- From the programme lesson [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution): Theorem 1.3 (shuffle and Alexander–Whitney maps) and its dual.
- From the AI-integrated Stacks project:
  - Dold–Kan in abelian categories and for cosimplicial objects [[Stacks, Tag 019G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-theorem-dold-kan), [Tag 019H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-section-dold-kan-cosimplicial)];
  - bounded above complexes of flat modules are K-flat [[Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat)].

## Conventions

\(A\) is a commutative ring of a topos \(T\), and \(\otimes=\otimes_A\). The integer \(n\geq1\) is such that \(n!\) is invertible in \(A\), that is, its image in \(\Gamma(T,A)\) is a unit; then \(k!\) is invertible for every \(k\leq n\). \(\mathbf T\) denotes \(S\) or \(\Lambda\). Complexes have differentials of degree \(+1\), and \(d(x\otimes y)=dx\otimes y+(-1)^{|x|}x\otimes dy\).

Mixed objects, \(N\), \(\Gamma\), \(i\) and \(\mathbf T^n(X)=\operatorname{Tot}N\mathbf T^n(\Gamma\,iX)\) are as in Section 2.2 of the lesson on non-additive functors. For a mixed object \(M\) with terms \(M^q_m\), \(M^q\) is the simplicial module \(m\mapsto M^q_m\). The complex \(N^hM^q\) is its normalized complex, with \(N_m\) in degree \(-m\) and differential \(\sum(-1)^id_i\). \(N^v\) is the cosimplicial normalization \(N^qV=\bigcap_i\ker(\sigma^i\colon V^q\to V^{q-1})\), with differential \(\sum(-1)^j\delta^j\). The double complex \(NM=N^hN^vM=N^vN^hM\) has terms \((NM)^{p,q}\), with \(d_h\) of bidegree \((1,0)\) and \(d_v\) of bidegree \((0,1)\).

For a double complex \(D\), \(\operatorname{Tot}D\) has the terms \(\bigoplus_{p+q=j}D^{p,q}\) and the differential \(d_h+(-1)^pd_v\), the rule of Lemma 3.1 of the lesson on Koszul complexes; then \(\operatorname{Tot}(iX)=X\). For the rule \(d_v+(-1)^qd_h\), the map \(x\mapsto(-1)^{pq}x\) on \(D^{p,q}\) is an isomorphism from the first total complex to the second. This map is the identity on \(iX\), and every statement below is transported through it.

A *strip of height \(b\)* is a double complex with \(D^{p,q}=0\) unless \(p\leq0\leq q\leq b\). A mixed object \(M\) is a strip of height \(b\) if \(NM\) is. If \(X\) vanishes in degrees \(>b\geq0\), \(iX\) is a strip of height \(b\). For a strip, \((\operatorname{Tot}D)^j=\bigoplus_{q=0}^bD^{j-q,q}\) is a finite sum, zero for \(j>b\).

## 1. Symmetric tensors

**1.0.** For a complex \(Z\), \(\Sigma_n\) acts on \(Z^{\otimes n}\) by the *Koszul rule*: the transposition of the factors \(i\), \(i+1\) sends \(z_i\otimes z_{i+1}\) to \((-1)^{|z_i||z_{i+1}|}z_{i+1}\otimes z_i\). This is the symmetry of the tensor category of complexes, an action by automorphisms of complexes; on a module in degree \(0\) it permutes factors. Put
\[
\begin{aligned}e_S&=\tfrac1{n!}\textstyle\sum_{\sigma\in\Sigma_n}\sigma,\\
e_\Lambda&=\tfrac1{n!}\textstyle\sum_{\sigma\in\Sigma_n}\operatorname{sgn}(\sigma)\sigma.\end{aligned}
\]
These are idempotents of \(A[\Sigma_n]\), with \(e_S\sigma=\sigma e_S=e_S\) and \(e_\Lambda\sigma=\sigma e_\Lambda=\operatorname{sgn}(\sigma)e_\Lambda\). For a complex \(Y\) with an action of \(\Sigma_n\) by maps of complexes, \(e_{\mathbf T}Y\) is a subcomplex and a direct summand of \(Y\).

An equivariant map \(f\colon Y\to Y'\) commutes with \(e_{\mathbf T}\). Its restriction \(e_{\mathbf T}Y\to e_{\mathbf T}Y'\) is a retract of \(f\), so it is a quasi-isomorphism if \(f\) is. Put \(\mathbf T^n_\otimes(Z)=e_{\mathbf T}(Z^{\otimes n})\), and for a map of complexes \(f\) let \(\mathbf T^n_\otimes(f)\) be the restriction of the equivariant map \(f^{\otimes n}\).

**Lemma 1.1.** For a module \(V\), the projection \(\pi\colon V^{\otimes n}\to\mathbf T^nV\) restricts to an isomorphism \(e_{\mathbf T}V^{\otimes n}\to\mathbf T^nV\), natural in \(V\). Its inverse \(s\) sends \(v_1\cdots v_n\), resp. \(v_1\wedge\cdots\wedge v_n\), to \(e_{\mathbf T}(v_1\otimes\cdots\otimes v_n)\).

**Proof.** We argue on presheaf sections and sheafify; sheafification is exact and commutes with images of idempotents. Since \(\pi\sigma=\pi\), resp. \(\pi\sigma=\operatorname{sgn}(\sigma)\pi\), we have \(\pi e_{\mathbf T}=\pi\). The map \((v_i)\mapsto e_{\mathbf T}(v_1\otimes\cdots\otimes v_n)\) is multilinear. In the symmetric case it is symmetric, because \(e_S\rho=e_S\) for each adjacent transposition \(\rho\).

In the exterior case, take \(n\geq2\). If \(v_i=v_{i+1}\), the tensor \(x\) is fixed by the transposition \(\rho\) of \(i,i+1\), so \(e_\Lambda x=e_\Lambda\rho x=-e_\Lambda x\). Hence \(e_\Lambda x=0\), \(2\) being invertible since it divides \(n!\). So the map is alternating, and \(s\) is defined; for \(n=1\) everything is the identity.

On generators \(\pi s=1\), and \(s\pi=e_{\mathbf T}\) on pure tensors, hence everywhere. If \(x=e_{\mathbf T}x\) and \(\pi x=0\), then \(x=s\pi x=0\). Finally \(\pi(e_{\mathbf T}V^{\otimes n})=\pi(V^{\otimes n})=\mathbf T^nV\). \(\square\)

**Lemma 1.2.** For a module \(V\), the degree-\(n\) part \(\kappa\colon S^nV\to\Gamma^nV\) of the algebra map \(S(V)\to\Gamma(V)\) that is the identity of \(V=\Gamma^1V\) is an isomorphism, natural in \(V\).

**Proof.** We argue on sections. Let \(\bar S=S(V)/S^{>n}(V)\) and \(\bar\Gamma=\Gamma(V)/\Gamma^{>n}(V)\). The map \(S(V)\to\Gamma(V)\) is graded, so it induces \(\bar\kappa\colon\bar S\to\bar\Gamma\), equal to \(\kappa\) in degree \(n\).

Send \(\gamma_k(v)\) to \(v^k/k!\) for \(k\leq n\) and to \(0\) for \(k>n\). The defining relations of \(\Gamma(V)\) hold in \(\bar S\):
- \((av)^k/k!=a^kv^k/k!\);
- for \(k\leq n\), \((x+y)^k/k!=\sum_{i+j=k}x^iy^j/(i!j!)\);
- \(x^ix^j/(i!j!)=\binom{i+j}{i}x^{i+j}/(i+j)!\);
- a relation of degree \(>n\) has both sides in \(S^{>n}(V)\) or contains a factor sent to \(0\).

This defines a graded algebra map \(\Gamma(V)\to\bar S\). It kills \(\Gamma^{>n}(V)\), and so induces \(\bar\theta\colon\bar\Gamma\to\bar S\).

The composite \(\bar\theta\bar\kappa\) is an algebra endomorphism of \(\bar S\) fixing \(V\), hence the identity. The composite \(\bar\kappa\bar\theta\) is an algebra endomorphism of \(\bar\Gamma\). It sends \(\gamma_k(v)\), \(k\leq n\), to \(\gamma_1(v)^k/k!=\gamma_k(v)\), by \(\gamma_1(v)^k=k!\,\gamma_k(v)\). These elements generate \(\bar\Gamma\), so \(\bar\kappa\bar\theta=1\). In degree \(n\), \(\kappa\) is therefore bijective. \(\square\)

## 2. Tensor powers of mixed objects

For double complexes \(D_1,\ldots,D_n\), the *external tensor product* \(D_1\boxtimes\cdots\boxtimes D_n\) has the terms \(\bigoplus\bigotimes_iD_i^{p_i,q_i}\) in bidegree \((p,q)\), the sum running over the families with \(\sum p_i=p\) and \(\sum q_i=q\). Its differentials are
\[
\begin{aligned}d_h&=\textstyle\sum_i(-1)^{p_1+\cdots+p_{i-1}}(\cdots\otimes d_h\otimes\cdots),\\
d_v&=\textstyle\sum_i(-1)^{q_1+\cdots+q_{i-1}}(\cdots\otimes d_v\otimes\cdots).\end{aligned}
\]
Each squares to zero, and they commute: \(d_v\) does not change the \(p_i\), and \(d_h\) does not change the \(q_i\).

**Lemma 2.1.**

1. If the \(D_i\) are strips of height \(b\), then \(\boxtimes_iD_i\) is a strip of height \(nb\), and the following map, for \(x_i\in D_i^{p_i,q_i}\), is an isomorphism of complexes:
\[
\begin{gathered}\tau_n \colon\textstyle\bigotimes_i\operatorname{Tot}D_i\\ \to\operatorname{Tot}(\boxtimes_iD_i),\\ x_1\otimes\cdots\otimes x_n\\ \mapsto(-1)^{\varepsilon}x_1\otimes\cdots\otimes x_n,\\ \varepsilon=\textstyle\sum_{i<j}q_ip_j.\end{gathered}
\]
If all \(D_i=D\), \(\tau_n\) carries the Koszul action on \((\operatorname{Tot}D)^{\otimes n}\) to the action on \(D^{\boxtimes n}\) in which the transposition of adjacent factors carries the sign \((-1)^{p_ip_{i+1}+q_iq_{i+1}}\).
2. Let \(f\colon K\to K'\) be a map of strips. If every row \(f^{\bullet,q}\), or every column \(f^{p,\bullet}\), is a quasi-isomorphism, then \(\operatorname{Tot}f\) is a quasi-isomorphism.

**Proof.** (1) The bound is clear, and \(\tau_n\) is bijective in each degree. Let \(n=2\), \(x\in D^{p,q}\), \(y\in D'^{r,s}\). The components of \(d(x\otimes y)\) in \(\operatorname{Tot}D\otimes\operatorname{Tot}D'\) are
\[
\begin{gathered}d_hx\otimes y,\quad(-1)^pd_vx\otimes y,\\
(-1)^{p+q}x\otimes d_hy,\quad(-1)^{p+q+r}x\otimes d_vy,\end{gathered}
\]
and \(\tau_2\) multiplies them by \((-1)^{qr}\), \((-1)^{(q+1)r}\), \((-1)^{q(r+1)}\), \((-1)^{qr}\) respectively. The differential of \((-1)^{qr}x\otimes y\) in \(\operatorname{Tot}(D\boxtimes D')\) is \((-1)^{qr}\) times the sum of four components:
\[
\begin{gathered}d_hx\otimes y,\quad(-1)^px\otimes d_hy,\\
(-1)^{p+r}d_vx\otimes y,\quad(-1)^{p+r+q}x\otimes d_vy.\end{gathered}
\]
The signs agree term by term, so \(\tau_2\) is a map of complexes.

For general \(n\), \(\tau_n\) is the iterate of \(\tau_2\) applied to \((x_1\otimes\cdots\otimes x_k)\otimes x_{k+1}\). This uses the identification \((D_1\boxtimes\cdots\boxtimes D_k)\boxtimes D_{k+1}=\) \(D_1\boxtimes\cdots\boxtimes D_{k+1}\), which matches the differentials. The step \(k\) contributes \((-1)^{(q_1+\cdots+q_k)p_{k+1}}\), and the product of these signs is \((-1)^\varepsilon\).

For the action, exchange \(x_i\) and \(x_{i+1}\). The terms of \(\varepsilon\) involving one of them and another factor are symmetric in \(i,i+1\). The two composites carry these exponents modulo \(2\):
- \(\tau_n\) after the Koszul exchange: \((p_i+q_i)(p_{i+1}+q_{i+1})+q_{i+1}p_i\);
- the signed exchange after \(\tau_n\): \(q_ip_{i+1}+p_ip_{i+1}+q_iq_{i+1}\).

Both are congruent to \(p_ip_{i+1}+p_iq_{i+1}+q_iq_{i+1}\).

(2) Let both strips have height \(b\). The subcomplexes \(\bigoplus_{q'\geq q}\) of rows form a finite filtration of \(\operatorname{Tot}\), with the rows as graded pieces, and the five lemma gives the first case.

For columns, let \(G_p\subseteq\operatorname{Tot}K\) be the subcomplex of the columns of index \(\geq p\); it is a subcomplex because \(d_h\) raises the column index. For \(p\leq j-1-b\), \(G_p\) and \(\operatorname{Tot}K\) agree in all degrees \(\geq j-1\), so they have the same \(H^j\); likewise for \(K'\), compatibly with \(f\). \(G_p\) has finitely many columns, so the five lemma applies to its finite filtration by columns. \(\square\)

**Lemma 2.2.**
1. If \(U_1,\ldots,U_k\) are cosimplicial modules with \(N^qU_i=0\) for \(q>b\), then \(N^q(U_1\otimes\cdots\otimes U_k)=0\) for \(q>kb\).
2. If \(M_1,\ldots,M_k\) are mixed strips of height \(b\), then \(M_1\otimes\cdots\otimes M_k\) is a strip of height \(kb\).

**Proof.** (1) We have \(\bigoplus_iU_i\cong\Gamma^\bullet(\bigoplus_iNU_i)\) [Tag 019H], with \(\bigoplus_iNU_i\) zero above \(b\). The cosimplicial form of Proposition 2.1 of the lesson on non-additive functors applies to \(\otimes^k\), which has degree \(\leq k\) (Example 1.3 there). It gives \(N^q((\bigoplus_iU_i)^{\otimes k})=0\) for \(q>kb\). The tensor product \(U_1\otimes\cdots\otimes U_k\) is a direct summand of \((\bigoplus_iU_i)^{\otimes k}\) as a cosimplicial module, and \(N\) is additive.

(2) By Dold–Kan in the simplicial direction [Tag 019G], \(N^vM_i\cong\Gamma^h(NM_i)\). So for every \(m\) the cosimplicial module \((M_i)_m\) has \(N^q=0\) for \(q>b\). By (1), \(N^v(M_1\otimes\cdots\otimes M_k)\) vanishes for \(q>kb\), and so does \(N=N^hN^v\). \(\square\)

**2.3. Shuffles and coshuffles.** For simplicial modules \(U_1,\ldots,U_k\), let \(\operatorname{sh}_k\colon\bigotimes_iNU_i\to N(\bigotimes_iU_i)\) be the iterated shuffle map. By Theorem 1.3 of *The cotangent complex*, it is natural, independent of the bracketing, and a homotopy equivalence, with \(\operatorname{AW}\circ\operatorname{sh}=1\) in \(D(A)\) (conventions of the lesson on diagonal maps).

For \(\sigma\in\Sigma_k\), let \(\sigma\) act on \(\bigotimes NU_i\) by the Koszul rule, and let \(t_\sigma\) permute the factors of \(\bigotimes U_i\) termwise. By Proposition 2.3 (1) of the lesson on diagonal maps, \(\operatorname{sh}_2\circ\sigma=N(t_\sigma)\circ\operatorname{sh}_2\). For an adjacent transposition of \(k\) factors, compute \(\operatorname{sh}_k\) by shuffling those two factors first; the naturality of \(\operatorname{sh}_{k-1}\) for \(t\) then gives \(\operatorname{sh}_k\circ\sigma=N(t_\sigma)\circ\operatorname{sh}_k\).

A cosimplicial module is a simplicial object of the opposite category \(\operatorname{Mod}(A)^{\mathrm{op}}\). That category is additive, and \(\otimes\) is a functor on it additive in each variable. The maps of Theorem 1.3 are composites of face and degeneracy maps with tensor products of maps, and their identities follow from the simplicial identities. Read in \(\operatorname{Mod}(A)^{\mathrm{op}}\), they give the *dual* of Theorem 1.3, which Section 5 of the lesson on non-additive functors uses for the cosimplicial Alexander–Whitney map \(\operatorname{AW}^c\colon NU\otimes NV\to N(U\otimes V)\), a homotopy equivalence.

The dual of the shuffle map is the *coshuffle*
\[
\operatorname{sh}^c_k\colon N(\textstyle\bigotimes_iU_i)\to\bigotimes_iNU_i .
\]
Its component in \(N^{q_1}U_1\otimes\cdots\otimes N^{q_k}U_k\) is given by the formula of the shuffle map, with each \(s_j\) replaced by \(\sigma^j\) and composites written in the opposite order. The dual statements give the following properties:
- \(\operatorname{sh}^c_k\) is a natural map of complexes, independent of the bracketing;
- \(\operatorname{sh}^c\circ\operatorname{AW}^c=1\);
- \(\sigma\circ\operatorname{sh}^c_k=\operatorname{sh}^c_k\circ N(t_\sigma)\), the transpose of Proposition 2.3 (1) of the lesson on diagonal maps.

Since \(\operatorname{AW}^c\) is a quasi-isomorphism with left inverse \(\operatorname{sh}^c\), \(\operatorname{sh}^c\) is a quasi-isomorphism, and so is every \(\operatorname{sh}^c_k\).

**Construction 2.4.** Let \(M\) be a mixed strip of height \(b\).

- \(B(M)=N(M^{\otimes n})\), the tensor power being taken termwise, with \(\Sigma_n\) acting by the maps \(N(t_\sigma)\).
- \(W^q=(N^hM^q)^{\otimes n}\) is a cosimplicial object in the category of complexes, the cosimplicial maps acting factorwise; \(\Sigma_n\) acts on it by the Koszul rule in the horizontal degrees. \(C(M)\) is the double complex with \(C^{p,q}=(N^qW)^p\), with \(d_h\) the differential of \(W\) and \(d_v=\sum_j(-1)^j\delta^j\).
- \(A(M)=(\operatorname{Tot}NM)^{\otimes n}\), with the Koszul action.

Let \(U_{p'}\) be the cosimplicial module \(q\mapsto(N^hM^q)^{p'}\); then \(NU_{p'}=(NM)^{p',\bullet}\). In horizontal degree \(p\), the cosimplicial module \(W\) is \(\bigoplus\bigotimes_iU_{p_i}\), over the finitely many \((p_1,\ldots,p_n)\) with \(p_i\leq0\) and \(\sum p_i=p\).

- \(\beta\colon C(M)\to B(M)\) is \(N^v\) of the maps \(\operatorname{sh}_n\colon W^q\to N^h((M^{\otimes n})^q)\). These form a map of cosimplicial complexes by naturality.
- \(\alpha'\colon C(M)\to(NM)^{\boxtimes n}\) is \(\operatorname{sh}^c_n\) on each summand \(N^q(\bigotimes_iU_{p_i})\), with values in \(\bigoplus_{\sum q_i=q}\bigotimes_i(NM)^{p_i,q_i}\). Put \(\alpha=\) \(\tau_n^{-1}\circ\operatorname{Tot}\alpha'\colon\) \(\operatorname{Tot}C(M)\to\) \(A(M)\).

**Proposition 2.5.** \(C(M)\) and \(B(M)\) are strips of height \(nb\), and the two maps
\[
\begin{gathered}\alpha\colon\operatorname{Tot}C(M)\to A(M),\\
\operatorname{Tot}\beta\colon\operatorname{Tot}C(M)\to\operatorname{Tot}B(M)\end{gathered}
\]
are \(\Sigma_n\)-equivariant quasi-isomorphisms, natural in \(M\).

**Proof.** *Bounds.* For \(B(M)\) the bound is Lemma 2.2 (2). For \(C(M)\), apply Lemma 2.2 (1) to the \(U_{p_i}\), whose normalizations vanish above \(b\).

*The map \(\beta\).*
- The Koszul action on \(W^q\) commutes with the differential and with the factorwise cosimplicial maps, so \(\Sigma_n\) acts on \(C(M)\) by maps of double complexes.
- \(\beta\) is a map of double complexes, and it is equivariant by 2.3.
- The row \(q\) of \(\beta\) is \(N^q\) of the quasi-isomorphism \(\operatorname{sh}_n\colon W^q\to N^h((M^{\otimes n})^q)\).
- By Dold–Kan in the abelian category of complexes [Tag 019H], \(N^q\) of a cosimplicial complex is a direct summand of its term of degree \(q\), functorially. So each row of \(\beta\) is a retract of a quasi-isomorphism, hence a quasi-isomorphism, and Lemma 2.1 (2) applies.

*The map \(\alpha\).*
- On a summand \(N^q(\bigotimes U_{p_i})\), \(d_h\) is \(\sum_i(-1)^{p_1+\cdots+p_{i-1}}N^q(\cdots\otimes d\otimes\cdots)\), where \(d\colon U_{p_i}\to U_{p_i+1}\) is a map of cosimplicial modules. By naturality, \(\operatorname{sh}^c_n\) carries it to the \(d_h\) of \((NM)^{\boxtimes n}\).
- \(\operatorname{sh}^c_n\) is a map of complexes for the vertical differentials, so \(\alpha'\) is a map of double complexes.
- On \(C(M)\), a transposition acts by \((-1)^{p_ip_{i+1}}\) times the termwise exchange. By 2.3, \(\alpha'\) carries it to the action with the sign \((-1)^{p_ip_{i+1}+q_iq_{i+1}}\), so \(\alpha\) is equivariant by Lemma 2.1 (1).
- Each column of \(\alpha'\) is a finite sum of the quasi-isomorphisms \(\operatorname{sh}^c_n\), and \(\tau_n\) is an isomorphism, so \(\alpha\) is a quasi-isomorphism by Lemma 2.1 (2).

Naturality in \(M\) is that of \(\operatorname{sh}_n\), \(\operatorname{sh}^c_n\) and \(\tau_n\). \(\square\)

## 3. Powers of mixed objects

By Lemma 1.1, applied termwise, \(\pi\) is an isomorphism of mixed objects \(e_{\mathbf T}(M^{\otimes n})\to\mathbf T^n(M)\), natural in \(M\). Since \(N\) and \(\operatorname{Tot}\) are additive, \(N(\pi)\) identifies \(e_{\mathbf T}\operatorname{Tot}B(M)\) with \(\operatorname{Tot}N\mathbf T^n(M)\). Moreover \(e_{\mathbf T}A(M)=\mathbf T^n_\otimes(\operatorname{Tot}NM)\).

**Theorem 3.1.** Let \(\mathbf T\in\{S,\Lambda\}\) and let \(n!\) be invertible in \(A\).

1. For a mixed strip \(M\), \(\alpha\) and \(N(\pi)\circ\operatorname{Tot}\beta\) restrict to quasi-isomorphisms from \(e_{\mathbf T}\operatorname{Tot}C(M)\) to \(\mathbf T^n_\otimes(\operatorname{Tot}NM)\) and to \(\operatorname{Tot}N\mathbf T^n(M)\). The resulting map
\[
\begin{aligned}&\zeta_M =\alpha\circ\beta^{-1} \colon\operatorname{Tot}N\mathbf T^n(M)\\&\quad \to\mathbf T^n_\otimes(\operatorname{Tot}NM)\end{aligned}
\]
is an isomorphism of \(D(A)\), natural in \(M\).
2. For a strip \(D\), with \(X=\operatorname{Tot}D\), the following is an isomorphism of \(D(A)\), natural in \(D\), and the identity for \(D=iX\):
\[
\begin{gathered}\chi_D=\zeta_{\Gamma\,iX}^{-1}\circ\zeta_{\Gamma D}\colon\\
\operatorname{Tot}N\mathbf T^n(\Gamma D)\to\mathbf T^n(X).\end{gathered}
\]
If \(D\) has flat terms, then \(\mathbf T^n(X)=L\mathbf T^n(X)\).
3. Let \(P\), \(Q\) be complexes vanishing in large degrees, \(M_{P,Q}=\Gamma\,iP\otimes\Gamma\,iQ\), and \(E\colon P\otimes Q\to\operatorname{Tot}NM_{P,Q}\) the map (5.1) of the lesson on non-additive functors. Then \(M_{P,Q}\) is a strip, and the following is an isomorphism of \(D(A)\), natural in \(P\) and \(Q\):
\[
\begin{gathered}\Theta_{P,Q}\\ =\zeta_{\Gamma\,i(P\otimes Q)}^{-1}\circ\mathbf T^n_\otimes(E)^{-1}\circ\zeta_{M_{P,Q}}\\ \colon\\ \operatorname{Tot}N\mathbf T^n(M_{P,Q})\to\mathbf T^n(P\otimes Q).\end{gathered}
\]
If \(P\), \(Q\) are bounded above with flat terms, then \(\mathbf T^n(P\otimes Q)=L\mathbf T^n(P\otimes Q)\), and \(P\otimes Q\) represents \(P\otimes^{\mathbf L}Q\).
4. Statements (2) and (3) hold for \(\Gamma^n\), through \(\kappa\) of Lemma 1.2 applied termwise.

**Proof.**

(1) This follows from Proposition 2.5 and 1.0, applied to the equivariant quasi-isomorphisms \(\alpha\) and \(\operatorname{Tot}\beta\).

(2) \(\Gamma D\) and \(\Gamma\,iX\) are strips, with \(\operatorname{Tot}N\Gamma D=X=\operatorname{Tot}N\Gamma\,iX\). So both maps \(\zeta\) have target \(\mathbf T^n_\otimes(X)\), and naturality follows from (1). Moreover \(X\) is bounded above. If its terms are flat, Theorem 4.4 of the lesson on non-additive functors gives \(L\mathbf T^n(X)\cong\mathbf T^n(X)\).

(3) Choose \(b\geq0\) with \(P\), \(Q\) zero above \(b\). Then \(\Gamma\,iP\) and \(\Gamma\,iQ\) are strips of height \(b\), and Lemma 2.2 (2) applies. The map \(E\) is a homotopy equivalence (Section 5 there), so \(E^{\otimes n}\) is an equivariant homotopy equivalence and \(\mathbf T^n_\otimes(E)\) is a quasi-isomorphism by 1.0. For flat terms, \(P\otimes Q\) is bounded above with flat terms and represents \(P\otimes^{\mathbf L}Q\) [Tag 06YQ].

(4) \(\kappa\) is a natural isomorphism of functors on modules, so \(\operatorname{Tot}N(\kappa)\colon\) \(\operatorname{Tot}NS^n(M)\to\) \(\operatorname{Tot}N\Gamma^n(M)\) is a natural isomorphism of complexes for every mixed object \(M\). Composing \(\chi\) and \(\Theta\) for \(S^n\) with these isomorphisms on both sides gives the statements for \(\Gamma^n\). \(\square\)

**Proposition 3.2.**
1. For a complex \(X\) vanishing in degrees \(>0\), \(C(\Gamma X)\) is \(X^{\otimes n}\) in row \(0\), \(\alpha=1\) and \(\beta=\operatorname{sh}_n\). Thus \(\zeta_{\Gamma X}\) is the inverse in \(D(A)\) of the quasi-isomorphism \(N(\pi)\circ\operatorname{sh}_n\colon\mathbf T^n_\otimes(X)\to\mathbf T^n(X)\).
2. Let \(P\), \(Q\) vanish in degrees \(>0\), and let \(g_{P,Q}\colon\Gamma(P\otimes Q)\to\Gamma P\otimes\Gamma Q\) be the map with \(N(g_{P,Q})=\operatorname{sh}_2\) (Construction 2.1 of the lesson on diagonal maps). Then \(\Theta_{P,Q}\circ N\mathbf T^n(g_{P,Q})=1\) in \(D(A)\), and the same holds for \(\Gamma^n\).

**Proof.** (1) The mixed object \(\Gamma\,iX=\Gamma X\) is constant in the cosimplicial direction. \(N^v\) of a constant cosimplicial object is its term of degree \(0\), in degree \(0\). In vertical degree \(0\), \(\operatorname{sh}^c_n\) is the identity, its only shuffle being empty, and \(\tau_n\) is the identity because all \(q_i=0\).

(2) Here \(M_{P,Q}=\Gamma P\otimes\Gamma Q\), \(\Gamma\,i(P\otimes Q)=\Gamma(P\otimes Q)\), and \(E=\operatorname{sh}_2=N(g_{P,Q})\), the map (5.1) being the shuffle map in degrees \(\leq0\). Naturality of \(\zeta\) for the map of strips \(g_{P,Q}\) gives
\[
\zeta_{M_{P,Q}}\circ N\mathbf T^n(g_{P,Q})=\mathbf T^n_\otimes(E)\circ\zeta_{\Gamma(P\otimes Q)},
\]
whence the claim. For \(\Gamma^n\), \(\kappa\) commutes with \(N\Gamma^n(g_{P,Q})\) and \(NS^n(g_{P,Q})\) by naturality. \(\square\)

**Corollary 3.3.** For a complex \(X\) vanishing in large degrees, \(\zeta_{\Gamma\,iX}\colon\mathbf T^n(X)\to\mathbf T^n_\otimes(X)\) is an isomorphism of \(D(A)\), natural in \(X\). For \(L\in D^-(A)\) represented by a bounded above complex \(X\) of flat modules, \(L\mathbf T^n(L)\cong e_{\mathbf T}(X^{\otimes n})\), naturally in \(L\).

**Proof.** The first statement is Theorem 3.1 (1) for \(M=\Gamma\,iX\), with \(\operatorname{Tot}N\Gamma\,iX=X\). For the second, \(L\mathbf T^n(L)\cong\mathbf T^n(X)\) by Theorem 4.4 of the lesson on non-additive functors. The functor \(X\mapsto e_{\mathbf T}(X^{\otimes n})\) on bounded above flat complexes inverts quasi-isomorphisms, by the first statement and Lemma 4.1 there. It carries homotopic maps to homotopic maps: averaging a homotopy between \(f^{\otimes n}\) and \(g^{\otimes n}\) over \(\Sigma_n\) gives an equivariant one. It therefore descends to \(D^-(A)\) by Lemma 4.2 (2) there, and \(\zeta\) is natural. \(\square\)

## 4. Diagonal maps

For complexes \(P\), \(Q\), let \(u\colon(P\otimes Q)^{\otimes n}\to P^{\otimes n}\otimes Q^{\otimes n}\) be the Koszul permutation
\[
\begin{gathered}\textstyle\bigotimes_i(x_i\otimes y_i)\mapsto(-1)^{\eta}x_1\otimes\cdots\otimes x_n\\
\otimes y_1\otimes\cdots\otimes y_n,\quad\eta=\textstyle\sum_{i<j}|y_i||x_j|,\end{gathered}
\]
an isomorphism of complexes. For \(\sigma\in\Sigma_n\), \(u\circ\sigma=(\sigma\otimes\sigma)\circ u\), both sides being the Koszul action of one permutation of \(2n\) factors. Hence \((e_S\otimes e_S)u\,e_S=(e_S\otimes e_S)u\), and \((e_\Lambda\otimes e_S)u\,e_\Lambda=(e_\Lambda\otimes e_S)u\) since \(\operatorname{sgn}(\sigma)^2=1\). So
\[
\begin{aligned}u_S&=(e_S\otimes e_S)u\colon\\&\ S^n_\otimes(P\otimes Q)\to S^n_\otimes P\otimes S^n_\otimes Q,\\
u_\Lambda&=(e_\Lambda\otimes e_S)u\colon\\&\ \Lambda^n_\otimes(P\otimes Q)\to\Lambda^n_\otimes P\otimes S^n_\otimes Q\end{aligned}
\]
are maps of complexes. For modules \(V\), \(W\) in degree \(0\), Lemma 1.1 and Proposition 1.2 of the lesson on diagonal maps identify \(u_S\), \(u_\Lambda\) with \(\varphi^n\), \(\psi^n\). For instance,
\[
\begin{gathered}u_S\bigl(s(\textstyle\prod(v_i\otimes w_i))\bigr)\\
=s(\textstyle\prod v_i)\otimes s(\textstyle\prod w_i),\end{gathered}
\]
and likewise for \(u_\Lambda\).

**Theorem 4.1.** Let \(n!\) be invertible in \(A\). For bounded above complexes \(P\), \(Q\) of flat modules, write \(\zeta_X=\zeta_{\Gamma\,iX}\) and put, in \(D(A)\),
\[
\begin{aligned}\varphi^n_{P,Q}&=(\zeta_P^{-1}\otimes\zeta_Q^{-1})\circ u_S\circ\zeta_{P\otimes Q}\colon\\
&\quad S^n(P\otimes Q)\to S^n(P)\otimes S^n(Q),\\
\psi^n_{P,Q}&=(\zeta_P^{-1}\otimes\zeta_Q^{-1})\circ u_\Lambda\circ\zeta_{P\otimes Q}\colon\\
&\quad\Lambda^n(P\otimes Q)\to\Lambda^n(P)\otimes S^n(Q).\end{aligned}
\]
Put \(\varphi^0=\psi^0\), the unit isomorphism \(A\to A\otimes^{\mathbf L}A\).

1. These maps define morphisms natural in \(L,M\in D^-(A)\):
\[
\begin{aligned}\varphi^n_{L,M}&\colon LS^n(L\otimes^{\mathbf L}M)\\&\quad\to LS^nL\otimes^{\mathbf L}LS^nM,\\
\psi^n_{L,M}&\colon L\Lambda^n(L\otimes^{\mathbf L}M)\\&\quad\to L\Lambda^nL\otimes^{\mathbf L}LS^nM.\end{aligned}
\]
2. If \(P\), \(Q\) vanish in degrees \(>0\), then \(\varphi^n_{P,Q}\) and \(\psi^n_{P,Q}\) are the maps of Construction 2.1 of the lesson on diagonal maps. Hence, on \(D^{\leq0}(A)\), the morphisms of (1) are those of Proposition 2.2 there.

**Proof.** (1)
- \(S^n(P)\) and \(S^n_\otimes(P)\) are bounded above with flat terms, by Proposition 2.2 (4) of the lesson on filtered and graded powers and as a summand of \(P^{\otimes n}\). So they are K-flat [Tag 06YQ], the tensor products of complexes in the definition compute the derived ones, and \(\varphi^n_{P,Q}\) is a morphism of \(D(A)\). It is natural for maps of complexes in \(P\) and \(Q\), since \(\zeta\) and \(u_S\) are.
- The source \(S^n(P\otimes Q)\) and the target \(S^n(P)\otimes S^n(Q)\) carry quasi-isomorphisms in either variable to quasi-isomorphisms, by K-flatness and Lemma 4.1 of the lesson on non-additive functors. They carry homotopic maps to homotopic maps, by Proposition 2.3 there.
- Given \(L\), \(M\), choose quasi-isomorphisms \(P\to L\), \(Q\to M\) from bounded above flat complexes (Lemma 4.2 (1) there). Define \(\varphi^n_{L,M}\) through the isomorphisms \(LS^n(L\otimes^{\mathbf L}M)\cong S^n(P\otimes Q)\) and \(LS^nL\otimes^{\mathbf L}LS^nM\cong\) \(S^n(P)\otimes S^n(Q)\) of Theorem 4.4 there.
- By Lemma 4.2 (2) there, a morphism \(a\colon L\to L'\) is \(f\circ s^{-1}\) for maps of complexes \(s\colon P''\to P\), a quasi-isomorphism, and \(f\colon P''\to P'\), with \(P''\) bounded above and flat. The squares for \(s\) and \(f\) commute, and the source and target send \(s\) to isomorphisms. So the square for \(a\) commutes.
- With \(a=1_L\), this shows that the definition does not depend on \(P\). The second variable is treated in the same way. The case of \(\psi^n\) is the same.

(2) Let \(X=P\otimes Q\), \(G=\Gamma P\otimes\Gamma Q\) and \(g=g_{P,Q}\). By Proposition 3.2 (1), \(\zeta_Y^{-1}=N(\pi)\circ\operatorname{sh}_n\) on \(S^n_\otimes(Y)\) for \(Y=P,Q,X\). Let \(\varphi_c=\operatorname{AW}\circ N(\varphi^n)\circ NS^n(g)\), with \(\varphi^n\) termwise. We use:
- (a) \(N(g^{\otimes n})\circ\operatorname{sh}_n=\operatorname{sh}_n\circ\operatorname{sh}_2^{\otimes n}=\operatorname{sh}_{2n}\), for the \(2n\) factors \(\Gamma P,\Gamma Q,\Gamma P,\ldots\), by naturality and associativity;
- (b) \(N(u_0)\circ\operatorname{sh}_{2n}=\operatorname{sh}_{2n}\circ u\), for the termwise permutation \(u_0\colon G^{\otimes n}\to(\Gamma P)^{\otimes n}\otimes(\Gamma Q)^{\otimes n}\), by 2.3;
- (c) \(\operatorname{sh}_{2n}=\operatorname{sh}_2\circ(\operatorname{sh}_n\otimes\operatorname{sh}_n)\) on \(P^{\otimes n}\otimes Q^{\otimes n}\);
- (d) termwise, \(S^n(g)\circ\pi=\pi\circ g^{\otimes n}\) and \(\varphi^n\circ\pi=(\pi\otimes\pi)\circ u_0\), by Proposition 1.2 there;
- (e) \(N(\pi\otimes\pi)\circ\operatorname{sh}_2=\operatorname{sh}_2\circ(N\pi\otimes N\pi)\), and \(\operatorname{AW}\circ\operatorname{sh}_2=1\) in \(D(A)\).

Then, on \(X^{\otimes n}\), in \(D(A)\),
\[
\begin{aligned}&\varphi_c\circ N(\pi)\circ\operatorname{sh}_n\\
&=\operatorname{AW}\circ N(\pi\otimes\pi)\\&\quad\circ N(u_0)\circ N(g^{\otimes n})\circ\operatorname{sh}_n\\
&=\operatorname{AW}\circ N(\pi\otimes\pi)\circ\operatorname{sh}_{2n}\circ u\\
&=\operatorname{AW}\circ\operatorname{sh}_2\\&\quad\circ(N\pi\operatorname{sh}_n\otimes N\pi\operatorname{sh}_n)\circ u\\
&=(N\pi\operatorname{sh}_n\otimes N\pi\operatorname{sh}_n)\circ u.\end{aligned}
\]
Since \(\operatorname{sh}_n\) is equivariant and \(\pi e_S=\pi\), we have \(N(\pi)\operatorname{sh}_ne_S=N(\pi)\operatorname{sh}_n\). The last line therefore equals \((\zeta_P^{-1}\otimes\zeta_Q^{-1})\circ(e_S\otimes e_S)\circ u\). Restricted to \(S^n_\otimes(X)\), this gives \(\varphi_c\circ\zeta_X^{-1}=(\zeta_P^{-1}\otimes\zeta_Q^{-1})\circ u_S\), that is, \(\varphi_c=\varphi^n_{P,Q}\). For \(\psi^n\) use \(\pi_\Lambda\), \(\psi^n\circ\pi_\Lambda=(\pi_\Lambda\otimes\pi_S)\circ u_0\), and \(e_\Lambda\otimes e_S\). On \(D^{\leq0}(A)\) the representatives may be taken in degrees \(\leq0\) (Proposition 2.4 of the lesson on filtered and graded powers), and both constructions use the same isomorphisms of Theorem 4.4. \(\square\)

**Corollary 4.2 (L-series with general coefficients).** Let \(A\) be a \(\mathbf Q\)-algebra, \(M\in D^-(A)\), \(E\in D^{\leq0}(A)\) of bounded perfect amplitude, and \(f\colon E\to E\otimes^{\mathbf L}M\). Then the following element is defined, in the ring of Definition 1.1 and Proposition 1.2 (1) of the lesson on L-series:
\[
\begin{gathered}L_t(f)=\textstyle\sum_{n\geq0}\operatorname{Tr}\bigl(\varphi^n_{E,M}\circ LS^n(f)\bigr)t^n\\
\in\operatorname{Hom}(A,LS^\bullet(M)).\end{gathered}
\]
It has constant term \(1\) and is invertible. For \(M\in D^{\leq0}(A)\) it is the L-series of Definition 3.1 there. It is natural in \(M\) and invariant under conjugation by isomorphisms \(E\to E'\).

**Proof.**
- \(LS^nE\) is perfect, by Proposition 2.8 of the lesson on filtered and graded powers with an interval containing \(0\).
- The trace of \(\varphi^n\circ LS^n(f)\colon\) \(LS^nE\to\) \(LS^nE\otimes^{\mathbf L}LS^nM\) is defined for arbitrary coefficients (Definition 2.1 of the lesson on traces).
- For \(n=0\), \(LS^0E=A\) and \(\varphi^0=1\), so the constant term is \(\operatorname{Tr}(1_A)=1\), and the series is invertible by Proposition 1.2 (1) there.
- The agreement for \(M\in D^{\leq0}(A)\) is Theorem 4.1 (2).
- Naturality in \(M\) and conjugation invariance follow by the proofs of Proposition 3.2 (1), (2) there. These use only the naturality of \(\varphi^n\) in both variables (Theorem 4.1 (1)) and Lemma 1.2 (2), (3) of the lesson on traces. \(\square\)

**Remark 4.3 (scope).** All results of this lesson use the invertibility of \(n!\) through the idempotents \(e_{\mathbf T}\). Over \(\mathbf Z\) neither \(e_S\) nor the coinvariants describe \(LS^n\) (Exercise 5.2). The following are not treated here:
- the filtered and graded forms of Theorems 3.1 and 4.1;
- the multiplicativity of \(\varphi^n\) and \(\psi^n\);
- their compatibility with the shift isomorphisms for objects not in \(D^{\leq0}(A)\).

## 5. Exercises

**Exercise 5.1.** Let \(2\) be invertible in \(A\). Use Corollary 3.3 to compute \(LS^2\), \(L\Lambda^2\) and \(L\Gamma^2\) of \(A[1]\) and of \(A[-1]\). Compare with Theorem 3.2 of the lesson on Koszul complexes.

**Exercise 5.2.** On the punctual topos with \(A=\mathbf Z\), compute the coinvariants \((X^{\otimes2})_{\Sigma_2}\) of the Koszul action for \(X=\mathbf Z[1]\), and compare with \(LS^2(X)\).

## 6. Complete solutions

**5.1.** \(A[1]^{\otimes2}\) is \(A\) in degree \(-2\), spanned by \(x\otimes x\) with \(|x|=-1\). The transposition acts by \((-1)^{(-1)(-1)}=-1\), so \(e_S=0\) and \(e_\Lambda=1\) on it. Hence:
- \(LS^2(A[1])\cong0\);
- \(L\Lambda^2(A[1])\cong A[2]\);
- \(L\Gamma^2(A[1])\cong0\), by Lemma 1.2.

For \(A[-1]\), \(|x|=1\), and the sign is again \(-1\). So \(LS^2(A[-1])\cong0\cong L\Gamma^2(A[-1])\) and \(L\Lambda^2(A[-1])\cong A[-2]\).

Theorem 3.2 of the lesson on Koszul complexes gives:
- \(LS^2(A[1])\cong L\Lambda^2(A)[2]=0\);
- \(L\Lambda^2(A[1])\cong L\Gamma^2(A)[2]=A[2]\);
- with \(E=A[-1]\), \(A=LS^2(A)\cong L\Lambda^2(A[-1])[2]\), so \(L\Lambda^2(A[-1])\cong A[-2]\);
- with \(E=A[-1]\), \(0=L\Lambda^2(A)\cong L\Gamma^2(A[-1])[2]\).

All of these agree with the values above.

**5.2.** \(X^{\otimes2}=\mathbf Z(x\otimes x)\) in degree \(-2\), and the transposition acts by \(-1\). The coinvariants are \(\mathbf Z/(2\,x\otimes x)\), that is, \((\mathbf Z/2)[2]\). But \(LS^2(\mathbf Z[1])\cong L\Lambda^2(\mathbf Z)[2]=0\) by Theorem 3.2 of the lesson on Koszul complexes, \(\Lambda^2\mathbf Z\) being zero. So the description of Corollary 3.3, with coinvariants in place of \(e_S\)-images, fails when \(2\) is not invertible.

## Sources

The mixed objects, the derived powers of complexes with terms of both signs, and the diagonal maps \(\varphi^n\), \(\psi^n\) on the whole bounded above derived category are due to Illusie, in his work on the cotangent complex. The shuffle and Alexander–Whitney maps are due to Eilenberg and Mac Lane, and the degree bound is due to Dold and Puppe. The description of symmetric and exterior powers by symmetrizers when \(n!\) is invertible is classical. Integral approaches through the extension of polynomial functors to stable categories are in:
- C. Barwick, S. Glasman, A. Mathew and T. Nikolaus, *K-theory and polynomial functors*, [arXiv:2102.00936](https://arxiv.org/abs/2102.00936);
- L. Brantner and A. Mathew, *Deformation theory and partition Lie algebras*, [arXiv:1904.07352](https://arxiv.org/abs/1904.07352).

The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and is completed here. The homological algebra is that of the Stacks project.
