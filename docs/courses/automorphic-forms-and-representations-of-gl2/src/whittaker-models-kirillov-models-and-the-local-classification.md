# Whittaker models, Kirillov models and the local classification

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A nontrivial additive character turns unipotent translation into scalar multiplication. Restricting the resulting Whittaker functions to a one-dimensional torus gives the Kirillov model. Compact functions form a common part of every infinite-dimensional irreducible model; the remaining germs at zero distinguish supercuspidal, special and principal-series representations. We will prove uniqueness, the compact-function inclusion and the local classification. Section 7 proves the unitary and tempered classifications through explicit invariant forms and coefficient estimates.

Use the local field, smooth representations and countable Schur lemma of the smooth local lesson, and normalized induction, exact Jacquet modules, reciprocity and the Steinberg construction from the induction lesson. Write
\[
G=\mathrm{GL}_2(F),\quad \nu(t)=|t|,\quad
d(t)=\operatorname{diag}(t,1),\quad
n(x)=\begin{pmatrix}1&x\\ 0&1\end{pmatrix}.
\]
Fix a nontrivial continuous additive character \(\psi:F\to\mathbb C^\times\). It is unitary. Let \(\varpi^{-\ell}\mathcal O\) be the largest fractional ideal on which it is trivial. We use
\[
w_0=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}.
\tag{0.1}
\]
This is the negative of the Weyl element in Lesson 6. Thus \(w_0^2=-I\), and its operator differs by \(\omega(-1)\) in a representation with central character \(\omega\). Additive measure is self-dual for \(\psi\) when Fourier inversion is used; this gives \(\operatorname{vol}(\mathcal O)=1\) precisely when \(\ell=0\). Normalized compact averages do not depend on this choice.

## 1. A vector-valued model before uniqueness

For a smooth representation \(V\), put
\[
V(N,\psi)=\operatorname{span}\{\pi(n(x))v-\psi(x)v\},\qquad
X=V/V(N,\psi).
\]
A Whittaker functional is a linear functional \(\lambda\) satisfying
\(\lambda(\pi(n(x))v)=\psi(x)\lambda(v)\). Hence
\[
\operatorname{Hom}_N(V,\psi)=X^*.
\tag{1.1}
\]
These are algebraic functionals; they need not belong to the smooth contragredient.

**Lemma 1.1 — weighted averages and exactness.** For a compact additive subgroup \(D\subset F\), define
\[
E_D^\psi v=\frac1{\operatorname{vol}(D)}
 \int_D\psi(-x)\pi(n(x))v\,dx.
\]
A vector has zero class in \(X\) if and only if \(E_D^\psi v=0\) for some sufficiently large \(D\). Twisted coinvariants are exact on smooth representations.

**Proof.** The integral is a finite linear combination because its integrand is locally constant on a compact set. The difference \(v-E_D^\psi v\) is a sum of twisted differences. If \(D\) contains \(x_0\), translation in the integral shows
\(E_D^\psi(\pi(n(x_0))v-\psi(x_0)v)=0\). Any finite sum of differences is therefore killed by an average containing all its translation parameters. This proves the criterion. For a subrepresentation \(W\subset V\), the criterion proves \(W\cap V(N,\psi)=W(N,\psi)\). The quotient assertion follows either by lifting a vector and averaging, or by the right exactness of a vector-space quotient. These two statements give exactness. \(\square\)

Define the function with values in \(X\)
\[
\Phi_v(t)=[\pi(d(t))v],\qquad t\in F^\times.
\]
It is locally constant and obeys
\[
\Phi_{\pi(n(x))v}(t)=\psi(tx)\Phi_v(t),\qquad
\Phi_{\pi(d(a))v}(t)=\Phi_v(ta).
\tag{1.2}
\]
A sufficiently small open subgroup of \(\mathcal O^\times\) fixes each function under dilation. If \(n(I)\) fixes \(v\), where \(I\) is a fractional ideal, its nonzero values require \(tI\subset\varpi^{-\ell}\mathcal O\). Thus every \(\Phi_v\) is supported in \(|t|\le C_v\).

**Lemma 1.2 — the kernel and unipotent invariance.** If \(\Phi_v(t)=0\) for every \(t\ne0\), then \(v\) is \(N\)-invariant. In any smooth \(G\)-representation, an \(N\)-invariant vector is \(\mathrm{SL}_2(F)\)-invariant.

**Proof.** Choose \(I\) with \(n(I)v=v\), and an open unit subgroup \(H\) with \(\pi(d(h))v=v\) for \(h\in H\). Write \(I^\perp=\{a:\psi(aI)=1\}\). To enlarge the stabilizing ideal from \(I\) to \(J=\varpi^{-1}I\), consider the annulus \(I^\perp\setminus J^\perp\). It has finitely many \(H\)-orbits: its valuation is fixed, and \(\mathcal O^\times/H\) is finite.

For each orbit representative \(a\), the zero class of \(\pi(d(a))v\) and Lemma 1.1 give a compact average killing it. Conjugating by \(d(a)\) gives
\[
E_D^{\psi(a\,\cdot)}v=0
\]
for a sufficiently large additive ideal \(D\). Increase \(D\) to work for all representatives and to contain \(J\). Such ideals are stable under unit multiplication. Conjugation by \(d(h)\), using that \(h\) fixes \(v\), makes the same assertion true for the entire annulus.

The \(n(D)\)-orbit of \(v\) factors through the finite abelian group \(D/I\). Its character projections are exactly these weighted averages, with frequencies in \(I^\perp/D^\perp\). All projections whose frequency is outside \(J^\perp\) vanish. Finite Fourier inversion therefore says that \(J/I\) acts trivially. Repeat this enlargement to obtain invariance under every \(n(x)\).

For the second assertion, smoothness supplies a nonzero \(c\) with
\(\pi(\left(\begin{smallmatrix}1&0\\ c&1\end{smallmatrix}\right))v=v\). All upper unipotents fix \(v\), so the product
\[
n(-c^{-1})
\begin{pmatrix}1&0\\ c&1\end{pmatrix}
n(-c^{-1})
=\begin{pmatrix}0&-c^{-1}\\ c&0\end{pmatrix}
\]
fixes it. Conjugating upper unipotents by this matrix supplies every lower unipotent. Upper and lower elementary matrices generate \(\mathrm{SL}_2(F)\), so this group fixes \(v\). \(\square\)

Now assume \(V\) is infinite-dimensional and irreducible. Its \(\mathrm{SL}_2(F)\)-fixed space is a \(G\)-subrepresentation, since \(\mathrm{SL}_2(F)\) is normal. If it were nonzero, \(V\) would factor through determinant; countable Schur would make the irreducible representation one-dimensional. Lemma 1.2 consequently makes \(v\mapsto\Phi_v\) injective. In particular \(X\ne0\).

**Proposition 1.3 — the compact part.** In this injective model,
\[
V_0:=C_c^\infty(F^\times,X)\subset V,\qquad
V(N)=V_0,\qquad V=V_0+\pi(w_0)V_0,
\tag{1.3}
\]
where \(V(N)\) denotes ordinary, untwisted unipotent differences.

**Proof.** Given \(u\in X\), choose \(v\) with \(\Phi_v(1)=u\). Formula (1.2) shows that \(E_D^\psi\) multiplies \(\Phi_v(t)\) by \(1_{1+D^\perp}(t)\). Choose \(D\) so large that this ball avoids zero and \(\Phi_v\) is constantly \(u\) there. We have produced its characteristic function times \(u\). Dilation and further weighted averages, now centered at any chosen frequency, refine this to arbitrary small balls away from zero. A compact locally constant \(X\)-valued function has finite image and can be partitioned into finitely many such balls. Thus it belongs to \(V\).

