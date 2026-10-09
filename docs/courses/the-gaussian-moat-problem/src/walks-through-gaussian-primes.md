# Walks through Gaussian primes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Gaussian primes are scattered over the plane, and their density near a point \(z\) decreases like \(1/\log|z|\). Can one walk to infinity on them with steps of bounded length? This course proves that one cannot, in the strong uniform form found by OpenAI in September 2026 [OpenAI-moat]: for every step bound \(D\), the graph joining Gaussian primes at distance at most \(D\) has connected components of bounded size, with one bound for all of them.

This lesson sets up the problem and reduces it to a statement about periodic sieves. It proves the facts about Gaussian integers that the course uses, the reduction from a finite sieve to a uniform bound on components, and the prime-counting estimates for the batches of primes used later. The finite sieve theorem itself is proved at the end of the course, in [Zero avoidance and the finite sieve](zero-avoidance-and-the-finite-sieve.md).

We assume ring theory at the level of Euclidean domains and unique factorization, as in the core course [Abstract Algebra II (C40)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40). Prime counting uses Chebyshev's bound from [Counting primes by elementary means: Chebyshev and Mertens](course:NT-ZETA/NT-ZETA-02) and the prime number theorem for the modulus four from [The prime number theorem for arithmetic progressions](course:NT-DIRL/NT-DIRL-09).

Basic references are [OpenAI-moat], [Gethner–Stark] and [Conrad].

## 1. The problem

A **Gaussian integer** is a complex number \(a+bi\) with \(a,b\in\mathbb Z\); these numbers form the ring \(\mathbb Z[i]\). We identify \(a+bi\) with the lattice point \((a,b)\in\mathbb Z^2\), and write

\[
N(a+bi)=a^2+b^2,\qquad |z|=\sqrt{N(z)}
\]

for the **norm** and the Euclidean length. Since \(|zw|=|z|\,|w|\), the norm is multiplicative. A **unit** is an invertible element, and a **Gaussian prime** is a nonzero nonunit that is not a product of two nonunits. Two elements are **associates** if one is a unit times the other.

For a real number \(D\), let \(G_D\) be the graph whose vertices are the Gaussian primes, with an edge between distinct primes \(z,w\) when \(|z-w|\le D\). A **\(D\)-walk** is a finite or infinite sequence \(z_0,z_1,\dots\) of *distinct* Gaussian integers with \(|z_{t+1}-z_t|\le D\) for every \(t\).

**Theorem 1.1** (uniform component bound). For every real number \(D\) there is a number \(B_D\) such that every connected component of \(G_D\) has at most \(B_D\) vertices. Consequently every \(D\)-walk through Gaussian primes has at most \(B_D\) terms, and no infinite \(D\)-walk runs through Gaussian primes.

The bound is the same for every component, wherever it lies in the plane. The proof gives no formula for \(B_D\): it fixes \(D\), and then chooses a sufficiently large scale.

The question goes back to Basil Gordon and Theodore Motzkin in the early 1960s; Erdős heard it from Motzkin in 1963 and passed it on, so that it was often attributed to him [Erdős 1977]. Gethner and Stark conjectured that one cannot walk to infinity from any starting point, and proved this for steps of length \(\sqrt2\) and \(2\) by constructing periodic moats [Gethner–Stark]. Vardi compared the Gaussian primes with a random model from percolation theory and predicted the critical step size near a point \(z\), which grows like \(\sqrt{\log|z|}\) [Vardi]. Large computations show, for example, that one cannot walk to infinity from the origin with steps of length at most \(6\) [Tsuchimura]. Theorem 1.1 was proved by OpenAI, together with a formal proof checked in the Lean proof assistant [OpenAI-moat]. This course follows the structure of that proof and gives complete arguments.

The simplest cases already show the role of congruences.

**Example 1.2** (short steps). If \(D<1\), then \(G_D\) has no edges, since distinct lattice points are at distance at least \(1\); so \(B_D=1\). Let \(1\le D<\sqrt2\). Then edges join Gaussian primes at distance exactly \(1\), and we claim that every component of \(G_D\) has at most three vertices.

