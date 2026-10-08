# Dimension theory of Noetherian local rings

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Original text: public domain (CC0). The example of Section 8 follows a construction presented in the Stacks Project, cited at the end.*

A prime chain measures how many successive specializations a space permits. A Hilbert–Samuel function measures how quickly its infinitesimal neighborhoods grow. A system of parameters measures how many equations are needed to isolate the closed point. For a Noetherian local ring, these three measurements agree. This is the bridge from the counting arguments of the preceding lesson to Krull’s height theorems.

We use the length and growth results of Graded modules and Hilbert–Samuel functions, and the chain conventions of Krull dimension and Noether normalization. Earlier tools used explicitly are finite prime filtrations and prime avoidance, Nakayama’s lemma, and going down for flat maps. All rings are commutative with identity. A local ring has one maximal ideal and is nonzero; it is not assumed Noetherian merely by being called local. A finite module means a finitely generated module.

For a Noetherian local ring \((R,\mathfrak m,\kappa)\), write
\[
H_M(n)=\ell_R(M/\mathfrak m^nM),\qquad d(M)=\deg P_M,
\tag{1}
\]
where \(P_M(n)=H_M(n)\) for large \(n\). The preceding lesson proves existence, a finite degree for nonzero finite \(M\), and independence of the ideal of definition. Put \(d(0)=-\infty\). Dimension of an empty spectrum or support is also \(-\infty\).

## 1. Growth bounds every prime chain

We first extract the precise consequence of leading-coefficient additivity that makes the dimension argument work.

**Lemma 1.1.** Let \(M\neq0\) be finite over a Noetherian local ring. If \(x\in\mathfrak m\) acts injectively on \(M\), then
\[
d(M/xM)<d(M).
\tag{2}
\]

**Proof.** Nakayama’s lemma, Theorem 4.2 of *Localization, local properties and support*, gives \(M/xM\neq0\). The exact sequence
\[
0\longrightarrow M\xrightarrow{x}M\longrightarrow M/xM\longrightarrow0
\]
and Theorem 6.1 of the preceding lesson give \(d(M/xM)\leq d(M)\). If equality held, its top-coefficient formula (17), with the ideal \(\mathfrak m\), would say
\[
e_{\mathfrak m}(M)=e_{\mathfrak m}(M)+e_{\mathfrak m}(M/xM).
\]
The last multiplicity is strictly positive, a contradiction. Thus (2) holds. In particular, an injective such \(x\) cannot occur on a nonzero module of degree zero. \(\square\)

If \(B=R/J\), its maximal ideal is \(\mathfrak m/J\), and its Hilbert–Samuel quotients are the same modules whether viewed over \(R\) or \(B\). Their submodule lattices, simple factors and lengths agree. Consequently the degree \(d_R(B)\) in (1) equals the ring degree \(d(B)\). We will use this identification for every local quotient.

**Proposition 1.2.** Every Noetherian local ring satisfies
\[
\dim R\leq d(R)<\infty.
\tag{3}
\]

**Proof.** Induct on the nonnegative integer \(d(R)\), simultaneously for all Noetherian local rings. When it is zero, Corollary 6.2 of the preceding lesson says that \(R\) has finite length. It is Artinian, so all its primes are maximal by Theorem 4.2 of *Noetherian and Artinian rings*. Its unique prime is therefore \(\mathfrak m\), and its dimension is zero.

Suppose the assertion is known for smaller degrees. Consider any strict chain
\[
\mathfrak p_0\subsetneq\mathfrak p_1\subsetneq\cdots\subsetneq\mathfrak p_l
\tag{4}
\]
in \(R\). A chain of length zero already satisfies the desired bound. For \(l\geq1\), put \(B=R/\mathfrak p_0\). This is a nonzero Noetherian local domain. The degree maximum theorem applied to \(0\to\mathfrak p_0\to R\to B\to0\) gives \(d(B)\leq d(R)\).

Choose \(x\in\mathfrak p_1\setminus\mathfrak p_0\). Its image in \(B\) is nonzero, belongs to the maximal ideal, and acts injectively because \(B\) is a domain. Lemma 1.1 shows that
\[
C=R/(\mathfrak p_0+(x))\quad\text{satisfies}\quad d(C)<d(B)\leq d(R).
\]
The ring \(C\) is nonzero since its defining ideal lies in \(\mathfrak p_1\). The induction hypothesis applies to \(C\). The images of \(\mathfrak p_1,\ldots,\mathfrak p_l\) form a strict chain in \(C\) of length \(l-1\). Hence
\[
l-1\leq\dim C\leq d(C)\leq d(R)-1,
\]
so \(l\leq d(R)\). Taking the supremum over all finite chains proves (3). No finite-dimensionality assumption entered the induction. \(\square\)

In particular, every prime of a Noetherian ring has finite height: apply (3) to \(R_{\mathfrak p}\), whose dimension is \(\operatorname{ht}\mathfrak p\). The whole ring can nevertheless have infinite dimension if these finite heights are unbounded.

