# Bounded ultrastrong topology and the semifinite tracial representation

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the AI that wrote it, under the stated foundations. New original text is public domain (CC0). Cited source texts retain their own rights. Source and proof revision by GPT-6 Astra (OpenAI), Ultra, October 2026.*

## Introduction

The [finite free-action argument](finite-free-actions-and-coboundaries.md) tests a bounded net in a tracial Hilbert space and then returns to the original algebra. This return needs two precise facts: the intrinsic ultrastrong topology agrees with the strong operator topology in every faithful normal representation on bounded sets, and a faithful normal semifinite trace supplies such a representation with a dense set of bounded square-integrable vectors.

We prove both facts with nets. The Hilbert spaces and indexing sets can have arbitrary cardinality. The topology theorem applies to every von Neumann algebra. The tracial construction applies whenever the given algebra carries the specified trace; it does not assert that every von Neumann algebra does.

Section 3A proves the faithful-state criterion used in the almost-invariant implementer argument: on a fixed norm ball, one faithful normal state tests the full strong* topology. Its proof includes the normal GNS construction, commutant density, moving normal-functional tests and a jointly indexed ordinary subsequence.

This is an independently written reconstruction of an existing foundation, prepared after reading the exact finite free-action interface and Jesse Peterson's freely accessible notes. The reconstruction uses the compact-ball argument for topology transport and constructs the tracial representation directly. Its scholarly context includes Takesaki’s treatment of trace and representation theory; the proofs here use the accessible foundations linked below.

## 1. The foundations and their two roles

For bounded representation transport and the faithful-state results in Sections 3–3A, normal linear functionals and maps mean ultraweakly continuous ones. The analytic inputs have the following complete earlier programme proofs, supplied as [accompanying bounded-topology foundation excerpts](../foundations/bounded-topology-foundations.md). The named sections refer to the exact accompanying texts:

- **Concrete preduals, CP01–CP07**, from OA-MOD, *Concrete preduals*: Hilbert completion, the projective tensor norm and its dual, summable-vector functionals, quotient and annihilator norms, \(M=(M_*)^*\), norm closure of \(M_*\) in \(M^*\), and positive functional decomposition.
- **Bounded operators, BK01–BK04**, from OA-MOD, *The bounded operator kernel*: bounded continuous functional calculus, the bicommutant proof, bounded WOT/ultraweak comparison, global ultraweak continuity of fixed multiplication, and bounded increasing positive nets and their strong suprema. The underlying **GP0** proof in *Bounded right multipliers*, Section GP0, supplies Bernstein approximation and the interval calculus; the opening Hilbert-tools section of *Real coercive equations* supplies projection and Riesz representation.
- **Norming and separation, NP1–NP2**, from OA-MOD, *Norming, convex separation and bounded functional supports*: real and complex Hahn–Banach, dual norming, strict separation, and equality of convex closures for topologies with the same continuous real dual.
- **Compactness, AB04–AB05**, from OA-MOD, *Banach second adjoints*: ultrafilters, compact products, compact scalar disks and the complete dual-ball compactness proof.
- **Density, HA03 and HAP04–HAP05**, from OA-MOD, *Hilbert-algebra kernel* and *Hilbert-algebra approximation*: nonunital bicommutant approximation, the real strong/WOT separation step and Kaplansky approximation by contractions in the original nondegenerate *-algebra. Nondegeneracy applies to a represented algebra on its active subspace; neither norm closure nor a countable approximating family is required by those proofs.

These inputs establish the predual, Hilbert, compactness and density branch used by Theorem 3.1 and Section 3A. In particular, Lemma 3A.1 provides a summable-vector proof of bounded WOT-to-ultraweak convergence and fixed-multiplication continuity. The normal GNS argument in Lemma 3A.3 proves ultraweak continuity directly, without converting an order-normal extended-valued weight into a normal functional.

The semifinite tracial construction in Sections 4–7 also uses BK04's bounded increasing positive nets. The [tracial-normality companion](../foundations/tracial-normality-foundations.md) supplies the complete additional proof chain: CP08–CP11, BK05–BK07, NP3, WG002–WG006, CV1–CV4 and NW01–NW11 lead to the full positive-functional normality criterion in NP02 and TP1. TP2 proves arbitrary projection joins; TP3 constructs the exact half-closed spectral cuts used in Section 5; TP4 checks the complete application in Section 6. These results retain arbitrary Hilbert dimensions and increasing nets. The broader Borel and unbounded spectral theorems are separate; their full statements are not claimed proved by the threshold-cut lemma.

The original reconstruction consulted [Peterson, Sections 2.4 and 2.6.1, Lemma 2.4.3 and Proposition 2.6.7, printed pages 26–27 and 31; Section 4.2, Lemma 4.2.1 and Proposition 4.2.2, printed pages 59–60](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf), including the proofs. Section 2 retains its trace-class presentation: restriction of trace-class functionals gives the concrete predual, and finite-rank density with \(\lvert\operatorname{Tr}(TS)\rvert\le\|T\|\|S\|_1\) gives (2.3). Peterson's Section 2.1, especially Lemma 2.1.4 and the finite-rank-density paragraph was the source for that presentation. For the bounded topology and state branch, the accompanying CP/BK proofs and Lemma 3A.1 supply the same needed conclusions by summable vector coefficients.

The target topology, faithful-state and semifinite representation assertions are proved below under their stated inputs. The general topology and semifinite trace results do not assume a faithful normal state. A specified faithful normal state enters only Section 3A's state assertions, and separable predual enters its existence and countable extraction statements. Standard-form existence, center-valued trace existence and a Hilbert-algebra commutation theorem are not used to prove these representation results.

## 2. Intrinsic seminorms and bounded positive nets

For each bounded normal positive functional \(\varphi\in M_*^+\), put

\[
p_\varphi(x)=\varphi(x^*x)^{1/2}.
\tag{2.1}
\]

The topology generated by these seminorms is the **intrinsic ultrastrong topology**. Thus \(x_i\to x\) means \(p_\varphi(x_i-x)\to0\) for every \(\varphi\in M_*^+\). The ultrastrong* topology additionally tests \(p_\varphi((x_i-x)^*)\). We will not infer convergence of adjoints from ultrastrong convergence alone.

Normal positive functionals linearly span \(M_*\). Indeed, extend a normal functional to a trace-class functional on \(B(H)\) by the predual identification. Decompose the real and imaginary parts of its trace-class operator into positive and negative parts; their restrictions give four normal positive functionals.

Consequently, for any net \(y_i\in M_+\),

