# The root space decomposition of a semisimple Lie algebra

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Commuting diagonalizable adjoint operators separate a Lie algebra into simultaneous eigenspaces. The bracket adds their eigenvalues. Each pair of opposite nonzero eigenspaces then supplies a copy of \(\mathfrak{sl}_2\). Its finite-dimensional representation theory forces the eigenspaces to be lines, arranges them in strings and supplies reflections. Finally, a trace calculation turns the resulting finite set of eigenvalues into a Euclidean root system.

Throughout, \(\mathfrak g\) is a finite-dimensional semisimple Lie algebra over \(\mathbb C\), and \(\kappa\) is its Killing form. We use Engel's and Lie's theorems from [Nilpotent and solvable Lie algebras: Engel's and Lie's theorems](RT-LIE-02.md), the nondegenerate Killing form and zero centre from [The Killing form and Cartan's criteria](RT-LIE-03.md), Jordan decomposition from [Complete reducibility: Casimir elements and Weyl's theorem](RT-LIE-04.md), and the finite module classification from [Representations of \(\mathfrak{sl}_2\)](RT-LIE-05.md). The cohomology lesson is optional and is not used.

The zero algebra has the empty decomposition and a zero-dimensional Euclidean space. Statements about a root concern the nonzero case. We postpone conjugacy of the chosen subalgebras to *Cartan subalgebras and their conjugacy*.

## 1. Find commuting diagonalizable adjoint operators

An element \(x\) is **semisimple** here when \(\operatorname{ad}x\) is diagonalizable. A **toral subalgebra** is an abelian subalgebra of such elements. Commuting diagonalizable operators are simultaneously diagonalizable: diagonalize one, restrict the others to its preserved eigenspaces, and continue with a finite spanning list of operators. Consequently every linear combination in an abelian family of semisimple elements is semisimple.

The abelian requirement is automatic if a subalgebra consists entirely of semisimple elements.

**Lemma 1.1.** A subalgebra \(\mathfrak t\subseteq\mathfrak g\) all of whose elements are semisimple is abelian.

**Proof.** Fix \(x\in\mathfrak t\). The invariant subspace \(\mathfrak t\) decomposes into eigenspaces of \(\operatorname{ad}x\). Suppose \(y\in\mathfrak t\) is an eigenvector with nonzero eigenvalue \(a\). Jacobi shows that \(\operatorname{ad}y\) sends the \(b\)-eigenspace of \(\operatorname{ad}x\) in \(\mathfrak g\) to its \((b+a)\)-eigenspace. Repeating this operator eventually leaves the finite set of eigenvalues, because \(a\ne0\) and characteristic is zero. A common sufficiently large power therefore vanishes on every eigenspace: \(\operatorname{ad}y\) is nilpotent.

It is also diagonalizable by hypothesis, hence zero. The centre of \(\mathfrak g\) is zero, so \(y=0\). Thus the only eigenvalue on \(\mathfrak t\) is zero and \([x,\mathfrak t]=0\). This holds for every \(x\), proving the lemma. \(\square\)

This lemma does not say that the set of all semisimple elements is itself a subalgebra. For example, in \(\mathfrak{sl}_2\), \(h\) and \(h+e\) are semisimple, whereas their bracket \(2e\) is nonzero nilpotent.

Maximal toral subalgebras exist: start with zero and choose a toral subalgebra of largest dimension. There is a nonzero one if \(\mathfrak g\ne0\). Indeed, if every \(\operatorname{ad}x\) were nilpotent, Engel would make \(\mathfrak g\) nilpotent, contradicting semisimplicity. Choose an \(x\) with a nonzero semisimple Jordan part \(x_s\). The previously proved Jordan theorem gives \(x_s\in\mathfrak g\) and \(\operatorname{ad}x_s=(\operatorname{ad}x)_s\); its span is a nonzero toral subalgebra.

Fix a maximal toral subalgebra \(\mathfrak h\). Simultaneous diagonalization gives
\[
\mathfrak g=\bigoplus_{\lambda\in\mathfrak h^*}\mathfrak g_\lambda,
\qquad
\mathfrak g_\lambda=\{v:[H,v]=\lambda(H)v
\text{ for every }H\in\mathfrak h\}.
\tag{1.1}
\]
Only finitely many summands are nonzero. Linearity of the adjoint action makes each eigenvalue assignment \(\lambda\) a linear functional. Write
\[
\Phi=\{\lambda\ne0:\mathfrak g_\lambda\ne0\}.
\]
These functionals are the **roots**, and their eigenspaces are **root spaces**. At this stage their dimensions are unknown.

Jacobi and invariance of the Killing form give
\[
[\mathfrak g_\lambda,\mathfrak g_\mu]
\subseteq\mathfrak g_{\lambda+\mu},
\qquad
\kappa(\mathfrak g_\lambda,\mathfrak g_\mu)=0
\quad\text{if }\lambda+\mu\ne0.
\tag{1.2}
\]
For the bracket, apply \([H,-]\) and use the derivation rule. For the pairing, if \(v,w\) have weights \(\lambda,\mu\), then
\[
0=\kappa([H,v],w)+\kappa(v,[H,w])
=(\lambda+\mu)(H)\kappa(v,w).
\]
Choose \(H\) on which the nonzero functional \(\lambda+\mu\) does not vanish.

