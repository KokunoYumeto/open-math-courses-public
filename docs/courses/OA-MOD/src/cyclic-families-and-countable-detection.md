# Cyclic families and countable detection

**Self-checked by the writing AI.**

A family of vectors can describe a representation in two different ways: its algebraic orbits may span the Hilbert space, or its values may detect every operator. Passing to the commutant exchanges these two properties. Countability of operator detection is then equivalent to an intrinsic condition on the algebra's projections, even when the Hilbert space is not separable.

Let \(M\subseteq B(H)\) be a unital concrete von Neumann algebra; allow \(H=0\). For \(K\subseteq H\), write \([MK]\) for the closed linear span of the vectors \(x\xi\), with \(x\in M\) and \(\xi\in K\). The span of the empty set is zero. A family \(K\) is **cyclic** for \(M\) if \([MK]=H\), and **separating** for \(M\) if the only \(x\in M\) annihilating every vector in \(K\) is zero. No countability is part of either definition.

The exact earlier inputs are BK01–04, orthogonal projections, bicommutants and increasing strong limits, CP06–07, the concrete predual and positive normal functionals, and WG006–007/010, GNS construction, normality and the finite faithful case. Normal means ultraweakly continuous. The same results are treated in Takesaki, *Theory of Operator Algebras I*, Chapter II, §3, Definitions 3.16 and 3.18 and Propositions 3.17 and 3.19, printed pp. 77–78. We keep the arbitrary-subset and arbitrary-representation scope.

## The projection determined by a family

Let \(p_K\) be the orthogonal projection onto \([MK]\). This subspace is invariant under \(M\), and also under adjoints because \(M\) is a star algebra. Its orthogonal complement is invariant too: if \(\eta\perp[MK]\) and \(v\in[MK]\), then \(\langle x\eta,v\rangle=\langle\eta,x^*v\rangle=0\). Thus both summands reduce every \(x\in M\), and

\[
 \begin{gathered}p_K\in M',\\p_KH=[MK].\end{gathered}
 \tag{CY.1}
\]

This is the least projection in \(M'\) fixing every vector of \(K\). Indeed a projection \(e\in M'\) fixing those vectors fixes all their \(M\)-orbits and their closed span, so \(p_K\leq e\).

For \(b\in M'\), annihilating \(K\) is equivalent to annihilating \([MK]\), by commutation and continuity. Therefore \(K\) is separating for \(M'\) exactly when \(p_K=1\): if \(p_K\ne1\), the nonzero element \(1-p_K\in M'\) annihilates \(K\); if \(p_K=1\), an annihilator vanishes on a dense subspace and hence on \(H\). Writing \(\mathcal A^{\prime}_K\) for this annihilator in \(M'\), the two implications read

\[
 \begin{gathered}p_K=1\\\Longleftrightarrow\mathcal A^{\prime}_K=\{0\}.\end{gathered}
 \tag{CY.2}
\]