\[
\begin{gathered}
\varphi(y_i)\longrightarrow0\quad(\varphi\in M_*^+)
\\
\quad\Longleftrightarrow\quad
y_i\longrightarrow0\text{ ultraweakly}.
\end{gathered}
\tag{2.2}
\]

No boundedness assumption is needed in (2.2). In particular, applying it to \(y_i=(x_i-x)^*(x_i-x)\) characterizes intrinsic ultrastrong convergence.

We will use the following bounded-net observation. If \(T_i\to0\) weakly as operators on any Hilbert space \(K\) and \(\sup_i\|T_i\|\leq C\), then \(T_i\to0\) ultraweakly. To prove it, for a trace-class \(S\) choose a finite-rank \(S_0\) with \(\|S-S_0\|_1<\varepsilon\). Then

\[
\lvert\operatorname{Tr}(T_iS)\rvert
\leq\lvert\operatorname{Tr}(T_iS_0)\rvert+C\varepsilon.
\tag{2.3}
\]

The first term tends to zero because it is a finite sum of matrix coefficients. First let the net tend to its limit and then let \(\varepsilon\) tend to zero. The reverse implication follows by testing rank-one trace-class operators. This proves equality of weak operator and ultraweak convergence on bounded sets, including nonseparable Hilbert spaces.

## 3. A faithful normal representation transports bounded nets

**Theorem 3.1.** Let \(M\) be any von Neumann algebra, let \(\pi:M\to B(K)\) be a faithful normal *-representation, and let \((x_i)\) be a net in a fixed norm-bounded subset of \(M\). For \(x\in M\), the following are equivalent:

1. \(x_i\to x\) intrinsically ultrastrongly;
2. \(\pi(x_i)\to\pi(x)\) strongly on \(K\);
3. \(\pi(x_i)\to\pi(x)\) intrinsically ultrastrongly in its represented algebra.

Hence \(\pi\) identifies the intrinsic ultrastrong topologies on bounded subsets of \(M\) and \(\pi(M)\).

**Proof.** Put \(p=\pi(1)\), and first view \(Q=\pi(M)\) on \(pK\). Multiplicativity gives \(\pi(a)=p\pi(a)p\), so its operators vanish on \((1-p)K\) and restriction to \(pK\) loses none of the convergence tests. On this active subspace the representation is unital.

Positivity follows from square-root factorization. Applying it to \(a^*a\le\|a\|^2 1\), together with the C*-norm identity, proves contractivity. To prove isometry, suppose \(a\ge0\) and \(r=\|\pi(a)\|<\|a\|=s\). Choose continuous \(f:[0,s]\to[0,1]\) vanishing on \([0,r]\) and satisfying \(f(s)=1\). The bounded calculus has \(s\in\sigma(a)\), so \(\|f(a)\|=1\). Polynomial approximation and contractivity give \(\pi(f(a))=f(\pi(a))=0\), contradicting faithfulness. Equality of norms on positive elements, applied to \(a^*a\), proves isometry for every \(a\).

For \(0\le C<\infty\), the closed ball \(M_C\) is ultraweakly compact by CP06 and AB05 from Section 1. Normality makes

\[
\pi:M_C\longrightarrow\pi(M_C)
\tag{3.1}
\]

ultraweakly continuous. It is a continuous bijection from a compact space to a Hausdorff space. Its inverse is continuous: a closed subset of \(M_C\) is compact, its image is compact, and compact subsets of a Hausdorff space are closed. Thus, for nets lying in \(M_C\), ultraweak convergence is equivalent to ultraweak convergence of their images in the relative topology inherited from \(B(K)\). This proves inverse continuity on each specified ball; no unrestricted inverse continuity is inferred merely by scaling.

We also need that \(Q\) is a von Neumann algebra on \(pK\). Isometry identifies its unit ball with the compact image \(\pi(M_1)\), which is ultraweakly closed in \(B(pK)\). A strong limit of contractions is a contraction; Lemma 3A.1 makes this bounded strong limit ultraweak as well. Hence the unit ball of \(Q\) is strongly closed. The algebra \(Q\) is unital on \(pK\), so the nondegenerate Kaplansky theorem HAP05 from Section 1 gives a net of contractions from \(Q\) converging strongly to each contraction of \(Q''\). Strong closedness puts each such contraction in \(Q\), and scaling gives \(Q=Q''\).

Put \(z_i=x_i-x\); this is again norm bounded. If \(z_i\to0\) intrinsically ultrastrongly, then for every \(\xi\in K\) the normal positive functional
\(\varphi_\xi(a)=\langle\pi(a)\xi,\xi\rangle\) gives

\[
\|\pi(z_i)\xi\|^2
=\varphi_\xi(z_i^*z_i)\longrightarrow0.
\tag{3.2}
\]

This direction uses normality but not faithfulness.

Conversely, assume \(\pi(z_i)\to0\) strongly. For every \(\xi,\eta\in K\),

\[
\begin{gathered}
\big\lvert\langle\pi(z_i^*z_i)\xi,\eta\rangle\big\rvert
\\
=\big\lvert\langle\pi(z_i)\xi,\pi(z_i)\eta\rangle\big\rvert
\\
\leq\|\pi(z_i)\xi\|\,\|\pi(z_i)\eta\|\longrightarrow0.
\end{gathered}
\tag{3.3}
\]

The net \(z_i^*z_i\) lies in one fixed norm ball. Lemma 3A.1, equivalently the bounded-net conclusion (2.3), makes its represented image ultraweakly null. The inverse in (3.1), used on that fixed ball, gives \(z_i^*z_i\to0\) ultraweakly in \(M\). Evaluation by every \(\varphi\in M_*^+\) gives \(p_\varphi(z_i)\to0\).

Finally apply the same equivalence to the identity representation of the von Neumann algebra \(\pi(M)\) on its active Hilbert space. This proves the third equivalence. Equivalence for all convergent nets identifies the restricted topologies. Indeed, if a neighborhood in one contained no neighborhood in the other, choose an outside point in each of the latter neighborhoods, directed by reverse inclusion. This gives a net converging for only one topology, a contradiction. Thus the conclusion concerns the topology itself, not only sequences. \(\square\)

**Corollary 3.2.** If \(\theta:M\to N\) is any normal *-homomorphism, intrinsic ultrastrong convergence implies intrinsic ultrastrong convergence after applying \(\theta\). For \(\psi\in N_*^+\),

\[
p_\psi(\theta(z))^2
=(\psi\circ\theta)(z^*z).
\tag{3.4}
\]

Normality puts \(\psi\circ\theta\) in \(M_*^+\). This direction needs neither faithfulness nor a norm bound. In particular it applies to a normal inclusion of von Neumann algebras.

