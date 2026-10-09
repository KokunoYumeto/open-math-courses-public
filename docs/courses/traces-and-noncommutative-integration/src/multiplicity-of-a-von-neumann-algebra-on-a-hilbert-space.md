# Multiplicity of a von Neumann algebra on a Hilbert space

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision of the references is self-checked by the writing AI. Proposition 2.11 was drafted by GPT-6 Astra (OpenAI) in ChatGPT web, Pro mode, and checked and adapted by Claude Opus 5.5, October 2026. Public domain (CC0).*

A von Neumann algebra can act on many Hilbert spaces. The matrix algebra \(M_n(\mathbb C)\) acts on \(\mathbb C^n\otimes\mathbb C^m\) for every \(m\ge1\), by \(a\mapsto a\otimes1\), and the number \(m\), the number of copies of \(\mathbb C^n\), is the only invariant of the action. This lesson finds the invariants that play the part of \(m\) for an arbitrary von Neumann algebra \(M\). The basic observation is simple. Two normal representations of \(M\) can be placed side by side on one Hilbert space. Then they are unitarily equivalent exactly when two projections of the common commutant are equivalent. So the comparison theory of projections, applied to commutants, answers questions about representations. We use the word *multiplicity* for the size of a representation, measured in this way.

The lesson answers four questions.

1. *When are two faithful normal representations unitarily equivalent?* If their commutants are \(\sigma\)-finite and properly infinite, they always are. So an algebra with \(\sigma\)-finite centre has exactly one faithful normal representation with \(\sigma\)-finite, properly infinite commutant. For an algebra of type III this is the only faithful normal representation with \(\sigma\)-finite commutant (Sections 4 and 9).
2. *When is there a cyclic or a separating vector?* If \(M\) or \(M'\) is \(\sigma\)-finite, the Hilbert space splits along the centre into a part with a cyclic vector and a part with a separating vector (Section 5). For a finite algebra with finite commutant and \(\sigma\)-finite centre the answer is numerical: a cyclic vector exists exactly when the coupling function is at most \(1\) (Theorem 10.8).
3. *What does a symmetry between \(M\) and \(M'\) give?* A *unitary involution* is an antiunitary \(J\) with \(J^2=1\) and \(JMJ=M'\) that acts on the centre as the adjoint: \(JaJ=a^*\) for central \(a\). If \(M\) has one, every normal state of \(M\) is a vector state, and every isomorphism onto another algebra with a unitary involution is implemented by a unitary (Section 7). The Hilbert space of a trace, \(L^2(M,\tau)\), is the model.
4. *How large is a representation?* Every normal trace on \(M\) has exactly one partner on \(M'\) that takes the same value on each pair of cyclic projections \([M'\xi]\) and \([M\xi]\) (Theorem 9.3). For centre-valued traces this gives the *coupling function* \(c(M,H)\), a central function with values in \((0,\infty)\) outside a nowhere dense set. For finite algebras with finite commutant it determines the representation up to unitary equivalence (Section 10).

Section 6 studies limits of cyclic projections, and Section 11 studies tracial states and the representations they produce.

The lesson assumes the comparison theory of projections and the type decomposition, from Projections and types of von Neumann algebras; traces and the centre-valued trace of a finite algebra, from Traces on von Neumann algebras; the Hilbert space \(L^2(M,\tau)\) of a trace and its commutation theorem, from the lesson *Measurable operators for a trace: examples, convergence and the commutant*; the structure of normal homomorphisms, from Spatial tensor products of von Neumann algebras; and the basic facts on von Neumann algebras from The double commutant theorem and [The universal enveloping von Neumann algebra of a \(C^*\)-algebra, and \(W^*\)-algebras](../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html). Section 2 states in full every result used from other lessons, with the place where it is proved.

Murray and von Neumann introduced the coupling constant of a finite factor with finite commutant. For algebras with a non-trivial centre the constant becomes a central operator [Griffin 1953]. The standard form of a von Neumann algebra, whose conjugation is a unitary involution in the sense of this lesson, is due to Haagerup [Haagerup 1975]. Basic references are [Kostecki] and [Blackadar].

## 1. Conventions

\(H\) is a complex Hilbert space, and inner products \(\langle\cdot,\cdot\rangle\) are linear in the first variable. \(M\subseteq B(H)\) is a von Neumann algebra, \(M'\) its commutant, and \(Z=M\cap M'\) its centre. For \(S\subseteq B(H)\) and \(X\subseteq H\), \([SX]\) is the closed linear span of the vectors \(x\xi\) with \(x\in S\), \(\xi\in X\), and we identify a closed subspace with the projection onto it. We write \(\omega_\xi(x)=\langle x\xi,\xi\rangle\) and \(\omega_{\eta,\xi}(x)=\langle x\eta,\xi\rangle\). \(M_*\) is the space of normal (\(\sigma\)-weakly continuous) linear functionals on \(M\), and \(M_*^+\) its positive part.

*Projections.* \(\mathcal P(M)\) is the set of projections of \(M\). Equivalence \(e\sim f\), subequivalence \(e\precsim f\), finite, infinite and properly infinite projections, and the central support \(c(e)\) (the least central projection majorizing \(e\)) are as in Projections and types of von Neumann algebras. \(M\) is *\(\sigma\)-finite* if every family of mutually orthogonal nonzero projections in \(M\) is countable, and a projection \(e\) is \(\sigma\)-finite if \(eMe\) is.

