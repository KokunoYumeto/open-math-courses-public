# Supercuspidal representations from compact induction

*Written by GPT-6.1 Sol (OpenAI), October 2026. Public domain (CC0).*

A finite-group cuspidal representation becomes a local supercuspidal representation by placing it at one integral lattice and translating that lattice through \(\mathrm{GL}_2(F)\). The central question is whether different lattice positions intertwine the original representation. A unipotent subgroup rules out every nontrivial Cartan position. The same calculation bounds fixed-vector spaces, and a conjugate of \(K_1(2)\) produces the newvector. A second construction uses a quadratic norm and its Gaussian Fourier transform; an explicit scalar model proves its irreducibility and factors. A norm-fibre vector and exact finite type counts then identify every odd-residue supercuspidal with one of these quadratic models. An explicit exceptional representation over Q₂ proves that the odd-residue qualification is necessary. Compact coefficients also control the character distribution: a positive double-coset operator becomes nilpotent, proving its vanishing near every noncompact adjoint element.

Let \(F,\mathcal O,\varpi,q\) be as in Lesson 9, with residue field \(k\), and put
\[
G=\mathrm{GL}_2(F),\quad Z=F^\times I,\quad K=\mathrm{GL}_2(\mathcal O),
\quad K(m)=1+\mathfrak p^m M_2(\mathcal O)\quad(m\geq1).
\]
We retain Lesson 8's convention: \(K_1(n)\) has lower-left entry in \(\mathfrak p^n\) and lower-right entry congruent to one modulo \(\mathfrak p^n\).

The finite-group cuspidal representations and their character formulas are supplied by the written finite-field prerequisite, with exact proof locators in Section 9. The compact-induction and conductor proofs need only their vanishing unipotent invariants. The general Mackey argument uses smooth admissibility as recorded in Lesson 5 and proved in Lesson 6, Theorem 5.4. We distinguish arbitrary compact induction from the irreducible compact inductions constructed here.

## 1. Functions, dual pairings, and the support qualification

Let \(J\) be open, contain \(Z\), and be compact modulo \(Z\). Let \(\tau\) be a finite-dimensional irreducible smooth representation of \(J\), with central character \(\omega\), on \(T\). Define
\[
V=\mathrm{c\!-\!Ind}_J^G\tau
 =\{f:G\to T:\ f(jg)=\tau(j)f(g),\
      \operatorname{supp}(f)\text{ is compact in }J\backslash G\}.
\tag{1.1}
\]
Since \(J\) is open, the support condition means finitely many left \(J\)-cosets. The action is \((\pi(g)f)(x)=f(xg)\). Each function is smooth: intersect the conjugates of open stabilizers of its finitely many values, also making this subgroup preserve its finitely many support cosets.

