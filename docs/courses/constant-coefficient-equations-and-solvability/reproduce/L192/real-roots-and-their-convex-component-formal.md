# Real roots and their convex component

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A homogeneous polynomial can have real roots on every line in one direction. We prove that this direction determines an open convex component, that every direction in the component has the same real-root property, and that the whole imaginary tube over the component contains no zero. Multiple roots and complex coefficients are included.

The proof separates a one-variable root operation from a compactness argument for directions. It uses Nuij's perturbation to remove multiple roots temporarily, then passes back to the original polynomial. Basic references are Nuij [N], Harvey and Lawson [L], and the preceding chapter [Cauchy bounds, root counts and analytic extensions][C]. That chapter supplies Rouché's theorem and the root continuity used below. The required arguments are given here.

For the polynomial factorizations, [C], Corollary 2.3, supplies the full-degree root count: on a sufficiently large circle, a polynomial's leading monomial strictly dominates the sum of its lower terms. Rouché gives exactly its degree many roots counted with multiplicity. Dividing by their linear factors gives the factorization. Small disjoint circles then give the root continuity used throughout this chapter.

## 1. Normalize the coefficients and specify the component

Let \(F\) be a homogeneous polynomial of positive degree \(m\), with complex coefficients, and let \(e\in\mathbb R^n\) satisfy \(F(e)\ne0\). Assume that
\[
                   F(x+te)=0\quad\Longrightarrow\quad t\in\mathbb R
                    \qquad(x\in\mathbb R^n).
 \tag{1}
\]
Set \(p=F/F(e)\), so \(p(e)=1\). We call a real vector \(v\) a hyperbolic direction for \(p\) if \(p(v)\ne0\) and every polynomial \(t\mapsto p(x+tv)\), for real \(x\), has only real roots.

**Lemma 1.1 (reality).** The normalized polynomial \(p\) has real coefficients.

**Proof.** For every real \(x\), the polynomial \(p(x+te)\) is monic of degree \(m\). Its real roots, with multiplicities, express it as a product of real monic linear factors. In particular its constant term \(p(x)\) is real. The imaginary part of \(p\) is therefore a real polynomial vanishing on every real point. Such a polynomial is zero: fix all but one coordinate, use that a nonzero one-variable polynomial has finitely many roots, and repeat in the other coordinates. Thus every coefficient of \(p\) is real. \(\square\)

Write \(\Gamma\) for the connected component containing \(e\) of
\[
                  \{x\in\mathbb R^n:p(x)\ne0\}.
 \tag{2}
\]
Components of this open set are open and polygonally connected. Indeed the points reachable from a chosen point by polygonal paths in the open set form an open subset; their complement in a connected component is also open, by small balls. Connectedness makes the reachable set the component. The component excludes zero because \(m>0\). Positive scaling preserves it: the path from \(x\) to \(a x\), \(a>0\), stays in the nonzero set by homogeneity.

For \(n=1\), \(p(x)=(x/e)^m\), and \(\Gamma=\{x:x/e>0\}\). Every nonzero direction is hyperbolic, and all the conclusions below follow directly. We may use tangential spheres in the remaining arguments with \(n\ge2\).

## 2. A derivative perturbation separates roots

**Lemma 2.1 (one variable).** If a nonzero real polynomial \(q\) has only real roots, then \(q+cq'\) has only real roots for every real \(c\). Its degree and leading coefficient are unchanged. If \(c\ne0\), a root of multiplicity \(a\) in \(q\) has multiplicity \(a-1\) in \(q+cq'\), and every newly created root is simple. Consequently, for a degree-\(m\) polynomial,
\[
                         (1+c\partial_t)^m q
 \tag{3}
\]
has only simple real roots whenever \(c\ne0\).

