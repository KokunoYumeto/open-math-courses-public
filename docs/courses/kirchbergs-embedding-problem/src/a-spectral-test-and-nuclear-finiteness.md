# A spectral test and nuclear finiteness

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\Gamma\) be a group with property (T) and \(S\) a finite generating set. To a tuple \((z_s)_{s\in S}\) of unitaries in a C\*-algebra and a finite-dimensional representation \(\pi\) of \(\Gamma\) this lesson attaches a number \(d(\mathbf z,\pi)\ge0\). If the unitaries come from a representation \(\varrho\) of \(\Gamma\), the number is \(0\) when \(\pi\) occurs in \(\varrho\) and at least a fixed \(\kappa>0\) otherwise. The number is defined for every tuple of unitaries, also when the tuple satisfies none of the relations of the group. The main result is a finiteness statement: for a tuple of unitaries in a *nuclear* C\*-algebra, only finitely many irreducible representations \(\pi\) have \(d(\mathbf z,\pi)\) below a fixed threshold. In the next lesson this is applied to the coordinates of a representation in an ultrapower, which satisfy the relations of the group only approximately.

- The Laplacian of a tuple of unitaries and the spectral gap (Lemma 1.2).
- Conjugate representations, invariant vectors and intertwiners (Section 2).
- The matching number \(d(\mathbf z,\pi)\) (Section 3).
- The square-root trace inequality (Lemma 4.1).
- A bound that is uniform in the first tensor factor (Lemma 5.1).
- Tensor norms, nuclearity and sequence algebras (Sections 6 and 7).
- Nuclear finiteness (Proposition 8.1).

The lesson follows [OpenAI-K, Sections 3 and 4]. It uses the facts (C1) to (C6), the ultraproduct lemmas, the group \(\Gamma\), the hypothesis (T) and Lemma 6.1 of [Norm ultrapowers and a group with property (T)](norm-ultrapowers-and-a-group-with-property-t.md). From the course *Foundations of von Neumann algebras* it uses Hilbert tensor products and compact operators ([Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators)) and trace-class and Hilbert–Schmidt operators ([Compact and trace-class operators, the predual of B(H), and the operator topologies](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies)). From the course *Positive maps and finite-dimensional approximation* it uses the two tensor norms ([Tensor positivity and nuclearity](course:OA-APPROX/tensor-positivity-nuclearity)).

Throughout, \(\Gamma\), \(S\), \(\kappa\) and \(R=4|S|\) are as in Lemma 6.1 of the first lesson: for every unitary representation \(\sigma\) of \(\Gamma\) without nonzero invariant vectors, \(\sum_{s\in S}\|\sigma(s)\xi-\xi\|^2\ge\kappa\|\xi\|^2\). This rests on the hypothesis (T).

## 1. The Laplacian of a tuple of unitaries

**Definition.** For a family \(\mathbf z=(z_s)_{s\in S}\) of unitaries in a unital C\*-algebra \(C\) let
\[
L(\mathbf z)=\sum_{s\in S}(z_s-1)^*(z_s-1) .
\]

Each term is \(2-z_s-z_s^*\), which lies between \(0\) and \(4\). So \(0\le L(\mathbf z)\le R\cdot1\). If \(C\) acts on a Hilbert space \(H\), then
\[
\langle L(\mathbf z)\xi,\xi\rangle=\sum_{s\in S}\|z_s\xi-\xi\|^2\qquad(\xi\in H) .
\]
A unital \(*\)-homomorphism \(\Psi\) maps \(L(\mathbf z)\) to \(L(\Psi(\mathbf z))\), where \(\Psi(\mathbf z)=(\Psi(z_s))_s\).

**Lemma 1.1.** Let \(P\) be a self-adjoint operator on a Hilbert space \(H\ne\{0\}\) with \(0\le P\le R\cdot1\). Then
\[
\min\operatorname{spec}P=\inf\{\langle P\xi,\xi\rangle:\ \|\xi\|=1\} .
\]

**Proof.** The norm of the positive operator \(R-P\) is the supremum of \(\langle(R-P)\xi,\xi\rangle\) over the unit vectors, that is, \(R\) minus the infimum on the right. By the formula for the spectral minimum, \(\min\operatorname{spec}P=R-\|R-P\|\). \(\blacksquare\)

