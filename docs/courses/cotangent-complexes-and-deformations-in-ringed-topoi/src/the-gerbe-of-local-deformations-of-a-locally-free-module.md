# The gerbe of local deformations of a locally free module

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

Let \(B\to R\) be a surjection of rings of a topos \(T\) whose kernel \(I\) has square zero, and \(M\) an \(R\)-module. Put \(N=I\otimes_RM\).

- Local extensions of \(M\) by \(N\) over \(B\) on which \(I\) acts through the identity form groupoids. Their automorphisms are the sections of \(H=\mathcal Hom_R(M,N)\).
- When \(M\) is finite locally free, these groupoids are locally nonempty and locally connected, and they have a class in \(H^2(T,H)\).
- The canonical class \(\omega(B,M)\) of the lesson on deformations of modules lies in \(\operatorname{Ext}^2_R(M,N)\), which is the same group.
- Both classes vanish exactly when \(M\) has a global deformation. This cannot fix their relation, because \(x\) and \(-x\) vanish together.

With every convention fixed, this lesson proves that the class of the gerbe is \(-\omega(B,M)\). This answers the question recorded in Remark 3.6 of that lesson.

Both classes are represented by one cocycle \(\theta\) of an injective resolution of \(N\). The gerbe is presented by splittings of an extension built from the resolution, and its cocycle on any hypercovering is cohomologous to \(+\theta\). A homotopy on a three-term complex representing the truncation of \(M\otimes^{\mathbf L}_BR\) gives \(\omega(B,M)=-\theta\). On the quadric surface over \(\mathbf Z\) the class is a generator of \(\mathbf Z\), so the sign cannot be dropped.

**Prerequisites.**
- [*Deformations of modules and of their morphisms*](deformations-of-modules-and-of-their-morphisms.md): Conventions, Definition 1.1, Lemma 1.2, Lemma 2.1, Definition 2.2, Theorems 2.3, 3.2 and 3.10, Example 3.11, and the proofs of Propositions 3.8 and 5.6 (2).
- [*Graded modules and the graded cotangent complex*](graded-modules-and-the-graded-cotangent-complex.md): Proposition 1.5 (3), with every grading trivial, and the proof of Lemma 4.3 (2), which shows that restriction to a slice preserves injective modules.
- From the AI-integrated Stacks project:
  - the cone [[Stacks, Tag 014E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-definition-cone)];
  - triangles of short exact sequences [[Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)];
  - Hom complexes into bounded below complexes of injectives [[Tag 05TG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-into-injective-complex)];
  - right adjoints of exact functors preserve injectives [[Tag 015Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-adjoint-preserve-injectives)];
  - bounded above flat complexes are K-flat [[Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat)].

## Conventions

**Rings and modules.** \(T\) is a topos with final object \(\ast\), and \(T=\operatorname{Sh}(\mathcal C)\) for a small site \(\mathcal C\); objects of \(\mathcal C\) are identified with their sheafified representables.

- The map \(B\to R\) is a surjection of rings of \(T\) with kernel \(I\) and \(I^2=0\), and \(f\colon(T,R)\to(T,B)\) is as in the lesson on deformations.
- For an object \(U\), \(F|_U\) is the restriction to \(T/U\), with \(F|_U(V\to U)=\operatorname{Hom}(V,F)\); it is strictly functorial in \(U\). We write \(\Gamma(U,F)=\operatorname{Hom}_T(U,F)\).
- Put \(N=I\otimes_RM\) and \(H=\mathcal Hom_R(M,N)\), the internal Hom.
- \(M\) is *finite locally free* if \(\ast\) is covered by objects \(U\) with \(M|_U\cong R|_U^{r}\), where \(r\) may depend on \(U\). Such an \(M\) is flat.
- \(H^n(T,F)\) is cohomology computed in \(R\)-modules.

**Lemma 0.1.** For \(R\)-modules \(A,M,F\) there is a natural isomorphism
\[
\begin{aligned}&\operatorname{Hom}_R(A,\mathcal Hom_R(M,F))\\&\quad \cong\operatorname{Hom}_R(A\otimes_RM,F).\end{aligned}
\]
If \(M\) is flat and \(F\) injective, then \(\mathcal Hom_R(M,F)\) is injective.

