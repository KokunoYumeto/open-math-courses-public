# The relative bicentralizer

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(N\subset M\) be von Neumann algebras with a faithful normal conditional expectation \(E\colon M\to N\), and let \(\varphi\) be a faithful normal state on \(N\). The *relative bicentralizer* \(\mathrm B(N\subset M,\varphi)\) consists of the elements of \(M\) that asymptotically commute with every bounded sequence of \(N\) that asymptotically commutes with \(\varphi\). Masuda introduced it for subfactors of finite index, and Ando, Haagerup, Houdayer and Marrakchi studied it for arbitrary inclusions with expectation [AHHM]. For \(N=M\) it is Connes' bicentralizer \(\mathrm B(M,\varphi)\) of the course [Bicentralizers of type III₁ factors](course:bicentralizers-of-type-iii1-factors/the-bicentralizer#1-three-descriptions).

This lesson proves the basic structure: four equivalent descriptions, one inside the Ocneanu ultrapower (Proposition 2.2); that \(\mathrm B(N\subset M,\varphi)\) is a von Neumann subalgebra with a state-preserving conditional expectation \(E_{\mathrm B}\) (Theorem 2.3); that \(E_{\mathrm B}\) is a limit of averages of conjugations by unitaries of \(N\) that almost commute with \(\varphi\) (Theorem 3.4); and that every element of \(M\) orthogonal to \(\mathrm B(N\subset M,\varphi)\) is moved by some unitary of the asymptotic centralizer of \(N\) (Theorem 3.4(5)). When \(N\) is a factor of type III₁ with separable predual, the triviality of its own bicentralizer gives \(E(b)=\varphi(E(b))1\) for \(b\in\mathrm B(N\subset M,\varphi)\) and \(E_{\mathrm B}(x)=\varphi(x)1\) for \(x\in N\) (Corollary 2.6). These two identities make the products \(xb\) and \(bx\) behave like elementary tensors, which is the starting point of the later lessons.

We use: the conventions of Section 1 and Lemmas 1.1 and 1.3 of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#1-conventions-ultrafilters-the-bimodule-of-normal-functionals--strong-convergence), together with its Theorem 5.1 (the finite von Neumann algebra \(M_{\varphi,\omega}\)); the Ocneanu ultrapower \(M^\omega\), its faithful normal state (Lemma 2.1 and Theorem 3.2) and the normal copy of \(M\) (Section 4) of [Multiplier ultraproducts and normal embeddings](course:OA-APPROX/multiplier-ultraproducts-and-normal-embeddings#3-completeness-on-two-cyclic-vectors); Lemma 1.1 (asymptotic centralizers inside \(M^\omega\)) and Theorem 3.1 of [Asymptotic centralizers of type III₁ factors](course:bicentralizers-of-type-iii1-factors/asymptotic-centralizers-of-type-iii1-factors#1-sequences-in-the-ultrapower), and equation (1.1) there; Lemma 1.2 (four unitaries) of [The bicentralizer](course:bicentralizers-of-type-iii1-factors/the-bicentralizer#1-three-descriptions); Theorem 6.1 of [The bicentralizer of a type III₁ factor is trivial](course:bicentralizers-of-type-iii1-factors/the-bicentralizer-is-trivial#6-the-bicentralizer-theorem); the modular expectation theorem (ME.1)–(ME.3) of [Conditional expectations from modular invariance](course:OA-MOD/OA-MOD-ME#OA-MOD-ME-01), including the uniqueness of a state-preserving contractive retraction; the Schwarz inequality for conditional expectations, [CE-006](course:OA-MOD/OA-MOD-CE#OA-MOD-CE-006); the Borel functional calculus in a von Neumann algebra, [Theorem 3.1 of the spectral theorem lesson](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators#OA-FND-ST-03); and Mazur's theorem (the weak and norm closures of a convex set in a Hilbert space agree), [Weak topologies, Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian).

## 1. Setting

Throughout, \(M\) is a countably decomposable von Neumann algebra, \(N\subset M\) a von Neumann subalgebra with the same unit, \(E\colon M\to N\) a faithful normal conditional expectation, and \(\omega\) a free ultrafilter on \(\mathbb N\). For a faithful normal state \(\varphi\) on \(N\) put
\[
\bar\varphi=\varphi\circ E ,
\]
a faithful normal state on \(M\). We work in the GNS space \(H=L^2(M,\bar\varphi)\) with cyclic and separating vector \(\bar\xi\), write \(\|x\|_{\bar\varphi}=\|x\bar\xi\|\) and \(\|x\|^\sharp_{\bar\varphi}=(\|x\|_{\bar\varphi}^2+\|x^*\|_{\bar\varphi}^2)^{1/2}\), and use the bimodule notation \((x\psi)(y)=\psi(yx)\), \((\psi x)(y)=\psi(xy)\), \([x,\psi]=x\psi-\psi x\) of the ultraproduct lesson. Since \(E\) is a \(\bar\varphi\)-preserving contractive retraction onto \(N\), the modular expectation theorem gives
\[
\sigma^{\bar\varphi}_t(N)=N,\qquad\sigma^{\bar\varphi}_t|_N=\sigma^\varphi_t,\qquad E\circ\sigma_t^{\bar\varphi}=\sigma^\varphi_t\circ E\qquad(t\in\mathbb R).
\tag{1.1}
\]
Write \(\mathcal U(N)\) for the unitary group of \(N\),
\[
\mathrm{AC}(N,\varphi)=\{(x_n)\in\ell^\infty(N):\ \|[x_n,\varphi]\|\to0\},\qquad
A_{\varphi,\omega}(N)=\{(x_n)\in\ell^\infty(N):\ \lim_{n\to\omega}\|[x_n,\varphi]\|=0\},
\]
and \(\mathcal U_\delta=\{u\in\mathcal U(N):\ \|[u,\varphi]\|<\delta\}\) for \(\delta>0\). Here \(\|[x,\varphi]\|\) is the norm in \(N_*\). By (1.1) of the asymptotic centralizer lesson, \(\|[u,\varphi]\|=\|u\varphi u^*-\varphi\|\) for a unitary \(u\).

