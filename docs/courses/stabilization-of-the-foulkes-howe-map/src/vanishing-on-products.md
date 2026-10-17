# Vanishing on products

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By the diagonal criterion (Proposition 3.1 of [Symmetric powers and the Foulkes–Howe map](symmetric-powers-and-the-foulkes-howe-map.md)), Theorem A follows from a vanishing statement for symmetric multilinear forms. This lesson proves it by induction on the number of slots, following OpenAI [OpenAI-FH, Section 4]. Two sequences of directional derivatives do the work, and each is undone by the injectivity lemma of [A differential injectivity lemma](a-differential-injectivity-lemma.md): the first frees one slot from a common factor, and the second, after the induction has made the other slots independent, removes the common power that remains. The second sequence raises the degree of one variable \(r^2\) times, which is where the quadratic bound comes from. Section 3 derives the equivariant embedding of Corollary B.

Throughout, \(V\) is a finite-dimensional complex vector space, products are taken in \(\operatorname{Sym}V\), and a *product of \(k\) vectors* is \(u_1\cdots u_k\) with \(u_i\in V\).

## 1. The vanishing theorem

**Proposition 1.1** (OpenAI). Let \(a,b\ge1\) with \(b\ge a(a-1)\). If a symmetric \(a\)-linear form \(T\) on \(\operatorname{Sym}^bV\) satisfies \(T(P,\dots,P)=0\) for every product \(P\) of \(b\) vectors, then \(T=0\).

*Proof.* If \(V=0\), then \(\operatorname{Sym}^bV=0\). Let \(\dim V=n\ge1\), and fix a basis, so that polynomials in vector variables are defined as in [A differential injectivity lemma](a-differential-injectivity-lemma.md). We prove the statement by induction on \(a\), for all admissible \(b\) and all \(V\) at once. For \(a=1\), \(T\) is a linear form vanishing on all products of \(b\) vectors, which span \(\operatorname{Sym}^bV\).

Let \(a\ge2\) and assume the statement for \(a-1\). Put \(r=a-1\) and \(m=b-r\). Then \(b\ge(r+1)r\) gives \(m\ge r^2\ge1\).

*Step 1: a split binary form.* Let \(Q=y_1\cdots y_m\) be a product of \(m\) vectors, and \(x,t\in V\). For \(c\in\mathbb C\), \(c\ne0\), choose \(\alpha\) with \(\alpha^r=-c\) and let \(\zeta=e^{2\pi i/r}\); then
\[
X^r+cY^r=\prod_{j=0}^{r-1}(X-\alpha\zeta^jY)
\]
as polynomials in \(X,Y\), because \(\prod_j(X-\zeta^jZ)=X^r-Z^r\) (the \(\zeta^j\) are the \(r\)-th roots of unity), applied with \(Z=\alpha Y\). Substituting \(X=x\), \(Y=t\) in \(\operatorname{Sym}V\) shows that \((x^r+ct^r)Q\) is a product of \(r+m=b\) vectors; for \(c=0\) it is \(x^rQ\). So the polynomial in \(c\)
\[
T\bigl((x^r+ct^r)Q,\dots,(x^r+ct^r)Q\bigr)
\]
vanishes for all \(c\), and so do its coefficients. By symmetry and multilinearity the coefficient of \(c\) is \(a\,T(x^rQ,\dots,x^rQ,t^rQ)\), with \(r\) slots \(x^rQ\). Hence
\[
T(x^rQ,\dots,x^rQ,t^rQ)=0 .\tag{1}
\]

*Step 2: freeing the last slot.* Fix \(x\in V\), let \(t,y_1,\dots,y_m\) be vector variables, \(Q=y_1\cdots y_m\), and
\[
H=T(x^rQ,\dots,x^rQ,t^b),
\]
with \(r\) slots \(x^rQ\). It is homogeneous of degree \(b\) in \(t\) and of degree \(r\) in each \(y_i\). Only the last slot involves \(t\), so by Section 1 of [A differential injectivity lemma](a-differential-injectivity-lemma.md), for \(0\le k\le m\),
\[
\begin{aligned}
&D_{y_k,t}\cdots D_{y_1,t}H=\frac{b!}{(b-k)!}\\
&\quad\times T(x^rQ,\dots,x^rQ,t^{b-k}y_1\cdots y_k).
\end{aligned}
\]
For \(k=m\) the last slot is \(t^rQ\), and (1) shows that the right side vanishes at every point, hence is the zero polynomial. Immediately before the \(i\)-th operator \(D_{y_i,t}\), the polynomial has degree \(b-i+1\) in \(t\) and degree \(r\) in \(y_i\), since the earlier operators raised only the degrees of \(y_1,\dots,y_{i-1}\); and \(b-i+1-r=m-i+1\ge1\). By Lemma 3.1 of [A differential injectivity lemma](a-differential-injectivity-lemma.md) each operator is injective there, so \(H=0\). Hence, for all \(x,t\in V\) and all products \(Q\) of \(m\) vectors,
\[
T(x^rQ,\dots,x^rQ,t^b)=0 .\tag{2}
\]

