# Weights and semicyclic representations: the exact opening package

**Self-checked by the writing AI.**

This lesson gives the exact opening package for weights on an arbitrary von Neumann algebra: the three defining regularity conditions, the hereditary-cone algebra, the finite definition domain, the semicyclic quotient representation, and the factorization lemma controlling support projections. No separability, sigma-finiteness, faithful state, or countability assumption is made.

A freely accessible comparison is Brent Nelson, [*Tomita–Takesaki Theory*, Definitions 3.1, 3.3 and 3.5, Lemmas 3.2 and 3.6, and Proposition 3.4, pages 19–21](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf). The finite-cone algebra and all three factorization conclusions are proved below. We supply the finite linear extension, quotient, normality and faithfulness arguments that the notes abbreviate, and make the semifiniteness convention explicit. A source reference is not a substitute for any of these proofs.

The foundational statements already have exact course owners: the regularity definitions, hereditary-cone algebra, finite complex extension, Cauchy–Schwarz and null quotient, GNS semicyclic construction, normality, finite cutoffs and faithfulness. The support-normalized factorization lemma owns the single-factor statement below. These owners retain their statements; the local arguments are alternative proofs and a direct reconstruction from these free inputs. The coefficient check, the convention counterexample and the full strong-family and increasing-net conclusions remain explicit local material. No duplicate foundational completion is claimed.

The earlier bridges to the foundation statements, semifiniteness correction and solved comparison are by GPT-6.1 Sol (OpenAI), Ultra, October 2026, CC0. The current free-source reconstruction and added proof details are by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0. Earlier exposition and provider credits retain their existing licences.

The bounded inputs have exact written proofs: BK01 for Hilbert completion, bounded extensions, square roots and continuous calculus; BK02 for the bicommutant theorem; BK04 for arbitrary bounded increasing positive nets; BK06 for supports; and BK08 for testing commutation on unitaries. Inner products are linear in the first variable.

## Weights, semifiniteness, faithfulness, and normality

Let \(M\) be a von Neumann algebra. A **weight** on \(M\) is a map

\[
\varphi:M_+\longrightarrow[0,\infty]
\tag{WF.1}
\]

such that, for \(x,y\in M_+\) and \(\lambda\geq0\),

\[
\begin{aligned}
\varphi(x+y)&=\varphi(x)+\varphi(y),\\
\varphi(\lambda x)&=\lambda\varphi(x).
\end{aligned}
\tag{WF.2}
\]

The extended-real convention is \(0\cdot(+\infty)=0\). Put

\[
\begin{aligned}
\mathfrak p_\varphi&=\{x\in M_+:\\
 &\qquad\varphi(x)<\infty\}.
\end{aligned}
\tag{WF.3}
\]

The weight is:

1. **semifinite** when \(\operatorname{span}_{\mathbb C}\mathfrak p_\varphi\) is ultraweakly dense in \(M\), as in the existing finite-domain definition;
2. **faithful** when \(\varphi(x)>0\) for every nonzero \(x\in M_+\);
3. **normal** when, for every bounded increasing net \((x_i)\) in \(M_+\),

\[
\varphi\!\left(\sup_i x_i\right)=\sup_i\varphi(x_i).
\tag{WF.4}
\]

WF-02 identifies this span with the definition algebra \(\mathfrak m_\varphi\), so the condition is exactly the existing ultraweak-density definition. We take the closure of the span without adjoining a unit. Unital von Neumann generation by the finite cone is insufficient. Nelson’s Definition 3.1 uses the word “generates”; we use the stated finite-domain density condition throughout, rather than unital generation. Faithfulness, normality and semifiniteness are separate conditions.

**Why adjoining the identity is insufficient.** The following diagonal example is proved directly, including its representation, normality, and failure of finite-domain density. On the diagonal algebra, define

\[
\begin{gathered}
M=\mathbb C\oplus\mathbb C,\\
\varphi(a,b)=
\begin{cases}
a,&b=0,\\
+\infty,&b>0,
\end{cases}\\
(a,b\geq0).
\end{gathered}
\tag{WF.43}
\]

This is a weight. If both second coordinates are zero, additivity is ordinary scalar addition; otherwise at least one summand and their sum have infinite value. Positive homogeneity follows in the same two cases, while zero homogeneity uses the declared convention. It is faithful because a zero value forces both coordinates to vanish. It is normal for every bounded increasing positive net: if the limiting second coordinate is positive, some term has positive second coordinate and the weight supremum is infinite; otherwise every second coordinate is zero and normality reduces to the supremum of the first coordinates.

