# Semisimple rings and Wedderburn's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An invariant subspace need not have an invariant complement. The simplest obstruction is the strictly upper triangular part of a triangular matrix algebra. This lesson isolates that obstruction as the Jacobson radical. Removing it from an Artinian ring leaves a product of full matrix rings over division rings. The result applies to arbitrary unital rings; no ground field is needed.

The prerequisite is Groups with operators, especially Schur's lemma, complete reducibility and finite-length modules. Basic references are [MIT], [Voight] and [Noether]. We use left modules. Endomorphisms multiply by composition, and every algebra and ring homomorphism preserves the identity.

## 1. Projections inside a ring

An **idempotent** is an element \(e\) with \(e^2=e\). It gives the left-module decomposition

\[
R=Re\oplus R(1-e).
\]

Indeed, \(r=re+r(1-e)\), and multiplying an element of the intersection on the right by \(e\) makes it both itself and zero. Conversely, a projection \(p\) of the left regular module has the form \(p(r)=re\), where \(e=p(1)\); its square equals itself exactly when \(e^2=e\).

For orthogonal idempotents \(e_1,\ldots,e_t\) with \(\sum e_i=1\), there is the **Peirce decomposition**

\[
R=\bigoplus_{i,j}e_iRe_j
\]

as an additive group. Every \(r\) is the sum of \(e_i r e_j\). Multiplication by \(e_i\) and \(e_j\) retrieves that component, proving directness. Products satisfy

\[
(e_iRe_j)(e_kRe_l)=0\quad(j\ne k),
\qquad (e_iRe_j)(e_jRe_l)\subseteq e_iRe_l.
\]

The diagonal corners are rings with identities \(e_i\). The off-diagonal corners describe how the corresponding pieces interact.

If each \(e_i\) is central, all off-diagonal corners vanish, and \(R\simeq\prod e_iR\) as rings. Conversely, a ring product decomposition supplies these central idempotents. In a left Artinian ring, repeated splitting by nontrivial central idempotents terminates: an endless choice of a factor that still splits would produce a strictly descending chain of nonzero left ideals. The resulting factors are called **blocks**. A block need not be a simple ring: a local ring such as \(k[t]/(t^2)\) has one block and still has a nonzero radical.

## 2. The elements that annihilate every simple module

The **Jacobson radical** \(J=J(R)\) is the intersection of the annihilators of all simple left \(R\)-modules. Each annihilator is a two-sided ideal, so \(J\) is a two-sided ideal. A nonzero unital ring has maximal left ideals, by Zorn's lemma: a chain of proper left ideals cannot contain \(1\) in its union.

### Lemma 2.1. Three descriptions of the radical

For \(a\in R\), the following are equivalent:

1. \(a\in J\).
2. \(a\) belongs to every maximal left ideal.
3. \(1-ra\) is a unit for every \(r\in R\).

Every left ideal all of whose elements are nilpotent is contained in \(J\).

**Proof.** If \(a\) annihilates every simple module, it annihilates \(R/P\) for every maximal left ideal \(P\), so \(a\in P\). Conversely, for any nonzero element \(v\) of a simple module \(S\), the surjection \(R\to S\), \(r\mapsto rv\), has a maximal left ideal as kernel. If \(a\) lies in every such kernel, it annihilates every \(v\), proving (1).

Assume (2). The element \(u=1-ra\) belongs to no maximal left ideal: such an ideal already contains \(ra\), so containing \(u\) would make it contain \(1\). Thus \(Ru=R\), and there is \(b\) with \(bu=1\). This is initially only a left inverse. But \(b=1+bra\), and \(bra\in J\). The same argument gives a left inverse \(c\) of \(b\). Then \(c=cbu=u\), so \(ub=1\) as well. Thus \(u\) is a unit.

If (2) fails, choose a maximal left ideal \(P\) with \(a\notin P\). Since \(P+Ra=R\), some \(r\) satisfies \(1-ra\in P\). This element has no left inverse, since a proper left ideal cannot contain a left-invertible element. This contradicts (3).

Finally, if \(a\) belongs to a nil left ideal, every \(ra\) is nilpotent. A finite geometric series in \(ra\) inverts \(1-ra\). Condition (3) puts \(a\) in \(J\). \(\square\)

### Lemma 2.2. Nakayama's lemma

If \(M\) is a finitely generated left module and \(JM=M\), then \(M=0\).

**Proof.** If \(M\ne0\), choose a generating set \(x_1,\ldots,x_m\) of least possible positive size. Since \(x_m\in JM\), expanding elements of \(M\) in these generators gives

