# Recognizing cocartesian squares

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A square in a derivator is cocartesian when its corner is the homotopy pushout of the other three vertices. In a diagram produced by a homotopy Kan extension, many squares are cocartesian for formal reasons, and suspensions, cofibre sequences and octahedra are built by recognizing them. This lesson proves one recognition lemma and draws three consequences from it: a detection criterion for squares inside Kan extensions, the composition and cancellation of cocartesian squares, and the fact that a square of diagrams is cocartesian exactly when each of its values is. The last consequence transports results about the underlying category \(\mathbb D(e)\) to every category \(\mathbb D(J)\), through the shifted derivators \(\mathbb D^M\). The final section builds, for every arrow, a diagram containing its cofibre and the suspension of its source.

**Prerequisites.** The lessons [*Kan extensions and the derivator axioms*](kan-extensions-and-the-derivator-axioms.md) (base change morphisms, Section 3; the axioms, Definition 4.1; duality, Remark 4.3; Propositions 5.1 and 6.1), [*Homotopy exact squares*](homotopy-exact-squares.md) (Lemmas 1.1, 2.2 and 3.1, Proposition 2.3, Corollary 2.4, Proposition 3.3) and [*Pointed and stable derivators*](pointed-and-stable-derivators.md) (Propositions 1.2 and 1.3, Definition 2.1, Lemma 2.2, Section 3). Strong derivators are those of Theorem 4.1 of [*The derivator of a ring*](the-derivator-of-a-ring.md).

Throughout, \(\mathbb D\) is a derivator. For a square of small categories

\[
\begin{array}{ccc}
J&\xrightarrow{v}&J'\\
{\scriptstyle u}\downarrow&&\downarrow{\scriptstyle u'}\\
K&\xrightarrow{w}&K'
\end{array}
\qquad\alpha:u'v\to wu,
\]

the base change morphism is \(\alpha_!:u_!v^*\to w^*u'_!\), as in Section 3 of the lesson on Kan extensions. Horizontal pasting (Lemma 1.1 of the lesson on homotopy exact squares) is used in the form: if \(\alpha\) is pasted from a left square \(\alpha_1\) and a right square \(\alpha_2\), then

\[
\alpha_!=w_1^*\alpha_{2!}\cdot\alpha_{1!}v_2^*,
\]

where \(w_1\) is the bottom edge of the left square and \(v_2\) the top edge of the right square. For an identity functor we use the identity adjunction.

## 1. The comparison map of a square

Let \(\square=[1]\times[1]\), with \(\ulcorner\subset\square\) the full subcategory without \((1,1)\), inclusion \(i_\ulcorner\), and \(p:{\ulcorner}\to e\). For \(a\) in \(\ulcorner\) let \(\beta_a:a\to(1,1)\) be the unique morphism of \(\square\); these form a natural transformation \(\beta:i_\ulcorner\to(1,1)\circ p\). Its square

\[
\begin{array}{ccc}
\ulcorner&\xrightarrow{i_\ulcorner}&\square\\
{\scriptstyle p}\downarrow&&\downarrow{\scriptstyle 1}\\
e&\xrightarrow{(1,1)}&\square
\end{array}
\]

has as base change morphism a natural map

\[
\begin{gathered}
\chi_X=\beta_!:\operatorname{hocolim}_\ulcorner i_\ulcorner^*X\longrightarrow X_{11},\\
X\in\mathbb D(\square),
\end{gathered}
\]

the *comparison map* of the square \(X\). In a represented derivator it is the canonical map from the pushout of \(X_{10}\leftarrow X_{00}\to X_{01}\) to \(X_{11}\) (Exercise 5.1).

**Lemma 1.1.** A square \(X\) is cocartesian if and only if \(\chi_X\) is invertible.

**Proof.** Every object of \(\ulcorner\) has exactly one morphism to \((1,1)\), so the projection \(\mathrm{pr}:{\ulcorner}_{/(1,1)}\to\ulcorner\) from the comma category of \(i_\ulcorner\) over \((1,1)\) is an isomorphism of categories, and the transformation \(\alpha^{/(1,1)}\) of that comma category is \(\beta\,\mathrm{pr}\). Consider the square with top \(i_\ulcorner\mathrm{pr}\), left \(p\), right \(1_\square\), bottom \((1,1)\), and transformation \(\alpha^{/(1,1)}\). It arises by pasting in two ways.

First, it is the comma square of \(i_\ulcorner\) at \((1,1)\), pasted on the right with the square with top and left \(i_\ulcorner\), right and bottom \(1_\square\), and identity transformation. The base change morphism of the latter is the counit \(\varepsilon\) of \(i_{\ulcorner!}\dashv i_\ulcorner^*\). Second, it is the square with top \(\mathrm{pr}\), sides \(p\), bottom \(1_e\) and identity transformation, pasted on the right with the square defining \(\chi\). Horizontal pasting gives

\[
(1,1)^*\varepsilon\cdot(\alpha^{/(1,1)})_!\,i_\ulcorner^*
=\chi\cdot\pi_!\,i_\ulcorner^*,
\]

where \(\pi_!\) is the base change morphism of the square with top \(\mathrm{pr}\). It is invertible by Proposition 2.3 of the lesson on homotopy exact squares, since the isomorphism \(\mathrm{pr}\) is a right adjoint; \((\alpha^{/(1,1)})_!\) is invertible by (Der4). Hence \(\chi_X\) is invertible exactly when \(\varepsilon_X\) is invertible at \((1,1)\). By Lemma 3.1 of the lesson on homotopy exact squares, applied to the fully faithful functor \(i_\ulcorner\), whose image misses only \((1,1)\), this is the condition for \(X\) to lie in the essential image of \(i_{\ulcorner!}\). \(\square\)

## 2. The recognition lemma

Fix a functor \(j:K'\to K\), an object \(x\) of \(K\), a functor \(i:{\square}\to K\) with \(i(1,1)=x\), and a functor \(i':{\ulcorner}\to K'\) with \(j\,i'=i\,i_\ulcorner\). Let \(K'_{/x}\) be the comma category of \(j\) over \(x\), with objects \((k',f:j(k')\to x)\), and define

\[
r:{\ulcorner}\to K'_{/x},
\qquad
r(a)=\bigl(i'(a),\,i(\beta_a)\bigr).
\]

For a morphism \(g:a\to a'\) of \(\ulcorner\), \(i(\beta_{a'})\,j\,i'(g)=i(\beta_{a'}g)=i(\beta_a)\), so \(i'(g)\) is a morphism \(r(a)\to r(a')\) and \(r\) is a functor.

