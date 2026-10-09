# Van der Waerden numbers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Van der Waerden proved in 1927 that for all positive integers \(r\) and \(k\) there is a least integer \(W_r(k)\) such that every colouring of \(\{1,\dots,W_r(k)\}\) with \(r\) colours contains a monochromatic arithmetic progression of length \(k\). How fast \(W_r(k)\) grows is one of the oldest quantitative questions of Ramsey theory. For two colours, Erdős asked whether \(W_2(k)^{1/k}\to\infty\) [Erd]. Lower bounds came from Erdős and Rado, Schmidt, Berlekamp's algebraic construction, and the local lemma of Erdős and Lovász [EL]; Szabó, Kozik and Shabanov, and Hunter sharpened the exponential bounds. Fox and Hunter proved super-exponential growth for three colours [FH], and Campos, Fox and Schildkraut proved \(W_2(k)\ge(1-o(1))k2^{k-1}\) [CFS]. This course presents OpenAI's answer to Erdős's question, for every number of colours at once [OpenAI-vdW]:

**Theorem** (OpenAI 2026; Theorem 4.1 of [Norm bands and the two-colouring](norm-bands-and-the-two-colouring.md)). There is an absolute integer \(K_0\) such that for every integer \(k\ge K_0\) and every integer \(r\ge2\),
\[
W_r(k)>k^{ck\lfloor\log_2r\rfloor},\qquad c=10^{-5}.
\]
In particular \(W_r(k)^{1/k}\to\infty\) for every fixed \(r\ge2\).

The proof constructs a two-colouring of a cyclic group \(\mathbb Z/N\mathbb Z\) with \(N\ge k^{ck}\) that has no monochromatic \(k\)-term progression, and then extends it to many colours and to integer intervals by base-\(N\) digits. This first lesson proves the classical facts that frame the problem: van der Waerden's theorem with an explicit recursive bound (Section 2), the digit product (Section 3), and a Behrend-type colouring that shows super-polynomial growth in the number of colours (Section 4). [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md) collects the counting and probabilistic tools; [Coordinates, meshes and label counts](coordinates-meshes-and-label-counts.md) sets up the cyclic construction and its counts; [A balanced colouring and the dichotomy](a-balanced-colouring-and-the-dichotomy.md) builds an outer colouring with a structural dichotomy; and [Norm bands and the two-colouring](norm-bands-and-the-two-colouring.md) completes the proof.

## 1. Definitions

For a positive integer \(N\) write \([N]=\{1,\dots,N\}\). A *\(k\)-term arithmetic progression* in \([N]\) is a sequence \(a,a+d,\dots,a+(k-1)d\) of elements of \([N]\) with \(a,d\ge1\). For positive integers \(r,k\), \(W_r(k)\) is the least positive integer \(N\) such that every map \([N]\to[r]\) is constant on some \(k\)-term arithmetic progression in \([N]\); maps using fewer than \(r\) colours are allowed. To prove \(W_r(k)>N\) it suffices to give a colouring of \([N]\), or of any \(N\) consecutive integers, with at most \(r\) colours and no monochromatic \(k\)-term progression.

In the cyclic group \(\mathbb Z/N\mathbb Z\), a *\(k\)-term progression* is a sequence \(a,a+d,\dots,a+(k-1)d\) with \(a,d\in\mathbb Z/N\mathbb Z\) and \(d\ne0\); its terms need not be distinct.

## 2. Finiteness

**Theorem 2.1** (Van der Waerden). Define \(F(r,1)=1\) and \(F(r,2)=r+1\) for every integer \(r\ge1\). For \(k\ge3\) and \(r\ge1\), define
\[
m_0=1,\qquad m_{t+1}=2m_tF\bigl(r^{m_t},k-1\bigr)\quad(0\le t<r),\qquad F(r,k)=m_r .
\]
Then \(W_r(k)\le F(r,k)<\infty\) for all positive integers \(r,k\). Moreover
\[
W_r(1)=1,\qquad W_r(2)=r+1,\qquad W_1(k)=k .
\]

