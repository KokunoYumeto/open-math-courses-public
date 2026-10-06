# Graded modules and Hilbert–Samuel functions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A grading lets us count equations and functions one degree at a time. In a local ring, powers of an ideal give a related count: the length of a module after discarding terms of sufficiently high order. The first count eventually becomes a polynomial; summing its layers gives the second. Its degree will be a dimension invariant, and its leading coefficient records multiplicity.

Rings are commutative with identity. A finite module is finitely generated. Graded rings in this lesson have **nonnegative** gradings; graded modules may have integer gradings. A local ring is not assumed Noetherian unless stated. We use Hilbert basis, the finite-length and Artinian criteria, radical-power containment, and Artin–Rees from [Noetherian and Artinian rings](noetherian-and-artinian-rings.md), Theorem 2.1, Proposition 2.2, and Theorems 3.3, 4.2 and 5.1. We also use Nakayama from [Localization, local properties and support](localization-local-properties-and-support.md), Theorem 4.2. No dimension theorem for Noetherian local rings is assumed here.

## 1. Finite generation and homogeneous pieces

A graded ring is a decomposition \(S=\bigoplus_{n\geq0}S_n\) with \(1\in S_0\) and \(S_iS_j\subseteq S_{i+j}\). Its positive part \(S_+=\bigoplus_{n>0}S_n\) is an ideal, and \(S/S_+=S_0\). A graded module \(M=\bigoplus_{n\in\mathbb Z}M_n\) satisfies \(S_iM_j\subseteq M_{i+j}\). Elements in a single piece are homogeneous. A graded submodule contains the homogeneous components of each of its elements. Maps of degree zero preserve pieces; kernels, images and quotients inherit gradings, and their sequences are exact piece by piece.

**Theorem 1.1.** Such an \(S\) is Noetherian if and only if \(S_0\) is Noetherian and \(S\) is a finite-type \(S_0\)-algebra.

**Proof.** If \(S\) is Noetherian, its quotient \(S_0\) is Noetherian. Choose finite ideal generators of \(S_+\), and replace them by all their homogeneous components. The replacement still generates the ideal: it contains the original generators in its span, and all its elements lie in \(S_+\). Denote the resulting homogeneous elements by \(x_1,\ldots,x_r\), all of positive degree.

They generate \(S\) as an algebra over \(S_0\). Indeed, induct on the degree of a homogeneous \(s\). Degree zero is already in the base ring. In degree \(d>0\), an ideal expression for \(s\), followed by taking its degree-\(d\) component, gives
\[
s=\sum_i a_i x_i,\qquad a_i\in S_{d-\deg x_i},
\]
where terms with negative subscripts vanish. Every remaining coefficient has smaller degree and belongs to \(S_0[x_1,\ldots,x_r]\) by induction. Every element is a finite sum of homogeneous ones, so the algebra assertion follows. Conversely, a finite-type algebra over the Noetherian ring \(S_0\) is Noetherian by Hilbert basis. \(\square\)

**Proposition 1.2.** If \(S\) is of finite type over \(S_0\) and \(M\) is finite and graded, each \(M_n\) is finite over \(S_0\), and \(M_n=0\) for sufficiently negative \(n\). If \(S_0\) is Artinian, each piece has finite length over \(S_0\).

**Proof.** Decomposing a finite algebra generating list into homogeneous components produces a finite homogeneous list. Its degree-zero members can be omitted, leaving positive-degree generators. In any fixed degree, only finitely many monomials in them occur: their positive weights bound every exponent. Thus each \(S_n\) is finite over \(S_0\).

Likewise, decomposing module generators gives homogeneous generators \(m_i\), of degrees \(a_i\). There is a surjection
\[
\bigoplus_i S_{n-a_i}\longrightarrow M_n.
\tag{1}
\]
This proves finiteness of the pieces and vanishing below \(\min_i a_i\). An Artinian commutative ring has finite length over itself by the earlier Artinian criterion. Its finite modules are quotients of finite sums of that ring, so have finite length. \(\square\)

The shift \(M(a)\) has \(M(a)_n=M_{n+a}\). In particular, a degree-\(a\) generator is the image of the degree-\(a\) element \(1\) in \(S(-a)\). This explains (1) as the degree part of a map between graded modules.

## 2. Discrete integration