\[
x_m=j_1x_1+\cdots+j_mx_m,\qquad j_i\in J.
\]

The element \(1-j_m\) is a unit by Lemma 2.1. Solving for \(x_m\) expresses it in the first \(m-1\) generators, a contradiction. This also covers \(m=1\), when the expression makes \(x_1=0\). \(\square\)

### Theorem 2.3. Radical structure of an Artinian ring

If \(R\) is left Artinian, then \(J\) is nilpotent and \(R/J\) is semisimple as a left module over itself. The radical contains every nil left ideal and is itself a nilpotent two-sided ideal.

**Proof.** The descending powers of \(J\) stabilize. Choose \(n\geq1\) with \(J^n=J^{n+1}=\cdots\), and put \(I=J^n\). Then \(I^2=I\). Suppose \(I\ne0\). Among left ideals \(K\) with \(IK\ne0\), choose a minimal one by the descending chain condition; \(R\) is one such ideal. The left ideal \(IK\) lies in \(K\), and

\[
I(IK)=I^2K=IK\ne0.
\]

Minimality gives \(IK=K\). Some \(x\in K\) has \(Ix\ne0\), since otherwise all finite sums defining \(IK\) would vanish. The cyclic left ideal \(Rx\subseteq K\) satisfies \(I(Rx)=Ix\ne0\), so minimality also gives \(Rx=K\). Since \(I\subseteq J\), we have \(JK=K\). Nakayama's lemma applies to this cyclic module and gives \(K=0\), a contradiction. Thus \(J^n=0\).

To identify the quotient, choose a minimal member \(P_1\cap\cdots\cap P_t\) among finite intersections of maximal left ideals. Intersecting it with any further maximal left ideal cannot decrease it. Consequently it equals their total intersection, which is \(J\) by Lemma 2.1. The map

\[
R/J\longrightarrow\bigoplus_{i=1}^t R/P_i,
\qquad r+J\longmapsto(r+P_i)_i,
\]

is injective. The target is a finite direct sum of simple modules. Its submodules are semisimple by complete reducibility in the preceding lesson. Hence \(R/J\) is semisimple. If \(R=0\), these conclusions are immediate, with the empty decomposition. The assertion about nil left ideals is Lemma 2.1. \(\square\)

The minimal-left-ideal argument matters here: one cannot apply the finitely generated version of Nakayama directly to a stabilized power before establishing its finite generation.

## 3. Matrix rings reconstructed from simple modules

A ring \(R\) is **semisimple** if its left regular module is a direct sum of simple modules. Because \(1\) has finite support in that direct sum and generates \(R\), only finitely many summands occur.

### Theorem 3.1. Wedderburn–Artin and its uniqueness

The following conditions on a unital ring are equivalent:

1. \(R\) is semisimple.
2. \(R\) is left Artinian and \(J(R)=0\).
3. There are division rings \(D_i\) and positive integers \(n_i\) with
   \[
   R\simeq\prod_{i=1}^t M_{n_i}(D_i).
   \]
4. Every left \(R\)-module is semisimple.

The matrix factors, including the integers \(n_i\) and the division rings up to isomorphism, are unique up to permutation. A nonzero simple left Artinian ring has exactly one factor \(M_n(D)\).

**Proof.** If (1) holds, the regular module has finite length and is Artinian. Every element of \(J\) annihilates its simple summands, hence all of \(R\); applying it to \(1\) gives zero. Thus (2) holds. Condition (2) implies (1) by Theorem 2.3.

To derive (3) from (1), group the finitely many simple summands by isomorphism class:

\[
{}_RR\simeq\bigoplus_{i=1}^t S_i^{n_i},\qquad S_i\not\simeq S_j\quad(i\ne j).
\]

Schur's lemma makes \(E_i=\operatorname{End}_R(S_i)\) a division ring and makes cross-Hom spaces zero. A map between copies of one \(S_i\) is specified by a matrix of elements of \(E_i\); composition is matrix multiplication with composition in each entry. Therefore

\[
\operatorname{End}_R({}_RR)\simeq\prod_i M_{n_i}(E_i).
\]

Every endomorphism of the regular module is right multiplication by its value at \(1\). Composing right multiplication by \(a\) after right multiplication by \(b\) multiplies by \(ba\), so this endomorphism ring is \(R^{\mathrm{op}}\). Taking opposite rings gives (3), with \(D_i=E_i^{\mathrm{op}}\). Transposition supplies the isomorphism \(M_n(E)^{\mathrm{op}}\simeq M_n(E^{\mathrm{op}})\). This explains the opposite-ring convention rather than suppressing it.

