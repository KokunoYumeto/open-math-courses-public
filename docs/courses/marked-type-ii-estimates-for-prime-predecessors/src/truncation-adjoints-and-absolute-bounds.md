# Truncation, adjoints and absolute bounds

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The operator identity of [*Lifespans and the memory space*](lifespans-and-the-memory-space.md) writes the model moment as a matrix element of a product of ghost and edge operations. To bound it by a product of operator norms, three preparations are needed. The memory must be truncated to a finite size, so that counting choices of particles costs only a power of \(L\). The adjoints of the operations must be identified, because norms are bounded by a weighted Schur test that uses row sums of an operation and of its adjoint. And the ghost operations, together with all edges, need absolute bounds; the ghost operations are bounded by a constant, the edges by a power of \(L\). The signed bounds that give decay are proved in the next two lessons.

**Prerequisites.** [*Lifespans and the memory space*](lifespans-and-the-memory-space.md); [*Independent residue lines*](independent-residue-lines.md), Lemmas 1.1 and 2.1.

Throughout, the archimedean root and the parameters of Lesson 8 are fixed, \(\rho=3/4\), and \(B=\lceil L^2\rceil\). Let \(\Pi_B\) be the orthogonal projection of \(\mathscr H\) onto the states whose memories have total size at most \(B\), and \(\mathscr H_B=\Pi_B\mathscr H\).

## 1. Truncating the memory

**Lemma 1.1.** For every fixed \(A\), inserting \(\Pi_B\) before and after every operation in the history sum of Theorem 4.1 of Lesson 12 (histories with globally distinct births) changes that sum by \(O(L^{-AN})\).