An ordinary \(N\)-difference is \((\psi(tx)-1)\Phi_v(t)\). It vanishes near zero and outside a bounded ball, hence belongs to \(V_0\). Conversely partition a compact function into balls on each of which some \(\psi(tx)-1\) is a fixed nonzero number. Dividing there expresses it as an \(N\)-difference. This proves \(V(N)=V_0\).

The space \(V_0+\pi(w_0)V_0\) is stable under the center and the torus, since
\(w_0d(a)=aI\,d(a^{-1})w_0\). It is stable under \(N\): applying \(n(x)-1\) to any vector gives an element of \(V_0\). It is stable under \(w_0\), since \(w_0^2=-I\). These matrices generate \(G\). The space is nonzero, so irreducibility makes it all of \(V\). \(\square\)

## 2. The coefficient calculation that makes the fiber one-dimensional

Existence has already been proved: \(X\ne0\). The remaining issue is that several independent values in \(X\) might survive. We now eliminate this possibility without assuming the Whittaker uniqueness theorem.

Let \(U=\mathcal O^\times\), with multiplicative measure \(du\) of total mass one. Put
\(\epsilon=\omega|_U\), \(z=\omega(\varpi)\), and
\(\widetilde\alpha=\alpha^{-1}\epsilon^{-1}\) for a smooth unit character \(\alpha\). For an \(X\)-valued function \(\phi\), write
\[
\phi_n^\alpha=\int_U\phi(\varpi^n u)\alpha(u)\,du,\qquad
\widehat\phi^\alpha(Z)=\sum_n Z^n\phi_n^\alpha.
\]
For a vector in \(V\), this series is bounded below in its powers of \(Z\), and only finitely many unit characters occur. For a vector in \(V_0\), it is a Laurent polynomial.

Define \(C_n^\alpha\in\operatorname{End}(X)\) as follows: apply \(W=\pi(w_0)\) to the compact function \(1_U(u)\alpha(u)\epsilon(u)x\), and take its \(n\)-th \(\alpha\)-coefficient. Torus conjugation and unit Fourier inversion give, for compact \(\phi\),
\[
(W\phi)_n^\alpha
 =\sum_p z^{-p}C_{n+p}^\alpha\phi_p^{\widetilde\alpha}.
\tag{2.1}
\]
For clarity, a function \(1_U\alpha\epsilon\,x\) has just the coefficient
\(\phi_0^{\widetilde\alpha}=x\). Dilation by \(\varpi^j\) shifts its input index to \(-j\), while \(W d(\varpi^j)=z^j d(\varpi^{-j})W\) shifts the output index by \(j\) and multiplies it by \(z^j\). This proves (2.1) on generators and hence on all compact functions. For each fixed \(x\), \(C_n^\alpha x=0\) when \(n\) is sufficiently negative.

Set
\[
\eta(\chi,b)=\int_U\chi(u)\psi(bu)\,du.
\]
Finite Fourier inversion on \(U\) gives
\[
(\pi(n(y))\phi)_n^\alpha
 =\sum_\beta\eta(\beta^{-1}\alpha,\varpi^n y)\phi_n^\beta.
\tag{2.2}
\]

We need two elementary Gauss-sum facts. If a nontrivial unit character \(\chi\) has conductor \(\varpi^m\), then
\[
\eta(\chi,\varpi^r)=0\quad(r\ne-m-\ell),\qquad
\eta(\chi,\varpi^{-m-\ell})\ne0.
\tag{2.3}
\]
At frequencies of smaller absolute value, averaging over the last nontrivial unit subgroup cancels \(\chi\); when \(m=1\), this is simply the sum of a nontrivial character of the residue-field units. At larger frequencies, average over additive cosets of \(\varpi^m\), where \(\chi\) is constant but the additive character is nontrivial. At the critical frequency, extend \(\chi\) by zero to \(\mathcal O/\varpi^m\). Its finite Fourier transform vanishes at nonunit frequencies, by the same subgroup cancellation, and its values at unit frequencies differ by unit-character factors. Parseval gives the square of each unnormalized critical Gauss sum as \(q^m\): the original function has \(q^m-q^{m-1}\) entries of absolute value one. Thus it cannot vanish. For the trivial character,
\[
\eta(1,\varpi^r)=
\begin{cases}
1&r\ge-\ell,\\
-1/(q-1)&r=-\ell-1,\\
0&r\le-\ell-2.
\end{cases}
\tag{2.4}
\]
Indeed integrate over \(\mathcal O\setminus\varpi\mathcal O\), subtracting the two additive-ball integrals and dividing by \(1-q^{-1}\).

**Lemma 2.1 — a symmetric coefficient identity.** Put \(h=\alpha\beta\epsilon\) and
\[
S_{n,p}^{\alpha,\beta}
 =\sum_\sigma\eta(\sigma^{-1}\alpha,\varpi^n)
                 \eta(\sigma^{-1}\beta,\varpi^p)C_{n+p}^{\sigma}.
\]
Then
\[
h(-1)S_{n,p}^{\alpha,\beta}
 =\sum_r z^{-r}\bigl(\eta(h^{-1},\varpi^r)-1_{h=1}\bigr)
       C_{n+r}^{\alpha}C_{p+r}^{\beta}
 +\epsilon(-1)z^p1_{n=p}1_{h=1}I_X.
\tag{2.5}
\]

**Proof.** The matrix relation
\(w_0n(1)w_0=-n(-1)w_0n(-1)\) gives
\[
W(\pi(n(1))-1)W\phi+\epsilon(-1)\phi
 =\epsilon(-1)\pi(n(-1))W\pi(n(-1))\phi.
\tag{2.6}
\]
Its middle input \((\pi(n(1))-1)W\phi\) is compact by Proposition 1.3, so (2.1) is applicable. To extract a coefficient without informal infinite-series multiplication, take a compact input with its only nonzero coefficient \(\phi_p^\rho=x\).

By (2.1), \(W\phi\) has only the unit-character packet \(\widetilde\rho\). Apply (2.2), subtract its original packet, then apply (2.1) again. The coefficient of the left side of (2.6), at output \((n,\alpha)\), is
\[
\sum_r z^{-p-r}
 \bigl(\eta(\rho\alpha^{-1},\varpi^r)-1_{\rho=\alpha}\bigr)
 C_{n+r}^{\alpha}C_{p+r}^{\widetilde\rho}x
 +\epsilon(-1)1_{n=p}1_{\rho=\alpha}x.
\tag{2.7}
\]
Applying (2.2), (2.1), (2.2) successively to the right side gives
\[
\epsilon(-1)z^{-p}\sum_\sigma
 \eta(\sigma^{-1}\alpha,-\varpi^n)
 \eta(\rho^{-1}\sigma^{-1}\epsilon^{-1},-\varpi^p)
 C_{n+p}^{\sigma}x.
\tag{2.8}
\]
Use \(\eta(\chi,-b)=\chi(-1)\eta(\chi,b)\), put
\(\beta=\widetilde\rho\), and multiply by \(z^p\). The sign in (2.8) becomes \(h(-1)\); \(\rho\alpha^{-1}=h^{-1}\). This is precisely (2.5).

All sums are legitimate on the fixed \(x\). The \(\sigma\)-sum is finite by the Gauss-sum conductor bounds in its two factors. The \(r\)-sum is finite: (2.3) leaves one term when \(h\ne1\); when \(h=1\), (2.4) kills its large positive indices and \(C_{p+r}^{\beta}x=0\) kills its sufficiently negative indices. Thus this coefficient extraction uses only finite sums. \(\square\)

**Proposition 2.2 — commuting coefficients.** Every \(C_n^\alpha\) commutes with every \(C_p^\beta\).

