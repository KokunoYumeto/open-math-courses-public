# Multiplicative states and the proof of Theorem A

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The set \(\mathcal K_{d,k}\) of states satisfying \(\mu(T_dU)\ge k\mu(U)\) is nonempty, compact and convex when \(k<d^\nu\) ([States and a catalytic comparison](states-and-a-catalytic-comparison.md), Lemma 6.3 and Proposition 6.7). This lesson finds a character in it. The inequalities defining \(\mathcal K_{d,k}\) are preserved by the normalized products \(\mu\mapsto\mu(z\,\cdot\,)/\mu(z)\); a fixed point of one of these maps, given by Schauder's theorem, is multiplicative with respect to \(z\), and a nested sequence of compact sets yields a state that is multiplicative with respect to all \(z\) at once (Lemma 7.2). Together with Theorem 5.2 this proves \(\nu\le9/4\) and Theorem A. The argument is OpenAI's [OpenAI-MM, Appendix A]; working over the countable field \(F\) lets Schauder's theorem for normed spaces replace the Schauder–Tychonoff theorem for locally convex spaces used there.

## 1. Normalized products

For a state \(\mu\) and a nonzero \(z\in S\) put
\[
(\Phi_z\mu)(A)=\frac{\mu(zA)}{\mu(z)}\qquad(A\in S).
\]
The denominator is at least \(1\), because \(z\ge1\).

**Lemma 7.1.** Let \(z\in S\) be nonzero. Then \(\Phi_z\) maps \(\mathcal K_{d,k}\) into itself, and it is continuous for the norm of Section 2 of the previous lesson.

**Proof.** Let \(\mu\in\mathcal K_{d,k}\). The map \(\Phi_z\mu\) is additive because \(z(A+U)=zA+zU\), monotone because \(A\ge A'\) implies \(zA\ge zA'\), and normalized because \(z1=z\). It satisfies (6.1): applying (6.1) for \(\mu\) to \(zU\),
\[
\begin{aligned}
(\Phi_z\mu)(T_dU)&=\frac{\mu(T_d\,zU)}{\mu(z)}\ge k\,\frac{\mu(zU)}{\mu(z)}\\
&=k\,(\Phi_z\mu)(U).
\end{aligned}
\]
For continuity, let \(\mu_n\to\mu\) in \(\mathcal K_{d,k}\). By Lemma 6.3(a), \(\mu_n\to\mu\) pointwise; each value \((\Phi_z\mu_n)(A)\) is a continuous function of \(\mu_n(zA)\) and \(\mu_n(z)\ge1\), so \(\Phi_z\mu_n\to\Phi_z\mu\) pointwise, and these functions lie in \(Q\) because they are states. By Lemma 6.3(a) again, the convergence holds in norm. \(\square\)

## 2. A multiplicative state

**Lemma 7.2.** Let \(\mathcal K'\) be a nonempty compact convex set of states in the normed space \(V\), mapped into itself by \(\Phi_z\) for every nonzero \(z\in S\). Then \(\mathcal K'\) contains a character.

**Proof.** Enumerate the nonzero elements of \(S\) as \(z_1,z_2,\dots\). We construct nonempty compact convex sets
\[
\mathcal K'=\mathcal K_0\supseteq\mathcal K_1\supseteq\mathcal K_2\supseteq\cdots,
\]
each mapped into itself by every \(\Phi_z\), such that every \(\mu\in\mathcal K_n\) satisfies \(\mu(z_nA)=\mu(z_n)\mu(A)\) for all \(A\in S\).

