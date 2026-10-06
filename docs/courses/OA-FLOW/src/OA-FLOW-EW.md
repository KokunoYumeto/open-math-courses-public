# Order normality and ultraweak lower semicontinuity for every weight

*Fresh reconstruction, GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

Let \(M\subseteq B(K)\) be a concrete von Neumann algebra on an arbitrary Hilbert space. A weight \(\varphi:M_+\to[0,\infty]\) is additive and positively homogeneous, with \(0\cdot\infty=0\). We prove, without faithfulness, semifiniteness or a countability assumption, that these conditions are equivalent:

1. \(\varphi\) preserves bounded increasing positive suprema.
2. Every sublevel \(E_r=\{a\in M_+:\varphi(a)\leq r\}\), \(0\leq r<\infty\), is ultraweakly closed.
3. On the whole positive cone, including infinite values,
   \[
   \varphi(a)=\sup\{f(a):f\in M_*^+,\ f\leq\varphi\}.
   \tag{EW1}
   \]

Here \(f\leq\varphi\) means the inequality on every positive element. No finite-cone-only convention is used.

The exact earlier inputs are [GW-1–5](OA-FLOW-GW.md#oa-flow.gw.1), [NF-5](OA-FLOW-NF.md#oa-flow.nf.5), [CF Sections 1 and 6–10](OA-FLOW-CF.md#oa-flow.cf.1), [SF-0 and SB-0–6](OA-FLOW-SF.md#oa-flow.sf.sf0), [FF-4](OA-FLOW-FF.md#oa-flow.ff.5) and [FF-5 form invariance](OA-FLOW-FF.md#oa-flow.ff.6), [CP01–06](OA-FLOW-CP.md#oa-flow.cp.1), [BD7](OA-FLOW-BD.md#oa-flow.bd.5), and [CV-1–4](OA-FLOW-CV.md#cv-1). In particular [NF-5](OA-FLOW-NF.md#oa-flow.nf.5) was proved using only the bounded-functional normality criterion; it did not import any implication of the present theorem. [FF-4](OA-FLOW-FF.md#oa-flow.ff.5) permits arbitrary Hilbert dimension and a nondense form domain. The proof below uses its dense-domain case on a reducing subspace constructed explicitly.

The broader theorem is stated in the freely available [Hiai notes, §7.1, Theorem 7.2](https://arxiv.org/pdf/2004.02383v1#page=63); that statement is context, not a proof input. The argument here is developed from the listed local bodies: a weighted difference form proves bounded GNS graph closedness, and a rational order cutoff proves positivity of the separating functionals.

Actual earlier proof ranges: [OA-FLOW.GW.1](OA-FLOW-GW.md#oa-flow.gw.1), [OA-FLOW.GW.2](OA-FLOW-GW.md#oa-flow.gw.2), [OA-FLOW.GW.3](OA-FLOW-GW.md#oa-flow.gw.3), [OA-FLOW.GW.4](OA-FLOW-GW.md#oa-flow.gw.4), [OA-FLOW.GW.5](OA-FLOW-GW.md#oa-flow.gw.5), [OA-FLOW.NF.5](OA-FLOW-NF.md#oa-flow.nf.5), [OA-FLOW.CF.1](OA-FLOW-CF.md#oa-flow.cf.1), [OA-FLOW.CF.6](OA-FLOW-CF.md#oa-flow.cf.6), [OA-FLOW.CF.7](OA-FLOW-CF.md#oa-flow.cf.7), [OA-FLOW.CF.8](OA-FLOW-CF.md#oa-flow.cf.8), [OA-FLOW.CF.9](OA-FLOW-CF.md#oa-flow.cf.9), [OA-FLOW.CF.10](OA-FLOW-CF.md#oa-flow.cf.10), [OA-FLOW.SF.SF0](OA-FLOW-SF.md#oa-flow.sf.sf0), [OA-FLOW.SF.SB0](OA-FLOW-SF.md#oa-flow.sf.sb0), [OA-FLOW.SF.SB1](OA-FLOW-SF.md#oa-flow.sf.sb1), [OA-FLOW.SF.SB2](OA-FLOW-SF.md#oa-flow.sf.sb2), [OA-FLOW.SF.SB3](OA-FLOW-SF.md#oa-flow.sf.sb3), [OA-FLOW.SF.SB4](OA-FLOW-SF.md#oa-flow.sf.sb4), [OA-FLOW.SF.SB5](OA-FLOW-SF.md#oa-flow.sf.sb5), [OA-FLOW.SF.SB6](OA-FLOW-SF.md#oa-flow.sf.sb6), [OA-FLOW.FF.5](OA-FLOW-FF.md#oa-flow.ff.5), [OA-FLOW.FF.6](OA-FLOW-FF.md#oa-flow.ff.6), [OA-FLOW.CP.1](OA-FLOW-CP.md#oa-flow.cp.1), [OA-FLOW.CP.2](OA-FLOW-CP.md#oa-flow.cp.2), [OA-FLOW.CP.3](OA-FLOW-CP.md#oa-flow.cp.3), [OA-FLOW.CP.4](OA-FLOW-CP.md#oa-flow.cp.4), [OA-FLOW.CP.5](OA-FLOW-CP.md#oa-flow.cp.5), [OA-FLOW.CP.6](OA-FLOW-CP.md#oa-flow.cp.6), [OA-FLOW.BD.5](OA-FLOW-BD.md#oa-flow.bd.5), [OA-FLOW.CV.1](OA-FLOW-CV.md#cv-1), [OA-FLOW.CV.2](OA-FLOW-CV.md#cv-2), [OA-FLOW.CV.3](OA-FLOW-CV.md#cv-3), [OA-FLOW.CV.4](OA-FLOW-CV.md#cv-4).

<a id="oa-flow.ew.1"></a><a id="ew-1"></a>

## EW-1. The norm-closed GNS graph

Assume condition 1. Let \(N=\{x:\varphi(x^*x)<\infty\}\), and write \((H,\Lambda,\pi)\) for GW's quotient GNS construction. The map \(\pi\) is ultraweakly continuous by [NF-5](OA-FLOW-NF.md#oa-flow.nf.5), even if the weight is not faithful or semifinite.

Suppose \(x_n\in N\), \(x_n\to x\) in operator norm, and \(\Lambda x_n\to\xi\) in Hilbert norm. Choose a subsequence \(x_{n_k}\) whose successive differences \(d_k=x_{n_{k+1}}-x_{n_k}\) satisfy
\[
\|d_k\|+\|\Lambda d_k\|\leq4^{-k}.
\]
The positive series \(b=\sum_{k\geq1}2^k d_k^*d_k\) converges in operator norm. Its increasing partial sums have supremum \(b\), so order normality gives
\[
\varphi(b)=\sum_{k\geq1}2^k\|\Lambda d_k\|^2<\infty.
\tag{EW2}
\]
For a finite sum, Hilbert-space Cauchy–Schwarz applied after evaluation on each vector proves
\[
\left(\sum_{j=k}^{l}d_j\right)^*
\left(\sum_{j=k}^{l}d_j\right)
\leq\left(\sum_{j=k}^{l}2^{-j}\right)
\left(\sum_{j=k}^{l}2^j d_j^*d_j\right).
\]
Pass to the norm limit \(l\to\infty\). Since \(z_k=x-x_{n_k}=\sum_{j\geq k}d_j\),
\[
z_k^*z_k\leq2^{1-k}b,\qquad
z_k\in N,\qquad \|\Lambda z_k\|^2\leq2^{1-k}\varphi(b)\longrightarrow0.
\tag{EW3}
\]
Thus \(x=x_{n_k}+z_k\in N\) and \(\Lambda x=\xi\). The linear graph of \(\Lambda\) is norm closed in \(M\oplus H\). This argument uses no assertion about continuity of the weight in the operator norm.

<a id="oa-flow.ew.2"></a><a id="ew-2"></a>

## EW-2. Bounded adjoint-strong graph closedness

Fix \(C<\infty\), and let a net satisfy
\[
x_i\in N,\quad \|x_i\|\leq C,\quad
x_i^*v\longrightarrow x^*v\ (v\in K),\quad
\Lambda x_i\longrightarrow\xi\text{ in }H.
\tag{EW4}
\]
We prove \(x\in N\), \(\Lambda x=\xi\). The uniform norm bound in (EW4) is a hypothesis, not a consequence asserted for arbitrary convergent nets.

Fix a finite set \(F\subset K\). Let \(p\) be the orthogonal projection onto
\[
K_F=\overline{\operatorname{span}}\{y'v:y'\in M',\ v\in F\}.
\]
This subspace reduces \(M'\), so \(p\in M\) by the bicommutant/unitary test in SF-0. Choose successive indices \(i_n\) so that, writing \(z_n=x_{i_n}\),
\[
\|\Lambda z_n-\xi\|\leq2^{-3n},\qquad
\|(z_n^*-x^*)v\|\leq2^{-3n}\quad(v\in F).
\tag{EW5}
\]
Directedness permits this selection. We do not assert that the sequence is cofinal in the original net. Because \(z_n^*-x^*\) commutes with \(M'\) and is uniformly bounded, (EW5) implies
\[
z_n^*v\longrightarrow x^*v\qquad(v\in K_F).
\tag{EW6}
\]

On \(K_F\) define
\[
q(v)=\sum_{n\geq1}4^n\|(z_{n+1}-z_n)^*v\|^2.
\tag{EW7}
\]
Its finite domain is linear. It contains \(F\), by (EW5), and is invariant under \(M'\); indeed every unitary of \(M'\) preserves \(q\), and every element of \(M'\) is a linear combination of its unitaries. Hence the finite domain is dense in \(K_F\). The form is closed: if \(v_j\) is Cauchy in its graph norm and \(v_j\to v\) in \(K_F\), each finite partial sum at \(v_j-v\) is bounded by the graph-Cauchy tail, after taking the limit in the second index. Supremizing those partial sums gives \(q(v_j-v)\to0\); one \(v_j\) then shows \(v\) has finite form value.

[FF-4](OA-FLOW-FF.md#oa-flow.ff.5) gives a positive self-adjoint \(T\) on \(K_F\), with \(q(v)=\|T^{1/2}v\|^2\). Form invariance and the uniqueness proved there imply that its spectral projections commute with the restrictions of all unitaries of \(M'\). Extend
\[
e_m=1_{[0,m]}(T)
\]
by zero on \(K_F^\perp\). Then \(e_m\in M\), \(e_m\uparrow p\), and (EW7) gives
\[
\|(z_{n+1}-z_n)^*e_m\|\leq\sqrt m\,2^{-n},\qquad
\|e_m(z_{n+1}-z_n)\|\leq\sqrt m\,2^{-n}.
\tag{EW8}
\]
Consequently \(e_m z_n\) converges in operator norm. By (EW6) its adjoint limit on every vector is \(x^*e_m\); thus its norm limit is exactly \(e_m x\). Also
\[
\Lambda(e_m z_n)=\pi(e_m)\Lambda z_n\longrightarrow\pi(e_m)\xi.
\]
[EW-1](OA-FLOW-EW.md#ew-1) proves
\[
e_m x\in N,\qquad \Lambda(e_m x)=\pi(e_m)\xi.
\tag{EW9}
\]
Since \(x^*e_m x\uparrow x^*px\), order normality yields
\[
\varphi(x^*px)=\sup_m\|\pi(e_m)\xi\|^2\leq\|\xi\|^2.
\]
Thus \(px\in N\). Finite additivity inside this finite value gives
\[
\|\Lambda((p-e_m)x)\|^2=\varphi(x^*px)-\varphi(x^*e_mx)\longrightarrow0.
\]
[NF-5](OA-FLOW-NF.md#oa-flow.nf.5) gives \(\pi(e_m)\to\pi(p)\) strongly, so (EW9) implies \(\Lambda(px)=\pi(p)\xi\).

Now let \(F\) run over all finite subsets of \(K\), ordered by inclusion. The corresponding \(p_F\) increase to \(1\), since their ranges contain those finite subsets. We have just proved
\[
\varphi(x^*p_Fx)=\|\pi(p_F)\xi\|^2\leq\|\xi\|^2.
\]
Order normality again gives \(x\in N\), and the same finite-value difference argument gives \(\Lambda x=\xi\). This proves (EW4) for arbitrary nets on arbitrary Hilbert spaces. Only the sequence on the explicitly chosen reducing subspace was used.

<a id="oa-flow.ew.3"></a><a id="ew-3"></a>

## EW-3. Ultraweak lower semicontinuity on the whole cone

The set
\[
G_C=\{(x,\Lambda x):x\in N,\ \|x\|\leq C\}\subset M\times H
\]
is convex and closed for adjoint-strong times Hilbert norm by [EW-2](OA-FLOW-EW.md#ew-2); the norm bound passes to adjoint-strong limits. [CV-2](OA-FLOW-CV.md#cv-2) makes \(G_C\) closed for ultraweak times Hilbert weak topology.

Fix \(r,C<\infty\), \(r,C\geq0\). Suppose \(a_i\in E_r\), \(\|a_i\|\leq C\), and \(a_i\to a\) strongly. Positivity and the norm bound pass to the limit. The square roots converge strongly: approximate \(t^{1/2}\) uniformly on \([0,C]\) by the actual CF polynomials, and use bounded strong continuity of multiplication in each polynomial. The vectors \(\Lambda(a_i^{1/2})\) lie in the radius-\(\sqrt r\) Hilbert ball. [CV-3](OA-FLOW-CV.md#cv-3) supplies a convergent subnet for the weak topology (or a cluster point of the tail filter), of weak limit \(\eta\) and norm at most \(\sqrt r\). Bounded strong convergence implies ultraweak convergence by [BD7](OA-FLOW-BD.md#oa-flow.bd.5). Closedness of \(G_{\sqrt C}\) therefore gives
\[
a^{1/2}\in N,\qquad\Lambda(a^{1/2})=\eta,\qquad\varphi(a)\leq r.
\]
Thus \(E_r\cap C\overline B_M\) is strongly closed. It is convex by weight additivity, so [CV-2](OA-FLOW-CV.md#cv-2) makes it ultraweakly closed.

CP01–06 identifies \(M=(M_*)^*\) isometrically with its concrete ultraweak topology and proves completeness of \(M_*\). Apply the full [CV-4](OA-FLOW-CV.md#cv-4) criterion to the convex subset \(E_r\) of this dual space. All its bounded slices have just been checked; hence \(E_r\) itself is ultraweakly closed. This proves \(1\Rightarrow2\), including the unbounded parts of the positive cone.

<a id="oa-flow.ew.4"></a><a id="ew-4"></a>

## EW-4. A positive downward hull and its exact closure

We prove the separation step needed for (EW1); a separator of a positive sublevel alone need not be positive.

Put \(E=E_1\) and
\[
D=\overline{E-M_+}^{\,\|\cdot\|}\subset M_{\rm sa}.
\]
This is convex, norm closed, contains \(0\) and \(-M_+\), and is downward closed under subtraction of \(M_+\). First,
\[
D\cap M_+=E.
\tag{EW10}
\]
Indeed let \(a_n-b_n\to x\geq0\) in norm with \(a_n\in E,b_n\geq0\), and choose \(\epsilon_n>0\) tending to zero with \(x\leq a_n+\epsilon_n1\). Set
\[
v_n=\left(a_n(a_n+\epsilon_n1)^{-1}\right)^{1/2},\qquad
c_n=v_n x v_n.
\]
Then \(0\leq c_n\leq a_n\), so \(c_n\in E\). Moreover
\[
\begin{split}
\|(1-v_n)x^{1/2}\|^2
&=\|(1-v_n)x(1-v_n)\|\\
&\leq\|(1-v_n)(a_n+\epsilon_n1)(1-v_n)\|
\leq\epsilon_n.
\end{split}
\tag{EW11}
\]
The last inequality is the scalar identity
\((t+\epsilon)(1-\sqrt{t/(t+\epsilon)})^2=(\sqrt{t+\epsilon}-\sqrt t)^2\leq\epsilon\)
in continuous calculus. Writing \(c_n=(v_nx^{1/2})(v_nx^{1/2})^*\) proves
\(\|c_n-x\|\leq2\sqrt{\|x\|\epsilon_n}\to0\).
[EW-3](OA-FLOW-EW.md#ew-3) makes \(E\) norm closed, proving (EW10).

Next \(D\) is ultraweakly closed. By [CV-4](OA-FLOW-CV.md#cv-4) it suffices to check its bounded slices. Suppose \(x_i\in D\), \(\|x_i\|\leq C\), and \(x_i\to x\) ultraweakly. Approximate each \(x_i\) in norm by elements of \(E-M_+\), on the product of the original directed set and a decreasing positive error parameter. This gives a net
\[
y_j=a_j-b_j\longrightarrow x\text{ ultraweakly},\quad
a_j\in E,\ b_j\geq0,\quad\|y_j\|\leq C+1=:L.
\]
The uniform bound follows by restricting the error parameter to at most \(1\). No bound on \(a_j\) or \(b_j\) is claimed.

Fix \(0<\delta<1/L\) when \(L>0\), and put \(g_\delta(t)=t/(1+\delta t)\). Inversion reverses the order of strictly positive operators: if \(0<A\leq B\), conjugate by \(A^{-1/2}\), invert its positive spectrum, and conjugate back to get \(B^{-1}\leq A^{-1}\). Since \(y_j\leq a_j\) and \(1+\delta y_j\geq(1-\delta L)1\), this proves
\[
g_\delta(y_j)\leq g_\delta(a_j)=:r_j,\quad
0\leq r_j\leq a_j,\quad \|r_j\|\leq\delta^{-1}.
\]
Thus \(r_j\in E\). On \([-L,L]\),
\[
g_\delta(t)=t-\frac{\delta t^2}{1+\delta t}
\geq t-\eta_\delta,\qquad
\eta_\delta=\frac{\delta L^2}{1-\delta L}\longrightarrow0.
\tag{EW12}
\]
The bounded slice of \(E\) is ultraweakly compact by [EW-3](OA-FLOW-EW.md#ew-3) and [CV-3](OA-FLOW-CV.md#cv-3). Along a subnet \(r_j\to r_\delta\in E\), positivity and (EW12) give
\[
r_\delta\geq x-\eta_\delta1.
\]
Consequently \(x-\eta_\delta1\in E-M_+\subset D\). Norm closedness and \(\eta_\delta\to0\) imply \(x\in D\). The zero bound case is immediate. This verifies every slice and hence proves ultraweak closedness of \(D\).

<a id="oa-flow.ew.5"></a><a id="ew-5"></a>

## EW-5. Normal positive minorants, including infinite values

Let \(a\geq0\) and \(0<t<\varphi(a)\). Then \(a/t\notin E\), hence \(a/t\notin D\) by (EW10). Apply real ultraweak separation [CV-1](OA-FLOW-CV.md#cv-1) to the closed convex set \(D\) inside \(M_{\rm sa}\). It gives a continuous real linear \(L\) with
\[
L(a/t)>c:=\sup_{d\in D}L(d)\geq0.
\tag{EW13}
\]
As \(-s b\in D\) for all \(s\geq0,b\geq0\), finiteness of \(c\) forces \(L(b)\geq0\). Its complexification \(f(x+iy)=L(x)+iL(y)\), \(x,y\in M_{\rm sa}\), is positive and ultraweakly continuous: the self-adjoint real/imaginary part maps are ultraweakly continuous, directly from the concrete vector-series description in CP01–06. Thus \(f\in M_*^+\).

If \(c>0\), replace \(f\) by \(f/c\). Then \(f(b)\leq1\) for \(b\in E\). If \(0<\varphi(b)<\infty\), apply this to \(b/\varphi(b)\); if \(\varphi(b)=0\), apply it to every \(s b\), \(s>0\), to obtain \(f(b)=0\). Infinite weight values impose no upper restriction. Hence \(f\leq\varphi\), and (EW13) gives \(f(a)>t\).

If \(c=0\), then \(f\) vanishes on \(E\), and therefore on every finite-weight positive element by the same scaling argument. Every positive multiple of \(f\) is dominated by \(\varphi\); since \(f(a)>0\), choose such a multiple with value greater than \(t\).

We have proved that for every \(0<t<\varphi(a)\) some \(f\in M_*^+\), \(f\leq\varphi\), satisfies \(f(a)>t\). When \(\varphi(a)=0\) use the zero functional. When \(\varphi(a)=\infty\), let \(t\) be arbitrarily large. This proves (EW1) on the entire cone, with no faithfulness or semifiniteness assumption.

Finally, condition 3 implies 2 because each normal positive functional is ultraweakly continuous and a supremum of continuous real functions is lower semicontinuous. Condition 2 implies 1: if \(a_i\uparrow a\) boundedly, bounded strong convergence and [BD7](OA-FLOW-BD.md#oa-flow.bd.5) give ultraweak convergence. With \(s=\sup_i\varphi(a_i)\), the case \(s=\infty\) follows from monotonicity; if \(s<\infty\), closedness of \(E_s\) gives \(\varphi(a)\leq s\), and monotonicity gives equality. All three conditions are equivalent.

<a id="oa-flow.ew.6"></a><a id="ew-6"></a>

## Exact scope

The equivalence theorem applies to every additive extended-valued weight, allowing zero, nonfaithful, nonsemifinite and non-countably-decomposable cases. The bounded GNS graph closedness statement assumes order normality (condition 1); it requires no additional faithfulness, semifiniteness or countability assumption. They prove neither a sum decomposition into normal functionals nor operator-valued weight comparison. Finite-star involution closability for a faithful normal semifinite weight is a separate consequence developed in the next provider.
