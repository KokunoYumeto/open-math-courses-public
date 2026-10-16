# Separated bands and equivariant traces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The projection of the course is the spectral projection of a self-adjoint operator onto a part of its spectrum that is separated from the rest. Such a projection is a continuous function of the operator, so it stays in every \(C^*\)-algebra containing the operator. Its size is measured by an *identity trace*: the sum of the diagonal coefficients at the identity of the group, for operators that commute with a right action of the group. This lesson proves the properties of that trace and two Hilbert-space estimates used at the end of the course: cutting a separated band by a projection that almost contains it, and moving a separated band by a small perturbation [OpenAI-KK, Lemmas 8.4, 10.1 and 10.2].

- Separated parts of the spectrum (Section 1).
- The identity trace of equivariant operators (Section 2).
- Cutting a separated band (Section 3).
- Perturbing a separated band (Section 4).

We use the continuous functional calculus (Theorem 5.1), spectral permanence (Theorem 3.2) and the compatibility of the calculus with \(*\)-homomorphisms (Corollary 5.4) of [C\*-algebras, continuous functional calculus, automatic continuity and positive cones](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones). All Hilbert spaces are complex; operators are bounded.

## 1. Separated parts of the spectrum

Let \(T=T^*\) be a bounded operator. A subset \(\Sigma\) of its spectrum is *separated* if it has positive distance from the rest of the spectrum. The function equal to \(1\) on \(\Sigma\) and \(0\) on the rest of the spectrum is then continuous on the spectrum, and \(\mathbf1_\Sigma(T)\), defined by the continuous functional calculus, is a projection.

**Lemma 1.1** (separated spectral projections). Let \(\mathcal A\) be a unital \(C^*\)-algebra of operators containing \(T=T^*\), and let \(\Sigma\) be a separated part of the spectrum of \(T\).

1. The projection \(\mathbf1_\Sigma(T)\) belongs to \(\mathcal A\), and it commutes with every operator that commutes with \(T\).
2. If \(\Sigma\) lies inside a circle \(\mathcal C\) and the rest of the spectrum lies outside it, then
\[
\mathbf1_\Sigma(T)=\frac1{2\pi i}\oint_{\mathcal C}(z-T)^{-1}\,dz ,
\]
the integral of a norm-continuous function, taken counterclockwise.

*Proof.* (1) By spectral permanence, the spectrum of \(T\) in \(\mathcal A\) equals its operator spectrum, so the continuous functional calculus of \(\mathcal A\) applies, and \(\mathbf1_\Sigma(T)\in\mathcal A\). It is a norm limit of polynomials in \(T\), which commute with every operator commuting with \(T\).

(2) For \(z\in\mathcal C\), \(z\mapsto(z-T)^{-1}\) is the continuous function \(\lambda\mapsto(z-\lambda)^{-1}\) of \(T\), and it is norm continuous in \(z\). Riemann sums of the integral are functions \(r_n(T)\), where \(r_n\) are Riemann sums of \(\lambda\mapsto\frac1{2\pi i}\oint_{\mathcal C}(z-\lambda)^{-1}dz\). This scalar integral is \(1\) for \(\lambda\) inside \(\mathcal C\) and \(0\) outside, by Cauchy's formula, and the \(r_n\) converge to it uniformly on the spectrum, which has positive distance from \(\mathcal C\). Since \(\|f(T)\|\) is the supremum of \(|f|\) on the spectrum, \(r_n(T)\) converges in norm to \(\mathbf1_\Sigma(T)\). \(\square\)

## 2. The identity trace of equivariant operators

Let \(L\) be a countable group and \(I\) a countable set. On \(\mathcal H_I=\ell^2(L)\otimes\ell^2(I)\) we write \(\delta_{(\eta,i)}=\delta_\eta\otimes\delta_i\). A *right phase action* of \(L\) is a family of unitaries \(R_k\), \(k\in L\), on \(\ell^2(L)\) with
\[
R_k\delta_\eta=\omega_k(\eta)\,\delta_{\eta k},\qquad|\omega_k(\eta)|=1 .
\]
The right translations \((R_k\xi)(\eta)=\xi(\eta k)\), up to replacing \(k\) by \(k^{-1}\), are an example; twisted versions with phases appear in later lessons. An operator \(A:\mathcal H_I\to\mathcal H_J\) is *equivariant* if \(A(R_k\otimes1)=(R_k\otimes1)A\) for all \(k\), with the same right phase action on both sides. Every element of \(M_N(C_r^*(L))\) is equivariant for the right translations, \(I=\{1,\ldots,N\}\), because left and right translations commute.

