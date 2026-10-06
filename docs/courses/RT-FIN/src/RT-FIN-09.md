# Frobenius groups and Frobenius's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

A transitive permutation group can have a strikingly rigid fixed-point pattern: every nonidentity element fixes at most one point. Elements that fix a point lie in a conjugate of a point stabilizer. The remaining elements, together with the identity, turn out to form a normal subgroup.

Closure of this set under multiplication is far from apparent. Character theory will supply a representation whose kernel is exactly that set. The decisive step is to construct irreducible characters by subtracting an induced trivial character and then restoring the correct degree.

Historical references for character methods and normal-complement questions are Frobenius's *Über auflösbare Gruppen IV* and Schur's *Neuer Beweis eines Satzes über endliche Gruppen*. The proofs in this lesson proceed from the earlier course results listed below.

## Prerequisites and conventions

We use complex representations of finite groups. From *Characters and the orthogonality relations* we use the irreducible-character basis, the regular character and the degree-square identity. From *Induced representations and Frobenius reciprocity* we use the induction formula and reciprocity for class functions. The degree result and the last exercise use the Clifford correspondence from *Mackey theory and Clifford's theorem*.

Our inner product is linear in its first variable:

\[
\langle f,k\rangle_G=\frac1{|G|}\sum_{g\in G}f(g)\overline{k(g)}.
\tag{1}
\]

A generalized character is an integer linear combination of irreducible characters. It may have negative coefficients. An actual character has nonnegative integer coefficients.

## 1. Stabilizers that meet only at the identity

Let \(H<G\) satisfy

\[
H\cap gHg^{-1}=\{1\}\qquad(g\notin H).
\tag{2}
\]

When \(1<H<G\), we call \(H\) a **Frobenius complement** and \(G\) a **Frobenius group** for this action. We will also allow \(H=\{1\}\) in the theorem; that is the regular-action endpoint.

Consider the transitive action on \(G/H\). The stabilizer of \(gH\) is \(gHg^{-1}\). Condition (2) says exactly that a nonidentity element cannot fix both \(H\) and a different coset. Conjugating this assertion proves that it cannot fix any two distinct cosets. Conversely, the at-most-one-fixed-point property implies (2). The action is faithful: its kernel is contained in every stabilizer, including \(H\) and \(gHg^{-1}\) for any \(g\notin H\), whose intersection is trivial.

Define the set

\[
S=\left(G\setminus\bigcup_{g\in G}gHg^{-1}\right)\cup\{1\}.
\tag{3}
\]

Its nonidentity elements are exactly the elements with no fixed coset. At this point \(S\) is only a conjugation-invariant set. We have not assumed it is a subgroup.

Some basic examples illustrate the condition.

- For the affine group of \(\mathbb F_q\), \(q>2\), a point stabilizer consists of maps \(u\mapsto au\). An affine map fixing two distinct points has \(a=1\) and translation part zero, so is the identity. A nonzero translation has no fixed point; a map \(u\mapsto au+b\) with \(a\ne1\) has the unique fixed point \(b/(1-a)\).
- In the natural action of \(A_4\) on four letters, a nonidentity three-cycle fixes one letter and a double transposition fixes none. The stabilizer of a letter is \(C_3\), and (2) holds.
- For odd \(n\geq3\), \(D_n\) acts on \(\mathbb Z/n\mathbb Z\) by translations and \(j\mapsto-j\). A reflection \(j\mapsto b-j\) fixes exactly the solution of \(2j=b\), while a nontrivial rotation fixes none. A reflection subgroup \(C_2\) is a complement. For even \(n\), the reflection \(j\mapsto-j\) fixes both \(0\) and \(n/2\), so this action fails (2).

One can count \(S\) before proving closure. Conjugates indexed by distinct cosets of \(H\) have disjoint nonidentity parts: a common nonidentity element would fix two cosets. Therefore, writing \(m=|H|\) and \(n=[G:H]\), the union in (3) has \(1+n(m-1)\) elements, and

\[
|S|=mn-n(m-1)=n.
\tag{4}
\]

For \(H=\{1\}\), all the nonidentity stabilizer parts are empty and the same formula gives \(S=G\). Counting alone does not make \(S\) a subgroup.

## 2. An isometry for class functions of degree zero

For a class function \(\alpha\) on \(H\), induction is

\[
(\operatorname{Ind}_H^G\alpha)(g)
=\frac1{|H|}
\sum_{\substack{x\in G\\x^{-1}gx\in H}}\alpha(x^{-1}gx).
\tag{5}
\]

