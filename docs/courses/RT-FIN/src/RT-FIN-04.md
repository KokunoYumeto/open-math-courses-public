# Tensor products, duals and real representations

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

A character remembers enough to recover a complex representation. It also tells us whether that representation can be written with real matrices, provided we ask the right question. Real character values alone do not suffice: the two-dimensional representation of the quaternion group is the basic counterexample.

We use Characters and the orthogonality relations and [The group algebra and Fourier analysis on a finite group](RT-FIN-03.md). Representations are finite-dimensional, \(G\) is finite, and the ground field is \(\mathbb C\) unless a real vector space is explicitly named. Inner products are linear in the first variable.

## 1. Operations on representations and their traces

For representations \(V,W\), define

\[
g(v\otimes w)=gv\otimes gw,\qquad
(g\ell)(v)=\ell(g^{-1}v)\quad(\ell\in V^*).
\]

The representation laws follow by applying two group elements successively. The map

\[
V^*\otimes W\longrightarrow\operatorname{Hom}_{\mathbb C}(V,W),
\qquad \ell\otimes w\longmapsto(v\mapsto\ell(v)w)
\]

is an isomorphism: in bases, the elementary tensors map to the rectangular matrix units. It is equivariant for \(gT=\rho_W(g)T\rho_V(g^{-1})\).

**Proposition 1.1 (character operations).** Writing \(\chi=\chi_V\),

\[
\chi_{V\otimes W}=\chi_V\chi_W,\qquad
\chi_{V^*}(g)=\chi(g^{-1})=\overline{\chi(g)},\qquad
\chi_{\operatorname{Hom}(V,W)}=\overline{\chi_V}\chi_W.
\tag{1}
\]

Moreover,

\[
\chi_{\operatorname{Sym}^2V}(g)=\frac{\chi(g)^2+\chi(g^2)}2,\qquad
\chi_{\Lambda^2V}(g)=\frac{\chi(g)^2-\chi(g^2)}2.
\tag{2}
\]

**Proof.** In tensor-product bases, the diagonal entries are products of diagonal entries, so the trace is the product of the traces. The dual matrix is the transpose of the inverse; its trace is \(\chi(g^{-1})\). An invariant Hermitian form makes the original matrix unitary, which identifies this trace with \(\overline{\chi(g)}\).

Let \(\tau(v\otimes w)=w\otimes v\). Its \(+1\) and \(-1\) eigenspaces are the symmetric and alternating tensors, with projectors \((I+\tau)/2\) and \((I-\tau)/2\). The action \(A\otimes A\) commutes with \(\tau\). In a basis, the coefficient of \(e_i\otimes e_j\) in \(\tau(Ae_i\otimes Ae_j)\) is \(A_{ji}A_{ij}\); hence

\[
\operatorname{tr}\bigl(\tau(A\otimes A)\bigr)
=\sum_{i,j}A_{ij}A_{ji}=\operatorname{tr}(A^2).
\]

Taking the trace after each projector gives (2). \(\square\)

The invariant vectors in \(\operatorname{Hom}(V,W)\) are exactly the intertwiners. Averaging its character therefore recovers

\[
\dim\operatorname{Hom}_G(V,W)=
\frac1{|G|}\sum_g\overline{\chi_V(g)}\chi_W(g)
=\langle\chi_W,\chi_V\rangle.
\tag{3}
\]

These formulas calculate multiplicities in tensor products without constructing a decomposition beforehand. They do not say that a tensor product of two irreducibles is usually irreducible.

## 2. A character sum detects invariant bilinear forms

A bilinear form \(B:V\times V\to\mathbb C\) is invariant when \(B(gv,gw)=B(v,w)\). It defines the intertwiner \(V\to V^*\), \(v\mapsto B(v,-)\). If \(V\) is irreducible, Schur's lemma says that the space of such forms has dimension zero or one. A nonzero form is nondegenerate. Its transpose \(B^{\mathrm t}(v,w)=B(w,v)\) is another invariant form, and transposing twice is the identity. Uniqueness thus makes \(B^{\mathrm t}=B\) or \(B^{\mathrm t}=-B\).

