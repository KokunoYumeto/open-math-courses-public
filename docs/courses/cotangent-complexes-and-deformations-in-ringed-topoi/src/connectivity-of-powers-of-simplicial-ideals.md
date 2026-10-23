# Connectivity of powers of simplicial ideals

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(R\) be a simplicial ring of a topos and \(J\) an ideal of \(R\) such that \(\pi_0(J)=0\) and every \(J_n\) is a weakly regular ideal of \(R_n\). Quillen's convergence theorem states that the powers \(J^m\) are \(m\)-connective: their homotopy vanishes in the degrees below \(m\). Apply it to the simplicial ring \(Q\) that computes \(\operatorname{Tor}^A_\bullet(B,B)\) for a quotient \(B=A/I\), with \(J\) the augmentation ideal: then \(\operatorname{Tor}^A_n(B,B)=\pi_n(Q/J^{n+1})\), so the filtration of \(\operatorname{Tor}\) by the powers of \(J\) is finite in each degree. The lesson proves:

- the derived tensor product of an \(a\)-connective and a \(b\)-connective module over a simplicial ring is \((a+b)\)-connective;
- a module with flat terms over a simplicial ring \(B\) is \(k\)-connective if its base change to \(\pi_0(B)\) is;
- for a module \(V\) with flat terms over a simplicial ring \(B\) with \(\pi_0(V)=0\), the module \(\Lambda^a_BV\otimes_BS^b_BV\) is \((a+b)\)-connective;
- the convergence theorem, and its consequence for the standard resolution;
- the stable homology of the free abelian group functor in low degrees: for an abelian sheaf \(X\), it is \(X/2X\) in degree \(2\) and the \(2\)-torsion of \(X\) in degree \(3\), and it is torsion in every positive degree; as a consequence, the spectra of complexes over the derived tensor product \(A\otimes^{\mathbf L}_{\mathbb Z}\mathcal O\) do not form a fully faithful functor on all bounded complexes.

