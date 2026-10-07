# A unitization that keeps its scalar quotient

*GPT-6 Sol (OpenAI), Codex writing thread, Ultra effort, September 2026. New original prose: CC0.*

Even when a \(C^*\)-algebra already has an identity, it can be useful to adjoin a *new* one. The resulting forced unitization always has a quotient onto \(\mathbb C\) whose kernel is the original algebra. That quotient detects when a continuous function of an element of \(A\) returns to \(A\), as needed for approximate identities. We use the programme's existing forced-unitization construction and give an alternative proof of its maximum norm for the C*-weight route. The required abstract self-adjoint calculus and positive-cone theorem are proved in AC1–4. The free comparison is [Blackadar, corrected author edition, II.1.2.1, printed page 54](https://bruceblackadar.com/Mathematics/Cycr.pdf). We keep the scalar coordinate in the norm so that the same construction also works for already-unital and zero algebras.

The earlier programme Banach-algebra lesson owns the forced-unitization statement. Equations (UZ.3)–(UZ.12) below give its complete local alternative proof; (UZ.2) and (UZ.14)–(UZ.15) prove the quotient-calculus and inherited-cone applications. The construction through UZ05 uses no functional calculus. Only UZ06–07 invoke AC1–4, which are proved for an already given unital C*-algebra. Thus neither unitization nor the calculus is being assumed circularly.

The programme provider is originally by Claude Opus 5.5 (Anthropic), September 2026, with its October 2026 revision and full self-check by GPT-6.1 Sol (OpenAI), Ultra, CC0. The new bridges to earlier programme lessons here are by GPT-6.1 Sol (OpenAI), Ultra, October 2026, CC0; the earlier local prose retains the credit above. The current free-source reconstruction, analytic prerequisite proof and domain checks are by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0.

For every complex \(C^*\)-algebra \(A\), including \(A=0\), we construct a unital \(C^*\)-algebra \(\widetilde A=A\oplus\mathbb C\), an isometric *-homomorphism \(j\), and a unital contractive *-homomorphism \(q\) satisfying

\[
j(a)=(a,0),\qquad q(a,\lambda)=\lambda,\qquad
\ker q=j(A).
\tag{UZ.1}
\]

The image \(j(A)\) will be a closed two-sided ideal, \(\widetilde A/j(A)\cong\mathbb C\) isometrically, and \(j(A_+)=j(A)\cap\widetilde A_+\). In particular, for self-adjoint \(a\in A\) and any continuous \(f\) on an interval containing the spectrum of \(j(a)\),

\[
q(f(j(a)))=f(0).
\tag{UZ.2}
\]

Thus \(f(j(a))\in j(A)\) whenever \(f(0)=0\). The zero is in the spectrum of \(j(a)\), since its image under the unital map \(q\) is zero.

## The algebraic extension and its left action

The following algebraic construction and norm calculation prove the programme contract in the scalar-quotient notation needed for weights.

Give \(A\oplus\mathbb C\) its vector-space operations and define

\[
\begin{aligned}
(a,\lambda)(b,\mu)&=(ab+\lambda b+\mu a,\lambda\mu),\\
(a,\lambda)^\star&=(a^*,\overline\lambda).
\end{aligned}
\tag{UZ.3}
\]

These operations have identity \({\bf1}=(0,1)\). Associativity can be checked without assuming a norm: both bracketings of a triple product have first coordinate

\[
abc+\lambda bc+\mu ac+\nu ab
+\lambda\mu c+\lambda\nu b+\mu\nu a
\]

and second coordinate \(\lambda\mu\nu\). The involution reverses products by the same expansion. Formula (UZ.3) also shows that \(j(A)\) is a two-sided ideal and that \(j,q\) preserve products and involutions.

Let \(\mathcal L(A)\) be the bounded linear operators on the Banach space \(A\). The left action and its seminorm are

\[
T_{(a,\lambda)}b=ab+\lambda b,\qquad
p(a,\lambda)=\|T_{(a,\lambda)}\|_{\mathcal L(A)}.
\tag{UZ.4}
\]