**Lemma 1.2** (spectral gap). Assume (T). Let \(\sigma\) be a homomorphism from \(\Gamma\) into the unitary group of a unital C\*-algebra \(C\), and \(\mathbf z=(\sigma(s))_{s\in S}\). Then
\[
\operatorname{spec}L(\mathbf z)\subseteq\{0\}\cup[\kappa,R] .
\]
If \(C=\mathcal B(H)\), then \(0\) lies in the spectrum exactly if \(\sigma\) has a nonzero invariant vector.

**Proof.** By (C5) and (C2) we may assume \(C\subseteq\mathcal B(H)\) with the same unit. Let \(H_0\) be the closed subspace of the invariant vectors of \(\sigma\). It is invariant under all \(\sigma(g)\), and so is its orthogonal complement \(H_1\), because the \(\sigma(g)\) are unitary. On \(H_0\) the operator \(L(\mathbf z)\) is \(0\). The representation on \(H_1\) has no nonzero invariant vector, so \(\langle L(\mathbf z)\xi,\xi\rangle\ge\kappa\|\xi\|^2\) for \(\xi\in H_1\). So \(L(\mathbf z)\) is the direct sum of \(0\) on \(H_0\) and an operator on \(H_1\) with spectrum in \([\kappa,R]\), by Lemma 1.1. \(\blacksquare\)

## 2. Conjugate representations and intertwiners

A unitary representation of \(\Gamma\) of finite dimension \(d\ge1\) is, after the choice of an orthonormal basis, a homomorphism \(\pi\) from \(\Gamma\) into the unitary \(d\times d\) matrices. Its *conjugate* \(\bar\pi\) is the representation whose matrices have the complex conjugate entries: \(\bar\pi(g)_{kl}=\overline{\pi(g)_{kl}}\). The conjugate of \(\bar\pi\) is \(\pi\); \(\bar\pi\) is irreducible exactly if \(\pi\) is; and \(\bar\pi\simeq\bar\pi'\) exactly if \(\pi\simeq\pi'\).

Let \(C\) be a unital C\*-algebra, \(z\in C\) a unitary and \(W\) a unitary \(d\times d\) matrix. We write \(z\otimes W\) for the matrix \((W_{kl}\,z)_{k,l}\) in \(M_d(C)\); it is unitary. If \(C\) acts on \(H\), then \(M_d(C)\) acts on \(H^d\), and for \(\xi=(\xi_1,\dots,\xi_d)\in H^d\)
\[
\bigl((z\otimes W)\xi\bigr)_k=\sum_lW_{kl}\,z\,\xi_l .
\]
For \(\xi\in H^d\) let \(T_\xi\) be the linear map from \(\mathbb C^d\) to \(H\) that sends the unit vector \(e_l\) to \(\xi_l\).

**Lemma 2.1.** Let \(U\) be a unitary operator on \(H\), \(W\) a unitary \(d\times d\) matrix and \(\xi\in H^d\). Then
\[
T_{(U\otimes\bar W)\xi}=U\,T_\xi\,W^* .
\]
Consequently, for a unitary representation \(\varrho\) of \(\Gamma\) on \(H\) and a representation \(\pi\) of dimension \(d\): the vector \(\xi\) is invariant under all \(\varrho(g)\otimes\bar\pi(g)\) exactly if \(\varrho(g)T_\xi=T_\xi\pi(g)\) for all \(g\in\Gamma\).

**Proof.** \(W^*e_k=\sum_l\overline{W_{kl}}\,e_l\), so \(UT_\xi W^*e_k=\sum_l\overline{W_{kl}}\,U\xi_l\), which is the \(k\)-th entry of \((U\otimes\bar W)\xi\). For the consequence, \(\xi\) is invariant exactly if \(\varrho(g)T_\xi\pi(g)^*=T_\xi\) for all \(g\). \(\blacksquare\)

A linear map \(T\) from \(\mathbb C^d\) to \(H\) with \(\varrho(g)T=T\pi(g)\) for all \(g\) is an *intertwiner* from \(\pi\) to \(\varrho\). We write \(\pi\prec\varrho\) if there is an intertwiner from \(\pi\) to \(\varrho\) that is an isometry; then \(\varrho\), restricted to the range of the isometry, is equivalent to \(\pi\). We say that \(\pi\) *occurs in* \(\varrho\).

