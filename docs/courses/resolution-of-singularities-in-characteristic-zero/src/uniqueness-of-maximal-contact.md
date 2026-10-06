# Uniqueness of maximal contact

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Hypersurfaces of maximal contact are not unique, and a construction that restricts to one of them must give the same blow-ups whichever one is chosen. This lesson proves this for MC-invariant ideals, a condition that says the ideal does not change under coordinate changes moving one hypersurface of maximal contact to another. The proof has two steps. First, two such hypersurfaces are related by a formal automorphism that preserves the ideal and is close to the identity, in a precise sense measured by the ideal of maximal contact. Second, blow-up sequences that correspond under such an automorphism, realised on an étale neighbourhood, are equal on the nose.

We use [Smooth blow-ups and transforms of ideals](smooth-blowups-and-transforms-of-ideals.md), [Blow-up sequences and the main theorems](blow-up-sequences-and-the-main-theorems.md), [Derivative ideals under blowing up](derivative-ideals-under-blowing-up.md) and [Hypersurfaces of maximal contact](hypersurfaces-of-maximal-contact.md).

## 1. Completions

Let \(p\) be a closed point of a smooth scheme \(X\) with residue field \(K\). As in the proof of the Taylor criterion in the first lesson, \(\widehat{\mathcal O}_{X,p}=K'[[x_1,\ldots,x_n]]\) for any coordinate system centred at \(p\), where \(K'\supset k\) is the unique coefficient field containing \(k\): it is the field generated over \(k\) by the Hensel lift of a primitive element of \(K/k\), and any coefficient field containing \(k\) contains that lift, by uniqueness in Hensel's lemma. The coordinate derivations extend to the completion as the formal partial derivatives, so for an ideal sheaf \(\mathcal I\), \(D(\widehat{\mathcal I})=\widehat{D(\mathcal I)}\), where on the left \(D\) is computed with formal partials; in particular \(MC(\widehat{\mathcal I})=\widehat{MC(\mathcal I)}\).

**Lemma 1.1.** Let \(\mathcal F\) be a coherent sheaf on a scheme of finite type over \(k\) and \(p\) a closed point. If \(\widehat{\mathcal F_p}=0\), then \(\mathcal F\) vanishes on a neighbourhood of \(p\). In particular, coherent ideals \(\mathcal A\subset\mathcal B\) with \(\widehat{\mathcal A}_p=\widehat{\mathcal B}_p\) agree near \(p\), and an inclusion of coherent ideals \(\mathcal A\subset\mathcal B\) holds near \(p\) if it holds after completion at \(p\).

**Proof.** Completion of the local ring is faithfully flat ([Completion](course:AG-CA/AG-CA-19), Theorem 3.2), so \(\mathcal F_p=0\), and a coherent sheaf with zero stalk vanishes near the point. For the inclusion apply this to \((\mathcal A+\mathcal B)/\mathcal B\). \(\square\)

## 2. Automorphisms close to the identity

Let \(R=K[[x_1,\ldots,x_n]]\), \(K\) a field of characteristic zero containing \(k\), with maximal ideal \(\mathfrak m\), and let \(B\subset\mathfrak m\) be an ideal. For \(b_1,\ldots,b_n\in B\) the continuous \(K\)-algebra endomorphism \(\sigma\) with \(\sigma(x_i)=x_i+b_i\) is an automorphism when the linear parts of the \(x_i+b_i\) are linearly independent. We call such automorphisms *of the form* \(\mathbf 1+B\). For \(f\in R\) and \(b\in B^n\), Taylor's formula

\[
f(x+b)=\sum_\alpha\frac{b^\alpha}{\alpha!}\,\partial^\alpha f
\]

holds: it holds for polynomials, both sides depend continuously on \(f\), and the sum converges because \(b^\alpha\in\mathfrak m^{|\alpha|}\).

**Proposition 2.1.** For an ideal \(\mathcal I\subset R\) the following are equivalent:

1. \(\sigma(\mathcal I)=\mathcal I\) for every automorphism \(\sigma\) of the form \(\mathbf 1+B\);
2. \(B\cdot D(\mathcal I)\subset\mathcal I\);
3. \(B^j\cdot D^j(\mathcal I)\subset\mathcal I\) for every \(j\ge1\).