Define the **Frobenius–Schur indicator**

\[
\nu(\chi)=\frac1{|G|}\sum_{g\in G}\chi(g^2).
\tag{4}
\]

**Theorem 2.1 (forms and indicator).** For an irreducible complex representation \(V\),

\[
\nu(\chi)=
\begin{cases}
1&\text{a nonzero invariant symmetric bilinear form exists},\\
-1&\text{a nonzero invariant alternating bilinear form exists},\\
0&\text{no nonzero invariant bilinear form exists}.
\end{cases}
\tag{5}
\]

The last case is equivalent to \(\chi\) not being real-valued.

**Proof.** The symmetric and alternating forms are the invariant subspaces in \(\operatorname{Sym}^2(V^*)\) and \(\Lambda^2(V^*)\). Let their dimensions be \(b_+\) and \(b_-\). Formula (2), applied to \(V^*\), and the invariant-vector character formula give

\[
b_+-b_-=\frac1{|G|}\sum_g\overline{\chi(g^2)}
=\overline{\nu(\chi)}.
\]

The left side is an integer, so \(\nu(\chi)\) equals it. Uniqueness and nondegeneracy of a nonzero invariant form say that the pair \((b_+,b_-)\) is exactly one of \((1,0),(0,1),(0,0)\). This proves (5).

A nonzero form exists exactly when \(V\simeq V^*\). The character of \(V^*\) is \(\overline\chi\), so character determination makes this equivalent to \(\chi=\overline\chi\) pointwise. \(\square\)

The indicator is attached here to an **irreducible** character. For an arbitrary character it is additive on irreducible constituents and need not be one of these three numbers.

## 3. From a bilinear form to a real or quaternionic structure

A **real form** of \(V\) is a real \(G\)-module \(R\) with \(V\simeq R\otimes_{\mathbb R}\mathbb C\). Equivalently, \(V\) has a basis in which all group matrices are real. A **quaternionic structure** is a conjugate-linear equivariant map \(J:V\to V\) with \(J^2=-I\).

**Theorem 3.1 (realizability).** An irreducible \(V\) has a real form exactly when \(\nu(\chi)=1\). It has a quaternionic structure exactly when \(\nu(\chi)=-1\). In the latter case its complex dimension is even.

**Proof.** Fix an invariant positive Hermitian inner product \(H\). For a nonzero invariant bilinear form \(B\), there is a unique conjugate-linear map \(J\) satisfying

\[
B(v,w)=H(v,Jw).
\tag{6}
\]

Existence and uniqueness follow by writing both forms in an orthonormal basis; conjugate-linearity is what makes the right side linear in \(w\). Nondegeneracy makes \(J\) invertible. Invariance of both forms gives \(Jg=gJ\), by testing (6) on all \(v\).

The form \(H'(v,w)=H(Jw,Jv)\) is positive Hermitian and invariant. Two invariant Hermitian forms on an irreducible are proportional: write \(H'(v,w)=H(Tv,w)\); invariance makes \(T\) an equivariant complex-linear operator, and Schur's lemma makes it scalar. Positivity then gives \(H'=cH\) with \(c>0\). In particular,

\[
H(Jv,Jv)=cH(v,v).
\]

The complex-linear equivariant operator \(J^2\) is \(\lambda I\). If \(B(w,v)=\epsilon B(v,w)\), with \(\epsilon=1\) or \(-1\), substituting \(w=Jv\) gives

\[
H(Jv,Jv)=B(Jv,v)=\epsilon B(v,Jv)
=\epsilon H(v,J^2v)
=\epsilon\overline\lambda H(v,v).
\]

