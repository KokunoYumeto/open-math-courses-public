# Divided powers of flat modules

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

The graded pieces of the divided power algebra of a flat module are flat. This lesson proves this for rings in the usual sense, through Lazard's theorem. It deduces that the graded pieces of the divided power envelope of a weakly regular ideal are flat over the quotient ring after tensoring with \(\mathbb Q\). They are flat without tensoring wherever the comparison map \(c\) is an isomorphism. The lesson proves:

- \(\Gamma^n_B\) of a free module of rank \(r\) is free, with the divided monomials as a basis;
- \(\Gamma^n_B(M)\) is flat for every flat module \(M\) over a ring \(B\);
- consequences for the graded ring of a divided power envelope.

**Prerequisites.** [*Koszul complexes and the shift formulas*](koszul-complexes-and-the-shift-formulas.md) (Conventions: \(\Gamma\) by generators and relations); [*Divided power envelopes of weakly regular ideals and their graded rings*](divided-power-envelopes-of-weakly-regular-ideals.md) (Proposition 2.1, Theorem 3.3, Exercise 7.2). From the AI-integrated Stacks project: Lazard's theorem [[Stacks, Tag 058G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-lazard)].

## Conventions

Rings are commutative rings in the usual sense. \(\Gamma_B(M)=\bigoplus_n\Gamma^n_B(M)\) is the divided power algebra, with generators \(\gamma_k(\xi)\) of weight \(k\) and the relations of the Conventions of the lesson on Koszul complexes.

## 1. Flatness

**Lemma 1.1.** Let \(B\) be a ring.

