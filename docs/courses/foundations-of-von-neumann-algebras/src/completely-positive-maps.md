# Completely positive maps

*Originally written by Claude Opus 5.5 (Anthropic), September 2026, with a separate historical AI spot-check. GPT-6.1 Sol (OpenAI), at the Ultra setting, read, replayed and revised the full lesson and all four solutions, compared the exact programme prerequisites, and completed the construction and boundary details, October 2026. Public domain (CC0).*

A linear map between C\(^*\)-algebras is *positive* if it maps positive elements to positive elements. For most purposes this is too weak. The transpose of \(2\times2\) matrices is positive, but applied entrywise to a \(2\times2\) matrix whose entries are \(2\times2\) matrices, it can destroy positivity. A linear map \(\varphi:A\to B\) is *completely positive* if every entrywise extension \(\varphi^{(n)}:M_n(A)\to M_n(B)\) is positive. States, \(*\)-homomorphisms and compressions \(x\mapsto V^*xV\) are completely positive, and so are their composites. Completely positive maps are the maps to use when multiplicativity is too much to ask: conditional expectations, quantum channels, and the maps that approximate an algebra by matrix algebras are all of this kind.

Section 2 makes the matrix algebra \(M_n(A)\) a C\(^*\)-algebra and describes its positive elements. Section 3 defines \(n\)-positive and completely positive maps, gives the basic examples, and shows that positive maps are bounded. Section 4 proves the Kadison–Schwarz inequality \(\varphi(a)^*\varphi(a)\le\|\varphi\|\,\varphi(a^*a)\) for 2-positive maps, and derives from it a formula for the norm and the multiplicative domain. Section 5 shows that positivity already implies complete positivity when the domain or the target is commutative, and that \(k\)-positivity is enough for maps on \(C_0(\Omega,M_k)\) and for maps into algebras whose irreducible representations have dimension at most \(k\). Section 6 is the centre of the lesson. Stinespring's theorem writes every completely positive map into \(B(H)\) as \(V^*\pi(\cdot)V\) for a representation \(\pi\); the minimal such dilation is unique, and it carries a representation of the commutant \(\varphi(A)'\). Section 7 carries the matrix order over to dual spaces. It identifies the commutant of a GNS representation with the functionals dominated by the state, and it shows how the transpose enters the duality of \(M_d(\mathbb C)\) with itself.

