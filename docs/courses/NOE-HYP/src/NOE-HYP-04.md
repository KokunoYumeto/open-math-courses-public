# Central simple algebras and the Brauer group

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A matrix algebra can conceal a division algebra. Extending the scalar field sometimes removes that division algebra, while changing the size of the matrices never does. The Brauer group records precisely the obstruction that survives changes of matrix size. To construct it, we first need to control tensor products, embeddings and the elements that commute with an embedded algebra.

The prerequisite is [Semisimple rings and Wedderburn's theorem](NOE-HYP-02.md). We use its classification of simple Artinian rings and their modules. Field extensions and finite fields have their usual meanings from [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40). Every algebra in this lesson is associative, finite-dimensional and unital; homomorphisms preserve the identity. The ground field \(k\) has arbitrary characteristic until the quaternion examples, where characteristic different from \(2\) is stated explicitly. References are [Noether], [Voight], [MIT], [Milne CFT] and [Stacks].

## 1. Tensor products and scalar extension

A nonzero algebra \(A\) is **simple** if its only two-sided ideals are \(0\) and \(A\). It is **central over \(k\)** if \(Z(A)=k1\), and **central simple** if both conditions hold. Thus \(M_r(k)\) is central simple, while \(\mathbb C\) is simple but not central as an \(\mathbb R\)-algebra. Wedderburn's theorem gives

\[
A\simeq M_r(D),
\]

where \(D\) is a finite-dimensional division algebra with centre \(k\). Indeed, the centre of a matrix ring consists of scalar matrices with entries in \(Z(D)\). The division algebra \(D\) is determined up to \(k\)-algebra isomorphism.

For a field extension \(F/k\), write \(A_F=A\otimes_k F\). Multiplication in a tensor product is \((a\otimes b)(a'\otimes b')=aa'\otimes bb'\). The **opposite algebra** \(A^{\mathrm{op}}\) has the same underlying vector space as \(A\), with \(a^{\mathrm{op}}b^{\mathrm{op}}=(ba)^{\mathrm{op}}\).

**Theorem 1.1 (extension and tensor products).** If \(A\) is central simple over \(k\) and \(B\) is a simple \(k\)-algebra, then \(A\otimes_k B\) is simple and its centre is \(1\otimes Z(B)\). In particular, \(A_F\) is central simple over every field extension \(F/k\), and the tensor product of two central simple \(k\)-algebras is central simple.

**Proof.** The same argument works when \(B=F\) is an infinite extension. Let \(I\) be a nonzero two-sided ideal of \(A\otimes_k B\). Choose a nonzero element of \(I\) with the least possible tensor length:

\[
x=\sum_{i=1}^{t}a_i\otimes b_i,
\]

where the \(b_i\) are linearly independent and \(a_1\ne0\). Simplicity of \(A\) says \(Aa_1A=A\), so there are finitely many \(u_j,v_j\in A\) with \(\sum_j u_ja_1v_j=1\). The element

\[
y=\sum_j(u_j\otimes1)x(v_j\otimes1)
 =1\otimes b_1+\sum_{i=2}^{t}c_i\otimes b_i
\]

lies in \(I\) and is nonzero. For \(a\in A\), the commutator \([a\otimes1,y]\) is a sum of at most \(t-1\) elementary tensors. Minimality forces it to vanish. Independence of the \(b_i\) therefore puts every \(c_i\) in \(Z(A)=k\). Consequently \(y=1\otimes b\) for a nonzero \(b\in B\). Simplicity of \(B\) gives \(\sum_j s_jbt_j=1\), and multiplication on the two sides now puts \(1\otimes1\) in \(I\). Thus \(I=A\otimes_k B\).

If \(z=\sum_i a_i\otimes b_i\) is central, choose the \(b_i\) independent. Commutation with every \(a\otimes1\) forces \(a_i\in k\), so \(z=1\otimes b\). Commutation with \(1\otimes B\) then forces \(b\in Z(B)\). Conversely these elements are central. Taking \(B=F\), or taking \(B\) central simple, proves the last assertions. \(\square\)

**Corollary 1.2 (left and right multiplication).** There is a \(k\)-algebra isomorphism

\[
A\otimes_k A^{\mathrm{op}}\xrightarrow{\sim}\operatorname{End}_k(A),
\qquad a\otimes b^{\mathrm{op}}\longmapsto(x\mapsto axb).
\]

**Proof.** Composition gives \(a(a'xb')b=aa'x(b'b)\), exactly the multiplication prescribed by the opposite factor. The map is unital, and its domain is simple by Theorem 1.1; its kernel is therefore zero. Domain and codomain both have dimension \((\dim_k A)^2\), so it is surjective. \(\square\)

Over an algebraic closure \(\overline k\), every finite-dimensional division algebra is \(\overline k\). To see this, an element has a polynomial relation over \(\overline k\); factor that polynomial into linear factors. Their product evaluated at the element is zero, and a division ring has no zero divisors, so one factor is zero. Every element is thus scalar. Applying Wedderburn to \(A_{\overline k}\) gives

