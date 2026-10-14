# Completed cones over surfaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A *small Cohen–Macaulay module* over a Noetherian local ring \((R,\mathfrak m)\) is a nonzero finitely generated \(R\)-module \(M\) with \(\operatorname{depth}M=\dim R\). Hochster asked whether every complete Noetherian local domain has one. [OpenAI-SCM] answers this in the negative: there is a three-dimensional complete Noetherian normal local domain, containing \(\mathbb C\) and with residue field \(\mathbb C\), without a small Cohen–Macaulay module. This course gives the proof.

The rings are completed cones over smooth projective surfaces. This lesson constructs them, together with a regular model that resolves the vertex, and shows how a small Cohen–Macaulay module produces a sheaf on the regular model whose restriction to the exceptional surface is torsion-free. The next lessons turn this sheaf into numerical inequalities.

- Small Cohen–Macaulay modules and the two theorems of the course (Section 1).
- A finite map from the surface to the plane (Lemma 2.1).
- The section ring and its completion (Proposition 3.1).
- The regular model and normality (Proposition 4.1).
- Small Cohen–Macaulay modules are free over a power series ring (Lemma 5.1).
- The extension to the regular model (Proposition 6.1).

The lesson follows [OpenAI-SCM, Sections 1 and 2]. It uses commutative algebra from the course *Commutative algebra for geometry*, schemes and their cohomology from the courses *Morphisms of schemes* and *Cohomology of quasi-coherent sheaves*, and surface Riemann–Roch for line bundles from the lesson [Cycle classes and the Lefschetz fixed point formula for curves](course:AG-LTF/cycle-classes-and-the-lefschetz-fixed-point-formula-for-curves) (course *ℓ-adic cohomology and trace formulas*); the exact results are named where they are used.

## 1. Small Cohen–Macaulay modules

Let \((R,\mathfrak m)\) be a Noetherian local ring. For a nonzero finite \(R\)-module \(M\), always \(\operatorname{depth}M\le\dim\operatorname{Supp}M\le\dim R\) (Theorem 3.1 of [Regular sequences, depth and Cohen–Macaulay modules](course:AG-CA/regular-sequences-depth-and-cohen-macaulay-modules)). A small Cohen–Macaulay module is one for which both inequalities are equalities. If \(R\) is Cohen–Macaulay, \(R\) itself is one; a regular local ring is Cohen–Macaulay (Theorem 6.1 there).

**The question.** Does every complete Noetherian local domain have a small Cohen–Macaulay module? In dimension at most two the answer is yes: the normalization is a finite extension, and a normal local domain of dimension at most two is Cohen–Macaulay. This is quoted from [Hochster, Section 2], as is the history of the question; it is not used below.

**Theorem 1.1** ([OpenAI-SCM, Theorem 1.1]). There is a three-dimensional complete Noetherian normal local domain \(R\) containing \(\mathbb C\), with residue field \(\mathbb C\), such that no nonzero finitely generated \(R\)-module has depth three.

The ring is the completed cone \(R(X,H)\) over a surface \(X\) with a polarization \(H\), defined in Section 3. The proof combines an obstruction with an example.

**Theorem 1.2** (obstruction; [OpenAI-SCM, Theorem 1.2]). Let \(X\) be a smooth integral projective surface over \(\mathbb C\) and \(H\) a divisor with \(\mathcal O_X(H)\) ample and globally generated. If \(R(X,H)\) has a small Cohen–Macaulay module, then
\[
K_X^2-2c_2(X)\le6H^2 .
\]

Theorem 1.2 is proved in [The numerical obstruction](the-numerical-obstruction.md), from this lesson and [Elementary modifications and a variance inequality](elementary-modifications-and-a-variance-inequality.md). A surface with \(K_X^2-2c_2(X)>6H^2\) is constructed in [A Hirzebruch–Kummer surface](a-hirzebruch-kummer-surface.md), which also proves Theorem 1.1.

