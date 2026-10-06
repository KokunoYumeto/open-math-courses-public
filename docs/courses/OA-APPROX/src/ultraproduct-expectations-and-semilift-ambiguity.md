# Ultraproduct expectations and semi-lift ambiguity

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

The [multiplier construction](multiplier-ultraproducts-and-normal-embeddings.md) gives a von Neumann algebra \(M^\omega=N_\omega/I_\omega\) with a normal constant copy of \(M\). Taking the ultraweak limit of a representative recovers an element of \(M\). We construct this map, prove its normality directly, and use it to distinguish the information in a convergent automorphism family from the information in its limit.

Throughout Sections 1–2, \(M\) has a faithful normal state \(\varphi\), and \(\omega\) is free. Section 3 assumes separable predual when using \(M_\omega=C_\omega/I_\omega\). Section 4 uses the tracial hyperfinite \(\mathrm{II}_1\) factor \(R\). Inputs are the preceding quotient and normal embedding proofs, ultraweak compactness of bounded balls, and the already proved tensor model for \(R\). We construct the expectation directly from the quotient.

## 1. The canonical ultraweak-limit map

**Theorem 1.1.** The formula
\[
E_\omega(\pi(x_n))=\operatorname*{uw-lim}_{n\to\omega}x_n
\tag{1}
\]
defines a faithful normal unital completely positive \(M\)-bimodule map \(E_\omega:M^\omega\to M\). It fixes the constant copy of \(M\), and
\[
\varphi\circ E_\omega=\varphi^\omega.
\tag{2}
\]
In particular it is an expectation onto that copy.

**Proof.** A bounded sequence has a unique ultraweak ultralimit, since a bounded closed ball of \(M\) is compact Hausdorff for that topology. A sequence in \(I_\omega\) converges strong* to zero along \(\omega\), hence ultraweakly to zero. Thus (1) is independent of the representative.

It is linear, unital and fixes constants. For \(a,b\in M\), their constant sequences are multipliers, and separate ultraweak continuity of multiplication gives
\[
E_\omega(aXb)=aE_\omega(X)b.
\tag{3}
\]
Complete positivity can be checked at every finite matrix level. A positive element of \(M_k(M^\omega)\) has a positive lift in \(M_k(N_\omega)\): lift its positive square root and multiply the lift by its adjoint. Every coordinate matrix is positive. Its entrywise ultraweak limit is positive because the positive cone of \(M_k(M)\) is ultraweakly closed. These entries are exactly the values of the matrix amplification of (1).

Equation (2) follows from the definition of the quotient state. To prove normality, let \(0\le X_i\uparrow X\) be an arbitrary bounded increasing net in \(M^\omega\), and put \(Y=\sup_i E_\omega(X_i)\) in \(M\). Positivity gives \(Y\le E_\omega(X)\). Normality of the two states and (2) give
\[
\varphi(E_\omega(X)-Y)
=\varphi^\omega(X)-\lim_i\varphi^\omega(X_i)=0.
\tag{4}
\]
The positive difference vanishes by faithfulness of \(\varphi\). Thus \(E_\omega\) preserves increasing positive suprema and is normal. If \(X\ge0\) and \(E_\omega(X)=0\), then \(\varphi^\omega(X)=0\); the faithful quotient state makes \(X=0\). This proves faithfulness as well. \(\square\)

The map depends on the ultrafilter but not on the state used to describe the strong*-null ideal. The state identity (2) is a convenient proof of normality, rather than an extra definition of the map.

## 2. Covariance of a chosen semi-lift

For a fixed normal automorphism \(\beta\), write \(\beta^\omega\) for its constant lift. If \(\beta_n\to\beta\) in the \(u\)-topology, retain the family in
\[
\Gamma_{(\beta_n)}(\pi(x_n))=\pi(\beta_n(x_n)).
\tag{5}
\]
The preceding lesson proves that this is a normal automorphism, and that its restriction to \(M\) is \(\beta\).

**Proposition 2.1.** Every such chosen family satisfies
\[
E_\omega\Gamma_{(\beta_n)}=\beta E_\omega.
\tag{6}
\]