**Lemma 1.1.** For \(x\in N\),
\[
\|[x,\bar\varphi]\|_{M_*}=\|[x,\varphi]\|_{N_*},\qquad\|x\|_{\bar\varphi}=\|x\|_\varphi,\qquad \|x\|^\sharp_{\bar\varphi}=\|x\|^\sharp_\varphi .
\]
Consequently \(\mathrm{AC}(N,\varphi)\subset\mathrm{AC}(M,\bar\varphi)\), \(A_{\varphi,\omega}(N)\subset A_{\bar\varphi,\omega}(M)\), and a bounded sequence in \(N\) tends to \(0\) \(*\)-strongly along \(\omega\) as a sequence in \(N\) exactly when it does so as a sequence in \(M\).

**Proof.** Since \(E\) is \(N\)-bimodular, for \(y\in M\)
\[
[x,\bar\varphi](y)=\varphi(E(yx)-E(xy))=\varphi(E(y)x-xE(y))=[x,\varphi](E(y)).
\]
\(E\) maps the unit ball of \(M\) onto the unit ball of \(N\) (it is contractive and fixes \(N\)), so the two norms agree. Also \(\|x\|^2_{\bar\varphi}=\varphi(E(x^*x))=\varphi(x^*x)\). The last assertion is Lemma 1.3 of the ultraproduct lesson, applied in \(N\) with \(\varphi\) and in \(M\) with \(\bar\varphi\). \(\square\)

Write \(I_\omega\), \(N_\omega\) and \(M^\omega=N_\omega/I_\omega\) for the Ocneanu ultrapower of \(M\), with its faithful normal state \(\bar\varphi^\omega\), and \(\pi\colon N_\omega\to M^\omega\) for the quotient map; we identify \(M\) with the constant sequences. By Theorem 5.1 of the ultraproduct lesson applied to \((N,\varphi)\), \(N_{\varphi,\omega}=A_{\varphi,\omega}(N)/I_\omega(N)\) is a finite von Neumann algebra with faithful normal tracial state \(\tau_{\varphi,\omega}([x_n])=\lim_\omega\varphi(x_n)\).

**Lemma 1.2.** The inclusion \(A_{\varphi,\omega}(N)\subset A_{\bar\varphi,\omega}(M)\subset N_\omega\) induces an injective normal unital \(*\)-homomorphism \(N_{\varphi,\omega}\to M^\omega\) with \(\bar\varphi^\omega\circ\iota=\tau_{\varphi,\omega}\). Every element of its image commutes with \(\bar\varphi^\omega\). If \(N\) is a factor of type III₁ with separable predual, \(N_{\varphi,\omega}\) is a factor of type II₁.

**Proof.** \(A_{\bar\varphi,\omega}(M)\subset N_\omega\) by Lemma 1.1(1) of the asymptotic centralizer lesson, and the first inclusion is Lemma 1.1. The kernel of \(A_{\varphi,\omega}(N)\to M^\omega\) is \(A_{\varphi,\omega}(N)\cap I_\omega=I_\omega(N)\) by Lemma 1.1, so the induced map \(\iota\) is injective, and \(\bar\varphi^\omega(\iota[x_n])=\lim_\omega\bar\varphi(x_n)=\lim_\omega\varphi(x_n)\). If \(a_i\uparrow a\) in \(N_{\varphi,\omega}\), then \(Z=\sup_i\iota(a_i)\le\iota(a)\) and \(\bar\varphi^\omega(\iota(a)-Z)=\tau_{\varphi,\omega}(a)-\lim_i\tau_{\varphi,\omega}(a_i)=0\), so \(Z=\iota(a)\) by faithfulness: \(\iota\) is normal. Commutation with \(\bar\varphi^\omega\) is Lemma 1.1(2) of the asymptotic centralizer lesson, applied in \(M\) with \(\bar\varphi\). The last statement is Theorem 3.1 of that lesson applied to \((N,\varphi)\). \(\square\)

We identify \(N_{\varphi,\omega}\) with its image in \(M^\omega\).

Let \(\mathcal G_\varphi\) be the set of classes \(\pi(u_n)\) of sequences \((u_n)\in A_{\varphi,\omega}(N)\) consisting of unitaries of \(N\). It is a subgroup of the unitary group of \(N_{\varphi,\omega}\), since products and adjoints of such sequences are again such sequences.

**Lemma 1.3.** Every element of \(N_{\varphi,\omega}\) is a linear combination of four elements of \(\mathcal G_\varphi\). Consequently an element of \(M^\omega\) commutes with \(N_{\varphi,\omega}\) as soon as it commutes with \(\mathcal G_\varphi\).

**Proof.** \(A_{\varphi,\omega}(N)\) is a unital \(C^*\)-algebra (Theorem 5.1 of the ultraproduct lesson), and every element of a unital \(C^*\)-algebra is a linear combination of four of its unitaries ([Proposition 7.3 of the \(C^*\)-algebra lesson](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-10)). A unitary of \(A_{\varphi,\omega}(N)\) is a sequence of unitaries of \(N\). Apply \(\pi\). \(\square\)

**Lemma 1.4** (the canonical expectation). For \(X=\pi(x_n)\in M^\omega\) the \(\sigma\)-weak limit \(E_\omega(X)=\lim_{n\to\omega}x_n\) exists in \(M\) and depends only on \(X\). The map \(E_\omega\colon M^\omega\to M\) is a faithful normal conditional expectation onto \(M\), with \(\bar\varphi\circ E_\omega=\bar\varphi^\omega\) and \(E_\omega(aXb)=aE_\omega(X)b\) for \(a,b\in M\).

