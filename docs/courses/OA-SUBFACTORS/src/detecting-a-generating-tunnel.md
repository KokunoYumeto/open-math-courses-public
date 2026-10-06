# Detecting a generating tunnel

A tunnel may generate a proper factor through its relative commutants. If that factor has finite index, its basis can be moved arbitrarily far down the tunnel. This makes it possible to test generation by conditional expectations of bounded vectors. The test is stronger than mere nonzero approximation: it must have one positive lower bound for every sufficiently late level and every vector in a specified norm ball.

We assume [Reflected traces and a uniform bound along a tunnel](reflected-traces-and-uniform-bounds.md), [Finite bases, bounded vectors and a positive-operator inequality](finite-bases-and-positive-index.md), [Going up and down the Jones tower](towers-and-tunnels.md), and [Positivity restricts the index](positivity-and-index-rigidity.md). References are [Popa], [Jones] and [Pimsner–Popa]. In the final section we use Definition 3.1 and Theorem 3.2 of Ultraproducts and the asymptotic centralizer, specialized to the finite tracial ultrapower. The relative-commutant lemma within that construction is proved here.

Let \(N\subsetneq M\) be separable II₁ factors of finite index \(d>1\) and finite depth. The identity inclusion is already classified separately. Write

\[
\begin{gathered}N_k=M_{-k-1},\\D_k=N_k'\cap M,\\R=\left(\bigcup_kD_k\right)''.\end{gathered}
\tag{15.1}
\]

Theorem 14.4 and reflection make \(R\) a factor. Unless stated otherwise, the tunnel is arbitrary. Expectations preserve normalized traces.

## Corners and downward finite depth

**Lemma 15.1.** Every consecutive inclusion in the tunnel has finite depth. For every \(k\), the algebra \(S_k=R\cap N_k\) is a factor.

**Proof.** A common corner by a nonzero projection \(p\) in the smaller factor preserves the standard invariant and finite depth. Here are the needed details. If \(P\subseteq Q\), the relative-commutant map is \(x\mapsto pxp\). It is faithful on \(P'\cap Q\), since \(p\) has full support in the factor \(P\). It is onto \((pPp)'\cap pQp\): choose finitely many partial isometries \(v_i\in P\) with \(v_i^*v_i\leq p\) and orthogonal \(v_iv_i^*\) summing to one, and extend an element \(y\) of the latter commutant by \(\sum_i v_i yv_i^*\). Commutation with the corner matrix coefficients \(v_i^*av_j\in pPp\) proves that this extension commutes with \(P\) and compresses back to \(y\). The same construction applies at every level of the common-corner Jones tower. Jones projections commute with \(p\), and their full-support criterion is preserved. This proves the claim about corners.

Now consider a downward triple \(P\subseteq Q\subseteq T=\langle Q,f\rangle\). Its next upward factor is \(T_1\). The common corner inclusion

\[
fTf\subseteq fT_1f
\]

is isomorphic to \(P\subseteq Q\). Indeed, \(fTf=Pf\). The adjoint pull-down identity gives \(fL^2(T)=\overline{fQ}\); the map \(\widehat x\mapsto [Q:P]^{1/2}f\widehat x\) identifies this right \(Q\)-module with \(L^2(Q)\). Since \(T_1=\operatorname{End}_{Q^{\mathrm{op}}}(L^2(T))\), its corner is \(Q\), and \(Pf\) becomes \(P\). If \(Q\subseteq T\) has finite depth, its dual \(T\subseteq T_1\) has finite depth by Theorem 14.4. The corner claim therefore gives finite depth of \(P\subseteq Q\). Induction moves this conclusion down the tunnel.

For \(l\geq k\), the expectation onto \(N_k\) preserves \(D_l\), since \(N_l\subseteq N_k\). Consequently

