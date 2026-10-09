# From inner derivations to similarity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Kirchberg proved that a C\*-algebra has the similarity property exactly when every derivation of it into the bounded operators, relative to any representation, is implemented [Kirchberg]. His argument needs much less than all derivations: a uniform bound for the completely bounded norms of the inner derivations \(x\mapsto tx-xt\) with \(t\) self-adjoint controls every conjugation \(x\mapsto e^{-t}xe^{t}\). Two analytic facts drive this. A three-lines estimate bounds the derivation by the logarithm of the norm of the conjugation, and an integral formula bounds the logarithm of the completely bounded norm of the conjugation by the completely bounded norm of the derivation. Paulsen's theorem brings an arbitrary similarity into this exponential form, and the finite cyclic set theorem of the previous lesson passes from conjugations to arbitrary bounded homomorphisms. As Pisier observed [Pisier-degree, Remark 4.7], the argument gives a polynomial bound: if the inner derivations of every representation satisfy \(\|\delta\|_{\rm cb}\le k\|\delta\|\), then every bounded unital homomorphism satisfies \(\|\pi\|_{\rm cb}\le\|\pi\|^{2k}\).

We use: Lemma 1.1, Lemma 2.2 and Theorem 3.1 of [Completely bounded homomorphisms and similarity](completely-bounded-homomorphisms-and-similarity.md); Theorem 3.1 of [Row, column and cyclic estimates](row-column-and-cyclic-estimates.md); the scalar three-lines bound (9) in Section 4 of [The sharp noncommutative bilinear inequality](course:OA-APPROX/sharp-noncommutative-bilinear-inequality#4-improving-the-best-constant); from [C\*-algebras, continuous functional calculus, automatic continuity and positive cones](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-10), Proposition 7.3 (a contraction is \(\frac12(u_1+u_2)+\frac i2(u_3+u_4)\) with unitaries \(u_j\)), [Corollary 15.4](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-26) and [Proposition 17.1](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-29) (norm-preserving lifts along surjective \(*\)-homomorphisms).

## 1. Conjugations and inner derivations

Throughout this section and the next three, \(B\subseteq B(H)\) is a C\*-algebra with \(1_H\in B\). For a self-adjoint \(t\in B(H)\) define \(\delta_t,r_t:B\to B(H)\) by
\[
\delta_t(x)=tx-xt,\qquad r_t(x)=e^{-t}xe^{t}.
\tag{1.1}
\]
The map \(r_t\) is a unital homomorphism, \((\delta_t)_n(X)=[t^{(n)},X]\) and \((r_t)_n(X)=e^{-t^{(n)}}Xe^{t^{(n)}}\) for \(X\in M_n(B)\); hence \(\|r_t\|_{\rm cb}\le\|e^{-t}\|\|e^{t}\|\), and \(\|r_t\|\ge1\) because \(r_t(1)=1\). The inequality can be strict (Exercise 6.1). The first lemma brings every similarity of the inclusion into a form where it is an equality.

**Lemma 1.1** (exponential form of a similarity). Let \(T\in B(H)\) be invertible and \(r(x)=T^{-1}xT\) for \(x\in B\). There are a self-adjoint \(t\in B(H)\) and a unitary \(U\in B(H)\) with
\[
r(x)=U^*r_t(x)U\quad(x\in B),\qquad \|r\|_{\rm cb}=\|e^{t}\|\,\|e^{-t}\| .
\]
In particular \(\|r_t\|=\|r\|\) and \(\|r_t\|_{\rm cb}=\|r\|_{\rm cb}\).

**Proof.** The map \(r\) is a completely bounded unital homomorphism (Lemma 1.1(3) of the first lesson, with the inclusion representation). Theorem 3.1 of the first lesson gives a positive invertible \(S\) with \(\|S\|\|S^{-1}\|=\|r\|_{\rm cb}\) such that \(\rho=Sr(\cdot)S^{-1}\) is a representation of \(B\) on \(H\). The operator \(V=ST^{-1}\) satisfies \(\rho(x)V=Vx\) for \(x\in B\). By Lemma 2.2 of the first lesson, \(W=V|V|^{-1}\) is unitary and \(\rho(x)=WxW^*\). Hence \(r(x)=S^{-1}WxW^*S=R^{-1}xR\) with \(R=W^*S\), and \(\|R\|\|R^{-1}\|=\|S\|\|S^{-1}\|=\|r\|_{\rm cb}\). Write \(R=|R^*|U\) with \(|R^*|=(RR^*)^{1/2}\), positive and invertible, and \(U=|R^*|^{-1}R\); then \(UU^*=|R^*|^{-1}RR^*|R^*|^{-1}=1\) and \(U\) is invertible, so \(U\) is unitary. Put \(t=\log|R^*|\). Then \(R=e^{t}U\), \(R^{-1}=U^*e^{-t}\), \(r(x)=U^*e^{-t}xe^{t}U\), and \(\|r\|_{\rm cb}=\|R\|\|R^{-1}\|=\|e^{t}\|\|e^{-t}\|\). The amplifications of \(r\) and \(r_t\) differ by conjugation with the unitaries \(U^{(n)}\), so their norms agree. \(\square\)

## 2. A three-lines bound for the derivation

**Lemma 2.1.** Let \(t\in B(H)\) be self-adjoint and \(a\in B(H)\) unitary, and put \(c_+=\|e^{-t}ae^{t}\|\) and \(c_-=\|e^{-t}a^*e^{t}\|\). Then
\[
\|ta-at\|\le\log\max(c_+,c_-).
\]

**Proof.** The function \(f(z)=e^{-zt}ae^{zt}\) is entire with values in \(B(H)\), and bounded by \(e^{2\|t\|}\) on the strip \(0\le\operatorname{Re}z\le1\). For real \(y\), \(f(iy)=e^{-iyt}ae^{iyt}\) is unitary, and \(f(1+iy)=e^{-iyt}(e^{-t}ae^{t})e^{iyt}\) has norm \(c_+\), which is positive. For a functional \(\phi\) on \(B(H)\) of norm at most \(1\), the scalar function \(\phi\circ f\) is bounded and holomorphic on the strip and continuous on its closure, with \(|\phi\circ f|\le1\) on \(\operatorname{Re}z=0\) and \(\le c_+\) on \(\operatorname{Re}z=1\). The three-lines bound (9) of the sharp bilinear inequality lesson gives \(|\phi(f(\theta))|\le c_+^{\theta}\) for \(0\le\theta\le1\), and by the Hahn–Banach theorem \(\|f(\theta)\|\le c_+^{\theta}\).

The power series of the exponentials give \(f(\theta)=a+\theta(at-ta)+R(\theta)\) with \(\|R(\theta)\|\le C\theta^2\) for \(0\le\theta\le1\), where \(C\) depends only on \(\|t\|\). The operator \(Y=(at-ta)a^*=ata^*-t\) is self-adjoint, and \(1+\theta Y=(a+\theta(at-ta))a^*\). For a unit vector \(\xi\),
\[
1+\theta\langle Y\xi,\xi\rangle\le\|a+\theta(at-ta)\|\le c_+^{\theta}+C\theta^2,
\]
so \(\langle Y\xi,\xi\rangle\le(c_+^{\theta}-1)/\theta+C\theta\), and \(\theta\downarrow0\) gives \(\langle Y\xi,\xi\rangle\le\log c_+\). The same argument for the unitary \(a^*\) gives \(\langle Y'\eta,\eta\rangle\le\log c_-\) for \(Y'=a^*ta-t\) and every unit vector \(\eta\). Since \(-Y=t-ata^*=aY'a^*\), we get \(-\langle Y\xi,\xi\rangle=\langle Y'a^*\xi,a^*\xi\rangle\le\log c_-\). So the spectrum of the self-adjoint \(Y\) lies in \([-\log c_-,\log c_+]\), and \(\|ta-at\|=\|Ya\|=\|Y\|\le\log\max(c_+,c_-)\). \(\square\)

**Corollary 2.2.** For every self-adjoint \(t\in B(H)\), \(\|\delta_t\|\le2\log\|r_t\|\).

**Proof.** For a unitary \(a\in B\), both \(a\) and \(a^*\) lie in the unit ball of \(B\), so \(c_\pm\le\|r_t\|\) and Lemma 2.1 gives \(\|\delta_t(a)\|\le\log\|r_t\|\). A contraction \(x\in B\) is \(\frac12(u_1+u_2)+\frac i2(u_3+u_4)\) with unitaries \(u_j\in B\) (Proposition 7.3 of the C\*-algebra lesson), so \(\|\delta_t(x)\|\le2\log\|r_t\|\). \(\square\)

## 3. An integral formula for the conjugation

**Lemma 3.1.** Let \(t\in B(H)\) be self-adjoint with \(\|r_t\|_{\rm cb}=\|e^{t}\|\|e^{-t}\|\). Then \(\log\|r_t\|_{\rm cb}\le\|\delta_t\|_{\rm cb}\).

**Proof.** Put \(c=\|e^{t}\|\|e^{-t}\|\ge\|e^{t}e^{-t}\|=1\). If \(c=1\) there is nothing to prove. Let \(M=\max\sigma(t)\) and \(m=\min\sigma(t)\). For \(\tau\ge0\) the spectral theorem gives \(\|e^{\tau t}\|=e^{\tau M}\) and \(\|e^{-\tau t}\|=e^{-\tau m}\), so
\[
\|e^{-\tau t}\|\,\|e^{\tau t}\|=e^{\tau(M-m)}=c^{\tau}.
\]
Fix \(n\) and \(X\in M_n(B)\), and write \(t_n=t^{(n)}\). The function \(\tau\mapsto e^{-\tau t_n}Xe^{\tau t_n}\) is norm differentiable with derivative \(-e^{-\tau t_n}[t_n,X]e^{\tau t_n}\), so
\[
(r_t)_n(X)-X=-\int_0^1e^{-\tau t_n}(\delta_t)_n(X)\,e^{\tau t_n}\,d\tau,\qquad
\|(r_t)_n(X)\|\le\|X\|+\|(\delta_t)_n(X)\|\int_0^1c^{\tau}d\tau .
\]
Since \(\int_0^1c^{\tau}d\tau=(c-1)/\log c\), taking the supremum over \(n\) and the unit ball of \(M_n(B)\) gives \(c\le1+\|\delta_t\|_{\rm cb}(c-1)/\log c\). Divide by \((c-1)/\log c>0\). \(\square\)

## 4. Kirchberg's lemma

**Theorem 4.1** (Kirchberg). Let \(k\ge0\), and suppose that \(\|\delta_t\|_{\rm cb}\le k\|\delta_t\|\) for every self-adjoint \(t\in B(H)\). Then every map \(r(x)=T^{-1}xT\), \(x\in B\), with \(T\in B(H)\) invertible, satisfies
\[
\|r\|_{\rm cb}\le\|r\|^{2k}.
\]

**Proof.** Lemma 1.1 gives a self-adjoint \(t\) with \(\|r_t\|=\|r\|\) and \(\|r_t\|_{\rm cb}=\|r\|_{\rm cb}=\|e^{t}\|\|e^{-t}\|\). By Lemma 3.1, the hypothesis and Corollary 2.2,
\[
\log\|r\|_{\rm cb}\le\|\delta_t\|_{\rm cb}\le k\|\delta_t\|\le2k\log\|r\| .\qquad\square
\]

Kirchberg's original statement has the weaker bound \(\exp(k(1+\|r\|))\), obtained from the Cauchy estimate for \(f'(0)\) in place of the three-lines bound [Kirchberg, Proposition 1].

