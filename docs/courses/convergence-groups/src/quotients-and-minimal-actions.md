# Quotients and minimal actions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson contains three tools for working with a convergence group \(\Gamma\) on a compact metric space \(M\), as defined in [Convergence actions and their elements](convergence-actions-and-their-elements.md).

- If \(M\) is mapped onto another compact metric space by a continuous map that respects the actions, the action on the image is again a convergence action, with the images of the repelling and attracting points (Proposition 1.1). For an element of infinite order, the fixed points in the image are the images of its fixed points (Corollary 1.2).
- An action is *minimal* if there is no closed invariant set other than the empty set and the whole space. Minimality passes to images, and a minimal action on a space with more than one point has no fixed point (Lemma 2.1).
- If \(M\) is connected, it has a dendrite quotient, constructed from its cut points in [The dendrite quotient of a continuum](course:pretrees/the-dendrite-quotient-of-a-continuum). The group acts on every step of that construction, and its action on the dendrite quotient is a convergence action (Theorem 4.1).

The first item is Lemma 6.5 of [Bowditch]; the third is the remark there that the construction of the quotient is natural. The lesson uses the first lesson of this course and, in Sections 3 and 4, the course [Pretrees](course:pretrees/betweenness-and-pretrees).

## 1. Quotients of convergence actions

Let \(\Gamma\) act by homeomorphisms on compact metric spaces \(M\) and \(N\). A map \(f\colon M\to N\) is *equivariant* if \(f(gx)=gf(x)\) for all \(g\in\Gamma\) and \(x\in M\).

In the definition of a convergence action, a sequence of pairwise distinct elements of \(\Gamma\) is required to have a collapsing subsequence. The elements are distinct in \(\Gamma\); they need not act differently. So the action on a space with one point is a convergence action, and an action on \(N\) can be a convergence action although some elements act trivially.

**Proposition 1.1.** Let \(f\colon M\to N\) be a continuous surjective equivariant map. If a sequence \((g_i)\) in \(\Gamma\) collapses on \(M\) with the pair \((a,b)\), it collapses on \(N\) with the pair \((f(a),f(b))\). Consequently, if the action on \(M\) is a convergence action, so is the action on \(N\).

**Proof.** Let \(K\subseteq N\setminus\{f(a)\}\) be closed and \(U\subseteq N\) open with \(f(b)\in U\). Then \(f^{-1}(K)\) is a closed subset of \(M\setminus\{a\}\), and \(f^{-1}(U)\) is an open set containing \(b\). So for all but finitely many \(i\),
\[
g_if^{-1}(K)\subseteq f^{-1}(U).
\]
Since \(f\) is surjective and equivariant, \(g_iK=f(g_if^{-1}(K))\subseteq U\) for these \(i\). \(\blacksquare\)

**Corollary 1.2.** Let \(f\colon M\to N\) be as in Proposition 1.1, let the action on \(M\) be a convergence action, and let \(M\) and \(N\) have at least three points. Let \(\gamma\in\Gamma\) have infinite order. Then the set of fixed points of \(\gamma\) in \(N\) is the image of the set of fixed points of \(\gamma\) in \(M\).

So a parabolic element has exactly one fixed point in \(N\), and a loxodromic element has one or two.

**Proof.** Choose pairwise distinct integers \(n_i\) such that \((\gamma^{n_i})\) collapses on \(M\), with a pair \((a,b)\). By Theorem 2.1 of the first lesson the set of fixed points of \(\gamma\) in \(M\) is \(\{a,b\}\). By Proposition 1.1 the action on \(N\) is a convergence action and the sequence collapses on \(N\) with \((f(a),f(b))\). The same theorem, applied to the action on \(N\), shows that the set of fixed points of \(\gamma\) in \(N\) is \(\{f(a),f(b)\}\). \(\blacksquare\)

## 2. Minimal actions

**Definition.** An action of \(\Gamma\) on a space \(M\) by homeomorphisms is *minimal* if the only closed subsets \(F\subseteq M\) with \(gF=F\) for all \(g\in\Gamma\) are the empty set and \(M\).