**Proof.** The insertion removes exactly the histories in which the memory exceeds \(B\) at some moment. The memory grows only by stores, at most \(K\) per edge and so at most \(KN\) in all, and by ghost creations. A removed history therefore has at least \(B-KN\) ghost creations. Let \(\mathcal M_2\) be the sum over all histories with distinct births of the absolute value of their weight times \(2^{\#\text{ghost creations}}\). The removed histories contribute at most \(2^{-(B-KN)}\mathcal M_2\).

To bound \(\mathcal M_2\), use the lifespan description. For a prime never in a list, fix the first ghost endpoint \(a\); the possible second endpoints \(c>a\) with the same line form a sequence \(c_1<c_2<\cdots\), and the \(k\)th of them comes with \(k-1\) hits strictly inside, each damped by \(q_j\le\frac12\). Their sum is at most \(\sum_k2^{1-k}=2\), so the absolute orphan sum, with the factor \(2\), is at most \(2(N+1)\cdot2\cdot2/(p+1)\le8(N+1)/p\), using \(b'_p\ge\frac12\). The product over all primes is at most \(\exp(8(N+1)\sum_p1/p)\)\(\le\exp(8K(N+1))\). A prime that is in some list has at most \((N+2)^2\) choices of ghost endpoints, and there are at most \((N+1)KM\) such primes. Multiplying by the data budget \(\exp(O_K(L^{0.73}))\) of Lemma 2.1 of Lesson 11 gives \(\mathcal M_2\le\exp(O_K(L^{0.74}))\). Since \(B-KN\ge L^2/2\), the removed part is at most \(2^{-L^2/2}\exp(O_K(L^{0.74}))\). \(\square\)

## 2. Operations, adjoints and the Schur test

Each operation \(O\) of Lesson 12 is a finite sum over discrete choices and integrals over new prime values, and so has a **joint measure** \(\Gamma_O\) on pairs (input state, output state): \(\langle\phi,O\psi\rangle=\iint\overline{\phi(s)}\,\psi(s')\,d\Gamma_O(s,s')\), where \(\Gamma_O\) records the input measure, the choice measures and the coefficients. The adjoint \(O^*\) has the transposed and conjugated joint measure. We say that \(O^*\) is **again an operation** of a stated kind when its joint measure is that of such an operation read in the reverse direction.

**Lemma 2.1 (weighted Schur test).** Let \(h>0\) be a function on states. Suppose that for every input state \(s\) the sum over the choices of \(O\) of \(|\text{coefficient}|\cdot h(\text{output})\) is at most \(R\,h(s)\), and that the same holds for \(O^*\) with a constant \(C\). Then \(\|O\|\le\sqrt{RC}\).

**Proof.** Let \(|\Gamma_O|\) be the joint measure with coefficients replaced by their moduli. By Cauchy's inequality,

\[
\begin{aligned}
&|\langle\phi,O\psi\rangle|\\
&\quad\le\Bigl(\iint|\phi(s)|^2\frac{h(s')}{h(s)}d|\Gamma_O|\Bigr)^{1/2}\\
&\qquad\times\Bigl(\iint|\psi(s')|^2\frac{h(s)}{h(s')}d|\Gamma_O|\Bigr)^{1/2}.
\end{aligned}
\]

The first integral is at most \(R\|\phi\|^2\) by the row hypothesis, and the second at most \(C\|\psi\|^2\) by the hypothesis for \(O^*\), whose joint measure is the transpose of \(\Gamma_O\). \(\square\)

Restricting an operation to \(\mathscr H_B\), or inserting a factor of modulus at most \(1\) on its choices, can only decrease both kinds of sums.

**Lemma 2.2 (factorials).** In a memory of size \(k+a\) with the measure \(\lambda^{\otimes(k+a)}/(k+a)!\) on ordered tuples,

\[
\begin{gathered}
\frac{\binom{k+a}a}{(k+a)!}=\frac1{k!\,a!},\\
\frac{\binom{k+a}a\,a!}{(k+a)!}=\frac1{k!}.\quad(2.1)
\end{gathered}
\]

The first identity says that choosing an unordered set of \(a\) particles to delete, from a symmetric memory of size \(k+a\), has the same joint measure as appending an unordered batch of \(a\) particles to a memory of size \(k\) with the measure \(\lambda^{\otimes a}/a!\). The second says that retrieving \(a\) particles into \(a\) prescribed ordered slots has the joint measure \(\lambda^{\otimes k}/k!\) of the remaining memory times the measure of the retrieved particles. The identities themselves are arithmetic; their meaning comes from the symmetry of the test functions, which makes all \(\binom{k+a}a\) choices of indices contribute equally.

**Lemma 2.3 (the adjoint of a ghost operation).** \(\mathcal G_j^*\) is again a ghost operation at the visit \(j\), with deletion coefficient \(-\eta_jV_i/\rho\), creation coefficient \(-\eta_j/\rho\) and survival coefficient \(q_j/\rho^2\), in each group \(i\).

**Proof.** Consider one group. A history of \(\mathcal G_j\) from a memory \(Z\cup A\) to \(Z\cup B'\) deletes the hitting particles \(A\) and creates the batch \(B'\), both anchored at the lines of \(z_j\), while the particles of \(Z\) stay; the hitting particles of \(Z\) contribute \((q_j/\rho^2)^{h(Z)}\). By (2.1), the joint measure is \(\lambda^{\otimes k}/k!\) on \(Z\) times \(\nu^{\otimes a}/a!\) on the primes of \(A\) times \(\nu^{\otimes l}/l!\) on the primes of \(B'\), the anchors being forced, with coefficient \((-\eta_j/\rho)^a(-\eta_jV_i/\rho)^l(q_j/\rho^2)^{h(Z)}\). This expression is symmetric under exchanging \((A,a)\) with \((B',l)\) provided the two coefficients are exchanged. \(\square\)

**Lemma 2.4 (the adjoint of an edge operation).** Split \(\mathcal E_j\) according to the set \(S\) of groups that store and the set \(I\) of groups that promote. The adjoint of the piece \((S,I)\) is the piece \((I,S)\) of the reversed edge: the reversed edge goes from the target to the source, has the conjugate multiplier, stores in the groups of \(I\) with coefficient \(1/V_i\), promotes in the groups of \(S\) with coefficient \(1\), and pays \(\rho\) for the hits of the old memory at its source and of the new memory at its target.

**Proof.** In one group with a promotion, the input memory has size \(k+1\) and the output size \(k\). By the second identity of (2.1) with \(a=1\), the joint measure is \(\lambda^{\otimes k}/k!\) on the remaining particles times \(\nu(p)\) for the promoted prime, its anchor being forced to the line of the target. Read backwards, this is the measure of a store from the target's last slot, whose entry has the list measure \(\nu(p)\), into a memory of size \(k\). A store read backwards is in the same way a promotion. A dropped source slot carries its list measure \(\nu\); read backwards it is a fresh draw, and conversely. The geometric multiplier is conjugated and the determinant changes sign, as in Lemma 2.1 of Lesson 8. Finally, the forward edge pays \(\rho\) for the hits of the old memory at the source and of the new memory at the target; these are the hits of the new and of the old memory of the reversed edge at its target and at its source. \(\square\)

## 3. Bounds for the ghost operations

Let \(k_{\rm tot}\) denote the total size of the memories of a state, and use the Schur weight

\[
\begin{gathered}
h=v_0^{\,k_{\rm tot}},\qquad v_0=8.\quad(3.1)
\end{gathered}
\]

**Lemma 3.1.** \(\|\mathcal G_j\|_{\mathscr H_B\to\mathscr H_B}\le e^{9K}\) for every \(j\) and large \(x\). The same bound holds after inserting factors of modulus at most \(1\) on the choices, as long as the operation preserves symmetric functions of the memory.

**Proof.** Consider one group with \(h\) particles hitting \(z_j\). In the row sum, each hitting particle is either deleted, contributing \((\eta_j/\rho)v_0^{-1}\), or survives, contributing \(q_j/\rho^2\), and a batch of \(l\) new particles contributes \((\eta_jV_i/\rho)^lv_0^l s_i^l/l!\). The weighted row sum is therefore

\[
\begin{gathered}
\Bigl(\frac{q_j}{\rho^2}+\frac{\eta_j}{\rho v_0}\Bigr)^h\exp\Bigl(\frac{v_0\eta_jV_is_i}\rho\Bigr).
\end{gathered}
\]

By Lemma 2.3 the column sum is the same with \(\eta_j\) and \(\eta_jV_i\) exchanged in the two places. Here \(\rho^2=\frac9{16}\), \(\rho v_0=6\), \(\eta_j=1-q_j\) and \(q_j\in\{\frac14,\frac12\}\), so

\[
\begin{gathered}
\frac{q_j}{\rho^2}+\frac{\eta_j}{\rho v_0}=\frac{16q_j}9+\frac{1-q_j}6\\
\in\Bigl\{\frac{41}{72},\frac{35}{36}\Bigr\},
\end{gathered}
\]

which is less than \(1\); since \(V_i\le1\), the same holds with \(\eta_jV_i\) in place of \(\eta_j\). Both exponentials are at most \(\exp(v_0s_i/\rho\cdot\frac34)=\exp(8s_i)\le e^9\), because \(s_i\le1.01\) by Lemma 2.1 of Lesson 12. Multiplying over the \(K\) groups, the row and column sums are at most \(e^{9K}\), and Lemma 2.1 gives the bound; the remarks after it cover \(\Pi_B\) and the inserted factors. \(\square\)

## 4. Crude bounds for the edges

For a source \(z\) choose an integer vector \(w_z\) with \(\det(z,w_z)=1\), and put \(r_z^*=\tau(w_z)/\tau(z)\), a real lift of the ratio \(r_{gz}\) (Lesson 11, (1.2)). Every \(z'\) has the form

\[
\begin{gathered}
z'=j_1w_z+hz,\qquad j_1=\det(z,z'),\\
h+j_1r_z^*=\frac{\tau(z')}{\tau(z)}.\quad(4.1)
\end{gathered}
\]

The first coordinates \(u\tau(z)\) and \(u\tau(z')\) of the two positions both lie in \([U,16U]\), so \(\tau(z')/\tau(z)\in[\frac1{16},16]\) and \(|h+j_1r_z^*|\le16\): for given \(z\) and \(j_1\) there are at most \(17\) targets.

**Lemma 4.1 (crude edge bound).** There is \(C_e=C_e(K,A_0)\) such that, for every \(j\), every piece \((S,I)\) of \(\mathcal E_j\), and every insertion of factors of modulus at most \(1\) on its choices, the weighted row and column sums on \(\mathscr H_B\) are at most \(L^{C_e}\). The same holds when any of the fresh prime values are fixed, their measures being left out of the bound.

**Proof.** Fix the source state. The source symmetrization is an average. Stores cost at most \(2^K\) choices and the weight ratio \(v_0^{|S|}\le8^K\); promotions cost at most \(B^K\) choices of indices, coefficients \(1/V_i\le2\), and lower the weight. Fresh draws have total mass \(s_i\le2\) per group. The factors \(\rho\) are at most \(1\). The multiplier vanishes unless \(D\mid\det(z,z')\), \(D\in[d_0,2d_0)\) and \(|t|\le5Y\). In the raw part, \(j_1=D(b-a)\) is fixed by the labels, so there are at most \(17\) targets, with multiplier at most \(2\). In the comparison part, \(j_1=Dt\) takes at most \(10Y+1\) values, each with at most \(17\) targets, and the multiplier is at most \((d_0/D)|\mathfrak M|\le4L^{3A_0}/Y\) by (5.2) of Lesson 7. Altogether the weighted row sum is at most \(C_KB^K(1+L^{3A_0})\le L^{C_e}\). By Lemma 2.4 the column sums are row sums of an operation of the same kind, with the same bound. \(\square\)

The factor \(B^K\) counts choices of particles to promote; it is a power of \(L\) that grows with \(K\). Lesson 15 shows that it never appears opposite a small factor in the Schur test.

## 5. Exercises

**13.1.** Prove the two identities (2.1).

**13.2.** Check the ghost row sum formula of Lemma 3.1 when \(h=1\) and no particles are created.

**13.3.** Show that the weighted Schur test with \(h\equiv1\) cannot give a bound for \(\mathcal G_j\) independent of the memory size, and explain the role of \(v_0\).

**13.4.** Prove the decomposition (4.1) and the count of at most \(17\) targets.

**13.5.** Explain why a factor depending on the index of an old particle (rather than on its prime and anchor) could destroy the symmetry of the memory, while a factor depending only on prime values does not.

## 6. Solutions

**13.1.** \(\binom{k+a}a/(k+a)!=1/(k!\,a!)\) by definition of the binomial coefficient, and multiplying by \(a!\) gives the second.

**13.2.** With one hitting particle and \(l=0\): deletion contributes \(\frac{\eta_j}\rho\cdot v_0^{-1}\) and survival \(\frac{q_j}{\rho^2}\), as in the formula with \(h=1\) and only the \(l=0\) term of the exponential.

**13.3.** With \(h\equiv1\) the row sum contains \((q_j/\rho^2+\eta_j/\rho)^{h_{\rm hit}}\), and \(q_j/\rho^2+\eta_j/\rho>1\) (for instance \(\frac89+\frac23\)), so it grows exponentially with the number of hitting particles. The weight \(v_0^{-1}\) attached to a deletion makes the deletion term small, while creations, which raise the weight, are controlled by the convergent exponential series.

**13.4.** The vectors \(z,w_z\) form a basis of \(\mathbb Z^2\), so \(z'=\beta w_z+hz\), and \(\det(z,z')=\beta\det(z,w_z)=\beta\). Applying the linear functional \(\tau\) and dividing by \(\tau(z)\) gives the last identity. For fixed \(j_1\), \(h=\tau(z')/\tau(z)-j_1r_z^*\) lies in an interval of length less than \(16\), which contains at most \(17\) integers.

**13.5.** The memory is a symmetric function of its particles; an operation must map symmetric functions to symmetric functions. A factor that depends on the position of a particle in an arbitrary ordering is not invariant under reordering, so averaging over orderings would change it. A factor that depends only on the prime value and anchor of the chosen particle is the same for every ordering.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Sections 4.3 and 4.4. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