*Proof.* The recursion defines \(F(r,k)\) for all \(r\) once \(F(\cdot,k-1)\) is known, so all values are finite positive integers. A one-term progression is a single point, so \(W_r(1)=1\). Among \(r+1\) points coloured with \(r\) colours two have the same colour and form a two-term progression, while an injective colouring of \([r]\) has none; so \(W_r(2)=r+1\). With one colour, \([k]\) is itself a progression and \([k-1]\) contains none of length \(k\); so \(W_1(k)=k\).

For \(k\ge3\) we prove, by induction on \(k\) for all \(r\) simultaneously, that every \(r\)-colouring of \(F(r,k)\) consecutive integers contains a monochromatic \(k\)-term progression; the cases \(k=1,2\) were just shown. Fix \(k\ge3\) and \(r\ge1\), and call a colouring *avoiding* if it has no monochromatic \(k\)-term progression.

A *focus with \(t\) colours* in a coloured interval is a point \(f\) together with positive integers \(d_1,\dots,d_t\) such that all points \(f-sd_i\) (\(1\le s\le k-1\), \(1\le i\le t\)) lie in the interval, the \(k-1\) points of the arm \(i\) have a common colour \(a_i\), and \(a_1,\dots,a_t\) are distinct. In an avoiding colouring, \(f\) itself has a colour different from every \(a_i\): otherwise \(f-(k-1)d_i,\dots,f-d_i,f\) would be a monochromatic progression.