## 2. Dimension, growth and parameter count

An *ideal of definition* of \((R,\mathfrak m)\) is an ideal \(I\) with \(\sqrt I=\mathfrak m\). In the Noetherian local case, this is equivalent to
\[
\mathfrak m^a\subseteq I\subseteq\mathfrak m
\quad\text{for some }a\geq1.
\tag{5}
\]
This characterization and finiteness of \(\ell_R(R/I)\) are proved at the start of Section 4 of the preceding lesson, using Proposition 2.2 and Theorem 4.2 of Noetherian and Artinian rings. Let \(\delta(R)\) be the least number of elements that generate an ideal of definition. It is finite because \(\mathfrak m\) is finitely generated. The ideal \((0)\) is generated by the empty list.

**Theorem 2.1 (local dimension theorem).** For every Noetherian local ring,
\[
\boxed{\dim R=d(R)=\delta(R).}
\tag{6}
\]

**Proof.** The Hilbert–Samuel degree bound in Theorem 4.2 of the preceding lesson says that an ideal of definition generated by \(r\) elements gives \(d(R)\leq r\). Thus \(d(R)\leq\delta(R)\). Proposition 1.2 gives \(\dim R\leq d(R)\).

It remains to construct an ideal of definition with at most \(D=\dim R\) generators. We can now induct on the finite integer \(D\). If \(D=0\), the only prime is \(\mathfrak m\), so \(\sqrt{(0)}=\mathfrak m\), and the empty list works.

Suppose \(D>0\). There are finitely many minimal primes \(\mathfrak q_1,\ldots,\mathfrak q_s\), by Proposition 2.2 of *Noetherian and Artinian rings*. None equals \(\mathfrak m\): if \(\mathfrak m\) were minimal, every prime contained in it would equal it, giving dimension zero. Finite prime avoidance, proved in Solution 8.5 of *Associated primes and primary decomposition*, therefore supplies
\[
x\in\mathfrak m\setminus\bigcup_{j=1}^s\mathfrak q_j.
\tag{7}
\]
Every chain in \(R/xR\) corresponds to a chain in \(R\) whose bottom prime \(\mathfrak p\) contains \(x\). Choose a minimal prime \(\mathfrak q\subseteq\mathfrak p\). Such a prime exists by Lemma 4.2 of *Spectra of rings*. Since \(x\notin\mathfrak q\), the containment \(\mathfrak q\subsetneq\mathfrak p\) is strict. Prepending it extends the chain by one. Thus
\[
\dim(R/xR)\leq D-1.
\tag{8}
\]
By induction, the quotient has an ideal of definition generated by at most \(D-1\) elements. Lift these generators to \(R\) and adjoin \(x\). The resulting ideal has radical \(\mathfrak m\), as follows directly from the quotient prime correspondence, and has at most \(D\) generators. Hence \(\delta(R)\leq\dim R\). The three inequalities yield (6). \(\square\)

The argument is useful because it gives an existence theorem over every residue field. Choosing parameters requires avoiding finitely many prime ideals, rather than choosing a generic scalar from an infinite field.

**Corollary 2.2 (the module dimension promised by the growth theory).** For every finite module \(M\) over a Noetherian local ring,
\[
d(M)=\dim\operatorname{Supp}M.
\tag{9}
\]
For \(M\neq0\), this also equals \(\dim(R/\operatorname{ann}_R M)\).

**Proof.** The zero case is our convention. For \(M\neq0\), Theorem 2.2 of *Associated primes and primary decomposition* gives a finite prime filtration whose successive factors are \(R/\mathfrak p_i\). Repeated use of the degree maximum theorem gives
\[
d(M)=\max_i d(R/\mathfrak p_i)=\max_i\dim(R/\mathfrak p_i),
\]
the second equality being Theorem 2.1. Localization of each exact sequence shows that
\(\operatorname{Supp}M=\bigcup_iV(\mathfrak p_i)\). A finite closed union has dimension the maximum of its members’ dimensions, as proved in Section 1 of *Krull dimension and Noether normalization*. This proves (9). The support of a finite module is \(V(\operatorname{ann}M)\), by Proposition 6.1 of *Localization, local properties and support*, giving the last assertion. \(\square\)

## 3. How much can one equation cut?

**Theorem 3.1 (Krull’s height theorem).** Let \(R\) be Noetherian, let \(J=(f_1,\ldots,f_r)\), and let \(\mathfrak p\) be a prime minimal among those containing \(J\). Then
\[
\operatorname{ht}\mathfrak p\leq r.
\tag{10}
\]
For \(r=1\), this is Krull’s principal ideal theorem. For \(r=0\), it says that minimal primes have height zero.

**Proof.** Set \(A=R_{\mathfrak p}\). Primes of \(A\) containing \(JA\) correspond to primes of \(R\) between \(J\) and \(\mathfrak p\). Minimality leaves only \(\mathfrak pA\). Thus \(JA\) is an ideal of definition, with at most \(r\) generators. By Theorem 2.1 and the height–localization identity,
\[
\operatorname{ht}\mathfrak p=\dim A=\delta(A)\leq r.
\]
This includes the empty generating list. \(\square\)

