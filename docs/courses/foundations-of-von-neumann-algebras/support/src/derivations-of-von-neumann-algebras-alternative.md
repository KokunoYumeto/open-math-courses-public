# Derivations of von Neumann algebras: an alternative proof

*Original proof received through ChatGPT Pro; the exact generating model and reasoning effort are unknown. GPT-6 Astra (OpenAI), Ultra, checked the retained argument and supplied the elementary closedness and compactness bridges and dependency integration. Original mathematical exposition: CC0 1.0.*

This proof treats arbitrary von Neumann algebras, with no countability or factor assumption. It proceeds through finite traces, affine fixed points and central reductions. It is retained as a distinct route, alongside the spectral reconstruction in the operator-algebra programme.

## Statement

**Theorem (automatic continuity and Kadison–Sakai innerness).** A derivation of a \(C^*\)-algebra \(A\) is a complex-linear map \(\delta:A\to A\) satisfying
\[
\delta(xy)=\delta(x)y+x\delta(y)\qquad(x,y\in A).
\]
No continuity is included in this definition.

Every derivation of every \(C^*\)-algebra is bounded. If \(M\) is a von Neumann algebra and \(\delta:M\to M\) is a derivation, then there exists \(a\in M\) such that
\[
\delta(x)=ax-xa\qquad(x\in M),
\qquad \|a\|\le 2\|\delta\|.
\]
Two implementers in \(M\) differ by an element of \(Z(M)\), and adding an element of \(Z(M)\) to an implementer does not change the derivation. Consequently every implementer \(b\in M\) satisfies
\[
\operatorname{dist}(b,Z(M))\le 2\|\delta\|.
\]
If, in addition,
\[
\delta(x^*)=\delta(x)^*\qquad(x\in M),
\]
then one can choose
\[
a=ih,\qquad h=h^*\in M,\qquad \|h\|\le\|\delta\|.
\]
In this case every implementer in \(M\) has distance at most \(\|\delta\|\) from \(Z(M)\).

There is no separability, countable decomposability, factor, type, or trace hypothesis. These are bounds furnished by the proof; no optimality assertion is made.

## Proof

Write \(A_h=\{x\in A:x=x^*\}\), \(\mathcal U(A)\) for the unitary group of a unital algebra, and \([a,x]=ax-xa\). A derivation preserving the involution is called a *-derivation. For a concrete von Neumann algebra, weak-* means its \(\sigma\)-weak topology. Central sums are indexed by arbitrary sets and are limits of finite partial sums. The lesson abbreviations used in citations are expanded, with result numbers, under **Results used**.

The zero algebra is immediate, with implementer zero. All algebras represented on Hilbert spaces below act nondegenerately.

### 1. Automatic continuity

