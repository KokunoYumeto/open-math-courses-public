# Integration for a trace, the commutation theorem, and applications

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision of the references is self-checked by the writing AI. Public domain (CC0).*

On a von Neumann algebra \(M\), a faithful semifinite normal trace \(\tau\) behaves like the integral on a measure space. The elements of finite trace play the part of integrable functions, and \(M\) itself plays the part of the bounded functions. This lesson makes the picture precise and uses it.

First, the completion \(L^1(M,\tau)\) of the elements of finite trace is the predual of \(M\), so \(M\) is the dual space of \(L^1(M,\tau)\), exactly as \(L^\infty\) is the dual of \(L^1\). Second, the square-integrable elements form a Hilbert space \(L^2(M,\tau)\) on which \(M\) acts by left and by right multiplication. The central result, the *commutation theorem*, says that these two actions are each other's commutants. For a commutative algebra it says that \(L^\infty\) is maximal abelian on \(L^2\).

The commutation theorem has many consequences, and the lesson proves the main ones. An algebra and its commutant are semifinite together, and they have the same type I, II and III parts. An algebra is semifinite exactly when it can be represented with a finite commutant. The involution is continuous on bounded sets for the \(\sigma\)-strong topology exactly on finite corners; from this we determine the type of a tensor product. Two semifinite traces differ by a central density, which leads to an extended center-valued trace on every semifinite algebra. A subalgebra on which the trace stays semifinite carries a unique trace-preserving conditional expectation. The last sections treat closed operators that agree outside a projection of small trace, an equivalence relation on positive elements that extends Murray–von Neumann equivalence, and algebras onto which \(B(H)\) has many normal bimodule maps.

The lesson assumes the lesson Traces on von Neumann algebras: traces, the definition ideal, supports, the center-valued trace of a finite algebra, and the trace norm. It also uses Projections and types of von Neumann algebras, The double commutant theorem, Spatial tensor products of von Neumann algebras, The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras and Polar decomposition of functionals and weak compactness in preduals. Every fact used from other lessons is stated in full in the list of results used, with the place where it is proved. The lesson *Measurable operators for a trace: examples, convergence and the commutant* proves the commutation theorem again, by measurable operators, and builds traces on commutants of arbitrary normal representations.

Basic references are [Kostecki] and [Blackadar].

## Conventions

- \(M\) is a von Neumann algebra acting on a complex Hilbert space \(H\), with center \(Z\), positive cone \(M_+\), projections \(\operatorname{Proj}(M)\) and predual \(M_*\). Inner products are linear in the first variable. We assume \(H\ne0\). Nothing is assumed separable or \(\sigma\)-finite.
- \(M_*^+\) is the set of normal positive functionals. The \(\sigma\)-strong topology is given by the seminorms \(x\mapsto\omega(x^*x)^{1/2}\), \(\omega\in M_*^+\); on bounded sets it agrees with the strong operator topology.
- For \(x\in M_+\), \(s(x)\) is the projection onto the closure of \(xH\). For a projection \(e\), \(c(e)\) is its central support. We write \(e\sim f\) and \(e\precsim f\) for Murray–von Neumann equivalence and subequivalence.
- A *trace* is a map \(\tau:M_+\to[0,\infty]\) that is additive, positively homogeneous (with \(0\cdot\infty=0\)) and satisfies \(\tau(x^*x)=\tau(xx^*)\) for \(x\in M\). It is *faithful*, *semifinite*, *normal* or *finite* as in the prerequisite lesson. We put
\[
F_\tau=\{x\in M_+\colon\tau(x)<\infty\},\qquad \mathfrak n_\tau=\{x\in M\colon\tau(x^*x)<\infty\},\qquad \mathfrak m_\tau=\operatorname{span}F_\tau ,
\]
and we write \(\tau(x)\) for the linear extension of \(\tau\) to \(\mathfrak m_\tau\).
- For \(x\in\mathfrak m_\tau\) put \(\|x\|_1=\tau(|x|)\), and for \(x\in\mathfrak n_\tau\) put \(\|x\|_2=\tau(x^*x)^{1/2}\). The operator norm is \(\|x\|\). For \(x\in\mathfrak m_\tau\) let \(\omega_x\) be the functional \(\omega_x(y)=\tau(yx)\) on \(M\).
- For a central element \(a\in Z_+\) and \(x\in M_+\), the product \(ax=a^{1/2}xa^{1/2}\) is positive.

## Results used from other lessons

*From the lesson Traces on von Neumann algebras.* Let \(\tau\) be a trace on \(M\).

- **The definition ideal** (Section 2). \(\mathfrak n_\tau\) and \(\mathfrak m_\tau\) are two-sided ideals, closed under the involution, with \(\mathfrak m_\tau\subseteq\mathfrak n_\tau\) and \(\mathfrak m_\tau\cap M_+=F_\tau\); every element of \(\mathfrak m_\tau\) is a product \(y^*z\) with \(y,z\in\mathfrak n_\tau\). The extension of \(\tau\) to \(\mathfrak m_\tau\) is linear, \(\tau(x^*)=\overline{\tau(x)}\), and
\[
\tau(xy)=\tau(yx)\quad(x,y\in\mathfrak n_\tau),\qquad \tau(ax)=\tau(xa)\quad(x\in\mathfrak m_\tau,\ a\in M).
\tag{0.1}
\]
Moreover \(x\in\mathfrak m_\tau\iff|x|\in\mathfrak m_\tau\iff|x^*|\in\mathfrak m_\tau\), and \(x\in\mathfrak n_\tau\iff|x|\in\mathfrak n_\tau\). A trace is monotone, and equivalent projections have equal trace.
- **Semifiniteness** (Section 2). The following are equivalent: \(\tau\) is semifinite; every nonzero projection majorizes a nonzero projection of finite trace; some net of projections of finite trace increases to \(1\); \(\mathfrak m_\tau\) is \(\sigma\)-weakly dense in \(M\).
- **Supports** (Section 3). If \(\tau\) is normal, the largest projection of trace \(0\) is central; its complement \(s(\tau)\) is the unique central projection such that \(\tau\) vanishes on \(M_+(1-s(\tau))\) and is faithful on \(Ms(\tau)\).
- **Sums** (Section 3). A sum of normal traces is a normal trace whose support is the supremum of the supports. A sum of semifinite normal traces is semifinite if the family is finite, or if the supports are mutually orthogonal.
- **The semifinite part** (Section 3). For every trace there is a unique central projection \(z\) such that \(\tau\) is semifinite on \(Mz\) and \(\tau(x)=\infty\) for every nonzero \(x\in M_+(1-z)\).
- **Finite algebras** (Section 4). If \(M\) is finite, \((e_n)\) are mutually orthogonal projections and \(f_n\sim e_n\), then \(f_n\to0\) \(\sigma\)-strongly. \(M\) is finite exactly when its finite normal traces separate \(M_+\).
- **The center-valued trace** (Section 5). A finite \(M\) has a unique linear map \(T:M\to Z\) with \(T(x^*x)=T(xx^*)\ge0\), \(T(ax)=aT(x)\) for \(a\in Z\), and \(T(1)=1\); uniqueness holds among all linear maps with these three properties. It is faithful, normal and \(\sigma\)-weakly continuous, \(T(a)=a\) for \(a\in Z\), and \(e\precsim f\iff T(e)\le T(f)\) for projections. Every finite trace \(\sigma\) on \(M\) satisfies \(\sigma(x)=\sigma(T(x))\) (Theorem 5.5).
- **Countable decomposability** (Section 5). \(M\) is \(\sigma\)-finite exactly when it has a faithful normal state. A finite \(M\) is the sum of orthogonal central pieces \(Mz_k\), \(\sum_kz_k=1\), each \(\sigma\)-finite, and each with a faithful normal finite trace.
- **Extension from a corner** (Section 6). A normal trace \(\tau_0\) on \(eMe\) extends uniquely to a normal trace \(\tau\) on \(M\) with \(\tau(1-c(e))=0\); \(\tau\) is faithful on \(Mc(e)\) if and only if \(\tau_0\) is faithful, and semifinite if and only if \(\tau_0\) is. The extension is \(\tau(x)=\sum_j\tau_0(v_jxv_j^*)\) for partial isometries \(v_j\) with \(v_jv_j^*\le e\) and \(\sum_jv_j^*v_j=c(e)\).
- **Amplification** (Section 6). If \(\tau\) is a normal trace on \(N\) and \((\varepsilon_i)\) is an orthonormal basis of \(K\), then \(\tilde\tau(x)=\sum_i\tau(x_{ii})\) is a normal trace on \(N\bar\otimes B(K)\), faithful or semifinite exactly when \(\tau\) is.
- **Semifinite algebras** (Section 6). \(M\) is semifinite exactly when it has a faithful semifinite normal trace.
- **The trace norm** (Section 7). For \(x\in\mathfrak m_\tau\) and \(y\in M\): \(|\tau(yx)|\le\tau(|yx|)\le\|y\|\,\|x\|_1\), \(\tau(|x^*|)=\tau(|x|)\), and \(\|x\|_1=\sup\{|\tau(yx)|:\|y\|\le1\}\). \(\|\cdot\|_1\) is a norm on \(\mathfrak m_\tau\) when \(\tau\) is faithful, with \(\|yx\|_1,\|xy\|_1\le\|y\|\|x\|_1\) and \(\|x^*\|_1=\|x\|_1\). If \(\tau\) is normal, \(\omega_x\in M_*\) and \(\|\omega_x\|=\|x\|_1\). If \(\tau\) is faithful, semifinite and normal, the \(\omega_x\) are norm dense in \(M_*\).
- **Projections** (Section 1). Orthogonal sums of equivalences are equivalences; central cuts preserve equivalence and \(c(e)=c(f)\) when \(e\sim f\); subprojections of finite projections and projections equivalent to finite ones are finite; the parallelogram law \(e\vee f-e\sim f-e\wedge f\); for a projection \(e\), the center of \(eMe\) is \(Ze\), the map \(a\mapsto ae\) is an isomorphism of \(Zc(e)\) onto \(Ze\), and \(e\) is finite exactly when \(eMe\) is. \(M\) is semifinite exactly when below every nonzero central projection there is a nonzero finite projection, and then below every nonzero projection there is one; there are central projections \(z_f+z_\infty=1\) with \(Mz_f\) finite and \(Mz_\infty\) properly infinite.

*From the lesson Projections and types of von Neumann algebras.*