**Proof.** If \(\|x_n\|\le C\) and \(\psi\in M_*\), then
\[
|\psi(\beta_n(x_n))-\psi(\beta(x_n))|
\le C\|\psi\circ\beta_n-\psi\circ\beta\|\longrightarrow0.
\tag{7}
\]
The ultraweak ultralimit of \(\beta(x_n)\) is \(\beta(E_\omega(X))\), by normality of \(\beta\). Taking scalar ultralimits in (7) proves (6). \(\square\)

Consequently every convergent family with limit \(\beta\) gives the same action on the constant algebra and the same covariance with \(E_\omega\). These two conclusions do not determine its action on varying quotient elements. Nor is \(\varphi^\omega\) automatically preserved: its transformed state is \((\varphi\circ\beta)\circ E_\omega\), which equals \(\varphi^\omega\) when \(\beta\) preserves \(\varphi\).

## 3. A trace with values in the original center

Assume now that \(M\) has separable predual, without imposing a factor hypothesis. The preceding lesson embeds the finite von Neumann algebra \(M_\omega\) normally in \(M^\omega\).

**Theorem 3.1.** The restriction
\[
T_\omega=E_\omega|_{M_\omega}:M_\omega\to Z(M)
\tag{8}
\]
is a faithful normal unital positive trace with values in \(Z(M)\). It fixes the constant copy of \(Z(M)\), is a \(Z(M)\)-bimodule map, and satisfies
\[
T_\omega(XY)=T_\omega(YX),\qquad X,Y\in M_\omega.
\tag{9}
\]
Here the specified value algebra is the center of the original \(M\); no equality with \(Z(M_\omega)\) is asserted.

**Proof.** For \(X=\pi(x_n)\), centralizing means \(\|[x_n,\psi]\|\to_\omega0\) for every \(\psi\in M_*\). For fixed \(a\in M\), this gives
\[
|\psi(x_na-ax_n)|\le\|a\|\|[x_n,\psi]\|\to_\omega0.
\tag{10}
\]
Passing to the ultraweak limit shows that \(E_\omega(X)\) commutes with every \(a\), so belongs to \(Z(M)\). For centralizing representatives \(x_n,y_n\),
\[
|\psi(x_ny_n-y_nx_n)|
\le\sup_n\|y_n\|\|[x_n,\psi]\|\to_\omega0,
\tag{11}
\]
which proves (9) for every normal functional.

The positivity, faithfulness and normality are restrictions of Theorem 1.1. A constant central element is centralizing, since its functional commutators vanish exactly. Equations (1) and (3) therefore give the remaining assertions. \(\square\)

If \(M\) is a factor, the value algebra is \(\mathbb C1\). Thus \(T_\omega(X)=\tau_\omega(X)1\), and the trace on \(M_\omega\) is independent of the particular faithful normal state of \(M\). For a nonfactor, composing (8) with a faithful normal state on \(Z(M)\) gives its corresponding faithful normal scalar trace.

## 4. Two different semi-lifts with the same limit

Use the concrete tracial tensor model
\[
R=\overline{\bigotimes_{n\ge1}(M_2,\operatorname{tr}_2)}^{\,\mathrm{vN}}.
\tag{12}
\]
Let \(z_n\) and \(x_n\) be identity on every tensor leg except leg \(n\), where they equal
\[
z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
x=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{13}
\]
They are self-adjoint unitaries, with trace zero and \(zx=-xz\). Each sequence commutes eventually with every finite tensor word. Approximating any \(a\in R\) in trace \(2\)-norm by such words proves
\[
\|[z_n,a]\|_2,\ \|[x_n,a]\|_2\longrightarrow0.
\tag{14}
\]
The finite trace centralizing criterion from the preceding lessons makes these sequences centralizing. Equivalently, finite tensor densities are dense in \(L^1(R,\tau)\), so their commutation proves the required convergence against every normal functional.

Put \(Z=\pi(z_n)\), \(X=\pi(x_n)\) in \(R_\omega\). They satisfy
\[
Z^2=X^2=1,\qquad Z^*=Z,\quad X^*=X,\qquad ZX=-XZ.
\tag{15}
\]
Their trace \(2\)-norms are one, so neither is zero.