For \(z=a+bi\) we have \(N(z)\equiv a+b\pmod2\), and a unit step changes \(a+b\) by \(\pm1\). So of two adjacent vertices, one has even norm. A Gaussian prime \(z\) of even norm is an associate of \(1+i\): the prime \(1+i\) divides \(2=-i(1+i)^2\), hence divides \(N(z)=z\bar z\), hence divides \(z\) or \(\bar z\); and \(1+i\) divides \(\bar z\) exactly when its conjugate \(1-i=-i(1+i)\) divides \(z\). So every edge has an endpoint among the four points \(\pm1\pm i\), which are pairwise at distance at least \(2\). The points at distance one from \(1+i\) are \(1\), \(i\), \(2+i\) and \(1+2i\); the first two are units and the last two have norm \(5\), so they are Gaussian primes (Lemma 2.2 below). All neighbours of \(2+i\) and of \(1+2i\) have even norm, and the only one of them that is an associate of \(1+i\) is \(1+i\) itself. So the component of \(1+i\) is \(\{1+i,2+i,1+2i\}\). Multiplication by a unit is a symmetry of \(G_D\), so the other three associates of \(1+i\) behave alike, and every other Gaussian prime is isolated.

In the language of Section 4, the residue class of \(0\) modulo the prime \(1+i\) is a periodic moat for unit steps: of two points at distance one, one lies in that class, and the class contains only four primes. Steps of length \(\sqrt2\) cross this moat: the points \((n+1)+ni\) all lie outside the class. A single split prime does not block even unit steps (Exercise 7.3). The proof of Theorem 1.1 therefore sieves by many primes at once.

## 2. Arithmetic of Gaussian integers

**Lemma 2.1** (division with remainder). For \(\alpha,\beta\in\mathbb Z[i]\) with \(\beta\ne0\) there are \(\gamma,\rho\in\mathbb Z[i]\) with \(\alpha=\gamma\beta+\rho\) and \(N(\rho)\le N(\beta)/2\).

**Proof.** Write \(\alpha/\beta=x+iy\) with \(x,y\in\mathbb Q\), and choose integers \(m,n\) with \(|x-m|\le\frac12\) and \(|y-n|\le\frac12\). Put \(\gamma=m+ni\) and \(\rho=\alpha-\gamma\beta=\beta(\alpha/\beta-\gamma)\). Then \(N(\rho)=N(\beta)\bigl((x-m)^2+(y-n)^2\bigr)\le N(\beta)/2\). \(\square\)

So \(\mathbb Z[i]\) is a Euclidean domain for the norm, and therefore a principal ideal domain with unique factorization into Gaussian primes. A Gaussian prime \(\pi\) is a prime element: if \(\pi\) divides a product, it divides a factor. The units are \(\pm1\) and \(\pm i\), because \(uv=1\) forces \(N(u)N(v)=1\), and the only Gaussian integers of norm \(1\) are \(\pm1,\pm i\). Complex conjugation is a ring automorphism of \(\mathbb Z[i]\), so it maps Gaussian primes to Gaussian primes.

**Lemma 2.2.** If \(N(\pi)\) is a rational prime, then \(\pi\) is a Gaussian prime.

**Proof.** If \(\pi=\gamma\delta\), then \(N(\gamma)N(\delta)\) is a rational prime, so one factor has norm \(1\) and is a unit. \(\square\)

**Proposition 2.3** (split primes). Let \(p\) be a rational prime with \(p\equiv1\pmod4\). There is a Gaussian prime \(\pi\) with \(\pi\bar\pi=p\). Its conjugate \(\bar\pi\) is a Gaussian prime that is not an associate of \(\pi\), both have norm \(p\), and every Gaussian prime dividing \(p\) is an associate of \(\pi\) or of \(\bar\pi\).

**Proof.** First, \(-1\) is a square modulo \(p\). By Wilson's theorem \((p-1)!\equiv-1\pmod p\): in the field \(\mathbf F_p\) each element other than \(\pm1\) is paired with its inverse, which is different from it. Pairing \(j\) with \(p-j\),