Nondegeneracy on \(\mathfrak g\) now gives a nondegenerate pairing between \(\mathfrak g_\lambda\) and \(\mathfrak g_{-\lambda}\). A vector orthogonal to that opposite space is orthogonal to every summand in (1.1), hence zero. In particular \(-\alpha\in\Phi\) whenever \(\alpha\in\Phi\), and \(\kappa\) restricts nondegenerately to \(\mathfrak g_0\).

## 2. Why the zero eigenspace is exactly the chosen subalgebra

**Theorem 2.1.** For the maximal toral \(\mathfrak h\),
\[
C_{\mathfrak g}(\mathfrak h)=\mathfrak h,\qquad
\mathfrak g=\mathfrak h\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha,
\qquad \kappa|_{\mathfrak h}\text{ is nondegenerate}.
\tag{2.1}
\]

**Proof.** Put \(C=\mathfrak g_0=C_{\mathfrak g}(\mathfrak h)\). We already know that \(\mathfrak h\subseteq C\) and that \(\kappa|_C\) is nondegenerate.

For \(x\in C\), the Jordan parts \(x_s,x_n\) also centralize \(\mathfrak h\), by the commuting-operator property of Jordan decomposition. Thus \(x_s,x_n\in C\). Since \(x_s\) commutes with \(\mathfrak h\) and is semisimple, simultaneous diagonalization makes \(\mathfrak h+\mathbb Cx_s\) toral. Maximality forces \(x_s\in\mathfrak h\). On \(C\) its adjoint action is zero, so
\[
\operatorname{ad}_C x=\operatorname{ad}_C x_n
\]
is nilpotent. Engel's theorem makes \(C\) nilpotent, hence solvable.

Apply Lie's theorem to the adjoint representation of \(C\) on \(\mathfrak g\). In a suitable basis all \(\operatorname{ad}x\), \(x\in C\), are upper triangular, and all \(\operatorname{ad}z\), \(z\in[C,C]\), are strictly upper triangular. Their products have zero trace. Therefore \(\kappa(C,[C,C])=0\). Since the restriction is nondegenerate, \([C,C]=0\).

Finally \(x_n\) commutes with every \(y\in C\). The operators \(\operatorname{ad}x_n\) and \(\operatorname{ad}y\) commute, and the former is nilpotent. Their product is nilpotent, since its \(N\)-th power is \((\operatorname{ad}x_n)^N(\operatorname{ad}y)^N=0\) for sufficiently large \(N\). Hence \(\kappa(x_n,y)=0\) for every \(y\in C\). Nondegeneracy on \(C\) gives \(x_n=0\). We obtain \(x=x_s\in\mathfrak h\), so \(C=\mathfrak h\). The decomposition and nondegeneracy follow from Section 1. \(\square\)

The roots span \(\mathfrak h^*\). Otherwise their common annihilator contains a nonzero \(H\). It commutes with \(\mathfrak h\) and every root space, so is central in \(\mathfrak g\), a contradiction.

For \(\lambda\in\mathfrak h^*\), let \(t_\lambda\in\mathfrak h\) be its unique Killing-dual vector:
\[
\kappa(t_\lambda,H)=\lambda(H)
\quad(H\in\mathfrak h).
\tag{2.2}
\]
This is a linear isomorphism \(\mathfrak h^*\to\mathfrak h\). The induced bilinear form on the dual is
\[
(\lambda,\mu)=\kappa(t_\lambda,t_\mu)
=\lambda(t_\mu).
\tag{2.3}
\]
It is complex bilinear at present; positivity has not yet been established.

For \(u\in\mathfrak g_\alpha\), \(v\in\mathfrak g_{-\alpha}\), the bracket belongs to \(\mathfrak h\), and
\[
\kappa([u,v],H)=\kappa(u,[v,H])
=\alpha(H)\kappa(u,v).
\]
Thus
\[
[u,v]=\kappa(u,v)t_\alpha,\qquad
[\mathfrak g_\alpha,\mathfrak g_{-\alpha}]
=\mathbb Ct_\alpha.
\tag{2.4}
\]
The equality follows because the opposite-space pairing is nondegenerate and \(t_\alpha\ne0\).

## 3. One rank-one algebra at every root

A nonzero vector for a complex bilinear form can have square zero. We must prove that this does not happen to a root.

**Lemma 3.1.** For every \(\alpha\in\Phi\), \(a_\alpha=(\alpha,\alpha)=\alpha(t_\alpha)\ne0\). There are \(e_\alpha\in\mathfrak g_\alpha\), \(f_\alpha\in\mathfrak g_{-\alpha}\) such that
\[
h_\alpha=\frac{2t_\alpha}{a_\alpha},\qquad
[h_\alpha,e_\alpha]=2e_\alpha,\quad
[h_\alpha,f_\alpha]=-2f_\alpha,\quad
[e_\alpha,f_\alpha]=h_\alpha.
\tag{3.1}
\]

**Proof.** Choose \(u,v\) with \(\kappa(u,v)=1\), so \([u,v]=t_\alpha\). If \(a_\alpha=0\), then \(t_\alpha\) commutes with \(u,v\), making their span with \(t_\alpha\) solvable. Lie's theorem triangularizes its adjoint action on \(\mathfrak g\). Since \(t_\alpha=[u,v]\), its adjoint is strictly upper triangular, hence nilpotent. But \(t_\alpha\in\mathfrak h\) is semisimple. Its adjoint is zero, so zero centre gives \(t_\alpha=0\), contrary to (2.2) and \(\alpha\ne0\).

