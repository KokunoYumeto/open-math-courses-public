# Finite covers of punctured polydiscs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Near a point of a divisor with simple normal crossings, the complement of the divisor looks like a product of punctured discs and discs. This lesson analyses the finite coverings of such a product and shows that every one of them extends, in a canonical way, to the whole polydisc as a finite cover whose sheaf of functions is locally free. The extension is defined by a growth condition: we keep the holomorphic functions on the cover that stay bounded near the divisor. The next lesson glues these local extensions over a smooth compactification and algebraizes the result.

The method is classical: after pulling back along the map that takes \(N\)-th roots of the coordinates, every finite covering becomes trivial, and the original covering is a quotient of a trivial one by a finite group. We use the Riemann extension theorem of [Holomorphic functions of several variables](course:complex-analytic-spaces-and-coherent-sheaves/holomorphic-functions-of-several-variables#4-the-riemann-extension-theorem) and elementary covering space theory from the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60): path lifting (Lecture 5), the action of loops on fibres (Lectures 6 and 7), the fibre of a connected covering as a coset space (Lectures 9 and 10), and the fundamental group of the circle (Lecture 10, Theorem 10.1).

## 1. Notation

Let \(\Delta=\{t\in\mathbf C:|t|<1\}\) and \(\Delta^*=\Delta\setminus\{0\}\). Fix integers \(0\le p\le n\) and put

\[
V=\Delta^n,\qquad V^*=\{z\in V:\ z_1\cdots z_p\ne0\}=(\Delta^*)^p\times\Delta^{n-p}.
\]

The space \(V^*\) is a connected complex manifold. For an integer \(N\ge1\) let

\[
\pi_N:V\to V,\qquad \pi_N(w)=(w_1^N,\ldots,w_p^N,w_{p+1},\ldots,w_n).
\]

It is a finite, proper, surjective holomorphic map, and \(\pi_N^{-1}(V^*)=V^*\). The finite group \(G=\mu_N^p\) of \(p\)-tuples of \(N\)-th roots of unity acts on \(V\) by \(\zeta\cdot w=(\zeta_1w_1,\ldots,\zeta_pw_p,w_{p+1},\ldots,w_n)\). It preserves the fibres of \(\pi_N\) and acts simply transitively on the fibres over points of \(V^*\). Over \(V^*\), \(\pi_N\) is a covering map of degree \(N^p\), and a local biholomorphism.

A finite covering \(q:E\to V^*\) carries a unique complex structure making \(q\) a local biholomorphism. Holomorphic functions on open subsets of \(E\) refer to it.

## 2. Monodromy

For a finite covering \(q:E\to M\) of a path-connected, locally path-connected space and a base point \(b\in M\), path lifting gives an action of \(\pi_1(M,b)\) on the fibre \(F=q^{-1}(b)\), the *monodromy action*.

**Lemma 2.1.** If the monodromy action is trivial, then \(E\cong M\times F\) over \(M\).

**Proof.** Since \(M\) is locally path-connected, so is \(E\), and the path components \(E_\alpha\) of \(E\) are open and closed. Over a path-connected evenly covered open set \(W\subset M\), each sheet of \(q^{-1}(W)\) is path-connected, so it lies in one \(E_\alpha\). Hence each restriction \(q|_{E_\alpha}\) is a covering map onto an open and closed subset of \(M\), hence onto \(M\). Two points of \(F\cap E_\alpha\) are joined by a path in \(E_\alpha\), whose image is a loop at \(b\) that carries one point to the other; so \(F\cap E_\alpha\) is a single orbit of the monodromy action, which is a single point. So \(q|_{E_\alpha}\) is a covering of degree one, a homeomorphism onto \(M\), and \(E=\coprod_\alpha E_\alpha\cong M\times F\). \(\square\)

**Lemma 2.2.**

1. For path-connected spaces \(X,Y\), the projections induce an isomorphism \(\pi_1(X\times Y,(x,y))\cong\pi_1(X,x)\times\pi_1(Y,y)\).
2. \(\pi_1(V^*,b)\cong\mathbf Z^p\), the \(i\)-th basis element being the class of a loop that winds once around zero in the \(i\)-th coordinate and is constant in the others.
3. The covering \(\pi_N|_{V^*}:V^*\to V^*\) induces multiplication by \(N\) on \(\pi_1\cong\mathbf Z^p\).

**Proof.** (1) A loop in \(X\times Y\) is a pair of loops, and a homotopy of loops relative to the end points is a pair of such homotopies; so the map is bijective, and it is a homomorphism because concatenation is computed componentwise. (2) The disc \(\Delta\) is contractible, and \(\Delta^*\) deformation retracts onto the circle \(|t|=1/2\) by \(t\mapsto\bigl((1-s)+s/(2|t|)\bigr)t\). Since \(\pi_1\) is a functor on the homotopy category of pointed spaces, \(\pi_1(\Delta^*)\cong\pi_1(S^1)\cong\mathbf Z\), by Theorem 10.1 of the core course. Use (1). (3) By (1) it suffices to treat \(p=1\) and the map \(t\mapsto t^N\) on \(\Delta^*\). The loop \(\gamma(s)=\tfrac12e^{2\pi is}\) represents a generator, and \(\gamma^N(s)=2^{-N}e^{2\pi iNs}\). Under the covering \(\mathbf R\to\{|t|=2^{-N}\}\), \(u\mapsto2^{-N}e^{2\pi iu}\), its lift starting at \(0\) ends at \(N\); this identifies its class with \(N\) times a generator, as in the proof of Theorem 10.1. \(\square\)

**Proposition 2.3 (Kummer trivialization).** Let \(q:E\to V^*\) be a finite covering of degree \(d\), and \(N=d!\). Then the pull-back \(\pi_N^*E=V^*\times_{V^*}E\), formed with \(\pi_N\), is a trivial covering of \(V^*\).

**Proof.** The monodromy of \(\pi_N^*E\) at a point \(b'\) is the monodromy of \(E\) at \(\pi_N(b')\) composed with the map induced by \(\pi_N\) on fundamental groups, because the fibres agree and lifts of paths correspond. By Lemma 2.2 the monodromy of \(E\) is a homomorphism \(\rho:\mathbf Z^p\to\operatorname{Sym}(F)\), and that of \(\pi_N^*E\) is \(v\mapsto\rho(Nv)=\rho(v)^N\). Every element of the symmetric group on \(d\) letters has order dividing \(d!=N\), so this is trivial. Apply Lemma 2.1. \(\square\)

