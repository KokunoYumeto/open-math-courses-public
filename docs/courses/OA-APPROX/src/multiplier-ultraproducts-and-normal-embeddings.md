# Multiplier ultraproducts and normal embeddings

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

The central sequence algebra uses sequences that asymptotically commute with normal functionals. A larger construction uses every bounded sequence that preserves the sequences vanishing strong*. This multiplier condition is essential for a nontracial algebra. We will prove that the resulting quotient is a von Neumann algebra, with normal copies of the original algebra and its central sequence algebra.

Let \(M\ne0\) have a faithful normal state \(\varphi\), and let \(\omega\) be a free ultrafilter on \(\mathbb N\). Sections 1–4 and 6–7 use only this hypothesis; equivalently, \(M\) is countably decomposable. Section 5 assumes separable predual for its central sequence algebra. No factor hypothesis is imposed until the type I example. Inputs are faithful normal state GNS representations, the bounded strong* topology, \(C^*\)-functional calculus and quotients, the definition of a multiplier by its two multiplication maps, and Kaplansky density.

Write
\[
\|a\|_\varphi=\varphi(a^*a)^{1/2},\qquad
\|a\|_{\varphi,\#}=
\left(\frac{\varphi(a^*a)+\varphi(aa^*)}{2}\right)^{1/2}.
\tag{1}
\]
On bounded subsets of \(M\), convergence of the latter to zero is precisely strong* convergence. The faithful state GNS proof uses the separating cyclic vector and the dense vectors from its commutant, and does not require a separable Hilbert space.

## 1. The zero algebra and its multipliers

Put
\[
I_\omega=\{(x_n)\in\ell^\infty(\mathbb N,M):
\|x_n\|_{\varphi,\#}\to_\omega0\},
\qquad
N_\omega=\{a:aI_\omega\subset I_\omega,\ I_\omega a\subset I_\omega\}.
\tag{2}
\]
The bounded strong* description shows that \(I_\omega\) is independent of the choice of faithful normal state. It is a norm-closed, self-adjoint algebra: products of two bounded strong*-null sequences vanish strong*, by applying them and their adjoints to fixed vectors. It need not be an ideal in the entire sequence algebra.

For example, in \(B(\ell^2(\mathbb N_0))\), take basis vectors \(\xi_n\), projections \(p_n\) onto \(\mathbb C\xi_n\), and operators \(a_n\xi_0=\xi_n\), zero on the other basis vectors. Then \(p_n\to0\) strong*, but \(p_na_n=a_n\) does not tend strongly to zero on \(\xi_0\). Thus \(a\notin N_\omega\).

**Proposition 1.1.** \(N_\omega\) is a unital \(C^*\)-algebra containing \(I_\omega\) as a closed two-sided ideal. It identifies with the multiplier algebra of \(I_\omega\).

**Proof.** The two ideal-preservation conditions survive products, sums and adjoints. For uniform norm limits, if \(a^{(r)}\to a\) and \(z\in I_\omega\) is bounded, the products with \(a-a^{(r)}\) have operator norms at most \(\|a-a^{(r)}\|\sup_n\|z_n\|\). First take the ultralimit for fixed \(r\), then let \(r\to\infty\). This proves closure and both ideal conditions. The unit sequence belongs to \(N_\omega\), and \(I_\omega\subset N_\omega\) follows from its own product closure.

To see the multiplier identification, let \(q_n\) be the sequence equal to \(1\) at coordinate \(n\) and zero elsewhere. These central projections belong to \(I_\omega\), and \(q_nI_\omega\) is the unital coordinate algebra \(M\). For an abstract multiplier \(m\), the products \(mq_n,q_nm\) belong to \(I_\omega\). The right-support identity \((mq_n)q_n=mq_n\), and centrality of \(q_n\) in \(I_\omega\), give \(mq_n=q_nmq_n=q_nm\). Thus \(mq_n\) specifies an operator \(a_n\in M\), with \(\|a_n\|\le\|m\|\).

For \(z\in I_\omega\), the coordinate of \(mz\) is \(a_nz_n\), and that of \(zm\) is \(z_na_n\). Hence \(a=(a_n)\) lies in \(N_\omega\) and realizes \(m\). Conversely every element of \(N_\omega\) defines those bounded left and right multiplier maps. Coordinate tests \(q_n\) and the operator norm bounds show that the identification is isometric. No assertion that the finite-coordinate projections approximate every element of \(I_\omega\) in norm is needed. \(\square\)

**Lemma 1.2.** A bounded sequence \(a_n\) belongs to \(N_\omega\) if and only if, for every \(\varepsilon>0\), there are \(\delta>0\) and \(A\in\omega\) such that
\[
n\in A,\quad \|x\|\le1,\quad\|x\|_{\varphi,\#}<\delta
\quad\Longrightarrow\quad
\|a_nx\|_{\varphi,\#}+\|xa_n\|_{\varphi,\#}<\varepsilon.
\tag{3}
\]

**Proof.** The displayed uniform condition applies to the coordinates of any bounded \(z\in I_\omega\), after rescaling its operator norm bound. Intersect \(A\) with the set on which its seminorm is less than \(\delta\); this proves both products vanish.

Conversely, if (3) fails for some \(\varepsilon\), the sets
\[
B_r=\{n:\text{some }\|x\|\le1,\ 
\|x\|_{\varphi,\#}<1/r
\text{ has }\|a_nx\|_{\varphi,\#}+\|xa_n\|_{\varphi,\#}\ge\varepsilon\}
\tag{4}
\]
belong to \(\omega\). Otherwise their complements would provide (3). They are decreasing. Let \(r(n)\) be the largest \(r\le n\) with \(n\in B_r\), and zero if none exists. Then \(r(n)\to_\omega\infty\). Choose a witnessing \(z_n\) for \(r(n)>0\), and use zero otherwise. These contractions belong to \(I_\omega\), but the sum of the two product seminorms stays at least \(\varepsilon\) on an \(\omega\)-large set. This contradicts \(a\in N_\omega\). \(\square\)

Constant sequences lie in \(N_\omega\), because multiplication by a fixed operator preserves bounded strong* convergence on either side.

## 2. A faithful quotient state

Define
\[
M^\omega=N_\omega/I_\omega,\qquad
\pi:N_\omega\to M^\omega,\qquad
\varphi^\omega(\pi(x_n))=\lim_{n\to\omega}\varphi(x_n).
\tag{5}
\]
The superscript distinguishes this algebra from the central sequence algebra \(M_\omega\).

**Lemma 2.1.** Formula (5) defines a faithful state on the quotient.

**Proof.** It is a state on \(N_\omega\) by scalar ultralimits and vanishes on \(I_\omega\) by Cauchy–Schwarz. It therefore descends to the quotient. If \(X\ge0\), lift \(X^{1/2}\) to \(b\in N_\omega\), and put \(h_n=b_n^*b_n\). Then \(h\) is positive and bounded, with \(\pi(h)=X\).
If \(\varphi^\omega(X)=0\), then for a bound \(h_n\le C1\),
\[
\varphi(h_n^2)\le C\varphi(h_n)\longrightarrow_\omega0.
\tag{6}
\]
Since \(h_n=h_n^*\), this is its symmetric strong* seminorm squared. Thus \(h\in I_\omega\) and \(X=0\). Faithfulness follows. \(\square\)

Use its faithful GNS representation, with cyclic vector \(\Omega\), and put
\(\|X\|_{\varphi^\omega}=\varphi^\omega(X^*X)^{1/2}\).
For a representative \(x\in N_\omega\), this norm equals the ultralimit of \(\|x_n\|_\varphi\).

## 3. Completeness on two cyclic vectors

**Lemma 3.1.** For every fixed \(Y\in M^\omega\), the self-adjoint unit ball is complete for
\[
p_Y(X)=\|X\|_{\varphi^\omega}+\|XY\|_{\varphi^\omega}.
\tag{7}
\]

**Proof.** From a \(p_Y\)-Cauchy sequence choose a subsequence \(X_r\) with
\(p_Y(X_{r+1}-X_r)<2^{-r-1}\).
Choose self-adjoint contraction representatives \(a_r(k)\in N_\omega\). Such lifts exist: take a self-adjoint lift and apply the continuous scalar clipping function to \([-1,1]\). Fix a representative \(y(k)\) of \(Y\).

Inductively modify the representative of \(X_{r+1}\) outside an \(\omega\)-large set so that, at every coordinate \(k\),
\[
\|a_{r+1}(k)-a_r(k)\|_\varphi
+\|(a_{r+1}(k)-a_r(k))y(k)\|_\varphi
\le2^{-r}.
\tag{8}
\]
The original differences have ultralimit less than \(2^{-r-1}\), so the set where (8) holds belongs to \(\omega\). Outside it set \(a_{r+1}(k)=a_r(k)\). This changes the sequence by an element of \(I_\omega\), preserving both its multiplier property and its quotient element.

For each fixed \(k\), the self-adjoint contractions \(a_r(k)\) are Cauchy in \(\|\cdot\|_\varphi\), hence in the bounded strong* topology. Their limit \(a(k)\in M\) is a self-adjoint contraction. Telescoping (8), including its action on the fixed vector \(y(k)\Omega_\varphi\), gives
\[
\|a(k)-a_r(k)\|_\varphi+
\|(a(k)-a_r(k))y(k)\|_\varphi
\le2^{1-r}.
\tag{9}
\]

We must check that \(a=(a(k))\) is a multiplier. For bounded \(z=(z(k))\in I_\omega\), with \(\|z(k)\|\le K\),
\[
\|z(k)a(k)\|_\varphi
\le\|z(k)a_r(k)\|_\varphi+K\,2^{1-r}.
\tag{10}
\]
The first term tends to zero along \(\omega\) for fixed \(r\), since \(a_r\in N_\omega\). Letting \(r\to\infty\) shows that \(za\) vanishes in its first seminorm. Its adjoint seminorm is bounded by \(\|z(k)^*\|_\varphi\), since \(a(k)\) is a self-adjoint contraction. Apply the same reasoning to \(z^*\) to obtain both seminorms for \(az\) as well. Thus \(a\in N_\omega\).

Equation (9) now passes to the quotient, giving \(p_Y(\pi(a)-X_r)\le2^{1-r}\). The selected subsequence converges, hence so does the original Cauchy sequence. \(\square\)

**Theorem 3.2.** \(M^\omega\) is a von Neumann algebra in this GNS representation, and \(\varphi^\omega\) is faithful normal.

**Proof.** Suppose \(X_i\) is a strong-operator Cauchy net of self-adjoint contractions. For every \(Y\in M^\omega\), it is Cauchy for (7), since that expression tests the vectors \(\Omega,Y\Omega\). Completeness of that metric gives an element \(X_Y\) with
\[
(X_i-X_Y)\Omega\to0,\qquad
(X_i-X_Y)Y\Omega\to0.
\tag{11}
\]
All the \(X_Y\Omega\) are the same limit. The state is faithful, so equality on \(\Omega\) implies equality of these algebra elements. Denote their common value by \(X\). Equation (11) for all \(Y\), density of \(M^\omega\Omega\), and uniform boundedness give \(X_i\to X\) strongly.

Thus the self-adjoint unit ball is strongly closed. Kaplansky density makes it strongly dense in the self-adjoint unit ball of the bicommutant. These balls therefore agree, and real and imaginary parts show that the whole represented algebra equals its bicommutant. The state is its vector state, hence normal, and remains faithful by Lemma 2.1. \(\square\)

## 4. The normal copy of the original algebra

The constant map
\[
\iota:M\to M^\omega,\qquad \iota(a)=\pi(a,a,\ldots)
\tag{12}
\]
is a unital injective *-homomorphism: a constant sequence can belong to \(I_\omega\) only if its operator is zero. Its state restriction is \(\varphi^\omega\circ\iota=\varphi\).
It is normal. If \(0\le a_i\uparrow a\), the supremum \(Z=\sup_i\iota(a_i)\) in \(M^\omega\) satisfies \(Z\le\iota(a)\), and
\[
\varphi^\omega(\iota(a)-Z)
=\varphi(a)-\lim_i\varphi(a_i)=0.
\tag{13}
\]
Faithfulness gives \(Z=\iota(a)\). We henceforth identify \(M\) with this normal copy.

## 5. The normal centralizing subalgebra

Now assume \(M\) has separable predual, but allow nonfactor algebras. Let \(C_\omega\) consist of bounded sequences with
\(\|[x_n,\psi]\|\to_\omega0\) for every \(\psi\in M_*\), using the functional convention of the preceding central sequence lessons.
Every element of \(I_\omega\) belongs to \(C_\omega\), by the normal-functional Cauchy–Schwarz estimate.

Also \(C_\omega\subset N_\omega\). To verify the potentially troublesome right multiplication, take \(\|a_n\|\le C\) and \(\|z_n\|\le K\), with \(a\) centralizing and \(z\in I_\omega\). Moving \(a_n^*\) past the state gives
\[
\begin{aligned}
\varphi(a_n^*z_n^*z_na_n)
&\le |\varphi(z_n^*z_na_na_n^*)|
+CK^2\|[a_n^*,\varphi]\|\\
&\le C^2K\,\|z_n\|_\varphi
+CK^2\|[a_n^*,\varphi]\|\longrightarrow_\omega0.
\end{aligned}
\tag{14}
\]
The second line is Cauchy–Schwarz applied to the positive bounded factors. The other right/left adjoint estimate is identical with \(z_nz_n^*\) and \([a_n,\varphi]\). The two remaining seminorms are bounded directly by \(C\|z_n\|_\varphi\) or \(C\|z_n^*\|_\varphi\).

**Theorem 5.1.** The inclusion induces a normal embedding of the finite von Neumann algebra
\[
M_\omega=C_\omega/I_\omega\subset M^\omega.
\tag{15}
\]
Its faithful normal trace is \(\tau_\omega=\varphi^\omega|_{M_\omega}\). In the factor case this is the previously defined scalar-limit trace.

**Proof.** The kernel of inclusion on \(C_\omega\) is exactly \(I_\omega\), so the quotient embeds isometrically. Its state is faithful by Lemma 2.1, and is tracial because
\[
|\varphi(x_ny_n-y_nx_n)|
\le\|y_n\|\|[x_n,\varphi]\|\to_\omega0.
\tag{16}
\]
Consequently its \(2\)-norm is the ultralimit of the symmetric seminorm (1).

Here is the completeness argument without assuming a scalar weak limit. Choose a norm-dense sequence of normal states \(\psi_j\). For a fast \(2\)-Cauchy subsequence \(X_r\) of quotient contractions, choose centralizing contraction representatives \(x_r(k)\), with \(\|X_r-X_p\|_2<2^{-p}\) for \(r>p\). Choose nested sets \(A_r\in\omega\), inside \(\{k\ge r\}\), on which
\[
\begin{aligned}
\|[x_r(k),\psi_j]\|&\le1/r&&(j\le r),\\
\|x_r(k)-x_p(k)\|_{\varphi,\#}&\le2^{-p}+2^{-r}&&(p<r).
\end{aligned}
\tag{17}
\]
Each finite collection is available by the ultralimit trace identity and centralizing. Set \(r(k)=\max\{r\le k:k\in A_r\}\), or zero when empty, and \(x(k)=x_{r(k)}(k)\), using \(x_0=0\). Since \(r(k)\to_\omega\infty\), the first line and norm density make \(x\) centralizing. The second line gives \(\|\pi(x)-X_p\|_2\le2^{-p}\). The unit ball is therefore \(2\)-complete.

For a strong Cauchy net in this represented unit ball, convergence on the faithful vector \(\Omega\) makes it \(2\)-Cauchy. Completeness gives a limit in \(M_\omega\). Trace equality makes both its first and adjoint state seminorms converge, so the bounded faithful-state strong* criterion in \(M^\omega\) gives strong convergence to that limit. Kaplansky density now proves that this unit ball, and hence the subalgebra, is strongly closed. It is a von Neumann subalgebra of \(M^\omega\), with the normal restriction of its faithful state. This proves normality of the embedding and finiteness. \(\square\)

## 6. Automorphisms and convergent implementing families

**Theorem 6.1.** A fixed normal automorphism \(\beta\) acts term by term on \(M^\omega\). More generally, if \(\beta_n\to\beta\) in the \(u\)-topology, the sequence action induces a normal automorphism
\[
\Gamma_{(\beta_n)}(\pi(x_n))=\pi(\beta_n(x_n)).
\tag{18}
\]
It restricts to \(\beta\) on the constant copy of \(M\). At separable-predual generality it also preserves \(M_\omega\).

**Proof.** For bounded \(z\in I_\omega\),
\[
\varphi(\beta_n(z_n^*z_n))
\le \|\varphi\circ\beta_n-\varphi\circ\beta\|\|z_n\|^2
+(\varphi\circ\beta)(z_n^*z_n)\to_\omega0.
\tag{19}
\]
The adjoint seminorm has the same estimate. Inverses converge in the \(u\)-topology as well: continuity of inversion for surjective predual isometries follows from its pointwise norm identity, without needing a metric or a separable Banach space. Thus the termwise sequence automorphism preserves \(I_\omega\) in both directions. It preserves its multiplier algebra, so induces a *-automorphism of the quotient. A bijective *-homomorphism between von Neumann algebras is normal: its order inverse preserves the least-upper-bound property of every increasing bounded positive net.

For fixed \(a\in M\), \(u\)-convergence gives \(\beta_n(a)\to\beta(a)\) strong*. Expand each state square norm of their difference; multiplicativity makes the square term \(\beta_n(a^*a)\), and the cross terms involve fixed normal functionals applied to \(\beta_n(a)\). Their limits cancel. The adjoint expansion is the same. This proves the constant restriction.

For a centralizing \(x_n\), the predual identity gives
\[
\|[\beta_n(x_n),\psi]\|
\le\|[x_n,\psi\circ\beta]\|
+2\sup_n\|x_n\|\|\psi\circ\beta_n-\psi\circ\beta\|
\to_\omega0.
\tag{20}
\]
The inverse family gives equality of the invariant subalgebra. \(\square\)

A constant automorphism family is called **liftable**; a convergent variable family is **semi-liftable**. Formula (18) keeps the family in its notation: the limit \(\beta\) alone does not determine that automorphism. The [next lesson](ultraproduct-expectations-and-semilift-ambiguity.md) gives the exact counterexample.

If \(\operatorname{Ad}(u_n)\to\alpha\), the unitaries \(u_n\) belong to \(N_\omega\). Indeed, the only nonautomatic square seminorms of their products with \(z_n\in I_\omega\) are tested by \(\varphi\circ\operatorname{Ad}(u_n)\) or its inverse; these converge in predual norm to the corresponding fixed normal states of \(\alpha\). The estimate (19) applies. Thus \(U=\pi(u_n)\) is a unitary and
\[
\operatorname{Ad}(U)|_M=\alpha.
\tag{21}
\]
This realizes an approximately inner automorphism of \(M\) by an actual inner automorphism in the larger algebra.

## 7. Dense representatives and type I factors

**Lemma 7.1.** If \(A_0\subset M\) is an ultraweakly dense *-subalgebra, every \(X\in M^\omega\) has a bounded multiplier representative \(b_n\in A_0\).

**Proof.** Start with a multiplier representative \(a_n\), uniformly bounded by \(C\). If \(C=0\) use zero. Otherwise Kaplansky density for the norm closure of \(A_0\), followed by norm approximation from \(A_0\), gives \(b_n\in A_0\) with \(\|b_n\|\le2C\) and
\(\|b_n-a_n\|_{\varphi,\#}<1/n\).
The difference belongs to \(I_\omega\subset N_\omega\); hence \(b\) is a multiplier and \(\pi(b)=X\). No assumption that \(A_0\) contains the unit is needed. \(\square\)

**Theorem 7.2.** If \(M=B(H)\) is a countably decomposable type I factor, then every multiplier sequence converges strong* along \(\omega\). The constant embedding is a normal isomorphism \(M\cong M^\omega\).

**Proof.** The finite-dimensional case follows from compactness of bounded operator balls. In infinite dimension \(H\) is separable; choose a basis \(\xi_j\) and the faithful diagonal state
\[
\varphi_0(x)=\sum_{j\ge0}2^{-j-1}\langle\xi_j,x\xi_j\rangle.
\tag{22}
\]
Changing the faithful state does not change (2). Put \(P_m\) for the first \(m\) basis projection and \(q_m=1-P_m\). Then \(\|q_m\|_{\varphi_0,\#}\to0\).

Let \(a\in N_\omega\), and let \(A\) be its bounded ultraweak \(\omega\)-limit. Given a fixed \(j\), Lemma 1.2, applied to \(q_m\) for sufficiently large \(m\), makes both
\[
\|q_ma_n\xi_j\|,\qquad \|q_ma_n^*\xi_j\|
\tag{23}
\]
arbitrarily small on an \(\omega\)-large set. For the first, the nonadjoint seminorm of \(q_ma_n\) includes the square in (23) with coefficient \(2^{-j-1}/2\); for the second use the adjoint seminorm of \(a_nq_m\).

In the finite-dimensional range of \(P_m\), the vectors \(P_ma_n\xi_j\) converge in norm along \(\omega\) to \(P_mA\xi_j\), by ultraweak convergence of their finitely many coefficients. Choose \(m\) also large enough that \(q_mA\xi_j\) is small. Equation (23) then proves \(a_n\xi_j\to_\omega A\xi_j\). The same argument for adjoints gives \(a_n^*\xi_j\to_\omega A^*\xi_j\). Uniform boundedness extends both conclusions from the basis span to every vector.
Thus \(a_n-A\in I_\omega\), and every quotient element is constant. Normality and injectivity of the constant embedding were proved in Section 4. \(\square\)

## 8. Exercises with complete solutions

**Exercise 1.** Verify that the null space in (2) is self-adjoint and product closed.

*Solution.* Adjointing interchanges the two state seminorms. In a faithful normal representation, if \(x_n,y_n\to_\omega0\) strong* with norm bounds \(C,D\), then \(\|x_ny_n\xi\|\le C\|y_n\xi\|\to0\), and \(\|(x_ny_n)^*\xi\|\le D\|x_n^*\xi\|\to0\). Thus the products vanish strong* as well.

**Exercise 2.** In the rank-one example in Section 1, compute the symmetric seminorm of \(p_na_n\) for the state (22).

*Solution.* Since \(p_na_n=a_n\), \(a_n^*a_n=p_0\) and \(a_na_n^*=p_n\). Its squared symmetric seminorm is \((2^{-1}+2^{-n-1})/2\), which tends to \(1/4\), rather than zero. Meanwhile \(\|p_n\|_{\varphi_0,\#}^2=2^{-n-1}\to0\). This proves both the nonideal phenomenon and failure of the multiplier condition.

**Exercise 3.** Why does the diagonal witness in Lemma 1.2 avoid a countable intersection of ultrafilter sets?

*Solution.* For each fixed \(r\), \(B_r\cap\{n\ge r\}\) is an \(\omega\)-large set on which \(r(n)\ge r\). These separate threshold bounds give \(r(n)\to_\omega\infty\). A common intersection over all \(r\) is neither required nor asserted.

**Exercise 4.** Explain why multipliers commute with the coordinate projections \(q_n\).

*Solution.* The element \(mq_n\) lies in \(I_\omega\) and has right support \(q_n\), since \((mq_n)q_n=mq_n\). Centrality of \(q_n\) within \(I_\omega\) makes it also left-supported there. The same argument applies to \(q_nm\), and both equal \(q_nmq_n\). Their coordinate value therefore lies in the unital coordinate algebra \(M\).

**Exercise 5.** Prove faithfulness of the quotient state on a positive element without assuming the state is tracial.

*Solution.* Lift the positive quotient element as \(h=b^*b\) in the multiplier algebra. If its state is zero, the positive operator inequality \(h_n^2\le Ch_n\) gives vanishing of \(\varphi(h_n^2)\). Self-adjointness makes this both strong* seminorms, so \(h\in I_\omega\). The quotient element is zero. No cyclic trace interchange occurs.

**Exercise 6.** Verify that changing a representative outside an \(\omega\)-large set leaves both the quotient and multiplier membership unchanged.

*Solution.* The bounded difference is zero on that set, so its symmetric seminorm has ultralimit zero. It belongs to \(I_\omega\), which is an ideal inside \(N_\omega\) and itself lies in \(N_\omega\). Adding it preserves multiplier membership and the quotient image.

**Exercise 7.** Explain why self-adjointness is used when showing that the coordinate limit in Lemma 3.1 is a multiplier.

*Solution.* The uniform one-sided estimate (9) controls the error in \(za\), giving its first seminorm by (10). For its adjoint, self-adjointness gives \((za)^*=az^*\), whose first seminorm is bounded directly by the null seminorm of \(z^*\). Applying the same argument to \(z^*\) handles \(az\). A one-sided bound on a general nonsymmetric sequence would not supply these adjoint identities.

**Exercise 8.** In Theorem 3.2, why do all the limits \(X_Y\) agree?

*Solution.* They give the same vector limit on \(\Omega\), because the first term of every \(p_Y\) is the same norm. Thus \((X_Y-X_Z)\Omega=0\). Faithfulness of the state implies \(\varphi^\omega((X_Y-X_Z)^*(X_Y-X_Z))=0\) only when \(X_Y=X_Z\). This produces one algebra element controlling every dense cyclic vector.

**Exercise 9.** Prove normality of the constant embedding by increasing positive nets.

*Solution.* If \(a_i\uparrow a\), the image supremum \(Z\) is bounded by \(\iota(a)\). Normality of \(\varphi\) and the vector-state normality of \(\varphi^\omega\) give zero state on the positive difference, as in (13). Faithfulness makes that difference zero, so the embedding preserves every such supremum.

**Exercise 10.** When \(M\) has a faithful normal tracial state, show that \(N_\omega=\ell^\infty(\mathbb N,M)\).

*Solution.* Use that trace to define the unchanged ideal. For bounded \(a_n\), the tracial \(2\)-norm inequalities \(\|a_nz_n\|_2,\|z_na_n\|_2\le\sup_n\|a_n\|\|z_n\|_2\) show preservation on both sides. Thus every bounded sequence is a multiplier. The ideal restriction is needed in the general nontracial construction.

**Exercise 11.** Derive the predual error term in (20).

*Solution.* Replace \(\psi\circ\beta_n\) by the fixed functional \(\psi\circ\beta\) inside \([x_n,\cdot]\). The uniform estimate \(\|[x_n,\rho]\|\le2\|x_n\|\|\rho\|\) bounds the difference by the displayed second term. Normalizing by \(\beta_n^{-1}\) does not change its norm. The fixed commutator and the predual error both tend to zero.

**Exercise 12.** Why is the implementing unitary in (21) allowed to have a nonscalar quotient even though the induced map has a prescribed limit on \(M\)?

*Solution.* Membership in \(N_\omega\) means preservation of strong*-null sequences, rather than scalar-triviality. Its quotient unitary can contain additional asymptotic information. Equation (21) specifies its action on the constant copy of \(M\); it does not determine its action on all varying quotient elements. The tensor-tail counterexample in the next lesson exhibits this distinction.

**Exercise 13.** Produce bounded representatives from a dense *-subalgebra that does not contain \(1\).

*Solution.* Let \(A_0\) be the finite-rank operators in \(B(\ell^2)\), and let \(a_n\) represent \(X\) with bound \(C>0\). Kaplansky approximation in their norm closure, followed by finite-rank norm approximation, gives \(b_n\in A_0\), bounded by \(2C\), with symmetric state error less than \(1/n\). Their difference lies in \(I_\omega\), so they represent the same element and remain multipliers. For the unit itself one can simply use increasing finite-rank projections.

**Exercise 14.** Identify the role of finite-dimensional compactness in Theorem 7.2.

*Solution.* The multiplier condition makes the tails in (23) uniformly small on an \(\omega\)-large set. Within a fixed finite-dimensional range, weak coefficient convergence is norm convergence. Adding the small tails gives norm convergence of each full column and row. Ultraweak convergence alone, without the multiplier tail control, would not give this conclusion.

## References

Adrian Ocneanu's free [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/1/WRAP_Theses_Ocneanu_1982.pdf), thesis, Chapter 5, Sections 5.1–5.2, printed pp.47–52 (PDF pp.61–66), supplies the multiplier criterion, self-adjoint completeness, von Neumann quotient, normal subalgebras and convergent automorphism construction. Section 5.1 assumes separable predual. The local completeness and normality proofs in Sections 1–4 use a faithful normal state and no predual countability; Section 5 explicitly retains separable predual. The multiplier criterion's converse, both state seminorms and the arbitrary strong-Cauchy net are supplied in full. A prescribed restriction to the constant copy does not give uniqueness on varying quotient elements.

Hiroshi Ando and Uffe Haagerup, [*Ultraproducts of von Neumann algebras*](https://arxiv.org/pdf/1212.5457v3), v3, Sections 3.1–3.3, especially Lemmas 3.10 and 3.13 and Propositions 3.14–3.15, provide a separate full corner realization for sigma-finite algebras. The referred left-ideal correspondence in their Theorem 3.9 is not proved in that paper and is not a substitute for the local completeness argument. Kaplansky density, faithful-state topology and type I projection foundations remain explicit prerequisites. Source reading and expression-reuse permissions are recorded separately.
