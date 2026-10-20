# Cubic theta and its Whittaker coefficients

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The coefficients \(\gamma_2(\mathfrak c)/(q_{\mathfrak c}^{1/2}q_{\mathfrak n})\) of the sums \(B_m(Z)\) of [*The coefficient family and the plan of the zero-free argument*](the-coefficient-family-and-the-plan-of-the-zero-free-argument.md) are Fourier coefficients of a cubic theta function: an automorphic form on a threefold cover of \(\mathrm{PGL}_2\) over \(F\), constructed by Kubota, Patterson, and Kazhdan and Patterson as a residue of Eisenstein series. Its Fourier coefficients are supported on ideals of the form \(\mathfrak c\mathfrak n^3\); this is why cubes appear in (3.1) of that lesson. This lesson states the properties of the cubic theta representation that the course uses, as a named result, and proves what is computed from them: the spherical Whittaker function at every prime outside \(S\), by an explicit Jacquet integral; the normalized product formula for the global Whittaker function; and the cocycle of the cover at \(S\).

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), (3.1)–(3.3) and Lemma 3.1; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), Section 1; [*Gauss sums and the correction characters*](gauss-sums-and-the-correction-characters.md), (3.1), Lemma 1.1 and Proposition 5.1; [*The adèle ring of a number field*](course:NT-ADL/NT-ADL-02), Theorem 2.3; [*Power residue symbols and reciprocity laws*](course:NT-CFT/power-residue-symbols-and-reciprocity-laws), Theorem 23.3.

## 1. The threefold cover

