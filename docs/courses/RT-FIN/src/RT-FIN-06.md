# Induced representations and Frobenius reciprocity

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

A representation of a subgroup describes some of a group's symmetries. Induction extends that information to a representation of the whole group by adding one copy of the original vector space for each coset. Frobenius reciprocity explains exactly how the resulting representation interacts with restriction. Its two morphism-level formulas are useful for different directions of a map.

We work over \(\mathbb C\), with finite groups and finite-dimensional representations. The prerequisite is [Characters and the orthogonality relations](RT-FIN-02.md), particularly Theorem 3.1 for character multiplicities and determination. Complete reducibility and Schur's lemma are Theorems 2.3 and 3.1 in [Representations and complete reducibility](RT-FIN-01.md). All modules are left modules. We use the class-function inner product linear in the first variable.

## 1. One copy for each coset

Let \(H\le G\) and let \(W\) be an \(H\)-representation. Restriction \(\operatorname{Res}_H^G V\) retains the vector space and forgets the action of elements outside \(H\). Define induction by the balanced tensor product

\[
\operatorname{Ind}_H^G W
=\mathbb C[G]\otimes_{\mathbb C[H]}W.
\tag{1}
\]

The balancing relation is \(gh\otimes w=g\otimes hw\), for \(g\in G,h\in H\). The \(G\)-action is left multiplication on the first factor:

\[
a(g\otimes w)=ag\otimes w.
\]

This respects balancing and satisfies the representation law.

Choose a set \(T\) of representatives of the **left cosets** \(G/H\). Every group element has a unique expression \(th\), with \(t\in T,h\in H\). Thus, as a right \(\mathbb C[H]\)-module,

\[
\mathbb C[G]=\bigoplus_{t\in T}t\mathbb C[H],
\qquad
\operatorname{Ind}_H^G W=\bigoplus_{t\in T}(t\otimes W).
\tag{2}
\]

One can verify the second equality directly: expand a group-algebra element in its unique \(th\) expressions and move each \(h\) onto \(W\). The inverse maps the tuple \((w_t)\) to \(\sum_t t\otimes w_t\). In particular,

\[
\dim\operatorname{Ind}_H^G W=[G:H]\dim W.
\tag{3}
\]