Related work, as described in [OpenAI-SCM, Section 1] and not used in this course: Anghel excludes graded maximal Cohen–Macaulay modules over section rings of the same surfaces [Anghel]; Chen proposes a local cohomology bound for reflexive modules over completed cones with \(K_X\equiv4H\), with a completed-local counterexample from a cover of exponent six [Chen].

Throughout this lesson, \(X\) is a smooth integral projective surface over \(\mathbb C\) and \(H\) a divisor on \(X\) such that \(\mathcal O_X(H)\) is ample and globally generated. Intersection numbers of divisors are those of the lesson on cycle classes named above, defined by Euler characteristics (its formula (HI.1)), and \(h=H^2=H\cdot H\).

## 2. A finite map to the plane

**Lemma 2.1.** There are sections \(s_0,s_1,s_2\) of \(\mathcal O_X(H)\) without a common zero. The morphism \(f\colon X\to\mathbb P^2\) that they define is finite and surjective, \(f^*\mathcal O(1)=\mathcal O_X(H)\), and \(f_*\mathcal O_X\) is a coherent sheaf of generic rank \(h\). In particular \(h>0\) and \(f\) has degree \(h\).

**Proof.** *The sections.* Since \(\mathcal O_X(H)\) is globally generated, the sections vanishing at a given point form a proper subspace of \(V=H^0(X,\mathcal O_X(H))\), and a finite union of proper subspaces of a complex vector space is not all of it. Choose \(s_0\ne0\); its zero set has finitely many irreducible components of dimension one. Choose \(s_1\) nonzero at one point of each of them. Then \(s_1\) vanishes on none of these curves, so the common zero set of \(s_0\) and \(s_1\) is finite. Choose \(s_2\) nonzero at each of its points.