Take \(e_\alpha=u\) and \(f_\alpha=2v/a_\alpha\). Equations (2.4) and the root eigenvalues give all three relations. The vectors have distinct weights \(\alpha,0,-\alpha\), so are independent and their span is isomorphic to \(\mathfrak{sl}_2\). \(\square\)

The vector \(h_\alpha\) is the **coroot**, with \(\alpha(h_\alpha)=2\). The algebra \(\mathfrak g\), under the adjoint action of this rank-one subalgebra, is a finite-dimensional \(\mathfrak{sl}_2\)-module. Its classification gives
\[
\beta(h_\alpha)\in\mathbb Z
\quad\text{for every }\beta\in\Phi.
\tag{3.2}
\]

We next prove the root-space dimension and reducedness before using any Euclidean geometry.

**Proposition 3.2.** For every root \(\alpha\),
\[
\dim\mathfrak g_\alpha=1,\qquad
\mathbb C\alpha\cap\Phi=\{\alpha,-\alpha\}.
\tag{3.3}
\]

**Proof.** Consider the finite subspace
\[
M_\alpha=\mathfrak h\oplus
\bigoplus_{\substack{c\in\mathbb C\\ c\alpha\in\Phi}}
\mathfrak g_{c\alpha}.
\]
It is stable under the rank-one algebra: the root bracket shifts \(c\) by \(1\) or \(-1\), the opposite bracket lies in \(\mathfrak h\), and brackets of \(e_\alpha,f_\alpha\) with \(\mathfrak h\) lie in their root lines.

Its \(h_\alpha\)-weight-zero space is exactly \(\mathfrak h\). Raising by \(e_\alpha\) on that space is the map
\[
H\longmapsto[e_\alpha,H]=-\alpha(H)e_\alpha,
\]
of rank one. Decompose \(M_\alpha\) into irreducible finite \(\mathfrak{sl}_2\)-modules. Each even highest-weight summand \(V(2m)\), \(m\ge1\), contributes rank one to raising from weight zero to weight two; \(V(0)\) contributes zero; odd highest-weight summands have no zero weight. The contained adjoint rank-one subalgebra is already a \(V(2)\), and complete reducibility permits it as a summand. Therefore it is the only nontrivial even summand.

Every weight-two vector lies in an even summand, so the weight-two space is the line \(\mathbb Ce_\alpha\). It is exactly \(\mathfrak g_\alpha\). Also no weight four occurs, proving \(2\alpha\notin\Phi\); the same argument excludes every integer multiple except \(\pm\alpha\).

If \(c\alpha\) is any root, (3.2), first for the coroot of \(\alpha\) and then for that of \(c\alpha\), gives
\[
2c\in\mathbb Z,\qquad 2/c\in\mathbb Z.
\]
The latter follows directly from (2.2): \(t_{c\alpha}=ct_\alpha\) and \(h_{c\alpha}=h_\alpha/c\). The two nonzero integers have product four. Hence
\(c\in\{\pm\tfrac12,\pm1,\pm2\}\).
The double cases are already excluded. The half cases would make twice the root \(c\alpha\) equal to \(\pm\alpha\), and applying the same double-root exclusion to \(c\alpha\) excludes them. Only \(\pm1\) remain. \(\square\)

Scaling the Killing form by a nonzero scalar \(z\) changes \(t_\alpha\) to \(t_\alpha/z\) and its induced root square to \(a_\alpha/z\). Their ratio in (3.1) is unchanged. Thus the coroot is independent of that scaling, while its unnormalized dual vector is not.

## 4. Strings, brackets and reflections

**Theorem 4.1.** Fix \(\alpha\in\Phi\). If \(\beta\in\Phi\) is not proportional to \(\alpha\), there are integers \(r,q\ge0\) such that
\[
\{j\in\mathbb Z:\beta+j\alpha\in\Phi\}
=\{-r,-r+1,\ldots,q\},\qquad
r-q=\beta(h_\alpha).
\tag{4.1}
\]
For all roots \(\beta\), including \(\pm\alpha\),
\[
s_\alpha(\beta)=\beta-\beta(h_\alpha)\alpha\in\Phi.
\tag{4.2}
\]
Whenever \(\alpha+\beta\in\Phi\),
\[
[\mathfrak g_\alpha,\mathfrak g_\beta]
=\mathfrak g_{\alpha+\beta}.
\tag{4.3}
\]

**Proof.** For nonproportional \(\beta\), the space
\[
M_{\alpha,\beta}=\bigoplus_{j\in\mathbb Z}
\mathfrak g_{\beta+j\alpha}
\]
is stable under the rank-one subalgebra. No index gives the zero root, and (1.2) shows stability under raising and lowering. Its \(h_\alpha\)-weights are \(\beta(h_\alpha)+2j\), each of multiplicity at most one by Proposition 3.2.

It is a nonzero finite sum of irreducibles. All highest weights have the same parity, since all occurring weights do. Two even highest-weight summands would both contain weight zero; two odd ones would both contain weight one. Either would contradict multiplicity at most one. Thus this module is a single \(V(n)\). Its weights, from lowest to highest, are
\(-n,-n+2,\ldots,n\). Since \(\mathfrak g_\beta\) occurs at index zero, the lowest and highest indices are \(-r,q\) with \(r,q\ge0\). They satisfy
\[
\beta(h_\alpha)-2r=-n,\qquad
\beta(h_\alpha)+2q=n.
\]
Adding gives \(\beta(h_\alpha)=r-q\), proving (4.1).

