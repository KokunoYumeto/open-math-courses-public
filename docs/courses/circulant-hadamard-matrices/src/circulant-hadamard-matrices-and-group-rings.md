# Circulant Hadamard matrices and group rings

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A real *Hadamard matrix* of order \(n\) is an \(n\times n\) matrix \(H\) with entries \(\pm1\) and \(HH^{\mathsf T}=nI\): its rows are pairwise orthogonal. It is *circulant* if each row is the cyclic shift of the one above, \(H_{ij}=h_{j-i\bmod n}\) for signs \(h_0,\dots,h_{n-1}\). The matrices \((1)\) and the circulant matrix with first row \((1,1,1,-1)\) are examples. The *circulant Hadamard conjecture*, usually attributed to Ryser (1963), says that there are no others: a circulant Hadamard matrix has order \(1\) or \(4\). Turyn proved in 1965 that any other order must be \(4u^2\) with \(u\) odd and not a prime power [Turyn], and many later restrictions followed; before 2026, the orders \(4<n\le4\cdot10^{30}\) had been excluded except for \(4\,489\) candidates. OpenAI proved the conjecture in September 2026 [OpenAI-H]:

**Theorem** (OpenAI). A real circulant Hadamard matrix of order \(n\) exists if and only if \(n\in\{1,4\}\).

This course proves the theorem. The proof works in the group ring of the cyclic group: the first row becomes an element \(h\) with \(hh^*=n\) (Lemma 2.1), and evaluating \(h\) and its pieces at characters gives algebraic integers whose norms are known. The lesson [Local rings of cyclotomic integers](local-rings-of-cyclotomic-integers.md) proves that \(n=4u^2\) with \(u\) odd; the lesson [Alternating character products](alternating-character-products.md) shows that certain alternating products of character values are roots of unity of odd order; and [The circulant Hadamard conjecture](the-circulant-hadamard-conjecture.md) derives a contradiction for \(u>1\) by reducing modulo a prime above \(2\). As a consequence, binary sequences of even length greater than \(4\) cannot have all aperiodic autocorrelations of size at most \(1\) (Section 3).

We use basic ring theory (rings, ideals, quotients, maximal ideals) as in the core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40), and linear algebra over \(\mathbb C\) as in the core course [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40).

## 1. Group rings and characters

Let \(V\) be a finite abelian group, written multiplicatively, and \(R\subseteq\mathbb C\) a subring with \(\overline R=R\). The *group ring* \(R[V]\) consists of the formal sums \(f=\sum_{z\in V}f_zz\) with \(f_z\in R\), multiplied by the rule \(z\cdot z'=zz'\) extended bilinearly. A scalar \(r\in R\) stands for \(r\cdot1\). The *involution* is
\[
f^*=\sum_{z\in V}\overline{f_z}\,z^{-1};
\]
it is additive, \((fg)^*=f^*g^*\) and \((f^*)^*=f\). For a cyclic group \(C_N\) with generator \(X\), \(R[C_N]=R[X]/(X^N-1)\).

A *character* of \(V\) is a homomorphism \(\chi:V\to\mathbb C^\times\); its values are roots of unity of order dividing \(|V|\). Evaluation \(f\mapsto\chi(f)=\sum_zf_z\chi(z)\) is a ring homomorphism \(R[V]\to\mathbb C\), and \(\chi(f^*)=\overline{\chi(f)}\) because \(\chi(z^{-1})=\overline{\chi(z)}\). A surjective homomorphism \(V\to V'\) induces a ring homomorphism \(R[V]\to R[V']\), the *projection*, which commutes with the involution. If \(V=V_1\times V_2\), evaluating the \(V_2\)-part at a character \(\psi\) of \(V_2\) gives a ring homomorphism \(R[V]\to R[\psi(V_2)][V_1]\) (partial evaluation); it commutes with the involutions, the latter conjugating the coefficients.

**Lemma 1.1.** Let \(J=\sum_{z\in V}z\). For a nontrivial character \(\chi\), \(\chi(J)=0\); for the trivial character, \(\chi(J)=|V|\).

**Proof.** Choose \(z_0\) with \(\chi(z_0)\neq1\). Multiplication by \(z_0\) permutes \(V\), so \(\chi(z_0)\chi(J)=\chi(z_0J)=\chi(J)\), and \((\chi(z_0)-1)\chi(J)=0\). \(\square\)

If \(a,b\) are coprime, the cyclic group of order \(ab\) is the product of its subgroups of orders \(a\) and \(b\) (Chinese remainder theorem). In particular a cyclic group is the product of its cyclic primary components.

## 2. The first row as a group ring element

Let \(H\) be a real circulant matrix with first row \(h_0,\dots,h_{n-1}\in\{\pm1\}\), and put \(h=\sum_jh_jX^j\in\mathbb Z[C_n]\).

**Lemma 2.1.** \(H\) is a Hadamard matrix if and only if \(hh^*=n\).

**Proof.** The coefficient of \(X^a\) in \(hh^*=\sum_{j,l}h_jh_lX^{j-l}\) is \(\sum_jh_jh_{j-a}\), indices modulo \(n\). Row \(i\) of \(H\) is \((h_{j-i})_j\), so this coefficient is the inner product of rows \(0\) and \(a\); by the cyclic symmetry, it is also that of rows \(i\) and \(i+a\). Thus \(HH^{\mathsf T}=nI\) exactly when the coefficient of \(X^a\) is \(n\) for \(a=0\) and \(0\) otherwise. \(\square\)