**Lemma 2.2** (Schur). Let \(\pi\) be irreducible and \(T\ne0\) an intertwiner from \(\pi\) to a unitary representation \(\varrho\). Then \(T^*T=c\cdot1\) with a number \(c>0\), and \(c^{-1/2}T\) is an isometric intertwiner. So \(\pi\prec\varrho\). If \(\varrho\) is irreducible of finite dimension, then \(\pi\simeq\varrho\).

**Proof.** Taking adjoints in \(\varrho(g^{-1})T=T\pi(g^{-1})\) gives \(T^*\varrho(g)=\pi(g)T^*\). So \(T^*T\) commutes with all \(\pi(g)\). It is a self-adjoint matrix; each of its eigenspaces is invariant under \(\pi\), so there is only one eigenvalue \(c\), and \(c>0\) because \(T\ne0\). The range of the isometry is a nonzero invariant subspace for \(\varrho\); if \(\varrho\) is irreducible, it is the whole space, and the isometry is a unitary. \(\blacksquare\)

**Lemma 2.3.** Let \(\varrho\) be a unitary representation of \(\Gamma\) on \(H\) and \(\pi\) an irreducible representation of dimension \(d\). The representation \(g\mapsto\varrho(g)\otimes\bar\pi(g)\) on \(H^d\) has a nonzero invariant vector exactly if \(\pi\prec\varrho\).

**Proof.** Lemmas 2.1 and 2.2; \(\xi\ne0\) exactly if \(T_\xi\ne0\). \(\blacksquare\)

## 3. The matching number

**Definition.** Let \(\mathbf z=(z_s)_{s\in S}\) be unitaries in a unital C\*-algebra \(C\) and \(\pi\) a unitary representation of \(\Gamma\) of dimension \(d\). Put
\[
d(\mathbf z,\pi)=\min\operatorname{spec}L\bigl((z_s\otimes\bar\pi(s))_{s\in S}\bigr) ,
\]
the spectrum taken in \(M_d(C)\).

No relation between the \(z_s\) is required. The number lies in \([0,R]\).

**Lemma 3.1.** 1. If \(C\) acts faithfully and with its unit on \(H\), then \(d(\mathbf z,\pi)\) is the infimum of \(\sum_{s\in S}\|(z_s\otimes\bar\pi(s))\xi-\xi\|^2\) over the unit vectors \(\xi\in H^d\).

2. If \(\pi\simeq\pi'\), then \(d(\mathbf z,\pi)=d(\mathbf z,\pi')\).

3. \(d(\mathbf z,\pi_1\oplus\dots\oplus\pi_r)=\min_id(\mathbf z,\pi_i)\).

4. If \(\Psi\) is a unital embedding of \(C\) into another unital C\*-algebra, then \(d(\Psi(\mathbf z),\pi)=d(\mathbf z,\pi)\).

**Proof.** Part 1 is Lemma 1.1 together with (C2). For part 2 let \(\pi'=w\pi w^*\) with a unitary matrix \(w\); then \(\bar\pi'=\bar w\bar\pi\bar w^*\), and the two Laplacians are conjugate by the unitary \(1\otimes\bar w\) of \(M_d(C)\). For part 3 the Laplacian is a block diagonal matrix with the Laplacians for the \(\pi_i\) as blocks, and its spectrum is the union of the spectra of the blocks. Part 4 follows from (C2) and (C6). \(\blacksquare\)

**Lemma 3.2.** Assume (T). Let \(\varrho\) be a unitary representation of \(\Gamma\) on \(H\), \(\mathbf z=(\varrho(s))_{s\in S}\) in \(\mathcal B(H)\), and \(\pi\) irreducible. If \(\pi\prec\varrho\), then \(d(\mathbf z,\pi)=0\). Otherwise \(d(\mathbf z,\pi)\ge\kappa\).

**Proof.** Apply Lemma 1.2 to the representation \(g\mapsto\varrho(g)\otimes\bar\pi(g)\) on \(H^d\), and Lemma 2.3. \(\blacksquare\)

So for representations the number \(d\) tests whether \(\pi\) occurs, with a gap. Fix from here on the two constants
\[
b=\frac{\kappa^2}{4|S|},\qquad0<a<b .
\]
Since \(\kappa\le4|S|\), we have \(b\le\kappa\), so \(a<\kappa\) too.

## 4. The square-root trace inequality

