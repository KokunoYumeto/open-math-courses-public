# Order and concavity of positive implementing vectors

A positive normal functional has a unique vector representative in a standard form's positive cone. This representative behaves like a square root: increasing the functional increases its vector, and mixing functionals before taking their representatives gives a larger vector than mixing the representatives. A projection detecting the negative part of a vector difference proves the order assertion directly.

We work in an arbitrary standard form \((M,H,J,P)\). Inner products are linear in the first variable. The complete geometric proofs in SF06, applied at their axiomatic scope in SE01, give the orthogonal positive/negative decomposition and its support projections. SE11 proves existence and uniqueness of the representative of every normal positive functional in every such form. No faithful state on \(M\), separability or countability assumption is imposed.

These properties are considered in Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(1). The proof here proceeds through cone geometry and projection tests. The citation does not replace any of the arguments or their linked prerequisites.

## A projection detects a negative part

Write \(\omega_\xi(x)=\langle x\xi,\xi\rangle\). For \(\xi,\eta\in P\), the difference is fixed by \(J\). Its unique orthogonal decomposition from SF06 is

\[
 \begin{gathered}
 \xi-\eta=p-m,\\
 p,m\in P,\\
 \langle p,m\rangle=0.
 \end{gathered}
 \tag{VQ.1}
\]