The estimate \(\|T_{(a,\lambda)}b\|\leq(\|a\|+|\lambda|)\|b\|\) proves boundedness. Expanding products gives \(T_{uv}=T_uT_v\), so \(p\) is submultiplicative. No Hilbert-space adjoint is involved in \(T_{u^\star}\); it is simply the left action of another algebra element.

For \(L_a=T_{j(a)}\),

\[
\|L_a\|=\|a\|.
\tag{UZ.5}
\]

Submultiplicativity gives the upper bound. If \(a\ne0\), test \(L_a\) on \(a^*/\|a\|\); the \(C^*\)-identity and isometry of involution give \(\|aa^*\|/\|a\|=\|a\|\). The latter isometry follows from \(\|a\|^2\leq\|a^*\|\|a\|\) and the same inequality with \(a^*\), treating zero separately. The zero algebra satisfies (UZ.5) as well.

## Checking the C*-seminorm

The next calculation proves the C*-seminorm identity directly from the C*-identity of the original algebra. The left action is on a Banach space; its involution is inherited algebraically and is not an operator adjoint on that space.

Write \(ub=T_ub\) for \(u\in A\oplus\mathbb C\) and \(b\in A\). The algebraic equality \((ub)^*(ub)=b^*(u^\star u)b\) occurs entirely in \(A\). Its \(C^*\)-identity gives

\[
\begin{aligned}
\|T_ub\|^2
&=\|b^*T_{u^\star u}b\|\\
&\leq\|b\|\|T_{u^\star u}b\|
\leq p(u^\star u)\|b\|^2.
\end{aligned}
\tag{UZ.6}
\]

Taking a supremum over unit-ball \(b\), then using \(T_{u^\star u}=T_{u^\star}T_u\), yields

\[
p(u)^2\leq p(u^\star u)\leq p(u^\star)p(u).
\tag{UZ.7}
\]

Apply this also to \(u^\star\). If one of \(p(u),p(u^\star)\) is zero, both are zero; otherwise divide to obtain \(p(u)\leq p(u^\star)\) and its reverse. The two bounds in (UZ.7) then coincide:

\[
p(u^\star)=p(u),\qquad p(u^\star u)=p(u)^2.
\tag{UZ.8}
\]

This argument uses neither a representation theorem nor an approximate identity.

## Why the scalar coordinate matters

The scalar coordinate will remove the possible kernel of the left action, including when the original algebra already has an identity.

Define

\[
N(a,\lambda)=\max\bigl(\|L_a+\lambda I_A\|,|\lambda|\bigr)
=\max\bigl(p(a,\lambda),|q(a,\lambda)|\bigr).
\tag{UZ.9}
\]

It is a seminorm by the triangle inequality. If it vanishes, \(\lambda=0\) and (UZ.5) forces \(a=0\), so it is a norm. Both terms are submultiplicative; (UZ.8) gives \(N(u^\star)=N(u)\) and

\[
\begin{aligned}
N(u^\star u)
&=\max\bigl(p(u^\star u),|q(u^\star u)|\bigr)\\
&=\max\bigl(p(u)^2,|q(u)|^2\bigr)=N(u)^2.
\end{aligned}
\tag{UZ.10}
\]

Also \(N({\bf1})=\max(\|I_A\|,1)=1\), including \(A=0\).

If \(A\) already has a unit, the formal element \((-1_A,1)\) is nonzero and acts as zero on \(A\). Its left-action seminorm is therefore zero, while \(N(-1_A,1)=1\). For \(A=\mathbb C\), the map \((a,\lambda)\mapsto(a+\lambda,\lambda)\) identifies the forced unitization with \(\mathbb C\oplus\mathbb C\) and gives \(N(a,\lambda)=\max(|a+\lambda|,|\lambda|)\). The extra scalar coordinate is visible even in this smallest example.

## Completeness, ideal and quotient norm

From the definition of \(T\),

\[
N(a,\lambda)\leq\|a\|+|\lambda|.
\tag{UZ.11}
\]

Conversely, \(|\lambda|\leq N(a,\lambda)\), and (UZ.5) gives
\(\|a\|=\|L_a\|\leq p(a,\lambda)+|\lambda|\|I_A\|\leq2N(a,\lambda)\).
Hence

\[
\|a\|+|\lambda|\leq3N(a,\lambda).
\tag{UZ.12}
\]