There is also an interval version: if \(\mathfrak q\) is minimal over \(\mathfrak p+(f_1,\ldots,f_r)\), apply the theorem in \(R/\mathfrak p\) to obtain \(\operatorname{ht}(\mathfrak q/\mathfrak p)\leq r\). Without additional hypotheses, do not replace this interval height by \(\operatorname{ht}\mathfrak q-\operatorname{ht}\mathfrak p\).

**Theorem 3.2 (one equation in a local ring).** If \(R\) is Noetherian local and \(x\in\mathfrak m\), then
\[
\dim(R/xR)\geq\dim R-1.
\tag{11}
\]
If \(x\) belongs to no minimal prime of \(R\), then equality holds. In particular, equality holds when \(x\) is a nonzerodivisor.

**Proof.** Let \(e=\dim(R/xR)\). By Theorem 2.1, choose \(e\) generators of an ideal of definition in the quotient. Their lifts, together with \(x\), generate an ideal of definition of \(R\). Therefore \(\dim R=\delta(R)\leq e+1\), proving (11).

If \(x\) avoids every minimal prime, the chain-prepending argument proving (8) gives \(e\leq\dim R-1\). This proves equality. Finally, minimal primes of a Noetherian ring are associated to its ring module, by Theorem 3.2 of *Associated primes and primary decomposition*. Its Theorem 1.2 says that the union of associated primes is the set of zero divisors. A nonzerodivisor consequently avoids every minimal prime. \(\square\)

Both the properness condition \(x\in\mathfrak m\) and the avoidance condition matter. A unit gives the zero quotient. An element lying in a minimal prime can leave a whole component uncut. For example, in \(k[x,y]_{(x,y)}/(xy)\), quotienting by \(x\) leaves \(k[y]_{(y)}\), so dimension stays one.

## 4. Parameters and embedding dimension

A *system of parameters* of a Noetherian local ring of dimension \(D\) is a list \(x_1,\ldots,x_D\in\mathfrak m\) whose ideal has radical \(\mathfrak m\). Theorem 2.1 proves that such lists exist. In dimension zero the empty list is a system of parameters.

**Proposition 4.1.** If \(x_1,\ldots,x_D\) is a system of parameters, then for every \(0\leq i\leq D\),
\[
\dim\bigl(R/(x_1,\ldots,x_i)\bigr)=D-i.
\tag{12}
\]
More generally, a list of \(i\) elements of \(\mathfrak m\), where \(i\leq D\), extends to a system of parameters exactly when its quotient has dimension \(D-i\).

**Proof.** Write \(B=R/(x_1,\ldots,x_i)\) and \(e=\dim B\). The remaining \(D-i\) parameters give an ideal of definition in \(B\), so \(e\leq D-i\). Conversely, lift an \(e\)-element system of parameters of \(B\) and adjoin the first \(i\) elements. Its radical is \(\mathfrak m\), hence \(D=\delta(R)\leq i+e\). This proves (12).

For any list of \(i\) elements, the same lifting argument gives \(e\geq D-i\). If equality holds, the lifted \(e\)-element list completes it to a system of parameters. The converse follows from (12). \(\square\)

The *embedding dimension* is
\[
\operatorname{embdim}R=\dim_\kappa(\mathfrak m/\mathfrak m^2).
\tag{13}
\]
It measures the number of independent first-order directions at the closed point.

**Proposition 4.2.** The embedding dimension is the minimum number of generators of \(\mathfrak m\), and
\[
\dim R\leq\operatorname{embdim}R.
\tag{14}
\]

**Proof.** Any generating list of \(\mathfrak m\) maps to a spanning list of \(\mathfrak m/\mathfrak m^2\). Conversely, choose lifts \(u_1,\ldots,u_e\) of a vector-space basis and put \(J=(u_1,\ldots,u_e)\). The relation \(\mathfrak m=J+\mathfrak m^2\) says that the finite module \(\mathfrak m/J\) equals its product with \(\mathfrak m\). Nakayama makes it zero. Thus the lifts generate \(\mathfrak m\), proving the minimum assertion. Since \(\mathfrak m\) itself is an ideal of definition, Theorem 2.1 gives (14). \(\square\)

A Noetherian local ring is *regular* when equality holds in (14). A minimum generating list of its maximal ideal is then called a *regular system of parameters*. In dimension zero this definition says precisely that the ring is a field: embedding dimension zero makes \(\mathfrak m=0\) by Nakayama. We will prove the stronger structural properties of regular local rings in *Regular local rings*.

## 5. Base dimension and fibre dimension

**Theorem 5.1 (local dimension formula).** Let \(R\to S\) be a map of Noetherian rings. For \(\mathfrak q\in\operatorname{Spec}S\) contracting to \(\mathfrak p\in\operatorname{Spec}R\),
\[
\dim S_{\mathfrak q}\leq
\dim R_{\mathfrak p}+\dim(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}).
\tag{15}
\]
Equality holds if the map satisfies going down, in particular if it is flat. No finite-type assumption is required.

