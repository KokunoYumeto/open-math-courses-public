# Convergent sequences and a relative tensor norm

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Theorem 2.3 of [Close operator algebras](close-operator-algebras.md) shows that the main theorem of this course has no analogue for separable C\*-algebras. Two unital norm-separable C\*-algebras on a separable Hilbert space can be arbitrarily close, share their identity and their von Neumann closure, and still not be conjugate by any unitary, near the identity or not. This lesson and [A free-group deformation and close separable algebras](a-free-group-deformation-and-close-separable-algebras.md) prove the theorem [OpenAI-289b].

The present lesson reduces it to a question about two subalgebras \(P,Q\) of one algebra \(D\) with trivial center. The sequences in \(D\) that converge to an element of \(P\) form a C\*-algebra \(\mathcal E_D(P)\), and similarly for \(Q\). The distance between \(\mathcal E_D(P)\) and \(\mathcal E_D(Q)\) equals that between \(P\) and \(Q\), but a unitary conjugating one onto the other is assembled from unitaries that normalize \(D\) and approximately carry \(P\) onto \(Q\) (Proposition 1.1). A property of the position of \(P\) in \(D\) that survives such approximations therefore separates the two sequence algebras. Section 2 introduces one: a comparison between products with the commutant of \(D\) and tensor products with it (Corollary 2.3).

We use: [Close operator algebras](close-operator-algebras.md) (Definition 1.1 and Lemma 1.5).

## 1. Algebras of convergent sequences

Throughout this section, \(L\) is a nonzero separable Hilbert space, \(D\subseteq B(L)\) is a unital norm-separable C\*-algebra whose center is \(Z(D)=\mathbb CI\), and \(P,Q\subseteq D\) are C\*-subalgebras containing \(I\). On \(H=\bigoplus_{n\ge1}L\), a bounded sequence \(x=(x_n)\) in \(B(L)\) acts as the block diagonal operator \((\xi_n)\mapsto(x_n\xi_n)\), whose norm is \(\sup_n\|x_n\|\). Put
\[
\begin{gathered}
\mathcal E_D(P)=\bigl\{(x_n)_{n\ge1}:x_n\in D,\ \lim_nx_n\\
\text{exists in norm and lies in }P\bigr\},
\end{gathered}
\]
and define \(\mathcal E_D(Q)\) in the same way. We write \(e_n\) for the projection of \(H\) onto its \(n\)-th summand, and \(\hat b=(b,b,\dots)\) for the constant sequence with value \(b\).

**Proposition 1.1.**

1. \(\mathcal E_D(P)\) and \(\mathcal E_D(Q)\) are norm-separable C\*-algebras on \(H\) containing \(I_H\), and
\[
d\bigl(\mathcal E_D(P),\mathcal E_D(Q)\bigr)=d(P,Q).
\]
2. If a unitary \(S\) of \(H\) satisfies \(S\mathcal E_D(P)S^*=\mathcal E_D(Q)\), then there are unitaries \(U_n\) of \(L\) with \(U_nDU_n^*=D\) for all \(n\), such that every \(b\in Q\) has an element \(p_b\in P\) with
\[
\lim_n\|b-U_np_bU_n^*\|=0 .
\]
The sequence \((U_n)\) does not depend on \(b\).
3. \(\mathcal E_D(P)'=\mathcal E_D(Q)'\); in particular \(\mathcal E_D(P)''=\mathcal E_D(Q)''\).

