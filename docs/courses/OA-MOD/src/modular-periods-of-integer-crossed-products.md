# Modular periods of integer crossed products

Fourier coefficients detect both the center of an integer crossed product and every unitary that normalizes its coefficient factor. Applied to a modular group, this gives an exact test for an inner modular time. We then use the test to separate two obstructions in the type III classification argument: a nontrivial weight-scaling phase and a finite return modulo modular automorphisms.

The normalization throughout is \(VxV^*=\alpha(x)\) and counting measure on \(\mathbb Z\). With this convention, \(\varphi\alpha=\mu\varphi\) produces the phase \(\mu^{it}\), with a positive exponent.

## 1. Conventions and the earlier constructions

Let \(M\ne0\) be a factor and \(\alpha\) a normal automorphism. Form


\[
 N=M\rtimes_\alpha\mathbb Z,\qquad VxV^*=\alpha(x).
 \tag{MPR.1}
\]


The normal regular construction and its independence of a faithful initial representation are proved in NR3–NR4. On \(\ell^2(\mathbb Z;H)\), for a faithful normal representation \(\rho\) of \(M\), its generators are


\[
 [\pi(x)\xi]_j=\rho(\alpha^{-j}(x))\xi_j,\qquad
 [V\xi]_j=\xi_{j-1}.
 \tag{MPR.2}
\]


We identify \(\pi(M)\) with \(M\). The complete compression proof in GDA13 gives the faithful normal coefficient expectation \(E:N\to M\). For \(X\in N\), write


\[
 X_k=E(XV^{-k}).
 \tag{MPR.3}
\]


Matrix compression in (MPR.2) gives, first on polynomials and then everywhere by normality,


\[
 I_i^*XI_j=\rho\!\left(\alpha^{-i}(X_{i-j})\right).
 \tag{MPR.4}
\]


Thus the coefficients determine \(X\): vanishing of all of them makes all its matrix entries zero. No convergence of a formal Fourier series is assumed. Polar decomposition, used below on a bounded intertwiner, is constructed in BK07.

When a faithful normal semifinite weight \(\varphi\) is specified, put \(\psi=\varphi E\). GDW6–GDW7 and GDA8, GDA13 prove that this is the actual faithful normal semifinite dual weight on the entire positive cone and compute its modular generators. BC4–BC5 prove the normalized cocycle, scalar and covariance identities. The faithful weight may be infinite. Neither separable predual nor approximate finite dimensionality is required by Sections 1–7.

For a factor \(A\) with a faithful normal semifinite weight \(\omega\), use


\[
 T(A)=\{t\in\mathbb R:\sigma_t^\omega\text{ is inner}\}.
 \tag{MPR.5}
\]


This is an additive subgroup, since AQ01 proves that the inner automorphisms form a normal subgroup of the automorphism group. It is independent of \(\omega\): BC4 gives
\(\sigma_t^\nu=\operatorname{Ad}((D\nu:D\omega)_t)\sigma_t^\omega\).
In contrast, write
\(\operatorname{Per}(\varphi)=\{t:\sigma_t^\varphi=\mathrm{id}\}\)
for the actual period group of the specified weight.

## 2. Factoriality excludes every inner power

**Proposition 2.1.** The algebra \(N\) is a factor if and only if every nonzero power of \(\alpha\) is outer. In that case


\[
 M'\cap N=\mathbb C1.
 \tag{MPR.6}
\]


First suppose \(\alpha^p=\operatorname{Ad}v\), with \(p\ge1\) and \(v\) unitary. Commutation of \(\alpha\) with its \(p\)-th power gives
\(\operatorname{Ad}\alpha(v)=\operatorname{Ad}v\).
Since \(M\) is a factor, \(\alpha(v)=cv\) for a scalar \(c\in\mathbb T\). Also
\(\alpha^p(v)=v\), hence \(c^p=1\). Consequently


\[
 Z=v^pV^{-p^2}
 \tag{MPR.7}
\]