## 5. The similarity criterion

**Theorem 5.1.** Let \(A\) be a unital C\*-algebra and \(k\ge0\). Suppose that for every representation \(\rho:A\to B(K)\) and every self-adjoint \(t\in B(K)\) the derivation \(\Delta_t(a)=t\rho(a)-\rho(a)t\) satisfies \(\|\Delta_t\|_{\rm cb}\le k\|\Delta_t\|\). Then every bounded unital homomorphism \(\pi:A\to B(H)\) satisfies
\[
\|\pi\|_{\rm cb}\le\|\pi\|^{2k},
\]
and there is a positive invertible \(S\in B(H)\) with \(\|S\|\|S^{-1}\|\le\|\pi\|^{2k}\) such that \(S\pi(\cdot)S^{-1}\) is a \(*\)-homomorphism.

**Proof.** We may assume \(H\ne0\). Let \(F\subseteq H\) be finite and \(H_F\) the closed linear span of \(\pi(A)F\). It is invariant under \(\pi(A)\) and contains \(F\), and \(\pi_F(a)=\pi(a)|_{H_F}\) is a bounded unital homomorphism with \(\|\pi_F\|\le\|\pi\|\) and the cyclic set \(F\). By Theorem 3.1 of the previous lesson \(\pi_F\) is completely bounded, so by Theorem 3.1 of the first lesson there is an invertible \(S_F\in B(H_F)\) such that \(\rho_F=S_F\pi_F(\cdot)S_F^{-1}\) is a representation of \(A\) on \(H_F\).

