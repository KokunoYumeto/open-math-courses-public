# Bounded-derivative operators: the complete AN-03 estimate

This modified selection retains AN03-EUC-006, equations E23–E27 and the complete packet proof, from *Euclidean symbol calculus*. Original principal author and publisher: AN-03 course-writing task / AN-03 local course project, 2026. Earlier modifications: AN-03 course-writing task and OpenAI Codex. Selection and exact prerequisite bindings: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## B0. Exact prerequisites

The complete [Fourier proof L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) supplies Schwartz inversion, both \(L^2\) extensions and Plancherel. The [measure proof M0–M8](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) supplies Tonelli, Cauchy–Schwarz, completeness and compact smooth density. [B3](../20261004-free-intrinsic-graph/prerequisites/dyadic-endpoint.md) proves Schur's estimate, repeated below. The [measurable vector integral proof](../20261005-restored-corank-continuity/corank-geometry-and-sufficient-continuity.md) constructs the Hilbert-valued integrals used in synthesis. The [Hilbert facts T1](../20261004-free-canonical-composition/compactness-and-essential-norms.md) supply polarization and adjoints. Every dependency is bound in the [proof map](proof-map.json).

Use the inner product linear in the first variable and \(\operatorname{Op}(a)u(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi\). References to (E10) in the retained proof mean this quantization formula. A normalized nonzero compact smooth bump is one possible fixed Schwartz packet. Its normalization uses its positive finite \(L^2\) norm. Smooth compact functions of the \(2n\) packet variables are dense in their \(L^2\) space. On a compact parameter set, \(Q\mapsto\phi_Q\) is norm-continuous in \(L^2\), by dominated convergence for its smooth translations and modulations. Thus synthesis of a bounded compact measurable scalar function is an actual strongly measurable vector integral with integrable norm. The cited vector-integral proof constructs it, and the bound below extends it to all \(L^2\) packet coefficients. Exhausting parameter space by compact sets justifies the same integral on Schwartz coefficients.

## AN03-EUC-006 — A finite-derivative \(L^2\) estimate

We first prove an estimate that involves no symbol order. Suppose \(a(x,\xi)\) is smooth and all derivatives up to a sufficiently large fixed order are bounded. Then
\[
\|\operatorname{Op}(a)u\|_2\leq C_n M\|u\|_2,
\qquad
M=\max_{|\alpha|+|\beta|\leq L_n}
\|\partial_\xi^\alpha\partial_x^\beta a\|_\infty.
\tag{E23}
\]
The number \(L_n\) is finite; the proof permits \(L_n=4N\) for any integer \(N>n/2\). Only this estimate, not an optimal derivative count, is needed.

We record the integral estimate used in its proof. If a measurable kernel \(K(s,t)\) on any two copies of a measure space satisfies
\(\sup_t\int|K(s,t)|\,ds\leq A\) and
\(\sup_s\int|K(s,t)|\,dt\leq B\), then its operator has \(L^2\) norm at most \(\sqrt{AB}\). In fact,
\[
\left|\int K(s,t)u(t)\,dt\right|^2
\leq\left(\int|K(s,t)|\,dt\right)
\left(\int|K(s,t)||u(t)|^2\,dt\right).
\tag{E24}
\]
Integration in \(s\) and Tonelli's theorem give \(AB\|u\|_2^2\). Truncation first handles any existence issue, and the estimate supplies the extension. This includes continuous kernels with equal marginal bound \(A=B=C\) and norm at most \(C\).

**Proof of (E23).** Fix \(\phi\in\mathcal S(\mathbb R^n)\) with \(\|\phi\|_2=1\), and put
\(\phi_{q,p}(x)=e^{ip\cdot x}\phi(x-q)\).
Use phase-space measure \(d\mu(q,p)=(2\pi)^{-n}dq\,dp\). The packet transform
\(Vu(q,p)=(u,\phi_{q,p})\) is an isometry from \(L^2\) into \(L^2(d\mu)\): Plancherel in \(p\), followed by integration in \(q\), gives
\[
\int|Vu(q,p)|^2d\mu(q,p)
=\iint |u(x)|^2|\phi(x-q)|^2\,dx\,dq=\|u\|_2^2.
\tag{E25}
\]
The synthesis map \(V^*f=\int f(Q)\phi_Q\,d\mu(Q)\), initially for bounded compactly supported \(f\), has norm at most one: pairing with an \(L^2\) function, applying Cauchy–Schwarz and (E25), and taking the supremum over unit vectors proves this bound. Completeness extends synthesis to every \(f\in L^2(d\mu)\). Polarization of (E25) gives \(V^*V=I\). For Schwartz \(u\), \(Vu\) decreases rapidly in both packet variables; integration by parts in \(x\) controls the momentum variable and the product of two Schwartz functions controls the position variable. Thus the reconstruction \(u=\int Vu(Q)\phi_Q\,d\mu(Q)\) converges in \(\mathcal S\).

Consider the matrix of \(A=\operatorname{Op}(a)\) between two packets, with output packet \((q,p)\) and input packet \((q',p')\). Substitute \(x=q+s\), \(\xi=p'+t\) in (E10). Apart from a factor of absolute value one it is
\[
(2\pi)^{-n}\iint
e^{i[s\cdot(p'-p)+t\cdot(q-q')]}
e^{is\cdot t}a(q+s,p'+t)\widehat\phi(t)\overline{\phi(s)},ds\,dt.
\tag{E26}
\]
Apply \((1-\Delta_s)^N(1-\Delta_t)^N\) to the last three factors by integration by parts. Derivatives of \(e^{is\cdot t}\) create only polynomials in \(s,t\); derivatives of the two fixed Schwartz functions absorb those polynomials. Consequently the absolute integral of all differentiated amplitudes is bounded by \(C_{n,N,\phi}M\), uniformly in all four packet parameters. The derivative order of \(a\) is at most \(4N\). We obtain
\[
|(A\phi_{q',p'},\phi_{q,p})|
\leq CM\langle q-q'\rangle^{-2N}
\langle p-p'\rangle^{-2N}.
\tag{E27}
\]
Since \(2N>n\), both phase-space marginals are integrable and uniformly bounded by \(CM\). Equation (E24) bounds the corresponding operator \(\mathcal M\) on \(L^2(d\mu)\). The zeroth bound on \(a\) already makes (E10) a continuous map \(\mathcal S\to\mathcal S'\), since its outputs are bounded functions. For Schwartz \(u,v\), their packet reconstructions and (E27) give
\((Au,v)=(\mathcal M Vu,Vv)\).
All integrals converge by the decay just proved. Hence \(A=V^*\mathcal M V\) on \(\mathcal S\) as distributions, which establishes both membership of \(Au\) in \(L^2\) and the norm bound. No \(L^2\) boundedness of \(A\) was assumed in forming its packet matrix. This proves (E23), and density gives the extension. ∎

The calculation works for fixed-size matrices by estimating the matrix norm in (E26) and applying the scalar majorant to the norm of the vector input. It therefore has no positivity or scalar-commutativity assumption.

