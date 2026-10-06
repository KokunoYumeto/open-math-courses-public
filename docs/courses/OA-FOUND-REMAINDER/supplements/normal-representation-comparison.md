# Comparing normal representations with properly infinite commutants

*Written by Claude Opus 5.5 (Anthropic), September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

This chapter develops the joint-algebra comparison and properly infinite commutant theorem. Results are referred to by their numbers below. The proofs use projection comparison, normal functionals and normal amplification; no trace-coupling or general standard-form theorem is an input. Selection and route notes: GPT-6.1 Sol (OpenAI), Ultra, October 2026; new notes CC0.

## 1. Conventions

\(H\) is a complex Hilbert space, and inner products \(\langle\cdot,\cdot\rangle\) are linear in the first variable. \(M\subseteq B(H)\) is a von Neumann algebra, \(M'\) its commutant, and \(Z=M\cap M'\) its centre. For \(S\subseteq B(H)\) and \(X\subseteq H\), \([SX]\) is the closed linear span of the vectors \(x\xi\) with \(x\in S\), \(\xi\in X\), and we identify a closed subspace with the projection onto it. We write \(\omega_\xi(x)=\langle x\xi,\xi\rangle\) and \(\omega_{\eta,\xi}(x)=\langle x\eta,\xi\rangle\). \(M_*\) is the space of normal (\(\sigma\)-weakly continuous) linear functionals on \(M\), and \(M_*^+\) its positive part.

*Projections.* \(\mathcal P(M)\) is the set of projections of \(M\). Equivalence \(e\sim f\), subequivalence \(e\precsim f\), finite, infinite and properly infinite projections, and the central support \(c(e)\) (the least central projection majorizing \(e\)) are as in [Projections and types of von Neumann algebras](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html). \(M\) is *\(\sigma\)-finite* if every family of mutually orthogonal nonzero projections in \(M\) is countable, and a projection \(e\) is \(\sigma\)-finite if \(eMe\) is.

