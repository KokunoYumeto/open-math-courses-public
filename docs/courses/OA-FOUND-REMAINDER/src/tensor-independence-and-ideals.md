# Tensor independence and ideals

*Written by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A tensor product combines two systems, but a commuting action can identify some of their joint observables. This lesson studies when that happens. We first establish algebraic independence for a factor and its commutant, then use the smallest tensor norm to study simple algebras and ideals. A free-group example gives an explicit difference between separate and commuting actions.

Prerequisites are [recovery of commuting factor actions](../reader/tensor-norms-and-independent-systems.html#1-recovering-the-two-actions), [the full minimality and pure-set/ideal proofs](../reader/states-ideals-and-the-smallest-tensor-norm.html#3-the-lower-bound-for-every-c-norm), and [the double commutant theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#OA-FND-BI-07). Freely readable treatments are Courtney, Gillaspy and Ismert’s *Notes on C\*-algebras* and Blackadar’s *Operator Algebras*. Section 4 computes both exact free-group norms directly by unitary absorption and the tree estimate. We use the word *factor* for a von Neumann algebra with scalar centre, and *simple* for a nonzero C*-algebra with no proper nonzero closed two-sided ideal.

## 1. A factor is algebraically independent of its commutant

**Theorem 1.1.** If \(M\subseteq B(H)\) is a factor, multiplication is an injective *-homomorphism
\[
M\odot M'\longrightarrow B(H),
\qquad \sum_i a_i\otimes b_i\longmapsto\sum_i a_ib_i.
\tag{1.1}
\]

**Proof.** Suppose \(\sum_{i=1}^n a_ib_i=0\), with \(a_i\in M,b_i\in M'\). On \(H^n\), let \(C\xi=(b_1\xi,\ldots,b_n\xi)\), let \(R(\eta_1,\ldots,\eta_n)=\sum_i a_i\eta_i\), and let \(V\) be the closed span of \((c\otimes1)C\xi\) for \(c\in M'\). Because each \(b_i\) commutes with \(M\), \(V\) is invariant under the diagonal actions of \(M\) and \(M'\), as well as their adjoints. Its projection \(P\) therefore commutes with both actions.

The algebra generated weakly by \(M,M'\) is all of \(B(H)\): its commutant is \(M\cap M'=\mathbb C1\). Thus \(P=1\otimes p\) for a scalar matrix \(p=[p_{ij}]\in M_n(\mathbb C)\). This last assertion can also be seen entry by entry: each entry of \(P\) commutes with every operator of \(B(H)\), so is scalar.

Since \(RC=0\) and \(R(c\otimes1)=cR\) for \(c\in M'\), \(R\) annihilates \(V\). Hence \(RP=0\). Also \(PC=C\). Entrywise these identities read
\[
\sum_i a_ip_{ij}=0,
\qquad
b_i=\sum_jp_{ij}b_j.
\]
Consequently
\[
\sum_i a_i\otimes b_i
=\sum_j\Big(\sum_i p_{ij}a_i\Big)\otimes b_j=0.
\]
Multiplication and involution are preserved because the two algebras commute. \(\square\)

The result is algebraic. It does not say that multiplication is continuous for the spatial norm. That additional question is substantial.

## 2. Simplicity survives the spatial tensor product

**Theorem 2.1.** If \(A,B\) are simple C*-algebras, with or without units, then \(A\otimes_{\min}B\) is simple.

**Proof.** Let \(r\) be an irreducible nondegenerate representation of the tensor product. Recover commuting nondegenerate representations \(r_A,r_B\). Both are nonzero and hence faithful, by simplicity. Put \(M=r_A(A)''\). The algebra \(r_B(B)\) lies in \(M'\). Any central element of \(M\) commutes with both factor images, hence with \(r(A\otimes_{\min}B)\), so is scalar. Thus \(M\) is a factor.

Theorem 1.1 shows that multiplication is injective on \(r_A(A)\odot r_B(B)\). Since both recovered maps are algebraically injective, \(r\) is injective on \(A\odot B\). Therefore \(\gamma(x)=\|r(x)\|\) is a C*-norm on the algebraic tensor product. Minimality gives
\[
\|x\|_{\min}\le\|r(x)\|\le\|x\|_{\min}.
\]
So \(r\) is isometric on the dense algebraic subalgebra, hence faithful on the completion.

If the completion had a proper nonzero closed ideal, its nonzero quotient would have an irreducible representation. Pulling it back would give an irreducible representation with nonzero kernel, contradicting what we proved. \(\square\)

## 3. Every nonzero ideal contains a product of two ideals

In this section \(A,B\) are unital. For a closed ideal \(I\subseteq A\otimes_{\min}B\), put
\[
S_I=\{(\varphi,\psi)\in P(A)\times P(B):
(\varphi\otimes\psi)(I)=0\}.
\]
It is relatively closed. It is also invariant under independent unitary conjugations, since \(I\) is an ideal.

**Theorem 3.1.** Every nonzero closed ideal \(I\) of \(A\otimes_{\min}B\) contains \(J_A\odot J_B\) for some nonzero closed ideals \(J_A\subseteq A,J_B\subseteq B\). Thus it contains a nonzero elementary tensor of positive elements.

**Proof.** Product pure states separate positive elements. Indeed, the faithful spatial representation obtained by summing all pure-state GNS representations in each factor has blocks \(\pi_\varphi\otimes\pi_\psi\). If a positive operator in every block has zero expectation on every product vector, its positive square root annihilates every product vector, hence the whole tensor space. Within each irreducible factor representation, unitary density approximates any unit vector by an orbit vector of the cyclic vector. Thus zero values of every product pure state imply these zero expectations. Faithfulness gives that the positive element is zero.

Choose \(0\ne z\in I_+\). Some product pure state has positive value on \(z\), so \(S_I\) is proper. An open rectangle in its complement can, as in the minimality proof, be enlarged by independent unitary translates. Denote the resulting open sets by \(U,V\). The pure-state ideal correspondence supplies nonzero ideals \(J_A,J_B\) whose annihilators are \(P(A)\setminus U\) and \(P(B)\setminus V\).

Let \(r\) be any irreducible representation annihilating \(I\). Its recovered representations have commuting ranges \(C=r_A(A)\), \(D=r_B(B)\), and \(r_A(A)''\) is a factor, by the same centre argument as in Theorem 2.1. Multiplication is algebraically injective on \(C\odot D\), so the operator norm of this commuting action is a C*-norm there. The minimality theorem makes every product of pure states of \(C,D\) continuous for that norm.

If neither \(r_A\) nor \(r_B\) annihilated the respective ideal, choose \(a\in(J_A)_+,b\in(J_B)_+\) with nonzero images, and pure states \(\alpha\) of \(C\), \(\beta\) of \(D\) positive on those images. The product \(\alpha\otimes\beta\) extends to a state on \(r(A\otimes_{\min}B)\). Pulling back gives the product of pure states \(\varphi=\alpha\circ r_A\), \(\psi=\beta\circ r_B\) of \(A,B\), and that product annihilates \(I\). Purity of the pullbacks follows because each factor map is onto its image. But \(\varphi\in U,\psi\in V\), contradicting that \(U\times V\) misses \(S_I\).

Thus every irreducible representation annihilating \(I\) annihilates \(J_A\odot J_B\). Irreducible representations separate the quotient by \(I\), proving the containment. Choose nonzero positive elements in both ideals for the final assertion. \(\square\)

**Corollary 3.2.** Let commuting unital C*-subalgebras \(A,B\) generate \(C\). Suppose one factor is commutative and \(ab=0\), for \(a\in A,b\in B\), forces \(a=0\) or \(b=0\). Then multiplication identifies \(A\otimes_{\min}B\) with \(C\).

**Proof.** The maximal and minimal products agree when one factor is commutative. The universal product map is onto \(C\). If its kernel were nonzero, Theorem 3.1 would supply a nonzero elementary tensor in it, contradicting the assumed absence of zero products. \(\square\)

## 4. Four unitaries exhibit two different norms

Let \(G\) be the free group on two generators \(s,t\). On \(\ell^2(G)\), define
\[
\lambda_g\delta_h=\delta_{gh},
\qquad
\rho_g\delta_h=\delta_{hg^{-1}}.
\]
Both are unitary representations, and their ranges commute. Let \(A=C^*(\lambda(G))\), \(B=C^*(\rho(G))\), and \(S=\{s,s^{-1},t,t^{-1}\}\). Consider
\[
x=\sum_{g\in S}\lambda_g\otimes\rho_g\in A\odot B.
\]

**Proposition 4.1.** For this tensor,
\[
\|x\|_{\max}=4,
\qquad
\|x\|_{\min}=2\sqrt3.
\tag{4.1}
\]

**Proof.** In the commuting action on \(\ell^2(G)\), each \(\lambda_g\rho_g\) fixes \(\delta_e\). Thus the product action sends \(x\) to an operator with eigenvalue four. The sum of four unitaries has norm at most four, so the maximal norm is four.

For the spatial norm, define the unitary
\[
U(\delta_h\otimes\eta)=\delta_h\otimes\rho_h^{-1}\eta.
\]
Direct calculation gives \(U(\lambda_g\otimes\rho_g)U^*=\lambda_g\otimes1\). The two concrete representations are faithful by definition of \(A,B\), so the spatial norm of \(x\) equals the norm of the adjacency operator
\[
T=\sum_{g\in S}\lambda_g
\]
on the four-regular Cayley tree.

Root the tree at \(e\) and put \(w(h)=3^{-|h|/2}\). For a nonroot vertex the sum of neighboring weights divided by its own weight is
\[
\sqrt3+3/\sqrt3=2\sqrt3;
\]
at the root it is \(4/\sqrt3<2\sqrt3\). The weighted Schur estimate gives \(\|T\|\le2\sqrt3\). To check that estimate directly, for a finitely supported \(v\), bound each edge term using
\[
2|v(h)v(k)|\le
\frac{w(k)}{w(h)}|v(h)|^2+
\frac{w(h)}{w(k)}|v(k)|^2.
\]
Sum over unoriented edges. This bounds \(|\langle Tv,v\rangle|\) by \(2\sqrt3\|v\|^2\); self-adjointness and density give the operator bound.

For the reverse inequality truncate \(w\) to the ball of radius \(N\), obtaining \(w_N\). There are \(4\cdot3^{n-1}\) vertices at distance \(n\ge1\), so
\[
\|w_N\|^2=1+\frac43N,
\qquad
\langle Tw_N,w_N\rangle=\frac8{\sqrt3}N.
\]
The Rayleigh quotients tend to \(2\sqrt3\). This proves (4.1). \(\square\)

The example proves failure of uniqueness of the C*-tensor norm with an explicit element. It does not require a classification of ideals in the commuting-action algebra.

## 5. Exercises with solutions

**Exercise 5.1 (first step).** Let \(A=\mathbb C\oplus\mathbb C\) and \(B=M_3(\mathbb C)\). Describe the tensor product and all its closed ideals. Which ideals are generated by one elementary tensor?

**Solution.** The tensor product is \(M_3\oplus M_3\), with \((\alpha,\beta)\otimes b\mapsto(\alpha b,\beta b)\). Matrix algebras are simple, so the closed ideals are \(0\), \(M_3\oplus0\), \(0\oplus M_3\), and the whole algebra. The three nonzero ideals are generated respectively by \((1,0)\otimes1\), \((0,1)\otimes1\), and \((1,1)\otimes1\). This also shows that the nonzero ideals in Theorem 3.1 need not be the whole factors.

**Exercise 5.2 (application).** In a representation of \(M_2\otimes M_3\), recover the factor actions when the representation has a zero summand. Explain the role of the active support.

**Solution.** A nondegenerate representation of \(M_6\) is a multiplicity representation on \(\mathbb C^6\otimes L\). Under \(\mathbb C^6=\mathbb C^2\otimes\mathbb C^3\), the recovered actions are \(a\otimes1_3\otimes1_L\) and \(1_2\otimes b\otimes1_L\). If a zero summand \(L_0\) is added, the original representation vanishes there. Choosing both recovered actions zero on \(L_0\) gives their common active support. The algebraic products alone cannot determine arbitrary independent actions on a summand where all products vanish; this is why uniqueness is asserted on the nondegenerate part.

**Exercise 5.3 (further step).** Give the same construction as Section 4 for a free group on \(d\ge2\) generators. Compute the maximal and minimal norms of the sum over the \(2d\) generators and their inverses.

**Solution.** Put \(q=2d-1\). The commuting action fixes \(\delta_e\), giving maximal norm \(2d\). The same unitary absorption reduces the spatial operator to adjacency on the \(2d\)-regular tree. The weight \(q^{-|h|/2}\) gives neighboring-weight ratio \(2\sqrt q\) away from the root and \(2d/\sqrt q\le2\sqrt q\) at the root. The latter inequality is \(2d\le2(2d-1)\). Thus the norm is at most \(2\sqrt q\). Truncating the weight gives
\[
\|w_N\|^2=1+\frac{2d}{q}N,
\qquad
\langle Tw_N,w_N\rangle=\frac{4d}{\sqrt q}N,
\]
whose quotient tends to \(2\sqrt q\). Hence the minimal norm is \(2\sqrt{2d-1}\), strictly below \(2d\) for \(d\ge2\).

## References

- [Courtney–Gillaspy–Ismert] K. Courtney, E. Gillaspy and L. Ismert, *Notes on C\*-algebras*, GOALS lecture notes, available from [IPAM, UCLA](https://www.ipam.ucla.edu/wp-content/uploads/2024/07/Notes_and_Exercises_for_GOALS.pdf).
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, freely accessible corrected manuscript, [author's PDF](https://bruceblackadar.com/Mathematics/Cycr.pdf).
