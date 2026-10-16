# Cone chains, torsion-freeness and the integral detector

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Coning off every sheet of the Cayley graph gives a two-dimensional complex whose cellular chains, by the cycle coordinates, form an exact sequence. Two consequences follow. A subgroup of prime order would act freely on this complex, which is impossible for an acyclic complex of dimension two; so the graphical group \(\Gamma\) is torsion-free. And the same exact sequence makes restriction \(H^2(B\Gamma;\mathbb Z)\to H^2(B\mathsf H;\mathbb Z)\) onto. An explicit integral \(2\)-cocycle on the Heisenberg group evaluates to \(-1\) on the torus spanned by \((z,x)\); extended to \(\Gamma\), it is the class that detects the torus in the main theorem [OpenAI-BCI, Sections 7.4-7.7, Lemmas 7.6-7.10, Proposition 7.11].

- The cone complex and exact chains (Section 1).
- Torsion-freeness (Section 2).
- The bar model and a Heisenberg cocycle (Section 3).
- Degree-two classes extend (Section 4).
- The detector (Section 5).

The setting of [Cycle coordinates and disjoint domains](cycle-coordinates-and-disjoint-domains.md) is in force: the formal right Cayley graph \(\mathcal C\), the family \(\mathcal Q\) of sheets, and the isomorphisms \(\Phi_R\) of Lemma 1.1 there. Domains play no role here. We use Lemmas 3.1 and 3.2 of [Torsion-freeness](course:kadison-kaplansky-projections/torsion-freeness#3-free-resolutions-over-a-cyclic-group) (the periodic resolution over a cyclic group of prime order), and two standard facts of algebraic topology, not proved in the programme:

**(BG)** (the bar construction; [Hatcher, Example 1B.7, Theorem 1B.8]). For a group \(\Lambda\), the \(\Delta\)-complex \(E\Lambda\) whose \(n\)-simplices are the ordered \((n+1)\)-tuples \((g_0,\ldots,g_n)\) of elements of \(\Lambda\), with faces given by deleting entries, is contractible, and \(\Lambda\) acts freely on it by left multiplication; the quotient \(B\Lambda\) is a \(K(\Lambda,1)\) CW complex, whose simplices are written \([g_1|\cdots|g_n]\) for the orbit of \((1,g_1,g_1g_2,\ldots,g_1\cdots g_n)\). The homotopy type of a CW complex \(K(\Lambda,1)\) is determined by \(\Lambda\), and a homomorphism \(f\) induces the cellular map \(Bf\) sending \([g_1|\cdots|g_n]\) to \([f(g_1)|\cdots|f(g_n)]\).

**(CC)** (cellular cohomology; [Hatcher, Theorem 3.5]). For a CW complex, singular cohomology with coefficients in \(G\) is the cohomology of the cellular cochain complex, which is \(\operatorname{Hom}(-,G)\) of the cellular chain complex, naturally for cellular maps.

## 1. The cone complex and exact chains

Starting from \(\mathcal C\), add a vertex \(c_Q\) for every sheet \(Q\), an oriented edge \(\sigma_{Q,u}\) (a *spoke*) from \(c_Q\) to every vertex \(u\) of \(Q\), and, for every positive edge \(e:u\to v\) of \(Q\), a triangle \(\tau_{Q,e}\) with cellular boundary
\[
\partial\tau_{Q,e}=e+\sigma_{Q,u}-\sigma_{Q,v} .\tag{1.1}
\]
Call the resulting two-dimensional complex \(\mathcal Z\). Different sheets give different spokes and triangles, also where their images in \(\mathcal C\) agree; the complex is defined by its cells, with finite chains only.

**Lemma 1.1** (exact cone chains; [OpenAI-BCI, Lemma 7.6]). For every commutative ring \(R\), the augmented cellular chain complex
\[
\begin{gathered}
0\to C_2(\mathcal Z;R)\xrightarrow{\partial_2}{}\\
C_1(\mathcal Z;R)\xrightarrow{\partial_1}C_0(\mathcal Z;R)\\
\xrightarrow{\varepsilon}R\to0
\end{gathered}\tag{1.2}
\]
is exact.

*Proof.* For an edge chain \(b\) of a sheet \(Q\), let \(c_Q*b\) be the same combination of its triangles, and for a vertex chain \(t\) of \(Q\) let \(\sigma_Q(t)\) be the corresponding spoke chain. By (1.1), \(\partial(c_Q*b)=b-\sigma_Q(\partial b)\).

*At \(C_2\).* A finite \(2\)-chain is \(\sum_Qc_Q*b_Q\) for finitely many edge chains \(b_Q\). If its boundary vanishes, its components on the distinct spoke sets give \(\partial b_Q=0\) for every \(Q\), and its component on \(\mathcal C\) gives \(\sum_Qb_Q=0\). Injectivity of \(\Phi_R\) gives all \(b_Q=0\).

*At \(C_1\).* Let \(b+\sum_Q\sigma_Q(t_Q)\) be a finite \(1\)-cycle, with \(b\) on \(\mathcal C\). Its coefficient at \(c_Q\) is the augmentation of \(t_Q\), so \(t_Q\) has total coefficient zero; as \(Q\) is connected, \(t_Q=\partial a_Q\) for a finite edge chain \(a_Q\) of \(Q\) (join the vertices of its support to one of them by paths). Adding \(\sum_Q\partial(c_Q*a_Q)\) removes all spokes, and leaves a \(1\)-cycle on \(\mathcal C\), which is \(\sum_Qz_Q\) with sheet cycles \(z_Q\), by surjectivity of \(\Phi_R\); and \(z_Q=\partial(c_Q*z_Q)\). So the original cycle is a boundary.

*At \(C_0\).* \(\mathcal C\) is connected and every cone vertex is joined to it, so a vertex chain of total coefficient zero is a boundary, and \(\varepsilon\) is onto. \(\square\)

Left translation acts cellularly on \(\mathcal Z\), preserving all orientations. Put \(A=\mathbb Z\Gamma\) and \(B=\mathbb Z\mathsf H\). Then
\[
\begin{gathered}
C_1(\mathcal Z;\mathbb Z),\ C_2(\mathcal Z;\mathbb Z)\\
\text{are free }A\text{-modules},\\
C_0(\mathcal Z;\mathbb Z)\cong A\oplus A\otimes_B\mathbb Z .
\end{gathered}\tag{1.3}
\]
Indeed an element stabilizing a formal edge fixes its initial vertex; one stabilizing a spoke fixes its endpoint in \(\mathcal C\); one stabilizing a triangle fixes its positive base edge. So these stabilizers are trivial. The group vertices form one free orbit, and the cone vertices the orbit \(\Gamma/\mathsf H\), since the stabilizer of a sheet is a conjugate of \(\mathsf H\) (Proposition 5.1 of [The private completion and the graphical group](the-private-completion-and-the-graphical-group.md)). Neither torsion-freeness nor equivariance of any domain choice is used.

## 2. Torsion-freeness

**Lemma 2.1** (comparison of free resolutions; [OpenAI-BCI, Lemma 7.7]). Let \(P_\bullet\to M\) and \(Q_\bullet\to N\) be exact augmented complexes of free modules over a ring \(A\). Every homomorphism \(M\to N\) lifts to a chain map \(P_\bullet\to Q_\bullet\), and any two lifts are chain homotopic. In particular two free resolutions of one module are chain homotopy equivalent, also after tensoring with a right module or applying \(\operatorname{Hom}_A(-,L)\).

*Proof.* On a basis of \(P_0\), choose images lifting the prescribed images under the augmentations. Having defined the map up to degree \(n-1\), the desired image of the boundary of a basis vector of \(P_n\) is a cycle of \(Q_{n-1}\), hence a boundary by exactness; choose a preimage and extend linearly. For two lifts, let \(f\) be their difference, with zero augmentation. Inductively, \(f_n-h_{n-1}\partial_n\) takes values in the cycles of \(Q_n\) (apply \(\partial\) and use the chain-map and previous homotopy identities), so it is \(\partial_{n+1}h_n\) on a basis; then \(f_n=\partial_{n+1}h_n+h_{n-1}\partial_n\), with \(h_{-1}=0\) and the zero augmentation at \(n=0\). Lifts of the identity in both directions give the homotopy equivalence; tensor and \(\operatorname{Hom}\) preserve the homotopy identities. No finite bases are needed. \(\square\)

**Lemma 2.2** (no element of finite order; [OpenAI-BCI, Lemma 7.8]). The group \(\Gamma\) is torsion-free.

*Proof.* \(\mathsf H\) is torsion-free (Corollary 1.2 of [The Heisenberg group and its laws](the-heisenberg-group-and-its-laws.md)). Suppose \(P\le\Gamma\) has prime order \(p\). The stabilizer of a cone vertex is a conjugate of \(\mathsf H\), so it meets \(P\) trivially; the other stabilizers are trivial by (1.3). So \(P\) acts freely on the cells of every dimension (on cells, not merely without fixed points of edges: no element can reverse a positive edge, since orientations are preserved). Choosing orbit representatives, the chains of \(\mathcal Z\) with coefficients \(\mathbb F_p\) are free \(\mathbb F_p[P]\)-modules, and Lemma 1.1 with \(R=\mathbb F_p\) makes them a free resolution of the trivial module \(\mathbb F_p\) of length two. Tensoring with \(\mathbb F_p\) gives zero homology above degree two, whereas by Lemmas 3.1 and 3.2 of [Torsion-freeness](course:kadison-kaplansky-projections/torsion-freeness#3-free-resolutions-over-a-cyclic-group) this homology is \(\mathbb F_p\) in every degree. Hence \(\Gamma\) has no subgroup of prime order, and an element of finite order \(n>1\) would have a power of prime order. \(\square\)

## 3. The bar model and a Heisenberg cocycle

For a group \(\Lambda\), let \(\mathcal B_n(\Lambda)\) be the free abelian group on the tuples \((g_0,\ldots,g_n)\in\Lambda^{n+1}\), with the diagonal left action, the alternating deletion boundary, and augmentation \(1\) on every tuple of length one. It is free over \(\mathbb Z\Lambda\), with the orbit representatives with \(g_0=1\), and prepending \(1\), \(s(g_0,\ldots,g_n)=(1,g_0,\ldots,g_n)\), is a contracting homotopy of abelian groups: \(\partial s+s\partial=\mathrm{id}\), including the augmentation. So \(\mathcal B_\bullet(\Lambda)\) is a free resolution of the trivial module \(\mathbb Z\). It is the cellular chain complex of \(E\Lambda\) in (BG), so by (BG) and (CC) the cohomology of
\[
\operatorname{Hom}_{\mathbb Z\Lambda}(\mathcal B_\bullet(\Lambda),\mathbb Z)
\]
is \(H^*(B\Lambda;\mathbb Z)\), and for a subgroup inclusion, restriction of these cochains to tuples of the subgroup is the pull-back along the induced map of classifying spaces. Write \([g_1|\cdots|g_n]\) for \((1,g_1,g_1g_2,\ldots,g_1\cdots g_n)\); then
\[
\begin{gathered}
\partial[g|h]=g[h]-[gh]+[g],\\
\partial[g|h|k]=g[h|k]-[gh|k]\\
+[g|hk]-[g|h],
\end{gathered}
\]
and with trivial coefficients these are the formulas of inhomogeneous group cochains.

In the matrix coordinates \((\alpha,\beta,\gamma)\) of Lemma 1.1 of the lesson on the Heisenberg group, \(x^ny^lz^c=(n,l,c+nl)\) and
\[
\begin{aligned}
&(\alpha,\beta,\gamma)(\alpha',\beta',\gamma')\\
&\quad=(\alpha+\alpha',\,\beta+\beta',\\
&\qquad\quad\gamma+\gamma'+\alpha\beta') .
\end{aligned}\tag{3.1}
\]

**Lemma 3.1** (a primitive Heisenberg detector; [OpenAI-BCI, Lemma 7.9]). The integer function
\[
\begin{gathered}
\omega\bigl((\alpha,\beta,\gamma),(\alpha',\beta',\gamma')\bigr)\\
=\alpha\gamma'+\binom\alpha2\beta'
\end{gathered}\tag{3.2}
\]
is a normalized group \(2\)-cocycle on \(\mathsf H\). Its class \(c_{\mathsf H}\in H^2(B\mathsf H;\mathbb Z)\) evaluates to \(-1\) on the torus with ordered generators \((z,x)\).

*Proof.* \(\binom\alpha2=\alpha(\alpha-1)/2\) is an integer for all integers \(\alpha\), and \(\omega\) vanishes when either argument is the identity. For \(g,h,k\) with coordinates \((\alpha,\beta,\gamma),(\alpha',\beta',\gamma'),(\alpha'',\beta'',\gamma'')\), the cocycle identity
\[
\omega(g,h)+\omega(gh,k)=\omega(h,k)+\omega(g,hk)
\]
reads, by (3.1),
\[
\begin{aligned}
&\alpha\gamma'+\tbinom\alpha2\beta'+(\alpha+\alpha')\gamma''\\
&\qquad+\tbinom{\alpha+\alpha'}2\beta''\\
&\quad=\alpha'\gamma''+\tbinom{\alpha'}2\beta''\\
&\qquad+\alpha(\gamma'+\gamma''+\alpha'\beta'')\\
&\qquad+\tbinom\alpha2(\beta'+\beta''),
\end{aligned}
\]
which holds by \(\binom{\alpha+\alpha'}2=\binom\alpha2+\binom{\alpha'}2+\alpha\alpha'\). Equivalently, \((t,g)(t',h)=(t+t'+\omega(g,h),gh)\) is an associative multiplication on \(\mathbb Z\times\mathsf H\), a central extension by \(\mathbb Z\).

The subgroup generated by \(z=(0,0,1)\) and \(x=(1,0,0)\) is free abelian of rank two, with \(z^ux^v=(v,0,u)\). Subdivide the square of the torus with vertices \(1,z,zx,x\) by the diagonal from \(1\) to \(zx\); its two oriented triangles are \((1,z,zx)-(1,x,xz)\), that is, the bar chain
\[
[z|x]-[x|z] .
\]
Sending the grid vertex \((u,v)\) to \(z^ux^v\) defines an equivariant map from the triangulated universal cover of the torus into \(E\Lambda\), \(\Lambda=\langle z,x\rangle\), which induces the identity on fundamental groups; so this chain represents the image of the fundamental class \([T^2]\). The evaluation is
\[
\omega(z,x)-\omega(x,z)=0-1=-1 ,
\]
since \(z\) has \(\alpha=0\), and \(x=(1,0,0)\), \(z=(0,0,1)\) give \(\omega(x,z)=1\). \(\square\)

## 4. Degree-two classes extend

**Lemma 4.1** (integral restriction is onto in degree two; [OpenAI-BCI, Lemma 7.10]). The inclusion \(\mathsf H\le\Gamma\) induces a surjection
\[
\begin{gathered}
H^2(B\Gamma;\mathbb Z)\\
\longrightarrow H^2(B\mathsf H;\mathbb Z) .
\end{gathered}\tag{4.1}
\]

*Proof.* Put \(M=\mathbb Z\), \(C_0=C_0(\mathcal Z;\mathbb Z)\cong A\oplus A\otimes_BM\) and \(K=\ker(C_0\to M)\). By Lemma 1.1 and (1.3), \(K\) has a free resolution of length one,
\[
\begin{gathered}
0\to P_1\xrightarrow{d_P}P_0\to K\to0,\\
P_1=C_2(\mathcal Z;\mathbb Z),\quad P_0=C_1(\mathcal Z;\mathbb Z) .
\end{gathered}
\]
As a right \(B\)-module, \(A\) is free (coset representatives), so \(I_\bullet=A\otimes_B\mathcal B_\bullet(\mathsf H)\) is a free resolution of \(A\otimes_BM\). Resolve \(C_0\) by \(Q_0=A\oplus I_0\) and \(Q_n=I_n\) for \(n\ge1\). Lift \(K\to C_0\) to a chain map \(f:P_\bullet\to Q_\bullet\): choose \(f_0\) on a basis lifting the inclusion; the elements \(f_0d_P(P_1)\) have zero augmentation in \(C_0\), so exactness gives \(f_1:P_1\to Q_1\) with \(d_Qf_1=f_0d_P\).

Define a free augmented complex \(T_\bullet\to M\) by \(T_0=Q_0\) and \(T_n=Q_n\oplus P_{n-1}\) for \(n\ge1\) (with \(P_j=0\) for \(j\ge2\)), with boundary \(d_T(q,p)=(d_Qq+f_{n-1}p,\,-d_Pp)\) for \(n\ge2\), \(d_T(q,p)=d_Qq+f_0p\) for \(n=1\), and augmentation \(Q_0\to C_0\to M\). The identities defining \(f\) give \(d_T^2=0\). It is exact. In degree two, a cycle \((q,p)\) has \(d_Pp=0\), so \(p=0\), and \(q\) is a boundary in \(Q_\bullet\); the same holds in higher degrees. In degree one, if \(d_Qq+f_0p=0\), then the image of \(p\) in \(K\) has zero image in \(C_0\), so \(p=d_Pp_1\); then \(q+f_1p_1\) is a \(Q\)-cycle, equal to \(d_Qq_2\), and \((q,p)=d_T(q_2,-p_1)\). In degree zero, an element with zero image in \(M\) has image in \(K\); subtract a suitable \(f_0p\) and lift the rest through \(d_Q\). So \(T_\bullet\) is a free resolution of \(M\).

The inclusion \(Q_\bullet\to T_\bullet\) lifts \(C_0\to M\). A degree-two cocycle \(\phi:Q_2\to M\) extends to \(\psi(q,p)=\phi(q)\) on \(T_2=Q_2\oplus P_1\), still a cocycle since \(T_3=Q_3\) and \(d_T\) on \(T_3\) has no \(P_1\) component. So
\[
\begin{gathered}
\operatorname{Ext}^2_A(M,M)\\
\longrightarrow\operatorname{Ext}^2_A(C_0,M)
\end{gathered}\tag{4.2}
\]
is onto. The isomorphism
\[
\begin{gathered}
\operatorname{Hom}_A(A\otimes_B\mathcal B_n(\mathsf H),M)\\
\to\operatorname{Hom}_B(\mathcal B_n(\mathsf H),M),\\
\phi\mapsto\bigl(b\mapsto\phi(1\otimes b)\bigr),
\end{gathered}
\]
with inverse \(\eta\mapsto(a\otimes b\mapsto a\eta(b))\), commutes with the boundaries, and the extra free summand \(A\) in degree zero contributes no cohomology in degree two; so the target of (4.2) is \(H^2(B\mathsf H;\mathbb Z)\).

It remains to identify (4.2) with restriction. Choose a comparison map \(T_\bullet\to\mathcal B_\bullet(\Gamma)\) lifting the identity of \(M\) (Lemma 2.1). The composite \(I_\bullet\to Q_\bullet\to T_\bullet\to\mathcal B_\bullet(\Gamma)\) lifts the augmentation \(A\otimes_BM\to M\), and so does
\[
\theta\bigl(a\otimes(h_0,\ldots,h_n)\bigr)=a\,(h_0,\ldots,h_n),
\]
the tuple read in \(\Gamma\). By Lemma 2.1 the two lifts are homotopic. After the isomorphism above, precomposition with \(\theta\) restricts a \(\Gamma\)-cochain to tuples of \(\mathsf H\), which is the pull-back along \(B\mathsf H\to B\Gamma\). So (4.2) is (4.1). \(\square\)

## 5. The detector

**Proposition 5.1** (torsion-freeness and the integral detector; [OpenAI-BCI, Proposition 7.11]). The graphical group \(\Gamma\) is torsion-free. The homomorphism \(i_\Gamma:\mathbb Z^2\to\Gamma\) sending the ordered basis to \((z,x)\) is injective, and there is \(c_\Gamma\in H^2(B\Gamma;\mathbb Z)\) with
\[
\bigl\langle(Bi_\Gamma)^*c_\Gamma,[T^2]\bigr\rangle=-1 .\tag{5.1}
\]

*Proof.* Lemma 2.2 gives torsion-freeness. The embedding \(\mathsf H\le\Gamma\) of Proposition 5.1 of the lesson on the graphical group and \(z^ux^v=(v,0,u)\) give injectivity of \(i_\Gamma\). Choose \(c_\Gamma\) mapping to \(c_{\mathsf H}\) under the surjection of Lemma 4.1; that map is restriction, so Lemma 3.1 gives (5.1). \(\square\)

## 6. Exercises

**Exercise 6.1.** Verify the cocycle identity of Lemma 3.1 directly for \(g=h=k=x\).

**Exercise 6.2.** In the central extension defined by \(\omega\), with multiplication \((t,g)(t',h)=(t+t'+\omega(g,h),gh)\), show that \(X=(0,x)\) and \(Z=(0,z)\) satisfy \([X,Z]=T\) with \(T=(1,1)\), and that \(Y=(0,y)\) commutes with \(Z\).

**Exercise 6.3.** Why does the proof of Lemma 2.2 need the free action on cells of every dimension, and not only on vertices?

**Exercise 6.4.** Show that \(H^2(B\mathbb Z^2;\mathbb Z)\cong\mathbb Z\), generated by a class taking the value \(\pm1\) on \([T^2]\), using the bar cochain \(\omega_0((u,v),(u',v'))=uv'\) on \(\mathbb Z^2\).

## 7. Solutions

**6.1.** With \(x=(1,0,0)\): \(x^2=(2,0,0)\), \(\omega(x,x)=1\cdot0+\binom12\cdot0=0\), and \(\omega(x^2,x)=0\); both sides vanish because \(\beta=\gamma=0\) throughout.

**6.2.** In matrix coordinates \(x=(1,0,0)\), \(y=(0,1,0)\), \(z=(0,0,1)\). Then \(\omega(x,z)=1\cdot1=1\) and \(\omega(z,x)=0\), so \(XZ=(1,xz)\) and \(ZX=(0,zx)=(0,xz)\). Hence \(XZ=T\cdot ZX\) with \(T=(1,1)\), which is central because \(\omega\) vanishes when an argument is the identity; that is, \([X,Z]=XZ(ZX)^{-1}=T\). Also \(\omega(y,z)=0\cdot1=0\) and \(\omega(z,y)=0\), so \(YZ=(0,yz)=(0,zy)=ZY\).

**6.3.** Freeness of a \(\mathbb F_p[P]\)-module of chains requires that \(P\) permute the cells of that dimension without fixed cells; a fixed edge or triangle would give a non-free summand \(\mathbb F_p\) in \(C_1\) or \(C_2\), and the chain complex would not be a free resolution.

**6.4.** For \(\Lambda=\mathbb Z^2\) the cocycle \(\omega_0\) is the bilinear form \(uv'\); on \([z|x]-[x|z]\) with \(z=(1,0)\), \(x=(0,1)\) it gives \(1\cdot1-0\cdot0=1\). Bilinear forms are cocycles, and \(H^2(B\mathbb Z^2;\mathbb Z)=H^2(T^2;\mathbb Z)\cong\mathbb Z\) by (BG), since the torus is a \(K(\mathbb Z^2,1)\); the class of \(\omega_0\) evaluates to \(1\) on the fundamental class, so it generates.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 7.4-7.7, Lemmas 7.6-7.10, Proposition 7.11. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press 2002, author's edition, Section 1.B (Example 1B.7, Theorem 1B.8) and Theorem 3.5. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