For an equivariant \(B\ge0\) on \(\mathcal H_I\), the *identity trace* is
\[
\operatorname{Tr}_I(B)=\sum_{i\in I}\langle B\delta_{(1,i)},\delta_{(1,i)}\rangle\in[0,\infty] .
\]
For \(B\in M_N(C_r^*(L))\) positive, \(\operatorname{Tr}_I(B)=\tau_{L,N}(B)\), the unnormalized matrix trace.

**Lemma 2.1** (the identity trace; [OpenAI-KK, Lemma 8.4]). Let \(A:\mathcal H_I\to\mathcal H_J\) be bounded and equivariant.

1. \(\operatorname{Tr}_I(A^*A)=\operatorname{Tr}_J(AA^*)\).
2. \(\operatorname{Tr}_I\) is additive on equivariant positive operators, monotone, and independent of the choice of orthonormal basis of \(\ell^2(I)\).
3. An equivariant projection \(P\) with \(\operatorname{Tr}_I(P)=0\) is zero.
4. If \(P,Q\) are equivariant projections and an equivariant bounded \(A\) is injective on the range of \(P\) and maps it into the range of \(Q\), then \(\operatorname{Tr}(P)\le\operatorname{Tr}(Q)\). If \(P\) and \(Q\) are equivalent through an equivariant partial isometry, their traces are equal.

*Proof.* (1) Let \(k=g^{-1}\). Since \(R_k\otimes1\) is unitary and commutes with \(A\),
\[
\begin{aligned}
&\langle A\delta_{(1,i)},\delta_{(g,j)}\rangle\\
&\qquad=\langle A(R_k\otimes1)\delta_{(1,i)},(R_k\otimes1)\delta_{(g,j)}\rangle ,
\end{aligned}
\]
and \((R_k\otimes1)\delta_{(1,i)}\), \((R_k\otimes1)\delta_{(g,j)}\) are unimodular multiples of \(\delta_{(g^{-1},i)}\), \(\delta_{(1,j)}\). So \(|\langle A\delta_{(1,i)},\delta_{(g,j)}\rangle|=|\langle A\delta_{(g^{-1},i)},\delta_{(1,j)}\rangle|\). Summing nonnegative terms in any order,
\[
\begin{aligned}
\operatorname{Tr}_I(A^*A)&=\sum_i\|A\delta_{(1,i)}\|^2\\
&=\sum_{i,j,g}|\langle A\delta_{(1,i)},\delta_{(g,j)}\rangle|^2\\
&=\sum_{j}\sum_{g,i}|\langle\delta_{(g^{-1},i)},A^*\delta_{(1,j)}\rangle|^2\\
&=\operatorname{Tr}_J(AA^*) ,
\end{aligned}
\]
including the value \(\infty\).

(2) Additivity and monotonicity hold termwise. A change of orthonormal basis of \(\ell^2(I)\) is conjugation by an equivariant unitary \(W=1\otimes w\); by (1) applied to \(A=WB^{1/2}\), which is equivariant because \(B^{1/2}\) is a norm limit of polynomials in \(B\), \(\operatorname{Tr}(WBW^*)=\operatorname{Tr}(B^{1/2}W^*WB^{1/2})\), which is \(\operatorname{Tr}(B)\).

(3) Each term \(\langle P\delta_{(1,i)},\delta_{(1,i)}\rangle=\|P\delta_{(1,i)}\|^2\) vanishes, so \(P\delta_{(1,i)}=0\), and \(P\delta_{(k,i)}\) is a unimodular multiple of \((R_k\otimes1)P\delta_{(1,i)}=0\). So \(P\) vanishes on a basis.