The index of \(s_\alpha(\beta)\) is \(q-r\), which lies between \(-r\) and \(q\). This proves (4.2) in the nonproportional case. The remaining roots are \(\beta=\pm\alpha\), by reducedness, and \(s_\alpha\) interchanges them because \(\alpha(h_\alpha)=2\).

Finally if \(\alpha+\beta\) is a root, \(\beta\) cannot be proportional to \(\alpha\): the only possibilities would give \(2\alpha\) or zero, neither a root. In the irreducible string module, raising by \(e_\alpha\) is nonzero on every weight except its highest. The existence of the next root \(\beta+\alpha\) therefore gives a nonzero bracket from \(\mathfrak g_\beta\) to the one-dimensional target \(\mathfrak g_{\alpha+\beta}\). Since \(\mathfrak g_\alpha=\mathbb Ce_\alpha\), this proves (4.3). \(\square\)

The nonproportional condition in (4.1) is necessary. In \(\{\alpha,-\alpha\}\), the translates of \(\beta=\alpha\) that are roots have indices \(0,-2\); index \(-1\) gives zero and is absent. The rank-one module has a zero-weight coroot between those two root spaces, but that coroot is not a root.

For an \(A_2\) example take \(\alpha=\epsilon_1-\epsilon_2\) and \(\beta=\epsilon_2-\epsilon_3\). The string is \(\beta,\beta+\alpha\), so \(r=0,q=1\) and \(\beta(h_\alpha)=-1\). The bracket of the corresponding matrix units is
\([E_{12},E_{23}]=E_{13}\), realizing the nonzero step in (4.3).

## 5. Recover a rational and positive Euclidean form

The complex bilinear form (2.3) becomes positive on a particular real space. That conclusion requires a real form; it is not a positivity claim on all of \(\mathfrak h^*\).

**Theorem 5.1.** Put
\[
\mathfrak h_{\mathbb Q}=\operatorname{span}_{\mathbb Q}
\{h_\alpha:\alpha\in\Phi\},\quad
\mathfrak h_{\mathbb R}=\operatorname{span}_{\mathbb R}
\{h_\alpha:\alpha\in\Phi\},\quad
E=\operatorname{span}_{\mathbb R}\Phi.
\]
Then \(\mathfrak h_{\mathbb R}\) is a real form of \(\mathfrak h\), the restriction of \(\kappa\) to it is real and positive definite, and \(E\) is its real dual under evaluation. The induced form (2.3) is positive definite on \(E\) and rational on \(\operatorname{span}_{\mathbb Q}\Phi\). With this form, \(\Phi\) is a reduced root system.

**Proof.** Let \(\ell=\dim_{\mathbb C}\mathfrak h\). Since roots span \(\mathfrak h^*\), their Killing-dual vectors span \(\mathfrak h\), as do their nonzero multiples \(h_\alpha\). Choose a complex basis \(H_1,\ldots,H_\ell\) among the coroots and a complex basis \(\gamma_1,\ldots,\gamma_\ell\) among the roots. The matrix
\[
A=(\gamma_i(H_j))_{i,j}
\]
is invertible and has integer entries by (3.2). For any coroot \(h_\beta=\sum_j c_jH_j\), the equations
\(A(c_j)_j=(\gamma_i(h_\beta))_i\) have integer right side. The inverse of the nonsingular integer matrix is rational, so every \(c_j\) is rational. Hence \(\mathfrak h_{\mathbb Q}=\bigoplus_j\mathbb QH_j\) and
\(\mathfrak h_{\mathbb R}=\bigoplus_j\mathbb RH_j\). The complex basis proves
\[
\mathfrak h=\mathfrak h_{\mathbb R}\oplus
i\mathfrak h_{\mathbb R}.
\tag{5.1}
\]

Every root is real-valued on \(\mathfrak h_{\mathbb R}\). In the root decomposition, \(\operatorname{ad}H\) acts as zero on \(\mathfrak h\) and as the scalar \(\gamma(H)\) on each root line. Therefore
\[
\kappa(H,K)=\sum_{\gamma\in\Phi}\gamma(H)\gamma(K)
\quad(H,K\in\mathfrak h).
\tag{5.2}
\]
For real \(H,K\) this is real. For \(H\ne0\) in \(\mathfrak h_{\mathbb R}\),
\[
\kappa(H,H)=\sum_{\gamma\in\Phi}\gamma(H)^2>0,
\tag{5.3}
\]
because all summands are nonnegative real numbers and their simultaneous vanishing would put \(H\) in the common root annihilator, already proved zero.

The roots \(\gamma_i\) form a real basis of the dual of \(\mathfrak h_{\mathbb R}\), since their evaluation matrix \(A\) is invertible over \(\mathbb R\). Thus \(E=(\mathfrak h_{\mathbb R})^*\), viewed as a real subspace of \(\mathfrak h^*\) by complex-linear extension. Let \(G=(\kappa(H_i,H_j))\). Equation (5.2) makes \(G\) an integer matrix, and (5.3) makes it positive definite. A root has an integer coordinate column of evaluations on the \(H_j\). Its Killing-dual vector consequently has rational coordinates, obtained by multiplying that column by \(G^{-1}\). In particular \(t_\alpha\in\mathfrak h_{\mathbb Q}\). Formula (2.3) is therefore rational on the rational root span and positive definite on its real span: it is the inverse form of the positive definite matrix \(G\).

