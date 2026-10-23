# The fundamental spectral sequence

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(A\) be a ring of a topos and \(B\) an \(A\)-algebra whose multiplication \(B\otimes_AB\to B\) is an isomorphism, for example a quotient \(B=A/I\). The simplicial ring \(Q=P\otimes_AB\) built from the standard resolution \(P\) of \(B\) computes \(\operatorname{Tor}^A_\bullet(B,B)\). Its augmentation ideal \(J\) satisfies \(J/J^2=L_{B/A}\), the cotangent complex, and \(J^q/J^{q+1}=S^q_B(L_{B/A})\). Filtering \(Q\) by the powers of \(J\) gives the *fundamental spectral sequence*
\[
\begin{aligned}&E^2_{p,q}=H_{p+q}\bigl(S^q_BL_{B/A}\bigr)\\&\quad\Longrightarrow\operatorname{Tor}^A_{p+q}(B,B),\end{aligned}
\]
a convergent spectral sequence of bigraded algebras. For a quotient \(B=A/I\) the cotangent complex decides weak regularity: \(I\) is weakly regular if and only if \(I/I^2\) is flat and \(L_{B/A}\cong(I/I^2)[1]\). The lesson proves:

- \(J/J^2\cong L_{B/A}\) and \(J^q/J^{q+1}\cong S^q_B(L_{B/A})\) as simplicial modules; for \(B=A/I\), \(H_0(L_{B/A})=0\) and \(H_1(L_{B/A})\cong I/I^2\), by an isomorphism that agrees with the one given by the naive cotangent complex;
- for a simplicial module \(L\) with flat terms and \(\pi_0(L)=0\) over a ring, products of classes of degree one give \(\Lambda^q(\pi_1L)\cong\pi_q(S^qL)\), and \(S^qL\) has the homotopy of \(S^q(\pi_1(L)[1])\) in a range of degrees fixed by the vanishing of the \(\pi_i(L)\);
- the spectral sequence of a differential graded ring with a multiplicative filtration is a spectral sequence of algebras; the fundamental spectral sequence, its convergence, and \(\theta\) as its edge homomorphism;
- for \(B=A/I\), the following are equivalent: \(I\) is weakly regular; the André–Quillen homology \(D_q(B/A,M)\) vanishes for \(q\geq2\) and every \(B\)-module \(M\); \(I/I^2\) is flat and \(L_{B/A}\cong(I/I^2)[1]\). In particular \(L_{B/A}\cong(I/I^2)[1]\) for a Koszul-regular ideal.

