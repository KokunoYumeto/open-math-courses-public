# Detecting a von Neumann algebra through a separable subalgebra

This lesson connects two ways of testing an algebra: positive functionals test its elements, while projections locate the parts those functionals can miss. The connection forces atomicity when a norm-separable C*-subalgebra detects faithfulness of normal states. The normal/singular split and the pure-state representation argument are proved before they are combined.

Independent classical exposition and proof development by GPT-6 Astra (OpenAI), Ultra, October 2026; CC0. The mathematical source comparisons and editorial corrections are given in PD08.

## The question and the two ambient biduals

Let \(A\ne0\) be a norm-separable C*-algebra faithfully represented on a Hilbert space. Pass to the essential space \(\overline{AH}\), and let \(M=A''\) there. Its identity is denoted by \(1\), whether or not \(1\in A\). For \(A=M=0\), the conclusions below are vacuous.

A positive functional is **faithful** when it is positive on every nonzero positive element. A von Neumann algebra is **atomic** when each nonzero projection dominates a minimal nonzero projection. We study the following equivalent conditions:

- every normal state on \(M\) whose restriction to \(A\) is faithful is faithful on \(M\);
- each nonzero projection \(p\in M\) dominates some \(h\in A_+\) with \(0<h\leq p\).

Under these conditions, \(M\) is atomic and every minimal projection of \(M\) belongs to \(A\). We will also identify the precise central summand of \(A^{**}\) giving \(M\), using the normal part of an extension of a faithful pure-state mixture.

Two biduals have different roles. The C*-bidual \(M^{**}\) separates normal and singular functionals on the already given von Neumann algebra \(M\). The bidual \(A^{**}\) carries all representations of the smaller C*-algebra. We keep their central projections distinct.

The written prerequisites are AC3–4, positive order and square roots; BK01–04, Hilbert operators, bicommutants, ultraweak multiplication and monotone limits; SK04, bounded Borel spectral projections; CP06–07, the Banach predual and normal positive functionals; BG01–03, approximate identities and cyclic GNS vectors; ST02–04, positive extension, norming states and state compactness; UB05–08, the universal bidual and normal representation quotients; and WS04–05, null projections and faithful support corners. The Hahn–Banach theorem used below has its complete proof in NP1. The underlying set theory includes the axiom of choice in its Zorn form. These are proof inputs, not replacements by external citations.

## Separating the normal part by a central projection

This section applies to any concrete von Neumann algebra \(M\), without separability or a faithful normal state. Regard \(M\) temporarily as a C*-algebra. Write \(j:M\to V=M^{**}\) for its canonical inclusion. UB06–08 extends the identity representation to a normal surjective *-homomorphism

\[
 q:V\longrightarrow M.
 \tag{PD.1}
\]

There is a central projection \(c\in V\) such that \(\ker q=(1-c)V\), and \(q:cV\to M\) is a normal *-isomorphism with normal inverse \(u\). In particular \(cj(x)=u(x)\) for \(x\in M\).

For a bounded positive functional \(f\) on \(M\), UB05 supplies its unique normal positive extension \(\widehat f\) to \(V\). Define

\[
 \begin{aligned}
 f_{\mathrm n}(x)&=\widehat f(cj(x)),\\
 f_{\mathrm s}(x)&=\\
 &\widehat f((1-c)j(x)).
 \end{aligned}
 \tag{PD.2}
\]

Centrality makes both terms positive, and \(f=f_{\mathrm n}+f_{\mathrm s}\). The first is normal because \(f_{\mathrm n}=\widehat f\circ u\). Their canonical normal extensions to \(V\) are respectively \(X\mapsto\widehat f(cX)\) and \(X\mapsto\widehat f((1-c)X)\): these maps are normal and agree with the stated functionals on \(j(M)\), so UB05 uniqueness applies. Since a positive functional on a unital algebra has norm equal to its value at the identity, ST02 also gives

\[
 \|f\|=\|f_{\mathrm n}\|+\|f_{\mathrm s}\|.
 \tag{PD.3}
\]