Finally the root set is finite, excludes zero, spans \(E\), and has only \(\pm\alpha\) on each root line. Equations (2.3) and (3.1) give
\[
\langle\beta,\alpha^\vee\rangle
:=\beta(h_\alpha)=\frac{2(\beta,\alpha)}{(\alpha,\alpha)}
\in\mathbb Z.
\tag{5.4}
\]
The map
\[
s_\alpha(\lambda)=\lambda-
\frac{2(\lambda,\alpha)}{(\alpha,\alpha)}\alpha
\tag{5.5}
\]
fixes \(\alpha^\perp\) and negates \(\alpha\). Decomposing each vector into these two components proves that it is an orthogonal reflection. Theorem 4.1 says that it preserves \(\Phi\). These are exactly the spanning, integrality, reflection and reducedness axioms of a reduced root system. \(\square\)

For the zero algebra this argument is the empty-basis calculation, with \(E=0\) and \(\Phi=\varnothing\). If a definition requires root systems to be nonempty, this case is recorded separately.

## 6. Read the classical roots directly from matrices

Write \(E_{ij}\) for matrix units. The following calculations use convenient forms with paired coordinate blocks. Reversing the order in the last block makes the symmetric paired form anti-diagonal. These are changes of basis, so they do not change the Lie algebra.

For \(\mathfrak{sl}_n\), \(n\ge2\), take diagonal traceless
\(H=\operatorname{diag}(t_1,\ldots,t_n)\) and define \(\epsilon_i(H)=t_i\). Then
\[
[H,E_{ij}]=(t_i-t_j)E_{ij},\qquad
\Phi=\{\epsilon_i-\epsilon_j:i\ne j\},\qquad
\mathfrak g_{\epsilon_i-\epsilon_j}=\mathbb CE_{ij}.
\tag{6.1}
\]
The diagonal zero-weight space has dimension \(n-1\), and \(\sum_i\epsilon_i=0\). The root space is the real hyperplane \(\sum_i x_i=0\) in \(\mathbb R^n\), with the indicated difference vectors. There are \(n(n-1)\) roots.

For even orthogonal and symplectic algebras use, respectively,
\[
Q=\begin{pmatrix}0&I\\I&0\end{pmatrix},
\qquad
J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]
Solving \(X^{\mathsf t}Q+QX=0\) or
\(X^{\mathsf t}J+JX=0\) gives
\[
X=\begin{pmatrix}A&B\\C&-A^{\mathsf t}\end{pmatrix},
\tag{6.2}
\]
where \(B,C\) are skew-symmetric for \(Q\) and symmetric for \(J\). Indeed the lower-right block is forced by the upper-left one; the other two equations are exactly the displayed symmetry conditions.

In both cases choose
\(H(t)=\operatorname{diag}(t_1,\ldots,t_n,-t_1,\ldots,-t_n)\).
Write
\[
A(F)=\begin{pmatrix}F&0\\0&-F^{\mathsf t}\end{pmatrix},\qquad
B(F)=\begin{pmatrix}0&F\\0&0\end{pmatrix},\qquad
C(F)=\begin{pmatrix}0&0\\F&0\end{pmatrix}.
\]
These satisfy (6.2) when \(F\) has the required symmetry in the latter two cases. Put \(\epsilon_i(H(t))=t_i\). The root vectors and weights are
\[
\begin{array}{c|c}
\text{matrix}&\text{weight}\\ \hline
A(E_{ij}),\ i\ne j&\epsilon_i-\epsilon_j\\
B(E_{ij}-E_{ji}),\ i<j&\epsilon_i+\epsilon_j\\
C(E_{ij}-E_{ji}),\ i<j&-\epsilon_i-\epsilon_j
\end{array}
\quad\text{for }\mathfrak{so}_{2n},
\tag{6.3}
\]
whereas for \(\mathfrak{sp}_{2n}\) replace the two minus signs inside the \(B,C\) matrices by plus signs and also include
\[
B(E_{ii})\text{ of weight }2\epsilon_i,\qquad
C(E_{ii})\text{ of weight }-2\epsilon_i.
\tag{6.4}
\]
Each weight is verified by multiplying the diagonal \(H(t)\) on the left and right. The free entries in (6.2) show that these vectors together with \(A(E_{ii})\) form a basis. Hence the complete root lists are
\[
\begin{aligned}
D_n:\quad&\{\pm\epsilon_i\pm\epsilon_j:i<j\},
&&n\ge2,\\
C_n:\quad&\{\pm\epsilon_i\pm\epsilon_j:i<j\}
\ \cup\ \{\pm2\epsilon_i\},
&&n\ge1.
\end{aligned}
\tag{6.5}
\]
The two signs in a pair are independent. The counts are \(2n(n-1)\) and \(2n^2\), respectively.