**Lemma 2.1.**

1. The action on \(M\) is minimal if and only if every orbit is dense in \(M\).
2. If the action on \(M\) is minimal and \(M\) has more than one point, no point of \(M\) is fixed by all of \(\Gamma\).
3. Let \(f\colon M\to N\) be a continuous surjective equivariant map. If the action on \(M\) is minimal, so is the action on \(N\).

**Proof.** (1) The closure of an orbit is a closed invariant set, and it is not empty; so if the action is minimal, it is \(M\). Conversely a nonempty closed invariant set contains an orbit, hence its closure.

(2) Points are closed, so a point fixed by all of \(\Gamma\) would be a closed invariant set that is neither empty nor \(M\).

(3) If \(F\subseteq N\) is closed and invariant, so is \(f^{-1}(F)\). So \(f^{-1}(F)\) is empty or \(M\), and \(F\) is empty or \(N\), because \(f\) is surjective. \(\blacksquare\)

## 3. Homeomorphisms and the pretree of cut points

Let \(M\) be a connected Hausdorff space. In [Cut points of a connected space](course:pretrees/cut-points-of-a-connected-space) it is made a pretree: \(xzy\) means that there are disjoint nonempty open sets \(U,V\) with \(U\cup V=M\setminus\{z\}\), \(x\in U\) and \(y\in V\). A homeomorphism \(g\) of \(M\) maps such a pair \(U,V\) for \(z\) to such a pair for \(gz\). So \(xzy\) holds if and only if \(gx\,gz\,gy\) holds, and \(g\) maps cut points to cut points: *a homeomorphism of \(M\) is an automorphism of the pretree \(M\).*

An *automorphism* of a pretree \(T\) is a bijection \(\alpha\colon T\to T\) such that \(xyz\) holds if and only if \(\alpha x\,\alpha y\,\alpha z\) holds. We recall from the course on pretrees: a *flow* \(p\) of \(T\) is a binary relation \(uv.p\) on \(T\) with three properties; the flows form the set \(P\); \(\bar a\) is the flow towards a point \(a\); and on \(P\) there is a betweenness \(\langle prq\rangle\) that makes it the pretree \(\Phi(T)\), the completion of \(T\).

For an automorphism \(\alpha\) of \(T\) and a flow \(p\) define the relation \(\alpha_*p\) by
\[
\begin{gathered}
uv.(\alpha_*p)\quad\Longleftrightarrow\\
(\alpha^{-1}u)(\alpha^{-1}v).p .
\end{gathered}
\]

**Lemma 3.1.** Let \(\alpha,\beta\) be automorphisms of a pretree \(T\).

1. \(\alpha_*p\) is a flow, \((\alpha\beta)_*=\alpha_*\beta_*\), and \(\alpha_*\bar a=\overline{\alpha a}\) for \(a\in T\).
2. \(\alpha_*\) is an automorphism of the pretree \(\Phi(T)\), and it maps the set \(\bar T\) of flows towards points onto itself.

**Proof.** (1) The three properties of a flow are stated through the relation of \(T\), which \(\alpha\) preserves; so they pass from \(p\) to \(\alpha_*p\). The rule for products follows from the definition. And \(uv.(\alpha_*\bar a)\) means \(\alpha^{-1}v\in(\alpha^{-1}u,a]\), that is, \(v\in(u,\alpha a]\).

(2) The betweenness of \(\Phi(T)\) is defined in two steps ([Flows on a pretree](course:pretrees/flows-on-a-pretree), Section 4, and [The completion of a pretree](course:pretrees/the-completion-of-a-pretree), Definition 2.1). First \(T\sqcup P\) is made a pretree: \(xyp\) means \(xy.p\), and \(pxq\), for \(p\ne q\), means that every \(y\ne x\) has \(yx.p\) or \(yx.q\). The map that is \(\alpha\) on \(T\) and \(\alpha_*\) on \(P\) preserves these relations in both directions, by the definition of \(\alpha_*\). Then \(\langle prq\rangle\) is defined for distinct flows by: \(r=\bar x\) and \(pxq\); or \(r\notin\bar T\) and no point of \(T\) lies both between \(p\) and \(r\) and between \(r\) and \(q\). By (1) and the first step these conditions are preserved in both directions. The inverse of \(\alpha_*\) is \((\alpha^{-1})_*\). \(\blacksquare\)