**Proof.** Bounded sets of \(M\) are \(\sigma\)-weakly compact, so the limit along \(\omega\) exists. A sequence in \(I_\omega\) tends to \(0\) strongly along \(\omega\), hence \(\sigma\)-weakly, so \(E_\omega\) is well defined; it is linear, unital and \(M\)-bimodular, and it is the identity on constants. If \(X\ge0\), write \(X=Y^*Y\) with \(Y=\pi(y_n)\); then \(X=\pi(y_n^*y_n)\) and \(E_\omega(X)=\lim_\omega y_n^*y_n\ge0\). By \(\sigma\)-weak continuity of \(\bar\varphi\), \(\bar\varphi(E_\omega(X))=\lim_\omega\bar\varphi(x_n)=\bar\varphi^\omega(X)\). If \(X\ge0\) and \(E_\omega(X)=0\), then \(\bar\varphi^\omega(X)=0\) and \(X=0\). If \(X_i\uparrow X\), then \(E_\omega(X_i)\uparrow Z\le E_\omega(X)\) and \(\bar\varphi(E_\omega(X)-Z)=\bar\varphi^\omega(X)-\lim_i\bar\varphi^\omega(X_i)=0\) by normality of \(\bar\varphi^\omega\), so \(Z=E_\omega(X)\). \(\square\)

For \(X=\pi(x_n)\) we have \(\|X\|_{\bar\varphi^\omega}=\lim_\omega\|x_n\|_{\bar\varphi}\), by the definition of \(\bar\varphi^\omega\) and multiplicativity of \(\pi\); in particular \(\langle X,Y\rangle_{\bar\varphi^\omega}=\bar\varphi^\omega(Y^*X)=\lim_\omega\bar\varphi(y_n^*x_n)\).

## 2. The relative bicentralizer

**Definition 2.1.** The *relative bicentralizer* of \(\varphi\) is
\[
\mathrm B(N\subset M,\varphi)=\{a\in M:\ \|[a,x_n]\|_{\bar\varphi}\to0\ \text{ for every }(x_n)\in\mathrm{AC}(N,\varphi)\}.
\]

By Lemma 1.3 of the ultraproduct lesson, the condition says that \([a,x_n]\to0\) strongly; it does not depend on the faithful normal state used to measure it, so \(\mathrm B(N\subset M,\varphi)\) does not depend on \(E\). For \(N=M\) and \(E=\mathrm{id}\) it is the bicentralizer \(\mathrm B(M,\varphi)\).

**Proposition 2.2.** For every \(a\in M\) the following are equivalent:

1. \(a\in\mathrm B(N\subset M,\varphi)\);
2. \(\lim_\omega\|[a,x_n]\|_{\bar\varphi}=0\) for every \((x_n)\in A_{\varphi,\omega}(N)\);
3. \(aX=Xa\) in \(M^\omega\) for every \(X\in N_{\varphi,\omega}\);
4. for every \(\varepsilon>0\) there is \(\delta>0\) with \(\|u^*au-a\|_{\bar\varphi}<\varepsilon\) for every \(u\in\mathcal U_\delta\).

**Proof.** (2)\(\Leftrightarrow\)(3). For \(X=\pi(x_n)\) with \((x_n)\in A_{\varphi,\omega}(N)\), \(aX-Xa=\pi(ax_n-x_na)\) and \(\|aX-Xa\|_{\bar\varphi^\omega}=\lim_\omega\|[a,x_n]\|_{\bar\varphi}\); \(\bar\varphi^\omega\) is faithful.

(2)\(\Rightarrow\)(1). If \((x_n)\in\mathrm{AC}(N,\varphi)\) and \(\|[a,x_{n_k}]\|_{\bar\varphi}\ge c>0\) along a subsequence, then \((x_{n_k})_k\in\mathrm{AC}(N,\varphi)\subset A_{\varphi,\omega}(N)\) contradicts (2).

(1)\(\Rightarrow\)(2). Let \((x_n)\in A_{\varphi,\omega}(N)\) with \(c=\lim_\omega\|[a,x_n]\|_{\bar\varphi}>0\). The sets \(\{n:\|[x_n,\varphi]\|<1/j,\ \|[a,x_n]\|_{\bar\varphi}>c/2\}\) belong to \(\omega\) and are infinite, so there are \(n_1<n_2<\cdots\) with \(n_j\) in the \(j\)-th set; then \((x_{n_j})_j\in\mathrm{AC}(N,\varphi)\) contradicts (1).

(1)\(\Leftrightarrow\)(4). For a unitary \(u\), \([a,u]=u(u^*au-a)\) and \(\|uy\|_{\bar\varphi}=\|y\|_{\bar\varphi}\), so \(\|[a,u]\|_{\bar\varphi}=\|u^*au-a\|_{\bar\varphi}\). If (4) fails, there are \(\varepsilon>0\) and \(u_j\in\mathcal U_{1/j}\) with \(\|[a,u_j]\|_{\bar\varphi}\ge\varepsilon\), against (1). Conversely (4) gives \(\|[a,u_n]\|_{\bar\varphi}\to0\) for every unitary \((u_n)\in\mathrm{AC}(N,\varphi)\); by Lemma 1.2 of the bicentralizer lesson, applied to \((N,\varphi)\), every element of the \(C^*\)-algebra \(\mathrm{AC}(N,\varphi)\) is a linear combination of four of its unitaries, which gives (1). \(\square\)

