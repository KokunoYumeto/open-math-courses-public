# Slow reindexing and semi-lift compatibility

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

Fast reindexing makes a centralizing input commute with a prescribed separable algebra. Slow reindexing reverses which sequences are held fixed during the selection: its entire image commutes with the centralizing part of that prescribed algebra. It also makes a semi-lift agree on the image with its constant limit lift. That compatibility survives the counterexample to unrestricted fast equivariance.

Let \(M\ne0\) have separable predual and a faithful normal state \(\varphi\). Use \(M^\omega=N_\omega/I_\omega\), the normal subalgebra \(M_\omega=C_\omega/I_\omega\), and \(E_\omega:M^\omega\to M\) from the [multiplier](multiplier-ultraproducts-and-normal-embeddings.md) and [expectation](ultraproduct-expectations-and-semilift-ambiguity.md) lessons. Write \(\|\cdot\|_\#=\|\cdot\|_{\varphi,\#}\).

## 1. The action condition and the theorem

A semi-lift \(\gamma\) is an actual automorphism of \(M^\omega\), represented by a family \(\gamma_k\to\beta_\gamma\) in the \(u\)-topology:
\[
\gamma(\pi(x_k))=\pi(\gamma_k(x_k)).
\tag{1}
\]
Although \(\beta_\gamma\) does not determine \(\gamma\), the given \(\gamma\) determines \(\beta_\gamma\): it is the restriction of \(\gamma\) to the constant copy of \(M\). Thus
\(\gamma\mapsto\beta_\gamma\) respects composition. Write \(b_\gamma=\beta_\gamma^\omega\) for the constant lift.

**Theorem 1.1.** Let \(P,Q\subset M^\omega\) have separable predual. Let \(H\) be a countable group of semi-lifts preserving \(P\). Assume that \(b_\gamma\in H\) for every \(\gamma\in H\). There is a normal unital injective *-homomorphism \(\Phi:P\to M^\omega\) with
\[
\begin{aligned}
\Phi(x)&=x&&(x\in P\cap M),\\
\Phi(P\cap M_\omega)&\subset M_\omega,\\
\Phi(P)&\subset (Q\cap M_\omega)'\cap M^\omega,\\
E_\omega(a\Phi(x))&=E_\omega(a)E_\omega(x)
&&(x\in P,\ a\in Q),\\
\gamma\Phi(x)&=b_\gamma\Phi(x)=\Phi(b_\gamma(x))
&&(x\in P,\ \gamma\in H).
\end{aligned}
\tag{2}
\]
No factor or trace hypothesis on \(M\) is needed.

The final line concerns \(b_\gamma(x)\) in the domain. It does not require \(\Phi(\gamma(x))=\gamma(\Phi(x))\). The associated constant lifts belong to \(H\), so \(b_\gamma(P)=P\), making the stated expression meaningful.

## 2. Countable data and the first selection

Adjoin \(M\) to \(P,Q\), as in [fast reindexing](fast-reindexing-with-liftable-actions.md#2-countable-data-and-bounded-representatives). The joins have separable predual, and the enlarged \(P\) is \(H\)-invariant because every semi-lift preserves the constant \(M\).

Choose countable unital \(\mathbb Q(i)\)-*-algebras
\(\mathcal A\subset P,\mathcal B\subset Q\), ultraweakly dense, with dense intersections with \(M\) and \(M_\omega\). Make \(\mathcal A\) invariant under \(H\) by including all translates before forming the algebra. Use increasing finite exhausting sets \(\mathcal A_n,\mathcal B_n,H_n\), with \(1\) included, and a norm-dense sequence \(\psi_j\) in \(M_*\).

Choose contractive multiplier representatives \(u_x(k)\) of \(x\in\mathcal A\), bounded by \(\|x\|\), and \(v_a(k)\) of \(a\in\mathcal B\). Use constants for elements of \(M\), and centralizing representatives for elements of \(M_\omega\). Choose one family in (1) for each \(\gamma\); use a constant family when the actual automorphism is a constant lift. The limit restriction is independent of that representative choice.

For each \(x\in\mathcal A\) choose decreasing positive moduli \(\delta_l(x)\) and sets \(W_l(x)\in\omega\) so that
\[
k\in W_l(x),\quad \|z\|\le1,\quad\|z\|_\#<\delta_l(x)
\ \Longrightarrow\
\|u_x(k)z\|_\#+\|zu_x(k)\|_\#<1/l.
\tag{3}
\]
These are the previously proved multiplier moduli.

Choose an inner index \(p(n)\ge n\) satisfying this finite list:

1. \(p(n)\in W_l(x)\) for \(x\in\mathcal A_n,\ l\le n\).
2. All addition, adjoint and multiplication discrepancies for operands in \(\mathcal A_n\), and scalar discrepancies for the first \(n\) rational complex scalars, have symmetric seminorm below \(1/n\) at \(p(n)\).
3. \(\|[u_x(p(n)),\psi_j]\|<1/n\) for \(x\in\mathcal A_n\cap M_\omega,\ j\le n\). Also require \(\|[u_x(p(n)),a]\|_\#<1/n\) for these \(x\) and \(a\in\mathcal B_n\cap M\).
4. For \(x\in\mathcal A_n,\ a\in\mathcal B_n,\ j\le n\),
\[
|\psi_j(E_\omega(a)(u_x(p(n))-E_\omega(x)))|<1/n.
\tag{4}
\]
5. For every constant lift \(b=\beta^\omega\) among the finitely many associated lifts being tested, and \(x\in\mathcal A_n\),
\[
\|\beta(u_x(p(n)))-u_{b(x)}(p(n))\|_\#<1/n.
\tag{5}
\]

**Lemma 2.1.** This finite selection is possible.

**Proof.** The first condition uses (3). Every algebraic discrepancy in the second represents zero, hence is in \(I_\omega\). The third uses the centralizing representative and the fact that centralizing sequences commute strong* with fixed operators. For the fourth, \(u_x(k)\to_\omega E_\omega(x)\) ultraweakly and the coefficient \(E_\omega(a)\) is fixed in \(M\). The fifth discrepancy represents zero by the definition of a constant lift. Each condition therefore holds on an \(\omega\)-large set; their finite intersection with \(\{k\ge n\}\) is nonempty. \(\square\)

This selection fixes the operators \(u_x(p(n))\) in \(M\). The second selection will then let the outer coordinate grow while these operators stay fixed.

## 3. The second selection and the slow index

Choose decreasing \(V_n\in\omega\), with \(V_n\subset\{k\ge n\}\), such that for \(k\in V_n\):
\[
\begin{aligned}
\|[u_x(p(n)),v_a(k)]\|_\#&<1/n
&&(x\in\mathcal A_n,\ a\in\mathcal B_n\cap M_\omega),\\
|\psi_j((v_a(k)-E_\omega(a))u_x(p(n)))|&<1/n
&&(x\in\mathcal A_n,\ a\in\mathcal B_n,\ j\le n),\\
\|\gamma_k(u_x(p(n)))-\beta_\gamma(u_x(p(n)))\|_\#&<1/n
&&(x\in\mathcal A_n,\ \gamma\in H_n).
\end{aligned}
\tag{6}
\]
Include the associated constant lifts in the finite action tests as needed.

**Lemma 3.1.** Such sets exist, and they can be chosen with empty total intersection.

**Proof.** In the first line, \(v_a(k)\) is centralizing, so it commutes strong* with the fixed element \(u_x(p(n))\). In the second line, its ultraweak limit is \(E_\omega(a)\), and the right factor and functional are fixed. In the last line, \(u\)-convergence of the automorphism family implies strong* convergence on every fixed element. All finitely many conditions hold on \(\omega\)-large sets. Intersect with the preceding \(V_{n-1}\) and \(\{k\ge n\}\). The latter restriction makes \(\bigcap_n V_n=\varnothing\). \(\square\)

Put \(V_0=\mathbb N\), define
\[
r(k)=\max\{n\ge1:k\in V_n\},
\qquad q(k)=p(r(k)),
\tag{7}
\]
and use \(r(k)=0,p(0)=1\) if the set is empty. The maximum is finite because \(r(k)\le k\). For each fixed \(n\), the set \(V_n\) makes \(r(k)\ge n\), so \(r(k)\to_\omega\infty\). Equivalently, on the band \(V_n\setminus V_{n+1}\) the chosen operator is \(u_x(p(n))\). This includes the initial band \(V_0\setminus V_1\), which has no effect on any ultralimit.

## 4. Multiplier membership and the map

Set
\[
w_x(k)=u_x(q(k)),\qquad \Phi_0(x)=\pi(w_x),
\quad x\in\mathcal A.
\tag{8}
\]

**Lemma 4.1.** Every \(w_x\) is a multiplier. If \(x\in\mathcal A\cap M_\omega\), it is centralizing along \(\omega\).

**Proof.** Fix \(x,l\), and choose \(n_0\) so \(x\in\mathcal A_n\) and \(n\ge l\) whenever \(n\ge n_0\). On the \(\omega\)-large set where \(r(k)\ge n_0\), the selected \(p(r(k))\) belongs to \(W_l(x)\). The fixed modulus \(\delta_l(x)\) in (3) therefore controls multiplication at every such outer coordinate. If \(z_k\in I_\omega\) is a contraction sequence, its seminorm is below that modulus on another \(\omega\)-large set. Both product seminorms have ultralimit at most \(1/l\). Let \(l\to\infty\) and rescale general bounded null sequences. This proves \(w_x\in N_\omega\).

For centralizing \(x\), the third first-selection test gives
\(\|[w_x(k),\psi_j]\|<1/r(k)\) on the large set where that datum is included. Norm density and the bound \(2\|x\|\|\psi\|\) extend this to every normal functional. \(\square\)

The algebraic tests make \(\Phi_0\) a unital rational *-homomorphism, with \(\|\Phi_0(x)\|\le\|x\|\). Combining (4) and the second line of (6) gives, for fixed \(x,a,j\) and sufficiently high levels,
\[
|\psi_j(v_a(k)w_x(k)-E_\omega(a)E_\omega(x))|
<2/r(k).
\tag{9}
\]
Thus
\[
E_\omega(a\Phi_0(x))=E_\omega(a)E_\omega(x).
\tag{10}
\]
Taking \(a=1\) shows state preservation and, by applying it to \(x^*x\) and \(xx^*\), preservation of the symmetric state seminorm.

The first line of (6) makes the full image commute with \(\mathcal B\cap M_\omega\). Lemma 4.1 places centralizing inputs in \(M_\omega\). Constants in \(\mathcal A\cap M\) are fixed by their chosen representatives.

For actions, the last line of (6) gives
\[
\gamma\Phi_0(x)=b_\gamma\Phi_0(x).
\tag{11}
\]
Equation (5), sampled at the same selected inner index on both sides, gives
\[
b_\gamma\Phi_0(x)=\Phi_0(b_\gamma(x)).
\tag{12}
\]
The first comparison uses \(\gamma_k\) at the actual outer coordinate \(k\); it does not replace it by \(\gamma_{q(k)}\).

## 5. Normal extension and an explicit example

The [faithful-state extension lemma](fast-reindexing-with-liftable-actions.md#lemma-5-1) applies: norm closure first, then bounded Kaplansky approximation and the exact symmetric state isometry give a unique normal injective *-homomorphism on \(P\). Constants are fixed by normal density. The image of \(P\cap M_\omega\) stays in the normal subalgebra \(M_\omega\). The commutation conclusion extends from the dense centralizing intersections because relative commutants are strongly closed. Equation (10) extends separately in \(x\) and \(a\) by normality. Equations (11)–(12) extend by normality of all automorphisms. This proves Theorem 1.1, including restriction back from the enlarged \(P,Q\).

The [Pauli example](ultraproduct-expectations-and-semilift-ambiguity.md#proposition-5-1) shows why the action condition matters. In \(R=\bigotimes_{k\ge1}(M_2,\operatorname{tr}_2)\), let \(X,Z\in R_\omega\) come from Pauli operators in leg \(k\), and let \(\gamma=\operatorname{Ad}(Z)\). Then \(\beta_\gamma=\mathrm{id}\). For \(P=Q=M_2(X,Z)\), replace leg \(k\) by leg \(\lfloor\sqrt k\rfloor\) in the representatives of its matrix generators. Their matrix relations remain exact, giving an injective map of \(P\). The new leg tends to infinity, so the images remain centralizing. For all sufficiently large \(k\), it differs from leg \(k\), so the image commutes with \(Q\) and is fixed by \(\gamma\). Thus
\[
\gamma\Phi(X)=\Phi(X)=\Phi(b_\gamma(X)),
\qquad
\Phi(\gamma(X))=-\Phi(X).
\tag{13}
\]
This supplies the slow compatibility and exhibits the failure of the stronger equivariance condition in the same example.

## 6. Exercises with complete solutions

**Exercise 1.** Why is \(\beta_\gamma\) unique even though a convergent limit does not determine its semi-lift?

*Solution.* The chosen family acts as its limit on every constant \(a\in M\). Hence \(\beta_\gamma(a)=\gamma(a)\). An actual \(\gamma\) fixes that restriction, so every family representing it has the same limit. The reverse implication fails: different semi-lifts can have that same restriction.

**Exercise 2.** What purpose does the hypothesis \(b_\gamma\in H\) serve?

*Solution.* It ensures \(b_\gamma(P)=P\), so \(\Phi(b_\gamma(x))\) is defined. It also allows a countable algebra invariant under all those constant lifts and their finite equivariance tests. Invariance under \(\gamma\) alone would not imply invariance under its different constant lift.

**Exercise 3.** Explain why the first weak-limit test uses \(E_\omega(a)\) rather than \(v_a(k)\).

*Solution.* The first selection varies the inner index while fixing \(n\). The coefficient \(E_\omega(a)\) is an operator of \(M\) independent of that index, so ultraweak convergence of \(u_x\) gives (4). After \(p(n)\) is fixed, the second selection varies the outer coordinate and replaces \(v_a(k)\) by that expectation, yielding the second error in (9).

**Exercise 4.** Why does the second commutator test apply to every \(x\), rather than only centralizing \(x\)?

*Solution.* Its varying sequence is \(v_a(k)\), with \(a\in Q\cap M_\omega\). That sequence is centralizing and therefore commutes strong* with each fixed \(u_x(p(n))\), regardless of whether \(x\) is centralizing. This gives commutation of the full image with the centralizing part of \(Q\).

**Exercise 5.** Verify that every coordinate has a finite level in (7).

*Solution.* Membership in \(V_n\) implies \(k\ge n\), so only the finitely many levels \(n\le k\) are possible. Nestedness makes those levels an initial segment. If it is empty use level zero; otherwise its last member is the required maximum.

**Exercise 6.** Why is \(r(k)\to_\omega\infty\) sufficient for the quotient conclusions?

*Solution.* For each threshold \(n\), the \(\omega\)-large set \(V_n\) has \(r(k)\ge n\). Thus every fixed datum is tested on an \(\omega\)-large set with arbitrarily small error. Ordinary convergence of \(r(k)\) is unnecessary for an ultrafilter quotient.

**Exercise 7.** Derive multiplier membership from the fixed moduli.

*Solution.* Fix \(x,l\). On a large set the chosen inner index lies in \(W_l(x)\); then every small contraction input is controlled by the same \(\delta_l(x)\). A null sequence of inputs satisfies that modulus on another large set. Both product seminorms have ultralimit at most \(1/l\). Letting \(l\) increase proves both ideal-preservation conditions.

**Exercise 8.** Why is it wrong to evaluate the semi-lift at the selected index \(q(k)\) when acting on the final representative?

*Solution.* Formula (1) applies \(\gamma_k\) to the coordinate actually indexed by \(k\). Its input happens to be \(u_x(q(k))\), but that does not change the automorphism index. The slow selection first fixes this input, then makes \(\gamma_k\) close to its limit on it. Replacing \(k\) by \(q(k)\) would describe a different family action.

**Exercise 9.** Prove injectivity without requiring the automorphisms of \(H\) to preserve \(\varphi^\omega\).

*Solution.* Equation (10) with \(a=1\) makes \(\Phi\) preserve \(\varphi^\omega\), independently of any action. If \(\Phi(x)=0\), multiplicativity gives \(\varphi^\omega(x^*x)=\varphi^\omega(\Phi(x)^*\Phi(x))=0\). Faithfulness makes \(x=0\). No state invariance of the automorphisms enters.

**Exercise 10.** Explain the normal extension of the commutation conclusion.

*Solution.* Each dense input image commutes with the dense \*-algebra in \(Q\cap M_\omega\), hence with its von Neumann closure by separate ultraweak continuity. The relative commutant of that closure is strongly closed. Bounded strong\* approximation of a general input and the normal extension therefore keep its image in that commutant.

**Exercise 11.** Check the Pauli slow-index example.

*Solution.* The indices \(k\) and \(\lfloor\sqrt k\rfloor\) are distinct for \(k\ge3\). Operators in distinct tensor legs commute. The reindexed Pauli pair still anticommutes within its single new leg, so its unital \(M_2\) relations persist. Since the new leg tends to infinity, all finite-head commutators eventually vanish; trace approximation gives centralizing sequences. These facts prove every assertion in (13).

**Exercise 12.** Recover scalar independence for a factor when the input \(x\) is centralizing.

*Solution.* Then \(E_\omega(x)=\tau_\omega(x)1\). Applying \(\varphi\) to (2) gives \(\varphi^\omega(a\Phi(x))=\varphi^\omega(a)\tau_\omega(x)\). If \(a\) is centralizing too, this is the trace identity on \(M_\omega\). The full expectation identity retains the ordered product for general \(x\).

## References

The free construction source is Adrian Ocneanu, [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/1/WRAP_Theses_Ocneanu_1982.pdf), thesis, Chapter 5, Section 5.4, Slow Reindexation Trick, printed pp.55–56 (PDF pp.69–70). Its action condition includes each semi-lift's constant limit lift. The proof first chooses fixed inner operators, then chooses outer neighborhoods for central commutation, ultraweak product tests and convergence of the chosen automorphism families. Its final extension steps are referred to the fast lemma.

Here all multiplier, algebraic, normal-extension and action estimates are written out. The equality compares the actual semi-lift on the new image with its constant limit lift, and with the image of that limit lift's action on the domain. It does not impose equivariance with the original semi-lift on the domain. The full nonfactor and nontracial setting is retained; the tensor-tail example checks the distinction directly.
