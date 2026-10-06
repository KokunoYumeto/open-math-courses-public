# Hilbert spaces and unitary representations

**Programme reading HA-LCA-PRE-HILBERT.** This reading supplies the Hilbert-space foundations used by the positive-type lesson. Self-checked by the writing AI. Hilbert spaces may have arbitrary dimension, measure spaces need not be sigma-finite, and topological groups need not be abelian.

Inner products are linear in the first variable and conjugate-linear in the second. The foundations are set theory with choice, the complete real and complex fields, and the definitions of topology and measure. Every additional result used below is proved here or linked to an exact earlier programme proof.

The freely accessible mathematical sources are Jean Gallier and Jocelyn Quaintance, [*A Glimpse at Hilbert Spaces*, author notes dated 10 March 2017](https://www.cis.upenn.edu/~jean/hilbert-spaces.pdf), §§1.1–1.3 through Theorem 1.16; Michael Taylor, [*Lectures on Banach Algebras*, author-hosted notes](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/banalg.pdf), §§4–5 and Proposition 6.1; D. H. Fremlin, [*Measure Theory*, §244, version of 6 March 2009](https://www1.essex.ac.uk/maths/people/fremlin/mt2.2016/mt244.tex), 244D–G, 244N(a) and 244P(a)–(b),(e); and B. Bekka, P. de la Harpe and A. Valette, [*Kazhdan's Property (T)*, free author draft dated 23 February 2007](https://perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf), Appendix A.1–A.2 at the specific results discussed in Section 7. All source citations identify reading material; all proof obligations are discharged below.

This combined reading is distributed under the [Design Science License](../../assets/fremlin/DESIGN-SCIENCE-LICENSE.txt), retaining Fremlin's original copyright 1995 for §244 and the unchanged volume 2 source package. The exposition is newly written; the other sources' prose and figures are not reproduced.

## 1. Positive forms and completion

A sesquilinear form \(B\) on a complex vector space \(V\) is linear in its first variable and conjugate-linear in its second. Call it positive if \(Q(x)=B(x,x)\) is real and nonnegative for every \(x\).

<a id="ha-lca-pre-hilbert-lemma-1-1"></a>
### Lemma 1.1. Positivity, Cauchy–Schwarz and the null quotient

A positive sesquilinear form satisfies
\[
 B(y,x)=\overline{B(x,y)},\qquad
 |B(x,y)|^2\le Q(x)Q(y).
\]
Its null space \(N=\{x:Q(x)=0\}\) is a linear subspace and \(B(N,V)=B(V,N)=0\). Consequently \(B\) induces an inner product on \(V/N\). For an inner product, \(\|x\|=\sqrt{B(x,x)}\) is a norm, and
\[
 \|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2.
 \tag{1}
\]
Inner products are jointly continuous in their norms.

**Proof.** Put \(a=B(x,y)\) and \(b=B(y,x)\). The imaginary parts of \(Q(x+y)\) and \(Q(x+iy)\) vanish. Expanding gives \(\operatorname{Im}(a+b)=0\) and \(\operatorname{Re}(b-a)=0\); hence \(b=\bar a\). If \(Q(y)>0\), positivity at \(x-B(x,y)y/Q(y)\) gives \(Q(x)-|B(x,y)|^2/Q(y)\ge0\). If \(Q(y)=0\), positivity of
\[
 Q(x+ty)=Q(x)+2\operatorname{Re}(\bar t B(x,y))
\]
for every complex \(t\) forces \(B(x,y)=0\). This proves Cauchy–Schwarz, including the null case.

Each null vector is orthogonal to every vector. Linearity then shows that every linear combination of null vectors is null, and that changing either representative modulo \(N\) leaves \(B\) unchanged. The quotient form is positive definite by the definition of \(N\).

Homogeneity of the proposed norm follows from sesquilinearity, and definiteness follows from positive definiteness. Expanding \(\|x+y\|^2\) and applying Cauchy–Schwarz gives the triangle inequality. Direct expansion gives (1). The triangle inequality also gives \(|\|x\|-\|y\||\le\|x-y\|\). Finally,
\[
 |\langle x,y\rangle-\langle x',y'\rangle|
 \le \|x-x'\|\,\|y\|+\|x'\|\,\|y-y'\|,
\]
which proves joint continuity. These computations also give the polarization identity
\[
 \langle x,y\rangle=\tfrac14\bigl(\|x+y\|^2-\|x-y\|^2
                +i\|x+iy\|^2-i\|x-iy\|^2\bigr).
 \tag{2}
\]
Thus equality of the diagonal values of two sesquilinear forms implies equality of the forms whenever their difference has zero diagonal: apply the same expansion to that difference. \(\square\)

<a id="ha-lca-pre-hilbert-theorem-1-2"></a>
### Theorem 1.2. Hilbert completion and extension from a dense subspace

Every inner-product space has an isometric dense linear embedding into a complete inner-product space, its Hilbert completion. Any bounded linear map from a dense linear subspace of a normed space into a Banach space extends uniquely and with the same norm to the closure of that subspace. An isometry between dense linear subspaces of Hilbert spaces, with dense range, extends to a surjective linear isometry.

**Proof.** Let \(\mathcal C\) be the vector space of Cauchy sequences in the given inner-product space \(V\). Declare \((x_n)\sim(y_n)\) when \(\|x_n-y_n\|\to0\). The triangle inequality proves that this is an equivalence relation compatible with addition and scalar multiplication. Every Cauchy sequence is bounded. Therefore the continuity estimate in Lemma 1.1 shows that \(\langle x_n,y_n\rangle\) is a Cauchy sequence of scalars. Define the inner product of the two classes to be its limit. The same estimate proves independence of representatives. Its diagonal value is \(\lim_n\|x_n\|^2\), which is zero exactly for the zero class.

Constant sequences embed \(V\) isometrically. The class \(X=[(x_n)]\) is the limit of the embedded vectors \(x_k\): given \(\varepsilon>0\), for large \(k\) all sufficiently late \(n\) satisfy \(\|x_k-x_n\|<\varepsilon\), whence \(\|x_k-X\|\le\varepsilon\). The image is dense.

To prove completeness, let \((X_n)\) be a Cauchy sequence of classes. Choose \(v_n\in V\) with \(\|v_n-X_n\|<1/n\), using density. The triangle inequality makes \((v_n)\) Cauchy in \(V\), so its class \(X\) exists. The preceding paragraph gives \(v_n\to X\), and consequently \(X_n\to X\).

For the extension assertion, if \(x_n\) lies in the dense subspace and converges to \(x\), the estimate \(\|Tx_n-Tx_m\|\le\|T\|\|x_n-x_m\|\) makes \(Tx_n\) Cauchy. Define the extension by its limit in the Banach target. Comparing two approximating sequences proves independence; passing to limits proves linearity, boundedness and uniqueness. The norm agrees because restriction cannot increase the supremum that defines the operator norm. For an isometry the extended map is again an isometry. Its range is closed: convergence of image vectors makes their preimages Cauchy and hence convergent. A closed dense range is the whole target. Polarization (2) shows that a linear isometry preserves inner products. \(\square\)

## 2. Projection, duality and bounded forms

<a id="ha-lca-pre-hilbert-theorem-2-1"></a>
### Theorem 2.1. Projection onto a closed convex set

Let \(C\) be a nonempty closed convex subset of a Hilbert space \(H\). For every \(u\in H\) there is a unique \(p\in C\) minimizing \(\|u-p\|\). It is characterized by
\[
 \operatorname{Re}\langle u-p,z-p\rangle\le0\quad(z\in C).
 \tag{3}
\]
The resulting projection \(P_C:H\to C\) satisfies \(\|P_Cu-P_Cv\|\le\|u-v\|\).

**Proof.** Let \(d=\inf_{z\in C}\|u-z\|\), which is finite because \(C\ne\varnothing\). Choose \(z_n\in C\) with \(\|u-z_n\|\to d\). Their midpoints belong to \(C\), so (1) gives
\[
 \|z_n-z_m\|^2
 =2\|u-z_n\|^2+2\|u-z_m\|^2
       -4\|u-(z_n+z_m)/2\|^2
 \le2\|u-z_n\|^2+2\|u-z_m\|^2-4d^2.
\]
The right side tends to zero, also when \(d=0\). Completeness and closedness give a limit \(p\in C\) with \(\|u-p\|=d\). Applying the same inequality to two minimizing points makes their distance zero.

For \(z\in C\) and \(0<t\le1\), the point \(p+t(z-p)\) belongs to \(C\). Subtracting \(d^2\) from its squared distance to \(u\) yields
\[
 -2t\operatorname{Re}\langle u-p,z-p\rangle+t^2\|z-p\|^2\ge0.
\]
Divide by \(t\) and let \(t\downarrow0\), obtaining (3). Conversely, expansion of \(\|u-z\|^2\) using (3) gives \(\|u-z\|^2\ge\|u-p\|^2+\|z-p\|^2\), so \(p\) is the minimizing point.

Write \(p=P_Cu\), \(q=P_Cv\). Applying (3) first to \(q\) and then to \(p\), and subtracting the two real inequalities, gives
\[
 \|p-q\|^2\le\operatorname{Re}\langle u-v,p-q\rangle
 \le\|u-v\|\|p-q\|.
\]
If \(p=q\) the assertion is immediate; otherwise division proves it. \(\square\)

<a id="ha-lca-pre-hilbert-corollary-2-2"></a>
### Corollary 2.2. Orthogonal decomposition

For a closed linear subspace \(M\subseteq H\), every \(x\in H\) has a unique decomposition \(x=m+n\), with \(m\in M\) and \(n\in M^\perp\). The projection \(P_Mx=m\) is linear, has norm at most one, and satisfies
\[
 P_M^2=P_M,\qquad
 \langle P_Mx,y\rangle=\langle x,P_My\rangle,\qquad
 \|x\|^2=\|P_Mx\|^2+\|(I-P_M)x\|^2.
 \tag{4}
\]
For any subset \(A\subseteq H\), \(A^\perp\) is closed and \(A^{\perp\perp}=\overline{\operatorname{span}A}\).

**Proof.** In (3) put \(z=P_Mx+tw\), where \(w\in M\) and \(t\) runs through positive and negative real and purely imaginary numbers. It follows that \(\langle x-P_Mx,w\rangle=0\). Orthogonal decompositions are unique because \(M\cap M^\perp=\{0\}\). Adding and scaling decompositions proves linearity. Expansion of the squared norm gives (4), including contractivity and the inner-product identity.

Each condition \(\langle x,a\rangle=0\) defines a closed set by Lemma 1.1, so their intersection \(A^\perp\) is closed. Put \(L=\overline{\operatorname{span}A}\). Continuity shows \(A^\perp=L^\perp\). If \(x\in A^{\perp\perp}\), decompose \(x=l+n\), with \(n\in L^\perp\). Then \(0=\langle x,n\rangle=\|n\|^2\), so \(x\in L\). The reverse inclusion follows from orthogonality and continuity. In particular, the orthogonal complement of a proper closed linear subspace is nonzero. \(\square\)

<a id="ha-lca-pre-hilbert-theorem-2-3"></a>
### Theorem 2.3. Riesz representation for the Hilbert dual

For every bounded linear functional \(\ell:H\to\mathbb C\), there is a unique \(v\in H\) with \(\ell(x)=\langle x,v\rangle\), and \(\|\ell\|=\|v\|\). The map \(v\mapsto\langle\,\cdot\,,v\rangle\) is conjugate-linear. A bounded conjugate-linear functional has instead the unique form \(x\mapsto\langle v,x\rangle\).

**Proof.** For \(\ell=0\) take \(v=0\). Otherwise \(M=\ker\ell\) is closed: convergence preserves the equation \(\ell(x)=0\). Choose \(w\) with \(\ell(w)\ne0\) and set \(a=w-P_Mw\). Then \(a\ne0\), \(a\perp M\), and \(\ell(a)=\ell(w)\ne0\). Every \(x\) satisfies \(x-\ell(x)a/\ell(a)\in M\). Taking its inner product with \(a\) gives
\[
 \langle x,a\rangle=\ell(x)\|a\|^2/\ell(a).
\]
Thus \(v=\overline{\ell(a)}a/\|a\|^2\) represents \(\ell\). Cauchy–Schwarz gives \(\|\ell\|\le\|v\|\), and evaluation at \(v/\|v\|\), when \(v\ne0\), gives equality. Two representing vectors differ by a vector orthogonal to all of \(H\), and hence are equal. The scalar convention follows directly from sesquilinearity. For a conjugate-linear functional, conjugate its values, apply the linear assertion and conjugate back. \(\square\)

<a id="ha-lca-pre-hilbert-proposition-2-4"></a>
### Proposition 2.4. Bounded forms and adjoints

Every sesquilinear form \(B\) on \(H\) satisfying \(|B(x,y)|\le C\|x\|\|y\|\) has a unique bounded linear operator \(T\) with \(B(x,y)=\langle Tx,y\rangle\), and \(\|T\|\le C\). If \(0\le B(x,x)\le c\|x\|^2\), the same conclusion holds with a self-adjoint operator \(T\), \(0\le T\le cI\), and \(\|T\|\le c\). Here \(S\ge0\) means \(\langle Sx,x\rangle\ge0\) for all \(x\).

Every bounded linear map \(A:H\to K\) between Hilbert spaces has a unique bounded adjoint \(A^*:K\to H\) characterized by
\[
 \langle Ax,y\rangle_K=\langle x,A^*y\rangle_H.
 \tag{5}
\]
It satisfies \(\|A^*\|=\|A\|\), \(A^{**}=A\), \((BA)^*=A^*B^*\), and \((aA+bB)^*=\bar a A^*+\bar b B^*\) whenever the expressions are defined.

**Proof.** For fixed \(x\), the functional \(y\mapsto B(x,y)\) is bounded and conjugate-linear. Theorem 2.3 gives its representing vector \(Tx\), with \(\|Tx\|\le C\|x\|\). Uniqueness makes \(x\mapsto Tx\) linear and also proves uniqueness of \(T\). Under the diagonal bound, Lemma 1.1 gives \(|B(x,y)|\le c\|x\|\|y\|\), so the first assertion applies. Hermitian symmetry gives \(\langle Tx,y\rangle=\langle x,Ty\rangle\). The two diagonal inequalities are exactly \(T\ge0\) and \(cI-T\ge0\).

For fixed \(y\in K\), the functional \(x\mapsto\langle Ax,y\rangle\) is bounded and linear, with norm at most \(\|A\|\|y\|\). Theorem 2.3 gives \(A^*y\) and the same bound. The conjugation in the second variable, together with uniqueness, makes \(A^*\) linear. Moreover \(\|z\|=\sup_{\|y\|\le1}|\langle z,y\rangle|\), by Cauchy–Schwarz and the choice \(y=z/\|z\|\) for \(z\ne0\). Hence
\[
 \|Ax\|=\sup_{\|y\|\le1}|\langle x,A^*y\rangle|
 \le\|x\|\|A^*\|,
\]
which, with the preceding bound, proves equality of the norms. Applying (5) twice proves \(A^{**}=A\). Substitution into (5) proves the product and linear-combination formulas, with uniqueness identifying the adjoints. The identity obtained for the positive form says precisely \(T=T^*\). \(\square\)

## 3. The operator argument

Write \(\mathcal B(H)\) for the bounded linear operators on \(H\), with norm \(\|T\|=\sup_{\|x\|\le1}\|Tx\|\). In this section assume \(H\ne\{0\}\), so the identity \(I\) has norm one.

<a id="ha-lca-pre-hilbert-proposition-3-1"></a>
### Proposition 3.1. The Banach algebra of bounded operators

The space \(\mathcal B(H)\) is a unital Banach algebra with the adjoint operation of Proposition 2.4. It satisfies
\[
 \|T^*T\|=\|T\|^2.                                      \tag{6}
\]
If \(S=S^*\) belongs to a closed unital subalgebra \(A\subseteq\mathcal B(H)\), then its spectral radius in \(A\) is \(\|S\|\), provided the norm on \(A\) is the operator norm.

**Proof.** The norm axioms follow by applying the vector norm axioms to each unit vector, and \(\|STx\|\le\|S\|\|T\|\|x\|\) gives submultiplicativity. If \(T_n\) is Cauchy in operator norm, each \(T_nx\) is Cauchy in \(H\). Put \(Tx=\lim_nT_nx\). The \(T_n\) have a common finite norm bound, so passing to limits proves linearity and boundedness of \(T\). Given \(\varepsilon>0\), choose \(N\) with \(\|T_n-T_m\|\le\varepsilon\) for \(n,m\ge N\). Letting \(m\to\infty\) at each unit vector gives \(\|T_n-T\|\le\varepsilon\). This proves completeness. A closed subalgebra is complete by the same limit argument.

One direction of (6) follows from submultiplicativity and \(\|T^*\|=\|T\|\). For the other, \(\|Tx\|^2=\langle T^*Tx,x\rangle\le\|T^*T\|\|x\|^2\), by (5) and Lemma 1.1. Take the supremum over unit vectors. For self-adjoint \(S\), (6) gives \(\|S^2\|=\|S\|^2\). Every power \(S^{2^n}\) is self-adjoint, so iteration gives \(\|S^{2^n}\|=\|S\|^{2^n}\). The already proved [spectral-radius formula](banach-spectrum.md#ha-lca-pre-banach-theorem-2-2), applied to the Banach algebra \(A\), now gives \(r_A(S)=\|S\|\) by taking this subsequence of the full radius limit. \(\square\)

<a id="ha-lca-pre-hilbert-theorem-3-2"></a>
### Theorem 3.2. Continuous calculus for one self-adjoint operator

Let \(S=S^*\), \(M=\|S\|\), and \(A=\overline{\{p(S):p\text{ is a complex polynomial}\}}\). There is a nonempty compact set
\[
 K=\{\chi(S):\chi\in\Delta(A)\}\subseteq[-M,M]
\]
such that, for every continuous complex function \(f\) on \([-M,M]\), a bounded operator \(f(S)\in A\) is defined, and
\[
 \|f(S)\|=\max_{t\in K}|f(t)|.                           \tag{7}
\]
The assignment preserves sums, products, constants and conjugation, sends \(t\mapsto t\) to \(S\), and sends nonnegative real functions to positive operators. Every bounded operator commuting with \(S\) commutes with every \(f(S)\).

**Proof.** Products and adjoints of polynomials in \(S\) are again polynomials in \(S\). The continuity of multiplication and of adjoints shows that \(A\) is a commutative closed unital algebra invariant under adjoints. Its character space is nonempty compact Hausdorff by the earlier [character-space theorem](banach-spectrum.md#ha-lca-pre-banach-theorem-4-2), and its characters are contractive by the earlier [character and spectrum theorem](banach-spectrum.md#ha-lca-pre-banach-theorem-3-3).

We first show \(\chi(S)\) is real. The series
\[
 E(t)=\sum_{n=0}^\infty (itS)^n/n!
\]
converges in operator norm. The scalar majorant \(\sum(|t|M)^n/n!\) converges, and absolute convergence permits the Cauchy product: its tails are bounded by the corresponding tails of the product of the two scalar majorants. Grouping by total degree and using the finite binomial formula gives \(E(t)E(u)=E(t+u)\). Termwise adjoints give \(E(t)^*=E(-t)\). Consequently \(E(t)^*E(t)=I\), and (6) gives \(\|E(t)\|=1\). A character therefore satisfies
\[
 |e^{it\chi(S)}|=|\chi(E(t))|\le1\qquad(t\in\mathbb R).
\]
The scalar exponential identities are proved in the earlier [exponential-series lemma](banach-spectrum.md#ha-lca-pre-banach-lemma-1-3). Explicitly, writing \(\chi(S)=a+ib\) gives \(|e^{it(a+ib)}|=e^{-tb}\); for a positive real number \(r\), its series gives \(e^r>1\). If \(b\ne0\), choose \(t\) with \(-tb>0\), a contradiction. Thus \(\chi(S)\in\mathbb R\), and contractivity bounds it by \(M\). The coordinate map \(\chi\mapsto\chi(S)\) is continuous, so \(K\) is compact and nonempty.

For \(b\in A\), approximating it by polynomials in \(S\) shows \(\chi(b^*)=\overline{\chi(b)}\): the identity holds for polynomials because \(\chi(S)\) is real, and contractivity passes it to limits. The element \(b^*b\) is self-adjoint. The spectrum theorem for commutative Banach algebras and Proposition 3.1 yield
\[
 \sup_{\chi\in\Delta(A)}|\chi(b)|^2
 =r_A(b^*b)=\|b^*b\|=\|b\|^2.
 \tag{8}
\]
In particular, \(\|p(S)\|=\max_K|p|\).

If \(M>0\), the earlier [Bernstein approximation proof](uniform-approximation.md#ha-lca-pre-approx-lemma-1-1), after affine rescaling of the interval and separate approximation of real and imaginary parts, supplies polynomials \(p_n\) converging uniformly to \(f\) on \([-M,M]\). The last norm identity makes \(p_n(S)\) Cauchy. Define \(f(S)\) as its limit. The same identity proves independence of the polynomials and (7). Limits of sums, products and adjoints prove the asserted algebraic identities. If \(M=0\), then \(S=0\), \(K=\{0\}\), and define \(f(S)=f(0)I\), which gives the same conclusions.

If \(f\ge0\), its continuous square root \(g=\sqrt f\) is real and \(f(S)=g(S)^*g(S)\), which is positive by (5). Continuity of the square root on \([0,\infty)\) follows, for example, from \(|\sqrt a-\sqrt b|\le\sqrt{|a-b|}\), obtained by squaring and ordering \(a,b\). Finally, an operator commuting with \(S\) commutes with each polynomial and hence with its operator-norm limit \(f(S)\). \(\square\)

<a id="ha-lca-pre-hilbert-proposition-3-3"></a>
### Proposition 3.3. Positive square roots and separation of a nonscalar operator

Every bounded positive operator \(S\) has a unique bounded positive square root \(R\), with \(R^2=S\). This root commutes with every bounded operator commuting with \(S\).

If a bounded self-adjoint \(S\) is not a scalar multiple of \(I\), there are nonzero positive operators \(F,G\), obtained by the calculus in Theorem 3.2, such that \(FG=0\). Their closed ranges are nonzero orthogonal proper closed subspaces, each preserved by every bounded operator commuting with \(S\).

**Proof.** Positivity implies self-adjointness: apply Lemma 1.1 to \(B(x,y)=\langle Sx,y\rangle\), and then use (5). For this \(S\), the set \(K\) of Theorem 3.2 is contained in \([0,M]\). Indeed, suppose \(\lambda\in K\) and \(\lambda<0\). Put \(\varepsilon=-\lambda/2>0\), \(f(t)=\max(0,-\varepsilon-t)\), and \(A=f(S)\). Since \(f(\lambda)>0\), (7) gives \(A\ne0\). The function \(h(t)=(-\varepsilon-t)f(t)^2\) is nonnegative on the whole interval. The calculus gives
\[
 0\le\langle h(S)x,x\rangle
 =-\varepsilon\|Ax\|^2-\langle S Ax,Ax\rangle.
\]
Positivity of \(S\) forces \(Ax=0\) for every \(x\), a contradiction. Now apply the calculus to \(r(t)=\sqrt{\max(t,0)}\). The operator \(R=r(S)\) is positive, and \(r(t)^2=t\) on \(K\), so (7) gives \(R^2=S\). The commutation claim follows from Theorem 3.2.

For uniqueness let \(Q\ge0\), \(Q^2=S\). Then \(Q\) commutes with \(S\), and hence with \(R\). Set \(C=Q-R\), \(D=Q+R\). These are self-adjoint, \(D\ge0\), and \(CD=0\). If \(Dx=0\), then \(0=\langle Qx,x\rangle+\langle Rx,x\rangle\), so both nonnegative terms vanish. Cauchy–Schwarz for each positive form, from Lemma 1.1, then gives \(Qx=Rx=0\), hence \(Cx=0\). Thus \(C\) vanishes both on \(\ker D\) and on \(\overline{\operatorname{ran}D}\). By (5), \((\operatorname{ran}D)^\perp=\ker D\); Corollary 2.2 therefore decomposes \(H\) as the orthogonal sum of these two spaces. Hence \(C=0\).

For the second assertion, if \(K\) were the singleton \(\{c\}\), (7) applied to \(t-c\) would give \(S=cI\). Thus choose \(a<b\) in \(K\) and \(c\in(a,b)\). Set
\[
 F=(\max(c-t,0))(S),\qquad G=(\max(t-c,0))(S).
\]
They are positive and nonzero by (7), and their product is zero. For any \(x,y\), (5) gives \(\langle Fx,Gy\rangle=\langle GFx,y\rangle=0\); continuity extends this orthogonality to the two closed ranges. Neither range closure can be all of \(H\), since the other is nonzero. An operator commuting with \(S\) commutes with \(F,G\), so it maps each range into itself and, by continuity, preserves each closure. \(\square\)

## 4. Arbitrary orthogonal sums

For nonnegative real numbers \((a_i)_{i\in I}\), define \(\sum_{i\in I}a_i\) as the supremum of their finite subsums, with value \(+\infty\) allowed. For vectors \(x_i\) in a normed space, \(\sum_{i\in I}x_i=x\) means that the finite subsums converge to \(x\), directed by inclusion of their finite index sets.

<a id="ha-lca-pre-hilbert-lemma-4-1"></a>
### Lemma 4.1. Summability of an orthogonal family

If \(\sum_i a_i<\infty\), at most countably many \(a_i\) are nonzero, and the sum outside a suitable finite subset is as small as desired. If \((x_i)\) is an orthogonal family of vectors in a Hilbert space and \(\sum_i\|x_i\|^2<\infty\), then \(\sum_i x_i\) exists and
\[
 \left\|\sum_i x_i\right\|^2=\sum_i\|x_i\|^2.
 \tag{9}
\]
For a finite subset \(F\subseteq I\), the squared norm of the omitted sum is \(\sum_{i\notin F}\|x_i\|^2\).

**Proof.** If the finite-subsums bound is \(A\), the set \(\{i:a_i\ge1/n\}\) is finite: a finite subset with more than \(nA\) members would contradict the bound. Their union contains every index with \(a_i>0\). For any \(\delta>0\), the definition of the supremum supplies a finite \(F\) with \(\sum_{i\in F}a_i>A-\delta\). Every finite subsum outside \(F\) is then at most \(\delta\), so its supremum is at most \(\delta\).

For the vector assertion, all nonzero vectors lie in the countable set just found for \(a_i=\|x_i\|^2\). Enumerate it, or use a finite enumeration if it is finite. Orthogonality gives \(\|\sum_{i\in E}x_i\|^2=\sum_{i\in E}\|x_i\|^2\) for finite \(E\), by expansion. The tail bound makes the enumerated partial sums Cauchy, hence convergent. For any finite \(F\), subtract its sum and pass to the limit of the remaining enumerated sums; continuity of the norm gives the claimed tail identity. The same tail bound proves convergence of all finite subsums directed by inclusion, independently of the enumeration. Taking \(F=\varnothing\) gives (9). \(\square\)

<a id="ha-lca-pre-hilbert-theorem-4-2"></a>
### Theorem 4.2. Orthogonal expansions and Hilbert bases

Let \((e_i)_{i\in I}\) be an orthonormal family in \(H\), and \(M=\overline{\operatorname{span}\{e_i:i\in I\}}\). For \(x\in H\), put \(c_i=\langle x,e_i\rangle\). Then
\[
 \sum_i|c_i|^2\le\|x\|^2,\qquad
 P_Mx=\sum_i c_i e_i,\qquad
 \|P_Mx\|^2=\sum_i|c_i|^2.
 \tag{10}
\]
Every orthonormal set extends to one whose closed linear span is \(H\). Such a set is a Hilbert basis. For a Hilbert basis and \(x,y\in H\),
\[
 x=\sum_i\langle x,e_i\rangle e_i,\qquad
 \langle x,y\rangle=\sum_i\langle x,e_i\rangle
                              \overline{\langle y,e_i\rangle}.
 \tag{11}
\]
For an orthogonal family of nonzero vectors \(u_i\), the corresponding norm sum has weights \(\|u_i\|^2\): if \(d_i=\langle x,u_i\rangle/\|u_i\|^2\), then
\[
 P_Mx=\sum_i d_i u_i,\qquad
 \|P_Mx\|^2=\sum_i |d_i|^2\|u_i\|^2.                    \tag{12}
\]

**Proof.** For finite \(F\), let \(s_F=\sum_{i\in F}c_i e_i\). The vector \(x-s_F\) is orthogonal to every \(e_i\) with \(i\in F\), by direct evaluation of its inner products. Thus
\[
 \|x\|^2=\|x-s_F\|^2+\sum_{i\in F}|c_i|^2.
\]
Taking the supremum gives the first inequality in (10). Lemma 4.1 supplies \(s=\sum_i c_i e_i\), lying in \(M\). For each fixed \(j\), all sufficiently large finite index sets include \(j\), so continuity gives \(\langle x-s,e_j\rangle=0\). Hence \(x-s\in M^\perp\), proving \(s=P_Mx\) and the last equality in (10).

Apply the maximal principle to the set of orthonormal subsets containing the given set, ordered by inclusion. A chain union is again an orthonormal set, since any two of its vectors belong together to some member of the chain. A maximal set therefore exists. If its closed span were proper, Corollary 2.2 would give a nonzero orthogonal vector; after normalization it could be added, contradicting maximality. For this basis \(P_M=I\), giving the first formula in (11). The series in the second is absolutely convergent: finite-dimensional Cauchy–Schwarz, proved by Lemma 1.1 on \(\mathbb C^F\), bounds every finite subsum of its absolute values by \(\|x\|\|y\|\). Lemma 4.1 applied to these nonnegative absolute values gives countable support and arbitrarily small absolute tails. The triangle inequality bounds the absolute value of any scalar tail by its absolute sum, so the enumerated scalar series is Cauchy in \(\mathbb C\), and all finite subsums converge to the same limit. Passing to limits of the finite expansions gives the identity. Finally put \(e_i=u_i/\|u_i\|\) in (10); substitution gives (12), including its weights. \(\square\)

<a id="ha-lca-pre-hilbert-theorem-4-3"></a>
### Theorem 4.3. Hilbert direct sums

For any family of Hilbert spaces \(H_i\), define
\[
 \bigoplus_{i\in I}H_i
 =\{(x_i):x_i\in H_i,\ \sum_i\|x_i\|^2<\infty\},\qquad
 \langle x,y\rangle=\sum_i\langle x_i,y_i\rangle.
 \tag{13}
\]
This is a Hilbert space, and finite-support vectors are dense. If \(H_i\) are mutually orthogonal closed subspaces of \(H\), their external direct sum maps isometrically onto \(\overline{\operatorname{span}\bigcup_iH_i}\) by \((x_i)\mapsto\sum_i x_i\). In particular, a Hilbert basis identifies \(H\) with \(\ell^2(I)=\bigoplus_{i\in I}\mathbb C\).

**Proof.** The inequality \(\|x_i+y_i\|^2\le2\|x_i\|^2+2\|y_i\|^2\) proves closure under addition; scalar multiplication is immediate. Cauchy–Schwarz in each coordinate and then for finite scalar families gives
\[
 \sum_{i\in F}|\langle x_i,y_i\rangle|
 \le\left(\sum_{i\in F}\|x_i\|^2\right)^{1/2}
       \left(\sum_{i\in F}\|y_i\|^2\right)^{1/2}
 \le\|x\|\|y\|.
\]
The scalar absolute-summability argument in Theorem 4.2 therefore defines (13) independently of ordering. Sesquilinearity and positive definiteness follow coordinatewise.

Let \(x^{(n)}\) be Cauchy in the proposed norm. Each coordinate is Cauchy, since \(\|x_i^{(n)}-x_i^{(m)}\|\le\|x^{(n)}-x^{(m)}\|\), and hence has a limit \(x_i\in H_i\). For fixed \(\varepsilon>0\), choose \(N\) with \(\|x^{(n)}-x^{(m)}\|\le\varepsilon\) for \(n,m\ge N\). For any finite \(F\), pass to the coordinate limits as \(m\to\infty\), obtaining
\[
 \sum_{i\in F}\|x_i^{(n)}-x_i\|^2\le\varepsilon^2
 \qquad(n\ge N).
\]
Taking the supremum over finite \(F\) shows \(x-x^{(n)}\) belongs to the direct sum and has norm at most \(\varepsilon\). Thus \(x\) also belongs to the direct sum and \(x^{(n)}\to x\). This proves completeness. The finite-tail estimate in Lemma 4.1 proves density of finite-support vectors.

For internal orthogonal subspaces, Lemma 4.1 defines the summation map and gives its isometry. It is linear by passage from finite sums to limits. Its range contains all finite sums of subspace vectors and is closed by completeness, as proved in Theorem 1.2, so the range is exactly the indicated closed span. Taking one-dimensional spaces generated by a Hilbert basis gives the final assertion. \(\square\)

## 5. Weak compactness

The weak topology on \(H\) is the topology of pointwise convergence against its bounded linear functionals. By Theorem 2.3, it is equivalently generated by the coordinates \(v\mapsto\langle v,x\rangle\), \(x\in H\), or their complex conjugates.

<a id="ha-lca-pre-hilbert-theorem-5-1"></a>
### Theorem 5.1. Weak compactness of a Hilbert ball

For \(R\ge0\), the ball \(B_R=\{v:\|v\|\le R\}\) is compact Hausdorff for the weak topology. The norm is weakly lower semicontinuous. Every net in \(B_R\) has a weakly convergent subnet with limit in \(B_R\).

**Proof.** Map \(v\in B_R\) to \((\langle x,v\rangle)_{x\in H}\) in
\[
 P=\prod_{x\in H}\{z\in\mathbb C:|z|\le R\|x\|\}.
\]
Each disk is compact by the earlier [finite-dimensional compactness proof](banach-spectrum.md#ha-lca-pre-banach-lemma-1-1), and \(P\) is compact Hausdorff by [arbitrary product compactness](banach-spectrum.md#ha-lca-pre-banach-lemma-4-1). The image consists exactly of the points \(z\in P\) satisfying
\[
 z_{ax+by}=a z_x+b z_y \qquad(a,b\in\mathbb C,\ x,y\in H).
\]
Necessity is sesquilinearity. Conversely these equations define a linear functional of norm at most \(R\); Theorem 2.3 represents it as \(x\mapsto\langle x,v\rangle\) with \(\|v\|\le R\). Each equation is closed, so the image is closed in \(P\) and compact. The map is injective by uniqueness in Theorem 2.3, and the definition of the weak topology makes it a homeomorphism onto its image. This proves compactness and the Hausdorff property. The same argument, or the identity
\[
 \|v\|=\sup_{\|x\|\le1}|\langle v,x\rangle|,
\]
shows that every norm sublevel set is weakly closed, which is lower semicontinuity.

For completeness, the net conclusion follows directly from compactness as follows. Let \((v_d)_{d\in D}\) be a net in a compact space \(K\). The closures of the tails \(\{v_e:e\ge d\}\) have the finite-intersection property: any finite family contains the tail for a common upper bound of its indices. Their intersection contains a point \(v\), by compactness. Therefore every neighbourhood \(U\) of \(v\) meets every tail. Form the directed set of triples \((d,U,e)\) with \(e\ge d\) and \(v_e\in U\), ordering triples by increase of both \(d,e\) and decrease of \(U\). Given two triples, take an index larger than all their indices, intersect their neighbourhoods and choose a later \(e\) with \(v_e\) in that intersection. This gives an upper bound. The map \((d,U,e)\mapsto e\) is order-preserving and cofinal; the resulting subnet converges to \(v\), because later neighbourhoods lie inside any prescribed one. Apply this construction to \(K=B_R\) with its weak topology. \(\square\)

## 6. \(L^2\) on a general measure space

<a id="ha-lca-pre-hilbert-theorem-6-1"></a>
### Theorem 6.1. The Hilbert space \(L^2\)

For any measure space \((X,\Sigma,\mu)\), the measurable complex functions with \(\int|f|^2\,d\mu<\infty\), modulo almost-everywhere equality, form a Hilbert space with
\[
 \langle f,g\rangle=\int f\bar g\,d\mu,\qquad
 \|f\|_2=\left(\int|f|^2\,d\mu\right)^{1/2}.
 \tag{14}
\]
No sigma-finiteness is required. If \(\sum_n\|g_n\|_2<\infty\), then \(\sum_n|g_n(x)|<\infty\) almost everywhere and the resulting series converges in \(L^2\), with norm at most \(\sum_n\|g_n\|_2\).

**Proof.** The pointwise inequality \(2|f\bar g|\le|f|^2+|g|^2\) makes the product integrable, using the [integral and null-set properties](integration-and-l1.md#ha-lca-pre-integral-theorem-1-2) and [complex integral inequalities](integration-and-l1.md#ha-lca-pre-integral-lemma-2-1). Formula (14) is therefore well defined on classes and is sesquilinear. Its diagonal is nonnegative and vanishes exactly for the zero class by [the zero-integral criterion](integration-and-l1.md#ha-lca-pre-integral-corollary-1-3). The bound \(|f+g|^2\le2|f|^2+2|g|^2\) proves closure under addition. Lemma 1.1 now proves Cauchy–Schwarz and the norm triangle inequality for \(L^2\).

Choose finite measurable representatives of the \(g_n\), modifying them on null sets if necessary; [measurable operations](integration-and-l1.md#ha-lca-pre-integral-lemma-1-1) justify all the following functions. Put \(h_N=\sum_{n\le N}|g_n|\). The triangle inequality gives
\[
 \int h_N^2\,d\mu\le\left(\sum_{n\le N}\|g_n\|_2\right)^2.
\]
Since \(h_N^2\) increases, the proved [monotone convergence theorem](integration-and-l1.md#ha-lca-pre-integral-theorem-1-2) gives
\[
 \int\left(\sum_n|g_n|\right)^2\,d\mu
 \le\left(\sum_n\|g_n\|_2\right)^2<\infty.
 \tag{15}
\]
The sum of absolute values is finite almost everywhere by the same zero/infinity integral criteria. Define \(g=\sum_n g_n\) where the series converges and \(g=0\) on the exceptional measurable null set. It is measurable by the earlier measurable-limit result and belongs to \(L^2\) by (15). Applied to the tail, the same estimate gives
\[
 \left\|g-\sum_{n\le N}g_n\right\|_2
 \le\sum_{n>N}\|g_n\|_2\longrightarrow0.
\]

Finally let \((f_n)\) be an \(L^2\)-Cauchy sequence. Choose a subsequence \(f_{n_k}\) such that \(\|f_{n_{k+1}}-f_{n_k}\|_2\le2^{-k}\). Such a subsequence is obtained recursively from the Cauchy property with \(n_{k+1}>n_k\). The series assertion applied to its differences gives an \(L^2\) limit of the subsequence after adding \(f_{n_1}\). The triangle inequality and the Cauchy property show that the whole sequence has that limit. This proves completeness. \(\square\)

<a id="ha-lca-pre-hilbert-proposition-6-2"></a>
### Proposition 6.2. Density and representatives

On any measure space, finite linear combinations of indicators of finite-measure sets are dense in \(L^2\).

Suppose additionally that \(X\) is locally compact Hausdorff, \(\Sigma\) contains its Borel sets, \(\mu\) is finite on compact sets, and every finite-measure member of \(\Sigma\) is inner regular by compact sets. Then \(C_c(X)\) is dense in \(L^2(\mu)\). Nonnegative \(L^2\) classes admit nonnegative \(C_c\) approximants. Every \(L^2\) class has a Borel representative zero outside a countable union of compact sets.

**Proof.** For a finite measurable representative \(f\), put \(E_n=\{1/n\le|f|\le n\}\). Then \(\mu(E_n)\le n^2\|f\|_2^2<\infty\). The sets increase to \(\{f\ne0\}\), and the already proved [dominated convergence theorem](integration-and-l1.md#ha-lca-pre-integral-theorem-2-2), applied to \(|f|^2 1_{X\setminus E_n}\), shows \(f1_{E_n}\to f\) in \(L^2\). On \(E_n\), round each of the bounded real and imaginary parts to a finite grid. With mesh \(\delta\), the pointwise error is at most \(\sqrt2\delta\), and the squared \(L^2\) error is at most \(2\delta^2\mu(E_n)\). The resulting simple function has finite-measure level sets. Nonnegative real functions can be rounded down on a nonnegative grid. This proves the first assertion and its positive version.

Let \(E\in\Sigma\) have finite measure and fix \(\varepsilon>0\). Choose a compact \(K\subseteq E\) with \(\mu(E\setminus K)<\varepsilon\). The cutoff construction in the proof of the earlier [\(C_c\)-density theorem](integration-and-l1.md#ha-lca-pre-integral-theorem-3-1), applied to this compact Borel set, gives \(u\in C_c(X)\), \(0\le u\le1\), \(u=1\) on \(K\), and \(\int|u-1_K|\,d\mu<\varepsilon\). That construction uses only finite compact restrictions of the Borel measure, whose compact inner regularity follows from the present assumptions. Consequently
\[
 \|u-1_E\|_2^2
 =\int_E|1-u|^2\,d\mu+\int_{X\setminus E}u^2\,d\mu
 \le\mu(E\setminus K)+\int_{X\setminus K}u\,d\mu
 <2\varepsilon.
\]
Approximate the finitely many indicators in the simple approximation and use the triangle inequality. The coefficients are nonnegative in the positive case, so their cutoff combination is nonnegative.

For the representative assertion, choose \(u_n\in C_c(X)\) with \(\|u_n-f\|_2\le4^{-n}\). Then \(\sum_n\|u_{n+1}-u_n\|_2<\infty\). Theorem 6.1 shows that \(u_n\) converges pointwise almost everywhere and in \(L^2\); its \(L^2\) limit is \(f\) by the chosen errors. The set on which a sequence of complex Borel functions converges is Borel: the Cauchy criterion expresses it using countable unions and intersections of inequalities \(|u_m-u_n|\le1/k\). Define \(u\) to be the pointwise limit there and zero elsewhere. The earlier measurable-limit result makes \(u\) Borel. It represents \(f\), and it vanishes outside \(\bigcup_n\operatorname{supp}u_n\). Thus it has the required support without a global countability assumption on \(X\) or \(\mu\). \(\square\)

## 7. Unitary representations

A unitary operator on \(H\) is a surjective linear isometry \(U:H\to H\). By (2) and (5), it preserves inner products and satisfies \(U^*=U^{-1}\). Conversely \(U^*U=UU^*=I\) implies both norm preservation and surjectivity. A unitary representation of a topological group \(G\) is a homomorphism \(g\mapsto\pi(g)\) into these operators such that \(g\mapsto\pi(g)x\) is norm-continuous for every \(x\in H\).

The free Bekka–de la Harpe–Valette draft supplies the representation definitions and comparison statements in A.1.1–A.1.7, A.1.10–A.1.11, A.2.1–A.2.3. The following proofs supply the Hilbert constructions, strong-continuity arguments and the operator step in Schur's lemma in full.

<a id="ha-lca-pre-hilbert-proposition-7-1"></a>
### Proposition 7.1. Continuity and cyclic decomposition

For a homomorphism \(\pi:G\to U(H)\), strong continuity follows if \(g\mapsto\pi(g)x\) is continuous for every \(x\) in a dense linear subspace. Strong continuity is equivalent to continuity of every coefficient \(g\mapsto\langle\pi(g)x,y\rangle\); it also makes \((g,x)\mapsto\pi(g)x\) jointly continuous.

Every unitary representation is an orthogonal direct sum of cyclic representations. Here a vector \(v\) is cyclic when \(\overline{\operatorname{span}\{\pi(g)v:g\in G\}}=H\). Arbitrary direct sums of unitary representations are strongly continuous.

**Proof.** For \(x\in H\), approximate it by \(z\) in the dense subspace and use
\[
 \|\pi(g)x-\pi(g_0)x\|
 \le2\|x-z\|+\|\pi(g)z-\pi(g_0)z\|.
 \tag{16}
\]
This proves the first assertion directly from the neighbourhood definition of continuity. Strong continuity implies coefficient continuity by Cauchy–Schwarz. Conversely, continuity of all coefficients and the identity
\[
 \|\pi(g)x-\pi(g_0)x\|^2
 =2\|x\|^2-2\operatorname{Re}\langle\pi(g)x,\pi(g_0)x\rangle
\]
give strong continuity at every \(g_0\). Joint continuity follows from
\[
 \|\pi(g)x-\pi(g_0)x_0\|
 \le\|x-x_0\|+\|\pi(g)x_0-\pi(g_0)x_0\|.
\]

If a closed subspace \(M\) is invariant under all \(\pi(g)\), then \(\pi(g)M=M\), by applying invariance also to \(g^{-1}\). Its orthogonal complement is invariant because
\[
 \langle\pi(g)x,m\rangle=\langle x,\pi(g^{-1})m\rangle=0
 \quad(x\in M^\perp,\ m\in M).
 \tag{17}
\]
For any \(v\), its closed orbit span \(H_v\) is invariant: multiplying each orbit vector by \(\pi(a)\) gives another orbit vector, and boundedness passes invariance to the closure. The restriction to \(H_v\) is a cyclic representation.

Use the maximal principle on families of mutually orthogonal nonzero closed cyclic invariant subspaces, ordered by inclusion. These families form a set, as they consist of subsets of \(H\). A chain union retains the required properties, so there is a maximal family \((H_i)\). If its closed span \(M\) were proper, Corollary 2.2 would give \(0\ne v\in M^\perp\). Equation (17) and the invariance of \(M\) put the whole cyclic space \(H_v\) in \(M^\perp\). It could be added to the family, contradicting maximality. Thus \(M=H\), and Theorem 4.3 identifies the representation with the orthogonal direct sum of its cyclic restrictions. The zero space corresponds to the empty sum.

For a family \(\pi_i\), the coordinatewise operator \((x_i)\mapsto(\pi_i(g)x_i)\) is an isometry of the Hilbert direct sum and has inverse given by \(g^{-1}\). It is a homomorphism. On a vector with finite support, continuity follows by adding finitely many squared coordinate differences. Such vectors are dense by Theorem 4.3, so (16) proves strong continuity on the whole direct sum. \(\square\)

<a id="ha-lca-pre-hilbert-theorem-7-2"></a>
### Theorem 7.2. Schur's lemma

A unitary representation on a nonzero Hilbert space is called irreducible if its only closed invariant subspaces are \(\{0\}\) and \(H\). It is irreducible if and only if its bounded commutant
\[
 \pi(G)'=\{T\in\mathcal B(H):T\pi(g)=\pi(g)T\text{ for every }g\in G\}
\]
consists exactly of the scalar multiples of \(I\).

Every nonzero vector in an irreducible representation is cyclic. If \(G\) is abelian, its irreducible unitary representations are precisely its one-dimensional continuous unitary characters.

**Proof.** For a closed invariant subspace \(M\), (17) shows that \(M^\perp\) is invariant as well. Decomposing \(x=P_Mx+(I-P_M)x\) and applying \(\pi(g)\) shows, by uniqueness of the orthogonal decomposition, that \(P_M\pi(g)=\pi(g)P_M\). Conversely, if this commutation holds, the range \(M\) of \(P_M\) is invariant. If all commuting operators are scalar, then \(P_M=cI\); from \(P_M^2=P_M\) and \(H\ne0\), \(c^2=c\), so \(M\) is zero or all of \(H\).

Now suppose the representation is irreducible. If \(T\) commutes with all \(\pi(g)\), take adjoints of its commutation with \(\pi(g^{-1})\) to see that \(T^*\) does too. Thus
\[
 S_1=(T+T^*)/2,\qquad S_2=(T-T^*)/(2i)
\]
are self-adjoint members of the commutant, with \(T=S_1+iS_2\). If either \(S_j\) were nonscalar, Proposition 3.3 would supply a nonzero proper closed subspace preserved by every \(\pi(g)\), a contradiction. Therefore both are scalar and so is \(T\). Scalar operators plainly commute, proving the equivalence.

The closed orbit span of a nonzero vector is a nonzero invariant subspace by Proposition 7.1 and hence is all of \(H\). If \(G\) is abelian, each \(\pi(g)\) belongs to the commutant, so \(\pi(g)=\chi(g)I\) for a scalar of modulus one. Every one-dimensional subspace is then invariant. Such a subspace is closed: if \(a_n v\) converges with \(v\ne0\), the identity \(\|(a_n-a_m)v\|=|a_n-a_m|\|v\|\) makes \(a_n\) converge in \(\mathbb C\). Irreducibility therefore forces \(\dim H=1\). For a unit vector \(v\), \(\chi(g)=\langle\pi(g)v,v\rangle\) is continuous; the homomorphism law makes it a character. Conversely, a continuous character acts unitarily and continuously on \(\mathbb C\), whose only linear subspaces are zero and itself. \(\square\)

<a id="ha-lca-pre-hilbert-proposition-7-3"></a>
### Proposition 7.3. Tensor and conjugate representations

For Hilbert spaces \(H,K\), there is a Hilbert tensor product \(H\otimes K\) containing finite sums of elementary tensors as a dense subspace and satisfying
\[
 \langle x\otimes y,x'\otimes y'\rangle
       =\langle x,x'\rangle\langle y,y'\rangle,\qquad
 \|x\otimes y\|=\|x\|\|y\|.
 \tag{18}
\]
If \(\pi,\rho\) are unitary representations of \(G\), then
\[
 (\pi\otimes\rho)(g)(x\otimes y)=\pi(g)x\otimes\rho(g)y
\]
extends to a strongly continuous unitary representation. Diagonal coefficients multiply:
\[
 \langle(\pi\otimes\rho)(g)(x\otimes y),x\otimes y\rangle
 =\langle\pi(g)x,x\rangle\langle\rho(g)y,y\rangle.
 \tag{19}
\]
There is also a conjugate Hilbert space \(\bar H\) and a conjugate representation whose diagonal coefficients are the complex conjugates of those of \(\pi\).

**Proof.** Begin with the free vector space on the symbols \((x,y)\in H\times K\) and quotient by the relations expressing linearity separately in \(x\) and \(y\). Write the class of \((x,y)\) as \(x\otimes y\). On finite sums define the sesquilinear form by extending the right side of (18). Each defining relation has zero pairing with every symbol, in either variable, by sesquilinearity in the original Hilbert spaces. The form therefore descends to the quotient.

To check positive definiteness, any given tensor has an expression involving finitely many \(x\)'s and \(y\)'s. Their finite spans have finite orthonormal bases: process the given spanning list in order, subtract its projections onto the already selected orthonormal vectors, omit a zero remainder and normalize a nonzero one. Direct inner-product evaluation proves orthogonality at each step, and induction shows that the resulting list spans the original finite list. In these bases \(e_1,\ldots,e_r\) and \(f_1,\ldots,f_s\), bilinearity writes the tensor as \(\sum_{i,j}a_{ij}e_i\otimes f_j\). Its squared norm by the proposed form is \(\sum_{i,j}|a_{ij}|^2\). Thus a zero norm forces every coefficient to vanish and the tensor itself to be zero. This proves positive definiteness; Theorem 1.2 constructs its Hilbert completion and proves (18).

The proposed action respects the quotient relations because \(\pi(g)\) and \(\rho(g)\) are linear. Formula (18) shows it preserves the form on all finite sums, and the action at \(g^{-1}\) is its inverse. Theorem 1.2 extends it to a surjective isometry of the completion. The homomorphism law holds on elementary tensors, then on their finite sums, and then everywhere by continuity. For an elementary tensor,
\[
 \|\pi(g)x\otimes\rho(g)y-\pi(g_0)x\otimes\rho(g_0)y\|
 \le \|\pi(g)x-\pi(g_0)x\|\,\|y\|
      +\|x\|\,\|\rho(g)y-\rho(g_0)y\|.
\]
This tends to zero. Finite sums are therefore continuous orbit vectors, and their density together with Proposition 7.1 proves strong continuity on the completion. Equation (19) is (18).

Define \(\bar H\) using symbols \(\bar x\), with addition \(\bar x+\bar y=\overline{x+y}\), scalar action \(a\bar x=\overline{\bar a x}\), and inner product \(\langle\bar x,\bar y\rangle_{\bar H}=\langle y,x\rangle_H\). The vector-space axioms, sesquilinearity and positivity follow by substitution; the norm is \(\|\bar x\|=\|x\|\), so completeness follows from completeness of \(H\). Define \(\bar\pi(g)\bar x=\overline{\pi(g)x}\). The scalar rule makes this map linear. Norm preservation, the inverse at \(g^{-1}\), the homomorphism law and strong continuity follow directly from those of \(\pi\). Finally its diagonal coefficient is \(\langle x,\pi(g)x\rangle=\overline{\langle\pi(g)x,x\rangle}\). \(\square\)