**Proof.** (3)⇒(1). Let \(f\in\mathcal I\). Each term \(\frac{b^\alpha}{\alpha!}\partial^\alpha f\) lies in \(B^{|\alpha|}D^{|\alpha|}(\mathcal I)\subset\mathcal I\). So for every \(s\), \(\sigma(f)\in\mathcal I+\mathfrak m^{s+1}\). By Krull's intersection theorem applied to \(R/\mathcal I\) ([Stacks, Tag 00IQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-intersection-powers-ideal-module)), \(\bigcap_s(\mathcal I+\mathfrak m^{s+1})=\mathcal I\), so \(\sigma(\mathcal I)\subset\mathcal I\). Then \(\mathcal I\subset\sigma^{-1}(\mathcal I)\subset\sigma^{-2}(\mathcal I)\subset\cdots\) stabilizes because \(R\) is Noetherian, say \(\sigma^{-t}(\mathcal I)=\sigma^{-t-1}(\mathcal I)\); applying \(\sigma^{t+1}\) gives \(\sigma(\mathcal I)=\mathcal I\).

(1)⇒(2). Let \(b\in B\), \(f\in\mathcal I\) and \(1\le i\le n\). For all but at most one \(\lambda\in k\), the endomorphism \(x_i\mapsto x_i+\lambda b\), \(x_l\mapsto x_l\) (\(l\ne i\)), is an automorphism of the form \(\mathbf 1+B\): the linear part of \(x_i+\lambda b\) has \(x_i\)-coefficient \(1+\lambda c\), where \(c\) is the \(x_i\)-coefficient of \(b\). Fix \(s\). Modulo \(\mathfrak m^{s+1}\),

\[
f(x_1,\ldots,x_i+\lambda b,\ldots,x_n)\equiv\sum_{t=0}^s\lambda^t\,\frac{b^t}{t!}\,\partial_i^tf.
\]

The left side lies in \(\mathcal I\) for \(s+1\) distinct admissible values \(\lambda_0,\ldots,\lambda_s\), which exist because \(k\) is infinite. The Vandermonde matrix \((\lambda_u^t)\) is invertible, so each \(\frac{b^t}{t!}\partial_i^tf\) lies in \(\mathcal I+\mathfrak m^{s+1}\), in particular \(b\,\partial_if\). Letting \(s\to\infty\), \(b\,\partial_if\in\mathcal I\). Since \(D(\mathcal I)\) is generated by \(\mathcal I\) and the \(\partial_if\), (2) follows.

(2)⇒(3). By induction on \(j\). \(B^{j+1}D^{j+1}(\mathcal I)\) is generated by the products \(b_0\cdots b_j\,g\) and \(b_0\cdots b_j\,\partial_ig\) with \(b_t\in B\) and \(g\in D^j(\mathcal I)\). The first lie in \(B^jD^j(\mathcal I)\subset\mathcal I\). For the second, the product rule gives

\[
b_0\cdots b_j\,\partial_ig=b_0\,\partial_i(b_1\cdots b_jg)-\sum_{t=1}^j(\partial_ib_t)\,b_0\cdots\widehat{b_t}\cdots b_j\,g .
\]

The first term lies in \(B\cdot D(B^jD^j(\mathcal I))\subset B\cdot D(\mathcal I)\subset\mathcal I\), and each remaining term lies in \(B^jD^j(\mathcal I)\subset\mathcal I\). \(\square\)

## 3. MC-invariant ideals and formal uniqueness

**Definition 3.1.** An ideal \(\mathcal I\) with \(m=\operatorname{maxord}\mathcal I\ge1\) is *MC-invariant* if \(MC(\mathcal I)\cdot D(\mathcal I)\subset\mathcal I\).

By Proposition 2.1 with \(B=MC(\widehat{\mathcal I})\), an MC-invariant ideal is preserved, after completion at any closed point, by every automorphism of the form \(\mathbf 1+MC(\widehat{\mathcal I})\).

