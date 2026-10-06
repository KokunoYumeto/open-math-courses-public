<a id="OA-MOD-SC-02"></a>
<span id="oa-mod-sc-02-positive-observations-can-be-implemented-by-vector-sums"></span>
<span id="oa-mod-sc-02"></span>
## OA-MOD-SC-02. Positive observations can be implemented by vector sums

**Lemma.** If \(A\subseteq B(L)\) is a concrete unital von Neumann algebra and \(\omega\in A_*^+\), there are vectors \(v_j\in L\), indexed by positive integers, such that
\[
\sum_j\|v_j\|^2=\omega(1),\qquad
\omega(a)=\sum_j\langle av_j,v_j\rangle
\quad(a\in A).
\tag{SC.3}
\]
The series is absolutely convergent. Every component functional \(\omega_{v_j}\) is positive normal and satisfies \(\omega_{v_j}\le\omega\). No separability hypothesis on \(L\) is needed.

**Proof.** CP-08 gives square-summable vectors \(\zeta=(\zeta_j)\in\ell^2(\mathbb N,L)\) such that
\[
\omega(a)\le\vartheta(a):=
\sum_j\langle a\zeta_j,\zeta_j\rangle
\qquad(a\ge0).
\]
Let \(\rho(a)=\operatorname{diag}(a,a,\ldots)\), a bounded *-representation on \(\ell^2(\mathbb N,L)\), and put \(K=\overline{\rho(A)\zeta}\). The subspace is invariant under \(\rho(A)\) and its adjoints, so it reduces this representation. Also \(\zeta\in K\), because \(A\) is unital.

On the dense subspace \(\rho(A)\zeta\subseteq K\), define
\[
B(\rho(a)\zeta,\rho(b)\zeta)=\omega(b^*a).
\]
The inequality \(\omega(a^*a)\le\vartheta(a^*a)=\|\rho(a)\zeta\|^2\), together with the positive-functional Cauchy–Schwarz inequality, proves that this rule is well-defined and
\[
|B(\rho(a)\zeta,\rho(b)\zeta)|
\le\|\rho(a)\zeta\|\,\|\rho(b)\zeta\|.
\]
It extends to a positive bounded sesquilinear form on \(K\). The bounded-form theorem gives a unique positive contraction \(h\in B(K)\) with \(B(u,v)=\langle hu,v\rangle\).

For \(c\in A\), the equality
\[
B(\rho(c)\rho(a)\zeta,\rho(b)\zeta)
=B(\rho(a)\zeta,\rho(c^*)\rho(b)\zeta)
\]
holds because both sides equal \(\omega(b^*ca)\). Extension from the dense cyclic subspace shows that \(h\) commutes with \(\rho(c)|_K\). Its square root commutes as well. Set \(v=h^{1/2}\zeta\in K\), and write its components as \(v_j\in L\). For every \(a\in A\),
\[
\omega(a)=B(\rho(a)\zeta,\zeta)
=\langle\rho(a)v,v\rangle
=\sum_j\langle av_j,v_j\rangle.
\]
Evaluation at \(1\) gives the asserted sum of squared norms. Absolute convergence follows from \(|\langle av_j,v_j\rangle|\le\|a\|\|v_j\|^2\). For positive \(a\), each nonnegative summand is at most the sum, proving \(\omega_{v_j}\le\omega\). Single-vector functionals are ultraweakly continuous by CP. If \(\omega=0\), the construction may be replaced by the zero sequence. ∎

The use of a countable series concerns one predual functional. The family of all normal functionals can be arbitrarily large. We have not chosen a countable family which detects the entire algebra.