Therefore \(\lambda=\epsilon c\). Replacing \(J\) by \(J/\sqrt c\) makes it antiunitary and gives \(J^2=\epsilon I\).

When \(\epsilon=1\), the fixed space \(R=\{v:Jv=v\}\) is invariant over \(\mathbb R\), and

\[
v=\frac{v+Jv}{2}
+i\frac{v-Jv}{2i}
\]

writes every vector uniquely in \(R\oplus iR\). A real basis of \(R\) is therefore a complex basis of \(V\), giving a real form. Conversely, a real form has an invariant positive real inner product by finite averaging. Its complex-bilinear extension is an invariant nondegenerate symmetric form, so Theorem 2.1 gives \(\nu=1\).

When \(\epsilon=-1\), the normalized \(J\) is the required quaternionic structure. Conversely, an equivariant conjugate-linear \(J\) with square \(-I\) can be made antiunitary by replacing \(H\) with

\[
H_0(v,w)=H(v,w)+H(Jw,Jv).
\]

This is positive and invariant, and satisfies \(H_0(Jv,Jw)=H_0(w,v)\). The form \(B(v,w)=H_0(v,Jw)\) is then bilinear and invariant, and

\[
B(w,v)=H_0(J^2v,Jw)=-B(v,w).
\]

It is nondegenerate, so \(\nu=-1\). Finally write \(Jv=M\overline v\) in a complex basis. Its square being \(-I\) means \(M\overline M=-I\). Taking determinants gives \(|\det M|^2=(-1)^{\dim V}\); the left side is positive, forcing even dimension. \(\square\)

### What the corresponding irreducibles over \(\mathbb R\) are

“Real-valued character,” “complex representation with a real form,” and “irreducible representation over \(\mathbb R\)” name different properties. The following description keeps all three fields of scalars visible.

**Proposition 3.2 (real irreducibles).**

| Complex irreducible type | Irreducible real module | Its complexification | Real commuting algebra |
|---|---|---|---|
| \(\nu=1\) | a real form \(R\) | \(V\) | \(\mathbb R\) |
| \(\nu=0\) | \(V\) with scalars restricted to \(\mathbb R\) | \(V\oplus\overline V\) | \(\mathbb C\) |
| \(\nu=-1\) | \(V\) with scalars restricted to \(\mathbb R\) | \(V\oplus V\) | \(\mathbb H\) |

Every irreducible real \(G\)-module occurs on this list. In the middle row, \(V\) and \(\overline V\) give the same real isomorphism class; there are no other repetitions.

**Proof.** On the underlying real space \(V_{\mathbb R}\), write \(I\) for multiplication by \(i\). Every real-linear equivariant map \(T\) splits as

\[
T=\frac{T-ITI}{2}+\frac{T+ITI}{2}.
\]

The first part is complex-linear and hence scalar. The second is conjugate-linear. Such maps correspond to intertwiners \(\overline V\to V\); their space is zero if \(\nu=0\), and one-dimensional over \(\mathbb C\) otherwise. In the latter cases a normalized \(J\) from Theorem 3.1 spans it. Thus the real commutant is either \(\mathbb C\), or

\[
\{a+bJ:a,b\in\mathbb C\},\qquad
Jz=\overline zJ,\quad J^2=\epsilon\,\mathrm{id}_{V_{\mathbb R}}.
\tag{7}
\]

For \(\epsilon=-1\), the generators \(I,J,IJ\) satisfy the quaternion relations. Each nonzero \(a+bJ\) has inverse

\[
\frac{\overline a-bJ}{|a|^2+|b|^2},
\]

so this algebra is the division algebra \(\mathbb H\). For \(\nu=0\), the commutant is also a division algebra, namely \(\mathbb C\). Maschke's theorem over \(\mathbb R\) implies that either underlying real module is irreducible: a proper nonzero invariant summand would yield a nontrivial idempotent in its division commutant.