\[
(p-1)!\equiv\prod_{j=1}^{(p-1)/2}j\,(-j)=(-1)^{(p-1)/2}\Bigl(\bigl(\tfrac{p-1}2\bigr)!\Bigr)^2\pmod p,
\]

and \((p-1)/2\) is even. So \(a=((p-1)/2)!\) satisfies \(p\mid a^2+1=(a+i)(a-i)\). The quotients \((a\pm i)/p\) have imaginary part \(\pm1/p\), so \(p\) divides neither factor; hence \(p\) is not a prime element, and \(p=\alpha\beta\) with nonunits \(\alpha,\beta\). From \(N(\alpha)N(\beta)=p^2\) and \(N(\alpha),N(\beta)>1\) we get \(N(\alpha)=p\). Put \(\pi=\alpha\). Lemma 2.2 shows that \(\pi\) and \(\bar\pi\) are Gaussian primes, and \(\pi\bar\pi=N(\pi)=p\).

Write \(\pi=x+iy\), so \(x^2+y^2=p\). If \(\bar\pi=u\pi\) for a unit \(u\), then \(u=1\) gives \(y=0\), \(u=-1\) gives \(x=0\), and \(u=\pm i\) gives \(x=\mp y\); each case makes \(p\) a square or twice a square, which is impossible for an odd prime. Finally a Gaussian prime dividing \(p=\pi\bar\pi\) divides \(\pi\) or \(\bar\pi\), hence is an associate of it. \(\square\)

Over each such \(p\) we therefore have two **conjugate factors** \(\pi,\bar\pi\). They are determined up to units and up to exchanging them; nothing below depends on these choices.

**Proposition 2.4** (residues modulo a split prime). Let \(\pi\) be a Gaussian prime of norm \(p\), where \(p\equiv1\pmod4\) is a rational prime.

1. Every residue class modulo \(\pi\) contains a rational integer, and an integer \(a\in\mathbb Z\) is divisible by \(\pi\) if and only if \(p\mid a\). Hence \(\mathbb Z[i]/(\pi)\) is a field with \(p\) elements.
2. Every nonzero multiple of \(\pi\) has length at least \(\sqrt p\).
3. If \(\pi\mid v\) and \(\bar\pi\mid v\), then \(p\mid v\); that is, \(p\) divides both coordinates of \(v\).
4. If Gaussian primes \(\pi_1,\dots,\pi_r\) have pairwise distinct norms and each divides \(v\), then \(\pi_1\cdots\pi_r\) divides \(v\).

**Proof.** (1) Write \(\pi=x+iy\). If \(p\mid y\), then \(p\mid x^2=p-y^2\), so \(p\mid x\) and \(p^2\mid x^2+y^2=p\), which is absurd. Choose \(y'\in\mathbb Z\) with \(yy'\equiv1\pmod p\). Since \(p=\pi\bar\pi\equiv0\pmod\pi\), also \(yy'\equiv1\pmod\pi\). From \(x+iy\equiv0\) we get \(i\equiv iyy'\equiv-xy'\pmod\pi\), so \(a+bi\equiv a-bxy'\pmod\pi\), a rational integer. If \(\pi\mid a\) with \(a\in\mathbb Z\), conjugation gives \(\bar\pi\mid a\); since \(\pi\) and \(\bar\pi\) are nonassociate primes, unique factorization gives \(p=\pi\bar\pi\mid a\) in \(\mathbb Z[i]\), and \(a/p\in\mathbb Z[i]\cap\mathbb Q=\mathbb Z\). Conversely \(p\mid a\) gives \(\pi\mid a\). Thus \(\mathbb Z\to\mathbb Z[i]/(\pi)\) is onto with kernel \(p\mathbb Z\).

(2) If \(v=\pi w\) with \(w\ne0\), then \(N(v)=pN(w)\ge p\).

