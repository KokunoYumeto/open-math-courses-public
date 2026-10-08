# One frequency sequence for all convolution factors

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

Fourier transforms turn compact convolution into multiplication. Logarithms then turn that product into a sum. To pass to growth indicators, every factor must use the same escaping real frequency sequence. Separate indicator families do not encode that synchronization.

Basic references are Tao's *246B, Notes 2*, Hörmander's *The Analysis of Linear Partial Differential Operators I*, and its second volume. The exact compactness and indicator proofs needed here are in the linked preceding lessons; the background references are not substitutes for those proofs.

## 1. The full joint-family identity

For a compact distribution \(u\), put

\[
 F_u(\zeta)=\langle u(x),e^{-ix\cdot\zeta}\rangle,\qquad
 L_u(z,c)=\frac{\log|F_u(c+z\log|c|)|}{\log|c|},
 \quad c\in\mathbb R^n,\quad |c|>2. \tag{1.1}
\]

Use \(D=-i\partial\). A coordinate of a limiting tuple is either a proper plurisubharmonic local \(L^1\) limit, or a uniform local collapse to \(-\infty\). A proper profile \(v\) has a finite support function \(h_v\) and a nonempty compact convex carrier \(C_v\). The collapsed profile has indicator \(-\infty\) and empty carrier.

Let \(\mathcal J(u_1,\ldots,u_k)\) denote the set of indicator tuples obtained from simultaneous profile convergence on one escaping real sequence. This definition and its full finite-coordinate extraction are proved in Joint logarithmic-frequency limits, Definition 4.1 and Theorem 4.2. Every input profile has a global linear imaginary-growth upper bound, and every normalized input family is locally uniformly bounded above along escaping frequencies.

For indicator sums adopt

\[
 (-\infty)+h=h+(-\infty)=-\infty,\qquad
 (-\infty)+(-\infty)=-\infty. \tag{1.2}
\]

Proper indicators are finite, so no \(+\infty\) is involved. At the carrier level, the corresponding convention is \(C+\varnothing=\varnothing+C=\varnothing\).