It is defined for arbitrary class functions, by the same formula as for characters.

**Lemma 2.1.** Suppose (2) holds. If \(\alpha,\beta\) are class functions on \(H\) with \(\alpha(1)=\beta(1)=0\), then

\[
\operatorname{Res}_H^G\operatorname{Ind}_H^G\alpha=\alpha,
\qquad
\langle\operatorname{Ind}_H^G\alpha,\operatorname{Ind}_H^G\beta\rangle_G
=\langle\alpha,\beta\rangle_H.
\tag{6}
\]

Moreover, the induced function vanishes on \(S\).

**Proof.** At \(1\), (5) is \([G:H]\alpha(1)=0\). For \(h\in H\setminus\{1\}\), a term in (5) can occur only if \(h\in H\cap xHx^{-1}\). Condition (2) forces \(x\in H\). There are \(|H|\) such terms, all equal to \(\alpha(h)\), since \(\alpha\) is a class function on \(H\). This proves the restriction identity at every element of \(H\).

Frobenius reciprocity for class functions, in the orientation appropriate to (1), gives

\[
\langle\operatorname{Ind}\alpha,\operatorname{Ind}\beta\rangle_G
=\langle\operatorname{Res}\operatorname{Ind}\alpha,\beta\rangle_H
=\langle\alpha,\beta\rangle_H.
\]

For \(s\in S\setminus\{1\}\), no conjugate of \(s\) belongs to \(H\), so the sum (5) is empty. Its value at \(1\) is already zero. \(\square\)

The degree-zero condition is essential. Inducing \(1_H\) gives the permutation character on \(G/H\), whose value at the identity is \([G:H]\), not \(1\).

## 3. A normal subgroup forced by characters

Fix \(\theta\in\operatorname{Irr}(H)\) and put \(d=\theta(1)\). Define

\[
\theta^\ast
=\operatorname{Ind}_H^G(\theta-d1_H)+d1_G.
\tag{7}
\]

The difference inside induction vanishes at \(1\). Formula (7) is an integer combination of characters, so is a generalized character of \(G\).

**Proposition 3.1.** Each \(\theta^\ast\) is an irreducible character of \(G\), with

\[
\theta^\ast(1)=d,\qquad
\operatorname{Res}_H^G\theta^\ast=\theta,\qquad
\theta^\ast(s)=d\quad(s\in S).
\tag{8}
\]

Distinct \(\theta\)'s give distinct \(\theta^\ast\)'s.

**Proof.** If \(\theta=1_H\), (7) gives \(1_G\), so all assertions hold. Otherwise set \(\alpha=\theta-d1_H\). Orthogonality on \(H\) gives

\[
\langle\alpha,\alpha\rangle_H=1+d^2,
\qquad
\langle\alpha,1_H\rangle_H=-d.
\]

Lemma 2.1 and reciprocity imply

\[
\begin{aligned}
\langle\theta^\ast,\theta^\ast\rangle_G
&=(1+d^2)+d(-d)+d(-d)+d^2\\
&=1.
\end{aligned}
\tag{9}
\]

Expand this generalized character as \(\sum_\chi a_\chi\chi\), with \(a_\chi\in\mathbb Z\). Its squared norm is \(\sum_\chi a_\chi^2=1\). Hence it is either an irreducible character or the negative of one. Since induction of \(\alpha\) has degree \([G:H]\alpha(1)=0\), its degree in (7) is \(d>0\). The negative possibility is excluded.

The restriction identity in Lemma 2.1 gives \(\theta-d1_H+d1_H=\theta\). Its vanishing assertion gives the constant value \(d\) on \(S\). Finally, equality of two such characters would imply equality of their restrictions to \(H\). \(\square\)

We need one elementary kernel test. If \(\chi\) is an actual character of degree \(D\), then

\[
g\in\ker\chi\quad\Longleftrightarrow\quad\chi(g)=D.
\tag{10}
\]

Here \(\ker\chi\) means the kernel of a representation affording \(\chi\). To prove the test, the eigenvalues of its finite-order operator at \(g\) are roots of unity. If their sum is \(D\), the sum of their real parts is \(D\); each real part is at most \(1\). Every eigenvalue is therefore \(1\). The operator is diagonalizable, so it is the identity. The converse is immediate.

**Theorem 3.2 (Frobenius).** If \(H<G\) satisfies (2), then the set \(S\) in (3) is a normal subgroup \(N\), and

