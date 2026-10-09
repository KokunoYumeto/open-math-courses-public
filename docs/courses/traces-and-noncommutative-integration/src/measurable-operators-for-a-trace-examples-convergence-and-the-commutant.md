# Measurable operators for a trace: examples, convergence and the commutant

*Written by Claude Opus 5.5 (Anthropic), September 2026, extended October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October additions (Theorem 8.7, the joint distribution in Section 10, Sections 14 and 15) and the October revision of the references are self-checked by the writing AI. Public domain (CC0).*

This lesson continues the theory of operators that are measurable with respect to a faithful normal semifinite trace \(\tau\) on a von Neumann algebra \(M\). The lessons Operators recovered from small trace defects and Trace densities and noncommutative integration construct the algebra \(S(M,\tau)\) of \(\tau\)-measurable operators, its measure topology and the spaces \(L^p(M,\tau)\). We assume them. Section 2 states in full every result from them that we use, together with the standard facts from operator algebras and measure theory that we need, and the place where each is proved.

The first half of the lesson is about the measure topology. Section 3 works out the commutative case, where measurable operators are functions and the measure topology is convergence in measure. Sections 4 and 5 show that minimal projections decide two extreme cases: every measurable operator is bounded exactly when the traces of nonzero projections are bounded away from zero, and every affiliated operator is measurable exactly when \(\tau(1)<\infty\). Section 6 shows that on a diffuse algebra few linear functionals are continuous in measure. Sections 7 and 8 study convergence nearly everywhere, a noncommutative form of almost everywhere convergence, and compare it with convergence in measure; Theorem 8.7 decides exactly when convergence in measure implies convergence nearly everywhere.

The second half is about integration. Section 9 treats generalized singular values. Section 10 proves an estimate for the spectral projections of two elements of \(L^2\): when two positive elements are close, their spectral projections are close on average. It then builds the joint distribution of one element acting on the left and another acting on the right, which gives a second proof. Section 11 shows that the commutant of left multiplication on \(L^2\) consists of the right multiplications. Sections 12 and 13 use this to build a trace on the commutant of any normal representation, and to turn the vectors of the representation into square-integrable intertwiners. Section 14 extends isomorphisms that scale the trace to measurable operators and to the spaces \(L^p\). Section 15 identifies the measurable operators and \(L^2\) of \(M_2(M)\) with \(2\times2\) matrices, and proves the estimate of Section 10 for arbitrary elements of \(L^2\) and their polar decompositions.

Basic references are [Nelson 1974], [Fack–Kosaki 1986] and [Hiai 2021, Section 4]; an open survey is [Kostecki 2014]. Operators measurable with respect to a trace go back to Segal. The stronger notion used here goes back to Stinespring and Nelson, and the approach through the measure topology is Nelson's. Generalized singular values were developed by Fack and Kosaki.

## 1. Setting and notation

Throughout, \(M\subseteq B(H)\) is a von Neumann algebra on a complex Hilbert space \(H\), and \(\tau\) is a faithful normal semifinite trace on \(M\). We assume nothing about the size of \(H\), about \(\sigma\)-finiteness, or about \(\tau(1)\), unless a statement says so. Inner products are linear in the first variable. For a projection \(e\) we write \(e^\perp=1-e\). \(\operatorname{Proj}(M)\) is the set of projections of \(M\), and \(\mathcal E\) is the set of projections of finite trace. Two projections are *equivalent*, \(e\sim f\), when \(e=v^*v\) and \(f=vv^*\) for a partial isometry \(v\in M\). We write \(e\precsim f\) when \(e\) is equivalent to a subprojection of \(f\).

A *minimal projection* is a nonzero projection \(e\in M\) whose only subprojections in \(M\) are \(0\) and \(e\). We call \(M\) *diffuse* when it has no minimal projection; such algebras are also called non-atomic. We put
\[
c(\tau)=\inf\{\tau(p):\ p\in\operatorname{Proj}(M),\ p\neq0\},
\]
with \(c(\tau)=+\infty\) when \(M=0\).