Write, for a field or ring of adèles,
\[
\begin{gathered}
n(x)=\begin{pmatrix}1&x\\0&1\end{pmatrix},\\
\bar n(x)=\begin{pmatrix}1&0\\x&1\end{pmatrix},\\
a(y)=\begin{pmatrix}y&0\\0&1\end{pmatrix},\\
w=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\end{gathered}
\]
At each place \(v\) of \(F\), Kubota's construction, in the determinant-modified form of Kazhdan and Patterson, uses the cubic Hilbert symbol to define a central extension of \(\mathrm{GL}_2(F_v)\) by \(\mu_3\); its cocycle restricted to the diagonal torus is
\[
\begin{gathered}
\begin{aligned}
&\sigma_{c,v}\bigl(\operatorname{diag}(a,b),\operatorname{diag}(a',b')\bigr)\\
&\quad =(a,b')_{3,v}\,(ab,a'b')_{3,v}^{\,c},
\end{aligned}\\
c\in\mathbb Z/3\mathbb Z .\quad(1.1)
\end{gathered}
\]
On two scalars this is \((z,z')_{3,v}^{1+4c}\), and for \(c=2\) it is \(1\): the preimage of the scalars is then central and the ordinary scalar section is a homomorphism. Quotienting by the split scalars gives a threefold cover \(\widetilde{\mathrm{PGL}}_2(F_v)\), and the restricted product of these gives a cover of \(\mathrm{PGL}_2(\mathbb A_F)\).

On the quotient torus, the section of \(a(y)\) satisfies \(a(x)a(y)=(x,y)_{3,v}^2\,a(xy)\). In a representation in which \(\mu_3\) acts through a fixed embedding \(\iota\colon\mu_3(F)\to\mathbb C^\times\) (a **genuine** representation), write
\[
\begin{aligned}
&\pi(a(x))\pi(a(y))\\
&\quad =\mathcal C_v(x,y)\,\pi(a(xy)) .\quad(1.2)
\end{aligned}
\]
Since \(-1=\zeta_{12}^6\) is a cube, \((\cdot,\cdot)_{3,v}^2\) is alternating and bimultiplicative. At a place \(v\notin S\) it is trivial on two units, and on a uniformizer and a unit it is the cubic residue symbol or its inverse, with the same orientation at all places. Choosing \(\iota\) accordingly, for every exterior prime \(\mathfrak p\), every uniformizer \(\varpi\) and all units \(u,u'\),
\[
\begin{gathered}
\mathcal C_{\mathfrak p}(\varpi,u)=\chi_{\mathfrak p}(u)^{-2},\\
\mathcal C_{\mathfrak p}(u,\varpi)=\chi_{\mathfrak p}(u)^{2},\\
\mathcal C_{\mathfrak p}(u,u')=1,\\
\mathcal C_{\mathfrak p}(\varpi,\varpi)=1 .\quad(1.3)
\end{gathered}
\]
Comparing with the tame formula (3.2) of [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md) and Lemma 3.1 there, both sides of the identity \(\mathcal C_{\mathfrak p}(x,y)=(x,y)_{6,\mathfrak p}^2\) are bimultiplicative and agree on these generators; so
\[
\begin{gathered}
\mathcal C_{\mathfrak p}(x,y)=(x,y)_{6,\mathfrak p}^2\\
(x,y\in F_{\mathfrak p}^\times,\ \mathfrak p\notin S).\quad(1.4)
\end{gathered}
\]

## 2. The cubic theta representation

**Named result N1** (Kazhdan–Patterson). Let \(F\) be a number field containing \(\mu_3\), and use the cover of Section 1 with \(c=2\). With the ordinary torus section and the canonical splittings of the root groups:

1. *The cover.* It splits over \(\mathrm{PGL}_2(F)\). In it, the lifts satisfy
\[
\begin{gathered}
n(x)a(y)=a(y)n(x/y),\\
wa(y)w^{-1}=a(y^{-1}),\\
wn(H)=n(H^{-1})a(-H^{-2})\bar n(H^{-1})\\
(H\ne0).\quad(2.1)
\end{gathered}
\]
At an exterior prime the compact subgroup \(\mathrm{PGL}_2(\mathcal O_{\mathfrak p})\) splits, and the splitting agrees with the sections on unit diagonals, on \(w\), and on integral upper and lower root elements.
2. *The local exceptional representation at an exterior prime \(\mathfrak p\).* Let \(Q=q_{\mathfrak p}\). There is a three-dimensional genuine representation \(\sigma^-\) of the covering torus with a basis \(e_0,e_1,e_2\), \(e_j=Q^{-j/6}\sigma^-(a(\varpi^j))e_0\) and \(e_{j+3}=e_j\) for all \(j\in\mathbb Z\), such that
\[
\begin{gathered}
\begin{aligned}
&\sigma^-(a(\varpi^ju))\,e_0\\
&\quad =Q^{j/6}\chi_{\mathfrak p}(u)^{2j}e_j
\end{aligned}\\
(j\in\mathbb Z,\ u\in\mathcal O_{\mathfrak p}^\times).\quad(2.2)
\end{gathered}
\]
In the normalized induced representation \(I^-\), realized by vector-valued functions with \(f(n(x)a(y)g)=|y|_{\mathfrak p}^{1/2}\sigma^-(a(y))f(g)\), the spherical vector \(f^\circ\) with \(f^\circ(k)=e_0\) on the compact subgroup lies in the irreducible subrepresentation \(\Theta_{\mathfrak p}\) of \(I^-\), and \(\Theta_{\mathfrak p}\) has a one-dimensional space of Whittaker functionals.
3. *The global representation.* There is an irreducible genuine automorphic representation \(\Theta=\bigotimes'_v\Theta_v\) of the cover of \(\mathrm{PGL}_2(\mathbb A_F)\), with \(\Theta_{\mathfrak p}\) as in part 2 at almost all exterior primes, whose automorphic realization \(\varphi\mapsto\theta_\varphi\) has a nonzero Whittaker functional
\[
\lambda(\varphi)=\int_{F\backslash\mathbb A_F}\theta_\varphi(n(x))\overline{\psi(x)}\,dx ,
\]
and every \(\Theta_v\) has a one-dimensional space of Whittaker functionals. The automorphic functions have the absolutely and locally uniformly convergent Fourier expansion
\[
\begin{aligned}
&\theta_\varphi(g)=\theta_{\varphi,N}(g)\\
&\qquad+\sum_{\nu\in F^\times}\lambda\bigl(\Theta(a(\nu)g)\varphi\bigr),\\
&\theta_{\varphi,N}(g)\\
&\qquad=\int_{F\backslash\mathbb A_F}\theta_\varphi(n(x)g)\,dx .\quad(2.3)
\end{aligned}
\]
At a complex place \(\Theta_v\) is the spherical principal series of \(\mathrm{PGL}_2(\mathbb C)\) with normalized characters \((|\cdot|_v^{1/6},|\cdot|_v^{-1/6})\), and the constant term \(\theta_{\varphi,N}\) lies in the induction from the Weyl-conjugate datum; in particular its dependence on a complex diagonal \(a(y)\) is radial.
4. *Exponents.* At a finite place, the twisted Jacquet quotient of \(\Theta_v\) is finite dimensional, and the element \(a(\varpi_v^3)\), central in the covering torus, acts on the ordinary Jacquet module of \(\Theta_v\) with eigenvalues of absolute values \(q_v^{-1}\) and \(q_v^{-2}\).

These statements are Kazhdan and Patterson's Proposition 0.1.1, Proposition 0.1.3 and Section 0.2 (the cover), Sections 0.3 and I.1 with Lemma I.1.3 (the torus representation and the spherical line), Theorem I.2.9 (a), (b), (f) (the exceptional representation), Corollary I.3.6 (uniqueness of Whittaker functionals; the case \(r=2\), \(n=3\), \(2(c+1)\equiv0\pmod3\)), Proposition I.2.1, Lemma I.3.2 and Theorem I.2.9 (exponents), Theorems I.6.4–I.6.5 (complex places), and Sections II.1–II.2 with Theorems II.2.1 and II.2.5 (the global representation and its Whittaker functional), together with their corrections to the global formula. They are used without proof in the programme. The specialization to \(c=2\), the exceptional character \(\omega_v(s_v(\operatorname{diag}(t^3,t^{-3})))=|t|_v\), and its central datum are checked against Kazhdan and Patterson's conditions in Appendix A of [OpenAI-029].

The places at which a chosen pure tensor in \(\Theta\) is not the distinguished spherical vector, and the places where Theorem I.2.9 (f) is not available, form a finite set; it is one of the two finite sets included in \(S\) in Lesson 2.

## 3. The normalized global Whittaker function

**Lemma 3.1** ([OpenAI-029, (5.2)]). There is a pure tensor \(\varphi^\circ\) with \(\lambda(\varphi^\circ)\ne0\). Choose \(S\) to contain its nondistinguished places, and for \(\mathfrak p\notin S\) let \(W_{\mathfrak p}\) be the spherical Whittaker function of \(\Theta_{\mathfrak p}\) normalized by \(W_{\mathfrak p}(1)=1\). For every pure tensor \(\varphi=\varphi_S\otimes\bigotimes_{v\notin S}\varphi_v\) with \(\varphi_v=\varphi_v^\circ\) for almost all \(v\),
\[
\begin{aligned}
&\mathcal W_\varphi(g):=\lambda(\Theta(g)\varphi)\\
&\quad=\mathcal W_{S,\varphi_S}(g_S)\prod_{v\notin S}W_{v,\varphi_v}(g_v),\quad(3.1)
\end{aligned}
\]
where \(\mathcal W_{S,\varphi_S}\) is a finite sum of products of local Whittaker functions at the places of \(S\), factored at the complex places.

*Proof.* The restricted tensor product is spanned by pure tensors, so some pure tensor has \(\lambda(\varphi^\circ)\ne0\). For \(v\notin S\), varying only the \(v\)-component of \(\varphi^\circ\) defines a Whittaker functional of \(\Theta_v\), nonzero at \(\varphi_v^\circ\); normalize it there. If finitely many other components have been varied, the resulting functional of the \(v\)-component is still a Whittaker functional, hence a multiple of the normalized one by uniqueness (N1); evaluating at \(\varphi_v^\circ\) identifies the multiple. Induction on the number of varied components gives (3.1) with the component at \(S\) collected into \(\mathcal W_S\). At the finite places of \(S\), \(\lambda\) factors through the tensor product of the finite-dimensional twisted Jacquet quotients (N1(4)), so it is a finite sum of products of local functionals; at the complex places uniqueness factors it. \(\square\)

## 4. The spherical Whittaker function at an exterior prime

Fix an exterior prime \(\mathfrak p\) and drop it from the notation: \(\psi=\psi_{\mathfrak p}\) has conductor \(\mathcal O\), \(\mathcal O\) has additive volume \(1\), \(\chi=\chi_{\mathfrak p}\), \(Q=q_{\mathfrak p}\), and \(\varpi\) is a uniformizer. Write
\[
\begin{gathered}
g_j=Q^{-1/2}\sum_{x\bmod\mathfrak p}\chi(x)^j\psi(x/\varpi)\\
(j\in\mathbb Z),
\end{gathered}
\]
with the unit mask. For \(j\not\equiv0\pmod 6\), \(|g_j|=1\) and \(g_jg_{-j}=\chi(-1)^j=1\) (Lemma 1.1 of [*Gauss sums and the correction characters*](gauss-sums-and-the-correction-characters.md)); in particular \(g_2g_4=1\). Since \(\chi(-1)=1\), replacing \(\psi(x/\varpi)\) by its conjugate does not change \(g_j\).

**Proposition 4.1** (local Whittaker values [OpenAI-029, Proposition 5.1(ii) and Appendix A]). For \(u\in\mathcal O^\times\), \(e\in\mathbb Z\) and integers \(k\ge0\),
\[
\begin{aligned}
&W_{\mathfrak p}(a(\varpi^eu))=\chi(u)^{2e}\\
&\quad\cdot\begin{cases}0,&e<0,\\ Q^{-k},&e=3k,\\ Q^{-k-1/2}\,g_2,&e=3k+1,\\ 0,&e=3k+2 .\end{cases}\quad(4.1)
\end{aligned}
\]

*Proof.* *The Jacquet integral.* For smooth \(f\in I^-\) put
\[
\mathscr J(f)=\lim_{L\to\infty}\int_{\varpi^{-L}\mathcal O}f(wn(x))\,\overline{\psi(x)}\,dx .
\]
For large \(|x|\), \(\bar n(x^{-1})\) fixes \(f\) on the right, and (2.1) with the transformation law gives \(f(wn(x))=|x|^{-1}\sigma^-(a(-x^{-2}))f(1)\). Choose \(m\) so that \(1+\varpi^m\mathcal O\) consists of cubes and fixes \(f(1)\). On a shell \(x=\varpi^{-l}v\), \(v\in\mathcal O^\times\), this expression is unchanged when \(v\) is replaced by \(vu\) with \(u\in1+\varpi^m\mathcal O\): the cocycles with \(u\) are trivial and \(a(u^{-2})\) fixes \(f(1)\). The set \(\{\varpi^{-l}vu:u\in1+\varpi^m\mathcal O\}\) is the additive coset \(\varpi^{-l}v+\varpi^{m-l}\mathcal O\), and \(\psi\) has integral zero over it once \(l>m\), because \(\psi\) is then nontrivial on \(\varpi^{m-l}\mathcal O\). So the limit stabilizes. Translation of \(x\) shows \(\mathscr J(\pi(n(t))f)=\psi(t)\mathscr J(f)\); each coordinate of \(\mathscr J\) in the basis \(e_0,e_1,e_2\) is a Whittaker functional on \(I^-\).

*The shells.* Let \(e\ge0\) and \(J_e=\mathscr J(\pi(a(\varpi^e))f^\circ)\)\(=\int f^\circ(wn(x)a(\varpi^e))\overline{\psi(x)}\,dx\). Put \(x=\varpi^eH\). By (2.1), \(wn(x)a(\varpi^e)=wa(\varpi^e)n(H)\)\(=a(\varpi^{-e})wn(H)\). The measure gives \(Q^{-e}\), the modular factor of \(a(\varpi^{-e})\) gives \(Q^{e/2}\), and \(\sigma^-(a(\varpi^{-e}))\) shifts the basis index by \(-e\) with the factor \(Q^{-e/6}\) from (2.2), with no cocycle between pure uniformizer powers. So every shell carries the common factor \(Q^{-e+e/2-e/6}=Q^{-2e/3}\).

For \(H\in\mathcal O\), \(wn(H)\) is in the compact subgroup and \(\psi(\varpi^eH)=1\): this region contributes \(e_{-e}\). For \(H=\varpi^{-l}v\) with \(l\ge1\), \(v\in\mathcal O^\times\), (2.1) gives \(wn(H)=n(H^{-1})a(-H^{-2})\bar n(H^{-1})\) with the last factor compact. The modular factor of \(a(-H^{-2})\) is \(Q^{-l}\); by (1.2) and (1.3), \(a(\varpi^{2l}v^{-2})=\mathcal C(\varpi^{2l},v^{-2})^{-1}a(\varpi^{2l})a(v^{-2})\) with \(\mathcal C(\varpi^{2l},v^{-2})^{-1}=\chi(v)^{-8l}\), and \(\sigma^-(a(\varpi^{2l}))e_0=Q^{l/3}e_{2l}\); the sign in \(-H^{-2}\) has no effect, because \(-1\) is a sixth power. With \(dH=Q^l\,dv\), the shell contributes, inside the common factor,
\[
\begin{gathered}
Q^{l/3}\,e_{2l-e}\;I_{e,l},\\
I_{e,l}=\int_{\mathcal O^\times}\chi(v)^{-2l}\,\overline{\psi(\varpi^{e-l}v)}\,dv ,
\end{gathered}
\]
where \(\chi^{-8l}=\chi^{-2l}\) as \(\chi^6=1\). For \(l\le e\) the additive factor is \(1\), and \(I_{e,l}=1-Q^{-1}\) if \(3\mid l\) and \(0\) otherwise. For \(l=e+1\), \(I_{e,l}=Q^{-1/2}g_{-2l}\) if \(3\nmid l\) and \(I_{e,l}=-Q^{-1}\) if \(3\mid l\). For \(l>e+1\), each class modulo \(\varpi^{l-e-1}\) splits into \(Q\) lifts on which \(\chi\) is constant and \(\psi\) sums to zero, so \(I_{e,l}=0\).

*Summing.* For \(k\ge0\) the unit ball and the shells \(l=3,6,\dots,3k\) all carry the same basis vector, with total coefficient \(1+(1-Q^{-1})\sum_{j=1}^kQ^j=Q^k\). For \(e=3k\) the terminal shell \(l=3k+1\) contributes \(Q^{k+1/3-1/2}g_{-2}e_2=Q^{k-1/6}g_4e_2\); for \(e=3k+1\) the terminal shell \(l=3k+2\) contributes \(Q^{k+2/3-1/2}g_{-4}e_0=Q^{k+1/6}g_2e_0\); for \(e=3k+2\) the terminal shell \(l=3k+3\) contributes \(-Q^k\) times the vector \(e_1\) carried by the others. With the common factor,
\[
\begin{aligned}
J_{3k}&=Q^{-k}\bigl(e_0+Q^{-1/6}g_4e_2\bigr),\\
J_{3k+1}&=Q^{-k}\bigl(Q^{-1/2}g_2e_0+Q^{-2/3}e_2\bigr)\\
&=Q^{-k-1/2}g_2\bigl(e_0+Q^{-1/6}g_4e_2\bigr),\\
J_{3k+2}&=0,\quad(4.2)
\end{aligned}
\]
using \(g_2g_4=1\).

*Normalization.* \(J_0=e_0+Q^{-1/6}g_4e_2\ne0\). Choose a coordinate of \(\mathscr J\) that is nonzero at \(J_0\); it is a Whittaker functional on \(I^-\), nonzero on the subrepresentation \(\Theta_{\mathfrak p}\ni f^\circ\), hence the Whittaker functional of \(\Theta_{\mathfrak p}\) up to a scalar (N1(2)). Since every \(J_e\) is a multiple of \(J_0\), (4.2) gives the values (4.1) for \(u=1\), \(e\ge0\). For \(e<0\) choose \(x\in\mathcal O\) with \(\psi(\varpi^ex)\ne1\); the spherical vector is fixed by \(n(x)\), and \(W(a(\varpi^e))=W(a(\varpi^e)n(x))\)\(=\psi(\varpi^ex)W(a(\varpi^e))\), so the value is \(0\). Finally \(a(\varpi^eu)=\mathcal C(\varpi^e,u)^{-1}a(\varpi^e)a(u)\) with \(\mathcal C(\varpi^e,u)^{-1}=\chi(u)^{2e}\) by (1.3), and \(a(u)\) fixes the spherical vector. \(\square\)

The middle value is \(Q^{-k-1}\sum_x\chi(x)^2\psi(x/\varpi)\). The formula is compatible with the change of uniformizer: replacing \(\varpi\) by \(\varpi u\) multiplies the \(e=1\) value by \(\chi(u)^2\), both through the unit rule and through the substitution \(x\mapsto ux\) in the Gauss sum.

## 5. The exterior coefficient

**Corollary 5.1** (the exterior theta coefficient [OpenAI-029, Corollary 5.2]). At every exterior prime use its allowed generator as the uniformizer in Proposition 4.1. Let \(A\in R\setminus\{0\}\) be an allowed generator of an exterior ideal \(\mathfrak A\). Then
\[
\begin{aligned}
&\prod_{\mathfrak p\notin S}W_{\mathfrak p}(a(A))\\
&\quad=\begin{cases}\dfrac{\gamma_2(\mathfrak c)}{q_{\mathfrak c}^{1/2}q_{\mathfrak n}},&\begin{aligned}&\mathfrak A=\mathfrak c\mathfrak n^3,\\&\mathfrak c\ \text{squarefree},\end{aligned}\\ 0,&\text{otherwise}.\end{cases}\quad(5.1)
\end{aligned}
\]
In the first case \(\mathfrak c\) and \(\mathfrak n\) are uniquely determined; they need not be coprime.

*Proof.* By (4.1) only the valuations \(3k\) and \(3k+1\) survive, which is the unique decomposition \(\mathfrak A=\mathfrak c\mathfrak n^3\) with \(\mathfrak c\) squarefree, and the magnitudes are \(q_{\mathfrak p}^{-k}\) and \(q_{\mathfrak p}^{-k-1/2}\). Use the allowed product generator \(A=cn^3\); another allowed generator differs by an element of \(U_S^6\), which does not change the local values. Let \(l=v_{\mathfrak p}(\mathfrak n)\). At \(\mathfrak p\mid\mathfrak c\) the valuation is \(e=1+3l\) and the unit of \(A\) is \((c/p)(n/p^l)^3\), so the unit factor in (4.1) is \(\chi_{\mathfrak p}(c/p)^{2+6l}\chi_{\mathfrak p}(n/p^l)^{3(2+6l)}=\chi_{\mathfrak p}(c/p)^2\). At a prime of \(\mathfrak n\) not dividing \(\mathfrak c\), \(e=3l\), the unit is \((n/p^l)^3\), and its factor \(\chi_{\mathfrak p}(n/p^l)^{18l}\) is \(1\). The prime sum \(g_{2,\mathfrak p}\) equals \(\gamma_2(\mathfrak p)\) (the sign of the additive argument is irrelevant since \(\chi_{\mathfrak p}(-1)=1\)). By (5.2) of Lesson 4, \(\prod_{\mathfrak p\mid\mathfrak c}\chi_{\mathfrak p}(c/p)^2\gamma_2(\mathfrak p)=\gamma_2(\mathfrak c)\). \(\square\)

## 6. The cocycle at S

Put \(\mathcal C_S=\prod_{v\in S}\mathcal C_v\), a function on \(F_S^\times\times F_S^\times\).

**Lemma 6.1** ([OpenAI-029, (5.9)]). For all \(x,y\in F_S^\times\),
\[
\mathcal C_S(x,y)=H_S(x,y)^2 .
\tag{6.1}
\]
In particular \(\mathcal C_S\) depends only on the classes of \(x,y\) in \(\mathcal V=F_S^\times/F_S^{\times6}\).

*Proof.* For \(a,b\in F^\times\), the product of the cocycles over all places is \(\prod_v\iota\bigl((a,b)_{3,v}^2\bigr)=1\) by Hilbert's product formula (Theorem 23.3 of [*Power residue symbols and reciprocity laws*](course:NT-CFT/power-residue-symbols-and-reciprocity-laws)), and likewise \(\prod_v(a,b)_{6,v}^2=1\). Hence, by (1.4),
\[
\begin{aligned}
\mathcal C_S(a,b)&=\prod_{v\notin S}\mathcal C_v(a,b)^{-1}\\
&=\prod_{v\notin S}(a,b)_{6,v}^{-2}\\
&=\prod_{v\in S}(a,b)_{6,v}^2\\
&=H_S(a,b)^2 .
\end{aligned}
\]
Both sides of (6.1) are locally constant on \(F_S^\times\times F_S^\times\), and \(F^\times\) is dense in \(F_S^\times\) (weak approximation, a consequence of Theorem 2.3 of [*The adèle ring of a number field*](course:NT-ADL/NT-ADL-02)). \(\square\)

## 7. Exercises

**7.1.** Show that for \(c=2\) the cocycle (1.1) on the quotient torus satisfies \(\sigma(a(x),a(y))=(x,y)_{3,v}^2\), and that it is alternating because \(-1\) is a cube in \(F\).

**7.2.** Verify the identity \(n(x)a(y)=a(y)n(x/y)\) and \(wa(y)w^{-1}=a(y^{-1})\) at the level of matrices in \(\mathrm{PGL}_2\).

**7.3.** Using (4.1), show that the spherical Whittaker function satisfies \(W_{\mathfrak p}(a(\varpi^{e+3}u))=Q^{-1}W_{\mathfrak p}(a(\varpi^eu))\) for \(e\ge0\), and explain this through the eigenvalue of \(a(\varpi^3)\).

**7.4.** Compute \(\prod_{\mathfrak p}W_{\mathfrak p}(a(A))\) for \(\mathfrak A=\mathfrak p^4\) and for \(\mathfrak A=\mathfrak p^5\).

**7.5.** Check the shell bookkeeping of the proof of Proposition 4.1 for \(e=1\): list the unit ball and the shells \(l=1,2\) with their basis vectors and coefficients.

## 8. Solutions

**7.1.** With \(a(x)=\operatorname{diag}(x,1)\) and \(a(y)=\operatorname{diag}(y,1)\), (1.1) gives \((x,1)_{3,v}(x,y)_{3,v}^{2}=(x,y)_{3,v}^2\). Alternation follows from \((x,x)_{3,v}=(x,-1)_{3,v}^{-1}=1\), since \(-1\) is a cube.

**7.2.** \(n(x)a(y)=\begin{pmatrix}y&x\\0&1\end{pmatrix}=a(y)n(x/y)\), and \(wa(y)w^{-1}=\operatorname{diag}(1,y)\), which equals \(a(y^{-1})\) modulo scalars.

**7.3.** Valuations \(e\) and \(e+3\) lie in the same residue class modulo \(3\), \(k\) increases by one, and \(\chi(u)^{2(e+3)}=\chi(u)^{2e}\). The value of the normalized Weyl-conjugate inducing character on \(a(\varpi^3)\) is \(Q^{1/2}\) and its modular factor is \(Q^{-3/2}\); their product \(Q^{-1}\) is the eigenvalue on the spherical Whittaker function.

**7.4.** \(4=3\cdot1+1\) gives \(\mathfrak c=\mathfrak p\), \(\mathfrak n=\mathfrak p\) and the value \(\gamma_2(\mathfrak p)/(q_{\mathfrak p}^{1/2}q_{\mathfrak p})\); \(5\equiv2\pmod3\) gives \(0\).

**7.5.** For \(e=1\): the unit ball gives \(e_{-1}=e_2\) with coefficient \(1\); the shell \(l=1\) has \(I_{1,1}=0\) since \(3\nmid1\); the shell \(l=2=e+1\) has \(3\nmid2\), coefficient \(Q^{2/3}Q^{-1/2}g_{-4}=Q^{1/6}g_2\) and vector \(e_{3}=e_0\); shells \(l\ge3\) vanish. With the common factor \(Q^{-2/3}\) this is \(J_1=Q^{-1/2}g_2e_0+Q^{-2/3}e_2\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 5 and Appendix A. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- [KP] D. A. Kazhdan and S. J. Patterson, *Metaplectic forms*, Publ. Math. IHÉS 59 (1984), 35–142; corrections, Publ. Math. IHÉS 62 (1985), 203. http://www.numdam.org/item/PMIHES_1984__59__35_0/ and http://www.numdam.org/item/PMIHES_1985__62__203_0/
- T. Kubota, *Topological covering of SL(2) over a local field*, J. Math. Soc. Japan 19 (1967), 114–121. https://doi.org/10.2969/jmsj/01910114