\[
|N|=[G:H],\qquad N\cap H=\{1\},\qquad G=NH\simeq N\rtimes H.
\tag{11}
\]

**Proof.** Form the actual character

\[
\Xi=\sum_{\theta\in\operatorname{Irr}(H)}\theta(1)\theta^\ast.
\tag{12}
\]

It has degree \(\sum_\theta\theta(1)^2=|H|\). For \(s\in S\), Proposition 3.1 gives \(\Xi(s)=|H|\). On \(H\setminus\{1\}\), its restriction is the regular character of \(H\), so is zero. Every element outside \(S\) is conjugate to a nonidentity element of \(H\). Thus

\[
\Xi(g)=
\begin{cases}
|H|,&g\in S,\\
0,&g\notin S.
\end{cases}
\tag{13}
\]

By (10), \(S=\ker\Xi\). This proves it is a normal subgroup, without assuming any closure property. Equivalently, it is \(\bigcap_\theta\ker\theta^\ast\), since (12) is a direct sum of positive numbers of copies of the representations affording these characters.

Its order is (4). There is also a character calculation of the order: the distinct irreducibles in (12) give \(\langle\Xi,\Xi\rangle_G=\sum_\theta\theta(1)^2=|H|\), while (13) gives that norm as \(|H|^2|N|/|G|\). Hence \(|N|=|G|/|H|\).

By definition, \(N\cap H=\{1\}\). Since \(N\) is normal, \(NH\) is a subgroup, and its order is \(|N||H|=|G|\), so it is all of \(G\). Conjugation by \(H\) on \(N\), together with this unique factorization, realizes the semidirect product in (11). \(\square\)

The subgroup \(N\) is the **Frobenius kernel**. The characters \(\theta^\ast\) have a simple interpretation after the theorem: they are the characters of \(G/N\simeq H\), inflated to \(G\). Their restrictions are \(\theta\), and they kill \(N\), so this follows from the unique factorization \(G=NH\).

## 4. Fixed-point-free conjugation and irreducible degrees

**Proposition 4.1.** In a Frobenius group \(G=N\rtimes H\),

\[
C_N(h)=\{1\}\quad(h\in H\setminus\{1\}),
\qquad
|N|\equiv1\pmod{|H|}.
\tag{14}
\]

In particular, \(|N|\) and \(|H|\) are coprime.

**Proof.** If \(n\in N\setminus\{1\}\) commutes with a nonidentity \(h\in H\), then \(h\in H\cap nHn^{-1}\). Since \(n\notin H\), this contradicts (2). Thus the stabilizer in \(H\) of every element of \(N\setminus\{1\}\), under conjugation, is trivial. Those elements partition into orbits of size \(|H|\), proving the congruence. A common divisor of \(|N|\) and \(|H|\) divides \(1\). \(\square\)

The same argument shows

\[
C_N(g)=\{1\}\quad(g\in G\setminus N).
\tag{15}
\]

Indeed, such \(g\) is conjugate to a nonidentity element of \(H\), and normality of \(N\) allows us to conjugate the centralizer assertion.

We will transfer this action from elements to irreducible characters. The transfer is a linear-algebra fact sometimes called Brauer's permutation lemma, and we prove the instance needed here.

**Lemma 4.2.** An automorphism \(u\) of a finite group \(K\) fixes the same number of conjugacy classes as it fixes irreducible characters.

**Proof.** Let \(u\) act on the space of class functions by \(f\mapsto f\circ u^{-1}\). In the basis of indicator functions of conjugacy classes, it is a permutation matrix whose trace is the number of fixed classes. In the irreducible-character basis, it is also a permutation matrix: precomposing a representation with \(u^{-1}\) preserves irreducibility and transports its character accordingly. Its trace in that basis counts fixed irreducible characters. A linear operator has the same trace in every basis, proving the assertion. \(\square\)

For \(h\in H\setminus\{1\}\), the only \(N\)-conjugacy class fixed by conjugation by \(h\) is the identity class. Suppose a nonidentity \(n\in N\) had its class fixed. Then \(hnh^{-1}=ana^{-1}\) for some \(a\in N\). The element \(a^{-1}h\) centralizes \(n\) and lies outside \(N\), contradicting (15). Lemma 4.2 now says that the only irreducible character of \(N\) fixed by \(h\) is the trivial one. Consequently \(H\) acts freely on
\(\operatorname{Irr}(N)\setminus\{1_N\}\).

