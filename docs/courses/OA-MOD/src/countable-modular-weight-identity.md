# Countable modular sums and the boundary of finite-weight tests

An analytic identity can determine a weight on every element where a
reference weight is finite, yet miss an infinite value. This distinction
matters when constructing operator-valued weights: their scalar
composites must agree on the entire positive cone. We prove the safe
part of the countable modular test, then build a counterexample from
two closed forms on the same Hilbert space. All Hilbert inner products
are linear in the first variable.

## What the analytic strong sum actually proves

Let \(\varphi\) be a faithful normal semifinite weight on a von Neumann
algebra \(M\). Write \(\mathfrak n_\varphi\), \(H_\varphi\),
\(\Lambda_\varphi\), \(J_\varphi\), and \(\sigma^\varphi\) for its GNS
and modular data. Given a sequence \((a_j)_{j\geq1}\subset M\), define
the normal weight for \(X\in M_+\) by

\[
\begin{gathered}
\Psi_A(X)=\sum_{j\geq1}\\
\varphi(a_jXa_j^*).
\end{gathered}
\tag{ACI.1}
\]

The sum is the supremum of its finite partial sums; normality follows
from normality of each summand and interchange of two directed
positive suprema.

The fixed-operator theorem proved in
HS02–03,
corresponding to Takesaki II, VIII.3.18(i)–(ii), says that
the global inequality
\(\varphi(aXa^*)\leq\varphi(X)\) for every
\(X\in M_+\) is equivalent to a bounded negative-half-strip modular
orbit of \(a\), with endpoint
\(b=\sigma^\varphi_{-i/2}(a)\) satisfying \(\|b\|\leq1\).
Under these conditions it also gives the typed right-action formula

\[
\begin{gathered}
x\in\mathfrak n_\varphi
\Longrightarrow xa^*\in\mathfrak n_\varphi,\\
\Lambda_\varphi(xa^*)
=J_\varphi bJ_\varphi\Lambda_\varphi(x).
\end{gathered}
\tag{ACI.2}
\]

HS02 constructs the bounded commutant operator from the global inequality;
HS03 proves the converse and this identity on the whole finite left ideal.
The source's proof of IX.4.20 cites VIII.3.17 at this step;
VIII.3.18 is the direct fixed-operator statement.

Suppose first that \(\Psi_A=\varphi\) on all of \(M_+\). Each
summand in (ACI.1) is then at most \(\varphi\), so (ACI.2) gives
bounded endpoints \(b_j\). Put
\(B_k=\sum_{j=1}^k b_j^*b_j\) and
\(\eta_x=J_\varphi\Lambda_\varphi(x)\). For
\(x\in\mathfrak n_\varphi\), the right-action formula yields

\[
\begin{gathered}
\langle B_k\eta_x,\eta_x\rangle\\
=\sum_{j\leq k}\varphi(a_jx^*xa_j^*)\\
\leq\|\eta_x\|^2.
\end{gathered}
\tag{ACI.3}
\]

Density of the GNS vectors and the antiunitarity of \(J_\varphi\)
give \(0\leq B_k\leq1\). The assumed equality of weights turns
(ACI.3) into equality as \(k\to\infty\). Thus the increasing
contractions \(B_k\) converge strongly to \(1\): their quadratic
forms converge to the identity on a dense set, and
\((1-B_k)^2\leq1-B_k\). This is the valid forward implication.

Conversely, suppose each \(a_j\) has such a contractive analytic
endpoint and \(B_k\uparrow1\) strongly. Applying (ACI.2) again gives

\[
\begin{gathered}
\Psi_A(x^*x)=\|\eta_x\|^2\\
=\varphi(x^*x).
\end{gathered}
\tag{ACI.4}
\]

Here \(x\in\mathfrak n_\varphi\); the first equality follows
by taking the strong limit of \(B_k\) in (ACI.3).
Every positive \(X\) with \(\varphi(X)<\infty\) is \(x^*x\)
for \(x=X^{1/2}\in\mathfrak n_\varphi\). Hence the strong sum
proves equality on the **finite \(\varphi\)-cone**. It gives no
value at a positive \(X\) of infinite \(\varphi\)-weight.

