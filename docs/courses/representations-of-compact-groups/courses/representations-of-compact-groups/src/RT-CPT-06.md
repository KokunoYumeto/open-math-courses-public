# Tori and the maximal torus theorem

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

A unitary matrix can be diagonalized by a unitary change of basis. The maximal torus theorem extends this phenomenon to every compact connected Lie group. A fixed torus supplies all elements up to conjugacy, and all maximal choices of that torus are equivalent.

Throughout, \(G\) is a compact connected Lie group, \(\mathfrak g\) is its real Lie algebra, and a **torus** is a compact connected abelian Lie group, including the trivial group. A torus in \(G\) means a closed subgroup with those properties. We import the exponential, closed subgroup theorem, differentiation and invariant inner product from [Compact Lie groups and their Lie algebras](RT-CPT-05.md). The geometric imports have the exact complete internal proof homes below; **D50** gives geometric orientation. The Kronecker import from **HA-LCA-12** is stated precisely where used.

## The exponential lattice of a torus

**Proposition 1.1.** A torus \(T\) of dimension \(r\) is isomorphic as a Lie group to \(\mathbb R^r/\mathbb Z^r\). More intrinsically, if \(\mathfrak t=\operatorname{Lie}(T)\), then
\[
T\simeq\mathfrak t/\Lambda,\qquad
\Lambda=\ker(\exp:\mathfrak t\to T),
\]
where \(\Lambda\) is a full lattice. Its continuous characters are exactly
\[
\chi_\ell(\exp X)=e^{2\pi i\ell(X)},\qquad
\ell\in\Lambda^*=\{\ell\in\mathfrak t^*:\ell(\Lambda)\subset\mathbb Z\}. \tag{1.2}
\]
In particular \(X^*(T)\simeq\mathbb Z^r\), and \(T\) has an element whose integer powers are dense.

*Proof.* Since \(\mathfrak t\) is abelian, commuting one-parameter subgroups give \(\exp(X+Y)=\exp X\exp Y\). Its image is a subgroup containing an identity neighborhood. Connectedness makes this image all of \(T\). Local injectivity of the exponential makes \(\Lambda\) discrete, and its quotient map is a local diffeomorphism. It induces the stated Lie-group isomorphism with \(\mathfrak t/\Lambda\).

Here is a direct lattice proof. In the real span \(W\) of the closed discrete subgroup \(\Lambda\), a bounded set meets \(\Lambda\) finitely. If \(\Lambda\neq\{0\}\), choose a nonzero element \(\lambda_1\) of shortest length. Then \(\Lambda\cap\mathbb R\lambda_1=\mathbb Z\lambda_1\): subtract an integer multiple to leave a shorter remainder on that line. Orthogonally project to \(\lambda_1^\perp\). The projected subgroup is discrete. Otherwise it would contain distinct nonzero points tending to zero; lift them to \(\Lambda\), and subtract multiples of \(\lambda_1\) so their parallel coordinates lie in \([0,1]\lambda_1\). These distinct lifts lie in a bounded set, a contradiction. A discrete subgroup of a vector space is closed, since sufficiently close elements have difference in an identity neighbourhood containing no nonzero subgroup point.

Induct on \(\dim W\) for the projected subgroup, whose real span has dimension one less. Lift its integer basis to \(\lambda_2,\ldots,\lambda_s\in\Lambda\). Every element of \(\Lambda\) differs from an integer combination of these lifts by an element of \(\mathbb Z\lambda_1\). Independence of the projected basis and then of \(\lambda_1\) proves that these vectors are also real-linearly independent. The trivial subgroup supplies the induction base. Thus \(\Lambda=\sum_{j=1}^s\mathbb Z\lambda_j\), with \(s=\dim W\). If \(W\neq\mathfrak t\), the continuous surjection
\[
\mathfrak t/\Lambda\longrightarrow\mathfrak t/W
\]
would map a compact space onto a nonzero real vector space. Hence \(s=r\). Sending a lattice basis to the standard basis gives \(\mathbb R^r/\mathbb Z^r\).