(4) Let \(AP=V|AP|\) be the polar decomposition, with \(\ker V=\ker AP\) (Proposition 5.2 of [The spectral theorem for bounded self-adjoint operators](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators)). Its initial projection is the projection onto \((\ker AP)^\perp\), which is \(P\) because \(AP\) is injective on the range of \(P\) and vanishes on its complement; its final projection is the projection onto the closure of the range of \(AP\), which is at most \(Q\). The partial isometry \(V\) is equivariant: if \(W_I,W_J\) denote the unitaries \(R_k\otimes1\) on the two spaces, then \(W_JVW_I^*\) is again a partial isometry with \(W_JVW_I^*\,|AP|=W_J\,AP\,W_I^*=AP\), because \(|AP|\) commutes with \(W_I\), and with the same kernel, so it equals \(V\) by the uniqueness of the polar decomposition. By (1) and monotonicity, \(\operatorname{Tr}(P)=\operatorname{Tr}(V^*V)\), which equals \(\operatorname{Tr}(VV^*)\le\operatorname{Tr}(Q)\). For equivalent projections apply (1) to the partial isometry. \(\square\)

The statements apply to countable orthogonal sums of such spaces, with the sum of the identity traces. In particular, a nonzero equivariant projection has strictly positive identity trace.

## 3. Cutting a separated band

**Lemma 3.1** (compression of a separated upper space; [OpenAI-KK, Lemma 10.1]). Let \(A=A^*\) with \(\|A\|\le2\), and \(E\) a projection commuting with \(A\), such that
\[
\begin{gathered}
\|(A-I)E\|\le a,\\
A|_{(1-E)\mathcal H}\le(1-b)I,\quad0<b<1 .
\end{gathered}
\]
Let \(J\) be a projection with \(\varepsilon=\|(1-J)E\|\le\frac12\). Then \(JE\) has closed range; let \(E^J\) be the projection onto it, and on \(J\mathcal H\) put
\[
B_J=E^J+(J-E^J)A(J-E^J).
\]
Then
\[
\begin{gathered}
\|JAJ-B_J\|\le a+12\varepsilon,\quad\|B_J\|\le2 ,\\
B_J|_{(J-E^J)\mathcal H}\le(1-b)I ,
\end{gathered}
\]
and there is a partial isometry \(V\) with \(V^*V=E\), \(VV^*=E^J\) and \(\|V-E\|\le2\varepsilon\). If \(A,E,J\) commute with a family of unitaries, so do \(E^J\), \(B_J\) and \(V\); in particular \(E\) and \(E^J\) have equal identity traces when the family is a right phase action.

*Proof.* In the corner \(E\mathcal H\),
\[
\begin{aligned}
EJE&=E-\bigl((1-J)E\bigr)^*(1-J)E\\
&\ge(1-\varepsilon^2)E .
\end{aligned}
\]
So \(\|JEx\|^2=\langle EJEx,x\rangle\ge(1-\varepsilon^2)\|x\|^2\) for \(x\in E\mathcal H\), and \(JE\) has closed range. Let \((EJE)^{-1/2}\) be taken in the corner, by the continuous functional calculus, and \(V=JE(EJE)^{-1/2}\). Then \(V^*V=E\), and \(VV^*\) is the projection onto the range of \(JE\), which is \(E^J\). The spectrum of \(EJE\) in the corner lies in \([1-\varepsilon^2,1]\), so
\[
\begin{aligned}
\|(EJE)^{-1/2}-E\|&\le(1-\varepsilon^2)^{-1/2}-1\\
&\le2\varepsilon^2 ,
\end{aligned}
\]
and \(\|V-E\|\le\|JE-E\|+2\varepsilon^2\), which is \(\varepsilon+2\varepsilon^2\le2\varepsilon\).

A vector \(y\) of \((J-E^J)\mathcal H\) is orthogonal to \(E\mathcal H\): \(\langle y,Ex\rangle=\langle Jy,Ex\rangle=\langle y,JEx\rangle=0\). Hence \((J-E^J)\mathcal H\subseteq(1-E)\mathcal H\), where \(A\le(1-b)I\); this is the second assertion. The third holds because \(B_J\) is the orthogonal sum of \(E^J\) and an operator of norm at most \(2\).