The inner products \(P_h(t)=\sum_jh_jh_{j+t}\) are the *periodic autocorrelations* of the row.

**Corollary 2.2.** If a circulant Hadamard matrix of order \(n>1\) exists, then \(n\) is an even square.

**Proof.** The trivial character gives \(h(1)^2=n\), so \(n\) is the square of the integer \(h(1)=\sum_jh_j\). The inner product of two distinct rows is a sum of \(n\) signs and vanishes, so \(n\) is even. \(\square\)

For \(n=4\) and the row \((1,1,1,-1)\), \(P_h(1)=1+1-1-1=0\), \(P_h(2)=1-1+1-1=0\) and \(P_h(3)=P_h(1)\), so the matrix is Hadamard.

## 3. Barker sequences

A sequence \(a=(a_0,\dots,a_{n-1})\in\{\pm1\}^n\), \(n>1\), is a *Barker sequence* if its *aperiodic autocorrelations* \(C_a(t)=\sum_{j=0}^{n-t-1}a_ja_{j+t}\) satisfy \(|C_a(t)|\le1\) for \(1\le t<n\). Examples exist for \(n=2,3,4,5,7,11,13\), for instance \(++\), \(++-\), \(+++-\), \(+++-+\), \(+++--+-\), \(+++---+--+-\) and \(+++++--++-+-+\).

**Proposition 3.1.** If \(a\) is a Barker sequence of even length \(n>2\), then the circulant matrix with first row \(a\) is a Hadamard matrix.

**Proof.** The periodic autocorrelation is \(P_a(t)=\sum_{j}a_ja_{j+t\bmod n}=C_a(t)+C_a(n-t)\). The product of its \(n\) summands is \((\prod_ja_j)^2=1\), so an even number of them equal \(-1\), and \(P_a(t)\equiv n\pmod4\). Also \(C_a(t)\equiv n-t\pmod2\), being a sum of \(n-t\) signs. For \(t=2\), both \(C_a(2)\) and \(C_a(n-2)\) are even, hence \(0\) by the Barker bound; so \(P_a(2)=0\) and \(4\mid n\). For every \(1\le t<n\), \(|P_a(t)|\le2\) and \(P_a(t)\equiv0\pmod4\), so \(P_a(t)=0\). \(\square\)

With the theorem, Barker sequences of even length exist only for \(n=2\) and \(n=4\). For odd lengths, Turyn and Storer proved in 1961 that none exist beyond \(13\), and Schmidt and Willms gave a simpler proof [SW]; that part is not proved in this course. Together these give the lengths \(2,3,4,5,7,11,13\).

## 4. Exercises

**Exercise 4.1** (easy). Show that if \(h\) is the first row of a circulant Hadamard matrix, so are \(-h\), the reversed row \((h_{-j})_j\), and \((h_{cj})_j\) for every \(c\) coprime to \(n\). *Hint:* apply the corresponding ring automorphisms of \(\mathbb Z[C_n]\) to \(hh^*=n\).

**Exercise 4.2** (medium). Let \(n=4u^2\) and let \(h\) give a circulant Hadamard matrix with \(h(1)=2u\). Show that \(D=\{j:h_j=-1\}\) has \(k=2u^2-u\) elements and that every nonzero residue modulo \(n\) is a difference of two elements of \(D\) in exactly \(u^2-u\) ways.

**Exercise 4.3** (easy). Verify the Barker property of the sequence of length \(13\) above.

**Exercise 4.4** (easy). Prove Lemma 1.1 for \(V=C_N\) and \(\chi(X)=\zeta\), a primitive \(m\)-th root of unity with \(1<m\mid N\), by summing a geometric series.

## 5. Solutions

**4.1.** The maps \(X\mapsto X^{-1}\) and \(X\mapsto X^c\) (with \(c\) coprime to \(n\)) are automorphisms of \(C_n\), hence of \(\mathbb Z[C_n]\), commuting with \(*\); they fix the scalar \(n\). Negation preserves \(hh^*\).

**4.2.** \(h(1)=n-2k\), so \(k=(4u^2-2u)/2=2u^2-u\). With \(N_D(t)\) the number of pairs \((a,b)\in D^2\) with \(a-b=t\), a direct count of the signs in \(P_h(t)\) gives \(P_h(t)=n-4k+4N_D(t)\). For \(t\neq0\), \(P_h(t)=0\) gives \(N_D(t)=k-u^2=u^2-u\).

**4.3.** For \(a=+++++--++-+-+\), a direct computation gives \(C_a(t)=0\) for odd \(t\) and \(C_a(t)=1\) for even \(t\), \(1\le t\le12\).

**4.4.** \(\chi(J)=\sum_{j=0}^{N-1}\zeta^j=\frac{\zeta^N-1}{\zeta-1}=0\), since \(\zeta^N=1\neq\zeta\).

## References

- [OpenAI-H] OpenAI, *The circulant Hadamard conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 1 and 6. https://github.com/openai/math/tree/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026
- [SW] K.-U. Schmidt and J. Willms, *Barker sequences of odd length*, Des. Codes Cryptogr. 80 (2016); arXiv:1501.06035. https://arxiv.org/abs/1501.06035
- [Turyn] R. J. Turyn, *Character sums and difference sets*, Pacific J. Math. 15 (1965), 319–346. https://msp.org/pjm/1965/15-1/p32.xhtml
