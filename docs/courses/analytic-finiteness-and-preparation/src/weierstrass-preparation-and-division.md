# Weierstrass preparation and division

**Human source and reuse terms.** The preparation, division and local parametrization treatment below is adapted from Jean-Pierre Demailly, *[Complex Analytic and Differential Geometry](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf)*, version of 21 June 2012. Demailly remains the author of that treatment. His [publication page](https://www-fourier.univ-grenoble-alpes.fr/~demailly/documents.html) describes the book as OpenContent and expressly permits printing, spreading and modifying it on the web, except claiming authorship. This is the author's custom grant; no Creative Commons licence is substituted for it. This adapted lesson is distributed under that grant and is excluded from the course's CC0 dedication.

**Adaptation provenance.** GPT-6.1 Sol (OpenAI), Ultra, October 2026, reorganized and transcribed the selected arguments into this course's notation, supplied elementary algebra details and a Cauchy extension argument, expanded the passage from germs to global components and constant rank, and wrote the exercises and solutions. These additions are identified below. Demailly attributes the Cauchy division method to C. L. Siegel. This is an adaptation with added explanations, not an independently authored replacement of Demailly's treatment. The additions have received an author self-check; independent review and the programme's transitive prerequisite closure remain open.

This reading selects the complete preparation, Cauchy division and Noetherianity arguments from the existing analytic lesson, followed by its multiplicity exercise and complete solution. It supplies the division input for [analytic finiteness and ordinary preparation](../analytic-finiteness-for-preparation.html). The source author's custom terms apply to this selection.

We write \(\mathcal O_n=\mathbb C\{z_1,\ldots,z_n\}\). Germs are taken at zero. The analytic inputs used here are the one-variable Cauchy formula, removable singularities, the argument principle, the identity theorem and continuity of polynomial roots.

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

A nonzero germ can always be prepared after a linear coordinate change. If \(g_m\) is its first nonzero homogeneous term, choose the last coordinate direction \(v\) with \(g_m(v)\ne0\). This direction can be chosen simultaneously for finitely many nonzero germs, since a finite union of proper polynomial zero sets does not cover the vector space.

There is a useful stronger estimate when the order of \(g\) at zero is \(s\). Its prepared coefficients satisfy \(a_j(z')=O(|z'|^j)\). To see the underlying root estimate, write
\(g(z',w)=c w^s+\) the other degree-\(s\) terms \(+\) higher terms, with \(c\ne0\). If \(|w|\ge C|z'|\) and \(w\) is small, the other terms are smaller than \(|c w^s|/2\), after choosing \(C\) large and the neighbourhood small. Hence every zero satisfies \(|w|\le C|z'|\). Taking elementary symmetric functions of the roots proves the coefficient estimate. This expanded estimate is an adaptation detail used below.

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

Induction proves that \(\mathcal O_n\) is Noetherian. For a nonzero ideal \(J\), prepare some element and thus place a polynomial \(P\) of degree \(s\) in \(J\). The remainders of elements of \(J\) form an \(\mathcal O_{n-1}\)-submodule of
\(\bigoplus_{j=0}^{s-1}\mathcal O_{n-1}w^j\). It is finitely generated, and those generators together with \(P\) generate \(J\). For \(n=0\) this is the field \(\mathbb C\). The module fact used in this induction has a short proof: project a submodule of \(R^s\) onto its last coordinate, generate the resulting ideal, lift its generators and then generate the kernel by induction on \(s\). This fills an algebra detail in the adapted proof.

## Exercise and complete solution

### 1. Multiplicity in division

*Difficulty: Introductory.*

For \(P(w)=w^3\), divide \(f(w)=e^w\). Explain why checking distinct zeros alone does not prove uniqueness.

**Solution.** The remainder is \(R=1+w+w^2/2\) and
\(q=(e^w-1-w-w^2/2)/w^3\), extended holomorphically at zero with value \(1/6\). A polynomial such as \(w\) vanishes at the only distinct zero, but is not divisible holomorphically by \(w^3\). Uniqueness requires the three zeros counted with multiplicity, or equality of the first three Taylor coefficients.