For odd orthogonal matrices order the coordinates in blocks of sizes \(n,1,n\), and take
\[
Q_o=\begin{pmatrix}0&0&I\\0&1&0\\I&0&0\end{pmatrix}.
\]
Solving the defining equation gives every matrix uniquely as
\[
X=\begin{pmatrix}
A&u&B\\
v^{\mathsf t}&0&-u^{\mathsf t}\\
C&-v&-A^{\mathsf t}
\end{pmatrix},
\qquad B^{\mathsf t}=-B,\quad C^{\mathsf t}=-C.
\tag{6.6}
\]
For example the upper-middle equation forces the lower-middle block to be \(-v\), the middle-right equation forces \(-u^{\mathsf t}\), and the middle diagonal equation forces zero. Choose
\(H(t)=\operatorname{diag}(t_1,\ldots,t_n,0,-t_1,\ldots,-t_n)\).
The \(A,B,C\) entries give the \(D_n\) roots. A single \(u_i\) entry has weight \(\epsilon_i\), and a single \(v_i\) entry has weight \(-\epsilon_i\). These supply the additional roots
\[
B_n:\quad
\{\pm\epsilon_i\pm\epsilon_j:i<j\}
\ \cup\ \{\pm\epsilon_i\},
\qquad n\ge1.
\tag{6.7}
\]
There are \(2n^2\) roots. In all three block models the zero-weight space is precisely the chosen diagonal algebra. Thus it centralizes only itself and is maximal toral: a larger toral algebra would commute with it and lie in that same zero space.

The lists also verify semisimplicity of these classical models without assuming the classification. Taking the trace of \(\operatorname{ad}H(t)\operatorname{ad}H(u)\) in the displayed matrix bases gives
\[
\begin{array}{c|c|c}
\text{algebra}&\kappa(H(t),H(u))&
\text{dual coordinate metric}\\ \hline
\mathfrak{sl}_n&2n\sum_i t_i u_i,\ \sum t_i=\sum u_i=0
&\frac1{2n}\text{ times the hyperplane dot product}\\
\mathfrak{so}_{2n+1}&(4n-2)\sum_i t_i u_i&
\frac1{4n-2}\text{ times the dot product}\\
\mathfrak{sp}_{2n}&4(n+1)\sum_i t_i u_i&
\frac1{4(n+1)}\text{ times the dot product}\\
\mathfrak{so}_{2n}&4(n-1)\sum_i t_i u_i&
\frac1{4(n-1)}\text{ times the dot product}
\end{array}
\tag{6.8}
\]
For the difference roots of \(\mathfrak{sl}_n\), expanding
\(\sum_{i\ne j}(t_i-t_j)(u_i-u_j)\) gives the first row. For the other rows each four-root pair
\(\{\pm\epsilon_i\pm\epsilon_j\}\) contributes
\(4(t_i u_i+t_j u_j)\); the short pair \(\pm\epsilon_i\) contributes \(2t_i u_i\), and the long pair \(\pm2\epsilon_i\) contributes \(8t_i u_i\). Summing gives every coefficient in (6.8).

To check nondegeneracy on the whole algebra, not just its diagonal part, opposite root matrices have a bracket \(K\) of the following forms: \(H_i-H_j\) for difference roots, \(H_i+H_j\) for pair-sum roots, and \(H_i\) for the short odd-orthogonal or long symplectic roots, where \(H_i=A(E_{ii})\). In \(\mathfrak{sl}_n\) use \(K=E_{ii}-E_{jj}\). For skew pair-sum matrices take the negative of the \(C\) matrix as the opposite vector; for symmetric pair-sum matrices take the \(C\) matrix itself. Direct multiplication gives these brackets. The \(u_i,v_i\) matrices in (6.6) also bracket to \(H_i\). Their respective root evaluations \(\alpha(K)\) are \(2,2,1,2\), all nonzero.

Invariance yields
\(\kappa(K,K)=\alpha(K)\kappa(X_\alpha,X_{-\alpha})\).
The left side is positive by the diagonal formulas, so every opposite-root pairing is nonzero. All other weight pairings are zero by the argument in (1.2), which uses invariance alone. The diagonal part is nondegenerate by (6.8), and each opposite pair of root lines is nondegenerate. Thus the entire Killing form is nondegenerate and the Killing criterion proves semisimplicity.

The low-dimensional boundaries matter. \(\mathfrak{sl}_1=0\); \(\mathfrak{sp}_2\) and \(\mathfrak{so}_3\) have rank one. The even orthogonal formula starts at \(n=2\): \(\mathfrak{so}_2\) is one-dimensional abelian, its Killing form is zero and it is not a semisimple \(D_1\) example. At \(n=2\), \(D_2\) is a reducible root system.

## 7. Three low-rank pictures

For \(\mathfrak{sl}_3\), the roots are the six vectors
\(\epsilon_i-\epsilon_j\) in the plane \(x_1+x_2+x_3=0\).
Use the ambient orthonormal axes
\[
a=\frac{(1,-1,0)}{\sqrt2},\qquad
b=\frac{(1,1,-2)}{\sqrt6}.
\]
The positive difference vectors have coordinates
\[
\epsilon_1-\epsilon_2=(\sqrt2,0),\quad
\epsilon_2-\epsilon_3=(-1/\sqrt2,\sqrt{3/2}),\quad
\epsilon_1-\epsilon_3=(1/\sqrt2,\sqrt{3/2}),
\tag{7.1}
\]
and the other roots are their negatives. These are six equally spaced points on a circle. The Killing-dual metric is \(1/6\) of the ambient dot product, so each root has squared length \(1/3\). This is the regular hexagon called \(A_2\).