(3) and (4) follow from unique factorization: primes of different norms are not associates, and \(\pi,\bar\pi\) are not associates by Proposition 2.3. In (3), \(v/p\in\mathbb Z[i]\) means that \(p\) divides both coordinates. \(\square\)

We also need a determinant identity. For \(v=v_1+iv_2\) and \(w=w_1+iw_2\) write \(\det(v,w)=v_1w_2-v_2w_1\), the signed area of the parallelogram spanned by \(v\) and \(w\).

**Lemma 2.5** (determinant divisibility). For \(\alpha\in\mathbb Z[i]\) and \(v,w\in\mathbb Z[i]\) we have \(\det(\alpha v,\alpha w)=N(\alpha)\det(v,w)\). In particular, if \(\alpha\) divides \(v\) and \(w\), then \(\det(v,w)\) is an integer multiple of \(N(\alpha)\).

**Proof.** Multiplication by \(\alpha=x+iy\) is the real linear map of \(\mathbb R^2\) with matrix \(\begin{pmatrix}x&-y\\y&x\end{pmatrix}\), whose determinant is \(x^2+y^2=N(\alpha)\). Determinants of pairs of vectors are multiplied by the determinant of a linear map applied to both. \(\square\)

## 3. Graphs with bounded steps

Put

\[
K_D=\#\{v\in\mathbb Z[i]:|v|\le D\}.
\]

This count includes \(v=0\). In \(G_D\), and in every graph on a subset of \(\mathbb Z[i]\) whose edges join distinct points at distance at most \(D\), each vertex has at most \(K_D-1\) neighbours. Multiplication by a unit and complex conjugation preserve distances and map Gaussian primes to Gaussian primes, so they are automorphisms of \(G_D\).

**Lemma 3.1** (König). Let \(\Gamma\) be a graph in which every vertex has finitely many neighbours. If \(\Gamma\) has an infinite connected component, then \(\Gamma\) contains an infinite path with distinct vertices.

**Proof.** Fix a vertex \(v_0\) of the infinite component. A ball of finite radius around \(v_0\) contains finitely many vertices, by induction on the radius, so there are vertices at every distance from \(v_0\). A shortest path from \(v_0\) to a vertex at distance \(n\) has \(n\) steps and distinct vertices. Call a path from \(v_0\) with distinct vertices *extendable* if it is an initial segment of such paths of every length. The path consisting of \(v_0\) alone is extendable. If a path \(v_0,\dots,v_m\) is extendable, then every longer path beginning with it continues through one of the finitely many neighbours of \(v_m\); if none of the one-step continuations were extendable, each would have extensions only up to some length, and taking the largest of these finitely many lengths would contradict extendability. So some continuation \(v_0,\dots,v_m,v_{m+1}\) is extendable. Induction produces an infinite path with distinct vertices. \(\square\)

## 4. Periodic sieves

Let \(\mathcal P\) be a finite set of rational primes congruent to \(1\) modulo \(4\), and choose for each \(p\in\mathcal P\) a Gaussian prime \(\pi_p\) of norm \(p\) (Proposition 2.3). Put

\[
\mathcal A(\mathcal P)=\{z\in\mathbb Z[i]:\ \pi_p\nmid z\text{ and }\bar\pi_p\nmid z\text{ for every }p\in\mathcal P\},
\qquad Q=\prod_{p\in\mathcal P}p.
\]

Replacing \(\pi_p\) by an associate, or by \(\bar\pi_p\), does not change this set. The set is **periodic**: if \(v\in Q\,\mathbb Z[i]\), then \(z\in\mathcal A(\mathcal P)\) if and only if \(z+v\in\mathcal A(\mathcal P)\), because \(\pi_p\) and \(\bar\pi_p\) divide \(p\), which divides \(Q\). Exercise 7.4 shows that exactly \(\prod_{p\in\mathcal P}(p-1)^2\) of the \(Q^2\) residues modulo \(Q\) lie in \(\mathcal A(\mathcal P)\).