For the reverse implication, columns give a decomposition of \(M_n(D)\) into \(n\) copies of \(D^n\). A nonzero column vector generates \(D^n\): choose a nonzero coordinate, use its inverse and a matrix unit to obtain each standard vector. Thus the column module is simple. Each matrix factor, and then their finite product, has a semisimple regular module.

Every module is a quotient of a free module, possibly on an infinite set of generators. A direct sum of semisimple modules is a sum of simple submodules and is semisimple. Its quotient is semisimple by the preceding lesson. This proves (1) implies (4); (4) applied to the regular module proves (1).

For uniqueness, the central idempotents that cannot be decomposed into two nonzero orthogonal central idempotents identify the factors. In \(M_n(D)\), a matrix commuting with every matrix unit is scalar diagonal, and commuting with all diagonal entries makes that scalar central in \(D\). Its centre is the field \(Z(D)\), whose only idempotents are \(0,1\). Thus the primitive central idempotents are exactly the factor identities. A ring isomorphism must permute them. In a given factor, every simple module is a quotient of the regular module and therefore isomorphic to the column module. Its endomorphism ring is \(D^{\mathrm{op}}\): commuting with the matrix units forces an endomorphism to multiply each coordinate on the right by one common element of \(D\). Consequently the simple module determines \(D\). The length of the regular module is \(n\), which determines the matrix size. This proves uniqueness.

Finally, \(M_n(D)\) is simple: from any nonzero matrix entry in a two-sided ideal, multiplication by matrix units and the inverse of that entry produces all matrix units and then \(1\). A product of two nonzero factors has proper nonzero two-sided ideals. If \(R\) is simple and left Artinian, its radical, being a proper two-sided ideal, is zero; (2) and (3) then give exactly one factor. \(\square\)

### Corollary 3.2. An Artinian ring is Noetherian

Every left Artinian unital ring has finite length as a left module over itself and is left Noetherian.

**Proof.** If \(J^n=0\), the layers \(J^i/J^{i+1}\), including \(R/J\), are modules over the semisimple ring \(R/J\), hence semisimple. They are Artinian because submodules and quotients of an Artinian module are Artinian. An Artinian direct sum of simple modules must have finitely many summands; infinitely many would allow a descending chain obtained by deleting successively distinct summands. Thus each layer has finite length. Length additivity along the finite radical filtration gives finite length for \(R\), and an ascending chain cannot have more strict steps than that length. \(\square\)

This proves the Akizuki–Hopkins–Levitzki conclusion in the scope needed here, rather than presupposing it in the radical proof.

## 4. Algebras one can calculate

**Triangular matrices.** Let \(T\) be the ring of upper triangular \(2\times2\) matrices over a field \(k\). Its strictly upper triangular ideal \(U=kE_{12}\) has square zero. It lies in \(J(T)\) by Lemma 2.1. The quotient is \(k\times k\), whose radical is zero. Every simple module of the quotient is a simple \(T\)-module, so the image of \(J(T)\) in that quotient is zero. Hence \(J(T)=U\). The idempotents \(E_{11},E_{22}\) decompose the left regular module, but are not central: the off-diagonal corner is nonzero. The ring has one block.

**A square-zero element.** The ring \(k[t]/(t^2)\) has radical \((t)\), by exactly the same quotient argument. It is not semisimple. The obstruction is present even though its vector-space dimension is only two.

**The group algebra of \(S_3\).** Write \(r=(123)\), \(s=(12)\), so \(r^3=s^2=1\) and \(srs=r^{-1}\). Over \(F=\mathbb R\) or \(\mathbb C\), use

