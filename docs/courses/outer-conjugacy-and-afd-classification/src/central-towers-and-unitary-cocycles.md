# Central towers and unitary cocycles

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Spot-checked by GPT-6 Astra (OpenAI) in a separate session. New original text is public domain (CC0).*

## Introduction

A tower turns an equation involving an automorphism into a recursion along finitely many corners. The recursion is exact except at one seam. Making the tower longer makes that seam small. In an asymptotic centralizer, a diagonal argument then removes it entirely.

This lesson proves the relative tower and first cohomology theorems behind outer-conjugacy arguments. The relevant hypothesis is that no nonzero power acts trivially on central sequences. Ordinary outerness of all powers does not suffice.

The main mathematical source is [Connes], Proposition 2.1.2, Lemma 2.1.4 and Theorem 2.1.3. [Takesaki], XVII.2.2–2.4, gives a later treatment. The prerequisites are [Cyclic towers in finite algebras](cyclic-towers-in-finite-algebras.md), Theorem 1.1, and Central sequence algebras and exact lifts, Theorems 3.1, 5.1 and 6.1. These provide the finite normal trace and exact lifts for a separable-predual factor of any type. The quotient need not be a factor and need not have separable predual. The finite tower theorem is used with precisely that generality.

The proof has two distinct selection steps. To construct a tower commuting with a prescribed algebra, we may choose a new coordinate in each row of approximate towers. To solve the equation for a prescribed cocycle, we keep its coordinate fixed and choose only the approximation row. Sections 3 and 5 explain this difference. Section 6 uses additional standard-form and type III modular facts, stated there; they are not inputs to the tower or cohomology theorem. [Ando–Haagerup] supplies a modern comparison of the ultraproduct constructions; [Connes–Størmer] is further background on type III₁ states.