Its finite cone and finite domains are

\[
\begin{gathered}
\mathfrak p_\varphi=\{(a,0):a\geq0\},\\
\mathfrak n_\varphi=\mathfrak m_\varphi
=\mathbb C\oplus0,\\
H_\varphi=\mathbb C,\\
\pi_\varphi(z,w)\xi=z\xi.
\end{gathered}
\tag{WF.44}
\]

Indeed, the weight of a square is finite precisely when its second coordinate is zero; the null ideal is zero, and the first-coordinate map is an isometry onto the displayed GNS space. Left multiplication gives the displayed representation, which kills the entire second summand. Meanwhile the finite cone contains the projection \((1,0)\), and adjoining the identity also gives \((0,1)\), so its unital generated von Neumann algebra is all of \(M\). Its complex span is nevertheless the proper, ultraweakly closed first-coordinate ideal. Thus the weight is not semifinite, despite its normality, faithfulness and unital generation. Every finite positive contraction has second coordinate zero, so no net of such contractions can converge strongly to the identity. This is consistent with the cutoff characterization and the corrected faithfulness theorem below.

## A hereditary cone generates its left ideal and definition algebra

This is the statement of the existing hereditary-cone proposition and its full generality corollary. Compare Nelson’s Lemma 3.2, whose polarization and order arguments work for an arbitrary hereditary cone.

Let \(P\subseteq M_+\) be a nonempty hereditary convex subcone:

\[
\begin{gathered}
P+P\subseteq P,\\
\lambda P\subseteq P\quad(\lambda\geq0),\\
0\leq y\leq x\in P\\
\Longrightarrow y\in P.
\end{gathered}
\tag{WF.5}
\]

Define

\[
\begin{aligned}
\mathfrak n_P&=\{x\in M:x^*x\in P\},\\
\mathfrak m_P&=\operatorname{span}_{\mathbb C}\\
 &\quad\{y^*x:x,y\in\mathfrak n_P\}.
\end{aligned}
\tag{WF.6}
\]

Then \(\mathfrak n_P\) is a left ideal, \(\mathfrak m_P\) is a hereditary star-subalgebra,

\[
\mathfrak m_P\cap M_+=P,
\tag{WF.7}
\]

and every element of \(\mathfrak m_P\) is a complex linear combination of four elements of \(P\).

**Proof.** If \(x,y\in\mathfrak n_P\), then

\[
\begin{gathered}
(x+y)^*(x+y)\leq\\
2(x^*x+y^*y)\in P.
\end{gathered}
\tag{WF.8}
\]

Heredity gives \(x+y\in\mathfrak n_P\); scalar closure is immediate. For \(a\in M\),

\[
(ax)^*(ax)\leq\|a\|^2x^*x\in P,
\tag{WF.9}
\]

so \(ax\in\mathfrak n_P\). Thus \(\mathfrak n_P\) is a left ideal.

Taking adjoints preserves the span in (WF.6). For four vectors in the ideal,

\[
(y^*x)(v^*u)=y^*\bigl((xv^*)u\bigr),
\tag{WF.10}
\]

and \((xv^*)u\in\mathfrak n_P\) by the left-ideal property. Hence
\(\mathfrak m_P\) is a star-subalgebra. Put \(z_k=x+i^k y\). The polarization identity

\[
4y^*x=\sum_{k=0}^3i^kz_k^*z_k.
\tag{WF.11}
\]

shows that \(\mathfrak m_P=\operatorname{span}_{\mathbb C}P\). The reverse inclusion uses
\(a=(a^{1/2})^*a^{1/2}\) for \(a\in P\).

It remains to identify the positive cone. Let
\(h=\sum_{k=1}^n y_k^*x_k\in\mathfrak m_P\cap M_+\). Put \(u_k=x_k+y_k\) and \(v_k=x_k-y_k\). Since \(h=h^*\),

\[
h=\frac14\sum_{k=1}^n(u_k^*u_k-v_k^*v_k).
\tag{WF.12}
\]

Set

\[
b=\frac14\sum_{k=1}^nu_k^*u_k\in P.
\tag{WF.13}
\]

Equation (WF.12) gives \(b-h\in P\subseteq M_+\), so
\(0\leq h\leq b\). Heredity yields \(h\in P\), proving (WF.7). It also proves that the star-subalgebra is hereditary.

