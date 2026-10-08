# The simple Lie algebras: classical models and the exceptional algebras

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The classification now gives a simple algebra for every connected finite Dynkin diagram. We will identify the classical presentations with matrix algebras, explain the small-rank coincidences by their actual representations, and construct the fourteen-dimensional exceptional algebra directly from octonion multiplication.

The field throughout is \(\mathbb C\). We use [The isomorphism theorem and Serre's theorem](RT-LIE-11.md), together with the explicit root systems and root counts in [Cartan matrices, Dynkin diagrams and the classification of root systems](RT-LIE-09.md). A matrix algebra will be shown to be simple by comparison with a proved Serre presentation; its simplicity will not be assumed merely because its weights resemble roots.

## 1. Classical matrix algebras and their root vectors

For type \(A_n\), take \(V=\mathbb C^{n+1}\) and \(\mathfrak{sl}(V)=\{X:\operatorname{tr}X=0\}\). Its diagonal subalgebra consists of \(\operatorname{diag}(t_1,\ldots,t_{n+1})\) with \(\sum t_i=0\). Write \(\varepsilon_i(H)=t_i\). The off-diagonal matrix \(E_{ij}\) has weight \(\varepsilon_i-\varepsilon_j\), because
\[
[H,E_{ij}]=(t_i-t_j)E_{ij}.
\tag{1.1}
\]
The simple roots are \(\alpha_i=\varepsilon_i-\varepsilon_{i+1}\), with normalized generators
\[
e_i=E_{i,i+1},\quad f_i=E_{i+1,i},\quad
h_i=E_{ii}-E_{i+1,i+1}.
\tag{1.2}
\]

For orthogonal and symplectic algebras, order basis labels as
\[
1,2,\ldots,n,\ -n,\ldots,-2,-1,
\]
inserting a label \(0\) between \(n\) and \(-n\) in odd orthogonal dimension. Matrix subscripts below refer to these labels. In the orthogonal case put \(B(v_i,v_{-j})=\delta_{ij}\), \(B(v_{-j},v_i)=\delta_{ij}\), and in odd dimension also \(B(v_0,v_0)=1\). Other pairings are zero. Thus the form matrix has ones on its anti-diagonal. In the symplectic case put
\(B(v_i,v_{-j})=\delta_{ij}\), \(B(v_{-j},v_i)=-\delta_{ij}\), with other pairings zero. Its matrix is anti-diagonal, with opposite signs on the two halves.

In either case the form algebra is
\[
\mathfrak g_B=\{X:B(Xv,w)+B(v,Xw)=0\}.
\tag{1.3}
\]
Substituting \(XY-YX\) proves that (1.3) is closed under commutators. Put
\[
H_i=E_{ii}-E_{-i,-i},\qquad
H(t)=\sum_i t_iH_i,\qquad\varepsilon_i(H(t))=t_i.
\tag{1.4}
\]
These \(H_i\) lie in the form algebra and commute. Substitution into (1.3) gives the following complete list of nonzero weight lines; a root vector and its displayed opposite are in the same row.

| Algebra | Root | Root vector | Opposite vector |
|---|---|---|---|
| Orthogonal or symplectic | \(\varepsilon_i-\varepsilon_j\), \(i\ne j\) | \(E_{ij}-E_{-j,-i}\) | \(E_{ji}-E_{-i,-j}\) |
| Orthogonal | \(\varepsilon_i+\varepsilon_j\), \(i<j\) | \(E_{i,-j}-E_{j,-i}\) | \(E_{-j,i}-E_{-i,j}\) |
| Odd orthogonal | \(\varepsilon_i\) | \(E_{i0}-E_{0,-i}\) | \(E_{0i}-E_{-i,0}\) |
| Symplectic | \(\varepsilon_i+\varepsilon_j\), \(i<j\) | \(E_{i,-j}+E_{j,-i}\) | \(E_{-j,i}+E_{-i,j}\) |
| Symplectic | \(2\varepsilon_i\) | \(E_{i,-i}\) | \(E_{-i,i}\) |

For clarity, the first row includes both signs already; the other rows are supplemented by their opposite weights. Here is why this is a complete decomposition, rather than only a list of eigenvectors. The equation (1.3) pairs an entry \(X_{ab}\) with \(X_{-b,-a}\), with the form's indicated sign. In the orthogonal case it forces entries \(X_{i,-i}\) to vanish, and pairs the entries involving \(0\). In the symplectic case it allows those entries \(X_{i,-i}\) independently. The diagonal entries in either case satisfy \(X_{-i,-i}=-X_{ii}\); the odd orthogonal middle entry is zero. These conditions give exactly the lines in the table and the span of the \(H_i\). Their disjoint matrix positions prove independence, and (1.1) gives each stated weight.

For \(B_n,C_n,D_n\), the simple roots and Cartan generators are
\[
\begin{array}{c|c|c}
\text{type}&\text{simple roots}&\text{simple coroot elements}\\\hline
B_n&\varepsilon_i-\varepsilon_{i+1}\ (i<n),\ \varepsilon_n
&H_i-H_{i+1}\ (i<n),\ 2H_n\\
C_n&\varepsilon_i-\varepsilon_{i+1}\ (i<n),\ 2\varepsilon_n
&H_i-H_{i+1}\ (i<n),\ H_n\\
D_n&\varepsilon_i-\varepsilon_{i+1}\ (i<n),\ \varepsilon_{n-1}+\varepsilon_n
&H_i-H_{i+1}\ (i<n),\ H_{n-1}+H_n.
\end{array}
\tag{1.5}
\]
For the chain generators use the first row of the matrix table. For the last generator of \(D_n\) use the orthogonal sum row, and for \(C_n\) use the long-root row. Their brackets with the displayed opposite vectors give exactly (1.5). For the last generator of \(B_n\), take
\[
e_n=E_{n0}-E_{0,-n},\qquad
f_n=2(E_{0n}-E_{-n,0}),\qquad h_n=2H_n.
\tag{1.6}
\]
Indeed the unscaled opposite bracket is \(H_n\), and \(\varepsilon_n(H_n)=1\); the factor two is required for \([h_n,e_n]=2e_n\).

**Theorem 1.1 (classical models).** In the classification ranges, the algebras
\[
\mathfrak{sl}_{n+1},\quad\mathfrak{so}_{2n+1},\quad
\mathfrak{sp}_{2n},\quad\mathfrak{so}_{2n}
\]
are simple of types \(A_n\) for \(n\ge1\), \(B_n\) for \(n\ge2\), \(C_n\) for \(n\ge3\), and \(D_n\) for \(n\ge4\), respectively. The displayed diagonal algebras are Cartan subalgebras.

**Proof.** The matrix-unit commutator proves \([e_i,f_i]=h_i\) with the choices above. All other Cartan actions have the coefficients \(a_{ji}=\alpha_j(h_i)\) from (1.5), following the column-coroot convention. For \(i\ne j\), the weight \(\alpha_i-\alpha_j\) is neither zero nor in the complete root list, so \([e_i,f_j]=0\). The Cartan elements commute.

The positive Serre word has weight \(\alpha_j+(1-a_{ji})\alpha_i\). The abstract root-string property says that this lies just beyond the root-string endpoint, since \(\alpha_j-\alpha_i\) is not a root. It is not in the table. Thus this word vanishes. The same reasoning for negative weights proves the negative Serre relations. No Lie-algebra structure theorem is used in this endpoint check: the root lists are the finite Euclidean root systems already verified in the classification lesson, and the matrix weight spaces have just been computed directly.

We obtain a nonzero homomorphism from the finite-type Serre algebra onto its image in each matrix algebra. The source is simple because its diagram is connected, so the map is injective. Counting the complete matrix decomposition gives precisely \(n+|\Phi|\), the dimension of the source. Hence the map is also surjective. This proves simplicity, the indicated root type, and generation by the matrices above. The diagonal algebra has zero-weight centralizer equal to itself. Its normalizer is also itself: any nonzero root component of a normalizing vector is excluded by bracketing with a diagonal element on which its root is nonzero. The diagonal algebra is abelian, hence nilpotent and self-normalizing, which proves the Cartan assertion. \(\square\)

The same argument identifies \(\mathfrak{so}_3\), \(\mathfrak{sp}_2\) and \(\mathfrak{sp}_4\) with their connected small-rank presentations. The reducible \(D_2\) case will be handled explicitly next.

## 2. The low-rank isomorphisms as actual maps

**Proposition 2.1.** There are isomorphisms
\[
\mathfrak{sl}_2\cong\mathfrak{so}_3\cong\mathfrak{sp}_2,
\qquad\mathfrak{so}_4\cong\mathfrak{sl}_2\oplus\mathfrak{sl}_2,
\qquad\mathfrak{sp}_4\cong\mathfrak{so}_5,
\qquad\mathfrak{sl}_4\cong\mathfrak{so}_6.
\tag{2.1}
\]

**Proof: dimension three and the split dimension six.** For a two-dimensional alternating form, (1.3) is exactly the condition
\(X=\left(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\right)\).
Thus \(\mathfrak{sp}_2=\mathfrak{sl}_2\). The adjoint representation of \(\mathfrak{sl}_2\) preserves its nondegenerate symmetric Killing form, by invariance of that form. Its kernel is the centre, which is zero. It therefore injects into the three-dimensional orthogonal form algebra on the three-dimensional vector space \(\mathfrak{sl}_2\), and dimension makes it an isomorphism. Every nondegenerate complex symmetric form is congruent to the anti-diagonal form, by the elementary form-normalization argument in the first lesson.

For \(\mathfrak{so}_4\), the roots are \(\pm(\varepsilon_1-\varepsilon_2)\) and \(\pm(\varepsilon_1+\varepsilon_2)\). Take the corresponding opposite matrix vectors from the table. Their brackets are respectively \(H_1-H_2\) and \(H_1+H_2\), and each triple has the \(\mathfrak{sl}_2\) relations. The two triples commute: their Cartan pairings vanish, and cross root sums are absent from the table. Their six vectors are independent and span the whole algebra. This is the asserted direct sum.

**Proof: the exterior square of dimension four.** Let \(V=\mathbb C^4\), fix a nonzero \(\Omega\in\Lambda^4V\), and put \(W=\Lambda^2V\). The equation
\[
\xi\wedge\eta=B_W(\xi,\eta)\Omega
\tag{2.2}
\]
defines a symmetric nondegenerate form on \(W\): two degree-two exterior factors commute, and a basis wedge pairs nontrivially with its complementary wedge. The action
\[
\rho(X)(v\wedge w)=Xv\wedge w+v\wedge Xw
\tag{2.3}
\]
is a Lie representation. On \(\Lambda^4V\), \(X\) acts by \(\operatorname{tr}X\); hence for \(X\in\mathfrak{sl}_4\), differentiating (2.2) gives \(\rho(X)\in\mathfrak{so}(W,B_W)\).

This action is faithful. If \(\rho(X)=0\), choose three distinct indices \(i,j,k\). The coefficient of \(v_k\wedge v_j\) in \(\rho(X)(v_i\wedge v_j)\) is \(X_{ki}\), up to the ordering sign. Thus every off-diagonal entry vanishes. For a diagonal \(X\), (2.3) then gives \(X_{ii}+X_{jj}=0\) for every pair \(i\ne j\). Taking three distinct indices and using characteristic zero forces each diagonal entry to vanish. Both algebras have dimension fifteen, so (2.3) is an isomorphism.

For an explicit anti-diagonal realization, take \(\Omega=v_1\wedge v_2\wedge v_3\wedge v_4\) and the ordered basis
\[
v_1\wedge v_2,\quad v_1\wedge v_3,\quad v_1\wedge v_4,
\quad v_2\wedge v_3,\quad -v_2\wedge v_4,\quad v_3\wedge v_4.
\tag{2.4}
\]
Its form matrix has ones on the anti-diagonal. For example \(\rho(E_{12})=E_{24}-E_{35}\) in this basis. Formula (2.3) computes the image of every matrix unit and gives the full explicit map.

**Proof: the symplectic exterior-square quotient.** Now give \(V\) a nondegenerate alternating form, with basis \(v_1,v_2,v_{-2},v_{-1}\) as in Section 1. The bivector
\[
\omega=v_1\wedge v_{-1}+v_2\wedge v_{-2}
\tag{2.5}
\]
is fixed by \(\mathfrak{sp}_4\). This follows directly from (1.3): in matrix form it is preservation of the inverse alternating tensor, obtained by multiplying the form equation by its inverse on both sides. All these matrices have trace zero. They consequently preserve the symmetric wedge form (2.2) as well. With \(\Omega=v_1\wedge v_2\wedge v_{-2}\wedge v_{-1}\), one has \(B_W(\omega,\omega)=2\ne0\).

Thus \(W=\mathbb C\omega\oplus\omega^\perp\), and \(\omega^\perp\) has dimension five and a nondegenerate symmetric restricted form. Orthogonal projection identifies it equivariantly with \(\Lambda^2V/\mathbb C\omega\). The form on that quotient means precisely the form transported through this identification; the original wedge form does not descend by simply ignoring \(\omega\).

We get \(\mathfrak{sp}_4\to\mathfrak{so}(\omega^\perp)\). If its image of \(X\) is zero, then \(X\) acts trivially on both \(\omega^\perp\) and \(\omega\), hence on all of \(\Lambda^2V\). The faithfulness just proved gives \(X=0\). Both algebras have dimension ten, so the map is an isomorphism. This proves the third assertion of (2.1). Exercise 7.2 gives a five-vector anti-diagonal basis and the exact quotient form. \(\square\)

## 3. Dimensions and the other exceptional presentations

**Proposition 3.1 (dimension table).** The dimensions of the simple complex Lie algebras are

| Type | Rank | Number of roots | Dimension |
|---|---:|---:|---:|
| \(A_n\) | \(n\) | \(n(n+1)\) | \(n(n+2)\) |
| \(B_n\) | \(n\) | \(2n^2\) | \(n(2n+1)\) |
| \(C_n\) | \(n\) | \(2n^2\) | \(n(2n+1)\) |
| \(D_n\) | \(n\) | \(2n(n-1)\) | \(n(2n-1)\) |
| \(G_2\) | 2 | 12 | 14 |
| \(F_4\) | 4 | 48 | 52 |
| \(E_6\) | 6 | 72 | 78 |
| \(E_7\) | 7 | 126 | 133 |
| \(E_8\) | 8 | 240 | 248 |

**Proof.** The proved root decomposition has a Cartan space of dimension equal to the rank and one dimension for each root. Thus \(\dim\mathfrak g=\operatorname{rank}\Phi+|\Phi|\). The classical lists in Section 1 give their counts directly: ordered differences for \(A_n\), four signed vectors per unordered pair and the extra axial roots for \(B_n,C_n\), and only the signed-pair vectors for \(D_n\). The exceptional counts were proved from their explicit coordinate systems in the classification lesson. Adding the rank gives every displayed entry. \(\square\)

For each of \(F_4,E_6,E_7,E_8\), take the corresponding numbered base and Cartan matrix of that lesson and impose the Serre presentation. This is an explicit construction with four, six, seven or eight normalized generator triples. The preceding theorem on presentations proves that the resulting algebra is simple, has exactly the indicated roots and has the listed dimension. In particular the \(E_8\) construction retains precisely its 240 root lines and eight Cartan directions; it does not require an unproved existence theorem for a separately proposed multiplication table.

For \(G_2\) the same presentation already constructs the algebra. We now identify it with derivations of an eight-dimensional nonassociative algebra, using a full calculation.

## 4. All derivations of the complex octonions

An octonion algebra is an eight-dimensional unital algebra with a nondegenerate multiplicative quadratic norm. We use the following explicit complex model. Let \(V=\mathbb C^3\), choose a volume form with \(\det(v_1,v_2,v_3)=1\), and use the induced cross products
\(V\times V\to V^*\) and \(V^*\times V^*\to V\). Thus \((x\times z)(w)=\det(x,z,w)\), with the analogous formula for the dual volume. In the chosen bases these are the usual epsilon-symbol formulas, interpreted between a space and its dual.

The **Zorn model** is the vector space of symbols
\[
X=\begin{pmatrix}a&u\\v&b\end{pmatrix},
\qquad a,b\in\mathbb C,\quad u\in V,\quad v\in V^*,
\]
with multiplication
\[
\begin{pmatrix}a&u\\v&b\end{pmatrix}
\begin{pmatrix}c&x\\y&d\end{pmatrix}
=\begin{pmatrix}
ac+y(u)&ax+du-v\times y\\
cv+by+u\times x&bd+v(x)
\end{pmatrix}.
\tag{4.1}
\]
This is a bilinear multiplication, rather than ordinary matrix multiplication. The diagonal symbol with both entries one is its unit. Put
\[
N(X)=ab-v(u).
\tag{4.2}
\]
Its polar form is nondegenerate: the two scalar coordinates pair with one another, and \(V\) pairs nondegenerately with \(V^*\). To verify composition, use
\[
(u\times x)(v\times y)=v(u)y(x)-v(x)y(u).
\tag{4.3}
\]
It follows by contracting two epsilon symbols, whose contraction is the difference of the two Kronecker-delta products. Expanding (4.1), all scalar-times-cross terms vanish by alternation, and (4.3) cancels the two remaining crossed pairings. The result is
\[
N(XY)=abcd-ab\,y(x)-cd\,v(u)+v(u)y(x)
=(ab-v(u))(cd-y(x)).
\]
Thus this is an octonion algebra, denoted \(\mathbb O\).

Write \(e_+,e_-\) for the two scalar idempotents, and \(u(x),v(y)\) for the two vector corners. Set \(h=e_+-e_-\). The products needed below are
\[
\begin{aligned}
e_+u(x)&=u(x)=u(x)e_-,&
e_-v(y)&=v(y)=v(y)e_+,\\
u(x)v(y)&=y(x)e_+,&
v(y)u(x)&=y(x)e_-,\\
u(x)u(z)&=v(x\times z),&
v(y)v(t)&=-u(y\times t).
\end{aligned}
\tag{4.4}
\]
The complementary corner products vanish; \(e_\pm^2=e_\pm\) and \(e_+e_-=e_-e_+=0\). These rules also show nonassociativity. For the standard three vector basis elements,
\((u(v_1)u(v_2))u(v_3)=e_-\), while
\(u(v_1)(u(v_2)u(v_3))=e_+\).

**Proposition 4.1 (complete derivation calculation).** Every derivation of \(\mathbb O\) has exactly one expression \(D_{A,p,q}\), where
\(A\in\mathfrak{sl}(V)\), \(p\in V\), \(q\in V^*\), given by
\[
\begin{aligned}
D_{A,p,q}e_+&=u(p)+v(q),&D_{A,p,q}e_-&=-u(p)-v(q),\\
D_{A,p,q}u(x)&=-q(x)h+u(Ax)+v(p\times x),\\
D_{A,p,q}v(y)&=-y(p)h+u(q\times y)-v(A^ty).
\end{aligned}
\tag{4.5}
\]
In particular \(\dim\operatorname{Der}(\mathbb O)=8+3+3=14\).

**Proof: necessity.** A derivation kills the unit, by applying its rule to \(1^2\). Applying it to \(e_+^2=e_+\) forces both scalar components of \(D e_+\) to be zero, so \(D e_+=u(p)+v(q)\) for unique \(p,q\), and \(D e_-=-D e_+\).

Write the four components of \(D u(x)\) temporarily as scalar linear forms and vector linear maps. Applying the derivation rule to \(e_+u(x)=u(x)\) forces its \(e_-\) component to be \(q(x)\), its \(V^*\) component to be \(p\times x\), and leaves its \(V\) component \(Ax\). Applying the rule to \(u(x)e_-=u(x)\) forces its \(e_+\) component to be \(-q(x)\). Similarly the two corner identities for \(v(y)\) force
\[
D v(y)=-y(p)h+u(q\times y)+v(By)
\]
for some \(B\in\operatorname{End}(V^*)\).

Now apply the rule to \(u(x)v(y)=y(x)e_+\). Its scalar component is \(y(Ax)+(By)(x)\), whereas the derivative of the right side has no scalar component. Hence \(B=-A^t\). Finally apply it to \(u(x)u(z)=v(x\times z)\). Equality of the \(V^*\) components requires
\[
Ax\times z+x\times Az=-A^t(x\times z).
\tag{4.6}
\]
For every \(A\), the left side equals
\((\operatorname{tr}A)(x\times z)-A^t(x\times z)\).
To prove this identity, differentiate the determinant in all three slots:
\(\det(Ax,z,w)+\det(x,Az,w)+\det(x,z,Aw)=\operatorname{tr}(A)\det(x,z,w)\).
That determinant identity follows by checking matrix units, or by expanding its three indices. Since the \(x\times z\) span \(V^*\), (4.6) forces \(\operatorname{tr}A=0\). This proves every restriction in (4.5).

**Proof: sufficiency.** Conversely take any parameters in (4.5), with trace zero. We verify the rule on all the product families (4.4) and the idempotents; bilinearity then gives it everywhere. The idempotent and corner identities hold by the very component calculations above. For both mixed products the two vector-triple identities
\[
(p\times x)\times y=y(p)x-y(x)p,
\qquad x\times(q\times y)=y(x)q-q(x)y
\tag{4.7}
\]
give respectively
\[
\begin{aligned}
D u(x)\,v(y)+u(x)\,D v(y)&=y(x)(u(p)+v(q)),\\
D v(y)\,u(x)+v(y)\,D u(x)&=-y(x)(u(p)+v(q)).
\end{aligned}
\]
These are the derivatives of \(y(x)e_+\) and \(y(x)e_-\). The scalar terms cancel by \(B=-A^t\). Identities (4.7), like (4.3), follow by the two-epsilon contraction.

For two positive corners, expansion gives
\[
\begin{aligned}
D u(x)\,u(z)+u(x)\,D u(z)
={}&-(x\times z)(p)h+u(q\times(x\times z))\\
&+v(Ax\times z+x\times Az).
\end{aligned}
\]
The trace-zero determinant identity (4.6) makes this exactly \(D v(x\times z)\). For two negative corners the analogous expansion is
\[
\begin{aligned}
D v(y)\,v(t)+v(y)\,D v(t)
={}&q(y\times t)h-v(p\times(y\times t))\\
&+u(A^ty\times t+y\times A^tt).
\end{aligned}
\]
Applying the determinant identity on the dual space makes its last term \(-u(A(y\times t))\), so the expression is \(-D u(y\times t)\), as required. Complementary zero corner products follow by subtracting the checked identities from multiplication by \(1=e_++e_-\). This checks every product. Thus every (4.5) is a derivation. Its parameters are detected by its value on \(e_+\) and its \(V\) component on \(u(V)\), so they are unique. The trace-zero matrices have dimension eight, proving the dimension assertion. \(\square\)

**Proposition 4.2 (the exceptional algebra \(G_2\)).** The Lie algebra \(\operatorname{Der}(\mathbb O)\) is simple of type \(G_2\).

**Proof.** Derivations of any algebra with bilinear multiplication form a Lie algebra under commutators, by the product-rule calculation in the first lesson. Denote the three parts of (4.5) by
\[
K_A=D_{A,0,0},\qquad P_p=D_{0,p,0},\qquad Q_q=D_{0,0,q}.
\]
Evaluation on (4.4) gives
\[
\begin{aligned}[c]
[K_A,K_C]&=K_{[A,C]},&[K_A,P_p]&=P_{Ap},&[K_A,Q_q]&=Q_{-A^tq},\\
[P_p,Q_q]&=K_{q(p)I-3p\otimes q},\\
[P_p,P_r]&=2Q_{p\times r},&[Q_q,Q_t]&=2P_{q\times t}.
\end{aligned}
\tag{4.8}
\]
For example the mixed commutator kills \(e_+\), and on \(u(x)\) its vector component is \(u(q(p)x-3q(x)p)\). The cross-product determinant identities give the other evaluations, exactly as in the sufficiency check. The matrix in that mixed bracket has trace zero.

Take the Cartan candidates \(K_A\) for diagonal \(A=\operatorname{diag}(a_1,a_2,a_3)\), \(\sum a_i=0\), and put \(\varepsilon_i(A)=a_i\). Formula (4.8) gives six one-dimensional weights \(\varepsilon_i-\varepsilon_j\) on off-diagonal matrices, three weights \(\varepsilon_i\) on the \(P\)'s, and three weights \(-\varepsilon_i\) on the \(Q\)'s. The zero-weight space is exactly the two-dimensional diagonal span. It is abelian and self-normalizing by the same root-component argument as in Theorem 1.1, so it is Cartan.

We prove simplicity directly. A nonzero ideal splits into its weight components by polynomial projections. If it has only a nonzero diagonal component, bracketing with some off-diagonal \(K_{E_{ij}}\) produces a nonzero root component: a trace-zero diagonal with all differences zero would be zero. If a root component is in the \(K\)-part, the ideal meets the simple algebra \(K\cong\mathfrak{sl}_3\) and thus contains all of \(K\). If instead it contains a \(P\)-component, the elementary matrices in \(K\) move that vector to all of \(P\); similarly a \(Q\)-component gives all of \(Q\). The mixed bracket in (4.8) then supplies a nonzero element of \(K\): for nonzero \(p,q\), the rank-one matrix \(3p\otimes q\) cannot equal \(q(p)I\). Once \(K\) is in the ideal, its actions on \(P\) and \(Q\) put both in the ideal. Thus every nonzero ideal is the whole algebra.

Finally \(\varepsilon_1+\varepsilon_2+\varepsilon_3=0\). Give their real span the form \((\varepsilon_i,\varepsilon_j)=\delta_{ij}-1/3\). The six difference roots have squared length two; the six \(\pm\varepsilon_i\) have squared length \(2/3\). The base
\[
\alpha_1=\varepsilon_2,\qquad\alpha_2=\varepsilon_1-\varepsilon_2
\]
has column-coroot Cartan matrix \(\left(\begin{smallmatrix}2&-1\\-3&2\end{smallmatrix}\right)\). Its positive roots are \(\alpha_1,\alpha_2,\alpha_1+\alpha_2,2\alpha_1+\alpha_2,3\alpha_1+\alpha_2,3\alpha_1+2\alpha_2\), exactly the weights listed above. The normalized triples (4.9), computed from (4.8), verify these coroot pairings directly: \(\alpha_1(h_1)=2\), \(\alpha_2(h_1)=-3\), \(\alpha_1(h_2)=-1\), and \(\alpha_2(h_2)=2\). Thus the coordinate form gives the actual root datum. This is the proved \(G_2\) root system, with vertex 1 short. The isomorphism theorem therefore identifies \(\operatorname{Der}(\mathbb O)\) with the simple \(G_2\) algebra. \(\square\)

The model even gives normalized generators without an unspecified sign choice:
\[
\begin{aligned}
e_1&=P_{v_2},&f_1&=-Q_{v_2^*},&h_1&=K_{\operatorname{diag}(-1,2,-1)},\\
e_2&=K_{E_{12}},&f_2&=K_{E_{21}},&h_2&=K_{\operatorname{diag}(1,-1,0)}.
\end{aligned}
\tag{4.9}
\]
In the short string, the successive brackets of \(e_2\) with \(e_1\) are
\(-P_{v_1}\), \(2Q_{v_3^*}\), \(-6K_{E_{23}}\), and zero. Bracketing the last nonzero vector with \(e_2\) gives \(-6K_{E_{13}}\), the highest-root line. These constants connect the octonion product to the fourth-power Serre relation explicitly.

## 5. The integral basis theorem and its simultaneous signs

The root-labelled adjoint construction is due to Lusztig; see Meinolf Geck, [*On the construction of semisimple Lie algebras and Chevalley groups*](https://arxiv.org/abs/1602.04583v5), and Meinolf Geck and Alexander Lang, [*Canonical structure constants for simple Lie algebras*](https://arxiv.org/abs/2404.07652v1). We give the construction, module identification and simultaneous normalization here, including the opposite-root signs used in the compact-form lesson.

**Theorem 5.1 (integral root basis).** Let \(\mathfrak g\) be finite-dimensional complex semisimple, \(\mathfrak h\) a Cartan subalgebra, \(\Delta=\{\alpha_i\}\) a base, and \(h_i=\alpha_i^\vee\) its simple coroots. We prove that nonzero \(x_\alpha\in\mathfrak g_\alpha\) can be chosen simultaneously with
\[
[x_\alpha,x_{-\alpha}]=h_\alpha,\qquad
[h_i,x_\alpha]=\alpha(h_i)x_\alpha,\qquad
[x_\alpha,x_\beta]=N_{\alpha,\beta}x_{\alpha+\beta},
\]
the last formula concerning root sums, and
\[
N_{\alpha,\beta}=\pm(p+1),\qquad
p=\max\{j\ge0:\beta-j\alpha\in\Phi\}.
\]
Every \(h_\alpha\) is an integral combination of the \(h_i\). We also obtain
\[
N_{-\alpha,-\beta}=-N_{\alpha,\beta}. \tag{5.14}
\]
Absent nonopposite root sums have zero bracket. These include all the normalizations required in 17.

**Proof.** We prove the result on each simple ideal independently. Roots from different ideals have zero brackets, so their bases then combine. Fix one irreducible component. For \(\gamma\ne\pm\alpha_i\), write
\[
r_i(\gamma)=\max\{k\ge0:\gamma-k\alpha_i\in\Phi\},\qquad
q_i(\gamma)=\max\{k\ge0:\gamma+k\alpha_i\in\Phi\}.
\]
The string identity is \(\gamma(h_i)=r_i(\gamma)-q_i(\gamma)\). The target's \(p\) is our \(r\), and is denoted \(q\) in the research papers.

### 5.2. Construct and verify a finite module

Let \(V\) have formal basis \(\{z_i\}\cup\{v_\gamma:\gamma\in\Phi\}\). Define
\[
\begin{aligned}
H_i z_j&=0,&H_i v_\gamma&=\gamma(h_i)v_\gamma,\\
E_i z_j&=|\alpha_i(h_j)|v_{\alpha_i},&
F_i z_j&=|\alpha_i(h_j)|v_{-\alpha_i},\\
E_i v_{-\alpha_i}&=z_i,& F_i v_{\alpha_i}&=z_i,
\end{aligned} \tag{5.3}
\]
and, for other roots,
\[
E_i v_\gamma=
\begin{cases}(r_i(\gamma)+1)v_{\gamma+\alpha_i}&\gamma+\alpha_i\in\Phi,\\0&\text{otherwise},\end{cases}
\quad
F_i v_\gamma=
\begin{cases}(q_i(\gamma)+1)v_{\gamma-\alpha_i}&\gamma-\alpha_i\in\Phi,\\0&\text{otherwise}.\end{cases} \tag{5.4}
\]
Here \(E_i v_{\alpha_i}=F_i v_{-\alpha_i}=0\); no string length is assigned to a proportional root.

The \(H_i\) commute. The weight shifts, including the exceptional maps to zero weight, give
\[
[H_j,E_i]=\alpha_i(h_j)E_i,\qquad
[H_j,F_i]=-\alpha_i(h_j)F_i. \tag{5.5}
\]
On a nonproportional string ordered as
\(\eta,\eta+\alpha_i,\ldots,\eta+d\alpha_i\), the \(k\)-th vector has raising coefficient \(k+1\) and lowering coefficient \(d-k+1\). Thus its commutator coefficient is
\[
k(d-k+1)-(k+1)(d-k)=2k-d=(\eta+k\alpha_i)(h_i).
\]
At the endpoints the missing action is zero. On \(v_{\alpha_i},v_{-\alpha_i}\) the commutator is respectively \(2v_{\alpha_i},-2v_{-\alpha_i}\). On \(z_j\) both compositions are \(|\alpha_i(h_j)|z_i\). Therefore
\[
[E_i,F_i]=H_i. \tag{5.6}
\]
The remaining identity is
\[
[E_i,F_j]=0\quad(i\ne j). \tag{5.7}
\]
[Section 5.8](#5-8-the-exhaustive-mixed-generator-calculation) supplies its complete finite calculation and the proof that the calculation covers arbitrary rank. Rank-two checks alone would not suffice.

Both \(E_i,F_i\) are nilpotent: the finite weight set bounds root-shifting chains, with the only passage through zero being \(v_{-\alpha_i},z_i,v_{\alpha_i}\). Their adjoint operators on \(\operatorname{End}(V)\) are nilpotent, as follows by expanding
\[
(\operatorname{ad}E_i)^m A=\sum_{k=0}^m(-1)^k\binom mk E_i^{m-k}AE_i^k.
\]
Equations (5.5)–(5.6) give a rank-one Lie algebra. For \(j\ne i\), its vector \(E_j\) in the finite-dimensional module \(\operatorname{End}(V)\) has weight \(a=\alpha_j(h_i)\le0\) and is annihilated by \(\operatorname{ad}F_i\), by (5.7). Complete reducibility and the rank-one classification make its components lowest vectors in simple modules of highest weight \(-a\). Hence
\[
(\operatorname{ad}E_i)^{1-\alpha_j(h_i)}E_j=0.
\]
Exchanging \(E_i,F_i\) and negating \(H_i\) proves the negative relation. The \(H_i\) are independent because their values on the \(v_{\alpha_j}\) give the invertible Cartan matrix.

All Serre relations are verified, with the course's column-coroot convention. The Serre algebra \(\mathfrak s\) from 11 therefore maps to \(\operatorname{End}(V)\), sending its generators to \(E_i,F_i,H_i\). It is simple, and the map is nonzero, so the map is injective. This gives an actual module for the already constructed simple algebra without assuming any Chevalley basis.

### 5.3. Reflections and simplicity of the module

Set \(R_i=\exp(E_i)\exp(-F_i)\exp(E_i)\). On the string in [§5.2](#5-2-construct-and-verify-a-finite-module) identify
\[
v_{\eta+k\alpha_i}\longleftrightarrow\binom dk X^kY^{d-k}.
\]
The two operators become \(X\partial_Y,Y\partial_X\). Their three substitutions send \(X\) to \(-Y\) and \(Y\) to \(X\), yielding
\[
R_i v_\gamma=(-1)^{r_i(\gamma)}v_{s_i\gamma}
\quad(\gamma\ne\pm\alpha_i). \tag{5.8}
\]
The three-dimensional zero chain gives
\[
R_i v_{\alpha_i}=v_{-\alpha_i},\quad
R_i v_{-\alpha_i}=v_{\alpha_i},\quad
R_i z_j=z_j-|\alpha_i(h_j)|z_i. \tag{5.9}
\]
For the last equality, the vector \(z_j-\tfrac12|\alpha_i(h_j)|z_i\) is killed by both operators and hence fixed, while \(R_i z_i=-z_i\).

Choose alternating signs \(\epsilon_i=\pm1\) on the Dynkin tree. With \(D=\operatorname{diag}(\epsilon_i)\), the absolute Cartan matrix \(C=(|\alpha_i(h_j)|)\) is \(DAD\), and is invertible.

Let \(U\ne0\) be a submodule. Polynomial projections in the commuting \(H_i\) separate each root weight and the zero-weight space. If initially \(U\) has only a nonzero zero-weight vector \(\sum c_jz_j\), invertibility of \(C\) gives an \(i\) whose \(E_i\)-image is a nonzero root vector. Thus \(U\) contains some \(v_\gamma\).

The \(R_i\) and their inverses preserve \(U\). Every root is Weyl-conjugate to a simple root, so (5.8)–(5.9) put some \(v_{\pm\alpha_i}\) in \(U\), then \(z_i\) and both opposite vectors. For every adjacent \(j\), the vector \(E_jz_i=|\alpha_j(h_i)|v_{\alpha_j}\) is nonzero. Connectedness supplies all simple roots and all \(z_j\), and reflection then supplies every root. Hence \(U=V\).

### 5.4. Identify the adjoint module

The needed highest-weight uniqueness fact has a short proof. Form the universal cyclic highest-weight module of weight \(\lambda\), quotienting \(U(\mathfrak s)\) by the left ideal generated by the positive generators and \(h-\lambda(h)\). Ordered enveloping words span: use \(xy=yx+[x,y]\), inducting first on length and then inversions. Order negative-root letters before Cartan letters before positive-root letters. After applying to the cyclic generator, the module is spanned by negative-root words.

These words have weights \(\lambda-\sum_{\alpha>0}n_\alpha\alpha\); only the empty word has weight \(\lambda\). Whenever a nonzero highest-weight module exists, the generator and its top weight survive in the universal module. Any proper submodule has zero component in that one-dimensional top space, since containing the generator would give the whole module. Weight projections are polynomial on each finite set of components, so this assertion also holds for nonhomogeneous elements. The sum of all proper submodules still has zero top component and is proper. It is the unique maximal proper submodule. Thus simple highest-weight modules of weight \(\lambda\) are isomorphic. Only ordered-word spanning was needed, not PBW independence.

Let \(\vartheta\) be the highest root established in 09. The module \(V\) is simple and \(v_\vartheta\) is a highest vector. The adjoint module of the simple algebra \(\mathfrak s\) is simple and its \(\vartheta\)-root vector is highest. Therefore there is an isomorphism
\(\phi:V\to\mathfrak s_{\mathrm{ad}}\).

Since root spaces are one-dimensional, write \(\phi(v_{\alpha_i})=c_i e_i\), \(c_i\ne0\). Intertwining \(F_i\) and \(E_i\) gives
\[
\phi(z_i)=-c_i h_i,\qquad \phi(v_{-\alpha_i})=-c_i f_i.
\]
For adjacent \(i,j\), intertwining \(E_i z_j\) gives
\(|\alpha_i(h_j)|c_i=c_j\alpha_i(h_j)\), so \(c_i=-c_j\). Rescale by a common scalar so \(c_i=\epsilon_i\), and put \(b_\gamma=\phi(v_\gamma)\). We have simultaneously
\[
\begin{aligned}
b_{\alpha_i}&=\epsilon_i e_i,&b_{-\alpha_i}&=-\epsilon_i f_i,\\
[e_i,b_\gamma]&=(r_i(\gamma)+1)b_{\gamma+\alpha_i},&
[f_i,b_\gamma]&=(q_i(\gamma)+1)b_{\gamma-\alpha_i}.
\end{aligned} \tag{5.10}
\]
The last two formulas concern root sums; the exceptional opposite-simple cases were handled separately.

### 5.5. All structure-constant magnitudes

Let \(T_i=\exp(\operatorname{ad}e_i)\exp(-\operatorname{ad}f_i)\exp(\operatorname{ad}e_i)\). The exponentials are finite. The derivation binomial rule proves bracket preservation, and negated exponents give inverses. Intertwining gives \(\phi R_i=T_i\phi\), so \(T_i\) permutes the \(b_\gamma\) up to signs.

On \(\mathfrak h\), \(T_i h=h-\alpha_i(h)h_i\): the vector \(h-\tfrac12\alpha_i(h)h_i\) commutes with both simple generators and is fixed, whereas the rank-one calculation sends \(h_i\) to \(-h_i\). Thus \(T_i h_\gamma=h_{s_i\gamma}\).

Given \(\alpha,\beta,\alpha+\beta\in\Phi\), choose \(w\) with \(w^{-1}\alpha=\alpha_i\), and lift it to a product of the \(T_j\). All three relevant root vectors are carried to signed root vectors. The magnitude of their bracket coefficient is therefore that of
\([b_{\alpha_i},b_{w^{-1}\beta}]\), which by (5.10) is \(r_i(w^{-1}\beta)+1\). Weyl transport bijects its string with the \(\alpha\)-string through \(\beta\). Consequently
\[
[b_\alpha,b_\beta]=\pm(p+1)b_{\alpha+\beta}. \tag{5.11}
\]
This proves real integral constants for every root sum simultaneously.

### 5.6. Opposite brackets and the compact-form signs

The Serre presentation gives the involution
\(\omega(e_i)=f_i,\ \omega(f_i)=e_i,\ \omega(h_i)=-h_i\).
We prove \(\omega(b_\gamma)=-b_{-\gamma}\). It holds on simple roots. For a nonsimple positive root choose \(\beta=\gamma-\alpha_i\in\Phi^+\). Apply \(\omega\) to (5.10) and induct:
\[
(r_i(\beta)+1)\omega(b_\gamma)
=-[f_i,b_{-\beta}]
=-(q_i(-\beta)+1)b_{-\gamma}.
\]
Negation identifies the two lengths. Negative roots follow from \(\omega^2=1\).

The opposite brackets in this intermediate basis are
\[
[b_\gamma,b_{-\gamma}]=(-1)^{\operatorname{ht}(\gamma)}h_\gamma. \tag{5.12}
\]
For a simple root this is \([\epsilon_i e_i,-\epsilon_i f_i]=-h_i\). For a nonsimple positive \(\gamma=\sum c_i\alpha_i\), choose \(i\) with \(m=\gamma(h_i)>0\), possible because
\((\gamma,\gamma)=\sum c_i(\gamma,\alpha_i)>0\).
Then \(s_i\gamma\) is positive with smaller height. Reflection changes only its \(i\)-th simple coefficient; another coefficient is still positive, so the same-sign property of root expansions forces positivity.

The product of the signs in (5.8) for \(\gamma\) and \(-\gamma\) is
\((-1)^{r_i(\gamma)+q_i(\gamma)}=(-1)^m\).
Apply \(T_i\) to their bracket and induct at \(s_i\gamma\). Its coefficient is
\((-1)^{m+\operatorname{ht}(s_i\gamma)}=(-1)^{\operatorname{ht}(\gamma)}\).
This proves (5.12); alternation and \(h_{-\gamma}=-h_\gamma\) give the negative case.

Now correct only the negative vectors:
\[
x_\gamma=b_\gamma,\qquad
x_{-\gamma}=(-1)^{\operatorname{ht}(\gamma)}b_{-\gamma}
\quad(\gamma>0). \tag{5.13}
\]
Then (5.12) gives the desired opposite normalization. Since (5.13) rescales only by signs, (5.11) retains its magnitudes and integral coefficients.

Let \(\delta\) be the grading automorphism multiplying a root degree \(\gamma\) by \((-1)^{\operatorname{ht}(\gamma)}\) and fixing the Cartan algebra. On the Serre presentation it simply negates all \(e_i,f_i\) and fixes all \(h_i\); every relation is homogeneous. The automorphism \(\theta=\delta\omega\) satisfies
\[
\theta(x_\gamma)=-x_{-\gamma},\qquad \theta(h_i)=-h_i
\]
for positive and negative roots alike. Applying it to the root-sum bracket gives
\[
-N_{\alpha,\beta}x_{-\alpha-\beta}
=[x_{-\alpha},x_{-\beta}],
\]
which proves (5.14). Thus the construction also supplies precisely the sign condition used by 17.

### 5.7. Coroot integrality and transport

Every root is a Weyl translate of a simple root, and the Euclidean identification defining coroots is Weyl-equivariant. Hence \(h_\gamma=w h_i\) for some \(i,w\). Every simple reflection sends
\[
h_j\longmapsto h_j-\alpha_i(h_j)h_i.
\]
Its coefficients are integers, so every reflection word preserves the simple-coroot lattice. Every \(h_\gamma\) is therefore integral in the \(h_i\).

Cartan brackets vanish; their actions on root vectors have integral Cartan coefficients; opposite brackets have integral coroot coordinates; root sums have (5.11); absent sums are zero by the root decomposition. The entire multiplication table is integral, so the integer span is a Lie algebra over \(\mathbb Z\).

The isomorphism theorem in 11 identifies the constructed Serre algebra with the requested simple algebra, carrying its normalized generators and Cartan data to the requested ones. Transport the basis. Applying the argument component by component proves the target for every complex semisimple algebra.

### 5.8. The exhaustive mixed-generator calculation

For \(i\ne j\), both \(E_iF_jz_k\) and \(F_jE_iz_k\) vanish because distinct simple-root differences are not roots. On \(v_{\alpha_j}\) both sides are \(|\alpha_i(h_j)|v_{\alpha_i}\), and on \(v_{-\alpha_i}\) both are \(|\alpha_j(h_i)|v_{-\alpha_j}\). On \(v_{\alpha_i}\) and \(v_{-\alpha_j}\) both are zero.

For other \(v_\gamma\), use (5.4) to compute each path's coefficient, taking a missing intermediate or final root as a zero contribution. All membership and string-length data lie in
\[
W=\mathbb R\gamma+\mathbb R\alpha_i+\mathbb R\alpha_j,\qquad\Psi=\Phi\cap W.
\]
The set \(\Psi\) is a reduced crystallographic root system of rank at most three. Positivity is inherited from \(\Phi\). Both \(\alpha_i,\alpha_j\) remain simple: a positive decomposition in \(\Psi\) would also decompose them in \(\Phi\). Thus they belong to the base of \(\Psi\). Restriction preserves every string in their directions. Intermediate zero terms \(z_i,z_j\) obey the same formulas. By the classification proved in 09, all possible data are covered by the following based systems:

| System | Roots | Model dimension | Ordered mixed-pair/basis cases |
|---|---:|---:|---:|
| \(A_1\) | 2 | 3 | 0 |
| \(A_1+A_1\) | 4 | 6 | 12 |
| \(A_2\) | 6 | 8 | 16 |
| \(B_2\) | 8 | 10 | 20 |
| \(G_2\) | 12 | 14 | 28 |
| \(A_1+A_1+A_1\) | 6 | 9 | 54 |
| \(A_2+A_1\) | 8 | 11 | 66 |
| \(B_2+A_1\) | 10 | 13 | 78 |
| \(G_2+A_1\) | 14 | 17 | 102 |
| \(A_3\) | 12 | 15 | 90 |
| \(B_3\) | 18 | 21 | 126 |
| \(C_3\) | 18 | 21 | 126 |

The [complete exact-arithmetic certificate](proofs/chevalley_rank3_check.py) specifies every root, Gram matrix, matrix action and comparison. Its [calculation record](proofs/chevalley_rank3_check.json) reports zero residual in all 718 cases. The certificate is included below as well, so the finite step can be reproduced directly from this lesson. It uses exact rational arithmetic, and does not suppress any ordered pair or basis vector.

For direct reproduction the positive root lists, followed by their Gram matrices, are
\[
\begin{array}{c|l|l}
A_1&(1)&(2)\\
A_2&(1,0),(0,1),(1,1)&\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\\
B_2&(1,0),(0,1),(1,1),(1,2)&\left(\begin{smallmatrix}2&-1\\-1&1\end{smallmatrix}\right)\\
G_2&(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)&\left(\begin{smallmatrix}2&-3\\-3&6\end{smallmatrix}\right).
\end{array}
\]
For \(A_3\) use all consecutive interval sums of its three simple roots, with diagonal Gram entries 2 and adjacent entries \(-1\). For \(B_3\) use \(\pm e_k,\pm e_k\pm e_l\), where \(e_1=(1,1,1),e_2=(0,1,1),e_3=(0,0,1)\), and
\[
G_B=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}.
\]
For \(C_3\) use \(\pm2e_k,\pm e_k\pm e_l\), where \(e_1=(1,1,\tfrac12),e_2=(0,1,\tfrac12),e_3=(0,0,\tfrac12)\), and
\[
G_C=\begin{pmatrix}2&-1&0\\-1&2&-2\\0&-2&4\end{pmatrix}.
\]
Add the negatives to every positive list. Products use block-diagonal Gram matrices and the union of roots in the separate coordinate blocks. These are the finite coordinate models from 09 in simple coordinates.

The script also verifies the Cartan relations, same-index commutators, Serre relations, reflection signs and integral coroot coordinates. Those additional checks are consistency checks; the proof above already establishes their general versions.

This is a finite computational proof of (5.7), together with a proof of its exhaustive reduction, followed by the general algebraic argument in [§§5.3–5.7](#5-3-reflections-and-simplicity-of-the-module). It is not a sample of selected large diagrams. The listed coordinate systems, action formulas and the following certificate cover every required case.

### 5.9. Complete calculation certificate

```python
"""Exact finite certificate for the mixed-generator lemma in the draft.

Independent root lists and matrix calculation, using Fraction only.
This checks every based root system of rank at most three, including products.
The draft explains why that finite set covers the lemma in arbitrary rank.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial
from pathlib import Path
import json, hashlib

def negate(v): return tuple(-x for x in v)
def add(v,w): return tuple(x+y for x,y in zip(v,w))
def scale(c,v): return tuple(c*x for x in v)
def dot(v,w,G): return sum(v[i]*G[i][j]*w[j] for i in range(len(v)) for j in range(len(v)))
def signed(positive): return sorted(set(positive)|{negate(v) for v in positive})
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def zero(n): return [[F(0) for _ in range(n)] for _ in range(n)]
def mul(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def minus(A,B): return [[x-y for x,y in zip(row,col)] for row,col in zip(A,B)]
def times(c,A): return [[c*x for x in row] for row in A]
def plus(A,B): return [[x+y for x,y in zip(row,col)] for row,col in zip(A,B)]
def comm(A,B): return minus(mul(A,B),mul(B,A))
def norm(A): return max((abs(x) for row in A for x in row),default=F(0))
def exp_nil(A):
    n=len(A); result=eye(n); power=eye(n)
    for k in range(1,n+1):
        power=mul(power,A)
        if not norm(power): return result
        result=plus(result,times(F(1,factorial(k)),power))
    raise AssertionError("operator not nilpotent")

def direct(left,right):
    R,G=left; S,H=right; a=len(G); b=len(H)
    roots=[tuple(r)+(0,)*b for r in R]+[(0,)*a+tuple(s) for s in S]
    gram=[list(row)+[0]*b for row in G]+[[0]*a+list(row) for row in H]
    return sorted(roots),gram

A1=(signed([(1,)]),[[2]])
A2=(signed([(1,0),(0,1),(1,1)]),[[2,-1],[-1,2]])
B2=(signed([(1,0),(0,1),(1,1),(1,2)]),[[2,-1],[-1,1]])
G2=(signed([(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)]),[[2,-3],[-3,6]])
A3=(signed([tuple(int(i<=k<=j) for k in range(3)) for i in range(3) for j in range(i,3)]),[[2,-1,0],[-1,2,-1],[0,-1,2]])
def classical(kind):
    e=[tuple(F(int(k>=i),2 if k==2 and kind=='C' else 1) for k in range(3)) for i in range(3)]
    roots=[]
    for v in e: roots += [scale(1 if kind=='B' else 2,v),scale(-1 if kind=='B' else -2,v)]
    for i,j in combinations(range(3),2):
        for s,t in product([-1,1],repeat=2): roots.append(add(scale(s,e[i]),scale(t,e[j])))
    assert all(x.denominator==1 for v in roots for x in v)
    gram=[[2,-1,0],[-1,2,-1],[0,-1,1]] if kind=='B' else [[2,-1,0],[-1,2,-2],[0,-2,4]]
    return sorted(set(tuple(int(x) for x in v) for v in roots)),gram
systems={'A1':A1,'A1+A1':direct(A1,A1),'A2':A2,'B2':B2,'G2':G2,
 'A1+A1+A1':direct(direct(A1,A1),A1),'A2+A1':direct(A2,A1),
 'B2+A1':direct(B2,A1),'G2+A1':direct(G2,A1),
 'A3':A3,'B3':classical('B'),'C3':classical('C')}

results=[]
for name,(roots,G) in systems.items():
    rank=len(G); rootset=set(roots); count=rank+len(roots)
    simple=[tuple(int(i==j) for j in range(rank)) for i in range(rank)]
    ix={root:rank+k for k,root in enumerate(roots)}
    def cartan(a,i): return F(2)*dot(a,simple[i],G)/G[i][i]
    def length(a,i,direction):
        k=0
        while add(a,scale(direction*(k+1),simple[i])) in rootset: k+=1
        return k
    E=[]; D=[]; H=[]
    for i in range(rank):
        e=zero(count); f=zero(count); h=zero(count)
        for j in range(rank):
            c=abs(cartan(simple[i],j)); e[ix[simple[i]]][j]=c; f[ix[negate(simple[i])]][j]=c
        for a in roots:
            col=ix[a]; h[col][col]=cartan(a,i)
            if a==negate(simple[i]): e[i][col]=1
            elif add(a,simple[i]) in rootset: e[ix[add(a,simple[i])]][col]=length(a,i,-1)+1
            if a==simple[i]: f[i][col]=1
            elif add(a,negate(simple[i])) in rootset: f[ix[add(a,negate(simple[i]))]][col]=length(a,i,1)+1
        E.append(e);D.append(f);H.append(h)
    residuals=[]; serre_residuals=[]; reflection_residuals=[]
    for i in range(rank):
        residuals.append(norm(minus(comm(E[i],D[i]),H[i])))
        for j in range(rank):
            residuals += [norm(comm(H[i],H[j])),norm(minus(comm(H[i],E[j]),times(cartan(simple[j],i),E[j]))),norm(plus(comm(H[i],D[j]),times(cartan(simple[j],i),D[j])))]
            if i!=j:
                residuals.append(norm(comm(E[i],D[j])))
                n=1-int(cartan(simple[j],i)); X=E[j];Y=D[j]
                for _ in range(n): X=comm(E[i],X);Y=comm(D[i],Y)
                serre_residuals += [norm(X),norm(Y)]
        N=mul(mul(exp_nil(E[i]),exp_nil(times(-1,D[i]))),exp_nil(E[i]))
        expected=zero(count)
        for j in range(rank):
            expected[j][j]=1;expected[i][j]-=abs(cartan(simple[i],j))
        for a in roots:
            reflected=add(a,scale(-cartan(a,i),simple[i]))
            sign=1 if a in [simple[i],negate(simple[i])] else (-1)**length(a,i,-1)
            expected[ix[reflected]][ix[a]]=sign
        reflection_residuals.append(norm(minus(N,expected)))
    coroot_coordinates=[tuple(F(a[i]*G[i][i],dot(a,a,G)) for i in range(rank)) for a in roots]
    assert all(c.denominator==1 for v in coroot_coordinates for c in v)
    assert not max(residuals+serre_residuals+reflection_residuals,default=0),name
    results.append({'type':name,'rank':rank,'roots':len(roots),'module_dimension':count,
        'mixed_commutator_basis_cases':rank*(rank-1)*count,'max_generator_residual':str(max(residuals,default=0)),
        'max_Serre_residual':str(max(serre_residuals,default=0)),'max_reflection_residual':str(max(reflection_residuals,default=0)),
        'all_coroot_coordinates_integral':True})

out={'arithmetic':'exact fractions; no floating point','systems':results,
     'mixed_commutator_basis_cases':sum(x['mixed_commutator_basis_cases'] for x in results),
     'all_checks_pass':True,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
```

Tensoring the resulting integral lattice with a field transports its bracket and Jacobi identity. This alone does not preserve simplicity: in characteristic \(p\), the nonzero identity matrix belongs to \(\mathfrak{sl}_p\) and is central. Positive-characteristic classification requires its own hypotheses and arguments.

## 6. A normalized dimension identity for eight algebras

Deligne's exceptional series is
\[
A_1,\quad A_2,\quad G_2,\quad D_4,\quad F_4,\quad E_6,\quad E_7,\quad E_8.
\tag{6.1}
\]
In particular it includes \(D_4\), in addition to the five types conventionally called exceptional. The numerical parameter is tied to the actual Killing form, rather than to a freely rescaled Euclidean picture. Let \(\theta\) be the highest root and let \(\varphi\) be the inverse of the restricted Killing form on the Cartan algebra. Put
\[
k=\varphi(\theta,\theta),\qquad a=k,\qquad\lambda=-6a.
\tag{6.2}
\]
We choose this positive branch. Deligne also allows \(a^*=-1/6-k\), whose parameter is \(\lambda^*=1-\lambda\).

The normalization can be computed directly from root weights. If \(t_\theta\) is the Killing-dual vector of \(\theta\), then \(k=\theta(t_\theta)\) and \(h_\theta=2t_\theta/k\). Consequently
\[
\kappa(h_\theta,h_\theta)=\frac4k
=\sum_{\beta\in\Phi}\beta(h_\theta)^2,
\qquad
k=\frac4{\sum_{\beta\in\Phi}\langle\beta,\theta^\vee\rangle^2}.
\tag{6.3}
\]
The sum is the trace of the diagonal Cartan adjoint action squared; its zero weights contribute zero. Thus (6.3) uses the intrinsic Killing normalization and is independent of a common coordinate scale.

For the eight types (6.1), the identity to check is
\[
\dim\mathfrak g
=F(\lambda):=-\frac{2(\lambda+5)(\lambda-6)}{\lambda(\lambda-1)}.
\tag{6.4}
\]
Here are its complete numerical data.

| Type | \(\sum_\beta\langle\beta,\theta^\vee\rangle^2\) | \(a=k\) | \(\lambda=-6a\) | \(F(\lambda)\) |
|---|---:|---:|---:|---:|
| \(A_1\) | 8 | \(1/2\) | \(-3\) | 3 |
| \(A_2\) | 12 | \(1/3\) | \(-2\) | 8 |
| \(G_2\) | 16 | \(1/4\) | \(-3/2\) | 14 |
| \(D_4\) | 24 | \(1/6\) | \(-1\) | 28 |
| \(F_4\) | 36 | \(1/9\) | \(-2/3\) | 52 |
| \(E_6\) | 48 | \(1/12\) | \(-1/2\) | 78 |
| \(E_7\) | 72 | \(1/18\) | \(-1/3\) | 133 |
| \(E_8\) | 120 | \(1/30\) | \(-1/5\) | 248 |

Here is the root count behind those trace sums. In every list, the pair \(\theta,-\theta\) has values \(2,-2\), contributing eight. All other nonzero values are \(1,-1\). In the order (6.1), the numbers of roots with value \(1\) are \(0,2,4,8,14,20,32,56\); the counts at \(-1\) are the same. These numbers come directly from the signed-coordinate lists: fixing a highest root, its scalar product with each signed-pair or half-sign root determines the pairing in (6.3). For the \(E\) types the highest roots have the coefficients given in the classification lesson. Thus the sums are respectively \(8+2m\) for the eight displayed counts \(m\), which yields the second column without an assumed dual Coxeter number; Exercise 7.3 checks all eight rational substitutions in (6.4). Direct replacement also gives \(F(1-\lambda)=F(\lambda)\), so the second branch has the same dimensions.

This is the finite-series numerology of Deligne, *La série exceptionnelle de groupes de Lie*, p. 321 for the parameter and p. 323, (E), for \(\dim X_1=\dim\mathfrak g\). We do not assert a dimension theorem for every simple algebra or the conjectural categorical interpretation of the paper. For a concrete boundary, \(A_3\) has highest-root trace sum sixteen and hence \(k=1/4\), but its dimension is fifteen, whereas \(F(-3/2)=14\). Membership in the list (6.1) matters.

## 7. Exercises with complete solutions

### Exercise 7.1 — count the dimensions from the roots (easy)

Recover every entry of Proposition 3.1 by counting the indicated roots and adding the rank.

**Solution.** For \(A_n\), \(n+1\) coordinates give \((n+1)n\) ordered differences. Adding \(n\) gives \(n(n+2)\). In each of \(B_n,C_n\), four choices of signs for an unordered pair give \(4\binom n2=2n(n-1)\) roots, and the axial list gives another \(2n\). Thus both have \(2n^2+n=n(2n+1)\) dimensions. For \(D_n\) there are only the signed-pair roots, giving \(2n(n-1)+n=n(2n-1)\).

The \(G_2\) list has six positive roots and their six negatives. For \(F_4\), the axis vectors contribute eight, the signed-pair vectors contribute \(4\binom42=24\), and the half-sign vectors contribute \(2^4=16\). Its total is 48. The coordinate \(E_6\) model has \(4\binom52=40\) signed-pair vectors and 32 half-sign vectors, giving 72. The \(E_7\) model has \(4\binom62=60\), the two opposite axial roots in its last two coordinates, and 64 half-sign vectors, giving 126. Finally \(E_8\) has \(4\binom82=112\) signed-pair vectors and \(2^7=128\) half-sign vectors of even parity, giving 240. Adding ranks \(2,4,6,7,8\) yields \(14,52,78,133,248\). These counts use the complete coordinate models in the classification lesson, including the two axial \(E_7\) roots.

### Exercise 7.2 — the five-dimensional symplectic representation (medium)

Construct \(\mathfrak{sp}_4\cong\mathfrak{so}_5\) through \(\Lambda^2\mathbb C^4/\mathbb C\omega\). Give the quotient its correct symmetric form and an explicit anti-diagonal basis.

**Solution.** Use the basis and volume preceding (2.5), and the form \(B_W\) defined by wedge multiplication. Since \(B_W(\omega,\omega)=2\), define on classes
\[
\overline B([\xi],[\eta])
=B_W(\xi,\eta)-\frac{B_W(\xi,\omega)B_W(\eta,\omega)}2.
\tag{7.1}
\]
Adding a multiple of \(\omega\) to either representative cancels out of this formula, so it is well defined. It is the nondegenerate restricted form on \(\omega^\perp\), transported by the projection \(\xi\mapsto\xi-\tfrac12B_W(\xi,\omega)\omega\).

Here is an ordered basis of \(\omega^\perp\), hence of the quotient:
\[
\begin{gathered}
v_1\wedge v_2,\qquad v_1\wedge v_{-2},\qquad
\frac{v_1\wedge v_{-1}-v_2\wedge v_{-2}}{i\sqrt2},\\
-v_2\wedge v_{-1},\qquad v_{-2}\wedge v_{-1}.
\end{gathered}
\tag{7.2}
\]
The first pairs with the last with value one, and the second with the fourth with value one. The middle numerator has square \(-2\), so its indicated multiple has square one. All other pairings vanish. Thus the matrix is anti-diagonal with ones. Each vector is orthogonal to \(\omega\), and their disjoint wedge coefficients prove independence.

Every \(X\in\mathfrak{sp}_4\) kills \(\omega\) and preserves both the volume form and \(B_W\), so it acts on (7.2) by an orthogonal matrix. Formula (2.3) gives its entries. If its five-dimensional action is zero, its action on \(\Lambda^2V\) is zero because that space is \(\omega^\perp\oplus\mathbb C\omega\). The elementary off-diagonal/diagonal coefficient argument in Proposition 2.1 then gives \(X=0\). The faithful map between two ten-dimensional algebras is onto, proving the isomorphism.

### Exercise 7.3 — all eight dimension substitutions (medium)

Evaluate (6.4) at the eight parameters of (6.2). Check the second branch as well.

**Solution.** Substituting the eight values of \(\lambda\), the numerator \(-2(\lambda+5)(\lambda-6)\) and denominator \(\lambda(\lambda-1)\) are respectively
\[
\begin{array}{c|r|r|r}
\lambda&\text{numerator}&\text{denominator}&\text{quotient}\\\hline
-3&36&12&3\\
-2&48&6&8\\
-3/2&105/2&15/4&14\\
-1&56&2&28\\
-2/3&520/9&10/9&52\\
-1/2&117/2&3/4&78\\
-1/3&532/9&4/9&133\\
-1/5&1488/25&6/25&248.
\end{array}
\]
Every denominator is nonzero. The outputs agree with Proposition 3.1, including \(D_4\). Under the alternate branch, \(a^*=-1/6-a\) and \(\lambda^*=1-\lambda\). Both numerator and denominator in \(F(1-\lambda)\) simplify to those of \(F(\lambda)\), proving equality of the rational functions wherever defined. In particular the second branch produces the same eight dimensions. Replacing the Killing form by an arbitrary scalar would change \(k\), so is not an allowed change of normalization for this check.

### Exercise 7.4 — fourteen parameters, with no uncounted derivations (hard)

Prove that \(\operatorname{Der}(\mathbb O)\) has dimension fourteen by solving the derivation conditions in the eight-dimensional model (4.4).

**Solution.** Start with a completely arbitrary linear map \(D\); do not assume it is generated by a previously chosen set of derivations. The unit equation gives \(D e_-=-D e_+\). The idempotent equation gives \(D e_+=u(p)+v(q)\), with six free scalar coordinates. The equations for \(e_+u(x)\) and \(u(x)e_-\) then force
\(D u(x)=-q(x)h+u(Ax)+v(p\times x)\).
The corresponding two equations on \(v(y)\) force
\(D v(y)=-y(p)h+u(q\times y)+v(By)\).
At this stage the two unknown matrix parts cannot be counted as independent parameters.

The derivative of \(u(x)v(y)=y(x)e_+\) requires
\(y(Ax)+(By)(x)=0\) for every \(x,y\), so \(B=-A^t\). The derivative of \(u(x)u(z)=v(x\times z)\) requires (4.6). The determinant identity shows that its only remaining matrix condition is \(\operatorname{tr}A=0\). Thus every derivation belongs to a space with at most \(6+(9-1)=14\) parameters.

For the reverse inequality, every trace-zero \(A\), \(p\) and \(q\) gives the actual derivation (4.5): the explicit mixed-product, two-positive-corner and two-negative-corner computations in the sufficiency part of Proposition 4.1 check every product family. None of these fourteen parameters are lost, since \(D e_+\) detects \(p,q\), and the vector component of \(D u(x)\) detects \(A\). Taking the six off-diagonal matrices and two independent trace-zero diagonals for \(A\), together with three basis choices each for \(p,q\), gives fourteen independent derivations. The upper and lower bounds agree.

## 8. What this lesson does not prove, and references

The classical models, their simplicity and roots, all low-rank isomorphisms, the dimension table, the complete octonion derivation space and its simplicity have been proved. The constructions of \(F_4,E_6,E_7,E_8\) use the previously proved finite-type Serre theorem. Section 5 proves Chevalley's simultaneous integral-basis theorem, including the compatible signs and integral structure constants. Section 6 proves the normalization formula (6.3) and checks only the eight dimension values. Deligne's other representation identities and conjectural categorical interpretation are outside this lesson.

The compact octonion interpretation belongs to the planned lesson *Compact G₂ and dimension formulas*. Here the algebra, vectors, duals and derivations are complex. No classification of real division algebras, real forms or positive-characteristic simple algebras is being used as an unproved step.

The [official Stacks project](https://stacks.math.columbia.edu/) is the reference project in the wider algebraic-geometry programme. The [AI Integrated Stacks Project reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) contains unofficial AI drafts, which are not maintainer-reviewed Stacks results. This lesson's new Lie-algebra models are established by the proofs here.

**References.**

- J. S. Milne, [*Algebraic Groups*](https://www.jmilne.org/math/Books/iAG2022.pdf), 2021 revision, §§21j and 24l for classical and exceptional group analogues; §23h, Theorem 23.71 for the integral structure constants. Group classification over general fields is additional structure beyond the complex Lie-algebra models proved here.
- P. Deligne, *La série exceptionnelle de groupes de Lie*, *C. R. Acad. Sci. Paris*, Série I 322 (1996), 321–326: p. 321 for \(k\) and the two branches of \(a\), and p. 323, (E), for the adjoint dimension formula. [Freely accessible IAS PDF](https://publications.ias.edu/sites/default/files/75_LaSerie.pdf).
- A. Premet and H. Strade, [*Classification of finite dimensional simple Lie algebras in prime characteristics*](https://arxiv.org/abs/math/0601380), §3, for the distinct characteristic-\(p\) families and their structural context.
