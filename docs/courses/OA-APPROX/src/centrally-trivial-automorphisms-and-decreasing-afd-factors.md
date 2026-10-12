# Centrally trivial automorphisms and decreasing AFD factors

*Written by GPT-6.1 Sol (OpenAI), Ultra. New original exposition: CC0-1.0 to the extent of rights held. Earlier programme and human-source notices retain their own terms.*

Uniform displacement and finite normal-functional tests answer different questions. The first detects an outer automorphism by looking arbitrarily far down a tensor tail. The second lets an approximately inner automorphism be compared with a centrally trivial one. We first construct the tail and fixed-algebra examples, then prove the two-state comparison and finish the abstract group criterion.

The complete [CT0–5 inputs](../components/centrally-trivial-and-bernoulli-inputs.md) supply normal transport, approximate innerness of every automorphism of \(R\), the tensor relative commutant, finite and infinite Bernoulli products, direct irreducibility of the finite fixed algebras, and compact twisted-orbit minimization. The [strong-stability lesson](strong-stability-and-tensor-absorption.md) supplies the whole absorption theorem; the [quotient and exact-lift lesson](central-sequence-algebras-and-exact-lifts.md) and [fullness/corner lesson](fullness-hypercentrality-and-ultrafilter-corners.md) supply the ordinary and all-ultrafilter alternatives at full factor scope.

<a id="1-central-triviality-and-two-fixed-states"></a>

## Normal transport and the groups being compared