Suppose \(\mathcal K_{n-1}\) is constructed. The map \(\Phi_{z_n}\) is a continuous self-map of the nonempty compact convex subset \(\mathcal K_{n-1}\) of the normed space \(V\) (continuity as in Lemma 7.1). By Schauder's theorem, Theorem 5.1 of [Ultrapowers and Darbo's fixed-point theorem](course:tingleys-problem/ultrapowers-and-darbos-fixed-point-theorem#5-schauder-s-theorem), it has a fixed point \(\kappa\). Put \(c=\kappa(z_n)\), and let \(\mathcal K_n\) be the set of \(\mu\in\mathcal K_{n-1}\) with \(\mu(z_nA)=c\,\mu(A)\) for all \(A\in S\). The fixed point equation \(\kappa(z_nA)=\kappa(z_n)\kappa(A)\) shows \(\kappa\in\mathcal K_n\). The defining conditions are closed by Lemma 6.3(a) and, because \(c\) is fixed, linear; so \(\mathcal K_n\) is compact and convex. Taking \(A=1\) shows \(\mu(z_n)=c\) for every \(\mu\in\mathcal K_n\), which gives the required multiplicativity. Finally, for \(\mu\in\mathcal K_n\) and nonzero \(w\), the state \(\Phi_w\mu\) lies in \(\mathcal K_{n-1}\), and
\[
\begin{aligned}
(\Phi_w\mu)(z_nA)&=\frac{\mu(z_n\,wA)}{\mu(w)}=c\,\frac{\mu(wA)}{\mu(w)}\\
&=c\,(\Phi_w\mu)(A),
\end{aligned}
\]
so \(\Phi_w\mu\in\mathcal K_n\).

The intersection of a decreasing sequence of nonempty compact sets is nonempty; let \(\lambda\) lie in all \(\mathcal K_n\). Then \(\lambda(zA)=\lambda(z)\lambda(A)\) for every nonzero \(z\) and every \(A\), and for \(z=0\) both sides vanish. So \(\lambda\) is a multiplicative state, that is, a character. \(\square\)

## 3. Detecting characters

**Theorem 7.3.** Let \(d\ge2\) and \(k\ge0\) be integers with \(k<d^\nu\). Then there is a character \(\lambda\) with \(\lambda(T_d)\ge k\).

**Proof.** By Proposition 6.7 and Lemma 6.3(c), \(\mathcal K_{d,k}\) is a nonempty compact convex set of states, and by Lemma 7.1 it is mapped into itself by every \(\Phi_z\). Lemma 7.2 gives a character \(\lambda\in\mathcal K_{d,k}\), and (6.1) with \(U=1\) gives \(\lambda(T_d)\ge k\). \(\square\)

## 4. The proof of Theorem A

**Theorem 7.4.** \(\nu\le9/4\).

**Proof.** Let \(d\ge2\) and \(k=\lceil d^\nu\rceil-1\), so that \(d^\nu-1\le k<d^\nu\). Theorem 7.3 gives a character \(\lambda\) with \(\lambda(T_d)\ge k\), and Theorem 5.2 gives \(\lambda(T_d)\le d^{9/4}\). Hence \(d^\nu\le d^{9/4}+1\le2d^{9/4}\) for every \(d\ge2\). Taking logarithms, \(\nu\le\frac94+\log2/\log d\), and letting \(d\to\infty\) gives \(\nu\le9/4\). The character may depend on \(d\); Theorem 5.2 applies to every character. \(\square\)

**Proof of Theorem A.** Apply Proposition 1.10 with \(\tau=9/4\). \(\square\)

The proof gives an exact rank decomposition of some \(T_u\) with coefficients in the field \(F\) generated by the roots of unity and with \(R(T_u)<u^{9/4+\delta}\), for every \(\delta>0\); the algorithms of Proposition 1.10 use only constants from \(F\), and the same bound \(\nu\le9/4\) holds over every field containing \(F\). OpenAI's companion papers [OpenAI-MM2] treat the bound \(\omega<2.258\) in characteristic zero, rectangular matrix multiplication, and bounds over every field; they are not treated in this course.

## 5. Exercises

**7.1** (medium). Show that every character satisfies \(\lambda(T_d)\le d^\nu\) for every \(d\ge2\). Deduce, with Theorem 7.3, that \(\nu\) is the supremum of \(3t(\lambda)\) over all characters.

**7.2** (easy). Show that \(\Phi_z\Phi_w=\Phi_{wz}\) on states, for nonzero \(z,w\in S\).

**7.3** (easy). Show that a state is a character if and only if it is fixed by every \(\Phi_z\), \(z\ne0\).

**7.4** (medium). In the proof of Lemma 7.2, why is it not enough to choose a fixed point of \(\Phi_{z_1}\) in \(\mathcal K'\), then a fixed point of \(\Phi_{z_2}\) in \(\mathcal K'\), and so on? Why is \(\mathcal K_n\) defined with the frozen value \(c\) instead of as the set of all \(\mu\in\mathcal K_{n-1}\) with \(\mu(z_nA)=\mu(z_n)\mu(A)\) for all \(A\)?

## 6. Solutions

**7.1.** For every \(j\), \(\lambda(T_d)^j=\lambda(T_{d^j})\le R(T_{d^j})\) by Lemma 1.6(a) and Lemma 2.2; take \(j\)-th roots and apply Exercise 1.5. With Lemma 2.5, \(3t(\lambda)\le\nu\) for every character. By Theorem 7.3, for every \(d\ge2\) there is a character with \(d^{3t(\lambda)}\ge d^\nu-1\), and \(\log_d(d^\nu-1)\to\nu\) as \(d\to\infty\).

**7.2.** For every \(A\),
\[
\begin{aligned}
(\Phi_z\Phi_w\mu)(A)&=\frac{(\Phi_w\mu)(zA)}{(\Phi_w\mu)(z)}\\
&=\frac{\mu(wzA)/\mu(w)}{\mu(wz)/\mu(w)}\\
&=(\Phi_{wz}\mu)(A).
\end{aligned}
\]

**7.3.** \(\Phi_z\mu=\mu\) means \(\mu(zA)=\mu(z)\mu(A)\) for all \(A\). If this holds for every nonzero \(z\), then \(\mu\) is multiplicative (for \(z=0\) both sides vanish); conversely a character satisfies it.

**7.4.** A fixed point of \(\Phi_{z_2}\) chosen in \(\mathcal K'\) need not be fixed by \(\Phi_{z_1}\), so separately chosen fixed points need not have a common limit with all the required properties. The sets \(\mathcal K_n\) carry the earlier equations along: \(\mathcal K_{n-1}\) consists of states multiplicative with respect to \(z_1,\dots,z_{n-1}\), it is mapped into itself by \(\Phi_{z_n}\), and the next fixed point is taken inside it; the nested compact sets then have a common point. The set of all \(\mu\in\mathcal K_{n-1}\) with \(\mu(z_nA)=\mu(z_n)\mu(A)\) for all \(A\) is defined by quadratic conditions and need not be convex. With the value \(c\) frozen the conditions are linear, so \(\mathcal K_n\) is convex, as the next application of Schauder's theorem requires.

## References

- [OpenAI-MM] OpenAI, *An upper bound of 9/4 for the matrix multiplication exponent*, OpenAI Math Release preprint, 2 October 2026, Section 5 and Appendix A. https://github.com/openai/math/tree/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026
- [OpenAI-MM2] OpenAI, *Complex matrix multiplication below 2.258 and rectangular bounds*, 24 September 2026, https://github.com/openai/math/tree/main/preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026 ; and *Staggered extraction for exact matrix multiplication over every field*, 24 September 2026, https://github.com/openai/math/tree/main/preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026
- [CVZ] M. Christandl, P. Vrana and J. Zuiddam, *Universal points in the asymptotic spectrum of tensors*, Journal of the American Mathematical Society 36 (2023), 31–79; arXiv:1709.07851. https://arxiv.org/abs/1709.07851