*Finiteness.* The morphism \(f\) is proper, since \(X\) is projective. If a fiber had positive dimension, it would contain an integral curve \(C\) mapped to a point, and \(\mathcal O_X(H)|_C=f^*\mathcal O(1)|_C\) would be trivial. But \(\mathcal O_X(H)|_C\) is ample on the projective curve \(C\), so \(\chi(C,\mathcal O_X(tH)|_C)\) is a polynomial of degree one in \(t\) (Theorem 3.1 of [Euler characteristics and Hilbert polynomials](course:AG-QC/euler-characteristics-and-hilbert-polynomials)), whereas for the trivial bundle it is constant. So \(f\) is quasi-finite, and a proper quasi-finite morphism is finite (Theorem 5.1 of [Zariski's main theorem](course:AG-MO/zariskis-main-theorem)). Its image is closed, irreducible and of dimension two, so \(f\) is surjective.

*Degree.* Since \(f\) is finite, \(H^q(X,\mathcal O_X(tH))=H^q(\mathbb P^2,f_*\mathcal O_X(t))\) for all \(q\) and \(t\) (projection formula and affineness of \(f\)). By surface Riemann–Roch for line bundles ((HI.17) of the lesson on cycle classes),
\[
\begin{aligned}
\chi(X,\mathcal O_X(tH))&=\tfrac h2t^2-\tfrac12(H\cdot K_X)\,t\\
&\quad+\chi(\mathcal O_X) .
\end{aligned}
\]
Let \(N_0\) be the generic rank of \(F_0=f_*\mathcal O_X\). Choose \(N_0\) sections of \(F_0(a)\), for large \(a\), that are linearly independent at the generic point; they give an injection \(\mathcal O(-a)^{N_0}\to F_0\) whose cokernel \(Q\) vanishes at the generic point, so \(\dim\operatorname{Supp}Q\le1\). By additivity, \(\chi(F_0(t))=N_0\chi(\mathcal O(t-a))+\chi(Q(t))\), and \(\chi(Q(t))\) has degree at most one in \(t\) (Theorem 3.1 of the lesson on Euler characteristics). Comparing the coefficients of \(t^2\) gives \(N_0=h\). The generic rank of \(f_*\mathcal O_X\) is the degree of the extension of function fields, so \(f\) has degree \(h\), and \(h>0\). \(\blacksquare\)

## 3. The section ring and its completion

Put
\[
T=T(X,H)=\bigoplus_{j\ge0}H^0(X,\mathcal O_X(jH)),
\]
a graded ring under multiplication of sections. Let \(S=\mathbb C[x_0,x_1,x_2]\) map to \(T\) by \(x_i\mapsto s_i\in T_1\), let \(A=\mathbb C[[x_0,x_1,x_2]]\), and
\[
R=R(X,H)=T\otimes_SA .
\]
Write \(\mathfrak n=T_{>0}=\bigoplus_{j>0}T_j\) and \(\mathfrak a=(x_0,x_1,x_2)T\).

**Proposition 3.1.**

1. \(T\) is a domain with \(T_0=\mathbb C\), and \(S\to T\) is injective and finite.
2. \(R\) is the ring \(\prod_{j\ge0}T_j\) of formal sums \(\sum_ja_j\), \(a_j\in T_j\), where the product of \(\sum_ja_j\) and \(\sum_kb_k\) is \(\sum_nc_n\) with \(c_n=\sum_{j+k=n}a_jb_k\).
3. \(R\) is a complete Noetherian local domain with maximal ideal \(\prod_{j>0}T_j\) and residue field \(\mathbb C\). It is finite over \(A\), \(A\to R\) is injective, and \(\dim R=3\).
4. \(R\) is the completion of the local ring \(T_{\mathfrak n}\) at its maximal ideal.

**Proof.** *Part 1.* \(T_0=H^0(X,\mathcal O_X)\) is a finite-dimensional \(\mathbb C\)-algebra without zero divisors, as \(X\) is integral and projective, hence a finite field extension of \(\mathbb C\), hence \(\mathbb C\). The product of two nonzero sections of line bundles on an integral scheme is nonzero, so \(T\) is a domain. A homogeneous polynomial \(P\) of degree \(j\) maps to the section \(f^*P\) of \(f^*\mathcal O(j)=\mathcal O_X(jH)\); if \(P\ne0\), then \(P\) is nonzero at the generic point of \(\mathbb P^2\), and \(f^*P\) is nonzero at the generic point of \(X\), which maps to it because \(f\) is surjective. So \(S\to T\) is injective. By the projection formula \(T_j=H^0(\mathbb P^2,F_0(j))\) with \(F_0=f_*\mathcal O_X\), and the module \(\bigoplus_{j\ge0}H^0(\mathbb P^2,F_0(j))\) is finite over \(S\) (Lemma 3.1 of [Serre's theorems on projective schemes](course:AG-QC/serres-theorems-on-projective-schemes)).

*Part 2.* As \(T\) is a finite \(S\)-module, \(T\otimes_SA\) is the \((x_0,x_1,x_2)\)-adic completion of \(T\) (Theorem 3.1 of [Completion](course:AG-CA/completion); the completion of \(S\) at \((x_0,x_1,x_2)\) is \(A\)). Let \(T\) be generated as an \(S\)-module by homogeneous elements of degrees at most \(a'\). Then
\[
\mathfrak a^j\subseteq T_{\ge j},\qquad T_{\ge j+a'}\subseteq\mathfrak a^j ,
\]
the second because an element of degree at least \(j+a'\) is a combination of the generators with coefficients of degree at least \(j\) in \(S\). So the \(\mathfrak a\)-adic completion is the inverse limit of the \(T/T_{\ge j}\), which is the ring of part 2.

*Part 3.* An element \(\sum_ja_j\) with \(a_0\ne0\) is a unit: its inverse is computed degree by degree, since \(T_0=\mathbb C\). So \(R\) is local with maximal ideal \(\prod_{j>0}T_j\) and residue field \(\mathbb C\). For nonzero elements, the product of the lowest nonzero homogeneous terms is nonzero, so \(R\) is a domain. \(R\) is finite over \(A\) because \(T\) is finite over \(S\), hence Noetherian. It is complete: it is a finite module over the complete local ring \(A\), hence \(\mathfrak m_A\)-adically complete (Theorem 3.1 of the lesson on completion), and \(\mathfrak m_AR\) is primary to the maximal ideal (part 4 below). The map \(A\to R\) is injective because \(S\to T\) is injective and \(A\) is flat over \(S\) (Theorem 3.2 of the lesson on completion). An injective finite extension does not change the Krull dimension (lying over, going up and incomparability, Theorems 3.2 and 3.3 of [Integral extensions, lying over, going up and going down](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down)), so \(\dim R=\dim A=3\).

*Part 4.* \(T/\mathfrak a\) is a finite-dimensional graded algebra with \(T_0=\mathbb C\), so its elements of positive degree are nilpotent and \(\sqrt{\mathfrak a}=\mathfrak n\). Hence the \(\mathfrak a\)-adic and the \(\mathfrak n\)-adic topologies on \(T\) coincide, and since \(\mathfrak n\) is maximal, \(T/\mathfrak n^k=T_{\mathfrak n}/\mathfrak n^kT_{\mathfrak n}\) for all \(k\). \(\blacksquare\)

## 4. The regular model

For an invertible sheaf \(L\) on a scheme \(Y\), its *total space* is \(\operatorname{Tot}(L)=\operatorname{Spec}_Y\operatorname{Sym}(L^{-1})\) (relative spectrum, Theorem 1.1 of [Affine, integral and finite morphisms](course:AG-MO/affine-integral-and-finite-morphisms)); its sections over \(Y\) are the sections of \(L\). The *zero section* \(Y\subset\operatorname{Tot}(L)\) is cut out by the ideal \(\bigoplus_{j\ge1}L^{-j}\), which is locally generated by one nonzerodivisor; so it is an effective Cartier divisor with conormal sheaf \(L^{-1}\).

Let
\[
\begin{gathered}
V_0=\operatorname{Tot}(\mathcal O_{\mathbb P^2}(-1)),\\
W_0=\operatorname{Tot}(\mathcal O_X(-H))=X\times_{\mathbb P^2}V_0 .
\end{gathered}
\]
The global functions are \(\Gamma(V_0,\mathcal O)=\bigoplus_jH^0(\mathcal O(j))=S\) and \(\Gamma(W_0,\mathcal O)=T\), which give morphisms \(V_0\to\operatorname{Spec}S\) and \(W_0\to\operatorname{Spec}T\); the function \(x_i\) is the fiberwise linear function given by \(s_i\). Base change along \(\operatorname{Spec}A\to\operatorname{Spec}S\) gives
\[
V=V_0\times_SA,\qquad W=W_0\times_SA ,
\]
with the finite morphism \(g\colon W\to V\) (base change of \(f\)) and \(p\colon W\to\operatorname{Spec}R\). The zero sections lie over the origin of \(\operatorname{Spec}S\), whose preimage in \(\operatorname{Spec}A\) is the closed point with the same residue field. So they stay unchanged: \(D=\mathbb P^2\subset V\) and \(X\subset W\), with ideal sheaves \(\mathcal I\) and \(\mathcal J\). Since \(A\) is flat over \(S\), they remain effective Cartier divisors, and
\[
\begin{gathered}
\mathcal J=g^*\mathcal I,\\
\mathcal I|_D=\mathcal O_D(1),\qquad\mathcal J|_X=\mathcal O_X(H) .
\end{gathered}
\]

**Proposition 4.1.**

1. The closed fiber of \(W\to\operatorname{Spec}A\) is \(X\), and \(p\) restricts to an isomorphism from \(W\setminus X\) onto the punctured spectrum \(\operatorname{Spec}R\setminus\{\mathfrak m_R\}\). Likewise for \(V\setminus D\) and \(\operatorname{Spec}A\).
2. \(V\) and \(W\) are regular and integral, and \(p\) is proper.
3. \(\Gamma(W,\mathcal O_W)=R\).
4. \(R\) is normal.

**Proof.** *Part 1.* Over the open set \(X_i\) where \(s_i\ne0\), which is affine as the preimage of an affine open set under the finite morphism \(f\), the bundle \(\mathcal O_X(-H)\) is trivialized and \(W_0|_{X_i}=X_i\times\mathbb A^1\) with fiber coordinate \(u=x_i\). There \(x_k=(s_k/s_i)u\), so \((x_0,x_1,x_2)\) generates the ideal \((u)\) of the zero section: the closed fiber is \(X\). Every element of \(\Gamma(X_i,\mathcal O_X)\) has the form \(a/s_i^j\) with \(a\in T_j\) (Lemma 2.1 of [Ample invertible sheaves](course:AG-MO/ample-invertible-sheaves)), so
\[
T[1/s_i]=\Gamma(X_i,\mathcal O_X)[s_i,s_i^{-1}] ,
\]
which is also the coordinate ring of \(X_i\times\mathbb G_m\), the part of \(W_0\) over \(X_i\) off the zero section. The open sets \(D(s_i)\) cover \(\operatorname{Spec}T\setminus V(\mathfrak n)\). So \(W_0\setminus X\to\operatorname{Spec}T\setminus V(\mathfrak n)\) is an isomorphism, and so is its base change; the preimage of \(V(\mathfrak n)\) in \(\operatorname{Spec}R\) is \(\{\mathfrak m_R\}\) by Proposition 3.1. The case of \(V\) is the case \(X=\mathbb P^2\), \(H=\mathcal O(1)\).

*Part 2.* \(W_0\to V_0\) is finite and \(V_0\to\operatorname{Spec}S\), the blowup of the origin, is proper; so \(W\to\operatorname{Spec}A\) is proper, and since \(\operatorname{Spec}R\to\operatorname{Spec}A\) is separated, \(p\) is proper. Let \(w\in X\). The equation \(u\) of \(X\) is a nonzerodivisor of \(\mathcal O_{W,w}\), and \(\mathcal O_{W,w}/u=\mathcal O_{X,w}\) is regular because \(X\) is smooth; so \(\mathcal O_{W,w}\) is regular (Proposition 1.3 of [Regular local rings](course:AG-CA/regular-local-rings)). Every other point \(w\) has a specialization in \(X\): the image of its closure in \(\operatorname{Spec}A\) is closed, so it contains the closed point, and the closure meets the closed fiber \(X\). So \(\mathcal O_{W,w}\) is a localization of a regular local ring, hence regular (Theorem 3.2 there). The local rings of \(W\) are domains (Theorem 6.1 of the lesson on regular sequences), so two irreducible components of the Noetherian scheme \(W\) cannot meet. Each component meets \(X\), by the same specialization argument, and the connected \(X\) is covered by the finitely many disjoint closed sets in which the components meet it; so there is only one component, and \(W\) is integral. The same holds for \(V\).

*Part 3.* \(W_0\to\operatorname{Spec}S\) is quasi-compact and separated and \(A\) is flat over \(S\), so flat base change gives \(\Gamma(W,\mathcal O_W)=\Gamma(W_0,\mathcal O_{W_0})\otimes_SA\), which is \(T\otimes_SA=R\) (Theorem 2.1 of [Base change and the Grothendieck complex](course:AG-QC/base-change-and-the-grothendieck-complex)).

*Part 4.* By part 1, the function field of the integral scheme \(W\) is the fraction field of \(R\). Let \(z\) in it be integral over \(R\). Then \(z\) is integral over every local ring \(\mathcal O_{W,w}\), which is regular, hence factorial (Theorem 5.3 of the lesson on regular local rings) and normal (Proposition 2.3 of the lesson on integral extensions). So \(z\) lies in every local ring, that is, \(z\) is a global function, and \(z\in R\) by part 3. \(\blacksquare\)

## 5. Small Cohen–Macaulay modules are free over the power series ring

**Lemma 5.1.** Let \(M\) be a small Cohen–Macaulay \(R\)-module. Then:

1. \(x_0,x_1,x_2\) is an \(M\)-regular sequence, and \(M\cong A^N\) as an \(A\)-module for some \(N\ge1\);
2. \(M\) has positive rank \(r\) over \(R\), that is, \(M\otimes_R\operatorname{Frac}R\ne0\);
3. \(M_{\mathfrak q}\) is a free \(R_{\mathfrak q}\)-module for every prime \(\mathfrak q\ne\mathfrak m_R\).

**Proof.** *Part 1.* By Proposition 3.1, \((x_0,x_1,x_2)R\) is primary to \(\mathfrak m_R\), so \(x_0,x_1,x_2\) is a system of parameters of \(R\). Since \(\operatorname{depth}M=3=\dim\operatorname{Supp}M\), \(M\) is Cohen–Macaulay of support dimension three, and every system of parameters of \(M\) is \(M\)-regular (Corollary 4.3 of the lesson on regular sequences). So \(x_0,x_1,x_2\) is a regular sequence on \(M\) as an \(A\)-module, which is finite, and \(\operatorname{depth}_AM=3\). The regular local ring \(A\) gives \(M\) finite projective dimension (Corollary 4.3 of [Projective dimension and the Auslander–Buchsbaum formula](course:AG-CA/projective-dimension-and-the-auslander-buchsbaum-formula)), and the Auslander–Buchsbaum formula (Theorem 3.1 there) gives projective dimension \(3-3=0\). A finite projective module over a local ring is free (Proposition 2.1 there).

*Part 2.* \(\operatorname{Supp}M\) contains a prime \(\mathfrak q\) with \(\dim R/\mathfrak q=3\). In the local domain \(R\) of dimension three, every nonzero prime \(\mathfrak q\) has \(\dim R/\mathfrak q\le2\), since a chain below \(R/\mathfrak q\) can be extended by \(0\subsetneq\mathfrak q\). So \(0\in\operatorname{Supp}M\).

*Part 3.* \(M_{\mathfrak q}\) is Cohen–Macaulay over \(R_{\mathfrak q}\) (Theorem 5.1 of the lesson on regular sequences), and its support is all of \(\operatorname{Spec}R_{\mathfrak q}\) by part 2; so \(\operatorname{depth}M_{\mathfrak q}=\dim R_{\mathfrak q}\). By Proposition 4.1, \(R_{\mathfrak q}\) is a local ring of the regular scheme \(W\setminus X\), hence regular. The Auslander–Buchsbaum formula over \(R_{\mathfrak q}\) gives projective dimension \(0\). \(\blacksquare\)

## 6. The extension to the regular model

For a coherent sheaf \(F\) on \(W\) write \(F^\vee=\mathcal{H}om(F,\mathcal O_W)\).

**Proposition 6.1.** Let \(M\) be a small Cohen–Macaulay \(R\)-module of rank \(r\), \(N\) as in Lemma 5.1, and
\[
\mathcal E=\bigl(p^*\widetilde M\bigr)^{\vee\vee},\qquad P=\mathcal E|_X=\mathcal E/\mathcal J\mathcal E .
\]
Then:

1. \(\mathcal E\) is coherent and torsion-free, and on \(W\setminus X\) it is the locally free sheaf of rank \(r\) given by \(M\).
2. \(P\) is a torsion-free sheaf of rank \(r\) on \(X\).
3. \(L'=g_*\mathcal E\) is a coherent torsion-free sheaf on \(V\) whose restriction to \(V\setminus D\) is isomorphic to \(\mathcal O^N\), and \(L'|_D\cong f_*P\).
4. \(N=rh\).

**Proof.** *Part 1.* Duals of coherent sheaves on the Noetherian scheme \(W\) are coherent and torsion-free. On \(W\setminus X\), \(p\) is an isomorphism onto the punctured spectrum, where \(\widetilde M\) is locally free of rank \(r\) by Lemma 5.1, and a locally free sheaf equals its double dual.

*A depth estimate.* Let \(w\in W\) and \(F\) coherent. A finite presentation \(\mathcal O^b\to\mathcal O^a\to F\to0\) near \(w\) dualizes to an exact sequence \(0\to F^\vee\to\mathcal O^a\to\mathcal O^b\); so \(F^\vee_w\) is the kernel of a map between free modules, whose image is a submodule of a free module. If \(\dim\mathcal O_{W,w}\ge2\), the depth lemma (Proposition 2.4 of the lesson on regular sequences), with free modules of depth \(\dim\mathcal O_{W,w}\) over the regular local ring and an image of depth at least one, gives \(\operatorname{depth}F^\vee_w\ge2\).

*Part 2.* Let \(w\in X\) be a point other than the generic point of \(X\); then \(\dim\mathcal O_{W,w}\ge2\), so \(\operatorname{depth}\mathcal E_w\ge2\). The equation \(u\) of \(X\) is a nonzerodivisor on the torsion-free \(\mathcal E_w\), so \(\operatorname{depth}P_w\ge1\), and \(w\) is not an associated point of \(P\). So \(P\) has no associated point except the generic point \(\xi\) of \(X\): it is torsion-free. At \(\xi\), \(\mathcal O_{W,\xi}\) is a regular local ring of dimension one, a discrete valuation ring, so \(\mathcal E_\xi\) is free of rank \(r\) and \(P_\xi\) has rank \(r\).

*Part 3.* \(g\) is finite, so \(L'\) is coherent; it is torsion-free because \(\mathcal E\) is and \(g\) is a finite surjective morphism of integral schemes. Since \(\mathcal J=g^*\mathcal I\), \(g^{-1}(D)=X\). Over \(V\setminus D\), the punctured spectrum of \(A\), the sheaf \(L'\) corresponds to \(M\) as an \(A\)-module, which is \(A^N\). Finally, since \(g\) is affine,
\[
\begin{aligned}
L'|_D&=g_*\mathcal E\otimes\mathcal O_V/\mathcal I\\
&=g_*\bigl(\mathcal E\otimes g^*(\mathcal O_V/\mathcal I)\bigr)\\
&=g_*(\mathcal E/\mathcal J\mathcal E),
\end{aligned}
\]
which is \(f_*P\) on \(D=\mathbb P^2\), as \(g\) restricts to \(f\) on \(X\).

*Part 4.* At the generic point of \(V\), the rank of \(L'\) is \(N\) by part 3, and it is \(r\) times the degree of \(g\). The degree of \(g\) is \([\operatorname{Frac}R:\operatorname{Frac}A]\), which equals \([\operatorname{Frac}T:\operatorname{Frac}S]=\deg f=h\), because \(R=T\otimes_SA\) and \(T\) is a torsion-free \(S\)-module of rank \(h\) (Lemma 2.1). \(\blacksquare\)

So a small Cohen–Macaulay module gives a torsion-free sheaf \(P\) of rank \(r\) on the exceptional surface, and the sheaf \(f_*P\) of rank \(N=rh\) on the plane is the restriction of a sheaf that is trivial away from the plane. The next lesson extracts a numerical inequality from this triviality.

## 7. Exercises

**7.1.** For \(X=\mathbb P^2\) and \(H\) a line, show that \(T=S\) and \(R=A\), and that \(R\) is a small Cohen–Macaulay module over itself.

**7.2.** For \(X=\mathbb P^1\times\mathbb P^1\) and \(H\) of bidegree \((1,1)\), the ring \(T\) is \(\mathbb C[a,b,c,d]/(ad-bc)\) (the Segre cone). Show that \(R\) is Cohen–Macaulay, so \(R\) is a small Cohen–Macaulay module over itself.

**7.3.** Let \(T\) be a finite graded \(S\)-module generated in degrees at most \(a'\). Show that \(T_{\ge j+a'}\subseteq(x_0,x_1,x_2)^jT\).

**7.4.** Let \(M\) be a small Cohen–Macaulay \(R\)-module of rank \(r\). Show that \(M^{\oplus2}\) is a small Cohen–Macaulay module of rank \(2r\), free of rank \(2N\) over \(A\).

**7.5.** Show that in Lemma 2.1 the sections can be chosen as general linear combinations of any basis of \(H^0(X,\mathcal O_X(H))\): the set of triples without a common zero contains a nonempty Zariski open subset of \(H^0(X,\mathcal O_X(H))^3\).

## 8. Solutions

**7.1.** \(H^0(\mathbb P^2,\mathcal O(j))\) is the space of forms of degree \(j\), so \(T=S\) with \(s_i=x_i\), and \(R=S\otimes_SA=A\). A regular local ring is Cohen–Macaulay (Theorem 6.1 of the lesson on regular sequences), so \(\operatorname{depth}A=3\).

**7.2.** \(ad-bc\) is a nonzero element of the maximal ideal of the regular local ring \(\mathbb C[[a,b,c,d]]\), and \(R=\mathbb C[[a,b,c,d]]/(ad-bc)\) by Proposition 3.1 (the degree completion of \(T\)). By Corollary 6.2 of the lesson on regular sequences, \(R\) is Cohen–Macaulay of dimension three.

**7.3.** A homogeneous element \(t\) of degree \(e\ge j+a'\) is \(\sum_k\sigma_kt_k\) with generators \(t_k\) of degree \(e_k\le a'\) and homogeneous \(\sigma_k\in S\) of degree \(e-e_k\ge j\), which lie in \((x_0,x_1,x_2)^j\).

**7.4.** By the Ext characterization of depth (Theorem 2.3 of the lesson on regular sequences), \(\operatorname{depth}M\) is the least \(i\) with \(\operatorname{Ext}^i(\mathbb C,M)\ne0\), and \(\operatorname{Ext}^i(\mathbb C,M^{\oplus2})=\operatorname{Ext}^i(\mathbb C,M)^{\oplus2}\). So \(M^{\oplus2}\) has depth three; its rank is \(2r\), and as an \(A\)-module it is \(A^{2N}\). So an obstruction has to exclude modules of every rank at once.

**7.5.** For each point \(y\in X\), the triples vanishing at \(y\) form a linear subspace of codimension three in \(V^3\), \(V=H^0(X,\mathcal O_X(H))\), because \(\mathcal O_X(H)\) is globally generated. The set of triples with a common zero is the image of the closed subset \(\{(y,s):s_i(y)=0\}\) of \(X\times V^3\), of dimension \(2+3\dim V-3<3\dim V\), under the proper projection to \(V^3\). Its image is closed and of smaller dimension, so its complement is a nonempty open set.

## References

- [OpenAI-SCM] OpenAI, *A Complete Local Domain without a Small Cohen–Macaulay Module*, OpenAI Math Release preprint, 23 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026
- [Hochster] M. Hochster, *Homological conjectures and lim Cohen–Macaulay sequences*, in: Homological and Computational Methods in Commutative Algebra, 2017, Section 2. https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/08/DSlim2.pdf
- [Anghel] C. Anghel, *Polarized varieties without arithmetically Cohen–Macaulay bundles and section rings without graded maximal Cohen–Macaulay modules in characteristic zero*, arXiv:2609.15589, version 1. https://arxiv.org/abs/2609.15589
- [Chen] L. Chen, *A local cohomology obstruction to small Cohen–Macaulay modules*, arXiv:2609.24142, version 1. https://arxiv.org/abs/2609.24142