We assume the basic theory of C\(^*\)-algebras, as in the lesson [C\(^*\)-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md). Finite operator matrices are developed below. Von Neumann algebras are treated in [The double commutant theorem](the-double-commutant-theorem.md), and the ultraweak topology and preduals in [Compact and trace-class operators, the predual of B(H), and the operator topologies](compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.md#oa-fnd-lt-10). Section 5 also uses two facts about locally compact spaces from the lesson The Stone–Weierstrass theorem for \(C_0(X)\). The earlier lesson [Representations and positive functionals: the GNS construction and the Gelfand–Naimark theorem](representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#oa-fnd-gn-05) supplies the GNS construction, including the nonunital case. The next section gives the exact earlier proof locations for the background facts.

For a state, Stinespring dilation is the GNS representation. For a general completely positive map, the scalar GNS form becomes an operator-valued positive matrix calculation. Sections 3–7 prove the Schwarz inequalities, the matrix criterion and the dilation, including extension and nonunital steps. A freely readable treatment is [Blackadar, II.6.9].

## Results used from earlier lessons

The proofs in this lesson use the following results. They are proved in the preceding lessons linked below, so the textbook references at the end provide further reading. All C\(^*\)-algebras in (B1)–(B9) may be nonunital.

- **(B1) Positive elements**, [Theorem 8.2 and Proposition 8.5(10) of the C\(^*\)-algebra lesson](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-15). Let \(x\) be a self-adjoint element of a C\(^*\)-algebra \(A\). The following are equivalent: \(x\ge0\), that is, the spectrum of \(x\) lies in \([0,\infty)\); \(x=y^*y\) for some \(y\in A\); \(x=h^2\) for some self-adjoint \(h\in A\). The positive elements form a norm-closed convex cone \(A_+\) with \(A_+\cap(-A_+)=\{0\}\). Every \(a\in A_+\) has exactly one positive square root \(a^{1/2}\). It is a norm limit of polynomials in \(a\) without constant term, so it commutes with every element that commutes with \(a\).
- **(B2) Spectral permanence**, [Theorem 3.2 of the C\(^*\)-algebra lesson](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-06). If \(B\) is a C\(^*\)-subalgebra of \(A\), an element of \(B\) has the same spectrum in \(B\) as in \(A\), apart from the point \(0\).
- **(B3) Homomorphisms**, [Theorem 4.2 and Corollary 4.6 of the C\(^*\)-algebra lesson](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-12). A \(*\)-homomorphism between C\(^*\)-algebras is contractive. An injective one is isometric, so its range is closed.
- **(B4) Functional calculus**, [Theorems 5.1 and 5.3](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-07) and [Proposition 7.2](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-09) of the C\(^*\)-algebra lesson. Let \(h\) be a self-adjoint element of a unital C\(^*\)-algebra, with spectrum \(\sigma(h)\). For continuous \(f\) on \(\sigma(h)\) the element \(f(h)\) is defined, and \(f\mapsto f(h)\) is an isometric \(*\)-homomorphism of \(C(\sigma(h))\) into the algebra that sends the identity function to \(h\). In particular, the norm of a self-adjoint element equals its spectral radius. Without a unit the same holds in the unitization, and \(f(h)\) lies in the algebra when \(f(0)=0\). With \(f(t)=\max(\pm t,0)\) this gives \(h=h_+-h_-\) with \(h_\pm\ge0\), \(h_+h_-=0\) and \(\|h_\pm\|\le\|h\|\).
- **(B5) Commutative C\(^*\)-algebras**, [Theorem 2.1 of the C\(^*\)-algebra lesson](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-04) (the commutative Gelfand–Naimark theorem). Let \(B\) be an abelian C\(^*\)-algebra, and \(\Omega\) its space of characters, a locally compact Hausdorff space. The Gelfand transform \(b\mapsto\hat b\), \(\hat b(\chi)=\chi(b)\), is an isometric \(*\)-isomorphism of \(B\) onto \(C_0(\Omega)\).
- **(B6) Approximate identities**, [Theorem 11.4, applied to the whole algebra](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-19). Every C\(^*\)-algebra \(A\) has an increasing net \((u_i)\) in \(A_+\) with \(\|u_i\|\le1\), \(\|u_ix-x\|\to0\) and \(\|xu_i-x\|\to0\) for all \(x\in A\).
- **(B7) Positive functionals**, [Proposition 3.2](representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#oa-fnd-gn-03) and [Theorem 4.7](representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#oa-fnd-gn-04) of the GNS lesson. A positive linear functional \(f\) on \(A\) is bounded, and \(f(x^*)=\overline{f(x)}\). The form \((x,y)\mapsto f(y^*x)\) is positive semidefinite, so \(|f(y^*x)|^2\le f(x^*x)f(y^*y)\).
- **(B8) The GNS construction**, [Construction 5.1 and Theorems 5.4–5.5 of the GNS lesson](representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#oa-fnd-gn-05). For every positive linear functional \(f\) on \(A\) there are a Hilbert space \(H_f\), a representation \(\pi_f\) of \(A\) on \(H_f\) and a vector \(\xi_f\in H_f\) with \(f(a)=\langle\pi_f(a)\xi_f,\xi_f\rangle\) for all \(a\in A\), such that \(\pi_f(A)\xi_f\) is dense in \(H_f\). Moreover \(\|\xi_f\|^2=\|f\|\), and the triple is unique up to the unitary that preserves this vector and intertwines the representations.
- **(B9) Enough representations**, [Theorem 7.2](representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#oa-fnd-gn-07) and [Theorem 8.5(2)](representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#oa-fnd-gn-10) of the GNS lesson. For every nonzero \(b\in A\) there is a positive linear functional \(f\) whose GNS representation \(\pi_f\) is irreducible and has \(\pi_f(b)\ne0\). So the irreducible representations of \(A\) separate its points, and the direct sum of the GNS representations of all positive functionals of \(A\) is faithful. In particular, every C\(^*\)-algebra has a faithful representation (the Gelfand–Naimark theorem).
- **(B10) Operators on Hilbert space**, [Theorem 3.1 and Corollary 3.2 of Hilbert spaces and compact operators](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-03), and [Corollary 5.2 of the Hahn–Banach and Baire lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-05). Every bounded sesquilinear form \(\beta\) on a Hilbert space \(H\) has the form \(\beta(\xi,\eta)=\langle T\xi,\eta\rangle\) for a unique \(T\in B(H)\). A self-adjoint \(T\in B(H)\) has \(\|T\|=\sup_{\|\xi\|=1}|\langle T\xi,\xi\rangle|\), so \(\|T\|=\sup_{\|\xi\|=1}\langle T\xi,\xi\rangle\) when \(T\ge0\). A bounded linear bijection between Banach spaces has a bounded inverse (the open mapping theorem).
- **(B11) Preduals**, [Theorem 9.4(a) of Compact and trace-class operators, the predual of B(H), and the operator topologies](compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.md#oa-fnd-lt-10). For a von Neumann algebra \(N\), the space \(N_*\) of ultraweakly continuous linear functionals on \(N\) is norm-closed in the dual space \(N^*\). The earlier theorem proves this for every ultraweakly closed linear subspace of \(B(H)\), by identifying its space of normal functionals isometrically with a quotient of \(B(H)_*\).
- **(B12) Locally compact spaces**, Proposition 4.2(2) and Corollary 5.2 of The Stone–Weierstrass theorem for functions vanishing at infinity. Let \(X\) be a locally compact Hausdorff space. If \(C\subseteq X\) is compact and \(V\supseteq C\) is open, some open \(W\supseteq C\) has compact closure contained in \(V\). If \(C\) is compact, \(F\) is closed and \(C\cap F=\varnothing\), there is \(g\in C_c(X)\) with \(0\le g\le1\), \(g=1\) on \(C\) and \(g=0\) on \(F\) (Urysohn's lemma).

The completion of a normed or inner product space, its null-space quotient and extension of bounded maps are proved in the [completion lemma in Section 1 of the Hilbert-space lesson](hilbert-spaces-and-compact-operators.md#completing-normed-and-inner-product-spaces). Its [Proposition 1.1](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-01) proves Cauchy–Schwarz and polarization for semidefinite forms. [Theorem 7.1(3) of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-07) proves boundedness of linear maps on finite-dimensional normed spaces. For Example 7.4, the [real-line measure and density lemma](compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.md#oa-fnd-lt-17), Lemma 0.1(b)–(c), constructs Lebesgue measure and proves \(C_c^\infty(0,1)\)-density in \(L^2(0,1)\); endpoints have measure zero. Theorem 3.2 of the measure-tools lesson proves its completeness.

## 1. Conventions

*Zero cases.* The zero algebra and zero Hilbert space are allowed. Their identity operator is zero; suprema of nonnegative quantities over an empty index set are taken as zero. Zero-dimensional summands can be discarded from a separating family of representations.

*Algebras and order.* C\(^*\)-algebras are complex and need not have a unit. \(A_h\) is the set of self-adjoint elements of \(A\), and \(A_+\) the set of positive ones, as in (B1). We write \(x\le y\) when \(y-x\in A_+\). If \(x\le y\), then \(z^*xz\le z^*yz\) for every \(z\in A\): write \(y-x=w^*w\), so that \(z^*(y-x)z=(wz)^*(wz)\).

*Representations.* A representation of \(A\) on a Hilbert space \(H\) is a \(*\)-homomorphism \(\pi:A\to B(H)\). It is faithful if it is injective, and nondegenerate if \(\pi(A)H\) spans a dense subspace. Inner products \(\langle\xi,\eta\rangle\) are linear in \(\xi\). A \(*\)-homomorphism between C\(^*\)-algebras is contractive, and an injective one is isometric (B3). Every C\(^*\)-algebra has a faithful representation, for instance the direct sum of the GNS representations of all its positive functionals (B8), (B9).

*(P1) Order is intrinsic.* If \(B\subseteq A\) is a C\(^*\)-subalgebra, an element of \(B\) is positive in \(B\) exactly when it is positive in \(A\), because its spectrum is the same in both algebras apart from \(0\) (B1), (B2). An injective \(*\)-homomorphism \(\sigma:A\to C\) is an isometric \(*\)-isomorphism onto a C\(^*\)-subalgebra of \(C\), so \(a\ge0\) if and only if \(\sigma(a)\ge0\).

*(P2) Operators.* \(T\in B(H)\) is positive in the C\(^*\)-algebra \(B(H)\) if and only if \(\langle T\xi,\xi\rangle\ge0\) for all \(\xi\). Indeed, if \(T=S^*S\), then \(\langle T\xi,\xi\rangle=\|S\xi\|^2\). Conversely, if the form is nonnegative, it is real, so \(T=T^*\). For \(\lambda<0\) we get \(\|(T-\lambda)\xi\|\,\|\xi\|\ge\langle(T-\lambda)\xi,\xi\rangle\ge|\lambda|\,\|\xi\|^2\). So \(T-\lambda\) is bounded below; being self-adjoint with zero kernel, it also has dense range, so it is invertible. Hence the spectrum of \(T\) lies in \([0,\infty)\). For positive \(T\) we also use \(\|T\|=\sup_{\|\xi\|=1}\langle T\xi,\xi\rangle\) (B10). With a faithful representation and (P1), it gives: \(0\le x\le y\) implies \(\|x\|\le\|y\|\), in every C\(^*\)-algebra.

*Functional calculus.* For \(h\in A_h\) there are \(h_\pm\in A_+\) with \(h=h_+-h_-\), \(h_+h_-=0\) and \(\|h_\pm\|\le\|h\|\) (B4). Every \(x\in A\) is \(h+ik\) with \(h,k\in A_h\) and \(\|h\|,\|k\|\le\|x\|\). So \(x\) is a combination of four positive elements of norm at most \(\|x\|\).

*Approximate identities.* In this lesson an approximate identity of \(A\) is an increasing net \((u_i)_{i\in I}\) in \(A_+\) with \(\|u_i\|\le1\), \(\|u_ix-x\|\to0\) and \(\|xu_i-x\|\to0\) for all \(x\). Every C\(^*\)-algebra has one (B6). If \(\pi\) is nondegenerate, then \(\pi(u_i)\to1\) strongly: on vectors \(\pi(a)\zeta\) we have \(\pi(u_i)\pi(a)\zeta=\pi(u_ia)\zeta\to\pi(a)\zeta\), these vectors span a dense subspace, and the net is bounded.

*Positive functionals.* A positive linear functional \(f\) on \(A\) is bounded, \(f(x^*)=\overline{f(x)}\), and \(|f(y^*x)|^2\le f(x^*x)f(y^*y)\) (B7). It satisfies \(\|f\|\le4\sup\{f(a):a\in A_+,\ \|a\|\le1\}\); this is the case \(B=\mathbb C\) of Proposition 3.2(4) below.

*Matrices of operators.* \(H^n\) is the direct sum of \(n\) copies of \(H\), and \(R_i:H\to H^n\) is the inclusion of the \(i\)-th copy. Then \(R_i^*R_j=\delta_{ij}1\) and \(\sum_iR_iR_i^*=1\). Every \(T\in B(H^n)\) is determined by its matrix \(T_{ij}=R_i^*TR_j\), and \(T=\sum_{i,j}R_iT_{ij}R_j^*\). The \(e_{ij}\) are the matrix units of \(M_n(\mathbb C)\), and \(\varepsilon_1,\dots,\varepsilon_k\) is the standard basis of \(\mathbb C^k\). The unitary \(\xi\otimes\varepsilon_i\mapsto R_i\xi\) identifies the Hilbert tensor product \(H\otimes\mathbb C^n\) with \(H^n\); see the description of [the Hilbert tensor-product construction](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-08), with \(K=\mathbb C^n\).

*Von Neumann algebras and normality.* For \(S\subseteq B(H)\), \(S'\) is its commutant. As in [Section 2 of the double-commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-02), a von Neumann algebra is a \(*\)-subalgebra \(M\) with \(M''=M\). If \(S^*=S\), then \(S'\) is a von Neumann algebra, since \(S'''=S'\). The space \(B(K)_*\) consists of the functionals \(\sum_n\langle\,\cdot\,\kappa_n,\lambda_n\rangle\) with \(\sum\|\kappa_n\|^2<\infty\) and \(\sum\|\lambda_n\|^2<\infty\), and the ultraweak (or \(\sigma\)-weak) topology is the weakest topology in which all of them are continuous. A linear map between von Neumann algebras is *normal* if it is ultraweakly continuous. For a map \(\rho\) into \(B(K)\) this means that \(\psi\circ\rho\) is ultraweakly continuous for every \(\psi\in B(K)_*\). For a von Neumann algebra \(N\), \(N_*\) is the space of its ultraweakly continuous functionals; it is norm-closed in \(N^*\) (B11).

## 2. Matrices over a C\(^*\)-algebra

Let \(A\) be a C\(^*\)-algebra and \(n\ge1\). \(M_n(A)\) is the set of \(n\times n\) matrices \(a=[a_{ij}]\) with entries in \(A\). With entrywise linear operations, the product \((ab)_{ij}=\sum_ka_{ik}b_{kj}\) and the adjoint \((a^*)_{ij}=(a_{ji})^*\), it is a \(*\)-algebra. For a representation \(\pi\) of \(A\) on \(H\) put
\[
\begin{gathered}
\pi^{(n)}(a)=\sum_{i,j}R_i\,\pi(a_{ij})\,R_j^*, \\
(\pi^{(n)}(a)\zeta)_i=\sum_j\pi(a_{ij})\zeta_j.
\end{gathered}
\tag{2.1}
\]

**Proposition 2.1** (The C\(^*\)-algebra \(M_n(A)\)).

1. \(\pi^{(n)}\) is a \(*\)-homomorphism of \(M_n(A)\) into \(B(H^n)\), with entries \(R_i^*\pi^{(n)}(a)R_j=\pi(a_{ij})\), and
\[
\begin{gathered}
\max_{i,j}\|\pi(a_{ij})\| \\
\le\|\pi^{(n)}(a)\| \\
\le\sum_{i,j}\|\pi(a_{ij})\|.
\end{gathered}
\tag{2.2}
\]
It is injective if and only if \(\pi\) is. Its range is the set of operators on \(H^n\) whose matrix entries all lie in \(\pi(A)\).
2. \(M_n(A)\) has exactly one norm in which it is a C\(^*\)-algebra. For every faithful \(\pi\) it is \(\|a\|=\|\pi^{(n)}(a)\|\), and \(\max_{i,j}\|a_{ij}\|\le\|a\|\le\sum_{i,j}\|a_{ij}\|\).
3. For every representation \(\pi\), \(\pi^{(n)}\) is a representation of the C\(^*\)-algebra \(M_n(A)\). For a \(*\)-homomorphism \(\sigma:A\to B\), the entrywise map \(\sigma^{(n)}:M_n(A)\to M_n(B)\) is a \(*\)-homomorphism, injective when \(\sigma\) is.
4. If \(B\subseteq A\) is a C\(^*\)-subalgebra, then \(M_n(B)\) is a C\(^*\)-subalgebra of \(M_n(A)\), and \(M_n(B)_+=M_n(B)\cap M_n(A)_+\).
5. \(X\mapsto\sum_{i,j}R_iX_{ij}R_j^*\) is a \(*\)-isomorphism of \(M_n(B(H))\) onto \(B(H^n)\). So \(X\in M_n(B(H))\) is positive exactly when \(\sum_{i,j}\langle X_{ij}\zeta_j,\zeta_i\rangle\ge0\) for every \(\zeta\in H^n\).
6. Let \(\Omega\) be a locally compact Hausdorff space. Identify \(F\in M_n(C_0(\Omega))\) with the function \(\omega\mapsto F(\omega)=[F_{ij}(\omega)]\in M_n(\mathbb C)\). Then \(\|F\|=\sup_\omega\|F(\omega)\|\), and \(F\ge0\) if and only if \(F(\omega)\ge0\) for every \(\omega\).
7. (*Scalar compressions.*) For \(a\in M_n(A)\) and a scalar \(n\times m\) matrix \(\alpha\), let \(\alpha^*a\alpha\in M_m(A)\) have entries \((\alpha^*a\alpha)_{pq}=\sum_{i,j}\overline{\alpha_{ip}}\,a_{ij}\,\alpha_{jq}\). If \(a\ge0\), then \(\alpha^*a\alpha\ge0\). In particular, square corners of positive matrices are positive, so are the diagonal entries, so is \(a\oplus0\), and so is every relabelling \([a_{\tau(i)\tau(j)}]\) by a permutation \(\tau\).

**Proof.** (1) The product rule gives \[
\begin{gathered}
(\pi^{(n)}(a)\pi^{(n)}(b))_{ik}\\
=\sum_j\pi(a_{ij})\pi(b_{jk})\\
=\pi((ab)_{ik}).
\end{gathered}
\] Also \(\pi^{(n)}(a)^*=\sum_{i,j}R_j\pi(a_{ij})^*R_i^*=\pi^{(n)}(a^*)\). The entry formula follows from \(R_i^*R_k=\delta_{ik}1\). It gives the left inequality in (2.2), and (2.1) gives the right one. An operator is determined by its entries, so \(\pi^{(n)}(a)=0\) exactly when every \(\pi(a_{ij})=0\). Every \(T\in B(H^n)\) equals \(\sum R_iT_{ij}R_j^*\), which describes the range.

(2) Let \(\pi\) be faithful; such a \(\pi\) exists by (B9). By (1), \(\pi^{(n)}\) is injective. The injective \(*\)-homomorphism \(\pi\) is isometric (B3), so (2.2) becomes the stated inequalities for \(\|a\|:=\|\pi^{(n)}(a)\|\). The range \(D=\pi^{(n)}(M_n(A))\) is closed. Indeed, if \(\pi^{(n)}(a^{(k)})\to T\), then by (2.2) every entry sequence \(\pi(a^{(k)}_{ij})\) is Cauchy. As \(\pi\) is isometric, \(\pi(A)\) is complete, so the sequence converges to some \(\pi(a_{ij})\), and then \(\pi^{(n)}(a^{(k)})\to\pi^{(n)}(a)\) by (2.2), so \(T\in D\). Thus \(D\) is a C\(^*\)-subalgebra of \(B(H^n)\), and \(\|\cdot\|\) makes \(M_n(A)\) a C\(^*\)-algebra. If \(\|\cdot\|'\) is another such norm, the identity map from \((M_n(A),\|\cdot\|)\) to \((M_n(A),\|\cdot\|')\) is an injective \(*\)-homomorphism between C\(^*\)-algebras, hence isometric by (B3). So the norm is unique, and in particular it does not depend on \(\pi\).

(3) The first claim is (1) combined with (2). For \(\sigma\), the algebraic identities are those of (1), and injectivity is checked entry by entry.

(4) A faithful representation of \(A\) restricts to a faithful representation of \(B\). By (2), the norm of \(M_n(B)\) is the restriction of that of \(M_n(A)\), and \(M_n(B)\) is complete, hence closed. The claim about positive elements is (P1).

(5) By (1) with \(\pi=\mathrm{id}_{B(H)}\), the map is an injective \(*\)-homomorphism onto \(B(H^n)\), isometric by (B3). For \(T=\sum R_iX_{ij}R_j^*\) we have \(\langle T\zeta,\zeta\rangle=\sum_{i,j}\langle X_{ij}\zeta_j,\zeta_i\rangle\); now use (P2).

(6) On \(\ell^2(\Omega)\), with orthonormal basis \((\delta_\omega)\), the operators \(\pi(f)\delta_\omega=f(\omega)\delta_\omega\) form a faithful representation of \(C_0(\Omega)\). After the unitary that regroups \(\ell^2(\Omega)^n\) as \(\bigoplus_\omega\mathbb C^n\), \(\pi^{(n)}(F)\) becomes the block-diagonal operator \(\bigoplus_\omega F(\omega)\). Its norm is \(\sup_\omega\|F(\omega)\|\), and it is positive exactly when every block is. Now apply (2) and (P1).

(7) Take a faithful \(\pi\) on \(H\) and let \(\alpha\otimes1:H^m\to H^n\) be \((\alpha\otimes1)\zeta=(\sum_q\alpha_{iq}\zeta_q)_i\). Then \(R_i^*(\alpha\otimes1)R_q=\alpha_{iq}1\), so the \((p,q)\) entry of \((\alpha\otimes1)^*\pi^{(n)}(a)(\alpha\otimes1)\) is \(\sum_{i,j}\overline{\alpha_{ip}}\alpha_{jq}\pi(a_{ij})=\pi((\alpha^*a\alpha)_{pq})\). Hence \(\pi^{(m)}(\alpha^*a\alpha)=(\alpha\otimes1)^*\pi^{(n)}(a)(\alpha\otimes1)\), which is positive when \(\pi^{(n)}(a)\) is. By (1) and (P1), \(\alpha^*a\alpha\ge0\). For the special cases take for \(\alpha\) a coordinate inclusion \(\mathbb C^m\to\mathbb C^n\), the matrix \([1_n\ 0]\), or a permutation matrix. \(\square\)

**Lemma 2.2** (The positive cone of \(M_n(A)\)).

1. For \(a_1,\dots,a_n\in A\), the matrix \([a_i^*a_j]\) is positive. Each positive element of \(M_n(A)\) can be written as the sum of \(n\) such matrices.
2. \(a\in M_n(A)\) is positive exactly when \(\sum_{i,j}x_i^*a_{ij}x_j\ge0\) in \(A\) for all \(x_1,\dots,x_n\in A\).
3. Let \(\pi\) be a representation of \(A\) on \(H\). If \(a\ge0\), then \(\sum_{i,j}\langle\pi(a_{ij})\zeta_j,\zeta_i\rangle\ge0\) for all \(\zeta\in H^n\). If \(\pi\) is faithful, the converse holds.
4. (*Two-by-two test.*) Let \(x,y\in B(H)\) and \(t>0\). The operator \(\begin{bmatrix}t1&x\\x^*&y\end{bmatrix}\) on \(H\oplus H\) is positive if and only if \(y\ge t^{-1}x^*x\).

**Proof.** (1) Let \(c\in M_n(A)\) have first row \((a_1,\dots,a_n)\) and all other rows zero. Then \((c^*c)_{ij}=\sum_k(c_{ki})^*c_{kj}=a_i^*a_j\), so \([a_i^*a_j]=c^*c\ge0\). Conversely, let \(a\ge0\) and write \(a=b^*b\) (B1). Then \(a_{ij}=\sum_kb_{ki}^*b_{kj}\), so \(a=\sum_{k=1}^n[b_{ki}^*b_{kj}]_{i,j}\), one summand for each row of \(b\).

(2) If \(a=\sum_k[b_{ki}^*b_{kj}]_{i,j}\), then \(\sum_{i,j}x_i^*a_{ij}x_j=\sum_kw_k^*w_k\) with \(w_k=\sum_jb_{kj}x_j\), which is positive. Conversely, assume the condition. Let \(f\) be a positive functional on \(A\) with GNS triple \((\pi_f,H_f,\xi_f)\) (B8). For \(x_1,\dots,x_n\in A\) and \(\zeta=(\pi_f(x_1)\xi_f,\dots,\pi_f(x_n)\xi_f)\),
\[
\begin{gathered}
\langle\pi_f^{(n)}(a)\zeta,\zeta\rangle \\
=\sum_{i,j}\langle\pi_f(x_i^*a_{ij}x_j)\xi_f,\xi_f\rangle \\
=f\Bigl(\sum_{i,j}x_i^*a_{ij}x_j\Bigr)\ge0.
\end{gathered}
\]
These \(\zeta\) are dense in \(H_f^n\), because \(\pi_f(A)\xi_f\) is dense in \(H_f\) and the coordinates can be chosen independently. So \(\pi_f^{(n)}(a)\ge0\) by (P2). Let \(\pi\) be the direct sum of the \(\pi_f\) over all positive functionals \(f\). Up to regrouping the summands, \(\pi^{(n)}(a)\) is the direct sum of the \(\pi_f^{(n)}(a)\), so it is positive. And \(\pi\) is faithful, because for each nonzero \(b\in A\) some positive functional \(f_b\) has \(\pi_{f_b}(b)\ne0\) (B9). So \(\pi^{(n)}\) is injective by Proposition 2.1(1), and \(a\ge0\) by (P1).

(3) \(\pi^{(n)}\) is a \(*\)-homomorphism, so \(a=c^*c\) gives \(\pi^{(n)}(a)=\pi^{(n)}(c)^*\pi^{(n)}(c)\ge0\), and \(\langle\pi^{(n)}(a)\zeta,\zeta\rangle\) is the given sum. For faithful \(\pi\), the converse is (P2) followed by (P1).

(4) Write \(S\) for the operator. For \((\xi,\eta)\in H\oplus H\),
\[
\langle S(\xi,\eta),(\xi,\eta)\rangle=t\|\xi\|^2+2\,\mathrm{Re}\,\langle x\eta,\xi\rangle+\langle y\eta,\eta\rangle .
\]
If \(S\ge0\), take \(\xi=-t^{-1}x\eta\); the right side becomes \(\langle y\eta,\eta\rangle-t^{-1}\|x\eta\|^2\), so \(y\ge t^{-1}x^*x\). Conversely, let \(R:H\oplus H\to H\) be \(R(\xi,\eta)=t^{1/2}\xi+t^{-1/2}x\eta\). Then \(R^*R=\begin{bmatrix}t1&x\\x^*&t^{-1}x^*x\end{bmatrix}\), and \(S=R^*R+\bigl(0\oplus(y-t^{-1}x^*x)\bigr)\), a sum of two positive operators. \(\square\)

## 3. Completely positive maps

**Definition 3.1.** Let \(A,B\) be C\(^*\)-algebras and \(\varphi:A\to B\) linear. Its \(n\)-th amplification \(\varphi^{(n)}:M_n(A)\to M_n(B)\) applies \(\varphi\) to every entry. The map \(\varphi\) is *\(n\)-positive* if \(\varphi^{(n)}\) maps positive elements to positive elements, and *completely positive* (CP) if it is \(n\)-positive for every \(n\). *Positive* means 1-positive.

**Proposition 3.2.**

1. (*A criterion.*) \(\varphi\) is \(n\)-positive exactly when
\[
\begin{gathered}
\sum_{i,j=1}^ny_i^*\,\varphi(x_i^*x_j)\,y_j\ge0, \\
\text{for all }x_1,\dots,x_n\in A, \\
y_1,\dots,y_n\in B.
\end{gathered}
\tag{3.1}
\]
If \(B\subseteq B(H)\), this holds if and only if \(\sum_{i,j}\langle\varphi(x_i^*x_j)\zeta_j,\zeta_i\rangle\ge0\) for all \(x\in A^n\) and \(\zeta\in H^n\).
2. An \(n\)-positive map is \(k\)-positive for every \(k\le n\). A positive map is hermitian: \(\varphi(x^*)=\varphi(x)^*\). If \(\psi:B\to C\) is \(n\)-positive too, so is \(\psi\circ\varphi\), because \((\psi\circ\varphi)^{(n)}=\psi^{(n)}\circ\varphi^{(n)}\).
3. (*Examples.*) Every \(*\)-homomorphism is CP. For \(V\in B(H,K)\), the map \(y\mapsto V^*yV\) from \(B(K)\) to \(B(H)\) is CP. The transpose \(t(x)=x^{\mathsf T}\) on \(M_d(\mathbb C)\), \(d\ge2\), is positive but not 2-positive.
4. (*Automatic boundedness.*) A positive map \(\varphi:A\to B\) is bounded, and
\[
\|\varphi\|\le4\sup\{\|\varphi(a)\|:\ a\in A_+,\ \|a\|\le1\}.
\]

**Proof.** (1) Let \(\varphi\) be \(n\)-positive. The matrix \([x_i^*x_j]\) is positive by Lemma 2.2(1), so \([\varphi(x_i^*x_j)]\ge0\), and Lemma 2.2(2), applied in \(M_n(B)\), gives (3.1). Conversely, assume (3.1). By Lemma 2.2(2) in \(M_n(B)\), \([\varphi(x_i^*x_j)]\ge0\) for every \(x\in A^n\). By Lemma 2.2(1), every positive element of \(M_n(A)\) is a finite sum of such matrices \([x_i^*x_j]\); \(\varphi^{(n)}\) is additive, and \(M_n(B)_+\) is a convex cone. For the second form, \([\varphi(x_i^*x_j)]\) is positive in \(M_n(B)\) exactly when it is positive in \(M_n(B(H))\) (Proposition 2.1(4)), that is, when the stated quadratic form is nonnegative (Proposition 2.1(5)).

(2) For \(X\in M_k(A)_+\), \(X\oplus0\in M_n(A)_+\) by Proposition 2.1(7), and \(\varphi^{(n)}(X\oplus0)=\varphi^{(k)}(X)\oplus0\). Its corner \(\varphi^{(k)}(X)\) is positive by Proposition 2.1(7) again. If \(h\in A_h\), then \(\varphi(h)=\varphi(h_+)-\varphi(h_-)\) is self-adjoint; for \(x=h+ik\), \(\varphi(x^*)=\varphi(h)-i\varphi(k)=\varphi(x)^*\). The rule for compositions holds entry by entry.

(3) A \(*\)-homomorphism \(\sigma\) has \(*\)-homomorphic amplifications (Proposition 2.1(3)), and \(\sigma^{(n)}(c^*c)=\sigma^{(n)}(c)^*\sigma^{(n)}(c)\). For \(y\mapsto V^*yV\), the amplification is \(Y\mapsto(V\otimes1)^*Y(V\otimes1)\) on \(B(K^n)=M_n(B(K))\) (Proposition 2.1(5)), where \((V\otimes1)(\zeta_j)_j=(V\zeta_j)_j\); this preserves positivity. For the transpose: if \(x=y^*y\), then \(x^{\mathsf T}=y^{\mathsf T}\bar y=(\bar y)^*\bar y\ge0\), where \(\bar y\) has the conjugate entries. Now let \(E=[e_{ij}]_{i,j=1,2}\in M_2(M_d(\mathbb C))\). It equals \([e_{1i}^*e_{1j}]\), so \(E\ge0\) by Lemma 2.2(1). Its image is \(t^{(2)}(E)=[e_{ji}]_{i,j}\). For \(\zeta=(\varepsilon_2,-\varepsilon_1)\in\mathbb C^d\oplus\mathbb C^d\),
\[
\begin{gathered}
\sum_{i,j=1}^2\langle e_{ji}\zeta_j,\zeta_i\rangle \\
=\langle e_{11}\varepsilon_2,\varepsilon_2\rangle-\langle e_{21}\varepsilon_1,\varepsilon_2\rangle \\
-\langle e_{12}\varepsilon_2,\varepsilon_1\rangle+\langle e_{22}\varepsilon_1,\varepsilon_1\rangle \\
=0-1-1+0=-2.
\end{gathered}
\]
So \(t^{(2)}(E)\) is not positive, by Proposition 2.1(5).

(4) Let \(M\) be the supremum on the right, and suppose \(M=\infty\). Choose \(a_k\in A_+\) with \(\|a_k\|\le1\) and \(\|\varphi(a_k)\|\ge4^k\). The series \(a=\sum_k2^{-k}a_k\) converges, and \(a-2^{-k}a_k\) is a limit of positive partial sums, so \(a\ge2^{-k}a_k\ge0\) (\(A_+\) is closed). Hence \(\varphi(a)\ge2^{-k}\varphi(a_k)\ge0\), and by (P2), \(\|\varphi(a)\|\ge2^{-k}\|\varphi(a_k)\|\ge2^k\) for every \(k\), which is absurd. So \(M<\infty\). A contraction \(x\) is a combination \(h_+-h_-+i(k_+-k_-)\) of four positive contractions (Section 1), so \(\|\varphi(x)\|\le4M\). \(\square\)

The argument for (4) is the usual proof that positive functionals are bounded, carried out for maps; it also gives the explicit bound. Proposition 7.1(5) extends (4) to maps into dual spaces.

**Exercise 3.3** (medium; Choi's criterion). Let \(\varphi:M_k(\mathbb C)\to B\) be linear. Show that the following are equivalent: (a) \(\varphi\) is CP; (b) \(\varphi\) is \(k\)-positive; (c) the matrix \(C_\varphi=[\varphi(e_{ij})]_{i,j=1}^k\in M_k(B)\) is positive. Compute \(C_t\) for the transpose.

*Solution.* (a)\(\Rightarrow\)(b) is clear. (b)\(\Rightarrow\)(c): \([e_{ij}]=[e_{1i}^*e_{1j}]\) is positive by Lemma 2.2(1), and \(C_\varphi=\varphi^{(k)}([e_{ij}])\). (c)\(\Rightarrow\)(a): let \(x_1,\dots,x_m\in M_k(\mathbb C)\) and \(y_1,\dots,y_m\in B\). Since \(x_p^*x_q=\sum_{i,j,l}\overline{(x_p)_{li}}\,(x_q)_{lj}\,e_{ij}\),
\[
\begin{gathered}
\sum_{p,q}y_p^*\varphi(x_p^*x_q)y_q \\
=\sum_{l=1}^k\sum_{i,j=1}^kz_{li}^*\,\varphi(e_{ij})\,z_{lj}, \\
z_{lj}=\sum_q(x_q)_{lj}\,y_q.
\end{gathered}
\]
For each \(l\), the inner sum is nonnegative by Lemma 2.2(2) applied to \(C_\varphi\ge0\) in \(M_k(B)\). So (3.1) holds for every \(m\), and \(\varphi\) is CP. For the transpose on \(M_2(\mathbb C)\), \(C_t=[e_{ji}]_{i,j}\), which is the operator on \(\mathbb C^2\oplus\mathbb C^2\) that exchanges the two tensor factors of \(\mathbb C^2\otimes\mathbb C^2\); it has eigenvalue \(-1\) on \(\varepsilon_1\otimes\varepsilon_2-\varepsilon_2\otimes\varepsilon_1\), so it is not positive. This is the computation of Proposition 3.2(3) again. The equivalence (a)\(\Leftrightarrow\)(b) is also the case "\(\Omega\) a point" of Theorem 5.4(1).

## 4. The Kadison–Schwarz inequality

**Theorem 4.1.** Let \(\varphi:A\to B\) be 2-positive.

1. (*The Kadison–Schwarz inequality.*) \(\varphi(a)^*\varphi(a)\le\|\varphi\|\,\varphi(a^*a)\) for all \(a\in A\).
2. \[
\begin{gathered}
\|\varphi\|\\
=\sup\{\|\varphi(b)\|:\ b\in A_+,\ \|b\|\le1\}\\
=\lim_i\|\varphi(u_i)\|
\end{gathered}
\] for every approximate identity \((u_i)\). If \(A\) has a unit, \(\|\varphi\|=\|\varphi(1)\|\).
3. (*Multiplicative domain.*) Let \(\|\varphi\|\le1\). If \(\varphi(a^*a)=\varphi(a)^*\varphi(a)\), then \(\varphi(xa)=\varphi(x)\varphi(a)\) for all \(x\in A\). If \(\varphi(aa^*)=\varphi(a)\varphi(a)^*\), then \(\varphi(ax)=\varphi(a)\varphi(x)\) for all \(x\in A\).
4. Positivity alone does not give (1). For the transpose \(t\) on \(M_2(\mathbb C)\), \(\|t\|=1\), but \(t(e_{12})^*t(e_{12})=e_{11}\) is not below \(t(e_{12}^*e_{12})=e_{22}\).



**Proof.** Represent \(B\) faithfully on \(H\); by (P1) we may compute with operators. (1) Let \(a\in A\) and \(R_i=\begin{bmatrix}u_i&a\\0&0\end{bmatrix}\in M_2(A)\). Then \(R_i^*R_i=\begin{bmatrix}u_i^2&u_ia\\a^*u_i&a^*a\end{bmatrix}\ge0\), so
\[
\begin{bmatrix}\varphi(u_i^2)&\varphi(u_ia)\\\varphi(u_ia)^*&\varphi(a^*a)\end{bmatrix}\ge0 ,
\]
using \(\varphi(a^*u_i)=\varphi(u_ia)^*\) (Proposition 3.2(2)). Since \(0\le\varphi(u_i^2)\le\|\varphi\|1\) by (P2), adding \((\|\varphi\|1-\varphi(u_i^2))\oplus0\ge0\) gives \(\begin{bmatrix}\|\varphi\|1&\varphi(u_ia)\\\varphi(u_ia)^*&\varphi(a^*a)\end{bmatrix}\ge0\). If \(\varphi=0\) there is nothing to prove. Otherwise the two-by-two test, Lemma 2.2(4), gives \(\varphi(u_ia)^*\varphi(u_ia)\le\|\varphi\|\,\varphi(a^*a)\). Now let \(i\to\infty\): \(u_ia\to a\), \(\varphi\) is bounded, and the positive cone is closed.

(2) Let \(s=\sup\{\|\varphi(b)\|:b\in A_+,\|b\|\le1\}\). For \(\|a\|\le1\), (1) and (P2) give \[
\begin{gathered}
\|\varphi(a)\|^2\\
=\|\varphi(a)^*\varphi(a)\|\\
\le\|\varphi\|\,\|\varphi(a^*a)\|\\
\le\|\varphi\|s,
\end{gathered}
\] so \(\|\varphi\|\le s\). For \(b\in A_+\) with \(\|b\|\le1\), in a faithful representation of \(A\) we have \(u_ibu_i\le u_i^2\le u_i\), so \(\|\varphi(u_ibu_i)\|\le\|\varphi(u_i)\|\) by positivity and (P2). As \(u_ibu_i\to b\), \(\|\varphi(b)\|\le\sup_i\|\varphi(u_i)\|\). Thus \(\|\varphi\|\le s\le\sup_i\|\varphi(u_i)\|\le\|\varphi\|\). The norms \(\|\varphi(u_i)\|\) increase, so the supremum is a limit. With a unit, \(0\le\varphi(b)\le\varphi(1)\) for \(0\le b\le1\), so \(s=\|\varphi(1)\|\).

(3) By (1) and \(\|\varphi\|\le1\), \(\varphi(y)^*\varphi(y)\le\varphi(y^*y)\) for every \(y\). Take \(y=a+tw\) with \(w\in A\) and \(t\) real. Expanding and using \(\varphi(a^*a)=\varphi(a)^*\varphi(a)\),
\[
\begin{gathered}
0\le\varphi(y^*y)-\varphi(y)^*\varphi(y) \\
=t\,(S+S^*)+t^2E, \\
S=\varphi(a^*w)-\varphi(a)^*\varphi(w), \\
E=\varphi(w^*w)-\varphi(w)^*\varphi(w),
\end{gathered}
\]
where \(\varphi(w^*a)-\varphi(w)^*\varphi(a)=S^*\) because \(\varphi\) is hermitian. Divide by \(|t|\) and let \(t\to0\) from each side: \(S+S^*\ge0\) and \(-(S+S^*)\ge0\), so \(S+S^*=0\). Replacing \(w\) by \(iw\) replaces \(S\) by \(iS\), so \(i(S-S^*)=0\) as well. Hence \(S=0\): \(\varphi(a^*w)=\varphi(a)^*\varphi(w)\) for all \(w\). Taking adjoints and writing \(x=w^*\) gives \(\varphi(xa)=\varphi(x)\varphi(a)\). For the second statement apply the first to \(a^*\), for which \(\varphi(a)=\varphi(a^*)^*\) turns the hypothesis into \(\varphi((a^*)^*a^*)=\varphi(a^*)^*\varphi(a^*)\); this gives \(\varphi(xa^*)=\varphi(x)\varphi(a^*)\) for all \(x\), and taking adjoints gives \(\varphi(ax^*)=\varphi(a)\varphi(x^*)\) for all \(x\), which is the claim.

(4) \(e_{12}^*e_{12}=e_{22}\) and \(t(e_{22})=e_{22}\), while \(t(e_{12})^*t(e_{12})=e_{21}^*e_{21}=e_{12}e_{21}=e_{11}\), and \(e_{22}-e_{11}\) is not positive. The transpose is isometric, since \(x^{\mathsf T}\) is the adjoint of the entrywise conjugate of \(x\), and entrywise conjugation is implemented by the conjugation of \(\mathbb C^2\). \(\square\)

*Remarks.* The two-by-two argument needs no dilation. For completely positive maps, (1) also follows from Stinespring's theorem; see the remark after Theorem 6.1. The case of positive maps and normal elements, Kadison's inequality, is Corollary 5.5. Part (3) is used in Exercise 4.3.

### Jordan homomorphisms

**Exercise 4.2** (easy; Amplification detects multiplicativity). Call a linear map \(\pi:A\to B\) between C\(^*\)-algebras a *Jordan \(*\)-homomorphism* if \(\pi(x^*)=\pi(x)^*\) for all \(x\) and \(\pi(h^2)=\pi(h)^2\) for self-adjoint \(h\). Let \(\pi:A\to B\) be linear and \(n\ge2\), and suppose that \(\pi^{(n)}=\pi\otimes\mathrm{id}_{M_n}:M_n(A)\to M_n(B)\) is a Jordan \(*\)-homomorphism. Show that \(\pi\) is a \(*\)-homomorphism; in particular, if \(\pi\) is bijective, it is a \(*\)-isomorphism. Show that the statement fails for \(n=1\).

*Solution.* First, \(\pi^{(n)}(Z^2)=\pi^{(n)}(Z)^2\) for every \(Z\in M_n(A)\), not only for self-adjoint \(Z\). Indeed, write \(Z=H+iK\) with \(H,K\) self-adjoint. Then \(Z^2=H^2-K^2+i\bigl((H+K)^2-H^2-K^2\bigr)\), each square on the right is a square of a self-adjoint matrix, and the same identity holds for \(\pi^{(n)}(Z)=\pi^{(n)}(H)+i\pi^{(n)}(K)\), whose parts \(\pi^{(n)}(H)\), \(\pi^{(n)}(K)\) are self-adjoint. Now let \(x,y\in A\) and \(Z=xe_{12}+ye_{21}\), the matrix with \(x\) in place \((1,2)\), \(y\) in place \((2,1)\), and zeros elsewhere; this uses \(n\ge2\). Then \(Z^2=xy\,e_{11}+yx\,e_{22}\) and \(\pi^{(n)}(Z)^2=\pi(x)\pi(y)e_{11}+\pi(y)\pi(x)e_{22}\). Comparing the \((1,1)\) entries gives \(\pi(xy)=\pi(x)\pi(y)\). Comparing the \((1,1)\) entries of \(\pi^{(n)}((xe_{11})^*)=\pi^{(n)}(xe_{11})^*\) gives \(\pi(x^*)=\pi(x)^*\). So \(\pi\) is a \(*\)-homomorphism. For \(n=1\), the transpose \(t\) on \(M_2(\mathbb C)\) is a bijective Jordan \(*\)-homomorphism, since \((h^{\mathsf T})^2=(h^2)^{\mathsf T}\) and \((x^*)^{\mathsf T}=(x^{\mathsf T})^*\), but \(t(e_{12}e_{21})=t(e_{11})=e_{11}\), while \(t(e_{12})t(e_{21})=e_{21}e_{12}=e_{22}\).

*Remarks.* Only the corner \(M_2\) is used, so \(n=2\) is the whole content. For the transpose, \(t^{(2)}\) is not even positive (Proposition 3.2(3)), while a Jordan \(*\)-homomorphism is positive, as \(\pi(h^2)=\pi(h)^2\ge0\). Exercise 4.3 gives an order-theoretic version.

**Exercise 4.3** (medium; Jordan maps that are 2-positive). Let \(\pi:A\to B\) be a Jordan \(*\)-homomorphism (Exercise 4.2). Show that \(\pi\) is positive and contractive on self-adjoint elements, and that \(\pi\) is a \(*\)-homomorphism exactly when it is 2-positive.

*Solution.* Every positive element is \(h^2\) with \(h\) self-adjoint (B1), and \(\pi(h^2)=\pi(h)^2\ge0\); so \(\pi\) is positive and hence bounded (Proposition 3.2(4)). For self-adjoint \(h\) and \(m\ge1\), induction on \(m\) gives \(\pi(h^{2^m})=\pi(h)^{2^m}\), so \(\|\pi(h)\|^{2^m}=\|\pi(h^{2^m})\|\le\|\pi\|\,\|h\|^{2^m}\), using \(\|y^2\|=\|y\|^2\) for self-adjoint \(y\). Taking \(2^m\)-th roots and letting \(m\to\infty\) gives \(\|\pi(h)\|\le\|h\|\). A \(*\)-homomorphism is CP (Proposition 3.2(3)). Conversely, let \(\pi\) be 2-positive. By Theorem 4.1(2), \(\|\pi\|=\lim_i\|\pi(u_i)\|\le1\), because the \(u_i\) are self-adjoint contractions. By Theorem 4.1(1), \(\pi(x)^*\pi(x)\le\pi(x^*x)\) and \(\pi(x)\pi(x)^*\le\pi(xx^*)\) for all \(x\). For \(x=h+ik\) with \(h,k\) self-adjoint, \(x^*x+xx^*=2(h^2+k^2)\), and likewise \[
\begin{gathered}
\pi(x)^*\pi(x)+\pi(x)\pi(x)^*\\
=2(\pi(h)^2+\pi(k)^2)\\
=2\pi(h^2+k^2).
\end{gathered}
\] So \(\pi(x^*x+xx^*)=\pi(x)^*\pi(x)+\pi(x)\pi(x)^*\). The two nonnegative differences therefore add up to \(0\), so both vanish: \(\pi(x^*x)=\pi(x)^*\pi(x)\) for all \(x\). By Theorem 4.1(3), \(\pi(yx)=\pi(y)\pi(x)\) for all \(x,y\). Together with \(\pi(x^*)=\pi(x)^*\), \(\pi\) is a \(*\)-homomorphism. The transpose on \(M_2(\mathbb C)\) shows that 2-positivity cannot be dropped.

## 5. When positivity implies complete positivity

The transpose shows that a positive map need not be 2-positive. This section shows that positivity is enough when the target or the domain is commutative, and that \(k\)-positivity is enough when the target has a separating family of representations of dimension at most \(k\), or when the domain is \(C_0(\Omega,M_k)\).

### Commutative targets, and targets with small representations

**Theorem 5.1.**

1. If \(B\) is abelian, every positive linear map \(\varphi:A\to B\) is completely positive. In particular, every positive linear functional is completely positive.
2. A \(k\)-positive map \(\psi:A\to M_k(\mathbb C)\) is completely positive.
3. Let \(n\ge1\), and let \(B\) have a separating family of representations \(\sigma_\alpha\) on spaces of dimension at most \(n\) (for every \(b\ne0\) some \(\sigma_\alpha(b)\ne0\)). Then every \(n\)-positive map \(\varphi:A\to B\) is completely positive. Since the irreducible representations of \(B\) separate its points (B9), this applies whenever every irreducible representation of \(B\) has dimension at most \(n\).

*Further reading:* [Blackadar, II.6.9.10]. The proof below needs only a separating family of representations of dimension at most \(n\).

**Proof.** (1) By the commutative Gelfand–Naimark theorem (B5), the Gelfand transform identifies \(B\) with \(C_0(\Omega)\) by an isometric \(*\)-isomorphism, where \(\Omega\) is the space of characters of \(B\). So an element \(b\in B\) is positive exactly when \(\chi(b)\ge0\) for every character \(\chi\), because positivity in \(C_0(\Omega)\) is pointwise (Proposition 2.1(6) with \(n=1\)) and the isomorphism preserves and reflects positivity (P1). A character is positive, since \(\chi(b^*b)=|\chi(b)|^2\), so \(\chi\circ\varphi\) is a positive functional on \(A\). For \(x\in A^n\), \(y\in B^n\) and a character \(\chi\), put \(w=\sum_j\chi(y_j)x_j\). Then
\[
\begin{gathered}
\chi\Bigl(\sum_{i,j}y_i^*\varphi(x_i^*x_j)y_j\Bigr) \\
=\sum_{i,j}\overline{\chi(y_i)}\,\chi(y_j)\,(\chi\circ\varphi)(x_i^*x_j) \\
=(\chi\circ\varphi)(w^*w)\ge0.
\end{gathered}
\]
So (3.1) holds for every \(n\). For a functional, take \(B=\mathbb C\).

(2) By Proposition 3.2(1), \(\psi\) is \(m\)-positive exactly when \(\sum_{p,q=1}^m\langle\psi(x_p^*x_q)\zeta_q,\zeta_p\rangle\ge0\) for all \(x\in A^m\) and \(\zeta\in(\mathbb C^k)^m\). Write \(\zeta_q=\sum_{s=1}^kc_{qs}\varepsilon_s\) and put \(w_t=\sum_qc_{qt}x_q\) for \(t=1,\dots,k\). Then \(w_s^*w_t=\sum_{p,q}\overline{c_{ps}}\,c_{qt}\,x_p^*x_q\), and
\[
\sum_{p,q=1}^m\langle\psi(x_p^*x_q)\zeta_q,\zeta_p\rangle=\sum_{s,t=1}^k\langle\psi(w_s^*w_t)\varepsilon_t,\varepsilon_s\rangle ,
\]
which is nonnegative by \(k\)-positivity. So \(m\) terms reduce to \(k\) terms.

(3) Let \(\sigma_\alpha\) act on \(K_\alpha\), with \(k_\alpha=\dim K_\alpha\le n\), and identify \(B(K_\alpha)\) with \(M_{k_\alpha}(\mathbb C)\). The \(*\)-homomorphism \(\sigma_\alpha\) is completely positive, so \(\sigma_\alpha\circ\varphi\) is \(n\)-positive (Proposition 3.2(2)–(3)); hence it is \(k_\alpha\)-positive, and completely positive by (2). The direct sum \(\sigma=\bigoplus_\alpha\sigma_\alpha\) is faithful, because the family separates points. For \(X\in M_m(A)_+\), after regrouping \((\bigoplus_\alpha K_\alpha)^m\) as \(\bigoplus_\alpha K_\alpha^m\), the operator \(\sigma^{(m)}(\varphi^{(m)}(X))\) is \(\bigoplus_\alpha(\sigma_\alpha\circ\varphi)^{(m)}(X)\), which is positive. Since \(\sigma^{(m)}\) is injective (Proposition 2.1(1)) and an injective \(*\)-homomorphism reflects positivity (P1), \(\varphi^{(m)}(X)\ge0\). Finally, for every nonzero \(b\) there is an irreducible representation \(\sigma_b\) with \(\sigma_b(b)\ne0\) (B9); these form a separating family. \(\square\)

*Remarks.* (i) Part (1) is also the case \(n=1\) of (3): by (B5) the characters of an abelian \(B\) are a separating family of representations on \(\mathbb C\). (ii) For \(n=2\) the hypothesis in (3) cannot be weakened to positivity: \(M_2(\mathbb C)\) has its identity representation, of dimension 2, and the transpose is a positive map into \(M_2(\mathbb C)\) that is not CP (Proposition 3.2(3)).

### Domains of the form \(C_0(\Omega,M_k)\)

Throughout this subsection, \(\Omega\) is a locally compact Hausdorff space.

**Lemma 5.2** (Partitions of unity). Let \(C\subseteq\Omega\) be compact and \(U_1,\dots,U_L\) open sets covering \(C\). There are \(g_1,\dots,g_L\in C_c(\Omega)\) with \(g_l\ge0\), \(g_l=0\) off \(U_l\), \(\sum_lg_l\le1\) on \(\Omega\), and \(\sum_lg_l=1\) on \(C\).

**Proof.** For each \(\omega\in C\) pick \(l(\omega)\) with \(\omega\in U_{l(\omega)}\), and an open \(W_\omega\ni\omega\) whose closure is compact and lies in \(U_{l(\omega)}\); such a set exists by the existence of neighbourhoods with compact closure (B12). Finitely many \(W_\omega\) cover \(C\). Let \(C_l\) be the union of the closures of the chosen \(W_\omega\) with \(l(\omega)=l\); it is compact and lies in \(U_l\). The locally compact form of Urysohn's lemma (B12), applied to \(C_l\) and the closed set \(\Omega\setminus U_l\), gives \(h_l\in C_c(\Omega)\) with \(0\le h_l\le1\), \(h_l=1\) on \(C_l\) and \(h_l=0\) off \(U_l\). Put \(g_1=h_1\) and \(g_l=(1-h_1)\cdots(1-h_{l-1})h_l\). Then \(0\le g_l\le h_l\), and by induction \(\sum_{l\le L}g_l=1-\prod_{l\le L}(1-h_l)\), which lies in \([0,1]\) and equals \(1\) on \(C\), since every point of \(C\) lies in some \(C_l\). \(\square\)

**Lemma 5.3** (Approximation). Let \(F:\Omega\to M_N(\mathbb C)\) be continuous and vanish at infinity, and let \(\varepsilon>0\). There are points \(\omega_1,\dots,\omega_L\) and functions \(g_1,\dots,g_L\) as in Lemma 5.2 with
\[
\sup_{\omega\in\Omega}\Bigl\|F(\omega)-\sum_lg_l(\omega)F(\omega_l)\Bigr\|\le2\varepsilon .
\]

**Proof.** The set \(C=\{\omega:\|F(\omega)\|\ge\varepsilon\}\) is compact; if it is empty, take \(L=0\). For \(p\in C\), the set \(U_p=\{\omega:\|F(\omega)-F(p)\|<\varepsilon\}\) is an open neighbourhood of \(p\). Choose \(p_1,\dots,p_L\) with \(C\subseteq\bigcup_lU_{p_l}\), take \(g_l\) from Lemma 5.2, and put \(\omega_l=p_l\). For every \(\omega\),
\[
\begin{gathered}
F(\omega)-\sum_lg_l(\omega)F(\omega_l) \\
=\Bigl(1-\sum_lg_l(\omega)\Bigr)F(\omega) \\
+\sum_lg_l(\omega)\bigl(F(\omega)-F(\omega_l)\bigr).
\end{gathered}
\]
The first term vanishes on \(C\) and has norm less than \(\varepsilon\) off \(C\). In the second, \(g_l(\omega)\ne0\) forces \(\omega\in U_{p_l}\), so its norm is at most \(\sum_lg_l(\omega)\varepsilon\le\varepsilon\). \(\square\)

**Theorem 5.4.**

1. Let \(k\ge1\). Every \(k\)-positive map \(\varphi\) from \(A=M_k(C_0(\Omega))=C_0(\Omega,M_k)\) into a C\(^*\)-algebra \(B\) is completely positive.
2. In particular, every positive map from an abelian C\(^*\)-algebra into a C\(^*\)-algebra is completely positive (\(k=1\)), and every \(k\)-positive map from \(M_k(\mathbb C)\) is completely positive (\(\Omega\) a point).

The proof below uses finite partitions of unity and scalar matrix compressions; it makes no point-dependent choice outside exceptional null sets.

**Proof.** (1) Let \(m\ge1\). By Lemma 2.2(1) it suffices to show \(\varphi^{(m)}(X)\ge0\) for \(X=[x_p^*x_q]_{p,q=1}^m\) with \(x_p\in A\). Identify \(M_m(A)\) with \(C_0(\Omega,M_{mk})\); by Proposition 2.1(6), with \(n=mk\), its norm is the supremum norm. The function \(\omega\mapsto X(\omega)=[x_p(\omega)^*x_q(\omega)]\) is continuous and vanishes at infinity. Fix \(\varepsilon>0\), take \(\omega_l\) and \(g_l\) from Lemma 5.3, and put \(G=\sum_lg_l\,X(\omega_l)\in M_m(A)\), where each scalar matrix \(X(\omega_l)\) is multiplied by the function \(g_l\). Then \(\|X-G\|\le2\varepsilon\).

We show \(\varphi^{(m)}(G)\ge0\). Fix \(l\), and write \(g=g_l\) and \(c_p=x_p(\omega_l)\in M_k(\mathbb C)\). Since \(\sum_re_{r1}e_{1r}=1\), we have \(c_p^*c_q=\sum_{r=1}^k(e_{1r}c_p)^*(e_{1r}c_q)\), so
\[
\begin{gathered}
g\,X(\omega_l)=\sum_{r=1}^k[w_{rp}^*w_{rq}]_{p,q}, \\
w_{rp}=g^{1/2}e_{1r}c_p\in A.
\end{gathered}
\]
For fixed \(r\), every \(w_{rp}\) is a combination of the \(k\) elements \(v_s=g^{1/2}e_{1s}\): \(w_{rp}=\sum_s\beta_{ps}v_s\), where \(\beta_{ps}\) is the \((r,s)\) entry of \(c_p\). Hence \([w_{rp}^*w_{rq}]_{p,q}=\alpha^*[v_s^*v_t]_{s,t}\,\alpha\) in the notation of Proposition 2.1(7), with \(\alpha\in M_{k,m}(\mathbb C)\), \(\alpha_{tq}=\beta_{qt}\). Now \(\varphi^{(m)}(\alpha^*T\alpha)=\alpha^*\varphi^{(k)}(T)\alpha\) for every \(T\in M_k(A)\), since both sides are linear in \(T\) and agree entry by entry. The matrix \([v_s^*v_t]\) is positive (Lemma 2.2(1)), \(\varphi^{(k)}\) preserves positivity, and so does \(\alpha^*(\cdot)\alpha\) (Proposition 2.1(7)). So each piece of \(G\) has positive image, and \(\varphi^{(m)}(G)\ge0\).

Finally, \(\varphi\) is bounded (Proposition 3.2(4)), so \(\|\varphi^{(m)}(Y)\|\le\|\varphi\|\sum_{p,q}\|Y_{pq}\|\le m^2\|\varphi\|\,\|Y\|\) by Proposition 2.1(2). Letting \(\varepsilon\to0\), \(\varphi^{(m)}(X)\) is a norm limit of positive elements, hence positive.

(2) An abelian \(A\) is \(C_0(\Omega)\) up to an isometric \(*\)-isomorphism \(\Gamma\) (B5), which is CP with CP inverse (Proposition 3.2(3)). By (1) with \(k=1\), \(\varphi\circ\Gamma^{-1}\) is CP, and so is \(\varphi=(\varphi\circ\Gamma^{-1})\circ\Gamma\) by Proposition 3.2(2). If \(\Omega\) is a point, \(C_0(\Omega,M_k)=M_k(\mathbb C)\). \(\square\)

With \(\Omega\) a point, (1) contains Choi's theorem that \(k\)-positive maps on \(M_k(\mathbb C)\) are completely positive; Exercise 3.3 gives a direct proof. Proposition 7.1(7) extends (1) to maps into dual spaces.

**Corollary 5.5** (Kadison's inequality). If \(\varphi:A\to B\) is positive and \(a\in A\) is normal, then \(\varphi(a)^*\varphi(a)\le\|\varphi\|\,\varphi(a^*a)\). In particular \(\varphi(h)^2\le\|\varphi\|\,\varphi(h^2)\) for \(h\in A_h\).

**Proof.** The C\(^*\)-subalgebra \(C\) generated by \(a\) is abelian, because \(a\) is normal. By (P1), \(\varphi|_C\) is positive, hence CP by Theorem 5.4(2). Theorem 4.1(1), applied to \(\varphi|_C\), gives \(\varphi(a)^*\varphi(a)\le\|\varphi|_C\|\,\varphi(a^*a)\le\|\varphi\|\,\varphi(a^*a)\). \(\square\)

**Example 5.6** (How far positivity goes). The transpose \(t\) on \(M_2(\mathbb C)\) is positive, isometric and unital. It is not 2-positive (Proposition 3.2(3)), and it breaks the Kadison–Schwarz inequality (Theorem 4.1(4)). It still satisfies Kadison's inequality for normal elements (Corollary 5.5), for instance \(t(h)^2=(h^2)^{\mathsf T}=t(h^2)\) for self-adjoint \(h\). Its restriction to any abelian C\(^*\)-subalgebra, such as the diagonal matrices, is CP, by Theorem 5.4(2). And its composition with the identification \(\Phi_1\) of Proposition 7.5 is \(\Phi_2\), which is not 2-positive.

## 6. Stinespring's dilation theorem

**Theorem 6.1** (Stinespring). Fix a Hilbert space \(H\) and a C\(^*\)-algebra \(A\).

1. If \(\pi\) is a representation of \(A\) on \(K\) and \(V\in B(H,K)\), then \(\varphi(a)=V^*\pi(a)V\) is completely positive, and \(\|\varphi\|\le\|V\|^2\).
2. Let \(\varphi:A\to B(H)\) be completely positive, and put \(N=\varphi(A)'\). This is a von Neumann algebra, because \(\varphi(A)\) is self-adjoint: positive maps are hermitian (Proposition 3.2(2)). There are a Hilbert space \(K\), a representation \(\pi\) of \(A\) on \(K\), an operator \(V\in B(H,K)\) and a unital normal representation \(\rho\) of \(N\) on \(K\) such that
\[
\begin{gathered}
\varphi(a)=V^*\pi(a)V, \\
K=\overline{\operatorname{span}}\,\pi(A)VH, \\
\rho(N)\subseteq\pi(A)', \\
\rho(x)V=Vx, \\
a\in A,\quad x\in N.
\end{gathered}
\tag{6.1}
\]
3. Let \((u_i)\) be any approximate identity of \(A\). The increasing net \((\varphi(u_i))\) converges weakly to \(a_0:=V^*V\), which is its least upper bound, and
\[
\begin{gathered}
\|\varphi\|=\|V\|^2=\|a_0\| \\
=\lim_i\|\varphi(u_i)\|.
\end{gathered}
\tag{6.2}
\]
If \(A\) has a unit, then \(a_0=\varphi(1)\) and \(\|\varphi\|=\|\varphi(1)\|\).

*Further reading:* [Blackadar, II.6.9.7]. The norm equality is proved in (3).

**Proof.** (1) For \(x\in A^n\) and \(y\in B(H)^n\), put \(W=\sum_j\pi(x_j)Vy_j\in B(H,K)\). Then \(\sum_{i,j}y_i^*V^*\pi(x_i^*x_j)Vy_j=W^*W\ge0\), and the criterion of Proposition 3.2(1) applies. Also \(\|V^*\pi(a)V\|\le\|V\|^2\|a\|\), since \(\pi\) is contractive.

(2) *Step 1: the form.* The algebraic tensor product \(A\odot H\) means the following concrete quotient. Take the complex vector space freely spanned by symbols \((a,\xi)\in A\times H\), and divide by the subspace generated by the additivity and scalar-linearity relations in each entry. Write \(a\otimes\xi\) for the class of \((a,\xi)\). On this quotient put
\[
\begin{gathered}
\Bigl\langle\sum_ix_i\otimes\xi_i,\ \sum_jy_j\otimes\eta_j\Bigr\rangle_\varphi \\
=\sum_{i,j}\langle\varphi(y_j^*x_i)\xi_i,\eta_j\rangle.
\end{gathered}
\tag{6.3}
\]
The expression is bilinear in \(x,\xi\) and conjugate-bilinear in \(y,\eta\). It therefore vanishes on every defining relation in either variable, so it descends to a well-defined sesquilinear form on the quotient. For \(\zeta=\sum_{i=1}^nx_i\otimes\xi_i\) and \(\hat\xi=(\xi_1,\dots,\xi_n)\in H^n\), exchanging the names of the indices gives
\[
\langle\zeta,\zeta\rangle_\varphi=\bigl\langle\varphi^{(n)}\bigl([x_i^*x_j]\bigr)\hat\xi,\hat\xi\bigr\rangle\ \ge\ 0 ,
\tag{6.4}
\]
because \([x_i^*x_j]\) is positive (Lemma 2.2(1)), \(\varphi^{(n)}\) preserves positivity, and a positive operator matrix has a nonnegative quadratic form (Proposition 2.1(5)). So the form is positive semidefinite. By [Cauchy–Schwarz for forms](hilbert-spaces-and-compact-operators.md#oa-fnd-hs-01), \(N_0=\{\zeta:\langle\zeta,\zeta\rangle_\varphi=0\}\) is the subspace of vectors orthogonal to everything. The [Hilbert completion lemma](hilbert-spaces-and-compact-operators.md#completing-normed-and-inner-product-spaces) constructs the Hilbert space \(K\) from \((A\odot H)/N_0\), and let \(q:A\odot H\to K\) be the quotient map.

*Step 2: the two actions.* For \(a\in A\) and \(b\in N\) define linear maps of \(A\odot H\) by \(\pi_0(a)(x\otimes\xi)=ax\otimes\xi\) and \(\rho_0(b)(x\otimes\xi)=x\otimes b\xi\). They commute. We claim that, for all \(\zeta,\eta\in A\odot H\),
\[
\begin{gathered}
\langle\pi_0(a)\zeta,\pi_0(a)\zeta\rangle_\varphi \\
\le\|a\|^2\langle\zeta,\zeta\rangle_\varphi, \\
\langle\rho_0(b)\zeta,\rho_0(b)\zeta\rangle_\varphi \\
\le\|b\|^2\langle\zeta,\zeta\rangle_\varphi,
\end{gathered}
\tag{6.5}
\]
\[
\begin{gathered}
\langle\pi_0(a)\zeta,\eta\rangle_\varphi \\
=\langle\zeta,\pi_0(a^*)\eta\rangle_\varphi, \\
\langle\rho_0(b)\zeta,\eta\rangle_\varphi \\
=\langle\zeta,\rho_0(b^*)\eta\rangle_\varphi.
\end{gathered}
\tag{6.6}
\]
Let \(\zeta=\sum_{i=1}^nx_i\otimes\xi_i\), \(X=[x_i^*x_j]\) and \(Y=[x_i^*a^*ax_j]\). In a faithful representation \(\sigma\) of \(A\) on \(L\), for \(\vartheta\in L^n\),
\[
\begin{gathered}
\langle\sigma^{(n)}(Y)\vartheta,\vartheta\rangle \\
=\Bigl\|\sigma(a)\sum_j\sigma(x_j)\vartheta_j\Bigr\|^2 \\
\le\|a\|^2\Bigl\|\sum_j\sigma(x_j)\vartheta_j\Bigr\|^2 \\
=\|a\|^2\langle\sigma^{(n)}(X)\vartheta,\vartheta\rangle.
\end{gathered}
\]
So \(Y\le\|a\|^2X\) by Lemma 2.2(3), since \(\sigma\) is faithful, and \(\varphi^{(n)}(Y)\le\|a\|^2\varphi^{(n)}(X)\). As in (6.4), \(\langle\pi_0(a)\zeta,\pi_0(a)\zeta\rangle_\varphi=\langle\varphi^{(n)}(Y)\hat\xi,\hat\xi\rangle\), which gives the first bound. For the second, let \(T=\varphi^{(n)}(X)\ge0\) and \(b_n=\operatorname{diag}(b,\dots,b)\) on \(H^n\). Since \(b\) commutes with \(\varphi(A)\), \(b_n\) commutes with \(T\), hence with \(T^{1/2}\), a norm limit of polynomials in \(T\). As in (6.4),
\[
\begin{gathered}
\langle\rho_0(b)\zeta,\rho_0(b)\zeta\rangle_\varphi \\
=\langle Tb_n\hat\xi,b_n\hat\xi\rangle \\
=\|b_nT^{1/2}\hat\xi\|^2 \\
\le\|b\|^2\langle T\hat\xi,\hat\xi\rangle.
\end{gathered}
\]
For (6.6), let \(\eta=\sum_jy_j\otimes\eta_j\). Both sides of the first identity equal \(\sum_{i,j}\langle\varphi(y_j^*ax_i)\xi_i,\eta_j\rangle\), since \((a^*y_j)^*=y_j^*a\). Both sides of the second equal \(\sum_{i,j}\langle b\,\varphi(y_j^*x_i)\xi_i,\eta_j\rangle\), because \(b\) commutes with \(\varphi(A)\).

By (6.5), \(\pi_0(a)\) and \(\rho_0(b)\) map \(N_0\) into itself and induce operators of norm at most \(\|a\|\) and \(\|b\|\) on \((A\odot H)/N_0\). Let \(\pi(a)\) and \(\rho(b)\) be their extensions to \(K\). The maps \(a\mapsto\pi_0(a)\) and \(b\mapsto\rho_0(b)\) are linear and multiplicative, so by (6.6) \(\pi\) is a representation of \(A\) and \(\rho\) is a representation of \(N\), with \(\rho(1)=1\). The ranges commute, because \(\pi_0\) and \(\rho_0\) commute.

*Step 3: the operator \(V\).* Fix an approximate identity \((u_i)\), and put \(V_i\xi=q(u_i\otimes\xi)\). Then \(\|V_i\xi\|^2=\langle\varphi(u_i^2)\xi,\xi\rangle\le\|\varphi\|\,\|\xi\|^2\); \(\varphi\) is bounded by Proposition 3.2(4). Let \(i\le j\) and \(c=u_j-u_i\). In a faithful representation, \(0\le c\le u_j\le1\), so \(c^2=c^{1/2}cc^{1/2}\le c\). Hence
\[
\begin{gathered}
\|V_j\xi-V_i\xi\|^2=\langle\varphi(c^2)\xi,\xi\rangle \\
\le\langle\varphi(u_j)\xi,\xi\rangle-\langle\varphi(u_i)\xi,\xi\rangle.
\end{gathered}
\]
The numbers \(\langle\varphi(u_i)\xi,\xi\rangle\) increase with \(i\) and are at most \(\|\varphi\|\,\|\xi\|^2\), so they converge. Comparing \(V_i\xi\) and \(V_j\xi\) with \(V_{i_0}\xi\) for \(i,j\ge i_0\) shows that \((V_i\xi)\) is a Cauchy net. A Cauchy net in a complete metric space converges: choose increasing indices \(i_n\) so that every tail after \(i_n\) has diameter at most \(1/n\), take the limit of the Cauchy sequence at those indices, and use the same tail bound for the whole net. So \(V\xi=\lim_iV_i\xi\) defines \(V\in B(H,K)\) with \(\|V\|^2\le\|\varphi\|\).

*Step 4: the identities.* Let \(x\in A\) and \(\xi,\eta\in H\).
- (a) \(V^*q(x\otimes\xi)=\varphi(x)\xi\). Indeed \[
\begin{gathered}
\langle q(x\otimes\xi),V\eta\rangle\\
=\lim_i\langle q(x\otimes\xi),q(u_i\otimes\eta)\rangle\\
=\lim_i\langle\varphi(u_ix)\xi,\eta\rangle\\
=\langle\varphi(x)\xi,\eta\rangle,
\end{gathered}
\] since \(u_ix\to x\) and \(\varphi\) is bounded.
- (b) \(\pi(x)V\xi=q(x\otimes\xi)\). Indeed \(\pi(x)V_i\xi=q(xu_i\otimes\xi)\), and \[
\begin{gathered}
\|q(xu_i\otimes\xi)-q(x\otimes\xi)\|^2\\
\le\|\varphi\|\,\|xu_i-x\|^2\|\xi\|^2\to0.
\end{gathered}
\]
- (c) By (a) and (b), \(V^*\pi(x)V\xi=\varphi(x)\xi\). So \(\varphi=V^*\pi(\cdot)V\).
- (d) By (b), \(q(A\odot H)\) is the span of \(\pi(A)VH\). So \(K\) is the closed span of \(\pi(A)VH\); in particular \(\pi\) is nondegenerate.
- (e) For \(b\in N\), \[
\begin{gathered}
\pi(x)\rho(b)V\xi\\
=\rho(b)q(x\otimes\xi)\\
=q(x\otimes b\xi)\\
=\pi(x)Vb\xi.
\end{gathered}
\] So \(w=\rho(b)V\xi-Vb\xi\) satisfies \(\pi(x)w=0\) for all \(x\). Then \(\langle w,\pi(x^*)\kappa\rangle=0\) for all \(x\) and \(\kappa\), and \(w=0\) by (d). Hence \(\rho(b)V=Vb\).

*Step 5: \(\rho\) is normal.* For \(\zeta=\sum_ix_i\otimes\xi_i\) and \(\eta=\sum_jy_j\otimes\eta_j\),
\[
\langle\rho(b)q(\zeta),q(\eta)\rangle=\sum_{i,j}\langle b\,\xi_i,\ \varphi(x_i^*y_j)\eta_j\rangle ,
\]
a finite sum of vector functionals of \(b\), hence ultraweakly continuous on \(N\). For arbitrary \(\kappa,\lambda\in K\), choose \(\kappa_m\to\kappa\) and \(\lambda_m\to\lambda\) in \(q(A\odot H)\). Then
\[
\begin{gathered}
|\langle\rho(b)\kappa,\lambda\rangle-\langle\rho(b)\kappa_m,\lambda_m\rangle|\\
\le\|b\|\,(\|\kappa-\kappa_m\|\,\|\lambda\|+\|\kappa_m\|\,\|\lambda-\lambda_m\|).
\end{gathered}
\]
So \(b\mapsto\langle\rho(b)\kappa,\lambda\rangle\) is a norm limit in \(N^*\) of elements of \(N_*\), and it lies in \(N_*\) because \(N_*\) is norm-closed (B11). Finally, let \(\psi=\sum_n\langle\,\cdot\,\kappa_n,\lambda_n\rangle\in B(K)_*\). The series \(\psi\circ\rho=\sum_n\langle\rho(\cdot)\kappa_n,\lambda_n\rangle\) converges in the norm of \(N^*\), since the \(n\)-th term has norm at most \(\|\kappa_n\|\,\|\lambda_n\|\) and \(\sum_n\|\kappa_n\|\,\|\lambda_n\|<\infty\). So \(\psi\circ\rho\in N_*\), and \(\rho\) is normal.

(3) Let \((u_i)\) be any approximate identity, not necessarily the one fixed in Step 3. By (b), \(q(u_i\otimes\xi)=\pi(u_i)V\xi\), and \(\pi(u_i)\to1\) strongly because \(\pi\) is nondegenerate by (d) (Section 1). So \(V\xi=\lim_iq(u_i\otimes\xi)\), and (a) gives \[
\begin{gathered}
\langle V\xi,V\xi\rangle\\
=\lim_i\langle V^*q(u_i\otimes\xi),\xi\rangle\\
=\lim_i\langle\varphi(u_i)\xi,\xi\rangle\\
=\sup_i\langle\varphi(u_i)\xi,\xi\rangle.
\end{gathered}
\] So \(\langle a_0\xi,\xi\rangle=\sup_i\langle\varphi(u_i)\xi,\xi\rangle\) for every \(\xi\). By polarization \(\varphi(u_i)\to a_0\) weakly, and every self-adjoint upper bound \(c\) of the net satisfies \(\langle c\xi,\xi\rangle\ge\langle a_0\xi,\xi\rangle\). By (P2), \(\|a_0\|=\sup_{\|\xi\|=1}\sup_i\langle\varphi(u_i)\xi,\xi\rangle=\sup_i\|\varphi(u_i)\|\), and this supremum is a limit because the norms increase. Now \(\|\varphi\|\le\|V\|^2\) by (1), while \(\|V\|^2=\|V^*V\|=\|a_0\|=\sup_i\|\varphi(u_i)\|\le\|\varphi\|\). If \(A\) has a unit, then \(\|u_i-1\|=\|u_i1-1\|\to0\), so \(a_0=\lim_i\varphi(u_i)=\varphi(1)\). \(\square\)

*Remark* (A second proof of the Kadison–Schwarz inequality for completely positive maps). If \(\varphi=V^*\pi(\cdot)V\) as in (6.1), then \[
\begin{gathered}
\varphi(a)^*\varphi(a)\\
=V^*\pi(a)^*VV^*\pi(a)V\\
\le\|V\|^2V^*\pi(a^*a)V,
\end{gathered}
\] because \(VV^*\le\|V\|^21\). By (6.2) the right side is \(\|\varphi\|\,\varphi(a^*a)\). This gives Theorem 4.1(1) for completely positive maps.

**Theorem 6.2** (Uniqueness of the minimal dilation, and when \(\rho\) is faithful). Let \(\varphi\), \(N\), \(K\), \(\pi\), \(V\), \(\rho\) and \(a_0\) be as in Theorem 6.1.

1. Let \(\pi'\) be a representation of \(A\) on \(K'\) and \(V'\in B(H,K')\) with \(\varphi=V'^*\pi'(\cdot)V'\) and \(K'=\overline{\operatorname{span}}\,\pi'(A)V'H\). There is exactly one unitary \(U:K\to K'\) with \(U\pi(a)=\pi'(a)U\) for all \(a\in A\) and \(UV=V'\). If a map \(\rho':N\to B(K')\) satisfies \(\rho'(N)\subseteq\pi'(A)'\) and \(\rho'(x)V'=V'x\) for all \(x\), then \(\rho'(x)=U\rho(x)U^*\). In particular \(\rho\) is determined by (6.1), and any such \(\rho'\) is automatically a unital normal representation.
2. \(\ker\rho=\{x\in N:\ a_0x=0\}=N(1-z)\), where \(z\) is the projection onto the closed span of \(N'a_0H\). The projection \(z\) lies in the centre \(N\cap N'\). So \(\rho\) is faithful if and only if \(z=1\). This holds when \(a_0\) has zero kernel, in particular when \(a_0=1\).
3. There are completely positive maps for which \(\rho\) is not faithful. So a triple as in (6.1) with a faithful \(\rho\) need not exist, and the uniqueness in (1) must be stated without faithfulness.
4. If \(A\) has a unit, then \(V\xi=q(1\otimes\xi)\) and \(V^*V=\varphi(1)\). \(V\) is an isometry if and only if \(\varphi(1)=1\); for general \(A\), if and only if \(a_0=1\). Then \(\rho\) is faithful, and \(\varphi(a)\) is the compression of \(\pi(a)\) to the subspace \(VH\), identified with \(H\).

The explicit example in (3) proves that faithfulness cannot be required for every minimal dilation; (2) gives the exact condition.

**Proof.** (1) For finite sums,
\[
\begin{gathered}
\Bigl\|\sum_i\pi'(x_i)V'\xi_i\Bigr\|^2 \\
=\sum_{i,j}\langle V'^*\pi'(x_j^*x_i)V'\xi_i,\xi_j\rangle \\
=\sum_{i,j}\langle\varphi(x_j^*x_i)\xi_i,\xi_j\rangle \\
=\Bigl\|\sum_i\pi(x_i)V\xi_i\Bigr\|^2.
\end{gathered}
\]
So \(U_0:\sum_i\pi(x_i)V\xi_i\mapsto\sum_i\pi'(x_i)V'\xi_i\) is well defined and isometric from a dense subspace of \(K\) onto a dense subspace of \(K'\). It extends to a unitary \(U\). The relation \(U\pi(a)=\pi'(a)U\) holds on the dense subspace, hence everywhere. Both representations are nondegenerate, so \(\pi(u_i)\to1\) and \(\pi'(u_i)\to1\) strongly (Section 1). Hence \(UV\xi=\lim_iU\pi(u_i)V\xi=\lim_i\pi'(u_i)V'\xi=V'\xi\). Any unitary with the two properties satisfies \(U\pi(a)V\xi=\pi'(a)V'\xi\), so it is unique. For \(\rho'\): on the total set of vectors \(\pi'(a)V'\xi\), \(\rho'(x)\pi'(a)V'\xi=\pi'(a)\rho'(x)V'\xi=\pi'(a)V'x\xi\). The operator \(U\rho(x)U^*\) has the same values there, because \[
\begin{gathered}
U\rho(x)U^*\pi'(a)V'\xi\\
=U\rho(x)\pi(a)V\xi\\
=U\pi(a)Vx\xi\\
=\pi'(a)V'x\xi.
\end{gathered}
\] Two bounded operators that agree on a total set are equal.

(2) If \(\rho(x)=0\), then \(Vx=\rho(x)V=0\) and \(a_0x=V^*Vx=0\). If \(a_0x=0\), then \(\|Vx\xi\|^2=\langle a_0x\xi,x\xi\rangle=0\), so \(Vx=0\), and \(\rho(x)\pi(a)V\xi=\pi(a)Vx\xi=0\) on a total set; so \(\rho(x)=0\). Next, \(a_0\) is a weak limit of elements of \(\varphi(A)\subseteq N'\), and \(N'\) is weakly closed, so \(a_0\in N'\). Let \(x\in N\); it commutes with \(a_0\in N'\). If \(a_0x=0\), then \(xa_0=0\), and for \(y\in N'\) we get \(xya_0=yxa_0=0\); so \(x\) vanishes on \(N'a_0H\), and \(xz=0\). Conversely, if \(xz=0\), then \(xa_0=xza_0=0\), because \(1\in N'\) gives \(a_0H\subseteq zH\); and \(a_0x=xa_0=0\), since \(x\) and \(a_0\) commute. The subspace \(zH\) is invariant under \(N'\), and under \(N\) because \(xya_0\xi=ya_0x\xi\) for \(x\in N\), \(y\in N'\). Both sets are self-adjoint, so \(z\in N''\cap N'=N\cap N'\). Hence \(\ker\rho=\{x\in N:xz=0\}=N(1-z)\). If \(\ker a_0=\{0\}\), then \(a_0H\) is dense, because \((a_0H)^\perp=\ker a_0\), and \(z=1\).

(3) Let \(A=\mathbb C\), \(H=\mathbb C^2\) and \(\varphi(\lambda)=\lambda e_{11}\). With \(V(\xi_1,\xi_2)=\xi_1\in\mathbb C\) and \(\pi(\lambda)=\lambda\) on \(K=\mathbb C\), we have \(\varphi(\lambda)=V^*\pi(\lambda)V\), so \(\varphi\) is CP by Theorem 6.1(1), and \(K\) is spanned by \(\pi(\mathbb C)VH\). Here \(N=\varphi(\mathbb C)'\) is the algebra of diagonal matrices, and \(\rho(\operatorname{diag}(s,t))V=V\operatorname{diag}(s,t)\) forces \(\rho(\operatorname{diag}(s,t))=s\). So \(\rho(\operatorname{diag}(0,1))=0\). By (1), every triple satisfying (6.1) is unitarily equivalent to this one, so none of them has a faithful \(\rho\). In the notation of (2), \(a_0=e_{11}\), \(N'=N\) and \(z=e_{11}\).

(4) If \(A\) has a unit, then \(\|u_i-1\|\to0\), and \(\|V_i\xi-q(1\otimes\xi)\|^2\le\|\varphi\|\,\|u_i-1\|^2\|\xi\|^2\) (Step 3 of the proof of Theorem 6.1); so \(V\xi=q(1\otimes\xi)\), and \(a_0=\varphi(1)\) by Theorem 6.1(3). \(V\) is an isometry exactly when \(V^*V=a_0=1\). Then \(\rho\) is faithful by (2), and \(VV^*\) is the projection onto \(VH\). \(\square\)

### Examples of dilations

**Example 6.3** (A state is its own dilation). Let \(f\) be a positive functional on \(A\), viewed as a CP map into \(B(\mathbb C)=\mathbb C\) (Theorem 5.1(1)). In the proof of Theorem 6.1, \(A\odot\mathbb C=A\) and the form (6.3) is \(\langle x,y\rangle_f=f(y^*x)\), so \(K\) is the GNS space \(H_f\), \(\pi=\pi_f\), and \(V1=\xi_f\), the limit of the classes of \(u_i\). Here \(N=\mathbb C\) and \(\rho(\lambda)=\lambda1_{H_f}\). If \(f=0\), then \(H_f=\{0\}\), and \(\pi,V,\rho\) are the zero operators, as the same formulas require. The identity \(\|f\|=\|V\|^2=\lim_if(u_i)\) of (6.2) is the familiar formula for the norm of a positive functional, and \(a_0=\|f\|\).

**Example 6.4** (Compressions and minimality). Let \(\sigma\) be a representation of \(A\) on \(L\), and \(V\in B(H,L)\). Then \(\varphi=V^*\sigma(\cdot)V\) is CP (Theorem 6.1(1)). The closed span \(K_1\) of \(\sigma(A)VH\) reduces \(\sigma\): multiplication and adjoints preserve this span. Let \(P_1\) be its orthogonal projection, \(\pi=\sigma|_{K_1}\) and \(V_1=P_1V\). For every \(a\in A\), \(\sigma(a)VH\subseteq K_1\). Since \(K_1\) reduces \(\sigma\), the vector \(\sigma(a)(1-P_1)V\xi\) also belongs to \(K_1^\perp\), hence is zero. Thus \(\sigma(a)V=P_1\sigma(a)P_1V\), and
\[
V_1^*\pi(a)V_1=V^*\sigma(a)V=\varphi(a).
\]
Moreover \(\pi(A)V_1H=\sigma(A)VH\), so this triple is minimal and Theorem 6.2(1) identifies it with the Stinespring triple. If \(\sigma\) is nondegenerate, \(\sigma(u_i)V\xi\to V\xi\) shows \(VH\subseteq K_1\), and \(V_1=V\). Without nondegeneracy, \(VH\) may leave \(K_1\): for \(A=\mathbb C\), \(L=\mathbb C^2\), \(\sigma(\lambda)=\lambda e_{11}\) and \(V=1\), the map \(\varphi(\lambda)=\lambda e_{11}\) of Theorem 6.2(3) appears, with \(K_1=\mathbb C\varepsilon_1\), and the minimal dilation replaces \(V\) by the compression \(e_{11}V\).

**Example 6.5** (A faithful \(\rho\) with \(a_0\ne1\)). Let \(A=c_0\), the sequences tending to \(0\), acting diagonally on \(H=\ell^2\), and \(\varphi(x)=\operatorname{diag}(x_n/n)\). With \(\pi(x)=\operatorname{diag}(x_n)\) and \(V=\operatorname{diag}(n^{-1/2})\), \(\varphi=V^*\pi(\cdot)V\), and \(\pi(A)VH\) contains every finitely supported sequence, so the triple is minimal. Here \(N=\varphi(A)'\) is the algebra of diagonal operators, \(\rho(b)=b\), and \(a_0=V^*V=\operatorname{diag}(1/n)\). It is not \(1\) and not invertible, but it has zero kernel, so \(\rho\) is faithful, as Theorem 6.2(2) predicts, although the condition \(a_0=1\) of Theorem 6.2(4) fails. The norm formula gives \(\|\varphi\|=\|a_0\|=1\), attained on the approximate identity \(u_i=1_{\{1,\dots,i\}}\).

**Example 6.6** (The diagonal compression). On \(M_d(\mathbb C)\) let \(E(x)=\sum_ie_{ii}xe_{ii}\), which keeps the diagonal of \(x\). With \(\pi(x)=x\oplus\cdots\oplus x\) on \((\mathbb C^d)^d\) and \(V\xi=(e_{11}\xi,\dots,e_{dd}\xi)\), \(V^*\pi(x)V=\sum_ie_{ii}xe_{ii}=E(x)\). The triple is minimal: \(\pi(x)V\varepsilon_i\) has \(x\varepsilon_i\) in the \(i\)-th place and \(0\) elsewhere, and \(x\varepsilon_i\) runs through \(\mathbb C^d\). Here \(N=E(M_d)'\) is the diagonal algebra, and \(\rho(b)=b_{11}1\oplus\cdots\oplus b_{dd}1\) satisfies \(\rho(b)V=Vb\). Since \(E(1)=1\), \(V\) is an isometry and \(\rho\) is faithful (Theorem 6.2(4)). \(E\) is a unital CP map that is not multiplicative, and \(E(x)^*E(x)\le E(x^*x)\) is the Kadison–Schwarz inequality of Theorem 4.1(1) with \(\|E\|=1\).

### Positive definite functions on groups

**Exercise 6.7** (hard; Completely positive definite functions). Let \(G\) be a topological group, \(H\) a Hilbert space, and \(x:G\to B(H)\) a function that is *completely positive definite*: for all \(s_1,\dots,s_n\in G\), the operator matrix \([x(s_i^{-1}s_j)]_{i,j}\) is positive on \(H^n\). Suppose \(x\) is weakly continuous at the identity \(e\). Show that there are a strongly continuous unitary representation \(U\) of \(G\) on a Hilbert space \(K\) and \(T\in B(H,K)\) with \(x(s)=T^*U(s)T\) for all \(s\), and \(K=\overline{\operatorname{span}}\,U(G)TH\). Show that such a pair is unique up to a unitary \(W\) with \(WU(s)W^*=U'(s)\) and \(WT=T'\), and that \(x\) is then strongly continuous on all of \(G\).

*Solution.* Let \(K_0\) be the space of finitely supported functions \(g:G\to H\), with
\[
\langle g,g'\rangle_x=\sum_{s,t\in G}\langle x(t^{-1}s)g(s),g'(t)\rangle .
\]
If \(g\) is supported in \(\{s_1,\dots,s_n\}\), put \(\zeta_j=g(s_j)\). Then \(\langle g,g\rangle_x=\sum_{i,j}\langle x(s_i^{-1}s_j)\zeta_j,\zeta_i\rangle\ge0\), by the hypothesis and Proposition 2.1(5). So the form is positive semidefinite, hence hermitian. Apply the [null-space quotient and Hilbert completion lemma](hilbert-spaces-and-compact-operators.md#completing-normed-and-inner-product-spaces), to get \(K\) and the class map \(g\mapsto[g]\). For \(r\in G\) let \((U_0(r)g)(s)=g(r^{-1}s)\). Substituting \(s=rs'\), \(t=rt'\) gives \(\langle U_0(r)g,U_0(r)g'\rangle_x=\langle g,g'\rangle_x\), because \((rt')^{-1}(rs')=t'^{-1}s'\). Also \(U_0(r)U_0(r')=U_0(rr')\) and \(U_0(e)=1\). So each \(U_0(r)\) induces an isometry \(U(r)\) of \(K\) with inverse \(U(r^{-1})\), and \(U\) is a unitary representation. Let \(\delta_s\xi\) be the function with value \(\xi\) at \(s\) and \(0\) elsewhere, and put \(T\xi=[\delta_e\xi]\). Then \(\|T\xi\|^2=\langle x(e)\xi,\xi\rangle\le\|x(e)\|\,\|\xi\|^2\), \(U(s)T\xi=[\delta_s\xi]\), and
\[
\langle T^*U(s)T\xi,\eta\rangle=\langle[\delta_s\xi],[\delta_e\eta]\rangle=\langle x(s)\xi,\eta\rangle .
\]
So \(x(s)=T^*U(s)T\). The vectors \(U(s)T\xi=[\delta_s\xi]\) span \([K_0]\), which is dense.

*Continuity.* \[
\begin{gathered}
\|U(r)[\delta_t\xi]-[\delta_t\xi]\|^2\\
=2\langle x(e)\xi,\xi\rangle-2\,\mathrm{Re}\,\langle x(t^{-1}rt)\xi,\xi\rangle,
\end{gathered}
\] since \(\langle[\delta_{rt}\xi],[\delta_t\xi]\rangle=\langle x(t^{-1}rt)\xi,\xi\rangle\). As \(r\to e\), \(t^{-1}rt\to e\), so the right side tends to \(0\) by weak continuity at \(e\). The unitaries \(U(r)\) are uniformly bounded and the vectors \([\delta_t\xi]\) span a dense subspace, so \(U(r)\to1\) strongly as \(r\to e\). Then \(U(r)\kappa-U(r_0)\kappa=U(r_0)(U(r_0^{-1}r)\kappa-\kappa)\to0\) as \(r\to r_0\), so \(U\) is strongly continuous, and so is \(x=T^*U(\cdot)T\).

*Uniqueness.* If \((U',K',T')\) is another such pair, then \[
\begin{gathered}
\|\sum_lU'(s_l)T'\xi_l\|^2\\
=\sum_{l,m}\langle x(s_m^{-1}s_l)\xi_l,\xi_m\rangle\\
=\|\sum_lU(s_l)T\xi_l\|^2.
\end{gathered}
\] As in the proof of Theorem 6.2(1), \(W:\sum U(s_l)T\xi_l\mapsto\sum U'(s_l)T'\xi_l\) extends to a unitary with the stated properties, and \(WT=T'\) because \(T\xi=U(e)T\xi\).

*Remarks.* The necessity is also true: if \(x(s)=T^*U(s)T\), then \([x(s_i^{-1}s_j)]=[(U(s_i)T)^*(U(s_j)T)]\ge0\). When \(G\) is locally compact the result can also be derived from Stinespring's theorem through the group C\(^*\)-algebra, but the direct construction is shorter, and it is Stinespring's construction with \(A\odot H\) replaced by functions on \(G\).

## 7. Completely positive maps and dual spaces

### Matrix order on dual spaces, and transposes

Let \(A\) be a C\(^*\)-algebra. Identify \(M_n(A^*)\) with the dual of \(M_n(A)\) through
\[
\begin{gathered}
\langle a,f\rangle=\sum_{i,j}f_{ij}(a_{ij}), \\
a\in M_n(A),\quad f\in M_n(A^*),
\end{gathered}
\tag{7.1}
\]
and call \(f\) positive if it is a positive functional on \(M_n(A)\). For a linear subspace \(E\) of \(A\) or of \(A^*\), give \(M_n(E)\) the order inherited from \(M_n(A)\) or \(M_n(A^*)\). A linear map \(\varphi:E\to F\) between two such subspaces is \(n\)-positive if \(\varphi^{(n)}\) maps positive elements of \(M_n(E)\) to positive elements of \(M_n(F)\), and completely positive if it is \(n\)-positive for all \(n\). For \(E=A\) and \(F=B\) this is Definition 3.1.

For a bounded map \(\varphi:A\to B\), write \(\varphi^\sharp:B^*\to A^*\), \((\varphi^\sharp g)(a)=g(\varphi(a))\), for its transpose (Banach-space adjoint).

**Proposition 7.1.**

1. (7.1) is a linear bijection of \(M_n(A^*)\) onto \(M_n(A)^*\), with \(\max_{i,j}\|f_{ij}\|\le\|f\|\le\sum_{i,j}\|f_{ij}\|\). The cone \(M_n(A^*)_+\) is weak\(^*\)-closed, hence norm-closed.
2. \(f\in M_n(A^*)\) is positive exactly when \(\sum_{i,j}f_{ij}(a_i^*a_j)\ge0\) for all \(a_1,\dots,a_n\in A\).
3. If \(f\in M_n(A^*)_+\) and \(\alpha\in M_{n,m}(\mathbb C)\), then \(\alpha^*f\alpha:=\bigl[\sum_{i,j}\overline{\alpha_{ip}}f_{ij}\alpha_{jq}\bigr]_{p,q}\) lies in \(M_m(A^*)_+\).
4. A composition of \(n\)-positive maps between such subspaces is \(n\)-positive; so a composition of CP maps is CP.
5. A positive linear map from a C\(^*\)-algebra \(A\) into a subspace \(F\) of a C\(^*\)-algebra \(B\) or of a dual \(B^*\) is bounded.
6. Let \(\varphi:A\to B\) be a bounded linear map of C\(^*\)-algebras. Under (7.1), \((\varphi^{(n)})^\sharp=(\varphi^\sharp)^{(n)}\). The map \(\varphi\) is positive exactly when \(\varphi^\sharp\) is. Hence \(\varphi\) and \(\varphi^\sharp\) are \(n\)-positive together, and CP together.
7. Theorem 5.4(1) holds for maps into a subspace \(F\) of a dual \(B^*\): every \(k\)-positive map from \(C_0(\Omega,M_k)\) into \(F\) is completely positive.

**Proof.** (1) As a Banach space, \(M_n(A)\) is the direct sum of \(n^2\) copies of \(A\), with a norm equivalent to the largest entry norm (Proposition 2.1(2)). A functional on it is the sum of its restrictions to the copies, which is (7.1). Then \(|\langle a,f\rangle|\le\sum\|f_{ij}\|\,\|a_{ij}\|\le(\sum\|f_{ij}\|)\|a\|\). The matrix with the single nonzero entry \(x\) at \((i,j)\) has norm \(\|x\|\) by Proposition 2.1(2), which gives \(\|f_{ij}\|\le\|f\|\). The cone is the intersection of the weak\(^*\)-closed half-spaces \(\{f:\langle a,f\rangle\ge0\}\), \(a\in M_n(A)_+\).

(2) This is Lemma 2.2(1): the matrices \([a_i^*a_j]\) generate \(M_n(A)_+\) as a convex cone.

(3) For \(a\in A^m\), put \(b_i=\sum_q\alpha_{iq}a_q\). Then \(\sum_{p,q}(\alpha^*f\alpha)_{pq}(a_p^*a_q)=\sum_{i,j}f_{ij}(b_i^*b_j)\ge0\) by (2).

(4) \((\psi\circ\varphi)^{(n)}=\psi^{(n)}\circ\varphi^{(n)}\).

(5) For \(F\subseteq B\) this is Proposition 3.2(4). Let \(F\subseteq B^*\). If \(0\le f\le g\) in \(B^*\), then \[
\begin{gathered}
\|f\|\\
\le4\sup\{f(c):c\in B_+,\|c\|\le1\}\\
\le4\sup\{g(c):c\in B_+,\|c\|\le1\}\\
\le4\|g\|;
\end{gathered}
\] the first inequality is Proposition 3.2(4) for the positive map \(f:B\to\mathbb C\). Now repeat the proof of Proposition 3.2(4) with \(\|\varphi(a_k)\|\ge8^k\): from \(\varphi(a)\ge2^{-k}\varphi(a_k)\ge0\) we get \(\|\varphi(a)\|\ge\tfrac14\,2^{-k}8^k=\tfrac14 4^k\) for every \(k\), which is absurd. The bound by four times the supremum over positive contractions follows as before.

(6) For \(x\in M_n(A)\) and \(f\in M_n(B^*)\),
\[
\begin{gathered}
\langle\varphi^{(n)}(x),f\rangle\\
=\sum_{i,j}f_{ij}(\varphi(x_{ij}))\\
=\sum_{i,j}(\varphi^\sharp f_{ij})(x_{ij})\\
=\langle x,(\varphi^\sharp)^{(n)}f\rangle.
\end{gathered}
\]
If \(\varphi\) is positive and \(g\in B^*_+\), then \((\varphi^\sharp g)(a)=g(\varphi(a))\ge0\) for \(a\ge0\). Conversely, let \(\varphi^\sharp\) be positive, let \(a\ge0\), and write \(\varphi(a)=h+ik\) with \(h,k\in B_h\). For every positive \(g\), \(g(\varphi(a))=(\varphi^\sharp g)(a)\ge0\) is real, while \(g(h)\) and \(g(k)\) are real (B7); so \(g(k)=0\). Take \(g=\langle\sigma(\cdot)\zeta,\zeta\rangle\) for a faithful representation \(\sigma\) of \(B\). Then \(\langle\sigma(k)\zeta,\zeta\rangle=0\) for all \(\zeta\), so \(\sigma(k)=0\) and \(k=0\); and \(\langle\sigma(h)\zeta,\zeta\rangle\ge0\) for all \(\zeta\), so \(h\ge0\) by (P2) and (P1). Thus \(\varphi(a)\ge0\). Apply this to the bounded map \(\varphi^{(n)}\) between the C\(^*\)-algebras \(M_n(A)\) and \(M_n(B)\): \(\varphi^{(n)}\) is positive exactly when \((\varphi^{(n)})^\sharp=(\varphi^\sharp)^{(n)}\) is.

(7) The proof of Theorem 5.4(1) uses three facts about the target: in each \(M_m(F)\) the positive cone is norm-closed, scalar compressions preserve positivity, and \(\varphi\) is bounded. For a subspace of \(B^*\) these are (1), (3) and (5). \(\square\)

### The commutant of a GNS representation

Let \(\omega\) be a positive linear functional on \(A\), and let \((\pi,H,\xi)\) be its GNS representation (B8): \(\omega(a)=\langle\pi(a)\xi,\xi\rangle\), and \(\pi(A)\xi\) is dense in \(H\). Let \(C_\omega^+\) be the set of \(f\in A^*_+\) with \(f\le\alpha\omega\) for some \(\alpha\ge0\), and \(C_\omega\) its linear span. Define
\[
\begin{gathered}
\theta_\omega(x)(a)=\langle\pi(a)x\xi,\xi\rangle, \\
x\in\pi(A)',\quad a\in A.
\end{gathered}
\tag{7.2}
\]

**Lemma 7.2** (Few orthogonal projections force finite dimension). Let \(M\) be a von Neumann algebra in which every family of pairwise orthogonal nonzero projections has at most \(N\) members. Then \(\dim M\le N^2\).

**Proof.** If \(M=\{0\}\) there is nothing to prove. Choose a family \(q_1,\dots,q_r\) of pairwise orthogonal nonzero projections in \(M\) with \(r\) as large as possible; \(r\le N\). Then \(\sum_iq_i=1\), since otherwise \(1-\sum_iq_i\) could be added. Each \(q=q_i\) is minimal: a projection \(e\in M\) with \(0\ne e\ne q\) and \(e\le q\) would split \(q\) into \(e\) and \(q-e\).

*Claim: \(qMq=\mathbb Cq\).* \(qMq\) is a C\(^*\)-algebra with unit \(q\). Let \(y\in qMq\) be self-adjoint, and suppose its spectrum in \(qMq\) contains two points \(\lambda\ne\mu\). Choose continuous \(f,g\ge0\) on the spectrum with disjoint supports and \(f(\lambda)=g(\mu)=1\). Then \(f(y),g(y)\in qMq\) are nonzero, positive, and \(f(y)g(y)=0\). Let \(e_f\) and \(e_g\) be the projections onto the closures of their ranges. They are orthogonal, because the range of \(g(y)\) lies in the kernel of \(f(y)\). They lie below \(q\), because \(f(y)=qf(y)\) and \(g(y)=qg(y)\). They lie in \(M\): if \(x'\in M'\), then \(x'\) commutes with \(f(y)\), so it maps the range of \(f(y)\) into itself, and \(x'e_f=e_fx'e_f\); the same for \(x'^*\), and taking adjoints gives \(e_fx'=e_fx'e_f\). So \(x'e_f=e_fx'\) for every \(x'\in M'\), and \(e_f\in M''=M\). So \(e_f\) is a projection in \(M\) with \(0\ne e_f\le q-e_g<q\), which contradicts minimality. Hence the spectrum of \(y\) is a single point \(\lambda\), and \(y=\lambda q\), since the norm of the self-adjoint element \(y-\lambda q\) equals its spectral radius (B4). Writing a general element as \(h+ik\) proves the claim.

*Claim: \(\dim q_iMq_j\le1\).* Let \(x,y\in q_iMq_j\) with \(x\ne0\). By the first claim, \(x^*x=cq_j\) with \(c=\|x\|^2>0\), and \(yx^*=\lambda q_i\) for some \(\lambda\). Then \(cy=yx^*x=\lambda q_ix=\lambda x\), so \(y\in\mathbb Cx\).

Every \(x\in M\) equals \(\sum_{i,j}q_ixq_j\), so \(\dim M\le r^2\le N^2\). \(\square\)

**Theorem 7.3.**

1. \(\theta_\omega\) is an injective CP map of \(\pi(A)'\) onto \(C_\omega\). It maps \(\pi(A)'_+\) onto \(C_\omega^+\), \(C_\omega\cap A^*_+=C_\omega^+\), and \(\theta_\omega(1)=\omega\). The inverse \(\theta_\omega^{-1}:C_\omega\to\pi(A)'\) is CP, with \(C_\omega\subseteq A^*\) ordered as in Proposition 7.1.
2. \(\|\theta_\omega(x)\|\le\|\omega\|\,\|x\|\). In particular \(\theta_\omega\) is contractive when \(\omega\) is a state.
3. The following are equivalent: (a) \(\theta_\omega^{-1}\) is bounded for the norm of \(A^*\); (b) \(C_\omega\) is norm-closed in \(A^*\); (c) \(\pi(A)'\) is finite-dimensional.
4. Let \(B\) be a unital C\(^*\)-algebra and \(\varphi:B\to A^*\) positive with \(\varphi(1)\le\alpha\omega\). Then \(\varphi(B)\subseteq C_\omega\), and \(\psi=\theta_\omega^{-1}\circ\varphi:B\to\pi(A)'\) is positive, hence bounded. If \(\varphi\) is \(n\)-positive (CP), so is \(\psi\). If \(\varphi\) is 2-positive, then \(\|\psi\|=\|\psi(1)\|\le\alpha\), and \(\psi\) is unital when \(\varphi(1)=\omega\).

Part (3) characterizes boundedness of \(\theta_\omega^{-1}\), and (4) needs only positivity and domination by a multiple of \(\omega\); complete positivity and equality at the identity are not needed for its factorization.

**Proof.** (1) *Positivity and range.* For \(x\in\pi(A)'_+\), its square root \(x^{1/2}\) lies in the C\(^*\)-algebra \(\pi(A)'\) and commutes with \(\pi(A)\). So
\[
\theta_\omega(x)(a^*a)=\langle\pi(a)^*\pi(a)x\xi,\xi\rangle=\|x^{1/2}\pi(a)\xi\|^2,
\]
which lies between \(0\) and \(\|x\|\,\omega(a^*a)\). Hence \(0\le\theta_\omega(x)\le\|x\|\omega\), and \(\theta_\omega(x)\in C_\omega^+\). Every element of \(\pi(A)'\) is a combination of four positive ones, so \(\theta_\omega(\pi(A)')\subseteq C_\omega\).

*Onto \(C_\omega^+\).* Let \(f\in A^*_+\) with \(f\le\alpha\omega\). By the Cauchy–Schwarz inequality, \[
\begin{gathered}
|f(b^*a)|^2\\
\le f(a^*a)f(b^*b)\\
\le\alpha^2\|\pi(a)\xi\|^2\|\pi(b)\xi\|^2.
\end{gathered}
\] So \(B_f(\pi(a)\xi,\pi(b)\xi)=f(b^*a)\) is a well-defined bounded positive sesquilinear form on the dense subspace \(\pi(A)\xi\). It extends to \(H\), and there is \(h\in B(H)\) with \(0\le h\le\alpha1\) and \(f(b^*a)=\langle h\pi(a)\xi,\pi(b)\xi\rangle\) (B10). For \(c\in A\), \[
\begin{gathered}
\langle h\pi(c)\pi(a)\xi,\pi(b)\xi\rangle\\
=f((c^*b)^*a)\\
=\langle h\pi(a)\xi,\pi(c^*b)\xi\rangle\\
=\langle\pi(c)h\pi(a)\xi,\pi(b)\xi\rangle,
\end{gathered}
\] so \(h\in\pi(A)'\). Since \(\pi\) is nondegenerate, \(\pi(u_i)\xi\to\xi\), and \[
\begin{gathered}
f(a)\\
=\lim_if(u_ia)\\
=\lim_i\langle h\pi(a)\xi,\pi(u_i)\xi\rangle\\
=\langle\pi(a)h\xi,\xi\rangle\\
=\theta_\omega(h)(a).
\end{gathered}
\] As \(C_\omega\) is spanned by \(C_\omega^+\), \(\theta_\omega\) maps onto \(C_\omega\).

*Injectivity and the cones.* \(\theta_\omega(x)(b^*a)=\langle x\pi(a)\xi,\pi(b)\xi\rangle\). If \(\theta_\omega(x)=0\), these numbers vanish on a dense set, so \(x=0\). If \(\theta_\omega(x)\ge0\), then \(\langle x\pi(a)\xi,\pi(a)\xi\rangle\ge0\) for all \(a\), so \(x\ge0\) by (P2), and \(\theta_\omega(x)\le\|x\|\omega\). This gives \(C_\omega\cap A^*_+=C_\omega^+\). Clearly \(\theta_\omega(1)=\omega\).

*\(\theta_\omega\) is CP.* The matrices \([x_p^*x_q]\) generate the positive cone of \(M_n(\pi(A)')\) (Lemma 2.2(1)), and \(f\in M_n(A^*)\) is positive exactly when \(\sum_{p,q}f_{pq}(a_p^*a_q)\ge0\) for all \(a_1,\dots,a_n\in A\) (Proposition 7.1(2)). So it suffices to check, for \(x_1,\dots,x_n\in\pi(A)'\) and \(a_1,\dots,a_n\in A\),
\[
\begin{gathered}
\sum_{p,q}\theta_\omega(x_p^*x_q)(a_p^*a_q) \\
=\sum_{p,q}\langle\pi(a_p)^*x_p^*x_q\pi(a_q)\xi,\xi\rangle \\
=\Bigl\|\sum_qx_q\pi(a_q)\xi\Bigr\|^2\ge0.
\end{gathered}
\]

*\(\theta_\omega^{-1}\) is CP.* Let \(f\in M_n(C_\omega)\) be positive in \(M_n(A^*)\), and \(X=[\theta_\omega^{-1}(f_{pq})]\). For \(\zeta=(\pi(a_1)\xi,\dots,\pi(a_n)\xi)\), since each \(\theta_\omega^{-1}(f_{pq})\) commutes with \(\pi(A)\),
\[
\begin{gathered}
\sum_{p,q}\langle\theta_\omega^{-1}(f_{pq})\pi(a_q)\xi,\pi(a_p)\xi\rangle \\
=\sum_{p,q}f_{pq}(a_p^*a_q)\ge0.
\end{gathered}
\]
Such \(\zeta\) are dense in \(H^n\). Positivity in \(M_n(B(H))\) is tested by this quadratic form (Proposition 2.1(5)), so \(X\ge0\) in \(M_n(B(H))\), and hence in the C\(^*\)-subalgebra \(M_n(\pi(A)')\) (Proposition 2.1(4)).

(2) \(|\theta_\omega(x)(a)|\le\|a\|\,\|x\|\,\|\xi\|^2\), and \(\|\xi\|^2=\lim_i\langle\pi(u_i)\xi,\xi\rangle=\lim_i\omega(u_i)\le\|\omega\|\).

(3) (a)\(\Leftrightarrow\)(b): \(\theta_\omega\) is a bounded bijection of the Banach space \(\pi(A)'\) onto \(C_\omega\). If \(C_\omega\) is closed, the open mapping theorem makes \(\theta_\omega^{-1}\) bounded. If \(\theta_\omega^{-1}\) is bounded, \(C_\omega\) is isomorphic to a Banach space, hence complete, hence closed. (c)\(\Rightarrow\)(a): \(C_\omega\) is then finite-dimensional, so [Theorem 7.1(3) of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-07) makes its linear map \(\theta_\omega^{-1}\) bounded. (a)\(\Rightarrow\)(c): let \(\|\theta_\omega^{-1}(f)\|\le c\|f\|\) on \(C_\omega\). For a projection \(p\in\pi(A)'\), \(\theta_\omega(p)(a)=\langle\pi(a)p\xi,p\xi\rangle\), so \(\|\theta_\omega(p)\|\le\|p\xi\|^2\). If \(p\ne0\), then \(1=\|p\|\le c\|p\xi\|^2\). For pairwise orthogonal nonzero projections \(p_1,\dots,p_m\) in \(\pi(A)'\) this gives \(m\le c\sum_l\|p_l\xi\|^2\le c\|\xi\|^2\). By Lemma 7.2, \(\pi(A)'\) is finite-dimensional.

(4) For \(b\in B_+\), \(0\le b\le\|b\|1\), so \(0\le\varphi(b)\le\|b\|\alpha\omega\), and \(\varphi(b)\in C_\omega^+\). \(B\) is spanned by \(B_+\), so \(\varphi(B)\subseteq C_\omega\). By (1), \(\theta_\omega^{-1}\) maps \(C_\omega^+\) into \(\pi(A)'_+\), so \(\psi\) is positive, and bounded by Proposition 3.2(4). If \(\varphi\) is \(n\)-positive, then \(\psi\) is \(n\)-positive by (1) and Proposition 7.1(4). If \(\varphi\) is 2-positive, Theorem 4.1(2) gives \(\|\psi\|=\|\psi(1)\|\). Now \(\alpha\omega-\varphi(1)\) lies in \(C_\omega\cap A^*_+=C_\omega^+\), so \(\alpha1-\psi(1)=\theta_\omega^{-1}(\alpha\omega-\varphi(1))\ge0\), and \(\|\psi(1)\|\le\alpha\) by (P2). If \(\varphi(1)=\omega\), then \(\psi(1)=\theta_\omega^{-1}(\omega)=1\). \(\square\)

**Example 7.4** (An unbounded inverse). Let \(A=C[0,1]\) and \(\omega(a)=\int_0^1a(t)\,dt\). The GNS space is \(L^2[0,1]\), \(\pi(a)\) is multiplication by \(a\), and \(\xi=1\). Multiplication by the indicator of an interval commutes with \(\pi(A)\). The indicators of \(I_k=[2^{-k},2^{-k+1})\), \(k\ge1\), give infinitely many pairwise orthogonal nonzero projections in \(\pi(A)'\), so \(\theta_\omega^{-1}\) is unbounded by Theorem 7.3(3). Concretely, \(\theta_\omega\) sends multiplication by \(1_{I_k}\), an operator of norm \(1\), to the functional \(a\mapsto\int_{I_k}a\,dt\), of norm \(2^{-k}\).

### Transposes and the dual of \(M_d(\mathbb C)\)

Let \(d\ge2\), \(A=M_d(\mathbb C)\), and \(\tau=d^{-1}\mathrm{Tr}\). Define \(\Phi_1,\Phi_2:A\to A^*\) by
\[
\begin{gathered}
\Phi_1(a)(x)=\sum_{i,j}a_{ij}x_{ij} \\
=\mathrm{Tr}(a^{\mathsf T}x), \\
\Phi_2(a)(x)=\sum_{i,j}a_{ji}x_{ij} \\
=\mathrm{Tr}(ax).
\end{gathered}
\tag{7.3}
\]

**Proposition 7.5.**

1. \(\Phi_1\) and \(\Phi_2\) are positive linear bijections of \(A\) onto \(A^*\).
2. \(\Phi_1\) is completely positive, and so is \(\Phi_1^{-1}\).
3. \(\Phi_2\) is not 2-positive.
4. Under the identification (7.1) for the algebra \(\mathbb C\), a functional \(f\) on \(M_d(\mathbb C)\) corresponds to the matrix \([f(e_{ij})]\), because \(f(x)=\sum_{i,j}f(e_{ij})x_{ij}\). Then \(\Phi_1(a)\) corresponds to \([a_{ij}]\) and \(\Phi_2(a)\) to \([a_{ji}]\). Under the trace pairing, \(f\) corresponds instead to the matrix \(D_f\) with \(f(x)=\mathrm{Tr}(D_fx)\); then \(\Phi_2(a)\) corresponds to \(a\) and \(\Phi_1(a)\) to \(a^{\mathsf T}\).

The explicit computations in (2)–(4) show how switching between the entrywise pairing (7.1) and the trace pairing introduces a transpose.

**Proof.** For finite matrices, \(\mathrm{Tr}(cd)=\sum_{i,j}c_{ij}d_{ji}=\mathrm{Tr}(dc)\); this proves every cyclic trace identity used below. (1) If \(a,x\ge0\), then \(\mathrm{Tr}(ax)=\mathrm{Tr}(a^{1/2}xa^{1/2})\ge0\), and \(a^{\mathsf T}\ge0\) (Proposition 3.2(3)), so both maps are positive. If \(\mathrm{Tr}(ax)=0\) for all \(x\), then \(a=0\); so both maps are injective, and they are onto by dimension.

(2) The GNS representation of \(\tau\) acts on \(H_\tau=M_d(\mathbb C)\) with \(\langle x,y\rangle=\tau(y^*x)\), by \(\pi(a)x=ax\), with \(\xi=1\). An operator \(T\) that commutes with every \(\pi(a)\) satisfies \(T(x)=T(x1)=xT(1)\), so \(\pi(A)'=\{R_c:c\in A\}\), where \(R_cx=xc\). With respect to \(\langle\cdot,\cdot\rangle\), \(R_c^*=R_{c^*}\), since \(\tau(y^*xc)=\tau((yc^*)^*x)\). The map \(j(a)=R_{a^{\mathsf T}}\) is a \(*\)-isomorphism of \(A\) onto \(\pi(A)'\): it is linear and bijective, \(R_{a^{\mathsf T}}R_{b^{\mathsf T}}x=xb^{\mathsf T}a^{\mathsf T}=R_{(ab)^{\mathsf T}}x\), and \(R_{a^{\mathsf T}}^*=R_{(a^*)^{\mathsf T}}\). Next, by (7.2), \(\theta_\tau(R_c)(x)=\langle\pi(x)R_c1,1\rangle=\tau(xc)\), so
\[
\begin{gathered}
\Phi_1(a)(x)=\mathrm{Tr}(xa^{\mathsf T}) \\
=d\,\theta_\tau(j(a))(x), \\
\text{that is, }\Phi_1=d\,\theta_\tau\circ j.
\end{gathered}
\]
Every \(f\in A^*_+\) has the form \(\mathrm{Tr}(D\,\cdot)\) with \(D=[f(e_{ji})]_{i,j}\): the matrix-unit expansion proves the formula, and \(v^*Dv=f(vv^*)\ge0\) for every column \(v\), so \(D\ge0\). Consequently \(f\le d\|D\|\tau\); hence \(C_\tau=A^*\). The maps \(\theta_\tau\) and \(\theta_\tau^{-1}\) are CP (Theorem 7.3(1)), the \(*\)-isomorphisms \(j\) and \(j^{-1}\) are CP (Proposition 3.2(3)), and compositions of CP maps are CP (Proposition 7.1(4)). So \(\Phi_1\) and \(\Phi_1^{-1}=j^{-1}\circ\theta_\tau^{-1}\circ d^{-1}\) are CP.

(3) The matrix \(X=[e_{pq}]_{p,q=1,2}\in M_2(A)\) is positive (Lemma 2.2(1)). Test \(\Phi_2^{(2)}(X)\) with Proposition 7.1(2), using \(a_1=e_{12}\), \(a_2=-e_{11}\) and \(\mathrm{Tr}(e_{pq}y)=y_{qp}\):
\[
\begin{gathered}
\sum_{p,q=1}^2\Phi_2(e_{pq})(a_p^*a_q) \\
=\sum_{p,q}(a_p^*a_q)_{qp} \\
=(e_{22})_{11}+(-e_{21})_{21} \\
+(-e_{12})_{12}+(e_{11})_{22} \\
=-2<0.
\end{gathered}
\]

(4) This is bookkeeping: \(\Phi_1(a)(e_{ij})=a_{ij}\) and \(\Phi_2(a)(e_{ij})=a_{ji}\); and \(\Phi_2(a)=\mathrm{Tr}(a\,\cdot)\), \(\Phi_1(a)=\mathrm{Tr}(a^{\mathsf T}\cdot)\). \(\square\)

So whether the natural map from \(M_d(\mathbb C)\) to its dual is completely positive depends on how the dual is identified with \(M_d(\mathbb C)\), and the transpose is what separates the two choices. The proof of (2) shows where the transpose comes from: the commutant of the trace representation acts by right multiplication, which reverses products.

## Where this leads

The following four extension results are further directions, not proved here and unused in the proofs of this lesson.

- Theorem 5.1(3) has a counterpart for domains: an \(n\)-positive map from a C\(^*\)-algebra whose irreducible representations all have dimension at most \(n\) is completely positive. Theorem 5.4 is the case of the domains \(C_0(\Omega,M_k)\).
- Conversely to Theorem 5.1(3), if every \(n\)-positive map from every C\(^*\)-algebra into \(B\) is completely positive, then every irreducible representation of \(B\) has dimension at most \(n\).
- A unital linear map between unital C\(^*\)-algebras, with nonzero target, is positive if and only if it is contractive [Blackadar, II.6.9.4]. So every positive unital map has norm \(1=\|\varphi(1)\|\), while Theorem 4.1(2) gives \(\|\varphi\|=\|\varphi(1)\|\) for 2-positive maps that need not be unital.
- Completely positive maps into \(B(H)\) extend from a C\(^*\)-subalgebra, and even from an operator system, to the whole algebra with the same norm [Blackadar, II.6.9.12]. This extension theorem leads to the theory of injective C\(^*\)-algebras.
- Tensor products of completely positive maps, and normal completely positive maps between von Neumann algebras, are the next steps. They are used for tensor products of C\(^*\)-algebras and for conditional expectations.

## References

- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, [revised author edition, 8 February 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).

*Freely accessible reading:* [Kristin Courtney; Elizabeth Gillaspy; Lara Ismert, *Notes on C*-algebras: Notes and Exercises for GOALS*, §10](https://www.ipam.ucla.edu/wp-content/uploads/2024/07/Notes_and_Exercises_for_GOALS.pdf) gives a route through matrix positivity, Stinespring dilation and multiplicative domains; omitted extension and nonunital steps are supplied here. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.