Finally, because \(\mathfrak m_P=\operatorname{span}_{\mathbb C}P\), grouping positive and negative real and imaginary coefficients expresses any \(z\in\mathfrak m_P\) as

\[
z=a-b+i(c-d).
\tag{WF.14}
\]

Here \(a,b,c,d\in P\). This is the asserted four-element decomposition. \(\square\)

**Coefficient check.** Replacing the coefficient in (WF.12) by \(1/2\) would give \(2h\), as direct expansion of the two squares shows. The coefficient \(1/4\) is required and agrees with the complete calculation in Nelson’s Lemma 3.2. Here heredity of the subalgebra concerns its positive cone; no norm-closedness is asserted.

## The definition subalgebra and finite linear extension

The existing finite-domain extension also proves this statement. We give the direct four-positive-elements argument, including independence of the decomposition; Nelson’s Definition 3.3 states the extension without these details.

For a weight \(\varphi\), its finite cone is hereditary: if \(0\leq a\leq b\), then additivity in \(b=a+(b-a)\) gives \(\varphi(a)\leq\varphi(b)\). Additivity and homogeneity preserve finite values, and zero homogeneity gives \(\varphi(0)=0\). Thus apply WF-02 to \(P=\mathfrak p_\varphi\) and write

\[
\begin{aligned}
\mathfrak n_\varphi&=\{x\in M:\\
 &\qquad\varphi(x^*x)<\infty\},\\
\mathfrak m_\varphi&=\operatorname{span}_{\mathbb C}\\
 &\quad\{y^*x:x,y\in\mathfrak n_\varphi\}.
\end{aligned}
\tag{WF.15}
\]

The hereditary star-subalgebra \(\mathfrak m_\varphi\) is the **definition domain**, or **definition subalgebra**, of \(\varphi\). Its positive cone is exactly
\(\mathfrak p_\varphi\).

There is a unique positive complex-linear functional

\[
\widetilde\varphi:\mathfrak m_\varphi\longrightarrow\mathbb C
\tag{WF.16}
\]

whose restriction to \(\mathfrak p_\varphi\) is \(\varphi\).

**Proof of the extension.** Every self-adjoint \(h\in\mathfrak m_\varphi\) has a decomposition
\(h=a-b\) with \(a,b\in\mathfrak p_\varphi\): average its four-term decomposition (WF.14) with its adjoint to remove the imaginary part. Define
\(\widetilde\varphi(h)=\varphi(a)-\varphi(b)\). If
\(a-b=c-d\), then \(a+d=c+b\), and all four weight values are finite. Additivity of \(\varphi\) gives

\[
\begin{gathered}
\varphi(a)-\varphi(b)=\\
\varphi(c)-\varphi(d).
\end{gathered}
\tag{WF.17}
\]

Thus the definition is independent of the decomposition and is real-linear on the self-adjoint part: add decompositions for additivity, scale their two positive terms for positive homogeneity, and swap the two terms for negative scalars. For

\[
z=\frac{z+z^*}{2}
+i\,\frac{z-z^*}{2i},
\tag{WF.18}
\]

define its value as the value on the first self-adjoint part plus \(i\) times the value on the second. Multiplication by \(i\) sends the pair of parts \((h,k)\) to \((-k,h)\), proving complex linearity. Adjoint sends it to \((h,-k)\), so the extension preserves adjoints by complex conjugation. Positivity follows from
\((\mathfrak m_\varphi)_+=\mathfrak p_\varphi\), and uniqueness follows because that cone linearly spans the domain. \(\square\)

## The semicyclic quotient representation

The existing general-weight construction supplies the null quotient, bounded left action, normality and faithfulness statements. Their hypotheses stay separate in the alternative proof below.

Define the null left ideal

\[
\begin{aligned}
N_\varphi&=\{x\in M:\\
 &\qquad\varphi(x^*x)=0\}\\
 &\subseteq\mathfrak n_\varphi.
\end{aligned}
\tag{WF.19}
\]

On \(\mathfrak n_\varphi/N_\varphi\), set

\[
\begin{aligned}
\langle\eta_\varphi(x),\eta_\varphi(y)\rangle
 &=\widetilde\varphi(y^*x),\\
\eta_\varphi(x)&=x+N_\varphi.
\end{aligned}
\tag{WF.20}
\]

Let \(H_\varphi\) be its Hilbert completion. The left action extends to

\[
\pi_\varphi(a)\eta_\varphi(x)=\eta_\varphi(ax).
\tag{WF.21}
\]