A *factor* is a von Neumann algebra \(M\) with \(M\cap M'=\mathbb C1\). A projection \(e\) is *abelian* when \(eMe\) is abelian. The algebra \(M\) is *of type I* when every nonzero central projection majorizes a nonzero abelian projection. So a factor is of type I exactly when it has a nonzero abelian projection.

A closed, densely defined operator \(T\) on \(H\) is *affiliated* with \(M\) when every unitary \(u\in M'\) satisfies \(uD(T)=D(T)\) and \(Tu\xi=uT\xi\) for \(\xi\in D(T)\).

We use the following objects from the prerequisite lessons.

- *Measure topologies.* For \(r,d>0\), \(U(r,d)\) is the set of \(x\in M\) with \(\|xp\|<r\) and \(\tau(1-p)<d\) for some \(p\in\operatorname{Proj}(M)\), and \(V(r,d)\) is the set of \(\xi\in H\) with \(\|p\xi\|<r\) and \(\tau(1-p)<d\) for some such \(p\). Such a \(p\) is called a *witness*. These sets are the basic neighbourhoods of \(0\) for the measure topologies on \(M\) and on \(H\).
- *Measurable operators.* \(S(M,\tau)\) is the algebra of \(\tau\)-measurable operators. We identify it with the completion \(\widehat M\) of \(M\) in the measure topology, and \(\widehat H\) is the completion of \(H\). The elements of \(S(M,\tau)\) are closed, densely defined operators affiliated with \(M\); for \(a\in\widehat M\), \(T_a\) denotes the corresponding operator (Fact 2.3). A sum or product in \(S(M,\tau)\) is the closure of the ordinary sum or product. We write \(x\le y\) when \(y-x\in S(M,\tau)_+\).
- \(\widetilde U(r,d)\) is the set of \(x\in S(M,\tau)\) for which some projection \(e\) has \(eH\subseteq D(x)\), \(\|xe\|<r\) and \(\tau(1-e)<d\).
- *Trace ideals.* \(\mathfrak n_\tau=\{x\in M:\tau(x^*x)<\infty\}\), and \(\mathfrak m_\tau\) is the linear span of \(\mathfrak n_\tau^*\mathfrak n_\tau\). \(\mathfrak m_0\) is the ideal of bounded operators whose right support (equivalently, left support) has finite trace.
- *\(L^p\) spaces.* For \(1\le p<\infty\), \(L^p(M,\tau)\) is the set of \(x\in S(M,\tau)\) with \(\|x\|_p=\tau(|x|^p)^{1/p}<\infty\). The trace extends to a linear functional on \(L^1\). On \(L^2=L^2(M,\tau)\) the inner product is \(\langle x,y\rangle_2=\tau(y^*x)\). For \(a\in M\) we write \(L_ax=ax\) and \(R_ax=xa\).
- *Distribution and singular values.* For \(x\in S(M,\tau)\), \(s\ge0\) and \(t>0\), put \(d_x(s)=\tau(1_{(s,\infty)}(|x|))\) and \(\mu_t(x)=\inf\{\|xe\|:\ e\in\operatorname{Proj}(M),\ eH\subseteq D(x),\ \tau(1-e)\le t\}\). The product \(xe\) here is bounded because \(eH\subseteq D(x)\) (Fact 2.3(a)).

## 2. Results used from other lessons

Facts 2.1–2.6 are proved in the lessons Operators recovered from small trace defects (its sections MT-02 to MT-13) and Trace densities and noncommutative integration (its sections TI-02 to TI-15). Fact 2.7 names the lessons that prove its statements. Other treatments are [Hiai 2021, Section 4] for Facts 2.1–2.4 and 2.6, and [Fack–Kosaki 1986] for Fact 2.5.

**Fact 2.1** (Projections and the trace). Let \(e,f,e_j,f_j,p_n\) be projections of \(M\).

- (a) If \(e\precsim f\), then \(\tau(e)\le\tau(f)\), and equivalent projections have equal trace. The left and right supports of an element of \(M\), or of a closed, densely defined operator affiliated with \(M\), are equivalent through its polar decomposition.
- (b) \(\tau(e\vee f)\le\tau(e)+\tau(f)\). If \(e\wedge f=0\), then \(e\precsim1-f\).
- (c) (Countable subadditivity.) For a countable family, \(\tau(1-\bigwedge_je_j)\le\sum_j\tau(1-e_j)\); equivalently, \(\tau(\bigvee_jf_j)\le\sum_j\tau(f_j)\).
- (d) If \(p_1\le p_2\le\dots\) and \(\tau(1-p_n)\to0\), then \(p_n\uparrow1\) strongly.
- (e) (Semifiniteness.) Every projection \(P\) is the supremum of the projections of finite trace below it, and \(\tau(P)=\sup\{\tau(e):e\in\mathcal E,\ e\le P\}\). By (b), \(\mathcal E\) is directed upward, and \(e\uparrow1\) strongly along \(\mathcal E\).

**Fact 2.2** (The measure topology).

- (a) For all positive parameters,
\[
\begin{aligned}
U(r,d)^*&=U(r,d),\\
U(r_1,d_1)+U(r_2,d_2)&\subseteq U(r_1+r_2,d_1+d_2),\\
U(r_1,d_1)U(r_2,d_2)&\subseteq U(r_1r_2,d_1+d_2),\\
V(r_1,d_1)+V(r_2,d_2)&\subseteq V(r_1+r_2,d_1+d_2),\\
U(r_1,d_1)V(r_2,d_2)&\subseteq V(r_1r_2,d_1+d_2).
\end{aligned}
\]
- (b) The translates of the sets \(U(r,d)\) and \(V(r,d)\) are the neighbourhoods of translation-invariant Hausdorff uniformities on \(M\) and on \(H\). Each \(U(r,d)\) and each \(V(r,d)\) contains the open norm ball of radius \(r\), so norm convergence implies convergence in measure. A set \(S\) is *bounded in measure* when for every \(d>0\) there is \(R\) with \(S\subseteq U(R,d)\) (or \(S\subseteq V(R,d)\)). Cauchy sequences are bounded in measure. Addition and the involution are uniformly continuous, and multiplication and the action of \(M\) on \(H\) are uniformly continuous on products of sets bounded in measure.
- (c) The operations extend to the completions. \(\widehat M\) is a complete topological \(*\)-algebra that acts on \(\widehat H\), with the same continuity properties, and \(M\) and \(H\) are dense in \(\widehat M\) and \(\widehat H\).
- (d) (Cutoffs.) For every \(a\in\widehat M\) there are projections \(p_1\le p_2\le\dots\) with \(\tau(1-p_n)\to0\) and \(ap_n\in M\). Whenever \(\tau(1-p_n)\to0\), \(p_n\to1\) in measure, and so \(ap_n\to a\) in measure.

**Fact 2.3** (Measurable operators).

- (a) (Bounded pieces.) If \(T\) is closed and affiliated with \(M\), \(e\in\operatorname{Proj}(M)\) and \(eH\subseteq D(T)\), then \(Te\in M\). The proof uses the closed graph theorem.
- (b) (Graph uniqueness.) Let \(S\) and \(T\) be closed, densely defined and affiliated with \(M\). Suppose that for every \(d>0\) some projection \(p\) has \(\tau(1-p)<d\), \(pH\subseteq D(S)\cap D(T)\) and \(Sp=Tp\). Then \(S=T\).
- (c) (Realization.) For \(a\in\widehat M\), let \(D(T_a)\) be the set of \(\xi\in H\) for which the vector \(a\xi\in\widehat H\) lies in \(H\), and put \(T_a\xi=a\xi\). Then \(T_a\) is closed, densely defined and affiliated with \(M\), and it has no proper closed extension affiliated with \(M\). The map \(a\mapsto T_a\) is injective, \(T_a=a\) for \(a\in M\), and its image is \(S(M,\tau)\).
- (d) (Operations.) \(T_{a^*}=T_a^*\), \(T_{a+b}=\overline{T_a+T_b}\) and \(T_{ab}=\overline{T_aT_b}\); the ordinary sum and product are densely defined and closable. If \(T\) is closed and \(e\) is a bounded projection, the ordinary product \(Te\), with domain \(\{\xi:e\xi\in D(T)\}\), is closed. If moreover \(T\in S(M,\tau)\) and \(e\in M\), this product is densely defined and equals the product in \(S(M,\tau)\).
- (e) (Increasing domains.) Let \(p_1\le p_2\le\dots\) be projections with \(\tau(1-p_n)\to0\), and let \(A\) be a linear operator on \(\bigcup_np_nH\) with \(Ap_n\in M\) for every \(n\). Then \(A\) is closable, and \(\overline A=T_a\) for a unique \(a\in\widehat M\).
- (f) (The spectral-tail criterion.) For a closed, densely defined operator \(T\) affiliated with \(M\), with \(h=|T|\), the following are equivalent: (1) \(T\in S(M,\tau)\); (2) for every \(d>0\) some projection \(p\) has \(\tau(1-p)<d\) and \(pH\subseteq D(T)\); (3) \(\tau(1_{(R,\infty)}(h))\to0\) as \(R\to\infty\); (4) \(\tau(1_{(R_0,\infty)}(h))<\infty\) for some \(R_0\ge0\).
- (g) (Positivity.) The positive elements of \(S(M,\tau)\) are the elements \(b^*b\), and also the elements \(a\) for which \(T_a\) is positive self-adjoint. Every positive element has a unique positive square root. Every \(a\in S(M,\tau)\) has a polar decomposition \(a=v|a|\) with \(|a|=(a^*a)^{1/2}\) and \(v\in M\) a partial isometry.

**Fact 2.4** (The trace on measurable operators).

- (a) For \(h\in S(M,\tau)_+\) with spectral measure \(E_h\), \(B\mapsto\tau(E_h(B))\) is a countably additive measure on the Borel sets of \([0,\infty)\), and the trace \(\tau(h)\in[0,\infty]\) is
\[
\tau(h)=\int_{[0,\infty)}t\,d(\tau\circ E_h)(t)=\int_0^\infty\tau\bigl(1_{(s,\infty)}(h)\bigr)\,ds.
\]
- (b) On \(S(M,\tau)_+\) the trace is additive and positively homogeneous, and \(\tau(x^*x)=\tau(xx^*)\) for every \(x\in S(M,\tau)\). If \(0\le a\le b\) in \(S(M,\tau)\), then \(\tau(1_{(s,\infty)}(a))\le\tau(1_{(s,\infty)}(b))\) for every \(s>0\).
- (c) \(\mathfrak n_\tau\) and \(\mathfrak m_\tau\) are two-sided ideals of \(M\), and \(\mathfrak n_\tau^*=\mathfrak n_\tau\). The trace extends to a linear functional on \(\mathfrak m_\tau\), and it is cyclic: \(\tau(xy)=\tau(yx)\) for \(x,y\in\mathfrak n_\tau\), and \(\tau(ab)=\tau(ba)\) for \(a\in\mathfrak m_\tau\) and \(b\in M\). The set \(\mathfrak m_0\) is a two-sided \(*\)-ideal, contained in \(\mathfrak m_\tau\) and in every \(L^p(M,\tau)\).

**Fact 2.5** (Distribution and singular values). Let \(x\in S(M,\tau)\).

- (a) \(\mu_t(x)=\inf\{s\ge0:d_x(s)\le t\}\), and \(\mu_t(x)\le s\) exactly when \(d_x(s)\le t\). The infimum defining \(\mu_t(x)\) is attained by the spectral projection \(1_{[0,\mu_t(x)]}(|x|)\).
- (b) (The layer-cake formula.) For \(0<p<\infty\), \(\tau(|x|^p)=\int_0^\infty ps^{p-1}d_x(s)\,ds=\int_0^\infty\mu_t(x)^p\,dt\).
- (c) \(|x|\) and \(|x^*|\) have the same spectral distribution on \((0,\infty)\): \(\tau(1_B(|x|))=\tau(1_B(|x^*|))\) for every Borel set \(B\subseteq(0,\infty)\).
- (d) (The Markov estimate.) \(s^pd_x(s)\le\tau(|x|^p)\) for \(s>0\), and \(\mu_t(x)\le t^{-1/p}\tau(|x|^p)^{1/p}\).
- (e) The sets \(\widetilde U(r,d)\) form a base of neighbourhoods of \(0\) in \(S(M,\tau)\). A net \((x_i)\) tends to \(0\) in measure exactly when \(\mu_t(x_i)\to0\) for every \(t>0\).

**Fact 2.6** (\(L^p\) spaces and the Hilbert space \(L^2\)).

- (a) For \(1\le p<\infty\), \(L^p(M,\tau)\) is a Banach space, \(\mathfrak m_0\) is dense in it, \(\|x^*\|_p=\|x\|_p\), and \(\|axb\|_p\le\|a\|\,\|x\|_p\,\|b\|\) for \(a,b\in M\). Convergence in \(L^p\) implies convergence in measure.
- (b) The trace extends to a continuous linear functional on \(L^1\), with \(\tau(ax)=\tau(xa)\) for \(a\in M\). Every normal positive functional \(\varphi\) on \(M\) has a unique density \(k\in L^1_+\), that is, \(\varphi(a)=\tau(ak)\) for \(a\in M\).
- (c) If \(x,y\in L^2\), then \(xy\in L^1\) and \(\tau(xy)=\tau(yx)\). \(L^2\) is a Hilbert space with the inner product \(\langle x,y\rangle_2=\tau(y^*x)\).
- (d) If \((a_i)\) is a bounded net in \(M\) such that \(a_i\to0\) and \(a_i^*\to0\) strongly, then \(a_ix\to0\) and \(xa_i\to0\) in \(L^p\) for every \(x\in L^p\).
- (e) (The trace representation.) Left multiplication \(\pi_\tau(a)=L_a\) is a faithful normal representation of \(M\) on \(L^2\), unitarily equivalent to the GNS representation of \(\tau\). Right multiplication \(R_b\) is bounded, \(R_b^*=R_{b^*}\), and \(L_aR_b=R_bL_a\). The map \(J_\tau x=x^*\) is an antiunitary involution of \(L^2\) with \(J_\tau L_aJ_\tau=R_{a^*}\).

**Fact 2.7** (Standard facts).

- (a) The closed graph theorem: an everywhere defined linear map between Banach spaces with closed graph is bounded. The uniform boundedness theorem: a family of bounded operators that is bounded at each vector is bounded in norm. Both are proved in Hahn–Banach, Baire and the basic theorems on Banach spaces, Theorems 5.3 and 4.2.
- (b) Zorn's lemma and the Hahn–Banach theorem. In particular Banach limits exist: linear functionals \(\operatorname{LIM}\) on \(\ell^\infty(\mathbb N)\) with \(|\operatorname{LIM}(c)|\le\sup_n|c_n|\), and with \(\operatorname{LIM}(c)=\lim_nc_n\) when the limit exists. By the axiom of choice, every subspace of a vector space has an algebraic complement. Zorn's lemma is Theorem 1.1 of the Hahn–Banach lesson and the Hahn–Banach theorem is Section 2 there. A Banach limit is an extension of \(\lim\) from the convergent sequences given by Theorem 2.2 there with the seminorm \(p(c)=\limsup_n|c_n|\), since \(|\lim_nc_n|=p(c)\) for convergent \(c\). A complement of a subspace is spanned by the vectors that extend a basis of the subspace to a basis of the whole space, which exists by Zorn's lemma.
- (c) The spectral theorem for self-adjoint operators, with its Borel functional calculus. A normal \(*\)-homomorphism between von Neumann algebras commutes with the bounded Borel functional calculus. The spectral theorem is proved in The spectral theorem for bounded self-adjoint operators and, for unbounded operators, in Spectral calculus with its domains retained. For the last statement, let \(\pi\) be normal and \(x\in M\) self-adjoint. The bounded Borel functions \(f\) with \(\pi(f(x))=f(\pi(x))\) include the continuous ones, and they are closed under bounded convergence: by Theorem 3.1(4) of the first of these lessons both sides converge strongly, hence \(\sigma\)-weakly, and \(\pi\) is \(\sigma\)-weakly continuous. By Lemma 1.1 there, they are all bounded Borel functions.
- (d) The bicommutant theorem: \(M''=M\). Hence \(M\) is strongly closed, and a bounded operator that commutes with every unitary of \(M'\) lies in \(M\). Every element of \(M\) is a linear combination of four unitaries of \(M\), and has a polar decomposition with its partial isometry in \(M\). These are The double commutant theorem, Theorem 4.4, C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients, Section 7 (applied to \(M'\) for the statement on unitaries of \(M'\)), and The double commutant theorem, Proposition 7.2.
- (e) A positive linear functional \(\varphi\) on \(M\) is *normal* when \(\varphi(\sup_ia_i)=\sup_i\varphi(a_i)\) for every bounded increasing net \((a_i)\) in \(M_+\). Normal positive functionals belong to the predual \(M_*\), and they are continuous for the strong operator topology on bounded sets. The first statement is Normal positive maps and their preadjoints, §NP-02; for the second, a \(\sigma\)-weakly continuous functional is \(\sigma\)-strongly continuous, and on bounded sets the strong and \(\sigma\)-strong topologies agree (Compact and trace-class operators, Lemma 8.5).
- (f) Measure theory: Tonelli's theorem, and the monotone and dominated convergence theorems. Every \(L^2\)-convergent sequence has an almost everywhere convergent subsequence. A \(\sigma\)-finite measure has at most countably many points of positive mass. For a \(\sigma\)-finite measure there are a finite measure with the same null sets and a strictly positive square-integrable function. Tonelli's theorem is [Fremlin, Measure Theory, Volume 2, Theorem 252B](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm) (free; Volumes 1 and 2 of this text are the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)); the convergence theorems are Measure and Hilbert space tools for Haar integration, Theorems 2.1 and 2.2, and the proof of Theorem 3.2 there gives the subsequence. For the last two statements write the space as a disjoint union of sets \(X_n\) of finite measure. At most \(k\mu(X_n)\) points of \(X_n\) have mass at least \(1/k\). The function \(w=\sum_n2^{-n}(1+\mu(X_n))^{-1/2}1_{X_n}\) is strictly positive with \(\int w^2\,d\mu\le\sum_n4^{-n}\), so \(w\) is square integrable and \(w^2\mu\) is a finite measure with the same null sets.

## 3. The commutative model

Let \((X,\mathcal A,\mu)\) be a \(\sigma\)-finite measure space. Let \(M=L^\infty(X,\mu)\) act on \(L^2(X,\mu)\) by multiplication, with the trace \(\tau(f)=\int_Xf\,d\mu\) for \(f\ge0\). This trace is faithful. It is semifinite, because sets of finite measure exhaust \(X\).

It is also normal. To see this, choose a finite measure \(\nu\) with the same null sets as \(\mu\), and let \(f_i\uparrow f\) be an increasing bounded net in \(M_+\). Choose indices \(i_1\le i_2\le\dots\) with \(\int f_{i_k}\,d\nu\to\sup_i\int f_i\,d\nu\), and let \(g\) be the pointwise supremum of the sequence \(f_{i_1}\le f_{i_2}\le\dots\). For each \(i\) and \(k\), some index lies above both \(i\) and \(i_k\), so \(\int\max(f_i,f_{i_k})\,d\nu\le\sup_j\int f_j\,d\nu\). Letting \(k\to\infty\) gives \(\int\max(f_i,g)\,d\nu\le\int g\,d\nu\), so \(f_i\le g\) almost everywhere. Thus \(g\) is an upper bound of the net. Since also \(g\le f\), and \(f\) is the least upper bound, \(g=f\) almost everywhere. The monotone convergence theorem, applied to the increasing sequence \(f_{i_k}\), now gives \(\tau(f)=\lim_k\tau(f_{i_k})\le\sup_i\tau(f_i)\), and the reverse inequality is clear.

Every projection of \(M\) is multiplication by the indicator \(1_E\) of a measurable set \(E\). For a measurable \(f:X\to\mathbb C\), \(M_f\) is multiplication by \(f\) on \(D(M_f)=\{\xi\in L^2:f\xi\in L^2\}\).

**Theorem 3.1** (Measurable operators of a commutative algebra).

1. For every measurable \(f\), \(M_f\) is closed, densely defined and affiliated with \(M\).
2. \(M_f\) is \(\tau\)-measurable if and only if \(\mu(\{|f|\ge n\})\to0\) as \(n\to\infty\). This holds if and only if \(\mu(\{|f|>R\})<\infty\) for some \(R\ge0\).
3. Every \(\tau\)-measurable operator equals \(M_f\) for a measurable \(f\) satisfying (2), and \(f\) is unique up to null sets.

So the \(\tau\)-measurable operators are exactly the operators \(M_f\) for which \(\mu(\{|f|>R\})<\infty\) for some \(R\).

**Proof.** (1) The sets \(\{|f|\le n\}\) increase to \(X\), so the subspaces \(1_{\{|f|\le n\}}L^2\subseteq D(M_f)\) have dense union. If \(\xi_j\to\xi\) and \(f\xi_j\to\eta\) in \(L^2\), a subsequence converges almost everywhere, so \(\eta=f\xi\). For affiliation, let \(u\in M'\) be unitary and \(\xi\in D(M_f)\). Put \(f_n=f1_{\{|f|\le n\}}\in M\). Then \(f_n\xi\to f\xi\) in \(L^2\) by dominated convergence, and \(u(f_n\xi)=f_n(u\xi)\). So \(f_n(u\xi)\to u(f\xi)\) in \(L^2\). A subsequence converges almost everywhere to \(f\,u\xi\). Hence \(f\,u\xi=u(f\xi)\in L^2\), which says \(u\xi\in D(M_f)\) and \(M_fu\xi=uM_f\xi\).

(2) Suppose \(\mu(\{|f|\ge n\})\to0\). Put \(p_n=1_{\{|f|\le n\}}\). These projections increase, \(\tau(1-p_n)=\mu(\{|f|>n\})\to0\), and \(M_fp_n=M_{f1_{\{|f|\le n\}}}\in M\). By the increasing-domain theorem (Fact 2.3(e)), the restriction of \(M_f\) to \(\bigcup_np_nL^2\) is closable, and its closure is \(\tau\)-measurable. That closure is \(M_f\), because \(p_n\xi\to\xi\) and \(fp_n\xi\to f\xi\) for \(\xi\in D(M_f)\). Conversely, suppose \(M_f\) is \(\tau\)-measurable, and let \(d>0\). Condition (2) of the spectral-tail criterion (Fact 2.3(f)) gives a projection \(1_E\) with \(\mu(X\setminus E)<d\) and \(1_EL^2\subseteq D(M_f)\). By Fact 2.3(a), \(M_f1_E=M_{f1_E}\) is bounded and lies in \(M\), so \(|f|\le R\) almost everywhere on \(E\) for some \(R\). Then \(\mu(\{|f|>R\})<d\). Since \(\mu(\{|f|\ge n\})\) decreases in \(n\), it tends to \(0\). Finally, if \(\mu(\{|f|>R\})<\infty\), the sets \(\{|f|\ge n\}\), \(n>R\), decrease to the empty set and have finite measure, so their measures tend to \(0\). The converse is clear.

(3) Let \(T\) be \(\tau\)-measurable. By the cutoff property and the realization theorem (Facts 2.2(d) and 2.3(c)), there are increasing projections \(p_n=1_{E_n}\) with \(\mu(X\setminus E_n)\to0\) and \(Tp_n\in M\), say \(Tp_n=M_{g_n}\) with \(g_n\) bounded. For \(m\ge n\), \(p_n=p_mp_n\), so \(g_n=g_m1_{E_n}\) almost everywhere. Also \(g_n=g_n1_{E_n}\). Define \(f=g_n\) on \(E_n\setminus E_{n-1}\), with \(E_0=\emptyset\), and \(f=0\) off \(\bigcup_nE_n\). Then \(f1_{E_n}=g_n\) almost everywhere for every \(n\). Since \(\mu(\{|f|>\|g_n\|_\infty\})\le\mu(X\setminus E_n)\), \(f\) satisfies (2), so \(M_f\) is \(\tau\)-measurable. Both \(T\) and \(M_f\) contain \(p_nL^2\) in their domains and satisfy \(Tp_n=M_fp_n\). Graph uniqueness (Fact 2.3(b)) gives \(T=M_f\). For uniqueness, let \(M_f=M_{f'}\) and let \(w\in L^2\) be strictly positive, which exists because \(\mu\) is \(\sigma\)-finite. Applying both operators to \(w1_{\{|f|+|f'|\le n\}}\) shows \(f=f'\) almost everywhere on \(\{|f|+|f'|\le n\}\), for every \(n\). \(\square\)

**Remark 3.2** (Convergence in measure). On \(M\) itself, the measure topology is convergence in measure. If \(\mu(\{|f|>r/2\})<d\), then \(f\in U(r,d)\), with witness \(1_{\{|f|\le r/2\}}\). If \(f\in U(r,d)\) with witness \(1_E\), then \(\{|f|\ge r\}\subseteq X\setminus E\) up to a null set, so \(\mu(\{|f|\ge r\})<d\).

## 4. Minimal projections and diffuse algebras

Minimal projections are the atoms of a von Neumann algebra. This section collects what we need about them, and about algebras that have none.

**Lemma 4.1** (Minimal projections).

- (a) If \(e\) is a minimal projection, then \(eMe=\mathbb Ce\).
- (b) If \(e\) is a minimal projection, then \(0<\tau(e)<\infty\).

Now let \(M\) be a factor, that is, \(M\cap M'=\mathbb C1\).

- (c) If \(f,g\in\operatorname{Proj}(M)\) are nonzero, then \(gMf\neq\{0\}\).
- (d) A nonzero projection \(e\) with \(eMe\) abelian is minimal.
- (e) If \(e\) is minimal and \(p\neq0\) is a projection, then there is a partial isometry \(v\in M\) with \(v^*v=e\) and \(vv^*\le p\).

**Proof.** (a) \(eMe\) is a von Neumann algebra on \(eH\) with unit \(e\), and its only projections are \(0\) and \(e\). Every spectral projection of a self-adjoint \(y\in eMe\) is therefore \(0\) or \(e\), so \(y\) is a real multiple of \(e\). Hence \(eMe=\mathbb Ce\).

(b) By semifiniteness (Fact 2.1(e)), \(e\) is the supremum of its subprojections of finite trace. One of them is nonzero, and by minimality it equals \(e\). So \(\tau(e)<\infty\), and \(\tau(e)>0\) because \(\tau\) is faithful.

(c) Let \(K\) be the closed span of \(MfH\). It is invariant under \(M\). It is also invariant under \(M'\), because \(M'MfH=MfM'H\subseteq MfH\). So its projection lies in \(M\cap M'=\mathbb C1\). It is nonzero, since \(K\supseteq fH\). Hence \(K=H\). If \(gMf=\{0\}\), then \(g\) kills \(MfH\), so \(g=0\).

(d) Suppose \(0\neq f\le e\) and \(f\neq e\). By (c) there is \(x\in M\) with \(y=fx(e-f)\neq0\). Then \(y=eye\in eMe\), and \(f\in eMe\). Since \(eMe\) is abelian, \(y=fy=yf=fx(e-f)f=0\), a contradiction.

(e) By (c) there is \(x\in M\) with \(y=pxe\neq0\). By (a), \(y^*y=\lambda e\) with \(\lambda=\|y\|^2>0\). Then \(v=\lambda^{-1/2}y\) has \(v^*v=e\), and \(vv^*\) is a projection with range inside \(pH\). \(\square\)

By (a) and (d), a nonzero projection in a factor is abelian exactly when it is minimal.

**Lemma 4.2** (Minimal projections when \(c(\tau)>0\)). If \(c(\tau)>0\), every nonzero projection majorizes a minimal projection.

**Proof.** Let \(p\neq0\). By semifiniteness (Fact 2.1(e)), choose a nonzero \(f\le p\) of finite trace. Let \(m\) be the infimum of the traces of the nonzero projections under \(f\), so \(m\ge c(\tau)\). Pick a nonzero \(g\le f\) with \(\tau(g)<m+c(\tau)\). If \(g\) were not minimal, then \(g=g_1+g_2\) with nonzero projections \(g_1,g_2\). Then \(\tau(g_1)\ge m\), since \(g_1\le f\), and \(\tau(g_2)\ge c(\tau)\), so \(\tau(g)\ge m+c(\tau)\). So \(g\) is minimal. \(\square\)

**Lemma 4.3** (Trace values in a diffuse algebra). Suppose that \(M\) is diffuse.

1. Every nonzero projection \(e\) with \(\tau(e)<\infty\) has, for every \(\eta>0\), a nonzero subprojection of trace less than \(\eta\).
2. For every projection \(e\) with \(\tau(e)<\infty\) and every \(s\in[0,\tau(e)]\), there is a projection \(f\le e\) with \(\tau(f)=s\).
3. For every such \(e\) and every \(n\ge1\), \(e\) is a sum of \(n\) mutually orthogonal projections of trace \(\tau(e)/n\).

**Proof.** (1) Since \(e\) is not minimal, it has a subprojection \(f\) with \(f\neq0\) and \(f\neq e\). One of \(f\) and \(e-f\) is nonzero with trace at most \(\tau(e)/2\). Repeat this. After \(k\) steps we have a nonzero subprojection of trace at most \(2^{-k}\tau(e)\).

(2) Consider families of mutually orthogonal nonzero subprojections of \(e\) whose sum has trace at most \(s\). Order them by inclusion. The union of a chain is again such a family, because by normality the trace of its sum is the supremum over its finite subfamilies. By Zorn's lemma there is a maximal family. Let \(f\) be its sum, so \(\tau(f)\le s\). Suppose \(\tau(f)<s\). Then \(\tau(e-f)=\tau(e)-\tau(f)>0\), so \(e-f\neq0\), and (1) gives a nonzero \(g\le e-f\) with \(\tau(g)<s-\tau(f)\). Adding \(g\) to the family contradicts maximality. So \(\tau(f)=s\).

(3) By (2) choose \(f_1\le e\) with \(\tau(f_1)=\tau(e)/n\). Then choose \(f_2\le e-f_1\) with \(\tau(f_2)=\tau(e)/n\), which is possible since \(\tau(e-f_1)=(n-1)\tau(e)/n\). Continue, and let \(f_n\) be what remains of \(e\). \(\square\)

**Remark 4.4.** Part (2) has a global form. Let \(M\) be diffuse and \(0\le s<\tau(1)\). Semifiniteness (Fact 2.1(e)) gives \(e\in\mathcal E\) with \(\tau(e)>s\), and (2) gives a projection \(f\le e\) with \(\tau(f)=s\). So every number in \([0,\tau(1)]\), or in \([0,\infty)\) when \(\tau(1)=\infty\), is the trace of a projection.

## 5. The size of the measurable algebra

Always \(M\subseteq S(M,\tau)\), and every element of \(S(M,\tau)\) is a closed, densely defined operator affiliated with \(M\). This section decides when the first inclusion is an equality, and when every affiliated operator is measurable.

**Theorem 5.1** (When the measure topology is the norm topology). The following are equivalent:

1. \(c(\tau)>0\);
2. the measure topology of \(M\) is its norm topology;
3. \(S(M,\tau)=M\), that is, every \(\tau\)-measurable operator is bounded.

When \(M\neq0\) they are also equivalent to

4. the measure topology of \(H\) is its norm topology.

When they hold, \(U(r,d)\) and \(V(r,d)\) are the open balls of radius \(r\) for every \(d\le c(\tau)\), and \(\widehat H=H\).

**Proof.** (1)\(\Rightarrow\)(2), (4). Let \(d\le c(\tau)\). A projection \(p\) with \(\tau(1-p)<d\) has \(1-p=0\). So \(U(r,d)\) is the open norm ball of radius \(r\), and so is \(V(r,d)\). For \(d>c(\tau)\) the sets \(U(r,d)\) and \(V(r,d)\) still contain the balls of radius \(r\). So the neighbourhood filters of \(0\) agree with the norm ones. The measure uniformities are translation invariant (Fact 2.2(b)), so they equal the norm uniformities. \(M\) and \(H\) are complete in norm, hence \(\widehat M=M\) and \(\widehat H=H\).

(2)\(\Rightarrow\)(3). The measure topology comes from a translation-invariant uniformity, which the topology determines. If it is the norm topology, the Cauchy sequences are the norm Cauchy sequences. So \(\widehat M=M\), and every \(\tau\)-measurable operator is \(T_a\) for some \(a\in M\), which is a bounded operator (Fact 2.3(c)).

(3)\(\Rightarrow\)(1). Suppose \(c(\tau)=0\). For each \(k\ge1\) choose a nonzero projection \(p_k\) with \(\tau(p_k)\le2^{-k}\). Put \(q_k=\bigvee_{j\ge k}p_j\). By countable subadditivity (Fact 2.1(c)), \(\tau(q_k)\le\sum_{j\ge k}2^{-j}=2^{1-k}\). The \(q_k\) decrease, and \(\bigwedge_kq_k\) has trace \(0\), so it is \(0\). Put \(r_k=q_k-q_{k+1}\). These projections are mutually orthogonal, and \(\sum_{j\ge k}r_j=q_k\) for every \(k\). Infinitely many \(r_k\) are nonzero. Otherwise \(q_k=q_K\) for all \(k\ge K\), so \(q_K=\bigwedge_kq_k=0\), which contradicts \(q_K\ge p_K\neq0\). Let \(h\) be the positive self-adjoint operator that is \(0\) on \((1-q_1)H\) and equals \(k\) on \(r_kH\). So \(D(h)=\{\xi:\sum_kk^2\|r_k\xi\|^2<\infty\}\). All its spectral projections are sums of the \(r_k\) and \(1-q_1\), so they lie in \(M\) and \(h\) is affiliated with \(M\). For \(R>0\), \(1_{(R,\infty)}(h)=q_K\), where \(K\) is the least integer \(>R\). So \(\tau(1_{(R,\infty)}(h))\le2^{1-K}\to0\), and \(h\) is \(\tau\)-measurable by the spectral-tail criterion (Fact 2.3(f)). It is unbounded, because infinitely many \(r_k\) are nonzero. So (3) fails.

(4)\(\Rightarrow\)(1) when \(M\neq0\). If \(c(\tau)=0\), choose nonzero projections \(p_k\) with \(\tau(p_k)\to0\) and unit vectors \(\xi_k\in p_kH\). Then \((1-p_k)\xi_k=0\), so \(\xi_k\in V(r,d)\), with witness \(1-p_k\), for every \(r>0\) once \(\tau(p_k)<d\). Thus \(\xi_k\to0\) in measure, while \(\|\xi_k\|=1\). So (4) fails. \(\square\)

**Corollary 5.2** (Type I factors). Let \(M\) be a type I factor. Then \(c(\tau)=\tau(e)\) for every minimal projection \(e\) of \(M\), and \(0<c(\tau)<\infty\). Hence \(\tau\)-measure convergence in \(M\) is norm convergence, and \(S(M,\tau)=M\).

**Proof.** Since \(M\) is a factor of type I, the central projection \(1\) majorizes a nonzero abelian projection \(e_0\), that is, a projection with \(e_0Me_0\) abelian. By Lemma 4.1(d), \(e_0\) is minimal, so \(M\) has minimal projections. Now let \(e\) be any minimal projection, and let \(p\neq0\). Lemma 4.1(e) gives a partial isometry \(v\) with \(v^*v=e\) and \(vv^*\le p\), so \(\tau(p)\ge\tau(vv^*)=\tau(e)\) by Fact 2.1(a). So \(c(\tau)=\tau(e)\), which lies in \((0,\infty)\) by Lemma 4.1(b). Theorem 5.1 now applies. \(\square\)

**Remark 5.3.** For \(B(\ell^2(I))\) with its canonical trace, acting on \(\ell^2(I)\), every nonzero projection has trace at least \(1\), so every measurable operator is bounded. Corollary 5.2 covers every representation of a type I factor and every faithful normal semifinite trace on it, for instance \(B(K)\otimes1\) on \(K\otimes L\) with the trace \(3\operatorname{Tr}\) (Example 5.4). Its proof does not use the structure theorem for type I factors. Theorem 5.1 also covers algebras that are not factors. For \(\ell^\infty(I)\) with a trace \(\tau(f)=\sum_iw_if(i)\), one has \(c(\tau)=\inf_iw_i\). For \(\ell^\infty(\mathbb N)\) with \(w_n=2^{-n}\), \(c(\tau)=0\), and the sequence \(g(n)=2^n\) is an unbounded \(\tau\)-measurable operator. Indeed \(\sum_{2^n>R}2^{-n}\to0\).

**Example 5.4** (A type I factor with multiplicity). Let \(M=B(\mathbb C^2)\otimes1\) act on \(\mathbb C^2\otimes\ell^2(\mathbb N)\), with \(\tau=3\operatorname{Tr}\). Every nonzero projection of \(M\) has the form \(e\otimes1\), with trace \(3\operatorname{rank}(e)\ge3\). So \(c(\tau)=3\), and for \(d\le3\) the sets \(U(r,d)\) are norm balls. The vector measure topology on \(\mathbb C^2\otimes\ell^2\) is the norm topology too. The vectors are not "small" in any direction, even though the space is infinite dimensional.

**Theorem 5.5** (Finite traces are detected by affiliated operators). The following are equivalent:

1. \(\tau(1)<\infty\);
2. every closed, densely defined operator affiliated with \(M\) is \(\tau\)-measurable;
3. every positive self-adjoint operator affiliated with \(M\) is \(\tau\)-measurable.

**Proof.** (1)\(\Rightarrow\)(2). Let \(T\) be closed, densely defined and affiliated. Then \(\tau(1_{(0,\infty)}(|T|))\le\tau(1)<\infty\), so condition (4) of the spectral-tail criterion (Fact 2.3(f)) holds with \(R_0=0\).

(2)\(\Rightarrow\)(3) is clear.

(3)\(\Rightarrow\)(1). Suppose \(\tau(1)=\infty\). By semifiniteness (Fact 2.1(e)), a projection of infinite trace has finite-trace subprojections of arbitrarily large trace. Choose \(f_1\in\mathcal E\) with \(\tau(f_1)\ge1\). Then \(\tau(1-f_1)=\infty\), so we can choose \(f_2\in\mathcal E\) with \(f_2\le1-f_1\) and \(\tau(f_2)\ge1\). Continuing, we get mutually orthogonal \(f_k\in\mathcal E\) with \(\tau(f_k)\ge1\). Let \(h\) be \(0\) on \((1-\sum_kf_k)H\) and equal to \(k\) on \(f_kH\). It is positive, self-adjoint and affiliated with \(M\). For every \(R\), \(\tau(1_{(R,\infty)}(h))=\sum_{k>R}\tau(f_k)=\infty\). By the spectral-tail criterion, \(h\) is not \(\tau\)-measurable. \(\square\)

**Corollary 5.6** (Weighted sequence algebras). Let \(M=\ell^\infty(\mathbb N)\) act on \(\ell^2(\mathbb N)\) by multiplication.

1. The faithful normal semifinite traces on \(M\) are the maps \(\tau_w(f)=\sum_nw_nf(n)\), \(f\ge0\), with all \(w_n\in(0,\infty)\).
2. A complex sequence \(g\), acting by multiplication on its maximal domain \(\{\xi:\sum_n|g(n)\xi_n|^2<\infty\}\), is \(\tau_w\)-measurable if and only if \(\sum_{\{n:|g(n)|>R\}}w_n\) is finite for some \(R\), and then it tends to \(0\) as \(R\to\infty\).
3. All sequences are \(\tau_w\)-measurable exactly when \(\sum_nw_n<\infty\).

**Proof.** (1) Let \(\delta_n\) be the indicator of \(\{n\}\). It is a minimal projection, so \(0<\tau(\delta_n)<\infty\) by Lemma 4.1(b). Put \(w_n=\tau(\delta_n)\). For \(f\ge0\), \(f\) is the supremum of the increasing finite sums \(\sum_{n\le N}f(n)\delta_n\), so normality gives \(\tau(f)=\sum_nw_nf(n)\). Conversely each \(\tau_w\) is a trace, normal as a sum of normal maps, faithful since every \(w_n>0\), and semifinite since the finite sets exhaust \(\mathbb N\).

(2) The multiplication operator \(M_g\) is closed, and it is densely defined because its domain contains the finitely supported sequences. It is affiliated with \(M\), because \(M'=M\): an operator commuting with every \(\delta_n\) maps each basis vector \(e_n\) into \(\mathbb Ce_n\), so it is diagonal. The spectral projection \(1_{(R,\infty)}(|M_g|)\) is multiplication by \(1_{\{|g|>R\}}\), with trace \(\sum_{\{|g(n)|>R\}}w_n\). Conditions (3) and (4) of the spectral-tail criterion give the claim. This is also the case of Theorem 3.1 in which \(\mu(\{n\})=w_n\).

(3) This follows from Theorem 5.5. Directly: if \(\sum_nw_n<\infty\), every tail sum is finite. If \(\sum_nw_n=\infty\), the sequence \(g(n)=n\) has infinite tail sums. \(\square\)

## 6. Continuous linear functionals for the measure topology

**Proposition 6.1** (Norm continuity). The identity map from \(M\) with the norm topology to \(M\) with the measure topology is uniformly continuous. Hence every linear functional on \(M\) that is continuous for the measure topology is bounded in norm.

**Proof.** If \(\|x\|<r\), then \(x\in U(r,d)\) for every \(d>0\), with witness \(p=1\). A linear functional that is continuous for a weaker topology is continuous for the norm. \(\square\)

**Theorem 6.2** (Continuous functionals on a diffuse algebra). Suppose that \(M\neq0\) is diffuse. For a linear functional \(\varphi\) on \(M\), the following are equivalent:

1. \(\varphi\) is continuous for the measure topology;
2. \(\varphi\) is bounded in norm and \(\varphi(\mathfrak m_\tau)=0\);
3. \(\varphi\) is bounded in norm and \(\varphi(\mathfrak m_0)=0\).

The continuous linear functionals on \(S(M,\tau)\) are exactly the continuous extensions of these functionals. If \(\tau(1)<\infty\), the only one is \(0\).

**Proof.** (1)\(\Rightarrow\)(3). The functional is bounded by Proposition 6.1. By continuity at \(0\) there are \(r,d>0\) with \(|\varphi(x)|<1\) for all \(x\in U(r,d)\). Let \(x\in\mathfrak m_0\) and let \(e\) be its right support. So \(\tau(e)<\infty\) and \(x=xe\). Choose \(n\) with \(\tau(e)/n<d\), and write \(e=e_1+\dots+e_n\) as in Lemma 4.3(3). For every scalar \(\lambda\), \((\lambda xe_i)(1-e_i)=0\). So \(\lambda xe_i\in U(r,d)\), with witness \(p=1-e_i\), for which \(\tau(1-p)=\tau(e_i)<d\). Hence \(|\lambda|\,|\varphi(xe_i)|<1\) for all \(\lambda\), so \(\varphi(xe_i)=0\). Therefore \(\varphi(x)=\sum_i\varphi(xe_i)=0\).

(3)\(\Rightarrow\)(2). Every element of \(\mathfrak m_\tau=\operatorname{span}(\mathfrak n_\tau^*\mathfrak n_\tau)\) is a combination of four positive elements of finite trace, by the polarization \(y^*z=\frac14\sum_{k=0}^3i^k(z+i^ky)^*(z+i^ky)\). For \(x\ge0\) with \(\tau(x)<\infty\), the operator \(x1_{[1/n,\infty)}(x)\) lies in \(\mathfrak m_0\), because its support has trace at most \(n\tau(x)\). It is within \(1/n\) of \(x\) in norm. So \(\mathfrak m_\tau\) lies in the norm closure of \(\mathfrak m_0\), and a bounded functional that vanishes on \(\mathfrak m_0\) vanishes on \(\mathfrak m_\tau\).

(2)\(\Rightarrow\)(1). Let \(x\in U(r,d)\) with witness \(p\). Then \(x=xp+x(1-p)\). The right support of \(x(1-p)\) lies under \(1-p\), which has finite trace, so \(x(1-p)\in\mathfrak m_0\subseteq\mathfrak m_\tau\) (Fact 2.4(c)). So \(\varphi(x)=\varphi(xp)\) and \(|\varphi(x)|\le\|\varphi\|\,r\). This is continuity at \(0\), which suffices for a linear functional. This step does not use diffuseness.

A continuous linear functional on the dense subspace \(M\) of \(S(M,\tau)\) is uniformly continuous, so it extends uniquely to \(S(M,\tau)\). Conversely, a continuous functional on \(S(M,\tau)\) restricts to one on \(M\). If \(\tau(1)<\infty\), then \(1\in\mathfrak m_\tau\), so \(\mathfrak m_\tau=M\), and (2) forces \(\varphi=0\). \(\square\)

The next three examples show that boundedness and diffuseness are needed in Theorem 6.2, and that nonzero continuous functionals exist when \(\tau(1)=\infty\).

**Example 6.3** (Boundedness is needed). On \(M=L^\infty(0,\infty)\) with the Lebesgue trace, there are linear functionals that vanish on \(\mathfrak m_\tau=L^1\cap L^\infty\) and are not continuous. Let \(g(t)=(1+t)^{-1}\). It is not in \(\mathfrak m_\tau\), but it is the norm limit of \(g1_{[0,n]}\in\mathfrak m_\tau\). Define \(\psi(m+cg)=c\) on \(\mathfrak m_\tau+\mathbb Cg\), and extend \(\psi\) linearly to \(M\) through an algebraic complement (this uses the axiom of choice). Then \(\psi\) vanishes on \(\mathfrak m_\tau\) and \(\psi(g)=1\), so \(\psi\) is not norm continuous. By Proposition 6.1, it is not continuous for the measure topology either. So the condition \(\varphi(\mathfrak m_\tau)=0\) alone does not give continuity.

**Example 6.4** (Diffuseness is needed). Let \(e\) be a minimal projection. By Lemma 4.1(a) and (b), \(eMe=\mathbb Ce\) and \(0<\tau(e)<\infty\). Define \(\varphi_e\) by \(exe=\varphi_e(x)e\). Let \(d<\tau(e)\), and let \(x\in U(r,d)\) with witness \(p\). If \(e\wedge p=0\), then \(e\precsim1-p\) by Fact 2.1(b), so \(\tau(e)\le\tau(1-p)<d\), which is impossible. So \(e\wedge p\neq0\), and by minimality \(e\le p\). Then \(|\varphi_e(x)|=\|exe\|\le\|xpe\|\le\|xp\|<r\). So \(\varphi_e\) is continuous, although \(\varphi_e(e)=1\) and \(e\in\mathfrak m_\tau\). Thus the implication (1)\(\Rightarrow\)(2) of Theorem 6.2, and its last statement, fail as soon as \(M\) has a minimal projection.

**Example 6.5** (Nonzero continuous functionals). On \(L^\infty(0,\infty)\) with the Lebesgue trace, let \(\varphi(f)=\operatorname{LIM}_n\int_n^{n+1}f(t)\,dt\), where \(\operatorname{LIM}\) is a Banach limit. Then \(|\varphi(f)|\le\|f\|_\infty\), \(\varphi\) vanishes on \(L^1\cap L^\infty\) because \(\int_n^{n+1}|f|\to0\) there, and \(\varphi(1)=1\). By Theorem 6.2, \(\varphi\) is a nonzero functional that is continuous for the measure topology.

## 7. Dense subspaces and convergence nearly everywhere

In measure theory a property holds almost everywhere when it holds off a null set. Here that role is played by the range of a projection whose complement has small trace.

**Definition 7.1.** A linear subspace \(D\subseteq H\), not necessarily closed, is \(\tau\)-dense if there are projections \(p_1\le p_2\le\dots\) in \(M\) with \(\tau(1-p_n)\to0\) and \(p_nH\subseteq D\) for all \(n\).

**Proposition 7.2.**

1. \(D\) is \(\tau\)-dense exactly when, for each \(\varepsilon>0\), some \(p\in\operatorname{Proj}(M)\) has \(\tau(1-p)<\varepsilon\) and \(pH\subseteq D\).
2. The intersection of a sequence of \(\tau\)-dense subspaces is \(\tau\)-dense.
3. A \(\tau\)-dense subspace is dense in \(H\). A closed \(\tau\)-dense subspace equals \(H\).
4. The domain of a \(\tau\)-measurable operator is \(\tau\)-dense. Hence countably many \(\tau\)-measurable operators have a \(\tau\)-dense common domain.

**Proof.** (1) One direction is immediate. For the other, choose projections \(q_n\) with \(\tau(1-q_n)<2^{-n}\) and \(q_nH\subseteq D\), and put \(p_n=\bigwedge_{k\ge n}q_k\). The \(p_n\) increase. By countable subadditivity (Fact 2.1(c)), \(\tau(1-p_n)\le\sum_{k\ge n}2^{-k}=2^{1-n}\). And \(p_nH\subseteq q_nH\subseteq D\).

(2) Let \(D_1,D_2,\dots\) be \(\tau\)-dense, and let \(\varepsilon>0\). By (1) choose \(p_n\) with \(\tau(1-p_n)<2^{-n}\varepsilon\) and \(p_nH\subseteq D_n\). Put \(p=\bigwedge_np_n\). Then \(pH\subseteq\bigcap_nD_n\), and \(\tau(1-p)\le\sum_n\tau(1-p_n)<\varepsilon\) by countable subadditivity. Now apply (1).

(3) The projections \(p_n\) increase strongly to \(1\) (Fact 2.1(d)). So \(\bigcup_np_nH\) is dense. If \(D\) is also closed, it contains the closure of this union.

(4) The first statement is condition (2) of the spectral-tail criterion (Fact 2.3(f)), together with (1). The second statement then follows from (2). \(\square\)

**Example 7.3** (Uncountable intersections). Let \(M=L^\infty(0,1)\) with the Lebesgue trace. For \(t\in[0,1]\) let \(D_t\) be the set of \(\xi\in L^2(0,1)\) that vanish almost everywhere on some neighbourhood of \(t\). With \(p=1_{[0,1]\setminus(t-\delta,t+\delta)}\) we get \(\tau(1-p)\le2\delta\) and \(pL^2\subseteq D_t\), so each \(D_t\) is \(\tau\)-dense. But \(\bigcap_tD_t=\{0\}\). Indeed, if \(\xi\) lies in every \(D_t\), each point of \([0,1]\) has an open neighbourhood on which \(\xi=0\) almost everywhere. Finitely many of these cover \([0,1]\), so \(\xi=0\). Hence Proposition 7.2(2) cannot be extended to uncountable families.

**Definition 7.4** (Convergence nearly everywhere). A sequence \((A_n)\) in \(S(M,\tau)\) converges \(\tau\)-nearly everywhere if there is a \(\tau\)-dense subspace \(D\subseteq\bigcap_nD(A_n)\) such that \((A_n\xi)\) converges in norm for every \(\xi\in D\). Its *limit operator* \(A\) has domain
\[
D(A)=\Bigl\{\xi\in\bigcap_nD(A_n):\ \lim_nA_n\xi\text{ exists in norm}\Bigr\},\qquad A\xi=\lim_nA_n\xi.
\]
\(D(A)\) is a linear subspace containing \(D\), and \(A\) is linear on it.

**Theorem 7.5** (The limit operator). Let \((A_n)\) converge \(\tau\)-nearly everywhere, with \(D\) and \(A\) as in Definition 7.4.

- (a) For every unitary \(u\in M'\), \(uD(A)=D(A)\) and \(Au\xi=uA\xi\) for \(\xi\in D(A)\). (So \(A\) is affiliated with \(M\) in the wide sense, which does not require closedness.)
- (b) If \(p\in\operatorname{Proj}(M)\) and \(pH\subseteq D\), then \(A_np\in M\) for every \(n\), \(\sup_n\|A_np\|<\infty\), \(pH\subseteq D(A)\), and \(Ap\) is the strong limit of \(A_np\). In particular \(Ap\in M\).
- (c) There is a unique \(a\in S(M,\tau)\) with \(Ap=ap\) for every \(p\in\operatorname{Proj}(M)\) such that \(pH\subseteq D\). The operator \(A\) is closable, and \(\overline A=a\). The subspace \(D\) is a core for \(a\).
- (d) \(A\) itself need not be closed (Example 7.6).

*Remark.* The limit operator is \(\tau\)-measurable only after closing: by (d), \(\overline A\) is \(\tau\)-measurable, while \(A\) need not be.

**Proof.** (a) Each \(A_n\) is affiliated, so \(uD(A_n)=D(A_n)\) and \(A_nu=uA_n\) there. So \(A_nu\xi=uA_n\xi\) converges exactly when \(A_n\xi\) converges, and the limits satisfy \(Au\xi=uA\xi\). The same holds for \(u^*\).

(b) Since \(pH\subseteq D(A_n)\), Fact 2.3(a) gives \(A_np\in M\); this step uses the closed graph theorem. For each \(\xi\in H\), \(p\xi\in D\), so \((A_np\xi)\) converges and is bounded. The uniform boundedness theorem gives \(K=\sup_n\|A_np\|<\infty\). The strong limit of \(A_np\) is a bounded operator of norm at most \(K\). It lies in \(M\), since \(M\) is strongly closed. It equals \(Ap\), and \(pH\subseteq D\subseteq D(A)\).

(c) By Proposition 7.2(1), choose increasing projections \(p_k\) with \(p_kH\subseteq D\) and \(\tau(1-p_k)\to0\). By (b), \(Ap_k\in M\). The increasing-domain theorem (Fact 2.3(e)), applied to the restriction of \(A\) to \(D_0=\bigcup_kp_kH\), shows that this restriction is closable and that its closure is \(T_a\) for a unique \(a\in S(M,\tau)\).

We show \(A\subseteq T_a\). Let \(\xi\in D(A)\) and \(\eta=A\xi\). Fix \(k\). Since \(p_k\xi\in D\), also \((1-p_k)\xi\in D(A)\). Since \(p_k\xi\in D_0\), where \(A\) agrees with \(T_a\), the definition of \(T_a\) (Fact 2.3(c)) gives \(Ap_k\xi=a(p_k\xi)\) in \(\widehat H\). So
\[
\eta=a(p_k\xi)+\eta_k,\qquad \eta_k=A\bigl((1-p_k)\xi\bigr)=\lim_nA_n(1-p_k)\xi.
\]
Let \(T_{n}\) be the ordinary product \(A_n(1-p_k)\), with domain \(\{\zeta:(1-p_k)\zeta\in D(A_n)\}\). It is closed and densely defined (Fact 2.3(d)), and it is affiliated with \(M\). Its kernel contains \(p_kH\), so its right support lies under \(1-p_k\). Let \(l_n\in M\) be its left support, the projection onto the closure of its range. The left and right supports of \(T_n\) are equivalent (Fact 2.1(a)), so \(\tau(l_n)\le\tau(1-p_k)\). The vector \(\zeta_n=T_n\xi=A_n(1-p_k)\xi\) satisfies \((1-l_n)\zeta_n=0\). Hence \(\zeta_n\in V(r,d)\) for every \(r>0\) whenever \(\tau(1-p_k)<d\), with witness \(1-l_n\). Since \(\zeta_n\to\eta_k\) in norm, and norm balls lie in every \(V(r',d')\), the sum estimate for the sets \(V\) (Fact 2.2(a)) gives \(\eta_k\in V(r,2d)\) for all \(r>0\), as soon as \(\tau(1-p_k)<d\). So \(\eta_k\to0\) in \(\widehat H\) as \(k\to\infty\). Also \(p_k\xi\to\xi\) in norm, hence in measure, and the action of the fixed element \(a\) on \(\widehat H\) is continuous (Fact 2.2(c)). So \(a(p_k\xi)\to a\xi\). Therefore the constant vector \(\eta\) equals \(a\xi\) in the Hausdorff space \(\widehat H\). This says \(\xi\in D(T_a)\) and \(T_a\xi=\eta\).

So \(A\) lies between its restriction to \(D_0\) and \(T_a\). Its closure is \(T_a\), and \(D\supseteq D_0\) is a core. For uniqueness: if \(b\in S(M,\tau)\) has \(bp_k=Ap_k=ap_k\) for all \(k\), then \((b-a)p_k=0\), and \(p_k\to1\) in measure (Fact 2.2(d)) gives \(b=a\). \(\square\)

**Example 7.6** (The limit operator need not be closed). Let \(M=L^\infty(0,1)\) with the Lebesgue trace, and let \(A_n\) be multiplication by \(f_n=n\,1_{(0,n^{-3})}\), a bounded function. Let \(D\) be the set of \(\xi\in L^2\) that vanish almost everywhere on some interval \((0,1/m)\). It is \(\tau\)-dense, with \(p_m=1_{(1/m,1)}\). For \(\xi\in p_mL^2\), \(f_n\xi=0\) once \(n^{-3}\le1/m\). So \((A_n)\) converges \(\tau\)-nearly everywhere, and \(Ap_m=0\). By Theorem 7.5(c), \(\overline A=0\) with domain \(L^2\). But \(\xi_0(t)=t^{-1/3}\) lies in \(L^2\), and
\[
\|f_n\xi_0\|_2^2=n^2\int_0^{n^{-3}}t^{-2/3}\,dt=3n\to\infty .
\]
So \(\xi_0\notin D(A)\). Thus \(D(A)\neq L^2=D(\overline A)\), and \(A\) is not closed.

When the \(A_n\) are self-adjoint, the closure of the limit operator is self-adjoint and the resolvents converge. This rests on a general criterion for self-adjoint operators.

**Lemma 7.7** (Strong resolvent convergence). Let \(B\) and \(B_n\) be self-adjoint operators on \(H\), and let \(D\subseteq\bigcap_nD(B_n)\) be a core for \(B\) with \(B_n\xi\to B\xi\) for every \(\xi\in D\). Then \((B_n-\lambda)^{-1}\to(B-\lambda)^{-1}\) strongly for every non-real \(\lambda\).

**Proof.** For \(\xi\in D\) put \(\psi=(B-\lambda)\xi\). Then
\[
(B_n-\lambda)^{-1}\psi-(B-\lambda)^{-1}\psi=(B_n-\lambda)^{-1}(B\xi-B_n\xi),
\]
whose norm is at most \(|\operatorname{Im}\lambda|^{-1}\|B\xi-B_n\xi\|\to0\). The vectors \(\psi\) of this form are dense. Indeed, every \(\psi\in H\) is \((B-\lambda)\zeta\) with \(\zeta\in D(B)\). Choose \(\xi_j\in D\) with \(\xi_j\to\zeta\) in the graph norm of \(B\); then \((B-\lambda)\xi_j\to\psi\). All the resolvents have norm at most \(|\operatorname{Im}\lambda|^{-1}\), so convergence on a dense set gives convergence everywhere. \(\square\)

**Theorem 7.8** (Self-adjoint limits). Let \((A_n)\) be self-adjoint \(\tau\)-measurable operators that converge \(\tau\)-nearly everywhere, with limit operator \(A\). Then \(\overline A\) is self-adjoint, and \((A_n-\lambda)^{-1}\to(\overline A-\lambda)^{-1}\) strongly for every non-real \(\lambda\).

**Proof.** For \(\xi,\eta\in D(A)\), \(\langle A\xi,\eta\rangle=\lim\langle A_n\xi,\eta\rangle=\lim\langle\xi,A_n\eta\rangle=\langle\xi,A\eta\rangle\). So \(A\) is symmetric, and so is \(\overline A=a\) (Theorem 7.5(c)). That is, \(a\subseteq a^*\). By Fact 2.3(d), \(a^*\) is the measurable operator \(T_{a^*}\). It is a closed affiliated extension of \(a\), so \(a^*=a\) by the maximality in Fact 2.3(c). By Theorem 7.5(c), \(D\) is a core for \(a\), and \(D\subseteq\bigcap_nD(A_n)\). Lemma 7.7 applies. \(\square\)

## 8. Convergence nearly everywhere compared with other modes

This section compares convergence nearly everywhere with uniform convergence off projections of small trace, with convergence in measure, and, for commutative algebras, with almost everywhere convergence.

**Theorem 8.1** (Egoroff's theorem along subsequences). Let \((A_n)\) converge \(\tau\)-nearly everywhere, with \(D\), \(A\) and \(a=\overline A\) as in Theorem 7.5. Let \(e\in\operatorname{Proj}(M)\) with \(\tau(e)<\infty\), and let \(\delta>0\). There are a projection \(p\le e\) with \(\tau(e-p)<\delta\) and \(pH\subseteq D\), and a strictly increasing sequence \((n_k)\), such that
\[
\|(A_{n_k}-a)p\|\le2^{-k}\qquad(k\ge1).
\]
Here \((A_n-a)p=A_np-ap\) is a bounded operator, by Theorem 7.5(b) and (c). In particular, for every \(\varepsilon,\delta>0\) and every \(N_0\) there are \(n\ge N_0\) and a projection \(p\le e\) with \(\tau(e-p)<\delta\) and \(\|(A_n-a)p\|<\varepsilon\).

*Remark.* One cannot ask for a single projection \(p\) that works for all large \(n\): Example 8.2 shows that no such projection need exist, so the theorem passes to a subsequence.

**Proof.** By Proposition 7.2(1), choose \(q\in\operatorname{Proj}(M)\) with \(qH\subseteq D\) and \(\tau(1-q)<\delta/2\). Put \(p_1=e\wedge q\). The projection \(e-p_1\) has zero meet with \(q\), so \(e-p_1\precsim1-q\) (Fact 2.1(b)), and \(\tau(e-p_1)<\delta/2\). Put \(x_n=(A_n-a)p_1=(A_nq-aq)p_1\). By Theorem 7.5(b), the \(x_n\) are in \(M\), \(\sup_n\|x_n\|=K<\infty\), and \(x_n\zeta\to0\) for every \(\zeta\in H\), since \(p_1\zeta\in qH\subseteq D\). Put \(y_n=x_n^*x_n\in p_1Mp_1\). Then \(\|y_n\|\le K^2\) and \(\|y_n\zeta\|\le K\|x_n\zeta\|\to0\).

The functional \(z\mapsto\tau(p_1zp_1)\) is positive and normal, since \(\tau\) is normal, and it has finite norm \(\tau(p_1)\). A normal positive functional is continuous for the strong topology on bounded sets (Fact 2.7(e)). So \(\tau(y_n)=\tau(p_1y_np_1)\to0\). Choose \(n_1<n_2<\dots\) with \(\tau(y_{n_k})<8^{-k}\delta/2\). Let \(f_k=1_{(4^{-k},\infty)}(y_{n_k})\). This projection lies under the support of \(y_{n_k}\), hence under \(p_1\), and \(4^{-k}f_k\le y_{n_k}\) gives \(\tau(f_k)\le4^k\tau(y_{n_k})<2^{-k}\delta/2\). Put \(f=\bigvee_kf_k\le p_1\) and \(p=p_1-f\). By countable subadditivity (Fact 2.1(c)), \(\tau(f)\le\sum_k\tau(f_k)<\delta/2\), so \(\tau(e-p)<\delta\). A vector \(\zeta\in pH\) lies in \(p_1H\) and in \((1-f_k)H=1_{[0,4^{-k}]}(y_{n_k})H\), so
\[
\|x_{n_k}\zeta\|^2=\langle y_{n_k}\zeta,\zeta\rangle\le4^{-k}\|\zeta\|^2 .
\]
Since \(p\le p_1\), \(x_{n_k}p=(A_{n_k}-a)p\), and its norm is at most \(2^{-k}\). \(\square\)

**Example 8.2** (One projection cannot serve all large \(n\)). One cannot ask in Theorem 8.1 for \(N\) and \(p\) with \(\|(A_n-A)p\|<\varepsilon\) for all \(n\ge N\), nor for one \(p\) with \(\|(A_n-A)p\|\to0\). Let \(M=L^\infty(0,1)\) with the Lebesgue trace. For \(k\ge0\) and \(1\le j\le k+1\) put
\[
I_{j+k(k+1)/2}=\Bigl[\frac{j-1}{k+1},\frac{j}{k+1}\Bigr].
\]
The intervals with a fixed \(k\) form a row that covers \([0,1]\). Let \(A_n\) be multiplication by \(1_{I_n}\). For \(\xi\in L^2\), \(\|A_n\xi\|_2^2=\int_{I_n}|\xi|^2\to0\), because \(|I_n|\to0\). So \(A_n\to0\) strongly on all of \(L^2\), hence \(\tau\)-nearly everywhere with \(D=L^2\) and \(A=0\). Take \(e=1\) and \(\varepsilon=\delta=1/2\). Suppose \(p=1_E\) has \(\tau(1-p)<1/2\) and \(\|A_np\|<1/2\) for all \(n\ge N\). Since \(\|1_{I_n\cap E}\|_\infty\) is \(0\) or \(1\), we get \(|I_n\cap E|=0\) for \(n\ge N\). A row whose indices are all \(\ge N\) covers \([0,1]\), so \(|E|=0\) and \(\tau(1-p)=1\), a contradiction. The second request fails too, since it would give such an \(N\).

**Theorem 8.3** (The commutative case). Let \((X,\mu)\), \(M\) and \(\tau\) be as in Section 3. Let \(A_n=M_{f_n}\) with \(f_n\) measurable and satisfying condition (2) of Theorem 3.1, so that each \(A_n\) is \(\tau\)-measurable. Put \(g=\sup_n|f_n|\).

1. If \((A_n)\) converges \(\tau\)-nearly everywhere, then \(\mu(\{g>R\})\to0\) as \(R\to\infty\).
2. If \(f_n\to f\) almost everywhere and \(\mu(\{g>R\})<\infty\) for some \(R\), then \((A_n)\) converges \(\tau\)-nearly everywhere, and the closure of the limit operator is \(M_f\).
3. If \(\mu(X)<\infty\), almost everywhere convergence of \((f_n)\) implies \(\tau\)-nearly everywhere convergence of \((A_n)\).
4. Suppose \((A_n)\) converges \(\tau\)-nearly everywhere, and let \(\overline A=M_f\), with \(f\) given by Theorem 3.1(3). Then some subsequence of \((f_n)\) converges to \(f\) almost everywhere, and every subsequence that converges almost everywhere has limit \(f\) almost everywhere.
5. When \(\mu(X)=\infty\), the condition on \(g\) in (2) cannot be dropped.

*Remark.* By (3) and (5), almost everywhere convergence of \((f_n)\) implies convergence nearly everywhere of \((A_n)\) for all sequences exactly when \(\mu(X)<\infty\).

**Proof.** (1) Let \(d>0\). By Proposition 7.2(1) there is \(1_E\) with \(\mu(X\setminus E)<d\) and \(1_EL^2\subseteq D\). By Theorem 7.5(b), \(\sup_n\|f_n1_E\|_\infty=R_E<\infty\). So \(g\le R_E\) almost everywhere on \(E\), and \(\mu(\{g>R_E\})<d\).

(2) A convergent sequence of numbers is bounded, so \(g<\infty\) almost everywhere. Hence the sets \(\{g>R\}\) decrease to a null set. One of them has finite measure, so \(\mu(\{g>R\})\to0\). Put \(E_R=\{g\le R\}\) and \(D=\bigcup_{R\in\mathbb N}1_{E_R}L^2\). This is \(\tau\)-dense, and \(D\subseteq D(A_n)\) for all \(n\), since \(|f_n|\le R\) on \(E_R\). For \(\xi\in1_{E_R}L^2\), \(f_n\xi\to f\xi\) almost everywhere and \(|f_n\xi-f\xi|^2\le4R^2|\xi|^2\), so \(f_n\xi\to f\xi\) in \(L^2\) by dominated convergence. Thus \((A_n)\) converges \(\tau\)-nearly everywhere, and \(A1_{E_R}=M_{f1_{E_R}}=M_f1_{E_R}\). Since \(|f|\le g\), \(M_f\) is \(\tau\)-measurable by Theorem 3.1(2). By Theorem 7.5(c), \(\overline A\) is the unique measurable operator that agrees with \(A\) on these cutoffs, so \(\overline A=M_f\).

(3) If \(\mu(X)<\infty\), every \(\mu(\{g>R\})\) is finite, and (2) applies.

(4) By Proposition 7.2(1) choose sets \(E_j\) with \(\mu(X\setminus E_j)<2^{-j}\) and \(1_{E_j}L^2\subseteq D\). Fix a strictly positive \(w\in L^2\) and put \(w_j=w1_{E_j}\in D\). Since \(A\subseteq\overline A=M_f\), \(f_nw_j\to fw_j\) in \(L^2\) for each \(j\). An \(L^2\)-convergent sequence has an almost everywhere convergent subsequence. A diagonal choice gives one subsequence \((f_{n_k})\) with \(f_{n_k}w_j\to fw_j\) almost everywhere for every \(j\). Since \(w_j>0\) on \(E_j\), \(f_{n_k}\to f\) almost everywhere on \(\bigcup_jE_j\), which has a null complement. If another subsequence converges almost everywhere to \(f'\), then for each \(j\) it still converges to \(fw_j\) in \(L^2\). A further subsequence converges to \(fw_j\) almost everywhere, so \(f'=f\) almost everywhere on \(E_j\), for every \(j\).

(5) Let \(X=[0,\infty)\) with Lebesgue measure and \(f_n(t)=t\,1_{[n-1,n)}(t)\). Each \(f_n\) is bounded, and \(f_n\to0\) everywhere. Suppose \((A_n)\) converged \(\tau\)-nearly everywhere. By Proposition 7.2(1) there is \(1_E\) with \(\mu(X\setminus E)<1/2\) and \(1_EL^2\subseteq D\). Put \(\xi=\sum_{n\ge2}n^{-1}1_{E\cap[n-1,n)}\). Then \(\|\xi\|_2^2\le\sum_nn^{-2}<\infty\), so \(\xi\in1_EL^2\). Since \(|[n-1,n)\setminus E|<1/2\),
\[
\|f_n\xi\|_2^2\ge\Bigl(\frac{n-1}{n}\Bigr)^2\bigl|E\cap[n-1,n)\bigr|\ge\frac12\Bigl(\frac{n-1}{n}\Bigr)^2 .
\]
So \(f_n\xi\) does not tend to \(0\). It cannot converge to anything else either, because a subsequence of an \(L^2\)-convergent sequence converges almost everywhere, and \(f_n\xi\to0\) pointwise. This contradicts \(\xi\in D\). The same argument works on every \(\sigma\)-finite \(X\) with \(\mu(X)=\infty\). Grouping a partition of \(X\) into sets of finite measure gives disjoint sets \(X_n\) with \(1\le\mu(X_n)<\infty\). Use \(f_n=n1_{X_n}\) and \(\xi=\sum_nn^{-1}\mu(E\cap X_n)^{-1/2}1_{E\cap X_n}\). Here \(\mu(E\cap X_n)>1/2\), \(\|\xi\|_2^2=\sum_nn^{-2}\) and \(\|f_n\xi\|_2=1\). \(\square\)

**Proposition 8.4** (Convergence in measure without convergence nearly everywhere). Let \(M\neq0\) be diffuse. There is a sequence in \(M\) that converges to \(0\) in measure but does not converge \(\tau\)-nearly everywhere.

**Proof.** By semifiniteness (Fact 2.1(e)) there is a nonzero \(e\in\mathcal E\). For each \(k\ge0\), Lemma 4.3(3) splits \(e\) into \(k+1\) mutually orthogonal projections \(P_{k,1},\dots,P_{k,k+1}\), each of trace \(\tau(e)/(k+1)\). Put \(A_n=(k+1)^2P_{k,j}\) for \(n=j+k(k+1)/2\). Since \(A_n(1-P_{k,j})=0\) and \(\tau(P_{k,j})\to0\), \(A_n\to0\) in measure. Suppose \((A_n)\) converged \(\tau\)-nearly everywhere with a \(\tau\)-dense \(D\). Choose \(p\) with \(pH\subseteq D\) and \(\tau(1-p)<\tau(e)\). By Theorem 7.5(b), \(K=\sup_n\|A_np\|<\infty\), so \(\|P_{k,j}p\|\le K/(k+1)^2\). Then for every \(k\),
\[
\|ep\|=\Bigl\|\sum_{j=1}^{k+1}P_{k,j}p\Bigr\|\le(k+1)\frac K{(k+1)^2}=\frac K{k+1}.
\]
So \(ep=0\), which means \(e\le1-p\) and \(\tau(e)\le\tau(1-p)<\tau(e)\). This is a contradiction. \(\square\)

The projection \(p\) need not commute with the \(P_{k,j}\); the norm estimate does not need this. In \(L^\infty(0,1)\) with the Lebesgue trace, the same argument applies to the sequence \(f_n=|I_n|^{-2}1_{I_n}\), with the intervals \(I_n\) of Example 8.2.

**Proposition 8.5** (Convergence nearly everywhere without pointwise convergence). On \(M=L^\infty(0,1)\) with the Lebesgue trace, the sequence \(A_n=1_{I_n}\) of Example 8.2 converges \(\tau\)-nearly everywhere to \(0\), but \(1_{I_n}(t)\) converges at no point \(t\in[0,1]\). If each \(1_{I_n}\) is changed on a null set, the new values still fail to converge almost everywhere.

**Proof.** Convergence \(\tau\)-nearly everywhere was shown in Example 8.2. Each row covers \(t\), so \(1_{I_n}(t)=1\) for infinitely many \(n\). For \(k\ge2\), \(t\) lies in at most two of the \(k+1\) intervals of row \(k\), so \(1_{I_n}(t)=0\) for infinitely many \(n\). Countably many null changes affect only a null set of points. \(\square\)

**Remark 8.6** (Atomic algebras). Diffuseness suffices for Proposition 8.4, but it is not necessary. On \(\ell^\infty(\mathbb N)\) with \(w_i=1/i\), the sequence \(A_n=n\delta_n\) tends to \(0\) in measure, since \(\tau(\delta_n)=1/n\). It does not converge \(\tau\)-nearly everywhere. Any \(1_E\) with \(\sum_{i\notin E}1/i<1\) has \(E\) infinite, so \(\sup_n\|A_n1_E\|=\sup_{n\in E}n=\infty\), which contradicts Theorem 7.5(b). On \(\ell^\infty(\mathbb N)\) with \(w_i=2^{-i}\), convergence in measure does imply convergence \(\tau\)-nearly everywhere. Convergence in measure forces convergence in each coordinate, because a witness projection of trace defect \(<w_i\) must contain \(\delta_i\). The finitely supported sequences form a \(\tau\)-dense common domain on which the convergence then holds. If \(c(\tau)>0\), convergence in measure is norm convergence (Theorem 5.1), which gives convergence on \(D=H\). Theorem 8.7 gives an exact criterion.

**Theorem 8.7** (When convergence in measure implies convergence nearly everywhere). Call \(M\) *atomic* when every
nonzero projection of \(M\) majorizes a minimal projection. For \(\varepsilon>0\) let \(z_\varepsilon\) be the supremum
of the minimal projections of \(M\) of trace less than \(\varepsilon\), with \(z_\varepsilon=0\) if there is none. The
following are equivalent:

1. every sequence in \(M\) that converges to \(0\) in measure converges \(\tau\)-nearly everywhere;
2. every sequence \((x_n)\) in \(S(M,\tau)\) that converges in measure to some \(x\in S(M,\tau)\) converges
   \(\tau\)-nearly everywhere, and the closure of its limit operator is \(x\);
3. \(M\) is atomic, and \(\tau(z_\varepsilon)<\infty\) for some \(\varepsilon>0\).

For \(\ell^\infty(\mathbb N)\) with \(\tau(f)=\sum_iw_if(i)\), \(z_\varepsilon\) is the indicator of
\(\{i:w_i<\varepsilon\}\), and (3) says that \(\sum_{\{i:w_i<\varepsilon\}}w_i<\infty\) for some \(\varepsilon>0\). This
holds for \(w_i=2^{-i}\) and fails for \(w_i=1/i\), as Remark 8.6 found. Condition (3) holds when \(c(\tau)>0\), by Lemma
4.2 and because \(z_\varepsilon=0\) for \(\varepsilon\le c(\tau)\), and it holds when \(M\) is atomic and
\(\tau(1)<\infty\).

**Proof.** We first record two facts.

(i) \(z_\varepsilon\) is central, and every minimal projection \(q\le z_\varepsilon\) has \(\tau(q)<\varepsilon\). For a
unitary \(u\in M\) and a minimal projection \(e\), \(ueu^*\) is minimal and \(\tau(ueu^*)=\tau(e)\) (Fact 2.1(a)). So
\(uz_\varepsilon u^*=z_\varepsilon\), and \(z_\varepsilon\) commutes with \(M\), which is spanned by its unitaries (Fact
2.7(d)). Let \(q\le z_\varepsilon\) be minimal. If \(q\) were orthogonal to every minimal projection of trace less than
\(\varepsilon\), it would lie under \(1-z_\varepsilon\). So \(qe\neq0\) for one such \(e\). By Lemma 4.1(a),
\((qe)^*(qe)=\lambda e\) with \(\lambda=\|qe\|^2>0\). Then \(v=\lambda^{-1/2}qe\) has \(v^*v=e\), and \(vv^*\) is a
nonzero projection in \(qMq=\mathbb Cq\), so \(vv^*=q\). Hence \(\tau(q)=\tau(e)<\varepsilon\).

(ii) Let \(q\) be a projection whose nonzero subprojections all have trace at least \(\eta>0\). Then every projection
\(e\) with \(\tau(1-e)<\eta\) majorizes \(q\), and \(qH\) lies in the domain of every \(y\in S(M,\tau)\). Indeed
\(q-q\wedge e\) has zero meet with \(e\), so \(q-q\wedge e\precsim1-e\) (Fact 2.1(b)); its trace is less than \(\eta\),
so it is \(0\). For the second statement choose \(e\) with \(\tau(1-e)<\eta\) and \(eH\subseteq D(y)\) (Fact 2.3(f)).

(3)\(\Rightarrow\)(2). Let \(\varepsilon\) be as in (3), and \(z=z_\varepsilon\). A nonzero projection \(p\le1-z\)
majorizes a minimal projection \(q'\), which is orthogonal to \(z\) and therefore has \(\tau(q')\ge\varepsilon\); so
\(\tau(p)\ge\varepsilon\). By Zorn's lemma and atomicity, \(z\) is the sum of a family of mutually orthogonal minimal
projections. The family is countable, because \(\tau(z)<\infty\) and each member has positive trace (Lemma 4.1(b)):
\(z=\sum_jq_j\). Put \(P_N=(1-z)+\sum_{j\le N}q_j\). Then \(\tau(1-P_N)=\sum_{j>N}\tau(q_j)\to0\), so
\(D=\bigcup_NP_NH\) is \(\tau\)-dense. Apply (ii) to \(1-z\) with \(\eta=\varepsilon\) and to each \(q_j\) with
\(\eta=\tau(q_j)\): every \(P_NH\) lies in the domain of every element of \(S(M,\tau)\), and with
\(\eta_N=\min(\varepsilon,\tau(q_1),\dots,\tau(q_N))\), every projection \(e\) with \(\tau(1-e)<\eta_N\) majorizes
\(1-z\) and \(q_1,\dots,q_N\), hence their sum \(P_N\). Now let \(x_n\to x\) in measure, and let \(r>0\). By Fact 2.5(e),
for all large \(n\) there is a projection \(e_n\) with \(\tau(1-e_n)<\eta_N\), \(e_nH\subseteq D(x_n-x)\) and
\(\|(x_n-x)e_n\|<r\). Then \(e_n\ge P_N\), so \(\|(x_n-x)P_N\|<r\). On \(P_NH\) the operator \(x_n-x\) acts as the
difference of \(x_n\) and \(x\) (Fact 2.3(d)). Hence \(x_n\xi\to x\xi\) for every \(\xi\in D\). So \((x_n)\) converges
\(\tau\)-nearly everywhere with this \(D\), its limit operator \(A\) satisfies \(Ap=xp\) whenever \(pH\subseteq D\), and
\(\overline A=x\) by the uniqueness in Theorem 7.5(c).

(2)\(\Rightarrow\)(1) is clear.

(1)\(\Rightarrow\)(3). Suppose first that \(M\) is not atomic, so that some nonzero projection \(p\) majorizes no minimal
projection. The corner \(pMp\) is a von Neumann algebra on \(pH\), and a minimal projection of \(pMp\) would be minimal
in \(M\); so \(pMp\) is diffuse. By semifiniteness (Fact 2.1(e)) there is a nonzero \(e\le p\) of finite trace. Lemma
4.3(3), applied in \(pMp\) with the restriction of \(\tau\), splits \(e\) into \(k+1\) mutually orthogonal projections of
trace \(\tau(e)/(k+1)\), for every \(k\). With these projections, the proof of Proposition 8.4 gives a sequence in \(M\)
that converges to \(0\) in measure and does not converge \(\tau\)-nearly everywhere.

Now suppose that \(M\) is atomic and \(\tau(z_\varepsilon)=\infty\) for every \(\varepsilon>0\). We choose mutually
orthogonal projections \(F_1,F_2,\dots\) with \(1/n\le\tau(F_n)<2/n\). Suppose \(F_1,\dots,F_{n-1}\) are chosen, and let
\(G=\sum_{l<n}F_l\), of finite trace. By (i), \(r=z_{1/n}(1-G)\) is a projection, and
\(\tau(z_{1/n})=\tau(r)+\tau(z_{1/n}G)\le\tau(r)+\tau(G)\), so \(\tau(r)=\infty\). By atomicity and Zorn's lemma, \(r\)
is the sum of mutually orthogonal minimal projections. Each has trace less than \(1/n\), by (i), and their traces add
up to \(\infty\), by normality. Adding finitely many of them until the sum first reaches \(1/n\) gives a projection
\(F_n\le r\) with \(1/n\le\tau(F_n)<2/n\).

Put \(A_n=nF_n\in M\). Since \(A_n(1-F_n)=0\) and \(\tau(F_n)\to0\), \(A_n\to0\) in measure. Suppose that \((A_n)\)
converged \(\tau\)-nearly everywhere, with a \(\tau\)-dense \(D\). Choose \(p\) with \(pH\subseteq D\) and
\(\tau(1-p)<1\) (Proposition 7.2(1)). By Theorem 7.5(b), \(K=\sup_n\|A_np\|<\infty\), so \(\|F_np\|\le K/n\). Choose
\(m\) with \(K^2\sum_{n\ge m}n^{-2}<1\). For \(N>m\) let \(G_N=\sum_{n=m}^NF_n\). For \(\xi\in H\),
\[
\|G_Np\xi\|^2=\sum_{n=m}^N\|F_np\xi\|^2\le K^2\sum_{n\ge m}n^{-2}\,\|\xi\|^2,
\]
so \(\|G_Np\|<1\) and \(G_N\wedge p=0\). By Fact 2.1(b) and (a), \(\tau(G_N)\le\tau(1-p)<1\). But
\(\tau(G_N)\ge\sum_{n=m}^N1/n\), which exceeds \(1\) for large \(N\). So \((A_n)\) does not converge \(\tau\)-nearly
everywhere, and (1) fails. \(\square\)

## 9. Distribution functions and generalized singular values

A reference for this section is [Fack–Kosaki 1986]. For \(T\in S(M,\tau)\), \(s\ge0\) and \(t>0\) put
\[
\lambda_s(T)=\tau\bigl(1_{(s,\infty)}(|T|)\bigr),\qquad
\mu_t(T)=\inf\{\|Te\|:\ e\in\operatorname{Proj}(M),\ eH\subseteq D(T),\ \tau(1-e)\le t\}.
\]
So \(\lambda_s(T)=d_T(s)\), and \(\mu_t(T)\) is the number defined in Section 1. The function \(t\mapsto\mu_t(T)\) is the *generalized singular value function* of \(T\). One may drop the condition \(eH\subseteq D(T)\), reading \(\|Te\|\) as \(+\infty\) when \(Te\) is unbounded. The two definitions agree: the ordinary product \(Te\) is closed and densely defined (Fact 2.3(d)), and a closed operator that is bounded on its domain has a closed, hence full, domain.

**Theorem 9.1** (Singular values from the distribution function). For \(t>0\),
\[
\mu_t(T)=\inf\{s\ge0:\ \lambda_s(T)\le t\},\qquad \lambda_{\mu_t(T)}(T)\le t.
\tag{9.1}
\]
This is Fact 2.5(a); here is a direct proof from the definitions.

**Proof.** *Step 1.* The function \(s\mapsto\lambda_s(T)\) does not increase. It is continuous from the right: if \(s_n\downarrow s\), the projections \(1_{(s_n,\infty)}(|T|)\) increase to \(1_{(s,\infty)}(|T|)\), and \(\tau\) is normal. By the spectral-tail criterion (Fact 2.3(f)), \(\lambda_s(T)\to0\) as \(s\to\infty\). So the set \(\{s:\lambda_s(T)\le t\}\) is nonempty. Let \(\alpha\) be its infimum. Right continuity gives \(\lambda_\alpha(T)\le t\). Let \(E=1_{[0,\alpha]}(|T|)\). Then \(EH\subseteq D(T)\), \(\|TE\|=\||T|E\|\le\alpha\), and \(\tau(1-E)=\lambda_\alpha(T)\le t\). Hence \(\mu_t(T)\le\alpha\).

*Step 2.* Let \(\varepsilon>0\). Choose \(e\) with \(eH\subseteq D(T)\), \(\tau(1-e)\le t\) and \(\|Te\|<\mu_t(T)+\varepsilon=\beta\). Then \(e\wedge1_{(\beta,\infty)}(|T|)=0\). Indeed, a unit vector \(\zeta\) in both ranges lies in \(D(T)\), and the spectral integral gives \(\|T\zeta\|=\||T|\zeta\|>\beta\), because the spectral measure of \(\zeta\) sits on \((\beta,\infty)\). But \(\|T\zeta\|=\|Te\zeta\|\le\|Te\|<\beta\). (We use \(\||T|\zeta\|\) rather than \(\langle T^*T\zeta,\zeta\rangle\), which would need \(\zeta\in D(T^*T)\).)

*Step 3.* By Fact 2.1(b), \(1_{(\beta,\infty)}(|T|)\precsim1-e\), so \(\lambda_\beta(T)\le\tau(1-e)\le t\) by Fact 2.1(a). Hence \(\alpha\le\beta=\mu_t(T)+\varepsilon\). Letting \(\varepsilon\to0\) and using Step 1 gives \(\mu_t(T)=\alpha\), and \(\lambda_{\mu_t(T)}(T)=\lambda_\alpha(T)\le t\). \(\square\)

**Theorem 9.2** (Monotone functions of measurable operators). Let \(0\le T\le S\) be \(\tau\)-measurable, and let \(f:[0,\infty)\to[0,\infty)\) be continuous and non-decreasing.

1. \(\tau(T)=\int_0^\infty\mu_t(T)\,dt\).
2. \(f(T)\) is \(\tau\)-measurable. For \(t>0\),
\[
\mu_t(f(T))=f(\mu_t(T))\ \text{ if }t<\tau(1),\qquad \mu_t(f(T))=0\ \text{ if }t\ge\tau(1).
\]
In particular \(\mu_t(f(T))=f(\mu_t(T))\) for all \(t>0\) if and only if \(f(0)=0\) or \(\tau(1)=\infty\).
3. \(\mu_t(T)\le\mu_t(S)\) for all \(t>0\).
4. \(\tau(f(T))\le\tau(f(S))\), and \(\tau(f(T))=\int_0^{\tau(1)}f(\mu_t(T))\,dt\).

The case distinction in (2) is needed. Take \(M=\mathbb C\) with \(\tau(1)=1\), \(T=0\), \(f\equiv1\) and \(t=1\). The projection \(e=0\) is allowed, since \(\tau(1-0)=1\le t\), so \(\mu_1(f(T))=\mu_1(1)=0\). But \(f(\mu_1(T))=f(0)=1\).

*Remark.* The identity \(\mu_t(f(T))=f(\mu_t(T))\) needs \(f(0)=0\) when \(\tau(1)<\infty\): the example above shows that it fails when \(f(0)>0\).

**Proof.** (1) This is the layer-cake formula (Fact 2.5(b)) with \(p=1\). It also follows from (9.1): \(\mu_t(T)>s\) exactly when \(t<\lambda_s(T)\), so the Lebesgue measure of \(\{t:\mu_t(T)>s\}\) is \(\lambda_s(T)\), and \(\int_0^\infty\lambda_s(T)\,ds=\tau(T)\) by Fact 2.4(a).

(2) For \(s\ge0\) the set \(U_s=\{\lambda\ge0:f(\lambda)>s\}\) is empty, or all of \([0,\infty)\), or an interval \((c_s,\infty)\), because \(f\) is continuous and non-decreasing. So \(\lambda_s(f(T))=\tau(1_{U_s}(T))\) is \(0\), \(\tau(1)\), or \(\lambda_{c_s}(T)\). If \(f\) is bounded, \(f(T)\in M\). If \(f\) is unbounded, then \(c_s\to\infty\) as \(s\to\infty\), so \(\lambda_s(f(T))\to0\), and \(f(T)\) is \(\tau\)-measurable by the spectral-tail criterion (Fact 2.3(f)).

Put \(m=\mu_t(T)\). *Upper bound.* \(\{f>f(m)\}\subseteq(m,\infty)\), so \(\lambda_{f(m)}(f(T))\le\lambda_m(T)\le t\), and (9.1) gives \(\mu_t(f(T))\le f(m)\). *Lower bound.* Let \(0\le s<f(m)\). If \(m>0\), continuity gives \(m'<m\) with \(f(m')>s\), so \(U_s\supseteq(m',\infty)\) and \(\lambda_s(f(T))\ge\lambda_{m'}(T)>t\) by (9.1). If \(m=0\), then \(U_s=[0,\infty)\) and \(\lambda_s(f(T))=\tau(1)\). So when \(\tau(1)>t\), no \(s<f(m)\) has \(\lambda_s(f(T))\le t\), and \(\mu_t(f(T))\ge f(m)\). When \(\tau(1)\le t\), every \(\lambda_s(f(T))\le\tau(1)\le t\), so \(\mu_t(f(T))=0\). Note that \(m>0\) forces \(\lambda_0(T)>t\), hence \(\tau(1)>t\).

(3) By Fact 2.4(b), \(\lambda_s(T)\le\lambda_s(S)\) for \(s>0\), and normality extends this to \(s=0\). Then (9.1) gives \(\mu_t(T)\le\mu_t(S)\).

(4) By Fact 2.4(a), \(\tau(f(T))=\int_0^\infty\lambda_s(f(T))\,ds\). The set \(U_s\) is the same for \(T\) and \(S\). By (3), \(\lambda_s(f(T))\le\lambda_s(f(S))\) for every \(s\), which gives the inequality. The formula follows from (1) applied to \(f(T)\) and from (2). \(\square\)

**Example 9.3** (Trace monotone, not operator monotone). Theorem 9.2(4) is a statement about traces, not about operators. In \(M_2(\mathbb C)\) with \(\operatorname{Tr}\), let
\[
T=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad S=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
Then \(S-T=\begin{pmatrix}1&1\\1&1\end{pmatrix}\ge0\), so \(0\le T\le S\). But \(S^2-T^2=\begin{pmatrix}4&3\\3&2\end{pmatrix}\) has determinant \(-1\), so \(T^2\not\le S^2\). Theorem 9.2(4) still gives \(\operatorname{Tr}(T^2)=1\le7=\operatorname{Tr}(S^2)\). The singular values are \((1,0)\) and \(\bigl((3+\sqrt5)/2,(3-\sqrt5)/2\bigr)\approx(2.618,0.382)\), and they are ordered term by term, as Theorem 9.2(3) says.

## 10. The layer-cake distance between spectral projections

The main result of this section, Theorem 10.4, compares the spectral projections of two self-adjoint elements \(h,k\) of \(L^2\). The idea is to look at \(h\) acting on the left of \(L^2\) and \(k\) acting on the right, at the same time. When both operators have finite spectrum, this joint picture is a finite table of numbers. Lemma 10.1 computes it exactly. The proof of Theorem 10.4 then passes to general \(h\) and \(k\) by approximation.

**Lemma 10.1** (A discrete joint distribution). Let \(h,k\in\mathfrak m_0\) be self-adjoint with finite spectrum. Write
\[
h=\sum_{i=1}^m\alpha_ip_i,\qquad k=\sum_{j=1}^n\beta_jq_j,
\]
where \(\alpha_1,\dots,\alpha_m\) are the distinct nonzero eigenvalues of \(h\) with spectral projections \(p_i\), and likewise for \(k\). Put \(\alpha_0=\beta_0=0\), \(p_0=1-\sum_{i\ge1}p_i\) and \(q_0=1-\sum_{j\ge1}q_j\). For every pair \((i,j)\neq(0,0)\) put \(c_{ij}=\tau(p_iq_j)\). Then:

1. \(\tau(p_i)<\infty\) for \(i\ge1\), \(\tau(q_j)<\infty\) for \(j\ge1\), and \(c_{ij}=\|p_iq_j\|_2^2\in[0,\infty)\).
2. \(\sum_{j=0}^nc_{ij}=\tau(p_i)\) for \(i\ge1\), and \(\sum_{i=0}^mc_{ij}=\tau(q_j)\) for \(j\ge1\).
3. For all real functions \(f,g\) on \(\mathbb R\) with \(f(0)=g(0)=0\),
\[
\|f(h)-g(k)\|_2^2=\sum_{(i,j)\neq(0,0)}\bigl(f(\alpha_i)-g(\beta_j)\bigr)^2c_{ij}.
\tag{10.1}
\]

**Proof.** (1) For \(i\ge1\), \(p_i\) lies under the support of \(h\), which has finite trace, so \(\tau(p_i)<\infty\). Then \(p_i=p_i^*p_i\in\mathfrak m_\tau\). Take a pair with \(i\ge1\). The cyclic rule \(\tau(ab)=\tau(ba)\) for \(a\in\mathfrak m_\tau\) and \(b\in M\) (Fact 2.4(c)) gives \(\tau(p_iq_j)=\tau(q_jp_i)\) and \(\tau(p_iq_jp_i)=\tau(q_jp_ip_i)=\tau(q_jp_i)\). Hence \(c_{ij}=\tau((q_jp_i)^*(q_jp_i))=\|q_jp_i\|_2^2\). The trace identity \(\tau(z^*z)=\tau(zz^*)\) turns this into \(\|p_iq_j\|_2^2\), a finite nonnegative number. If \(i=0\), then \(j\ge1\), and the same argument works with the roles of the two families exchanged.

(2) The trace is linear on \(\mathfrak m_\tau\). For \(i\ge1\), \(p_i=\sum_{j=0}^np_iq_j\) is a finite sum of elements of \(\mathfrak m_\tau\), since \(\mathfrak m_\tau\) is an ideal. The second formula is the same argument.

(3) Put \(F=f(h)=\sum_{i\ge1}f(\alpha_i)p_i\) and \(G=g(k)=\sum_{j\ge1}g(\beta_j)q_j\). The terms with index \(0\) drop out because \(f(0)=g(0)=0\). Both are self-adjoint elements of \(\mathfrak m_0\subseteq L^2\), and
\[
\|F-G\|_2^2=\tau(F^2)+\tau(G^2)-\tau(FG)-\tau(GF),
\]
with \(\tau(GF)=\tau(FG)\) by the cyclic rule. By (2),
\[
\tau(F^2)=\sum_{i\ge1}f(\alpha_i)^2\tau(p_i)=\sum_{i\ge1}\sum_{j\ge0}f(\alpha_i)^2c_{ij},\qquad
\tau(G^2)=\sum_{j\ge1}\sum_{i\ge0}g(\beta_j)^2c_{ij},
\]
and \(\tau(FG)=\sum_{i,j\ge1}f(\alpha_i)g(\beta_j)c_{ij}\). Since \(f(\alpha_0)=g(\beta_0)=0\), each of the three sums may be taken over all pairs \((i,j)\neq(0,0)\). Adding them gives (10.1). \(\square\)

**Remark 10.2** (The joint distribution and its axes). The table \((c_{ij})\) plays the part of a joint distribution of "\(h\) on the left, \(k\) on the right". In a standard form, such a joint distribution can be built as a measure for a normal positive functional given by its vector in the positive cone; see the lesson Joint spectral measures and commutator estimates in standard form. Here no such vector is available: the unit \(1\) is a vector of \(L^2\) only when \(\tau(1)<\infty\). That is why the pair \((0,0)\) is left out. The number \(\tau(p_0q_0)\) may be infinite, and it never matters, because every function we use vanishes at \((0,0)\). For all self-adjoint \(h,k\in L^2\), Theorem 10.9 below builds this joint distribution as a measure on \(\mathbb R^2\setminus\{(0,0)\}\).

The pairs on the two axes, \((i,0)\) and \((0,j)\), do matter. A joint distribution built only from the sums \(\sum_if_i(h)g_i(k)\), with \(f_i,g_i\) continuous and compactly supported in \((0,\infty)\), sees only the part of \(L^2\) on which \(h\), acting on the left, and \(k\), acting on the right, are both nonzero. Such a measure \(\mu\) on \((0,\infty)^2\) cannot give \(\|f(h)-g(k)\|_2^2=\int|f(x)-g(y)|^2\,d\mu(x,y)\) for all Borel functions (take \(f=1_{\{0\}}\) and \(g=0\)) as soon as \(h\) or \(k\) has a nonzero kernel. For the spectral projections \(E_{\sqrt a}\) used below, the part of \(E_{\sqrt a}(h)-E_{\sqrt a}(k)\) that it misses is nonzero for some \(a>0\) exactly when \(h\) and \(k\) have different supports. For example, take \(M=\mathbb C\), \(h=1\), \(k=0\). Every such sum vanishes, because every \(g_i(0)\) is \(0\), so \(\mu=0\). But \(\|E_{\sqrt a}(h)-E_{\sqrt a}(k)\|_2^2=1\) for \(0<a\le1\). In (10.1) this mass is visible: it sits in the pairs \((i,0)\) and \((0,j)\), on the two axes.

For \(a>0\) let \(E_a=1_{[a,\infty)}\). For a real number \(s\) and \(a>0\) put
\[
G_a(s)=\operatorname{sgn}(s)\,1_{[a,\infty)}(s^2).
\]
So \(G_a(s)=E_{\sqrt a}(s)\) when \(s\ge0\). For self-adjoint \(h\), \(G_a(h)=1_{[\sqrt a,\infty)}(h)-1_{(-\infty,-\sqrt a]}(h)\).

**Lemma 10.3** (A scalar identity). For real \(s,t\) put \(I(s,t)=\int_0^\infty\bigl(G_a(s)-G_a(t)\bigr)^2\,da\). Then
\[
I(s,t)=\begin{cases}|s^2-t^2|,& st\ge0,\\ m^2+3n^2,& st<0,\end{cases}
\qquad m=\max(|s|,|t|),\ n=\min(|s|,|t|).
\tag{10.2}
\]
Consequently
\[
I(s,t)\le|s-t|\,(|s|+|t|)\ \text{ for all }s,t,\qquad
(s-t)^2\le I(s,t)\ \text{ when }st\ge0.
\tag{10.3}
\]

**Proof.** If \(st\ge0\), the numbers \(G_a(s)\) and \(G_a(t)\) are \(0\) or have one common sign. Their difference squared is \(1\) when \(a\) lies in \((\min(s^2,t^2),\max(s^2,t^2)]\), and \(0\) otherwise. So \(I(s,t)=|s^2-t^2|\). Since \(s\) and \(t\) do not have opposite signs, \(|s^2-t^2|=\bigl||s|-|t|\bigr|(|s|+|t|)=|s-t|(|s|+|t|)\). Also \((s-t)^2=|s-t|\,|s-t|\le|s-t|(|s|+|t|)\). If \(st<0\), the difference is \(\pm2\) for \(0<a\le n^2\), it is \(\pm1\) for \(n^2<a\le m^2\), and it is \(0\) for \(a>m^2\). So \(I(s,t)=4n^2+(m^2-n^2)=m^2+3n^2\). In this case \(|s-t|=m+n\), and \((m+n)^2-(m^2+3n^2)=2n(m-n)\ge0\). \(\square\)

**Theorem 10.4** (The layer-cake distance between spectral projections).

1. Let \(h\in L^2(M,\tau)\) be self-adjoint. For \(a>0\), \(G_a(h)\in\mathfrak m_0\). The function \(a\mapsto\|G_a(h)\|_2^2\) does not increase, and
\[
\int_0^\infty\|G_a(h)\|_2^2\,da=\|h\|_2^2.
\tag{10.4}
\]
In particular \(\int_0^\infty\|E_{\sqrt a}(h)\|_2^2\,da=\|h\|_2^2\) for \(h\in L^2(M,\tau)_+\).
2. Let \(h,k\in L^2(M,\tau)\) be self-adjoint. The function \(a\mapsto\|G_a(h)-G_a(k)\|_2^2\) is Lebesgue measurable, and
\[
\int_0^\infty\|G_a(h)-G_a(k)\|_2^2\,da\le\|h-k\|_2\,\bigl\||h|+|k|\bigr\|_2.
\tag{10.5}
\]
3. Let \(h,k\in L^2(M,\tau)_+\). Then
\[
\|h-k\|_2^2\ \le\ \int_0^\infty\|E_{\sqrt a}(h)-E_{\sqrt a}(k)\|_2^2\,da\ \le\ \|h-k\|_2\,\|h+k\|_2.
\tag{10.6}
\]
4. Both inequalities in (10.6) are sharp. Positivity cannot be dropped from the right inequality. On \(M=\mathbb C\) with \(\tau(1)=1\), take \(h=1\) and \(k=-1\). The middle term of (10.6) is \(1\), and the right side is \(2\cdot0=0\).

*Remark.* The right inequality of (10.6) needs \(h,k\ge0\) (part 4). The joint distribution has to include its mass on the axes (Remark 10.2).

**Proof.** *Step 1: the identity (10.4).* Let \(\nu\) be the measure \(B\mapsto\tau(1_B(h))\) on the Borel sets of \(\mathbb R\setminus\{0\}\). By Fact 2.4(a) applied to the positive measurable operator \(h^2\), \(\int t^2\,d\nu(t)=\tau(h^2)=\|h\|_2^2<\infty\). The point \(0\) contributes nothing to this integral. Hence \(\nu(\{t^2\ge a\})\le\|h\|_2^2/a\) for \(a>0\). So \(G_a(h)\) is a bounded operator whose support \(1_{\{t^2\ge a\}}(h)\) has finite trace, which means \(G_a(h)\in\mathfrak m_0\). Since \(G_a(h)^2=1_{\{t^2\ge a\}}(h)\), we get \(\|G_a(h)\|_2^2=\nu(\{t^2\ge a\})\), and this does not increase in \(a\). The measure \(\nu\) is \(\sigma\)-finite, so Tonelli's theorem gives \(\int_0^\infty\nu(\{t^2\ge a\})\,da=\int t^2\,d\nu(t)=\|h\|_2^2\).

*Step 2: finite spectrum.* Let \(h,k\in\mathfrak m_0\) be self-adjoint with finite spectrum, with the notation of Lemma 10.1. Apply (10.1) with \(f=g=G_a\):
\[
\|G_a(h)-G_a(k)\|_2^2=\sum_{(i,j)\neq(0,0)}\bigl(G_a(\alpha_i)-G_a(\beta_j)\bigr)^2c_{ij}.
\]
As a function of \(a\), this is a finite sum of nonnegative multiples of indicator functions of intervals. It is measurable, and its integral is \(\sum I(\alpha_i,\beta_j)c_{ij}\). Next apply (10.1) with \(f=g=\mathrm{id}\), and with \(f=|\cdot|\), \(g=-|\cdot|\):
\[
\|h-k\|_2^2=\sum(\alpha_i-\beta_j)^2c_{ij},\qquad \bigl\||h|+|k|\bigr\|_2^2=\sum(|\alpha_i|+|\beta_j|)^2c_{ij}.
\]
By (10.3) and the Cauchy–Schwarz inequality for sums with weights \(c_{ij}\ge0\),
\[
\sum I(\alpha_i,\beta_j)c_{ij}\le\sum|\alpha_i-\beta_j|(|\alpha_i|+|\beta_j|)c_{ij}\le\|h-k\|_2\,\bigl\||h|+|k|\bigr\|_2.
\]
If \(h,k\ge0\), every product \(\alpha_i\beta_j\) is \(\ge0\), so (10.3) also gives \(\sum I(\alpha_i,\beta_j)c_{ij}\ge\sum(\alpha_i-\beta_j)^2c_{ij}=\|h-k\|_2^2\). So (10.5) and (10.6) hold in this case. For positive \(h,k\) we have \(G_a=E_{\sqrt a}\) on the spectra and \(|h|+|k|=h+k\).

*Step 3: approximation.* For \(n\ge1\) and real \(t\) put
\[
\varphi_n(t)=\operatorname{sgn}(t)\,2^{-n}\bigl\lfloor2^n\min(|t|,n)\bigr\rfloor .
\]
Each \(\varphi_n\) takes finitely many values, vanishes when \(|t|<2^{-n}\), and satisfies \(|\varphi_n(t)|\le|t|\). Also \(\operatorname{sgn}\varphi_n(t)=\operatorname{sgn}t\) whenever \(\varphi_n(t)\neq0\), \(|\varphi_n(t)|\) increases with \(n\), and \(\varphi_n(t)\to t\). For self-adjoint \(h\in L^2\) put \(h_n=\varphi_n(h)\). The nonzero spectral projections of \(h_n\) lie under \(1_{\{t^2\ge4^{-n}\}}(h)\), which has finite trace by Step 1. So \(h_n\) is a self-adjoint element of \(\mathfrak m_0\) with finite spectrum, and \(h_n\ge0\) when \(h\ge0\). With \(\nu\) as in Step 1:

- (i) \(\|h-h_n\|_2^2=\int(t-\varphi_n(t))^2\,d\nu(t)\to0\) and \(\||h|-|h_n|\|_2^2=\int(|t|-|\varphi_n(t)|)^2\,d\nu(t)\to0\). This is dominated convergence with majorant \(t^2\).
- (ii) Let \(a>0\) with \(\nu(\{\sqrt a,-\sqrt a\})=0\). Then \(\|G_a(h_n)-G_a(h)\|_2^2=\int\bigl(G_a(\varphi_n(t))-G_a(t)\bigr)^2d\nu(t)\to0\). Indeed the integrand vanishes where \(t^2<a\), because both terms are \(0\) there. It is at most \(4\) where \(t^2\ge a\). Where \(t^2>a\), it is \(0\) for large \(n\), since then \(|\varphi_n(t)|\ge\sqrt a\) and the signs agree. The majorant \(4\cdot1_{\{t^2\ge a\}}\) is \(\nu\)-integrable.
- (iii) \(\|G_a(h_n)\|_2^2\le\nu(\{t^2\ge a\})\), because \(|\varphi_n(t)|\le|t|\).

A \(\sigma\)-finite measure has at most countably many points of positive mass. So (ii) holds for all \(a>0\) outside a countable set.

Now take \(h,k\) and approximate both. Put \(\Phi_n(a)=\|G_a(h_n)-G_a(k_n)\|_2^2\) and \(\Phi(a)=\|G_a(h)-G_a(k)\|_2^2\). By (ii) and the triangle inequality in \(L^2\), \(\Phi_n(a)\to\Phi(a)\) for all \(a\) outside a countable set, so \(\Phi\) is measurable. By (iii),
\[
0\le\Phi_n(a)\le2\|G_a(h_n)\|_2^2+2\|G_a(k_n)\|_2^2\le2\nu_h(\{t^2\ge a\})+2\nu_k(\{t^2\ge a\}),
\]
and the right side has integral \(2\|h\|_2^2+2\|k\|_2^2<\infty\) by Step 1. Dominated convergence gives \(\int\Phi=\lim\int\Phi_n\). By Step 2, \(\int\Phi_n\le\|h_n-k_n\|_2\,\||h_n|+|k_n|\|_2\), and for positive \(h,k\) also \(\int\Phi_n\ge\|h_n-k_n\|_2^2\). By (i) these bounds converge to the same expressions for \(h\) and \(k\). This proves (10.5) and (10.6).

*Step 4: sharpness.* Let \(e,f\) be projections of finite trace. Then \(E_{\sqrt a}(e)=e\) for \(0<a\le1\) and \(E_{\sqrt a}(e)=0\) for \(a>1\), and the same holds for \(f\). So the middle term of (10.6) is \(\|e-f\|_2^2\), and the left inequality is an equality. For \(M=\mathbb C\), \(h=1\) and \(k=0\), all three terms of (10.6) equal \(1\). For the example in part 4, \(E_{\sqrt a}(1)=1\) and \(E_{\sqrt a}(-1)=0\) for \(0<a\le1\), while both vanish for \(a>1\). \(\square\)

**Remark 10.5.** For \(h\ge0\), (10.4) is the layer-cake formula of Fact 2.5(b) with \(p=2\), after the substitution \(a=s^2\), because \(1_{[s,\infty)}(h)\) and \(1_{(s,\infty)}(h)\) differ for at most countably many \(s\). In a standard form, the analogous estimate holds for bounded operators and a normal positive functional, with the same scalar function \(I(s,t)\) of (10.2); see Joint spectral measures and commutator estimates in standard form.

**Example 10.6** (Two lines in \(\mathbb C^2\)). Let \(M=M_2(\mathbb C)\) with \(\tau=\operatorname{Tr}\). Let \(e\) project onto \((1,0)\) and \(f\) onto \((\cos\theta,\sin\theta)\). By Step 4 of the proof of Theorem 10.4, the middle term of (10.6) is \(\|e-f\|_2^2=\operatorname{Tr}(e)+\operatorname{Tr}(f)-2\operatorname{Tr}(ef)=2\sin^2\theta\). So the lower bound is attained. For the upper bound, \(\|e+f\|_2^2=2+2\cos^2\theta\), and \(\|e-f\|_2\|e+f\|_2=2|\sin\theta|(1+\cos^2\theta)^{1/2}\). As \(\theta\to0\), the middle term is about \(2\theta^2\) and the upper bound about \(2\sqrt2|\theta|\). At \(\theta=\pi/2\) all three terms equal \(2\).

**Example 10.7** (Kernels and signs). On \(M=\mathbb C\) with \(\tau(1)=1\): for \(h=1\), \(k=0\), all three terms of (10.6) equal \(1\), and all of this mass sits on an axis of the joint distribution (Remark 10.2). For \(h=1\), \(k=-1\), the unsigned middle term is \(1\) while \(\|h-k\|_2\|h+k\|_2=0\). The signed form gives \(G_a(1)-G_a(-1)=2\) for \(0<a\le1\), so the left side of (10.5) is \(4\). The right side is \(\|h-k\|_2\,\||h|+|k|\|_2=2\cdot2=4\). So (10.5) is sharp here.

### The joint distribution of a left and a right multiplication

In this subsection \(h,k\in L^2(M,\tau)\) are self-adjoint. For a Borel set \(A\subseteq\mathbb R\) we write
\(1_A(h)\) for the spectral projection \(1_A(T_h)\), and \(f(h)=f(T_h)\) for a bounded Borel function \(f\); these lie in
\(M\) (Spectral calculus with its domains retained, SK-08). As in Step 1 of the proof of Theorem
10.4, \(\nu_h(A)=\tau(1_A(h))\) is a measure on the Borel sets of \(\mathbb R\setminus\{0\}\), and
\(\int t^2\,d\nu_h(t)=\|h\|_2^2\).

**Lemma 10.8** (The joint spectral measure). There is a projection-valued measure \(E\) on the Borel sets of
\(\mathbb R^2\), acting on \(L^2(M,\tau)\), with
\[
E(A\times B)\xi=1_A(h)\,\xi\,1_B(k)\qquad(\xi\in L^2)
\tag{10.7}
\]
for all Borel sets \(A,B\subseteq\mathbb R\). For bounded Borel functions \(f,g\) on \(\mathbb R\),
\(\int f(s)\,dE(s,t)=L_{f(h)}\) and \(\int g(t)\,dE(s,t)=R_{g(k)}\).

**Proof.** Put \(\varphi(t)=t/(1+|t|)\), a homeomorphism of \(\mathbb R\) onto \((-1,1)\), and \(a=\varphi(h)\),
\(b=\varphi(k)\), self-adjoint contractions in \(M\). By the change of variables (SK.15) of SK-07,
\(1_{A'}(a)=1_{\varphi^{-1}(A')}(h)\) for every Borel \(A'\subseteq\mathbb R\), and likewise for \(b\). The operators
\(L_a\) and \(R_b\) are commuting bounded self-adjoint operators on \(L^2\) (Fact 2.6(e)), so \(T=L_a+iR_b\) is a
bounded normal operator. Let \(\Phi\) be its bounded Borel calculus on \(\sigma(T)\subseteq\mathbb C=\mathbb R^2\)
(SK-04), and \(F(S)=\Phi(1_{S\cap\sigma(T)})\) for Borel \(S\subseteq\mathbb R^2\). The map
\(f\mapsto\Phi(f\circ\operatorname{Re})\) on bounded Borel functions on \(\mathbb R\) is a unital \(*\)-homomorphism
that preserves bounded pointwise sequential limits, and it equals \(f(\operatorname{Re}T)\) for continuous \(f\): both
sides agree for polynomials and are norm limits of them. By the uniqueness in SK-04 it is the Borel calculus of
\(L_a=\operatorname{Re}T\). The same holds for \(\operatorname{Im}\) and \(R_b\). Hence
\(F(A'\times B')=1_{A'}(L_a)1_{B'}(R_b)\). Since \(L\) is a normal representation, \(1_{A'}(L_a)=L_{1_{A'}(a)}\) (Fact
2.6(e) and Fact 2.7(c)). Since \(R_b=J_\tau L_bJ_\tau\) with \(J_\tau\) antiunitary,
\(1_{B'}(R_b)=J_\tau L_{1_{B'}(b)}J_\tau=R_{1_{B'}(b)}\) (Fact 2.6(e) and (SK.23) of SK-08). As
\(1_{\mathbb R\setminus(-1,1)}(a)=1_\emptyset(h)=0\), and likewise for \(b\), the projection-valued measure \(F\) is
carried by the open square \((-1,1)^2\). The map \(\varphi\times\varphi\) is a homeomorphism of \(\mathbb R^2\) onto
that square, so \(E(S)=F((\varphi\times\varphi)(S))\) is a projection-valued measure on \(\mathbb R^2\), and (10.7)
follows from \(1_{\varphi(A)}(a)=1_A(h)\) and \(1_{\varphi(B)}(b)=1_B(k)\). The two integrals agree with \(L_{f(h)}\)
and \(R_{g(k)}\) on indicator functions, by (10.7), hence on simple functions, and all four are norm continuous for
uniform convergence of \(f\) and \(g\). \(\square\)

The same construction, for bounded \(h\) and \(k\) and a vector of a standard form, is the proof of Joint spectral
measures and commutator estimates in standard form, NC-20.

**Theorem 10.9** (The joint distribution). There is a unique measure \(\mu=\mu_{h,k}\) on the Borel sets of
\(\mathbb R^2\setminus\{(0,0)\}\) such that
\[
\mu(A\times B)=\tau\bigl(1_B(k)\,1_A(h)\,1_B(k)\bigr)\in[0,\infty]
\tag{10.8}
\]
for all Borel sets \(A,B\subseteq\mathbb R\) with \(0\notin A\) or \(0\notin B\). It is \(\sigma\)-finite, and:

1. \(\mu(A\times\mathbb R)=\nu_h(A)\) and \(\mu(\mathbb R\times A)=\nu_k(A)\) for Borel sets
   \(A\subseteq\mathbb R\setminus\{0\}\).
2. Let \(f,g\) be Borel functions on \(\mathbb R\) with \(f(0)=g(0)=0\), \(\int|f|^2\,d\nu_h<\infty\) and
   \(\int|g|^2\,d\nu_k<\infty\). Then \(f(h)=f(T_h)\) and \(g(k)=g(T_k)\) lie in \(L^2(M,\tau)\), and
\[
\|f(h)-g(k)\|_2^2=\int_{\mathbb R^2\setminus\{(0,0)\}}|f(s)-g(t)|^2\,d\mu(s,t).
\tag{10.9}
\]
3. In the setting of Lemma 10.1, \(\mu\) is the measure with mass \(c_{ij}\) at \((\alpha_i,\beta_j)\) for
   \((i,j)\neq(0,0)\).
4. If \(h,k\ge0\), then \(\mu\) is carried by \([0,\infty)^2\setminus\{(0,0)\}\).

**Proof.** *Construction.* For \(n\ge1\) let \(A_n=\{t\in\mathbb R:|t|\ge1/n\}\), \(e_n=1_{A_n}(h)\),
\(e_n'=1_{A_n}(k)\) and \(r_n=e_n\vee e_n'\). By Step 1 of the proof of Theorem 10.4, \(\tau(e_n)\le n^2\|h\|_2^2\) and
\(\tau(e_n')\le n^2\|k\|_2^2\), so \(\tau(r_n)<\infty\) (Fact 2.1(b)) and \(r_n\in L^2\). Let
\(\Omega_n=(A_n\times\mathbb R)\cup(\mathbb R\times A_n)\); these sets increase to \(\mathbb R^2\setminus\{(0,0)\}\).
Let \(\mu_n(S)=\|E(S)r_n\|_2^2\), a finite measure on \(\mathbb R^2\).

We claim that \(\mu_m(S)=\mu_n(S)\) for \(m\ge n\) and Borel \(S\subseteq\Omega_n\). If \(S\subseteq A_n\times\mathbb R\),
then \(E(S)=E(S)E(A_n\times\mathbb R)\), and \(E(A_n\times\mathbb R)r_m=e_nr_m=e_n\) by (10.7), because
\(e_n\le e_m\le r_m\). So \(E(S)r_m=E(S)e_n\), and in the same way \(E(S)r_n=E(S)e_n\). If \(S\subseteq\mathbb R\times A_n\),
then \(E(\mathbb R\times A_n)r_m=r_me_n'=e_n'\) gives \(E(S)r_m=E(S)e_n'=E(S)r_n\). A Borel subset of \(\Omega_n\) is the
disjoint union of a set of each kind.

Put \(\Omega_0=\emptyset\). By the claim, for Borel \(S\subseteq\mathbb R^2\setminus\{(0,0)\}\),
\[
\mu_n(S\cap\Omega_n)=\sum_{l=1}^n\mu_l\bigl(S\cap(\Omega_l\setminus\Omega_{l-1})\bigr).
\]
So \(\mu(S)=\sum_{l\ge1}\mu_l(S\cap(\Omega_l\setminus\Omega_{l-1}))\) is a countable sum of measures, hence a measure; it
agrees with \(\mu_n\) on the Borel subsets of \(\Omega_n\), and \(\mu(\Omega_n)\le\|r_n\|_2^2=\tau(r_n)<\infty\). So
\(\mu\) is \(\sigma\)-finite.

*Rectangles.* Let \(A,B\subseteq\mathbb R\) be Borel. If \(A\subseteq A_n\), then \(A\times B\subseteq\Omega_n\), and
by (10.7) and \(1_A(h)e_n=1_A(h)\),
\[
\mu(A\times B)=\|1_A(h)e_n1_B(k)\|_2^2=\|1_A(h)1_B(k)\|_2^2=\tau\bigl(1_B(k)1_A(h)1_B(k)\bigr).
\]
If \(B\subseteq A_n\), the same computation with \(e_n'\) gives the same formula. Now let \(0\notin A\). The sets
\(A\cap A_n\) increase to \(A\), so \(1_{A\cap A_n}(h)\uparrow1_A(h)\) strongly, and
\(1_B(k)1_{A\cap A_n}(h)1_B(k)\uparrow1_B(k)1_A(h)1_B(k)\). Continuity of \(\mu\) from below and normality of \(\tau\)
give (10.8). Let \(0\notin B\). For \(z_n=1_A(h)1_{B\cap A_n}(k)\),
\(\mu(A\times(B\cap A_n))=\tau(z_n^*z_n)=\tau(z_nz_n^*)=\tau(1_A(h)1_{B\cap A_n}(k)1_A(h))\). This increases to
\(\tau(1_A(h)1_B(k)1_A(h))\) by normality, and that equals \(\tau(1_B(k)1_A(h)1_B(k))\), by \(\tau(z^*z)=\tau(zz^*)\) for
\(z=1_B(k)1_A(h)\).

*Uniqueness.* A measure with (10.8) is finite on \(A_n\times\mathbb R\) and on \((\mathbb R\setminus A_n)\times A_n\),
and its values on the rectangles contained in each of these two sets are fixed by (10.8). These rectangles are closed
under finite intersections and generate the Borel sets of each of the two sets. So the measure is fixed on both sets
([Fremlin, Measure Theory, Volume 1, Corollary 136C](https://www1.essex.ac.uk/maths/people/fremlin/cont13.htm), free; Volumes 1 and 2 are the core course [Measure and
Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)). The two sets partition
\(\Omega_n\), and \(\Omega_n\uparrow\mathbb R^2\setminus\{(0,0)\}\).

(1) Take \(B=\mathbb R\), or \(A=\mathbb R\), in (10.8).

(2) First let \(f\) and \(g\) be bounded and vanish on \((-1/n,1/n)\). Then \(f(h)=f(h)e_n\) and \(g(k)=e_n'g(k)\) are
bounded with supports of finite trace, so they lie in \(L^2\). Since \(e_n,e_n'\le r_n\), Lemma 10.8 gives
\[
f(h)-g(k)=L_{f(h)}r_n-R_{g(k)}r_n=\Bigl(\int\bigl(f(s)-g(t)\bigr)\,dE(s,t)\Bigr)r_n ,
\]
so \(\|f(h)-g(k)\|_2^2=\int|f(s)-g(t)|^2\,d\mu_n(s,t)\) by (SK.6) of SK-04. The integrand
vanishes off \(\Omega_n\), and \(\mu_n=\mu\) on \(\Omega_n\). This is (10.9).

In general, let \(u\) be a Borel function with \(u(0)=0\) and \(\int|u|^2\,d\nu_h<\infty\). The operator \(u(T_h)\) is
closed, densely defined and affiliated with \(M\) (SK-05, SK-08), and
\(\tau(1_{(R,\infty)}(|u(T_h)|))=\nu_h(\{|u|>R\})\le R^{-2}\int|u|^2\,d\nu_h<\infty\) for \(R>0\), by (SK.15). By the
spectral-tail criterion (Fact 2.3(f)) it is \(\tau\)-measurable; we write \(u(h)\) for it. By Fact 2.4(a), applied to
\(|u(h)|^2=|u|^2(T_h)\) with (SK.15), \(\|u(h)\|_2^2=\int|u|^2\,d\nu_h\); the point \(0\) contributes nothing, since
\(u(0)=0\). Now put \(f_n=f1_{A_n}1_{\{|f|\le n\}}\) and \(g_n=g1_{A_n}1_{\{|g|\le n\}}\). Then \(f-f_n\) is a Borel
function vanishing at \(0\), and \(f(h)-f_n(h)=(f-f_n)(h)\) because \(f_n\) is bounded (SK-05). So
\(\|f(h)-f_n(h)\|_2^2=\int|f-f_n|^2\,d\nu_h\to0\) by dominated convergence, and likewise for \(g\). On the other side, by
(1) and because \(f\) and \(f_n\) vanish at \(0\), \(\int|f(s)-f_n(s)|^2\,d\mu(s,t)=\int|f-f_n|^2\,d\nu_h\to0\), and
likewise for \(g\). So \(f_n(s)-g_n(t)\to f(s)-g(t)\) in \(L^2(\mu)\), and \(f_n(h)-g_n(k)\to f(h)-g(k)\) in \(L^2\).
Formula (10.9) for \(f_n,g_n\) passes to the limit.

(3) By (1), \(\mu\) vanishes on \((\mathbb R\setminus\{\alpha_0,\dots,\alpha_m\})\times\mathbb R\) and on
\(\mathbb R\times(\mathbb R\setminus\{\beta_0,\dots,\beta_n\})\), so it is carried by the points
\((\alpha_i,\beta_j)\neq(0,0)\). By (10.8) and Lemma 10.1(1), the mass at \((\alpha_i,\beta_j)\) is
\(\tau(q_jp_iq_j)=\|p_iq_j\|_2^2=c_{ij}\).

(4) If \(h\ge0\), then \(\nu_h((-\infty,0))=0\), so \(\mu((-\infty,0)\times\mathbb R)=0\) by (1); likewise for \(k\).
\(\square\)

**Corollary 10.10** (Theorem 10.4 from the joint distribution). For self-adjoint \(h,k\in L^2(M,\tau)\), the function
\(a\mapsto\|G_a(h)-G_a(k)\|_2^2\) is Borel on \((0,\infty)\), and
\[
\int_0^\infty\|G_a(h)-G_a(k)\|_2^2\,da=\int_{\mathbb R^2\setminus\{(0,0)\}}I(s,t)\,d\mu_{h,k}(s,t),
\]
with \(I\) as in Lemma 10.3. This gives a second proof of (10.5) and (10.6).

**Proof.** \(G_a\) vanishes at \(0\) and \(|G_a|\le1_{\{t^2\ge a\}}\), so (10.9) applies:
\(\|G_a(h)-G_a(k)\|_2^2=\int(G_a(s)-G_a(t))^2\,d\mu(s,t)\). The function \((a,s,t)\mapsto(G_a(s)-G_a(t))^2\) is Borel,
because \(\{(a,s):s^2\ge a\}\) is closed, and \(\mu\) is \(\sigma\)-finite. Tonelli's theorem (Fact 2.7(f)) gives the
measurability and the displayed identity. By (10.3), \(I(s,t)\le|s-t|(|s|+|t|)\). The Cauchy–Schwarz inequality in
\(L^2(\mu)\), with (10.9) for \(f=g=\mathrm{id}\) and for \(f=|\cdot|\), \(g=-|\cdot|\), gives (10.5). If \(h,k\ge0\),
\(\mu\) is carried by \([0,\infty)^2\) (Theorem 10.9(4)), where \(st\ge0\) and \((s-t)^2\le I(s,t)\) by (10.3); with
(10.9) for \(f=g=\mathrm{id}\) this gives the left inequality of (10.6). \(\square\)

## 11. The commutant of the trace representation

By Fact 2.6(e), left multiplication \(\pi_\tau(a)=L_a\) is the GNS representation of \(\tau\), realized on \(L^2\). For \(b\in M\) put \(\rho(b)=R_b\), and let \(N=\pi_\tau(M)'\). This section shows that \(N\) consists of the right multiplications. This gives a trace on \(N\), and it lets right multiplication act on measurable operators.

**Theorem 11.1** (The commutation theorem for a trace).
\[
\pi_\tau(M)'=\rho(M),\qquad \rho(M)'=\pi_\tau(M).
\tag{11.1}
\]
The map \(\rho\) is a linear bijection of \(M\) onto \(N\), isometric, with \(\rho(ab)=\rho(b)\rho(a)\), \(\rho(a^*)=\rho(a)^*\) and \(\rho(M_+)=N_+\). It preserves suprema of bounded increasing nets, and \(J_\tau\pi_\tau(a)J_\tau=\rho(a^*)\). Hence \(\tau_N=\tau\circ\rho^{-1}\) is a faithful normal semifinite trace on \(N\). This is the trace opposite to \(\tau\).

**Proof.** Left and right multiplications commute (Fact 2.6(e)), so \(\rho(M)\subseteq\pi_\tau(M)'\). Let \(T\in\pi_\tau(M)'\).

*Step 1.* Let \(e\in\mathcal E\), so \(e\in\mathfrak m_0\subseteq L^2\). Put \(b_e=T(e)\in L^2\). For \(a\in M\), \(T(ae)=T(L_ae)=ab_e\). With \(a=e\), \(b_e=T(ee)=eb_e\). Also \(\|ab_e\|_2\le\|T\|\,\|ae\|_2\) for all \(a\in M\).

*Step 2: \(b_e\) is bounded.* Let \(k=|b_e^*|\in L^2_+\). Take \(R>\|T\|\) and \(q=1_{(R,\infty)}(k)\). By the Markov estimate (Fact 2.5(d)), \(\tau(q)\le\|k\|_2^2/R^2<\infty\). Step 1 with \(a=q\) gives \(\|qb_e\|_2^2\le\|T\|^2\|qe\|_2^2\). The trace identity \(\tau(x^*x)=\tau(xx^*)\) (Fact 2.4(b)) gives \(\|qe\|_2^2=\tau(eqe)=\tau(qeq)\le\tau(q)\), and
\[
\|qb_e\|_2^2=\tau\bigl((qb_e)(qb_e)^*\bigr)=\tau(qk^2q)=\tau(k^21_{(R,\infty)}(k))\ge R^2\tau(q).
\]
So \(R^2\tau(q)\le\|T\|^2\tau(q)\), with \(\tau(q)\) finite. Hence \(\tau(q)=0\) and \(q=0\). So \(k\) is bounded by \(\|T\|\), and the polar decomposition \(b_e^*=wk\) (Fact 2.3(g)), with \(w\in M\), shows \(b_e\in M\) with \(\|b_e\|\le\|T\|\).

*Step 3: compatibility.* If \(e\le f\) in \(\mathcal E\), then \(b_e=T(ef)=eb_f\), so \(b_e^*=b_f^*e\).

*Step 4: one operator.* The union \(U\) of the subspaces \(fH\), \(f\in\mathcal E\), is a linear subspace, since \(\mathcal E\) is directed. It is dense, since \(f\uparrow1\) along \(\mathcal E\) (Fact 2.1(e)). For \(\xi\in fH\) put \(B\xi=b_f^*\xi\). This is well defined: if \(\xi\in fH\cap f'H\), take \(g\in\mathcal E\) above \(f\) and \(f'\); by Step 3, \(b_f^*\xi=b_g^*f\xi=b_g^*\xi\), and similarly for \(f'\). Also \(\|B\xi\|\le\|T\|\|\xi\|\). So \(B\) extends to a bounded operator. For \(\xi\in H\), \(b_f^*\xi=b_f^*f\xi=B(f\xi)\to B\xi\) along \(\mathcal E\). So \(B\) is a strong limit of elements of \(M\), and \(B\in M\). Put \(b=B^*\). Then \(b_e^*=Be\), that is, \(b_e=eb\) for every \(e\in\mathcal E\).

*Step 5.* For \(a\in M\) and \(e\in\mathcal E\), \(T(ae)=ab_e=aeb=R_b(ae)\). Every \(x\in\mathfrak m_0\) has the form \(x=xe\), with \(e\) its right support. So \(T\) and \(R_b\) agree on \(\mathfrak m_0\), which is dense in \(L^2\) (Fact 2.6(a)). Hence \(T=R_b\), with \(\|b\|\le\|T\|\).

This proves \(\pi_\tau(M)'=\rho(M)\). By Fact 2.6(e), \(J_\tau\) is an antiunitary involution with \(J_\tau L_aJ_\tau=R_{a^*}\). So \(\rho(M)=J_\tau\pi_\tau(M)J_\tau\), and \(\rho(M)'=J_\tau\pi_\tau(M)'J_\tau=J_\tau\rho(M)J_\tau=\pi_\tau(M)\).

The identities \(\rho(ab)=\rho(b)\rho(a)\) and \(\rho(a^*)=\rho(a)^*\) are associativity and the rule \(R_b^*=R_{b^*}\) (Fact 2.6(e)). If \(R_b=0\), then \(eb=R_b(e)=0\) for all \(e\in\mathcal E\), so \(b=0\). Applying Steps 1–5 to \(T=R_b\) gives \(\|b\|\le\|R_b\|\), and \(\|R_b\|\le\|b\|\) by the module estimate (Fact 2.6(a)). Next, \(\rho(a^*a)=\rho(a)\rho(a)^*\ge0\). Conversely, if \(\rho(a)\ge0\), then \(a=a^*\). Write \(a=a_+-a_-\) with \(a_\pm\ge0\) and \(a_+a_-=0\). Then \(\rho(a)=\rho(a_+)-\rho(a_-)\) with \(\rho(a_\pm)\ge0\) and \(\rho(a_+)\rho(a_-)=\rho(a_-a_+)=0\). By uniqueness of this decomposition, \(\rho(a_-)=0\), so \(a_-=0\). Thus \(\rho\) is an order isomorphism of the self-adjoint parts. The supremum of a bounded increasing net is its least upper bound, so \(\rho\) and \(\rho^{-1}\) preserve suprema. Finally, \(\tau_N(\rho(c)^*\rho(c))=\tau(cc^*)=\tau(c^*c)=\tau_N(\rho(c)\rho(c)^*)\). Normality, faithfulness and semifiniteness pass through \(\rho\). \(\square\)

**Theorem 11.2** (The opposite measurable algebra). The map \(\rho\) of Theorem 11.1 extends uniquely to a bijection \(\widehat\rho:S(M,\tau)\to S(N,\tau_N)\). This extension is a homeomorphism for the measure topologies, and it satisfies
\[
\widehat\rho(x+y)=\widehat\rho(x)+\widehat\rho(y),\qquad \widehat\rho(xy)=\widehat\rho(y)\widehat\rho(x),\qquad \widehat\rho(x^*)=\widehat\rho(x)^*.
\]
Moreover:

1. \(\widehat\rho(S(M,\tau)_+)=S(N,\tau_N)_+\). For \(h\in S(M,\tau)_+\) and Borel \(B\subseteq[0,\infty)\), \(\widehat\rho(1_B(h))=1_B(\widehat\rho(h))\), and \(\tau_N(\widehat\rho(h))=\tau(h)\).
2. \(|\widehat\rho(x)|=\widehat\rho(|x^*|)\), and \(\widehat\rho\) maps \(L^p(M,\tau)\) isometrically onto \(L^p(N,\tau_N)\) for \(1\le p<\infty\).
3. For \(h\in S(M,\tau)\), the operator \(\widehat\rho(h)\) on \(L^2\) is right multiplication by \(h\):
\[
D(\widehat\rho(h))=\{x\in L^2:\ xh\in L^2\},\qquad \widehat\rho(h)x=xh,
\]
where \(xh\) is the product in \(S(M,\tau)\).

**Proof.** *Topology.* Every projection of \(N\) is \(\rho(p)\) for a projection \(p\) of \(M\), with \(\tau_N(1-\rho(p))=\tau(1-p)\) and \(\|\rho(x)\rho(p)\|=\|px\|\). So \(\rho(x)\in U_N(r,d)\) exactly when some \(p\) has \(\|px\|<r\) and \(\tau(1-p)<d\), that is, when \(x^*\in U_M(r,d)\). By Fact 2.2(a), \(U_M(r,d)^*=U_M(r,d)\). Hence \(\rho(U_M(r,d))=U_N(r,d)\), and \(\rho\) is a uniform isomorphism. It extends uniquely to a uniform isomorphism of the completions. Sums and adjoints pass to the limit by uniform continuity. For products, approximate \(x,y\) by sequences \(x_n,y_n\in M\). These are bounded in measure, and multiplication is continuous on bounded sets (Fact 2.2(b) and (c)). Then \(\widehat\rho(xy)=\lim\rho(y_n)\rho(x_n)=\widehat\rho(y)\widehat\rho(x)\).

*(1)* The positive elements are the elements \(b^*b\) (Fact 2.3(g)), and \(\widehat\rho(b^*b)=\widehat\rho(b)\widehat\rho(b)^*\ge0\); the same holds for \(\widehat\rho^{-1}\). Let \(h\ge0\) and \(r=(1+h)^{-1}\in M\). In \(S(M,\tau)\), \((1+h)r=r(1+h)=1\). Indeed, by Fact 2.3(d) the operators of both products are the closures of \((1+h)(1+h)^{-1}\) and \((1+h)^{-1}(1+h)\), and these are the identity. Apply \(\widehat\rho\): \(\rho(r)(1+\widehat\rho(h))=(1+\widehat\rho(h))\rho(r)=1\). The element \((1+\widehat\rho(h))^{-1}\in N\) satisfies the same identities, so associativity gives \(\rho(r)=(1+\widehat\rho(h))^{-1}\). On the abelian von Neumann algebra generated by \(r\), \(\rho\) is multiplicative and normal. A normal \(*\)-homomorphism commutes with the bounded Borel calculus. This holds for polynomials, then for continuous functions by norm limits, and then for all bounded Borel functions by monotone limits. The map \(\lambda\mapsto(1+\lambda)^{-1}\) is a bijection of \([0,\infty)\) onto \((0,1]\), and \(r\) has zero kernel, so \(1_B(h)=g_B(r)\) with \(g_B(s)=1_B(s^{-1}-1)\) on \((0,1]\) and \(g_B(0)=0\). Hence \(\rho(1_B(h))=g_B(\rho(r))=1_B(\widehat\rho(h))\). The spectral distributions agree, since \(\tau_N(1_B(\widehat\rho(h)))=\tau(1_B(h))\). So Fact 2.4(a) gives \(\tau_N(\widehat\rho(h))=\tau(h)\).

*(2)* \(\widehat\rho(x)^*\widehat\rho(x)=\widehat\rho(x^*)\widehat\rho(x)=\widehat\rho(xx^*)=\widehat\rho(|x^*|)^2\). By the uniqueness of positive square roots (Fact 2.3(g)), \(|\widehat\rho(x)|=\widehat\rho(|x^*|)\). By (1), \(\tau_N(|\widehat\rho(x)|^p)=\tau(|x^*|^p)=\tau(|x|^p)\). The last equality holds because \(|x|\) and \(|x^*|\) have the same nonzero spectral distribution (Fact 2.5(c)). Surjectivity follows by applying the same construction to \(\rho^{-1}\).

*(3)* First, the inclusion \(\iota:L^2\to S(M,\tau)\) is uniformly continuous when \(L^2\) carries the vector measure topology of \((N,\tau_N)\). By the description of projections of \(N\), \(\xi\in V_N(r,d)\) means \(\|\xi p\|_2<r\) and \(\tau(1-p)<d\) for some \(p\in\operatorname{Proj}(M)\). Write \(\xi=\xi p+\xi(1-p)\). By the Markov estimate and the attained cutoffs of Fact 2.5(a) and (d), \(\xi p\in\widetilde U(rt^{-1/2},2t)\) for every \(t>0\). Also \(\xi(1-p)p=0\), so \(\xi(1-p)\in\widetilde U(s,d)\) for every \(s>0\). Given \((r_0,d_0)\), take \(t=d=d_0/4\), \(s=r_0/2\) and \(r=r_0t^{1/2}/2\). Then \(\xi\in\widetilde U(r_0,d_0)\). So \(\iota\) extends continuously to a map \(\widehat\iota\) from the completion \(\widehat{L^2}{}^N\) into \(S(M,\tau)\).

Let \(x\in L^2\) and choose \(h_n\in M\) with \(h_n\to h\) in measure. Then \(\rho(h_n)x=xh_n\to\widehat\rho(h)x\) in \(\widehat{L^2}{}^N\) (Fact 2.2(c)), so \(xh_n\to\widehat\iota(\widehat\rho(h)x)\) in \(S(M,\tau)\). Also \(xh_n\to xh\) in \(S(M,\tau)\). So \(\widehat\iota(\widehat\rho(h)x)=xh\). If \(x\in D(\widehat\rho(h))\), then \(\widehat\rho(h)x\in L^2\), so \(xh=\widehat\rho(h)x\in L^2\). This shows that \(\widehat\rho(h)\) is contained in the operator \(R_h:x\mapsto xh\) on \(\{x\in L^2:xh\in L^2\}\). Now \(R_h\) is closed: if \(x_j\to x\) and \(x_jh\to z\) in \(L^2\), then both convergences hold in measure (Fact 2.6(a)), and continuity of multiplication gives \(xh=z\). \(R_h\) is densely defined, since it extends \(\widehat\rho(h)\). It is affiliated with \(N\): by (11.1), the unitaries of \(N'=\pi_\tau(M)\) are the \(L_u\), and \((ux)h=u(xh)\). By the maximality in Fact 2.3(c), applied to \((N,\tau_N)\), \(R_h=\widehat\rho(h)\). \(\square\)

## 12. The coupling trace on a commutant

Let \(\pi:M\to B(\mathcal K)\) be a normal unital \(*\)-representation. We do not assume that \(\pi\) is faithful. For two such representations \(\pi_1\) on \(\mathcal K_1\) and \(\pi_2\) on \(\mathcal K_2\), let
\[
L_M(\mathcal K_1,\mathcal K_2)=\{y\in B(\mathcal K_1,\mathcal K_2):\ y\pi_1(a)=\pi_2(a)y\ \text{for all }a\in M\}.
\]
When \(\mathcal K_1=L^2\) we use \(\pi_1=\pi_\tau\). Taking adjoints, \(y^*\in L_M(\mathcal K_2,\mathcal K_1)\). Hence \(yy^*\in\pi_2(M)'\) and \(y^*y\in\pi_1(M)'\). For \(\mathcal K_1=L^2\), \(y^*y\in N\).

**Lemma 12.1** (Cyclic pieces). Let \(\zeta\in\mathcal K\). There is a unique \(h_\zeta\in L^2_+\) with
\[
\langle\pi(a)\zeta,\zeta\rangle=\langle ah_\zeta,h_\zeta\rangle_2=\tau(ah_\zeta^2)\qquad(a\in M).
\]
There is a partial isometry \(y_\zeta\in L_M(L^2,\mathcal K)\) with \(y_\zeta(ah_\zeta)=\pi(a)\zeta\) for \(a\in M\). Its initial projection is the projection onto the closure \([Mh_\zeta]\) of \(Mh_\zeta\), its final projection is the projection onto \([\pi(M)\zeta]\), and \(y_\zeta h_\zeta=\zeta\).

**Proof.** The functional \(a\mapsto\langle\pi(a)\zeta,\zeta\rangle\) is positive and normal, because \(\pi\) is normal. So it lies in \(M_*^+\) (Fact 2.7(e)), and Fact 2.6(b) gives a unique density \(k\in L^1_+\). Put \(h_\zeta=k^{1/2}\in L^2_+\). By the cyclicity of the trace on products of two elements of \(L^2\) (Fact 2.6(c)), \(\tau(ak)=\tau(h_\zeta(ah_\zeta))=\langle ah_\zeta,h_\zeta\rangle_2\). Uniqueness: if \(h'\in L^2_+\) gives the same functional, then \(h'^2=k\) by the uniqueness of densities (Fact 2.6(b)), and \(h'=h_\zeta\) by uniqueness of positive square roots (Fact 2.3(g)). Now \(\|ah_\zeta\|_2^2=\tau(a^*ak)=\|\pi(a)\zeta\|^2\). So \(ah_\zeta\mapsto\pi(a)\zeta\) is a well-defined isometry from \(Mh_\zeta\) onto \(\pi(M)\zeta\). It extends to a unitary between the closures. Extend it by \(0\) on \([Mh_\zeta]^\perp\). That subspace is invariant under every \(L_a\), since \([Mh_\zeta]\) is invariant and \(M\) is closed under adjoints. So the extension \(y_\zeta\) intertwines on both pieces. Finally \(y_\zeta h_\zeta=\pi(1)\zeta=\zeta\). \(\square\)

**Theorem 12.2** (The coupling trace). There is a unique normal weight \(\tau_\pi\) on \(\pi(M)'\) such that
\[
\tau_\pi(yy^*)=\tau_N(y^*y)\qquad\text{for every }y\in L_M(L^2,\mathcal K).
\tag{12.1}
\]
It is a faithful normal semifinite trace. For any family \((y_i)\) in \(L_M(L^2,\mathcal K)\) with \(\sum_iy_iy_i^*=1\) (strongly),
\[
\tau_\pi(z)=\sum_i\tau_N(y_i^*zy_i)\qquad(z\in\pi(M)'_+).
\]

**Proof.** *A family exists.* By Zorn's lemma choose a maximal family of nonzero vectors \(\zeta_i\) whose cyclic subspaces \([\pi(M)\zeta_i]\) are mutually orthogonal. The orthogonal complement of their sum is invariant under \(\pi(M)\). If it contained a nonzero vector, its cyclic subspace could be added to the family. So the cyclic subspaces fill \(\mathcal K\), and the partial isometries \(y_i=y_{\zeta_i}\) of Lemma 12.1 satisfy \(\sum_iy_iy_i^*=1\). Fix such a family, and define \(\tau_\pi(z)=\sum_i\tau_N(y_i^*zy_i)\) for \(z\in\pi(M)'_+\).

*(12.1) holds.* Let \(y\in L_M(L^2,\mathcal K)\). Each \(y^*y_i\) lies in \(N\). By the trace property of \(\tau_N\),
\[
\tau_N(y_i^*yy^*y_i)=\tau_N\bigl((y^*y_i)^*(y^*y_i)\bigr)=\tau_N\bigl((y^*y_i)(y^*y_i)^*\bigr)=\tau_N(y^*y_iy_i^*y).
\]
The finite partial sums of \(y^*y_iy_i^*y\) increase to \(y^*y\). Normality of \(\tau_N\) gives \(\tau_\pi(yy^*)=\tau_N(y^*y)\).

*Normal weight.* Each \(z\mapsto\tau_N(y_i^*zy_i)\) is a normal weight, and a sum of normal weights is a normal weight, since suprema of increasing nets commute with suprema of finite partial sums.

*Trace.* For \(z\in\pi(M)'\), each \(zy_i\) lies in \(L_M(L^2,\mathcal K)\). By (12.1) and normality,
\[
\tau_\pi(z^*z)=\sum_i\tau_N\bigl((zy_i)^*(zy_i)\bigr)=\sum_i\tau_\pi\bigl(zy_iy_i^*z^*\bigr)=\tau_\pi(zz^*).
\]

*Faithful.* If \(\tau_\pi(z^*z)=0\), then \(zy_i=0\) for every \(i\), since \(\tau_N\) is faithful. So \(z=z\sum_iy_iy_i^*=0\).

*Semifinite.* Let \(f\in N\) be a projection with \(\tau_N(f)<\infty\), and let \(F\) be a finite set of indices. Put \(z_{F,f}=\sum_{i\in F}y_ify_i^*\). By (12.1), \(\tau_\pi(y_ify_i^*)=\tau_N(fy_i^*y_if)\le\tau_N(f)\), so \(z_{F,f}\) has finite trace. These elements increase to \(\sum_iy_iy_i^*=1\), because the projections of finite trace increase to \(1\) in \(N\) (Fact 2.1(e) for \(\tau_N\)). For \(x\in\pi(M)'\), the elements \(z_{F,f}xz_{F,f}\) have finite trace, since \(\mathfrak m_{\tau_\pi}\) is an ideal, and they converge weakly to \(x\) along a bounded net. So \(\mathfrak m_{\tau_\pi}\) is \(\sigma\)-weakly dense.

*Uniqueness.* Let \(\varphi\) be any normal weight on \(\pi(M)'\) that satisfies (12.1). For \(z\in\pi(M)'_+\), the partial sums of \(z^{1/2}y_iy_i^*z^{1/2}\) increase to \(z\), and \(z^{1/2}y_i\in L_M(L^2,\mathcal K)\). So
\[
\varphi(z)=\sum_i\varphi\bigl((z^{1/2}y_i)(z^{1/2}y_i)^*\bigr)=\sum_i\tau_N(y_i^*zy_i)=\tau_\pi(z).
\]
In particular \(\tau_\pi\) does not depend on the family. \(\square\)

**Corollary 12.3.**

1. For \(y\in L_M(\mathcal K_1,\mathcal K_2)\), \(\tau_{\pi_1}(y^*y)=\tau_{\pi_2}(yy^*)\).
2. For \(\pi=\pi_\tau\), \(\tau_\pi=\tau_N\).
3. For \(\pi=\pi_1\oplus\pi_2\) on \(\mathcal K_1\oplus\mathcal K_2\), the projection \(p_1\) onto \(\mathcal K_1\) lies in \(\pi(M)'\), \(p_1\pi(M)'p_1=\pi_1(M)'\), and the restriction of \(\tau_\pi\) to it is \(\tau_{\pi_1}\).

**Proof.** (1) Choose a family \((w_j)\) for \(\mathcal K_2\) as in Theorem 12.2. Each \(y^*w_j\) lies in \(L_M(L^2,\mathcal K_1)\). By the formula of Theorem 12.2, then (12.1) for \(\pi_1\), then normality,
\[
\tau_{\pi_2}(yy^*)=\sum_j\tau_N\bigl((y^*w_j)^*(y^*w_j)\bigr)=\sum_j\tau_{\pi_1}\bigl(y^*w_jw_j^*y\bigr)=\tau_{\pi_1}(y^*y).
\]
(2) \(\tau_N\) is a normal trace on \(N=\pi_\tau(M)'\), so it satisfies (12.1). Uniqueness applies. (3) Block matrices show that \(p_1\in\pi(M)'\) and that \(p_1\pi(M)'p_1\) consists of the elements of \(\pi_1(M)'\), extended by \(0\). The restriction of \(\tau_\pi\) is a normal weight on it. It satisfies (12.1) for \(\pi_1\), because \(y\in L_M(L^2,\mathcal K_1)\) followed by the inclusion lies in \(L_M(L^2,\mathcal K)\). Uniqueness applies. \(\square\)

For \(M\) acting on its own space \(H\), this gives a faithful normal semifinite trace \(\tau_H=\tau_{\mathrm{id}}\) on \(M'\).

## 13. Measurable intertwiners and square-integrable vectors

Let \(\pi_1,\pi_2,\pi_3\) be normal unital representations on \(\mathcal K_1,\mathcal K_2,\mathcal K_3\). Put \(\widetilde{\mathcal K}=\mathcal K_1\oplus\mathcal K_2\oplus\mathcal K_3\), \(\widetilde\pi=\pi_1\oplus\pi_2\oplus\pi_3\), \(P=\widetilde\pi(M)'\) and \(\tau_P=\tau_{\widetilde\pi}\). Let \(p_i\in P\) be the projection onto \(\mathcal K_i\). By block matrices, \(p_jPp_i=L_M(\mathcal K_i,\mathcal K_j)\) and \(p_iPp_i=\pi_i(M)'\). By Corollary 12.3(3), applied to \(\pi_i\) and the sum of the other two representations, \(\tau_P\) restricts to \(\tau_{\pi_i}\) on \(p_iPp_i\). The indices may repeat: every statement below, with the same proof, holds for corners \(p_jPp_i\) with any \(i\) and \(j\), including \(i=j\). Theorem 13.4 uses this for the corners of \(L^2\oplus\mathcal K\).

For \(y\in L_M(\mathcal K_1,\mathcal K_2)\) we say \(y\in N_{12}(r,d)\) if \(\|ye\|<r\) and \(\tau_{\pi_1}(1-e)<d\) for some projection \(e\in\pi_1(M)'\). For vectors of \(\mathcal K_1\) we use the neighbourhoods \(V_1(r,d)\) of \((\pi_1(M)',\tau_{\pi_1})\).

**Lemma 13.1** (Compression). Let \(P\) be a von Neumann algebra on \(\widetilde{\mathcal K}\) with a faithful normal semifinite trace \(\tau_P\), and let \(p,q\in\operatorname{Proj}(P)\).

1. For \(x\in qPp\): \(x\in U_P(r,d)\) if and only if some projection \(e\le p\) in \(P\) has \(\|xe\|<r\) and \(\tau_P(p-e)<d\).
2. For \(\xi\in p\widetilde{\mathcal K}\): \(\xi\in V_P(r,d)\) if and only if some projection \(e\le p\) in \(P\) has \(\|e\xi\|<r\) and \(\tau_P(p-e)<d\).
3. \(pPp\) is a von Neumann algebra on \(p\widetilde{\mathcal K}\), and the restriction of \(\tau_P\) is a faithful normal semifinite trace on it. Its measure uniformity is the one it inherits from \(P\). The closure of \(pPp\) in \(\widehat P\) is \(p\widehat Pp\), and this is the completion of \(pPp\). For \(a\in p\widehat Pp\), the operator \(T_a\) on \(\widetilde{\mathcal K}\) equals \(T^{(p)}_ap\), where \(T^{(p)}_a\) is the operator of \(a\) computed in \(pPp\).

**Proof.** (1) Suppose \(\|xf\|<r\) and \(\tau_P(1-f)<d\). Put \(e=p\wedge f\). Then \(\|xe\|=\|xfe\|\le\|xf\|\). The projection \(p-e\) has zero meet with \(f\), so \(p-e\precsim1-f\) (Fact 2.1(b)), and \(\tau_P(p-e)<d\). Conversely, given \(e\), put \(f=e+(1-p)\). Then \(xf=xe\), because \(x=xp\), and \(1-f=p-e\). (2) is the same argument, with \(\|e\xi\|=\|ef\xi\|\le\|f\xi\|\) and \(f\xi=e\xi\).

(3) By semifiniteness of \(\tau_P\) (Fact 2.1(e)), \(p\) is the supremum of its subprojections of finite trace, which gives semifiniteness of the restriction. Faithfulness and normality are inherited. By (1) with \(q=p\), the uniformity of \(pPp\) is the restriction of that of \(P\). So the inclusion extends to an embedding of the completion onto the closure of \(pPp\). The closure is \(p\widehat Pp\): the continuous idempotent map \(x\mapsto pxp\) fixes \(pPp\), and every \(x\in p\widehat Pp\) is the limit of \(px_np\) when \(x_n\to x\). For the last claim, let \(a\in p\widehat Pp\). By the cutoff property (Fact 2.2(d)) in \(pPp\), choose increasing \(e_n\le p\) with \(\tau_P(p-e_n)\to0\) and \(ae_n\in pPp\). Put \(f_n=e_n+(1-p)\). Then \(af_n=ae_n\), since \(a(1-p)=0\), and \(\tau_P(1-f_n)\to0\). The operators \(T_a\) and \(T^{(p)}_ap\) are closed and densely defined. Both are affiliated with \(P\): if \(v\in P'\) is unitary, then \(vp\) restricted to \(p\widetilde{\mathcal K}\) is a unitary commuting with \(pPp\), so it commutes with \(T^{(p)}_a\). Both contain \(f_n\widetilde{\mathcal K}\) in their domains, and both equal \(ae_n\) there. Graph uniqueness (Fact 2.3(b)) gives \(T_a=T^{(p)}_ap\). \(\square\)

**Theorem 13.2** (The measure topology on intertwiners). For all positive parameters:
\[
N_{12}(r,d)^*=N_{21}(r,d),\qquad N_{12}(r_1,d_1)+N_{12}(r_2,d_2)\subseteq N_{12}(r_1+r_2,d_1+d_2),
\]
\[
N_{23}(r_1,d_1)\,N_{12}(r_2,d_2)\subseteq N_{13}(r_1r_2,d_1+d_2),\qquad
N_{12}(r_1,d_1)\,V_1(r_2,d_2)\subseteq V_2(r_1r_2,d_1+d_2).
\]
The involution \(L_M(\mathcal K_1,\mathcal K_2)\to L_M(\mathcal K_2,\mathcal K_1)\) and addition are uniformly continuous. The products \(L_M(\mathcal K_2,\mathcal K_3)\times L_M(\mathcal K_1,\mathcal K_2)\to L_M(\mathcal K_1,\mathcal K_3)\) and \(L_M(\mathcal K_1,\mathcal K_2)\times\mathcal K_1\to\mathcal K_2\) are uniformly continuous on bounded sets. All these maps extend uniquely to the completions.

**Proof.** By parts (1) and (2) of Lemma 13.1, \(N_{ij}(r,d)=U_P(r,d)\cap p_jPp_i\), and \(V_i(r,d)=V_P(r,d)\cap\mathcal K_i\). The inclusions are those of Fact 2.2(a) for \(P\), intersected with the corners. Continuity and extension follow from Fact 2.2(b) and (c) for \(P\), restricted to the corners. \(\square\)

Let \(\mathfrak M_M(\mathcal K_1,\mathcal K_2)\) be the completion of \(L_M(\mathcal K_1,\mathcal K_2)\). By the argument of Lemma 13.1(3), it is the corner \(p_2\widehat Pp_1\). For \(a\in p_2\widehat Pp_1\) the operator \(T_a\) equals \(T_ap_1\), because the ordinary product with the bounded projection \(p_1\) is closed (Fact 2.3(d)). Its values lie in \(\mathcal K_2\), because \(T_a=T_{p_2a}\). Let \(\check T_a\) be the restriction of \(T_a\) to \(D(T_a)\cap\mathcal K_1\), an operator from \(\mathcal K_1\) to \(\mathcal K_2\).

**Theorem 13.3** (Measurable intertwiners as closed operators).

1. For \(a\in\mathfrak M_M(\mathcal K_1,\mathcal K_2)\), \(\check T_a\) is closed and densely defined, and it intertwines: for every unitary \(u\in M\), \(\pi_1(u)D(\check T_a)=D(\check T_a)\) and \(\check T_a\pi_1(u)=\pi_2(u)\check T_a\). It has no proper closed intertwining extension. The map \(a\mapsto\check T_a\) is injective.
2. \(\check T_{a^*}=\check T_a^*\) and \(\check T_{a+b}=\overline{\check T_a+\check T_b}\). For \(a\in\mathfrak M_M(\mathcal K_2,\mathcal K_3)\) and \(b\in\mathfrak M_M(\mathcal K_1,\mathcal K_2)\), \(\check T_{ab}=\overline{\check T_a\check T_b}\).
3. Let \(e_n\in\pi_1(M)'\) be increasing projections with \(\tau_{\pi_1}(1-e_n)\to0\). Let \(A\) be a linear map from \(\bigcup_ne_n\mathcal K_1\) to \(\mathcal K_2\) with \(Ae_n\in L_M(\mathcal K_1,\mathcal K_2)\) for every \(n\). Then \(A\) is closable, and \(\overline A=\check T_a\) for a unique \(a\in\mathfrak M_M(\mathcal K_1,\mathcal K_2)\).

**Proof.** (1) The graph of \(\check T_a\) is the intersection of the graph of \(T_a\) with \(\mathcal K_1\times\widetilde{\mathcal K}\), so it is closed. Since \(D(T_a)=\{\xi:p_1\xi\in D(T_a)\}\), \(p_1D(T_a)\subseteq D(\check T_a)\), and this is dense in \(\mathcal K_1\). \(T_a\) commutes with every unitary of \(P'\), and \(\widetilde\pi(u)\) is such a unitary for \(u\in M\) unitary. That gives the intertwining. For maximality, let \(S\supseteq\check T_a\) be closed, densely defined and intertwining. Then \(Sp_1\) is closed and densely defined on \(\widetilde{\mathcal K}\). The set of bounded \(c\) with \(cSp_1\subseteq Sp_1c\) is an algebra. It is strongly closed, because the graph is closed. It contains \(\widetilde\pi(u)\) for unitaries \(u\in M\), hence all of \(\widetilde\pi(M)\), since every element of \(M\) is a combination of four unitaries. By the bicommutant theorem it contains \(\widetilde\pi(M)''=P'\). So \(Sp_1\) is affiliated with \(P\) and extends \(T_a\), and the maximality in Fact 2.3(c) gives \(Sp_1=T_a\), that is, \(S=\check T_a\). Injectivity follows from the injectivity of \(a\mapsto T_a\) (Fact 2.3(c)), since \(T_a=\check T_ap_1\).

(2) By Fact 2.3(d), \(T_{a^*}=T_a^*\). A vector \(\eta\) lies in \(D((\check T_ap_1)^*)\) exactly when \(p_2\eta\in D(\check T_a^*)\), and then \((\check T_ap_1)^*\eta=\check T_a^*p_2\eta\). So \(\check T_{a^*}p_2=T_{a^*}=\check T_a^*p_2\). For sums and products, Fact 2.3(d) gives \(T_{a+b}=\overline{(\check T_a+\check T_b)p_1}=\overline{\check T_a+\check T_b}\,p_1\) and \(T_{ab}=\overline{\check T_ap_2\check T_bp_1}=\overline{\check T_a\check T_b}\,p_1\).

(3) Put \(f_n=e_n+(1-p_1)\in\operatorname{Proj}(P)\). These increase, and \(\tau_P(1-f_n)=\tau_{\pi_1}(1-e_n)\to0\). Define \(\widetilde A\xi=A(p_1\xi)\) on \(\bigcup_nf_n\widetilde{\mathcal K}\). Then \(\widetilde Af_n=Ae_np_1\in P\). By the increasing-domain theorem (Fact 2.3(e)), \(\widetilde A\) is closable with closure \(T_a\) for a unique \(a\in\widehat P\). Since \(\widetilde A=\widetilde Ap_1\) and its values lie in \(\mathcal K_2\), injectivity gives \(a=p_2ap_1\), and \(\overline A=\check T_a\). \(\square\)

Now fix a normal unital representation \(\pi\) on \(\mathcal K\). Apply the construction above to \(\widetilde{\mathcal K}=L^2\oplus\mathcal K\) and \(\widetilde\pi=\pi_\tau\oplus\pi\), with \(P=\widetilde\pi(M)'\), \(p_0\) the projection onto \(L^2\), and \(p_1\) the projection onto \(\mathcal K\). By Corollary 12.3(2) and (3), \(\tau_P\) restricts to \(\tau_N\) on \(p_0Pp_0=N\). By Lemma 13.1(3), \(S(N,\tau_N)\) is the corner \(p_0\widehat Pp_0\), with the same operators. For \(\xi\in\mathcal K\) let \(h=h_\xi\) and \(y=y_\xi\) be as in Lemma 12.1, and let \(R_0(\xi):\mathfrak n_\tau\to\mathcal K\) be the map \(x\mapsto\pi(x)\xi\). Here \(\mathfrak n_\tau=M\cap L^2\) is viewed inside \(L^2\).

**Theorem 13.4** (Vectors as square-integrable intertwiners).

1. \(R_0(\xi)\) is closable. Its closure \(R(\xi)\) is the ordinary product \(y\,\widehat\rho(h)\):
\[
D(R(\xi))=\{x\in L^2:\ xh\in L^2\},\qquad R(\xi)x=y(xh),
\]
and \(\mathfrak n_\tau\) is a core for it.
2. \(R(\xi)=\check T_{a_\xi}\) with \(a_\xi=y\widehat\rho(h)\in\mathfrak M_M(L^2,\mathcal K)\), and \(R(\xi)x=\pi(x)\xi\) for \(x\in\mathfrak n_\tau\).
3. \(R(\xi)^*R(\xi)=\widehat\rho(h^2)\in L^1(N,\tau_N)_+\), and \(\tau_N(R(\xi)^*R(\xi))=\|\xi\|^2\).
4. If \(R\in\mathfrak M_M(L^2,\mathcal K)\) and \(\tau_N(R^*R)<\infty\), then \(R=R(\xi)\) for exactly one \(\xi\in\mathcal K\). Explicitly, \(\xi=wk\), where \(R=w|R|\) is the polar decomposition and \(|R|=\widehat\rho(k)\) with \(k\in L^2_+\).
5. Let \(L^2_M(\mathcal K)\) be the set of such \(R\), with \(\|R\|_2=\tau_N(R^*R)^{1/2}\). The map \(\xi\mapsto R(\xi)\) is a linear isometry of \(\mathcal K\) onto \(L^2_M(\mathcal K)\). So \(L^2_M(\mathcal K)\) is a Hilbert space, with the inner product given by polarization.
6. For \(z\in\pi(M)'\) and \(b\in M\),
\[
zR(\xi)=R(z\xi),\qquad R(\xi)\rho(b)=R(\pi(b)\xi).
\]
So \(\pi(M)'\) acts on \(L^2_M(\mathcal K)\) by left multiplication, and \(N\) acts by right multiplication. The unitary \(\xi\mapsto R(\xi)\) carries \(\pi(b)\) to right multiplication by \(\rho(b)\).
7. Let \(M\subseteq B(H)\) act on its own space. Then \(M'\) is a von Neumann algebra on \(H\) with the faithful normal semifinite trace \(\tau_H\) of Section 12, and \((M')'=M\). Applying Sections 11–13 to the pair \((M',\tau_H)\) gives a unitary from \(H\) onto the square-integrable intertwiners from \(L^2(M',\tau_H)\) to \(H\). Under it, \(M\) acts by left multiplication.

**Proof.** Write \(R_h=\widehat\rho(h)\), so by Theorem 11.2(3), \(R_hx=xh\) on \(\{x\in L^2:xh\in L^2\}\).

*The range of \(R_h\) lies in \([Mh]\), and \(\mathfrak n_\tau\) is a core for \(R_h\).* Let \(x\in D(R_h)\). Put \(g_j=1_{[0,j]}(|x^*|)\). Then \((g_jx)(g_jx)^*=|x^*|^2g_j\le j^2\), so \(g_jx\) is bounded. It lies in \(L^2\), hence in \(\mathfrak n_\tau\). The projections \(g_j\) increase to \(1\), because the spectral tails of the measurable operator \(|x^*|\) have traces tending to \(0\) (Facts 2.3(f) and 2.1(d)). By Fact 2.6(d), \(g_jx\to x\) and \((g_jx)h=g_j(xh)\to xh\) in \(L^2\). This shows \(xh\in[Mh]\), and it shows the core property. Also \(\mathfrak n_\tau\subseteq D(R_h)\), since \(Mh\subseteq L^2\).

(1) For \(x\in\mathfrak n_\tau\), \(yR_hx=y(xh)=\pi(x)\xi=R_0(\xi)x\). The operator \(yR_h\) is closed. Indeed, \(y^*y\) is the projection onto \([Mh]\), which contains the range of \(R_h\). If \(x_j\to x\) and \(yR_hx_j\to\zeta\), then \(R_hx_j=y^*yR_hx_j\to y^*\zeta\). Since \(R_h\) is closed, \(R_hx=y^*\zeta\). As \(\zeta\) lies in the closed range of \(y\), \(yR_hx=yy^*\zeta=\zeta\). By the core property, the closure of \(R_0(\xi)\) is \(yR_h\).

(2) Since \(y\in p_1Pp_0\) and \(\widehat\rho(h)\in p_0\widehat Pp_0\), \(a_\xi\) lies in \(p_1\widehat Pp_0\). By Theorem 13.3(2), \(\check T_{a_\xi}=\overline{\check T_y\check T_{\widehat\rho(h)}}=\overline{yR_h}=yR_h\). Here \(\check T_{\widehat\rho(h)}=R_h\) by Lemma 13.1(3) and Theorem 11.2(3).

(3) \(a_\xi^*a_\xi=\widehat\rho(h)\,y^*y\,\widehat\rho(h)\). Since \(y^*y\) is the projection onto \([Mh]\), which contains the range of \(R_h\), the operator of \(y^*y\widehat\rho(h)\) is \(R_h\). By injectivity, \(y^*y\widehat\rho(h)=\widehat\rho(h)\). So \(a_\xi^*a_\xi=\widehat\rho(h)^2=\widehat\rho(h^2)\). By Theorem 11.2(1), \(\tau_N(\widehat\rho(h^2))=\tau(h^2)=\|h\|_2^2=\langle\pi(1)\xi,\xi\rangle=\|\xi\|^2\).

(4) Let \(R=\check T_a\), \(a\in p_1\widehat Pp_0\), with \(\tau_N(a^*a)<\infty\). Take the polar decomposition \(a=w|a|\) in \(\widehat P\) (Fact 2.3(g)). Since \(a^*a\in p_0\widehat Pp_0\), also \(|a|\) lies in this corner. The initial projection of \(w\) lies under \(p_0\) and its final projection under \(p_1\), so \(w\in p_1Pp_0=L_M(L^2,\mathcal K)\). Also \(\tau_N(|a|^2)<\infty\), so \(|a|\in L^2(N,\tau_N)_+\). By Theorem 11.2(2) and (1), \(|a|=\widehat\rho(k)\) for some \(k\in L^2(M,\tau)_+\). Put \(\xi=wk\in\mathcal K\). Since \(a=w\widehat\rho(k)\), Theorem 13.3(2) gives \(\check T_a=\overline{wR_k}\supseteq wR_k\). For \(x\in\mathfrak n_\tau\), \(xk\in L^2\), so \(x\in D(wR_k)\subseteq D(\check T_a)\), and
\[
\check T_ax=w(xk)=wL_xk=\pi(x)wk=\pi(x)\xi .
\]
So \(\check T_a\supseteq R_0(\xi)\) and hence \(\check T_a\supseteq R(\xi)=\check T_{a_\xi}\). By the maximality in Theorem 13.3(1), \(R=R(\xi)\). For uniqueness, if \(R(\xi)=R(\xi')\), then \(\pi(e)\xi=\pi(e)\xi'\) for every \(e\in\mathcal E\subseteq\mathfrak n_\tau\). Since \(e\uparrow1\) and \(\pi\) is normal, \(\xi=\xi'\).

(5) \(R(\xi)+R(\xi')\) (the closure of the sum, Theorem 13.3(2)) extends \(R_0(\xi)+R_0(\xi')=R_0(\xi+\xi')\), hence extends \(R(\xi+\xi')\), and maximality gives equality. Scalars are the same. By (3), \(\|R(\xi)\|_2=\|\xi\|\). By (4), the map is onto \(L^2_M(\mathcal K)\).

(6) \(zR(\xi)\) is the operator of \(za_\xi\), and it extends \(zR_0(\xi)=R_0(z\xi)\). Also \(R(\xi)\rho(b)\) extends \(R_0(\pi(b)\xi)\): for \(x\in\mathfrak n_\tau\), \(xb\in\mathfrak n_\tau\) and \(R_0(\xi)(xb)=\pi(x)\pi(b)\xi\). Maximality gives both identities. \(\square\)

**Example 13.5** (Square-integrable vectors for a commutative algebra). Let \(M=L^\infty(0,1)\) with the Lebesgue trace, acting on \(\mathcal K=L^2(0,1)\). Then \(L^2(M,\tau)=L^2(0,1)\), \(N=M\) and \(\tau_N=\tau\). For \(\xi\in\mathcal K\), \(h_\xi=|\xi|\), and \(y_\xi\) is multiplication by the phase \(u=\xi/|\xi|\) on \(\{\xi\neq0\}\). So \(R(\xi)=M_uM_{|\xi|}=M_\xi\), with domain \(\{x:x|\xi|\in L^2\}\). Also \(R(\xi)^*R(\xi)=M_{|\xi|^2}\in L^1\), with trace \(\|\xi\|_2^2\).

## 14. Isomorphisms that scale the trace

Let \(M_1\) be a second von Neumann algebra, on a Hilbert space \(H_1\), with a faithful normal semifinite trace
\(\tau_1\), and let \(\theta:M\to M_1\) be a \(*\)-isomorphism with
\[
\tau_1\circ\theta=\lambda\,\tau\quad\text{on }M_+
\tag{14.1}
\]
for some \(\lambda>0\). We write \(U_1(r,d)\), \(S(M_1,\tau_1)\) and so on for the objects of Section 1 built from
\((M_1,\tau_1)\). A \(*\)-isomorphism of von Neumann algebras is normal (The universal enveloping von Neumann algebra of
a C\*-algebra, and W\*-algebras, Corollary 11.4),
and an injective \(*\)-homomorphism of C\*-algebras is isometric (C\*-algebras: continuous functional calculus,
automatic continuity, positive cones, approximate identities and quotients, Corollary
4.6). Examples: an automorphism
of a finite algebra with a faithful normal tracial state that preserves the state (\(\lambda=1\)); the automorphisms of
\(R\bar\otimes B(\ell^2)\) that scale its trace.

**Theorem 14.1.** \(\theta\) extends uniquely to a map \(\tilde\theta:S(M,\tau)\to S(M_1,\tau_1)\) that is continuous
for the measure topologies. The map \(\tilde\theta\) is a bijection and a \(*\)-isomorphism, its inverse is the
extension of \(\theta^{-1}\), and:

1. \(\tilde\theta\) maps \(S(M,\tau)_+\) onto \(S(M_1,\tau_1)_+\), with \(\tilde\theta(h^{1/2})=\tilde\theta(h)^{1/2}\)
   and \(\tilde\theta(|x|)=|\tilde\theta(x)|\). If \(x=v|x|\) is the polar decomposition of \(x\), then
   \(\tilde\theta(x)=\theta(v)|\tilde\theta(x)|\) is that of \(\tilde\theta(x)\).
2. Let \(h\in S(M,\tau)_+\) and let \(f:[0,\infty)\to\mathbb C\) be a Borel function that is bounded on bounded sets,
   with \(f(h)\in S(M,\tau)\); this holds for every bounded Borel \(f\). Then \(\tilde\theta(f(h))=f(\tilde\theta(h))\).
   In particular \(\theta(1_B(h))=1_B(\tilde\theta(h))\) for every Borel set \(B\).
3. \(\tau_1(\tilde\theta(h))=\lambda\tau(h)\) for \(h\in S(M,\tau)_+\). For \(1\leq p<\infty\), \(\tilde\theta\) maps
   \(L^p(M,\tau)\) onto \(L^p(M_1,\tau_1)\), and \(\|\tilde\theta(x)\|_p=\lambda^{1/p}\|x\|_p\).
4. If \(M_1=M\), \(\tau_1=\tau\) and \(\lambda=1\), the restriction of \(\tilde\theta\) to \(L^2(M,\tau)\) is the unitary
   \(U_\theta\) with \(U_\theta\hat x=\widehat{\theta(x)}\) for \(x\in\mathfrak n_\tau\), and
   \(U_\theta L_aU_\theta^*=L_{\theta(a)}\), \(U_\theta R_bU_\theta^*=R_{\theta(b)}\), \(U_\theta J=JU_\theta\).

**Proof.** *The extension.* For \(x\in M\) and a projection \(p\in M\), \(\theta(p)\) is a projection,
\(\|\theta(x)\theta(p)\|=\|\theta(xp)\|=\|xp\|\), and \(\tau_1(1-\theta(p))=\lambda\tau(1-p)\) by (14.1). Hence
\(\theta(U(r,d))=U_1(r,\lambda d)\), using \(\theta^{-1}\) for the inclusion \(\supseteq\). So \(\theta\) and \(\theta^{-1}\) are uniformly continuous for the uniformities of Fact 2.2(b). A
uniformly continuous map into a complete uniform space extends uniquely to the completion, so \(\theta\) and
\(\theta^{-1}\) extend to mutually inverse continuous maps between \(\widehat M=S(M,\tau)\) and
\(\widehat{M_1}=S(M_1,\tau_1)\) (Fact 2.2(c)). Every continuous extension agrees with \(\tilde\theta\) on the dense set
\(M\), hence everywhere. For \(x,y\in S(M,\tau)\), Fact 2.2(d) gives \(x_n,y_n\in M\) with \(x_n\to x\), \(y_n\to y\) in
measure; these sequences are Cauchy, hence bounded in measure, so \(x_ny_n\to xy\), \(x_n+y_n\to x+y\) and
\(x_n^*\to x^*\) (Fact 2.2(b), (c)). Applying \(\theta\) and passing to the limit shows that \(\tilde\theta\) preserves
products, sums and adjoints.

(1) The positive elements are the \(b^*b\) (Fact 2.3(g)), and \(\tilde\theta(b^*b)=\tilde\theta(b)^*\tilde\theta(b)\);
the same for \(\tilde\theta^{-1}\). The element \(\tilde\theta(h^{1/2})\) is positive with square \(\tilde\theta(h)\), so it
is the unique positive square root of \(\tilde\theta(h)\) (Fact 2.3(g)); with \(h=x^*x\) this gives
\(\tilde\theta(|x|)=|\tilde\theta(x)|\). The polar decomposition is treated after (2).

(2) For \(h\in M_+\) and bounded Borel \(f\), \(\theta(f(h))=f(\theta(h))\), because a normal \(*\)-homomorphism commutes
with the bounded Borel calculus (Fact 2.7(c)). For \(h\in S(M,\tau)_+\), put \(r=(1+h)^{-1}=g(h)\) with
\(g(t)=(1+t)^{-1}\); this is an element of \(M\) with \(0\leq r\leq1\), and \((1+h)r=1\) in \(S(M,\tau)\). Applying
\(\tilde\theta\), \((1+\tilde\theta(h))\theta(r)=1\), so \(\theta(r)=(1+\tilde\theta(h))^{-1}\). For bounded Borel
\(f\) on \([0,\infty)\), \(f(h)=(f\circ\psi)(r)\) with \(\psi(s)=s^{-1}-1\) on \((0,1]\) (the composition rule of the
Borel calculus), and \(r\) is injective, so its spectral measure is carried by \((0,1]\). Hence
\[
\theta(f(h))=\theta\bigl((f\circ\psi)(r)\bigr)=(f\circ\psi)(\theta(r))=f(\tilde\theta(h)) .
\]
Now let \(f\) be bounded on bounded sets with \(f(h)\in S(M,\tau)\). Put \(p_n=1_{[0,n]}(h)\). Then
\(\tau(1-p_n)\to0\) by the spectral-tail criterion (Fact 2.3(f)), and \(f(h)p_n=(f1_{[0,n]})(h)\in M\). By the bounded
case, \(\tilde\theta(f(h))\theta(p_n)=\theta(f(h)p_n)=(f1_{[0,n]})(\tilde\theta(h))=f(\tilde\theta(h))\theta(p_n)\). So
the closed affiliated operators \(\tilde\theta(f(h))\) and \(f(\tilde\theta(h))\) agree on the subspaces
\(\theta(p_n)H_1\), which lie in both domains, and \(\tau_1(1-\theta(p_n))=\lambda\tau(1-p_n)\to0\). By graph uniqueness
(Fact 2.3(b)) they are equal.

*The polar decomposition.* Let \(x=v|x|\), so \(v\in M\) is a partial isometry with \(v^*v=1_{(0,\infty)}(|x|)\) (Fact
2.3(g)). Then \(\tilde\theta(x)=\theta(v)\tilde\theta(|x|)=\theta(v)|\tilde\theta(x)|\), and \(\theta(v)\) is a partial
isometry with \(\theta(v)^*\theta(v)=\theta(1_{(0,\infty)}(|x|))=1_{(0,\infty)}(|\tilde\theta(x)|)\) by (2). By the
uniqueness of the polar decomposition, this is the polar decomposition of \(\tilde\theta(x)\).

(3) By Fact 2.4(a) and (2),
\[
\tau_1(\tilde\theta(h))=\int_0^\infty\tau_1\bigl(1_{(s,\infty)}(\tilde\theta(h))\bigr)\,ds
=\int_0^\infty\tau_1\bigl(\theta(1_{(s,\infty)}(h))\bigr)\,ds=\lambda\int_0^\infty\tau\bigl(1_{(s,\infty)}(h)\bigr)\,ds
=\lambda\tau(h).
\]
By (1) and (2) with \(f(t)=t^p\), \(|\tilde\theta(x)|^p=\tilde\theta(|x|^p)\), so
\(\|\tilde\theta(x)\|_p^p=\lambda\|x\|_p^p\); applying the same to \(\tilde\theta^{-1}\) gives the image.

(4) By (3), \(\tilde\theta\) restricts to a linear isometry of \(L^2(M,\tau)\) onto itself, and it agrees with \(\theta\)
on \(\mathfrak n_\tau\subseteq M\), which gives the formula for \(U_\theta\). Since \(\tilde\theta(a\xi b)=\theta(a)\tilde
\theta(\xi)\theta(b)\) and \(\tilde\theta(\xi^*)=\tilde\theta(\xi)^*\), \(U_\theta\) intertwines \(L_a\) with
\(L_{\theta(a)}\), \(R_b\) with \(R_{\theta(b)}\), and \(J\xi=\xi^*\) with itself (Fact 2.6(e)). \(\square\)

**Proposition 14.2** (Corners). Let \(e\in M\) be a nonzero projection with \(\tau(e)<\infty\), and let
\(\tau_e=\tau(e)^{-1}\tau|_{eMe}\), a faithful normal tracial state of \(M_e=eMe\) on \(eH\). The map
\(\xi\mapsto\tau(e)^{1/2}\xi\), defined on \(eMe\), extends to a unitary \(V\) of \(eL^2(M,\tau)e\) onto
\(L^2(M_e,\tau_e)\), with \(V(a\xi b)=aV(\xi)b\) for \(a,b\in M_e\) and \(VJ=JV\). Equivalently, \(\eta\mapsto
\tau(e)^{-1/2}\eta\) maps \(L^2(M_e,\tau_e)\) unitarily onto \(eL^2(M,\tau)e\).

**Proof.** For \(x\in eMe\), \(\|\tau(e)^{1/2}x\|_{L^2(\tau_e)}^2=\tau(e)\,\tau_e(x^*x)=\tau(x^*x)=\|x\|_{L^2(\tau)}^2\).
The subspace \(eMe\) is dense in \(eL^2(M,\tau)e\): the map \(\xi\mapsto e\xi e\) is a contractive projection of
\(L^2(M,\tau)\) onto \(eL^2(M,\tau)e\) (Fact 2.6(a)), and it maps the dense set \(M\cap L^2\) into \(eMe\). By
definition \(eMe\) is dense in \(L^2(M_e,\tau_e)\). So the isometry extends to a unitary. The two module identities
and \(VJ=JV\) hold on \(eMe\) and extend by continuity. \(\square\)

## 15. Two-by-two matrices and the polar form of Theorem 10.4

Let \(M_2(M)\) act on \(H\oplus H\), with matrix units \(E_{ij}\), and write \(X=(x_{ij})\) for its elements. For a
self-adjoint \(h\in S(M,\tau)\) and a bounded Borel function \(f\) on \(\mathbb R\), \(f(h)\) is the bounded operator
\(f(T_h)\), which lies in \(M\) (Spectral calculus with its domains retained,
SK-08).

**Lemma 15.1.** For \(X\in M_2(M)_+\) put \(\tau_2(X)=\tau(x_{11})+\tau(x_{22})\). Then \(\tau_2\) is a faithful normal
semifinite trace on \(M_2(M)\), and \(\tau_2(X^*X)=\sum_{i,j}\tau(x_{ij}^*x_{ij})\) for \(X\in M_2(M)\). The commutant
of \(M_2(M)\) consists of the operators \(u'\oplus u'\) with \(u'\in M'\).

**Proof.** \(M_2(M)\) is \(M\bar\otimes B(\mathbb C^2)\), and \(\tau_2\) is the amplification of \(\tau\) by
\(B(\mathbb C^2)\). Proposition 6.5 of the lesson on traces
proves that it is a faithful normal semifinite trace, and the proof of Lemma 6.4 there computes the commutant. The
\((j,j)\) entry of \(X^*X\) is \(\sum_ix_{ij}^*x_{ij}\), which gives the formula. \(\square\)

We write \(U_2(r,d)\) for the sets of Section 1 built from \((M_2(M),\tau_2)\). All results of Sections 1–14 apply to
\((M_2(M),\tau_2)\).

**Proposition 15.2.** (a) Let \(X\in M_2(M)\) and \(r,d>0\). If every \(x_{ij}\) lies in \(U(r,d)\), then
\(X\in U_2(4r,8d)\). If \(X\in U_2(r,d)\), then every \(x_{ij}\) lies in \(U(r,d)\).

(b) The map \(X\mapsto(x_{ij})\) extends to a \(*\)-isomorphism of \(S(M_2(M),\tau_2)\) onto the algebra
\(M_2(S(M,\tau))\) of \(2\times2\) matrices over \(S(M,\tau)\), with the matrix operations. It is a homeomorphism for
the measure topology on the left and the product of the measure topologies on the right.

(c) Under this isomorphism, \(L^2(M_2(M),\tau_2)=M_2(L^2(M,\tau))\), and \(\|X\|_2^2=\sum_{i,j}\|x_{ij}\|_2^2\).

(d) Let \(h_1,h_2\in S(M,\tau)\) be self-adjoint, and let \(h_1\oplus h_2\) be the diagonal matrix with entries
\(h_1,h_2\). Then \(T_{h_1\oplus h_2}=T_{h_1}\oplus T_{h_2}\), and \(f(h_1\oplus h_2)=f(h_1)\oplus f(h_2)\) for every
bounded Borel function \(f\) on \(\mathbb R\).

**Proof.** (a) Let \(p_{ij}\) witness \(x_{ij}\in U(r,d)\), and let \(p=\bigwedge_{i,j}p_{ij}\). Then
\(\|x_{ij}p\|\leq\|x_{ij}p_{ij}\|<r\) and \(\tau(1-p)\leq\sum_{i,j}\tau(1-p_{ij})<4d\) (Fact 2.1(c)). For
\(P=p\oplus p\), the entries of \(XP\) are the \(x_{ij}p\), so \(\|XP\|<4r\), and \(\tau_2(1-P)=2\tau(1-p)<8d\).
Conversely, let \(P\) witness \(X\in U_2(r,d)\), and fix \(j\). Put \(Q=E_{jj}\wedge P\). The projection
\(E_{jj}-Q\) has zero meet with \(P\), so \(E_{jj}-Q\precsim1-P\) and \(\tau_2(E_{jj}-Q)\leq\tau_2(1-P)<d\) (Fact
2.1(a), (b), for the trace \(\tau_2\)). As \(Q\leq E_{jj}\), the only nonzero entry of \(Q\) is a projection
\(q\in M\) in place \((j,j)\), and \(\tau(1-q)=\tau_2(E_{jj}-Q)<d\). The \((i,j)\) entry of \(XQ\) is \(x_{ij}q\), and
\(Q\leq P\), so \(\|x_{ij}q\|\leq\|XQ\|=\|XPQ\|\leq\|XP\|<r\).

(b) By (a), the bijection \(X\mapsto(x_{ij})\) of \(M_2(M)\) onto \(M^4\) is a uniform isomorphism for the measure
uniformity of \(\tau_2\) on the left and the product of the measure uniformities of \(\tau\) on the right (Fact
2.2(b)). So it extends to a bijection of the completions \(S(M_2(M),\tau_2)\) and \(S(M,\tau)^4\), which we write as
matrices. Both uniformities have countable bases, given by the sets with \(r=d=1/n\), so every element of either
completion is the limit of a sequence from \(M_2(M)\), and convergent sequences are bounded in measure (Fact 2.2(b)).
Let \(X_n\to X\) and \(Y_n\to Y\) be such sequences. Then \(X_nY_n\), \(X_n+Y_n\) and \(X_n^*\) converge to \(XY\),
\(X+Y\) and \(X^*\) in \(S(M_2(M),\tau_2)\) (Fact 2.2(b), (c)). Their entries are the entries of the matrix product, sum
and adjoint of \((x_n)_{ij}\) and \((y_n)_{ij}\), which converge in \(S(M,\tau)\) to the matrix product, sum and
adjoint of the limits, for the same reason. So the extension carries the operations of \(S(M_2(M),\tau_2)\) to the
matrix operations.

(c) By Lemma 15.1, \(X\in M_2(M)\) lies in \(\mathfrak n_{\tau_2}\) exactly when every entry lies in
\(\mathfrak n_\tau\), and then \(\|X\|_2^2=\sum_{i,j}\|x_{ij}\|_2^2\). The bounded elements of \(L^2\) form
\(\mathfrak n_\tau\), which contains \(\mathfrak m_0\) and is therefore dense in \(L^2(M,\tau)\) (Fact 2.6(a)); the
same holds for \(\tau_2\). So \(M_2(\mathfrak n_\tau)\) is dense in both \(L^2(M_2(M),\tau_2)\) and
\(M_2(L^2(M,\tau))\), with the same norm on it. A sequence in \(M_2(\mathfrak n_\tau)\) that converges in one space is
Cauchy in the other. Its limits in the two spaces are both its limit in measure, by Fact 2.6(a) and part (b); so they
are equal. Hence the two spaces coincide, with the same norm.

(d) Take cutoffs for \(h_1\) and \(h_2\) (Fact 2.2(d)) and their meets: these are projections \(p_n\) with
\(\tau(1-p_n)\to0\) and \(h_1p_n,h_2p_n\in M\) (Fact 2.1(c)). By Fact 2.3(d), \(p_nH\subseteq D(T_{h_i})\) and
\(T_{h_i}p_n=h_ip_n\). By (b) the same holds for \(h_1\oplus h_2\) and \(P_n=p_n\oplus p_n\), with
\(T_{h_1\oplus h_2}P_n=h_1p_n\oplus h_2p_n\). The operator \(T_{h_1}\oplus T_{h_2}\) is self-adjoint, and it is
affiliated with \(M_2(M)\), because it commutes with every unitary \(u'\oplus u'\) of the commutant (Lemma 15.1). It
agrees with \(T_{h_1\oplus h_2}\) on \(P_n(H\oplus H)\), and \(\tau_2(1-P_n)=2\tau(1-p_n)\to0\). Graph uniqueness (Fact
2.3(b)) gives \(T_{h_1\oplus h_2}=T_{h_1}\oplus T_{h_2}\). The Borel calculus of an orthogonal direct sum of
self-adjoint operators is the direct sum of the calculi (SK-08, cited above). \(\square\)

**Theorem 15.3** (Polar form of Theorem 10.4). Let \(x,y\in L^2(M,\tau)\) have polar decompositions \(x=u|x|\) and
\(y=v|y|\). The function \(a\mapsto\|u1_{[\sqrt a,\infty)}(|x|)-v1_{[\sqrt a,\infty)}(|y|)\|_2^2\) is Lebesgue
measurable on \((0,\infty)\), and
\[
\int_0^\infty\bigl\|u1_{[\sqrt a,\infty)}(|x|)-v1_{[\sqrt a,\infty)}(|y|)\bigr\|_2^2\,da
\leq\frac1{\sqrt2}\,\|x-y\|_2\,\Bigl(\bigl\||x|+|y|\bigr\|_2^2+\bigl\||x^*|+|y^*|\bigr\|_2^2\Bigr)^{1/2}.
\tag{15.1}
\]
The constant is sharp: on \(M=\mathbb C\) with \(\tau(1)=1\), \(x=1\) and \(y=-1\) give \(4\) on both sides. For
self-adjoint \(x\) and \(y\), \(u1_{[\sqrt a,\infty)}(|x|)=G_a(x)\) and \(|x^*|=|x|\), and (15.1) is (10.5).

**Proof.** Put \(X=\begin{pmatrix}0&x\\x^*&0\end{pmatrix}\), a self-adjoint element of \(L^2(M_2(M),\tau_2)\) by
Proposition 15.2(c), and define \(Y\) from \(y\) in the same way. Then \(X^2=xx^*\oplus x^*x\), by Proposition
15.2(b). The diagonal matrix \(|x^*|\oplus|x|\) is positive, being the square of the self-adjoint matrix
\(|x^*|^{1/2}\oplus|x|^{1/2}\), and its square is \(X^2\). By uniqueness of positive square roots (Fact 2.3(g)),
\(|X|=|x^*|\oplus|x|\). The element \(u|x|u^*=(|x|^{1/2}u^*)^*(|x|^{1/2}u^*)\) is positive, and
\((u|x|u^*)^2=u|x|^2u^*=xx^*\) because \(u^*u|x|=|x|\); so \(|x^*|=u|x|u^*\). Hence \(u^*|x^*|=|x|u^*=x^*\), and with
\(W=\begin{pmatrix}0&u\\u^*&0\end{pmatrix}\),
\[
W|X|=\begin{pmatrix}0&u|x|\\u^*|x^*|&0\end{pmatrix}=X .
\]
The partial isometry \(W\) is self-adjoint, and \(W^*W=uu^*\oplus u^*u\). This is the support of \(|X|\), since the
supports of \(|x^*|\) and \(|x|\) are the left and right supports \(uu^*\) and \(u^*u\) of \(x\). The operator
\(\operatorname{sgn}(X)\) has the same two properties: \(\operatorname{sgn}(X)|X|=X\), and
\(\operatorname{sgn}(X)^*\operatorname{sgn}(X)=1_{\mathbb R\setminus\{0\}}(X)\) is the support of \(|X|\). So \(W\) and
\(\operatorname{sgn}(X)\) agree on the range of \(T_{|X|}\), which is dense in that support, and both vanish on its
orthogonal complement. Hence \(W=\operatorname{sgn}(X)\). Since \(G_a(t)=\operatorname{sgn}(t)1_{[\sqrt a,\infty)}(|t|)\),
the Borel calculus and Proposition 15.2(d) give
\[
G_a(X)=W\bigl(1_{[\sqrt a,\infty)}(|x^*|)\oplus1_{[\sqrt a,\infty)}(|x|)\bigr)
=\begin{pmatrix}0&u1_{[\sqrt a,\infty)}(|x|)\\ \ast&0\end{pmatrix}.
\]
As \(G_a\) is real, \(G_a(X)\) is self-adjoint, so its lower left entry is the adjoint of its upper right entry. The
same holds for \(Y\). By Proposition 15.2(c) and \(\|z^*\|_2=\|z\|_2\) (Fact 2.6(a)),
\[
\|G_a(X)-G_a(Y)\|_2^2=2\bigl\|u1_{[\sqrt a,\infty)}(|x|)-v1_{[\sqrt a,\infty)}(|y|)\bigr\|_2^2,\qquad
\|X-Y\|_2^2=2\|x-y\|_2^2,
\]
and \(\||X|+|Y|\|_2^2=\||x^*|+|y^*|\|_2^2+\||x|+|y|\|_2^2\). Theorem 10.4(2), applied to \((M_2(M),\tau_2)\) and to
\(X,Y\), gives the measurability and
\[
2\int_0^\infty\bigl\|u1_{[\sqrt a,\infty)}(|x|)-v1_{[\sqrt a,\infty)}(|y|)\bigr\|_2^2\,da
\leq\|X-Y\|_2\,\bigl\||X|+|Y|\bigr\|_2
=\sqrt2\,\|x-y\|_2\,\Bigl(\bigl\||x|+|y|\bigr\|_2^2+\bigl\||x^*|+|y^*|\bigr\|_2^2\Bigr)^{1/2},
\]
which is (15.1). In the example, \(u=1\), \(v=-1\) and \(|x|=|y|=1\); the integrand is \(4\) for \(0<a\leq1\) and \(0\)
afterwards, and the right side is \(2^{-1/2}\cdot2\cdot8^{1/2}=4\). For self-adjoint \(x\), \(u=\operatorname{sgn}(x)\),
so \(u1_{[\sqrt a,\infty)}(|x|)=G_a(x)\). \(\square\)

## 16. Exercises

**Exercise 1** (A finite trace and the endpoint of singular values). Let \(M=M_2(\mathbb C)\) with \(\tau=\frac12\operatorname{Tr}\), let \(T=\operatorname{diag}(3,1)\), and let \(f(\lambda)=1+\lambda\). Compute \(\lambda_s(T)\), \(\mu_t(T)\) and \(\mu_t(f(T))\). Check (9.1), the case distinction in Theorem 9.2(2), and the formula \(\tau(f(T))=\int_0^{\tau(1)}f(\mu_t(T))\,dt\).

*Solution.* Here \(\tau(1)=1\). The distribution is \(\lambda_s(T)=1\) for \(0\le s<1\), \(1/2\) for \(1\le s<3\), and \(0\) for \(s\ge3\). By (9.1), \(\mu_t(T)=3\) for \(0<t<1/2\), \(1\) for \(1/2\le t<1\), and \(0\) for \(t\ge1\). Since \(f(T)=\operatorname{diag}(4,2)\), the same computation gives \(\mu_t(f(T))=4,2,0\) on these three ranges. For \(t<1\) this is \(f(\mu_t(T))\). For \(t\ge1\) it is \(0\), not \(f(0)=1\): a cutoff \(e=0\) is allowed there. Finally \(\int_0^1f(\mu_t(T))\,dt=\frac12\cdot4+\frac12\cdot2=3=\frac12(4+2)=\tau(f(T))\).

**Exercise 2** (Truncations converge nearly everywhere, and the limit is closed). Let \(h\in S(M,\tau)_+\) and \(h_n=h1_{[0,n]}(h)\). Show that \((h_n)\) converges \(\tau\)-nearly everywhere, and that its limit operator is exactly \(h\), with domain \(D(h)\). Compare with Example 7.6.

*Solution.* Put \(e_n=1_{[0,n]}(h)\). These projections increase, and \(\tau(1-e_n)=\tau(1_{(n,\infty)}(h))\to0\) by the spectral-tail criterion (Fact 2.3(f)). So \(D=\bigcup_ne_nH\) is \(\tau\)-dense, and \(D\subseteq H=D(h_n)\). For \(\xi\in e_mH\), \(h_n\xi=h\xi\) once \(n\ge m\). So the sequence converges \(\tau\)-nearly everywhere. For any \(\xi\in H\), \(\|h_n\xi\|^2=\int_{[0,n]}\lambda^2\,d\langle E_h(\lambda)\xi,\xi\rangle\) increases with \(n\). If \((h_n\xi)\) converges, these numbers are bounded, so \(\xi\in D(h)\). Conversely, for \(\xi\in D(h)\), \(\|h\xi-h_n\xi\|^2=\int_{(n,\infty)}\lambda^2\,d\langle E_h(\lambda)\xi,\xi\rangle\to0\). So \(D(A)=D(h)\) and \(A=h\), which is closed. In Example 7.6 the limit operator was not closed, because the functions \(f_n\) there grow on shrinking sets instead of being truncations of one operator.

**Exercise 3** (The coupling trace for matrices). Let \(M=M_n(\mathbb C)\) with \(\tau=\operatorname{Tr}\), acting on \(\mathcal K=\mathbb C^n\otimes\mathbb C^m\) by \(\pi(x)=x\otimes1\). Show that \(\tau_\pi(1\otimes z)=\operatorname{Tr}(z)\) on \(\pi(M)'=1\otimes M_m(\mathbb C)\). For \(\zeta=e_1\otimes f_1\), compute \(h_\zeta\), \(y_\zeta\) and \(\|R(\zeta)\|_2\).

*Solution.* An operator commuting with all \(x\otimes1\) commutes with the matrix units \(E_{ij}\otimes1\). Such an operator has the form \(1\otimes z\), so \(\pi(M)'=1\otimes M_m(\mathbb C)\). Next, \(\langle\pi(x)\zeta,\zeta\rangle=\langle xe_1,e_1\rangle=\operatorname{Tr}(xE_{11})\), so the density is \(E_{11}\) and \(h_\zeta=E_{11}\). Then \(Mh_\zeta\) is the set of matrices supported in the first column, and \(y_\zeta(xE_{11})=xe_1\otimes f_1\). So \(y_\zeta y_\zeta^*=1\otimes F_{11}\), where \(F_{11}\) projects onto \(f_1\), and \(y_\zeta^*y_\zeta\) is the projection onto first-column matrices, which is \(\rho(E_{11})\). By (12.1), \(\tau_\pi(1\otimes F_{11})=\tau_N(\rho(E_{11}))=\operatorname{Tr}(E_{11})=1\). Every minimal projection \(1\otimes F\) of \(\pi(M)'\) is unitarily equivalent in \(\pi(M)'\) to \(1\otimes F_{11}\), so it has trace \(1\). A normal trace on \(M_m(\mathbb C)\) is fixed by its value on minimal projections, so \(\tau_\pi(1\otimes z)=\operatorname{Tr}(z)\). Finally \(\|R(\zeta)\|_2^2=\tau_N(\rho(h_\zeta^2))=\operatorname{Tr}(E_{11})=1=\|\zeta\|^2\).

**Exercise 4** (A minimal projection gives a continuous functional). Let \(M=\ell^\infty(\mathbb N)\) with the finite trace \(\tau(f)=\sum_n2^{-n}f(n)\). Show that \(\varphi(f)=f(1)\) is continuous for the measure topology. Which hypothesis of Theorem 6.2 fails?

*Solution.* Take \(d<1/2=\tau(\delta_1)\). If \(f\in U(r,d)\) with witness \(1_E\), then \(1\in E\), since otherwise \(\tau(1-1_E)\ge1/2\). So \(|f(1)|\le\|f1_E\|<r\). This proves continuity at \(0\). The algebra has the minimal projection \(\delta_1\), so it is not diffuse. This is an instance of Example 6.4.

**Exercise 5** (Decreasing projections). Let \(e_1\ge e_2\ge\dots\) be projections with \(\tau(e_1)<\infty\) and \(\bigwedge_ne_n=0\). Show that \(e_n\to0\) both in measure and \(\tau\)-nearly everywhere. Show by an example that \(\tau(e_1)<\infty\) is needed for convergence in measure.

*Solution.* Normality gives \(\tau(e_n)\to0\), because \(e_1-e_n\) increases to \(e_1\). Since \(e_n(1-e_n)=0\), \(e_n\in U(r,d)\) for every \(r\) once \(\tau(e_n)<d\). Also \(e_n\to0\) strongly, so the convergence holds on \(D=H\). Without the finite trace, take \(M=\ell^\infty(\mathbb N)\) with the counting trace and \(e_n=1_{\{n,n+1,\dots\}}\). Then \(e_n\to0\) strongly, so \(\tau\)-nearly everywhere. But every nonzero projection has trace at least \(1\), so for \(d<1\) the set \(U(1,d)\) is the open unit ball, which does not contain \(e_n\).

## 17. Where this leads

- The polar form of Theorem 10.4 is Theorem 15.3. It rests on the identification of the measurable operators and of \(L^2\) of \(M_2(M)\) with \(2\times2\) matrices over those of \(M\) (Proposition 15.2).
- Generalized singular values lead to majorization, to Hölder-type inequalities for \(\mu_t\), and to symmetric spaces of measurable operators [Fack–Kosaki 1986].
- Theorem 13.4, in which the vectors of a representation become square-integrable intertwiners with \(\pi(M)'\) acting on the left and \(N\) on the right, is the starting point for bimodules (correspondences), spatial derivatives and relative tensor products.
- All results here use a trace. Measurable operators and \(L^p\) spaces for weights that are not traces need other constructions, such as Haagerup's \(L^p\) spaces [Hiai, Chapter 11].

## References



- [Fack–Kosaki 1986] T. Fack and H. Kosaki, Generalized \(s\)-numbers of \(\tau\)-measurable operators, *Pacific Journal of Mathematics* 123 (1986), 269–300. https://doi.org/10.2140/pjm.1986.123.269
- [Kostecki 2014] R. P. Kostecki, \(W^*\)-algebras and noncommutative integration, survey, version 5, 2014. https://arxiv.org/abs/1307.4818
- [Nelson 1974] E. Nelson, Notes on non-commutative integration, *Journal of Functional Analysis* 15 (1974), 103–116. https://doi.org/10.1016/0022-1236(74)90014-7. Free at https://linkinghub.elsevier.com/retrieve/pii/0022123674900147
- [Hiai 2021] F. Hiai, *Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383. Free at
  https://arxiv.org/abs/2004.02383

- [Hiai] F. Hiai, *Concise lectures on selected topics of von Neumann algebras*, 2020, [arXiv:2004.02383](https://arxiv.org/abs/2004.02383); published as *Lectures on Selected Topics in von Neumann Algebras*, EMS Series of Lectures in Mathematics, EMS Press, 2021.
