# Ergodic factors and trace normalization

**Self-checked by the writing AI.**

A finite invariant functional rules out the trace-scaling freedom of an automorphism on a semifinite factor. Once this is proved, ergodicity forces its possibly unbounded trace density to be scalar. The source target is Takesaki, *Theory of Operator Algebras II*, Exercise VIII.3(4). Exercises VIII.3(5) and (9) retain their separate solution obligations.

Inputs are WG-008's finite positive cutoffs, PT-08's full trace-density theorem, VE-01's uniqueness up to scale on a factor, SF-12's standard implementation, and SK-05–08's Borel calculus, domains and spectral transport. All weight identities on positive elements include infinite values. A normal automorphism means a normal unital *-automorphism.

One additional input, **FT-DEP-FACTOR-TRACE**, is stated exactly in FT-01: a nonzero factor with a nonzero finite projection admits a faithful normal semifinite trace. Its primary locators are Takesaki, *Theory of Operator Algebras I*, Corollary V.1.20 and Theorem V.2.15, printed pages 297 and 317. The exact programme trace-existence proof is imported at The programme arbitrary-algebra trace-existence theorem through Exact theorem owners and the FT/MB applications, and its factor consequence is recorded there. The complete existing affine group proof is reproduced with attribution at TE-14–16. TE-01 names the written programme predual compactness proof and its Banach foundations. The exercise below uses that precise factor consequence. The prerequisites of these imported proofs are not proved here.

## Finite projections and the exact trace-existence input

A projection \(e\in M\) is **finite** if

\[
 v^*v=e,\quad vv^*=f\leq e,\quad v\in M
 \quad\Longrightarrow\quad f=e.
 \tag{FT.1}
\]

An algebra is of type III when it has no nonzero finite projection. A factor has scalar center. These are the projection and type conventions of Takesaki I, Definitions V.1.15 and V.1.17.

Here is the trace direction with its corner argument included. Suppose \(\tau\) is a faithful normal semifinite trace and \(\tau(e)<\infty\). For a partial isometry as in (FT.1), the trace identity gives \(\tau(f)=\tau(vv^*)=\tau(v^*v)=\tau(e)\). Additivity on \(e=f+(e-f)\), finite subtraction and faithfulness imply \(e=f\). Thus every finite-trace projection is finite in the projection sense.

In fact every nonzero projection \(e\) dominates such a nonzero projection. Choose finite positive contractions \(q_i\uparrow1\) from WG-008. The positive elements \(y_i=e q_i e\) converge strongly to \(e\), and

\[
 \tau(y_i)=\tau(q_i^{1/2}e q_i^{1/2})
            \leq\tau(q_i)<\infty.
 \tag{FT.2}
\]

The equality uses the trace identity on the bounded operator \(q_i^{1/2}e\). Some \(y_i\ne0\). Choose \(\delta>0\) so that \(f=1_{[\delta,\infty)}(y_i)\ne0\). Spectral calculus gives \(f\leq e\) and \(\delta f\leq y_i\), hence \(\tau(f)\leq\delta^{-1}\tau(y_i)<\infty\). The first paragraph makes \(f\) finite. In particular a nonzero algebra carrying such a trace cannot be type III; the same argument excludes any nonzero type III central summand. The use of the trace in (FT.2) matters: this is not a general corner assertion for an arbitrary semifinite weight.

The input used in the other direction is precisely

\[
 \begin{gathered}
 M\ne0\text{ a factor},\quad
 \exists e\ne0\text{ finite in }M\\
 \Longrightarrow\quad
 \exists\tau\text{ faithful normal semifinite trace on }M.
 \end{gathered}
 \tag{FT.3}
\]

**FT-DEP-FACTOR-TRACE** is the factor consequence recorded in Exact theorem owners and the FT/MB applications of the exact programme arbitrary-algebra equivalence imported at The programme arbitrary-algebra trace-existence theorem. The trace course, Theorem 6.7, owns the existence proof; Lemma 6.1 and Theorem 6.2 give its full normal corner-extension input. The complete existing affine group proof is reproduced with attribution in TE-14–16. TE-01 routes the unrestricted predual compactness clause to the written programme proof in PD-17 and its Banach foundations. The trace direction just written remains a separate direct argument.

## Automorphisms transport the density and the trace scale

Let \(M\ne0\) be a factor carrying a faithful normal semifinite trace \(\tau\). Any other faithful normal semifinite trace has trivial modular group by PT-08 and therefore equals \(c\tau\), for a unique \(c>0\), by VE-01. For a normal automorphism \(\alpha\), the weight \(\tau\circ\alpha\) is a faithful normal semifinite trace: faithfulness, normality and the trace identity transport directly, while \(\alpha^{-1}(q_i)\uparrow1\) transports the finite cutoffs. Consequently there is a unique positive number \(c_\alpha\) with