The left-action identity holds for \(a\in M\) and \(x\in\mathfrak n_\varphi\). If \(\varphi\) is normal and semifinite, then
\(\pi_\varphi:M\to B(H_\varphi)\) is a nondegenerate normal star-representation. If \(\varphi\) is also faithful, then \(\pi_\varphi\) is faithful.

**Proof.** Positivity of \(\widetilde\varphi\), applied to
\((x+zy)^*(x+zy)\), gives the Cauchy–Schwarz inequality

\[
\begin{aligned}
\left|\widetilde\varphi(y^*x)\right|^2
 &\leq\\
 &\quad\varphi(x^*x)\varphi(y^*y).
\end{aligned}
\tag{WF.22}
\]

Here is the scalar minimization, including the null case. Put \(A=\varphi(x^*x)\), \(C=\varphi(y^*y)\), and \(b=\widetilde\varphi(y^*x)\). All are finite, and positivity says

\[
 0\leq A+z\overline b+\overline z b+|z|^2C.
\]

If \(C>0\), substitute \(z=-b/C\). If \(C=0\) and \(b\ne0\), substitution of \(z=-r b\) for arbitrarily large positive \(r\) gives a contradiction. This proves (WF.22) in both cases. Sesquilinearity and conjugate symmetry follow from WF-03. Null vectors are orthogonal to the whole domain, so their sums and scalar multiples remain null. Inequality (WF.23) makes this null space a left ideal. The quotient form is therefore independent of both representatives. Hilbert completion and extension of bounded maps from a dense subspace are supplied by BK01.

Hence the zero-length vectors form the radical of the form, so (WF.20) is a genuine inner product on the quotient. The inequality

\[
(ax)^*(ax)\leq\|a\|^2x^*x
\tag{WF.23}
\]

shows that (WF.21) is well defined and bounded by \(\|a\|\). Multiplication and linearity hold on the dense quotient range. Moreover, abbreviate \(\xi_x=\eta_\varphi(x)\). Then

\[
\begin{gathered}
\langle\pi_\varphi(a)\xi_x,\xi_y\rangle\\
 =\widetilde\varphi(y^*ax)\\
 =\langle\xi_x,\pi_\varphi(a^*)\xi_y\rangle.
\end{gathered}
\tag{WF.24}
\]

Thus \(\pi_\varphi(a)^*=\pi_\varphi(a^*)\). Since
\(\pi_\varphi(1)=I\), the representation is nondegenerate. This includes the zero Hilbert space, whose identity operator is zero.

For normality, let \(0\leq a_i\uparrow a\) in \(M\). For
\(x\in\mathfrak n_\varphi\),

\[
\begin{gathered}
x^*a_i x\uparrow x^*ax,\\
\varphi(x^*a_i x)\uparrow\varphi(x^*ax).
\end{gathered}
\tag{WF.25}
\]

The congruence convergence in (WF.25) is BK04. Its weight values are finite, since \(x^*a_i x\leq x^*ax\leq\|a\|x^*x\). Additivity therefore permits subtraction of these finite values, with no infinite subtraction. Put \(D_i=\pi_\varphi(a-a_i)\). Then \(0\leq D_i\leq\|a\|I\), and

\[
\left\langle D_i\eta_\varphi(x),\eta_\varphi(x)\right\rangle
\longrightarrow0.
\tag{WF.26}
\]

Since \(D_i^2\leq\|a\|D_i\), equation (WF.26) implies
\(D_i\eta_\varphi(x)\to0\). Density and the uniform norm bound extend this to every vector in \(H_\varphi\). Therefore
\(\pi_\varphi(a_i)\uparrow\pi_\varphi(a)\) strongly. The proved bounded positive-map equivalence NP04 gives ultraweak continuity, hence normality. Its proof uses algebraic GNS construction through WG006, so this invocation does not assume normality of the representation being constructed.

For faithfulness, apply the complete finite-cutoff characterization with the ultraweak-density definition above. It supplies an increasing net \((e_j)\subseteq\mathfrak p_\varphi\) of positive contractions with \(e_j\uparrow1\). Since \(e_j^2\leq e_j\), each cutoff also lies in \(\mathfrak n_\varphi\). If \(\pi_\varphi(c)=0\), then

\[
\begin{aligned}
0&=\|\eta_\varphi(ce_j)\|^2\\
 &=\varphi(e_jc^*ce_j).
\end{aligned}
\tag{WF.27}
\]

Faithfulness gives \(ce_j=0\). Strong convergence \(e_j\to1\) now yields \(c=0\). \(\square\)