- **Comparison** (Section 5). If \(e\precsim f\) and \(f\precsim e\) then \(e\sim f\). For projections \(e,f\) there is a central projection \(h\) with \(he\precsim hf\) and \((1-h)f\precsim(1-h)e\). If \(c(e)c(f)\ne0\), there are nonzero projections \(e_1\le e\) and \(f_1\le f\) with \(e_1\sim f_1\). If \(v\) implements \(e\sim f\), then \(y\mapsto vyv^*\) is an isomorphism of \(eMe\) onto \(fMf\); in particular a projection equivalent to an abelian projection is abelian (Lemma 6.2(1)).
- **Type decomposition** (Section 7). There are unique orthogonal central projections \(z_{\rm I},z_{\rm II},z_{\rm III}\) with sum \(1\) such that \(Mz_{\rm I}\) is of type I, \(Mz_{\rm II}\) of type II and \(Mz_{\rm III}\) of type III. Every projection is uniquely the sum of a finite and a properly infinite projection that are centrally orthogonal. A type I algebra has an abelian projection with central support \(1\), and a semifinite algebra has a finite projection with central support \(1\).
- **Abelian projections are smallest** (Section 9). If \(e\) is abelian and \(c(e)\le c(f)\), then \(e\precsim f\).
- **Type I factors** (Section 10). A factor of type I is isomorphic to \(B(K)\) for a Hilbert space \(K\).
- **Type I commutants** (Section 11). If \(M\) is of type I, so is \(M'\).
- **Halving** (Section 13). If \(M\) has no nonzero abelian projection, every projection is the sum of two orthogonal equivalent projections. A properly infinite projection \(e\) can be written as \(\sum_{n\ge1}e_n\) with mutually orthogonal \(e_n\sim e\).
- **Absorption** (Proposition 15.2). Let \(e\) be properly infinite. If \(f_1,f_2,\dots\) are mutually orthogonal projections with \(f_n\precsim e\), then \(\sum_nf_n\precsim e\). If \(f\) is \(\sigma\)-finite and \(c(f)\le c(e)\), then \(f\precsim e\).
- **Cyclic projections** (Section 4). For \(\xi\in H\), the projection \(p_\xi\) onto the closure of \(M'\xi\) lies in \(M\); it is the least projection of \(M\) that fixes \(\xi\), and the vector functional of \(\xi\) is faithful on \(p_\xi Mp_\xi\). So \(p_\xi\) is \(\sigma\)-finite.

*From the lessons The double commutant theorem, Spatial tensor products of von Neumann algebras, The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras, Polar decomposition of functionals and weak compactness in preduals, C\*-algebras, Integral representations of states and Decomposable operators and the diagonal algebra.*

- **Polar decomposition** (Proposition 7.2). Every \(x\in M\) is \(x=u|x|\) with \(|x|\in M\) and a partial isometry \(u\in M\); \(u^*u=s(x^*x)\) is the projection onto the closure of \(x^*H\), that is onto \((\ker x)^\perp\), and \(uu^*=s(xx^*)\) is the projection onto the closure of \(xH\). In particular \(s(x^*x)\sim s(xx^*)\).
- **\(\sigma\)-finite projections** (Section 9). \(M\) is \(\sigma\)-finite if every family of mutually orthogonal nonzero projections of \(M\) is countable, and this holds exactly when \(M\) has a faithful normal state. A projection \(e\) is \(\sigma\)-finite if \(eMe\) is, that is, if every family of mutually orthogonal nonzero projections below \(e\) is countable.
- **Minimal projections** (Section 6 and Section 10 of the lesson on types). A projection \(f\) is *minimal* if \(f\ne0\) and \(fMf=\mathbb Cf\), that is, if \(0\) and \(f\) are its only subprojections in \(M\). A factor that contains a minimal projection is isomorphic to \(B(L)\) for a Hilbert space \(L\).
- **Normal functionals** (normal positive functionals, Theorem 9.4 of the lesson on compact and trace-class operators and Section 10 of the lesson on W\*-algebras). Every \(\omega\in M_*^+\) has the form \(\omega(x)=\sum_n\langle x\xi_n,\xi_n\rangle\) with \(\sum_n\|\xi_n\|^2<\infty\). \(M_*\) is norm closed in the dual of \(M\), it is spanned by \(M_*^+\), and \(x\mapsto(\omega\mapsto\omega(x))\) is an isometric isomorphism of \(M\) onto \((M_*)^*\) that carries the \(\sigma\)-weak topology to the weak\(^*\) topology. An element \(x\) is positive exactly when \(\omega(x)\ge0\) for all \(\omega\in M_*^+\).
- **Normal maps** (Normal positive maps and their preadjoints, §NP-04). A positive linear map between von Neumann algebras is normal, that is, it preserves suprema of bounded increasing nets, exactly when it is \(\sigma\)-weakly continuous. A \(*\)-isomorphism between von Neumann algebras is normal, and it is a homeomorphism for the \(\sigma\)-weak and \(\sigma\)-strong topologies (Corollary 11.4). The image of a normal representation is a von Neumann algebra, and the cyclic representation of a normal positive functional is normal (Section 12).
- **Tomiyama's theorem** (Section 8). A projection of norm one \(E\) from a C\*-algebra onto a C\*-subalgebra \(B\) is positive and satisfies \(E(bxc)=bE(x)c\) for \(b,c\in B\).
- **Singular functionals** (Section 10 and Section 11). Every positive functional \(\varphi\) on \(M\) is uniquely \(\varphi_n+\varphi_s\) with \(\varphi_n\in M_*^+\) and \(\varphi_s\) positive and singular. A positive functional is singular exactly when every nonzero projection majorizes a nonzero projection on which it vanishes. A normal positive functional \(\omega\ne0\) has a support: a projection \(e\ne0\) with \(\omega(x)=\omega(exe)\) and \(\omega\) faithful on \(eMe\).
- **Pure states** (Representations and positive functionals, Definition 8.2 and Theorems 8.3 and 8.5(2), with Schur's lemma in Section 2 there, and the state space). For \(x\) positive in a C\*-algebra, \(\|x\|=\sup\{\rho(x):\rho\text{ a pure state}\}\). A state \(\rho\) is pure exactly when every positive functional \(\psi\le\rho\) is a multiple of \(\rho\), and exactly when its cyclic representation \(\pi_\rho\) is irreducible, \(\pi_\rho(A)'=\mathbb C1\).
- **Tensor products** (Sections 5–11). For von Neumann algebras \(M_k\) on \(H_k\): \(x\mapsto x\otimes1\) is an injective normal \(*\)-homomorphism of \(M_1\) into \(M_1\bar\otimes M_2\) when \(H_2\ne0\); for projections \(e\in M_1\), \(f\in M_2\), the corner \((e\otimes f)(M_1\bar\otimes M_2)(e\otimes f)\) is \(eM_1e\bar\otimes fM_2f\) on \(eH_1\otimes fH_2\); \((M\otimes1_K)'=M'\bar\otimes B(K)\); the flip is an isomorphism \(M_1\bar\otimes M_2\cong M_2\bar\otimes M_1\). For normal functionals \(\varphi,\omega\) there is a unique normal functional \(\varphi\otimes\omega\) with \((\varphi\otimes\omega)(x\otimes y)=\varphi(x)\omega(y)\); it is positive when both are, and faithful when both are faithful and positive. For a unit vector \(\eta\in H_2\) and \(X\in M_1\bar\otimes M_2\), the slice \(R_\eta^*XR_\eta\) lies in \(M_1\), where \(R_\eta\xi=\xi\otimes\eta\); the map \(X\mapsto R_\eta^*XR_\eta\) is normal and positive, and \(R_\eta^*(a\otimes1)X(b\otimes1)R_\eta=a\,R_\eta^*XR_\eta\,b\) for \(a,b\in M_1\). Two normal maps that agree on the algebraic tensor product agree on \(M_1\bar\otimes M_2\).
- **Normal homomorphisms** (Theorem 8.2). For a von Neumann algebra \(M\subseteq B(H)\) and a normal unital \(*\)-homomorphism \(\pi:M\to B(L)\), there are a Hilbert space \(R\) and an isometry \(V:L\to H\otimes R\) such that \(VV^*\) commutes with \(M\otimes1_R\) and \(\pi(x)=V^*(x\otimes1_R)V\) for \(x\in M\).
- **Normal isomorphisms** (Corollary 8.3). Let \(\theta:M_1\to M_2\) be a normal \(*\)-isomorphism with \(H_1\ne0\). There are a Hilbert space \(R\) and a projection \(e'\in(M_1\otimes1_R)'\), with the projection onto the closed span of \((M_1\otimes1_R)'e'(H_1\otimes R)\) equal to \(1\), such that \(M_2\) is spatially isomorphic to the induced algebra \((M_1\otimes1_R)_{e'}\), the operators \((x\otimes1)e'\) restricted to \(e'(H_1\otimes R)\). The commutant of an induced algebra \(N_{e'}\) is the reduced algebra \(e'N'e'\) on \(e'(H_1\otimes R)\) (Proposition 6.1).
- **Functionals on the predual** (Theorem 2.2, Theorem 10.2 and Theorem 11.2). For \(\varphi\in M_*\) there is exactly one pair of a partial isometry \(v\in M\) and a positive normal functional \(|\varphi|\) with \(\varphi(x)=|\varphi|(xv)\) for \(x\in M\) and \(v^*v=s(|\varphi|)\); then \(|\varphi|(x)=\varphi(xv^*)\) and \(\||\varphi|\|=\|\varphi\|\). A subset \(K\subseteq M_*\) is relatively \(\sigma(M_*,M)\)-compact exactly when it is bounded and \(\sup_{\psi\in K}|\psi(p_n)|\to0\) for every decreasing sequence of projections \(p_n\) with infimum \(0\). If \(K\) is relatively \(\sigma(M_*,M)\)-compact and \((a_i)\) is a bounded net converging to \(0\) \(\sigma\)-strongly\(^*\), then \(\sup_{\psi\in K}|\psi(a_i)|\to0\).
- **Commutative C\*-algebras** (Section 2). A unital commutative C\*-algebra is isometrically \(*\)-isomorphic to \(C(\Omega)\) for a compact Hausdorff space \(\Omega\).
- **Multiplication algebras** (Theorem 7.1(5) of the lesson on decomposable operators). For a \(\sigma\)-finite measure space \((X,\mu)\), the multiplication operators by \(L^\infty(X,\mu)\) form a maximal abelian von Neumann algebra on \(L^2(X,\mu)\).

*From measure theory and operator theory.*

- **Riesz–Markov.** For a compact Hausdorff space \(\Omega\) and a positive linear functional \(\ell\) on \(C(\Omega)\) there is a unique positive Radon measure \(\mu\) with \(\ell(f)=\int f\,d\mu\); it is finite, \(\mu(\Omega)=\ell(1)\), and \(C(\Omega)\) is dense in \(L^1(\Omega,\mu)\). Proved in Haar measure on locally compact groups, Theorem 2.2 and Proposition 3.1(4).
- **Closed operators.** Let \(T\) be a closed densely defined operator on \(H\). Its adjoint \(T^*\) is closed and densely defined, and \(T^{**}=T\); more generally a densely defined operator \(S\) is closable exactly when \(S^*\) is densely defined, and then its closure is \(S^{**}\). \(T\) is *symmetric* if \(T\subseteq T^*\), and *self-adjoint* if \(T=T^*\). There are a positive self-adjoint operator \(|T|\) with domain \(D(|T|)=D(T)\) and \(\||T|\xi\|=\|T\xi\|\), and a partial isometry \(U\) with \(T=U|T|\); \(|T|\) and \(U\) are unique with \(\ker U=\ker T\). A positive self-adjoint operator has a spectral resolution; its spectral projections \(1_{[0,n]}(|T|)\) increase strongly to \(1\) and have range in \(D(|T|)\). These are proved in Analytic elements and strip arguments, Lemmas 7.2–7.4: Lemma 7.2 treats linear operators, and the proofs of Lemmas 7.3 and 7.4 apply verbatim to a linear \(T\); there \(U\) is unique once \(\ker U=\ker T\), which is \(\ker|T|\). The spectral statements are in Spectral calculus with its domains retained, SK-05, SK-06 and SK-09.
- **Arens–Mackey topology.** On bounded subsets of a von Neumann algebra, the Mackey topology \(\tau(M,M_*)\) coincides with the \(\sigma\)-strong\(^*\) topology. It is used only in Corollary 5.5. Proved in Polar decomposition of functionals and weak compactness in preduals, Theorem 11.2 and Remark 11.3.

## 1. Integrable elements and duality

Throughout this section \(\tau\) is a faithful semifinite normal trace on \(M\).

The prerequisite lesson introduced the norm \(\|x\|_1=\tau(|x|)\) on \(\mathfrak m_\tau\) and showed that \(x\mapsto\omega_x\) is isometric with dense range in \(M_*\). Let \(L^1(M,\tau)\) be the completion of \((\mathfrak m_\tau,\|\cdot\|_1)\). The map \(x\mapsto\omega_x\) extends to an isometric isomorphism of \(L^1(M,\tau)\) onto \(M_*\), and we use it to regard every element of \(L^1(M,\tau)\) as a normal functional. For \(y\in M\) and \(x\in L^1(M,\tau)\) we write
\[
\tau(yx)=\tau(xy)=\omega_x(y).
\tag{1.1}
\]
For \(x\in\mathfrak m_\tau\) this is the old meaning, by (0.1), and \(|\tau(yx)|\le\|y\|\,\|x\|_1\).

**Theorem 1.1** (Duality). The map \(\Phi\) that sends \(y\in M\) to the functional \(x\mapsto\tau(yx)\) on \(L^1(M,\tau)\) is an isometric linear bijection of \(M\) onto the dual space \(L^1(M,\tau)^*\). It carries the \(\sigma\)-weak topology of \(M\) to the weak\(^*\) topology of \(L^1(M,\tau)^*\).

**Proof.** Let \(j:L^1(M,\tau)\to M_*\), \(j(x)=\omega_x\), be the isometric isomorphism above. The map \(y\mapsto(\omega\mapsto\omega(y))\) is an isometric isomorphism of \(M\) onto \((M_*)^*\) that carries the \(\sigma\)-weak topology to the weak\(^*\) topology (background). Composing with the transpose of \(j\), which is an isometric isomorphism of \((M_*)^*\) onto \(L^1(M,\tau)^*\) and a homeomorphism for the weak\(^*\) topologies, we get \(\Phi(y)(x)=\omega_x(y)=\tau(yx)\). \(\square\)

So \(M\) is the dual of \(L^1(M,\tau)\), and we may think of \(M\) as \(L^\infty(M,\tau)\), with the operator norm in the role of the essential supremum. The elements of \(\mathfrak m_\tau\) lie in both spaces. The next result identifies them inside \(L^1(M,\tau)\): they are the integrable elements that are also bounded.

**Proposition 1.2** (Bounded densities). For \(x\in L^1(M,\tau)\) put
\[
N_\infty(x)=\sup\{|\tau(yx)|:\ y\in\mathfrak m_\tau,\ \|y\|_1\le1\}\in[0,\infty].
\]
Then \(x\) belongs to \(\mathfrak m_\tau\) if and only if \(N_\infty(x)<\infty\), and in that case \(N_\infty(x)=\|x\|\). Equivalently: a normal functional \(\omega\) on \(M\) equals \(\omega_x\) for some \(x\in\mathfrak m_\tau\) exactly when \(\omega\) is bounded on the \(\|\cdot\|_1\)-unit ball of \(\mathfrak m_\tau\).

**Proof.** Let \(x\in\mathfrak m_\tau\). For \(y\in\mathfrak m_\tau\), (0.1) and the trace-norm inequality give \(|\tau(yx)|=|\tau(xy)|\le\|x\|\,\|y\|_1\), so \(N_\infty(x)\le\|x\|\). By Theorem 1.1, \(\|x\|\) is the norm of \(\Phi(x)\), the supremum of \(|\tau(xy)|\) over the unit ball of \(L^1(M,\tau)\); since \(\mathfrak m_\tau\) is dense there, the supremum over its unit ball is the same. So \(N_\infty(x)=\|x\|\).

Conversely, let \(C=N_\infty(x)<\infty\). The functional \(y\mapsto\tau(yx)\) on \(\mathfrak m_\tau\) has norm at most \(C\) for \(\|\cdot\|_1\), so it extends to a bounded functional on \(L^1(M,\tau)\), and Theorem 1.1 gives \(z\in M\) with \(\|z\|=C\) and \(\tau(yx)=\tau(zy)\) for all \(y\in\mathfrak m_\tau\). We show that \(z\in\mathfrak m_\tau\). Let \(z=u|z|\) be the polar decomposition, and choose projections \(e_i\in F_\tau\) that increase to \(1\) (semifiniteness). The element \(e_iu^*\) lies in \(\mathfrak m_\tau\), because \(\mathfrak m_\tau\) is an ideal containing \(e_i\). By (0.1),
\[
\tau(e_i|z|e_i)=\tau\bigl((e_iu^*)(ze_i)\bigr)=\tau\bigl(ze_i\,e_iu^*\bigr)=\tau(z\,e_iu^*)=\tau(e_iu^*\,x),
\]
and the last number is at most \(\|e_iu^*\|\,\|x\|_1\le\|x\|_1\) in absolute value. On the other hand \(e_i|z|e_i=(|z|^{1/2}e_i)^*(|z|^{1/2}e_i)\), so the trace property gives \(\tau(e_i|z|e_i)=\tau(|z|^{1/2}e_i|z|^{1/2})\), and these numbers increase to \(\tau(|z|)\) by normality. Hence \(\tau(|z|)\le\|x\|_1<\infty\), and \(z\in\mathfrak m_\tau\). Now \(\omega_z\) and \(\omega_x\) are normal and agree on \(\mathfrak m_\tau\), which is \(\sigma\)-weakly dense; so they are equal, and \(x=z\) in \(L^1(M,\tau)\). \(\square\)

**Example 1.3** (\(B(H)\) and the trace class). Let \(M=B(H)\) and let \(\tau=\operatorname{Tr}\) be the usual trace, \(\operatorname{Tr}(x)=\sum_i\langle x\varepsilon_i,\varepsilon_i\rangle\) for an orthonormal basis. For a unit vector \(\xi\) and any unit vector \(\eta\), the rank-one operator \(r=\langle\,\cdot\,,\xi\rangle\eta\) has norm \(1\), and for \(y\in\mathfrak m_{\operatorname{Tr}}\) the linear extension of the trace gives \(\operatorname{Tr}(yr)=\langle y\eta,\xi\rangle\). The trace-norm inequality gives \(|\langle y\eta,\xi\rangle|\le\|y\|_1\), so
\[
\|y\|\le\|y\|_1\qquad(y\in\mathfrak m_{\operatorname{Tr}}).
\]
Consequently, for \(x\in L^1(B(H),\operatorname{Tr})\) and \(y\in\mathfrak m_{\operatorname{Tr}}\) with \(\|y\|_1\le1\), \(|\operatorname{Tr}(yx)|\le\|y\|\,\|x\|_1\le\|x\|_1\). So \(N_\infty(x)\le\|x\|_1<\infty\) for every \(x\), and Proposition 1.2 shows that \(L^1(B(H),\operatorname{Tr})=\mathfrak m_{\operatorname{Tr}}\): no completion is needed. These are the trace-class operators, and Theorem 1.1 is the classical statement that \(B(H)\) is the dual of the trace class. In contrast, for a diffuse algebra such as \(L^\infty[0,1]\) the completion adds unbounded elements (Example 1.4).

**Example 1.4** (Measure spaces). Let \((X_k,\mu_k)_{k\in K}\) be finite measure spaces and let \((X,\mu)\) be their disjoint union: a function on \(X\) is measurable when its restriction to each \(X_k\) is, and \(\int_Xf\,d\mu=\sum_k\int_{X_k}f\,d\mu_k\) for \(f\ge0\). Put \(L^p(X,\mu)=\{f:\|f\|_p<\infty\}\) modulo null functions, for \(p=1,2\), and let \(L^\infty(X,\mu)\) be the bounded families \((f_k)\) with \(f_k\in L^\infty(X_k,\mu_k)\). Every \(\sigma\)-finite measure space has this form, with \(K\) countable.

Let \(M=L^\infty(X,\mu)\) act on \(L^2(X,\mu)=\bigoplus_kL^2(X_k,\mu_k)\) by multiplication. Each summand is a maximal abelian von Neumann algebra on \(L^2(X_k,\mu_k)\) (background), so \(M\) is a von Neumann algebra, the direct sum of these. Put \(\tau(f)=\int_Xf\,d\mu\) for \(f\in M_+\). Then:

- \(\tau\) is a trace, since \(M\) is commutative. It is faithful. It is normal: \(\tau(f)=\sum_k\langle f1_{X_k},1_{X_k}\rangle\) is a sum of vector functionals. It is semifinite: the projections \(\sum_{k\in F}1_{X_k}\), \(F\) finite, have finite trace and increase to \(1\).
- \(F_\tau\) consists of the bounded integrable functions \(f\ge0\), so \(\mathfrak m_\tau=L^\infty\cap L^1\), and \(\|f\|_1=\int|f|\,d\mu\) is the \(L^1\)-norm. Likewise \(\mathfrak n_\tau=L^\infty\cap L^2\) with the \(L^2\)-norm.
- \(L^\infty\cap L^1\) is dense in \(L^1(X,\mu)\): for \(f\in L^1\), the functions \(f\,1_{\{|f|\le n\}}\sum_{k\in F}1_{X_k}\) converge to \(f\) in \(L^1\) by dominated convergence, along \(n\to\infty\) and finite sets \(F\) increasing to \(K\). As \(L^1(X,\mu)\) is complete, \(L^1(M,\tau)=L^1(X,\mu)\), and the pairing (1.1) is \(\tau(gf)=\int_Xgf\,d\mu\).

Theorem 1.1 now says that \(L^\infty(X,\mu)\) is the dual of \(L^1(X,\mu)\) through \(g\mapsto(f\mapsto\int gf\,d\mu)\), and Proposition 1.2 says that an integrable \(f\) is essentially bounded exactly when \(g\mapsto\int gf\,d\mu\) is bounded on the unit ball of \(L^\infty\cap L^1\) for the \(L^1\)-norm, with bound \(\|f\|_\infty\). By Theorem 3.3, every commutative von Neumann algebra that carries a faithful semifinite normal trace is of this form.

**Remark 1.5.** Faithfulness is used to make \(\|\cdot\|_1\) a norm. If \(\tau\) is only semifinite and normal, \(\|\cdot\|_1\) vanishes exactly on \(\mathfrak m_\tau(1-s(\tau))=\mathfrak m_\tau\cap M(1-s(\tau))\), and the same results hold for the algebra \(Ms(\tau)\), whose predual is the set of normal functionals on \(M\) that vanish on \(M(1-s(\tau))\).

## 2. The Hilbert space of a trace

Throughout this section \(\tau\) is a faithful semifinite normal trace on \(M\). A reference for Sections 1–3 is [Kostecki, Section 5.2].

**Definition 2.1.** For \(x,y\in\mathfrak n_\tau\) put \(\langle x,y\rangle_2=\tau(y^*x)\); this makes sense because \(y^*x\in\mathfrak m_\tau\). It is a sesquilinear form, positive, and definite because \(\tau\) is faithful: \(\langle x,x\rangle_2=\tau(x^*x)=0\) forces \(x=0\). The completion of \(\mathfrak n_\tau\) is a Hilbert space \(L^2(M,\tau)\), and \(\mathfrak n_\tau\) is a dense subspace of it. The norm is \(\|x\|_2\).

**Lemma 2.2** (The two actions). Let \(a\in M\) and \(x\in\mathfrak n_\tau\).

1. \(\|ax\|_2\le\|a\|\,\|x\|_2\), \(\|xa\|_2\le\|a\|\,\|x\|_2\) and \(\|x^*\|_2=\|x\|_2\).
2. There are bounded operators \(\pi_\tau(a)\) and \(\rho_\tau(a)\) on \(L^2(M,\tau)\) with \(\pi_\tau(a)x=ax\) and \(\rho_\tau(a)x=xa\). The map \(\pi_\tau\) is a unital \(*\)-homomorphism. The map \(\rho_\tau\) is linear and unital, with \(\rho_\tau(ab)=\rho_\tau(b)\rho_\tau(a)\) and \(\rho_\tau(a^*)=\rho_\tau(a)^*\). Every \(\pi_\tau(a)\) commutes with every \(\rho_\tau(b)\).
3. The map \(x\mapsto x^*\) extends to a conjugate-linear isometry \(J\) of \(L^2(M,\tau)\) with \(J^2=1\), \(\langle J\xi,J\eta\rangle_2=\langle\eta,\xi\rangle_2\), and \(J\pi_\tau(a)J=\rho_\tau(a^*)\).
4. For \(x,y\in\mathfrak n_\tau\), \(\langle\pi_\tau(a)x,y\rangle_2=\tau(a\,xy^*)=\omega_{xy^*}(a)\). The maps \(\pi_\tau\) and \(\rho_\tau\) are injective and normal, in the sense that \(a\mapsto\langle\pi_\tau(a)\xi,\eta\rangle_2\) and \(a\mapsto\langle\rho_\tau(a)\xi,\eta\rangle_2\) lie in \(M_*\) for all vectors \(\xi,\eta\).
5. \(\mathfrak m_\tau\) is dense in \(L^2(M,\tau)\). If \(e_i\in F_\tau\) are projections that increase to \(1\), then \(\pi_\tau(e_i)\to1\) and \(\rho_\tau(e_i)\to1\) strongly.

We call \(\pi_\tau\) the *standard representation* of \(M\) defined by \(\tau\), \(\rho_\tau\) the *right representation* and \(J\) the *conjugation*. When no confusion arises we write \(\pi,\rho\).

**Proof.** (1) Since \(x^*a^*ax\le\|a\|^2x^*x\), monotonicity of \(\tau\) gives the first inequality. By the trace identity for \(z=xa\), \(\tau(a^*x^*xa)=\tau(xaa^*x^*)\le\|a\|^2\tau(xx^*)=\|a\|^2\tau(x^*x)\). Finally \(\tau(xx^*)=\tau(x^*x)\).

(2) By (1), left and right multiplication by \(a\) are bounded on \(\mathfrak n_\tau\) for \(\|\cdot\|_2\), with norm at most \(\|a\|\), and extend to \(L^2(M,\tau)\). The algebraic rules hold on \(\mathfrak n_\tau\) and pass to the closure. For adjoints, let \(x,y\in\mathfrak n_\tau\). Then \(\langle ax,y\rangle_2=\tau(y^*ax)=\tau((a^*y)^*x)=\langle x,a^*y\rangle_2\). Also \(\langle xa,y\rangle_2=\tau(y^*x\,a)=\tau(a\,y^*x)\) by (0.1), since \(y^*x\in\mathfrak m_\tau\), and \(\tau(a\,y^*x)=\tau((ya^*)^*x)=\langle x,ya^*\rangle_2\). The commutation is associativity: \((ax)b=a(xb)\).

(3) By (1), \(J\) is isometric on \(\mathfrak n_\tau\), so it extends; \(J^2=1\) is clear. For \(x,y\in\mathfrak n_\tau\), \(\langle x^*,y^*\rangle_2=\tau(yx^*)=\tau(x^*y)=\langle y,x\rangle_2\) by (0.1), and this passes to limits. Finally \(J\pi_\tau(a)Jx=(ax^*)^*=xa^*=\rho_\tau(a^*)x\).

(4) By (0.1) with the elements \(y^*\) and \(ax\) of \(\mathfrak n_\tau\), \(\tau(y^*\,ax)=\tau(ax\,y^*)\), and \(xy^*\in\mathfrak m_\tau\). So \(a\mapsto\langle\pi_\tau(a)x,y\rangle_2\) is \(\omega_{xy^*}\), which is normal. For arbitrary vectors \(\xi,\eta\), approximate them by \(x,y\in\mathfrak n_\tau\); the functionals converge in norm, and \(M_*\) is norm closed. For \(\rho_\tau\), part (3) gives \(\langle\rho_\tau(a)\xi,\eta\rangle_2=\langle J\pi_\tau(a^*)J\xi,\eta\rangle_2=\langle\pi_\tau(a)J\eta,J\xi\rangle_2\), which is normal in \(a\). If \(\pi_\tau(a)=0\), then \(ae_i=\pi_\tau(a)e_i=0\) for projections \(e_i\in F_\tau\) increasing to \(1\), so \(a=0\); and \(\rho_\tau(a)=J\pi_\tau(a^*)J\).

(5) For \(y\in\mathfrak n_\tau\), \(e_iy\in\mathfrak m_\tau\), and \(\|y-e_iy\|_2^2=\tau(y^*(1-e_i)y)=\tau(y^*y)-\tau(y^*e_iy)\to0\) because \(y^*e_iy\uparrow y^*y\) and \(\tau\) is normal. So \(\mathfrak m_\tau\) is dense, and \(\pi_\tau(e_i)\to1\) on the dense set \(\mathfrak n_\tau\); being contractions, they converge strongly. Then \(\rho_\tau(e_i)=J\pi_\tau(e_i)J\to1\) strongly. \(\square\)

The next two results decide when a vector of \(L^2(M,\tau)\), or an element of \(M\), comes from \(\mathfrak n_\tau\). They are the Hilbert-space analogues of Proposition 1.2.

**Proposition 2.3** (Square-integrable elements). For \(x\in M\) put
\[
N_2(x)=\sup\{|\tau(y^*x)|:\ y\in\mathfrak m_\tau,\ \|y\|_2\le1\}\in[0,\infty].
\]
Then \(x\in\mathfrak n_\tau\) if and only if \(N_2(x)<\infty\), and then \(N_2(x)=\|x\|_2\).

**Proof.** The number \(\tau(y^*x)\) is defined because \(\mathfrak m_\tau\) is an ideal. If \(x\in\mathfrak n_\tau\), then \(\tau(y^*x)=\langle x,y\rangle_2\), so \(N_2(x)\le\|x\|_2\) by Cauchy–Schwarz, and equality holds because \(\mathfrak m_\tau\) is dense in \(L^2(M,\tau)\).

Conversely let \(N_2(x)<\infty\). The map \(y\mapsto\overline{\tau(y^*x)}\) is linear and bounded on the dense subspace \(\mathfrak m_\tau\), so the Riesz representation theorem gives \(\xi\in L^2(M,\tau)\) with \(\tau(y^*x)=\langle\xi,y\rangle_2\) for all \(y\in\mathfrak m_\tau\). Let \(e_i\in F_\tau\) be projections increasing to \(1\). For \(y\in\mathfrak m_\tau\),
\[
\langle e_ix,y\rangle_2=\tau(y^*e_ix)=\tau((e_iy)^*x)=\langle\xi,e_iy\rangle_2=\langle\pi_\tau(e_i)\xi,y\rangle_2 ,
\]
where \(e_ix\in\mathfrak m_\tau\). By density, \(e_ix=\pi_\tau(e_i)\xi\) in \(L^2(M,\tau)\). Hence \(\tau(x^*e_ix)=\|e_ix\|_2^2\le\|\xi\|_2^2\). As \(x^*e_ix\uparrow x^*x\), normality gives \(\tau(x^*x)\le\|\xi\|_2^2<\infty\). \(\square\)

**Proposition 2.4** (Bounded vectors). For \(\xi\in L^2(M,\tau)\) the following are equivalent:

- (i) \(\xi\in\mathfrak n_\tau\);
- (ii) \(N_\infty(\xi)=\sup\{|\langle\xi,y\rangle_2|:\ y\in\mathfrak m_\tau,\ \|y\|_1\le1\}<\infty\);
- (iii) \(N_\ell(\xi)=\sup\{\|\pi_\tau(a)\xi\|_2:\ a\in\mathfrak n_\tau,\ \|a\|_2\le1\}<\infty\);
- (iv) \(N_r(\xi)=\sup\{\|\rho_\tau(a)\xi\|_2:\ a\in\mathfrak n_\tau,\ \|a\|_2\le1\}<\infty\).

When they hold, and \(\xi=x\in\mathfrak n_\tau\), all three suprema equal the operator norm \(\|x\|\).

**Proof.** (i)\(\Rightarrow\)(iii): for \(a\in\mathfrak n_\tau\), \(\pi_\tau(a)x=ax=\rho_\tau(x)a\), so \(\|ax\|_2\le\|x\|\,\|a\|_2\) by Lemma 2.2(1). Thus \(N_\ell(x)\le\|x\|\).

(iii)\(\Rightarrow\)(ii): let \(y\in\mathfrak m_\tau\) with polar decomposition \(y=u|y|\). Then \(k=|y^*|=u|y|u^*\) satisfies \(ku=u|y|=y\), and \(k\in F_\tau\), so \(k^{1/2}\in\mathfrak n_\tau\) with \(\|k^{1/2}\|_2^2=\tau(k)=\tau(|y|)=\|y\|_1\). Write \(y=k^{1/2}(k^{1/2}u)\). As \(\pi_\tau(k^{1/2})\) is self-adjoint,
\[
|\langle\xi,y\rangle_2|=|\langle\pi_\tau(k^{1/2})\xi,\,k^{1/2}u\rangle_2|\le\|\pi_\tau(k^{1/2})\xi\|_2\,\|k^{1/2}u\|_2\le N_\ell(\xi)\,\|k^{1/2}\|_2\cdot\|k^{1/2}\|_2=N_\ell(\xi)\,\|y\|_1 ,
\]
using Lemma 2.2(1) for \(\|k^{1/2}u\|_2\le\|k^{1/2}\|_2\). So \(N_\infty(\xi)\le N_\ell(\xi)\).

(ii)\(\Rightarrow\)(i): the map \(w\mapsto\langle\xi,w^*\rangle_2\) is linear on \(\mathfrak m_\tau\) and bounded for \(\|\cdot\|_1\), since \(\|w^*\|_1=\|w\|_1\). By Theorem 1.1 there is \(x'\in M\) with \(\|x'\|=N_\infty(\xi)\) and \(\langle\xi,w^*\rangle_2=\tau(wx')\) for \(w\in\mathfrak m_\tau\); with \(w=y^*\) this reads \(\langle\xi,y\rangle_2=\tau(y^*x')\). Let \(e_i\in F_\tau\) be projections increasing to \(1\). For \(y\in\mathfrak m_\tau\),
\[
\langle e_ix',y\rangle_2=\tau(y^*e_ix')=\tau((e_iy)^*x')=\langle\xi,e_iy\rangle_2=\langle\pi_\tau(e_i)\xi,y\rangle_2 ,
\]
so \(e_ix'=\pi_\tau(e_i)\xi\). Then \(\tau(x'^*e_ix')=\|\pi_\tau(e_i)\xi\|_2^2\le\|\xi\|_2^2\), and normality gives \(\tau(x'^*x')\le\|\xi\|_2^2\): so \(x'\in\mathfrak n_\tau\). Finally \(\pi_\tau(e_i)\xi\to\xi\) and \(e_ix'\to x'\) in \(L^2(M,\tau)\) (Lemma 2.2(5)), so \(\xi=x'\).

Norms: for \(x\in\mathfrak n_\tau\), \(N_\infty(x)=\sup\{|\tau(wx)|:w\in\mathfrak m_\tau,\|w\|_1\le1\}\), which is \(\|x\|\) by Theorem 1.1 and density. With the inequalities above, \(\|x\|=N_\infty(x)\le N_\ell(x)\le\|x\|\).

(i)\(\Leftrightarrow\)(iv): \(J\) is isometric, maps \(\mathfrak n_\tau\) onto itself, and \(\|\rho_\tau(a)\xi\|_2=\|J\rho_\tau(a)\xi\|_2=\|\pi_\tau(a^*)J\xi\|_2\) by Lemma 2.2(3). As \(a\mapsto a^*\) preserves \(\mathfrak n_\tau\) and \(\|\cdot\|_2\), \(N_r(\xi)=N_\ell(J\xi)\), and \(\|x^*\|=\|x\|\). \(\square\)

**Example 2.5.** (a) *\(B(H)\).* By Example 1.3, \(\|y\|\le\|y\|_1\) for \(y\in\mathfrak m_{\operatorname{Tr}}\). For \(x\in\mathfrak n_{\operatorname{Tr}}\) this gives \(\|x\|^2=\|x^*x\|\le\|x^*x\|_1=\|x\|_2^2\). Let \(\xi\in L^2(B(H),\operatorname{Tr})\) be the limit of \(x_n\in\mathfrak n_{\operatorname{Tr}}\). For \(a\in\mathfrak n_{\operatorname{Tr}}\), \(\|\pi(a)\xi\|_2=\lim_n\|ax_n\|_2\le\|a\|\,\|\xi\|_2\le\|a\|_2\|\xi\|_2\). So \(N_\ell(\xi)\le\|\xi\|_2\), and \(\xi\in\mathfrak n_{\operatorname{Tr}}\) by Proposition 2.4. Every vector is bounded: \(L^2(B(H),\operatorname{Tr})\) is the space of Hilbert–Schmidt operators, with \(\|x\|\le\|x\|_2\).

(b) *\(L^\infty[0,1]\).* With Lebesgue measure, \(L^2(M,\tau)=L^2[0,1]\) by Example 1.4, and for \(f\in L^2\), \(N_\ell(f)=\sup\{\|gf\|_2:\ g\in L^\infty,\ \|g\|_2\le1\}\). For \(f(t)=t^{-1/4}\) and \(g=\delta^{-1/2}1_{[0,\delta]}\), \(\|gf\|_2^2=\delta^{-1}\int_0^\delta t^{-1/2}\,dt=2\delta^{-1/2}\to\infty\). So \(f\) is not a bounded vector, although it lies in \(L^2\). Here the bounded vectors are exactly the essentially bounded functions, and Proposition 2.4 recovers \(\|f\|_\infty=\sup\{\|gf\|_2:\|g\|_2\le1\}\).

## 3. The commutation theorem

**Theorem 3.1** (The commutation theorem). Let \(\tau\) be a faithful semifinite normal trace on \(M\). Then \(\pi_\tau(M)\) and \(\rho_\tau(M)\) are von Neumann algebras on \(L^2(M,\tau)\),
\[
\pi_\tau(M)'=\rho_\tau(M),\qquad \rho_\tau(M)'=\pi_\tau(M),\qquad J\pi_\tau(M)J=\rho_\tau(M).
\tag{3.1}
\]
\(\pi_\tau\) is a normal \(*\)-isomorphism of \(M\) onto \(\pi_\tau(M)\), and \(\rho_\tau\) is a normal anti-isomorphism of \(M\) onto \(\rho_\tau(M)\). The center of \(\pi_\tau(M)\) is \(\pi_\tau(Z)=\rho_\tau(Z)\).

**Proof.** By Lemma 2.2, \(\pi_\tau\) is a faithful normal representation, so its image is a von Neumann algebra (background), and \(\pi_\tau\) is an isomorphism onto it. Since \(J\) is a conjugate-linear isometry with \(J^2=1\), the map \(X\mapsto JXJ\) preserves products, adjoints and strong limits. By Lemma 2.2(3), \(\rho_\tau(M)=J\pi_\tau(M)J\); so \(\rho_\tau(M)\) is strongly closed, contains \(1\) and is closed under adjoints: a von Neumann algebra.

By Lemma 2.2(2), \(\rho_\tau(M)\subseteq\pi_\tau(M)'\). For the converse, let \(b\in\pi_\tau(M)'\) and \(x\in\mathfrak n_\tau\). Consider the vector \(\xi=bx\). For \(a\in\mathfrak n_\tau\),
\[
\|\pi_\tau(a)\xi\|_2=\|b\,\pi_\tau(a)x\|_2=\|b(ax)\|_2\le\|b\|\,\|ax\|_2\le\|b\|\,\|x\|\,\|a\|_2 .
\]
So \(N_\ell(\xi)\le\|b\|\|x\|\), and Proposition 2.4 gives an element \(w\in\mathfrak n_\tau\) with \(bx=w\). For \(a\in\mathfrak n_\tau\),
\[
\rho_\tau(w)a=aw=\pi_\tau(a)bx=b\,\pi_\tau(a)x=b(ax)=b\,\rho_\tau(x)a .
\]
Both \(\rho_\tau(w)\) and \(b\rho_\tau(x)\) are bounded and agree on the dense set \(\mathfrak n_\tau\), so \(b\rho_\tau(x)=\rho_\tau(w)\in\rho_\tau(M)\). Now let \(e_i\in F_\tau\) be projections increasing to \(1\); they lie in \(\mathfrak n_\tau\). By Lemma 2.2(5), \(b\rho_\tau(e_i)\to b\) strongly, and \(\rho_\tau(M)\) is strongly closed; so \(b\in\rho_\tau(M)\). This proves \(\pi_\tau(M)'=\rho_\tau(M)\), and then \(\rho_\tau(M)'=\pi_\tau(M)''=\pi_\tau(M)\) by the bicommutant theorem.

\(\rho_\tau\) is injective and normal by Lemma 2.2(4), and it reverses products. For \(a\in Z\) and \(x\in\mathfrak n_\tau\), \(ax=xa\), so \(\pi_\tau(a)=\rho_\tau(a)\). The center of \(\pi_\tau(M)\) is \(\pi_\tau(M)\cap\pi_\tau(M)'=\pi_\tau(M)\cap\rho_\tau(M)\), and \(\pi_\tau\) maps \(Z\) onto the center of \(\pi_\tau(M)\) because it is an isomorphism. \(\square\)

When \(\tau(1)<\infty\), the vector \(1\in\mathfrak n_\tau\) is cyclic for \(\pi_\tau(M)\) and for \(\rho_\tau(M)\), since \(\pi_\tau(x)1=x=\rho_\tau(x)1\); by (3.1) it is then also separating for both.

**Example 3.2** (Matrices). Let \(M=M_n(\mathbb C)\) and \(\tau=\operatorname{Tr}\). Then \(L^2(M,\tau)\) is \(M_n(\mathbb C)\) with \(\langle x,y\rangle_2=\operatorname{Tr}(y^*x)\), \(\pi\) and \(\rho\) are left and right multiplication, and \(J\) is the adjoint. Theorem 3.1 is here elementary: if a linear map \(T\) of \(M_n(\mathbb C)\) commutes with every left multiplication, then \(T(x)=T(x\cdot1)=xT(1)\), so \(T=\rho(T(1))\).

**Theorem 3.3** (Commutative algebras). Let \(A\) be a commutative von Neumann algebra carrying a faithful semifinite normal trace \(\tau\).

1. \(\pi_\tau(A)\) is maximal abelian on \(L^2(A,\tau)\): \(\pi_\tau(A)'=\pi_\tau(A)\).
2. There are compact Hausdorff spaces \(\Omega_k\) (\(k\in K\)) with finite positive Baire measures \(\mu_k\), and a \(*\)-isomorphism \(\Phi\) of \(A\) onto the algebra \(L^\infty(X,\mu)\) of the disjoint union \((X,\mu)\) of the \((\Omega_k,\mu_k)\), as in Example 1.4, such that \(\tau(a)=\int_X\Phi(a)\,d\mu\) for \(a\in A_+\).

Consequently, by Example 1.4, \(\mathfrak m_\tau\), \(\mathfrak n_\tau\), \(L^1(A,\tau)\) and \(L^2(A,\tau)\) correspond to \(L^\infty\cap L^1\), \(L^\infty\cap L^2\), \(L^1(X,\mu)\) and \(L^2(X,\mu)\). The space \(X\) is locally compact, each \(\Omega_k\) being open and compact in it, and \(\mu\) is finite on compact sets.

**Proof.** (1) For \(a\in A\) and \(x\in\mathfrak n_\tau\), \(ax=xa\), so \(\pi_\tau(a)=\rho_\tau(a)\). By Theorem 3.1, \(\pi_\tau(A)'=\rho_\tau(A)=\pi_\tau(A)\).

(2) By Zorn's lemma choose a maximal family \((e_k)_{k\in K}\) of mutually orthogonal nonzero projections of finite trace. Its sum is \(1\): otherwise the remainder would majorize a nonzero projection of finite trace (semifiniteness). The algebra \(A_k=Ae_k\), acting on \(e_kH\), is a commutative von Neumann algebra with unit \(e_k\), and \(\tau_k=\tau|_{A_k}\) is a faithful normal finite trace on it.

Fix \(k\). By the Gelfand–Naimark theorem there is an isometric \(*\)-isomorphism \(\Gamma_k:A_k\to C(\Omega_k)\) onto the continuous functions on a compact Hausdorff space. By the Riesz–Markov theorem there is a finite positive Radon measure \(\mu_k\) on \(\Omega_k\) with \(\tau_k(a)=\int\Gamma_k(a)\,d\mu_k\). The continuous functions are dense in \(L^2(\Omega_k,\mu_k)\): given \(g\in L^2\), the truncations \(g1_{\{|g|\le n\}}\) converge to \(g\) in \(L^2\); if \(|g|\le n\), choose continuous \(f_m\to g\) in \(L^1\) and replace \(f_m\) by \(\tilde f_m=f_m\min(1,n/|f_m|)\), which is continuous with \(|\tilde f_m-g|\le|f_m-g|\) (the map \(z\mapsto z\min(1,n/|z|)\) is a 1-Lipschitz retraction onto the disc of radius \(n\), which contains the values of \(g\)); then \(\|\tilde f_m-g\|_2^2\le2n\|\tilde f_m-g\|_1\to0\).

Since \(\tau_k\) is finite, \(\mathfrak n_{\tau_k}=A_k\), and \(\|a\|_2^2=\tau_k(a^*a)=\int|\Gamma_k(a)|^2\,d\mu_k\). So \(a\mapsto\Gamma_k(a)\) extends to a unitary \(U_k\) of \(L^2(A_k,\tau_k)\) onto \(L^2(\Omega_k,\mu_k)\), and \(U_k\pi_{\tau_k}(a)U_k^*\) is multiplication by \(\Gamma_k(a)\), because both agree on the dense set of continuous functions. By part (1) applied to \((A_k,\tau_k)\), the set \(\mathcal R=\{M_{\Gamma_k(a)}:a\in A_k\}\) of these multiplication operators is maximal abelian. It lies in the commutative set of all multiplications \(M_g\), \(g\in L^\infty(\Omega_k,\mu_k)\); a commutative set containing a maximal abelian algebra equals it. So every \(M_g\) equals some \(M_{\Gamma_k(a)}\), and then \(g=\Gamma_k(a)\) almost everywhere (apply both to the vector \(1\)). Hence \(\Phi_k(a)=\Gamma_k(a)\) (as a class in \(L^\infty\)) is a \(*\)-homomorphism of \(A_k\) onto \(L^\infty(\Omega_k,\mu_k)\). It is injective: if \(\Gamma_k(a)=0\) almost everywhere, then \(\tau_k(a^*a)=0\) and \(a=0\). And \(\tau_k(a)=\int\Phi_k(a)\,d\mu_k\).

Finally \(a\mapsto(ae_k)_k\) is a \(*\)-isomorphism of \(A\) onto the bounded families \((a_k)\) with \(a_k\in A_k\): a bounded family has the strong sum \(\sum_ka_k\in A\). Put \(\Phi(a)=(\Phi_k(ae_k))_k\in L^\infty(X,\mu)\). For \(a\in A_+\), the partial sums of \(\sum_ka^{1/2}e_ka^{1/2}\) increase to \(a\), so normality gives \(\tau(a)=\sum_k\tau_k(ae_k)=\int_X\Phi(a)\,d\mu\). The statements about \(X\) are clear from the definition of the disjoint union. \(\square\)

So the commutation theorem is the noncommutative form of the statement that \(L^\infty\) is maximal abelian on \(L^2\).

## 4. Commutants of semifinite algebras

The commutation theorem gives a concrete model of the commutant for one representation, the standard one. Every other faithful normal representation is built from an amplification of it, and this transfers semifiniteness to all commutants.

**Theorem 4.1** (The commutant of a semifinite algebra). A von Neumann algebra \(M\) on \(H\) is semifinite exactly when its commutant \(M'\) is semifinite.

**Proof.** As \(M''=M\), it suffices to show that \(M'\) is semifinite when \(M\) is. Let \(\tau\) be a faithful semifinite normal trace on \(M\), and put \(M_1=\pi_\tau(M)\) on \(L^2(M,\tau)\ne0\). The map \(\theta=\pi_\tau^{-1}:M_1\to M\) is a normal \(*\)-isomorphism. By the structure of normal isomorphisms (background), there are a Hilbert space \(R\) and a projection \(e'\) in \((M_1\otimes1_R)'\) such that \(M\) is spatially isomorphic to the induced algebra \((M_1\otimes1_R)_{e'}\). Then \(M'\) is spatially isomorphic to the commutant of that induced algebra, which is the reduced algebra \(e'Pe'\) of
\[
P=(M_1\otimes1_R)'=M_1'\bar\otimes B(R)=\rho_\tau(M)\bar\otimes B(R),
\]
by Theorem 3.1.

The algebra \(\rho_\tau(M)\) carries the faithful semifinite normal trace \(\tau\circ\rho_\tau^{-1}\). Indeed, for \(z=\rho_\tau(y)\) we have \(z^*z=\rho_\tau(y^*)\rho_\tau(y)=\rho_\tau(yy^*)\) and \(zz^*=\rho_\tau(y^*y)\), so the trace identity for \(\tau\) gives the one for \(\tau\circ\rho_\tau^{-1}\); an anti-isomorphism preserves the order and suprema of bounded increasing nets, so normality, faithfulness and semifiniteness carry over. By amplification (background), \(P\) has a faithful semifinite normal trace, so it is semifinite. Finally a corner \(e'Pe'\) of a semifinite algebra is semifinite: a nonzero projection \(q\le e'\) majorizes a nonzero projection that is finite in \(P\), and finiteness of a projection below \(e'\) is the same in \(e'Pe'\) as in \(P\). \(\square\)

**Corollary 4.2** (Types of the commutant). \(M\) and \(M'\) have the same type decomposition: \(z_{\rm I}(M)=z_{\rm I}(M')\), \(z_{\rm II}(M)=z_{\rm II}(M')\) and \(z_{\rm III}(M)=z_{\rm III}(M')\). In particular \(M\) is of type I, II or III exactly when \(M'\) is.

**Proof.** \(M\) and \(M'\) have the same center \(Z\). For a central projection \(z\), the commutant of \(Mz\) on \(zH\) is \(M'z\) (background on reduced algebras).

First, \(z_{\rm I}(M)\) is the largest central projection \(z\) with \(Mz\) of type I. Indeed \(Mz_{\rm I}\) is of type I, and if \(Mz\) is of type I then \(M(zz_{\rm II})\) is a central summand both of the type I algebra \(Mz\) and of the type II algebra \(Mz_{\rm II}\); a type I summand has nonzero abelian projections unless it is \(0\), and a type II algebra has none, so \(zz_{\rm II}=0\). In the same way \(zz_{\rm III}=0\), since abelian projections are finite and a type III algebra has no nonzero finite projection. So \(z\le z_{\rm I}\). Likewise \(1-z_{\rm III}(M)\) is the largest central projection \(z\) with \(Mz\) semifinite.

By the background on type I commutants, \(Mz\) is of type I exactly when \(M'z\) is; by Theorem 4.1, \(Mz\) is semifinite exactly when \(M'z\) is. Hence \(z_{\rm I}\) and \(1-z_{\rm III}\) are the same for \(M\) and \(M'\), and so is \(z_{\rm II}=1-z_{\rm I}-z_{\rm III}\). \(\square\)

The finer types are not preserved.

**Example 4.3** (A type II\(_1\) algebra with a type II\(_\infty\) commutant). Let \(N\) be a factor of type II\(_1\). It is finite and \(\sigma\)-finite, so it has a faithful normal tracial state \(\tau\) (background on countable decomposability). On \(L^2(N,\tau)\), the commutant \(\rho_\tau(N)\) of \(\pi_\tau(N)\) is anti-isomorphic to \(N\), hence a factor of type II\(_1\). Now let \(M=\pi_\tau(N)\otimes1\) act on \(L^2(N,\tau)\otimes\ell^2(\mathbb N)\). It is isomorphic to \(N\). Its commutant is \(\rho_\tau(N)\bar\otimes B(\ell^2(\mathbb N))\), a factor (its commutant \(M\) is a factor), semifinite by amplification, of type II by Corollary 4.2, and infinite: \(1\otimes s\), with \(s\) the unilateral shift, is an isometry that is not unitary. So \(M\) is of type II\(_1\) and \(M'\) is of type II\(_\infty\). In the same way, for \(\dim H=n\ge2\) the factor \(B(H)\) of type I\(_n\) has the commutant \(\mathbb C1\) of type I\(_1\).

**Theorem 4.4** (Representations with finite commutant). \(M\) is semifinite exactly when it has a faithful normal representation \(\pi\) with \(\pi(M)'\) finite.

**Proof.** If \(\pi(M)'\) is finite, it is semifinite, so \(\pi(M)\) is semifinite by Theorem 4.1, and so is \(M\cong\pi(M)\).

Conversely, let \(M\) be semifinite, with a faithful semifinite normal trace \(\tau\), and let \(f\) be a finite projection with \(c(f)=1\) (background). Put \(N=\pi_\tau(M)\) and \(e'=\rho_\tau(f)\), a projection in \(N'=\rho_\tau(M)\). Define \(\pi(x)=\pi_\tau(x)e'\), restricted to \(e'L^2(M,\tau)\). This is the induction of \(N\) by \(e'\), composed with \(\pi_\tau\); it is a normal representation. The central projections of \(\rho_\tau(M)\) are the \(\rho_\tau(z)\), \(z\in Z\), and \(\rho_\tau(z)\ge\rho_\tau(f)\) exactly when \(z\ge f\); so the central support of \(e'\) in \(N'\) is \(\rho_\tau(c(f))=1\). The central support of \(e'\) is the projection onto the closed span of \(N'e'L^2(M,\tau)\), and since it is \(1\), the induction is injective (background on induced algebras). So \(\pi\) is faithful. Its commutant is the reduced algebra \(e'N'e'=\rho_\tau(fMf)\), restricted to \(e'L^2(M,\tau)\), which is anti-isomorphic to \(fMf\) through \(y\mapsto\rho_\tau(y)\). The algebra \(fMf\) is finite, and an anti-isomorphism \(\alpha\) of a finite algebra onto another algebra preserves finiteness. Indeed, let \(v^*v=1\) in the image and put \(w=\alpha^{-1}(v)^*\). As \(\alpha^{-1}\) reverses products and preserves adjoints, \(w^*w=\alpha^{-1}(v)\alpha^{-1}(v^*)=\alpha^{-1}(v^*v)=1\). By finiteness \(ww^*=1\), and then \(vv^*=\alpha(\alpha^{-1}(v)^*\alpha^{-1}(v))=\alpha(ww^*)=1\). So \(\pi(M)'\) is finite. \(\square\)

## 5. The involution and finiteness

The involution \(x\mapsto x^*\) is continuous for the \(\sigma\)-weak topology but not, in general, for the \(\sigma\)-strong topology. This section shows that its continuity on bounded sets characterizes finiteness. The trace enters through the next lemma. A reference for this section is [Blackadar, III.2.5].

**Lemma 5.1.** Let \(\tau\) be a faithful semifinite normal trace on \(M\) and \(a\in\mathfrak n_\tau\). Then \(x\mapsto ax^*\) is \(\sigma\)-strongly continuous on bounded subsets of \(M\).

**Proof.** Let \((x_i)\) be a bounded net converging \(\sigma\)-strongly to \(x\); replacing \(x_i\) by \(x_i-x\), we may assume \(x=0\). Put \(C=\sup_i\|x_i\|\). The representation \(\pi_\tau\) is normal, so \(\omega(x_i^*x_i)\to0\) for the normal positive functional \(\omega(y)=\langle\pi_\tau(y)a^*,a^*\rangle_2\); that is, \(\|x_ia^*\|_2\to0\). By Lemma 2.2(1), \(\|ax_i^*\|_2=\|(x_ia^*)^*\|_2=\|x_ia^*\|_2\to0\). For \(y\in\mathfrak n_\tau\), \(\|\pi_\tau(ax_i^*)y\|_2=\|(ax_i^*)y\|_2\le\|ax_i^*\|_2\,\|y\|\to0\), again by Lemma 2.2(1). So the bounded net \(\pi_\tau(ax_i^*)\), of norm at most \(\|a\|C\), converges strongly to \(0\) on the dense set \(\mathfrak n_\tau\), hence on \(L^2(M,\tau)\). As \(\pi_\tau^{-1}\) is a homeomorphism for the \(\sigma\)-strong topologies (background), and the strong and \(\sigma\)-strong topologies agree on bounded sets, \(ax_i^*\to0\) \(\sigma\)-strongly. \(\square\)

**Lemma 5.2.** If a projection \(e\in M\) is infinite, the involution of \(eMe\), restricted to the unit ball, is not \(\sigma\)-strongly continuous.

**Proof.** Choose \(v\in M\) with \(v^*v=e\) and \(vv^*=f\), where \(f\le e\) and \(f\ne e\), and put \(g=e-f\ne0\). Then \(v=ev=ve\), \(v^*g=v^*-v^*vv^*=0\), and by induction \(v^{*n}v^n=e\) for \(n\ge0\), with \(v^0=e\). Put \(e_n=v^ngv^{*n}\). These are projections below \(e\), each equivalent to \(g\) through \(v^ng\), and they are mutually orthogonal: for \(m<n\), \(e_me_n=v^mg(v^{*m}v^m)v^{n-m}gv^{*n}=v^mg\,v^{n-m}gv^{*n}=0\), because \(gv=(v^*g)^*=0\).

For \(k\le n\) we have \(v^{*k}v^ng=v^{n-k}g\), so \(v^{*k}\) maps \(e_nH\) isometrically onto \(e_{n-k}H\); for \(k>n\), \(v^{*k}v^ng=v^{*(k-n)}g=0\), so \(v^{*k}e_n=0\). Let \(p=\sum_ne_n\) and \(x_k=v^{*k}p\in eMe\), a contraction. For \(\xi\in H\) the vectors \(v^{*k}e_n\xi\), \(n\ge k\), are orthogonal, so
\[
\|x_k\xi\|^2=\sum_{n\ge k}\|e_n\xi\|^2\longrightarrow0\qquad(k\to\infty).
\]
So \(x_k\to0\) strongly, and \(\sigma\)-strongly because the sequence is bounded. But \(x_k^*=pv^k\), and for a unit vector \(\xi\in gH\) the vector \(v^k\xi=v^kgv^{*k}(v^k\xi)\) lies in \(e_kH\subseteq pH\), so \(\|x_k^*\xi\|=\|v^k\xi\|=1\). \(\square\)

**Theorem 5.3** (Finiteness and the involution). For a projection \(p\in M\) the following are equivalent:

- (i) \(p\) is finite;
- (ii) the involution is \(\sigma\)-strongly continuous on bounded subsets of \(pMp\);
- (iii) the map \(x\mapsto px^*\) is \(\sigma\)-strongly continuous on bounded subsets of \(M\).

In particular \(M\) is finite exactly when the involution is \(\sigma\)-strongly continuous on its unit ball, that is, exactly when the \(\sigma\)-strong and the \(\sigma\)-strong\(^*\) topologies agree on bounded subsets of \(M\).

*Reference:* [Blackadar, III.2.5.23].

**Proof.** (iii)\(\Rightarrow\)(ii): for \(x\in pMp\), \(px^*=x^*\). (ii)\(\Rightarrow\)(i) is Lemma 5.2.

(i)\(\Rightarrow\)(iii). The corner \(pMp\) is finite. By the background on countable decomposability, applied to \(pMp\), there are orthogonal central projections of \(pMp\) with sum \(p\), each cutting out a \(\sigma\)-finite algebra with a faithful normal finite trace. The central projections of \(pMp\) are the \(pz\) with \(z\in Z\); for orthogonal \(pz\) and \(pz'\) we have \(c(p)zz'=0\). So we get orthogonal central projections \(z_k\le c(p)\) of \(M\) with \(\sum_kz_k=c(p)\), and faithful normal finite traces \(\tau_k\) on \(pz_kMpz_k\). Extend \(\tau_k\) from the corner \(pz_k\) to a normal trace \(\sigma_k\) on \(M\) (background); it vanishes on \(M(1-z_k)\), since \(c(pz_k)=z_k\), and it is faithful and semifinite on \(Mz_k\). As \(\sigma_k(pz_k)<\infty\), \(pz_k\in\mathfrak n_{\sigma_k}\).

Let \((x_i)\) be a bounded net, \(\|x_i\|\le C\), converging \(\sigma\)-strongly to \(0\). Then \(x_iz_k\to0\) \(\sigma\)-strongly in \(Mz_k\), and Lemma 5.1 in \(Mz_k\) gives \(pz_kx_i^*\to0\) \(\sigma\)-strongly for each \(k\). Let \(\xi\in H\). Since \(p=\sum_kpz_k\) and the \(z_k\) are central and orthogonal,
\[
\|px_i^*\xi\|^2=\sum_k\|pz_kx_i^*(z_k\xi)\|^2 ,
\]
each term tends to \(0\), and the sum over \(k\) outside a finite set \(F\) is at most \(C^2\sum_{k\notin F}\|z_k\xi\|^2\), which is small for large \(F\) uniformly in \(i\). So \(px_i^*\xi\to0\), and \(px_i^*\to0\) strongly, hence \(\sigma\)-strongly. For a net converging to \(x\ne0\), apply this to \(x_i-x\).

For the last sentence take \(p=1\); continuity on the unit ball is continuity on all bounded sets, by scaling. A bounded net converges \(\sigma\)-strongly\(^*\) exactly when it and its adjoints converge \(\sigma\)-strongly. \(\square\)

The restriction to bounded sets cannot be dropped, even for finite algebras.

**Example 5.4** (A finite algebra with a discontinuous involution). Let \(M=\bigoplus_{n\ge1}M_n(\mathbb C)\), the bounded sequences \(x=(x_n)\), acting on \(\bigoplus_n\mathbb C^n\). It is finite: \(\sum_n2^{-n}\operatorname{tr}_n(x_n)\), with \(\operatorname{tr}_n\) the normalized trace, is a faithful normal finite trace. Suppose the involution were \(\sigma\)-strongly continuous on all of \(M\). The \(\sigma\)-strong topology is locally convex, given by the directed family of seminorms \(x\mapsto\psi(x^*x)^{1/2}\), \(\psi\in M_*^+\). So for the normal state \(\omega=c\sum_nn^{-2}\omega_{\xi_n}\), with unit vectors \(\xi_n\in\mathbb C^n\) and \(c^{-1}=\sum_nn^{-2}\), there would be \(\psi\in M_*^+\) with
\[
\omega(xx^*)\le\psi(x^*x)\qquad(x\in M).
\]
The restriction of \(\psi\) to the \(n\)-th summand is \(\operatorname{Tr}(k_n\,\cdot\,)\) with \(k_n\ge0\) and \(\sum_n\operatorname{Tr}(k_n)=\psi(1)<\infty\). Let \(\eta_n\) be a unit eigenvector of \(k_n\) for its smallest eigenvalue \(\lambda_n\le\operatorname{Tr}(k_n)/n\), and let \(x\) have the single nonzero entry \(x_n=\langle\,\cdot\,,\eta_n\rangle\xi_n\). Then \(\omega(xx^*)=cn^{-2}\) and \(\psi(x^*x)=\lambda_n\le\operatorname{Tr}(k_n)/n\). So \(\operatorname{Tr}(k_n)\ge c/n\) for every \(n\), and \(\sum_n\operatorname{Tr}(k_n)=\infty\), a contradiction.

*Remark.* Finiteness of \(M\) does not make the involution \(\sigma\)-strongly continuous on all of \(M\): this fails for the finite algebra above, so Theorem 5.3 asks for continuity on bounded sets only. Compare [Blackadar, III.2.5.23].

**Corollary 5.5** (The Mackey topology). \(M\) is finite exactly when, on bounded subsets of \(M\), the \(\sigma\)-strong topology coincides with the Mackey topology \(\tau(M,M_*)\).

**Proof.** On bounded sets the Mackey topology is the \(\sigma\)-strong\(^*\) topology (background). Apply the last sentence of Theorem 5.3. \(\square\)

Finiteness can also be read off the closure of the inner automorphisms. By compactness of the balls of \(M\) in the \(\sigma\)-weak topology and Tychonoff's theorem, every net of maps \(x\mapsto u_ixu_i^*\), \(u_i\) unitary, has a subnet that converges pointwise \(\sigma\)-weakly; the limit is a positive unital map of \(M\) into itself.

**Theorem 5.6** (Limits of inner automorphisms). \(M\) is finite exactly when every map \(T:M\to M\) that is a pointwise \(\sigma\)-weak limit of a net of inner automorphisms \(x\mapsto u_ixu_i^*\) is normal.

**Proof.** Let \(M\) be finite, and \(T(x)=\lim_iu_ixu_i^*\) \(\sigma\)-weakly for every \(x\). Fix \(\varphi\in M_*^+\) and let \(Q=\{\varphi(u\,\cdot\,u^*):u\text{ unitary}\}\subseteq M_*^+\), a bounded set.

*Step 1.* If \((e_n)\) are mutually orthogonal projections, then \(\sup_{\psi\in Q}\psi(e_n)\to0\). Otherwise there are \(\delta>0\), indices \(n_1<n_2<\cdots\) and unitaries \(v_k\) with \(\varphi(v_ke_{n_k}v_k^*)\ge\delta\). The projections \(v_ke_{n_k}v_k^*\) are equivalent to the orthogonal projections \(e_{n_k}\), so they tend to \(0\) \(\sigma\)-strongly because \(M\) is finite (background), and \(\varphi\) of them tends to \(0\): a contradiction.

*Step 2.* If projections \(p_n\) decrease to \(0\), then \(s_n=\sup_{\psi\in Q}\psi(p_n)\to0\). The \(s_n\) decrease; suppose they stay above \(\delta>0\). Choose \(\psi_1\in Q\) and \(n_1\) with \(\psi_1(p_{n_1})>\delta/2\). Since \(\psi_1\) is normal, there is \(n_2>n_1\) with \(\psi_1(p_{n_2})<\delta/4\). Choose \(\psi_2\in Q\) with \(\psi_2(p_{n_2})>\delta/2\), then \(n_3>n_2\) with \(\psi_2(p_{n_3})<\delta/4\), and so on. The projections \(e_k=p_{n_k}-p_{n_{k+1}}\) are orthogonal and \(\psi_k(e_k)>\delta/4\), against Step 1.

\(Q\) is bounded by \(\varphi(1)\), so by the weak compactness criterion (background on functionals), \(Q\) is relatively \(\sigma(M_*,M)\)-compact. The net \(\psi_i=\varphi(u_i\,\cdot\,u_i^*)\) in \(Q\) has a subnet converging to some \(\psi\in M_*\) for \(\sigma(M_*,M)\). For \(x\in M\), \(\varphi(T(x))=\lim_i\psi_i(x)=\psi(x)\), as the limit along a subnet is the same. So \(\varphi\circ T\in M_*\) for every \(\varphi\in M_*^+\), hence for every \(\varphi\in M_*\), and \(T\) is normal (background).

Conversely, let \(M\) be infinite. There is a nonzero central projection \(z\) with \(Mz\) properly infinite (background), so \(z=\sum_{n\ge1}e_n\) with orthogonal projections \(e_n\sim z\) (halving). Relabel them by the integers as \((f_k)_{k\in\mathbb Z}\), and choose partial isometries \(w_k\) with \(w_k^*w_k=f_k\) and \(w_kw_k^*=f_{k+1}\). The strong sum \(W=\sum_kw_k+(1-z)\) is a unitary with \(Wf_kW^*=f_{k+1}\) and \(Wz=zW\). By the remark before the theorem, a subnet of the sequence of maps \(x\mapsto W^nxW^{-n}\), \(n\in\mathbb N\), converges pointwise \(\sigma\)-weakly to a map \(T\). The indices of a subnet of a sequence tend to infinity, and \(W^nf_kW^{-n}=f_{k+n}\to0\) \(\sigma\)-weakly, because the \(f_m\) are orthogonal. So \(T(f_k)=0\) for every \(k\), while \(T(z)=z\ne0\) and \(\sum_kf_k=z\). A normal positive map preserves such sums, so \(T\) is not normal. \(\square\)

Finiteness can also be read off the absolute values of normal functionals. For \(K\subseteq M_*\) write \(|K|=\{|\varphi|:\varphi\in K\}\).

**Theorem 5.7** (Absolute values of weakly compact sets). \(M\) is finite exactly when \(|K|\) is relatively \(\sigma(M_*,M)\)-compact for every relatively \(\sigma(M_*,M)\)-compact set \(K\subseteq M_*\).

**Proof.** Let \(M\) be finite and \(K\) relatively \(\sigma(M_*,M)\)-compact. The set \(|K|\) is bounded, since \(\||\varphi|\|=\|\varphi\|\). Suppose it is not relatively compact. By the weak compactness criterion there are projections \(p_n\) decreasing to \(0\) such that \(s_n=\sup_{\varphi\in K}|\varphi|(p_n)\) does not tend to \(0\). The \(s_n\) decrease, so \(s_n>\varepsilon\) for all \(n\) and some \(\varepsilon>0\). Choose \(\varphi_n\in K\) with \(|\varphi_n|(p_n)>\varepsilon\), let \(v_n\) be the partial isometry of the polar decomposition of \(\varphi_n\), and put \(a_n=p_nv_n^*\). Then \(\|a_n\|\le1\) and \(\varphi_n(a_n)=|\varphi_n|(p_n)>\varepsilon\). For \(\omega\in M_*^+\),
\[
\omega\bigl((a_n^*)^*a_n^*\bigr)=\omega(p_nv_n^*v_np_n)\le\omega(p_n)\longrightarrow0 ,
\]
so \(a_n^*\to0\) \(\sigma\)-strongly. By Theorem 5.3, the involution is \(\sigma\)-strongly continuous on bounded subsets of \(M\), so \(a_n\to0\) \(\sigma\)-strongly as well. Thus \(a_n\to0\) \(\sigma\)-strongly\(^*\), and \(\sup_{\varphi\in K}|\varphi(a_n)|\to0\) (background on functionals). This contradicts \(|\varphi_n(a_n)|>\varepsilon\).

Conversely, let \(M\) be infinite. By the construction in the proof of Lemma 5.2, applied with \(e=1\), there are mutually orthogonal nonzero projections \(e_1,e_2,\dots\) that are mutually equivalent. Choose partial isometries \(w_n\) with \(w_n^*w_n=e_1\) and \(w_nw_n^*=e_n\), a unit vector \(\xi\in e_1H\), and put \(\xi_n=w_n\xi\), an orthonormal sequence with \(\xi_n\in e_nH\). Let \(\varphi_n(x)=\langle x\xi,\xi_n\rangle\) for \(x\in M\).

The set \(K=\{\varphi_n\}\) is relatively compact. By Bessel's inequality, \(\sum_n|\varphi_n(x)|^2\le\|x\xi\|^2\), so \(\varphi_n(x)\to0\) for every \(x\in M\). Thus \(\varphi_n\to0\) for \(\sigma(M_*,M)\), and \(K\cup\{0\}\) is compact.

The set \(|K|\) is not. Let \(\omega_n(x)=\langle x\xi_n,\xi_n\rangle\) and let \(s_n\) be its support in \(M\); then \(s_n\le e_n\), since \(\omega_n(1-e_n)=0\). As \(w_n^*\xi_n=e_1\xi=\xi\), we have \(\varphi_n(x)=\langle xw_n^*\xi_n,\xi_n\rangle=\omega_n(xw_n^*)\). By the Cauchy–Schwarz inequality \(\omega_n(y(1-s_n))=0\) for every \(y\in M\), so \(\varphi_n(x)=\omega_n(xv_n)\) with \(v_n=w_n^*s_n\). Here \(v_n^*v_n=s_ne_ns_n=s_n\). By the uniqueness of the polar decomposition, \(|\varphi_n|=\omega_n\). The projections \(r_m=\sum_{j\ge m}e_j\) decrease to \(0\), while \(\omega_n(r_m)=1\) for \(n\ge m\). By the weak compactness criterion, \(|K|\) is not relatively compact. \(\square\)

*Reference:* the lesson on polar decomposition of functionals, Example 10.7 gives the same example in \(B(H)\).

## 6. Tensor products: finiteness and type

In this section \(M_1\) and \(M_2\) are von Neumann algebras on nonzero Hilbert spaces \(H_1\) and \(H_2\), and \(M=M_1\bar\otimes M_2\). The hypothesis \(H_k\ne0\) matters: if \(H_2=0\), then \(M=\{0\}\) is finite and of every type, whatever \(M_1\) is. A reference for this section is [Blackadar, III.2.5.24–III.2.5.29].

**Proposition 6.1** (Finite tensor products).

1. If \(\tau_1\) and \(\tau_2\) are faithful normal finite traces on \(M_1\) and \(M_2\), the product functional \(\tau_1\otimes\tau_2\) is a faithful normal finite trace on \(M\), and it is the only normal functional with \((\tau_1\otimes\tau_2)(x\otimes y)=\tau_1(x)\tau_2(y)\).
2. \(M\) is finite exactly when \(M_1\) and \(M_2\) are finite.

**Proof.** (1) The product functional \(\omega=\tau_1\otimes\tau_2\) is normal, positive and faithful, and unique with the given values (background). Let \(\mathcal A\) be the algebraic tensor product, spanned by the \(x\otimes y\). For elementary tensors, \(\omega((x\otimes y)(x'\otimes y'))=\tau_1(xx')\tau_2(yy')=\tau_1(x'x)\tau_2(y'y)=\omega((x'\otimes y')(x\otimes y))\), so \(\omega(ab)=\omega(ba)\) for \(a,b\in\mathcal A\). Fix \(b\in\mathcal A\). The normal functionals \(a\mapsto\omega(ab)\) and \(a\mapsto\omega(ba)\) agree on \(\mathcal A\), hence on \(M\). Then fix \(a\in M\): the normal functionals \(b\mapsto\omega(ab)\) and \(b\mapsto\omega(ba)\) agree on \(\mathcal A\), hence on \(M\). So \(\omega(z^*z)=\omega(zz^*)\) for all \(z\in M\), and \(\omega\) restricts to a faithful normal finite trace.

(2) If \(M\) is finite and \(v\in M_1\) satisfies \(v^*v=1\), then \(v\otimes1\) is an isometry in \(M\), hence unitary, and \(vv^*=1\) because \(x\mapsto x\otimes1\) is injective. So \(M_1\) is finite, and \(M_2\) likewise.

Conversely let \(M_1\) and \(M_2\) be finite. By the background on countable decomposability, \(1=\sum_kz_k\) in \(M_1\) and \(1=\sum_lw_l\) in \(M_2\), with orthogonal central projections, where each \(M_1z_k\) and \(M_2w_l\) has a faithful normal finite trace. The projections \(z_k\otimes w_l\) are central in \(M\), orthogonal, and add up to \(1\). The corner \(M(z_k\otimes w_l)\) is \(M_1z_k\bar\otimes M_2w_l\), which by (1) has a faithful finite trace \(\sigma\), and is therefore finite: \(u^*u=1\) gives \(\sigma(1-uu^*)=\sigma(u^*u)-\sigma(uu^*)=0\). Finally, if \(u\in M\) and \(u^*u=1\), then for each of these central projections \(q\), \(uq\) is an isometry in the finite algebra \(Mq\), so \(uu^*q=q\); summing over \(q\), \(uu^*=1\). \(\square\)

The next theorem is the tool for type III. It concerns maps that behave like conditional expectations.

**Theorem 6.2** (Bimodule maps onto a type III algebra). Let \(N\subseteq M\) be a von Neumann subalgebra (a von Neumann algebra on \(H\) contained in \(M\)) and \(\varepsilon:M\to N\) a normal positive linear map with
\[
\varepsilon(axb)=a\,\varepsilon(x)\,b\qquad(a,b\in N,\ x\in M).
\]
If \(N\) is of type III, then \(\varepsilon(p)=0\) for every finite projection \(p\in M\). Consequently, if \((\varepsilon_i)\) is a family of such maps such that \(\varepsilon_i(x^*x)=0\) for all \(i\) only when \(x=0\), and \(N\) is of type III, then \(M\) is of type III. By Tomiyama's theorem, normal projections of norm one of \(M\) onto \(N\) are such maps, so this applies to every family of them with that property.

**Proof.** Let \(p\) be a finite projection and suppose \(\varepsilon(p)\ne0\). Put \(\lambda=\|\varepsilon(p)\|/2\) and let \(q\in N\) be the spectral projection of \(\varepsilon(p)\) for \([\lambda,\infty)\). Then \(q\ne0\) and \(\lambda q\le q\varepsilon(p)q\). For \(x\in qNq\), \(x=xq\), so
\[
xx^*=xqx^*\le\lambda^{-1}x\varepsilon(p)x^*=\lambda^{-1}\varepsilon(xpx^*)=\lambda^{-1}\varepsilon\bigl((px^*)^*(px^*)\bigr).
\]
Let \((x_j)\) be a bounded net in \(qNq\) converging \(\sigma\)-strongly to \(0\). By Theorem 5.3 ((i)\(\Rightarrow\)(iii)), \(px_j^*\to0\) \(\sigma\)-strongly, that is, \(\omega\bigl((px_j^*)^*(px_j^*)\bigr)\to0\) for every \(\omega\in M_*^+\); as \(M_*^+\) spans \(M_*\), \((px_j^*)^*(px_j^*)=x_jpx_j^*\to0\) \(\sigma\)-weakly. The map \(\varepsilon\) is \(\sigma\)-weakly continuous (background), so \(\varepsilon(x_jpx_j^*)\to0\) \(\sigma\)-weakly, and the inequality above gives \(\omega(x_jx_j^*)\to0\) for every \(\omega\in M_*^+\). So \(x_j^*\to0\) \(\sigma\)-strongly. Applied to \(x_j-x\), this shows that the involution is \(\sigma\)-strongly continuous on bounded subsets of \(qNq\). By Theorem 5.3 in \(N\), \(q\) is finite, which is impossible in a type III algebra since \(q\ne0\).

For the family: if \(M\) were not of type III, it would contain a nonzero finite projection \(p\), and \(\varepsilon_i(p^*p)=\varepsilon_i(p)=0\) for all \(i\) would force \(p=0\), which is impossible. A normal projection of norm one onto \(N\) is positive and \(N\)-bimodular by Tomiyama's theorem. \(\square\)

**Theorem 6.3** (Types of tensor products).

- (a) If \(M_1\) or \(M_2\) is of type III, so is \(M\).
- (b) If \(M_1\) and \(M_2\) are semifinite, so is \(M\).
- (c) If \(M_1\) and \(M_2\) are of type I, so is \(M\).
- (d) If \(M_1\) is of type II and \(M_2\) is semifinite, or the other way round, then \(M\) is of type II.
- (e) Write \(z_{\rm I},z_{\rm II},z_{\rm III}\) for the type projections of \(M_1\) and \(w_{\rm I},w_{\rm II},w_{\rm III}\) for those of \(M_2\). Then
\[
z_{\rm I}(M)=z_{\rm I}\otimes w_{\rm I},\qquad z_{\rm II}(M)=z_{\rm I}\otimes w_{\rm II}+z_{\rm II}\otimes w_{\rm I}+z_{\rm II}\otimes w_{\rm II},\qquad 1-z_{\rm III}(M)=(1-z_{\rm III})\otimes(1-w_{\rm III}).
\tag{6.1}
\]

Consequently: \(M\) is of type I exactly when \(M_1\) and \(M_2\) are; \(M\) is of type III exactly when \(M_1\) or \(M_2\) is; and \(M\) is of type II exactly when neither \(M_1\) nor \(M_2\) has a nonzero type III summand and at least one of them is of type II.

**Proof.** (a) Exchanging the factors by the flip, we may assume that \(M_1\) is of type III. The algebra \(N=M_1\otimes1\) is a von Neumann subalgebra of \(M\) isomorphic to \(M_1\), so it is of type III. For a unit vector \(\eta\in H_2\) put \(\varepsilon_\eta(X)=(R_\eta^*XR_\eta)\otimes1\). By the background on slice maps, \(\varepsilon_\eta\) is a normal positive map of \(M\) into \(N\), and \(\varepsilon_\eta((a\otimes1)X(b\otimes1))=(a\otimes1)\varepsilon_\eta(X)(b\otimes1)\) for \(a,b\in M_1\). If \(\varepsilon_\eta(X^*X)=0\) for every \(\eta\), then \(\|X(\xi\otimes\eta)\|^2=\langle R_\eta^*X^*XR_\eta\xi,\xi\rangle=0\) for all \(\xi,\eta\), and \(X=0\) because product vectors span a dense subspace. Theorem 6.2 shows that \(M\) is of type III.

(b) In a semifinite algebra, a maximal family of mutually orthogonal nonzero finite projections has sum \(1\), because below every nonzero projection there is a nonzero finite one. So \(1=\sum_ie_i\) in \(M_1\) and \(1=\sum_jf_j\) in \(M_2\) with finite \(e_i,f_j\). The corner of \(M\) at \(e_i\otimes f_j\) is \(e_iM_1e_i\bar\otimes f_jM_2f_j\), which is finite by Proposition 6.1; so \(e_i\otimes f_j\) is a finite projection, and \(\sum_{i,j}e_i\otimes f_j=1\). If \(q\ne0\) is a central projection of \(M\), some \(q(e_i\otimes f_j)\) is nonzero, and it is a finite projection below \(q\). So \(M\) is semifinite.

(c) Choose abelian projections \(e\in M_1\) and \(f\in M_2\) with \(c(e)=1\) and \(c(f)=1\) (background). The corner of \(M\) at \(e\otimes f\) is \(eM_1e\bar\otimes fM_2f\), which is generated by the pairwise commuting elements \(a\otimes b\); the bicommutant of a commuting self-adjoint set is commutative, so \(e\otimes f\) is abelian. Its central support is the projection onto the closed span of \(M(e\otimes f)(H_1\otimes H_2)\), which contains every \(xe\xi\otimes yf\eta\), hence the closed span of \(c(e)H_1\otimes c(f)H_2=H_1\otimes H_2\). So \(c(e\otimes f)=1\). For a nonzero central projection \(q\), \(q(e\otimes f)\) is then nonzero and abelian, and \(M\) is of type I.

(d) By the flip we may assume that \(M_1\) is of type II and \(M_2\) is semifinite. By (b), \(M\) is semifinite, so it has no type III part. We show that \(M\) has no nonzero abelian projection; then \(z_{\rm I}(M)=0\) and \(M\) is of type II.

Suppose \(g\ne0\) is abelian in \(M\). With \(e_i,f_j\) as in (b), \(\sum_{i,j}e_i\otimes f_j=1\), so \(c(g)(e_i\otimes f_j)\ne0\) for some \(i,j\). Put \(p=e_i\otimes f_j\); then \(c(g)c(p)\ne0\), and there are nonzero \(g_1\le g\) and \(p_1\le p\) with \(g_1\sim p_1\) (background). The projection \(g_1\) is abelian, and so is \(p_1\). So the corner \(P=pMp=A\bar\otimes B\), with \(A=e_iM_1e_i\) and \(B=f_jM_2f_j\), contains the nonzero abelian projection \(p_1\).

Now \(A\) and \(B\) are finite, so \(P\) is finite by Proposition 6.1; let \(T\) be its center-valued trace. The algebra \(A\) has no nonzero abelian projection, since an abelian projection of \(A\) is abelian in \(M_1\). By halving, \(1_A=a_1+a_2\) with \(a_1\sim a_2\). Halve \(a_1=a_{11}+a_{12}\) and move the halves to \(a_2\) with a partial isometry implementing \(a_1\sim a_2\); repeating, for every \(n\) we get \(2^n\) mutually orthogonal, mutually equivalent projections \(a_k\) of \(A\) with sum \(1_A\). The projections \(a_k\otimes1\) are mutually equivalent in \(P\) and add up to \(1_P\). Hence \(T(a_1\otimes1)=2^{-n}\), and \(c(a_1\otimes1)=1_P\), since equivalent projections have equal central supports. As abelian projections are smallest, \(p_1\precsim a_1\otimes1\), so \(T(p_1)\le2^{-n}\) for every \(n\). So \(T(p_1)=0\), and \(p_1=0\) because \(T\) is faithful. A contradiction.

(e) The nine central projections \(z_a\otimes w_b\), with \(a,b\in\{{\rm I},{\rm II},{\rm III}\}\), are orthogonal with sum \(1\), and the summand \(M(z_a\otimes w_b)\) is \(M_1z_a\bar\otimes M_2w_b\). When it is nonzero, both factors are nonzero, and by (a), (c) and (d) its type is: I for \((a,b)=({\rm I},{\rm I})\); II for \(({\rm I},{\rm II})\), \(({\rm II},{\rm I})\) and \(({\rm II},{\rm II})\), since type I algebras are semifinite; III whenever \(a\) or \(b\) is III.

If \(1=\sum_kq_k\) with orthogonal central \(q_k\) and every \(Mq_k\) of a single type, then \(z_t(M)\) is the sum of the \(q_k\) of type \(t\). Indeed, \(Mq_k\) of type I forces \(q_k\le z_{\rm I}(M)\), as in the proof of Corollary 4.2. If \(Mq_k\) is of type II, then \(M(q_kz_{\rm I}(M))\) has no nonzero abelian projection and is of type I, so it is \(0\); and \(M(q_kz_{\rm III}(M))\) is semifinite and of type III, so it is \(0\). If \(Mq_k\) is of type III, the same reasoning gives \(q_k\le z_{\rm III}(M)\). So each sum of the \(q_k\) of one type lies below the matching \(z_t(M)\), and since both families add up to \(1\), they are equal. This gives (6.1): for instance \(1-z_{\rm III}(M)\) is the sum over \(a,b\in\{{\rm I},{\rm II}\}\), which is \((z_{\rm I}+z_{\rm II})\otimes(w_{\rm I}+w_{\rm II})\).

For the consequences: for projections \(p\) on \(H_1\) and \(q\) on \(H_2\), \(\|(p\otimes q)(\xi\otimes\eta)\|=\|p\xi\|\,\|q\eta\|\); so \(p\otimes q=1\) only if \(p=1\) and \(q=1\), and \(p\otimes q=0\) only if \(p=0\) or \(q=0\). Hence \(z_{\rm I}(M)=1\) exactly when \(z_{\rm I}=1=w_{\rm I}\), and \(z_{\rm III}(M)=1\) exactly when \(z_{\rm III}=1\) or \(w_{\rm III}=1\). Finally \(M\) is of type II exactly when \(z_{\rm I}(M)=0\) and \(z_{\rm III}(M)=0\), that is, when \(z_{\rm III}=w_{\rm III}=0\) and \(z_{\rm I}\otimes w_{\rm I}=0\). The last condition means \(z_{\rm I}=0\) or \(w_{\rm I}=0\), and given the first, \(z_{\rm I}=0\) means that \(M_1\) is of type II, and \(w_{\rm I}=0\) that \(M_2\) is. \(\square\)

**Example 6.4.** Let \(N\) be a factor of type II\(_1\) and \(K\) an infinite-dimensional Hilbert space. By Theorem 6.3, \(N\bar\otimes B(K)\) is of type II, and it is not finite, since \(1\otimes s\), with \(s\) a non-unitary isometry of \(K\), is an isometry that is not unitary. By Proposition 6.1 and Theorem 6.3, \(N\bar\otimes N\) is finite and of type II, that is, of type II\(_1\). If \(R\) is of type III, then \(R\bar\otimes B(K)\) and \(R\bar\otimes N\) are of type III, by part (a).

## 7. Comparing two traces

We first describe all normal traces through functionals. This is used in Section 8.

**Proposition 7.1** (Normal traces as sums of functionals). For a trace \(\tau\) on \(M\) the following are equivalent:

- (a) \(\tau\) is normal;
- (b) there are normal positive functionals \(\varphi_i\) with \(\tau(x)=\sum_i\varphi_i(x)\) for \(x\in M_+\);
- (c) \(\tau\) is lower semicontinuous on \(M_+\) for the \(\sigma\)-weak topology.

If \(\tau\) is normal and semifinite, one can take \(\varphi_i(x)=\tau(e_ixe_i)\) for mutually orthogonal projections \(e_i\) of finite trace with \(\sum_ie_i=1\).

**Proof.** (a)\(\Rightarrow\)(b). Let \(z\) be the central projection of the semifinite part of \(\tau\) (background). As in (b) of Theorem 6.3, there are mutually orthogonal projections \(e_i\le z\) of finite trace with \(\sum_ie_i=z\). For \(x\in M_+\), normality and the trace identity for \(e_ix^{1/2}\) give
\[
\tau(xz)=\tau(x^{1/2}zx^{1/2})=\sum_i\tau(x^{1/2}e_ix^{1/2})=\sum_i\tau(e_ixe_i).
\]
Since \(e_i\in\mathfrak m_\tau\), \(\varphi_i(x)=\tau(e_ixe_i)=\tau(xe_i)=\omega_{e_i}(x)\) defines a normal positive functional (background on the trace norm). If \(1-z\ne0\), use Zorn's lemma to choose normal states \(\omega_j\) whose supports \(s_j\) are mutually orthogonal and lie below \(1-z\), with the family maximal for these properties. Their supports add up to \(1-z\): otherwise a vector state at a unit vector in the range of the remainder would have its support there, against maximality. For \(x\in M_+\), \(\omega_j(x)=0\) for all \(j\) exactly when \(s_jxs_j=0\) for all \(j\), that is, when \(x^{1/2}(1-z)=0\). So the family consisting of countably many copies of each \(\omega_j\) has sum \(\infty\) at \(x\) when \(x(1-z)\ne0\), and \(0\) otherwise; that is exactly \(\tau(x(1-z))\). Together, the two families consist of normal positive functionals whose sum at \(x\) is \(\tau(xz)+\tau(x(1-z))=\tau(x)\).

(b)\(\Rightarrow\)(c): each finite partial sum is \(\sigma\)-weakly continuous, and a supremum of continuous functions is lower semicontinuous.

(c)\(\Rightarrow\)(a): if \(x_i\uparrow x\), then \(x_i\to x\) \(\sigma\)-weakly, so \(\tau(x)\le\liminf_i\tau(x_i)=\sup_i\tau(x_i)\le\tau(x)\). \(\square\)

A finite trace that is not normal, such as a limit along a free ultrafilter on \(\ell^\infty(\mathbb N)\), is therefore not \(\sigma\)-weakly lower semicontinuous.

The main result of this section compares two traces. It is a Radon–Nikodym theorem, and its density is central.

**Theorem 7.2** (Comparing two traces). Let \(\tau\) be a faithful semifinite normal trace and \(\tau'\) a semifinite normal trace on \(M\). Then \(\tau_0=\tau+\tau'\) is a faithful semifinite normal trace, and there is a unique central element \(a\) with \(0\le a\le1\) such that
\[
\tau(x)=\tau_0(ax),\qquad \tau'(x)=\tau_0((1-a)x)\qquad(x\in M_+).
\tag{7.1}
\]
Moreover \(s(a)=1\) and \(s(1-a)=s(\tau')\).

**Proof.** \(\tau_0\) is normal and semifinite (background on sums), and faithful because \(\tau\) is. Note that \(\mathfrak n_{\tau_0}=\mathfrak n_\tau\cap\mathfrak n_{\tau'}\). For \(x,y\in\mathfrak n_{\tau_0}\), the Cauchy–Schwarz inequality for the positive form \((x,y)\mapsto\tau(y^*x)\) gives
\[
|\tau(y^*x)|^2\le\tau(x^*x)\tau(y^*y)\le\tau_0(x^*x)\tau_0(y^*y)=\|x\|_{2,\tau_0}^2\|y\|_{2,\tau_0}^2 .
\]
So there is a unique operator \(A\) on \(L^2(M,\tau_0)\) with \(\langle Ax,y\rangle_2=\tau(y^*x)\) for \(x,y\in\mathfrak n_{\tau_0}\), and \(0\le A\le1\). Let \(u\in M\) be unitary. For \(x,y\in\mathfrak n_{\tau_0}\),
\[
\langle A\pi_{\tau_0}(u)x,y\rangle_2=\tau(y^*ux)=\tau((u^*y)^*x)=\langle Ax,u^*y\rangle_2=\langle\pi_{\tau_0}(u)Ax,y\rangle_2 ,
\]
and, using (0.1) with \(y^*x\in\mathfrak m_\tau\),
\[
\langle A\rho_{\tau_0}(u)x,y\rangle_2=\tau(y^*xu)=\tau(uy^*x)=\tau((yu^*)^*x)=\langle Ax,\rho_{\tau_0}(u^*)y\rangle_2=\langle\rho_{\tau_0}(u)Ax,y\rangle_2 .
\]
Every element of \(M\) is a combination of unitaries, so \(A\) commutes with \(\pi_{\tau_0}(M)\) and with \(\rho_{\tau_0}(M)\). By Theorem 3.1, \(A\in\rho_{\tau_0}(M)\cap\pi_{\tau_0}(M)\), the center of \(\pi_{\tau_0}(M)\), which is \(\pi_{\tau_0}(Z)\). So \(A=\pi_{\tau_0}(a)\) for a central \(a\), with \(0\le a\le1\) because \(\pi_{\tau_0}\) is an order isomorphism onto its image. Then \(\tau(y^*x)=\tau_0(y^*ax)\) for \(x,y\in\mathfrak n_{\tau_0}\), and for \(x\in F_{\tau_0}\), taking \(x^{1/2}\) for both vectors, \(\tau(x)=\tau_0(ax)\). For general \(x\in M_+\), let \(e_i\in F_{\tau_0}\) be projections increasing to \(1\); then \(x_i=x^{1/2}e_ix^{1/2}\in F_{\tau_0}\) increase to \(x\), and normality of \(\tau\) and of \(\tau_0(a\,\cdot\,)\) gives \(\tau(x)=\tau_0(ax)\). For \(x\in F_{\tau_0}\), \(\tau'(x)=\tau_0(x)-\tau(x)=\tau_0((1-a)x)\), and the same limit argument extends this to \(M_+\).

If \(q=1-s(a)\), then \(\tau(q)=\tau_0(aq)=0\), so \(q=0\). A central projection \(q\) has \(\tau'(q)=\tau_0((1-a)q)=0\) exactly when \((1-a)q=0\), because \(\tau_0\) is faithful. The largest such \(q\) is \(1-s(1-a)\), and it is also \(1-s(\tau')\) (background on supports). So \(s(1-a)=s(\tau')\).

Uniqueness: if \(a'\) also satisfies (7.1), put \(b=a-a'\) and \(q=1_{(0,\infty)}(b)\). For projections \(e\in F_{\tau_0}\), \(\tau_0(bq\,e)=\tau(qe)-\tau(qe)=0\), where \(bq\,e=(bq)^{1/2}e(bq)^{1/2}\ge0\). By faithfulness \(e(bq)^{1/2}=0\) for all such \(e\), whose supremum is \(1\); so \(bq=0\). In the same way \(b(1-q)=0\), and \(a=a'\). \(\square\)

**Example 7.3** (Semifiniteness of \(\tau'\) is needed). On \(M=\mathbb C\) let \(\tau(t)=t\) and \(\tau'(t)=\infty\) for \(t>0\), \(\tau'(0)=0\). Then \(\tau'\) is a faithful normal trace that is not semifinite, and \(\tau+\tau'=\tau'\). No \(a\in[0,1]\) satisfies \(\tau(1)=\tau'(a)\): the right side is \(0\) or \(\infty\).

**Corollary 7.4** (Factors). On a semifinite factor, any two semifinite normal traces are proportional: if \(\tau\ne0\), then \(\tau'=c\tau\) for some \(c\in[0,\infty)\).

**Proof.** The support of a nonzero normal trace is a nonzero central projection, hence \(1\), so \(\tau\) is faithful. By Theorem 7.2, \(a=\lambda1\) with \(0<\lambda\le1\), and \(\tau'=(1-\lambda)\tau_0=\lambda^{-1}(1-\lambda)\tau\). \(\square\)

For \(B(H)\) this recovers that the semifinite normal traces are the multiples \(c\operatorname{Tr}\) with \(c<\infty\); the multiple \(\infty\cdot\operatorname{Tr}\) is normal but not semifinite.

**Example 7.5** (A computation). Let \(M=\ell^\infty(\mathbb N)\) with \(\mathbb N=\{0,1,2,\dots\}\), \(\tau(f)=\sum_nf(n)\) and \(\tau'(f)=\sum_nnf(n)\). Then \(\tau_0(f)=\sum_n(1+n)f(n)\) and \(a(n)=1/(1+n)\). Here \(s(a)=1\), while \(1-a\) vanishes at \(0\): its support is the indicator of \(\{1,2,\dots\}\), which is \(s(\tau')\).

## 8. The extended center-valued trace

A finite algebra has a center-valued trace with values in \(Z\). On a semifinite algebra such as \(B(H)\), the trace of \(1\) is infinite, so a center-valued trace must be allowed to take infinite values. We first build the space of such values, then the trace itself, and we show that it is unique up to an invertible central factor.

### The extended positive part of an abelian algebra

In this subsection \(Z\) is any commutative von Neumann algebra and \(Z_*^+\) its set of normal positive functionals. For \(b\in Z_+\) and \(\varphi\in Z_*^+\), the functional \(b\varphi=\varphi(b\,\cdot\,)\) is again normal and positive, since \(\varphi(bc)=\varphi(b^{1/2}cb^{1/2})\).

**Definition 8.1** (Extended positive part). \(\widehat Z_+\) is the set of functions \(m:Z_*^+\to[0,\infty]\) for which some increasing net \((a_i)\) in \(Z_+\) satisfies \(m(\varphi)=\sup_i\varphi(a_i)\) for every \(\varphi\); we say that \((a_i)\) *represents* \(m\). An element \(a\in Z_+\) gives the function \(\varphi\mapsto\varphi(a)\), and \(a\) is determined by it; we identify the two, so \(Z_+\subseteq\widehat Z_+\). We write \(m\le n\) if \(m(\varphi)\le n(\varphi)\) for all \(\varphi\), and we define \(m+n\), \(\lambda m\) for \(\lambda\ge0\) (with \(0\cdot\infty=0\)), and \((b\cdot m)(\varphi)=m(b\varphi)\) for \(b\in Z_+\).

For \(Z=\mathbb C1\) this is simply \([0,\infty]\). For \(Z=\ell^\infty(S)\) it is the set of all functions \(S\to[0,\infty]\), through \(m\mapsto(m(\delta_s))_s\).

**Lemma 8.2** (Calculus in \(\widehat Z_+\)). Let \(m,n\in\widehat Z_+\) be represented by \((a_i)_{i\in I}\) and \((c_j)_{j\in J}\).

1. \(m\) is additive and positively homogeneous in \(\varphi\), and \(m(\sum_k\varphi_k)=\sum_km(\varphi_k)\) whenever \(\varphi_k\in Z_*^+\) and \(\sum_k\varphi_k(1)<\infty\).
2. \(m+n\), \(\lambda m\) and \(b\cdot m\) lie in \(\widehat Z_+\), represented by \((a_i+c_j)_{(i,j)}\), \((\lambda a_i)\) and \((ba_i)\).
3. If \(m\le c\) for some \(c\in Z_+\), then \(m\in Z_+\).
4. Every upward directed family \((m_\alpha)\) in \(\widehat Z_+\) has its pointwise supremum in \(\widehat Z_+\).
5. The function \(m\cdot n\) represented by \((a_ic_j)_{(i,j)}\) does not depend on the representing nets. The product is commutative and distributive, \(m\cdot b=b\cdot m\) for \(b\in Z_+\), \((b\cdot m)\cdot n=b\cdot(m\cdot n)\), and \((\sup_\alpha m_\alpha)\cdot n=\sup_\alpha(m_\alpha\cdot n)\) for upward directed families.
6. If \((z_k)\) are orthogonal projections of \(Z\) with \(\sum_kz_k=1\), then \(m(\varphi)=\sum_k(z_k\cdot m)(\varphi)\) for all \(\varphi\). So \(m\) is determined by the \(z_k\cdot m\).

**Proof.** (1) Suprema of increasing nets add, so \(m\) is additive, and it is homogeneous. Additivity gives \(m(\psi)\ge m(\varphi)\) when \(\psi-\varphi\in Z_*^+\). If \(\varphi=\sum_k\varphi_k\) with \(\sum_k\varphi_k(1)<\infty\), the series converges in norm, so \(\varphi\in Z_*^+\). For each \(i\), \(\varphi(a_i)=\sum_k\varphi_k(a_i)\le\sum_km(\varphi_k)\), so \(m(\varphi)\le\sum_km(\varphi_k)\); and for finite \(F\), \(\sum_{k\in F}m(\varphi_k)=m(\sum_{k\in F}\varphi_k)\le m(\varphi)\).

(2) The nets are increasing; for \(ba_i\) this uses \(ba_i=b^{1/2}a_ib^{1/2}\). The values are \(\sup\varphi(a_i)+\sup\varphi(c_j)\), \(\lambda\sup\varphi(a_i)\) and \(\sup_i(b\varphi)(a_i)=m(b\varphi)\).

(3) \(\varphi(a_i)\le m(\varphi)\le\varphi(c)\) for all \(\varphi\), so \(a_i\le c\). The bounded increasing net \((a_i)\) has a supremum \(a\in Z_+\), and \(\varphi(a)=\sup_i\varphi(a_i)=m(\varphi)\) by normality.

(4) For \(m\in\widehat Z_+\) let \(D(m)=\{a\in Z_+:a\le m\}\). It contains the representing net, so its pointwise supremum is \(m\). It is upward directed: for \(a,c\in D(m)\) let \(p\) be the spectral projection of \(a-c\) for \([0,\infty)\) and \(a\vee c=ap+c(1-p)\), which majorizes \(a\) and \(c\). By (1), \(\varphi(a\vee c)=(p\varphi)(a)+((1-p)\varphi)(c)\le m(p\varphi)+m((1-p)\varphi)=m(\varphi)\). Now let \((m_\alpha)\) be upward directed. The union \(D\) of the sets \(D(m_\alpha)\) is upward directed, since two of its elements lie in a common \(D(m_\gamma)\), and \(\sup_{a\in D}\varphi(a)=\sup_\alpha m_\alpha(\varphi)\). So \(D\), indexed by itself, represents the pointwise supremum.

(5) The net \((a_ic_j)\) is increasing, and
\[
\sup_{i,j}\varphi(a_ic_j)=\sup_i\sup_j(a_i\varphi)(c_j)=\sup_in(a_i\varphi)=\sup_jm(c_j\varphi),
\]
the last by symmetry. The third expression does not involve the net of \(n\), and the fourth does not involve the net of \(m\); so the value depends only on \(m\) and \(n\). Commutativity is clear. The other rules follow by computing with representing nets: \((c_j+c'_l)\) represents \(n+n'\) and \(a_i(c_j+c'_l)=a_ic_j+a_ic'_l\); a constant net represents \(b\); \((ba_i)c_j=b(a_ic_j)\); and for an upward directed family, \(D=\bigcup_\alpha D(m_\alpha)\) represents \(\sup_\alpha m_\alpha\), so \(\sup_{a\in D,j}\varphi(ac_j)=\sup_\alpha(m_\alpha\cdot n)(\varphi)\).

(6) \(\varphi=\sum_kz_k\varphi\) with \(\sum_k(z_k\varphi)(1)=\varphi(1)\), so (1) gives \(m(\varphi)=\sum_km(z_k\varphi)\). \(\square\)

**Definition 8.3** (Finite and invertible elements). An element \(m\in\widehat Z_+\) is *finite* if there are orthogonal projections \(z_k\in Z\) with \(\sum_kz_k=1\) and \(z_k\cdot m\in Z_+\) for every \(k\). It is *invertible* if, moreover, \(z_k\cdot m\ge\varepsilon_kz_k\) for some \(\varepsilon_k>0\) and every \(k\).

If \(m\) is invertible, let \(c_k\) be the inverse of \(z_k\cdot m\) in \(Zz_k\), and let \(m^{-1}\) be the supremum of the finite partial sums of \(\sum_kc_k\). By Lemma 8.2(5) and (6), \(z_k\cdot(m\cdot m^{-1})=(z_k\cdot m)\,c_k=z_k\) for each \(k\), so \(m\cdot m^{-1}=1\). A product of two invertible elements, or of an invertible and a finite element, is invertible, respectively finite: refine the two families of projections to the family of products \(z_kw_l\).

*Remark.* One can also describe \(\widehat Z_+\) through the Gelfand spectrum of \(Z\), as continuous functions with values in \([0,\infty]\); a finite element in the sense above is one that is finite on a dense open subset of the spectrum. [Kostecki, Section 5.3] describes the extended positive part of any von Neumann algebra through lower semicontinuous functions on the normal positive functionals.

**Lemma 8.4** (Extending a trace of \(Z\)). Let \(\mu\) be a normal trace on \(Z\), written \(\mu=\sum_k\mu_k\) with \(\mu_k\in Z_*^+\) (Proposition 7.1). For \(m\in\widehat Z_+\) put \(\mu(m)=\sum_km(\mu_k)\).

1. \(\mu(m)=\sup_i\mu(a_i)\) for every representing net; so \(\mu(m)\) does not depend on the choice of the \(\mu_k\), and it agrees with \(\mu\) on \(Z_+\).
2. \(\mu\) is additive and positively homogeneous on \(\widehat Z_+\), and \(\mu(\sup_\alpha m_\alpha)=\sup_\alpha\mu(m_\alpha)\) for upward directed families.
3. If \(\mu\) is faithful and \(\mu(m)=0\), then \(m=0\).
4. If \(\mu\) is faithful and \(\mu(m)<\infty\), then \(m\) is finite.

**Proof.** (1) \(\sum_k\sup_i\mu_k(a_i)=\sup_i\sum_k\mu_k(a_i)\): for finite sums of increasing nets this is clear, and both sides are suprema over the finite partial sums. (2) follows from (1), with the representing nets of Lemma 8.2. (3) If \(\mu(m)=0\), then \(\mu(a_i)=0\), so \(a_i=0\) for all \(i\), and \(m=0\).

(4) Let \((a_i)\) represent \(m\). For \(n\ge1\) let \(q_{n,i}\) be the spectral projection of \(a_i\) for \((n,\infty)\). It increases with \(i\), because the \(a_i\) commute and increase. Put \(P_n=\sup_iq_{n,i}\), which decreases in \(n\), and \(P=\inf_nP_n\). Since \(a_i\ge n\,q_{n,i}\) and \(P\le P_n\),
\[
\mu(m)\ge\mu(P\cdot m)=\sup_i\mu(Pa_i)\ge n\sup_i\mu(Pq_{n,i})=n\,\mu(PP_n)=n\,\mu(P),
\]
by normality. So \(\mu(P)\le\mu(m)/n\) for all \(n\), \(\mu(P)=0\), and \(P=0\). On the other hand \(1-P_n\le1-q_{n,i}\), so \((1-P_n)a_i=(1-P_n)(1-q_{n,i})a_i\le n(1-P_n)\), and therefore \((1-P_n)\cdot m\le n(1-P_n)\) is in \(Z_+\) by Lemma 8.2(3). The projections \(z_1=1-P_1\) and \(z_n=P_{n-1}-P_n\) (\(n\ge2\)) are orthogonal, add up to \(1-P=1\), and \(z_n\cdot m=z_n\cdot((1-P_n)\cdot m)\in Z_+\). \(\square\)

**Proposition 8.5** (Radon–Nikodym theorem in the center). Let \(\mu\) be a faithful semifinite normal trace on \(Z\), and \(\nu\) any normal trace on \(Z\). There is a unique \(h\in\widehat Z_+\) with
\[
\nu(b)=\mu(b\cdot h)\qquad(b\in Z_+).
\tag{8.1}
\]

**Proof.** For \(n\ge1\) let \(f_n(t)=\min((1-t)/t,\,n)\) for \(0<t\le1\), and \(f_n(0)=n\); then \(tf_n(t)=\min(1-t,nt)\), which increases to \((1-t)1_{(0,1]}(t)\) as \(n\to\infty\).

*Existence.* Let \(z\) be the projection of the semifinite part of \(\nu\): \(\nu\) is semifinite on \(Zz\), and \(\nu(b)=\infty\) for nonzero \(b\in Z_+(1-z)\). On the algebra \(Zz\), with unit \(z\), apply Theorem 7.2 to the faithful semifinite normal trace \(\mu|_{Zz}\) and the semifinite normal trace \(\nu|_{Zz}\): there is \(a\in Zz\), \(0\le a\le z\), with support \(z\), such that \(\mu(c)=(\mu+\nu)(ac)\) and \(\nu(c)=(\mu+\nu)((z-a)c)\) for \(c\in(Zz)_+\). Put \(h_n=f_n(a)z+n(1-z)\), with \(f_n(a)\) computed in \(Zz\). The \(h_n\) increase; let \(h\) be their supremum. For \(b\in Z_+\), Lemma 8.2(5) and Lemma 8.4(2) give \(\mu(b\cdot h)=\sup_n\mu(bh_n)\), and
\[
\mu(bh_n)=(\mu+\nu)\bigl(\min(z-a,na)\,bz\bigr)+n\,\mu(b(1-z)).
\]
As \(n\to\infty\), the first term increases to \((\mu+\nu)((z-a)bz)=\nu(bz)\), by normality and because \(a\) has support \(z\). The second is \(0\) if \(b(1-z)=0\) and increases to \(\infty\) otherwise, since \(\mu\) is faithful; so it tends to \(\nu(b(1-z))\). Hence \(\mu(b\cdot h)=\nu(bz)+\nu(b(1-z))=\nu(b)\).

*Uniqueness.* Let \(h\) satisfy (8.1). For \(b\in Z_+\) with \(\mu(b)<\infty\), the functional \(b\mu=\mu(b\,\cdot\,)\) is normal and positive, equal to \(\sum_kb\mu_k\), and Lemma 8.2(1) gives \(\mu(b\cdot h)=\sum_kh(b\mu_k)=h(b\mu)\). So (8.1) determines \(h\) on these functionals. Now let \(\varphi\in Z_*^+\). By Theorem 7.2 on \(Z\), applied to \(\mu\) and \(\varphi\), there is \(a\in Z\) with \(0\le a\le1\), \(s(a)=1\), \(\mu=(\mu+\varphi)(a\,\cdot\,)\) and \(\varphi=(\mu+\varphi)((1-a)\,\cdot\,)\). Put \(b_n=f_n(a)\). Then \(b_n\mu=(\mu+\varphi)(\min(1-a,na)\,\cdot\,)\), so \(\mu(b_n)\le\varphi(1)<\infty\), and the functionals \(b_n\mu\) increase to \(\varphi\). Writing \(\varphi=b_1\mu+\sum_n(b_{n+1}-b_n)\mu\), Lemma 8.2(1) gives \(h(\varphi)=\sup_nh(b_n\mu)\). So \(h\) is determined by (8.1). \(\square\)

### Extended center-valued traces

From now on \(Z\) is the center of the von Neumann algebra \(M\).

**Definition 8.6** (Extended center-valued trace). A map \(T:M_+\to\widehat Z_+\) is an *extended center-valued trace* if
\[
T(x+y)=T(x)+T(y),\qquad T(ax)=a\cdot T(x)\ (a\in Z_+),\qquad T(x^*x)=T(xx^*).
\tag{8.2}
\]
It is *normal* if \(T(\sup_ix_i)=\sup_iT(x_i)\) for bounded increasing nets, *faithful* if \(T(x)=0\) only for \(x=0\), and *semifinite* if \(\mathfrak n_T=\{x\in M:T(x^*x)\in Z_+\}\) is \(\sigma\)-weakly dense in \(M\).

With \(a=\lambda1\), \(T\) is positively homogeneous; it is monotone, since \(T(y)=T(x)+T(y-x)\) for \(x\le y\); and \(T(e)=T(f)\) when \(e\sim f\). The set \(\mathfrak n_T\) is a two-sided ideal, by the argument used for \(\mathfrak n_\tau\): \((x+y)^*(x+y)\le2x^*x+2y^*y\), \((ax)^*(ax)\le\|a\|^2x^*x\), \(T(xx^*)=T(x^*x)\), and Lemma 8.2(3).

Examples: the center-valued trace of a finite algebra, restricted to \(M_+\), is a faithful semifinite normal extended center-valued trace with values in \(Z_+\). On \(B(H)\) with \(H\neq0\), where \(\widehat Z_+=[0,\infty]\), the usual trace is one.

**Theorem 8.7** (Construction from a trace). Let \(\tau\) be a faithful semifinite normal trace on \(M\) and \(\mu\) a faithful semifinite normal trace on \(Z\). For \(x\in M_+\), \(\nu_x(b)=\tau(bx)\) is a normal trace on \(Z\); let \(T(x)\in\widehat Z_+\) be its density with respect to \(\mu\) (Proposition 8.5), so that
\[
\tau(bx)=\mu(b\cdot T(x))\qquad(b\in Z_+,\ x\in M_+).
\tag{8.3}
\]
Then \(T\) is a faithful semifinite normal extended center-valued trace, and \(\tau(x)=\mu(T(x))\).

**Proof.** \(\nu_x\) is additive and homogeneous; it is normal because \(b_i\uparrow b\) gives \(x^{1/2}b_ix^{1/2}\uparrow x^{1/2}bx^{1/2}\); and it is a trace because \(Z\) is commutative. Each property of \(T\) follows from the uniqueness in Proposition 8.5, applied to two densities of the same normal trace:

- \(\nu_{x+y}=\nu_x+\nu_y\), and \(\mu(b\cdot(T(x)+T(y)))=\nu_x(b)+\nu_y(b)\); so \(T(x+y)=T(x)+T(y)\).
- For \(a\in Z_+\), \(\nu_{ax}(b)=\tau(bax)=\nu_x(ab)=\mu(b\cdot(a\cdot T(x)))\); so \(T(ax)=a\cdot T(x)\).
- For \(z\in M\) and \(b\in Z_+\), with \(w=zb^{1/2}\), \(\nu_{z^*z}(b)=\tau(w^*w)=\tau(ww^*)=\tau(zbz^*)=\nu_{zz^*}(b)\); so \(T(z^*z)=T(zz^*)\).
- If \(x_i\uparrow x\), the \(T(x_i)\) increase by additivity. Let \(m\) be their supremum. By Lemma 8.4(2) and Lemma 8.2(5), \(\mu(b\cdot m)=\sup_i\mu(b\cdot T(x_i))=\sup_i\tau(bx_i)=\tau(bx)\), by normality of \(\tau\). So \(m=T(x)\).
- \(\tau(x)=\nu_x(1)=\mu(T(x))\). If \(T(x)=0\), then \(\tau(x)=0\) and \(x=0\).
- If \(x\in\mathfrak n_\tau\), then \(\mu(T(x^*x))=\tau(x^*x)<\infty\), so \(T(x^*x)\) is finite (Lemma 8.4(4)): there are orthogonal central projections \(z_k\) with sum \(1\) and \(z_k\cdot T(x^*x)\in Z_+\). For finite sets \(F\), with \(z_F=\sum_{k\in F}z_k\), we get \(T((xz_F)^*(xz_F))=z_F\cdot T(x^*x)\in Z_+\), so \(xz_F\in\mathfrak n_T\), and \(xz_F\to x\) strongly. So the \(\sigma\)-weak closure of \(\mathfrak n_T\) contains \(\mathfrak n_\tau\), which is dense. \(\square\)

**Lemma 8.8.** Let \(T\) be a faithful extended center-valued trace and \(e\) a projection. If \(T(e)\) is finite, then \(e\) is finite.

**Proof.** Let \(e\sim e_1\le e\). Then \(T(e)=T(e_1)\) and \(T(e)=T(e_1)+T(e-e_1)\). Let \(z_k\) be orthogonal central projections with sum \(1\) and \(z_k\cdot T(e)\in Z_+\). Then \(z_k\cdot T(e_1)\) and \(z_k\cdot T(e-e_1)\) are dominated by \(z_k\cdot T(e)\), so they lie in \(Z_+\), and we may subtract: \(z_k\cdot T(e-e_1)=z_k\cdot T(e)-z_k\cdot T(e_1)=0\). So \(T(z_k(e-e_1))=0\), and \(z_k(e-e_1)=0\) by faithfulness. Summing over \(k\), \(e=e_1\). \(\square\)

**Theorem 8.9** (Semifiniteness and uniqueness). For a von Neumann algebra \(M\) the following are equivalent:

- (i) \(M\) is semifinite;
- (ii) \(M\) has a faithful semifinite normal extended center-valued trace.

Moreover:

1. If \(T\) is a faithful semifinite normal extended center-valued trace and \(\mu\) a faithful semifinite normal trace on \(Z\), then \(\mu\circ T\) is a faithful semifinite normal trace on \(M\).
2. If \(T_1\) and \(T_2\) are faithful semifinite normal extended center-valued traces, there is an invertible \(c\in\widehat Z_+\) with \(T_2(x)=c\cdot T_1(x)\) for all \(x\in M_+\).
3. If \(T\) is a faithful semifinite normal extended center-valued trace and \(\tau\) a faithful semifinite normal trace on \(M\), there is a faithful semifinite normal trace \(\mu\) on \(Z\) with \(\tau=\mu\circ T\).

**Proof.** (i)\(\Rightarrow\)(ii). \(M\) has a faithful semifinite normal trace (background). So does \(Z\): every projection of the commutative algebra \(Z\) is abelian, hence finite, so \(Z\) is semifinite. Theorem 8.7 gives (ii).

(ii)\(\Rightarrow\)(i). Let \(q\ne0\) be a central projection. As \(\mathfrak n_T\) is a \(\sigma\)-weakly dense ideal, \(\mathfrak n_Tq\) contains a nonzero \(x\), and \(x=xq\). The spectral projection \(p\) of \(x^*x\) for \([\|x\|^2/2,\infty)\) is nonzero, lies below \(q\), and satisfies \(p\le2\|x\|^{-2}x^*x\). So \(T(p)\in Z_+\) by Lemma 8.2(3), and \(p\) is finite by Lemma 8.8. So below every nonzero central projection there is a nonzero finite projection, and \(M\) is semifinite.

(1) \(\mu\circ T\) is additive, homogeneous and satisfies the trace identity, by (8.2) and Lemma 8.4(2). It is normal because \(T\) is normal and \(\mu\) preserves suprema (Lemma 8.4(2)), and faithful by Lemma 8.4(3). Semifinite: let \(x\in\mathfrak n_T\) and let \(z\) be a central projection with \(\mu(z)<\infty\). Then \((\mu\circ T)((xz)^*(xz))=\mu(zT(x^*x))\le\|T(x^*x)\|\,\mu(z)<\infty\). Central projections of finite \(\mu\)-trace increase to \(1\), so the \(\sigma\)-weak closure of \(\mathfrak n_{\mu\circ T}\) contains \(\mathfrak n_T\), which is dense.

(2) Choose a faithful semifinite normal trace \(\mu\) on \(Z\) and put \(\tau_k=\mu\circ T_k\), faithful semifinite normal traces by (1). Theorem 7.2 gives a central \(a\) with \(0\le a\le1\), \(s(a)=1\), \(s(1-a)=s(\tau_2)=1\), \(\tau_1=(\tau_1+\tau_2)(a\,\cdot\,)\) and \(\tau_2=(\tau_1+\tau_2)((1-a)\,\cdot\,)\). With \(f_n\) as in Proposition 8.5 put \(c_n=f_n(a)\) and let \(c\) be the supremum of the increasing sequence \(c_n\). For \(x\in M_+\), \(\tau_1(c_nx)=(\tau_1+\tau_2)(\min(1-a,na)x)\), which increases to \((\tau_1+\tau_2)((1-a)x)=\tau_2(x)\) because \(s(a)=1\). Hence, for \(b\in Z_+\),
\[
\mu(b\cdot T_2(x))=\tau_2(bx)=\sup_n\tau_1(c_nbx)=\sup_n\mu\bigl(c_nb\cdot T_1(x)\bigr)=\mu\bigl(b\cdot(c\cdot T_1(x))\bigr),
\]
by Lemma 8.2(5) and Lemma 8.4(2). By the uniqueness in Proposition 8.5, \(T_2(x)=c\cdot T_1(x)\). To see that \(c\) is invertible, let \(z_k\) be the spectral projection of \(a\) for \(\{t:1/k\le t\le1-1/k\}\setminus\{t:1/(k-1)\le t\le1-1/(k-1)\}\) (\(k\ge2\)). Since \(s(a)=s(1-a)=1\), the \(z_k\) are orthogonal with sum \(1\). On \(z_k\) and for \(n\ge k\), \(c_nz_k=((1-a)/a)z_k\) lies between \(z_k/(k-1)\) and \((k-1)z_k\); so \(z_k\cdot c\) is bounded and bounded below.

(3) Let \(\mu_0\) be a faithful semifinite normal trace on \(Z\), and \(\tau_0=\mu_0\circ T\), which is faithful semifinite normal by (1). Theorem 7.2, applied to \(\tau_0\) and \(\tau\), gives a central \(a\) with \(0\le a\le1\), \(s(a)=s(1-a)=1\), \(\tau_0=(\tau_0+\tau)(a\,\cdot\,)\) and \(\tau=(\tau_0+\tau)((1-a)\,\cdot\,)\). With \(c_n=f_n(a)\) as in (2), \(\tau(x)=\sup_n\tau_0(c_nx)=\sup_n\mu_0(c_n\cdot T(x))\). Put \(\mu(b)=\sup_n\mu_0(c_nb)\) for \(b\in Z_+\). This is a normal trace on \(Z\): a supremum of an increasing sequence of normal traces. For \(m\in\widehat Z_+\) represented by \((a_i)\), Lemma 8.4(1) for \(\mu\) and for the traces \(\mu_0(c_n\,\cdot\,)\) gives \(\mu(m)=\sup_i\sup_n\mu_0(c_na_i)=\sup_n\mu_0(c_n\cdot m)\). Hence \(\mu(T(x))=\tau(x)\).

\(\mu\) is faithful: \(\mu(b)=0\) gives \(\mu_0(c_1b)=0\), so \(c_1b=0\), and \(c_1\) has support \(s(1-a)=1\), so \(b=0\). \(\mu\) is semifinite: let \(q\ne0\) be a central projection and \(p\le q\) a nonzero projection of \(M\) with \(\tau(p)<\infty\). Then \(T(p)=q\cdot T(p)\ne0\), so some element \(a_i\) of a net representing \(T(p)\) is nonzero, and \((1-q)a_i\le(1-q)\cdot T(p)=0\). The spectral projection \(q'\) of \(a_i\) for \([\|a_i\|/2,\infty)\) is nonzero, lies below \(q\), and \((\|a_i\|/2)\,\mu(q')\le\mu(T(p))=\tau(p)<\infty\). \(\square\)

**Proposition 8.10** (Finite projections). Let \(M\) be semifinite and \(T\) a faithful semifinite normal extended center-valued trace. A projection \(e\) is finite exactly when \(T(e)\) is finite.

**Proof.** If \(T(e)\) is finite, \(e\) is finite by Lemma 8.8. Conversely let \(e\ne0\) be finite. The algebra \(eMe\) is finite. By the background on countable decomposability, applied to \(eMe\), and since its central projections are the \(ez\) with \(z\in Z\), there are orthogonal central projections \(p_k\) of \(M\) with \(\sum_kp_k=c(e)\) and faithful normal finite traces \(\tau_k\) on \(ep_kMep_k\). Extend \(\tau_k\) from the corner \(ep_k\) to a normal trace \(\sigma_k\) on \(M\) (background); it is faithful and semifinite on \(Mp_k\) and zero on \(M(1-p_k)\). Let \(\tau_1\) be any faithful semifinite normal trace on \(M\), and
\[
\tau(x)=\sum_k\sigma_k(x)+\tau_1(x(1-c(e)))\qquad(x\in M_+).
\]
This is a normal trace; its summands have orthogonal supports \(p_k\) and \(1-c(e)\) with sum \(1\), so it is faithful and semifinite (background on sums). And \(\tau(ep_k)=\tau_k(ep_k)<\infty\).

Let \(\mu\) be a faithful semifinite normal trace on \(Z\), and \(T'\) the extended center-valued trace of Theorem 8.7 for \(\tau\) and \(\mu\). Then \(\mu(p_k\cdot T'(e))=\tau(p_ke)<\infty\), so \(p_k\cdot T'(e)\) is finite by Lemma 8.4(4), while \((1-c(e))\cdot T'(e)=T'((1-c(e))e)=0\). Refining the families, \(T'(e)\) is finite. By Theorem 8.9(2), \(T(e)=c\cdot T'(e)\) with \(c\) invertible, and so \(T(e)\) is finite (Definition 8.3). \(\square\)

**Example 8.11.** (a) If \(M\) is finite with center-valued trace \(T_0\), Theorem 8.9(2) shows that every faithful semifinite normal extended center-valued trace is \(c\cdot T_0\) with \(c=T(1)\) invertible.

(b) Let \(K=\ell^2(\mathbb N)\) and let \(M\) be the algebra of bounded sequences \(x=(x_n)\) with \(x_n\in B(K)\), acting on \(\bigoplus_nK\). Its center is \(\ell^\infty(\mathbb N)\), and \(\widehat Z_+\) is the set of all functions \(\mathbb N\to[0,\infty]\). The map \(T(x)=(\operatorname{Tr}(x_n))_n\) is a faithful semifinite normal extended center-valued trace. Let \(e_n\) be a projection of rank \(n\) in \(B(K)\) and \(e=(e_n)\). Then \(T(e)=(n)_n\) is finite but not bounded, and \(e\) is finite: an isometry \(v\) of \(eMe\) has isometric components \(v_n\) on the finite-dimensional ranges of the \(e_n\), which are unitary. On the other hand the projection \(f\) with \(f_1=1\) and \(f_n=0\) for \(n\ge2\) has \(T(f)=(\infty,0,0,\dots)\), which is not finite, and \(f\) is infinite. So "finite" in Proposition 8.10 cannot be replaced by "bounded".

## 9. Conditional expectations that preserve a trace

**Theorem 9.1** (Trace-preserving conditional expectation). Let \(\tau\) be a faithful semifinite normal trace on \(M\) and \(N\subseteq M\) a von Neumann subalgebra with the same unit. The following are equivalent:

- (a) the restriction of \(\tau\) to \(N_+\) is semifinite;
- (b) there is a normal projection of norm one \(E\) of \(M\) onto \(N\) with \(\tau(E(x))=\tau(x)\) for \(x\in M_+\).

When they hold, \(E\) is unique and faithful, \(E(axb)=aE(x)b\) for \(a,b\in N\), and \(E(x)\) is the unique element of \(N\) with
\[
\tau(E(x)\,y)=\tau(xy)\qquad(y\in\mathfrak m_\tau\cap N).
\tag{9.1}
\]
We call \(E\) the *conditional expectation* of \(M\) onto \(N\) with respect to \(\tau\).

**Proof.** (a)\(\Rightarrow\)(b). The restriction \(\tau_N\) is a faithful semifinite normal trace on \(N\). Its definition ideal is \(\mathfrak m_\tau\cap N\): the inclusion \(\subseteq\) is clear, and if \(x\in\mathfrak m_\tau\cap N\), then \(|x|\in F_\tau\cap N\) and \(x=u|x|\) with \(u\in N\), so \(x\) lies in the definition ideal of \(\tau_N\). For such \(x\), \(|x|\) is the same in \(N\) and in \(M\), so the two trace norms agree. Hence the inclusion extends to an isometry \(j:L^1(N,\tau_N)\to L^1(M,\tau)\). Let \(E\) be its transpose under the dualities of Theorem 1.1: for \(x\in M\), \(E(x)\in N\) is the element with \(\tau_N(E(x)y)=\tau(xy)\) for \(y\in L^1(N,\tau_N)\), in particular (9.1). Then \(E\) is linear, \(\|E(x)\|\le\|x\|\), \(E(b)=b\) for \(b\in N\), and \(E\) is continuous for the \(\sigma\)-weak topologies, because transposes are weak\(^*\) continuous and Theorem 1.1 identifies the topologies. By Tomiyama's theorem \(E\) is positive and \(N\)-bimodular, and a positive \(\sigma\)-weakly continuous map is normal. For \(x\in M_+\), let \(e_i\in F_\tau\cap N\) be projections increasing to \(1\) (semifiniteness of \(\tau_N\)). Using (0.1) and (9.1),
\[
\tau(x)=\sup_i\tau(x^{1/2}e_ix^{1/2})=\sup_i\tau(xe_i)=\sup_i\tau(E(x)e_i)=\sup_i\tau(E(x)^{1/2}e_iE(x)^{1/2})=\tau(E(x)).
\]
If \(E(x^*x)=0\), then \(\tau(x^*x)=0\) and \(x=0\): \(E\) is faithful.

(b)\(\Rightarrow\)(a). Let \(e_i\in F_\tau\) be projections increasing to \(1\). Then \(E(e_i)\in N_+\), \(\tau(E(e_i))=\tau(e_i)<\infty\), and \(E(e_i)\) increases to \(E(1)=1\) by normality. For \(b\in N\), the elements \(E(e_i)bE(e_i)\) lie in the definition ideal of \(\tau_N\) and converge \(\sigma\)-weakly to \(b\). So that ideal is \(\sigma\)-weakly dense, and \(\tau_N\) is semifinite.

Uniqueness. Let \(E'\) be a normal projection of norm one onto \(N\) with \(\tau\circ E'=\tau\). By Tomiyama's theorem it is positive and \(N\)-bimodular. For \(x\in M_+\) and \(y\in F_\tau\cap N\),
\[
\tau(E'(x)y)=\tau(y^{1/2}E'(x)y^{1/2})=\tau(E'(y^{1/2}xy^{1/2}))=\tau(y^{1/2}xy^{1/2})=\tau(xy).
\]
By linearity \(E'(x)\) satisfies (9.1) for all \(x\in M\), and an element of \(N\) is determined by its pairing with the dense subspace \(\mathfrak m_\tau\cap N\) of \(L^1(N,\tau_N)\) (Theorem 1.1 for \(N\)). So \(E'=E\). \(\square\)

**Example 9.2.** (a) *Diagonals.* In \(B(\ell^2)\) with the usual trace, let \(N\) be the diagonal operators. The trace is semifinite on \(N\), and \(E(x)\) is the diagonal of \(x\): both sides of (9.1) equal \(\sum_nx_{nn}y_n\) for a finitely supported diagonal \(y\).

(b) *Scalars.* For \(N=\mathbb C1\subseteq B(\ell^2)\), \(\operatorname{Tr}(\lambda1)=\infty\) for \(\lambda>0\), so the restriction is not semifinite, and there is no trace-preserving normal projection of norm one onto \(\mathbb C1\). Directly: such a map would be \(x\mapsto\varphi(x)1\) with a normal state \(\varphi\), and \(\operatorname{Tr}(x)=\infty\cdot\varphi(x)\) would fail for a rank-one \(x\) (the left side is finite and nonzero, the right side is \(0\) or \(\infty\)).

(c) *Partial traces.* Let \(\tau_0\) be a faithful semifinite normal trace on \(N_0\), let \(M=N_0\bar\otimes B(K)\) with the amplified trace \(\tau(x)=\sum_i\tau_0(x_{ii})\), and \(N=N_0\otimes1\). Then \(\tau(y\otimes1)=(\dim K)\,\tau_0(y)\), so the restriction is semifinite exactly when \(\dim K=n<\infty\). In that case \(E(x)=\bigl(\tfrac1n\sum_ix_{ii}\bigr)\otimes1\), the normalized partial trace.

(d) *The center.* If \(\tau\) is a faithful normal finite trace, the conditional expectation onto the center \(Z\) is the center-valued trace \(T\): for \(y\in Z\), \(\tau(T(x)y)=\tau(T(xy))=\tau(xy)\), because every finite trace factors through the center-valued trace (background), so \(T(x)\) satisfies (9.1).

## 10. Closed operators that agree off a small projection

In an algebra with projections of arbitrarily small trace, a closed operator affiliated with \(M\) is determined by what it does inside corners \(pH\) whose complements have small trace. This section proves this and applies it to cores and to self-adjointness. Only faithfulness of the trace is used; normality and semifiniteness play no part.

An *operator* \(T\) on \(H\) is a linear map from a subspace \(D(T)\), its domain, into \(H\). Its graph is \(G(T)=\{(\xi,T\xi):\xi\in D(T)\}\subseteq H\oplus H\), and \(T\) is *closed* if \(G(T)\) is closed. We write \(S\subseteq T\) if \(G(S)\subseteq G(T)\). An operator \(T\) is *affiliated* with \(M\) if \(u'D(T)=D(T)\) and \(Tu'\xi=u'T\xi\) for every unitary \(u'\in M'\) and every \(\xi\in D(T)\); equivalently, \(u'Tu'^*=T\) for every unitary \(u'\in M'\). Every element of \(M\), as an operator with domain \(H\), is closed and affiliated with \(M\).

**Proposition 10.1** (Small complements). Let \(\tau\) be a faithful trace on \(M\), and let \(e,f\) be projections of \(M\).

1. If for every \(\varepsilon>0\) there is a projection \(p\) with \(e\wedge p=0\) and \(\tau(1-p)<\varepsilon\), then \(e=0\).
2. If for every \(\varepsilon>0\) there is a projection \(p\) with \(e\wedge p\le f\) and \(\tau(1-p)<\varepsilon\), then \(e\le f\).
3. If for every \(\varepsilon>0\) there is a projection \(p\) with \(e\wedge p=f\wedge p\) and \(\tau(1-p)<\varepsilon\), then \(e=f\).

**Proof.** (1) By the parallelogram law, \(e=e-e\wedge p\sim e\vee p-p\le1-p\). Equivalent projections have equal trace and \(\tau\) is monotone, so \(\tau(e)\le\tau(1-p)<\varepsilon\). Hence \(\tau(e)=0\), and \(e=0\).

(2) Put \(g=e-e\wedge f\). For \(p\) as in the hypothesis, \(g\wedge p\le e\wedge p\le f\) and \(g\wedge p\le g\le e\), so \(g\wedge p\le e\wedge f\). The projection \(g\wedge p\) lies below the two orthogonal projections \(g\) and \(e\wedge f\), so it is \(0\). By (1), \(g=0\), that is, \(e=e\wedge f\le f\).

(3) Apply (2) twice. \(\square\)

To compare unbounded operators we pass to matrices over \(M\).

**Lemma 10.2** (Matrices and graphs). For \(n\ge1\) let \(M_n(M)\) be the set of \(n\times n\) matrices \(X=(x_{ij})\) with entries in \(M\), acting on \(H^n=H\oplus\cdots\oplus H\). For \(y\in B(H)\) write \(y\otimes1\) for the diagonal matrix with all diagonal entries \(y\).

1. \(M_n(M)\) is a von Neumann algebra: it is the commutant of \(\{y'\otimes1:y'\in M'\}\). It contains the scalar matrices \((c_{ij}1)\) and the projections \(p\otimes1\), \(p\in\operatorname{Proj}(M)\).
2. If \(\tau\) is a faithful trace on \(M\), then \(\tau_n(X)=\sum_i\tau(x_{ii})\), for \(X\in M_n(M)_+\), is a faithful trace on \(M_n(M)\), and \(\tau_n(p\otimes1)=n\,\tau(p)\).
3. Let \(T_1,\dots,T_k\) be closed operators affiliated with \(M\), and \(D=D(T_1)\cap\cdots\cap D(T_k)\). The subspace
\[
G(T_1,\dots,T_k)=\{(\xi,T_1\xi,\dots,T_k\xi):\xi\in D\}\subseteq H^{k+1}
\]
is closed, and its projection \(g\) lies in \(M_{k+1}(M)\). For a projection \(p\in M\), the projection \(g\wedge(p\otimes1)\) has range consisting of the vectors \((\xi,T_1\xi,\dots,T_k\xi)\) with \(\xi\in D\cap pH\) and \(T_j\xi\in pH\) for every \(j\).

For \(k=1\) we write \(g(T)\in M_2(M)\) for the projection onto \(G(T)\).

**Proof.** (1) A matrix \(X\) commutes with \(y'\otimes1\) exactly when \(x_{ij}y'=y'x_{ij}\) for all \(i,j\). So \(M_n(M)\) is the commutant of a self-adjoint set of operators, hence a von Neumann algebra.

(2) The diagonal entries of a positive matrix are positive, since \(x_{ii}=V_i^*XV_i\) for the inclusion \(V_i\) of \(H\) as the \(i\)-th summand. So \(\tau_n\) is defined, and it is additive and positively homogeneous. For \(Y\in M_n(M)\),
\[
\tau_n(Y^*Y)=\sum_{i,k}\tau(y_{ki}^*y_{ki})=\sum_{i,k}\tau(y_{ki}y_{ki}^*)=\tau_n(YY^*).
\]
If \(X\ge0\) and \(\tau_n(X)=0\), write \(X=Y^*Y\) with \(Y=X^{1/2}\). The computation gives \(\tau(y_{ki}^*y_{ki})=0\), so every \(y_{ki}\) is \(0\), and \(X=0\).

(3) If \((\xi_m,T_1\xi_m,\dots,T_k\xi_m)\) converges to \((\xi,\eta_1,\dots,\eta_k)\), then \(\xi\in D(T_j)\) and \(T_j\xi=\eta_j\), because each \(T_j\) is closed. So the subspace is closed. For a unitary \(u'\in M'\), \((u'\otimes1)(\xi,T_1\xi,\dots)=(u'\xi,T_1u'\xi,\dots)\), so the subspace is invariant under the unitaries \(u'\otimes1\), and \(g\) commutes with them. Every element of \(M'\) is a linear combination of unitaries, so \(g\) commutes with every \(y'\otimes1\), and \(g\in M_{k+1}(M)\) by (1). The projection \(g\wedge(p\otimes1)\) is the projection onto the intersection of the two ranges, and the range of \(p\otimes1\) is \((pH)^{k+1}\). \(\square\)

**Theorem 10.3** (Operators that agree on large corners). Let \(\tau\) be a faithful trace on \(M\), and let \(S\) and \(T\) be closed operators affiliated with \(M\). Suppose there are projections \(p_n\in M\) with \(\tau(1-p_n)\to0\) such that, for every \(n\):

- (i) if \(\xi\in p_nH\cap D(T)\) and \(T\xi\in p_nH\), then \(\xi\in D(S)\);
- (ii) if \(\xi\in p_nH\cap D(S)\) and \(S\xi\in p_nH\), then \(\xi\in D(T)\);
- (iii) \(S\xi=T\xi\) whenever \(\xi\in p_nH\cap D(S)\cap D(T)\) and both \(S\xi\) and \(T\xi\) lie in \(p_nH\).

Then \(S=T\).

**Proof.** *Step 1: \(S\xi=T\xi\) for every \(\xi\in D(S)\cap D(T)\).* Let \(g\in M_3(M)\) be the projection onto \(G(T,S)\) (Lemma 10.2(3)), and let \(d\) be the projection onto \(\{(\xi,\eta,\zeta)\in H^3:\eta=\zeta\}\). The projection \(d\) is a scalar matrix, so \(d\in M_3(M)\). By Lemma 10.2(3) and condition (iii), the range of \(g\wedge(p_n\otimes1)\) lies in the range of \(d\), so \(g\wedge(p_n\otimes1)\le d\). As \(\tau_3(1-p_n\otimes1)=3\tau(1-p_n)\to0\), Proposition 10.1(2), applied in \(M_3(M)\) with the faithful trace \(\tau_3\), gives \(g\le d\). This is the claim.

*Step 2: \(T\subseteq S\).* By Lemma 10.2(3), the range of \(g(T)\wedge(p_n\otimes1)\) consists of the vectors \((\xi,T\xi)\) with \(\xi\in p_nH\cap D(T)\) and \(T\xi\in p_nH\). For such \(\xi\), condition (i) gives \(\xi\in D(S)\), and Step 1 gives \(S\xi=T\xi\); so \((\xi,T\xi)\in G(S)\). Hence \(g(T)\wedge(p_n\otimes1)\le g(S)\) for every \(n\), and Proposition 10.1(2) in \(M_2(M)\) gives \(g(T)\le g(S)\), that is, \(T\subseteq S\).

*Step 3.* By condition (ii) and Step 1, the argument of Step 2 with \(S\) and \(T\) exchanged gives \(S\subseteq T\). \(\square\)

**Remark 10.4.** (a) For a single projection the three conditions do not make the two graphs meet \((pH)^2\) in the same subspace. Take \(M=M_2(\mathbb C)\) with standard basis \(\varepsilon_1,\varepsilon_2\), the projection \(p=e_{11}\), \(T=0\) and \(S=e_{21}\). The only \(\xi\in pH\) with \(S\xi\in pH\) is \(\xi=0\), so (i)–(iii) hold for \(p\). But \((\varepsilon_1,0)\) lies in \(G(T)\cap(pH)^2\) and not in \(G(S)\). For this reason Step 1 compares \(S\) and \(T\) in \(M_3(M)\) before the graphs are compared in \(M_2(M)\).

(b) For \(M=B(H)\) with the trace \(\operatorname{Tr}\), the number \(\operatorname{Tr}(1-p)\) is the dimension of \((1-p)H\). So \(\operatorname{Tr}(1-p_n)\to0\) forces \(p_n=1\) for large \(n\), and Theorem 10.3 says nothing new. It has content in algebras with projections of arbitrarily small nonzero trace, such as \(L^\infty[0,1]\) or a factor of type II\(_1\).

**Corollary 10.5** (Cores and self-adjointness). Let \(\tau\) be a faithful trace on \(M\), let \(e_n\in M\) be projections with \(\tau(1-e_n)\to0\), and let \(\mathcal D\) be the linear span of \(\bigcup_ne_nH\).

1. \(\mathcal D\) is dense in \(H\).
2. If \(T\) is closed, affiliated with \(M\), and \(\mathcal D\subseteq D(T)\), then \(\mathcal D\) is a core for \(T\): for every \(\xi\in D(T)\) there are \(\xi_m\in\mathcal D\) with \(\xi_m\to\xi\) and \(T\xi_m\to T\xi\).
3. If \(T\) is closed, symmetric and affiliated with \(M\), and \(\mathcal D\subseteq D(T)\), then \(T\) is self-adjoint.

**Proof.** (1) Let \(e=\bigvee_ne_n\). Then \(\tau(1-e)\le\tau(1-e_n)\) for every \(n\), so \(\tau(1-e)=0\) and \(e=1\). The closure of \(\mathcal D\) is \(eH=H\).

(2) The graph of the restriction \(T|_{\mathcal D}\) has its closure inside the closed set \(G(T)\), so this closure is the graph of an operator \(T_0\subseteq T\). As \(e_n\in M\), the subspace \(\mathcal D\) is invariant under the unitaries of \(M'\); hence the graph of \(T|_{\mathcal D}\) and its closure are invariant under \(u'\otimes1\), and \(T_0\) is affiliated with \(M\). Apply Theorem 10.3 to \(S=T_0\), \(T\) and \(p_n=e_n\). Condition (i) holds because \(e_nH\subseteq\mathcal D\subseteq D(T_0)\), and (ii) and (iii) hold because \(T_0\subseteq T\). So \(T_0=T\), which is the claim.

(3) Here \(T\) is densely defined and \(T\subseteq T^*\). The adjoint \(T^*\) is closed (background). It is affiliated with \(M\): for a unitary \(U\) and a densely defined \(A\), the definition of the adjoint gives \((UAU^*)^*=UA^*U^*\); so \(u'T^*u'^*=(u'Tu'^*)^*=T^*\) for every unitary \(u'\in M'\). Apply Theorem 10.3 to \(S=T^*\), \(T\) and \(p_n=e_n\). Condition (i) holds because \(D(T)\subseteq D(T^*)\); (ii) holds because \(e_nH\subseteq\mathcal D\subseteq D(T)\); and (iii) holds because \(T^*\) extends \(T\). So \(T^*=T\). \(\square\)

In a finite algebra no trace is needed.

**Theorem 10.6** (Finite algebras). If \(M\) is finite, every closed symmetric operator affiliated with \(M\) is self-adjoint.

**Proof.** Let \(R\) be a closed, densely defined operator affiliated with \(M\), and let \(e_{11}\in M_2(M)\) be the diagonal matrix with entries \(1\) and \(0\). The element \(x=e_{11}g(R)\) of \(M_2(M)\) maps \(G(R)\) onto \(D(R)\oplus0\), which is dense in \(H\oplus0\); so the projection onto the closure of the range of \(x\) is \(e_{11}\). If \(x\zeta=0\), then \(g(R)\zeta\) lies in \(G(R)\cap(0\oplus H)\), which is \(\{0\}\) because \(R0=0\); so the kernel of \(x\) is the kernel of \(g(R)\), and the projection onto \((\ker x)^\perp\) is \(g(R)\). By the polar decomposition in \(M_2(M)\), \(g(R)\sim e_{11}\).

Now let \(T\) be closed, symmetric and affiliated with \(M\). As in Corollary 10.5(3), \(T^*\) is closed, densely defined and affiliated with \(M\), and \(g(T)\le g(T^*)\) because \(T\subseteq T^*\). By the first paragraph, \(g(T)\sim e_{11}\sim g(T^*)\). Under the identification of \(H^2\) with \(H\otimes\mathbb C^2\), the algebra \(M_2(M)\) is \(M\bar\otimes B(\mathbb C^2)\), since both consist of the finite sums of the operators \(y\otimes e_{ij}\); so it is finite by Proposition 6.1(2). A finite projection is not equivalent to a proper subprojection, so \(g(T)=g(T^*)\), and \(T=T^*\). \(\square\)

**Example 10.7** (Finiteness is needed). On \(L^2[0,1]\), the operator \(i\,d/dx\), with domain the absolutely continuous functions \(\varphi\) with \(\varphi'\in L^2\) and \(\varphi(0)=\varphi(1)=0\), is closed and symmetric but not self-adjoint: its adjoint is \(i\,d/dx\) on all absolutely continuous \(\varphi\) with \(\varphi'\in L^2\), without boundary conditions. It is affiliated with the infinite factor \(B(L^2[0,1])\), whose commutant is \(\mathbb C1\).

## 11. Equivalence of positive elements

Two projections are equivalent when they have the form \(v^*v\) and \(vv^*\). For positive elements one allows sums. Throughout this section \(M\) is an arbitrary von Neumann algebra. A sum \(\sum_ia_i\) of positive elements is the strong limit of the increasing net of its finite partial sums. It exists exactly when these partial sums are bounded, it is then their supremum, and a double sum of positive elements may be summed in either order.

**Definition 11.1.** For \(h,k\in M_+\) we write \(h\approx k\) if there is a family \((x_i)_{i\in I}\) in \(M\) with
\[
h=\sum_ix_i^*x_i,\qquad k=\sum_ix_ix_i^* .
\tag{11.1}
\]

If \(e\sim f\) for projections \(e,f\), then \(e\approx f\), with a family of one element. Theorem 11.10 proves the converse. The main tool is a refinement of two decompositions of the same element.

**Lemma 11.2** (Asymmetric Riesz decomposition). Let \((x_i)_{i\in I}\) and \((y_j)_{j\in J}\) be families in \(M\) with \(\sum_ix_i^*x_i=\sum_jy_j^*y_j=a\). There are \(z_{ij}\in M\) with
\[
x_ix_i^*=\sum_jz_{ij}^*z_{ij}\quad(i\in I),\qquad y_jy_j^*=\sum_iz_{ij}z_{ij}^*\quad(j\in J).
\tag{11.2}
\]

**Proof.** Fix \(i\). Since \(x_i^*x_i\le a\), we have \(\|x_i\xi\|^2\le\langle a\xi,\xi\rangle=\|a^{1/2}\xi\|^2\) for \(\xi\in H\). So \(c_i(a^{1/2}\xi)=x_i\xi\) defines a linear contraction on the range of \(a^{1/2}\). Extend it by continuity to the closure \(s(a)H\) of that range, and by \(0\) on \((1-s(a))H\). Then \(c_ia^{1/2}=x_i\) and \(c_i(1-s(a))=0\). For a unitary \(u'\in M'\) we have \(u'c_ia^{1/2}\xi=u'x_i\xi=x_iu'\xi=c_iu'a^{1/2}\xi\), and \(u'\) leaves \((1-s(a))H\) invariant. So \(c_i\) commutes with \(u'\), and \(c_i\in M\).

For \(\xi\in H\), \(\sum_i\|c_ia^{1/2}\xi\|^2=\sum_i\langle x_i^*x_i\xi,\xi\rangle=\|a^{1/2}\xi\|^2\). So every finite partial sum \(S_F\) of \(\sum_ic_i^*c_i\) satisfies \(\langle S_F\eta,\eta\rangle\le\|\eta\|^2\) for \(\eta\in s(a)H\), and \(S_F=s(a)S_Fs(a)\); hence \(S_F\le s(a)\). The supremum \(c\) of the \(S_F\) satisfies \(c\le s(a)\) and \(\langle c\eta,\eta\rangle=\|\eta\|^2\) for \(\eta\) in the dense subspace \(a^{1/2}H\) of \(s(a)H\). So the positive operator \(s(a)-c\) vanishes on a dense subspace of \(s(a)H\) and on \((1-s(a))H\), and \(\sum_ic_i^*c_i=s(a)\).

In the same way \(y_j=d_ja^{1/2}\) with \(d_j\in M\) and \(\sum_jd_j^*d_j=s(a)\). Put \(z_{ij}=d_ja^{1/2}c_i^*\). Conjugation \(y\mapsto wyw^*\) preserves suprema of bounded increasing nets, so
\[
\sum_iz_{ij}z_{ij}^*=d_ja^{1/2}s(a)a^{1/2}d_j^*=d_jad_j^*=y_jy_j^*,\qquad\sum_jz_{ij}^*z_{ij}=c_ia^{1/2}s(a)a^{1/2}c_i^*=c_iac_i^*=x_ix_i^* .\qquad\square
\]

*Reference:* the lesson on C\*-algebras, Theorem 14.1 proves the same refinement for sums that converge in norm in a C\*-algebra.

**Proposition 11.3** (Properties of \(\approx\)). Let \(h,k\in M_+\).

- (a) \(\approx\) is an equivalence relation on \(M_+\).
- (b) If \(h=\sum_ih_i\), \(k=\sum_ik_i\) and \(h_i\approx k_i\) for every \(i\), then \(h\approx k\).
- (c) If \(h\approx k\) and \(\lambda\ge0\), then \(\lambda h\approx\lambda k\).
- (d) If \(h\approx\sum_{i\in I}k_i\) with \(k_i\in M_+\), then \(h=\sum_{i\in I}h_i\) with \(h_i\in M_+\) and \(h_i\approx k_i\) for every \(i\).
- (e) If \(h\approx k\) and \(a\in Z_+\), then \(ah\approx ak\). Moreover \(h=0\) exactly when \(k=0\); so \(zh=0\) exactly when \(zk=0\), for every central projection \(z\).
- (f) If \(hMk\ne\{0\}\), there are \(h_1,k_1\in M_+\) with \(0\ne h_1\approx k_1\), \(h_1\le h\) and \(k_1\le k\).
- (g) There are a central projection \(z\) and elements \(h_1,k_1\in M_+\) with \(zh\approx k_1\le zk\) and \((1-z)k\approx h_1\le(1-z)h\).

**Proof.** (a) Reflexivity: \(h=(h^{1/2})^*h^{1/2}=h^{1/2}(h^{1/2})^*\). Symmetry: replace \(x_i\) by \(x_i^*\). Transitivity: let \(h\approx k\) through \((x_i)\) and \(k\approx l\) through \((y_j)\). Then \(\sum_i(x_i^*)^*x_i^*=k=\sum_jy_j^*y_j\). Lemma 11.2, applied to the families \((x_i^*)\) and \((y_j)\), gives \(z_{ij}\) with \(x_i^*x_i=\sum_jz_{ij}^*z_{ij}\) and \(y_jy_j^*=\sum_iz_{ij}z_{ij}^*\). So \(h=\sum_{i,j}z_{ij}^*z_{ij}\) and \(l=\sum_{i,j}z_{ij}z_{ij}^*\), and \(h\approx l\).

(b) Put the implementing families side by side.

(c) Use the family \((\lambda^{1/2}x_i)\).

(d) Let \(h\approx\sum_ik_i\) through \((x_\alpha)\). Lemma 11.2, applied to the families \((x_\alpha^*)\) and \((k_i^{1/2})\), gives \(z_{\alpha i}\) with \(x_\alpha^*x_\alpha=\sum_iz_{\alpha i}^*z_{\alpha i}\) and \(k_i=\sum_\alpha z_{\alpha i}z_{\alpha i}^*\). Put \(h_i=\sum_\alpha z_{\alpha i}^*z_{\alpha i}\); its partial sums are bounded by \(h\). Then \(\sum_ih_i=\sum_\alpha x_\alpha^*x_\alpha=h\), and \(h_i\approx k_i\) through \((z_{\alpha i})_\alpha\).

(e) As \(a\) is central and multiplication by \(a\) preserves suprema of bounded increasing nets, \(ah=\sum_i(x_ia^{1/2})^*(x_ia^{1/2})\) and \(ak=\sum_i(x_ia^{1/2})(x_ia^{1/2})^*\). If \(k=0\), then \(x_ix_i^*=0\), so \(x_i=0\) for every \(i\), and \(h=0\); by symmetry \(h=0\) forces \(k=0\). Apply this to \(zh\approx zk\).

(f) Choose \(y\in M\) with \(hyk\ne0\). Then \(x=h^{1/2}yk^{1/2}\) is nonzero, since \(hyk=h^{1/2}xk^{1/2}\). Scaling \(y\), we may assume \(\|y\|^2\max(\|h\|,\|k\|)\le1\). Then
\[
x^*x=k^{1/2}y^*hyk^{1/2}\le\|h\|\,k^{1/2}y^*yk^{1/2}\le k,\qquad xx^*=h^{1/2}yky^*h^{1/2}\le\|k\|\,h^{1/2}yy^*h^{1/2}\le h .
\]
Take \(h_1=xx^*\) and \(k_1=x^*x\). The one-element family \((x^*)\) gives \(h_1\approx k_1\), and \(h_1\ne0\).

(g) Let \(\mathcal F\) be the collection of subsets \(F\subseteq M\setminus\{0\}\) with \(\sum_{x\in F}xx^*\le h\) and \(\sum_{x\in F}x^*x\le k\), ordered by inclusion. The union of a chain in \(\mathcal F\) lies in \(\mathcal F\), since each finite subset of it lies in one member. By Zorn's lemma, \(\mathcal F\) has a maximal element \(F\). Put \(h'=h-\sum_{x\in F}xx^*\) and \(k'=k-\sum_{x\in F}x^*x\), both positive.

Suppose \(h'Mk'\ne\{0\}\). By (f) there is \(x\ne0\) with \(xx^*\le h'\) and \(x^*x\le k'\), and then \(tx\) has the same properties for \(0<t\le1\). Only countably many of the elements \(tx\) lie in \(F\): if \(\xi\) is a vector with \(\langle xx^*\xi,\xi\rangle>0\), then \(\sum_{tx\in F}t^2\langle xx^*\xi,\xi\rangle\le\langle h\xi,\xi\rangle\). So some \(tx\) is not in \(F\), and \(F\cup\{tx\}\) belongs to \(\mathcal F\), which contradicts maximality. Hence \(h'Mk'=\{0\}\).

Let \(e=s(h')\) and \(f=s(k')\). From \(h'yk'=0\) for all \(y\in M\) we get \(q(h')yk'=0\) for every polynomial \(q\) with \(q(0)=0\), then \(g(h')yk'=0\) for every continuous \(g\) with \(g(0)=0\), and finally \(eyk'=0\), since \(\min(mh',1)\to e\) strongly. The same argument on the right gives \(eyf=0\) for all \(y\in M\). If \(c(e)c(f)\) were nonzero, the comparison theorem would give nonzero projections \(e_1\le e\), \(f_1\le f\) and a partial isometry \(v\) with \(v^*v=f_1\) and \(vv^*=e_1\); then \(v=e_1vf_1\) would be a nonzero element of \(eMf\). So \(c(e)c(f)=0\). Put \(z=c(f)\). Then \(zh'=zeh'=0\) and \((1-z)k'=(1-z)fk'=0\). Hence
\[
zh=\sum_{x\in F}(zx)(zx)^*\approx\sum_{x\in F}(zx)^*(zx)=:k_1\le zk,\qquad (1-z)k=\sum_{x\in F}((1-z)x)^*((1-z)x)\approx\sum_{x\in F}((1-z)x)((1-z)x)^*=:h_1\le(1-z)h .\qquad\square
\]

**Example 11.4.** (a) In a commutative algebra \(x^*x=xx^*\), so \(h\approx k\) only if \(h=k\).

(b) In \(M_2(\mathbb C)\) put \(x_1=2^{-1/2}e_{11}\) and \(x_2=2^{-1/2}e_{21}\). Then
\[
x_1^*x_1+x_2^*x_2=e_{11},\qquad x_1x_1^*+x_2x_2^*=\tfrac12(e_{11}+e_{22})=\tfrac12\cdot1 .
\]
So the projection \(e_{11}\) is equivalent to the scalar \(\frac12\cdot1\), which is not a projection. Theorem 11.5 explains this: \(\frac12\cdot1\) is the value of the center-valued trace at \(e_{11}\).

**Theorem 11.5** (Traces and \(\approx\)). Let \(M\) be semifinite and \(T\) a faithful semifinite normal extended center-valued trace on \(M\) (Definition 8.6).

1. If \(h\approx k\), then \(T(h)=T(k)\).
2. If \(T(h)=T(k)\) and this element of \(\widehat Z_+\) is finite (Definition 8.3), then \(h\approx k\).
3. If \(M\) is finite with center-valued trace \(T_0\), then \(h\approx T_0(h)\) for every \(h\in M_+\).

**Proof.** We use two facts about a finite element \(m\in\widehat Z_+\). Let \(z_j\) be orthogonal central projections with sum \(1\) and \(z_j\cdot m\in Z_+\). If \(n\in\widehat Z_+\) and \(n\le m\), then \(z_j\cdot n\le z_j\cdot m\), so \(z_j\cdot n\in Z_+\) by Lemma 8.2(3), and \(n\) is finite. If moreover \(m+n=m\), then \(z_j\cdot m+z_j\cdot n=z_j\cdot m\) in \(Z_+\), so \(z_j\cdot n=0\) for every \(j\), and \(n=0\) by Lemma 8.2(6). Also \(z\cdot m\) is finite for every central projection \(z\), with the same \(z_j\).

(1) If \(h=\sum_ix_i^*x_i\) and \(k=\sum_ix_ix_i^*\), then normality, additivity and \(T(x^*x)=T(xx^*)\) give
\[
T(h)=\sup_F\sum_{i\in F}T(x_i^*x_i)=\sup_F\sum_{i\in F}T(x_ix_i^*)=T(k),
\]
the suprema taken over the finite sets \(F\subseteq I\).

(2) Let \(m=T(h)=T(k)\), and take \(z\), \(h_1\), \(k_1\) as in Proposition 11.3(g). By (1) and (8.2), \(T(k_1)=T(zh)=z\cdot m\). Also
\[
z\cdot m=T(zk)=T(k_1)+T(zk-k_1)=z\cdot m+T(zk-k_1).
\]
As \(z\cdot m\) is finite, \(T(zk-k_1)=0\), and \(zk=k_1\) because \(T\) is faithful. So \(zh\approx zk\). In the same way \(T(h_1)=T((1-z)k)=(1-z)\cdot m\) and \((1-z)\cdot m=T((1-z)h)=T(h_1)+T((1-z)h-h_1)\), so \(h_1=(1-z)h\) and \((1-z)h\approx(1-z)k\). By Proposition 11.3(a),(b), \(h=zh+(1-z)h\approx zk+(1-z)k=k\).

(3) A finite algebra is semifinite, and \(T_0\), restricted to \(M_+\), is a faithful semifinite normal extended center-valued trace with values in \(Z_+\) (Section 8); its values are finite. Since \(T_0(a)=a\) for central \(a\), \(T_0(T_0(h))=T_0(h)\), and (2) gives \(h\approx T_0(h)\). \(\square\)

Example 11.11 shows that the finiteness condition in (2) cannot be omitted. To go further we need a notion of size for positive elements.

**Lemma 11.6** (\(\sigma\)-finite projections and elements). Call \(h\in M_+\) *\(\sigma\)-finite* if, whenever \(h=\sum_{i\in I}h_i\) with nonzero \(h_i\in M_+\), the index set \(I\) is countable.

1. Subprojections of \(\sigma\)-finite projections, projections equivalent to \(\sigma\)-finite projections, and countable orthogonal sums of \(\sigma\)-finite projections are \(\sigma\)-finite. Below every nonzero projection there is a nonzero \(\sigma\)-finite projection, and \(1\) is the sum of a family of mutually orthogonal \(\sigma\)-finite projections.
2. \(h\in M_+\) is \(\sigma\)-finite exactly when the projection \(s(h)\) is \(\sigma\)-finite. In particular, for projections the two meanings of \(\sigma\)-finite agree.
3. If \(h\) is \(\sigma\)-finite and \(h\approx k\), then \(k\) is \(\sigma\)-finite.
4. For every \(x\in M\) there is a family \((y_\gamma)\) in \(M\) with \(x^*x=\sum_\gamma y_\gamma^*y_\gamma\), \(xx^*=\sum_\gamma y_\gamma y_\gamma^*\), and every \(y_\gamma^*y_\gamma\) and \(y_\gamma y_\gamma^*\) \(\sigma\)-finite.

**Proof.** (1) The claim about subprojections is clear from the definition. Let \(v^*v=e\) and \(vv^*=f\) with \(f\) \(\sigma\)-finite. If the \(e_i\) are mutually orthogonal nonzero projections below \(e\), the \(ve_iv^*\) are mutually orthogonal nonzero projections below \(f\); so there are countably many. Let \(e=\sum_ne_n\) with \(\sigma\)-finite \(e_n\). Choose faithful normal states \(\varphi_n\) of \(e_nMe_n\) (background) and put \(\varphi(x)=\sum_n2^{-n}\varphi_n(e_nxe_n)\). If \(x\in(eMe)_+\) and \(\varphi(x)=0\), then \(e_nxe_n=0\), so \(x^{1/2}e_n=0\) for every \(n\), and \(x^{1/2}=x^{1/2}e=0\). So \(\varphi\) is a faithful normal state of \(eMe\), and \(e\) is \(\sigma\)-finite. For a nonzero projection \(e\) and a unit vector \(\xi\in eH\), the cyclic projection \(p_\xi\) is \(\sigma\)-finite and lies below \(e\) (background). So a maximal family of mutually orthogonal nonzero \(\sigma\)-finite projections has sum \(1\).

(2) Let \(s(h)\) be \(\sigma\)-finite, with a faithful normal state \(\varphi\) of \(s(h)Ms(h)\). If \(h=\sum_ih_i\) with \(h_i\ne0\), then \(h_i\le h\), so \(h_i=s(h)h_is(h)\) and \(\varphi(h_i)>0\). As \(\sum_i\varphi(h_i)=\varphi(h)<\infty\), the set \(I\) is countable. Conversely, if \(s(h)\) is not \(\sigma\)-finite, there are uncountably many mutually orthogonal nonzero projections \(e_\alpha\le s(h)\). With \(r=s(h)-\sum_\alpha e_\alpha\),
\[
h=h^{1/2}rh^{1/2}+\sum_\alpha h^{1/2}e_\alpha h^{1/2},
\]
and every \(h^{1/2}e_\alpha h^{1/2}=(h^{1/2}e_\alpha)(h^{1/2}e_\alpha)^*\) is nonzero, because \(h^{1/2}\) is injective on \(s(h)H\). So \(h\) is not \(\sigma\)-finite. For a projection \(e\), \(s(e)=e\).

(3) Let \(k=\sum_{j\in J}k_j\) with nonzero \(k_j\in M_+\). By Proposition 11.3(d), \(h=\sum_jh_j\) with \(h_j\approx k_j\), and \(h_j\ne0\) by Proposition 11.3(e). So \(J\) is countable.

(4) By (1) choose mutually orthogonal \(\sigma\)-finite projections \(f_\gamma\) with sum \(1\), and put \(a_\gamma=|x|f_\gamma|x|\), so that \(\sum_\gamma a_\gamma=|x|^2=x^*x\). The support of \(a_\gamma=(f_\gamma|x|)^*(f_\gamma|x|)\) is equivalent to the support of \((f_\gamma|x|)(f_\gamma|x|)^*\), which lies below \(f_\gamma\) (background on the polar decomposition). So \(s(a_\gamma)\) is \(\sigma\)-finite by (1). Lemma 11.2, applied to the one-element family \((x)\) and to the family \((a_\gamma^{1/2})\), gives \(z_\gamma\) with \(xx^*=\sum_\gamma z_\gamma^*z_\gamma\) and \(a_\gamma=z_\gamma z_\gamma^*\). Put \(y_\gamma=z_\gamma^*\). Then \(y_\gamma^*y_\gamma=a_\gamma\) is \(\sigma\)-finite by (2), \(\sum_\gamma y_\gamma^*y_\gamma=x^*x\) and \(\sum_\gamma y_\gamma y_\gamma^*=xx^*\). Finally \(s(y_\gamma y_\gamma^*)\sim s(y_\gamma^*y_\gamma)\), so \(y_\gamma y_\gamma^*\) is \(\sigma\)-finite too. \(\square\)

**Proposition 11.7** (Counting \(\sigma\)-finite pieces). Write \(|I|\) for the cardinality of a set \(I\).

1. If \(a=\sum_{i\in I}b_i=\sum_{j\in J}c_j\) with nonzero \(\sigma\)-finite \(b_i,c_j\in M_+\), then \(\aleph_0\cdot|I|=\aleph_0\cdot|J|\).
2. If \(h=\sum_{i\in I}h_i\), \(k=\sum_{j\in J}k_j\) with nonzero \(\sigma\)-finite \(h_i,k_j\in M_+\), and \(h\approx k\), then \(\aleph_0\cdot|I|=\aleph_0\cdot|J|\).

**Proof.** (1) Lemma 11.2, applied to the families \((b_i^{1/2})\) and \((c_j^{1/2})\), gives \(z_{ij}\) with \(b_i=\sum_jz_{ij}^*z_{ij}\) and \(c_j=\sum_iz_{ij}z_{ij}^*\). For fixed \(j\), the element \(c_j\) is \(\sigma\)-finite, so the set \(I_j=\{i:z_{ij}\ne0\}\) is countable. For each \(i\), \(b_i\ne0\), so \(i\in I_j\) for some \(j\). Hence \(I=\bigcup_jI_j\), and \(|I|\le\aleph_0\cdot|J|\). By symmetry \(|J|\le\aleph_0\cdot|I|\), and the claim follows.

(2) Apply Lemma 11.6(4) to each element of a family that implements \(h\approx k\), and delete the zero elements. This gives a family \((y_\alpha)_{\alpha\in A}\) of nonzero elements with \(h=\sum_\alpha y_\alpha^*y_\alpha\), \(k=\sum_\alpha y_\alpha y_\alpha^*\), and all \(y_\alpha^*y_\alpha\) and \(y_\alpha y_\alpha^*\) nonzero and \(\sigma\)-finite. By (1), \(\aleph_0\cdot|I|=\aleph_0\cdot|A|=\aleph_0\cdot|J|\). \(\square\)

**Lemma 11.8.** If \(g\le p\) are projections with \(g\approx p\) and \(g\) finite, then \(g=p\).

**Proof.** Put \(r=p-g\). By Proposition 11.3(d), applied to \(g\approx g+r\), we can write \(g=a+b\) with \(a\approx g\) and \(b\approx r\). Let \(a=\sum_ix_i^*x_i\) and \(g=\sum_ix_ix_i^*\). Then \(x_ix_i^*\le g\) and \(x_i^*x_i\le a\le g\), so \(x_i=gx_ig\), and \(a\approx g\) holds in the finite algebra \(gMg\). Let \(T_g\) be the center-valued trace of \(gMg\). By Theorem 11.5(1) in \(gMg\), \(T_g(a)=T_g(g)=g\). As \(T_g(a)+T_g(b)=T_g(g)\), we get \(T_g(b)=0\), so \(b=0\). Then \(r=0\) by Proposition 11.3(e). \(\square\)

**Lemma 11.9** (Local homogeneity). Let \(e\) be a properly infinite projection and \(q_0\ne0\) a central projection with \(q_0\le c(e)\). There are a nonzero central projection \(q\le q_0\) and a family \((E_\beta)_{\beta\in B}\) of mutually orthogonal, mutually equivalent, properly infinite \(\sigma\)-finite projections with \(c(E_\beta)=q\) for every \(\beta\) and \(\sum_\beta E_\beta=qe\).

**Proof.** The projection \(e'=q_0e\) is nonzero and properly infinite, with \(c(e')=q_0\). Choose a nonzero \(\sigma\)-finite projection \(p\le e'\) (Lemma 11.6(1)), and, by Zorn's lemma, a maximal family \((p_i)_{i\in I}\) of mutually orthogonal projections below \(e'\) with \(p_i\sim p\); the family \(\{p\}\) shows that \(I\) is not empty. Put \(r=e'-\sum_ip_i\). By the comparison theorem there is a central projection \(z\) with \(zp\precsim zr\) and \((1-z)r\precsim(1-z)p\). If \((1-z)p=0\), then \(p=zp\precsim r\), and a subprojection of \(r\) equivalent to \(p\) could be added to the family. So \((1-z)p\ne0\), and \(q=(1-z)c(p)\) is a nonzero central projection with \(q\le c(p)\le q_0\). Then \(qp_i\sim qp\), \(c(qp)=q\), and \(qr\precsim qp\), so \(qr\) is \(\sigma\)-finite.

If \(I\) is finite, \(qe=qe'=\sum_iqp_i+qr\) is a finite sum of \(\sigma\)-finite projections, hence \(\sigma\)-finite. It is properly infinite, as a nonzero central part of \(e\), and \(c(qe)=qc(e)=q\). Take the one-element family \(E=qe\).

If \(I\) is infinite, split \(I\) into countably infinite subsets \(I_\beta\), \(\beta\in B\), and put \(F_\beta=\sum_{i\in I_\beta}qp_i\). Each \(F_\beta\) is \(\sigma\)-finite with \(c(F_\beta)=q\), and the \(F_\beta\) are mutually equivalent, as sums of countably many orthogonal copies of \(qp\). Each \(F_\beta\) is properly infinite. Indeed, write \(F_\beta=\sum_{n\ge1}g_n\) with \(g_n\sim qp\), and let \(w\) be a central projection with \(wF_\beta\ne0\). The projections \(wg_n\) are equivalent to each other, so all of them are nonzero, and \(wF_\beta\sim\sum_nwg_{2n}\), a proper subprojection of \(wF_\beta\). So \(wF_\beta\) is infinite. Fix \(\beta_0\in B\), put \(E_{\beta_0}=F_{\beta_0}+qr\) and \(E_\beta=F_\beta\) for \(\beta\ne\beta_0\). The projection \(E_{\beta_0}\) is \(\sigma\)-finite with central support \(q\), so absorption gives \(E_{\beta_0}\precsim F_{\beta_0}\). As \(F_{\beta_0}\le E_{\beta_0}\), we get \(E_{\beta_0}\sim F_{\beta_0}\), and \(E_{\beta_0}\) is properly infinite too. So the \(E_\beta\) are as claimed, and \(\sum_\beta E_\beta=\sum_iqp_i+qr=qe\). \(\square\)

**Theorem 11.10** (\(\approx\) on projections). Let \(e\) and \(f\) be projections with \(e\approx f\).

1. If \(e\) or \(f\) is finite, then \(e\sim f\).
2. If \(e\) or \(f\) is \(\sigma\)-finite, then \(e\sim f\).
3. In all cases \(e\sim f\).

So on projections, \(\approx\) is Murray–von Neumann equivalence.

**Proof.** By Proposition 11.3(e), \(ze=0\) exactly when \(zf=0\), for central projections \(z\); so \(c(e)=c(f)\).

(1) As \(\approx\) is symmetric, we may assume that \(f\) is finite. By the comparison theorem there is a central projection \(z\) with \(ze\precsim zf\) and \((1-z)f\precsim(1-z)e\). Let \(ze\sim g\le zf\). Then \(g\approx ze\), because \(g\sim ze\), and \(ze\approx zf\) by Proposition 11.3(e); so \(g\approx zf\). Also \(g\) is finite, being below \(f\). Lemma 11.8 gives \(g=zf\), so \(ze\sim zf\). Let \((1-z)f\sim g'\le(1-z)e\). Then \(g'\) is finite, being equivalent to a subprojection of \(f\), and in the same way \(g'\approx(1-z)f\approx(1-z)e\). Lemma 11.8 gives \(g'=(1-z)e\), so \((1-z)e\sim(1-z)f\). Adding, \(e\sim f\).

(2) We may assume that \(e\) is \(\sigma\)-finite; then \(f\) is \(\sigma\)-finite by Lemma 11.6(2),(3). Write \(e=e_1+e_2\) with \(e_1\) finite, \(e_2\) properly infinite and \(c(e_1)c(e_2)=0\) (background), and put \(z_1=1-c(e_2)\). Then \(z_1e=e_1\) is finite and \((1-z_1)e=e_2\). Define \(z_2\) for \(f\) in the same way. The central projections \(q_1=z_1\), \(q_2=(1-z_1)z_2\) and \(q_3=(1-z_1)(1-z_2)\) add up to \(1\), and \(q_ke\approx q_kf\) for each \(k\). Since \(q_1e\) and \(q_2f\) are finite, (1) gives \(q_1e\sim q_1f\) and \(q_2e\sim q_2f\). The projections \(q_3e\) and \(q_3f\) are \(\sigma\)-finite, properly infinite or zero, and have the same central support. By absorption each is subequivalent to the other, so \(q_3e\sim q_3f\). Adding, \(e\sim f\).

(3) Define \(q_1,q_2,q_3\) as in (2). As there, \(q_1e\sim q_1f\) and \(q_2e\sim q_2f\) by (1). Replacing \(e\) and \(f\) by \(q_3e\) and \(q_3f\), we may assume that \(e\) and \(f\) are properly infinite, with \(c(e)=c(f)\); if \(q_3e=0\) there is nothing to prove.

Call a nonzero central projection \(q\le c(e)\) *good* if \(qe\) and \(qf\) are both sums of families of mutually orthogonal, mutually equivalent, properly infinite \(\sigma\)-finite projections with central support \(q\). Every nonzero central \(q_0\le c(e)\) majorizes a good projection. Indeed, Lemma 11.9 for \(e\) gives \(q'\le q_0\) and a family \((E_\beta)\) for \(q'e\); Lemma 11.9 for \(f\), with \(q'\le c(f)\), gives a nonzero \(q\le q'\) and a family for \(qf\); and the family \((qE_\beta)\) has the required properties for \(qe\). By Zorn's lemma choose a maximal family \((q_\lambda)\) of mutually orthogonal good projections. Its sum is \(c(e)\), since otherwise \(c(e)-\sum_\lambda q_\lambda\) would majorize a further good projection. As \((1-c(e))e=0=(1-c(f))f\), it suffices to show \(qe\sim qf\) for every good \(q\).

So let \(q\) be good, with \(qe=\sum_{\beta\in B}E_\beta\) and \(qf=\sum_{\gamma\in C}F_\gamma\). Since \(qe\approx qf\), Proposition 11.7(2) gives \(\aleph_0\cdot|B|=\aleph_0\cdot|C|\). If \(B\) and \(C\) are countable, \(qe\) and \(qf\) are \(\sigma\)-finite by Lemma 11.6(1), and (2) gives \(qe\sim qf\). Otherwise both are uncountable and \(|B|=\aleph_0\cdot|B|=\aleph_0\cdot|C|=|C|\). Choose a bijection \(\sigma:B\to C\). For every \(\beta\), the projections \(E_\beta\) and \(F_{\sigma(\beta)}\) are \(\sigma\)-finite and properly infinite with central support \(q\), so by absorption each is subequivalent to the other, and \(E_\beta\sim F_{\sigma(\beta)}\). Adding, \(qe\sim qf\). \(\square\)

**Example 11.11** (Finiteness in Theorem 11.5(2) is needed). Let \(K\) be a Hilbert space of dimension \(\aleph_1\) and \(M=B(K)\). It is a factor, so \(\widehat Z_+=[0,\infty]\), and the trace \(\operatorname{Tr}\) is a faithful semifinite normal extended center-valued trace. Let \(k\) be the projection onto a separable infinite-dimensional subspace. Then \(\operatorname{Tr}(1)=\operatorname{Tr}(k)=\infty\). The projection \(k\) is \(\sigma\)-finite, because orthogonal nonzero subprojections of \(k\) have orthogonal ranges in a separable space. The projection \(1\) is not, because an orthonormal basis of \(K\) gives uncountably many orthogonal rank-one projections. By Lemma 11.6(3), \(1\not\approx k\).

## 12. Bimodule maps on \(B(H)\) and atomic algebras

In this section the von Neumann algebra \(M\) acts on a Hilbert space \(H\ne0\). A *bimodule map* for \(M\) is a positive linear map \(E:B(H)\to M\) with
\[
E(axb)=aE(x)b\qquad(a,b\in M,\ x\in B(H)).
\tag{12.1}
\]
For such a map, \(E(1)\) is central: for a unitary \(u\in M\), \(uE(1)u^*=E(u1u^*)=E(1)\). By Tomiyama's theorem, every projection of norm one of \(B(H)\) onto \(M\) is a bimodule map.

**Definition 12.1.** \(M\) has *enough normal bimodule maps* if for every nonzero \(x\in B(H)_+\) there is a normal bimodule map \(E\) for \(M\) with \(E(x)\ne0\). \(M\) is *atomic* if every nonzero projection of \(M\) majorizes a minimal projection.

For example, \(B(H)\) has enough normal bimodule maps: the identity map is one. The algebra \(\mathbb C1\) has them as well, but a single map need not suffice (Exercise 3). The atomic algebras are described as follows.

**Lemma 12.2** (Atomic algebras). \(M\) is atomic if and only if there are mutually orthogonal central projections \(z_i\) with \(\sum_iz_i=1\) such that each \(Mz_i\) is a factor containing a minimal projection. In that case \(M\) is isomorphic to a direct sum \(\bigoplus_iB(K_i)\) for Hilbert spaces \(K_i\).

**Proof.** Let \(M\) be atomic and \(e\) a minimal projection. The center of \(eMe=\mathbb Ce\) is \(\mathbb Ce\); it is also \(Ze\), which is isomorphic to \(Zc(e)\) through \(a\mapsto ae\) (background on projections). So \(Zc(e)=\mathbb Cc(e)\): the algebra \(Mc(e)\) is a factor containing \(e\), and \(c(e)\) is a minimal projection of \(Z\). Two minimal projections of \(Z\) are equal or orthogonal. Let \((z_i)\) be the distinct central supports of minimal projections of \(M\), and \(z=\sum_iz_i\). If \(1-z\ne0\), it majorizes a minimal projection \(e\), and \(c(e)\le1-z\) would be one of the \(z_i\), which is impossible. So \(\sum_iz_i=1\).

Conversely, let the \(z_i\) be as in the statement, and let \(p\ne0\) be a projection. Some \(pz_i\) is nonzero. The factor \(Mz_i\) contains a minimal projection \(f\). As the center of \(Mz_i\) is \(\mathbb Cz_i\), the only nonzero central projection below \(z_i\) is \(z_i\), so \(c(f)=z_i=c(pz_i)\). By the comparison theorem there are nonzero \(f_1\le f\) and \(p_1\le pz_i\) with \(f_1\sim p_1\). Then \(f_1=f\), and \(p_1\) is minimal, because \(p_1Mp_1\) is isomorphic to \(fMf=\mathbb Cf\). So \(p\) majorizes the minimal projection \(p_1\).

Finally, \(x\mapsto(xz_i)_i\) is an isomorphism of \(M\) onto the bounded families \((x_i)\) with \(x_i\in Mz_i\), and each factor \(Mz_i\) is isomorphic to some \(B(K_i)\) (background on minimal projections). \(\square\)

The next lemma is the key to the converse direction.

**Lemma 12.3** (Diffuse algebras). A nonzero von Neumann algebra \(N\) without minimal projections has no normal pure state. Hence every pure state of \(N\) is singular.

**Proof.** Suppose \(\omega\) is a normal pure state of \(N\), with support \(e\), and let \((\pi,K,\xi)\) be its cyclic representation. It is normal (background), so \(\pi(N)\) is a von Neumann algebra; it is irreducible because \(\omega\) is pure; so \(\pi(N)=\pi(N)''=B(K)\). If \(x\in eNe\) and \(\pi(x)=0\), then \(\omega(x^*x)=\|\pi(x)\xi\|^2=0\), so \(x=0\), because \(\omega\) is faithful on \(eNe\). Also \(\pi(e)\xi=\xi\), because \(\|\pi(1-e)\xi\|^2=\omega(1-e)=0\). So \(\pi\) is a \(*\)-isomorphism of \(eNe\) onto \(\pi(e)B(K)\pi(e)=B(\pi(e)K)\), and it carries \(\omega\) to the vector state of \(\xi\). That vector state is therefore faithful on \(B(\pi(e)K)\). This forces \(\dim\pi(e)K=1\): otherwise the projection onto the orthogonal complement of \(\xi\) in \(\pi(e)K\) would be a nonzero positive element with value \(0\). Hence \(eNe\) is one-dimensional, and \(e\) is a minimal projection of \(N\), a contradiction.

Now let \(\rho\) be a pure state of \(N\), and \(\rho=\rho_n+\rho_s\) its splitting into a normal and a singular positive functional (background). As \(\rho_n\le\rho\) and \(\rho\) is pure, \(\rho_n=\lambda\rho\) with \(\lambda\in[0,1]\). If \(\lambda>0\), then \(\rho=\lambda^{-1}\rho_n\) is a normal pure state, which we have excluded. So \(\rho=\rho_s\) is singular. \(\square\)

**Lemma 12.4** (Bimodule maps vanish over a diffuse part). Let \(z\ne0\) be a central projection of \(M\) such that \(Mz\) has no minimal projection, and let \(E\) be a bimodule map for \(M\). Then \(E(q)=0\) for every rank-one projection \(q\in B(H)\) with \(q\le z\). If \(E\) is normal, then \(E(zxz)=0\) for every \(x\in B(H)\).

**Proof.** Let \(\omega\) be a pure state of the von Neumann algebra \(Mz\) on \(zH\), and put \(\varphi(x)=\omega(E(zxz))\) for \(x\in B(H)\); note that \(E(zxz)=zE(x)z\) lies in \(Mz\). Split the positive functional \(\varphi\) on \(B(H)\) as \(\varphi=\varphi_n+\varphi_s\), with \(\varphi_n\) normal and \(\varphi_s\) singular (background).

Put \(c=E(1)z\), a positive element of the center of \(Mz\). For \(a\in Mz\), (12.1) gives \(\varphi(a)=\omega(E(a))=\omega(aE(1))=\omega(ac)\). The restriction \(\psi\) of \(\varphi\) to \(Mz\) is singular. Indeed, \(\omega\) is singular by Lemma 12.3, so every nonzero projection of \(Mz\) majorizes a nonzero projection \(r\in Mz\) with \(\omega(r)=0\), and then \(\psi(r)=\omega(rcr)\le\|c\|\,\omega(r)=0\).

The restriction \(\theta\) of \(\varphi_n\) to \(Mz\) is normal, and \(\theta\le\psi\). Take a maximal family of mutually orthogonal nonzero projections \(r_j\in Mz\) with \(\psi(r_j)=0\). Its sum is \(z\), since a nonzero remainder would majorize one more such projection. Then \(\theta(r_j)=0\) for every \(j\), and \(\theta(z)=\sum_j\theta(r_j)=0\) by normality. So \(\varphi_n(z)=0\). By the Cauchy–Schwarz inequality, \(|\varphi_n(zy)|^2\le\varphi_n(z)\varphi_n(y^*y)=0\) for every \(y\in B(H)\). In particular \(\varphi_n(q)=\varphi_n(zqz)=0\) for a rank-one projection \(q\le z\).

A rank-one projection \(q\) has no nonzero subprojection other than itself, so the singular functional \(\varphi_s\) vanishes at \(q\) (background). Hence \(\omega(E(q))=\varphi(q)=0\). As \(E(q)\in(Mz)_+\) and \(\omega\) is an arbitrary pure state of \(Mz\), the norm formula for positive elements (background) gives \(E(q)=0\).

Let \(E\) be normal and \(x\in B(H)_+\), and put \(y=zxz\). The finite-rank projections \(p\le z\) increase to \(z\), so the elements \(y^{1/2}py^{1/2}\) increase to \(y\). Each of them is a positive operator of finite rank with range in \(zH\), hence a finite sum of positive multiples of rank-one projections below \(z\). So \(E(y)=\sup_pE(y^{1/2}py^{1/2})=0\). Every element of \(B(H)\) is a combination of positive ones. \(\square\)

**Theorem 12.5** (Bimodule maps and atomic algebras).

1. Let \(\theta:M\to N\) be a \(*\)-isomorphism onto a von Neumann algebra \(N\) acting on \(K\). Then \(M\) has enough normal bimodule maps if and only if \(N\) has. So the property depends only on the isomorphism class of \(M\).
2. \(M\) has enough normal bimodule maps if and only if \(M\) is atomic.

**Proof.** (1) By symmetry it suffices to pass the property from \(M\) to \(N\). The isomorphism \(\theta\) is normal (background), so it is a normal unital \(*\)-homomorphism of \(M\) into \(B(K)\). By the structure of normal homomorphisms there are a Hilbert space \(R\) and an isometry \(V:K\to H\otimes R\) such that \(VV^*\) commutes with \(M\otimes1_R\) and \(\theta(a)=V^*(a\otimes1)V\) for \(a\in M\). Then \(V\theta(a)=VV^*(a\otimes1)V=(a\otimes1)VV^*V=(a\otimes1)V\), and taking adjoints, \(\theta(a)V^*=V^*(a\otimes1)\). The space \(R\) is nonzero, because \(K\ne0\) (the algebra \(N\cong M\) is nonzero). For a unit vector \(\eta\in R\) let \(R_\eta\xi=\xi\otimes\eta\); then \((a\otimes1)R_\eta=R_\eta a\) and \(R_\eta^*(a\otimes1)=aR_\eta^*\). Given a normal bimodule map \(E\) for \(M\), put
\[
F(y)=\theta\bigl(E(R_\eta^*VyV^*R_\eta)\bigr)\qquad(y\in B(K)).
\]
It is positive and normal, and it maps \(B(K)\) into \(N\). For \(a,b\in M\),
\[
F(\theta(a)y\theta(b))=\theta\bigl(E(R_\eta^*(a\otimes1)VyV^*(b\otimes1)R_\eta)\bigr)=\theta\bigl(aE(R_\eta^*VyV^*R_\eta)b\bigr)=\theta(a)F(y)\theta(b).
\]
So \(F\) is a normal bimodule map for \(N\). Now let \(y\in B(K)_+\) be nonzero. Then \(VyV^*\ne0\), since \(V^*(VyV^*)V=y\). If \(R_\eta^*VyV^*R_\eta=0\) for every unit vector \(\eta\), then \(\langle VyV^*(\xi\otimes\eta),\xi\otimes\eta\rangle=0\) for all \(\xi,\eta\); so \((VyV^*)^{1/2}\) vanishes on the product vectors, which span a dense subspace, and \(VyV^*=0\). So \(R_\eta^*VyV^*R_\eta\) is a nonzero positive element of \(B(H)\) for some \(\eta\), and some normal bimodule map \(E\) for \(M\) does not vanish at it. As \(\theta\) is injective, the corresponding \(F\) satisfies \(F(y)\ne0\).

(2) Let \(M\) be atomic. By Lemma 12.2 there is an isomorphism of \(M\) onto \(N=\bigoplus_iB(K_i)\), acting on \(K=\bigoplus_iK_i\). Let \(p_i\) be the projection of \(K\) onto \(K_i\), and put \(E(x)=\sum_ip_ixp_i\) for \(x\in B(K)\). The sum converges strongly, \(E(x)\in N\), and \(E\) is positive and normal, as a sum of the normal maps \(x\mapsto p_ixp_i\) with orthogonal ranges. For \(a=(a_i)\) and \(b=(b_i)\) in \(N\), \(p_iaxbp_i=a_ip_ixp_ib_i\), so \(E(axb)=aE(x)b\). If \(x\ge0\) and \(E(x)=0\), then \(x^{1/2}p_i=0\) for every \(i\), so \(x=0\). This single map shows that \(N\) has enough normal bimodule maps, and so has \(M\), by (1).

Conversely, suppose that \(M\) is not atomic. Let \(z_a\) be the supremum of the central supports of the minimal projections of \(M\) (\(z_a=0\) if there are none), and \(z=1-z_a\). If \(z=0\), every nonzero projection \(p\) satisfies \(pc(e)\ne0\) for some minimal \(e\), so \(c(p)c(e)\ne0\), and as in the proof of Lemma 12.2, \(p\) majorizes a minimal projection; then \(M\) would be atomic. So \(z\ne0\). A minimal projection of \(Mz\) is minimal in \(M\), so its central support would lie below both \(z_a\) and \(z\); hence \(Mz\) has no minimal projection. Take a unit vector \(\xi\in zH\) and let \(q\) be the projection onto \(\mathbb C\xi\). By Lemma 12.4, \(E(q)=0\) for every bimodule map \(E\) for \(M\), so \(M\) does not have enough normal bimodule maps. \(\square\)

## Exercises

**Exercise 1** (Matrices). Let \(M=M_n(\mathbb C)\). (a) Show that \(h\approx k\) if and only if \(\operatorname{Tr}(h)=\operatorname{Tr}(k)\), for \(h,k\in M_+\). (b) Find an explicit family that implements \(e_{11}\approx\frac1n\cdot1\).

*Solution.* (a) \(M\) is a finite factor. The map \(T_0(x)=\frac1n\operatorname{Tr}(x)1\) is linear, satisfies \(T_0(x^*x)=T_0(xx^*)\ge0\) and \(T_0(ax)=aT_0(x)\) for scalars \(a\), and \(T_0(1)=1\); so it is the center-valued trace. By Theorem 11.5(1), \(h\approx k\) gives \(T_0(h)=T_0(k)\), that is, \(\operatorname{Tr}(h)=\operatorname{Tr}(k)\). Conversely, if \(\operatorname{Tr}(h)=\operatorname{Tr}(k)\), Theorem 11.5(3) gives \(h\approx T_0(h)=T_0(k)\approx k\), and \(\approx\) is transitive.
(b) Put \(x_j=n^{-1/2}e_{j1}\) for \(j=1,\dots,n\). Then \(\sum_jx_j^*x_j=\frac1n\sum_je_{1j}e_{j1}=e_{11}\) and \(\sum_jx_jx_j^*=\frac1n\sum_je_{j1}e_{1j}=\frac1n\sum_je_{jj}=\frac1n\cdot1\). For \(n=2\) this is Example 11.4(b).

**Exercise 2** (Multiplication operators). Let \((X,\mu)\) be a finite measure space and \(M=L^\infty(X,\mu)\), acting on \(L^2(X,\mu)\) by multiplication. Let \(f\) be a measurable function that is finite almost everywhere, and let \(T_f\) be multiplication by \(f\), with domain \(D(T_f)=\{g\in L^2:fg\in L^2\}\). Show: (a) \(T_f\) is closed and affiliated with \(M\); (b) the functions in \(L^2\) that vanish outside \(\{|f|\le n\}\) for some \(n\) form a core for \(T_f\); (c) if \(f\) is real, \(T_f\) is self-adjoint.

*Solution.* (a) If \(g_m\to g\) and \(fg_m\to h\) in \(L^2\), a subsequence converges almost everywhere, so \(fg=h\) almost everywhere, and \(g\in D(T_f)\) with \(T_fg=h\). A finite measure space is \(\sigma\)-finite, so \(M'=M\) (background on multiplication algebras). A unitary of \(M'\) is multiplication by a function \(u\) with \(|u|=1\) almost everywhere. It maps \(D(T_f)\) onto itself and commutes with \(T_f\).
(b) Let \(e_n\) be multiplication by the indicator function of \(\{|f|\le n\}\), and \(\tau(g)=\int g\,d\mu\), a faithful trace on \(M\) (Example 1.4). Then \(e_nL^2\subseteq D(T_f)\), and \(\tau(1-e_n)=\mu(\{|f|>n\})\to0\), because \(f\) is finite almost everywhere and \(\mu\) is finite. The subspace in (b) is the span of the \(e_nL^2\), so Corollary 10.5(2) applies.
(c) By Corollary 10.5(1), \(T_f\) is densely defined, and for real \(f\) it is symmetric: \(\langle fg,h\rangle=\int fg\bar h\,d\mu=\langle g,fh\rangle\) for \(g,h\in D(T_f)\). Corollary 10.5(3) shows that \(T_f\) is self-adjoint.

**Exercise 3** (Scalars). Let \(M=\mathbb C1\subseteq B(H)\). (a) Show that the normal bimodule maps for \(M\) are the maps \(x\mapsto\omega(x)1\) with \(\omega\) a normal positive functional on \(B(H)\), and that \(M\) has enough normal bimodule maps. (b) Show that there is one normal bimodule map \(E\) with \(E(x)\ne0\) for every nonzero \(x\in B(H)_+\) if and only if \(H\) is separable.

*Solution.* (a) A linear map into \(\mathbb C1\) has the form \(x\mapsto\omega(x)1\) for a linear functional \(\omega\). The map is positive and normal exactly when \(\omega\) is, and (12.1) holds automatically for scalars \(a,b\). For a nonzero \(x\ge0\), choose a unit vector \(\xi\) with \(\langle x\xi,\xi\rangle>0\); the vector state of \(\xi\) gives a map that does not vanish at \(x\).
(b) If \((\varepsilon_n)\) is a countable orthonormal basis, then \(\omega=\sum_n2^{-n}\omega_{\varepsilon_n}\), with \(\omega_{\varepsilon_n}(x)=\langle x\varepsilon_n,\varepsilon_n\rangle\), is faithful: \(\omega(x)=0\) for \(x\ge0\) gives \(x^{1/2}\varepsilon_n=0\) for all \(n\). Conversely, let \(\omega\) be a faithful normal positive functional. By the background on normal functionals, \(\omega(x)=\sum_n\langle x\xi_n,\xi_n\rangle\) for a sequence \((\xi_n)\). Let \(p\) be the projection onto the orthogonal complement of the closed span of the \(\xi_n\). Then \(\omega(p)=0\), so \(p=0\), and \(H\) is the closed span of countably many vectors, hence separable. So for nonseparable \(H\), the atomic algebra \(\mathbb C1\) has enough normal bimodule maps, but no single one does the job.

**Exercise 4** (Diagonal algebras). (a) Show that taking the diagonal of a matrix, \(E(x)=\sum_n\langle x\delta_n,\delta_n\rangle p_n\) with \(p_n\) the projection onto \(\mathbb C\delta_n\), is a normal projection of norm one of \(B(\ell^2)\) onto the algebra \(\ell^\infty\) of diagonal operators. (b) Let \(A\) be the algebra of multiplications by functions in \(L^\infty[0,1]\) on \(L^2[0,1]\), with Lebesgue measure \(\lambda\). Show that every normal bimodule map for \(A\) is zero, and conclude that there is no normal projection of norm one of \(B(L^2[0,1])\) onto \(A\).

*Solution.* (a) Here \(E(x)=\sum_np_nxp_n\), the map of the proof of Theorem 12.5(2) with \(K_n=\mathbb C\delta_n\); so \(E\) is a normal bimodule map into \(\ell^\infty\). It fixes every diagonal operator, and \(\|E(x)\|=\sup_n|\langle x\delta_n,\delta_n\rangle|\le\|x\|\). So \(E\) is a normal projection of norm one onto \(\ell^\infty\).
(b) A projection of \(A\) is multiplication by the indicator function of a measurable set \(S\), and it is nonzero when \(S\) has positive measure. Then \(t\mapsto\lambda(S\cap[0,t])\) is continuous, from \(0\) to \(\lambda(S)\), so \(S\) splits into two sets of positive measure, and the projection has two nonzero orthogonal subprojections. So \(A\) has no minimal projection, and Lemma 12.4, with \(z=1\), shows that every normal bimodule map for \(A\) vanishes on all of \(B(L^2[0,1])\). A normal projection of norm one \(E\) onto \(A\) would be a normal bimodule map by Tomiyama's theorem, with \(E(1)=1\ne0\). By contrast \(\ell^\infty\) in (a) is atomic: the \(p_n\) are minimal projections.

## Historical remarks

The comparison of projections and the dimension theory of factors go back to Murray and von Neumann, who first developed the theory for factors. The algebraic content of this dimension theory was later isolated by Kaplansky in AW\*-algebras and in Baer \*-rings.

Finding a short proof that a finite algebra carries a trace took several attempts, among them [Dixmier 1949] and [Kadison 1955]. The difficulty is additivity. A dimension function on projections yields a functional that is linear on each commutative subalgebra, and the task is to show that it is additive on elements that do not commute. For \(B(H)\), with \(H\) separable of dimension at least \(3\), [Gleason 1957] showed that every countably additive probability measure on the closed subspaces of \(H\) has the form \(P\mapsto\operatorname{Tr}(\rho P)\) for a positive trace-class operator \(\rho\) of trace \(1\). A short proof of the existence of the center-valued trace on a finite algebra was given in [Yeadon 1971].

The duality between an algebra and the integrable elements of a trace (Theorem 1.1), the Hilbert space of a trace and its two actions belong to the noncommutative integration theory of Segal and of [Dixmier 1953], with further contributions in [Dye 1952] and [Kunze 1958]. A short account of the theory is [Nelson 1974].

Semifiniteness of the tensor product of two semifinite algebras was proved in [Misonou 1954], and the case of type III algebras was settled in [Sakai 1957]; together they give Theorem 6.3. The description of the weakly compact subsets of a predual used in Theorems 5.6 and 5.7 comes from [Akemann 1967].

## Where this leads

The norms \(\|x\|_1\) and \(\|x\|_2\) are the cases \(p=1,2\) of \(\|x\|_p=\tau(|x|^p)^{1/p}\). The completions give spaces \(L^p(M,\tau)\), \(1\le p<\infty\), with \(L^p(M,\tau)^*=L^q(M,\tau)\) for \(1<p<\infty\) and \(1/p+1/q=1\), in analogy with Theorem 1.1. They can be realized inside the algebra of \(\tau\)-measurable operators: closed operators affiliated with \(M\) that are controlled, as in Section 10, by projections whose complements have small trace. The lesson *Measurable operators for a trace: examples, convergence and the commutant* studies this algebra and its measure topology.

A faithful normal state that is not a trace still gives a Hilbert space with a left action of \(M\), but \(x\mapsto x^*\) is no longer isometric for its norm, so the conjugation \(J\) of Section 2 is not available directly. The modular operator and the modular conjugation repair this, and the commutation theorem survives in the form \(JMJ=M'\). The lesson *Left and right Hilbert algebras* works out examples of this structure. The lesson Multiplicity of a von Neumann algebra on a Hilbert space compares normal representations through their commutants; there the Hilbert space of a trace is the model of a representation with a conjugation \(J\) such that \(JMJ=M'\).

Traces also enter the topology of unitary groups. For a factor of type II\(_1\), the fundamental group of the unitary group in the norm topology is isomorphic to \(\mathbb R\) under addition [Araki–Smith–Smith 1971], while for many such factors the unitary group is contractible in the strong operator topology, by a theorem of Popa and Takesaki.

## References



- [Kostecki] R. P. Kostecki, *W\*-algebras and noncommutative integration*, arXiv:1307.4818. https://arxiv.org/abs/1307.4818
- [Akemann 1967] C. A. Akemann, *The dual space of an operator algebra*, Trans. Amer. Math. Soc. 126 (1967), 286–302. https://doi.org/10.1090/S0002-9947-1967-0206732-8. Free at https://www.ams.org/journals/tran/1967-126-02/S0002-9947-1967-0206732-8/S0002-9947-1967-0206732-8.pdf
- [Dixmier 1949] J. Dixmier, *Les anneaux d'opérateurs de classe finie*, Ann. Sci. École Norm. Sup. 66 (1949), 209–261. https://doi.org/10.24033/asens.970
- [Dixmier 1953] J. Dixmier, *Formes linéaires sur un anneau d'opérateurs*, Bull. Soc. Math. France 81 (1953), 9–39. https://doi.org/10.24033/bsmf.1436
- [Misonou 1954] Y. Misonou, *On the direct product of W\*-algebras*, Tôhoku Math. J. (2) 6 (1954), 189–204. https://www.jstage.jst.go.jp/article/tmj1949/6/2-3/6_2-3_189/_article
- [Nelson 1974] E. Nelson, *Notes on non-commutative integration*, J. Funct. Anal. 15 (1974), 103–116. https://doi.org/10.1016/0022-1236(74)90014-7. Free at https://linkinghub.elsevier.com/retrieve/pii/0022123674900147
- [Yeadon 1971] F. J. Yeadon, *A new proof of the existence of a trace in a finite von Neumann algebra*, Bull. Amer. Math. Soc. 77 (1971), 257–260. https://doi.org/10.1090/S0002-9904-1971-12708-8. Free at https://www.ams.org/journals/bull/1971-077-02/S0002-9904-1971-12708-8/
- [Araki–Smith–Smith 1971] H. Araki, M.-S. B. Smith and L. Smith, *On the homotopical significance of the type of von Neumann algebra factors*, Comm. Math. Phys. 22 (1971), 71–88. Free at https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-22/issue-1/On-the-homotopical-significance-of-the-type-of-von-Neumann/cmp/1103857414.full
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, revised and corrected edition with hyperlinks, free from the author: https://bruceblackadar.com/Mathematics/Cycr.pdf (first published as Encyclopaedia of Mathematical Sciences 122, 2006; the numbering is the same).
- [Dye 1952] H. A. Dye, *The Radon–Nikodym theorem for finite rings of operators*, Trans. Amer. Math. Soc. 72 (1952), 243–280. Free at https://www.ams.org/journals/tran/1952-072-02/S0002-9947-1952-0045954-5/
- [Gleason 1957] A. M. Gleason, *Measures on the closed subspaces of a Hilbert space*, J. Math. Mech. 6 (1957), 885–894. Free at https://doi.org/10.1512/iumj.1957.6.56050
- [Kadison 1955] R. V. Kadison, *On the additivity of the trace in finite factors*, Proc. Nat. Acad. Sci. U.S.A. 41 (1955), 385–387. Free at https://pmc.ncbi.nlm.nih.gov/articles/PMC528101/
- [Kunze 1958] R. A. Kunze, *\(L_p\) Fourier transforms on locally compact unimodular groups*, Trans. Amer. Math. Soc. 89 (1958), 519–540. Free at https://www.ams.org/journals/tran/1958-089-02/S0002-9947-1958-0100235-1/
- [Sakai 1957] S. Sakai, *On topological properties of W\*-algebras*, Proc. Japan Acad. 33 (1957), 439–444. Free at https://doi.org/10.3792/pja/1195524953