**Proof.** The left side of (2.5) is symmetric under \((n,\alpha)\leftrightarrow(p,\beta)\). If \(h\ne1\) has conductor \(\varpi^m\), (2.3) makes its right side a nonzero scalar times
\(C_{n-m-\ell}^{\alpha}C_{p-m-\ell}^{\beta}\). Swapping proves commutation for all indices in this case.

If \(h=1\), (2.4) rewrites (2.5) as
\[
S_{n,p}^{\alpha,\widetilde\alpha}
 =\epsilon(-1)z^p1_{n=p}I_X
 +a C_{n-\ell-1}^{\alpha}C_{p-\ell-1}^{\widetilde\alpha}
 -\sum_{r\le-\ell-2}z^{-r}
       C_{n+r}^{\alpha}C_{p+r}^{\widetilde\alpha},
\quad
a=\frac{z^{\ell+1}}{q^{-1}-1}\ne0.
\tag{2.9}
\]
Subtract the swapped identity. The identity-operator terms cancel, since \(n=p\) makes \(z^p=z^n\). For fixed integers \(i,j\) and \(x\in X\), both ordered products
\(C_{i+k}^{\alpha}C_{j+k}^{\widetilde\alpha}x\) and its reverse are zero for sufficiently negative \(k\): their respective right factors vanish. Insert
\(n=i+k+\ell+1,\ p=j+k+\ell+1\) in (2.9). Its subtraction expresses \(a\) times the commutator at shift \(k\) as a finite sum of commutators at shifts at most \(k-1\). Induction starting at the vanishing negative shifts proves the required commutator is zero on \(x\). Since \(x\) was arbitrary, all coefficients commute. \(\square\)

**Theorem 2.3 — Whittaker existence and uniqueness.** For an irreducible smooth admissible \(G\)-representation,
\[
\dim\operatorname{Hom}_N(V,\psi)=
\begin{cases}0&\dim V<\infty,\\1&\dim V=\infty.\end{cases}
\tag{2.10}
\]

**Proof.** In the infinite-dimensional case, let \(A\in\operatorname{End}(X)\) commute with all \(C_n^\alpha\). Its pointwise action preserves \(V_0\). Formula (2.1) says that it also preserves \(WV_0\), and that \(AW=WA\) on \(V_0\). By (1.3) it preserves \(V\). On \(WV_0\), the identity \(W^2=\epsilon(-1)I\) gives commutation with \(W\) as well. It commutes with \(N\), the torus and the center by their pointwise formulas, so countable Schur makes its action on \(V\) scalar. Evaluating compact functions at one makes the original \(A\) scalar on \(X\).

Proposition 2.2 permits taking \(A=C_n^\alpha\), so each coefficient is scalar. Now every endomorphism of \(X\) commutes with them, hence every endomorphism is scalar. A nonzero vector space of dimension at least two has a nonscalar projection, obtained by extending two independent vectors to a basis. Therefore \(\dim X=1\), and (1.1) proves the assertion. In the finite-dimensional case, Lesson 5 makes \(V=\chi\circ\det\). Since \(N\) acts trivially and \(\psi\ne1\), a Whittaker functional is zero. \(\square\)

## 3. Whittaker functions, Kirillov functions and a Weyl kernel

Choose a nonzero Whittaker functional \(\lambda\). The functions
\[
W_v(g)=\lambda(\pi(g)v),\qquad
\xi_v(t)=W_v(d(t))
\]
satisfy \(W_v(n(x)g)=\psi(x)W_v(g)\); right translation corresponds to \(\pi\). The map to \(\xi_v\) is injective by Lemma 1.2. The image \(\mathcal K(\pi,\psi)\) is the Kirillov model. Scaling \(\lambda\) does not change its function space. The image of \(v\mapsto W_v\) is the Whittaker model \(\mathcal W(\pi,\psi)\). Any equivariant map into smooth \(\psi\)-equivariant functions on \(G\) is determined by evaluation at the identity; this evaluation is a Whittaker functional. Theorem 2.3 therefore makes that realization unique up to scalar, and its image unique.

By Proposition 1.3,
\[
C_c^\infty(F^\times)\subset\mathcal K(\pi,\psi),\qquad
\mathcal K(\pi,\psi)/C_c^\infty(F^\times)\simeq V_N.
\tag{3.1}
\]
The isomorphism uses the **unnormalized** Jacquet module. Its torus action is the induced dilation action. To obtain \(r_N(V)\), twist this action by \(\delta_B^{-1/2}\).

For any upper triangular matrix,
\[
\left(\pi\begin{pmatrix}a&b\\0&d\end{pmatrix}\xi\right)(t)
 =\omega(d)\psi(tb/d)\xi(ta/d).
\tag{3.2}
\]
In particular \(\pi(d(a)n(x))\xi(t)=\psi(tax)\xi(ta)\), while
\(\pi(n(x)d(a))\xi(t)=\psi(tx)\xi(ta)\). The order matters.

Equations (2.1) and unit Fourier inversion are an explicit Weyl operator for every irreducible generic representation. More concretely, if the compact input \(\xi\) is fixed under unit dilation by an open subgroup \(H\), let
\(R_H=\{\alpha:\widetilde\alpha|_H=1\}\), a finite set. Then
\[
(W\xi)(\varpi^n v)=
 \sum_p\int_U
 z^{-p}\epsilon(u)^{-1}
 \left(\sum_{\alpha\in R_H}C_{n+p}^\alpha\alpha(uv)^{-1}\right)
 \xi(\varpi^p u)\,du,\qquad v\in U.
\tag{3.3}
\]
Only finitely many input shells \(p\) occur. The coefficients are now complex scalars. This is a finite unit-Fourier kernel on each space of compact inputs with fixed unit level. It determines the full \(G\)-action because \(V=V_0+WV_0\) and \(W^2=\omega(-1)\). For principal series we will calculate a closed integral form in Section 5.


## 4. Principal series and the two exceptional extensions

Let
\[
I(\mu_1,\mu_2)=\operatorname{Ind}_B^G(\mu_1\otimes\mu_2)
\]
with the normalized multiplier \(|a/d|^{1/2}\mu_1(a)\mu_2(d)\) and right translation as in Lesson 6.

**Lemma 4.1 — three facts about an induced representation.**

1. Its twisted coinvariants have dimension one.
2. A character subrepresentation \(\chi\circ\det\) exists exactly when
\((\mu_1,\mu_2)=(\chi\nu^{-1/2},\chi\nu^{1/2})\).
3. A character quotient \(\chi\circ\det\) exists exactly when
\((\mu_1,\mu_2)=(\chi\nu^{1/2},\chi\nu^{-1/2})\).

Each character map in the last two assertions has a one-dimensional Hom space.

**Proof.** The two Bruhat cells give an exact sequence of \(N\)-modules
\[
0\longrightarrow C_c^\infty(F)\longrightarrow I(\mu_1,\mu_2)
 \longrightarrow\mathbb C\longrightarrow0.
\]
On the open chart \(f_o(x)=f(w n(x))\), with \(w=-w_0\), \(N\) acts by translation \(f_o(x+y)\); it acts trivially on the closed cell. The latter has zero \(\psi\)-coinvariants. On the open cell the nonzero functional
\(f_o\mapsto\int_F f_o(x)\psi(-x)\,dx\) gives its twisted coinvariant line. Its kernel is precisely the twisted-difference space: once an additive ideal \(D\) contains the support of \(f_o\), its weighted average on \(D\) is a scalar times \(\psi(x)1_D(x)\), with scalar this integral. Lemma 1.1 proves the claim. Exactness now proves assertion 1.