The construction is nondegenerate for every weight because its identity acts as the Hilbert-space identity. Normality of the representation uses normality of the weight alone. Its faithfulness uses faithfulness and the exact finite-cutoff consequence of semifiniteness; normality is not needed for that particular implication. The two-coordinate example above shows why unital generation cannot supply the missing cutoffs.

## Abstract semicyclic representations

This elaborates the existing semicyclic module convention and Nelson’s Definition 3.5. It is not a new representation theorem.

The triple

\[
(\pi_\varphi,H_\varphi,\eta_\varphi)
\tag{WF.28}
\]

constructed in WF-04 is the **semicyclic representation associated with**
\(\varphi\).

More generally, a semicyclic representation of \(M\) is a triple
\((\pi,H,\eta)\) consisting of:

1. a representation \(\pi:M\to B(H)\);
2. a left ideal \(\mathfrak n\subseteq M\);
3. a linear map \(\eta:\mathfrak n\to H\) with dense range;

such that

\[
\pi(a)\eta(x)=\eta(ax).
\tag{WF.29}
\]

The displayed identity holds for every \(a\in M\) and \(x\in\mathfrak n\). This definition asserts the module covariance and dense range. It does not silently add closedness of \(\eta\), faithfulness of \(\pi\), or the existence of a single cyclic vector.

## Dominated factorizations and strong support limits

Part (i) is the existing support-normalized factorization lemma. Parts (ii) and (iii) give the full-family and increasing-net conclusions of Nelson’s Lemma 3.6; they are not collapsed into a single-factor import.

Let \(M\subseteq B(H)\) be a von Neumann algebra.

**(i) Single factorization.** If \(x,y\in M\) satisfy
\(y^*y\leq x^*x\), then there is a unique contraction \(s\in M\) such that

\[
y=sx,
\qquad
s\big|_{\overline{xH}^{\,\perp}}=0.
\tag{WF.30}
\]

**(ii) A strongly summable family.** Suppose \((x_i)_{i\in I}\subseteq M\) and

\[
a=\sum_{i\in I}x_i^*x_i
\tag{WF.31}
\]

in the strong topology, where the sum is the increasing net of finite partial sums. Let \(s_i\) be the contraction from (i) determined by

\[
\begin{gathered}
x_i=s_i a^{1/2},\\
s_i\big|_{\overline{aH}^{\,\perp}}=0.
\end{gathered}
\tag{WF.32}
\]

Then

\[
\sum_{i\in I}s_i^*s_i
\tag{WF.33}
\]

converges strongly to the range projection \(p=s(a)\).

**(iii) An increasing positive net.** Suppose
\((x_i)\) is a bounded increasing net in \(M_+\), with
\(x=\sup_i x_i\), and let \(s_i\) be determined by

\[
\begin{gathered}
x_i^{1/2}=s_i x^{1/2},\\
s_i\big|_{\overline{xH}^{\,\perp}}=0.
\end{gathered}
\tag{WF.34}
\]

Then \((s_i^*s_i)\) is increasing,

\[
\begin{gathered}
\sup_i s_i^*s_i=s(x),\\
s_i\longrightarrow s(x)\quad\text{strongly}.
\end{gathered}
\tag{WF.35}
\]

**Proof of (i).** Define \(s_0(x\xi)=y\xi\) on \(xH\). The order inequality gives

\[
\|y\xi\|^2\leq\|x\xi\|^2,
\tag{WF.36}
\]

so \(s_0\) is well defined and contractive. Extend it to
\(\overline{xH}\) and set it equal to zero on the orthogonal complement. This gives the unique operator satisfying (WF.30).