**Lemma 3.2.** Let \(\beta\) be an automorphism of a pretree \(S\) and \(\approx\) the least codense relation of \(S\) ([The dense quotient of a pretree](course:pretrees/the-dense-quotient-of-a-pretree)). Then \(p\approx q\) if and only if \(\beta p\approx\beta q\), and \(\beta\) induces an automorphism of the pretree \(S/{\approx}\).

**Proof.** By Theorem 3.3 of that lesson, \(p\approx q\) fails exactly when the interval \((p,q)\) contains a rational subset: a countable linear subset with a direction that is a dense order without ends. An automorphism maps intervals to intervals and rational subsets to rational subsets. So \(\beta\) maps classes to classes. A class \(Y\) lies between classes \(X\) and \(Z\) if \(X\ne Z\) and some point of \(Y\) outside \(X\cup Z\) lies between a point of \(X\) and a point of \(Z\); this is preserved by \(\beta\) and by its inverse. \(\blacksquare\)

## 4. The action on the dendrite quotient

Let \(M\) be a compact connected metric space and \(T\) a set of cut points of \(M\). The lesson on the dendrite quotient constructs from these data: the completion \(\Phi=\Phi(T)\); the map \(\varphi\colon M\to\Phi\) that sends \(x\) to the flow of \(T\) towards \(x\); for a flow \(p\notin\bar T\) the closed connected set \(R_M(p)\subseteq M\); the dense quotient \(\Psi=\Phi/{\approx}\) with quotient map \(\pi\); the surjective map \(f=\pi\circ\varphi\colon M\to\Psi\); and the space \(D\), which is the set \(\Psi\) with the quotient topology of \(f\). Since \(M\) is a compact metric space, it has a countable dense subset, and \(D\) is a dendrite; in particular \(D\) is compact and metrizable.

**Theorem 4.1.** Let \(\Gamma\) act by homeomorphisms on a compact connected metric space \(M\), and let \(T\) be a set of cut points of \(M\) with \(gT=T\) for all \(g\in\Gamma\).

1. \(\Gamma\) acts on \(\Phi(T)\) by automorphisms of the pretree, through \(p\mapsto g_*p\), where \(g_*\) is formed with the automorphism of \(T\) given by \(g\). The map \(\varphi\) is equivariant, and \(R_M(g_*p)=gR_M(p)\) for every flow \(p\notin\bar T\).
2. \(\Gamma\) acts on \(D\) by homeomorphisms that are automorphisms of the pretree \(\Psi\), and \(f\colon M\to D\) is equivariant.
3. If the action on \(M\) is a convergence action, so is the action on \(D\). If the action on \(M\) is minimal, so is the action on \(D\).

**Proof.** (1) Each \(g\) restricts to an automorphism of the pretree \(T\), by the beginning of Section 3. Lemma 3.1 gives the action on \(\Phi(T)\). For \(x\in M\) and \(u,v\in T\), the relation \(uv.\varphi(gx)\) means \(v\in(u,gx]\), that is, \(g^{-1}v\in(g^{-1}u,x]\), that is, \(uv.(g_*\varphi(x))\). So \(\varphi(gx)=g_*\varphi(x)\).

The set \(R_M(p)\) is the intersection over \(a\in T\) of the sets \(R_M(a,b)\) of points \(x\) for which \(xab\) fails, where \(b\) is any point of \(T\setminus\{a\}\) for which \(ba.p\) fails ([Mapping a pretree to the completion of a subset](course:pretrees/mapping-a-pretree-to-the-completion-of-a-subset), Section 2). Now \(ba.p\) fails if and only if \((gb)(ga).(g_*p)\) fails, and \(xab\) fails if and only if \(gx\,ga\,gb\) fails. So \(gR_M(a,p)=R_M(ga,g_*p)\), and the intersection over all \(a\in T\) gives \(gR_M(p)=R_M(g_*p)\).