Let \(K\) be a Hilbert space. We use the following facts on the trace class \(\mathcal L^1(K)\), with the norm \(\|\cdot\|_1\) and the trace \(\operatorname{Tr}\), and on the Hilbert–Schmidt operators \(\mathcal L^2(K)\), a Hilbert space with the inner product \(\langle x,y\rangle_2=\operatorname{Tr}(y^*x)\) and the norm \(\|\cdot\|_2\). They are proved in the lesson on compact and trace-class operators named at the beginning (Theorem 4.6, Proposition 4.9 and Theorems 5.2 and 5.4 there).

- (H1) If \(x,y\in\mathcal L^2(K)\), then \(xy\in\mathcal L^1(K)\), \(\|xy\|_1\le\|x\|_2\|y\|_2\) and \(\operatorname{Tr}(xy)=\operatorname{Tr}(yx)\). An operator \(x\) is Hilbert–Schmidt exactly if \(x^*x\) is of trace class, and then \(\|x\|_2^2=\operatorname{Tr}(x^*x)\).
- (H2) If \(t\in\mathcal L^1(K)\) and \(c\in\mathcal B(K)\), then \(ct\) and \(tc\) are of trace class, \(\operatorname{Tr}(ct)=\operatorname{Tr}(tc)\), and \(\|t\|_1\) is the supremum of \(|\operatorname{Tr}(ct)|\) over the \(c\) with \(\|c\|\le1\).
- (H3) If \(x,y\) are positive Hilbert–Schmidt operators, then \(\operatorname{Tr}(xy)\ge0\). Indeed \(x\) is compact and positive, so there is an orthonormal basis of eigenvectors \(\varepsilon_i\) with eigenvalues \(\lambda_i\ge0\), and \(\operatorname{Tr}(xy)=\operatorname{Tr}(yx)=\sum_i\lambda_i\langle y\varepsilon_i,\varepsilon_i\rangle\).

**Lemma 4.1** (Powers and Størmer). For positive Hilbert–Schmidt operators \(X,Y\) on \(K\),
\[
\|X-Y\|_2^2\le\|X^2-Y^2\|_1 .
\]

**Proof.** Let \(F=X-Y\). It is self-adjoint and compact, so \(K\) has an orthonormal basis of eigenvectors of \(F\). Let \(F_+\) and \(F_-\) be the positive and the negative part of \(F\): \(F=F_+-F_-\), \(F_+F_-=0\), both positive and Hilbert–Schmidt. Let \(J\) be the operator that is \(1\), \(-1\), \(0\) on the eigenvectors with positive, negative, zero eigenvalue. Then \(\|J\|\le1\) and \(JF=FJ=|F|\), where \(|F|=F_++F_-\).

First, \(X^2-Y^2=FX+YF\). By (H2), then (H2) and (H1),
\[
\begin{aligned}
\|X^2-Y^2\|_1&\ge\operatorname{Tr}\bigl(J(FX+YF)\bigr)\\
&=\operatorname{Tr}(|F|X)+\operatorname{Tr}(Y|F|)\\
&=\operatorname{Tr}\bigl(|F|(X+Y)\bigr) .
\end{aligned}
\]
Now \(X+Y=F+2Y\) and \(X+Y=-F+2X\). With \(F_+F=F_+^2\), \(F_-F=-F_-^2\) and (H3),
\[
\begin{aligned}
&\operatorname{Tr}\bigl(F_+(X+Y)\bigr)\\
&\quad=\operatorname{Tr}(F_+^2)+2\operatorname{Tr}(F_+Y)\ge\operatorname{Tr}(F_+^2),\\
&\operatorname{Tr}\bigl(F_-(X+Y)\bigr)\\
&\quad=\operatorname{Tr}(F_-^2)+2\operatorname{Tr}(F_-X)\ge\operatorname{Tr}(F_-^2) .
\end{aligned}
\]
The sum of the right sides is \(\operatorname{Tr}(F^2)=\|F\|_2^2\). \(\blacksquare\)

## 5. A bound that is uniform in the first factor

Let \(E\) and \(K\) be Hilbert spaces and \(E\otimes K\) their Hilbert tensor product. For unitaries \(U\) on \(E\) and \(V\) on \(K\), \(U\otimes V\) is the unitary on \(E\otimes K\) with \((U\otimes V)(e\otimes v)=Ue\otimes Vv\).

**Lemma 5.1** (uniform bound). Assume (T). Let \(\sigma\) be a unitary representation of \(\Gamma\) on \(K\) that has no nonzero invariant subspace of finite dimension. Then for every Hilbert space \(E\) and all unitaries \((U_s)_{s\in S}\) on \(E\),
\[
L\bigl((U_s\otimes\sigma(s))_{s\in S}\bigr)\ge b\cdot1 .
\]
No relation between the \(U_s\) is required.