**Proposition 4.1.** The families \(\beta_n=\operatorname{Ad}(z_n)\) and \(\widetilde\beta_n=\mathrm{id}\) both converge to \(\mathrm{id}\) in the \(u\)-topology, but induce different normal automorphisms of \(R^\omega\), even on \(R_\omega\).

**Proof.** The ordinary centralizing unitary criterion gives \(\operatorname{Ad}(z_n)\to\mathrm{id}\) in the \(u\)-topology. It can also be checked directly on the dense finite tensor normal functionals: they are eventually fixed, and conjugation is an isometry on the predual. The induced automorphisms are
\[
\Gamma_{(\beta_n)}=\operatorname{Ad}(Z),\qquad
\Gamma_{(\widetilde\beta_n)}=\mathrm{id}.
\tag{16}
\]
By (15), the first sends \(X\) to \(-X\), whereas the second fixes \(X\). Their difference on \(X\) has trace \(2\)-norm two. Both restrict to the identity on constant \(R\) and obey \(E_\omega\Gamma=E_\omega\). \(\square\)

A prescribed constant restriction therefore does not determine the automorphism on varying quotient elements. What is proved for each chosen family is a normal automorphism with that constant restriction and the covariance (6). The family cannot be suppressed from the notation merely because it converges.

## 5. Two limits on a fast reindexing theorem

The same example prevents fast reindexing with unrestricted semi-lift equivariance.

**Proposition 5.1.** There are separable von Neumann subalgebras \(P,Q\subset R^\omega\) and a countable group \(G\) of semi-liftable automorphisms preserving \(P\), for which no injective *-homomorphism can satisfy simultaneously
\[
\Phi(P\cap R_\omega)\subset Q'\cap R_\omega,
\qquad \gamma\Phi=\Phi\gamma\quad(\gamma\in G).
\tag{17}
\]

**Proof.** Take \(P=Q=W^*(X,Z)\), and \(G=\{\mathrm{id},\gamma\}\), with \(\gamma=\operatorname{Ad}(Z)\). Relations (15) give \(P\cong M_2\): the projections \((1\pm Z)/2\), and their off-diagonal operators obtained from \(X\), are matrix units. Both projections have trace \(1/2\), so the representation is faithful. In particular \(P\) has separable predual and lies in \(R_\omega\). The group has order two, is semi-liftable by (16), and preserves \(P\).

The first condition of (17) makes \(\Phi(X)\) commute with \(Z\), hence \(\gamma(\Phi(X))=\Phi(X)\). Equivariance and \(\gamma(X)=-X\) instead give \(\gamma(\Phi(X))=-\Phi(X)\). Thus \(\Phi(X)=0\), contradicting injectivity. \(\square\)

There is also a separate obstruction to full scalar trace independence when constants are fixed. Let \(a=x\) be a constant trace-zero self-adjoint unitary in \(M_2\subset R\), and let \(P,Q\) contain it. Then
\[
\tau^\omega(a\Phi(x))=\tau(a^2)=1,
\qquad
\tau^\omega(a)\tau^\omega(x)=0
\tag{18}
\]
for every map fixing that constant. Thus scalar factorization cannot hold for arbitrary \(x\in P,a\in Q\). In a nontracial algebra a scalar trace on all \(M^\omega\) is not part of the construction in the first place.

The [next lesson](fast-reindexing-with-liftable-actions.md) proves the corrected fast result: equivariance for a countable group of constant lifts, and the identity
\[
E_\omega(a\Phi(x))=E_\omega(a)E_\omega(x),
\qquad x\in P,\ a\in Q.
\tag{19}
\]
For a factor and a centralizing \(x\), its right side has the scalar factorization suggested by the source. The domain assignment \(x\in P,a\in Q\) is necessary because \(\Phi\) is defined on \(P\).

## 6. Exercises with complete solutions

**Exercise 1.** Why does a positive matrix in the quotient have a positive matrix lift for the complete positivity argument?

*Solution.* The quotient map \(M_k(N_\omega)\to M_k(M^\omega)\) is surjective. Lift the positive square root of the given matrix to \(B\), and use \(B^*B\). Its image is the original positive matrix. Every coordinate of \(B^*B\) is positive, so taking ultraweak limits proves positivity at that matrix level.

