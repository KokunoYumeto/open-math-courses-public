# Laplace resolvents of the weak-star generator

The generator of a uniformly bounded real-parameter action can be unbounded and only weak-star closed. Its resolvents still exist throughout both open half-planes, given by forward and backward Laplace integrals. This lesson proves Takesaki II, Lemma XI.1.19 with both inverse identities on the correct domains. The backward formula needs a minus sign under the convention of [the earlier generator proof](OA-FLOW-L94.md#oa-flow.gen.domain).

*Programme proof written in Codex (OpenAI), September 2026; restoration and proof expansion, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

The earlier proofs are [BS0–1](OA-FLOW-BS.md#bs-0) for specified preadjoints and complete integrated maps, [L24 Proposition4.1](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) for Banach-valued integration, [CF1](OA-FLOW-CF.md#oa-flow.cf.1) for oriented fundamental calculus, and the earlier generator's [full domain](OA-FLOW-L94.md#oa-flow.gen.domain), [closed graph](OA-FLOW-L94.md#oa-flow.gen.closed) and [invariance](OA-FLOW-L94.md#oa-flow.gen.invariant). Here \(dt\) is Lebesgue measure with \(\int_0^s1\,dt=s\) as an oriented integral.

<a id="oa-flow.res.twist"></a><a id="OA-FLOW.RES.TWIST"></a>

## Scalar twists shift the generator

Retain \(X=X_*^*\), the uniformly bounded weak-star continuous action \(\alpha:\mathbb R\to\operatorname{GL}(X)\), and its weak-star generator \(\delta\) from lesson 94. For real \(b\), define \(\alpha_t^{(b)}=e^{ibt}\alpha_t\). This is another action with the same uniform bound and predual continuity. The scalar product rule in (G2) gives

<a id="equation-l1"></a>

$$D(\delta^{(b)})=D(\delta),\qquad
\delta^{(b)}x=\delta x+ibx.\tag{L1}$$

Thus an imaginary shift of the spectral parameter can be absorbed into an action. We will prove the stronger direct claim that every complex \(\lambda\) with nonzero real part is resolvent, without first restricting \(\lambda\) to the real axis.

<a id="oa-flow.res.forward"></a><a id="OA-FLOW.RES.FORWARD"></a>

## The forward Laplace operator

For \(\operatorname{Re}\lambda>0\), define, through the specified predual,

<a id="equation-l2"></a>

$$R_\lambda^+x=\int_0^\infty e^{-\lambda t}\alpha_t x\,dt,
\qquad\|R_\lambda^+\|\le\frac{C_\alpha}{\operatorname{Re}\lambda}.\tag{L2}$$

The integral is a weak-star integral: on \(X_*\), the norm-convergent Bochner integral \(\int_0^\infty e^{-\lambda t}\beta_t\phi\,dt\) is its preadjoint. Indeed \(1_{[0,\infty)}(t)e^{-\lambda t}\) is in \(L^1(\mathbb R)\), and the predual orbit is norm continuous and bounded by \(C_\alpha\|\phi\|\); the complete integral proof of BS1/L24 applies. Its norm bound is the integral of \(C_\alpha e^{-\operatorname{Re}\lambda t}\). BS0 proves that its adjoint is normal, with the same norm. For real \(s\), with oriented integration when \(s<0\), the group law yields

<a id="equation-l3"></a>

$$\alpha_sR_\lambda^+x
=e^{\lambda s}R_\lambda^+x
-e^{\lambda s}\int_0^s e^{-\lambda u}\alpha_u x\,du.\tag{L3}$$

Take the weak-star derivative at \(s=0\). The last integral divided by \(s\) tends weak-star to \(x\), while the first term has derivative \(\lambda R_\lambda^+x\). Hence \(R_\lambda^+x\in D(\delta)\) and

<a id="equation-l4"></a>

$$(\lambda I-\delta)R_\lambda^+x=x\qquad(x\in X).\tag{L4}$$

For the other inverse identity, let \(x\in D(\delta)\). Domain invariance (G10) and scalar differentiation give

<a id="equation-l5"></a>

$$\frac{d}{dt}\big(e^{-\lambda t}\alpha_t x\big)
=-e^{-\lambda t}\alpha_t(\lambda I-\delta)x
\quad\text{in the weak-star sense}.\tag{L5}$$

Pair with an arbitrary predual functional and integrate from zero to \(T\). The boundary term \(e^{-\lambda T}\alpha_Tx\) tends to zero in norm by uniform boundedness and \(\operatorname{Re}\lambda>0\). Letting \(T\to\infty\) gives

<a id="equation-l6"></a>

$$R_\lambda^+(\lambda I-\delta)x=x\qquad(x\in D(\delta)).\tag{L6}$$

Equations (L4) and (L6) show that \(\lambda I-\delta:D(\delta)\to X\) is bijective with bounded, normal, everywhere-defined inverse \(R_\lambda^+\).

<a id="oa-flow.res.backward"></a><a id="OA-FLOW.RES.BACKWARD"></a>

## The backward Laplace operator and its sign

For \(\operatorname{Re}\lambda<0\), apply the preceding argument to the reversed action \(t\mapsto\alpha_{-t}\), whose generator is \(-\delta\), with positive parameter \(-\lambda\). The inverse of \(\delta-\lambda I\) is \(\int_0^\infty e^{\lambda t}\alpha_{-t}\,dt\). Therefore the inverse of \(\lambda I-\delta\) is its negative:

<a id="equation-l7"></a>

$$R_\lambda^-x
:=-\int_0^\infty e^{\lambda t}\alpha_{-t}x\,dt,
\qquad\|R_\lambda^-\|\le\frac{C_\alpha}{|\operatorname{Re}\lambda|}.\tag{L7}$$

It is a normal weak-star integral and satisfies the two domain-sensitive identities

<a id="equation-l8"></a>

$$(\lambda I-\delta)R_\lambda^-x=x\quad(x\in X),
\qquad R_\lambda^-(\lambda I-\delta)x=x\quad(x\in D(\delta)).\tag{L8}$$

The initial minus sign in (L7) is necessary. For the trivial action \(\alpha_t=I\), the generator is \(\delta=0\); then the integral *without* the minus sign equals \(-1/\lambda\), whereas the inverse of \(\lambda I\) is \(1/\lambda\). This small model detects the sign before any unbounded-domain argument is used.

<a id="oa-flow.res.imaginary"></a><a id="OA-FLOW.RES.IMAGINARY"></a>

## The spectrum lies on the imaginary axis

For a closed operator, \(\lambda\) belongs to the resolvent set when \(\lambda I-\delta:D(\delta)\to X\) has a bounded everywhere-defined inverse. Lessons 94 and (L2)–(L8) establish precisely that for every \(\lambda\) off the imaginary axis. Thus

<a id="equation-l9"></a>

$$\operatorname{Sp}(\delta)\subset i\mathbb R.\tag{L9}$$

The estimates also give \(\|(\lambda I-\delta)^{-1}\|\le C_\alpha/|\operatorname{Re}\lambda|\) on both half-planes. They do not assert that every point of the imaginary axis is spectral, nor that the generator is bounded or norm densely defined on \(X\).

**Problem.** Let \(\alpha_tz=e^{i\omega t}z\) on \(\mathbb C\). Compute \(R_\lambda^+\) and \(R_\lambda^-\) and compare them with the algebraic inverse.

**Solution.** The generator is multiplication by \(i\omega\). For \(\operatorname{Re}\lambda>0\), \(\int_0^\infty e^{-(\lambda-i\omega)t}dt=(\lambda-i\omega)^{-1}\). For \(\operatorname{Re}\lambda<0\), \(-\int_0^\infty e^{(\lambda-i\omega)t}dt=(\lambda-i\omega)^{-1}\) as well. Both agree with \((\lambda I-\delta)^{-1}\). \(\square\)

The mathematical source is M. Takesaki, *Theory of Operator Algebras II*, Lemma XI.1.19, printed pages 325–326 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The backward display on page326 needs the minus sign for the convention \((\lambda I-\delta)^{-1}\); the trivial-action test and the full reversed-action proof (L7)–(L8) establish it. The proof above retains both inverse identities at their exact domains and supplies all integral and earlier generator inputs.