**Proof of the upper bound.** Replace the rings by the local map \((A,\mathfrak m)\to(B,\mathfrak n)=(R_{\mathfrak p},\mathfrak pR_{\mathfrak p})\to(S_{\mathfrak q},\mathfrak qS_{\mathfrak q})\). The ring \(C=B/\mathfrak mB\) is nonzero Noetherian local. Put \(d=\dim A\) and \(e=\dim C\). Choose base parameters \(x_1,\ldots,x_d\) and lift fibre parameters \(\bar y_1,\ldots,\bar y_e\) to \(y_j\in\mathfrak n\). Consider
\[
K=(x_1,\ldots,x_d,y_1,\ldots,y_e)B.
\tag{16}
\]
If a prime of \(B\) contains \(K\), it contains \(\mathfrak mB\): some \(\mathfrak m^a\) lies in the base parameter ideal, so the image of every element of \(\mathfrak m\) has a power in that prime. In \(C\), the prime then contains all the fibre parameters and hence is the maximal ideal. Its inverse image is \(\mathfrak n\). Thus \(\sqrt K=\mathfrak n\). Theorem 2.1 gives \(\dim B\leq d+e\), which is (15).

**Proof of equality with going down.** Since all three local dimensions are finite, their supremal chain lengths are attained. Choose a length-\(e\) chain in \(C\) ending at its maximal ideal; a chain of maximum length must end there. Its inverse image in \(B\) is
\[
\mathfrak q_0\subsetneq\cdots\subsetneq\mathfrak q_e=\mathfrak n.
\]
Every member contracts to \(\mathfrak m\), because it contains \(\mathfrak mB\). Choose a length-\(d\) chain \(\mathfrak p_0\subsetneq\cdots\subsetneq\mathfrak p_d=\mathfrak m\) in \(A\). Starting at \(\mathfrak q_0\), repeated going down lifts this base chain below it. The lifted inclusions are strict since the contractions differ. Append the original fibre chain. The combined chain in \(B\) has length \(d+e\), so \(\dim B\geq d+e\).

Going down passes to the indicated localizations by prime correspondence. Flat maps satisfy it by Theorem 6.3 of *Tor and flat modules*, and their localizations remain flat. This proves the equality claims. \(\square\)

The fibre term is the dimension of the local ring at the selected point of \(\operatorname{Spec}(S\otimes_R\kappa(\mathfrak p))\). Elements outside \(\mathfrak p\) are already inverted in \(S_{\mathfrak q}\), so this fibre’s local ring is exactly \(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}\).

## 6. Polynomial rings over Noetherian bases

**Theorem 6.1.** For any Noetherian ring \(R\) and \(n\geq0\),
\[
\dim R[T_1,\ldots,T_n]=\dim R+n.
\tag{17}
\]
Here \(\infty+n=\infty\) and \(-\infty+n=-\infty\), so the statement includes rings of infinite dimension and the zero ring.

**Proof.** First consider one variable. For an arbitrary ring \(R\), any strict chain \(\mathfrak p_0\subsetneq\cdots\subsetneq\mathfrak p_l\) extends to
\[
\mathfrak p_0R[T]\subsetneq\cdots\subsetneq\mathfrak p_lR[T]
\subsetneq\mathfrak p_lR[T]+(T).
\tag{18}
\]
Every extended ideal is prime because its quotient is \((R/\mathfrak p_i)[T]\), a domain. The last quotient is \(R/\mathfrak p_l\), also a domain. Strictness of the extended inclusions follows by contracting to \(R\), and the last one is strict because \(T\notin\mathfrak p_lR[T]\). Thus
\[
\dim R[T]\geq\dim R+1
\tag{19}
\]
for every ring, interpreting unbounded finite chains and the empty spectrum as above.

Now let \(R\) be Noetherian. Hilbert’s basis theorem makes \(R[T]\) Noetherian. It is free over \(R\), with basis \(1,T,T^2,\ldots\), hence flat. For a prime \(P\) above \(\mathfrak p\), Theorem 5.1 gives
\[
\operatorname{ht}P=\operatorname{ht}\mathfrak p+
\dim\bigl(\kappa(\mathfrak p)[T]_{\bar P}\bigr)
\leq\operatorname{ht}\mathfrak p+1.
\tag{20}
\]
The fibre identification follows by first localizing \(R\) at \(\mathfrak p\), reducing modulo \(\mathfrak p\), and then localizing at the corresponding fibre prime \(\bar P\). A polynomial ring in one variable over a field is a PID: its zero prime has height zero and its nonzero primes have height one. This justifies both the inequality and the fact that the last dimension is either zero or one. For \(P=\mathfrak pR[T]+(T)\), it is one.