*Cyclic projections.* For \(\xi\in H\), \(p_\xi\in M\) is the projection onto \([M'\xi]\) and \(p'_\xi\in M'\) the projection onto \([M\xi]\). We call the projections of the form \(p_\xi\) the *cyclic projections* of \(M\), and those of the form \(p'_\xi\) the cyclic projections of \(M'\). A vector \(\xi\) is *cyclic* for \(M\) if \(p'_\xi=1\), and *separating* for \(M\) if \(x\in M\), \(x\xi=0\) imply \(x=0\).

*Reduced and induced algebras.* For \(e\in\mathcal P(M)\), the *reduced algebra* is \(M_e=eMe\), acting on \(eH\). For \(e'\in\mathcal P(M')\), the *induced algebra* is \(M_{e'}=\{x_{e'}:x\in M\}\), acting on \(e'H\), where \(x_{e'}=xe'|_{e'H}\); the map \(x\mapsto x_{e'}\) is the *induction*. If \(e\in\mathcal P(M)\) and \(e'\in\mathcal P(M')\), then \(ee'\) is a projection, and \(M_{ee'}\) denotes the algebra of the restrictions \(x|_{ee'H}\), \(x\in eMe\), acting on \(ee'H\).

*Representations.* A *normal representation* of \(M\) on a Hilbert space \(K\) is a unital \(*\)-homomorphism \(\pi:M\to B(K)\) that is \(\sigma\)-weakly continuous. Two representations \(\pi_1,\pi_2\) on \(K_1,K_2\) are *unitarily equivalent*, \(\pi_1\simeq\pi_2\), if some unitary \(U:K_1\to K_2\) satisfies \(U\pi_1(x)=\pi_2(x)U\) for all \(x\). A *subrepresentation* is the restriction of a representation to a closed invariant subspace. The notation \(\{M,H\}\cong\{N,K\}\) means that some unitary \(W:H\to K\) satisfies \(WMW^*=N\). An isomorphism \(\pi:M\to N\) of von Neumann algebras is *spatial* if \(\pi(x)=WxW^*\) for such a \(W\).

## 2. Background used without proof

The following results are used as stated.

**Fact 2.1** (Reduced and induced algebras, central supports). Let \(e\in\mathcal P(M)\) and \(e'\in\mathcal P(M')\).

1. \(eMe\) and \(M'e\) (restricted to \(eH\)) are von Neumann algebras on \(eH\) and each is the commutant of the other. Likewise \(M_{e'}\) and \(e'M'e'\) are mutual commutants on \(e'H\).
2. \(c(e)\) is the projection onto \([MeH]\). For a central projection \(z\), \(ze=0\) if and only if \(zc(e)=0\), and \(c(ze)=zc(e)\). Equivalent projections have the same central support.
3. The induction \(x\mapsto x_{e'}\) is a \(*\)-homomorphism of \(M\) onto \(M_{e'}\) with kernel \(M(1-c(e'))\), where \(c(e')\) is the central support of \(e'\) in \(M'\). Likewise \(x'\mapsto x'e|_{eH}\) maps \(M'\) onto \(M'e\) with kernel \(M'(1-c(e))\).
4. The centre of \(eMe\) is \(Ze\), and \(a\mapsto ae\) is an isomorphism of \(Zc(e)\) onto it.

These are proved in [Projections and types of von Neumann algebras](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html#oa-fnd-ty-02) (Proposition 3.5) and [The double commutant theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-08).

**Fact 2.2** (Comparison of projections). The following are proved in [Projections and types of von Neumann algebras](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html).

1. (*Additivity*, Lemma 3.3.) If \(\{e_i\}\), \(\{f_i\}\) are families of mutually orthogonal projections with \(e_i\sim f_i\) (or \(e_i\precsim f_i\)), then \(\sum_ie_i\sim\sum_if_i\) (or \(\precsim\)). Central cuts preserve \(\sim\) and \(\precsim\).
2. (*Parallelogram law*, Proposition 4.4.) \((e\vee f)-e\sim f-(e\wedge f)\).
3. (*Schröder–Bernstein*, Proposition 5.1.) \(e\precsim f\) and \(f\precsim e\) imply \(e\sim f\).
4. (*Equivalent pieces*, Lemma 5.3.) If \(c(e)c(f)\ne0\), there are nonzero \(e_1\le e\), \(f_1\le f\) with \(e_1\sim f_1\).
5. (*Comparison theorem*, Theorem 5.5.) For projections \(e,f\) there is a central projection \(z\) with \(ze\precsim zf\) and \((1-z)f\precsim(1-z)e\).
6. (*Finite and properly infinite parts*, Theorem 7.2.) Every projection is \(e_1+e_2\) with \(e_1\) finite, \(e_2\) properly infinite and \(c(e_1)c(e_2)=0\). For \(e=1\) this gives central projections \(z_f+z_\infty=1\) with \(Mz_f\) finite and \(Mz_\infty\) properly infinite. \(M\) has central projections \(z_{\rm I},z_{\rm II},z_{\rm III}\) with sum \(1\) cutting out its parts of types I, II and III; they are unique.
7. (*Matrix algebras*, Lemma 8.2 and Proposition 8.4.) For a von Neumann algebra \(N\) on \(K\), \((N\otimes1)'\) on \(K\otimes\ell^2(I)\) is the algebra \(\mathbb M_I(N')\) of operators whose matrix entries lie in \(N'\), and its centre is \((N\cap N')\otimes1\). The algebra \(\mathbb M_I(N)\), also written \(N\bar\otimes B(\ell^2(I))\), is the von Neumann algebra generated by \(N\otimes1\) and \(1\otimes B(\ell^2(I))\). If \(\{e_i\}_{i\in I}\) are mutually orthogonal, mutually equivalent projections of \(M\) with sum \(1\), there is a unitary \(W:e_{i_0}H\otimes\ell^2(I)\to H\) with \(W^*x'W=x'e_{i_0}|_{e_{i_0}H}\otimes1\) for every \(x'\in M'\).
8. (*Families of equivalent projections*, Proposition 13.1.) Let \(\{e_i\}_{i\in I}\) be mutually orthogonal, mutually equivalent, nonzero projections. There are a nonzero central projection \(z\) and mutually orthogonal, mutually equivalent projections \(\{f_j\}_{j\in J}\), \(J\supseteq I\), with \(f_i=ze_i\) for \(i\in I\) and \(z-\sum_jf_j\prec f_j\) for all \(j\). If \(J\) is infinite, the \(f_j\) can be replaced by mutually orthogonal projections \(f_j\sim ze_{i}\) (any fixed \(i\in I\)) with \(\sum_{j\in J}f_j=z\).
9. (*Division by \(\aleph_0\)*, Corollary 13.5.) A properly infinite projection \(e\) is \(\sum_{n\ge1}e_n\) with mutually orthogonal \(e_n\sim e\).
10. (*Finite projections*, Theorem 14.1.) If \(e\) and \(f\) are finite, so is \(e\vee f\).
11. (*Absorption*, Proposition 15.2.) Let \(e\) be properly infinite. If \(f_1,f_2,\ldots\) are mutually orthogonal with \(f_n\precsim e\), then \(\sum_nf_n\precsim e\). If \(f\) is locally \(\sigma\)-finite (in particular \(\sigma\)-finite) and \(c(f)\le c(e)\), then \(f\precsim e\). Here \(f\) is *locally \(\sigma\)-finite* if every central \(z\) with \(zf\ne0\) majorizes a central \(z'\) with \(z'f\) nonzero and \(\sigma\)-finite; \(M\) is locally \(\sigma\)-finite if \(1\) is (Definition 15.1).

**Fact 2.3** (The cyclic support used here). For a vector \(\xi\), \(p_\xi\) is the least projection of \(M\) fixing \(\xi\), and is the support of \(\omega_\xi|_M\). This is Lemma 4.6 of [Projections and types](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html).

**Fact 2.4** (Normal functionals and \(\sigma\)-finiteness).

1. A set \(S\subseteq H\) is *cyclic* for \(M\) if \([MS]=H\), and *separating* for \(M\) if \(x\in M\) and \(xS=\{0\}\) imply \(x=0\). A set, in particular a single vector, is cyclic for \(M\) exactly when it is separating for \(M'\). \(M\) is \(\sigma\)-finite if and only if \(H\) contains a countable set that is separating for \(M\), and if and only if \(M\) has a faithful normal state [The double commutant theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-12).
2. Every \(\varphi\in M_*^+\) equals \(\sum_n\omega_{\xi_n}\) with \(\sum_n\|\xi_n\|^2<\infty\) [The double commutant theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-14).
3. Every \(\varphi\in M_*^+\) has a support \(s(\varphi)\), the least projection \(p\) with \(\varphi(1-p)=0\), and \(\{x\in M:\varphi(x^*x)=0\}=M(1-s(\varphi))\). An isomorphism of von Neumann algebras and its inverse are normal. If \(\pi\) is a normal representation of \(M\), then \(\ker\pi=M(1-z)\) for a central projection \(z\), the image \(\pi(M)\) is a von Neumann algebra, and \(\pi\) maps \(Mz\) isomorphically onto \(\pi(M)\). These are Lemma 11.1, Corollary 11.4 and Proposition 12.1 of [The universal enveloping von Neumann algebra of a \(C^*\)-algebra, and \(W^*\)-algebras](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-24).
4. (*Density and topologies.*) A \(*\)-algebra of operators acting nondegenerately is \(\sigma\)-weakly dense in its bicommutant, and on bounded sets strong convergence implies \(\sigma\)-weak convergence [The double commutant theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-06).
5. (*Cyclic representations.*) For every positive linear functional \(\varphi\) on a \(C^*\)-algebra \(A\) there are a representation \(\pi_\varphi\) of \(A\) on a Hilbert space \(H_\varphi\) and a vector \(\xi_\varphi\) such that \(\varphi(a)=\langle\pi_\varphi(a)\xi_\varphi,\xi_\varphi\rangle\) and \(\pi_\varphi(A)\xi_\varphi\) is dense in \(H_\varphi\) [Blackadar, II.6.4]. If \(A\) has a unit, \(\xi_\varphi=\pi_\varphi(1)\xi_\varphi\); in general \(\xi_\varphi\) is the limit of \(\pi_\varphi(u_i)\xi_\varphi\) along an approximate unit \((u_i)\) of positive contractions.
6. (*Normal maps.*) A positive linear functional on \(M\) is \(\sigma\)-weakly continuous exactly when it preserves suprema of bounded increasing nets, and \(M_*\) is spanned by \(M_*^+\) [Blackadar, III.2.1.3–III.2.1.4]. Consequently a positive linear map \(T:M\to N\) between von Neumann algebras that preserves suprema of bounded increasing nets is normal, because \(\psi\circ T\) is normal for every \(\psi\in N_*^+\); and a linear bijection that preserves order and suprema in both directions is a homeomorphism for the \(\sigma\)-weak topologies.

**Fact 2.7** (Normal homomorphisms). For a von Neumann algebra \(N\subseteq B(L)\) and a normal unital \(*\)-homomorphism \(\pi:N\to B(H)\), there are a Hilbert space \(R\) and an isometry \(V:H\to L\otimes R\) such that \(VV^*\) commutes with \(N\otimes1_R\) and \(\pi(y)=V^*(y\otimes1_R)V\) for \(y\in N\). This is Theorem 8.2 of [Spatial tensor products of von Neumann algebras](../reader/supplements/spatial-tensor-products.html#8-maps-between-tensor-products-and-normal-homomorphisms).

**Fact 2.10** (Set theory). Zorn's lemma; \(\kappa\cdot\aleph_0=\kappa\) for infinite cardinals \(\kappa\); the Cantor–Bernstein theorem, as in [Projections and types of von Neumann algebras](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html) (Fact 2.9 there).

## 3. Comparing representations inside one commutant

Let \(\pi_1\) and \(\pi_2\) be normal representations of \(M\) on \(K_1\) and \(K_2\). Put \(K=K_1\oplus K_2\), \(\rho(x)=\pi_1(x)\oplus\pi_2(x)\), \(P=\rho(M)\), and let \(q_i\) be the projection of \(K\) onto \(K_i\). We call \(P\) the *joint algebra* of \(\pi_1\) and \(\pi_2\). The next lemma turns every question about the two representations into a question about \(q_1\) and \(q_2\).

**Lemma 3.1** (Two representations in one commutant).

1. \(P\) is a von Neumann algebra on \(K\), and \(q_1,q_2\) are projections of \(P'\) with \(q_1+q_2=1\).
2. An operator \(t\) on \(K\) lies in \(P'\) if and only if its matrix entries \(t_{ij}=q_itq_j|_{K_j}:K_j\to K_i\) satisfy \(t_{ij}\pi_j(x)=\pi_i(x)t_{ij}\) for all \(x\in M\). In particular the reduced algebra \(q_iP'q_i\), on \(K_i\), is \(\pi_i(M)'\), and the induced algebra \(P_{q_i}\) is \(\pi_i(M)\).
3. \(\pi_1\simeq\pi_2\) if and only if \(q_1\sim q_2\) in \(P'\). And \(\pi_1\) is unitarily equivalent to a subrepresentation of \(\pi_2\) if and only if \(q_1\precsim q_2\) in \(P'\).
4. Let \(c(q_i)\) be the central support of \(q_i\) in \(P'\). Then \(\ker\pi_i=\{x\in M:\rho(x)\in P(1-c(q_i))\}\). Hence \(\ker\pi_1=\ker\pi_2\) if and only if \(c(q_1)=c(q_2)\), and \(c(q_i)=1\) when \(\pi_i\) is faithful.

**Proof.** (1) \(\rho\) is a normal representation, so \(P\) is a von Neumann algebra (Fact 2.4(3)). Each \(\rho(x)\) maps \(K_1\) into \(K_1\) and \(K_2\) into \(K_2\), so it commutes with \(q_1\) and \(q_2\).

(2) Write \(t\) as a \(2\times2\) matrix of operators \(t_{ij}\). The entries of \(t\rho(x)\) are \(t_{ij}\pi_j(x)\), and those of \(\rho(x)t\) are \(\pi_i(x)t_{ij}\). They agree for all \(x\) exactly when every entry intertwines. The operators \(q_itq_i\), \(t\in P'\), are the operators with a single entry \(t_{ii}\in\pi_i(M)'\), so \(q_iP'q_i\) is \(\pi_i(M)'\) on \(K_i\). Finally \(\rho(x)q_i\) restricted to \(K_i\) is \(\pi_i(x)\).

(3) Let \(U:K_1\to K_2\) be a unitary with \(U\pi_1(x)=\pi_2(x)U\), and let \(t\) be the operator whose only nonzero entry is \(t_{21}=U\). By (2), \(t\in P'\), and \(t^*t=q_1\), \(tt^*=q_2\). Conversely, let \(t\in P'\) with \(t^*t=q_1\) and \(tt^*=q_2\). Then \(t=q_2tq_1\), so its only nonzero entry is \(t_{21}\), which maps \(K_1\) isometrically onto \(K_2\) and intertwines \(\pi_1\) with \(\pi_2\) by (2). For the second statement, let \(t\in P'\) with \(t^*t=q_1\) and \(tt^*\le q_2\). Then \(t_{21}\) is an isometry of \(K_1\) onto \(L=tt^*K\subseteq K_2\). This subspace is invariant under \(\pi_2(M)\), because \(tt^*\in P'\), and \(t_{21}\) intertwines \(\pi_1\) with the subrepresentation of \(\pi_2\) on \(L\). Conversely, if an isometry \(V:K_1\to K_2\) intertwines \(\pi_1\) with the subrepresentation on an invariant subspace \(L\), then the projection \(VV^*\) onto \(L\) commutes with \(\pi_2(M)\), because an invariant subspace of a self-adjoint set of operators reduces it. The operator \(t\) with the single entry \(t_{21}=V\) lies in \(P'\), and \(t^*t=q_1\), \(tt^*=VV^*\le q_2\).

(4) The map \(y\mapsto yq_i|_{K_i}\) is the induction of \(P\) by \(q_i\in P'\). By Fact 2.1(3) its kernel is \(P(1-c(q_i))\), and by (2) it sends \(\rho(x)\) to \(\pi_i(x)\). This gives the formula for \(\ker\pi_i\). As \(\rho\) maps \(M\) onto \(P\), \(\ker\pi_1=\ker\pi_2\) exactly when \(P(1-c(q_1))=P(1-c(q_2))\). For central projections \(w_1,w_2\), \(Pw_1=Pw_2\) forces \(w_1=w_1w_2=w_2\), because \(w_1\in Pw_2\) and \(w_2\in Pw_1\). If \(\pi_i\) is faithful, then \(P(1-c(q_i))=\rho(\ker\pi_i)=\{0\}\), so \(c(q_i)=1\). \(\square\)

The centre of \(P'\) equals the centre of \(P\), which is \(\rho(Z)\): by Fact 2.4(3), \(\rho\) maps a central summand \(Mz\) of \(M\) isomorphically onto \(P\), so the centre of \(P\) is \(\rho(Zz)=\rho(Z)\). So the central supports in (4) are images of central projections of \(M\).

**Remark 3.2** (One commutant for all representations). Let \(\pi\) be a faithful normal representation of \(M\) on \(L\), and \(\sigma\) any normal representation on \(K\). Fact 2.7, applied to the von Neumann algebra \(\pi(M)\) and the normal homomorphism \(\pi(x)\mapsto\sigma(x)\) (normal because \(\pi^{-1}\) is, Fact 2.4(3)), gives an isometry \(V:K\to L\otimes R\) with \(V\sigma(x)=(\pi(x)\otimes1)V\). So \(\sigma\) is equivalent to the subrepresentation of the amplification \(x\mapsto\pi(x)\otimes1_R\) on the invariant subspace \(VK\). Thus the normal representations of \(M\) correspond to projections in the commutants of the amplifications of one faithful representation.

**Lemma 3.3** (Cyclic projections). Let \(\xi\in H\).

1. For a central projection \(z\), \(p_{z\xi}=zp_\xi\) and \(p'_{z\xi}=zp'_\xi\).
2. If \(v\in M\) is a partial isometry with \(v^*v\ge p_\xi\), then \(p_{v\xi}=vp_\xi v^*\) and \(p'_{v\xi}=p'_\xi\). Consequently a projection of \(M\) that is equivalent to a cyclic projection is cyclic.
3. If \(g\in\mathcal P(M)\) and \(g\le p_\xi\), then \(g=p_{g\xi}\). So a subprojection of a cyclic projection is cyclic.
4. Every \(e\in\mathcal P(M)\) is the sum of mutually orthogonal cyclic projections \(p_{\xi_i}\) with \(\xi_i\in eH\).
5. Every cyclic projection is \(\sigma\)-finite.
6. For \(e\in\mathcal P(M)\) and \(e'\in\mathcal P(M')\), \(ee'=0\) if and only if \(c(e)c(e')=0\).

The same holds with \(M\) and \(M'\) exchanged.

**Proof.** (1) \(z\) commutes with \(M'\), so \([M'z\xi]=z[M'\xi]\). The same argument works for \(M\).

(2) Since \(v\in M\) commutes with \(M'\), \(M'v\xi=vM'\xi\). The operator \(v\) is isometric on \(v^*vH\supseteq p_\xi H\), so it maps the closed subspace \(p_\xi H=[M'\xi]\) isometrically onto a closed subspace, which is the closure of \(vM'\xi\). Hence \(p_{v\xi}\) is the projection onto \(vp_\xi H\), namely \(vp_\xi v^*\). Next, \([Mv\xi]\subseteq[M\xi]\), and \(\xi=v^*v\xi\in Mv\xi\), so \([Mv\xi]=[M\xi]\). If \(v^*v=p_\xi\) and \(vv^*=g\), this gives \(g=p_{v\xi}\).

(3) \(gM'\xi=M'g\xi\), and \(g\) maps the dense subset \(M'\xi\) of \(p_\xi H\) onto a dense subset of \(gp_\xi H=gH\). So \([M'g\xi]=gH\).

(4) By Zorn's lemma, choose nonzero vectors \(\xi_i\in eH\) with mutually orthogonal cyclic projections, the family being maximal for this property. By Fact 2.3(1), \(p_{\xi_i}\le e\). If \(r=e-\sum_ip_{\xi_i}\) were nonzero, a nonzero \(\eta\in rH\) would have \(p_\eta\le r\), and could be added to the family.

(5) By Fact 2.1(1), the commutant of \(p_\xi Mp_\xi\) on \(p_\xi H\) is \(M'p_\xi\), for which \(\xi\) is cyclic. So \(\xi\) is separating for \(p_\xi Mp_\xi\) (Fact 2.4(1)), which is therefore \(\sigma\)-finite.

(6) If \(ee'=0\), then \(e'\) lies in the kernel of the induction \(x'\mapsto x'e|_{eH}\) of \(M'\), which is \(M'(1-c(e))\) (Fact 2.1(3)). So \(e'c(e)=0\), and the central projection \(1-c(e)\) majorizes \(e'\); hence \(c(e')\le1-c(e)\). Conversely, \(c(e)c(e')=0\) gives \(ee'=ec(e)c(e')e'=0\). \(\square\)

**Lemma 3.4** (Properly infinite commutants). If \(M'\) is properly infinite, every positive normal functional on \(M\) is a vector functional \(\omega_\zeta|_M\).

**Proof.** By division by \(\aleph_0\) (Fact 2.2(9)) in \(M'\), \(1=\sum_{n\ge1}e'_n\) with mutually orthogonal projections \(e'_n\in M'\), each equivalent to \(1\). By Fact 2.2(7), applied to the algebra \(M'\), whose commutant is \(M\), there is a unitary \(W:e'_1H\otimes\ell^2(\mathbb N)\to H\) with \(W^*xW=x_{e'_1}\otimes1\) for \(x\in M\). The induction \(x\mapsto x_{e'_1}\) is injective, because its kernel is \(M(1-c(e'_1))\) and \(c(e'_1)=c(1)=1\) (Fact 2.1). Let \(\varphi\in M_*^+\). The functional \(x_{e'_1}\mapsto\varphi(x)\) is positive and normal on \(M_{e'_1}\) (Fact 2.4(3)), so it equals \(\sum_n\omega_{\xi_n}\) with \(\xi_n\in e'_1H\) and \(\sum_n\|\xi_n\|^2<\infty\) (Fact 2.4(2)). Put \(\zeta=W(\sum_n\xi_n\otimes\delta_n)\). Then
\[
\omega_\zeta(x)=\Bigl\langle(x_{e'_1}\otimes1)\sum_n\xi_n\otimes\delta_n,\sum_m\xi_m\otimes\delta_m\Bigr\rangle=\sum_n\langle x_{e'_1}\xi_n,\xi_n\rangle=\varphi(x).\qquad\square
\]

**Example 3.5** (Matrix algebras). Every normal representation of \(M_n(\mathbb C)\) is unitarily equivalent to \(x\mapsto x\otimes1_m\) on \(\mathbb C^n\otimes\mathbb C^m\) for one cardinal \(m\): the images of the matrix units are mutually equivalent projections with sum \(1\), and Fact 2.2(7) splits the space. For two such representations, with \(m_1\) and \(m_2\) copies, the joint algebra is \(M_n(\mathbb C)\otimes1\) on \(\mathbb C^n\otimes(\mathbb C^{m_1}\oplus\mathbb C^{m_2})\). Its commutant is \(1\otimes B(\mathbb C^{m_1}\oplus\mathbb C^{m_2})\), and \(q_1,q_2\) are projections of rank \(m_1\) and \(m_2\) there. They are equivalent exactly when \(m_1=m_2\). This recovers the multiplicity \(m\) of the introduction.

## 4. Representations with properly infinite commutant

If the commutants are properly infinite and not too large, there is no room for multiplicity at all: only the kernel matters.

**Theorem 4.1.** Let \(\pi_1\) and \(\pi_2\) be normal representations of \(M\) whose commutants \(\pi_1(M)'\) and \(\pi_2(M)'\) are properly infinite and locally \(\sigma\)-finite (for example, \(\sigma\)-finite). Then \(\pi_1\simeq\pi_2\) if and only if \(\ker\pi_1=\ker\pi_2\). In particular, two faithful normal representations with \(\sigma\)-finite, properly infinite commutants are unitarily equivalent.

**Proof.** Equivalent representations have the same kernel. Conversely, let \(\ker\pi_1=\ker\pi_2\), and use the joint algebra \(P\) of Lemma 3.1. By Lemma 3.1(2), the reduced algebra \(q_iP'q_i\) is \(\pi_i(M)'\). Its central projections are the \(wq_i\) with \(w\) central in \(P'\) (Fact 2.1(4)), and the reduced algebra of \(q_iP'q_i\) by \(wq_i\) is \((wq_i)P'(wq_i)\). So the hypotheses say that \(q_i\) is a properly infinite and locally \(\sigma\)-finite projection of \(P'\). By Lemma 3.1(4), \(c(q_1)=c(q_2)\). The absorption property (Fact 2.2(11)) gives \(q_1\precsim q_2\) and \(q_2\precsim q_1\), so \(q_1\sim q_2\) by Schröder–Bernstein, and \(\pi_1\simeq\pi_2\) by Lemma 3.1(3). \(\square\)

**Example 4.2** (Both conditions are needed). Let \(M=\mathbb C1\). A normal representation is the scalar action on a Hilbert space \(K\), it is faithful if \(K\ne0\), and its commutant is \(B(K)\).

- \(K_1=\mathbb C\) and \(K_2=\mathbb C^2\) give faithful representations with \(\sigma\)-finite commutants that are not equivalent. The commutants \(\mathbb C\) and \(M_2(\mathbb C)\) are not properly infinite.
- \(K_1=\ell^2(\mathbb N)\) and \(K_2=\ell^2(\Gamma)\) with \(|\Gamma|=\aleph_1\) give properly infinite commutants and faithful representations that are not equivalent, since the dimensions differ. The factor \(B(\ell^2(\Gamma))\) is not \(\sigma\)-finite (the rank-one projections of the basis form an uncountable orthogonal family), and a factor is locally \(\sigma\)-finite only if it is \(\sigma\)-finite.

**Theorem 4.3.** Let \(Z\) be the centre of \(M\).

1. \(M\) has a faithful normal representation with \(\sigma\)-finite commutant if and only if \(Z\) is \(\sigma\)-finite.
2. If \(Z\) is \(\sigma\)-finite, \(M\) has a faithful normal representation whose commutant is \(\sigma\)-finite and properly infinite, and any two such representations are unitarily equivalent.

**Proof.** (1) Let \(\pi\) be faithful and normal with \(\pi(M)'\) \(\sigma\)-finite. The centre \(\pi(Z)\) of \(\pi(M)'\) is \(\sigma\)-finite, because an orthogonal family of central projections is an orthogonal family in \(\pi(M)'\); and \(Z\cong\pi(Z)\).

Conversely, let \(Z\) be \(\sigma\)-finite. By Zorn's lemma choose normal states \(\varphi_i\) of \(M\) whose supports have mutually orthogonal central supports \(z_i=c(s(\varphi_i))\), the family \(\{\varphi_i\}\) being maximal for this property. The \(z_i\) are nonzero, mutually orthogonal central projections, so there are countably many; index them by \(i=1,2,\ldots\). If \(w=1-\sum_iz_i\) were nonzero, a unit vector \(\xi\in wH\) would give the normal state \(\omega_\xi|_M\) with support \(p_\xi\le w\) (Fact 2.3(1)), and hence \(c(p_\xi)\le w\), against maximality. So \(\sum_iz_i=1\). Put \(\varphi=\sum_i2^{-i}\varphi_i\), divided by \(\varphi(1)\). This is a normal state, and \(\varphi(1-q)=0\) exactly when \(\varphi_i(1-q)=0\) for all \(i\); so \(s(\varphi)=\bigvee_is(\varphi_i)\), and \(c(s(\varphi))=\bigvee_iz_i=1\).

Let \((\pi_\varphi,H_\varphi,\xi_\varphi)\) be the cyclic representation of \(\varphi\) (Fact 2.4(5)). It is normal. Let \(x_j\uparrow x\) be a bounded increasing net in \(M_+\), and let \(S\) be the supremum of the bounded increasing net \(\pi_\varphi(x_j)\). For \(\eta=\pi_\varphi(y)\xi_\varphi\), normality of \(\varphi\) gives \(\langle S\eta,\eta\rangle=\lim_j\varphi(y^*x_jy)=\varphi(y^*xy)=\langle\pi_\varphi(x)\eta,\eta\rangle\). These vectors form a dense subspace, so polarization and continuity give \(S=\pi_\varphi(x)\). Thus \(\pi_\varphi\) preserves suprema, and it is normal (Fact 2.4(6)). It is faithful: \(\pi_\varphi(x)=0\) means \(\varphi(y^*x^*xy)=0\) for all \(y\in M\), that is, \(xys(\varphi)=0\) for all \(y\) (Fact 2.4(3)); so \(x\) vanishes on \([Ms(\varphi)H]=c(s(\varphi))H=H\) (Fact 2.1(2)). Finally \(\xi_\varphi\) is cyclic for \(\pi_\varphi(M)\), hence separating for \(\pi_\varphi(M)'\), which is therefore \(\sigma\)-finite (Fact 2.4(1)).

(2) Let \(\pi_\varphi\) be as above and \(\sigma(x)=\pi_\varphi(x)\otimes1\) on \(H_\varphi\otimes\ell^2(\mathbb N)\). It is faithful and normal. By Fact 2.2(7), \(\sigma(M)'=\mathbb M_{\mathbb N}(\pi_\varphi(M)')\), with centre \(\{w\otimes1\}\). For a nonzero central projection \(w\otimes1\), the operator \(w\otimes s\), where \(s\) is the unilateral shift, lies in \(\sigma(M)'\); it has initial projection \(w\otimes1\) and final projection \(w\otimes(1-e_0)\), where \(e_0\) projects onto \(\mathbb C\delta_0\). So every nonzero central projection is infinite, and \(\sigma(M)'\) is properly infinite. The countable set \(\{\xi_\varphi\otimes\delta_n\}\) is cyclic for \(\sigma(M)\), hence separating for \(\sigma(M)'\), which is therefore \(\sigma\)-finite (Fact 2.4(1)). Uniqueness is Theorem 4.1. \(\square\)

The next lemma counts orthogonal projections without assuming that the whole algebra is \(\sigma\)-finite.

**Lemma 4.5** (Counting orthogonal projections). Let \(\{e_j\}_{j\in J}\) be mutually orthogonal \(\sigma\)-finite projections of \(M\) with \(\sum_je_j=1\). If \(\{f_i\}_{i\in I}\) are mutually orthogonal *nonzero* projections of \(M\), then \(|I|\le\aleph_0\cdot|J|\). If \(J\) is infinite, then \(|I|\le|J|\).

*Reference:* [Takesaki I, Lemma V.3.17] states the bound for every orthogonal family of projections; this fails because the zero projection may be repeated any number of times, so we require the \(f_i\) to be nonzero.

**Proof.** For each \(j\), the algebra \(e_jMe_j\) is \(\sigma\)-finite, so it has a faithful normal state \(\psi_j\) (Fact 2.4(1)); put \(\varphi_j(x)=\psi_j(e_jxe_j)\). Let \(I_j=\{i:\varphi_j(f_i)>0\}\). For a finite \(F\subseteq I\), \(\sum_{i\in F}\varphi_j(f_i)=\varphi_j(\sum_{i\in F}f_i)\le1\), so \(I_j\) is countable. Fix \(i\). Since \(f_i\ne0\) and \(f_i=\sum_jf_ie_j\) strongly, some \(f_ie_j\ne0\). Then \(e_jf_ie_j=(f_ie_j)^*(f_ie_j)\ne0\), and \(\varphi_j(f_i)=\psi_j(e_jf_ie_j)>0\) by faithfulness. So \(I=\bigcup_jI_j\), and \(|I|\le\aleph_0\cdot|J|\). If \(J\) is infinite, \(\aleph_0\cdot|J|=|J|\) (Fact 2.10). \(\square\)