**Proof.** *The algebras.* Let \(\mathcal C\) be the set of norm-convergent sequences in \(D\), acting on \(H\) as above. It is closed under sums, products and adjoints and contains \(\hat I=I_H\). It is norm closed: if \(x^{(k)}\in\mathcal C\) and \(\sup_n\|x^{(k)}_n-x_n\|\to0\), then
\[
\begin{aligned}
\|x_n-x_m\|&\le2\sup_j\|x_j-x^{(k)}_j\|\\
&\quad +\|x^{(k)}_n-x^{(k)}_m\|
\end{aligned}
\]
shows that \((x_n)\) is a Cauchy sequence in the complete space \(D\). The map \(\lim:\mathcal C\to D\) is a unital \(*\)-homomorphism with \(\|\lim x\|\le\|x\|\), so \(\mathcal E_D(P)=\lim^{-1}(P)\) is a norm-closed \(*\)-subalgebra of \(\mathcal C\) containing \(I_H\). Each \(x\in\mathcal E_D(P)\) is the sum of the constant sequence \(\widehat{\lim x}\) and a sequence tending to \(0\). Fix countable dense subsets \(D^\circ\subseteq D\) and \(P^\circ\subseteq P\). The sequences with finitely many nonzero entries, all in \(D^\circ\), are dense among the sequences in \(D\) tending to \(0\), and the constant sequences with value in \(P^\circ\) are dense among the constant sequences in \(P\). So \(\mathcal E_D(P)\) is norm separable.

*The distance.* With the directed distance \(\delta\) of Definition 1.1 of [Close operator algebras](close-operator-algebras.md), we show \(\delta(\mathcal E_D(P),\mathcal E_D(Q))=\delta(P,Q)\); exchanging \(P\) and \(Q\) then gives part 1. Let \(x\) be a contraction in \(\mathcal E_D(P)\) and \(p=\lim x\), so \(\|p\|\le1\). For \(\eta>0\) choose \(q\in Q_1\) with \(\|p-q\|\le\delta(P,Q)+\eta\), and \(N\) with \(\|x_n-p\|\le\eta\) for \(n>N\). Let \(y_n=x_n\) for \(n\le N\) and \(y_n=q\) for \(n>N\). Since \(Q\subseteq D\), the contraction \(y\) lies in \(\mathcal E_D(Q)\), and
\[
\begin{aligned}
\|x-y\|&=\sup_{n>N}\|x_n-q\|\\
&\le\delta(P,Q)+2\eta .
\end{aligned}
\]
Hence \(\delta(\mathcal E_D(P),\mathcal E_D(Q))\le\delta(P,Q)\). Conversely, let \(p\in P_1\) and let \(y\) be a contraction in \(\mathcal E_D(Q)\), with limit \(q\in Q_1\). Then
\[
\begin{aligned}
\|\hat p-y\|&\ge\lim_n\|p-y_n\|=\|p-q\|\\
&\ge\operatorname{dist}(p,Q_1).
\end{aligned}
\]
Since \(\hat p\) is a contraction in \(\mathcal E_D(P)\), \(\delta(\mathcal E_D(P),\mathcal E_D(Q))\ge\delta(P,Q)\).

