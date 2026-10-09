# Locally polynomial algebras

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A finitely presented algebra \(A\) over a ring \(K\) is **locally polynomial** if \(A_{\mathfrak m}\) is a polynomial ring over \(K_{\mathfrak m}\) for every maximal ideal \(\mathfrak m\) of \(K\). Geometrically, \(\operatorname{Spec}A\to\operatorname{Spec}K\) is then a family of affine spaces which is trivial over a neighbourhood \(\operatorname{Spec}K_s\), \(s\notin\mathfrak m\), of every maximal ideal \(\mathfrak m\), by Lemma 2.1(3) of the automorphisms lesson. This lesson proves the theorem of Bass, Connell and Wright: such an algebra is the symmetric algebra of a finitely generated projective module, so the fibre space comes from a vector bundle. With the Quillen–Suslin theorem it follows that over a polynomial ring over a field, every locally polynomial algebra is a polynomial ring.

We use [Patching extended modules](patching-extended-modules.md) (Lemma 1.2, Proposition 3.1), [Horrocks' theorem and the Quillen–Suslin theorem](horrocks-and-quillen-suslin.md) (Lemma 1.1, Theorem 3.2) and [Automorphisms of symmetric algebras](automorphisms-of-symmetric-algebras.md) (Lemma 2.1, Proposition 4.4 and the notation of Section 3); Theorem 2.2 (localizing \(\operatorname{Hom}\)) of [Localization, local properties and support](course:AG-CA/localization-local-properties-and-support#2-relations-survive-localization); and Schanuel's lemma, Lemma 1.1 of [Projective dimension and the Auslander–Buchsbaum formula](course:AG-CA/projective-dimension-and-the-auslander-buchsbaum-formula). Rings and algebras are commutative, and \(K\) is a fixed ring.

## 1. Modules over two localizations

**Lemma 1.1.** Let \(s_0,s_1\in K\) with \(Ks_0+Ks_1=K\).

1. For every \(K\)-module \(E\), every element of \(E_{s_0s_1}\) is the sum of the images of an element of \(E_{s_0}\) and an element of \(E_{s_1}\).
2. Let \(M_i\) be a \(K_{s_i}\)-module (\(i=0,1\)) and \(\varphi\colon(M_0)_{s_1}\to(M_1)_{s_0}\) an isomorphism. Then \(M=\{(m_0,m_1)\in M_0\times M_1:\varphi(m_0)=m_1\text{ in }(M_1)_{s_0}\}\) is a \(K\)-module, and the projections induce isomorphisms \(M_{s_i}\to M_i\) compatible with \(\varphi\).
3. If \(E_{s_0}\) and \(E_{s_1}\) are finitely presented, then \(E\) is finitely presented.
4. If \(S\subseteq K\) is multiplicative, every finitely presented \(K_S\)-module is isomorphic to \(N_S\) for some \(s\in S\) and some finitely presented \(K_s\)-module \(N\).

**Proof.** (1) Write the element as \(x/(s_0s_1)^n\) and \(1=cs_0^n+ds_1^n\). Then \(x/(s_0s_1)^n=cx/s_1^n+dx/s_0^n\), the images of \(cx/s_1^n\in E_{s_1}\) and \(dx/s_0^n\in E_{s_0}\).

(2) Consider \(M\to M_0\). If \((m_0,m_1)\in M\) and \(m_0=0\), then \(m_1\) is zero in \((M_1)_{s_0}\), so \(s_0^km_1=0\) for some \(k\), and \((m_0,m_1)\) is zero in \(M_{s_0}\). Given \(m_0\in M_0\), write \(\varphi(m_0)=m_1'/s_0^k\); then \((s_0^km_0,m_1')\in M\), so \(m_0\) is the image of \((s_0^km_0,m_1')/s_0^k\). Hence \(M_{s_0}\to M_0\) is bijective, and symmetrically, using \(\varphi^{-1}\), so is \(M_{s_1}\to M_1\). The two identifications differ on \(M_{s_0s_1}\) exactly by \(\varphi\).

(3) Choose finitely many elements of \(E\) whose images generate \(E_{s_0}\) and \(E_{s_1}\). The cokernel of the map \(K^n\to E\) they define vanishes after inverting \(s_0\) and after inverting \(s_1\); an element killed by powers of \(s_0\) and of \(s_1\) is zero, so the map is onto. Its kernel \(Z\) satisfies: \(Z_{s_i}\) is the kernel of a surjection from a finitely generated free module onto the finitely presented \(E_{s_i}\), hence finitely generated, by Schanuel's lemma comparing with a finite presentation. The same argument shows that \(Z\) is finitely generated.

(4) A finite presentation matrix over \(K_S\) has entries with a common denominator \(s\in S\); the same matrix over \(K_s\) presents a module \(N\) with \(N_S\) isomorphic to the given one. \(\square\)

**Lemma 1.2.** If \(M,N\) are \(K\)-modules and \(S(M)\cong S(N)\) as \(K\)-algebras, then \(M\cong N\).

**Proof.** Let \(\phi\colon S(M)\to S(N)\) be an isomorphism and \(t=\varepsilon_N\circ\phi|_M\colon M\to K\). With the translation \(\tau_{-t}\) of \(S(M)\), the isomorphism \(w=\phi\circ\tau_{-t}\) maps \(x\in M\) to \(\phi(x)-t(x)\in I_N\). So \(\varepsilon_N\circ w=\varepsilon_M\), hence also \(\varepsilon_M\circ w^{-1}=\varepsilon_N\), and \(w(I_M)=I_N\), \(w(I_M^2)=I_N^2\). Thus \(M\cong I_M/I_M^2\cong I_N/I_N^2\cong N\). \(\square\)

**Lemma 1.3.** Let \(A\) be a finitely presented algebra and \(\varepsilon\colon A\to K\) an algebra homomorphism with kernel \(I\). Then \(I/I^2\) is a finitely presented \(K\)-module. In particular, if \(A\cong S(N)\) for some \(K\)-module \(N\), then \(N\) is finitely presented.

**Proof.** Write \(A=K[X_1,\ldots,X_p]/(f_1,\ldots,f_q)\). After the substitution \(X_i\mapsto X_i+\varepsilon(x_i)\) we may assume \(\varepsilon(x_i)=0\); then \(f_j(0)=0\), and \(I\) is generated by \(x_1,\ldots,x_p\). So \(I/I^2\) is generated by their classes, and a linear form \(\lambda=\sum a_iX_i\) maps to zero exactly when \(\lambda\in(X)^2+(f_1,\ldots,f_q)\), i.e. when \(\lambda\) is the linear part of an element \(\sum g_jf_j\). That linear part is \(\sum g_j(0)\,\ell_j\), where \(\ell_j\) is the linear part of \(f_j\), because \(f_j\) has no constant term. So \(I/I^2\cong K^p/(\ell_1,\ldots,\ell_q)\). For the second assertion, let \(\psi\colon S(N)\to A\) be an isomorphism and \(\varepsilon=\varepsilon_N\circ\psi^{-1}\). Then \(I=\psi(I_N)\), so \(N\cong I_N/I_N^2\cong I/I^2\). \(\square\)

## 2. The theorem

**Theorem 2.1** (Bass–Connell–Wright). Let \(A\) be a finitely presented \(K\)-algebra such that for every maximal ideal \(\mathfrak m\) of \(K\), \(A_{\mathfrak m}\cong S(N_{\mathfrak m})\) as \(K_{\mathfrak m}\)-algebras for some \(K_{\mathfrak m}\)-module \(N_{\mathfrak m}\). Then \(A\cong S(N)\) for a finitely presented \(K\)-module \(N\).

**Proof.** If \(K=0\), then \(A=0=S(0)\); let \(K\ne0\). We apply Quillen induction (Proposition 3.1 of the patching lesson) to the property \(\mathcal P(L)\): *\(A_L\cong S(N)\) as \(L\)-algebras for some finitely presented \(L\)-module \(N\)*, for \(L\in\operatorname{Loc}(K)\).

*Specialization.* \(S(N)\) and finite presentation are compatible with base change.

*Local validity.* This is the hypothesis, together with Lemma 1.3.

*Finiteness.* Let \(A_S\cong S(N)\) with \(N\) finitely presented over \(K_S\). By Lemma 1.1(4), \(N\cong N'_S\) with \(N'\) finitely presented over some \(K_s\), \(s\in S\). The \(K_s\)-algebras \(A_s\) and \(S(N')\) are finitely presented and become isomorphic over \(K_S\), so by Lemma 2.1 of the automorphism lesson (over the ring \(K_s\)) they are isomorphic over \(K_{st}\) for some \(t\in S\).

*Sheaf condition.* Let \(L\in\operatorname{Loc}(K)\) and \(s_0,s_1\in L\) with \(Ls_0+Ls_1=L\); everything below takes place over \(L\), and to simplify notation we write \(K\) for \(L\). We are given finitely presented \(K_{s_i}\)-modules \(M_i\) and isomorphisms \(u_i\colon S(M_i)\to A_{s_i}\).

*Step 1: a global module.* Over \(K_{s_0s_1}\), \(S((M_0)_{s_1})\cong A_{s_0s_1}\cong S((M_1)_{s_0})\), so Lemma 1.2 gives an isomorphism \(\varphi\colon(M_0)_{s_1}\to(M_1)_{s_0}\). Lemma 1.1(2) and (3) give a finitely presented \(K\)-module \(M\) with \(M_{s_i}=M_i\), the identifications differing by \(\varphi\). Put \(B=S(M)\); the \(u_i\) become isomorphisms \(u_i\colon B_{s_i}\to A_{s_i}\).

*Step 2: an affine comparison.* The element \(\theta=(u_0)_{s_1}^{-1}(u_1)_{s_0}\) lies in \(GA_M(K_{s_0s_1})\). By Proposition 4.4 of the automorphism lesson, \(\theta=(v_0)_{s_1}\,h\,(v_1)_{s_0}\) with \(v_0\in G_{M,0}(K_{s_0})\), \(h\in Af_M(K_{s_0s_1})\) and \(v_1\in GA_M(K_{s_1})\). Put \(w_0=u_0v_0\) and \(w_1=u_1v_1^{-1}\), isomorphisms \(B_{s_i}\to A_{s_i}\). Then
\[
(w_0)_{s_1}^{-1}(w_1)_{s_0}=(v_0)_{s_1}^{-1}\,\theta\,(v_1)_{s_0}^{-1}=h .
\]

*Step 3: the linear part of \(A\).* Let \(B^{\le1}=K\oplus M\subseteq B\). Since \(h\) is affine, \(h(B^{\le1}_{s_0s_1})=B^{\le1}_{s_0s_1}\), so the submodules \(w_i(B^{\le1}_{s_i})\subseteq A_{s_i}\) have the same localization in \(A_{s_0s_1}\). Let
\[
A^{\le1}=\{a\in A:\ a\in w_0(B^{\le1}_{s_0})\text{ in }A_{s_0}\ \text{and}\ a\in w_1(B^{\le1}_{s_1})\text{ in }A_{s_1}\}.
\]
Since localization is exact, the localizations of \(M_i'=w_i(B^{\le1}_{s_i})\) at \(s_{1-i}\) are submodules of \(A_{s_0s_1}\), and they are equal. By Lemma 1.2 of the patching lesson, \(A\) is the fibre product of \(A_{s_0}\) and \(A_{s_1}\) over \(A_{s_0s_1}\), so \(A^{\le1}\) is the module obtained from \(M_0'\) and \(M_1'\) by Lemma 1.1(2) with \(\varphi\) the identity; hence \((A^{\le1})_{s_i}\to A_{s_i}\) is injective with image \(M_i'=w_i(B^{\le1}_{s_i})\). It contains \(K\cdot1\), and \(K\to A\) is injective, because it is so after inverting \(s_0\) and \(s_1\). Let \(N=A^{\le1}/K\). Then \(w_i\) induces \(N_{s_i}\cong B^{\le1}_{s_i}/K_{s_i}=M_{s_i}\), and \(N\) is finitely presented by Lemma 1.1(3).

*Step 4: a splitting.* The maps \(\rho_i=\varepsilon\circ w_i^{-1}\colon(A^{\le1})_{s_i}\to K_{s_i}\), with \(\varepsilon\) the augmentation of \(B\), are retractions of the inclusions of \(K_{s_i}\). Their difference on \(A^{\le1}_{s_0s_1}\) kills \(K\), so it is \(\delta\circ\pi\) with \(\pi\colon A^{\le1}\to N\) and \(\delta\in\operatorname{Hom}(N_{s_0s_1},K_{s_0s_1})\). As \(N\) is finitely presented, \(\operatorname{Hom}(N_{s_0s_1},K_{s_0s_1})=\operatorname{Hom}_K(N,K)_{s_0s_1}\), and by Lemma 1.1(1), \(\delta=\alpha+\beta\) with \(\alpha\) coming from \(\operatorname{Hom}(N_{s_0},K_{s_0})\) and \(\beta\) from \(\operatorname{Hom}(N_{s_1},K_{s_1})\). The retractions \(\rho_0-\alpha\pi\) and \(\rho_1+\beta\pi\) agree on \(A^{\le1}_{s_0s_1}\). By the exact sequence of Lemma 1.2 of the patching lesson for the module \(K\), there is for each \(a\in A^{\le1}\) a unique \(\rho(a)\in K\) whose images in \(K_{s_0}\) and \(K_{s_1}\) are the values of these two retractions at \(a\). This defines a \(K\)-linear \(\rho\colon A^{\le1}\to K\), and \(\rho(c)=c\) for \(c\in K\), since this holds after inverting \(s_0\) and \(s_1\). Then \(A^{\le1}=K\cdot1\oplus\ker\rho\) and \(\ker\rho\cong N\).

*Step 5: the isomorphism.* Let \(t\colon S(N)\to A\) be the algebra map extending \(N\cong\ker\rho\subseteq A\). For each \(i\), \(w_i^{-1}\circ t_{s_i}\colon S(N_{s_i})\to S(M_{s_i})\) sends \(N_{s_i}\) into \(K_{s_i}\oplus M_{s_i}\), and its component in \(M_{s_i}\) is the isomorphism \(N_{s_i}\cong M_{s_i}\) of Step 3. So it is the composite of the graded isomorphism defined by that linear map with a translation, an isomorphism. Hence \(t_{s_0}\) and \(t_{s_1}\) are isomorphisms, and so is \(t\), its kernel and cokernel being killed by powers of \(s_0\) and of \(s_1\). This proves \(\mathcal P(K)\), the sheaf condition.

Quillen induction now gives \(\mathcal P(K)\). \(\square\)

**Corollary 2.2.** Let \(A\) be a finitely presented \(K\)-algebra with \(A_{\mathfrak m}\cong K_{\mathfrak m}[X_1,\ldots,X_n]\) for every maximal ideal \(\mathfrak m\). Then \(A\cong S(P)\) for a finitely generated projective \(K\)-module \(P\) of rank \(n\). If every finitely generated projective \(K\)-module of rank \(n\) is free, then \(A\cong K[X_1,\ldots,X_n]\). This holds for \(K=F[y_1,\ldots,y_r]\) with \(F\) a field.

**Proof.** Theorem 2.1 gives \(A\cong S(P)\) with \(P\) finitely presented. For each \(\mathfrak m\), \(S(P_{\mathfrak m})\cong S(K_{\mathfrak m}^n)\), so \(P_{\mathfrak m}\cong K_{\mathfrak m}^n\) by Lemma 1.2. Every prime \(\mathfrak q\) lies in a maximal ideal \(\mathfrak m\), and \(P_{\mathfrak q}\) is a localization of \(P_{\mathfrak m}\), hence free of rank \(n\). By Lemma 1.1(2) of the Horrocks lesson, \(P\) is projective, of rank \(n\). If \(P\cong K^n\), then \(A\cong S(K^n)=K[X_1,\ldots,X_n]\). For \(K=F[y_1,\ldots,y_r]\), freeness is the Quillen–Suslin theorem. \(\square\)

## 3. Exercises

**Exercise 3.1.** For \(K=\mathbb Z\) and \(N=\mathbb Z/2\), describe \(S(N)\) as a quotient of \(\mathbb Z[X]\) and decide whether it is locally polynomial.

**Exercise 3.2.** For \(A=K[X,Y]/(X-Y^2)\) with the augmentation \(X,Y\mapsto0\), compute \(I/I^2\) by the method of Lemma 1.3.

**Exercise 3.3.** Let \(K=\mathbb R[x,y,z]/(x^2+y^2+z^2-1)\) and let \(P\) be the kernel of the map \(K^3\to K\), \((a,b,c)\mapsto ax+by+cz\). Show that \(P\oplus K\cong K^3\), that \(S(P)[T]\cong K[X_1,X_2,X_3]\), and that \(S(P)\) is locally polynomial in two variables. Show that if \(P\) is not free, then \(S(P)\) is not isomorphic to \(K[X_1,X_2]\).

**Exercise 3.4.** Show that Corollary 2.2 applies to \(K=F[y]\) with \(F\) a field without using the Quillen–Suslin theorem.

## 4. Solutions

**3.1.** \(S(\mathbb Z/2)=\mathbb Z[X]/(2X)\). It is not locally polynomial at \((2)\): a polynomial ring over \(\mathbb Z_{(2)}\) is a domain, but \(2\cdot X=0\) with \(2\ne0\) and \(X\ne0\) in the localization. (At primes \(p\ne2\), the localization is \(\mathbb Z_{(p)}\), polynomial in zero variables.)

**3.2.** Here \(q=1\), \(f_1=X-Y^2\) with linear part \(\ell_1=X\), so \(I/I^2\cong K^2/(K\cdot e_1)\cong K\), generated by the class of \(Y\). Indeed \(A\cong K[Y]\).

**3.3.** The element \((x,y,z)\) is mapped to \(1\), so \(K^3=K\cdot(x,y,z)\oplus P\). Then \(S(P)[T]=S(P)\otimes S(K)=S(P\oplus K)\cong S(K^3)\). \(P\) is a direct summand of \(K^3\), hence finitely presented and projective, and \(P_{\mathfrak m}\) is free (Lemma 1.1(1) of the Horrocks lesson) of rank \(2\), since \(P_{\mathfrak m}\oplus K_{\mathfrak m}\cong K_{\mathfrak m}^3\). So \(S(P)\) is finitely presented and \(S(P)_{\mathfrak m}=S(P_{\mathfrak m})\cong K_{\mathfrak m}[X_1,X_2]\). If \(S(P)\cong K[X_1,X_2]=S(K^2)\), Lemma 1.2 would give \(P\cong K^2\).

**3.4.** \(F[y]\) is a principal ideal domain, so finitely generated projective modules are free by Lemma 1.2(1) of the Horrocks lesson.

## References

- [BCW] H. Bass, E. H. Connell, D. Wright, Locally polynomial algebras are symmetric algebras, Inventiones Mathematicae 38 (1977), 279–299. https://gdz.sub.uni-goettingen.de/id/PPN356556735_0038
- [Quillen] D. Quillen, Projective modules over polynomial rings, Inventiones Mathematicae 36 (1976), 167–171. https://gdz.sub.uni-goettingen.de/id/PPN356556735_0036
