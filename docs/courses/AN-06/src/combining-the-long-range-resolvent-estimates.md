# Combining the long-range resolvent estimates

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: Which error remains after the two frequency estimates are combined?** The off-energy inverse and the near-energy commutator control complementary frequency regions. The rough short-range term still has to map between their weighted spaces. Symmetry gives a second map from the first, and absorption removes a weaker exterior norm while retaining a compact interior observation. That retained observation explains why this estimate alone does not exclude eigenvalues.

The smooth long-range equation now has two estimates. Away from its free energy surface, it gains the full differential order. Near noncritical frequencies, a commutator controls the spatial endpoint norm. The actual perturbation also has a rough short-range part. We account for that part by two weighted maps, combine the frequency pieces, and absorb a weaker spatial norm. The resulting estimate holds near every regular free energy, including an energy at which the perturbed operator has an eigenvalue.

Read [Admissible differential perturbations](admissible-differential-perturbations.md) for the coefficient class and symmetric splitting, [The Sobolev domain of an elliptic operator](the-sobolev-domain-of-an-elliptic-operator.md) for the self-adjoint realization, and [Weighted Sobolev spaces and rough elliptic estimates](weighted-sobolev-spaces-and-rough-elliptic-estimates.md) for the weighted calculus and graph estimate. The two frequency estimates are [The resolvent away from the energy surface](the-resolvent-away-from-the-energy-surface.md) and [A resolvent estimate at noncritical frequencies](a-resolvent-estimate-at-noncritical-frequencies.md). [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md) gives the spatial norms, while [Resolvents, domains and spectral density](resolvents-domains-and-spectral-density.md) gives the nonreal resolvent of a self-adjoint operator. The freely readable Agmon notes [A] supply the classical combination to compare with; the rough maps and absorption are proved below. Teschl [T] explains resolvents and bound states.

Use \(D=-i\partial\), \(X=\langle x\rangle\), \(M_t=X^t\), \(J_s=\langle D\rangle^s\), and an inner product linear in its first entry. Our weighted spaces have the exact convention

\[
 \|u\|_{s,t}=\|M_tJ_su\|_2,\qquad
 (M_tJ_s)^{-1}=J_{-s}M_{-t}.
 \tag{1}
\]

## 1. The complete local endpoint estimate

Recall the spatial shells

\[
 \begin{gathered}
 A_0=\{|x|<1\},\qquad R_j=2^j,\\
 A_j=\{2^{j-1}\le |x|<2^j\}\quad(j\ge1),
 \end{gathered}
 \tag{2}
\]

and the norms

\[
 \begin{aligned}
 \|f\|_B&=\sum_{j\ge0}R_j^{1/2}\|f\|_{L^2(A_j)},\\
 \|u\|_{B^*}&=\sup_{j\ge0}R_j^{-1/2}\|u\|_{L^2(A_j)}.
 \end{aligned}
 \tag{3}
\]

<a id="combined-domain"></a>

