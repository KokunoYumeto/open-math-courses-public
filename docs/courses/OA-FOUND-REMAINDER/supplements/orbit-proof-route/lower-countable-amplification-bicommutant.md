<span id="countable-amplification-and-the-ultraweak-bicommutant-closure"></span>
# Countable amplification and the ultraweak bicommutant closure

<span id="oa-mod-ba-01--statement-and-conventions"></span>
<span id="OA-MOD-BA-01"></span>
<span id="oa-mod-ba-01"></span>
## OA-MOD-BA-01 — Statement and conventions

Let \(K\) be an arbitrary complex Hilbert space, with inner products linear in the first variable. Let \(A\subseteq B(K)\) be a complex unital *-subalgebra, without any initial closure assumption. Then
\[
 \overline A^{\,\mathrm{ultraweak}}=A''.
 \tag{BA.1}
\]
In particular, if \(A\) is ultraweakly closed, then \(A=A''\), so \(A\) is WOT closed and SOT closed. More precisely, each \(T\in A''\) lies in the sigma-strong closure of \(A\): for every finite family of square-summable vector sequences \((u_{k,n})_n\) and positive tolerances \(\varepsilon_k\), an \(a\in A\) can be chosen with
\[
 \left(\sum_n\|(T-a)u_{k,n}\|^2\right)^{1/2}<\varepsilon_k
 \quad\text{for every }k.
 \tag{BA.2}
\]
The proof of (BA.1) below directly tests the ultraweak functionals, so it does not require a further convex-closure theorem.

A unital algebra on the zero Hilbert space is included; all statements there are immediate. For a possibly degenerate represented algebra with identity projection \(p\), the theorem is applied on \(pK\).

<span id="exact-prerequisites"></span>
## Exact prerequisites

The proof uses the Hilbert completion, orthogonal projection and Cauchy–Schwarz results in [Hilbert spaces and compact operators](../../../foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html); the elementary commutant and bounded weak-operator facts of BK-02 and BK-03; and the concrete-predual vector-series representation of CP-03, CP-04 and CP-06. These are bounded Hilbert/operator facts. It does not use a standard form, a normal weight, the normal-map converse, an unbounded spectral theorem, or a Kaplansky density theorem.

The Hilbert direct sum needed here can be defined directly as
\[
 \ell^2(K)=\{(v_n):\ \sum_n\|v_n\|^2<\infty\},
 \qquad
 \langle v,w\rangle=\sum_n\langle v_n,w_n\rangle.
\]
Cauchy–Schwarz makes the pairing absolutely convergent. Finite-support vectors are dense by truncation. Completeness follows by taking coordinate limits of a Cauchy sequence, bounding every finite partial sum by the same Cauchy estimate, and then taking the supremum of these finite sums. Thus no dimension restriction on \(K\) is introduced by the countable amplification. A finite family of countable index sets can equally be used as its coordinate set.

For \(x\in B(K)\), write \(D(x)\) for coordinatewise multiplication by \(x\) on \(\ell^2(K)\). The inequalities
\(\sum_n\|xv_n\|^2\leq\|x\|^2\sum_n\|v_n\|^2\)
show that \(D(x)\) is bounded, and coordinate pairings give \(D(x)^*=D(x^*)\).

<span id="the-orbit-projection"></span>
## The orbit projection

Fix \(\Xi\in\ell^2(K)\), and let
\[
 L=\overline{\{D(a)\Xi:a\in A\}}^{\,\|\cdot\|}.
 \tag{BA.3}
\]
The set inside the closure is linear because \(A\) is linear. Multiplicativity gives \(D(a)L\subseteq L\) for every \(a\in A\). The same is true of \(D(a)^*=D(a^*)\). Thus \(L\) reduces every \(D(a)\), and its orthogonal projection \(P\) commutes with each \(D(a)\).