*Claim: for \(0\le t\le r\), every avoiding \(r\)-colouring of an interval of length \(m_t\) has a focus with \(t\) colours.* For \(t=0\) take the single point of an interval of length \(1\). Suppose the claim holds for \(t<r\); put \(m=m_t\), \(B=F(r^m,k-1)\), so \(m_{t+1}=2mB\), and let \(\chi\) be an avoiding colouring of \([2mB]\). Cut \([2mB]\) into \(2B\) consecutive blocks of length \(m\), and give block \(j\) its word \(w_j=(\chi((j-1)m+1),\dots,\chi(jm))\), one of at most \(r^m\) words. By the induction hypothesis on \(k-1\), applied to the colouring \(j\mapsto w_j\) of the first \(B\) block indices, there are \(b,\Delta\ge1\) with
\[
w_b=w_{b+\Delta}=\dots=w_{b+(k-2)\Delta},\qquad b+(k-2)\Delta\le B .
\]
As \(k-2\ge1\), \(\Delta\le B-1\), so \(q=b+(k-1)\Delta\le2B-1\) is the index of a block. The common word is an avoiding colouring of \([m]\) (it is a copy of block \(b\)), so by the claim for \(t\) it has a focus \(f\) with differences \(d_1,\dots,d_t\) and colours \(a_1,\dots,a_t\); let \(a_0\) be the colour of \(f\), different from all \(a_i\). Put \(f'=(q-1)m+f\). For \(1\le s\le k-1\),
\[
f'-s(m\Delta+d_i)=\bigl(b+(k-1-s)\Delta-1\bigr)m+(f-sd_i),\qquad f'-sm\Delta=\bigl(b+(k-1-s)\Delta-1\bigr)m+f .
\]
These are points of the matching blocks \(b+(k-1-s)\Delta\), at positions \(f-sd_i\) and \(f\), so they have the colours \(a_i\) and \(a_0\). Hence \(f'\) is a focus with the \(t+1\) colours \(a_0,a_1,\dots,a_t\), with differences \(m\Delta,m\Delta+d_1,\dots,m\Delta+d_t\). This proves the claim.

For \(t=r\), an avoiding colouring of \([m_r]\) would have a focus whose \(r\) arms use all \(r\) colours, and the focus could have none of them. So every \(r\)-colouring of \(F(r,k)=m_r\) consecutive integers contains a monochromatic \(k\)-term progression. \(\square\)

The bound \(F(r,k)\) grows extremely fast; the question addressed in this course is how small \(W_r(k)\) can be.

## 3. Digit products

**Proposition 3.1** (Digit product). Let \(N,k\ge2\), and let \(C:\mathbb Z/N\mathbb Z\to\{0,1\}\) be a colouring with no monochromatic \(k\)-term progression. Then \(W_{2^m}(k)>N^m\) for every positive integer \(m\), and \(W_r(k)>N^{\lfloor\log_2r\rfloor}\) for every integer \(r\ge2\).

*Proof.* Colour \(0\le n<N^m\), with base-\(N\) digits \(n=\sum_{i=0}^{m-1}n_iN^i\), by the vector \((C(n_0),\dots,C(n_{m-1}))\in\{0,1\}^m\), a digit being read as a residue modulo \(N\). Suppose \(a,a+d,\dots,a+(k-1)d\) is a monochromatic progression in \([0,N^m)\) with \(d\ge1\). Then \(d<N^m\), so there is a largest \(i\le m-1\) with \(N^i\mid d\); put \(e=d/N^i\), so \(N\nmid e\). Since \(je\) is an integer,
\[
\Bigl\lfloor\frac{a+jd}{N^i}\Bigr\rfloor=\Bigl\lfloor\frac a{N^i}\Bigr\rfloor+je\qquad(0\le j<k),
\]
and reducing modulo \(N\) shows that the \(i\)-th digits form a progression of \(\mathbb Z/N\mathbb Z\) with step \(e\not\equiv0\). Monochromaticity would make \(C\) constant on it. Shifting \([0,N^m)\) to \([N^m]\) gives a colouring with \(2^m\) colours and no monochromatic \(k\)-term progression. For \(r\ge2\) take \(m=\lfloor\log_2r\rfloor\), so \(2^m\le r\). \(\square\)

## 4. Many colours: a digit-and-sphere colouring

**Theorem 4.1.** For all integers \(r\ge256\) and \(k\ge3\),
\[
W_r(k)>\exp\Bigl(\frac{(\log r)^2}{64\log2}\Bigr).
\]

*Proof.* Put \(b=\lfloor r^{1/4}\rfloor\ge4\) and \(s=\lfloor\log r/(4\log2)\rfloor\ge2\). Split the digits \(\{0,\dots,b-1\}\) into the halves \(H_0=\{0,\dots,\lceil b/2\rceil-1\}\) and \(H_1=\{\lceil b/2\rceil,\dots,b-1\}\), and let \(\epsilon(u)\in\{0,1\}\) record the half containing \(u\). Colour \(0\le n<b^s\), with base-\(b\) digit vector \(x=(x_0,\dots,x_{s-1})\), by
\[
\Bigl(\epsilon(x_0),\dots,\epsilon(x_{s-1}),\ \textstyle\sum_ix_i^2\Bigr).
\]
There are at most \(2^s(1+s(b-1)^2)\le2^s(s+1)b^2\le r^{1/4}\cdot r^{1/4}\cdot r^{1/2}=r\) colours, using \(s+1\le2^s\le r^{1/4}\) and \(b^2\le r^{1/2}\).

Suppose three equally spaced integers with digit vectors \(x,y,z\) have one colour. Then \(\sum_i(x_i-2y_i+z_i)b^i=0\). For each \(i\), the digits \(x_i,y_i,z_i\) lie in one half, of diameter at most \(\lceil b/2\rceil-1\), so \(|x_i-2y_i+z_i|\le2(\lceil b/2\rceil-1)<b\). Reading the equation modulo \(b\) shows that the coefficient of \(b^0\) is divisible by \(b\), hence zero; dividing by \(b\) and repeating gives \(x+z=2y\). Equal colours also give \(\|x\|^2=\|y\|^2=\|z\|^2\), so
\[
\|x-z\|^2=2\|x\|^2+2\|z\|^2-\|x+z\|^2=2\|x\|^2+2\|z\|^2-4\|y\|^2=0,
\]
and the three integers coincide. So no progression with positive step and at least three terms is monochromatic, and \(W_r(k)>b^s\).

Finally, with \(L=\log r\ge8\log2\) and \(\lfloor u\rfloor\ge u/2\) for \(u\ge1\): \(s\ge L/(8\log2)\) and \(\log b\ge L/4-\log2\ge L/8\), so \(\log b^s\ge L^2/(64\log2)\). \(\square\)

For fixed \(k\ge3\), Theorem 4.1 shows that \(W_r(k)/r^A\to\infty\) as \(r\to\infty\) for every \(A>0\): growth in the number of colours is super-polynomial. The squared-norm idea is Behrend's [Beh]; it returns in a randomized form in the last lesson.

## 5. Exercises

**5.1.** Show that the colouring \((0,0,1,1)\) of \(\mathbb Z/4\mathbb Z\) has no monochromatic \(3\)-term progression (with nonzero step, terms allowed to repeat), and deduce \(W_4(3)>16\).

**5.2.** Compute \(F(2,3)\) from the recursion of Theorem 2.1 and compare it with \(W_2(3)=9\).

**5.3.** Show that the hypothesis \(N\nmid e\) is what makes the \(i\)-th digits in the proof of Proposition 3.1 form a progression with nonzero step, and give an example where the lowest digit of a progression is constant.

**5.4.** For \(b=4\) and \(s=2\), list the colours of Theorem 4.1 on \(\{0,\dots,15\}\) and check that no three-term progression with positive step is monochromatic.

## 6. Solutions

**5.1.** The progressions with step \(1\) or \(3\) contain three consecutive residues (in some order), which take both colours. The step \(2\) gives \(a,a+2,a\), and \(a\), \(a+2\) have different colours. By Proposition 3.1 with \(N=4\), \(m=2\): \(W_4(3)>16\).

**5.2.** \(m_0=1\), \(m_1=2\cdot1\cdot F(2,2)=2\cdot3=6\), \(m_2=2\cdot6\cdot F(2^6,2)=12\cdot65=780\). So \(F(2,3)=780\), far above \(W_2(3)=9\).

**5.3.** The \(i\)-th digit of \(a+jd\) is \(\lfloor a/N^i\rfloor+je\) modulo \(N\), a progression with step \(e\bmod N\); this step is nonzero because \(N\nmid e\). Lower digits can be constant: for \(N=10\) and the progression \(10,20,30\), the lowest digit is always \(0\), while the tens digit runs through \(1,2,3\).

**5.4.** The halves are \(\{0,1\}\) and \(\{2,3\}\), and \(n=x_0+4x_1\) has colour \((\epsilon(x_0),\epsilon(x_1),x_0^2+x_1^2)\). In the order \(n=0,\dots,15\) the colours are \((0,0,0)\), \((0,0,1)\), \((1,0,4)\), \((1,0,9)\), \((0,0,1)\), \((0,0,2)\), \((1,0,5)\), \((1,0,10)\), \((0,1,4)\), \((0,1,5)\), \((1,1,8)\), \((1,1,13)\), \((0,1,9)\), \((0,1,10)\), \((1,1,13)\), \((1,1,18)\). The only repeated colours are \((0,0,1)\), on \(\{1,4\}\), and \((1,1,13)\), on \(\{11,14\}\). Every colour class has at most two elements, so no three-term progression is monochromatic.

## References

- [OpenAI-vdW] OpenAI, *Quantitative superexponential bounds for van der Waerden numbers*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf
- [Erd] P. Erdős, *A survey of problems in combinatorial number theory*, Annals of Discrete Mathematics 6 (1980). https://www.renyi.hu/~p_erdos/1980-03.pdf
- [EL] P. Erdős and L. Lovász, *Problems and results on 3-chromatic hypergraphs and some related questions*, in Infinite and Finite Sets II (1975). https://www.renyi.hu/~p_erdos/1975-34.pdf
- [FH] J. Fox and Z. Hunter, *Three-color van der Waerden numbers grow super-exponentially*, 2026. https://arxiv.org/abs/2606.02541
- [CFS] M. Campos, J. Fox and C. Schildkraut, *A new lower bound for two-color van der Waerden numbers*, 2026. https://arxiv.org/abs/2608.20824
- [Beh] F. A. Behrend, *On sets of integers which contain no three terms in arithmetical progression*, Proceedings of the National Academy of Sciences 32 (1946), 331–332. https://pmc.ncbi.nlm.nih.gov/articles/PMC1078964/
