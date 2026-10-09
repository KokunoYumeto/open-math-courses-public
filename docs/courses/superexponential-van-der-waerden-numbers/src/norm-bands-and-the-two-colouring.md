# Norm bands and the two-colouring

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The outer colouring \(c_0\) of [A balanced colouring and the dichotomy](a-balanced-colouring-and-the-dichotomy.md) still has monochromatic progressions. This lesson removes all of them by a sparse random perturbation (Theorem 3.1) and deduces the main theorem (Theorem 4.1). Each element of \(G\) receives a *key*: its second-system box together with the integer part of a scaled squared norm. One random bit per key, equal to \(1\) with the small probability \(p=k^{-1/20}\), is added to \(c_0\). A key occurs at most four times along a progression (Lemma 1.1), by the equal-norm geometry of Behrend's construction [Beh]: a thin band around a sphere meets a line in two short pieces. Progressions rich in both outer colours would need many rare flips; affine progressions are so few that a union bound over their *signatures* suffices (Lemma 2.1). Notation is that of [Coordinates, meshes and label counts](coordinates-meshes-and-label-counts.md).

## 1. Keys

For \(n\in G\) let
\[
f(n)=\|q\tilde y(n)\|_2^2,\qquad\kappa(n)=\Bigl((V(y_i(n)))_{i=1}^D,\ \lfloor f(n)\rfloor\Bigr),
\]
and let \(\mathcal K\) be the finite set of keys \(\kappa(n)\), \(n\in G\).

**Lemma 1.1** (Four occurrences at most). Along every progression \(n_j=n_0+jd\) (\(0\le j<k\), \(d\ne0\)), every key occurs at most four times.

*Proof.* Fix a box of the second system and let \(J\) be the positions whose representatives \(\tilde y(n_j)\) lie in it. Its sides have length at most \(2H\), so by Lemma 2.1 of [A balanced colouring and the dichotomy](a-balanced-colouring-and-the-dichotomy.md) the points \(q\tilde y(n_j)\), \(j\in J\), lie on an affine line \(\ell\) (when \(|J|\ge2\)).