commutes with \(M\): \(\operatorname{Ad}(v^p)=\alpha^{p^2}\), which cancels the action of \(V^{-p^2}\). It commutes with \(V\) because \(\alpha(v^p)=v^p\). Thus \(Z\in Z(N)\). But \(Z\) is a unitary of nonzero Fourier degree and \(E(Z)=0\), so it cannot be scalar. This proves the necessary direction, including a power whose implementing unitary is fixed only up to a root of unity.

For the converse, let \(X\in M'\cap N\). Bimodularity and covariance give


\[
 aX_k=X_k\alpha^k(a)\qquad(a\in M).
 \tag{MPR.8}
\]


If \(X_k\ne0\), the two intertwiner identities imply that \(X_kX_k^*\) and \(X_k^*X_k\) commute with \(M\). They are positive scalars. The nonzero polar part is therefore a unitary: both support projections are \(1\), and the two positive scalars are the same by polar decomposition. It follows that \(\alpha^k\) is inner. Under the hypothesis of the proposition this forces \(k=0\); then (MPR.8) says \(X_0\) is scalar. Fourier uniqueness from (MPR.4) gives (MPR.6). The center of \(N\) is contained in this relative commutant, proving factoriality. \(\square\)

The proof uses factoriality of \(M\) at the polar-decomposition step. An arbitrary action on an algebra with center does not satisfy this criterion.

## 3. Every normalizing unitary has one Fourier degree

Assume henceforth that \(N\) is a factor. Thus all the nonzero powers of \(\alpha\) are outer.

**Theorem 3.1.** If \(W\in\mathcal U(N)\) and \(WMW^*=M\), then there are unique \(k\in\mathbb Z\) and \(v\in\mathcal U(M)\) such that


\[
 W=vV^k.
 \tag{MPR.9}
\]


In particular, its action on the coefficient factor is
\(\operatorname{Ad}v\circ\alpha^k\).

To prove the theorem, set \(\beta=\operatorname{Ad}W|_M\). The identity \(\beta(a)W=Wa\) gives


\[
 \beta(a)W_k=W_k\alpha^k(a).
 \tag{MPR.10}
\]


Some \(W_k\) is nonzero, by Fourier uniqueness. The same polar argument as in Section 2, now between the two surjective factor representations \(\beta(M)\) and \(\alpha^k(M)\), writes \(W_k=dv\) with \(d>0\) and \(v\) unitary. Hence \(\beta=\operatorname{Ad}v\circ\alpha^k\).

A second nonzero coefficient at degree \(l\) would imply that \(\alpha^k\) and \(\alpha^l\) differ by an inner automorphism. Then \(\alpha^{k-l}\) would be inner, forcing \(k=l\). Thus \(W\) has exactly one nonzero coefficient. Equation (MPR.4) identifies \(W=dvV^k\). Unitarity gives \(d=1\), proving (MPR.9) and both uniqueness assertions.

For two such normalizers,


\[
 (vV^k)(wV^l)=v\alpha^k(w)V^{k+l}.
 \tag{MPR.11}
\]


Thus their degree is a homomorphism onto \(\mathbb Z\), with kernel precisely \(\mathcal U(M)\). This describes actual unitaries, without choosing representatives in an outer automorphism quotient.

## 4. The normalized dual-weight phase

Let \(\varphi\) be any faithful normal semifinite weight on \(M\). Write


\[
 c_t=(D(\varphi\circ\alpha):D\varphi)_t,\qquad
 \psi=\varphi E.
 \tag{MPR.12}
\]


The complete modular generator calculation in GDW7, together with the whole-cone identification GDA8 and the counting-measure normalization GDA13, gives


\[
 \begin{aligned}
 \sigma_t^\psi(x)&=\sigma_t^\varphi(x)\quad(x\in M),\\
 \sigma_t^\psi(V)&=Vc_t=\alpha(c_t)V.
 \end{aligned}
 \tag{MPR.13}
\]


The cocycle lies on the right in the first expression for the second line. Moving it to the left applies \(\alpha\); it does not take its adjoint.

If, on the entire positive cone,


\[
 \varphi\circ\alpha=\mu\varphi,\qquad \mu>0,
 \tag{MPR.14}
\]


then BC5's scalar normalization gives \(c_t=\mu^{it}1\). Hence


\[
 \sigma_t^\psi(V)=\mu^{it}V.
 \tag{MPR.15}
\]


Here and below \(\mu^{it}=\exp(it\log\mu)\), with the real logarithm. A hypothesis written instead as \(\varphi\circ\alpha^{-1}=\mu\varphi\) would give \(\varphi\alpha=\mu^{-1}\varphi\) and therefore the phase \(\mu^{-it}\). These are different hypotheses.

We will also use the exact inner-derivative identity proved in GDA8, equation GDA34:


\[
 (D(\varphi\circ\operatorname{Ad}u):D\varphi)_t
       =u^*\sigma_t^\varphi(u).
 \tag{MPR.16}
\]


If \(\varphi\circ\operatorname{Ad}u=\varphi\), BC4's identical-weight normalization makes the left side \(1\). Thus \(u\) belongs to the centralizer
\(M_\varphi=\{x:\sigma_t^\varphi(x)=x\text{ for all }t\}\).
This conclusion uses equality of weights, including their normalization, rather than only equality of modular automorphism groups.

## 5. An exact criterion for every inner modular time

**Theorem 5.1.** Under the factorial crossing hypothesis, \(t\in T(N)\) if and only if there are \(k\in\mathbb Z\) and \(v\in\mathcal U(M)\) such that


\[
 \begin{aligned}
 \sigma_t^\varphi&=\operatorname{Ad}v\circ\alpha^k,\\
 v\alpha(v^*)&=\alpha(c_t).
 \end{aligned}
 \tag{MPR.17}
\]


When these conditions hold, \(vV^k\) implements \(\sigma_t^\psi\). The integer \(k\) is unique, and \(v\) is unique up to a scalar of modulus one.

If \(t\in T(N)\), choose a unitary implementer \(W\). Formula (MPR.13) shows that it normalizes \(M\). Theorem 3.1 gives \(W=vV^k\), and restriction to \(M\) yields the first line of (MPR.17). On the crossing unitary,


\[
 (vV^k)V(vV^k)^*=v\alpha(v^*)V.
 \tag{MPR.18}
\]


Comparison with (MPR.13) gives the second line. Conversely, (MPR.17) and (MPR.18) make the two normal automorphisms equal on both generating families of \(N\), hence everywhere. Uniqueness of the degree follows as in Theorem 3.1; two unitary implementers of the same automorphism of the factor \(N\) differ by a scalar. \(\square\)

For completeness, the associated degree map


\[
 d_\varphi:T(N)\longrightarrow\mathbb Z
 \tag{MPR.19}
\]


is an additive homomorphism. If \(W_t,W_s\) implement the modular automorphisms at times \(t,s\), then \(W_tW_s\) implements the one at \(t+s\). Equation (MPR.11) adds the degrees. Moreover


\[
 \ker d_\varphi=T(N)\cap T(M).
 \tag{MPR.20}
\]


Degree zero makes the restriction inner. Conversely, if that restriction is inner, the first line of (MPR.17) and outerness of all nonzero powers force \(k=0\). No continuity of this integer-valued map is asserted or needed.

## 6. Actual periods detect a scaling obstruction

Assume (MPR.14). At every \(t\in\operatorname{Per}(\varphi)\), an inner implementer of \(\sigma_t^\psi\) must commute with \(M\). Proposition 2.1 makes it scalar. Hence \(\sigma_t^\psi\) must be the identity. Conversely, (MPR.13)–(MPR.15) make it the identity whenever \(\mu^{it}=1\). Therefore


\[
 T(N)\cap\operatorname{Per}(\varphi)
   =\{t\in\operatorname{Per}(\varphi):t\log\mu\in2\pi\mathbb Z\}.
 \tag{MPR.21}
\]


In particular, if \(P>0\) and \(\sigma_P^\varphi=\mathrm{id}\), then


\[
 T(N)\cap P\mathbb Z
   =\{nP:nP\log\mu\in2\pi\mathbb Z\}.
 \tag{MPR.22}
\]


This remains valid when \(P\) is a nonfundamental period of the weight.

Put \(L=2\pi/P\) and \(\lambda=e^{-L}\). If \(P\in T(N)\), (MPR.22) forces \(\mu\in\lambda^{\mathbb Z}\). If a representative has additionally been normalized so that \(\lambda<\mu\le1\), it follows that \(\mu=1\). The half-open interval matters: the excluded endpoint \(\lambda\) has the same phase as \(1\).

This is the weight-scaling obstruction in the type \(\mathrm{III}_\lambda\) crossing argument. Using it for an arbitrary automorphism requires an actual proof that an inner perturbation admits the specified periodic weight normalization. Formula (MPR.22) proves the obstruction for every such normalization; it does not supply the existence of one.

## 7. A finite modular return creates a new inner time

Assume now that \(\varphi\alpha=\varphi\). Suppose that, for \(p\ge1\), \(s\in\mathbb R\) and \(u\in\mathcal U(M)\),


\[
 \alpha^p=\operatorname{Ad}u\circ\sigma_s^\varphi.
 \tag{MPR.23}
\]


**Theorem 7.1.** There is a unitary


\[
 W=u^{-p}V^{p^2}
 \tag{MPR.24}
\]


such that


\[
 \operatorname{Ad}W=\sigma_{ps}^\psi.
 \tag{MPR.25}
\]


Consequently \(ps\in T(N)\), \(d_\varphi(ps)=p^2\), and \(ps\notin\operatorname{Per}(\varphi)\).

Here is the full phase calculation. Since both \(\alpha\) and \(\sigma^\varphi\) preserve \(\varphi\), (MPR.23) implies \(\varphi\operatorname{Ad}u=\varphi\): compose its weight identity with \(\sigma_{-s}^\varphi\). Equation (MPR.16) makes \(u\in M_\varphi\). Also \(\alpha\) commutes with the modular group, by normal-isomorphism covariance and \(\varphi\alpha=\varphi\).

Conjugate (MPR.23) by \(\alpha\). Commutation with \(\sigma_s^\varphi\) shows that \(\operatorname{Ad}\alpha(u)=\operatorname{Ad}u\); hence \(\alpha(u)=cu\) for \(c\in\mathbb T\). Evaluating (MPR.23) at \(u\) gives \(\alpha^p(u)=u\), because \(\sigma_s^\varphi(u)=u\). Thus \(c^p=1\) and \(\alpha(u^p)=u^p\).

Since \(\sigma_s^\varphi\) fixes \(u\), taking the \(p\)-th power in (MPR.23) gives


\[
 \alpha^{p^2}=\operatorname{Ad}(u^p)\circ\sigma_{ps}^\varphi.
 \tag{MPR.26}
\]


Equations (MPR.24) and (MPR.26) show that \(\operatorname{Ad}W\) agrees with \(\sigma_{ps}^\varphi\) on \(M\). Also


\[
 WVW^*=u^{-p}\alpha(u^p)V=V.
 \tag{MPR.27}
\]


The preserved-weight case of (MPR.13) fixes \(V\), so these two generator calculations prove (MPR.25). The displayed implementer has Fourier degree \(p^2\); Theorem 5.1 gives the stated value of \(d_\varphi\).

If \(ps\) were an actual period of \(\varphi\), then \(W\) would commute with \(M\), contrary to (MPR.6) and its nonzero degree. Equivalently, (MPR.26) would make the nonzero power \(\alpha^{p^2}\) inner. This proves the last assertion. \(\square\)

**Corollary 7.2.** If \(\varphi\alpha=\varphi\) and


\[
 T(N)\subseteq\operatorname{Per}(\varphi),
 \tag{MPR.28}
\]


then no positive power of \(\alpha\) is an inner perturbation of a modular automorphism of \(\varphi\). Indeed (MPR.25) and the last assertion of Theorem 7.1 would contradict (MPR.28).

For a factor with separable predual, suppose one has also proved the structural statement


\[
 \operatorname{Cnt}(M)\subseteq
 \{\operatorname{Ad}u\circ\sigma_s^\varphi:
                   u\in\mathcal U(M),\ s\in\mathbb R\}.
 \tag{MPR.29}
\]


Here \(\operatorname{Cnt}(M)\) denotes the automorphisms acting trivially, up to strong* null differences, on every bounded sequence centralizing the entire predual. Corollary 7.2 then implies \(p_a(\alpha)=0\): a finite asymptotic period would put a positive power in (MPR.29), which was just excluded. This is a consequence with (MPR.29) as an explicit hypothesis, not a proof of that classification of centrally trivial automorphisms.

## 8. Solved phase and hypothesis checks

**A phase of order three.** Suppose \(\sigma_P^\varphi=\mathrm{id}\), let \(L=2\pi/P\), and suppose \(\varphi\alpha=e^{-L/3}\varphi\) in a factorial crossing. What does the actual-period test say?

**Solution.** Formula (MPR.15) gives
\(\sigma_P^\psi(V)=e^{-2\pi i/3}V\).
Thus \(P\notin T(N)\). More generally
\(e^{-2\pi in/3}=1\) exactly when \(3\) divides \(n\), so (MPR.22) gives
\(T(N)\cap P\mathbb Z=3P\mathbb Z\).
Using the inverse scaling hypothesis instead would conjugate the phase. It would not change its order, which explains why an incorrect sign can escape this particular subgroup test.

**A nontracial coefficient need not commute with the crossing unitary.** Put \(M=M_2(\mathbb C)\), \(\varphi(x)=\operatorname{Tr}(hx)\), \(h=\operatorname{diag}(1,2)\), and let \(a\) be the flip matrix. Take \(\alpha=\operatorname{Ad}a\). Check the order of factors in (MPR.13) at \(t=\pi/(2\log2)\).

**Solution.** The elementary density formula \(\sigma_t^\varphi(x)=h^{it}xh^{-it}\), proved in FS10, gives
\(h^{it}=\operatorname{diag}(1,i)\).
Equation (MPR.16) gives


\[
 c_t=a^*\sigma_t^\varphi(a)=\operatorname{diag}(i,-i),
 \qquad
 \alpha(c_t)=\operatorname{diag}(-i,i)\ne c_t.
 \tag{MPR.30}
\]


Thus \(Vc_t=\alpha(c_t)V\), and replacing this by \(c_tV\) is wrong. The dual-weight formula applies, although the crossing here is not a factor: \(\alpha\) is inner, and Proposition 2.1 gives the nonscalar central unitary \(aV^{-1}\). This example tests the generator formula, not the factorial hypotheses of Theorem 5.1.

**Why the exponent is squared.** In (MPR.23), why does the proof use \(p^2\), rather than simply \(p\)?

**Solution.** The unitary \(u^{-1}V^p\) acts on \(M\) as \(\sigma_s^\varphi\), but its action on \(V\) is \(cV\), where \(\alpha(u)=cu\). Weight preservation gives \(c^p=1\), not necessarily \(c=1\). Raising to the \(p\)-th power removes this phase; since \(\alpha^p(u)=u\), that power is exactly \(u^{-p}V^{p^2}\). The resulting modular time is \(ps\).

**Changing an inner representative.** Let \(\alpha'=\operatorname{Ad}b\circ\alpha\). The normal isomorphism proved in AC07 sends \(x\) to \(x\) and \(V\) to \(b^*V'\). Its expectation identity gives \(E'\Phi=E\), hence
\((\varphi E')\Phi=\varphi E\) on the full positive cone. Modular covariance therefore transports the inner-time group. The identity does not imply \(\varphi\alpha'=\varphi\alpha\); any weight normalization for the new representative must still be proved.

## Source

The classical application motivating Sections 2, 6 and 7 is Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Theorem 4.18(i), printed pages 390–391, especially its proof on page 391. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The present arguments are independently written. The full normalizer and inner-time criteria above make explicit the Fourier mechanism used in that application. The source's proof displays both signs for the same scaled-weight phase; (MPR.13)–(MPR.15) fix the convention through the normalized dual-weight theorem.