Taking suprema of (20) gives \(\dim R[T]\leq\dim R+1\); together with (19) this gives equality. This step does not require a prime of height \(\dim R\) when \(\dim R=\infty\). If \(R=0\), both spectra are empty and the formula is immediate. Iterating the one-variable result proves (17), with each intermediate ring Noetherian. \(\square\)

## 7. Four local calculations

**Formal plane.** The ring \(A=k[[x,y]]\) is Noetherian by the coefficientwise formal-series argument in Solution 7.3 of *Noetherian and Artinian rings*, iterated from \(k\). A series is a unit exactly when its constant coefficient is nonzero: the inverse is obtained by a geometric-series expansion in the ideal \((x,y)\). Thus \(A\) is local with maximal ideal \(\mathfrak n=(x,y)\).

The ideal \(\mathfrak n^j\) consists exactly of series with no monomial of total degree below \(j\). Indeed, distribute the monomials of such a series among the finitely many degree-\(j\) monomials that divide them; each group is that monomial times a series. Consequently the degree-\(j\) layer has basis \(x^jy^0,\ldots,x^0y^j\), and
\[
\ell_A(A/\mathfrak n^n)=\sum_{j=0}^{n-1}(j+1)=\frac{n(n+1)}2.
\tag{21}
\]
Theorem 2.1 gives \(\dim A=2\). The degree-one layer has basis \(x,y\), so the embedding dimension is two. The ring is regular, with parameters \(x,y\).

**Cusp and node.** For \(k[x,y]_{(x,y)}/(y^2-x^3)\), and for \(k[x,y]_{(x,y)}/(y^2-x^2)\), Theorem 7.1 of the preceding lesson computes
\(H(n)=2n-1\) for \(n\geq1\). Their dimension is one by (6). Each equation lies in \((x,y)^2\), so imposing it introduces no relation in \((x,y)/(x,y)^2\); the embedding dimension stays two. Neither ring is regular. The second equation describes the usual two distinct tangent branches when \(\operatorname{char}k\neq2\). In characteristic two the same dimension calculation holds, but the equation is a square and does not describe that node.

**Quadric surface.** Put
\[
B=\bigl(k[x,y,z]/(xy-z^2)\bigr)_{(x,y,z)}.
\tag{22}
\]
Monic division in \(z\) makes \(k[x,y,z]/(xy-z^2)\) a free \(k[x,y]\)-module with basis \(1,z\). Thus the local map \(k[x,y]_{(x,y)}\to B\) is flat, by base change and localization. The base dimension is two by the field polynomial height formula of the preceding dimension lesson. Its closed fibre is \(k[z]/(z^2)\), already local and Artinian, so has dimension zero. Theorem 5.1 gives \(\dim B=2\).

The quotient by \((x,y)\) is \(k[z]/(z^2)\), so \(x,y\) is a system of parameters. The quotient by \((x,z)\) is \(k[y]_{(y)}\), of dimension one. Thus \(x,z\) fails to isolate the closed point and is not a system of parameters.

**Arithmetic surface.** Let \(p\) be a prime integer and put
\[
A=\mathbb Z_{(p)}[x]_{(p,x)}.
\tag{23}
\]
The base \(\mathbb Z_{(p)}\) has the chain \((0)\subsetneq(p)\) and dimension one. The map to \(A\) is flat, and the closed fibre is \(\mathbb F_p[x]_{(x)}\), also of dimension one. Therefore \(\dim A=2\). Its maximal ideal is generated by \(p,x\), so (14) forces its embedding dimension to be exactly two. It is regular with regular parameters \(p,x\).

## 8. A noncatenary Noetherian local ring

The height theorem gives a finite bound on prime chains in a Noetherian local ring. It does not make every saturated chain between fixed endpoints have the same length. We construct the counterexample, following Nagata's example as presented in AI Integrated Stacks Project, and supply the verifications needed for this conclusion.

**Lemma 8.1 (two local branches).** There is a Noetherian semilocal domain \(B\) over \(k=\mathbb Q\) with exactly two maximal ideals \(\mathfrak m_B,\mathfrak n_B\), residue field \(k\) at both, and local dimensions one and two respectively.

**Proof.** Choose \(z=\sum_{i\ge1}a_i x^i\in k[[x]]\) transcendental over \(k(x)\). Such a series exists: \(k(x)\) and its set of polynomials are countable, so the elements of \(k((x))\) algebraic over it form a countable set, whereas binary coefficient sequences give an uncountable subset of \(xk[[x]]\), by Cantor's diagonal argument. Put
\[
z_j=x^{-j}\left(z-\sum_{i<j}a_i x^i\right),
\qquad R=k[x,z_1,z_2,\ldots]\subset k[[x]].
\tag{17a}
\]
The relations are \(z_j=a_j+xz_{j+1}\), and \(z=xz_1\). Each \(k[x,z_j]\) is a polynomial ring in two independent elements, by transcendence of \(z\), and \(R\) is their increasing union with the indicated substitutions. Modulo \(x\), every \(z_j\) becomes \(a_j\), so \(\mathfrak m=(x)\) is maximal with residue \(k\). The local ring \(R_{\mathfrak m}\) embeds in \(k[[x]]\). A nonzero element whose constant term is zero lies in \(xR_{\mathfrak m}\), while a nonzero constant term makes it a unit. Dividing repeatedly by \(x\) ends after its finite power-series order. Thus every nonzero element is \(x^v\) times a unit, and every ideal is generated by its least occurring power of \(x\). This is a DVR of dimension one.