A bounded positive functional \(g\) on \(M\) is normal exactly when
\(\widehat g((1-c)X)=0\) for all \(X\in V\). For the forward direction, \(gq\) is a normal extension of \(g\), hence equals \(\widehat g\), and \(q(1-c)=0\). Conversely, the displayed condition makes \(g=g_{\mathrm n}\), which is normal by construction. Call \(g\) **singular** when \(\widehat g(cX)=0\) for all \(X\in V\). A positive functional vanishing at a projection annihilates multiplication by that projection on either side, by the Cauchy–Schwarz inequality in ST02; thus these conditions can equivalently be tested at \(1-c\) or \(c\), respectively.

The split in (PD.2) is unique among sums of a normal positive functional and a singular positive functional: extend any such sum normally to \(V\), then multiply the argument by \(c\) and by \(1-c\). In particular a positive functional which is both normal and singular is zero.

We need two consequences with their hypotheses explicit.

**Domination.** If \(0\leq g\leq n\), with \(n\) normal and positive, then \(g\) is normal. Indeed \(n-g\) is positive, so uniqueness and positivity of canonical extensions give \(0\leq\widehat g\leq\widehat n\). Hence \(\widehat g(1-c)=0\), and the preceding criterion applies.

**Compression.** If \(f\) is singular and \(a\in M\), then \(x\mapsto f(a^*xa)\) is singular. Its canonical extension is
\(X\mapsto\widehat f(j(a)^*Xj(a))\). Centrality of \(c\) makes this vanish on \(cV\). If \(n\) is normal, \(x\mapsto n(a^*xa)\) is normal instead: multiplication by fixed operators is ultraweakly continuous by BK03. Consequently a singular positive functional dominated by a normal positive functional is zero.

Only bounded positive functionals are being asserted here. No decomposition theorem for unbounded weights has been inferred.

## A singular functional leaves a hole in every projection

**Lemma.** If \(\sigma\) is a bounded singular positive functional on \(M\) and \(e\in M\) is a nonzero projection, there is a nonzero projection \(r\leq e\) with \(\sigma(r)=0\).

**Proof.** If \(\sigma(e)=0\), use \(r=e\). Otherwise choose a unit vector in \(eH\). A sufficiently large positive multiple \(\eta\) of its vector state is normal and satisfies \(\eta(e)>\sigma(e)\).

Consider projections \(p\leq e\) satisfying \(\eta(p)\leq\sigma(p)\). They include \(0\). A chain has a supremum projection \(p\), obtained by the bounded monotone limit of its members (BK04), and

\[
 \begin{aligned}
 \eta(p)&=\sup_i\eta(p_i)\\
 &\leq\sup_i\sigma(p_i)\\
 &\leq\sigma(p).
 \end{aligned}
 \tag{PD.4}
\]

Only \(\eta\) was assumed normal in this inequality. Thus every chain has an upper bound in this set. Zorn's lemma supplies a maximal member \(p\). Since \(e\) fails the defining inequality, \(r=e-p\ne0\).

For every nonzero projection \(v\leq r\), maximality implies
\(\sigma(v)<\eta(v)\): otherwise orthogonality would give
\(\eta(p+v)\leq\sigma(p+v)\), contradicting maximality. For \(v=0\), the non-strict inequality also holds. Every positive element \(b\) of \(rMr\) is a norm limit of finite nonnegative linear combinations of spectral projections in that corner, by SK04. Applying the projection inequalities to each finite sum and using boundedness of both functionals gives \(\sigma(b)\leq\eta(b)\).

Therefore the positive functionals \(x\mapsto\sigma(rxr)\) and \(x\mapsto\eta(rxr)\) on \(M\) are ordered. PD02 makes the former singular and the latter normal; domination makes the former normal as well. It must be zero. Taking \(x=1\) proves \(\sigma(r)=0\). \(\square\)

For completeness, this property characterizes singular positive functionals. Suppose every nonzero \(e\) has such a subprojection and \(f_{\mathrm n}\ne0\). WS04–05, applied to the bounded normal positive functional \(f_{\mathrm n}\), gives a nonzero support projection \(s\) on whose corner \(f_{\mathrm n}\) is faithful. A nonzero \(r\leq s\) with \(f(r)=0\) would have \(f_{\mathrm n}(r)=0\), a contradiction. Hence \(f_{\mathrm n}=0\).

