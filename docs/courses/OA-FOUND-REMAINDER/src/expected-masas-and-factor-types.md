# Expected maximal abelian algebras and factor types

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A normal expectation onto a maximal abelian algebra preserves every semifinite normal trace. This is stronger than saying that the expectation preserves one chosen trace. We prove it by averaging over the abelian algebra's unitaries, then use it to decide the type of a free ergodic crossed product from invariant traces on its coefficient algebra.

The resulting examples have the same diffuse coefficient algebra on the real line. Rational translations give a type-II factor with an infinite semifinite trace. Adding a dilation destroys every invariant semifinite normal trace and gives type III.

Our crossed-product prerequisites are Proposition 1.1, Proposition 3.1 and Theorem 3.2 of [Crossed-product coefficients and factor tests](../reader/crossed-product-coefficients-and-factor-tests.html): the faithful normal coefficient expectation, the two positive coefficient sums, and the maximal-abelian and factor tests. Its named regular-model and freeness prerequisites remain in force. We use existing trace theory rather than reconstruct it here:

- Tomiyama's norm-one projection theorem is Theorem 8.5 of [The universal enveloping von Neumann algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html). A norm-one linear retraction onto a unital operator subalgebra is positive and bimodular.
- Proposition 2.5 of [Traces, part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html) gives the finite-trace approximation criteria for semifiniteness. Its Theorem 6.7 says that an algebra is semifinite exactly when it has a faithful semifinite normal trace. Theorem 5.2 gives the normal centre-valued trace of a finite algebra.
- Proposition 7.1, Theorem 7.2 and Theorem 9.1 of [Traces, part B](../reader/supplements/trace-duality-and-expectations.html) give ultraweak lower semicontinuity of normal traces, the bounded central density comparing two semifinite normal traces, and the trace-preserving normal expectation when the restricted trace is semifinite.
- Type decomposition and the classification of type-I factors are Theorems 7.2 and 10.3 of [Projections and types](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html). Banach–Alaoglu and the elementary operator topologies are in [Operator spaces, trace class and preduals](../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html).

The linked programme lessons contain the complete prerequisite proofs at the stated locators. The elementary examples also use Lebesgue integration, density of interval step functions in \(L^1\), Fubini’s theorem and the usual multiplication representation on \(L^2\). Anantharaman and Popa’s freely readable draft treats finite trace-preserving expectations and normalizers; Takesaki’s book provides further context. The arguments below establish the arbitrary semifinite MASA trace-restriction theorem and the type-II-infinity/type-III alternatives.

## 1. Averaging onto an expected maximal abelian algebra