*The center.* The projection \(e_n\) is the sequence with \(I\) in place \(n\) and \(0\) elsewhere. It tends to \(0\in P\), so it lies in \(\mathcal E_D(P)\), and it commutes with every block diagonal operator. Let \(z=(z_n)\) be central in \(\mathcal E_D(P)\). For \(c\in D\), the sequence with \(c\) in place \(n\) and \(0\) elsewhere lies in \(\mathcal E_D(P)\); commuting with it gives \(z_nc=cz_n\). So \(z_n\in D\cap D'=\mathbb CI\) for every \(n\). A central projection is therefore a sequence whose entries are \(0\) or \(I\), and a nonzero one dominates some \(e_n\). So the \(e_n\) are exactly the minimal nonzero central projections of \(\mathcal E_D(P)\), and likewise of \(\mathcal E_D(Q)\).

*Conjugating unitaries.* Let \(S\) be as in part 2. The \(*\)-isomorphism \(x\mapsto SxS^*\) maps the center of \(\mathcal E_D(P)\) onto that of \(\mathcal E_D(Q)\) and preserves minimal projections, so there is a bijection \(\sigma\) of \(\{1,2,\dots\}\) with \(Se_nS^*=e_{\sigma(n)}\). Hence \(S\) maps the \(n\)-th summand onto the \(\sigma(n)\)-th; identifying both with \(L\) gives a unitary \(U_n\) of \(L\). Every sequence supported in place \(n\) lies in \(\mathcal E_D(P)\), so the corner \(e_n\mathcal E_D(P)e_n\) is \(D\) acting on the \(n\)-th summand; likewise \(e_{\sigma(n)}\mathcal E_D(Q)e_{\sigma(n)}\) is \(D\) on the \(\sigma(n)\)-th summand. Conjugation by \(S\) maps the first corner onto the second, which says \(U_nDU_n^*=D\). For \(b\in Q\), \(\hat b\in\mathcal E_D(Q)\), so \(S^*\hat bS\in\mathcal E_D(P)\). On the \(n\)-th summand, \(S\) acts as \(U_n\) into the \(\sigma(n)\)-th summand, \(\hat b\) acts there as \(b\), and \(S^*\) returns; so the \(n\)-th entry of \(S^*\hat bS\) is \(U_n^*bU_n\). These entries converge to some \(p_b\in P\), and
\[
\|b-U_np_bU_n^*\|=\|U_n^*bU_n-p_b\|\longrightarrow0 .
\]

*Commutants.* An operator \(T\) on \(H\) commuting with \(\mathcal E_D(P)\) commutes with every \(e_n\), so \(T\) is block diagonal, \(T=(T_n)\) with \(\sup_n\|T_n\|<\infty\). Commuting with the sequences supported in place \(n\) gives \(T_n\in D'\). Conversely, every bounded block diagonal operator with blocks in \(D'\) commutes with every block diagonal operator with blocks in \(D\). This description of the commutant does not involve \(P\), so it is also the commutant of \(\mathcal E_D(Q)\). \(\square\)

Both algebras contain all sequences in \(D\) tending to \(0\); this common part fixes their commutant and their von Neumann closure. They differ only in the limits allowed.

## 2. A tensor-norm identity relative to the ambient algebra

Let \(P\subseteq D\subseteq B(L)\) be unital C\*-algebras. Elements of \(P\) commute with elements of the commutant \(D'\), so for \(p_1,\dots,p_m\in P\) and \(z_1,\dots,z_m\in D'\) two operators can be formed from the pairs \((p_i,z_i)\): the sum of products \(\sum_ip_iz_i\) on \(L\), and the sum of tensor products \(\sum_ip_i\otimes z_i\) on \(L\otimes L\).

**Definition 2.1.** \(P\) has the *spatial tensor-norm identity relative to \(D\)* if
\[
\Bigl\|\sum_{i=1}^mp_iz_i\Bigr\|=\Bigl\|\sum_{i=1}^mp_i\otimes z_i\Bigr\|
\]
for every \(m\ge1\), all \(p_1,\dots,p_m\in P\) and all \(z_1,\dots,z_m\in D'\).

The right side is the spatial C\*-norm of \(\sum_ip_i\otimes z_i\) in the algebraic tensor product of \(P\) and \(D'\). The identity therefore says that the product map \(\sum_ip_i\otimes z_i\mapsto\sum_ip_iz_i\) is isometric for the spatial norm, so that the C\*-algebra generated by \(P\) and \(D'\) is a copy of their spatial tensor product (Exercise 3.3).

**Lemma 2.2** (invariance). Let \(P,Q\subseteq D\subseteq B(L)\) be unital C\*-algebras, and suppose \(P\) has the spatial tensor-norm identity relative to \(D\).

1. If \(U\) is a unitary of \(L\) with \(UDU^*=D\), then \(UPU^*\) has the identity relative to \(D\).
2. If unitaries \(U_n\) of \(L\) satisfy \(U_nDU_n^*=D\), and every \(b\in Q\) has some \(p_b\in P\) with \(\|b-U_np_bU_n^*\|\to0\), then \(Q\) has the identity relative to \(D\).

**Proof.** (1) Since \(U\) maps \(D\) onto itself by conjugation, it maps \(D'\) onto itself as well. Let \(p_i\in P\) and \(z_i\in D'\), and put \(z_i^U=U^*z_iU\in D'\). Then
\[
\begin{gathered}
\begin{aligned}
\sum_iUp_iU^*z_i&=U\Bigl(\sum_ip_iz_i^U\Bigr)U^*,
\end{aligned}\\
\begin{aligned}
&\sum_iUp_iU^*\otimes z_i=(U\otimes U)\Bigl(\sum_ip_i\\
&\qquad \otimes z_i^U\Bigr)(U\otimes U)^*,
\end{aligned}
\end{gathered}
\]
and the identity for the families \((p_i)\) and \((z_i^U)\) gives equal norms on the left.

(2) Let \(b_1,\dots,b_m\in Q\), \(z_1,\dots,z_m\in D'\), and \(q_{i,n}=U_np_{b_i}U_n^*\). For each \(n\), the family \(q_{1,n},\dots,q_{m,n}\) lies in \(U_nPU_n^*\), so part 1 gives \(\|\sum_iq_{i,n}z_i\|=\|\sum_iq_{i,n}\otimes z_i\|\). Both \(\|\sum_i(b_i-q_{i,n})z_i\|\) and \(\|\sum_i(b_i-q_{i,n})\otimes z_i\|\) are at most \(\sum_i\|b_i-q_{i,n}\|\|z_i\|\), which tends to \(0\). So \(\|\sum_ib_iz_i\|\) and \(\|\sum_ib_i\otimes z_i\|\) are limits of the same sequence of numbers. \(\square\)

**Corollary 2.3** (the obstruction). Assume the hypotheses of Section 1. Suppose that \(P\) has the spatial tensor-norm identity relative to \(D\) and \(Q\) does not. Then no unitary of \(H\) conjugates \(\mathcal E_D(P)\) onto \(\mathcal E_D(Q)\). If \(W\) is a unitary of \(L\) with \(WPW^*=Q\), then
\[
d\bigl(\mathcal E_D(P),\mathcal E_D(Q)\bigr)\le2\|W-I\| .
\]

**Proof.** A unitary \(S\) with \(S\mathcal E_D(P)S^*=\mathcal E_D(Q)\) would give, by Proposition 1.1(2), unitaries \(U_n\) as in Lemma 2.2(2), and that lemma would give the identity for \(Q\). For the estimate, Lemma 1.5(2) of [Close operator algebras](close-operator-algebras.md), with \(A=B=P\) and \(v=W\), gives \(d(P,Q)\le2\|W-I\|\); Proposition 1.1(1) transfers this bound to the sequence algebras. \(\square\)

In [A free-group deformation and close separable algebras](a-free-group-deformation-and-close-separable-algebras.md), \(P\) and \(Q\) are conjugate by a unitary \(W\) close to \(I\), so as algebras of operators on \(L\) they look alike. By the corollary, no such \(W\) normalizes \(D\): what differs is the position of \(P\) and \(Q\) inside \(D\), and the sequence algebras turn this relative difference into an obstruction to every unitary conjugacy.

## 3. Exercises

**Exercise 3.1.** Show that every element of \(\mathcal E_D(P)\) is uniquely the sum of a sequence in \(D\) tending to \(0\) and a constant sequence with value in \(P\), and that \(x\mapsto\lim x\) induces a \(*\)-isomorphism from the quotient of \(\mathcal E_D(P)\) by the sequences tending to \(0\) onto \(P\).

**Exercise 3.2.** Let \(D=B(L)\). Show that every unital C\*-subalgebra \(P\subseteq D\) has the spatial tensor-norm identity relative to \(D\).

**Exercise 3.3.** Let \(P\subseteq D\subseteq B(L)\) be unital C\*-algebras and \(P\odot D'\) the algebraic tensor product, with the norm \(\|w\|_{\rm sp}\) of \(w\) as an operator on \(L\otimes L\). Show that \(\mu(p\otimes z)=pz\) defines a \(*\)-homomorphism \(\mu:P\odot D'\to B(L)\), and that \(P\) has the identity relative to \(D\) exactly when \(\|\mu(w)\|=\|w\|_{\rm sp}\) for all \(w\). Deduce that the identity passes from \(P\) to every unital C\*-subalgebra of \(P\).

**Exercise 3.4.** Let \(U_n\) be unitaries of \(L\) normalizing \(D\) and converging in norm to a unitary \(U\) with \(UPU^*=P\). Show that the block diagonal unitary \((U_n)\) of \(H\) conjugates \(\mathcal E_D(P)\) onto itself.

**Exercise 3.5.** Drop the hypothesis \(Z(D)=\mathbb CI\). Show that the center of \(\mathcal E_D(P)\) consists of the norm-convergent sequences in \(Z(D)\) whose limit lies in \(P\). If \(Z(D)\) is spanned by a projection \(f\notin\{0,I\}\) and \(I-f\), list the minimal nonzero central projections of \(\mathcal E_D(P)\).

## 4. Solutions

**Solution 3.1.** For \(x\in\mathcal E_D(P)\), \(x-\widehat{\lim x}\) tends to \(0\), and its entries lie in \(D\) because \(P\subseteq D\). A constant sequence tending to \(0\) is \(0\), which gives uniqueness. The map \(\lim\) is a \(*\)-homomorphism from \(\mathcal E_D(P)\) onto \(P\) (it takes the value \(p\) at \(\hat p\)), and its kernel is the set of sequences tending to \(0\).

**Solution 3.2.** Here \(D'=\mathbb CI\), so \(z_i=c_iI\) with \(c_i\in\mathbb C\). Then \(\sum_ip_iz_i=p\) and \(\sum_ip_i\otimes z_i=p\otimes I\), with \(p=\sum_ic_ip_i\), and \(\|p\otimes I\|=\|p\|\).

**Solution 3.3.** Elements of \(P\subseteq D\) commute with elements of \(D'\), so \(\mu\) is multiplicative on elementary tensors, hence on \(P\odot D'\), and it respects adjoints. Every \(w\in P\odot D'\) has the form \(\sum_ip_i\otimes z_i\), with \(\mu(w)=\sum_ip_iz_i\); so equality of norms for all \(w\) is Definition 2.1. If \(R\subseteq P\) is a unital C\*-subalgebra, Definition 2.1 for \(R\) is the special case of Definition 2.1 for \(P\) with \(p_i\in R\).

**Solution 3.4.** Conjugation by \((U_n)\) maps \(x=(x_n)\) to \((U_nx_nU_n^*)\), whose entries lie in \(D\). If \(x_n\to p\), then
\[
\begin{aligned}
&\|U_nx_nU_n^*-UpU^*\|\\
&\quad \le2\|U_n-U\|\|x_n\|+\|x_n-p\|\\
&\quad \to0,
\end{aligned}
\]
and \(UpU^*\in P\). So \((U_n)\) maps \(\mathcal E_D(P)\) into itself. The inverse \((U_n^*)\) has the same form, with limit \(U^*\) and \(U^*PU=P\), so the map is onto.

**Solution 3.5.** As in the proof of Proposition 1.1, a central element \(z\) has \(z_n\in D\cap D'=Z(D)\) for all \(n\), and its limit lies in \(P\) by definition of \(\mathcal E_D(P)\). Conversely, such a sequence commutes with all block diagonal operators with blocks in \(D\). With \(Z(D)=\mathbb Cf+\mathbb C(I-f)\), the projections \(fe_n\) and \((I-f)e_n\) (meaning \(f\), respectively \(I-f\), in place \(n\) and \(0\) elsewhere) tend to \(0\), so they are central projections of \(\mathcal E_D(P)\); they are minimal, and every nonzero central projection dominates one of them. These are all the minimal ones.

## References

- [OpenAI-289b] OpenAI, Close separable C\*-algebras without spatial conjugacy, preprint, 5 October 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026