For \(V'=\mathrm{c\!-\!Ind}_J^G\tau^\vee\), there is a nondegenerate invariant pairing
\[
[f,f']=\sum_{x\in J\backslash G}\langle f(x),f'(x)\rangle.
\tag{1.2}
\]
Dual \(J\)-actions make the summands independent of the representatives. The sum is finite, and right translation permutes the cosets. Pairing a nonzero value with a dual value on the same coset proves nondegeneracy.

**Lemma 1.1 — finite-support coefficients.** For \(f\in V,f'\in V'\), the function \(g\mapsto[\pi(g)f,f']\) is compactly supported modulo \(Z\).

**Proof.** Write the supports inside \(\bigcup_i Jx_i\) and \(\bigcup_j Jy_j\). A nonzero summand requires \(y_jg\in Jx_i\), so \(g\in y_j^{-1}Jx_i\). This is a finite union of sets compact modulo \(Z\), since \(J/Z\) is compact and \(Z\) is central. \(\square\)

The finite-support condition on \(f'\) matters. The full smooth dual of an arbitrary compact induction can be larger.

**Counterexample.** For \(J=ZK,\tau=1\), the characteristic functions of the distinct double cosets \(Jd(\varpi^n)K\), \(n\geq0\), belong to \(V^K\) and are linearly independent. Each double coset contains finitely many left \(J\)-cosets: its stabilizer in compact \(K\) is open. Hence this compact induction is not admissible.

Moreover \(\ell(f)=\sum_{x\in J\backslash G}f(x)\) is a \(G\)-invariant linear functional, hence a smooth dual vector. For \(f=1_J\), its coefficient \(\ell(\pi(g)f)\) is identically one. The Cartan positions escape every compact set in \(G/Z\), so this coefficient is not compact modulo \(Z\). The irreducibility condition below lets us identify the entire smooth dual and avoid this defect.

## 2. The algebraic Mackey criterion

Put
\[
H_g=J\cap gJg^{-1},\qquad \tau^g(h)=\tau(g^{-1}hg),\qquad
I_G(\tau)=\{g:\operatorname{Hom}_{H_g}(\tau,\tau^g)\ne0\}.
\tag{2.1}
\]

**Theorem 2.1.** If \(I_G(\tau)=J\), then \(V\) is irreducible. For \(G=\mathrm{GL}_2(F)\), it is admissible, all smooth-dual matrix coefficients are compact modulo \(Z\), and it is supercuspidal.

**Proof of the multiplicity calculation.** Restrict to the right action of \(J\), and partition support by the double cosets \(Jg^{-1}J\). Evaluation along \(g^{-1}J\) gives
\[
V|_J\simeq\bigoplus_{Jg^{-1}J}\operatorname{Ind}_{H_g}^{J}\tau^g.
\tag{2.2}
\]
Indeed \(f(g^{-1}hj)=\tau(g^{-1}hg)f(g^{-1}j)\). The index \([J:H_g]\) is finite: \(H_g\) is open and contains \(Z\), so the discrete quotient is an image of compact \(J/Z\).

Finite-index Frobenius reciprocity follows by evaluation at one. An \(H_g\)-map \(A:T\to T^g\) gives the \(J\)-map \(v\mapsto(j\mapsto A\tau(j)v)\); evaluation is its inverse. Since \(T\) is finite dimensional, a map from \(T\) into a direct sum has only finitely many components. Thus
\[
\operatorname{Hom}_J(\tau,V)
 \simeq\bigoplus_{Jg^{-1}J}\operatorname{Hom}_{H_g}(\tau,\tau^g).
\tag{2.3}
\]
If \(I_G(\tau)=J\), only the identity double coset contributes. Its Hom space has dimension one, and the unique \(\tau\)-isotypic part is
\[
V[J]=\{f:\operatorname{supp}(f)\subset J\}\simeq T.
\tag{2.4}
\]

Here is the projection needed to use this assertion. All the representations have the same scalar action \(\omega\) on \(Z\), so averaging integrands descend to \(J/Z\). First make \(\omega\) unitary by an unramified determinant twist if necessary. Its unit restriction already has finite image, and a real power of \(|\det|\) adjusts its value at \(\varpi I\). The twist affects neither intertwining nor irreducibility. Averaging a Hermitian form over \(J/Z\) makes \(\tau\) unitary. Each finite sum of the finite-dimensional summands (2.2) is then unitary and completely reducible.

Schur orthogonality holds for these common-central-character representations on the quotient: average a map between irreducibles by conjugation. The average is an intertwiner, zero between different irreducibles, and on one irreducible of dimension \(d\) equals \(\operatorname{tr}(A)I/d\). Applying this to matrix units gives the character projection
\[
P_\tau=d\int_{J/Z}\operatorname{tr}\tau(j^{-1})\,\pi(j)\,dj,
\qquad \operatorname{vol}(J/Z)=1.
\tag{2.5}
\]
Central scalar factors cancel, making the integrand representative-independent. On each vector its \(J\)-orbit lies in finitely many summands of (2.2), and the smooth quotient integrand is locally constant. Thus this is a finite algebraic average, projecting onto (2.4).

**Proof of irreducibility.** For a nonzero \(G\)-submodule \(A\), take \(0\ne f\in A\), and translate it so \(f(1)\ne0\). Evaluation at one is \(J\)-equivariant with target \(\tau\), so \((P_\tau f)(1)=f(1)\ne0\). Hence \(A\cap V[J]\ne0\). Irreducibility of \(\tau\) gives all of \(V[J]\), whose translates generate every finite-support function. Therefore \(A=V\).

**Proof of compact coefficients and cuspidality.** Lesson 6, Theorem 5.4, makes the irreducible smooth representation \(V\) admissible. The same intertwining criterion holds for \(\tau^\vee\): dualization reverses the Hom direction on \(H_g\), while complete reducibility on its compact central quotient makes nonzero intertwining symmetric. Thus \(V'\) is irreducible too. Pairing (1.2) gives a nonzero injection \(V'\to V^\vee\); invariance makes its functionals smooth. The admissible contragredient is irreducible by Lesson 5, Theorem 5.2, so this image is the entire smooth dual. Every matrix coefficient is consequently covered by Lemma 1.1. Lesson 6, Theorem 5.2, proves that compact coefficients force the Jacquet module to vanish. This is supercuspidality. \(\square\)

The general proof uses the earlier isolated admissibility theorem. We will also prove admissibility directly for the depth-zero construction.

## 3. Depth zero: extending the finite representation and computing intertwining

Let \(\tau_0\) be an irreducible representation of \(\mathrm{GL}_2(k)\) with no upper-unipotent fixed vectors. The lower unipotent group is conjugate to it and also has no fixed vectors. Inflate \(\tau_0\) to \(K\), and let its central character on \(k^\times\) be \(\omega_0\).

Choose \(A\in\mathbb C^\times\). Extend to \(J=ZK\) by
\[
\widetilde\tau(\varpi^r k)=A^r\tau_0(\bar k),\qquad
\omega(\varpi^r u)=A^r\omega_0(\bar u).
\tag{3.1}
\]
In the first formula \(\varpi^r\) means the scalar matrix \(\varpi^r I\). Its decomposition with \(k\in K\) is unique. Unit scalars already act in the inflated representation, so the second formula gives the compatible central character.

**Theorem 3.1.** The representation
\(\pi=\mathrm{c\!-\!Ind}_{ZK}^{G}\widetilde\tau\)
is irreducible, admissible and supercuspidal.

**Proof of intertwining.** Elementary divisors give
\[
G=\coprod_{n\geq0}Jg_nK,\qquad g_n=d(\varpi^n).
\tag{3.2}
\]
To see this directly, scale a matrix to make its entries integral, move a least-valuation entry to the top-left, and eliminate its row and column by integral elementary operations. The diagonal entries are units times powers of \(\varpi\). Unit factors lie in \(K\); a scalar removes the smaller exponent and a permutation exchanges the two positions. The nonnegative exponent difference is invariant under left and right \(K\) and scalar multiplication, proving uniqueness.

For \(n\geq1\), \(H_{g_n}\) contains \(l(u)\) for every \(u\in\mathcal O\), and
\[
g_n^{-1}l(u)g_n=l(\varpi^n u).
\]
The latter acts trivially in the inflated finite representation. For an intertwiner \(B:\widetilde\tau\to\widetilde\tau^{g_n}\), this gives
\(B\widetilde\tau(l(u))=B\).
Average over \(u\bmod\mathfrak p\). Cuspidality makes the average on the left zero, hence \(B=0\).
Multiplying a double-coset representative on either side by \(J\) does not change existence of intertwining. Therefore \(I_G(\widetilde\tau)=J\), and Theorem 2.1 applies.

**Direct admissibility proof.** A \(K(m)\)-fixed function on \(Jg_n kK(m)\) has value fixed by
\(J\cap g_nK(m)g_n^{-1}\), using normality of \(K(m)\) in \(K\).
For \(n\geq m\), this intersection contains \(l(\mathcal O)\): its preimage is \(l(\varpi^n\mathcal O)\subset K(m)\). Cuspidality makes the value zero. Only \(0\leq n<m\) contribute. Each of these positions has finitely many right \(K(m)\)-cosets modulo \(J\), bounded by \([K:K(m)]\), and each value lies in finite-dimensional \(T\). Thus \(\dim V^{K(m)}<\infty\).
Every compact open subgroup contains some \(K(m)\), so its fixed space is a subspace of this finite-dimensional space. \(\square\)

## 4. The conductor-two vector

**Lemma 4.1.** A nonzero representation \(T\) of \(\mathrm{GL}_2(k)\) with no upper-unipotent invariants has a nonzero fixed vector under
\(D=\{\operatorname{diag}(a,1):a\in k^\times\}\).

**Proof.** Decompose the action of the finite additive upper-unipotent group into character eigenspaces. The trivial character is absent and some nontrivial eigenspace is nonzero. Conjugation by \(D\) acts freely and transitively on nontrivial additive characters. Choose \(0\ne v\) in one eigenspace. The vectors \(\tau(d)v\), \(d\in D\), lie in distinct eigenspaces, so their sum is nonzero. Permutation of the summands makes it \(D\)-fixed. \(\square\)

**Theorem 4.2.** The depth-zero representation of Theorem 3.1 has conductor exactly two.

**Proof.** Lesson 8, Theorem 4.3, gives \(c(\pi)\geq2\) because it is supercuspidal. Put \(g_1=d(\varpi)\). For \(h\in K_1(2)\),
\[
g_1h g_1^{-1}
 =\begin{pmatrix}a&\varpi b\\c/\varpi&d\end{pmatrix},
\qquad c\in\mathfrak p^2,\quad d\equiv1\pmod{\mathfrak p^2}.
\tag{4.1}
\]
The intersection \(H=J\cap g_1K_1(2)g_1^{-1}\) lies in \(K\): its determinant is a unit, and an element \(\varpi^r k\) of \(J\) has determinant valuation \(2r\). Its reduction is exactly \(D\), by (4.1), and every unit \(a\) occurs. Lemma 4.1 gives a nonzero \(v\in T^H\).

Define \(f(jg_1h)=\widetilde\tau(j)v\) on \(Jg_1K_1(2)\), and zero elsewhere. Two expressions differ by an element of \(H\) fixing \(v\), so the function is well-defined. Its support is compact modulo \(J\), it is right \(K_1(2)\)-fixed, and \(f(g_1)=v\ne0\). Hence \(c(\pi)\leq2\), proving equality. \(\square\)

The conductor proof needed only vanishing unipotent invariants. The finite representation's dimension will enter the explicit examples.


## 5. The finite input and a complete example over \(\mathbb F_3\)

Here is the finite representation input, stated rather than reconstructed. For a character
\(\theta:k_2^\times\to\mathbb C^\times\), where \(k_2/k\) is quadratic, suppose \(\theta\ne\theta^q\).
There is an irreducible cuspidal representation \(\tau_\theta\) of \(\mathrm{GL}_2(k)\), of dimension \(q-1\), depending on the unordered pair \(\{\theta,\theta^q\}\). Its central character is \(\theta|_{k^\times}\), and its character is
\[
\begin{array}{c|c}
\text{class}&\operatorname{tr}\tau_\theta\\ \hline
aI&(q-1)\theta(a)\\
a\begin{pmatrix}1&1\\0&1\end{pmatrix}&-\theta(a)\\
\operatorname{diag}(a,b),\ a\ne b&0\\
\text{multiplication by }t\in k_2^\times\setminus k^\times&
 -\theta(t)-\theta(t^q).
\end{array}
\tag{5.1}
\]
The finite-group construction is proved within the programme in Representations of GL₂ over finite fields, Lemma 3.1, equation (13), and Theorem 4.1. Those results give precisely the character values, degree and absence of unipotent invariants used here; Theorem 5.1 gives the complete finite-group classification. The argument applies also in even characteristic. For the general geometric construction, the original references are Deligne–Lusztig (1976): Theorem 4.2 for the character formula, Theorem 7.1 and Corollary 7.2 for the degree and semisimple values, Proposition 7.4 for irreducibility in general position, Theorem 8.3 for cuspidality, and Theorem 9.16 for the regular-unipotent value. For the elliptic torus \(k_2^\times\), \(\tau_\theta=-R_T^\theta\). The degree formula gives
\[
\dim\tau_\theta=\frac{|\mathrm{GL}_2(k)|_{p'}}{|k_2^\times|}
 =\frac{(q-1)^2(q+1)}{q^2-1}=q-1.
\]
The finite construction and its character theorem are the imported input; the local induction in Sections 1–4 is proved here.

**Example 5.1 — \(q=3\).** Take \(k_2=\mathbb F_3[i]\), \(i^2=-1\), and \(\alpha=1+i\). Then
\(\alpha^2=-i,\alpha^4=-1,\alpha^8=1\), so \(\alpha\) generates \(k_2^\times\).
Let \(\zeta=e^{2\pi i/8}\), and define \(\theta_j(\alpha)=\zeta^j\).
Frobenius sends \(j\) to \(3j\bmod8\). The fixed indices are \(0,4\); the regular pairs are
\[
\{1,3\},\quad\{2,6\},\quad\{5,7\}.
\]
They give three cuspidal representations of dimension two, which we denote by \(\tau_1,\tau_2,\tau_5\).

The group has order \((3^2-1)(3^2-3)=48\). Its eight conjugacy classes and the complete three character rows are as follows. Write \(u_a=a\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\), and let \(t_m\) denote multiplication by \(\alpha^m\) on the two-dimensional \(\mathbb F_3\)-space \(k_2\).

| Class | \(I\) | \(-I\) | \(u_1\) | \(u_{-1}\) | \(\operatorname{diag}(1,-1)\) | \(t_1\) | \(t_2\) | \(t_5\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Size | \(1\) | \(1\) | \(8\) | \(8\) | \(12\) | \(6\) | \(6\) | \(6\) |
| \(\tau_1\) | \(2\) | \(-2\) | \(-1\) | \(1\) | \(0\) | \(-i\sqrt2\) | \(0\) | \(i\sqrt2\) |
| \(\tau_2\) | \(2\) | \(2\) | \(-1\) | \(-1\) | \(0\) | \(0\) | \(2\) | \(0\) |
| \(\tau_5\) | \(2\) | \(-2\) | \(-1\) | \(1\) | \(0\) | \(i\sqrt2\) | \(0\) | \(-i\sqrt2\) |

The class sizes follow from centralizers: scalar classes are singletons, a nontrivial Jordan centralizer has order \(q(q-1)=6\), the split centralizer has order \((q-1)^2=4\), and the elliptic centralizer has order \(q^2-1=8\). They sum to 48. The entries follow by substituting the powers of \(\zeta\) in (5.1); for example
\(-(\zeta+\zeta^3)=-i\sqrt2\) and
\(-(\zeta^4+\zeta^{12})=2\).

Each row has norm one. For the first and third this is
\((4+4+8+8+12+12)/48=1\), and for the second it is
\((4+4+8+8+24)/48=1\).
The first and third have inner product
\((4+4+8+8-12-12)/48=0\).
Each odd row has inner product zero with the even row: its two central contributions cancel, its two Jordan contributions cancel, and the elliptic products vanish.
Also
\[
\dim\tau_j^{U_{\mathrm{upper}}}=(2-1-1)/3=0,\qquad
\dim\tau_j^D=(2+0)/2=1.
\]
Thus both finite invariant calculations needed above are visible in the table.

Inflate each \(\tau_j\) to \(\mathrm{GL}_2(\mathbb Z_3)\), choose the scalar action \(A\) of \(3I\), and apply (3.3). Each resulting representation of \(\mathrm{GL}_2(\mathbb Q_3)\) is irreducible supercuspidal, has conductor two, and has central character
\(\omega(3^r u)=A^r\theta_j(\bar u)\).
For \(A=1\), the central character is trivial for \(j=2\) and is the quadratic residue character on units for \(j=1,5\). Theorem 4.2 constructs its nonzero level-two vector from the one-dimensional \(D\)-fixed space. Lesson 9 gives \(L(s,\pi)=1\) and epsilon exponent two; its phase requires the particular Weyl action and is not specified by the conductor alone.

## 6. The quadratic Weil construction with full proofs

Let \(E/F\) be a separable quadratic field extension, with involution \(\sigma\), norm \(N\), trace \(\operatorname{Tr}\), and quadratic norm character \(\eta=\eta_{E/F}\). We work over every nonarchimedean local field, in either characteristic. The norm group
\(F_+=N(E^\times)=\ker\eta\) is open of index two. These assertions are the proved Local reciprocity and norm groups, Proposition 6.2 and Section 5. Only its cyclic norm-index calculation and polynomial proof of openness are needed; no local Langlands correspondence is used. The norm-one group \(E^1\) is compact, since its elements have valuation zero.

For a smooth character \(\theta:E^\times\to\mathbf C^\times\), put
\[
\mathcal S(E,\theta)=
 \{\Phi\in\mathcal S(E):\Phi(xh)=\theta(h)^{-1}\Phi(x),\ h\in E^1\},
\qquad G^+=\{g:\det g\in F_+\}.
\tag{6.1}
\]
We first construct the representation for every \(\theta\), and then prove that the regular case, \(\theta\ne\chi\circ N\), is supercuspidal.

### 6.1. The character Fourier calculation in both characteristics

**Lemma 6.1 — the Tate calculation needed here.** Let \(k\) be any nonarchimedean local field, \(\psi_k\ne1\) an additive character, and \(\alpha:k^\times\to\mathbf C^\times\) a smooth character. With self-dual additive measure and multiplicative measure giving the units volume one, set
\[
Z_k(\phi,\alpha,s)=\int_{k^\times}\phi(x)\alpha(x)|x|_k^s\,d^\times x,
\qquad
\widehat\phi(y)=\int_k\phi(x)\psi_k(xy)\,dx.
\]
Then the full test-function family has
\[
Z_k(\widehat\phi,\alpha^{-1},1-s)
 =\gamma_k(s,\alpha,\psi_k)Z_k(\phi,\alpha,s),
\quad
\gamma_k=\epsilon_k
 \frac{L_k(1-s,\alpha^{-1})}{L_k(s,\alpha)}.
\tag{6.7}
\]
All normalized integrals are Laurent polynomials in \(q_k^{-s}\), and a test attains \(L_k(s,\alpha)\). If the largest triviality ideal of \(\psi_k\) is \(\pi_k^{-\ell}\mathcal O_k\), its self-dual integral-ring mass is \(q_k^{-\ell/2}\). For unitary \(\alpha\), the central value of \(\epsilon_k\) has absolute value one. For a quadratic nontrivial \(\eta\),
\[
\lambda=\epsilon_k(1/2,\eta,\psi_k),\qquad
\lambda^2=\eta(-1),\qquad
\lambda_{\psi_k(c\,\cdot)}=\eta(c)\lambda.
\tag{6.8}
\]

**Proof.** The Fourier assertions reduce to finite additive groups. The annihilator of \(\mathcal O_k\) is \(\pi_k^{-\ell}\mathcal O_k\), since multiplication by any nonzero element scales its annihilator. Orthogonality on the finite quotients of fractional ideals gives
\(\widehat{\mathbf1_A}=\operatorname{vol}(A)\mathbf1_{A^\perp}\);
choosing \(\operatorname{vol}(\mathcal O_k)=q_k^{-\ell/2}\) makes
\(\widehat{\widehat\phi}(x)=\phi(-x)\) on every locally constant compact test. These tests span \(\mathcal S(k)\). The same finite perfect pairings show that every nontrivial additive character is \(\psi_k(c\,\cdot)\): on increasing fractional ideals choose the compatible coefficients \(c\) modulo their annihilators, and completeness supplies their limit.

A test is constant on a sufficiently small ball about zero. Its remaining support is a finite union of unit shells. The small-ball tail vanishes by unit-character orthogonality when \(\alpha\) is ramified; otherwise it is a geometric series. This proves continuation, the Laurent-polynomial assertion after division by \(L_k\), and attainment, using \(\mathbf1_{\mathcal O_k}\) if \(\alpha\) is unramified and \(\alpha^{-1}\mathbf1_{\mathcal O_k^\times}\) otherwise.

For completeness, the proportionality in (6.7) holds for the entire family. Both sides, as functionals of \(\phi\), transform under \(\phi(x)\mapsto\phi(ax)\) by
\(\alpha(a)^{-1}|a|^{-s}\). On \(\mathcal S(k^\times)\) this equivariance determines a functional up to scalar: decompose into cosets of a small open unit group, where translation forces its values to be the character-weighted Haar integral. A difference vanishing on \(\mathcal S(k^\times)\) factors through \(\phi(0)\), because a test with value zero at zero vanishes near zero. That remaining functional has scaling character one. For generic \(s\), our scaling character is not one, so the difference is zero. Rational continuation removes the exceptional \(s\). Fourier change of variables gives the asserted equivariance of the left side; convergence of its zeta integral first holds in a half-plane, followed by the shell continuation just proved.

Here is the exact scalar. If \(a=a(\alpha)\ge1\), choose \(b\) of valuation \(a+\ell\), and write
\[
G(\alpha,\psi_k,b)=
 \sum_{u\in(\mathcal O_k/\mathfrak p_k^a)^\times}
       \alpha(u)^{-1}\psi_k(u/b).
\]
For \(\phi=\alpha^{-1}\mathbf1_{\mathcal O_k^\times}\), translation invariance by \(\mathfrak p_k^a\) bounds its Fourier support by
\(\pi_k^{-a-\ell}\mathcal O_k\). A unit on which \(\alpha\) is nontrivial but whose effect on \(\psi_k(uy)\) is trivial kills every smaller frequency shell. Explicitly, for \(a\ge2\) use a unit in \(1+\mathfrak p_k^{a-1}\) on which \(\alpha\ne1\); for \(a=1\) use orthogonality on all units. Thus only \(y=w/b\), \(w\) a unit, survives, and
\[
\widehat\phi(w/b)=q_k^{-a-\ell/2}\alpha(w)G(\alpha,\psi_k,b).
\]
Its dual zeta integral gives
\[
\epsilon_k(s,\alpha,\psi_k)
 =q_k^{\ell/2}\alpha(b)q_k^{-s(a+\ell)}
       G(\alpha,\psi_k,b)\quad(a\ge1).
\tag{6.9}
\]
In the unramified case, transforming \(\mathbf1_{\mathcal O_k}\) gives instead
\[
\epsilon_k(s,\alpha,\psi_k)
 =\alpha(\pi_k)^\ell q_k^{\ell(1/2-s)}.
\tag{6.10}
\]
These computations also prove the scalar in (6.7).

Finite Fourier inversion, applied twice to the unit-character test, gives
\(G(\alpha,\psi_k,b)G(\alpha^{-1},\psi_k,b)=\alpha(-1)q_k^a\).
For unitary \(\alpha\), conjugation and \(u\mapsto-u\) therefore give
\(|G|=q_k^{a/2}\). Applying (6.7) twice and using Fourier inversion gives
\(\epsilon_k(s,\alpha,\psi_k)
 \epsilon_k(1-s,\alpha^{-1},\psi_k)=\alpha(-1)\).
Finally the change \(\psi_k\mapsto\psi_k(c\,\cdot)\) changes self-dual measure by \(|c|^{1/2}\), and substitution in the dual integral multiplies \(\epsilon_k\) by
\(\alpha(c)|c|^{s-1/2}\). This proves (6.8) and the central absolute value. Every step used fractional ideals, finite-character orthogonality and completeness, so it applies in positive characteristic as well. It is the finite-place Tate proof, with that field scope made explicit. \(\square\)

For \(k=F\) and \(\alpha=\eta\), (6.9)–(6.10) identify \(\lambda\) with the phase
\[
\lambda(E/F,\psi)=
 \eta(b_0)
 \frac{\displaystyle\int_U\eta(u)^{-1}\psi(u/b_0)\,du}
      {\displaystyle\left|\int_U\eta(u)^{-1}\psi(u/b_0)\,du\right|},
\qquad v(b_0)=a(\eta)+\ell.
\tag{6.4}
\]
A positive Haar normalization on \(U\) cancels. If \(E/F\) is unramified and \(\ell=0\), \(\lambda=1\). This proves, rather than leaves open, the phase used below.

### 6.2. The norm Gaussian and the group relations

Put \(Q(x)=N(x)\), \(B(x,y)=\operatorname{Tr}(xy^\sigma)\), and use self-dual measure on \(E\) for \(\psi_E=\psi\circ\operatorname{Tr}\).
Write
\(\mathcal F_B\Phi(x)=\widehat\Phi(x^\sigma)\).
Separability makes \(B\) nondegenerate, also in characteristic two. Since \(\sigma\) preserves measure, \(\mathcal F_B^2\Phi(x)=\Phi(-x)\).

**Lemma 6.2 — exact stable Gaussian.** For \(b\in F^\times\),
\[
I(b)=\int_E^{\mathrm{st}}\psi(bQ(x))\,dx
 =\lambda\,\eta(b)|b|^{-1},
\qquad
\mathcal F_B(\psi(bQ))(y)
 =I(b)\psi(-Q(y)/b).
\tag{6.11}
\]
The second identity is an identity of distributions; the first is the eventually constant integral over expanding fractional ideals.

**Proof.** The norm is proper, since \(|Nx|_F=|x|_E\). Push multiplicative Haar measure on \(E^\times\) through its compact norm-one fibres. Its image is a positive multiple of multiplicative Haar measure on \(F_+\). Converting both measures to additive ones by their absolute-value factors shows that the additive norm pushforward away from zero is
\[
c_0(1+\eta(t))\,dt,\qquad c_0>0.
\]
There is no atom at zero. An expanding ball in \(E\) maps to
\(F_+\cap\mathfrak p_F^{-fR}\), where \(f=f(E/F)\). Hence its Gaussian integral is
\(c_0\int_{\mathfrak p_F^{-fR}}(1+\eta(t))\psi(bt)\,dt\).
For large \(R\) the constant-character term is zero.

The remaining integral is the homogeneous Fourier transform of \(\eta\), at the nonzero point \(b\). Equation (6.7) at \(s=0\) gives its value
\(\gamma_F(0,\eta,\psi)\eta(b)|b|^{-1}\).
One can also obtain this value directly by the unit-shell sum in (6.9)–(6.10): high negative shells vanish by the same unit orthogonality, so the integral stabilizes. On the ramified branch \(\gamma_F(0,\eta,\psi)/\lambda\) is a positive conductor power. On the unramified quadratic branch its additional Euler ratio is
\(2/(1+q^{-1})>0\). Consequently
\(I(b)=c\lambda\eta(b)|b|^{-1}\) with \(c>0\) independent of \(b\).

Complete the square using
\[
bQ(x)+B(x,y)=bQ(x+y/b)-Q(y)/b.
\]
No division by two occurs. Translating a sufficiently large fractional ideal leaves it unchanged, uniformly for \(y\) in a fixed compact set. This proves the distributional Fourier formula. Apply \(\mathcal F_B\) twice to it. Fourier inversion gives
\(I(b)I(-b^{-1})=1\).
Together with \(\lambda^2=\eta(-1)\), our positive-amplitude formula gives \(c^2=1\), hence \(c=1\). This determines the exact amplitude and proves (6.11). \(\square\)

**Theorem 6.3 — the Weil operators.** There is a unique smooth representation of \(\mathrm{SL}_2(F)\) on \(\mathcal S(E)\) with
\[
r(n(b))\Phi(x)=\psi(bN(x))\Phi(x),
\]
\[
r(m(a))\Phi(x)=\eta(a)|a|_F\Phi(ax),\qquad
r(w_0)\Phi(x)=\lambda\widehat\Phi(x^\sigma),
\quad m(a)=\operatorname{diag}(a,a^{-1}).
\tag{6.2}
\]
It preserves (6.1), and extends there to \(G^+\) by
\[
r_\theta(d(Nh))\Phi(x)
 =|h|_E^{1/2}\theta(h)\Phi(xh).
\tag{6.3}
\]
In particular a scalar \(cI\) acts by \(\eta(c)\theta(c)\).

**Proof.** Norm-one covariance is preserved by \(n(b)\) and \(m(a)\). For the Fourier operator substitute \(y=hz\), \(h\in E^1\), in
\(\mathcal F_B\Phi(xh)\); the identity \(B(xh,hz)=B(x,z)\) gives the same covariance \(\theta(h)^{-1}\).

The operators satisfy the upper-triangular relations, including
\(m(a)n(b)m(a)^{-1}=n(a^2b)\).
Fourier scaling gives \(r(w_0)r(m(a))=r(m(a^{-1}))r(w_0)\).
Inversion and (6.8) give \(r(w_0)^2=r(m(-1))\).
For \(b\ne0\) the remaining Bruhat relation is
\[
w_0n(b)w_0=n(-b^{-1})m(-b^{-1})w_0n(-b^{-1}).
\tag{6.12}
\]
The left operator's kernel, by (6.11), is
\[
\lambda^3\eta(b)|b|^{-1}
 \psi\bigl(-(Q(x)+Q(y)+B(x,y))/b\bigr).
\]
The right kernel has the same phase and coefficient
\(\lambda\eta(-b^{-1})|b|^{-1}\).
They agree because \(\lambda^2=\eta(-1)\).
The Gaussian calculation is applied to compact tests, so its distributional interpretation justifies this kernel multiplication.

These relations are a presentation of \(\mathrm{SL}_2(F)\). To see that no additional relation is needed, write a matrix with lower-left entry zero in the upper-triangular cell; a matrix with lower-left entry nonzero has a unique expression
\(n(x)m(a)w_0n(y)\).
Multiplication by \(n(b)\) or \(m(a)\) reduces using the triangular relations and Fourier-scaling relation. Multiplication by \(w_0\) either uses \(w_0^2=m(-1)\), or reduces through (6.12). Thus every word reduces to the unique matrix coordinates in one of these cells. This proves existence and uniqueness.

The operators \(D_h\) in (6.3) multiply as \(D_hD_{h'}=D_{hh'}\). Replacing \(h\) by \(hz\), \(z\in E^1\), has no effect by the covariance. They conjugate \(r(n(b))\) to \(r(n(Nh\,b))\) and commute with \(r(m(a))\). Change variables in Fourier transformation to obtain
\[
D_h r(w_0)D_h^{-1}\Phi(x)
 =|Nh|_F\lambda\mathcal F_B\Phi((Nh)x)
 =r(m(Nh))r(w_0)\Phi(x).
\]
Here \(\eta(Nh)=1\). These are precisely conjugation by \(d(Nh)\) in the group. Since
\(G^+=\mathrm{SL}_2(F)\rtimes d(F_+)\), the extension is a representation.

We also verify smoothness. A sufficiently small upper-unipotent group fixes a compact test because its norms are bounded. A sufficiently small diagonal group fixes it by local constancy, as well as fixing \(\eta\). Applying the same upper-unipotent assertion to \(r(w_0)^{-1}\Phi\) gives a small lower-unipotent fixing group. Gaussian elimination near the identity then gives an open fixing subgroup in \(\mathrm{SL}_2(F)\). For (6.3), choose \(h\) in a sufficiently small unit group fixing \(\theta\) and every value of \(\Phi\). Its norms contain a neighborhood of one: the norm-polynomial contraction proof in the norm-group prerequisite, with its radius made smaller, gives this for any prescribed neighborhood of one in \(E^\times\). Thus the extension is smooth on \(G^+\).

Finally \(cI=m(c^{-1})d(c^2)\). Take \(h=c\) in (6.3), and apply \(m(c^{-1})\); its scalar factors reduce to \(\eta(c)\theta(c)\), and its arguments reduce to \(x\). This proves the central character. If \(\theta\) is unitary, all operators are unitary for the \(L^2(E)\) norm on this subspace: the scaling Jacobians cancel the displayed absolute-value factors, the phases have modulus one, and Fourier inversion gives the Fourier isometry. \(\square\)

### 6.3. Irreducibility, supercuspidality and the norm-factor case

**Theorem 6.4 — the scalar model and its classification.** If \(\theta\ne\chi\circ N\), \(r_\theta\) on (6.1) is irreducible and
\(\pi(\theta)=\operatorname{Ind}_{G^+}^G r_\theta\) is irreducible, admissible and supercuspidal. If \(\theta=\chi\circ N\), the same induction is the irreducible principal series \(I(\chi,\chi\eta)\).

**Proof.** First, \(\theta|_{E^1}=1\) if and only if \(\theta=\chi\circ N\). In that case it descends to a smooth character of the open subgroup \(F_+\). It extends to \(F^\times\): choose \(c\notin F_+\), choose a square root of its prescribed value at \(c^2\), and use it as \(\chi(c)\). Conversely a norm-factor character is trivial on \(E^1\). Openness of the norm map makes the descended character smooth; the small-unit norm calculation in Theorem 6.3 proves this directly.

In the regular case \(\Phi(0)=0\), since covariance by an element with \(\theta(h)\ne1\) forces this value to vanish. Local constancy makes \(\Phi\) vanish near zero. The map
\[
\Phi\longmapsto\xi_\Phi,\qquad
\xi_\Phi(Nh)=|Nh|_F^{1/2}\theta(h)\Phi(h)
\tag{6.13}
\]
is therefore a bijection with \(C_c^\infty(F_+)\). Independence of \(h\) is covariance; the inverse uses the same formula solved for \(\Phi(h)\). Properness of the norm gives compact support of that inverse. Its local constancy follows from the norm map's small-unit openness and smoothness of \(\theta\). The upper mirabolic action becomes
\[
n(b)\xi(t)=\psi(bt)\xi(t),\qquad d(a)\xi(t)=\xi(at),
\quad a\in F_+.
\tag{6.14}
\]

Here is the algebraic irreducibility of this action. From a nonzero function choose a small additive ball about a nonzero point on which it is a nonzero constant, contained in \(F_+\). Averaging \(n(b)\) against \(\psi(-bt_0)\) on a suitable compact additive group projects onto that ball, by finite-character orthogonality, and produces its indicator. Such an average is a finite sum on the given smooth vector, so it preserves every algebraic invariant subspace. The same projections give indicators of arbitrarily smaller balls. Dilation by \(F_+\) moves their centres to any desired point of \(F_+\); sufficiently small ball indicators span all compact locally constant functions, with larger balls obtained by finite partitions. Thus every nonzero invariant subspace is all of \(C_c^\infty(F_+)\). In particular \(r_\theta\) is irreducible.

Since \(G^+\) has index two, induction is two copies of this space. Evaluation at one defines a Whittaker functional
\(\Lambda(f)=f(1)(1)\), with \(\Lambda(\pi(n(b))f)=\psi(b)\Lambda(f)\).
Its scalar realization \(\xi_f(t)=\Lambda(\pi(d(t))f)\) is
\(C_c^\infty(F^\times)\): the two copies occupy \(F_+\) and \(cF_+\), respectively. The same projection-and-dilation proof, now with \(a\in F^\times\), proves irreducibility of \(\pi(\theta)\) already on the full mirabolic group.

Its ordinary \(N\)-coinvariants vanish. For a compactly supported function on \(F^\times\), partition its support into finitely many small balls on each of which some \(\psi(bt)-1\) is nonzero and constant. Divide the function there by that constant. This expresses the function as a sum of \((\pi(n(b))-1)\)-images. Hence its Jacquet module is zero, so it is supercuspidal by Lesson 6. The independently proved smooth admissibility theorem there, Theorem 5.4, now applies; it did not use the present construction or exhaustion.

For the norm-factor case (6.13) instead has image
\[
V_+=C_c^\infty(F_+)
 +\mathbf C\,\chi(t)|t|^{1/2}\mathbf1_{\{|t|\le q^{-M}\}\cap F_+},
\]
where changing a sufficiently large \(M\) changes the displayed tail by a compact function. There is one germ at zero, namely \(\Phi(0)\). The induced scalar model has \(C_c^\infty(F^\times)\) and two such germs, one on each norm coset. No nonzero function in this model is fixed by all \(N\): for every nonzero \(t\), some \(\psi(bt)\ne1\). Every \(N\)-difference is compactly supported away from zero. Consequently a nonzero \(G\)-submodule contains a nonzero compact function and, by (6.14), all \(C_c^\infty(F^\times)\).

It also contains both germs. Choose a nonnegative, nonzero, compact shell test \(\Phi\in\mathcal S(E,\chi\circ N)\) that is invariant under \(E^1\). Its Fourier value at zero is \(\int_E\Phi\ne0\), so \(r(w_0)\Phi(0)=\lambda\int_E\Phi\ne0\). Starting in the identity component, this supplies its germ; translating by \(d(c)\) supplies the other germ. Thus the induction is irreducible in this case too. The same compact-part argument and the one nonzero Fourier germ show that the representation on \(V_+\) itself is irreducible.

The Jacquet quotient is precisely the two-germ quotient, since the compact part has zero coinvariants by the preceding ball argument. Diagonal dilation acts on its unnormalized germs by
\(\chi(a)|a|^{1/2}\) and \(\chi(a)\eta(a)|a|^{1/2}\). To check the characters even when \(a\notin F_+\), dilation interchanges the two norm cosets; a tail can be written as
\(\chi(t)|t|^{1/2}(A+B\eta(t))\), which gives these two eigencharacters. With the central character
\(\chi(c)^2\eta(c)\), the normalized full torus characters are
\(\chi\boxtimes\chi\eta\) and its exchange. The Jacquet adjunction proved in Lesson 6 therefore embeds our irreducible representation into \(I(\chi,\chi\eta)\).
That principal series is irreducible: its character ratio is the nontrivial quadratic \(\eta\), which is neither \(|\cdot|\) nor \(|\cdot|^{-1}\). The embedding is consequently an isomorphism. This proves the norm-factor assertion as well. \(\square\)

### 6.4. Auxiliary choices, symmetries and the full factor identity

**Theorem 6.5 — all quadratic properties and factors.** In the regular case \(\pi(\theta)\) is independent up to isomorphism of \(\psi\), and
\[
\pi(\theta^\sigma)\simeq\pi(\theta),\qquad
\pi(\theta)^\vee\simeq\pi(\theta^{-1}),\qquad
\pi(\theta)\otimes\chi\simeq\pi(\theta(\chi\circ N)),
\tag{6.5}
\]
\[
\omega_{\pi(\theta)}=\theta|_{F^\times}\eta,\qquad
L(s,\pi(\theta))=L_E(s,\theta)=1,
\]
\[
\epsilon(s,\pi(\theta),\psi)
 =\lambda(E/F,\psi)\epsilon_E(s,\theta,\psi\circ\operatorname{Tr}).
\tag{6.6}
\]
For a norm-factor character the same identity holds with
\(L(s,\pi)=L_E(s,\theta)=L_F(s,\chi)L_F(s,\chi\eta)\).
In every case the factor identity holds for the full zeta-integral family, with the actual conductor of the trace character on \(E\).

**Proof.** Every additive choice is \(\psi_c=\psi(c\,\cdot)\), as in Lemma 6.1.
Its self-dual measure on \(E\) is \(|c|_F\) times the old one, because \(E\) has dimension two over \(F\). Thus
\(\mathcal F_{B,\psi_c}\Phi(x)=|c|_F\mathcal F_{B,\psi}\Phi(cx)\).
Combining this with \(\lambda_{\psi_c}=\eta(c)\lambda_\psi\) shows on \(n(b),m(a),w_0\), and \(d(F_+)\), that
\[
r_{\theta,\psi_c}(g)
 =r_{\theta,\psi}(d(c)g\,d(c)^{-1}).
\]
For \(w_0\) use \(d(c)w_0d(c)^{-1}=m(c)w_0\).
Conjugating an induced representation by a group element gives an isomorphic \(G\)-representation, via translation of its induced functions. Hence the induced representation is independent of \(\psi\).

The map \(\Phi(x)\mapsto\Phi(x^\sigma)\) intertwines the \(\theta\) and \(\theta^\sigma\) spaces and all their operators; in (6.3) use \(h^\sigma\), which has the same norm. Twisting by \(\chi(\det g)\) changes (6.3) exactly to the operator for \(\theta(\chi\circ N)\), and changes none of the determinant-one operators. This proves symmetry and twisting. Lesson 9 proves for every irreducible infinite-dimensional \(G\)-representation that
\(\pi^\vee\simeq\omega_\pi^{-1}\otimes\pi\).
For \(h\in E^\times\),
\[
\omega_\pi(Nh)=\theta(h)\theta(h^\sigma),
\]
since \(\eta(Nh)=1\). Therefore the twist replaces \(\theta\) by
\((\theta^\sigma)^{-1}\); symmetry proves the dual assertion. The central character was computed directly in Theorem 6.3.

We now calculate the complete functional equation. Write
\[
M_s(\xi)=\int_{F^\times}\xi(t)|t|^{s-1/2}\,d^\times t,
\quad
D_s(\xi)=\int_{F^\times}(\pi(w_0)\xi)(t)
                  \omega_\pi(t)^{-1}|t|^{1/2-s}\,d^\times t.
\tag{6.15}
\]
These are the zeta and dual-zeta functionals used in Lesson 9. Normalize multiplicative measures on both unit groups to volume one. Norm pushforward is
\(N_*d^\times h=\kappa\,\mathbf1_{F_+}\,d^\times t\), \(\kappa>0\).
For a vector from the identity component (6.13), substitution gives exactly
\[
M_s(\xi_\Phi)=\kappa^{-1}Z_E(\Phi,\theta,s),\qquad
D_s(\xi_\Phi)=\lambda\kappa^{-1}
                   Z_E(\widehat\Phi,\theta^{-1},1-s).
\tag{6.16}
\]
For the second equation start with
\((\pi(w_0)\xi_\Phi)(Nh)=|Nh|^{1/2}\theta(h)\lambda\widehat\Phi(h^\sigma)\).
Then use \(\omega_\pi(Nh)=\theta(h)\theta(h^\sigma)\), and substitute \(h^\sigma\) in the remaining integral. Both additive and multiplicative measures are invariant under \(\sigma\). No discriminant factor or unspecified Haar scalar remains; \(\kappa\) is the same on both sides.

Lemma 6.1 on \(E\) yields
\(D_s(\xi_\Phi)=\lambda\gamma_E(s,\theta,\psi_E)M_s(\xi_\Phi)\).
This equation holds for the other norm component as well. Indeed if \(T_c=\pi(d(c))\), then
\[
M_s(T_c\xi)=|c|^{1/2-s}M_s(\xi),\qquad
D_s(T_c\xi)=|c|^{1/2-s}D_s(\xi).
\]
The second equality follows from
\(\pi(w_0)T_c=\omega_\pi(c)T_{c^{-1}}\pi(w_0)\), followed by \(t=cu\) in (6.15).
The two components span the whole induced model. Thus this is an all-vector functional equation, and its scalar is the unique factor in Lesson 9:
\[
\gamma_F(s,\pi(\theta),\psi)=
 \lambda\,\gamma_E(s,\theta,\psi_E).
\tag{6.17}
\]

The ideal also agrees, not just the scalar. Lemma 6.1 shows that (6.16), divided by \(L_E(s,\theta)\), is always a Laurent polynomial and some \(\Phi\) attains the entire Euler factor. The attaining tests may be chosen in \(\mathcal S(E,\theta)\): use \(\mathbf1_{\mathcal O_E}\) when \(\theta\) is unramified, and
\(\theta^{-1}\mathbf1_{\mathcal O_E^\times}\) when it is ramified. The other component contributes only the invertible monomial \(|c|^{1/2-s}\). This proves equality of the full zeta ideals, hence \(L_F(s,\pi)=L_E(s,\theta)\), and the same argument with \(\theta^{-1}\) proves the dual equality. Comparing (6.17) with (6.7) proves (6.6).

In the regular case \(\theta\) is ramified: \(E^1\subset\mathcal O_E^\times\), and \(\theta|_{E^1}\ne1\). Thus both character Euler factors are one, consistently with supercuspidality.

Finally, the norm-factor Euler identity can be checked without a reciprocity-factor theorem. If \(E/F\) is unramified, norms on units are surjective, \(q_E=q_F^2\), and \(\eta(\pi_F)=-1\). A ramified \(\chi\) gives three trivial Euler factors; an unramified \(\chi\) gives
\[
(1-\chi(\pi_F)^2q_F^{-2s})^{-1}
 =\bigl((1-\chi(\pi_F)q_F^{-s})
        (1+\chi(\pi_F)q_F^{-s})\bigr)^{-1}.
\]
If \(E/F\) is ramified, \(q_E=q_F\) and norm units have index two in the \(F\)-units. The character \(\chi\circ N\) is unramified precisely when \(\chi|_U\) is \(1\) or \(\eta|_U\), so precisely one of \(\chi,\chi\eta\) is unramified. Its uniformizer value equals \(\theta(\pi_E)\), since \(N\pi_E\) has valuation one and \(\eta(N\pi_E)=1\). Otherwise all three Euler factors are one. This proves the claimed product in every ramification case and completes the theorem. \(\square\)

Jacquet–Langlands, Lemma 1.2(iv) and Propositions 1.3/1.5, give the historical Weil constants and operators. Their Theorem 4.6(i)–(iv) gives the regular and norm-factor classification, and Theorem 4.7(i)–(iii) gives the symmetries, central character and factors. Sections 6.1–6.4 supply full proofs of those quadratic-extension assertions. In particular their factor assertion is item (iii), and its additive conductor is the conductor of \(\psi\circ\operatorname{Tr}\), which need not be \(\mathcal O_E\). Compact-induction exhaustion is a separate assertion in Section 7.


### 6.5. Distinguishing the quadratic models without a correspondence theorem

**Lemma 6.6 — injectivity for a fixed quadratic field.** For a fixed separable quadratic extension \(E/F\), two regular characters give isomorphic models precisely when
\[
\{\theta_1,\theta_1^\sigma\}=\{\theta_2,\theta_2^\sigma\}.
\tag{6.18}
\]

**Proof.** Theorem 6.5 gives the sufficiency. For the converse, realize both representations in the scalar Kirillov space \(C_c^\infty(F^\times)\) of Theorem 6.4. Their upper mirabolic actions are identical. Every linear map commuting with those actions is scalar, with no continuity assumption needed. Indeed, evaluation at \(t\), composed with such a map, is an upper-unipotent eigenfunctional of character \(b\mapsto\psi(bt)\). Averaging over sufficiently large compact additive groups projects a test to an arbitrarily small ball about \(t\). A test vanishing near \(t\) is killed by one such projection; on a sufficiently small ball a locally constant test is its value at \(t\) times the indicator. The eigenfunctional is therefore a multiple of evaluation. Commutation with all multiplicative dilations makes that multiple independent of \(t\).

An isomorphism thus identifies the two Weyl operators in this common space. Their central characters also agree, so \(\theta_1(c)=\theta_2(c)\) for \(c\in F^\times\), by Theorem 6.5. On the norm component, take a test \(\xi\in C_c^\infty(F_+)\). Its quadratic-plane representative is
\[
\Phi_i(y)=\theta_i(y)^{-1}|Ny|^{-1/2}\xi(Ny).
\]
The value of the Weyl operator at one, using (6.2), is
\[
\lambda\int_E\theta_i(y)^{-1}|Ny|^{-1/2}
                  \xi(Ny)\psi(\operatorname{Tr}y)\,dy.
\tag{6.19}
\]
The integral is supported on a compact set away from zero. Equality for the two models gives equality of (6.19) for all \(\xi\). Substitute \(y=cu\), and replace the test by \(t\mapsto\xi(t/c^2)\). The resulting common scalar is
\(|c|_F\theta_i(c)^{-1}\), so it cancels. We obtain equality with \(\psi(c\operatorname{Tr}u)\) in place of \(\psi(\operatorname{Tr}u)\), for every \(c\ne0\). It also holds at \(c=0\), because a sufficiently small \(c\) makes that phase one on the compact support.

Fourier uniqueness for compactly supported measures on the additive group of \(F\) now gives equality after replacing that phase by any compact locally constant trace test. Here Fourier uniqueness is elementary: a compactly supported locally constant test factors through a finite additive quotient, on which additive characters form a basis. Products of trace tests and norm tests give all compact locally constant tests on the image of \(y\mapsto(\operatorname{Tr}y,Ny)\), by finite partitions into rectangles.

Away from \(F\subset E\), the trace-norm map has two local branches, \(y\) and \(y^\sigma\). Its derivative has nonzero determinant \(y-y^\sigma\); the elementary nonarchimedean inverse-function argument, obtained by shrinking balls until the linear term dominates the quadratic term, identifies each branch with a ball in \(F^2\). The two Haar Jacobians are equal, since \(\sigma\) preserves additive Haar measure. The other weight in (6.19) depends only on the norm. Consequently equality of the pushed-forward measures gives
\[
\theta_1(y)^{-1}+\theta_1(y^\sigma)^{-1}
 =\theta_2(y)^{-1}+\theta_2(y^\sigma)^{-1}.
\tag{6.20}
\]
It holds pointwise by local constancy. On \(F^\times\) the same equality follows from the already equal central restrictions. Distinct characters of a group are linearly independent: in a shortest nontrivial linear relation, translate by an element on which two characters differ and subtract an appropriate scalar multiple of the original relation, obtaining a shorter one. Apply this to (6.20). It proves (6.18). No parameter correspondence has entered the proof. \(\square\)

## 7. Exhaustion and the support of a character

### 7.1. Why every supercuspidal is compactly induced

The problem is to find a finite-dimensional compact block whose translates cannot overlap in the wrong places. We will find that block inside the given representation, using its compact coefficients and four-entry matrix calculations. No parametrization by Weil representations is needed. Throughout this subsection the local field can have either characteristic, and its residue characteristic can be two.

Choose an auxiliary additive character \(\psi_*\) trivial on \(\mathfrak p\) and nontrivial on \(\mathcal O\). It will only label compact characters. Put
\[
\begin{aligned}
\mathfrak M&=M_2(\mathcal O),&\mathfrak P_{\mathfrak M}&=\varpi M_2(\mathcal O),\\
\mathfrak I&=\begin{pmatrix}\mathcal O&\mathcal O\\\mathfrak p&\mathcal O\end{pmatrix},&
\mathfrak P_{\mathfrak I}&=\begin{pmatrix}\mathfrak p&\mathcal O\\\mathfrak p&\mathfrak p\end{pmatrix}.
\end{aligned}
\tag{7.4}
\]
For either order, and for its conjugates, write \(U_{\mathfrak A}=\mathfrak A^\times\) and \(U_{\mathfrak A}^j=1+\mathfrak P^j\), \(j\geq1\). The periods are \(e_{\mathfrak M}=1\) and \(e_{\mathfrak I}=2\). Indeed, with
\(\Pi=\left(\begin{smallmatrix}0&1\\\varpi&0\end{smallmatrix}\right)\), one has \(\mathfrak P_{\mathfrak I}=\Pi\mathfrak I=\mathfrak I\Pi\) and \(\Pi^2=\varpi I\).

Here is the lattice meaning of these matrices. The first order preserves all \(\varpi^a\mathcal O^2\); the second also preserves \(\varpi^a(\mathcal O\oplus\mathfrak p)\). Conversely these are their full chains of stable lattices, up to a common change of basis. To check this, use the two diagonal idempotents to write a stable lattice as \(\mathfrak p^a\oplus\mathfrak p^b\). The two off-diagonal entries impose \(a=b\) for \(\mathfrak M\), and \(a\leq b\leq a+1\) for \(\mathfrak I\). A strict periodic lattice chain in a two-dimensional space has no other form: its intermediate lattices give a strict flag in the two-dimensional residue space. Thus these two explicit orders describe both possible chains.

We will repeatedly use the following trace pairing, including its shift by one:
\[
 (\mathfrak P^j)^\perp=\mathfrak P^{1-j},
 \qquad L^\perp=\{y:\psi_*(\operatorname{tr}(xy))=1\text{ for every }x\in L\}.
\tag{7.5}
\]
For the maximal order it follows by pairing each matrix entry with its transposed entry. For the other order use
\(\mathfrak P^{2a}=\varpi^a\mathfrak I\) and
\(\mathfrak P^{2a+1}=\varpi^a\mathfrak P_{\mathfrak I}\): the diagonal entries pair with diagonal entries and the upper-right with the lower-left. This checks both parities, also for negative powers. Consequently, if \(2r\geq n+1\) and \(1\leq r\leq n\), all characters of \(U_{\mathfrak A}^r/U_{\mathfrak A}^{n+1}\) are
\[
 \theta_\alpha(1+x)=\psi_*(\operatorname{tr}(\alpha x)),
 \qquad \alpha\in\mathfrak P^{-n}/\mathfrak P^{1-r}.
\tag{7.6}
\]
The inequality makes the product term \(xy\) invisible to the pairing; (7.5) proves both exhaustion and the asserted ambiguity. Admissibility from Lesson 6 makes every character space occurring below finite dimensional: its compact open kernel fixes that entire space.

We first exclude the two ways a compact block could still see a split direction.

**Lemma 7.4 — the Iwahori obstruction.** A supercuspidal representation has no nonzero vector fixed by \(U_{\mathfrak I}^1\).

**Proof.** Set \(I=U_{\mathfrak I}\). If such a vector exists, the finite abelian quotient \(I/U_{\mathfrak I}^1=k^\times\times k^\times\) gives a nonzero character space \(V^\phi\), where \(\phi=\phi_1\otimes\phi_2\). Denote its averaging projector by \(E_\phi\). Let
\[
 s=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 j=\begin{pmatrix}0&1\\\varpi&0\end{pmatrix},\qquad
 t=sj=\operatorname{diag}(\varpi,1).
\]
The operator \(A_\phi=E_{\phi^w}\pi(s)E_\phi\) exchanges the two character spaces. In the finite \(K/K(1)\)-module it satisfies
\[
\begin{cases}
 A_{\phi^w}A_\phi=q^{-1}1,&\phi_1\ne\phi_2,\\
 A_\phi^2=q^{-1}1+\phi_1(-1)(1-q^{-1})A_\phi,&\phi_1=\phi_2.
\end{cases}
\tag{7.7}
\]
Here is the calculation. On a Borel-character vector, averaging \(\pi(s)\) over the Borel is \(q^{-1}\sum_{x\in k}\pi(n(x)s)\). Multiply the two averages. The zero lower-root parameter gives \(q^{-1}1\). For a nonzero lower parameter \(y\), use the matrix identity
\[
 n(x)l(y)=n(x+y^{-1})
       \operatorname{diag}(-y^{-1},y)s n(y^{-1}).
\]
The remaining coefficient is the sum of \(\phi_2(-1)(\phi_1\phi_2^{-1})(y)\) over \(k^\times\), divided by the averaging factors. That sum is zero for unequal characters and \(\phi_1(-1)(q-1)\) for equal characters, giving (7.7). Thus each \(A_\phi\) is invertible: use \(qA_{\phi^w}\) in the first case and \(qA_\phi-\phi_1(-1)(q-1)1\) in the second.

Since \(j\) normalizes \(I\) and exchanges the two diagonal characters, the operator
\(T=E_\phi\pi(t)E_\phi=A_{\phi^w}\pi(j)|_{V^\phi}\) is invertible. On the other hand, the upper-root representatives for \(It^aI/I\) are \(n(x)t^a\), \(x\in\mathcal O/\mathfrak p^a\). Multiplying these representatives appends one base-\(\varpi\) digit, so normalized averaging gives
\[
 T^a=E_\phi\pi(t^a)E_\phi\qquad(a\geq1).
\tag{7.8}
\]
The characters contribute no extra factor: they are trivial on these root groups and agree on the conjugated diagonal intersection. By Lesson 6 all the finitely many matrix coefficients defining this operator on \(V^\phi\) have compact support modulo the centre. The class of \(t^a\) leaves every such compact set. Hence (7.8) is zero for sufficiently large \(a\), contradicting invertibility. \(\square\)

**Lemma 7.5 — a split compact character cannot occur.** Suppose \(n\geq1\), \(a,b\in\mathcal O\), and \(a-b\in\mathcal O^\times\). No supercuspidal contains the character of \(K(n)\) given by \(\alpha=\varpi^{-n}\operatorname{diag}(a,b)\) in (7.6).

**Proof.** Suppose its character space \(W\) is nonzero. Put \(N_i=n(\mathfrak p^i)\). The vanishing Jacquet module and Lesson 6's averaging criterion give \(E_{N_i}W=0\) for some \(i\), by choosing one averaging group for a basis of \(W\). Such vanishing persists as \(i\) decreases. It fails for \(i=n\), since \(N_n\) fixes \(W\). There is therefore a largest \(i\) with vanishing. Choose \(v\in W\) with \(E_{N_{i+1}}v\ne0\), and put \(v'=\pi(t^{-1})v\), where \(t=\operatorname{diag}(\varpi,1)\). Then \(E_{N_i}v'\ne0\).

The vector \(v'\) has the same diagonal character on
\[
 Y=K(n)\cap t^{-1}K(n)t
   =1+\begin{pmatrix}\mathfrak p^n&\mathfrak p^n\\
                     \mathfrak p^{n+1}&\mathfrak p^n\end{pmatrix}.
\]
In particular \(K(n+1)\) fixes it. Decompose its finite \(K(n)/K(n+1)\)-span into characters. Pairing the four entries shows that every character extending the one on \(Y\) has parameter
\(\varpi^{-n}\left(\begin{smallmatrix}a&c\\0&b\end{smallmatrix}\right)\) modulo \(\mathfrak p^{1-n}\mathfrak M\). Conjugation by an upper unit \(n(z)\), \(z\in\mathcal O\), removes \(c\), because \(a-b\) is a unit. Some component still has nonzero \(N_i\)-average. Carrying that component back by this upper unit puts it in \(W\); upper-root translations commute with the averaging operator. This contradicts \(E_{N_i}W=0\). \(\square\)

Next select a compact character without presupposing any list of inducing types. For a smooth representation set
\[
 \ell(\pi)=\min\left\{n/e_{\mathfrak A}:n\geq0,
       \ V^{U_{\mathfrak A}^{n+1}}\ne0\right\},
\tag{7.9}
\]
where both chains and all their conjugates are allowed. Smoothness makes the set nonempty; its values belong to \(\tfrac12\mathbb Z_{\geq0}\), so a minimum is attained. Choose a determinant twist with the least possible level. Twisting preserves vanishing of the Jacquet module and compactness of coefficients modulo the centre.

**Lemma 7.6 — the elliptic alternative.** This least-level twist either contains an inflated finite cuspidal \(K\)-type, or contains a first-layer character with one of these parameters:

- \(\mathfrak A=\mathfrak M\), \(n\geq1\), and \(\varpi^n\alpha\) has irreducible quadratic reduction;
- \(\mathfrak A=\mathfrak I\), \(n=2m+1\), and \(\alpha\mathfrak I=\mathfrak P^{-n}\).

In both positive-level cases every parameter in \(\alpha+\mathfrak P^{1-n}\) generates a quadratic field whose full integral lattice chain is the chosen chain.

**Proof.** At level zero either chain gives a \(K(1)\)-fixed vector, because \(K(1)\subset U_{\mathfrak I}^1\). Take a finite irreducible \(K/K(1)\)-constituent. Upper-unipotent invariants in it would give \(U_{\mathfrak I}^1\)-invariants, contrary to Lemma 7.4. Thus it is finite cuspidal.

At a positive integral level \(n\), a maximal-order vector is available even if the minimizing chain had period two: \(K(n+1)\subset U_{\mathfrak I}^{2n+1}\). Its characters on \(K(n)/K(n+1)\) correspond to matrices \(\bar A\in M_2(k)\). Zero lowers the level. A nonzero nilpotent can be put in strictly upper triangular form; its character is trivial on \(1+\varpi^n\mathfrak I\), giving level \(n-\tfrac12\), again impossible. If \(\bar A\) has a repeated eigenvalue \(c\), subtract \(cI\) by a determinant twist. Explicitly extend the character
\(1+x\mapsto\psi_*(-c\varpi^{-n}x)\) of \((1+\mathfrak p^n)/(1+\mathfrak p^{n+1})\) to \(F^\times\). For clarity, characters of a subgroup of a finite abelian group extend by adjoining one element at a time: if its coset has order \(d\), choose a \(d\)-th root of the prescribed value on its \(d\)-th power. The resulting character is well defined on the enlarged subgroup. Apply this to \(\mathcal O^\times/(1+\mathfrak p^{n+1})\), then extend to \(F^\times=\varpi^{\mathbb Z}\mathcal O^\times\). Since \(\det(1+X)\equiv1+\operatorname{tr}X\pmod{\mathfrak p^{n+1}}\), this produces the already excluded nilpotent case at a lower level of a twist. Distinct residue eigenvalues are excluded by Lemma 7.5. The remaining quadratic reduction is irreducible.

At level \(m+\tfrac12\), the first character of the period-two chain can be represented by
\[
 \alpha=\begin{pmatrix}0&\varpi^{-m-1}u\\
                         \varpi^{-m}v&0\end{pmatrix},
 \qquad u,v\in\mathcal O\pmod{\mathfrak p}.
\]
If \(u=0\), that character is trivial on \(K(m+1)\); if \(v=0\), it is trivial on the corresponding subgroup for the other adjacent maximal order \(\operatorname{diag}(\varpi^{-1},1)\mathfrak M\operatorname{diag}(\varpi,1)\). In either case the vector has level at most \(m\). Thus both entries are units, which says exactly \(\alpha\mathfrak I=\mathfrak P^{-n}\).

In the maximal-order case \(\beta=\varpi^n\alpha\) generates the unramified quadratic extension and \(\mathcal O[\beta]=\mathcal O_E\). To see the equality, lift the residue basis \(1,\bar\beta\) successively and use completeness. In the period-two case \(\beta=\varpi^{m+1}\alpha\) has trace in \(\mathfrak p\) and determinant of valuation one. Its polynomial is Eisenstein, and \(\mathcal O[\beta]=\mathcal O_E\): the two terms of \(a+b\beta\) have different valuation parity, so an integral element has \(a,b\in\mathcal O\). This also covers an inseparable quadratic extension in characteristic two. Changing the parameter by \(\mathfrak P^{1-n}\) preserves these reduction or Eisenstein conditions. In the one-dimensional \(E\)-space \(F^2\), integral field lattices are precisely the fractional ideals of \(\mathcal O_E\). Their chain is exactly the one described in (7.4). \(\square\)

Refine the chosen first character as follows:
\[
 r=\lfloor n/2\rfloor+1,\qquad l=n+1-r,
 \qquad H=U_{\mathfrak A}^r.
\tag{7.10}
\]
The first character space in \(V^{U_{\mathfrak A}^{n+1}}\) is stable under \(H\), whose action there factors through an abelian group. Select one character component. Formula (7.6) supplies a parameter \(\alpha\) for it, retaining the first layer and hence Lemma 7.6's conditions. If the period-two quadratic polynomial is inseparable, add a sufficiently small diagonal entry in \(\mathfrak P^{1-r}\). Its trace becomes nonzero, without changing the character or its Eisenstein property. We can take \(E=F[\alpha]\) separable.

**Lemma 7.7 — the full intertwining set.** The character just selected has
\[
 I_G(\theta_\alpha|_H)
   =\{g:gHg^{-1}=H,\ \theta_\alpha^g=\theta_\alpha\}
   =E^\times U_{\mathfrak A}^{l}=:J_\alpha.
\tag{7.11}
\]
This group is open, contains the centre, and is compact modulo it.

**Proof.** We must first rule out intertwiners moving the chain. For additive lattices in \(M_2(F)\),
\((L_1\cap L_2)^\perp=L_1^\perp+L_2^\perp\). This is finite abelian duality: place both lattices between two scalar matrix lattices, use the perfect four-entry pairing on the quotient, and apply \(|L_1+L_2||L_1\cap L_2|=|L_1||L_2|\). In particular, intertwining the first-layer character gives
\[
 (\alpha+\mathfrak P^{1-n})\cap
       g^{-1}(\alpha+\mathfrak P^{1-n})g\ne\varnothing.
\tag{7.12}
\]
This follows by testing equality of the two characters on
\(1+(\mathfrak P^n\cap g^{-1}\mathfrak P^ng)\), and applying (7.5).

Choose \(\gamma\) in that intersection. Lemma 7.6 identifies the full chain of \(\mathcal O_{F[\gamma]}\)-lattices with the chosen chain. It does the same for \(g\gamma g^{-1}\). Conjugation by \(g\) carries the first full chain onto the second, so \(g\) preserves the chain and normalizes \(\mathfrak A\). Any intertwiner on \(H\) intertwines the first layer, since \(U_{\mathfrak A}^n\subset H\), so this conclusion applies to it. It now normalizes \(H\); intertwining becomes equality of its characters on all of \(H\).

The chain normalizer is \(E^\times U_{\mathfrak A}\). An element preserving the chain translates its integer index; a power of a field uniformizer effects that same translation, leaving an element fixing every lattice. This remainder is an order unit. After removing the field factor we may suppose \(g\in U_{\mathfrak A}\). The character equality is
\(g^{-1}\alpha g-\alpha\in\mathfrak P^{1-r}\). Since \(\alpha\mathfrak A=\mathfrak P^{-n}\), multiplication by the unit and by \(\alpha^{-1}\) makes this equivalent to
\[
 \alpha g\alpha^{-1}-g\in\mathfrak P^l.
\tag{7.13}
\]

Here is the required congruence calculation, without a centralizer theorem:
\[
 \{x\in\mathfrak A:\alpha x\alpha^{-1}-x\in\mathfrak P^a\}
       =\mathcal O_E+\mathfrak P^a\qquad(a\geq1).
\tag{7.14}
\]
For the maximal order, reduce modulo \(\mathfrak P\). A linear map commuting with multiplication by the generating residue element of \(k_2\) is multiplication by its value at \(1\); thus its residue lies in \(k_2\). For the other order, \(\mathfrak I/\mathfrak P=k\oplus k\), and conjugation by \(\alpha\) exchanges these factors. The fixed pairs are \((c,c)\), the image of \(\mathcal O_E\). This proves (7.14) for \(a=1\).

For higher \(a\), subtract that integral field approximation, leaving \(x\in\mathfrak P\). More generally, after \(a-1\) layers the remainder lies in \(\mathfrak P^{a-1}\). Divide it on the left by the \((a-1)\)-st power of an \(E\)-uniformizer. This takes that lattice to \(\mathfrak A\), commutes with \(\alpha\), and reduces the desired next layer to the case just proved. Multiply back and add the resulting integral field element. This gives the next approximation, proving (7.14) by induction. The reverse inclusion follows because field elements commute with \(\alpha\), which normalizes every \(\mathfrak P^a\).

If \(g\) is a unit, the field approximation in (7.14) is an \(E\)-unit; hence (7.13) puts it in \(\mathcal O_E^\times U_{\mathfrak A}^l\). Restoring the field factor gives the required upper bound for the intertwining set. Conversely \(E^\times\) commutes with \(\alpha\), and conjugation by \(1+y\), \(y\in\mathfrak P^l\), changes \(x\in\mathfrak P^r\) only by \(\mathfrak P^{l+r}=\mathfrak P^{n+1}\). This preserves the character, proving equality. Finally \(U_{\mathfrak A}^l\) is compact open, and \(E^\times/F^\times\) is compact: valuation classes form a finite quotient, and unit classes are compact. \(\square\)

**Theorem 7.8 — full compact-induction exhaustion.** Every irreducible supercuspidal of \(\mathrm{GL}_2(F)\) is compactly induced from a finite-dimensional irreducible smooth representation of an open subgroup containing the centre and compact modulo it.

**Proof.** Apply the preceding selection to a least-level determinant twist. At level zero, its finite cuspidal \(K\)-type extends to \(ZK\) using the representation's central character: scalar units already act correctly, and the value at \(\varpi I\) determines the extension. Theorem 3.1 gives intertwining exactly \(ZK\). The irreducibility criterion of Theorem 2.1 and compact Frobenius reciprocity give a nonzero map from that irreducible compact induction onto the given irreducible representation, hence an isomorphism.

At positive level, take the nonzero finite-dimensional space \(W=V^{\theta_\alpha|_H}\). Lemma 7.7 makes it a \(J_\alpha\)-module. Choose a nonzero invariant subspace of minimum dimension; it is an irreducible smooth representation \(\tau\), and \(\tau|_H\) is a multiple of the chosen character. An intertwiner of \(\tau\) must therefore intertwine that character on the intersection of \(H\) and its conjugate. Lemma 7.7 puts it in \(J_\alpha\), so \(I_G(\tau)=J_\alpha\). Theorem 2.1 makes its compact induction irreducible and supercuspidal. Compact Frobenius reciprocity maps it nontrivially to the given representation, again an isomorphism. Twisting \(\tau\) back on the same subgroup removes the initial determinant twist. This proves the assertion in every characteristic. \(\square\)

The compact field-lattice construction is treated in Gérardin–Kutzko, *Facteurs locaux pour GL(2)*, Section 5.3, for the ramified lattice filtration. The proof above also selects the required character inside an arbitrary supercuspidal and computes its entire intertwining set. Carayol's Théorème 8.1 gives a counting approach for prime rank in characteristic zero. Neither an external exhaustion theorem nor a local parameter correspondence is an input to the argument here.


### 7.2. Exhaustion by the quadratic Weil models in odd residue characteristic

We now assume that \(q\) is odd. All quadratic extensions used below are separable. A ramified quadratic extension is tame, has different exponent one, and may be written \(F(\sqrt{\varpi u})\), with \(u\) a unit. To see the assertions directly, complete the square in a quadratic polynomial, and remove even powers of \(\varpi\). A nonsquare unit gives the unramified extension, since its reduction is nonsquare and Hensel lifting applies; a unit whose reduction is square is itself a square, because two is a unit. In the remaining case \(X^2-\varpi u\) is Eisenstein, and its derivative \(2\sqrt{\varpi u}\) gives the different ideal \(\mathfrak p_E\). These arguments work also over fields of positive characteristic.

Use the auxiliary additive character \(\psi_*\) of conductor \(\mathfrak p\) from Section 7.1 in the Weil construction. Theorem 6.5 permits this choice. In both the unramified and tame ramified cases,
\[
\{x\in E:\psi_*(\operatorname{Tr}(x\mathcal O_E))=1\}
 =\mathfrak p_E.
\tag{7.15}
\]
For the unramified extension this follows from nondegeneracy of the residue trace pairing. For the ramified extension, in the basis \(1,t\), \(t^2=\varpi u\), the trace pairing is diagonal with entries \(2\) and \(2\varpi u\); its conductor-one annihilator is \(\varpi\mathcal O\oplus\mathcal O t=\mathfrak p_E\). Multiplication by a uniformizer gives the annihilator of \(\mathfrak p_E^j\) as \(\mathfrak p_E^{1-j}\).

The unit norms satisfy
\[
N(U_E^j)\subset
\begin{cases}
 U_F^j,&E/F\text{ unramified},\\
 U_F^{\lceil j/2\rceil},&E/F\text{ tame ramified}.
\end{cases}
\tag{7.16}
\]
Indeed \(N(1+x)=1+\operatorname{Tr}x+Nx\). The trace ideals in the two cases are respectively \(\mathfrak p_F^j\) and \(\mathfrak p_F^{\lceil j/2\rceil}\), as the same two integral bases show, and the norm terms have valuations at least \(2j\) and \(j\). In particular the ramified norm character is trivial on \(U_F^1\): every \(1+x\) there has a square root in \(U_F^1\), and the norm of a scalar square root is \(1+x\).

**Lemma 7.9 — a vector carrying the minimal compact character.** Let \(b\) be one of the minimal elliptic elements of Lemma 7.6, refined as at the end of that lemma. In the unramified case let
\[
v_E(b)=-n,\quad h=\lfloor n/2\rfloor+1,\quad
 l=n+1-h,\quad H=U_{\mathfrak A}^h.
\]
In the ramified case write
\[
v_E(b)=1-2N,\quad h=N,\quad a=\lceil N/2\rceil,
 \quad H=U_{\mathfrak A}^N.
\]
Thus the ramified order exponent in Section 7.1 is \(2N-1\). Choose any character \(\theta\) of \(E^\times\) such that
\[
\theta(1+x)=\psi_*(\operatorname{Tr}(bx)),\qquad
 x\in\mathfrak p_E^h.
\tag{7.17}
\]
Every such character is regular. The Weil representation \(\pi(\theta)\) contains the character \(\theta_b\) of \(H\).

**Proof.** The prescribed deep character is well-defined because products of two such \(x\)'s pair trivially with \(b\) under (7.15): the required inequalities are \(2h-n\ge1\) and \(2N+(1-2N)=1\). It extends to a smooth character of \(E^\times\). For example first work in the finite abelian unit quotient killing \(U_E^{n+1}\), or \(U_E^{2N}\), extend its subgroup character using roots in \(\mathbb C^\times\), and then choose a value on an \(E\)-uniformizer.

In the unramified case \(b-b^\sigma\) has valuation \(-n\), because the residue of \(\varpi^n b\) generates the quadratic residue field. In the ramified case it has valuation \(1-2N\), because two is a unit and the leading term of \(b\) is an odd uniformizer power, whereas its trace has even valuation at least \(2-2N\). Equation (7.15) shows in either case that the prescribed characters for \(b\) and \(b^\sigma\) differ on \(U_E^h\). Thus \(\theta\ne\theta^\sigma\), hence \(\theta\) is regular.

Use the basis \(1,b\) to write multiplication by \(b\) as
\[
 b=\begin{pmatrix}0&-Nb\\1&\operatorname{Tr}b\end{pmatrix}.
\tag{7.18}
\]
The maximal order in the unramified case and the chain order in the ramified case become
\[
\mathfrak A=
\begin{cases}
\begin{pmatrix}\mathcal O&\mathfrak p^{-n}\\
                \mathfrak p^n&\mathcal O\end{pmatrix},&\text{unramified},\\[6pt]
\begin{pmatrix}\mathcal O&\mathfrak p^{1-N}\\
                \mathfrak p^N&\mathcal O\end{pmatrix},&\text{ramified}.
\end{cases}
\tag{7.19}
\]
These follow respectively from the bases \(1,\varpi^n b\) of \(\mathcal O_E\), and \(1,\varpi^N b\) with the latter element an \(E\)-uniformizer. They agree with the unique field lattice chains proved in Lemma 7.7.

Put \(a=h\) in the unramified case and retain the stated \(a\) in the ramified case. In the norm component of the Weil model take
\[
\Phi_0(y)=\theta(y)^{-1}|y|_E^{-1/2}
                       \mathbf1_{U_F^a}(Ny).
\tag{7.20}
\]
This is a nonzero compact locally constant test, supported on \(E\)-units, with the required \(E^1\)-covariance. The formula is nonzero already at one. Its scalar Kirillov test is \(\mathbf1_{U_F^a}\).

For \(n(z)\in H\), the parameter \(z\) has valuation at least \(h-n\) in the unramified case and \(1-a\) in the ramified case. The norm support and the inequalities \(2h-n\ge1\) and \(1-a+a=1\) therefore give
\(r(n(z))\Phi_0=\psi_*(z)\Phi_0\), the value prescribed by (7.18).

Diagonal elements of \(H\) have entries \(u,v\in U_F^a\). Write their matrix as \(vI\,d(u/v)\), and choose \(z_E\) of norm \(u/v\), which is possible by taking the principal-unit square root of \(u/v\) as a scalar in either case. Formulas (6.2)–(6.3) cancel the \(z_E\)-factors in (7.20). The norm support is unchanged, and the resulting scalar is \(\eta(v)\theta(v)=\theta(v)\). Here \(\eta(v)=1\) in both cases. Equation (7.17) applies to \(v\), since its \(E\)-unit depth is \(h\) in the unramified case and \(2a\ge N\) in the ramified case. The scalar is consequently \(\psi_*(\operatorname{Tr}b(v-1))\), again exactly \(\theta_b\).

It remains to check the lower root. The Fourier transform of (7.20), at \(x\), is an integral with phase \(\psi_*(\operatorname{Tr}(x^\sigma y))\). Average that integral after replacing \(y\) by \(y(1+z)\), \(z\in\mathfrak p_E^h\). This preserves its domain by (7.16), its Haar measure since \(1+z\) is a unit, and its absolute-value factor. By (7.17), the new phase factor is
\[
\psi_*(\operatorname{Tr}((x^\sigma y-b)z)).
\]
Finite additive-character orthogonality and (7.15) imply that a nonzero Fourier value requires, for some \(y\) in the original support,
\[
x^\sigma y-b\in\mathfrak p_E^{1-h}.
\tag{7.21}
\]
The averaging is legitimate as an ordinary finite average after a sufficiently small subgroup is divided out; no oscillatory convergence is used. In the unramified case (7.21) implies
\(x^\sigma y/b\in U_E^l\), hence
\(Nx/Nb\in U_F^l\). In the ramified case it implies membership in \(U_E^N\), hence \(Nx/Nb\in U_F^a\).

A lower-root parameter in \(H\) has valuation at least \(n+h\) or \(2N-a\), respectively. Since \(v_F(Nb)=-2n\) or \(1-2N\), the corresponding phase difference has valuation at least
\[
(n+h)-2n+l=1,
 \qquad (2N-a)+(1-2N)+a=1.
\]
Thus multiplication by \(\psi_*(-zNx)\) on the Fourier support is the scalar \(\psi_*(-zNb)\). The identity
\(l(z)=w_0^{-1}n(-z)w_0\) proves the required lower-root eigenvalue. Gaussian elimination, with the displayed valuation bounds, generates \(H\) by these diagonal and root elements. Since \(\theta_b\) is a character, the generator calculations prove the assertion on all of \(H\). \(\square\)

We will count the irreducible types over this fixed deep character, rather than guess how a uniformizer acts on (7.20). Write \(A_0\ne0\) for the desired central value at \(\varpi I\); the unit part of the central character is allowed to vary in this finite count.

**Lemma 7.10 — the exact number of compact types.** With \(b,H\) as above, put \(J=I_G(\theta_b|_H)\), as determined in Lemma 7.7. The number of irreducible \(J\)-representations whose restriction to \(H\) is a multiple of \(\theta_b\) and whose scalar action at \(\varpi I\) is \(A_0\) is
\[
\begin{array}{c|c|c}
\text{case}&\text{number}&\text{dimension}\\ \hline
\text{ramified }(2N-1)&2(q-1)q^{N-1}&1\\
\text{unramified }n=2m+1&(q^2-1)q^{2m}&1\\
\text{unramified }n=2m\ (m\ge1)&(q^2-1)q^{2m}&q.
\end{array}
\tag{7.22}
\]

**Proof in the two character cases.** For the ramified case \(J=E^\times H\) with \(H=U_{\mathfrak A}^N\), and for odd unramified \(n\), \(J=E^\times H\) with \(H=U_{\mathfrak A}^{m+1}\). The deep character is invariant under \(E^\times\). Its intersection with the torus is \(U_E^N\) or \(U_E^{m+1}\), with character (7.17). Extend that torus character, prescribing its value at the scalar \(\varpi\) to be \(A_0\), and define
\(\tau(eh)=\tau(e)\theta_b(h)\). This is a well-defined character of \(J\). Dividing any irreducible type by it leaves a representation of the abelian quotient \(J/H\); with the prescribed scalar value this factors through a finite abelian quotient, so it is a character.

For ramified \(E\), the finite torus quotient after imposing the scalar-uniformizer value has order
\[
[E^\times:\langle\varpi\rangle U_E^N]
 =2[\mathcal O_E^\times:U_E^N]
 =2(q-1)q^{N-1}.
\tag{7.23}
\]
The factor two is the valuation quotient \(\mathbb Z/2\mathbb Z\). It persists when the central value is fixed: the two allowed values of an \(E\)-uniformizer are the two square roots of the compatible scalar-unit value. In the unramified case an \(E\)-uniformizer is the scalar \(\varpi\), and the analogous quotient has order
\((q^2-1)q^{2m}\). This proves the first two rows.

**Proof in the even unramified case.** Conjugate the maximal order to \(M_2(\mathcal O)\), and set
\[
P=K(m),\quad H=K(m+1),\quad
 Q=U_E^mH,\quad b=\varpi^{-2m}b_0,
 \quad \bar b_0\in k_2\setminus k.
\]
The character \(\theta_b\) of \(H\) is invariant under \(P\). Indeed \([P,H]\subset K(2m+1)\), on which it is trivial. Extend it to \(Q\) by choosing a character \(\varphi\) on \(U_E^m\) with the given restriction on \(U_E^{m+1}\), and setting
\(\chi_Q(eh)=\varphi(e)\theta_b(h)\). There are exactly \(q^2\) choices, since \(U_E^m/U_E^{m+1}\simeq k_2^+\).

For \(1+\varpi^mX,1+\varpi^mY\), their commutator, evaluated by the deep character, is
\[
\bar\psi\bigl(\operatorname{tr}(\bar b_0[\bar X,\bar Y])\bigr).
\tag{7.24}
\]
The omitted terms have matrix valuation at least \(2m+1\). The radical of this alternating pairing on \(M_2(k)\) is exactly \(k_2\):
\(\operatorname{tr}(\bar b_0[X,Y])
 =\operatorname{tr}([\bar b_0,X]Y)\), and varying \(Y\), including all scalar multiples, makes the residue trace pairing nondegenerate. Its vanishing therefore says \([\bar b_0,X]=0\), whose solutions are precisely the multiplication maps by \(k_2\). Thus \(P/Q\) is a two-dimensional symplectic \(k\)-space. The character \(\chi_Q\) is \(P\)-invariant, and its kernel has finite index in the relevant compact groups.

Here is the finite Heisenberg argument in full. Choose a one-dimensional isotropic line in \(P/Q\), and let \(L\) be its inverse image. The commutator has trivial \(\chi_Q\)-value on \(L\), so \(\chi_Q\) extends to a character of \(L\) by finite abelian character extension. Inducing it from \(L\) to \(P\) has dimension \(q\). For an element outside \(L\), the nondegenerate pairing with that line changes the inducing character on their intersection. Finite Mackey reciprocity consequently gives endomorphism dimension one. Finite complete reducibility then gives irreducibility. Conversely every irreducible \(P\)-representation with this \(Q\)-character contains one of the characters of \(L\) extending it. There are \(q\) such extensions, and conjugation by \(P/L\) permutes them freely and transitively through (7.24). Their induced representations are all the same. Hence there is a unique such irreducible representation \(\rho_\varphi\), of dimension \(q\).

It extends to \(J=E^\times P\). We give the extension, including its possible choices. First \(U_E^1\) centralizes the action of \(P\) in \(\rho_\varphi\). For \(e\in U_E^1\), \(x=1+\varpi^mX\), the commutator belongs to \(H\). In
\[
exe^{-1}x^{-1}-1
 =\varpi^m(eXe^{-1}-X)(1+\varpi^mX)^{-1},
\]
the trace against \(b\) of the first term is zero because \(e\) commutes with \(b\). The next terms pair trivially: \(eXe^{-1}-X\in\varpi M_2(\mathcal O)\) and their valuation after pairing with \(b\) is at least one. Thus their \(\theta_b\)-value is one. Extend \(\varphi\) from \(U_E^m\) to a scalar character of \(U_E^1\).

The residue-unit group has a cyclic lift \(\mu_{q^2-1}\subset\mathcal O_E^\times\), obtained by Hensel lifting the simple roots of \(X^{q^2-1}-1\); every unit is a unique product of such a lift and a principal unit. A generator preserves the \(Q\)-character, so uniqueness of \(\rho_\varphi\) supplies an intertwining matrix \(T\). Its \((q^2-1)\)-st power is scalar. Rescale \(T\) by a complex root to make that power the identity. Together with the scalar principal-unit action and the prescribed scalar-uniformizer action \(A_0\), this defines an extension to \(E^\times P\). Its values agree on the intersections, and the verified commutator identity gives every compatibility relation.

All extensions for fixed \(\varphi\) differ by characters of
\(E^\times/U_E^m\), with the scalar-uniformizer value fixed. There are
\((q^2-1)q^{2m-2}\) such choices. They exhaust the irreducible \(J\)-types for this \(\varphi\): after choosing one extension, its multiplicity space in any irreducible type is a representation of the abelian quotient \(J/P\), so is one dimensional. The \(q^2\) possible \(\varphi\)'s are preserved individually by \(E^\times\), since this torus commutes with its units and preserves the deep trace character. Multiplying the two counts proves the last row of (7.22). \(\square\)

**Theorem 7.11 — every positive-level odd-residue type is quadratic Weil.** Every positive-level supercuspidal of Theorem 7.8, over a field of odd residue characteristic, is one of the models \(\pi(\theta)\) of Section 6, after its indicated determinant twist.

**Proof.** Fix the minimal element \(b\) and its deep character, and fix \(A_0\) as in Lemma 7.10. Count characters \(\theta\) satisfying (7.17) and
\[
\theta(\varpi)\eta(\varpi)=A_0.
\tag{7.25}
\]
Their number is
\(2(q-1)q^{N-1}\) in the ramified case, and
\((q^2-1)q^{2(h-1)}\) in the unramified case. This is the same finite torus-quotient count as (7.23), with a different prescribed nonzero scalar value; character extension is always possible. In the unramified even case \(h=m+1\), this becomes \((q^2-1)q^{2m}\), exactly the last row of (7.22).

They give pairwise distinct Weil models. In fact the deep characters for \(b\) and \(b^\sigma\) differ, as proved in Lemma 7.9, so the conjugate of one character in this list is not in the list. Lemma 6.6 now gives injectivity.

Each model contains \(\theta_b|_H\), by Lemma 7.9. This character space is finite dimensional by admissibility, is stable under \(J\), and contains an irreducible \(J\)-type. Every such type has intertwining exactly \(J\), since any intertwiner also intertwines its scalar \(H\)-character, whose entire intertwining set is \(J\). Theorem 2.1 and compact Frobenius reciprocity identify its compact induction with the irreducible Weil model.

Moreover this type is unique. In that compact induction the \(H\)-character space has support only on \(J\): the restriction-by-double-cosets calculation of Section 2 shows that any other support coset would intertwine the character on the common \(H\)-subgroup, contrary to Lemma 7.7. On \(J\) that space is precisely the inducing type. Thus two different Weil models in our list yield two different types in (7.22).

The finite lists have equal size, so this injection is a bijection. It includes every type contained in the original least-level twist, not merely one type for each leading matrix. Removing the determinant twist uses
\(\pi(\theta)\otimes\nu^{-1}
 =\pi(\theta(\nu^{-1}\circ N))\), from Theorem 6.5; regularity is preserved. This proves the theorem. \(\square\)

**Lemma 7.12 — level zero is quadratic Weil too.** Every depth-zero supercuspidal in Section 3 is a quadratic Weil model for the unramified quadratic extension.

**Proof.** Let \(\theta_0:k_2^\times\to\mathbb C^\times\) be regular, inflate it to \(\mathcal O_E^\times\), and choose
\(\theta(\varpi)=A_0/\eta(\varpi)\). In the quadratic-plane space use the finite subspace of tests supported on \(\mathcal O_E\) and constant on cosets of \(\mathfrak p_E\). For conductor-one \(\psi_*\), its Fourier transform is the finite transform on \(k_2\), with coefficient \(q^{-1}\): the self-dual volume of \(\mathcal O_E\) is \(q\), since its annihilator is \(\mathfrak p_E\), and each residue ball has volume \(q^{-1}\). The finite subspace is therefore Fourier invariant.

Impose the \(E^1\)-character covariance. The reduction of \(E^1\) is the norm-one subgroup of \(k_2^\times\), of order \(q+1\). Its character is nontrivial precisely because \(\theta_0\) is regular. The value at zero is forced to vanish. Each nonzero norm fibre contributes one dimension, so this subspace has dimension \(q-1\).

The Weil operators preserve it under \(K\): upper roots are norm phases, diagonal units permute the residue norms and multiply by the given character, and the Weyl operator is the finite Fourier transform. The principal congruence subgroup \(K(1)\) acts trivially. For upper roots this follows because their parameters lie in \(\mathfrak p\), the norms are integral and \(\psi_*\) kills \(\mathfrak p\); for lower roots it follows by Fourier invariance. For diagonal principal units choose principal-unit norm lifts, on which \(\theta\) is trivial. Gaussian elimination then proves the assertion on all of \(K(1)\).

The resulting \(\mathrm{GL}_2(k)\)-representation is irreducible and cuspidal. Its upper-root eigencharacters are the \(q-1\) distinct nonzero norm values, each once. Diagonal units act transitively on them. Finite character projections and those dilations show that a nonzero invariant subspace contains each of the one-dimensional eigenspaces. The trivial upper-root character is absent, which proves cuspidality.

There are \(q(q-1)\) regular characters of \(k_2^\times\): among its \(q^2-1\) characters, the \(q-1\) norm-factor characters are exactly those fixed by Frobenius. Their conjugate pairs give \(q(q-1)/2\) pairwise distinct Weil models with central-uniformizer value \(A_0\), by Lemma 6.6. Each contains the finite cuspidal type just constructed, and its \(ZK\)-extension has scalar value \(A_0\). Theorem 3.1 and Frobenius reciprocity identify its compact induction with that model.

Distinct finite cuspidal types cannot have isomorphic compact inductions. The cross-type version of the Cartan calculation in Section 3 kills every positive Cartan position by unipotent averaging; at the identity position finite Schur orthogonality allows a map only between isomorphic types. Finally the finite-field classification proved in the prerequisite of Section 5 gives exactly \(q(q-1)/2\) finite cuspidal types. Equal counts prove that all of them occur. \(\square\)

**Theorem 7.13 — odd-residue quadratic exhaustion.** Over every nonarchimedean local field of odd residue characteristic, every irreducible supercuspidal representation of \(\mathrm{GL}_2(F)\) is a regular quadratic Weil representation \(\pi(\theta)\). Its character may have arbitrarily high conductor.

**Proof.** Theorem 7.8 supplies, after a determinant twist, either the finite cuspidal type of level zero or one of the positive-level elliptic types. Lemma 7.12 and Theorem 7.11 identify all of them. Remove the twist by Theorem 6.5. The entire argument uses explicit Fourier orthogonality, the compact-intertwining theorem, and finite character counts; it does not use local Langlands or Jacquet–Langlands. \(\square\)

### 7.2.1. An actual exceptional representation in residue characteristic two

**Theorem 7.14 — the odd-residue restriction is necessary.** There is an irreducible supercuspidal representation of \(\mathrm{GL}_2(\mathbb Q_2)\) which is not a quadratic Weil model for any quadratic extension. Thus the exhaustion in Theorem 7.13 cannot be asserted in residue characteristic two.

**Proof.** We construct it and distinguish it using self-twists. Work with an additive character \(\psi_*\) of conductor \(2\mathbb Z_2\), so \(\psi_*(1)=-1\). Put \(E=\mathbb Q_2(i)\), \(i^2=-1\), and
\[
b=(1+i)/4,\qquad t=1+i.
\]
The element \(t\) is an \(E\)-uniformizer: \(t^2=2i\). Its Eisenstein polynomial is \(X^2-2X+2\), so \(\mathcal O_E=\mathbb Z_2[t]\). Use the integral basis \(1,t\). Multiplication by \(b=t/4\), and the order preserving the ideals of \(\mathcal O_E\), are
\[
b=\begin{pmatrix}0&-1/2\\1/4&1/2\end{pmatrix},\qquad
\mathfrak A=\begin{pmatrix}\mathbb Z_2&2\mathbb Z_2\\
                         \mathbb Z_2&\mathbb Z_2\end{pmatrix},\qquad
\mathfrak P=\begin{pmatrix}2\mathbb Z_2&2\mathbb Z_2\\
                         \mathbb Z_2&2\mathbb Z_2\end{pmatrix}.
\tag{7.26}
\]
Here \(\mathfrak P^2=2\mathfrak A\). We have \(v_E(b)=-3\), so this is the ramified minimal element of order exponent three in Lemma 7.7. Set
\[
H=1+\mathfrak P^2,\qquad
\xi(1+x)=\psi_*(\operatorname{tr}(bx)),\qquad
J=E^\times H.
\tag{7.27}
\]
The same trace-annihilator calculation as (7.5) makes \(\xi\) a character, and Lemma 7.7 proves \(I_G(\xi)=J\), in residue characteristic two as well.

The torus intersection is \(E^\times\cap H=U_E^2\). Extend \(\xi|_{U_E^2}\) to a smooth character of \(E^\times\), by finite abelian character extension and a choice on the uniformizer. Combining it with \(\xi\) gives a character \(\tau\) of \(J\); torus invariance of the trace formula verifies the product rule. Since every intertwiner of \(\tau\) intertwines \(\xi\), Theorem 2.1 proves that
\(\pi=\mathrm{c\!-\!Ind}_J^G\tau\) is irreducible and supercuspidal. Notice the forced value
\[
\tau(-1)=\psi_*(\operatorname{tr}(-2b))=\psi_*(-1)=-1.
\tag{7.28}
\]
We will show that \(\pi\) has no nontrivial quadratic determinant self-twist.

We first list all possible quadratic characters \(\chi\) of \(\mathbb Q_2^\times\), without a reciprocity classification. An odd unit is a square precisely when it is one modulo eight. Necessity follows by squaring odd integers. For sufficiency, start with the root one modulo eight, and lift a solution \(r^2\equiv u\pmod{2^n}\), \(n\ge3\), by replacing the odd \(r\) with \(r+\epsilon2^{n-1}\). Its square changes by \(\epsilon2^n r\) modulo \(2^{n+1}\), so one choice of \(\epsilon\) lifts the next digit. The compatible roots converge. Valuation parity and the four odd residues modulo eight therefore give a square-class group of order eight.

Its seven nontrivial characters comprise the unramified character, two characters of conductor two, and four of conductor three. Indeed \(\mathbb Z_2^\times=U_F^1\), its quotient by \(U_F^3\) has order four, and \(U_F^2/U_F^3\) has order two. A nontrivial unit character trivial on \(U_F^2\) is unique; either choice of its value at two gives the two conductor-two characters. The other two nontrivial unit characters give the four conductor-three characters. The remaining nontrivial character is trivial on units and has \(\chi(2)=-1\). In particular,
\[
\chi(1+2z)=(-1)^z\quad(a(\chi)=2),\qquad
\chi(1+4z)=(-1)^z\quad(a(\chi)=3).
\tag{7.29}
\]

A self-twist would give an intertwiner between the compact inductions of \(\tau\) and \(\tau(\chi\circ\det)\). Compact Frobenius reciprocity and the double-coset calculation of Section 2 imply a nonzero intertwiner on some \(J\cap gJg^{-1}\). We exclude it in the three cases.

For unramified \(\chi\), the two types have the same \(H\)-character, so Lemma 7.7 forces \(g\in J\). Their torus values differ at \(t\): \(Nt=2\), so \(\chi(Nt)=-1\). Since the two \(J\)-types are characters, conjugation by \(J\) cannot change them. They cannot intertwine.

For conductor two, \(x\in\mathfrak P^2=2\mathfrak A\) has \(\det x\in4\mathbb Z_2\). Thus \(\det(1+x)=1+\operatorname{tr}x+\det x\), together with (7.29), gives
\[
\xi(1+x)\chi(\det(1+x))
 =\psi_*(\operatorname{tr}((b+\tfrac12 I)x)).
\tag{7.30}
\]
Let \(s\) be the \(F\)-linear map inducing the involution of \(E/F\); in the basis (7.26) its matrix is \(\left(\begin{smallmatrix}1&2\\0&-1\end{smallmatrix}\right)\). It preserves the ideal chain, hence normalizes \(H\). We have
\(b^\sigma=\tfrac12-b\), and
\(b+\tfrac12-b^\sigma=2b\in\mathfrak P^{-1}\), which is the trace annihilator of \(\mathfrak P^2\). Consequently (7.30) is exactly the conjugate \(H\)-character \(\xi^s\). Its intertwiners with \(\xi\) lie in the single coset obtained by composing \(s\) with \(I_G(\xi)=J\). On the torus such an intertwiner would require agreement of \(\tau^\sigma\) and \(\tau(\chi\circ N)\). At \(i\) this is impossible:
\[
\tau(i^\sigma)=\tau(-i)=-\tau(i),\qquad
\tau(i)\chi(Ni)=\tau(i),\qquad Ni=1.
\tag{7.31}
\]
Inner conjugations from the extra \(J\)-factor do not change a character. This excludes both conductor-two possibilities.

For conductor three, restrict to \(H'=1+\mathfrak P^3\). Its matrices \(x\) have diagonal entries in \(4\mathbb Z_2\), upper-right entry in \(4\mathbb Z_2\), and lower-left entry in \(2\mathbb Z_2\). Hence \(\det x\in8\mathbb Z_2\), and (7.29) gives the two linear characters represented by
\[
b\quad\text{and}\quad b'=b+\tfrac14 I
\tag{7.32}
\]
on \(H'\). Intertwining these characters would force an intersection of the trace-dual cosets
\[
(b+\mathfrak P^{-2})\ \cap\
 g(b'+\mathfrak P^{-2})g^{-1}\ne\varnothing.
\tag{7.33}
\]
This is the lattice-duality implication used in Lemma 7.7: the annihilator of an intersection is the sum of the annihilators, and the annihilator of \(\mathfrak P^3\) is \(\mathfrak P^{-2}\). It applies to these linear characters without an ellipticity hypothesis.

But all matrices in the first coset have determinant valuation \(-3\), and all in the second have determinant valuation \(-4\). Here
\[
\det b=1/8,\qquad \det b'=5/16,\qquad
\mathfrak P^{-2}=\tfrac12\mathfrak A
 =\begin{pmatrix}\tfrac12\mathbb Z_2&\mathbb Z_2\\
                 \tfrac12\mathbb Z_2&\tfrac12\mathbb Z_2\end{pmatrix}.
\tag{7.34}
\]
For \(\delta\) in this lattice, every term in
\(\det(b+\delta)-\det b\) has valuation at least \(-2\), by the four entry bounds. Every term in
\(\det(b'+\delta)-\det b'\) has valuation at least \(-3\). Neither leading determinant can cancel. Conjugation preserves the determinant, so (7.33) is impossible. This excludes all four conductor-three possibilities.

Finally every quadratic Weil model has the nontrivial self-twist \(\eta_{E/F}\circ\det\). Indeed it is induced from the index-two subgroup \(G^+=\ker(\eta_{E/F}\circ\det)\), by Theorem 6.4; multiplying an induced function by that quotient character is an explicit intertwiner with its twist. The representation constructed above has none, so it cannot be any quadratic Weil model. This proves an actual residue-two exception without a local Langlands correspondence or an exceptional-classification theorem. \(\square\)

Theorems 7.8, 7.13 and 7.14 now give the full asserted exhaustion and its qualification: all supercuspidals are compact inductions, all are quadratic Weil in odd residue characteristic, and the latter restriction has a concrete counterexample over \(\mathbb Q_2\). The construction of Section 6 and the compact theorem of Section 7.1 remain valid in residue characteristic two. No assertion that every field of residue characteristic two has the same exceptional list is needed or made.

### 7.3. Character support

For the support statement, let \(p:G\to G^{\mathrm{ad}}=\mathrm{PGL}_2(F)\), and let \(C_{\mathrm{ad}}\) be the union of its compact subgroups. We prove the GL₂ support theorem directly from the compact-coefficient theorem of Lesson 6.

The character distribution is well-defined here by
\[
\Theta_\pi(f)=\operatorname{tr}\pi(f),\qquad f\in C_c^\infty(G).
\tag{7.1}
\]
Indeed \(f\) is bi-invariant under some compact open \(J\), so
\(\pi(f)=E_J\pi(f)E_J\), where \(E_J\) is the normalized compact average. Its image is in the finite-dimensional \(V^J\), and its trace is the trace there. This definition is continuous on every fixed support and level test space and is invariant under conjugation. In particular we do not need to assume a pointwise regular-character theorem to prove distributional support.

**Lemma 7.1 — which adjoint elements are compact.** An element \(p(g)\) lies outside \(C_{\mathrm{ad}}\) precisely when \(g\) is split with two eigenvalues of different absolute values.

**Proof.** In that split case, conjugate and scale it to
\(d(a)=\operatorname{diag}(a,1)\), with \(0<|a|<1\), interchanging the eigenlines if necessary. The central-invariant continuous quantity
\(\|g^n\|\|g^{-n}\|\), using the maximum-entry matrix norm, is then
\(|a|^{-n}\). Its powers cannot lie in a compact group.

If the eigenvalues are distinct and have the same absolute value, their ratio is a unit; the element lies in a conjugate of the compact unit diagonal torus. If its characteristic polynomial is irreducible, \(g\) lies in the multiplicative group of the quadratic field algebra \(E=F[g]\). The quotient \(E^\times/F^\times\) is compact: valuation classes modulo the ramification index form a finite set, and the remaining representatives are in the compact unit group of \(E\). This reasoning also covers an inseparable quadratic field algebra in characteristic two.

Finally a repeated-root nonscalar matrix is either in that field case or has the form \(a(I+N)\), with \(N^2=0\). Its adjoint powers are \(I+nN\); the integer scalars \(n\) have compact closure in \(\mathcal O\) in characteristic zero, and form a finite set in positive characteristic. Their closure gives a compact subgroup. Scalars give the identity in the adjoint group. These cases exhaust quadratic minimal polynomials. \(\square\)

**Lemma 7.2 — a positive double-coset operator is nilpotent.** Suppose \(d=\operatorname{diag}(a,b)\) and
\(\delta=a/b\) has valuation \(r>0\). For \(J=K(m)\), \(m\ge1\), put
\(T_d=E_J\pi(d)E_J\). Then
\[
T_d^N=E_J\pi(d^N)E_J\quad(N\ge1).
\tag{7.2}
\]
If \(\pi\) is supercuspidal, \(T_d\) is nilpotent on \(V^J\) and therefore has trace zero.

**Proof.** Gaussian elimination in \(J\) gives its upper-unipotent, diagonal, lower-unipotent factorization. The diagonal factors have entries in \(1+\mathfrak p^m\); both root factors have entries in \(\mathfrak p^m\). Conjugation by \(d\) contracts the upper root by \(\delta\) and expands the lower root by \(\delta^{-1}\). Thus the right \(J\)-cosets in \(JdJ\) have representatives
\[
n(x)dJ,\qquad x\in\mathfrak p^m/\delta\mathfrak p^m.
\]
There are \(q^r\) of them, and normalized averaging gives
\[
T_d=q^{-r}\sum_x\pi(n(x)d)E_J.
\tag{7.3}
\]
For an explicit check on the representatives, \(J\cap dJd^{-1}\) imposes exactly that the upper-right entry have valuation at least \(m+r\). For \(j\in J\), subtract \(x\) times its bottom row, with
\(x\equiv j_{12}/j_{22}\pmod{\mathfrak p^{m+r}}\); the result is in that intersection. This proves the claimed coset decomposition and normalization.

The sum in (7.3) has left \(J\)-invariant image, so the middle compact projector disappears when we multiply two such sums. The relation
\(d^N n(y)d^{-N}=n(\delta^Ny)\) shows inductively that the products of representatives give exactly
\[
n(x+\delta^Ny)d^{N+1}J,\qquad
x\in\mathfrak p^m/\delta^N\mathfrak p^m,\quad
y\in\mathfrak p^m/\delta\mathfrak p^m.
\]
These are all representatives modulo \(\delta^{N+1}\mathfrak p^m\), each once. The coefficient is \(q^{-(N+1)r}\). This proves (7.2), including arbitrary unit factors in \(\delta\).

For a supercuspidal, choose a basis of \(V^J\) and its pairing-dual \(J\)-fixed smooth functionals, using Lesson 5's fixed-space duality. The finitely many resulting coefficients have support in one compact set modulo \(Z\), by Lesson 6. But \(p(d^N)\) escapes every such compact set by Lemma 7.1. For all sufficiently large \(N\), every matrix entry of
\(E_J\pi(d^N)E_J|_{V^J}\) is consequently zero. Equation (7.2) proves nilpotence. The trace of a nilpotent finite-dimensional operator is zero. \(\square\)

**Theorem 7.3 — supercuspidal character support.** For every nonarchimedean local field \(F\), in either characteristic and every residue characteristic,
\[
\operatorname{supp}\Theta_\pi\ \subset\ p^{-1}(C_{\mathrm{ad}})
\]
for every admissible supercuspidal \(\pi\).

**Proof.** We must prove vanishing on a neighborhood of each noncompact adjoint element, rather than only calculate one double-coset trace. By conjugation, scalar translation and Lemma 7.1, reduce that element to
\(g=d(a)\), with \(v(a)=r>0\). Scalar translation multiplies the character by its central-character value, which does not affect vanishing.

Choose \(M\ge1\), and consider the compact open neighborhood \(gK(M)\). Every element
\[
h=gk=
 \begin{pmatrix}a(1+u)&av\\ w&1+t\end{pmatrix},
\qquad u,v,w,t\in\mathfrak p^M,
\]
has two distinct eigenvalues in \(F\), of valuations \(r,0\), and can be diagonalized by an element of \(K(M)\). Here are the details. Its characteristic polynomial modulo \(\mathfrak p^M\) is
\((X-a)(X-1)\); at \(X=1\) its derivative is congruent to \(1-a\), a unit. The elementary Hensel iteration therefore gives a root
\(\lambda_2\in1+\mathfrak p^M\). One can see this iteration directly: correct the root by \(-P(x)/P'(x)\); its error valuation doubles while its derivative remains a unit, so the complete-field sequence converges. The other root is
\(\lambda_1=\det h/\lambda_2\), of valuation \(r\).
Their difference is a unit. The eigenvectors
\[
\binom{1}{-h_{21}/(h_{22}-\lambda_1)},\qquad
\binom{h_{12}/(\lambda_2-h_{11})}{1}
\]
form an invertible matrix \(s_h\in K(M)\), and
\(h=s_h\operatorname{diag}(\lambda_1,\lambda_2)s_h^{-1}\).
No division by two or separability assumption on other elements has entered this calculation.

Let \(f\) be any locally constant compactly supported test with support in \(gK(M)\). Choose \(\ell\ge M+r\) so large that \(f\) is bi-invariant under \(J=K(\ell)\). This is possible by compactness of its support and local constancy. Its support is a finite union of double cosets \(JhJ\) on which it is constant. Each representative \(h\) is in \(gK(M)\). Since \(J\) is normal in \(K\), the diagonalizer \(s_h\in K(M)\) preserves it. Lemma 7.2 and conjugation therefore make
\(E_J\pi(h)E_J|_{V^J}\) nilpotent.

The normalized compact measure \(e_J*\delta_h*e_J\) is the constant density of total mass one on \(JhJ\). Hence \(\pi(1_{JhJ})\) is the positive scalar
\(\operatorname{vol}(JhJ)\) times this compressed operator and has trace zero. Every term of the finite double-coset expansion of \(f\) has trace zero. Thus \(\Theta_\pi(f)=0\) for every test supported in this neighborhood. It follows that no element outside \(p^{-1}(C_{\mathrm{ad}})\) belongs to the distribution support. \(\square\)

Deligne's 1976 note, *Le support du caractère d'une représentation supercuspidale*, §2, proves the more general reductive-group theorem. The argument here supplies its complete GL₂ specialization with explicit principal-congruence cosets and nearby eigenvectors; the cited note retains the historical credit.

This union is not one fixed compact subgroup, nor a claim that the character distribution has compact support modulo \(Z\). The proof says that an element outside all compact adjoint subgroups has a neighborhood on which the distribution vanishes. An elliptic regular element lies in a compact adjoint field torus, so the theorem permits a nonzero character there. This is the support distinction needed in the quaternionic comparison.


## 8. Exercises with complete solutions

**Exercise 8.1 — admissibility with the stated hypotheses.** Prove admissibility of the irreducible compact induction in Theorem 2.1. For the depth-zero induction (3.3), give a direct fixed-space proof. Explain why the conclusion fails without these hypotheses.

**Solution 8.1.** Under \(I_G(\tau)=J\), the algebraic argument in Theorem 2.1 proves irreducibility. The admissibility theorem for irreducible smooth \(\mathrm{GL}_2(F)\)-representations, isolated in Lesson 5, then applies.

For (3.3), fix \(m\geq1\). Decompose the support of a \(K(m)\)-fixed function into \(J\backslash G/K(m)\). A value at \(g_nk\) must be fixed by
\(J\cap g_nkK(m)k^{-1}g_n^{-1}=J\cap g_nK(m)g_n^{-1}\).
If \(n\geq m\), every \(l(u)\), \(u\in\mathcal O\), is in this intersection, since \(g_n^{-1}l(u)g_n=l(\varpi^n u)\in K(m)\). The finite cuspidal representation has no invariants under the reduction of this lower unipotent group, so the value vanishes. There remain fewer than \(m[K:K(m)]\) possible cosets, each with values in finite-dimensional \(T\). Thus
\(\dim V^{K(m)}\leq m[K:K(m)]\dim T<\infty\).
For any compact open \(L\), choose \(m\) with \(K(m)\subset L\); then \(V^L\subset V^{K(m)}\), proving admissibility.

For \(\mathrm{c\!-\!Ind}_{ZK}^{G}1\), the infinitely many Cartan double-coset indicators are independent \(K\)-fixed vectors, as computed in Section 1. Hence an unconditional claim for arbitrary compact induction would be false. \(\square\)

**Exercise 8.2 — the first Cartan intertwining.** Compute the intertwining of the inflated cuspidal representation at \(g=d(\varpi)\).

**Solution 8.2.** On \(K\), the intersection \(H_g=J\cap gJg^{-1}\) has upper-right entry in \(\mathfrak p\), with no extra divisibility restriction on its lower-left entry. It contains \(l(u)\) for \(u\in\mathcal O\). Conjugation gives
\(g^{-1}l(u)g=l(\varpi u)\), which acts trivially in \(\widetilde\tau^g\).
If \(B\) intertwines on \(H_g\), then
\[
B\widetilde\tau(l(u))=\widetilde\tau^g(l(u))B=B.
\]
Consequently
\[
B=B\left(\frac1q\sum_{\bar u\in k}\tau_0(l(\bar u))\right)=0.
\]
The parenthesized operator is the projection onto lower-unipotent invariants, and that space is zero. Thus the intertwining Hom space is zero, not merely a scalar endomorphism space. The same computation with \(\varpi^n\) proves vanishing at every \(g_n\), \(n\geq1\). \(\square\)

**Exercise 8.3 — central character and conductor.** Compute both for the depth-zero induction attached to \(\tau_\theta\) and the chosen scalar action \(A\).

**Solution 8.3.** A scalar \(z=\varpi^r u\) acts by right translation:
\(f(xz)=f(zx)=\widetilde\tau(z)f(x)\).
The finite central character gives
\[
\omega_\pi(\varpi^r u)=A^r\theta(\bar u).
\]
In particular its unit restriction is tame; its value at \(\varpi\) is the freely chosen \(A\).

For the conductor, supercuspidality and Lesson 8 give the lower bound two. Conjugating \(K_1(2)\) by \(g_1=d(\varpi)\) gives (4.1), whose reduction is exactly \(D\). Cuspidality of \(\tau_\theta\) excludes the trivial upper-unipotent character. Since \(D\) acts transitively on the other \(q-1\) character eigenspaces, those eigenspaces have the same dimension. Their total dimension is \(q-1\), so each has dimension one. The sum of a \(D\)-orbit of a nonzero eigenvector is a nonzero \(D\)-fixed vector \(v\).

Place \(v\) at \(g_1\), and extend by left \(J\)-covariance and right \(K_1(2)\)-invariance on \(Jg_1K_1(2)\), taking zero elsewhere. The intersection condition just computed makes this a well-defined finite-support function. It is a nonzero \(K_1(2)\)-fixed vector. Thus \(c(\pi)\leq2\), and equality follows. This computation is independent of \(A\). \(\square\)

**Exercise 8.4 — algebraic Mackey irreducibility.** Prove the criterion \(I_G(\tau)=J\Rightarrow\mathrm{c\!-\!Ind}_J^G\tau\) irreducible.

**Solution 8.4.** A function supported on \(Jg^{-1}J\), restricted to \(g^{-1}J\), has covariance \(\tau^g\) under \(H_g=J\cap gJg^{-1}\). This identifies its \(J\)-module with \(\operatorname{Ind}_{H_g}^J\tau^g\); the index is finite because \(H_g/Z\) is open in compact \(J/Z\). Taking Hom from the finite-dimensional \(\tau\), and using evaluation Frobenius reciprocity, gives (2.3). Under the hypothesis only the identity term survives, with multiplicity one. Thus the entire \(\tau\)-isotypic part is the base copy \(V[J]\).

With the common central character fixed, averaging on \(J/Z\) is defined. Complete reducibility and the matrix-unit orthogonality argument of Section 2 make \(P_\tau\) in (2.5) an algebraic projector onto \(V[J]\). For a nonzero invariant subspace \(A\), choose \(f\in A\) with some nonzero value, and translate that value to one. Evaluation at one is a \(J\)-map into \(\tau\), so it is unchanged by \(P_\tau\). Hence \(A\) contains a nonzero vector of \(V[J]\). The \(J\)-action then supplies all of this irreducible copy. Its translates span all single-coset functions and hence all of the compact induction. Therefore \(A=V\).

This proves irreducibility on the smooth algebraic space itself. No density argument from an irreducible Hilbert completion is substituted for it. The subsequent admissibility, smooth-dual identification and compact-coefficient argument give supercuspidality as in Theorem 2.1. \(\square\)

## 9. Proof boundaries and exact source locators

The finite-group construction and character theorem in (5.1) are the proved prerequisite Representations of GL₂ over finite fields, Lemma 3.1, equation (13), and Theorem 4.1. Its proof constructs the character by finite-group induction and verifies irreducibility and cuspidality, so these facts need no external proof substitute. The checked original geometric references are Deligne–Lusztig (1976), Theorem 4.2, printed p. 124; Theorem 7.1, p. 140; Corollary 7.2 and Proposition 7.4, p. 141; Theorem 8.3, p. 147; and Theorem 9.16, p. 153. The local construction and the finite unipotent/diagonal invariant calculations are proved here.

Section 6 proves the quadratic-extension Weil construction and every property in Jacquet–Langlands, Lemma 1.2(iv), Propositions 1.3/1.5 and Theorems 4.6(i)–(iv)/4.7(i)–(iii). Lemma 6.1 supplies the required full character Fourier calculation in both local characteristics, including all conductor powers, finite Gauss sums and arbitrary additive choices; the proof is not limited to characteristic zero. The norm Gaussian, exact Bruhat relation, small-unit smoothness, scalar mirabolic models, regular and norm-factor irreducibility, central character, auxiliary-choice independence, symmetries and full zeta ideals are proved here. Only the cyclic norm-index and norm-openness prerequisite remains in its exact owning lesson, linked in Section 6. No compact-induction exhaustion or local Langlands parametrization is used in these proofs.

Section 7.1 proves the full compact-induction exhaustion theorem, including all positive and residue characteristics. Its compact-filtration selection, Iwahori obstruction, split-character averaging contradiction, exact elliptic intertwining set and irreducible induction argument are given in Lemmas 7.4–7.7 and Theorem 7.8. The exhaustion is due to Kutzko; a counting proof for general linear groups of prime rank, in characteristic zero, is Carayol 1984, Théorème 8.1. Section 7.2 proves the identification of every odd-residue supercuspidal with a quadratic Weil model in Lemmas 7.9–7.10, Theorem 7.11, Lemma 7.12 and Theorem 7.13. Lemma 6.6 proves the required fixed-field injectivity directly from the Weyl kernel. The vector, finite Heisenberg extension and complete type counts are supplied here, including the ramified valuation factor of two; no parameter correspondence is imported. The historical odd-residue statement is [Kutzko (1984)](https://www.numdam.org/item/CM_1984__51_1_3_0.pdf), Corollary 4.3, p. 14. Theorem 7.14 proves the residue-two qualification by an explicit supercuspidal over Q₂ with no nontrivial quadratic determinant self-twist: all seven possible quadratic characters are excluded by compact intertwining, a torus sign, and disjoint determinant cosets. Every quadratic Weil model has the index-two norm self-twist, so the example is not quadratic. No exceptional-classification theorem is imported. All substantive local results required in this lesson have their own proofs, with the finite-field prerequisite retained at its exact written locators.

Section 7 proves the full GL₂ distribution-character support theorem in either characteristic, independently of the compact-induction exhaustion proof. The compact-element criterion includes inseparable quadratic field algebras, and an explicit principal-congruence double-coset identity makes the split positive operator nilpotent. The nearby-eigenvector/Hensel calculation and finite double-coset expansion prove vanishing on a whole neighborhood. Deligne, §2, **THÉORÈME**, printed p. 156, retains historical credit for the general reductive-group support theorem; its generality beyond GL₂ is not claimed here.

The general compact-induction theorem also uses the smooth admissibility theorem proved in Lesson 6, Theorem 5.4, with its original reference Getz–Hahn, Theorem 5.3.4. Its smooth dual argument is Lesson 5, Theorem 5.2, and compact coefficients imply vanishing Jacquet module by the proved Lesson 6, Theorem 5.2. The direct depth-zero admissibility proof and conductor-two vector require no new admissibility or conductor theorem.

Bibliographic authorities are:

- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf) (1970), §§1 and 4, with the exact result numbers above. In the consulted retypeset PDF, the Weil constants/operators are on PDF pp. 8–14, Theorem 4.6 on PDF p. 77, and Theorem 4.7 on PDF p. 81. Theorems 4.2–4.3 in that section concern the quaternion-algebra construction, and are not mislabeled here as quadratic-extension results.
- P. Deligne and G. Lusztig, [*Representations of reductive groups over finite fields*](https://publications.ias.edu/sites/default/files/Number27.pdf), Annals of Mathematics **103** (1976), 103–161, with the finite-input locators above.
- P. C. Kutzko, [*The exceptional representations of Gl2*](https://www.numdam.org/item/CM_1984__51_1_3_0/), Compositio Mathematica **51** (1984), 3–14.
- P. Deligne, [*Le support du caractère d'une représentation supercuspidale*](https://publications.ias.edu/sites/default/files/31_LeSupport.pdf), C. R. Acad. Sci. Paris, Série A **283** (1976), 155–157.
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), consulted 2022 draft, §8.1 for local representation context and §8.5 for distribution characters and coefficients. These sections are not used as an unlocated substitute for a depth-zero construction proof.

- P. Gérardin and P. Kutzko, [*Facteurs locaux pour GL(2)*](https://www.numdam.org/articles/10.24033/asens.1386/), Annales scientifiques de l’École Normale Supérieure **13** (1980), 349–384, Section 5.3, pp. 373–374.
- H. Carayol, [*Représentations cuspidales du groupe linéaire*](https://www.numdam.org/item/ASENS_1984_4_17_2_191_0/), Annales scientifiques de l'École normale supérieure **17** (1984), 191–225, Théorème 8.1. The complete compact-exhaustion argument is supplied here in Section 7.1.
