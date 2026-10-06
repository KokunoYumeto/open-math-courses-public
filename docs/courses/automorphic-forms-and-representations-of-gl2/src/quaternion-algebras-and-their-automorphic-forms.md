# Quaternion algebras and their automorphic forms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The split algebra \(M_2\) produces the noncompact modular quotient and its Eisenstein spectrum. A quaternion division algebra gives another form of the same local matrix group, but its rational quotient is compact after removing the centre. In the definite rational case, imposing weight zero and maximal finite level reduces automorphic forms to functions on finitely many ideal classes. Hecke operators then become explicit integer matrices. We will obtain a two-dimensional example whose nonconstant eigenvalue is the coefficient \(-2\) of the level-eleven newform.

The representation conventions are those of Lesson 12. Central simple algebras and the Brauer group, Sections 6–7, supplies quaternion conjugation, reduced trace and reduced norm. The arithmetic proof provider is now the written class-field lesson Brauer groups of local and global fields: Proposition 24.1 and Theorem 24.2 prove the local invariant and its restriction rule; Theorem 24.4 proves the global localization exact sequence. We deduce the needed quaternion classification from these statements below, including global fields of characteristic two. Corollary 24.5 of that provider gives the rational case. Our inner products are linear in the first variable.

## 1. The local compact quotient

A quaternion algebra \(D\) over a field \(F\) is a central simple algebra of dimension four. It is either \(M_2(F)\) or a division algebra: the matrix size and the dimension of its division representative multiply to four. Write \(\overline x\) for its standard conjugation, and
\[
\operatorname{trd}(x)=x+\overline x,\qquad
\operatorname{nrd}(x)=x\overline x,\qquad
\operatorname{nrd}(xy)=\operatorname{nrd}(x)\operatorname{nrd}(y).
\tag{1.1}
\]
In characteristic different from two, the symbol algebra \((a,b)_F\) has generators satisfying \(i^2=a\), \(j^2=b\), \(ij=-ji\). Its norm is \(x_0^2-a x_1^2-b x_2^2+ab x_3^2\). The cyclic model (1.2) below works in every characteristic. In the split algebra, reduced norm is determinant.

**Local classification.** If \(F\) is a nonarchimedean local field, there is exactly one quaternion division algebra up to \(F\)-isomorphism. Let \(L/F\) be the unramified quadratic extension and \(\varpi\) a uniformizer. This algebra and its maximal order have the descriptions
\[
\begin{gathered}
D=L\oplus Lj,\qquad j^2=\varpi,\qquad jx=\overline xj\quad(x\in L),\\
\mathcal O_D=\mathcal O_L\oplus\mathcal O_Lj,\qquad
v_D(x)=v_F(\operatorname{nrd}(x))\quad(x\ne0).
\end{gathered}
\tag{1.2}
\]
Here \(v_D\) is a discrete valuation with \(v_D(j)=1\); its valuation ring is \(\mathcal O_D\). Notice the sign \(\operatorname{nrd}(j)=-\varpi\), since \(\overline j=-j\). The valuation still equals one.

**Proof of classification.** Quaternion conjugation identifies an algebra with its opposite, so its Brauer class has order dividing two. Theorem 24.2 of the linked class-field lesson identifies \(\operatorname{Br}(F)\) with \(\mathbb Q/\mathbb Z\). A division quaternion algebra has nonzero class and therefore invariant \(1/2\). Proposition 24.1 gives that invariant to the unramified cyclic algebra in (1.2), with arithmetic Frobenius and parameter \(\varpi\). Its explicit norm calculation just below proves it is division. Thus every division quaternion algebra has the same Brauer class as this model. Uniqueness of the division representative, proved in the linked central-simple-algebra lesson, makes them isomorphic. Over \(\mathbb R\), Theorem 24.2 gives just two classes; Hamilton's positive definite norm makes it the nonzero degree-two division representative. Over \(\mathbb C\) the Brauer group is zero and every quaternion algebra is split. This proves all three classifications. Their original locators are Voight, Theorem 13.3.11, with Lemma 13.3.2 and Proposition 13.3.4. \(\square\)

The valuation and order assertions in this model can be checked directly. For \(x=a+bj\),
\[
\operatorname{nrd}(x)=N_{L/F}(a)-\varpi N_{L/F}(b),\qquad
v_D(x)=\min\{2v_L(a),\,1+2v_L(b)\}.
\]
The two finite valuations have different parity and cannot cancel. This proves anisotropy, the valuation inequality for addition, and the stated valuation ring; multiplicativity follows from (1.1). That ring is closed under multiplication by the displayed relations and is a full compact lattice. Every order is contained in it, because an element of negative valuation would have powers escaping that compact order. It is therefore the unique maximal order. These checks work also in residue characteristic two.

**Theorem 1.1.** For the local division algebra, \(D^\times/F^\times\) is compact. Every irreducible smooth complex representation of \(D^\times\) is finite-dimensional.

**Proof of compactness.** A scalar \(\varpi\) has valuation two, because its reduced norm is \(\varpi^2\). Multiplying an element by a suitable scalar power makes its valuation either zero or one. The elements of valuation zero are \(\mathcal O_D^\times\); those of valuation one are \(j\mathcal O_D^\times\). Consequently
\[
D^\times=\varpi^{\mathbb Z}C,
\qquad C=\mathcal O_D^\times\cup j\mathcal O_D^\times.
\tag{1.3}
\]
The order is a compact rank-four \(\mathcal O_F\)-lattice. Its units are a closed subset, being the inverse image of \(\mathcal O_F^\times\) under the continuous norm map. Thus \(C\) is compact and maps onto the central quotient, proving the assertion. \(\square\)

**Proof of finite dimension.** We first justify the scalar action needed in using (1.3); an unrestricted infinite-dimensional form of Schur's lemma would not suffice.

Let \(V\) be irreducible and smooth, and choose \(v\ne0\). It is cyclic by irreducibility. Its stabilizer contains an open subgroup. The second-countable group \(D^\times\) has only countably many cosets of any open subgroup: these cosets are disjoint open sets, and each contains a distinct member of a countable basis. The orbit of \(v\), and hence a spanning set of \(V\), is countable.

Let \(T\) be the action of the central scalar \(\varpi\). Every \(T-\lambda\) is a module endomorphism. If it is nonzero, its kernel is zero and its image is all of \(V\), by irreducibility. Suppose \(T\) were not scalar. Every \(T-\lambda\) would then be invertible, and so would every nonzero polynomial in \(T\), after factoring that polynomial over \(\mathbb C\). The vectors
\[
(T-\lambda)^{-1}v\qquad(\lambda\in\mathbb C)
\tag{1.4}
\]
would be linearly independent. Indeed, multiply a finite alleged relation by \(\prod_r(T-\lambda_r)\). The resulting polynomial is
\(P(t)=\sum_r c_r\prod_{s\ne r}(t-\lambda_s)\); evaluating at \(\lambda_r\) shows that it is nonzero if some \(c_r\ne0\). Then \(P(T)v=0\) contradicts invertibility. An uncountable independent set contradicts the countable spanning set. Therefore \(T=c\operatorname{id}\), with \(c\ne0\).

Smoothness makes the map \(x\mapsto xv\) locally constant. On the compact set \(C\) it has finite image, since finitely many stabilizer cosets cover \(C\). Formula (1.3) now says that the whole orbit of \(v\) is contained in the union of scalar multiples of this finite set. It spans a finite-dimensional space, which is \(V\). \(\square\)

**Corollary 1.2 — the precise finite-quotient assertion.** Such a representation has a smooth central character \(\chi\). Its projective image is finite. After twisting by an unramified character of the reduced norm, the representation itself factors through a finite quotient of \(D^\times\).

**Proof.** Finite-dimensional Schur's lemma makes every central element scalar. The common stabilizer of a basis is open and lies in the kernel \(U\) of the representation. Thus \(U\) is an open normal subgroup. The projective representation has kernel containing \(F^\times U\), and
\(D^\times/(F^\times U)\) is a discrete quotient of the compact group in Theorem 1.1, hence finite.