So \(\mathrm B(N\subset M,\varphi)=(N_{\varphi,\omega})'\cap M\), the relative commutant being taken in \(M^\omega\), for every free ultrafilter \(\omega\).

**Theorem 2.3.** \(\mathrm B=\mathrm B(N\subset M,\varphi)\) is a von Neumann subalgebra of \(M\), and
\[
N'\cap M\subset\mathrm B\subset(N_\varphi)'\cap M,\qquad\sigma_t^{\bar\varphi}(\mathrm B)=\mathrm B\ (t\in\mathbb R),\qquad\mathrm B\cap N=\mathrm B(N,\varphi).
\]
There is a unique \(\bar\varphi\)-preserving normal conditional expectation \(E_{\mathrm B}\) of \(M\) onto \(\mathrm B\); it is faithful.

**Proof.** By Proposition 2.2, \(\mathrm B\) is the set of constants commuting with the self-adjoint set \(N_{\varphi,\omega}\subset M^\omega\): a unital \(*\)-subalgebra. If \(a_i\in\mathrm B\) is a bounded net converging \(\sigma\)-weakly to \(a\in M\), it converges \(\sigma\)-weakly in \(M^\omega\) (the constant embedding is normal), and commutants are \(\sigma\)-weakly closed, so \(a\in\mathrm B\). By Kaplansky's density theorem, exactly as in the proof of Theorem 2.1 of the bicentralizer lesson, a unital \(*\)-algebra with this property is \(\sigma\)-weakly closed. Elements of \(N'\cap M\) commute with every \(x_n\in N\). A constant \(x\in N_\varphi\) gives \((x)\in\mathrm{AC}(N,\varphi)\), so \([a,x]=0\) for \(a\in\mathrm B\).

By (1.1) and \(\varphi\circ\sigma^\varphi_t=\varphi\), \(\|[\sigma_t^{\varphi}(x),\varphi]\|=\|[x,\varphi]\|\) for \(x\in N\), so \(\mathrm{AC}(N,\varphi)\) is invariant under \(\sigma^\varphi_t\) termwise. For \(a\in\mathrm B\) and \((x_n)\in\mathrm{AC}(N,\varphi)\),
\[
\|[\sigma_t^{\bar\varphi}(a),x_n]\|_{\bar\varphi}=\|\sigma_t^{\bar\varphi}([a,\sigma^{\varphi}_{-t}(x_n)])\|_{\bar\varphi}=\|[a,\sigma^\varphi_{-t}(x_n)]\|_{\bar\varphi}\to0,
\]
since \(\bar\varphi\circ\sigma^{\bar\varphi}_t=\bar\varphi\). So \(\mathrm B\) is \(\sigma^{\bar\varphi}\)-invariant, and the modular expectation theorem gives a unique \(\bar\varphi\)-preserving contractive retraction onto \(\mathrm B\), which is a faithful normal conditional expectation. Finally, for \(a\in N\), \(\|[a,x_n]\|_{\bar\varphi}=\|[a,x_n]\|_\varphi\) by Lemma 1.1, which gives \(\mathrm B\cap N=\mathrm B(N,\varphi)\). \(\square\)

Since \(E_{\mathrm B}\) is \(\mathrm B\)-bimodular and \(\bar\varphi\)-preserving, \(\langle z,b\rangle_{\bar\varphi}=\bar\varphi(b^*z)=\bar\varphi(b^*E_{\mathrm B}(z))\) for \(z\in M\), \(b\in\mathrm B\): the map \(z\bar\xi\mapsto E_{\mathrm B}(z)\bar\xi\) is the orthogonal projection of \(H\) onto the closure of \(\mathrm B\bar\xi\). In particular \(E_{\mathrm B}(z)=0\) exactly when \(z\bar\xi\perp\mathrm B\bar\xi\).

**Lemma 2.4** (uniform modulus). Let \(a\in\mathrm B(N\subset M,\varphi)\) and \(\varepsilon>0\). There is \(\delta>0\) such that \(\|[a,y]\|^\sharp_{\bar\varphi}\le\varepsilon\) for every \(y\in N\) with \(\|y\|\le1\) and \(\|[y,\varphi]\|\le\delta\).

**Proof.** Otherwise there are contractions \(y_k\in N\) with \(\|[y_k,\varphi]\|\le1/k\) and \(\|[a,y_k]\|^\sharp_{\bar\varphi}>\varepsilon\). Then \((y_k)\) and \((y_k^*)\) belong to \(\mathrm{AC}(N,\varphi)\) (Lemma 1.1(a) of the ultraproduct lesson), and \(a,a^*\in\mathrm B(N\subset M,\varphi)\) by Theorem 2.3, so \(\|[a,y_k]\|_{\bar\varphi}\to0\) and \(\|[a,y_k]^*\|_{\bar\varphi}=\|[a^*,y_k^*]\|_{\bar\varphi}\to0\), a contradiction. \(\square\)

**Proposition 2.5.** \(E(\mathrm B(N\subset M,\varphi))\subset\mathrm B(N,\varphi)\).

**Proof.** Let \(a\in\mathrm B(N\subset M,\varphi)\) and \((x_n)\in\mathrm{AC}(N,\varphi)\). Since \(E\) is \(N\)-bimodular, \([E(a),x_n]=E([a,x_n])\), and the Schwarz inequality \(E(z)^*E(z)\le E(z^*z)\) gives
\[
\|[E(a),x_n]\|_\varphi^2=\varphi(E([a,x_n])^*E([a,x_n]))\le\bar\varphi([a,x_n]^*[a,x_n])=\|[a,x_n]\|^2_{\bar\varphi}\to0 .\qquad\square
\]

**Corollary 2.6.** Suppose \(N\) is a factor of type III₁ with separable predual, and write \(\mathrm B=\mathrm B(N\subset M,\varphi)\). Then
\[
E(b)=\bar\varphi(b)1\quad(b\in\mathrm B),\qquad E_{\mathrm B}(x)=\varphi(x)1\quad(x\in N),
\]
and consequently \(\bar\varphi(xb)=\bar\varphi(bx)=\varphi(x)\bar\varphi(b)\) for \(x\in N\), \(b\in\mathrm B\).