\[
 \tau\circ\alpha=c_\alpha\tau,\qquad
 c_{\alpha\beta}=c_\alpha c_\beta.
 \tag{FT.4}
\]

No invariance of \(\tau\) under \(\alpha\) has been presumed.

Write a faithful normal semifinite weight as \(\varphi=\tau_h\), using PT-08. Its density \(h\) is positive, self-adjoint, injective and affiliated with \(M\). To specify the automorphism on unbounded operators, work in standard form and use SF-12's canonical unitary \(U_\alpha\). Define

\[
 \alpha(h)=U_\alpha hU_\alpha^*,\qquad
 D(\alpha(h))=U_\alpha D(h),\qquad
 E_{\alpha(h)}(B)=\alpha(E_h(B)).
 \tag{FT.5}
\]

SK-08 proves this spectral transport; the same convention applies to every Borel function of \(h\). In particular it transports square roots and \(h_\varepsilon=h(1+\varepsilon h)^{-1}\).

Put \(H=\alpha^{-1}(h)\). On every \(x\in M_+\), the bounded regularizations in PT-08 give

\[
 \begin{aligned}
 (\tau_h\circ\alpha)(x)
 &=\sup_{\varepsilon>0}
       (\tau\circ\alpha)(H_\varepsilon^{1/2}xH_\varepsilon^{1/2})\\
 &=c_\alpha\tau_H(x)
  =\tau_{c_\alpha H}(x).
 \end{aligned}
 \tag{FT.6}
\]

The last equality uses \((cH)_\varepsilon=cH_{c\varepsilon}\) and reindexes the supremum. Thus it is an equality on all positives, rather than only on a finite ideal. If \(\varphi\circ\alpha=\varphi\), density uniqueness in PT-08 gives

\[
 h=c_\alpha\alpha^{-1}(h),\qquad
 \alpha(h)=c_\alpha h.
 \tag{FT.7}
\]

These are equalities of closed operators with their full domains. In particular \(U_\alpha D(h)=D(h)\).

## Finite mass eliminates a nontrivial scaling character

Now assume \(\varphi\) is a faithful normal positive functional and \(\varphi\circ\alpha=\varphi\). Since \(M\ne0\), its mass satisfies \(0<\varphi(1)<\infty\). We will prove \(c_\alpha=1\), without assuming \(\tau(1)<\infty\) or that \(h\) is bounded.

Injectivity of \(h\) makes \(A=\log h\) a densely defined self-adjoint operator. Its domain is the spectral domain
\(\{\xi:\int_{(0,\infty)}|\log s|^2\,d\langle E_h(s)\xi,\xi\rangle<\infty\}\).
Equation (FT.7) and spectral transport give

\[
 \alpha(A)=A+\delta I,\qquad
 \delta=\log c_\alpha.
 \tag{FT.8}
\]

This equality retains the full domain \(D(A)\). Suppose \(\delta\ne0\), and set \(\ell=|\delta|\). For \(k\in\mathbb Z\), let

\[
 I_k=[k\ell,(k+1)\ell),\qquad P_k=1_{I_k}(A),
 \qquad \alpha(P_k)=P_{k-\operatorname{sgn}(\delta)}.
 \tag{FT.9}
\]

The sign follows because \(1_{I_k}(A+\delta I)=1_{I_k-\delta}(A)\). The projections are mutually orthogonal and sum strongly to 1. Normality and positivity of the functional therefore give

\[
 \sum_{k\in\mathbb Z}\varphi(P_k)=\varphi(1)\in(0,\infty).
 \tag{FT.10}
\]

Invariance under \(\alpha\) makes all the nonnegative summands equal. If their common value is zero, (FT.10) has zero right side. If it is positive, the sum is infinite. Both contradict (FT.10). Hence

\[
 c_\alpha=1,\qquad \tau\circ\alpha=\tau,
 \qquad\alpha(h)=h.
 \tag{FT.11}
\]

The finite mass used here is \(\varphi(1)\), not the trace's total mass. The countable partition is the spectral partition of one self-adjoint operator; it requires no separability or sequence of finite projections exhausting the algebra.

## Ergodic invariance forces a trace or type III

**Theorem, Exercise VIII.3(4), at FT-DEP-FACTOR-TRACE.** Let \(M\ne0\) be a factor and \(\varphi\in M_*^+\) faithful. Put

\[
 \operatorname{Aut}_\varphi(M)
    =\{\alpha\in\operatorname{Aut}(M):\varphi\circ\alpha=\varphi\}.
 \tag{FT.12}
\]

