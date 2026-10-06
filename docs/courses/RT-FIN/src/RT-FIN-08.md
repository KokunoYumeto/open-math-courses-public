# Groups with an abelian normal subgroup: the little-group method

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

An abelian normal subgroup supplies a set of simultaneous eigencharacters. The rest of the group permutes those characters. An irreducible representation uses one orbit, and the action on one eigenspace determines the action everywhere.

When the normal subgroup has a complement, its character extends to the stabilizer by an explicit formula. The remaining data are ordinary representations of a smaller group. We will prove this classification, use it for several familiar groups, and construct the finite Schrödinger representation with all signs fixed by the group law.

Basic references are Teleman's *Representation Theory* and Gruson–Serganova's *A Journey Through Representation Theory*.

## Prerequisites and conventions

All groups are finite and all representations are finite-dimensional over \(\mathbb C\). We use complete reducibility, Schur's lemma, character orthogonality and the degree-square identity from *Representations and complete reducibility* and *Characters and the orthogonality relations*. From *Induced representations and Frobenius reciprocity* we use induction, its dimension and conjugation properties. From *Mackey theory and Clifford's theorem* we use Mackey's criterion and the Clifford correspondence.

Write \(\widehat A=\operatorname{Hom}(A,\mathbb C^\times)\) for the character group of an abelian group \(A\). Its elements are exactly the irreducible representations of \(A\), and \(|\widehat A|=|A|\). If \(G=A\rtimes H\), each element has a unique expression \(ah\), and