For \(\mathfrak{so}_5\) and \(\mathfrak{sp}_4\), write their coordinate roots as \(B_2\) in \(\epsilon_i\) and \(C_2\) in \(\delta_i\). Their sets are
\[
\begin{aligned}
B_2&=\{\pm\epsilon_1,\pm\epsilon_2,
\pm\epsilon_1\pm\epsilon_2\},\\
C_2&=\{\pm2\delta_1,\pm2\delta_2,
\pm\delta_1\pm\delta_2\}.
\end{aligned}
\tag{7.2}
\]
The map
\[
T(\epsilon_1)=\delta_1+\delta_2,\qquad
T(\epsilon_2)=\delta_1-\delta_2
\tag{7.3}
\]
sends the first root set bijectively to the second: it sends the axis roots to diagonal roots, and the diagonal roots to doubled axis roots. In the usual unscaled coordinates it is a rotation or reflection combined with a dilation by \(\sqrt2\). In the actual Killing-dual metrics it is an isometry, because those matrices are \(I/6\) for \(B_2\) and \(I/12\) for \(C_2\), and \(T^{\mathsf t}T=2I\). Thus the two root configurations agree with their intrinsic metrics. The construction of the corresponding Lie algebra isomorphism belongs to the later classical-model lesson.

For \(\mathfrak{so}_4\), the roots are
\[
\pm(\epsilon_1-\epsilon_2),\qquad
\pm(\epsilon_1+\epsilon_2).
\tag{7.4}
\]
The two pairs are orthogonal. We can see the two Lie algebra factors explicitly in the block model (6.2). Put
\[
K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
For \(\alpha=\epsilon_1-\epsilon_2\), take
\[
e_\alpha=A(E_{12}),\quad f_\alpha=A(E_{21}),\quad
h_\alpha=A(\operatorname{diag}(1,-1)).
\]
For \(\beta=\epsilon_1+\epsilon_2\), take
\[
e_\beta=B(K),\quad f_\beta=C(-K),\quad h_\beta=A(I).
\]
Since \(K^2=-I\), multiplying the blocks gives
\([B(K),C(-K)]=A(I)\). The other brackets in each triple are
\([h,e]=2e,[h,f]=-2f\); the first triple also has
\([A(E_{12}),A(E_{21})]=A(\operatorname{diag}(1,-1))\).
Across the two triples, the coroot evaluations are zero and the sums or differences of their root weights are not roots or zero. Hence every cross bracket vanishes by (1.2). The six displayed matrices span \(\mathfrak{so}_4\): the four root lines and two independent diagonal directions are its whole basis. Consequently
\[
\mathfrak{so}_4\simeq
\mathfrak{sl}_2\oplus\mathfrak{sl}_2,
\qquad D_2=A_1\sqcup A_1.
\tag{7.5}
\]
This proof uses no compact group or conjugacy theorem.

## 8. Exercises with complete solutions

**Exercise 8.1 (easy).** Compute the root decomposition of \(\mathfrak{sl}_3\), including its zero-weight space and Killing-dual metric.

**Solution.** Let
\(\mathfrak h=\{\operatorname{diag}(t_1,t_2,t_3):t_1+t_2+t_3=0\}\).
For \(i\ne j\),
\([H,E_{ij}]=(t_i-t_j)E_{ij}\). Thus the six nonzero weights are \(\epsilon_i-\epsilon_j\) and each root space is the span of that matrix unit. The diagonal trace-zero matrices are exactly the zero-weight space; they have dimension two. Therefore
\[
\mathfrak{sl}_3=\mathfrak h\oplus
\mathbb CE_{12}\oplus\mathbb CE_{21}\oplus
\mathbb CE_{13}\oplus\mathbb CE_{31}\oplus
\mathbb CE_{23}\oplus\mathbb CE_{32}.
\]
This accounts for all eight dimensions. The root trace sum is
\(\sum_{i\ne j}(t_i-t_j)(u_i-u_j)=6\sum_i t_i u_i\),
because both coordinate sums are zero. Its inverse metric on the root plane is the ambient dot product divided by six. For example the dual vector for \(\epsilon_i-\epsilon_j\) is
\(t_\alpha=(E_{ii}-E_{jj})/6\), its squared length is \(1/3\), and (3.1) gives \(h_\alpha=E_{ii}-E_{jj}\). The six coordinates in (7.1) and their negatives give the hexagon.

**Exercise 8.2 (medium).** Compute the roots of \(\mathfrak{sp}_4\) and \(\mathfrak{so}_5\), and compare them.

**Solution.** For the symplectic algebra set \(n=2\) in (6.2). Its \(A\)-block is arbitrary and its \(B,C\)-blocks are symmetric. The two diagonal \(A\)-matrices give a two-dimensional zero-weight space. The off-diagonal \(A\)-matrices give \(\pm(\delta_1-\delta_2)\); the off-diagonal symmetric \(B,C\)-matrices give \(\pm(\delta_1+\delta_2)\); their diagonal entries give \(\pm2\delta_1,\pm2\delta_2\). Each entry direction is one-dimensional. These eight root directions and two diagonal directions account for \(4+3+3=10\) dimensions.

For the odd orthogonal algebra use the blocks of sizes \(2,1,2\) in (6.6). The off-diagonal \(A\)-directions give \(\pm(\epsilon_1-\epsilon_2)\), the skew \(B,C\)-directions give \(\pm(\epsilon_1+\epsilon_2)\), and \(u_1,u_2,v_1,v_2\) give \(\pm\epsilon_1,\pm\epsilon_2\). The two diagonal directions are the zero-weight space, and the total dimension is \(4+1+1+2+2=10\).

The eight-root sets are (7.2). Apply (7.3): the images of \(\epsilon_1,\epsilon_2,\epsilon_1+\epsilon_2,\epsilon_1-\epsilon_2\) are respectively
\(\delta_1+\delta_2,\delta_1-\delta_2,2\delta_1,2\delta_2\).
Including negatives proves a bijection. The Killing trace sums give metric matrices \(I/6,I/12\), so \(T^{\mathsf t}(I/12)T=I/6\). This establishes the precise root-system isometry.

**Exercise 8.3 (medium).** Prove \(\dim\mathfrak g_\alpha=1\) using the module formed from root spaces on the line through \(\alpha\).

**Solution.** Include the zero-weight space: take
\(M=\mathfrak h\oplus\bigoplus_{c\alpha\in\Phi}\mathfrak g_{c\alpha}\).
It is a finite module for \(e_\alpha,h_\alpha,f_\alpha\) because raising and lowering shift \(c\) and the bracket of opposite root spaces is in \(\mathfrak h\). The weight-zero space is \(\mathfrak h\), and raising on it is \(H\mapsto-\alpha(H)e_\alpha\), which has rank one.

In a decomposition into \(V(n)\), a nontrivial even \(V(n)\) contributes exactly one to this rank: its zero-weight vector raises to a nonzero weight-two vector. Trivial summands contribute zero and odd summands have no weight zero. The adjoint span \(\mathbb Cf_\alpha\oplus\mathbb Ch_\alpha\oplus\mathbb Ce_\alpha\) is a \(V(2)\) summand by complete reducibility. It already contributes the full rank one, so no other nontrivial even summand occurs. Weight two can occur only in such an even summand. Thus the weight-two space of \(M\) is precisely \(\mathbb Ce_\alpha\); by its definition that space is \(\mathfrak g_\alpha\). Its dimension is one. Leaving out the zero-weight space would not give a submodule, since \([e_\alpha,f_\alpha]=h_\alpha\).

**Exercise 8.4 (hard).** Prove that the Killing-dual form is positive definite on the real span of the roots. Include the rationality assertion.

**Solution.** Roots span \(\mathfrak h^*\), so coroots span \(\mathfrak h\). Choose complex bases \(H_j\) from the coroots and \(\gamma_i\) from the roots. All entries \(\gamma_i(H_j)\) are integers, and their matrix is nonsingular. For any coroot \(h_\beta=\sum c_jH_j\), evaluation by all \(\gamma_i\) gives a nonsingular integer linear system with integer right side. Hence the coefficients \(c_j\) are rational. The real coroot span is therefore \(\bigoplus_j\mathbb RH_j\), a real form of \(\mathfrak h\), and each root takes real values on it.

The root-space dimension is one, so the trace of two diagonal adjoint operators is
\(\kappa(H,K)=\sum_{\alpha\in\Phi}\alpha(H)\alpha(K)\).
For real nonzero \(H\), this gives a sum of nonnegative real squares, and at least one is positive because roots have zero common annihilator. Thus the restriction is positive definite.

The chosen roots have nonsingular real evaluation matrix, so their real span is the whole real dual. Its induced Killing-dual form is the inverse positive definite form and hence positive definite. More explicitly, the Gram matrix \(G=(\kappa(H_i,H_j))\) has integer entries by the trace sum. It is nonsingular, so \(G^{-1}\) has rational entries. Every root evaluation column is integer; dual root pairings are obtained from these columns and \(G^{-1}\), proving rationality on their rational span. This proves both assertions without assuming a compact real form.

## What this lesson does not prove

Engel, Lie, the Killing criterion, zero centre, Jordan decomposition and the finite \(\mathfrak{sl}_2\)-module classification are the proved prerequisites linked at the start. No classification theorem for semisimple Lie algebras or abstract root systems is used.

Conjugacy of maximal toral subalgebras, and their equivalence with the general nilpotent self-normalizing definition of Cartan subalgebra, are treated in *Cartan subalgebras and their conjugacy*. The Lie algebra isomorphism \(\mathfrak{sp}_4\simeq\mathfrak{so}_5\) is not inferred from a picture here; its root-system comparison is proved, and the Lie algebra construction belongs to *The simple Lie algebras: classical models and the exceptional algebras*. Exceptional root systems and their classification are addressed in the subsequent root-system lessons.

The root decomposition, opposite pairings, rank-one triples, one-dimensional root spaces, reducedness, all Cartan integers and reflections, nonproportional root strings, bracket equality, rationality and positivity are all proved in this lesson. The classical matrix decompositions and their semisimplicity checks are included.

## References

- **[Milne]** J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected 2021 text, published 2022, §21a, pp. 424–426; §21j, pp. 457–462. These compare Lie weights with algebraic-group characters; the group-theoretic structure theorems are not imports here. [Author's corrected 2021 edition](https://www.jmilne.org/math/Books/iAG2022.pdf).
- **[Kirillov]** A. Kirillov, Jr., *Introduction to Lie Groups and Lie Algebras*, §§6.4–6.6, pp. 95–102, especially Theorems 6.35, 6.44 and 6.45. [Author-hosted notes](https://math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf).