*Cyclic projections.* For \(\xi\in H\), \(p_\xi\in M\) is the projection onto \([M'\xi]\) and \(p'_\xi\in M'\) the projection onto \([M\xi]\). We call the projections of the form \(p_\xi\) the *cyclic projections* of \(M\), and those of the form \(p'_\xi\) the cyclic projections of \(M'\). A vector \(\xi\) is *cyclic* for \(M\) if \(p'_\xi=1\), and *separating* for \(M\) if \(x\in M\), \(x\xi=0\) imply \(x=0\).

*Reduced and induced algebras.* For \(e\in\mathcal P(M)\), the *reduced algebra* is \(M_e=eMe\), acting on \(eH\). For \(e'\in\mathcal P(M')\), the *induced algebra* is \(M_{e'}=\{x_{e'}:x\in M\}\), acting on \(e'H\), where \(x_{e'}=xe'|_{e'H}\); the map \(x\mapsto x_{e'}\) is the *induction*. If \(e\in\mathcal P(M)\) and \(e'\in\mathcal P(M')\), then \(ee'\) is a projection, and \(M_{ee'}\) denotes the algebra of the restrictions \(x|_{ee'H}\), \(x\in eMe\), acting on \(ee'H\).

*Representations.* A *normal representation* of \(M\) on a Hilbert space \(K\) is a unital \(*\)-homomorphism \(\pi:M\to B(K)\) that is \(\sigma\)-weakly continuous. Two representations \(\pi_1,\pi_2\) on \(K_1,K_2\) are *unitarily equivalent*, \(\pi_1\simeq\pi_2\), if some unitary \(U:K_1\to K_2\) satisfies \(U\pi_1(x)=\pi_2(x)U\) for all \(x\). A *subrepresentation* is the restriction of a representation to a closed invariant subspace. The notation \(\{M,H\}\cong\{N,K\}\) means that some unitary \(W:H\to K\) satisfies \(WMW^*=N\). An isomorphism \(\pi:M\to N\) of von Neumann algebras is *spatial* if \(\pi(x)=WxW^*\) for such a \(W\).

*Traces.* A *trace* on \(M\) is a map \(\tau:M_+\to[0,\infty]\) that is additive, positively homogeneous (with \(0\cdot\infty=0\)) and satisfies \(\tau(x^*x)=\tau(xx^*)\). It is *normal*, *faithful*, *finite* or *semifinite* as in Traces on von Neumann algebras. For \(a\in Z_+\) we write \(\tau_a(x)=\tau(ax)=\tau(a^{1/2}xa^{1/2})\) (\(x\in M_+\)); this is again a trace, normal if \(\tau\) is.

## 2. Results used from other lessons

The following results are proved in the lessons named, except Proposition 2.11, which is proved at the end of the section.

**Fact 2.1** (Reduced and induced algebras, central supports). Let \(e\in\mathcal P(M)\) and \(e'\in\mathcal P(M')\).

1. \(eMe\) and \(M'e\) (restricted to \(eH\)) are von Neumann algebras on \(eH\) and each is the commutant of the other. Likewise \(M_{e'}\) and \(e'M'e'\) are mutual commutants on \(e'H\).
2. \(c(e)\) is the projection onto \([MeH]\). For a central projection \(z\), \(ze=0\) if and only if \(zc(e)=0\), and \(c(ze)=zc(e)\). Equivalent projections have the same central support.
3. The induction \(x\mapsto x_{e'}\) is a \(*\)-homomorphism of \(M\) onto \(M_{e'}\) with kernel \(M(1-c(e'))\), where \(c(e')\) is the central support of \(e'\) in \(M'\). Likewise \(x'\mapsto x'e|_{eH}\) maps \(M'\) onto \(M'e\) with kernel \(M'(1-c(e))\).
4. The centre of \(eMe\) is \(Ze\), and \(a\mapsto ae\) is an isomorphism of \(Zc(e)\) onto it.

These are proved in Projections and types of von Neumann algebras (Proposition 3.5) and The double commutant theorem.

**Fact 2.2** (Comparison of projections). The following are proved in Projections and types of von Neumann algebras.

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

**Fact 2.3** (Cyclic projections of \(M\) and \(M'\)). The following are proved in Projections and types of von Neumann algebras.

1. (Lemma 4.6.) \(p_\xi\) is the least projection \(p\in M\) with \(p\xi=\xi\), and it is the support of \(\omega_\xi|_M\).
2. (*Transfer theorem*, Theorem 17.5.) \(p_\xi\succsim p_\eta\) in \(M\) if and only if \(p'_\xi\succsim p'_\eta\) in \(M'\).
3. (Proposition 18.2.) If \(M\) has a separating vector, every positive normal functional on \(M\) is a vector functional \(\omega_\xi|_M\).
4. (Proposition 18.5.) If some vector is cyclic for \(M\) and some vector is separating for \(M\), then one vector is both.
5. (Proposition 18.6.) An isomorphism between two von Neumann algebras that both have a cyclic and separating vector is spatial.
6. (Corollary 11.3.) If \(M\) is of type I, so is \(M'\).

**Fact 2.4** (Normal functionals and \(\sigma\)-finiteness).

1. A set \(S\subseteq H\) is *cyclic* for \(M\) if \([MS]=H\), and *separating* for \(M\) if \(x\in M\) and \(xS=\{0\}\) imply \(x=0\). A set, in particular a single vector, is cyclic for \(M\) exactly when it is separating for \(M'\). \(M\) is \(\sigma\)-finite if and only if \(H\) contains a countable set that is separating for \(M\), and if and only if \(M\) has a faithful normal state The double commutant theorem.
2. Every \(\varphi\in M_*^+\) equals \(\sum_n\omega_{\xi_n}\) with \(\sum_n\|\xi_n\|^2<\infty\) The double commutant theorem.
3. Every \(\varphi\in M_*^+\) has a support \(s(\varphi)\), the least projection \(p\) with \(\varphi(1-p)=0\), and \(\{x\in M:\varphi(x^*x)=0\}=M(1-s(\varphi))\). An isomorphism of von Neumann algebras and its inverse are normal. If \(\pi\) is a normal representation of \(M\), then \(\ker\pi=M(1-z)\) for a central projection \(z\), the image \(\pi(M)\) is a von Neumann algebra, and \(\pi\) maps \(Mz\) isomorphically onto \(\pi(M)\). These are Lemma 11.1, Corollary 11.4 and Proposition 12.1 of [The universal enveloping von Neumann algebra of a \(C^*\)-algebra, and \(W^*\)-algebras](../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-24).
4. (*Density and topologies.*) A \(*\)-algebra of operators acting nondegenerately is \(\sigma\)-weakly dense in its bicommutant, and on bounded sets strong convergence implies \(\sigma\)-weak convergence The double commutant theorem.
5. (*Cyclic representations.*) For every positive linear functional \(\varphi\) on a \(C^*\)-algebra \(A\) there are a representation \(\pi_\varphi\) of \(A\) on a Hilbert space \(H_\varphi\) and a vector \(\xi_\varphi\) such that \(\varphi(a)=\langle\pi_\varphi(a)\xi_\varphi,\xi_\varphi\rangle\) and \(\pi_\varphi(A)\xi_\varphi\) is dense in \(H_\varphi\) (Representations and positive functionals, Sections 5 and 6). If \(A\) has a unit, \(\xi_\varphi=\pi_\varphi(1)\xi_\varphi\); in general \(\xi_\varphi\) is the limit of \(\pi_\varphi(u_i)\xi_\varphi\) along an approximate unit \((u_i)\) of positive contractions.
6. (*Normal maps.*) A positive linear functional on \(M\) is \(\sigma\)-weakly continuous exactly when it preserves suprema of bounded increasing nets, and \(M_*\) is spanned by \(M_*^+\) (Normal positive maps and their preadjoints, §§NP-02 and NP-04, and The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras, Section 10). Consequently a positive linear map \(T:M\to N\) between von Neumann algebras that preserves suprema of bounded increasing nets is normal, because \(\psi\circ T\) is normal for every \(\psi\in N_*^+\); and a linear bijection that preserves order and suprema in both directions is a homeomorphism for the \(\sigma\)-weak topologies.

**Fact 2.5** (Traces). The following are proved in Traces on von Neumann algebras.

1. (Proposition 2.2.) A trace is monotone and takes equal values at equivalent projections. A finite trace extends to a positive linear functional with \(\tau(xy)=\tau(yx)\); a positive linear functional \(\varphi\) with \(\varphi(x^*x)=\varphi(xx^*)\) for all \(x\) is a finite trace, and it is normal exactly when it lies in \(M_*\).
2. (Proposition 3.2 and Proposition 3.7.) A normal trace \(\tau\) has a central *support* \(s(\tau)\): \(\tau\) vanishes on \(M_+(1-s(\tau))\) and is faithful on \(Ms(\tau)\). Every trace has a *semifinite part*: a unique central projection \(z\) such that \(\tau\) is semifinite on \(Mz\) and \(\tau(x)=\infty\) for every nonzero \(x\in M_+(1-z)\).
3. (Theorem 4.7.) \(M\) is finite if and only if its finite traces separate \(M_+\), and then already its finite normal traces separate \(M_+\).
4. (Theorem 5.2, Corollary 5.4, Theorem 5.5.) A finite \(M\) has a unique linear map \(T_M:M\to Z\), the *centre-valued trace*, with \(T_M(x^*x)=T_M(xx^*)\ge0\), \(T_M(ax)=aT_M(x)\) \((a\in Z)\) and \(T_M(1)=1\). It is normal and faithful. For projections, \(e\precsim f\) if and only if \(T_M(e)\le T_M(f)\), and \(e\sim f\) if and only if \(T_M(e)=T_M(f)\). Every finite trace \(\sigma\) satisfies \(\sigma(x)=\sigma(T_M(x))\).
5. (Corollary 5.12.) A finite algebra is \(\sigma\)-finite if and only if its centre is, and then \(\psi\circ T_M\) is a faithful normal finite trace for every faithful normal state \(\psi\) of \(Z\). Every finite algebra is the sum of central summands \(Mz_k\) that are \(\sigma\)-finite.
6. (*Extension from a corner*, Lemma 6.1 and Theorem 6.2.) Let \(e\in\mathcal P(M)\) and let \(\tau_0\) be a normal trace on \(eMe\). There are partial isometries \(v_j\) with \(v_jv_j^*\le e\), mutually orthogonal \(v_j^*v_j\), and \(\sum_jv_j^*v_j=c(e)\); and \(\tau(x)=\sum_j\tau_0(v_jxv_j^*)\) is the unique normal trace on \(M\) that extends \(\tau_0\) and vanishes at \(1-c(e)\). It is faithful on \(Mc(e)\) if and only if \(\tau_0\) is faithful, and semifinite if and only if \(\tau_0\) is.
7. (*Amplification*, Proposition 6.5.) Let \(\tau\) be a normal trace on \(M\) and \(K\) a Hilbert space with orthonormal basis \((\varepsilon_i)\). Then \(\tilde\tau(x)=\sum_i\tau(x_{ii})\), where \(x_{ij}\in M\) are the matrix entries of \(x\in M\bar\otimes B(K)\), is a normal trace on \(M\bar\otimes B(K)\) that does not depend on the basis; it is faithful, or semifinite, if and only if \(\tau\) is, and \(\tilde\tau(y\otimes p)=\tau(y)\) for rank-one projections \(p\).
8. (Theorem 6.7.) \(M\) is semifinite if and only if it has a faithful normal semifinite trace.

**Fact 2.6** (The Hilbert space of a trace). Let \(\tau\) be a faithful normal semifinite trace on \(M\), \(\mathfrak n_\tau=\{x\in M:\tau(x^*x)<\infty\}\), and \(L^2(M,\tau)\) the completion of \(\mathfrak n_\tau\) for \(\langle x,y\rangle=\tau(y^*x)\), with \(\Lambda_\tau:\mathfrak n_\tau\to L^2(M,\tau)\) the inclusion. Left multiplication \(L_a\Lambda_\tau(x)=\Lambda_\tau(ax)\) and right multiplication \(R_b\Lambda_\tau(x)=\Lambda_\tau(xb)\) (\(a,b\in M\)) extend to bounded operators; \(\pi_\tau(a)=L_a\) is a faithful normal representation; \(J_\tau\Lambda_\tau(x)=\Lambda_\tau(x^*)\) extends to a conjugate-linear isometric involution \(J_\tau\) of \(L^2(M,\tau)\); and
\[
\pi_\tau(M)'=\{R_b:b\in M\},\qquad J_\tau L_aJ_\tau=R_{a^*}\quad(a\in M).
\]
The map \(b\mapsto R_b\) is an injective linear \(*\)-anti-homomorphism. This is the commutation theorem of the lesson *Measurable operators for a trace: examples, convergence and the commutant* (Theorem 11.1 and Fact 2.6(e) there).

**Fact 2.7** (Normal homomorphisms). For a von Neumann algebra \(N\subseteq B(L)\) and a normal unital \(*\)-homomorphism \(\pi:N\to B(H)\), there are a Hilbert space \(R\) and an isometry \(V:H\to L\otimes R\) such that \(VV^*\) commutes with \(N\otimes1_R\) and \(\pi(y)=V^*(y\otimes1_R)V\) for \(y\in N\). This is Theorem 8.2 of Spatial tensor products of von Neumann algebras.

**Fact 2.8** (The spectrum of the centre). By the Gelfand theorem, \(Z\cong C(\Omega)\) for a compact Hausdorff space \(\Omega\), the *spectrum* of \(Z\) [\(C^*\)-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](../NCG-FOLIATIONS/companions/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-04). The projections of \(Z\) correspond to the characteristic functions of the subsets of \(\Omega\) that are both open and closed. \(\Omega\) is *stonean*: the closure of every open set is open. Every bounded continuous function on a dense open subset of \(\Omega\) extends to a continuous function on \(\Omega\). The space \(\Omega\) is hyperstonean, in particular stonean, by Abelian operator algebras, Theorem 7.1, and the extension is Theorem 4.4 there.

**Fact 2.9** (Extended centre-valued traces). Let \(\widehat Z_+\) be the set of continuous maps \(\Omega\to[0,\infty]\), where \([0,\infty]\) carries the topology of a closed interval; it contains \(Z_+\) as the finite-valued maps. Every lower semicontinuous \(h:\Omega\to[0,\infty]\) has a least continuous majorant \(\mathcal Rh\in\widehat Z_+\), equal to \(h\) outside a meagre set (Proposition 2.11). Sums in \(\widehat Z_+\) are pointwise. The product of \(f,g\in\widehat Z_+\), in particular of \(a\in Z_+\) and \(f\), is \(\mathcal R\) of the pointwise product, with \(0\cdot\infty=0\): it is the pointwise product outside a meagre set and on every open set on which one factor is finite and nonzero, and for a central projection \(z\), \(zf\) is \(f\) on \(\Omega_z\) and \(0\) elsewhere. The least upper bound of a family is \(\mathcal R\) of its pointwise supremum. The pointwise product itself need not be continuous: for \(Z=\ell^\infty(\mathbb N)\), \(\Omega=\beta\mathbb N\), \(a(n)=1/n\) and \(f=1/a\) (so \(f=\infty\) on \(\beta\mathbb N\setminus\mathbb N\), where \(a=0\)), the pointwise product is the indicator of \(\mathbb N\), which is not continuous, and \(af=1\). A set \(R\subseteq\Omega\) is *rare* if its closure has no interior point. An *extended centre-valued trace* on \(M\) is a map \(T:M_+\to\widehat Z_+\) with
\[
T(x+y)=T(x)+T(y),\qquad T(ax)=aT(x)\ (a\in Z_+),\qquad T(x^*x)=T(xx^*).
\]
It is *normal* if \(T(\sup_ix_i)=\sup_iT(x_i)\) for bounded increasing nets, *faithful* if \(T(x^*x)=0\) only for \(x=0\), and *semifinite* if \(\{x\in M:T(x^*x)\in Z_+\}\) is \(\sigma\)-weakly dense in \(M\). Then \(M\) is semifinite if and only if it has a faithful normal semifinite extended centre-valued trace. If \(T_1,T_2\) are two such traces, there is \(d\in\widehat Z_+\) with \(0<d<\infty\) outside a rare set such that, for every \(x\in M_+\), \(T_1(x)(\omega)=d(\omega)T_2(x)(\omega)\) for all \(\omega\) in a dense open set that may depend on \(x\) (with \(t\cdot\infty=\infty\) for \(t>0\)); see [Anantharaman–Popa, Section 9.2]. The proof is not repeated here. If \(M\) is finite, its centre-valued trace \(T_M\) is a faithful normal semifinite extended centre-valued trace with finite values. Section 8 of Integration for a trace, the commutation theorem, and applications proves these facts (Theorem 8.9 and the examples after Definition 8.6 there) in another model of \(\widehat Z_+\): the functions \(m\) on the normal positive functionals of \(Z\) that are pointwise suprema of increasing nets in \(Z_+\). The map sending a continuous \(f:\Omega\to[0,\infty]\) to \(m(\varphi)=\int_\Omega f\,d\mu_\varphi\), where \(\mu_\varphi\) is the Radon measure on \(\Omega\) that represents \(\varphi\), is a bijection of the model used here onto that one; it preserves order, sums, products with \(Z_+\) and least upper bounds, and it carries the \(d\) with \(0<d<\infty\) outside a rare set onto the invertible elements of Definition 8.3 there. Proposition 2.11 proves this; it also shows that the relation \(T_1(x)=dT_2(x)\) of this fact corresponds to the relation \(T_2(x)=c\cdot T_1(x)\) of Theorem 8.9(2) there, with \(c\) the image of \(1/d\).

**Fact 2.10** (Set theory). Zorn's lemma; \(\kappa\cdot\aleph_0=\kappa\) for infinite cardinals \(\kappa\); the Cantor–Bernstein theorem. These are Theorems 1.1, 8.4(1) and 8.1 of Hahn–Banach, Baire and the basic theorems on Banach spaces.

The last result of this section is proved here. It translates between the two models of the extended positive part.

**Proposition 2.11** (The two models of the extended positive part). Let \(F\) be the extended positive part of Integration for a trace, Definition 8.1. For \(\varphi\in Z_*^+\) let \(\mu_\varphi\) be the Radon measure on \(\Omega\) with \(\int a\,d\mu_\varphi=\varphi(a)\) for \(a\in Z\), and put \(\Phi(f)(\varphi)=\int_\Omega f\,d\mu_\varphi\) for \(f\in\widehat Z_+\).

1. Every lower semicontinuous \(h:\Omega\to[0,\infty]\) has a least continuous majorant \(\mathcal Rh\), and \(\{\mathcal Rh\neq h\}\) is a meagre Borel set, null for every \(\mu_\varphi\).
2. \(\Phi\) is a bijection of \(\widehat Z_+\) onto \(F\) that fixes \(Z_+\); \(f\le g\) if and only if \(\Phi(f)\le\Phi(g)\); and \(\Phi\) preserves sums, products (\(\Phi(fg)=\Phi(f)\cdot\Phi(g)\) for the product of Lemma 8.2(5) there, and \(\Phi(af)=a\cdot\Phi(f)\) for \(a\in Z_+\)) and least upper bounds of arbitrary families.
3. \(\Phi(f)\) is finite, respectively invertible, in the sense of Definition 8.3 there if and only if \(f<\infty\), respectively \(0<f<\infty\), outside a rare set.
4. Let \(T_1,T_2:M_+\to\widehat Z_+\), and let \(d\in\widehat Z_+\) satisfy \(0<d<\infty\) outside a rare set. Then \(T_1(x)=dT_2(x)\) in the sense of Fact 2.9 for all \(x\in M_+\) if and only if \(\Phi(T_2(x))=\Phi(1/d)\cdot\Phi(T_1(x))\) for all \(x\in M_+\).

So additivity, the rule \(T(ax)=aT(x)\), normality, faithfulness, semifiniteness and the form of uniqueness mean the same in both models, and Section 8 of that lesson proves Fact 2.9. If \(Z=0\), then \(\Omega=\varnothing\) and both models have one element.

**Proof.** (1) The space \(\Omega\) is stonean (Fact 2.8), so its open and closed sets form a base: for \(\omega\) in an open set \(U\), choose an open \(V\ni\omega\) with \(\overline V\subseteq U\); then \(\overline V\) is open and closed. Let \(\theta(t)=t/(1+t)\), \(\theta(\infty)=1\), \(k=\theta\circ h\), and \(k^*(\omega)=\inf_U\sup_Uk\), the infimum over the open neighbourhoods \(U\) of \(\omega\). Then \(k\le k^*\), \(k^*\) is upper semicontinuous, and \(\{k^*>r\}=\bigcup_{s>r}\overline{\{k>s\}}\) is open, because \(k\) is lower semicontinuous and closures of open sets are open. So \(k^*\) is continuous, and every continuous \(v\ge k\) satisfies \(v\ge k^*\). Put \(\mathcal Rh=\theta^{-1}\circ k^*\). If \(k^*(\omega)>k(\omega)\), a rational \(r\) between the two values puts \(\omega\) in \(\overline{\{k>r\}}\setminus\{k>r\}\), a closed set without interior points; so \(\{\mathcal Rh\neq h\}\) is meagre. Let \(R\) be closed without interior points. The open and closed subsets \(C\) of \(\Omega\setminus R\) form an upward directed family with union \(\Omega\setminus R\), and the least upper bound of their indicators in \(Z\) is \(1\), since a continuous upper bound is \(\ge1\) on the dense set \(\Omega\setminus R\). Least upper bounds in \(Z\) of bounded increasing nets are strong limits (Commutative operator algebras, Lemma 2.4), so normality of \(\varphi\) gives \(\mu_\varphi(\Omega)=\sup_C\mu_\varphi(C)\le\mu_\varphi(\Omega\setminus R)\), and \(\mu_\varphi(R)=0\). A meagre set lies in a countable union of such sets \(R\).

(2) For \(f\in\widehat Z_+\), the functions \(f\wedge n\in Z_+\) increase to \(f\), so \(\Phi(f)(\varphi)=\sup_n\varphi(f\wedge n)\) by monotone convergence; hence \(\Phi(f)\in F\), and \(\Phi\) fixes \(Z_+\). For a Radon measure \(\mu\) and an increasing net \((h_i)\) of lower semicontinuous functions, \(\int\sup_ih_i\,d\mu=\sup_i\int h_i\,d\mu\). For indicators of open sets this follows from inner regularity, since a compact subset of \(\bigcup_iU_i\) lies in one \(U_i\). In general, with \(h=\sup_ih_i\) and \(s_{N,j}(t)=2^{-j}\sum_{r=1}^{N2^j}1_{\{t>r2^{-j}\}}\), which satisfies \(t\wedge N-2^{-j}\le s_{N,j}(t)\le t\wedge N\), we get \(\int s_{N,j}(h)\,d\mu=\sup_i\int s_{N,j}(h_i)\,d\mu\le\sup_i\int h_i\,d\mu\); let \(j\to\infty\) and then \(N\to\infty\). Now let \(m\in F\) be represented by an increasing net \((a_i)\) in \(Z_+\), and \(h=\sup_ia_i\), which is lower semicontinuous. By the preceding sentence and (1), \(m(\varphi)=\int h\,d\mu_\varphi=\int\mathcal Rh\,d\mu_\varphi=\Phi(\mathcal Rh)(\varphi)\); so \(\Phi\) is onto. It is monotone. If \(f(\omega)>g(\omega)\), choose reals \(r<s\) with \(g(\omega)<r<s<f(\omega)\), an open and closed set \(C\ni\omega\) inside \(\{g<r\}\cap\{f>s\}\), and a unit vector \(\xi\) in the range of the nonzero projection \(1_C\). The measure of \(\varphi=\omega_\xi|_Z\) lives on \(C\), so \(\Phi(f)(\varphi)\ge s>r\ge\Phi(g)(\varphi)\). Hence \(\Phi\) is an order isomorphism, and it preserves every least upper bound; in \(\widehat Z_+\) the least upper bound of \((f_\alpha)\) is \(\mathcal R(\sup_\alpha f_\alpha)\), by (1). Sums of continuous \([0,\infty]\)-valued maps are continuous, and \(\Phi\) is additive. The pointwise product \(fg=\sup_{n,k}(f\wedge n)(g\wedge k)\) is lower semicontinuous, and by the preceding arguments \(\Phi(\mathcal R(fg))(\varphi)=\int fg\,d\mu_\varphi=\sup_{n,k}\varphi((f\wedge n)(g\wedge k))\), which is \((\Phi(f)\cdot\Phi(g))(\varphi)\) by Lemma 8.2(5) there. For \(a\in Z_+\), uniqueness of the representing measure gives \(\mu_{a\varphi}=a\mu_\varphi\), so \(\Phi(af)(\varphi)=\Phi(f)(a\varphi)=(a\cdot\Phi(f))(\varphi)\). Finally, if one factor is finite and nonzero on an open set \(D\), the pointwise product is continuous on \(D\), and \(\mathcal R\) does not change a function on an open set where it is continuous.

(3) A projection of \(Z\) is \(1_C\) with \(C\) open and closed, and for orthogonal \(z_k=1_{C_k}\) the least upper bound of the partial sums is \(1_{\overline{\bigcup_kC_k}}\); so \(\sum_kz_k=1\) exactly when \(\bigcup_kC_k\) is dense. If \(\Phi(f)\) is finite, then \(z_kf\in Z_+\) by (2), so \(f\) is bounded on each \(C_k\) and finite on the dense open set \(\bigcup_kC_k\). Conversely, if \(\{f<\infty\}\) is dense, the open and closed sets \(C_n=\overline{\{f<n\}}\subseteq\{f\le n\}\) increase to \(\{f<\infty\}\), and \(z_n=1_{C_n\setminus C_{n-1}}\), with \(C_0=\varnothing\), satisfy \(\sum_nz_n=1\) and \(z_nf\le nz_n\). For invertibility, use the sets \(\overline{\{1/n<f<n\}}\subseteq\{1/n\le f\le n\}\) in the same way. The set \(\{0<f<\infty\}\) is open, so it is dense exactly when its closed complement has no interior points, that is, is rare; and the same holds for \(\{f<\infty\}\).

(4) Let \(G=\{0<d<\infty\}\), a dense open set. On \(G\), the products with \(d\) and with \(1/d\) are pointwise, by (2). If \(T_1(x)=dT_2(x)\) on a dense subset of \(G\), then \(T_2(x)=(1/d)T_1(x)\) on that subset; both sides are continuous, so they agree everywhere, and \(\Phi(T_2(x))=\Phi(1/d)\cdot\Phi(T_1(x))\) by (2). Conversely, applying \(\Phi^{-1}\) gives \(T_2(x)=(1/d)T_1(x)\), which is a pointwise identity on \(G\); multiplying by \(d(\omega)\in(0,\infty)\) gives \(T_1(x)=dT_2(x)\) on \(G\). \(\square\)

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

**Remark 4.4.** If \(M\) is of type III, the commutant of every faithful normal representation is of type III (Corollary 9.4), hence properly infinite. So an algebra of type III with \(\sigma\)-finite centre has exactly one faithful normal representation with \(\sigma\)-finite commutant, up to unitary equivalence (Corollary 9.5).

The next lemma counts orthogonal projections. It is used in Section 7, where the algebras are not \(\sigma\)-finite.

**Lemma 4.5** (Counting orthogonal projections). Let \(\{e_j\}_{j\in J}\) be mutually orthogonal \(\sigma\)-finite projections of \(M\) with \(\sum_je_j=1\). If \(\{f_i\}_{i\in I}\) are mutually orthogonal *nonzero* projections of \(M\), then \(|I|\le\aleph_0\cdot|J|\). If \(J\) is infinite, then \(|I|\le|J|\).

*Remark.* The bound fails for orthogonal families that contain the zero projection, which may be repeated any number of times; so the \(f_i\) are required to be nonzero.

**Proof.** For each \(j\), the algebra \(e_jMe_j\) is \(\sigma\)-finite, so it has a faithful normal state \(\psi_j\) (Fact 2.4(1)); put \(\varphi_j(x)=\psi_j(e_jxe_j)\). Let \(I_j=\{i:\varphi_j(f_i)>0\}\). For a finite \(F\subseteq I\), \(\sum_{i\in F}\varphi_j(f_i)=\varphi_j(\sum_{i\in F}f_i)\le1\), so \(I_j\) is countable. Fix \(i\). Since \(f_i\ne0\) and \(f_i=\sum_jf_ie_j\) strongly, some \(f_ie_j\ne0\). Then \(e_jf_ie_j=(f_ie_j)^*(f_ie_j)\ne0\), and \(\varphi_j(f_i)=\psi_j(e_jf_ie_j)>0\) by faithfulness. So \(I=\bigcup_jI_j\), and \(|I|\le\aleph_0\cdot|J|\). If \(J\) is infinite, \(\aleph_0\cdot|J|=|J|\) (Fact 2.10). \(\square\)

## 5. Cyclic and separating vectors

A cyclic vector exists only if \(M'\) is \(\sigma\)-finite, and a separating vector only if \(M\) is. Under either condition the space splits along the centre into a cyclic part and a separating part.

**Proposition 5.1.** Suppose that \(M\) or \(M'\) is \(\sigma\)-finite. Then there are a central projection \(z\) and a vector \(\xi\in H\) such that \(z\xi\) is cyclic for \(Mz\) on \(zH\), and \((1-z)\xi\) is separating for \(M(1-z)\) on \((1-z)H\). Equivalently, \(z\le p'_\xi\) and \(1-z\le p_\xi\).

*Reference:* [Blackadar, III.2.6.11], for \(\sigma\)-finite \(M\).

**Proof.** By Zorn's lemma choose nonzero vectors \(\xi_i\) (\(i\in I\)) such that the projections \(p_{\xi_i}\) are mutually orthogonal and so are the projections \(p'_{\xi_i}\), the family being maximal for this property. The set \(I\) is countable: the \(p_{\xi_i}\) are nonzero orthogonal projections of \(M\), the \(p'_{\xi_i}\) are nonzero orthogonal projections of \(M'\), and one of the two algebras is \(\sigma\)-finite. After multiplying the \(\xi_i\) by positive scalars we may assume \(\sum_i\|\xi_i\|^2<\infty\). The \(\xi_i\) are mutually orthogonal, since \(\xi_i\in p_{\xi_i}H\), so \(\xi=\sum_i\xi_i\) converges. Put \(e=\sum_ip_{\xi_i}\in M\) and \(e'=\sum_ip'_{\xi_i}\in M'\).

*Step 1: \(p_\xi=e\) and \(p'_\xi=e'\).* For \(j\ne i\), \(\xi_j\in p'_{\xi_j}H\perp p'_{\xi_i}H\), so \(p'_{\xi_i}\xi=\xi_i\). Hence \(\xi_i\in M'\xi\), and \(p_{\xi_i}\le p_\xi\) for every \(i\); so \(e\le p_\xi\). Conversely \(\xi\in eH\), so \(p_\xi\le e\) by Fact 2.3(1). Exchanging \(M\) and \(M'\) gives \(p'_\xi=e'\).

*Step 2: \((1-e)(1-e')=0\).* The commuting projections \(1-e\in M\) and \(1-e'\in M'\) have as product the projection onto \((1-e)H\cap(1-e')H\). A nonzero vector \(\eta\) in this space would have \(p_\eta\le1-e\) and \(p'_\eta\le1-e'\) (Fact 2.3(1)), and could be added to the family.

*Step 3.* By Lemma 3.3(6), \(c(1-e)\,c(1-e')=0\). Put \(z=c(1-e)\). Then \(z(1-e')=zc(1-e')(1-e')=0\), so \(z\le e'=p'_\xi\). Also \(1-e\le z\), so \(1-z\le e=p_\xi\). Finally, \(z\le p'_\xi\) says \(p'_{z\xi}=zp'_\xi=z\) (Lemma 3.3(1)), that is, \(z\xi\) is cyclic for \(Mz\); and \(1-z\le p_\xi\) says that \((1-z)\xi\) is cyclic for \(M'(1-z)\), that is, separating for \(M(1-z)\) (Fact 2.4(1)). \(\square\)

Exercise 12.4 shows exactly when such a splitting exists.

**Proposition 5.2** (The largest \(\sigma\)-finite projection). Let \(Z\) be \(\sigma\)-finite. There is a \(\sigma\)-finite projection \(e\in M\) such that \(f\precsim e\) for every \(\sigma\)-finite projection \(f\in M\). Any two such projections are equivalent.

**Proof.** Let \(1=z_f+z_\infty\) with \(Mz_f\) finite and \(Mz_\infty\) properly infinite (Fact 2.2(6)). The finite algebra \(Mz_f\) has the \(\sigma\)-finite centre \(Zz_f\), so it is \(\sigma\)-finite (Fact 2.5(5)); that is, \(z_f\) is a \(\sigma\)-finite projection.

Next we build a \(\sigma\)-finite, properly infinite projection \(g\) with \(c(g)=z_\infty\). If \(z_\infty=0\), take \(g=0\). Otherwise, the construction in the proof of Theorem 4.3(1), applied to the algebra \(Mz_\infty\) with its \(\sigma\)-finite centre \(Zz_\infty\), gives a normal state whose support \(h\) has central support \(z_\infty\). The projection \(h\) is \(\sigma\)-finite, because the state is faithful on \(hMh\). By division by \(\aleph_0\) (Fact 2.2(9)), \(z_\infty=\sum_{n\ge1}e_n\) with mutually orthogonal \(e_n\sim z_\infty\). As \(h\le z_\infty\sim e_n\), there are projections \(h_n\le e_n\) with \(h_n\sim h\). Put \(g=\sum_nh_n\).

- *\(g\) is \(\sigma\)-finite.* Let \(\psi_n\) be a faithful normal state of \(h_nMh_n\). The normal functional \(x\mapsto\sum_n2^{-n}\psi_n(h_nxh_n)\) is faithful on \(gMg\): if it vanishes at \(x\ge0\) in \(gMg\), then \(h_nxh_n=0\), so \(x^{1/2}h_n=0\) for all \(n\), and \(x^{1/2}=x^{1/2}g=0\).
- *\(c(g)=z_\infty\),* because \(c(h_n)=c(h)=z_\infty\) for every \(n\) (Fact 2.1(2)).
- *\(g\) is properly infinite.* Let \(w\) be central with \(wg\ne0\). Then \(wz_\infty\ne0\), so \(wh_1\ne0\), because \(c(h_1)=z_\infty\). Additivity, applied to \(wh_n\sim wh_{n+1}\), gives \(wg=\sum_{n\ge1}wh_n\sim\sum_{n\ge2}wh_n=wg-wh_1\). So \(wg\) is infinite.

Put \(e=z_f+g\). It is \(\sigma\)-finite by the argument used for \(g\). Let \(f\) be \(\sigma\)-finite. Then \(fz_f\le z_f\). The projection \(fz_\infty\) is \(\sigma\)-finite (orthogonal families in \((fz_\infty)M(fz_\infty)\) are orthogonal families in \(fMf\)), and \(c(fz_\infty)\le z_\infty=c(g)\). By absorption (Fact 2.2(11)), \(fz_\infty\precsim g\). Adding, \(f\precsim z_f+g=e\). If \(e_1\) and \(e_2\) both have the property, then \(e_1\precsim e_2\precsim e_1\), and \(e_1\sim e_2\) by Schröder–Bernstein. \(\square\)

**Proposition 5.3** (The largest cyclic projection). Let \(Z\) be \(\sigma\)-finite. There is a vector \(\xi\in H\) with \(p_\eta\precsim p_\xi\) for every \(\eta\in H\).

**Proof.** *Step 1: \(M\) is \(\sigma\)-finite.* Take \(z\) and \(\xi\) from Proposition 5.1, so that \(z\le p'_\xi\) and \(1-z\le p_\xi\). Let \(\eta\in H\). Since \(1-z\le p_\xi\), \((1-z)p_\eta\le1-z=(1-z)p_\xi\). Since \(z\le p'_\xi\), \(p'_{z\eta}=zp'_\eta\le z=zp'_\xi=p'_{z\xi}\) (Lemma 3.3(1)). The transfer theorem (Fact 2.3(2)) turns \(p'_{z\eta}\precsim p'_{z\xi}\) into \(zp_\eta=p_{z\eta}\precsim p_{z\xi}=zp_\xi\). Adding the two parts, \(p_\eta\precsim p_\xi\).

*Step 2: the general case.* Let \(e\) be the projection of Proposition 5.2. The reduced algebra \(eMe\) on \(eH\) is \(\sigma\)-finite, and its commutant is \(M'e\) (Fact 2.1(1)). For \(\eta\in eH\), its cyclic projection in \(eMe\) is the projection onto \([M'e\eta]=[M'\eta]\), which is \(p_\eta\). Step 1, applied to \(eMe\), gives \(\xi\in eH\) with \(p_\eta\precsim p_\xi\) for all \(\eta\in eH\). Now let \(\eta\in H\). By Lemma 3.3(5), \(p_\eta\) is \(\sigma\)-finite, so \(p_\eta\precsim e\): some \(v\in M\) has \(v^*v=p_\eta\) and \(vv^*\le e\). Then \(v\eta\in vv^*H\subseteq eH\), and \(p_{v\eta}=vp_\eta v^*\sim p_\eta\) (Lemma 3.3(2)). So \(p_\eta\sim p_{v\eta}\precsim p_\xi\). \(\square\)

**Example 5.4.** In \(B(H)\), with \(H\) of uncountable Hilbert dimension, the \(\sigma\)-finite projections are those of countable rank; a largest one is the projection onto any separable infinite-dimensional subspace. The cyclic projections are those of rank at most one, because \(B(H)'=\mathbb C1\).

**Example 5.5** (The centre must be \(\sigma\)-finite). Let \(\Gamma\) be uncountable and let \(M=\ell^\infty(\Gamma)\) act on \(\ell^2(\Gamma)\) by multiplication. An operator that commutes with every multiplication by an indicator \(1_{\{\gamma\}}\) maps each basis vector \(\delta_\gamma\) into \(\mathbb C\delta_\gamma\), so it is a multiplication operator; thus \(M'=M=Z\). The \(\sigma\)-finite projections are the indicators \(1_A\) of countable sets \(A\), the cyclic projections are the indicators of the countable supports of vectors, and \(e\precsim f\) means \(e\le f\), since \(M\) is commutative. No countable \(A\) contains all points, so there is neither a largest \(\sigma\)-finite projection nor a largest cyclic projection. Here \(Z\) is not \(\sigma\)-finite.

## 6. Limits of projections

Subequivalence survives limits under a finite projection, and along sequences in general. The first result uses traces.

**Theorem 6.1.** Let \(f\in M\) be a finite projection, and let \((e_i)\) be a net of projections converging strongly to a projection \(e\), with \(e_i\precsim f\) for every \(i\). Then \(e\precsim f\).

**Proof.** Since \(e_i\precsim f\), \(c(e_i)\le c(f)\), so \(e_i=e_ic(f)\); in the limit, \(e=ec(f)\). By the comparison theorem there is a central projection \(w\) with \(we\precsim wf\) and \((1-w)f\precsim(1-w)e\). It suffices to show \((1-w)e\precsim(1-w)f\). Choose \(f_0\le(1-w)e\) with \(f_0\sim(1-w)f\), and put \(r=(1-w)e-f_0\). Suppose \(r\ne0\).

Since \(r\le e\le c(f)\), \(c(r)c(f)=c(r)\ne0\), and Fact 2.2(4) gives nonzero projections \(r_1\le r\) and \(f_1\le f\) with \(r_1\sim f_1\). The algebra \(fMf\) is finite, so it has a finite normal trace \(\tau_0\) with \(\tau_0(f_1)>0\) (Fact 2.5(3)). Extend it to a normal trace \(\tau(x)=\sum_j\tau_0(v_jxv_j^*)\) on \(M\) (Fact 2.5(6)). Each term \(x\mapsto\tau_0(v_jxv_j^*)\) is a positive normal functional, because \(\tau_0\in(fMf)_*\) (Fact 2.5(1)). Hence \(\tau\) is a sum of positive normal functionals \(\psi_j\). Along the net, \((1-w)e_i\to(1-w)e\) strongly, hence \(\sigma\)-weakly (Fact 2.4(4)). For a finite set \(F\) of indices,
\[
\sum_{j\in F}\psi_j((1-w)e)=\lim_i\sum_{j\in F}\psi_j((1-w)e_i)\le\liminf_i\tau((1-w)e_i)\le\tau((1-w)f),
\]
because \((1-w)e_i\precsim(1-w)f\) and traces are monotone and constant on equivalence classes (Fact 2.5(1)). Taking the supremum over \(F\), \(\tau((1-w)e)\le\tau((1-w)f)\le\tau_0(f)<\infty\). But \(\tau((1-w)e)=\tau(f_0)+\tau(r)=\tau((1-w)f)+\tau(r)\). So \(\tau(r)=0\), while \(\tau(r)\ge\tau(r_1)=\tau(f_1)=\tau_0(f_1)>0\). This contradiction shows \(r=0\). So \((1-w)e=f_0\sim(1-w)f\), and \(e=we+(1-w)e\precsim wf+(1-w)f=f\). \(\square\)

**Theorem 6.2.** Let \(f\in M\) be any projection.

1. If a sequence of projections \(e_n\) converges strongly to a projection \(e\) and \(e_n\precsim f\) for all \(n\), then \(e\precsim f\).
2. If \(M\) is locally \(\sigma\)-finite, the same holds for nets.

**Proof.** Write \(f=f_1+f_2\) with \(f_1\) finite, \(f_2\) properly infinite and \(c(f_1)c(f_2)=0\) (Fact 2.2(6)), and put \(c=c(f_1)\). Then \(fc=f_1\) and \(f(1-c)=f_2\).

*The finite part.* \(e_nc\precsim fc=f_1\) and \(e_nc\to ec\), so \(ec\precsim f_1\) by Theorem 6.1. This works for nets as well.

*The properly infinite part, for sequences.* If \(f_2=0\), then \(e_n(1-c)=0\) for all \(n\) and \(e(1-c)=0\). Otherwise put \(g_n=\bigvee_{k\le n}e_k(1-c)-\bigvee_{k<n}e_k(1-c)\). These are mutually orthogonal, and \(\sum_ng_n=\bigvee_ne_n(1-c)\). By the parallelogram law (Fact 2.2(2)), \(g_n\sim e_n(1-c)-e_n(1-c)\wedge\bigvee_{k<n}e_k(1-c)\le e_n(1-c)\precsim f_2\). Absorption (Fact 2.2(11)) gives \(\sum_ng_n\precsim f_2\). Every vector \(\zeta\) in \(e(1-c)H\) is the limit of \(e_n(1-c)\zeta\), so \(e(1-c)\le\bigvee_ne_n(1-c)\precsim f_2\).

*The properly infinite part, for nets in a locally \(\sigma\)-finite algebra.* As in Theorem 6.1, \(e\le c(f)\), and \(c(f)=c(f_1)+c(f_2)\), so \(e(1-c)\le c(f_2)\). Every projection \(g\) of \(M\) is locally \(\sigma\)-finite. Indeed, let \(w\) be central with \(wg\ne0\). Then \(wc(g)\ne0\) (Fact 2.1(2)), and since \(M\) is locally \(\sigma\)-finite, \(wc(g)\) majorizes a nonzero central \(z'\) with \(Mz'\) \(\sigma\)-finite. As \(z'\le c(g)\), \(z'g\ne0\); and \(z'g\) is \(\sigma\)-finite, because orthogonal families in its corner are orthogonal families in \(Mz'\). So absorption (Fact 2.2(11)) gives \(e(1-c)\precsim f_2\).

Adding the two parts gives \(e\precsim f\). \(\square\)

**Example 6.3** (Nets in general). Let \(H\) be a nonseparable Hilbert space (for instance of Hilbert dimension \(\aleph_1\)), \(M=B(H)\), and \(f\) the projection onto a separable infinite-dimensional subspace. The projections onto the spans of finite subsets of an orthonormal basis form a net of finite-rank projections \(e_F\precsim f\) that converges strongly to \(1\). But \(1\not\precsim f\), since an isometry of \(H\) into \(fH\) would make \(\dim H\le\aleph_0\). The same example appears in Traces on von Neumann algebras (Example 4.3). So Theorem 6.1 needs \(f\) finite for nets, and Theorem 6.2(2) needs a countability hypothesis.

**Theorem 6.4** (Limits of cyclic projections). If cyclic projections \(p_{\xi_n}\) (\(n\ge1\)) of \(M\) converge strongly to a projection \(e\), then \(e\) is cyclic. If \(M\) is \(\sigma\)-finite, the same holds for nets.

**Proof.** Put \(p=\bigvee_np_{\xi_n}\). By the parallelogram law, \(p\) is the sum of the mutually orthogonal projections \(\bigvee_{k\le n}p_{\xi_k}-\bigvee_{k<n}p_{\xi_k}\precsim p_{\xi_n}\), which are cyclic, hence \(\sigma\)-finite (Lemma 3.3(2), (3) and (5)). A countable orthogonal sum of \(\sigma\)-finite projections is \(\sigma\)-finite, by the argument used for \(g\) in Proposition 5.2. So \(p\) is \(\sigma\)-finite. Every vector \(\zeta\in eH\) is the limit of \(p_{\xi_n}\zeta\in pH\), so \(e\le p\).

Consider the \(\sigma\)-finite algebra \(pMp\) on \(pH\). For \(\eta\in pH\), its cyclic projection in \(pMp\) is \([M'p\eta]=p_\eta\). In particular \(\xi_n=p_{\xi_n}\xi_n\in pH\), and the \(p_{\xi_n}\) are cyclic projections of \(pMp\). By Proposition 5.3 (Step 1), \(pMp\) has a largest cyclic projection \(p_\xi\) with \(\xi\in pH\), so \(p_{\xi_n}\precsim p_\xi\). Theorem 6.2(1), applied in \(pMp\), gives \(e\precsim p_\xi\). By Lemma 3.3(2) and (3), \(e\) is cyclic.

If \(M\) is \(\sigma\)-finite and \((p_{\xi_i})\) is a net, Proposition 5.3 gives a largest cyclic projection \(p_\xi\) of \(M\), and Theorem 6.2(2) gives \(e\precsim p_\xi\). \(\square\)

**Example 6.5** (Nets of cyclic projections). In Example 5.5 the indicators \(1_F\) of finite sets \(F\subseteq\Gamma\) are cyclic projections, and they converge strongly to \(1\), which is not cyclic. So the net version needs \(\sigma\)-finiteness.

## 7. Unitary involutions

On the Hilbert space of a trace, the map \(x\mapsto x^*\) turns left multiplications into right multiplications. This section takes that symmetry as an axiom and draws its consequences.

**Definition 7.1.** A *unitary involution* of \(\{M,H\}\) is a conjugate-linear map \(J:H\to H\) such that

1. \(\langle J\xi,J\eta\rangle=\langle\eta,\xi\rangle\) for \(\xi,\eta\in H\);
2. \(J^2=1\);
3. \(JMJ=M'\);
4. \(JaJ=a^*\) for every \(a\in Z\).

By (1) and (2), \(J\) is a bijective isometry, and \(\langle J\xi,\eta\rangle=\langle J\xi,J(J\eta)\rangle=\langle J\eta,\xi\rangle\). For \(x\in B(H)\), \(JxJ\) is linear, and \((JxJ)^*=Jx^*J\), because \(\langle JxJ\xi,\eta\rangle=\langle J\eta,xJ\xi\rangle=\langle x^*J\eta,J\xi\rangle=\langle\xi,Jx^*J\eta\rangle\). Since \(J^2=1\), condition (3) is equivalent to \(JM'J=M\). Condition (4) holds as soon as \(JzJ=z\) for every central projection \(z\), because \(Z\) is the norm-closed linear span of its projections and \(x\mapsto JxJ\) is conjugate-linear and isometric.

**Example 7.2.**

1. (*The Hilbert space of a trace.*) Let \(\tau\) be a faithful normal semifinite trace on \(M\). By Fact 2.6, \(J_\tau\) satisfies (1)–(3) for \(\pi_\tau(M)\) on \(L^2(M,\tau)\): \(J_\tau\pi_\tau(M)J_\tau=\{R_{a^*}:a\in M\}=\pi_\tau(M)'\). For central \(a\), \(R_{a^*}\Lambda_\tau(x)=\Lambda_\tau(xa^*)=\Lambda_\tau(a^*x)\), so \(J_\tau L_aJ_\tau=L_{a^*}\), which is (4). So \(J_\tau\) is a unitary involution, the *canonical* one of \(L^2(M,\tau)\).
2. (*Matrices.*) The algebra \(M_n(\mathbb C)\) acting on itself by left multiplication, with \(\langle x,y\rangle=\mathrm{Tr}(y^*x)\) and \(Jx=x^*\), is the case \(\tau=\mathrm{Tr}\) of (1). Under the identification \(E_{ij}\mapsto\delta_i\otimes\delta_j\) of \(M_n(\mathbb C)\) with \(\mathbb C^n\otimes\mathbb C^n\), the action becomes \(a\mapsto a\otimes1\), and \(J\) becomes the conjugate-linear map with \(J(\delta_i\otimes\delta_j)=\delta_j\otimes\delta_i\).
3. (*Multiplication algebras.*) \(L^\infty[0,1]\), acting on \(L^2[0,1]\) by multiplication, has the cyclic vector \(1\), so it is its own commutant (Projections and types of von Neumann algebras, Lemma 11.1). Complex conjugation \(Jf=\bar f\) is a unitary involution: \(JM_gJ=M_{\bar g}\).
4. (*No unitary involution.*) Let \(M=M_n(\mathbb C)\otimes1\) on \(\mathbb C^n\otimes\mathbb C^m\) with \(m\ne n\). By Fact 2.2(7), \(M'=1\otimes M_m(\mathbb C)\). A unitary involution would give a linear bijection \(x\mapsto Jx^*J\) of \(M\) onto \(M'\) (Lemma 7.3), so \(n^2=m^2\). Hence there is none. The case \(n=1\), \(m=2\) is \(\mathbb C1\) on \(\mathbb C^2\).

**Lemma 7.3** (The anti-isomorphism of a unitary involution). Let \(J\) be a unitary involution of \(\{M,H\}\) and put \(\theta(x)=Jx^*J\) for \(x\in M\).

1. \(\theta\) is a linear bijection of \(M\) onto \(M'\) with \(\theta(xy)=\theta(y)\theta(x)\) and \(\theta(x^*)=\theta(x)^*\), and \(\theta(a)=a\) for \(a\in Z\). It is a homeomorphism for the \(\sigma\)-weak topologies.
2. \(\theta\) maps projections to projections; it preserves the order, equivalence and subequivalence of projections, and it maps finite, properly infinite and \(\sigma\)-finite projections to projections of the same kind.
3. For every central projection \(z\), \(Mz\) is \(\sigma\)-finite (finite, properly infinite) if and only if \(M'z\) is.
4. \(J\) is also a unitary involution of \(\{M',H\}\).

**Proof.** (1) \(x\mapsto x^*\) and \(x\mapsto JxJ\) are conjugate-linear, so \(\theta\) is linear, and \(\theta(M)=JMJ=M'\). The inverse is \(y'\mapsto Jy'^*J\). Next, \(\theta(xy)=Jy^*x^*J=Jy^*JJx^*J=\theta(y)\theta(x)\) and \(\theta(x^*)=JxJ=(Jx^*J)^*=\theta(x)^*\). For \(a\in Z\), \(\theta(a)=Ja^*J=(a^*)^*=a\) by Definition 7.1(4). Finally, \(\langle\theta(x)\xi,\eta\rangle=\langle J\eta,x^*J\xi\rangle=\langle xJ\eta,J\xi\rangle\), so every vector functional of \(\theta(x)\) is a vector functional of \(x\); countable sums of vector functionals define the \(\sigma\)-weak topology, so \(\theta\) and, by symmetry, \(\theta^{-1}\) are \(\sigma\)-weakly continuous.

(2) For a projection \(p\), \(\theta(p)=JpJ\) is a projection. If \(p\le q\), then \(pq=p\), so \(\theta(q)\theta(p)=\theta(p)\), that is, \(\theta(p)\le\theta(q)\). If \(v^*v=p\) and \(vv^*=q\), then \(\theta(v)\theta(v)^*=\theta(v^*v)=\theta(p)\) and \(\theta(v)^*\theta(v)=\theta(vv^*)=\theta(q)\); so \(\theta(p)\sim\theta(q)\). With the order this gives subequivalence. If \(p\) is finite and \(\theta(p)\sim g\le\theta(p)\), then applying the same facts to \(\theta^{-1}\) gives \(p\sim\theta^{-1}(g)\le p\), so \(\theta^{-1}(g)=p\) and \(g=\theta(p)\). For a central \(z\), \(\theta(zp)=\theta(p)z\), so nonzero central cuts correspond, and proper infiniteness is preserved. Finally \(\theta\) maps \(pMp\) onto \(\theta(p)M'\theta(p)\) and orthogonal families of projections to orthogonal families.

(3) \(\theta\) maps \(Mz\) onto \(M'z\), and (2) applies.

(4) \(JM'J=M=(M')'\), and \(M'\) has the centre \(Z\). \(\square\)

**Proposition 7.4** (Cyclic projections under \(J\)). Let \(J\) be a unitary involution of \(\{M,H\}\) and \(\xi\in H\). Then
\[
Jp_\xi J=p'_{J\xi},\qquad Jp'_\xi J=p_{J\xi},\qquad p_\xi\sim p_{J\xi}\ \text{in }M,\qquad p'_\xi\sim p'_{J\xi}\ \text{in }M'.
\tag{7.1}
\]

**Proof.** \(JM'\xi=(JM'J)J\xi=MJ\xi\). As \(J\) is a bijective isometry, it maps the closed subspace \([M'\xi]\) onto \([MJ\xi]\). For a closed subspace \(L\) with projection \(P_L\), \(JP_LJ\) is a self-adjoint idempotent with range \(JL\), so it is \(P_{JL}\). Hence \(Jp_\xi J=p'_{J\xi}\). Applying this to \(J\xi\) and using \(J^2=1\) gives \(Jp'_\xi J=p_{J\xi}\).

For the equivalence, the comparison theorem gives a central projection \(z\) with \(zp_\xi\precsim zp_{J\xi}\) and \((1-z)p_{J\xi}\precsim(1-z)p_\xi\). Put \(\xi_1=z\xi\). Since \(JzJ=z\), \(J\) commutes with \(z\), so \(J\xi_1=zJ\xi\), and by Lemma 3.3(1) \(p_{\xi_1}=zp_\xi\precsim zp_{J\xi}=p_{J\xi_1}\). The transfer theorem (Fact 2.3(2)) gives \(p'_{\xi_1}\precsim p'_{J\xi_1}\) in \(M'\). The map \(y'\mapsto Jy'J\) on projections is \(\theta^{-1}\), which preserves subequivalence (Lemma 7.3). By the first part it sends \(p'_{\xi_1}\) to \(p_{J\xi_1}\) and \(p'_{J\xi_1}\) to \(p_{\xi_1}\). So \(p_{J\xi_1}\precsim p_{\xi_1}\), and Schröder–Bernstein gives \(zp_\xi=p_{\xi_1}\sim p_{J\xi_1}=zp_{J\xi}\). The same argument, applied to \(\eta=(1-z)J\xi\), for which \(J\eta=(1-z)\xi\) and \(p_\eta\precsim p_{J\eta}\), gives \((1-z)p_{J\xi}\sim(1-z)p_\xi\). Adding, \(p_\xi\sim p_{J\xi}\). The last statement is the same fact for \(M'\), which has the unitary involution \(J\) by Lemma 7.3(4). \(\square\)

**Corollary 7.5** (Traces through \(J\)). Let \(J\) be a unitary involution of \(\{M,H\}\).

1. If \(\tau\) is a normal trace on \(M\), then \(\tau^J(y')=\tau(Jy'J)\) (\(y'\in M'_+\)) is a normal trace on \(M'\), faithful, semifinite or finite exactly when \(\tau\) is, and \(\tau^J(p'_\xi)=\tau(p_\xi)\) for every \(\xi\in H\).
2. If \(T\) is an extended centre-valued trace on \(M\), then \(T^J(y')=T(Jy'J)\) is an extended centre-valued trace on \(M'\) (whose centre is \(Z\)), normal, faithful or semifinite exactly when \(T\) is, and \(T^J(p'_\xi)=T(p_\xi)\) for every \(\xi\in H\).

**Proof.** For \(y'\in M'_+\), \(Jy'J=\theta^{-1}(y')\), and \(\theta^{-1}\) is a linear bijection of \(M'\) onto \(M\) that reverses products, commutes with the adjoint and preserves order and suprema. Hence \(\tau^J\) is additive, homogeneous and normal, and
\[
\tau^J(w^*w)=\tau\bigl(\theta^{-1}(w)\theta^{-1}(w)^*\bigr)=\tau\bigl(\theta^{-1}(w)^*\theta^{-1}(w)\bigr)=\tau^J(ww^*)\qquad(w\in M').
\]
Faithfulness, semifiniteness and finiteness pass through the order isomorphism \(\theta^{-1}\) of the positive parts. By (7.1), \(Jp'_\xi J=p_{J\xi}\sim p_\xi\), so \(\tau^J(p'_\xi)=\tau(p_{J\xi})=\tau(p_\xi)\) (Fact 2.5(1)). For (2) the same computations apply, and for \(a\in Z_+\), \(T^J(ay')=T\bigl((JaJ)(Jy'J)\bigr)=T(a\,Jy'J)=aT^J(y')\), because \(JaJ=a^*=a\). Semifiniteness passes through \(\theta\), which is a \(\sigma\)-weak homeomorphism: \(\{y':T^J(y'^*y')\in Z_+\}=\theta(\{x:T(x^*x)\in Z_+\})\), by the trace identity. Finally \(T(v^*v)=T(vv^*)\) shows that \(T\) is constant on equivalence classes, so \(T^J(p'_\xi)=T(p_{J\xi})=T(p_\xi)\). \(\square\)

**Example 7.6** (The condition on the centre cannot be dropped). Let \(M=M_2(\mathbb C)\oplus\mathbb C1\) act on \(H=\mathbb C^2\oplus\mathbb C^2\); then \(M'=\mathbb C1\oplus M_2(\mathbb C)\). Let \(C_0\) be complex conjugation of coordinates on \(\mathbb C^2\) and \(J(u\oplus v)=C_0v\oplus C_0u\). Then \(J\) is conjugate-linear, satisfies (1) and (2) of Definition 7.1, and \(J(m\oplus\lambda1)J=\bar\lambda1\oplus C_0mC_0\), so \(JMJ=M'\). But \(J\) exchanges the central projections \(z=1\oplus0\) and \(1-z\), so (4) fails. The conclusions of this section fail too.

- *Proposition 7.4.* For \(\xi=\delta_1\oplus0\), \(p_\xi=[M'\xi]=\mathbb C\delta_1\oplus0\), a projection with central support \(z\); and \(J\xi=0\oplus\delta_1\) has \(p_{J\xi}=[M'J\xi]=0\oplus\mathbb C^2=1-z\). Projections with different central supports are not equivalent.
- *Theorem 7.8.* The normal state \(\varphi(m\oplus\lambda)=\tfrac12\mathrm{Tr}(m)\) is not a vector state. If \(\varphi=\omega_{u\oplus v}\), then \(m=0\), \(\lambda=1\) gives \(\|v\|^2=0\), and then \(\langle mu,u\rangle=\tfrac12\mathrm{Tr}(m)\) for all \(m\); for \(m\) the projection onto a line orthogonal to \(u\) the left side is \(0\) and the right side is \(\tfrac12\).
- *Proposition 7.7.* \(M\) is \(\sigma\)-finite, but a separating vector for \(M\) would give an injective linear map \(m\mapsto mu\) of \(M_2(\mathbb C)\) into \(\mathbb C^2\), which is impossible.
- *Theorem 7.10.* The isomorphism \(m\oplus\lambda\mapsto(m\otimes1)\oplus\lambda\) of \(M\) onto \(N=(M_2(\mathbb C)\otimes1)\oplus\mathbb C\), acting on \((\mathbb C^2\otimes\mathbb C^2)\oplus\mathbb C\), is not spatial, since the spaces have dimensions \(4\) and \(5\). Yet \(N\) has a unitary involution: that of Example 7.2(2) on the first summand, and complex conjugation on \(\mathbb C\).

\(M\) itself has no unitary involution at all: by Lemma 7.3(1) one would map \(Mz\cong M_2(\mathbb C)\) onto \(M'z\cong\mathbb C\).

**Proposition 7.7.** If \(M\) is \(\sigma\)-finite and has a unitary involution \(J\), then \(M\) has a vector that is cyclic and separating.

**Proof.** Proposition 5.1 gives a central projection \(z\) and \(\xi\in H\) with \(z\le p'_\xi\) and \(1-z\le p_\xi\). Put \(\xi_1=(1-z)\xi\) and \(\xi_2=z\xi\). By Lemma 3.3(1), \(p_{\xi_1}=1-z\) and \(p'_{\xi_2}=z\). As \(J\) commutes with \(z\), \(J\xi_1\in(1-z)H\) and \(J\xi_2\in zH\), and (7.1) gives \(p'_{J\xi_1}=Jp_{\xi_1}J=1-z\) and \(p_{J\xi_2}=Jp'_{\xi_2}J=z\). So on \((1-z)H\) the algebra \(M(1-z)\) has the separating vector \(\xi_1\) and the cyclic vector \(J\xi_1\), and on \(zH\) the algebra \(Mz\) has the cyclic vector \(\xi_2\) and the separating vector \(J\xi_2\). By Fact 2.3(4) there are \(\zeta_1\in(1-z)H\), cyclic and separating for \(M(1-z)\), and \(\zeta_2\in zH\), cyclic and separating for \(Mz\). For \(\zeta=\zeta_1+\zeta_2\), Lemma 3.3(1) gives \(p_\zeta=p_{\zeta_1}+p_{\zeta_2}=(1-z)+z=1\) and likewise \(p'_\zeta=1\). So \(\zeta\) is cyclic and separating. \(\square\)

**Theorem 7.8** (Normal functionals are vector functionals). Let \(\{M,H\}\) have a unitary involution \(J\).

1. Every positive normal functional on \(M\) is \(\omega_\xi|_M\) for some \(\xi\in H\).
2. Every normal functional on \(M\) is \(\omega_{\eta,\xi}|_M\) for some \(\eta,\xi\in H\).

**Proof.** (1) Let \(\varphi\in M_*^+\), \(e=s(\varphi)\) its support, and \(e'=JeJ\), a projection of \(M'\).

*Step 1: a smaller algebra with a unitary involution.* The projections \(e\in M\) and \(e'\in M'\) commute, and \(J(ee')J=(JeJ)(Je'J)=e'e=ee'\). So \(J\) maps \(K=ee'H\) onto itself. Let \(A\) be the algebra of the restrictions \(x|_K\), \(x\in eMe\). Reduce \(M\) by \(e\) and then induce by \(e'|_{eH}\), which lies in the commutant \(M'e\) of \(eMe\). By Fact 2.1(1), used twice, \(A\) is a von Neumann algebra on \(K\) whose commutant \(A'\) consists of the restrictions \(y'|_K\), \(y'\in e'M'e'\). For \(x\in eMe\), \(JxJ=J(exe)J=e'(JxJ)e'\in e'M'e'\); so \(J|_KAJ|_K\subseteq A'\), likewise \(J|_KA'J|_K\subseteq A\), and since \(J^2=1\), \(J|_KAJ|_K=A'\). The centre of \(A\) consists of the restrictions of the \(ae\), \(a\in Z\) (Fact 2.1(4), and the fact that an induction maps the centre onto the centre of the induced algebra, since both equal the centre of the commutant). As \(JaJ=a^*\), \(J|_K\) is a unitary involution of \(\{A,K\}\).

*Step 2: \(x\mapsto x|_K\) is an isomorphism of \(eMe\) onto \(A\).* This map is the induction of \(eMe\) by \(e'|_{eH}\), so by Fact 2.1(3) it is injective as soon as the central support of \(e'e\) in \(M'e\) is \(e\). The central projections of \(M'e\) are the \(we\) with \(w\) a central projection of \(M\) (the centre of \(M'e\) equals that of its commutant \(eMe\), which is \(Ze\)). Suppose \(we\cdot e'e=0\), that is, \((we)e'=0\). Lemma 3.3(6) gives \(c(we)c(e')=0\), that is, \(wc(e)c(e')=0\). Now \(c(e')=c(JeJ)=Jc(e)J=c(e)\): the map \(p\mapsto JpJ\) is an order isomorphism from the projections of \(M\) onto those of \(M'\) that fixes central projections (Lemma 7.3), so it maps the least central projection above \(e\) to the least central projection above \(JeJ\). Hence \(wc(e)=0\) and \(we=0\). So the central support of \(e'e\) is \(e\).

*Step 3.* \(\varphi\) is faithful on \(eMe\), so \(eMe\) is \(\sigma\)-finite (Fact 2.4(1)), and so is \(A\). By Proposition 7.7, \(A\) has a separating vector. The functional \(x|_K\mapsto\varphi(x)\) on \(A\) is positive and normal (Step 2 and Fact 2.4(3)), so by Fact 2.3(3) there is \(\xi\in K\) with \(\varphi(x)=\langle x\xi,\xi\rangle\) for all \(x\in eMe\). For \(x\in M\), the Cauchy–Schwarz inequality and \(\varphi(1-e)=0\) give \(\varphi(x)=\varphi(exe)\), and \(\langle exe\xi,\xi\rangle=\langle x\xi,\xi\rangle\) because \(e\xi=\xi\). So \(\varphi=\omega_\xi|_M\).

(2) First a comparison lemma: *if \(\omega_\xi\le\omega_\zeta\) on \(M_+\), then \(\xi=t'\zeta\) for some \(t'\in M'\) with \(\|t'\|\le1\).* Indeed, \(\|x\xi\|^2=\omega_\xi(x^*x)\le\omega_\zeta(x^*x)=\|x\zeta\|^2\), so \(x\zeta\mapsto x\xi\) is a well-defined contraction from \(M\zeta\) onto \(M\xi\). Extend it by continuity to \([M\zeta]\) and by \(0\) on \([M\zeta]^\perp\). The result \(t'\) commutes with every \(y\in M\): on \(M\zeta\), \(t'yx\zeta=yx\xi=yt'x\zeta\), and \([M\zeta]^\perp\) is invariant under \(M\), where both \(t'y\) and \(yt'\) vanish. So \(t'\in M'\), and \(t'\zeta=\xi\).

Now let \(\varphi\in M_*\). Since \(M_*\) is spanned by \(M_*^+\) (Fact 2.4(6)), \(\varphi=\sum_{k=1}^nc_k\varphi_k\) with \(\varphi_k\in M_*^+\) and \(c_k\in\mathbb C\). By (1), \(\psi=\sum_k\varphi_k=\omega_\zeta\) and \(\varphi_k=\omega_{\xi_k}\). As \(\varphi_k\le\psi\), the lemma gives \(t'_k\in M'\) with \(\xi_k=t'_k\zeta\). Then \(\varphi_k(x)=\langle xt'_k\zeta,t'_k\zeta\rangle=\langle x\,t'^*_kt'_k\zeta,\zeta\rangle\), and \(\varphi=\omega_{a'\zeta,\zeta}\) with \(a'=\sum_kc_kt'^*_kt'_k\in M'\). \(\square\)

The next lemma is the heart of the proof that isomorphisms are spatial. Recall that for \(q\in\mathcal P(M')\) the induced algebra is \(M_q\) on \(qH\), with commutant \(qM'q\) (Fact 2.1(1)).

**Lemma 7.9.** Let \(\{M,H\}\) have a unitary involution \(J\). Let \(q\in M'\) be a projection with \(c(q)=1\) such that \(\{M_q,qH\}\) has a unitary involution \(J_q\). Then \(q\sim1\) in \(M'\).

**Proof.** *Step 0.* The induction \(\iota(x)=x_q\) is an isomorphism of \(M\) onto \(M_q\), since its kernel is \(M(1-c(q))=\{0\}\). The centre of \(M_q\) is \(\iota(Z)\). Let \(\theta\) be the anti-isomorphism of Lemma 7.3 for \(J\), and \(\theta_q(y)=J_qy^*J_q\) the one for \(J_q\), from \(M_q\) onto \(qM'q\). Then \(\gamma=\theta_q\circ\iota\circ\theta^{-1}\) is an isomorphism of \(M'\) onto \(qM'q\), and for a central \(z\), \(\gamma(z)=\theta_q(\iota(z))=\iota(z)=zq\), because \(\theta\) and \(\theta_q\) fix central elements.

*Step 1: \(\sigma\)-finite central summands.* Let \(z\ne0\) be a central projection with \(Mz\) \(\sigma\)-finite. We show \(zq\sim z\) in \(M'\). \(J\) commutes with \(z\), so \(J|_{zH}\) is a unitary involution of \(Mz\), and Proposition 7.7 gives a vector that is cyclic and separating for \(Mz\). The algebra \(M_{zq}\) on \(zqH\) is isomorphic to \(Mz\) by \(x\mapsto x_{zq}\) (its kernel on \(Mz\) is \(Mz(z-c(zq))\), and \(c(zq)=zc(q)=z\)), so it is \(\sigma\)-finite; and \(J_q\) commutes with the central projection \(\iota(z)\) of \(M_q\), so its restriction to \(zqH\) is a unitary involution of \(M_{zq}\). So some vector is cyclic and separating for \(M_{zq}\) as well. By Fact 2.3(5) the isomorphism \(x\mapsto x_{zq}\) of \(Mz\) onto \(M_{zq}\) is spatial: there is a unitary \(U:zH\to zqH\) with \(Ux\eta=xU\eta\) for \(x\in M\) and \(\eta\in zH\). Let \(V\) be \(U\) on \(zH\) and \(0\) on \((1-z)H\). Then \(V\) commutes with \(M\), so \(V\in M'\), and \(V^*V=z\), \(VV^*=zq\).

*Step 2: no \(\sigma\)-finite central summand.* Suppose that no nonzero central projection \(w\) makes \(Mw\) \(\sigma\)-finite. We find a nonzero central \(z\) with \(zq\sim z\).

Pick a nonzero \(\xi\in qH\). Then \(p'_\xi\le q\) (Fact 2.3(1) for \(M'\)), and \(p'_\xi\) is \(\sigma\)-finite in \(M'\) (Lemma 3.3(5)).

(a) Apply Fact 2.2(8) in the algebra \(qM'q\), with unit \(q\), to the one-element family \(\{p'_\xi\}\). The central projection it produces has the form \(z_1q\) with \(z_1\) central in \(M\) (Fact 2.1(4)), and it comes with mutually orthogonal, mutually equivalent projections \(g_j\) (\(j\in J_0\)) in \(qM'q\), one of them \(z_1p'_\xi\), with \(z_1q-\sum_jg_j\prec g_j\). If \(J_0\) were finite, \(z_1q\) would be a finite sum of projections subequivalent to the \(\sigma\)-finite projection \(z_1p'_\xi\), hence \(\sigma\)-finite. Then \((qM'q)z_1q=\gamma(M'z_1)\) would be \(\sigma\)-finite, hence \(M'z_1\), hence \(Mz_1\) (Lemma 7.3(3)), against the hypothesis. So \(J_0\) is infinite, and by Fact 2.2(8) we may take the \(g_j\) mutually orthogonal with \(g_j\sim z_1p'_\xi\) and \(\sum_{j\in J_0}g_j=z_1q\).

(b) Apply Fact 2.2(8) in \(M'\) to the family \(\{g_j\}_{j\in J_0}\). It gives a nonzero central projection \(z_2\) and mutually orthogonal, mutually equivalent projections \(h_i\) (\(i\in I\)), with \(I\supseteq J_0\), \(h_j=z_2g_j\) for \(j\in J_0\), and \(z_2-\sum_ih_i\prec h_i\); in particular \(h_i\ne0\). The \(h_i\) and the remainder have central supports below \(c(g_j)\le z_1\), so \(z_2\le z_1\). As \(I\) is infinite, we may take the \(h_i\) mutually orthogonal with \(h_i\sim z_2p'_\xi\) and \(\sum_{i\in I}h_i=z_2\). Also \(z_2q=\sum_{j\in J_0}z_2g_j\), with \(z_2g_j\sim z_2p'_\xi\ne0\).

(c) *Counting.* \(|J_0|\le|I|\), since \(J_0\subseteq I\). For the reverse inequality, \(\gamma\) maps \(M'z_2\) isomorphically onto \(z_2qM'qz_2\), because \(\gamma(z_2)=z_2q\). So the \(\gamma(h_i)\), \(i\in I\), are mutually orthogonal nonzero projections of \(z_2qM'qz_2\). In that algebra the \(z_2g_j\), \(j\in J_0\), are mutually orthogonal \(\sigma\)-finite projections (each is equivalent to a subprojection of \(p'_\xi\)) with sum equal to its unit \(z_2q\), and \(J_0\) is infinite. Lemma 4.5 gives \(|I|\le|J_0|\). By the Cantor–Bernstein theorem, \(|I|=|J_0|\).

(d) Choose a bijection \(b:J_0\to I\). Then \(z_2g_j\sim h_{b(j)}\) for every \(j\), and additivity gives \(z_2q=\sum_jz_2g_j\sim\sum_jh_{b(j)}=z_2\). So \(z=z_2\) works.

*Step 3: exhaustion.* By Zorn's lemma choose a maximal family \(\{z_k\}\) of mutually orthogonal nonzero central projections with \(z_kq\sim z_k\). Suppose \(w=1-\sum_kz_k\ne0\). If some nonzero central \(z\le w\) makes \(Mz\) \(\sigma\)-finite, Step 1 contradicts maximality. Otherwise \(Mw\) on \(wH\), with \(J|_{wH}\), the projection \(wq\in M'w\) (whose central support is \(wc(q)=w\)), and \(J_q\) restricted to \(wqH\), satisfies the hypotheses of Step 2, which again contradicts maximality. So \(\sum_kz_k=1\), and additivity gives \(q=\sum_kz_kq\sim\sum_kz_k=1\). \(\square\)

**Theorem 7.10** (Isomorphisms are spatial). Suppose that \(\{M_1,H_1\}\) and \(\{M_2,H_2\}\) have unitary involutions \(J_1\) and \(J_2\). Every isomorphism \(\pi\) of \(M_1\) onto \(M_2\) is spatial.

**Proof.** \(\pi\) is normal (Fact 2.4(3)). Let \(P\), \(q_1\), \(q_2\) be the joint algebra and projections of the representations \(x\mapsto x\) and \(x\mapsto\pi(x)\) of \(M_1\) (Lemma 3.1). Both are faithful, so \(c(q_1)=c(q_2)=1\). By Lemma 3.1(3) it suffices to show \(q_1\sim q_2\) in \(P'\): a unitary \(U:H_1\to H_2\) with \(Ux=\pi(x)U\) gives \(\pi(x)=UxU^*\).

By the comparison theorem there is a central projection \(w\) of \(P'\) with \(wq_2\precsim wq_1\) and \((1-w)q_1\precsim(1-w)q_2\). We show \(wq_2\sim wq_1\); the other half is the same with the indices exchanged. Choose \(v\in P'\) with \(v^*v=wq_2\) and \(vv^*=r\le wq_1\).

Consider the induced algebra \(B=P_{wq_1}\) on \(wq_1K\), where \(K=H_1\oplus H_2\). By Lemma 3.1(2) it is the central summand \(M_1z_1\) of \(M_1\) on \(z_1H_1\), where \(z_1\) is the central projection of \(M_1\) with \(w=z_1\oplus\pi(z_1)\); so \(J_1\) restricted to \(z_1H_1\) is a unitary involution of \(B\). The commutant of \(B\) is \(wq_1P'wq_1\), and \(r\) is a projection there. Its central support in \(P'\) is \(c(r)=c(wq_2)=wc(q_2)=w\) (Fact 2.1(2)), so its central support in the corner \(wq_1P'wq_1\), whose centre is the centre of \(P'\) cut by \(wq_1\), is \(wq_1\), the unit. The induced algebra \(B_r\), on \(rK\), is the restriction of \(P\) to \(rK\). The operator \(v\) maps \(wq_2K\) unitarily onto \(rK\) and commutes with \(P\), so it carries the restriction of \(P\) to \(wq_2K\), which is \(M_2\pi(z_1)\) with the unitary involution given by \(J_2\), onto \(B_r\); so \(B_r\) has a unitary involution too. Lemma 7.9, applied to \(B\) and \(r\), gives \(r\sim wq_1\). Hence \(wq_2\sim r\sim wq_1\). \(\square\)

**Corollary 7.11.**

1. If \(M\) has a unitary involution, every automorphism of \(M\) is implemented by a unitary on \(H\).
2. Let \(M\) be semifinite with a unitary involution, and let \(\tau\) be a faithful normal semifinite trace on \(M\). Then there is a unitary \(W:H\to L^2(M,\tau)\) with \(WxW^*=L_x\) for \(x\in M\). So an algebra with a unitary involution is a copy of the Hilbert space of its trace.

**Proof.** (1) is Theorem 7.10 with \(M_1=M_2=M\). (2) is Theorem 7.10 applied to \(\pi_\tau:M\to\pi_\tau(M)\) and Example 7.2(1). \(\square\)

**Remark 7.12.** By Tomita–Takesaki theory, if a vector is cyclic and separating for \(M\), its modular conjugation is a unitary involution [Kostecki, Sections 3.2–3.3]. With Proposition 7.7, a \(\sigma\)-finite algebra has a unitary involution exactly when some vector is cyclic and separating for it. A *standard form* in the sense of [Haagerup 1975] is a unitary involution together with a self-polar cone of vectors, each fixed by \(J\), that is mapped into itself by every \(xJxJ\) with \(x\in M\); see [Kostecki, Section 3.3]. Theorems 7.8 and 7.10 show that the vector-state property and the spatiality of isomorphisms already follow from the involution alone, without the cone.

## 8. The Hilbert space of an amplified trace, and corners

This section shows that every semifinite algebra, acting on any Hilbert space, is a two-sided corner of the Hilbert space of a trace. The traces of Section 9 and the coupling function of Section 10 are built on this.

We use the conjugate Hilbert space \(\bar K\) of a Hilbert space \(K\): its elements are symbols \(\bar\eta\) (\(\eta\in K\)), with \(\bar\eta+\bar\eta'=\overline{\eta+\eta'}\), \(\lambda\bar\eta=\overline{\bar\lambda\eta}\) and \(\langle\bar\eta,\bar\eta'\rangle=\langle\eta',\eta\rangle\). For \(\zeta,\eta\in K\), \(t_{\zeta,\eta}\) is the rank-one operator \(\theta\mapsto\langle\theta,\eta\rangle\zeta\). Then \(t_{\zeta,\eta}^*=t_{\eta,\zeta}\), \(bt_{\zeta,\eta}=t_{b\zeta,\eta}\) for \(b\in B(K)\), \(t_{\eta',\zeta'}t_{\zeta,\eta}=\langle\zeta,\zeta'\rangle t_{\eta',\eta}\), and \(\mathrm{Tr}(t_{\eta',\eta})=\langle\eta',\eta\rangle\).

**Proposition 8.1** (The Hilbert space of an amplified trace). Let \(\tau\) be a faithful normal semifinite trace on \(M\), \(K\) a Hilbert space, \(N=M\bar\otimes B(K)\), and \(\sigma\) the trace \(\sigma(x)=\sum_i\tau(x_{ii})\) of Fact 2.5(7), which is faithful, normal and semifinite. There is a unitary
\[
U:L^2(N,\sigma)\to L^2(M,\tau)\otimes K\otimes\bar K,\qquad U\Lambda_\sigma(a\otimes t_{\zeta,\eta})=\Lambda_\tau(a)\otimes\zeta\otimes\bar\eta\quad(a\in\mathfrak n_\tau,\ \zeta,\eta\in K),
\tag{8.1}
\]
such that \(UL_{x\otimes b}U^*=L_x\otimes b\otimes1\) for \(x\in M\), \(b\in B(K)\), and \(UJ_\sigma U^*=J_\tau\otimes\Phi\), where \(\Phi\) is the conjugate-linear map with \(\Phi(\zeta\otimes\bar\eta)=\eta\otimes\bar\zeta\). Consequently
\[
\{\pi_\sigma(N),L^2(N,\sigma)\}\cong\{\pi_\tau(M)\bar\otimes B(K)\otimes1,\ L^2(M,\tau)\otimes K\otimes\bar K\}.
\]

One may read \(K\otimes\bar K\) as the space of Hilbert–Schmidt operators on \(K\), with \(\zeta\otimes\bar\eta\) standing for \(t_{\zeta,\eta}\). Then (8.1) says that \(L^2(M\bar\otimes B(K))\) consists of the Hilbert–Schmidt "matrices" with entries in \(L^2(M)\), that \(N\) acts by left multiplication, and that \(J_\sigma\) takes adjoints.

**Proof.** *The trace of a product.* For \(y\in M_+\) and a finite-rank positive \(s\in B(K)\), the matrix entries of \(y\otimes s\) are \(\langle s\varepsilon_j,\varepsilon_i\rangle y\), so \(\sigma(y\otimes s)=\tau(y)\sum_i\langle s\varepsilon_i,\varepsilon_i\rangle=\tau(y)\mathrm{Tr}(s)\). The trace \(\sigma\) extends linearly to the span of its positive elements of finite trace (Traces on von Neumann algebras, Lemma 2.4), so \(\sigma(y\otimes s)=\tau(y)\mathrm{Tr}(s)\) also for \(y\) in the span of the positive elements of finite \(\tau\)-trace and \(s\) of finite rank. In particular \(a\otimes t_{\zeta,\eta}\in\mathfrak n_\sigma\) for \(a\in\mathfrak n_\tau\).

*Inner products.* For \(a,a'\in\mathfrak n_\tau\),
\[
\bigl\langle\Lambda_\sigma(a\otimes t_{\zeta,\eta}),\Lambda_\sigma(a'\otimes t_{\zeta',\eta'})\bigr\rangle=\sigma\bigl(a'^*a\otimes t_{\eta',\zeta'}t_{\zeta,\eta}\bigr)=\langle\zeta,\zeta'\rangle\langle\eta',\eta\rangle\tau(a'^*a),
\]
which is \(\langle\Lambda_\tau(a)\otimes\zeta\otimes\bar\eta,\Lambda_\tau(a')\otimes\zeta'\otimes\bar\eta'\rangle\). A map defined on a spanning set that preserves inner products extends to a well-defined linear isometry of the span. So (8.1) defines an isometry \(U\) on the span \(D\) of the vectors \(\Lambda_\sigma(a\otimes t_{\zeta,\eta})\).

*Density.* Fix an orthonormal basis \((\varepsilon_i)\) of \(K\) and write \(e_{ij}=t_{\varepsilon_i,\varepsilon_j}\). For \(x\in\mathfrak n_\sigma\) with entries \(x_{ij}\), \((x^*x)_{jj}=\sum_ix_{ij}^*x_{ij}\) strongly, so normality of \(\tau\) gives \(\sigma(x^*x)=\sum_{i,j}\tau(x_{ij}^*x_{ij})<\infty\). In particular every \(x_{ij}\) lies in \(\mathfrak n_\tau\). For a finite set \(F\) of indices let \(x_F=\sum_{i,j\in F}x_{ij}\otimes e_{ij}\); then \(\Lambda_\sigma(x_F)\in D\). The entries of \(x-x_F\) are \(x_{ij}\) for \((i,j)\notin F\times F\) and \(0\) otherwise, so \(\|\Lambda_\sigma(x)-\Lambda_\sigma(x_F)\|^2=\sum_{(i,j)\notin F\times F}\tau(x_{ij}^*x_{ij})\to0\). So \(D\) is dense in \(L^2(N,\sigma)\). The vectors \(\Lambda_\tau(a)\otimes\zeta\otimes\bar\eta\) span a dense subspace of the target. Hence \(U\) extends to a unitary.

*Operators.* \((x\otimes b)(a\otimes t_{\zeta,\eta})=xa\otimes t_{b\zeta,\eta}\), and \(U\) maps it to \(\Lambda_\tau(xa)\otimes b\zeta\otimes\bar\eta=(L_x\otimes b\otimes1)(\Lambda_\tau(a)\otimes\zeta\otimes\bar\eta)\). Also \(J_\sigma\Lambda_\sigma(a\otimes t_{\zeta,\eta})=\Lambda_\sigma(a^*\otimes t_{\eta,\zeta})\), which \(U\) maps to \(J_\tau\Lambda_\tau(a)\otimes\eta\otimes\bar\zeta\). By continuity the two identities hold everywhere. Finally, \(N\) is generated as a von Neumann algebra by \(M\otimes1\) and \(1\otimes B(K)\) (Fact 2.2(7)), and \(\pi_\sigma\) is normal; so \(U\pi_\sigma(N)U^*\) is the von Neumann algebra generated by \(L_x\otimes1\otimes1\) and \(1\otimes b\otimes1\), which is \(\pi_\tau(M)\bar\otimes B(K)\otimes1\). \(\square\)

**Theorem 8.2** (Semifinite algebras are corners of a trace space). Let \(M\), acting on \(H\ne0\), be semifinite. We can find the following data: a von Neumann algebra \(N\) carrying a faithful normal semifinite trace \(\sigma\), projections \(e,f\in N\) with \(c(e)=c(f)=1\), and a unitary \(W\) from \(H\) onto
\[
K=L_eR_f\,L^2(N,\sigma)
\]
with the following properties.

1. For \(x\in M\) there is a unique \(\alpha(x)\in eNe\) with \(WxW^*=L_{\alpha(x)}|_K\), and \(\alpha\) is an isomorphism of \(M\) onto \(eNe\).
2. For \(y'\in M'\) there is a unique \(\beta(y')\in fNf\) with \(Wy'W^*=R_{\beta(y')}|_K\), and \(\beta\) is an anti-isomorphism (a linear bijection with \(\beta(y'z')=\beta(z')\beta(y')\) and \(\beta(y'^*)=\beta(y')^*\)) of \(M'\) onto \(fNf\).
3. There is an isomorphism \(\kappa\) of \(Z\) onto the centre of \(N\) with \(\alpha(z)=\kappa(z)e\) and \(\beta(z)=\kappa(z)f\) for \(z\in Z\).

One can take \(N=M\bar\otimes B(\bar R)\) for a Hilbert space \(R\), with \(\sigma=\tau_0\otimes\mathrm{Tr}\) for any faithful normal semifinite trace \(\tau_0\) of \(M\) and \(e=1\otimes q\) for a rank-one projection \(q\). In words: \(\{M,H\}\) is spatially isomorphic to the algebra \(\pi_\sigma(N)\), reduced by the projection \(L_e\in\pi_\sigma(N)\) and then induced by the projection \(R_f\) of its commutant; and \(\pi_\sigma(N)\) has the unitary involution \(J_\sigma\).

**Proof.** *Step 1: an isometry into an amplified trace space.* Let \(\tau_0\) be a faithful normal semifinite trace on \(M\) (Fact 2.5(8)), \(L=L^2(M,\tau_0)\) and \(\pi_0=\pi_{\tau_0}\). The map \(\pi_0(x)\mapsto x\) is a normal isomorphism of \(\pi_0(M)\) onto \(M\) (Fact 2.4(3)). Fact 2.7 gives a Hilbert space \(R\) and an isometry \(V:H\to L\otimes R\) such that \(VV^*\) commutes with \(\pi_0(M)\otimes1\) and \(x=V^*(\pi_0(x)\otimes1)V\). Then \(Vx=VV^*(\pi_0(x)\otimes1)V=(\pi_0(x)\otimes1)V\).

*Step 2: the trace space of \(N\).* Let \(N=M\bar\otimes B(\bar R)\), \(\sigma\) the amplified trace (Fact 2.5(7)), \(\theta_0\) a unit vector of \(\bar R\), \(q=t_{\theta_0,\theta_0}\), and \(e=1\otimes q\). The centre of \(N\) is \(Z\otimes1\) (Fact 2.2(7)), and \((z\otimes1)e=z\otimes q=0\) only if \(z=0\); so \(c(e)=1\). The corner \(eNe\) consists of the elements \(a\otimes q\), \(a\in M\): in matrix form relative to a basis containing \(\theta_0\), \(e\) keeps only the diagonal entry at \(\theta_0\). By Proposition 8.1 (with \(K=\bar R\), so \(\bar K=R\)), \(L_e\) corresponds to \(1\otimes q\otimes1\), whose range is \(L\otimes\mathbb C\theta_0\otimes R\cong L\otimes R\). So there is a unitary \(\Psi:L\otimes R\to eL^2(N,\sigma)\) with \(\Psi(\pi_0(a)\otimes1)=L_{a\otimes q}\Psi\) for \(a\in M\).

*Step 3: the projection \(f\).* Put \(\alpha(x)=x\otimes q\) and \(W_0=\Psi V:H\to eL^2(N,\sigma)\). Then \(W_0\) is an isometry with \(W_0x=L_{\alpha(x)}W_0\), and taking adjoints, \(xW_0^*=W_0^*L_{\alpha(x)}\). Hence \(W_0W_0^*\) commutes with the algebra \(A=\{L_a|_{eL^2}:a\in eNe\}\). This is the reduced algebra of \(\pi_\sigma(N)\) by \(L_e\), so by Fact 2.1(1) and Fact 2.6 its commutant is \(\{R_y|_{eL^2}:y\in N\}\). The map \(y\mapsto R_y|_{eL^2}\) is injective: it is the induction of \(\pi_\sigma(N)'=\{R_y\}\) by the projection \(L_e\) of \(\pi_\sigma(N)\), whose kernel is determined by the central support of \(L_e\) in \(\pi_\sigma(N)\), which is \(L_{c(e)}=1\) (Fact 2.1(3)). It reverses products and commutes with adjoints (Fact 2.6). So \(W_0W_0^*=R_f|_{eL^2}\) for a unique \(f\in N\), and \(f\) is a projection, since \(R_{f^*}=R_f^*=R_f\) and \(R_{f^2}=R_f^2=R_f\).

Put \(K=W_0H=R_f\,eL^2(N,\sigma)=L_eR_fL^2(N,\sigma)\) (the projections \(L_e\) and \(R_f\) commute), and let \(W:H\to K\) be \(W_0\) with this range.

*Step 4: properties.* (1) \(\alpha(x)=x\otimes q\) is a \(*\)-homomorphism of \(M\) onto \(eNe\), and \(WxW^*=L_{\alpha(x)}|_K\). If \(a\in eNe\) and \(L_a|_K=0\), write \(a=\alpha(x)\); then \(WxW^*=0\), so \(x=0\) and \(a=0\). Hence \(a\mapsto L_a|_K\) is injective on \(eNe\), the element \(\alpha(x)\) is unique, and \(\alpha\) is injective.

(2) The algebra \(WMW^*\) is the induced algebra of \(A\) by \(R_f|_{eL^2}\in A'\). By Fact 2.1(1) its commutant on \(K\), which is \(WM'W^*\), is the reduced algebra of \(A'\) by \(R_f\), namely \(\{R_fR_yR_f|_K\}=\{R_{fyf}|_K:y\in N\}\). The map \(y\mapsto R_y|_K\) is injective on \(fNf\): if \(y=fyf\) and \(R_y|_K=0\), then \(R_yL_eR_f=0\), and \(R_y=R_fR_yR_f\) gives \(R_yL_e=R_f(R_yL_eR_f)=0\), so \(y=0\) by Step 3. So \(\beta\) is well defined and bijective, and it reverses products and commutes with adjoints because \(y\mapsto R_y\) does.

(3) Let \(\kappa(z)=z\otimes1\). Then \(\alpha(z)=z\otimes q=\kappa(z)e\). For central \(z\), \(WzW^*=L_{\kappa(z)e}|_K=L_{\kappa(z)}|_K\), and \(L_{\kappa(z)}=R_{\kappa(z)}\) because \(\kappa(z)\) is central in \(N\). So \(WzW^*=R_{\kappa(z)f}|_K\), that is, \(\beta(z)=\kappa(z)f\).

*\(c(f)=1\).* Let \(z\in Z\) with \(\kappa(z)f=0\). Then \(L_{\alpha(z)}W_0W_0^*=L_{\kappa(z)}R_f|_{eL^2}=R_{f\kappa(z)}|_{eL^2}=0\), so \(W_0zW_0^*=0\), and \(z=0\). As the central projections of \(N\) are the \(\kappa(z)\), \(c(f)=1\). \(\square\)

## 9. Transfer of traces to the commutant

A trace on \(M\) measures the cyclic projections \(p_\xi\). This section shows that there is exactly one trace on \(M'\) that gives each \(p'_\xi\) the same size. We first show that traces are determined by their values on cyclic projections.

**Lemma 9.1.** Let \(\rho_1\) and \(\rho_2\) be normal traces on \(M'\) with \(\rho_1(p'_\xi)=\rho_2(p'_\xi)\) for every \(\xi\in H\). Then \(\rho_1=\rho_2\). The same holds for \(M\) and the \(p_\xi\).

**Proof.** By Lemma 3.3(4), applied to \(M'\), every projection \(e'\) of \(M'\) is \(\sum_ip'_{\xi_i}\) with mutually orthogonal terms. The finite partial sums increase to \(e'\), so normality and additivity give \(\rho_k(e')=\sum_i\rho_k(p'_{\xi_i})\); hence \(\rho_1=\rho_2\) on projections. For \(y\in M'_+\) let \(f_n(t)=2^{-n}\min(\lfloor2^nt\rfloor,n2^n)\) for \(t\ge0\). Then \(y_n=f_n(y)=2^{-n}\sum_{k=1}^{n2^n}\chi_{[k2^{-n},\infty)}(y)\) is a positive combination of spectral projections of \(y\), which lie in \(M'\). The \(f_n\) increase and converge to \(t\) uniformly on \([0,\|y\|]\), so \(y_n\uparrow y\). Normality gives \(\rho_1(y)=\lim\rho_1(y_n)=\lim\rho_2(y_n)=\rho_2(y)\). \(\square\)

**Lemma 9.2.** In the setting of Theorem 8.2, \(\alpha(p_\xi)\sim\beta(p'_\xi)\) in \(N\) for every \(\xi\in H\).

**Proof.** Put \(\zeta=W\xi\in K\). In the von Neumann algebra \(\pi_\sigma(N)\) on \(L^2(N,\sigma)\), whose commutant is \(\{R_y:y\in N\}\) (Fact 2.6), let \(P_\zeta\) be the projection onto the closed span of \(\{R_y\zeta:y\in N\}\) and \(P'_\zeta\) the projection onto the closed span of \(\{L_y\zeta:y\in N\}\); these are the cyclic projections of \(\pi_\sigma(N)\) and of its commutant at \(\zeta\). Write \(P_\zeta=L_g\) and \(P'_\zeta=R_{g'}\) with projections \(g,g'\in N\). As \(L_e\zeta=\zeta\) and \(L_e\in\pi_\sigma(N)\), \(g\le e\) (Fact 2.3(1)); likewise \(g'\le f\).

*\(\alpha(p_\xi)=g\).* \(Wp_\xi W^*\) is the projection onto \(W[M'\xi]=[WM'W^*\zeta]\), the closure of \(\{R_{fyf}\zeta:y\in N\}\). Since \(R_f\zeta=\zeta\), \(R_{fyf}\zeta=R_fR_yR_f\zeta=R_fR_y\zeta\). The projection \(R_f\) commutes with \(P_\zeta\), so this closure is \(R_fP_\zeta L^2(N,\sigma)=L_gR_fL^2(N,\sigma)\), a subspace of \(K\) because \(g\le e\). So \(Wp_\xi W^*=L_g|_K\), and \(\alpha(p_\xi)=g\).

*\(\beta(p'_\xi)=g'\).* In the same way, \(Wp'_\xi W^*\) projects onto the closure of \(\{L_{eye}\zeta:y\in N\}=\{L_eL_y\zeta\}\), which is \(L_eP'_\zeta L^2(N,\sigma)=R_{g'}L_eL^2(N,\sigma)\subseteq K\). So \(\beta(p'_\xi)=g'\).

*\(g\sim g'\).* \(J_\sigma\) is a unitary involution of \(\pi_\sigma(N)\) (Example 7.2(1)). By (7.1), \(P_\zeta\sim P_{J_\sigma\zeta}=J_\sigma P'_\zeta J_\sigma\) in \(\pi_\sigma(N)\). Since \(J_\sigma L_aJ_\sigma=R_{a^*}\), also \(J_\sigma R_bJ_\sigma=L_{b^*}\), so \(J_\sigma R_{g'}J_\sigma=L_{g'}\). Hence \(L_g\sim L_{g'}\) in \(\pi_\sigma(N)\), and \(g\sim g'\) in \(N\), because \(\pi_\sigma\) is an isomorphism onto \(\pi_\sigma(N)\). \(\square\)

**Theorem 9.3** (Transfer of traces). Let \(M\) be any von Neumann algebra on \(H\). For every normal trace \(\tau\) on \(M\) there is exactly one normal trace \(\tau'\) on \(M'\) with
\[
\tau'(p'_\xi)=\tau(p_\xi)\qquad(\xi\in H).
\tag{9.1}
\]
Moreover:

1. \(\tau''=\tau\), so \(\tau\mapsto\tau'\) is a bijection from the normal traces on \(M\) onto those on \(M'\).
2. \((\tau_1+\tau_2)'=\tau_1'+\tau_2'\), \((\lambda\tau)'=\lambda\tau'\) for \(\lambda\ge0\), and \((\tau_a)'=(\tau')_a\) for \(a\in Z_+\).
3. \(s(\tau')=s(\tau)\), and \(\tau\) and \(\tau'\) have the same semifinite part. In particular \(\tau'\) is faithful, or semifinite, exactly when \(\tau\) is.
4. If \(\{M,H\}\) has a unitary involution \(J\), then \(\tau'=\tau^J\).

**Proof.** *Uniqueness* is Lemma 9.1.

*Existence when \(\tau\) is faithful and semifinite.* Then \(M\) is semifinite (Fact 2.5(8)), and we use Theorem 8.2. The trace \(\tau\circ\alpha^{-1}\) on \(eNe\) is faithful, normal and semifinite, because \(\alpha\) is an isomorphism, which preserves order and suprema. As \(c(e)=1\), Fact 2.5(6) extends it to a faithful normal semifinite trace \(\hat\sigma\) on \(N\). Put \(\tau'(y')=\hat\sigma(\beta(y'))\) for \(y'\in M'_+\). Since \(\beta\) is an anti-isomorphism, it maps \(M'_+\) onto \((fNf)_+\), preserves sums and suprema, and satisfies \(\beta(w^*w)=\beta(w)\beta(w)^*\) and \(\beta(ww^*)=\beta(w)^*\beta(w)\). Hence \(\tau'\) is a normal trace. It is faithful because \(\hat\sigma\) is. It is semifinite: a nonzero \(b\in(fNf)_+\) majorizes a nonzero \(y\ge0\) with \(\hat\sigma(y)<\infty\), and \(y=fyf\) because \(0\le y\le\|b\|f\). By Lemma 9.2, \(\tau'(p'_\xi)=\hat\sigma(\beta(p'_\xi))=\hat\sigma(\alpha(p_\xi))=\tau(p_\xi)\).

*Existence in general.* Let \(s=s(\tau)\) and let \(z\) be the semifinite part of \(\tau\) (Fact 2.5(2)). The projection \((1-z)(1-s)\) has trace \(0\) and lies in \(M_+(1-z)\), where \(\tau\) is infinite on nonzero elements; so \((1-z)(1-s)=0\), that is, \(1-z\le s\). Put \(w_1=zs\), \(w_2=1-z\) and \(w_3=z(1-s)\), orthogonal central projections with sum \(1\).

The restriction of \(\tau\) to \(Mw_1\), acting on \(w_1H\) with commutant \(M'w_1\), is faithful and semifinite. For \(\eta\in w_1H\) the cyclic projections of \(Mw_1\) are \(p_\eta\) and \(p'_\eta\). The case already treated gives a normal trace \(\rho_1\) on \(M'w_1\) with \(\rho_1(p'_\eta)=\tau(p_\eta)\) for \(\eta\in w_1H\). Define \(\rho_2\) on \(M'_+\) by \(\rho_2(y')=0\) if \(y'w_2=0\) and \(\rho_2(y')=\infty\) otherwise. It is a normal trace: \((y'_1+y'_2)w_2=0\) exactly when both \(y'_kw_2=0\); \(y'^*y'w_2=(y'w_2)^*(y'w_2)\) vanishes exactly when \(y'w_2\) does, and so does \(y'y'^*w_2\); and if \(y'_i\uparrow y'\) with \(y'w_2\ne0\), then some \(y'_iw_2\ne0\). Put
\[
\tau'(y')=\rho_1(y'w_1)+\rho_2(y').
\]
This is a normal trace on \(M'\). Let \(\xi\in H\). As \(\tau\) vanishes on \(M_+w_3\) and \(p_\xi w=p_{w\xi}\) for central \(w\), \(\tau(p_\xi)=\tau(p_{w_1\xi})+\tau(p_{w_2\xi})\). Here \(\tau(p_{w_2\xi})\) is \(\infty\) if \(w_2\xi\ne0\) and \(0\) otherwise, which is \(\rho_2(p'_\xi)\), since \(p'_\xi w_2=p'_{w_2\xi}\) vanishes exactly when \(w_2\xi=0\). And \(\tau(p_{w_1\xi})=\rho_1(p'_{w_1\xi})=\rho_1(p'_\xi w_1)\). This proves (9.1).

(1) \(\tau''\) is a normal trace on \(M''=M\). The cyclic projections of \(M'\) at \(\xi\) are \(p'_\xi\), and those of its commutant \(M\) are \(p_\xi\). So \(\tau''(p_\xi)=\tau'(p'_\xi)=\tau(p_\xi)\), and \(\tau''=\tau\) by Lemma 9.1.

(2) Both sides of each identity are normal traces on \(M'\), so by Lemma 9.1 it suffices to compare them at the \(p'_\xi\). For sums and scalars this is (9.1). For \(a=\sum_k\lambda_kw_k\) with \(\lambda_k\ge0\) and orthogonal central projections \(w_k\), \(\tau(ap_\xi)=\sum_k\lambda_k\tau(p_{w_k\xi})=\sum_k\lambda_k\tau'(p'_{w_k\xi})=\tau'(ap'_\xi)\). A general \(a\in Z_+\) is the norm limit of the increasing sequence \(f_n(a)\) of such elements (Lemma 9.1), and \(f_n(a)p_\xi\uparrow ap_\xi\), \(f_n(a)p'_\xi\uparrow ap'_\xi\); normality gives \(\tau(ap_\xi)=\tau'(ap'_\xi)\).

(3) In the construction, \(\rho_1\) is faithful and semifinite on \(M'w_1\), \(\tau'\) is infinite on the nonzero elements of \(M'_+w_2\), and \(\tau'\) vanishes on \(M'_+w_3\). So \(s(\tau')=w_1+w_2=s\) (note \(s=zs+(1-z)\)) and the semifinite part of \(\tau'\) is \(w_1+w_3=z\), by the uniqueness in Fact 2.5(2).

(4) \(\tau^J\) is a normal trace on \(M'\) with \(\tau^J(p'_\xi)=\tau(p_\xi)\) (Corollary 7.5), so \(\tau^J=\tau'\). \(\square\)

**Corollary 9.4** (The types of \(M\) and \(M'\)). \(M\) and \(M'\) have the same central projections \(z_{\rm I}\), \(z_{\rm II}\) and \(z_{\rm III}\) cutting out their parts of types I, II and III. In particular \(M\) is semifinite if and only if \(M'\) is, and \(M\) is of type I, II or III if and only if \(M'\) is.

**Proof.** Let \(w=1-z_{\rm III}(M')\), so that \(M'w\) is semifinite. It has a faithful normal semifinite trace (Fact 2.5(8)). Theorem 9.3, applied to the algebra \(M'w\) on \(wH\), whose commutant is \(Mw\), gives a faithful normal semifinite trace on \(Mw\), so \(Mw\) is semifinite. A central summand that is both semifinite and of type III is \(0\), so \(wz_{\rm III}(M)=0\), that is, \(z_{\rm III}(M)\le z_{\rm III}(M')\). Exchanging \(M\) and \(M'\) gives equality. Next, \(Mz_{\rm I}(M)\) is of type I, so its commutant \(M'z_{\rm I}(M)\) is of type I (Fact 2.3(6)), and \(z_{\rm I}(M)\le z_{\rm I}(M')\); by symmetry they are equal. Then \(z_{\rm II}=1-z_{\rm I}-z_{\rm III}\) agrees too. \(\square\)

**Corollary 9.5** (Algebras of type III). Let \(M\) be of type III with \(\sigma\)-finite centre. Then \(M\) has a faithful normal representation with \(\sigma\)-finite commutant, and any two such representations are unitarily equivalent.

**Proof.** Existence is Theorem 4.3(1). If \(\pi\) is a faithful normal representation, \(\pi(M)\cong M\) is of type III, so \(\pi(M)'\) is of type III by Corollary 9.4. An algebra of type III has no nonzero finite projection, so every nonzero central projection of \(\pi(M)'\) is infinite: \(\pi(M)'\) is properly infinite. Theorem 4.1 gives uniqueness. \(\square\)

**Corollary 9.6.** If \(M\) is finite and has a cyclic vector, then \(M'\) is finite.

**Proof.** A cyclic vector \(\xi\) is separating for \(M'\supseteq Z\), so \(Z\) is \(\sigma\)-finite, and \(M\) has a faithful normal finite trace \(\tau\) (Fact 2.5(5)). By Theorem 9.3, \(\tau'\) is faithful and \(\tau'(1)=\tau'(p'_\xi)=\tau(p_\xi)\le\tau(1)<\infty\). A faithful finite trace separates \(M'_+\), so \(M'\) is finite (Fact 2.5(3)). \(\square\)

**Example 9.7** (Scalars). Let \(M=\mathbb C1\) on \(H\ne0\), so \(M'=B(H)\). The normal traces on \(M\) are \(\tau_t(\lambda1)=t\lambda\) with \(t\in[0,\infty]\). For \(\xi\ne0\), \(p_\xi=1\) and \(p'_\xi\) is the projection onto \(\mathbb C\xi\). So \(\tau_t'\) takes the value \(t\) at every rank-one projection, and \(\tau_t'=t\,\mathrm{Tr}\) by Lemma 9.1. For \(t=1\) the trace \(\tau_1\) is finite, while \(\tau_1'=\mathrm{Tr}\) is finite only if \(\dim H<\infty\): a finite trace can have an infinite partner. For \(t=\infty\), both \(\tau\) and \(\tau'\) are faithful and take only the values \(0\) and \(\infty\).

## 10. The coupling function

Theorem 9.3 compares scalar traces on \(M\) and \(M'\). Centre-valued traces carry more information, and comparing them gives a central function, the coupling function. We use the spectrum \(\Omega\) of \(Z\) and the extended positive part \(\widehat Z_+\) of Facts 2.8 and 2.9.

*Products with an invertible central function.* For \(c\in\widehat Z_+\) let \(G_c=\{\omega\in\Omega:0<c(\omega)<\infty\}\). This set is open, and it is dense exactly when \(c\) is finite and nonzero outside a rare set. For such \(c\) and for \(f,g\in\widehat Z_+\) we write
\[
f=cg\quad\text{if}\quad f(\omega)=c(\omega)g(\omega)\ \text{ for every }\omega\in G_c,
\tag{10.1}
\]
with \(t\cdot\infty=\infty\) for \(t>0\). Both sides are continuous on \(G_c\), so it suffices that the equality holds on a dense subset of \(G_c\); in this sense the relation of Fact 2.9 reads \(T_1(x)=dT_2(x)\). Since \(G_c\) is dense and \(f,g\) are continuous, each of \(f\) and \(g\) determines the other. The reciprocal \(1/c\), with \(1/0=\infty\) and \(1/\infty=0\), again lies in \(\widehat Z_+\), and \(G_{1/c}=G_c\). A central projection \(z\) corresponds to an open and closed set \(\Omega_z\) (Fact 2.8), and \(zf\) equals \(f\) on \(\Omega_z\) and \(0\) elsewhere.

**Lemma 10.1** (Transport and corners of extended centre-valued traces).

1. Let \(\alpha:A\to B\) be an isomorphism or an anti-isomorphism of von Neumann algebras. It maps the centre of \(A\) onto the centre of \(B\), and so induces a bijection \(\alpha_*\) of the extended positive parts that extends \(\alpha\) and respects sums, products with finite elements and least upper bounds. If \(T\) is a faithful normal semifinite extended centre-valued trace on \(A\), then \(\alpha_*\circ T\circ\alpha^{-1}\) is one on \(B\).
2. Let \(S\) be a faithful normal semifinite extended centre-valued trace on a von Neumann algebra \(N\), and \(e\in\mathcal P(N)\) with \(c(e)=1\). Identify the centre \(Z_Ne\) of \(eNe\) with the centre \(Z_N\) of \(N\) (Fact 2.1(4)). Then the restriction of \(S\) to \((eNe)_+\) is a faithful normal semifinite extended centre-valued trace on \(eNe\).

**Proof.** (1) An isomorphism or anti-isomorphism maps the centre onto the centre, and on the commutative centre it is an isomorphism. By the Gelfand theorem it is composition with a homeomorphism of the spectra, and composition with the same homeomorphism defines \(\alpha_*\) on continuous \([0,\infty]\)-valued functions. It respects pointwise sums and products, and it is an order isomorphism, so it also respects least upper bounds. For an anti-isomorphism, \(\alpha(w^*w)=\alpha(w)\alpha(w)^*\) and \(\alpha(ww^*)=\alpha(w)^*\alpha(w)\), so the identity \(T(x^*x)=T(xx^*)\) is carried over in both cases. Additivity, the identity \(T(ax)=aT(x)\) for central \(a\ge0\), normality and faithfulness transfer directly, since \(\alpha\) preserves order and suprema. For semifiniteness, the trace identity shows that \(\alpha\) maps \(\{x:T(x^*x)\in Z_{A,+}\}\) onto the corresponding set for the new trace. A linear bijection that preserves order and suprema in both directions is a homeomorphism for the \(\sigma\)-weak topologies (Fact 2.4(6)), so density is preserved.

(2) The set \(\mathfrak n=\{x\in N:S(x^*x)\in Z_{N,+}\}\) is a two-sided ideal: \((x+y)^*(x+y)\le2x^*x+2y^*y\) gives closure under sums, \(S((ax)^*(ax))\le\|a\|^2S(x^*x)\), and \(S((xa)^*(xa))=S(xaa^*x^*)\le\|a\|^2S(xx^*)=\|a\|^2S(x^*x)\). Hence \(e\mathfrak ne\subseteq\mathfrak n\cap eNe\), and it is \(\sigma\)-weakly dense in \(eNe\) because \(x\mapsto exe\) is continuous. The other properties are inherited; the central elements of \(eNe\) are the \(ae\), and \(S(ae\,y)=S(ay)=aS(y)\) for \(y\in(eNe)_+\). \(\square\)

**Theorem 10.2** (The coupling function). Let \(M\) be semifinite, and let \(T\) and \(T'\) be faithful normal semifinite extended centre-valued traces on \(M\) and \(M'\). There is exactly one \(c\in\widehat Z_+\), finite and nonzero outside a rare set, such that
\[
T(p_\xi)=c\,T'(p'_\xi)\qquad(\xi\in H)
\tag{10.2}
\]
in the sense of (10.1).

**Proof.** *Existence.* Take \(N,\sigma,e,f,W,\alpha,\beta,\kappa\) from Theorem 8.2. \(N\) is semifinite, since it has the trace \(\sigma\), so it has a faithful normal semifinite extended centre-valued trace \(S\) (Fact 2.9). By Lemma 10.1(2), \(S\) restricts to such traces on \(eNe\) and on \(fNf\), with centres identified with \(Z_N\). By Theorem 8.2(3), \(\alpha\) and \(\beta\) both induce the isomorphism \(\kappa\) on the centres. So Lemma 10.1(1) turns \(\tilde T(x)=\kappa^{-1}_*S(\alpha(x))\) and \(\tilde T'(y')=\kappa^{-1}_*S(\beta(y'))\) into faithful normal semifinite extended centre-valued traces on \(M\) and on \(M'\), with values in \(\widehat Z_+\). By Lemma 9.2, \(\alpha(p_\xi)\sim\beta(p'_\xi)\), and \(S\) is constant on equivalence classes because \(S(v^*v)=S(vv^*)\). So
\[
\tilde T(p_\xi)=\tilde T'(p'_\xi)\qquad(\xi\in H).
\]
By Fact 2.9 there are \(d,d'\in\widehat Z_+\), finite and nonzero outside rare sets, with \(\tilde T=dT\) and \(\tilde T'=d'T'\). On the dense open set \(G=G_d\cap G_{d'}\), the function \(d'/d\) is continuous with values in \((0,\infty)\). Composed with the homeomorphism \(t\mapsto t/(1+t)\) of \([0,\infty]\) onto \([0,1]\), it becomes a bounded continuous function on \(G\), so by Fact 2.8 it extends to some \(c\in\widehat Z_+\) with \(c=d'/d\) on \(G\). Then \(G\subseteq G_c\), so \(G_c\) is dense. For \(\omega\in G\), \(d(\omega)T(p_\xi)(\omega)=\tilde T(p_\xi)(\omega)=\tilde T'(p'_\xi)(\omega)=d'(\omega)T'(p'_\xi)(\omega)\), so \(T(p_\xi)(\omega)=c(\omega)T'(p'_\xi)(\omega)\). As \(G\) is dense in \(G_c\), this is (10.2).

*Uniqueness.* Let \(c_1,c_2\) both satisfy (10.2), and suppose \(c_1(\omega_0)\ne c_2(\omega_0)\). By continuity \(c_1\ne c_2\) on an open neighbourhood of \(\omega_0\), which meets the dense open set \(G_{c_1}\cap G_{c_2}\); so there is a nonempty open \(U\subseteq G_{c_1}\cap G_{c_2}\) on which \(c_1\ne c_2\). Choose \(\omega_1\in U\) and an open \(V\) with \(\omega_1\in V\subseteq\bar V\subseteq U\). The closure \(\bar V\) is open because \(\Omega\) is stonean, so \(\bar V=\Omega_z\) for a nonzero central projection \(z\).

We find \(\xi\) such that \(T'(p'_\xi)\) is finite and not identically zero on \(\Omega_z\). The set \(\mathfrak n'=\{y'\in M':T'(y'^*y')\in Z_+\}\) is a two-sided ideal (as in Lemma 10.1(2)) and \(\sigma\)-weakly dense in \(M'\), so some \(y'\in\mathfrak n'\) has \(y'z\ne0\). The element \(h=zy'^*y'z\) is positive and nonzero, and \(T'(h)=zT'(y'^*y')\in Z_+\). Its spectral projection \(e'=\chi_{[\|h\|/2,\infty)}(h)\) is nonzero, lies below \(z\), and satisfies \(e'\le(2/\|h\|)h\), so \(T'(e')\in Z_+\). Take a nonzero \(\xi\in e'H\). Then \(p'_\xi\le e'\) (Fact 2.3(1)), so \(T'(p'_\xi)\le T'(e')\) is finite-valued; \(T'(p'_\xi)\ne0\) by faithfulness; and \(T'(p'_\xi)=zT'(p'_\xi)\) vanishes outside \(\Omega_z\). So \(O=\{\omega:T'(p'_\xi)(\omega)>0\}\) is a nonempty open subset of \(\Omega_z\subseteq U\). For \(\omega\in O\), (10.2) for \(c_1\) and \(c_2\) gives \(c_1(\omega)T'(p'_\xi)(\omega)=T(p_\xi)(\omega)=c_2(\omega)T'(p'_\xi)(\omega)\) with \(0<T'(p'_\xi)(\omega)<\infty\), so \(c_1(\omega)=c_2(\omega)\). This contradicts \(O\subseteq U\). \(\square\)

**Definition 10.3** (Coupling function and coupling constant).

1. If \(M\) and \(M'\) are finite, their centre-valued traces \(T_M\) and \(T_{M'}\) are faithful normal semifinite extended centre-valued traces (Fact 2.9). The element \(c\) of Theorem 10.2 for \(T=T_M\) and \(T'=T_{M'}\) is the *coupling function* \(c(M,H)\):
\[
T_M(p_\xi)=c(M,H)\,T_{M'}(p'_\xi)\qquad(\xi\in H).
\]
If \(M\) is a factor, \(\Omega\) is a point, and \(c(M,H)\) is a positive number, the *coupling constant* of \(M\) on \(H\).
2. More generally, let \(M\) be semifinite with finite commutant, and let \(T\) be a faithful normal semifinite extended centre-valued trace on \(M\). We write \(c_T(M,H)\) for the element \(c\) of Theorem 10.2 with \(T'=T_{M'}\). For finite \(M\), \(c_{T_M}(M,H)=c(M,H)\).

*Reference:* Murray and von Neumann for factors; [Griffin 1953] for algebras with a centre.

**Example 10.4.**

1. (*Matrix algebras.*) For \(M=M_n(\mathbb C)\otimes1\) on \(\mathbb C^n\otimes\mathbb C^m\), \(c(M,H)=m/n\) (Exercise 12.1). This is the number \(m\) of copies of \(\mathbb C^n\), divided by \(n\).
2. (*A multiplicity-\(n\) abelian algebra.*) Let \(M=L^\infty[0,1]\otimes1\) on \(L^2[0,1]\otimes\mathbb C^n\). As \(L^\infty[0,1]\) is its own commutant (Example 7.2(3)), Fact 2.2(7) gives \(M'=\mathbb M_n(L^\infty[0,1])\), whose centre is \(Z=M\). Here \(T_M\) is the identity, and \(T_{M'}(x)=\frac1n\sum_kx_{kk}\) (Traces on von Neumann algebras, Example 5.8). For \(\xi=1\otimes\delta_1\), the vectors \((g\otimes E_{k1})\xi=g\otimes\delta_k\) show \(p_\xi=1\), and \(p'_\xi\) projects onto \(L^2[0,1]\otimes\mathbb C\delta_1\), so \(p'_\xi=1\otimes E_{11}\) and \(T_{M'}(p'_\xi)=\frac1n\). Hence \(c(M,H)=n\) everywhere.
3. (*An unbounded coupling function.*) Let \(M\) be the algebra of operators \(\bigoplus_k\lambda_k1\) (bounded scalars \(\lambda_k\)) on \(H=\bigoplus_{k\ge1}\mathbb C^k\). It is commutative. An operator that commutes with \(M\) commutes with the projections onto the summands, so it is block diagonal; hence \(M'\) is the algebra of bounded block-diagonal operators \(\bigoplus_ky_k\), \(y_k\in M_k(\mathbb C)\). It is finite, because \(u^*u=1\) forces \(u_k^*u_k=1\), hence \(u_ku_k^*=1\), in each block. Its centre-valued trace is \(T_{M'}(\bigoplus_ky_k)=\bigoplus_k\mathrm{tr}_k(y_k)1\), with normalized traces \(\mathrm{tr}_k\), by the uniqueness in Fact 2.5(4). Let \(z_k\) be the projection onto the \(k\)-th summand. For a nonzero \(\xi\) in that summand, \(p_\xi=z_k\) and \(p'_\xi\) is the projection onto \(\mathbb C\xi\), so \(T_M(p_\xi)=z_k\) and \(T_{M'}(p'_\xi)=\frac1kz_k\). Hence \(c(M,H)=k\) on \(\Omega_{z_k}\). These open and closed sets are disjoint and their union is dense, so \(c(M,H)\) is finite outside a rare set but not bounded. So the coupling function need not lie in \(Z\), even for finite algebras with finite commutant.
4. (*A semifinite algebra with finite commutant.*) Let \(L\) be infinite-dimensional and \(M=B(L)\otimes1\) on \(L\otimes\mathbb C^m\), with the trace \(T(x\otimes1)=\mathrm{Tr}(x)\). Then \(M'=1\otimes M_m(\mathbb C)\) is finite, and \(c_T(M,H)=m\) (Exercise 12.1). Theorem 10.6 below shows that this number, computed with \(\mathrm{Tr}\) transported to each image, classifies the faithful normal representations of \(B(L)\) with finite commutant.

**Proposition 10.5** (Changing the space).

1. If \(M\) and \(M'\) are finite, then \(c(M',H)=1/c(M,H)\).
2. Let \(M\) be semifinite with finite commutant, \(T\) a faithful normal semifinite extended centre-valued trace on \(M\), and \(e'\in\mathcal P(M')\) with \(c(e')=1\). The induction \(\iota(x)=x_{e'}\) is an isomorphism of \(M\) onto \(M_{e'}\), whose commutant \(e'M'e'\) is finite. Identify the centres through \(\iota\), and put \(T_{e'}=\iota_*\circ T\circ\iota^{-1}\). Then
\[
c_{T_{e'}}(M_{e'},e'H)(\omega)=c_T(M,H)(\omega)\,T_{M'}(e')(\omega)\qquad\text{for every }\omega\in G_{c_T(M,H)}.
\]
In particular \(c(M_{e'},e'H)=c(M,H)T_{M'}(e')\) on \(G_{c(M,H)}\) when \(M\) is finite.
3. If \(M\) and \(M'\) are finite and \(e\in\mathcal P(M)\) has \(c(e)=1\), then, with the centre of \(eMe\) identified with \(Z\), \(c(eMe,eH)(\omega)=c(M,H)(\omega)/T_M(e)(\omega)\) for every \(\omega\in G_{c(M,H)}\) with \(T_M(e)(\omega)>0\).

**Proof.** (1) Write \(c=c(M,H)\). For the algebra \(M'\), whose commutant is \(M\), the roles of \(p_\xi\) and \(p'_\xi\) are exchanged. On \(G_c=G_{1/c}\), \(T_M(p_\xi)=cT_{M'}(p'_\xi)\) is equivalent to \(T_{M'}(p'_\xi)=(1/c)T_M(p_\xi)\). By uniqueness in Theorem 10.2, \(c(M',H)=1/c\).

(2) The kernel of \(\iota\) is \(M(1-c(e'))=\{0\}\), so \(\iota\) is an isomorphism and \(M_{e'}\) is semifinite; its commutant \(e'M'e'\) (Fact 2.1(1)) is a corner of a finite algebra, hence finite.

*A formula for \(T_{M'}\) on the corner.* Identify the centre \(Ze'\) of \(e'M'e'\) with \(Z\) (Fact 2.1(4)); write \(T_{e'M'e'}(y)=a_ye'\) with \(a_y\in Z\). We claim \(T_{M'}(y)=a_yT_{M'}(e')\) for \(y\in e'M'e'\). Let \(\psi\) be a normal state of \(Z\). Then \(y\mapsto\psi(T_{M'}(y))\) defines a finite normal trace of the finite algebra \(e'M'e'\), so by Fact 2.5(4) it equals its value at \(T_{e'M'e'}(y)=a_ye'\), which is \(\psi(T_{M'}(a_ye'))=\psi(a_yT_{M'}(e'))\). Normal states separate \(Z\), so the claim follows.

*The coupling function.* For \(\xi\in e'H\), the cyclic projection of \(M_{e'}\) at \(\xi\) is the projection onto \([(e'M'e')\xi]=e'[M'\xi]\), that is, \(\iota(p_\xi)\); and the cyclic projection of its commutant is the projection onto \([M_{e'}\xi]=[M\xi]\), that is, \(p'_\xi\). So, with \(c=c_T(M,H)\) and for \(\omega\in G_c\),
\[
T_{e'}(\iota(p_\xi))(\omega)=T(p_\xi)(\omega)=c(\omega)T_{M'}(p'_\xi)(\omega)=c(\omega)T_{M'}(e')(\omega)\,T_{e'M'e'}(p'_\xi)(\omega).
\]
The function \(T_{M'}(e')\) is finite, and it is positive on a dense open set: otherwise it would vanish on some \(\Omega_z\) with \(z\ne0\), so \(T_{M'}(ze')=0\), \(ze'=0\), and \(zc(e')=0\), against \(c(e')=1\). By Fact 2.8 the function \(cT_{M'}(e')\) on \(G_c\) extends (after composing with \(t\mapsto t/(1+t)\)) to some \(\tilde c\in\widehat Z_+\), finite and nonzero on the dense open set \(G_c\cap\{T_{M'}(e')>0\}\). The display shows that \(\tilde c\) satisfies (10.2) for \(M_{e'}\), with \(T_{e'}\) and \(T_{e'M'e'}\). By uniqueness in Theorem 10.2, \(c_{T_{e'}}(M_{e'},e'H)=\tilde c\).

(3) Apply (2) to the finite algebra \(M'\), whose commutant \(M\) is finite, and to the projection \(e\) of \((M')'=M\). The induced algebra of \(M'\) by \(e\) is \(M'e\) on \(eH\), and (2) gives \(c(M'e,eH)=c(M',H)T_M(e)\) on \(G_{c(M',H)}\). The algebra \(eMe\) on \(eH\) has commutant \(M'e\), so by (1), twice, \(c(eMe,eH)=1/c(M'e,eH)=c(M,H)/T_M(e)\) at the points stated. \(\square\)

**Theorem 10.6** (The coupling function classifies). Let \(M_1\) on \(H_1\) and \(M_2\) on \(H_2\) be semifinite with finite commutants, \(\pi:M_1\to M_2\) an isomorphism, \(T_1\) a faithful normal semifinite extended centre-valued trace on \(M_1\), and \(T_2=\pi_*\circ T_1\circ\pi^{-1}\). Then \(\pi\) is spatial exactly when
\[
\pi_*\bigl(c_{T_1}(M_1,H_1)\bigr)=c_{T_2}(M_2,H_2).
\]
If \(M_1\) is finite, then \(T_{M_2}=\pi_*\circ T_{M_1}\circ\pi^{-1}\), and the condition reads \(\pi_*(c(M_1,H_1))=c(M_2,H_2)\).


**Proof.** The last sentence holds by uniqueness of the centre-valued trace (Fact 2.5(4)).

*Only if.* Let \(\pi(x)=UxU^*\). Then \(UM_1'U^*=M_2'\), \(Up_\xi U^*=p_{U\xi}\) and \(Up'_\xi U^*=p'_{U\xi}\), and \(T_{M_2'}(Uy'U^*)=\pi_*(T_{M_1'}(y'))\) by uniqueness of the centre-valued trace. Applying \(\pi_*\) to \(T_1(p_\xi)=c_1T_{M_1'}(p'_\xi)\) gives \(T_2(p_{U\xi})=\pi_*(c_1)T_{M_2'}(p'_{U\xi})\) for all \(\xi\), and \(U\) is onto. Uniqueness gives \(c_2=\pi_*(c_1)\).

*If.* Let \(P\), \(q_1\), \(q_2\) be the joint algebra and projections of \(x\mapsto x\) and \(x\mapsto\pi(x)\) (Lemma 3.1), and \(\rho(x)=x\oplus\pi(x)\). Both representations are faithful, so \(c(q_1)=c(q_2)=1\). The corners \(q_iP'q_i=M_i'\) are finite, so \(q_1\) and \(q_2\) are finite projections of \(P'\), and so is \(q_1\vee q_2=1\) (Fact 2.2(10)); thus \(P'\) is finite. \(P\cong M_1\) is semifinite; transport \(T_1\) to \(T_P=\rho_*\circ T_1\circ\rho^{-1}\). The induction of \(P\) by \(q_1\) is \(\rho(x)\mapsto x\), and that by \(q_2\) is \(\rho(x)\mapsto\pi(x)\) (Lemma 3.1(2)). They carry \(T_P\) to \(T_1\) and \(T_2\), and they identify the centres compatibly with \(\pi_*\). Proposition 10.5(2) gives, on \(G_{c_{T_P}(P,K)}\),
\[
c_{T_1}(M_1,H_1)=c_{T_P}(P,K)\,T_{P'}(q_1),\qquad c_{T_2}(M_2,H_2)=c_{T_P}(P,K)\,T_{P'}(q_2),
\]
after these identifications. If the two coupling functions agree, then \(T_{P'}(q_1)=T_{P'}(q_2)\) on the dense set \(G_{c_{T_P}(P,K)}\), hence everywhere by continuity. By Fact 2.5(4), \(q_1\sim q_2\) in \(P'\), and \(\pi\) is spatial by Lemma 3.1(3). \(\square\)

**Corollary 10.7** (II\(_\infty\) factors whose commutant is finite). Let \(M\) on \(H\) and \(N\) on \(K\) be factors of type II\(_\infty\) whose commutants are finite.

1. \(M\) has a cyclic vector.
2. Let \(\tau_M\) be a faithful normal semifinite trace on \(M\), \(\pi:M\to N\) an isomorphism, and \(\tau_N=\tau_M\circ\pi^{-1}\). For every cyclic vector \(\xi_0\) of \(M\), \(\tau_M(p_{\xi_0})=c_{\tau_M}(M,H)\), a number in \((0,\infty)\) that does not depend on \(\xi_0\). And \(\pi\) is spatial exactly when \(\tau_M(p_{\xi_0})=\tau_N(p_{\eta_0})\) for cyclic vectors \(\xi_0\) of \(M\) and \(\eta_0\) of \(N\).

**Proof.** (1) \(M'\) is a finite factor, hence \(\sigma\)-finite (Fact 2.5(5)), and it has a faithful normal state \(\psi\). Its commutant \(M\) is of type II\(_\infty\), hence properly infinite. Lemma 3.4, applied to \(M'\), gives \(\psi=\omega_\xi|_{M'}\). As \(\psi\) is faithful, \(\xi\) is separating for \(M'\), that is, cyclic for \(M\).

(2) For factors, \(\Omega\) is a point, \(\widehat Z_+=[0,\infty]\), and \(\tau_M\) is a faithful normal semifinite extended centre-valued trace; \(T_{M'}\) is the tracial state of \(M'\). If \(\xi_0\) is cyclic, \(p'_{\xi_0}=1\), so \(\tau_M(p_{\xi_0})=c_{\tau_M}(M,H)\cdot1\). The same holds for \(N\). Here \(\pi_*\) is the identity of \([0,\infty]\), so Theorem 10.6 says that \(\pi\) is spatial exactly when \(c_{\tau_M}(M,H)=c_{\tau_N}(N,K)\). \(\square\)

The condition in (2) is not automatic. If an automorphism \(\theta\) of \(M\) scales the trace, \(\tau_M\circ\theta=\lambda\tau_M\) with \(\lambda\ne1\), then \(\tau_N=\lambda^{-1}\tau_M\) for \(N=M\) and \(\pi=\theta\), so (2) shows that \(\theta\) is not implemented by a unitary. Such factors exist: \(R\bar\otimes B(\ell^2)\), on \(L^2(R)\otimes\ell^2\), has commutant of type II\(_1\) and has automorphisms that scale its trace by every \(\lambda>0\) [Connes 1976, §3.7].

**Theorem 10.8** (Cyclic and separating vectors of finite algebras). Let \(M\) be finite with \(\sigma\)-finite centre, and let \(1=z_f+z_\infty\), with \(M'z_f\) finite and \(M'z_\infty\) properly infinite (Fact 2.2(6) for \(M'\)).

1. \(M\) has a cyclic vector if and only if \(z_\infty=0\) and \(c(M,H)\le1\).
2. \(M\) has a separating vector exactly when \(c(Mz_f,z_fH)\ge1\).

In particular, if \(M'\) is also finite, \(M\) has a cyclic vector exactly when \(c(M,H)\le1\), and a separating vector exactly when \(c(M,H)\ge1\).

**Proof.** By Fact 2.5(5), \(M\) is \(\sigma\)-finite.

(1) Let \(\xi\) be cyclic. By Corollary 9.6, \(M'\) is finite, so \(z_\infty=0\). As \(p'_\xi=1\), \(T_M(p_\xi)=c\,T_{M'}(1)=c\) on \(G_c\), where \(c=c(M,H)\); so \(c\le T_M(p_\xi)\le1\) on \(G_c\), and on \(\Omega\) by continuity. Conversely, let \(M'\) be finite and \(c\le1\). Proposition 5.1 gives a central \(z\) and \(\xi\) with \(z\le p'_\xi\) and \(1-z\le p_\xi\). Put \(\xi_2=(1-z)\xi\), so \(p_{\xi_2}=1-z\) and \(p'_{\xi_2}\le1-z\). At \(\omega\in G_c\cap\Omega_{1-z}\), \(1=T_M(p_{\xi_2})(\omega)=c(\omega)T_{M'}(p'_{\xi_2})(\omega)\le T_{M'}(p'_{\xi_2})(\omega)\le1\); at \(\omega\in\Omega_z\), \(T_{M'}(p'_{\xi_2})(\omega)=0\). So \(T_{M'}(p'_{\xi_2})=1-z\) on a dense set, hence everywhere, and faithfulness gives \(p'_{\xi_2}=1-z\). Now \(p'_{z\xi}=z\) and \(p'_{(1-z)\xi}=1-z\), so \(p'_\xi=1\) (Lemma 3.3(1)).

(2) The algebra \(Mz_\infty\) is \(\sigma\)-finite, so it has a faithful normal state, and its commutant \(M'z_\infty\) is properly infinite. By Lemma 3.4 the state is \(\omega_{\zeta_\infty}\) with \(\zeta_\infty\in z_\infty H\), and faithfulness makes \(\zeta_\infty\) separating for \(Mz_\infty\). If \(\zeta\) is separating for \(M\), then \(z_f\zeta\) is separating for \(Mz_f\); and if \(\zeta_f\) is separating for \(Mz_f\), then \(\zeta_f+\zeta_\infty\) is separating for \(M\). So it suffices to treat \(Mz_f\), which is finite, with finite commutant \(M'z_f\) and \(\sigma\)-finite centre. A vector is separating for \(Mz_f\) exactly when it is cyclic for \(M'z_f\). By (1), applied to \(M'z_f\), this happens exactly when \(c(M'z_f,z_fH)\le1\), that is, \(c(Mz_f,z_fH)\ge1\) (Proposition 10.5(1)). \(\square\)

**Example 10.9** (The centre must be \(\sigma\)-finite). In Example 5.5, \(M=M'=Z=\ell^\infty(\Gamma)\), \(T_M\) and \(T_{M'}\) are the identity, and \(p_\xi=p'_\xi\) is the indicator of the support of \(\xi\); so \(c(M,H)=1\). But \(M\) has neither a cyclic nor a separating vector, since either would make \(Z\) \(\sigma\)-finite (Fact 2.4(1)).

**Corollary 10.10.** Let \(M\) be finite with finite commutant and \(\sigma\)-finite centre. The following are equivalent: (a) \(c(M,H)=1\); (b) some vector is cyclic and separating for \(M\); (c) \(M\) has a unitary involution.

**Proof.** (a)⇒(b): by Theorem 10.8, \(M\) has both a cyclic and a separating vector, and by Fact 2.3(4) one vector does both jobs. (b)⇒(c): let \(\tau\) be a faithful normal finite trace on \(M\) (Fact 2.5(5)). In \(L^2(M,\tau)\) the vector \(\Lambda_\tau(1)\) is cyclic and separating for \(\pi_\tau(M)\): \(L_x\Lambda_\tau(1)=\Lambda_\tau(x)\), these vectors are dense, and \(\Lambda_\tau(x)=0\) forces \(\tau(x^*x)=0\), so \(x=0\). By Fact 2.3(5), \(\pi_\tau\) is spatial, and the canonical unitary involution of \(L^2(M,\tau)\) (Example 7.2(1)) can be carried to \(H\). (c)⇒(a): let \(\theta\) be the anti-isomorphism of Lemma 7.3. The linear map \(y'\mapsto T_M(\theta^{-1}(y'))\) on \(M'\) satisfies the three conditions of Fact 2.5(4). Indeed \(\theta^{-1}(w^*w)=\theta^{-1}(w)\theta^{-1}(w)^*\) and \(\theta^{-1}(ww^*)=\theta^{-1}(w)^*\theta^{-1}(w)\), and \(T_M\) takes equal, positive values at these two elements; \(\theta^{-1}(ay')=\theta^{-1}(y')a\) for central \(a\); and the value at \(1\) is \(1\). So it is \(T_{M'}\). For positive \(y'\), \(\theta^{-1}(y')=Jy'J\), so Corollary 7.5(2) gives \(T_{M'}(p'_\xi)=T_M(p_\xi)\) for all \(\xi\), and \(c(M,H)=1\) by uniqueness. \(\square\)

## 11. Tracial states and their representations

A tracial state of a \(C^*\)-algebra produces, through its cyclic representation, a finite algebra with a unitary involution. So the results of Section 7 apply to it.

**Definition 11.1.** A positive linear functional \(\varphi\) on a \(C^*\)-algebra \(A\) is *tracial*, or *central*, if \(\varphi(x^*x)=\varphi(xx^*)\) for all \(x\in A\).

Then \(\varphi(xy)=\varphi(yx)\) for all \(x,y\in A\). Indeed, in any \(*\)-algebra \(4y^*x=\sum_{k=0}^3i^k(x+i^ky)^*(x+i^ky)\) and \(4xy^*=\sum_{k=0}^3i^k(x+i^ky)(x+i^ky)^*\); applying \(\varphi\) gives \(\varphi(y^*x)=\varphi(xy^*)\), and we replace \(y\) by \(y^*\).

**Proposition 11.2.** Let \(A\) be a \(C^*\)-algebra, with or without a unit, let \(\varphi\) be a positive linear functional on \(A\) that is tracial, and let \((\pi,K,\xi)\) be a cyclic representation with \(\varphi(a)=\langle\pi(a)\xi,\xi\rangle\) (Fact 2.4(5)). Let \(M=\pi(A)''\).

1. \(\tilde\varphi(x)=\langle x\xi,\xi\rangle\) is a faithful normal finite trace on \(M\).
2. \(\xi\) is cyclic and separating for \(M\).
3. The map \(\pi(a)\xi\mapsto\pi(a^*)\xi\) extends to a unitary involution \(J\) of \(\{M,K\}\), with \(J\xi=\xi\) and \(J(x\xi)=x^*\xi\) for every \(x\in M\).

Consequently every normal state of \(M\) is a vector state, and every automorphism of \(M\) is implemented by a unitary on \(K\) (Theorem 7.8, Corollary 7.11).

**Proof.** *The trace property.* For \(a,b\in A\), \(\tilde\varphi(\pi(a)\pi(b))=\varphi(ab)=\varphi(ba)=\tilde\varphi(\pi(b)\pi(a))\). Fix \(y\in\pi(A)\). The functional \(x\mapsto\tilde\varphi(xy)-\tilde\varphi(yx)\) is \(\sigma\)-weakly continuous and vanishes on \(\pi(A)\), which is \(\sigma\)-weakly dense in \(M\) because \(\pi\) is nondegenerate (Fact 2.4(4)); so it vanishes on \(M\). Now fix \(x\in M\): the functional \(y\mapsto\tilde\varphi(xy)-\tilde\varphi(yx)\) vanishes on \(\pi(A)\), hence on \(M\). So \(\tilde\varphi(xy)=\tilde\varphi(yx)\) on \(M\), and \(\tilde\varphi\), a positive normal functional, is a finite normal trace (Fact 2.5(1)).

*The involution.* For \(a\in A\), \(\|\pi(a^*)\xi\|^2=\varphi(aa^*)=\varphi(a^*a)=\|\pi(a)\xi\|^2\). So \(J_0(\pi(a)\xi)=\pi(a^*)\xi\) is a well-defined conjugate-linear isometry of the dense subspace \(\pi(A)\xi\) onto itself, with \(J_0^2=1\). It extends to a conjugate-linear isometry \(J\) of \(K\) with \(J^2=1\); so \(J\) is onto. Polarization gives \(\langle J\eta,J\zeta\rangle=\langle\zeta,\eta\rangle\): the real parts agree because \(\|J(\eta+\zeta)\|=\|\eta+\zeta\|\), and replacing \(\zeta\) by \(i\zeta\) handles the imaginary parts. If \(A\) has a unit, \(J\xi=J\pi(1)\xi=\xi\). In general, let \((u_i)\) be an approximate unit of positive contractions (Fact 2.4(5)). Then \(\pi(u_i)\pi(a)\xi=\pi(u_ia)\xi\to\pi(a)\xi\), so the bounded net \(\pi(u_i)\) tends to \(1\) strongly on the dense subspace \(\pi(A)\xi\), hence on \(K\), and \(\xi=\lim_i\pi(u_i)\xi\). As \(J\pi(u_i)\xi=\pi(u_i)\xi\), \(J\xi=\xi\).

For \(a,b,x\in A\), \(J\pi(a)J\pi(x)\xi=J\pi(a)\pi(x^*)\xi=J\pi(ax^*)\xi=\pi(xa^*)\xi\). Hence
\[
J\pi(a)J\,\pi(b)\pi(x)\xi=\pi(bxa^*)\xi=\pi(b)\,J\pi(a)J\,\pi(x)\xi .
\]
So \(J\pi(a)J\) commutes with \(\pi(b)\) on a dense subspace, hence everywhere, and \(J\pi(A)J\subseteq\pi(A)'=M'\). The map \(x\mapsto JxJ\) is continuous for the weak operator topology, since \(\langle JxJ\eta,\zeta\rangle=\langle J\zeta,xJ\eta\rangle\), and \(M\) is the weak closure of \(\pi(A)\); so \(JMJ\subseteq M'\).

For \(x\in M\) and \(a\in A\), using \(\langle J\alpha,\beta\rangle=\langle J\beta,\alpha\rangle\) and the trace property,
\[
\langle J(x\xi),\pi(a)\xi\rangle=\langle\pi(a^*)\xi,x\xi\rangle=\tilde\varphi\bigl(x^*\pi(a^*)\bigr)=\tilde\varphi\bigl(\pi(a^*)x^*\bigr)=\langle x^*\xi,\pi(a)\xi\rangle .
\]
So \(J(x\xi)=x^*\xi\).

*Cyclic and separating.* \(\xi\) is cyclic for \(M\supseteq\pi(A)\). And \(M'\xi\supseteq JMJ\xi=JM\xi=M^*\xi=M\xi\), which is dense; so \(\xi\) is cyclic for \(M'\), that is, separating for \(M\). Hence \(\tilde\varphi(x^*x)=\|x\xi\|^2=0\) forces \(x=0\): \(\tilde\varphi\) is faithful.

*\(JMJ=M'\) and the centre.* \(\tilde\varphi\) is a faithful normal finite trace, so \(\mathfrak n_{\tilde\varphi}=M\), and \(L^2(M,\tilde\varphi)\) is the completion of \(M\) for \(\langle x,y\rangle=\tilde\varphi(y^*x)\). The map \(\Lambda_{\tilde\varphi}(x)\mapsto x\xi\) is isometric with dense range, so it extends to a unitary \(V:L^2(M,\tilde\varphi)\to K\). It satisfies \(VL_xV^*=x\), because \(VL_x\Lambda(y)=xy\xi=xV\Lambda(y)\), and \(VJ_{\tilde\varphi}V^*=J\), because \(VJ_{\tilde\varphi}\Lambda(y)=y^*\xi=J(y\xi)\). By Fact 2.6, \(L_M'=J_{\tilde\varphi}L_MJ_{\tilde\varphi}\); transported by \(V\), this says \(M'=JMJ\). Finally, for \(a\in Z\) and \(x\in M\), \(JaJ(x\xi)=Ja(x^*\xi)=(ax^*)^*\xi=xa^*\xi=a^*x\xi\); so \(JaJ=a^*\). \(\square\)

**Example 11.3** (Group von Neumann algebras). Let \(G\) be a discrete group, \(\lambda(g)\delta_h=\delta_{gh}\) its left regular representation on \(\ell^2(G)\), \(A\) the norm closure of the span of \(\lambda(G)\), and \(\varphi(x)=\langle x\delta_e,\delta_e\rangle\). For \(x=\sum_gc_g\lambda(g)\) (a finite sum), \(\varphi(x^*x)=\|x\delta_e\|^2=\sum_g|c_g|^2\) and \(\varphi(xx^*)=\|x^*\delta_e\|^2=\sum_g|\bar c_g|^2\); by continuity \(\varphi\) is tracial on \(A\). The identity representation with the vector \(\delta_e\) is cyclic, since \(\lambda(g)\delta_e=\delta_g\). Proposition 11.2 shows:

- \(L(G)=\lambda(G)''\) carries the faithful normal tracial state \(\omega_{\delta_e}\), and \(\delta_e\) is cyclic and separating;
- \(J(\sum_gc_g\delta_g)=\sum_g\bar c_g\delta_{g^{-1}}\) is a unitary involution, since \(J(\lambda(g)\delta_e)=\lambda(g)^*\delta_e=\delta_{g^{-1}}\).

Moreover \(J\lambda(g)J\delta_h=J\lambda(g)\delta_{h^{-1}}=J\delta_{gh^{-1}}=\delta_{hg^{-1}}\), so \(J\lambda(g)J=\rho(g)\), the right regular representation. As \(x\mapsto JxJ\) is weakly continuous, \(L(G)'=JL(G)J=\rho(G)''\). This is the commutation theorem for group von Neumann algebras, and by Theorem 7.8 every normal state of \(L(G)\) is a vector state on \(\ell^2(G)\).

## 12. Exercises

**Exercise 12.1** (Matrix algebras and their amplifications). Let \(L\) be a Hilbert space of dimension \(n\), finite or infinite, \(m\ge1\) an integer, and \(M=B(L)\otimes1\) on \(H=L\otimes\mathbb C^m\), so that \(M'=1\otimes M_m(\mathbb C)\) (Fact 2.2(7)). For \(\xi=\sum_{j=1}^mu_j\otimes\delta_j\) let \(U\) be the span of \(u_1,\ldots,u_m\) and \(r=\dim U\).

- (a) Show that \(p_\xi=P_U\otimes1\), and \(p'_\xi=1\otimes Q\) for a projection \(Q\) of rank \(r\).
- (b) If \(n\) is finite, show that \(c(M,H)=m/n\).
- (c) If \(n\) is infinite and \(T(x\otimes1)=\mathrm{Tr}(x)\), show that \(c_T(M,H)=m\).
- (d) If \(n\) is finite, show that \(M\) has a cyclic vector exactly when \(m\le n\), a separating vector exactly when \(m\ge n\), and a unitary involution exactly when \(m=n\).

*Solution.* (a) \(M'\) is spanned by the operators \(1\otimes E_{kl}\), and \((1\otimes E_{kl})\xi=u_l\otimes\delta_k\). So \([M'\xi]=U\otimes\mathbb C^m\) and \(p_\xi=P_U\otimes1\). Choose an orthonormal basis \(f_1,\ldots,f_r\) of \(U\) and write \(u_j=\sum_sa_{sj}f_s\). The \(r\times m\) matrix \(A=(a_{sj})\) has rank \(r\), because its columns span \(\mathbb C^r\). Let \(\alpha_s=\sum_ja_{sj}\delta_j\in\mathbb C^m\) be its rows; they are linearly independent. For \(x\in B(L)\),
\[
(x\otimes1)\xi=\sum_j\sum_sa_{sj}\,xf_s\otimes\delta_j=\sum_sxf_s\otimes\alpha_s .
\]
The vectors \(xf_s\) can be any vectors of \(L\) (take \(x\) of finite rank), so \(M\xi=L\otimes\mathrm{span}\{\alpha_s\}\), a closed subspace. Hence \(p'_\xi=1\otimes Q\), with \(Q\) the projection onto the \(r\)-dimensional span of the \(\alpha_s\).

(b) \(M\cong M_n(\mathbb C)\) and \(M'\cong M_m(\mathbb C)\) are finite factors, and their centre-valued traces are the normalized traces (Fact 2.5(4)). By (a), \(T_M(p_\xi)=r/n\) and \(T_{M'}(p'_\xi)=r/m\), so \(T_M(p_\xi)=\frac mnT_{M'}(p'_\xi)\) for every \(\xi\), and \(c(M,H)=m/n\).

(c) \(T\) is a faithful normal semifinite trace on the factor \(M\), and \(\widehat Z_+=[0,\infty]\). By (a), \(T(p_\xi)=r\) and \(T_{M'}(p'_\xi)=r/m\), so \(c_T(M,H)=m\).

(d) \(\xi\) is cyclic exactly when \(p'_\xi=1\), that is, \(r=m\); since \(r\le\min(n,m)\), such a \(\xi\) exists exactly when \(m\le n\). \(\xi\) is separating exactly when \(p_\xi=1\), that is, \(U=L\) and \(r=n\); such a \(\xi\) exists exactly when \(n\le m\). This agrees with Theorem 10.8, since \(c=m/n\). For unitary involutions, see Example 7.2(4) when \(m\ne n\) and Example 7.2(2) when \(m=n\).

**Exercise 12.2** (The partner of a tracial state). Let \(M\) and \(M'\) be finite factors on \(H\), with tracial states \(\mathrm{tr}_M\) and \(\mathrm{tr}_{M'}\). Show that the partner of \(\mathrm{tr}_M\) in Theorem 9.3 is \(c(M,H)\,\mathrm{tr}_{M'}\), so that \(c(M,H)=(\mathrm{tr}_M)'(1)\). Check this against Exercise 12.1.

*Solution.* For a factor, \(T_M=\mathrm{tr}_M\) and \(T_{M'}=\mathrm{tr}_{M'}\), and \(\Omega\) is a point. By Definition 10.3, \(\mathrm{tr}_M(p_\xi)=c\,\mathrm{tr}_{M'}(p'_\xi)\) for every \(\xi\), with \(c=c(M,H)\in(0,\infty)\). So the normal trace \(c\,\mathrm{tr}_{M'}\) satisfies (9.1), and by uniqueness it is \((\mathrm{tr}_M)'\). Its value at \(1\) is \(c\). In Exercise 12.1 with \(n\) finite, \(\mathrm{tr}_M(p_\xi)=r/n=\frac mn\cdot\frac rm\), as it should be.

**Exercise 12.3** (Cyclic projections and common vectors). Let \(M\) be finite with finite commutant and \(\sigma\)-finite centre, and \(c=c(M,H)\).

- (a) Show that \(e\in\mathcal P(M)\) is a cyclic projection exactly when \(T_M(e)\le c\).
- (b) Show that \(e\in\mathcal P(M)\) and \(e'\in\mathcal P(M')\) have a common vector, \(e=p_\xi\) and \(e'=p'_\xi\), exactly when \(T_M(e)=cT_{M'}(e')\).


*Solution.* By Fact 2.5(5), \(M\) and \(M'\) are \(\sigma\)-finite; so are their corners and central summands. For a central projection \(w\), the coupling function of \(Mw\) on \(wH\) is the restriction of \(c\) to \(\Omega_w\), by uniqueness in Theorem 10.2.

(a) If \(e=p_\xi\), then \(T_M(e)=cT_{M'}(p'_\xi)\le c\) on \(G_c\), and by continuity everywhere. Conversely, let \(T_M(e)\le c\), and put \(w=c(e)\). Working in \(Mw\), we may assume \(c(e)=1\); then \(T_M(e)>0\) on a dense open set (as in the proof of Proposition 10.5(2)). By Proposition 10.5(3), \(c(eMe,eH)=c/T_M(e)\ge1\) on a dense set, hence everywhere. The algebra \(eMe\) on \(eH\) is finite, with finite commutant \(M'e\) and \(\sigma\)-finite centre, so Theorem 10.8 provides a vector \(\xi\in eH\) that separates \(eMe\); it is therefore cyclic for \(M'e\), that is, \([M'\xi]=[M'e\xi]=eH\), and \(e=p_\xi\).

(b) One direction is (10.2). Conversely, let \(T_M(e)=cT_{M'}(e')\).

*Equal central supports.* Suppose \(z=c(e)(1-c(e'))\ne0\). On \(\Omega_z\), \(T_{M'}(e')=0\), because \(T_{M'}(e')(1-c(e'))=T_{M'}(e'(1-c(e')))=0\); while \(T_M(e)>0\) on a dense open subset of \(\Omega_z\), because \(c(ze)=z\). At points of that subset that lie in \(G_c\), the relation gives \(T_M(e)=c\cdot0=0\), a contradiction. So \(c(e)\le c(e')\), and by symmetry they are equal. Working in \(Mc(e)\), we may assume \(c(e)=c(e')=1\).

*A smaller algebra.* Let \(A\) be the restriction of \(eMe\) to \(K=ee'H\): reduce by \(e\), then induce by \(e'e\in M'e\). The central support of \(e'e\) in \(M'e\) is \(e\) (if \(w\) is central and \(wee'=0\), then \(wc(e)c(e')=0\) by Lemma 3.3(6), so \(w=0\)). By Proposition 10.5(3), \(c(eMe,eH)=c/T_M(e)\). The induction \(y'\mapsto y'e\) is an isomorphism of \(M'\) onto \(M'e\), because \(c(e)=1\), and it carries \(T_{M'}\) to \(T_{M'e}\) by uniqueness; so \(T_{M'e}(e'e)=T_{M'}(e')\). Proposition 10.5(2), applied to \(eMe\) and \(e'e\), gives \(c(A,K)=\bigl(c/T_M(e)\bigr)T_{M'}(e')=1\) on a dense set, hence \(c(A,K)=1\). The algebra \(A\) is finite with finite commutant and \(\sigma\)-finite centre, so Corollary 10.10 gives a cyclic and separating vector \(\xi\in K\) for \(A\).

*The vector.* The commutant of \(A\) is the restriction of \(e'M'e'\) to \(K\), for which \(\xi\) is cyclic. So \([M'\xi]\supseteq K=ee'H\). As \([M'\xi]\) is invariant under \(M'\), it contains \([M'ee'H]=e[M'e'H]=ec(e')H=eH\) (Fact 2.1(2) for \(M'\)). Also \(\xi\in eH\), so \([M'\xi]\subseteq eH\). Hence \(p_\xi=e\). In the same way \([M\xi]\supseteq[Mee'H]=e'c(e)H=e'H\) and \(\xi\in e'H\), so \(p'_\xi=e'\).

**Exercise 12.4** (When the space splits). Show that there is a central projection \(z\) such that \(Mz\) has a cyclic vector in \(zH\) and \(M(1-z)\) has a separating vector in \((1-z)H\), if and only if there is a central projection \(w\) such that \(M'w\) and \(M(1-w)\) are \(\sigma\)-finite. (Proposition 5.1 is the case \(w=0\) or \(w=1\).)

*Solution.* If \(z\) exists, the cyclic vector of \(Mz\) is separating for \(M'z\), and \(M(1-z)\) has a separating vector; so \(w=z\) works (Fact 2.4(1)). Conversely, let \(w\) be given. Proposition 5.1, applied to the \(\sigma\)-finite algebra \(M(1-w)\) on \((1-w)H\), gives a central \(z_1\le1-w\) and \(\xi_1\in(1-w)H\) with \(p'_{z_1\xi_1}=z_1\) and \(p_{(1-w-z_1)\xi_1}=1-w-z_1\). Applied to the \(\sigma\)-finite algebra \(M'w\) on \(wH\), whose commutant is \(Mw\), it gives a central \(z_2\le w\) and \(\xi_2\in wH\) such that \(z_2\xi_2\) is cyclic for \(M'z_2\) and \((w-z_2)\xi_2\) is separating for \(M'(w-z_2)\); that is, \(p_{z_2\xi_2}=z_2\) and \(p'_{(w-z_2)\xi_2}=w-z_2\). Put \(z=z_1+(w-z_2)\) and \(\xi=\xi_1+\xi_2\). By Lemma 3.3(1), \(p'_{z\xi}=p'_{z_1\xi_1}+p'_{(w-z_2)\xi_2}=z\), so \(z\xi\) is cyclic for \(Mz\); and \(1-z=(1-w-z_1)+z_2\) gives \(p_{(1-z)\xi}=(1-w-z_1)+z_2=1-z\), so \((1-z)\xi\) is separating for \(M(1-z)\). The example \(B(H_1)\oplus\mathbb C1_{H_2}\) on \(H_1\oplus H_2\), with \(H_1\) and \(H_2\) of uncountable dimension, has such a splitting although neither \(M\) nor \(M'\) is \(\sigma\)-finite.

## Where this leads

- Every von Neumann algebra has a standard form, unique up to spatial isomorphism [Haagerup 1975], [Kostecki, Section 3.3]. Its conjugation is a unitary involution, so by Theorem 7.10 every algebra with a unitary involution is a copy of it; for semifinite algebras this is Corollary 7.11(2).
- For a subfactor \(N\) of finite index in a factor \(M\) of type II\(_1\), acting on the Hilbert space of the trace of \(M\), the coupling constant of \(N\) is the index \([M:N]\) [Blackadar, III.2.6.21].

## References



- [Kostecki] R. P. Kostecki, *W\*-algebras and noncommutative integration*, arXiv:1307.4818, 2013. https://arxiv.org/abs/1307.4818
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, revised and corrected edition with hyperlinks, free from the author: https://bruceblackadar.com/Mathematics/Cycr.pdf (first published as Encyclopaedia of Mathematical Sciences 122, 2006; the numbering is the same).
- [Griffin 1953] E. Griffin, Some contributions to the theory of rings of operators, *Transactions of the American Mathematical Society* 75 (1953), 471–504. Free at https://www.ams.org/journals/tran/1953-075-03/S0002-9947-1953-0059487-4/
- [Haagerup 1975] U. Haagerup, The standard form of von Neumann algebras, *Mathematica Scandinavica* 37 (1975), 271–283. Free at https://doi.org/10.7146/math.scand.a-11606
- [Connes 1976] A. Connes, *On the classification of von Neumann algebras and their automorphisms*, IHÉS preprint
  IHES/P/76/132, February 1976. Free at
  https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1976-1984/P_76_132/P_76_132_web.pdf

- [Anantharaman–Popa] C. Anantharaman and S. Popa, *An introduction to II₁ factors*, book draft. Free at
  https://www.math.ucla.edu/~popa/Books/IIun.pdf
