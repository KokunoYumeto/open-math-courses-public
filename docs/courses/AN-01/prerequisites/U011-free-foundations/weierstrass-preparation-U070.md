# Weierstrass preparation and division

**Human source and reuse terms.** The preparation, division and local parametrization treatment below is adapted from Jean-Pierre Demailly, *[Complex Analytic and Differential Geometry](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf)*, version of 21 June 2012. Demailly remains the author of that treatment. His [publication page](https://www-fourier.univ-grenoble-alpes.fr/~demailly/documents.html) describes the book as OpenContent and expressly permits printing, spreading and modifying it on the web, except claiming authorship. This is the author's custom grant; no Creative Commons licence is substituted for it. This adapted lesson is distributed under that grant and is excluded from the course's CC0 dedication.

**Adaptation.** GPT-6.1 Sol (OpenAI), Ultra, October 2026, reorganized and transcribed the selected arguments into this course's notation, supplied elementary algebra details and a Cauchy extension argument, expanded the passage from germs to global components and constant rank, and wrote the exercises and solutions. These additions are identified below. Demailly attributes the Cauchy division method to C. L. Siegel. This is an adaptation with added explanations, not an independently authored replacement of Demailly's treatment. The additions are self-checked by the writing AI; not every result they depend on, directly or through earlier results, is proved in these lessons.

This selection retains the existing preparation and Cauchy division proofs. Demailly’s authorship and custom terms remain in force. The algebraic consequences and unrelated exercises are outside this selected component.

The supplied [contour foundation](complex-contours-U070.md), §§16.1–16.6, gives power series, isolated zeros, jointly holomorphic integrals, winding, finite-pole residues and the maximum principle. [Polynomial roots](polynomial-roots-U070.md), §9, supplies all multiplicities. The finite symmetric-coefficient identity is proved in the receiving note below.

## Preparation by the zeros in one fibre

This section adapts Demailly's preparation argument. Let \(g\in\mathcal O_n\) and suppose \(w\mapsto g(0,w)\), with \(w=z_n\), has a zero of finite order \(s\) at zero. Choose a small vertical circle \(|w|=r\) without zeros and then a small base polydisc so that \(g(z',w)\ne0\) on an annulus about that circle. The argument principle gives

