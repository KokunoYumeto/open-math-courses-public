# The bicentralizer

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The centralizer \(M_\varphi\) of a faithful normal state consists of the elements that commute exactly with \(\varphi\). Connes introduced a weaker requirement: an element \(a\) lies in the *bicentralizer* of \(\varphi\) when it asymptotically commutes with every bounded sequence that asymptotically commutes with \(\varphi\). The bicentralizer always contains the centre of \(M\), and Connes asked whether, for a type III₁ factor with separable predual, it is always trivial. This lesson develops its basic structure: three equivalent descriptions, one of them inside the Ocneanu ultrapower; the fact that it is a von Neumann subalgebra with a state-preserving conditional expectation; the theorem of Houdayer and Isono that it is its own bicentralizer [HI]; and, for type III₁ factors, the triviality of its centre and of the centralizer of the restricted state.

We use [Asymptotic centralizers of type III₁ factors](asymptotic-centralizers-of-type-iii1-factors.md) (Lemma 1.1 and Theorem 3.1); the conventions of Section 1, Lemmas 1.1 and 1.3 and the results (B2), (B6) listed in [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons); the normal copy of \(M\) in the Ocneanu ultrapower from Section 4 of [Multiplier ultraproducts and normal embeddings](course:OA-APPROX/multiplier-ultraproducts-and-normal-embeddings#4-the-normal-copy-of-the-original-algebra); and the existence and uniqueness of state-preserving conditional expectations onto modular-invariant subalgebras, §§ME-01 and ME-08 of [Conditional expectations from modular invariance](course:OA-MOD/OA-MOD-ME#OA-MOD-ME-01). The notation \(M^\omega\), \(\varphi^\omega\), \(A_{\varphi,\omega}\), \(M_{\varphi,\omega}\) is that of the previous lesson.

## 1. Three descriptions

Let \(M\) be a countably decomposable von Neumann algebra and \(\varphi\) a faithful normal state on \(M\).

**Definition 1.1.** The *asymptotic centralizer* of \(\varphi\) is
\[
\mathrm{AC}(M,\varphi)=\{(x_n)\in\ell^\infty(M):\ \|[x_n,\varphi]\|\to0\},
\]
and the *bicentralizer* is
\[
\mathrm B(M,\varphi)=\{a\in M:\ \|[a,x_n]\|_\varphi\to0\ \text{ for every }(x_n)\in\mathrm{AC}(M,\varphi)\}.
\]
For a free ultrafilter \(\omega\) put \(\mathrm B_\omega(M,\varphi)=\{a\in M:\lim_\omega\|[a,x_n]\|_\varphi=0\ \text{for every }(x_n)\in A_{\varphi,\omega}\}\).

Here \([a,x]=ax-xa\), and \([x,\varphi]=x\varphi-\varphi x\) in the bimodule notation of the previous lesson.

**Lemma 1.2.** \(\mathrm{AC}(M,\varphi)\) is a unital \(C^*\)-subalgebra of \(\ell^\infty(M)\). Its unitaries are the sequences of unitaries \((u_n)\) with \(\|[u_n,\varphi]\|\to0\), and every element is a linear combination of four of them.

**Proof.** By Lemma 1.1(a) and (d) of the ultraproduct lesson, \(\|[x^*,\varphi]\|=\|[x,\varphi]\|\) and \(\|[xy,\varphi]\|\le\|x\|\|[y,\varphi]\|+\|y\|\|[x,\varphi]\|\); and \(\|[x,\varphi]-[y,\varphi]\|\le2\|x-y\|\) gives norm closure. A unitary of \(\ell^\infty(M)\) is a sequence of unitaries. Every element of a unital \(C^*\)-algebra is a linear combination of four unitaries of that algebra. \(\square\)

**Proposition 1.3.** For every free ultrafilter \(\omega\) and every \(a\in M\), the following are equivalent:

1. \(a\in\mathrm B(M,\varphi)\);
2. \(a\in\mathrm B_\omega(M,\varphi)\);
3. \(aX=Xa\) in \(M^\omega\) for every \(X\in M_{\varphi,\omega}\);
4. for every \(\varepsilon>0\) there is \(\delta>0\) such that every unitary \(u\in M\) with \(\|[u,\varphi]\|<\delta\) satisfies \(\|u^*au-a\|_\varphi<\varepsilon\).

**Proof.** (2)\(\Leftrightarrow\)(3). Let \(X=[x_n]\in M_{\varphi,\omega}\), with \((x_n)\in A_{\varphi,\omega}\subset N_\omega\). The constant sequence \(a\) lies in \(N_\omega\), so \(aX-Xa\) is the class of \((ax_n-x_na)\), and \(\|aX-Xa\|_{\varphi^\omega}=\lim_\omega\|[a,x_n]\|_\varphi\). Since \(\varphi^\omega\) is faithful, \(aX=Xa\) exactly when this limit is \(0\).

(2)\(\Rightarrow\)(1). Let \((x_n)\in\mathrm{AC}(M,\varphi)\) and suppose \(\|[a,x_{n_k}]\|_\varphi\ge c>0\) along a subsequence. The sequence \(y_k=x_{n_k}\) still belongs to \(\mathrm{AC}(M,\varphi)\subset A_{\varphi,\omega}\), and \(\lim_\omega\|[a,y_k]\|_\varphi\ge c\), contradicting (2).

(1)\(\Rightarrow\)(2). Let \((x_n)\in A_{\varphi,\omega}\) with \(c=\lim_\omega\|[a,x_n]\|_\varphi>0\). For each \(j\) the set \(\{n:\|[x_n,\varphi]\|<1/j,\ \|[a,x_n]\|_\varphi>c/2\}\) belongs to \(\omega\) and is therefore infinite, so we can choose \(n_1<n_2<\cdots\) with \(n_j\) in the \(j\)-th set. Then \((x_{n_j})_j\in\mathrm{AC}(M,\varphi)\) and \(\|[a,x_{n_j}]\|_\varphi>c/2\) for all \(j\), contradicting (1).

(1)\(\Leftrightarrow\)(4). For a unitary \(u\), \([a,u]=u(u^*au-a)\), and \(\|uy\|_\varphi^2=\varphi(y^*u^*uy)=\|y\|_\varphi^2\); so \(\|[a,u]\|_\varphi=\|u^*au-a\|_\varphi\). If (4) fails, there are \(\varepsilon>0\) and unitaries \(u_j\) with \(\|[u_j,\varphi]\|<1/j\) and \(\|[a,u_j]\|_\varphi\ge\varepsilon\); then \((u_j)\in\mathrm{AC}(M,\varphi)\), and (1) fails. Conversely, (4) gives \(\|[a,u_n]\|_\varphi\to0\) for every unitary \((u_n)\in\mathrm{AC}(M,\varphi)\), and Lemma 1.2 extends this to every element of \(\mathrm{AC}(M,\varphi)\). \(\square\)

So \(\mathrm B_\omega(M,\varphi)\) does not depend on \(\omega\), and
\[
\mathrm B(M,\varphi)=(M_{\varphi,\omega})'\cap M ,
\]
the relative commutant being taken inside \(M^\omega\). In (4), the condition \(\|[u,\varphi]\|<\delta\) is equivalent to \(\|u\varphi u^*-\varphi\|<\delta\).

## 2. Structure

**Theorem 2.1.** \(\mathrm B(M,\varphi)\) is a von Neumann subalgebra of \(M\) containing the centre of \(M\), globally invariant under the modular group \(\sigma^\varphi\). There is a unique \(\varphi\)-preserving normal conditional expectation \(E\) of \(M\) onto \(\mathrm B(M,\varphi)\), and it is faithful. Moreover \(\mathrm B(M,\varphi)\subset(M_\varphi)'\cap M\).

**Proof.** By Proposition 1.3, \(\mathrm B(M,\varphi)\) is the set of constants commuting with the self-adjoint set \(M_{\varphi,\omega}\subset M^\omega\), so it is a unital \(*\)-subalgebra. If \(a_i\in\mathrm B(M,\varphi)\) is a bounded net converging \(\sigma\)-weakly to \(a\in M\), then \(a_i\to a\) \(\sigma\)-weakly in \(M^\omega\), because the constant embedding is normal; the commutant of \(M_{\varphi,\omega}\) in \(M^\omega\) is \(\sigma\)-weakly closed, so \(a\in\mathrm B(M,\varphi)\). By Kaplansky's density theorem (B2), the unit ball of the \(\sigma\)-weak closure of a \(*\)-algebra is the strong closure of its unit ball, so \(\mathrm B(M,\varphi)\) is \(\sigma\)-weakly closed. Central elements commute with everything, so they lie in \(\mathrm B(M,\varphi)\). A constant \(x\in M_\varphi\) gives \((x)\in\mathrm{AC}(M,\varphi)\), so every \(a\in\mathrm B(M,\varphi)\) satisfies \(\|[a,x]\|_\varphi=0\), that is \([a,x]=0\); hence \(\mathrm B(M,\varphi)\subset(M_\varphi)'\cap M\).

Since \(\varphi\circ\sigma_t^\varphi=\varphi\), for \(x,y\in M\) we have \((\sigma_t^\varphi(x)\varphi)(y)=\varphi(y\sigma_t^\varphi(x))=(x\varphi)(\sigma^\varphi_{-t}(y))\), and similarly on the other side; so \(\|[\sigma_t^\varphi(x),\varphi]\|=\|[x,\varphi]\|\), and \(\mathrm{AC}(M,\varphi)\) is invariant under \(\sigma_t^\varphi\) applied termwise. If \(a\in\mathrm B(M,\varphi)\) and \((x_n)\in\mathrm{AC}(M,\varphi)\), then
\[
\|[\sigma_t^\varphi(a),x_n]\|_\varphi=\|\sigma_t^\varphi([a,\sigma_{-t}^\varphi(x_n)])\|_\varphi=\|[a,\sigma^\varphi_{-t}(x_n)]\|_\varphi\to0 .
\]
So \(\mathrm B(M,\varphi)\) is invariant under \(\sigma^\varphi\), and §ME-01 of the modular expectation lesson gives a \(\varphi\)-preserving faithful normal conditional expectation onto it, unique by §ME-08 there. \(\square\)

Write \(\mathrm B=\mathrm B(M,\varphi)\), \(\varphi_{\mathrm B}=\varphi|_{\mathrm B}\), and \(E\) for the expectation of Theorem 2.1. Since \(E\) is a \(\mathrm B\)-bimodule map with \(\varphi\circ E=\varphi\),
\[
\varphi(yb)=\varphi_{\mathrm B}(E(y)b),\qquad\varphi(by)=\varphi_{\mathrm B}(bE(y))\qquad(y\in M,\ b\in\mathrm B).
\tag{2.1}
\]

**Proposition 2.2** (Houdayer–Isono). \(\mathrm B(\mathrm B,\varphi_{\mathrm B})=\mathrm B\).

**Proof.** Always \(\mathrm B(\mathrm B,\varphi_{\mathrm B})\subset\mathrm B\). Let \((x_n)\in\mathrm{AC}(\mathrm B,\varphi_{\mathrm B})\). By (2.1), for \(y\in M\),
\[
[x_n,\varphi](y)=\varphi(yx_n)-\varphi(x_ny)=\varphi_{\mathrm B}(E(y)x_n-x_nE(y))=[x_n,\varphi_{\mathrm B}](E(y)),
\]
so \(\|[x_n,\varphi]\|\le\|[x_n,\varphi_{\mathrm B}]\|\to0\), and \((x_n)\in\mathrm{AC}(M,\varphi)\). Every \(a\in\mathrm B\) therefore satisfies \(\|[a,x_n]\|_{\varphi_{\mathrm B}}=\|[a,x_n]\|_\varphi\to0\). So \(\mathrm B\subset\mathrm B(\mathrm B,\varphi_{\mathrm B})\). \(\square\)

**Lemma 2.3.** The predual of \(\mathrm B\) embeds isometrically in \(M_*\) by \(\rho\mapsto\rho\circ E\). In particular \(\mathrm B\) has separable predual when \(M\) does.

**Proof.** \(\|\rho\circ E\|\le\|\rho\|\) since \(E\) is a contraction, and \((\rho\circ E)|_{\mathrm B}=\rho\). \(\square\)

## 3. Type III1 factors

**Theorem 3.1.** Let \(M\) be a type III₁ factor with separable predual and \(\varphi\) a faithful normal state. Then
\[
\mathrm B\cap M_\varphi=\mathbb C1 .
\]
Consequently the centralizer of \(\varphi_{\mathrm B}\) in \(\mathrm B\) is \(\mathbb C1\), and \(\mathrm B\) is a factor. If \(\mathrm B\ne\mathbb C1\), then \(\mathrm B\) is a factor with separable predual, \(\varphi_{\mathrm B}\) is a faithful normal state with trivial centralizer, and \(\mathrm B(\mathrm B,\varphi_{\mathrm B})=\mathrm B\).

**Proof.** Let \(a\in\mathrm B\cap M_\varphi\) and fix a free ultrafilter \(\omega\). The constant sequence \(a\) belongs to \(A_{\varphi,\omega}\), so its class lies in \(M_{\varphi,\omega}\); by Proposition 1.3 it commutes with \(M_{\varphi,\omega}\), so it lies in the centre of \(M_{\varphi,\omega}\), which is \(\mathbb C1\) by Theorem 3.1 of the previous lesson. Thus \(a-c\in I_\omega\) for a scalar \(c\); for a constant sequence this means \(\|a-c\|_\varphi=0\), so \(a=c\).

If \(b\in\mathrm B\) satisfies \([b,\varphi_{\mathrm B}]=0\), then by (2.1), \(\varphi(yb)=\varphi_{\mathrm B}(E(y)b)=\varphi_{\mathrm B}(bE(y))=\varphi(by)\) for all \(y\in M\), so \(b\in M_\varphi\) by (B6), and \(b\) is a scalar. A central element \(z\) of \(\mathrm B\) satisfies \([z,\varphi_{\mathrm B}]=0\), so it is a scalar. The remaining statements are Lemma 2.3 and Proposition 2.2. \(\square\)

Connes' bicentralizer problem asks whether \(\mathrm B(M,\varphi)=\mathbb C1\) for every type III₁ factor with separable predual. Theorem 3.1 reduces it to the question whether a *self-bicentralizing* factor, one with \(\mathrm B(M,\varphi)=M\), must be \(\mathbb C1\). For such a factor the centralizer of \(\varphi\) is trivial, so \(\varphi\) is ergodic for its modular group.

## 4. Exercises

**Exercise 4.1.** Let \(M\) be a finite factor with faithful normal tracial state \(\tau\). Show that \(\mathrm{AC}(M,\tau)=\ell^\infty(M)\) and \(\mathrm B(M,\tau)=\mathbb C1\).

**Exercise 4.2.** Show that \(\mathrm B(M,\varphi)\) is contained in the centre of \(M\) whenever \(M_\varphi'\cap M\) is contained in the centre. (In a factor this gives \(\mathrm B(M,\varphi)=\mathbb C1\) when \(\varphi\) has an irreducible centralizer, \(M_\varphi'\cap M=\mathbb C1\).)

