# Centrally trivial automorphisms and decreasing AFD factors

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

The [absorption theorem](strong-stability-and-tensor-absorption.md) characterized strong stability by noncommuting central sequences. We complete its group-theoretic characterization, then show that the hyperfinite factor has no outer automorphism acting trivially on central sequences. Finally, a locally finite group action constructs decreasing irreducible hyperfinite subfactors with scalar intersection.

For Sections 1–3, \(M\) is a factor with separable predual. Its automorphism group carries the \(u\)-topology from the [fullness lesson](central-sequences-and-free-group-factors.md). Closure of \(\operatorname{Int}(M)\) always means closure in that topology. We use that lesson's complete strong* unitary metric and continuous group operations, the preceding hypercentrality/absorption proofs, the [finite outer-action theorem](finite-outer-actions.md), and the explicitly constructed finite matrix averages. Outer quotients below are used as abstract groups; no closedness of \(\operatorname{Int}(M)\) is assumed.

## 1. Central triviality and two fixed states

An automorphism \(\theta\) is **centrally trivial** if
\[
\theta(x_n)-x_n\longrightarrow0\quad\text{strong*}
\tag{1}
\]
for every bounded ordinary centralizing sequence \(x_n\). Denote these automorphisms by \(\operatorname{Cnt}(M)\).

This is a normal subgroup of \(\operatorname{Aut}(M)\). For composition, apply one fixed automorphism to the other's vanishing difference and then add its own difference. For inverses, apply (1) to the centralizing sequence \(\theta^{-1}(x_n)\). For normality, apply (1) to \(\gamma^{-1}(x_n)\), then apply \(\gamma\). Automorphisms preserve centralizing sequences by their normal predual commutator identity. Every inner automorphism is centrally trivial by centrality with its fixed implementing unitary.

If \(u_n\) are unitaries, then
\[
\operatorname{Ad}(u_n)\to\operatorname{id}\text{ in the }u\text{-topology}
\quad\Longleftrightarrow\quad
\|[u_n,\psi]\|\to0\quad(\psi\in M_*).
\tag{2}
\]
Indeed, multiplying the functional commutator by \(u_n^*\) identifies its norm with
\(\|\psi\circ\operatorname{Ad}(u_n)-\psi\|\), using the isometry of precomposition by an automorphism.

**Lemma 1.1.** If \(\theta\in\operatorname{Cnt}(M)\), finitely many normal states \(\sigma_j\), and \(\varepsilon>0\) are given, there is a neighborhood \(V\) of the identity such that
\[
\operatorname{Ad}(u)\in V
\quad\Longrightarrow\quad
\|\theta(u)-u\|_{\sigma_j}<\varepsilon
\quad\text{for all }j,
\tag{3}
\]
where \(\|a\|_\sigma=\sigma(a^*a)^{1/2}\).

**Proof.** Otherwise, in successively smaller members of a countable neighborhood basis choose implementing unitaries violating at least one bound. Their inner automorphisms tend to the identity. By (2) they form a centralizing sequence, so (1) makes every displayed seminorm tend to zero. This contradicts the violation. \(\square\)

**Theorem 1.2.** In \(\operatorname{Out}(M)\), the images of
\(\overline{\operatorname{Int}(M)}\) and \(\operatorname{Cnt}(M)\) commute.

**Proof.** Fix \(\alpha\in\overline{\operatorname{Int}(M)}\), \(\theta\in\operatorname{Cnt}(M)\), and a faithful normal state \(\varphi\). Put
\[
\sigma_1=\varphi\circ\alpha^{-1},\qquad
\sigma_2=\varphi\circ\theta\circ\alpha^{-1}\circ\theta^{-1}.
\tag{4}
\]
For \(\varepsilon_n=2^{-n}\), use Lemma 1.1 to obtain neighborhoods \(V_n\) controlling both states in (4). Choose nested neighborhoods \(W_n\) of \(\alpha\) such that
\[
W_nW_n^{-1}\subset V_n
\tag{5}
\]
and, for every \(\beta\in W_n\),
\[
\begin{aligned}
\|\varphi\circ\beta^{-1}-\sigma_1\|&<4^{-n},\\
\|\varphi\circ\theta\circ\beta^{-1}\circ\theta^{-1}-\sigma_2\|&<4^{-n}.
\end{aligned}
\tag{6}
\]
Also make \(W_n\) shrink to \(\alpha\) in a countable neighborhood basis. Group continuity and the definition of the \(u\)-topology permit these choices.