\[
A_{\overline k}\simeq M_n(\overline k),\qquad \dim_k A=n^2.
\]

The integer \(n\) is the **degree** \(\deg A\). If \(A=M_r(D)\) and \(\deg D=d\), then \(\deg A=rd\). The integer \(d\) is the **index** \(\operatorname{ind} A\). A field extension \(F/k\) **splits** \(A\) if \(A_F\simeq M_n(F)\).

The finite-dimensional hypotheses matter for the degree and index. The tensor-length argument itself also explains why extending scalars preserves simplicity without any separability hypothesis. See [Stacks, Tags 074F–074H and 074N] for the corresponding tensor, extension and dimension results.

## 2. Embeddings are conjugate

**Theorem 2.1 (Skolem–Noether).** Let \(B\) be a simple \(k\)-algebra and \(A\) a central simple \(k\)-algebra. Any two \(k\)-algebra maps \(f,g:B\to A\) satisfy

\[
g(b)=u f(b)u^{-1}\quad(b\in B)
\]

for some \(u\in A^\times\). In particular, every \(k\)-algebra automorphism of \(A\) is inner.

**Proof.** First, \(F=Z(B)\) is a field. For \(0\ne z\in Z(B)\), the nonzero ideal \(zB\) equals \(B\), so \(z\) has an inverse, which is again central. The algebra \(B\) is central simple over \(F\). Moreover

\[
R=B\otimes_k A^{\mathrm{op}}
 \simeq B\otimes_F (F\otimes_k A^{\mathrm{op}})
\]

is simple by Theorem 1.1 over \(F\). This step allows \(F\) to be larger than \(k\).

Give the vector space \(A\) two left \(R\)-module structures:

\[
(b\otimes a^{\mathrm{op}})\cdot_f x=f(b)xa,
\qquad
(b\otimes a^{\mathrm{op}})\cdot_g x=g(b)xa.
\]

The simple Artinian algebra \(R\) has one simple module type \(S\), and every finite module is a sum of copies of \(S\). The two modules just constructed have the same \(k\)-dimension, so their multiplicities of \(S\) agree. There is an \(R\)-module isomorphism \(T:A_f\to A_g\). It commutes with all right multiplications. Hence \(T(x)=T(1)x=ux\). Its inverse also commutes with right multiplication, and is left multiplication by some \(v\); therefore \(uv=vu=1\). Finally \(T(f(b)x)=g(b)T(x)\), evaluated at \(x=1\), gives \(uf(b)=g(b)u\). Take \(B=A\), \(f\) the identity and \(g\) an automorphism for the last assertion. \(\square\)

Conjugation by two units has the same effect precisely when their quotient is central. Thus

\[
\operatorname{Aut}_k(A)\simeq A^\times/k^\times,
\qquad
\operatorname{Aut}_k(M_n(k))\simeq\operatorname{PGL}_n(k).
\]

The simplicity assumption on \(B\) cannot be dropped. In \(M_3(k)\), two unital embeddings of \(k\times k\) can send \((1,0)\) respectively to idempotents of ranks \(1\) and \(2\). Conjugation preserves rank, so these maps are not conjugate. The theorem is [Stacks, Tag 074Q], with the automorphism consequence [Tag 074R].

## 3. The algebra that commutes with a subalgebra

For a subalgebra \(B\subseteq A\), set

\[
C_A(B)=\{x\in A:xb=bx\text{ for every }b\in B\}.
\]

It is a unital subalgebra. Its dimension measures how much of \(A\) remains after imposing commutation with \(B\).

**Theorem 3.1 (double centralizer).** If \(A\) is central simple and \(B\subseteq A\) is simple, then \(C=C_A(B)\) is simple,

\[
C_A(C)=B,\qquad
\dim_k B\,\dim_k C=\dim_k A,\qquad
Z(C)=Z(B).
\]

If \(B\) is central over \(k\), so is \(C\), and multiplication induces an isomorphism \(B\otimes_k C\simeq A\).

**Proof.** Put \(R=B\otimes_k A^{\mathrm{op}}\), acting on \(A\) by \((b\otimes a^{\mathrm{op}})x=bxa\). It is simple by the argument in Theorem 2.1. Write \(R=M_r(E)\), where \(E\) is a division algebra, and write \(A\simeq S^m\) as an \(R\)-module, with \(S=E^r\). An \(R\)-linear endomorphism of \(A\) commutes with right multiplication, so it is left multiplication by \(c=T(1)\). It also commutes with left multiplication by \(B\) exactly when \(c\in C\). Consequently

\[
C\simeq\operatorname{End}_R(A)\simeq M_m(E^{\mathrm{op}}),
\]

which proves simplicity. Put \(e=\dim_k E\). Dimensions give

\[
\dim_k R=r^2e=(\dim_k B)(\dim_k A),\quad
\dim_k A=rme,\quad \dim_k C=m^2e.
\]