Let \(B=\rho_F(A)\subseteq B(H_F)\), a C\*-algebra containing \(1\) (Corollary 15.4 of the C\*-algebra lesson). For every \(n\), \((\rho_F)_n\) maps \(M_n(A)\) onto \(M_n(B)\) and, by Proposition 17.1 of the C\*-algebra lesson, maps the unit ball onto the unit ball. Consequently, for a linear map \(u\) on \(B\), the maps \(u\) and \(u\circ\rho_F\) have the same norms and the same completely bounded norms. Applied to \(\delta_t\) on \(B\), with \(\delta_t\circ\rho_F=\Delta_t\) for \(\rho=\rho_F\), this shows that \(B\) satisfies the hypothesis of Theorem 4.1. Applied to \(r(y)=S_F^{-1}yS_F\), \(y\in B\), with \(r\circ\rho_F=\pi_F\), it shows \(\|r\|=\|\pi_F\|\) and \(\|r\|_{\rm cb}=\|\pi_F\|_{\rm cb}\). Theorem 4.1 gives
\[
\|\pi_F\|_{\rm cb}\le\|\pi_F\|^{2k}\le\|\pi\|^{2k},
\]
using \(1\le\|\pi_F\|\le\|\pi\|\).

Now let \(X\in M_n(A)\) and \(\eta=(\eta_1,\dots,\eta_n)\in H^n\). With \(F=\{\eta_1,\dots,\eta_n\}\), the vector \(\eta\) lies in \(H_F^n\) and \(\pi_n(X)\eta=(\pi_F)_n(X)\eta\), so \(\|\pi_n(X)\eta\|\le\|\pi\|^{2k}\|X\|\|\eta\|\). Hence \(\|\pi\|_{\rm cb}\le\|\pi\|^{2k}\), and Theorem 3.1 of the first lesson gives \(S\). \(\square\)