Choose \(\alpha_n=\operatorname{Ad}(u_n)\in W_n\). Put
\[
v_n=u_{n+1}u_n^*,\qquad w_n=u_n^*\theta(u_n).
\tag{7}
\]
Then \(\operatorname{Ad}(v_n)=\alpha_{n+1}\alpha_n^{-1}\in V_n\), so
\(\|\theta(v_n)-v_n\|_{\sigma_i}<2^{-n}\).
The successive difference has the exact form
\[
w_{n+1}-w_n
=u_n^*(v_n^*\theta(v_n)-1)\theta(u_n).
\tag{8}
\]
Left multiplication by a unitary preserves the one-sided \(\varphi\)-seminorm. Right multiplication changes its state. Accordingly the square norm in (8) is tested by
\(\varphi\circ\operatorname{Ad}(\theta(u_n)^*)\), which differs from \(\sigma_2\) by less than \(4^{-n}\), by (6). Since
\[
v_n^*\theta(v_n)-1=v_n^*(\theta(v_n)-v_n)
\tag{9}
\]
has norm at most \(2\), (3), (6) and (9) give
\[
\|w_{n+1}-w_n\|_\varphi^2
\le4^{-n}+4\cdot4^{-n}=5\cdot4^{-n}.
\tag{10}
\]
For adjoints, use
\[
w_{n+1}^*-w_n^*
=\theta(u_n)^*(\theta(v_n)^*v_n-1)u_n.
\tag{11}
\]
Its right multiplication changes the state to
\(\varphi\circ\operatorname{Ad}(u_n^*)\), controlled by \(\sigma_1\). The same bound holds. Thus
\[
\|w_{n+1}-w_n\|_\varphi+
\|w_{n+1}^*-w_n^*\|_\varphi
\le2\sqrt5\,2^{-n}.
\tag{12}
\]
The complete unitary metric proved earlier gives a strong* limit \(w\in\mathcal U(M)\).

Strong* convergence of unitaries gives \(u\)-convergence of their inner automorphisms: normal vector functionals are norm approximated by finite sums, and the transformed vectors converge in norm. Therefore
\[
\operatorname{Ad}(w)
=\lim_n\operatorname{Ad}(w_n)
=\lim_n\alpha_n^{-1}\theta\alpha_n\theta^{-1}
=\alpha^{-1}\theta\alpha\theta^{-1}.
\tag{13}
\]
The commutator is inner, proving the assertion about outer classes. \(\square\)

## 2. Commutative central algebras force central triviality

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

**Proof.** If no finite tests worked, use the first \(n\) states of a norm-dense sequence, together with \(\varphi\), and tolerance \(1/n\) to choose contractions \(x_n,y_n\) violating the last bound. Both sequences are centralizing by density and uniform boundedness. Their commutator fails to vanish strong*, contradicting universal hypercentrality. \(\square\)

**Theorem 2.2.** If \(M_\omega\) is commutative for one free ultrafilter, then
\[
\overline{\operatorname{Int}(M)}\subset\operatorname{Cnt}(M),
\qquad
\overline{\operatorname{Int}(M)}/\operatorname{Int}(M)
\text{ is abelian}.
\tag{15}
\]