**Lemma 2.1 (recognition).** Suppose \(r\) has a left adjoint. Then for every \(X\) in \(\mathbb D(K)\) there is an isomorphism

\[
\gamma_X:\operatorname{hocolim}_\ulcorner i'^*j^*X\longrightarrow x^*j_!j^*X,
\]

natural in \(X\), with

\[
\chi_{i^*X}=x^*(\varepsilon_X)\circ\gamma_X,
\]

where \(\varepsilon\) is the counit of \(j_!\dashv j^*\). In particular \(i^*X\) is cocartesian if and only if \(\varepsilon_X\) is invertible at \(x\).

**Proof.** Since \(i_\ulcorner^*i^*=i'^*j^*\), both sides of the claimed equation are maps from \(\operatorname{hocolim}_\ulcorner i'^*j^*X\) to \(X_x\). Let \(A\) be the square with top \(i\,i_\ulcorner\), left \(p\), right \(1_K\), bottom \(x\), and transformation \(i\beta:i\,i_\ulcorner\to x\,p\).

(1) \(A\) is the square of \(\chi\) pasted on the right with the square with top and bottom \(i\), sides \(1_\square\) and \(1_K\), and identity transformation. The latter has identity base change morphism, so horizontal pasting gives \(A_!=\chi\,i^*\).

(2) \(A\) is also the square \(S\) with top \(i'\), left \(p\), right \(j\), bottom \(x\) and transformation \(i\beta:j\,i'\to x\,p\), pasted on the right with the square with top and left \(j\), right and bottom \(1_K\), and identity transformation. The base change morphism of the latter is \(\varepsilon\), so \(A_!=x^*\varepsilon\cdot S_!\,j^*\).