**Exercise 4.3.** Let \(\alpha\) be an automorphism of \(M\). Show that \(\alpha(\mathrm B(M,\varphi))=\mathrm B(M,\varphi\circ\alpha^{-1})\).

**Exercise 4.4.** Show that, in Proposition 1.3(4), the conclusion \(\|u^*au-a\|_\varphi<\varepsilon\) may be replaced by \(\|uau^*-a\|_\varphi<\varepsilon\).

## 5. Solutions

**4.1.** \([x,\tau]=0\) for every \(x\), since \(\tau(yx)=\tau(xy)\); so every bounded sequence is in \(\mathrm{AC}(M,\tau)\). Taking constant sequences, every \(a\in\mathrm B(M,\tau)\) commutes with all of \(M\), so it is central, hence scalar.

**4.2.** By Theorem 2.1, \(\mathrm B(M,\varphi)\subset M_\varphi'\cap M\).

**4.3.** Put \(\psi=\varphi\circ\alpha^{-1}\). For \(x\in M\), \([\alpha(x),\psi]=[x,\varphi]\circ\alpha^{-1}\), so \((x_n)\in\mathrm{AC}(M,\varphi)\) exactly when \((\alpha(x_n))\in\mathrm{AC}(M,\psi)\). Also \(\|\alpha(y)\|_\psi=\|y\|_\varphi\). Hence \(\|[\alpha(a),\alpha(x_n)]\|_\psi=\|[a,x_n]\|_\varphi\), and \(a\in\mathrm B(M,\varphi)\) exactly when \(\alpha(a)\in\mathrm B(M,\psi)\).

**4.4.** Apply Proposition 1.3(4) to \(u^*\): \(\|[u^*,\varphi]\|=\|[u,\varphi]\|\) by Lemma 1.1(a) of the ultraproduct lesson, and \((u^*)^*au^*=uau^*\).

## References

- [HI] C. Houdayer, Y. Isono, Unique prime factorization and bicentralizer problem for a class of type III factors, Advances in Mathematics 305 (2017), 402–455. https://arxiv.org/abs/1503.01388
- [AHHM] H. Ando, U. Haagerup, C. Houdayer, A. Marrakchi, Structure of bicentralizer algebras and inclusions of type III factors, Mathematische Annalen 376 (2020), 1145–1194. https://arxiv.org/abs/1804.05706