(2) By Lemma 3.2, applied to \(\beta=g_*\) on \(S=\Phi\), each \(g\) induces an automorphism \(\bar g\) of \(\Psi\) with \(\bar g\circ\pi=\pi\circ g_*\). With (1), \(\bar g\circ f=f\circ g\). These automorphisms form an action of \(\Gamma\). For \(O\subseteq D\) we have \(f^{-1}(\bar g^{-1}(O))=g^{-1}(f^{-1}(O))\), which is open exactly when \(f^{-1}(O)\) is open. So \(\bar g^{-1}(O)\) is open exactly when \(O\) is: \(\bar g\) is a homeomorphism of \(D\).

(3) \(D\) is a compact metrizable space, and \(f\) is continuous, surjective and equivariant. Apply Proposition 1.1 and Lemma 2.1(3). \(\blacksquare\)

The dendrite \(D\) may be a single point. Deciding when it is not is the subject of the next lessons.

## 5. Exercises

**5.1.** Show that the action of the integers on the circle \(\mathbb R\cup\{\infty\}\) by the powers of \(\tau(x)=x+1\) (Example 1.3 of the first lesson) is not minimal.

**5.2.** Let \(f\colon M\to N\) be as in Corollary 1.2 and \(\gamma\) loxodromic on \(M\) with fixed points \(a,b\). Describe the powers of \(\gamma\) on \(N\) when \(f(a)=f(b)\).

**5.3.** Let \(M=[0,1]\), \(T=(0,1)\) and \(g(x)=1-x\). For \(t\in T\) let \(t^-\) be the flow of the numbers below \(t\) directed upwards, and \(t^+\) the flow of the numbers above \(t\) directed downwards, so that \(uv.t^-\) holds if and only if \(u<v<t\) or \(t\le v<u\), and \(uv.t^+\) if and only if \(t<v<u\) or \(u<v\le t\). Show that \(g_*(t^-)=(1-t)^+\).

**5.4.** Let \(\Gamma\) act minimally on a compact metric space \(M\) with more than one point, and let \(F\subseteq M\) be a closed set with \(gF\subseteq F\) for all \(g\in\Gamma\). Show that \(F\) is empty or \(M\).

## 6. Solutions

**5.1.** The point \(\infty\) is fixed, so \(\{\infty\}\) is a closed invariant set that is neither empty nor the whole circle.

**5.2.** By Corollary 1.2, \(\gamma\) has exactly one fixed point \(c=f(a)=f(b)\) in \(N\). By Proposition 3.1 of the first lesson, \((\gamma^n)_{n\ge1}\) collapses on \(M\) with \((a,b)\) and \((\gamma^{-n})_{n\ge1}\) with \((b,a)\); by Proposition 1.1 both collapse on \(N\) with \((c,c)\). So on \(N\) the powers of \(\gamma\) behave like those of a parabolic element: every closed set that does not contain \(c\) is moved into any given neighbourhood of \(c\) by all powers with large exponent, positive or negative.

**5.3.** \(uv.g_*(t^-)\) means \((1-u)(1-v).t^-\), that is, \(1-u<1-v<t\) or \(t\le1-v<1-u\); that is, \(1-t<v<u\) or \(u<v\le1-t\). This is \(uv.(1-t)^+\).

**5.4.** For \(g\in\Gamma\) we have \(gF\subseteq F\) and \(g^{-1}F\subseteq F\), so \(F\subseteq gF\). Hence \(gF=F\) for all \(g\), and \(F\) is a closed invariant set.

## References

- [Bowditch] B. H. Bowditch, *Treelike structures arising from continua and convergence groups*, Memoirs of the American Mathematical Society 662 (1999), Section 6. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-treelike.pdf
