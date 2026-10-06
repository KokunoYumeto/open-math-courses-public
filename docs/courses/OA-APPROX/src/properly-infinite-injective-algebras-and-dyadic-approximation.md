# Properly infinite injective algebras and dyadic approximation

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

Finite completely positive models record operators in a matrix algebra. In a properly infinite algebra, their reconstruction map can be implemented by one isometry. Approximating that isometry by unitaries then moves the matrix algebra itself into a position that approximates the original operators.

We use the equivalence of injectivity and semidiscreteness proved in [Averaging, crossed products, and injectivity](averaging-crossed-products-injectivity.md), the Choi matrix criterion in [Completely positive finite models](completely-positive-finite-models.md), and standard form from OA-MOD. The projection facts are the existing foundations inputs: halving a properly infinite projection, projection comparison and projection Schroeder–Bernstein. The central finite-part criterion for projections and finite absorption are used in (8): a projection with no nonzero finite central summand in its central support is properly infinite. These facts imply a partition of the properly infinite identity into countably many projections equivalent to it. No general weight construction enters this lesson.

Here is the countable-partition argument, including its possible residual projection. Repeated proper halving gives orthogonal projections \(p_j\sim1\) and decreasing remainders \(r_j\sim1\), with
\[
1=p_1+\cdots+p_j+r_j.
\]
Let \(r_\infty=\bigwedge_jr_j\). The projections \(p_1+r_\infty,p_2,p_3,\ldots\) sum strongly to one. Since
\(p_1\le p_1+r_\infty\le1\) and \(p_1\sim1\), projection Schroeder–Bernstein makes \(p_1+r_\infty\sim1\). Thus the residual is absorbed and the asserted partition has every member equivalent to one. This argument uses neither a faithful state nor separability.

Write
\[
\|x\|_\varphi^\#=\left(\frac{\varphi(x^*x)+\varphi(xx^*)}{2}\right)^{1/2}.
\tag{1}
\]
Here \(\varphi\) is a normal state, and \(\xi_\varphi\) its standard-form vector. Local **AFD** means approximation of each finite set in each sigma-strong* neighborhood by one finite-dimensional *-subalgebra. Separability below means separability of the predual. Local AFD makes sense without it; an increasing sequence is a stronger organizational conclusion for which we will explicitly assume it.

## 1. A unitary can converge strongly to an isometry

**Lemma 1.1.** In any von Neumann algebra \(M\), the sigma-strong closure of \(\mathcal U(M)\) is the set of isometries.

**Proof.** If unitaries converge strongly to \(v\), then \(\|v\eta\|=\|\eta\|\) for every vector, so \(v^*v=1\). Conversely let \(v^*v=1\), set
\[
e=1-vv^*,\quad e_j=v^{j-1}e(v^*)^{j-1},\quad
f=1-\sum_{j\ge1}e_j.
\]
The \(e_j\)'s are orthogonal: \(ev=0\), hence \(e(v^*)^r e=0\) and \(ev^r e=0\) for positive \(r\). Also \(ve_jv^*=e_{j+1}\) and \(vfv^*=f\); on \(f\), the operator \(vf\) is unitary. Define
\[
w_n=v\sum_{j=1}^n e_j+(v^*)^n e_{n+1}
       +\sum_{j\ge n+2}e_j+vf.
\tag{2}
\]
On the first \(n+1\) wandering spaces this is a cyclic permutation, using \(v\) to move one step forward and \((v^*)^n\) to return to the first space. It is the identity on the remaining wandering spaces and \(vf\) on \(f\). Initial and final projections of these partial isometries are orthogonal partitions of one. Thus \(w_n^*w_n=w_nw_n^*=1\).

The difference from \(v\) vanishes on \(f+\sum_{j\le n}e_j\). Therefore
\[
\|(w_n-v)\eta\|\le2\left\|\sum_{j\ge n+1}e_j\eta\right\|\longrightarrow0.
\tag{3}
\]
The same estimate in a countable Hilbert-space amplification proves sigma-strong convergence, since its vector tests are exactly square-summable families of vector tests. This argument also covers \(e=0\). \(\square\)

An isometry with nonzero range defect cannot be a strong* limit of unitaries: strong* convergence would give both \(v^*v=1\) and \(vv^*=1\). We will use only the strong convergence in Lemma 1.1.

**Lemma 1.2.** In a properly infinite \(M\), there are isometries \(u_n\to1\) sigma-strong* whose defects \(q_n=1-u_nu_n^*\) satisfy \(q_n\sim1\) and \(q_n\to0\) sigma-strong.

