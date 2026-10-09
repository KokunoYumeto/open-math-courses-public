# Patching extended modules

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A module \(M\) over a polynomial ring \(A[T]\) is **extended** from \(A\) if \(M\cong N\otimes_AA[T]\) for some \(A\)-module \(N\). This lesson proves Quillen's local–global principle: a finitely presented \(A[T]\)-module which is extended after localizing at every maximal ideal of \(A\) is extended. The global isomorphism is assembled from local ones. Two local isomorphisms on comaximal localizations differ by an automorphism of \(N[T]\) congruent to the identity modulo \(T\), and such an automorphism splits into a factor defined over each localization after the variable \(T\) is rescaled. The argument is organized as Quillen induction, a principle that later lessons of this course apply to projective modules and to algebras.

We use from [Localization, local properties and support](course:AG-CA/localization-local-properties-and-support#2-relations-survive-localization) Theorem 2.1 (exactness of localization), Theorem 2.2 (localizing \(\operatorname{Hom}\) out of a finitely presented module) and Theorem 5.1 (local detection of zero). All rings are commutative with \(1\), except the rings \(R\) of Section 2. For an element \(f\) of a ring \(A\), \(A_f=A[1/f]\) and \(M_f=M\otimes_AA_f\); localization of elements and maps at \(f\) is indicated by the subscript \(f\). We write \(N[T]=N\otimes_AA[T]\).

## 1. Localizations and gluing

**Lemma 1.1** (isomorphisms spread). Let \(N,N'\) be finitely presented modules over a ring \(B\), \(S\subseteq B\) multiplicative, and \(\varphi\colon S^{-1}N\to S^{-1}N'\) an isomorphism. There are \(s\in S\) and an isomorphism \(N_s\to N'_s\) whose localization is \(\varphi\). Two homomorphisms \(N\to N'\) with the same localization agree after inverting some \(t\in S\).

**Proof.** By Theorem 2.2 of the localization lesson, \(S^{-1}\operatorname{Hom}_B(N,N')=\operatorname{Hom}_{S^{-1}B}(S^{-1}N,S^{-1}N')\), and similarly for \(\operatorname{Hom}(N',N)\) and the endomorphism modules. So \(\varphi=\alpha/s_1\) and \(\varphi^{-1}=\beta/s_2\) with \(\alpha\colon N\to N'\), \(\beta\colon N'\to N\), \(s_i\in S\). The endomorphisms \(\beta\alpha-s_1s_2\) and \(\alpha\beta-s_1s_2\) have zero localization, so they are killed by some \(s_3\in S\). With \(s=s_1s_2s_3\), the maps \(\alpha/s_1\colon N_s\to N'_s\) and \(\beta/s_2\colon N'_s\to N_s\) are inverse to each other. The second assertion is the injectivity of \(\operatorname{Hom}_B(N,N')\to\operatorname{Hom}(S^{-1}N,S^{-1}N')\) up to \(S\)-torsion: a homomorphism with zero localization is killed by some \(t\in S\). \(\square\)

**Lemma 1.2** (gluing). Let \(f_0,f_1\in A\) with \(Af_0+Af_1=A\). For every \(A\)-module \(M\) the sequence
\[
0\to M\to M_{f_0}\times M_{f_1}\to M_{f_0f_1},\qquad x\mapsto(x,x),\quad(a,b)\mapsto a-b,
\]
is exact. Consequently, if \(u_i\colon M'_{f_i}\to M_{f_i}\) are isomorphisms of \(A_{f_i}\)-modules with \((u_0)_{f_1}=(u_1)_{f_0}\), there is a unique isomorphism \(u\colon M'\to M\) with \(u_{f_i}=u_i\) for \(i=0,1\).

**Proof.** For every \(n\), \(Af_0^n+Af_1^n=A\), since a maximal ideal containing both powers would contain \(f_0\) and \(f_1\). If \(x\) maps to zero in both localizations, then \(f_0^nx=f_1^nx=0\) for some \(n\), so \(x=0\). Let \(a=y/f_0^n\) and \(b=z/f_1^n\) have the same image in \(M_{f_0f_1}\). Then \((f_0f_1)^m(f_1^ny-f_0^nz)=0\) for some \(m\); replacing \(y,z,n\) by \(f_0^my,\ f_1^mz,\ n+m\), which does not change \(a\) and \(b\), we may assume \(f_1^ny=f_0^nz\). Write \(1=cf_0^n+df_1^n\) and put \(x=cy+dz\). Then
\[
f_0^nx=cf_0^ny+df_0^nz=cf_0^ny+df_1^ny=y,\qquad f_1^nx=cf_1^ny+df_1^nz=cf_0^nz+df_1^nz=z,
\]
so \(x\) maps to \((a,b)\). For the second assertion, send \(x'\in M'\) to the unique \(x\in M\) with image \((u_0(x'),u_1(x'))\); this defines an \(A\)-linear \(u\) with \(u_{f_i}=u_i\), because both sides are \(A_{f_i}\)-linear and agree on the image of \(M'\). The isomorphisms \(u_i^{-1}\) give \(v\colon M\to M'\) in the same way, and \(uv\), \(vu\) are identities by the uniqueness part of exactness. \(\square\)

## 2. Quillen's lemma

For a ring \(R\), not necessarily commutative, write \((1+TR[T])^\times\) for the group of units of \(R[T]\) that are congruent to \(1\) modulo \(T\) and whose inverses are congruent to \(1\) modulo \(T\). Here \(T\) and further indeterminates commute with \(R\). Let \(R\) be an algebra over a commutative ring \(A\), with \(A\) mapping to the centre of \(R\). For \(f\in A\), \(R_f=R\otimes_AA_f\), and for \(\theta(T)\in R_f[T]\) and \(g\in A\), \(\theta(gT)\) is obtained by substituting \(gT\) for \(T\).

**Lemma 2.1** (Quillen). Let \(f\in A\) and \(\theta\in(1+TR_f[T])^\times\). There is an integer \(k\ge0\) with the following property: whenever \(g_1,g_2\in A\) and \(g_1-g_2\in f^kA\), there is \(\psi\in(1+TR[T])^\times\) with \(\psi_f(T)=\theta(g_1T)\,\theta(g_2T)^{-1}\).

**Proof.** Write \(\theta(T)=\sum_{i=0}^pa_iT^i\) and \(\theta(T)^{-1}=\sum_{j=0}^pb_jT^j\) with \(a_i,b_j\in R_f\) and \(a_0=b_0=1\). Let \(Y,Z\) be further central indeterminates and \(r\ge0\). Since \(U^i-V^i=(U-V)\sum_{n=0}^{i-1}U^{i-1-n}V^n\),
\[
\theta\bigl((Y+f^rZ)T\bigr)\,\theta(YT)^{-1}
=1+\bigl[\theta((Y+f^rZ)T)-\theta(YT)\bigr]\theta(YT)^{-1}
=1+ZT\sum_{i=1}^p\sum_{j=0}^p\sum_{n=0}^{i-1}f^ra_ib_j\,(Y+f^rZ)^{i-1-n}\,Y^{n+j}\,T^{i-1+j}.
\]
For \(r\) large, each of the finitely many elements \(f^ra_ib_j\) is the image of some \(c_{ij}\in R\). Hence there is \(\phi\in1+ZT\,R[Y,Z,T]\) with \(\phi_f=\theta((Y+f^rZ)T)\,\theta(YT)^{-1}\). Applying the same construction after the substitution \(Y\mapsto Y+f^rZ\), \(Z\mapsto-Z\) gives \(\phi'\in1+ZT\,R[Y,Z,T]\) with \(\phi'_f=\theta(YT)\,\theta((Y+f^rZ)T)^{-1}\). Then \((\phi\phi')_f=(\phi'\phi)_f=1\). Write \(\phi\phi'=1+ZTh_1\) and \(\phi'\phi=1+ZTh_2\); the polynomials \(h_1,h_2\) have zero image over \(R_f\), so their finitely many coefficients are killed by some power \(f^s\). Consequently \(\phi(Y,f^sZ,T)\) is invertible with inverse \(\phi'(Y,f^sZ,T)\): for instance \(\phi(Y,f^sZ,T)\phi'(Y,f^sZ,T)=1+f^sZT\,h_1(Y,f^sZ,T)=1\).

Put \(k=r+s\). If \(g_1=g_2+f^kz\) with \(z\in A\), let \(\psi(T)=\phi(g_2,f^sz,T)\). It lies in \((1+TR[T])^\times\), because \(\phi\) and its inverse are congruent to \(1\) modulo \(ZT\), and
\[
\psi_f(T)=\theta\bigl((g_2+f^rf^sz)T\bigr)\,\theta(g_2T)^{-1}=\theta(g_1T)\,\theta(g_2T)^{-1}.\qquad\square
\]

## 3. Quillen induction

Let \(K\) be a nonzero ring, and let \(\operatorname{Loc}(K)\) be the class of \(K\)-algebras of the form \(S^{-1}K\) with \(S\subseteq K\) multiplicative. For \(L=S^{-1}K\) and \(s\in L\) the algebra \(L_s\) again lies in \(\operatorname{Loc}(K)\).

**Proposition 3.1** (Quillen induction). Let \(\mathcal P\) be a property of the algebras in \(\operatorname{Loc}(K)\) such that:

1. (specialization) if \(\mathcal P(L)\) holds and \(L\to L'\) is a \(K\)-algebra map between members of \(\operatorname{Loc}(K)\), then \(\mathcal P(L')\) holds;
2. (finiteness) if \(S\subseteq K\) is multiplicative and \(\mathcal P(S^{-1}K)\) holds, then \(\mathcal P(K_s)\) holds for some \(s\in S\);
3. (local validity) \(\mathcal P(K_{\mathfrak m})\) holds for every maximal ideal \(\mathfrak m\) of \(K\);
4. (sheaf condition) if \(L\in\operatorname{Loc}(K)\), \(t_0,t_1\in L\), \(Lt_0+Lt_1=L\), and \(\mathcal P(L_{t_0})\), \(\mathcal P(L_{t_1})\) hold, then \(\mathcal P(L)\) holds.

Then \(\mathcal P(K)\) holds.

**Proof.** Let \(I\) be the set of \(s\in K\) with \(\mathcal P(K_s)\). By local validity and finiteness, for every maximal ideal \(\mathfrak m\) there is \(s\in I\setminus\mathfrak m\). By specialization, \(as\in I\) for \(s\in I\), \(a\in K\). Let \(s_0,s_1\in I\) and \(s=as_0+bs_1\), and put \(L=K_s\), with \(t_i\) the image of \(s_i\). Then \(Lt_0+Lt_1=L\), and \(L_{t_i}=K_{ss_i}\) is a localization of \(K_{s_i}\), so \(\mathcal P(L_{t_i})\) holds by specialization; the sheaf condition gives \(s\in I\). Thus \(I\) is an ideal contained in no maximal ideal, so \(1\in I\), i.e. \(\mathcal P(K)\). \(\square\)

## 4. Quillen's theorem

**Theorem 4.1** (Quillen). Let \(A\) be a ring and \(M\) a finitely presented \(A[T]\)-module. If \(M_{\mathfrak m}\) is extended from \(A_{\mathfrak m}\) for every maximal ideal \(\mathfrak m\) of \(A\), then \(M\) is extended from \(A\); more precisely \(M\cong N[T]\) with \(N=M/TM\), by an isomorphism which reduces to the identity of \(N\) modulo \(T\).

**Proof.** If \(A=0\), then \(M=0\) and there is nothing to prove; let \(A\ne0\). The module \(N=M/TM\) is finitely presented over \(A\). For \(L\in\operatorname{Loc}(A)\) let \(\mathcal P(L)\) be the statement: there is an \(L[T]\)-linear isomorphism \(u\colon N_L[T]\to M_L\) which reduces modulo \(T\) to the identity of \(N_L=M_L/TM_L\). (Subscripts \(L\) denote base change to \(L\); base change from \(A\) to \(L\) commutes with reduction modulo \(T\), by exactness of localization.) We verify the four conditions of Proposition 3.1.

*Specialization* is base change of \(u\).

*Local validity.* By hypothesis \(M_{\mathfrak m}\cong N'[T]\) for some \(A_{\mathfrak m}\)-module \(N'\). Reducing modulo \(T\) gives an isomorphism \(\gamma\colon N'\to N_{\mathfrak m}\), and composing the given isomorphism \(N'[T]\to M_{\mathfrak m}\) with \(\gamma^{-1}[T]\) gives an isomorphism reducing to the identity.

*Finiteness.* Let \(u\colon N_{S}[T]\to M_S\) be as in \(\mathcal P(S^{-1}A)\). The modules \(N[T]\) and \(M\) are finitely presented over \(A[T]\), and \(S\) is a multiplicative subset of \(A[T]\). By Lemma 1.1, \(u\) comes from an isomorphism \(u'\colon N_s[T]\to M_s\) for some \(s\in S\). Its reduction modulo \(T\) and the identity of \(N_s\) have the same localization, so by Lemma 1.1 they agree after inverting some \(t\in S\), and \(\mathcal P(A_{st})\) holds.

*Sheaf condition.* Replacing \(A\) by \(L\), we may assume \(L=A\), with \(t_0,t_1\in A\), \(At_0+At_1=A\), and isomorphisms \(u_i\colon N_{t_i}[T]\to M_{t_i}\) reducing to the identity. Let \(R=\operatorname{End}_A(N)\). Since \(N\) is finitely presented, Theorem 2.2 of the localization lesson and the finite generation of \(N\) give
\[
\operatorname{End}_{A_{t_0t_1}[T]}\bigl(N_{t_0t_1}[T]\bigr)=\operatorname{Hom}_{A_{t_0t_1}}\Bigl(N_{t_0t_1},\bigoplus_{i\ge0}N_{t_0t_1}T^i\Bigr)=R_{t_0t_1}[T].
\]
So \(\theta=(u_0)_{t_1}^{-1}(u_1)_{t_0}\) is an element of \((1+TR_{t_0t_1}[T])^\times\). Apply Lemma 2.1 twice: to the \(A_{t_0}\)-algebra \(R_{t_0}\), the element \(t_1\) and \(\theta\), and to the \(A_{t_1}\)-algebra \(R_{t_1}\), the element \(t_0\) and \(\theta\); let \(k\) be larger than both resulting integers. Since \(At_0^k+At_1^k=A\), there is \(g\in At_0^k\) with \(1-g\in At_1^k\). Write
\[
\theta(T)=\bigl[\theta(T)\,\theta(gT)^{-1}\bigr]\bigl[\theta(gT)\,\theta(0\cdot T)^{-1}\bigr],\qquad\theta(0\cdot T)=1 .
\]
In \(A_{t_0}\), \(1-g\in t_1^kA_{t_0}\), so the first factor is \((\psi_0)_{t_1}\) for some \(\psi_0\in(1+TR_{t_0}[T])^\times\). In \(A_{t_1}\), \(g-0\in t_0^kA_{t_1}\), so the second factor is \((\psi_1)_{t_0}\) for some \(\psi_1\in(1+TR_{t_1}[T])^\times\). Now \(u_0\psi_0\) and \(u_1\psi_1^{-1}\) are isomorphisms reducing to the identity, and
\[
(u_0\psi_0)_{t_1}^{-1}(u_1\psi_1^{-1})_{t_0}=(\psi_0)_{t_1}^{-1}\,\theta\,(\psi_1)_{t_0}^{-1}=1 .
\]
By Lemma 1.2 they glue to an isomorphism \(N[T]\to M\); its reduction modulo \(T\) is the identity, as it is after localizing at \(t_0\) and at \(t_1\). This proves \(\mathcal P(A)\).

Proposition 3.1 now gives \(\mathcal P(A)\). \(\square\)

**Corollary 4.2.** Let \(A\) be a ring and \(P\) a finitely generated projective \(A[T]\)-module such that \(P_{\mathfrak m}\) is a free \(A_{\mathfrak m}[T]\)-module for every maximal ideal \(\mathfrak m\) of \(A\). Then \(P\cong(P/TP)[T]\).

**Proof.** A finitely generated projective module is finitely presented: it is a direct summand of some \(A[T]^n\), so the kernel of a surjection \(A[T]^n\to P\) is a direct summand of \(A[T]^n\), hence finitely generated. A free \(A_{\mathfrak m}[T]\)-module is extended from \(A_{\mathfrak m}\). Apply Theorem 4.1. \(\square\)

## 5. Exercises

**Exercise 5.1.** Show that if \(M\cong N[T]\) for an \(A\)-module \(N\), then \(N\cong M/TM\).

**Exercise 5.2.** Let \(R=M_2(\mathbb Z)\), \(A=\mathbb Z\), \(t_0=2\), \(t_1=3\), and let \(\theta(T)\in R_6[T]\) be the matrix with rows \((1,\ T/6)\) and \((0,\ 1)\). Write \(\theta=(\psi_0)_3(\psi_1)_2\) with \(\psi_0\) a unipotent matrix over \(\mathbb Z[1/2][T]\) and \(\psi_1\) one over \(\mathbb Z[1/3][T]\).

**Exercise 5.3.** Extend Lemma 1.2 to elements \(f_1,\ldots,f_n\) generating the unit ideal.

**Exercise 5.4.** Let \(A\) be a ring and \(P\) a finitely generated projective \(A[T]\)-module. Show that \(P\) is extended from \(A\) as soon as \(P_{\mathfrak m}\) is extended from \(A_{\mathfrak m}\) for all maximal ideals \(\mathfrak m\), and that then \(P/TP\) is a finitely generated projective \(A\)-module.

## 6. Solutions

**5.1.** Tensoring with \(A[T]/(T)=A\) over \(A[T]\) gives \(M/TM\cong N[T]\otimes_{A[T]}A=N\).

**5.2.** Since \(\tfrac16=\tfrac12-\tfrac13\), take \(\psi_0\) with rows \((1,\ T/2)\), \((0,1)\) and \(\psi_1\) with rows \((1,\ -T/3)\), \((0,1)\). Unipotent upper triangular matrices multiply by adding their corner entries, so \(\psi_0\psi_1=\theta\) in \(R_6[T]\).

**5.3.** Let \((a_i)\in\prod_iM_{f_i}\) have equal images in all \(M_{f_if_j}\). Write \(a_i=y_i/f_i^n\) with one \(n\). For each pair \(i,j\), \((f_if_j)^{m}(f_j^ny_i-f_i^ny_j)=0\) for some \(m\), and one \(m\) serves all pairs. Since \((f_if_j)^m(f_j^ny_i-f_i^ny_j)=f_j^{n+m}(f_i^my_i)-f_i^{n+m}(f_j^my_j)\), replacing \(y_i\) by \(f_i^my_i\) and \(n\) by \(n+m\) achieves \(f_j^ny_i=f_i^ny_j\) for all \(i,j\). The \(f_i^n\) generate the unit ideal; write \(1=\sum_ic_if_i^n\) and put \(x=\sum_ic_iy_i\). Then \(f_j^nx=\sum_ic_if_j^ny_i=\sum_ic_if_i^ny_j=y_j\), so \(x\) maps to \(a_j\) for every \(j\). Injectivity and the gluing of isomorphisms follow as in Lemma 1.2.

**5.4.** The first claim is Theorem 4.1, since \(P\) is finitely presented. Then \(P\cong(P/TP)[T]\), and \(P/TP\) is a direct summand of \((A[T]/(T))^n=A^n\) because \(P\) is a direct summand of \(A[T]^n\).

## References

- [Quillen] D. Quillen, Projective modules over polynomial rings, Inventiones Mathematicae 36 (1976), 167–171. https://gdz.sub.uni-goettingen.de/id/PPN356556735_0036
- [BCW] H. Bass, E. H. Connell, D. Wright, Locally polynomial algebras are symmetric algebras, Inventiones Mathematicae 38 (1977), 279–299. https://gdz.sub.uni-goettingen.de/id/PPN356556735_0038
- [Lombardi–Quitté] H. Lombardi, C. Quitté, Commutative algebra: constructive methods, Springer 2015. https://arxiv.org/abs/1605.04832