Substituting the middle equality into the first yields \(\dim_k B=r/m\); multiplying this by \(m^2e\) gives \(\dim_k A\). Thus the dimension formula is proved.

There is always an inclusion \(B\subseteq C_A(C)\). Since \(C\) is now known to be simple, apply the dimension formula again, with \(C\) in place of \(B\). It gives

\[
\dim_k C_A(C)=\frac{\dim_k A}{\dim_k C}=\dim_k B.
\]

The inclusion is therefore equality. It follows that

\[
Z(C)=C\cap C_A(C)=C\cap B=Z(B).
\]

If \(Z(B)=k\), both \(B\) and \(C\) are central simple. Their elements commute, so multiplication defines a unital map \(B\otimes_k C\to A\). Its domain is simple by Theorem 1.1, so it is injective, and the dimension formula makes it surjective. \(\square\)

This proof requires neither a separable centre nor an algebraically closed field. In particular, if a subfield \(L\subseteq A\) has degree \(s=[L:k]\), then \(C_A(L)\) is central simple over \(L\), and

\[
\dim_L C_A(L)=\frac{(\deg A)^2}{s^2}.
\]

Its degree over \(L\) is an integer, so \(s\) divides \(\deg A\): a rational number whose square is an integer is an integer. The reference for the theorem is [Stacks, Tag 074T], and for the tensor decomposition [Tag 074U].

For example, in \(A=M_r(k)\otimes_k M_s(k)\), the centralizer of \(M_r(k)\otimes1\) is \(1\otimes M_s(k)\). This can also be checked with matrix units: commuting with all \(E_{ij}\otimes1\) forces the first matrix coordinate to be scalar. The dimension equality reads \(r^2s^2=(rs)^2\).

## 4. Maximal subfields and splitting fields

A **maximal subfield** of a division algebra \(D\) is a commutative subfield containing \(k\) which is not properly contained in another such subfield of \(D\). There is one: enlarge any subfield as long as its dimension increases, which can happen only finitely many times.

**Theorem 4.1 (maximal subfields).** Let \(D\) be central division of degree \(d\). Every maximal subfield \(L\subseteq D\) satisfies

\[
C_D(L)=L,\qquad [L:k]=d,\qquad D\otimes_k L\simeq M_d(L).
\]

**Proof.** If \(x\) commutes with \(L\), then \(L[x]\) is a finite-dimensional commutative domain, hence a field. Maximality forces \(x\in L\). Apply Theorem 3.1 to get \([L:k]^2=\dim_k D=d^2\), giving \([L:k]=d\). Regard \(D\) as a right \(L\)-vector space of dimension \(d\). The map

\[
D\otimes_k L\longrightarrow\operatorname{End}_L(D),
\qquad a\otimes \ell\longmapsto(x\mapsto ax\ell)
\]

is well defined and multiplicative because \(L\) is commutative. Its simple domain makes it injective, and both sides have \(L\)-dimension \(d^2\). Hence it is an isomorphism. \(\square\)

For matrix algebras, a maximal *subfield* need not be self-centralizing. If \(k\) is algebraically closed, the only subfield of \(M_n(k)\) containing \(k\) is \(k\), but its centralizer is the entire algebra. The splitting criterion must use a maximal **commutative subalgebra**, rather than just maximality among fields.

Call two central simple algebras **Brauer equivalent**, or **similar**, if their division algebras in Wedderburn's classification are isomorphic. We will make these classes into a group in the next section.

**Theorem 4.2 (finite splitting criterion).** Let \(A=M_r(D)\) be central simple, with \(d=\deg D\), and let \(L/k\) be a finite extension of degree \(s\). The following are equivalent:

1. \(L\) splits \(A\).
2. \(L\) splits \(D\).
3. \(L\) embeds into an algebra \(A'\) similar to \(A\) with \(\deg A'=s\).
4. \(L\) embeds as a maximal commutative subalgebra into an algebra similar to \(A\).

Under condition 3 the embedded \(L\) is self-centralizing. Every finite splitting extension satisfies \(d\mid s\).

**Proof.** Write \(D_L=M_t(E)\) by Wedderburn. Then \(A_L=M_{rt}(E)\). Uniqueness of the division algebra shows that one is split exactly when \(E=L\), proving \(1\Leftrightarrow2\).

Suppose 2 holds. The opposite algebra \(D^{\mathrm{op}}_L\) also splits. Its simple left module \(V=L^d\) is a right \(D\)-vector space, with the left scalar action of \(L\) commuting with the right \(D\)-action. Comparing \(k\)-dimensions gives

\[
m=\dim_D V=\frac{sd}{d^2}=\frac{s}{d}\in\mathbb Z.
\]