**Proof.** By Proposition 2.5 and Theorem 6.1 of the trivial bicentralizer lesson, \(E(b)\in\mathrm B(N,\varphi)=\mathbb C1\), and the scalar is \(\varphi(E(b))=\bar\varphi(b)\). For \(x\in N\) and \(b\in\mathrm B\), bimodularity of \(E\) gives
\[
\bar\varphi(xb)=\varphi(xE(b))=\varphi(x)\bar\varphi(b),\qquad\bar\varphi(bx)=\varphi(E(b)x)=\bar\varphi(b)\varphi(x).
\]
The second identity, with \(b^*\) in place of \(b\), says \(\langle x,b\rangle_{\bar\varphi}=\langle\varphi(x)1,b\rangle_{\bar\varphi}\) for all \(b\in\mathrm B\); since \(\varphi(x)1\in\mathrm B\), this is \(E_{\mathrm B}(x)=\varphi(x)1\). \(\square\)

## 3. Averaging by asymptotically centralizing unitaries

**Lemma 3.1** (averaging over state-preserving automorphisms). Let \(P\) be a von Neumann algebra with a faithful normal state \(\psi\), \(G\) a group of \(\psi\)-preserving \(*\)-automorphisms of \(P\), and \(P^G\) its fixed-point algebra. For \(X\in P\) let \(K_G(X)\) be the \(\sigma\)-weakly closed convex hull of \(\{\alpha(X):\alpha\in G\}\).

1. \(K_G(X)\cap P^G\) consists of exactly one element \(E_G(X)\), which is also the unique element of \(K_G(X)\) of minimal \(\|\cdot\|_\psi\)-norm. The map \(E_G\) is the unique \(\psi\)-preserving conditional expectation of \(P\) onto \(P^G\); it is normal and faithful, and \(\langle X-E_G(X),Z\rangle_\psi=0\) for \(Z\in P^G\).
2. If \(E_G(X)=0\), there is \(\alpha\in G\) with \(\|\alpha(X)-X\|_\psi\ge\|X\|_\psi\).

**Proof.** (1) \(K_G(X)\) is a \(\sigma\)-weakly compact convex set, and \(Y\mapsto Y\xi_\psi\) is injective and continuous from the \(\sigma\)-weak to the weak topology, so \(K_G(X)\xi_\psi\) is weakly compact and convex and has a unique vector \(Y_0\xi_\psi\) of minimal norm, \(Y_0\in K_G(X)\). Automorphisms of von Neumann algebras are \(\sigma\)-weakly continuous, so each \(\alpha\in G\) maps \(K_G(X)\) onto itself, and \(\|\alpha(Y)\|_\psi=\|Y\|_\psi\); hence \(\alpha(Y_0)=Y_0\), and \(Y_0\in P^G\). For \(Z\in P^G\) and \(\alpha\in G\), \(\langle\alpha(X),Z\rangle_\psi=\psi(\alpha(Z^*X))=\langle X,Z\rangle_\psi\), so \(Y\mapsto\langle Y,Z\rangle_\psi\) is constant on \(K_G(X)\). If \(Y,Y'\in K_G(X)\cap P^G\), then \(\langle Y-Y',Z\rangle_\psi=0\) for all \(Z\in P^G\), in particular for \(Z=Y-Y'\), so \(Y=Y'\). Thus \(K_G(X)\cap P^G=\{Y_0\}\); put \(E_G(X)=Y_0\). Then \(E_G(X)\xi_\psi\) is the orthogonal projection of \(X\xi_\psi\) onto the closure of \(P^G\xi_\psi\), so \(E_G\) is linear. It is positive (\(K_G(X)\subset P_+\) when \(X\ge0\)), unital, \(\psi\)-preserving (take \(Z=1\)), and \(P^G\)-bimodular, because \(Z_1K_G(X)Z_2=K_G(Z_1XZ_2)\) for \(Z_1,Z_2\in P^G\) and \(Z_1E_G(X)Z_2\in K_G(Z_1XZ_2)\cap P^G\). So \(E_G\) is a \(\psi\)-preserving conditional expectation onto \(P^G\); by the modular expectation theorem it is unique, normal and faithful.

(2) Suppose \(X\ne0\) and \(\|\alpha(X)-X\|_\psi<\|X\|_\psi\) for all \(\alpha\). Since \(\|\alpha(X)\|_\psi=\|X\|_\psi\), this says \(\operatorname{Re}\langle\alpha(X),X\rangle_\psi>\frac12\|X\|_\psi^2\). The set of \(Y\in P\) with \(\operatorname{Re}\langle Y,X\rangle_\psi\ge\frac12\|X\|^2_\psi\) is convex and \(\sigma\)-weakly closed, so it contains \(K_G(X)\ni E_G(X)=0\), which is absurd. \(\square\)

Apply Lemma 3.1 to \(P=M^\omega\), \(\psi=\bar\varphi^\omega\) and \(G=\{\operatorname{Ad}U:U\in\mathcal G_\varphi\}\). These automorphisms preserve \(\bar\varphi^\omega\) by Lemma 1.2, and by Lemma 1.3 the fixed-point algebra is
\[
Q_\varphi=(N_{\varphi,\omega})'\cap M^\omega .
\]
Write \(F_\varphi\) for the \(\bar\varphi^\omega\)-preserving conditional expectation of \(M^\omega\) onto \(Q_\varphi\). By Proposition 2.2, \(Q_\varphi\cap M=\mathrm B(N\subset M,\varphi)\).