Applying Theorem 3.1 to both \(z_i\) and \(z_i^*\) also proves transport of intrinsic ultrastrong* topology on bounded sets.

## 3A. Faithful-state tests and ordinary extraction

This section supplies the bounded strong* interface for the almost-invariant implementer argument. Theorem 3.1 retains its state-free scope; a state is used only where the hypotheses below specify one.

### 3A.1. Vector tests and fixed multiplication

A von Neumann algebra is allowed to act on a nonseparable Hilbert space. Its concrete predual is denoted by \(M_*\); normal linear functionals and normal linear maps mean ultraweakly continuous ones. We use inner products linear in the first variable. For \(\psi\in M_*^+\), set

\[
\begin{gathered}
p_\psi(z)=\psi(z^*z)^{1/2},\\
q_\psi(z)=\bigl(\psi(z^*z)+\psi(zz^*)\bigr)^{1/2}.
\end{gathered}
\tag{3A.1}
\]

These generate the intrinsic ultrastrong and ultrastrong* topologies, respectively. The name “strong*” below means the strong operator topology applied to the operator and its adjoint in the specified concrete representation. The two meanings agree on bounded sets by Theorem 3.1.

**Lemma 3A.1 (vector tests and fixed multiplication).** On any concrete von Neumann algebra \(M\), a norm-bounded WOT-null net is ultraweakly null. For fixed \(a,b\in M\), the map \(M\ni T\mapsto aTb\in M\) is ultraweakly continuous on the entire algebra.

**Proof.** By CP04 and CP06 in the accompanying foundation excerpts, every \(\rho\in B(K)_*\) has the form

\[
\begin{gathered}
\rho(T)=\sum_{n=1}^{\infty}\langle T\xi_n,\eta_n\rangle,\\
\sum_n\|\xi_n\|\|\eta_n\|<\infty.
\end{gathered}
\tag{3A.2}
\]

Consequently a bounded WOT-null net \((T_i)\), with \(\|T_i\|\le C\), is ultraweakly null: choose \(N\) so the tail of the sum in (3A.2) is less than \(\varepsilon/C\) when \(C>0\), bound the tail uniformly by \(\varepsilon\), and use WOT convergence for the first \(N\) terms. The case \(C=0\) is immediate. Conversely, individual vector functionals are normal, so ultraweak convergence implies WOT convergence. The same argument holds for restrictions to a concrete von Neumann subalgebra.

Fixed multiplication is ultraweakly continuous on the entire algebra. For fixed \(a,b\in B(K)\),

\[
\begin{gathered}
\rho(aTb)=\sum_n\langle T b\xi_n,a^*\eta_n\rangle,\\
\sum_n\|b\xi_n\|\|a^*\eta_n\|\\
\le \|a\|\|b\|\sum_n\|\xi_n\|\|\eta_n\|.
\end{gathered}
\tag{3A.3}
\]

Restriction gives this assertion for \(M\). Thus \(x\mapsto\psi(axb)\) belongs to \(M_*\) whenever \(\psi\in M_*\) and \(a,b\in M\). These assertions have no bounded-net restriction; only the equivalence between WOT and ultraweak convergence above has that restriction. \(\square\)

### 3A.2. Existence of a faithful normal state

**Lemma 3A.2 (existence of a faithful normal state).** Every nonzero von Neumann algebra with separable predual has a faithful normal state. No factoriality assumption is required.

**Proof.** The positive part of the predual unit ball has a countable norm-dense subset \((\psi_n)\). To justify this elementary separability step, take a countable base of norm balls for \(M_*\), and choose a point of the positive unit ball from each base member that meets it. Such a base comes from rational radii and a countable dense set. The resulting choices are dense in that subset. Include a nonzero positive member and repeat members if necessary to obtain a sequence.

Normal positive functionals separate \(M_+\): in any concrete faithful realization, a nonzero positive \(a\) has a vector \(\xi\) with \(\langle a\xi,\xi\rangle>0\). After normalization this is a positive normal functional of norm at most one. Approximating it in norm shows \(\psi_n(a)>0\) for some \(n\). The series

\[
\omega=\sum_{n=1}^{\infty}2^{-n}\psi_n
\tag{3A.4}
\]

converges in predual norm, is positive, and is nonzero. If \(a\ge0\) and \(\omega(a)=0\), positivity forces \(\psi_n(a)=0\) for every \(n\), hence \(a=0\). Since \(\omega(1)>0\), the functional \(\varphi=\omega/\omega(1)\) is the required faithful normal state. \(\square\)

The assertions involving \(\varphi\) below assume a specified faithful normal state; they do not require a separable predual. Theorem 3.1 needs no state.

### 3A.3. The normal faithful-state GNS representation

**Lemma 3A.3 (the normal faithful-state GNS representation).** Let \(\varphi\in M_*^+\) be faithful and satisfy \(\varphi(1)=1\). There are a Hilbert space \(H_\varphi\), a unital faithful normal *-representation
\(\pi_\varphi:M\to B(H_\varphi)\), and a cyclic separating unit vector \(\Omega_\varphi\), such that

\[
\begin{gathered}
\varphi(a)=\langle\pi_\varphi(a)\Omega_\varphi,\Omega_\varphi\rangle,\\
\|\pi_\varphi(a)\Omega_\varphi\|^2=\varphi(a^*a).
\end{gathered}
\tag{3A.5}
\]

**Proof.** Give \(M\) the inner product
\(\langle a,b\rangle_\varphi=\varphi(b^*a)\). Positivity and Cauchy–Schwarz follow by applying \(\varphi\) to
\((a+\lambda b)^*(a+\lambda b)\) and minimizing in \(\lambda\); if a diagonal term vanishes, varying the magnitude and phase of \(\lambda\) forces the mixed term to vanish. Faithfulness makes this inner product definite. Complete it to \(H_\varphi\), and write \(\Lambda(a)\) for the image of \(a\).

For \(c,a\in M\), the order inequality
\(a^*c^*ca\le\|c\|^2a^*a\) gives
\(\|\Lambda(ca)\|\le\|c\|\|\Lambda(a)\|\). Therefore left multiplication extends to a bounded operator

\[
\pi_\varphi(c)\Lambda(a)=\Lambda(ca).
\tag{3A.6}
\]