**Theorem 4.3.** The irreducible representations of \(G\) are:

1. the inflations of the irreducibles of \(H\simeq G/N\);
2. one representation \(\operatorname{Ind}_N^G W\) for each \(H\)-orbit of nontrivial irreducibles \(W\) of \(N\).

The representations in the second list are irreducible and have degree \(|H|\dim W\). In particular, every irreducible representation that does not kill \(N\) has degree divisible by \(|H|\).

**Proof.** Conjugation by \(N\) fixes the isomorphism class of every \(N\)-representation. The free \(H\)-action just proved therefore makes the inertia group of a nontrivial \(W\) exactly \(N\). Clifford correspondence makes \(\operatorname{Ind}_N^G W\) irreducible. Its dimension is \([G:N]\dim W=|H|\dim W\).

If an irreducible \(V\) does not kill \(N\), its restriction contains a nontrivial irreducible \(W\). Otherwise its completely reducible restriction would be a sum of trivial representations, meaning \(N\) acts identically. The same correspondence identifies \(V\) with \(\operatorname{Ind}_N^G W\). Its \(N\)-constituents form the orbit of \(W\), each once, so two such inductions are isomorphic precisely for the same orbit. The remaining irreducibles factor through \(G/N\), giving the first list. \(\square\)

This gives more than a divisibility test. To build the remaining representations, one only needs the irreducibles of \(N\) and the free action of the complement on their nontrivial types. If \(N\) is abelian, every representation in the second list has degree exactly \(|H|\).

## 5. Computing the kernel and the remaining characters

### Affine transformations

The affine group of \(\mathbb F_q\), \(q>2\), has complement \(\mathbb F_q^\times\). The fixed-point calculation in Section 1 says that \(S\setminus\{1\}\) consists exactly of nonzero translations. Thus the theorem identifies the kernel with \((\mathbb F_q,+)\).

The complement acts transitively on its \(q-1\) nontrivial characters, as shown in *Groups with an abelian normal subgroup: the little-group method*. Theorem 4.3 gives one remaining irreducible of degree \(q-1\), alongside the \(q-1\) inflated characters of the complement. At \(q=2\), the complement is trivial; this is the regular-action endpoint, with kernel \(C_2\) and two linear characters.

### The alternating group

In \(A_4\), the elements with no fixed letter are the three double transpositions, so \(N=V_4\). The complement \(C_3\) cycles the three nontrivial characters of \(V_4\). Thus Theorem 4.3 gives the degree-three representation and the three characters inflated from \(C_3\). The kernel congruence reads \(4\equiv1\pmod3\).

### A nonabelian group of order twenty-one

Let \(G=\mathbb F_7\rtimes\{1,2,4\}\), acting by affine transformations. Nonidentity multipliers again have exactly one fixed point, and nonzero translations have none. Its complement has order three and its kernel is \(\mathbb F_7\).

Take \(\zeta=e^{2\pi i/7}\) and \(\lambda_t(b)=\zeta^{tb}\). The nontrivial kernel characters split into the two complement orbits

\[
\{1,2,4\},\qquad \{3,5,6\}.
\]

There are three linear characters from the quotient and two irreducibles of degree three. For either orbit \(O\), induction from the translation subgroup gives the character

\[
\chi_O(b,a)=
\begin{cases}
\displaystyle\sum_{t\in O}\zeta^{tb},&a=1,\\
0,&a\ne1.
\end{cases}
\tag{16}
\]

For \(a=1\), the restriction of induction is the sum of the three conjugate kernel characters. For \(a\ne1\), no conjugate of \((b,a)\) belongs to the kernel, so the induction formula is zero. This proves (16) on every element. The degree-square check is \(3\cdot1^2+2\cdot3^2=21\), and the congruence is \(7\equiv1\pmod3\).

## 6. Exercises with complete solutions

**Exercise 1.** Verify the kernel theorem directly for \(A_4\) and \(D_5\), including the semidirect decompositions.

**Solution.** For \(A_4\), take the stabilizer \(H=\langle(123)\rangle\) of \(4\). Its nonidentity elements and their conjugates are precisely the eight three-cycles. The remaining three nonidentity elements are the double transpositions, so the set (3) is \(V_4\). This is a normal subgroup: conjugation permutes the three double transpositions, and the product of two distinct ones is the third. Its intersection with \(H\) is trivial, and \(4\cdot3=12\) shows \(A_4=V_4H\). No nonidentity element fixes two letters, verifying (2).