**Lemma 3.2** (uniformity). Let \(X=\pi(x_n)\in M^\omega\). Then \(X\in Q_\varphi\) if and only if for every \(\varepsilon>0\) there are \(\delta>0\) and \(A\in\omega\) such that
\[
\|ux_nu^*-x_n\|_{\bar\varphi}\le\varepsilon\qquad(n\in A,\ u\in\mathcal U_\delta).
\]

**Proof.** Suppose the condition holds and let \(U=\pi(u_n)\in\mathcal G_\varphi\), with unitaries \(u_n\) and \(\lim_\omega\|[u_n,\varphi]\|=0\). Given \(\varepsilon\), with \(\delta,A\) as in the condition, the set of \(n\in A\) with \(u_n\in\mathcal U_\delta\) belongs to \(\omega\), so \(\|UXU^*-X\|_{\bar\varphi^\omega}=\lim_\omega\|u_nx_nu_n^*-x_n\|_{\bar\varphi}\le\varepsilon\). Hence \(UXU^*=X\), and \(X\in Q_\varphi\) by Lemma 1.3.

Conversely suppose the condition fails for some \(\varepsilon\). For each \(k\) the set
\[
B_k=\{n:\ \text{some }u\in\mathcal U_{1/k}\text{ has }\|ux_nu^*-x_n\|_{\bar\varphi}>\varepsilon\}
\]
belongs to \(\omega\) (otherwise its complement would serve as \(A\) with \(\delta=1/k\)), and \(B_1\supset B_2\supset\cdots\). For \(n\in B_1\) let \(k(n)\) be the largest \(k\le n\) with \(n\in B_k\), and choose \(u_n\in\mathcal U_{1/k(n)}\) with \(\|u_nx_nu_n^*-x_n\|_{\bar\varphi}>\varepsilon\); for \(n\notin B_1\) put \(u_n=1\). For every \(K\), \(\{n:k(n)\ge K\}\supset B_K\cap\{n\ge K\}\in\omega\), so \(\lim_\omega\|[u_n,\varphi]\|=0\), and \(U=\pi(u_n)\in\mathcal G_\varphi\). But \(\|UXU^*-X\|_{\bar\varphi^\omega}\ge\varepsilon\) because \(B_1\in\omega\), so \(X\notin Q_\varphi\). \(\square\)

For \(x\in M\) and \(\delta>0\) let \(K_\delta(x)\) be the \(\sigma\)-weakly closed convex hull in \(M\) of \(\{uxu^*:u\in\mathcal U_\delta\}\). As in the proof of Lemma 3.1, \(K_\delta(x)\) has a unique element \(y_\delta(x)\) of minimal \(\|\cdot\|_{\bar\varphi}\)-norm. We use the elementary estimate, valid for a unitary \(v\in N\) and \(w\in M\):
\[
\|wv^*\|^2_{\bar\varphi}=\bar\varphi(vw^*wv^*)=(v^*\bar\varphi v)(w^*w)\le\|w\|^2_{\bar\varphi}+\|w\|^2\,\|[v,\varphi]\| ,
\tag{3.1}
\]
because \(\|v^*\bar\varphi v-\bar\varphi\|=\|\bar\varphi-v\bar\varphi v^*\|=\|[v,\bar\varphi]\|=\|[v,\varphi]\|\) by Lemma 1.1; the same bound holds for \(\|wv\|^2_{\bar\varphi}\). Also \(\|vw\|_{\bar\varphi}=\|w\|_{\bar\varphi}\).

**Proposition 3.3.** For every \(x\in M\) and \(\delta>0\), \(y_\delta(x)\in\mathrm B(N\subset M,\varphi)\).

**Proof.** Put \(y=y_\delta(x)\), \(m=\|y\|_{\bar\varphi}\), and let \(C_\eta\) be the convex hull of \(\{uxu^*:u\in\mathcal U_\eta\}\). Since \(\mathcal U_\delta=\bigcup_{\eta<\delta}\mathcal U_\eta\), \(C_\delta\) is the increasing union of the \(C_\eta\), \(\eta<\delta\). The vector \(y\bar\xi\) is a weak limit of vectors in \(C_\delta\bar\xi\), so by Mazur's theorem it is a norm limit of such vectors: for every \(k\) there are \(\eta_k<\delta\) and \(z^{(k)}\in C_{\eta_k}\) with \(\|z^{(k)}-y\|_{\bar\varphi}<1/k\), and we may take \(\eta_1\le\eta_2\le\cdots\).

For \(w\in K_\delta(x)\), \((w+y)/2\in K_\delta(x)\), so the parallelogram law gives
\[
\|w-y\|^2_{\bar\varphi}=2\|w\|^2_{\bar\varphi}+2m^2-4\|(w+y)/2\|^2_{\bar\varphi}\le2\|w\|^2_{\bar\varphi}-2m^2 .
\tag{3.2}
\]

Let \((v_n)\) be unitaries of \(N\) with \(\theta_n=\|[v_n,\varphi]\|\to0\). For \(n\) with \(\theta_n<\delta-\eta_1\) let \(k(n)\) be the largest \(k\le n\) with \(\theta_n<\delta-\eta_k\); then \(k(n)\to\infty\). Put \(z_n=z^{(k(n))}\). If \(u\in\mathcal U_{\eta_{k(n)}}\), then \(\|[v_nu,\varphi]\|\le\theta_n+\|[u,\varphi]\|<\delta\) by Lemma 1.1(d) of the ultraproduct lesson, so \(v_nz_nv_n^*\in C_\delta\subset K_\delta(x)\). By (3.1), \(\|v_nz_nv_n^*\|^2_{\bar\varphi}\le\|z_n\|^2_{\bar\varphi}+\|x\|^2\theta_n\to m^2\), so (3.2) gives \(\|v_nz_nv_n^*-y\|_{\bar\varphi}\to0\). Also by (3.1), \(\|v_n(y-z_n)v_n^*\|^2_{\bar\varphi}\le\|y-z_n\|^2_{\bar\varphi}+4\|x\|^2\theta_n\to0\). Hence \(\|v_nyv_n^*-y\|_{\bar\varphi}\to0\), and again by (3.1)
\[
\|[v_n,y]\|^2_{\bar\varphi}=\|(v_nyv_n^*-y)v_n\|^2_{\bar\varphi}\le\|v_nyv_n^*-y\|^2_{\bar\varphi}+4\|x\|^2\theta_n\to0 .
\]
This holds for every unitary sequence in \(\mathrm{AC}(N,\varphi)\), hence, by the four-unitary decomposition used in Proposition 2.2, for every sequence in \(\mathrm{AC}(N,\varphi)\). So \(y\in\mathrm B(N\subset M,\varphi)\). \(\square\)