**Nonfaithful weights and the support corner.** Let now \(\varphi\)
be normal and semifinite, with support \(e\). The support theorem
WS04–06 gives a faithful
normal semifinite restriction \(\varphi_e\) to \(eMe\) and
\(\varphi(X)=\varphi_e(eXe)\) for every \(X\in M_+\).
The zero weight has \(e=0\) and all the conclusions below are immediate.

For one multiplier \(a\), suppose first that
\(\varphi(aXa^*)\leq\varphi(X)\) on the entire positive cone.
Apply this to \(X=1-e\). Faithfulness on the corner gives
\[
 \begin{gathered}
 ea(1-e)a^*e=0,\\
 ea(1-e)=0.
 \end{gathered}
\]
Thus \(ea=eae\). Put \(c=eae\). For every positive \(X\),
\[
 \begin{aligned}
 \varphi(aXa^*)
 &=\varphi_e(eaXa^*e)\\
 &=\varphi_e(c(eXe)c^*).
 \end{aligned}
\]
The global domination is therefore equivalent to the two conditions
\(ea(1-e)=0\) and
\(\varphi_e(cYc^*)\leq\varphi_e(Y)\) for every \(Y\in(eMe)_+\).
Sufficiency follows from the displayed identity and the support formula.
HS02–03 applied to \(\varphi_e\) identify the latter condition with
the bounded corner orbit of \(c\), with endpoint \(b\in eMe\)
of norm at most one. Their right-action formula is on the GNS space
of this faithful corner:
\[
 \begin{gathered}
 x\in\mathfrak n_{\varphi_e}
 \Longrightarrow xc^*\in\mathfrak n_{\varphi_e},\\
 \Lambda_{\varphi_e}(xc^*)\\
 =J_{\varphi_e}bJ_{\varphi_e}\Lambda_{\varphi_e}(x).
 \end{gathered}
\]
No modular conjugation for a nonfaithful weight on all of \(M\)
has been presumed.

If \(\Psi_A=\varphi\) on all positive elements, apply the preceding
argument to every summand. It yields \(ea_j(1-e)=0\), the corner
multipliers \(c_j=ea_je\), and their endpoints \(b_j\).
The faithful argument in \(eMe\) proves
\(\sum_j b_j^*b_j=e\) strongly. Conversely, if these support and
corner strip conditions hold and the endpoint squares sum strongly
to \(e\), then for \(\varphi(X)<\infty\) the element \(eXe\)
has finite \(\varphi_e\)-weight. The faithful finite-cone calculation gives
\[
 \begin{aligned}
 \Psi_A(X)
 &=\sum_j\varphi_e(c_j(eXe)c_j^*)\\
 &=\varphi_e(eXe)=\varphi(X).
 \end{aligned}
\]
The support condition is essential: compressing \(a_j\) alone does
not discard its off-corner action on \(X\). This proves the full
support reduction for the forward and finite-cone statements.
The counterexample below already has support \(1\), so it still
refutes the all-positive reverse implication.

**The finite-domain boundary for arbitrary normal weights.** The
standing scalar-weight convention in Takesaki II, printed p. 57,
includes semifiniteness. The preceding statements display that
hypothesis explicitly. Here is the separate conclusion when it is
removed; it must not be obtained merely by renaming the support.

Let now \(\varphi\) be any normal weight. Use the projections of
WS02–06: \(e\) is the
finite-domain projection, \(f\leq e\) is the largest null projection,
and \(p=e-f\). The restriction \(\varphi_p\) to \(pMp\) is faithful,
normal and semifinite, including the zero corner. Its reconstruction
formula is

\[
\varphi(X)=
\begin{cases}
\varphi_p(pXp),&X=eXe,\\
\infty,&X\ne eXe.
\end{cases}
\tag{ACI.4a}
\]

Suppose \(a_j\in pMp\), as for the support-corner multipliers in
the printed lemma. Put

\[
\begin{aligned}
\Psi_p(Y)&=\sum_j\varphi_p(a_jYa_j^*),\\
&\hspace{2em}Y\in(pMp)_+.
\end{aligned}
\tag{ACI.4b}
\]

Since \(a_jXa_j^*=a_j(pXp)a_j^*\in(pMp)_+\), restriction gives
\(\Psi_A(X)=\Psi_p(pXp)\) for every positive \(X\).