*Separation.* For \(j\ne j'\), \(\lambda(n_j-n_{j'})\) is a nonzero residue modulo \(q^D\), because the terms are distinct and \(\gcd(\lambda,q)=1\). Let \(z\) be an integer representative, \(a\le D-1\) the largest integer with \(q^a\mid z\) (independent of the representative), and \(z=q^au\) with \(q\nmid u\). In coordinate \(a+1\), \(y_{a+1}(n_j)-y_{a+1}(n_{j'})=u/q\bmod1\), at circle distance at least \(1/q\) from \(0\). Hence
\[
\|q\tilde y(n_j)-q\tilde y(n_{j'})\|_2\ge1\qquad(j\ne j'). \tag{1.1}
\]

*Bands.* Let \(z_0\) be the point of \(\ell\) nearest to the origin and \(e\) a unit vector along \(\ell\), so the points of \(\ell\) are \(z_0+se\) with \(\|z_0+se\|^2=s^2+C'\), \(C'=\|z_0\|^2\). For an integer \(m\ge0\), the band \(m\le s^2+C'<m+1\) meets the half-line \(s\ge0\) in a set contained in the interval between \(\sqrt{\max\{0,m-C'\}}\) and \(\sqrt{m+1-C'}\), of length at most \(1\) because \((\sqrt v-\sqrt u)^2\le v-u\) for \(0\le u\le v\); likewise for \(s\le0\). By (1.1), an interval of length at most \(1\) contains at most two of the points, so the key occurs at most four times. \(\square\)

## 2. Affine progressions and their signatures

A progression is *affine* if \(\tilde y(n_j)\) is affine in \(j\) as a sequence in \(\mathbb R^D\). Its *signature* is the word \(\bigl((c_0(n_j),\kappa(n_j))\bigr)_{0\le j<k}\), whose entries are the actual colours, boxes and band numbers.

**Lemma 2.1** (Few signatures). The number \(T_{\mathrm{aff}}\) of signatures of affine progressions satisfies
\[
T_{\mathrm{aff}}\le CT_{\mathrm{glob}}\bigl(k(Dq^2+2)\bigr)^3,\qquad\log\max\{1,T_{\mathrm{aff}}\}=O(k^{9/10}\log k)=o(pk),
\]
for an absolute constant \(C\).

*Proof.* If \(\tilde y(n_j)=A+jB\), then \(f(n_j)=\theta_0+\theta_1j+\theta_2j^2\) with \(\theta_0=q^2\|A\|^2\), \(\theta_1=2q^2\langle A,B\rangle\), \(\theta_2=q^2\|B\|^2\), and \(0\le f(n_j)\le Dq^2/4\). With \(B_*=\lfloor Dq^2/4\rfloor+1\), the word \((\lfloor f(n_j)\rfloor)_j\) is determined by the signs of \(\theta_0+\theta_1j+\theta_2j^2-b\) for \(j<k\) and \(0\le b\le B_*\): at most \(k(Dq^2+2)\) affine functions of \((\theta_0,\theta_1,\theta_2)\). By Corollary 1.2 of [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md) at most \(16(k(Dq^2+2)+1)^3\) such words occur. The label word determines the boxes and, as \(c_*\) is fixed, the colours \(c_0(n_j)\); with the band word it determines the signature. Finally \(\log T_{\mathrm{glob}}=O(k^{3/10}\log k)\), \(\log(Dq^2+2)\le2\log q+O(\log k)\), and \(\log q\le\frac{ck}D\log k+\log(2k^2)=O(k^{9/10}\log k)\), while \(pk=k^{19/20}\). \(\square\)

## 3. The cyclic two-colouring

**Theorem 3.1** (A cyclic two-colouring). There is an absolute integer \(K_0\) such that for every \(k\ge K_0\) the group \(G=\mathbb Z/N\mathbb Z\), \(N=q^D\ge k^{ck}\), carries a colouring \(\chi:G\to\{0,1\}\) with no monochromatic progression \(n_0,n_0+d,\dots,n_0+(k-1)d\), \(d\ne0\).

*Proof.* For each key \(\kappa\in\mathcal K\) take an independent bit \(E_\kappa\) with \(\Pr(E_\kappa=1)=p\), and put \(\chi(n)=c_0(n)+E_{\kappa(n)}\bmod2\). Positions with the same key use the same bit. Take \(k\) so large that \(p<1/2\).

*Progressions rich in both outer colours.* Suppose each outer colour occurs at least \(\gamma k\) times, and fix a target colour \(b\). Every position with \(c_0=1-b\) needs \(E_\kappa=1\) at its key; by Lemma 1.1 these positions carry at least \(\gamma k/4\) distinct keys, determined before sampling. So the progression has colour \(b\) everywhere with probability at most \(p^{\gamma k/4}\) (and probability \(0\) if a key also needs the value \(0\)). There are fewer than \(q^{2D}\) pairs \((n_0,d)\), so the probability that some such progression is monochromatic is at most
\[
2q^{2D}p^{\gamma k/4}\le\exp\Bigl(\bigl(2c-\tfrac{\gamma}{80}\bigr)k\log k+2D\log(2k^2)+\log2\Bigr)=o(1),
\]
using (2.1) of [Coordinates, meshes and label counts](coordinates-meshes-and-label-counts.md) and \(2c-\gamma/80=-21/200000<0\).

*Affine progressions.* Fix a signature and a target colour \(b\). Monochromaticity prescribes \(E_{\kappa_j}=b-c_j\bmod2\) for every entry \((c_j,\kappa_j)\). If these prescriptions are consistent and involve \(s\) distinct keys, \(u\) of them prescribed \(1\), the probability is \(p^u(1-p)^{s-u}\le(1-p)^s\le(1-p)^{k/4}\), as \(s\ge k/4\) by Lemma 1.1. Progressions with the same signature give the same event. Hence the probability that some affine progression is monochromatic is at most
\[
2T_{\mathrm{aff}}(1-p)^{k/4}\le2\max\{1,T_{\mathrm{aff}}\}e^{-pk/4}=\exp\bigl(-pk/4+o(pk)\bigr)=o(1).
\]

By Theorem 4.1 of [A balanced colouring and the dichotomy](a-balanced-colouring-and-the-dichotomy.md), every progression is rich in both outer colours or affine. For large \(k\) the two probabilities sum to less than \(1\), so some choice of the bits gives the required colouring. All thresholds are absolute, uniformly over the primes \(P\) allowed in the choice of \(q\), and \(N=q^D\ge k^{ck}\). \(\square\)

## 4. The main theorem

**Theorem 4.1** (OpenAI 2026). There is an absolute integer \(K_0\) such that for every integer \(k\ge K_0\) and every integer \(r\ge2\),
\[
W_r(k)>k^{ck\lfloor\log_2r\rfloor},\qquad c=10^{-5}.
\]

*Proof.* Theorem 3.1 gives a colouring of \(\mathbb Z/N\mathbb Z\) with no monochromatic \(k\)-term progression and \(N\ge k^{ck}\). Proposition 3.1 of [Van der Waerden numbers](van-der-waerden-numbers.md) gives \(W_r(k)>N^{\lfloor\log_2r\rfloor}\ge k^{ck\lfloor\log_2r\rfloor}\). The threshold on \(k\) does not depend on \(r\). \(\square\)

**Corollary 4.2.**
\[
\lim_{k\to\infty}\ \inf_{r\ge2}\frac{\log W_r(k)}{k\log r}=\infty,\qquad\lim_{r\to\infty}\ \inf_{k\ge3}\frac{\log W_r(k)}{\log r}=\infty .
\]
In particular \(W_r(k)^{1/k}\to\infty\) for every fixed \(r\ge2\), which answers Erdős's question, and \(W_r(k)/r^A\to\infty\) as \(r\to\infty\) for every fixed \(k\ge3\) and \(A>0\).

*Proof.* Since \(\lfloor\log_2r\rfloor\ge\log r/(2\log2)\), Theorem 4.1 gives \(\log W_r(k)/(k\log r)\ge\frac c{2\log2}\log k\) for \(k\ge K_0\) and all \(r\ge2\). Theorem 4.1 of [Van der Waerden numbers](van-der-waerden-numbers.md) gives \(\log W_r(k)/\log r\ge\log r/(64\log2)\) for \(r\ge256\) and all \(k\ge3\). For fixed \(r\), \(W_r(k)^{1/k}>k^{c\lfloor\log_2r\rfloor}\to\infty\). \(\square\)

The constant \(c=10^{-5}\) is far from optimal, and the threshold \(K_0\) is astronomically large. For two colours, Campos, Fox and Schildkraut proved the lower bound \((1-o(1))k2^{k-1}\) [CFS]; for three colours, Fox and Hunter proved \(W_3(k)>2^{k\log^*k/4}\) [FH]. Upper bounds are much larger. For three-term progressions, the density bound of Kelley and Meka gives an upper bound quasipolynomial in the number of colours [KM], and Leng, Sah and Sawhney improved the density bounds for longer progressions [LSS].

## 5. Exercises

**5.1.** Let a line in \(\mathbb R^2\) have nearest point \(z_0\) to the origin. Show that each of the two half-lines from \(z_0\) meets the annulus \(\{4\le\|z\|^2<5\}\) in a set of length at most \(1\), and find the lines for which the total length is largest.

**5.2.** Check the arithmetic \(2c-\gamma/80=-21/200000\), and explain why the flip probability \(p=k^{-1/20}\) must be small for the rich case but not too small for the affine case.

**5.3.** In the proof of Theorem 3.1, why may the same key occur at a position needing a flip and at a position not needing one, and why does that only help?

**5.4.** Derive \(W_2(k)^{1/k}\to\infty\) from Theorem 4.1, and compare the growth \(k^{ck}\) with the lower bound \(2^k\) of the first moment method.

## 6. Solutions

**5.1.** On the line \(z_0+se\), with \(z_0\perp e\), \(\|z\|^2=s^2+C'\), and the annulus corresponds to \(4-C'\le s^2<5-C'\). On \(s\ge0\) this is an interval from \(\sqrt{\max\{0,4-C'\}}\) to \(\sqrt{5-C'}\), of length at most \(1\); likewise on \(s\le0\). If \(C'\le4\) the total length is \(2(\sqrt{5-C'}-\sqrt{4-C'})\), and if \(4<C'<5\) it is \(2\sqrt{5-C'}\); both are at most \(2\), with equality exactly when \(C'=4\), that is, for the lines tangent to the inner circle, where the two pieces meet at the tangent point.

**5.2.** \(2c=2\cdot10^{-5}=\frac1{50000}\) and \(\gamma/80=\frac1{8000}\); their difference is \(\frac{4-25}{200000}=-\frac{21}{200000}\). In the rich case the probability \(p^{\gamma k/4}=e^{-\gamma k\log k/80}\) must beat the number \(q^{2D}\approx k^{2ck}\) of progressions, which needs \(p\) to be a negative power of \(k\). In the affine case the probability \((1-p)^{k/4}\approx e^{-pk/4}\) must beat the number of signatures, \(e^{O(k^{9/10}\log k)}\), which needs \(pk\) to be much larger than \(k^{9/10}\log k\); \(p=k^{-1/20}\) satisfies both.

**5.3.** A key is a box and a band, and positions with different outer colours can share it. If a key must be \(1\) at one position and \(0\) at another for the progression to be monochromatic in colour \(b\), the event is impossible, so its probability \(0\) satisfies the bound.

**5.4.** For \(r=2\), \(\lfloor\log_2r\rfloor=1\) and \(W_2(k)>k^{ck}\), so \(W_2(k)^{1/k}>k^c\to\infty\). The first moment method colours \([N]\) at random and needs the expected number \(\approx N^2\cdot2^{1-k}/(k-1)\) of monochromatic progressions to be below \(1\), giving only \(N\approx2^{k/2}\); the local lemma improves this to about \(2^k/k\). Theorem 4.1 gives \(e^{ck\log k}\), larger than every \(C^k\).

## References

- [OpenAI-vdW] OpenAI, *Quantitative superexponential bounds for van der Waerden numbers*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf
- [Beh] F. A. Behrend, *On sets of integers which contain no three terms in arithmetical progression*, Proceedings of the National Academy of Sciences 32 (1946), 331–332. https://pmc.ncbi.nlm.nih.gov/articles/PMC1078964/
- [CFS] M. Campos, J. Fox and C. Schildkraut, *A new lower bound for two-color van der Waerden numbers*, 2026. https://arxiv.org/abs/2608.20824
- [FH] J. Fox and Z. Hunter, *Three-color van der Waerden numbers grow super-exponentially*, 2026. https://arxiv.org/abs/2606.02541
- [KM] Z. Kelley and R. Meka, *Strong bounds for 3-progressions*, 2023. https://arxiv.org/abs/2302.05537
- [LSS] J. Leng, A. Sah and M. Sawhney, *Improved bounds for Szemerédi's theorem*, 2024. https://arxiv.org/abs/2402.17995