\[
(ah)(a'h')=a(ha'h^{-1})hh'.
\tag{1}
\]

The action on characters is

\[
(h\lambda)(a)=\lambda(h^{-1}ah).
\tag{2}
\]

Thus \(h\) sends a vector of weight \(\lambda\) to a vector of weight \(h\lambda\). For a representation \(V\), put

\[
V_\lambda=\{v\in V:av=\lambda(a)v\text{ for all }a\in A\}.
\tag{3}
\]

Complete reducibility gives \(V=\bigoplus_{\lambda\in\widehat A}V_\lambda\).

## 1. Extending one weight to its stabilizer

Fix \(\lambda\in\widehat A\), and define

\[
H_\lambda=\{h\in H:h\lambda=\lambda\},
\qquad I_\lambda=A\rtimes H_\lambda.
\tag{4}
\]

The inertia group of \(\lambda\) in \(G\) is \(I_\lambda\): conjugation by \(A\) fixes every character of \(A\).

**Lemma 1.1.** The formula

\[
\widetilde\lambda(ah)=\lambda(a)
\quad(a\in A,\ h\in H_\lambda)
\tag{5}
\]

defines a character of \(I_\lambda\) extending \(\lambda\).

**Proof.** Invariance under \(h\) implies \(\lambda(ha'h^{-1})=\lambda(a')\). Apply this to (1):

\[
\widetilde\lambda((ah)(a'h'))
=\lambda(a)\lambda(ha'h^{-1})
=\widetilde\lambda(ah)\widetilde\lambda(a'h').
\]

The restriction to \(A\) is the required character. Unique factorization makes the definition unambiguous. \(\square\)

For a representation \(\sigma\) of \(H_\lambda\), inflate \(\sigma\) along \(I_\lambda\to H_\lambda\) and form

\[
U_{\lambda,\sigma}(ah)=\lambda(a)\sigma(h),
\qquad
\Theta_{\lambda,\sigma}=\operatorname{Ind}_{I_\lambda}^{G}U_{\lambda,\sigma}.
\tag{6}
\]

Multiplication in (6) is valid for exactly the reason in Lemma 1.1.

**Lemma 1.2.** The irreducible representations of \(I_\lambda\) whose restriction to \(A\) is a sum of copies of \(\lambda\) are exactly \(U_{\lambda,\sigma}\), with \(\sigma\) irreducible over \(H_\lambda\). This parametrization is a bijection on isomorphism classes.

**Proof.** In such a representation \(U\), every \(a\in A\) acts as \(\lambda(a)\operatorname{Id}\). Tensor \(U\) with \(\widetilde\lambda^{-1}\). The resulting action kills \(A\), so factors through \(I_\lambda/A=H_\lambda\); call it \(\sigma\). Conversely, (6) reverses this operation. Tensoring by a character preserves invariant subspaces and intertwiners, as does passing between a quotient representation and its inflation. Thus irreducibility and isomorphism are preserved in both directions. \(\square\)

The complement is doing real work here. An invariant character of an abelian normal subgroup of an arbitrary extension need not extend to its inertia group. The quaternion examples below explain both the obstruction and what remains usable.

## 2. The classification theorem

Conjugation transports \(\sigma\) to a representation \({}^{h}\sigma\) of \(hH_\lambda h^{-1}=H_{h\lambda}\), by

\[
({}^{h}\sigma)(k)=\sigma(h^{-1}kh).
\tag{7}
\]

**Theorem 2.1 (little-group method).** For \(G=A\rtimes H\) with \(A\) abelian:

1. Every \(\Theta_{\lambda,\sigma}\) with \(\sigma\in\operatorname{Irr}(H_\lambda)\) is irreducible, and
   \[
   \dim\Theta_{\lambda,\sigma}=[H:H_\lambda]\dim\sigma.
   \tag{8}
   \]
2. Two such representations are isomorphic precisely when there is \(h\in H\) such that \(\lambda'=h\lambda\) and \(\sigma'\simeq{}^{h}\sigma\).
3. Every irreducible representation of \(G\) arises in this way.

**Proof of irreducibility and the dimension.** Lemma 1.2 makes \(U_{\lambda,\sigma}\) irreducible over the inertia group. The Clifford correspondence, Theorem 4.1 of *Mackey theory and Clifford's theorem*, makes its induction irreducible. The induction dimension formula gives (8).

Here is also a direct check using Mackey's criterion. If \(s\notin I_\lambda\), the restrictions of \(U_{\lambda,\sigma}\) and its conjugate by \(s\) to \(A\) have distinct weights \(\lambda\) and \(s\lambda\). Their intertwiners on \(I_\lambda\cap sI_\lambda s^{-1}\) vanish because this intersection contains \(A\). The identity double coset contributes the scalar endomorphisms of \(U_{\lambda,\sigma}\). Mackey's criterion therefore gives irreducibility.

**Proof of the isomorphism assertion.** The restriction of \(\Theta_{\lambda,\sigma}\) to \(A\) is

\[
\bigoplus_{h\in H/H_\lambda}(h\lambda)^{\oplus\dim\sigma}.
\tag{9}
\]

Indeed, a coset summand \(h\otimes U_{\lambda,\sigma}\) has weight \(h\lambda\); distinct cosets give distinct weights. Its \(\lambda\)-eigenspace is the original \(U_{\lambda,\sigma}\).

An isomorphism must preserve the set of weights, so \(\lambda'=h\lambda\) for some \(h\). Conjugation carries the inducing representation to \(U_{\lambda',{}^{h}\sigma}\), by (5) and (7), and conjugate inducing data give isomorphic inductions. We may therefore reduce to \(\lambda'=\lambda\). An isomorphism now restricts to an \(I_\lambda\)-isomorphism on the intrinsic \(\lambda\)-eigenspaces. Lemma 1.2 forces \(\sigma'\simeq\sigma\). Conversely, the stated conjugacy of the data induces an isomorphism.

**Proof of exhaustion.** Let \(V\) be irreducible, and choose a weight \(\lambda\) occurring in its restriction to \(A\). Clifford theory says that \(V_\lambda\) is irreducible over \(I_\lambda\) and that

\[
V\simeq\operatorname{Ind}_{I_\lambda}^{G}V_\lambda.
\]

On this eigenspace \(A\) acts by \(\lambda\), so Lemma 1.2 identifies \(V_\lambda\) with \(U_{\lambda,\sigma}\) for an irreducible \(\sigma\) of \(H_\lambda\). This proves exhaustion. \(\square\)

In practice, choose one character from each \(H\)-orbit. For each chosen character, list the irreducibles of its stabilizer. This removes duplication from the classification.

The dimensions provide a useful completeness check. The degree-square identity for each stabilizer gives

\[
\begin{aligned}
\sum_{\lambda\text{ orbit representatives}}\ \sum_\sigma
 \bigl([H:H_\lambda]\dim\sigma\bigr)^2
&=\sum_{\lambda\text{ orbit representatives}}
 [H:H_\lambda]^2|H_\lambda|\\
&=|H|\sum_{\lambda\text{ orbit representatives}}[H:H_\lambda]\\
&=|H||A|=|G|.
\end{aligned}
\tag{10}
\]

## 3. Dihedral groups and permutation groups

### Dihedral groups

Let \(D_n=\langle r,s:r^n=s^2=1,\ srs^{-1}=r^{-1}\rangle\), of order \(2n\), with \(n\geq1\). Here \(A=\langle r\rangle\) and \(H=\langle s\rangle\). Put \(\zeta=e^{2\pi i/n}\) and \(\lambda_k(r)=\zeta^k\), with \(k\) taken modulo \(n\). The nonidentity element of \(H\) sends \(k\) to \(-k\).

A fixed character has \(2k=0\) modulo \(n\). For \(k=0\), and also \(k=n/2\) when \(n\) is even, the stabilizer is all of \(H\). Each gives two linear representations, with \(s\) acting by \(+1\) or \(-1\). Each remaining pair \(\{k,-k\}\) gives one irreducible of degree two:

\[
r\longmapsto
\begin{pmatrix}\zeta^k&0\\0&\zeta^{-k}\end{pmatrix},
\qquad
s\longmapsto
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{11}
\]

These are the coset matrices of the induction from \(A\). The relations are immediate, and the theorem proves irreducibility and exhausts the list. Their characters are

\[
\chi_k(r^j)=\zeta^{kj}+\zeta^{-kj},
\qquad \chi_k(sr^j)=0.
\tag{12}
\]

For odd \(n\), there are two linear representations and \((n-1)/2\) of degree two. For even \(n\), there are four linear representations and \(n/2-1\) of degree two. The formulas include \(D_1\simeq C_2\) and \(D_2\simeq C_2\times C_2\), where there are no degree-two representations.

### The alternating group on four letters

Let

\[
A=\{1,(12)(34),(13)(24),(14)(23)\}\simeq C_2\times C_2.
\]

It is normal in \(A_4\), and \(H=\langle(123)\rangle\) is a complement. The trivial character of \(A\) is fixed and gives the three linear representations inflated from \(C_3\). Conjugation by \((123)\) cycles the three nontrivial elements of \(A\), and therefore cycles the three nontrivial characters. That orbit has trivial stabilizer and gives one irreducible of degree three. The degree squares are \(3+9=12\).

This degree-three representation is the subspace

\[
V=\{(v_1,v_2,v_3,v_4)\in\mathbb C^4:\textstyle\sum_i v_i=0\}
\]

in the permutation representation. To see the identification, its character on a nonidentity element of \(A\) is \(-1\), since that permutation has no fixed coordinate. The sum of the three nontrivial characters of \(A\) has the same values: it is \(3\) at \(1\) and \(-1\) elsewhere by orthogonality. Thus \(V|_A\) contains each nontrivial weight once. A nonzero invariant subspace contains some weight and, by the transitive \(H\)-action, contains all three. This proves irreducibility and identifies it with the unique degree-three entry.

### The symmetric group on four letters

The same \(A\) is normal in \(S_4\). The permutations fixing \(4\) form a complement \(H\simeq S_3\). Its action permutes the three nontrivial characters transitively. The trivial orbit gives the two linear representations and one degree-two representation inflated from \(S_3\), whose classification was proved in *Characters and the orthogonality relations*.

Choose the character \(\lambda\) with kernel \(\{1,(12)(34)\}\). Its stabilizer inside \(H\) is \(\{1,(12)\}\simeq C_2\), so its two characters give two irreducibles of degree three. This accounts for

\[
1^2+1^2+2^2+3^2+3^2=24.
\]

They are the standard permutation subspace \(V\) above and \(V\otimes\operatorname{sgn}\). Indeed, the vector \((1,1,-1,-1)\) spans \(V_\lambda\): \((12)(34)\) fixes it and the other two nonidentity elements of \(A\) negate it. The stabilizer generator \((12)\) fixes that vector, so \(V\) uses the positive stabilizer character. The sign character is trivial on \(A\) and negative on \((12)\), so the twist uses the negative stabilizer character. Theorem 2.1 both proves their irreducibility and distinguishes them.

## 4. The affine group of a finite field

For a finite field \(\mathbb F_q\), let

\[
G=\{(b,a):b\in\mathbb F_q,\ a\in\mathbb F_q^\times\},
\qquad
(b,a)(b',a')=(b+ab',aa').
\tag{13}
\]

It acts on the field by \(u\mapsto au+b\). Translations form the abelian normal subgroup \(A=(\mathbb F_q,+)\), and \(H=\mathbb F_q^\times\) is a complement.

Choose a nontrivial additive character \(\psi\). Such a character exists: choose a nonzero \(\mathbb F_p\)-linear functional on the vector space \(\mathbb F_q\) and compose it with \(j\mapsto e^{2\pi ij/p}\). For \(t\in\mathbb F_q\), put \(\psi_t(b)=\psi(tb)\). These are distinct. If \(t\ne u\), multiplication by \(t-u\) is a bijection of the field, so some \(b\) satisfies \(\psi((t-u)b)\ne1\). There are \(q\) characters, so these are all the characters of \(A\).

The action is \(a\psi_t=\psi_{t/a}\). There are two orbits: \(\psi_0\), with stabilizer \(H\), and all \(q-1\) nontrivial characters, with trivial stabilizer.

**Proposition 4.1.** The irreducibles of the affine group are the \(q-1\) characters inflated from \(\mathbb F_q^\times\), and one additional irreducible \(W\) of degree \(q-1\). For \(q>2\), these are exactly \(q-1\) linear representations and one of higher degree. For \(q=2\), both representations are linear.

**Proof.** The two orbits and their stabilizers give the list by Theorem 2.1. The group \(H\) is abelian and has \(q-1\) irreducible characters. The other stabilizer is trivial and yields degree \(q-1\). At \(q=2\), \(G\simeq C_2\), and the additional representation has degree one. \(\square\)

An explicit model for \(W\) is the space of functions on \(\mathbb F_q^\times\), with

\[
(\rho(b,a)f)(t)=\psi(tb)f(ta).
\tag{14}
\]

Composing two operators gives the phase \(\psi(t(b+ab'))\) and argument \(taa'\), exactly as required by (13). The translation weights are the \(q-1\) distinct nontrivial characters, and \(H\) permutes their lines transitively; this also proves irreducibility directly.

When \(a\ne1\), multiplication by \(a\) fixes no nonzero field element, so the operator in (14) has zero trace. When \(a=1\), its trace is \(\sum_{t\ne0}\psi(tb)\). Additive-character orthogonality gives

\[
\chi_W(b,a)=
\begin{cases}
q-1,&a=1,\ b=0,\\
-1,&a=1,\ b\ne0,\\
0,&a\ne1.
\end{cases}
\tag{15}
\]

For \(\mathbb F_5\), take \(\psi(b)=e^{2\pi ib/5}\). The four inflated characters and \(W\) have degrees \(1,1,1,1,4\), whose squares sum to \(20\). On functions indexed by \(1,2,3,4\), translations are diagonal with entries \(\psi(b),\psi(2b),\psi(3b),\psi(4b)\); multiplication by \(2\) permutes the arguments through \(1,2,4,3\). The character of \(W\) is \(4\) at the identity, \(-1\) at a nonzero translation and \(0\) at every element with multiplier different from \(1\).

## 5. Quaternion groups: using the inertia group without a complement

Consider the group \(Q_{4m}\), \(m\geq2\), with relations

\[
a^{2m}=1,\qquad b^2=a^m,\qquad bab^{-1}=a^{-1}.
\tag{16}
\]

It has elements \(a^j\) and \(ba^j\), \(0\leq j<2m\). These normal forms are distinct: the matrices

\[
a=\operatorname{diag}(\xi,\xi^{-1}),\qquad
b=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\quad \xi=e^{\pi i/m},
\]

satisfy (16) and give \(4m\) distinct such matrices. The relations reduce every word to one of the normal forms, so the order is exactly \(4m\). When \(m\) is a power of two, these are the usual generalized quaternion groups; the same presentation for general \(m\) defines a dicyclic group.

The cyclic subgroup \(A=\langle a\rangle\) is normal of index two. Every element outside it squares to \(a^m\), which is not the identity, so there is no subgroup of order two complementary to \(A\). We must use Clifford theory directly.

For \(\lambda_k(a)=\xi^k\), the conjugation orbit is \(\{k,-k\}\) modulo \(2m\). If \(k\notin\{0,m\}\), the inertia group is just \(A\), so \(\operatorname{Ind}_A^{Q_{4m}}\lambda_k\) is irreducible of degree two. Choose \(1\leq k\leq m-1\) to avoid duplication. Coset representatives \(1,b\) give

\[
a\longmapsto
\begin{pmatrix}\xi^k&0\\0&\xi^{-k}\end{pmatrix},
\qquad
b\longmapsto
\begin{pmatrix}0&(-1)^k\\1&0\end{pmatrix}.
\tag{17}
\]

The factor \((-1)^k\) records \(b^2=a^m\); replacing this matrix by the dihedral flip would fail for odd \(k\).

For each of the fixed characters \(k=0,m\), the inertia group is all of \(Q_{4m}\). Here an extension does exist, but its value on \(b\) must be chosen to satisfy the relation. Assign \(a\mapsto\alpha\), where \(\alpha=1\) or \(-1\), and \(b\mapsto\beta\), where

\[
\beta^2=\alpha^m.
\tag{18}
\]

There are two choices of \(\beta\) for each \(\alpha\), giving four linear representations. They respect all the relations because \(\alpha=\alpha^{-1}\). Every irreducible over that fixed character is one of these: tensor with one extension to make \(A\) act trivially, then use the two characters of \(Q_{4m}/A\simeq C_2\).

We have obtained all irreducibles, with degree squares \(4+4(m-1)=4m\). In \(Q_8\), this gives four linear representations and one degree-two representation. Its central character sends \(a^2\) to \(-1\). That character of the center cannot extend to a linear character of \(Q_8\), because the center's nonidentity element is a commutator. Thus extension from \(A\) in this example does not justify extension from every abelian normal subgroup.

## 6. The finite Heisenberg group

Let \(p\) be an odd prime. On \(\mathbb F_p^3\), define

\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy').
\tag{19}
\]

Associativity follows because either bracketing of three factors has third coordinate \(z+z'+z''+xy'+xy''+x'y''\). The identity is \((0,0,0)\), and

\[
(x,y,z)^{-1}=(-x,-y,-z+xy).
\tag{20}
\]

The commutator of two elements is \((0,0,xy'-x'y)\). Consequently the center is

\[
Z=\{(0,0,z):z\in\mathbb F_p\}.
\tag{21}
\]

Indeed, commuting with all \((x',y',0)\) forces \(x=y=0\). The same commutator formula shows that \([G,G]=Z\): take \(x=1,y=0,x'=0\) and vary \(y'\). Thus the linear characters are exactly

\[
\ell_{s,r}(x,y,z)=\zeta^{sx+ry},
\qquad s,r\in\mathbb F_p,\quad \zeta=e^{2\pi i/p}.
\tag{22}
\]

They are distinct and give the \(p^2\) characters of \(G/Z\simeq\mathbb F_p^2\).

### Classification by the little-group method

For this application use the larger abelian normal subgroup

\[
B=\{(0,y,z)\},\qquad X=\{(x,0,0)\}.
\]

It is a split extension \(G=B\rtimes X\); in fact
\((x,y,z)=(0,y,z)(x,0,0)\). The characters of \(B\) are

\[
\lambda_{r,c}(0,y,z)=\zeta^{ry+cz}.
\]

Conjugation as in (2) sends \(\lambda_{r,c}\) to \(\lambda_{r-cx,c}\), since conjugating \((0,y,z)\) by \((-x,0,0)\) on the left and \((x,0,0)\) on the right gives \((0,y,z-xy)\).

If \(c=0\), each character is fixed, and the \(p\) characters of \(X\) supply (22). If \(c\ne0\), its orbit contains every \(r\) and its stabilizer in \(X\) is trivial. There is exactly one irreducible of degree \(p\) for each \(c\ne0\). The central character is \(\psi_c(z)=\zeta^{cz}\).

### The Schrödinger model

Fix a nontrivial character \(\psi=\psi_c\) of the additive group \(\mathbb F_p\). On the space of functions \(f:\mathbb F_p\to\mathbb C\), define

\[
(\rho_\psi(x,y,z)f)(t)=\psi(z+yt)f(t+x).
\tag{23}
\]

This formula is tied to the nonsymmetric cocycle \(xy'\) in (19). Direct composition gives

\[
\begin{aligned}
(\rho_\psi(x,y,z)\rho_\psi(x',y',z')f)(t)
&=\psi\bigl(z+yt+z'+y'(t+x)\bigr)f(t+x+x')\\
&=\psi\bigl(z+z'+xy'+(y+y')t\bigr)f(t+x+x'),
\end{aligned}
\tag{24}
\]

which is the operator for the product in (19).

Let \(e_u\) be the function supported at \(u\) with value \(1\). Then

\[
\rho_\psi(x,y,z)e_u=\psi\bigl(z+y(u-x)\bigr)e_{u-x}.
\tag{25}
\]

Put \(T=\rho_\psi(1,0,0)\) and \(M=\rho_\psi(0,1,0)\). Thus \(Te_u=e_{u-1}\), \(Me_u=\psi(u)e_u\), and

\[
TM=\psi(1)MT.
\tag{26}
\]

The \(p\) eigenvalues \(\psi(u)\) are distinct. Any endomorphism commuting with \(M\) is diagonal in this basis, and commuting also with the cyclic shift \(T\) forces all diagonal entries to agree. The commutant is therefore \(\mathbb C\). Complete reducibility implies that this representation is irreducible: a proper invariant summand would give a nonscalar commuting projection.

**Theorem 6.1 (finite Stone–von Neumann theorem).** For every nontrivial character \(\psi\) of \(Z\simeq\mathbb F_p\), there is exactly one irreducible representation of the group (19), up to isomorphism, with central action \(z\mapsto\psi(z)\operatorname{Id}\). It has degree \(p\) and is realized by (23).

**Proof.** Formula (24) proves existence of the representation; the commutant argument proves irreducibility, and (23) gives the stated central action. The little-group classification above proves uniqueness, since for a fixed nonzero \(c\) all characters \(\lambda_{r,c}\) form one orbit with trivial stabilizer.

One can also see uniqueness directly in any irreducible \(V\) with this central action. Write \(T,M\) for the actions of \((1,0,0),(0,1,0)\). They satisfy (26) and \(T^p=M^p=1\). Diagonalize \(M\). The relation \(MT=\psi(1)^{-1}TM\) shows that powers of \(T\) move an eigenvector through all \(p\) distinct eigenvalues, since \(\psi(1)\) has order \(p\). In particular, an eigenvector \(v\ne0\) with eigenvalue \(1\) exists. The vectors \(T^jv\), \(0\leq j<p\), are linearly independent and their span is stable under \(T,M\) and the center. These elements generate \(G\), so irreducibility makes that span all of \(V\). The map

\[
e_{-j}\longmapsto T^jv
\]

intertwines \(T\), \(M\) and the center, hence all of \(G\). It identifies \(V\) with (23) and proves both the dimension and uniqueness again. \(\square\)

For the character, (25) has no fixed basis vector when \(x\ne0\). When \(x=0\), its trace is \(\psi(z)\sum_t\psi(yt)\). Therefore

\[
\chi_\psi(x,y,z)=
\begin{cases}
p\psi(z),&x=y=0,\\
0,&(x,y)\ne(0,0).
\end{cases}
\tag{27}
\]

The whole classification contains \(p^2\) linear representations and \(p-1\) of degree \(p\), with degree squares \(p^2+(p-1)p^2=p^3\). Two nontrivial central characters give nonisomorphic representations already by their central actions.

For \(p=3\), let \(\omega=e^{2\pi i/3}\) and \(\psi(z)=\omega^z\). In the ordered basis \(e_0,e_1,e_2\),

\[
T=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},
\qquad M=\operatorname{diag}(1,\omega,\omega^2),
\qquad \rho_\psi(0,0,1)=\omega I.
\tag{28}
\]

We have \(TM=\omega MT\) and \(\rho_\psi(x,y,z)=\omega^zM^yT^x\). The other degree-three irreducible replaces \(\omega\) by \(\omega^2\). Alongside the nine characters in (22), these exhaust the group of order \(27\).

## 7. Exercises with complete solutions

**Exercise 1.** Classify the irreducible representations of \(D_5\) by the little-group method and write their characters.

**Solution.** The action on the five characters of \(\langle r\rangle\) has orbits \(\{0\},\{1,4\},\{2,3\}\). The fixed orbit has stabilizer \(C_2\), giving the trivial character and the character with \(r\mapsto1,s\mapsto-1\). The other stabilizers are trivial, giving the two matrices (11) for \(k=1,2\). Their characters are \(2\cos(2\pi kj/5)\) on \(r^j\) and zero on \(sr^j\). The linear characters take value \(1\) on rotations and respectively \(1,-1\) on reflections. Theorem 2.1 proves irreducibility and exhaustion; the check \(1+1+4+4=10\) agrees with the order.

**Exercise 2.** Derive the affine-group classification and compute the character of the additional degree-\((q-1)\) representation, including the smallest field.

**Solution.** Choose a nontrivial additive \(\psi\). The characters \(\psi_t\) constructed in Section 4 are distinct and exhaust \(\widehat A\). The multiplier \(a\) sends \(t\) to \(t/a\), so the zero orbit gives the \(q-1\) inflated characters of \(H\), and the nonzero orbit gives one irreducible of degree \(q-1\). In (14), the underlying permutation of the basis has no fixed point for \(a\ne1\), hence trace zero. For \(a=1\) the trace is \(\sum_{t\ne0}\psi(tb)\). It is \(q-1\) when \(b=0\). When \(b\ne0\), a change of variable and orthogonality give \(\sum_{t\in\mathbb F_q}\psi(tb)=0\); removing the zero term gives \(-1\). This proves (15). The degrees check as
\((q-1)+(q-1)^2=q(q-1)\). At \(q=2\), \(H\) is trivial and the additional representation is \(b\mapsto(-1)^b\); together with the trivial character it gives the two linear characters of \(C_2\).

**Exercise 3.** Construct the Schrödinger representation for (19), check its group law and prove irreducibility.

**Solution.** Define the operators by (23). Calculation (24) verifies their multiplication, including the term \(xy'\). Their inverse operators exist because they permute the basis (25) and multiply its vectors by nonzero scalars. On this basis, \(M\) has the \(p\) distinct eigenvalues \(\psi(u)\), while \(T\) permutes the corresponding lines cyclically.

If \(W\ne0\) is invariant, it contains an \(M\)-eigenvector: the spectral projection onto an eigenvalue is a polynomial in \(M\), by interpolation at the distinct eigenvalues, and some such projection of a nonzero vector of \(W\) is nonzero. That eigenvector spans one of the lines \(\mathbb Ce_u\). Applying powers of \(T\) puts every basis line in \(W\), so \(W\) is the whole space. This proves irreducibility directly from invariant subspaces.

The model is also the induction of \(\lambda_{0,c}\) from \(B\). Explicitly send \((j,0,0)\otimes1\) in its coset basis to \(e_{-j}\). For \(g=(x,y,z)\),

\[
g(j,0,0)=(x+j,0,0)(0,y,z-(x+j)y).
\]

The induced action therefore gives the factor \(\psi(z-(x+j)y)\) and basis vector \(e_{-(x+j)}\), exactly as (25). This verifies the induction identification with its signs.

**Exercise 4.** Prove the little-group theorem in full using Mackey's criterion, weight spaces and the degree-square identity.

**Solution.** Formula (5) is multiplicative by (1) and character invariance. For every irreducible \(\sigma\) of \(H_\lambda\), \(U_{\lambda,\sigma}\) is irreducible: its invariant subspaces are exactly those of \(\sigma\), since \(A\) acts by scalars. For a double coset represented by \(s\notin I_\lambda\), the two inducing representations restrict to distinct \(A\)-weights. An intertwiner must commute with \(A\), so is zero. The identity double coset has a one-dimensional intertwiner space by Schur's lemma. Mackey's criterion proves \(\Theta_{\lambda,\sigma}\) irreducible, of degree (8).

Its \(A\)-weights are (9). Distinct orbits therefore give nonisomorphic representations. Within a fixed orbit choose the same \(\lambda\). The \(\lambda\)-eigenspace is exactly the identity coset summand, with action \(U_{\lambda,\sigma}\). An isomorphism of induced representations restricts to an isomorphism on this eigenspace and forces \(\sigma\simeq\sigma'\). Conjugating the data by \(h\) transports the extension (5) and \(\sigma\) as in (7), and induction of conjugate data is isomorphic. This proves precisely the stated equivalence on all pairs.

Finally, choose orbit representatives so the representations just proved irreducible are pairwise distinct. Their degree squares sum to \(|G|\) by (10). The degree-square identity for all irreducibles of \(G\) leaves no room for any additional irreducible, since its squared dimension would be positive. This proves exhaustion and completes every part of Theorem 2.1.

## What this lesson does not prove

The earlier course results listed under prerequisites, and the real Hilbert-space analogue discussed in Gruson–Serganova, Chapter 4 §2, Definition 2.2 and Theorem 2.4. That analytic theorem is outside the scope of this lesson; our finite theorem requires only finite-dimensional linear algebra. There are no unproved new finite-group results used in the classification or the exercise solutions.

The broader analytic analogue is also discussed in *Recovering multiplicity from a Weyl system* in the operator-algebra course; that pointer supplies no prerequisite for the finite proof.

## References

- Constantin Teleman, [*Representation Theory*](https://math.berkeley.edu/~teleman/math/RepThry.pdf), lecture notes, §§17.6–17.7: abelian normal subgroups and stabilizers.
- Caroline Gruson and Vera Serganova, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, Universitext, Springer, 2018, Chapter 2 §10: the affine group; Chapter 4 §2: the real Heisenberg group and its unitary representations.