**Proof.** A map \(A\to\mathcal Hom_R(M,F)\) is a family of maps \(A(U)\to\operatorname{Hom}_{R|_U}(M|_U,F|_U)\), compatible with restriction. Equivalently, it is a compatible family of \(R\)-bilinear maps \(A(U)\times M(U)\to F(U)\), that is, a map of presheaves from the presheaf tensor product to \(F\). By the universal property of sheafification this is a map \(A\otimes_RM\to F\). If \(M\) is flat, \(-\otimes_RM\) is exact, so its right adjoint \(\mathcal Hom_R(M,-)\) preserves injectives [Tag 015Z]. \(\square\)

**Cones and triangles.** For a map \(\alpha\colon A\to C\) of complexes, \(\operatorname{Cone}(\alpha)^n=C^n\oplus A^{n+1}\) with \(d(c,a)=(dc+\alpha(a),-da)\) [Tag 014E]. A short exact sequence \(0\to A\to C\to D\to0\) gives the triangle \(A\to C\to D\to A[1]\), whose third map is \(-\mathrm{pr}\circ q^{-1}\) [Tag 0152]. Here \(q\colon\operatorname{Cone}\to D\) is the quasi-isomorphism and \(\mathrm{pr}\colon\operatorname{Cone}\to A[1]\) the projection. On cohomology this third map is the connecting map: lift a cocycle and apply the differential.

For a complex \(Y\) with cohomology in degrees \(-1,0\), the truncation triangle of Definition 2.2 of the lesson on deformations is read as the triangle of
\[
0\to\tau_{\le-1}Y\to Y\to\tau_{\ge0}Y\to0,
\]
with \(\tau_{\le-1}Y\simeq H^{-1}(Y)[1]\) and \(\tau_{\ge0}Y\simeq H^0(Y)\). This triangle is natural in \(Y\).

**Čech cochains.** A *semi-simplicial object* \(K\) consists of objects \(K_p\) (\(p\ge0\)) and maps \(d_i\colon K_p\to K_{p-1}\) (\(0\le i\le p\)) with \(d_id_j=d_{j-1}d_i\) for \(i<j\).

- For a module \(F\), put \(C^p(K,F)=\Gamma(K_p,F)\) and \(\check\delta=\sum_i(-1)^id_i^*\).
- For a complex \(F^\bullet\), \(\operatorname{Tot}C^\bullet(K,F^\bullet)\) has the differential \(D=\check\delta+(-1)^pd\).
- With vertices numbered, \(\check\delta s=s_1-s_0\) and \(\check\delta a=a_{12}-a_{02}+a_{01}\).

**The deformation groupoids.** For an object \(U\), \(\mathcal G(U)\) is the groupoid of extensions \(0\to N|_U\xrightarrow{i}L\xrightarrow{p}M|_U\to0\) of \(B|_U\)-modules with \(u(L)=1_N\) (Definition 1.1 of the lesson on deformations). Its morphisms are the isomorphisms of extensions inducing the identity on \(N\) and on \(M\). The *band* is \(h\mapsto1+ihp\) (Lemma 1.1). The class below uses only presentations (Definition 1.5); no stack property of \(\mathcal G\) is used.

## 1. Hypercoverings and the class of a presentation

