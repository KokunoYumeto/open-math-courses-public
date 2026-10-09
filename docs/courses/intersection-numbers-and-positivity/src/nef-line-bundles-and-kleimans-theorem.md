# Nef line bundles and Kleiman's theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A line bundle is *nef* (numerically effective) if its degree on every curve is nonnegative. Ample bundles are nef, but nef bundles can have degree zero on some curves; the bundle \(\mathcal O(1,0)\) on \(\mathbf P^1\times\mathbf P^1\) is an example. Kleiman's theorem says that nefness, a condition on curves only, controls the intersection numbers on subvarieties of every dimension: a nef bundle has \((L^{\dim V}\cdot V)\ge0\) for every subvariety \(V\). Combined with the Nakai–Moishezon criterion it gives the principle used most often in applications: a nef bundle plus an ample bundle is ample. Equivalently, the nef bundles are the limits of ample ones.

We use [Intersection numbers of line bundles](intersection-numbers-of-line-bundles.md) and [The Nakai–Moishezon criterion](the-nakai-moishezon-criterion.md). Throughout, \(k\) is an algebraically closed field and \(X\) is a projective \(k\)-scheme. In this lesson we write the group of invertible sheaves additively: \(L+M\) means \(L\otimes M\), \(mL\) means \(L^m\) for \(m\in\mathbb Z\). Intersection numbers are multilinear, so for integers \(a,b\),

\[
((aL+bM)^d\cdot V)=\sum_{i=0}^d\binom di a^ib^{d-i}(L^i\cdot M^{d-i}\cdot V).
\]

## 1. Nef line bundles

**Definition 1.1.** An invertible sheaf \(L\) on \(X\) is *nef* if \(\deg(L|_C)\ge0\) for every curve \(C\subseteq X\) (an integral closed subscheme of dimension one).

**Proposition 1.2.**

1. Ample sheaves are nef. Globally generated sheaves are nef.
2. Sums of nef sheaves are nef, and \(mL\) is nef for \(m\ge1\) if and only if \(L\) is.
3. If \(f:Y\to X\) is a morphism of projective \(k\)-schemes and \(L\) is nef on \(X\), then \(f^*L\) is nef on \(Y\). In particular restrictions to closed subschemes are nef.

**Proof.** (1) The first claim is Theorem 3.4 of the intersection-number lesson. If \(L\) is globally generated and \(C\) is a curve, some section does not vanish at the generic point of \(C\); its restriction is a nonzero section of \(L|_C\), and Corollary 2.5 there gives \(\deg(L|_C)\ge0\). (2) Degree on a curve is additive. (3) For a curve \(C\subseteq Y\), Proposition 3.1 of the intersection-number lesson gives \(\deg(f^*L|_C)=e\deg(L|_{f(C)})\ge0\) when \(f(C)\) is a curve, and \(0\) when \(f(C)\) is a point. \(\square\)

On \(\mathbf P^1\times\mathbf P^1\), the bundle \(\mathcal O(1,0)\) is globally generated, hence nef; its degree on the curves \(\{p\}\times\mathbf P^1\) is zero, so it is not ample. On the blow-up \(Y\) of \(\mathbf P^2\) at a point, the pullback \(H\) of \(\mathcal O(1)\) is nef with \((H^2)=1>0\), and \((H\cdot E)=0\) for the exceptional curve; so a nef bundle with positive top self-intersection need not be ample.

## 2. Kleiman's theorem

**Theorem 2.1** (Kleiman). Let \(L\) be nef and \(A\) ample on \(X\). For every integral closed subscheme \(V\subseteq X\) of dimension \(d\ge1\) and every \(0\le i\le d\),

\[
(L^i\cdot A^{d-i}\cdot V)\ge0 .
\]

In particular \((L^d\cdot V)\ge0\).

**Proof.** Induction on \(d\). For \(d=1\), \((L\cdot V)\ge0\) by nefness and \((A\cdot V)>0\). Let \(d\ge2\) and assume the theorem for all integral subschemes of dimension less than \(d\), for all nef \(L\) and ample \(A\). Replacing \(X\) by \(V\) and \(L,A\) by their restrictions, which are nef and ample, we may assume \(X=V\) is integral of dimension \(d\).

*Step 1: the terms with \(i<d\).* Let \(0\le i\le d-1\). Choose \(p\ge1\) with \(pA\) very ample. Applying Proposition 3.5 of the intersection-number lesson \(d-i\) times,

\[
p^{d-i}(L^i\cdot A^{d-i}\cdot X)=(L^i\cdot(pA)^{d-i}\cdot X)=\sum_jm_j\,(L^i\cdot W_j)
\]