(3) \(S\) is the square with top \(r\), sides \(p\), bottom \(1_e\) and identity transformation, pasted on the right with the comma square of \(j\) at \(x\), whose transformation is \(\alpha^{/x}\). Indeed \(\mathrm{pr}\,r=i'\), and the pasted transformation \(\alpha^{/x}r\) has at \(a\) the structure morphism of \(r(a)\), which is \(i(\beta_a)\). The first square is homotopy exact by Proposition 2.3 of the lesson on homotopy exact squares, since \(r\) is a right adjoint, and the comma square by (Der4). Horizontal pasting shows that \(S_!\) is invertible.

Put \(\gamma_X=S_!(j^*X)\). Comparing (1) and (2) at \(X\) gives the equation. By Lemma 1.1, \(i^*X\) is cocartesian exactly when \(\chi_{i^*X}\) is invertible, that is, when \(x^*\varepsilon_X\) is. \(\square\)

**Corollary 2.2 (detection).** In the situation of Lemma 2.1, let \(j\) be fully faithful and \(X\) in the essential image of \(j_!\). Then \(i^*X\) is cocartesian.

**Proof.** If \(X\cong j_!Y\), the counit at \(X\) is invertible: the triangle identity \(\varepsilon_{j_!Y}\circ j_!\eta_Y=1\) and the invertibility of \(\eta_Y\) (Proposition 6.1 of the lesson on Kan extensions) give it at \(j_!Y\), and naturality transfers it to \(X\). Lemma 2.1 concludes. \(\square\)

Groth attributes this detection criterion to Franke's work on systems of triangulated diagram categories. It is used for posets: there a functor is an order-preserving map, and \(r:P\to Q\) has a left adjoint exactly when there is an order-preserving \(L:Q\to P\) with \(L(q)\le a\Leftrightarrow q\le r(a)\) for all \(q\) and \(a\). The dual statements, obtained by applying Lemma 2.1 and Corollary 2.2 to the dual derivator \(\mathbb D^{\mathrm{op}}\) (Remark 4.3 of the lesson on Kan extensions), read: with \(x=i(0,0)\), \(i':{\lrcorner}\to K'\), and \(r:{\lrcorner}\to K'_{x/}\) a left adjoint, the square \(i^*X\) is cartesian if and only if the unit \(X\to j_*j^*X\) is invertible at \(x\); this holds when \(j\) is fully faithful and \(X\) lies in the essential image of \(j_*\).

Next, the composition of squares. In \([2]\times[1]\) let

\[
s_{01},\;s_{12},\;s_{02}:{\square}\to[2]\times[1],
\]
\[
\begin{gathered}
s_{01}(c,t)=(c,t),\quad s_{12}(c,t)=(c+1,t),\\
s_{02}(c,t)=(2c,t),
\end{gathered}
\]

be the left square, the right square and the composite square.

**Proposition 2.3 (composition and cancellation).** Let \(X\) be in \(\mathbb D([2]\times[1])\).

1. If \(s_{01}^*X\) is cocartesian, then \(s_{12}^*X\) is cocartesian if and only if \(s_{02}^*X\) is.
2. If \(s_{12}^*X\) is cartesian, then \(s_{01}^*X\) is cartesian if and only if \(s_{02}^*X\) is.

**Proof.** (1) Let \(J_0\subset J_1\subset J_2=[2]\times[1]\) be the full subcategories on \(\{(0,0),(1,0),(2,0),(0,1)\}\) and on these together with \((1,1)\), with inclusions \(e_0:J_0\to J_1\), \(e_1:J_1\to J_2\) and \(e=e_1e_0\). Take \(e_!=e_{1!}e_{0!}\) with the composite adjunction; its counit is

\[
\varepsilon^e=\varepsilon^{e_1}\cdot e_{1!}\,\varepsilon^{e_0}e_1^*.
\]

Apply Lemma 2.1 three times; in each case the categories are posets.