Let \(\iota_j:K\to\ell^2(K)\) insert a vector into coordinate \(j\), and put
\[
 P_{ij}=\iota_i^*P\iota_j\in B(K).
\]
Taking matrix entries of \(PD(a)=D(a)P\) gives
\[
 P_{ij}a=aP_{ij}\qquad(a\in A).
\]
Consequently \(P_{ij}\in A'\) for every \(i,j\).

Now let \(T\in A''\). It commutes with every \(P_{ij}\). For a finite-support vector \(v\), the \(i\)-th coordinates of \(PD(T)v\) and \(D(T)Pv\) are respectively
\[
 \sum_jP_{ij}Tv_j,\qquad \sum_jTP_{ij}v_j.
\]
Both sums here are finite and are equal. Equality of every coordinate proves equality of the two vectors. The operators \(PD(T)\) and \(D(T)P\) are bounded, so density of finite-support vectors extends this equality to all of \(\ell^2(K)\). Therefore \(D(T)\) commutes with \(P\).

Because \(1\in A\), we have \(\Xi=D(1)\Xi\in L\). It follows that
\[
 P D(T)\Xi=D(T)P\Xi=D(T)\Xi.
\]
Thus \(D(T)\Xi\in L\). By the definition of \(L\), for each \(\delta>0\) there is \(a\in A\) such that
\[
 \|D(T-a)\Xi\|<\delta.
 \tag{BA.4}
\]
This is approximation for the actual chosen square-summable family; no operator-norm bound on \(a\) is claimed or used. Concatenating any finite collection of vector sequences into \(\Xi\), and taking \(\delta\) smaller than each prescribed tolerance, proves (BA.2).

<span id="ultraweak-approximation"></span>
## Ultraweak approximation

Let \(f_1,\ldots,f_m\) be a finite family of ultraweakly continuous complex linear functionals on \(B(K)\), with positive tolerances \(\varepsilon_1,\ldots,\varepsilon_m\). By CP-03, CP-04 and CP-06, each functional has a vector-series representation
\[
 f_k(x)=\sum_{n=1}^\infty\langle x u_{k,n},v_{k,n}\rangle,
 \qquad
 \sum_n\|u_{k,n}\|\,\|v_{k,n}\|<\infty.
 \tag{BA.5}
\]
Terms with a zero vector may be omitted. Rescale the two vectors in each remaining term by reciprocal positive factors, leaving the coefficient unchanged, so that both vector norms equal
\(\sqrt{\|u_{k,n}\|\,\|v_{k,n}\|}\).
After this balancing, both \((u_{k,n})_n\) and \((v_{k,n})_n\) are square summable.

Use coordinates \((k,n)\) in a single Hilbert direct sum and put
\[
 \Xi_{k,n}=u_{k,n}.
\]
The finite number of functionals makes \(\Xi\) square summable. Let \(\Eta^{(k)}\) have entries \(v_{k,n}\) in the \(k\)-th row and zero in the other rows. Then (BA.5) is exactly
\[
 f_k(x)=\langle D(x)\Xi,\Eta^{(k)}\rangle.
\]
Choose
\[
 0<\delta<\min_{1\leq k\leq m}
       \frac{\varepsilon_k}{1+\|\Eta^{(k)}\|}.
\]
Apply (BA.4) to find one \(a\in A\) with \(\|D(T-a)\Xi\|<\delta\). Cauchy–Schwarz gives, simultaneously for every \(k\),
\[
 |f_k(T-a)|
 \leq\|D(T-a)\Xi\|\,\|\Eta^{(k)}\|
 <\varepsilon_k.
\]
If the family of tests is empty there is nothing to check. Thus every ultraweak neighborhood of \(T\) meets \(A\), proving
\(A''\subseteq\overline A^{\,\mathrm{ultraweak}}\).

Conversely, \(A''\) is WOT closed: its commutation equations are closed under matrix-coefficient convergence, because fixed left and right multiplication are WOT continuous. It is therefore ultraweakly closed, since every vector coefficient is ultraweakly continuous. Since \(A\subseteq A''\), we have
\(\overline A^{\,\mathrm{ultraweak}}\subseteq A''\).
This proves (BA.1). A bicommutant is SOT closed as well, by the same fixed-multiplication argument or BK-02. \(\square\)

<span id="application-to-wh-02-and-the-oa-flow-gns-contract"></span>
## Application to WH-02 and the OA-FLOW GNS contract

At the 48,230-byte WH manuscript, SHA-256
43274e05ac747aab3b3e5b422fe99b5a05383c8ec451778c53185d242aeea7de,
WH-02 lines 30–38 prove isometry and ultraweak closure of the faithful normal representation image. Its identity is \(p=\pi(1)\). Compression and zero extension identify its inherited ultraweak topology with that on \(B(pH)\): the coefficient of the zero extension at \(\xi,\eta\in H\) equals the corner coefficient at \(p\xi,p\eta\), and the same observation applies to the square-summable vector series. Thus the image is an ultraweakly closed unital *-subalgebra of \(B(pH)\).

Apply (BA.1) on \(pH\). This proves precisely the WOT/bicommutant-closed concrete von Neumann algebra assertion in WH-02 line 38. WH-02 line 40 can then apply NP-04 and NP-06 to both directions of the positive *-isomorphism, giving the stated ultraweak and sigma-strong-star homeomorphism. For the unital GNS representation, \(p=I\).

Together with the GNS construction, this proves the concrete-image assertion used in OA-FLOW.DW.IMPORT.GNS. It does not establish any natural cone, relative Tomita operator, modular automorphism theorem or Connes derivative.

<span id="validation-and-status"></span>
## Proof boundary

The theorem uses bounded Hilbert-space, commutant and predual results. The normal-map, weight and unbounded-operator conclusions require their separate proofs.