A **numerical polynomial** is a polynomial in \(\mathbb Q[t]\) taking integer values at all sufficiently large integers. This is weaker than having integer coefficients in the power basis. For example, \(t(t-1)/2\) is numerical.

Write
\[
B_i(t)=\binom ti=\frac{t(t-1)\cdots(t-i+1)}{i!},\qquad B_0(t)=1.
\]
The forward difference is \(\Delta P(t)=P(t+1)-P(t)\).

**Lemma 2.1.** A polynomial is numerical exactly when it is an integer linear combination of the \(B_i\). It then takes integer values at every integer. Moreover \(\Delta B_i=B_{i-1}\) for \(i\geq1\).

**Proof.** For nonnegative integers the binomial values are integers, and for a negative integer \(t\),
\[
\binom ti=(-1)^i\binom{i-t-1}{i},
\]
which is again integral. The difference identity follows from Pascal's identity at nonnegative integers, hence holds as a polynomial identity. The \(B_i\) have distinct degrees and nonzero leading coefficients, so \(B_0,\ldots,B_d\) form a rational basis of the polynomials of degree at most \(d\).

Suppose \(P=\sum_{i=0}^d c_iB_i\) is numerical. Induct on \(d\). For constants the assertion is immediate. Its difference is numerical of smaller degree and has expansion \(\sum_{i=1}^d c_iB_{i-1}\). Induction and uniqueness of the rational basis expansion show that \(c_1,\ldots,c_d\) are integers. Evaluating \(P\) at one sufficiently large integer then shows that \(c_0\) is integral. The converse follows from the integer values of each \(B_i\). \(\square\)

**Lemma 2.2.** If an integer-valued function \(h\) satisfies
\[
h(n)-h(n-1)=Q(n)
\tag{2}
\]
for all sufficiently large \(n\), with \(Q\) numerical, then \(h\) is eventually a numerical polynomial. If \(Q\neq0\) has degree \(s\), that polynomial has degree \(s+1\). If \(Q=0\), the function is eventually constant.

**Proof.** Express \(Q(t)=\sum c_i\binom ti\) with integral coefficients. Set \(F(t)=\sum c_i\binom{t+1}{i+1}\). Pascal's identity gives \(F(n)-F(n-1)=Q(n)\). Thus \(h(n)-F(n)\) is constant on the sufficiently large integers. That constant is integral, proving the claim. For nonzero \(Q\), its highest coefficient produces the unique term of degree \(s+1\) in \(F\). \(\square\)

Throughout, the degree of the zero polynomial is \(-\infty\). An eventual polynomial is unique, since a nonzero polynomial cannot vanish at infinitely many integers. Lemma 2.1 also shows that a numerical polynomial of degree \(d\) has leading coefficient \(c/d!\) for a nonzero integer \(c\).

## 3. Hilbert–Serre by multiplication

Call \(S\) **standard graded** over \(S_0\) if it is generated by finitely many degree-one elements. For a finite graded module over such a ring with \(S_0\) Artinian, define its Hilbert function by
\[
h_M(n)=\ell_{S_0}(M_n).
\]

**Theorem 3.1 (Hilbert–Serre).** Suppose \(S\) is generated over an Artinian \(S_0\) by \(r\) degree-one elements. For every finite graded \(S\)-module \(M\), the function \(h_M(n)\) agrees eventually with a numerical polynomial of degree at most \(r-1\) if \(r\geq1\). If \(r=0\), it is eventually zero.

**Proof.** Let \(A=S_0[X_1,\ldots,X_r]\) with each variable of degree one, mapping onto \(S\). Then \(M\) is finite and graded over \(A\); this polynomial ring is Noetherian by Theorem 1.1. Induct on \(r\). For \(r=0\), a finite homogeneous generating list over \(S_0\) has only finitely many degrees, so all large pieces vanish.

