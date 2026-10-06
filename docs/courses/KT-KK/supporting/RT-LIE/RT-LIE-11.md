# The isomorphism theorem and Serre's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*KT–KK receiving revision, 5 October 2026: the proofs used by Lesson 18 are rewritten from the checked free author editions and bound to the local companion. Original authorship and CC0 remain as stated above. The proof/source audit distinguishes this used chain from retained comparisons and unused later dependencies.*

A Dynkin diagram first records the relative positions of simple roots. It also tells us how many times one simple-root generator can be bracketed with another before the result is zero. We will show that these instructions determine every bracket of a semisimple Lie algebra, and that they construct an algebra for every finite Dynkin diagram.

The ground field is \(\mathbb C\). The used presentation proof takes its root decomposition and nonzero brackets from [RT-LIE-07, Sections 1–5](RT-LIE-07.md#RTLIE07-T21), arithmetic and base/reflection descent from [RT-LIE-08, Sections 1–4](RT-LIE-08.md#RTLIE08-L41), finite rank-one calculations from [RTF-003](RT-LIE-foundations.md#RTF-003), and the arbitrary-dimensional ordered-word/free-Lie statement from [RTF-004](RT-LIE-foundations.md#RTF-004). For Theorem 6.1, **finite type** means the Cartan matrix of a given finite reduced Euclidean root system. Its proof does not import the classification of all diagrams or Cartan conjugacy. The retained classification Corollary 6.2 additionally uses the separate [root-system classification provider](../../../RT-LIE/RT-LIE-09.html), and the statement about independence of the choice of Cartan additionally uses the separate [Cartan-conjugacy provider](../../../RT-LIE/RT-LIE-10.html). Those two imports are outside this receiving edition's checked Lesson-18 proof chain. The auxiliary algebra can be infinite-dimensional; no argument below assumes its finite dimension before proving it.

## 1. Read the generators from the root spaces

Choose a Cartan subalgebra \(\mathfrak h\), a base \(\Delta=\{\alpha_1,\ldots,\alpha_r\}\) of its roots, and nonzero vectors \(e_i\in\mathfrak g_{\alpha_i}\). Normalize \(f_i\in\mathfrak g_{-\alpha_i}\) so that
\[
[e_i,f_i]=h_i=\alpha_i^\vee,
\qquad [h_i,e_i]=2e_i,
\qquad [h_i,f_i]=-2f_i.
\tag{1.1}
\]
The coroot here is the element of \(\mathfrak h\) furnished by the Killing-dual construction. The \(h_i\) form a basis, since simple coroots form a base of the dual root system. Our convention is
\[
a_{ij}=\langle\alpha_i,\alpha_j^\vee\rangle
=\alpha_i(h_j).
\tag{1.2}
\]
Thus the index on the acting generator is the **second** index of a Cartan entry.

<a id="RTLIE11-P11"></a>
**Proposition 1.1 (Chevalley generators).** The \(e_i,f_i,h_i\) generate \(\mathfrak g\). They satisfy
\[
\begin{aligned}
[h_i,h_j]&=0,&
[h_i,e_j]&=a_{ji}e_j,&
[h_i,f_j]&=-a_{ji}f_j,\\
[e_i,f_j]&=\delta_{ij}h_i,&&&
\end{aligned}
\tag{1.3}
\]
and, for \(i\ne j\),
\[
(\operatorname{ad}e_i)^{1-a_{ji}}e_j=0,
\qquad
(\operatorname{ad}f_i)^{1-a_{ji}}f_j=0.
\tag{1.4}
\]

**Proof.** The root-space eigenvalue equations and normalization give the Cartan and same-index relations in (1.3). For different indices, \(\alpha_i-\alpha_j\) is forbidden by the same-sign basis property of RT-LIE-08, Theorem 2.1, so the mixed bracket is zero.

For positive nonsimple \(\beta=\sum b_i\alpha_i\), the equality \((\beta,\beta)=\sum b_i(\beta,\alpha_i)>0\) gives an i with positive coefficient and positive inner product. It is not proportional to \(\alpha_i\) by reducedness. The root string of RT-LIE-07, Theorem 4.1, has \(r-q=\beta(h_i)>0\), hence r is at least one: \(\beta-\alpha_i\) is a root. Subtracting one from its positive coefficient leaves a nonnegative expansion with smaller height. The same theorem gives
\[
[\mathfrak g_{\alpha_i},\mathfrak g_{\beta-\alpha_i}]=\mathfrak g_\beta.
\tag{1.5}
\]
Induct on positive integral height to generate every positive root line. Apply this argument to the opposite base for the negative lines. Their mixed brackets give the coroot basis, so these elements generate all of \(\mathfrak g\).

For \(i\ne j\), the root string through \(\alpha_j\) in direction \(\alpha_i\) has r=0: subtracting \(\alpha_i\) would give mixed signs. Thus \(q=-\alpha_j(h_i)=-a_{ji}\). Raising reaches its last root after q steps and vanishes at q+1; this is exactly the first relation in (1.4). The opposite string gives the negative relation. In particular the acting index i is the **column** index in \(a_{ji}\), and the exponent is \(1-a_{ji}\). \(\square\)

The choice of \(e_i\) is free up to a nonzero scalar, after which (1.1) determines \(f_i\). A presentation theorem must respect those choices; it cannot silently prescribe extra normalization on all other root vectors.

## 2. Separate formal generators before imposing the endpoints

Let \(A\) be the Cartan matrix of any finite reduced root system \(\Phi\), with chosen base \(\alpha_i\). For the presentation theorem a given such system suffices; the retained classification corollary makes the additional diagram-realization import. Write \(Q=\bigoplus_i\mathbb Z\alpha_i\) and \(Q_+=\bigoplus_i\mathbb Z_{\ge0}\alpha_i\). Take an abstract vector space \(H\) with basis \(h_i\), and define the linear forms \(\alpha_j\in H^*\) by \(\alpha_j(h_i)=a_{ji}\). The matrix is invertible: its Euclidean realization is the positive-definite Gram matrix of the simple roots multiplied by the invertible diagonal matrix with entries \(2/(\alpha_i,\alpha_i)\). Thus these \(\alpha_j\) form a basis of \(H^*\).

Define \(\widetilde{\mathfrak g}\) by generators \(e_i,f_i,h_i\) and only (1.3), leaving out (1.4). A Lie algebra given by generators and relations means a quotient of the free Lie algebra by the ideal of the stated relations. Free Lie algebras themselves can be constructed from formal bracket expressions modulo bilinearity, alternation and Jacobi; their universal property follows by evaluation of those expressions.

We need to know that this quotient has not accidentally introduced relations among the positive generators or collapsed \(H\). The following elementary separation fact will supply that check.

<a id="RTLIE11-L21"></a>
**Lemma 2.1 (free Lie expressions inside a tensor algebra).** The free Lie algebra on a vector space \(V\) embeds into its tensor algebra \(T(V)\), as the Lie subalgebra generated by \(V\) under commutators.

**Proof.** The full ordered-word proof, including arbitrary-dimensional bases, terminating reductions, disjoint and three-letter overlap checks, and independence in the quotient, is [RTF-004](RT-LIE-foundations.md#RTF-004). It injects every Lie algebra L into \(U(L)\). For the free algebra F(V), the universal property identifies \(U(F(V))\) with T(V): both algebra maps to an associative algebra are exactly the linear maps from V to that algebra. Their inverse maps fix V and its generated algebra. Under this identification the injection of F(V) has image the Lie subalgebra generated by V. This proves the stated separation before it is used below. \(\square\)

<a id="RTLIE11-P22"></a>
**Proposition 2.2 (the auxiliary triangular decomposition).** There is a direct decomposition
\[
\widetilde{\mathfrak g}
=\widetilde{\mathfrak n}^-\oplus H\oplus
\widetilde{\mathfrak n}^+,
\tag{2.2}
\]
where \(\widetilde{\mathfrak n}^+\) is free on the \(e_i\), \(\widetilde{\mathfrak n}^-\) is free on the \(f_i\), and the displayed \(h_i\) are linearly independent. The degrees are \(\deg e_i=\alpha_i\), \(\deg f_i=-\alpha_i\), \(\deg h_i=0\). There are no degrees outside \(Q_+\cup(-Q_+)\), and each nonzero-degree space is finite-dimensional.

**Proof of spanning.** All defining relations are homogeneous for the root-lattice grading. Pure positive and negative words are eigenvectors for H with their assigned degrees; Jacobi gives the sum of eigenvalues. A negative word can be written as a linear combination of words \([f_j,w]\), with w shorter, by repeatedly using Jacobi to put a generator at the left. The identity
\[
[e_i,[f_j,w]]=[[e_i,f_j],w]+[f_j,[e_i,w]]
\tag{2.3}
\]
proves by induction on negative length that a bracket of one positive generator with a negative word lies in that sum: length one gives a Cartan vector, and at longer length the Cartan term acts on a shorter negative word and the induction term brackets a negative generator with a negative or Cartan word. Equivalently its total height is at most zero, so no positive component can occur. For longer positive words use
\([[e_i,u],w]=[e_i,[u,w]]-[u,[e_i,w]]\)
and induction on positive word length, valid for negative words of every length, with (2.3) for its first step. In the first term, bracket the one generator with the negative, Cartan or positive components already found. In the second, (2.3) has produced negative or Cartan components, so the shorter positive word uses the induction. Cartan brackets preserve the spaces. Thus this sum is a subalgebra containing every generator, and is the whole auxiliary algebra.

**Proof of independence and freeness.** Let
\(M=T(\mathbb C\{F_1,\ldots,F_r\})\otimes\mathbb C[z_1,\ldots,z_r]\).
For a word w with letter-root sum \(\beta\), define
\[
\begin{aligned}
\mathcal F_j(w\otimes P)&=F_jw\otimes P,\\
\mathcal H_i(w\otimes P)&=w\otimes(z_i-\beta(h_i))P,\\
\mathcal E_i(1\otimes P)&=0,\\
\mathcal E_i(F_jw\otimes P)&=F_j\mathcal E_i(w\otimes P)
+\delta_{ij}\mathcal H_i(w\otimes P).
\end{aligned}
\tag{2.4}
\]
The last formula is a recursion on word length, so defines the operators on every finite word. The Cartan operators commute. Prepending \(F_j\) changes \(\beta\) by \(\alpha_j\), giving \([\mathcal H_i,\mathcal F_j]=-a_{ji}\mathcal F_j\). Each nonzero term of \(\mathcal E_j\) deletes one \(F_j\); comparing the Cartan scalar before and after this deletion gives \([\mathcal H_i,\mathcal E_j]=a_{ji}\mathcal E_j\). The recursion itself says \([\mathcal E_i,\mathcal F_j]=\delta_{ij}\mathcal H_i\). These are all auxiliary relations: no positive-positive or negative-negative relation has yet been imposed. Therefore the operators represent the auxiliary algebra.

On \(1\otimes1\), the Cartan generators give the independent polynomials \(z_i\), so H survives. A negative bracket word acts by left multiplication by the identical commutator expression in the tensor algebra. Its value on \(1\otimes1\), together with Lemma 2.1, proves injection of the negative free Lie algebra. The involution
\[
e_i\longleftrightarrow f_i,\qquad h_i\longmapsto-h_i
\tag{2.5}
\]
preserves every auxiliary relation and gives the positive injection. Positive words have strictly positive total height, negative words strictly negative, and H has degree zero. Their spanning sum is thus direct. A fixed multidegree uses a fixed finite number of letters and finitely many bracket patterns, so its space is finite-dimensional. The triangular decomposition also excludes all mixed-sign nonzero degrees. \(\square\)

## 3. A root-system isomorphism gives a Lie-algebra isomorphism

We can already prove uniqueness, before the finite-dimensional construction theorem.

**Theorem 3.1 (isomorphism theorem).** Let \(\mathfrak g,\mathfrak g'\) be complex semisimple algebras. An isomorphism of their root systems taking \(\alpha_i\) to \(\alpha_i'\) extends to a unique Lie-algebra isomorphism taking any chosen normalized \(e_i,f_i\) to the corresponding normalized \(e_i',f_i'\).

**Proof.** Root-system isomorphisms preserve all Cartan integers and coroots. The subalgebra \(L\subseteq\mathfrak g\oplus\mathfrak g'\) generated by
\((e_i,e_i')\) and \((f_i,f_i')\) also contains \((h_i,h_i')\), and satisfies the auxiliary relations (1.3). Proposition 2.2 gives its spanning decomposition into negative words, the diagonal Cartan span
\[
H_D=\operatorname{span}\{(h_i,h_i')\},
\]
and positive words. Those words have negative and positive root weights for the common Cartan action. Hence the common zero-weight subspace of \(L\) is exactly \(H_D\), and
\[
L\cap(\mathfrak h\oplus\mathfrak h')=H_D.
\tag{3.1}
\]
Both projections of \(L\) are onto by Proposition 1.1.

The subspace \(I=\{x\in\mathfrak g:(x,0)\in L\}\) is an ideal of \(\mathfrak g\): bracket \((x,0)\) with a lift in \(L\) of any element of \(\mathfrak g\). Every nonzero ideal of a semisimple algebra meets its Cartan subalgebra nontrivially. Here is the needed argument. It is stable under the commuting diagonalizable \(\operatorname{ad}H\), so polynomial spectral projections split it into its Cartan and root components. If a Cartan component is nonzero we are done. Otherwise it contains a nonzero vector in some one-dimensional \(\mathfrak g_\beta\). Bracketing with a nonzero opposite root vector gives the nonzero Killing-dual coroot direction in \(\mathfrak h\), still in the ideal.

But (3.1) prohibits any nonzero \((H,0)\) in \(L\): the second components of the basis of \(H_D\) are independent. Therefore \(I=0\). The same argument with the factors interchanged gives the other projection's kernel zero. Thus both projections are isomorphisms, and \(p_2p_1^{-1}\) is the required isomorphism. Generation proves uniqueness. It maps \(h_i\) to \(h_i'\), so transporting the weight equation shows that it realizes the specified root-system map on every root, not only on the simple roots. \(\square\)

If the root-system map is given without bases, choose a base in its source and its image base in the target. The theorem applies to those bases. Together with Cartan conjugacy, it says that the isomorphism class of the root system determines the isomorphism class of a semisimple Lie algebra whenever such an algebra exists. We now prove existence.

## 4. The Serre ideal stays on the two sides

In \(\widetilde{\mathfrak g}\), set
\[
m_{ij}=1-a_{ji},\qquad
S^+_{ij}=(\operatorname{ad}e_i)^{m_{ij}}e_j,
\qquad
S^-_{ij}=(\operatorname{ad}f_i)^{m_{ij}}f_j
\quad(i\ne j).
\tag{4.1}
\]
Let \(I^+\) be the ideal they generate **inside** \(\widetilde{\mathfrak n}^+\), and \(I^-\) its negative counterpart. The next calculation shows why imposing the endpoint relations does not create a new degree-zero relation.

<a id="RTLIE11-L41"></a>
**Lemma 4.1.** Every \(S^+_{ij}\) is killed by \(\operatorname{ad}f_k\), for every \(k\). The ideal generated by all Serre elements in \(\widetilde{\mathfrak g}\) is precisely \(I^-\oplus I^+\).

**Proof.** A negative generator outside \(\{i,j\}\) commutes with both positive letters, hence kills \(S^+_{ij}\). For k=i, apply the rank-one relations to the vector \(v=e_j\), which has \([f_i,v]=0\) and \([h_i,v]=a_{ji}v\). Jacobi proves by induction
\[
[f_i,(\operatorname{ad}e_i)^m v]
=-m(a_{ji}+m-1)(\operatorname{ad}e_i)^{m-1}v.
\tag{4.2}
\]
In the induction step, the additional term from \([f_i,e_i]=-h_i\) has weight \(a_{ji}+2m\); adding it to the previous coefficient gives \(-(m+1)(a_{ji}+m)\). At \(m=1-a_{ji}\) the coefficient vanishes.

For k=j, \(\operatorname{ad}f_j\) commutes with \(\operatorname{ad}e_i\) and replaces e_j by \(-h_j\). If \(a_{ji}<0\), the exponent is at least two, and \((\operatorname{ad}e_i)^2h_j=0\). If \(a_{ji}=0\), the Euclidean Cartan matrix has the symmetric zero pattern \(a_{ij}=0\), and already \([e_i,h_j]=0\). This proves all the annihilations. Involution (2.5) proves the negative counterpart.

Inside the positive free algebra, \(I^+\) is spanned by successive adjoints of positive generators on these homogeneous Serre elements. Indeed, Jacobi writes adjoint action of a bracket word as a combination of such successive actions. Homogeneity makes it H-stable. Induct on the number of these actions and use
\[
[f_k,[e_l,u]]=[[f_k,e_l],u]+[e_l,[f_k,u]].
\tag{4.3}
\]
The first term is either zero or Cartan action on an element of \(I^+\); the second term uses the induction. The just-proved annihilation is the initial case. Thus \(I^+\) is stable under every negative generator too, and is an ideal of the whole auxiliary algebra. The involution gives the same result for \(I^-\). Their direct sum, direct by Proposition 2.2, is therefore an ideal containing all Serre elements. Conversely their defining positive and negative adjoints already lie in the full Serre ideal. These inclusions identify that ideal exactly with \(I^-\oplus I^+\). In particular it has no Cartan component. \(\square\)

Define the **Serre algebra**
\[
\mathfrak g(A)=
\widetilde{\mathfrak g}/(I^-\oplus I^+).
\tag{4.4}
\]
It has the direct triangular decomposition
\[
\mathfrak g(A)=\mathfrak n^-\oplus H\oplus\mathfrak n^+,
\qquad
\mathfrak n^\pm=\widetilde{\mathfrak n}^\pm/I^\pm.
\tag{4.5}
\]
In particular the positive and negative subalgebras have exactly their respective Serre relations as defining relations. The \(h_i\) remain independent. The \(e_i,f_i\) remain nonzero as well: \([e_i,f_i]=h_i\ne0\). Their individual degree spaces are one-dimensional. There are no degrees \(k\alpha_i\), \(|k|>1\), because a bracket word on a single generator vanishes once its length exceeds one. Every degree space is finite-dimensional, and the only degree-zero space is \(H\).

## 5. Nilpotent adjoints move the weights by reflections

<a id="RTLIE11-P51"></a>
**Proposition 5.1.** On \(\mathfrak g(A)\), each \(\operatorname{ad}e_i\) and \(\operatorname{ad}f_i\) is locally nilpotent: every individual vector is killed by a sufficiently high power. The automorphism
\[
T_i=
\exp(\operatorname{ad}e_i)
\exp(-\operatorname{ad}f_i)
\exp(\operatorname{ad}e_i)
\tag{5.1}
\]
acts on \(H\) as \(H_0\mapsto H_0-\alpha_i(H_0)h_i\), and carries the degree space \(\mathfrak g(A)_\beta\) isomorphically onto \(\mathfrak g(A)_{s_i\beta}\).

**Proof.** For \(D=\operatorname{ad}e_i\), nilpotence on each generator follows explicitly: D kills e_i and all \(f_j\) with \(j\ne i\), its third power kills f_i through \(f_i\mapsto h_i\mapsto-2e_i\mapsto0\), its second power kills every h_j, and the Serre exponent kills every e_j with \(j\ne i\). The derivation binomial rule gives
\[
D^pu=D^qv=0\quad\Longrightarrow\quad D^{p+q-1}[u,v]=0:
\quad D^n[u,v]=\sum_{k=0}^n\binom nk[D^ku,D^{n-k}v].
\tag{5.2}
\]
It follows by induction on the bracket tree, and then by taking a maximum for a finite linear combination, that D is locally nilpotent on every element. The involution gives the assertion for \(\operatorname{ad}f_i\). No common exponent for the entire algebra, and no finite dimension, has been used.

For a locally nilpotent derivation the exponential is a finite polynomial on each argument. The same binomial identity proves \(\exp D[u,v]=[\exp D u,\exp D v]\), and multiplication of finite series gives inverse \(\exp(-D)\). The three factors in (5.1) therefore define an automorphism.

For explicit verification on the rank-one triple, \(\exp(\operatorname{ad}e)\) sends \((e,h,f)\) to \((e,h-2e,f+h-e)\), whereas \(\exp(-\operatorname{ad}f)\) sends them to \((e+h-f,h-2f,f)\). Composing right to left gives
\[
T_i(e_i)=-f_i,\qquad T_i(f_i)=-e_i,\qquad T_i(h_i)=-h_i.
\tag{5.3}
\]
For general \(H_0\in H\), its part \(H_0-\alpha_i(H_0)h_i/2\) centralizes both rank-one generators, and its remaining part is negated. Thus \(T_iH_0=H_0-\alpha_i(H_0)h_i\). Transporting the equation \([H_0,v]=\beta(H_0)v\) gives the weight
\(\beta\circ T_i^{-1}|_H=\beta-\beta(h_i)\alpha_i=s_i\beta\).
The inverse yields an isomorphism of the two weight spaces, preserving dimensions. Products give any sequence of Weyl reflections; no Coxeter relations for the particular lifts \(T_i\) are needed. \(\square\)

## 6. Finite type leaves exactly the prescribed roots

<a id="RTLIE11-T61"></a>
**Theorem 6.1 (Serre).** For a Cartan matrix \(A\) of finite type, the presentation (1.3)–(1.4) defines a finite-dimensional semisimple complex Lie algebra. Its Cartan subalgebra is \(H=\operatorname{span}\{h_i\}\), and its root system is \(\Phi(A)\). More precisely,
\[
\mathfrak g(A)=H\oplus\bigoplus_{\beta\in\Phi(A)}\mathfrak g(A)_\beta,
\qquad \dim\mathfrak g(A)_\beta=1,
\qquad \dim\mathfrak g(A)=r+|\Phi(A)|.
\tag{6.1}
\]
Every connected component of the Dynkin diagram gives a simple ideal, and these are the direct simple summands.

**Proof of the exact root set.** Use the positive Euclidean form of the given finite root system, with simple-root basis \(\alpha_i\). Proposition 2.2 and Lemma 4.1 say that every nonzero degree lies in \(Q_+\setminus\{0\}\) or its negative. A positive degree on just one simple-root line can only be \(\alpha_i\), because every longer bracket word in a single generator is zero.

Consider a positive occurring degree \(\beta=\sum b_i\alpha_i\) with at least two positive coefficients. The equality
\(0<(\beta,\beta)=\sum b_i(\beta,\alpha_i)\)
supplies i with \(b_i>0\) and positive inner product. The integer \(m=\beta(h_i)=\sum b_j a_{ji}\) is positive. Proposition 5.1 makes degree \(s_i\beta=\beta-m\alpha_i\) occur. Its unchanged positive coefficient outside i forbids zero or a negative degree. Triangularity consequently makes it positive, with smaller integral height. Repeated descent reaches a simple root. The negative side follows from the involution. RT-LIE-08, Lemma 4.1, says \(W\Delta=\Phi\), so all possible nonzero degrees are in the prescribed finite root set.

Conversely every element of \(W\Delta\) occurs, by applying the corresponding product of the \(T_i\) to a nonzero simple generator. Their spaces are lines: a simple generator has a one-dimensional degree space after (4.5), and Proposition 5.1 preserves dimensions. The surviving Cartan basis and exact triangular decomposition now give (6.1), including finite dimension. Positive definiteness was essential to the descending step; the argument is not asserted for indefinite Cartan matrices.

**Proof of simplicity and Cartan.** For a connected diagram let J be a nonzero ideal. The commuting diagonalizable Cartan actions split it into weight components: choose finitely many separating Cartan operators and use their polynomial spectral projections. If J contains a nonzero Cartan vector H_0, some \(\alpha_i(H_0)\ne0\) because the simple roots form a basis of \(H^*\); bracketing with e_i supplies a root vector. Otherwise it already has a nonzero root component. Every \(T_i\) and its inverse preserve ideals, being products of adjoint polynomials. The root descent carries this component to a simple root line, giving some e_i in J. Then J contains \(h_i=[e_i,f_i]\) and \(f_i=-[h_i,f_i]/2\). If j is a neighboring vertex, \([h_i,e_j]=a_{ji}e_j\ne0\) supplies e_j, and the same argument supplies h_j,f_j. Connectedness reaches every generator; J is the whole algebra, which is nonabelian by its rank-one relations. It is simple.

Generators on different components commute: the Cartan entries and cross mixed brackets vanish, and the cross Serre exponents are one. Jacobi then makes their generated subalgebras commute. They span, and their sum is direct because the nonzero component weights are disjoint while their Cartan spans have disjoint independent bases. Applying the connected proof to each gives the stated direct simple decomposition and semisimplicity.

Finally H acts diagonally, is abelian and hence nilpotent, and is its own normalizer. Indeed, for an element in its normalizer each nonzero weight component has to vanish by bracketing with an H_0 on which that weight is nonzero. Its remaining component lies in H. Thus H is a Cartan subalgebra by the nilpotent self-normalizing definition; this step needs no Cartan-conjugacy or Cartan-equivalence import. Its weights are exactly \(\Phi\) and its pairings \(\alpha_i(h_j)=a_{ij}\). Relative lengths are those of the given Euclidean system; independent overall scales on orthogonal components do not affect these pairings. This proves the theorem in the stated root-system convention. \(\square\)

The empty matrix gives the zero algebra. All arguments above then have empty sets of generators and roots; (6.1) gives dimension zero. Semisimplicity includes this case, while simplicity does not.

**Corollary 6.2 (classification).** Complex simple Lie algebras, up to isomorphism, correspond bijectively to
\[
A_n\ (n\ge1),\quad B_n\ (n\ge2),\quad
C_n\ (n\ge3),\quad D_n\ (n\ge4),\quad
E_6,E_7,E_8,F_4,G_2.
\]

**Proof.** The preceding root-decomposition and classification lessons give a finite Dynkin diagram for every semisimple algebra. For a connected diagram, Theorem 6.1 constructs a simple algebra with that root system, and Theorem 3.1 proves uniqueness. To see that a simple algebra's diagram is connected, its Chevalley generators belonging to distinct components commute, by Proposition 1.1; they would give disjoint nonzero ideals and a direct decomposition as in the theorem. Conversely a connected diagram gives a simple algebra by the theorem. The specified rank cutoffs remove \(B_1=C_1=A_1\), \(B_2=C_2\) and \(D_3=A_3\), and exclude the reducible \(D_2\). This proves both surjectivity and injectivity. \(\square\)

In particular any original semisimple \(\mathfrak g\) has exactly this Serre presentation. Proposition 1.1 gives a surjection \(\mathfrak g(A)\to\mathfrak g\); both have dimension \(r+|\Phi|\), so it is an isomorphism. The endpoint relations are therefore sufficient, not only necessary.

## 7. Two matrix examples and one asymmetric exponent

For \(A=[2]\), there are no cross-vertex Serre relations. The algebra has basis \(e,f,h\) with \([h,e]=2e\), \([h,f]=-2f\), \([e,f]=h\). The matrices \(E_{12},E_{21},\operatorname{diag}(1,-1)\) satisfy these relations and are independent, giving \(\mathfrak g(A)=\mathfrak{sl}_2\).

For
\[
A=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\qquad e_1=E_{12},\quad e_2=E_{23},\quad
f_1=E_{21},\quad f_2=E_{32},
\tag{7.1}
\]
the extra positive vector is \([e_1,e_2]=E_{13}\), and the negative one is \([f_2,f_1]=E_{31}\). The two Cartan generators are \(E_{11}-E_{22}\) and \(E_{22}-E_{33}\). These eight independent matrices span \(\mathfrak{sl}_3\). The Serre algebra also has dimension \(2+6=8\), so the generator map is an isomorphism. Exercise 8.1 checks all relations explicitly.

For \(G_2\), number the short simple root by 1. Our column-coroot matrix is
\[
A=\begin{pmatrix}2&-1\\-3&2\end{pmatrix}.
\tag{7.2}
\]
Consequently the two positive endpoint relations are
\[
(\operatorname{ad}e_1)^4e_2=0,
\qquad (\operatorname{ad}e_2)^2e_1=0,
\tag{7.3}
\]
and the same powers hold for the negative generators. The first string contains the roots
\(\alpha_2,\alpha_1+\alpha_2,2\alpha_1+\alpha_2,3\alpha_1+\alpha_2\).
Its last vector is nonzero by the rank-one string calculation, while one further bracket is zero. The other positive nonsimple root \(3\alpha_1+2\alpha_2\) comes from the bracket at the remaining endpoint with \(e_2\). Thus the four and the two in (7.3) correspond to the actual short/long geometry. Transposing (7.2) without changing the acting-index convention would reverse these instructions.

## 8. Exercises with complete solutions

### Exercise 8.1 — the relations in three-by-three matrices (easy)

Use the generators in (7.1), with \(h_1=E_{11}-E_{22}\) and \(h_2=E_{22}-E_{33}\). Check the Cartan, mixed and Serre relations, including the negative generators.

**Solution.** Matrix units satisfy
\[
[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}.
\tag{8.1}
\]
The diagonal matrices \(h_1,h_2\) commute. For a diagonal \(H=\operatorname{diag}(d_1,d_2,d_3)\),
\([H,E_{ab}]=(d_a-d_b)E_{ab}\). Consequently
\[
\begin{array}{c|rr}
 &e_1&e_2\\\hline
\operatorname{ad}h_1&2e_1&-e_2\\
\operatorname{ad}h_2&-e_1&2e_2
\end{array}
\]
and the corresponding coefficients on \(f_1,f_2\) are their negatives. These are exactly the entries \(a_{ji}\) and \(-a_{ji}\). Formula (8.1) gives
\([e_1,f_1]=h_1\), \([e_2,f_2]=h_2\), and
\([e_1,f_2]=[e_2,f_1]=0\).

Next \([e_1,e_2]=E_{13}\), while
\([E_{12},E_{13}]=[E_{23},E_{13}]=0\). Therefore
\((\operatorname{ad}e_1)^2e_2=(\operatorname{ad}e_2)^2e_1=0\).
For the negative generators, \([f_1,f_2]=-E_{31}\), and
\([E_{21},E_{31}]=[E_{32},E_{31}]=0\). Both negative endpoint relations also have exponent two. This checks all defining relations. The additional vectors \(E_{13},E_{31}\), the four initial off-diagonal units and the two diagonals are independent and span all trace-zero matrices, so the generators give all of \(\mathfrak{sl}_3\). Its dimension agrees with Theorem 6.1, proving that this representation of the presentation is faithful.

### Exercise 8.2 — generation from the simple root spaces (medium)

Let \(\mathfrak g\) be any complex semisimple Lie algebra. Prove directly that normalized Chevalley generators for a base of its root system generate \(\mathfrak g\).

**Solution.** Let \(K\) be their generated subalgebra. The simple coroots form a basis of \(\mathfrak h\), and all of them belong to \(K\), so \(\mathfrak h\subseteq K\). We prove by height induction that every positive root space is in \(K\). Height one is the given set of simple root vectors, whose spaces are one-dimensional.

Write a positive nonsimple root as \(\beta=\sum b_j\alpha_j\). Since
\((\beta,\beta)=\sum b_j(\beta,\alpha_j)>0\), choose \(i\) with \(b_i>0\) and \((\beta,\alpha_i)>0\). Here \(\beta\ne\alpha_i\), and a reduced root system has no other root that is a positive multiple of \(\alpha_i\). The root-string property therefore says that \(\beta-\alpha_i\) is a root. Its coefficients are nonnegative and its height is one less, so its space lies in \(K\) by induction. The nonzero-bracket theorem for root spaces gives
\[
[\mathfrak g_{\alpha_i},\mathfrak g_{\beta-\alpha_i}]
=\mathfrak g_\beta.
\]
Thus \(\mathfrak g_\beta\subseteq K\). Apply the same argument to the base \(-\Delta\), starting with the \(f_i\), to get every negative root space. The root decomposition now gives \(K=\mathfrak g\). The proof applies component by component, and to the zero algebra with an empty base.

### Exercise 8.3 — a bound on each adjoint orbit (medium)

Prove local nilpotence of \(D=\operatorname{ad}e_i\) using only the defining relations, before finite dimension is known. Give a nilpotence bound for any specified bracket word.

**Solution.** Fix \(i\). Assign the following safe exponents to generators:
\[
\begin{aligned}
\nu(e_i)&=1,&\nu(e_j)&=1-a_{ji}\quad(j\ne i),\\
\nu(f_i)&=3,&\nu(f_j)&=1\quad(j\ne i),&
\nu(h_j)&=2.
\end{aligned}
\tag{8.2}
\]
Each satisfies \(D^{\nu(x)}x=0\). For the \(e_j\) this is the Serre relation; for the mixed \(f_j\) it is \([e_i,f_j]=0\). For \(f_i\) the successive values are \(h_i,-2e_i,0\). Finally \([e_i,h_j]=-a_{ij}e_i\), so the second iterate vanishes.

A derivation obeys the iterated Leibniz formula
\[
D^n[u,v]=\sum_{k=0}^n\binom nk[D^ku,D^{n-k}v].
\tag{8.3}
\]
It follows by induction on \(n\) from the derivation rule and Pascal's identity. If \(D^pu=D^qv=0\), then every term in (8.3) vanishes for \(n=p+q-1\): either \(k\ge p\) or \(n-k\ge q\). By induction on the bracket tree, a word with leaves \(x_1,\ldots,x_s\) is killed by
\[
D^{\,1+\sum_{\ell=1}^s(\nu(x_\ell)-1)}.
\tag{8.4}
\]
Every element of a presented Lie algebra is a finite linear combination of words. The maximum of their bounds kills that element. Thus \(D\) is locally nilpotent without any appeal to finite dimension. This also proves that the exponentials used in (5.1) are well defined at that stage of the argument.

### Exercise 8.4 — reconstructing the graph proof (hard)

Let \(\sigma:\Phi\to\Phi'\) be an isomorphism of root systems taking \(\Delta\) to \(\Delta'\), with corresponding normalized generators. Prove the isomorphism theorem by examining the subalgebra generated by their paired vectors.

**Solution.** Write corresponding generators with the same indices and set
\[
L=\big\langle(e_i,e_i'),(f_i,f_i')\big\rangle
\subseteq\mathfrak g\oplus\mathfrak g',\qquad
H_D=\operatorname{span}\{(h_i,h_i')\}.
\]
The paired mixed brackets give \((h_i,h_i')\), so \(H_D\subseteq L\). Exercise 8.2 makes both projections of \(L\) surjective. The Cartan matrices agree, and hence the paired generators satisfy the non-Serre relations (1.3). Proposition 2.2 applies to the resulting map from the auxiliary algebra: \(L\) is spanned by its positive words, its negative words and \(H_D\).

Every positive word has a strictly positive weight for the common Cartan action; every negative word has a strictly negative one. They may vanish, but they cannot contribute a zero-weight vector. Polynomial weight projections therefore give
\[
L\cap(\mathfrak h\oplus\mathfrak h')=H_D.
\tag{8.5}
\]
The projection of \(H_D\) to either Cartan algebra is an isomorphism because the simple coroots are bases.

Define \(I=\{x\in\mathfrak g:(x,0)\in L\}\). This is an ideal: given \(y\in\mathfrak g\), choose \((y,y')\in L\) by surjectivity, and then \(([y,x],0)\in L\). Any nonzero ideal of \(\mathfrak g\) meets \(\mathfrak h\) nontrivially. Indeed, its weight components belong to the ideal. If one is a nonzero \(x\in\mathfrak g_\beta\), nondegeneracy of the opposite-root pairing gives \(y\in\mathfrak g_{-\beta}\) with \(\kappa(x,y)\ne0\). Then \([x,y]\in\mathfrak h\) is nonzero, since for \(H\in\mathfrak h\)
\[
\kappa([x,y],H)=\beta(H)\kappa(x,y).
\]
If the only nonzero component is already in \(\mathfrak h\), the assertion is immediate.

But \(I\cap\mathfrak h=0\): by (8.5), \((H,0)\) would belong to \(H_D\), whose projection to \(\mathfrak h'\) is injective. Thus \(I=0\). Interchanging the two factors gives the other kernel zero. Both projections \(L\to\mathfrak g,\mathfrak g'\) are now isomorphisms. Their composite defines an isomorphism \(\psi:\mathfrak g\to\mathfrak g'\) with graph \(L\), sending every \(e_i,f_i,h_i\) to its primed counterpart.

For \(H\in\mathfrak h\), the equal Cartan pairings give
\(\alpha_i'(\psi H)=\alpha_i(H)\); extending linearly to roots shows
\(\psi(\mathfrak g_\beta)=\mathfrak g'_{\sigma\beta}\). Hence this map extends the specified root-system isomorphism. Its values on the generating vectors force uniqueness. The argument also covers empty root systems, in which both algebras are zero.

## 9. Scope, automorphisms and references

The proofs above establish the isomorphism theorem and the finite-type Serre theorem for every complex semisimple Lie algebra, with arbitrary rank and any number of simple components. In particular the auxiliary free algebras, survival of the Cartan generators, stability of the Serre ideals, locally nilpotent reflection operators, absence of additional weights, and simplicity of each connected component have all been proved. The exact checked prerequisites for the presentation are the receiving root decomposition, finite Euclidean base/reflection lemmas and RTF-004. The retained classification corollary additionally depends on the separate classification provider; it is outside the scoped proof audit.

**What this lesson does not prove.** After choosing a base and normalized simple generators, the automorphism group has the decomposition
\[
\operatorname{Aut}(\mathfrak g)
\cong\operatorname{Int}(\mathfrak g)
\rtimes\operatorname{Aut}(\operatorname{Dyn}(\mathfrak g)).
\tag{9.1}
\]
Here diagram automorphisms preserve the Cartan entries, including the directions of multiple edges, and may permute isomorphic connected components. Their chosen lifts permute the corresponding normalized generators. Theorem 3.1 supplies these lifts; the assertion not proved here is that every automorphism factors uniquely as an inner automorphism followed by such a lift. This unproved automorphism factorization is retained as a clearly stated further result and is not used by Lesson 18 or by the Serre proof above.

The planned algebraic-geometry lesson *Isomorphism and existence theorems for split reductive group schemes* develops the group version. Its additional data are the character and cocharacter lattices; a root system alone does not determine a reductive group. The Serre presentation here is a Lie-algebra statement over \(\mathbb C\), and does not assert the same semisimplicity result in positive characteristic.

For comparison with the wider algebraic-geometry programme, the [official Stacks project](https://stacks.math.columbia.edu/) remains the reference project. The [AI Integrated Stacks Project reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) presents unofficial AI drafts; those drafts are not maintainer-reviewed Stacks results. No result from that reader is needed as an external proof in this lesson.

**References.**

- P. Etingof, [*18.745: Lie Groups and Lie Algebras, I*, author-hosted lecture notes](https://math.mit.edu/~etingof/lnlg.pdf), Section 23: Theorem 23.1 (Chevalley generators and Serre relations), Theorem 23.2 (Serre presentation) and Lemma 23.3 (the auxiliary free triangular algebra); Sections 10–11 for tensor/enveloping algebras and PBW. These locators refer to the checked 223-page author PDF. Its row-coroot convention is the transpose of the column-coroot convention (1.2), so its \(a_{ij}\) in an acting-i exponent becomes our \(a_{ji}\).
- A. Kirillov, Jr., [*Introduction to Lie Groups and Lie Algebras*, author-hosted notes](https://math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf), Sections 6.6 and 7.3–7.7, for the root-space brackets and finite Euclidean arithmetic/base/reflection inputs reconstructed in the receiving RT-LIE-07 and RT-LIE-08.