**Prerequisites.** [*Weakly regular ideals*](weakly-regular-ideals.md) (Lemma 1.1, Section 2, Propositions 4.1 and 4.2, Exercises 5.2 and 5.3); [*Connectivity of powers of simplicial ideals*](connectivity-of-powers-of-simplicial-ideals.md) (Lemmas 1.1, 1.2 and 1.5, Proposition 1.4, Corollary 2.2, Exercises 3.1 and 3.2); [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md) (Proposition 2.1); [*Derived tensor products of simplicial modules*](derived-tensor-products-of-simplicial-modules.md) (Proposition 3.2); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Sections 2 and 5, Proposition 2.2, Lemma 4.1, Theorem 4.4); [*Koszul complexes and the shift formulas*](koszul-complexes-and-the-shift-formulas.md) (Theorem 3.2, Proposition 3.4); [*Filtered and graded powers of complexes*](filtered-and-graded-powers-of-complexes.md) (Proposition 1.7); [*The cotangent complex*](course:AG-HP/the-cotangent-complex#2-independence-of-the-resolution) (Theorems 1.1 and 1.2, the definition in Section 2, Theorem 6.1 with formula (6.5), Lemma 7.1, Section 10). From the AI-integrated Stacks project: the cotangent complex of a map of sheaves of rings [[Stacks, Tag 08SS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-definition-cotangent-complex-morphism-sheaves-rings)]; the spectral sequence of a filtered complex [[Tag 012M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-spectral-sequence-filtered-complex)] and its convergence for finite filtrations [[Tag 012W](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-biregular-ss-converges)].

## Conventions

\(T\) is a topos and rings are commutative. For a simplicial module \(E\), \(H_n(E)=\pi_n(E)\) is the homology of its normalized complex \(NE\), and \(E\) is *\(k\)-connective* if \(H_i(E)=0\) for \(i<k\). Exterior and symmetric powers and tensor products of simplicial modules are formed degreewise. For a module \(N\) over a ring \(B\), \(\Sigma N\) is the simplicial module that corresponds to \(N\) placed in homological degree \(1\) under the Dold–Kan correspondence (Theorem 1.2 of *The cotangent complex*); its normalized complex is \(N[1]\). In Sections 1, 3 and 4, \(A\) is a ring of \(T\), \(B\) an \(A\)-algebra with \(B\otimes_AB\xrightarrow{\sim}B\), \(P\to B\) the resolution of Section 2 of the lesson on weakly regular ideals (the standard resolution), \(Q=P\otimes_AB\), \(\varepsilon\colon Q\to B\) the augmentation and \(J=\ker\varepsilon\). The cotangent complex \(L_{B/A}\) is the simplicial \(B\)-module \(\Omega_{P/A}\otimes_PB\) [Tag 08SS], or its normalized complex, with chain degree \(n\) in cohomological degree \(-n\) (Section 2 of *The cotangent complex*, in the sheaf form of its Section 10). For a \(B\)-module \(M\), the *André–Quillen homology* is \(D_q(B/A,M)=H_q(L_{B/A}\otimes_BM)\); since \(L_{B/A}\) has flat terms, \(L_{B/A}\otimes_BM\) represents \(L_{B/A}\otimes^\ell_BM\) (Proposition 3.2 (1) of the lesson on derived tensor products).

## 1. The augmentation ideal of the Tor resolution

**Proposition 1.1.**

1. The maps \(J_n\to\Omega_{Q_n/B}\otimes_{Q_n}B=\Omega_{P_n/A}\otimes_{P_n}B\), \(f\mapsto df\otimes1\), induce an isomorphism of simplicial \(B\)-modules \(J/J^2\cong L_{B/A}\).
2. The multiplication maps \(S^q_B(J/J^2)\to J^q/J^{q+1}\) are isomorphisms of simplicial \(B\)-modules.
3. \(\pi_0(L_{B/A})=0\), and the maps \(\pi_1(J)\to\pi_1(J/J^2)\) and \(\pi_1(J)\to\pi_1(Q)\) are isomorphisms. For \(B=A/I\) let
\[
\partial_L\colon H_1(L_{B/A})\to I/I^2
\]
be the composite of their inverses with the conormal isomorphism \(\partial\colon\pi_1(Q)=\operatorname{Tor}^A_1(B,B)\to I/I^2\) of the lesson on weakly regular ideals (2.3 there); it is an isomorphism.

**Proof.** (1) In degree \(n\), \(Q_n=B[X_n]\), and \(\varepsilon\) maps a variable \(x\) to its image \(\varepsilon(x)\) in \(B\). The derivation \(d\colon Q_n\to\Omega_{Q_n/B}\), followed by \(\varepsilon\), kills \(J_n^2\), because \(d(fg)=f\,dg+g\,df\); so it induces a map \(J_n/J_n^2\to\Omega_{Q_n/B}\otimes_{Q_n}B\). Both sides are free \(B\)-modules, on the classes of the \(x-\varepsilon(x)\) and on the \(dx\), and the map matches these bases; so it is an isomorphism. Moreover \(\Omega_{Q_n/B}=\Omega_{P_n/A}\otimes_AB\), so \(\Omega_{Q_n/B}\otimes_{Q_n}B=\Omega_{P_n/A}\otimes_{P_n}B\). The face and degeneracy maps of \(Q\) are homomorphisms of augmented \(B\)-algebras, and the map is natural in these; so the isomorphisms form an isomorphism of simplicial modules.

(2) In each degree, after the change of variables \(x\mapsto x-\varepsilon(x)\), \(Q_n\) is the symmetric algebra of a free \(B\)-module with its ideal of variables, for which the multiplication maps are isomorphisms; they are natural, hence simplicial.

(3) By Corollary 2.2 of the lesson on connectivity of powers of simplicial ideals, the hypotheses of its Theorem 2.1 hold for \(Q\) and \(J\). Exercise 3.1 there gives \(\pi_0(J/J^2)=0\) and the first isomorphism; the second follows from the long exact sequence of \(0\to J\to Q\to B\to0\), \(B\) being constant, as in Solution 3.2 there. \(\square\)

**Proposition 1.2.** Let \(B=A/I\). The isomorphism \(\partial_L\colon H_1(L_{B/A})\to I/I^2\) of Proposition 1.1 (3) is the isomorphism \(H^{-1}(L_{B/A})\cong I/I^2\) of Theorem 6.1 of *The cotangent complex*, given by the naive cotangent complex.

**Proof.** Homology classes of a simplicial module, and the connecting maps of short exact sequences of simplicial modules, may be computed on the unnormalized complexes, whose differential from degree \(1\) to degree \(0\) is \(d_0-d_1\): the normalized complex is a natural direct summand with acyclic complement (Theorem 1.1 of *The cotangent complex*). Both maps are maps of sheaves, so it suffices to compare them on a local section \(\xi\) of \(H_1(L_{B/A})\) over an object \(U\) of \(T\). By Proposition 1.1, after replacing \(U\) by the members of a covering, \(\xi\) is the image of the class of a cycle \(w\) of \(J_1\) over \(U\), and \(w\) is the image of a section \(y\) of \(P_1\) over \(U\), as \(P_1\to Q_1=P_1\otimes_AB\) is surjective. Under \(\Omega_{Q_1/B}\otimes_{Q_1}B=\Omega_{P_1/A}\otimes_{P_1}B\) (Proposition 1.1 (1)), \(\xi\) is the class of \(dy\otimes1\). Put \(g=d_0y-d_1y\), a section of \(P_0\). Its image in \(Q_0\) is \(d_0w-d_1w=0\), so \(g\) is a section of \(P_0\otimes_AI=IP_0\), \(P_0\) being flat over \(A\). Locally write \(g=\sum_ki_kp_k\) with \(i_k\) in \(I\) and \(p_k\) in \(P_0\), and choose sections \(a_k\) of \(A\) with the same images in \(B\) as the \(p_k\).

By definition, \(\partial_L(\xi)\) is the image of the class of \(w\) in \(\pi_1(Q)\) under the connecting map of \(0\to P\otimes_AI\to P\to Q\to0\): lift \(w\) to \(y\), apply the differential, and take the class of \(g\) in \(\pi_0(P\otimes_AI)=B\otimes_AI=I/I^2\), the map \(P_0\otimes_AI\to B\otimes_AI\) being induced by the augmentation. So \(\partial_L(\xi)=\sum_k\overline{a_ki_k}\).

Theorem 6.1 there identifies \(H^{-1}(L_{B/A})\) with \(H^{-1}\) of the naive complex of the presentation \(P_0\to B\), whose kernel we call \(I_0\), by its formula (6.5), which sends \(\xi\) to the class of \(g\) in \(I_0/I_0^2\). It identifies the latter with \(H^{-1}\) of the naive complex of the presentation of \(B\) by \(A\) itself, \(I/I^2\), through the map of presentations \(A\to P_0\), which sends the class of a section of \(I\) to the class of the same section in \(I_0/I_0^2\). Since \(p_k-a_k\) lies in \(I_0\), \(i_kp_k-a_ki_k=i_k(p_k-a_k)\) lies in \(I_0^2\), and the class of \(g\) in \(I_0/I_0^2\) is that of \(\sum_ka_ki_k\), a section of \(I\). So this identification also sends \(\xi\) to \(\sum_k\overline{a_ki_k}\). \(\square\)

## 2. Symmetric powers of 1-connective simplicial modules

In this section \(B\) is a ring of \(T\), regarded as a constant simplicial ring.

**Lemma 2.1.** For a simplicial \(B\)-module \(X\) and \(k\geq0\), \(\pi_0(\Lambda^k_BX)=\Lambda^k_B(\pi_0X)\).

**Proof.** For a simplicial module \(Y\), \(\pi_0(Y)\) is the cokernel of \(d_0-d_1\colon Y_1\to Y_0\). Let \(X'=(d_0-d_1)(X_1)\). The kernel of \(\Lambda^k_BX_0\to\Lambda^k_B(X_0/X')\) is generated by the products \(x'\wedge y_2\wedge\cdots\wedge y_k\) with \(x'\in X'\), and
\[
\begin{aligned}&(d_0-d_1)(x\wedge s_0y_2\wedge\cdots\wedge s_0y_k)\\&\quad=(d_0x-d_1x)\wedge y_2\wedge\cdots\wedge y_k,\end{aligned}
\]
since \(d_0s_0=d_1s_0=1\). So the kernel lies in the image of \(d_0-d_1\) on \(\Lambda^k_BX_1\). Conversely, for \(x_1,\dots,x_k\in X_1\),
\[
\begin{aligned}&d_0x_1\wedge\cdots\wedge d_0x_k\\&\quad-d_1x_1\wedge\cdots\wedge d_1x_k\\&\quad=\sum_{i=1}^kd_1x_1\wedge\cdots\wedge d_1x_{i-1}\\&\qquad\wedge(d_0x_i-d_1x_i)\\&\qquad\wedge d_0x_{i+1}\wedge\cdots\wedge d_0x_k\end{aligned}
\]
lies in that kernel. \(\square\)

**Lemma 2.2.** Let \(V\) be a simplicial \(B\)-module with flat terms that is \(c\)-connective, \(c\geq1\). For \(p\geq1\), \(S^p_BV\) is \((c+p-1)\)-connective.

**Proof.** The terms of \(NV\) are flat. The complex \(N_cV\to N_{c-1}V\to\cdots\to N_0V\to0\) is exact except at \(N_cV\), so by ascending induction its cycles \(Z_i\) are flat for \(i\leq c\), each being the kernel of a surjection \(N_iV\to Z_{i-1}\) of flat modules. Hence \(NV\) is quasi-isomorphic to its subcomplex \(\cdots\to N_{c+1}V\to Z_c\to0\), which is \(E[c]\) for a complex \(E\) of flat modules in cohomological degrees \(\leq0\). By Theorem 4.4 and Section 2 of the lesson on non-additive functors, the normalized complex of \(S^p_BV\) represents \(LS^p(E[c])\). By Theorem 3.2 of the lesson on Koszul complexes, applied to \(E[c-1]\), this is \(L\Lambda^p(E[c-1])[p]\), and \(L\Lambda^p(E[c-1])=\Lambda^p(E[c-1])\) vanishes in the degrees \(>-(c-1)\) (Proposition 2.2 of the lesson on non-additive functors). \(\square\)

**Proposition 2.3.** Let \(L\) be a simplicial \(B\)-module with flat terms and \(\pi_0(L)=0\), and \(k\geq1\).

1. \(S^k_BL\) is \(k\)-connective.
2. The product map \(\pi_1(L)^{\otimes k}\to\pi_k(S^k_BL)\) of the simplicial ring \(S_B(L)\) factors through an isomorphism \(\Lambda^k_B(\pi_1L)\to\pi_k(S^k_BL)\).

**Proof.** (1) is Lemma 2.2 with \(c=1\). (2) As in the proof of Lemma 2.2, \(NL\cong E[1]\) in \(D(B)\), with \(E\) a complex of flat modules in degrees \(\leq0\) and \(H^0(E)=\pi_1(L)\). The normalized complex of \(S^k_BL\) represents \(LS^k(E[1])\), and Theorem 3.2 of the lesson on Koszul complexes gives the shift isomorphism \(LS^k(E[1])\cong L\Lambda^k(E)[k]\). Here \(L\Lambda^k(E)=\Lambda^k(E)\), the normalized complex of \(\Lambda^k(\Gamma E)\) with \(\Gamma E\) the simplicial module of \(E\), so by Lemma 2.1
\[
\begin{aligned}&H^0(L\Lambda^kE)=\pi_0(\Lambda^k\Gamma E)\\&\quad=\Lambda^k(\pi_0\Gamma E)=\Lambda^k_B(\pi_1L).\end{aligned}
\]
Let \(\sigma_k\colon\Lambda^k_B(\pi_1L)\to\pi_k(S^k_BL)\) be the inverse of the isomorphism induced on \(H_k\) by the shift isomorphism. The product of \(\pi_\bullet(S_BL)\) on \(\pi_a\otimes\pi_b\) is induced by the product \(S^a(NL)\otimes S^b(NL)\to S^{a+b}(NL)\) of Section 5 of the lesson on non-additive functors, because for complexes in nonpositive cohomological degrees the map (5.1) there is the shuffle map. By Proposition 3.4 of the lesson on Koszul complexes, for \(a,b\geq1\) the shift isomorphisms carry this product to the product of \(L\Lambda(E)\), shifted and composed with \(\tau\). On \(H^0\) the product of \(L\Lambda(E)\) is the exterior product of \(\Lambda_B(\pi_1L)\), since \(\pi_0\) of the simplicial ring \(\Lambda(\Gamma E)\) is \(\Lambda(\pi_0\Gamma E)\) with its product, and \(\tau\) multiplies \(x\otimes y\) by \((-1)^{ab}\) for \(x\) of degree \(-a\) in \(L\Lambda^a(E)[a]\). So \(\sigma_a(x)\sigma_b(y)=(-1)^{ab}\sigma_{a+b}(x\wedge y)\), and by induction on \(k\)
\[
\begin{aligned}&\sigma_1(y_1)\cdots\sigma_1(y_k)\\&\quad=(-1)^{k(k-1)/2}\sigma_k(y_1\wedge\cdots\wedge y_k).\end{aligned}
\]
As \(\sigma_1\) is an automorphism of \(\pi_1(L)\), the product map is
\[
\begin{aligned}&x_1\otimes\cdots\otimes x_k\\&\quad\mapsto(-1)^{k(k-1)/2}\\&\qquad\cdot\sigma_k(\sigma_1^{-1}x_1\wedge\cdots\wedge\sigma_1^{-1}x_k);\end{aligned}
\]
it factors through the isomorphism \((-1)^{k(k-1)/2}\sigma_k\circ\Lambda^k(\sigma_1^{-1})\). \(\square\)

**Proposition 2.4.** Let \(L\) be a simplicial \(B\)-module with flat terms, \(\pi_0(L)=0\) and \(N=\pi_1(L)\) flat.

1. Let \(n\geq1\) and suppose \(\pi_i(L)=0\) for \(2\leq i\leq n\). Then for \(k\geq2\), \(\pi_j(S^k_BL)=0\) for every \(j\leq n+k-2\) with \(j\neq k\).
2. If \(\pi_i(L)=0\) for every \(i\geq2\), then \(\pi_j(S^k_BL)=0\) for every \(k\geq1\) and \(j\neq k\).

**Proof.** Let \(Z_1\) be the kernel of \(N_1L\to N_0L\), which is surjective, and \(B_1\) the image of \(N_2L\to N_1L\). The modules \(Z_1\) and \(N=Z_1/B_1\) are flat, so \(B_1\) is flat. Let \(N'\) be the subcomplex \(\cdots\to N_2L\to Z_1\to0\) of \(NL\), quasi-isomorphic to \(NL\), and \(K\) its subcomplex \(\cdots\to N_3L\to N_2L\to B_1\to0\). Then \(N'/K=N[1]\), and the sequence of complexes of flat modules \(0\to K\to N'\to N[1]\to0\) is exact. The homology of \(K\) is \(0\) in degree \(1\) and \(\pi_i(L)\) in degrees \(i\geq2\). Applying the Dold–Kan functor \(\Gamma\) gives an exact sequence \(0\to\Gamma K\to\Gamma N'\to\Sigma N\to0\) of simplicial modules with flat terms, and \(\Gamma N'\to L\) is a quasi-isomorphism, so \(S^k(\Gamma N')\to S^k(L)\) is one (Lemma 4.1 of the lesson on non-additive functors).