The hypothesis concerns inner derivations only, and only through a single constant \(k\). The converse direction is elementary: if every bounded unital homomorphism of \(A\) is similar to a \(*\)-homomorphism, then every bounded derivation of \(A\) relative to any representation is implemented (Exercise 6.2). Together with Theorem 5.1 and a direct-sum argument for the uniform constant, this is Kirchberg's equivalence of the similarity and derivation problems [Kirchberg], [Ozawa, Theorem 1.1]. The remaining lessons prove the hypothesis of Theorem 5.1 for every unital C\*-algebra, with one absolute constant.

## 6. Exercises

**Exercise 6.1.** Let \(B=\mathbb C1_H\) and \(t\) self-adjoint and not scalar. Show that \(r_t\) is the identity map of \(B\), so \(\|r_t\|_{\rm cb}=1<\|e^{t}\|\|e^{-t}\|\). Which \(t\) does Lemma 1.1 produce for \(r=r_t\) here?

**Exercise 6.2.** Suppose every bounded unital homomorphism of \(A\) into the bounded operators on a Hilbert space is similar to a \(*\)-homomorphism. Let \(\sigma:A\to B(K)\) be a representation and \(\Delta\) a bounded \(\sigma\)-derivation. Show that \(\Delta\) is implemented by an operator on \(K\).

**Exercise 6.3.** On \(H=\mathbb C^2\) let \(t=\operatorname{diag}(s,-s)\) with \(s>0\) and let \(a\) be the unitary exchanging the basis vectors. Compute \(e^{-t}ae^{t}\), \(e^{-t}a^*e^{t}\) and \(ta-at\), and show that Lemma 2.1 holds with equality.

**Exercise 6.4.** Let \(B=M_2(\mathbb C)\) act on \(\mathbb C^2\) and \(t=\operatorname{diag}(s,-s)\) with \(s>0\). Show that \(\|r_t\|=\|r_t\|_{\rm cb}=e^{2s}\), \(\|\delta_t\|=\|\delta_t\|_{\rm cb}=2s\), and that Lemma 3.1 holds with equality.