**1.1. Algebraic reduction to *-derivations.** For an arbitrary derivation define
\[
\delta^\#(x)=\delta(x^*)^*,\qquad
\delta_1=\frac{\delta+\delta^\#}{2},\qquad
\delta_2=\frac{\delta-\delta^\#}{2i}.
\]
The map \(\delta^\#\) is complex-linear. Moreover,
\[
\delta^\#(xy)
=\bigl(\delta(y^*)x^*+y^*\delta(x^*)\bigr)^*
=x\delta^\#(y)+\delta^\#(x)y.
\]
Thus \(\delta_1,\delta_2\) are derivations, and
\[
\delta_1(x^*)=\frac{\delta(x^*)+\delta(x)^*}{2}=\delta_1(x)^*,
\qquad
\delta_2(x^*)=\frac{\delta(x^*)-\delta(x)^*}{2i}=\delta_2(x)^*.
\]
Moreover,
\[
\delta=\delta_1+i\delta_2.
\]
These assertions are algebraic and do not assume continuity. Once boundedness is established, they also give
\[
\|\delta^\#\|=\|\delta\|,
\qquad \|\delta_j\|\le\|\delta\|\quad(j=1,2).
\tag{1.1}
\]

It suffices to treat a unital algebra. Indeed, represent a nonunital \(A\) faithfully, using [GNS, Theorem 7.2](../../representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#faithful-representations-of-c--algebras). The algebra \(A+\mathbb C1\subseteq B(H)\) is closed: a finite-dimensional extension of a closed subspace of a Banach space is closed. The [closedness bridge below](#OA-FND-INNER-CLOSEDNESS) proves this implication explicitly. Since \(1\notin A\), the expression \(x+\lambda1\) is unique, and
\[
\widetilde\delta(x+\lambda1)=\delta(x)
\]
defines a derivation: both sides of its product rule at \(x+\lambda1,y+\mu1\) equal
\[
\delta(x)y+x\delta(y)+\lambda\delta(y)+\mu\delta(x).
\]
It preserves the involution when \(\delta\) does, since
\(\widetilde\delta((x+\lambda1)^*)=\delta(x^*)=\delta(x)^*\).
Boundedness of this extension implies boundedness on \(A\). In a unital algebra every derivation satisfies \(\delta(1)=0\), by applying the product rule to \(1\cdot1\).

**1.2. A state calculation.** Let \(D\) be any derivation of a unital \(C^*\)-algebra, let \(b=b^*\), and let \(\varphi\) be a state whose restriction to \(C^*(1,b)\) is a character. Then
\[
\varphi(D(b))=0.
\tag{1.2}
\]
To prove this, put \(c=b-\varphi(b)1\). Continuous functional calculus [CF, Theorem 5.1](../../c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-07) gives positive elements
\[
s_+=(c_+)^{1/2},\qquad s_-=(c_-)^{1/2},
\qquad c=s_+^2-s_-^2
\]
in \(C^*(1,b)\). The character takes \(c\) to zero and therefore takes \(s_+^2,s_-^2\) to zero. Hence \(\varphi(s_\pm^2)=0\). The Cauchy–Schwarz inequality for a positive functional [GNS, Proposition 3.2](../../representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#OA-FND-GN-03), in the form
\[
|\varphi(rs)|^2\le\varphi(rr^*)\varphi(s^*s),
\]
shows that
\[
\varphi(D(s_\pm)s_\pm)=\varphi(s_\pm D(s_\pm))=0.
\]
Applying \(D\) to \(c=s_+^2-s_-^2\), and using \(D(1)=0\), proves (1.2).

**1.3. Closed graph.** Let \(D\) be a *-derivation. Suppose that
\[
x_n\in A_h,\qquad x_n\longrightarrow0,\qquad D(x_n)\longrightarrow b\in A_h
\]
in norm. We prove \(b=0\). If \(b\ne0\), its spectrum contains a nonzero real number \(\lambda\). Replacing \(x_n,b\) by \(x_n/\lambda,b/\lambda\), we can assume \(1\in\sigma(b)\).

Choose a continuous real function \(f\) on \(\sigma(b)\) such that
\[
0\le f\le1,\qquad f(1)=1,\qquad f(t)=0\text{ for }t\le\tfrac12.
\]
For \(v=f(b)\), functional calculus gives
\[
0\le v\le1,\qquad \|v\|=1,\qquad vbv\ge\tfrac12v^2.
\]
After discarding finitely many terms, \(r_n=\|x_n\|>0\). Set
\[
y_n=x_n+3r_n1,\qquad b_n=vy_nv,\qquad t_n=\frac{b_n}{4r_n}.
\]
Then
\[
2r_n1\le y_n\le4r_n1,
\qquad \tfrac12v^2\le t_n\le v^2,
\qquad \|t_n\|\ge\tfrac12.
\tag{1.3}
\]
The product rule, without any continuity assumption on \(D\), gives
\[
D(b_n)=D(v)y_nv+vD(x_n)v+vy_nD(v)\longrightarrow vbv.
\tag{1.4}
\]
Here \(D(v)\) is one fixed element, and \(\|y_n\|\to0\).

Evaluation at the spectral point \(\|b_n\|\) is a character of \(C^*(1,b_n)\). Extend it to a state \(\varphi_n\) of \(A\), using [GNS, Proposition 7.1a](../../representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#faithful-representations-of-c--algebras). Equation (1.2) gives \(\varphi_n(D(b_n))=0\), while
\[
\varphi_n(t_n)=\|t_n\|\ge\tfrac12.
\]
Consequently, for every sufficiently large \(n\),
\[
\frac14
\le\frac12\varphi_n(t_n)
\le\varphi_n(vbv)
=\varphi_n(vbv-D(b_n))
\le\|vbv-D(b_n)\|
<\frac18,
\]
a contradiction.

The graph of the real-linear map \(D:A_h\to A_h\) is therefore closed: a convergent graph sequence is reduced to the preceding case by subtracting its limiting first coordinate. The real Closed Graph Theorem makes this restriction bounded. Every \(x\in A\) is \(x=h+ik\), where \(h,k\in A_h\) and \(\|h\|,\|k\|\le\|x\|\); hence \(D\) is bounded on \(A\). Applying this to \(\delta_1,\delta_2\) proves automatic continuity for \(\delta\).

The spectral-cut argument above is the automatic-continuity argument of [S60, unnumbered theorem, pp. 31–32], with the algebraic *-splitting and the nonunital reduction included explicitly.

### 2. The centre and uniformly bounded central sums

For a central projection \(z\) and any derivation \(D\),
\[
D(z)=D(z)z+zD(z)=2zD(z).
\]
Multiplication by \(z\) first gives \(zD(z)=0\), and then \(D(z)=0\). For a bounded derivation on a von Neumann algebra, spectral approximation of central self-adjoint elements by finite linear combinations of central projections gives
\[
D(c)=0\quad(c\in Z(M)),\qquad D(zx)=zD(x).
\tag{2.1}
\]
The approximation follows from [ST, Theorem 3.1 and Proposition 5.1](../../the-spectral-theorem-for-bounded-self-adjoint-operators.html#OA-FND-ST-03). In particular, \(D\) restricts to each central summand \(Mz\), with norm at most \(\|D\|\).

We record the precise summation statement. Suppose that \((z_i)_{i\in I}\) are pairwise orthogonal central projections with strong sum \(1\), and that
\[
a_i\in Mz_i,\qquad \|a_i\|\le C,\qquad
D(x)=[a_i,x]\quad(x\in Mz_i).
\]
For finite \(F\subset I\), put \(a_F=\sum_{i\in F}a_i\). Since the ranges of the summands are in orthogonal subspaces,
\[
\|a_F\xi\|^2
=\sum_{i\in F}\|a_i z_i\xi\|^2
\le C^2\sum_{i\in F}\|z_i\xi\|^2
\le C^2\|\xi\|^2.
\]
The same estimate for differences of partial sums proves strong convergence to an operator \(a\). Strong closedness gives \(a\in M\), and \(\|a\|\le C\), \(az_i=a_i\). If all \(a_i\) are self-adjoint, or all are skew-adjoint, the same property holds for \(a\), since the adjoint relation passes to matrix coefficients.

For every \(x\in M\), (2.1) gives
\[
\bigl(D(x)-[a,x]\bigr)z_i
=D(xz_i)-[a_i,xz_i]=0.
\]
Taking the strong sum of the \(z_i\) yields \(D(x)=[a,x]\). This argument never applies \(D\) to a strong limit.

A *-isomorphism transports derivations and their implementers, preserves their norms, and preserves self-adjointness. Isometry of *-isomorphisms is [CF, Corollary 4.6](../../c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-12). Between von Neumann algebras such an isomorphism is also normal, by [UE, Corollary 11.4](../../the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-18).

### 3. Normal extension without a continuity assumption on the representation

Let \(A\subseteq B(H)\) be a nondegenerate \(C^*\)-algebra and \(D:A\to A\) a bounded derivation. We show that it has a unique normal extension
\[
\overline D:A''\longrightarrow A'',\qquad
\|\overline D\|=\|D\|.
\tag{3.1}
\]
If \(D\) is a *-derivation, so is \(\overline D\).

Identify \(A^{**}\) with its enveloping von Neumann algebra by [UE, Theorem 3.3](../../the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-03), and write \(j:A\to A^{**}\) for the canonical embedding. The second adjoint \(D^{**}\) is weak-* continuous and has norm \(\|D\|\) [WT, Proposition 5.3](../../weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-05). It is a derivation. Here is the required verification of the product rule.

For \(a\in A\) and \(Y\in A^{**}\), choose a net \(b_\beta\in A\) with \(j(b_\beta)\to Y\) weak-*, using [WT, Theorem 5.2](../../weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-05). Passing to the limit in the product rule for \(ab_\beta\), by separate weak-* continuity of multiplication, gives
\[
D^{**}(j(a)Y)=j(D(a))Y+j(a)D^{**}(Y).
\]
Now choose \(j(a_\alpha)\to X\) weak-* and pass to the limit in this identity, keeping \(Y\) fixed. It follows that
\[
D^{**}(XY)=D^{**}(X)Y+XD^{**}(Y).
\]
Only one variable is allowed to tend to its limit at each passage. The involution is weak-* continuous, so the same density argument preserves the *-condition.

By [UE, Lemma 2.1(2)–(4)](../../the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-02), the given representation extends to a normal surjection
\[
q:A^{**}\longrightarrow A''
\]
whose kernel is \(A^{**}(1-z)\) for a central projection \(z\). Its restriction
\[
\theta:A^{**}z\longrightarrow A''
\]
is an isometric *-isomorphism, normal in both directions. Step 2's algebraic calculation gives \(D^{**}(z)=0\). Thus \(D^{**}\) preserves \(A^{**}z\), and
\[
\overline D=\theta\circ\bigl(D^{**}|_{A^{**}z}\bigr)\circ\theta^{-1}
\]
is a normal derivation of norm at most \(\|D\|\). For \(a\in A\),
\[
\theta^{-1}(a)=j(a)z,
\qquad D^{**}(j(a)z)=j(D(a))z,
\]
so \(\overline D(a)=D(a)\). This also proves the reverse norm inequality. Uniqueness follows from weak-* density of \(A\) in \(A''\), [DC, Theorem 4.4](../../the-double-commutant-theorem.html#OA-FND-BI-06).

In particular, on taking \(A=M=M''\), every bounded derivation of a von Neumann algebra is normal. The topology facts used here are [OT, Proposition 8.6 and Theorem 9.4](../../compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#OA-FND-LT-09).

### 4. Type I algebras: finite averaging with a uniform bound

**4.1. Finite-dimensional averaging.** Every finite-dimensional unital \(C^*\)-algebra \(F\) has a finite subgroup of its unitary group whose complex linear span is \(F\).

After a faithful unital representation, \(F\) is a von Neumann algebra: a finite-dimensional subspace is closed for the Hausdorff \(\sigma\)-weak topology. By [UE, Lemma 6.3](../../the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-13), \(F\) is therefore a finite direct sum of full matrix algebras. On \(\mathbb C^n\), with indices modulo \(n\), let
\[
S e_j=e_{j+1},\qquad T e_j=\zeta^j e_j,
\qquad \zeta=e^{2\pi i/n}.
\]
The group generated by \(S,T,-1\) is finite, because every word has the form \(\pm\zeta^kS^rT^s\), with exponents taken modulo \(n\). Its span contains
\[
E_{jj}=\frac1n\sum_{s=0}^{n-1}\zeta^{-js}T^s,
\qquad E_{ij}=S^{i-j}E_{jj},
\]
and thus all matrices. For a direct sum, take the product of these groups. Its span is an algebra and contains the central projection of each block: this projection is \((1-g)/2\), where \(g\) is \(-1\) on that block and \(1\) elsewhere. Multiplying by these projections isolates the matrix spans of all blocks.

Let \(F\subseteq P\) be a finite-dimensional unital subalgebra of a von Neumann algebra, and let \(D\) be a bounded derivation of \(P\). Choose such a finite group \(G\subseteq\mathcal U(F)\), and set
\[
b(u)=D(u)u^*,\qquad a_G=\frac1{|G|}\sum_{u\in G}b(u).
\]
The product rule gives the cocycle identity
\[
b(vu)=b(v)+vb(u)v^*.
\]
Averaging over \(u\in G\) yields
\[
a_G=b(v)+va_Gv^*,\qquad D(v)=a_Gv-va_G\quad(v\in G).
\]
Since \(G\) spans \(F\),
\[
D|_F=[a_G,\cdot]|_F,
\qquad \|a_G\|\le\|D\|.
\tag{4.1}
\]
For a *-derivation,
\[
b(u)^*=uD(u^*)=-D(u)u^*=-b(u),
\]
so \(a_G\) is skew-adjoint.

**4.2. Homogeneous type I algebras.** Suppose first that \(P\) is homogeneous of type I. By [PT, Theorem 10.3, Proposition 8.4 and Proposition 9.1](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-14), it has the form
\[
P\cong B\,\bar\otimes\,B(\ell^2(I)),\qquad B\text{ abelian},
\]
with matrix units \(w_{ij}\). Every finite matrix compression has an expression
\[
e_Jxe_J=\sum_{i,j\in J}c_{ij}w_{ij},
\qquad e_J=\sum_{i\in J}w_{ii},\qquad c_{ij}\in Z(P),
\tag{4.2}
\]
where \(J\subset I\) is finite and nonempty.

The finite-dimensional unital algebras
\[
F_J=\operatorname{span}\{w_{ij}:i,j\in J\}+\mathbb C(1-e_J)
\]
form an increasing net; the zero last summand is omitted when \(e_J=1\). By (4.1), for a *-derivation \(D\) there is a skew-adjoint \(a_J\in P\) with
\[
\|a_J\|\le\|D\|,\qquad D|_{F_J}=[a_J,\cdot]|_{F_J}.
\]
The weak-* compact ball has a cluster point \(a\), still skew-adjoint and of norm at most \(\|D\|\). For fixed \(i,j\), the identity for \(w_{ij}\) holds eventually along the net, and separate weak-* continuity of multiplication gives
\[
D(w_{ij})=[a,w_{ij}].
\]
Step 2 gives \(D(c)=0\) for \(c\in Z(P)\). Hence (4.2) implies
\[
D(e_Jxe_J)=[a,e_Jxe_J].
\]
The projections \(e_J\) increase strongly to \(1\); consequently \(e_Jxe_J\to x\) strongly, with norms bounded by \(\|x\|\). Bounded strong convergence implies weak-* convergence [OT, Lemma 8.5](../../compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#OA-FND-LT-09). By Step 3 and separate normality of multiplication, \(D(x)=[a,x]\).

**4.3. Arbitrary type I algebras.** Decompose a type I algebra into its homogeneous central summands by [PT, Theorem 10.3](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-14). Apply 4.2 on each summand and combine the implementers by Step 2. Setting \(h=-ia\) for the combined skew-adjoint implementer gives
\[
D(x)=i[h,x],\qquad h=h^*\in P,\qquad \|h\|\le\|D\|
\tag{4.3}
\]
for every *-derivation of every type I von Neumann algebra. There is no restriction on the cardinalities of the homogeneous summands.

### 5. Spatiality with the same norm bound

Let \(M\subseteq B(H)\), and let \(D:M\to M\) be a *-derivation with \(\|D\|\le C\). We prove that
\[
D(x)=i[h,x]\quad(x\in M)
\]
for some \(h=h^*\in B(H)\) with \(\|h\|\le C\).

Choose a maximal abelian von Neumann subalgebra \(B\subseteq M'\). Existence follows from Zorn's lemma: the von Neumann algebra generated by the union of a chain of abelian unital algebras is abelian. Maximality gives
\[
M'\cap B'=B.
\tag{5.1}
\]
Indeed, a self-adjoint element of the left side can be adjoined to \(B\) while preserving commutativity; applying this to the real and imaginary parts proves (5.1).

Let \(\mathcal A_0\) be the linear span of products \(xe\), with \(x\in M\) and \(e\) a projection of \(B\). Any finite family of projections in \(B\) can be refined into pairwise orthogonal Boolean atoms whose sum is \(1\). Thus every element of \(\mathcal A_0\) can be written
\[
T=\sum_{j=1}^n x_je_j,
\qquad e_je_k=0\ (j\ne k),\qquad\sum_j e_j=1.
\]
For \(e\in\mathcal P(B)\), put \(z=c_{M'}(e)\). Then \(z\in Z(M)\), and the induction map
\[
Mz\longrightarrow Me\subseteq B(eH),\qquad xz\longmapsto xe,
\]
is an isometric *-isomorphism [DC, Theorem 5.8; PT, Proposition 3.5(3)](../../the-double-commutant-theorem.html#OA-FND-BI-04). By (2.1),
\[
\|D(x)e\|=\|D(x)z\|=\|D(xz)\|
\le C\|xz\|=C\|xe\|.
\tag{5.2}
\]
Define
\[
E(T)=\sum_{j=1}^nD(x_j)e_j.
\]
If \(T=0\), multiplying by \(e_j\) gives \(x_je_j=0\), and (5.2) gives \(D(x_j)e_j=0\). Refining two expressions to common Boolean atoms therefore proves that \(E\) is well-defined. The orthogonal block decomposition gives
\[
\|E(T)\|=\max_j\|D(x_j)e_j\|
\le C\max_j\|x_je_j\|=C\|T\|.
\]
Products of generators satisfy \((xe)(yf)=xyef\), and \(e,f\) commute with all elements of \(M\), including their derivatives. The product rule for \(D\) therefore proves the product rule for \(E\). The same calculation with adjoints proves that \(E\) is a *-derivation.

Extend \(E\) by norm continuity to \(\mathcal A=\overline{\mathcal A_0}^{\|\cdot\|}\), then normally to \(\mathcal A''\) by Step 3. Its norm remains at most \(C\). Spectral approximation shows that \(\mathcal A\) contains \(B\); hence
\[
\mathcal A''=(M\cup B)'',\qquad (\mathcal A'')'=M'\cap B'=B.
\]
An algebra with abelian commutant is type I [PT, Proposition 11.2](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-15). Step 4 supplies \(h=h^*\in\mathcal A''\), \(\|h\|\le C\), implementing \(E\), and therefore implementing \(D\) on \(M\). This is the spatial construction underlying [K66, Theorem 4], with its well-definedness and norm estimate supplied by (5.2).

Two consequences will be used repeatedly. First, (2.1) gives
\[
[h,z]=0\qquad(z\in Z(M)).
\tag{5.3}
\]
Second, if \(N=M'\), then \([h,N]\subseteq N\). For \(y\in N,x\in M\), direct expansion gives
\[
[[h,y],x]=[[h,x],y]=0,
\]
since \([h,x]\in M\). Consequently
\[
uhu^*-h\in N\qquad(u\in\mathcal U(N)).
\tag{5.4}
\]
Replacing \(h\) by \(h+t\) with \(t\in N_h\) does not change its commutator with \(M\).

### 6. A fixed-point theorem for linear isometries

We need the following result, including its proof.

**Lemma.** Let \(E\) be a real Banach space, \(K\subseteq E\) a nonempty weakly compact convex set, and \(G\) a group of surjective linear isometries of \(E\) with \(gK=K\). Then some point of \(K\) is fixed by every \(g\in G\).

**6.1. One bounded linear map.** If a bounded linear map \(F:E\to E\) satisfies \(F(K)\subseteq K\), fix \(x_0\in K\) and put
\[
x_n=\frac1n\sum_{j=0}^{n-1}F^jx_0.
\]
The set \(K\) is norm bounded: weak compactness gives pointwise boundedness on \(E^*\), and the Uniform Boundedness Theorem applies to the canonical images in \(E^{**}\). Write \(R=\sup_{x\in K}\|x\|\). Then
\[
x_n\in K,\qquad
\|Fx_n-x_n\|=\frac1n\|F^nx_0-x_0\|\le\frac{2R}{n}.
\]
A weakly convergent subnet has limit \(x\in K\). Bounded linear maps are weakly continuous, so \(Fx=x\).

**6.2. Small caps in a separable space.** Suppose that \(E\) is separable and \(K\) has more than one point. For every \(\varepsilon>0\), there is a proper weakly compact convex subset \(K_0\subsetneq K\) such that
\[
\operatorname{diam}(K\setminus K_0)\le\varepsilon.
\tag{6.1}
\]
Here and below closures in this substep are weak closures.

Let \(L=\overline{\operatorname{Ext}K}\). By [WT, Theorem 6.1](../../weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-06), \(L\) is nonempty and compact and \(K=\overline{\operatorname{co}}L\). Separability provides a countable cover of \(E\) by closed norm balls of radius \(\varepsilon/3\). Such balls are weakly closed, by Hahn–Banach separation. The Baire theorem for compact Hausdorff spaces, applied to \(L\), gives a ball \(B_0\) for which \(L\cap B_0\) contains a nonempty relatively weakly open subset \(U\) of \(L\).

If \(L\setminus U\) is empty, then \(K\subseteq B_0\), so \(\operatorname{diam}K\le2\varepsilon/3\). Any singleton in \(K\) is a proper subset satisfying (6.1).

Otherwise put
\[
K_1=\overline{\operatorname{co}}(L\setminus U),\qquad
K_2=\overline{\operatorname{co}}(L\cap B_0).
\]
Both are nonempty compact convex subsets of \(K\), and \(K_2\subseteq B_0\). The convex join
\[
\{tv+(1-t)w:v\in K_1,\ w\in K_2,\ 0\le t\le1\}
\]
is compact, convex, and contains \(L\); it is therefore \(K\).

Choose \(y\in\operatorname{Ext}K\cap U\), which exists because \(\operatorname{Ext}K\) is dense in \(L\). We have \(y\notin K_1\). Indeed, otherwise \(y\) would be extreme in \(K_1\), and the converse to Krein–Milman [WT, Theorem 6.2](../../weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-06), applied to the compact set \(L\setminus U\), would give \(y\in L\setminus U\).

For \(0<\eta<1\), define
\[
K_\eta=\eta K_1+(1-\eta)K
=\{tv+(1-t)w:v\in K_1,\ w\in K_2,\ \eta\le t\le1\}.
\]
The equality follows by substituting the preceding description of \(K\) into the first expression. This set is compact and convex. It does not contain \(y\): an expression \(y=\eta v+(1-\eta)k\), with \(v\in K_1,k\in K\), would force \(v=y\) by extremality.

If \(x,x'\notin K_\eta\), write
\[
x=tv+(1-t)w,\qquad x'=t'v'+(1-t')w'
\]
with \(v,v'\in K_1\), \(w,w'\in K_2\). Necessarily \(t,t'<\eta\). Since \(R=\sup_K\|x\|>0\),
\[
\begin{aligned}
\|x-x'\|
&\le t\|v-w\|+\|w-w'\|+t'\|v'-w'\|\\
&\le2R(t+t')+\frac{2\varepsilon}{3}
\le4R\eta+\frac{2\varepsilon}{3}.
\end{aligned}
\]
Choose \(\eta<\min\{1,\varepsilon/(12R)\}\). Then \(K_0=K_\eta\) proves (6.1).

**6.3. Finitely many isometries.** Given \(g_1,\dots,g_n\in G\), apply 6.1 to \(F=n^{-1}\sum_jg_j\), obtaining \(x\in K\) with
\[
x=\frac1n\sum_{j=1}^ng_jx.
\]
If some, but not all, of the \(g_j\) fix \(x\), cancel their contributions and renumber. To obtain a contradiction, we may thus assume
\[
x=\frac1m\sum_{j=1}^mg_jx,
\qquad g_jx\ne x\quad(1\le j\le m).
\tag{6.2}
\]
The subgroup \(G_0\) generated by these finitely many isometries is countable. Replace \(K\) by the weakly closed convex hull of \(G_0x\). This hull is a weakly compact subset of the original \(K\). It lies in the norm-closed linear span \(E_0\) of the countable orbit: a norm-closed linear subspace is weakly closed by Hahn–Banach. The space \(E_0\) is separable, and its weak topology is the subspace weak topology, again by Hahn–Banach extension. Thus 6.2 applies.

Choose
\[
0<\varepsilon<\min_{1\le j\le m}\|g_jx-x\|
\]
and a set \(K_0\subsetneq K\) satisfying (6.1). Some \(hx\), \(h\in G_0\), lies outside \(K_0\), since otherwise the closed convex hull of the orbit would be contained in \(K_0\). Equation (6.2) gives
\[
hx=\frac1m\sum_{j=1}^m hg_jx.
\]
Convexity of \(K_0\) implies that \(hg_jx\notin K_0\) for some \(j\). But then
\[
\|g_jx-x\|=\|hg_jx-hx\|\le\varepsilon,
\]
contrary to the choice of \(\varepsilon\). Therefore the original \(x\) is fixed by all \(g_1,\dots,g_n\).

**6.4. An arbitrary group.** For each \(g\), its fixed-point set in \(K\) is weakly closed. Substep 6.3 proves the finite intersection property for these sets. Compactness gives a point in their intersection. This proves the lemma.

The fixed-point argument follows [L26, Theorem 1, Proposition 2 and Lemma 3].

### 7. Finite algebras have nonzero normal finite traces

We first prove the projection estimates needed to construct a trace.

**7.1. Increasing comparison in a finite algebra.** Let \(P\) be a finite von Neumann algebra. If
\[
e_n\uparrow e,\qquad e_n\precsim f\quad(n\ge1),
\]
then \(e\precsim f\).

Construct partial isometries \(v_n\) with
\[
v_n^*v_n=e_n,\qquad v_nv_n^*\le f,\qquad v_{n+1}e_n=v_n.
\tag{7.1}
\]
Choose \(v_1\) using \(e_1\precsim f\). If \(v_n\) is chosen, choose \(w\) with \(w^*w=e_{n+1}\), \(ww^*\le f\). Put
\[
p=we_nw^*,\qquad r=v_nv_n^*,\qquad t=v_nw^*.
\]
Then \(t^*t=p\), \(tt^*=r\). The algebra \(fPf\) is finite [PT, Lemma 6.2](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-09). Complement equivalence in this finite algebra [PT, Proposition 14.2](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-18) gives a partial isometry \(t_0\) from \(f-p\) to \(f-r\). Hence \(u=t+t_0\) is a unitary of \(fPf\). Define \(v_{n+1}=uw\). It has the required initial and final projections, and
\[
v_{n+1}e_n=tw e_n=v_nw^*we_n=v_n.
\]
This proves (7.1).

For \(m\ge n\),
\[
v_m-v_n=v_m(e_m-e_n),\qquad
\|(v_m-v_n)\xi\|=\|(e_m-e_n)\xi\|.
\]
Thus \(v_n\) converges strongly to \(v\in P\). Moreover, \(\|v\xi\|=\|e\xi\|\) for every \(\xi\), so \(v^*v=e\), while \(fv=v\). Consequently \(vv^*\le f\), proving \(e\precsim f\).

We will also use reversal of comparison on complements in \(P\). If \(e\precsim f\), choose \(e_1\le f\) with \(e_1\sim e\). Proposition 14.2 gives \(1-e_1\sim1-e\). Since \(1-f\le1-e_1\),
\[
1-f\precsim1-e.
\tag{7.2}
\]

**7.2. Equivalent copies of orthogonal projections tend strongly to zero.** Suppose that \(f_n\in\mathcal P(P)\) are pairwise orthogonal and \(g_n\sim f_n\). We claim that \(g_n\to0\) strongly.

For \(n\ge m\), let
\[
r_{m,n}=\bigvee_{j=m}^n g_j,\qquad r_{m,m-1}=0,
\qquad d_{m,n}=r_{m,n}-r_{m,n-1}.
\]
The parallelogram law [PT, Proposition 4.4](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-04) gives
\[
d_{m,n}\sim g_n-(g_n\wedge r_{m,n-1})\precsim g_n\sim f_n.
\]
For fixed \(m\), the \(d_{m,n}\) are orthogonal. Additivity of subequivalence [PT, Lemma 3.3](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-01) yields
\[
r_{m,n}\precsim\sum_{j=m}^n f_j\le F_m,
\qquad F_m=\sum_{j\ge m}f_j.
\]
By 7.1,
\[
p_m:=\bigvee_{j\ge m}g_j\precsim F_m.
\]
Let \(p=\bigwedge_m p_m\). By (7.2),
\[
1-F_m\precsim1-p_m\le1-p.
\]
Orthogonality of the \(f_n\) gives \(F_m\downarrow0\) strongly, hence \(1-F_m\uparrow1\). Applying 7.1 again gives \(1\precsim1-p\). Finiteness of \(1\) forces \(p=0\): a subprojection of \(1-p\) equivalent to \(1\) must equal \(1\). Therefore \(p_m\downarrow0\) strongly. Since \(g_m\le p_m\),
\[
\|g_m\xi\|\le\|p_m\xi\|\longrightarrow0.
\tag{7.3}
\]

**7.3. Weak compactness of a normal state's conjugates.** Choose a normal state \(\varphi\) on a nonzero finite algebra \(P\), for example a unit-vector state in a faithful concrete representation. For every orthogonal sequence \((f_n)\subseteq\mathcal P(P)\),
\[
\sup_{u\in\mathcal U(P)}\varphi(u^*f_nu)\longrightarrow0.
\tag{7.4}
\]
Otherwise there are a subsequence \(f_{n_k}\), unitaries \(u_k\), and \(\varepsilon>0\) for which \(\varphi(u_k^*f_{n_k}u_k)\ge\varepsilon\). The projections \(g_k=u_k^*f_{n_k}u_k\) are equivalent to the orthogonal projections \(f_{n_k}\); (7.3) makes them converge strongly to zero. Their norms are bounded, so [OT, Lemma 8.5](../../compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#OA-FND-LT-09) gives weak-* convergence to zero, contradicting normality of \(\varphi\).

Let \(K\) be the weak closure in \(P_*\) of the convex hull of
\[
\{\varphi\circ\operatorname{Ad}u:u\in\mathcal U(P)\}.
\]
The convex hull is norm bounded and satisfies (7.4) uniformly. Therefore [PW, Theorem 10.2, implication (7)\(\Rightarrow\)(1)](../../polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#OA-FND-PD-16) makes \(K\) weakly compact. Positivity and value \(1\) at the identity are weakly closed conditions, so every element of \(K\) is a normal state.

The weak topology on the real self-adjoint part \((P_*)_h\) is its real Banach-space weak topology, by Hahn–Banach extension and complexification of real functionals. Conjugation acts on this real Banach space by surjective linear isometries preserving \(K\). The lemma in Step 6 gives a normal state \(\tau\in K\) invariant under all conjugations. For \(u\) unitary and \(x\in P\), invariance applied to \(xu\) gives
\[
\tau(ux)=\tau\bigl(u(xu)u^*\bigr)=\tau(xu).
\]
The unitaries linearly span \(P\) [CF, Proposition 7.3](../../c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-09), so
\[
\tau(yx)=\tau(xy)\qquad(x,y\in P).
\tag{7.5}
\]
Thus every nonzero finite von Neumann algebra has a nonzero normal finite trace, normalized here to be a state. The trace construction uses the orbit idea of [L25, Propositions 3 and 6]; 7.1–7.2 give all comparison and limiting details needed for its Proposition 7.

**7.4. Central supports and faithfulness.** The support \(s(\tau)\) exists and \(\tau\) is faithful on \(s(\tau)Ps(\tau)\) [UE, Lemma 11.1](../../the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-18). Unitary invariance and uniqueness of the support give
\[
us(\tau)u^*=s(\tau)\qquad(u\in\mathcal U(P)).
\]
Since unitaries span \(P\), \(s(\tau)\) is central.

Choose a maximal family of normal tracial states whose nonzero central supports \(z_i\) are pairwise orthogonal. If \(1-\sum_i z_i\ne0\), apply 7.3 to that finite central summand and extend its trace by zero to \(P\). Its nonzero support is orthogonal to every \(z_i\), contradicting maximality. Thus
\[
\sum_i z_i=1,
\]
and each \(Pz_i\) has a faithful normal tracial state.

If \(P\) is countably decomposable, this family is countable. Choose strictly positive scalar weights \(\lambda_i\) with \(\sum_i\lambda_i=1\). The norm-convergent sum
\[
\tau_0=\sum_i\lambda_i\tau_i\in P_*
\]
is a normal tracial state. It is faithful: for \(x\ge0\), \(\tau_0(x)=0\) forces \(\tau_i(x)=0\) for every \(i\), hence \(xz_i=0\) by faithfulness on \(Pz_i\), and then \(x=0\). Consequently every countably decomposable finite von Neumann algebra has a faithful normal tracial state.

### 8. Replacing a spatial implementer when the commutant is finite

We prove a statement about normalizing operators. Let \(P\subseteq B(H)\) be finite and countably decomposable, and let \(h=h^*\in B(H)\) satisfy
\[
\|h\|\le C,\qquad uhu^*-h\in P\quad(u\in\mathcal U(P)).
\tag{8.1}
\]
Then there exists \(k=k^*\in P'\) such that
\[
k-h\in P,\qquad \|k\|\le C.
\tag{8.2}
\]

Take a faithful normal tracial state \(\tau\) from Step 7. On the real vector space \(P_h\), set
\[
\langle x,y\rangle_2=\tau(xy),\qquad \|x\|_2=\tau(x^2)^{1/2}.
\]
The trace identity makes this a real symmetric bilinear form: \(\overline{\tau(xy)}=\tau(yx)=\tau(xy)\). Faithfulness makes it positive definite. Let \(L^2(P,\tau)_h\) denote its real Hilbert completion, and \(j:P_h\to L^2(P,\tau)_h\) the injective inclusion.

Put
\[
c(u)=uhu^*-h\in P_h,
\qquad T_u(y)=c(u)+uyu^*.
\]
Conjugation preserves \(\|\cdot\|_2\), by the trace property. Also
\[
c(uv)=c(u)+uc(v)u^*.
\]
Thus the \(T_u\) extend to an action by affine isometries of the real Hilbert space. The orbit of zero is \(\{j(c(u))\}\), and it is bounded, since \(\|c(u)\|_2\le\|c(u)\|\le2C\). Its Hilbert-norm closed convex hull \(S\) is nonempty, bounded, and invariant under every \(T_u\).

**8.1. A Hilbert-space circumcentre.** For \(y\in S\), define
\[
R(y)=\sup_{s\in S}\|y-s\|_2,\qquad r=\inf_{y\in S}R(y).
\]
For \(y,z\in S\), the parallelogram identity gives
\[
R\!\left(\frac{y+z}{2}\right)^2
\le\frac{R(y)^2+R(z)^2}{2}-\frac{\|y-z\|_2^2}{4}.
\]
Since the midpoint belongs to \(S\),
\[
\|y-z\|_2^2\le2R(y)^2+2R(z)^2-4r^2.
\tag{8.3}
\]
A sequence with \(R(y_n)\to r\) is therefore Cauchy. Its limit lies in \(S\), and the inequality \(|R(y)-R(z)|\le\|y-z\|_2\) shows that it attains \(r\). Equation (8.3) proves uniqueness. As each \(T_u\) is an isometry carrying \(S\) onto itself, it preserves \(R\) and hence fixes this unique point, say \(y_0\).

**8.2. Recovering the operator norm bound.** Let
\[
K=\overline{\operatorname{co}}^{\,w^*}
\{uhu^*:u\in\mathcal U(P)\}\subseteq B(H)_h.
\]
It is weak-* compact and contained in the operator-norm ball of radius \(C\). From (8.1),
\[
K-h\subseteq P_h,\qquad \|t\|\le2C\quad(t\in K-h).
\tag{8.4}
\]
The weak-* topology of \(P\) is the subspace \(\sigma\)-weak topology from \(B(H)\), by [OT, Theorem 9.4](../../compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#OA-FND-LT-10). On a norm-bounded subset of \(P_h\), the map \(j\) is continuous from weak-* to Hilbert-space weak topology. For a test vector \(j(z)\), \(z\in P_h\), this follows because
\[
\langle j(t),j(z)\rangle_2=\tau(tz)
\]
is a normal functional of \(t\). For an arbitrary Hilbert-space test vector, approximate it in \(\|\cdot\|_2\) by such \(j(z)\); the approximation is uniform over (8.4), since \(\|j(t)\|_2\le2C\).

It follows that \(j(K-h)\) is weakly compact and convex in the Hilbert space, and hence norm closed. It contains the orbit of zero, so it contains \(S\). In particular \(y_0=j(t)\) for some \(t\in K-h\). Since \(j\) is injective, the fixed-point equations for \(y_0\) give
\[
c(u)+utu^*=t\qquad(u\in\mathcal U(P)).
\]
Thus \(k=h+t\in K\) satisfies \(uku^*=k\) for all unitaries of \(P\). Their linear span is \(P\), so \(k\in P'\), and \(\|k\|\le C\). This proves (8.2).

Applied to \(P=M'\), using (5.4), this replaces the spatial implementer by a self-adjoint element of \(M\), without increasing its norm, whenever \(M'\) is finite and countably decomposable.

### 9. Averaging in a countably decomposable type III algebra

We prove the exact averaging assertion needed for the type III case.

**Lemma.** Let \(P\) be a countably decomposable type III von Neumann algebra, and let \(x=x^*\in P\). There is a least self-adjoint central majorant \(b=b(x)\) of \(x\), and
\[
\|b\|\le\|x\|,\qquad
b\in\overline{\operatorname{co}}^{\|\cdot\|}
\{uxu^*:u\in\mathcal U(P)\}.
\tag{9.1}
\]

If \(x=0\), take \(b=0\). Otherwise let \(R=\|x\|\) and consider
\[
\mathcal C_x=\{c\in Z(P)_h:x\le c\le R1\}.
\]
It is nonempty. If \(c,d\in\mathcal C_x\), the central projection
\[
e=1_{(-\infty,0]}(c-d)
\]
satisfies
\[
\min(c,d)=ec+(1-e)d\ge x.
\]
Thus \(\mathcal C_x\) is downward directed, and its elements lie between \(-R1\) and \(R1\). The bounded decreasing net of these elements has a strong limit \(b\), by [ST, Theorem 6.1](../../the-spectral-theorem-for-bounded-self-adjoint-operators.html#OA-FND-ST-06). The centre is strongly closed, so \(b\in Z(P)_h\). Passing to the strong limit in the inequalities gives \(x\le b\le R1\), and \(b\le c\) for every \(c\in\mathcal C_x\). If \(c\) is any other central self-adjoint majorant of \(x\), then \(\min(c,R1)\in\mathcal C_x\), so \(b\le c\). This proves leastness and \(\|b\|\le R\).

For \(\varepsilon>0\), set
\[
p=1_{[0,\varepsilon)}(b-x),\qquad q=1-p.
\]
The central support of \(p\) is \(1\). Otherwise \(z=1-c(p)\ne0\) is central and annihilates \(p\). Spectral calculus then gives
\[
z(b-x)\ge\varepsilon z.
\]
Consequently \(b-\varepsilon z\) is a central majorant of \(x\) strictly smaller than \(b\), a contradiction.

Put \(w=c(q)\). If \(w\ne0\), both \(wp\) and \(q\) have central support \(w\) in \(Pw\). Every nonzero projection of a type III algebra is properly infinite [PT, Lemma 6.2(3) and Definition 7.1](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-09). The algebra \(Pw\) is countably decomposable. Therefore [PT, Proposition 15.2(4)](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-19) gives
\[
wp\sim w\sim q.
\tag{9.2}
\]
For any integer \(n\ge2\), repeated halving [PT, Proposition 13.4](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-17) partitions \(w\) into orthogonal projections
\[
w=q_1+\cdots+q_n,\qquad q_j\sim w.
\]
For every \(j\), \(w-q_j\sim w\), since it contains one of the other \(q_k\sim w\) and is at most \(w\); use projection Schröder–Bernstein [PT, Proposition 5.1](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-03). By (9.2),
\[
q\sim q_j,\qquad wp=w-q\sim w-q_j.
\]
Add partial isometries implementing these two equivalences. Their orthogonal initial and final projections make their sum a unitary of \(Pw\) sending \(q\) to \(q_j\). Extend it by \(1-w\) to a unitary \(u_j\in P\).

Functional calculus gives
\[
0\le b-x\le\varepsilon1+2R q.
\]
Each \(u_j\) commutes with the central element \(b\), so
\[
0\le b-\frac1n\sum_{j=1}^nu_jxu_j^*
\le\varepsilon1+\frac{2R}{n}\sum_{j=1}^nq_j
=\varepsilon1+\frac{2R}{n}w.
\tag{9.3}
\]
If \(w=0\), then \(q=0\) and \(0\le b-x\le\varepsilon1\), which gives the needed approximation with the identity unitary. For any prescribed error, choose \(\varepsilon\) small and then \(n\) large in (9.3). This proves (9.1).

### 10. Replacing a spatial implementer when the commutant is type III

Let \(M\subseteq B(H)\), let \(N=M'\) be countably decomposable and type III, and let \(h=h^*\), \(\|h\|\le C\), be the spatial implementer from Step 5. We construct
\[
h_0=h_0^*\in M,\qquad \|h_0\|\le C,
\qquad h_0-h\in N.
\tag{10.1}
\]
For \(C=0\), take \(h_0=0\). Suppose \(C>0\), put \(b=h+C1\), and define
\[
K=\overline{\operatorname{co}}^{\,w^*}
\{ubu^*:u\in\mathcal U(N)\}.
\]
Then
\[
K\subseteq[0,2C1]\cap(b+N)_h.
\tag{10.2}
\]
Also every element of \(K\) commutes with \(Z(N)=Z(M)\), by (5.3). The set \(K\) is nonempty, weak-* compact, convex, and invariant under conjugation by \(\mathcal U(N)\).

Choose an inclusion-minimal nonempty weak-* compact convex invariant subset \(L\subseteq K\). Zorn's lemma applies because an inclusion-decreasing chain has nonempty intersection by compactness of \(K\), and that intersection remains compact, convex, and invariant.

For a central projection \(z\in N\) and \(k\in L\), the set
\[
\{l\in L:\|lz\|\le\|kz\|\}
\]
is nonempty, weak-* compact, convex, and invariant. Weak-* closedness follows from lower semicontinuity of the norm and normality of multiplication by \(z\); invariance follows because the conjugating unitaries commute with \(z\). Minimality forces this set to be all of \(L\). Interchanging \(k,l\), we obtain
\[
\|kz\|=\|lz\|\qquad(k,l\in L,\ z\in\mathcal P(Z(N))).
\tag{10.3}
\]

The difference set
\[
V=L-L
\]
is a weak-* compact convex symmetric invariant subset of \(N_h\), by (10.2). Suppose \(d\in V\) is nonzero. Replacing \(d\) by \(-d\) if necessary, arrange that its positive part is nonzero. Apply Step 9 inside \(N\). The central majorant \(b_N(d)\) belongs to the norm-closed convex hull of the unitary orbit of \(d\), and hence to \(V\). Since \(b_N(d)\ge d\), it cannot be nonpositive. There are therefore \(\varepsilon>0\) and a nonzero central spectral projection \(z\) with
\[
b_N(d)z\ge\varepsilon z.
\]
Write \(b_N(d)=k-l\) with \(k,l\in L\). The operators \(k,l\) are positive and commute with \(z\), so
\[
kz\ge lz+\varepsilon z.
\]
On the nonzero Hilbert space \(zH\), positivity implies
\[
\|kz\|\ge\|lz+\varepsilon z\|=\|lz\|+\varepsilon,
\]
contradicting (10.3). Thus \(V=\{0\}\), and \(L\) is a singleton, say \(\{k\}\).

Its invariance makes \(k\) commute with every unitary of \(N\), hence with \(N\), so \(k\in N'=M\). By (10.2), \(0\le k\le2C1\) and \(k-b\in N\). Set \(h_0=k-C1\). Then \(-C1\le h_0\le C1\), and (10.1) follows.

The minimal-invariant-set argument is the part of [K66, Addendum, Theorem 15, p. 292] needed here. Its averaging input has been proved explicitly in Step 9.

### 11. Finite, properly infinite, and semifinite commutants

We now prove innerness, with the same bound \(C\), for every concrete algebra whose commutant is countably decomposable.

**11.1. A full finite corner in a semifinite algebra.** Let \(N\) be semifinite. Every nonzero central summand of \(N\) contains a nonzero finite projection. Indeed, by [PT, Definition 7.1 and Theorem 7.2](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-10), a nonzero type I part contains an abelian projection, which is finite by Lemma 6.2; a nonzero type II part contains a nonzero finite projection by the definition of type II. There is no type III central part in a semifinite algebra.

Choose a maximal family of nonzero finite projections \(q_j\in N\) whose central supports \(z_j=c_N(q_j)\) are pairwise orthogonal. If \(z=1-\sum_jz_j\ne0\), a nonzero finite projection in \(Nz\) would enlarge the family. Hence \(\sum_jz_j=1\). The strong sum
\[
q=\sum_jq_j
\]
is finite by [PT, Lemma 6.3](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-09), which proves finiteness of centrally orthogonal sums of finite projections. Moreover,
\[
c_N(q)=1.
\tag{11.1}
\]
For if a central projection majorizes \(q\), it majorizes every \(q_j\), and therefore every \(z_j\).

**11.2. Compression of a spatial implementer.** Let \(M\subseteq B(H)\), \(N=M'\), and suppose now that \(N\) is countably decomposable and semifinite. Let \(D\) be a *-derivation of \(M\) with \(\|D\|\le C\), and take a spatial implementer \(h=h^*\), \(\|h\|\le C\), from Step 5. Choose \(q\in N\) as in 11.1.

By [DC, Theorem 5.8; PT, Proposition 3.5(3)](../../the-double-commutant-theorem.html#OA-FND-BI-04), the map
\[
\sigma:M\longrightarrow B(qH),\qquad \sigma(x)=xq|_{qH},
\]
has a von Neumann algebra as its image, with commutant \(qNq\), and its kernel is \(M(1-c_N(q))=0\). It is therefore an isometric *-isomorphism onto its image, and is normal in both directions by [UE, Corollary 11.4](../../the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-18). Transport \(D\) to \(\sigma(M)\), writing
\[
D_q(\sigma(x))=\sigma(D(x)).
\]
For \(h_q=qhq|_{qH}\), direct multiplication, using \(xq=qx\), gives
\[
i[h_q,\sigma(x)]=iq[h,x]q|_{qH}
=\sigma(D(x)).
\tag{11.2}
\]
Also \(\|h_q\|\le C\).

The algebra \(qNq\) is finite, because \(q\) is a finite projection, and is countably decomposable, because any orthogonal family in it is an orthogonal family in \(N\). From (11.2), the commutator calculation following (5.3), now in \(B(qH)\), gives
\[
vh_qv^*-h_q\in qNq\qquad(v\in\mathcal U(qNq)).
\]
Step 8 therefore provides a self-adjoint
\[
k_q\in(qNq)'=\sigma(M),\qquad \|k_q\|\le C,
\]
with \(k_q-h_q\in qNq\). It implements \(D_q\). Its inverse image \(k=\sigma^{-1}(k_q)\) is self-adjoint, has norm at most \(C\), and satisfies
\[
D(x)=i[k,x]\qquad(x\in M),
\]
by injectivity of \(\sigma\).

This argument includes properly infinite semifinite algebras, of types I and II. In the finite case one may take \(q=1\), reducing directly to Step 8. No trace on the original semifinite algebra is assumed or used; the finite trace is constructed on the finite corner.

**11.3. The complete countably decomposable-commutant case.** For an arbitrary countably decomposable \(N=M'\), [PT, Theorem 7.2](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-10) first splits its identity by central projections into a finite part and a properly infinite part. For completeness, if \(1=e_f+e_p\) with orthogonal central supports, then \(c(e_f)=c(e_f)(e_f+e_p)=e_f\), and similarly \(e_p\) is central. The type decomposition then splits the properly infinite part into its semifinite and type III parts. Thus there are pairwise orthogonal central projections
\[
z_f+z_s+z_3=1
\]
with \(Nz_f\) finite, \(Nz_s\) properly infinite and semifinite, and \(Nz_3\) type III; zero parts are omitted.

These projections belong to \(Z(M)\). On each \(z_jH\), the algebras \(Mz_j\) and \(Nz_j\) are mutual commutants [DC, Theorem 5.8](../../the-double-commutant-theorem.html#OA-FND-BI-04). Each commutant remains countably decomposable. Equation (5.3) makes \(hz_j\) a self-adjoint spatial implementer on that subspace, of norm at most \(C\). Apply Step 8 on \(z_f\), 11.2 on \(z_s\), and Step 10 on \(z_3\). The resulting self-adjoint implementers in \(Mz_j\) all have norm at most \(C\). Step 2 combines them into one self-adjoint \(k\in M\) with \(\|k\|\le C\).

We have proved:
\[
\boxed{\ M'\text{ countably decomposable},\ D\text{ a *-derivation}
\ \Longrightarrow\ D=i[k,\cdot],\quad k=k^*\in M,
\quad\|k\|\le\|D\|.\ }
\tag{11.3}
\]

### 12. Arbitrary central sums through faithful cyclic representations

An arbitrary von Neumann algebra need not be a central sum of countably decomposable algebras. The reduction needed here is instead to faithful cyclic representations of central summands; their **commutants** are countably decomposable. We prove that reduction.

Fix a concrete \(M\subseteq B(H)\), and put \(N=M'\). For a nonzero vector \(\xi\in H\), let \(p_\xi\) be the projection onto \([M\xi]\). This subspace reduces \(M\), so \(p_\xi\in N\). Put
\[
z_\xi=c_N(p_\xi)\in Z(N)=Z(M).
\]
The induction results [DC, Theorem 5.8; PT, Proposition 3.5(3)](../../the-double-commutant-theorem.html#OA-FND-BI-04), together with normality of *-isomorphisms [UE, Corollary 11.4](../../the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-18), give a faithful normal isometric representation
\[
\rho_\xi:Mz_\xi\longrightarrow B(p_\xi H),
\qquad \rho_\xi(x)=xp_\xi|_{p_\xi H},
\tag{12.1}
\]
whose image is a von Neumann algebra with commutant
\[
\rho_\xi(Mz_\xi)'=p_\xi Np_\xi.
\tag{12.2}
\]
The vector \(\xi\) is cyclic for the image in (12.1). It is separating for the algebra in (12.2): if \(t\xi=0\) and \(t\in p_\xi Np_\xi\), then
\[
t(x\xi)=x(t\xi)=0\qquad(x\in M),
\]
and these vectors have dense span in \(p_\xi H\), so \(t=0\).

It follows directly that \(p_\xi Np_\xi\) is countably decomposable. Indeed, if \((e_j)\) is an orthogonal family of nonzero projections in it, each \(e_j\xi\ne0\), while
\[
\sum_{j\in F}\|e_j\xi\|^2\le\|\xi\|^2
\]
for every finite subfamily \(F\). A family of strictly positive real numbers with bounded finite subsums is countable: for each positive integer \(n\), only finitely many terms can exceed \(1/n\), and every positive term exceeds \(1/n\) for some \(n\). Thus the family of projections is countable.

Choose, by Zorn's lemma, a maximal family \((\xi_i)_{i\in I}\) for which the nonzero central projections \(z_i=z_{\xi_i}\) are pairwise orthogonal. Their strong sum is \(1\). To see this, if
\[
z=1-\sum_i z_i\ne0,
\]
choose a nonzero \(\xi\in zH\). Since \(z\) is central, \(M\xi\subseteq zH\); thus \(p_\xi\le z\) and \(0\ne z_\xi\le z\). This contradicts maximality.

Let \(D\) be a *-derivation of \(M\), and set \(C=\|D\|\). Step 2 restricts it to each \(Mz_i\), with norm at most \(C\). Transport that restriction through the isomorphism \(\rho_{\xi_i}\). Its image algebra has countably decomposable commutant by (12.2), so (11.3) gives a self-adjoint implementer of norm at most \(C\) there. Pull it back through \(\rho_{\xi_i}\), obtaining
\[
h_i=h_i^*\in Mz_i,\qquad \|h_i\|\le C,
\qquad D|_{Mz_i}=i[h_i,\cdot].
\]
The uniform central-sum construction of Step 2 applies to the arbitrary index set \(I\). It gives
\[
h=\sum_i h_i\in M_h,\qquad \|h\|\le C,
\qquad D(x)=i[h,x]\quad(x\in M).
\tag{12.3}
\]
This is the central-cyclic reduction in [K66, Addendum, Theorem 15, pp. 291–292], with the countability assertion made on the commutants and the uniform summation estimate given explicitly.

### 13. General derivations, the bound, and uniqueness

Let \(\delta\) now be an arbitrary complex-linear derivation of \(M\). It is bounded by Step 1. The *-derivations \(\delta_1,\delta_2\) in 1.1 satisfy (1.1). By (12.3), choose
\[
h_j=h_j^*\in M,\qquad
\delta_j=i[h_j,\cdot],\qquad
\|h_j\|\le\|\delta_j\|\le\|\delta\|
\quad(j=1,2).
\]
Then
\[
\delta=\delta_1+i\delta_2=[ih_1-h_2,\cdot].
\]
Thus
\[
a=ih_1-h_2\in M,\qquad
\|a\|\le\|h_1\|+\|h_2\|\le2\|\delta\|.
\]
If \(\delta\) itself preserves the involution, (12.3) directly gives \(a=ih\), \(h=h^*\), \(\|h\|\le\|\delta\|\).

Finally,
\[
[a,x]=[b,x]\text{ for every }x\in M
\quad\Longleftrightarrow\quad
[a-b,x]=0\text{ for every }x\in M
\quad\Longleftrightarrow\quad a-b\in Z(M).
\]
This proves uniqueness modulo the centre and its converse. If \(b\) is any implementer and \(a\) is one of the bounded implementers just constructed, then \(b-a\in Z(M)\), so
\[
\operatorname{dist}(b,Z(M))\le\|a\|.
\]
All the stated conclusions follow. \(\square\)

## Closedness under a finite-dimensional extension

**Lemma.** Let \(E\) be a normed space, \(F\subseteq E\) a closed linear subspace and \(V\subseteq E\) a finite-dimensional subspace. Then \(F+V\) is closed in \(E\).

**Proof.** Write \(q:E\to E/F\) for the quotient map. The formula
\[
\|q(x)\|=\inf_{f\in F}\|x-f\|
\]
is independent of the representative, since translating \(x\) by an element of \(F\) merely permutes the elements over which the infimum is taken. It defines a norm: the triangle inequality follows by adding approximants in \(F\), and homogeneity follows by rescaling them; zero norm implies \(x\in\overline F=F\). Also \(\|q(x)\|\le\|x\|\), so \(q\) is continuous. The image \(q(V)\) is finite-dimensional and is therefore closed in the normed, hence Hausdorff, space \(E/F\), by [HB, Theorem 7.1](../../hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-07)(2). Since \(F+V=q^{-1}(q(V))\), the desired sum is closed. No completeness assumption on the quotient is needed. \(\square\)

In Step 1, faithful representation is isometric by [CF, Corollary 4.6](../../c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-12), so the represented C*-algebra is closed in \(B(H)\). Apply the lemma with \(E=B(H)\), \(F=A\) and \(V=\mathbb C1\).

## Compactness, intersections and convergent subnets

**Lemma.** A family of closed subsets of a compact space has nonempty intersection if every finite subfamily has nonempty intersection. Every net in a compact space has a convergent subnet. Neither assertion requires metrizability or a countable index set.

**Proof.** If the closed sets had empty intersection, their open complements would cover the space. A finite subcover would contradict the finite intersection assumption.

For a net \((x_i)_{i\in I}\) in a compact space \(K\), let \(F_i\) be the closure of its tail \(\{x_j:j\ge i\}\). These nonempty closed sets have the finite intersection property, because any finite set of indices has a common upper bound. Choose \(x\in\bigcap_iF_i\). Every open neighbourhood of \(x\) meets every tail.

Let \(D\) consist of pairs \((i,U)\), where \(U\) is an open neighbourhood of \(x\) and \(x_i\in U\). Order it by \((i,U)\preceq(j,V)\) when \(i\le j\) and \(V\subseteq U\). It is directed: given two pairs, choose an upper bound of their indices and then a later term lying in the intersection of their neighbourhoods. The projection \(D\to I\), \((i,U)\mapsto i\), is order-preserving and cofinal, since \((i,K)\in D\) for every \(i\). The resulting subnet converges to \(x\): after any pair whose neighbourhood is contained in a prescribed neighbourhood \(U_0\), all subsequent terms lie in \(U_0\). Such a pair exists because every neighbourhood meets every tail. \(\square\)

## Results used

### Results proved in the attached lessons

The following results are used from the indicated attached lessons, with their existing proofs.

**[CF](../../c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-07) Order, local units and quotients of C*-algebras.** Theorem 5.1, continuous functional calculus; Corollary 4.6, isometry of injective *-homomorphisms; Proposition 7.3, linear spanning by unitaries; Theorem 8.2 and Proposition 8.5, the positive cone and its order properties. These supply spectral cuts, square roots, order estimates, and isometric transport. **Proof status:** proved in the attached lesson.

**[GNS](../../representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#OA-FND-GN-03) Building representations from positive functionals.** Proposition 3.2, Cauchy–Schwarz for positive functionals; Theorem 4.7, boundedness and the norm of positive functionals; Proposition 7.1a, extension of states from a unital subalgebra and norm-attaining states on positive elements; Theorem 7.2, faithful Gelfand–Naimark representation. **Proof status:** proved in the attached lesson.

**[ST](../../the-spectral-theorem-for-bounded-self-adjoint-operators.html#OA-FND-ST-03) The spectral theorem for bounded self-adjoint operators.** Theorem 3.1, bounded Borel functional calculus; Proposition 5.1, spectral projections in a von Neumann algebra; Theorem 6.1, strong convergence of bounded monotone nets of self-adjoint operators. **Proof status:** proved in the attached lesson.

**[DC](../../the-double-commutant-theorem.html#OA-FND-BI-06) The double commutant theorem.** Theorem 4.4, strong and \(\sigma\)-weak density; Theorem 5.8, reduced and induced algebras, their mutual commutants, and their central-support kernels. **Proof status:** proved in the attached lesson.

**[PT](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-01) Projections and types of von Neumann algebras.** Proposition 3.1, the projection lattice; Lemma 3.3, additivity of equivalence and subequivalence; Proposition 3.5, central supports and induction kernels; Proposition 4.4, the parallelogram law; Proposition 5.1, projection Schröder–Bernstein; Lemmas 6.2–6.3, finiteness properties and centrally orthogonal sums; Definition 7.1 and Theorem 7.2, types and the central type/finite–properly-infinite decompositions; Proposition 8.4, matrix units; Proposition 9.1 and Theorem 10.3, homogeneous type I structure and its central decomposition; Proposition 11.2, an abelian commutant implies type I; Proposition 13.4, halving of properly infinite projections; Proposition 14.2, unitary equivalence of equivalent finite projections and equivalence of their complements; Proposition 15.2(4), equivalence of a full properly infinite projection with the identity in a locally countably decomposable algebra. **Proof status:** proved in the attached lesson. Increasing continuity of comparison, which is additional to this list, is proved in 7.1 above.

**[PW](../../polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#OA-FND-PD-16) Polar decomposition of functionals and weak compactness in preduals.** Theorem 10.2, specifically implication (7)\(\Rightarrow\)(1): bounded families of normal functionals uniformly tending to zero on every orthogonal projection sequence are relatively weakly compact. **Proof status:** proved in the attached lesson. The uniform hypothesis for the family used here is proved in 7.1–7.3 above.

**[UE](../../the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#OA-FND-WA-02) The universal enveloping von Neumann algebra of a \(C^*\)-algebra, and \(W^*\)-algebras.** Lemma 2.1(2)–(4), normal extension of representations, central kernels, and normal inverses on central corners; Theorem 3.3, identification of \(A^{**}\) with the enveloping von Neumann algebra; Lemma 6.3, finite-dimensional algebras as finite sums of matrix algebras; Lemma 11.1, supports and faithfulness of normal positive functionals on their supports; Corollary 11.4, normality of *-isomorphisms of von Neumann algebras. **Proof status:** proved in the attached lesson. The extension of a derivation, as opposed to a representation, is proved in Step 3 above.

**[WT](../../weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-02) Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian.** Theorem 3.1, Banach–Alaoglu; Theorem 5.2, Goldstine density; Proposition 5.3, second adjoints and their norms; Theorem 6.1, Krein–Milman; Theorem 6.2, its converse due to Milman. **Proof status:** proved in the attached lesson.

**[OT](../../compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html#OA-FND-LT-07) Compact and trace-class operators, the predual of B(H), and the operator topologies.** Theorem 6.2, the trace-class predual of \(B(H)\); Lemma 8.5, agreement of weak and \(\sigma\)-weak topologies, and of strong and \(\sigma\)-strong topologies, on bounded sets; Proposition 8.6, continuity of involution and separate continuity of multiplication; Theorem 9.4, the predual of a concrete von Neumann algebra and its induced \(\sigma\)-weak topology. **Proof status:** proved in the attached lesson.

### Foundational results and their providers

The real and complex Hahn–Banach theorems are [HB, Theorem 2.1](../../hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-02) and [HB, Theorem 2.2](../../hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-02). The Closed Graph Theorem is [HB, Theorem 5.3](../../hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-05); uniform boundedness is [HB, Theorem 4.2](../../hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-04). Compact Hausdorff Baire and the small-diameter consequence are [HB, Theorem 3.2](../../hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-03-LCH) and [HB, Corollary 3.3](../../hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-03-LCH). The compactness criterion and Tychonoff theorem are [WT, Lemma 2.2](../../weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-02) and [WT, Theorem 2.3](../../weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-02). The [compactness bridge above](#OA-FND-INNER-COMPACTNESS) supplies the finite intersection and convergent-subnet arguments. Normed-space and Hilbert completions, including extension of bounded maps, are proved in [HS, Lemma (Completion)](../../hilbert-spaces-and-compact-operators.html#completing-normed-and-inner-product-spaces). The closedness bridge above supplies the finite-dimensional-extension argument. [HB, Theorem 1.1](../../hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-01) proves Zorn’s lemma from the explicitly assumed axiom of choice. The Hilbert-space circumcentre argument is proved in Step 8.1, not left as an additional theorem.

### Free-source arguments whose needed conclusions are proved above

**[S60], unnumbered theorem, pp. 31–32:** the positive spectral cut and state argument for automatic continuity. **Proof status:** complete in Step 1, including nonunital algebras and algebraic *-splitting.

**[K66], Lemma 3, Theorem 4, and Addendum, Theorem 15:** normal extension, spatiality, the central-cyclic reduction, and the minimal-invariant-set argument. **Proof status:** complete in Steps 3–5 and 9–12; Step 3 uses the bidual construction rather than requiring any unproved continuity assertion from the paper. Finite-dimensional averaging, the finite-commutant argument, and the type III averaging input are proved in Steps 4, 8, and 9. The collected-works copy specified under **Source references** is the copy used.

**[L25], Lemma 2, Propositions 3, 6 and 7; [L26], Theorem 1, Proposition 2 and Lemma 3:** finite normal traces through a weakly compact predual orbit, and the isometric fixed-point argument. **Proof status:** complete in Steps 6–7, with the corrections stated below. Full bibliographic details and URLs for all these free sources are in the following source list.

## Scope cautions and corrections to source arguments

### Countable decomposability in the reduction

The assertion that every von Neumann algebra is a central sum of countably decomposable algebras is false. For example, if \(I\) is uncountable, then \(B(\ell^2(I))\) has uncountably many orthogonal rank-one projections and is not countably decomposable. Its centre is \(\mathbb C1\): an operator commuting with all rank-one projections is diagonal in an orthonormal basis, and commuting with the rank-one matrix units makes all diagonal entries equal. Thus it has no nontrivial central decomposition at all.

The correct reduction is (12.1)–(12.2): central summands admit faithful normal cyclic representations whose **commutants** are countably decomposable. Step 12 proves this reduction, and Step 2 supplies the uniform norm estimate for reassembly. This does not change the definition of “locally \(\sigma\)-finite” in [PT, Definition 15.1](../../projections-and-types-of-von-neumann-algebras.html#OA-FND-TY-19), which is a genuine additional property and is not asserted there for every algebra.

### Corrections and completed steps in the free-source arguments

**Finite traces: [L25, Proposition 3, p. 1].** Delete “faithful” from the assertion for an arbitrary nonzero finite von Neumann algebra. The universally valid conclusion is a nonzero normal finite trace, faithful on its central support. A faithful normal tracial state on the entire algebra is obtained here under countable decomposability, in 7.4.

For a counterexample to the uncorrected assertion, take \(P=\ell^\infty(I)\) with \(I\) uncountable. It is finite because equivalence of projections in an abelian algebra implies equality. Let \(e_i\) denote its coordinate projections. For any bounded positive functional \(\omega\),
\[
\sum_{i\in F}\omega(e_i)\le\omega(1)
\]
for every finite \(F\). Hence at most countably many of the numbers \(\omega(e_i)\) can be positive. A faithful functional would make every one of them positive, a contradiction. In [L25, Lemma 2], “faithful” should likewise be removed from the hypothesis when that lemma is used to extract the central support; with that word retained the stated splitting is only the trivial splitting.

**Fixed points: [L25, Theorem 5, p. 2; L26, Theorem 1, p. 1].** The fixed-point argument requires a group of linear isometries, not merely a group each of whose operators is bounded. The needed formulation is proved in Step 6. The isometry hypothesis is missing from Lecture 25's statement, but is already present in Lecture 26's Theorem 1. Conjugation on the predual is a surjective linear isometry, so the corrected theorem applies.

**Projection ranges and comparison limits: [L25, Proposition 7, p. 3].** The displayed orthogonal-projection map from \(g_nV\) to the incremental closed subspace is not necessarily surjective; it has dense range, which suffices after polar decomposition. Concretely, in \(M_2(L^\infty(0,1))\) on \(L^2((0,1);\mathbb C^2)\), let \(e\) project onto the first coordinate and let \(f(t)\) project onto the unit vector
\[
(\sqrt{1-t^2},t),\qquad 0<t<1.
\]
Then \(e\vee f=1\), but \((1-e)|_{fH}\), after identifying \(fH\) with \(L^2(0,1)\), is multiplication by \(t\) onto the second coordinate. Its range is dense and is not all of \(L^2(0,1)\): the constant function \(1\) would require the non-square-integrable preimage \(1/t\). The projection inequality actually needed is the parallelogram inequality used in 7.2. The subsequent passage from comparison of all finite initial pieces to comparison of their supremum is proved by the coherent partial isometries in 7.1, rather than left implicit.

**The small-cap argument: [L26, Lemma 3, proof on pp. 2–3].** For the set defined by coefficients in \([\eta,1]\), the coefficient condition in the extremal-point argument is \(t\ge\eta\), not \(t\le1-\eta\). For two points outside that set, the applicable diameter estimate is
\[
2R(t+t')+2\varepsilon/3\le4R\eta+2\varepsilon/3,
\]
not an intermediate bound using \(4Rt\) alone. Substep 6.2 gives these bounds, proves convexity of the truncated join through \(K_\eta=\eta K_1+(1-\eta)K\), and handles the case \(L\setminus U=\varnothing\).

The affine action in Step 8 uses a circumcentre, not a minimum-distance-to-zero point: an affine isometry need not preserve distance to zero. Existence, uniqueness and invariance of the circumcentre, as well as the return to the original operator-norm ball, are proved in 8.1–8.2.

## Source references

**[S60] Shôichirô Sakai.** *On a conjecture of Kaplansky*. Tôhoku Mathematical Journal, Second Series **12** (1960), 31–33. Original journal version, received 14 August 1959. Source loci: the unnumbered theorem and its full proof, pp. 31–32; reference page 33.

<https://www.jstage.jst.go.jp/article/tmj1949/12/1/12_1_31/_pdf/-char/en>

**[K66] Richard V. Kadison.** *Derivations of operator algebras*. Annals of Mathematics, Second Series **83** (1966), 280–293. Original journal version, including the Addendum. Source loci: Lemma 1, p. 281; Lemma 3, pp. 282–283; Theorem 4, pp. 283–284; Lemma 5, pp. 284–285; Addendum, Theorem 15, pp. 291–293. The free collected-works copy hosted by the Indian Statistical Institute Bangalore is used here.

<https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1960s/1966_Derivations%20of%20Operator%20Algebras.pdf>

**[L25] Jacob Lurie.** *Math 261y: von Neumann Algebras (Lecture 25)*. Harvard course notes dated 30 October 2011, three-page version hosted by the Institute for Advanced Study. Source loci: Theorem 1, Lemma 2, Proposition 3, Lemma 4, Theorem 5, and Propositions 6–7, pp. 1–3. The corrections needed for the trace and fixed-point arguments are specified above.

<https://www.math.ias.edu/~lurie/261ynotes/lecture25.pdf>

**[L26] Jacob Lurie.** *Math 261y: von Neumann Algebras (Lecture 26)*. Harvard course notes dated 1 November 2011, three-page version hosted by the Institute for Advanced Study. Source loci: Theorem 1, Proposition 2 and Lemma 3, including their proofs, pp. 1–3.

<https://www.math.ias.edu/~lurie/261ynotes/lecture26.pdf>

**[ZM67] Georges Zeller-Meier.** *Dérivations et automorphismes des algèbres d’opérateurs*. Séminaire Bourbaki, exposé 324, February 1967; collected publication 1968, pp. 179–188. Original version digitized by Numdam. Source loci: Sections 1–3, in particular Theorem 1 and the opening proof outline in Section 3. No theorem from this survey is used as an unproved input.

<https://www.numdam.org/article/SB_1966-1968__10__179_0.pdf>

**Kadison–Ringrose: bibliographical reference, not a proof input.** Richard V. Kadison and John R. Ringrose, *Derivations and automorphisms of operator algebras*, Communications in Mathematical Physics **4** (1967), 32–63, original journal version, Lemma 1. No result from this paper is invoked without proof here. The required type III averaging assertion is proved in Step 9 above.

<https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-4/issue-1/Derivations-and-automorphisms-of-operator-algebras/cmp/1103839770.pdf>

<https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1960s/1967_DerivationsAndAutomorphismsOfOperatorAlgebras.pdf>

**Attached lesson sources.** The nine lesson titles and exact result numbers used directly are listed under **Results used**. The accompanying lesson *Kaplansky's density theorem and its consequences* supplies background to the enveloping-algebra and topology lessons; no additional result from it is invoked directly in this proof.

## Proof and checking scope

The thirteen-step argument and its declared immediate programme inputs have been checked at the scopes recorded with this edition. This is a coordinator self-check, not independent review, human review or formal verification. The original received proof is preserved separately; the elementary closedness and compactness arguments and navigable dependency bindings are additions to this edition.