Normalized reciprocity says
\[
\operatorname{Hom}_G(\chi\circ\det,I(\mu_1,\mu_2))
 =\operatorname{Hom}_T\bigl(
 \chi(a)\chi(d)|a/d|^{-1/2},\,\mu_1(a)\mu_2(d)\bigr).
\]
These are characters of \(T\), so this space is one-dimensional precisely in assertion 2 and is zero otherwise. The induced dual from Lesson 6 is
\(I(\mu_1^{-1},\mu_2^{-1})\). Dualizing a character quotient makes it a character subrepresentation of this dual, proving assertion 3, including its dimension. \(\square\)

For any \(I=I(\mu_1,\mu_2)\), an \(N\)-invariant vector injects into \(I_N\): a vector both invariant and an ordinary difference is killed by a sufficiently large average, while averaging leaves it unchanged. Lesson 6 gives \(\dim I_N=2\). By Lemma 1.2 the \(N\)-fixed space factors through determinant; if nonzero, this finite-dimensional space has a character subrepresentation, by simultaneous triangularization of commuting matrices. Consequently
\[
\mu_1/\mu_2\ne\nu^{-1}
 \quad\Longrightarrow\quad I^N=0
 \quad\Longrightarrow\quad \Phi:I\longrightarrow\{\text{scalar functions on }F^\times\}
 \text{ is injective}.
\tag{4.1}
\]
We identify its one-dimensional twisted fiber with \(\mathbb C\). The compact-function construction and the ordinary-difference argument in Proposition 1.3 used only injectivity, so they apply to this induced representation as well:
\[
I(N)=C_c^\infty(F^\times)=:V_0.
\tag{4.2}
\]
Every nonzero \(G\)-subrepresentation \(A\subset I\) has a nonzero twisted fiber. Otherwise each \(\pi(d(t))v\), \(v\in A\), would have zero class in the fiber of \(I\), contradicting injectivity. Exactness injects that fiber into the one-dimensional fiber of \(I\), so it is the entire fiber. Applying the Fourier-ball projectors to vectors of \(A\) now yields
\[
V_0\subset A.
\tag{4.3}
\]

**Theorem 4.2 — irreducibility and exceptional factors.** The principal series is irreducible if and only if
\(\mu_1/\mu_2\notin\{\nu,\nu^{-1}\}\). At the two exceptional ratios it has length two. Writing \(D_\chi=\chi\circ\det\) and \(\mathrm{St}_\chi=\mathrm{St}\otimes D_\chi\), the exact sequences are
\[
0\longrightarrow\mathrm{St}_\chi
 \longrightarrow I(\chi\nu^{1/2},\chi\nu^{-1/2})
 \longrightarrow D_\chi\longrightarrow0,
\tag{4.4}
\]
\[
0\longrightarrow D_\chi
 \longrightarrow I(\chi\nu^{-1/2},\chi\nu^{1/2})
 \longrightarrow\mathrm{St}_\chi\longrightarrow0.
\tag{4.5}
\]
The Steinberg representations are irreducible, and these extensions do not split.

**Proof.** First suppose neither exceptional ratio occurs. The \(G\)-span \(G V_0\) has finite-dimensional quotient in \(I\), because \(V_0=I(N)\) and \(\dim I_N=2\). \(N\) acts trivially on that quotient; its normal closure \(\mathrm{SL}_2(F)\) consequently does too. If nonzero, the quotient is a finite-dimensional representation of the abelian group \(F^\times\), and has a character quotient. This contradicts Lemma 4.1(3). Thus \(G V_0=I\). Equation (4.3) makes every nonzero subrepresentation all of \(I\).

At ratio \(\nu\), twist by \(D_\chi^{-1}\) to reduce to
\(I_+=I(\nu^{1/2},\nu^{-1/2})\). Lesson 6 explicitly constructed
\(0\to\mathrm{St}\to I_+\to1\to0\), without assuming Steinberg irreducibility. Its character quotient kills \(I_+(N)=V_0\), so \(V_0\subset\mathrm{St}\).
The quotient \(\mathrm{St}/G V_0\) is finite-dimensional and \(N\)-trivial. If it were nonzero it would have a character quotient \(D_\eta\). Exactness of normalized Jacquet modules would give a nonzero torus quotient map
\[
(\nu^{1/2},\nu^{-1/2})=r_N(\mathrm{St})
 \longrightarrow
(\eta\nu^{-1/2},\eta\nu^{1/2})=r_N(D_\eta).
\]
The two characters cannot coincide: their ratio on the two diagonal coordinates would force both \(\eta=\nu\) and \(\eta=\nu^{-1}\). Thus \(\mathrm{St}=G V_0\). Every nonzero subrepresentation of \(\mathrm{St}\), viewed inside \(I_+\), contains \(V_0\) by (4.3), so it is all of \(\mathrm{St}\). This proves irreducibility.

It follows that any nonzero proper subrepresentation of \(I_+\) is \(\mathrm{St}\): it contains \(\mathrm{St}\), and the remaining quotient has dimension one. Lemma 4.1(2) prohibits a trivial subrepresentation of \(I_+\), so (4.4) does not split. Lesson 6 proved \(\mathrm{St}^\vee\simeq\mathrm{St}\) and the induced duality. Dualizing (4.4) with inverse twist gives (4.5), also nonsplit and of length two. Both exceptional series are therefore reducible. \(\square\)

## 5. An explicit principal-series Weyl kernel and parameter symmetry

This computation also proves the interchange of principal-series parameters. Put \(r=\mu_1/\mu_2\) and use the self-dual additive measure \(dx\). For the open chart of a section \(f\), define
\[
\Lambda(f)=\int_F^{\mathrm{st}} f_o(x)\psi(-x)\,dx,\qquad
\xi_f(t)=|t|^{1/2}\mu_2(t)\int_F^{\mathrm{st}} f_o(x)\psi(-tx)\,dx.
\tag{5.1}
\]
Here “st” means that the integrals over increasing additive balls eventually have the same value. They exist for every pair of smooth characters. Indeed for large \(|x|\),
\[
w n(x)=
\begin{pmatrix}x^{-1}&-1\\0&x\end{pmatrix}
\begin{pmatrix}1&0\\x^{-1}&1\end{pmatrix},\qquad
f_o(x)=|x|^{-1}r(x)^{-1}f(1).
\]
The lower matrix eventually lies in a right stabilizer of \(f\). Far-out shell integrals of this tail times \(\psi(-tx)\) vanish by the Gauss-sum bounds of Section 2. This is uniform when \(t\) ranges over a compact subset of \(F^\times\). Translation of a sufficiently large integration ball proves that \(\Lambda\) is a Whittaker functional. It is nonzero on an open-cell bump. The identity for \(\xi_f\) follows from \(w d(t)=\operatorname{diag}(1,t)w\) and the substitution \(x=ty\).