**Theorem 3.4.** Write \(\mathrm B=\mathrm B(N\subset M,\varphi)\).

1. \(E_\omega(Q_\varphi)\subset\mathrm B\).
2. \(E_{\mathrm B}=E_\omega\circ F_\varphi|_M\).
3. For every \(\delta>0\), every finite set \(S\subset M\) and every \(\varepsilon>0\) there is a probability measure \(\mu\) on \(\mathcal U_\delta\) with finite support such that
\[
\Big\|\int uxu^*\,d\mu(u)-E_{\mathrm B}(x)\Big\|^\sharp_{\bar\varphi}<\varepsilon\qquad(x\in S).
\]
4. In particular \(E_{\mathrm B}(x)\in K_\delta(x)\) for every \(x\in M\) and \(\delta>0\).
5. If \(z\in M\) and \(E_{\mathrm B}(z)=0\), then \(F_\varphi(z)=0\), and there is \(U\in\mathcal G_\varphi\) with \(\|UzU^*-z\|_{\bar\varphi^\omega}\ge\|z\|_{\bar\varphi}\).

**Proof.** (1) Let \(X=\pi(x_n)\in Q_\varphi\), \(a=E_\omega(X)\), and \(\varepsilon>0\); take \(\delta,A\) from Lemma 3.2. For \(u\in\mathcal U_\delta\), \(uau^*-a\) is the \(\sigma\)-weak limit along \(\omega\) of \(ux_nu^*-x_n\), and the map \(y\mapsto y\bar\xi\) is \(\sigma\)-weak to weak continuous, so \(\|uau^*-a\|_{\bar\varphi}\le\lim_\omega\|ux_nu^*-x_n\|_{\bar\varphi}\le\varepsilon\). Since \(u^*\in\mathcal U_\delta\) whenever \(u\in\mathcal U_\delta\), Proposition 2.2(4) gives \(a\in\mathrm B\).

(2) The map \(E_\omega\circ F_\varphi|_M\) takes values in \(\mathrm B\) by (1), and is the identity on \(\mathrm B\subset Q_\varphi\). It is a positive unital \(\mathrm B\)-bimodular map, hence a contractive retraction onto \(\mathrm B\), and \(\bar\varphi\circ E_\omega\circ F_\varphi=\bar\varphi^\omega\circ F_\varphi=\bar\varphi^\omega\) restricts to \(\bar\varphi\) on \(M\). By the uniqueness in the modular expectation theorem it equals \(E_{\mathrm B}\).

(3) Let \(S=\{x_1,\ldots,x_k\}\) and enlarge it to contain the adjoints. Apply Lemma 3.1 to \(P=(M^\omega)^{\oplus k}\) with the state \(\frac1k\sum_i\bar\varphi^\omega\) and the diagonal action of \(\mathcal G_\varphi\): its fixed-point algebra is \(Q_\varphi^{\oplus k}\), and by uniqueness its expectation is \(F_\varphi^{\oplus k}\). So \((F_\varphi(x_i))_i\) is a \(\sigma\)-weak limit of convex combinations \(\big(\sum_j\lambda_jU_jx_iU_j^*\big)_i\) with \(U_j\in\mathcal G_\varphi\). Applying the normal map \(E_\omega\) and (2), \((E_{\mathrm B}(x_i))_i\) is a \(\sigma\)-weak limit of the tuples \(\big(E_\omega(\sum_j\lambda_jU_jx_iU_j^*)\big)_i\). Write \(U_j=\pi(u_{j,n})\) with unitaries \(u_{j,n}\in N\) and \(\lim_\omega\|[u_{j,n},\varphi]\|=0\). Then \(E_\omega(\sum_j\lambda_jU_jx_iU_j^*)\) is the \(\sigma\)-weak limit along \(\omega\) of \(\sum_j\lambda_ju_{j,n}x_iu_{j,n}^*\), and for \(n\) in a set belonging to \(\omega\) all \(u_{j,n}\) lie in \(\mathcal U_\delta\). Consequently \((E_{\mathrm B}(x_i))_i\) lies in the \(\sigma\)-weak closure, in \(M^{\oplus k}\), of the convex set of tuples \(\big(\int ux_iu^*d\mu(u)\big)_i\) with \(\mu\) finitely supported on \(\mathcal U_\delta\). Passing to the vectors \((y_i\bar\xi)_i\in H^{\oplus k}\), Mazur's theorem turns the weak approximation into a norm approximation; since the adjoints are in \(S\), this is the \(\|\cdot\|^\sharp_{\bar\varphi}\) estimate.

(4) is the case \(S=\{x\}\) of the argument in (3), before Mazur's theorem.