\[
R\cap N_k=\left(\bigcup_{l\geq k}(N_l'\cap N_k)\right)''.
\tag{15.2}
\]

To justify equality, approximate an element of \(R\cap N_k\) by expectations onto the increasing finite algebras \(D_l\), then apply \(E_{N_k}\). The resulting elements lie in the union on the right and converge in \(L^2\). This is the downward relative-commutant closure for the finite-depth adjacent pair \(N_k\subseteq N_{k-1}\), so Theorems 14.3–14.4 make it a factor. \(\square\)

## Expectations commute with later relative commutants

**Proposition 15.2.** If \(l\geq k\), then

\[
E_{D_l}E_{N_k}=E_{N_k}E_{D_l}=E_{D_l\cap N_k}.
\tag{15.3}
\]

The same commutation holds with \(N_k\) replaced by \(Q_k=N_k\vee D_k\). Its product is \(E_{Q_k\cap D_l}\), where

\[
Q_k\cap D_l=(N_k\cap D_l)\vee D_k.
\tag{15.4}
\]

Taking increasing limits gives the commuting square

\[
\begin{array}{ccc}N_k&\subseteq&M\\\cup&&\cup\\S_k&\subseteq&R.\end{array}
\tag{15.5}
\]

**Proof.** Conjugation by \(\mathcal U(N_l)\) on \(L^2(M)\) has fixed-vector space \(L^2(D_l)\). The projection onto \(L^2(N_k)\) commutes with that action because \(N_l\subseteq N_k\). It thus commutes with the projection onto the fixed vectors. Their common range is \(L^2(N_k\cap D_l)\), proving (15.3).

For clarity, that fixed-vector projection can be obtained without any group amenability assumption. The norm-closed convex hull of the conjugates of a bounded element has a unique vector of least \(L^2\)-norm. Invariance of the hull makes this vector fixed. Its pairing with every fixed vector agrees with that of the original element, so it is the orthogonal fixed-vector projection, namely the relative-commutant expectation. The hull is uniformly bounded, hence its \(L^2\) limits are elements of \(M\).

The subspace \(L^2(Q_k)\) is also invariant, so the same projection argument applies to \(Q_k\). Alternatively, for \(a\in N_k\) and \(b\in D_k\subseteq D_l\),

\[
E_{D_l}(ab)=E_{D_l}(a)b,\qquad E_{D_l}(a)\in N_k\cap D_l.
\]

Such products span \(Q_k\), since the commuting algebra \(D_k\) is finite dimensional. This proves (15.4). Finally \(E_{D_l}\to E_R\) in \(L^2\). Pass to the limit in (15.3) and use (15.2). The resulting product of expectations is \(E_{S_k}\), proving (15.5). \(\square\)

## The same index is visible at every tunnel level

Assume now that \(D=[M:R]<\infty\). This is a substantive hypothesis; finite depth alone has not yet supplied its existence in the present argument.

**Theorem 15.3.** For every \(k\),

\[
[N_k:S_k]=D.
\tag{15.6}
\]

A partial orthonormal basis for \(S_k\subseteq N_k\) is also such a basis for \(R\subseteq M\).

**Proof.** Put \(D_k^{\mathrm{ind}}=[M:N_k]=d^{k+1}\); this scalar is distinct from the algebra \(D_k\). By (15.5) and the positive-operator index inequality,

\[
E_{S_k}=E_RE_{N_k}\geq
(D D_k^{\mathrm{ind}})^{-1}\operatorname{id}
\quad\text{on }M_+.
\]

The variational characterization of index therefore gives
\([M:S_k]\leq D D_k^{\mathrm{ind}}\).

Apply Proposition 14.8 to the skipped-level triple

\[
M_{-2k-2}\subseteq N_k\subseteq M.
\]

Its Jones projection \(g\in M\) satisfies \(E_{N_k}(g)=(D_k^{\mathrm{ind}})^{-1}1\). It commutes with \(M_{-2k-2}=N_{2k+1}\), so \(g\in D_{2k+1}\subseteq R\). Equation (15.5) gives \(E_{S_k}(g)=E_{N_k}(g)\). The optimal positive-operator bound for \(S_k\subseteq R\), evaluated on the nonzero projection \(g\), yields

\[
[R:S_k]\geq D_k^{\mathrm{ind}}.
\]

Multiplicativity now forces equality:

\[
D D_k^{\mathrm{ind}}\geq[M:S_k]
=D[R:S_k]\geq D D_k^{\mathrm{ind}}.
\]

Computing \([M:S_k]\) through \(N_k\) proves (15.6).

Let \(u_1,\ldots,u_s\in N_k\) be a partial orthonormal basis over \(S_k\), with support projections \(p_i\in S_k\). Commutation of expectations gives

\[
E_R(u_i^*u_j)=\delta_{ij}p_i,\qquad
\sum_i u_i u_i^*=D1.
\]

In the basic construction of \(R\subseteq M\), the operators \(u_i e_Ru_i^*\) are mutually orthogonal projections. Their sum has normalized trace

\[
D^{-1}\sum_i\tau(u_i^*u_i)=1.
\]

Faithfulness makes that sum the identity. Multiplying by \(xe_R\) and using the compression identity gives

\[
x=\sum_i u_iE_R(u_i^*x)\quad(x\in M).
\tag{15.7}
\]

Thus the basis is also a basis over \(R\). \(\square\)

The fractional support in this basis measures \([N_k:S_k]=D\), not \([R:S_k]=d^{k+1}\). More precisely, with \(n=\lfloor D\rfloor\), one can choose \(n\) full entries and one additional entry with support \(p\in S_k\) of trace \(D-n\). If \(D\) is an integer, the additional entry is zero. All traces here are normalized; the inclusions \(S_k\subseteq N_k,R,M\) preserve that trace. Takesaki's proof of Lemma 4.26(iii) puts \([R:S_k]-n\) in this support formula. Exercise 15.5 shows that this expression can exceed one in an actual generating tunnel.

The basis uses right coefficients as in (15.7): the coefficient \(E_R(u_i^*x)\) follows \(u_i\). Partial orthonormality \(E_R(u_i^*u_j)=\delta_{ij}p_i\) does not justify reversing that order. The proof above obtains the correctly ordered expansion directly from the basic-construction identity.

## A bounded vector detects a proper inclusion

**Lemma 15.4.** If \(T\subsetneq M\) are II₁ factors with finite index \(s\), there is \(a\in M\) such that

\[
\begin{gathered}E_T(a)=0,\qquad E_T(a^*a)=1,\\\|a\|_2=1,\qquad \|a\|\leq\sqrt s.\end{gathered}
\tag{15.8}
\]

**Proof.** A proper finite-index inclusion has \(s\geq2\), by the allowed-index theorem. In its basic construction the Jones projection \(e_T\) has normalized trace \(s^{-1}\leq\tfrac12\). Projection comparison provides a unitary \(v\) with \(v e_Tv^*\perp e_T\). Pull down \(v\) to \(a\in M\), so \(ae_T=ve_T\) and \(\|a\|\leq\sqrt s\). Orthogonality gives \(e_Tae_T=0\), hence \(E_T(a)=0\). Also

\[
E_T(a^*a)e_T=e_Ta^*ae_T=e_Tv^*ve_T=e_T.
\]

The corner map is faithful, giving \(E_T(a^*a)=1\), and its trace gives \(\|a\|_2=1\). \(\square\)

## A uniform orbital test forces generation

**Theorem 15.5.** Suppose the tunnel in (15.1) has \([M:R]=D<\infty\). Suppose further that there are \(\varepsilon_0>0\) and \(k_0\) such that for every \(k>k_0\) and every \(x\in M\) with

\[
\|x\|_2=1,\qquad\|x\|\leq\sqrt D,
\]

some \(u\in\mathcal U(N_k)\) satisfies

\[
\|E_{uRu^*}(x)\|_2>\varepsilon_0.
\tag{15.9}
\]

Then \(N\subseteq M\) admits a generating tunnel.

**Proof.** Choose a countable \(L^2\)-dense sequence \(x_i\) in the displayed norm-bounded unit sphere, and a countable \(L^2\)-dense sequence \(y_i\) in the positive unit ball of \(M\). Separability supplies both sequences.

We build finite prefixes \(Q_0=N\supseteq Q_1\supseteq\cdots\supseteq Q_{l_n}\). Any already chosen finite prefix can be matched with the original one by a unitary \(w\in N\): use one-step tunnel uniqueness successively; a correcting unitary at the next level lies in the previous smaller factor and preserves every earlier level.

At stage \(n\), take such \(w\). The positive-vector index inequality, with its squared \(L^2\)-norm convention, gives

\[
\|E_R(w^*y_iw)\|_2\geq D^{-1/2}\|y_i\|_2.
\]

Choose \(k>\max\{l_{n-1},k_0\}\) sufficiently large that, for \(i\leq n\),

\[
\begin{gathered}\|E_{D_k}(w^*y_iw)\|_2\\\geq D^{-1/2}\|y_i\|_2-n^{-1}.\end{gathered}
\tag{15.10}
\]

This uses the increasing-limit convergence \(E_{D_k}\to E_R\). Apply (15.9) to \(w^*x_nw\), obtaining \(v\in\mathcal U(N_k)\). Increasing-limit convergence then supplies \(l_n>k\) such that

\[
\|E_{vD_{l_n}v^*}(w^*x_nw)\|_2>\varepsilon_0.
\]

Extend the prefix by \(Q_i=wvN_iv^*w^*\) through level \(l_n\). Because \(v\in N_k\), it preserves all \(N_i\) with \(i\leq k\), and it fixes \(D_k\) pointwise. Thus the old prefix is preserved, as are all earlier detection bounds. Equation (15.10) is preserved too. This completes the induction.

Let \(T=(\bigcup Q_i'\cap M)''\). Lemma 15.1 makes it a factor. Passing to limits and using density gives

\[
\begin{gathered}\|E_T(y)\|_2\geq D^{-1/2}\|y\|_2\quad(y\geq0),\\\|E_T(x)\|_2\geq\varepsilon_0.\end{gathered}
\]

for every \(x\) in the stated unit sphere. The positive-vector variational characterization gives \([M:T]\leq D\). If \(T\ne M\), Lemma 15.4 supplies a vector of that sphere with \(E_T(x)=0\), a contradiction. Hence \(T=M\).

Finally \((\bigcup Q_i'\cap N)''=N\). The expectations \(E_N\) commute with those onto \(Q_i'\cap M\), by Proposition 15.2 with the fixed initial level. Since the latter converge to the identity on \(M\), their restrictions approximate every element of \(N\) by \(Q_i'\cap N\). Thus the constructed tunnel generates both endpoints. \(\square\)

The quantifiers in (15.9) cannot be replaced by a separate lower bound for each vector or by detection at only one level. The induction uses later-level freedom while preserving all earlier choices.

The two normalization requirements in this argument remain fixed throughout the induction. A dense sequence of orbital test vectors must belong to the same set
\(\{x:\|x\|_2=1,\ \|x\|\leq\sqrt D\}\)
that occurs in the hypothesis; it is dense in that set for the tracial \(L^2\) metric. The bounded missed vector from Lemma 15.4 belongs to this set when \([M:T]\leq D\). For positive vectors, the squared variational bound \(D^{-1}\) gives the nonsquared norm bound \(D^{-1/2}\), as used in (15.10). A nonsquared bound \(D^{-1}\) alone would only imply \([M:T]\leq D^2\), which does not put that missed vector under the required cutoff. These are the needed corrections to the dense-vector cutoff and the norm coefficient in the proof of Takesaki's Lemma 4.25; the generating-tunnel conclusion is retained with the corrected proof above.

## Relative commutants of varying algebras in an ultrapower

Let \(\omega\) be a free ultrafilter and \(M^\omega\) the tracial ultrapower. A bounded sequence \((x_n)\) represents zero precisely when \(\lim_\omega\|x_n\|_2=0\). For subalgebras \(P_n\subseteq M\), let \(P=\prod_\omega P_n\subseteq M^\omega\).

**Lemma 15.6.** There is equality

\[
P'\cap M^\omega
=\prod_\omega(P_n'\cap M).
\tag{15.11}
\]

**Proof.** The right side plainly commutes with \(P\). Conversely, put \(C_n=P_n'\cap M\). Coordinatewise expectations define the trace-preserving expectation onto \(\prod_\omega C_n\): they are uniformly bounded and contract \(L^2\), so the definition is independent of representatives. An element represented by \((x_n)\) is outside this subalgebra exactly when

\[
\eta=\lim_\omega\|x_n-E_{C_n}(x_n)\|_2>0.
\]

By the least-norm orbit argument in Proposition 15.2, \(E_{C_n}(x_n)\) lies in the closed convex hull of the \(P_n\)-unitary conjugates of \(x_n\). Hence

\[
\|x_n-E_{C_n}(x_n)\|_2
\leq\sup_{u\in\mathcal U(P_n)}\|x_n-ux_nu^*\|_2.
\]

Choose \(u_n\in\mathcal U(P_n)\) realizing at least half of that lower bound whenever it is nonzero. The sequence defines a unitary \(u\in P\), and \(\|x-uxu^*\|_{2,\omega}\geq\eta/2>0\). Thus \(x\notin P'\cap M^\omega\). This proves the reverse inclusion. No uniform choice of a single unitary in all \(P_n\) was required. \(\square\)

The remaining existence argument must establish a finite-index tunnel and the uniform orbital test (15.9). The lemmas above give their consequences without assuming either conclusion in their proofs.

## Exercises

**Exercise 15.1 — introductory.** If \(R=M\), what constant and unitary work in (15.9)?

**Solution.** Here \(D=1\), every expectation onto \(uRu^*=M\) is the identity, and every tested vector has \(L^2\)-norm one. Take \(u=1\) and any \(0<\varepsilon_0<1\).

**Exercise 15.2 — intermediate.** In Theorem 15.3, explain why one ordinary negative Jones projection cannot simply be declared to be the skipped-level projection \(g\).

**Solution.** The skipped inclusion \(N_k\subseteq M\) has index \(d^{k+1}\), so its downward Jones projection must have expectation \(d^{-(k+1)}1\) onto \(N_k\). A projection for one adjacent inclusion has the one-step normalization \(d^{-1}\) at its own level, and may even belong to \(N_k\). Proposition 14.8 constructs the appropriate projection for the composite inclusion; its commutation with \(N_{2k+1}\) then puts it in \(R\).

**Exercise 15.3 — intermediate.** Suppose a family \(u_i\in M\) obeys partial orthonormality over \(R\), and \(\sum_i\tau(u_i^*u_i)=[M:R]\). Prove that it is a complete basis.

**Solution.** The projections \(u_i e_Ru_i^*\) in the basic construction are orthogonal. Their sum has normalized trace one by the basic-construction trace formula. Thus it is the identity. Apply it to \(xe_R\), use compression, and use faithfulness of \(a\mapsto ae_R\) to obtain (15.7).

**Exercise 15.4 — advanced.** In Lemma 15.6, why would testing only constant sequences of unitaries be insufficient?

**Solution.** Commutation with the diagonal copy of one fixed algebra tests \(\lim_\omega\|[x_n,u]\|_2\) for each constant \(u\). The obstruction at coordinate \(n\) can depend on \(n\), and for varying \(P_n\) there may be no common unitary detecting it. The proof chooses \(u_n\) separately and tests the resulting unitary of \(P\). The full ultraproduct relative commutant quantifies over all such bounded sequences.

**Exercise 15.5 — advanced.** Take the actual index-six hyperfinite group inclusion of Theorem 41.4, and choose a generating tunnel using Theorem 17.5. For \(k=1\), compute the fractional support trace in the basis for \(S_k=R\cap N_k\subseteq N_k\). Compare it with \([R:S_k]-\lfloor[M:R]\rfloor\).

**Solution.** The group example is a proper finite-depth inclusion of separable hyperfinite II₁ factors, so Theorem 17.5 applies. Generation makes \(R=M\), whence \(D=[M:R]=1\) and \(S_k=N_k\). The basis is the single element \(1\), with an optional zero second entry. Its fractional support trace is \(D-\lfloor D\rfloor=0\). On the other hand, \(N_k=M_{-k-1}\), so \([R:S_1]=[M:M_{-2}]=6^2=36\). The compared expression is \(36-1=35\), which cannot be the normalized trace of a projection. This verifies the erroneous support formula inside the hypotheses of the source lemma, while Theorem 15.3 and its correctly normalized basis remain valid.

## References

- Masamichi Takesaki, [*Theory of Operator Algebras III*](https://doi.org/10.1007/978-3-662-10453-8), Springer, 2003, Chapter XIX, Lemmas 4.25–4.26.

- Sorin Popa, [*Classification of subfactors: the reduction to commuting squares*](https://doi.org/10.1007/BF01231494), Inventiones Mathematicae 101 (1990), 19–43.
- Vaughan F. R. Jones, [*Index for subfactors*](https://doi.org/10.1007/BF01389127), Inventiones Mathematicae 72 (1983), 1–25.
- Mihai Pimsner and Sorin Popa, [*Entropy and index for subfactors*](https://www.numdam.org/item/ASENS_1986_4_19_1_57_0/), Annales scientifiques de l'École Normale Supérieure 19 (1986), 57–106.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Self-checked by the writing AI. Public domain (CC0).*
