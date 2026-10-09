# Automorphisms of symmetric algebras

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The next lesson proves that a finitely presented algebra which is locally a symmetric algebra is a symmetric algebra. The proof patches local isomorphisms as Quillen's theorem does for modules, but the comparison between two local isomorphisms is now an automorphism of a symmetric algebra, possibly nonlinear. This lesson provides the tool: such an automorphism over a double localization factors into a part over each localization and an affine part. Two properties make this work. Automorphism groups of finitely presented algebras satisfy a rescaling property, called axiom Q; and the automorphisms preserving the augmentation carry an action of the scalars, which interpolates between an automorphism and its linear part. The method is due to Bass, Connell and Wright, following Quillen.

The arguments of Section 2 adapt Lemma 1.1 and Quillen's Lemma 2.1 of [Patching extended modules](patching-extended-modules.md) from modules to algebras; the lesson is otherwise self-contained. All rings and algebras are commutative with \(1\). We fix a ring \(K\); "algebra" means commutative \(K\)-algebra. For an algebra \(L\), an element \(s\in L\) and an \(L\)-module or \(L\)-algebra \(X\), \(X_s=X\otimes_LL_s\).

## 1. Group functors and axiom Q

Let \(G\) be a functor from algebras to groups. For an algebra \(L\) and \(s\in L\), \(G(L)_s\) denotes the image of \(G(L)\to G(L_s)\), and \(u\mapsto u_s\) the map. For an indeterminate \(T\), an element \(u\in G(L[T])\) is also written \(u(T)\); if \(L'\) is an \(L\)-algebra and \(c\in L'\), \(u(c)\) is its image under the map induced by \(L[T]\to L'\), \(T\mapsto c\). In particular \(u(cT)\in G(L'[T])\) for \(c\in L'\). Put
\[
G(TL[T])=\ker\bigl(G(L[T])\to G(L)\bigr),\qquad T\mapsto0 .
\]

**Definition 1.1.** \(G\) satisfies **axiom Q** if for every algebra \(L\), every \(s\in L\) and every \(u(T)\in G(TL_s[T])\) there are \(r\ge0\) and \(v(T)\in G(TL[T])\) with \(v(T)_s=u(s^rT)\).

## 2. Finitely presented algebras

Let \(A=K[X_1,\ldots,X_p]/(f_1,\ldots,f_q)\) be a finitely presented algebra, with \(x_i\) the image of \(X_i\). For an algebra \(C\), algebra homomorphisms \(A\to C\) correspond to tuples \(y\in C^p\) with \(f_j(y)=0\) for all \(j\), via \(\phi\mapsto(\phi(x_i))_i\). For an algebra \(L\), \(A_L=L\otimes_KA\).

**Lemma 2.1.** Let \(A,B\) be algebras with \(A\) finitely presented, and \(S\subseteq K\) multiplicative.

1. Every \(K_S\)-algebra homomorphism \(A_S\to B_S\) is the localization of a \(K_s\)-algebra homomorphism \(A_s\to B_s\) for some \(s\in S\).
2. Two \(K_s\)-algebra homomorphisms \(A_s\to B_s\) with the same localization agree after inverting some \(t\in S\).
3. If \(B\) is also finitely presented, every isomorphism \(A_S\to B_S\) is the localization of an isomorphism \(A_s\to B_s\) for some \(s\in S\).

**Proof.** A homomorphism \(A_s\to B_s\) of \(K_s\)-algebras is a homomorphism \(A\to B_s\) of \(K\)-algebras, i.e. a tuple \(y\in B_s^p\) with \(f_j(y)=0\). (2) Two tuples with the same image in \(B_S^p\) agree in \(B_{st}^p\) for some \(t\in S\). (1) A tuple \(y\in B_S^p\) with \(f_j(y)=0\) is the image of some \(w\in B_s^p\), and the finitely many elements \(f_j(w)\in B_s\) vanish in \(B_S\), hence in \(B_{st}\) for some \(t\); then \(w\) defines a homomorphism \(A_{st}\to B_{st}\). (3) Lift the isomorphism and its inverse by (1) to \(\alpha\colon A_s\to B_s\) and \(\beta\colon B_s\to A_s\). The composites \(\beta\alpha\) and \(\alpha\beta\) have the same localizations as the identities, so by (2), applied to \(A\) and to \(B\), they are identities after inverting some \(t\in S\). \(\square\)

**Lemma 2.2.** Let \(A\) be finitely presented, \(L\) an algebra, \(s\in L\), and \(u(T)\) an automorphism of the \(L_s[T]\)-algebra \(A_{L_s}[T]\) with \(u(0)=\mathrm{id}\). There are \(r\ge0\) and an automorphism \(v(T)\) of the \(L[T]\)-algebra \(A_L[T]\) with \(v(0)=\mathrm{id}\) and \(v(T)_s=u(s^rT)\).

**Proof.** The condition \(u(0)=\mathrm{id}\) means \(u(T)(x)=x+Ty_1(T)\) for the tuple \(x=(x_i)\) and some \(y_1(T)\in A_{L_s}[T]^p\).

*Clearing denominators.* All coefficients of \(y_1\) have the form \(c/s^e\) with \(c\) from \(A_L\) and one exponent \(e\). The coefficient of \(T^i\) in \(s^{r_1}y_1(s^{r_1}T)\) is \(s^{r_1(i+1)}\) times that of \(T^i\) in \(y_1\); for \(r_1\ge e\) it comes from \(A_L\). So there is \(w_1(T)\in A_L[T]^p\) with \(w_1(T)_s=s^{r_1}y_1(s^{r_1}T)\), and \(w(T)=x+Tw_1(T)\) satisfies \(w(T)_s=x+s^{r_1}Ty_1(s^{r_1}T)\), the tuple of \(u(s^{r_1}T)\).

*Relations.* Since \(f_j(x)=0\), \(f_j(w(T))=Tg_j(T)\) for some \(g_j\in A_L[T]\). Its image over \(L_s\) is \(f_j\) of the tuple of the homomorphism \(u(s^{r_1}T)\), hence \(0\); as \(T\) is a nonzerodivisor, \(g_j(T)_s=0\), and the finitely many coefficients of the \(g_j\) are killed by some \(s^{r_2}\). Then \(f_j(w(s^{r_2}T))=s^{r_2}T\,g_j(s^{r_2}T)=0\), because \(s^{r_2}g_j(s^{r_2}T)\) has coefficients \(s^{r_2(i+1)}\) times those of \(g_j\). So \(w(s^{r_2}T)\) is the tuple of an endomorphism \(W(T)\) of \(A_L[T]\) with \(W(0)=\mathrm{id}\) and \(W(T)_s=u(s^{r_1+r_2}T)\).

*Inverse.* The same construction for \(u(T)^{-1}\) gives an endomorphism \(W'(T)\) with \(W'(0)=\mathrm{id}\) and \(W'(T)_s=u(s^{r}T)^{-1}\); replacing \(W(T)\) or \(W'(T)\) by \(W(s^eT)\) or \(W'(s^eT)\) we may use one exponent \(r\) for both. The endomorphisms \(WW'\) and \(W'W\) send \(x\) to \(x+Tz(T)\) and \(x+Tz'(T)\) with \(z(T)_s=z'(T)_s=0\), so \(s^m\) kills the coefficients of \(z,z'\) for some \(m\). Substituting \(s^mT\) for \(T\) commutes with composition, and \((WW')(s^mT)\) sends \(x\) to \(x+s^mTz(s^mT)=x\); similarly for \(W'W\). Hence \(v(T)=W(s^mT)\) is an automorphism with inverse \(W'(s^mT)\), \(v(0)=\mathrm{id}\) and \(v(T)_s=u(s^{r+m}T)\). \(\square\)

**Proposition 2.3.** If \(A\) is finitely presented, the functor \(L\mapsto\operatorname{Aut}_{L\text{-alg}}(A_L)\) satisfies axiom Q.

**Proof.** Its value on \(L[T]\) is the group of automorphisms of \(A_L[T]\), and \(G(TL_s[T])\) consists of the automorphisms \(u(T)\) of \(A_{L_s}[T]\) with \(u(0)=\mathrm{id}\). Apply Lemma 2.2. \(\square\)

## 3. Symmetric algebras and scalar operations

Let \(M\) be a \(K\)-module and \(S(M)=\bigoplus_{n\ge0}S^n(M)\) its symmetric algebra. For an algebra \(L\), \(M_L=L\otimes_KM\) and \(L\otimes_KS(M)=S(M_L)\), the symmetric algebra of \(M_L\) over \(L\). It is generated as an \(L\)-algebra by \(S^1(M_L)=M_L\). Its **augmentation** \(\varepsilon\colon S(M_L)\to L\) kills \(I_L=\bigoplus_{n\ge1}S^n(M_L)\). If \(M\) is finitely presented, \(S(M)\) is a finitely presented algebra: a presentation \(K^q\to K^p\to M\to0\) gives \(S(M)=K[X_1,\ldots,X_p]\) modulo the \(q\) linear forms of the relations.

For an algebra \(L\) define three groups of \(L\)-algebra automorphisms of \(S(M_L)\):

- \(GA_M(L)\), all automorphisms;
- \(G_M(L)\), the automorphisms \(u\) with \(\varepsilon\circ u=\varepsilon\);
- \(Af_M(L)\), the **affine** automorphisms, those with \(u(L\oplus M_L)=L\oplus M_L\).

All three are functors of \(L\). An endomorphism \(u\) satisfies \(\varepsilon\circ u=\varepsilon\) if and only if \(u(I_L)\subseteq I_L\), and since \(M_L\) generates, if and only if \(u(M_L)\subseteq I_L\). If \(u\) is an automorphism with \(\varepsilon\circ u=\varepsilon\), then \(\varepsilon\circ u^{-1}=\varepsilon\), so \(G_M(L)\) is a group. The group \(\operatorname{GL}(M_L)\) of linear automorphisms acts by graded automorphisms, and for every \(L\)-linear \(t\colon M_L\to L\) the **translation** \(\tau_t\), the endomorphism with \(\tau_t(x)=x+t(x)\) for \(x\in M_L\), is an automorphism with inverse \(\tau_{-t}\); both lie in \(Af_M(L)\).

*Components.* Let \(u\in G_M(L)\). Since \(u(M_L)\subseteq I_L\), \(u\) maps \(S^p(M_L)\), which is spanned by products of \(p\) elements of \(M_L\), into \(\bigoplus_{m\ge p}S^m(M_L)\). For \(n\ge0\) let \(u_n\) be the \(L\)-linear map sending \(a\in S^p(M_L)\) to the component of \(u(a)\) in degree \(p+n\). Then \(u=\sum_{n\ge0}u_n\), the sum being finite on each element, and comparing components of \(u(ab)=u(a)u(b)\) and of \(u(v(a))\) gives, for homogeneous \(a,b\) and \(u,v\in G_M(L)\),
\[
u_n(ab)=\sum_{p+q=n}u_p(a)\,u_q(b),\qquad (uv)_n=\sum_{p+q=n}u_p\,v_q .
\tag{3.1}
\]
The map \(u_0\) is the graded automorphism of \(S(M_L)\) induced by the linear map \(u_0|_{M_L}\colon M_L\to M_L\); it is an automorphism because \((u^{-1})_0\) is its inverse, by (3.1).

**Definition 3.1** (scalar operation). For \(c\in L\) and \(u\in G_M(L)\) put \({}^c u=\sum_{n\ge0}c^nu_n\).

**Lemma 3.2.** For \(c,d\in L\) and \(u,v\in G_M(L)\): \({}^cu\in G_M(L)\); \({}^1u=u\); \({}^c({}^du)={}^{cd}u\); \({}^c(uv)={}^cu\,{}^cv\); and \({}^0u=u_0\). The operation is natural: for an algebra map \(\phi\colon L\to L'\), the image of \({}^cu\) in \(G_M(L')\) is \({}^{\phi(c)}\) applied to the image of \(u\).

**Proof.** By the first identity of (3.1), \({}^cu\) is multiplicative; it is \(L\)-linear and fixes \(1\), since \(u_0(1)=1\) and \(u_n(1)=0\) for \(n>0\). It maps \(I_L\) into \(I_L\). The components of \({}^du\) are \(d^nu_n\), giving \({}^c({}^du)={}^{cd}u\); the second identity of (3.1) gives \({}^c(uv)={}^cu\,{}^cv\). Hence \({}^cu\) has inverse \({}^c(u^{-1})\) and lies in \(G_M(L)\). The last two statements are clear from the definition, as base change preserves degrees. \(\square\)

Put \(G_{M,0}(L)=\{u\in G_M(L):{}^0u=\mathrm{id}\}\), the automorphisms with \(u(x)-x\in I_L^2\) for \(x\in M_L\). It is a normal subgroup of \(G_M(L)\), the kernel of \(u\mapsto u_0\).

**Proposition 3.3.** For every algebra \(L\), \(GA_M(L)=G_{M,0}(L)\cdot Af_M(L)\).

**Proof.** Let \(u\in GA_M(L)\) and \(t=\varepsilon\circ u|_{M_L}\colon M_L\to L\). Then \(v=u\circ\tau_{-t}\) satisfies \(v(x)=u(x)-t(x)\), so \(\varepsilon\circ v=\varepsilon\) and \(v\in G_M(L)\). Let \(\ell={}^0v\), a graded automorphism, and \(g=v\ell^{-1}\). By Lemma 3.2, \({}^0g={}^0v\,{}^0(\ell^{-1})=\ell\,\ell^{-1}=\mathrm{id}\), since \({}^0\) fixes graded automorphisms. So \(u=v\tau_t=g\,(\ell\tau_t)\) with \(g\in G_{M,0}(L)\) and \(\ell\tau_t\in Af_M(L)\). \(\square\)

**Proposition 3.4.** If \(M\) is finitely presented, the functors \(GA_M\) and \(G_M\) satisfy axiom Q.

**Proof.** For \(GA_M\) this is Proposition 2.3, since \(S(M)\) is finitely presented. Let \(u(T)\in G_M(TL_s[T])\) and take \(r\) and \(v'(T)\in GA_M(TL[T])\) with \(v'(T)_s=u(s^rT)\). Let \(x_1,\ldots,x_p\) generate \(M\). Then \(v'(T)(x_i)=x_i+Ty_i(T)\), and \(\varepsilon(Ty_i(T))\in L[T]\) vanishes over \(L_s\) because \(u(s^rT)\in G_M\). So \(s^m\) kills the coefficients of the \(\varepsilon(y_i(T))\) for some \(m\), and \(v(T)=v'(s^mT)\) satisfies \(\varepsilon(v(T)(x_i))=s^mT\,\varepsilon(y_i)(s^mT)=0\). Thus \(v(T)\in G_M(TL[T])\) and \(v(T)_s=u(s^{r+m}T)\). \(\square\)

## 4. Factorization over two localizations

Throughout this section \(M\) is finitely presented.

**Lemma 4.1.** Let \(L\) be an algebra, \(s\in L\) and \(u\in G_{M,0}(L_s)\). There is \(r\ge0\) such that for all \(a,b\in L\) with \(a-b\in Ls^r\) there is \(v\in G_{M,0}(L)\) with \(v_s=({}^au)({}^bu)^{-1}\).

**Proof.** Let \(Y,T\) be indeterminates and
\[
w(Y,T)=({}^{Y+T}u)\,({}^Yu)^{-1}\in G_M\bigl(L_s[Y,T]\bigr),
\]
where \(u\) is regarded over \(L_s[Y,T]\). Since \(w(Y,0)=\mathrm{id}\), \(w\) lies in \(G_M(T\,L[Y]_s[T])\), and \({}^0w=u_0u_0^{-1}=\mathrm{id}\). Axiom Q for \(G_M\) (Proposition 3.4), over the algebra \(L[Y]\), gives \(r\) and \(v(Y,T)\in G_M(T\,L[Y][T])\) with \(v_s=w(Y,s^rT)\). By naturality \(({}^0v)_s={}^0w(Y,s^rT)=\mathrm{id}\), and \({}^0v(Y,0)=\mathrm{id}\); replacing \(v\) by \(v\,({}^0v)^{-1}\) keeps these properties and gives \({}^0v=\mathrm{id}\), by Lemma 3.2. If \(a=b+s^rc\) with \(c\in L\), the specialization \(Y\mapsto b\), \(T\mapsto c\) gives \(v(b,c)\in G_{M,0}(L)\) with
\[
v(b,c)_s=w(b,s^rc)=({}^{b+s^rc}u)({}^bu)^{-1}=({}^au)({}^bu)^{-1}.\qquad\square
\]

**Theorem 4.2.** Let \(L\) be an algebra and \(s_0,s_1\in L\) with \(Ls_0+Ls_1=L\). Then
\[
G_{M,0}(L_{s_0s_1})=G_{M,0}(L_{s_0})_{s_1}\cdot G_{M,0}(L_{s_1})_{s_0}.
\]

**Proof.** Let \(u\in G_{M,0}(L_{s_0s_1})\). Apply Lemma 4.1 to the algebra \(L_{s_0}\) with the element \(s_1\), and to \(L_{s_1}\) with \(s_0\); let \(r\) exceed both resulting integers. Since \(Ls_0^r+Ls_1^r=L\), there is \(a\in Ls_0^r\) with \(1-a\in Ls_1^r\). Then
\[
u=\bigl[({}^1u)({}^au)^{-1}\bigr]\,\bigl[({}^au)({}^0u)^{-1}\bigr],
\]
using \({}^1u=u\) and \({}^0u=\mathrm{id}\). As \(1-a\in L_{s_0}s_1^r\), the first factor is \((v_0)_{s_1}\) with \(v_0\in G_{M,0}(L_{s_0})\); as \(a-0\in L_{s_1}s_0^r\), the second is \((v_1)_{s_0}\) with \(v_1\in G_{M,0}(L_{s_1})\). \(\square\)

**Lemma 4.3.** Let \(L\) be an algebra, \(s\in L\), \(w\in GA_M(L_s)\) and \(u\in G_M(L_s)\) with \({}^0u=\mathrm{id}\). There is \(r\ge0\) such that for every \(a\in Ls^r\) there is \(v\in GA_M(L)\) with \(v_s=w^{-1}\,({}^au)\,w\).

**Proof.** Let \(u'(T)=w^{-1}({}^Tu)w\in GA_M(L_s[T])\). Since \(u'(0)=w^{-1}({}^0u)w=\mathrm{id}\), axiom Q for \(GA_M\) gives \(r\) and \(v'(T)\in GA_M(TL[T])\) with \(v'(T)_s=u'(s^rT)\). For \(a=s^rc\), \(v=v'(c)\) satisfies \(v_s=u'(s^rc)=w^{-1}({}^au)w\). \(\square\)

**Proposition 4.4.** Let \(L\) be an algebra and \(s_0,s_1\in L\) with \(Ls_0+Ls_1=L\). Every element of \(GA_M(L_{s_0s_1})\) can be written
\[
(v_0)_{s_1}\,h\,(v_1)_{s_0},\qquad v_0\in G_{M,0}(L_{s_0}),\quad h\in Af_M(L_{s_0s_1}),\quad v_1\in GA_M(L_{s_1}).
\]

**Proof.** By Proposition 3.3 an element of \(GA_M(L_{s_0s_1})\) is \(uh\) with \(u\in G_{M,0}(L_{s_0s_1})\) and \(h\in Af_M(L_{s_0s_1})\). For \(a\in L\),
\[
uh=\bigl[({}^1u)({}^au)^{-1}\bigr]\,h\,\bigl[h^{-1}({}^au)h\bigr].
\]
Let \(r\) be larger than the integer of Lemma 4.1 for the algebra \(L_{s_0}\), the element \(s_1\) and \(u\), and than that of Lemma 4.3 for \(L_{s_1}\), the element \(s_0\), \(w=h\) and \(u\). Choose \(a\in Ls_0^r\) with \(1-a\in Ls_1^r\). Then the first factor is \((v_0)_{s_1}\) with \(v_0\in G_{M,0}(L_{s_0})\), and the last is \((v_1)_{s_0}\) with \(v_1\in GA_M(L_{s_1})\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(M=K\), so that \(S(M)=K[X]\). Describe \(G_M(K)\), the components \(u_n\), the scalar operation, \(G_{M,0}(K)\) and \(Af_M(K)\) explicitly when \(K\) is a domain.

**Exercise 5.2.** For \(M=K^2\), \(S(M)=K[X,Y]\), let \(u\) be the automorphism \(X\mapsto X+Y^2\), \(Y\mapsto Y\). Compute \({}^cu\) and check \({}^c({}^du)={}^{cd}u\).

**Exercise 5.3.** Show that for \(u\in G_M(L)\) and a unit \(c\in L\), \({}^cu=\delta_c\circ u\circ\delta_c^{-1}\), where \(\delta_c\) multiplies \(S^n(M_L)\) by \(c^n\).

**Exercise 5.4.** Show that an \(L\)-algebra endomorphism \(u\) of \(S(M_L)\) with \(\varepsilon\circ u=\varepsilon\) maps \(\bigoplus_{m\ge p}S^m(M_L)\) into itself for every \(p\).

## 6. Solutions

**5.1.** An automorphism of \(K[X]\) over a domain \(K\) is \(X\mapsto\alpha X+\beta\) with \(\alpha\in K^\times\), \(\beta\in K\): degrees multiply. So \(GA_M(K)=Af_M(K)\); \(G_M(K)\) consists of \(X\mapsto\alpha X\), with \(u_0=u\) and \(u_n=0\) for \(n>0\); the scalar operation is trivial and \(G_{M,0}(K)\) is trivial.

**5.2.** Here \(u_0=\mathrm{id}\) and \(u_1\) sends \(X\) to \(Y^2\) (degree raised by one); on generators \({}^cu\) is \(X\mapsto X+cY^2\), \(Y\mapsto Y\). Then \({}^c({}^du)\) is \(X\mapsto X+cdY^2\), which is \({}^{cd}u\).

**5.3.** For \(a\in S^p(M_L)\), \(\delta_c^{-1}a=c^{-p}a\) and \(u(c^{-p}a)=\sum_nc^{-p}u_n(a)\), where \(u_n(a)\) has degree \(p+n\). Applying \(\delta_c\) multiplies it by \(c^{p+n}\), so \(\delta_cu\delta_c^{-1}(a)=\sum_nc^nu_n(a)=({}^cu)(a)\).

**5.4.** \(u(I_L)\subseteq I_L\), and \(\bigoplus_{m\ge p}S^m(M_L)=I_L^p\), so \(u(I_L^p)\subseteq I_L^p\).

## References

- [BCW] H. Bass, E. H. Connell, D. Wright, Locally polynomial algebras are symmetric algebras, Inventiones Mathematicae 38 (1977), 279–299. https://gdz.sub.uni-goettingen.de/id/PPN356556735_0038
- [Quillen] D. Quillen, Projective modules over polynomial rings, Inventiones Mathematicae 36 (1976), 167–171. https://gdz.sub.uni-goettingen.de/id/PPN356556735_0036