Modulo \(x-1\), each transition \(k[x,z_j]\to k[x,z_{j+1}]\) becomes the isomorphism \(k[z_j]\to k[z_{j+1}]\), \(z_j\mapsto a_j+z_{j+1}\). Since quotients commute with these directed unions, \(R/(x-1)=k[z]\), where \(z=xz_1\) has residue \(z_1\). Hence \(\mathfrak n=(x-1,z)\) is another maximal ideal with residue \(k\). Inverting \(x\) gives \(R_x=k[x,x^{-1},z]\), directly from (17a). Therefore
\[
R_{\mathfrak n}=k[x,x^{-1},z]_{(x-1,z)},
\]
a Noetherian local ring of dimension two: its maximal ideal has two generators, and \((0)\subset(z)\subset(x-1,z)\) has length two.

Let \(S=R\setminus(\mathfrak m\cup\mathfrak n)\), and \(B=S^{-1}R\). Finite prime avoidance shows that every prime disjoint from \(S\) lies in \(\mathfrak m\) or \(\mathfrak n\). Thus these give exactly the two maximal ideals of \(B\), with the local rings and residue fields just computed. For any ideal \(I\subset B\), choose finitely many numerators in \(I\) generating its localization at each of the two maximal ideals. Their combined ideal \(I_0\) has \((I/I_0)\) zero at every maximal ideal, hence is all of \(I\) by local detection. Every ideal is finite, so \(B\) is Noetherian. \(\square\)

**Lemma 8.2 (identifying the closed points).** Put \(J=\mathfrak m_B\cap\mathfrak n_B\) and \(A=k+J\subset B\). Then \(A\) is a two-dimensional Noetherian local domain with maximal ideal \(J\), and \(B\) is finite over \(A\) with the same fraction field.

**Proof.** Chinese remainder identifies \(B/J\) with \(k\times k\), and \(A/J\) with its diagonal \(k\). Choose \(\beta\in B\) with residues \((0,1)\). Subtracting the two residue components of any element shows \(B=A+A\beta\); hence it is finite over \(A\) and integral. For \(c+j\in A\), \(c\ne0\), its inverse in the semilocal ring \(B\) has residues \((c^{-1},c^{-1})\), hence lies in \(A\). Thus \(A\) is local with maximal ideal \(J\).

Here is a direct Noetherian proof, so no unproved finite-subring theorem is required. The ideal \(J\) is an ideal of \(B\), because it is the intersection of its maximal ideals, and it is contained in \(A\). Let \(I\) be a proper ideal of \(A\), so \(I\subset J\). The ideal \(BI\) is finite over the Noetherian ring \(B\). The submodule \(JBI\) is likewise finite over \(B\), hence finite over \(A\), since \(B\) is finite over \(A\). Moreover \(JBI\subset I\): write its terms as \(jbi\), with \(jb\in J\subset A\). The quotient \(BI/JBI\) is finite over \(B/J=k\times k\), so finite-dimensional over \(k\). Its subspace \(I/JBI\) is therefore finite-dimensional. Lift a basis and combine it with a finite \(A\)-generating set of \(JBI\); these generate \(I\). The whole ring ideal is generated by one. Thus \(A\) is Noetherian.

The ideal \(J\) contains a nonzero element, for example the image of \(x(x-1)\). For \(0\ne j\in J\) and \(b\in B\), we have \(jb\in J\subset A\), so \(b=(jb)/j\) belongs to \(\operatorname{Frac}A\). The fraction fields coincide. Integral inclusions preserve dimension, as proved in *Integral extensions*, Theorem 5.1; thus \(\dim A=\dim B=2\). \(\square\)

**Theorem 8.3 (noncatenarity).** The Noetherian local domain
\[
D=A[T]_{\mathfrak M},\qquad \mathfrak M=(J,T),
\tag{17b}
\]
has saturated chains of different lengths between its zero prime and maximal ideal.

**Proof.** Send \(T\) to \(\beta\) from Lemma 8.2. This gives a surjection \(A[T]\to B\) with prime kernel \(P\), contained in \(\mathfrak M\), since the residue of \(\beta\) at \(\mathfrak m_B\) is zero. Its contraction to \(A\) is zero. After inverting all nonzero elements of \(A\), the map is the evaluation \(K[T]\to K\) at \(\beta\), where \(K\) is the common fraction field. Its kernel is \((T-\beta)\), a height-one prime of the PID \(K[T]\). Every prime below \(P\) also contracts to zero, so the same localization proves that no prime lies strictly between \(0\) and \(P\). The kernel is nonzero because \(\beta\) is integral and has a monic relation. Also \(D/PD=B_{\mathfrak m_B}\), a DVR. Consequently
\[
(0)\subsetneq PD\subsetneq\mathfrak MD
\]
is saturated of length two.

