# Support distances and admissible convolution domains

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Uniform confinement of transpose-test supports has a geometric formulation: convolution preserves their distance from the relevant domain complements. We prove the equivalence for compact distributions, including the passage from smooth tests. It then identifies the maximal equation domain for a convex solution domain and shows that an admissible equation domain must be a union of entire components of the domain where convolution is defined.

Basic references are [Grubb's Fourier-distribution notes](https://web.math.ku.dk/~grubb/dist5.pdf), [Melrose's tempered-distribution notes](https://math.mit.edu/~rbm/iml/Chapter1.pdf), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. The exact ordinary-support identity used below is Theorem 3.1 of Convex supports and convolution cancellation, for two nonzero compact distributions. Its proof covers complex cancellation and lower-dimensional supports. The support-confinement condition required by smooth solvability is proved in Theorem 5.1 of Smooth forcing, invertible kernels and support confinement. Cutoffs, mollifiers and finite-dimensional compactness have their proofs in Metric and topological foundations. Every distance and domain argument needed here is supplied below.

## 1. Confinement and distance from the complement

For sets \(A,B\subset\mathbb R^n\), set
\[
 d(A,B)=\inf\{|a-b|:a\in A,\ b\in B\},\qquad
 \inf\varnothing=+\infty .
 \tag{1.1}
\]
Let \(n\ge1\), \(0\ne\mu\in\mathcal E'(\mathbb R^n)\), \(S=\operatorname{supp}\mu\), and let \(X_1,X_2\) be nonempty open sets with
\[
 X_2-S\subset X_1.
 \tag{1.2}
\]
Subtraction between support sets always means the Minkowski difference
\(A-B=\{a-b:a\in A,\ b\in B\}\), not removal of points from a set.
The reflected kernel is \(\check\mu(\phi)=\mu(\phi(-\,\cdot))\). For compact \(v\) supported in \(X_2\), put
\[
 T=\operatorname{supp}v,\qquad
 W=\operatorname{supp}(\check\mu*v).
 \tag{1.3}
\]
Then \(W\subset T-S\subset X_1\). Both are compact. If \(v\ne0\), then \(W\ne\varnothing\): the exact ordinary-support theorem gives
\[
 \operatorname{conv}W
       =\operatorname{conv}T-\operatorname{conv}S.
 \tag{1.4}
\]
The zero distribution is treated separately by the empty-support convention.

**Theorem 1.1 (support-distance criterion).** Under these hypotheses the following conditions are equivalent.

1. For every compact \(K_1\subset X_1\), there is a compact \(K_2\subset X_2\) such that
   \[
   v\in C_c^\infty(X_2),\
       \operatorname{supp}(\check\mu*v)\subset K_1
       \ \Longrightarrow\ \operatorname{supp}v\subset K_2.
   \tag{1.5}
   \]
2. For every compact distribution \(v\) supported in \(X_2\),
   \[
   d(T,\mathbb R^n\setminus X_2)
       =d(W,\mathbb R^n\setminus X_1).
   \tag{1.6}
   \]
3. Identity (1.6) holds for every \(v\in C_c^\infty(X_2)\).

These conditions also give (1.5) with compact distributions in place of smooth tests. The kernel is not required to be invertible, and the domains need not be convex. The zero-kernel case is classified in Section 5.

## 2. Distances under translation and regularization

**Lemma 2.1 (the forward inequality).** For every compact \(v\) as above,
\[
 d(W,\mathbb R^n\setminus X_1)
          \ge d(T,\mathbb R^n\setminus X_2).
 \tag{2.1}
\]

*Proof.* For \(v=0\), both sides are infinite. Otherwise let
\(r<d(T,\mathbb R^n\setminus X_2)\), \(r\ge0\). Then
\(T+\overline B_r\subset X_2\), and compatibility gives
\[
 W+\overline B_r
       \subset T-S+\overline B_r\subset X_1.
 \tag{2.2}
\]
Thus the distance on the left of (2.1) is at least \(r\). Let \(r\) increase to the right side, including arbitrarily large \(r\) if that side is infinite. \(\square\)

**Lemma 2.2 (distance of mollified supports).** Let \(a\ne0\) be a compact distribution with support \(A\subset X\), where \(X\) is open. Let \(\rho\) be a nonnegative smooth mollifier supported in the closed unit ball, with integral one, and set \(a_\varepsilon=a*\rho_\varepsilon\). Then, for sufficiently small positive \(\varepsilon\),
\[
 \operatorname{supp}a_\varepsilon\subset A+\overline B_\varepsilon\subset X,
 \qquad
 d(\operatorname{supp}a_\varepsilon,\mathbb R^n\setminus X)
                \longrightarrow d(A,\mathbb R^n\setminus X).
 \tag{2.3}
\]
No equality between the full support and its outer parallel set is assumed.

*Proof.* Support inclusion follows from compact convolution. The positive gap of the compact \(A\) inside \(X\) gives the second inclusion for small \(\varepsilon\). If the complement is empty, all the distances are infinite, and the assertion follows directly.

Otherwise write \(d=d(A,\mathbb R^n\setminus X)<\infty\). The complement is closed, and a nearest pair \(x\in A\), \(y\notin X\) attains \(d\). To see attainment, choose a minimizing sequence. Compactness gives a convergent subsequence of its points in \(A\); bounded distances make the other points bounded, and their subsequence limit stays in the closed complement.

The outer support inclusion gives the lower bound \(d-\varepsilon\) for the mollified distance. For the upper bound, fix \(r>0\). Since \(x\in\operatorname{supp}a\), some compact smooth test supported in \(B_r(x)\) has nonzero pairing with \(a\). Mollifier convergence in distributions makes its pairing with \(a_\varepsilon\) nonzero for every sufficiently small \(\varepsilon\). Consequently the mollified support meets \(B_r(x)\), so its distance from the complement is at most \(d+r\). First let \(\varepsilon\downarrow0\), then \(r\downarrow0\). This proves convergence. The ordinary-support theorem also ensures that each \(a_\varepsilon\) is nonzero, since both compact factors are nonzero. \(\square\)

## 3. Proof of the support-distance criterion

*Proof of Theorem 1.1.* We first show \(1\Rightarrow3\). Take nonzero smooth compact \(v\), and let
\[
 t=d(T,\mathbb R^n\setminus X_2),\qquad
 w=d(W,\mathbb R^n\setminus X_1).
 \tag{3.1}
\]
Lemma 2.1 gives \(w\ge t\). If \(t=\infty\), this already proves equality. Otherwise \(t>0\), and suppose \(w>t\), allowing \(w=\infty\).

Choose a nearest pair \(x_0\in T\), \(y_0\notin X_2\), so \(|y_0-x_0|=t\), and let \(e=(y_0-x_0)/t\). For \(0\le s<t\), translate \(v\) by \(se\). Its support \(T+se\) stays in \(X_2\), since the translation length is less than \(t\). Its convolution support is exactly \(W+se\), by translation invariance. All these image supports lie in the one compact set
\[
 K_1=W+[0,t]e\subset X_1.
 \tag{3.2}
\]
The inclusion follows from \(t<w\); every displacement has length at most \(t\), less than the distance of \(W\) from the complement.

Condition 1 gives one compact \(K_2\subset X_2\) containing every \(T+se\), \(s<t\). It therefore contains the limit \(x_0+te=y_0\), by closedness. This contradicts \(y_0\notin X_2\). Thus \(w=t\), proving condition 3. Zero \(v\) gives the equality of infinite distances.

Next prove \(3\Rightarrow2\). For a nonzero compact distribution \(v\) supported in \(X_2\), use \(v_\varepsilon=v*\rho_\varepsilon\), whose support lies in \(X_2\) for small \(\varepsilon\). These are smooth compact tests. Their image is
\[
 \check\mu*v_\varepsilon=(\check\mu*v)*\rho_\varepsilon.
 \tag{3.3}
\]
Both \(v\) and \(\check\mu*v\) are nonzero compact distributions. Apply Lemma 2.2 to each side's support and take the limit in condition 3. This gives (1.6), including an empty domain complement. Again the zero input is immediate.

Finally assume condition 2. Fix a nonempty compact \(K_1\subset X_1\), choose \(s_0\in S\), and set
\[
 Q=\operatorname{conv}K_1+s_0,\qquad
 \delta=\min\{1,d(K_1,\mathbb R^n\setminus X_1)\}>0.
 \tag{3.4}
\]
The hull \(Q\) is compact: affine dependence reduces convex combinations to at most \(n+1\) points, so the hull is a compact image of a finite support product and a coefficient simplex.

For any nonzero compact distribution \(v\) whose image support \(W\) lies in \(K_1\), (1.4) gives
\[
 T-s_0\subset\operatorname{conv}W\subset\operatorname{conv}K_1,
 \quad T\subset Q,\qquad
 d(T,\mathbb R^n\setminus X_2)\ge\delta.
 \tag{3.5}
\]
The last inequality is condition 2 and \(W\subset K_1\). Define
\[
 K_2=\{x\in Q:d(\{x\},\mathbb R^n\setminus X_2)\ge\delta\}.
 \tag{3.6}
\]
If the complement is empty, use \(K_2=Q\). Otherwise distance to that closed set is continuous, so \(K_2\) is closed in the compact \(Q\). Its positive distance condition puts it inside \(X_2\). Formula (3.5) gives \(T\subset K_2\). For zero \(v\), containment is automatic. If \(K_1\) is empty, no nonzero \(v\) can have zero convolution, by (1.4); take empty \(K_2\). We have proved confinement even for compact distributions, hence condition 1. This completes all implications. \(\square\)

The ordinary-support hull in (1.4) has two distinct uses: it excludes a zero convolution of nonzero factors, and it supplies a bounded set \(Q\). The distance equality supplies the positive boundary margin. Neither property alone gives compact confinement on an unbounded domain.

## 4. Maximal equation domains and connected components

**Definition 4.1.** A compatible pair of nonempty open sets is called \(\mu\)-convex for supports when it satisfies the equivalent conditions of Theorem 1.1.

For an open solution domain \(X_1\), its maximal equation domain is
\[
 Y=\{x:x-S\subset X_1\}.
 \tag{4.1}
\]
The compact translated support \(x-S\) has a positive margin inside \(X_1\), which persists near \(x\); thus \(Y\) is open. Compatibility is exactly \(X_2\subset Y\). If \(X_1\) is convex, so is \(Y=\bigcap_{s\in S}(X_1+s)\).

**Theorem 4.2 (the convex maximal domain).** Suppose \(X_1\) is open and convex and \(Y\ne\varnothing\). Then \((X_1,Y)\) is \(\mu\)-convex for supports.

*Proof.* For nonempty compact \(K_1\subset X_1\), its compact hull \(C=\operatorname{conv}K_1\) lies in \(X_1\). Every finite convex combination lies there by convexity, and compactness gives a positive margin. Choose \(s_0\in S\) and put
\[
 K_2=\{x\in C+s_0:x-\operatorname{conv}S\subset C\}.
 \tag{4.2}
\]
This is a closed subset of the compact \(C+s_0\), since it is the intersection of closed conditions \(x-s\in C\), \(s\in\operatorname{conv}S\). Each of its points satisfies \(x-S\subset C\subset X_1\), so \(K_2\subset Y\).

For nonzero \(v\) supported in \(Y\) with \(W\subset K_1\), (1.4) gives
\(T-\operatorname{conv}S\subset\operatorname{conv}W\subset C\).
In particular \(T\subset C+s_0\), so \(T\subset K_2\). Zero inputs and empty \(K_1\) are handled as in Section 3. Theorem 1.1 proves the claim. If \(Y\) is empty, there is no nonempty equation domain in this definition; the confinement statement for tests in the empty set is vacuous. \(\square\)

**Proposition 4.3 (whole components are required).** If a compatible pair \((X_1,X_2)\) is \(\mu\)-convex for supports, then \(X_2\) is a union of connected components of \(Y\) in (4.1).

*Proof.* It is relatively open in \(Y\). To prove relative closedness, let \(x_j\in X_2\) tend to \(x\in Y\). The compact \(x-S\) has positive distance \(\delta\) from the complement of \(X_1\); if that complement is empty, choose any positive \(\delta\). For sufficiently large \(j\),
\[
 d(x_j-S,\mathbb R^n\setminus X_1)\ge\delta/2 .
 \tag{4.3}
\]
Apply the distance equality to the compact distribution \(\delta_{x_j}\). Its image is the translate of \(\check\mu\), with support \(x_j-S\), so
\[
 d(\{x_j\},\mathbb R^n\setminus X_2)\ge\delta/2.
 \tag{4.4}
\]
If \(x\notin X_2\), the left side is at most \(|x_j-x|\), tending to zero. This is a contradiction. Thus \(x\in X_2\), proving relative closedness.

The intersection of \(X_2\) with each connected component of \(Y\) is both relatively open and relatively closed in that component. Connectedness forces it to be empty or the entire component. This proves the assertion; no path selection is required. \(\square\)

**Corollary 4.4 (uniqueness in the convex case).** If \(X_1\) is convex and \(X_2\) is nonempty and makes a \(\mu\)-convex pair, then \(X_2=Y\).

*Proof.* The nonempty convex \(Y\) is connected: the line segment between any two points lies in it and provides a continuous path. Proposition 4.3 makes the nonempty \(X_2\) a union of its components, hence all of \(Y\). Theorem 4.2 supplies that maximal pair. \(\square\)

## 5. The degenerate zero kernel

The nonzero kernel in Theorem 1.1 matters. With \(\mu=0\), every transpose image has empty support. Confinement (1.5) is false on every nonempty open \(X_2\subset\mathbb R^n\), \(n\ge1\): for \(K_1=\varnothing\), it would require one compact \(K_2\subset X_2\) containing every smooth test support. A bump at each point makes \(X_2\subset K_2\), hence \(X_2=K_2\) compact. A nonempty open subset of \(\mathbb R^n\) cannot be compact: if also closed, connectedness of \(\mathbb R^n\) would make it the whole space, which is unbounded.

Under the explicit distance convention (1.1), the image distance is always infinite. The distance identity for every compact input then holds exactly when \(X_2=\mathbb R^n\). If the domain is proper, a point mass has finite distance from its nonempty complement, so the identity fails. If it is the whole space, both distances are infinite. Thus distance equality without a nonzero-kernel hypothesis is not equivalent to confinement on the full equation space. The zero kernel never satisfies the original solvability hypothesis for every nonzero forcing.

## References

- Gerd Grubb, *Distributions and Operators*, Chapter 5, “Fourier transformation of distributions,” freely readable [lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard B. Melrose, *Introduction to Microlocal Analysis*, MIT, 2007, Chapter 1, “Tempered distributions and the Fourier transform,” freely readable [notes](https://math.mit.edu/~rbm/iml/Chapter1.pdf).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
- The exact ordinary convolution-support theorem is linked in the introduction with its own attribution and terms. The translation, regularization, compact-margin and component arguments are proved here.