For \(\epsilon=1\), \(V_{\mathbb R}=R\oplus iR\) as above. A proper real invariant subspace of \(R\) would complexify to a proper complex invariant subspace of \(V\), so \(R\) is irreducible. An equivariant real endomorphism of \(R\) extends to a scalar complex endomorphism of \(V\); preserving \(R\) forces the scalar to be real. Therefore \(\operatorname{End}_G(R)=\mathbb R\), and \(\operatorname{End}_G(V_{\mathbb R})=M_2(\mathbb R)\).

The complexification of an underlying real complex module is \(V\oplus\overline V\). One way to check this is to extend \(I\) to the complexification: its \(i\) and \(-i\) eigenspaces give the two summands, with the scalar structures of \(V\) and \(\overline V\). Their dimensions are both \(\dim_{\mathbb C}V\). When \(\nu=-1\), \(V\simeq\overline V\), giving two copies.

To prove exhaustiveness, complexify an irreducible real module \(W\) and choose a complex irreducible summand \(V\). Compose its inclusion with the real-part projection \(W\otimes\mathbb C\to W\), viewing \(V\) over \(\mathbb R\). This map is nonzero: a complex subspace cannot lie entirely in \(iW\), since multiplication by \(i\) would place it in \(W\) as well, and \(W\cap iW=0\). It is an equivariant map onto \(W\), so \(W\) is a real irreducible summand of \(V_{\mathbb R}\). The preceding cases list all such summands. Their complexifications show exactly when two entries can be isomorphic. \(\square\)

It follows that a general complex representation has a real form exactly when each quaternionic irreducible occurs with even multiplicity and each non-real irreducible occurs with the same multiplicity as its conjugate. Necessity follows by complexifying real irreducible summands; sufficiency follows by assembling the real modules in the table.

## 4. Counting square roots with the indicator

**Theorem 4.1 (square roots).** For every \(z\in G\),

\[
\#\{x\in G:x^2=z\}=\sum_i\nu(\chi_i)\chi_i(z).
\tag{8}
\]

In particular,

\[
\#\{x:x^2=1\}=\sum_i\nu(\chi_i)d_i.
\tag{9}
\]

**Proof.** The left side of (8) is a class function \(q\). Its coefficient in the orthonormal character basis is

\[
\langle q,\chi_i\rangle
=\frac1{|G|}\sum_z q(z)\overline{\chi_i(z)}
=\frac1{|G|}\sum_x\overline{\chi_i(x^2)}
=\nu(\chi_i).
\]

The last equality uses the reality of each indicator proved in Theorem 2.1. Character completeness gives (8), and setting \(z=1\) gives (9). \(\square\)

The identity is included in (9). Thus the number of elements of order exactly two is its right side minus one.

The number of real irreducible isomorphism classes also has a class-theoretic description. If \(r\) is the total class count and \(s\) is the number of classes equal to their inverse classes, that number is \((r+s)/2\). Indeed, the complex-linear operator \(f(g)\mapsto f(g^{-1})\) permutes the class-indicator basis, with trace \(s\). It also permutes the irreducible-character basis by \(\chi\mapsto\overline\chi\), so exactly \(s\) irreducible characters are self-conjugate. Proposition 3.2 counts one real module for each fixed character and one for each conjugate pair, giving \(s+(r-s)/2\).

For a group of odd order, squaring is a permutation of its elements: choose an odd common multiple \(m\) of their orders and an integer \(a\) with \(2a\equiv1\pmod m\); \(x\mapsto x^a\) is the inverse map. Hence \(\nu(\chi)=|G|^{-1}\sum_g\chi(g)\). Every nontrivial irreducible then has indicator zero, and only the trivial irreducible has a real form.

## 5. A faithful representation eventually sees every irreducible

Put \(V^{\otimes0}=\mathbb C\) with trivial action, so its character is the constant function one.

