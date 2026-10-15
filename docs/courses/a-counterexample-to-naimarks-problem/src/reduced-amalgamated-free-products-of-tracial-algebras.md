# Reduced amalgamated free products of tracial algebras

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two tracial algebras that share a subalgebra \(D\), with trace-preserving conditional expectations onto \(D\), generate a free product over \(D\): an algebra in which products of elements alternating between the two factors and centered for the expectations have expectation zero. This lesson constructs it on a Hilbert module over \(D\), proves that it carries a faithful trace extending both traces, and constructs the conditional expectation onto one factor. The next lesson, [Reduced HNN adjunctions](reduced-hnn-adjunctions.md), cuts a corner out of such a free product to adjoin a unitary. The construction follows [OpenAI-NA, Lemma 3.2]; the corresponding statements for reduced amalgamated free products are in [Blanchard–Dykema 2001, Lemma 1.1 and Theorem 1.3]. Notation is that of [Pure states, excision and peaking projections](pure-states-excision-and-peaking-projections.md) and [Expectations from peaking projections](expectations-from-peaking-projections.md).

- Hilbert modules from expectations (Section 1).
- The free product module (Section 2).
- The algebra and its trace (Section 3).
- The expectation onto a factor (Section 4).

Throughout, Hilbert modules are right modules with inner products linear in the second variable, as in [Hilbert C\(^*\)-modules](course:hilbert-c-star-modules-and-morita-equivalence/hilbert-c-star-modules); \(\mathcal L(X)\) denotes the C\(^*\)-algebra of adjointable operators on \(X\) (Theorem 2.2 of [Adjointable operators](course:hilbert-c-star-modules-and-morita-equivalence/adjointable-operators)).

**Setting.** \((F,\tau_F)\) and \((G,\tau_G)\) are tracial algebras containing a common unital C\(^*\)-subalgebra \(D\) on which the traces agree, with value \(\tau_D\); and \(E^F_D\colon F\to D\), \(E^G_D\colon G\to D\) are trace-preserving conditional expectations. The letter \(i\) stands for \(F\) or \(G\). An element \(a\in i\) is *centered* if \(E^i_D(a)=0\), and \(i^\circ=\ker E^i_D\).

## 1. Hilbert modules from expectations

On \(i\) put \(\langle x,y\rangle=E^i_D(x^*y)\). It is \(D\)-linear in \(y\), hermitian and positive, and definite: \(\tau_D(E^i_D(x^*x))=\tau_i(x^*x)>0\) for \(x\ne0\). So \(i\), with right multiplication by \(D\), is a pre-Hilbert \(D\)-module; let \(L_i\) be its completion (Theorem 2.3 of the Hilbert module lesson).

**Lemma 1.1.**

1. For \(a\in i\), left multiplication \(x\mapsto ax\) extends to an adjointable operator \(\lambda_i(a)\) of \(L_i\) with adjoint \(\lambda_i(a^*)\), and \(\lambda_i\colon i\to\mathcal L(L_i)\) is an injective unital \(*\)-homomorphism.
2. The map \(x\mapsto E^i_D(x)\) extends to a projection \(P\in\mathcal L(L_i)\) with range \(D\), on which the module norm is the C\(^*\)-norm. So \(L_i=D\oplus L_i^\circ\) with \(L_i^\circ=(1-P)L_i\), the closure of \(i^\circ\). Both summands are invariant under \(\lambda_i(D)\).

*Proof.* (1) Since \(x^*a^*ax\le\|a\|^2x^*x\) and \(E^i_D\) is positive, \(\langle ax,ax\rangle\le\|a\|^2\langle x,x\rangle\), so \(\|ax\|\le\|a\|\,\|x\|\). Also \(\langle ax,y\rangle=E^i_D(x^*a^*y)=\langle x,a^*y\rangle\). Multiplicativity and \(\lambda_i(1)=1\) are clear. As \(\lambda_i(a)1=a\) and \(L_i\) contains \(i\), \(\lambda_i\) is injective.