**Proof.** Choose orthogonal \(p_j\sim1\) with sum one, and put \(r_n=\sum_{j\ge n}p_j\). Both \(r_n\) and \(r_n-p_n\) are equivalent to one: each dominates a projection equivalent to one and is bounded above by one. Projection Schroeder–Bernstein gives the assertion. Choose \(a_n\) with \(a_n^*a_n=r_n\), \(a_na_n^*=r_n-p_n\), and put \(u_n=1-r_n+a_n\). Then \(u_n^*u_n=1\), \(q_n=p_n\), and
\[
\|(1-u_n)\eta\|\le2\|r_n\eta\|,\qquad
\|(1-u_n^*)\eta\|\le2\|r_n\eta\|,\qquad
\|q_n\eta\|\le\|r_n\eta\|.
\tag{4}
\]
The tails decrease strongly to zero; square-summable vector tests give the stated topologies. Thus the errors can be made small on any prescribed finite collection of vectors at once. \(\square\)

## 2. Membership from possibly unbounded approximants

**Lemma 2.1.** Let \(N\subset M\) be a unital von Neumann subalgebra and \(\varphi\) a faithful normal state. If \(x_n\in N\) and \(\|x_n-x\|_\varphi^\#\to0\), then \(x\in N\). No bound on \(\|x_n\|\) is required.

**Proof.** Splitting real and imaginary parts reduces to self-adjoint \(x_n,x\). Set \(\eta=(x+i)\xi_\varphi\). Resolvent multiplication gives
\[
\bigl((x_n+i)^{-1}-(x+i)^{-1}\bigr)\eta
=(x_n+i)^{-1}(x-x_n)\xi_\varphi\longrightarrow0,
\tag{5}
\]
because the first resolvent has norm at most one. The vector \(\eta\) is separating for \(M\): if \(b\eta=0\), faithfulness of \(\varphi\) implies \(b(x+i)=0\), hence \(b=0\).

A separating vector is cyclic for \(M'\). Indeed the projection onto \(\overline{M'\eta}\) belongs to \(M\); its complement annihilates \(\eta\) and is therefore zero. A uniformly bounded sequence in \(M\) converging on \(\eta\) converges strongly on \(M'\eta\), by commutation, and then on the whole Hilbert space by density. This applies to the resolvent differences in (5). Their limit \((x+i)^{-1}\) belongs to \(N\). A unital C*-subalgebra is inverse closed; inverting this element shows \(x+i\in N\), hence \(x\in N\). Apply this conclusion to both self-adjoint parts. \(\square\)

The same cyclic-commutant argument shows that, on bounded sets, the seminorm (1) for a faithful normal state determines sigma-strong* convergence. It does not assert that the original unbounded approximants in Lemma 2.1 converge in that topology.

## 3. Replacing a finite algebra by a dyadic subfactor

**Lemma 3.1.** If a properly infinite algebra is locally AFD, every finite set can be approximated in any sigma-strong* neighborhood by a unital matrix subfactor \(M_{2^k}\). Its size can be required to exceed any fixed bound.

**Proof.** First approximate by a finite-dimensional unital algebra \(D\), adjoining \(1\) if necessary. Write its matrix systems as \(e_{ij}^{(a)}\), with block sizes \(d_a\), and put \(t=\sum_a d_a\). Lemma 1.2 gives an isometry \(u\) close enough to one that \(uzu^*\) is close to \(z\) for each of the finitely many chosen \(z\in D\), with small defect \(q=1-uu^*\sim1\).

Choose \(2^k>t\). Partition \(q\) into \(2^k\) projections equivalent to one. For the first \(t\) projections choose block matrix systems \(g_{ij}^{(a)}\) with the same sizes as \(D\). Then
\[
f_{ij}^{(a)}=ue_{ij}^{(a)}u^*+g_{ij}^{(a)}
\tag{6}
\]
are orthogonal block matrix systems. For \(z=\sum\lambda_{ij}^{(a)}e_{ij}^{(a)}\), put \(\rho(z)=\sum\lambda_{ij}^{(a)}g_{ij}^{(a)}\). This *-homomorphism has norm at most one, range supported on \(q\), and
\[
\rho(z)^*\rho(z),\ \rho(z)\rho(z)^*\le\|z\|^2q.
\tag{7}
\]
Thus \(\rho(z)\) tends to zero in every specified strong* test as \(q\) does. The new approximant \(uzu^*+\rho(z)\) is close to \(z\).

Every diagonal projection in (6) is equivalent to one, since it dominates the corresponding \(g_{ii}^{(a)}\sim1\). Include the unused defect projections too. There are \(2^k\) mutually equivalent diagonals summing to one. They extend to a full matrix system respecting all the prescribed block connections: choose a reference diagonal, connect it to the first diagonal of each block, and use that block's existing matrix units to connect to its other diagonals. If these connecting partial isometries are \(v_j\), the operators \(v_iv_j^*\) are the desired system. Its span contains every new approximant. Choosing the original error and the two new errors sufficiently small proves the lemma. \(\square\)

**Theorem 3.2.** For properly infinite \(M\) with separable predual, local AFD is equivalent to generation by an increasing sequence \(A_k\cong M_{2^k}\).

**Proof.** An increasing generating sequence gives local approximation by Kaplansky density. Conversely choose a faithful normal state \(\varphi\) and a sigma-strong* dense sequence \((x_j)\) in the unit ball. Such a sequence exists for separable predual: the standard representation is separable and its bounded strong* balls are metrizable and separable.

Suppose a unital dyadic subfactor \(A\cong M_d\) has already been chosen, with units \(e_{ij}\). Matrix coordinates identify
\[
M\cong M_d\bar\otimes e_{11}Me_{11},\qquad
C=A'\cap M\cong e_{11}Me_{11}.
\tag{8}
\]
The projection \(e_{11}\) is properly infinite. A finite nonzero central cut of it would make the corresponding sum of its \(d\) equivalent cuts finite, contrary to proper infiniteness of \(M\). A properly infinite projection absorbs finitely many equivalent copies of itself; consequently \(e_{11}\sim1\). Thus \(C\cong M\), so \(C\) is properly infinite and locally AFD.

Write the next finitely many \(x_j\)'s as \(\sum_{r,s}b_{rs}^{(j)}e_{rs}\), with \(b_{rs}^{(j)}\in C\). Multiplication by any fixed operator is continuous for sigma-strong*: its seminorms are bounded by finitely many seminorms obtained from normal positive functionals. Lemma 3.1 in \(C\) therefore gives a dyadic \(B\subset C\) and coefficients in \(B\) whose reconstructed sums approximate the \(x_j\)'s within \(1/n\) in (1). The algebra \(A\vee B\cong A\otimes B\) is a larger dyadic factor containing \(A\) exactly. This constructs increasing \(N_n\), with approximants to the first \(n\) elements and errors tending to zero.

Let \(P=(\bigcup_nN_n)''\). Lemma 2.1 puts every \(x_j\) in \(P\), without imposing bounds on the reconstructed sums. Density and closedness give \(P=M\). Between successive dyadic matrix sizes insert the missing \(M_2\) tensor levels of their finite-dimensional relative commutants, and insert the initial levels inside \(N_1\). This gives all the sizes \(2^k\). \(\square\)

## 4. A finite CP reconstruction is one compression

**Lemma 4.1.** Let \(D\cong M_m\) be a unital subfactor of \(M\). Every cp \(T:D\to M\) has
\[
T(x)=\sum_{k,\ell=1}^m a_{k\ell}^*xa_{k\ell}.
\tag{9}
\]
If \(M\) is properly infinite, it also has \(T(x)=v^*xv\) for one \(v\in M\). If \(T\) is unital, \(v\) is an isometry.

**Proof.** The Choi matrix \([T(e_{ij})]\) is positive. Write its positive square root as \([b_{ki}]\), so \(T(e_{ij})=\sum_kb_{ki}^*b_{kj}\). Put \(a_{k\ell}=\sum_i e_{i\ell}b_{ki}\). Matrix-unit multiplication gives
\[
a_{k\ell}^*e_{ij}a_{k\ell}=b_{ki}^*e_{\ell\ell}b_{kj}.
\]
Summing \(k,\ell\) proves (9). In the properly infinite case, (8) makes \(D'\cap M\) properly infinite. Choose \(m^2\) isometries \(s_{k\ell}\) there with orthogonal ranges, and set \(v=\sum s_{k\ell}a_{k\ell}\). Commutation with \(D\) and \(s_{k\ell}^*s_{rs}=\delta_{kr}\delta_{\ell s}1\) give \(v^*xv=T(x)\). At \(x=1\) the unital case gives \(v^*v=1\). \(\square\)

**Theorem 4.2.** Every properly infinite injective von Neumann algebra is locally AFD. If its predual is separable, it is generated by an increasing dyadic sequence as in Theorem 3.2.

**Proof.** Semidiscreteness supplies normal ucp recording maps \(S_i:M\to M_{m_i}\) and cpc reconstruction maps \(T_i\), with \(T_iS_i\to\mathrm{id}\) sigma-strong* pointwise. Both maps can be made unital. Choose a state \(\omega_i\) on \(M_{m_i}\) and replace
\[
T_i(z)\quad\hbox{by}\quad T_i(z)+\omega_i(z)(1-T_i(1)).
\tag{10}
\]
This is ucp. Since \(T_i(1)=T_iS_i(1)\to1\) and \(|\omega_i(S_i(x))|\le\|x\|\), the correction tends to zero in every strong* test. It preserves the approximation.

It suffices to approximate finitely many unitaries \(U_j\): every operator is a linear combination of four unitaries, by writing each self-adjoint contraction as the real part of \(a+i(1-a^2)^{1/2}\). Fix a normal state \(\varphi\) and a small \(\theta>0\). Finitely many normal-functional tests can be dominated by a scalar multiple of one such state, so this handles any requested neighborhood. Choose a unital factorization with
\(\|T S(U_j)-U_j\|_\varphi^\#<\theta\). Embed its matrix algebra unitally as \(D\subset M\), and use Lemma 4.1 to write \(T(z)=v^*zv\), with \(v^*v=1\). Set \(z_j=S(U_j)\); these are contractions.

With inner products linear in the second variable,
\[
\operatorname{Re}\langle vU_j\xi_\varphi,z_jv\xi_\varphi\rangle>1-\sqrt2\theta.
\tag{11}
\]
Indeed its difference from \(1\) is bounded by \(\|(v^*z_jv-U_j)\xi_\varphi\|\). The same estimate holds for \(U_j^*,z_j^*\). Lemma 1.1 gives unitaries converging strongly to \(v\), on both \(\xi_\varphi\) and \(U_j\xi_\varphi,U_j^*\xi_\varphi\). Choose one \(w\) such that both real parts remain greater than \(1-(\sqrt2+1)\theta\). Since the compared vectors have norms at most one,
\[
\|w^*z_jw-U_j\|_\varphi^\#
<\bigl(2(\sqrt2+1)\theta\bigr)^{1/2}.
\tag{12}
\]
Taking \(\theta\) sufficiently small gives the desired approximation inside the finite-dimensional subfactor \(w^*Dw\). No faithful state or separability was needed for this local conclusion. Apply Theorem 3.2 when the predual is separable. \(\square\)

## 5. Problems with complete solutions

**Exercise 1.** For the unilateral shift \(v\) on \(\ell^2(\mathbb N)\), describe the unitaries (2) and verify (3) directly.

*Solution.* The defect is the first coordinate, and \(e_j\) is the \(j\)-th coordinate projection. The unitary cycles coordinates \(1,\ldots,n+1\), sends the last back to the first, and fixes all later coordinates. It agrees with the shift on the first \(n\) coordinates. Thus its difference from the shift has norm at most two and annihilates that initial span, giving exactly the tail bound (3).

**Exercise 2.** Explain why the same unitaries do not converge strong* to the shift.

*Solution.* The shift adjoint annihilates the first basis vector, whereas each cycling unitary's adjoint sends it to the \((n+1)\)-st basis vector, of norm one. Strong convergence of the adjoints fails. Alternatively a strong* limit would preserve the identity \(w_nw_n^*=1\), while the shift has a one-dimensional range defect.

**Exercise 3.** Prove the two estimates in (4) involving \(u_n\) and \(u_n^*\).

*Solution.* Both differences are supported on \(r_n\): the partial isometry and its adjoint have initial and final projections below \(r_n\). On that space each difference is the difference of two contractions, hence has norm at most two. Apply this to \(r_n\eta\). Outside that space the differences vanish.

**Exercise 4.** Give unbounded approximants converging in a faithful-state norm, and explain why a boundedness argument would miss them.

*Solution.* In \(L^\infty[0,1]\) with the integration state take \(x_n=n1_{[0,n^{-4}]}\). Their operator norms are \(n\), while their \(2\)-norms are \(1/n\); adjoints are the same, so (1) tends to zero. They lie outside every fixed operator-norm ball. Lemma 2.1 applies through their uniformly bounded resolvents rather than through boundedness of the original sequence.

**Exercise 5.** Why does a bounded sequence converging on a separating vector converge strongly on every vector?

*Solution.* For \(a'\in M'\), \(b_n a'\eta=a'b_n\eta\to0\) if \(b_n\eta\to0\). The vectors \(a'\eta\) are dense because \(\eta\) is separating. If \(\sup\|b_n\|=C\), approximating a vector by such a vector gives an error at most \(C\) times the approximation error, uniformly in \(n\). First take the limit in \(n\), then make the density error tend to zero.

**Exercise 6.** Verify (7), including its adjoint version, without assuming a trace.

*Solution.* The homomorphism \(\rho\) is contractive and supported on \(q\). Thus \(\rho(z)^*\rho(z)\) is positive, supported on \(q\), and has norm at most \(\|z\|^2\), giving the first inequality. Apply the same argument to \(z^*\). Consequently (1) is at most \(\|z\|\varphi(q)^{1/2}\) for every normal state, whether tracial or not.

**Exercise 7.** Explain why the relative-commutant step in Theorem 3.2 gives exact containment of the old factor.

*Solution.* The new matrix factor \(B\) lies in \(A'\cap M\), so it commutes with \(A\). Matrix coordinates (8) identify their generated algebra with \(M_d\otimes B\), a full matrix algebra with the shared identity. The inclusion of \(A\) is its first tensor leg, so every old matrix unit is retained exactly; only the other leg is being approximated.

**Exercise 8.** Check the reconstruction formula (9) on a matrix unit.

*Solution.* Expand \(a_{k\ell}^*e_{ij}a_{k\ell}\). In the product \(e_{\ell r}e_{ij}e_{s\ell}\), the nonzero term requires \(r=i,s=j\), and equals \(e_{\ell\ell}\). The result is \(b_{ki}^*e_{\ell\ell}b_{kj}\). Summing over \(\ell\) gives \(b_{ki}^*b_{kj}\), and summing over \(k\) gives \(T(e_{ij})\), as required.

**Exercise 9.** Why does (10) preserve complete positivity and convergence?

*Solution.* A positive scalar functional is cp, and multiplication of its scalar values by the fixed positive element \(1-T_i(1)\) is cp at every matrix size. Their sum with \(T_i\) is cp and has unit value one. The composite correction is a scalar of modulus at most \(\|x\|\) times \(1-T_i(1)\), which tends to zero sigma-strong*. Both incoming and outgoing maps therefore become unital without losing the finite approximation.

**Exercise 10.** Derive (12) from the two real-part bounds following (11).

*Solution.* Put \(c=(\sqrt2+1)\theta\). The vectors \(wU_j\xi\) have norm one and \(z_jw\xi\) have norm at most one. Their squared difference is at most \(2-2(1-c)=2c\). The same bound holds with both operators adjointed. Conjugating by \(w^*\) gives the two vector errors defining (1); their squared average is at most \(2c\). Taking square roots gives (12).

## References and proof scope

George A. Elliott and E. J. Woods, [*The equivalence of various definitions for a properly infinite von Neumann algebra to be approximately finite dimensional*](https://www.ams.org/journals/proc/1976-060-01/S0002-9939-1976-0512370-0/S0002-9939-1976-0512370-0.pdf), *Proceedings of the American Mathematical Society* **60** (October 1976), 175–178, DOI [10.1090/S0002-9939-1976-0512370-0](https://doi.org/10.1090/S0002-9939-1976-0512370-0). Lemma 1 on printed p.175 constructs an isometry close to one with a small defect equivalent to one. Lemma 2 on p.176 proves membership from potentially unbounded approximants by using resolvents and a separating vector. Theorem 3, pp.176–178, proves dyadic finite-factor replacement and increasing dyadic assembly for a properly infinite algebra on a separable Hilbert space. The proofs above give the normal-state formulation, explicit matrix-system extension, and exact containment through the relative commutant. Separability is used for the generating sequence, while the local replacement remains valid without it.

Uffe Haagerup, [*A new proof of the equivalence of injectivity and hyperfiniteness for factors on a separable Hilbert space*](https://doi.org/10.1016/0022-1236(85)90002-3), *Journal of Functional Analysis* 62 (1985), 160–201. Proposition 2.1 and Theorem 2.2 develop the internal matrix reconstruction and isometry-conjugation method. Here the matrix calculation is given explicitly, the isometry is approximated by a constructed unitary sequence, and the local conclusion retains arbitrary properly infinite algebras. The dyadic assembly and exact containment arguments are proved above, with separable predual required for the generating sequence. The finite injective converse is developed separately. The existing programme lesson *Injective von Neumann algebras*, Sections 2 and 4, supplies the declared abstract injectivity and permanence prerequisites; its directed AFD statement does not supply the local-to-sequential construction proved here.