**Theorem 5.1 (Burnside–Brauer).** If \(V\) is faithful and its character takes exactly \(r\) distinct values, every irreducible occurs in one of

\[
V^{\otimes0},\quad V,\quad V^{\otimes2},\quad\ldots,\quad V^{\otimes(r-1)}.
\tag{10}
\]

**Proof.** List the character values as \(a_1,\ldots,a_r\), with \(a_1=d=\dim V\). For an irreducible character \(\psi\), suppose all its multiplicities in (10) vanish. For \(0\le k<r\),

\[
0=|G|\langle\chi^k,\psi\rangle
=\sum_{j=1}^r a_j^k b_j,\qquad
b_j=\sum_{\chi(g)=a_j}\overline{\psi(g)}.
\]

The coefficient matrix is Vandermonde; its determinant is \(\prod_{i<j}(a_j-a_i)\ne0\). Consequently every \(b_j\) is zero.

But \(\chi(g)=d\) holds exactly when \(\rho(g)=I\). Indeed, in a unitary realization the eigenvalues have absolute value one. The real part of their sum equals \(d\) only when every eigenvalue has real part one, hence equals one. Finite-order operators are diagonalizable, so the operator is the identity. Faithfulness now says that the level set for \(a_1\) consists only of the group identity. Hence \(b_1=\psi(1)>0\), a contradiction. The zero-dimensional faithful case can occur only for the trivial group and gives the same conclusion from the zeroth power. \(\square\)

The bound counts character values, rather than the representation's dimension. Including the zeroth power is essential to the precise statement.

## 6. Character tables and geometric models

### The quaternion group and a cyclic group

For \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\), use

\[
\rho(i)=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\qquad
\rho(j)=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

They satisfy \(\rho(i)^2=\rho(j)^2=-I\) and anticommute, so give the irreducible row \((2,-2,0,0,0)\) on \(1,-1,\{\pm i\},\{\pm j\},\{\pm k\}\). Two elements square to \(1\) and six square to \(-1\), giving

\[
\nu(\chi)=\frac{2\cdot2+6(-2)}8=-1.
\]

The conjugate-linear operator \(J(v)=\rho(j)\overline v\) commutes with both displayed generators and has \(J^2=-I\). This realizes the quaternionic structure directly. The underlying real space has dimension four; it is an irreducible real representation even though the complex representation has no real form.

For \(C_3=\langle t\rangle\), the characters with \(t\mapsto\zeta,\zeta^{-1}\), where \(\zeta=e^{2\pi i/3}\), each have indicator \((1+\zeta+\zeta^2)/3=0\). Their underlying real modules are isomorphic rotations of a plane; their complexifications contain the two distinct conjugate characters.

### The full table of \(S_4\)

The classes have cycle types \(1,2,22,3,4\) and sizes \(1,6,3,8,6\). The permutation representation on four letters gives the standard irreducible \(W\) with character “number of fixed letters minus one.” Twisting by sign gives another degree-three irreducible.

For the remaining degree-two representation, let \(S_4\) permute the three decompositions

\[
12|34,\qquad13|24,\qquad14|23
\]

into unordered pairs. This action gives a surjection onto \(S_3\), with kernel the Klein four-group of double transpositions. Pulling back the standard irreducible of \(S_3\) gives \(U\). In the stated class order the complete table is

| Representation | \(1\) | \(2\) | \(22\) | \(3\) | \(4\) |
|---|---:|---:|---:|---:|---:|
| Trivial | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) |
| Sign | \(1\) | \(-1\) | \(1\) | \(1\) | \(-1\) |
| \(W\) | \(3\) | \(1\) | \(-1\) | \(0\) | \(-1\) |
| \(W\otimes\mathrm{sign}\) | \(3\) | \(-1\) | \(-1\) | \(0\) | \(1\) |
| \(U\) | \(2\) | \(0\) | \(2\) | \(-1\) | \(0\) |