*Step 3: the induction.* For fixed \(x,t\in V\),
\[
S(Q_1,\dots,Q_r)=T(x^rQ_1,\dots,x^rQ_r,t^b)
\]
is a symmetric \(r\)-linear form on \(\operatorname{Sym}^mV\), and by (2) it vanishes on the diagonal at every product of \(m\) vectors. As \(m\ge1\) and \(m\ge r^2\ge r(r-1)\), the induction hypothesis gives \(S=0\): for all \(Q_1,\dots,Q_r\in\operatorname{Sym}^mV\),
\[
T(x^rQ_1,\dots,x^rQ_r,t^b)=0 .\tag{3}
\]

*Step 4: removing the common power.* Fix \(t\in V\) and let \(v_1,\dots,v_r\) and \(x\) be vector variables. Consider
\[
f=T(v_1^b,\dots,v_r^b,t^b),
\]
of degree \(b\) in each \(v_i\) and degree \(0\) in \(x\). Apply \(D_{x,v_1}\) \(r\) times, then \(D_{x,v_2}\) \(r\) times, and so on up to \(v_r\). Each operator acts only on its own slot, and \(D_{x,v}^{\,r}(v^b)=\frac{b!}{m!}x^rv^m\), so
\[
\begin{aligned}
&D_{x,v_r}^{\,r}\cdots D_{x,v_1}^{\,r}f\\
&\quad=\Bigl(\frac{b!}{m!}\Bigr)^rT(x^rv_1^m,\dots,x^rv_r^m,t^b),
\end{aligned}
\]
which vanishes at every point by (3), with \(Q_i=v_i^m\), and so is the zero polynomial. Before any one of these \(r^2\) operators, the degree in \(x\) is at most \(r^2-1\), while its source \(v_i\) has been differentiated at most \(r-1\) times and has degree at least \(b-r+1=m+1\ge r^2+1\). So Lemma 3.1 of [A differential injectivity lemma](a-differential-injectivity-lemma.md) applies before every operator, and \(f=0\).

*Conclusion.* So \(T(v_1^b,\dots,v_r^b,t^b)=0\) for all \(v_1,\dots,v_r,t\in V\): \(T\) vanishes on all tuples of pure powers. Pure powers span \(\operatorname{Sym}^bV\) (Lemma 1.2 of [Symmetric powers and the Foulkes–Howe map](symmetric-powers-and-the-foulkes-howe-map.md)), and \(T\) is multilinear, so \(T=0\). \(\square\)

## 2. Proof of Theorem A

For \(a\ge2\) and \(b\ge a(a-1)\), Proposition 1.1 is the vanishing statement of the diagonal criterion, Proposition 3.1 of [Symmetric powers and the Foulkes–Howe map](symmetric-powers-and-the-foulkes-howe-map.md). So \(\mu_{a,b,V}\) is surjective. \(\square\)

## 3. An equivariant embedding

Fix a Hermitian inner product on \(V\), and give \(V^{\otimes k}\) the inner product for which \(\langle x_1\otimes\cdots\otimes x_k,y_1\otimes\cdots\otimes y_k\rangle\) equals \(\prod_i\langle x_i,y_i\rangle\). For \(g\in\mathrm{GL}(V)\) with adjoint \(g^*\), the adjoint of \(g^{\otimes k}\) is \((g^*)^{\otimes k}\), as one checks on simple tensors.