**Proposition 2.4 (covers as quotients).** In the situation of Proposition 2.3, choose a trivialization \(\tau:\pi_N^*E\cong V^*\times F\). There is a homomorphism \(c:G\to\operatorname{Sym}(F)\) such that the map \(V^*\times F\to E\) induced by \(\tau^{-1}\) and the projection identifies \(E\) with the quotient of \(V^*\times F\) by the action \(\zeta\cdot(w,\phi)=(\zeta\cdot w,c_\zeta(\phi))\). In particular, holomorphic functions on \(q^{-1}(U)\), for open \(U\subset V^*\), are the families \((f_\phi)_{\phi\in F}\) of holomorphic functions on \(\pi_N^{-1}(U)\) with \(f_{c_\zeta(\phi)}(\zeta\cdot w)=f_\phi(w)\).

**Proof.** The group \(G\) acts on \(\pi_N^*E=\{(w,e):\pi_N(w)=q(e)\}\) by \(\zeta\cdot(w,e)=(\zeta\cdot w,e)\), and the projection to \(E\) is a surjective local homeomorphism whose fibres are exactly the \(G\)-orbits, because \(G\) acts simply transitively on the fibres of \(\pi_N\) over \(V^*\). Transported by \(\tau\), the action has the form \(\zeta\cdot(w,\phi)=(\zeta\cdot w,c_\zeta(w)(\phi))\) with \(c_\zeta(w)\in\operatorname{Sym}(F)\) depending continuously on \(w\). As \(V^*\) is connected, \(c_\zeta\) is constant, and \(c_{\zeta\eta}=c_\zeta c_\eta\) because the formula defines an action. A function on an open subset of \(E\) is holomorphic exactly when its pull-back is, the projection being a surjective local biholomorphism, and pull-backs are the \(G\)-invariant functions. \(\square\)

