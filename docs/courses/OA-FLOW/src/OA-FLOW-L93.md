# Norm-continuous groups in a Banach algebra

A norm-continuous one-parameter group in a unital Banach algebra has a bounded generator and is an exponential. The existence of that generator can be seen directly by averaging the group near zero. A local logarithm gives a second route and explains the construction used in Takesaki II, Lemma XI.1.17. The same lemma places the generator's spectrum on the imaginary axis when every group element has norm one.

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

The norm integrals, fundamental theorem and absolutely convergent products are proved in CF1; the Neumann inverse and spectral bounds are in CF2. [AF4](OA-FLOW-AF.md#af-4) proves the precise logarithm identities and full exponential spectral mapping, including an arbitrary identity norm. Here \(\operatorname{GL}(A)\) denotes the multiplicative group of invertible elements of \(A\).

<a id="oa-flow.frequency.banachexponential"></a>

<a id="OA-FLOW.BGROUP.EXPONENTIAL"></a><a id="oa-flow.bgroup.exponential"></a>

## Exponentials give norm-continuous groups

Let \(A\) be a complex unital Banach algebra with identity \(1\), and let \(h\in A\). The series

<a id="equation-b1"></a>

$$g_h(t)=\exp(th):=\sum_{n=0}^{\infty}\frac{t^nh^n}{n!}\tag{B1}$$

converges absolutely and uniformly in norm on bounded intervals of \(t\in\mathbb R\). The usual Cauchy-product rearrangement is justified by absolute convergence and gives \(g_h(s+t)=g_h(s)g_h(t)\). In particular \(g_h(t)^{-1}=g_h(-t)\). Termwise differentiation, again uniform on bounded intervals, gives

<a id="equation-b2"></a>

$$g_h'(t)=h g_h(t)=g_h(t)h.\tag{B2}$$

Thus \(t\mapsto g_h(t)\) is a norm-continuous group of invertible elements, differentiable in the Banach-algebra norm.

<a id="OA-FLOW.BGROUP.AVERAGING"></a><a id="oa-flow.bgroup.averaging"></a>

## Averaging recovers a bounded generator

Conversely let \(g:\mathbb R\to\operatorname{GL}(A)\) be a norm-continuous homomorphism. The group law makes all \(g(t)\) commute and gives \(g(0)=1\). Choose \(d>0\) so small that \(\|g(u)-1\|<1/2\) for \(0\le u\le d\), and form the norm integral \(B=\int_0^d g(u)\,du\). Then \(\|d^{-1}B-1\|<1/2\), so \(B\) is invertible by a Neumann series.

Translation of the integral by the group law gives, for real \(t\),

<a id="equation-b3"></a>

$$g(t)B=\int_t^{t+d}g(u)\,du,\qquad
\frac{g(t)-1}{t}B
=\frac1t\left(\int_d^{d+t}g(u)\,du-\int_0^t g(u)\,du\right).\tag{B3}$$

Both average integrals on the right have norm limits as \(t\to0\), from either sign of \(t\), so

<a id="equation-b4"></a>

$$h:=\lim_{t\to0}\frac{g(t)-1}{t}
=(g(d)-1)B^{-1}\in A.\tag{B4}$$

The group law now gives \(g'(t)=g(t)h=hg(t)\). Differentiating \(\exp(-th)g(t)\) shows it is constant and equals \(1\) at zero. Hence

<a id="equation-b5"></a>

$$g(t)=\exp(th)\quad(t\in\mathbb R),\qquad
h=g'(0)\text{ is unique}.\tag{B5}$$

This proof uses norm continuity and elementary Banach integration only. In particular, no differentiability hypothesis was inserted into the converse.

<a id="OA-FLOW.BGROUP.LOGARITHM"></a><a id="oa-flow.bgroup.logarithm"></a>

## The local logarithm and its branch control

For comparison with the source construction, shrink an interval \((-d_0,d_0)\) until \(\|g(t)-1\|<1/10\) there. Define

<a id="equation-b6"></a>

$$L(t)=\log g(t)
=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}(g(t)-1)^n
\qquad(|t|<d_0).\tag{B6}$$

This series converges in norm. Its norm is at most \(-\log(9/10)<1/8\). If \(s,t,s+t\) all lie in the interval, the elements \(L(s)\) and \(L(t)\) commute. Their sum and \(L(s+t)\) have norm less than \(1/4\), within the exact ball on which \(\log(\exp z)=z\) by the complete differentiation-and-integral proof (AF14)–(AF15). That proof also gives \(\exp(\log(1+b))=1+b\) for \(\|b\|<1\). Since \(\exp(L(s)+L(t))=g(s)g(t)=g(s+t)\), the logarithm is locally additive:

<a id="equation-b7"></a>

$$L(s+t)=L(s)+L(t)
\quad(|s|,|t|,|s+t|<d_0).\tag{B7}$$

For arbitrary \(t\), set \(H(t)=nL(t/n)\) once \(|t/n|<d_0\). This does not depend on a sufficiently large integer \(n\): compare two choices using a common multiple and repeated applications of (B7), with every intermediate point remaining in the local interval. Choose one large \(n\) for \(s,t,s+t\) to see that \(H(s+t)=H(s)+H(t)\). Near zero \(H=L\), so \(H\) is continuous. Every continuous additive map \(\mathbb R\to A\) is of the form \(H(t)=tH(1)\): addition and negation give integer homogeneity, subdividing \(1\) gives rational homogeneity, and a sequence of rationals converging to \(t\), with continuity, gives the real identity. Finally \(\exp(H(t))=g(t/n)^n=g(t)\). Its generator \(H(1)\) equals the unique derivative \(h\) in (B4).

The small logarithm ball is the branch check omitted by a bare appeal to commutativity. Without it, equality of exponentials would determine logarithms only modulo possible periods.

<a id="OA-FLOW.BGROUP.IMAGINARY"></a><a id="oa-flow.bgroup.imaginary"></a>

## Norm-one groups have imaginary generator spectrum

Assume in addition \(\|g(t)\|=1\) for every real \(t\). Its inverse \(g(-t)\) also has norm one. For \(z\ne0\), the identity \(g(t)-z1=-z g(t)(g(t)^{-1}-z^{-1}1)\) proves that \(z\) is a spectral point of \(g(t)\) exactly when \(z^{-1}\) is one of its inverse; zero is excluded by invertibility. For any \(z\in\operatorname{Sp}_A(g(t))\), the spectral-radius bounds for \(g(t)\) and its inverse give \(|z|\le1\) and \(|z|^{-1}\le1\), so \(|z|=1\). The fully proved exponential spectral-mapping identity (AF16) yields

<a id="equation-b8"></a>

$$\operatorname{Sp}_A(g(t))
=\{e^{t\lambda}:\lambda\in\operatorname{Sp}_A(h)\}.\tag{B8}$$

For \(t\ne0\), every \(\lambda\in\operatorname{Sp}_A(h)\) therefore satisfies \(|e^{t\lambda}|=e^{t\operatorname{Re}\lambda}=1\), hence \(\operatorname{Re}\lambda=0\). Thus

<a id="equation-b9"></a>

$$\operatorname{Sp}_A(h)\subset i\mathbb R.\tag{B9}$$

**Problem.** Does the converse of (B9) hold? Take \(h=\begin{pmatrix}0&1\\0&0\end{pmatrix}\) in \(M_2(\mathbb C)\) with its operator norm.

**Solution.** Its spectrum is \(\{0\}\subset i\mathbb R\), but \(h^2=0\) makes \(\exp(th)=I+th\), whose norm grows without bound as \(|t|\to\infty\): its value on the unit vector \(e_2\) is \(te_1+e_2\), of norm \(\sqrt{1+t^2}\). Imaginary generator spectrum alone does not make the exponential group norm one. \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Lemma XI.1.17, printed pages 324–325 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). Both retained converses are complete: the averaging proof gives the bounded derivative, and the logarithm proof uses an explicit injective branch. AF4 supplies the actual full spectral-mapping proof used for the imaginary-spectrum conclusion. No Hille–Yosida theorem or holomorphic functional calculus is imported.