**Proof.** The hypercentrality equivalences give the hypothesis of Lemma 2.1. Fix \(\varepsilon>0\), take \(\eta=\varepsilon/\sqrt2\), and decrease its tolerance so that \(\delta\le\varepsilon^2/4\).
Let \(V\) be the identity neighborhood defined by
\(\|\psi_j\circ\beta-\psi_j\|<\delta\) for all tests. If \(\beta=\operatorname{Ad}(u)\in V\) and a contraction \(x\) satisfies the tests, (14) gives \(\|[u,x]\|_{\varphi,\#}<\eta\). For \(z=[u,x]\), with \(\|z\|\le2\),
\[
\begin{aligned}
\|\beta(x)-x\|_{\varphi,\#}^2
&=\tfrac12\varphi(uz^*zu^*)+\tfrac12\varphi(zz^*)\\
&\le\|z\|_{\varphi,\#}^2+
\tfrac12\|\varphi\circ\beta-\varphi\|\|z\|^2\\
&\le\eta^2+2\delta\le\varepsilon^2.
\end{aligned}
\tag{16}
\]
The state test for \(\varphi\) is essential in this right-multiplication estimate.

The same bound, with weak inequalities, holds for \(\beta\in\overline{\operatorname{Int}(M)}\cap V\). Approximate such a \(\beta\) by inner automorphisms eventually in the open set \(V\), and pass to the limit for the fixed \(x\). To justify this, \(u\)-convergence of automorphisms implies pointwise strong* convergence: for fixed \(x\), expand
\(\varphi((\beta_n(x)-\beta(x))^*(\beta_n(x)-\beta(x)))\).
The square term is \(\varphi(\beta_n(x^*x))\), and the cross terms test \(\beta_n(x)\) by fixed normal functionals. All converge to the corresponding \(\beta\)-terms. The adjoint expansion is identical.

Now fix \(\theta\in\overline{\operatorname{Int}(M)}\), and choose an inner automorphism \(\operatorname{Ad}(w)\) such that
\(\beta=\theta\operatorname{Ad}(w)^{-1}\in V\).
For a contraction centralizing sequence \(x_n\), its finite tests eventually hold, and
\[
\theta(x_n)-x_n
=\beta(wx_nw^*-x_n)+(\beta(x_n)-x_n).
\tag{17}
\]
The first term tends strong* to zero, by centrality with the fixed \(w\). The second has symmetric seminorm at most \(\varepsilon\), by (16) and its closure version. Taking limsup and then arbitrary \(\varepsilon\) proves central triviality; bounded sequences follow by scaling.
Theorem 1.2 now makes the outer classes of any two approximately inner automorphisms commute. This is exactly the quotient conclusion in (15). \(\square\)

## 3. The complete group criterion for absorption

**Theorem 3.1.** For a factor \(M\) with separable predual, strong stability is equivalent to noncommutativity of the abstract quotient group
\[
\overline{\operatorname{Int}(M)}/\operatorname{Int}(M).
\tag{18}
\]
Together with the preceding absorption theorem, this completes all four characterizations of strong stability.

**Proof.** If \(M\) is not strongly stable, that theorem makes its central sequence algebras commutative. Theorem 2.2 then makes (18) abelian.

Conversely, write a strongly stable \(M\) as \(N\bar\otimes R\), with \(N\) a factor. The finite outer-action construction supplies an action \(\gamma\) of \(S_3\) on \(R\), outer at every nonidentity element. Take the transpositions \(s=(12)\) and \(t=(23)\); their commutator \(c=sts^{-1}t^{-1}\) is nonidentity. All automorphisms of \(R\) are approximately inner, by the finite factor lesson. Hence
\[
\alpha=\operatorname{id}_N\otimes\gamma_s,\qquad
\beta=\operatorname{id}_N\otimes\gamma_t
\tag{19}
\]
are approximately inner on \(N\bar\otimes R\). Tensoring approximating inner automorphisms preserves \(u\)-convergence, by the norm density of elementary normal tensor functionals.

Their commutator is \(\operatorname{id}_N\otimes\gamma_c\), and it is outer. If implemented by a unitary \(v\in N\bar\otimes R\), that unitary would commute with \(N\otimes1\). The spatial commutation theorem gives
\[
(N\otimes1)'\cap(N\bar\otimes R)
=Z(N)\bar\otimes R=1\otimes R.
\tag{20}
\]
Thus \(v=1\otimes v_0\) would implement \(\gamma_c\) on \(R\), contradicting its outerness. The two classes in (18) therefore do not commute. Transfer by the normal isomorphism proves the assertion for \(M\). \(\square\)

The **characteristic group** is
\[
\chi(M)=
\bigl(\operatorname{Cnt}(M)\cap
\overline{\operatorname{Int}(M)}\bigr)/
\operatorname{Int}(M).
\tag{21}
\]
Its numerator is a normal subgroup and contains \(\operatorname{Int}(M)\). Theorem 1.2 proves that this group is abelian.

## 4. A uniform displacement criterion in finite factors

In this section \(M\) can be any \(\mathrm{II}_1\) factor, without a separability hypothesis. Let \(\tau\) be its normalized trace.

**Lemma 4.1.** Let \(D\subset M\) be a unital finite type I subfactor and \(C=D'\cap M\). If \(\alpha\in\operatorname{Aut}(M)\) satisfies
\[
d=\sup_{u\in\mathcal U(C)}\|\alpha(u)-u\|_2<1,
\tag{22}
\]
then \(\alpha\) is inner.

**Proof.** Let \(K\) be the ultraweakly closed convex hull of \(u\alpha(u^*)\), \(u\in\mathcal U(C)\). These elements lie in the operator unit ball and the closed \(2\)-ball of radius \(d\) centered at \(1\). The latter is ultraweakly closed by lower semicontinuity, so \(0\notin K\).
Its map into \(L^2(M,\tau)\) is weakly continuous on this bounded set. For bounded test vectors this follows from normality of \(x\mapsto\tau(b^*x)\); arbitrary \(L^2\) test vectors follow by approximation and the uniform \(2\)-norm bound. Thus \(K\) is weakly compact and convex in \(L^2\), hence norm closed. The Hilbert-space projection theorem gives a unique least-norm point \(y\in K\), with \(y\ne0\) because \(0\notin K\). This is the same convexity mechanism as the [finite trace averaging lemma](hyperfinite-finite-factors.md#lemma-2-1).

For \(v\in\mathcal U(C)\), the map \(x\mapsto vx\alpha(v^*)\) preserves \(K\), bijectively, and is a trace \(2\)-isometry. It therefore fixes \(y\), yielding
\[
y\alpha(x)=xy,\qquad x\in C.
\tag{23}
\]
The unitary identity extends to all \(x\) by their linear span.

Choose a unitary \(w\in M\) implementing \(\alpha\) on \(D\). For completeness, if \(e_{ij}\) are matrix units and \(f_{ij}=\alpha(e_{ij})\), their equal trace diagonal projections are equivalent. Choose \(v\) from \(e_{11}\) to \(f_{11}\); then
\[
w=\sum_i f_{i1}ve_{1i}
\tag{24}
\]
is unitary and satisfies \(we_{ij}w^*=f_{ij}\).
Set \(\beta=\operatorname{Ad}(w^*)\alpha\); it fixes \(D\) pointwise and maps \(C\) onto \(C\). Put \(a=yw\ne0\). Equation (23) becomes
\[
a\beta(x)=xa,\qquad x\in C.
\tag{25}
\]
Expand \(a\) in the matrix coordinates \(M=D\bar\otimes C\). At least one coefficient \(z\in C\) is nonzero, and each coefficient obeys \(z\beta(x)=xz\). Since \(\beta(C)=C\), this implies \(zz^*\) commutes with \(C\) and \(z^*z\) commutes with \(\beta(C)\). The relative commutant \(C\) is a factor, so both are positive nonzero scalars, equal because their operator norms are equal.
Thus \(q=z/\|z\|\) is a unitary in \(C\), and
\[
\beta(x)=q^*xq,\qquad x\in C.
\tag{26}
\]
It also holds on \(D\), since \(\beta\) fixes \(D\) and \(q\) commutes with it. These two algebras generate \(M\); hence
\(\alpha=\operatorname{Ad}(wq^*)\) is inner. The adjoint in (26) follows directly from the intertwining equation. \(\square\)

**Theorem 4.2.** For the separable AFD \(\mathrm{II}_1\) factor \(R\),
\[
\operatorname{Cnt}(R)=\operatorname{Int}(R),\qquad
\chi(R)=\{1\}.
\tag{27}
\]
Every outer \(\alpha\in\operatorname{Aut}(R)\) induces a nonidentity automorphism of \(R_\omega\), for every free ultrafilter.

**Proof.** Let \(D_n\) be the increasing dyadic factors generating \(R\), and \(C_n=D_n'\cap R\).
If \(\alpha\) is outer, the contrapositive of Lemma 4.1 gives
\[
\sup_{u\in\mathcal U(C_n)}\|\alpha(u)-u\|_2\ge1.
\tag{28}
\]
Choose \(u_n\in\mathcal U(C_n)\) with displacement at least \(1/2\). For each fixed \(x\in R\), choose \(a\in D_k\) close to \(x\) in \(2\)-norm. When \(n\ge k\), \(u_n\) commutes with \(a\), so \(\|[u_n,x]\|_2\le2\|x-a\|_2\). The same estimate for adjoints proves centrality, and the [finite tracial centrality criterion](central-sequences-and-free-group-factors.md#lemma-1-1) makes this an ordinary centralizing sequence. Its displacement never tends to zero, so \(\alpha\) is not centrally trivial. Inner automorphisms are centrally trivial by Section 1, proving the first equality in (27), and the definition (21) gives the second.

For every free \(\omega\), the quotient image of \(\alpha(u_n)-u_n\) has \(2\)-norm at least \(1/2\), so the induced automorphism \(\alpha_\omega\) is nonidentity. No conclusion about continuity of the homomorphism \(\alpha\mapsto\alpha_\omega\) is needed. \(\square\)

## 5. Decreasing irreducible hyperfinite subfactors

**Theorem 5.1.** \(R\) admits a decreasing sequence of AFD \(\mathrm{II}_1\) subfactors \(R_n\) satisfying
\[
R_n'\cap R=\mathbb C,\qquad
\bigcap_{n\ge1}R_n=\mathbb C.
\tag{29}
\]

**Proof.** Take a countably infinite locally finite group \(G=\bigcup_nG_n\), where \(G_n\) are increasing finite subgroups. Finitary permutations of \(\mathbb N\), with the subgroups permuting the first \(n\) points, are one example. Form
\[
R_0=\overline{\bigotimes_{h\in G}}(R_h,\tau_h),
\tag{30}
\]
with identical copies \(R_h\) of \(R\). The countable product is a separable AFD \(\mathrm{II}_1\) factor, hence isomorphic to \(R\).
Use the left Bernoulli convention
\[
\alpha_g\left(\bigotimes_hx_h\right)
=\bigotimes_hx_{g^{-1}h}.
\tag{31}
\]
On finite-support tensors it gives \(\alpha_g\alpha_k=\alpha_{gk}\), and the trace GNS unitary extends it normally to \(R_0\).

Choose trace-zero unitaries \(a_m\) in successive dyadic tensor legs of \(R_e\), and embed them as \(\widetilde a_m\) in the single coordinate \(e\) of (30). Finite-stage density makes this an ordinary centralizing sequence in \(R_0\). For \(g\ne e\), its translate is supported on coordinate \(g\); product trace gives
\[
\|\alpha_g(\widetilde a_m)-\widetilde a_m\|_2^2=2.
\tag{32}
\]
An inner automorphism would move a centralizing sequence by a strong*-vanishing difference, contradicting (32). Thus every nonidentity \(\alpha_g\) is outer.

Let \(D_m\subset R_h\) denote the same identified dyadic factor in every coordinate. The finite matrix stages
\[
A_m=\bigotimes_{h\in G_m}D_m\otimes1_{\text{outside }G_m}
\tag{33}
\]
increase and generate \(R_0\). For \(m\ge n\), left translation by \(G_n\) permutes \(G_m\), so \(A_m\) is invariant under that finite group.
Put \(R_n=R_0^{G_n}\). The finite outer-action theorem gives \(R_n'\cap R_0=\mathbb C\) and makes \(R_n\) a \(\mathrm{II}_1\) factor. Its finite-dimensional fixed stages \(A_m^{G_n}\) generate it: for \(x\in R_n\), approximate in \(2\)-norm by bounded \(a_m\in A_m\), and average over \(G_n\). That average is a \(2\)-contraction fixing \(x\), so the averaged approximants still converge to \(x\). Thus \(R_n\) is separable AFD, and isomorphic to \(R\). Increasing groups make these fixed algebras decreasing.

Their intersection is \(R_0^G\). It is scalar. Indeed, finite-support operators \(a,b\) have disjoint translated supports whenever \(g\) lies outside a finite subset of \(G\), giving
\[
\tau(\alpha_g(a)b)=\tau(a)\tau(b).
\tag{34}
\]
If the supports are \(F,H\), the excluded set is \(HF^{-1}\). Bounded finite-stage \(2\)-approximation and trace Cauchy–Schwarz extend (34) to
\[
\lim_{g\to\infty}\tau(\alpha_g(a)b)=\tau(a)\tau(b),
\qquad a,b\in R_0,
\tag{35}
\]
where \(g\to\infty\) means eventually outside each finite subset. The approximation error is uniform in \(g\), since all \(\alpha_g\) preserve the trace and the \(2\)-norm.
For a fixed \(x\in R_0^G\) with \(\tau(x)=0\), take \(a=x,b=x^*\). The left side is the constant \(\tau(xx^*)\), while the right side is zero. Faithfulness gives \(x=0\). Thus the intersection is \(\mathbb C\), proving (29) after a normal identification of \(R_0\) with \(R\). \(\square\)

## 6. Exercises with complete solutions

**Exercise 1.** Prove normality of \(\operatorname{Cnt}(M)\) directly.

*Solution.* For a centralizing \(x_n\), the sequence \(\gamma^{-1}(x_n)\) is centralizing by the predual identity for automorphisms. If \(\theta\) is centrally trivial, its difference on this sequence tends strong* to zero. Applying the fixed normal automorphism \(\gamma\) gives
\(\gamma\theta\gamma^{-1}(x_n)-x_n\to0\) strong*. Hence the conjugate is centrally trivial.

**Exercise 2.** Derive (8) from (7).

*Solution.* From \(u_{n+1}=v_nu_n\), one has
\(w_{n+1}=u_n^*v_n^*\theta(v_n)\theta(u_n)\).
Subtract \(w_n=u_n^*\theta(u_n)\) to obtain (8). Adjointing gives (11). These two identities determine which fixed state controls each seminorm.

**Exercise 3.** Explain why the two states in (4) are both needed.

*Solution.* The right factor in (8) is \(\theta(u_n)\), changing the state to \(\varphi\circ\operatorname{Ad}(\theta(u_n)^*)\), whose limit is \(\sigma_2\). The right factor in the adjoint difference (11) is \(u_n\), changing it to \(\varphi\circ\operatorname{Ad}(u_n^*)\), whose limit is \(\sigma_1\). Control of one seminorm alone would not prove strong* Cauchy convergence to a unitary.

**Exercise 4.** Show that the bound (12) gives a Cauchy sequence for the complete unitary metric.

*Solution.* For \(m>n\), the triangle inequality bounds the metric distance by
\(\sum_{k=n}^{m-1}2\sqrt5\,2^{-k}\le4\sqrt5\,2^{-n}\).
This tends to zero uniformly in \(m\). Completeness yields a unitary limit, which then implements the automorphism commutator in (13).

**Exercise 5.** In (16), identify the error caused by right multiplication.

*Solution.* With \(z=[u,x]\), the square of the first seminorm of \(zu^*\) is \(\varphi(uz^*zu^*)\), while its adjoint seminorm has square \(\varphi(zz^*)\). The first differs from \(\varphi(z^*z)\) by at most \(\|\varphi\circ\operatorname{Ad}(u)-\varphi\|\|z\|^2\). The symmetric seminorm divides this error by two. Since \(\|z\|\le2\), its contribution is at most \(2\delta\).

**Exercise 6.** Verify that \(s=(12)\) and \(t=(23)\) have nonidentity commutator in \(S_3\).

*Solution.* Both are involutions, so their commutator is \(stst=(st)^2\). With rightmost-first composition, \(st=(123)\), whose square is \((132)\). Thus the commutator is nonidentity and the everywhere-outer action sends it to an outer automorphism.

**Exercise 7.** Why does innerness of \(\operatorname{id}_N\otimes\gamma\) imply innerness of \(\gamma\) when \(N\) is a factor?

*Solution.* An implementing unitary must commute with every \(a\otimes1\), because the automorphism fixes them. Equation (20) places it in \(1\otimes R\). Its second coordinate unitary then implements \(\gamma\). The factor hypothesis makes \(Z(N)=\mathbb C\) in that commutant calculation.

**Exercise 8.** In Lemma 4.1, explain why the least-norm intertwiner is nonzero.

*Solution.* The convex set \(K\) lies in the ultraweakly closed \(2\)-ball of radius \(d<1\) around \(1\). Zero is at distance exactly \(1\), hence is outside \(K\). Its minimum-norm point therefore cannot be zero. Strict convexity gives uniqueness, allowing invariance of \(K\) to produce the intertwining equation.

**Exercise 9.** Starting with \(z\beta(x)=xz\) and unitary \(q=z/\|z\|\), determine the implementing unitary and its adjoint.

*Solution.* Divide the equation by \(\|z\|\) to get \(q\beta(x)=xq\). Multiplication on the left by \(q^*\) gives \(\beta(x)=q^*xq\). Under \(\operatorname{Ad}(v)(x)=vxv^*\), the implementer is \(q^*\). Thus \(\alpha=\operatorname{Ad}(wq^*)\), as in the proof.

**Exercise 10.** Show that any outer automorphism of \(R\) acts nontrivially on every \(R_\omega\).

*Solution.* Choose \(u_n\) in successive finite-head commutants as in (28), with \(\|\alpha(u_n)-u_n\|_2\ge1/2\). They are ordinary centralizing, hence centralizing along every free \(\omega\). Their quotient difference has \(2\)-norm at least \(1/2\), so the induced automorphism cannot fix their quotient image.

**Exercise 11.** Verify (32) using the two distinct tensor coordinates.

*Solution.* Both translated and original unitaries have squared \(2\)-norm \(1\). Their mixed trace is the product of their single-coordinate traces, both zero. Expanding the squared norm of their difference gives \(1+1-2\operatorname{Re}(0)=2\). Specifying trace-zero unitaries is necessary; scalar units would have zero displacement.

**Exercise 12.** Determine the finite exceptional set in the disjoint-support argument and prove the scalar fixed-point conclusion.

*Solution.* Translated support \(gF\) meets \(H\) only if \(gf=h\) for some \(f\in F,h\in H\), that is, \(g=hf^{-1}\in HF^{-1}\). Outside that finite set, tensor independence gives (34). Extend by \(2\)-approximation as in (35). A trace-zero fixed operator \(x\) then satisfies \(\tau(xx^*)=0\) by taking \(a=x,b=x^*\). Trace faithfulness makes \(x=0\), so every fixed operator is scalar.

## Reading and prerequisites

Alain Connes, [*Outer conjugacy classes of automorphisms of factors*](https://numdam.org/item/ASENS_1975_4_8_3_383_0.pdf), *Annales scientifiques de l’École Normale Supérieure*, series 4, 8 (1975), 383–419. Lemma 2.2.2, printed p.402, gives the two-state telescoping method for central triviality and approximate innerness. Theorem 2.2.1 and its proof, printed pp.400–402, give the commutative-central-algebra implication and group criterion. The proofs here include the exact right-multiplication state changes, both adjoint seminorms, finite test quantifiers and the noncommuting \(S_3\) outer action omitted from the source’s brief converse. The absorption implication in that paper cites Araki’s theorem; this course retains its earlier full absorption construction as a separate dependency.

Alain Connes, [*Periodic automorphisms of the hyperfinite factor of type II₁*](https://alainconnes.org/wp-content/uploads/szego.pdf), *Acta Scientiarum Mathematicarum* 39 (1977), 39–66. Lemma 3.4 and its full proof, printed p.50 (PDF p.12), give the uniform displacement criterion in an arbitrary \(\mathrm{II}_1\) factor. Theorem 3.2(1), stated on printed p.49 and proved on pp.50–51 (PDF pp.11–13), constructs displaced central sequences for outer automorphisms of \(R\). Lemma 4.1 here includes the bounded convex-hull compactness, explicit finite matrix implementation, coefficient polar argument and implementing-unitary orientation. Theorem 4.2 uses fixed dyadic heads to prove its stated nonidentity conclusion for every free ultrafilter; the source additionally proves that the induced automorphism is outer, which is not asserted here.

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft. Example 5.2.4, printed pp.69–70, gives Bernoulli mixing and outerness, with an infinite index and the inverse-index convention checked explicitly here. Exercise 5.11, printed p.81, supplies the finite crossed-product realization route expanded in the [finite outer-action lesson](finite-outer-actions.md). Section 5 above gives the full locally finite invariant stages, finite fixed factors and scalar intersection; it does not assume a decreasing-factor existence theorem. Sections 4 and 5 retain their own exact stated hypotheses. The ordinary-sequence, asymptotic-centralizer, full absorption, unitary topology and matrix foundations remain separately declared prerequisites, with accessible transitive verification pending.