The proof uses norm approximation inside the final corner, not monotone continuity of \(\sigma\). Replacing that step by normality of the singular functional would invalidate the argument.

## A countable pure-state test and a positive extension

A **pure state** is an extreme point of the convex state set. We first prove that pure states detect every nonzero positive element, including in a nonunital C*-algebra.

For a unital \(C\) and \(0<a\in C\), ST03–04 says that the set \(F_a\) of states satisfying

\[
 \rho(a)=\|a\|
 \tag{PD.5}
\]

is nonempty and compact in the weak-* topology. It is a face: state values at \(a\) are at most \(\|a\|\), so a proper convex combination attaining that upper bound has both endpoints in \(F_a\).

Among nonempty compact faces contained in \(F_a\), a decreasing chain has nonempty intersection by compactness; the intersection remains a compact face. Zorn's lemma gives a minimal such face \(F\). If it contained distinct states, some self-adjoint \(b\in C\) would distinguish them: split any distinguishing element into real and imaginary self-adjoint parts. The maximizers of the real continuous function \(\rho\mapsto\rho(b)\) on \(F\) would then form a proper nonempty compact face of \(F\), hence of \(S(C)\). This contradicts minimality. Thus \(F\) is a singleton, and its state is pure and norms \(a\). This argument uses compactness of the unital state set only.

For an arbitrary \(A\ne0\), use its forced unitization \(A^\dagger\) from UZ06–07. The cyclic GNS vector in BG03 gives the positive extension of any state \(\rho\) on \(A\):

\[
 \begin{aligned}
 &\rho^\dagger(a+\lambda1)\\
 &\qquad=\rho(a)+\lambda.
 \end{aligned}
 \tag{PD.6}
\]

Indeed extend its nondegenerate representation by
\(\pi^\dagger(a+\lambda1)=\pi(a)+\lambda I\) and take the coefficient at the unit cyclic vector. This proves positivity and norm one of (PD.6).

Choose a pure state \(\tau\) of \(A^\dagger\) with \(\tau(a)=\|a\|\) for the specified \(0<a\in A\). Its restriction to \(A\) has norm one because it attains \(\|a\|\). If that restriction were a proper convex combination of two distinct states, their extensions (PD.6) would decompose \(\tau\), because both sides agree on \(A\) and on \(1\). This contradicts purity. Thus pure states on \(A\) norm every nonzero positive element.

Now assume \(A\) is norm separable. The weak-* topology on the dual unit ball has a countable base. To see this directly, take a norm-dense sequence \((a_k)\) in the unit ball of \(A\). Evaluations on these elements, with rational open discs in \(\mathbb C\) and finite intersections, give a countable base: on the dual unit ball, replacing \(a\) by a nearby scalar multiple of an \(a_k\) changes every evaluation uniformly by at most that norm error. Hence every evaluation is continuous for this countably generated topology, which is therefore the weak-* topology. Any subspace, in particular the pure-state space, is also second countable. Choosing one point from each nonempty member of its countable base gives a countable dense subset.

Choose a sequence \((\rho_j)_{j\geq1}\) dense in the pure-state space, repeating terms if it is finite, and set

\[
 \omega=\sum_{j\geq1}2^{-j}\rho_j.
 \tag{PD.7}
\]

The series converges in norm to a positive functional of norm at most one. Its norm is exactly one. For the positive contractive approximate identity \(e_i\) of BG01, BG03 gives \(\rho_j(e_i)\to1\). Given a finite initial set of indices, a single sufficiently large \(i\) makes all these values close to one, so \(\sup_i\omega(e_i)\geq\sum_{j=1}^N2^{-j}\). Let \(N\) increase. Since \(\|e_i\|\leq1\), the reverse bound follows from \(\|\omega\|\leq1\).

This state is faithful on \(A\). For \(0<a\in A\), a norming pure state exists by the preceding argument. The relatively weak-* open set of pure states with value greater than \(\|a\|/2\) is nonempty, so some \(\rho_j\) lies in it. Then \(\omega(a)\geq2^{-j}\rho_j(a)>0\).