Choose \(b\in\mathbb C^\times\) with \(b^2=c^{-1}\), and define the unramified character \(\nu(x)=b^{v_F(x)}\). The twist \(\nu\circ\operatorname{nrd}\) makes the scalar \(\varpi\) act as \(b^2c=1\). Its kernel \(U'\) is open, so it factors through
\(D^\times/(\varpi^{\mathbb Z}U')\). This quotient is discrete and has the compact set \(C\) as a set of representatives, hence is finite. \(\square\)

A representation with nontrivial \(\chi\) need not be a representation of \(D^\times/F^\times\). For example, the one-dimensional character \(|\operatorname{nrd}|_F\) acts on a scalar \(a\) by \(|a|_F^2\). The finite assertion modulo the centre is about its projective action; literal descent requires trivial central character.

## 2. Ramification and the global group

For a quaternion algebra over a global field \(F\), set
\[
\operatorname{Ram}(D)=\{v:D\otimes_FF_v\text{ is division}\}.
\tag{2.1}
\]
**Global classification.** This set is finite, contains no complex place, has even cardinality, and determines the algebra up to \(F\)-isomorphism. Conversely each finite even set of noncomplex places occurs.

**Proof.** Theorem 24.4 of the linked class-field lesson proves that localization embeds \(\operatorname{Br}(F)\) into the direct sum of its local Brauer groups, with image exactly the tuples whose invariant sum is zero. The local classification just proved identifies the quaternion invariants as zero or \(1/2\). Finite support and the sum law give finiteness and even cardinality. The tuple determines the Brauer class. Equal degree-two central simple algebras in that class are isomorphic by uniqueness of the division representative and their matrix size.

For existence, let \(S\) be a nonempty finite even set of noncomplex places. The localization theorem supplies a class \(\beta\) with invariant \(1/2\) at \(S\) and zero elsewhere. We must show that it has a degree-two representative; a two-torsion Brauer class over an arbitrary field would not suffice. Choose a separable quadratic extension \(E/F\) that remains a field at every place in \(S\). In characteristic different from two, weak approximation supplies \(d\in F\) of valuation one at each specified finite place and negative at each specified real place. Then \(E=F(\sqrt d)\) has the required local degree two. In characteristic two all places are finite. At each place in \(S\), choose an integral \(a_v\) whose residue has trace one to \(\mathbb F_2\), and use weak approximation to choose \(a\in F\) congruent to \(a_v\) modulo that maximal ideal. The polynomial \(X^2+X+a\) is locally irreducible: a root of negative valuation is impossible, and an integral root would have residue with trace-zero Artin–Schreier image. Its derivative is one. Thus it defines a separable quadratic field \(E/F\) with the same local property, also in characteristic two.

Restriction multiplies a local invariant by its extension degree, by Theorem 24.2. Hence every invariant of \(\beta|_E\) is zero: degree two kills \(1/2\) at \(S\), and the other original invariants were zero. Global injectivity over \(E\) gives \(\beta|_E=0\). The finite splitting criterion in the linked central-simple-algebra lesson, Theorem 4.2, now gives an algebra in class \(\beta\) of degree \([E:F]=2\). Because \(S\ne\varnothing\), it is nonsplit and therefore quaternion division. For \(S=\varnothing\), use \(M_2(F)\). This proves existence in every global field and completes the classification. The rational version is Voight, Main Theorem 14.1.3 and Proposition 14.2.1; the general version is Main Theorem 14.6.1 and Remark 14.6.10. \(\square\)

Over \(\mathbb Q\), the algebra is **definite** when \(\infty\in\operatorname{Ram}(D)\), so \(D_\infty\simeq\mathbb H\). Write \(B_{p,\infty}\) for the algebra ramified exactly at \(p\) and \(\infty\), and \(d_D\) for the product of its finite ramified primes. An indefinite algebra can still be division over \(\mathbb Q\): splitting at infinity does not make it split at all places. At a split finite place its multiplicative group is \(\mathrm{GL}_2(F_v)\); at a ramified one Theorem 1.1 applies.

Put \(G=D^\times\). An automorphic form is a left \(G(\mathbb Q)\)-invariant smooth function on \(G(\mathbb A)\), right invariant under some finite compact open subgroup, finite under a maximal compact group at infinity and under the centre of the real enveloping algebra, with the usual moderate growth. We can impose a central character
\[
\phi(zg)=\omega(z)\phi(g),\qquad
\omega:\mathbb Q^\times\backslash\mathbb A^\times\longrightarrow\mathbb C^\times.
\tag{2.2}
\]
For unitary \(\omega\), its Hilbert space is measured modulo the adelic centre, exactly as in Lesson 4. Compactness below makes the growth condition automatic in fixed central character, and makes smooth automorphic forms square integrable. Square integrability here always means modulo the centre with a unitary central character.

For a division quaternion algebra, there are no proper rational parabolic subgroups. In the matrix form of this rank-one group, a proper parabolic stabilizes a nontrivial flag, equivalently a proper nonzero right ideal of reduced dimension one. To see the descent, split the algebra over a finite Galois extension. The right ideal associated with a line consists of matrices whose images lie in that line. Conjugating the parabolic conjugates this ideal, so a rational parabolic makes the corresponding ideal stable under the descent action. Galois descent of a linear subspace then gives a proper nonzero right ideal of the rational algebra. A division algebra has no such ideal: if an ideal contains \(x\ne0\), it contains \(xx^{-1}=1\). Thus there are no constant-term conditions to impose, and all its automorphic forms are cuspidal in the rational-parabolic sense. This includes the characters \(\xi\circ\operatorname{nrd}\). The exclusion of such characters in transfer to the cuspidal \(\mathrm{GL}_2\) spectrum will matter in Lesson 19.

## 3. A finite class set and a compact adelic quotient

We shall use the following local-to-global fact explicitly. If full \(\mathbb Z_\ell\)-lattices \(L_\ell\subset D_\ell\) equal a fixed full lattice's completions at almost all primes, then
\[
L=D\cap\prod_\ell L_\ell
\]
is a full \(\mathbb Z\)-lattice with \(L\otimes\mathbb Z_\ell=L_\ell\) at every prime. To prove it, choose \(M\ge1\) such that
\[
M\mathcal O_\ell\subset L_\ell\subset M^{-1}\mathcal O_\ell
\]
for all primes, with equality to \(\mathcal O_\ell\) outside the divisors of \(M\). The finite group \(M^{-1}\mathcal O/M\mathcal O\) is the direct sum of its primary parts, by the integer Chinese remainder theorem. Choose in each part the subgroup prescribed by \(L_\ell/M\mathcal O_\ell\), and take its inverse image in \(M^{-1}\mathcal O\). This constructs exactly \(L\) and proves the completion assertion. Containment, products and multiplication stability can all be checked in these completions; an element is in the global lattice exactly when it is in every local lattice. In particular the same construction glues local right ideals or orders. This is the lattice dictionary used below.

Let \(D\) be definite over \(\mathbb Q\), and let \(\mathcal O\) be a maximal order. A fractional right ideal is a full lattice \(I\subset D\) stable under right multiplication by \(\mathcal O\). At every finite place it is principal, \(I_p=x_p\mathcal O_p\). At a split place, matrix units show that a right ideal consists of matrices with columns in a fixed full rank-two lattice; a basis matrix for that lattice is such an \(x_p\). At a division place, choose \(a\) of least valuation in the ideal. Every \(b\) in it has \(a^{-1}b\in\mathcal O_D\), and right stability gives the converse inclusion, so the ideal is \(a\mathcal O_D\). The local-global dictionary is Voight, Section 27.6, especially Lemma 27.6.8. Two ideals are equivalent if \(J=\alpha I\) for \(\alpha\in D^\times\). Their classes form \(\operatorname{Cls}(\mathcal O)\).

We use the same dictionary for norm and inverse. Define the positive rational \(q_I\) by \(q_I\mathbb Z=\operatorname{nrd}(I)\). Let
\[
\mathcal O_L(I)=\{a\in D:aI\subset I\},\qquad
I^{-1}=\{a\in D:aI\subset\mathcal O\}.
\tag{3.1}
\]
Local multiplication gives \(\overline I=q_I I^{-1}\), and
\(I J^{-1}=\{a:aJ\subset I\}\). These follow locally from principal ideals and then by intersecting the local lattices. The latter product is the additive span of products; it is a lattice of homomorphisms, not a commutative ideal product.

**Lemma 3.1.** The class set is finite. Each \(\mathcal O_L(I)^\times\) is finite.

**Proof.** Identify \(D_\infty\) with \(\mathbb R^4\) with squared Euclidean norm \(\operatorname{nrd}\), and let \(V\) be the covolume of \(\mathcal O\). Left multiplication by \(a\) has real determinant \(\operatorname{nrd}(a)^2\); it scales lengths by \(\sqrt{\operatorname{nrd}(a)}\). The local principal description therefore gives
\[
\operatorname{covol}(I)=q_I^2V,
\qquad \operatorname{covol}(I^{-1})=q_I^{-2}V.
\tag{3.2}
\]
For an integral ideal, the first equality can also be read as
\([\mathcal O:I]=q_I^2\); fractional ideals follow by clearing denominators. The inverse equality follows from \(I^{-1}=q_I^{-1}\overline I\), since conjugation preserves volume.

Let \(v_4\) be the volume of the unit ball in this Euclidean space. Choose \(R\) with
\(R^4=17V/(v_4q_I^2)\). Minkowski's convex-body theorem, proved in the earlier lattice lesson cited in Section 7, says that a symmetric convex body of volume greater than \(2^4\) times the lattice covolume contains a nonzero lattice point. Applied to the radius-\(R\) ball in \(I^{-1}\), it supplies \(0\ne a\in I^{-1}\). Then \(aI\subset\mathcal O\), lies in the same class, and
\[
[\mathcal O:aI]
 =\operatorname{nrd}(a)^2q_I^2
 \le R^4q_I^2=\frac{17V}{v_4}.
\tag{3.3}
\]
This bound is independent of \(I\). Choose an integer \(M\) at least that bound. Any subgroup of \(\mathcal O\simeq\mathbb Z^4\) of index \(k\le M\) contains \(k\mathcal O\), and therefore contains \(M!\mathcal O\). There are only finitely many subgroups between \(M!\mathcal O\) and \(\mathcal O\), proving finiteness of the classes.

A unit of a definite order has positive integral norm, whose inverse is also integral, so its norm is one. The units of \(\mathcal O_L(I)\) lie in the compact unit sphere and in a discrete lattice, hence are finite. \(\square\)

The ideal dictionary also gives
\[
\operatorname{Cls}(\mathcal O)
 \simeq D^\times\backslash D^\times(\mathbb A_f)/\widehat{\mathcal O}^{\times},
\qquad
[g]\longmapsto[D\cap g\widehat{\mathcal O}].
\tag{3.4}
\]
Surjectivity chooses local generators; equality of classes means those generators differ by rational left multiplication and local right units. This proves the displayed equivalence using the local dictionary.

**Theorem 3.2.** For definite \(D/\mathbb Q\),
\[
X_D=D^\times\backslash D^\times(\mathbb A)/\mathbb A^\times
\tag{3.5}
\]
is compact.

**Proof.** First
\(\mathbb H^\times/\mathbb R^\times\simeq S^3/\{\pm1\}\): send \(x\) to \(x/\sqrt{\operatorname{nrd}(x)}\), and a negative scalar changes that unit quaternion only by sign. This is a continuous quotient of a compact sphere.

Choose finitely many representatives \(g_1,\ldots,g_h\) in (3.4). Every adelic element, after rational left multiplication, has finite component \(g_i u\) with \(u\in\widehat{\mathcal O}^{\times}\). Its real component is arbitrary in \(\mathbb H^\times\); after a real central scalar it is represented by a unit quaternion. Hence the finite union of compact sets
\[
\bigcup_{i=1}^h S^3\times g_i\widehat{\mathcal O}^{\times}
\tag{3.6}
\]
maps onto \(X_D\). Its image is compact. \(\square\)

### 3.1. Compactness without definiteness

The real factor need not be compact. We replace that condition by the fact that a division algebra has no nonzero element of reduced norm zero. The proof uses the written Minkowski theorem cited in Section 7 and elementary lattice bases.

**Lemma — bounded lattice bases.** Given \(n\), \(C>0\) and \(\epsilon>0\), every full lattice \(L\subset\mathbb R^n\) with covolume at most \(C\), and with \(\|v\|\ge\epsilon\) for \(v\ne0\), has a basis of bounded length, with bound depending only on these three quantities.

**Proof.** In dimension one a basis has length equal to the covolume. For the induction step choose a shortest nonzero vector \(v\), of length \(a\). Minkowski's theorem on a ball of volume greater than \(2^nC\) bounds \(a\) above; by hypothesis \(a\ge\epsilon\). The vector is primitive, since a proper integer division of it in \(L\) would be shorter. Extend it to an integral lattice basis and project orthogonally onto \(v^\perp\). The projected basis is independent, so its image \(L'\) is a full lattice of covolume
\[
\operatorname{covol}(L')=\operatorname{covol}(L)/a\le C/\epsilon.
\]
Any nonzero projected vector has a lift whose coefficient along \(v\) has absolute length at most \(a/2\), after subtracting a multiple of \(v\). Minimality of \(a\) forces its projected length to be at least \(\sqrt3\,a/2\). Thus \(L'\) satisfies the induction hypothesis with lower length \(\sqrt3\,\epsilon/2\). Lift its bounded basis, again reducing each parallel component to length at most \(a/2\). Together with \(v\) these lifts form a basis of \(L\) of bounded length. \(\square\)

**Theorem 3.3 — compactness over a number field.** If \(F\) is a number field and \(D/F\) a quaternion division algebra, then both
\[
D(F)^\times\backslash D^\times(\mathbb A_F)^1,
\qquad
D(F)^\times\backslash D^\times(\mathbb A_F)/
                 \mathbb A_F^\times
\tag{3.8}
\]
are compact. The superscript \(1\) means
\(\lvert\operatorname{nrd}(g)\rvert_{\mathbb A_F}=1\).

**Proof.** Choose a full order \(\mathcal O\) over \(\mathcal O_F\). Such an order can be constructed without a maximal-order theorem: choose a basis \(1,e_1,e_2,e_3\) of \(D\), and an integer \(N\ge1\) clearing the denominators of every multiplication coefficient. Then
\(\mathcal O_F1+\sum_{r=1}^3N\mathcal O_Fe_r\) is a full order. It is a full \(\mathbb Z\)-lattice of rank \(n=4[F:\mathbb Q]\). Fix a positive Euclidean metric on
\[
D_\infty=D\otimes_{\mathbb Q}\mathbb R
        =\prod_{v\mid\infty}D_v
\]
and let \(V\) be the covolume of \(\mathcal O\).

For \(g=(g_\infty,g_f)\) in the first adelic group, form the right \(\mathcal O\)-lattice
\[
I_g=D(F)\cap g_f\widehat{\mathcal O},\qquad
L_g=g_\infty^{-1}I_g\subset D_\infty.
\tag{3.9}
\]
The Chinese remainder proof of the Section 3 lattice dictionary applies here to the underlying rank-\(n\) integer lattice: at a rational prime \(\ell\), group together the completions at \(v\mid\ell\). Thus the completion of \(I_g\) at each finite \(v\) is exactly \(g_v\mathcal O_v\).

Left multiplication by \(a\) on a quaternion algebra has determinant \(\operatorname{nrd}(a)^2\) over its centre. This is the matrix identity after splitting the algebra, and hence is an identity before splitting. For real volume, the complex places contribute the squared complex absolute value. The local lattice-index formula and real change of variables consequently give
\[
\operatorname{covol}(L_g)
 =V\left|\operatorname{nrd}(g_f)\right|_f^{-2}
      \left|\operatorname{nrd}(g_\infty)\right|_\infty^{-2}
 =V.
\tag{3.10}
\]

There is also a uniform lower bound for the lengths of its nonzero vectors. Write such a vector as \(x=g_\infty^{-1}a\), with \(0\ne a\in I_g\). Since \(D\) is division, \(\operatorname{nrd}(a)\ne0\). At every finite \(v\), the element \(g_v^{-1}a\) belongs to the order, so its reduced norm is integral. Integrality follows because the multiplication operator on a finite integral module makes its eigenvalues integral, and the reduced norm belongs to the integrally closed ring \(\mathcal O_{F_v}\). Therefore
\[
|\operatorname{nrd}(a)|_f
 \le|\operatorname{nrd}(g_f)|_f.
\]
The product formula and the module-one condition now show
\[
|\operatorname{nrd}(x)|_\infty
 =\frac{|\operatorname{nrd}(a)|_\infty}
        {|\operatorname{nrd}(g_\infty)|_\infty}
 \ge1.
\tag{3.11}
\]
On this fixed real vector space the continuous homogeneous expression on the left has degree \(2[F:\mathbb Q]\): degree two at a real place and degree four at a complex place. Its maximum on the Euclidean unit sphere is a finite constant \(A>0\). Hence
\[
1\le A\|x\|^{2[F:\mathbb Q]}.
\]
All the lattices \(L_g\) have shortest length at least one fixed positive \(\epsilon\).

The bounded-basis lemma supplies a basis matrix \(T_g\) for each \(L_g\) with uniformly bounded entries. Its determinant has absolute value \(V\), so its inverse is uniformly bounded too, by the cofactor formula. Choose a \(\mathbb Z\)-basis \(o_1,\ldots,o_n\) of \(\mathcal O\), and write \(R(o)\) for right multiplication on \(D_\infty\). Right stability of \(L_g\) says that all the matrices
\[
T_g^{-1}R(o_r)T_g
\tag{3.12}
\]
are integral. Uniform bounds on \(T_g\) and its inverse bound their entries. There are only finitely many possible tuples (3.12).

For each tuple which occurs, choose a representative \(g_\mu\) and its basis matrix \(T_\mu\). If \(g\) has that tuple, the real linear map
\[
T_gT_\mu^{-1}
\]
commutes with every \(R(o_r)\), hence with the right action of all \(D_\infty\), since the \(o_r\) span it over \(\mathbb R\). A map commuting with that right regular action is left multiplication by its value \(b\) at \(1\): for every \(y\), its value at \(y=1y\) is \(by\). Invertibility makes \(b\in D_\infty^\times\), and the bounds on the matrices bound both \(b\) and \(b^{-1}\). The equality of lattices is
\[
L_g=bL_{g_\mu},\qquad
I_g=\gamma I_{g_\mu},
\quad
\gamma=g_\infty b g_{\mu,\infty}^{-1}.
\tag{3.13}
\]
Although \(\gamma\) was initially an archimedean element, it is rational over \(F\). Pick \(0\ne a\in I_{g_\mu}\). The division hypothesis makes \(a^{-1}\in D(F)\); equation (3.13) puts \(\gamma a\) in \(I_g\subset D(F)\). Thus \(\gamma=(\gamma a)a^{-1}\in D(F)^\times\).

Taking completions in (3.13) gives
\[
g_f=\gamma g_{\mu,f}u,\qquad
u\in\widehat{\mathcal O}^{\times}.
\]
Indeed the quotient multiplier carries \(\mathcal O_v\) onto itself; it and its inverse therefore belong to that order. The archimedean part of \(\gamma^{-1}g\) is \(g_{\mu,\infty}b^{-1}\). For each of the finitely many \(\mu\), these archimedean parts lie in a compact set: the bounds on \(b\) and \(b^{-1}\) keep them in a closed bounded subset of the invertible real algebra. Its finite parts lie in the compact set \(g_{\mu,f}\widehat{\mathcal O}^\times\). Intersecting these compact products with the closed module-one group gives a finite union of compact sets of representatives. This proves compactness of the first quotient in (3.8).

Finally the idele module over a number field takes every positive real value, by varying a positive archimedean coordinate. Given any \(g\), choose a central idele \(c\) with
\[
|c|_{\mathbb A_F}
  =|\operatorname{nrd}(g)|_{\mathbb A_F}^{-1/2}.
\]
Its reduced norm is \(c^2\), so \(cg\) has module one. The compact first quotient therefore maps onto the central quotient. Its continuous image is compact, proving the second assertion. \(\square\)

The theorem uses division over \(F\), rather than division at every completion. At a split real place the group can be noncompact; (3.11), the bounded bases and the integral right actions provide the compact representatives.

**Proposition 3.4.** With a unitary central character, the right regular Hilbert representation on this compact quotient is a discrete Hilbert sum of irreducible representations, each with finite multiplicity.

**Proof.** We explain the compact convolution input, then apply the functional argument already proved in Lesson 4, Theorem 5.2. For trivial central character put \(\overline G=G(\mathbb A)/\mathbb A^\times\) and \(\Gamma=G(\mathbb Q)/\mathbb Q^\times\). The latter is discrete: use its faithful adjoint action on the rational trace-zero space; rational matrices form a discrete subgroup of adelic matrices. For compactly supported smooth \(f\) on \(\overline G\), convolution has kernel
\[
K_f(x,y)=\sum_{\gamma\in\Gamma}f(x^{-1}\gamma y).
\tag{3.7}
\]
Choose a compact set of representatives for \(\Gamma\backslash\overline G\). Only finitely many \(\gamma\) can contribute anywhere on this set squared: they lie in its product with \(\operatorname{supp}f\) and the inverse representative set, a compact set meeting the discrete \(\Gamma\) finitely. Thus \(K_f\) is bounded on the compact finite-volume quotient and is square integrable. Its operator is Hilbert–Schmidt and compact, as proved in Lesson 4, Proposition 5.1 and Solution 7.1.

Smooth compact approximate identities converge strongly to the identity. Their positive products \(R(f)^*R(f)\) are compact. The proof of Lesson 4, Theorem 5.2, uses a smallest nonzero intersection of a positive eigenspace with invariant subspaces to find an irreducible subspace in every nonzero invariant subspace. A maximal orthogonal family exhausts the Hilbert space. Infinite multiplicity of any one irreducible would give an infinite-dimensional positive eigenspace of a compact operator, which is impossible. These arguments apply to the whole space here because its kernels are compact without deleting a constant term.

For unitary \(\omega\), the kernel is the same local periodization in the associated central-character line bundle. Changing representatives multiplies its terms by phases of absolute value one. The finite-sum bound, compactness and the positive approximate-identity argument are unchanged. This proves the assertion in every fixed unitary central character. \(\square\)

## 4. Functions on classes and Brandt matrices

Impose trivial central character, right \(\widehat{\mathcal O}^{\times}\)-invariance, and **weight zero**, meaning invariance under all of \(D_\infty^\times\). The resulting automorphic space is
\[
\mathcal M(\mathcal O)=\{f:\operatorname{Cls}(\mathcal O)\longrightarrow\mathbb C\}.
\tag{4.1}
\]
To check the centre in this identification, any finite idele can be written as a rational scalar times an element of \(\widehat{\mathbb Z}^{\times}\): choose the rational scalar with its finitely many nonzero prime valuations. These two factors are already removed in (3.4). The real centre is removed by weight zero. Thus no further ideal classes are identified. Conversely a function on classes gives such an adelic function; all real derivatives vanish, and the finite class space ensures the required finiteness conditions.

Choose right ideals \(I_1,\ldots,I_h\) representing the classes, and set
\[
q_i=q_{I_i},\qquad
w_i=\#\bigl(\mathcal O_L(I_i)^\times/\{\pm1\}\bigr),\qquad
\langle f,g\rangle=\sum_{i=1}^h\frac{f_i\overline{g_i}}{w_i}.
\tag{4.2}
\]
The \(w_i\) are finite by Lemma 3.1. These weights also agree, up to one common normalization, with quotient measure: the real compact fibre above a class is divided by its stabilizer \(\mathcal O_L(I_i)^\times/\{\pm1\}\). We can prove the required adjoint statement directly from ideal counts, independently of this measure interpretation.

For an integer \(n\ge1\), define the **row-convention Brandt matrix** by
\[
B(n)_{ij}=
\#\{J\subset I_i:J\text{ a right }\mathcal O\text{-ideal},
 q_J=nq_i,\ [J]=[I_j]\}.
\tag{4.3}
\]
It acts on column vectors of function values:
\[
(T_nf)_i=\sum_j B(n)_{ij}f_j.
\tag{4.4}
\]
Every ideal here is locally principal because the order is maximal. The count is finite: such a \(J\) has additive index \([I_i:J]=n^2\), so contains \(n^2I_i\). Voight's introductory convention, (41.1.1), counts source classes in columns; its matrix is the transpose of (4.3).

Let \(\ell\nmid d_D\). Under \(\mathcal O_\ell\simeq M_2(\mathbb Z_\ell)\), a right ideal consists of matrices whose columns belong to a fixed lattice \(L\subset\mathbb Q_\ell^2\). The lattice determines the ideal: multiplying by matrix units isolates either column, and moves it to the other position. Norm ratio \(\ell\) means \([\mathbb Z_\ell^2:L]=\ell\). Such lattices contain \(\ell\mathbb Z_\ell^2\), and correspond to lines in \(\mathbb F_\ell^2\). There are \(\ell+1\). At all other places keep the given ideal, and intersect the local lattices to recover the global one. Thus
\[
\sum_j B(\ell)_{ij}=\ell+1=\sigma_1(\ell).
\tag{4.5}
\]
More generally the number of index-\(\ell^r\) sublattices of \(\mathbb Z_\ell^2\) is \(1+\ell+\cdots+\ell^r\). An upper-triangular lattice basis has diagonal \(\ell^a,\ell^b\), \(a+b=r\), and \(\ell^a\) choices for its other entry modulo \(\ell^a\). Summing over \(a\) proves the count. At a division prime there is one ideal for each valuation, namely the corresponding power of the maximal ideal. These statements specify the row degrees of all \(B(n)\) by multiplying the local counts.

We count all ideals of norm ratio \(\ell^r\), including those divisible by the scalar \(\ell\). A primitive-distance operator on the lattice tree has a different degree at \(r=2\). In particular \(B(\ell^2)\) has row sum \(1+\ell+\ell^2\), whereas a distance-two operator has row sum \(\ell(\ell+1)\).

**Theorem 4.1 — Brandt operators.** All \(B(n)\) commute. They are self-adjoint for (4.2), equivalently
\[
\frac{B(n)_{ij}}{w_i}=\frac{B(n)_{ji}}{w_j}.
\tag{4.6}
\]
They admit a common orthogonal eigenbasis with real eigenvalues.

**Proof of self-adjointness.** An ideal counted in (4.3) has the form \(aI_j\). The allowed multipliers are precisely
\[
S_{ij}(n)=\{a\in I_iI_j^{-1}:\operatorname{nrd}(a)=nq_i/q_j\}.
\tag{4.7}
\]
Two multipliers give the same ideal exactly when they differ on the right by a unit of \(\mathcal O_L(I_j)\). That unit group has order \(2w_j\), and acts freely. Hence
\[
\#S_{ij}(n)=2w_jB(n)_{ij}.
\tag{4.8}
\]
These sets are finite, since a positive norm sphere meets a lattice finitely.

Conjugating the product lattice and using \(\overline I=q_I I^{-1}\) gives
\[
\overline{I_iI_j^{-1}}=(q_i/q_j)I_jI_i^{-1}.
\tag{4.9}
\]
For \(a\in S_{ij}(n)\), put
\[
a'=na^{-1}=(q_j/q_i)\overline a.
\tag{4.10}
\]
Equation (4.9) places \(a'\) in \(I_jI_i^{-1}\), and multiplicativity gives
\(\operatorname{nrd}(a')=nq_j/q_i\). Applying the same construction again returns \(a\). Thus (4.10) is a bijection \(S_{ij}(n)\simeq S_{ji}(n)\). Formula (4.8) yields
\(w_j B(n)_{ij}=w_i B(n)_{ji}\), which is exactly (4.6). Inserting this equality into the two finite sums defining \(\langle T_nf,g\rangle\) and \(\langle f,T_ng\rangle\) proves self-adjointness. \(\square\)

**Proof of commutativity.** We prove commutativity of the local algebras that produce (4.3), including prime powers.

At a split place put \(K=\mathrm{GL}_2(\mathbb Z_\ell)\), and normalize Haar measure by \(\operatorname{vol}K=1\). Every double coset in \(\mathrm{GL}_2(\mathbb Q_\ell)\) has a representative
\(\operatorname{diag}(\ell^a,\ell^b)\), by the elementary-divisor theorem for lattices, allowing negative integers after clearing denominators. Transposition fixes this representative and preserves \(K\), so it fixes every double coset as a set. Every compactly supported bi-\(K\)-invariant function \(h\) therefore satisfies \(h^t(x):=h(x^t)=h(x)\).

Transposition preserves Haar measure. Explicitly an invariant measure on invertible matrices is a constant times
\(dX/|\det X|_\ell^2\); left or right multiplication by \(A\) changes the additive four-coordinate measure by \(|\det A|_\ell^2\), and changes the denominator by the same factor. Transposition changes neither. Its reversal of multiplication then gives
\[
(h_1*h_2)^t=h_2^t*h_1^t.
\tag{4.11}
\]
For completeness, transpose the convolution integral and substitute \(z=y^t\). Its integrand becomes \(h_1^t(z)h_2^t(xz^{-1})\). Substitute \(u=xz^{-1}\); inversion and translations preserve Haar measure in this unimodular group. The integral is \(\int h_2^t(u)h_1^t(u^{-1}x)\,du\), proving (4.11). The convolution is again bi-\(K\)-invariant, hence fixed by transposition. Thus \(h_1*h_2=h_2*h_1\).

At a division place \(\mathcal O_D^\times\) is normal in \(D^\times\): conjugation preserves \(v_D\). The quotient is \(\mathbb Z\), by that valuation. Its bi-unit Hecke algebra is the convolution algebra of finitely supported functions on \(\mathbb Z\), which is commutative. Different places commute because their group coordinates and product convolutions are independent.

Finally, at a good prime the operator for norm ratio \(\ell^r\) is the characteristic function of
\[
\{x\in M_2(\mathbb Z_\ell):v_\ell(\det x)=r\},
\tag{4.12}
\]
restricted to invertible matrices. This compact bi-\(K\) set is the finite union of double cosets with nonnegative elementary-divisor exponents summing to \(r\). At a division prime use \(j^r\mathcal O_D^\times\). Take their product over primes dividing \(n\), with unit characteristic functions elsewhere. Right convolution on (4.1) sums over its right-unit cosets, each of measure one. Those cosets are exactly the local subideals of norm ratio \(n\); the local-global lattice dictionary identifies them with the ideals in (4.3). Thus this convolution is \(T_n\). The preceding local commutativity proves \(T_mT_n=T_nT_m\) for all \(m,n\). When \(m,n\) are coprime the same description also gives \(T_mT_n=T_{mn}\).

For the final assertion, diagonalize any one self-adjoint operator. All commuting operators preserve its orthogonal eigenspaces. If an eigenspace has a nonscalar restriction of another operator, diagonalize that restriction and refine the orthogonal decomposition. Each refinement increases the number of nonzero summands, which is bounded by \(h\). Eventually every operator is scalar on every summand; an orthonormal basis in those summands is a common eigenbasis. Self-adjointness makes every eigenvalue real. \(\square\)

The normalization is the unscaled integral Hecke operator. At a split prime its unitary Satake eigenvalue is \(\ell^{1/2}(\alpha_\ell+\beta_\ell)\), as in Lesson 13. The constant function has eigenvalue \(\ell+1\). These conventions also give the usual weight-two classical coefficients in the later correspondence.

### 4.1. Count the classes with their stabilizers

The weights in (4.2) are necessary even when the question is only the number of classes. We first compute their sum and then count the units which make the ordinary class number differ from that sum. Throughout this subsection, \(D/\mathbb Q\) is definite, \(\mathcal O\) is maximal, and \(d=d_D\).

**Lemma 4.2 — the lattice volume.** For the Euclidean metric \(\|x\|^2=\operatorname{nrd}(x)\) on \(D_\infty\simeq\mathbb H\),
\[
\operatorname{covol}(\mathcal O)=d/4.
\tag{4.13}
\]

**Proof.** The integral pairing is \(T(x,y)=\operatorname{trd}(xy)\). We compute its discriminant locally. A maximal order in the split algebra over \(\mathbb Q_\ell\) is an endomorphism ring of a lattice: if \(R\) is any order, the lattice \(R\mathbb Z_\ell^2\) is full and \(R\)-stable, so
\[
R\subset\operatorname{End}_{\mathbb Z_\ell}(R\mathbb Z_\ell^2);
\]
maximality gives equality. Choosing a lattice basis identifies it with \(M_2(\mathbb Z_\ell)\). The four matrix units give a trace-pairing determinant of absolute \(\ell\)-adic value one.

At a division place use (1.2). Every order lies in \(\mathcal O_D\): a member of negative valuation would have powers of unbounded size, whereas all its powers belong to the compact order. Thus the maximal order is \(\mathcal O_D\). Choose an integral basis \(e_1,e_2\) of the unramified quadratic ring \(\mathcal O_L\). Its trace pairing is perfect: modulo \(\ell\) it is the nondegenerate trace pairing of a finite separable field extension. In the basis \(e_1,e_2,e_1j,e_2j\), the quaternion trace pairing has zero off-diagonal blocks. The first block is the quadratic trace pairing; the second is
\[
\ell\bigl(\operatorname{Tr}_{L/\mathbb Q_\ell}(e_r\overline e_s)\bigr)_{r,s}.
\]
Conjugation preserves the integral lattice, so the matrix in parentheses has unit determinant. The four-dimensional determinant therefore has valuation two, including at \(\ell=2\).

A globally maximal order is maximal at each finite place. Otherwise enlarging at that place and keeping the other local lattices unchanged, by the lattice dictionary of Section 3, gives a strictly larger global order. The pairing is integral: multiplication by an element of an order preserves an integral lattice, so its eigenvalues are algebraic integers. Its reduced trace is the rational sum of its two distinct eigenvalues, or twice the single eigenvalue in the scalar case, and is consequently an integer. Apply this to each product \(xy\). The local calculations give \(|\det T|=d^2\).

Finally \(\operatorname{trd}(x\overline y)=2\langle x,y\rangle\) in the real norm metric. Conjugation has real determinant \(-1\), so it does not change the absolute determinant of the trace pairing. If \(V=\operatorname{covol}(\mathcal O)\), its Gram determinant is \(2^4V^2\). Thus \(16V^2=d^2\), giving (4.13). This also proves the maximality test used below. An order contained in a maximal order has trace discriminant equal to that of the maximal order times the square of its lattice index. Hence reduced discriminant \(d\) forces index one. A maximal overorder exists because the positive integral discriminant prevents an infinite chain of strict overorders. \(\square\)

**Theorem 4.3 — the mass.** The stabilizer weights satisfy
\[
\sum_{[I]\in\operatorname{Cls}(\mathcal O)}\frac1{w_I}
=\frac1{12}\prod_{\ell\mid d}(\ell-1).
\tag{4.14}
\]

**Proof.** Count integral right ideals by their additive index:
\[
Z_{\mathcal O}(s)
=\sum_{J\subset\mathcal O}[\mathcal O:J]^{-s}
=\sum_{n\ge1}a_n n^{-2s},\qquad \operatorname{Re}s>1.
\tag{4.15}
\]
The local counts proved after (4.5) give \(a_{\ell^r}=1+\ell+\cdots+\ell^r\) at split primes and \(a_{\ell^r}=1\) at division primes. Specifying independent local ideals and intersecting their lattices proves \(a_{mn}=a_ma_n\) for coprime \(m,n\). Consequently
\[
Z_{\mathcal O}(s)
=\zeta(2s)\zeta(2s-1)
  \prod_{\ell\mid d}(1-\ell^{1-2s}).
\tag{4.16}
\]
For the split local factor, expand \((1-T)^{-1}(1-\ell T)^{-1}\), whose coefficient of \(T^r\) is the required sum, and take \(T=\ell^{-2s}\). At a division place only \((1-T)^{-1}\) remains. These products converge absolutely on the asserted half-plane.

We need two scalar constants, which can be checked directly. Integration of the counting function of the positive integers gives
\[
\zeta(u)=\frac{u}{u-1}
 -u\int_1^\infty\{x\}x^{-u-1}\,dx.
\]
The integral is holomorphic for \(\operatorname{Re}u>0\), so the residue at \(u=1\) is one. Also two integrations by parts give the cosine coefficients in
\[
x^2=\frac{\pi^2}{3}
 +4\sum_{n\ge1}\frac{(-1)^n\cos(nx)}{n^2}
 \qquad(-\pi\le x\le\pi).
\]
The series converges uniformly and has exactly those coefficients. Its difference from \(x^2\) is a continuous periodic function with every Fourier coefficient zero. Convolution with the Fejér kernels makes that difference zero: these are nonnegative trigonometric polynomials of integral one whose mass outside every neighborhood of zero tends to zero, since
\[
\frac1N\left|\sum_{r=0}^{N-1}e^{irx}\right|^2
 \le\frac1{N\sin^2(x/2)}.
\]
Uniform continuity makes their convolutions converge uniformly to the difference. This proves the equality. Evaluating at \(x=\pi\) gives \(\zeta(2)=\pi^2/6\). Equation (4.16) therefore has residue
\[
\operatorname*{Res}_{s=1}Z_{\mathcal O}(s)
=\frac{\pi^2}{12}\prod_{\ell\mid d}(1-\ell^{-1}).
\tag{4.17}
\]

Compute the same residue class by class. Fix \(I\), with \(q=q_I\) and \(w=w_I\). Ideals in its class contained in \(\mathcal O\) are \(aI\), for nonzero \(a\in I^{-1}\), modulo right multiplication of \(a\) by \(\mathcal O_L(I)^\times\). This action is free and has \(2w\) elements. The part belonging to this class is
\[
Z_{[I]}(s)=\frac{q^{-2s}}{2w}
  \sum_{0\ne a\in I^{-1}}\|a\|^{-4s}.
\tag{4.18}
\]
Indeed \(\operatorname{nrd}(aI)=\operatorname{nrd}(a)q\), so the exponents agree with the additive index.

For a full lattice \(L\subset\mathbb R^4\) of covolume \(c\), let \(N_L(R)\) count its nonzero points of length at most \(R\). A bounded fundamental parallelepiped has some diameter \(b\). Tiles based at points inside the radius-\(R\) ball lie inside the radius-\(R+b\) ball. Conversely, tiles meeting the radius-\(R-b\) ball are based inside the radius-\(R\) ball. Comparing volumes, and omitting the zero point, proves
\[
N_L(R)=\frac{v_4}{c}R^4+O_L(R^3+1),
\qquad v_4=\pi^2/2.
\tag{4.19}
\]
The value of \(v_4\) follows by integrating two polar-coordinate planes. Summation by parts writes the lattice series, up to the entire finite correction for lengths below one, as
\[
4s\int_1^\infty N_L(R)R^{-4s-1}\,dR.
\]
Its main term is \((v_4/c)s/(s-1)\); the error integral is holomorphic for \(\operatorname{Re}s>3/4\). This proves continuation near one and residue \(v_4/c\).

Apply it to \(L=I^{-1}\), whose covolume is \(q^{-2}d/4\) by (3.2) and Lemma 4.2. Equation (4.18) has residue \(\pi^2/(wd)\). There are finitely many classes by Lemma 3.1, so their residues add. Equate that sum with (4.17) and cancel \(\pi^2/d\). The result is (4.14). \(\square\)

**Theorem 4.4 — the ordinary class number at prime discriminant.** For \(D=B_{p,\infty}\), \(p>3\),
\[
h_p=\frac{p-1}{12}
 +\frac14\left(1-\left(\frac{-4}{p}\right)\right)
 +\frac13\left(1-\left(\frac{-3}{p}\right)\right).
\tag{4.20}
\]

**Proof.** Put \(R_i=\mathcal O_L(I_i)\). A unit has norm one, and its integral trace lies between \(-2\) and \(2\). Trace \(2\) or \(-2\) forces the quaternion to be \(1\) or \(-1\). Let \(r_i\) count roots of \(X^2+1\) in \(R_i\), and let \(t_i\) count roots of \(X^2-X+1\). Trace zero gives the first roots; trace one gives the second; negating gives a bijection from trace one to trace minus one. These cases account for every unit, so
\[
2w_i=2+r_i+2t_i,\qquad
h_p-\sum_i\frac1{w_i}
=\sum_i\frac{r_i}{2w_i}+\sum_i\frac{t_i}{w_i}.
\tag{4.21}
\]
We count the right side by embeddings, without assuming a classification of finite quaternion unit groups.

Take first \(E=\mathbb Q(i)\), then \(E=\mathbb Q(\sqrt{-3})\), with its full ring \(\mathcal O_E\). Their unit groups have orders four and six; write \(w_E=2\) and \(3\). Both rings have class number one. In the Gaussian lattice, coordinate rounding leaves squared distance at most \(1/2\). In the basis \(1,e^{i\pi/3}\) of the second lattice, rounding both coefficients leaves squared distance at most \(3/4\). Division with remainder of smaller norm follows in both rings. Choosing a nonzero element of least norm in an ideal proves that ideal principal, by the descent of Proposition 5.1.

If \(p\) splits in \(E\), there is no embedding \(E\hookrightarrow D\): its completion would embed \(\mathbb Q_p\times\mathbb Q_p\) in a division algebra, which has no nontrivial idempotent. If \(p\) is inert, an embedding exists explicitly. In the Gaussian case \((-1,-p)_{\mathbb Q}\) has ramification precisely \(\{p,\infty\}\), and contains \(i\). In the second case use \((-3,-p)_{\mathbb Q}\). The Hilbert-symbol rules used in Section 5 check this. At \(p\) the first parameter is a nonsquare. At other odd primes not dividing that parameter both parameters are units. The odd-unit symbol at \(2\) is positive in both cases: for the first case use \(p\equiv3\pmod4\); for the second, \((-3-1)/2\) is even. At \(3\) in the second case the remaining symbol is \((-p/3)=1\), since \(p\equiv2\pmod3\). Both real symbols are negative. Global classification from Section 2 identifies these algebras with \(B_{p,\infty}\). The Legendre symbols in (4.20) are nonzero because \(p>3\), so split and inert exhaust the possibilities.

Suppose \(p\) is inert, and fix such an embedded \(E\). Let \(e_i(E)\) be the number of embeddings \(\mathcal O_E\hookrightarrow R_i\) modulo conjugation by \(R_i^\times\). Each embedding extends to the fraction field; Skolem–Noether identifies it with the fixed embedding after rational conjugation. The pairs consisting of an ideal class and an embedding consequently identify with lattices \(I\) satisfying \(\mathcal O_EI\subset I\), modulo left multiplication by \(E^\times\). The dictionary (3.4) parametrizes them by
\[
E^\times\backslash X/\widehat{\mathcal O}^{\times},
\qquad
X=\{x\in D^\times(\mathbb A_f):
 x^{-1}\widehat{\mathcal O}_E x\subset\widehat{\mathcal O}\}.
\tag{4.22}
\]
Indeed \(I=D\cap x\widehat{\mathcal O}\) is left \(\mathcal O_E\)-stable exactly when the local inclusions hold. Changing its right local generators changes \(x\) by \(\widehat{\mathcal O}^\times\). After changing the embedding to the fixed one, precisely its centralizer \(E^\times\) remains as the allowed rational change. Thus the equivalence relation in (4.22) also agrees with that of the pairs.

At \(\ell\ne p\), identify \(D_\ell\) with \(M_2(\mathbb Q_\ell)\). Its column space is the rank-one \(E_\ell\)-module \(E_\ell\); when \(E_\ell\) is split, this means its two eigenspaces. The condition in \(X\) says that the column lattice \(x_\ell\mathbb Z_\ell^2\) is an \(\mathcal O_{E,\ell}\)-module. In the field case it is a fractional ideal of a discrete valuation ring, hence principal. In the split case the two idempotents decompose it as two fractional \(\mathbb Z_\ell\)-ideals, again principal as a module over the product ring. Consequently there is one local double coset under \(E_\ell^\times\) on the left and \(\mathcal O_\ell^\times\) on the right. This includes the primes ramified in \(E\).

At \(p\), the maximal division order is invariant under conjugation and meets \(E_p\) in \(\mathcal O_{E,p}\); hence \(X_p=D_p^\times\). The valuation \(v_D\) identifies \(D_p^\times/\mathcal O_{D,p}^\times\) with \(\mathbb Z\). The unramified quadratic group \(E_p^\times\) has even valuations, so there are exactly two local double cosets. For each of these orientations, and the unique cosets elsewhere, choose a representative \(x\). The remaining global quotient is
\[
E^\times\backslash\mathbb A_{E,f}^\times/
\widehat{\mathcal O}_E^\times.
\]
For its denominator, the ring
\[
E_\ell\cap x_\ell\mathcal O_\ell x_\ell^{-1}
\]
contains \(\mathcal O_{E,\ell}\) by the definition of \(X\). Every one of its members is integral, so this is exactly the maximal ring \(\mathcal O_{E,\ell}\); its units are the stabilizer. The quotient is therefore the ideal class group of \(E\), which is trivial as proved above. All local representatives can be chosen integral at almost all places, so they form restricted adeles. The lattice dictionary gives actual global ideals for them. We have proved
\[
\sum_i e_i(E)=2
\quad\text{if \(p\) is inert, and }0\text{ if \(p\) splits.}
\tag{4.23}
\]

The centralizer of an embedded \(E\) in \(D\) is \(E\) by the double-centralizer theorem. Its intersection with \(R_i\) is \(\mathcal O_E\), since elements of \(R_i\) are integral. An embedding's stabilizer under \(R_i^\times\) thus has \(2w_E\) elements, and its orbit has \(w_i/w_E\) elements. An embedding is determined by the image of \(i\), or of the trace-one sixth root of unity. It follows that
\[
r_i=\frac{w_i}{2}e_i(\mathbb Q(i)),\qquad
t_i=\frac{w_i}{3}e_i(\mathbb Q(\sqrt{-3})).
\tag{4.24}
\]
Insert (4.23)–(4.24) into (4.21), and use the mass (4.14). The correction terms are exactly those in (4.20), with every stabilizer factor accounted for. \(\square\)

These are Eichler's mass and class-number formulas. Voight's Theorems 25.3.15 and 30.1.5 give the reference conventions. The local counts, lattice residue and embedding-orbit arguments above supply the proofs used here; the following examples therefore require no external class-counting theorem.

## 5. Two computed definite examples

### 5.1. The Hurwitz order

For \(D=(-1,-1)_{\mathbb Q}\), the real norm is the sum of four squares. Its ramification set is \(\{2,\infty\}\): at odd primes both parameters are units and the Hilbert symbol is \(+1\); at \(2\) it is \((-1)^{((-1-1)/2)^2}=-1\), and at infinity both parameters are negative. These Hilbert-symbol rules are Voight, Section 14.2. Thus this is \(B_{2,\infty}\).

Its Hurwitz order is
\[
\mathcal O_H=\mathbb Z^4\ \cup\ (\mathbb Z+\tfrac12)^4
\tag{5.1}
\]
in coordinates \(1,i,j,k\). To verify it is an order, write it as the Lipschitz order plus \(\mathbb Z h\), where \(h=(1+i+j+k)/2\). Left and right multiplication of \(h\) by \(i,j,k\) gives elements with four half-integral coordinates, and \(h^2=h-1\). Thus products remain in this lattice. The trace Gram matrix of the Lipschitz order is \(\operatorname{diag}(2,-2,-2,-2)\), with absolute determinant \(16\). Enlarging by index two divides the determinant by four, so the Hurwitz reduced discriminant is \(2\). The maximal-order discriminant criterion in Lemma 4.2 proves maximality.

**Proposition 5.1.** The Hurwitz order has class number one and \(24\) units. Its weight-zero class space is one-dimensional, and \(B(\ell)=[\ell+1]\) for every odd prime \(\ell\).

**Proof.** Round the four coordinates of any \(x\in\mathbb H\) to integers. The squared distance to that point is at most \(4(1/2)^2=1\). Equality requires every coordinate to be a half-integer; then \(x\) itself belongs to \(\mathcal O_H\) and has distance zero from the order. Hence in every case there is \(q\in\mathcal O_H\) with \(\operatorname{nrd}(x-q)<1\).

Let \(I\subset\mathcal O_H\) be a nonzero right ideal and choose \(a\in I\setminus\{0\}\) of minimum positive norm. For \(b\in I\), approximate \(a^{-1}b\) by such a \(q\). Then
\[
r=b-aq\in I,
\qquad \operatorname{nrd}(r)
 =\operatorname{nrd}(a)\operatorname{nrd}(a^{-1}b-q)
 <\operatorname{nrd}(a).
\tag{5.2}
\]
Minimality forces \(r=0\). Thus \(I=a\mathcal O_H\), and clearing a scalar denominator gives the same conclusion for fractional ideals. There is one class.

Norm-one integral coordinates give \(\pm1,\pm i,\pm j,\pm k\), eight units. Norm-one half-integral coordinates must each be \(\pm1/2\), giving sixteen further units. Conversely all these elements have integral conjugates and norm one, hence are units. So \(w=24/2=12\). With one class, the degree calculation (4.5) gives the asserted scalar Brandt matrix. At the ramified prime \(2\) the corresponding matrix is instead \([1]\), since its local ideal is unique. \(\square\)

### 5.2. An order in \(B_{11,\infty}\)

Take
\[
D=(-1,-11)_{\mathbb Q},\qquad i^2=-1,\quad j^2=-11,\quad k=ij,
\qquad u=\frac{1+j}{2},\quad v=\frac{i+k}{2}.
\tag{5.3}
\]
At odd primes other than \(11\) the parameters are units, so the Hilbert symbol is \(+1\). At \(11\) it is \(({-1}/11)=-1\). At \(2\) the odd-unit formula gives \((-1)^{(-1)(-6)}=+1\), and at infinity it is \(-1\). The algebra is therefore \(B_{11,\infty}\).

Let \(\mathcal O_1=\mathbb Z+\mathbb Zi+\mathbb Zu+\mathbb Zv\). The identities
\[
i^2=-1,\qquad u^2=u-3,\qquad iu=v,\qquad ui=i-v
\tag{5.4}
\]
reduce products to this lattice. In particular \(iv=-u\), \(vi=u-1\), \(uv=3i\), \(vu=v-3i\), and \(v^2=-3\), so it is an order. The trace pairing in this basis is
\[
\bigl(\operatorname{trd}(e_re_s)\bigr)_{r,s}
 =\begin{pmatrix}
2&0&1&0\\
0&-2&0&-1\\
1&0&-5&0\\
0&-1&0&-6
\end{pmatrix}.
\tag{5.5}
\]
Its determinant is \(-121\); the reduced discriminant is \(11\), equal to the algebra's discriminant. Lemma 4.2 therefore proves this order maximal.

Theorems 4.3–4.4 count its classes and stabilizers. For a maximal order in \(B_{p,\infty}\), \(p>3\), Eichler's formula is
\[
h_p=\frac{p-1}{12}
 +\frac14\left(1-\left(\frac{-4}{p}\right)\right)
 +\frac13\left(1-\left(\frac{-3}{p}\right)\right).
\tag{5.6}
\]
This is Theorem 4.4. Its mass formula, Theorem 4.3, is
\[
\sum_{[I]}\frac1{w_I}=\frac{p-1}{12},
\tag{5.7}
\]
The formulas were proved above; we now compute the substitution, weights and matrix entries.

The nonzero squares modulo \(11\) are \(1,3,4,5,9\). Both \(-4\equiv7\) and \(-3\equiv8\) are nonsquares. Hence
\[
h_{11}=\frac56+\frac12+\frac23=2,
\qquad \frac1{w_1}+\frac1{w_2}=\frac56.
\tag{5.8}
\]
For \(a,b,c,d\in\mathbb Z\), direct evaluation of the norm gives
\[
\operatorname{nrd}(a+bi+cu+dv)
 =(a+c/2)^2+(b+d/2)^2+\frac{11}{4}(c^2+d^2).
\tag{5.9}
\]
If this equals one or two, then \(c=d=0\), since otherwise its last term alone exceeds two. Norm one therefore gives \(\pm1,\pm i\), so \(w_1=2\). Norm two gives exactly \(\pm1\pm i\), four elements. The other class has \(1/w_2=5/6-1/2=1/3\), so \(w_2=3\).

Label \(I_1=\mathcal O_1\). Formula (4.8) gives \(B(2)_{11}=4/(2w_1)=1\). Each row has sum three. Thus \(B(2)_{12}=2\). Detailed balance (4.6) now forces \(B(2)_{21}/3=2/2=1\), hence \(B(2)_{21}=3\) and \(B(2)_{22}=0\). We have obtained
\[
B(2)=\begin{pmatrix}1&2\\3&0\end{pmatrix},
\qquad
\det(tI-B(2))=t^2-t-6=(t-3)(t+2).
\tag{5.10}
\]
The eigenvectors are \((1,1)^t\) for \(3\), and \((2,-3)^t\) for \(-2\). The second has weighted mean zero:
\(2/2-3/3=0\). Its squared norm is \(4/2+9/3=5\), while the constant vector has squared norm \(1/2+1/3=5/6\). Thus the eigenlines are orthogonal for exactly our weights. In ordinary Euclidean coordinates the matrix is not symmetric; in weighted coordinates,
\[
\operatorname{diag}(1/2,1/3)B(2)
 =\begin{pmatrix}1/2&1\\1&0\end{pmatrix}
\tag{5.11}
\]
is symmetric, checking the convention.

### 5.3. Comparison with the classical coefficient

The normalized level-eleven form is
\[
f_{11}(z)=\eta(z)^2\eta(11z)^2
 =q\prod_{m\ge1}(1-q^m)^2(1-q^{11m})^2,
\qquad q=e^{2\pi iz}.
\tag{5.12}
\]
Its modularity, vanishing at both cusps, and \(\dim S_2(\Gamma_0(11))=1\) were proved in LG-MF-09, Section 6. We import those exact assertions. The oldspace is zero: the only proper divisor is one, and \(S_2(\mathrm{SL}_2(\mathbb Z))=0\) by LG-MF-06, Theorem 4.1 and Section 4.1. The old/new definition is LG-MF-10, Section 1. Therefore this is a newform.

Here its first coefficients can be calculated without invoking the correspondence. Modulo \(q^4\), the factors beyond \(m=3\) do not matter before the initial \(q\), and the \(11m\)-factors are one. The finite multiplication is
\[
\begin{aligned}
(1-q)^2(1-q^2)^2
 &=1-2q-q^2+4q^3+O(q^4),\\
(1-q)^2(1-q^2)^2(1-q^3)^2
 &=1-2q-q^2+2q^3+O(q^4).
\end{aligned}
\tag{5.13}
\]
Thus \(f_{11}=q-2q^2-q^3+2q^4+O(q^5)\), and \(a_2=-2\). This agrees with (5.10). Theorem 4.1 proves a simultaneous eigenline in the weighted-mean-zero class space, since its dimension is one. Identifying all of its good-prime eigenvalues with those of \(f_{11}\) is the Jacquet–Langlands correspondence, to be stated precisely in Lesson 19. The matrix was determined here by quaternionic counts and arithmetic formulas, without using that identification.

## 6. Exercises and complete solutions

**Exercise 6.1 — easy.** Prove \(\mathbb H^\times/\mathbb R^\times\) compact. Describe the residual sign when using norm-one representatives.

**Solution 6.1.** The norm of \(x\ne0\) is a positive real number, so write
\(x=r u\), \(r=\sqrt{\operatorname{nrd}(x)}>0\), \(\operatorname{nrd}(u)=1\). The unit quaternions form the sphere \(S^3\), a compact subset of \(\mathbb R^4\). Positive scalars change \(r\) but leave \(u\) unchanged; negative scalars change \(u\) to \(-u\). Thus the continuous map \(S^3\to\mathbb H^\times/\mathbb R^\times\) is onto with fibres \(\{u,-u\}\). The quotient is \(S^3/\{\pm1\}\), and is compact as the continuous image of \(S^3\). Equivalently it is \(\mathrm{SO}(3)\), but that identification is not needed for the proof.

**Exercise 6.2 — medium.** Compute the class number for a maximal order of \(B_{11,\infty}\) and its \(T_2\) Brandt matrix. State the class ordering, inner product and eigenvectors.

**Solution 6.2.** Work with the order \(\mathcal O_1\) in (5.3)–(5.4). Its multiplication table is integral and its trace determinant is \(-11^2\), so Lemma 4.2 makes it maximal. Modulo \(11\), the nonzero squares \(1,3,4,5,9\) exclude \(-4\) and \(-3\). Substitution into Theorem 4.4 gives
\[
h=10/12+(1/4)(1-(-1))+(1/3)(1-(-1))=2.
\tag{6.1}
\]
Take the first ideal class to be \([\mathcal O_1]\), and the second to be the other class; no additional choice of a representative affects the following count. In (5.9), norm at most two forces \(c=d=0\). Norm one gives four units, so \(w_1=2\). The mass formula gives \(1/w_2=10/12-1/2=1/3\), hence \(w_2=3\). Norm two gives four elements. Their right-unit orbits each have four elements, so there is one norm-two subideal in the first class: \(B_{11}=1\). As \(2\) is split, there are three norm-two subideals in total, so \(B_{12}=2\). Balance is \(B_{12}/w_1=B_{21}/w_2\), forcing \(B_{21}=3\). Its row degree then gives \(B_{22}=0\).

Thus the row-sum matrix on column functions is \(\left(\begin{smallmatrix}1&2\\3&0\end{smallmatrix}\right)\). Direct multiplication gives
\[
B(2)\binom{1}{1}=3\binom{1}{1},
\qquad B(2)\binom{2}{-3}=-2\binom{2}{-3}.
\tag{6.2}
\]
The product is \(f_1\overline g_1/2+f_2\overline g_2/3\). The two vectors are orthogonal because \(2/2-3/3=0\). The eigenvalue \(-2\) agrees with the independently multiplied coefficient of (5.12). Transposing the matrix without changing the vector convention or the weights would lose this calculation.

**Exercise 6.3 — medium.** Establish the finite-image assertion for an irreducible smooth complex representation of a local quaternion division group, keeping track of the centre. Decide when it literally descends to the central quotient.

**Solution 6.3.** Theorem 1.1 proves finite dimension without assuming a central character first. For a finite basis, intersect the open stabilizers of all its vectors; the intersection acts identically. The kernel \(U\) is therefore open and normal. By finite-dimensional Schur, \(F^\times\) acts through a character \(\chi\), so the projective action has kernel containing \(F^\times U\). Its quotient is discrete and is a quotient of the compact \(D^\times/F^\times\); it is finite. This proves finite projective image modulo the centre.

For an actual finite image, write the action of the scalar uniformizer as \(c\operatorname{id}\), choose \(b^2=c^{-1}\), and twist by \(b^{v_F(\operatorname{nrd}(x))}\). The scalar uniformizer now acts as \(b^2c=1\). If \(U'\) is the open kernel of the twist, then (1.3) makes \(D^\times/(\varpi^{\mathbb Z}U')\) compact and discrete, hence finite. The twisted representation factors through that finite group.

The original representation descends to \(D^\times/F^\times\) exactly when \(\chi=1\). Even a one-dimensional \(|\operatorname{nrd}|_F\) has nontrivial central action \(|a|_F^2\), so literal descent for arbitrary central character would be false. For trivial central character the preceding projective quotient is already an actual finite representation quotient. This is the required qualification of “a finite quotient modulo the centre.”

**Exercise 6.4 — hard.** Prove commutativity of all Brandt matrices, including operators at prime powers. Explain why coprime-prime commutation alone is insufficient.

**Solution 6.4.** At a good place, use right-unit cosets of integral invertible matrices of determinant valuation \(r\). They parameterize all sublattices of index \(\ell^r\), and hence the corresponding local subideals. Elementary divisors show every bi-\(K\) double coset has a diagonal representative fixed by transpose. Thus all bi-\(K\) functions equal their transposes. For Haar measure \(dX/|\det X|^2\), transpose preserves measure and reverses multiplication. The convolution substitution in (4.11) therefore gives
\[
h_1*h_2=(h_1*h_2)^t=h_2^t*h_1^t=h_2*h_1.
\tag{6.3}
\]
This applies to every determinant-valuation union, not only the prime operator. At a ramified place, the unit group is normal, the valuation quotient is \(\mathbb Z\), and convolution is the commutative convolution on that abelian group. Different places commute in the product group. The local-global lattice intersection and the norm formula identify the product convolution with the count (4.3); the right cosets all have volume one. Therefore every pair \(B(m),B(n)\) commutes.

A proof only for distinct primes would not address two different powers of the same prime. The local algebra argument does. It also avoids replacing our full norm operator by a primitive sphere: at a good prime, the scalar sublattice \(\ell\mathbb Z_\ell^2\) contributes to norm \(\ell^2\), but represents distance zero after homothety. Its contribution explains why the full norm degree is \(1+\ell+\ell^2\). The row sums of products and all prime powers are consistent with the same local convolution convention.

## 7. Proof providers and source locators

The local and global quaternion classifications in Sections 1–2 are deduced from the written Brauer groups of local and global fields, Proposition 24.1 and Theorems 24.2 and 24.4. The invariant uses arithmetic Frobenius, is \(1/2\) for quaternion division, is zero at complex places, and multiplies by the local extension degree under restriction. The global existence proof above constructs a quadratic splitting field before applying the finite splitting criterion; it covers characteristic two. The explicit valuation and maximal local ring in (1.2) are checked here. Original locators are Voight, Theorem 13.3.11, Main Theorems 14.1.3 and 14.6.1. The Hilbert-symbol rules used in Sections 4.1 and 5 have the local-field and class-field providers; their reference formulas are Voight (12.4.10) and (12.4.14), criteria 12.4.12, and Proposition 14.2.1. Quaternion conjugation, reduced norm, Skolem–Noether, the double-centralizer theorem and the finite splitting criterion are Central simple algebras and the Brauer group, Theorems 2.1, 3.1 and 4.2 and Sections 6–7.

The local-to-global lattice dictionary is proved in Section 3 by the finite Chinese remainder theorem. Local principality is proved there by matrix units and the division valuation; (3.2), (3.4) and the convolution interpretation use these arguments. Minkowski's precise proof provider is the written Lattices, Minkowski's theorem and the Minkowski embedding, Theorem 7.1: a centrally symmetric convex body in \(\mathbb R^n\) of volume greater than \(2^n\) times the lattice covolume contains a nonzero lattice point. Lemma 3.1 applies it with \(n=4\). Lemma 4.2 proves the maximal-order discriminant and volume assertions, including the maximality test used in both examples. Voight's original corresponding locators are Lemmas 27.3.6 and 27.6.8, Theorem 17.5.5 and Theorem 15.5.5.

Theorems 4.3–4.4 prove the maximal rational mass and prime-discriminant class-number formulas. Their original references are Voight, Theorems 25.3.15 and 30.1.5, with Main Theorem 30.8.6. The mass argument here includes the local Euler factors, lattice counting error, meromorphic residue and volume constant. The class-number argument includes existence of the two quadratic embeddings, all local ideal orbits, their global quotient and the unit stabilizers. Section 5 and Solution 6.2 use those proved formulas.

General division-algebra adelic compactness over number fields is proved in Theorem 3.3, using the bounded-basis lemma, the product formula and the integral right actions. Definiteness is not required. Its original locator is Voight, Main Theorem 27.6.14. The discrete-spectrum argument is Lesson 4, Proposition 5.1, Theorem 5.2 and Solution 7.1, after checking the compact-kernel hypothesis here. Jacquet–Langlands, Lemma 14.1, is the original automorphic discrete finite-multiplicity assertion. Its Theorem 14.2 concerns continuation and functional equations for quaternionic automorphic \(L\)-functions, rather than quaternion classification.

The modularity, cusp conditions and dimension of \(f_{11}\) are Hecke operators for congruence groups, Section 6 and Solution 1. Level-one weight-two vanishing is Dimension formulas for congruence subgroups, Theorem 4.1 and Section 4.1; old and new forms are Oldforms, newforms and the theory of Atkin, Lehner and Li, Section 1. All-prime identification of the nonconstant quaternionic eigenline uses the correspondence in Lesson 19; no transfer theorem enters the computation of \(T_2\).

## References

- J. Voight, [*Quaternion Algebras*](https://jvoight.github.io/quat.html), Graduate Texts in Mathematics 288, Springer, 2021. The complete assigned comparison scopes are §§13.1–13.4, 14.1–14.6, 27.3, 27.6, 28.4–28.5 and 41.1–41.4. Additional exact inputs are §§11.1–11.3, 12.4, 15.5, 17.5, 25.3, 30.1 and 30.8. Sections 28.4–28.5 concern strong approximation and norm class maps; they do not turn a definite class set into a single class. Sections 41.3–41.4 compare the Brandt multiplication and adjoint conventions.
- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, Springer, 1970, §14, Lemma 14.1 and Theorem 14.2, with its complete proof through Lemma 14.2.1. The latter theorem's quaternionic \(L\)-function context prepares the correspondence in Lesson 19.