For \(r>0\), let \(x\) act as \(X_r\), and put
\[
L=(0:_M x),\qquad C=M/xM.
\]
Both are finite graded modules: finiteness of the submodule \(L\) uses Noetherianity. Both are killed by \(X_r\), so are finite over \(S_0[X_1,\ldots,X_{r-1}]\). Taking degree parts of multiplication gives the exact sequence
\[
0\longrightarrow L_{n-1}\longrightarrow M_{n-1}
\xrightarrow{x}M_n\longrightarrow C_n\longrightarrow0.
\tag{3}
\]
Length additivity therefore yields
\[
h_M(n)-h_M(n-1)=h_C(n)-h_L(n-1).
\tag{4}
\]
If \(r=1\), induction makes the right side eventually zero, so \(h_M\) is eventually constant. If \(r\geq2\), that side is eventually a numerical polynomial of degree at most \(r-2\): a translate of a numerical polynomial remains numerical. Lemma 2.2 gives the degree bound \(r-1\), including the possibility that the difference or the resulting polynomial is zero. \(\square\)

Multiplication need not be injective. The kernel term in (3) is what makes the proof work for arbitrary finite modules, including modules with torsion. There is also a version without the Artinian assumption, retaining module classes in place of their lengths.

**Proposition 3.2 (Hilbert–Serre with module classes).** Let \(S_0\) be Noetherian and let \(S\) be generated by \(r\) degree-one elements. In the Grothendieck group \(G_0(S_0)\) of finite modules, generated by classes \([N]\) with relations \([N]=[N']+[N'']\) for short exact sequences, every finite graded \(S\)-module satisfies
\[
\sum_n[M_n]t^n=\frac{Q(t)}{(1-t)^r},
\tag{4a}
\]
with \(Q\) a Laurent polynomial over \(G_0(S_0)\). Its classes consequently have an eventual expression as a finite \(G_0(S_0)\)-linear combination of binomial polynomials of degree at most \(r-1\), or are eventually zero if \(r=0\).

**Proof.** Every degree part is finite over \(S_0\), by the homogeneous finite generating list, and degrees are bounded below. In (3), the Grothendieck relation gives exactly
\([M_n]-[M_{n-1}]=[C_n]-[L_{n-1}]\).
Multiply by \(t^n\) and sum formally. This yields \((1-t)H_M=H_C-tH_L\). Both modules on the right are finite graded modules over the polynomial ring with one fewer variable, just as in the proof of Theorem 3.1. Induction, starting with the finite number of nonzero degree parts when \(r=0\), proves (4a). Finally \((1-t)^{-r}=\sum_{n\ge0}\binom{n+r-1}{r-1}t^n\) for \(r>0\), as follows by multiplying \(r\) geometric series and counting weak compositions. Coefficient comparison with the finite numerator gives the claimed eventual binomial expression. Applying the additive length homomorphism when \(S_0\) is Artinian recovers the length version. \(\square\)

For a polynomial ring \(k[x_0,\ldots,x_q]\) over a field, its degree-\(t\) monomials correspond to tuples of \(q+1\) nonnegative exponents with sum \(t\). Placing \(q\) dividers among \(t+q\) positions gives
\[
h(t)=\binom{t+q}{q}\qquad(t\geq0).
\tag{5}
\]
If \(0\neq f\in k[x,y,z]\) is homogeneous of degree \(a\geq1\), multiplication by \(f\) is injective in this polynomial domain. Hence the quotient \(S=k[x,y,z]/(f)\) has
\[
h_S(t)=\binom{t+2}{2}-\dim_k k[x,y,z]_{t-a}.
\]
For \(t\geq\max(0,a-2)\), the second term equals the polynomial \(\binom{t-a+2}{2}\): at \(t-a=-2,-1\), both the piece and that polynomial are zero. Expanding gives
\[
h_S(t)=at-\frac{a(a-3)}2.
\tag{6}
\]
Thus the degree of the homogeneous equation appears in the slope of the count. Degree-one generation matters: a single variable of degree two has one monomial in every even degree and none in odd degree. Exercise 9.6 proves why that function cannot eventually be polynomial.

## 4. From an ideal filtration to a graded module

Let \((R,\mathfrak m)\) be Noetherian local. An **ideal of definition** is a proper ideal \(I\) with \(\sqrt I=\mathfrak m\) [Stacks, Tag 07DU]. Equivalently,
\[
\mathfrak m^a\subseteq I\subseteq\mathfrak m
\tag{7}
\]
for some \(a\geq1\). Radical-power containment proves the forward implication, and taking radicals proves the converse. In particular, \(R/I^n\) for \(n\geq1\) is Noetherian and has only one prime, its maximal ideal. The earlier Artinian criterion makes it Artinian, so every finite module over it has finite length.

For a finite \(R\)-module \(M\), the **Hilbert–Samuel function** is
\[
H_{I,M}(n)=\ell_R(M/I^nM)\qquad(n\geq0).
\tag{8}
\]
Here \(I^0M=M\), so \(H_{I,M}(0)=0\). Its consecutive layers are the pieces of
\[
\operatorname{gr}_I(R)=\bigoplus_{j\geq0} I^j/I^{j+1},\qquad
\operatorname{gr}_I(M)=\bigoplus_{j\geq0}I^jM/I^{j+1}M.
\tag{9}
\]
Multiplication is induced by multiplication in \(R\) and its action on \(M\). Changing representatives introduces terms of one higher order, so these operations are well defined.

**Lemma 4.1.** The ring in (9) is standard graded over \(R/I\), which is Artinian, and its module is finite, generated in degree zero.

**Proof.** Choose ideal generators \(a_1,\ldots,a_r\) of \(I\). Products of their classes in \(I/I^2\) generate every ring piece over \(R/I\), because products of \(j\) ideal generators generate \(I^j\). If \(m_1,\ldots,m_s\) generate \(M\), each element of \(I^jM\) is a sum of those same products times the \(m_i\). Thus their images in \(M/IM\) generate the graded module. \(\square\)

The **Rees algebra** retains the filtration before taking its consecutive quotients:
\[
\mathcal R_I(R)=\bigoplus_{j\geq0}I^jT^j\subseteq R[T],\qquad
\mathcal R_I(M)=\bigoplus_{j\geq0}I^jM T^j.
\tag{10}
\]
It is generated as an \(R\)-algebra by \(a_iT\), so is Noetherian by Hilbert basis. Its module is generated by the \(m_i\) in degree zero. Quotienting by the action of the degree-zero ideal \(I\) gives precisely (9): the degree-\(j\) denominator is \(I^{j+1}T^j\), or \(I^{j+1}M T^j\) for the module. This distinguishes the Rees algebra from the associated graded ring. Neither requires a completion.

**Theorem 4.2 (Hilbert–Samuel polynomial).** For an ideal of definition \(I\) and a finite \(M\), the function (8) is eventually a numerical polynomial \(P_{I,M}(t)\). If \(I\) has \(r\) generators, its degree is at most \(r\).

**Proof.** Apply Theorem 3.1 to (9), using Lemma 4.1. The layer length
\[
g(j)=\ell_R(I^jM/I^{j+1}M)
\]
is eventually numerical of degree at most \(r-1\) for \(r\geq1\). Its length over \(R/I\) is the same as its length over \(R\), because it is killed by \(I\) and these actions have exactly the same submodules. The finite filtration of \(M/I^nM\) gives
\[
H_{I,M}(n)=\sum_{j=0}^{n-1}g(j),\qquad
H_{I,M}(n)-H_{I,M}(n-1)=g(n-1).
\tag{11}
\]
Lemma 2.2 now proves the assertion and degree bound. If \(r=0\), then \(I=0\), \(R\) is Artinian, and \(H(n)=\ell_R(M)\) for every \(n\geq1\). This includes the zero module. \(\square\)

## 5. Degree and multiplicity

If \(M\neq0\), Nakayama gives \(M/IM\neq0\). The function \(H_{I,M}\) is nondecreasing and at least its positive value at one for \(n\geq1\). Its eventual polynomial is therefore nonzero and has positive leading coefficient. For \(M=0\) it is zero, of degree \(-\infty\).

**Theorem 5.1.** The degree of \(P_{I,M}\) is independent of the ideal of definition \(I\).

**Proof.** If \(I,J\) are ideals of definition, (7) supplies positive integers \(a,b\) with \(I^a\subseteq J\) and \(J^b\subseteq I\). Raising these containments to the \(n\)-th power and passing to quotient lengths gives
\[
H_{J,M}(n)\leq H_{I,M}(an),\qquad
H_{I,M}(n)\leq H_{J,M}(bn).
\tag{12}
\]
For \(M\neq0\), both eventual polynomials have positive leading coefficients. The first inequality prevents the degree for \(J\) from exceeding that for \(I\): otherwise its higher power of \(n\) eventually exceeds the other polynomial. The second gives the reverse comparison. For \(M=0\), both degrees are \(-\infty\). \(\square\)

Denote this degree by \(d(M)\). For nonzero \(M\), define its **multiplicity with respect to \(I\)** by
\[
e_I(M)=d(M)!\,[t^{d(M)}]P_{I,M}(t).
\tag{13}
\]
It is a positive integer by Lemma 2.1. Set \(e_I(0)=0\). The eventual growth reads \(e_I(M)n^{d(M)}/d(M)!\) plus lower-degree terms.

The ideal remains part of multiplicity's notation. For example, in \(R=k[t]_{(t)}\), the ideal \(I=(t^a)\) gives \(H_{I,R}(n)=an\). Indeed the quotient has basis \(1,t,\ldots,t^{an-1}\), and its local composition factors are copies of \(k\). Thus \(d(R)=1\) for every positive \(a\), but \(e_{(t^a)}(R)=a\).

At this stage \(d(M)\) is defined by growth. Its equality with the dimension of the support is proved in *Dimension theory of Noetherian local rings*. The current results neither assume nor need that equality.

## 6. Exact sequences and the induced filtration

**Theorem 6.1.** In an exact sequence of finite modules over a Noetherian local ring,
\[
0\longrightarrow M'\longrightarrow M\longrightarrow M''\longrightarrow0,
\]
we have \(d(M)=\max\{d(M'),d(M'')\}\).

**Proof.** Identify \(M'\) with its image and fix an ideal of definition \(I\). The relevant quotient sequence is
\[
0\longrightarrow M'/(M'\cap I^nM)\longrightarrow M/I^nM
\longrightarrow M''/I^nM''\longrightarrow0.
\tag{14}
\]
The middle map is surjective. Its kernel consists of the image of \(M'\), because the preimage of \(I^nM''\) is \(M'+I^nM\). This proves (14), including its stated first term.

Artin–Rees supplies \(c\geq0\) such that for \(n\geq c\),
\[
I^nM'\subseteq M'\cap I^nM
=I^{n-c}(M'\cap I^cM)\subseteq I^{n-c}M'.
\tag{15}
\]
Quotient lengths and (14) therefore give
\[
H_{I,M''}(n)+H_{I,M'}(n-c)
\leq H_{I,M}(n)
\leq H_{I,M''}(n)+H_{I,M'}(n).
\tag{16}
\]
If both end modules are zero, so is \(M\). Otherwise the two bounding eventual polynomials have the same degree, namely the maximum of the end degrees, and the same positive leading coefficient. Translation does not alter a polynomial's degree or leading coefficient. Polynomial growth in (16) then forces the middle polynomial to have that same degree and leading coefficient. This includes degree zero, where translation leaves the constant polynomial unchanged, and includes one zero end module. \(\square\)

For a fixed nonnegative degree \(d\), set
\[
E_{I,d}(N)=
\begin{cases}
e_I(N),&d(N)=d,\\
0,&d(N)<d.
\end{cases}
\]
When \(d=d(M)\), the same proof yields
\[
e_I(M)=E_{I,d}(M')+E_{I,d}(M'').
\tag{17}
\]
Only contributions in the largest degree count. The whole Hilbert–Samuel polynomial need not be additive, because the induced filtration \(M'\cap I^nM\) need not equal \(I^nM'\).

**Corollary 6.2.** For a nonzero finite module, \(d(M)=0\) exactly when \(M\) has finite length; then \(e_I(M)=\ell_R(M)\).

**Proof.** If \(d(M)=0\), the eventual function \(H(n)\) is constant. By (11), \(I^nM/I^{n+1}M=0\) for sufficiently large \(n\). The finite module \(I^nM\) satisfies \(I(I^nM)=I^nM\), so Nakayama gives \(I^nM=0\). Thus \(M\) is finite over the Artinian ring \(R/I^n\), and has finite length. Conversely, all simple factors of a finite-length module over the local ring are \(R/\mathfrak m\). A composition series of length \(l\) shows successively that \(\mathfrak m^lM=0\). Therefore \(I^nM=0\) for \(n\geq l\), and \(H(n)=\ell_R(M)\). \(\square\)

## 7. Initial forms and plane hypersurfaces

Let \(A=k[x,y]_{(x,y)}\), with maximal ideal \(\mathfrak n=(x,y)A\). For a nonzero polynomial, its order is the least total degree of a nonzero homogeneous part. A fraction \(p/q\in A\), with \(q(0,0)\neq0\), has the order of \(p\). This is independent of its representation: equality \(pq'=p'q\) gives equality of lowest degrees, and denominators have order zero. Its initial form is the lowest homogeneous part of \(p\), divided by \(q(0,0)\).

These forms identify
\[
\operatorname{gr}_{\mathfrak n}(A)=k[X,Y].
\tag{18}
\]
To check this, every fraction in \(\mathfrak n^j\) has a numerator in \((x,y)^j\). Modulo \(\mathfrak n^{j+1}\), only its degree-\(j\) numerator and the constant denominator remain. This proves surjectivity onto each piece. A nonzero homogeneous polynomial of degree \(j\) cannot enter \(\mathfrak n^{j+1}\) upon localization: multiplying it by a polynomial with nonzero constant term preserves its nonzero lowest degree. This proves injectivity. Products of nonzero initial forms in the polynomial domain are nonzero, so
\[
\operatorname{ord}(uv)=\operatorname{ord}(u)+\operatorname{ord}(v)
\tag{19}
\]
for nonzero \(u,v\in A\).

**Theorem 7.1.** Let \(0\neq f\in(x,y)\subset k[x,y]\), let \(r=\operatorname{ord}(f)\), and let \(f_r\) be its degree-\(r\) homogeneous part. For \(R=A/(f)\), with maximal ideal \(\mathfrak m\),
\[
\operatorname{gr}_{\mathfrak m}(R)=k[X,Y]/(f_r).
\tag{20}
\]
Its layer lengths are \(\min(j+1,r)\) in degree \(j\geq0\). In particular,
\[
\ell_R(R/\mathfrak m^n)=rn-\frac{r(r-1)}2
\quad\text{for }n\geq\max(1,r-1),
\tag{21}
\]
so \(d(R)=1\) and \(e_{\mathfrak m}(R)=r\).

**Proof.** The quotient map induces a surjection in (18) onto the graded ring of \(R\). In degree \(j\), its kernel is represented by elements
\[
g\in\mathfrak n^j\cap\bigl((f)+\mathfrak n^{j+1}\bigr).
\]
Write \(g=hf+b\), with \(b\in\mathfrak n^{j+1}\). If its degree-\(j\) class is nonzero, then \(hf\) has order exactly \(j\), and (19) identifies that class with the initial form of \(h\) times \(f_r\). Conversely each homogeneous multiple of \(f_r\) is the initial form of the corresponding polynomial multiple of \(f\), hence belongs to the kernel. This proves (20).

Multiplication by the nonzero homogeneous \(f_r\) is injective in \(k[X,Y]\). Consequently its degree-\(j\) quotient has dimension
\[
(j+1)-\max(0,j-r+1)=\min(j+1,r).
\tag{22}
\]
The residue field is \(k\), so a finite-dimensional layer has length equal to its \(k\)-dimension: all its local simple factors are one-dimensional over \(k\). Summing (22) proves (21), since the deficit from the constant value \(r\) is \((r-1)+(r-2)+\cdots+1=r(r-1)/2\). At \(n=r-1\) this already gives the correct sum; for smaller \(n\) the sum is \(n(n+1)/2\). Its eventual linear polynomial has leading coefficient \(r\). \(\square\)

For the cusp \(f=y^2-x^3\), the initial form is \(Y^2\). Thus its tangent graded algebra is \(k[X,Y]/(Y^2)\), and \(H(n)=2n-1\) for every \(n\geq1\). The multiplicity is two. For \(f=y^2-x^2(x+1)\), the initial form is \(Y^2-X^2\), so the same function and multiplicity occur. In characteristic different from two, this form is the product of two distinct tangent lines, and the singularity is a node. In characteristic two the two factors coincide; the multiplicity calculation still holds, but the distinct-tangent description does not.

Multiplicity therefore measures a count that need not distinguish different singularities. The graded algebras retain additional information: one example has a doubled tangent direction, while the other, in characteristic different from two, has two tangent directions.

## 8. What this lesson does not prove

Hilbert basis, radical-power containment, finite-length and Artinian criteria, Artin–Rees and Nakayama are imported at the prerequisite locators given at the start. Every graded finiteness, numerical-polynomial, Hilbert–Serre, Hilbert–Samuel, degree and multiplicity assertion taught here is proved. Proposition 3.2 also proves the Grothendieck-group version of Hilbert–Serre [Stacks, Tag 00K1]. Equality of \(d(M)\) with support dimension belongs to *Dimension theory of Noetherian local rings*. Projective sheaf Hilbert polynomials require further geometric results and are not used in these proofs.

## 9. Exercises

**Exercise 9.1 (easy: three axes).** With standard grading, compute the Hilbert function and polynomial of \(k[x,y,z]/(xy,yz,zx)\).

**Exercise 9.2 (easy: a finite local algebra).** For \(R=k[[x,y]]/(x^2,y^3)\) and \(\mathfrak m=(x,y)R\), compute \(\ell(R/\mathfrak m^n)\) for all \(n\geq0\), and its degree and multiplicity.

**Exercise 9.3 (medium: comparison of ideals).** Prove directly from power containments and polynomial growth that \(d(M)\) is independent of the ideal of definition. Then compute the different multiplicities of \((t)\) and \((t^3)\) on \(k[t]_{(t)}\).

**Exercise 9.4 (medium: the order of an equation).** For a nonzero \(f\in(x,y)\), prove that the multiplicity of \(k[x,y]_{(x,y)}/(f)\) is the lowest degree of its nonzero homogeneous parts. Compute the multiplicity for \(x^3+x^2y+y^5\) over any field.

**Exercise 9.5 (hard: top coefficients and filtration error).** Starting with Artin–Rees, prove (17) in a short exact sequence. Show that additivity of the whole Hilbert–Samuel polynomial fails in \(0\to(t)\to k[t]_{(t)}\to k\to0\), with ideal of definition \((t)\). Identify the induced filtration that restores exact quotient lengths.

**Exercise 9.6 (medium: a weighted grading).** Grade \(k[u]\) by \(\deg u=2\). Compute its Hilbert function, prove it is not eventually a polynomial, and compute the cumulative function \(\sum_{j=0}^{n-1}\dim_k k[u]_j\). Explain the role of standard grading.

## 10. Solutions

**Solution 9.1.** The monomial ideal kills exactly the monomials involving two or more of the variables. Monomials are a vector-space basis of the polynomial ring, and the ideal is spanned by those divisible by one of its three generators, so the remaining monomials form a quotient basis. They are \(1\), and \(x^n,y^n,z^n\) for each \(n\geq1\). Thus \(h(0)=1\), \(h(n)=3\) for \(n\geq1\), and the eventual polynomial is the constant three, of degree zero. This degree is the graded Hilbert polynomial's degree, not the Hilbert–Samuel degree of a local ring.

**Solution 9.2.** Every formal series reduces uniquely to a linear combination of
\[
1,\ y,\ x,\ y^2,\ xy,\ xy^2.
\]
Indeed every other monomial is divisible by \(x^2\) or \(y^3\), and coefficient comparison shows that no combination of the displayed monomials lies in that ideal. The quotient is therefore six-dimensional over \(k\). Elements with nonzero constant coefficient are units, by a finite geometric series in the nilpotent maximal ideal; elements with zero constant coefficient form \(\mathfrak m\). Thus this is a local Artinian algebra with residue field \(k\).

The displayed basis has total degrees \(0,1,1,2,2,3\). Products of \(n\) elements of \(\mathfrak m\) span exactly the surviving monomials of degree at least \(n\): every such monomial is a product of that many variables times another monomial, and every product has at least that degree. Hence the layer dimensions are \(1,2,2,1\), then zero. Cumulative lengths are
\[
H(0)=0,\quad H(1)=1,\quad H(2)=3,\quad H(3)=5,\quad H(n)=6\ (n\geq4).
\]
Lengths equal vector-space dimensions because every simple factor is \(k\). The eventual polynomial is six, so \(d(R)=0\) and \(e_{\mathfrak m}(R)=6\).

**Solution 9.3.** Choose \(a,b\geq1\) with \(I^a\subseteq J\) and \(J^b\subseteq I\), using the powers of \(\mathfrak m\) contained in each ideal and the containments \(I,J\subseteq\mathfrak m\). Then \(I^{an}M\subseteq J^nM\) and \(J^{bn}M\subseteq I^nM\), giving (12). For nonzero \(M\), both eventual polynomials have positive leading terms, so the inequalities give both degree comparisons. The zero module has both degrees \(-\infty\). For the specified one-variable ring, the quotients by \((t)^n\) and \((t^3)^n\) have respective bases \(1,\ldots,t^{n-1}\) and \(1,\ldots,t^{3n-1}\). Their polynomials are \(n\) and \(3n\): the degree is one, while the multiplicities are one and three.

**Solution 9.4.** Set \(r=\operatorname{ord}(f)\). The initial-form product rule in (19) shows that every initial form of a nonzero multiple of \(f\) is divisible by \(f_r\), and multiplying \(f\) by homogeneous polynomials realizes all such homogeneous multiples. The kernel computation in Theorem 7.1 therefore gives \(\operatorname{gr}(A/(f))=k[X,Y]/(f_r)\). Multiplication by \(f_r\) in the polynomial domain is injective, so the degree-\(j\) dimension is \(\min(j+1,r)\). Summation gives \(rn-r(r-1)/2\) eventually, with degree one and multiplicity \(r\). For \(x^3+x^2y+y^5\), the nonzero lowest part is \(X^3+X^2Y\), of degree three in every characteristic, so the multiplicity is three. Its eventual function is \(3n-3\), valid for \(n\geq2\). The nonzero nonunit hypotheses ensure that this argument concerns a nonzero plane hypersurface local ring.

**Solution 9.5.** The quotient kernel is \(M'/(M'\cap I^nM)\). Artin–Rees bounds its length between \(H_{I,M'}(n-c)\) and \(H_{I,M'}(n)\); adding the quotient-module length gives (16). Write the end polynomials in their largest occurring degree \(d\), assigning coefficient zero to any end of smaller degree. Translating \(n\) to \(n-c\) preserves that degree's coefficient. Divide (16) by \(n^d\) and take the limits of these polynomial expressions; for \(d=0\) the expressions are eventual constants and the same conclusion holds. The middle leading coefficient equals the sum of the end coefficients. Multiplying by \(d!\) proves (17). If both ends vanish, every module vanishes and there is no nonnegative degree to consider.

Now put \(B=k[t]_{(t)}\) and \(I=(t)\). Multiplication by \(t\) identifies the module \((t)\) with \(B\). Thus for \(n\geq1\), \(H_{I,(t)}(n)=n\), \(H_{I,B}(n)=n\), and \(H_{I,k}(n)=1\). The sum of the end polynomials is \(n+1\), not \(n\). Nevertheless their degree-one coefficients give \(1=1+0\), as required. The induced submodule filtration is
\[
(t)\cap I^nB=(t^n),
\]
whereas \(I^n(t)=(t^{n+1})\). The induced quotient \((t)/(t^n)\) has length \(n-1\), including zero at \(n=1\). Its length plus that of \(k\) is exactly \(n\). The discrepancy is the filtration, not a failure of length additivity.

**Solution 9.6.** The monomial \(u^a\) has degree \(2a\), so the function is one in nonnegative even degrees and zero in odd degrees. If an eventual polynomial \(P\) existed, it would vanish at all sufficiently large odd integers, forcing \(P=0\); its values at the even integers contradict this. The cumulative function counts nonnegative even integers strictly below \(n\), so is \(\lceil n/2\rceil\). It too is not eventually polynomial: on even integers it equals \(n/2\), which would force that polynomial everywhere, but its odd values differ by \(1/2\). Each residue class modulo two has a polynomial formula. Degree-one generation removes this periodic obstruction and is the hypothesis used by the difference step (3).

## References

- The Stacks project authors, *The Stacks project*, graded finiteness [Tag 00JW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-graded-Noetherian), numerical polynomials [Tag 00JX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-numerical-polynomial), [Tag 00JZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-numerical-polynomial), and Hilbert–Serre [Tag 00K1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-graded-hilbert-polynomial).
- The same work, ideals of definition [Tag 07DU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-ideal-definition), Hilbert–Samuel polynomial [Tag 00K8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-hilbert-function-polynomial), degree independence [Tag 00K9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-d-independent), exact-sequence degree [Tag 00KC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-hilbert-ses-chi), and Rees algebras [Section 052P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-section-blow-up). These links use the AI Integrated Stacks Project English reader described in the course introduction.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Section 18.6, for the projective Hilbert-polynomial comparison and hypersurface calculation. [Author's public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).