Let \(M\) be a nonzero von Neumann algebra and \(D\subseteq M\) a maximal abelian unital von Neumann subalgebra. Thus \(D'\cap M=D\). Suppose
\[
P:M\longrightarrow D
\]
is a normal linear retraction of norm one: \(P(d)=d\) for \(d\in D\). Tomiyama's theorem makes \(P\) positive, unital and \(D\)-bimodular. For \(x\in M\), set
\[
K_D(x)=\overline{\operatorname{conv}}^{\,\mathrm{uw}}
\{uxu^*:u\in\mathcal U(D)\}.
\tag{1.1}
\]
This is an ultraweakly compact convex subset of the ball of radius \(\|x\|\).

**Lemma 1.1.** For every \(x\in M\),
\[
K_D(x)\cap D=\{P(x)\}.
\tag{1.2}
\]
Consequently there is at most one normal norm-one retraction onto \(D\).

**Proof.** We first construct a point of \(K_D(x)\) fixed by every conjugation from \(\mathcal U(D)\). For a unitary \(u\in D\), put
\[
A_{n,u}(y)=\frac1n\sum_{k=0}^{n-1}u^k y u^{-k}.
\]
The maps \(A_{n,u}\) are contractions, preserve \(K_D(x)\), and commute for different \(u\), since \(D\) is abelian. The telescoping identity gives
\[
\|\operatorname{Ad}(u)A_{n,u}(y)-A_{n,u}(y)\|
\leq \frac{2\|y\|}{n}.
\tag{1.3}
\]
For a finite set \(F\subseteq\mathcal U(D)\), compose \(A_{n,u}\) over \(u\in F\) and apply the composition to \(x\). The resulting point \(y_{F,n}\in K_D(x)\) satisfies (1.3), with \(y\) replaced by \(x\), for every \(u\in F\): all the other averages commute with \(\operatorname{Ad}(u)\) and are contractions.

For finite \(F\) and \(\varepsilon>0\), the sets
\[
C(F,\varepsilon)=
\{y\in K_D(x):\|\operatorname{Ad}(u)y-y\|\leq\varepsilon
\text{ for every }u\in F\}
\]
are nonempty and ultraweakly closed. Closedness follows because conjugation is normal and a closed norm ball is ultraweakly closed. They have the finite intersection property: use the union of the finitely many sets \(F\), the smallest \(\varepsilon\), and a sufficiently large \(n\) in (1.3). Compactness therefore gives a point fixed by all these conjugations. It commutes with all unitaries of \(D\), hence with \(D\), and lies in \(D'\cap M=D\).

Bimodularity gives \(P(uxu^*)=uP(x)u^*=P(x)\). Normality and linearity then give \(P(y)=P(x)\) for every \(y\in K_D(x)\). Any such \(y\) in \(D\) satisfies \(y=P(y)=P(x)\). This proves (1.2), including existence.

If \(Q\) is a second normal norm-one retraction onto \(D\), the same argument gives \(Q(y)=Q(x)\) on \(K_D(x)\). Since \(P(x)\in K_D(x)\cap D\), we get \(Q(x)=Q(P(x))=P(x)\). \(\square\)

Normality matters here: it passes the retraction through the ultraweak closure in (1.1). No separability or countable family of unitaries was assumed.

**Theorem 1.2.** If \(\tau\) is a faithful semifinite normal trace on \(M\), then its restriction \(\tau_D\) to \(D\) is semifinite, and
\[
\tau(x)=\tau_D(P(x))\qquad(x\in M_+).
\tag{1.4}
\]

**Proof.** By the finite-trace approximation criterion, choose projections \(e_i\uparrow1\) with \(\tau(e_i)<\infty\). For \(x\geq0\), normality and the trace identity give
\[
\tau(x)
=\sup_i\tau(x^{1/2}e_i x^{1/2})
=\sup_i\tau(e_i x e_i).
\tag{1.5}
\]
Each \(x\mapsto\tau(e_i x e_i)\) is a bounded normal positive functional; its norm is \(\tau(e_i)\). Thus (1.5) also explains the ultraweak lower semicontinuity furnished by the trace prerequisite.

For positive \(x\), every point of the convex orbit in (1.1) is positive and has trace \(\tau(x)\). If \(\tau(x)<\infty\), lower semicontinuity puts its entire ultraweak closure in \(\{y\geq0:\tau(y)\leq\tau(x)\}\). If \(\tau(x)=\infty\), that inequality is automatic. Since \(P(x)\in K_D(x)\), we obtain
\[
\tau(P(x))\leq\tau(x).
\tag{1.6}
\]
In particular \(b_i=P(e_i)\) are positive contractions with
\(\tau_D(b_i)<\infty\). Normality of \(P\) gives \(b_i\uparrow1\). The positive-contraction approximation criterion for semifiniteness, Proposition 2.5 of the trace prerequisite, now makes \(\tau_D\) semifinite. It is faithful and normal by restriction.

The existing trace-preserving expectation theorem applies at this point: Theorem 9.1 of *Traces, part B* gives a normal norm-one retraction \(P_\tau:M\to D\) with \(\tau=\tau_D P_\tau\) on the positive cone. Lemma 1.1 makes \(P_\tau=P\), proving (1.4). \(\square\)

The semifiniteness of the restriction was proved before using the trace-preserving expectation theorem. Assuming that restriction in advance would omit the main step.

## 2. Invariant coefficient traces and crossed-product traces

Let \(A\) be a nonzero abelian von Neumann algebra, \(G\) a countable discrete group, and \(\alpha:G\to\operatorname{Aut}(A)\) an action. Use the regular crossed product \(R=A\rtimes_\alpha G\), its coefficient representation \(\pi\), and its faithful normal expectation \(E:R\to A\) from the preceding lesson. Identifying \(A\) with \(\pi(A)\), its \(R\)-valued retraction is \(\pi E\).

A trace here is an additive, positively homogeneous map \(A_+\to[0,\infty]\). Normal means preservation of increasing suprema; semifinite has the usual finite-value approximation meaning. On an abelian algebra a normal weight is a trace. Invariant means
\[
\nu(\alpha_g(a))=\nu(a)\qquad(a\in A_+,\ g\in G).
\tag{2.1}
\]

**Proposition 2.1.** A faithful invariant semifinite normal trace \(\nu\) on \(A\) extends to the faithful semifinite normal trace
\[
\tau_\nu(x)=\nu(E(x)),\qquad x\in R_+.
\tag{2.2}
\]
It is finite exactly when \(\nu(1)<\infty\). If the action is free, every faithful semifinite normal trace on \(R\) arises in this way from its restriction to \(A\).

**Proof.** Additivity, homogeneity and normality of \(\nu E\) follow from positivity and normality of \(E\). It is faithful because both \(\nu\) and \(E\) are faithful. For the coefficient \(x_g=E(xu_g^*)\), the positive sums proved in the preceding lesson are
\[
E(xx^*)=\sum_{g\in G}x_gx_g^*,\qquad
E(x^*x)=\sum_{g\in G}\alpha_{g^{-1}}(x_g^*x_g).
\tag{2.3}
\]
Both are increasing limits of finite sums. Normality, invariance and commutativity of \(A\) give
\[
\begin{aligned}
\tau_\nu(x^*x)
&=\sum_g\nu(\alpha_{g^{-1}}(x_g^*x_g))\\
&=\sum_g\nu(x_g^*x_g)
=\sum_g\nu(x_gx_g^*)
=\tau_\nu(xx^*).
\end{aligned}
\tag{2.4}
\]
The equality is valid with infinite values; no subtraction of infinite quantities occurs. This is the trace identity.

Choose finite-\(\nu\) projections \(f_i\uparrow1\) in \(A\). Then
\(\pi(f_i)\uparrow1\) in \(R\) and
\(\tau_\nu(\pi(f_i))=\nu(f_i)<\infty\). The trace approximation criterion makes \(\tau_\nu\) semifinite. Also \(\tau_\nu(1)=\nu(1)\).

Conversely, suppose the action is free and \(\tau\) is faithful, semifinite and normal on \(R\). The coefficient algebra is maximal abelian. Apply Theorem 1.2 to \(\pi E\). It gives a faithful semifinite normal trace
\(\nu(a)=\tau(\pi(a))\) and \(\tau=\nu E\). Covariance and unitary invariance of a trace give
\[
\nu(\alpha_g(a))
=\tau(u_g\pi(a)u_g^*)
=\tau(\pi(a))
=\nu(a).
\]
Thus \(\nu\) is invariant. \(\square\)

## 3. Ergodicity and the four type criteria

The action is *ergodic* when \(A^\alpha=\mathbb C1\).

**Lemma 3.1.** For an ergodic action, every nonzero invariant semifinite normal trace on \(A\) is faithful. Any two such traces are positive scalar multiples of one another.

**Proof.** The support \(s(\nu)\) of an invariant normal trace is invariant: an automorphism takes its largest zero projection to another zero projection, and invariance gives equality. Ergodicity makes \(s(\nu)\) either \(0\) or \(1\). Since \(\nu\ne0\), it is \(1\), which means faithfulness.

Let \(\nu,\mu\) be two nonzero invariant semifinite normal traces. The bounded density comparison theorem, Theorem 7.2 of *Traces, part B*, applies to these faithful traces. It states that \(\rho=\nu+\mu\) is faithful, semifinite and normal, and there is a unique \(h\in A\), \(0\leq h\leq1\), such that
\[
\nu(a)=\rho(ha),\qquad
\mu(a)=\rho((1-h)a)\qquad(a\in A_+),
\tag{3.1}
\]
with \(s(h)=s(1-h)=1\).

Invariance of \(\rho\) and \(\nu\) gives, for every \(g\),
\[
\rho(\alpha_g(h)a)
=\rho(h\alpha_{g^{-1}}(a))
=\nu(\alpha_{g^{-1}}(a))
=\nu(a).
\]
The analogous identity holds for \(\mu\). Uniqueness in the comparison theorem therefore gives \(\alpha_g(h)=h\). Ergodicity yields \(h=t1\). Its two support assertions give \(0<t<1\). Equation (3.1) now implies
\(\nu=t\rho\), \(\mu=(1-t)\rho\), and
\(\mu=(1-t)t^{-1}\nu\). \(\square\)

**Theorem 3.2.** Suppose \(G\) is countably infinite and \(\alpha\) is free and ergodic. Then \(R=A\rtimes_\alpha G\) is an infinite-dimensional factor, with the following alternatives.

1. \(R\) is type I exactly when \(A\) contains a minimal projection \(p\) whose translates satisfy
   \[
   \sum_{g\in G}\alpha_g(p)=1.
   \tag{3.2}
   \]
   In this case \(A\) is atomic and \(R\) is type I\(_\infty\).
2. \(R\) is type II\(_1\) exactly when \(A\) has a faithful finite invariant normal trace.
3. \(R\) is type II\(_\infty\) exactly when \(A\) is nonatomic and has a faithful invariant semifinite normal trace \(\nu\) with \(\nu(1)=\infty\).
4. \(R\) is type III exactly when \(A\) has no nonzero invariant semifinite normal trace.

Here nonatomic means that \(A\) has no minimal projection. Under ergodicity, existence of even one minimal projection gives (3.2), so the atomic and nonatomic alternatives exhaust this situation.

**Proof.** Freeness and ergodicity give factoriality by the preceding lesson. The unitaries \(u_g\) are linearly independent: applying \(E(\,\cdot\,u_h^*)\) to a finite relation selects its coefficient at \(h\). Since \(G\) is infinite, \(R\) is infinite-dimensional.

*The atomic alternative.* Let \(p\) be a minimal projection of \(A\). If \(\alpha_g(p)=p\), the restriction of \(\alpha_g\) to \(Ap=\mathbb Cp\) is the identity, so for every \(a\in A\)
\[
\alpha_g(a)p=\alpha_g(ap)=ap.
\]
For \(g\ne e\) this contradicts freeness. The minimal projections \(\alpha_g(p)\) are therefore all distinct, and distinct minimal projections in an abelian algebra are orthogonal. Their sum is a nonzero invariant projection, hence is \(1\). In particular \(A\) is atomic with these atoms.

The projection \(\pi(p)\) is minimal in \(R\). Indeed, for \(y\in\pi(p)R\pi(p)\), every \(a\in A\) is scalar on \(p\), so \(y\) commutes with \(\pi(A)\). Maximal abelianness puts \(y\) in \(\pi(A)\), and then in \(\mathbb C\pi(p)\). A factor with a nonzero minimal projection is type I by the type-I classification prerequisite. Infinite dimension excludes finite matrix factors, and gives type I\(_\infty\). One can also see the countable matrix units directly:
\[
v_g=u_g\pi(p),\qquad
v_g^*v_g=\pi(p),\qquad
v_gv_g^*=\pi(\alpha_g(p)),\qquad
e_{g,h}=v_gv_h^*.
\tag{3.3}
\]
The orthogonality in (3.2) makes \(e_{g,h}e_{k,l}=\delta_{h,k}e_{g,l}\), and their diagonal sum is \(1\). The usual minimal-corner matrix-unit decomposition identifies \(R\) with \(B(\ell^2(G))\).

Conversely, suppose \(R\) is type I, and identify it normally with \(B(L)\). Its canonical operator trace is faithful, semifinite and normal. Theorem 1.2 makes its restriction to the coefficient maximal abelian algebra semifinite. There is therefore a nonzero \(a\in A_+\) with finite operator trace. For some \(\varepsilon>0\), its spectral projection \(q=1_{[\varepsilon,\infty)}(a)\) is nonzero, and
\[
\operatorname{Tr}(q)\leq\varepsilon^{-1}\operatorname{Tr}(a)<\infty.
\]
Thus \(q\) is finite rank in \(B(L)\). The nonzero abelian algebra \(qAq\subseteq B(qL)\) is finite-dimensional and has a minimal projection \(p\). It is minimal in \(A\) too, because any subprojection of \(p\) in \(A\) already lies in \(qAq\). The previous orbit argument gives (3.2). This proves the first alternative and the asserted atomic dichotomy.

*Finite traces.* A faithful finite invariant normal trace \(\nu\) gives the faithful finite normal trace \(\nu E\) on \(R\). Thus \(R\) is finite. A finite type-I factor is a finite matrix algebra, whereas \(R\) is infinite-dimensional. Hence \(R\) is type II\(_1\). Conversely a type-II\(_1\) factor has its faithful normal finite trace, obtained from the centre-valued trace of a finite algebra. Proposition 2.1 restricts it to the required invariant trace on \(A\). This proves the second alternative.

*Infinite semifinite traces.* Suppose \(A\) is nonatomic and \(\nu\) is faithful, invariant, normal and semifinite with \(\nu(1)=\infty\). The trace \(\nu E\) makes \(R\) semifinite. The first alternative excludes type I. If \(R\) were finite, the second alternative would give a finite invariant normal trace \(\mu\) on \(A\). Lemma 3.1 would make \(\nu\) a finite positive multiple of \(\mu\), contrary to \(\nu(1)=\infty\). The type decomposition for factors therefore makes \(R\) type II\(_\infty\).

Conversely a type-II\(_\infty\) factor has a faithful semifinite normal trace by Theorem 6.7 of *Traces, part A*. Its value at \(1\) is infinite: a faithful finite trace would make the factor finite. Proposition 2.1 gives the invariant restricted trace \(\nu\), with \(\nu(1)=\infty\); the first alternative makes \(A\) nonatomic. This proves the third alternative.

*Type III.* A factor is type III exactly when it is not semifinite. If \(A\) has a nonzero invariant semifinite normal trace, Lemma 3.1 makes it faithful and Proposition 2.1 makes \(R\) semifinite. Conversely if \(R\) is semifinite, the trace existence theorem and Proposition 2.1 supply such an invariant trace on \(A\). This proves the fourth alternative. \(\square\)

The infinite-group hypothesis excludes finite matrix factors from the finite-trace alternative. For example the free transitive action of a group of order \(n\) on \(n\) atoms gives \(M_n(\mathbb C)\), with a finite invariant coefficient trace.

## 4. Rational translations

We establish ergodicity and freeness explicitly for the examples.

**Lemma 4.1.** On either \(\mathbb R\) with Lebesgue measure or \(\mathbb T=\mathbb R/\mathbb Z\) with normalized Lebesgue measure, a function in \(L^\infty\) fixed by all rational translations is constant almost everywhere.

**Proof.** Translation is continuous in the \(L^1\) norm. For an indicator of a bounded interval on \(\mathbb R\), the norm difference from a translate is at most twice the translation distance. Arc indicators give the same conclusion on \(\mathbb T\). Finite linear combinations have the property, and their density in \(L^1\), together with the isometric nature of translation, proves it for every \(L^1\) function.

For \(f\in L^\infty\), this makes translation ultraweakly continuous: pairing a translated \(f\) against \(h\in L^1\) is pairing \(f\) against the oppositely translated \(h\). If all rational translations fix \(f\), density of \(\mathbb Q\) in \(\mathbb R\), or of \(\mathbb Q/\mathbb Z\) in \(\mathbb T\), shows that every translation fixes \(f\).

Choose a measurable bounded representative. For each translation \(t\), \(f(x-t)=f(x)\) for almost every \(x\). Fubini, on bounded rectangles and then their countable union in the real case, gives this equality for almost every pair \((t,x)\). The change of variables \((t,x)\mapsto(x-t,x)\) preserves product Lebesgue measure (and product normalized Lebesgue measure on the circle). Hence \(f(y)=f(x)\) for almost every pair \((y,x)\). Fubini once more, with any \(x\) from the conull set of good sections, makes \(f\) constant almost everywhere. \(\square\)

**Lemma 4.2.** Let \(T\) be an invertible nonsingular Borel transformation of \(\mathbb R\) or \(\mathbb T\), and let \(\beta(f)=f\circ T^{-1}\). If the fixed-point set of \(T\) has measure zero, then \(\beta\) is free on \(L^\infty\).

**Proof.** Suppose a nonzero projection \(p=1_S\) supported an identity part, so
\((\beta(f)-f)1_S=0\) for all \(f\). Apply this to indicators from a countable Borel family separating points, for example rational open intervals or rational arcs. Outside the union of the resulting countably many null exceptional sets, membership of \(x\) and \(T^{-1}x\) in every member of that family agrees for \(x\in S\). The separating property gives \(T^{-1}x=x\). Thus \(S\) is contained, modulo a null set, in the fixed-point set. It is null, contradicting \(p\ne0\). \(\square\)

**Example 4.3: a type-II\(_1\) factor from circle translations.** Let
\[
A=L^\infty(\mathbb T),\qquad G=\mathbb Q/\mathbb Z,\qquad
\alpha_q(f)(x)=f(x-q).
\]
Every nonidentity translation has no fixed point, so Lemma 4.2 gives freeness. Lemma 4.1 gives ergodicity. The coefficient algebra is nonatomic, and
\[
\nu(f)=\int_{\mathbb T}f(x)\,dx,\qquad f\geq0,
\]
is faithful, invariant, normal and finite. Theorem 3.2 gives a type-II\(_1\) factor. Its normalized trace is \(x\mapsto\int_{\mathbb T}E(x)\,dx\).

**Example 4.4: a type-II\(_\infty\) factor from real translations.** Let
\[
A=L^\infty(\mathbb R),\qquad G=\mathbb Q,\qquad
\alpha_q(f)(x)=f(x-q).
\]
The same two lemmas give freeness and ergodicity. Lebesgue integration
\[
\nu(f)=\int_{\mathbb R}f(x)\,dx
\]
is faithful, invariant and normal, with \(\nu(1)=\infty\). It is semifinite because the projections \(1_{[-n,n]}\uparrow1\) have finite trace. The coefficient algebra is nonatomic. Theorem 3.2 gives type II\(_\infty\).

## 5. A dilation produces type III

**Example 5.1.** Let \(G\) be the countable group of affine transformations
\[
T_{b,n}(x)=2^n x+b,\qquad b\in\mathbb Q,\ n\in\mathbb Z.
\tag{5.1}
\]
Composition and inversion are
\[
T_{b,n}T_{c,m}=T_{b+2^n c,n+m},\qquad
T_{b,n}^{-1}=T_{-2^{-n}b,-n}.
\tag{5.2}
\]
Thus the displayed transformations form a group, with identity \(T_{0,0}\). They are distinct for distinct pairs \((b,n)\).

On \(A=L^\infty(\mathbb R)\) set
\[
\alpha_{b,n}(f)(x)=f(2^{-n}(x-b)).
\tag{5.3}
\]
The transformations and their inverses preserve null sets, so these formulas give normal automorphisms of the measure algebra and define the required action. To see normality also from the predual, a change of variables pairs (5.3) with the \(L^1\) function \(t\mapsto2^n h(2^n t+b)\).

A nonidentity translation has no fixed point. A transformation with \(n\ne0\) has exactly one fixed point, \(b/(1-2^n)\). Each nonidentity element therefore has a null fixed-point set. Lemma 4.2 gives freeness. The rational-translation subgroup is already ergodic by Lemma 4.1, so the full action is ergodic.

Suppose \(\eta\ne0\) were an invariant semifinite normal trace on \(A\) for this full group. It is invariant under the rational translations. Lebesgue integration \(\nu\) is also invariant, faithful, semifinite and normal for that subgroup. Apply Lemma 3.1 to the ergodic rational-translation action: it gives \(\eta=c\nu\) for a finite scalar \(c>0\).

But the dilation \(d=T_{0,1}\) obeys
\[
\nu(\alpha_d(f))
=\int_{\mathbb R}f(x/2)\,dx
=2\int_{\mathbb R}f(x)\,dx
=2\nu(f).
\tag{5.4}
\]
For \(f=1_{[0,1]}\), the values are finite and unequal. Thus \(c\nu\) is not dilation invariant. This contradicts the assumption on \(\eta\). There is no nonzero invariant semifinite normal trace, and Theorem 3.2 makes
\[
L^\infty(\mathbb R)\rtimes G
\]
a type-III factor.

The uniqueness lemma applies to the translation subgroup before the dilation is added. This avoids an assumption that an arbitrary invariant trace must first be presented by a measurable density.

**Corollary 5.2.** Factors of types I, II\(_1\), II\(_\infty\) and III exist in faithful representations on separable Hilbert spaces.

**Proof.** The atomic shift example in Exercise 6.3 of the preceding lesson gives \(B(\ell^2(\mathbb Z))\), type I\(_\infty\); finite matrix factors give the finite type-I cases. Examples 4.3, 4.4 and 5.1 supply the other three types. In each new example the multiplication space \(H=L^2(\mathbb T)\) or \(L^2(\mathbb R)\) is separable, and \(G\) is countable. The regular representation is therefore on the separable Hilbert space \(H\otimes\ell^2(G)\). \(\square\)

## 6. Graded exercises with complete solutions

**Exercise 6.1 (introductory: a faithful state need not give a trace).** In \(M_3(\mathbb C)\), let \(D\) be the diagonal algebra and let \(P(x)\) be the diagonal of \(x\). Put
\[
\nu(\operatorname{diag}(a_1,a_2,a_3))
=\frac{a_1+2a_2+4a_3}{7}.
\]
Show that \(\nu P\) is a faithful normal state but is not a trace. Determine exactly which positive diagonal weights give a trace, and relate the answer to invariance under cyclic permutation of the atoms.

*Solution.* \(P(x)=\sum_{j=1}^3 e_{jj}xe_{jj}\) is unital and completely positive. Thus \(\nu P\) is a positive state; it is normal in this finite-dimensional algebra. If \(x\geq0\) and \(\nu P(x)=0\), all three diagonal entries are zero, because their weights are strictly positive. Then
\(\|x^{1/2}e_j\|^2=x_{jj}=0\) for every standard basis vector, so \(x=0\). This proves faithfulness.

For \(y=e_{12}\),
\[
(\nu P)(y^*y)=(\nu P)(e_{22})=\frac27,\qquad
(\nu P)(yy^*)=(\nu P)(e_{11})=\frac17.
\]
The trace identity fails. More generally, with strictly positive weights \(w_j\) of sum \(1\), testing \(e_{ij}\) gives \(w_i=w_j\) as a necessary condition for a trace. It is sufficient: equal weights give \(3^{-1}\operatorname{Tr}\). Invariance under a cyclic permutation of the three atoms is exactly \(w_1=w_2=w_3\). Thus it is invariance, in addition to faithfulness and normality, that is missing in the displayed example.

**Exercise 6.2 (intermediate: the absolute dilation factor).** For
\(\lambda=-3/2\) and \(\lambda=-1\), let \(G_\lambda\) be the group of actual transformations
\[
x\longmapsto\lambda^n x+b,\qquad b\in\mathbb Q,\ n\in\mathbb Z,
\]
and let it act by inverse composition on \(L^\infty(\mathbb R)\).
Prove freeness and ergodicity in both cases. Determine the crossed-product type. Explain why for \(\lambda=-1\) one must identify exponents with the same transformation.

*Solution.* Since \(\lambda,\lambda^{-1}\) are rational, composition and inversion preserve the displayed set of affine transformations. The group is countable and contains all rational translations. Hence the action is ergodic by Lemma 4.1.

Every nonidentity transformation with slope \(1\) is a nonzero translation and has no fixed point. Every transformation with slope different from \(1\) has one fixed point. Thus all nonidentity fixed-point sets are null, and Lemma 4.2 proves freeness.

Change of variables gives, for \(f\geq0\),
\[
\int_{\mathbb R}f(x/\lambda)\,dx
=|\lambda|\int_{\mathbb R}f(x)\,dx.
\]
For \(\lambda=-3/2\), any invariant nonzero semifinite normal trace would, by uniqueness for the rational-translation subgroup, be \(c\nu\) with \(c>0\). The transformation of slope \(-3/2\) multiplies its value on an interval indicator by \(3/2\), contradicting invariance. The factor is type III.

For \(\lambda=-1\), every transformation has slope \(1\) or \(-1\) and preserves Lebesgue measure. Integration is faithful, invariant, semifinite and normal with infinite value at \(1\). Since \(L^\infty(\mathbb R)\) is nonatomic, the factor is type II\(_\infty\).

For \(\lambda=-1\), exponents differing by \(2\) give the same slope. The actual group is \(\mathbb Q\rtimes\{1,-1\}\). Keeping the redundant abstract exponent group \(\mathbb Z\) would give nonidentity elements acting identically, so that action would fail freeness. The exercise's definition as a group of transformations removes this kernel.

**Exercise 6.3 (advanced: why ergodicity is necessary for uniqueness).** Let \(\mathbb Z\) act on \(A=L^\infty(\mathbb R)\) by integer translations. Show that the action is free but not ergodic. Construct two invariant faithful semifinite normal traces which are not proportional, extend them to the crossed product, and exhibit a nonconstant central element of that crossed product.

*Solution.* Every nonidentity integer translation has no fixed point, so Lemma 4.2 gives freeness. The bounded nonconstant function \(\sin(2\pi x)\) is invariant under every integer translation; the action is therefore not ergodic.

For \(f\in A_+\), set
\[
\nu_1(f)=\int_{\mathbb R}f(x)\,dx,\qquad
\nu_2(f)=\int_{\mathbb R}(2+\sin(2\pi x))f(x)\,dx.
\]
The density in the second formula is between \(1\) and \(3\). Both traces are faithful and normal, and both are finite on \(1_{[-n,n]}\), which increase to \(1\); hence both are semifinite. Periodicity makes \(\nu_2\) invariant, and translation invariance makes \(\nu_1\) invariant.

They are not proportional. Indeed,
\[
\nu_1(1_{[0,1/2]})=\nu_1(1_{[1/2,1]})=\frac12,
\]
whereas
\[
\nu_2(1_{[0,1/2]})=1+\frac1\pi,\qquad
\nu_2(1_{[1/2,1]})=1-\frac1\pi.
\]
Proposition 2.1 extends them to faithful semifinite normal traces
\(\tau_j=\nu_j E\). The extensions cannot be proportional because their restrictions to \(\pi(A)\) are not.

Finally \(\pi(\sin(2\pi x))\) commutes with \(\pi(A)\) by commutativity and with every \(u_n\) by invariance. It is a nonconstant central element. Equivalently the centre formula for this free action gives \(Z(R)=\pi(A^\alpha)\). This explains why the factorial and proportionality conclusions required ergodicity.

## References

[Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer-Verlag, 1979.

[Anantharaman–Popa] Claire Anantharaman and Sorin Popa, [An introduction to II1 factors](https://www.math.ucla.edu/~popa/Books/IIunV15.pdf), author-hosted draft IIunV15.

[Trace prerequisites] *Traces on von Neumann algebras*, parts A and B, and the other programme lessons linked above, with their specific proof locators.