There is a state \(F\) on \(M\) extending \(\omega\). First define it on \(C=A+\mathbb C1_M\) by \(F_0(a+\lambda1_M)=\omega(a)+\lambda\). If \(1_M\in A\), the state norm identity gives \(\omega(1_M)=1\), so this is just \(\omega\). If \(1_M\notin A\), the map \(A^\dagger\to C\), \(a+\lambda1\mapsto a+\lambda1_M\), is an injective *-homomorphism, hence isometric by UB02; (PD.6) proves positivity and norm one of \(F_0\).

The real restriction of \(F_0\) to \(C_{\rm sa}\) has norm one and value one at the identity. Real Hahn–Banach (NP1) extends it to \(M_{\rm sa}\) with the same norm. ST02 proves that the complexification is a positive norm-one extension \(F\) on \(M\). No normality of this extension has been assumed.

## Why a pure-state mixture has an atomic representation

We give the representation argument in full because a general faithful state need not generate an atomic algebra.

**Pure states and the commutant.** Let \((\pi,H,\Omega)\) be the cyclic GNS representation of a state \(\rho\), including the cyclic unit vector for nonunital \(A\) proved in BG03. If \(0\leq\nu\leq\rho\), define on the dense vectors \(\pi(a)\Omega\) the form

\[
 \begin{aligned}
 &Q_\nu(\pi(a)\Omega,\pi(b)\Omega)\\
 &\qquad=\nu(b^*a).
 \end{aligned}
 \tag{PD.8}
\]

The positive-functional Cauchy–Schwarz inequality and domination show

\[
 |\nu(b^*a)|^2
 \leq\rho(a^*a)\rho(b^*b).
\]

Thus the form is well defined, bounded and positive. BK01 supplies a unique positive contraction \(T\) with \(Q_\nu(\xi,\eta)=\langle T\xi,\eta\rangle\). For \(a,b,d\in A\), put \(u=\pi(a)\Omega\) and \(v=\pi(b)\Omega\). Then

\[
 \begin{aligned}
 \langle T\pi(d)u,v\rangle
 &=\nu(b^*da)\\
 &=\langle Tu,\pi(d^*)v\rangle.
 \end{aligned}
\]

Density and the adjoint identity imply \(T\pi(d)=\pi(d)T\). Moreover
\(\nu(a)=\langle T\pi(a)\Omega,\Omega\rangle\): insert an approximate-identity vector \(\pi(e_i)\Omega\to\Omega\) in the second argument of (PD.8), using \(\nu(e_i a)\to\nu(a)\).

