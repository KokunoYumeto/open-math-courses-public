# Finite Lie-algebra tools for the receiving editions

*Written by GPT-6.1 Sol (OpenAI). Original text and proofs: CC0 1.0. Linked primary works keep their authors' copyrights; no licence for their prose is inferred.*

This companion precedes the four receiving editions of RT-LIE-03, 07, 08 and 11 used in KT–KK Lesson 18. It proves their actual imported algebraic tools without requiring a compact real form, Lie-group integration, the classification of root systems, or complete reducibility for general semisimple algebras. Lie algebras, modules and representations are finite dimensional unless expressly stated otherwise. Brackets are bilinear, alternating and satisfy Jacobi. A representation respects brackets. Sections 1–2 apply over the fields stated there; Section 3 is over an algebraically closed field of characteristic zero, and Section 4 allows arbitrary dimension in characteristic zero. Section 5 is real or complex finite matrix analysis.

The eligible comparisons are the actual freely accessible author editions of [Etingof's lecture notes](https://math.mit.edu/~etingof/lnlg.pdf), Sections 13–15 and 23; [Kirillov's notes](https://math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf), Theorem 2.29 for matrix exponentials and Sections 4.8 and 6.1–6.6 for algebra; and [Milne's notes, version 2.00](https://www.jmilne.org/math/CourseNotes/LAG.pdf), Chapter I, Sections 1–5. The proofs needed by the receiving editions are given below. Section 3 uses a direct extension-splitting argument, so it imports neither averaging over SU(2) nor Weyl's general complete-reducibility theorem. The matrix closed-subgroup argument in Section 5 is proved here using only the displayed series, contraction and limit calculations.

<a id="RTF-001"></a>
## 1. Engel's theorem and elementary ideal operations

Write \(L^{(0)}=L\), \(L^{(j+1)}=[L^{(j)},L^{(j)}]\), and \(L^1=L\), \(L^{j+1}=[L,L^j]\). Solvability means that a derived term is zero; nilpotence means that a lower-central term is zero. Jacobi proves that all these terms are ideals, and homomorphisms carry each term onto the corresponding term of their image. If \(I\) and \(L/I\) are solvable, a sufficiently late derived term of \(L\) lies in \(I\); further derivation kills it. Thus solvable extensions are solvable. In particular the sum of two solvable ideals is solvable, since \((I+J)/I\) is a quotient of \(J\). Finite dimensionality then gives a unique largest solvable ideal, the radical. Its last nonzero derived term is an abelian ideal of the whole algebra. Extension of the ground field commutes with forming brackets, derived terms and lower-central terms: expand elementary tensors and use bilinearity. Consequently it preserves and reflects their eventual vanishing.

**Theorem RTF-001 (Engel).** If \(V\ne0\) and \(L\subset\operatorname{End}(V)\) consists of nilpotent operators, a nonzero vector is killed by all of \(L\). There is a basis in which all operators of \(L\) are strictly upper triangular. An abstract finite-dimensional Lie algebra is nilpotent if every one of its adjoint operators is nilpotent. These statements hold over any field.

The lower-central estimate \([L^p,L^q]\subset L^{p+q}\) follows by induction and Jacobi: move the outer left factor of an element of \(L^p=[L,L^{p-1}]\) across the bracket, leaving the two smaller inductive brackets. Consequently \(L^{(j)}\subset L^{2^j}\), by induction on j. In particular every nilpotent algebra is solvable, a fact used below.

**Proof.** Induct on \(\dim L\), with zero algebra immediate. For a nilpotent matrix \(x\), its commutator operator on \(\operatorname{End}(V)\) is nilpotent: the expansion
\[
(\operatorname{ad}x)^N(T)=\sum_{j=0}^N(-1)^j\binom Nj x^{N-j}Tx^j
\]
vanishes for \(N\ge2r-1\) if \(x^r=0\). Choose a maximal proper subalgebra \(K\) of \(L\). Its action on \(L/K\) by commutators consists of nilpotent operators. Its represented dimension is smaller than \(\dim L\), so the induction supplies a nonzero fixed coset. A representative outside \(K\) normalizes \(K\). The normalizer is a subalgebra strictly larger than \(K\); maximality makes it \(L\), hence \(K\) is an ideal. If \(\dim L/K>1\), the inverse image of a one-dimensional subalgebra of \(L/K\) contradicts maximality. Therefore \(L=K+kx\).

The induction applied to \(K\) on \(V\) gives a nonzero common kernel \(W\). For \(a\in K\) and \(w\in W\), \(a(xw)=x(aw)+[a,x]w=0\), so \(xW\subset W\). A nilpotent operator on a nonzero finite space has a nonzero kernel, giving a vector in \(W\cap\ker x\). This proves the first assertion. Apply it successively to the quotient by the line obtained, lifting the quotient basis; nilpotence descends to quotients. The resulting flag has one-dimensional successive quotients with zero action, giving simultaneous strict triangularity.

Apply the represented assertion to \(\operatorname{ad}L\) on \(L\). In the resulting flag, each adjoint lowers the flag by one. A bracket with sufficiently many left factors therefore vanishes, exactly saying that a lower-central term of \(L\) is zero. The reverse implication follows since \((\operatorname{ad}x)^j(L)\subset L^{j+1}\). \(\square\)

<a id="RTF-002"></a>
## 2. Lie's theorem without a group representation

**Theorem RTF-002 (Lie).** Over an algebraically closed field of characteristic zero, every representation of a solvable finite-dimensional Lie algebra on a nonzero finite-dimensional space has a common eigenvector and a full invariant flag. Its represented derived algebra is strictly upper triangular in a flag basis.

**Proof.** Induct on the dimension of the algebra \(L\). If it is nonzero and solvable, \([L,L]\ne L\). Choose a codimension-one subspace \(K\) containing \([L,L]\); it is an ideal. The induction gives a vector \(v\ne0\) with \(av=\lambda(a)v\) for \(a\in K\), where \(\lambda\) is linear. Write \(L=K+kx\). On the cyclic space \(W=\operatorname{span}(v,xv,x^2v,\ldots)\), the formula
\[
a x^jv=x(a x^{j-1}v)+[a,x]x^{j-1}v
\]
proves inductively that each \(a\in K\) preserves the filtration by initial powers, with diagonal entries \(\lambda(a)\). The initial powers through their first dependence give a basis of \(W\), and \(x\) preserves it. Thus
\[
0=\operatorname{tr}_W[x,a]=(\dim W)\lambda([x,a]).
\]
Characteristic zero gives \(\lambda([x,a])=0\). The common \(K\)-eigenspace
\(V_\lambda=\{w:aw=\lambda(a)w\text{ for all }a\in K\}\)
is now \(x\)-invariant, since the same commutator identity shows \(a(xw)=\lambda(a)xw\). It is nonzero and the field is algebraically closed, so \(x\) has an eigenvector on it. That vector is a common eigenvector for \(L\). Induction on the dimension of \(V\), applied to its quotient by this eigenline, gives the full flag. Commutators of upper-triangular matrices have zero diagonal, proving the last assertion. \(\square\)

These two theorems, the ideal operations in Section 1, and polynomial finite-dimensional linear algebra suffice for the Cartan criteria in RT-LIE-03. No theorem about reductive algebraic groups is required.

<a id="RTF-003"></a>
## 3. Every finite rank-one module is a sum of the familiar strings

Let \(e,f,h\) satisfy \([h,e]=2e\), \([h,f]=-2f\), \([e,f]=h\).

**Theorem RTF-003.** Every finite-dimensional module is a direct sum of modules \(V(n)\), \(n\in\mathbb Z_{\ge0}\). The module \(V(n)\) has basis \(v_0,\ldots,v_n\) and actions
\[
h v_j=(n-2j)v_j,\quad f v_j=v_{j+1},\quad
e v_j=j(n-j+1)v_{j-1},
\]
with missing endpoint vectors interpreted as zero. Each \(V(n)\) is irreducible. Thus h is diagonalizable; its weights are integers, each string has multiplicity one, and raising and lowering are nonzero at every interior step.

**Proof of the irreducibles.** The relation \([h,e]=2e\) shifts generalized h-eigenspaces by two. There are only finitely many eigenvalues, so e is nilpotent. Its nonzero kernel is h-invariant and contains an h-eigenvector \(v\) with eigenvalue \(\lambda\). Direct induction on j from the three relations gives
\[
h f^jv=(\lambda-2j)f^jv,\qquad
e f^jv=j(\lambda-j+1)f^{j-1}v.
\tag{F.1}
\]
The nonzero vectors in this list have distinct eigenvalues. Finiteness gives a last one, \(f^nv\ne0\), with \(f^{n+1}v=0\). Applying e to the latter equation gives \((n+1)(\lambda-n)f^nv=0\), hence \(\lambda=n\). The span is a submodule. If the original module is irreducible, it is the whole module. Conversely any nonzero invariant subspace of the displayed model contains a weight component, because the spectral projections of h are polynomials in h. Raising to the top and lowering to the bottom gives every basis vector; thus the model is irreducible.

**Proof that extensions split.** The operator
\[
C=h^2+2h+4fe
\]
commutes with h, e and f, as expansion of the three commutators verifies. On \(V(n)\) it acts as \(c_n=n(n+2)\), first on the top vector and then on its generated span. Consider an extension of \(V(n)\) by \(V(m)\). If \(m\ne n\), then \(c_m\ne c_n\), and \((C-c_m)(C-c_n)=0\) on the extension. The two polynomial spectral projections split it into its \(c_m\)- and \(c_n\)-eigenspaces. The former is the kernel module, and the latter maps isomorphically onto the quotient, giving a complement.

For \(m=n\), choose a lift v of the top quotient vector in the generalized h-eigenspace of n. Such a lift exists by the polynomial generalized-eigenspace projections. Let u be the top vector of the kernel. The quotient relations and generalized eigenvalues give
\[
ev=0,\qquad(h-n)v=c u,\qquad f^{n+1}v=0
\]
for a scalar c: the kernel has no weights \(n+2\) or \(-n-2\). The operator identity
\[
e f^j=f^j e+j f^{j-1}(h-j+1)
\]
at \(j=n+1\) yields \(0=(n+1)c f^n u\), so c is zero. Formula (F.1) now shows that v generates a copy of \(V(n)\) mapping isomorphically onto the quotient. This also splits the extension.

For a general module choose an irreducible submodule U of smallest positive dimension. Induct on dimension to decompose the quotient into irreducibles. The inverse image of each quotient summand is an extension by U and splits by the preceding argument. Choose its complement. The sum of those chosen complements is direct and disjoint from U, because their quotient images are independent; its image is the entire quotient. Thus it is a complement to U. This completes the induction and the theorem. \(\square\)

This proof is purely algebraic and works over any algebraically closed characteristic-zero field. It supplies the decomposition used in RT-LIE-07's proportional-root submodule and nonproportional root strings, without first constructing a compact real form.

<a id="RTF-004"></a>
## 4. Ordered words and the free Lie algebra

**Theorem RTF-004 (the needed PBW statement).** For any characteristic-zero Lie algebra L, even of infinite dimension, fix a totally ordered vector-space basis \((x_i)\). In
\[
U(L)=T(L)/(xy-yx-[x,y]),
\]
the ordered words \(x_{i_1}\cdots x_{i_r}\), \(i_1\le\cdots\le i_r\), including the empty word, form a basis. In particular \(L\to U(L)\) is injective. The free Lie algebra on a vector space V embeds as the Lie subalgebra of \(T(V)\) generated by V.

**Proof.** Replace each adjacent inversion \(x_jx_i\), \(j>i\), by \(x_ix_j+[x_j,x_i]\), expanding the bracket in its finite basis support. Along each branch the pair (word length, inversion count) decreases lexicographically. Length is bounded by the original word length, and the inversion count at each length is bounded by its squared length, so every branch terminates after a uniformly finite number of steps. Each reduction has only finitely many branches.

Disjoint adjacent reductions commute. The only overlapping ambiguity has three descending letters x, y, z. Reduce first the left pair or first the right pair, exchange the remaining inversions, and subtract. Terms with three letters cancel; after replacing the remaining two-letter commutators the difference is
\[
[[x,y],z]+[[y,z],x]+[[z,x],y]=0.
\]
All intermediate terms in this comparison are smaller than the original ambiguous word. Induction on the finite reduction measure therefore proves independence of every choice of the next inversion: two first choices either commute or have the resolved three-letter overlap, and the smaller remaining choices agree by the induction. Extend the unique ordered reduction linearly.

Every defining relation, including one surrounded by any words on the left and right, reduces to zero; hence the reduction vanishes on the defining two-sided ideal. Conversely subtracting a word's normal form is a sum of defining relations with such contexts. The quotient is consequently exactly the vector space of ordered words, establishing both spanning and independence. Length-one words remain independent, proving the injection.

Construct the free Lie algebra F(V) from finite bracket expressions modulo bilinearity, alternation and Jacobi. Its defining property is immediate by evaluation of those expressions. The enveloping algebra U(F(V)) has the same universal property as T(V): a linear map from V to an associative algebra extends first to its commutator Lie algebra and then to the enveloping algebra. The resulting maps in both directions fix V, and V generates each algebra, so they are inverse. The just-proved injection of F(V) into its enveloping algebra identifies it with the Lie subalgebra of T(V) generated by V. \(\square\)

<a id="RTF-005"></a>
## 5. Matrix exponentials, local inversion and closed subgroups

**Theorem RTF-005.** A closed subgroup H of \(\operatorname{GL}_d(\mathbb R)\), or of \(\operatorname{GL}_d(\mathbb C)\) viewed as a real group, is an embedded Lie subgroup. Its Lie algebra is
\[
\mathfrak h=\{X:\exp(tX)\in H\text{ for every real }t\}.
\]
The exponential gives a local smooth chart from \(\mathfrak h\) onto H near its identity. If H is the automorphism group of a finite-dimensional real or complex Lie algebra, \(\mathfrak h\) is its derivation algebra. Exponentials of derivations preserve brackets.

**Local analytic facts.** The matrix exponential series and all its derivatives converge uniformly on bounded sets, by the scalar factorial majorant. Thus it is smooth, \(D\exp_0=I\), and \(\exp((s+t)X)=\exp(sX)\exp(tX)\) by multiplying absolutely convergent series. Conjugation carries \(\exp X\) to the exponential of the conjugate X.

Here is the finite-dimensional inverse theorem used below. For a smooth f with invertible derivative at a, translate and apply its derivative inverse so that \(f(0)=0\), \(Df(0)=I\). On a small closed ball \(B_r\), \(k(x)=x-f(x)\) is q-Lipschitz with \(q<1\), by integrating its derivative on line segments. For \(\|y\|<(1-q)r\), the map \(x\mapsto y+k(x)\) preserves \(B_r\). Its iterates are Cauchy, since successive distances form a geometric series; completeness gives their unique fixed point g(y). Subtracting fixed-point equations gives \(\|g(y)-g(z)\|\le(1-q)^{-1}\|y-z\|\). Taylor expansion now gives \(Dg(y)=Df(g(y))^{-1}\). The derivative is continuous, and differentiating this identity proves smoothness inductively. Hence f is a local smooth diffeomorphism. This applies in particular to the exponential at zero.

**The Lie algebra.** The set \(\mathfrak h\) is closed and stable under real scalar multiplication. For matrices X, Y, Taylor expansion on bounded sets gives
\[
(\exp(tX/n)\exp(tY/n))^n\longrightarrow\exp(t(X+Y)),
\]
and, for \(t\ge0\),
\[
\bigl(\exp(\sqrt{t/n}X)\exp(\sqrt{t/n}Y)
\exp(-\sqrt{t/n}X)\exp(-\sqrt{t/n}Y)\bigr)^n
\longrightarrow\exp(t[X,Y]).
\]
For completeness, the factors in the first line equal \(I+t(X+Y)/n+O(n^{-2})\); those in the second equal \(I+t[X,Y]/n+O(n^{-3/2})\). Comparing with the corresponding exponential factors, the identity \(P^n-Q^n=\sum_{j=0}^{n-1}P^j(P-Q)Q^{n-1-j}\) bounds the error by n times the one-step error times a uniform exponential bound. This tends to zero in each case. Closedness of H proves closure under sums and brackets; negative t in the bracket formula follows by inversion. Thus \(\mathfrak h\) is a real Lie subalgebra.

Choose a vector-space complement \(\mathfrak m\). The map \((X,Y)\mapsto\exp X\exp Y\), from \(\mathfrak h\oplus\mathfrak m\), has identity derivative at zero and hence is a local chart in the ambient matrix group. Near the identity, H contains no point \(\exp X\exp Y\) with \(Y\ne0\). Otherwise choose such points tending to the identity; then \(Y_j\to0\), \(\exp Y_j\in H\), and a subsequence of \(Y_j/\|Y_j\|\) converges to a unit vector \(Y\in\mathfrak m\). For each fixed real t choose integers \(r_j\) with \(r_j\|Y_j\|\to t\). Closedness gives
\(\exp(tY)=\lim(\exp Y_j)^{r_j}\in H\).
This puts Y in \(\mathfrak h\), a contradiction. The chart therefore identifies H with \(\mathfrak h\times\{0\}\) near the identity. Translation supplies embedded charts everywhere; group operations restrict smoothly. This proves the theorem about closed subgroups and their tangent algebra.

For the automorphism group, preservation of a bracket is a closed family of polynomial matrix equations inside GL. Differentiating \(\exp(tD)[u,v]=[\exp(tD)u,\exp(tD)v]\) at zero gives exactly the derivation rule. Conversely, for a derivation D the derivative of
\(\exp(-tD)[\exp(tD)u,\exp(tD)v]\)
is zero by that rule. Its value at zero is \([u,v]\), proving bracket preservation for every t. Therefore its tangent algebra is precisely the derivation algebra. The identity component is closed, has the same tangent algebra and inherits these charts. \(\square\)

This is the matrix case actually needed for the automorphism group in Lesson 18, Proposition 12.11. It also proves the matrix-group local exponential and closed-subgroup inputs of the compact-group receiving lessons. It does not assert that an arbitrary Lie group has a faithful finite-dimensional representation. The general closed-subgroup and flow theorems used elsewhere in Lesson 18 remain separate programme providers.
