# Detecting and determining operator-valued weights

A faithful scalar weight can reveal whether an operator-valued weight is semifinite and can determine every one of its extended-positive outputs. Its modular group also remembers the scalar modular action on the target algebra. The three claims have different proofs: the last requires a mixed analytic graph theorem. Throughout, \(N\subseteq M\) is a unital inclusion of arbitrary von Neumann algebras, and no countability hypothesis is imposed.

## The three assertions and the scalar detector

Write \(\mathcal W(N)\) for normal semifinite weights on \(N\), and \(\mathcal W_0(N)\) for their faithful members. For operator-valued weights, the source uses \(\mathcal W(M,N)\) for all normal operator-valued weights and \(\mathcal W_0(M,N)\) for the faithful normal semifinite ones. In particular, \(S\in\mathcal W(M,N)\) need not be semifinite. Let \(T:M_+\to\widehat N_+\) initially be only normal. Takesaki II IX.4 Lemma 4.21 says:

1. If \(\psi\in\mathcal W_0(N)\) and \(\widehat\psi\circ T\) is semifinite, then \(T\) is semifinite.
2. If \(S\in\mathcal W(M,N)\) and \(\widehat\psi\circ T=\widehat\psi\circ S\) for one \(\psi\in\mathcal W_0(N)\), then \(T=S\), even when \(S\) is neither faithful nor semifinite.
3. If \(T\in\mathcal W_0(M,N)\), then \(\sigma_t^{\widehat\psi\circ T}(n)=\sigma_t^\psi(n)\) for every \(n\in N\), \(t\in\mathbb R\), and \(\psi\in\mathcal W_0(N)\).

Here scalar composition evaluates a normal weight on the **extended** positive \(T(x)\), including its infinite values. For (1), put \(\Phi=\widehat\psi\circ T\). If \(x\in\mathfrak M_\Phi^+\), faithfulness of \(\psi\) forces the infinite projection of \(T(x)\) to vanish. With \(e_r=1_{[0,r]}(T(x))\in N\), covariance gives

\[
\begin{aligned}
T(e_rxe_r)&=e_rT(x)e_r\in N_+,\\
e_rxe_r&\longrightarrow x\quad\text{strongly}.
\end{aligned}
\tag{OR.1}
\]

The finite cone of the semifinite scalar weight \(\Phi\) linearly spans the ultraweakly dense hereditary *-subalgebra \(\mathfrak M_\Phi\) of \(M\). Equation (OR.1) places each of its positive generators in the ultraweak closure of the bounded-output linear domain \(\mathfrak M_T\); hence that domain is ultraweakly dense and \(T\) is semifinite. Neither finite linear domain is asserted to be a two-sided ideal of \(M\). This is the scalar detector with the source quantifiers displayed. The cutdowns need not increase. Conversely, the composition theorem makes \(\widehat\psi\circ T\) semifinite when both \(T\) and \(\psi\) are semifinite. \(\square\)

## Uniqueness from one scalar composite, including infinity

Assume the hypotheses of assertion (2). Set \(\Phi=\widehat\psi\circ T=\widehat\psi\circ S\). This common scalar weight need not be semifinite. The argument uses faithfulness and semifiniteness of \(\psi\), the covariance identities for \(S,T\), and their extended-positive outputs; it requires no semifiniteness or faithfulness assumption on either operator-valued weight.

For every \(x\in M_+\) and \(a\in N\), covariance and the equality of scalar composites give the identity in \([0,\infty]\)

\[
\begin{aligned}
\widehat\psi\bigl(a^*T(x)a\bigr)
&=\Phi(a^*xa)\\
&=\widehat\psi\bigl(a^*S(x)a\bigr).
\end{aligned}
\tag{OR.2}
\]

First suppose \(S(x)=K\in N_+\) and let \(C=\|K\|\). For every \(a\in\mathfrak N_\psi\), (OR.2) yields

\[
\begin{aligned}
\widehat\psi\bigl(a^*T(x)a\bigr)
&\le C\psi(a^*a)\\
&<\infty.
\end{aligned}
\tag{OR.3}
\]

This forces \(H=T(x)\le C1\) as an extended positive. Indeed, if its spectral projection \(q=1_{(C+\varepsilon,\infty]}(H)\) were nonzero, faithfulness and semifiniteness of \(\psi\) would give a nonzero \(a\in\mathfrak N_\psi\) with \(qa=a\). Then the left side of (OR.3) would be at least \((C+\varepsilon)\psi(a^*a)\), a contradiction. The same test excludes a nonzero infinite projection. Now both \(H\) and \(K\) are bounded. Their quadratic forms agree on the dense set \(\Lambda_\psi(\mathfrak N_\psi)\) by (OR.2), so polarization and faithfulness of the GNS representation give \(H=K\). The same reasoning applies whenever \(T(x)\) is bounded.

For arbitrary \(x\in M_+\), write \(K=S(x)\) and \(H=T(x)\) as extended spectral positives in a faithful normal representation of \(N\). Let \(e_r=1_{[0,r]}(K)\) and \(f_r=1_{[0,r]}(H)\), excluding any infinite part. Covariance and the bounded-output case just proved yield

\[
\begin{aligned}
e_rHe_r&=e_rKe_r,\\
f_rHf_r&=f_rKf_r\quad(r>0).
\end{aligned}
\tag{OR.4}
\]