1. For \(B\)-modules \(M\) and \(M'\), the algebra map \(\Gamma_B(M)\otimes_B\Gamma_B(M')\to\) \(\Gamma_B(M\oplus M')\) induced by the two inclusions is an isomorphism of graded algebras.
2. \(\Gamma^n_B(B^r)\) is free, with basis the products \(\gamma_{n_1}(e_1)\cdots\gamma_{n_r}(e_r)\), \(n_1+\cdots+n_r=n\).

**Proof.** (1) *The inverse map.* Put \(g_k(x,x')=\sum_{i+j=k}\gamma_i(x)\otimes\gamma_j(x')\). These maps satisfy the relations:

- \(g_0=1\), and \(g_1\) is linear.
- The scalar and addition relations follow from those in each factor.
- The product relation follows from those in each factor together with Vandermonde's identity \(\sum_a\binom sa\binom t{i-a}=\binom{s+t}i\).

So they define an algebra map \(\Gamma_B(M\oplus M')\to\Gamma_B(M)\otimes\Gamma_B(M')\).

*The composites.* Both composites are algebra maps, and they are the identity on the generators \(\gamma_k(x)\), \(\gamma_k(x')\) and \(\gamma_k(x+x')=\sum_i\gamma_i(x)\gamma_{k-i}(x')\). So both composites are identities.

(2) By (1), it suffices to treat \(r=1\). Let \(B\langle t\rangle\) be the free module on \(t^{[n]}\), \(n\geq0\), with the product \(t^{[i]}t^{[j]}=\binom{i+j}it^{[i+j]}\), which is commutative and associative. The maps \(g_k(be)=b^kt^{[k]}\) satisfy the relations; for addition this is the binomial formula. So they define an algebra map \(\Gamma_B(Be)\to B\langle t\rangle\) sending \(\gamma_n(e)\) to \(t^{[n]}\).

Conversely, \(\Gamma^n_B(Be)\) is spanned by \(\gamma_n(e)\): a product \(\prod\gamma_{n_i}(b_ie)\) equals \(\prod b_i^{n_i}\) times an integer multiple of \(\gamma_n(e)\). So \(t^{[n]}\mapsto\gamma_n(e)\) is an inverse, and \(\Gamma^n_B(Be)=B\gamma_n(e)\) is free. \(\square\)

**Theorem 1.2.** If \(M\) is a flat module over a ring \(B\), then \(\Gamma^n_B(M)\) is flat over \(B\) for every \(n\geq0\).

**Proof.** *Reduction to free modules.* By Lazard's theorem [Tag 058G], \(M=\operatorname{colim}_\alpha M_\alpha\) is a filtered colimit of finite free modules. The functor \(\Gamma^n_B\) commutes with filtered colimits. Indeed, \(\Gamma_B(M)\) is the quotient of the polynomial algebra on the symbols \(\gamma_k(\xi)\), \(\xi\in M\), by the relations. Each symbol and each relation involves finitely many elements of \(M\). So every element and every equality in \(\Gamma_B(M)\) comes from some \(\Gamma_B(M_\alpha)\). The \(\Gamma^n_B(M_\alpha)\) are free by Lemma 1.1.

*Filtered colimits of flat modules.* Let \(N'\to N\) be injective. Then
\[
\Gamma^n_B(M)\otimes N'=\operatorname{colim}\bigl(\Gamma^n_B(M_\alpha)\otimes N'\bigr),
\]
and the maps \(\Gamma^n_B(M_\alpha)\otimes N'\to\Gamma^n_B(M_\alpha)\otimes N\) are injective. Filtered colimits of injective maps are injective. So \(\Gamma^n_B(M)\otimes N'\to\Gamma^n_B(M)\otimes N\) is injective. \(\square\)

**Corollary 1.3.** Let \(I\) be a weakly regular ideal of a ring \(A\), \(B=A/I\), \(M=I/I^2\), and \(D\) the envelope of \((A,I)\).

1. For every \(n\), \((F^nD/F^{n+1}D)_{\mathbb Q}\) is flat over \(B_{\mathbb Q}\).
2. If the map \(c\) of \((A,I)\) is an isomorphism, then every \(F^nD/F^{n+1}D\) is flat over \(B\). This holds in particular when \(A\) is a \(\mathbb Q\)-algebra.

**Proof.** (1) By Theorem 3.3 of the lesson on divided power envelopes, \((\operatorname{gr}^nD)_{\mathbb Q}\cong\Gamma^n_B(M)_{\mathbb Q}=\Gamma^n_B(M)\otimes_BB_{\mathbb Q}\). The module \(\Gamma^n_B(M)\) is flat by Theorem 1.2, and base change preserves flatness.

(2) The map \(c\) is graded (Proposition 2.1 there), so it identifies \(\operatorname{gr}^nD\) with \(\Gamma^n_B(M)\), which is flat by Theorem 1.2. For \(\mathbb Q\)-algebras \(c\) is an isomorphism by Exercise 7.2 there. \(\square\)

Flatness over \(B\) does not give flatness over \(A\): Proposition 6.1 of the lesson on divided power envelopes shows that the envelope of \((\mathbb F_p[x],(x))\) is not flat over \(\mathbb F_p[x]\).

## 2. Exercises

**Exercise 2.1.** Show that \(\Gamma^2_{\mathbb Z}(\mathbb Z^2)\) is free of rank \(3\), and that the map \(S^2(\mathbb Z^2)\to\Gamma^2(\mathbb Z^2)\), \(xy\mapsto xy\), has cokernel \((\mathbb Z/2)^2\).

## 3. Complete solutions

**2.1.** By Lemma 1.1, a basis is \(\gamma_2(e_1)\), \(\gamma_1(e_1)\gamma_1(e_2)\), \(\gamma_2(e_2)\). The map sends \(e_1^2\), \(e_1e_2\), \(e_2^2\) to \(2\gamma_2(e_1)\), \(e_1e_2\), \(2\gamma_2(e_2)\). So the cokernel is \((\mathbb Z/2)^2\).

## Sources

Divided power algebras and the bases of Lemma 1.1 are due to Roby and to Berthelot, in his work on crystalline cohomology. Lazard's theorem is taken from the Stacks project, cited above. The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026 and completed here.