On the other hand, take a nonzero prime \(\mathfrak r\subsetneq\mathfrak n_B\), which exists in the two-dimensional local branch. Its contraction \(\mathfrak a\) to \(A\) is nonzero: after inverting \(A\setminus\{0\}\), the integral domain \(B\) becomes the field \(K\), whose only prime is zero. It is strictly smaller than \(J\) by incomparability for the integral extension, applied to \(\mathfrak r\subsetneq\mathfrak n_B\). Thus
\[
(0)\subsetneq\mathfrak aA[T]\subsetneq JA[T]\subsetneq(J,T)
\]
is a length-three chain of primes. Localization at \(\mathfrak M\) preserves it. The finite dimension bound already proved here lets us extend it to a saturated chain, of length at least three. This differs from the saturated length-two chain with the same endpoints, proving noncatenarity. \(\square\)

Finite local dimension and the height theorem therefore do not justify subtracting endpoint heights along an arbitrary prime interval. The CM hypothesis in the following depth lesson will give a positive catenarity theorem.

Systems of parameters need not be regular sequences. Exercise 9.6 makes the distinction explicit. Depth, the Cohen–Macaulay condition, the stronger properties of regular local rings, and completion are developed in their later lessons. Every theorem assigned to the present lesson has been proved above.

## 9. Exercises

**Exercise 9.1 (easy).** Let \(\mathfrak p\) be a prime of a Noetherian ring generated as an ideal by \(r\) elements. Prove \(\operatorname{ht}\mathfrak p\leq r\). Explain why this is a statement about generators of the ideal, not the number of points of its spectrum.

**Exercise 9.2 (easy).** Compute the dimension and embedding dimension of \(k[x,y]_{(x,y)}/(y^2-x^3)\). Is this local ring regular?

**Exercise 9.3 (medium).** Let \(x\in\mathfrak m\) be a nonzerodivisor of a Noetherian local ring. Prove \(\dim(R/xR)=\dim R-1\). Show also that every prime minimal over \((x)\) in \(R\) has height exactly one.

**Exercise 9.4 (medium).** In the ring (22), prove that \(x,y\) is a system of parameters and \(x,z\) is not. Compute the dimensions after imposing only \(x\), then after imposing \(x,y\).

**Exercise 9.5 (hard).** For an arbitrary ring \(R\), prove \(\dim R[T]\geq\dim R+1\), including infinite and empty spectra. For Noetherian \(R\), prove that every prime \(P\) contracts to a prime \(\mathfrak p\) with \(\operatorname{ht}P\leq\operatorname{ht}\mathfrak p+1\). Determine exactly when the increment in height is zero or one using the fibre prime.

**Exercise 9.6 (hard).** Let \(R=k[x,y]_{(x,y)}/(x^2,xy)\), with maximal ideal \(\mathfrak m\). Compute its dimension and embedding dimension. Show that \(y\) is a parameter but a zero divisor. Compute \(\ell_R(R/\mathfrak m^n)\) for all \(n\geq1\) and its multiplicity. Explain why a parameter need not begin a regular sequence.

## 10. Solutions

**Solution 9.1.** The prime \(\mathfrak p\) is minimal among primes containing its own generating ideal: any prime containing that ideal contains \(\mathfrak p\) itself. Apply Theorem 3.1. Equivalently, localize at \(\mathfrak p\); its \(r\) generators generate the maximal ideal and hence an ideal of definition, so local dimension is at most \(r\). Neither reasoning counts points. For example, the principal prime \((0)\) in \(k[T]\) has height zero while its closed subset is the entire, potentially very large, spectrum.

**Solution 9.2.** The equation has order two. The preceding lesson’s plane-hypersurface calculation gives \(H(n)=2n-1\), so \(d(R)=1\). Theorem 2.1 gives \(\dim R=1\). With \(A=k[x,y]_{(x,y)}\) and \(\mathfrak n=(x,y)A\), the quotient cotangent space is
\[
\mathfrak m/\mathfrak m^2
\cong\mathfrak n/\bigl(\mathfrak n^2+(y^2-x^3)\bigr)
=\mathfrak n/\mathfrak n^2.
\]
The classes of \(x,y\) are a basis, so the embedding dimension is two. Since \(1<2\), the ring is not regular. This argument works in every characteristic.

**Solution 9.3.** Minimal primes are associated to \(R\). If \(x\) belonged to one, it would annihilate a nonzero element of \(R\), contradicting injectivity. Thus it avoids them all, and Theorem 3.2 gives the dimension formula. For a prime \(\mathfrak p\) minimal over \((x)\), the principal ideal theorem gives height at most one. Height zero would make it a minimal prime of \(R\): a nonminimal prime contains a minimal prime strictly, producing a chain of length one. This is impossible because \(x\in\mathfrak p\) avoids all minimal primes. Hence the height is one.