On \(J\mathcal H=E^J\mathcal H\oplus(J-E^J)\mathcal H\), the operators \(JAJ\) and \(B_J\) have the same lower right block. In the upper left block, \(E^JAE^J-E^J=V(V^*AV-E)V^*\), and
\[
\begin{aligned}
\|V^*AV-E\|&\le\|V^*AV-EAE\|\\
&\quad+\|EAE-E\|\\
&\le8\varepsilon+a ,
\end{aligned}
\]
since \(\|V-E\|\le2\varepsilon\), \(\|A\|\le2\) and \(\|V\|=1\). The off-diagonal block of \(JAJ\) is \((J-E^J)AE^J=(J-E^J)AVV^*\), and since \(AE=EAE\) and \((J-E^J)E=0\),
\[
\begin{aligned}
&\|(J-E^J)AV\|\\
&\quad=\|(J-E^J)A(V-E)\|\le4\varepsilon .
\end{aligned}
\]
A self-adjoint block matrix with blocks of norms \(x\), \(y\), \(y\), \(0\) has norm at most \(x+y\). So \(\|JAJ-B_J\|\le a+8\varepsilon+4\varepsilon\).

All the operators are built from \(A,E,J\) by products, adjoints and continuous functions, which commute with every unitary commuting with \(A,E,J\). The trace statement is Lemma 2.1(4). \(\square\)

## 4. Perturbing a separated band

**Lemma 4.1** (close projections). Let \(F_1,F_2\) be projections with \(\|F_1-F_2\|<1\). Then
\[
W=F_2F_1(F_1F_2F_1)^{-1/2},
\]
with the inverse taken in the corner \(F_1\mathcal H\), is a partial isometry with \(W^*W=F_1\) and \(WW^*=F_2\). It commutes with every unitary commuting with \(F_1\) and \(F_2\).

*Proof.* For \(x=F_1x\), \(\|F_2x\|=\|x-(F_1-F_2)x\|\), which is at least \((1-\|F_1-F_2\|)\|x\|\), so \(F_1F_2F_1\ge(1-\|F_1-F_2\|)^2F_1\) in the corner and the inverse square root exists there. Then \(W^*W=G^{-1/2}GG^{-1/2}=F_1\) with \(G=F_1F_2F_1\), and \(WW^*\) is the projection onto the range of \(F_2F_1\). That range is closed; if \(y=F_2y\) is orthogonal to it, then \(\langle y,F_1x\rangle=\langle F_2y,F_1x\rangle=0\) for all \(x\), so \(F_1y=0\) and \(\|(F_2-F_1)y\|=\|y\|\), which forces \(y=0\). So \(WW^*=F_2\). The last statement holds as in Lemma 3.1. \(\square\)

**Lemma 4.2** (a contour estimate; [OpenAI-KK, Lemma 10.2]). Let \(B=B^*\) and \(F\) a projection commuting with \(B\), with \(BF=F\), and the spectrum of \(B\) on \((1-F)\mathcal H\) contained in \([-2,1-b]\), \(0<b<1\). Let \(0<r_0\le b/2\), \(r_0<1\), and \(\mathcal C\) the circle \(|z-1|=r_0\). Let \(A=A^*\) with \(\|A-B\|\le u<r_0\). Then \(\mathcal C\) lies in the resolvent sets of \(A\) and \(B\), the spectrum of \(A\) lies in \([-2-u,1-b+u]\cup[1-u,1+u]\), and the projection
\[
F_A=\frac1{2\pi i}\oint_{\mathcal C}(z-A)^{-1}\,dz
\]
onto the spectral part of \(A\) in \([1-u,1+u]\) satisfies
\[
\|F_A-F\|\le\frac u{r_0-u} .
\]
If \(u<r_0/2\), then \(F_A\) and \(F\) are equivalent through the partial isometry of Lemma 4.1, and if \(A\), \(B\), \(F\) commute with a right phase action, \(F_A\) and \(F\) have equal identity traces.