**Proof.** *The conjugation representation.* For \(g\in\Gamma\) and \(A\in\mathcal L^2(K)\) let \(c(g)A=\sigma(g)A\sigma(g)^*\). This is a unitary representation of \(\Gamma\) on the Hilbert space \(\mathcal L^2(K)\). It has no nonzero invariant vector: if \(A\ne0\) commutes with all \(\sigma(g)\), so does the nonzero positive compact operator \(A^*A\); the eigenspace of a positive eigenvalue of \(A^*A\) is nonzero, of finite dimension and invariant under \(\sigma\). So by Lemma 6.1 of the first lesson, for all \(A\in\mathcal L^2(K)\),
\[
\sum_{s\in S}\|\sigma(s)A\sigma(s)^*-A\|_2^2\ge\kappa\,\|A\|_2^2 .
\]

*The density operator.* Let \(\xi\) be a unit vector of \(E\otimes K\). With an orthonormal basis \((e_i)\) of \(E\), write \(\xi=\sum_ie_i\otimes v_i\) with \(v_i\in K\) and \(\sum_i\|v_i\|^2=1\). Let \(T\) be the operator \(T w=\sum_i\langle w,v_i\rangle v_i\) on \(K\). It is positive and of trace class with \(\operatorname{Tr}T=1\), and for all \(C\in\mathcal B(K)\)
\[
\begin{aligned}
\operatorname{Tr}(TC)&=\sum_i\langle Cv_i,v_i\rangle\\
&=\langle(1\otimes C)\xi,\xi\rangle .
\end{aligned}
\]
By (H2) this identity determines \(T\). For unitaries \(U\) on \(E\) and \(V\) on \(K\), the vector \(\xi'=(U\otimes V)\xi\) has the density operator \(VTV^*\), because
\[
\begin{aligned}
&\langle(1\otimes C)\xi',\xi'\rangle\\
&\qquad=\langle(1\otimes V^*CV)\xi,\xi\rangle\\
&\qquad=\operatorname{Tr}(TV^*CV)=\operatorname{Tr}(VTV^*C) .
\end{aligned}
\]

*The estimate.* For \(s\in S\) let \(\xi_s=(U_s\otimes\sigma(s))\xi\) and \(\delta_s=\|\xi_s-\xi\|\), and let \(T_s=\sigma(s)T\sigma(s)^*\) be the density operator of \(\xi_s\). For \(\|C\|\le1\) the numbers \(\langle(1\otimes C)\xi_s,\xi_s\rangle\) and \(\langle(1\otimes C)\xi,\xi\rangle\) differ by at most \(2\delta_s\), and they are \(\operatorname{Tr}(T_sC)\) and \(\operatorname{Tr}(TC)\). So \(\|T_s-T\|_1\le2\delta_s\) by (H2). The operator \(A=T^{1/2}\) is positive and Hilbert–Schmidt with \(\|A\|_2^2=\operatorname{Tr}T=1\), and \(T_s^{1/2}=\sigma(s)A\sigma(s)^*\). By Lemma 4.1,
\[
\|\sigma(s)A\sigma(s)^*-A\|_2^2\le\|T_s-T\|_1\le2\,\delta_s .
\]
Summing over \(s\) and using the first step and the Cauchy–Schwarz inequality,
\[
\kappa\le2\sum_{s\in S}\delta_s\le2\sqrt{|S|}\,\Bigl(\sum_{s\in S}\delta_s^2\Bigr)^{1/2} .
\]
So \(\sum_s\delta_s^2\ge\kappa^2/(4|S|)=b\). The left side is \(\langle L\xi,\xi\rangle\) for the operator \(L\) of the lemma. \(\blacksquare\)

The point of the lemma: the density operator forgets the first factor. Whatever the unitaries \(U_s\) do, the density operator of the moved vector is the conjugate of the old one by \(\sigma(s)\). The square root turns the density operator into a vector for the conjugation representation, and the inequality of Powers and Størmer controls the change of the square root.

The condition on \(\sigma\) is necessary (Exercise 9.4).

## 6. Tensor norms and nuclearity

Let \(B\) and \(Q\) be unital C\*-algebras. We use the following facts, which are established in the lesson on tensor positivity and nuclearity named at the beginning (sections TN03 and TN04 there).

- (N1) Let \(B\) act faithfully with its unit on \(E\), and \(Q\) on \(K\). The closed linear span of the operators \(x\otimes y\), \(x\in B\), \(y\in Q\), on \(E\otimes K\) is a unital C\*-algebra, the *minimal tensor product* \(B\otimes_{\min}Q\). Up to a \(*\)-isomorphism that respects the elements \(x\otimes y\), it does not depend on the two representations.
- (N2) There is a unital C\*-algebra \(B\otimes_{\max}Q\), the *maximal tensor product*, spanned densely by elements \(x\otimes y\) that are bilinear in \((x,y)\) and satisfy \((x\otimes y)(x'\otimes y')=xx'\otimes yy'\) and \((x\otimes y)^*=x^*\otimes y^*\), with the following property. If \(\alpha\) and \(\beta\) are unital \(*\)-homomorphisms from \(B\) and from \(Q\) into a unital C\*-algebra \(C\) such that \(\alpha(x)\beta(y)=\beta(y)\alpha(x)\) for all \(x,y\), there is exactly one unital \(*\)-homomorphism \(\Psi\) from \(B\otimes_{\max}Q\) to \(C\) with \(\Psi(x\otimes y)=\alpha(x)\beta(y)\).
- (N3) There is a surjective unital \(*\)-homomorphism from \(B\otimes_{\max}Q\) onto \(B\otimes_{\min}Q\) that maps \(x\otimes y\) to \(x\otimes y\).

**Definition.** The C\*-algebra \(B\) is *nuclear* if for every C\*-algebra \(Q\) the \(*\)-homomorphism of (N3) is injective, so that it is a \(*\)-isomorphism.

In (N2) the lesson named above works with commuting representations on one Hilbert space; apply it in a faithful unital representation of \(C\). Matrix algebras and commutative C\*-algebras are nuclear (Theorem 5.1 there, on algebras of type I). For \(Q=M_d(\mathbb C)\) both tensor products are \(M_d(B)\), with \(x\otimes y\) the matrix \((y_{kl}\,x)_{k,l}\).

## 7. Sequence algebras

Let \(C_1,C_2,\dots\) be unital C\*-algebras. In the product \(\prod_jC_j\) of the bounded sequences let \(\bigoplus_jC_j\) be the set of the sequences \((c_j)\) with \(\|c_j\|\to0\) in the ordinary sense. It is a closed two-sided ideal, and the quotient
\[
\prod_jC_j\Big/\bigoplus_jC_j
\]
is a unital C\*-algebra. No ultrafilter is involved here.

**Lemma 7.1.** 1. \(\|[(c_j)]\|=\limsup_j\|c_j\|\).

2. If \(P_j\in C_j\) are self-adjoint and uniformly bounded, and \(P_j\ge m\cdot1\) for all but finitely many \(j\), then \([(P_j)]\ge m\cdot1\).

3. If \(0\le P_j\le R\cdot1\) for all \(j\) and \(f\) is a continuous function on \([0,R]\), then \(f([(P_j)])=[(f(P_j))]\).

4. For \(d\ge1\), the algebra of the \(d\times d\) matrices over \(\prod_jC_j/\bigoplus_jC_j\) is \(\prod_jM_d(C_j)/\bigoplus_jM_d(C_j)\), entry by entry.

**Proof.** Part 1 is proved like Lemma 2.2 of the first lesson: changing finitely many coordinates does not change the class. For part 2 change the finitely many exceptional \(P_j\) to \(m\cdot1\); then every \(P_j-m\) is of the form \(y_j^*y_j\) with bounded \(y_j\), so the class is positive. For part 3: the functional calculus in the product is taken in each coordinate, because the coordinate maps are unital \(*\)-homomorphisms (C1); and the quotient map is a unital \(*\)-homomorphism. Part 4 is proved like Lemma 2.5 of the first lesson. \(\blacksquare\)

## 8. Nuclear finiteness

**Proposition 8.1** (nuclear finiteness; [OpenAI-K, Section 4]). Assume (T). Let \(B\) be a nuclear unital C\*-algebra and \(\mathbf u=(u_s)_{s\in S}\) unitaries in \(B\). Then only finitely many equivalence classes of irreducible unitary representations \(\pi\) of \(\Gamma\) of finite dimension satisfy \(d(\mathbf u,\pi)<a\).

The set of these classes is written \(D(\mathbf u)\). No relation between the \(u_s\) is assumed.

**Proof.** Suppose \(\pi_1,\pi_2,\dots\) are irreducible, pairwise inequivalent, with \(d(\mathbf u,\pi_j)<a\) for all \(j\). Let \(d_j\) be the dimension of \(\pi_j\) and \(M_j=M_{d_j}(\mathbb C)\).

*Step 1: a representation in a sequence algebra.* Let
\[
\begin{gathered}
Q=\prod_jM_j\Big/\bigoplus_jM_j,\\
q(g)=[(\bar\pi_j(g))_j]\qquad(g\in\Gamma) .
\end{gathered}
\]
Then \(q\) is a homomorphism from \(\Gamma\) into the unitary group of \(Q\). Choose a faithful unital representation \(\eta\) of \(Q\) on a Hilbert space \(K\), and let \(\sigma=\eta\circ q\), a unitary representation of \(\Gamma\) on \(K\).

*Step 2: \(\sigma\) has no nonzero invariant subspace of finite dimension.* Such a subspace would contain an irreducible one. So let \(\tau\) be an irreducible representation of dimension \(m\) and suppose \(\tau\prec\sigma\). By Lemma 2.3 and Lemma 2.2 the representation \(\bar\pi_j\otimes\bar\tau\) has a nonzero invariant vector only if \(\tau\simeq\bar\pi_j\). The \(\bar\pi_j\) are pairwise inequivalent, so this happens for at most one \(j\). For all other \(j\), Lemma 1.2 gives
\[
L\bigl((\bar\pi_j(s)\otimes\bar\tau(s))_{s\in S}\bigr)\ge\kappa\cdot1
\]
in \(M_m(M_j)\). By Lemma 7.1, parts 4 and 2,
\[
L\bigl((q(s)\otimes\bar\tau(s))_{s\in S}\bigr)\ge\kappa\cdot1
\]
in \(M_m(Q)\). Applying \(\eta\) to the entries gives \(L((\sigma(s)\otimes\bar\tau(s))_s)\ge\kappa\) on \(K^m\). But \(\tau\prec\sigma\) gives a nonzero vector \(\xi\in K^m\) that is invariant under \(\sigma\otimes\bar\tau\) (Lemma 2.3), and \(\langle L\xi,\xi\rangle=0\) for it. This is a contradiction.

*Step 3: the bound in the minimal tensor product.* Let \(B\) act faithfully with its unit on \(E\). By Step 2 and Lemma 5.1,
\[
L\bigl((u_s\otimes\sigma(s))_{s\in S}\bigr)\ge b\cdot1
\]
on \(E\otimes K\). By (N1) this operator is \(L((u_s\otimes q(s))_s)\), computed in \(B\otimes_{\min}Q\). So \(L((u_s\otimes q(s))_s)\ge b\) in \(B\otimes_{\min}Q\), by spectral permanence (C2).

*Step 4: transport to a sequence algebra over \(B\).* Since \(B\) is nuclear, the same inequality holds in \(B\otimes_{\max}Q\). Let
\[
C=\prod_jM_{d_j}(B)\Big/\bigoplus_jM_{d_j}(B) ,
\]
and define
\[
\begin{aligned}
\alpha(x)&=[(x\otimes1_{M_j})_j]&&(x\in B),\\
\beta([(y_j)_j])&=[(1_B\otimes y_j)_j]&&(y_j\in M_j).
\end{aligned}
\]
Here \(x\otimes1\) is the diagonal matrix with the entries \(x\), and \(1\otimes y\) is the matrix \(y\) with scalar entries, both in \(M_{d_j}(B)\). The map \(\beta\) is well defined on the quotient \(Q\) because \(\|1\otimes y_j\|=\|y_j\|\). Both maps are unital \(*\)-homomorphisms into \(C\), and their ranges commute. By (N2) there is a unital \(*\)-homomorphism \(\Psi\) from \(B\otimes_{\max}Q\) to \(C\) with \(\Psi(x\otimes y)=\alpha(x)\beta(y)\). It maps \(u_s\otimes q(s)\) to the class of \((u_s\otimes\bar\pi_j(s))_j\). So with
\[
L_j=L\bigl((u_s\otimes\bar\pi_j(s))_{s\in S}\bigr)\in M_{d_j}(B) ,
\]
we get \([(L_j)_j]=\Psi\bigl(L((u_s\otimes q(s))_s)\bigr)\ge b\cdot1\) in \(C\), by (C1).

*Step 5: the contradiction.* Let \(f(r)=\max\{b-r,0\}\) on \([0,R]\). The spectrum of \([(L_j)_j]\) lies in \([b,R]\), where \(f=0\); so \(f([(L_j)_j])=0\). By Lemma 7.1, parts 3 and 1, \(\limsup_j\|f(L_j)\|=0\). But \(\|f(L_j)\|\) is the largest value of \(f\) on the spectrum of \(L_j\), which is
\[
\begin{aligned}
b-\min\operatorname{spec}L_j&=b-d(\mathbf u,\pi_j)\\
&>b-a>0
\end{aligned}
\]
for every \(j\). This is a contradiction. \(\blacksquare\)

Nuclearity is used once, in Step 4: the bound is obtained in the minimal tensor product, where the two factors act on different Hilbert spaces and the density operator argument applies, and it is needed in the maximal tensor product, which maps to the sequence algebra \(C\). The dimensions \(d_j\) may be unbounded.

## 9. Exercises

**9.1.** Show that \(L(\mathbf z)=0\) exactly if \(z_s=1\) for all \(s\in S\), and that \(d(\mathbf z,\mathbf 1)=\min\operatorname{spec}L(\mathbf z)\) for the trivial representation \(\mathbf 1\) of dimension \(1\).

**9.2.** Let \(\pi\) be a unitary representation of dimension \(d\). Show that the vector \(\xi=(e_1,\dots,e_d)\) of \((\mathbb C^d)^d\) is invariant under \(\pi\otimes\bar\pi\), and identify \(T_\xi\).

**9.3.** Show by an example with \(2\times2\) matrices that Lemma 4.1 fails for self-adjoint matrices that are not positive.

**9.4.** Let \(\sigma\) be a unitary representation of \(\Gamma\) on \(K\) and \(\tau\prec\sigma\) with \(\tau\) of dimension \(m\). Find unitaries \(U_s\) on \(E=\mathbb C^m\) such that \(L((U_s\otimes\sigma(s))_s)\) has the eigenvalue \(0\).

**9.5.** Let \(B=\mathbb C\) and let \(\mathbf u=(1)_{s\in S}\). Assume (T). Show directly that \(D(\mathbf u)\) consists of the class of the trivial representation only.

## 10. Solutions

**9.1.** In a faithful unital representation, \(\langle L(\mathbf z)\xi,\xi\rangle=\sum_s\|z_s\xi-\xi\|^2\); this vanishes for all \(\xi\) exactly if all \(z_s=1\), and a positive operator with vanishing quadratic form is \(0\). For the trivial representation, \(z_s\otimes\bar{\mathbf 1}(s)=z_s\).

**9.2.** \(T_\xi\) maps \(e_l\) to \(e_l\); it is the identity matrix. By Lemma 2.1, \(T_{(\pi(g)\otimes\bar\pi(g))\xi}=\pi(g)\,T_\xi\,\pi(g)^*=T_\xi\).

**9.3.** Let \(X\) be the diagonal matrix with the entries \(1,-1\) and \(Y=-X\). Then \(X^2=Y^2\), but \(\|X-Y\|_2^2=8\).

**9.4.** Take \(U_s=\bar\tau(s)\). The representation \(\tau\otimes\bar\tau\) has the nonzero invariant vector of Exercise 9.2. Identify \(E\otimes K\) with \(K^m\), so that \(U_s\otimes\sigma(s)\) becomes \(\sigma(s)\otimes\bar\tau(s)\) in the notation of Section 2. By Lemma 2.3, \(\sigma\otimes\bar\tau\) has a nonzero invariant vector, on which \(L\) vanishes.

**9.5.** \(u_s\otimes\bar\pi(s)=\bar\pi(s)\), so \(d(\mathbf u,\pi)=\min\operatorname{spec}L((\bar\pi(s))_s)\). By Lemma 1.2 for the representation \(\bar\pi\) this is \(0\) if \(\bar\pi\) has a nonzero invariant vector and at least \(\kappa>a\) otherwise. An irreducible representation with a nonzero invariant vector is the trivial representation of dimension \(1\).

## References

- [OpenAI-K] OpenAI, *An explicit obstruction to nuclear norm-ultrapower embeddings*, OpenAI Math Release preprint, 23 September 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026