**Solution 9.4.** Section 7 proves \(\dim B=2\). Quotienting by \((x,y)\) gives the local Artinian ring \(k[z]/(z^2)\), whose only prime is \((z)\). Thus \(\sqrt{(x,y)B}\) is the maximal ideal, and the two-element list is a system of parameters. Quotienting by \((x,z)\) gives \(k[y]_{(y)}\), where the zero prime is strictly below \((y)\). Its dimension is one, so that pair does not define the closed point alone. After imposing just \(x\), the quotient is
\[
\bigl(k[y,z]/(z^2)\bigr)_{(y,z)}.
\]
Every prime contains \(z\), and reducing modulo \(z\) identifies its spectrum with \(\operatorname{Spec}k[y]_{(y)}\), preserving chains. Its dimension is one. After imposing \(x,y\), it is zero, as also required by (12).

**Solution 9.5.** Extend every finite prime chain of \(R\) coefficientwise and append the prime generated by its last extended ideal and \(T\), as in (18). Domain quotients verify primality, contraction verifies all earlier strict inclusions, and the nonzero class of \(T\) verifies the last one. For finite nonempty dimension \(D\), a length-\(D\) chain exists because a bounded nonempty set of nonnegative integers attains its supremum. This produces length \(D+1\). For infinite dimension, chains of unbounded finite lengths produce the required infinite supremum. An empty spectrum means \(R=0\), by maximal-ideal existence for nonzero rings, and \(R[T]=0\) too.

In the Noetherian case, apply the flat local formula to \(R\to R[T]\) at \(P\). It gives precisely (20). The corresponding prime \(\bar P\) of \(\kappa(\mathfrak p)[T]\) is either zero, when its local ring is the rational-function field and the increment is zero, or a nonzero principal prime, when its local ring has dimension one and the increment is one. The prime \(\mathfrak pR[T]+(T)\) realizes the second possibility for every \(\mathfrak p\). All these heights are finite, even if their global supremum is infinite.

**Solution 9.6.** Before localization, every class has a unique form \(f(y)+cx\), with \(f\in k[y]\) and \(c\in k\): the surviving monomials are \(1,y,y^2,\ldots,x\). This was also the embedded-point example in Section 7 of *Associated primes and primary decomposition*. Localization does not kill \(x\). Indeed, multiplying it by any polynomial outside \((x,y)\) multiplies it by a nonzero constant, since \(x^2=xy=0\).

Every prime contains the nilpotent \(x\). Reducing modulo it identifies the local spectrum with \(\operatorname{Spec}k[y]_{(y)}\), so dimension is one. Both defining equations lie in \((x,y)^2\); hence the classes of \(x,y\) remain independent in \(\mathfrak m/\mathfrak m^2\), and the embedding dimension is two. Quotienting by \(y\) leaves \(k[x]/(x^2)\), an Artinian local ring, so \(y\) is a one-element system of parameters. Yet \(yx=0\) with \(x\neq0\).

For \(n=1\), the quotient by \(\mathfrak m\) has length one. For \(n\geq2\), every product involving \(x\) and another generator vanishes, so \(\mathfrak m^n=(y^n)\). Its quotient has basis
\[
1,y,\ldots,y^{n-1},x.
\]
Localization introduces no further change: in this finite-dimensional quotient the ideal \((x,y)\) is nilpotent, so every element with nonzero constant term already has an inverse. A composition series over this local \(k\)-algebra has one-dimensional simple factors, and its length is its vector-space dimension. Therefore
\[
H_R(1)=1,\qquad H_R(n)=n+1\ (n\geq2),
\qquad e_{\mathfrak m}(R)=1.
\tag{24}
\]
The degree is one, agreeing with the prime-chain dimension. The first element of a regular sequence must act injectively on the ring; this parameter does not. Even multiplicity one here does not imply regularity.

## References

- The Stacks project authors, *The Stacks project*, Commutative Algebra: [Tag 00KQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-dimension), [Tag 00KU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-regular-local), [Tag 00KV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-minimal-over-1), [Tag 0BBZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-minimal-over-r), [Tag 00KW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-one-equation), [Tag 02IE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-elements-generate-ideal-definition), [Tag 00OM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-base-fibre-total), and [Tag 00ON](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-base-fibre-equals-total). These give the dimension theorem, parameters, height theorems and local base/fibre comparison. The tag links use the AI Integrated Stacks Project English reader described in the course introduction. The polynomial-ring theorem over a general Noetherian base is proved in Section 6.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Section 12.3, Krull’s theorems. [Author’s public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).

## Sources

The noncatenary example of Section 8 follows the construction presented by the Stacks Project authors in the examples chapter ([source at the pinned AI Integrated Stacks Project revision](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/examples.tex#L1410)). Its valuation, conductor and prime-chain verifications are supplied here; the conductor proof establishes Noetherianity directly.

## Licence

The text of this lesson is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). The Stacks Project, cited above for the arguments this lesson follows, is distributed by its authors under the GNU FDL 1.2 or later.