*Proof.* The spectrum of \(B\) lies in \(\{1\}\cup[-2,1-b]\). A point \(z\in\mathcal C\) has distance \(r_0\) from \(1\) and distance at least \(1-r_0-(1-b)=b-r_0\ge r_0\) from \([-2,1-b]\). For the normal operator \(z-B\) this gives \(\|(z-B)^{-1}\|\le r_0^{-1}\). Writing \(z-A=(z-B)Y\) with \(Y=1-(z-B)^{-1}(A-B)\) and summing the Neumann series, \(z-A\) is invertible with \(\|(z-A)^{-1}\|\le(r_0-u)^{-1}\). The same argument shows that every real \(\lambda\) at distance more than \(u\) from the spectrum of \(B\) is outside the spectrum of \(A\), which gives the stated location; the two parts lie inside and outside \(\mathcal C\), since \(1-b+u<1-r_0<1-u\). By Lemma 1.1(2), \(F\) and \(F_A\) are the contour integrals for \(B\) and \(A\). The resolvent identity
\[
\begin{aligned}
&(z-A)^{-1}-(z-B)^{-1}\\
&\qquad=(z-A)^{-1}(A-B)(z-B)^{-1}
\end{aligned}
\]
bounds the integrand difference by \(u/\bigl(r_0(r_0-u)\bigr)\), and the circle has length \(2\pi r_0\). This gives the estimate. If \(u<r_0/2\), then \(\|F_A-F\|<1\), and Lemma 4.1 applies; \(F_A\) commutes with every unitary commuting with \(A\), by Lemma 1.1(1). The trace statement is Lemma 2.1(4). \(\square\)

## 5. Exercises

**5.1** (easy). Let \(T=\operatorname{diag}(0,1,1)\) and \(\Sigma=\{1\}\). Compute the contour integral of Lemma 1.1(2) over the circle \(|z-1|=\frac12\), and check that it is \(\operatorname{diag}(0,1,1)\).

**5.2** (easy). On \(\ell^2(\mathbb Z)\) with the right translations, show that the operator of multiplication by a function \(f\) on \(\mathbb Z\) is equivariant only if \(f\) is constant. Through the unitary \(\ell^2(\mathbb Z)\cong L^2(\mathbb R/\mathbb Z)\), \(\delta_n\mapsto e^{2\pi in\theta}\), let \(P\) be the projection onto the functions vanishing outside \([0,\frac13]\). Show that \(P\) is equivariant and compute its identity trace.

**5.3** (medium). In Lemma 3.1 take \(\mathcal H=\mathbb C^2\), \(A=\operatorname{diag}(1,0)\), \(E=\operatorname{diag}(1,0)\), \(b=1/2\), and \(J\) the projection onto the line spanned by \((\cos\theta,\sin\theta)\). Compute \(\varepsilon\), \(E^J\), \(B_J\) and \(\|JAJ-B_J\|\), and compare with \(12\varepsilon\).

**5.4** (medium). Show that two projections \(F_1,F_2\) with \(\|F_1-F_2\|<1\) on a finite-dimensional space have the same rank, and give an example with \(\|F_1-F_2\|=1\) and different ranks.

## 6. Solutions

**5.1.** \((z-T)^{-1}\) is diagonal with the entries \(z^{-1}\), \((z-1)^{-1}\), \((z-1)^{-1}\). Over \(|z-1|=\frac12\), \(\frac1{2\pi i}\oint z^{-1}dz=0\) because \(0\) lies outside, and \(\frac1{2\pi i}\oint(z-1)^{-1}dz=1\).

**5.2.** If \(M_f\) commutes with the right translations, then \(f(\eta k)=f(\eta)\) for all \(\eta,k\), so \(f\) is constant. Under \(\delta_n\mapsto e^{2\pi in\theta}\), the right translations become multiplications by \(e^{\pm2\pi ik\theta}\), and the projection \(P\) becomes multiplication by \(\mathbf1_{[0,1/3]}\), which commutes with them. Its identity trace is \(\langle P\delta_0,\delta_0\rangle=\int_0^{1/3}1\,d\theta=\frac13\).

**5.3.** \(\varepsilon=\|(1-J)E\|=|\sin\theta|\). For \(\theta\ne\frac\pi2\), \(JE\) maps \(e_1\) to \(\cos\theta\,(\cos\theta,\sin\theta)\), so \(E^J=J\) and \(J-E^J=0\), and \(B_J=J\) on \(J\mathcal H\). There \(JAJ=\cos^2\theta\,J\), so \(\|JAJ-B_J\|=\sin^2\theta=\varepsilon^2\le12\varepsilon\).

**5.4.** \(W\) of Lemma 4.1 is an isometry from the range of \(F_1\) onto the range of \(F_2\). The coordinate projections onto \(e_1\) and onto the span of \(e_1,e_2\) in \(\mathbb C^2\) differ by the projection onto \(e_2\), of norm \(1\).

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Lemmas 8.4, 10.1 and 10.2. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
