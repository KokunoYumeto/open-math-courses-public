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

We name the precise analytic input rather than hiding it. The
fixed-operator theorem of Takesaki II, VIII.3.18(i)–(ii), says that
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

The full proof of this analytic theorem is an explicit open course
prerequisite, `OA-MOD-ACI-DEP-RIGHT-ACTION`. The source's proof of
IX.4.20 cites VIII.3.17 at this step; VIII.3.18 is the direct
fixed-operator statement.

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

The printed IX.4.20 permits a nonfaithful semifinite normal weight
and formulates its analytic test in the support corner. The faithful
argument above applies there once the exact support-reduction
contract is supplied. That reduction and the complete proof of
VIII.3.18 remain open course dependencies; the counterexample below
already has support \(1\), so neither issue can repair the printed
all-positive reverse implication.

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
refute the separate existence theorem IX.4.18. That theorem needs
an independent all-positive construction, which is not given in
these lessons. The analytic right-action theorem behind (ACI.2) and
the modular theorem used for the type I model are not proved in
this lesson.