Until a finite-factor hypothesis is explicitly imposed, \(M\) is a nonzero factor with separable predual. Automorphisms are normal, and their \(u\)-topology is pointwise norm convergence on \(M_*\). CT0 proves a countable neighborhood basis and continuity of the group operations from the predual isometries. A faithful normal state exists by NT2. For a positive normal state \(\sigma\), write \(\|x\|_\sigma^2=\sigma(x^*x)\), and use the two-square seminorm
\(\|x\|_{\varphi,\#}^2=(\varphi(x^*x)+\varphi(xx^*))/2\).

An automorphism \(\theta\) belongs to \(\operatorname{Cnt}(M)\) when
\[
\theta(x_n)-x_n\longrightarrow0\quad\hbox{strong*}
\tag{1}
\]
for every bounded ordinary centralizing sequence. The normal transport identity of CT0 makes this a normal subgroup. For composition, add \(\theta(\rho(x_n)-x_n)\) to \(\theta(x_n)-x_n\); both differences vanish strong*. For the inverse, apply the condition to \(\theta^{-1}(x_n)\) and apply \(\theta^{-1}\) to the difference. The same identity handles conjugation, as Exercise 1 spells out. Every inner automorphism is centrally trivial: centrality gives a strong*-zero commutator with its fixed implementing unitary, and fixed multiplication preserves that convergence.

For unitaries the exact identity is
\[
\operatorname{Ad}(u_n)\to\operatorname{id}\text{ in }u
\quad\Longleftrightarrow\quad
\|[u_n,\psi]\|\to0\quad(\psi\in M_*).
\tag{2}
\]
Here \([x,\psi](z)=\psi(zx)-\psi(xz)\); CT0 proves equality of the corresponding functional norms by unitary multiplication. Inner automorphisms form a normal subgroup, as does their closure. All quotients used below are abstract groups; no closedness of the inner subgroup is assumed.

**Exercise 1.** Prove directly that \(\operatorname{Cnt}(M)\) is normal in \(\operatorname{Aut}(M)\).

*Solution.* Fix a bounded centralizing \(x_n\), a normal \(\gamma\), and \(\theta\in\operatorname{Cnt}(M)\). For each \(\psi\), CT0.1 expresses the commutator of \(\gamma^{-1}(x_n)\) as the original commutator with a normal precomposed test, so this sequence is centralizing. Hence \(\theta(\gamma^{-1}(x_n))-\gamma^{-1}(x_n)\) tends strong* to zero. Applying the fixed normal \(\gamma\) preserves every normal two-square test and gives \(\gamma\theta\gamma^{-1}(x_n)-x_n\to0\). This is the required membership of the conjugate.

<a id="4-a-uniform-displacement-criterion-in-finite-factors"></a>

## An intertwiner detects uniform displacement

Here \(M\) is any \(\mathrm{II}_1\) factor, including one with nonseparable predual. Its normalized trace is faithful normal by FH0, which also proves trace preservation by every automorphism.

**Lemma 4.1.** Let \(D\subset M\) be a unital finite type I subfactor and \(C=D'\cap M\). If \(\alpha\in\operatorname{Aut}(M)\) satisfies
\[
d=\sup_{u\in\mathcal U(C)}\|\alpha(u)-u\|_2<1,
\tag{22}
\]
then \(\alpha\) is inner.

**Proof.** CT5 constructs the ultraweakly closed convex hull \(K\) of \(u\alpha(u^*)\), \(u\in\mathcal U(C)\). It is compact in the operator unit ball and lies in the ultraweakly closed trace ball of radius \(d<1\) about \(1\). In particular \(0\notin K\). Compact sublevel sets of the lower semicontinuous trace norm yield its least-norm point \(y\). The midpoint identity and trace faithfulness prove uniqueness.

For \(v\in\mathcal U(C)\), \(x\mapsto vx\alpha(v^*)\) bijects this convex set isometrically; hence it fixes \(y\ne0\). The four-unitary span extends the resulting relation to
\[
y\alpha(x)=xy,\qquad x\in C.
\tag{23}
\]
CT1 supplies the complete finite-matrix implementer: if \(e_{ij}\) generate \(D\) and \(f_{ij}=\alpha(e_{ij})\), equal-trace comparison gives \(v^*v=e_{11}\), \(vv^*=f_{11}\), and
\[
w=\sum_i f_{i1}ve_{1i}
\tag{24}
\]
is unitary with \(we_{ij}w^*=f_{ij}\). Thus \(\beta=\operatorname{Ad}(w^*)\alpha\) fixes \(D\) pointwise, and maps \(C\) onto \(C\).

Put \(a=yw\ne0\). Substituting \(\alpha(x)=w\beta(x)w^*\) in (23) gives
\[
a\beta(x)=xa,\qquad x\in C.
\tag{25}
\]
SS0's exact \(M=D\bar\otimes C\) coordinates give at least one nonzero coefficient \(z\in C\), and extracting coefficients in this equation gives \(z\beta(x)=xz\). Adjointing at \(x^*\) gives \(\beta(x)z^*=z^*x\). These two identities make \(zz^*\) commute with \(C\), and \(z^*z\) commute with \(\beta(C)=C\). The matrix-coordinate center calculation makes \(C\) a factor. Consequently both positive elements are nonzero scalars, equal because both norms are \(\|z\|^2\). Hence \(q=z/\|z\|\) is unitary and
\[
\beta(x)=q^*xq,\qquad x\in C.
\tag{26}
\]
This equality also holds on \(D\), because \(\beta\) fixes it and \(q\in C\). The two algebras generate all \(M\), and the normal maps agree there. Therefore \(\alpha=\operatorname{Ad}(wq^*)\). The proof retains arbitrary \(\mathrm{II}_1\) factors and the original strict threshold \(d<1\). \(\square\)

**Exercise 8.** Why is the least-norm intertwiner in Lemma 4.1 nonzero?

*Solution.* Every orbit element has distance \(\|u\alpha(u^*)-1\|_2=\|\alpha(u)-u\|_2\leq d\) from \(1\). The centered trace ball is convex and ultraweakly closed, by its supremum of normal scalar pairings, so it contains \(K\). Zero has distance \(1>d\) and cannot belong to \(K\). The compact-sublevel minimizer belongs to \(K\), hence is nonzero. The midpoint square identity gives uniqueness, allowing each orbit-preserving isometry to fix it and produce the intertwining equation.

**Exercise 9.** From \(z\beta(x)=xz\) and the unitary \(q=z/\|z\|\), determine the implementing unitary with its correct adjoint.

*Solution.* Divide by the positive scalar \(\|z\|\) to obtain \(q\beta(x)=xq\), then multiply on the left by \(q^*\). This gives \(\beta(x)=q^*xq=\operatorname{Ad}(q^*)(x)\), under the convention \(\operatorname{Ad}(v)(x)=vxv^*\). Since \(\alpha=\operatorname{Ad}(w)\beta\), its implementer is \(wq^*\). The same formula fixes \(D\) because \(q\in D^c\), and so implements the entire automorphism.

**Theorem 4.2.** For the separable AFD \(\mathrm{II}_1\) factor \(R\),
\[
\operatorname{Cnt}(R)=\operatorname{Int}(R),\qquad
\chi(R)=\{1\}.
\tag{27}
\]
Every outer \(\alpha\in\operatorname{Aut}(R)\) induces a nonidentity automorphism of \(R_\omega\), for every free ultrafilter.

**Proof.** In the complete dyadic model let \(D_n\) be the increasing full matrix heads and \(C_n=D_n'\cap R\). If \(\alpha\) is outer, the contrapositive of Lemma 4.1 gives
\[
\sup_{u\in\mathcal U(C_n)}\|\alpha(u)-u\|_2\geq1.
\tag{28}
\]
Choose a unitary \(u_n\in C_n\) with displacement at least \(1/2\). AF1's bounded trace approximations in the heads show that for each fixed \(x\in R\) and \(a\in D_k\),
\(\|[u_n,x]\|_2\leq2\|x-a\|_2\) when \(n\geq k\). Approximation and the identical adjoint estimate give intrinsic centrality; the trace functional commutator is zero. The complete tracial centrality criterion therefore makes \(u_n\) ordinary centralizing. Its displacement fails to vanish strong*, so \(\alpha\notin\operatorname{Cnt}(R)\). Every inner automorphism is centrally trivial by the setup, proving the first equality in (27).

CT0 proves that \(\alpha\) induces a trace-preserving normal automorphism of every \(R_\omega\). Both \(u_n\) and \(\alpha(u_n)\) are centralizing. The complete quotient trace identity gives
\[
\|\pi_\omega(\alpha(u_n)-u_n)\|_{2,\tau_\omega}^2
=\lim_{n\to\omega}\|\alpha(u_n)-u_n\|_2^2\geq1/4.
\]
Thus the induced map moves a quotient element for every free \(\omega\). The characteristic group is
\[
\chi(M)=\bigl(\operatorname{Cnt}(M)\cap
\overline{\operatorname{Int}(M)}\bigr)/\operatorname{Int}(M).
\tag{21}
\]
Its numerator contains the inner subgroup and is normal; at \(R\) the first equality in (27) makes this quotient trivial. This proves all the conclusions. \(\square\)

**Exercise 10.** Show that an outer automorphism of \(R\) acts nontrivially on \(R_\omega\) for every free ultrafilter.

*Solution.* Use the same \(u_n\in C_n\) with displacement at least \(1/2\). Bounded finite-head approximation proves ordinary centralizing, so the sequence belongs to \(C_\omega\) for each \(\omega\). Normal transport gives the same property for \(\alpha(u_n)\), and preservation of \(J_\omega\) makes the induced map well defined. Its quotient difference has squared trace norm equal to the coordinate squared-norm ultralimit, at least \(1/4\). It is nonzero, so the quotient image of \(u_n\) is moved. The argument retains the nonidentity conclusion, without asserting the stronger outer-action conclusion for the induced map.

<a id="5-decreasing-irreducible-hyperfinite-subfactors"></a>

## Independent tensor supports give the decreasing example

**Theorem 5.1.** \(R\) admits a decreasing sequence of AFD \(\mathrm{II}_1\) subfactors \(R_n\) satisfying
\[
R_n'\cap R=\mathbb C,\qquad
\bigcap_{n\ge1}R_n=\mathbb C.
\tag{29}
\]

**Proof.** Use \(G=\bigcup_nG_n\), the group of finitary permutations of \(\mathbb N\), with \(G_n\) permuting its first \(n\) points. Each \(G_n\) is finite, these groups increase, and their union is countably infinite: it is a countable union of finite sets and contains infinitely many distinct transpositions.

CT3 constructs the whole faithful normal tracial product
\[
B=\overline{\bigotimes_{h\in G}}(R_h,\tau_h)\cong R
\tag{30}
\]
from the countably many dyadic legs \(G\times\mathbb N\). The left action has the explicit convention
\[
\alpha_g\left(\bigotimes_hx_h\right)=
\bigotimes_hx_{g^{-1}h}.
\tag{31}
\]
Trace-vector unitaries give its normal extension and all group identities. In coordinate \(e\), the moving trace-zero dyadic unitaries \(\widetilde a_r\) are ordinary centralizing; their translate at \(g\ne e\) has distinct coordinate support and
\[
\|\alpha_g(\widetilde a_r)-\widetilde a_r\|_2^2=2.
\tag{32}
\]
Thus the action is outer at every nonidentity element, as CT3 proves directly.

Put \(N_n=B^{G_n}\). CT4 proves \(N_n'\cap B=\mathbb C\) by a direct orthogonal-marker argument. Namely, approximate a commuting \(x\) by a finite-support \(x_L\), choose a coordinate outside \(G_n(L\cup F)\), and sum the \(G_n\)-translates of a local operator times its trace-zero markers. The sum belongs to \(N_n\); the mutually orthogonal marker coefficients make its commutator norm squared the sum of the coefficient commutator squares. This forces \(x\) to commute with every local operator, hence to be scalar.

CT4 also proves the full type conclusion: \(N_n\) has a faithful normal restricted trace and scalar center, while its invariant diagonal orbit sums have arbitrarily small positive trace. Finite comparison excludes a minimal projection; the full type criterion gives \(\mathrm{II}_1\), without assuming that a fixed algebra of a finite action is automatically a factor.

For AFD use the concrete invariant stages
\[
A_m=\bigotimes_{h\in G_m}D_m\otimes1_{\text{outside }G_m}.
\tag{33}
\]
They are increasing finite matrix algebras, and generate \(B\). For \(m\geq n\) they are invariant under left translation by \(G_n\). At \(x\in N_n\), AF1's bounded trace approximants in \(A_m\), averaged over the finite group \(G_n\), belong to \(A_m^{G_n}\) and still converge in trace norm to \(x\). The average is a trace contraction fixing \(x\). Thus these increasing finite-dimensional fixed stages generate \(N_n\). Its predual embeds isometrically into \(B_*\) by its finite normal expectation, so it is separable. AF5 identifies each \(N_n\) normally with \(R\).

The increasing groups make the fixed algebras decreasing, with intersection \(B^G\). If \(a,b\) have finite coordinate supports \(F,H\), respectively, then \(gF\cap H=\varnothing\) when \(g\notin HF^{-1}\). Product trace independence gives
\[
\tau(\alpha_g(a)b)=\tau(a)\tau(b)
\quad(g\notin HF^{-1}).
\tag{34}
\]
For arbitrary \(a,b\in B\), choose bounded finite-stage approximants \(a_0,b_0\). Trace Schwarz bounds the pairing error, uniformly in \(g\), by
\[
\|a-a_0\|_2\|b\|_2+\|a_0\|_2\|b-b_0\|_2.
\]
The trace product has the same approximation bound. Decreasing both errors and excluding the finite exceptional set for \(a_0,b_0\) proves
\[
\lim_{g\to\infty}\tau(\alpha_g(a)b)=\tau(a)\tau(b),
\tag{35}
\]
where the limit is outside every finite subset of this infinite discrete group.

At a fixed \(x\in B^G\) with \(\tau(x)=0\), choose \(a=x,b=x^*\). Its pairing is constantly \(\tau(xx^*)\), but (35) makes it zero. Trace faithfulness gives \(x=0\). Subtracting the trace of an arbitrary fixed operator shows \(B^G=\mathbb C1\). A normal identification \(B\cong R\) carries \(N_n\) to the requested \(R_n\), preserving irreducibility, type, AFD and intersection. This proves (29). \(\square\)

**Exercise 11.** Verify the squared displacement in (32) from the two distinct tensor coordinates.

*Solution.* The original and translated trace-zero unitaries each have squared trace norm one. Since their supports are distinct, their mixed trace is the product of the two individual traces, hence zero. Expansion therefore gives \(1+1-2\operatorname{Re}(0)=2\). The trace-zero choice is essential: using scalar units would leave the coordinate tensor unchanged and would not produce displacement.

**Exercise 12.** Find the finite exceptional set in the disjoint-support argument and prove the scalar fixed-point conclusion.

*Solution.* The intersection \(gF\cap H\) is nonempty exactly when \(gf=h\) for some \(f\in F,h\in H\), so every exception lies in the finite \(HF^{-1}\). Outside it, independent coordinate trace factors give (34). For general operators the two trace-Schwarz bounds in the proof are uniform in \(g\), so bounded trace approximation gives (35). A trace-zero fixed \(x\) has the constant pairing \(\tau(xx^*)\), which (35) makes equal to zero. Faithfulness gives \(x=0\), and subtracting \(\tau(x)1\) from any fixed element proves that every fixed element is scalar.

## A centrally trivial automorphism controls two fixed states

**Lemma 1.1.** If \(\theta\in\operatorname{Cnt}(M)\), finitely many normal states \(\sigma_j\), and \(\varepsilon>0\) are given, there is a neighborhood \(V\) of the identity such that
\[
\operatorname{Ad}(u)\in V
\quad\Longrightarrow\quad
\|\theta(u)-u\|_{\sigma_j}<\varepsilon
\quad\text{for all }j,
\tag{3}
\]
where \(\|a\|_\sigma=\sigma(a^*a)^{1/2}\).

**Proof.** CT0 gives a countable decreasing neighborhood basis \(V_n\) at the identity. If the assertion fails, for each \(n\) choose a unitary \(u_n\) with \(\operatorname{Ad}(u_n)\in V_n\) and at least one of the finitely many seminorms at least \(\varepsilon\). Equation (2) makes this a bounded ordinary centralizing sequence. Central triviality forces \(\theta(u_n)-u_n\to0\) strong*, hence each of the finitely many normal-state square tests tends to zero. Their finite maximum tends to zero, contradicting the selected violations. This gives the full simultaneous finite-state assertion. \(\square\)

**Theorem 1.2.** In \(\operatorname{Out}(M)\), the images of
\(\overline{\operatorname{Int}(M)}\) and \(\operatorname{Cnt}(M)\) commute.

**Proof.** Fix an approximately inner \(\alpha\), a centrally trivial \(\theta\), and a faithful normal \(\varphi\). The two normal states that remain fixed throughout the construction are
\[
\sigma_1=\varphi\alpha^{-1},\qquad
\sigma_2=\varphi\theta\alpha^{-1}\theta^{-1}.
\tag{4}
\]
Apply Lemma 1.1 with tolerance \(2^{-n}\) to both. Its neighborhoods \(V_n\) and continuity of the group operations allow nested neighborhoods \(W_n\) of \(\alpha\), shrinking in a countable basis, such that
\[
W_nW_n^{-1}\subseteq V_n
\tag{5}
\]
and for every \(\beta\in W_n\),
\[
\begin{aligned}
\|\varphi\beta^{-1}-\sigma_1\|&<4^{-n},\\
\|\varphi\theta\beta^{-1}\theta^{-1}-\sigma_2\|&<4^{-n}.
\end{aligned}
\tag{6}
\]
Continuity at the pair \((\alpha,\alpha)\) gives the first inclusion, and the two predual evaluations give the other open constraints; intersection with the earlier neighborhood and basis element makes the choices nested.

Choose \(\alpha_n=\operatorname{Ad}(u_n)\in W_n\), possible by \(\alpha\) lying in the closure, and put
\[
v_n=u_{n+1}u_n^*,\qquad w_n=u_n^*\theta(u_n).
\tag{7}
\]
Then \(\operatorname{Ad}(v_n)=\alpha_{n+1}\alpha_n^{-1}\in V_n\), so both \(\sigma_i\)-seminorms of \(\theta(v_n)-v_n\) are less than \(2^{-n}\). The exact successive identities are
\[
w_{n+1}-w_n
=u_n^*(v_n^*\theta(v_n)-1)\theta(u_n),
\tag{8}
\]
\[
w_{n+1}^*-w_n^*
=\theta(u_n)^*(\theta(v_n)^*v_n-1)u_n.
\tag{11}
\]
For the first, left unitary multiplication preserves the \(\varphi\)-seminorm, while its right multiplier changes the testing state to
\(\varphi\operatorname{Ad}(\theta(u_n)^*)=\varphi\theta\alpha_n^{-1}\theta^{-1}\).
The middle expression is
\[
v_n^*\theta(v_n)-1=v_n^*(\theta(v_n)-v_n),
\tag{9}
\]
so its \(\sigma_2\)-square is less than \(4^{-n}\) and its operator norm at most two. The state difference in (6) contributes at most \(4\cdot4^{-n}\). Thus
\[
\|w_{n+1}-w_n\|_\varphi^2\leq5\cdot4^{-n}.
\tag{10}
\]
For the adjoint identity the right multiplier changes the state to
\(\varphi\operatorname{Ad}(u_n^*)=\varphi\alpha_n^{-1}\), approximating \(\sigma_1\). Its middle expression is \(-\theta(v_n)^*(\theta(v_n)-v_n)\), again a left unitary multiple with norm at most two. Hence it satisfies the same square bound. Consequently
\[
\|w_{n+1}-w_n\|_\varphi+
\|w_{n+1}^*-w_n^*\|_\varphi
\leq2\sqrt5\,2^{-n}.
\tag{12}
\]
Summing the tails makes \(w_n\) Cauchy for the complete strong* unitary metric proved in the central-sequence lesson. Its limit \(w\) is a unitary. CT0's vector-pair proof makes their inner automorphisms \(u\)-convergent; continuity of the group operations gives
\[
\operatorname{Ad}(w)
=\lim_n\alpha_n^{-1}\theta\alpha_n\theta^{-1}
=\alpha^{-1}\theta\alpha\theta^{-1}.
\tag{13}
\]
This commutator is inner. Inner automorphisms are a normal subgroup, so the corresponding two abstract outer classes commute. No Hausdorff topology on the outer quotient is required. \(\square\)

**Exercise 2.** Derive (8) from (7), including the adjoint identity needed for the second seminorm.

*Solution.* The definition gives \(u_{n+1}=v_nu_n\), so
\(w_{n+1}=u_n^*v_n^*\theta(v_n)\theta(u_n)\).
Subtract \(w_n=u_n^*\theta(u_n)\) and factor the fixed outer multipliers to obtain (8). Taking adjoints reverses their order and gives exactly (11). Thus the right multiplier for the first difference is \(\theta(u_n)\), and that for the adjoint is \(u_n\), which determines the two tested states.

**Exercise 3.** Explain why both fixed states in (4) are needed.

*Solution.* For a one-sided seminorm, left multiplication by a unitary changes nothing, but right multiplication by \(r\) changes the state to \(x\mapsto\varphi(r^*xr)\). In (8) this is \(\varphi\operatorname{Ad}(\theta(u_n)^*)\), whose norm limit is \(\sigma_2\). In (11) it is \(\varphi\operatorname{Ad}(u_n^*)\), whose norm limit is \(\sigma_1\). Lemma 1.1 must therefore control the same middle difference under both states. One square alone would not give the two-sided strong* Cauchy property or the complete unitary limit.

**Exercise 4.** Prove that (12) makes the sequence Cauchy for the complete unitary metric.

*Solution.* For \(m>n\), the triangle inequality bounds the two-seminorm metric distance by
\[
\sum_{k=n}^{m-1}2\sqrt5\,2^{-k}\leq4\sqrt5\,2^{-n}.
\]
This tends to zero uniformly in \(m>n\). The earlier complete unitary metric consequently gives a unitary strong* limit, not merely a contraction or one-sided limit. CT0 then gives \(u\)-convergence of its inner automorphisms, and (13) identifies the automorphism it implements.

The numerator defining \(\chi(M)\) in (21) is the intersection of two normal subgroups containing \(\operatorname{Int}(M)\). Applying Theorem 1.2 to any two elements in this intersection proves that \(\chi(M)\) is abelian for every factor in the stated general setting.

<a id="2-commutative-central-algebras-force-central-triviality"></a>

## Finite tests turn hypercentrality into a group statement

**Lemma 2.1.** If all ordinary centralizing sequences are hypercentral, then for every \(\eta>0\) and faithful normal state \(\varphi\) there are finitely many normal states \(\psi_j\), including \(\varphi\), and \(\delta>0\) such that
\[
\begin{gathered}
\|x\|,\|y\|\le1,\qquad
\|[x,\psi_j]\|,\|[y,\psi_j]\|<\delta\quad\text{for every }j\\
\Longrightarrow\quad
\|[x,y]\|_{\varphi,\#}<\eta.
\end{gathered}
\tag{14}
\]

**Proof.** Fix \(\eta>0\) and faithful normal \(\varphi\). If no finite tests work, take the first \(n\) members of a norm-dense normal-state family together with \(\varphi\), and tolerance \(1/n\). Choose contractions \(x_n,y_n\) satisfying these tests but with \(\|[x_n,y_n]\|_{\varphi,\#}\geq\eta\). Norm density, NT1's four-positive-functional decomposition and the uniform commutator bound \(2\|\psi-\xi\|\) make both sequences centralizing for every normal test. Universal hypercentrality says their commutator tends strong* to zero. NT2 makes its two-square faithful-state seminorm tend to zero, contradicting the fixed lower bound. This proves (14) with \(\varphi\) included among the tests. \(\square\)

**Theorem 2.2.** If \(M_\omega\) is commutative for one free ultrafilter, then
\[
\overline{\operatorname{Int}(M)}\subset\operatorname{Cnt}(M),
\qquad
\overline{\operatorname{Int}(M)}/\operatorname{Int}(M)
\text{ is abelian}.
\tag{15}
\]

**Proof.** The completed hypercentrality theorem says that a commutative \(M_\omega\) at one free \(\omega\) makes every ordinary centralizing sequence hypercentral. Fix \(\varepsilon>0\) and a faithful normal \(\varphi\). Apply Lemma 2.1 with \(\eta=\varepsilon/\sqrt2\) and decrease its tolerance to ensure \(\delta\leq\varepsilon^2/4\).

Let \(V\) impose \(\|\psi_j\beta-\psi_j\|<\delta\) for all its finite tests, including \(\varphi\). If \(\beta=\operatorname{Ad}(u)\in V\), (2) gives the required commutator tests for \(u\). For any contraction \(x\) satisfying those tests, set \(z=[u,x]\), with \(\|z\|\leq2\). Lemma 2.1 gives \(\|z\|_{\varphi,\#}<\eta\), and \(\beta(x)-x=zu^*\). Its two squares give the full right-multiplier estimate
\[
\begin{aligned}
\|\beta(x)-x\|_{\varphi,\#}^2
&=\tfrac12\varphi(uz^*zu^*)+\tfrac12\varphi(zz^*)\\
&\leq\|z\|_{\varphi,\#}^2+
\tfrac12\|\varphi\beta-\varphi\|\,\|z\|^2\\
&\leq\eta^2+2\delta\leq\varepsilon^2.
\end{aligned}
\tag{16}
\]
This bound holds also for \(\beta\in\overline{\operatorname{Int}(M)}\cap V\). Approximate it by inner maps eventually in the open \(V\). CT0 proves pointwise strong* convergence at this fixed \(x\), so both normal-state squares converge and the bound passes with weak inequalities.

For a fixed \(\theta\in\overline{\operatorname{Int}(M)}\), choose an inner \(\operatorname{Ad}(w)\) sufficiently near it that
\(\beta=\theta\operatorname{Ad}(w)^{-1}\in V\).
For a contraction centralizing sequence, its finitely many tests hold eventually and
\[
\theta(x_n)-x_n
=\beta(wx_nw^*-x_n)+(\beta(x_n)-x_n).
\tag{17}
\]
The first term tends strong* to zero by centrality with fixed \(w\) and normal transport by fixed \(\beta\). The second has faithful-state symmetric seminorm at most \(\varepsilon\). Hence the limsup of the seminorm of the left side is at most \(\varepsilon\). That left side is independent of the approximation chosen for each \(\varepsilon\); making \(\varepsilon\) arbitrarily small proves its convergence to zero. NT2 gives strong*, and scaling covers every bounded sequence. Thus \(\theta\) is centrally trivial.

Theorem 1.2 now applies to two arbitrary members of the inner closure, since each is centrally trivial. Their outer classes commute, which proves the abstract quotient in (15) abelian. \(\square\)

**Exercise 5.** Identify the right-multiplication error in (16).

*Solution.* The first square of \(zu^*\) is tested as \(\varphi(uz^*zu^*)\); the adjoint square is exactly \(\varphi(zz^*)\). The first differs from \(\varphi(z^*z)\) by at most \(\|\varphi\operatorname{Ad}(u)-\varphi\|\|z\|^2\). The symmetric seminorm halves this error. Since \(\|z\|\leq2\) and the \(\varphi\)-test is less than \(\delta\), its contribution is at most \(2\delta\). Together with \(\eta^2=\varepsilon^2/2\) and \(\delta\leq\varepsilon^2/4\), this gives the entire \(\varepsilon^2\) bound.

<a id="3-the-complete-group-criterion-for-absorption"></a>

## Noncommuting outer classes complete the absorption criterion

**Theorem 3.1.** For a factor \(M\) with separable predual, strong stability is equivalent to noncommutativity of the abstract quotient group
\[
\overline{\operatorname{Int}(M)}/\operatorname{Int}(M).
\tag{18}
\]
Together with the preceding absorption theorem, this completes all four characterizations of strong stability.

**Proof.** If \(M\) does not absorb \(R\), the complete strong-stability equivalence makes \(M_\omega\) commutative for every free \(\omega\). Theorem 2.2 therefore makes the abstract quotient (18) abelian.

Suppose instead \(M\cong N\bar\otimes R\), taking \(N=M\) in an absorption isomorphism, so \(N\) is a factor with separable predual. CT3 applied to the finite group \(S_3\) constructs an everywhere-outer action \(\gamma\) on a complete product normally isomorphic to \(R\). The coordinate algebras are copies of \(R\), so the product is type \(\mathrm{II}_1\) even for this finite index group. Its moving dyadic coordinate-tail unitaries prove outerness at every nonidentity element.

Let \(s=(12)\), \(t=(23)\) and \(c=sts^{-1}t^{-1}=(132)\ne e\), with rightmost-first composition. CT1 proves that every automorphism of \(R\), in particular \(\gamma_s,\gamma_t\), is approximately inner. CT2 transports their approximating inner maps to
\[
\alpha=\operatorname{id}_N\otimes\gamma_s,\qquad
\beta=\operatorname{id}_N\otimes\gamma_t,
\tag{19}
\]
with convergence on the entire normal predual. Their commutator is \(\operatorname{id}_N\otimes\gamma_c\). If this were \(\operatorname{Ad}(v)\), it fixes \(N\otimes1\), so its implementer commutes with that whole algebra. CT2 gives
\[
(N\otimes1)'\cap(N\bar\otimes R)
=Z(N)\bar\otimes R=1\otimes R.
\tag{20}
\]
Hence \(v=1\otimes v_0\) would implement \(\gamma_c\), contrary to its outerness. These two approximately inner automorphisms have noncommuting abstract outer classes. A normal absorption isomorphism transports those classes back to \(M\), proving (18).

The four characterizations are now explicit: absorption, noncommutative central sequence algebra, failure of \(\overline{\operatorname{Int}(M)}\subseteq\operatorname{Cnt}(M)\), and the nonabelian quotient (18). The first and central-sequence versions, for some/every free \(\omega\), are the preceding absorption theorem. A nonabelian quotient forces the stated inclusion to fail by Theorem 1.2. Conversely failure of that inclusion forces a noncommutative central algebra by Theorem 2.2, hence absorption. This completes the entire criterion. \(\square\)

**Exercise 6.** Compute the commutator of \(s=(12)\) and \(t=(23)\) in \(S_3\).

*Solution.* They are involutions, so \(sts^{-1}t^{-1}=stst=(st)^2\). Rightmost-first composition sends \(1\mapsto2\mapsto3\mapsto1\) under \(st\), so \(st=(123)\) and its square is \((132)\ne e\). CT3's action is outer at this nonidentity element, which is what makes the two outer classes noncommuting.

**Exercise 7.** If \(N\) is a factor and \(\operatorname{id}_N\otimes\gamma\) is inner, why is \(\gamma\) inner?

*Solution.* An implementing unitary \(v\) must commute with every \(a\otimes1\), because all those elements are fixed. The complete coefficient-compression proof of CT2 places \(v\) in \(1\otimes R\): each second-leg matrix coefficient belongs to \(N\) and commutes with \(N\), hence is scalar since \(Z(N)=\mathbb C\). The scalar coefficients reconstruct \(v=1\otimes v_0\); its unitarity makes \(v_0\) unitary. Applying the implemented automorphism to \(1\otimes b\) gives \(\gamma(b)=v_0bv_0^*\) for every \(b\in R\).

<a id="6-exercises-with-complete-solutions"></a>
<a id="reading-and-prerequisites"></a>

## Complete free proofs and the comparison sources

The full prerequisite route is [CT0–5](../components/centrally-trivial-and-bernoulli-inputs.md) with the exact completed normal-predual, matrix comparison, faithful trace, dyadic product, AFD uniqueness, central sequence, hypercentrality and absorption inputs. It includes all twelve whole problems and solutions. The finite fixed factors are proved irreducible directly using remote orthogonal markers, with their type, predual separability and AFD stages checked separately.

Alain Connes, [*Outer conjugacy classes of automorphisms of factors*](https://www.numdam.org/articles/10.24033/asens.1295/), Theorem 2.2.1 and Lemma 2.2.2, printed pp.400–402 (PDF pp.19–21), is the free comparison for the finite-test and two-state methods. The two faithful-state squares, state-change errors and complete unitary convergence above are explicit. The source's absorption reference is supplied by the completed preceding lesson, and its brief assertion about noncommuting approximately inner automorphisms is supplied by the entire finite \(S_3\) construction.

Alain Connes, [*Periodic automorphisms of the hyperfinite factor of type II₁*](https://alainconnes.org/wp-content/uploads/szego.pdf), Lemma 3.4 and Theorem 3.2(1), printed pp.49–51 (PDF pp.11–13), compares the twisted-orbit displacement method. CT5 proves the compact minimizer directly, and CT1/SS0 supplies the finite implementation, coefficient extraction and unitary orientation. Theorem 4.2 retains its original nonidentity conclusion on every quotient.

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), Example 5.2.4, printed pp.69–70 (PDF pp.75–76), is the Bernoulli comparison. Its escape-from-finite-support argument uses an infinite group. Here the inverse-index convention and infinite-group mixing are explicit, while the finite \(S_3\) action has its own complete dyadic-tail outerness proof.