Every unitary \(u\in M'\) preserves \(\overline{xH}\) and its orthogonal complement: both \(u\) and \(u^*\) commute with \(x\). The operators
\(s\) and \(usu^*\) have the same action on \(xH\) and both vanish on its orthogonal complement, so uniqueness gives \(usu^*=s\). Thus \(s\) commutes with every unitary of \(M'\), hence lies in
\((M')'=M\). The implication from unitaries to the whole commutant is BK08, and the final equality is BK02.

**Proof of (ii).** Each inequality \(x_i^*x_i\leq a\) permits (i) with
\(x=a^{1/2}\). For a finite \(F\subseteq I\), put

\[
q_F=\sum_{i\in F}s_i^*s_i.
\tag{WF.37}
\]

If \(\eta=a^{1/2}\xi\), then

\[
\begin{aligned}
\langle q_F\eta,\eta\rangle
 &=\sum_{i\in F}\|s_i a^{1/2}\xi\|^2\\
 &=\sum_{i\in F}\langle x_i^*x_i\xi,\xi\rangle\\
 &\leq\langle a\xi,\xi\rangle\\
 &=\|\eta\|^2.
\end{aligned}
\tag{WF.38}
\]

The kernel and range identities in BK01 and BK06 give \(s(a^{1/2})=s(a)=p\). Hence the range of \(a^{1/2}\) is dense in \(pH\), and every \(s_i\) vanishes on
\((1-p)H\). Hence \(0\leq q_F\leq p\). The increasing net
\((q_F)\) has a strong limit \(q\leq p\) by BK04. Letting \(F\) exhaust \(I\) in
(WF.38) gives

\[
\langle q\eta,\eta\rangle=\|\eta\|^2.
\tag{WF.39}
\]

This equality holds for \(\eta\in a^{1/2}H\). Continuity on \(pH\) yields \(q=p\), proving (WF.33).

**Proof of (iii).** Part (i) supplies (WF.34). If \(i\leq j\) and
\(\eta=x^{1/2}\xi\), then

\[
\begin{aligned}
\langle s_i^*s_i\eta,\eta\rangle
 &=\langle x_i\xi,\xi\rangle\\
 &\leq\langle x_j\xi,\xi\rangle\\
 &=\langle s_j^*s_j\eta,\eta\rangle.
\end{aligned}
\tag{WF.40}
\]

Density in \(s(x)H\), together with vanishing on its orthogonal complement, proves
\(s_i^*s_i\leq s_j^*s_j\leq s(x)\). Its strong supremum \(q\) satisfies, with \(\eta=x^{1/2}\xi\),

\[
\begin{aligned}
\langle q\eta,\eta\rangle
 &=\sup_i\langle x_i\xi,\xi\rangle\\
 &=\langle x\xi,\xi\rangle.
\end{aligned}
\tag{WF.41}
\]

so \(q=s(x)\).

Finally, \(x_i^{1/2}\to x^{1/2}\) strongly by the following continuous-calculus argument. BK04 gives \(x_i\to x\) strongly and \(0\leq x_i\leq x\), with a common norm bound \(C=\|x\|\). If \(C=0\), all operators vanish. Otherwise bounded products preserve strong limits: for \(a_i\to a\), \(b_i\to b\) strongly and \(\sup_i\|a_i\|\leq K\),

\[
 \begin{aligned}
 \|(a_i b_i-ab)\xi\|
 &\leq K\|(b_i-b)\xi\|\\
 &\quad+\|(a_i-a)b\xi\|\longrightarrow0.
 \end{aligned}
\]

Induction gives convergence of every polynomial in \(x_i\). By the uniform polynomial approximation proved in BK01, choose a polynomial \(r\) within \(\varepsilon\) of the square-root function on \([0,C]\). The calculus norm bound then yields

\[
 \begin{aligned}
 \|(x_i^{1/2}-x^{1/2})\xi\|
 &\leq2\varepsilon\|\xi\|\\
 &\quad+\|(r(x_i)-r(x))\xi\|.
 \end{aligned}
\]

First let the directed index tend to its limit and then let \(\varepsilon\downarrow0\). This proves strong convergence for the original net without commutation between its terms or a countability assumption. Therefore, on the dense subspace
\(x^{1/2}H\subseteq s(x)H\),

\[
\begin{aligned}
s_i x^{1/2}\xi&=x_i^{1/2}\xi\\
 &\longrightarrow x^{1/2}\xi\\
 &=s(x)x^{1/2}\xi.
\end{aligned}
\tag{WF.42}
\]

The contractions \(s_i\) and \(s(x)\) vanish on
\((1-s(x))H\), so the convergence extends by density and uniform boundedness to every vector of \(H\). This proves the final assertion of (WF.35). \(\square\)

## Source and completion boundary

WF-01 through WF-06 reconstruct the weight-domain, semicyclic and factorization package using the free Nelson passages and the named existing WG and DW providers. Their foundational statements belong to those WG and DW lessons; the local proofs are alternative proofs, alongside the explicit convention counterexample and full strong-family and increasing-net conclusions. WF-02 checks the scalar coefficient by expansion; WF-04 supplies the complete quotient and normality argument, and WF-06 proves the continuous-calculus convergence needed for its final support limit. The lesson relies only on the visible bounded-operator, weight-domain, and finite-cutoff prerequisites already present in the course.
