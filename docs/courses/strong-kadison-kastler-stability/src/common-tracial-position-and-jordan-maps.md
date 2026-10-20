# Common tracial position and Jordan maps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two close II\(_1\) factors can be moved, after a change of representation, into a position in which one vector is the trace vector of both, and their common hyperfinite subfactor acts in the same way on the left and on the right. This *common tracial position* is a theorem of Cameron, Christensen, Sinclair, Smith, White and Wiggins [CCSSWW, Lemma 4.10], used here without proof (Proposition 1.2). In common position, the two modular conjugations \(J_M\) and \(J_N\) are close in norm, with an explicit constant (Lemma 2.2). The lesson ends with Herstein's lemma: a surjective Jordan homomorphism onto a factor is a homomorphism or an antihomomorphism (Lemma 3.1). The next lesson combines these facts with the boundary of the earlier lessons to build an isomorphism between close finite factors [OpenAI-289, Section 5].

We use: [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md) (Lemmas 2.1 and 3.1); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (the notion of an injective von Neumann algebra); from [Integration for a trace](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications#3-the-commutation-theorem), Theorem 3.1 (the commutation theorem \(JMJ=M'\) on the trace Hilbert space) and [Theorem 9.1](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications#9-conditional-expectations-that-preserve-a-trace) (trace-preserving conditional expectations).

## 1. Standard tracial position

Let \(P\subseteq B(K)\) be a II\(_1\) factor with trace \(\tau_P\). We say that \(P\) is in *standard tracial position* with the unit vector \(\Omega\) when \(\Omega\) is cyclic for \(P\) and \(\langle x\Omega,\Omega\rangle=\tau_P(x)\) for \(x\in P\). Then \(x\Omega\mapsto x\) identifies \(K\) with the trace Hilbert space \(L^2(P,\tau_P)\), and \(\Omega\) is also separating. The *conjugation* of \(P\) is the antiunitary involution \(J_P\) with \(J_P(x\Omega)=x^*\Omega\). By the commutation theorem, \(J_PPJ_P=P'\), and \(J_Py^*J_P\) is right multiplication by \(y\in P\): \(J_Py^*J_P(x\Omega)=xy\Omega\).

For a von Neumann subalgebra \(Q\subseteq P\) let \(e_Q\) be the orthogonal projection onto the closure of \(Q\Omega\). If \(E_Q\) is the trace-preserving conditional expectation of Theorem 9.1, then \(e_Q(x\Omega)=E_Q(x)\Omega\) for \(x\in P\), because \(E_Q\) is the orthogonal projection of \(L^2(P,\tau_P)\) onto the closure of \(Q\Omega\).

**Lemma 1.1** (the commutant of a basic construction). In standard tracial position, the commutant of \((P\cup\{e_Q\})''\) is \(J_PQJ_P\).

**Proof.** An element of \(P'\) is \(J_Py^*J_P\) for some \(y\in P\), and it sends \(\Omega\) to \(y\Omega\). If it commutes with \(e_Q\), then \(y\Omega=e_Q(y\Omega)=E_Q(y)\Omega\), so \(y=E_Q(y)\in Q\) because \(\Omega\) is separating. Conversely, for \(r\in Q\), right multiplication by \(r\) and by \(r^*\) maps \(Q\Omega\) into itself, so the closure of \(Q\Omega\) reduces it, and it commutes with \(e_Q\). \(\square\)

The following theorem is used without proof. Here the near inclusions are those of [Close operator algebras](close-operator-algebras.md), Definition 1.2.

**Proposition 1.2** (common tracial position [CCSSWW, Lemma 4.10]). Let \(M,N\) be II\(_1\) factors with separable preduals acting nondegenerately on one Hilbert space, with \(M\subset_gN\) and \(N\subset_gM\), where \(0<g<1.74\cdot10^{-13}\). Suppose that an injective von Neumann subalgebra \(R\subseteq M\cap N\) satisfies \(R'\cap M\subseteq R\). There are faithful normal representations \(\pi:M\to B(K)\) and \(\rho:N\to B(K)\), a unit vector \(\Omega\in K\) and a number \(\beta<50948\sqrt g\) such that:

1. \(\pi(M)\) and \(\rho(N)\) are in standard tracial position with the vector \(\Omega\);
2. \(\pi|_R=\rho|_R\), and \(\pi(M)\subset_\beta\rho(N)\), \(\rho(N)\subset_\beta\pi(M)\);
3. \(\|\pi(x)-\rho(y)\|\le\beta+\|x-y\|\) for contractions \(x\in M\) and \(y\in N\);
4. if \(e_R\) is the projection onto the closure of \(\pi(R)\Omega\), then \((\pi(M)\cup\{e_R\})''=(\rho(N)\cup\{e_R\})''\).

Since \(K\) is the trace Hilbert space of \(M\), it is separable.

After applying Proposition 1.2 we suppress \(\pi\) and \(\rho\) and write \(M,N\) for the images. Normalizing approximants (Lemma 1.4 of [Close operator algebras](close-operator-algebras.md)) gives \(d(M,N)\le2\beta\).

## 2. The common right action and the two conjugations

**Lemma 2.1** (common right action). In the situation of Proposition 1.2,
\[
J_MrJ_M=J_NrJ_N\qquad(r\in R).
\]
Consequently \(T=J_NJ_M-I\) commutes with every \(r\in R\) and every \(J_MrJ_M\), \(r\in R\).

**Proof.** By Lemma 1.1 and part (4) of Proposition 1.2, \(J_MRJ_M\) and \(J_NRJ_N\) are both the commutant of the same algebra, so they are equal as sets. For \(r\in R\), the operators \(J_MrJ_M\) and \(J_NrJ_N\) both send \(\Omega\) to \(r^*\Omega\), and both lie in this common algebra, which is contained in \(M'\). The vector \(\Omega\) is cyclic for \(M\), hence separating for \(M'\), so the two operators are equal. Then \(J_NJ_Mr=J_N(J_MrJ_M)J_M\)\(=J_N(J_NrJ_N)J_M=rJ_NJ_M\), and for \(s=J_MrJ_M=J_NrJ_N\), \(J_NJ_Ms=J_NrJ_M=sJ_NJ_M\). \(\square\)

**Lemma 2.2** (the two conjugations are close). Let \(M,N\subseteq B(K)\) be II\(_1\) factors in common standard tracial position with the vector \(\Omega\), on a separable Hilbert space. Suppose that \(R\subseteq M\cap N\) is a subfactor of \(M\) as in Lemma 2.1 of [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md), and that \(J_MrJ_M=J_NrJ_N\) for \(r\in R\). If \(d(M,N)<b\), then
\[
\|J_M-J_N\|\le768\,b .
\]

**Proof.** The operator \(T=J_NJ_M-I\) is linear and, by the computation at the end of the proof of Lemma 2.1, commutes with the left action of \(R\) and with right multiplications by elements of \(R\), which are the operators \(J_MrJ_M\). For \(x\in M_1\) choose \(y\in N_1\) with \(\|x-y\|<b\). Since \(J_N(y^*\Omega)=y\Omega\),
\[
\begin{aligned}
Tx\Omega&=J_Nx^*\Omega-x\Omega\\
&=J_N(x^*-y^*)\Omega+(y-x)\Omega,
\end{aligned}
\]
so \(\|Tx\Omega\|<2b\), and \(|\langle Ta\Omega,c\Omega\rangle|<2b\) for \(a,c\in M_1\). Lemma 3.1 of [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md) gives \(\|T\|\le768b\). Finally \(J_N-J_M=TJ_M\) and \(J_M\) is a norm-preserving bijection, so \(\|J_N-J_M\|=\|T\|\). \(\square\)

## 3. Jordan homomorphisms into a factor

For elements of an algebra put \(x\circ y=\frac12(xy+yx)\). A linear map \(\theta\) between algebras is a *Jordan homomorphism* if \(\theta(x\circ y)=\theta(x)\circ\theta(y)\) for all \(x,y\). A homomorphism and an antihomomorphism (\(\theta(xy)=\theta(y)\theta(x)\)) are Jordan homomorphisms. A von Neumann algebra \(N\) is *prime* if \(xNy=\{0\}\) implies \(x=0\) or \(y=0\). A factor is prime: if \(y\ne0\), the closed span of \(NyK\) is the range of the central support of the range projection of \(y\), which is \(1\) in a factor; if \(x\) vanishes on it, then \(x=0\).

**Lemma 3.1** (Herstein's orientation lemma). Let \(\theta:\mathcal A\to N\) be a surjective linear Jordan homomorphism from a unital complex algebra onto a factor \(N\). Then \(\theta\) is a homomorphism or an antihomomorphism.

**Proof.** *Triple products.* A direct expansion gives \(xyx=2x\circ(x\circ y)-(x\circ x)\circ y\), so \(\theta(xyx)=\theta(x)\theta(y)\theta(x)\). Replacing \(x\) by \(x+z\) gives
\[
\begin{aligned}
\theta(xyz+zyx)&=\theta(x)\theta(y)\theta(z)\\
&\quad +\theta(z)\theta(y)\theta(x).
\end{aligned}
\]

*Each pair is oriented.* Fix \(a,b\in\mathcal A\) and put \(A=\theta(a)\), \(B=\theta(b)\), \(D=\theta(ab)\), \(E=\theta(ba)\). From \(ab+ba=2a\circ b\) we get \(E=AB+BA-D\). Put \(h=D-AB\) and \(k=D-BA\), so that \(E=BA-h\) and \(BA-AB=h-k\). For \(c\in\mathcal A\) with \(C=\theta(c)\), compute \(\theta(ab\,c\,ba+ba\,c\,ab)\) in two ways. The polarized identity gives \(DCE+ECD\). Writing \(ab\,c\,ba=a(bcb)a\) and \(ba\,c\,ab=b(aca)b\) gives \(ABCBA+BACAB\). Substituting \(D=AB+h\) and \(E=BA-h\) and comparing,
\[
\begin{aligned}
&(BA-AB)Ch+hC(BA-AB)\\
&\qquad -2hCh=0,
\end{aligned}
\]
that is, \(hCk+kCh=0\). Since \(\theta\) is onto, this holds for every \(C\in N\). Take \(C=C_1kC_2\) with \(C_1,C_2\in N\). Using the identity for \(C_2\) and then for \(C_1\),
\[
kC_1kC_2h=-kC_1hC_2k=hC_1kC_2k,
\]
so \(2hC_1kC_2k=0\). If \(k\ne0\), primeness gives \(hC_1k=0\) for every \(C_1\), and then \(h=0\). So for each pair \((a,b)\), either \(\theta(ab)=\theta(a)\theta(b)\) or \(\theta(ab)=\theta(b)\theta(a)\).

*One orientation.* A group is not the union of two proper subgroups: if \(x\in G_1\setminus G_2\) and \(y\in G_2\setminus G_1\), then \(x+y\) lies in neither. For fixed \(a\), the sets of \(b\) satisfying each of the two identities are additive subgroups covering \(\mathcal A\), so one of them is all of \(\mathcal A\). Then the sets of \(a\) for which the first, respectively the second, identity holds for every \(b\) are additive subgroups covering \(\mathcal A\), and one of them is all of \(\mathcal A\). \(\square\)

## 4. Exercises

**Exercise 4.1.** Verify the identity \(xyx=2x\circ(x\circ y)-(x\circ x)\circ y\).

**Exercise 4.2.** Show that the transpose \(x\mapsto x^{\rm T}\) of \(M_2(\mathbb C)\) is an antihomomorphism and a Jordan homomorphism, and that \(\|x^{\rm T}-x\|=1\) for the matrix unit \(x=e_{12}\).

**Exercise 4.3.** In standard tracial position, show that \(J_P\) is isometric and that \(J_Py^*J_P(x\Omega)=xy\Omega\) for \(x,y\in P\).

**Exercise 4.4.** Show that the conclusion of Lemma 3.1 can fail when \(N\) is not prime: on \(\mathcal A=N=M_2(\mathbb C)\oplus M_2(\mathbb C)\), find a Jordan automorphism that is neither multiplicative nor antimultiplicative.

**Exercise 4.5.** Let \(M\) be a II\(_1\) factor in standard tracial position and \(u\in M\) unitary. Show that \(uJ_MuJ_M\) fixes \(\Omega\) and commutes with \(J_M\).

## 5. Solutions

**Solution 4.1.** \(x\circ(x\circ y)=\frac14(x^2y+2xyx+yx^2)\) and \((x\circ x)\circ y=\frac12(x^2y+yx^2)\).

**Solution 4.2.** \((xy)^{\rm T}=y^{\rm T}x^{\rm T}\), so \((xy+yx)^{\rm T}=y^{\rm T}x^{\rm T}+x^{\rm T}y^{\rm T}\). For \(x=e_{12}\), \(x^{\rm T}-x=e_{21}-e_{12}\) is the rotation \(\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), a unitary, so its norm is \(1\).

**Solution 4.3.** \(\|x^*\Omega\|^2=\tau(xx^*)=\tau(x^*x)=\|x\Omega\|^2\), so \(J_P\) is isometric on the dense set \(P\Omega\). Then \(J_Py^*J_P(x\Omega)=J_P(y^*x^*\Omega)=xy\Omega\).

**Solution 4.4.** \(\theta(x\oplus y)=x\oplus y^{\rm T}\) preserves \(\circ\) in each summand. With \(x=e_{12}\oplus e_{12}\) and \(z=e_{21}\oplus e_{21}\), \(\theta(xz)=e_{11}\oplus e_{11}\), while \(\theta(x)\theta(z)=e_{11}\oplus e_{22}\) and \(\theta(z)\theta(x)=e_{22}\oplus e_{11}\). The center of \(N\) contains \(1\oplus0\), and \((1\oplus0)N(0\oplus1)=\{0\}\), so \(N\) is not prime.

**Solution 4.5.** \(J_MuJ_M\) is right multiplication by \(u^*\), so \(uJ_MuJ_M\Omega=uu^*\Omega=\Omega\). Also \(J_M(uJ_MuJ_M)J_M=J_MuJ_Mu\), and \(J_MuJ_M\in M'\) commutes with \(u\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
- [CCSSWW] J. Cameron, E. Christensen, A. M. Sinclair, R. R. Smith, S. White, A. D. Wiggins, Kadison–Kastler stable factors, Duke Mathematical Journal 163 (2014), 2639–2686; Lemma 4.10 in arXiv version 3. https://arxiv.org/abs/1209.4116v3