Suppose this group acts ergodically, meaning that its fixed algebra is \(\mathbb C1\). Then \(\varphi\) is a trace or \(M\) is of type III.

**Proof.** If \(M\) is type III, the alternative holds. Otherwise the definition in FT-01 supplies a nonzero finite projection. Invoke the exact structural input (FT.3) to choose a faithful normal semifinite trace \(\tau\), and write \(\varphi=\tau_h\). For every \(\alpha\in\operatorname{Aut}_\varphi(M)\), FT-03 gives \(\alpha(h)=h\). Its bounded spectral projections

\[
 p_n=1_{[1/n,n]}(h)\quad(n\geq1)
 \tag{FT.13}
\]

are therefore fixed by every such automorphism. Ergodicity gives \(p_n\in\{0,1\}\). Since \(h\) is injective, \(p_n\uparrow1\). They cannot all be zero, so \(p_n=1\) for some \(n\). Spectral calculus now makes \(h\) a bounded element of \(M\), defined on the whole Hilbert space, with \(n^{-1}1\leq h\leq n1\). Its inverse is bounded as well. Only at this point may ergodicity be applied to \(h\) itself: \(h=a1\) for some \(a>0\). Thus on every positive element

\[
 \varphi=a\tau,\qquad \tau(1)=a^{-1}\varphi(1)<\infty.
 \tag{FT.14}
\]

The functional \(\varphi\) is a trace. FT-01 also shows that the identity projection is finite. \(\square\)

In particular an infinite semifinite factor cannot admit an ergodic group of automorphisms preserving a faithful normal positive functional. The proof needs neither a bounded density at the start nor a normalized state. Its one structural trace-existence input remains visible in (FT.3).

## Scope checks and examples

**A nontracial matrix functional is not ergodic.** In \(M_2(\mathbb C)\), let \(\tau=\operatorname{Tr}\), \(h=\operatorname{diag}(1,4)\), and \(\varphi(x)=\operatorname{Tr}(hx)\). FT-03 shows that every \(\varphi\)-preserving automorphism fixes \(h\), hence fixes the nontrivial projection \(E_{11}=1_{\{1\}}(h)\). Its fixed algebra is not scalar. The trace defect is explicit:

\[
 \varphi(E_{12}E_{21})=1,\qquad
 \varphi(E_{21}E_{12})=4.
 \tag{FT.15}
\]

This argument does not require a classification of matrix automorphisms.

**A faithful finite trace does give ergodicity on a factor.** Every inner automorphism \(x\mapsto uxu^*\) preserves such a trace. An element fixed by all these automorphisms commutes with every unitary. It therefore commutes with all of \(M\): a self-adjoint contraction \(b\) is the real part of the unitary \(b+i(1-b^2)^{1/2}\), and every element is a complex linear combination of self-adjoint contractions. The fixed algebra of \(\operatorname{Aut}_\varphi(M)\) is consequently contained in the center \(\mathbb C1\), and contains that center.

**Finite mass does not bound the density.** Here is a conditional spectral model that specifies all its hypotheses. Suppose a finite factor with normalized faithful normal trace \(\tau\) has mutually orthogonal projections \(p_n\), \(n\geq1\), with strong sum 1 and \(\tau(p_n)=3\,4^{-n}\). Define

\[
 h\xi=\sum_{n\geq1}2^n p_n\xi,\qquad
 D(h)=\left\{\xi:\sum_{n\geq1}4^n\|p_n\xi\|^2<\infty\right\}.
 \tag{FT.16}
\]

Spectral calculus makes \(h\) positive, self-adjoint, injective and affiliated. Each \(p_n\ne0\), so \(h\) is unbounded. Nevertheless PT-08 and normal monotone evaluation give

\[
 \tau(1)=\sum_{n\geq1}3\,4^{-n}=1,\qquad
 \tau_h(1)=\sum_{n\geq1}3\,2^{-n}=3.
 \tag{FT.17}
\]

Thus \(\tau_h\) is a faithful normal finite functional with unbounded density. Its invariant automorphisms fix each \(p_n\), so they cannot act ergodically. Existence of projections with these prescribed traces is a hypothesis of this example, not an additional theorem asserted here. The spectral domain and the exact sums explain why the boundedness step in FT-04 must come after ergodicity.

The accompanying reproducible draft figure shows the hypothetical logarithmic translation and its mass contradiction, the exact matrix density and fixed projection, and the conditional unbounded spectral model. These panels explain FT-03–05; they do not replace the all-positive transport identity or the full closed-operator domains in the proofs.

Compare Masamichi Takesaki, *Theory of Operator Algebras I*, Definitions V.1.15 and V.1.17; Corollary V.1.20; Theorem V.2.15. Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise VIII.3(4). The prose, proofs and figure are original.