\[
\rho(r)=\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad
\rho(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

These matrices satisfy the relations. Alongside \(\rho\), take the trivial and sign representations. They give an algebra map

\[
F[S_3]\longrightarrow F\times F\times M_2(F).
\]

Let \(e_+=\frac16\sum_g g\) and \(e_-=\frac16\sum_g\operatorname{sgn}(g)g\). Their images are \((1,0,0)\) and \((0,1,0)\). The third coordinates vanish because \(1+\rho(r)+\rho(r)^2=0\), and the six-term sums group into triples. Put \(e_0=1-e_+-e_-\). The images of \(e_0,e_0r,e_0s,e_0sr\) have zero first two coordinates and third coordinates \(I,\rho(r),\rho(s),\rho(sr)\). These four matrices are linearly independent: in a relation with coefficients \(\alpha,\beta,\gamma,\delta\), the entries give \(\gamma=-\beta\), \(\delta=-2\beta\), \(\alpha=2\beta\), and \(3\beta=0\). In either field all coefficients vanish. The algebra map is therefore onto; both sides have dimension six, so it is an isomorphism:

\[
\mathbb C[S_3]\simeq\mathbb C\times\mathbb C\times M_2(\mathbb C),
\qquad
\mathbb R[S_3]\simeq\mathbb R\times\mathbb R\times M_2(\mathbb R).
\]

This computation proves the decomposition directly; the general averaging theorem appears in *Representations, characters and the group determinant*.

**Quaternions.** The real quaternion algebra \(\mathbb H\) has basis \(1,i,j,ij\), with \(i^2=j^2=-1\) and \(ij=-ji\). Conjugation gives \(q\bar q=a^2+b^2+c^2+d^2\) for \(q=a+bi+cj+dij\). A nonzero element has inverse \(\bar q/(q\bar q)\), so \(\mathbb H\) is a real division algebra and a semisimple ring. Over \(\mathbb C\), send its two generators to

\[
i\longmapsto\begin{pmatrix}\mathrm i&0\\0&-\mathrm i\end{pmatrix},
\qquad
j\longmapsto\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Their squares are \(-I\), they anticommute, and the images of \(1,i,j,ij\) are linearly independent over \(\mathbb C\). Thus

\[
\mathbb H\otimes_{\mathbb R}\mathbb C\simeq M_2(\mathbb C).
\]

Frobenius's real division-algebra theorem states that every finite-dimensional associative real division algebra is \(\mathbb R\), \(\mathbb C\) or \(\mathbb H\). It is stated here, with reference [Frobenius]; its proof is outside this lesson. The finite-dimensional \(C^*\)-algebra case adds an involution and positivity, as discussed in *Foundations of von Neumann algebras*, in its lesson on AF-algebras.

## 5. Exercises

### Exercise 5.1. Easy: radical and blocks

Compute the radical, its nilpotence exponent and the quotient for the upper triangular \(3\times3\) matrices over \(k\). Determine whether its three diagonal idempotents are central, and find all central idempotents.

### Exercise 5.2. Medium: finite group calculations

For a generator \(z\) of the cyclic group of order \(m\), construct \(\mathbb C[\langle z\rangle]\simeq\mathbb C^m\) and its primitive idempotents. For \(S_3\), justify every coordinate of the three idempotents \(e_+,e_-,e_0\) from Section 4 and recover its three simple modules.

### Exercise 5.3. Medium: the division ring and its side

For a minimal nonzero left ideal \(L\) in a simple left Artinian ring, prove that \(\operatorname{End}_R(L)^{\mathrm{op}}\) is a division ring. For \(R=M_n(D)\), compute the endomorphisms of the column module explicitly, and verify the multiplication order.

### Exercise 5.4. Medium: splitting the quaternions

Check the two matrix relations in the complex model of \(\mathbb H\), calculate the image of \(ij\), and express each standard \(2\times2\) matrix unit as a complex linear combination of the four images.

### Exercise 5.5. Hard: recover the factors intrinsically

Suppose \(\prod_i M_{n_i}(D_i)\simeq\prod_j M_{m_j}(E_j)\) as rings. Prove uniqueness without using the dimension over a ground field, which need not exist in the statement. Identify the invariant recovering the size of a matrix factor.

## 6. Solutions

### Solution 5.1

The strictly upper triangular ideal \(U\) has \(U^3=0\), while \(E_{12}E_{23}=E_{13}\ne0\), so its nilpotence exponent is three. Its quotient is \(k^3\), which is semisimple. The same nil-ideal and quotient argument as in Section 4 gives \(J=U\). A matrix commuting with each \(E_{aa}\) must be diagonal. A diagonal matrix \(\operatorname{diag}(d_1,d_2,d_3)\) commutes with \(E_{12}\) and \(E_{23}\) exactly when \(d_1=d_2=d_3\). Thus the centre is the scalar matrices, and its idempotents are just \(0,I\). The ring has one block, and none of the three individual diagonal matrix units is central.

### Solution 5.2

Let \(\zeta=\exp(2\pi\mathrm i/m)\). Identify the group algebra with \(\mathbb C[t]/(t^m-1)\), and send the class of \(f\) to \((f(\zeta^j))_{j=0}^{m-1}\). The roots are distinct, and division by the product of the linear factors shows that the kernel before passing to the quotient is exactly \((t^m-1)\). Interpolation proves surjectivity. The idempotent with coordinate one at \(j\) and zero elsewhere is

\[
e_j=\frac1m\sum_{a=0}^{m-1}\zeta^{-ja}z^a.
\]

Evaluation uses the geometric sum \(\sum_a\zeta^{(l-j)a}\), equal to \(m\) for \(l=j\) and zero otherwise. The one-dimensional simple modules have \(z\) acting by \(\zeta^j\).

For \(S_3\), the trivial coordinate of \(e_+\) is one; its sign coordinate is zero because there are three even and three odd permutations. Its matrix coordinate is \(\frac16(I+\rho(s))(I+\rho(r)+\rho(r)^2)=0\). For \(e_-\), the trivial coordinate is zero, its sign coordinate is one, and its matrix coordinate is \(\frac16(I-\rho(s))(I+\rho(r)+\rho(r)^2)=0\). Subtraction from \(1\) gives the image \((0,0,I)\) for \(e_0\). The simple modules are the trivial line, the sign line and the two-dimensional column module for the matrix factor. The last is irreducible because the image algebra is all of \(M_2(F)\), which acts simply on columns.

### Solution 5.3

A minimal nonzero left ideal is simple. Schur's lemma makes its endomorphism ring a division ring, and reversing multiplication in a division ring again gives a division ring, with the same inverses. On \(D^n\), an endomorphism commuting with the diagonal matrix units sends each coordinate axis to itself. Commuting with the other matrix units makes its action on each coordinate the same additive map \(h:D\to D\). Commuting with multiplication by any \(d\in D\) gives \(h(dx)=d h(x)\), so \(h(x)=x h(1)\). The endomorphism is right multiplication by \(c=h(1)\). If \(T_c(v)=vc\), then \(T_c\circ T_d(v)=vdc\). Hence \(c\mapsto T_c\) identifies \(D^{\mathrm{op}}\) with the endomorphism ring. Taking the opposite recovers \(D\), as required by Theorem 3.1.

### Solution 5.4

Write the two displayed images as \(A,B\). Direct multiplication gives \(A^2=B^2=-I\),

\[
AB=\begin{pmatrix}0&\mathrm i\\\mathrm i&0\end{pmatrix},
\qquad BA=-AB.
\]

The matrix units are

\[
E_{11}=\tfrac12(I+A/\mathrm i),\quad
E_{22}=\tfrac12(I-A/\mathrm i),\quad
E_{12}=\tfrac12(B+AB/\mathrm i),\quad
E_{21}=\tfrac12(-B+AB/\mathrm i).
\]

They show surjectivity of the quaternion homomorphism. Domain and target have complex dimension four, so it is an isomorphism.

### Solution 5.5

The primitive central idempotents are exactly the identities of the separate matrix factors: their centres are fields, and no field has a nontrivial idempotent. The isomorphism must give a bijection between these idempotents and hence between the factors. Within a factor \(M_n(D)\), every simple module is isomorphic to the column module, because the regular module is the sum of its \(n\) simple columns and every simple module is a cyclic quotient of that regular module. The endomorphism ring of the column module is \(D^{\mathrm{op}}\), by Solution 5.3. An isomorphism of rings transports modules and their endomorphism rings, so matched factors have isomorphic division rings. Finally, the composition length of the regular module of \(M_n(D)\) is \(n\), independently of cardinalities or field dimensions. Ring isomorphisms preserve this length, so \(n_i=m_j\) for matched factors. This completes the uniqueness proof in its full ring-theoretic generality.

## What this lesson does not prove

Frobenius's classification of finite-dimensional real associative division algebras is stated with its original reference. The structure theorem for finite-dimensional \(C^*\)-algebras is only a comparison with a later analytic subject. Radical nilpotence, the semisimple quotient, Wedderburn–Artin, its uniqueness and the left Artinian-to-Noetherian implication have all been proved here for unital rings.

## References

- **[MIT]** *Noncommutative Algebra*, MIT OpenCourseWare, Spring 2023, instructor Roman Bezrukavnikov, lectures 2–6. [Course notes](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/resources/mit18_706_s23_full_lec_pdf/).
- **[Voight]** John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288, Springer, 2021, §§7.2–7.4. [Author's book page](https://jvoight.github.io/quat.html).
- **[Noether]** Emmy Noether, *Hyperkomplexe Größen und Darstellungstheorie*, written up by B. L. van der Waerden, *Mathematische Zeitschrift* **30** (1929), 641–692, §§8–14; and *Nichtkommutative Algebra*, *Mathematische Zeitschrift* **37** (1933), 514–541, §5.
- **[Frobenius]** Ferdinand Georg Frobenius, *Über lineare Substitutionen und bilineare Formen*, *Journal für die reine und angewandte Mathematik* **84** (1878), 1–63, for the real division-algebra theorem.