On the dense subspace \(\Lambda(M)\), multiplication, linearity and the unit give the representation identities. The equality
\(\varphi(b^*ca)=\varphi((c^*b)^*a)\) proves
\(\pi_\varphi(c)^*=\pi_\varphi(c^*)\). The identities extend to the completion. Put \(\Omega_\varphi=\Lambda(1)\). It is a unit vector and its orbit \(\Lambda(M)\) is dense. If \(\pi_\varphi(c)\Omega_\varphi=0\), then \(\varphi(c^*c)=0\), so \(c=0\). This proves both faithfulness of the representation and separation of \(\Omega_\varphi\) for its image.

Normality requires an additional argument. For \(a,b,c\in M\),

\[
\langle\pi_\varphi(c)\Lambda(a),\Lambda(b)\rangle
=\varphi(b^*ca).
\tag{3A.7}
\]

As a function of \(c\), this belongs to \(M_*\) by (3A.3). Given arbitrary \(\xi,\eta\in H_\varphi\), choose \(\xi_j,\eta_j\in\Lambda(M)\) converging in norm to \(\xi,\eta\). Contractivity of \(\pi_\varphi\) gives, uniformly for \(\|c\|\le1\),

\[
\begin{gathered}
\left|\langle\pi_\varphi(c)\xi,\eta\rangle
-\langle\pi_\varphi(c)\xi_j,\eta_j\rangle\right|\\
\le \|\xi-\xi_j\|\|\eta\|
+\|\xi_j\|\|\eta-\eta_j\|.
\end{gathered}
\tag{3A.8}
\]

Thus all vector coefficient functionals of \(\pi_\varphi\) belong to the norm-closed subspace \(M_*\). If \(\rho\in B(H_\varphi)_*\), express it by (3A.2). Each term of \(\rho\circ\pi_\varphi\) belongs to \(M_*\), and the series converges there in norm, because the norm of its \(n\)-th term is at most \(\|\xi_n\|\|\eta_n\|\). Hence \(\rho\circ\pi_\varphi\in M_*\).

If \(c_i\to c\) ultraweakly in \(M\), evaluation by every such pullback gives \(\rho(\pi_\varphi(c_i))\to\rho(\pi_\varphi(c))\). This proves ultraweak continuity of \(\pi_\varphi\) for arbitrary nets, not just bounded nets. \(\square\)

### 3A.4. The faithful-state criterion

**Theorem 3A.4 (the faithful-state criterion).** Let \(M\) carry a faithful normal state \(\varphi\), and let \((x_i)\) be any net in a fixed norm-bounded subset of \(M\). For \(x\in M\),

\[
\begin{gathered}
q_\varphi(x_i-x)\longrightarrow0\\
\Updownarrow\\
x_i\longrightarrow x\text{ intrinsically ultrastrong*}\\
\Updownarrow\\
\pi(x_i)\longrightarrow\pi(x)\text{ strongly*}.
\end{gathered}
\tag{3A.9}
\]

for every faithful normal representation \(\pi\). The one-sided assertion with \(p_\varphi\), ultrastrong and strong also holds. No separability or factoriality assumption is needed.

