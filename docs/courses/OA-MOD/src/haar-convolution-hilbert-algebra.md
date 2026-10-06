# Haar convolution from both sides

*GPT-6 (OpenAI), Codex writing thread, Ultra effort, September 2026. New original prose: CC0. Self-checked by the writing AI.*

Convolution on a nonunimodular group has two natural adjoint operations. The left one contains the modular function; the right one does not. The right structure is imported from the existing foundation theorem and verified here in the same compactly supported convolution algebra. The left calculation remains in this lesson. The argument keeps arbitrary locally compact Hausdorff groups and uses nets rather than a hidden countability assumption.

The abstract target is the four Hilbert-algebra axioms. The group-analysis input is left Haar measure with its modular and inversion formulas, density of compactly supported continuous functions in the relevant Radon \(L^2\)-spaces, strong continuity of translations, and compactly supported approximate identities. No separability, sigma-compactness, unimodularity, or finite-Haar-measure hypothesis is imposed.

**Source and statement ownership.** Takesaki, *Theory of Operator Algebras II*, Example VI.1.2, printed p. 2, gives these two structures. Left and right Hilbert algebras, Theorem 4.1 is the existing programme owner of the right-convolution statements: clauses (1)–(3) give boundedness, the adjoint identity and inversion involution; clause (4) gives the weighted graph core once the closed left model is supplied; clause (5) includes the right Hilbert-algebra conclusion. The worked calculations below verify those clauses in our notation, where \(b=\flat\). Their Haar/Radon inputs are the exact programme Haar proofs named in PF's group-analysis input: Proposition 3.1(2),(4), Theorems 10.1 and 11.1, Theorem 14.2(6), and Theorem 15.1. The right clauses use these inputs and the explicit left model below, with no whole-course import. The broader right-algebra and commutant statements remain with their foundation and PF01 proofs.

## One product and two involutions

Let \(G\) be a locally compact Hausdorff group, fix a left Haar measure \(dt\), and write \(\delta:G\to(0,\infty)\) for the continuous modular homomorphism in the convention

\[
 \begin{aligned}
 &\int_G F(th)\,dt\\
 &\qquad=\delta(h)^{-1}\int_G F(t)\,dt,\\
 &\int_G F(t^{-1})\,dt\\
 &\qquad=\int_G F(t)\delta(t)^{-1}\,dt.
 \end{aligned}
 \tag{HG.1}
\]

Put \(H=L^2(G,dt)\), with inner product linear in the first variable, and let \(\mathcal K=C_c(G)\). For \(f,k\in\mathcal K\), define

\[
 \begin{aligned}
 (f*k)(t)
 &=\int_G f(s)\\
 &\qquad{}\cdot k(s^{-1}t)\,ds,
 \end{aligned}
 \tag{HG.2}
\]

and define two conjugate-linear operations

\[
 \begin{aligned}
 f^\sharp(t)&=\delta(t)^{-1}\overline{f(t^{-1})},\\
 f^b(t)&=\overline{f(t^{-1})}.
 \end{aligned}
 \tag{HG.3}
\]

Continuity of translation under a compactly supported integral shows that \(f*k\in C_c(G)\), with
\(\operatorname{supp}(f*k)\subseteq\operatorname{supp}(f)\operatorname{supp}(k)\). Both involutions also preserve \(C_c(G)\), since inversion is a homeomorphism and \(\delta\) is continuous and positive.

Fubini's theorem and left invariance prove associativity. Indeed, after setting \(s=ru\),

\[
 \begin{aligned}
 &((f*k)*h)(t)\\
 &=\int_G\!\int_G f(r)k(r^{-1}s)\\
 &\qquad{}\cdot h(s^{-1}t)\,dr\,ds\\
 &=\int_G f(r)\Bigl(\int_G k(u)\\
 &\qquad{}\cdot h(u^{-1}r^{-1}t)\,du\Bigr)dr\\
 &=(f*(k*h))(t).
 \end{aligned}
 \tag{HG.4}
\]

Every integrand here has compact support, so the iterated integrals are absolutely convergent.

**Worked verification of Theorem 4.1(3).** The two operations in (HG.3) are involutive anti-automorphisms. For \(b\), left invariance alone gives the useful transparent calculation