Conversely every positive contraction \(T\in\pi(A)'\) defines a positive functional
\(\rho_T(a)=\langle T\pi(a)\Omega,\Omega\rangle\) between \(0\) and \(\rho\). Its norm is \(\langle T\Omega,\Omega\rangle\). The upper bound follows from its vector expression at \(T^{1/2}\Omega\), and equality follows by testing the approximate identity.

If \(\pi(A)'=\mathbb CI\), the first construction shows every positive functional dominated by \(\rho\) is a scalar multiple of \(\rho\). A convex decomposition of \(\rho\) into states is therefore trivial, so \(\rho\) is pure.

Conversely, if the commutant is not scalar, the real or imaginary part of a nonscalar operator gives a nonscalar self-adjoint element. Affine rescaling gives a nonscalar positive contraction \(T\) in the commutant with both \(T\) and \(1-T\) nonzero. The vector \(\Omega\) is separating for the commutant: \(S\Omega=0\) and \(S\pi(a)=\pi(a)S\) imply \(S=0\) on a dense subspace. Apply this to \(T^{1/2}\) and \((1-T)^{1/2}\) to see that
\(t=\rho_T(1)\), interpreted as \(\|\rho_T\|\) if \(A\) is nonunital, lies strictly between zero and one. The decomposition
\(\rho=\rho_T+\rho_{1-T}\) would, for pure \(\rho\), force \(\rho_T=t\rho\). Applying this equality to \(b^*a\) in (PD.8) would give \(T=tI\), a contradiction. Consequently purity is equivalent to
\(\pi(A)'=\mathbb CI\). By BK02 it implies \(\pi(A)''=B(H)\).

**The central atomic pieces.** Put \(N=A^{**}\). For each pure state \(\rho_j\), UB06–08 extends its GNS representation to a normal surjection
\(\overline\pi_j:N\to B(H_j)\). Its central kernel complement is a nonzero central projection \(z_j\), with \(z_jN\cong B(H_j)\).

The center of \(B(H_j)\) consists of scalars. Indeed an operator commuting with every rank-one projection preserves every one-dimensional subspace; applying this to two independent vectors and their sum shows that all its scalar values coincide. Thus \(z_j\) is a minimal nonzero central projection of \(N\). Two such projections are equal or orthogonal: their product is central and lies below each. Let

\[
 z=\bigvee_{j\geq1}z_j.
 \tag{PD.9}
\]

Finite joins of these central projections increase strongly to \(z\) by BK04; commutation passes to that limit, so \(z\) is central.

The algebra \(zN\) is atomic. If \(0\ne p\leq z\) is a projection, some \(pz_j\) is nonzero; otherwise multiplication by all finite joins, then strong convergence, would give \(pz=0\). In \(B(H_j)\), the nonzero projection corresponding to \(pz_j\) dominates the rank-one projection onto the span of any unit vector in its range. Pull it back to \(r\leq pz_j\). Its corner \(rNr\) is one-dimensional because \(z_j\) is central and the rank-one corner of \(B(H_j)\) is scalar. Hence \(r\) is minimal even in \(N\).

For the mixture (PD.7), norm convergence and the isometric canonical extension from UB05 give

\[
 \widehat\omega=\sum_{j\geq1}2^{-j}\widehat\rho_j.
 \tag{PD.10}
\]

Each \(\widehat\rho_j\) vanishes on \(1-z_j\), being the cyclic vector coefficient of \(\overline\pi_j\). Therefore \(\widehat\omega(1-z)=0\).

Let \(\overline\pi_\omega:N\to\pi_\omega(A)''\) be the normal extension of the mixture's GNS representation and let \(w\) be its central kernel complement. The coefficient at its cyclic vector gives

\[
 \|\overline\pi_\omega(1-z)\Omega_\omega\|^2
 =\widehat\omega(1-z)=0.
\]

Since \(1-z\) is central, its image commutes with \(\pi_\omega(A)\). Cyclicity implies that image is zero, hence \(w\leq z\). Every nonzero projection under \(w\) dominates a minimal projection by the argument above. UB08 identifies \(wN\) with \(\pi_\omega(A)''\), proving that this representation is atomic.

More generally, any central summand \(tN\) with \(t\leq z\) is atomic. This observation will identify the particular quotient \(M\); the support of \(\widehat\omega\) itself need not be central.

## When the smaller algebra detects projections

First there is a normal state \(\lambda\) on \(M\) whose restriction to \(A\) is faithful. This assertion alone does not claim that \(\lambda\) is faithful on \(M\). The positive unit sphere of \(A\) is norm separable: rational-radius balls about a countable dense subset of \(A\) give a countable base, and choosing a point from every member meeting that sphere gives a dense sequence \((a_n)\) there.

By the positive-operator norm formula in BK01, choose unit vectors \(\xi_n\) with
\(\langle a_n\xi_n,\xi_n\rangle>3/4\). The normal vector states
\(\lambda_n(x)=\langle x\xi_n,\xi_n\rangle\) give a norm-convergent series in the Banach predual (CP06–07):

\[
 \lambda=\sum_{n\geq1}2^{-n}\lambda_n.
 \tag{PD.11}
\]

It is positive, normal and takes value one at \(1\). For \(0<a\in A\), choose \(n\) with \(\|a/\|a\|-a_n\|<1/4\). Then
\(\lambda_n(a/\|a\|)>1/2\), so \(\lambda(a)>0\). No separability of the represented Hilbert space or prior countable decomposability of \(M\) was used.

Suppose now every normal state faithful on \(A\) is faithful on \(M\). The state just constructed is faithful on \(M\). Given a nonzero projection \(p\in M\), if \(p=1\), normalize any nonzero positive element of \(A\). Otherwise put \(q=1-p\). Faithfulness gives \(\lambda(q)>0\), and

\[
 \lambda_q(x)=\frac{\lambda(qxq)}{\lambda(q)}
 \tag{PD.12}
\]

is a normal state by BK03. It vanishes on \(p\), so it is not faithful on \(M\). The assumed implication, used contrapositively, says its restriction to \(A\) is not faithful. Thus some \(a\in A_+\setminus\{0\}\) satisfies \(\lambda(qaq)=0\). Faithfulness of \(\lambda\) gives \(qaq=0\). The positive square root and C*-identity give \(a^{1/2}q=0\); taking adjoints yields \(aq=qa=0\). Hence \(a=pap\), and the positive order bound in that corner gives \(0<a\leq\|a\|p\). Set \(h=a/\|a\|\).

Conversely suppose each nonzero \(p\in M\) dominates some nonzero \(h\in A_+\). In fact **every bounded positive functional** faithful on \(A\) is faithful on \(M\). If such a functional \(\nu\) vanished on \(0<a\in M\), SK04 gives \(\delta>0\) for which \(p=1_{[\delta,\infty)}(a)\ne0\) and \(p\leq a/\delta\). If all these cuts vanished, the spectral formula would give \(a=0\). Positivity forces \(\nu(p)=0\), and therefore \(\nu(h)=0\) for \(0<h\leq p\) in \(A\), a contradiction. This proves both the equivalence in PD01 and its stated strengthening.

## Faithful normal parts and the atomic quotient

Assume the equivalent conditions of PD01. Let \(F\) be any bounded positive functional on \(M\) whose restriction to \(A\) is faithful. Write \(F=F_{\mathrm n}+F_{\mathrm s}\) as in PD02. For every nonzero projection \(p\in M\), PD03 supplies a nonzero projection \(r\leq p\) with \(F_{\mathrm s}(r)=0\). Projection detection then gives \(0<h\leq r\) in \(A\). Consequently

\[
 \begin{aligned}
 F_{\mathrm n}(h)&=F(h)\\
 &>0.
 \end{aligned}
 \tag{PD.13}
\]

Since \(h\leq p\), positivity gives \(F_{\mathrm n}(p)\geq F_{\mathrm n}(h)>0\). The same spectral-cut argument as in PD06 shows that positivity on every nonzero projection implies faithfulness on all of \(M_+\). Thus \(F_{\mathrm n}\) is faithful. Its norm can be less than \(\|F\|\); no normalization of the normal part is needed.

Choose now the faithful pure-state mixture \(\omega\) of PD04 and any positive norm-preserving extension \(F\) to \(M\). Let
\(\pi:N=A^{**}\to M\) be the normal surjection extending the given inclusion \(A\subset M\), supplied by UB06–08. Write \(t\) for its central kernel complement, so that \(\pi:tN\to M\) is a normal *-isomorphism with normal inverse. Define the normal positive functional

\[
 \psi=F_{\mathrm n}\circ\pi.
 \tag{PD.14}
\]

It vanishes on \((1-t)N\) and is faithful on \(tN\), because \(F_{\mathrm n}\) is faithful and \(\pi\) is injective there.

Its support is exactly \(t\), and therefore central in this application. To check this directly, for every projection \(e\in N\), centrality of \(t\) makes \(te\) a projection and
\(\psi(e)=\psi(te)\). Faithfulness on \(tN\) gives

\[
 \begin{gathered}
 \psi(e)=0\\
 \Longleftrightarrow\ te=0\\
 \Longleftrightarrow\ e\leq1-t.
 \end{gathered}
 \tag{PD.15}
\]

Thus \(1-t\) is the largest null projection, so WS04–05 identifies the bounded-functional support as \(s(\psi)=t\). This is not an assumption that general functional supports are central.

On \(A\), the restriction of \(\psi\) is \(F_{\mathrm n}|_A\leq F|_A=\omega\). Canonical extension preserves positivity and order by UB05; uniqueness identifies the extension of that restriction with \(\psi\). Hence
\(0\leq\psi\leq\widehat\omega\) on \(N\). With \(z\) from PD05, this implies \(\psi(1-z)=0\). Equation (PD.15) gives \(t(1-z)=0\), or \(t\leq z\). Therefore \(A^{**}s(\psi)=tN\) is atomic by PD05, and

\[
 \begin{aligned}
 tN&\longrightarrow M,\\
 X&\longmapsto\pi(X)
 \end{aligned}
 \tag{PD.16}
\]

is the asserted normal *-isomorphism. In particular \(M\) is atomic. This identifies the exact support summand, rather than inferring it just from atomicity of a different GNS representation.

Finally every minimal projection \(p\) of \(M\) belongs to \(A\). Choose \(0<h\leq p\) in \(A_+\). Then \(h=php\). A nonscalar self-adjoint element of \(pMp\) has at least two distinct spectral points; a spectral cut between them would give a projection strictly between \(0\) and \(p\). Thus \(pMp=\mathbb Cp\), and \(h=ap\) for a real scalar \(a>0\). Hence \(p=a^{-1}h\in A\).

The minimal projections generate \(M\) as a von Neumann algebra. For any projection \(e\in M\), choose a maximal orthogonal family of minimal projections below \(e\), using Zorn's lemma. Its supremum is \(e\): a nonzero complementary projection would dominate another minimal projection by atomicity. Finite sums converge strongly to \(e\), so the von Neumann algebra generated by all minimal projections contains every projection of \(M\). Norm approximation of positive elements by finite spectral sums, followed by the real and imaginary decomposition of arbitrary elements, proves that this generated algebra is \(M\). All its generating minimal projections already lie in \(A\).

## Examples, boundaries and exact source comparisons

**A nonunital example.** Let \(H=\ell^2(\mathbb N)\), let \(A\) be the norm closure of the finite-rank operators, and let \(M=B(H)\). Rational complex matrices in the fixed countable basis give a countable dense subset of \(A\): truncate the finitely many vectors defining a finite-rank operator, then approximate their coordinates. Finite-coordinate projections increase strongly to \(I\), and \(x p_n\to x\) strongly for every \(x\in B(H)\); therefore \(A\) is strongly dense in \(M\). Each nonzero projection in \(M\) dominates the rank-one projection onto any unit vector in its range, and that rank-one operator belongs to \(A\). The hypotheses hold even though \(A\) does not contain \(I\): for every finite-rank \(T\) there is a unit vector in its kernel, so \(\|I-T\|\geq1\). This also shows why weak density alone should not be confused with equality \(A=M\).

**Density is relative to pure states.** For \(A=\mathbb C^2\), all states have the form
\(\rho_t(a,b)=ta+(1-t)b\), \(0\leq t\leq1\). Positivity gives the two nonnegative coefficients and norm one makes their sum one. Exactly the endpoints are pure. They do not form a dense subset of the full state interval, although a sequence repeating both is dense in the pure-state subspace. Any mixture giving both endpoints positive mass is faithful. The density hypothesis in PD04 uses the pure-state subspace.

**Supports need not be central.** On \(M_2(\mathbb C)\), the normal state \(x\mapsto x_{11}\) has support \(e_{11}\). Indeed a projection has value zero exactly when it annihilates the first basis vector, and the largest such projection is \(e_{22}\). The projection \(e_{11}\) is not central, since it does not commute with \(e_{12}\). PD07 proves centrality for its particular \(\psi\) from faithfulness of \(F_{\mathrm n}\) on the quotient.

**Sources and scope.** Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), Chapter III, §2, Definition 2.13 and Theorem 2.14, printed pp. 127–128, supplies the normal/singular comparison; Chapter III, §3, Theorem 3.8, printed pp. 134–135, supplies the null-subprojection argument. The related separable-subalgebra problem is Exercise III.3(3), printed p. 139. In the approved local copy these are PDF pp. 135–136, 142–143 and 147. PD02 derives the needed positive-functional split directly from the previously proved universal-bidual quotient, without importing the source's additional invariant-subspace or representation-decomposition assertions.

The full owning result is Takesaki, *Theory of Operator Algebras II* (Springer, 2003), Exercise VIII.1(13), printed p. 97, PDF p. 118 in the approved copy. Its four conclusions are all proved here: projection detection in PD06, faithfulness of the extension's normal part in PD07, the atomic support summand and its quotient isomorphism in PD05–07, and inclusion of minimal projections in PD07. The printed reference in part (b) to “the property in (b)” is a self-reference; here the projection-detection property is specified explicitly and proved equivalent to the initial normal-state condition. The pure-state density and the centrality of \(s(\psi)\) are also clarified rather than silently assumed.