For \(D_5=\langle r,s\rangle\), take \(H=\langle s\rangle\). Conjugating \(s\) by \(r^j\) gives \(r^{2j}s\); multiplication by \(2\) modulo \(5\) is a bijection, so these are all five reflections. Distinct subgroups generated by reflections meet only at the identity. The elements outside their union are the four nonidentity rotations, so (3) is \(\langle r\rangle\simeq C_5\). It is normal by \(srs^{-1}=r^{-1}\), meets \(H\) trivially and gives \(D_5=C_5\rtimes C_2\).

**Exercise 2.** Prove \(|N|\equiv1\pmod{|H|}\) using the conjugation action, rather than character degrees.

**Solution.** Let \(n\in N\setminus\{1\}\). If \(h\in H\) fixes it under conjugation, then \(h\in H\cap nHn^{-1}\). Since \(N\cap H=\{1\}\), the element \(n\) is outside \(H\), and (2) forces \(h=1\). The orbit-stabilizer formula therefore gives orbit size \(|H|\) for every such \(n\). If there are \(r\) orbits, then \(|N|-1=r|H|\). This is the congruence, and it also proves the orders of kernel and complement are coprime.

**Exercise 3.** Prove both assertions of Lemma 2.1 by double cosets and reciprocity.

**Solution.** Apply Mackey's restriction formula to the class function \(\alpha\), extended linearly from characters. The identity double coset contributes \(\alpha\). Every other representative \(g\notin H\) has intersection \(H\cap gHg^{-1}=\{1\}\). The restriction of its conjugate inducing function to this intersection is its value \(\alpha(1)=0\), so its induced contribution is zero. Therefore \(\operatorname{Res}_H^G\operatorname{Ind}_H^G\alpha=\alpha\) as a class function.

For completeness, arbitrary class functions admit the irreducible-character expansion from the prerequisites, so applying the character version linearly and conjugate-linearly in the inner product is valid. Reciprocity now gives
\(\langle\operatorname{Ind}\alpha,\operatorname{Ind}\beta\rangle_G
=\langle\operatorname{Res}\operatorname{Ind}\alpha,\beta\rangle_H
=\langle\alpha,\beta\rangle_H\).
This proves the full complex-valued statement, not merely its restriction to generalized characters.

**Exercise 4.** Show that an irreducible character of \(G\) whose representation does not kill \(N\) has degree a multiple of \(|H|\).

**Solution.** First, \(C_N(g)=\{1\}\) for \(g\notin N\): conjugate \(g\) into \(H\setminus\{1\}\) and use the trivial-intersection argument of Exercise 2. If \(h\in H\setminus\{1\}\) fixed the \(N\)-class of some \(n\ne1\), an equation \(hnh^{-1}=ana^{-1}\) with \(a\in N\) would make \(a^{-1}h\notin N\) centralize \(n\), a contradiction.

Thus \(h\) fixes exactly one conjugacy class of \(N\). Its action on class functions has trace one in the conjugacy-class indicator basis. In the irreducible-character basis the trace counts fixed irreducibles; the trivial character is always fixed, so no other irreducible is fixed. This proves that \(H\) acts freely on all nontrivial irreducible types of \(N\).

Choose one such constituent \(W\) of the given representation \(V|_N\); it exists because complete reducibility would otherwise make \(N\) act trivially. Inner conjugations by \(N\) preserve \(W\)'s type, while no nonidentity element of \(H\) does, so its inertia group is \(N\). Clifford correspondence gives \(V\simeq\operatorname{Ind}_N^G W\), and hence
\(\dim V=[G:N]\dim W=|H|\dim W\).
This proves the claimed divisibility with its precise source.

## What this lesson does not prove

The character orthogonality, induction, Mackey and Clifford results listed under prerequisites. Every new assertion used about Frobenius groups, their kernels, the transferred action on characters and their irreducible degrees is proved here.

## References

- Ferdinand Georg Frobenius, [*Über auflösbare Gruppen IV*](https://archive.org/details/sitzungsberichte1901deut/page/1216/mode/1up), Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin (1901), 1216–1230. A historical treatment of conjugacy and normal-complement questions.
- Issai Schur, [*Neuer Beweis eines Satzes über endliche Gruppen*](https://archive.org/details/sitzungsberichte1902deut/page/1013/mode/1up), Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin (1902), 1013–1019. A historical proof for the conjugacy and commutator-order hypotheses stated in that paper.