Let \(P_0(D)\) be a real scalar constant-coefficient elliptic differential operator of order \(m\ge1\), and let \(V\) be a symmetric \(1\)-admissible differential perturbation of the same maximal order. The admissible-perturbation lesson gives its full definition: continuous highest coefficients, the precise local \(L^p\) lower coefficients, an elliptic total principal symbol, and a \(C^1\) long-range splitting with a positive decay gap. The [full Sobolev-domain theorem](the-sobolev-domain-of-an-elliptic-operator.md#domain-theorem) gives

\[
 H=P_0(D)+V(x,D),\qquad \mathcal D(H)=H^m,
 \tag{4}
\]

as a self-adjoint operator in \(L^2\). Define the free critical-value set

\[
 Z(P_0)=\{P_0(\xi):\nabla P_0(\xi)=0\}.
 \tag{5}
\]

<a id="combined-theorem"></a>

This combination of the two frequency estimates is Hörmander [H4, Theorem 30.2.5].

**Theorem 1.1.** For every \(\lambda\in\mathbb R\setminus Z(P_0)\), there are \(r>0\) and \(C_\lambda<\infty\) such that, for \(f\in B\),

\[
 \begin{gathered}
 u=(H-z)^{-1}f,\qquad |z-\lambda|<r,\quad
 \operatorname{Im}z\ne0,\\
 \sum_{|\alpha|\le m}\|D^\alpha u\|_{B^*}
 \le C_\lambda\bigl(\|f\|_B+\|u\|_{0,-1}\bigr).
 \end{gathered}
 \tag{6}
\]

The constant is uniform throughout this punctured disc in both half-planes. All derivatives through the full order occur on the left. No point-spectrum exclusion is assumed. The auxiliary norm on the right is part of the conclusion, and cannot generally be discarded; Exercise 5 gives an explicit eigenvalue example.

<a id="combined-split"></a>

## 2. The symmetric split and its rough coefficient scope

The smoothing and symmetrization theorems in the admissible-perturbation lesson let us choose

\[
 V=V_L+V_S,
 \tag{7}
\]

with both summands symmetric and \(P_0+V_L\) uniformly elliptic. Corollary 5.3 of [Admissible differential perturbations](admissible-differential-perturbations.md#admissible-exterior-ellipticity) proves the complete compact modification: cut off the real smooth part inside a large ball and symmetrize it. Its highest coefficients are uniformly small, every derivative bound is preserved, and the compact coefficient difference and adjoint defect enter the symmetric short-range remainder. This normalization depends only on the coefficient lemmas; it precedes both frequency estimates.

Fix one \(0<\delta\le1\), no larger than the available smooth and short-range decay gaps. The smooth part has all the bounds required by the two frequency estimates:

\[
 \begin{aligned}
 |b_\alpha(x)|&\le C_\alpha X^{-\delta},\\
 |\partial^\beta b_\alpha(x)|
 &\le C_{\alpha\beta}X^{-1-\delta|\beta|}
       &&(|\beta|\ge1).
 \end{aligned}
 \tag{8}
\]

For the rough part, put \(d=1+\delta\) and write

\[
 V_S=\sum_{|\alpha|\le m}c_\alpha(x)D^\alpha.
 \tag{9}
\]

Highest coefficients are continuous and satisfy a pointwise bound. The lower coefficients satisfy a translated local bound:

\[
 \begin{aligned}
 |c_\alpha(x)|&\le CX^{-d}&&(|\alpha|=m),\\
 \|c_\alpha\|_{L^{p_\alpha}(B(y,1))}
 &\le C\langle y\rangle^{-d}&&(|\alpha|<m).
 \end{aligned}
 \tag{10}
\]

For \(k=m-|\alpha|>0\), the exponents are

\[
 p_\alpha=
 \begin{cases}
 n/k,&n>2k,\\
 \text{a fixed }p>2,&n=2k,\\
 2,&n<2k.
 \end{cases}
 \tag{11}
\]

These coefficients may be unbounded. Their original splitting and the symmetric differential expression can also have complex lower coefficients. We keep the actual coefficient products and never differentiate a rough coefficient.

The [global coefficient multiplier proposition](admissible-differential-perturbations.md#admissible-global-mapping) states that uniformly bounded translated local norms in (11), together with bounded highest coefficients, give a continuous differential map \(H^m\to L^2\). Its proof uses local Sobolev embedding, Hölder, a fixed cutoff and integration over its translations. It remains valid when a derivative has a larger gap than the coefficient originally required.

## 3. The primary short-range weighted map

<a id="combined-primary-map"></a>

The two short-range weighted maps are Hörmander [H4, (30.2.19)–(30.2.20)]. Sections 3–4 give their proofs with the full rough-coefficient hypotheses and the factor order in (1).

**Lemma 3.1.** For every real \(t\),

\[
 \begin{gathered}
 V_S:H^{m,t}\longrightarrow H^{0,t+d},\\
 \|V_Su\|_{0,t+d}\le C_t\|u\|_{m,t}.
 \end{gathered}
 \tag{12}
\]

This is the distributionally consistent extension of the differential expression.

**Proof.** First take \(u\in\mathcal S\), and put \(v=M_tu\). Leibniz gives a finite expansion of the conjugated expression:

\[
 \begin{aligned}
 M_{t+d}c_\alpha D^\alpha(M_{-t}v)
 ={}&\sum_{\gamma\le\alpha}\binom{\alpha}{\gamma}\\
 &\quad\cdot C_{\alpha\gamma,t}(x)
                  D^{\alpha-\gamma}v,\\
 C_{\alpha\gamma,t}
 ={}&X^{t+d}c_\alpha(x)(D^\gamma X^{-t}).
 \end{aligned}
 \tag{13}
\]

Here \(D^\gamma X^{-t}\) is a derivative of the multiplier function. The smooth power bound is

\[
 |D^\gamma X^{-t}|\le C_{t,\gamma}X^{-t-|\gamma|}.
 \tag{14}
\]

Brackets on a unit ball are uniformly comparable, so each lower coefficient in (13) has a uniformly bounded local \(L^{p_\alpha}\) norm, with the more precise bound \(C\langle y\rangle^{-|\gamma|}\). For an originally highest coefficient, it has a uniform pointwise bound.

For an originally lower coefficient, the new derivative gap is

\[
 k'=m-|\alpha-\gamma|=k+|\gamma|\ge k.
 \tag{15}
\]

If \(n>2k'\), its required exponent \(n/k'\) is no larger than \(p_\alpha\). If \(n=2k'\), choose a finite exponent greater than \(2\) and no larger than \(p_\alpha\); the original exponent is greater than \(2\), since \(k\le k'=n/2\). If \(n<2k'\), use \(2\le p_\alpha\). Finite-volume inclusion on each unit ball proves the needed smaller-exponent bounds. Terms from originally highest coefficients are already bounded multipliers. Thus the coefficient multiplier proposition applies to every term in the finite expansion, and gives

\[
 \begin{aligned}
 \|X^{t+d}V_Su\|_2
 &\le C_t\|X^tu\|_{H^m}\\
 &\le C'_t\|u\|_{m,t}.
 \end{aligned}
 \tag{16}
\]

The last comparison is the [factor-exchange theorem](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-factor-exchange).

Schwartz density gives a unique bounded extension. Convergence in \(H^{m,t}\) implies \(H^m\) convergence after any fixed compact cutoff. The local coefficient multiplier proof then identifies each limiting coefficient product in local \(L^2\). Hence the extension agrees with the differential expression as a distribution. \(\square\)

Symmetry on compact smooth functions extends to Schwartz pairings by the \(H^m\to L^2\) bound and approximation by compact tests. We use that fact for the second map.

## 4. The integral dual and the symmetric second map

<a id="combined-dual"></a>

**Lemma 4.1.** With the convention (1), the integral dual of \(H^{s,r}\) is exactly \(H^{-s,-r}\), with its displayed norm. In particular, for Schwartz \(g\),

\[
 \sup_{\substack{v\in\mathcal S\\ \|v\|_{s,r}\le1}}
 |(g,v)|=\|g\|_{-s,-r}.
 \tag{17}
\]

**Proof.** Put \(T=M_rJ_s\). Its inverse and the adjoint of that inverse are

\[
 T^{-1}=J_{-s}M_{-r},\qquad
 (T^{-1})^*=M_{-r}J_{-s}.
 \tag{18}
\]

Consequently

\[
 (g,v)=\bigl(M_{-r}J_{-s}g,Tv\bigr).
 \tag{19}
\]

Cauchy–Schwarz gives the upper bound. The operator \(T\) maps Schwartz space onto itself, densely in \(L^2\), so the \(L^2\) norm gives the exact supremum.

Conversely, the [local representing-vector proof in the endpoint lesson](endpoint-spaces-and-flat-energy-shells.md#endpoint-shell-spaces), applied after the isometry \(T\), writes a continuous conjugate-linear functional as \(F(v)=(h,Tv)\). Its representing distribution is

\[
 g=T^*h=J_sM_rh,\qquad
 M_{-r}J_{-s}g=h.
 \tag{20}
\]

It therefore belongs to \(H^{-s,-r}\) with norm \(\|h\|_2\). These identities extend by the distributional actions of the factors. No position factor was commuted through a Fourier factor. \(\square\)

The inverse in (18) and its adjoint have different orders. The dual norm uses the latter.

<a id="combined-symmetric-map"></a>

**Lemma 4.2.** For every real \(t\), symmetry gives a second continuous map,

\[
 \begin{gathered}
 V_S:H^{0,t}\longrightarrow H^{-m,t+d},\\
 \|V_Sg\|_{-m,t+d}\le C_t\|g\|_{0,t}.
 \end{gathered}
 \tag{21}
\]

**Proof.** On Schwartz inputs use symmetry and (12) at weight \(-t-d\):

\[
 \begin{aligned}
 |(V_Sg,v)|
 &=|(g,V_Sv)|\\
 &\le\|g\|_{0,t}\|V_Sv\|_{0,-t}\\
 &\le C_t\|g\|_{0,t}\|v\|_{m,-t-d}.
 \end{aligned}
 \tag{22}
\]

Lemma 4.1 identifies its representing distribution as an element of \(H^{-m,t+d}\), with the stated bound. Schwartz density extends the map uniquely. For each compact smooth test \(v\), the extension satisfies \((V_Sg,v)=(g,V_Sv)\): the right side is continuous in \(H^{0,t}\), since \(V_Sv\) is a compactly supported \(L^2\) function. If \(g\) also belongs to a primary-map domain \(H^{m,s}\), cut it off to a function in \(H^m\) equal to \(g\) on a neighborhood of \(\operatorname{supp}v\), and approximate that function by compact smooth functions in \(H^m\). The local coefficient multiplier bound passes the symmetry identity to the limit, giving the same pairing for the primary differential expression. Equality on every compact smooth test identifies the two distributions, for every such common domain. In particular, for the negative input weights used below, an \(H^m\) approximation also converges in \(H^{0,t}\), so consistency on the actual resolvent input follows directly. \(\square\)

This dual extension does not require defining a rough coefficient product on every arbitrary \(L^2_{\mathrm{loc}}\) input separately. It is the unique extension of the symmetric differential expression with the asserted topology.

<a id="combined-embeddings"></a>

## 5. Endpoint embeddings and the off-energy part

Two strict weighted embeddings will be useful. If \(\mu>1/2\) and \(b>1/2\), then

\[
 \|g\|_B\le C_\mu\|g\|_{0,\mu},
 \qquad
 \|u\|_{0,-b}\le C_b\|u\|_{B^*}.
 \tag{23}
\]

For the first, shell comparison and sequence Cauchy–Schwarz give

\[
 \begin{aligned}
 R_j^{1/2}\|g\|_{L^2(A_j)}
 &\le C_\mu R_j^{1/2-\mu}
             \|X^\mu g\|_{L^2(A_j)},\\
 \sum_jR_j^{1-2\mu}&<\infty.
 \end{aligned}
 \tag{24}
\]

For the second, square the shell estimate and sum:

\[
 \|X^{-b}u\|_2^2
 \le C_b\sum_jR_j^{1-2b}\|u\|_{B^*}^2.
 \tag{25}
\]

The unit shell obeys the same uniform bracket comparison. Exercise 3 checks why equality at the threshold is insufficient.

<a id="combined-off-energy"></a>

Fix \(\lambda\notin Z(P_0)\), and write \(M_\lambda=\{\xi:P_0(\xi)=\lambda\}\). Ellipticity makes this shell compact. Choose a real compact smooth \(\chi\), supported where \(\nabla P_0\ne0\), equal one near \(M_\lambda\). If the shell is empty, choose \(\chi=0\). Let \(r\le1\) be no larger than the radius in the off-energy theorem.

For \(|z-\lambda|<r\), \(Hu=f+zu\). The [rough graph estimate](weighted-sobolev-spaces-and-rough-elliptic-estimates.md#weighted-rough-graph-proof) at weight \(-d\) gives

\[
 \begin{aligned}
 \|u\|_{m,-d}
 &\le C\bigl(\|f\|_{0,-d}
              +(1+|z|)\|u\|_{0,-d}\bigr)\\
 &\le C_\lambda\bigl(\|f\|_B+\|u\|_{0,-1}\bigr).
 \end{aligned}
 \tag{26}
\]

Here \(|z|\le|\lambda|+1\), \(B\subset L^2\), and \(d>1\). All constants are fixed before \(z\) varies. Lemma 3.1 at \(t=-d\) now bounds \(\|V_Su\|_2\) by the same right side.

Apply [the off-energy estimate](the-resolvent-away-from-the-energy-surface.md#off-energy-resolvent-estimate) to

\[
 (P_0+V_L-z)u=f-V_Su.
 \tag{27}
\]

Use forcing exponents \(s=t=0\) and auxiliary exponents \(s'=0,t'=-1\). It gives

\[
 \|(1-\chi(D))u\|_{m,0}
 \le C_\lambda\bigl(\|f\|_B+\|u\|_{0,-1}\bigr).
 \tag{28}
\]

Every derivative of this part through order \(m\) belongs to \(L^2\subset B^*\), so its full derivative sum has that same bound.

<a id="combined-forcing-membership"></a>

## 6. The near-frequency part and uniform absorption

Before applying the near-frequency theorem, its complete forcing in (27) must belong to \(B\). This follows from a known domain bound: \(u\in H^m\), and (12) at \(t=0\) puts \(V_Su\) in \(H^{0,d}\subset B\). Thus \(f-V_Su\in B\). We have not used an endpoint estimate to establish that membership.

Put

\[
 \begin{gathered}
 a=\frac{1+\delta}{2},\qquad
 b=\frac12+\frac{\delta}{4},\\
 \frac12<b<a\le1.
 \end{gathered}
 \tag{29}
\]

<a id="combined-localized-rough"></a>

A compact smooth frequency multiplier has every negative frequency order. The weighted mapping theorem therefore gives
\(\chi(D):H^{-m,a}\to H^{0,a}\).
Combine this with (23) and the symmetric map (21):

\[
 \begin{aligned}
 \|\chi(D)V_Su\|_B
 &\le C_a\|\chi(D)V_Su\|_{0,a}\\
 &\le C\|V_Su\|_{-m,a}\\
 &\le C\|u\|_{0,a-d}
  =C\|u\|_{0,-a}.
 \end{aligned}
 \tag{30}
\]

The extended short-range action equals the primary action on this \(H^m\) input. The [noncritical-frequency estimate](a-resolvent-estimate-at-noncritical-frequencies.md#noncritical-theorem), its exact forcing cutoff, and boundedness of \(\chi(D)\) on \(B\) yield

\[
 \|\chi(D)u\|_{B^*}
 \le C_\lambda\bigl(\|f\|_B+\|u\|_{0,-a}\bigr).
 \tag{31}
\]

<a id="combined-derivatives"></a>

Choose a second compact cutoff \(\chi'\), equal one near \(\operatorname{supp}\chi\). The exact multiplier identity

\[
 D^\alpha\chi(D)=D^\alpha\chi'(D)\chi(D)
 \tag{32}
\]

and the [shell mapping estimate](a-resolvent-estimate-at-noncritical-frequencies.md#noncritical-shell-transfer) bound its \(B^*\) norm by \(C_\alpha\|\chi(D)u\|_{B^*}\). The multiplier \(D^\alpha\chi'(D)\) has a compact smooth symbol, so that interface applies for every \(|\alpha|\le m\).

Combine (28) and (31), and put
\(Y=\sum_{|\alpha|\le m}\|D^\alpha u\|_{B^*}\).
Since \(X^{-1}\le X^{-a}\), the result is

\[
 Y\le K_\lambda\bigl(\|f\|_B+\|u\|_{0,-a}\bigr).
 \tag{33}
\]

The second embedding in (23) gives

\[
 \|u\|_{0,-b}\le C_b\|u\|_{B^*}\le C_bY.
 \tag{34}
\]

<a id="combined-absorption"></a>

For any \(\eta>0\), split space at a sufficiently large fixed radius \(R\). On its exterior, \(X^{-a}=X^{b-a}X^{-b}\), and \(X^{b-a}\) can be made at most \(\eta\). Inside, \(X^{-a}=X^{1-a}X^{-1}\), and \(X^{1-a}\le\langle R\rangle^{1-a}\). The triangle inequality gives

\[
 \|u\|_{0,-a}
 \le\eta\|u\|_{0,-b}+C_\eta\|u\|_{0,-1}.
 \tag{35}
\]

Choose \(\eta\) after \(K_\lambda,C_b\), so that \(K_\lambda\eta C_b\le1/2\). Substitute (34)–(35) in (33) and absorb:

\[
 Y\le2K_\lambda\|f\|_B
          +2K_\lambda C_\eta\|u\|_{0,-1}.
 \tag{36}
\]

All numbers before absorption are finite because \(u\in H^m\). The radius is independent of \(f,u,z\). Both frequency estimates cover both signs of \(\operatorname{Im}z\). If the free shell is empty, (28) alone controls the full derivative sum. These observations prove Theorem 1.1 in its complete stated range. \(\square\)

### Use the conclusion

Identify both rough maps and the constants used in the absorption step. Compare the resulting estimate with the later limiting-absorption theorem: the latter must remove the compact error using a uniqueness argument.

For the last exercise, \(\operatorname{sech}x=2/(e^x+e^{-x})\); the [exponential construction and derivative rule](../providers/analysis/elementary-functions-and-cutoffs.md#scalar-exponential) give the required differentiation and decay.

<a id="combined-solutions"></a>

## 7. Graded exercises with complete solutions

**Exercise 1 — Basic: representing a weighted functional.** For real \(s,r\) and nonzero \(h\in\mathcal S\), define
\(F(v)=(h,M_rJ_sv)\).
Find its representing distribution \(g\) for the integral pairing, calculate its exact dual norm, and exhibit a test attaining that norm. Explain why using the un-adjointed inverse would give the wrong operator order.

**Solution 1.** Move the two factors to the first entry in reverse order:

\[
 g=J_sM_rh,\qquad
 M_{-r}J_{-s}g=h.
 \tag{37}
\]

Thus \(g\in H^{-s,-r}\) has exact norm \(\|h\|_2\). Take
\(v=J_{-s}M_{-r}h/\|h\|_2\).
It is Schwartz, \(M_rJ_sv=h/\|h\|_2\), and hence \(\|v\|_{s,r}=1\) and \(F(v)=\|h\|_2\). The dual norm is produced by \((T^{-1})^*\), which reverses the order of \(T^{-1}=J_{-s}M_{-r}\). Substitution of that inverse itself would not undo \(g=J_sM_rh\). No commutation identity is available to repair such a substitution.

**Exercise 2 — Intermediate: an unbounded short-range coefficient.** In dimension three and differential order two, choose a nonnegative \(\theta\in C_c^\infty(B(0,1))\) with \(\theta(0)=1\). For \(d>1\), put \(x_j=4je_1\), \(r_j=2^{-j}\), and

\[
 W(x)=\sum_{j\ge1}2^j\langle x_j\rangle^{-d}
                       \theta((x-x_j)/r_j).
 \tag{38}
\]

Prove that \(W\) is unbounded but satisfies the zeroth-order short-range local \(L^2\) condition. Deduce \(W:H^{2,t}\to H^{0,t+d}\) for every real \(t\).

**Solution 2.** The supports are disjoint and locally finite, so \(W\) is a smooth real function. Its value at \(x_j\) is \(2^j\langle x_j\rangle^{-d}\), which tends to infinity. The \(L^2\) norm of its \(j\)-th bump is

\[
 2^j\langle x_j\rangle^{-d}r_j^{3/2}\|\theta\|_2
 =2^{-j/2}\langle x_j\rangle^{-d}\|\theta\|_2.
 \tag{39}
\]

A unit ball meets at most one support: the centers are four units apart and every radius is at most one half. If it meets that support, \(\langle y\rangle\) is uniformly comparable with \(\langle x_j\rangle\). Its local norm is therefore at most \(C\langle y\rangle^{-d}\). For a zeroth-order coefficient in this case, the gap is \(k=2\) and \(n<2k\), so the exact required exponent is \(p=2\). Lemma 3.1 applies, giving the displayed weighted map. This argument uses local \(L^2\) bounds and never assumes a uniform pointwise bound for \(W\).

**Exercise 3 — Intermediate: both strict endpoint thresholds.** Show that \(H^{0,1/2}\subset B\) fails, and that \(B^*\subset H^{0,-1/2}\) fails. Construct both examples using normalized \(L^2\) functions \(h_j\) supported in the separate shells \(A_j\), \(j\ge1\).

**Solution 3.** Choose \(\|h_j\|_2=1\), and set

\[
 g=\sum_{j\ge1}\frac{R_j^{-1/2}}{j}h_j,\qquad
 v=\sum_{j\ge1}R_j^{1/2}h_j.
 \tag{40}
\]

These sums define locally square-integrable functions, because every fixed ball meets only finitely many shells. On \(A_j\), \(X\) is comparable to \(R_j\). Thus \(\|g\|_{0,1/2}^2\) is comparable with \(\sum_jj^{-2}<\infty\), but \(\|g\|_B=\sum_jj^{-1}=\infty\). Also \(\|v\|_{B^*}=1\), whereas \(\|v\|_{0,-1/2}^2\) is comparable with \(\sum_j1=\infty\). This proves both failures and explains the strict inequalities in (23).

**Exercise 4 — Advanced: the full forcing and its localized bound.** Explain why the application of the near-frequency theorem is legitimate before its conclusion is known. Then prove the estimate for \(\chi(D)V_Su\) in (30) from only the zeroth-order weighted norm of \(u\). State which of the two short-range maps is needed at each step.

**Solution 4.** The known resolvent domain is \(H^m\). The primary map (12) at \(t=0\) sends its input to \(H^{0,d}\), and \(d>1/2\), so (23) puts \(V_Su\) in \(B\). Therefore the complete forcing \(f-V_Su\) lies in \(B\), independently of any endpoint conclusion.

For the desired bound use the symmetric map, with input weight \(t=a-d=-a\). It gives
\(\|V_Su\|_{-m,a}\le C\|u\|_{0,-a}\).
The compact smooth multiplier \(\chi(D)\) has a symbol of order \(-m\) in the weighted calculus, and hence maps \(H^{-m,a}\to H^{0,a}\). Since \(a>1/2\), (23) sends the output to \(B\). These three bounds give (30). Replacing the symmetric map by the primary one would demand an \(H^{m,-a}\) input norm, which is not the auxiliary norm needed for the final absorption.

**Exercise 5 — Advanced: absorption and an eigenvalue pole.** For \(\delta=1/4\), give a sufficient large radius in (35) in terms of its small coefficient \(\eta\). Then consider, on the line,

\[
 H=-\partial_x^2-2\operatorname{sech}^2x,\qquad
 e(x)=\operatorname{sech}x.
 \tag{41}
\]

Verify its eigenvalue and explain why Theorem 1.1 cannot generally be strengthened by removing its auxiliary norm, even at a regular free energy with an empty shell.

**Solution 5.** Now \(a=5/8\), \(b=9/16\), and \(a-b=1/16\). For \(0<\eta\le1\), choose \(R\ge\eta^{-16}\). On \(|x|>R\), \(X^{-1/16}\le\eta\). Inside, \(X^{1-a}\le\langle R\rangle^{3/8}\). Thus (35) holds with \(C_\eta=\langle R\rangle^{3/8}\). Choosing \(\eta\le(2K_\lambda C_b)^{-1}\) supplies the absorption independently of \(u,f,z\).

The function \(e\) and its derivatives decrease exponentially, so \(e\in H^2\cap B\), with a nonzero finite \(B^*\) norm. Direct differentiation gives
\(e''=e-2e^3\), and therefore \(He=-e\).
The real potential is smooth and short range, and the principal symbol remains \(\xi^2\); thus the operator meets the admissible hypotheses. Its free critical-value set is \(\{0\}\). The value \(\lambda=-1\) is regular, and its free energy shell is empty.

For \(f=e\) and \(z=-1+i\varepsilon\), the resolvent solution is

\[
 u=(-1-z)^{-1}e=\frac{i}{\varepsilon}e.
 \tag{42}
\]

Its \(B^*\) norm tends to infinity as \(\varepsilon\downarrow0\), while \(\|f\|_B\) stays fixed. A uniform estimate with only that forcing norm is impossible. The retained norm \(\|u\|_{0,-1}\) has the same \(1/\varepsilon\) growth, so (6) remains consistent. The theorem deliberately includes this eigenvalue situation.

## 8. Reading and further directions

An a priori estimate with an auxiliary term is an intermediate step toward a limiting resolvent theorem. The next issue is the behavior of limits of resolvent graphs, including radiation conditions along the free normal directions. Removing an auxiliary term on suitable energy sets requires the corresponding uniqueness and point-spectrum arguments.

## References

The [accessible scalar comparisons in the limiting-absorption lesson](limiting-absorption-for-long-range-differential-perturbations.md#accessible-scalar-comparisons-and-their-proof-limits) state the precise Ito–Skibsted and Yafaev hypotheses, conclusions and proof dependencies. Ito–Skibsted's strong distorted-commutator estimates use an existing LAP; Yafaev cites the Mourre-to-LAP implication. Neither is an input to the compact-error estimate proved here.

[A] Shmuel Agmon, notes by Karl Gustafson, reworked by Michael Taylor, [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), lectures of 17–21 July 1978, §3, Theorem 3.A and equations (3.2)–(3.8), gives the freely readable off-shell/near-shell/absorption construction. Its coefficient hypotheses are pointwise bounds, and its auxiliary Proposition 3.F is left without a complete proof. The argument above instead uses the proved near-frequency commutator, not Proposition 3.F. Sections 3–4 prove the two maps for the full local \(L^p\) rough coefficients, Section 6 establishes the complete forcing before applying that commutator, and (35)–(36) prove the uniform absorption. Thus the transcription supplies a construction to compare with; the full rough extension is proved here.

[T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*, author's online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf), develops self-adjoint resolvents, Schrödinger operators and bound states. The calculated example in Exercise 5 shows why an auxiliary norm can coexist with an eigenvalue pole.


[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, the short-range weighted maps (30.2.19)–(30.2.20), Theorem 30.2.5 and its proof, pp. 288–289. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
