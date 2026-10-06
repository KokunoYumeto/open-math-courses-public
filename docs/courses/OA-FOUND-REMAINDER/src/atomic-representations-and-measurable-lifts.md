# Atomic representations and measurable lifts

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

Pure states give irreducible representations. Taking all of them together produces the universal atomic representation. It may lose a large central part of the bidual, yet it preserves both order and norm on universally measurable self-adjoint elements.

In the other direction, every self-adjoint element of a sigma-finite represented von Neumann algebra has a universally measurable lift. We prove this by lifting projections and then summing a dyadic spectral expansion. The lift preserves norm, and positive elements have positive lifts. A non-sigma-finite example shows why the hypothesis cannot be omitted.

Use [Universal measurability and strong sequences](../reader/universal-measurability-and-strong-sequences.html) for the measurable space and its sequential closure, and [Affine approximation and quasi-state spaces](../reader/affine-approximation-and-quasi-state-spaces.html), Proposition 1.4 and Section 4, for extreme minimizers in the compact quasi-state space. The exact full [pure-state GNS proof](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#OA-FND-GN-10), Theorem 8.3, and [central-support proof](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-09), Theorem 5.3, are used on essential representation spaces; bidual normal extension remains a stated prerequisite. The full [countable-vector projection argument](../../foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html#oa-fnd-kd-14), Lemma 12.5, [dyadic expansion](../../foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html#oa-fnd-kd-04), Corollary 4.6, and [faithful normal state criterion](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-13), Theorem 9.5, supply the lift. Brown’s freely readable paper also treats the atomic representation. The order-detection and lifting arguments below are given in full.

The function model used in the last two exercises is [Abelian semicontinuity and multiplier spectra](../reader/abelian-semicontinuity-and-multiplier-spectra.html), Theorem 2.1. It identifies semicontinuous bounds by all finite positive Radon measures, before their point functions are used.

## 1. The atomic central part of the bidual

Let \(M=A^{**}\). A von Neumann algebra is atomic if every nonzero projection majorizes a nonzero minimal projection. A projection \(e\) is minimal when \(eMe=\mathbb Ce\) and \(e\ne0\).

The zero algebra and zero represented image have the asserted conclusions with zero lifts. The state arguments below treat the nonzero cases.

For every pure state \(\omega\in P(A)\), let \((\pi_\omega,H_\omega,\xi_\omega)\) be its GNS representation. Define
\[
\pi_0=\bigoplus_{\omega\in P(A)}\pi_\omega,
\qquad H_0=\bigoplus_{\omega\in P(A)}H_\omega.
\tag{1.1}
\]
This is the universal atomic representation. The representations and generated algebras below are first taken on their essential spaces, so they are nondegenerate. For a possibly degenerate representation use the weak closure \(N(\pi)=\overline{\pi(A)}^{\mathrm{uw}}\), acting as zero off the essential space; WA Lemma 2.1 gives its same central-support description.

**Lemma 1.1 — pure states and minimal supports.** The normal extension of a pure state of \(A\) has a minimal support projection in \(M\). Conversely every minimal projection in \(M\) is the support of the normal extension of a pure state of \(A\).

**Proof.** If \(\omega\) is pure, its GNS representation is irreducible by GN Theorem 8.3. Its generated von Neumann algebra is therefore \(B(H_\omega)\). Let \(z_\omega\) be its central support. The normal extension restricts to an isomorphism
\[
M z_\omega\longrightarrow B(H_\omega).
\]
Pull back the rank-one projection onto \(\mathbb C\xi_\omega\). The resulting projection \(e_\omega\) is minimal in \(M\), and
\[
\omega(X)=\langle\overline\pi_\omega(X)\xi_\omega,\xi_\omega\rangle
\quad(X\in M)
\]
has support \(e_\omega\). Indeed, it has value one there. If another projection has state value one, its represented range contains \(\xi_\omega\); hence its \(z_\omega\)-part majorizes that rank-one projection. This proves minimality of the support in the usual support ordering.

Conversely let \(e\) be minimal. There is a scalar-valued normal positive functional \(\omega\) on \(M\) defined by
\[
eXe=\omega(X)e.
\tag{1.2}
\]
Compression is normal, and evaluating its scalar corner shows that \(\omega\) is a normal state with \(\omega(e)=1\). Its restriction to \(A\) is a state: a positive approximate identity converges strongly to \(1\), so its state values tend to one. If \(0\le\psi\le\omega|_A\), normal extension preserves that inequality on \(M\). Since \(\psi(1-e)=0\), Cauchy–Schwarz removes both \(1-e\) terms and gives
\[
\psi(X)=\psi(eXe)=\omega(X)\psi(e).
\]
Thus every positive functional dominated by \(\omega|_A\) is proportional to it. If \(\omega|_A=t\rho+(1-t)\tau\) for states and \(0<t<1\), applying this to \(t\rho\) forces \(\rho=\omega|_A\), and then \(\tau=\omega|_A\). This proves purity. Also \(e\) is the support of \(\omega\). If a projection \(q\) has \(\omega(q)=1\), then \(e(1-q)e=0\). Since this is \(((1-q)e)^*((1-q)e)\), it follows that \((1-q)e=0\), or \(e\le q\). Thus \(e\) is the least projection of state value one. \(\square\)

Let \(z_0\) be the central support of \(\pi_0\). Its normal image is isomorphic to \(M z_0\). The direct sum in (1.1) has kernel equal to the intersection of its component kernels, so
\[
z_0=\bigvee_{\omega\in P(A)}z_\omega.
\tag{1.3}
\]

**Theorem 1.2.** The representation \(\pi_0\) is atomic. For any representation \(\pi\) with central support \(z\), the following are equivalent:

1. Its generated von Neumann algebra is atomic.
2. \(z\le z_0\).
3. \(\pi\) is quasi-equivalent to a direct summand of \(\pi_0\).

**Proof.** Let \(p\ne0\) be a projection in \(Mz_0\). Equation (1.3) gives a pure state \(\omega\) with \(pz_\omega\ne0\). The represented projection in \(B(H_\omega)\) contains a rank-one projection. Pulling that projection back through the isomorphism of \(Mz_\omega\) gives a minimal projection of \(M\) below \(p\). This proves atomicity of \(Mz_0\), and of every central summand \(Mz\) with \(z\le z_0\).

By Lemma 1.1, every minimal projection \(e\) of \(M\) is supported by a pure state, so \(e\le z_0\). If \(Mz\) is atomic, take a maximal orthogonal family of its minimal projections. Its strong sum must equal \(z\): a nonzero residual projection would contain another minimal projection. Since \(z\) is central, those minimal projections are also minimal in \(M\), and each lies below \(z_0\). Therefore \(z\le z_0\). This proves 1 equivalent to 2.

When \(z\le z_0\), the reducing projection \(\overline\pi_0(z)\) cuts out a direct summand of \(\pi_0\) whose central support is exactly \(z\). WA Theorem 5.3 identifies it as quasi-equivalent to \(\pi\). Conversely every reducing summand of \(\pi_0\) has central support at most \(z_0\). This proves the final equivalence. \(\square\)

For degenerate representations the theorem describes the weak generated image on the essential space, as specified after (1.1). An additional zero-action space does not add represented operators.

## 2. Order and norm seen by pure states

Write \(\overline\pi_0\) for the normal extension to \(M\), and \(\mathcal M_u(A)\) for the universally measurable self-adjoint space.

**Theorem 2.1 — order detection and isometry.** For \(a\in\mathcal M_u(A)\),
\[
\overline\pi_0(a)\ge0\quad\Longleftrightarrow\quad a\ge0,
\qquad
\|\overline\pi_0(a)\|=\|a\|.
\tag{2.1}
\]

**Proof.** Suppose \(a\) is not positive. Some normal state \(\varphi\) of \(M\), equivalently a state of \(A\), has \(\varphi(a)<0\). Choose an original semicontinuous upper bound \(x\in A_{\mathrm{sa}}^\uparrow\) with
\[
x\ge a,\qquad \varphi(x-a)<-\tfrac12\varphi(a).
\]
Then \(\varphi(x)<0\). The evaluation of \(x\) on the compact quasi-state space is lower semicontinuous and affine. Its minimum occurs at an extreme point by the affine-approximation lesson. The extreme points are zero and the pure states; zero evaluates to zero, so the negative minimum occurs at a pure state \(\omega\). Hence
\[
\omega(a)\le\omega(x)<0.
\]
The corresponding GNS vector detects a negative quadratic value of \(\overline\pi_0(a)\). Thus \(\overline\pi_0(a)\) cannot be positive. The other implication follows from positivity of the representation.

Let \(c=\|\overline\pi_0(a)\|\). Since \(1,a\) lie in the real measurable space, so do \(c1+a\) and \(c1-a\). Their images are positive. Order detection gives \(-c1\le a\le c1\), so \(\|a\|\le c\). Contractivity gives the reverse inequality. \(\square\)

**Corollary 2.2.** If \(a\in\mathcal M_u(A)\) and \(a\ge z_0\), then \(a\ge1\). In particular,
\[
z_0\ne1\quad\Longrightarrow\quad z_0\notin\mathcal M_u(A).
\tag{2.2}
\]

**Proof.** The image of \(z_0\) is the identity of the atomic generated algebra. Thus \(\overline\pi_0(a-1)\ge0\). The measurable space contains \(a-1\), so order detection gives \(a-1\ge0\). Apply this to \(a=z_0\) if that projection were measurable. \(\square\)

## 3. Measurable lifts into sigma-finite representations

Let \(\pi:A\to B(K)\) be nondegenerate, let \(N=\pi(A)''\), and suppose \(N\) is sigma-finite. Write \(z\) for its central support, so \(\overline\pi\) is an isomorphism from \(Mz\) onto \(N\).

**Theorem 3.1.** Every self-adjoint \(b\in N\) has a lift \(a\in\mathcal M_u(A)\) satisfying
\[
\overline\pi(a)=b,\qquad\|a\|=\|b\|.
\tag{3.1}
\]
If \(b\ge0\), the lift can be positive. If \(b\) is a projection, the lift can be a projection. Consequently
\[
\overline\pi(\mathcal M_u(A))=N_{\mathrm{sa}}.
\tag{3.2}
\]
For a degenerate representation the same result holds with \(N(\pi)\) as its image.

**Proof for projections.** Sigma-finiteness of \(Mz\) gives a faithful normal state there, by MI Theorem 9.5. Extend it to \(M\) by central compression; the resulting normal state has support \(z\). In the universal representation it is a vector state \(\omega_\xi\), with \(z\xi=\xi\). Faithfulness on \(Mz\) makes \(\xi\) separating for that corner.

Let \(p\in Mz\) be a projection. Apply the complete KD Lemma 12.5 in the universal representation to \(p\) and the single vector \(\xi\). It supplies a projection \(q\) that is a decreasing sequential strong limit of elements that are themselves increasing sequential strong limits of positive contractions in \(A\), with
\[
q(1-p)\xi=0,
\qquad qp\xi=p\xi.
\tag{3.3}
\]
Every inner increasing limit belongs to \(A_+^\uparrow\subset\mathcal M_u(A)\). Sequential strong closure therefore puts \(q\) in \(\mathcal M_u(A)\). Equation (3.3) gives \(q\xi=p\xi\). Since \(z\) is central,
\[
(zq-p)\xi=0,
\qquad zq-p\in Mz.
\]
The separating property forces \(zq=p\). Transporting this equality through \(\overline\pi\) lifts the corresponding projection in \(N\). The countable-vector lemma is used by its exact statement and full existing proof; no new construction of that lemma is needed. \(\square\)

**Proof for positive elements.** Work first with a positive contraction \(x\in Mz\). The complete dyadic expansion in KD Corollary 4.6, using the corner identity \(z\), gives
\[
x=\sum_{k=1}^\infty2^{-k}p_k,
\qquad p_k\in Mz\text{ projections},
\qquad
\left\|x-\sum_{k\le m}2^{-k}p_k\right\|\le2^{-m}.
\tag{3.4}
\]
That proof fixes the endpoint by assigning all binary digits of one the value one. Lift each \(p_k\) to a measurable projection \(q_k\) as above. The norm-convergent series
\[
y=\sum_{k=1}^\infty2^{-k}q_k
\tag{3.5}
\]
belongs to \(\mathcal M_u(A)\), since it is a norm-closed real space. It is a positive contraction, whether or not the chosen projections \(q_k\) commute. Central compression gives \(zy=x\). Scaling supplies a positive lift with norm at most \(\|x\|\), and contractivity of compression forces equality. \(\square\)

**Proof for self-adjoint elements.** If \(x\in(Mz)_{\mathrm{sa}}\) has norm \(r>0\), then
\[
h=\frac{x+rz}{2r}
\]
is a positive contraction. Take its positive contraction lift \(y\in\mathcal M_u(A)\), and put \(a=2ry-r1\). Then \(-r1\le a\le r1\) and \(za=x\). Thus \(\|a\|\le r\), and the image has norm \(r\), proving equality. The zero case uses \(a=0\). Identifying \(Mz\) with \(N\) proves (3.1)–(3.2). For a degenerate representation apply the result on the essential space and append the zero action; the represented weak image is exactly \(N(\pi)\). \(\square\)

The measurable lift in (3.5) sums the lifted projections. Summing the original corner projections would recover \(x\) inside \(Mz\) but would not establish its universal measurability in the original bidual.

## 4. Graded exercises with solutions

**Exercise 4.1 — introductory: quasi-equivalence need not preserve multiplicity.** Let \(A=M_2(\mathbb C)\oplus M_3(\mathbb C)\), represented on \(\mathbb C^2\oplus\mathbb C^3\) in the usual way. Determine its atomic support, compare this representation with \(\pi_0\), and identify \(\mathcal M_u(A)\).

**Solution.** The bidual is \(A\) itself. Every nonzero projection in either matrix block contains a rank-one projection, so the algebra is atomic. Pure states from the two blocks have central supports \((I_2,0)\) and \((0,I_3)\), and their join is \(z_0=1\). The defining representation and \(\pi_0\) both have support one, so they are quasi-equivalent. They are not unitarily equivalent: the defining representation acts on a five-dimensional space, while the sum of the GNS spaces of the infinitely many pure states already has infinite dimension. Constant nets give \(A_{\mathrm{sa}}\subset\mathcal M_u(A)\), and there are no further self-adjoint bidual elements. Thus \(\mathcal M_u(A)=A_{\mathrm{sa}}\).

**Exercise 4.2 — intermediate: strong nets beyond sequential closure.** For \(A=C([0,1])\), let \(e_t\) be the normal support of evaluation at \(t\). Show that the finite sums \(p_F=\sum_{t\in F}e_t\), directed by finite subsets of \([0,1]\), are measurable and increase strongly to \(z_0\). Prove that \(z_0\) is not measurable.

**Solution.** The pure states are the point evaluations. For each \(t\), continuous triangular bumps decreasing to the point indicator have a decreasing strong limit \(b_t\). Its evaluation at any finite positive Radon measure is the mass at \(\{t\}\). The squared bumps have the same limiting integrals; bounded strong functional calculus and separation by normal functionals give \(b_t^2=b_t\).

For \(g\in C([0,1])\), continuity at \(t\) gives \(\|(g-g(t))\,\text{bump}_n\|\to0\), so \(gb_t=g(t)b_t\). Ultraweak density of \(A\) in \(M\) now gives \(b_tMb_t=\mathbb Cb_t\). This is a nonzero minimal projection, and its compressed state restricts to evaluation at \(t\). Lemma 1.1 identifies its support with \(e_t\), so \(b_t=e_t\). Thus \(e_t\in A_{\mathrm{sa}}^\downarrow\subset\mathcal M_u(A)\). Distinct supports are orthogonal, and finite sums are measurable projections by linearity.

Since the pure GNS spaces are one dimensional, these minimal projections are also their central supports. Equation (1.3) gives \(p_F\uparrow z_0\). The normal extension of Lebesgue probability measure has value zero at every \(p_F\), and hence at their supremum by normality. It has value one at the bidual identity, so \(z_0\ne1\). Corollary 2.2 excludes \(z_0\) from \(\mathcal M_u(A)\). Thus the space is sequentially strongly closed but need not be strongly closed under arbitrary nets.

**Exercise 4.3 — advanced: the sigma-finite hypothesis is necessary.** Let \(A=C([0,1])\) act diagonally on \(\ell^2([0,1])\) by point evaluation. Show that its generated algebra is \(\ell^\infty([0,1])\), and construct a projection there that is not the image of any element of \(\mathcal M_u(A)\).

**Solution.** A matrix entry of an operator commuting with every continuous diagonal function must vanish between distinct points, because continuous functions separate them. The commutant is therefore exactly the bounded diagonal algebra, which is its own commutant. This proves the generated algebra is \(\ell^\infty([0,1])\). It is not sigma-finite, since its coordinate projections are an uncountable orthogonal family of nonzero projections.

We first show that the point function \(f(t)=\delta_t(a)\) of any \(a\in\mathcal M_u(A)\) is measurable for the completion of every finite positive Radon measure \(\mu\). Normalize a nonzero measure to a state, and choose original bounds \(y_n\le a\le x_n\) with \(\mu(x_n-y_n)\to0\). The abelian function model identifies their point functions with bounded upper and lower semicontinuous functions \(\ell_n\) and \(u_n\). Thus
\[
\ell_n\le f\le u_n,
\qquad\int(u_n-\ell_n)\,d\mu\longrightarrow0.
\]
Put \(\ell=\sup_n\ell_n\) and \(u=\inf_nu_n\). These are finite Borel functions: they are squeezed around the bounded \(f\), while the first pair supplies finite outer bounds. Moreover \(0\le u-\ell\le u_n-\ell_n\) for every \(n\), so its integral is zero. Hence \(\ell=f=u\) off a Borel null set, proving completed measurability.

Choose one representative from each equivalence class of \([0,1]\) under \(s\sim t\) when \(s-t\in\mathbb Q\), and call the set \(V\). It is not Lebesgue measurable, including for the completed measure. Its distinct translates by rational numbers in \([-1,1]\) are disjoint, their union contains \([0,1]\), and they are all contained in \([-1,2]\). If \(V\) had zero measure, that countable union could not cover an interval of measure one. If it had positive measure, arbitrarily many disjoint translates would exceed the finite measure of \([-1,2]\). Both cases are impossible.

The indicator \(1_V\) is nevertheless a bounded diagonal projection in the generated algebra. If it were the image of \(a\in\mathcal M_u(A)\), its point function would be \(1_V\) and would be Lebesgue measurable by the preceding argument. This contradiction proves that the image equality in Theorem 3.1 fails without sigma-finiteness.

## 5. Historical setting of the chapter

The chapter connects three descriptions of an operator algebra: its algebraic operations, its normal functionals, and the topology of its representations. This historical overview retains the named contributors and results explained in the existing prerequisite lessons. Freely readable primary examples are [Takeda 1954], whose opening explicitly records Sherman's announcement and his own proof, [Sakai 1956], whose introduction states the dual-space characterization, and [Tomiyama 1957], whose Theorem 2 derives that characterization from the norm-one projection theorem. These papers provide historical context here; the mathematical inputs are the precise programme arguments linked above.

For abelian algebras, Stone's Boolean-ring methods explain why complete projection lattices lead to stonean spectra. Dixmier developed the distinction between stonean and hyperstonean spaces, where enough normal measures recover a von Neumann algebra. The countably generated diffuse model is attributed to Halmos and von Neumann, and the sequential functional argument is Phillips's lemma. These subjects are treated in [Abelian operator algebras](../../foundations-of-von-neumann-algebras/abelian-operator-algebras.html), Sections 4–8 and 10, with their proofs and historical references.

The bidual construction is the Sherman–Takeda theorem: Sherman announced it, and Takeda supplied the proof. Kaplansky's AW*-algebras separated projection-lattice properties from the additional requirements of a von Neumann algebra. Takeda's representation work and Banach-space duality led to Sakai's characterization of W*-algebras; Tomiyama's norm-one projection theorem supplies the proof used by Takesaki. Kadison's monotone-closed characterization connects this direction to Pedersen's up-down approximation problem. Takesaki's normal/singular decomposition and singularity criterion, together with Dixmier's uniqueness of the predual, show how much of the normal topology is determined by the algebra. These results and attributions are retained in [The universal enveloping von Neumann algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html), Sections 3 and 8–13.

For the predual itself, the polar-decomposition results are associated with Sakai and Tomita. The weak-compactness criterion combines work of Grothendieck, Sakai, Takesaki, Umegaki and Akemann. Sakai studied the Mackey topology on bounded parts of finite von Neumann algebras; Akemann supplied its general characterization. The complete proofs and references appear in [Polar decomposition and topological properties of the predual](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#OA-FND-PD-02), Sections 2, 8 and 10–11. On bounded parts of a general von Neumann algebra the resulting operator topology is sigma-strong-star; in the finite case the sigma-strong formulation agrees there.

The semicontinuity concepts for elements of the bidual come from Pedersen's work on weak-star semicontinuity (1972) and from Akemann and Pedersen (1973), who distinguished three notions of semicontinuity and analysed their complications; [Brown, semicontinuity] recalls these notions and develops them on closed faces of the quasi-state space. Busby's double-centralizer and extension theory introduced the multiplier-algebra formulation [Busby 1968], following Johnson's general theory of centralizers (1964), which [Daws 2010] surveys for Banach algebras. The multiplier lesson makes the essential-ideal detection explicit, while the measurable-space lessons distinguish sequential strong limits from arbitrary strong nets.

This approximation viewpoint also explains the chapter's final question about a noncommutative counterpart of Borel theory. The original C*-algebra remembers continuity; its bidual contains many additional operators. Semicontinuous bounds and state-measured gaps give intermediate classes tied to the original algebra. The measurable lift theorem passes to sigma-finite representations without losing norm, while Exercise 4.3 shows that the full point-diagonal representation can contain functions beyond this universally measurable class. This is a concrete reason to keep the approximation class and the represented von Neumann algebra distinct.

## References

[Brown] Lawrence G. Brown, *Large C\*-algebras of universally measurable operators*, [arXiv:1309.6306v1](https://arxiv.org/abs/1309.6306v1), 24 September 2013; *Quarterly Journal of Mathematics* 65 (2014), 851–855.

[Takeda 1954] Ziro Takeda, *Conjugate Spaces of Operator Algebras*, *Proceedings of the Japan Academy* 30 (1954), 90–95. [Free primary article](https://www.jstage.jst.go.jp/article/pjab1945/30/2/30_2_90/_pdf).

[Sakai 1956] Shoichiro Sakai, *A characterization of W\*-algebras*, *Pacific Journal of Mathematics* 6 (1956), 763–773. [Free primary article](https://msp.org/pjm/1956/6-4/pjm-v6-n4-p11-s.pdf).

[Tomiyama 1957] Jun Tomiyama, *On the Projection of Norm One in W\*-algebras*, *Proceedings of the Japan Academy* 33 (1957), 608–612. [Free primary article](https://www.jstage.jst.go.jp/article/pjab1945/33/10/33_10_608/_pdf/-char/ja).

[Brown, semicontinuity] Lawrence G. Brown, *Semicontinuity and closed faces of C\*-algebras*, [arXiv:1312.3624](https://arxiv.org/abs/1312.3624), 2013.

[Busby 1968] R. C. Busby, Double centralizers and extensions of C*-algebras, *Transactions of the American Mathematical Society* 132 (1968), 79–99. [PDF](https://www.ams.org/journals/tran/1968-132-01/S0002-9947-1968-0225175-5/S0002-9947-1968-0225175-5.pdf).

[Daws 2010] Matthew Daws, *Multipliers, self-induced and dual Banach algebras*, [arXiv:1001.1633v4](https://arxiv.org/abs/1001.1633v4), 2010; *Dissertationes Mathematicae* 470 (2010).