**Prerequisites.** [*Weakly regular ideals*](weakly-regular-ideals.md) (Section 2, Definition 2.4, Theorem 3.3, Corollary 3.4, Propositions 4.1 and 4.2); [*Derived tensor products of simplicial modules*](derived-tensor-products-of-simplicial-modules.md) (Definition 3.1, Proposition 3.2); [*Spectral sequences for derived tensor products*](spectral-sequences-for-derived-tensor-products.md) (Section 2, Theorems 2.1 and 3.4); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Section 2, Proposition 2.2, Theorem 3.2, Theorem 4.4, Example 4.7); [*Koszul complexes and the shift formulas*](koszul-complexes-and-the-shift-formulas.md) (Theorem 3.2); [*Stable derived functors*](stable-derived-functors.md) (Conventions, Theorems 1.3 and 1.6, Examples 2.1 and 2.3); [*Stabilization of non-additive functors*](stabilization-of-non-additive-functors.md) (Theorem 3.6, Corollary 3.7, Example 5.2, Exercise 6.2); [*Differential graded modules in a topos*](differential-graded-modules-in-a-topos.md) (Lemma 1.1, Propositions 1.2, 1.3, 2.3 and 2.5); [*The stable ring of a ring and the Mac Lane resolution*](the-stable-ring-of-a-ring-and-the-mac-lane-resolution.md) (Proposition 2.4); [*Ext groups of modules as cohomology of spectral nerves*](ext-groups-of-modules-as-cohomology-of-spectral-nerves.md) (Conventions, Proposition 3.1, Definition 3.2, Proposition 3.4); [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution) (Theorem 1.2). From the AI-integrated Stacks project: regular sequences are Koszul-regular [[Stacks, Tag 062F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-regular-koszul-regular)]; short exact sequences of differential graded modules give distinguished triangles [[Tag 0FTB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sdga.html#sdga-lemma-derived-canonical-delta-functor)].

## Conventions

\(T\) is a topos and rings are commutative. For a simplicial module \(E\) over a simplicial ring, \(H_n(E)=\pi_n(E)\) is the \(n\)-th homology sheaf of its normalized complex \(NE\); \(E\) is *\(k\)-connective* if \(H_i(E)=0\) for \(i<k\). Tensor products, exterior and symmetric powers of modules over a simplicial ring are formed degreewise, and a module has *flat terms* if each of its terms is flat over the corresponding term of the ring. For a simplicial ring \(R\) and \(R\)-modules \(E\), \(F\), \(\operatorname{Tor}^R_q(E,F)\) is the \(R\)-module with terms \(\operatorname{Tor}^{R_n}_q(E_n,F_n)\), whose face and degeneracy maps are induced by those of \(R\), \(E\) and \(F\) (Section 2 of the lesson on spectral sequences for derived tensor products). Weakly regular ideals are as in the lesson on weakly regular ideals.

## 1. Connectivity

**Lemma 1.1.** Let \(A\) be a simplicial ring, \(E\) an \(a\)-connective and \(F\) a \(b\)-connective \(A\)-module. Then \(E\otimes^\ell_AF\) is \((a+b)\)-connective.

**Proof.** In the spectral sequence of Theorem 3.4 of the lesson on spectral sequences for derived tensor products, \(E^2_{p,q}=H_p(\pi_q(E)\otimes^\ell_AF)\) vanishes for \(q<a\). By the symmetry of \(\otimes^\ell_A\) and the same theorem for \(F\otimes^\ell_A\pi_q(E)\), whose second page \(H_p(\pi_{q'}(F)\otimes^\ell_A\pi_q(E))\) vanishes for \(q'<b\) and for \(p<0\), \(H_p(\pi_q(E)\otimes^\ell_AF)=0\) for \(p<b\). The spectral sequences converge, so \(H_n(E\otimes^\ell_AF)=0\) for \(n<a+b\). \(\square\)

**Lemma 1.2.** Let \(B\) be a simplicial ring and \(E\), \(F\) \(B\)-modules. Then \(\pi_0(E\otimes_BF)=\pi_0(E)\otimes_{\pi_0(B)}\pi_0(F)\), and the same holds for \(E\otimes^\ell_BF\).

**Proof.** For a simplicial module \(X\), \(\pi_0(X)\) is the cokernel of \(d_0-d_1\colon X_1\to X_0\). Put \(E'=(d_0-d_1)(E_1)\) and \(F'=(d_0-d_1)(F_1)\). The ideal \((d_0-d_1)(B_1)\) of \(B_0\) kills \(E_0/E'\), since \((d_0c-d_1c)e=(d_0-d_1)(c\,s_0e)\); so \(\pi_0(E)\otimes_{\pi_0(B)}\pi_0(F)\) is the quotient of \(E_0\otimes_{B_0}F_0\) by the image \(S\) of \(E'\otimes F_0+E_0\otimes F'\). This submodule \(S\) is the image of \(d_0-d_1\) on \(E_1\otimes_{B_1}F_1\). Indeed \((d_0-d_1)(x\otimes s_0f)=(d_0x-d_1x)\otimes f\) and \((d_0-d_1)(s_0e\otimes y)=e\otimes(d_0y-d_1y)\), so \(S\) lies in the image; conversely the image is generated by the elements
\[
\begin{aligned}&d_0x\otimes d_0y-d_1x\otimes d_1y\\&\quad=(d_0x-d_1x)\otimes d_0y\\&\qquad+d_1x\otimes(d_0y-d_1y),\end{aligned}
\]
which lie in \(S\).
For the derived tensor product, \(E\otimes^\ell_BF=P(E)\otimes_BP(F)\) with quasi-isomorphisms \(P(E)\to E\) and \(P(F)\to F\) (Definition 3.1 of the lesson on derived tensor products), which induce isomorphisms on \(\pi_0\). \(\square\)

**Lemma 1.3.** Let \(B\) be a simplicial ring and \(M\) a \(B\)-module with flat terms. If \(\pi_0(B)\otimes_BM\) is \(k\)-connective, so is \(M\).

**Proof.** Here \(\pi_0(B)\) is a \(B\)-module through \(B\to\pi_0(B)\), and since \(M\) has flat terms, \(\pi_0(B)\otimes_BM\) represents \(M\otimes^\ell_B\pi_0(B)\) (Proposition 3.2 (1) of the lesson on derived tensor products). We show \(\pi_i(M)=0\) for \(i<k\) by induction on \(i\). Let \(i<k\) and suppose \(\pi_j(M)=0\) for \(j<i\). In the spectral sequence of Theorem 3.4 of the lesson on spectral sequences for derived tensor products,
\[
\begin{aligned}&E^2_{p,q}=H_p\bigl(\pi_q(M)\otimes^\ell_B\pi_0(B)\bigr)\\&\quad\Longrightarrow H_{p+q}\bigl(M\otimes^\ell_B\pi_0(B)\bigr),\end{aligned}
\]
the terms with \(q<i\) vanish, and \(E^2_{0,i}=\pi_i(M)\otimes_{\pi_0(B)}\pi_0(B)=\pi_i(M)\) by Lemma 1.2. The differentials \(d^r\colon E^r_{p,q}\to E^r_{p-r,q+r-1}\) that leave \(E_{0,i}\) land in negative \(p\), and those that reach it start from \(q=i-r+1<i\). So \(\pi_i(M)=E^\infty_{0,i}\) is a subquotient of \(H_i(\pi_0(B)\otimes_BM)\), which is zero because \(i<k\). \(\square\)

**Proposition 1.4.** Let \(B\) be a simplicial ring and \(V\) a \(B\)-module with flat terms such that \(\pi_0(V)=0\). Then for \(a,b\geq0\) the module \(\Lambda^a_BV\otimes_BS^b_BV\) is \((a+b)\)-connective.

**Proof.** Its terms are flat (Example 4.7 of the lesson on non-additive functors). Let \(B'=\pi_0(B)\) and \(V'=B'\otimes_BV\), a simplicial module over the constant ring \(B'\) with flat terms; \(\pi_0(V')=B'\otimes_{\pi_0(B)}\pi_0(V)=0\) by Lemma 1.2. Exterior and symmetric powers and tensor products commute with base change, so
\[
\begin{aligned}&B'\otimes_B(\Lambda^a_BV\otimes_BS^b_BV)\\&\quad=\Lambda^a_{B'}V'\otimes_{B'}S^b_{B'}V'.\end{aligned}
\]
By Lemma 1.3 it suffices to show that this is \((a+b)\)-connective; so we may assume that \(B\) is a constant ring.

Then the terms of \(NV\) are flat, being direct summands of those of \(V\), and \(N_1V\to N_0V\) is surjective because \(H_0(V)=0\); so its kernel \(Z_1\) is flat, and \(NV\) is quasi-isomorphic to the complex \(\cdots\to N_2V\to Z_1\to0\) of flat modules in homological degrees \(\geq1\). Hence \(NV\cong E[1]\) in \(D(B)\), with \(E\) a complex of flat modules in cohomological degrees \(\leq0\). For \(b\geq1\), by Theorem 4.4 and Section 2 of the lesson on non-additive functors, the normalized complex of \(S^b_BV\) is \(S^b(NV)\), which represents \(LS^b(NV)\cong LS^b(E[1])\); this is \(L\Lambda^b(E)[b]\) by Theorem 3.2 of the lesson on Koszul complexes. As \(L\Lambda^b(E)=\Lambda^b(E)\) vanishes in positive degrees (Proposition 2.2 of the lesson on non-additive functors), \(S^b_BV\) is \(b\)-connective. In the same way \(\Lambda^a_BV\) represents \(L\Lambda^a(E[1])\cong L\Gamma^a(E)[a]\) and is \(a\)-connective for \(a\geq1\); for \(a=0\) or \(b=0\) the factor is \(B\). The terms of \(S^b_BV\) and \(\Lambda^a_BV\) are flat, so their tensor product computes the derived one (Proposition 3.2 (1) of the lesson on derived tensor products), which is \((a+b)\)-connective by Lemma 1.1. \(\square\)

**Lemma 1.5.** Let \(0\to X_r\to\cdots\to X_0\to Z\to0\) be an exact sequence of simplicial modules in which every \(X_j\) is \(c\)-connective. Then \(Z\) is \(c\)-connective.

**Proof.** Let \(K_j\) be the image of \(X_{j+1}\to X_j\), so that \(K_{r-1}=X_r\), \(Z=X_0/K_0\), and \(0\to K_j\to X_j\to K_{j-1}\to0\) is exact, with \(K_{-1}=Z\). If \(K_j\) is \(c\)-connective, the exact sequence \(H_i(X_j)\to H_i(K_{j-1})\to H_{i-1}(K_j)\) shows that \(K_{j-1}\) is. Descend from \(j=r-1\). \(\square\)

## 2. The convergence theorem

**Theorem 2.1 (convergence).** Let \(R\) be a simplicial ring of \(T\) and \(J\) an ideal of \(R\) such that every \(J_n\) is a weakly regular ideal of \(R_n\). If \(\pi_0(J)=0\), then \(J^m\) is \(m\)-connective for every \(m\geq1\).

**Proof.** Put \(B=R/J\), a simplicial ring, and \(N=J/J^2\), a \(B\)-module. Its terms \(N_n=J_n/J_n^2\) are flat over \(B_n\), because \(J_n\) is weakly regular, and \(\pi_0(N)=0\), because \(J\to N\) is surjective in each degree.

*Step 1: the Tor sheaves of the quotients.* For \(q\geq1\) and \(n\geq0\), \(\operatorname{Tor}^R_q(B,R/J^{n+1})\) is \((q+n)\)-connective. Indeed, by Corollary 3.4 of the lesson on weakly regular ideals, applied in each degree, there are exact sequences
\[
\begin{aligned}&0\to\Lambda^{q+n}_{B_k}N_k\to\cdots\to\Lambda^q_{B_k}N_k\otimes S^n_{B_k}N_k\\&\quad\to\operatorname{Tor}^{R_k}_q(B_k,R_k/J_k^{n+1})\to0,\end{aligned}
\]
natural in the pair \((R_k,J_k)\). The face and degeneracy maps of \(R\) are maps of pairs, so these sequences form an exact sequence of simplicial modules, from \(\Lambda^{q+n}_BN\) to \(\operatorname{Tor}^R_q(B,R/J^{n+1})\). By Proposition 1.4 its terms \(\Lambda^{q+j}_BN\otimes_BS^{n-j}_BN\) are \((q+n)\)-connective, and Lemma 1.5 concludes.

*Step 2: dimension shifting.* In each degree, \(R_k\) is flat over itself, so the sequences \(0\to J^m\to R\to R/J^m\to0\) and \(0\to J\to R\to B\to0\) give natural isomorphisms \(\operatorname{Tor}^R_q(B,R/J^m)\cong\operatorname{Tor}^R_{q-1}(B,J^m)\) for \(q\geq2\) and \(\operatorname{Tor}^R_{s+1}(B,J^m)\cong\operatorname{Tor}^R_s(J,J^m)\) for \(s\geq1\). By Step 1, \(\operatorname{Tor}^R_1(B,J^m)\cong\operatorname{Tor}^R_2(B,R/J^m)\) is \((m+1)\)-connective, and \(\operatorname{Tor}^R_s(J,J^m)\cong\operatorname{Tor}^R_{s+2}(B,R/J^m)\) is \((s+m+1)\)-connective for \(s\geq1\).

*Step 3: induction on \(m\).* For \(m=1\) the claim is the hypothesis. Suppose \(J^m\) is \(m\)-connective. By Lemma 1.1, \(J\otimes^\ell_RJ^m\) is \((m+1)\)-connective. Theorem 2.1 of the lesson on spectral sequences for derived tensor products gives the spectral sequence of a first-quadrant double complex
\[
\begin{aligned}&E^2_{p,s}=H_p\bigl(\operatorname{Tor}^R_s(J,J^m)\bigr)\\
&\quad\Longrightarrow H_{p+s}(J\otimes^\ell_RJ^m),\end{aligned}
\]
with \(d^r\colon E^r_{p,s}\to E^r_{p-r,s+r-1}\). Its terms with \(s\geq1\) vanish for \(p<s+m+1\) by Step 2, in particular in every total degree \(\leq m\). For \(t\leq m\), no differential leaves or reaches \(E_{t,0}\): those leaving it land in total degree \(t-1\) with \(s\geq1\), and those reaching it come from \(s<0\). So \(E^2_{t,0}=H_t(J\otimes_RJ^m)\) is a subquotient of \(H_t(J\otimes^\ell_RJ^m)=0\). In each degree the sequence \(0\to J_k\to R_k\to B_k\to0\), tensored with \(J^m_k\), gives the exact sequence
\[
\begin{aligned}&0\to\operatorname{Tor}^R_1(B,J^m)\\
&\quad\to J\otimes_RJ^m\to J^{m+1}\to0,\end{aligned}
\]
the image of \(J\otimes_RJ^m\to J^m\) being \(J^{m+1}\). For \(t\leq m\), \(H_t(J\otimes_RJ^m)=0\) and \(H_{t-1}(\operatorname{Tor}^R_1(B,J^m))=0\), since \(t-1<m+1\). So \(H_t(J^{m+1})=0\) for \(t\leq m\), and \(J^{m+1}\) is \((m+1)\)-connective. \(\square\)

**Corollary 2.2.** Let \(A\) be a ring of \(T\) and \(B\) an \(A\)-algebra whose multiplication \(B\otimes_AB\to B\) is an isomorphism (for example \(B=A/I\)). Let \(P\to B\) be the resolution of Section 2 of the lesson on weakly regular ideals, \(Q=P\otimes_AB\), and \(J\) the kernel of the augmentation \(Q\to B\otimes_AB\to B\).

1. \(J^m\) is \(m\)-connective for every \(m\geq1\).
2. The map \(\pi_n(Q)\to\pi_n(Q/J^m)\) is an isomorphism for \(m\geq n+1\); here \(\pi_n(Q)=\operatorname{Tor}^A_n(B,B)\).

**Proof.** (1) \(Q_n=B[X_n]\), and the augmentation sends \(x\in X_n\) to the image \(\varepsilon(x)\) of \(x\) in \(B\). The automorphism \(x\mapsto x-\varepsilon(x)\) of the \(B\)-algebra \(B[X_n]\) identifies \(Q_n\) with the augmented algebra \(S_B(B^{(X_n)})\), whose augmentation ideal is weakly regular (Proposition 4.1 of the lesson on weakly regular ideals). Moreover \(\pi_0(Q)=B\otimes_AB\to B\) is an isomorphism, so \(\pi_0(J)=0\). Theorem 2.1 applies.

(2) In the long exact sequence of \(0\to J^m\to Q\to Q/J^m\to0\), \(\pi_n(J^m)\) and \(\pi_{n-1}(J^m)\) vanish for \(m\geq n+1\), by (1). \(\square\)

**Remark 2.3.** For a surjection of rings \(A\to B\) and a resolution of \(B\) built from polynomial cells, the same connectivity is Lemma 7.4 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#7-complete-intersections-and-computations), where it gives the convergence of the spectral sequence of the filtration by the powers of \(J\) (Theorem 7.5 there). Corollary 2.2 gives it for rings of a topos and for the functorial resolution of the lesson on weakly regular ideals.

**2.4. The free abelian group functor.** For an abelian sheaf \(M\) on \(T\), let \(\mathbb Z[M]=\mathbb Z^{(M)}\) be its group ring, the free abelian sheaf on the underlying sheaf of sets of \(M\) with the product \([m][m']=[m+m']\); let \(I(M)\) be the kernel of the augmentation \(\mathbb Z[M]\to\mathbb Z\), \([m]\mapsto1\), and \(I^r(M)=I(M)^r\) its powers, \(r\geq1\). These are reduced functors of \(M\) that commute with restriction and with local inductive limits, as do the symmetric powers \(S^r=S^r_{\mathbb Z}\). The functor \(I\) is the reduced part of the free abelian group functor of Example 2.1 of the lesson on stable derived functors, so \(\mathbb Z^{\mathrm{st}}=I^{\mathrm{st}}\) (Conventions there). Stable derived functors are as in that lesson, for a site of \(T\).

**Lemma 2.5.** Let \(M\) be a flat abelian sheaf. Then \(I(M)\) is a weakly regular ideal of \(\mathbb Z[M]\), and \(m\mapsto[m]-1\) induces isomorphisms \(S^r(M)\to I^r(M)/I^{r+1}(M)\) for \(r\geq1\), natural in \(M\).

**Proof.** By Example 2.1 (3) of the lesson on stable derived functors, \(m\mapsto[m]-1\) induces an isomorphism \(M\to I(M)/I(M)^2\), with inverse \([m]-1\mapsto m\). First let \(M=\mathbb Z_U^s\) over an object \(U\), with basis \(e_1,\dots,e_s\), and put \(t_i=[e_i]\). Then \(\mathbb Z[M]\) is the ring of Laurent polynomials \(\mathbb Z_U[t_1^{\pm1},\dots,t_s^{\pm1}]\), and \(I(M)\) is generated by the \(u_i=t_i-1\), because \([\sum_ia_ie_i]-1=\prod_it_i^{a_i}-1\) lies in the ideal they generate. This ring is the localization of the polynomial ring \(\mathbb Z_U[u_1,\dots,u_s]\) at the multiplicative set generated by the \(1+u_i\). The variables form a regular sequence of the polynomial ring, so their Koszul complex has no homology in positive degrees [[Stacks, Tag 062F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-regular-koszul-regular)], and localization is exact; so \(u_1,\dots,u_s\) is a Koszul-regular sequence of \(\mathbb Z[M]\), and \(I(M)\) is weakly regular by Proposition 4.2 of the lesson on weakly regular ideals. In general, \(M\) is the local inductive limit of a local system of finite free modules \(M_\alpha\) (Theorem 3.2 of the lesson on non-additive functors), and \(\mathbb Z[M]\), \(I(M)\) are the local inductive limits of the \(\mathbb Z[M_\alpha]\), \(I(M_\alpha)\). The Tor algebra and the map \(\theta\) of Definition 2.4 of the lesson on weakly regular ideals are computed by a resolution built from free algebras on sheaves of sets, whose formation commutes with filtered colimits, as does homology. So \(\theta_{\mathbb Z[M],I(M)}\) is the local inductive limit of the isomorphisms \(\theta_{\mathbb Z[M_\alpha],I(M_\alpha)}\), hence an isomorphism, local inductive limits being exact; and \(I(M)/I(M)^2\cong M\) is flat. So \(I(M)\) is weakly regular, and Theorem 3.3 (1) there gives the isomorphisms \(S^r(I/I^2)\to I^r/I^{r+1}\), hence \(S^r(M)\to I^r(M)/I^{r+1}(M)\). \(\square\)

**Proposition 2.6.** Let \(X\) be an abelian sheaf on \(T\). Then \(H_iL(S^2)^{\mathrm{st}}(X)=0\) for \(i\leq1\), and there are isomorphisms, natural in \(X\),
\[
\begin{aligned}H_2L(S^2)^{\mathrm{st}}(X)&\cong X/2X,\\ H_3L(S^2)^{\mathrm{st}}(X)&\cong\ker(2\cdot1_X).\end{aligned}
\]

**Proof.** By Example 2.3 of the lesson on stable derived functors, \(L(S^2)^{\mathrm{st}}(X)\cong L(\Gamma^2)^{\mathrm{st}}(X)[2]\), and \(L(\Gamma^2)^{\mathrm{st}}(X)\) has no homology in negative degrees. So it suffices to show \(H_0L(\Gamma^2)^{\mathrm{st}}(X)\cong X/2X\) and \(H_1L(\Gamma^2)^{\mathrm{st}}(X)\cong\ker(2\cdot1_X)\). For a flat abelian sheaf \(P\) the sequence
\[
0\to S^2P\to\Gamma^2P\to P/2P\to0,
\]
with \(xy\mapsto xy\) and \(\gamma_2(x)\mapsto\bar x\), \(xy\mapsto0\), is exact and natural in \(P\): for \(P=\mathbb Z_U^s\) with basis \(e_i\), the first map sends the basis \(e_ie_j\), \(i<j\), and \(e_i^2\) of \(S^2P\) to \(e_ie_j\) and \(2\gamma_2(e_i)\), and \(\Gamma^2P\) has the basis \(e_ie_j\), \(i<j\), and \(\gamma_2(e_i)\); the general case follows by local inductive limits. The functor \(P\mapsto P/2P\) is additive, so its stabilization is \(P/2P\) in degree \(0\) (Corollary 3.7 of the lesson on stabilization). Stabilizing the sequence as in the proof of Example 2.3 of the lesson on stable derived functors gives a distinguished triangle whose first term \((S^2)^{\mathrm{st}}(P)\cong(\Gamma^2)^{\mathrm{st}}(P)[2]\) has no homology in degrees \(0\) and \(1\). So \(H_0(\Gamma^2)^{\mathrm{st}}(P)\cong P/2P\) and \(H_1(\Gamma^2)^{\mathrm{st}}(P)=0\), naturally in the flat \(P\). For an abelian sheaf \(X\), let \(K\) be the kernel of the counit \(\mathbb Z^{(X)}\to X\). The sections of \(\mathbb Z^{(X)}\) and of its subsheaf \(K\) are torsion-free abelian groups, so both sheaves are flat: tensoring with them preserves injective maps on sections, and sheafification is exact. Theorem 1.6 of the lesson on stable derived functors, applied to the triangle of \(0\to K\to\mathbb Z^{(X)}\to X\to0\), gives the exact sequence
\[
\begin{aligned}&0\to H_1L(\Gamma^2)^{\mathrm{st}}(X)\to K/2K\\&\quad\to\mathbb Z^{(X)}/2\mathbb Z^{(X)}\to H_0L(\Gamma^2)^{\mathrm{st}}(X)\to0,\end{aligned}
\]
natural in \(X\). Multiplication by \(2\) on \(0\to K\to\mathbb Z^{(X)}\to X\to0\), whose first two terms have no \(2\)-torsion, identifies the kernel of the middle map with \(\ker(2\cdot1_X)\) (snake lemma) and its cokernel with \(X/2X\). \(\square\)

**Theorem 2.7 (the stable homology of the free abelian group in low degrees).** Let \(X\) be an abelian sheaf on \(T\).

1. For \(i\geq1\), \(H_i\mathbb Z^{\mathrm{st}}(X)\otimes\mathbb Q=0\): every local section of \(H_i\mathbb Z^{\mathrm{st}}(X)\) is locally killed by a positive integer.
2. There are isomorphisms, natural in \(X\),
\[
\begin{aligned}H_2\mathbb Z^{\mathrm{st}}(X)&\cong X/2X,\\ H_3\mathbb Z^{\mathrm{st}}(X)&\cong\ker(2\cdot1_X).\end{aligned}
\]

With Example 2.1 of the lesson on stable derived functors, \(H_0\mathbb Z^{\mathrm{st}}(X)=X\) and \(H_1\mathbb Z^{\mathrm{st}}(X)=0\).

**Proof.** *Step 1: the filtration.* For flat \(M\), the sequences \(0\to I^{r+1}(M)\to I^r(M)\to S^r(M)\to0\), \(r\geq1\), are exact and natural (Lemma 2.5), with \(S^1\) the identity. Applied to flat simplicial modules and stabilized as in the proof of Example 2.3 of the lesson on stable derived functors, they give distinguished triangles
\[
\begin{aligned}&L(I^{r+1})^{\mathrm{st}}(X)\to L(I^r)^{\mathrm{st}}(X)\\&\quad\to L(S^r)^{\mathrm{st}}(X)\to\end{aligned}
\]
natural in \(X\) (Theorem 1.3 there), with \(L(S^1)^{\mathrm{st}}(X)=X\) (Corollary 3.7 of the lesson on stabilization). Moreover \(\mathbb Z^{\mathrm{st}}=I^{\mathrm{st}}\), and \(L\mathbb Z^{\mathrm{st}}(X)=\mathbb Z^{\mathrm{st}}(X)\) by Example 2.1 (1) there.

*Step 2: far in the filtration.* Let \(i\geq0\) and \(r\geq2i+2\). Then \(H_iL(I^r)^{\mathrm{st}}(X)=0\). Indeed, let \(X'\to X\) be a quasi-isomorphism from a flat simplicial module and \(n=i+1\). By Theorem 3.6 (2) of the lesson on stabilization, \(H_iL(I^r)^{\mathrm{st}}(X)\cong H_{2i+1}I^r(X'[n])\). The simplicial module \(Y=X'[n]\) has flat terms and \(Y_0=0\). Let \(R=\mathbb Z[Y]\), formed termwise, and \(J=I(Y)\subseteq R\). Every \(J_k\) is weakly regular (Lemma 2.5), and \(J_0=I(0)=0\), so \(\pi_0(J)=0\). By Theorem 2.1, \(J^r=I^r(Y)\) is \(r\)-connective, and \(2i+1<r\).

*Step 3: degrees \(2\) and \(3\).* For \(r\geq2\), Example 2.3 of the lesson on stable derived functors gives \(L(S^r)^{\mathrm{st}}(X)\cong L(\Gamma^r)^{\mathrm{st}}(X)[2(r-1)]\), so \(H_jL(S^r)^{\mathrm{st}}(X)=0\) for \(j<2(r-1)\), in particular for \(j\leq3\) when \(r\geq3\). By Step 2 with \(r=8\), \(H_jL(I^8)^{\mathrm{st}}(X)=0\) for \(j\leq3\). The exact sequences \(H_jL(I^{r+1})^{\mathrm{st}}(X)\to\) \(H_jL(I^r)^{\mathrm{st}}(X)\to\) \(H_jL(S^r)^{\mathrm{st}}(X)\), for \(r=7,6,\ldots,3\), give \(H_jL(I^3)^{\mathrm{st}}(X)=0\) for \(j\leq3\). The triangle for \(r=2\) then gives \(H_jL(I^2)^{\mathrm{st}}(X)\cong H_jL(S^2)^{\mathrm{st}}(X)\) for \(j\leq3\), the neighbouring groups \(H_j\) and \(H_{j-1}\) of \(L(I^3)^{\mathrm{st}}(X)\) vanishing. The triangle for \(r=1\) gives \(H_jL(I^2)^{\mathrm{st}}(X)\cong H_j\mathbb Z^{\mathrm{st}}(X)\) for \(j\geq2\), as \(X\) has no homology in degrees \(\geq1\). Proposition 2.6 gives (2).

*Step 4: rational vanishing.* For \(r\geq2\), \(H_jL(S^r)^{\mathrm{st}}(X)\otimes\mathbb Q=0\) for all \(j\). Indeed, the functor \(M\mapsto S^r(M)\otimes\mathbb Q\) is a natural direct summand of \(M\mapsto M^{\otimes r}\otimes\mathbb Q\), through the symmetrization \(\frac1{r!}\sum_\sigma\sigma\) and the projection \(M^{\otimes r}\to S^r(M)\). The functor \(M^{\otimes r}=T(M,M)\), with \(T(M_1,M_2)=M_1\otimes M_2^{\otimes(r-1)}\) vanishing when one variable is \(0\), has an acyclic stabilization (Example 5.2 of the lesson on stabilization). Tensoring with \(\mathbb Q\) is exact and commutes with the constructions of the stabilization, and so does passing to a natural direct summand; so \((S^r)^{\mathrm{st}}(X')\otimes\mathbb Q\) is acyclic for flat \(X'\). Now let \(i\geq1\) and \(r_0\geq2i+2\). By Step 2, \(H_iL(I^{r_0})^{\mathrm{st}}(X)=0\), and the triangles for \(r=r_0-1,\ldots,2\), tensored with \(\mathbb Q\), give \(H_iL(I^2)^{\mathrm{st}}(X)\otimes\mathbb Q=0\). The triangle for \(r=1\) gives an exact sequence \(H_iL(I^2)^{\mathrm{st}}(X)\otimes\mathbb Q\to\) \(H_i\mathbb Z^{\mathrm{st}}(X)\otimes\mathbb Q\to\) \(H_i(X)\otimes\mathbb Q=0\). So \(H_i\mathbb Z^{\mathrm{st}}(X)\otimes\mathbb Q=0\), which is (1): \(H_i\mathbb Z^{\mathrm{st}}(X)\otimes\mathbb Q\) is the colimit of the multiplications by \(1,2,3,\ldots\) on \(H_i\mathbb Z^{\mathrm{st}}(X)\). \(\square\)

The same filtration computes \(H_4\mathbb Z^{\mathrm{st}}(X)\) from \(L(S^2)^{\mathrm{st}}\), \(L(S^3)^{\mathrm{st}}\) and the connecting maps; for \(X=\mathbb Z\), \(H_4L(S^3)^{\mathrm{st}}(\mathbb Z)=H_0L(\Gamma^3)^{\mathrm{st}}(\mathbb Z)=\mathbb Z/3\), by Exercise 6.2 of the lesson on stabilization: the image of the cross-effect in \(\Gamma^3(\mathbb Z)=\mathbb Z\gamma_3(1)\) is generated by \(\gamma_1(1)\gamma_2(1)=3\gamma_3(1)\).

**Proposition 2.8 (spectra over the derived tensor product).** Let \(T\) be the topos of sets and \(A=\mathcal O=\mathbb Z\), so that, in the notation of the lesson on Ext groups as cohomology of spectral nerves, \(Q_{\mathcal O}=Q\), \(B:=B_A^{\mathcal O}=B_A=N\mathbb Z^{\mathrm{st}}(\mathbb Z)\), \(R:=R_{\mathcal O}=P_A=t_1(B)\) and \(\pi_{\mathcal O}=\pi\). Then
\[
\begin{aligned}\operatorname{Hom}_{D(R)}(R,R[4])&=0,\\ \operatorname{Hom}_{D(Q)}\bigl(\Psi(R),\Psi(R)[4]\bigr)&\cong\mathbb Z/2.\end{aligned}
\]
So the functor \(\Psi\colon D^b(R_{\mathcal O})\to D^b(Q_{\mathcal O})\) of Definition 3.2 there is not fully faithful, although its restriction to the complexes with cohomology in two consecutive degrees is (Proposition 3.4 there).

**Proof.** \(B\) is a differential graded ring in nonpositive degrees, with \(H^{-i}(B)=H_i\mathbb Z^{\mathrm{st}}(\mathbb Z)\): this is \(\mathbb Z\) for \(i=0\), \(0\) for \(i=1\) (Example 2.1 of the lesson on stable derived functors), \(\mathbb Z/2\) for \(i=2\) and \(0\) for \(i=3\) (Theorem 2.7). For a differential graded ring \(C\) and a module \(X\), \(\operatorname{Hom}_{D(C)}(C,X[n])=H^n(X)\): by Proposition 2.3 (2) of the lesson on differential graded modules it is \(H^n\operatorname{Hom}^\bullet_C(C,I)=H^n(I)\) for a K-injective \(I\) quasi-isomorphic to \(X\). As \(R\) lies in degrees \(-1\) and \(0\), \(\operatorname{Hom}_{D(R)}(R,R[4])=H^4(R)=0\).

By Definition 3.2 there, \(\Psi\) is \(\pi^*\) followed by a quasi-inverse of the equivalence \(\Phi_{\mathcal O}\colon\mathcal D_c\to\mathcal T\), and it is exact; so \(\operatorname{Hom}_{D(Q)}(\Psi(R),\Psi(R)[4])\cong\) \(\operatorname{Hom}_{D(B)}(\pi^*R,\pi^*R[4])\). Let \(\rho\colon B\to t_0(B)=H^0(B)=\mathbb Z\) be the projection of Proposition 1.3 of the lesson on differential graded modules, and \(\mathbb Z_0=\rho^*\mathbb Z\), the module \(\mathbb Z\) in degree \(0\). Since \(H^{-1}(R)=H^{-1}(B)=0\), the map \(R\to\tau^{\geq0}R=H^0(R)=\mathbb Z\) of Lemma 1.1 there is a quasi-isomorphism of \(R\)-modules, so \(\pi^*R\cong\mathbb Z_0\) in \(D(B)\). It remains to show \(\operatorname{Hom}_{D(B)}(\mathbb Z_0,\mathbb Z_0[4])\cong\mathbb Z/2\).

Let \(K=\ker\rho\). The exact sequence \(0\to K\to B\to\mathbb Z_0\to0\) gives a distinguished triangle [Stacks, Tag 0FTB], and \(\operatorname{Hom}_{D(B)}(B[1],\mathbb Z_0[4])=H^3(\mathbb Z_0)=0\), \(\operatorname{Hom}_{D(B)}(B,\mathbb Z_0[4])=H^4(\mathbb Z_0)=0\). So
\[
\begin{aligned}&\operatorname{Hom}_{D(B)}(\mathbb Z_0,\mathbb Z_0[4])\\&\quad\cong\operatorname{Hom}_{D(B)}(K,\mathbb Z_0[3]).\end{aligned}
\]
The long exact cohomology sequence gives \(H^i(K)=H^i(B)\) for \(i\leq-1\) and \(H^i(K)=0\) for \(i\geq0\); so \(K\) has cohomology \(\mathbb Z/2\) in degree \(-2\), and \(0\) in degrees \(-3\), \(-1\) and above. The submodule \(\tau^{\leq-4}K\) gives the exact sequence \(0\to\tau^{\leq-4}K\to K\to K/\tau^{\leq-4}K\to0\), and the quotient maps quasi-isomorphically to \(\tau^{\geq-3}K\): both have the cohomology of \(K\) in degrees \(\geq-3\) and none below. By Proposition 1.2 (1) of the lesson on differential graded modules, \(\operatorname{Hom}(\tau^{\leq-4}K,\mathbb Z_0[3])=0\) and \(\operatorname{Hom}(\tau^{\leq-4}K[1],\mathbb Z_0[3])=0\), the first object having no cohomology above \(-4\), resp. \(-5\), and \(\mathbb Z_0[3]\) none at or below. Hence
\[
\begin{aligned}&\operatorname{Hom}_{D(B)}(K,\mathbb Z_0[3])\\&\quad\cong\operatorname{Hom}_{D(B)}(\tau^{\geq-3}K,\mathbb Z_0[3]).\end{aligned}
\]
As \(H^{-3}(K)=0\), the quotient map \(\tau^{\geq-3}K\to\tau^{\geq-2}K\) is a quasi-isomorphism, and as \(H^i(K)=0\) for \(i>-2\), so is the inclusion \(\tau^{\leq-2}\tau^{\geq-2}K\to\tau^{\geq-2}K\). The module \(\tau^{\leq-2}\tau^{\geq-2}K\) is \(H^{-2}(K)=\mathbb Z/2\) in degree \(-2\), on which \(B\) acts through \(\rho\) (Proposition 1.3 there, with \(n=0\)). So \(\tau^{\geq-3}K\cong(\rho^*\mathbb Z/2)[2]\), and
\[
\begin{aligned}&\operatorname{Hom}_{D(B)}(\mathbb Z_0,\mathbb Z_0[4])\\&\quad\cong\operatorname{Hom}_{D(B)}(\rho^*\mathbb Z/2,\mathbb Z_0[1]).\end{aligned}
\]
Both objects have cohomology in \([-1,0]\). By Proposition 1.3 there, with \(n=1\), restriction along \(\pi\colon B\to t_1(B)=R\) induces an equivalence between the objects of \(D(R)\) and of \(D(B)\) with cohomology in \([-1,0]\); and the quasi-isomorphism of rings \(w\colon R\to\mathbb Z\) (Proposition 2.4 (1) of the lesson on the stable ring) induces an equivalence \(D(\mathbb Z)\to D(R)\) (Proposition 2.5 (3) of the lesson on differential graded modules). These carry \(\mathbb Z/2\) and \(\mathbb Z[1]\) to \(\rho^*\mathbb Z/2\) and \(\mathbb Z_0[1]\), as \(\rho\) is \(w\pi\) followed by the identity of \(\mathbb Z\). So the group is \(\operatorname{Hom}_{D(\mathbb Z)}(\mathbb Z/2,\mathbb Z[1])=\) \(\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/2,\mathbb Z)=\mathbb Z/2\). \(\square\)

The proof identifies the extra group with \(\operatorname{Ext}^1_{\mathbb Z}\bigl(H_2\mathbb Z^{\mathrm{st}}(\mathbb Z),H_0\mathbb Z^{\mathrm{st}}(\mathbb Z)\bigr)\): it comes from the first homology group of the stabilization above the two degrees that \(t_1\) keeps.

## 3. Exercises

**Exercise 3.1.** In the situation of Theorem 2.1, show that \(\pi_1(J)\to\pi_1(J/J^2)\) is an isomorphism and that \(\pi_0(J/J^2)=0\).

**Exercise 3.2.** In the situation of Corollary 2.2 with \(B=A/I\), show that \(\pi_1(J/J^2)\cong I/I^2\).

**Exercise 3.3.** Let \(B\) be a ring of \(T\), \(F\) a flat \(B\)-module, \(\Sigma F\) the simplicial module corresponding to \(F\) placed in degree \(1\), \(R=S_B(\Sigma F)\) and \(J=S^+_B(\Sigma F)\). Show that \(R\) and \(J\) satisfy the hypotheses of Theorem 2.1, compute \(\pi_\bullet(J^m)\), and conclude that the bound of the theorem is attained when \(\Lambda^m_BF\neq0\).

**Exercise 3.4.** Let \(T\) be the topos of sets and \(n\geq1\). Compute \(H_i\mathbb Z^{\mathrm{st}}(\mathbb Z/n)\) for \(i\leq3\), and show that \(H_i\mathbb Z^{\mathrm{st}}(\mathbb Q)=0\) for \(1\leq i\leq3\).

## 4. Complete solutions

**Solution 3.1.** By Theorem 2.1, \(J^2\) is \(2\)-connective, so the exact sequence \(0\to J^2\to J\to J/J^2\to0\) gives \(\pi_1(J)\cong\pi_1(J/J^2)\) and \(\pi_0(J/J^2)=\pi_0(J)=0\).

**Solution 3.2.** The exact sequence \(0\to J\to Q\to B\to0\), with \(B\) constant, gives \(\pi_1(J)\cong\pi_1(Q)=\operatorname{Tor}^A_1(B,B)\), and this is \(I/I^2\) by the conormal isomorphism of the lesson on weakly regular ideals (2.3 there). By Exercise 3.1, \(\pi_1(J/J^2)\cong\pi_1(J)\).

**Solution 3.3.** In each degree \(R_n=S_B((\Sigma F)_n)\) with \((\Sigma F)_n\) a finite sum of copies of \(F\), so \(J_n\) is weakly regular by Proposition 4.1 of the lesson on weakly regular ideals. Here \(J^m=S^{\geq m}_B(\Sigma F)\). As in the proof of that proposition, \(\pi_q(S^k_B(\Sigma F))\) is \(\Lambda^k_BF\) for \(q=k\) and \(0\) otherwise. So \(\pi_0(J)=0\), and \(\pi_q(J^m)=\bigoplus_{k\geq m}\pi_q(S^k_B(\Sigma F))\) is \(\Lambda^q_BF\) for \(q\geq m\) and \(0\) for \(q<m\), as Theorem 2.1 requires. In degree \(m\) it is \(\Lambda^m_BF\), so \(J^m\) is not \((m+1)\)-connective when \(\Lambda^m_BF\neq0\).

**Solution 3.4.** By Theorem 2.7 and Example 2.1 of the lesson on stable derived functors, \(H_0\mathbb Z^{\mathrm{st}}(\mathbb Z/n)=\mathbb Z/n\), \(H_1=0\), \(H_2=(\mathbb Z/n)/2(\mathbb Z/n)\) and \(H_3=\ker(2\cdot1_{\mathbb Z/n})\). Both are \(0\) for odd \(n\), since \(2\) is then invertible on \(\mathbb Z/n\), and \(\mathbb Z/2\) for even \(n\), generated by the class of \(1\), resp. by \(n/2\). For \(\mathbb Q\), \(H_1=0\), and \(\mathbb Q/2\mathbb Q=0=\ker(2\cdot1_{\mathbb Q})\) give \(H_2=H_3=0\).

## Sources

The convergence theorem is due to Quillen for simplicial rings, in Section 8 of his MIT notes on the homology of commutative rings (1968), [available from Haynes Miller's page](https://math.mit.edu/~hrm/manuscripts/quillen-commutative-algebra.pdf); its use for rings of a topos is due to Illusie, in his work on the cotangent complex. Quillen obtains the connectivity of Proposition 1.4 from derived symmetric powers over simplicial rings; the proof given here reduces to the constant ring \(\pi_0(B)\) through Lemma 1.3. The stable homology of Eilenberg–MacLane spaces was determined by H. Cartan, Séminaire Henri Cartan 7 (1954–1955), *Algèbres d'Eilenberg–MacLane et homotopie* ([Numdam](https://www.numdam.org/issues/SHC_1954-1955__7_1/)); Theorem 2.7 derives its values in degrees \(2\) and \(3\), and its rational vanishing, from the filtration of the group ring by the powers of its augmentation ideal and the convergence theorem.