**Exercise 2.** Prove normality of \(E_\omega\) without interchanging an increasing supremum with an ultralimit.

*Solution.* Form the supremum \(Y\) of the increasing images in the already known von Neumann algebra \(M\). Positivity gives \(Y\le E_\omega(X)\). The normal state identity (2) gives zero value on their positive difference, as in (4), and faithfulness makes the difference zero. No interchange of two limits is used.

**Exercise 3.** What changes if \(M\) has a nontrivial center?

*Solution.* The ultraweak limit of a centralizing representative need only be central, rather than scalar. Equations (10)–(11) still prove a normal \(Z(M)\)-valued trace. A scalar trace on \(M_\omega\) is then obtained by composing with a normal state on the original center; different center states can give different scalar traces.

**Exercise 4.** Check the off-diagonal matrix units in the counterexample.

*Solution.* Put \(e=(1+Z)/2\), \(f=(1-Z)/2\), \(v=eXf\). Anticommutation gives \(Xf=eX\) and \(Xe=fX\). Hence \(vv^*=e\), \(v^*v=f\), \(v^2=0\), and \(e+f=1\). Together with \(e,f,v,v^*\), these are a unital \(M_2\) system. Since \(E_\omega(Z)=0\), both diagonal projections have trace \(1/2\).

**Exercise 5.** Compute the size of the ambiguity between the two semi-lifts on \(X\).

*Solution.* One sends \(X\) to \(-X\), and the other sends it to \(X\). The difference is \(-2X\), with squared trace \(2\)-norm \(4\tau_\omega(X^*X)=4\). In particular it is neither zero nor a strong*-null quotient element.

**Exercise 6.** Explain why covariance with \(E_\omega\) does not detect this ambiguity.

*Solution.* The element \(X\) has ultraweak limit zero, so \(E_\omega(X)=E_\omega(-X)=0\). Both families have identity limit and therefore satisfy (6) with that limit. The faithful expectation detects positive elements faithfully, but it is not an injective linear map on all elements.

**Exercise 7.** Identify the incompatible requirements in Proposition 5.1.

*Solution.* Relative commutation with \(Q\), which contains \(Z\), makes the image of \(X\) fixed by \(\operatorname{Ad}(Z)\). Equivariance makes that same image negated because \(X\) is negated in the domain. Over \(\mathbb C\) these equations force zero. This contradiction uses neither a trace-factorization requirement nor failure to fix constants.

**Exercise 8.** Recover the scalar centralizing version of (19) when \(M\) is a factor.

*Solution.* If \(x\in P\cap M_\omega\), Theorem 3.1 gives \(E_\omega(x)=\tau_\omega(x)1\). Equation (19) becomes \(E_\omega(a\Phi(x))=\tau_\omega(x)E_\omega(a)\). Applying any normal state \(\varphi\) gives \(\varphi^\omega(a\Phi(x))=\tau_\omega(x)\varphi^\omega(a)\). If \(a\) is centralizing too, this is the scalar trace factorization on \(M_\omega\). For arbitrary constant \(x\) it need not hold, as (18) shows.

## References

Adrian Ocneanu, [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/1/WRAP_Theses_Ocneanu_1982.pdf), thesis, Chapter 5, Section 5.1, printed pp.49–50 (PDF pp.63–64), constructs the canonical normal expectation and its center-valued tracial restriction. Section 5.2, printed pp.50–52 (PDF pp.64–66), constructs actions from convergent automorphism families. The local proofs give the positive matrix lift, faithful-state normality and covariance estimates explicitly. The general expectation and covariance use a faithful normal state; the centralizing algebra's stated separable-predual assumption is retained.

The two Pauli tensor-tail obstructions are proved here directly. A chosen family's limit determines its action on constants, but does not determine its action on varying ultraproduct elements. Ocneanu's fast reindexing lemma in Section 5.3, printed pp.53–54 (PDF pp.67–68), uses constant lifts and an ordered expectation identity, as does the following lesson. No freely accessible source is claimed to prove the false unrestricted semi-lift or scalar-independence assertions.