By Proposition 1.7 of the lesson on filtered and graded powers, applied in each degree, the kernel \(F^1\) of \(S^k(\Gamma N')\to S^k(\Sigma N)\) has a finite filtration by simplicial submodules with quotients \(S^{k-p}(\Sigma N)\otimes S^p(\Gamma K)\), \(1\leq p\leq k\). In case (1), \(\Gamma K\) is \((n+1)\)-connective, so \(S^p(\Gamma K)\) is \((n+p)\)-connective by Lemma 2.2, \(S^{k-p}(\Sigma N)\) is \((k-p)\)-connective, and the tensor product, which computes the derived one, is \((n+k)\)-connective (Lemma 1.1 of the lesson on connectivity of powers of simplicial ideals). By the long exact sequences of the filtration, \(F^1\) is \((n+k)\)-connective. So \(\pi_j(S^kL)\to\pi_j(S^k\Sigma N)\) is an isomorphism for \(j\leq n+k-2\). Finally \(\pi_j(S^k\Sigma N)\) is \(\Lambda^k_BN\) for \(j=k\) and \(0\) otherwise, by the shift isomorphism \(LS^k(N[1])\cong\Lambda^k_B(N)[k]\) (Theorem 3.2 of the lesson on Koszul complexes). In case (2), \(K\) is acyclic and \(\Gamma K\) is \(m\)-connective for every \(m\), so the map is an isomorphism in all degrees. \(\square\)

## 3. The fundamental spectral sequence

**Lemma 3.1.** Let \(C\) be a differential graded ring, with differential \(d\) of degree \(-1\) satisfying \(d(xy)=(dx)y+(-1)^{|x|}x\,dy\), and let \(C=F^0\supseteq F^1\supseteq\cdots\supseteq F^m=0\) be a filtration by subcomplexes with \(F^wF^{w'}\subseteq F^{w+w'}\). Then the spectral sequence of the filtered complex [Tag 012M] is a spectral sequence of bigraded rings: each page is a bigraded ring, each differential is a derivation, the product of each page is induced by that of the page before it, and the limit page is the graded ring of \(H(C)\) for the induced filtration.

**Proof.** Put \(Z^w_r=\{x\in F^w:dx\in F^{w+r}\}\), with \(F^w=C\) for \(w\leq0\). The \(r\)-th page in weight \(w\) of [Tag 012M] is \(E^w_r=Z^w_r/(Z^{w+1}_{r-1}+dZ^{w-r+1}_{r-1})\), with \(d_r[x]=[dx]\): indeed the denominator of [Tag 012M] is \(F^w\cap dF^{w-r+1}=dZ^{w-r+1}_{r-1}\) plus the part \(Z^{w+1}_{r-1}=Z^w_r\cap F^{w+1}\) of \(F^{w+1}\). By the Leibniz rule \(Z^w_rZ^{w'}_r\subseteq Z^{w+w'}_r\). For \(x\in Z^w_r\) and \(y\in Z^{w'+1}_{r-1}\), \(xy\in F^{w+w'+1}\) and \(d(xy)\in F^{w+w'+r}\), so \(xy\in Z^{w+w'+1}_{r-1}\). For \(x\in Z^w_r\) and \(z\in Z^{w'-r+1}_{r-1}\),
\[
x\,dz=\pm\bigl(d(xz)-(dx)z\bigr),
\]
where \(xz\in Z^{w+w'-r+1}_{r-1}\), because \(d(xz)\in F^{w+w'}\), and \((dx)z\in Z^{w+w'+1}_{r-1}\). The same holds with the factors exchanged. So the product passes to \(E_r\), and \(d_r\) is a derivation by the Leibniz rule. The identification of \(E_{r+1}\) with the homology of \((E_r,d_r)\) is induced by the inclusions \(Z^w_{r+1}\subseteq Z^w_r\), so it respects the products. For \(r>m\), \(Z^w_r\) and \(Z^{w+1}_{r-1}\) consist of the cycles of \(F^w\) and of \(F^{w+1}\), \(dZ^{w-r+1}_{r-1}\) of the boundaries lying in \(F^w\), and \(E^w_r\) is the quotient of the image of \(H(F^w)\) in \(H(C)\) by that of \(H(F^{w+1})\), with the product of \(H(C)\). \(\square\)

**Theorem 3.2 (the fundamental spectral sequence).** For \(m\geq1\), the filtration of \(Q/J^m\) by the \(J^q/J^m\) gives a convergent first-quadrant spectral sequence \(E(m)\) of bigraded \(B\)-algebras, natural in \(A\to B\),
\[
\begin{aligned}&E(m)^2_{p,q}=H_{p+q}\bigl(S^q_BL_{B/A}\bigr)\ (q<m)\\&\quad\Longrightarrow\pi_{p+q}(Q/J^m),\end{aligned}
\]
with \(E(m)^2_{p,q}=0\) for \(q\geq m\) and differentials \(d^r\colon E^r_{p,q}\to E^r_{p-r,q+r-1}\), \(r\geq2\). Let \(n\geq0\) and \(m\geq2n+1\). In total degree \(n\), \(E(m)^2_{p,q}=H_n(S^q_BL_{B/A})\) for every \(q\); the projections \(Q/J^{m'}\to Q/J^m\), \(m'\geq m\), induce isomorphisms of all the pages in total degree \(n\); the pages from \(E^{n+2}\) on are equal to \(E^\infty\) there; and the abutment is \(\operatorname{Tor}^A_n(B,B)\), filtered by the images \(F^q\) of the \(\pi_n(J^q)\), with \(F^0=\operatorname{Tor}^A_n(B,B)\), \(F^{n+1}=0\) and \(E^\infty_{p,q}=F^q/F^{q+1}\). This is the *fundamental spectral sequence*.

**Proof.** The normalized complex of \(Q/J^m\) is a differential graded ring (Proposition 2.1 of the lesson on simplicial rings and modules) with the finite multiplicative filtration by the normalized complexes of the \(J^q/J^m\), whose graded pieces are the normalized complexes of the \(S^q_BL_{B/A}\), \(q<m\) (Proposition 1.1). Lemma 3.1 and [Tag 012W] give a convergent spectral sequence of bigraded rings, natural in \(A\to B\) through the standard resolution, which we index by the weight \(q\) and the total degree \(p+q\), starting the numbering of the pages at \(2\): its differentials lower the total degree by one and raise the weight by \(r-1\). By Propositions 1.1 (3) and 2.3 (1), \(S^q_BL_{B/A}\) is \(q\)-connective, so \(E(m)^2_{p,q}=0\) for \(p<0\).

In total degree \(t\), a term of weight \(q\geq m\) would have \(p=t-q<0\) if \(t<m\). So the projections induce isomorphisms of the second pages in the total degrees \(\leq m-1\), and a map of spectral sequences that is an isomorphism on a page in the total degrees \(\leq s\) is one on the next page in the total degrees \(\leq s-1\). Differentials into or out of total degree \(n\) vanish on the pages \(E^r\) with \(r\geq n+2\): those leaving \(E_{p,q}\) end in \(p-r<0\) unless \(r\leq p\leq n\), and those reaching it start in weight \(q-r+1<0\) unless \(r\leq q+1\leq n+1\). As \(m-1\geq2n\), the projections are isomorphisms on the pages \(E^2,\dots,E^{n+2}\) in total degree \(n\). By Corollary 2.2 of the lesson on connectivity of powers of simplicial ideals, \(\pi_n(Q/J^m)=\operatorname{Tor}^A_n(B,B)\). Its filtration is by the images of the \(\pi_n(J^q/J^m)\), which are the images of the \(\pi_n(J^q)\), since \(\pi_n(J^q)\to\pi_n(J^q/J^m)\) is surjective, \(J^m\) being \(m\)-connective; and \(\pi_n(J^q)=0\) for \(q>n\). \(\square\)

Since \(\pi_q(J^{q+1})=\pi_{q-1}(J^{q+1})=0\), the top term in total degree \(q\) is \(E^\infty_{0,q}=F^q\), the image of \(\pi_q(J^q)\cong\pi_q(J^q/J^{q+1})=E^2_{0,q}\). No differential leaves \(E_{0,q}\), so \(E^2_{0,q}\to E^\infty_{0,q}\subseteq\operatorname{Tor}^A_q(B,B)\) is the *edge homomorphism*.

## 4. Weakly regular ideals and the cotangent complex

In this section \(B=A/I\) and \(N=I/I^2\).

**Lemma 4.1.** For \(q\geq1\), the \(q\)-fold product \(\pi_1(J)^{\otimes q}\to\pi_q(J^q)\) factors through an isomorphism \(\lambda_q\colon\Lambda^q_B(\pi_1J)\to\pi_q(J^q)\). With \(\iota_q\colon\pi_q(J^q)\to\pi_q(Q)\) induced by the inclusion, and \(\pi_1(J)\) identified with \(\pi_1(Q)\),
\[
\begin{aligned}&\theta_q=\iota_q\circ\lambda_q\circ\Lambda^q(\partial^{-1})\\&\quad\colon\Lambda^q_BN\to\operatorname{Tor}^A_q(B,B),\end{aligned}
\]
and the edge homomorphism of Theorem 3.2 is \(\theta_q\circ\Lambda^q(\partial_L)\circ\sigma\), where \(\sigma\colon E^2_{0,q}=\pi_q(S^qL_{B/A})\to\Lambda^q(\pi_1L_{B/A})\) is the inverse of the isomorphism of Proposition 2.3 (2).

**Proof.** The map \(\pi_q(J^q)\to\pi_q(J^q/J^{q+1})\) is an isomorphism, \(J^{q+1}\) being \((q+1)\)-connective, and \(J^q/J^{q+1}=S^q_B(J/J^2)\) (Proposition 1.1). The multiplication of \(Q\) followed by the projections is the multiplication of the graded ring \(\operatorname{gr}_J(Q)=S_B(J/J^2)\), so the \(q\)-fold product of \(\pi_1(J)\), followed by this isomorphism, is the \(q\)-fold product of \(\pi_1(J/J^2)\) composed with the isomorphism \(\pi_1(J)\to\pi_1(J/J^2)\). Proposition 2.3 (2) gives the factorization and \(\lambda_q\). The homomorphism \(\theta\) maps \(x_1\wedge\cdots\wedge x_q\) to the product of the \(\partial^{-1}x_i\in\pi_1(Q)=\pi_1(J)\), and the product of classes of \(J\) computed in \(\pi_q(J^q)\) maps under \(\iota_q\) to their product in \(\pi_q(Q)\). The last assertion follows from the definition of \(\partial_L\). \(\square\)

**Theorem 4.2.** The following are equivalent:

1. \(I\) is weakly regular;
2. \(D_q(B/A,M)=0\) for every \(B\)-module \(M\) and every \(q\geq2\);
3. \(N\) is flat and \(H_i(L_{B/A})=0\) for \(i\geq2\); that is, \(N\) is flat and \(\partial_L\) induces an isomorphism \(L_{B/A}\cong N[1]\) in \(D(B)\).

**Proof.** In (3), \(H_0(L_{B/A})=0\) and \(H_1(L_{B/A})\cong N\) by Proposition 1.1, so the two formulations agree.

(3) implies (2): \(L_{B/A}\otimes^\ell_BM\cong(N\otimes_BM)[1]\), because \(N\) is flat.

(2) implies (3): for \(M=B\), \(H_q(L_{B/A})=0\) for \(q\geq2\), so \(L_{B/A}\cong N[1]\) and \(D_2(B/A,M)=H_1(N\otimes^\ell_BM)\), which is \(\operatorname{Tor}^B_1(N,M)\). If these vanish for all \(M\), then for every injection \(M'\to M\) the map \(N\otimes M'\to N\otimes M\) is injective, by the long exact sequence of \(\operatorname{Tor}\); so \(N\) is flat.

(3) implies (1): by Proposition 2.4 (2), \(\pi_j(S^kL_{B/A})=0\) for \(j\neq k\). The simplicial module \(Q/J^q\) has the finite filtration by the \(J^k/J^q\), \(0\leq k<q\), with quotients \(S^kL_{B/A}\) (Proposition 1.1), whose homotopy is concentrated in degree \(k<q\). By the long exact sequences, \(\pi_i(Q/J^q)=0\) for \(i\geq q\). The long exact sequence of \(0\to J^q\to Q\to Q/J^q\to0\) shows that \(\iota_q\) is an isomorphism, and by Lemma 4.1 so is \(\theta_q\). As \(N\) is flat, \(I\) is weakly regular.

(1) implies (3): \(N\) is flat, and \(\theta_q\), hence \(\iota_q\), is an isomorphism for every \(q\) (Lemma 4.1). Write \(L=L_{B/A}=J/J^2\). We show \(\pi_{n+1}(L)=0\) by induction on \(n\geq1\), assuming \(\pi_i(L)=0\) for \(2\leq i\leq n\). Put \(X=J/J^{n+2}\) and \(Y=J^2/J^{n+2}\), so that \(X/Y=L\).

For \(i\geq1\), \(\pi_i(X)\cong\pi_i(Q/J^{n+2})\), since \(Q/J^{n+2}\to B\) has kernel \(X\) and \(B\) is constant, and \(\pi_i(Q)\to\pi_i(Q/J^{n+2})\) is an isomorphism for \(i\leq n+1\) (Corollary 2.2 of the lesson on connectivity of powers of simplicial ideals). Under these identifications, the map \(\pi_i(J^i)\to\pi_i(X)\) induced by \(J^i\subseteq J\) is \(\iota_i\), for \(1\leq i\leq n+1\).

The surjection \(\iota_{n+1}\) factors through \(\pi_{n+1}(Y)\), because \(J^{n+1}/J^{n+2}\subseteq Y\); so \(\pi_{n+1}(Y)\to\pi_{n+1}(X)\) is surjective. In the long exact sequence
\[
\begin{aligned}&\pi_{n+1}(Y)\to\pi_{n+1}(X)\to\pi_{n+1}(L)\\
&\quad\xrightarrow{\ \partial\ }\pi_n(Y)\to\pi_n(X)\end{aligned}
\]
the map \(\partial\) is therefore injective. It remains to show that \(\pi_n(Y)\to\pi_n(X)\) is injective; then \(\partial=0\) and \(\pi_{n+1}(L)=0\). For \(n=1\), \(\pi_1(Y)=0\), since \(Y=J^2/J^3\) is \(2\)-connective. For \(n\geq2\), the quotient \(Y/(J^n/J^{n+2})=J^2/J^n\) has the finite filtration with quotients \(S^kL\), \(2\leq k\leq n-1\), and \(\pi_n(S^kL)=0\) for these \(k\) by Proposition 2.4 (1), since \(n\leq n+k-2\) and \(n\neq k\). So \(\pi_n(J^2/J^n)=0\), and \(\pi_n(J^n/J^{n+2})\to\pi_n(Y)\) is surjective. As \(\pi_n(J^n)\to\pi_n(J^n/J^{n+2})\) is surjective too, \(\pi_n(J^n)\to\pi_n(Y)\) is surjective; its composite with \(\pi_n(Y)\to\pi_n(X)\) is the injection \(\iota_n\). So \(\pi_n(Y)\to\pi_n(X)\) is injective. \(\square\)

**Corollary 4.3.** If \(I\) is Koszul-regular, then \(I/I^2\) is locally free of finite rank and \(L_{B/A}\cong(I/I^2)[1]\). For every \(B\)-module \(M\), \(D_1(B/A,M)=I/I^2\otimes_BM\) and \(D_q(B/A,M)=0\) for \(q\neq1\).

**Proof.** By Proposition 4.2 of the lesson on weakly regular ideals, \(I\) is weakly regular and \(I/I^2\) is locally free. Apply Theorem 4.2 and the formula \(L_{B/A}\otimes^\ell_BM\cong(I/I^2\otimes_BM)[1]\). \(\square\)

For a Koszul-regular sequence in a ring, Lemma 7.1 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#7-complete-intersections-and-computations) obtains \(L_{B/A}\cong(I/I^2)[1]\) through the transitivity triangle.

**Corollary 4.4.** If \(I\) is weakly regular, then \(E^2_{p,q}=0\) for \(p\neq0\) in the fundamental spectral sequence, all differentials vanish, and the edge homomorphism is the isomorphism \(\theta_q\circ\Lambda^q(\partial_L)\circ\sigma\colon E^2_{0,q}\to\operatorname{Tor}^A_q(B,B)\).

**Proof.** By Theorem 4.2, \(L_{B/A}\) satisfies the hypothesis of Proposition 2.4 (2), so \(E^2_{p,q}=\pi_{p+q}(S^qL_{B/A})=0\) unless \(p=0\). Every differential changes \(p\), so all vanish. The edge homomorphism is described in Lemma 4.1, and \(\theta_q\) is an isomorphism. \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(k\) be a field, \(A=k[t]/(t^2)\) and \(B=k=A/(t)\). Using Theorem 3.2 and Exercise 5.2 of the lesson on weakly regular ideals, show that \(H_2(L_{k/A})\cong k\).

**Exercise 5.2.** Let \(k\) be a field, \(A=k[x,y]/(xy)\) and \(B=k=A/(x,y)\). Using Theorem 3.2 and Exercise 5.3 of the lesson on weakly regular ideals, show that \(H_2(L_{k/A})\neq0\), and deduce from Theorem 4.2 again that \((x,y)\) is not weakly regular.

**Exercise 5.3.** Let \(L\) be a simplicial module with flat terms over a ring \(B\), with \(\pi_0(L)=0\), and let \(N\) be a flat \(B\)-module. Show that for \(L=\Sigma N\) all the maps of Proposition 2.3 (2) are isomorphisms \(\Lambda^kN\cong\pi_k(S^k\Sigma N)\) and that \(\pi_j(S^k\Sigma N)=0\) for \(j\neq k\), and compare with Proposition 4.1 of the lesson on weakly regular ideals.

## 6. Complete solutions

**Solution 5.1.** By Exercise 5.2 of the lesson on weakly regular ideals, \(\operatorname{Tor}^A_2(k,k)=k\), and \(I/I^2=kt\) has \(\Lambda^2_k(I/I^2)=0\). In total degree \(2\) the second page has \(E^2_{0,2}=\pi_2(S^2L_{k/A})\), isomorphic to \(\Lambda^2_k(\pi_1L_{k/A})=\Lambda^2_k(kt)=0\) (Propositions 1.1 and 2.3), \(E^2_{1,1}=H_2(L_{k/A})\) and \(E^2_{2,0}=H_2(B)=0\). The differentials leaving \(E_{1,1}\) end in \(p<0\), and those reaching it start in weight \(2-r\leq0\), from \(E_{3,0}=H_3(B)=0\) for \(r=2\) and from negative weights otherwise. So \(E^\infty_{1,1}=H_2(L_{k/A})\) is the only nonzero graded piece of \(\operatorname{Tor}^A_2(k,k)\), and \(H_2(L_{k/A})\cong k\).

**Solution 5.2.** By Exercise 5.3 of the lesson on weakly regular ideals, \(\operatorname{Tor}^A_2(k,k)\) has dimension \(2\) and \(I/I^2\) dimension \(2\). In total degree \(2\), \(E^\infty_{0,2}\) is a quotient of \(E^2_{0,2}\cong\Lambda^2_k(I/I^2)=k\), \(E^\infty_{2,0}=0\), and as in Solution 5.1, \(E^\infty_{1,1}=H_2(L_{k/A})\). The dimensions of the graded pieces add up to \(2\), so \(H_2(L_{k/A})\) has dimension at least \(1\). By Theorem 4.2, \((x,y)\) is not weakly regular.

**Solution 5.3.** Here \(NL=N[1]\), so in the proof of Proposition 2.3 one can take \(E=N\), and \(\pi_k(S^k\Sigma N)\cong\Lambda^kN\) through the shift isomorphism, while \(\pi_j(S^k\Sigma N)=0\) for \(j\neq k\) because \(\Lambda^k(N)[k]\) is concentrated in degree \(-k\). Proposition 2.3 (2) says that the products of classes of degree one give \(\Lambda^kN\cong\pi_k(S^k\Sigma N)\); with the signs \((-1)^{k(k-1)/2}\) this is the isomorphism \(\psi\) of the proof of Proposition 4.1 of the lesson on weakly regular ideals.

## Sources

The fundamental spectral sequence and the characterization of weakly regular ideals by the cotangent complex are due to Quillen for rings, in Sections 6, 8 and 10 of his MIT notes on the homology of commutative rings (1968), [available from Haynes Miller's page](https://math.mit.edu/~hrm/manuscripts/quillen-commutative-algebra.pdf), where these ideals are called quasi-regular and the cotangent complex is written \(\mathbb L D_{B/A}\). Their form for rings of a topos is due to Illusie, in his work on the cotangent complex. The proof of the criterion given here works with the long exact sequences of the powers of \(J\) instead of the spectral sequence.