**Lemma 1.1 (the band).** Let \(L\in\mathcal G(U)\). The map \(h\mapsto1_L+ihp\) is an isomorphism from \(H(U)\) onto the group of automorphisms of \(L\) in \(\mathcal G(U)\). For every morphism \(\psi\colon L\to L'\) of \(\mathcal G(U)\), \(\psi(1+ihp)\psi^{-1}=1+ihp\).

**Proof.** Let \(\varphi\) be an automorphism. Then \(\varphi-1\) kills \(i(N)\) and lands in \(\ker p=i(N)\). So \(\varphi-1=ihp\) for a unique \(h\colon M|_U\to N|_U\), which is \(B\)-linear between \(R\)-modules, hence \(R\)-linear.

Since \(pi=0\), we have \((1+ihp)(1+ih'p)=1+i(h+h')p\). So \(1+ihp\) is invertible with inverse \(1-ihp\), and \(h\mapsto1+ihp\) is a homomorphism; it is injective because \(i\) is a monomorphism and \(p\) an epimorphism. Finally \(\psi i=i\) and \(p\psi^{-1}=p\). \(\square\)

**Definition 1.2.** Let \(K\) be a semi-simplicial object. For \(p\ge0\), let \(M_{p+1}K\subseteq K_p^{p+2}\) be the subobject of the families \((b_0,\dots,b_{p+1})\) with \(d_ib_j=d_{j-1}b_i\) for \(i<j\); thus \(M_1K=K_0\times K_0\). The map \(K_{p+1}\to M_{p+1}K\), \(\sigma\mapsto(d_i\sigma)_i\), is well defined. \(K\) is a *hypercovering* if \(K_0\to\ast\) and all the maps \(K_{p+1}\to M_{p+1}K\) are epimorphisms.

For a sheaf of sets \(X\), \(R[X]\) is the sheafification of \(V\mapsto R(V)^{(X(V))}\), so that \(\operatorname{Hom}_R(R[X],F)=\Gamma(X,F)\). The modules \(R[K_p]\), with \(d=\sum_i(-1)^id_i\), form a complex augmented to \(R=R[\ast]\).

**Lemma 1.3.** For a hypercovering \(K\), the augmented complex \(\cdots\to R[K_1]\to R[K_0]\to R\to0\) is exact.

**Proof.** The augmentation is an epimorphism, because \(K_0\to\ast\) is one.

*Setting up.* Let \(z\) be a section of \(R[K_n]\) over \(V\) such that \(dz=0\) if \(n\ge1\), or such that its augmentation is \(0\) if \(n=0\). After an epimorphism \(V'\to V\), \(z\) is a finite sum \(\sum_kr_k[x_k]\) with \(x_k\in K_n(V')\), and the relation on \(z\) holds in \(R(V')^{(K_\bullet(V'))}\). Let \(\Phi\) be the finite set of the \(x_k\) and of all their iterated faces. Choose an epimorphism \(V_0\to V'\) and \(c_\ast\in K_0(V_0)\). All further epimorphisms are taken over \(V_0\), and sections are restricted along them.

*The elements \(c(y)\).* By induction on \(m\), after an epimorphism \(V''\to V_0\) we find \(c(y)\in K_{m+1}(V'')\) for \(y\in\Phi\cap K_m\), with
\[
\begin{gathered}d_0c(y)=y,\quad d_1c(y)=c_\ast\ (m=0),\\ d_ic(y)=c(d_{i-1}y)\ (i\ge1,\ m\ge1).\end{gathered}
\]
For \(m=0\), the family \((y,c_\ast)\) lies in \(M_1K\). For \(m\ge1\), the family \((y,c(d_0y),\dots,c(d_my))\) lies in \(M_{m+1}K\):
- for \(0<j\), \(d_0c(d_{j-1}y)=d_{j-1}y\);
- for \(1\le i<j\) and \(m\ge2\), \(d_ic(d_{j-1}y)=\) \(c(d_{i-1}d_{j-1}y)=\) \(c(d_{j-2}d_{i-1}y)=\) \(d_{j-1}c(d_{i-1}y)\);
- for \(m=1\), both sides equal \(c_\ast\).

Each family lifts along the epimorphism \(K_{m+1}\to M_{m+1}K\) after an epimorphism, and \(\Phi\) is finite.

*The contraction.* Put \(h[y]=[c(y)]\) on \(R(V'')^{(\Phi)}\). For \(m\ge1\),
\[
\begin{aligned}dh[y]&=[y]+\textstyle\sum_{i\ge1}(-1)^i[c(d_{i-1}y)]\\&=[y]-h(d[y]),\end{aligned}
\]
and \(dh[y]=[y]-[c_\ast]\) for \(m=0\). If \(n\ge1\), then \(h(dz)=0\) gives \(z=dh(z)\). If \(n=0\), then \(z=dh(z)+(\sum_kr_k)[c_\ast]=dh(z)\). \(\square\)

**Lemma 1.4.** Let \(K\) be a hypercovering and \(L^\bullet\) a complex of injective \(R\)-modules in degrees \(\ge0\). Restriction along \(K_0\to\ast\) into the column \(p=0\) is a quasi-isomorphism \(\Gamma(\ast,L^\bullet)\to\operatorname{Tot}C^\bullet(K,L^\bullet)\). This map is natural in \(L^\bullet\).

**Proof.** The map is a map of complexes, because the two maps \(K_1\to\ast\) agree. Adjoin \(\Gamma(\ast,L^q)\) as a column \(p=-1\). With \(D=\check\delta+(-1)^pd\), the total complex of the enlarged double complex is the cone of the map. Each row \(0\to\Gamma(\ast,L^q)\to\Gamma(K_0,L^q)\to\cdots\) is \(\operatorname{Hom}_R(-,L^q)\) of the complex of Lemma 1.3, hence exact.

Let \(z\) be a cycle of degree \(n\), with components \(z_p\) for \(-1\le p\le n\), and let \(p_1\) be the largest \(p\) with \(z_p\ne0\). The component of \(Dz\) in bidegree \((p_1+1,n-p_1)\) is \(\check\delta z_{p_1}=0\).
- If \(p_1=-1\), exactness of the row gives \(z_{-1}=0\).
- If \(p_1\ge0\), then \(z_{p_1}=\check\delta w\), and \(z-Dw\) has components only in columns \(p<p_1\).

By induction, every cycle of the cone is a boundary. \(\square\)

**Definition 1.5 (the class of a presentation).** A *presentation* of \(\mathcal G\) is a triple \((K,x,\varphi)\) of a hypercovering \(K\), an object \(x\in\mathcal G(K_0)\) and a morphism \(\varphi\colon d_0^*x\to d_1^*x\) of \(\mathcal G(K_1)\).

Let \(x_0,x_1,x_2\) be the restrictions of \(x\) to \(K_2\) along the vertex maps \(d_1d_1\), \(d_1d_0\) and \(d_0d_0\). Then \(d_2^*\varphi\colon x_1\to x_0\), \(d_0^*\varphi\colon x_2\to x_1\) and \(d_1^*\varphi\colon x_2\to x_0\). By Lemma 1.1 there is a unique \(c\in\Gamma(K_2,H)\) with
\[
(d_2^*\varphi)(d_0^*\varphi)=(1+icp)(d_1^*\varphi).
\]
If \(\check\delta c=0\), let \(H\xrightarrow{j_L}L^\bullet\) be an injective resolution. Then \(j_Lc\) is a cycle of degree \(2\) of \(\operatorname{Tot}C^\bullet(K,L^\bullet)\). The *class* of \((K,x,\varphi)\) is the element of \(H^2(T,H)=H^2\Gamma(\ast,L^\bullet)\) that Lemma 1.4 carries to \([j_Lc]\).

The class does not depend on \(L^\bullet\). A map \(L^\bullet\to L'^\bullet\) over \(1_H\) exists and is unique up to homotopy [Tag 05TG]. It commutes with both augmentations, and Lemma 1.4 is natural in \(L^\bullet\).

## 2. A model of the deformation groupoids

**2.0. Setting.** In this section \(M\) is any \(R\)-module.
- By Proposition 1.5 (3) of the lesson on graded modules, choose an epimorphism \(F\to M\) of \(B\)-modules with \(F\) flat, with kernel \(Z\). Continuing gives a flat resolution \(G^\bullet\to M\) with \(G^0=F\), which computes \(Lf^*M=G^\bullet\otimes_BR\) [Tag 06YQ].
- Put \(P=F/IF\) and \(Q=Z/IZ\). Let \(v\colon Q\to P\) and \(\rho\colon P\to M\) be the induced maps, and \(C=[Q\xrightarrow{v}P]\) in degrees \(-1,0\).
- Choose an injective resolution \(N\xrightarrow{j}J^\bullet\) in \(R\)-modules.

**Lemma 2.1.**
1. The differential \(G^{-1}\to Z\) induces an isomorphism \(\tau_{\ge-1}(G^\bullet\otimes_BR)\to C\), equal to the identity in degree \(0\).
2. Through (1), the map \(\gamma\) of Lemma 2.1 of the lesson on deformations is
\[
\begin{aligned}&n \colon N \to Q,\quad x\otimes m\\&\quad \mapsto x\tilde m\bmod IZ,\end{aligned}
\]
with \(\tilde m\in F\) a local lift of \(m\). So \(n\) is injective with image \(\ker v\).
3. Let \(W=[N\xrightarrow{n}Q\xrightarrow{v}P]\) in degrees \(-2,-1,0\). Let \(q\colon W\to M\) be \(\rho\) in degree \(0\), and \(r\colon W\to N[2]\) the identity in degree \(-2\). Then \(q\) is a quasi-isomorphism and
\[
\omega(B,M)=-r\circ q^{-1}\quad\text{in }D(R).
\]

**Proof.** (1) The degree \(-1\) term of \(\tau_{\ge-1}\) is \(G^{-1}/(IG^{-1}+dG^{-2})\), and \(d\colon G^{-1}\to Z\) is onto. If \(dg=\sum x_\nu z_\nu\in IZ\), write locally \(z_\nu=dg_\nu\). Then \(g-\sum x_\nu g_\nu\in\ker d=dG^{-2}\) locally, so the induced map to \(Q\) is injective.

(2) The map \(n\) is well defined: \(x\tilde m\in Z\) because \(IM=0\), and changing \(\tilde m\) by an element of \(Z\) changes \(x\tilde m\) by an element of \(IZ\). The rule is balanced over \(R\).

The map \(\delta_I\) is the connecting map of \(0\to G\otimes_BI\to G\to G\otimes_BR\to0\), which is exact because the \(G^n\) are flat. Write locally \(x\tilde m=dg\) with \(g\in G^{-1}\); then \(\bar g\) is a cycle of \(G\otimes_B R\). Lifting \(\bar g\) to \(g\) and applying \(d\) gives \(x\tilde m\in IF=F\otimes_BI\), whose class in \(M\otimes_BI\) is \(m\otimes x\). So \(\gamma(x\otimes m)=[\bar g]\). Under (1), this class goes to \(dg\bmod IZ=n(x\otimes m)\).

By Lemma 2.1 (1) there, \(\gamma\) is an isomorphism onto \(H^{-1}(C)=\ker v\).

(3) The sequence \(0\to N\to Q\to P\to M\to0\) is exact by (2), because \(\operatorname{coker}v=F/(Z+IF)=M\), so \(q\) is a quasi-isomorphism. By (2), \(n\) gives an isomorphism of complexes \(N[1]\to\tau_{\le-1}C=[\ker v\to0]\). Hence the sequence \(0\to N[1]\to C\to\tau_{\ge0}C\to0\) is isomorphic to the truncation sequence.

The cone of \(N[1]\to C\) is \(W\), with differential \(+n\) in degree \(-2\). Its quasi-isomorphism to \(\tau_{\ge0}C\simeq M\) is \(q\), and its projection to \(N[2]\) is \(r\). So the third map of the truncation triangle, read through \(n=\gamma\), is \(-r\circ q^{-1}\). By Definition 2.2 there, \(\omega=\gamma^{-1}[2]\circ\kappa=-r\circ q^{-1}\). \(\square\)

**Construction 2.2.** Since \(J^0\) is injective and \(n\) is a monomorphism, there is an \(R\)-linear \(\lambda\colon Q\to J^0\) with \(\lambda n=j\).

- Let \(X\) be the pushout of the extension \(0\to Q\to F/IZ\to M\to0\) along \(\lambda\). It is an extension of \(M\) by \(J^0\) over \(B\).
- By its definition, \(u(F/IZ)=n\). So \(u(X)=\lambda n=j\) and \(IX=j(N)\) (Lemma 1.2 (4), (1) there).
- Put \(A_0=J^0/jN\) and \(E=X/jN\). These are \(R\)-modules, with an exact sequence
\[
0\to A_0\xrightarrow{k}E\xrightarrow{\pi}M\to0.
\]
- The map \(F\to X\to E\) kills \(IF\), so it induces \(t\colon P\to E\) with \(\pi t=\rho\) and \(tv=k\bar\lambda\), where \(\bar\lambda\) is \(\lambda\) modulo \(jN\).
- \(d^0\) induces an injection \(\bar d^0\colon A_0\to J^1\). By injectivity of \(J^1\), extend it to \(g\colon E\to J^1\) with \(gk=\bar d^0\).
- Since \(d^1gk=0\), there is a unique \(\theta\colon M\to J^2\) with \(\theta\pi=d^1g\). Then \(d^2\theta=0\), because \(\pi\) is an epimorphism.

**Lemma 2.3.** In \(\operatorname{Hom}_{D(R)}(M,J^\bullet[2])=\) \(H^2\operatorname{Hom}_R(M,J^\bullet)\) [Tag 05TG],
\[
j[2]\circ\omega(B,M)=[-\theta].
\]

**Proof.** Define \(s\) of degree \(-1\) from \(W\) to \(J^\bullet[2]\) by \(s=\lambda\) on \(Q\), \(s=-gt\) on \(P\) and \(s=0\) on \(N\). Then \(ds+sd\) is:
- \(\lambda n=j\) in degree \(-2\);
- \(d^0\lambda-gtv=d^0\lambda-gk\bar\lambda=0\) in degree \(-1\);
- \(-d^1gt=-\theta\pi t=-\theta\rho\) in degree \(0\).

So \(j[2]\circ r-\theta\circ q=ds+sd\), and \(j[2]\circ r\circ q^{-1}=\theta\). Lemma 2.1 (3) gives \(j[2]\circ\omega=-\theta\). \(\square\)

**Proposition 2.4 (splittings).** Let \(U\) be an object of \(T\).
1. For an \(R\)-linear section \(s\) of \(\pi\) over \(U\), let \(X_s\subseteq X|_U\) be the inverse image of \(s(M)\). With \(i=j\), \(X_s\) is an object of \(\mathcal G(U)\).
2. The morphisms \(X_s\to X_t\) of \(\mathcal G(U)\) correspond bijectively to the \(a\in\Gamma(U,\mathcal Hom_R(M,J^0))\) with \(k\bar a=t-s\), through \(z\mapsto z+a(p(z))\), where \(\bar a\) is \(a\) modulo \(jN\). Composition adds the maps \(a\), and \(a=jh\) gives \(1+ihp\). This correspondence commutes with restriction.
3. Every object of \(\mathcal G(U)\) is isomorphic to some \(X_s\).
4. If \(M\) is finite locally free, then sections \(s\) exist locally, and for sections \(s,t\) over \(U\), maps \(a\) with \(k\bar a=t-s\) exist locally on \(U\).

**Proof.** (1) The submodule \(X_s\) contains \(jN=\ker(X\to E)\). If an element of \(X_s\) maps to \(0\) in \(M\), its image \(s(m)\) in \(E\) has \(m=0\). So \(\ker(X_s\to M)=jN\). Since \(s(m)\) lifts locally to \(X\), the map \(X_s\to M\) is onto. Lifts in \(X_s\) are lifts in \(X\), so \(u(X_s)=j\).

(2) Let \(\varphi\) be such a morphism. Then \(\varphi\) minus the inclusion kills \(jN\) and lands in \(\ker(X\to M)=J^0\). So it is \(a\circ p\) for an \(R\)-linear \(a\). The image of \(z\) in \(E\) is \(s(pz)\) and that of \(\varphi(z)\) is \(t(pz)\), which gives \(k\bar a=t-s\). Conversely, such an \(a\) gives a map into \(X_t\) inducing the identities on \(N\) and \(M\), hence an isomorphism. Composites add because \(p\circ a=0\).

(3) Let \(L\in\mathcal G(U)\). The pushout \(j_*L\) and \(X|_U\) are extensions of \(M\) by \(J^0\) with \(u=j\). Their Baer difference has \(u=0\), so it lies in \(\operatorname{Ext}^1_{R|_U}(M|_U,J^0|_U)\) (Lemma 1.2 (3) there). This group is zero, because \(J^0|_U\) is injective.

Choose an isomorphism \(j_*L\cong X|_U\) of extensions. The composite \(L\to j_*L\cong X|_U\) is injective, with image \(L'\) satisfying \(L'\cap J^0=jN\) and \(L'\to M\) onto. The image of \(L'\) in \(E\) is an \(R\)-submodule mapped isomorphically onto \(M\) by \(\pi\), that is, \(s(M)\) for an \(R\)-linear section \(s\). Then \(L'\subseteq X_s\), and the two are equal by the five lemma.

(4) Where \(M\cong R^r\), a basis lifts locally through the epimorphism \(\pi\), which gives \(s\). Also \(t-s\) lands in \(k(A_0)\), and the images of a local basis lift locally through \(J^0\to A_0\). \(\square\)

## 3. The comparison theorem

**Theorem 3.1.** Let \(M\) be a finite locally free \(R\)-module and \(\mathcal K^q=\mathcal Hom_R(M,J^q)\).
1. \(\mathcal G\) is locally nonempty and locally connected, Lemma 1.1 bands it by \(H\), and presentations of \(\mathcal G\) exist.
2. \(\mathcal K^\bullet\) is an injective resolution of \(H\). The equality \(\Gamma(\ast,\mathcal K^q)=\operatorname{Hom}_R(M,J^q)\) gives an isomorphism \(\iota\colon H^2(T,H)\to\operatorname{Ext}^2_R(M,N)\).
3. Every presentation has \(\check\delta c=0\), and its class \([\mathcal G]\) satisfies
\[
\iota([\mathcal G])=-\omega(B,M).
\]
In particular \([\mathcal G]\) does not depend on the presentation.

**Proof.** (1) The first statement follows from Proposition 2.4 (3), (4) and Lemma 1.1.

*A presentation.* Let \(\mathcal C_0\) be the set of the \(U\in\mathcal C\) over which \(\pi\) has a section, and choose a section \(s_U\) for each. By Proposition 2.4 (4), \(\mathcal C_0\) covers \(\ast\), so \(K_0=\coprod_{U\in\mathcal C_0}U\to\ast\) is an epimorphism. The \(s_U\) define a section \(s\) of \(\pi\) over \(K_0\), by the universal property of the coproduct. Put \(x=X_s\).

Let \(K_1\subseteq K_0\times K_0\times\mathcal Hom_R(M,J^0)\) be the subobject of the triples \((v_0,v_1,a)\) with \(k\bar a=s(v_1)-s(v_0)\), with \(d_0(v_0,v_1,a)=v_1\) and \(d_1(v_0,v_1,a)=v_0\). By Proposition 2.4 (4), \(K_1\to K_0\times K_0\) is an epimorphism. Let \(\varphi\) be the morphism given by the tautological \(a\) (Proposition 2.4 (2)).

For \(p\ge2\), let \(K_p\) be the object of the families of vertices \((v_0,\dots,v_p)\) and edges \((v_a,v_b,a_{ab})\in K_1\) for \(a<b\), with \(d_i\) deleting the index \(i\). For \(p\ge2\) the maps \(K_p\to M_pK\) are isomorphisms, both sides being compatible families of vertices and edges.

(2) The functor \(\mathcal Hom_R(M,-)\) is exact, because this holds locally where \(M\) is free. It preserves injectives (Lemma 0.1). So \(\mathcal K^\bullet\) resolves \(\mathcal Hom_R(M,N)=H\), and
\[
\begin{aligned}&\iota \colon H^2\Gamma(\ast,\mathcal K^\bullet)\\&\quad =H^2\operatorname{Hom}_R(M,J^\bullet)\\&\quad =\operatorname{Ext}^2_R(M,N)\end{aligned}
\]
by [Tag 05TG].

(3) *Transport to the model.* By Proposition 2.4 (3), choose a section \(s\) of \(\pi\) over \(K_0\) and an isomorphism \(\psi\colon x\to X_s\). Put \(\varphi'=(d_1^*\psi)\varphi(d_0^*\psi)^{-1}\). Write \(\psi_k\) for the restrictions of \(\psi\) to the vertices of \(K_2\). Then
\[
(d_2^*\varphi')(d_0^*\varphi')=\psi_0(1+icp)\psi_0^{-1}(d_1^*\varphi'),
\]
and Lemma 1.1 shows that \(\varphi'\) has the same cocycle \(c\).

*The cocycle as a coboundary.* By Proposition 2.4 (2), \(\varphi'\) corresponds to \(a\in\Gamma(K_1,\mathcal K^0)\) with \(k\bar a=d_1^*s-d_0^*s\). Since composition adds the maps \(a\), the defining identity reads \(d_2^*a+d_0^*a=jc+d_1^*a\), that is,
\[
jc=\check\delta a.
\]
Hence \(\check\delta c=0\), \(j\) being a monomorphism.

*The total complex.* Put \(w=gs\in\Gamma(K_0,\mathcal K^1)\). Then
\[
\begin{gathered}da=\bar d^0\bar a=gk\bar a=-\check\delta w,\\ dw=d^1gs=\theta\pi s=\theta|_{K_0}.\end{gathered}
\]
So
\[
\begin{aligned}D(a-w)&=\check\delta a-da-\check\delta w-dw\\&=jc-\theta|_{K_0}.\end{aligned}
\]
For \(L^\bullet=\mathcal K^\bullet\), Lemma 1.4 therefore gives the class \([\theta]\), and Lemma 2.3 gives \(\iota[\theta]=-\omega(B,M)\). \(\square\)

**Corollary 3.2 (the Atiyah form).** For every map of rings \(A\to B\),
\[
\iota([\mathcal G])=-(e(B)\otimes1_M)[1]\circ\operatorname{at}_{R/A}(M).
\]

**Proof.** Apply Theorem 3.2 of the lesson on deformations, where the final projection is the identity because \(M\) is flat, together with Theorem 3.1. \(\square\)

**Corollary 3.3.** In the situation of Theorem 3.10 of the lesson on deformations, put \(\mathcal N=\mathcal I/\mathcal I^2\). Let \(L\) be a locally free \(\mathcal O_Y\)-module of finite rank, and \(\mathcal G_L\) the groupoids of Section 1 for \(B=\mathcal O_{Y_1}\), \(R=\mathcal O_Y\) and \(M=L\). Then, in \(H^2(Y,\mathcal End(L)\otimes\mathcal N)\) computed in \(\mathcal O_Y\)-modules,
\[
[\mathcal G_L]=\partial\operatorname{at}_{Y/S}(L).
\]

**Proof.** The identification \(\operatorname{Ext}^2(L,\mathcal N\otimes L)=H^2(Y,\mathcal End(L)\otimes\mathcal N)\) used there is induced by \(\mathcal Hom(L,-)\) on an injective resolution (proof of Proposition 3.8 there), that is, by \(\iota\). Theorem 3.10 (3) there gives \(\omega(i,L)=-\partial\operatorname{at}_{Y/S}(L)\), and Theorem 3.1 gives \(\iota[\mathcal G_L]=-\omega(i,L)\). \(\square\)

**Example 3.4 (the sign is detected).** In Example 3.11 of the lesson on deformations, \(H^2(Y,\mathcal N)\cong\mathbf Z\) with basis \(\omega(i,L_1)\). For an invertible \(L\), the isomorphism \(\mathcal N\to\mathcal Hom(L,\mathcal N\otimes L)\), \(y\mapsto(m\mapsto y\otimes m)\), identifies \(H\) with \(\mathcal N\). By Corollary 3.3,
\[
[\mathcal G_{L_1}]=\partial e_1=-\omega(i,L_1),
\]
and \(-\omega(i,L_1)\ne\omega(i,L_1)\) in \(\mathbf Z\). So the relation \(\iota[\mathcal G]=\omega(B,M)\) is false in general.

## 4. Exercises

**Exercise 4.1.** Replace the band by \(h\mapsto1-ihp\), and define the cocycle by the same identity. Show that the class of every presentation becomes \(\iota^{-1}(\omega(B,M))\).

**Exercise 4.2.** In Example 3.4, compute \([\mathcal G_{L_1^{\otimes m}}]\) for \(m\in\mathbf Z\), and \([\mathcal G_{L_1\otimes L_2}]\).

## 5. Complete solutions

**4.1.** The identity reads \((d_2^*\varphi)(d_0^*\varphi)=(1-ic'p)(d_1^*\varphi)\). By uniqueness in Lemma 1.1, \(c'=-c\). The class is therefore \(-[\mathcal G]=\iota^{-1}(\omega(B,M))\) by Theorem 3.1.

**4.2.** By Theorem 3.10 (4) of the lesson on deformations, \(L\mapsto\omega(i,L)\) is a homomorphism on \(\operatorname{Pic}(Y)\). By Corollary 3.3 and Example 3.4:
- \([\mathcal G_{L_1^{\otimes m}}]=-m\,\omega(i,L_1)=m\,\partial e_1\), which is nonzero for \(m\ne0\);
- \([\mathcal G_{L_1\otimes L_2}]=\) \(-\omega(i,L_1)-\omega(i,L_2)=\) \(0\).

The second agrees with the fact that \(L_1\otimes L_2\cong\mathcal O_Y(1)\) extends to \(Y_1\).

## Sources

The canonical class and the question of comparing it with the class of the gerbe of local deformations are due to Illusie, in his work on the cotangent complex. Gerbes and their classes are due to Giraud. A comparison of obstruction gerbes for modules is studied by L. Herr, *Deformations of modules through butterflies and gerbes*, [arXiv:1712.01384](https://arxiv.org/abs/1712.01384). The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026, completed here. The homological algebra is that of the Stacks project.