(5) Let \(X=\pi(x_n)\in Q_\varphi\) and \(\varepsilon>0\), with \(\delta,A\) from Lemma 3.2. For \(n\in A\) every element of \(C_\delta(x_n)\), hence of \(K_\delta(x_n)\), lies within \(\varepsilon\) of \(x_n\) in \(\|\cdot\|_{\bar\varphi}\) (weak lower semicontinuity of the norm), so \(\|y_\delta(x_n)-x_n\|_{\bar\varphi}\le\varepsilon\). By Proposition 3.3, \(y_\delta(x_n)\in\mathrm B\), so \(\langle y_\delta(x_n),z\rangle_{\bar\varphi}=0\) since \(E_{\mathrm B}(z)=0\). Hence \(|\langle x_n,z\rangle_{\bar\varphi}|\le\varepsilon\|z\|_{\bar\varphi}\) for \(n\in A\), and
\[
|\langle X,z\rangle_{\bar\varphi^\omega}|=\lim_\omega|\bar\varphi(z^*x_n)|\le\varepsilon\|z\|_{\bar\varphi} .
\]
So \(z\perp Q_\varphi\) in \(L^2(M^\omega,\bar\varphi^\omega)\), and \(\|F_\varphi(z)\|^2_{\bar\varphi^\omega}=\langle z,F_\varphi(z)\rangle_{\bar\varphi^\omega}=0\) by Lemma 3.1(1). Lemma 3.1(2) gives the unitary. \(\square\)

Part (3) is the averaging statement used by Marrakchi to construct the zero-shift maps of a later lesson [M2, Lemma 2.2(1)]; part (5) is the form of the argument of [AHHM, Proposition 3.3] used in the construction of amenable subalgebras.

## 4. Exercises

**Exercise 4.1.** Let \(Q\) be a von Neumann algebra with faithful normal state \(\chi\), and consider \(N\otimes1\subset N\bar\otimes Q\) with the expectation \(\mathrm{id}\otimes\chi\). Show that \(\mathrm B(N,\varphi)\bar\otimes Q\subset\mathrm B(N\otimes1\subset N\bar\otimes Q,\varphi)\).

**Exercise 4.2.** In the setting of Exercise 4.1, assume that \(N\) is a factor of type III₁ with separable predual. Show that \(\mathrm B(N\otimes1\subset N\bar\otimes Q,\varphi)=1\otimes Q\).

**Exercise 4.3.** Show that \(\mathrm B(N\subset M,\varphi)\) contains \(\mathrm B(N,\varphi)\vee(N'\cap M)\), and that for \(N\) a factor of type III₁ with separable predual every element \(b\) of \(\mathrm B(N\subset M,\varphi)\) satisfies \(E(b^*b)=\bar\varphi(b^*b)1\).

**Exercise 4.4.** Let \(P=M_2(\mathbb C)\), \(\psi=\operatorname{Tr}/2\), \(G=\{\mathrm{id},\operatorname{Ad}u\}\) with \(u=\operatorname{diag}(1,-1)\), and \(X=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Compute \(E_G(X)\) and \(\|uXu^*-X\|_\psi\), and compare with Lemma 3.1(2).

## 5. Solutions

**4.1.** For \(b\in\mathrm B(N,\varphi)\), \(q\in Q\) and \((x_n)\in\mathrm{AC}(N,\varphi)\), \([b\otimes q,x_n\otimes1]=[b,x_n]\otimes q\), and \(\|[b,x_n]\otimes q\|_{\varphi\otimes\chi}\le\|q\|\,\|[b,x_n]\|_\varphi\to0\). So the algebraic tensor product lies in the relative bicentralizer, which is a von Neumann algebra by Theorem 2.3.

**4.2.** Let \(a\) be in the relative bicentralizer, \(\eta\) a vector in the GNS space \(K\) of \(\chi\) and \(\omega_\eta=\langle\,\cdot\,\eta,\eta\rangle\). For bounded \(z_n\to0\) strongly, the slice \((\mathrm{id}\otimes\omega_\eta)(z_n)\) satisfies \(\|(\mathrm{id}\otimes\omega_\eta)(z_n)\zeta\|\le\|\eta\|\,\|z_n(\zeta\otimes\eta)\|\to0\) for every vector \(\zeta\), so it tends to \(0\) strongly. Applied to \(z_n=[a,x_n\otimes1]\) this shows \([(\mathrm{id}\otimes\omega_\eta)(a),x_n]\to0\) strongly, so the slice lies in \(\mathrm B(N,\varphi)=\mathbb C1\). Slices by vector functionals determine \(a\), and an element whose slices are all scalar lies in \(1\otimes Q\). The reverse inclusion is Exercise 4.1.

**4.3.** \(\mathrm B(N,\varphi)\subset\mathrm B(N\subset M,\varphi)\) by Lemma 1.1, \(N'\cap M\subset\mathrm B(N\subset M,\varphi)\) by Theorem 2.3, and the latter is an algebra. For the second statement apply Corollary 2.6 to \(b^*b\in\mathrm B(N\subset M,\varphi)\).

**4.4.** The fixed-point algebra is the diagonal, and \(E_G(X)=\frac12(X+uXu^*)=0\). Here \(uXu^*=-X\), so \(\|uXu^*-X\|_\psi=2\|X\|_\psi\ge\|X\|_\psi\), as Lemma 3.1(2) predicts.

## References

- [AHHM] H. Ando, U. Haagerup, C. Houdayer, A. Marrakchi, Structure of bicentralizer algebras and inclusions of type III factors, Mathematische Annalen 376 (2020), 1145–1194. https://arxiv.org/abs/1804.05706
- [M1] A. Marrakchi, Kadison's problem for type III subfactors and the bicentralizer conjecture, Inventiones Mathematicae 239 (2025), 79–163. https://arxiv.org/abs/2308.15163
- [M2] A. Marrakchi, Kadison's problem and ergodicity of the bicentralizer flow (2026). https://arxiv.org/abs/2606.23636