The five rows are characters of the representations just constructed. Their weighted norms equal one and their pairwise weighted inner products equal zero. Their degree squares sum to \(1+1+9+9+4=24\), proving completeness. If \(X\) is this table and \(D=\operatorname{diag}(1,6,3,8,6)\), direct multiplication gives

\[
XDX^{\mathrm t}=24I,\qquad
X^{\mathrm t}X=\operatorname{diag}(24,4,8,3,4).
\tag{11}
\]

The second identity checks all column centralizer orders.

Squaring sends the five class types to \(1,1,1,3,22\). Formula (2) therefore gives

\[
\chi_{\Lambda^2W}=(3,-1,-1,0,1),\qquad
\chi_{\operatorname{Sym}^2W}=(6,2,2,0,0).
\]

Character determination identifies \(\Lambda^2W\simeq W\otimes\mathrm{sign}\) and \(\operatorname{Sym}^2W\simeq\mathbf1\oplus U\oplus W\). Consequently

\[
W\otimes W\simeq
\mathbf1\oplus U\oplus W\oplus(W\otimes\mathrm{sign}).
\tag{12}
\]

All five representations have explicit real forms from their permutation constructions, so all indicators are \(+1\). The standard representation is faithful: its action together with the trivial line is the faithful four-point permutation action. Its four character values give the bound \(0\le k\le3\) in Theorem 5.1. Formula (12) supplies every type except sign by the second power, and

\[
\langle\chi_W^3,\mathrm{sign}\rangle
=\frac{27-6-3+6}{24}=1
\]

supplies sign in the third.

### \(A_5\): the table and its rotations

The preceding Fourier lesson derived all five rows from the five-letter and six-Sylow-subgroup permutation actions, completeness, and eigenvalue constraints. In class order \(1,2A,3A,5A,5B\), sizes \(1,15,20,12,12\), they are