Assume the corner orbits have bounded negative-half-strip
continuations and their endpoints satisfy
\(\sum_j b_j^*b_j=p\) strongly. Each endpoint is contractive in
\(pMp\). The faithful calculation (ACI.4) applied there yields
\(\Psi_p(Y)=\varphi_p(Y)\) whenever \(\varphi_p(Y)<\infty\).
If \(\varphi(X)<\infty\), (ACI.4a) gives \(X=eXe\) and
\(\varphi_p(pXp)<\infty\). Therefore

\[
\begin{gathered}
\Psi_A(X)=\varphi(X)\\
\text{whenever }\varphi(X)<\infty.
\end{gathered}
\tag{ACI.4c}
\]

Global equality has a further necessary condition. If \(e\ne1\),
take \(X=1-e\). Then \(\varphi(X)=\infty\) by (ACI.4a), but
every \(a_jXa_j^*\) is zero because \(a_j\in pMp\) and \(p\leq e\).
Thus \(\Psi_A(X)=0\). In particular, global equality forces
\(e=1\), hence semifiniteness. More precisely,

\[
\begin{gathered}
\Psi_A=\varphi\text{ on }M_+\\
\Longleftrightarrow\\
e=1\text{ and }\\
\Psi_p=\varphi_p\text{ on }(pMp)_+.
\end{gathered}
\tag{ACI.4d}
\]

Necessity of the corner identity follows by restricting to \(pMp\).
For sufficiency, \(e=1\) makes (ACI.4a) equal to
\(\varphi(X)=\varphi_p(pXp)\) for every \(X\geq0\); combine this
with the formula for \(\Psi_A\). Global equality also gives the
corner analytic endpoint condition by the faithful forward proof.
Neither (ACI.4c) nor that endpoint condition replaces the all-positive
corner equality in (ACI.4d).

For a concrete nonsemifinite example, take \(M=\mathbb C^2\) and
\(\varphi(s,t)=s+\infty\,t\) for \(s,t\geq0\), using
\(0\cdot\infty=0\). This weight is additive and homogeneous. It is
normal: if an increasing net has limit with positive second coordinate,
some member already has positive second coordinate; otherwise all
second coordinates vanish and normality is the scalar limit in the
first coordinate. Its finite-domain projection is \(e=(1,0)\), its
largest null projection is zero, and \(p=e\). Choose \(a_1=p\) and
\(a_j=0\) for \(j>1\). The corner modular flow is trivial, so the
endpoints are these same elements and their squares sum to \(p\).
Nevertheless \(\Psi_A(s,t)=s\), whereas
\(\varphi(0,1)=\infty\). The obstruction at \(1-e\) is distinct
from the infinite-value counterexample below, where \(e=p=1\).

The compact spectral argument in
Trace-class coordinates without separability
supplies the orthonormal eigenbasis used in the next construction.

## A one-dimensional extension of a closed form

Let \(H=\ell^2(\mathbb N)\) with standard basis \((e_n)\).
Write \(f_n=\langle f,e_n\rangle\) and
\(\lambda_n=n^2+3\). Define the diagonal operator by

\[
De_n=\lambda_ne_n.
\tag{ACI.5}
\]

For \(f\in H\), put
\(q_D(f)=\sum_n\lambda_n|f_n|^2\), allowing the value
\(\infty\). The form domain \(Q_D=\{f:q_D(f)<\infty\}\), with inner product
induced by \(q_D\), is a Hilbert space and \(q_D(f)\geq4\|f\|^2\).
Choose the unit vector

\[
\begin{gathered}
v=c\sum_{n\geq1}n^{-1}e_n,
\\
c^{-2}=\sum_{n\geq1}n^{-2}.
\end{gathered}
\tag{ACI.6}
\]

It lies in \(H\) but not in \(Q_D\), because the summands in
\(q_D(v)=c^2\sum_n(n^2+3)n^{-2}\) do not tend to zero.

Form the algebraic direct sum
\(Q_K=Q_D\oplus\mathbb Cv\). For \(f\in Q_D\), define

\[
\begin{gathered}
q_K(f+\alpha v)=\\
q_D(f)+4|\alpha|^2.
\end{gathered}
\tag{ACI.7}
\]