We must use both families: equality on a merely dense set of test vectors need not identify closed unbounded forms. If \(\xi\) has finite \(K\)-energy, spectral calculus gives \(e_r\xi\to\xi\) in the \(K\)-form norm. By (OR.4), each \(e_r\xi\) has finite \(H\)-energy and, for \(s\ge r\), the \(H\)-energy of \((e_s-e_r)\xi\) equals its \(K\)-energy. Closedness of the \(H\)-form therefore puts \(\xi\) in its finite form domain with the same energy. The \(f_r\) argument gives the reverse inclusion and equality. The finite domains, their quadratic forms, and hence their infinite projections coincide. Uniqueness of the closed spectral form gives \(T(x)=S(x)\). Since \(x\) was arbitrary, \(T=S\) on the full positive cone. \(\square\)

## The forward modular graph transfer

Now let \(T\in\mathcal W_0(M,N)\) and \(\varphi,\psi\in\mathcal W_0(N)\). Set \(\Phi=\widehat\varphi\circ T\) and \(\Psi=\widehat\psi\circ T\), both faithful normal semifinite by composition. With the course's balanced-matrix cocycle convention, form the mixed actions

\[
\begin{aligned}
u_t^N&=[D\psi:D\varphi]_t\,\sigma_t^\varphi,\\
u_t^M&=[D\Psi:D\Phi]_t\,\sigma_t^\Phi.
\end{aligned}
\tag{OR.5}
\]

The needed scalar mixed-graph contract says that if \((a,b)\) belongs to the closed analytic graph \(G(u_{-i}^N)\), then there are finite constants \(K,L\) such that, for every \(Q\in\widehat N_+\),

\[
\begin{aligned}
\widehat\psi(aQa^*)&\le K^2\widehat\varphi(Q),\\
\widehat\varphi(b^*Qb)&\le L^2\widehat\psi(Q),
\end{aligned}
\tag{OR.6}
\]

and on its oriented finite mixed ideal \(\mathfrak N_\varphi^*\mathfrak N_\psi\) one has \(\psi(az)=\varphi(zb)\). Normal evaluation of bounded spectral truncations extends the domination to the entire extended cone. Bimodularity then transfers (OR.6) to \(T(q)\) for every \(q\in M_+\), giving

\[
\begin{aligned}
\Psi(aqa^*)&\le K^2\Phi(q),\\
\Phi(b^*qb)&\le L^2\Psi(q).
\end{aligned}
\tag{OR.7}
\]

Thus the two GNS ideal inclusions and norm estimates required by the mixed graph on \(M\) hold. The separate finite-matrix contract is needed for its finite mixed identity: when \(y\in\mathfrak N_\Phi\cap\mathfrak N_T\) and \(z\in\mathfrak N_\Psi\cap\mathfrak N_T\), the bounded extension \(\dot T(y^*z)\) lies in \(\mathfrak N_\varphi^*\mathfrak N_\psi\), with the displayed orientation. Applying the scalar identity there yields

\[
\Psi(ay^*z)=\Phi(y^*zb).
\tag{OR.8}
\]

For general scalar-domain \(y,z\), cut \(T(y^*y)\) and \(T(z^*z)\) separately on the **right** by bounded spectral projections in \(N\). Their finite faithful scalar evaluations exclude infinite projections; the cuts put both vectors in \(\mathfrak N_T\) and converge in their scalar GNS norms. The two estimates (OR.7) transport this convergence through multiplication by \(a^*\) and \(b\), so (OR.8) passes to all \(y\in\mathfrak N_\Phi\), \(z\in\mathfrak N_\Psi\). The scalar mixed-graph criterion now gives

\[
G(u_{-i}^N)\subseteq G(u_{-i}^M).
\tag{OR.9}
\]

The inclusion is inside \(M\oplus M\). Finally the analytic-generator comparison contract turns it into \(u_t^M(n)=u_t^N(n)\) for every \(n\in N\) and real \(t\), without assuming beforehand that \(N\) is globally invariant under \(u^M\). Put \(\psi=\varphi\) to obtain

\[
\sigma_t^{\widehat\varphi\circ T}(n)=\sigma_t^\varphi(n).
\tag{OR.10}
\]

For general \(\psi\), evaluating the same mixed equality at \(n=1\) also gives \([D\Psi:D\Phi]_t=[D\psi:D\varphi]_t\in N\). This strengthening has the cocycle order specified in (OR.5). The proof assembly is valid relative to the three exact contracts named in OR-04; it does not use modular compatibility to construct \(T\).

## What remains to close the modular assertion

The source of OR-01–03 is Takesaki II IX.4 Lemma 4.21, printed pp. 227–230 / PDF pp. 247–250. Clauses (i) and (ii) have original arguments above relative to the course's extended-positive spectral and scalar-composition foundations. OR-03 is a **conditional** assembly, not a complete proof of clause (iii). Its three remaining component contracts are: the scalar mixed analytic graph with its half-strip domination and oriented finite identity (Takesaki II VIII.3.18/3.25; Haagerup I Theorem 3.2/Lemma 3.3); positivity and mixed-ideal placement for the finite matrix transfer, including the right spectral-cut passage (Haagerup I Lemmas 4.5–4.6); and analytic-generator comparison from graph inclusion to real actions (Takesaki II VIII.3.24; Haagerup I Lemmas 4.2–4.4). Their scalar strip/Fourier and finite-ideal foundations are also not proved here.

A proof of Haagerup I Theorem 4.7(1) under these contracts is not given in this course. The compatible-pair lesson may use the forward theorem only after this dependency is closed; neither IX.4.18 nor the false reverse of IX.4.20 proves it.