For \(z'\ne0\), define the stable Bessel integral
\[
J_r(z')=\int_{F^\times}^{\mathrm{st}}
 r(u)\psi(u+z'/u)\,\frac{du}{|u|}.
\tag{5.2}
\]
At the large-\(|u|\) end, \(\psi(z'/u)=1\), and the remaining shell integrals vanish beyond the conductor of \(r|_U\). At the small-\(|u|\) end, invert \(u\) to obtain the same argument. Thus only finitely many shells contribute. Their bounds can be chosen uniformly on compact sets of \(z'\ne0\).

**Proposition 5.1 — Weyl action.** If \(\mu_1/\mu_2\ne\nu^{-1}\), the injective scalar model of \(I(\mu_1,\mu_2)\) obeys, for \(\xi\in C_c^\infty(F^\times)\),
\[
(W\xi)(t)=\int_{F^\times}
 |ts|^{1/2}\mu_2(t)\mu_1(s)^{-1}J_r(ts)\xi(s)\,\frac{ds}{|s|}.
\tag{5.3}
\]

**Proof.** Extend \(\xi(s)/(|s|^{1/2}\mu_2(s))\) by zero at \(s=0\). It is a compact locally constant function on \(F\), so its inverse Fourier transform is
\[
f_o(x)=\int_F
 \xi(s)|s|^{-1/2}\mu_2(s)^{-1}\psi(sx)\,ds.
\]
This is a compact locally constant open-cell section and gives \(\xi\) by (5.1); injectivity makes it the unique section with that Kirillov function. Matrix multiplication and the Bruhat factorization give, for \(x\ne0\),
\[
(\pi(w_0)f)_o(x)
 =\omega(-1)|x|^{-1}r(x)^{-1}f_o(-x^{-1}).
\]
Insert the inverse Fourier integral into (5.1). For each \(s\ne0\), substitute \(u=-s/x\). The phase \(-tx-s/x\) becomes \(ts/u+u\). Multiplicative measure is invariant under this substitution. The sign factor is
\(\omega(-1)r(-1)=\mu_1(-1)^2=1\). The remaining factor, after replacing \(ds\) by \(|s|\,ds/|s|\), is
\[
|t|^{1/2}\mu_2(t)\,
 |s|^{1/2}\mu_2(s)^{-1}r(s)^{-1}
 =|ts|^{1/2}\mu_2(t)\mu_1(s)^{-1}.
\]
This gives (5.3). The interchange of integrals is justified first on finite annuli. For \(s\) in the compact support of \(\xi\), the shell-vanishing bounds for (5.2) are uniform; increasing the annuli changes neither side. No assertion of absolute convergence at both infinite ends is needed. \(\square\)

**Corollary 5.2 — the unordered parameter pair.** If the principal series is irreducible, then
\[
I(\mu_1,\mu_2)\simeq I(\mu_2,\mu_1).
\tag{5.4}
\]

**Proof.** In (5.2), the substitution \(u=z'/v\) gives
\[
J_r(z')=r(z')J_{r^{-1}}(z').
\tag{5.5}
\]
Its factor converts the kernel in (5.3) into
\[
|ts|^{1/2}\mu_1(t)\mu_2(s)^{-1}J_{r^{-1}}(ts),
\]
the kernel for the swapped parameters. The two models have the same compact part, the same pointwise upper-triangular action (3.2), and the same central character \(\mu_1\mu_2\). Their Weyl actions on the compact part agree by (5.3). By (1.3) each model is \(V_0+WV_0\); hence their function spaces agree. On such a sum, the Weyl action is determined by its action on \(V_0\) and \(W^2=\omega(-1)\). Thus all generating matrices have the same action, giving (5.4). \(\square\)

## 6. Classification and the germs at zero

**Theorem 6.1 — the four families.** Every irreducible smooth representation of \(G\) belongs to exactly one of the following families:
\[
D_\chi;\qquad \mathrm{St}_\chi;\qquad
I(\mu_1,\mu_2)\ \ (\mu_1/\mu_2\ne\nu^{\pm1});\qquad
\text{supercuspidal representations }(V_N=0).
\tag{6.1}
\]
The principal-series parameter is the unordered pair \(\{\mu_1,\mu_2\}\). Character and Steinberg twists each have their unique parameter \(\chi\). No representation in one family is isomorphic to a representation in another.

**Proof.** Admissibility is already proved in Lesson 6, Theorem 5.4. A finite-dimensional irreducible is \(D_\chi\) by Lesson 5. If an infinite-dimensional irreducible has \(V_N\ne0\), Lesson 6 embeds it in a normalized principal series. Theorem 4.2 shows that it is either that entire irreducible principal series or the infinite-dimensional constituent of an exceptional series, namely \(\mathrm{St}_\chi\). If \(V_N=0\), the equivalence with the matrix-coefficient definition of supercuspidality is proved in Lesson 6, Theorems 5.2–5.3.

Their Jacquet dimensions are
\[
\dim V_N=0\text{ for supercuspidals},\quad
1\text{ for }\mathrm{St}_\chi,\quad
2\text{ for irreducible principal series}.
\tag{6.2}
\]
The last two values are the exact cell and Steinberg calculations of Lesson 6. Together with finite versus infinite dimension, these separate the families. The two torus characters in the semisimplified normalized Jacquet module of a principal series are
\((\mu_1,\mu_2)\) and \((\mu_2,\mu_1)\). They recover the unordered pair, and Corollary 5.2 proves its sufficiency. For Steinberg,
\[
r_N(\mathrm{St}_\chi)=(\chi\nu^{1/2},\chi\nu^{-1/2}),
\]
which recovers \(\chi\). Determinant recovers \(\chi\) for \(D_\chi\). The list leaves the individual supercuspidal classes as parameters; it does not assert that their common zero Jacquet module distinguishes them. \(\square\)

Equations (3.1) and (6.2) prove that the compact part has codimension zero, one or two. These numbers have a concrete function interpretation. Put \(\tau_i(t)=|t|^{1/2}\mu_i(t)\).

**Proposition 6.2 — complete function spaces.** All functions below are locally constant on \(F^\times\) and supported in \(|t|\le C\) for some \(C\).

- A supercuspidal has \(\mathcal K(\pi,\psi)=C_c^\infty(F^\times)\).
- For \(\mathrm{St}_\chi\), the model consists exactly of these functions with germ \(c|t|\chi(t)\) at zero.
- For an irreducible principal series with \(\mu_1\ne\mu_2\), it consists exactly of these functions with germ \(c_1\tau_1(t)+c_2\tau_2(t)\).
- When \(\mu_1=\mu_2=\mu\), replace this germ by
\(|t|^{1/2}\mu(t)(c_1+c_2v_F(t))\), where \(v_F(\varpi)=1\).

**Proof.** Zero Jacquet module proves the first assertion directly from (3.1). For Steinberg, the unnormalized dilation character on the one-dimensional quotient is \(\nu\chi\). Average a lift of its nonzero class over \(U\) with this unit character. The lift \(f\) can therefore be chosen to transform exactly by \(\chi|_U\) under unit dilation. The relation
\(f(\varpi t)-|\varpi|\chi(\varpi)f(t)\in C_c^\infty(F^\times)\) holds on the quotient, so it is zero for sufficiently small \(|t|\). Solving this recurrence gives the germ \(c|t|\chi(t)\). Its coefficient is nonzero for a nonzero quotient class; otherwise the lift itself would be compact away from zero.

For distinct principal-series characters the normalized Jacquet module splits into its two distinct character lines. To see splitting directly, choose a torus element where their eigenvalues differ; its two eigenspaces are stable under all commuting torus operators. The corresponding unnormalized dilation characters are \(\tau_1,\tau_2\). Choose unit-isotypic lifts by compact averaging and solve the uniformizer recurrence as above. Each nonzero quotient line gives a nonzero multiple of its \(\tau_i\). They span the two-dimensional germ space.

When the parameters coincide, every unit acts as a scalar on the quotient, since compact-unit representations are semisimple and both constituents have the same character. Dilation by \(\varpi\) has both eigenvalues \(\tau(\varpi)\). It cannot act as a scalar: the preceding recurrence would then make every germ a multiple of \(\tau\), contradicting the two-dimensional quotient. It therefore has one Jordan block. Lift a Jordan basis with exact unit transformation. The first lift has germ \(c\tau\); the second satisfies, near zero,
\[
f_2(\varpi t)-\tau(\varpi)f_2(t)=f_1(t).
\]
Dividing by \(\tau(\varpi t)\) gives a constant first difference along valuation indices. Its solutions are exactly an affine function of \(v_F(t)\) times \(\tau(t)\).

Finally each indicated germ is realized by these lifts. Any other function with the same germ differs from its lift by a compact function supported away from zero, which lies in the model. This proves equality of the function spaces, not just necessary asymptotics. \(\square\)

**Example 6.3 — Steinberg.** For the untwisted Steinberg representation,
\[
\mathcal K(\mathrm{St},\psi)
 =\{\xi:\operatorname{supp}\xi\subset\{|t|\le C\},
           \ \xi(t)=c|t|\text{ for sufficiently small }|t|\}.
\tag{6.3}
\]
For example \(|t|1_{\{|t|\le1\}}\) gives a nonzero quotient class. A compact bump gives the zero class. The factor is \(|t|\), rather than \(1\), because the quotient in (3.1) is unnormalized.

**Example 6.4 — unramified principal series and a repeated parameter.** If \(\mu_1,\mu_2\) are unramified, write \(\alpha=\mu_1(\varpi)\), \(\beta=\mu_2(\varpi)\). For \(\alpha/\beta\ne q^{\pm1}\) and \(\alpha\ne\beta\), the two germs on \(t=\varpi^n u\), \(n\) large, are
\(q^{-n/2}\alpha^n\) and \(q^{-n/2}\beta^n\). Extend each by zero for \(n<0\); Proposition 6.2 puts both extensions in the model. Their classes are independent. If \(\alpha=\beta\), the two germs are instead
\(q^{-n/2}\alpha^n\) and \(nq^{-n/2}\alpha^n\). Equal parameters still give an irreducible principal series: the exceptional ratios are \(q\) and \(q^{-1}\), not \(1\).

**Example 6.5 — supercuspidal.** A supercuspidal Kirillov function always vanishes on a sufficiently small neighborhood of zero as well as outside a bounded ball. Every compact bump away from zero occurs, and there are no additional germs. Thus its model is exactly the compact-function space, although its Weyl coefficients in (3.3) carry information that differentiates supercuspidal representations.

Deligne's *Formes modulaires et représentations de GL(2)*, §2.2, Théorème 2.2.4, singles out this finite codimension as the difficult part of the Kirillov-model theorem. Here the compact inclusion comes from Fourier-ball projectors; the finite bound comes from the principal-series embedding and classification. These are distinct steps. Uniqueness of the functional alone would not give the bound.

## 7. Unitarity and temperedness

A smooth irreducible representation is **unitarizable** if it has a positive definite \(G\)-invariant Hermitian form. We call a representation with unitary central character **tempered** when all its smooth matrix coefficients belong to \(L^{2+\epsilon}(G/Z)\) for every \(\epsilon>0\). The following proof gives both classifications without using a classification of higher-rank unitary representations.

**Theorem 7.1 — the unitary families.** The irreducible unitarizable representations are \(D_\chi\) and \(\mathrm{St}_\chi\) with \(\chi\) unitary; supercuspidals with unitary central character; principal series with both inducing characters unitary; and the complementary series
\[
I(\chi\nu^s,\chi\nu^{-s}),\qquad
\chi\text{ unitary},\quad 0<s<\tfrac12.
\tag{7.1}
\]
At \(s=1/2\), the principal series has the two constituents in (4.4), rather than being an additional irreducible family.

**Necessity.** An invariant positive form makes the central character unitary. Admissibility from Lesson 6, Theorem 5.4, identifies the Hermitian dual with the representation itself: the form gives an injection into the conjugate smooth dual, and it is onto on every fixed space by finite-dimensional duality. For a principal series, Lesson 6, Proposition 1.2, and Corollary 5.2 therefore give
\[
\{\mu_1,\mu_2\}
=\{\overline{\mu_1}^{-1},\overline{\mu_2}^{-1}\}.
\]
Either each character is unitary, or they are exchanged by this involution. In the second case write \(\mu_1=\chi\nu^s\), with \(\chi\) unitary and \(s\) real; smooth characters have unitary restriction to the compact unit group, and their absolute values are powers of \(\nu\). Then \(\mu_2=\chi\nu^{-s}\). Swapping the parameters permits \(s>0\).

The smoothed evaluation argument in the proof of Lesson 6, Theorem 5.2, gives a smooth matrix coefficient that, for all sufficiently large \(r\), is a nonzero constant times
\(\delta_B(t_r)^{1/2}\mu_1(\varpi)^r\), where
\(t_r=\operatorname{diag}(\varpi^r,1)\). Order the pair so
\(|\mu_1(\varpi)|=q^s\). Its absolute value is a positive constant times \(q^{(s-1/2)r}\). If \(s>1/2\), this is unbounded, contradicting Cauchy–Schwarz for an invariant positive form. At \(s=1/2\), the principal series is reducible by Theorem 4.2. This proves the necessary range. For a character or Steinberg twist, the central character is \(\chi^2\), so its unitarity forces \(\chi\) to be unitary.

**Unitary principal series and supercuspidals.** For unitary inducing characters, the compact-model pairing is positive. Equivalently, in the open chart it is
\(\int_F|\phi(x)|^2dx\), with \(\phi(x)=f(wn(x))\). The \(N,T,w\) changes of variables in Lesson 6, Proposition 1.2, prove invariance, now with complex conjugation. The chart determines the section and the form is positive definite.

For a supercuspidal with unitary central character, choose a nonzero smooth functional \(\ell\). Theorem 5.3 of that lesson proves compact support of each coefficient modulo \(Z\), so
\[
H(v,u)=\int_{G/Z}\ell(\pi(g)v)
                    \overline{\ell(\pi(g)u)}\,d\bar g
\]
converges. The integrand descends because the central character is unitary. The quotient group is unimodular, so right translation proves invariance. The form is nonzero, since a nonzero value of \(\ell(v)\) persists on an open neighborhood. Its radical is invariant and hence zero by irreducibility. This gives the required positive form.

**Complementary series.** A common unitary determinant twist does not affect positivity, so take \(I(\nu^s,\nu^{-s})\), \(0<s<1/2\). Its open-chart functions satisfy
\[
|\phi(x)|\leq C\max(1,|x|)^{-1-2s}.
\]
The bound follows from Iwasawa decomposition and the bounded restriction to \(K_0\). Define
\[
H_s(\phi,\psi)=
\int_{F^2}\phi(x)\overline{\psi(y)}
                  |x-y|^{-1+2s}\,dx\,dy.
\tag{7.2}
\]
The kernel is locally integrable at the diagonal, since \(2s>0\). Away from it the kernel is bounded, while both functions are integrable and bounded. These observations prove absolute convergence.

Put \(\lambda=1-2s>0\). For \(z\ne0\),
\[
|z|^{-\lambda}
=\sum_{m\in\mathbb Z}
  (q^{m\lambda}-q^{(m-1)\lambda})\,1_{\varpi^m\mathcal O}(z).
\]
Every coefficient is positive. The quadratic form of a ball kernel is
\[
Q_m(\phi)=
\sum_{C\in F/\varpi^m\mathcal O}
             \left|\int_C\phi(x)\,dx\right|^2\geq0.
\]
Absolute convergence of (7.2) justifies the expansion of its quadratic form. A nonzero locally constant \(\phi\) is constant and nonzero on some sufficiently small ball, so some \(Q_m(\phi)>0\). Thus \(H_s\) is positive definite.

Translations preserve (7.2). For \(t=\operatorname{diag}(a,d)\), write \(b=d/a\). Its action is
\(\phi(x)\mapsto |b|^{1/2+s}\phi(bx)\); the two Jacobians and the kernel's homogeneity cancel the multiplier. For \(w\), the open-cell factorization gives
\[
\phi(x)\longmapsto |x|^{-1-2s}\phi(-1/x).
\]
Under \(u=-1/x,\ v=-1/y\), use
\(|x-y|=|u-v|/(|uv|)\) and \(dx=|u|^{-2}du\).
Again all multipliers cancel. The omitted points have measure zero. Since \(N,T,w\) generate \(G\), this proves invariance and sufficiency for the complementary series.

**Steinberg.** Untwist \(\chi\). By Lesson 6, equation (6.3), realize \(\mathrm{St}\) inside \(I(\nu^{1/2},\nu^{-1/2})\). In the open chart its functions have
\[
|\phi(x)|\leq C\max(1,|x|)^{-2},
\qquad \int_F\phi(x)\,dx=0.
\]
The last condition is precisely the trivial quotient functional in that lesson. Define
\[
H_{\mathrm{St}}(\phi,\psi)=
-\int_{F^2}\phi(x)\overline{\psi(y)}\log|x-y|\,dx\,dy
=(\log q)\sum_{m\in\mathbb Z}Q_m(\phi,\psi),
\tag{7.3}
\]
where \(Q_m(\phi,\psi)\) is the polarized ball form. The logarithmic integral is absolutely convergent: near the diagonal use boundedness, integrability and the integrable function \(|\log|z||\); at infinity use the displayed quadratic decay.

To verify the second equality, use
\[
v_F(z)=\sum_{m\in\mathbb Z}
 (1_{\varpi^m\mathcal O}(z)-1_{m\leq0}).
\]
Symmetric finite truncations are bounded in absolute value by \(|v_F(z)|\), so dominated convergence applies. Each subtracted constant contributes zero because both means vanish. The series is convergent: for \(m\to+\infty\), Cauchy–Schwarz gives
\(Q_m(\phi)\leq q^{-m}\|\phi\|_2^2\). For \(m\to-\infty\), the zero mean and the \(O(|x|^{-2})\) tail give
\(Q_m(\phi)=O(q^{2m})\). Indeed the integral on the ball containing zero is the negative tail integral, of size \(O(q^m)\), and the absolute integrals on all other cosets have total size \(O(q^m)\). Polarization gives convergence for the mixed form as well. Positivity and strict positivity follow from the same small-ball argument as before.

Translations preserve (7.3). Torus scaling adds a constant to the logarithm, whose contribution vanishes by the zero means. Under inversion, the two Jacobians cancel the multipliers \(|x|^{-2}\), and
\[
-\log|x-y|=-\log|u-v|+\log|u|+\log|v|.
\]
The last two terms again vanish by the zero means; their integrals converge by the same decay bounds. Hence (7.3) is invariant. This proves Steinberg unitarity and finishes Theorem 7.1. \(\square\)

Every positive form constructed above gives a strongly continuous unitary completion. Smooth vectors have finite-dimensional fixed spaces. Averaging the dense smooth space shows that the completion's \(J\)-fixed space is exactly that same finite-dimensional space. Thus a commuting orthogonal projection preserves the smooth representation and is scalar by Schur's lemma; the completion is irreducible. This argument concerns the completions just constructed and uses the proved smooth admissibility theorem.

**Theorem 7.2 — the tempered families.** Among representations with unitary central character, the tempered ones are precisely unitary principal series, unitary Steinberg twists and supercuspidals.

**Proof of the positive assertions.** Normalize the image of \(K_0\) in \(G/Z\) to have volume one. For \(r\geq1\),
\[
\operatorname{vol}(K_0t_rK_0/Z)
=(q+1)q^{r-1}.
\tag{7.4}
\]
Here the notation means the image of that double coset in \(G/Z\). Its right compact cosets are counted by primitive rows modulo \(\varpi^r\), up to a unit scalar. There are \(q^{2r}-q^{2r-2}\) primitive rows and \(q^r-q^{r-1}\) unit scalars; dividing gives (7.4). The Cartan decomposition in Lesson 6, equation (5.4), exhausts the quotient by these disjoint shells and the compact shell \(r=0\).

For a unitary principal series, its open-chart functions satisfy
\(|\phi(x)|\leq C\max(1,|x|)^{-1}\). Its invariant \(L^2(F)\) form gives the coefficient bound
\[
|\langle\pi(t_r)\phi,\psi\rangle|
\leq C(r+1)q^{-r/2}.
\tag{7.5}
\]
Indeed its absolute integral is bounded by
\[
Cq^{r/2}\int_F
 \frac{dx}{\max(1,q^r|x|)\max(1,|x|)}.
\]
The regions \(|x|\leq q^{-r}\), \(q^{-r}<|x|\leq1\), and \(|x|>1\) contribute respectively
\(O(q^{-r})\), \(O(rq^{-r})\), and \(O(q^{-r})\) before the prefactor. Compact \(K_0\)-orbits of fixed smooth vectors are finite-dimensional, so the same bound, with a changed constant, holds throughout each double coset. Equation (7.4) then gives \(L^{2+\epsilon}\) for every \(\epsilon>0\).

For Steinberg, choose an additive character of conductor \(\mathcal O\) and additive measure of volume one on \(\mathcal O\). The elementary Fourier calculation for a ball gives
\[
Q_m(\phi,\psi)
=q^{-m}\int_{|\xi|\leq q^m}
 \widehat\phi(\xi)\overline{\widehat\psi(\xi)}\,d\xi.
\]
It follows by Fourier orthogonality on finite quotients, then by \(L^2\) approximation; these are the same ball projectors used in Section 1. Summing the geometric series in (7.3) yields
\[
H_{\mathrm{St}}(\phi,\psi)
=\frac{\log q}{1-q^{-1}}
 \int_F\widehat\phi(\xi)\overline{\widehat\psi(\xi)}
                     |\xi|^{-1}\,d\xi.
\]
The value at \(\xi=0\) has measure zero. Every \(\phi\) here is fixed by sufficiently small additive translations, so its Fourier transform is compactly supported. Its zero mean and tail bound also give
\(|\widehat\phi(\xi)|\leq C|\xi|\) near zero: subtract the constant Fourier value and integrate only over \(|x|>|\xi|^{-1}\).
Since \(t_r\) acts in this chart by \(q^r\phi(\varpi^{-r}x)\), it acts on the transform by
\(\widehat\phi(\varpi^r\xi)\). In the compact support of \(\widehat\psi\), the last bound therefore proves
\[
|\langle\pi(t_r)\phi,\psi\rangle|\leq Cq^{-r}.
\]
Finite compact orbits and (7.4) show that these coefficients are in \(L^2(G/Z)\), and hence in every \(L^{2+\epsilon}\) since they are bounded.

A supercuspidal has compactly supported coefficients modulo \(Z\), by Lesson 6, Theorem 5.3. They too are bounded and in every required space. In each unitary family the invariant form identifies all smooth dual functionals with smooth vectors, by fixed-space duality, so these checks cover every smooth matrix coefficient.

**Exclusion of the remaining families.** A unitary determinant character has coefficients of constant absolute value, while (7.4) gives infinite quotient volume. It is not tempered.

For any irreducible principal series with unitary central character, the absolute values of the inducing characters are \(\nu^s\) and \(\nu^{-s}\) for some \(s\geq0\). If \(s=0\), both characters are unitary. If \(s>0\), order them so \(|\mu_1(\varpi)|=q^s\). The smoothed evaluation coefficient used in the necessity proof has absolute value \(cq^{(s-1/2)r}\) on \(t_r\), for all sufficiently large \(r\), with \(c>0\). Choose \(K_m\) fixing both its vector and its smooth functional. It is constant on \(K_mt_rK_m\). The image of this double coset in \(G/Z\) has volume \(c_mq^r\), with \(c_m>0\): in the integral Gauss decomposition of \(K_m\), the intersection with \(t_rK_mt_r^{-1}\) imposes \(r\) additional upper-unipotent digits. The central units of \(K_m\) are already in the intersection and do not change this index. These sets lie in distinct Cartan shells. Its \(p\)-th power integral is therefore bounded below by a positive constant times
\[
\sum_{r\text{ large}}q^{\,r(1+p(s-1/2))}.
\]
For some \(p=2+\epsilon>2\), the exponent is nonnegative, so this diverges. This excludes every principal series with \(s>0\), including the complementary series. The other families with unitary central character were all covered above. \(\square\)

This is the rank-two result of [Tadić's unitary classification, Theorem D and §7.5](https://www.numdam.org/item/10.24033/asens.1510.pdf). Getz–Hahn, Theorem 8.4.5, is the original reference for the tempered classification. The positive forms and coefficient estimates needed in rank two have been proved here.

## 8. Exercises with complete solutions

**Exercise 8.1 — matrix order.** Compute the Kirillov action of \(d(a)n(x)\) and \(n(x)d(a)\), and identify the multiplier for \(\left(\begin{smallmatrix}a&b\\0&d\end{smallmatrix}\right)\).

**Solution 8.1.** For the first product,
\(d(t)d(a)n(x)=n(tax)d(ta)\). Applying the Whittaker functional gives
\[
(\pi(d(a)n(x))\xi)(t)=\psi(tax)\xi(ta).
\]
For the second product, \(d(t)n(x)d(a)=n(tx)d(ta)\), giving
\(\psi(tx)\xi(ta)\). A general upper triangular matrix is
\(dI\,n(b/d)d(a/d)\), so its action is
\(\omega(d)\psi(tb/d)\xi(ta/d)\). Thus a formula with \(\psi(tx)\) attached to \(d(a)n(x)\) has interchanged the two factors. For instance, taking \(a=\varpi\) and an \(x\) with \(\psi(x)\ne\psi(\varpi x)\) distinguishes the two actions at \(t=1\).

**Exercise 8.2 — dimensions and families.** Compute the dimension of the Kirillov quotient by compact functions for each infinite-dimensional irreducible family. Explain what happens for a character.

**Solution 8.2.** Proposition 1.3 identifies the ordinary unipotent differences with the compact functions. Therefore the quotient is \(V_N\), with no square-root twist. A supercuspidal has zero Jacquet module and quotient dimension zero. Exactness applied to
\(0\to\mathrm{St}_\chi\to I(\chi\nu^{1/2},\chi\nu^{-1/2})\to D_\chi\to0\)
subtracts the one-dimensional character Jacquet module from the two-dimensional induced one, giving dimension one for Steinberg. A nonexceptional principal series has the two Bruhat-cell Jacquet factors from Lesson 6 and therefore dimension two. Proposition 6.2 realizes these dimensions as zero germs, one \(\nu\chi\) germ, or two principal germs; at a repeated parameter the valuation term provides the second germ. A character \(D_\chi\) has a one-dimensional Jacquet module, but no Whittaker functional. It has no injective scalar Kirillov model of the type considered here, so the quotient calculation must not be assigned to it.

**Exercise 8.3 — swapped parameters through the Kirillov model.** Prove the isomorphism \(I(\mu_1,\mu_2)\simeq I(\mu_2,\mu_1)\) when irreducible, using its Weyl action on compact functions.

**Solution 8.3.** With \(r=\mu_1/\mu_2\), substitute \(u=ts/v\) in the stable integral (5.2). Both tails consist of zero shell integrals, so the substitution gives
\(J_r(ts)=r(ts)J_{r^{-1}}(ts)\). Multiply this into the first kernel's factor:
\[
\mu_2(t)\mu_1(s)^{-1}r(ts)
 =\mu_1(t)\mu_2(s)^{-1}.
\]
Consequently (5.3) is exactly the swapped kernel. Normalize the two Whittaker functionals so that both compact parts are the same scalar function space; the function spaces themselves do not depend on this scaling. Their upper-triangular actions agree because the central character is \(\mu_1\mu_2\). Their Weyl actions agree on \(V_0\), hence their spaces \(V_0+WV_0\) agree. On \(f_0+Wf_1\), the action of \(W\) is \(Wf_0+\omega(-1)f_1\), so it also agrees on the whole space. Upper-triangular matrices and \(w_0\) generate \(G\). The identity of these two function spaces is therefore the desired \(G\)-isomorphism. This argument proves symmetry of the actual representation, rather than only symmetry of its Jacquet characters.

**Exercise 8.4 — irreducibility without assuming finite length.** Prove the principal-series criterion and Steinberg irreducibility from twisted coinvariants, reciprocity and the known induced Jacquet calculation.

**Solution 8.4.** The open Bruhat cell contributes one twisted coinvariant and the closed cell contributes zero, so the induced twisted fiber has dimension one. A vector with zero Kirillov function is \(N\)-fixed by the finite-Fourier enlargement argument. Such a vector is \(\mathrm{SL}_2(F)\)-fixed. The \(N\)-fixed space injects into the two-dimensional ordinary Jacquet module; if nonzero, it has a character subrepresentation. Reciprocity permits this exactly at ratio \(\nu^{-1}\). At every other ratio the scalar function model is consequently injective.

Any nonzero subrepresentation then has a nonzero twisted fiber, which equals the induced fiber by exactness. Fourier-ball projectors put all compact functions \(V_0\) in that subrepresentation. The quotient of the induction by \(G V_0\) is finite-dimensional and \(N\)-trivial, so if nonzero it has a character quotient. Induced duality and reciprocity permit a character quotient exactly at ratio \(\nu\). Away from both exceptional ratios, \(G V_0=I\), and every nonzero subrepresentation equals \(I\).

At ratio \(\nu\), the constructed Steinberg subrepresentation contains \(V_0\). If \(\mathrm{St}/G V_0\) were nonzero, it would have a character quotient \(D_\eta\). Exact Jacquet modules would require
\((\nu^{1/2},\nu^{-1/2})=(\eta\nu^{-1/2},\eta\nu^{1/2})\), which is impossible on the two independent diagonal coordinates. Thus \(\mathrm{St}=G V_0\), and every nonzero Steinberg subrepresentation equals it. Its quotient in \(I_+\) is trivial, giving the two irreducible factors at ratio \(\nu\); twisting and dualizing give their reverse order at ratio \(\nu^{-1}\). Both ratios are reducible, completing both directions. Finite length has been obtained from these explicit sequences, rather than used as an assumption.

## References

- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf) (1970), §2, Propositions 2.7–2.12 and Theorems 2.13–2.14, for the vector-valued model, Weyl coefficients and uniqueness; §3, Theorem 3.3 and Proposition 3.4, for principal-series classification and symmetry. Its \(w_0\) agrees with (0.1). Its normalized \(B(\mu_1,\mu_2)\) agrees with our \(I(\mu_1,\mu_2)\). Its exceptional infinite-dimensional representation is denoted \(\sigma(\mu_1,\mu_2)\).
- P. Deligne, *Formes modulaires et représentations de GL(2)* (1973), §2.2, especially Théorèmes 2.2.2 and 2.2.4: unique Whittaker functional, compact Kirillov part and its finite codimension.
- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, §§8.3–8.4, especially Theorem 8.4.5 for the tempered classification proved in Section 7; see the [author's text page](https://sites.duke.edu/jgetz/graduate-text/). The complementary-series proof here uses the positive ball-kernel expansion in (7.2).
- M. Tadić, *Classification of unitary representations in irreducible representations of general linear group (non-Archimedean case)*, Ann. Sci. École Norm. Sup. 19 (1986), 335–382, [Theorem D, pp. 338–339, and §7.5, p. 370](https://www.numdam.org/item/10.24033/asens.1510.pdf). Its rank-two unitary consequence is proved here in Theorem 7.1.
- Lesson 5, Theorem 4.1 and Proposition 6.2, for countable Schur and the finite-dimensional determinant classification; Lesson 6, Theorems 3.1 and 4.1, Section 6, for reciprocity, exact induced Jacquet modules, and the two Steinberg sequences. Theorem 4.2 here completes its forward reference to Steinberg irreducibility.