## 7. Solutions

**Solution 6.1.** \(e^{-t}\lambda e^{t}=\lambda\) for scalars, so \(r_t=\mathrm{id}_B\) and \(\|r_t\|_{\rm cb}=1\). If \(t\) is not scalar, \(\max\sigma(t)>\min\sigma(t)\), so \(\|e^{t}\|\|e^{-t}\|=e^{\max\sigma(t)-\min\sigma(t)}>1\). For \(r=r_t=\mathrm{id}_B\), written as \(r(x)=T^{-1}xT\) with \(T=e^{t}\), Theorem 3.1 of the first lesson gives a positive scalar \(S\), say \(S=1\). In the proof of Lemma 1.1, \(V=e^{-t}\) is positive, so \(W=1\), \(R=1\), and the self-adjoint operator produced is \(0\).

**Solution 6.2.** Lemma 4.2 of the first lesson with \(\lambda=\sigma\) and \(c=1\) gives a bounded unital homomorphism \(\Phi_1\) of \(A\) on \(K\oplus K\). By hypothesis it is similar to a \(*\)-homomorphism, so it is completely bounded (Theorem 3.1 of the first lesson). The upper right block of \((\Phi_1)_n(x)\) is \(\Delta_n(x)\), so \(\|\Delta\|_{\rm cb}\le\|\Phi_1\|_{\rm cb}<\infty\), and Corollary 4.4 of the first lesson implements \(\Delta\).

**Solution 6.3.** Conjugation by \(e^{-t}\) multiplies the \((i,j)\) entry by \(e^{-t_i+t_j}\), with \((t_1,t_2)=(s,-s)\). So \(e^{-t}ae^{t}=\left(\begin{smallmatrix}0&e^{-2s}\\e^{2s}&0\end{smallmatrix}\right)\) and, as \(a^*=a\), the same for \(a^*\); both have norm \(e^{2s}\). Next \(ta-at=\left(\begin{smallmatrix}0&2s\\-2s&0\end{smallmatrix}\right)\), of norm \(2s=\log e^{2s}\).

**Solution 6.4.** As in 6.3, \(r_t\) multiplies the off-diagonal entries by \(e^{-2s}\) and \(e^{2s}\) and fixes the diagonal ones. So \(\|r_t\|\ge\|r_t(e_{21})\|=e^{2s}\), while \(\|r_t\|_{\rm cb}\le\|e^{-t}\|\|e^{t}\|=e^{s}e^{s}=e^{2s}\); hence both equal \(e^{2s}\). The derivation \(\delta_t\) kills the diagonal entries and multiplies \(x_{12}\) by \(2s\), \(x_{21}\) by \(-2s\), so \(\|\delta_t(x)\|=2s\max(|x_{12}|,|x_{21}|)\le2s\|x\|\), with equality at \(x=e_{12}\). By Arveson's distance formula, Corollary 4.5 of the first lesson, \(\|\delta_t\|_{\rm cb}=2\operatorname{dist}(t,B')=2\operatorname{dist}(t,\mathbb C1)=2s\), the last distance being attained at \(0\) because \(\|t-\lambda\|\ge\max(|s-\lambda|,|s+\lambda|)\ge s\). Here \(\|r_t\|_{\rm cb}=\|e^{t}\|\|e^{-t}\|\), and \(\log\|r_t\|_{\rm cb}=2s=\|\delta_t\|_{\rm cb}\).

## References

- [Kirchberg] E. Kirchberg, The derivation problem and the similarity problem are equivalent, Journal of Operator Theory 36 (1996), 59–62. https://jot.theta.ro/jot/archive/1996-036-001/1996-036-001-004.pdf
- [Pisier-degree] G. Pisier, The similarity degree of an operator algebra, St. Petersburg Mathematical Journal 10 (1999), Remark 4.7. https://arxiv.org/abs/math/9706211
- [Ozawa] N. Ozawa, An invitation to the similarity problems (after Pisier), lecture notes, RIMS, 2006, Theorem 1.1 and Lemma 1.2. https://www.kurims.kyoto-u.ac.jp/~narutaka/notes/similarity.pdf
- [OpenAI-288] OpenAI, Kadison's similarity theorem through uniform derivation estimates, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