**Proof.** Use Lemma 3A.3 and write \(\pi_\varphi=\pi_0\), \(\Omega_\varphi=\Omega\), and \(Q=\pi_0(M)\). By Theorem 3.1, \(Q\) is a von Neumann algebra on \(H_\varphi\). We first prove the commutant assertion used in the usual short argument. Let \(e\) be the orthogonal projection onto \(\overline{Q'\Omega}\). This subspace is invariant under \(Q'\) and its adjoints, so \(e\) commutes with \(Q'\) and belongs to \(Q''=Q\). Since \(1\in Q'\), \(e\Omega=\Omega\). The vector \(\Omega\) is separating for \(Q\), so \((1-e)\Omega=0\) gives \(e=1\). Therefore

\[
\overline{Q'\Omega}=H_\varphi.
\tag{3A.10}
\]

Put \(z_i=x_i-x\), with \(\|z_i\|\le C\). If \(p_\varphi(z_i)\to0\), then \(\|\pi_0(z_i)\Omega\|\to0\). For \(b'\in Q'\),

\[
\begin{gathered}
\|\pi_0(z_i)b'\Omega\|
=\|b'\pi_0(z_i)\Omega\|\\
\le\|b'\|\,p_\varphi(z_i)\longrightarrow0.
\end{gathered}
\tag{3A.11}
\]

For arbitrary \(\xi\in H_\varphi\) and \(v=b'\Omega\), boundedness gives
\(\|\pi_0(z_i)\xi\|\le C\|\xi-v\|+\|\pi_0(z_i)v\|\).
By (3A.10), first make the first term arbitrarily small and then let \(i\) tend along its directed set. Thus \(\pi_0(z_i)\to0\) strongly. Theorem 3.1 transfers this to all intrinsic seminorms and to every faithful normal representation. The converse follows by evaluating the state seminorm itself, or by testing \(\Omega\).

Finally \(q_\varphi(z_i)\to0\) is equivalent to both
\(p_\varphi(z_i)\to0\) and \(p_\varphi(z_i^*)\to0\). Apply the one-sided result twice. This proves all assertions without inferring convergence of adjoints from convergence of operators. \(\square\)

The hypotheses are substantive. A nonfaithful state on \(M_2(\mathbb C)\) given by the first coordinate vanishes on the nonzero projection \(e_{22}\). Boundedness also matters: on diagonal \(M=\ell^\infty(\mathbb N)\subset B(\ell^2)\), take
\(\varphi(a)=\sum_{n\ge1}2^{-n}a_n\) and \(z_n=2^{n/4}e_n\). Then \(q_\varphi(z_n)^2=2^{1-n/2}\to0\), but for the fixed vector \(\xi=(2^{-n/4})_{n\ge1}\in\ell^2\), \(\|z_n\xi\|=1\). This gives no strong convergence. These examples explain the exact faithful-state and bounded-family hypotheses; neither is silently omitted.

### 3A.5. Finite and moving normal-functional tests

The following estimate makes the bounded topology comparison uniform for finite tests, as needed when choosing an ordinary subsequence.

**Lemma 3A.5 (finite and moving normal-functional tests).** Fix \(0\le C<\infty\), a faithful normal state \(\varphi\), and \(\psi\in M_*^+\). Given any \(d>0\), there is \(a\in M\) with
\(\|\psi-a\varphi\|<d\), where \((a\varphi)(y)=\varphi(ya)\). For every \(\|z\|\le C\),

\[
q_\psi(z)^2
\le 2C^2d+\sqrt2\,C\,\varphi(a^*a)^{1/2}q_\varphi(z).
\tag{3A.12}
\]

Consequently \(q_\varphi(z_i)\to0\) on a fixed ball implies \(q_\psi(z_i)\to0\), uniformly over \(\psi\) in any fixed norm-compact subset of \(M_*^+\).

**Proof.** Each \(a\varphi\) is normal by (3A.3). If the norm closure of the linear subspace \(M\varphi\) were proper in \(M_*\), complex Hahn–Banach would give a nonzero continuous linear functional on \(M_*\) annihilating it. By \((M_*)^*=M\), it would be evaluation by a nonzero \(y\in M\). The resulting equations \(\varphi(ya)=0\) for all \(a\) contradict faithfulness on choosing \(a=y^*\). Therefore \(M\varphi\) is norm dense.

If \(0\le y\le C^2 1\), Cauchy–Schwarz and \(y^2\le C^2y\) give

\[
|\varphi(ya)|^2\le\varphi(y^2)\varphi(a^*a)
\le C^2\varphi(y)\varphi(a^*a).
\tag{3A.13}
\]

Apply this to \(y=z^*z\) and \(y=zz^*\), bounding each error \(|(\psi-a\varphi)(y)|\) by \(C^2d\). Add and use
\(\sqrt{s}+\sqrt{t}\le\sqrt{2(s+t)}\) to obtain (3A.12).
For a fixed finite collection of \(\psi\)'s, first choose \(d\) to make all the constant errors small, choose the corresponding \(a\)'s, and then choose a common threshold for \(q_\varphi(z)\). The cases \(C=0\) or \(\varphi(a^*a)=0\) need no division.

For positive \(\psi,\eta\) and \(\|z\|\le C\), the simpler estimate

\[
|q_\psi(z)^2-q_\eta(z)^2|
\le 2C^2\|\psi-\eta\|
\tag{3A.14}
\]

follows directly by evaluating \(z^*z+zz^*\). A norm-compact family has a finite norm \(\delta\)-net. Apply the finite-test assertion to its finitely many centers and then (3A.14); first shrink \(\delta\) and then the \(q_\varphi\) threshold. This proves uniformity. It also shows directly that if \(\psi_i\to\psi\) in predual norm and \(z_i\) is bounded with \(q_\varphi(z_i)\to0\), then \(q_{\psi_i}(z_i)\to0\). \(\square\)

### 3A.6. Joint ordinary extraction

**Corollary 3A.6 (joint ordinary extraction).** Let \(M\) carry a faithful normal state \(\varphi\). If \((b_n)\) is bounded and \(b_n\to0\) strongly* along a free ultrafilter \(\omega\), there is a strictly increasing sequence \(n_r\) with \(b_{n_r}\to0\) strongly*. At stage \(r\), the same indices can satisfy any prescribed finite collection of other conditions whose sets of valid indices belong to \(\omega\).

**Proof.** The estimates in Lemma 3A.5, and the state criterion, hold along a filter as well as a directed net: they specify finitely many tests and a scalar threshold. Thus \(\{n:q_\varphi(b_n)<1/r\}\in\omega\) for every positive integer \(r\). Intersect this set with any prescribed finite collection of other sets in \(\omega\), and with the cofinite set \(\{n:n>n_{r-1}\}\). Properness gives a choice \(n_r\) from their intersection. The sequence \(n_r\) is strictly increasing, and Theorem 3A.4 gives ordinary strong* convergence \(b_{n_r}\to0\).

Now suppose the predual is separable and, in the implementer application, the automorphisms \(\alpha_n=\operatorname{Ad}u'_n\) converge to \(\theta\) along \(\omega\) in the \(u\)-topology. All coordinates must use these same indices. If \(u'_n=v_nx_n^*\), then the selected sequence is \(u_r=v_{n_r}x_{n_r}^*\), and its defect is \(b_{n_r}=(u'_{n_r})^*\theta(u'_{n_r})-1\). Choose a norm-dense sequence \((\rho_j)\) in the predual unit ball and include
\(\|\rho_j\circ\alpha_n-\rho_j\circ\theta\|<1/r\) for \(j\le r\) among the finite tests. For arbitrary \(\rho\) in that ball and an approximating \(\rho_j\),

\[
\begin{gathered}
\|\rho\circ\alpha_{n_r}-\rho\circ\theta\|\\
\le 2\|\rho-\rho_j\|
+\|\rho_j\circ\alpha_{n_r}-\rho_j\circ\theta\|.
\end{gathered}
\tag{3A.15}
\]

First choose \(j\), then \(r\ge j\); scaling treats all \(\rho\in M_*\). Thus the same sequence retains the required \(u\)-topology limit and the strong* defect limit. This is an ordinary subsequence argument under separable predual; Lemma 3A.3, Theorem 3.1 and Theorem 3A.4 themselves retain their full arbitrary-net scope. \(\square\)

## 4. Constructing the left tracial representation

Let \(R\) be any von Neumann algebra with a faithful normal semifinite trace
\(\tau:R_+\to[0,\infty]\). A trace is additive and positively homogeneous on the positive cone and satisfies
\(\tau(c^*c)=\tau(cc^*)\) for \(c\in R\). Normality concerns all increasing positive nets. We may take semifiniteness to mean

\[
\begin{gathered}
\tau(t)=\sup\{\tau(b):0\leq b\leq t,\ \tau(b)<\infty\}
\\
\qquad(t\in R_+).
\end{gathered}
\tag{4.1}
\]

The proof below also covers the usual equivalent convention that the trace's finite ideal is ultraweakly dense; the finite-projection argument for that convention is given explicitly in Section 5.

Define the bounded square-integrable elements by

\[
\begin{gathered}
\mathfrak n_\tau=\{a\in R:\tau(a^*a)<\infty\},
\\
\qquad
\|a\|_{2,\tau}=\tau(a^*a)^{1/2}.
\end{gathered}
\tag{4.2}
\]

Every member is a bounded operator in \(R\); the Hilbert-space completion will contain further vectors.

The inequality
\((a+b)^*(a+b)\leq2a^*a+2b^*b\)
shows that \(\mathfrak n_\tau\) is a vector space. For \(x\in R\),

\[
\begin{gathered}
\tau((xa)^*(xa))\leq\|x\|^2\tau(a^*a),
\\
\qquad
\tau((ax)^*(ax))
\\
=\tau(a xx^*a^*)\leq\|x\|^2\tau(aa^*).
\end{gathered}
\tag{4.3}
\]

Traciality also gives \(\|a^*\|_{2,\tau}=\|a\|_{2,\tau}\). Thus \(\mathfrak n_\tau\) is a self-adjoint two-sided ideal.

To make mixed products precise, let \(\mathfrak m_\tau\) be the complex span of positive elements of finite trace. The trace extends linearly to this span. Its real extension is well-defined because equality \(b-c=d-e\), for positive finite-trace elements, gives \(b+e=d+c\); additivity then gives equal differences of trace values. Taking real and imaginary parts defines the complex extension. The polarization identity

\[
4b^*a=\sum_{k=0}^3 i^k
(a+i^k b)^*(a+i^k b)
\tag{4.4}
\]

puts \(b^*a\) in \(\mathfrak m_\tau\) for \(a,b\in\mathfrak n_\tau\). Hence

\[
\langle a,b\rangle_\tau=\tau(b^*a)
\tag{4.5}
\]

is a sesquilinear form, with the convention that the first variable is linear. It is positive definite by faithfulness. Cauchy–Schwarz follows by expanding the nonnegative quadratic
\(\tau((a+t b)^*(a+t b))\); the case \(\|b\|_{2,\tau}=0\) is immediate. Its norm is therefore \(\|\cdot\|_{2,\tau}\).

Let \(H_\tau\) be the Hilbert-space completion and let \(\Lambda_\tau:\mathfrak n_\tau\to H_\tau\) be its natural map. By definition,

\[
\overline{\Lambda_\tau(\mathfrak n_\tau)}=H_\tau,
\qquad
\|\Lambda_\tau(a)\|^2=\tau(a^*a).
\tag{4.6}
\]

Left multiplication extends by (4.3) to a bounded operator \(\lambda_\tau(x)\) satisfying

\[
\begin{gathered}
\lambda_\tau(x)\Lambda_\tau(a)=\Lambda_\tau(xa),
\\
\qquad
\|\lambda_\tau(x)\|\leq\|x\|.
\end{gathered}
\tag{4.7}
\]

Associativity on the dense domain gives multiplication. Also,

\[
\begin{gathered}
\langle\lambda_\tau(x)\Lambda_\tau(a),\Lambda_\tau(b)\rangle
\\
=\tau(b^*xa)
\\
=\langle\Lambda_\tau(a),\lambda_\tau(x^*)\Lambda_\tau(b)\rangle.
\end{gathered}
\tag{4.8}
\]

Thus \(\lambda_\tau\) is a unital *-representation. No vector \(\Lambda_\tau(1)\) is used: it might not exist when \(\tau(1)=\infty\).

## 5. Finite-trace cuts and faithfulness

Every nonzero projection \(h\in R\) contains a nonzero projection \(q\) with finite trace. Indeed, faithfulness and (4.1) give a nonzero \(b\) with \(0\leq b\leq h\) and \(\tau(b)<\infty\). By [TP3](../foundations/tracial-normality-foundations.md#tp3-the-exact-half-closed-spectral-cuts-used-by-finite-traces), for a suitable \(\varepsilon>0\), the spectral projection
\(q=1_{[\varepsilon,\infty)}(b)\)
is nonzero and satisfies

\[
\begin{gathered}
q\leq h,\qquad \varepsilon q\leq b,
\\
\qquad \tau(q)\leq\varepsilon^{-1}\tau(b)<\infty.
\end{gathered}
\tag{5.1}
\]

[TP2](../foundations/tracial-normality-foundations.md#tp2-arbitrary-joins-and-orthogonal-sums-of-projections) supplies arbitrary projection joins and the orthogonal finite-sum net. Choose by Zorn's lemma a maximal family \((q_j)_{j\in J}\) of nonzero pairwise orthogonal finite-trace projections. If \(1-\sum_jq_j\ne0\), (5.1) adds another member, contradicting maximality. Therefore, with finite subsets \(F\subseteq J\) directed by inclusion,

\[
e_F=\sum_{j\in F}q_j,\qquad
\tau(e_F)<\infty,\qquad e_F\uparrow1.
\tag{5.2}
\]

This is an actual net, with no countability assumption on \(J\).

Here is the promised argument for the other semifiniteness convention. Suppose the finite ideal \(\mathfrak m_\tau\) is ultraweakly dense. For \(h\ne0\), there must be \(a\in\mathfrak n_\tau\) with \(ha\ne0\): otherwise \(h\) annihilates \(\mathfrak n_\tau\), and, since this ideal is self-adjoint and every positive finite-trace \(b\) equals \((b^{1/2})^*b^{1/2}\), it annihilates \(\mathfrak m_\tau\). Ultraweak density would give \(h=0\). Now \(b=haa^*h\ne0\) has finite trace by (4.3) and traciality. Its spectral cuts again give (5.1), hence (5.2). Thus the construction does not leave a choice of semifiniteness convention as an extra theorem-sized gap.

If \(\lambda_\tau(x)=0\), then every \(e_F\) is a vector in \(\mathfrak n_\tau\), and

\[
0=\|\lambda_\tau(x)\Lambda_\tau(e_F)\|^2
=\tau(e_Fx^*xe_F).
\tag{5.3}
\]

Faithfulness of \(\tau\) forces \(xe_F=0\). Since \(e_F\uparrow1\) strongly in the original algebra, \(x=0\). This proves faithfulness of \(\lambda_\tau\), and therefore \(\|\lambda_\tau(x)\|=\|x\|\).

The cuts also give a useful dense core. For \(a\in\mathfrak n_\tau\), normality and traciality give

\[
\begin{aligned}
\|a-ae_F\|_{2,\tau}^2
&=\tau(a(1-e_F)a^*)\longrightarrow0,\\
\|a-e_Fa\|_{2,\tau}^2
&=\tau(a^*(1-e_F)a)\longrightarrow0.
\end{aligned}
\tag{5.4}
\]

For example, \(ae_Fa^*\uparrow aa^*\), whose trace is finite, so the first limit follows by subtraction of finite values. The second is identical with \(a\) and \(a^*\) exchanged. Equation (4.3) and the triangle inequality now give \(e_Fae_F\to a\) in square norm. Thus bounded elements in finite-trace corners have dense images in \(H_\tau\).

## 6. Normality of the representation

For \(a\in\mathfrak n_\tau\), the bounded positive functional

\[
\varphi_a(t)=\tau(a^*ta)\qquad(t\in R_+)
\tag{6.1}
\]

extends linearly to \(R\) because its value on positive \(t\) is at most
\(\|t\|\tau(a^*a)\). It is normal: if \(0\leq t_i\uparrow t\), then \(a^*t_i a\uparrow a^*ta\), and normality of \(\tau\) gives
\(\varphi_a(t_i)\uparrow\varphi_a(t)\).
[TP1](../foundations/tracial-normality-foundations.md#tp1-positive-functional-order-normality-and-ultraweak-continuity) therefore puts \(\varphi_a\) in \(R_*^+\).

Now let \(0\leq x_i\uparrow x\) in \(R\), and put \(d_i=x-x_i\). Then \(0\leq d_i\leq\|x\|1\), so

\[
\begin{gathered}
\|\lambda_\tau(d_i)\Lambda_\tau(a)\|^2
=\tau(a^*d_i^2a)
\\
\leq\|x\|\varphi_a(d_i)\longrightarrow0.
\end{gathered}
\tag{6.2}
\]

The operators \(\lambda_\tau(d_i)\) are uniformly bounded. Their convergence on the dense set (4.6) implies strong convergence on all of \(H_\tau\): approximate any vector by \(\Lambda_\tau(a)\) and bound the error uniformly by \(\|x\|\) times its Hilbert-space distance. Hence

\[
\lambda_\tau(x_i)\uparrow\lambda_\tau(x).
\tag{6.3}
\]

This also proves ultraweak normality explicitly. For a normal positive functional \(\omega\) on \(B(H_\tau)\), the functional \(\omega\circ\lambda_\tau\) preserves increasing suprema by (6.3), so belongs to \(R_*^+\) by the same [TP1 criterion](../foundations/tracial-normality-foundations.md#tp1-positive-functional-order-normality-and-ultraweak-continuity). Trace-class functionals on \(B(H_\tau)\) are linear combinations of positive ones. Thus every ultraweak functional pulls back to \(R_*\), precisely the assertion that \(\lambda_\tau\) is ultraweakly continuous.

[TP4](../foundations/tracial-normality-foundations.md#tp4-exact-application-to-the-tracial-representation) supplies the finite positive-functional extension and the full predual argument at these exact hypotheses. We have proved the full required statement.

**Theorem 6.1.** For every von Neumann algebra \(R\) with a faithful normal semifinite trace \(\tau\), the construction (4.2)–(4.8) gives a faithful normal unital left representation on \(H_\tau\). Its bounded finite-square-norm vectors \(\Lambda_\tau(\mathfrak n_\tau)\) are dense; finite-trace-corner vectors are already dense. The represented algebra is a von Neumann algebra, and Theorem 3.1 applies to it. All assertions use the actual indexing nets, with arbitrary cardinality.

## 7. The exact return to the finite free-action proof

Let \(a\in R\) satisfy \(\tau(a^*a)<\infty\), and let \(x_i\in R\) be a norm-bounded net tending intrinsically ultrastrongly to zero. Then \(a^*\in\mathfrak n_\tau\). Theorem 3.1 and (4.7) give

\[
\begin{gathered}
\|ax_i^*\|_{2,\tau}
=\|x_i a^*\|_{2,\tau}
\\
=\|\lambda_\tau(x_i)\Lambda_\tau(a^*)\|
\longrightarrow0.
\end{gathered}
\tag{7.1}
\]

The first equality uses the trace of an element and its adjoint. For bounded \(b\in R\), traciality and \(bb^*\leq\|b\|^21\) give

\[
\begin{gathered}
\|(ax_i^*)b\|_{2,\tau}^2
=\tau((ax_i^*)bb^*(ax_i^*)^*)
\\
\leq\|b\|^2\|ax_i^*\|_{2,\tau}^2.
\end{gathered}
\tag{7.2}
\]

Testing (7.2) on \(b\in\mathfrak n_\tau\) proves strong convergence of \(\lambda_\tau(ax_i^*)\) on the dense bounded square-integrable vectors. The operators are uniformly bounded by \(\|a\|\sup_i\|x_i\|\), so this convergence holds on all of \(H_\tau\). The inverse implication in Theorem 3.1 finally gives

\[
\begin{gathered}
ax_i^*\longrightarrow0
\\
\quad\text{intrinsically ultrastrongly in }R.
\end{gathered}
\tag{7.3}
\]

These are precisely the representation, density, and topology steps used in the finite free-action lesson's (L1).

For its (F6), let \(P\subseteq Q\) be the normal inclusion already constructed there, let \(\operatorname{Tr}\) be its faithful normal semifinite trace, and let \(e_B\in Q\) be a projection with \(\operatorname{Tr}(e_B)<\infty\). A bounded ultrastrong-null net \(x_i\in P\) remains ultrastrong-null in \(Q\) by Corollary 3.2. Equation (7.3) with \(a=e_B\) gives \(z_i=e_Bx_i^*\to0\) ultrastrongly. Equations (2.1)–(2.2) imply

\[
z_i^*z_i=x_i e_Bx_i^*\longrightarrow0
\quad\text{ultraweakly in }Q.
\tag{7.4}
\]

The bridge has already proved that \(\Phi/n\) is a normal unital completely positive map, \(\Phi(e_Bx_i^*)=x_i^*\), and \(n=|K|\). Its retained Schwarz inequality consequently gives the unchanged constant and orientation

\[
\begin{gathered}
x_i x_i^*
=\Phi(e_Bx_i^*)^*\Phi(e_Bx_i^*)
\\
\leq n\Phi(x_i e_Bx_i^*)
\longrightarrow0\quad\text{ultraweakly}.
\end{gathered}
\tag{7.5}
\]

Normality of \(\Phi\) justifies the last limit. Testing positive normal functionals then proves ultrastrong convergence of \(x_i^*\). This closes the targeted representation/topology interface; it does not replace the free-action bridge's crossed-product, standard-form, or center-valued-trace proofs.

## 8. Exercises with solutions

**Exercise 8.1 (Why is the norm bound visible).**

Locate the norm bound in the reverse implication of Theorem 3.1, and explain why pointwise testing on vectors alone does not justify omitting it for an arbitrary net.

*Solution.* It bounds both \(\pi(z_i^*z_i)\) for (2.3) and \(z_i^*z_i\) for the compact-ball inverse (3.1). Strong convergence of a sequence implies a global norm bound by uniform boundedness, but a convergent net need not have a norm-bounded tail common to every vector. For an explicit example on an infinite-dimensional \(H\), direct pairs \((F,n)\) by inclusion of finite subsets \(F\subset H\) and the usual order of \(n\in\mathbb N\). Choose a unit vector \(v_F\perp\operatorname{span}(F)\), and put \(T_{F,n}=nP_{\mathbb Cv_F}\). Each fixed vector \(\xi\) is annihilated once \(F\) contains \(\xi\), so this net is strong-null; every tail still has unbounded operator norms. The theorem's explicit hypothesis avoids replacing its net by a sequence or using a nonexistent common tail. Its forward implication (3.2) requires no norm bound.

**Exercise 8.2 (A trace with no faithful state).**

Let \(I\) be uncountable, \(R=\ell^\infty(I)\), and
\(\tau(f)=\sum_{s\in I}f(s)\) for \(f\geq0\), where the sum is the supremum of finite subsums. Describe \(H_\tau\), \(\lambda_\tau\), and the net (5.2). Show that no faithful normal state can replace \(\tau\).

*Solution.* Here \(\mathfrak n_\tau=\ell^\infty(I)\cap\ell^2(I)=\ell^2(I)\), since a square-summable function is bounded. Its Hilbert completion is \(\ell^2(I)\), and \(\lambda_\tau(f)\) is coordinatewise multiplication. For finite \(F\subseteq I\), \(e_F=1_F\) increases strongly to \(1\). Finite-support vectors are dense. Every normal state is given by nonnegative \(\ell^1(I)\) weights of sum one; only countably many are nonzero, so the state vanishes on some nonzero singleton projection and is not faithful. The trace and the full net nevertheless have exactly the required scope.

**Exercise 8.3 (Strong convergence does not automatically pass to adjoints).**

On \(\ell^2(\mathbb N_0)\), let \(S\) be the unilateral shift. Show that \(x_n=(S^*)^n\to0\) strongly but \(x_n^*=S^n\) does not. Check that (7.3) remains true for a square-integrable bounded \(a\) and the usual semifinite trace on \(B(\ell^2)\).

*Solution.* For \(\xi\in\ell^2\),
\(\|(S^*)^n\xi\|^2=\sum_{k\geq n}|\xi_k|^2\to0\).
But \(\|S^n\xi\|=\|\xi\|\), so the adjoints do not tend strongly to zero. If \(a\) is bounded Hilbert–Schmidt, (7.1) gives
\(\|aS^n\|_2=\|(S^*)^n a^*\|_2\to0\).
Theorem 3.1 and (7.2) then give \(aS^n\to0\) ultrastrongly. The finite-square-norm multiplier, rather than bare adjoint continuity, is responsible for this conclusion.

**Exercise 8.4 (Two distinct faithfulness arguments).**

Explain which faithfulness assumption is used in (5.3), and which is used in (3.1). Is normality alone enough for the reverse topology implication?

*Solution.* Equation (5.3) uses faithfulness of the trace to deduce \(xe_F=0\) from zero square norm, then the projection net deduces \(x=0\). This proves faithfulness of the newly built representation. Equation (3.1) uses faithfulness of the representation to obtain injectivity, isometry, and a compact-to-Hausdorff bijection on each ball. A nonfaithful normal representation kills every element of its kernel; a constant nonzero net in that kernel has zero represented image but cannot be ultrastrong-null because normal positive functionals separate positive elements. Normality alone proves only the forward implication.

**Exercise 8.5 (Recover the Schwarz constant).**

Suppose \(\Psi=\Phi/n\) is unital completely positive, \(e_B\) is a projection, and \(z=e_Bx^*\) with \(\Phi(z)=x^*\). Starting from Schwarz for \(\Psi\), derive the inequality in (7.5).

*Solution.* Schwarz reads
\(\Psi(z)^*\Psi(z)\leq\Psi(z^*z)\).
Since \(\Psi(z)=x^*/n\), multiply by \(n^2\) to obtain
\(xx^*\leq n\Phi(z^*z)=n\Phi(xe_Bx^*)\).
For the bounded net under discussion, (7.4) and normality of \(\Phi\) make the right-hand side ultraweak-null. Every positive normal functional then vanishes in the limit on \(x_i x_i^*\), proving the required ultrastrong convergence of \(x_i^*\).

## 9. Source roles and the remaining foundations

The original reconstruction's accessed primary proof provider is [Jesse Peterson, *Notes on von Neumann algebras*, April 5, 2013](https://math.vanderbilt.edu/peters10/teaching/spring2013/vonNeumannAlgebras.pdf). Its exact consumed foundational locators are listed in Section 1; Section 2.6, Theorem 2.6.4 and Corollary 2.6.5 supplied the original Kaplansky/unit-ball comparison. The accompanying HAP04–HAP05 proof now supplies the exact nondegenerate Kaplansky input used in Theorem 3.1. The proof here of bounded representation transport is (3.1)–(3.3); the complete semifinite tracial construction is (4.2)–(6.3). Peterson's Corollary 4.2.3 is a statement about normal states; it is not used as a substitute for our semifinite trace proof.

The [finite free-action lesson](finite-free-actions-and-coboundaries.md), Section 6 (L1) and Section 7 (F6), consumes exactly the representation and topology results proved here. For classical trace and representation theory, see Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979, first-edition reprint, [DOI 10.1007/978-1-4612-6188-9](https://doi.org/10.1007/978-1-4612-6188-9). The proof above uses the precise Peterson foundations listed in Section 1 and the compact-ball and tracial constructions given here. The bounded-adjoint argument (7.1)–(7.3) is the classical argument of Takesaki I, Lemma V.2.27 with its faithful normal tracial representation and topology transport established in Sections 3–6. This identifies the mathematical source of that argument without treating the normal-state GNS construction as a semifinite proof.

Fumio Hiai's [*Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383v1](https://arxiv.org/abs/2004.02383) was checked at its contents and introductory Sections 1.1–1.3 as an optional overview. Its introductory GNS description is not a complete proof of this consumer interface and is not used as one.

The accompanying programme proofs named in Section 1 now supply the exact predual, bounded-calculus, Hilbert, compactness and nondegenerate density inputs for Theorem 3.1 and Section 3A. Their complete statements and proofs retain arbitrary Hilbert spaces and nets. The faithful-state subsection develops the brief commutant-orbit argument in *Central sequences, fullness and free group factors*, Section 2 before Lemma 2.2, and the norm density of \(M\varphi\) from its Lemma 1.1. Lemmas 3A.1–3A.3 provide the normality and topology foundations explicitly; Theorem 3A.4 and Lemma 3A.5 give the state and moving-test criteria; Corollary 3A.6 gives the jointly indexed extraction.

The additional order-normality and projection inputs for the semifinite construction are now supplied in the [tracial-normality companion](../foundations/tracial-normality-foundations.md), with their full preceding proofs and source/change notices. TP1 proves the bounded positive-functional equivalence using the full arbitrary-weight theorem; TP2–TP3 give the exact joins and half-closed threshold cuts used in Section 5; TP4 verifies their application to the tracial representation. A faithful state is used only inside supported corners in the normal-weight proof, whose return to arbitrary algebras is explicit. The free-action bridge's standard-form existence/canonical implementation, finite center-valued trace existence and its other construction inputs remain separate prerequisites. These supplied arguments do not certify the entire lesson, the full P514 dependency graph or every general trace/weight or spectral theorem.