The faithful-state existence, globally normal GNS representation, bounded strong-star criterion and uniform finite-test estimates used in the selections are proved in [Bounded topology and tracial representations, Section 3A](bounded-topology-and-tracial-representations.md#3a-faithful-state-tests-and-ordinary-extraction). Its [proof companion](../foundations/bounded-topology-foundations.md) supplies the exact earlier compactness, predual, bicommutant and Kaplansky arguments. These close that bounded-topology branch; the cyclic-tower spectral foundations and the additional modular inputs of Section 6 retain their separately stated obligations.

## 1. Conventions and the lifting statements

Let \(M\) be a factor with separable predual, \(\varphi\) a faithful normal state, and \(\omega\) a free ultrafilter on \(\mathbb N\). A bounded sequence \((x_k)\) is **strongly central along \(\omega\)** when
\[
\lim_{k\to\omega}\|x_k\psi-\psi x_k\|=0\qquad(\psi\in M_*).
\tag{1.1}
\]
The bimodule convention is \((x\psi)(a)=\psi(ax)\), \((\psi x)(a)=\psi(xa)\). Write \(\|x\|_\varphi=\varphi(x^*x)^{1/2}\) and
\[
\|x\|^\sharp_\varphi
=\bigl(\varphi(x^*x)+\varphi(xx^*)\bigr)^{1/2}.
\]
On bounded sets, the latter seminorm detects strong-star convergence. Strongly central sequences form an algebra; the strong-star-null sequences in that algebra form an ideal. Their quotient is the finite von Neumann algebra \(F=M_\omega\), with faithful normal tracial state \(\tau_\omega\).

For a factor its trace is canonical:
\[
\tau_\omega([(x_k)])=\lim_{k\to\omega}\varphi(x_k).
\tag{1.2}
\]
To see state independence, take the ultraweak limit of \(x_k\) along \(\omega\). Asymptotic commutation with every element makes this limit central, hence scalar. Every normal state therefore gives the same limit. In particular an automorphism \(\theta\) induces a trace-preserving \(\gamma=\theta_\omega\) on \(F\).

We use the following exact forms of the lifting statements:

1. Every finite projection partition \(E_0,\ldots,E_{n-1}\) of \(1\) in \(F\) has representatives \(e_{j,k}\) that are a projection partition of \(1\) in \(M\) for every \(k\).
2. Every unitary \(V\in F\) has a representative consisting of unitaries \(v_k\in M\).
3. If \(X=[(x_k)]\in F\), then
   \[
   \|X\|_{2,\omega}^2=\lim_{k\to\omega}\varphi(x_k^*x_k).
   \]
   Vanishing of this quantity is equivalent to strong-star nullity for strongly central sequences. Products and adjoints are consequently well defined in the quotient.

These statements include strong centrality of the representatives. The exact provider is [OA-APPROX]: Theorem 3.1 constructs the finite von Neumann quotient, its faithful normal trace and normal induced automorphisms; Theorem 6.1 lifts finite projection partitions; Theorem 5.1, with both prescribed endpoints equal to \(1\), lifts unitaries. Its endpoint-equivalence hypothesis then holds at every coordinate. The provider uses \(\|x\|_{\varphi,\#}=\|x\|^\sharp_\varphi/\sqrt2\); consequently a centralizing representative of \(X\) satisfies
\[
\lim_{k\to\omega}\|x_k\|^\sharp_\varphi
=\sqrt2\,\|X\|_{2,\omega}.
\]
An arbitrary C*-quotient unitary-lifting assertion would not supply these interfaces. The provider's analytic and projection-comparison prerequisites, and the finite tower theorem's spectrum and projection prerequisites, retain their stated scope.

Choose a norm-dense sequence \((\psi_l)\) in the unit ball of \(M_*\). To establish (1.1) for a new bounded sequence, it suffices to establish it for every \(\psi_l\), because
\[
\|[x,\psi]-[x,\psi_l]\|\leq2\|x\|\|\psi-\psi_l\|.
\tag{1.3}
\]
Strong centrality also implies strong-star commutation with each fixed element of \(M\), by the normal-functional commutator estimate in Central sequences and free-group factors, Section 1. This implication applies along \(\omega\) and along the ordinary limit.

## 2. Reindexing detects every invariant corner

An automorphism is **centrally trivial** when it fixes every bounded ordinary strongly central sequence modulo strong-star null sequences. Its **asymptotic period** is
\[
\begin{aligned}
p_a(\theta)=\min\{r\geq1:\;&\\
\theta^r\text{ is centrally trivial}&\},
\end{aligned}
\tag{2.1}
\]
with value \(0\) if the set is empty. This is the order of \(\theta_\omega\), with \(0\) denoting infinite order, for every free \(\omega\). Here is the separability argument.

Suppose first that \(\theta\) is centrally trivial but that a bounded strongly \(\omega\)-central sequence \((x_k)\) has
\(\|\theta(x_k)-x_k\|^\sharp_\varphi>\delta\) on some \(B\in\omega\), for a fixed \(\delta>0\). For each \(m\), choose \(k_m\in B\) so large that \(k_m>k_{m-1}\) and
\(\|[x_{k_m},\psi_s]\|<1/m\) for \(s\le m\). Each finite collection of tests holds on an \(\omega\)-large set, which intersects \(B\) and the cofinite lower bound. Equation (1.3) makes \((x_{k_m})\) ordinarily strongly central, while its displacement stays above \(\delta\), a contradiction. Hence \(\theta_\omega=\mathrm{id}\).

Conversely, if \(\theta\) is not centrally trivial, select a subsequence of an ordinary centralizing witness with displacement above some \(\delta>0\) at every term. That subsequence is strongly central along every free ultrafilter and its displacement represents a nonzero element, so \(\theta_\omega\ne\mathrm{id}\). Apply both implications to every positive power of \(\theta\) to obtain the assertion about \(p_a\).

**Lemma 2.1 (nontriviality becomes proper outerness).** If \(\theta\) is not centrally trivial, then \(\theta_\omega\) is properly outer.

*Proof.* Choose an ordinary strongly central sequence of contractions \(y_l\) for which \(\theta(y_l)-y_l\) does not tend strongly-star to zero. Passing to a subsequence, and replacing the sequence by its adjoint if necessary, the fixed faithful state gives
\[
\begin{gathered}
z_l=(\theta(y_l)-y_l)^*(\theta(y_l)-y_l),\\
\varphi(z_l)\longrightarrow c>0.
\end{gathered}
\tag{2.2}
\]
If the failure is first detected in the adjoint seminorm, replace \(y_l\) by \(y_l^*\). Products of bounded strongly central sequences are strongly central. Thus \(z_l\) converges ultraweakly to \(c1\): every ultraweak cluster point is scalar, and its state value is fixed by (2.2).

Suppose \(\gamma=\theta_\omega\) were inner on a nonzero invariant corner \(eFe\), implemented by a unitary \(u\in eFe\). Lift \(e\) to projections \(e_k\), and choose bounded representatives \(u_k\) of \(u\). For each coordinate \(k\), choose an index \(l(k)\) large enough that:

- \(y_{l(k)}\) commutes with \(\psi_1,\ldots,\psi_k\) in predual norm to within \(1/k\);
- it commutes with \(e_k,u_k,u_k^*\) in both state seminorms to within \(1/k\);
- \(|\varphi(e_kz_{l(k)}e_k)-c\varphi(e_k)|<1/k\).

The first two requirements follow from ordinary strong centrality, treating the finitely many elements at coordinate \(k\) as fixed. The last follows from ultraweak convergence of \(z_l\), tested by the normal functional \(x\mapsto\varphi(e_kxe_k)\).

Then \(Y=[(y_{l(k)})]\) lies in \(F\) and commutes with \(e,u\). Equation (2.2) and the last requirement give
\[
\|e(\gamma(Y)-Y)e\|_{2,\omega}^2=c\tau_\omega(e)>0.
\tag{2.3}
\]
Indeed, put \(D=\gamma(Y)-Y\). Commutation of \(Y\) with \(e\) and invariance of \(e\) make \(D\) commute with \(e\). Thus
\[
\begin{aligned}
\|eDe\|_{2,\omega}^2
&=\tau_\omega(eD^*De)\\
&=\lim_{k\to\omega}\varphi(e_kz_{l(k)}e_k)\\
&=c\tau_\omega(e).
\end{aligned}
\]
All products in this calculation use centralizing representatives, so their quotient products are legitimate. The trace is faithful and \(e\ne0\).

But innerness on \(eFe\) would give
\[
e\gamma(Y)e=\gamma(eYe)=u(eYe)u^*=eYe,
\]
contradicting (2.3). \(\square\)

The trace test in this proof is needed. Producing a moved element that commutes with \(e,u\) is insufficient if its movement might occur only outside \(e\).

**Corollary 2.2.** If \(p_a(\theta)=0\), then every nonzero power of \(\theta_\omega\) is properly outer.

*Proof.* Apply Lemma 2.1 to each \(\theta^r\), since \((\theta^r)_\omega=\theta_\omega^r\). Negative powers have the same proper-outerness property as their inverses. \(\square\)

## 3. Exact towers in a relative commutant

**Theorem 3.1 (relative towers).** Suppose \(p_a(\theta)=0\). For every von Neumann subalgebra \(P\subset F\) with separable predual and every \(n\geq1\), there is a projection partition \(E_0,\ldots,E_{n-1}\) of \(1\) in \(P'\cap F\) such that
\[
\gamma(E_j)=E_{j+1}\qquad(0\leq j<n).
\tag{3.1}
\]
Tower subscripts are read modulo \(n\). There is no requirement that \(P\) be invariant under \(\gamma\).

*Proof.* By Corollary 2.2 and the cyclic tower theorem, for each positive integer \(r\) there is a partition \(F^{(r)}_j\) in \(F\) with
\[
\|\gamma(F^{(r)}_j)-F^{(r)}_{j+1}\|_{2,\omega}<1/r.
\]
Lift each of these partitions to exact partitions \(f^{(r)}_{j,l}\) in \(M\).

Take a countable strong-star dense subset \((X_s)\) of the unit ball of \(P\), and choose bounded representatives \(x_{s,k}\). At coordinate \(k\), use the row \(r=k\). Choose a coordinate \(l(k)\) of that row where all of the following hold:
\[
\|[f^{(k)}_{j,l(k)},\psi_s]\|<1/k\quad(s\leq k),
\tag{3.2}
\]
\[
\|[f^{(k)}_{j,l(k)},x_{s,k}]\|^\sharp_\varphi<1/k\quad(s\leq k),
\tag{3.3}
\]
\[
\|\theta(f^{(k)}_{j,l(k)})-f^{(k)}_{j+1,l(k)}\|_\varphi<2/k.
\tag{3.4}
\]
For each of the finitely many levels \(j\), each requirement holds on a set in \(\omega\). In (3.3), the finitely many \(x_{s,k}\) are fixed while \(l\) is chosen; centrality of the entire row supplies these tests. For (3.4), the ultralimit of its left side is below \(1/k\), so the larger bound \(2/k\) holds on an \(\omega\)-large set. The finite intersection is nonempty. Moreover the difference in (3.4) is self-adjoint, so its \(\varphi\)-seminorm controls both strong-star seminorms.

Set \(e_{j,k}=f^{(k)}_{j,l(k)}\). These are exact projection partitions at every coordinate. Equations (3.2)–(3.4) show that their classes are strongly central, commute with each \(X_s\), and are rotated exactly. Bounded multiplication is strong-star continuous, so commuting with the dense set means commuting with all of \(P\). This proves (3.1). \(\square\)

Trace preservation now gives \(\tau_\omega(E_j)=1/n\) for every \(j\). Thus exact cyclic covariance has repaired both the seam and the small trace discrepancies of the finite-algebra theorem.

## 4. One seam solves approximate cohomology

**Lemma 4.1 (the cyclic recursion).** Let \(F\) be a finite von Neumann algebra with faithful normal tracial state \(\tau\), let \(\gamma\) be a trace-preserving automorphism, and let \(u\in\mathcal U(F)\). Suppose an exactly rotated partition \((E_j)_{j=0}^{n-1}\) commutes with \(u\). Then there is \(V\in\mathcal U(F)\) such that
\[
\|\gamma(V)-uV\|_2\leq2/\sqrt n.
\tag{4.1}
\]

*Proof.* Put \(v_0=E_0\) and recursively
\[
v_{j+1}=\gamma^{-1}(u v_j)\qquad(0\leq j<n-1).
\tag{4.2}
\]
Each \(v_j\) is a unitary in its corner \(E_{-j}FE_{-j}\), with identity \(E_{-j}\). Indeed, \(u\) commutes with every \(E_l\), and applying \(\gamma^{-1}\) moves the initial and final projections to the preceding level. Thus \(V=\sum_{j=0}^{n-1}v_j\) is a unitary.

For \(j<n-1\), \(\gamma(v_{j+1})=uv_j\). All these terms cancel in \(\gamma(V)-uV\), leaving
\[
\gamma(V)-uV=\gamma(v_0)-uv_{n-1}.
\]
Both remaining terms are supported in \(E_1\), which has trace \(1/n\). Each has \(L^2\) norm \(1/\sqrt n\), proving (4.1). \(\square\)

## 5. Removing the seam without changing the given cocycle

**Theorem 5.1 (Connes's first cohomology theorem).** Let \(M\) be a factor with separable predual and let \(p_a(\theta)=0\). For every \(u\in\mathcal U(M_\omega)\), there is \(v\in\mathcal U(M_\omega)\) with
\[
\theta_\omega(v)=uv.
\tag{5.1}
\]

*Proof.* Apply Theorem 3.1 with \(P=W^*(u)\). This algebra has separable predual: its faithful normal state \(\tau_\omega|_{W^*(u)}\) gives a finite spectral measure on the circle, and the spectral theorem identifies \(W^*(u)\) with the corresponding \(L^\infty\) algebra. Lemma 4.1 gives unitaries \(V^{(r)}\in F\) whose errors are below \(1/(2r)\), by choosing a sufficiently long tower.

Lift the given \(u\) once to a unitary sequence \((u_k)\), and each \(V^{(r)}\) to a unitary sequence \((V^{(r)}_k)\). For every \(r\), a set \(A_r\in\omega\) can be chosen so that, for \(k\in A_r\),
\[
\begin{gathered}
\|[V^{(r)}_k,\psi_s]\|<1/r\quad(s\leq r),\\
\|\theta(V^{(r)}_k)-u_kV^{(r)}_k\|_\varphi<1/r.
\end{gathered}
\tag{5.2}
\]
Replace these sets by decreasing finite intersections, also imposing \(k\geq r\). For each \(k\in A_1\), let \(d(k)\) be the largest \(r\leq k\) with \(k\in A_r\), and put
\[
v_k=V^{(d(k))}_k.
\]
For \(k\notin A_1\), put \(v_k=1\) and \(d(k)=0\). For every fixed \(r\), one has \(d(k)\ge r\) on \(A_r\), so \(d(k)\to\infty\) along \(\omega\). The first part of (5.2), followed by (1.3), makes \((v_k)\) strongly central. The residual \(\theta(v_k)-u_kv_k\) is therefore also centralizing, and the second part of (5.2) makes its trace square norm zero. Section 1's trace-null criterion gives strong-star nullity, including the adjoint seminorm. Thus \(v=[(v_k)]\) is a unitary satisfying (5.1).

The prescribed sequence \(u_k\) has retained its original coordinate throughout. Reindexing it at this last step could change the element \(u\), and would not prove the stated equation. \(\square\)

**Corollary 5.2 (inner conjugacy of a cocycle perturbation).** Under the hypotheses of Theorem 5.1,
\[
\operatorname{Ad}(u^*)\circ\gamma
=\operatorname{Ad}v\circ\gamma\circ\operatorname{Ad}(v^*).
\tag{5.3}
\]

*Proof.* Equation (5.1) gives \(\gamma(v^*)=v^*u^*\). Hence \(v\gamma(v^*)=u^*\); computing the composite on an arbitrary \(x\in F\) proves (5.3). \(\square\)

To express this in the usual left-cocycle convention, a unitary cocycle for \(\gamma\) is a family \((w_r)_{r\in\mathbb Z}\) satisfying
\[
w_{r+s}=w_r\gamma^r(w_s),\qquad w_0=1.
\]
Its generator \(w_1=a\) determines the positive values by this recursion and the negative values by \(w_{-r}=\gamma^{-r}(w_r^*)\); there is no finite-order relation to impose. Apply Theorem 5.1 with \(u=a^*\). Equation (5.3) gives \(a=v\gamma(v^*)\), and the cocycle identity yields
\[
w_r=v\gamma^r(v^*)\qquad(r\in\mathbb Z).
\]
Thus every left cocycle is a coboundary. For the original equation \(\gamma(v)=uv\), the associated left-cocycle generator is \(u^*\). This adjoint accounts for the order of factors in Exercise 7.5.

## 6. Why ordinary aperiodicity is insufficient

We first supply the modular fact used in the counterexample. Only this section uses the standard form of a faithful normal state: its cone vector \(\xi\), modular conjugation \(J\), modular operator \(\Delta\), and the natural-cone estimate
\[
\|\xi_\rho-\xi_\eta\|^2\le\|\rho-\eta\|
\qquad(\rho,\eta\in M_*^+).
\]
These are named modular prerequisites, including the estimate for general normal positive functionals, not only for matrices or tracial states. The precise source is [Takesaki II], Theorem IX.1.2, inequality (9), whose norm-estimate proof ends on.

**Modular fixed-point lemma.** For every faithful normal state \(\varphi\) on our factor and every real \(t\), the induced automorphism \((\sigma_t^\varphi)_\omega\) is the identity.

*Proof.* Let \(a\in M\) be unitary. The vector \(aJaJ\xi\) belongs to the natural cone and represents \(\varphi\circ\operatorname{Ad}(a^*)\). The cone estimate, followed by multiplication by the commuting unitary \(Ja^*J\), gives
\[
\begin{aligned}
\|a\xi-Ja^*J\xi\|^2
&=\|aJaJ\xi-\xi\|^2\\
&\le\|\varphi\circ\operatorname{Ad}(a^*)-\varphi\|\\
&=\|[a,\varphi]\|.
\end{aligned}
\]
The Tomita identity on \(M\xi\) says \(\Delta^{1/2}a\xi=Ja^*\xi=Ja^*J\xi\). For \(h>0\),
\[
|h^{2it}-1|\le4(1+|t|)|h-1|.
\]
Indeed, if \(h<1/2\), bound the left side by \(2\) and use \(|h-1|>1/2\). If \(h\ge1/2\), use \(|\log h|\le2|h-1|\) and \(|e^{is}-1|\le|s|\). Spectral calculus at \(h=\Delta^{1/2}\), on the vector \(a\xi\) in its domain, now proves
\[
\begin{aligned}
\|\sigma_t^\varphi(a)-a\|_\varphi
&=\|(\Delta^{it}-1)a\xi\|\\
&\le4(1+|t|)\|[a,\varphi]\|^{1/2}.
\end{aligned}
\]
The same estimate applies to \(a^*\), since its predual commutator has the same norm. Every unitary \(A\in M_\omega\) has an exact centralizing unitary lift \((a_k)\) by Section 1. Both displacement seminorms therefore tend to zero along \(\omega\), proving \((\sigma_t^\varphi)_\omega(A)=A\). Finally every element of a unital C*-algebra is a linear combination of unitaries: for a self-adjoint contraction \(b\), the unitary \(b+i(1-b^2)^{1/2}\) has real part \(b\), and real and imaginary parts treat a general element. Hence the induced automorphism fixes all of \(M_\omega\). \(\square\)

**Example 6.1 (a modular automorphism).** Let \(M=R_\infty\bar\otimes R\), where \(R_\infty\) is the Araki–Woods type III₁ factor and \(R\) is the hyperfinite II₁ factor. This is a strongly stable type III₁ factor: \(R\bar\otimes R\cong R\) by rearranging its matrix tensor factors, giving \(M\bar\otimes R\cong M\). For the type assertion, choose a product state \(\varphi_\infty\otimes\tau_R\). Its modular action is \(\sigma^{\varphi_\infty}\otimes\mathrm{id}_R\), so its continuous core is the tensor product of the factor core of \(R_\infty\) with \(R\), again a factor. The continuous-core characterization of type III₁ gives the claim. Let \(\varphi\) be a faithful normal state. Choose \(t\ne0\) and put \(\theta=\sigma_t^\varphi\).

Here the type III₁ modular input is \(T(M)=\{0\}\), where
\[
T(M)=\{s\in\mathbb R:\sigma_s^\varphi\text{ is inner}\}.
\]
One can see this from the continuous-core characterization of type III₁. Its core \(C=M\rtimes_{\sigma^\varphi}\mathbb R\) is a factor. If \(\sigma_s^\varphi=\operatorname{Ad}(a)\), state preservation makes \(a\) belong to the centralizer of \(\varphi\): the identity \(\varphi(axa^*)=\varphi(x)\), applied to \(xa\), gives \(\varphi(ax)=\varphi(xa)\). Thus \(a^*\lambda(s)\) commutes both with \(M\) and with all the implementing unitaries \(\lambda(r)\), and is central in \(C\). It must be scalar. But the dual action fixes \(a\) and multiplies \(\lambda(s)\) by \(e^{-iqs}\) at time \(q\). A nonzero scalar is fixed, forcing \(s=0\). The core characterization, the modular description of the state centralizer, and the existence of the Araki–Woods factor are the type III prerequisites of this example.

Consequently every \(\theta^r=\sigma_{rt}^\varphi\), \(r\ne0\), is outer, so \(\theta\) is ordinarily aperiodic. The modular fixed-point lemma nevertheless gives \(\gamma=\mathrm{id}\), and Section 2 then gives \(p_a(\theta)=1\).

Take \(u=-1\). Equation (5.1) would become \(v=-v\), which is impossible for a unitary. Ordinary aperiodicity has not supplied the hypothesis of Theorem 5.1.

*Source comparison.* [Takesaki], Theorem XVII.2.4 uses the word “aperiodic”; its proof invokes Lemma XVII.2.3, whose explicit hypothesis is \(p_a(\theta)=0\). [Connes], Theorem 2.1.3 states \(p_a(\theta)=0\) explicitly. The example shows why the theorem here uses that precise condition: interpreting “aperiodic” as ordinary outerness of all nonzero powers would give a false assertion, even for a strongly stable factor.

**Example 6.2 (approximation in an ordinary algebra need not give equality).** Let \(\gamma\) be an irrational rotation on \(L^\infty(\mathbb T)\), with normalized Haar trace and \(\gamma(z)=e^{2\pi it}z\) for the circle coordinate \(z\). Every nonzero power is properly outer: on a nonzero invariant corner \(eL^\infty(\mathbb T)\), the unitary \(ez\) is multiplied by \(e^{2\pi irt}\ne1\), while an inner automorphism of this abelian corner would be the identity. Cyclic towers therefore give approximate solutions of \(\gamma(v)=-v\) with unitary \(v\). There is no exact measurable unitary solution. The Fourier coefficients of such a solution would vanish except at integers \(k\) with \(e^{2\pi ikt}=-1\); irrationality makes this set empty. Since Fourier characters have dense span in \(L^2(\mathbb T)\), the putative solution would be zero. The exact conclusion of Theorem 5.1 uses the diagonal structure of the asymptotic centralizer.

## 7. Exercises with solutions

**Exercise 7.1 (introductory: seam size).** Choose a tower length guaranteeing error at most \(1/20\) in Lemma 4.1.

*Solution.* We need \(2/\sqrt n\leq1/20\), so any \(n\geq1600\) works. The estimate is uniform in the given unitary \(u\).

**Exercise 7.2 (intermediate: the conjugacy orientation).** Starting from \(\gamma(v)=uv\), compute the unitary multiplying \(\gamma\) in \(\operatorname{Ad}v\circ\gamma\circ\operatorname{Ad}(v^*)\).

*Solution.* The multiplier is \(v\gamma(v^*)=v v^*u^*=u^*\). Thus the composite is \(\operatorname{Ad}(u^*)\circ\gamma\). Replacing it by \(\operatorname{Ad}u\circ\gamma\) would reverse the equation being solved.

**Exercise 7.3 (intermediate: a relative tower commutes with translates).** If \(E_j\) commutes with \(u\) and \(\gamma(E_j)=E_{j+1}\), show that every \(E_j\) commutes with \(\gamma^k(u)\), for every integer \(k\).

*Solution.* Apply \(\gamma^k\) to \([E_{j-k},u]=0\). The result is \([E_j,\gamma^k(u)]=0\). This includes negative \(k\), since \(\gamma\) is invertible.

**Exercise 7.4 (advanced: a corner cannot hide the movement).** In Lemma 2.1, explain the role of \(\varphi(e_kz_{l(k)}e_k)\to c\tau_\omega(e)\). Why is \(\|\gamma(Y)-Y\|_2>0\) alone insufficient?

*Solution.* Innerness is being tested on \(eFe\). A nonzero difference could be supported in \((1-e)F(1-e)\), where it says nothing about that corner. The additional trace test makes its squared norm in \(eFe\) equal to \(c\tau_\omega(e)>0\). Commutation with the implementing unitary then contradicts innerness in precisely the corner being tested.

**Exercise 7.5 (advanced: a finite-cycle cocycle condition).** Let \(\gamma^n=\mathrm{id}\). Show that a solution of \(\gamma(v)=uv\) forces
\[
\gamma^{n-1}(u)\cdots\gamma(u)u=1.
\]

*Solution.* Iterating the equation gives \(\gamma^r(v)=\gamma^{r-1}(u)\cdots\gamma(u)uv\). At \(r=n\), its left side is \(v\). Right multiplication by \(v^*\) proves the condition. For a \(\mathbb Z\)-action there is no finite-order relation, so every generator unitary defines a cocycle. With the left-cocycle convention after Corollary 5.2, the generator associated with this equation is \(u^*\). Its cyclic-group condition is \(u^*\gamma(u^*)\cdots\gamma^{n-1}(u^*)=1\), whose adjoint is exactly the displayed condition.

## References

[Connes] Alain Connes, *Outer conjugacy classes of automorphisms of factors*, Annales scientifiques de l'École Normale Supérieure, série 4, 8 (1975), 383–419. [Article and original text](https://numdam.org/articles/10.24033/asens.1295/).

[Connes–Størmer] Alain Connes and Erling Størmer, *Homogeneity of the state space of factors of type III₁*, Journal of Functional Analysis 28 (1978), 187–196. [DOI](https://doi.org/10.1016/0022-1236(78)90085-X).

[Ando–Haagerup] Hiroshi Ando and Uffe Haagerup, *Ultraproducts of von Neumann algebras*, Journal of Functional Analysis 266 (2014), 6842–6913. [Open author version](https://arxiv.org/abs/1212.5457).

[Takesaki] Masamichi Takesaki, *Theory of Operator Algebras III*, Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).

[OA-APPROX] *Central sequence algebras and exact lifts*, Theorems 3.1, 5.1 and 6.1 (exact source version). The finite quotient, normal trace, induced actions and exact lifting interfaces are used in Sections 1–5. The hypotheses include all separable-predual factors, without a tracial or strong-stability restriction.

[Takesaki II] Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. Theorem IX.1.2, inequality (9) and its proof on printed page 151, supplies the natural-cone norm estimate. Theorem XII.1.1, Definition XII.1.5(iii) and Theorem XII.1.6(iv) supply the continuous-core and modular-period framework used only in Example 6.1. [Publisher record](https://doi.org/10.1007/978-3-662-10451-4).

The principal source passages for the main proof are [Connes], Proposition 2.1.2, Lemma 2.1.4 and Theorem 2.1.3. The relative tower, corner detection, cyclic recursion and final diagonal are written out above. [Takesaki], XVII.2.2–2.4 is compared at the exact asymptotic-period hypothesis. The modular example has the separate standard-form and continuous-core prerequisites stated in Section 6; neither that example nor those prerequisites is used to prove Theorems 3.1 and 5.1.
