# Recovering the subgroup representation from imprimitivity

The induced system of lesson 44 starts with a representation of $H$ and produces a covariant representation of $C_0(G/H)$. The converse can be built from the covariant representation itself: smooth its spectral measures, take the density at the identity coset, and complete that positive form. The resulting Hilbert space carries the missing subgroup representation.

*Programme exposition written in Codex (OpenAI), September 2026; foundation integration and proof restoration by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original programme expression is dedicated under CC0 to the extent of rights held. No human review is asserted.*

The exact earlier foundations are [QF4–5](OA-FLOW-QF.md#qf-4) for locally finite complex Radon functionals and scalar representing measures, [HR5](OA-FLOW-HR.md#hr-05) and [H0](OA-FLOW-TOPOLOGY.md#l138-h0) for compact product interchange, [CF8](OA-FLOW-CF.md#oa-flow.cf.8) and [CF10](OA-FLOW-CF.md#oa-flow.cf.10) for Hilbert completion and orthogonal complements, and the complete preceding quotient and induced-field chapters. Closed-subspace compact extensions are [QF1](OA-FLOW-QF.md#qf-1).

<a id="oa-flow.impr.setting"></a>

## The covariant system and the smooth domain

Let $G$ be a locally compact Hausdorff group, $H\subseteq G$ closed, and $Y=G/H$. Let $\mathcal L$ be an arbitrary Hilbert space, $U:G\to\mathcal U(\mathcal L)$ a strongly continuous representation, and $\pi:C_0(Y)\to B(\mathcal L)$ a nondegenerate representation satisfying

<a id="equation-m1"></a>

$$ U_t\pi(F)U_t^*=\pi(\alpha_tF),
    \qquad(\alpha_tF)(sH)=F(t^{-1}sH). \tag{M1} $$

The zero Hilbert space gives the zero induced system; assume $\mathcal L\ne0$. The compact-partition argument in [QF5](OA-FLOW-QF.md#qf-5) proves that $\pi$ is faithful. It uses transitivity and nondegeneracy directly, without an additional theorem identifying all ideals of $C_0(Y)$.

Use the left Haar and modular conventions of lesson 43, with $\chi(h)=\Delta_G(h)/\Delta_H(h)$. For $f\in C_c(G)$ put $U(f)=\int_G f(t)U_t\,dt$ and let

<a id="equation-m2"></a>

$$ \mathscr D=\operatorname{span}\{U(f)\zeta:
                   f\in C_c(G),\ \zeta\in\mathcal L\}. \tag{M2} $$

Normalized compactly supported approximate identities, indexed by neighborhoods of the identity, converge strongly by continuity of each orbit map. These are nets when a countable neighborhood base is unavailable. They show that $\mathscr D$ is dense in $\mathcal L$. It is invariant under each $U_t$ because $U_tU(f)=U(L_tf)$.

For $\xi,\eta\in\mathcal L$, define a complex Radon measure $m_{\xi,\eta}$ on $G$ by

<a id="equation-m3"></a>

$$ m_{\xi,\eta}(f)=\langle\pi(Qf)\xi,\eta\rangle,
                    \qquad f\in C_c(G), \tag{M3} $$

where $Qf(sH)=\int_Hf(sh)\,dh$ as in lesson 43. For $\xi=\eta$, the measure is positive. It is the lift through $Q$ of the scalar representing measure $\mu_{\xi,\eta}$ from [QF5](OA-FLOW-QF.md#qf-5). Only these scalar measures are needed.

<a id="oa-flow.impr.smooth"></a>

## Smoothing yields a continuous density

**Lemma.** For $\xi,\eta\in\mathscr D$, the measure $m_{\xi,\eta}$ has a unique continuous density $k_{\xi,\eta}$ against left Haar measure.

**Proof.** It suffices to take $\xi=U(f)\zeta$ and $\eta=U(g)\omega$ with $f,g\in C_c(G)$. For a test $F\in C_c(G\times G)$, write $F_v(s)=F(s,v)$ and define a complex Radon measure $\nu_{\zeta,\omega}$ on $G\times G$ by

<a id="equation-m4"></a>

$$ \nu_{\zeta,\omega}(F)
    =\int_G\langle\pi(QF_v)U_v\zeta,\omega\rangle\,dv. \tag{M4} $$

On any compact rectangle, the quotient averages $QF_v$ are uniformly bounded by a compact-dependent multiple of $\|F\|_\infty$; the $v$-integral also ranges over a compact set. Thus (M4) is a locally bounded functional on $C_c(G\times G)$; [QF4](OA-FLOW-QF.md#qf-4) represents it by a locally finite complex Radon measure, with finite variation on every compact set. No finite global total variation is asserted.

Expand (M3) for the smoothed vectors and move $U_t^*$ through $\pi$ using (M1). Substitute first $r=t v$ and then $x=t u$ in the resulting Haar integrals. The formula becomes

<a id="equation-m5"></a>

$$ k_{U(f)\zeta,U(g)\omega}(x)
   =\int_{G\times G}
       \overline{g(xu^{-1})}\,
       f(xu^{-1}v)\,
       \Delta_G(u)^{-1}\,
       d\nu_{\zeta,\omega}(u,v). \tag{M5} $$

The change $x=tu$ is a right translation, so its Jacobian is the displayed inverse modular function. For $x$ in a compact set, nonzero integrands in (M5) use only a common compact part of $G\times G$, determined by the supports of $f$ and $g$. Continuity of the integrand and local finiteness of $\nu_{\zeta,\omega}$ give continuity in $x$. All interchanges here concern continuous scalar functions on compact products and finite restrictions of Radon measures. Compact Radon Fubini, or uniform approximation by sums of product functions, proves that integrating (M5) against any test recovers (M3). No countable base, separable Hilbert space or equality of global product Borel sigma-algebras is used. Finite sums give the claim. $\square$

The same compact-support calculation gives joint continuity of the density after replacing $\xi,\eta$ by $U_r\xi,U_s\eta$ and varying $r,s$ locally. We will use that continuity when completing a fiber at the identity. On fixed compact supports for $f,g$, (M4)–(M5) also bound $|B(U(f)\zeta,U(g)\omega)|$ by a constant times $\|f\|_\infty\|g\|_\infty\|\zeta\|\|\omega\|$; the constant depends only on the supports.

<a id="oa-flow.impr.fiber"></a>

## The identity-coset Hilbert space

Define on $\mathscr D$

<a id="equation-m6"></a>

$$ B(\xi,\eta)=k_{\xi,\eta}(e). \tag{M6} $$

This form is positive: $m_{\xi,\xi}$ is a positive measure, so its continuous density is nonnegative at every point. Let $K$ be the Hilbert completion of $\mathscr D/\ker B$ and denote the class of $\xi$ by $[\xi]$.

Two identities determine the subgroup action. First, covariance of $U$ and uniqueness of the continuous density give

<a id="equation-m7"></a>

$$ k_{\xi,\eta}(s)
      =B(U_s^*\xi,U_s^*\eta). \tag{M7} $$

Second, because $m_{\xi,\eta}$ is a quotient lift, its density obeys the right-$H$ modular law of lesson 43:

<a id="equation-m8"></a>

$$ k_{\xi,\eta}(sh)=\chi(h)^{-1}k_{\xi,\eta}(s)
       \qquad(s\in G,\ h\in H). \tag{M8} $$

The identity is pointwise here: the quotient lift gives it almost everywhere for each $h$, and both sides are continuous in $s$.

Evaluate (M7) at $s=h^{-1}$ and use (M8). It follows that

<a id="equation-m9"></a>

$$ B(U_h\xi,U_h\eta)=\chi(h)B(\xi,\eta). \tag{M9} $$

Thus

<a id="equation-m10"></a>

$$ V_h[\xi]=\chi(h)^{-1/2}[U_h\xi],
                    \qquad h\in H, \tag{M10} $$

is an isometry of $K$, with inverse $V_{h^{-1}}$. It is a group representation. Joint continuity of the smoothed densities from (M5) makes $h\mapsto B(U_h\xi,\eta)$ continuous on $\mathscr D$; (M10) is weakly continuous on a dense set and hence strongly continuous as a unitary representation.

This explains the inverse square root in the *recovered* representation. It precisely cancels the scaling (M9). The induced-field covariance of lesson 44 has the opposite placement of the same square root.

<a id="oa-flow.impr.unitary"></a>

## The reconstruction map is unitary

For $\xi\in\mathscr D$, define a $K$-valued field

<a id="equation-m11"></a>

$$ (W\xi)(s)=[U_s^*\xi]. \tag{M11} $$

Joint continuity of the smoothed densities makes it a continuous field. Its image on each compact is compact in the metric space $K$, hence separable. It satisfies the local measurability convention of [lesson 44](OA-FLOW-L44.md) even when $K$ is not separable. Equations (M9)–(M10) give

<a id="equation-m12"></a>

$$ (W\xi)(sh)=\chi(h)^{-1/2}V_h^*(W\xi)(s), \tag{M12} $$

so it is a field of the induced representation from $V$. If $k_0$ is the cutoff from lesson 43, then (M7), (M3), and $Qk_0=1$ yield

<a id="equation-m13"></a>

$$ \|W\xi\|_{\mathrm{ind}}^2
   =\int_G k_0(s)B(U_s^*\xi,U_s^*\xi)\,ds
   =\int_G k_0(s)k_{\xi,\xi}(s)\,ds
   =\|\xi\|_{\mathcal L}^2. \tag{M13} $$

The final equality follows first with $k_0(s)F(sH)$, $F\in C_c(Y)_+$ and $F\leq1$, by (M3). Take the supremum over $F$: the scalar positive measure of $\pi$ has total mass $\|\xi\|^2$ by QF5, and the cutoff identity is (I4) of lesson 44. This does not use a global countable exhaustion or arbitrary-net monotone convergence. Thus $W$ extends to an isometry $\mathcal L\to\operatorname{Ind}_H^G K$. Directly from (M11), $WU_t=U_t^{\mathrm{ind}}W$. The scalar representing measures from QF5 and (M3) give, for $F\in C_c(Y)$ and $\xi,\eta\in\mathscr D$,

<a id="equation-m14"></a>

$$ \langle\pi_{\mathrm{ind}}(F)W\xi,W\eta\rangle
  =\int_G k_0(s)F(sH)k_{\xi,\eta}(s)\,ds
  =\langle\pi(F)\xi,\eta\rangle. \tag{M14} $$

The compressed identity (M14) implies actual intertwining. Put $A=\pi_{\mathrm{ind}}(F)$. Apply (M14) also to $F^*F$; multiplicativity of both representations gives

<a id="equation-mi1"></a>

\[
 \|AW\xi-W\pi(F)\xi\|^2
 =\langle\pi(F^*F)\xi,\xi\rangle-\|\pi(F)\xi\|^2=0 .
 \tag{MI1}
\]
Here the mixed terms are evaluated with $W^*AW=\pi(F)$, and $W$ is an isometry. Thus $W\pi(F)=\pi_{\mathrm{ind}}(F)W$; continuity extends this to $C_0(Y)$.

It remains to show that $W$ is onto. Choose countably many tests only on one compact at a time. Let $\theta$ be an induced field and fix a compact $C$. Choose a separable closed subspace $E_C$ containing $\theta(s)$ for almost every $s\in C$, and a countable dense family $(v_j)$ in $E_C$. For every $s\in C$, the set $\{[U_s^*\xi]:\xi\in\mathscr D\}$ is dense in $K$, since $U_s^*\mathscr D=\mathscr D$. Given $j,n,s$, choose $\xi_{s,j,n}$ with $\|[U_s^*\xi_{s,j,n}]-v_j\|<1/(2n)$. Continuity gives a neighborhood of $s$ where the distance is less than $1/n$. Finitely many such neighborhoods cover $C$.

Collect their selected vectors for every pair $j,n$ into a countable subset $\mathscr D_C\subseteq\mathscr D$. It satisfies

<a id="equation-m15"></a>

$$ \inf_{\xi\in\mathscr D_C}
       \|[U_s^*\xi]-v_j\|=0
       \qquad(s\in C,\ j\geq1). \tag{M15} $$

Neither $G$, $\mathcal L$ nor $K$ has been assumed separable. Compactness of $C$, continuity of the smoothed fields and the local separable range of this one $\theta$ give precisely the countable tests needed.

If $\theta$ is orthogonal to the range of $W$, it is also orthogonal to every $\pi_{\mathrm{ind}}(Qf)W\xi$. The induced pairing of lesson 44 and (M11) then imply

<a id="equation-m16"></a>

$$ \int_G f(s)\langle[U_s^*\xi],\theta(s)\rangle\,ds=0
      \qquad(f\in C_c(G),\ \xi\in\mathscr D). \tag{M16} $$

For each $\xi\in\mathscr D_C$, its locally integrable coefficient in (M16) vanishes locally almost everywhere. Remove their countable union of exceptional sets on $C$, along with the exception for $\theta(s)\in E_C$. At a remaining $s$, (M15) gives $\langle v_j,\theta(s)\rangle=0$ for every $j$. Since $\theta(s)\in E_C$, it follows that $\theta(s)=0$. This holds almost everywhere on each compact, so $\theta$ is locally zero and has zero induced norm by (I3) of lesson 44. The range of the isometry $W$ is closed and has zero orthogonal complement. Therefore $W$ is surjective and is a unitary equivalence of covariant systems.

<a id="oa-flow.impr.uniqueness"></a>

## Uniqueness of the inducing representation

The construction of $K$ and $V$ used only $(\pi,U)$, so it is canonical up to the unitary completion of a positive form. To see directly that it recovers a previously given subgroup representation $V_0$, apply it to the induced system of lesson 44. The full smoothing proof in [the preceding chapter](OA-FLOW-L44.md#oa-flow.ind.smoothing) gives continuous induced fields. Their lifted scalar measures have density

<a id="equation-m17"></a>

$$ k_{\xi,\eta}(s)=\langle\xi(s),\eta(s)\rangle,
       \qquad \xi,\eta\in\mathscr D. \tag{M17} $$

Consequently $B(\xi,\eta)=\langle\xi(e),\eta(e)\rangle$. Evaluation at $e$ identifies the completed quotient with the closure of $\{\xi(e):\xi\in\mathscr D\}$. This closure is all of the original inducing Hilbert space: for the elementary fields of lesson 44, $A(f,\eta)(e)=\int_H\chi(h)^{1/2}f(h)V_0(h)\eta\,dh$. [QF1](OA-FLOW-QF.md#qf-1) extends compactly supported approximate-identity kernels on $H$ to $C_c(G)$; the resulting elementary fields approximate $\eta$ at $e$. Convolving an elementary field with a group approximate identity places it in $\mathscr D$ and preserves its value at $e$ in the limit. Thus evaluation is a unitary.

Under that unitary, the recovered action (M10) is $V_0$: the induced covariance gives $\xi(h^{-1})=\chi(h)^{1/2}V_0(h)\xi(e)$, so

<a id="equation-m18"></a>

$$ \chi(h)^{-1/2}(U_h\xi)(e)
     =\chi(h)^{-1/2}\xi(h^{-1})
     =V_0(h)\xi(e). \tag{M18} $$

Therefore two subgroup representations inducing equivalent covariant systems are unitarily equivalent. This proves the converse imprimitivity theorem and uniqueness for every locally compact Hausdorff $G$, closed $H$ and Hilbert space $\mathcal L$.

**Problem.** Why would taking an arbitrary measurable fiber of the spectral representation at $eH$ fail to reconstruct $V$?

**Solution.** A measurable field is defined only almost everywhere in $G/H$, and a single coset may have measure zero. Its fiber can be changed without changing the covariant representation. The continuous densities of smoothed vectors give a canonical positive form at $e$, so (M6) has meaning independent of that arbitrary null-set choice.

The classical source is M. Takesaki, *Theory of Operator Algebras II*, Theorem X.4.7, printed pages296–299 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The reconstruction retains its continuous-density route. The written local proof additionally makes the finite measure restrictions, compressed-action argument, compactwise countable tests and compact extension used for uniqueness explicit. It has arbitrary locally compact Hausdorff group and arbitrary Hilbert-space scope.