The sum norm on \(A\oplus\mathbb C\) is complete because both coordinates are complete. The two inequalities show that an \(N\)-Cauchy sequence converges in the sum norm and hence in \(N\). Therefore \((A\oplus\mathbb C,N)\) is a unital \(C^*\)-algebra.

Equation (UZ.5) makes \(j\) isometric. Its image is closed by completeness and is the ideal already identified algebraically. The inequality \(|q(u)|\leq N(u)\), with equality at \({\bf1}\), makes \(q\) contractive of norm one. Every element with scalar coordinate \(\lambda\) has norm at least \(|\lambda|\); the representative \((0,\lambda)\) has norm exactly \(|\lambda|\). Thus the quotient norm of its coset is \(|\lambda|\), proving the asserted isometric quotient.

## Continuous functions and the quotient

We now apply the self-adjoint continuous calculus proved in AC1–4 to the constructed unital \(C^*\)-algebra. If \(h=h^\star\), then \(q(h)\) is real and lies in \(\sigma_{\widetilde A}(h)\): otherwise an inverse for \(h-q(h){\bf1}\) would map under \(q\) to an inverse for zero.

Take a compact real interval \(J\) containing the spectrum and a continuous \(f:J\to\mathbb C\). Polynomial approximation on \(J\) can be seen directly from Bernstein polynomials. After rescaling to \([0,1]\), for real continuous \(g\) put

\[
B_ng(t)=\sum_{k=0}^n g(k/n){n\choose k}t^k(1-t)^{n-k}.
\]

The binomial weights sum to one, have weighted mean \(k/n=t\), and variance \(t(1-t)/n\). Their mass outside \(|k/n-t|<\delta\) is at most \(1/(4n\delta^2)\). Uniform continuity then gives, whenever \(|g(s)-g(t)|<\eta\) for \(|s-t|<\delta\),

\[
\sup_t|B_ng(t)-g(t)|
\leq\eta+\frac{\|g\|_\infty}{2n\delta^2}.
\tag{UZ.13}
\]

Send \(n\) to infinity and then \(\eta\) to zero; approximate the real and imaginary parts separately. A singleton interval uses only a constant polynomial.

Choose resulting polynomials \(P_n\to f\) uniformly on \(J\). Since \(q\) is unital and multiplicative,
\(q(P_n(h))=P_n(q(h))\).
Continuity of \(q\) and isometry of functional calculus pass to the limit, giving

\[
q(f(h))=f(q(h)).
\tag{UZ.14}
\]

For \(h=j(a)\) with \(a=a^*\), this is (UZ.2). If \(f(0)=0\), the result lies in \(\ker q=j(A)\). For positive \(j(a)\), the functions \(t/(t+\varepsilon)\), \(\sqrt{t/(t+\varepsilon)}\), and \(\sqrt t\) therefore return elements of \(j(A)\). The inverse \((j(a)+\varepsilon{\bf1})^{-1}\) need not itself lie there.

## The inherited positive cone

Use \(A_+=\{b^*b:b\in A\}\). If \(a=b^*b\), then \(j(a)=j(b)^\star j(b)\geq0\) in \(\widetilde A\). Conversely, suppose \(j(a)\geq0\) there. Its positive square root \(c\) exists by the unital functional calculus. Formula (UZ.14) gives \(q(c)=\sqrt{q(j(a))}=0\), so \(c=j(b)\) for some \(b\in A\). Now
\(j(a)=c^\star c=j(b^*b)\), and injectivity of \(j\) yields \(a=b^*b\). Therefore

\[
j(A_+)=j(A)\cap\widetilde A_+.
\tag{UZ.15}
\]

Order comparisons among self-adjoint elements of \(A\) agree with those in \(\widetilde A\), and their norms agree by (UZ.5). The approximate-identity calculation can therefore use the forced unitization without changing either the original order or the original norm.

## References

- Bruce Blackadar, [*Operator Algebras*, corrected author edition of 8 February 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf), II.1.2.1 (unitization), II.2.3.1–2 and II.3.1.1–5 (calculus and order), printed pages 54 and 63–66. The local proofs above and AC1–4 supply the arguments; the reference does not replace them.