with integers \(m_j\ge1\) and integral \(W_j\subseteq X\) of dimension \(i\). For \(i\ge1\), each \((L^i\cdot W_j)\ge0\) by the inductive hypothesis; for \(i=0\), each term is \(\chi(\mathcal O_{W_j})\ge1\) for a point \(W_j\). So \((L^i\cdot A^{d-i}\cdot X)\ge0\) for \(i<d\), and \((A^d\cdot X)>0\).

*Step 2: the polynomial \(P\).* Define

\[
P(t)=\sum_{i=0}^d\binom di t^{d-i}(L^i\cdot A^{d-i}\cdot X),\qquad t\in\mathbb R,
\]

so that \(q^dP(p/q)=((qL+pA)^d\cdot X)\) for integers \(p,q\ge1\). Its leading coefficient \((A^d\cdot X)\) is positive. We claim \(P(t)>0\) for all \(t>0\); then \((L^d\cdot X)=P(0)=\lim_{t\to0^+}P(t)\ge0\), which is the case \(i=d\).

*Step 3: ampleness above the last zero.* For a rational \(t=p/q>0\) with \(P(t)>0\), the bundle \(D=qL+pA\) is ample. Indeed, by the Nakai–Moishezon criterion it suffices to check \((D^{e}\cdot W)>0\) for integral \(W\subseteq X\) of dimension \(e\ge1\). For \(W=X\) this is \(q^dP(t)>0\). For \(W\ne X\), \(e<d\), and

\[
(D^e\cdot W)=\sum_{i=0}^e\binom ei q^ip^{e-i}(L^i\cdot A^{e-i}\cdot W)\ge p^e(A^e\cdot W)>0,
\]

since every term is nonnegative by the inductive hypothesis applied to \(W\).

*Step 4: \(P\) has no positive zero.* Suppose \(P(t)\le0\) for some \(t>0\). Since \(P(t)\to\infty\), the number \(s=\sup\{t>0:P(t)\le0\}\) is finite and positive, \(P(s)\le0\) by continuity, and \(P(t)>0\) for \(t>s\). Let \(t=p/q>s\) be rational. By Step 3, \(D=qL+pA\) is ample; choose \(r\ge1\) with \(rD\) very ample. By multilinearity

\[
q^{d}P(t)=(D^{d-1}\cdot qL\cdot X)+(D^{d-1}\cdot pA\cdot X).
\]

For the first term, Proposition 3.5 of the intersection-number lesson applied \(d-1\) times to the very ample \(rD\) gives \(r^{d-1}(D^{d-1}\cdot L\cdot X)=\sum_jm_j\deg(L|_{C_j})\ge0\), with curves \(C_j\) and \(m_j\ge1\), because \(L\) is nef. For the second term, expand \(D^{d-1}=(qL+pA)^{d-1}\):

\[
(D^{d-1}\cdot A\cdot X)=\sum_{i=0}^{d-1}\binom{d-1}iq^ip^{d-1-i}(L^i\cdot A^{d-i}\cdot X)\ge p^{d-1}(A^d\cdot X),
\]

by Step 1. Hence \(q^dP(t)\ge p^d(A^d\cdot X)\), that is, \(P(t)\ge t^d(A^d\cdot X)\) for every rational \(t>s\). Letting \(t\) decrease to \(s\), continuity gives \(P(s)\ge s^d(A^d\cdot X)>0\), a contradiction. \(\square\)

## 3. Consequences

**Corollary 3.1** (nef plus ample). If \(L\) is nef and \(A\) is ample, then \(L+A\) is ample. More generally \(aL+bA\) is ample for all integers \(a\ge0\), \(b\ge1\).

**Proof.** For integral \(V\) of dimension \(e\ge1\),

\[
((L+A)^e\cdot V)=\sum_{i=0}^e\binom ei(L^i\cdot A^{e-i}\cdot V)\ge(A^e\cdot V)>0
\]

by Theorem 2.1, and the Nakai–Moishezon criterion applies. The general case follows because \(aL\) is nef and \(bA\) is ample. \(\square\)

**Corollary 3.2** (nef as a limit of ample). Let \(A\) be ample. Then \(L\) is nef if and only if \(mL+A\) is ample for every \(m\ge1\).

**Proof.** If \(L\) is nef, \(mL\) is nef and Corollary 3.1 applies. Conversely, if \(mL+A\) is ample for all \(m\ge1\), then \(m\deg(L|_C)+\deg(A|_C)>0\) for every curve \(C\) and every \(m\), which forces \(\deg(L|_C)\ge0\). \(\square\)

The following form is the one used for blow-ups in the course on the irrationality exponent of \(\pi\).

**Corollary 3.3** (rational combinations). Let \(N\) be nef and \(M\) ample, and suppose that for some integers \(c\ge1\), \(a\ge1\), \(b\ge1\) one has \(cL=aN+bM\). Then \(L\) is ample.