## 3. The extension

**Definition 3.1.** Let \(q:E\to V^*\) be a finite covering. For an open set \(W\subset V\), let \(\mathcal A_E(W)\) be the set of holomorphic functions \(f\) on \(q^{-1}(W\cap V^*)\) that are *locally bounded on* \(W\): every point of \(W\) has a neighbourhood \(W'\subset W\) such that \(f\) is bounded on \(q^{-1}(W'\cap V^*)\).

This is a sheaf of \(\mathcal O_V\)-algebras on \(V\). Over \(V^*\) the boundedness condition is automatic, because \(q\) is proper, so \(\mathcal A_E|_{V^*}=q_*\mathcal O_E\), which is locally free of rank \(d\) when \(E\) has degree \(d\).

**Lemma 3.2.** The \(\mathcal O_V\)-module \(\pi_{N*}\mathcal O_V\) is free with basis \(w^a=w_1^{a_1}\cdots w_p^{a_p}\), \(a\in\{0,\ldots,N-1\}^p\), and the \(G\)-action on it is \(\mathcal O_V\)-linear. Moreover, every \(G\)-invariant holomorphic function on \(\pi_N^{-1}(W)\) is \(h\circ\pi_N\) for a unique holomorphic \(h\) on \(W\).

**Proof.** First the invariant functions. Let \(u\) be \(G\)-invariant and holomorphic on \(\pi_N^{-1}(W)\). On \(W\cap V^*\), where \(\pi_N\) is a covering with group \(G\), \(u=h\circ\pi_N\) for a holomorphic \(h\). Near a point of \(W\setminus V^*\), \(h\) is bounded, because \(\pi_N\) is proper and \(u\) is locally bounded. By the Riemann extension theorem ([Holomorphic functions of several variables, Theorem 4.2](course:complex-analytic-spaces-and-coherent-sheaves/holomorphic-functions-of-several-variables#4-the-riemann-extension-theorem), with the function \(z_1\cdots z_p\)), \(h\) extends holomorphically to \(W\), and \(u=h\circ\pi_N\) by continuity. Uniqueness holds because \(\pi_N\) is surjective.

Now let \(f\) be holomorphic on \(\pi_N^{-1}(W)\), a \(G\)-stable open set. For \(a\in\{0,\ldots,N-1\}^p\) let \(\chi_a(\zeta)=\zeta^a\) and

\[
f_a=\frac1{|G|}\sum_{\zeta\in G}\chi_a(\zeta)^{-1}\,f\circ\zeta .
\]

Then \(f_a\circ\zeta=\chi_a(\zeta)f_a\), and \(f=\sum_af_a\) by the orthogonality of the characters of \(G\). We claim \(f_a/w^a\) is holomorphic. Near a point where \(w_i=0\) for some \(i\le p\), expand \(f_a=\sum_{k\ge0}c_k\,w_i^k\) with \(c_k\) holomorphic in the other variables. Invariance under the \(i\)-th factor of \(G\) forces \(c_k=0\) unless \(k\equiv a_i\) modulo \(N\), hence unless \(k\ge a_i\); so \(w_i^{a_i}\) divides \(f_a\). Doing this for each \(i\) shows that \(f_a/w^a\) is holomorphic, and it is \(G\)-invariant. By the first part, \(f_a=w^a\,(h_a\circ\pi_N)\) with \(h_a\) holomorphic on \(W\). This proves that the \(w^a\) generate. If \(\sum_aw^a(h_a\circ\pi_N)=0\), applying the projection to the \(\chi_a\)-component gives \(w^a(h_a\circ\pi_N)=0\), so \(h_a=0\). The action of \(G\) commutes with multiplication by functions \(h\circ\pi_N\), since \(\pi_N\circ\zeta=\pi_N\). \(\square\)

**Theorem 3.3.** Let \(q:E\to V^*\) be a finite covering of degree \(d\). Then \(\mathcal A_E\) is a locally free \(\mathcal O_V\)-algebra of rank \(d\), with \(\mathcal A_E|_{V^*}=q_*\mathcal O_E\).

**Proof.** Let \(N=d!\) and choose \(\tau\) and \(c\) as in Proposition 2.4. The group \(G\) acts \(\mathcal O_V\)-linearly on the free \(\mathcal O_V\)-module \(\mathcal M=(\pi_{N*}\mathcal O_V)^F\) of rank \(N^pd\) by

\[
(\zeta\star f)_\phi=f_{c_\zeta(\phi)}\circ\zeta .
\]

We claim that \(\mathcal A_E\) is the sheaf \(\mathcal M^G\) of invariants. By Proposition 2.4, a holomorphic function on \(q^{-1}(W\cap V^*)\) is a \(G\)-invariant family \((f_\phi)\) of holomorphic functions on \(\pi_N^{-1}(W)\cap V^*\). It is locally bounded on \(W\) if and only if every \(f_\phi\) is locally bounded on \(\pi_N^{-1}(W)\): the projection \(\pi_N^*E\to E\) is surjective, and since \(\pi_N\) is proper, small neighbourhoods of a point of \(W\) have inverse images inside small neighbourhoods of its finitely many preimages. By the Riemann extension theorem, applied with the function \(w_1\cdots w_p\), the locally bounded \(f_\phi\) are exactly the restrictions of holomorphic functions on \(\pi_N^{-1}(W)\); the invariance relations extend by continuity, since \(\pi_N^{-1}(W)\cap V^*\) is dense. This proves the claim.

The averaging map \(e=|G|^{-1}\sum_\zeta\zeta\star(-)\) is an \(\mathcal O_V\)-linear idempotent endomorphism of \(\mathcal M\) with image \(\mathcal M^G\). So \(\mathcal A_E\) is a direct summand of a free module of finite rank. Its stalks are finitely generated projective modules over local rings, hence free, and \(\mathcal A_E\) is locally free. Its rank is locally constant; on \(V^*\) it equals the rank \(d\) of \(q_*\mathcal O_E\), and \(V\) is connected. Products of locally bounded functions are locally bounded, so \(\mathcal A_E\) is a subalgebra. \(\square\)

**Remark 3.4.** The sheaf \(\mathcal A_E\) is defined by a condition that does not refer to \(N\), \(\tau\) or the coordinates. If \(W\subset V\) is open and \(\psi\) is a biholomorphism of \(W\) onto an open subset of another such polydisc carrying \(W\cap V^*\) onto the complement of the coordinate hyperplanes, then \(\psi\) identifies the sheaves \(\mathcal A\) on both sides. This is what allows the local extensions to be glued in the next lesson.

## 4. Examples

**Example 4.1 (one punctured disc).** Let \(n=p=1\) and \(E=\Delta^*\to\Delta^*\), \(t\mapsto t^m\). Here \(d=m\), and \(\mathcal A_E\) is the sheaf of holomorphic functions of \(t\) that are bounded near \(t=0\), namely the holomorphic functions of \(t\) on the disc. As an \(\mathcal O_\Delta\)-module it is free with basis \(1,t,\ldots,t^{m-1}\), with \(z=t^m\). The extension of the cover is the map \(\Delta\to\Delta\), \(t\mapsto t^m\), branched at the origin.

**Example 4.2 (a disconnected cover).** Let \(E=\Delta^*\times\{1,2\}\) be the trivial double cover. Then \(\mathcal A_E=\mathcal O_\Delta^2\): a pair of bounded holomorphic functions on \(\Delta^*\) extends to the disc. The extension is the trivial double cover of \(\Delta\).

**Example 4.3 (two coordinates).** Let \(n=p=2\) and let \(E\) be the double cover of \((\Delta^*)^2\) defined by \(s^2=z_1z_2\). Then \(\mathcal A_E\) is free with basis \(1,s\), and its analytic spectrum is the cone \(s^2=z_1z_2\), which is singular at the origin. The extension is a finite cover whose sheaf of functions is locally free, but which is not smooth. Smoothness is not needed in this course, only local freeness.

## 5. Exercises

**Exercise 5.1.** In Example 4.3, compute the monodromy representation \(\rho:\mathbf Z^2\to\operatorname{Sym}(\{\pm\})\) and verify that it is trivial after pull-back along \(\pi_2\).

*Solution.* Going once around \(z_1=0\) multiplies \(z_1z_2\) by a loop of winding number one, so \(s\) changes sign; likewise around \(z_2=0\). So \(\rho(1,0)=\rho(0,1)\) is the transposition. After pull-back along \(\pi_2\), \(z_1z_2=(w_1w_2)^2\), and \(s=\pm w_1w_2\) are two global sections; the cover is trivial.

**Exercise 5.2.** Let \(n=p=1\). Write the function \(f(w)=e^w\) on \(\pi_N^{-1}(\Delta)=\Delta\) in the form \(\sum_{a=0}^{N-1}w^a\,(h_a\circ\pi_N)\) of Lemma 3.2, and find the functions \(h_a\).

*Solution.* Group the terms of \(e^w=\sum_{k\ge0}w^k/k!\) by the residue of \(k\) modulo \(N\). The \(\chi_a\)-component is \(f_a=\sum_{m\ge0}w^{a+mN}/(a+mN)!=w^a\sum_{m\ge0}(w^N)^m/(a+mN)!\), so \(h_a(z)=\sum_{m\ge0}z^m/(a+mN)!\), an entire function. For \(N=2\) this is \(e^w=\cosh w+\sinh w\), with \(h_0(z)=\cosh\sqrt z\) and \(h_1(z)=\sinh(\sqrt z)/\sqrt z\), both holomorphic in \(z\).

**Exercise 5.3.** Let \(E\to\Delta^*\) be the identity covering, and \(j:\Delta^*\to\Delta\) the inclusion. Show that \(\mathcal A_E=\mathcal O_\Delta\), and that the stalk at \(0\) of the sheaf \(j_*\mathcal O_{\Delta^*}\) of all holomorphic functions on punctured neighbourhoods is not a finitely generated \(\mathcal O_{\Delta,0}\)-module. This is why the growth condition is needed.

*Solution.* A holomorphic function on a punctured neighbourhood of \(0\) that is bounded near \(0\) extends holomorphically by the Riemann extension theorem, so \(\mathcal A_E=\mathcal O_\Delta\). The stalk \(M\) of \(j_*\mathcal O_{\Delta^*}\) at \(0\) contains the germs of \(z^{-k}\) for all \(k\). If \(M\) were finitely generated over the noetherian ring \(\mathcal O_{\Delta,0}\), it would be a noetherian module, and the increasing chain of submodules \(z^{-k}\mathcal O_{\Delta,0}\) would become stationary. But \(z^{-k-1}\notin z^{-k}\mathcal O_{\Delta,0}\), since \(z^{-1}\) is not holomorphic at \(0\).

## References

- [SGA 1] A. Grothendieck et al., *Revêtements étales et groupe fondamental (SGA 1)*, Exposé XII, proof of Theorem 5.1, part c), where finite covers of products of punctured discs are described as quotients of Kummer covers; free re-edition arXiv:math/0206203. This lesson describes the extension through the algebra of locally bounded functions, which avoids quotients of analytic spaces. <https://arxiv.org/abs/math/0206203>