A continuous character \(\chi:T\to S^1\) is smooth by Lemma 4.1 of the preceding lesson. Its derivative is \(2\pi i\ell\) for a real linear functional \(\ell\), and differentiation of homomorphisms gives (1.2). This descends through \(\Lambda\) exactly when \(\ell(\Lambda)\subset\mathbb Z\). Conversely every such functional defines a character, proving the classification.

For the last assertion we import [**HA-LCA-12, Theorem 6.1 (Kronecker)**](course:HA-LCA/HA-LCA-12#section-6): the integer multiples of \(a+\mathbb Z^r\) are dense in \(\mathbb R^r/\mathbb Z^r\) exactly when \(1,a_1,\ldots,a_r\) are linearly independent over \(\mathbb Q\). Such a tuple exists by choosing each coordinate outside the countable rational span of the previous ones and \(1\). Its image in \(T\) is a topological generator. For \(r=0\) the identity is a generator. \(\square\)

One useful consequence is that there is \(Y\in\mathfrak t\) with
\[
\overline{\{\exp(tY):t\in\mathbb R\}}=T. \tag{1.3}
\]
Choose any logarithm of a topological generator: its one-parameter subgroup contains all integer powers of that generator. The lattice and dual lattice are different objects; the factor \(2\pi\) in (1.2) fixes their normalization.

The exact Kronecker provider proves this criterion using double annihilators. There is also a proof using just the compact results already established here. Let \(K\) be the closure of the powers of \(a+\mathbb Z^r\). If no nonzero \(m\in\mathbb Z^r\) has \(m\cdot a\in\mathbb Z\), every nonconstant torus character has nontrivial restriction to \(K\). Translation invariance makes its Haar integral on \(K\) zero: translate by a point where its value differs from one. Its integral on the whole torus is zero too; the constant has integral one on both. The character polynomials are dense in continuous functions by Peter–Weyl in lesson two. Thus the two probability integrals agree on every continuous function. If \(K\) were proper, a nonnegative continuous function supported in its nonempty open complement, positive at one point, would have positive torus integral and zero \(K\)-integral, a contradiction. Conversely a nonzero \(m\) with \(m\cdot a\in\mathbb Z\) puts \(K\) in the proper kernel of its character. Clearing denominators gives precisely the rational independence criterion, including the empty tuple when \(r=0\).

## Maximal abelian subalgebras

A maximal abelian subalgebra means one maximal by inclusion. Such subalgebras exist by finite dimensionality, and any abelian subalgebra extends to one.

**Lemma 2.1.** Maximal tori in \(G\) are exactly the groups \(\exp\mathfrak t\) for maximal abelian subalgebras \(\mathfrak t\subset\mathfrak g\). These exponentials are closed. Every torus is contained in a maximal torus.

*Proof.* If \(\mathfrak t\) is maximal abelian, \(\exp\mathfrak t\) is a connected abelian subgroup. Its closure \(A\) is compact, connected and abelian. By the closed subgroup theorem it is a torus. Its abelian Lie algebra contains \(\mathfrak t\), and therefore equals \(\mathfrak t\) by maximality. Proposition 1.1 gives \(A=\exp\mathfrak t\), proving closedness and maximality.

Conversely, if \(T\) is a maximal torus, extend \(\operatorname{Lie}(T)\) to a maximal abelian subalgebra \(\mathfrak a\). The preceding construction gives a torus \(\exp\mathfrak a\) containing \(T=\exp\operatorname{Lie}(T)\), so equality holds. Applying the same argument to any torus proves the last assertion. \(\square\)

Fix henceforth a maximal abelian \(\mathfrak t\) and its maximal torus \(T\). For a subset of the Lie algebra, a centralizer consists of the vectors commuting with every vector in that subset. Maximality gives
\[
\mathfrak z_{\mathfrak g}(\mathfrak t)=\mathfrak t: \tag{2.2}
\]
if \(X\) commutes with \(\mathfrak t\), then \(\mathfrak t+\mathbb RX\) is abelian.

**Lemma 2.3 (a regular vector).** There exists \(Y\in\mathfrak t\) such that \(\mathfrak z_{\mathfrak g}(Y)=\mathfrak t\).

*Proof.* Use the invariant inner product from the preceding lesson. The operators \(\operatorname{ad}_H\), \(H\in\mathfrak t\), commute and are skew-adjoint. On \(\mathfrak g_{\mathbb C}\) they can be simultaneously diagonalized: diagonalize one normal operator; its eigenspaces are preserved by the others, and repeat on those eigenspaces for a basis of \(\mathfrak t\). Thus there is a finite joint eigenspace decomposition on which
\[
\operatorname{ad}_H=i\,a(H)
\]
for real linear functionals \(a\) on \(\mathfrak t\). The joint zero eigenspace is \(\mathfrak t_{\mathbb C}\) by (2.2). Choose \(Y\) outside the kernels of all the nonzero \(a\)'s. A finite union of proper real hyperplanes cannot fill a real vector space; for example the product of their nonzero defining linear polynomials is not the zero polynomial. Then precisely the joint zero eigenspace is killed by \(\operatorname{ad}_Y\). Taking real parts proves the assertion. If there are no nonzero eigenfunctionals, \(\mathfrak g=\mathfrak t\) and any \(Y\) works. \(\square\)

This genericity argument needs no previously established root system and works with an arbitrary centre.

**Theorem 2.4 (Lie-algebra conjugacy).** Every \(X\in\mathfrak g\) is \(\operatorname{Ad}(G)\)-conjugate into \(\mathfrak t\). All maximal abelian subalgebras are conjugate.

*Proof.* Choose \(Y\) as in Lemma 2.3. The continuous function
\[
f(g)=\langle\operatorname{Ad}_gX,Y\rangle
\]
attains a maximum, say at \(g_0\). Put \(X'=\operatorname{Ad}_{g_0}X\). For every \(Z\in\mathfrak g\), differentiating \(f(\exp(tZ)g_0)\) gives
\[
0=\langle[Z,X'],Y\rangle=\langle Z,[X',Y]\rangle.
\]
Nondegeneracy implies \([X',Y]=0\), and hence \(X'\in\mathfrak t\).

For another maximal abelian subalgebra \(\mathfrak t'\), choose a regular \(Y'\in\mathfrak t'\) by the same lemma. Conjugate it into \(\mathfrak t\). Its centralizer is the corresponding conjugate of \(\mathfrak t'\) and contains \(\mathfrak t\). Both are maximal abelian, so they are equal. \(\square\)

## Why every element has a logarithm

We use [*Riemannian connections and convex neighbourhoods*, Theorem 2.1](course:DG-FND/riemannian-connections-and-convex-neighbourhoods#section-2), the complete Levi–Civita and Koszul proof, and [*Completeness and the Hopf–Rinow theorem*, Theorem 3.1 and Corollary 3.2](course:DG-FND/completeness-and-the-hopf-rinow-theorem#section-3). The latter proves all four completeness equivalences for every connected Riemannian manifold, as well as minimizing geodesics and compact-manifold completeness. In the present setting their use is as follows. An \(\operatorname{Ad}(G)\)-invariant positive inner product on \(\mathfrak g\), translated on the left, defines a bi-invariant Riemannian metric. For this metric the Levi–Civita connection on left-invariant vector fields satisfies
\[
\nabla_XY=\tfrac12[X,Y], \tag{3.1}
\]
Indeed, for left-invariant fields all three derivatives of their metric pairings in the Koszul formula vanish. Adjoint invariance converts its three bracket terms into \(\langle[X,Y],Z\rangle\), giving (3.1). Therefore \(\nabla_XX=0\), so \(t\mapsto\exp(tX)\) is the geodesic with initial velocity \(X\). We also import **Hopf–Rinow**: any two points of a connected complete finite-dimensional Riemannian manifold are joined by a minimizing geodesic. A compact Riemannian manifold is complete.

**Theorem 3.2 (surjectivity of the exponential).** The map \(\exp:\mathfrak g\to G\) is onto.

*Proof.* The invariant inner product exists by compact averaging. Its bi-invariant metric is complete since \(G\) is compact. For \(g\in G\), Hopf–Rinow supplies a geodesic from \(e\) to \(g\); parametrize it on \([0,1]\) and let \(X\) be its initial velocity. Formula (3.1) and uniqueness of a geodesic with prescribed initial data identify it with \(\exp(tX)\). Thus \(g=\exp X\). \(\square\)

This proof uses connectedness to join the two points and compactness for both the invariant positive metric and completeness.

**Theorem 3.3 (maximal torus theorem).** Every element of \(G\) lies in a maximal torus, and any two maximal tori are conjugate.

*Proof.* Write \(g=\exp X\). By Theorem 2.4 there is \(h\in G\) with \(\operatorname{Ad}_hX\in\mathfrak t\). Naturality of the exponential gives
\[
hgh^{-1}=\exp(\operatorname{Ad}_hX)\in T.
\]
Thus \(g\) belongs to \(h^{-1}Th\), a maximal torus. Lie-algebra conjugacy and Lemma 2.1 already imply conjugacy of all maximal tori.

There is also a purely group-theoretic final step: if \(T'\) is a maximal torus, choose its topological generator \(t'\). The first assertion puts \(t'\) in some \(hTh^{-1}\). Closedness then puts the closure of its integer powers, namely \(T'\), in that torus. Maximality makes the inclusion an equality. \(\square\)

The common dimension of the maximal tori is the **rank** of \(G\).

## Connected centralizers of tori

For \(Y\in\mathfrak g\), write \(C_G(Y)=\{g:\operatorname{Ad}_gY=Y\}\). For a subgroup \(S\), write \(C_G(S)=\{g:gs=sg\text{ for every }s\in S\}\).

**Lemma 4.1.** Every element of \(C_G(Y)\) has a logarithm commuting with \(Y\). In particular \(C_G(Y)\) is path connected.

*Proof.* Let \(g\in C_G(Y)\). Choose \(X\in\mathfrak g\) with \(\exp X=g\), using Theorem 3.2. Consider the compact group
\[
C=C_G(g)=\{h:hg=gh\},\qquad
\mathfrak c=\{Z:\operatorname{Ad}_gZ=Z\}.
\]
The displayed Lie-algebra equality follows by exponentiating a fixed vector and conversely differentiating commutation. Both \(X\) and \(Y\) belong to \(\mathfrak c\): \(X\) commutes with its own exponential and \(g\) fixes \(Y\).

Maximize \(\langle\operatorname{Ad}_hX,Y\rangle\) over \(h\in C\), and call the maximizing vector \(X'\). It still lies in \(\mathfrak c\), and \(\exp X'=g\), because \(h\) commutes with \(g\). Differentiation along \(\exp(tZ)\), for \(Z\in\mathfrak c\), gives
\[
\langle Z,[X',Y]\rangle=0\qquad(Z\in\mathfrak c).
\]
Since \(\mathfrak c\) is a Lie subalgebra and contains \(X',Y\), their bracket also belongs to \(\mathfrak c\). Positive definiteness therefore forces that bracket to be zero. The path \(t\mapsto\exp(tX')\) joins \(e\) to \(g\) inside \(C_G(Y)\). Notice that no connectedness of \(C_G(g)\) was assumed. \(\square\)

**Theorem 4.2.** The centralizer of any torus \(S\subset G\) is connected. For a maximal torus \(T\),
\[
C_G(T)=T,\qquad Z(G)\subset T. \tag{4.3}
\]
Thus the centre is contained in every maximal torus.

*Proof.* Choose \(Y\in\operatorname{Lie}(S)\) whose one-parameter subgroup is dense in \(S\), as in (1.3). Commutation with that subgroup, followed by closure, shows
\[
C_G(S)=C_G(Y).
\]
Conversely commutation with \(S\) differentiates to fixing \(Y\). Lemma 4.1 proves connectedness. Its Lie algebra is \(\mathfrak z_{\mathfrak g}(\operatorname{Lie}(S))\), by differentiation and exponentiation.

For maximal \(T\), this Lie algebra is \(\mathfrak t\) by (2.2). More explicitly Lemma 4.1 gives each \(g\in C_G(T)\) a logarithm in this centralizer algebra, so \(g\in\exp\mathfrak t=T\). The opposite inclusion is immediate. Every central element commutes with \(T\), giving (4.3). Apply the same proof to each maximal torus. \(\square\)

The distinction between a torus and a single group element matters. In \(SO(3)\), let \(g=\operatorname{diag}(1,-1,-1)\), the half-turn about the first axis. Its centralizer consists of
\[
\operatorname{diag}(\det A,A),\qquad A\in O(2).
\]
Indeed a commuting orthogonal matrix preserves the two eigenspaces of \(g\); determinant one fixes the first block as displayed. This centralizer has two components. The centralizer of the **entire** axis-rotation torus is its connected circle of rotations.

## Classical maximal tori

In \(U(n)\), the diagonal unitary matrices form a maximal torus of rank \(n\). Commuting with every diagonal matrix forces a skew-Hermitian matrix to be diagonal, so its Lie algebra is maximal abelian. The maximal torus theorem here is exactly unitary diagonalization. In \(SO(3)\), the rotations about a fixed axis form a maximal torus of rank one; every rotation is conjugate to one about that axis.

**Exercise 1 (easy).** Describe maximal tori and ranks in \(SU(n),SO(2n),SO(2n+1),Sp(n)\).

*Solution.* Let
\[
R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta\end{pmatrix}.
\]
Representative tori are
\[
\begin{aligned}
SU(n):&\quad \operatorname{diag}(z_1,\ldots,z_n),\
|z_j|=1,\ \prod z_j=1,\\
SO(2n):&\quad \operatorname{diag}(R(\theta_1),\ldots,R(\theta_n)),\\
SO(2n+1):&\quad \operatorname{diag}(R(\theta_1),\ldots,R(\theta_n),1),\\
Sp(n):&\quad \operatorname{diag}(z_1,\ldots,z_n,\overline z_1,\ldots,\overline z_n),\
|z_j|=1.
\end{aligned} \tag{5.1}
\]
Their dimensions are respectively \(n-1,n,n,n\). To verify maximality, it suffices to show that the Lie centralizer of each displayed torus is its own Lie algebra.

For \(SU(n)\), the coordinate characters \(z_j\) are distinct when \(n\geq2\), including the pair \(z,z^{-1}\) when \(n=2\). Thus a commuting matrix is diagonal, and the skew-Hermitian trace-zero condition gives exactly the torus algebra. For \(n=1\) the group is trivial and the rank is zero.

For the two orthogonal groups, complexify their defining real representation. Each plane has two one-dimensional eigenspaces with characters \(e^{i\theta_j}\) and \(e^{-i\theta_j}\); in odd dimension there is also a one-dimensional zero-weight axis. These characters are all distinct functions on the torus. A commuting complex matrix preserves every line. Reality and skew-symmetry force its restriction to each real plane to be an infinitesimal rotation and its restriction to the possible real axis to be zero. These are precisely the block-rotation Lie algebras.

For \(Sp(n)\), use the blocks \(A,B\) in (2.3) of the preceding lesson. Conjugation by \(\operatorname{diag}(D,\overline D)\) sends them to \(DAD^{-1}\) and \(DBD^t\). Invariance under all independent \(z_j\)'s forces \(A\) to be diagonal and \(B=0\), since even the factor on \(B_{jj}\) is \(z_j^2\), a nontrivial character. Thus the centralizer algebra is exactly the \(n\)-dimensional imaginary diagonal one. Lemma 2.1 now proves maximality in every case.

**Exercise 2 (medium).** Give the full genericity argument for a regular \(Y\in\mathfrak t\), including the abelian case.

*Solution.* Choose a real basis \(H_1,\ldots,H_r\) of \(\mathfrak t\). The normal commuting matrices \(\operatorname{ad}_{H_j}\) on \(\mathfrak g_{\mathbb C}\) have finitely many joint eigenvalue tuples \((ia_1,\ldots,ia_r)\), with real \(a_j\). For \(Y=\sum y_jH_j\), the corresponding eigenvalue is \(i\sum a_jy_j\). Each nonzero tuple forbids just one proper hyperplane. Choose a point outside their finite union; its kernel consists only of the simultaneous zero eigenspace. By (2.2) that eigenspace is \(\mathfrak t_{\mathbb C}\), so the real centralizer is \(\mathfrak t\). If every tuple is zero, all \(\operatorname{ad}_{H_j}\) vanish, and (2.2) forces \(\mathfrak g=\mathfrak t\); any vector, including zero, then has the required centralizer.

**Exercise 3 (medium).** Prove \(C_G(T)=T\) while explicitly avoiding an assumption about centralizers of individual group elements.

*Solution.* Pick \(Y\in\mathfrak t\) with dense one-parameter subgroup. Then \(C_G(T)=C_G(Y)\). For \(g\) in this group, take a logarithm \(X\) of \(g\). The compact group \(C_G(g)\) may be disconnected, but this does not obstruct maximizing \(\langle\operatorname{Ad}_hX,Y\rangle\) on it. Both the maximizing \(X'\) and \(Y\) belong to its Lie algebra \(\mathfrak c\). Stationarity against every \(Z\in\mathfrak c\), together with \([X',Y]\in\mathfrak c\), proves \([X',Y]=0\), exactly as in Lemma 4.1. It follows that \(X'\) commutes with all of \(\mathfrak t\), because \(\exp(tY)\) is dense in \(T\). By maximality \(X'\in\mathfrak t\). Therefore \(g=\exp X'\in T\). Conversely every element of \(T\) commutes with \(T\). The argument needs neither \(C_G(g)\) connected nor \(C_G(g)=T\).

**Exercise 4 (hard).** Show that
\[
A=-\begin{pmatrix}1&1\\0&1\end{pmatrix}\in SL(2,\mathbb R)
\]
is not an exponential, and identify the failure of Theorem 3.2's proof.

*Solution.* If \(e^X=A\), then \(X\) commutes with \(A\). Solving \(XA=AX\) gives
\[
X=\begin{pmatrix}a&b\\0&a\end{pmatrix},\qquad a,b\in\mathbb R.
\]
For \(X\in\mathfrak{sl}_2(\mathbb R)\), trace zero forces \(a=0\), so \(e^X=\begin{pmatrix}1&b\\0&1\end{pmatrix}\), contradicting the diagonal entries of \(A\). In fact there is no real \(2\times2\) logarithm at all: \(\det e^X=e^{\operatorname{tr}X}=1\) would again force the real trace to be zero.

The group \(SL(2,\mathbb R)\) is connected: polar decomposition writes a matrix as a rotation times a positive definite symmetric determinant-one matrix, and each factor has a path to the identity, the latter via its real symmetric logarithm. But it is not compact. There is no positive definite adjoint-invariant metric on its Lie algebra: for \(H=\operatorname{diag}(1,-1)\), \(\operatorname{ad}_H(E_{12})=2E_{12}\), a nonzero real eigenvalue impossible for a skew-adjoint operator. Thus the bi-invariant Riemannian construction used to identify all geodesics through \(e\) with one-parameter subgroups is unavailable. Connectedness alone does not supply the required logarithm.

## Sources and unproved inputs

The geometric inputs in Section 3 are the exact internal Levi–Civita and Hopf–Rinow proofs linked there; the bi-invariant metric formula is derived from Koszul above. The Kronecker criterion in Proposition 1.1 is [HA-LCA-12, Theorem 6.1](course:HA-LCA/HA-LCA-12#section-6), and the compact argument is also supplied above. These inputs are not reproved.

The simultaneous spectral argument above establishes the regular vector directly for every compact connected \(G\), and the geometric logarithm proof is supplied explicitly. For the algebraic analogue, Milne, *Algebraic Groups*, Sections 12a–e treats characters and algebraic tori; Theorem 17.10 proves conjugacy of maximal tori, and Theorem 17.38 proves connectedness of their centralizers. Our compact analytic proofs use Haar averaging and Riemannian geometry rather than importing those algebraic theorems.

The next lesson studies the finite symmetry group that remains after choosing \(T\), then the roots describing the nonzero eigenspaces of its adjoint action.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §§35–36. Compact unitarity and finite-dimensional compact Lie representations supply context for the adjoint metric. The torus lattice, conjugacy and geometric arguments above retain their own proofs and exact programme providers.