**Proof.** By Corollary 3.1, \(cL\) is ample, and an invertible sheaf with an ample positive power is ample. \(\square\)

In words: if a rational positive multiple of \(L\) is a positive rational combination of a nef class and an ample class, then \(L\) is ample.

## 4. Exercises

**Exercise 4.1.** On \(\mathbf P^1\times\mathbf P^1\) determine the nef bundles among the \(\mathcal O(a,b)\), and check Corollary 3.2 for them.

**Exercise 4.2.** Let \(X\) be an integral projective surface, \(L\) nef and \(A\) ample. Write out the proof of Theorem 2.1 for \(d=2\) and show directly that \((L^2)\ge0\) and \((L\cdot A)\ge0\).

**Exercise 4.3.** Let \(f:Y\to X\) be a morphism of projective schemes and \(A\) ample on \(X\). Show that \(f^*A\) is nef; that it is not ample if \(f\) maps some curve to a point; and that it is ample if \(f\) is finite.

**Exercise 4.4.** On the blow-up \(Y\) of \(\mathbf P^2\) at a point, with \(H\) the pullback of \(\mathcal O(1)\) and \(E\) the exceptional curve, assume that \(H-E\) is globally generated (it is the pullback of \(\mathcal O(1)\) under the projection from the point to a line) and that \((H^2)=1\), \((H\cdot E)=0\), \((E^2)=-1\). Show with the Nakai–Moishezon criterion that \(2H-E\) is ample, and deduce from Corollary 3.1 that \(aH-E\) is ample for every \(a\ge2\).

**Exercise 4.5.** On the same blow-up, let \(L=\mathcal O_Y(E)\). Show that \(\deg(L|_C)\ge0\) for every curve \(C\ne E\), that \(\deg(L|_E)=-1\), and that \((L^2)<0\). So the hypothesis of Theorem 2.1 cannot be weakened by allowing one curve of negative degree.

## 5. Solutions

**4.1.** With the notation of Exercise 3.3 of the previous lesson, \((\mathcal O(a,b)\cdot C)=ac+bd\) with \(c,d\ge0\) for every curve, and the rulings realize \((c,d)=(1,0),(0,1)\). So \(\mathcal O(a,b)\) is nef if and only if \(a,b\ge0\). Then \(m\mathcal O(a,b)+\mathcal O(1,1)=\mathcal O(ma+1,mb+1)\) is ample for all \(m\ge1\) exactly when \(a,b\ge0\).

**4.2.** Step 1 gives \((L\cdot A)\ge0\): for very ample \(pA\), \((L\cdot pA)=\sum m_j\deg(L|_{C_j})\ge0\). With \(P(t)=(L^2)+2t(L\cdot A)+t^2(A^2)\), Steps 3 and 4 show \(P(t)>0\) for \(t>0\), so \((L^2)=P(0)\ge0\). Step 4 here reads: if \(D=qL+pA\) is ample, then \((D\cdot L)\ge0\) because \(L\) is nef and \(rD\) is very ample.

**4.3.** Nefness is Proposition 1.2(3). If \(f\) maps a curve \(C\) to a point, then \(\deg(f^*A|_C)=0\) by Proposition 3.1 of the intersection-number lesson, and \(f^*A\) is not ample. If \(f\) is finite, \(f^*A\) is ample by Lemma 1.2 of the previous lesson.

**4.4.** The integral subvarieties of positive dimension are \(Y\) and the curves. First, \(((2H-E)^2)=4(H^2)-4(H\cdot E)+(E^2)=3>0\). For a curve \(C\ne E\), the image of \(C\) in \(\mathbf P^2\) is a curve, so \((H\cdot C)>0\) by Proposition 3.1 of the intersection-number lesson, while \(((H-E)\cdot C)\ge0\) because \(H-E\) is globally generated; hence \(((2H-E)\cdot C)>0\). Finally \(((2H-E)\cdot E)=2\cdot0-(-1)=1>0\). So \(2H-E\) is ample. For \(a\ge2\), \(aH-E=(2H-E)+(a-2)H\) is ample plus nef, hence ample by Corollary 3.1.

**4.5.** For a curve \(C\ne E\), the canonical section of \(\mathcal O_Y(E)\) does not vanish identically on \(C\), so its restriction is a nonzero section of \(L|_C\) and \(\deg(L|_C)\ge0\) by Corollary 2.5 of the intersection-number lesson. On \(E\), \(\deg(L|_E)=(E^2)=-1\) by the given value, and \((L^2)=(E^2)=-1<0\).

## References

- [Vakil] R. Vakil, The Rising Sea: Foundations of Algebraic Geometry, public draft of 21 October 2025. https://math.stanford.edu/~vakil/216blog/
- [Stacks] The Stacks project authors, The Stacks project, chapter Varieties, section Numerical intersections. https://stacks.math.columbia.edu/tag/0BEL