\[
 \begin{aligned}
 (f*k)^b(t)
 &=\int_G\overline{f(s)}\\
 &\qquad{}\cdot\overline{k(s^{-1}t^{-1})}\,ds\\
 &=\int_G\overline{k(u^{-1})}\\
 &\qquad{}\cdot\overline{f(t^{-1}u)}\,du\\
 &=(k^b*f^b)(t),
 \end{aligned}
 \tag{HG.5}
\]

where \(u=ts\). For \(\sharp\), use inversion in (HG.1) and the homomorphism identity \(\delta(rs)=\delta(r)\delta(s)\) to obtain

\[
 (f*k)^\sharp=k^\sharp*f^\sharp.
 \tag{HG.6}
\]

Applying either operation twice gives \(f\): in the \(\sharp\)-case the two scalar factors cancel because \(\delta(t^{-1})=\delta(t)^{-1}\). Thus \((\mathcal K,*,\sharp)\) and \((\mathcal K,*,b)\) are involutive algebras on the same underlying product.

## Bounded multiplication and the two adjoint identities

Define the left and right regular unitaries on \(H\) by

\[
 \begin{aligned}
 (\lambda(s)\xi)(t)&=\xi(s^{-1}t),\\
 (\rho(s)\xi)(t)&=\delta(s)^{1/2}\xi(ts).
 \end{aligned}
 \tag{HG.7}
\]

Left invariance proves that \(\lambda(s)\) is unitary, and the first formula in (HG.1) proves the same for \(\rho(s)\). For \(f\in\mathcal K\), left convolution extends from \(\mathcal K\) to

\[
 \begin{aligned}
 L_f&=\int_G f(s)\lambda(s)\,ds,\\
 \|L_f\|&\leq\|f\|_1.
 \end{aligned}
 \tag{HG.8}
\]

For each \(\xi\in H\), the map \(s\mapsto f(s)\lambda(s)\xi\) is norm continuous and compactly supported. Its \(H\)-valued Bochner integral defines \(L_f\xi\). The estimate in (HG.8) makes this prescription a bounded operator and gives the displayed weak operator integral. Taking the adjoint, using \(\lambda(s)^*=\lambda(s^{-1})\), and then applying Haar inversion yields

\[
 \begin{aligned}
 L_f^*
 &=\int_G \overline{f(s)}\lambda(s^{-1})\,ds\\
 &=\int_G \delta(u)^{-1}\overline{f(u^{-1})}\\
 &\qquad{}\cdot\lambda(u)\,du\\
 &=L_{f^\sharp}.
 \end{aligned}
 \tag{HG.9}
\]

Consequently, for \(f,k,h\in\mathcal K\),

\[
 \langle f*k,h\rangle=\langle k,f^\sharp*h\rangle
 \tag{HG.10}
\]

which is the left Hilbert-algebra adjoint identity.

**Worked verification of Theorem 4.1(1)–(2).** Right convolution has a different but equally bounded integrated form. Substituting \(u=s^{-1}t\) in (HG.2) gives, first on \(\mathcal K\) and then on \(H\),

\[
 \begin{aligned}
 &R_k\xi=\xi*k\\
 &=\int_G k(u)\delta(u)^{-1/2}\\
 &\qquad{}\cdot\rho(u^{-1})\xi\,du,\\
 &\|R_k\|\\
 &\qquad\leq\int_G|k(u)|\\
 &\qquad\quad{}\cdot\delta(u)^{-1/2}\,du.
 \end{aligned}
 \tag{HG.11}
\]

The bound is finite because \(k\) has compact support. Since \(\rho(u^{-1})^*=\rho(u)\),

\[
 \begin{aligned}
 R_k^*
 &=\int_G\overline{k(u)}\delta(u)^{-1/2}\\
 &\qquad{}\cdot\rho(u)\,du.
 \end{aligned}
 \tag{HG.12}
\]

On the other hand, insert \(k^b(v)=\overline{k(v^{-1})}\) in (HG.11) and substitute \(u=v^{-1}\). Haar inversion changes \(dv\) to \(\delta(u)^{-1}du\), while \(\delta(v)^{-1/2}=\delta(u)^{1/2}\). The result is exactly the right side of (HG.12). Hence