Let \(q=s_M(\omega_m)\). The support is the projection onto \(\overline{M'm}\); in particular \(qm=m\). Orthogonality of cone vectors gives orthogonal support projections, by SF06, so \(qp=0\). Consequently \(q\eta=q\xi+m\). Put \(\delta=\omega_\xi-\omega_\eta\). Since a projection satisfies \(\omega_\xi(q)=\|q\xi\|^2\), expansion gives

\[
 \begin{aligned}
 \delta(q)
 &=\|q\xi\|^2-\|q\xi+m\|^2\\
 &=-\|m\|^2-2\langle\xi,m\rangle.
 \end{aligned}
\]

Here \(\langle q\xi,m\rangle=\langle\xi,m\rangle\), because \(q\) is self-adjoint and fixes \(m\). This pairing is real and nonnegative by self-duality of \(P\), so

\[
 \delta(q)\le-\|m\|^2.
 \tag{VQ.2}
\]

Thus any nonzero negative part supplies a projection on which the functional difference is strictly negative. This proof also includes \(m=0\), when its support is the zero projection.

For clarity about the input, SF06's orthogonality argument uses positivity of the pairing of \((1+tx)J(1+tx)Jp\) with \(m\), for every complex \(t\) and \(x\in M\). Its linear term forces \(m\perp Mp\); applying \(J\) gives orthogonal support projections. It uses only the standard-form axioms, so VQ.2 holds in an axiomatic form before choosing any weight model.

## Scaling and increasing a functional

For \(\varphi\in M_*^+\), denote its unique representative by \(\Xi(\varphi)\in P\). Thus \(\omega_{\Xi(\varphi)}=\varphi\), as proved in SE11. Functional order means positivity of the difference on every element of \(M_+\); cone order means membership of the vector difference in \(P\).

**Theorem.** For \(a\ge0\) and \(\varphi,\psi\in M_*^+\),

\[
 \Xi(a\varphi)=\sqrt a\,\Xi(\varphi),
 \tag{VQ.3}
\]

and, whenever \(\varphi\ge\psi\),

\[
 \begin{gathered}
 \Xi(\varphi)-\Xi(\psi)\\
 \in P.
 \end{gathered}
 \tag{VQ.4}
\]

**Proof.** The cone contains \(\sqrt a\,\Xi(\varphi)\), and evaluation of its vector functional gives \(a\varphi\). Uniqueness proves VQ.3. This includes \(a=0\), since the zero vector represents the zero functional.

For VQ.4 put \(\xi=\Xi(\varphi)\), \(\eta=\Xi(\psi)\), and take the negative part \(m\) and projection \(q\) from VQ01. Positivity of \(\varphi-\psi\) gives \(\delta(q)\ge0\). Equation VQ.2 then forces \(\|m\|=0\). Equation VQ.1 becomes \(\xi-\eta=p\in P\), as required. Neither functional was required to be faithful. \(\square\)

An immediate converse in the opposite direction would be false: squaring positive vectors need not preserve order. VQ04 gives a projection that detects this failure in a two-dimensional matrix algebra.

## Mixing before taking the square root

**Theorem.** For \(\varphi,\psi\in M_*^+\) and \(0\le\lambda\le1\), put

\[
 \begin{gathered}
 \xi=\Xi(\varphi),\qquad \eta=\Xi(\psi),\\
 \rho=\lambda\varphi+(1-\lambda)\psi,\\
 \zeta=\lambda\xi+(1-\lambda)\eta.
 \end{gathered}
\]

Then

\[
 \Xi(\rho)-\zeta\in P.
 \tag{VQ.5}
\]

If \(0<\lambda<1\), equality holds exactly when \(\varphi=\psi\). At either endpoint equality always holds.

**Proof.** Convexity gives \(\zeta\in P\). Expansion of the squared norms, with \(x\in M_+\), gives the exact identity

\[
 \begin{gathered}
 \rho(x)-\omega_\zeta(x)\\
 =\lambda(1-\lambda)\omega_{\xi-\eta}(x).
 \end{gathered}
\]

Indeed, writing \(u=x^{1/2}\xi\) and \(v=x^{1/2}\eta\), the left side is

\[
 \begin{aligned}
 &\lambda\|u\|^2+(1-\lambda)\|v\|^2\\
 &\qquad-\|\lambda u+(1-\lambda)v\|^2\\
 &=\lambda(1-\lambda)\|u-v\|^2.
 \end{aligned}
\]

The positive square root exists by the concrete operator calculus of BK01. In particular,

\[
 \rho(x)-\omega_\zeta(x)\ge0.
 \tag{VQ.6}
\]

This verifies positivity directly, without any claim that cone order is preserved by the vector-to-functional map.

Apply VQ.4 to \(\rho\ge\omega_\zeta\). Uniqueness of the cone representative gives \(\Xi(\omega_\zeta)=\zeta\), which proves VQ.5. If its difference is zero, the represented functionals coincide. Evaluating the exact identity above at \(1\), for an interior value of \(\lambda\), gives \(\|\xi-\eta\|^2=0\). Therefore \(\varphi=\psi\). Conversely equal functionals have equal representatives and give equality. The endpoint cases follow immediately from the definitions. \(\square\)

Repeated application gives the finite-mixture assertion: the representative of a finite convex combination dominates the same combination of the representatives. To check this without an additional theorem, discard zero coefficients. For at least two remaining coefficients, separate the last coefficient \(t<1\), divide the others by \(1-t\), and apply VQ.5 followed by the assertion for one fewer coefficient. Multiplication by the nonnegative scalar \(1-t\) and addition preserve cone order. The case of one nonzero coefficient is equality, starting the induction.

## Three checks on the two orders

**Scaling is not additivity.** In the scalar standard form \(M=\mathbb C\), \(H=\mathbb C\), \(J\) is complex conjugation and \(P=0,\infty)\). The functional \(z\mapsto az\), for \(a\ge0\), has representative \(\sqrt a\), by direct evaluation. The equal mixture of the functionals with coefficients \(0\) and \(4\) therefore has representative \(\sqrt2\), whereas the equal mixture of their representatives is \(1\). This verifies strict concavity in a concrete case and disproves additivity.

**The reverse order assertion fails.** In the standard Hilbert–Schmidt form of \(M_2(\mathbb C)\), described and proved in [SF14, let

\[
 A=\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad
 B=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]

Here \(A\ge0\) and \(B-A=ww^*\ge0\), where \(w=(1,1)^T\). Thus \(0\le A\le B\) in the cone. Their functionals have densities \(A^2\) and \(B^2\). Direct multiplication yields

\[
 B^2-A^2=\begin{pmatrix}4&3\\3&2\end{pmatrix}.
\]

Put \(v=(2,-3)^T\), and let \(e=vv^*/13\), a rank-one projection since \(v^*v=13\). Then

\[
 \begin{aligned}
 (\omega_B-\omega_A)(e)
 &=\frac{v^*(B^2-A^2)v}{13}\\
 &=-\frac{2}{13}<0.
 \end{aligned}
\]

The density formula follows from \(\omega_A(x)=\operatorname{Tr}(A x A)=\operatorname{Tr}(xA^2)\); cyclicity here follows by interchanging the two indices in the finite trace sum. This explicitly disproves \(\omega_A\le\omega_B\) despite \(A\le B\).

**Order controls supports.** Suppose \(\varphi\ge\psi\), with representatives \(\xi,\eta\). Let \(e=s_M(\varphi)\). Then \(\varphi(1-e)=0\) implies \(\psi(1-e)=0\). Hence \(\|(1-e)\eta\|^2=0\), so \(e\eta=\eta\). The support's minimal-projection characterization in SF06 yields \(s_M(\psi)\le e\). This includes zero functionals and shows explicitly why they cause no exception in the order theorem.