For \(a\in G\), write \(at=t'h\), uniquely. Then

\[
a(t\otimes w)=t'\otimes hw.
\tag{4}
\]

This explicit rule constructs matrices in a coset basis.

If \(W\) is trivial and one-dimensional, the basis in (2) is indexed by \(G/H\), and (4) is the coset permutation action. Therefore \(\operatorname{Ind}_H^G\mathbf1\simeq\mathbb C[G/H]\). For \(H=1\), this is the left regular representation.

## 2. The function model and the same character formula

Consider

\[
\mathcal F_H^G(W)=
\{f:G\longrightarrow W\mid f(hx)=h f(x)\text{ for }h\in H,x\in G\}.
\tag{5}
\]

Use right translation:

\[
(a f)(x)=f(xa).
\tag{6}
\]

It preserves the covariance condition. Also \(a(bf)(x)=f(xab)=((ab)f)(x)\), so (6) is a left representation. The functions are determined by their values at the representatives \(t^{-1}\) of the right cosets \(H\backslash G\), again giving (3).

**Proposition 2.1 (the two models).** The following map is a natural \(G\)-isomorphism:

\[
\begin{aligned}
\Psi:\mathbb C[G]\otimes_{\mathbb C[H]}W&\longrightarrow\mathcal F_H^G(W),\\
\Psi(g\otimes w)(x)&=
\begin{cases}(xg)w&xg\in H,\\0&xg\notin H.\end{cases}
\end{aligned}
\tag{7}
\]

If \(\psi=\chi_W\), the character of either model is

\[
(\operatorname{Ind}_H^G\psi)(a)
=\sum_{\substack{t\in T\\t^{-1}at\in H}}\psi(t^{-1}at)
=\frac1{|H|}\sum_{\substack{x\in G\\x^{-1}ax\in H}}\psi(x^{-1}ax).
\tag{8}
\]

**Proof.** The function in (7) satisfies (5), since replacing \(x\) by \(hx\) multiplies its value by \(h\). Moreover,

\[
\Psi(gh\otimes w)=\Psi(g\otimes hw),
\qquad a\Psi(g\otimes w)=\Psi(ag\otimes w),
\]

as is seen by substitution in (7). Hence \(\Psi\) is well-defined and equivariant.

In (2), the image of \(t\otimes w\) is supported on \(Ht^{-1}\), and has value \(w\) at \(t^{-1}\). These disjoint supports give an explicit inverse:

\[
f\longmapsto\sum_{t\in T}t\otimes f(t^{-1}).
\tag{9}
\]

Indeed the covariance condition determines the function on each support from that one value. Formula (7) commutes with every \(H\)-equivariant map \(W\to W'\), which proves naturality.

For the trace, (4) contributes only when the coset \(tH\) is fixed by \(a\), namely when \(t^{-1}at\in H\). On that summand the operator is \(\rho_W(t^{-1}at)\), giving the first sum in (8). The same statement in the function model follows by evaluating at \(t^{-1}\): for a fixed coset, \(t^{-1}a=(t^{-1}at)t^{-1}\), so (5) gives exactly that operator on its value.

To obtain the second sum, write \(x=th\). Then \(x^{-1}ax=h^{-1}(t^{-1}at)h\), and the summand is independent of \(h\) because \(\psi\) is a class function on \(H\). There are \(|H|\) such choices in each qualifying coset. \(\square\)

The formula defines induction of any class function on \(H\), even one that is not a character. For \(H\triangleleft G\), it is zero outside \(H\), and on \(H\) it is the sum of the conjugates of \(\psi\), one for each coset. This follows directly from (8), without assuming an irreducibility criterion.

## 3. Both adjunctions

**Theorem 3.1 (Frobenius reciprocity).** For a \(G\)-module \(V\) and an \(H\)-module \(W\), there are natural isomorphisms

\[
\begin{aligned}
\operatorname{Hom}_G(\operatorname{Ind}_H^G W,V)
&\simeq\operatorname{Hom}_H(W,\operatorname{Res}_H^G V),\\
\operatorname{Hom}_G(V,\operatorname{Ind}_H^G W)
&\simeq\operatorname{Hom}_H(\operatorname{Res}_H^G V,W).
\end{aligned}
\tag{10}
\]

For class functions \(\psi\) on \(H\) and \(\chi\) on \(G\),

\[
\langle\operatorname{Ind}_H^G\psi,\chi\rangle_G
=\langle\psi,\operatorname{Res}_H^G\chi\rangle_H.
\tag{11}
\]

**Proof of the first isomorphism.** Given \(A:\operatorname{Ind}W\to V\), restrict it to the copy at the identity:

\[
u(w)=A(1\otimes w).
\]

Balancing and equivariance give \(u(hw)=A(h\otimes w)=h u(w)\). Conversely, from an \(H\)-map \(u:W\to V\), define

\[
A_u(g\otimes w)=g u(w).
\tag{12}
\]

The expressions for \(gh\otimes w\) and \(g\otimes hw\) coincide because \(u\) is \(H\)-equivariant. The map is \(G\)-equivariant, and every such map is determined by its values on \(1\otimes W\), so the constructions are inverse.

**Proof of the second isomorphism.** Use the function model. Given \(B:V\to\mathcal F_H^G(W)\), set \(v\mapsto B(v)(1)\). For \(h\in H\),

\[
B(hv)(1)=(hB(v))(1)=B(v)(h)=hB(v)(1),
\]

so this is an \(H\)-map. Conversely, from an \(H\)-map \(b:V\to W\), define

\[
B_b(v)(x)=b(xv).
\tag{13}
\]

It satisfies \(B_b(v)(hx)=hB_b(v)(x)\), and

\[
B_b(av)(x)=b(xav)=(aB_b(v))(x).
\]

Thus it defines a \(G\)-map to the function model. Evaluation at \(1\) recovers \(b\). Conversely \(B(xv)=xB(v)\) makes (13) recover every original \(B\). Composing with \(\Psi^{-1}\) gives the second isomorphism for the tensor model.

All formulas commute with precomposition and postcomposition by intertwiners, which proves naturality in both arguments. No chosen inner product is used to identify the two Hom spaces.

**The same adjunctions in the other model.** The first adjunction has the function-model formula

\[
A_u(f)=\sum_{t\in T}t\,u(f(t^{-1})).
\]

Replacing \(t\) by \(th\) changes its summand to \(th\,u(h^{-1}f(t^{-1}))=t\,u(f(t^{-1}))\). Hence it is independent of the coset representatives. If \(at=t'h\), then \(t'^{-1}a=ht^{-1}\), and the summand for \(t'\) in \(A_u(af)\) is \(t'u(hf(t^{-1}))=at\,u(f(t^{-1}))\). This proves equivariance. The function supported on \(H\) with value \(w\) at \(1\) recovers \(u(w)\); its translates give the inverse by the disjoint-support decomposition.

The second adjunction has the tensor-model formula

\[
B_b(v)=\sum_{t\in T}t\otimes b(t^{-1}v).
\]

Changing \(t\) to \(th\) leaves this tensor unchanged by \(H\)-equivariance of \(b\) and balancing. To check \(B_b(av)=aB_b(v)\), again write \(at=t'h\). The term in \(aB_b(v)\) is \(t'\otimes h b(t^{-1}v)=t'\otimes b(t'^{-1}av)\), precisely the corresponding term in \(B_b(av)\). Its inverse extracts the coefficient of \(1\otimes W\) in a coset decomposition with \(1\in T\). Formula (9) identifies these formulas with (12) and (13), so their two inverse and naturality statements agree in both models.

**Proof of the class-function identity.** Insert the second formula in (8) into the left side of (11). For each \(x\in G\), put \(a=xhx^{-1}\). The summation becomes

\[
\frac1{|G||H|}\sum_{x\in G}\sum_{h\in H}
\psi(h)\overline{\chi(xhx^{-1})}
=\frac1{|H|}\sum_{h\in H}\psi(h)\overline{\chi(h)},
\]

since \(\chi\) is a class function. This is the right side. For characters, (11) also follows by taking dimensions in (10) and applying the earlier character-Hom formula. \(\square\)

The first tensor adjunction exists much more generally for extension of scalars. The function adjunction is a right adjunction for coinduction. For finite groups, (7) identifies coinduction and induction; finiteness is what allows all functions here to be reconstructed from finitely many coset copies.

## 4. Induction in stages and tensoring

**Proposition 4.1 (transitivity and projection formula).** For \(H\le K\le G\), and for a \(G\)-module \(V\),

\[
\operatorname{Ind}_K^G(\operatorname{Ind}_H^K W)
\simeq\operatorname{Ind}_H^G W,
\qquad
\operatorname{Ind}_H^G(W\otimes\operatorname{Res}_H^G V)
\simeq(\operatorname{Ind}_H^G W)\otimes V.
\tag{14}
\]

These isomorphisms are natural.

**Proof of transitivity in tensors.** The map and inverse are

\[
g\otimes(k\otimes w)\longmapsto gk\otimes w,
\qquad
g\otimes w\longmapsto g\otimes(1\otimes w).
\tag{15}
\]

Moving an element of \(K\) across the first balancing relation leaves \(gk\) unchanged; moving an element of \(H\) across the second is exactly the final \(H\)-balancing relation. The inverse respects \(H\)-balancing because \(h\otimes w=1\otimes hw\) in \(\operatorname{Ind}_H^K W\). The maps are inverse and commute with left \(G\)-multiplication.

**Proof of transitivity in functions.** If \(F\in\mathcal F_K^G(\mathcal F_H^K(W))\), set \(f(x)=F(x)(1)\). Then \(f(hx)=F(x)(h)=hF(x)(1)\). Its inverse is

\[
F(x)(k)=f(kx)\quad(k\in K).
\tag{16}
\]

The inner \(H\)-covariance and outer \(K\)-covariance follow by direct substitution; for the latter, \(F(k_0x)(k)=f(kk_0x)=(k_0F(x))(k)\). Evaluation at \(1\) and (16) are inverse and commute with right \(G\)-translation.

**Proof of the projection formula in tensors.** Use

\[
g\otimes(w\otimes v)\longmapsto(g\otimes w)\otimes gv,
\tag{17}
\]

with inverse

\[
(g\otimes w)\otimes v\longmapsto
g\otimes(w\otimes g^{-1}v).
\tag{18}
\]

Balancing in (17) follows from
\((gh\otimes w)\otimes ghv=(g\otimes hw)\otimes g(hv)\).
For (18), replacing \(gh\otimes w\) by \(g\otimes hw\) gives the same answer, since moving \(h\) onto the inner tensor changes \(w\otimes h^{-1}g^{-1}v\) to \(hw\otimes g^{-1}v\). The maps are inverse and respect the diagonal \(G\)-action.

**Proof in functions.** Map \(\sum_i f_i\otimes v_i\) to

\[
x\longmapsto\sum_i f_i(x)\otimes xv_i
\in\mathcal F_H^G(W\otimes\operatorname{Res}V).
\tag{19}
\]

Its \(H\)-covariance acts on both factors, and its \(G\)-action is (6), as substitution of \(xa\) shows. Conversely, apply \(1\otimes x^{-1}\) to the value of a function in the target. The result has \(H\)-covariance on the \(W\)-factor only. Expanding its second factor in a fixed basis of \(V\) gives a finite sum of \(W\)-valued covariant functions times basis vectors. This inverts (19); the resulting inverse is independent of the basis because it is characterized by that pointwise formula. Every construction commutes with intertwiners. \(\square\)

## 5. Orbit counting is a character calculation

**Corollary 5.1 (Burnside's orbit-counting formula).** For a finite \(G\)-set \(X\),

\[
|G\backslash X|=\frac1{|G|}\sum_{g\in G}|X^g|.
\tag{20}
\]

**Proof.** The permutation character of \(\mathbb C[X]\) is \(g\mapsto|X^g|\). A fixed vector has equal coefficients at points in the same orbit, and the sums of basis vectors over the separate orbits are a basis of the fixed subspace. Its dimension is therefore \(|G\backslash X|\). Averaging the representation gives the projector onto this subspace, whose trace is the right side of (20). \(\square\)

Taking \(X=G/H\) also shows that \(\operatorname{Ind}_H^G\mathbf1\) contains the trivial representation exactly once. This is the case of (11) with both characters trivial.

## 6. All dihedral irreducibles

Write

\[
D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,
\qquad |D_n|=2n.
\]

For the ordinary polygon interpretation \(n\ge3\); the presentation also gives \(D_1=C_2\) and \(D_2=C_2\times C_2\). Let \(H=\langle r\rangle\), \(\zeta=e^{2\pi i/n}\), and \(\theta_k(r)=\zeta^k\).

In the coset basis \(1\otimes1,s\otimes1\), induction gives

\[
\rho_k(r)=
\begin{pmatrix}\zeta^k&0\\0&\zeta^{-k}\end{pmatrix},
\qquad
\rho_k(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{21}
\]

If \(k\not\equiv-k\pmod n\), the two rotation eigenvalues are distinct. Any invariant line would be one of their eigenlines, but \(s\) exchanges them. Thus the representation is irreducible. Its character is

\[
\chi_k(r^j)=\zeta^{kj}+\zeta^{-kj},
\qquad \chi_k(sr^j)=0.
\tag{22}
\]

Exchanging the two basis vectors identifies \(k\) and \(-k\). Conversely, equivalence of the restrictions to the cyclic subgroup requires the unordered eigenvalue pairs to agree, so these are the only repetitions.

For \(k=0\), \(r=I\) and the two \(s\)-eigenlines give the trivial and reflection-sign representations. If \(n\) is even, \(k=n/2\) gives \(r=-I\) and again two lines with \(s=1,-1\).

Every one-dimensional representation sends \(r\) to a number \(\alpha\) with \(\alpha^n=1\) and \(\alpha=\alpha^{-1}\), and \(s\) to \(\beta=\pm1\). Hence there are two such representations when \(n\) is odd and four when it is even. There are respectively \((n-1)/2\) and \((n-2)/2\) two-dimensional irreducibles, represented by \(1\le k<n/2\). Their degree squares sum to

\[
2+4\frac{n-1}2=2n
\quad\text{or}\quad
4+4\frac{n-2}2=2n.
\]

The regular degree-square identity proves completeness. The formulas include the two small presentations, for which no two-dimensional irreducible occurs.

## 7. Three subgroup routes into \(S_4\)

Use the class order \(1,2,22,3,4\), with sizes \(1,6,3,8,6\).

The point stabilizer \(S_3\) gives the four-point permutation character

\[
\operatorname{Ind}_{S_3}^{S_4}\mathbf1=(4,2,0,1,0).
\]

Removing its trivial line gives \(W\) with character \((3,1,-1,0,-1)\). Its squared norm is \((9+6+3+6)/24=1\), so it is irreducible. Tensoring with sign gives the irreducible \(W\otimes\mathrm{sign}\), with row \((3,-1,-1,0,1)\).

Now \(A_4\triangleleft S_4\), and \(A_4/V_4\simeq C_3\). Choose a nontrivial linear character \(\alpha\) of this quotient. An odd permutation interchanges its two 3-cycle classes and therefore \(\alpha,\overline\alpha\). The normal-subgroup form of (8) gives

\[
\operatorname{Ind}_{A_4}^{S_4}\alpha=(2,0,2,-1,0).
\tag{23}
\]

On a 3-cycle the value is \(\omega+\omega^2=-1\), with \(\omega^3=1,\omega\ne1\); on a double transposition it is \(1+1=2\). The squared norm is \((4+3\cdot4+8)/24=1\), so (23) is an irreducible \(U\). Trivial, sign, \(U,W,W\otimes\mathrm{sign}\) are distinct, and their squared degrees total \(24\), proving completeness.

Finally take the order-eight dihedral subgroup

\[
H=\langle r=(1234),s=(13)\rangle.
\]

Define its linear character \(\eta\) by \(\eta(r)=-1,\eta(s)=1\). The relation \(srs=r^{-1}\) is respected. In \(H\), there are two transpositions \(s,r^2s\), three double transpositions \(r^2,rs,r^3s\), and two 4-cycles \(r,r^3\). For any class element \(g\), (8) can be regrouped as

\[
(\operatorname{Ind}_H^{S_4}\eta)(g)
=\frac{|C_{S_4}(g)|}{8}
\sum_{h\in H\cap g^{S_4}}\eta(h).
\tag{24}
\]

Each element of the intersection has exactly \(|C_{S_4}(g)|\) conjugators. Its five intersection sums are \(1,2,-1,0,-2\); the centralizer orders are \(24,4,8,3,4\). Thus (24) gives \((3,1,-1,0,-1)\), constructing \(W\) by induction from a line. The character \(\eta\,\operatorname{Res}_H\mathrm{sign}\) induces \(W\otimes\mathrm{sign}\) by (14).

Inducing the trivial character of \(H\) gives \((3,1,3,0,1)=\mathbf1+\chi_U\), the permutation action on the three pair partitions. These different subgroup choices produce different useful constituents; induction need not preserve irreducibility.

## 8. Exercises with complete solutions

### Exercise 1. A character of \(C_3\) produces the standard plane

Let \(H=\langle(123)\rangle\le S_3\). Induce a nontrivial linear character of \(H\), and prove irreducibility both from matrices and from its character.

**Solution.** Write \(\theta((123))=\omega\), where \(\omega=e^{2\pi i/3}\). With coset representatives \(1,(12)\), formula (4) gives the matrices

\[
r\longmapsto\operatorname{diag}(\omega,\omega^{-1}),
\qquad s\longmapsto\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

The distinct \(r\)-eigenlines are exchanged by \(s\), so neither is invariant under the whole group. This proves irreducibility. Alternatively, its character has values \(2,0,\omega+\omega^{-1}=-1\) on the identity, transpositions and 3-cycles. Its norm is \((4+3\cdot0+2\cdot1)/6=1\), giving the same conclusion. It is the degree-two standard representation by character determination.

### Exercise 2. The action on the second tensor factor

Prove the projection formula, including a well-defined inverse. Explain why simply leaving the vector in \(V\) unchanged does not define the required map.

**Solution.** Define \(g\otimes(w\otimes v)\mapsto(g\otimes w)\otimes gv\). The balanced expressions \(gh\otimes(w\otimes v)\) and \(g\otimes(hw\otimes hv)\) map respectively to

\[
(gh\otimes w)\otimes ghv
=(g\otimes hw)\otimes ghv
\quad\text{and}\quad
(g\otimes hw)\otimes g(hv),
\]

which coincide. Applying \(a\in G\) changes the output to \((ag\otimes w)\otimes agv\), exactly the diagonal action.

The inverse is \((g\otimes w)\otimes v\mapsto g\otimes(w\otimes g^{-1}v)\). If \(g\) is replaced by \(gh\) and balancing moves \(h\) onto \(w\), its image is unchanged, since

\[
gh\otimes(w\otimes h^{-1}g^{-1}v)
=g\otimes(hw\otimes g^{-1}v).
\]

Both compositions are the identity. If the proposed forward map omitted the factor \(g\) acting on \(v\), the two balanced inputs would generally give second factors \(v\) and \(hv\); these need not agree.

### Exercise 3. The trivial constituent

Show that \(\operatorname{Ind}_H^G\mathbf1\) contains the trivial representation once, and determine when it is irreducible.

**Solution.** Frobenius reciprocity gives

\[
\langle\operatorname{Ind}_H^G\mathbf1,\mathbf1\rangle_G
=\langle\mathbf1,\mathbf1\rangle_H=1.
\]

Equivalently, the transitive coset permutation representation has exactly one fixed line, spanned by the sum of its coset basis vectors. If it is irreducible, the nonzero trivial summand must be the whole representation. Its dimension is then one, whereas (3) makes that dimension \([G:H]\). Hence \(H=G\). Conversely \(H=G\) gives the one-dimensional trivial representation, which is irreducible.

### Exercise 4. The precise Gelfand-pair criterion

Let \(\mathcal H(G,H)\) be the complex functions on \(G\) constant on the double cosets \(HgH\), with convolution \((f*k)(g)=\sum_x f(x)k(x^{-1}g)\). Prove that this algebra is commutative exactly when every irreducible has multiplicity **zero or one** in \(\mathbb C[G/H]\). Explain why requiring every irreducible to occur would be stronger and would spoil the equivalence.

**Solution.** Identify functions with their group-algebra coefficient sums, and put

\[
e_H=\frac1{|H|}\sum_{h\in H}h.
\]

Then \(e_H^2=e_H\). Left and right multiplication by each \(h\in H\) fixes an element exactly when its coefficients are left and right \(H\)-invariant. Hence

\[
\mathcal H(G,H)=e_H\mathbb C[G]e_H
\tag{25}
\]

as convolution algebras, with unit \(e_H\). The indicators of the double cosets form a basis.

The map \(g\otimes1\mapsto ge_H\) identifies \(\mathbb C[G/H]\) with the left ideal \(\mathbb C[G]e_H\): it respects \(gh\otimes1=g\otimes1\), and disjoint coset supports prove that it is a basis isomorphism.

Every \(G\)-endomorphism \(T\) of that ideal is determined by \(b=T(e_H)\). Since \(T(e_H)=T(e_H^2)=e_HT(e_H)\), we have \(b\in e_H\mathbb C[G]e_H\), and \(T(ae_H)=ab\). Conversely right multiplication \(R_b\) by such a \(b\) is a \(G\)-endomorphism. Composition satisfies

\[
R_bR_c=R_{cb}.
\]

Thus the endomorphism algebra is the **opposite** of the corner algebra (25). An algebra and its opposite are commutative in exactly the same cases.

By complete reducibility, write \(\mathbb C[G/H]\simeq\bigoplus_i V_i^{\oplus m_i}\). Schur's lemma gives

\[
\operatorname{End}_G(\mathbb C[G/H])
\simeq\bigoplus_{i:m_i>0}M_{m_i}(\mathbb C).
\tag{26}
\]

To see the matrix factors, each map between two copies of \(V_i\) is a scalar, and maps between inequivalent types are zero; composing the scalar arrays is matrix multiplication. A matrix algebra is commutative exactly when its size is one: for size at least two, the two matrix units \(E_{12},E_{21}\) do not commute. Therefore (26) is commutative exactly when every \(m_i\) is zero or one. Reciprocity also identifies \(m_i=\dim V_i^H\).

For the stronger wording, take a nontrivial group and \(H=G\). Its Hecke algebra is one-dimensional and commutative, while its coset representation contains only the trivial irreducible. Thus commutativity does not require all irreducibles to occur. A pair satisfying the proved multiplicity condition is called a **Gelfand pair**. The pairs \((S_4,S_3)\) and \((S_4,D_4)\) above are examples, because their permutation representations are respectively \(\mathbf1+W\) and \(\mathbf1+U\).

## 9. What this lesson assumes

All induction constructions, the model isomorphism, both adjunctions, both forms of transitivity and the projection formula, orbit counting, the dihedral classification and the Hecke criterion were proved here. We use the earlier lessons' precise complete-reducibility, Schur and character results identified in the opening paragraph. Tensor-product traces, proved in Proposition 1.1 of [Tensor products, duals and real representations](RT-FIN-04.md), justify character twists. The class sizes and \(A_4\) linear characters used in the \(S_4\) example are constructed in the earlier character lessons.

Elementary tensor products are understood through their linearity and balancing relations. Coset partition and counting are proved in [the Fourier lesson, Lemma 6.1](RT-FIN-03.md#lemma-6-1). No Mackey irreducibility or Clifford theorem was used to classify the dihedral representations; those more general results are the next topic.

## References

- **C. Gruson and V. Serganova**, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, 2018, Chapter 2 §5, Theorem 5.3 and Lemma 5.4, for the tensor adjunction; §6, Lemmas 6.1–6.3, Corollaries 6.4–6.5 and Theorem 6.7, for induction and characters; §9, Proposition 9.5, for the multiplicity-free Hecke criterion.
- **F. G. Frobenius**, *Über Relationen zwischen den Charakteren einer Gruppe und denen ihrer Untergruppen*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin (1898), pp. 501–515, reprinted as paper 57 in *Gesammelte Abhandlungen*. Its restriction multiplicities and corresponding subgroup character relations are the historical setting of reciprocity.