- Left square: \(K=J_1\), \(j=e_0\), \(x=(1,1)\), \(i=s_{01}\). The objects of \(J_0\) below \((1,1)\) are \((0,0)\), \((1,0)\), \((0,1)\), so \(r\) is an isomorphism onto \((J_0)_{/(1,1)}\). Hence \(s_{01}^*X\) is cocartesian if and only if the counit of \(e_0\) at \(e_1^*X\) is invertible at \((1,1)\), that is, invertible (by the proof of Lemma 3.1 of the lesson on homotopy exact squares it is invertible at the objects of \(J_0\)).
- Right square: \(K=J_2\), \(j=e_1\), \(x=(2,1)\), \(i=s_{12}\). Every object of \(J_1\) lies below \((2,1)\), and \(r\) is the inclusion of \(\{(1,0),(2,0),(1,1)\}\) into \(J_1\). It has the left adjoint sending \((0,0)\) and \((1,0)\) to \((0,0)\), \((2,0)\) to \((1,0)\), and \((0,1)\) and \((1,1)\) to \((0,1)\); the condition \(L(y)\le a\Leftrightarrow y\le r(a)\) is checked object by object. Hence \(s_{12}^*X\) is cocartesian if and only if \(\varepsilon^{e_1}_X\) is invertible at \((2,1)\).
- Composite square: \(K=J_2\), \(j=e\), \(x=(2,1)\), \(i=s_{02}\). Here \(r\) is the inclusion of \(\{(0,0),(2,0),(0,1)\}\) into \(J_0\), with left adjoint fixing \((0,0)\) and \((0,1)\) and sending \((1,0)\) and \((2,0)\) to \((1,0)\). Hence \(s_{02}^*X\) is cocartesian if and only if \(\varepsilon^e_X\) is invertible at \((2,1)\).

If \(s_{01}^*X\) is cocartesian, the map \(e_{1!}\varepsilon^{e_0}_{e_1^*X}\) is invertible, and by the formula for \(\varepsilon^e\), the counit \(\varepsilon^e_X\) is invertible at \((2,1)\) exactly when \(\varepsilon^{e_1}_X\) is. By Lemma 3.1 of the lesson on Kan extensions, invertibility of a counit does not depend on the chosen adjoints.

(2) Apply (1) to the dual derivator. Passing to opposite categories reverses \([2]\times[1]\) by \((c,t)\mapsto(2-c,1-t)\); this exchanges the left and the right squares, fixes the composite square, and turns cocartesian squares of \(\mathbb D^{\mathrm{op}}\) into cartesian squares of \(\mathbb D\). \(\square\)

## 3. Shifted derivators

For a small category \(M\), the shifted prederivator \(\mathbb D^M\) has \(\mathbb D^M(J)=\mathbb D(M\times J)\), with restrictions and transformations along \(1_M\times u\) and \(1_M\times\alpha\) (Example 4.5 of the first lesson). For an object \(m\) of \(M\) and \(X\) in \(\mathbb D(M\times J)\) write \(X_m=(m\times1_J)^*X\) in \(\mathbb D(J)\).

**Proposition 3.1.** \(\mathbb D^M\) is a derivator. Its left and right Kan extensions along \(u:J\to K\) are those of \(\mathbb D\) along \(1_M\times u\). If \(\mathbb D\) is pointed, so is \(\mathbb D^M\).

**Proof.** (Der1): \(M\times(J_1\sqcup J_2)=(M\times J_1)\sqcup(M\times J_2)\) and \(M\times\emptyset=\emptyset\). (Der2): the object \((m,j)\) of \(M\times J\) is the composite of \(m:e\to M\) and \(1_M\times j:M\to M\times J\); if every \((1_M\times j)^*f\) is invertible in \(\mathbb D(M)\), then so is every \((m,j)^*f\), and (Der2) for \(\mathbb D\) applies. (Der3) holds by definition.

(Der4): let \(u:J\to K\) and \(k\) in \(K\). In \(\mathbb D\), the comma square of \(u\) at \(k\) for \(\mathbb D^M\) is the square \(Q\) with top \(1_M\times\mathrm{pr}\), left \(1_M\times p\), right \(1_M\times u\), bottom \(1_M\times k\), and transformation \(1_M\times\alpha^{/k}\). Its base change morphism is a morphism of \(\mathbb D(M)\), so by (Der2) it suffices to show that \(m^*Q_!\) is invertible for every \(m\) in \(M\). The comma category of \(1_M\times p:M\times J_{/k}\to M\) over \(m\) is \(M_{/m}\times J_{/k}\). Pasting its comma square (on the left) with \(Q\) (on the right) gives the square with top the projection \(M_{/m}\times J_{/k}\to M\times J\), left \(p\), right \(1_M\times u\), bottom \((m,k)\), whose transformation has components \((f,g):(m',u(j))\to(m,k)\) at \(((m',f),(j,g))\). This is the comma square of \(1_M\times u\) at \((m,k)\), because

\[
(M\times J)_{/(m,k)}=M_{/m}\times J_{/k}.
\]