\[
S_j(z')=\frac1{2\pi i}\int_{|w|=r}
w^j\frac{\partial_wg(z',w)}{g(z',w)}\,dw.
\tag{2}
\]

Each \(S_j\) is holomorphic in \(z'\). The integer \(S_0\) is continuous and hence constant, equal to \(s\). For \(j\ge1\), \(S_j\) is the power sum of the \(s\) fibre zeros, counted with multiplicity. Newton's identities express their elementary symmetric functions as holomorphic functions. Thus the monic polynomial

\[
P(z',w)=w^s+a_1(z')w^{s-1}+\cdots+a_s(z'),
\qquad a_j(0)=0,
\tag{3}
\]

has exactly the zeros of \(g\) inside the circle, with the same multiplicities. On each fibre both \(g/P\) and \(P/g\) have removable singularities. Their Cauchy integrals over the fixed circle make these extensions jointly holomorphic. They remain inverse to one another by the identity theorem. Consequently \(g=uP\), where \(u\) is a holomorphic unit. Uniqueness follows from the zeros and the monic normalization.

## Division, finite generation and elementary algebra

Demailly's division proof uses the following Cauchy formula. For \(P\) as in (3) and a holomorphic \(f\), shrink so that \(f\) is holomorphic on a neighbourhood of the closed adapted polydisc. Define

\[
\begin{aligned}
q(z',w)&=\frac1{2\pi i}\int_{|\zeta|=r}
\frac{f(z',\zeta)}{P(z',\zeta)(\zeta-w)}\,d\zeta,\\
R(z',w)&=\frac1{2\pi i}\int_{|\zeta|=r}
\frac{f(z',\zeta)}{P(z',\zeta)}
\frac{P(z',\zeta)-P(z',w)}{\zeta-w}\,d\zeta.
\end{aligned}
\tag{4}
\]

The Cauchy formula gives \(f=qP+R\); the difference quotient makes \(R\) a polynomial in \(w\) of degree less than \(s\), with holomorphic coefficients in \(z'\). Uniqueness follows on each fibre: if a polynomial of degree less than \(s\) is divisible by \(P\) as a holomorphic function, it has all \(s\) zeros with multiplicity and is zero. The quotient is then zero as well.

The division can be performed on a common smaller polydisc for all bounded holomorphic \(f\). On the boundary annulus, \(P\) has a fixed positive lower bound. Formula (4) bounds \(R\) by a constant times the supremum of \(f\). Then \(q=(f-R)/P\) has the same kind of boundary bound, which extends to the interior by the maximum principle on each vertical disc. The constant depends on \(P\) and the polydiscs, not on \(f\).

## Receiving details and finite symmetric coefficients

*AN-01 receiving note, GPT-6 Astra (OpenAI), Ultra, October 2026; CC0 additions. The two preceding adapted arguments retain Demailly's terms.*

The zero-free annulus and compactness put only finitely many isolated zeros in each fibre disk. Factoring their local power series gives the residue of $w^j g'/g$ at a zero $\lambda$ of order $m$ as $m\lambda^j$, with $m$ for $j=0$. The supplied residue theorem therefore proves the integer count and every moment in (2), without presuming continuously labelled roots. The dominated product-circle argument proves joint holomorphy of every parameter integral. At a common zero, cancel the same power of $w-\lambda$ in the two local series; their remaining constant coefficients are nonzero. This proves both fibrewise removable quotients used above.

For uniqueness as germs, choose a common small product on which both proposed units are nonzero. The coefficients of either monic polynomial vanish at the base mark. For any fixed small $r>0$, shrink the base so that

$$
 \sum_{j=0}^{s-1}|b_j(z')|r^{j-s}<1.
$$

For $|w|\ge r$, the lower terms then have total modulus strictly below $|w|^s$; hence every root of either polynomial lies in $|w|<r$. Their roots with multiplicities equal those of the original function there. Full complex factorization and monicity make the polynomials equal; cancellation off their zeros and continuity make the units equal. This also proves the fibrewise multiplicity argument for uniqueness of division. On a common smaller polydisc, fixed-contour denominators are uniformly bounded away from zero, proving the asserted bounds for bounded dividends. Dividing the polynomial quotient by the original unit gives division by the original function.

The following finite identity is the unchanged AN-01 symmetric-coefficient proof. It does not use preparation or root continuity.

### A finite identity that does not distinguish repeated roots

For any list \(\lambda_1,\ldots,\lambda_k\in\mathbb C\), repetitions allowed, define

\[
S_\ell=\sum_{i=1}^k\lambda_i^\ell\quad(\ell\ge1),\qquad
e_0=1,\qquad
e_j=\sum_{1\le i_1<\cdots<i_j\le k}
\lambda_{i_1}\cdots\lambda_{i_j}\quad(1\le j\le k).
\tag{N1}
\]

The indices in the definition of \(e_j\) select occurrences in the list, even when their values coincide. Set \(e_j=0\) for \(j>k\). The finite Newton identities are

\[
j e_j=\sum_{\ell=1}^j(-1)^{\ell-1}e_{j-\ell}S_\ell,
\qquad 1\le j\le k.
\tag{N2}
\]

**Proof.** Work first in the polynomial ring
\(R=\mathbb C[\lambda_1,\ldots,\lambda_k]\), treating the \(\lambda_i\) as indeterminates. Introduce a formal variable \(X\) and the finite polynomial

\[
E(X)=\prod_{i=1}^k(1+\lambda_iX)
     =\sum_{j=0}^k e_jX^j.
\tag{N3}
\]

Each factor has constant coefficient one, so it is invertible in \(R[[X]]\), with formal inverse
\(\sum_{m\ge0}(-\lambda_iX)^m\). Formal differentiation of the finite product gives

\[
\begin{aligned}
E'(X)
&=\sum_{i=1}^k\lambda_i\prod_{h\ne i}(1+\lambda_hX)\\
&=E(X)\sum_{i=1}^k\frac{\lambda_i}{1+\lambda_iX}\\
&=E(X)\sum_{\ell\ge1}(-1)^{\ell-1}S_\ell X^{\ell-1}.
\end{aligned}
\tag{N4}
\]

Equality of the coefficients of \(X^{j-1}\) is exactly (N2). There is no analytic convergence or division by a root. To make the argument entirely finite, truncate each geometric inverse after degree \(k-1\) and work modulo \(X^k\); its product with \(1+\lambda_iX\) is one modulo \(X^k\). This determines all the coefficients used in (N2). Finally specialize the indeterminates to the given complex numbers. Polynomial identities remain valid when values coincide or vanish. \(\square\)

Since division by the positive integer \(j\) is allowed in \(\mathbb C\), (N2) recursively expresses every \(e_j\), \(1\le j\le k\), as a polynomial with rational coefficients in \(S_1,\ldots,S_j\). For indices not exceeding \(k\),

\[
e_1=S_1,\qquad
e_2=\frac{S_1^2-S_2}{2},\qquad
e_3=\frac{S_1^3-3S_1S_2+2S_3}{6}.
\tag{N5}
\]

For the descending coefficients of

\[
P(w)=\prod_{i=1}^k(w-\lambda_i)
    =w^k+A_1w^{k-1}+\cdots+A_k,
\tag{N6}
\]

we have \(A_0=1\) and \(A_j=(-1)^je_j\). Thus the equivalent coefficient recursion is

\[
jA_j+\sum_{\ell=1}^j A_{j-\ell}S_\ell=0,
\qquad 1\le j\le k.
\tag{N7}
\]

For example, where the indices do not exceed \(k\), \(A_1=-S_1\), \(A_2=(S_1^2-S_2)/2\), and
\(A_3=(-S_1^3+3S_1S_2-2S_3)/6\). These signs correspond to the factors \(w-\lambda_i\).