**Proof.** The case \(c=0\) is immediate. For \(c\ne0\), let \(r_1<\cdots<r_k\) be the distinct roots, of multiplicities \(a_1,\ldots,a_k\). Away from them,
\[
        \frac{q'}q(t)=\sum_{i=1}^k\frac{a_i}{t-r_i},\qquad
        \left(\frac{q'}q\right)'(t)
                    =-\sum_{i=1}^k\frac{a_i}{(t-r_i)^2}<0.
 \tag{4}
\]
A new root is exactly a solution of \(q'/q=-1/c\). On each interval \((r_i,r_{i+1})\), the left side decreases from positive infinity to negative infinity, giving one simple root. If \(c>0\), there is also one root to the left of \(r_1\), where the range is \((-\infty,0)\); if \(c<0\), there is one to the right of \(r_k\), where the range is \((0,\infty)\). The other exterior interval gives none. All new roots are simple by the strict derivative in (4).

At an old root, write \(q=(t-r_i)^{a_i}h\), \(h(r_i)\ne0\). Then
\[
 q+cq'=(t-r_i)^{a_i-1}
       \big((t-r_i)h+c a_i h+c(t-r_i)h'\big),
 \tag{5}
\]
whose bracket is nonzero at \(r_i\). These old multiplicities sum to \(m-k\); there are \(k\) new simple roots. We have accounted for all \(m\) roots. At every iteration the largest multiplicity decreases by one until it is one, and simple roots remain simple. This proves (3). A nonzero constant remains constant and has no roots. \(\square\)

Choose real linear forms \(\ell_1,\ldots,\ell_{n-1}\) spanning the annihilator of \(e\). For real \(s\ne0\), define
\[
 p_s(x)=\prod_{j=1}^{n-1}
               (1+s\ell_j(x)\partial_e)^m p(x),
 \qquad \partial_e=\sum_i e_i\partial_{x_i}.
 \tag{6}
\]
The factors commute because \(\partial_e\ell_j=0\). Each factor preserves homogeneity of degree \(m\), and \(p_s\to p\) in coefficients as \(s\to0\). Expanding the factors shows \(p_s(e)=p(e)=1\).

**Proposition 2.2 (strict perturbations).** Every \(p_s\) is hyperbolic in \(e\). If \(x\) is not parallel to \(e\), the polynomial \(p_s(x+te)\) has \(m\) distinct real roots.

**Proof.** Along the line \(x+te\), each \(\ell_j\) is the constant \(\ell_j(x)\), and \(\partial_e\) is \(\partial_t\). Thus each factor in (6) is precisely the operation (3). Lemma 2.1 preserves real roots. If \(x\notin\mathbb R e\), at least one \(\ell_j(x)\) is nonzero, so its \(m\) operations make every root simple. The other factors preserve simplicity or act as the identity. The leading coefficient remains one. \(\square\)

This is Nuij's strict-root perturbation, expressed through tangential linear forms. No perturbation of a solution of a differential equation is involved.

## 3. Strictness makes the set of directions open

The next elementary fact prevents tangency at a smooth zero.

**Lemma 3.1 (a multiple root has zero gradient).** Suppose a real homogeneous polynomial \(h\) is hyperbolic in \(v\). If \(h(z)=0\) and \(t=0\) is a root of multiplicity \(k\ge2\) of \(h(z+tv)\), then \(\nabla h(z)=0\).

**Proof.** The leading term of that one-variable polynomial is \(a t^k\), \(a\ne0\). If the gradient is nonzero, choose a real \(w\) with \(b=\partial_w h(z)\ne0\). For \(\delta=\sigma r\), \(\sigma\in\{1,-1\}\), \(r>0\), the finite Taylor formula gives, uniformly for complex \(u\) in compact sets,
\[
 r^{-1}h(z+\sigma r w+r^{1/k}u v)
                         \longrightarrow a u^k+\sigma b.
 \tag{7}
\]
To check this limit, pure \(v\)-terms of degree below \(k\) vanish by the line multiplicity; the degree-\(k\) term is \(a u^k\). The linear \(w\)-term is \(\sigma b\). Every remaining Taylor monomial \(r^i r^{j/k}\), with \(i\ge1\), has exponent strictly larger than one unless \((i,j)=(1,0)\).

For \(k=2\), choose the sign so that \(\sigma b/a>0\). For \(k>2\), either sign gives at least one nonreal root of \(a u^k+\sigma b\): a real equation \(u^k=c\ne0\) has at most two real roots. All roots of this polynomial are simple. Put a small circle around a nonreal root, disjoint from the real axis and other roots. Rouché's theorem from [C] and (7) gives a nonreal root inside the circle for small \(r\). It yields a nonreal \(t=r^{1/k}u\) on the real affine \(v\)-line based at \(z+\sigma r w\), contradicting hyperbolicity. \(\square\)

**Lemma 3.2 (strict directions are open).** Let \(h\) be real and homogeneous of degree \(m\). If it is hyperbolic in \(v\), with distinct line roots whenever the base point is not parallel to \(v\), then all sufficiently nearby directions have the same strict property.

**Proof.** Consider unit base points \(w\in v^\perp\). This is a compact sphere. At a fixed such point, choose disjoint real intervals around the \(m\) simple roots of \(h(w+tv)\), with nonzero opposite signs at the endpoints of each interval. The endpoint signs persist when both \(w\) and the direction are changed slightly. Also the leading coefficient stays nonzero. Hence there is one real root in each of the \(m\) disjoint intervals, by the intermediate value theorem. Degree \(m\) accounts for all roots and makes them distinct.

Finitely many neighborhoods cover the sphere. Intersect their direction neighborhoods to obtain a single neighborhood of \(v\) valid for every unit \(w\in v^\perp\). Shrink it so that \(v\cdot v'\ne0\) and \(h(v')\ne0\) there. Any real base point \(x\) decomposes uniquely as \(x=w+a v'\), with \(w\in v^\perp\). If \(w\ne0\), homogeneity reduces its line polynomial to one with unit base point; translation by \(a\) merely translates roots. If \(w=0\), the base point is parallel to the direction and the line polynomial is \(h(v')(t+a)^m\). Thus every direction in the chosen neighborhood is hyperbolic and strict off its own line. \(\square\)

**Proposition 3.3 (all directions in a strict component).** Suppose \(h\) is homogeneous and strictly hyperbolic in \(e\). Every direction in the component of \(e\) in \(\{h\ne0\}\) is hyperbolic.

**Proof.** At every nonzero zero \(z\) of \(h\), strictness in \(e\) gives \(\partial_e h(z)\ne0\). Indeed \(z\) cannot be parallel to \(e\), and zero is then a simple root on its \(e\)-line. In particular the gradient is nonzero there.

Let \(H\) be the hyperbolic directions in the indicated component. It contains \(e\). It is relatively closed: if \(v_j\to v\) in the component, the leading coefficient \(h(v)\) is nonzero; for each fixed real \(x\), coefficient convergence and Rouché rule out a nonreal root of \(h(x+tv)\) as the polynomials with directions \(v_j\) have only real roots.

Every \(v\in H\) is strict. A multiple root on a line whose base point is not parallel to \(v\) would occur at a nonzero zero \(z\). Lemma 3.1 would give \(\nabla h(z)=0\), contrary to the preceding paragraph. Lemma 3.2 therefore makes \(H\) relatively open. A nonempty subset both open and closed in a connected component is the whole component. \(\square\)

## 4. Pass to multiple roots and obtain convexity

**Theorem 4.1 (the hyperbolic component).** Under (1), \(\Gamma\) is an open convex cone. Every \(v\in\Gamma\) is a hyperbolic direction. For every such \(v\) and every real \(x\),
\[
 x\in\Gamma\quad\Longleftrightarrow\quad
          \text{all roots of }t\mapsto F(x+tv)\text{ are strictly negative}.
 \tag{8}
\]
Moreover
\[
                         F(x+i y)\ne0
                  \qquad(x\in\mathbb R^n,\ y\in\Gamma).
 \tag{9}
\]

**Proof.** Fix \(v\in\Gamma\), and take a polygonal path from \(e\) to \(v\) in \(\Gamma\). Its image is compact, so \(|p|\) has a strictly positive minimum on it. Coefficient convergence \(p_s\to p\) is uniform on this compact set. For all sufficiently small nonzero \(s\), the entire same path lies in \(\{p_s\ne0\}\). Thus \(v\) belongs to the component of \(e\) for \(p_s\). Propositions 2.2 and 3.3 make it a hyperbolic direction for each such \(p_s\). For any fixed real \(x\), the polynomials \(p_s(x+tv)\) converge in coefficients to \(p(x+tv)\), whose leading coefficient \(p(v)\) is nonzero. Rouché again excludes every nonreal limiting root. Therefore \(v\) is hyperbolic for \(p\).

If \(x\in\Gamma\), join \(v\) to \(x\) by a path in the component. The roots on the \(v\)-line are all real, vary continuously with their multiplicities, and never pass through zero because \(p\) is nonzero on the path. They cannot escape to infinity on the compact path, since their leading coefficient is the fixed nonzero number \(p(v)\) and their other coefficients are bounded. At the starting point \(v\) all roots equal \(-1\). They remain strictly negative, proving one implication of (8).

Conversely suppose all these roots are negative. For \(0<a\le1\), homogeneity gives
\[
 p(a x+(1-a)v)=a^m p\big(x+((1-a)/a)v\big)\ne0.
 \tag{10}
\]
The parameter \((1-a)/a\) is nonnegative and hence is no root. At \(a=0\), the endpoint is \(v\), also nonzero. The segment connects \(v\) to \(x\) in the nonzero set, so \(x\in\Gamma\). This proves the other implication.

For two points \(x,v\in\Gamma\), the already proved first implication and (10) put their whole segment in \(\Gamma\). Hence the component is convex. Openness and positive scaling were proved after (2), and zero is excluded for positive degree.

Finally \(y\in\Gamma\) is a hyperbolic direction. For real \(x\), \(p(x+ty)\) has only real roots and leading coefficient \(p(y)\ne0\). The nonreal value \(t=i\) is not a root, proving (9). Multiplying by \(F(e)\) recovers every assertion for \(F\). \(\square\)

The strict perturbations need only preserve one compact path at a time. No uniform approximation assertion over an unbounded component was used. The tube in (9) is open; it excludes every zero, including when the polynomial has repeated irreducible factors. It gives no assertion at imaginary vectors on the boundary of the cone.

For a nonzero constant polynomial the roots are empty and the imaginary tube over the whole space is zero-free. Its nonzero set is the whole space and includes the origin. The positive-degree cone assertion above uses \(m>0\) explicitly.

## References

[C]: ../../AN02-L045.html

- **[C]** *Cauchy bounds, root counts and analytic extensions*, Section 2. Complete Rouché theorem and persistent root counts.
- **[N]** Wim Nuij, “A Note on Hyperbolic Polynomials,” *Mathematica Scandinavica* **23** (1968), 69–72. [Original journal record](https://journals.msp.org/mscand/article/view/2455), DOI 10.7146/math.scand.a-10898. Credit for the strict-root derivative perturbation; its root argument is proved here.
- **[L]** F. Reese Harvey and H. Blaine Lawson Jr., *Hyperbolic polynomials and the Dirichlet problem*, arXiv:0912.5220, version 2 (2010). [Author-deposited account](https://arxiv.org/abs/0912.5220). Freely readable background on Gårding's theory; no redistribution licence is inferred.
- **[G]** Lars Gårding, “An inequality for hyperbolic polynomials,” *Journal of Mathematics and Mechanics* **8** (1959), 957–965, DOI 10.1512/IUMJ.1959.8.58061. Historical credit for the hyperbolic component theorem; no paid proof is required by this chapter.