Left multiplication by \(L\) is a unital embedding into \(A'=\operatorname{End}_D(V)\simeq M_m(D)\). This algebra is similar to \(A\), and has degree \(md=s\). By Theorem 3.1 its centralizer of \(L\) has \(k\)-dimension \(s^2/s=s\); since it contains \(L\), it equals \(L\). This proves 3 and 4 and the divisibility assertion.

Conversely, suppose \(L\subseteq A'\) and \(\deg A'=s\). Then \(A'\) has right \(L\)-dimension \(s\). The left–right multiplication map

\[
A'\otimes_k L\longrightarrow\operatorname{End}_L(A')
\]

is injective by simplicity and is an isomorphism by \(L\)-dimension \(s^2\). Thus \(L\) splits \(A'\), and uniqueness of the division representative proves 2.

Finally, if \(L\) is maximal commutative in \(A'\), every \(x\in C_{A'}(L)\) generates a commutative subalgebra \(L[x]\), so maximality forces \(x\in L\). Theorem 3.1 now gives \(\dim_k A'=s^2\), reducing 4 to 3. The same observation shows why self-centralizing and maximal commutative are equivalent here. \(\square\)

The statements above permit inseparable maximal subfields. Nevertheless separable ones always exist.

**Theorem 4.3 (separable maximal subfields).** Every finite-dimensional central division algebra over \(k\) has a maximal subfield separable over \(k\). Consequently every central simple algebra has a finite separable splitting field, and therefore a finite Galois splitting field.

**Proof.** We first show that if a central division algebra \(D\) is larger than its centre \(k\), it contains an element outside \(k\) separable over \(k\). In characteristic zero this is automatic. If \(k\) is finite, every \(k[x]\) is a finite field, so its elements are separable; this also proves the assertion.

Suppose now that \(k\) is infinite of characteristic \(p>0\), and that no element outside \(k\) is separable over \(k\). For \(x\in D\), its irreducible minimal polynomial is \(h(T^{p^e})\) with \(h\) separable. Thus \(x^{p^e}\) is separable over \(k\) and belongs to \(k\) by the assumption. The minimal polynomial must then be \(T^{p^e}-a\). Its degree is at most \(\dim_k D\). Choose one power \(q=p^N\) at least that dimension. Every \(x\in D\) satisfies \(x^q\in k\).

Choose a \(k\)-basis of \(D\) beginning with \(1\). Multiplication has structure constants in \(k\), so every coordinate of \(x^q\) is a polynomial in the coordinates of \(x\). All coordinates except the first vanish at every point of \(k^{\dim_k D}\). A polynomial over an infinite field which vanishes at all such points is zero: induct on the number of variables using the one-variable root bound. The same coordinates therefore vanish after extending to \(\overline k\). In \(D_{\overline k}\simeq M_d(\overline k)\), every \(q\)-th power would be scalar. For \(d>1\), the matrix \(E_{11}\) is not scalar and satisfies \(E_{11}^q=E_{11}\), a contradiction.

Start with the separable subfield \(L=k\) of \(D\). Theorem 3.1 makes \(C_D(L)\) a division algebra central over \(L\). If it is larger than \(L\), the preceding argument produces an element \(x\) in it, outside \(L\), separable over \(L\). Then \(L[x]\) is a larger subfield, separable over \(k\). Repeat. Strictly increasing \(k\)-dimensions force the process to end, at a separable field whose centralizer is itself; it is maximal. Theorem 4.1 splits \(D\), hence \(A=M_r(D)\). A normal closure of the finite separable field is finite Galois and still splits \(A\). \(\square\)

This is the division-algebra argument behind [Stacks, Tag 0752]; the maximal-subfield and splitting-degree statements are [Tags 074Z–0751]. It does not say that a Galois splitting field must embed into the given division algebra. The next lesson studies the algebras which do contain a Galois maximal subfield.

## 5. Brauer classes and three basic fields

Similarity also has a definition avoiding a chosen division representative:

\[
A\sim B
\quad\Longleftrightarrow\quad
M_u(A)\simeq M_v(B)\text{ for some }u,v\ge1.
\]

Indeed, if \(A=M_r(D)\), \(B=M_s(D)\), then \(M_s(A)\simeq M_r(B)\). Conversely, an isomorphism of matrix enlargements forces their division representatives to be isomorphic by Wedderburn uniqueness.

**Theorem 5.1 (Brauer group).** Similarity classes of central simple \(k\)-algebras form an abelian group \(\operatorname{Br}(k)\), with

\[
[A]+[B]=[A\otimes_k B],\qquad
0=[k],\qquad -[A]=[A^{\mathrm{op}}].
\]

**Proof.** Matrix units give

\[
M_u(A)\otimes_k M_v(B)\simeq M_{uv}(A\otimes_k B).
\]

Thus tensor product respects similarity in each variable. Theorem 1.1 ensures the result is central simple. Associativity and the interchange map \(a\otimes b\mapsto b\otimes a\) give an associative commutative operation on classes. The algebra \(k\) is its identity. Corollary 1.2 shows

\[
A\otimes_k A^{\mathrm{op}}\simeq M_{\dim_k A}(k),
\]

whose class is \([k]\), proving the inverse formula. \(\square\)

Scalar extension respects these operations, so every extension \(F/k\) induces a group homomorphism \(\operatorname{Br}(k)\to\operatorname{Br}(F)\), called restriction. Its kernel is the **relative Brauer group** \(\operatorname{Br}(F/k)\). The zero class consists precisely of split algebras. Noether's “reciprocally isomorphic” algebra in [Noether, §7] is the opposite algebra in this notation.

If \(k\) is algebraically closed, the division-algebra argument in section 1 gives \(\operatorname{Br}(k)=0\). For finite fields the corresponding conclusion has a short proof using the theorems already established.

**Proposition 5.2 (finite fields).** Every finite division ring is commutative. In particular, \(\operatorname{Br}(\mathbb F_q)=0\).

**Proof.** Let \(D\) be finite, with centre \(k=\mathbb F_q\), and let \(L\) be a maximal subfield. Put \(d=\deg D\). Theorem 4.1 gives \(|L|=q^d\). For \(x\in D\), the subfield \(k[x]\) has degree \(e\) dividing \(d\), by the subfield consequence of Theorem 3.1. The finite-field theorem gives a \(k\)-embedding \(k[x]\to L\). Skolem–Noether compares it with the original inclusion into \(D\); hence \(x\) is conjugate to an element of \(L\).

It remains to use a finite-group fact. If every element of a finite group \(G\) is conjugate to an element of \(H\le G\), then \(H=G\). Let \(G\) act on the left cosets \(G/H\). The conjugacy hypothesis says each \(g\) fixes at least one coset. The average number of fixed cosets equals the number of orbits, which is \(1\): count the pairs \((g,z)\) with \(gz=z\) by stabilizers, and each orbit contributes \(|G|\). If \(|G/H|>1\), the identity fixes more than one coset and every other element fixes at least one, contradicting that average. Thus \(G=H\).

Apply this fact to \(G=D^\times\), \(H=L^\times\). Then \(D=L\), so \(D\) is commutative. A division representative central over \(\mathbb F_q\) must consequently be \(\mathbb F_q\), giving the Brauer-group assertion. \(\square\)

This is Wedderburn's little theorem; compare [MIT, §14.5] and [Stacks, Tag 0753]. The finite-field input used here is that a degree-\(e\) extension of \(\mathbb F_q\) embeds into a degree-\(d\) extension when \(e\mid d\).

Over \(\mathbb R\), Frobenius's theorem states that a finite-dimensional associative real division algebra is isomorphic to \(\mathbb R\), \(\mathbb C\), or Hamilton's \(\mathbb H\); it was stated in the preceding lesson. Only \(\mathbb R\) and \(\mathbb H\) have centre \(\mathbb R\). Thus there are two real Brauer classes. Quaternion conjugation is an isomorphism \(\mathbb H\simeq\mathbb H^{\mathrm{op}}\), so its class is its own inverse. Since \(\mathbb H\) is a division algebra of degree \(2\), it is not split. Therefore

\[
\operatorname{Br}(\mathbb R)\simeq\mathbb Z/2\mathbb Z.
\]

## 6. Quaternion algebras and norms

Assume \(\operatorname{char} k\ne2\) and \(a,b\in k^\times\). The quaternion algebra

\[
Q=(a,b)_k=k\langle i,j\rangle/(i^2-a,\ j^2-b,\ ij+ji)
\]

has basis \(1,i,j,ij\). The relations first show these four elements span. Over \(\overline k\), choose \(\alpha^2=a\) and use the matrices

\[
I_a=\begin{pmatrix}\alpha&0\\0&-\alpha\end{pmatrix},
\qquad J_b=\begin{pmatrix}0&b\\1&0\end{pmatrix}.
\]

They satisfy the relations. The four matrices \(1,I_a,J_b,I_aJ_b\) are independent: the first two span the diagonal matrices and the last two span the off-diagonal matrices, since \(2\alpha b\ne0\). This proves the basis assertion and \(Q_{\overline k}\simeq M_2(\overline k)\). It also proves \(Q\) is central simple. A nonzero proper ideal would remain such after extension, contradicting simplicity of the matrix algebra; independence of a basis preserves both nonzeroness and properness. A central element becomes a scalar matrix after extension, so already lies in \(k1\).

If \(a\) is a square in \(k\), these same matrices give \(Q\simeq M_2(k)\). If \(a\) is not a square, \(L=k(i)\simeq k(\sqrt a)\) is a quadratic field and

\[
Q=L\oplus Lj,\qquad j\ell=\overline\ell j,
\]

where the bar is the nontrivial automorphism of \(L/k\).

**Proposition 6.1 (norm criterion).** For nonsquare \(a\),

\[
(a,b)_k\text{ is split}
\quad\Longleftrightarrow\quad
b=N_{L/k}(c)\text{ for some }c\in L^\times.
\]

**Proof.** If \(b=c\overline c\), let \(Q\) act on the \(k\)-vector space \(L\): let \(i\) multiply by \(\sqrt a\), and let \(j\) act by \(z\mapsto c\overline z\). Then \(j^2z=bz\) and \(jiz=-ijz\). We obtain a unital map \(Q\to\operatorname{End}_k(L)\); it is injective by simplicity and an isomorphism by dimension \(4\).

Conversely, suppose \(Q=\operatorname{End}_k(V)\), \(\dim_k V=2\). The embedded \(L\) makes \(V\) a one-dimensional \(L\)-vector space. Choose an \(L\)-basis and identify \(V=L\). The relation with \(L\) forces \(j\) to act as \(z\mapsto c\overline z\), with \(c=j(1)\ne0\). Its square acts as \(c\overline c\), which must equal \(b\). \(\square\)

Swapping \(i\) and \(j\) identifies \((a,b)_k\) with \((b,a)_k\). Thus, when \(b\) is nonsquare, the equivalent alternative criterion is that \(a\) be a norm from \(k(\sqrt b)\). If a parameter is square, the algebra is already split; one can extend the norm formulation using the split quadratic algebra \(k\times k\), whose norm is \((x,y)\mapsto xy\).

For \(k=\mathbb Q\), the algebra \((-1,2)_{\mathbb Q}\) splits because \(2=N_{\mathbb Q(i)/\mathbb Q}(1+i)\). In the basis \(1,i\) of \(\mathbb Q(i)\), the explicit matrices are

\[
i\longmapsto\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
j\longmapsto\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

Their squares are \(-1\) and \(2\), and they anticommute. By contrast, \((-1,-1)_{\mathbb Q}\) is not split: a norm from \(\mathbb Q(i)\) is \(x^2+y^2\), which cannot be \(-1\). Over \(\mathbb R\), the same norm criterion shows \((a,b)_{\mathbb R}\) splits if either parameter is positive. If both are negative, rescaling the generators identifies it with \(\mathbb H\).

The centralizer of \(L=k(i)\) inside \(Q\) is \(L\). In fact, for \(x=\ell+mj\),

\[
xi-ix=-2mi j,
\]

which is zero exactly when \(m=0\). In particular \(C_{\mathbb H}(\mathbb C)=\mathbb C\), and the centralizer dimension formula is \(2\cdot2=4\).

Quaternion conjugation is the linear map fixing \(1\) and negating \(i,j,ij\). The relations show \(\overline{xy}=\overline y\,\overline x\), so it gives \(Q\simeq Q^{\mathrm{op}}\). Therefore every quaternion Brauer class has order dividing \(2\). A nonsplit quaternion algebra has order exactly \(2\).

## 7. Reduced trace and reduced norm

The regular trace used in [Representations, characters and the group determinant](NOE-HYP-03.md) can vanish identically in positive characteristic. Central simple algebras have a more precise trace.

Choose a finite Galois splitting field \(F/k\), whose existence was proved in Theorem 4.3, and an isomorphism \(\phi:A_F\simeq M_n(F)\). For \(x\in A\), form

\[
P_x(T)=\det(TI_n-\phi(x\otimes1)).
\]

This polynomial lies in \(k[T]\) and is independent of \(F\) and \(\phi\). Indeed, two splitting isomorphisms over \(F\) differ by an inner automorphism by Theorem 2.1, which preserves the characteristic polynomial. For \(\sigma\in\operatorname{Gal}(F/k)\), compose \(\phi\) with \(1\otimes\sigma^{-1}\) on its domain and entrywise \(\sigma\) on its codomain. The resulting map is again \(F\)-linear. On \(x\otimes1\) it gives \(\sigma(\phi(x\otimes1))\). Inner conjugacy shows \(\sigma(P_x)=P_x\), so its coefficients are in the fixed field \(k\). For two different finite Galois splitting fields, pass to their compositum and use the same conjugacy argument there.

Define \(\operatorname{Trd}_{A/k}(x)\) to be minus the coefficient of \(T^{n-1}\) in \(P_x\), and \(\operatorname{Nrd}_{A/k}(x)\) to be \((-1)^nP_x(0)\). They become ordinary matrix trace and determinant over a splitting field. Thus reduced trace is \(k\)-linear, reduced norm is multiplicative, and

\[
\operatorname{Trd}(xy)=\operatorname{Trd}(yx),\qquad
\operatorname{Tr}_k(L_x)=n\operatorname{Trd}(x).
\]

The second equality follows after extension, since left multiplication by an \(n\)-by-\(n\) matrix acts on each of its \(n\) columns. Equality over \(F\) implies equality over \(k\).

The pairing \((x,y)\mapsto\operatorname{Trd}(xy)\) is nondegenerate in every characteristic. In a split algebra, \(\operatorname{tr}(XE_{ji})=X_{ij}\), so the matrix units detect every nonzero entry. The determinant of a Gram matrix is therefore nonzero after extension to \(F\), and hence already nonzero over \(k\). This explains why reduced trace remains useful when \(n=0\) in \(k\) and the regular trace is zero.

For \(Q=(a,b)_k\), writing \(x=x_0+x_1i+x_2j+x_3ij\), the splitting matrices give

\[
\operatorname{Trd}(x)=2x_0,\qquad
\operatorname{Nrd}(x)=x\overline x
 =x_0^2-a x_1^2-b x_2^2+ab x_3^2.
\]

For instance \(\operatorname{Nrd}_{\mathbb H/\mathbb R}(x)\) is the sum of four squares. See [Voight, §7.8] for reduced invariants in this generality.

## 8. Exercises

**Exercise 8.1 (easy).** Prove directly that every \(k\)-algebra automorphism \(f\) of \(M_n(k)\) is inner, using the images of the matrix units. Give a matrix which performs the conjugation.

**Exercise 8.2 (medium).** Assume \(\operatorname{char} k\ne2\), \(a\) nonsquare and \(b\ne0\). Reconstruct both directions of the norm criterion for \((a,b)_k\). For \(a=-1\), \(b=2\), verify the two displayed rational matrices satisfy the defining relations.

**Exercise 8.3 (medium).** Compute \(C_Q(k(i))\) in \(Q=(a,b)_k\), with \(a\) nonsquare and characteristic different from \(2\). Compute the double centralizer and check all dimensions. Specialize to \(\mathbb C\subset\mathbb H\).

**Exercise 8.4 (medium).** Check quaternion conjugation is an anti-automorphism, and deduce \(2[Q]=0\) in \(\operatorname{Br}(k)\). Explain why the class of \((-1,-1)_{\mathbb Q}\) is nonzero.

**Exercise 8.5 (hard).** Prove the double centralizer theorem independently in the following order: identify \(C_A(B)\) with an endomorphism algebra; use the multiplicity of the unique simple module to compute its dimension; then apply that computation a second time. Explain where centrality of \(A\), simplicity of \(B\), and finite dimension are each used.

## 9. Solutions

**Solution 8.1.** Choose \(0\ne v\in\operatorname{im}f(E_{11})\) and put \(v_i=f(E_{i1})v\). Here \(f(E_{11})v=v\). Since \(f(E_{1j})v_i=\delta_{ji}v\), the \(v_i\) are linearly independent; they therefore form a basis of \(k^n\). Let \(u\) have these columns. Then

\[
f(E_{ab})v_i=\delta_{bi}v_a=uE_{ab}u^{-1}v_i.
\]

Hence \(f(E_{ab})=uE_{ab}u^{-1}\), and linearity gives the same identity for every matrix. No separability or characteristic condition was used.

**Solution 8.2.** If \(b=c\overline c\), multiplication by \(\sqrt a\) and the map \(z\mapsto c\overline z\) on \(L=k(\sqrt a)\) satisfy \(i^2=a\), \(j^2=b\) and \(ji=-ij\). The induced algebra map to \(\operatorname{End}_k(L)\) is injective because \(Q\) is simple and unital, and surjective because both dimensions are \(4\). If \(Q\) is split on \(V=k^2\), the action of the field \(L\) makes \(V\) one-dimensional over \(L\). The relation \(j\ell=\overline\ell j\) says that, in an \(L\)-basis, \(j(z)=c\overline z\); its invertibility gives \(c\ne0\). Squaring gives \(b=c\overline c\).

For the rational matrices \(I=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\) and \(J=\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\), multiplication yields \(I^2=-I_2\), \(J^2=2I_2\), and

\[
IJ=\begin{pmatrix}-1&1\\1&1\end{pmatrix},\qquad
JI=\begin{pmatrix}1&-1\\-1&-1\end{pmatrix}=-IJ.
\]

They realize the norm \(N(1+i)=2\).

**Solution 8.3.** Write \(x=\ell+mj\) uniquely with \(\ell,m\in L\). Then \(xi-ix=-2mi j\). The factors \(2,i,j\) are invertible, so this is zero exactly when \(m=0\). Thus \(C_Q(L)=L\) and \(C_Q(C_Q(L))=L\). The centre of this centralizer is \(L\), not \(k\), and \(\dim_k L\cdot\dim_k L=2\cdot2=4=\dim_k Q\). For \(a=b=-1\) over \(\mathbb R\), this is exactly \(C_{\mathbb H}(\mathbb C)=\mathbb C\).

**Solution 8.4.** Reverse the order of every product in the defining relations and send \(i\) to \(-i\), \(j\) to \(-j\). The squared relations remain \(a\) and \(b\), and the reversed anticommutation relation remains valid. Thus the assignment defines a homomorphism \(Q\to Q^{\mathrm{op}}\); applying it twice is the identity, so it is an isomorphism. It sends \(ij\) to \(-ij\), and is quaternion conjugation. The inverse formula in the Brauer group gives \([Q]=[Q^{\mathrm{op}}]=-[Q]\), hence \(2[Q]=0\). The rational algebra \((-1,-1)\) cannot split because that would require \(-1=x^2+y^2\) with \(x,y\in\mathbb Q\). Its nonzero class therefore has order exactly \(2\).

**Solution 8.5.** The field \(F=Z(B)\) makes \(B\) central simple over \(F\). The algebra \(R=B\otimes_k A^{\mathrm{op}}\) is simple since it is \(B\otimes_F A_F^{\mathrm{op}}\). It acts on \(A\) by left \(B\)- and right \(A\)-multiplication. An \(R\)-endomorphism has the form \(x\mapsto cx\), because of right \(A\)-linearity, and left \(B\)-linearity says precisely \(c\in C_A(B)\).

Write \(R=M_r(E)\), \(A=(E^r)^m\) as an \(R\)-module, and \(e=\dim_k E\). Then

\[
C_A(B)\simeq M_m(E^{\mathrm{op}}),\qquad
\dim_k A=rme,\qquad
(\dim_k B)(\dim_k A)=r^2e.
\]

This makes \(C_A(B)\) simple of dimension \(m^2e\), and gives \(\dim_k B\,\dim_k C_A(B)=\dim_k A\). Apply the same formula to the now simple subalgebra \(C_A(B)\). Its centralizer has dimension \(\dim_k B\) and contains \(B\), so it equals \(B\). The centres are their intersection, namely \(Z(B)\). If \(B\) is central, both factors in \(B\otimes C_A(B)\) are central simple, and multiplication is injective by simplicity and surjective by dimension.

Centrality of \(A\) is used to preserve simplicity under scalar extension and tensor product. Simplicity of \(B\) gives its field centre and the simple algebra \(R\). Finite dimension provides Wedderburn's finite module multiplicities and the dimension comparisons. The conclusion about \(B\otimes C_A(B)\) additionally requires \(Z(B)=k\); for \(\mathbb C\subset\mathbb H\), the two factors share \(\mathbb C\) and this tensor conclusion over \(\mathbb R\) does not hold.

## Sources and further reading

- **[Noether]** Emmy Noether, “Nichtkommutative Algebra,” *Mathematische Zeitschrift* **37** (1933), 514–541, especially §§4–7. The representation viewpoint, commutation theorem and §7's similar algebra classes explain the common mechanism behind this lesson. The paper is work 40 in *Gesammelte Abhandlungen / Collected Papers*.
- **[Voight]** John Voight, *Quaternion Algebras*, GTM 288, Springer, 2021: §§7.5–7.7 for scalar extension, Skolem–Noether and centralizers; §7.8 for reduced invariants; §8.3 for the Brauer group. An [author-maintained edition](https://jvoight.github.io/quat.html) is available.
- **[MIT]** *Noncommutative Algebra*, MIT OpenCourseWare 18.706, Spring 2023, lecture notes §§13.3 and 14.1–14.5. The finite-division-ring proof uses the coset-counting argument developed there. See the [course materials](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/pages/lecture-notes/).
- **[Milne CFT]** J. S. Milne, [*Class Field Theory*](https://www.jmilne.org/math/CourseNotes/CFT.pdf), course notes, Chapter IV, for central simple algebras, the Brauer group and its relation with Galois cohomology; our proofs above use elementary module and tensor arguments.
- **[Stacks]** The Stacks Project, “Brauer groups,” tags [074F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#lemma-tensor-simple), [074G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#lemma-tensor-central-simple), [074H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#lemma-base-change), [074I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#lemma-inverse), [074N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#lemma-dimension-square), [074Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#theorem-skolem-noether), [074R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#lemma-automorphism-inner), [074T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#theorem-centralizer), [074U](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#lemma-when-tensor-is-equal), [0752](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#proposition-separable-splitting-field), and [0753](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/brauer.html#lemma-finite-central-simple-algebra). These links read the AI Integrated Stacks Project edition with the same official tags. That edition is an independent AI draft, not a reviewed release by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).

The next lesson, *Crossed products and factor systems*, identifies the relative Brauer group for a finite Galois splitting extension with a second cohomology group. The separate planned lesson *Brauer groups and Tsen's theorem* in the étale-cohomology course connects this field theory with geometric Brauer groups and the vanishing theorem for function fields of curves; those are further results, beyond the present lesson.

## What this lesson does not prove

Frobenius's classification of real division algebras is used as stated in *Semisimple rings and Wedderburn's theorem*, with its source there. We use the standard finite-field classification and embedding theorem, and the elementary field-theoretic facts about separability, normal closures and fixed fields of finite Galois extensions, from Abstract Algebra II. All central-simple-algebra, centralizer, splitting and Brauer-group results used here are proved above, including separable maximal-subfield existence and the finite-division-ring theorem. The lesson does not prove Tsen's theorem, identify geometric Brauer groups, classify \(\operatorname{Br}(\mathbb Q)\), or assert that every central division algebra contains a Galois maximal subfield.