(2) A conditional expectation has norm one, so Tomiyama's theorem (Theorem 8.5(3) of [The universal enveloping von Neumann algebra of a C\(^*\)-algebra and W\(^*\)-algebras](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras)) gives
\[
\begin{aligned}\langle E^i_D(x),E^i_D(x)\rangle&=E^i_D(x)^*E^i_D(x)\\&\le E^i_D(x^*x).\end{aligned}
\]
So \(x\mapsto E^i_D(x)\) is bounded and extends to \(P\). Both \(\langle E^i_D(x),y\rangle\) and \(\langle x,E^i_D(y)\rangle\) equal \(E^i_D(x)^*E^i_D(y)\), so \(P\) is self-adjoint, and \(P^2=P\). On \(D\), \(\langle d,d\rangle=d^*d\), so the module norm is the C\(^*\)-norm, \(D\) is complete and closed in \(L_i\), and \(PL_i=D\). The range of \(1-P\) is the closure of \((1-P)(i)=i^\circ\). Finally \(E^i_D(dx)=dE^i_D(x)\), so \(\lambda_i(d)\) commutes with \(P\). \(\square\)

## 2. The free product module

A *word* is a finite sequence \(\iota=(i_1,\ldots,i_m)\), \(m\ge1\), of letters from \(\{F,G\}\) with \(i_t\ne i_{t+1}\). For a word put
\[
L_\iota=L^\circ_{i_1}\otimes_DL^\circ_{i_2}\otimes_D\cdots\otimes_DL^\circ_{i_m},
\]
the interior tensor product formed with the left actions \(\lambda_{i_t}|_D\) (Theorems 1.2 and 3.1 of [Tensor products and C\(^*\)-correspondences](course:hilbert-c-star-modules-and-morita-equivalence/tensor-products-and-c-star-correspondences)). Let
\[
K=D\oplus\bigoplus_\iota L_\iota ,
\]
the completion of the algebraic direct sum for the sum of the inner products (Theorem 2.3 of the Hilbert module lesson). The *vacuum vector* is \(\Omega=1\in D\). The algebra \(D\) acts on \(K\) on the left: by multiplication on the summand \(D\), and on \(L_\iota\) through its first tensor factor (Theorem 2.1 of the tensor lesson). For \(i\in\{F,G\}\) let \(K^{(i)}\) be the closed span of \(D\) and the \(L_\iota\) with \(i_1\ne i\), a submodule invariant under the left action of \(D\).

Interior tensor products distribute over orthogonal direct sums, finite or countable: on finite sums of elementary tensors the inner products (1.2) of the tensor lesson add over the summands, and the images are dense. Together with the units \(D\otimes_DY\cong Y\) for a unital left action (Proposition 3.2 there), this gives the following.

**Lemma 2.1.** There is a unitary \(V_i\colon L_i\otimes_DK^{(i)}\to K\) of Hilbert \(D\)-modules with
\[
\begin{gathered}
V_i(d\otimes\eta)=d\eta\quad(d\in D,\ \eta\in K^{(i)}),\\
V_i(x\otimes d)=xd\in L_{(i)},\\
V_i(x\otimes\eta)=x\otimes\eta\in L_{(i,\iota)}
\end{gathered}
\]
for \(x\in L_i^\circ\), \(d\in D\), and \(\eta\in L_\iota\) with \(\iota\) not starting with \(i\).

*Proof.* By Lemma 1.1(2) and distributivity,
\[
\begin{aligned}&L_i\otimes_DK^{(i)}\\&\quad\cong\bigl(D\otimes_DK^{(i)}\bigr)\oplus\bigl(L_i^\circ\otimes_DD\bigr)\\&\qquad\oplus\bigoplus_{i_1\ne i}\bigl(L_i^\circ\otimes_DL_\iota\bigr).\end{aligned}
\]
The first summand is \(K^{(i)}\), the second is \(L_i^\circ=L_{(i)}\), and the remaining ones are the \(L_{(i,\iota)}\), which are exactly the summands of \(K\) indexed by words starting with \(i\) and having length at least two. Together these summands make up \(K\). \(\square\)