**Definition 3.2 (étale equivalence).** Let \(\mathcal I\) have \(m=\operatorname{maxord}\mathcal I\), let \(E=(E^1,\ldots,E^s)\) be snc and \(H,H'\) MC-hypersurfaces for \(\mathcal I\). Write \(\Delta\subset X\times X\) for the diagonal, with ideal \(\mathcal I_\Delta\). We say \(H\) and \(H'\) are *étale equivalent* with respect to \((X,\mathcal I,E)\) if there are a scheme \(U\) and two étale morphisms \(\psi,\psi':U\to X\), each with image containing \(\operatorname{cosupp}(\mathcal I,m)\), such that

1. \(\psi^{-1}(H)=\psi'^{-1}(H')\);
2. \(\psi^*\mathcal I=\psi'^*\mathcal I\);
3. \(\psi^{-1}(E^i)=\psi'^{-1}(E^i)\) for every \(i\);
4. \((\psi,\psi')^{-1}\mathcal I_\Delta\cdot\mathcal O_U\subset MC(\psi^*\mathcal I)\).

Condition (4) says, locally, that \(\psi^*h-\psi'^*h\in MC(\psi^*\mathcal I)\) for the functions \(h\); it means that \(\psi\) and \(\psi'\) agree on the closed subscheme \(V(MC(\psi^*\mathcal I))\), which lies over \(\operatorname{cosupp}(\mathcal I,m)\).

**Theorem 3.3 (uniqueness of maximal contact).** Let \(\mathcal I\) be MC-invariant with \(m=\operatorname{maxord}\mathcal I\), \(E\) snc, and \(H,H'\) MC-hypersurfaces for \(\mathcal I\) such that \((H,E)\) and \((H',E)\) are snc. Then \(H\) and \(H'\) are étale equivalent with respect to \((X,\mathcal I,E)\).

**Proof.** Both \(H\) and \(H'\) contain \(\operatorname{cosupp}(\mathcal I,m)\). Indeed \(\operatorname{cosupp}(\mathcal I,m)=V(MC(\mathcal I))\) by [Hypersurfaces of maximal contact, Lemma 1.2](hypersurfaces-of-maximal-contact.md#1-the-ideal-of-maximal-contact), and locally \(H=V(h)\) with \(h\) a section of \(MC(\mathcal I)\).

*Formal step.* Fix a closed point \(p\in\operatorname{cosupp}(\mathcal I,m)\), with local equations \(x_1,x_1'\in MC(\mathcal I)_p\) of \(H\) and \(H'\). Both have order \(1\) at \(p\), because \(H\) and \(H'\) are smooth hypersurfaces through \(p\). Let \(E^{i}\), \(i\in A\), be the members through \(p\), with local equations \(e_i\). Since \((H,E)\) and \((H',E)\) are snc at \(p\), both \(\{dx_1\}\cup\{de_i\}\) and \(\{dx_1'\}\cup\{de_i\}\) are linearly independent in \(\Omega_X\otimes K\). Complete both to bases by the same further covectors, chosen among \(k\)-linear combinations of a fixed coordinate system centred at \(p\); a general choice works because \(k\) is infinite. This gives two coordinate systems centred at \(p\),

\[
(x_1,x_2,\ldots,x_n)\quad\text{and}\quad(x_1',x_2,\ldots,x_n),\qquad\text{with }E^i=V(x_{c(i)}),\ i\in A .
\]

In \(R=\widehat{\mathcal O}_{X,p}=K'[[x_1',x_2,\ldots,x_n]]\) let \(\varphi^*\) be the automorphism of the form \(\mathbf 1+MC(\widehat{\mathcal I})\) given by \(x_1'\mapsto x_1'+(x_1-x_1')=x_1\) and \(x_l\mapsto x_l\) for \(l\ge2\); here \(x_1-x_1'\in MC(\mathcal I)\), and \(\varphi^*\) is an automorphism since \((x_1,x_2,\ldots,x_n)\) is a coordinate system. By Proposition 2.1, \(\varphi^*\widehat{\mathcal I}=\widehat{\mathcal I}\). Also \(\varphi^*(x_1')=x_1\), \(\varphi^*(x_{c(i)})=x_{c(i)}\), and \(h-\varphi^*h\in(x_1-x_1')\subset MC(\widehat{\mathcal I})\) for every \(h\in R\), by Taylor's formula.

*Étale step.* Let \(\Delta(p)\) be the image of \(p\) under the diagonal, a closed point of \(X\times_kX\) with residue field \(K\). Near \(\Delta(p)\) let

\[
U_1=V\bigl(\mathrm{pr}_1^*x_1-\mathrm{pr}_2^*x_1',\ \mathrm{pr}_1^*x_l-\mathrm{pr}_2^*x_l\ (2\le l\le n)\bigr)\subset X\times_kX,
\]

with \(\psi=\mathrm{pr}_1|_{U_1}\) and \(\psi'=\mathrm{pr}_2|_{U_1}\). It contains \(\Delta(p)\). To see that \(\psi\) is étale near \(\Delta(p)\), let \(x=(x_1,\ldots,x_n)\) and \(x'=(x_1',x_2,\ldots,x_n)\), both étale maps to \(\mathbf A^n\) near \(p\). Then \(U_1=(X\times X)\times_{X\times\mathbf A^n}\Gamma\), where \(X\times X\to X\times\mathbf A^n\) is \(\mathrm{id}\times x'\), which is étale near \(\Delta(p)\), and \(\Gamma\subset X\times\mathbf A^n\) is the graph of \(x\), which \(\mathrm{pr}_1\) maps isomorphically onto \(X\). So \(\psi\) is a base change of an étale morphism, hence étale near \(\Delta(p)\); the same argument with \(x\times\mathrm{id}\) and the graph of \(x'\) applies to \(\psi'\). Both induce the identity on the residue field \(K\) of \(\Delta(p)\), so the completed maps \(\widehat\psi^*,\widehat\psi'^*:R\to\widehat{\mathcal O}_{U_1,\Delta(p)}\) are isomorphisms that fix \(K'\); the composite \((\widehat\psi^*)^{-1}\widehat\psi'^*\) sends \(x_1'\mapsto x_1\) and \(x_l\mapsto x_l\), so it is \(\varphi^*\). On \(U_1\) itself, \(\psi^*x_1=\psi'^*x_1'\) and \(\psi^*x_{c(i)}=\psi'^*x_{c(i)}\), which give (1) and (3) near \(\Delta(p)\). Conditions (2) and (4) are inclusions of coherent ideals that hold after completion at \(\Delta(p)\): for (2), \(\widehat\psi'^*\widehat{\mathcal I}=\widehat\psi^*\varphi^*\widehat{\mathcal I}=\widehat\psi^*\widehat{\mathcal I}\); for (4), near \(\Delta(p)\) the diagonal ideal is generated by functions \(h\otimes1-1\otimes h\), whose pull-backs are \(\widehat\psi^*(h-\varphi^*h)\in\widehat\psi^*MC(\widehat{\mathcal I})=MC(\widehat{\psi^*\mathcal I})\). By Lemma 1.1 they hold on an open neighbourhood \(U(p)\) of \(\Delta(p)\) in \(U_1\), which we also choose so small that \(\psi,\psi'\) are étale on it.

*Covering.* The open sets \(\psi(U(p))\cap\psi'(U(p))\) contain \(p\), and finitely many of them cover the quasi-compact set \(\operatorname{cosupp}(\mathcal I,m)\). The disjoint union \(U\) of the corresponding \(U(p)\), with the induced \(\psi,\psi'\), satisfies (1)–(4), and both images contain the cosupport. \(\square\)

## 4. Étale equivalent blow-up sequences are equal

**Theorem 4.1.** Let \(\mathcal I\) have \(m=\operatorname{maxord}\mathcal I\). Let \(\mathbf B\) and \(\mathbf B'\) be blow-up sequences of order \(m\) for \((X,\mathcal I)\), and let \(\psi,\psi':U\to X\) be étale morphisms whose images contain \(\operatorname{cosupp}(\mathcal I,m)\), satisfying conditions (2) and (4) of Definition 3.2, and such that \(\psi^*\mathbf B=\psi'^*\mathbf B'\). Then \(\mathbf B=\mathbf B'\).

**Proof.** Every centre of an order-\(m\) sequence lies over \(\operatorname{cosupp}(\mathcal I,m)\): over the complement of the centre \(Z_i\) the transform does not change, and the new exceptional divisor lies over \(Z_i\). So no pulled-back centre is empty, and \(\psi^*\mathbf B=\psi'^*\mathbf B'\) is a single sequence \((U_i,\mathcal I^U_i)\) with centres \(Z^U_i\), where \(\mathcal I^U_0=\psi^*\mathcal I=\psi'^*\mathcal I\). Let \(\mathcal T_i\) be the transform of the marked ideal \((MC(\mathcal I^U_0),1)\) along it; by [Derivative ideals under blowing up, Theorem 3.1](derivative-ideals-under-blowing-up.md#3-the-basic-inclusion) with \(j=m-1\) the transforms are defined and \(Z^U_i\subset V(\mathcal T_i)\). We prove by induction on \(i\):

(a) the first \(i\) centres of \(\mathbf B\) and \(\mathbf B'\) agree, so \(X_i=X'_i\) and \(\mathcal I_i=\mathcal I'_i\);

(b) the two base changes \(\psi_i,\psi'_i:U_i\to X_i\) of \(\psi,\psi'\) satisfy \((\psi_i,\psi'_i)^{-1}\mathcal I_{\Delta_i}\cdot\mathcal O_{U_i}\subset\mathcal T_i\), where \(\Delta_i\) is the diagonal of \(X_i\); that is, \(\psi_i\) and \(\psi'_i\) agree on \(V(\mathcal T_i)\).

For \(i=0\), (b) is condition (4). Assume (a) and (b) for \(i\). Then \(\psi_i^{-1}(Z_i)=Z^U_i=\psi'^{-1}_i(Z'_i)\). The centres lie over the cosupport, which lies in the images, so \(Z_i=\psi_i(Z^U_i)\) and \(Z'_i=\psi'_i(Z^U_i)\) as sets. Since \(Z^U_i\subset V(\mathcal T_i)\), where \(\psi_i=\psi'_i\), the two images agree; centres are reduced, so \(Z_i=Z'_i\), which gives (a) for \(i+1\).

For (b) at \(i+1\), let \(u\in U_{i+1}\). Over the complement of \(Z^U_i\) the statement is (b) for \(i\), because \(\psi_{i+1}(u)\) lies over \(Z_i\) exactly when \(u\) lies over \(\psi_i^{-1}(Z_i)=Z^U_i\), and the same holds for \(\psi'\). Where \(\mathcal T_{i+1}=\mathcal O\) there is nothing to prove. So let \(u\) lie over \(Z^U_i\) with \(u\in V(\mathcal T_{i+1})\), and let \(z\) be the common image of \(u\) in \(X_i\). Choose coordinates \(x_1,\ldots,x_n\) near \(z\) with \(Z_i=V(x_1,\ldots,x_c)\). Near \((z,z)\) the diagonal of \(X_i\) is cut out by the \(x_l\otimes1-1\otimes x_l\), because \(x:X_i\to\mathbf A^n\) is étale near \(z\), so the diagonal is open and closed in \(X_i\times_{\mathbf A^n}X_i\). By (b), \(b_l=\psi_i^*x_l-\psi'^*_ix_l\in\mathcal T_i\) near the image of \(u\). On the blow-up, \(\pi^*\mathcal T_i=\mathcal O(-F^U)\mathcal T_{i+1}\), so \(\pi^*b_l=g\,b'_l\) with \(g\) a local equation of the exceptional divisor \(F^U\) and \(b'_l\in\mathcal T_{i+1}\), vanishing at \(u\). Choose \(k_0\le c\) with \(g=\pi^*\psi_i^*x_{k_0}\) near \(u\). Then \(\pi^*\psi'^*_ix_{k_0}=g(1-b'_{k_0})\), with \(1-b'_{k_0}\) a unit at \(u\). So \(\psi_{i+1}(u)\) and \(\psi'_{i+1}(u)\) lie in the same chart of [Smooth blow-ups and transforms of ideals, Proposition 3.1](smooth-blowups-and-transforms-of-ideals.md#3-blowing-up-a-smooth-centre), with coordinates \(y_l=x_l/x_{k_0}\) for \(l\le c\), \(l\ne k_0\), and \(y_l=x_l\) otherwise. For \(l\le c\), \(l\ne k_0\),

\[
\psi'^*_{i+1}y_l=\frac{g\,\psi_{i+1}^*y_l-g\,b'_l}{g(1-b'_{k_0})},\qquad
\psi_{i+1}^*y_l-\psi'^*_{i+1}y_l=\frac{b'_l-b'_{k_0}\,\psi_{i+1}^*y_l}{1-b'_{k_0}}\in\mathcal T_{i+1},
\]

and for the other \(l\), \(\psi_{i+1}^*y_l-\psi'^*_{i+1}y_l=\pi^*b_l=g\,b'_l\in\mathcal T_{i+1}\). At \(u\) all these differences vanish, so \(\psi_{i+1}(u)\) and \(\psi'_{i+1}(u)\) are the same point: both lie over the same point of \(Z_i\) and have the same fibre coordinates in \(F\cap(\text{chart})\cong(Z_i\cap\text{chart})\times\mathbf A^{c-1}\). Near that point the diagonal of \(X_{i+1}\) is generated by the \(y_l\otimes1-1\otimes y_l\), as before, and their pull-backs lie in \(\mathcal T_{i+1}\). This proves (b) for \(i+1\). \(\square\)

**Corollary 4.2.** Let \(\mathcal I\) be MC-invariant, \(E\) snc, and \(H,H'\) as in Theorem 3.3. Let \(\mathcal C\) be a blow-up sequence functor, defined on triples \((X,\mathcal I,(H,E))\) of this kind and producing sequences of order \(m\) for \((X,\mathcal I,E)\), that commutes with étale morphisms. Then \(\mathcal C(X,\mathcal I,(H,E))=\mathcal C(X,\mathcal I,(H',E))\).

**Proof.** Take \(\psi,\psi'\) from Theorem 3.3. Functoriality gives \(\psi^*\mathcal C(X,\mathcal I,(H,E))=\mathcal C(U,\psi^*\mathcal I,\psi^{-1}(H,E))\) and \(\psi'^*\mathcal C(X,\mathcal I,(H',E))=\mathcal C(U,\psi'^*\mathcal I,\psi'^{-1}(H',E))\), with no empty blow-ups deleted since all centres lie over the cosupport (proof of Theorem 4.1). The two triples on \(U\) are equal by conditions (1)–(3). Theorem 4.1 gives the equality. \(\square\)

## 5. Exercises

**Exercise 5.1.** Show that \(\mathcal I=(x,y)^m\) on \(\mathbf A^2\) is MC-invariant, and that \(\mathcal I=(x^2+y^3)\) is not.

*Solution.* For \((x,y)^m\): \(MC(\mathcal I)=(x,y)\) and \(D(\mathcal I)=(x,y)^{m-1}\), so \(MC(\mathcal I)D(\mathcal I)=(x,y)^m=\mathcal I\). For \(x^2+y^3\): \(m=2\), \(MC(\mathcal I)=D(\mathcal I)=(x,y^2)\), and \(MC(\mathcal I)D(\mathcal I)\ni x^2\notin(x^2+y^3)\).

**Exercise 5.2.** For \(\mathcal I=(x^2+y^3)\), the MC-hypersurfaces \(H=V(x)\) and \(H'=V(x+y^2)\) give the restrictions \((y^3)\) and \(((y^2)^2+y^3)=(y^3(1+y))\). Show that the formal automorphism \(x\mapsto x+y^2\), \(y\mapsto y\) does not preserve \(\mathcal I\), in accordance with Exercise 5.1.

*Solution.* It sends \(x^2+y^3\) to \(x^2+2xy^2+y^4+y^3\). Suppose this equals \(g\cdot(x^2+y^3)\) in \(k[[x,y]]\), and let \(g_0,g_1\) be the parts of \(g\) of degree \(0\) and \(1\). Comparing degree \(2\) gives \(g_0=1\). Comparing degree \(3\) gives \(2xy^2+y^3=g_1x^2+y^3\), that is, \(2xy^2=g_1x^2\), which is impossible because \(x^2\) does not divide \(xy^2\).

**Exercise 5.3.** Check the formula of Proposition 2.1, (3)⇒(1), for \(\mathcal I=(x^2)\), \(B=(x)\) and \(\sigma(x)=x+x^2\).

*Solution.* \(D(\mathcal I)=(x)\) and \(B\cdot D(\mathcal I)=(x^2)\subset\mathcal I\). Indeed \(\sigma(x^2)=x^2(1+x)^2\in\mathcal I\).

## References

- [Kollár] J. Kollár, *Resolution of singularities — Seattle lecture*, arXiv:math/0508332, section "Uniqueness of maximal contact". <https://arxiv.org/abs/math/0508332>
- [Włodarczyk] J. Włodarczyk, *Simple Hironaka resolution in characteristic zero*, arXiv:math/0401401, the homogenization and Glueing Lemma, where the formal-automorphism idea originates. <https://arxiv.org/abs/math/0401401>