It extends \(q_D\) on its whole form domain, but
\(q_K(v)=4<\infty\). The decomposition is unique. Its direct-sum
form norm is complete, and its inclusion into \(H\) is continuous:

\[
\begin{aligned}
\|f+\alpha v\|^2
&\leq2\|f\|^2+2|\alpha|^2\\
&\leq q_D(f)+4|\alpha|^2.
\end{aligned}
\tag{ACI.8}
\]

Thus \(q_K\) is a densely defined closed positive form bounded
below by the Hilbert norm.

We construct its operator explicitly from a compact embedding. Let
\(j:(Q_K,q_K)\to H\) be the inclusion. The unit ball of \(Q_D\)
is relatively compact in \(H\): its tail past coordinate \(N\)
has squared norm at most \((N+1)^{-2}\), while its first \(N\)
coordinates form a bounded finite-dimensional set. Adding the
bounded one-dimensional \(\alpha v\) part preserves compactness.
Hence \(j\) is compact, injective, and has dense range. The positive
compact operator \(T=jj^*\) is injective. Let
\((v_j)_{j\geq1}\) be an orthonormal eigenbasis with
\(Tv_j=\mu_j^{-1}v_j\), where \(\mu_j\geq1\) and
\(\mu_j\to\infty\).

For clarity, the spectral form of \(q_K\) follows directly from
this construction. The vectors
\(w_j=\sqrt{\mu_j}\,j^*v_j\) form an orthonormal basis of
\(Q_K\): orthogonality follows from \(T=jj^*\), and a vector
orthogonal to all \(w_j\) has zero image under \(j\). Since
\(\langle jf,v_j\rangle_H
=\mu_j^{-1/2}\langle f,w_j\rangle_{Q_K}\), Parseval gives

\[
q_K(h)=\sum_{j\geq1}\mu_j
       |\langle h,v_j\rangle|^2.
\tag{ACI.9}
\]

Here \(h\in Q_K\).
Conversely, any \(h\in H\) for which the sum is finite is
\(jf\) for the element of \(Q_K\) with coefficients
\(\sqrt{\mu_j}\langle h,v_j\rangle\) in the \(w_j\) basis.
Thus (ACI.9) is the full form domain, and the diagonal operator
\(Kv_j=\mu_jv_j\) is positive self-adjoint with compact inverse.
The two forms agree at every point of \(Q_D\), yet the vector
\(v\) belongs only to the larger domain.

## Analytic rank-one operators with the wrong infinite value

The extended trace weight associated to \(D\) is

\[
\varphi(X)=\sum_{n\geq1}\lambda_n
                   \langle Xe_n,e_n\rangle.
\tag{ACI.10}
\]

Here \(X\in B(H)_+\).
It is faithful and normal: it is the supremum of finite sums of
positive normal functionals and dominates the usual trace.
Let \(P_N\) project onto the first \(N\) basis vectors. For every
positive \(X\), the compressions \(P_NXP_N\) have finite weight
and converge ultraweakly to \(X\), proving semifiniteness. Write
\(E_{mn}=|e_m\rangle\langle e_n|\) and
\(\lambda_n=n^2+3\). The vectors
\(f_{mn}=\lambda_n^{-1/2}\Lambda_\varphi(E_{mn})\)
are an orthonormal GNS basis. On their finite span the Tomita map is
\(Sf_{mn}=\sqrt{\lambda_m/\lambda_n}\,f_{nm}\), hence
\(\Delta f_{mn}=(\lambda_m/\lambda_n)f_{mn}\).
Coordinate truncation is a graph core for this diagonal map.
The modular theorem therefore gives
\(\sigma_t^\varphi(E_{mn})
=(\lambda_m/\lambda_n)^{it}E_{mn}\), and normality extends
the formula to
\(\sigma_t^\varphi(X)=D^{it}XD^{-it}\) on \(B(H)\).

Put \(u=e_1/2\), so \(D^{1/2}u=e_1\), and use the
\((v_j,\mu_j)\) from (ACI.9). With
\(|r\rangle\langle s|\xi=\langle\xi,s\rangle r\), define