**Theorem 4.1** (from a periodic obstruction to a uniform bound). Let \(D\ge1\), and let \(\mathcal P\) be a finite set of rational primes congruent to \(1\) modulo \(4\) such that \(\mathcal A(\mathcal P)\) contains no infinite \(D\)-walk. Let \(E\) be the set of associates of the factors \(\pi_p,\bar\pi_p\) for \(p\in\mathcal P\); it has \(8|\mathcal P|\) elements. Then a component of \(G_D\) that contains no element of \(E\) has at most \(Q^2\) vertices, and every component of \(G_D\) has at most

\[
|E|+(K_D-1)\,|E|\,Q^2
\]

vertices.

**Proof.** Let \(\Gamma\) be the graph with vertex set \(\mathcal A(\mathcal P)\) and an edge between distinct points at distance at most \(D\). Every vertex of \(\Gamma\) has finitely many neighbours, and translation by any \(v\in Q\,\mathbb Z[i]\) is an automorphism of \(\Gamma\), by periodicity. An infinite component of \(\Gamma\) would contain an infinite path with distinct vertices (Lemma 3.1), that is, an infinite \(D\)-walk in \(\mathcal A(\mathcal P)\). So every component of \(\Gamma\) is finite.

Let \(C\) be a component of \(\Gamma\), and suppose that two distinct points \(x,y\in C\) differ by some \(v\in Q\,\mathbb Z[i]\). Translation by \(v\) maps \(C\) onto a component containing \(x+v=y\), hence onto \(C\) itself. But a finite nonempty set \(C\subset\mathbb Z^2\) is never mapped onto itself by a nonzero translation \(v\): a point of \(C\) at which the scalar product with \(v\) is largest is moved to a point where that scalar product is larger still. So distinct points of \(C\) have distinct residues modulo \(Q\), and \(\#C\le Q^2\).

A Gaussian prime \(z\) outside \(\mathcal A(\mathcal P)\) is divisible by some \(\pi_p\) or \(\bar\pi_p\), and is then an associate of it, because \(z\) is prime; so \(z\in E\). Hence the Gaussian primes outside \(E\) lie in \(\mathcal A(\mathcal P)\), and the graph \(G_D\) with the vertices of \(E\) removed is a subgraph of \(\Gamma\). Each of its components is a connected subgraph of \(\Gamma\), hence lies in one component of \(\Gamma\) and has at most \(Q^2\) vertices. This proves the first assertion.

Now let \(C\) be a component of \(G_D\) meeting \(E\). Let \(K\) be a component of the graph induced on \(C\setminus E\). Since \(C\) is connected and \(K\ne C\), some edge of \(C\) joins a vertex of \(K\) to a vertex outside \(K\); that vertex cannot lie in \(C\setminus E\), by maximality of \(K\), so it lies in \(E\). Thus every such \(K\) is joined by an edge to \(E\). The vertices of \(E\) have at most \((K_D-1)|E|\) edges in total, so there are at most that many components \(K\), each with at most \(Q^2\) vertices. Adding the at most \(|E|\) vertices of \(C\cap E\) gives the bound. \(\square\)

Periodicity is what makes the bound uniform. In a general graph with finitely many neighbours at each vertex, the absence of an infinite path says nothing about the sizes of the finite components.

The main work of the course is the following theorem.

**Theorem 4.2** (finite sieve obstruction). For every \(D\ge1\) there is a finite set \(\mathcal P_D\) of rational primes congruent to \(1\) modulo \(4\) such that \(\mathcal A(\mathcal P_D)\) contains no infinite \(D\)-walk.

It is proved in [Zero avoidance and the finite sieve](zero-avoidance-and-the-finite-sieve.md), as Theorem 4.1 of that lesson.

**Proof of Theorem 1.1, assuming Theorem 4.2.** For \(D<1\) take \(B_D=1\) (Example 1.2). For \(D\ge1\), apply Theorem 4.1 to the set \(\mathcal P_D\) of Theorem 4.2. A \(D\)-walk through Gaussian primes lies in one component of \(G_D\), so it has at most \(B_D\) terms. \(\square\)

## 5. Batches of split primes

The proof of Theorem 4.2 uses the split primes in dyadic intervals. For a real number \(T>1\) put

\[
\mathcal B_T=\{p\text{ prime}:\ T\le p\le2T,\ p\equiv1\pmod4\},\qquad
k_T=\#\mathcal B_T,\qquad
L^*_T=\frac1{k_T}\sum_{p\in\mathcal B_T}\log p,
\]

the last when \(k_T>0\). We call \(\mathcal B_T\) the **batch** at \(T\). Logarithms are natural throughout the course.

**Proposition 5.1** (size of a batch). As \(T\to\infty\),

\[
k_T=\Bigl(\frac12+o(1)\Bigr)\frac{T}{\log T},
\qquad \log T\le L^*_T\le\log(2T).
\]

Moreover \(k_T\log(2T)\le(8\log2)\,T\) for every \(T\ge2\).

**Proof.** Write \(\theta(x;4,1)\) for the sum of \(\log p\) over primes \(p\le x\) with \(p\equiv1\pmod4\). For the fixed modulus \(4\), Theorem 3.1 of [The prime number theorem for arithmetic progressions](course:NT-DIRL/NT-DIRL-09#3-passing-from-prime-powers-to-primes) gives \(\theta(x;4,1)=x/2+o(x)\): its exceptional term, if present at all, is \(x^{\beta_1}/(2\beta_1)\) with one fixed real number \(\beta_1<1\). The sum of \(\log p\) over \(\mathcal B_T\) is \(\theta(2T;4,1)-\theta(T;4,1)\), plus \(\log T\) if \(T\) itself belongs to \(\mathcal B_T\); hence it equals \(T/2+o(T)\). Every term lies between \(\log T\) and \(\log(2T)\), which gives the bounds for \(L^*_T\), and the sum lies between \(k_T\log T\) and \(k_T\log(2T)\). Since \(\log(2T)/\log T\to1\), the asymptotic formula for \(k_T\) follows.

For the last assertion, Chebyshev's bound \(\theta(x)<(2\log2)\,x\) for the sum of \(\log p\) over all primes \(p\le x\) (Theorem 2.1 of [Counting primes by elementary means: Chebyshev and Mertens](course:NT-ZETA/NT-ZETA-02#2-a-binomial-coefficient-measures-primes)) gives \(k_T\log T\le\theta(2T)<(4\log2)\,T\). For \(T\ge2\) we have \(\log(2T)\le2\log T\). \(\square\)

**Lemma 5.2** (geometric sums of batches). Let \(B>2\), and let \(T\) be an integer power of \(B\). Then

\[
\sum_{\substack{T'\in B^{\mathbb Z}\\ 2\le T'<T}}k_{T'}\log(2T')\le\frac{(8\log2)\,T}{B-1}.
\]

Moreover, the batches \(\mathcal B_{T'}\) for distinct powers \(T'\) of \(B\) are disjoint.

**Proof.** By Proposition 5.1 the sum is at most \((8\log2)\sum_{j\ge1}TB^{-j}=(8\log2)\,T/(B-1)\). If \(T'<T''\) are powers of \(B\), then \(T''\ge BT'>2T'\), so the intervals \([T',2T']\) and \([T'',2T'']\) are disjoint. \(\square\)

## 6. The plan of the proof

Fix \(D\ge1\). To prove Theorem 4.2, we suppose that an infinite \(D\)-walk \(z_0,z_1,\dots\) avoids the zero classes of all primes in a large finite union of batches, and derive a contradiction. The walk is a fixed deterministic sequence; randomness enters only through the times at which we look at it and through auxiliary choices of prime factors.

1. **Geometry** ([Differences of a walk and separating products](differences-of-a-walk-and-separating-products.md)). A stretch of \(n\) steps of the walk has many distinct differences \(z_s-z_t\): at least a constant times the area of a rectangle around the stretch. Reduction modulo a product of randomly chosen conjugate factors usually separates all these differences.
2. **Entropy enrichment** ([Entropy enrichment](entropy-enrichment.md)). Choose a uniformly random difference in a long stretch, and then one of its two endpoints. The residues of this endpoint modulo many selected factors are more uniformly spread than those of the starting point. Iterating over decreasing scales makes the joint distribution of residues almost uniform, in the sense of entropy.
3. **Coverage** ([Coverage from shared continuations](coverage-from-shared-continuations.md) and [A common sampling schedule](a-common-sampling-schedule.md)). Almost maximal joint entropy does not say that each single residue receives a fair share of probability. A transfer argument with one shared vector of repeated continuations proves such *coverage* at a sequence of checkpoints, by backward induction.
4. **Information** ([Zero avoidance and the finite sieve](zero-avoidance-and-the-finite-sieve.md)). Since the walk never meets the zero class of a selected factor \(\pi\), a short word of increments after the sampled time excludes every starting residue that would lead into that class. Coverage makes these exclusions informative: a batch of primes near \(T\) forces about \(1/\log T\) units of information per increment.
5. **Budget.** An increment has at most \(K_D\) values, so the words carry at most \(\log K_D\) units of information per increment, and the nested batches share this budget. The batch costs \(\sum_T c/\log T\) diverge as the number of scales grows. This contradiction proves Theorem 4.2.

The tools are Shannon entropy ([Entropy of finite random variables](entropy-of-finite-random-variables.md)) and a few concentration inequalities and facts about the discrete cube ([Concentration and the discrete cube](concentration-and-the-discrete-cube.md)).

## 7. Exercises

**Exercise 7.1 (easy).** Show that \(2+i\) is a Gaussian prime, that \(i\equiv-2\pmod{2+i}\), and that \(2+i\) divides \(a+bi\) exactly when \(a\equiv2b\pmod5\). Which congruence describes divisibility by \(2-i\)?

**Exercise 7.2 (easy).** Let \(\pi\) be a Gaussian prime of norm \(p\equiv1\pmod4\). Show that the \(p\) integers \(0,1,\dots,p-1\) represent the residue classes modulo \(\pi\), each exactly once.

**Exercise 7.3 (medium).** Show that \(\mathcal A(\{5\})\) contains an infinite \(1\)-walk. *Hint:* determine which points of the columns \(a=0\) and \(a=1\) lie in \(\mathcal A(\{5\})\).

**Exercise 7.4 (medium).** Let \(\mathcal P\) and \(Q\) be as in Section 4. Show that exactly \(\prod_{p\in\mathcal P}(p-1)^2\) residue classes modulo \(Q\) lie in \(\mathcal A(\mathcal P)\).

**Exercise 7.5 (medium).** Give a connected graph with infinitely many vertices but no infinite path with distinct vertices. Which hypothesis of Lemma 3.1 fails?

**Exercise 7.6 (medium).** Let \(1\le D<\sqrt2\) and \(\mathcal A'=\{z\in\mathbb Z[i]:(1+i)\nmid z\}\). Show that no two points of \(\mathcal A'\) are at distance at most \(D\). Then adapt the proof of Theorem 4.1, with the prime \(1+i\) in place of the split primes, to show that every component of \(G_D\) has at most \(20\) vertices, without using Example 1.2.

## 8. Solutions

**7.1.** \(N(2+i)=5\) is prime, so Lemma 2.2 applies. Since \(i+2=2+i\), we have \(i\equiv-2\). Hence \(a+bi\equiv a-2b\pmod{2+i}\), and by Proposition 2.4(1) the integer \(a-2b\) is divisible by \(2+i\) exactly when \(5\mid a-2b\). For \(2-i\) we have \(i\equiv2\), so \(2-i\) divides \(a+bi\) exactly when \(a\equiv-2b\pmod5\).

**7.2.** By Proposition 2.4(1) every class contains an integer \(a\), and integers \(a,a'\) lie in the same class exactly when \(\pi\mid a-a'\), that is, when \(p\mid a-a'\). Each integer is congruent modulo \(p\) to exactly one of \(0,\dots,p-1\).

**7.3.** By Exercise 7.1, \(a+bi\in\mathcal A(\{5\})\) exactly when \(a\not\equiv2b\) and \(a\not\equiv-2b\pmod5\). In the column \(a=0\) this excludes only \(b\equiv0\). In the column \(a=1\) it excludes \(2b\equiv1\) and \(2b\equiv-1\), that is, \(b\equiv3\) and \(b\equiv2\). The walk that runs, for \(k=0,1,2,\dots\), through

\[
5k+1,\ 5k+2,\ 5k+3,\ 5k+4\ \text{in the column }0,\qquad
5k+4,\ 5k+5,\ 5k+6\ \text{in the column }1,
\]

listing the second coordinates, and then returns to the column \(0\) at height \(5(k+1)+1\), uses unit steps, never repeats a point, and avoids every excluded point.

**7.4.** The reduction maps \(\mathbb Z[i]/Q\mathbb Z[i]\to\prod_{p}\mathbb Z[i]/p\mathbb Z[i]\) and \(\mathbb Z[i]/p\mathbb Z[i]\to\mathbb Z[i]/(\pi_p)\times\mathbb Z[i]/(\bar\pi_p)\) are injective: the first by the Chinese remainder theorem for the coordinates, and the second by Proposition 2.4(3). Counting elements (\(Q^2\), \(\prod p^2\) and \(p^2\) on the respective sides) shows that they are bijective. A residue lies in \(\mathcal A(\mathcal P)\) exactly when all its \(2|\mathcal P|\) components are nonzero, and each field \(\mathbb Z[i]/(\pi)\) has \(p-1\) nonzero elements.

**7.5.** Join one central vertex to the first vertex of a path of length \(n\), for every \(n\ge1\), using disjoint paths. The graph is connected and infinite; an infinite path with distinct vertices would have to stay in one of the finite paths after leaving the centre, which is impossible. The central vertex has infinitely many neighbours, so the hypothesis of Lemma 3.1 fails.

**7.6.** The prime \(1+i\) has norm \(2\), and \(z\equiv0\pmod{1+i}\) exactly when \(N(z)\) is even, that is, when the coordinate sum is even. Distinct lattice points at distance at most \(D<\sqrt2\) are at distance exactly one, and a step of length one changes the parity of the coordinate sum; so no two points of \(\mathcal A'\) are at distance at most \(D\), and the graph \(\Gamma\) of the proof of Theorem 4.1 has no edges. Its components are single points. The Gaussian primes outside \(\mathcal A'\) are the four associates of \(1+i\), each with at most \(K_D-1=4\) neighbours. Following the last paragraph of the proof of Theorem 4.1 with \(E=\{\pm1\pm i\}\), a component of \(G_D\) meeting \(E\) has at most \(4+4\cdot4\cdot1=20\) vertices, and the other components are single points. Example 1.2 sharpens \(20\) to \(3\).

## References

- [OpenAI-moat] OpenAI, Bounded-step walks on Gaussian primes, preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf
- [Gethner–Stark] E. Gethner, H. M. Stark, Periodic Gaussian moats, Experimental Mathematics 6 (1997), 289–292. https://projecteuclid.org/euclid.em/1047047189
- [Conrad] K. Conrad, The Gaussian integers, expository notes. https://kconrad.math.uconn.edu/blurbs/ugradnumthy/Zinotes.pdf
- [Erdős 1977] P. Erdős, Problems and results on combinatorial number theory III, in Number Theory Day (New York, 1976), Lecture Notes in Mathematics 626, Springer, 1977, 43–72. https://users.renyi.hu/~p_erdos/1977-27.pdf
- [Vardi] I. Vardi, Prime percolation, Experimental Mathematics 7 (1998), 275–289. https://projecteuclid.org/euclid.em/1047674208
- [Tsuchimura] N. Tsuchimura, Computational results for Gaussian moat problem, Mathematical Engineering Technical Reports METR 2004-13, University of Tokyo, 2004. https://www.keisu.t.u-tokyo.ac.jp/data/2004/METR04-13.pdf