| Degree | \(1\) | \(2A\) | \(3A\) | \(5A\) | \(5B\) |
|---|---:|---:|---:|---:|---:|
| \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(1\) |
| \(3\) | \(3\) | \(-1\) | \(0\) | \(\varphi\) | \(\varphi'\) |
| \(3\) | \(3\) | \(-1\) | \(0\) | \(\varphi'\) | \(\varphi\) |
| \(4\) | \(4\) | \(0\) | \(1\) | \(-1\) | \(-1\) |
| \(5\) | \(5\) | \(1\) | \(-1\) | \(0\) | \(0\) |

Here \(\varphi=(1+\sqrt5)/2\), \(\varphi'=(1-\sqrt5)/2\); thus \(\varphi+\varphi'=1\), \(\varphi\varphi'=-1\), and \(\varphi^2+\varphi'^2=3\). These identities verify

\[
X\operatorname{diag}(1,15,20,12,12)X^{\mathrm t}=60I,\qquad
X^{\mathrm t}X=\operatorname{diag}(60,4,3,5,5).
\tag{13}
\]

All values are real, but we still calculate the indicators. Squaring sends \(2A\) to \(1\), preserves \(3A\), and exchanges \(5A,5B\). For either degree-three row,

\[
\nu=\frac{3+15\cdot3+12(\varphi+\varphi')} {60}=1.
\]

For degrees four and five it gives respectively

\[
\frac{4+15\cdot4+20\cdot1-24}{60}=1,\qquad
\frac{5+15\cdot5-20}{60}=1.
\]

The trivial indicator is one as well. Thus both degree-three representations have real forms. Average a positive real inner product on each. Their determinants are trivial, since \(A_5\) has no nontrivial linear character, and faithfulness was proved in the preceding lesson. They embed \(A_5\) into \(SO(3)\). A trace \(\varphi\) means rotation angle \(2\pi/5\); a trace \(\varphi'\) means angle \(4\pi/5\), since a three-dimensional rotation has trace \(1+2\cos\theta\). Exchanging \(\sqrt5\) and \(-\sqrt5\) exchanges their character rows.

We can identify the polyhedron in this rotation picture without assuming it in the character construction. In either representation choose an element acting by a \(2\pi/5\) rotation and a unit vector \(v\) on its oriented axis. Its stabilizer consists of rotations about that axis and is cyclic. The element orders in \(A_5\) are \(1,2,3,5\), so this stabilizer has order five. The orbit \(S\) has twelve points. An involution in the dihedral normalizer of the order-five subgroup reverses the axis, so \(S\) contains \(-v\) and is antipodal.

The axis subgroup acts freely on the other ten points, giving two regular pentagons. Antipodality exchanges them, so their heights are \(h,-h\). The operator

\[
T=\sum_{w\in S}ww^{\mathrm t}
\]

commutes with the real irreducible action and hence is scalar, by Proposition 3.2. Its trace is twelve, so \(T=4I\). Evaluating \(v^{\mathrm t}Tv\) gives \(2+10h^2=4\), hence \(|h|=1/\sqrt5\). After choosing the upper pentagon's phase, the points are

\[
(0,0,\pm1),\qquad
p_j=\left(\frac2{\sqrt5}\cos\frac{2\pi j}5,\
\frac2{\sqrt5}\sin\frac{2\pi j}5,\
\frac1{\sqrt5}\right),\qquad -p_j
\quad(0\le j<5).
\]

The two pentagons are staggered by \(36^\circ\). Distinct nonantipodal points have inner products \(\pm1/\sqrt5\). The triples of mutual inner product \(1/\sqrt5\) give twenty equilateral triangular faces: five at each pole and ten between the pentagons. Each such triangle is supporting: its sum of vertex vectors has inner product \(1+2/\sqrt5\) with each of its vertices, while every other orbit point has inner product at most \(3/\sqrt5\) with that sum. These triangles form the convex hull's boundary, with thirty edges, each belonging to two triangles. The hull is therefore a regular icosahedron. A rotation preserving it is determined by a vertex and one of that vertex's five neighbors, so there are at most \(12\cdot5=60\) such rotations. The faithful \(A_5\) action already supplies sixty; it is the full rotational symmetry group.

## 7. Exercises with solutions

### Exercise 1. Three groups, three indicator calculations

Compute the indicators of every irreducible of \(S_3\), of the dihedral group \(D_4\) of order eight, and of \(Q_8\).

**Solution.** For \(S_3\), trivial and sign have indicator one: their values on every square are one. The degree-two character has values \(2,0,-1\), and squaring sends a transposition to the identity and interchanges the two 3-cycles. Its indicator is \((2+3\cdot2+2(-1))/6=1\).

For \(D_4=\langle r,s:r^4=s^2=1,\ srs=r^{-1}\rangle\), its four linear characters send each generator to \(\pm1\), so again their values on squares are one. The degree-two square-symmetry character is \(2,-2,0,0,0\) on \(1,r^2,\{r,r^3\},\{s,r^2s\},\{rs,r^3s\}\). Six elements square to \(1\) and two square to \(r^2\), giving \((6\cdot2+2(-2))/8=1\).

The four linear characters of \(Q_8\) factor through its exponent-two quotient by \(\{\pm1\}\), so have indicator one. Its degree-two character has indicator \((2\cdot2+6(-2))/8=-1\), as above. Thus the equal character tables of \(D_4\) and \(Q_8\) do not give equal indicators: one also needs the class map induced by squaring.

### Exercise 2. Involutions in \(S_4\)

Prove (9) and use it to count the elements of order exactly two in \(S_4\).

**Solution.** The regular character is \(\chi_{\mathrm{reg}}=\sum_i d_i\chi_i\), equal to \(|G|\) at the identity and zero elsewhere. Therefore

\[
\sum_i d_i\nu(\chi_i)=
\frac1{|G|}\sum_g\chi_{\mathrm{reg}}(g^2)
=\#\{g:g^2=1\}.
\]

All five \(S_4\) indicators are one, so this number is \(1+1+3+3+2=10\). Subtract the identity to obtain nine involutions. Directly, they are the six transpositions and three double transpositions, giving the same count.

### Exercise 3. Real values versus a real form

Prove that every character of \(S_n\) is real-valued. State what this alone proves about irreducible indicators, and determine the indicators in \(S_4\).

**Solution.** A permutation and its inverse have the same cycle lengths. Permutations with the same cycle lengths are conjugate: match corresponding cycles entry by entry. Characters are constant on conjugacy classes, so \(\chi(g)=\chi(g^{-1})=\overline{\chi(g)}\). For an irreducible, Theorem 2.1 then says \(\nu=\pm1\), without deciding the sign.

For \(S_4\), trivial and sign are real one-dimensional representations. The standard representation is the real sum-zero subspace of the permutation representation; its sign twist is also defined over \(\mathbb R\). The degree-two representation is pulled back from the real standard plane of \(S_3\) through the action on pairings. Thus every one of the five irreducibles has a real form and indicator \(+1\). The general rational constructions for \(S_n\) will provide the stronger conclusion for every \(n\).

### Exercise 4. The tensor bound and its precise scope

Prove Theorem 5.1 by grouping elements according to their character values. Then state and prove its counterpart when the representation is not faithful.

**Solution.** If an irreducible \(\psi\) occurs in none of the first \(r\) powers, its \(r\) zero multiplicities give the linear equations \(\sum_j a_j^k b_j=0\), \(0\le k<r\), with \(b_j=\sum_{\chi(g)=a_j}\overline{\psi(g)}\). Distinct values make the Vandermonde matrix invertible. Hence \(b_j=0\) for every \(j\). The level \(\chi(g)=\dim V\) consists of elements acting identically; for a faithful representation it is \(\{1\}\). Its sum is \(\psi(1)>0\), contradiction.

For an arbitrary representation with kernel \(K\), every tensor power is trivial on \(K\). Thus every constituent factors through \(G/K\). Conversely the representation of \(G/K\) is faithful, has the same \(r\) character values, and Theorem 5.1 gives every irreducible of that quotient in a power with exponent at most \(r-1\). Inflating to \(G\) proves that the constituents of all tensor powers are exactly the irreducibles with \(K\) in their kernels, with the same bound. For example, powers of the trivial representation of a nontrivial group never supply any nontrivial irreducible.

## 8. Prerequisite results used without proof

Complete reducibility over \(\mathbb R\) and \(\mathbb C\), invariant positive inner products and Schur's lemma come from the first lesson. Character determination, orthogonality, class completeness and regular multiplicities come from the second. The class sizes, simplicity, permutation constructions and degree-three character derivation for \(A_5\) are proved in Exercise 4 of the preceding Fourier lesson. We also use elementary finite-dimensional linear algebra: trace, determinants, adjoints and the Vandermonde determinant formula.

The general Young-tableau construction over \(\mathbb Q\) for \(S_n\) is a later topic; this lesson proves real realizability for \(S_4\) directly. No general classification of finite-dimensional division algebras was needed for Proposition 3.2: its three commuting algebras were computed from complex Schur's lemma and conjugate-linear operators.

## References

- **C. Gruson and V. Serganova**, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, 2018, Chapter 1 §2 for tensor and dual actions; Theorem 4.27 for faithful tensor powers; §§6–8, especially Lemmas 6.2–6.4, Proposition 8.3 and Corollary 8.4, for invariant forms and real representations.
- **F. G. Frobenius and I. Schur**, *Über die reellen Darstellungen der endlichen Gruppen*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin, 1906, pp. 186–208; the introduction states both the indicator criterion and the square-root character expansion. Reprinted as paper 75 in Frobenius's *Gesammelte Abhandlungen*.