\[
 \begin{aligned}
 R_k^*&=R_{k^b},\\
 \langle f*k,h\rangle&=\langle f,h*k^b\rangle.
 \end{aligned}
 \tag{HG.13}
\]

Equations (HG.8) and (HG.11) establish the required boundedness from the left and from the right without claiming bounded convolution for an arbitrary \(L^2\)-vector.

## Closed involutions and the product core

Let \(D\) be multiplication by \(\delta\) on its maximal positive self-adjoint domain and define

\[
 (J\xi)(t)=\delta(t)^{-1/2}\overline{\xi(t^{-1})}.
 \tag{HG.14}
\]

Haar inversion shows that \(J\) is antiunitary. The same calculation, together with \(\delta(t^{-1})=\delta(t)^{-1}\), gives \(J^2=I\). On \(C_c(G)\), the two algebraic involutions have the closed-operator models

\[
 \begin{aligned}
 f^\sharp&=JD^{1/2}f,\\
 f^b&=JD^{-1/2}f.
 \end{aligned}
 \tag{HG.15}
\]

Both operators on the right are closed because \(D^{1/2}\) and \(D^{-1/2}\) are closed and \(J\) is antiunitary.

**Worked verification of Theorem 4.1(4).** These are not merely closed extensions: \(C_c(G)\) is a graph core for each. Write the two graph norms as

\[
 \begin{aligned}
 \|f\|_\sharp^2
 &:=\|f\|^2+\|D^{1/2}f\|^2\\
 &=\int_G(1+\delta)|f|^2\,dt,\\
 \|f\|_b^2
 &:=\|f\|^2+\|D^{-1/2}f\|^2\\
 &=\int_G(1+\delta^{-1})|f|^2\,dt.
 \end{aligned}
 \tag{HG.16}
\]

The measures \((1+\delta)dt\) and \((1+\delta^{-1})dt\) are Radon measures because their densities are positive and continuous. Compactly supported continuous functions are dense in both \(L^2\)-spaces. Therefore the closures of the involutions initially defined on \(\mathcal K\) are exactly \(JD^{1/2}\) and \(JD^{-1/2}\), respectively. In particular, both algebraic involutions are closable.

**The adjoint domain.** Put \(S=\overline{\sharp}=JD^{1/2}\). Haar inversion gives \(JDJ=D^{-1}\), with maximal multiplication domains: multiplication by \(\delta\) becomes multiplication by \(\delta^{-1}\). The adjoint-involution theorem TC09 therefore gives \(S^*=JD^{-1/2}\) on \(D(D^{-1/2})\). Thus the right closure just verified is exactly the adjoint involution in foundation clause (4). Its only left input is the closed multiplication model established in this paragraph; the Fourier-algebra part of PF is not an antecedent of this argument.

It remains to verify density of products. Direct the identity neighborhoods \(U\) by reverse inclusion and choose \(u_U\in C_c(G)_+\) with integral one and support contained in \(U\). For every \(\xi\in C_c(G)\),

\[
 \begin{aligned}
 &\|u_U*\xi-\xi\|_2\\
 &\qquad\leq\sup_{s\in U}\|\lambda(s)\xi-\xi\|_2\\
 &\qquad\longrightarrow0.
 \end{aligned}
 \tag{HG.17}
\]

by strong continuity of the left regular representation. Each \(u_U*\xi\) is a product of two elements of \(\mathcal K\). Since \(\mathcal K\) is itself dense in \(H\), the linear span \(\mathcal K^2\) is dense in \(H\).

The retained calculations verify all four axioms on arbitrary \(G\), with the right statement supplied by Theorem 4.1(5):

* \((C_c(G),*,\sharp)\) is a left Hilbert algebra in \(L^2(G,dt)\);
* \((C_c(G),*,b)\) is a right Hilbert algebra in the same Hilbert space.

The modular factor appears on the side selected by left Haar measure. When \(G\) is unimodular, \(\delta=1\) and the two involutions coincide. In general they are genuinely different, even though their product core and Hilbert completion are the same.