\[
\begin{gathered}
a_j=\sqrt{\mu_j}\,|u\rangle\langle v_j|,
\\
b_j=\sqrt{\mu_j}\,
     |e_1\rangle\langle D^{-1/2}v_j|.
\end{gathered}
\tag{ACI.11}
\]

Every \(a_j\) and \(b_j\) is bounded. For
\(-1/2\leq\operatorname{Im}z\leq0\), the orbit

\[
\begin{gathered}
F_j(z)=\sqrt{\mu_j}\,
     |D^{iz}u\rangle\\
     \langle D^{i\bar z}v_j|
\end{gathered}
\tag{ACI.12}
\]

is bounded on the closed strip for each fixed \(j\), sigma-weakly
continuous there, and holomorphic inside. Indeed \(u\) is a
\(D\)-eigenvector, while \(D^{i\bar z}\) has nonpositive real
exponent on this strip and is uniformly bounded. Scalar spectral
integrals give the claimed continuity and holomorphy. For real
\(t\), (ACI.12) is \(D^{it}a_jD^{-it}\), and
\(F_j(-i/2)=b_j\). The source requires boundedness for each
orbit, not a common bound over all \(j\).

The endpoint-square partial sums are positive. From (ACI.11),
\(b_j^*b_j=\mu_j|D^{-1/2}v_j\rangle\langle D^{-1/2}v_j|\).
For every \(\xi\in H\), put \(\eta=D^{-1/2}\xi\).
The spectral form (ACI.9) then gives

\[
\begin{gathered}
\sum_j\langle b_j^*b_j\xi,\xi\rangle\\
=q_K(\eta)=q_D(\eta)=\|\xi\|^2.
\end{gathered}
\tag{ACI.13}
\]

Here \(D^{-1/2}H=Q_D\), exactly the smaller form domain where
the two forms agree. Each partial sum is at most \(1\); the
increasing sums therefore converge **strongly** to \(1\).
They cannot converge in norm, since each has finite rank.

For \(X\in B(H)_+\), the rank-one formula and
\(\varphi(|u\rangle\langle u|)=1\) give

\[
\begin{gathered}
\Psi_A(X)=\\
\sum_j\mu_j\langle Xv_j,v_j\rangle.
\end{gathered}
\tag{ACI.14}
\]

This is the normal extended trace weight determined by \(K\).
It agrees with \(\varphi\) whenever \(\varphi(X)<\infty\):
then \(X\) is trace class, and a positive rank-one spectral
decomposition expresses both values as sums of \(q_D(f)\) and
\(q_K(f)\) for vectors \(f\in Q_D\). At the rank-one
projection \(P_v=|v\rangle\langle v|\), however,

\[
\begin{gathered}
\varphi(P_v)=q_D(v)=\infty,
\\
\Psi_A(P_v)=q_K(v)=4.
\end{gathered}
\tag{ACI.15}
\]

Thus the full analytic strip condition and the strong endpoint
identity hold for a faithful normal semifinite weight on a
separable type I factor, while the printed all-positive reverse
conclusion fails. Even \(a_ja_j^*=\mu_j|u\rangle\langle u|\)
lies in the \(\varphi\)-centralizer.

The mechanism is a proper closed-form extension: the endpoint
identity tests the common smaller domain \(Q_D\), not the extra
vector \(v\in Q_K\setminus Q_D\). No nonzero positive finite-
\(\varphi\) operator lies below \(P_v\), so monotone finite
cutdowns cannot fill this gap. Indeed any \(0\leq Y\leq P_v\)
is \(tP_v\) for some \(0\leq t\leq1\), and its \(\varphi\)-weight
is infinite if \(t>0\).

**Source and boundary.** The target is Takesaki, *Theory of Operator
Algebras II*, IX.4 Lemma 4.20, printed p. 225/PDF p. 245, with
VIII.3 Lemma 3.18(i)–(ii), printed pp. 125–126/PDF pp. 145–146,
as its direct analytic input. The source's forward implication
and finite-cone reverse calculation survive; its reverse claim on
all positive elements does not. This counterexample does **not**
refute the separate existence theorem IX.4.18. A written all-positive
construction is supplied in Reconstruction from compatible modular
flows.
It does not use the false reverse implication. The analytic right action
is proved in HS02–03, and the support and finite-domain reductions are
proved above. The diagonal modular model is computed in ACI03.
