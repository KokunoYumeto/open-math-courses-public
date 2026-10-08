# The isomorphism theorem and Serre's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Dynkin diagram first records the relative positions of simple roots. It also tells us how many times one simple-root generator can be bracketed with another before the result is zero. We will show that these instructions determine every bracket of a semisimple Lie algebra, and that they construct an algebra for every finite Dynkin diagram.

The main ground field is \(\mathbb C\); Section 6.3 also constructs the split rational form and its characteristic-zero extensions. We use the root decomposition and root-string brackets from [The root space decomposition of a semisimple Lie algebra](RT-LIE-07.md), the base and reflection results from [Root systems and their Weyl groups](RT-LIE-08.md), the full finite classification from [Cartan matrices, Dynkin diagrams and the classification of root systems](RT-LIE-09.md), and Cartan conjugacy from [Cartan subalgebras and their conjugacy](RT-LIE-10.md). The rank-one representation calculations are those of [Representations of sl(2)](RT-LIE-05.md). The auxiliary algebra will initially be infinite-dimensional; we prove its needed structural properties before using them.

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

**Proposition 1.1 (Chevalley generators).** The \(e_i,f_i,h_i\) generate \(\mathfrak g\). They satisfy
\[
\begin{aligned}[c]
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

**Proof.** The relations (1.3) follow from the root decomposition and (1.1). For \(i\ne j\), \(\alpha_i-\alpha_j\) has coefficients of both signs in the simple base, so it is not a root and the cross bracket is zero.

Let \(\beta=\sum b_i\alpha_i\) be a positive nonsimple root. Since
\((\beta,\beta)=\sum b_i(\beta,\alpha_i)>0\), some \(i\) has \(b_i>0\) and \((\beta,\alpha_i)>0\). The root string then gives \(\beta-\alpha_i\) as a root. It is positive: \(\beta\) is not a multiple of \(\alpha_i\), and the remaining nonzero coefficient prevents a negative expansion. Its height is one smaller. The nonvanishing root-string bracket gives
\[
[\mathfrak g_{\alpha_i},\mathfrak g_{\beta-\alpha_i}]
=\mathfrak g_\beta.
\tag{1.5}
\]
Induction on height shows that the \(e_i\) generate all positive root spaces. Apply the same proof to the opposite base to generate all negative spaces using the \(f_i\). Their pair brackets give the basis \(h_i\), so the entire algebra is generated.

For (1.4), set \(p=-a_{ji}\ge0\). In the adjoint representation of the rank-one algebra spanned by \(e_i,f_i,h_i\), the vector \(e_j\) has weight \(-p\) and is killed by \(\operatorname{ad}f_i\). The finite-dimensional \(\mathfrak{sl}_2\) calculation makes its generated module the simple module of highest weight \(p\); in particular \((\operatorname{ad}e_i)^{p+1}e_j=0\). Equivalently this is the endpoint of its root string. The vector \(f_j\) has weight \(p\) and is killed by \(\operatorname{ad}e_i\); the same calculation gives the other relation. \(\square\)

The choice of \(e_i\) is free up to a nonzero scalar, after which (1.1) determines \(f_i\). A presentation theorem must respect those choices; it cannot silently prescribe extra normalization on all other root vectors.

## 2. Separate formal generators before imposing the endpoints

Let \(A\) be the Cartan matrix of any finite reduced root system \(\Phi\), with chosen base \(\alpha_i\). Such systems have already been constructed for every classified diagram. Write \(Q=\bigoplus_i\mathbb Z\alpha_i\) and \(Q_+=\bigoplus_i\mathbb Z_{\ge0}\alpha_i\). Take an abstract vector space \(H\) with basis \(h_i\), and define the linear forms \(\alpha_j\in H^*\) by \(\alpha_j(h_i)=a_{ji}\). The matrix is invertible, so these \(\alpha_j\) form a basis of \(H^*\).

Define \(\widetilde{\mathfrak g}\) by generators \(e_i,f_i,h_i\) and only (1.3), leaving out (1.4). A Lie algebra given by generators and relations means a quotient of the free Lie algebra by the ideal of the stated relations. Free Lie algebras themselves can be constructed from formal bracket expressions modulo bilinearity, alternation and Jacobi; their universal property follows by evaluation of those expressions.

We need to know that this quotient has not accidentally introduced relations among the positive generators or collapsed \(H\). The following elementary separation fact will supply that check.

**Lemma 2.1 (free Lie expressions inside a tensor algebra).** The free Lie algebra on a vector space \(V\) embeds into its tensor algebra \(T(V)\), as the Lie subalgebra generated by \(V\) under commutators.

**Proof.** We first prove the needed injectivity fact for an arbitrary Lie algebra \(L\), with no finite-dimension assumption. Choose a totally ordered vector-space basis \(x_i\) and form
\[
U(L)=T(L)/(xy-yx-[x,y]).
\]
For an adjacent inversion \(i>j\), replace \(x_ix_j\) by \(x_jx_i+[x_i,x_j]\), expanding the bracket in the chosen basis. Each resulting word decreases the pair consisting of its length and its inversion count, ordered lexicographically. The bracket term has shorter length, and the exchanged term has one fewer inversion. This pair lies in \(\mathbb N^2\), so the reduction terminates, including for an infinite basis since each word and each expanded bracket is finite.

There is no choice conflict for two disjoint adjacent pairs: performing both replacements in either order gives the same expansion. The sole overlapping case is three basis elements \(x>y>z\). Reducing its two possible inversions first gives, after moving its length-three term into order, the respective expressions
\[
zyx+[y,z]x+y[x,z]+[x,y]z,
\qquad
zyx+z[x,y]+[x,z]y+x[y,z].
\tag{2.1}
\]
Their difference reduces in length two to
\[
[[y,z],x]+[y,[x,z]]+[[x,y],z]=0
\]
by Jacobi. This calculation works in every surrounding word as well: all remaining terms have smaller length. It proves uniqueness of a reduced expression by induction on the decreasing pair. Indeed, compare the first choices of two reductions; resolve their disjoint or overlapping difference as above, then apply the induction to the smaller terms. Linearity extends the comparison to finite sums.

Thus reduction defines a linear map onto the span of ordered words. It kills every defining relation in every word context, and it fixes each ordered word. It descends to \(U(L)\), proving that those words are linearly independent there. In particular the length-one words embed \(L\) into \(U(L)\).

Now let \(L\) be free on \(V\). Algebra maps \(U(L)\to B\), for any associative algebra \(B\), are exactly Lie maps \(L\to B\) with commutator bracket, hence exactly linear maps \(V\to B\). This is also the universal property of \(T(V)\). The two algebra homomorphisms induced by the generators are inverse, so \(U(L)=T(V)\) canonically. The injection just proved identifies \(L\) with the Lie subalgebra generated by \(V\). \(\square\)

This proves the ordered-word fact needed here. The later enveloping-algebra lesson develops its filtration, associated graded algebra and other PBW consequences systematically.

**Proposition 2.2 (the auxiliary triangular decomposition).** There is a direct decomposition
\[
\widetilde{\mathfrak g}
=\widetilde{\mathfrak n}^-\oplus H\oplus
\widetilde{\mathfrak n}^+,
\tag{2.2}
\]
where \(\widetilde{\mathfrak n}^+\) is free on the \(e_i\), \(\widetilde{\mathfrak n}^-\) is free on the \(f_i\), and the displayed \(h_i\) are linearly independent. The degrees are \(\deg e_i=\alpha_i\), \(\deg f_i=-\alpha_i\), \(\deg h_i=0\). There are no degrees outside \(Q_+\cup(-Q_+)\), and each nonzero-degree space is finite-dimensional.

**Proof: spanning and directness.** The presentation is \(Q\)-graded, since every defining relation is homogeneous. The adjoint action of \(H\) on a bracket word has the weight given by its degree, by Jacobi.

First, the bracket of \(e_i\) with a word of length \(q\) in the \(f_j\) lies in \(H\) for \(q=1\), and in the negative subalgebra for \(q>1\). Prove this by induction on \(q\), expressing negative words as linear combinations of words \([f_j,w]\) by Jacobi. The formula
\[
[e_i,[f_j,w]]=[[e_i,f_j],w]+[f_j,[e_i,w]]
\tag{2.3}
\]
uses only a Cartan action in the first term and the shorter-word induction in the second. The positive analogue holds for brackets of \(f_i\) with positive words.

For a general positive word, express it as \([e_i,u]\) and use
\([[e_i,u],w]=[e_i,[u,w]]-[u,[e_i,w]]\).
Induction on the positive length, using (2.3) and the Cartan weight actions, puts every mixed bracket in the sum in (2.2). That sum is consequently a subalgebra containing all generators, hence is the whole algebra. Positive words have strictly positive total height, negative words strictly negative height, and \(H\) has height zero. The grading makes this sum direct once the asserted embeddings are established.

**Proof: no hidden relations.** Put
\(M=T(\mathbb C\{F_1,\ldots,F_r\})\otimes\mathbb C[z_1,\ldots,z_r]\).
For a tensor word \(w\) in the \(F_j\), let \(\beta\in Q_+\) be the sum of its letter roots. Define operators on \(w\otimes P\) by
\[
\begin{aligned}
\mathcal F_j(w\otimes P)&=F_jw\otimes P,\\
\mathcal H_i(w\otimes P)&=w\otimes(z_i-\beta(h_i))P,\\
\mathcal E_i(1\otimes P)&=0,\\
\mathcal E_i(F_jw\otimes P)
&=F_j\mathcal E_i(w\otimes P)
+\delta_{ij}w\otimes(z_i-\beta(h_i))P.
\end{aligned}
\tag{2.4}
\]
In the last line \(F_j\) means left multiplication on the tensor factor. These recursive formulas define linear operators on all finite words.

They satisfy all of (1.3). The \(\mathcal H_i\) commute because they multiply the polynomial factor by commuting scalars on each fixed word. Prepending \(F_j\) increases \(\beta\) by \(\alpha_j\), giving
\([\mathcal H_i,\mathcal F_j]=-a_{ji}\mathcal F_j\).
Every summand of \(\mathcal E_j\) deletes precisely one \(F_j\), so its output has degree \(\beta-\alpha_j\); comparing the two \(\mathcal H_i\) factors gives
\([\mathcal H_i,\mathcal E_j]=a_{ji}\mathcal E_j\).
Finally the last line of (2.4) is exactly
\([\mathcal E_i,\mathcal F_j]=\delta_{ij}\mathcal H_i\).
There are no relations between two positive or two negative generators to check. We have therefore constructed a representation of \(\widetilde{\mathfrak g}\).

On \(1\otimes1\), the \(h_i\) give the independent polynomials \(z_i\). Thus \(H\) embeds. Every bracket word in the \(f_i\) acts by left multiplication by the identical commutator word in the \(F_i\); evaluating on \(1\otimes1\) and using Lemma 2.1 proves that the negative free Lie algebra embeds. The involution
\[
e_i\longleftrightarrow f_i,
\qquad h_i\longmapsto-h_i
\tag{2.5}
\]
preserves (1.3) and proves the positive embedding too. This establishes (2.2). Each fixed multidegree has only finitely many letters and finitely many bracket patterns, so its spanning expressions form a finite set. There are no mixed-sign degrees by (2.2). \(\square\)

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

**Lemma 4.1.** Every \(S^+_{ij}\) is killed by \(\operatorname{ad}f_k\), for every \(k\). The ideal generated by all Serre elements in \(\widetilde{\mathfrak g}\) is precisely \(I^-\oplus I^+\).

**Proof.** If \(k\notin\{i,j\}\), the operator \(\operatorname{ad}f_k\) kills both \(e_i,e_j\), so Jacobi kills the whole word. For \(k=i\), use the rank-one identities on a vector \(v\) with \([f_i,v]=0\) and \([h_i,v]=\lambda v\). Induction from \([e_i,f_i]=h_i\) gives
\[
[f_i,(\operatorname{ad}e_i)^m v]
=-m(\lambda+m-1)(\operatorname{ad}e_i)^{m-1}v.
\tag{4.2}
\]
For clarity, the induction step applies
\([f_i,[e_i,u]]=-[h_i,u]+[e_i,[f_i,u]]\),
where \(u=(\operatorname{ad}e_i)^m v\) has weight \(\lambda+2m\). The two scalar contributions add to \(-(m+1)(\lambda+m)\), the required next coefficient. Take \(v=e_j\), \(\lambda=a_{ji}\), and \(m=1-a_{ji}\); the coefficient in (4.2) is zero.

For \(k=j\), \(\operatorname{ad}f_j\) commutes with \(\operatorname{ad}e_i\). Thus its value is
\(-(\operatorname{ad}e_i)^{m_{ij}}h_j\).
If \(a_{ji}<0\), then \(m_{ij}\ge2\), while \((\operatorname{ad}e_i)^2h_j=0\). If \(a_{ji}=0\), the symmetric zero pattern of a Cartan matrix gives \(a_{ij}=0\), so already \([e_i,h_j]=0\). This proves the first assertion in every case. The involution (2.5) gives the negative assertion with \(e_k\) in place of \(f_k\).

The ideal \(I^+\) is spanned by repeated adjoints of the positive generators applied to the \(S^+_{ij}\). Jacobi expresses an adjoint of any positive bracket word as a combination of such adjoints. Its generators are homogeneous, so the ideal is stable under \(H\). It is also stable under every \(f_k\): induct on the number of those repeated positive adjoints and use
\[
[f_k,[e_l,u]]
=[[f_k,e_l],u]+[e_l,[f_k,u]].
\tag{4.3}
\]
The first term is either zero or a Cartan action on \(u\in I^+\); the second uses the induction. The base case is the annihilation just proved. Thus \(I^+\) is an ideal of the whole auxiliary algebra. So is \(I^-\). Their sum is direct by (2.2), contains all Serre elements and lies in the ideal generated by them. These two inclusions prove equality. \(\square\)

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

**Proposition 5.1.** On \(\mathfrak g(A)\), each \(\operatorname{ad}e_i\) and \(\operatorname{ad}f_i\) is locally nilpotent: every individual vector is killed by a sufficiently high power. The automorphism
\[
T_i=
\exp(\operatorname{ad}e_i)
\exp(-\operatorname{ad}f_i)
\exp(\operatorname{ad}e_i)
\tag{5.1}
\]
acts on \(H\) as \(H_0\mapsto H_0-\alpha_i(H_0)h_i\), and carries the degree space \(\mathfrak g(A)_\beta\) isomorphically onto \(\mathfrak g(A)_{s_i\beta}\).

**Proof.** Fix \(i\) and put \(D=\operatorname{ad}e_i\). On \(e_j\), \(j\ne i\), the Serre relation gives nilpotence; on \(e_i\) the first power is zero. On \(f_j\), \(j\ne i\), the first power is zero; on \(f_i\) the successive nonzero values are \(h_i,-2e_i\), so the third power is zero. On \(h_j\), the second power is zero. Thus it is nilpotent on each generator.

If \(D^pu=0\) and \(D^qv=0\), the binomial derivation formula gives
\[
D^{p+q-1}[u,v]
=\sum_{l=0}^{p+q-1}\binom{p+q-1}{l}
[D^lu,D^{p+q-1-l}v]=0.
\tag{5.2}
\]
One factor in each summand is zero. Induction on a bracket word, followed by taking a maximum over a finite linear combination, proves local nilpotence on the whole algebra. Involution (2.5) proves the assertion for \(f_i\). A uniform exponent for the whole auxiliary construction has not been assumed.

For a locally nilpotent derivation, its exponential is a finite sum on each vector. The derivation formula proves preservation of brackets by comparing coefficients; finite multiplication gives inverse \(\exp(-D)\). Hence (5.1) is an automorphism even before we know the algebra is finite-dimensional.

The rank-one calculation gives
\[
T_i(e_i)=-f_i,\qquad T_i(f_i)=-e_i,
\qquad T_i(h_i)=-h_i.
\tag{5.3}
\]
For example apply the three finite adjoint polynomials successively using (1.1); they are the adjoint action of the matrix \(\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\). Decompose an arbitrary \(H_0\in H\) as
\(H_0-\tfrac12\alpha_i(H_0)h_i\), which centralizes both \(e_i,f_i\), plus \(\tfrac12\alpha_i(H_0)h_i\). Equation (5.3) yields the asserted action on \(H\).

If \([H_0,v]=\beta(H_0)v\), transporting that equation by \(T_i\) makes the weight of \(T_i v\) equal to
\[
\beta\circ T_i^{-1}|_H
=\beta-\beta(h_i)\alpha_i=s_i\beta.
\tag{5.4}
\]
The inverse gives equality of the two weight spaces and their dimensions. Products of these operators give the corresponding result for every element of the abstract Weyl group; no assertion that the \(T_i\) themselves satisfy the Coxeter relations is needed. \(\square\)

## 6. Finite type leaves exactly the prescribed roots

**Theorem 6.1 (Serre).** For a Cartan matrix \(A\) of finite type, the presentation (1.3)–(1.4) defines a finite-dimensional semisimple complex Lie algebra. Its Cartan subalgebra is \(H=\operatorname{span}\{h_i\}\), and its root system is \(\Phi(A)\). More precisely,
\[
\mathfrak g(A)=H\oplus\bigoplus_{\beta\in\Phi(A)}\mathfrak g(A)_\beta,
\qquad \dim\mathfrak g(A)_\beta=1,
\qquad \dim\mathfrak g(A)=r+|\Phi(A)|.
\tag{6.1}
\]
Every connected component of the Dynkin diagram gives a simple ideal, and these are the direct simple summands.

**Proof: all possible weights.** Realize \(Q\) in the positive Euclidean root space of the given finite root system. Its positive-definite form is the one used in this part of the proof. If \(\beta=\sum b_j\alpha_j\in Q_+\setminus\{0\}\) has a nonzero degree space, we show by decreasing its height that it is in the Weyl orbit of a simple root.

If just one coefficient is strictly positive, then \(\beta=k\alpha_i\). The single-generator observation after (4.5) forces \(k=1\). Otherwise at least two coefficients are strictly positive. The identity
\[
(\beta,\beta)=\sum_j b_j(\beta,\alpha_j)>0
\]
gives an \(i\) with \(b_i>0\) and \((\beta,\alpha_i)>0\). Set
\(m=\beta(h_i)=2(\beta,\alpha_i)/(\alpha_i,\alpha_i)\).
The Cartan entries make it an integer, so \(m\ge1\). Proposition 5.1 makes the space of degree
\[
s_i\beta=\beta-m\alpha_i
\tag{6.2}
\]
nonzero. Some other coefficient is still strictly positive, so this vector cannot lie in \(-Q_+\) or be zero. By the triangular decomposition every nonzero degree is in \(Q_+\) or \(-Q_+\). It must therefore lie in \(Q_+\), with height smaller by \(m\). Repeating this step reaches a simple root. Thus every positive nonzero weight is in \(W\Delta\); negative weights follow by (2.5). As \(W\Delta=\Phi(A)\), there are no additional roots.

Conversely every root in \(W\Delta\) occurs: apply the corresponding product of \(T_i\) to a nonzero \(e_j\). These maps preserve weight-space dimensions. The simple-root spaces are one-dimensional, so all occurring nonzero spaces are one-dimensional. Together with (4.5), this proves (6.1) and finite dimension. This is where finite type is essential: the positive norm made the height-reducing reflection possible, and \(W\Delta\) is finite.

**Proof: simplicity and the Cartan subalgebra.** First suppose the diagram is connected. A nonzero ideal \(J\) is stable under the diagonalizable Cartan actions, hence is a sum of its weight components by polynomial spectral projections. If it has only a nonzero zero-weight vector \(H_0\), some \(\alpha_i(H_0)\ne0\), because the \(\alpha_i\) form a basis of \(H^*\). Then \([H_0,e_i]\) puts a nonzero root component in \(J\). Otherwise it already contains such a component.

Every \(T_i\) and its inverse preserve an ideal, since their adjoint-polynomial factors do. As every root can be carried to a simple root, \(J\) contains some \(e_i\). It then contains \(h_i=[e_i,f_i]\) and \(f_i=-\tfrac12[h_i,f_i]\). For any neighboring vertex \(j\),
\([h_i,e_j]=a_{ji}e_j\ne0\)
puts \(e_j\) in \(J\), and then also \(h_j,f_j\). Connectedness propagates to every vertex. These generators give all of \(\mathfrak g(A)\), so it is simple. It is nonabelian by its embedded rank-one triple.

For different connected components, all cross brackets of generators vanish. The Cartan entries and cross \(e,f\) brackets are zero, and (1.4) has exponent one for the cross \(e,e\) and \(f,f\) brackets. Jacobi makes the generated component subalgebras commute. They span the whole algebra. Their nonzero weights belong to disjoint component root sets, while their degree-zero parts are disjoint spans of the independent \(h_i\). Their sum is consequently direct. The preceding connected proof applies to each component and proves semisimplicity.

The algebra \(H\) acts diagonally in (6.1), so it is toral. Its centralizer is precisely its zero-weight space \(H\); no larger toral algebra can contain it. Thus it is maximal toral and hence Cartan by the preceding Cartan-equivalence theorem. Alternatively its normalizer is \(H\) directly by evaluating every nonzero root component, so its abelianity gives the Cartan definition without another import. The roots and coroot pairings in (6.1) are the original \(\alpha_i(h_j)=a_{ij}\); hence the root system is \(\Phi(A)\), with the root-system convention of the preceding classification lesson. Absolute Euclidean scales may be chosen separately on irreducible components; the Cartan pairings determine their relative root lengths. \(\square\)

The empty matrix gives the zero algebra. All arguments above then have empty sets of generators and roots; (6.1) gives dimension zero. Semisimplicity includes this case, while simplicity does not.

**Corollary 6.2 (classification).** Complex simple Lie algebras, up to isomorphism, correspond bijectively to
\[
A_n\ (n\ge1),\quad B_n\ (n\ge2),\quad
C_n\ (n\ge3),\quad D_n\ (n\ge4),\quad
E_6,E_7,E_8,F_4,G_2.
\]

**Proof.** The preceding root-decomposition and classification lessons give a finite Dynkin diagram for every semisimple algebra. For a connected diagram, Theorem 6.1 constructs a simple algebra with that root system, and Theorem 3.1 proves uniqueness. To see that a simple algebra's diagram is connected, its Chevalley generators belonging to distinct components commute, by Proposition 1.1; they would give disjoint nonzero ideals and a direct decomposition as in the theorem. Conversely a connected diagram gives a simple algebra by the theorem. The specified rank cutoffs remove \(B_1=C_1=A_1\), \(B_2=C_2\) and \(D_3=A_3\), and exclude the reducible \(D_2\). This proves both surjectivity and injectivity. \(\square\)

In particular any original semisimple \(\mathfrak g\) has exactly this Serre presentation. Proposition 1.1 gives a surjection \(\mathfrak g(A)\to\mathfrak g\); both have dimension \(r+|\Phi|\), so it is an isomorphism. The endpoint relations are therefore sufficient, not only necessary.

### 6.3. The rational presentation and scalar extension

**Corollary 6.3.** Let \(A\) be a finite-type Cartan matrix in our column-coroot convention. The same generators and relations (1.3)–(1.4), interpreted over \(\mathbb Q\), define a split semisimple Lie algebra \(\mathfrak g_{\mathbb Q}(A)\). Its dimension is \(r+|\Phi(A)|\), and
\[
\mathfrak g_{\mathbb Q}(A)\otimes_{\mathbb Q}\mathbb C
\cong\mathfrak g(A).
\tag{6.3}
\]
More generally its scalar extension to any characteristic-zero field has the same split root decomposition and is semisimple.

**Proof.** A free Lie algebra can be formed from the free vector space on bracketed words by imposing bilinearity, alternation and Jacobi. Imposing a presentation means further quotienting by the ideal generated by its relations. Tensoring with a field extension commutes with these quotients: the defining words and all their bracket multiples have exactly the same span after extending coefficients. Thus presentations commute with scalar extension, giving (6.3).

For completeness, finiteness descends without assuming it beforehand. Choose finitely many vectors in \(\mathfrak g_{\mathbb Q}(A)\) whose tensors span the finite-dimensional complex algebra. Their rational span \(E\) has \((\mathfrak g_{\mathbb Q}(A)/E)\otimes\mathbb C=0\). A nonzero rational vector remains nonzero after tensoring with \(\mathbb C\), as extending a basis shows. Hence the quotient is zero. Dimension is unchanged by field extension. The complex independence of the \(h_i\) proves their rational independence. Every bracket word has an integral root degree and is a joint eigenvector for their adjoint actions. The complex decomposition in Theorem 6.1 therefore descends to a rational zero-weight space spanned by the \(h_i\), and one-dimensional rational spaces indexed by exactly \(\Phi(A)\). Their weights have the prescribed integer values \(\alpha_i(h_j)=a_{ij}\).

The matrix of the Killing form over \(\mathbb Q\) becomes the complex Killing matrix in (6.3), so its determinant is nonzero. Over any characteristic-zero extension it remains nonzero, and [Cartan's criterion](RT-LIE-03.md) proves semisimplicity. Extending the rational weight decomposition supplies the same split Cartan and root spaces. This argument concerns field extensions; it makes no semisimplicity assertion in positive characteristic or over arbitrary rings. \(\square\)

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

The proofs above establish the isomorphism theorem and the finite-type Serre theorem for every complex semisimple Lie algebra, with arbitrary rank and any number of simple components. In particular the auxiliary free algebras, survival of the Cartan generators, stability of the Serre ideals, locally nilpotent reflection operators, absence of additional weights, and simplicity of each connected component have all been proved. The root decomposition and nonzero root-space brackets, finite root-system classification, and Cartan equivalence are the previously proved prerequisites.

The existence and uniqueness of the finite fundamental modules \(L(\omega_i)\) are proved in [the highest-weight lesson](RT-LIE-14.md#section-4). That result uses the Serre theorem in Section 6, and its proof uses no automorphism decomposition. This forward result dependency is therefore acyclic. A reader can return to this section after Lesson 14.

### The groups and the direction of the indices

Fix a Cartan subalgebra \(\mathfrak h\), a base \(\Delta=\{\alpha_1,\ldots,\alpha_r\}\), and normalized generators \(e_i,f_i,h_i\) with \(h_i=\alpha_i^\vee\). As throughout this lesson,

\[
a_{ij}=\alpha_i(h_j),\qquad
[h_i,e_j]=a_{ji}e_j,\qquad
(\operatorname{ad}e_i)^{1-a_{ji}}e_j=0\quad(i\ne j).
\]

Define \(D\) to be the group of permutations \(\sigma\) of the vertices satisfying

\[
a_{\sigma(i),\sigma(j)}=a_{ij}\qquad\text{for every }i,j.
\tag{9.2}
\]

This is the automorphism group of the directed Dynkin diagram, including permutations of isomorphic connected components. In particular, preserving only the unoriented multiple-edge graph does not suffice. For \(\sigma\in D\), the assignment

\[
\delta_\sigma(e_i)=e_{\sigma(i)},\qquad
\delta_\sigma(f_i)=f_{\sigma(i)},\qquad
\delta_\sigma(h_i)=h_{\sigma(i)}
\tag{9.3}
\]

preserves every Serre defining relation. The same assignment with \(\sigma^{-1}\) is its inverse. Theorem 6.1 and the presentation identification following it therefore give an automorphism \(\delta_\sigma\) of the actual algebra. Equality on the generators gives \(\delta_\sigma\delta_\tau=\delta_{\sigma\tau}\). The action is faithful because the \(h_i\) are independent.

Use the definition established in RT-LIE-10 §3:

\[
G=\operatorname{Int}(\mathfrak g)
=\left\langle\exp(\operatorname{ad}z):
\operatorname{ad}z\text{ is nilpotent}\right\rangle.
\]

Each displayed exponential is a finite polynomial. That lesson's Theorem 3.2 proves that this group is exactly the complex points of \(\operatorname{Aut}(\mathfrak g)^\circ\); it proves equality with the generated subgroup, not merely with its closure. Also \(G\) is normal in \(\operatorname{Aut}(\mathfrak g)\): for an automorphism \(b\),

\[
b\exp(\operatorname{ad}z)b^{-1}
=\exp(\operatorname{ad}(bz)),
\]

and \(\operatorname{ad}(bz)=b(\operatorname{ad}z)b^{-1}\) remains nilpotent.

### The scalar correction is inner

For \(c=(c_1,\ldots,c_r)\in(\mathbb C^\times)^r\), define \(t_c\) on the generators by

\[
t_c(e_i)=c_i e_i,\qquad
t_c(f_i)=c_i^{-1}f_i,\qquad
t_c(h_i)=h_i.
\tag{9.4}
\]

Homogeneity of the Serre relations gives an automorphism, with inverse \(t_{c^{-1}}\). On a root space of root \(\beta=\sum_i m_i\alpha_i\), it is multiplication by \(\prod_i c_i^{m_i}\); this follows first on homogeneous bracket words and then on their span. It fixes \(\mathfrak h\).

These formulas define a regular group homomorphism

\[
(\mathbb C^\times)^r\longrightarrow\operatorname{Aut}(\mathfrak g),
\qquad c\longmapsto t_c,
\]

because the finitely many matrix entries in a root-space basis are Laurent monomials. The source is a nonempty Zariski-open subset of affine \(\mathbb C^r\), so it is irreducible: two nonempty relatively open subsets have nonempty intersection by irreducibility of affine space. Its image is therefore connected and contains the identity, so it lies in the identity component. RT-LIE-10 Theorem 3.2 now proves \(t_c\in G\). This supplies the algebraic argument for innerness of the scalar correction.

The same correction can be written \(t_c=\exp(\operatorname{ad}H)\): choose complex logarithms \(b_i\) with \(e^{b_i}=c_i\), and use the simple-root basis of \(\mathfrak h^*\) to choose \(H\) with \(\alpha_i(H)=b_i\). On the root space of \(\beta\), this exponential acts by \(e^{\beta(H)}=\prod_i c_i^{m_i}\), and it fixes \(\mathfrak h\). No chosen branch or logarithm affects the resulting automorphism.

In fact these are exactly the automorphisms fixing \(\mathfrak h\) pointwise. Such an automorphism preserves every root space, so it sends \(e_i\) to \(c_i e_i\) and \(f_i\) to \(d_i f_i\). The equality \([e_i,f_i]=h_i\) and pointwise fixation of \(h_i\) imply \(c_i d_i=1\). It consequently agrees with \(t_c\) on every generator, and hence on \(\mathfrak g\). Write

\[
T=\{t_c:c\in(\mathbb C^\times)^r\}.
\]

The map \(c\mapsto t_c\) is injective because its values on the \(e_i\) recover the \(c_i\). Thus \(T\cong(\mathbb C^\times)^r\), and the pointwise stabilizer of \(\mathfrak h\) in the full automorphism group, and in \(G\), is \(T\).

### Finite modules detect a diagram permutation

For a finite-dimensional representation \(\rho:\mathfrak g\to\operatorname{End}(V)\) and an automorphism \(b\), let \(V^{b}\) denote its pullback, with action \(x\mapsto\rho(bx)\).

Every inner automorphism preserves the isomorphism class of \(V\). To prove this directly, first take \(b=\exp(\operatorname{ad}z)\), with \(\operatorname{ad}z\) nilpotent, and put \(A=\rho(z)\). Ordinary finite-matrix exponentials give

\[
\exp(A)\rho(x)\exp(-A)
=\sum_{n\ge0}\frac{(\operatorname{ad}A)^n\rho(x)}{n!}
=\rho\left(\exp(\operatorname{ad}z)x\right).
\tag{9.5}
\]

For completeness, the first equality follows by multiplying the absolutely convergent matrix series: induction gives

\[
(\operatorname{ad}A)^n B
=\sum_{k=0}^n(-1)^k\binom nk A^{n-k}BA^k.
\]

The representation identity gives \((\operatorname{ad}A)^n\rho(x)=\rho((\operatorname{ad}z)^n x)\), so the right side of (9.5) is actually finite. The invertible matrix \(\exp(A)\) intertwines the original and pulled-back actions. Applying this for each factor proves the assertion for every \(b\in G\). No integration of the representation to a Lie group is used.

Let \(\omega_i\) be the fundamental weights, characterized by \(\omega_i(h_j)=\delta_{ij}\), and put \(F_i=L(\omega_i)\). [Theorem 2.1](RT-LIE-14.md#theorem-2-1), [Theorem 3.1](RT-LIE-14.md#theorem-3-1) and [Theorem 4.1](RT-LIE-14.md#theorem-4-1) of RT-LIE-14 prove that these modules exist, are finite-dimensional and irreducible, and have pairwise distinct isomorphism classes. That highest-weight construction uses only §§1–6 of this lesson; the present automorphism argument is its later application. Under pullback by \(\delta_\sigma\), the original highest vector remains highest, because the simple raising generators are permuted. Its weight is

\[
(\omega_i\circ\delta_\sigma)(h_j)
=\omega_i(h_{\sigma(j)})
=\delta_{i,\sigma(j)}
=\omega_{\sigma^{-1}(i)}(h_j).
\]

The pullback is still irreducible and cyclic, so highest-weight uniqueness gives

\[
F_i^{\delta_\sigma}\cong F_{\sigma^{-1}(i)}.
\tag{9.6}
\]

If \(\delta_\sigma\) is inner, (9.5) makes the left side isomorphic to \(F_i\) for every \(i\). Pairwise distinct highest weights force \(\sigma(i)=i\) for every vertex. Therefore

\[
G\cap\delta(D)=\{1\}.
\tag{9.7}
\]

This argument also detects permutations of isomorphic simple components. A fundamental weight attached to one component and the corresponding weight attached to another are distinct weights of the fixed algebra, even when their modules have equal dimensions.

### Every automorphism has the required factorization

**Theorem 9.1.** For every complex semisimple Lie algebra, the normalized generators give an isomorphism

\[
\operatorname{Aut}(\mathfrak g)
\cong\operatorname{Int}(\mathfrak g)\rtimes D.
\tag{9.1}
\]

The action of \(D\) on the inner group is conjugation by the lifts \(\delta_\sigma\), and every automorphism factors uniquely as an inner automorphism followed by one such lift.

**Proof of existence.** Let \(b\in\operatorname{Aut}(\mathfrak g)\). An automorphism takes a Cartan subalgebra to a Cartan subalgebra, since it preserves nilpotence and the Lie-algebra normalizer condition. RT-LIE-10 Theorem 4.2 supplies \(u_0\in G\) with \(u_0b(\mathfrak h)=\mathfrak h\). Set \(b_0=u_0b\).

The induced root map is

\[
b_{0*}(\alpha)=\alpha\circ(b_0|_{\mathfrak h})^{-1}.
\]

Transporting the weight equation proves that it permutes the roots. Automorphisms preserve the Killing form, since their adjoint matrices are conjugate. Hence this map preserves the induced root inner product, normalized coroots and all Cartan pairings, by the explicit argument in RT-LIE-10 Corollary 5.1. In particular \(b_{0*}\Delta\) is another base.

RT-LIE-08 Theorem 5.1 gives a \(w\in W\) with \(wb_{0*}\Delta=\Delta\). The simple-reflection operators \(T_i\) of Proposition 5.1 in this lesson are products of exponentials of the ad-nilpotent generators \(e_i,f_i\). Thus they belong to \(G\), and they induce \(s_i\) on the root space. A product along any expression for \(w\) gives \(n_w\in G\) inducing \(w\); independence of the expression is unnecessary.

Set \(y=n_wb_0\). Its root map permutes the simple roots, say \(y_*(\alpha_i)=\alpha_{\sigma(i)}\). Preservation of coroots gives \(y(h_i)=h_{\sigma(i)}\). Therefore

\[
a_{ij}=\alpha_i(h_j)
=\alpha_{\sigma(i)}(h_{\sigma(j)})
=a_{\sigma(i),\sigma(j)},
\]

so \(\sigma\in D\) with the full directed convention (9.2). The automorphism \(\delta_\sigma^{-1}y\) fixes every \(h_i\), hence all of \(\mathfrak h\), pointwise. The scalar-correction argument identifies it with some \(t_c\in G\). Consequently

\[
b=u_0^{-1}n_w^{-1}\delta_\sigma t_c
=\left(u_0^{-1}n_w^{-1}\delta_\sigma t_c\delta_\sigma^{-1}\right)
\delta_\sigma.
\]

The parenthesized factor lies in \(G\) because \(G\) is normal. This proves existence for every rank and every component decomposition.

**Proof of uniqueness and the group law.** If \(u\delta_\sigma=v\delta_\tau\), then \(\delta_{\sigma\tau^{-1}}=u^{-1}v\) is inner. Equation (9.7) gives \(\sigma=\tau\), and then \(u=v\). Normality gives

\[
(u,\sigma)(v,\tau)
=\bigl(u\delta_\sigma v\delta_\sigma^{-1},\sigma\tau\bigr),
\]

which is exactly the semidirect-product law. \(\square\)

The empty root system corresponds to \(\mathfrak g=0\); the inner group, the diagram group and the automorphism group are all trivial, so the theorem includes this case.

### The Cartan normalizer follows from the proof

Here is the precise normalizer statement, proved without using it in the preceding factorization. Define

\[
N_G(\mathfrak h)=\{u\in G:u\mathfrak h=\mathfrak h\},\qquad
Z_G(\mathfrak h)=\{u\in G:uH=H\text{ for all }H\in\mathfrak h\}.
\]

We already proved \(Z_G(\mathfrak h)=T\). The root action maps \(N_G(\mathfrak h)\) to root-system automorphisms. For \(u\in N_G(\mathfrak h)\), repeat the base-alignment step with no Cartan transporter: choose \(w\) with \(wu_*\Delta=\Delta\). The same scalar argument writes \(n_wu=\delta_\sigma t_c\). Both \(n_wu\) and \(t_c\) are inner; therefore \(\delta_\sigma\) is inner. Equation (9.7) forces \(\sigma=1\). Thus \(u_*\in W\). Conversely each element of \(W\) is induced by its constructed lift \(n_w\). The kernel fixes every root and hence all of \(\mathfrak h\), because the roots span \(\mathfrak h^*\). The kernel is therefore \(T\), proving

\[
N_G(\mathfrak h)/Z_G(\mathfrak h)
=N_G(\mathfrak h)/T\cong W.
\tag{9.8}
\]

The normalizer of \(T\) in \(G\) also equals \(N_G(\mathfrak h)\). Indeed, the common fixed space of \(T\) on \(\mathfrak g\) is exactly \(\mathfrak h\), since a nonzero root has a nontrivial Laurent-monomial character. Normalizing \(T\) therefore preserves \(\mathfrak h\). Conversely an automorphism preserving \(\mathfrak h\) conjugates its pointwise stabilizer \(T\) to itself. This proves the group-normalizer assertion as well. It does not assert that the normalizer extension (9.8) splits as groups: the reflection lifts were never required to satisfy the Coxeter relations in \(G\).

No Borel conjugacy assertion enters this proof. The only Cartan conjugacy assertion is exactly RT-LIE-10 Theorem 4.2, whose proof uses finite nilpotent exponentials and its stated algebraic-geometric inputs.

The planned algebraic-geometry lesson *Isomorphism and existence theorems for split reductive group schemes* develops the group version. Its additional data are the character and cocharacter lattices; a root system alone does not determine a reductive group. The Serre presentation here is a Lie-algebra statement over \(\mathbb C\), and does not assert the same semisimplicity result in positive characteristic.

For comparison with the wider algebraic-geometry programme, the [official Stacks project](https://stacks.math.columbia.edu/) remains the reference project. The [AI Integrated Stacks Project reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) presents unofficial AI drafts; those drafts are not maintainer-reviewed Stacks results. No result from that reader is needed as an external proof in this lesson.

**References.**

- P. Etingof, [*Lie groups and Lie algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), for diagram automorphisms and their action on fundamental representations. The finite-matrix intertwining argument and the Cartan normalizer calculation are supplied here.

- P. Etingof, [*Lie Groups and Lie Algebras I*, MIT OpenCourseWare, Fall 2020](https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/): §24, Theorems 24.1–24.2 and Lemma 24.3, for the isomorphism and Serre theorems; §§13–14 for ordered enveloping-algebra words and free Lie algebras. These notes use the row-coroot Cartan convention, the transpose of (1.2).
- J. S. Milne, [*Algebraic Groups*](https://www.jmilne.org/math/Books/iAG2022.pdf), Chapter 23: §23d on pinnings, §23e on automorphisms and §23h on existence. The 2021 revision of the book is used here. Theorem 23.63 states the Cartan–Killing classification, and its first proof points to Serre presentations in other works.