Applying the same argument to \(M'\), and using \(M''=M\) from BK02, gives the reciprocal equivalence.

It is useful to name \(q_K\), the projection onto \([M'K]\). Then \(q_K\in M\) is the least projection of \(M\) fixing \(K\), and

\[
 \begin{gathered}xK=0\\\Longleftrightarrow xq_K=0.\end{gathered}
 \tag{CY.3}
\]

Moreover, \(K\) is separating for \(M\) exactly when \(q_K=1\), by the reciprocal equivalence. Equation (CY.3) holds for every \(x\in M\): commute \(x\) through \(M'\) on the generating vectors and then take the closure. In particular the annihilator is the left ideal \(M(1-q_K)\). These projections need not be central.

For a union of families, the least-projection characterization gives \(q_{\cup_i K_i}=\bigvee_iq_{K_i}\). The join is the projection onto the closed span of their ranges and belongs to \(M\), since this span reduces \(M'\). This proves the assertion even for uncountably many families and noncommuting support projections. Identical statements hold for \(p_K\) with the two algebras interchanged.

## Countable observations give a faithful normal functional

Suppose \((\xi_n)\) is a countable separating family for \(M\). Define

\[
 \begin{gathered}
 c_n=\frac{2^{-n}}{1+\|\xi_n\|^2},\\
 \varphi(x)\\ =\sum_{n\geq1}
           c_n\langle x\xi_n,\xi_n\rangle.
 \end{gathered}
 \tag{CY.4}
\]

A finite family may be extended by zero vectors. The formula also handles zero vectors without division by zero. Each term is a positive normal functional, and its norm is \(c_n\|\xi_n\|^2\leq2^{-n}\), by CP07. The series converges in functional norm. Norm closure of the predual's positive cone, proved in CP06–07, makes \(\varphi\) a bounded positive normal functional. Thus normality here follows for arbitrary increasing nets; it is not just countable additivity.

For any \(x\in M\), positivity of each summand gives

\[
 \begin{gathered}\varphi(x^*x)=0\\\Longleftrightarrow(\forall n)\;x\xi_n=0\\\Longleftrightarrow x=0.\end{gathered}
 \tag{CY.5}
\]

This is faithfulness. If \(M\ne0\), then \(\varphi(1)>0\), and dividing by that number gives a faithful normal state.

A von Neumann algebra is called **sigma-finite** here if every family of pairwise orthogonal **nonzero** projections is at most countable. Let \(\psi\) be any faithful bounded positive functional on \(M\). For an orthogonal family \((e_i)_{i\in I}\) of nonzero projections, put \(I_m=\{i:\psi(e_i)\geq1/m\}\). For every finite \(F\subseteq I_m\),

\[
 \frac{|F|}{m}\leq\psi(1).
 \tag{CY.6}
\]

Indeed \(\sum_{i\in F}e_i\leq1\), and finite additivity gives the inequality. This forces \(I_m\) to be finite. Faithfulness gives \(\psi(e_i)>0\), so \(I=\bigcup_{m\geq1}I_m\) is countable. This implication does not require normality of \(\psi\). Together with (CY.4), it proves that a countable separating family forces sigma-finiteness.

## Projection countability recovers the observations

Suppose now that \(M\) is sigma-finite. Consider sets of nonzero vectors whose closed \(M'\)-cyclic subspaces are pairwise orthogonal. Order these sets by inclusion. The union of a chain still has the pairwise orthogonality property, because any two vectors in that union occur together in one member of the chain. Zorn's lemma gives a maximal set \(\{\eta_i:i\in I\}\).

By CY01 the projections \(q_i\) onto \([M'\eta_i]\) belong to \(M\). They are pairwise orthogonal and nonzero. Hence \(I\) is countable. Their strong sum is a projection \(q\in M\), with

\[
 \begin{gathered}qH\\=\bigoplus_{i\in I}[M'\eta_i].\end{gathered}
 \tag{CY.7}
\]

If \(q\ne1\), choose a nonzero \(\eta\in(1-q)H\). As \(q\in M\), it commutes with \(M'\). Thus \([M'\eta]\subseteq(1-q)H\), so adjoining \(\eta\) contradicts maximality. Therefore \(q=1\). The countable family \(\{\eta_i\}\) is cyclic for \(M'\), and CY01 makes it separating for \(M\).

We have proved the full equivalence between sigma-finiteness, the existence of a countable separating family in the **given** representation, and the existence of a faithful positive normal functional. If the algebra is nonzero, “functional” may be replaced by “state.” For the zero algebra on the zero Hilbert space, the empty family is cyclic and separating, projection countability is vacuous, and the zero functional is faithful; there is no state of norm one. This is why the state formulation carries its nonzero hypothesis.

There is a useful countable selection consequence. Let \(M\ne0\) be sigma-finite, let \(\varphi\) be a faithful normal state just constructed, and let \(\{e_i:i\in I\}\) be **any** family of projections of \(M\), not necessarily orthogonal or commuting. Write \(e=\bigvee_i e_i\). For finite \(F\subseteq I\), put \(e_F=\bigvee_{i\in F}e_i\). These projections increase strongly to \(e\). Normality gives \(\varphi(e_F)\uparrow\varphi(e)\), so choose finite \(F_n\) with

\[
 \begin{gathered}\varphi(e)-\varphi(e_{F_n})\\<1/n.\end{gathered}
 \tag{CY.8}
\]

For \(J=\bigcup_nF_n\), put \(r=\bigvee_{j\in J}e_j\). Then \(e_{F_n}\leq r\leq e\), whence \(0\leq\varphi(e-r)<1/n\) for every \(n\). Faithfulness makes \(r=e\). Thus every projection join has a countable subfamily with the same join. If \(I\) is empty, take \(J\) empty; the same statement is immediate for the zero algebra.

Apply this to \(e_\xi=q_{\{\xi\}}\), \(\xi\in K\). CY01 yields a countable \(K_0\subseteq K\) with \(q_{K_0}=q_K\). In particular, every separating family for a sigma-finite algebra contains a countable separating subfamily. This does not say that every cyclic family has a countable cyclic subfamily: that analogous conclusion requires sigma-finiteness of the commutant.

## Where a single cyclic and separating vector lives

The existence of a faithful normal functional is an assertion about the algebra and its predual. A single separating vector is an additional assertion about a particular representation. Here is the precise representation change that supplies such a vector.

Let \(M\ne0\) be sigma-finite and choose a faithful normal state \(\varphi\). Its finite GNS construction, proved in WG006, has dense map \(\Lambda_\varphi:M\to H_\varphi\), representation \(\pi_\varphi:M\to B(H_\varphi)\), and vector \(\Omega=\Lambda_\varphi(1)\). In these specified coordinates,

\[
 \pi_\varphi(x)\Omega=\Lambda_\varphi(x).
 \tag{CY.9}
\]

The dense range makes \(\Omega\) cyclic. The norm identity gives

\[
 \begin{gathered}\|\pi_\varphi(x)\Omega\|^2\\=\varphi(x^*x).\end{gathered}
 \tag{CY.10}
\]

Faithfulness implies that \(\pi_\varphi(x)\Omega=0\) forces \(x=0\). Thus the representation is faithful and \(\Omega\) is separating for its image. WG007 proves normality using bounded increasing nets, and WH02 proves that the faithful normal image is a von Neumann algebra. Consequently CY01 applies to this image and its commutant as well. This reuses the full finite faithful GNS result WG010, rather than assuming a faithful vector already exists in \(H\).

Conversely, a faithful normal representation \(\pi:M\to B(E)\) with a nonzero separating vector \(\zeta\) supplies the faithful normal functional \(x\mapsto\langle\pi(x)\zeta,\zeta\rangle\). Faithfulness follows from separation and injectivity of \(\pi\); normality follows by composing the normal representation with the normal vector functional. CY02 makes \(M\) sigma-finite. Hence the GNS construction establishes an equivalence involving **existence of a suitable representation**, not a claim that every faithful representation has such a vector.

Sigma-finiteness itself is independent of a faithful normal representation. A faithful normal star representation is a star isomorphism onto its von Neumann image by WH02; it gives a bijection of projections preserving nonzeroness and orthogonality. Applying the intrinsic projection condition on either side proves the assertion. CY03 then supplies countable separating families in every such representation, with no claim that those families are the same vectors.

## Examples that separate the countability conditions

**A scalar algebra on a nonseparable space.** Let \(I\) be uncountable, let \(H=\ell^2(I)\), and let \(M=\mathbb C1\). Any nonzero vector is separating for \(M\), and the scalar functional is a faithful normal state. The only projections of \(M\) are \(0,1\), so it is sigma-finite. However, the orbit span of a family under \(M\) is just that family's closed linear span. No countable family spans \(H\): each vector has countable coordinate support, since for each positive integer \(m\) only finitely many coordinates have modulus at least \(1/m\). The union of the supports of countably many vectors is still countable, and a coordinate vector outside it is orthogonal to their span. Thus sigma-finiteness does not imply separability or a countable cyclic family in the given representation.

Here \(M'=B(H)\) contains the uncountable family of coordinate rank-one projections, so it is not sigma-finite. There is therefore no symmetry claim exchanging sigma-finiteness of an algebra and of its commutant. In contrast, the cyclic/separating equivalence CY01 always exchanges the algebras.

**Countably many tests but no single separating vector.** Let \(M=B(\ell^2(\mathbb N))\) in its defining representation. Its standard orthonormal basis \((e_n)\) is separating as a family: a bounded operator zero on every basis vector is zero by finite-span density. Thus CY02 constructs a faithful normal state, for example with \(\omega_{e_n}(x)=\langle xe_n,e_n\rangle\),

\[
 \varphi=\sum_{n\geq1}2^{-n}\omega_{e_n}.
 \tag{CY.11}
\]

Nevertheless no vector is separating. For every \(\xi\), choose a nonzero vector \(\eta\perp\xi\); the rank-one orthogonal projection onto \(\mathbb C\eta\) is a nonzero member of \(M\) annihilating \(\xi\). CY04 constructs a faithful normal GNS representation with a single cyclic and separating vector, but that changes the representation.

**An algebra that is not sigma-finite.** On \(\ell^2(I)\), let \(D\) consist of bounded diagonal multipliers. An operator commuting with all coordinate projections is itself diagonal, by its action on each basis vector and finite-support density. Hence \(D'=D\), so \(D\) is a von Neumann algebra. If \(I\) is uncountable its coordinate projections violate sigma-finiteness. Equivalently no countable family is separating, because the union of its countable supports misses an index whose coordinate projection annihilates the whole family. If \(I\) is countable, the basis is separating and CY02 applies. Thus this model has the exact equivalence

\[
 \begin{gathered}D\text{ sigma-finite}\\\Longleftrightarrow |I|\leq\aleph_0.\end{gathered}
 \tag{CY.12}
\]

The empty index set agrees with the zero-algebra convention above. None of these examples relies on a countable exhaustion of an arbitrary von Neumann algebra.