**Theorem 1.1.** Let \(u'_j,u''_j\) be compact distributions on the same \(\mathbb R^n\), for \(1\leq j\leq k\). Then

\[
 \begin{split}
 &\mathcal J(u'_1*u''_1,\ldots,u'_k*u''_k)\\
 &\quad=
 \left\{(h'_1+h''_1,\ldots,h'_k+h''_k):
 (h'_1,\ldots,h'_k,h''_1,\ldots,h''_k)
 \in\mathcal J(u'_1,\ldots,u'_k,u''_1,\ldots,u''_k)\right\}.
 \end{split} \tag{1.3}
\]

The right side uses a joint \(2k\)-coordinate family. It is not the Cartesian product of separately chosen families of the primed and double-primed factors. The theorem includes zero distributions, smooth factors, and mixtures of proper and collapsed coordinates.

For every tuple in this identity, its output carrier in coordinate \(j\) is

\[
 C_j=C'_j+C''_j, \tag{1.4}
\]

with the empty-set convention above. This statement concerns the carriers selected by that common frequency sequence, rather than the ordinary supports of the distributions.

## 2. Convolution, limits and indicators

**Lemma 2.1 (no Fourier normalization factor).** For compact distributions \(a,b\),

\[
 F_{a*b}(\zeta)=F_a(\zeta)F_b(\zeta),\qquad
 L_{a*b}(z,c)=L_a(z,c)+L_b(z,c). \tag{2.1}
\]

The second identity holds with extended values at every transform zero.

*Proof.* Define compact convolution by
\(\langle a*b,\phi\rangle=\langle a_x,\langle b_y,\phi(x+y)\rangle\rangle\).
Use fixed compact cutoffs equal to one near the two supports when a test function is not compact in the separate variables. The inner pairing is smooth in \(x\): differentiating the test function in \(x\) is valid in every test-function seminorm on the fixed compact support of \(b\), and the distribution pairing is continuous in those seminorms. The outer pairing is therefore defined. The sum of the two supports is compact, so \(a*b\) is compactly supported.

More explicitly, finite-order bounds for the two distributions, of orders \(m_a\) and \(m_b\) on fixed compact cutoff supports, bound the nested action by a fixed constant times the supremum of the derivatives of \(\phi\) through order \(m_a+m_b\) on their compact sum. Fixed cutoff derivatives only change the constant. This proves continuity in the test-function topology. If \(\phi\) vanishes near the sum of the actual supports, compactness supplies separate neighborhoods of those supports on whose sum it vanishes; the nested action is then zero. Thus the support claim also uses the actual supports, independently of the chosen larger cutoff sets.

For the exponential test, the inner pairing is
\(e^{-ix\cdot\zeta}F_b(\zeta)\). Pairing this with \(a\) proves the first identity. With convention (1.1), the factor \((2\pi)^{-n}\) occurs in inverse Fourier integration and does not occur in this forward product identity. Taking logarithmic moduli and dividing by the same positive \(\log|c|\) proves the second identity. If either transform vanishes at a point, the product and the extended sum both have logarithmic value \(-\infty\). \(\square\)

**Lemma 2.2 (proper sums).** If \(L_a(\cdot,c_\nu)\to v_a\) and \(L_b(\cdot,c_\nu)\to v_b\) in local \(L^1\), with proper limits, then the convolution profiles converge in local \(L^1\) to the proper PSH function \(v_a+v_b\).

*Proof.* Proper PSH functions are locally integrable and finite almost everywhere. The intersection of their finite full-measure sets is still full measure, so their sum is not identically \(-\infty\). Their sum is PSH: upper semicontinuity and the line submean inequalities add, with no positive infinite values.

The exact identity in Lemma 2.1 holds almost everywhere for these nonzero entire transforms. For every compact observation region,
\[
 \|L_{a*b}-v_a-v_b\|_{L^1}
 \leq\|L_a-v_a\|_{L^1}+\|L_b-v_b\|_{L^1}\longrightarrow0. \tag{2.2}
\]
The zeros of a nonzero entire transform have zero volume; the full logarithmic local-integrability proof is supplied in Scalar holomorphic logarithms. Thus the extended pointwise equalities cause no obstruction to (2.2). The sum is the canonical PSH representative of this limit, by uniqueness of the local \(L^1\) profile. \(\square\)

**Lemma 2.3 (collapsed sums).** If either input profile collapses uniformly locally to \(-\infty\), then the convolution profile also collapses uniformly locally. This conclusion does not require convergence of the other input.

*Proof.* On every fixed compact parameter set \(B\), ordinary compact Fourier growth gives an upper bound \(M_B\) for the other input normalized logarithms for all sufficiently large frequencies. If the first input has supremum \(A_\nu\to-\infty\) on \(B\), Lemma 2.1 gives
\[
 \sup_B L_{a*b}(\cdot,c_\nu)\leq A_\nu+M_B\longrightarrow-\infty. \tag{2.3}
\]
The same argument interchanges the inputs. It also covers identically zero input transforms. \(\square\)

**Lemma 2.4 (indicator and carrier addition).** For two proper input profiles,
\[
 h_{v_a+v_b}=h_{v_a}+h_{v_b},\qquad
 C_{v_a+v_b}=C_{v_a}+C_{v_b}. \tag{2.4}
\]
With a collapsed input, the corresponding indicator and carrier are given by (1.2).

*Proof.* Proper input profiles satisfy global linear imaginary-growth bounds. Their proper sum also satisfies such a bound. The exact indicator additivity theorem in Directional averages and additivity of growth indicators, Theorem D4, applies. Its complete proof in Section D6 identifies the directional indicator by integral convergence and then integrates the sum identity. It does not add finite-height suprema: those suprema need not add.

For nonempty compact convex sets, their Minkowski sum is compact and convex. A maximizing point can be chosen separately in each compact set, so its support function is the sum of their support functions. The uniqueness of compact convex sets from their support functions, proved in Plurisubharmonic envelopes and support functions, gives the carrier equality. With a collapsed input, Lemma 2.3 makes the sum collapsed and both sides have empty carrier. \(\square\)

## 3. Prove both inclusions on the same sequence

*Proof of Theorem 1.1: left to right.* Choose any tuple on the left. By definition it is realized by a common escaping sequence \(c_\nu\) on which all \(k\) product profiles converge, properly or by collapse. Their indicators are the prescribed tuple.

Apply finite-coordinate compactness to all \(2k\) input families along that very sequence. Repeated extraction gives a further common subsequence on which every input has a proper or collapsed limit \(v'_j,v''_j\). The original product limits are unchanged on the further subsequence.

If both inputs in coordinate \(j\) are proper, Lemma 2.2 says the product has canonical profile \(v'_j+v''_j\). It cannot have a collapsed profile, and uniqueness identifies this with its originally prescribed proper limit. Lemma 2.4 identifies its indicator with \(h'_j+h''_j\).

If either input coordinate is collapsed, Lemma 2.3 forces its product coordinate to collapse. The prescribed output indicator is therefore \(-\infty=h'_j+h''_j\). This covers every coordinate, including tuples with both kinds of output. The extracted input indicator tuple belongs to the joint family on the right, and produces the chosen left tuple. This proves the first inclusion.

*Right to left.* Choose any full \(2k\)-coordinate joint tuple on the right. Its definition provides a single escaping sequence and simultaneous input profiles \(v'_j,v''_j\). On that same sequence, apply Lemma 2.2 wherever both profiles are proper, and Lemma 2.3 wherever at least one collapses. Every product coordinate converges, with no further choice of frequencies required. Lemma 2.4 and the extended convention identify all output indicators with \(h'_j+h''_j\). Consequently the entire resulting \(k\)-tuple belongs to the family on the left. This proves the second inclusion, and (1.4) follows coordinate by coordinate. \(\square\)

**Corollary 3.1 (finitely many factors).** The same statement holds for \(s\) compact factors in each of \(k\) coordinates, using a common \(sk\)-coordinate input family and summing its indicators coordinatewise.

*Proof.* Along a common input sequence, apply Lemmas 2.2–2.4 repeatedly. If any factor in a coordinate collapses, the whole coordinate collapses; otherwise the finite proper sum converges in local \(L^1\) and its indicator is the sum of all factor indicators. Conversely, start with a joint output sequence and extract all finitely many input profiles on a common subsequence. The same alternatives identify the already specified output profiles. These are exactly the two inclusions used above, with a finite sum in place of a pair. \(\square\)

## References

- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), for named background on entire Fourier transforms. Its normalization differs from (1.1); no source text or proof is imported.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 1983, Chapter VII, for background on compact distributions and entire Fourier transforms.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Springer, 1983, Chapter XVI, for joint convolution families. Both inclusions, all mixed cases and the exact normalization are proved above.