By Lemma 1.1 of [Symmetric powers and the Foulkes–Howe map](symmetric-powers-and-the-foulkes-howe-map.md), applied twice, \(\operatorname{Sym}^b(\operatorname{Sym}^aV)\) is identified with a subspace of \((V^{\otimes a})^{\otimes b}\), compatibly with the actions of \(\mathrm{GL}(V)\), where \(g\) acts by \(g^{\otimes ab}\); likewise \(\operatorname{Sym}^a(\operatorname{Sym}^bV)\) with a subspace of \((V^{\otimes b})^{\otimes a}\). Give both the restricted inner products. Each subspace is invariant under \(g\) and under \(g^*\), so the adjoint of the action of \(g\) on it is the action of \(g^*\). Write \(\rho(g)\) and \(\rho'(g)\) for the two actions.

*Proof of Corollary B.* Let \(\mu=\mu_{a,b,V}\), which is surjective by Theorem A and equivariant (Section 2 of [Symmetric powers and the Foulkes–Howe map](symmetric-powers-and-the-foulkes-howe-map.md)), and let \(\mu^*:\operatorname{Sym}^a(\operatorname{Sym}^bV)\to\operatorname{Sym}^b(\operatorname{Sym}^aV)\) be its adjoint. The kernel of \(\mu^*\) is the orthogonal complement of the image of \(\mu\), which is zero, so \(\mu^*\) is injective. For \(g\in\mathrm{GL}(V)\) and all \(x,y\),
\[
\begin{aligned}
\langle\mu^*\rho'(g)x,y\rangle&=\langle x,\rho'(g^*)\mu y\rangle\\
&=\langle x,\mu\rho(g^*)y\rangle\\
&=\langle\rho(g)\mu^*x,y\rangle ,
\end{aligned}
\]
so \(\mu^*\rho'(g)=\rho(g)\mu^*\). \(\square\)

This argument replaces the complete reducibility of polynomial representations, used in [OpenAI-FH, Section 5], by the adjoint of the canonical map. For \(a=6\) the corollary gives an equivariant embedding \(\operatorname{Sym}^6(\operatorname{Sym}^bV)\hookrightarrow\operatorname{Sym}^b(\operatorname{Sym}^6V)\) for every \(b\ge30\).

## 4. Scope

The bound \(a(a-1)\) is sufficient, not claimed to be the least. Below it, surjectivity can fail. For \(a=b\) the map is an endomorphism of \(\operatorname{Sym}^a(\operatorname{Sym}^aV)\), and for \((a,b)=(5,5)\) and \((6,6)\) it has a nonzero kernel for suitable \(V\) [CIM, Theorem 6], so it is not surjective; both pairs lie below the bound of Theorem A.

## 5. Exercises

**5.1** (easy). Write out the proof of Proposition 1.1 for \(a=2\), where \(r=1\) and \(m=b-1\).

**5.2** (medium). Let \(\dim V=2\), \(b=2\), and in the basis \(e_1^2,e_1e_2,e_2^2\) of \(\operatorname{Sym}^2V\) write elements as \((A,B,C)\). Show that the nonzero symmetric bilinear form \(T\) with \(T(w,w)=B^2-4AC\) vanishes at \((u^2,u^2)\) for every \(u\in V\), but not at \((P,P)\) for every product \(P\) of two vectors. So in Proposition 1.1 products cannot be replaced by pure powers.

**5.3** (easy). Explain why an endomorphism of a finite-dimensional space with a nonzero kernel is not surjective.

## 6. Solutions

**5.1.** Here \(Q=y_1\cdots y_{b-1}\). Step 1 gives \(T(xQ,tQ)=0\). Step 2 applies \(D_{y_1,t},\dots,D_{y_{b-1},t}\) to \(H=T(xQ,t^b)\); before the \(i\)-th operator the degrees are \(b-i+1\) in \(t\) and \(1\) in \(y_i\), so each is injective, and \(T(xQ,t^b)=0\). Step 3 is the case \(a=1\): \(Q\mapsto T(xQ,t^b)\) is linear and vanishes on products, so \(T(xQ_1,t^b)=0\) for all \(Q_1\in\operatorname{Sym}^{b-1}V\). Step 4 applies \(D_{x,v}\) once to \(T(v^b,t^b)\), giving \(b\,T(xv^{b-1},t^b)=0\); as \(v\) has degree \(b\ge2>0\) before it, \(T(v^b,t^b)=0\).

**5.2.** For \(u=se_1+te_2\), \(u^2=(s^2,2st,t^2)\) and \(B^2-4AC=4s^2t^2-4s^2t^2=0\). For \(P=(s_1e_1+t_1e_2)(s_2e_1+t_2e_2)\), with coordinates \((s_1s_2,\ s_1t_2+s_2t_1,\ t_1t_2)\), \(B^2-4AC=(s_1t_2-s_2t_1)^2\), which is nonzero for \(P=e_1e_2\). The form \(T\) is the polarization \(T(w,w')=BB'-2AC'-2A'C\).

**5.3.** By the rank–nullity theorem, the image has dimension \(\dim W-\dim\ker<\dim W\).

## References

- [OpenAI-FH] OpenAI, *Quadratic stabilization of the canonical Foulkes–Howe map*, OpenAI Math Release preprint, 25 September 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026
- [CIM] M.-W. Cheung, C. Ikenmeyer and S. Mkrtchyan, *Symmetrizing tableaux and the 5th case of the Foulkes conjecture*, Journal of Symbolic Computation 80 (2017), 833–843; arXiv:1509.03944, Theorem 6. https://arxiv.org/abs/1509.03944