By (Der4) for \(\mathbb D\), both the pasted square and the left square are homotopy exact, and horizontal pasting shows that \(m^*Q_!\) is invertible. Right Kan extensions are dual. If \(\mathbb D(e)\) has a zero object, so has \(\mathbb D^M(e)=\mathbb D(M)\) (Proposition 1.2 of the lesson on pointed derivators). \(\square\)

**Corollary 3.2 (objectwise criterion).** An object \(X\) of \(\mathbb D^M(\square)=\mathbb D(M\times\square)\) is a cocartesian square of \(\mathbb D^M\) if and only if \(X_m\) is a cocartesian square of \(\mathbb D\) for every \(m\) in \(M\). The same holds for cartesian squares.

**Proof.** By Proposition 3.1, \(X\) is cocartesian in \(\mathbb D^M\) when it lies in the essential image of the left Kan extension along \(1_M\times i_\ulcorner\). By Lemma 3.1 of the lesson on homotopy exact squares this means that the counit \(\varepsilon_X\) of that extension is invertible at every object \((m,(1,1))\). Apply Lemma 2.1 with \(K=M\times\square\), \(K'=M\times\ulcorner\), \(j=1_M\times i_\ulcorner\), \(x=(m,(1,1))\), \(i=m\times1_\square\) and \(i'=m\times1_\ulcorner\). The comma category \(K'_{/x}\) is \(M_{/m}\times\ulcorner\), and \(r\) sends \(a\) to \(((m,1_m),a)\). Since \((m,1_m)\) is terminal in \(M_{/m}\), the projection \(M_{/m}\times\ulcorner\to\ulcorner\) is left adjoint to \(r\). So \(X_m=i^*X\) is cocartesian exactly when \(\varepsilon_X\) is invertible at \((m,(1,1))\). Cartesian squares are dual. \(\square\)

**Corollary 3.3.** If \(\mathbb D\) is stable, so is \(\mathbb D^M\). If \(\mathbb D\) is strong, so is \(\mathbb D^M\).

**Proof.** \(\mathbb D^M\) is pointed by Proposition 3.1, and by Corollary 3.2 a square of \(\mathbb D^M\) is cocartesian if and only if all its values are, if and only if they are all cartesian, if and only if it is cartesian. For strongness, the partial underlying diagram functor \(\mathbb D^M([1]\times J)\to\mathbb D^M(J)^{[1]}\) is the functor \(\operatorname{dia}_{[1],M\times J}\) of \(\mathbb D\), composed with restriction along the isomorphism \([1]\times M\times J\cong M\times[1]\times J\). \(\square\)

Corollary 3.3 is the device for passing from \(\mathbb D(e)\) to \(\mathbb D(J)\): a statement proved about the underlying category of every stable, or strong, derivator applies to \(\mathbb D^J(e)=\mathbb D(J)\).

## 4. The cofibre sequence of an arrow

Let \(\mathbb D\) be pointed. In \([2]\times[1]\) let \(K\) be the full subcategory on \(\{(0,0),(1,0),(2,0),(0,1)\}\), let \(k_0:[1]\to K\) send \(0\to1\) to \((0,0)\to(1,0)\), and let \(k_1:K\to[2]\times[1]\) be the inclusion. No object of \(K\) outside the image of \(k_0\) has a morphism into it, so \(k_0\) is a sieve. For \(f\) in \(\mathbb D([1])\) put

\[
Y=k_{1!}\,k_{0*}f\in\mathbb D([2]\times[1]).
\]

**Proposition 4.1.** The squares \(s_{01}^*Y\), \(s_{12}^*Y\) and \(s_{02}^*Y\) are cocartesian, \(Y_{20}\) and \(Y_{01}\) are zero objects, and the restriction of \(Y\) to the arrow \((0,0)\to(1,0)\) is isomorphic to \(f\). Consequently there are isomorphisms, natural in \(f\),

\[
Y_{11}\cong\operatorname{cof}(f),
\qquad
Y_{21}\cong\Sigma f_0,
\]

and along the path \((0,0)\to(1,0)\to(1,1)\to(2,1)\) the underlying diagram of \(Y\) is a sequence

\[
f_0\to f_1\to\operatorname{cof}(f)\to\Sigma f_0 .
\]

**Proof.** Since \(k_1\) is fully faithful, \(k_1^*Y\cong k_{0*}f\) (Proposition 6.1 of the lesson on Kan extensions). Extension by zero along the sieve \(k_0\) (Proposition 1.3 of the lesson on pointed derivators) gives \(Y_{20}\cong0\cong Y_{01}\), and \(k_0^*k_{0*}f\cong f\).

The left square: Corollary 2.2 with \(j=k_1\), \(x=(1,1)\), \(i=s_{01}\). The objects of \(K\) below \((1,1)\) are \((0,0)\), \((1,0)\), \((0,1)\), so \(r\) is an isomorphism.

The right square: \(Y\) also lies in the essential image of the left Kan extension along the inclusion \(e_1:J_1\to[2]\times[1]\) of Section 2, since \(k_1=e_1e_0\) and \(k_{1!}\cong e_{1!}e_{0!}\). Corollary 2.2 with \(j=e_1\), \(x=(2,1)\), \(i=s_{12}\) applies, with the left adjoint of \(r\) found in the proof of Proposition 2.3.

The composite square: Proposition 2.3(1).

For the identifications, let \(W\) be a cocartesian square. Then \(W\cong i_{\ulcorner!}i_\ulcorner^*W\), and if \(W_{01}\cong0\), the object \(i_\ulcorner^*W\) of \(\mathbb D(\ulcorner)\) vanishes at \((0,1)\) and is the extension by zero of its restriction to \((0,0)\to(1,0)\) along this sieve. For \(W=s_{01}^*Y\) that restriction is \(f\), so \(W\) is the cofibre square of \(f\) (Section 3 of the lesson on pointed derivators) and \(Y_{11}\cong\operatorname{cof}(f)\). If moreover \(W_{10}\cong0\), the object \(i_\ulcorner^*W\) is the extension by zero of \(W_{00}\) along the sieve \((0,0)\), and \(W_{11}\cong\Sigma W_{00}\) by Definition 3.1 there. For \(W=s_{02}^*Y\) this gives \(Y_{21}\cong\Sigma Y_{00}\cong\Sigma f_0\). Each isomorphism is a composite of units and counits of the adjunctions involved, hence natural. \(\square\)

The last term \(\Sigma f_0\) is also the cofibre of the map \(f_1\to\operatorname{cof}(f)\): the right square is cocartesian with \(Y_{20}\cong0\), and its transpose (Exercise 5.2) is the cofibre square of that map. The distinguished triangles of a stable derivator are built from this diagram.

## 5. Exercises

**5.1** (easy). Let \(\mathcal C\) be a complete and cocomplete category and \(\mathbb D=y(\mathcal C)\). Show that \(\chi_X\) is the canonical map from the pushout of \(X_{10}\leftarrow X_{00}\to X_{01}\) to \(X_{11}\), and deduce that a square is cocartesian exactly when it is a pushout square.

**5.2** (easy). Let \(\sigma:{\square}\to\square\) be the transposition \((a,b)\mapsto(b,a)\). Use Lemma 2.1 to show that \(\sigma^*X\) is cocartesian if and only if \(X\) is.

**5.3** (medium). Show that in every derivator the coproduct, in \(\mathbb D(\square)\), of two cocartesian squares is cocartesian. Deduce that in a stable derivator the coproduct of two cartesian squares is cartesian.

**5.4** (medium). In a pointed derivator, let \(Y\) be as in Section 4. Show that the composite square \(s_{02}^*Y\) is also obtained from \(f_0\) by the construction defining \(\Sigma\), by restricting \(Y\) along \(s_{02}\) and comparing with \(i_{\ulcorner!}(0,0)_*f_0\) directly, without Proposition 2.3.

**5.5** (hard). Show that a square \(X\) whose two vertical arrows \(X_{00}\to X_{01}\) and \(X_{10}\to X_{11}\) are isomorphisms is cocartesian. (Write \(X\) as \(\pi^*Z\) for the projection \(\pi:{\square}\to[1]\), \((a,b)\mapsto a\).)

## 6. Solutions

**5.1.** With the identity adjunction for \(1_\square\), the base change morphism is \(\varepsilon\cdot p_!\beta^*\), where \(\varepsilon\) is the counit of \(\operatorname{colim}_\ulcorner\dashv p^*\) at \(X_{11}\) and \(\beta^*:i_\ulcorner^*X\to p^*X_{11}\) has components \(X(\beta_a)\). On the colimit injection at \(a\) the composite is \(X(\beta_a)\), so \(\chi_X\) is the map induced by the cocone of the three maps into \(X_{11}\). By Lemma 1.1, \(X\) is cocartesian exactly when this map is invertible, that is, when the square is a pushout.

**5.2.** Apply Lemma 2.1 with \(K=\square\), \(K'=\ulcorner\), \(j=i_\ulcorner\), \(x=(1,1)\), \(i=\sigma\) and \(i'\) the transposition of \(\ulcorner\). Then \(r\) is an isomorphism \(\ulcorner\to\ulcorner_{/(1,1)}\), so \(\sigma^*X\) is cocartesian exactly when the counit of \(i_{\ulcorner!}\dashv i_\ulcorner^*\) is invertible at \((1,1)\). By Lemma 2.2 of the lesson on pointed derivators this is the condition for \(X\) to be cocartesian.

**5.3.** The functors \(\operatorname{hocolim}_\ulcorner i_\ulcorner^*\) and \((1,1)^*\) preserve coproducts, being left adjoints. For a natural transformation \(\theta:F\to G\) between coproduct-preserving functors, naturality with respect to the two coproduct injections shows that \(\theta_{A\sqcup B}\) is \(\theta_A\sqcup\theta_B\) under the canonical isomorphisms. So \(\chi_{A\sqcup B}\) is invertible when \(\chi_A\) and \(\chi_B\) are, and Lemma 1.1 applies. In a stable derivator cartesian squares are cocartesian, their coproduct is cocartesian, hence cartesian.

**5.4.** The square \(W=s_{02}^*Y\) has \(W_{10}=Y_{20}\cong0\) and \(W_{01}=Y_{01}\cong0\). It is cocartesian by Corollary 2.2 with \(j=k_1\), \(x=(2,1)\), \(i=s_{02}\): every object of \(K\) lies below \((2,1)\), and \(r\) is the inclusion of \(\{(0,0),(2,0),(0,1)\}\) into \(K\), with the left adjoint sending \((1,0)\) and \((2,0)\) to \((1,0)\) and fixing the other two objects. As in the proof of Proposition 4.1, a cocartesian square vanishing at \((1,0)\) and \((0,1)\) is \(i_{\ulcorner!}(0,0)_*\) of its value at \((0,0)\), which is \(f_0\).

**5.5.** Let \(s:[1]\to\square\), \(a\mapsto(a,0)\). The morphisms \((a,0)\to(a,b)\) form a transformation \(\tau:s\pi\to1_\square\), and \(\tau^*:\pi^*s^*X\to X\) has components the identities at \((a,0)\) and the two vertical arrows at \((a,1)\). By (Der2) it is an isomorphism, so \(X\cong\pi^*Z\) with \(Z=s^*X\). For such a square, paste the square of \(\chi\) on the right with the square with top and bottom \(\pi\), sides \(1_\square\) and \(1_{[1]}\), and identity transformation; this gives \(\chi_{\pi^*Z}\) as the base change morphism of the square with top \(\pi i_\ulcorner\), left \(p\), right \(1_{[1]}\), bottom \(1:e\to[1]\), and transformation \(\pi\beta\). The same square is the square with top \(\pi i_\ulcorner\), sides \(p\), bottom \(1_e\) and identity transformation, pasted with the comma square of \(1_{[1]}\) at the object \(1\), since \([1]_{/1}=[1]\). The first is homotopy exact because \(\pi i_\ulcorner\) is a right adjoint, with left adjoint \(0\mapsto(0,0)\), \(1\mapsto(1,0)\); the second by (Der4). Hence \(\chi_{\pi^*Z}\) is invertible and \(\pi^*Z\) is cocartesian.

## Sources

- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840 — Section 3.2: the detection result, which Groth attributes to Franke, and the composition and cancellation of cocartesian squares; Section 1: shifted derivators and the objectwise criterion. The recognition lemma above derives these from a single pasting argument.
- [PS] A. Grothendieck, *Pursuing Stacks*, §69, arXiv:2111.01000. https://arxiv.org/abs/2111.01000 — the demand that systems of objects of \(\mathbb D(J)\) be objects of a value of \(\mathbb D\), which the shifted derivators answer.