For \(a\in i\) put
\[
\pi_i(a)=V_i\bigl(\lambda_i(a)\otimes1\bigr)V_i^*\in\mathcal L(K),
\]
an adjointable operator by Theorem 2.1 of the tensor lesson.

**Lemma 2.2.**

1. \(\pi_F\) and \(\pi_G\) are injective unital \(*\)-homomorphisms. On \(D\) both equal the left action of \(D\) on \(K\).
2. For \(a\in i\), \(\pi_i(a)\Omega\) is the vector \(E^i_D(a)+\bigl(a-E^i_D(a)\bigr)\) of \(D\oplus L_{(i)}\).
3. For \(a\in i^\circ\) and \(\eta\in K^{(i)}\), \(\pi_i(a)\eta=V_i(a\otimes\eta)\) lies in the closed span of the \(L_\iota\) with \(\iota\) starting with \(i\). For \(\eta\in L_\iota\) with \(i_1\ne i\), \(\pi_i(a)\eta=a\otimes\eta\in L_{(i,\iota)}\); for \(d\in D\), \(\pi_i(a)d=ad\in L_{(i)}\).

*Proof.* For \(\eta\in K^{(i)}\), \(V_i^*\eta=1\otimes\eta\). So \(\pi_i(a)\eta=V_i(a\otimes\eta)\), and with \(a=E^i_D(a)+(a-E^i_D(a))\) the formulas of Lemma 2.1 give (2) and (3). The map \(a\mapsto\lambda_i(a)\otimes1\) is a unital \(*\)-homomorphism (Theorem 2.1 of the tensor lesson), so \(\pi_i\) is one. By (2), \(\pi_i(a)\Omega\ne0\) for \(a\ne0\). For \(d\in D\), \(\pi_i(d)\) acts on \(V_i(d'\otimes\eta)=d'\eta\) as \(dd'\eta\), and on \(V_i(x\otimes\eta)\) as \(dx\otimes\eta\), with \(dx\in L_i^\circ\) by Lemma 1.1(2): this is the left action of \(d\) on \(K\). \(\square\)

## 3. The algebra and its trace

Let \(Z\) be the C\(^*\)-subalgebra of \(\mathcal L(K)\) generated by \(\pi_F(F)\cup\pi_G(G)\). We identify \(F\) and \(G\) with their images; they intersect in \(D\) as required. A *centered alternating product* of type \(\iota=(i_1,\ldots,i_m)\) is a product \(a_1a_2\cdots a_m\) with \(a_t\in i_t^\circ\).

**Lemma 3.1.**

1. A centered alternating product of type \(\iota\) maps \(\Omega\) to \(a_1\otimes a_2\otimes\cdots\otimes a_m\in L_\iota\).
2. \(D\) and the centered alternating products span a dense \(*\)-subalgebra \(S\) of \(Z\).

*Proof.* (1) By Lemma 2.2(3), \(a_m\Omega=a_m\in L_{(i_m)}\), and if \(\eta\in L_{(i_{t+1},\ldots,i_m)}\), a word not starting with \(i_t\), then \(a_t\eta=a_t\otimes\eta\).

(2) The adjoint of a centered alternating product is one, since \(E^i_D(a^*)=E^i_D(a)^*\). Multiplying by elements of \(D\) keeps the product centered alternating, as \(E^i_D(da)=dE^i_D(a)\). We show by induction on \(m+n\) that the product of centered alternating products \(w=a_1\cdots a_m\) and \(w'=b_1\cdots b_n\) lies in \(S\). If the letters of \(a_m\) and \(b_1\) differ, \(ww'\) is centered alternating. Otherwise \(c=a_mb_1\) lies in one factor; write \(c=E(c)+c^\circ\) with \(E(c)\in D\) and \(c^\circ\) centered. Then \(a_1\cdots a_{m-1}c^\circ b_2\cdots b_n\) is centered alternating, and in the remaining term \(a_1\cdots a_{m-1}\cdot E(c)b_2\cdots b_n\) the second factor is centered alternating of length \(n-1\) (or lies in \(D\)), so the induction applies. Hence \(S\) is a \(*\)-algebra. It contains \(F\) and \(G\), because \(a=E(a)+(a-E(a))\), so it is dense in \(Z\). \(\square\)

For \(z\in Z\) put \(E_D(z)=\langle\Omega,z\Omega\rangle\in D\), the vacuum component of \(z\Omega\).

**Proposition 3.2.** \(E_D\) is a conditional expectation of \(Z\) onto \(D\). It extends \(E^F_D\) and \(E^G_D\) and vanishes on every centered alternating product. The functional \(\tau_Z=\tau_D\circ E_D\) is a faithful tracial state of \(Z\) extending \(\tau_F\) and \(\tau_G\).

*Proof.* *Expectation.* \(E_D(1)=1\) and \(E_D(d)=\langle1,d\rangle=d\). For \(d,d'\in D\), \(d'\Omega=\Omega d'\), so
\[
E_D(dzd')=\langle\Omega d^*,z\Omega d'\rangle=d\,E_D(z)\,d' .
\]
For \(z_1,\ldots,z_n\in Z\) and \(d_1,\ldots,d_n\in D\),
\[
\begin{aligned}&\sum_{j,k}d_j^*E_D(z_j^*z_k)d_k\\&\quad=\Bigl\langle\sum_jz_j\Omega d_j,\sum_kz_k\Omega d_k\Bigr\rangle\ge0,\end{aligned}
\]
so \(E_D\) is completely positive (Proposition 3.2(1) of [Completely positive maps](course:foundations-of-von-neumann-algebras/completely-positive-maps)). By Lemma 2.2(2), \(E_D(a)=E^i_D(a)\) for \(a\in i\), and by Lemma 3.1(1), \(E_D\) vanishes on centered alternating products.

*Trace.* We show \(\tau_Z(aw)=\tau_Z(wa)\) for \(a\in F\cup G\) and \(w\) in \(S\). For \(a=d\in D\), \(\tau_D(dE_D(w))=\tau_D(E_D(w)d)\) because \(\tau_D\) is tracial. So let \(a\in i^\circ\). If \(w\in D\), both sides vanish. If \(w=b\) is a single centered letter, both sides vanish when \(b\) lies in the other factor, and \(\tau_Z(ab)=\tau_i(ab)=\tau_i(ba)=\tau_Z(ba)\) when \(b\in i\). If \(w=b_1\cdots b_n\) with \(n\ge2\) and \(b_1\notin i\), then \(aw\) is centered alternating, and if \(b_1\in i\), then \(aw=E(ab_1)b_2\cdots b_n+(ab_1)^\circ b_2\cdots b_n\) is a sum of two centered alternating products of positive length. In all cases \(\tau_Z(aw)=0\); by the same argument at the right end, \(\tau_Z(wa)=0\). Products of elements of \(F\cup G\) span \(S\), and moving one letter at a time from the front to the back gives \(\tau_Z(xw)=\tau_Z(wx)\) for \(x,w\in S\); by continuity \(\tau_Z\) is tracial. It extends \(\tau_i\), since \(\tau_D\circ E^i_D=\tau_i\).

*Faithfulness.* Let \(\tau_Z(z^*z)=0\). For \(t\in Z\),
\[
\begin{aligned}0\le\tau_Z(t^*z^*zt)&=\tau_Z(ztt^*z^*)\\&\le\|t\|^2\tau_Z(zz^*)\\&=\|t\|^2\tau_Z(z^*z)=0 .\end{aligned}
\]
As \(\tau_D\) is faithful, \(E_D((zt)^*(zt))=\langle zt\Omega,zt\Omega\rangle=0\), so \(zt\Omega=0\). By Lemma 3.1(1), \(Z\Omega\) contains the elementary tensors \(a_1\otimes\cdots\otimes a_m\) with \(a_t\in i_t^\circ\), which span a dense subspace of each \(L_\iota\) because \(i_t^\circ\) is dense in \(L^\circ_{i_t}\); it also contains \(D\). So \(Z\Omega\) is dense in \(K\), \(z\) vanishes on a dense subspace, and \(z=0\). \(\square\)

## 4. The expectation onto a factor

Let \(P_F\) be the projection of \(K\) onto \(D\oplus L_{(F)}=V_F(L_F\otimes\Omega)\), and \(P_G\) the projection onto the closed span of the \(L_\iota\) with \(\iota\) starting with \(G\). A *core* is a centered alternating product \(w=b_1a_1b_2\cdots a_{m-1}b_m\), \(m\ge1\), that starts and ends with a letter from \(G\): \(b_t\in G^\circ\), \(a_t\in F^\circ\).

**Lemma 4.1.**

1. \(P_F\) commutes with \(F\), and \(P_FwP_F=0\) for every core \(w\).
2. For every core \(w\), \((1-P_G)w(1-P_G)=0\); hence \(w=P_Gw+(1-P_G)wP_G\).
3. For \(d\in F\), \(\|dP_G\|\le\|E^F_D(d^*d)\|^{1/2}\).

*Proof.* (1) \(\lambda_F(a)\otimes1\) maps \(L_F\otimes\Omega\) into itself and preserves its orthogonal complement \(L_F\otimes(K^{(F)}\ominus D)\), so \(\pi_F(a)\) commutes with \(P_F\). The range of \(1-P_G\) is \(D\) together with the words starting with \(F\), which lies in \(K^{(G)}\). By Lemma 2.2(3), \(b_m\) maps \(K^{(G)}\) into the words starting with \(G\), which lie in \(K^{(F)}\); then \(a_{m-1}\) maps these into the words starting with \(F\), and so on; finally \(b_1\) maps into the words starting with \(G\). So \(w(1-P_G)K\subseteq P_GK\). Since \(P_FK\subseteq(1-P_G)K\) is orthogonal to \(P_GK\), \(P_FwP_F=0\).

(2) This is the inclusion \(w(1-P_G)K\subseteq P_GK\) just proved.

(3) \(P_GK\subseteq K^{(F)}\), and for \(\eta\in K^{(F)}\), \(d\eta=V_F(d\otimes\eta)\). By (1.2) of the tensor lesson,
\[
\begin{aligned}\langle d\otimes\eta,d\otimes\eta\rangle&=\langle\eta,E^F_D(d^*d)\eta\rangle\\&\le\|E^F_D(d^*d)\|\,\langle\eta,\eta\rangle,\end{aligned}
\]
since \(c\le\|c\|\) for \(c\ge0\) in \(D\) and the left action of \(D\) is a \(*\)-homomorphism into \(\mathcal L(K)\). \(\square\)

**Proposition 4.2.** There is a faithful trace-preserving conditional expectation \(E_F\colon Z\to F\), determined by \(P_FzP_F=E_F(z)P_F\). It vanishes on every product \(a_0wa_m\) with \(a_0,a_m\in F\) and \(w\) a core, and \(E_D=E^F_D\circ E_F\). The space \(F\) together with these products spans a dense subspace of \(Z\).

*Proof.* A centered alternating product either lies in \(F\) or contains a letter from \(G\); in the second case it is \(a_0wa_m\), where \(w\) runs from the first to the last letter from \(G\), and \(a_0,a_m\) are the remaining \(F\)-letters or \(1\). By Lemma 3.1(2), \(F\) and the products \(a_0wa_m\) span a dense subspace. For such products, Lemma 4.1(1) gives \(P_Fa_0wa_mP_F=a_0P_FwP_Fa_m=0\). So \(P_FzP_F\) lies in \(\Theta(F)\) for \(z\) in this span, where \(\Theta(f)=fP_F\) restricted to \(P_FK\). The map \(\Theta\) is an injective \(*\)-homomorphism (it sends \(f\) to an operator mapping \(\Omega\) to \(f\in L_F\)), so it is isometric with closed range. As \(z\mapsto P_FzP_F\) is continuous, \(P_FzP_F\in\Theta(F)\) for every \(z\in Z\), and \(E_F(z)=\Theta^{-1}(P_FzP_F)\) is well defined. It is unital, completely positive, fixes \(F\), and is \(F\)-bimodular because \(P_F\) commutes with \(F\). Since \(\Omega\in P_FK\), \(E_D(z)=\langle\Omega,P_FzP_F\Omega\rangle=E^F_D(E_F(z))\), and \(\tau_F\circ E_F=\tau_D\circ E_D=\tau_Z\). Faithfulness follows from that of \(\tau_Z\). \(\square\)

We call \(Z\) the *reduced amalgamated free product* of \(F\) and \(G\) over \(D\), and write \(Z=F*_DG\).

## 5. Exercises

**5.1.** Show that \(E_F(g)=E^G_D(g)\) for \(g\in G\).

**5.2.** For centered \(a_1,a_2\in F^\circ\) and \(b_1,b_2\in G^\circ\), compute \(\tau_Z(a_1b_1a_2b_2)\) and \(\tau_Z(a_1b_1b_2a_2)\) in terms of \(\tau_F\), \(\tau_G\) and the expectations.

**5.3.** Let \(D=\mathbb C\), \(F=G=\mathbb C^2\) with the uniform traces, and \(u=(1,-1)\in F\), \(v=(1,-1)\in G\). Show that \(\tau_Z((uv)^n)=0\) for every integer \(n\ne0\).

**5.4.** Show that \(K=D\) and \(Z=D\) when \(F=G=D\).

**5.5.** Show that the vacuum vector \(\Omega\) is cyclic for \(Z\): the closed span of \(Z\Omega\) is \(K\).

## 6. Solutions

**5.1.** Write \(g=E^G_D(g)+g^\circ\). Here \(g^\circ\) is a core of length one, so \(E_F(g^\circ)=0\) by Proposition 4.2, and \(E_F\) fixes \(D\subset F\).

**5.2.** \(a_1b_1a_2b_2\) is centered alternating, so its trace is \(0\). In \(a_1(b_1b_2)a_2\), write \(b_1b_2=E^G_D(b_1b_2)+(b_1b_2)^\circ\). The second part gives the centered alternating product \(a_1(b_1b_2)^\circ a_2\) of trace \(0\). The first part gives \(a_1E^G_D(b_1b_2)a_2\in F\), so
\[
\tau_Z(a_1b_1b_2a_2)=\tau_F\bigl(a_1E^G_D(b_1b_2)a_2\bigr).
\]

**5.3.** Here \(E^F_{\mathbb C}=\tau_F\), and \(\tau_F(u)=0\), so \(u\) and \(v\) are centered. For \(n\ge1\), \((uv)^n=uvuv\cdots uv\) is a centered alternating product, so its trace is \(0\). For \(n\le-1\), \((uv)^n=(v^{-1}u^{-1})^{|n|}=(vu)^{|n|}\), again centered alternating.

**5.4.** Then \(i^\circ=0\) and \(L_i^\circ=0\), so every \(L_\iota\) is zero and \(K=D\). Both representations are left multiplication on \(D\), so \(Z=D\).

**5.5.** This was shown in the proof of Proposition 3.2: \(Z\Omega\) contains \(D\) and the elementary tensors \(a_1\otimes\cdots\otimes a_m\) with centered entries, which span a dense subspace of every \(L_\iota\).

## References

- [OpenAI-NA] OpenAI, *A counterexample to Naimark's problem in ZFC*, OpenAI Math Release preprint, 24 September 2026, Section 3.2 (Lemma 3.2). https://github.com/openai/math/tree/main/preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026
- [Blanchard–Dykema 2001] E. Blanchard, K. Dykema, *Embeddings of reduced free products of operator algebras*, Pacific J. Math. 199 (2001), 1–19. https://arxiv.org/abs/math/9911012
