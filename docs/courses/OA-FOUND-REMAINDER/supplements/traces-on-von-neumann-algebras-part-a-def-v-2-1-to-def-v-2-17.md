# Traces on von Neumann algebras

*Written by Claude Opus 5.5 (Anthropic), September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A trace on a von Neumann algebra measures the size of positive elements, and it cannot tell \(x^*x\) from \(xx^*\). The usual trace of matrices is the model. Since a trace gives equivalent projections the same value, it turns the comparison of projections into arithmetic. It is also the starting point of integration on von Neumann algebras.

This lesson develops traces from the definition up to the trace norm. We introduce the definition ideal of a trace and show that the usual forms of semifiniteness agree. For traces that take infinite values we construct supports, semifinite parts and sums. We prove that an algebra is finite exactly when its finite normal traces separate its positive elements. For a finite algebra we build the center-valued trace, and we show that every finite trace on it, normal or not, is determined by its values on the center. We extend normal traces from corners and amplify them by type I factors, and we show that an algebra is semifinite exactly when it carries a faithful semifinite normal trace. The last section introduces the trace norm and, for a faithful semifinite normal trace, identifies the completion of the definition ideal with the predual.

The lesson assumes the comparison theory of projections and the type decomposition, from [Projections and types of von Neumann algebras](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html); the basic structure of von Neumann algebras, from [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html); and normal functionals and preduals, from [The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html). One step uses [Spatial tensor products of von Neumann algebras](../reader/supplements/spatial-tensor-products.html). The results used without proof are stated in full below.

Traces go back to the work of Murray and von Neumann on rings of operators (1936); the trace of a finite factor is constructed in [Murray–von Neumann 1937]. Other proofs that finite algebras carry traces came later, among them [Dixmier 1949] and [Yeadon 1971]; Section 4 uses Yeadon's fixed-point argument. Integration with respect to a trace goes back to Segal (1953) and [Dixmier 1953]; [Nelson 1974] presents Segal's theory through convergence in measure. Basic references are [Kostecki] and [Takesaki I].

## Conventions

- \(M\) is a von Neumann algebra on a complex Hilbert space \(H\). Nothing is assumed separable or \(\sigma\)-finite. Inner products are linear in the first variable. \(\mathcal Z\) is the center of \(M\), \(\mathcal U(M)\) its unitary group, \(M_+\) its positive cone and \(\operatorname{Proj}(M)\) its set of projections.
- A sum of numbers in \([0,\infty]\) over any index set is the supremum of its finite partial sums, and \(0\cdot\infty=0\).
- A norm-bounded increasing net \((x_i)\) in \(M_+\) has a least upper bound \(x\in M_+\), and \(x_i\to x\) strongly. We write \(x_i\uparrow x\), and \(x_i\downarrow x\) for decreasing nets.
- For \(x\in M_+\), \(s(x)\) is the projection onto the closure of \(xH\). It lies in \(M\), and \(s(x)=\sup_n1_{[1/n,\infty)}(x)\). The central support \(c(e)\) of a projection \(e\) is the smallest central projection that majorizes \(e\); it is the projection onto the closed span \([MeH]\). For \(x\in M_+\) put \(c(x)=c(s(x))\). Then \(xc(x)=x\), and for a central projection \(q\) we have \(xq=0\) exactly when \(qc(x)=0\).
- Projections \(e,f\) are *equivalent*, \(e\sim f\), if \(v^*v=e\) and \(vv^*=f\) for some \(v\in M\). We write \(e\precsim f\) if \(e\sim f'\) for some projection \(f'\leq f\), and \(e\prec f\) if \(e\precsim f\) but not \(e\sim f\).
- A projection \(e\) is *finite* if \(e\sim f\leq e\) forces \(f=e\). It is *properly infinite* if \(ze\) is infinite for every central projection \(z\) with \(ze\neq0\), and *abelian* if \(eMe\) is commutative. \(M\) is finite, or properly infinite, when \(1\) is.
- \(M\) is *of type I* if every nonzero central projection majorizes a nonzero abelian projection; *of type II* if \(0\) is its only abelian projection while every nonzero central projection majorizes a nonzero finite projection; and *of type III* if \(0\) is its only finite projection. An algebra of type II is *of type II\(_1\)* if it is finite, and *of type II\(_\infty\)* if \(0\) is its only finite central projection. \(M\) is *semifinite* when it has no nonzero central summand of type III.
- For a projection \(e\), the corner \(eMe\) is a von Neumann algebra on \(eH\) with unit \(e\). Its projections are the projections of \(M\) below \(e\), and two of them are equivalent in \(eMe\) exactly when they are equivalent in \(M\).
- \(M_*\) is the space of \(\sigma\)-weakly continuous linear functionals on \(M\), and \(M=(M_*)^*\). A positive linear functional \(\varphi\) on \(M\) is *normal* if \(\varphi(x_i)\uparrow\varphi(x)\) whenever \(x_i\uparrow x\). The normal positive functionals are exactly the elements of \(M_*^+\) (see "Normal functionals" in the list below).
- \(M\) is *\(\sigma\)-finite* if every family of mutually orthogonal nonzero projections in \(M\) is countable.

Standard background, used without comment: the bounded Borel functional calculus (spectral projections of self-adjoint elements of \(M\) lie in \(M\)); the polar decomposition \(x=u|x|\) with \(u,|x|\in M\) (proved in [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-09)); the bicommutant theorem; the \(\sigma\)-weak compactness of the closed balls of \(M\); on bounded sets, strong convergence implies \(\sigma\)-weak convergence; the Hahn–Banach theorem and Mazur's theorem (a norm-closed convex set in a Banach space is weakly closed); Zorn's lemma; and the Cauchy–Schwarz inequality \(|\varphi(y^*x)|^2\leq\varphi(x^*x)\varphi(y^*y)\) for positive functionals.

## Background used without proof

The following results are used as stated. In the proofs we refer to each of them by its name.

*Comparison of projections.* These facts are proved in [Projections and types of von Neumann algebras](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html).

- **Schröder–Bernstein for projections.** If \(e\precsim f\) and \(f\precsim e\), then \(e\sim f\).
- **Equivalent pieces.** If \(c(e)c(f)\neq0\), there are nonzero projections \(e_1\leq e\) and \(f_1\leq f\) with \(e_1\sim f_1\).
- **The comparison theorem.** For projections \(e,f\) there is a central projection \(h\) with \(he\precsim hf\) and \((1-h)f\precsim(1-h)e\).
- **The type decomposition.** \(M\) is the direct sum of its parts of type I, II\(_1\), II\(_\infty\) and III, cut out by central projections \(z_{\rm I},z_{{\rm II}_1},z_{{\rm II}_\infty},z_{\rm III}\) with sum \(1\). Every projection is uniquely the sum of two centrally orthogonal projections, one finite and one properly infinite.
- **Abelian projections are smallest.** If \(e\) is abelian and \(c(f)\geq e\), then \(e\precsim f\). *Reference:* [Takesaki I, Lemma V.1.25] states the relation the other way round; that version fails for \(M_2(\mathbb C)\) with \(e=e_{11}\) and \(f=1\).
- **Structure of type I algebras.** If \(M\) is of type I, then \(1=\sum_\alpha z_\alpha\), where \(\alpha\) runs over the nonzero cardinals, the \(z_\alpha\) are mutually orthogonal central projections, and \(z_\alpha\) is a sum of \(\alpha\) orthogonal abelian projections each with central support \(z_\alpha\). If \(M\) is finite, \(z_\alpha=0\) for every infinite \(\alpha\).
- **Type I factors.** A factor of type I is \(*\)-isomorphic to \(B(K)\) for some Hilbert space \(K\).
- **Halving.** If \(M\) has no direct summand of type I, every projection is the sum of two orthogonal equivalent projections.
- **Halving a properly infinite algebra.** If \(M\) is properly infinite, there is a projection \(e\) with \(e\sim1-e\sim1\).
- **Finite projections form a lattice.** If \(e\) and \(f\) are finite, so is \(e\vee f\).
- **Complements of equivalent finite projections.** If \(e,f\) are finite and \(e\sim f\), then \(1-e\sim1-f\).
- **Properly infinite semifinite algebras.** A properly infinite semifinite \(M\) has orthogonal central projections \(z_\alpha\), indexed by infinite cardinals, with \(\sum_\alpha z_\alpha=1\) and \(Mz_\alpha\cong N_\alpha\bar\otimes B(H_\alpha)\), where \(N_\alpha\) is finite and \(\dim H_\alpha=\alpha\). This is used only in Section 5, where we prove that the \(z_\alpha\) are unique.

*Ideals and functionals.*

- **\(\sigma\)-weakly closed ideals.** Every two-sided ideal of \(M\) that is closed in the \(\sigma\)-weak topology equals \(Mz\) for exactly one central projection \(z\). This is proved in [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-11).
- **Normal functionals.** A bounded linear functional on \(M\) lies in \(M_*\) exactly when it is completely additive on orthogonal families of projections. For a positive functional, preserving suprema of bounded increasing nets implies complete additivity, and membership in \(M_*\) implies preserving such suprema; so the two notions of normality agree. The first statement is proved in [The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-25).
- **Positive parts of normal functionals.** A hermitian element of \(M_*\) is the difference of two elements of \(M_*^+\). Hence \(M_*\) is spanned by \(M_*^+\). This follows from the Jordan decomposition of a hermitian functional and the splitting of functionals into normal and singular parts, both proved in [the same lesson](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-10).
- **Akemann's weak compactness criterion.** Let \(K\subseteq M_*\) be bounded, and suppose that \(\sup_{\psi\in K}|\psi(p_n)|\to0\) for every decreasing sequence of projections \(p_n\) with infimum \(0\). Then \(K\) is relatively \(\sigma(M_*,M)\)-compact. *Reference:* [Akemann 1967].
- **Tensor products of isomorphisms.** If \(\pi_1:M_1\to N_1\) and \(\pi_2:M_2\to N_2\) are \(*\)-isomorphisms of von Neumann algebras, there is a \(*\)-isomorphism of \(M_1\bar\otimes M_2\) onto \(N_1\bar\otimes N_2\) that sends \(x_1\otimes x_2\) to \(\pi_1(x_1)\otimes\pi_2(x_2)\). This is proved in [Spatial tensor products of von Neumann algebras](../reader/supplements/spatial-tensor-products.html#8-maps-between-tensor-products-and-normal-homomorphisms); recall that a \(*\)-isomorphism of von Neumann algebras and its inverse are normal.
- **The fixed point theorem of Ryll-Nardzewski.** If \(Q\) is a nonempty weakly compact convex subset of a Banach space and \(G\) is a group of linear isometries of the space with \(g(Q)\subseteq Q\) for \(g\in G\), then some point of \(Q\) is fixed by every \(g\in G\). *Reference:* [Ryll-Nardzewski 1967]; a short proof is in [Namioka–Asplund 1967].

## 1. Facts about projections

This section proves the facts about projections that the later sections use.

**Lemma 1.1** (Orthogonal sums). Let \((e_i)\) and \((f_i)\) be families of mutually orthogonal projections with \(e_i\sim f_i\) for each \(i\). Then \(\sum_ie_i\sim\sum_if_i\). The same holds with \(\precsim\) in place of \(\sim\).

**Proof.** Choose \(v_i\) with \(v_i^*v_i=e_i\) and \(v_iv_i^*=f_i\). Their initial spaces are orthogonal and so are their final spaces, so \(\sum_iv_i\) converges strongly to a partial isometry \(v\) with \(v^*v=\sum_ie_i\) and \(vv^*=\sum_if_i\). For \(\precsim\), apply this to \(e_i\sim f_i'\leq f_i\). \(\square\)

**Lemma 1.2** (Central cuts and invariance). If \(e\sim f\) through \(v\) and \(z\) is a central projection, then \(ze\sim zf\) through \(vz\). Hence \(c(e)=c(f)\), and \(e\precsim f\) implies \(ze\precsim zf\). A projection equivalent to a finite projection is finite, and a subprojection of a finite projection is finite. A projection equivalent to a properly infinite projection is properly infinite.

**Proof.** Since \(z\) is central, \((vz)^*(vz)=ze\) and \((vz)(vz)^*=zf\). If a central projection \(z\) majorizes \(e\), then \((1-z)f\sim(1-z)e=0\), so \(z\) majorizes \(f\). Thus \(c(f)\leq c(e)\), and by symmetry \(c(e)=c(f)\).

Let \(f\) be finite and \(e\sim f\) through \(v\). If \(e\sim e'\leq e\), then \(f\sim ve'v^*\leq f\), so \(ve'v^*=f\) and \(e'=v^*(ve'v^*)v=v^*fv=e\). So \(e\) is finite.

Let \(f\) be finite, \(g\leq f\) and \(g\sim g'\leq g\). By Lemma 1.1, \(f=g+(f-g)\sim g'+(f-g)\leq f\), so \(g'+(f-g)=f\) and \(g'=g\). So \(g\) is finite.

For the last claim, let \(e\sim f\) with \(f\) properly infinite, and let \(z\) be central. By the first sentence, \(ze\sim zf\). So \(ze\neq0\) exactly when \(zf\neq0\), and, by the second claim, \(ze\) is finite exactly when \(zf\) is. \(\square\)

**Lemma 1.3** (Parallelogram law). For projections \(e,f\), \(\;e\vee f-e\sim f-e\wedge f\).

**Proof.** Put \(w=(1-e)f\in M\). Its range is \((1-e)fH=(1-e)(eH+fH)\). The space \(eH+fH\) is dense in \((e\vee f)H\), and on \((e\vee f)H\) the operator \(1-e\) acts as the projection \(e\vee f-e\). So the range of \(w\) is dense in \((e\vee f-e)H\), and the left support of \(w\) is \(e\vee f-e\). A vector \(\xi\) is in the kernel of \(w\) exactly when \(f\xi\in eH\), that is, when \(f\xi\in(e\wedge f)H\). So the kernel of \(w\) is \((1-f)H\oplus(e\wedge f)H\), and the right support of \(w\) is \(f-e\wedge f\). If \(w=u|w|\) is the polar decomposition, \(u^*u\) is the right support and \(uu^*\) the left support, so \(u\) implements the equivalence. \(\square\)

**Lemma 1.4** (Four unitaries). Every element of \(M\) is a linear combination of four unitaries of \(M\). Consequently an element of \(M\) that commutes with every unitary of \(M\) is central.

**Proof.** If \(h=h^*\) and \(\|h\|\leq1\), then \(u=h+i(1-h^2)^{1/2}\) is unitary and \(h=(u+u^*)/2\). A general element is a combination of its real and imaginary parts, after scaling. So an element that commutes with every unitary commutes with all of \(M\), and it lies in \(M\cap M'=\mathcal Z\). \(\square\)

**Lemma 1.5** (Corners). Let \(e\) be a projection. The center of \(eMe\) is \(\mathcal Ze\), and \(a\mapsto ae\) is a \(*\)-isomorphism of \(\mathcal Zc(e)\) onto \(\mathcal Ze\). Consequently the central projections of \(eMe\) are the \(ze\) with \(z\) a central projection of \(M\), and \(e\) is finite, or properly infinite, exactly when the algebra \(eMe\) is.

The same computation of the center of a reduced algebra appears in [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-08).

**Proof.** Every \(ae\) with \(a\in\mathcal Z\) is central in \(eMe\), because \(a\) commutes with \(M\).

Conversely, let \(y\) be central in \(eMe\). Let \(D\) be the span of the vectors \(xe\xi\) with \(x\in M\) and \(\xi\in H\). We want to define an operator \(Y\) on \(D\) by \(Y(\sum_kx_ke\xi_k)=\sum_kx_ky\xi_k\), and we first show that this is well defined and bounded. Fix finitely many \(x_k\in M\) and \(\xi_k\in H\). Let \(A\) be the positive matrix \([ex_l^*x_ke]_{l,k}\) over \(eMe\), and let \(D_y\) be the diagonal matrix with \(y^*y\) in each diagonal place. Since \(y^*y\) is central in \(eMe\), \(D_y\) is central in the matrix algebra over \(eMe\). So \(D_y\) commutes with \(A\) and with \(A^{1/2}\), and \(AD_y=A^{1/2}D_yA^{1/2}\leq\|y\|^2A\). With \(\vec\xi=(e\xi_k)_k\), and using \(y=eye\),
\[
\Bigl\|\sum_kx_ky\xi_k\Bigr\|^2=\langle AD_y\vec\xi,\vec\xi\rangle\leq\|y\|^2\langle A\vec\xi,\vec\xi\rangle=\|y\|^2\Bigl\|\sum_kx_ke\xi_k\Bigr\|^2 .
\]
So \(Y\) is well defined and bounded on \(D\). The closure of \(D\) is \(c(e)H\), because \(c(e)\) is the projection onto \([MeH]\). Extend \(Y\) by continuity to \(c(e)H\), and by \(0\) on \((1-c(e))H\).

Now let \(b\in M'\) and \(m\in M\). On \(D\), \(Y\) commutes with \(b\) and with \(m\): for instance \(Yb(xe\xi)=Y(xe\,b\xi)=xyb\xi=bxy\xi=bY(xe\xi)\), and \(Ym(xe\xi)=mxy\xi=mY(xe\xi)\). All these operators leave \((1-c(e))H\) invariant, since \(c(e)\) is central, and \(Y\) vanishes there. So \(Y\) commutes with \(M'\) and with \(M\), that is, \(Y\in M\cap M'=\mathcal Z\). Taking \(x=1\) in the definition gives \(Ye\xi=y\xi\) for all \(\xi\), that is, \(y=Ye\).

The map \(a\mapsto ae\) is injective on \(\mathcal Zc(e)\): if \(a\in\mathcal Zc(e)\) and \(ae=0\), then \(axe\xi=xae\xi=0\), so \(a\) vanishes on \(c(e)H\), and \(a=0\).

For the consequences: a central projection \(y\) of \(eMe\) is \(Ye\) with \(Y\in\mathcal Zc(e)\), and since \(a\mapsto ae\) is an injective \(*\)-homomorphism, \(Y\) is a projection. Finally, finiteness of \(ze\) is the same notion in \(eMe\) and in \(M\), because the projections of \(eMe\) and their equivalences are those of \(M\) below \(e\). \(\square\)

**Proposition 1.6** (Three consequences of the type decomposition).

(a) A finite algebra has no parts of type II\(_\infty\) or III, so \(M=Mz_{\rm I}\oplus Mz_{{\rm II}_1}\), and \(z_{\rm I}=\sum_{n\geq1}z_n\) with \(z_n\) a sum of \(n\) orthogonal abelian projections each of central support \(z_n\).

(b) For every \(M\) there are central projections \(z_f,z_\infty\) with \(z_f+z_\infty=1\), \(Mz_f\) finite and \(Mz_\infty\) properly infinite (either may be zero).

(c) \(M\) is semifinite exactly when each nonzero central projection lies above some nonzero finite projection, and exactly when each nonzero projection does.

**Proof.** (a) The projection \(z_{\rm III}\) lies below the finite projection \(1\), so it is finite by Lemma 1.2. The type III part has no nonzero finite projection, so \(z_{\rm III}=0\). Likewise \(z_{{\rm II}_\infty}\) is finite, and it is a central projection of the type II\(_\infty\) part, which has no nonzero finite central projection; so \(z_{{\rm II}_\infty}=0\). The rest is the structure of type I algebras, applied to the finite algebra \(Mz_{\rm I}\).

(b) By the type decomposition, \(1=e_1+e_2\) with \(e_1\) finite, \(e_2\) properly infinite and \(c(e_1)c(e_2)=0\). Then \(c(e_1)e_2=c(e_1)c(e_2)e_2=0\), so \(c(e_1)=c(e_1)(e_1+e_2)=e_1\), and \(e_1\) is central. Put \(z_f=e_1\) and \(z_\infty=e_2\). The algebra \(Mz_\infty\) is properly infinite by Lemma 1.5.

(c) An abelian projection is finite: if \(e\) is abelian and \(e\sim f\leq e\) through \(v\), then \(v=fve\in eMe\), so \(v^*v=vv^*\) and \(f=e\). Let \(M\) be semifinite and \(z\neq0\) central. If \(zz_{\rm I}\neq0\), the definition of type I gives a nonzero abelian, hence finite, projection below \(zz_{\rm I}\). Otherwise \(z(z_{{\rm II}_1}+z_{{\rm II}_\infty})=z\neq0\), because \(z_{\rm III}=0\), and the definition of type II gives a nonzero finite projection below it. Now let \(e\neq0\) be a projection. By what we just proved, there is a nonzero finite \(g\leq c(e)\). Since \(c(g)\leq c(e)\), \(c(g)c(e)=c(g)\neq0\), and the equivalent-pieces fact gives nonzero \(g'\leq g\) and \(e'\leq e\) with \(g'\sim e'\). By Lemma 1.2, \(g'\) is finite, and so is \(e'\). Conversely, if each nonzero central projection lies above some nonzero finite projection, then \(z_{\rm III}=0\), because the type III part has no nonzero finite projection. \(\square\)

## 2. Traces and the definition ideal

### Definition and first properties

**Definition 2.1.** A *trace* on \(M\) is a map \(\tau:M_+\to[0,\infty]\) such that, for \(x,y\in M_+\), \(\lambda\geq0\) and \(z\in M\),
\[
\tau(x+y)=\tau(x)+\tau(y),\qquad \tau(\lambda x)=\lambda\tau(x),\qquad \tau(z^*z)=\tau(zz^*).
\tag{2.1}
\]
It is *faithful* if \(\tau(x)>0\) for every nonzero \(x\in M_+\); *finite* if \(\tau(1)<\infty\); *semifinite* if every nonzero \(x\in M_+\) majorizes a nonzero \(y\in M_+\) with \(\tau(y)<\infty\); and *normal* if \(\tau(x_i)\uparrow\tau(x)\) whenever \(x_i\uparrow x\) in \(M_+\).

A map \(M_+\to[0,\infty]\) with the first two properties in (2.1) is called a *weight*. So a trace is a weight with the extra identity \(\tau(z^*z)=\tau(zz^*)\). For weights, semifiniteness can also be defined by density of the finite domain; Proposition 2.5 shows that for traces the two definitions agree.

**Proposition 2.2.** Let \(\tau\) be a trace on \(M\).

1. If \(0\leq x\leq y\), then \(\tau(x)\leq\tau(y)\).
2. If \(v\) is a partial isometry and \(x\in M_+\) satisfies \(x=(v^*v)x(v^*v)\), then \(\tau(vxv^*)=\tau(x)\). In particular \(\tau(uxu^*)=\tau(x)\) for every unitary \(u\).
3. If \(e\sim f\), then \(\tau(e)=\tau(f)\). If \(e\precsim f\), then \(\tau(e)\leq\tau(f)\).
4. \(\tau(e)+\tau(f)=\tau(e\vee f)+\tau(e\wedge f)\) for projections \(e,f\), as an identity in \([0,\infty]\).
5. For a central projection \(z\), \(xz\leq x\) for \(x\in M_+\), and \(\tau_z(x)=\tau(xz)\) defines a trace, which is normal if \(\tau\) is.
6. (*Finite traces.*) If \(\tau\) is finite, exactly one positive linear functional on \(M\) agrees with \(\tau\) on \(M_+\); we write it \(\tau\) again, and \(\tau(xy)=\tau(yx)\) for all \(x,y\in M\). Conversely, a positive linear functional \(\varphi\) with \(\varphi(uxu^*)=\varphi(x)\) for all unitaries \(u\) and all \(x\), or with \(\varphi(z^*z)=\varphi(zz^*)\) for all \(z\), restricts to a finite trace. A finite trace is normal exactly when its extension lies in \(M_*\).

**Proof.** (1) Since \(y=x+(y-x)\) with \(y-x\in M_+\), additivity gives \(\tau(y)=\tau(x)+\tau(y-x)\geq\tau(x)\).

(2) Put \(p=v^*v\). Since \(x=pxp\), also \(x^{1/2}=px^{1/2}p\), because \(x^{1/2}\) is a norm limit of polynomials in \(x\) without constant term. With \(z=vx^{1/2}\), (2.1) gives \(\tau(vxv^*)=\tau(zz^*)=\tau(z^*z)=\tau(x^{1/2}px^{1/2})=\tau(x)\).

(3) If \(v^*v=e\) and \(vv^*=f\), apply (2) with \(x=e\). The second claim then follows from (1).

(4) Write \(e\vee f=e+(e\vee f-e)\) and \(f=e\wedge f+(f-e\wedge f)\), with orthogonal summands. By the parallelogram law (Lemma 1.3) and part (3), \(\tau(e\vee f-e)=\tau(f-e\wedge f)\). Hence
\(\tau(e\vee f)+\tau(e\wedge f)=\tau(e)+\tau(f-e\wedge f)+\tau(e\wedge f)=\tau(e)+\tau(f)\). Only additions occur, so infinite values cause no trouble.

(5) Since \(z\) is central, \(xz=x^{1/2}zx^{1/2}\leq x\). Additivity and homogeneity of \(\tau_z\) are clear. For \(w\in M\), \(\tau_z(w^*w)=\tau((wz)^*(wz))=\tau((wz)(wz)^*)=\tau_z(ww^*)\). If \(x_i\uparrow x\), then \(x_iz\uparrow xz\).

(6) Every element of \(M\) is a combination of positive elements, and \(\tau(x^*x)\leq\|x\|^2\tau(1)<\infty\). So the definition ideal of Definition 2.3 below is all of \(M\), and Lemma 2.4(3) gives the extension and \(\tau(xy)=\tau(yx)\) for all \(x,y\). Conversely, if \(\varphi(uxu^*)=\varphi(x)\) for all \(u\) and \(x\), then \(\varphi(ux)=\varphi(u(xu)u^*)=\varphi(xu)\). Every \(y\in M\) is a combination of unitaries (Lemma 1.4), so \(\varphi(yx)=\varphi(xy)\), and in particular \(\varphi(z^*z)=\varphi(zz^*)\). The last sentence holds because the two notions of normality agree for positive functionals (see "Normal functionals" in the background list). \(\square\)

### The definition ideal

**Definition 2.3.** For a trace \(\tau\) put
\[
F_\tau=\{x\in M_+:\tau(x)<\infty\},\qquad
\mathfrak n_\tau=\{x\in M :\tau(x^*x)<\infty\},\qquad
\mathfrak m_\tau=\operatorname{span}\{y^*x:x,y\in\mathfrak n_\tau\}.
\tag{2.2}
\]
We call \(\mathfrak m_\tau\) the *definition ideal* of \(\tau\).

**Lemma 2.4.** Let \(\tau\) be any trace on \(M\). No normality, faithfulness or semifiniteness is assumed.

1. \(\mathfrak n_\tau\) is a two-sided ideal with \(\mathfrak n_\tau^*=\mathfrak n_\tau\). \(\mathfrak m_\tau\) is a two-sided ideal with \(\mathfrak m_\tau^*=\mathfrak m_\tau\) and \(\mathfrak m_\tau\subseteq\mathfrak n_\tau\).
2. \(\mathfrak m_\tau\cap M_+=F_\tau\) and \(\mathfrak m_\tau=\operatorname{span}F_\tau\). Every self-adjoint element of \(\mathfrak m_\tau\) is \(a-b\) with \(a,b\in F_\tau\).
3. \(\tau|_{F_\tau}\) extends uniquely to a linear functional \(\dot\tau\) on \(\mathfrak m_\tau\), and
\[
\dot\tau(x^*)=\overline{\dot\tau(x)}\ (x\in\mathfrak m_\tau),\qquad
\dot\tau(xy)=\dot\tau(yx)\ (x,y\in\mathfrak n_\tau),\qquad
\dot\tau(ax)=\dot\tau(xa)\ (x\in\mathfrak m_\tau,\ a\in M).
\tag{2.3}
\]
4. \(x\in\mathfrak m_\tau\iff|x|\in\mathfrak m_\tau\iff|x^*|\in\mathfrak m_\tau\), and \(x\in\mathfrak n_\tau\iff|x|\in\mathfrak n_\tau\). Every element of \(\mathfrak m_\tau\) is a single product \(yz\) with \(y,z\in\mathfrak n_\tau\), so \(\mathfrak m_\tau=\{yz:y,z\in\mathfrak n_\tau\}\).

**Proof.** (1) For \(x,y\in M\),
\((x+y)^*(x+y)\leq(x+y)^*(x+y)+(x-y)^*(x-y)=2x^*x+2y^*y\), and \((ax)^*(ax)=x^*a^*ax\leq\|a\|^2x^*x\). With Proposition 2.2(1) these show that \(\mathfrak n_\tau\) is a linear subspace and a left ideal. By (2.1), \(\tau(xx^*)=\tau(x^*x)\), so \(\mathfrak n_\tau^*=\mathfrak n_\tau\), and \(\mathfrak n_\tau\) is also a right ideal. For \(a\in M\) and \(x,y\in\mathfrak n_\tau\), \(a(y^*x)=(ya^*)^*x\) and \((y^*x)a=y^*(xa)\) with \(ya^*,xa\in\mathfrak n_\tau\), and \((y^*x)^*=x^*y\). So \(\mathfrak m_\tau\) is a self-adjoint two-sided ideal. Finally \(y^*\in\mathfrak n_\tau\), so \(y^*x\in\mathfrak n_\tau\).

(2) In any \(*\)-algebra,
\[
4y^*x=\sum_{k=0}^3i^k(x+i^ky)^*(x+i^ky),
\tag{2.4}
\]
as one sees by expanding and using \(\sum_ki^k=\sum_ki^{2k}=0\). For \(x,y\in\mathfrak n_\tau\), each \(x+i^ky\) lies in \(\mathfrak n_\tau\), so each \((x+i^ky)^*(x+i^ky)\) lies in \(F_\tau\). Hence \(\mathfrak m_\tau\subseteq\operatorname{span}F_\tau\). If \(a\in F_\tau\), then \(a^{1/2}\in\mathfrak n_\tau\) and \(a=(a^{1/2})^*a^{1/2}\in\mathfrak m_\tau\). So \(\mathfrak m_\tau=\operatorname{span}F_\tau\). If \(h=\sum_kc_ka_k\) is self-adjoint, with \(a_k\in F_\tau\), then \(h=(h+h^*)/2=\sum_k(\operatorname{Re}c_k)a_k\). This is \(a-b\), where \(a\) collects the terms with \(\operatorname{Re}c_k>0\) and \(b\) the terms with \(\operatorname{Re}c_k<0\) (with coefficient \(|\operatorname{Re}c_k|\)); both lie in \(F_\tau\). If moreover \(h\geq0\), then \(0\leq h\leq a\), so \(\tau(h)\leq\tau(a)<\infty\) and \(h\in F_\tau\).

(3) If \(a-b=a'-b'\) with \(a,b,a',b'\in F_\tau\), then \(a+b'=a'+b\), so \(\tau(a)+\tau(b')=\tau(a')+\tau(b)\). All four numbers are finite, so \(\tau(a)-\tau(b)=\tau(a')-\tau(b')\). Hence \(\dot\tau(a-b)=\tau(a)-\tau(b)\) is well defined on the self-adjoint part of \(\mathfrak m_\tau\), and it is additive and real-homogeneous there. Extend it by \(\dot\tau(h+ik)=\dot\tau(h)+i\dot\tau(k)\) for self-adjoint \(h,k\in\mathfrak m_\tau\). The result is linear, agrees with \(\tau\) on \(F_\tau\), satisfies \(\dot\tau(x^*)=\overline{\dot\tau(x)}\), and is unique because \(\mathfrak m_\tau=\operatorname{span}F_\tau\).

For \(x\in\mathfrak n_\tau\), (2.1) says \(\dot\tau(x^*x)=\dot\tau(xx^*)\). Besides (2.4) there is the mirror identity
\[
4xy^*=\sum_{k=0}^3i^k(x+i^ky)(x+i^ky)^*.
\tag{2.5}
\]
For \(x,y\in\mathfrak n_\tau\), the right sides of (2.4) and (2.5) have equal traces term by term, so \(\dot\tau(y^*x)=\dot\tau(xy^*)\). Replacing \(y\) by \(y^*\) gives \(\dot\tau(yx)=\dot\tau(xy)\) for \(x,y\in\mathfrak n_\tau\). Now let \(a\in M\) and \(x,y\in\mathfrak n_\tau\). Since \(ya^*,xa\in\mathfrak n_\tau\),
\[
\dot\tau(a\,y^*x)=\dot\tau((ya^*)^*x)=\dot\tau(x(ya^*)^*)=\dot\tau((xa)y^*)=\dot\tau(y^*(xa))=\dot\tau(y^*x\,a).
\]
By linearity \(\dot\tau(aw)=\dot\tau(wa)\) for every \(w\in\mathfrak m_\tau\).

(4) Let \(x=u|x|\) be the polar decomposition. Then \(|x|=u^*x\), \(x=u|x|\), \(|x^*|=u|x|u^*\) and \(|x|=u^*|x^*|u\). Since \(\mathfrak m_\tau\) and \(\mathfrak n_\tau\) are two-sided ideals, \(x\in\mathfrak m_\tau\iff|x|\in\mathfrak m_\tau\iff|x^*|\in\mathfrak m_\tau\). As \(x^*x=|x|^*|x|\), \(x\in\mathfrak n_\tau\iff|x|\in\mathfrak n_\tau\). If \(x\in\mathfrak m_\tau\), then \(|x|\in\mathfrak m_\tau\cap M_+=F_\tau\), so \(|x|^{1/2}\in\mathfrak n_\tau\) and \(x=(u|x|^{1/2})\,|x|^{1/2}\) with both factors in \(\mathfrak n_\tau\). Conversely \(yz=(y^*)^*z\in\mathfrak m_\tau\) for \(y,z\in\mathfrak n_\tau\). \(\square\)

**Remarks.** (1) The proof uses only the identities (2.1). From now on we write \(\tau(x)\) for \(\dot\tau(x)\) when \(x\in\mathfrak m_\tau\). (2) For a weight \(\varphi\), the sets \(\mathfrak n_\varphi\) and \(\mathfrak m_\varphi\) are defined in the same way, and part (2) and the extension in part (3) still hold. But \(\mathfrak n_\varphi\) is only a left ideal, and \(\mathfrak m_\varphi\) only a \(*\)-subalgebra.

### Equivalent forms of semifiniteness

**Proposition 2.5.** For a trace \(\tau\) on \(M\) the following are equivalent. Normality is not needed.

- (a) \(\tau\) is semifinite in the sense of Definition 2.1.
- (b) Below each nonzero projection there is a nonzero projection of finite trace.
- (c) There is an increasing net of projections \(e_i\) with \(\tau(e_i)<\infty\) and \(e_i\uparrow1\).
- (d) There is an increasing net of positive contractions \(a_i\in F_\tau\) with \(a_i\uparrow1\).
- (e) \(\mathfrak m_\tau\) is \(\sigma\)-weakly dense in \(M\). This is the usual definition of semifiniteness for weights.

**Proof.** (a)\(\Rightarrow\)(b). Let \(e\neq0\) be a projection and \(0\neq y\leq e\) with \(\tau(y)<\infty\). From \(0\leq y\leq e\) we get \((1-e)y(1-e)\leq(1-e)e(1-e)=0\), so \(y^{1/2}(1-e)=0\). Hence \(y=eye\) and \(s(y)\leq e\). Put \(f=1_{[\|y\|/2,\infty)}(y)\). Then \(0\neq f\leq s(y)\leq e\) and \((\|y\|/2)f\leq y\), so \(\tau(f)\leq2\tau(y)/\|y\|<\infty\).

(b)\(\Rightarrow\)(c). By Zorn's lemma choose a maximal family \((f_k)\) of mutually orthogonal nonzero projections of finite trace. If \(1-\sum_kf_k\neq0\), (b) gives a nonzero projection of finite trace below it, against maximality. So \(\sum_kf_k=1\). The finite partial sums \(e_F=\sum_{k\in F}f_k\) increase to \(1\), and \(\tau(e_F)=\sum_{k\in F}\tau(f_k)<\infty\).

(c)\(\Rightarrow\)(d). Take \(a_i=e_i\).

(d)\(\Rightarrow\)(e). Since \(a_i^2\leq a_i\), each \(a_i\) lies in \(\mathfrak n_\tau\). For \(x\in M\), \(xa_i\in\mathfrak n_\tau\), so \(a_ixa_i=a_i^*(xa_i)\in\mathfrak m_\tau\). Also \(\|(a_ixa_i-x)\xi\|\leq\|x\|\,\|(a_i-1)\xi\|+\|(a_i-1)x\xi\|\to0\). So \(a_ixa_i\to x\) strongly and with bounded norms, hence \(\sigma\)-weakly.

(e)\(\Rightarrow\)(a). Let \(0\neq x\in M_+\). If \(x^{1/2}ax^{1/2}=0\) for all \(a\in F_\tau\), then \(x^{1/2}\mathfrak m_\tau x^{1/2}=0\), because \(\mathfrak m_\tau=\operatorname{span}F_\tau\) by Lemma 2.4(2). The map \(b\mapsto x^{1/2}bx^{1/2}\) is \(\sigma\)-weakly continuous, so (e) gives \(x^{1/2}Mx^{1/2}=0\), and \(x=x^{1/2}\cdot1\cdot x^{1/2}=0\), a contradiction. So choose \(a\in F_\tau\) with \(x^{1/2}ax^{1/2}\neq0\), and put \(y=\|a\|^{-1}x^{1/2}ax^{1/2}\). Then \(0\neq y\leq x\). With \(w=a^{1/2}x^{1/2}\), (2.1) gives \(\tau(x^{1/2}ax^{1/2})=\tau(w^*w)=\tau(ww^*)=\tau(a^{1/2}xa^{1/2})\leq\|x\|\tau(a)<\infty\). \(\square\)

**Remarks.** (1) For weights, (e) does not imply (a). Let \((u_n)_{n\geq1}\) be an orthonormal basis of \(\ell^2(\mathbb N)\), and put \(\varphi(a)=\sum_nn^2\langle au_n,u_n\rangle\) for \(a\in B(\ell^2(\mathbb N))_+\). This weight is faithful and normal. It satisfies (e): the projections onto the first \(N\) basis vectors have finite weight and increase to \(1\), and the argument for (d)\(\Rightarrow\)(e) applies. Now choose \(c>0\) so that \(v=\sum_n(c/n)u_n\) is a unit vector, and let \(q\) be the projection onto \(\mathbb Cv\). Every \(b\) with \(0\leq b\leq q\) is a multiple \(tq\) with \(0\leq t\leq1\), and \(\varphi(q)=\sum_nn^2(c^2/n^2)=\infty\). So \(q\) majorizes no nonzero element of finite weight. For traces, the identity \(\tau(z^*z)=\tau(zz^*)\) enters the proof above only in its last line. (2) From now on "semifinite" may be read in any of the five forms. For a central projection \(z\), "\(\tau\) is semifinite on \(Mz\)" means that the restriction of \(\tau\) to \((Mz)_+\), which is a trace on the von Neumann algebra \(Mz\), is semifinite.

## 3. Supports, sums and semifinite parts

### Null projections and the support of a normal trace

A weight \(\varphi\) is *normal* if \(\varphi(x_i)\uparrow\varphi(x)\) whenever \(x_i\uparrow x\). Normal positive functionals and normal traces are examples.

**Lemma 3.1.** Let \(\varphi\) be a normal weight on \(M\), and let \(\mathcal N_\varphi\) be the set of projections \(e\) with \(\varphi(e)=0\).

1. \(\mathcal N_\varphi\) is upward directed, and \(p_\varphi=\sup\mathcal N_\varphi\) lies in \(\mathcal N_\varphi\).
2. \(\varphi(x)=0\) for every \(x\in M_+\) with \(x=p_\varphi xp_\varphi\).
3. \(\varphi(x)>0\) for every nonzero \(x\in M_+\) with \(x=(1-p_\varphi)x(1-p_\varphi)\).
4. If \(\varphi\) is a normal positive functional and \(s=1-p_\varphi\), then \(\varphi(x)=\varphi(sxs)\) for all \(x\in M\). (This \(s\) is the usual support of \(\varphi\).)

**Proof.** (1) Let \(e,f\in\mathcal N_\varphi\). Then \(\varphi(e+f)=0\). For \(n\geq1\) the projection \(1_{[1/n,\infty)}(e+f)\) is at most \(n(e+f)\), so it lies in \(\mathcal N_\varphi\). These projections increase to \(s(e+f)\), and normality gives \(\varphi(s(e+f))=0\). Moreover \(s(e+f)=e\vee f\): since \(\langle(e+f)\xi,\xi\rangle=\|e\xi\|^2+\|f\xi\|^2\), the kernel of \(e+f\) is the intersection of the kernels of \(e\) and \(f\). So \(\mathcal N_\varphi\) is upward directed. Indexed by itself, it is an increasing net with supremum \(p_\varphi\), and normality gives \(\varphi(p_\varphi)=0\).

(2) Such an \(x\) satisfies \(x\leq\|x\|p_\varphi\), so \(\varphi(x)\leq\|x\|\varphi(p_\varphi)=0\).

(3) If \(x\neq0\), the projection \(f=1_{[\|x\|/2,\infty)}(x)\) is nonzero, \(f\leq s(x)\leq1-p_\varphi\) and \((\|x\|/2)f\leq x\). If \(\varphi(x)=0\), then \(\varphi(f)=0\), so \(f\leq p_\varphi\) and \(f=0\), a contradiction.

(4) By Cauchy–Schwarz, \(|\varphi(x(1-s))|^2\leq\varphi(xx^*)\varphi(1-s)=0\), and in the same way \(\varphi((1-s)x)=0\). Hence \(\varphi(x)=\varphi(sx)=\varphi(sxs)\). \(\square\)

**Proposition 3.2.** Let \(\tau\) be a normal trace on \(M\). Then \(p_\tau\) is central. Put \(s(\tau)=1-p_\tau\). Then \(s(\tau)\) is the unique central projection \(z\) such that \(\tau\) vanishes on \(M_+(1-z)\) and \(\tau\) is faithful on \(Mz\).

**Proof.** For a unitary \(u\), \(\tau(up_\tau u^*)=\tau(p_\tau)=0\) by Proposition 2.2(2). Since \(p_\tau\) is the largest projection of trace \(0\), \(up_\tau u^*\leq p_\tau\). Applying this to \(u^*\) gives equality. So \(p_\tau\) commutes with every unitary, and it is central by Lemma 1.4. Parts (2) and (3) of Lemma 3.1 give the two properties of \(z=s(\tau)\). If \(z'\) is another central projection with these properties, then \(\tau(1-z')=0\), so \(1-z'\leq p_\tau\). Also \(p_\tau z'\) is a projection in \(Mz'\) with \(\tau(p_\tau z')\leq\tau(p_\tau)=0\), so \(p_\tau z'=0\) and \(p_\tau\leq1-z'\). Thus \(z'=s(\tau)\). \(\square\)

**Definition 3.3.** \(s(\tau)\) is the *support* of the normal trace \(\tau\).

**Remarks.** (1) Lemma 3.1 uses only normality, so it covers normal weights as well as normal traces. (2) Normality cannot be dropped: the finite trace of Example 3.4 has no largest null projection and no support. (3) For weights, \(p_\varphi\) need not be central: for a unit vector \(\xi\) and \(\varphi=\langle\,\cdot\,\xi,\xi\rangle\) on \(B(H)\) with \(\dim H\geq2\), \(p_\varphi\) is the projection onto \(\xi^\perp\). (4) For a normal trace, \(\tau(x)=\tau(xs(\tau))\) for every \(x\in M_+\).

**Example 3.4** (A finite trace that is not normal). Let \(\omega\) be a free ultrafilter on \(\mathbb N\), and on \(M=\ell^\infty(\mathbb N)\), acting on \(\ell^2(\mathbb N)\), put \(\tau(f)=\lim_\omega f(n)\). This is a finite trace, since \(M\) is commutative. It vanishes on every \(1_F\) with \(F\) finite; these projections increase to \(1\), while \(\tau(1)=1\). So \(\tau\) is not normal. Its null projections are the \(1_A\) with \(A\notin\omega\), and their supremum is \(1\), which is not null. No central projection \(z\) has the two properties of Proposition 3.2: faithfulness on \(Mz\) fails if \(z\neq0\), since a free ultrafilter contains no singleton, and \(z=0\) would force \(\tau=0\). So Proposition 3.2 fails without normality. Looking ahead: here \(\mathcal Z=M\) and the center-valued trace of Section 5 is the identity map, so Theorem 5.5 holds trivially, and Theorem 5.9(3) is consistent, since \(\tau|_{\mathcal Z}=\tau\) is not normal.

### Sums of traces

**Proposition 3.5** (Sums of normal traces). Let \((\tau_i)_{i\in I}\) be normal traces on \(M\), and put \(\tau(x)=\sum_i\tau_i(x)\) for \(x\in M_+\).

1. \(\tau\) is a normal trace, and \(s(\tau)=\bigvee_is(\tau_i)\).
2. Suppose each \(\tau_i\) is semifinite, and every nonzero central projection \(q\) majorizes a nonzero central projection \(q'\) with \(q's(\tau_i)\neq0\) for only finitely many \(i\). Then \(\tau\) is semifinite. The condition holds when \(I\) is finite, and when the supports \(s(\tau_i)\) are mutually orthogonal.
3. Without such a condition \(\tau\) can fail to be semifinite (Example 3.6).

**Proof.** (1) The identities (2.1) hold term by term. Let \(x_\alpha\uparrow x\). For a finite set \(F\subseteq I\), \(\sup_\alpha\sum_{i\in F}\tau_i(x_\alpha)=\sum_{i\in F}\tau_i(x)\), because finitely many increasing nets over one directed set can be added. Taking the supremum over \(F\) on both sides, and exchanging the two suprema on the left, gives \(\tau(x_\alpha)\uparrow\tau(x)\). For a projection \(e\), \(\tau(e)=0\) exactly when \(\tau_i(e)=0\) for all \(i\), that is, when \(e\leq1-s(\tau_i)\) for all \(i\), that is, when \(e\leq1-\bigvee_is(\tau_i)\). So \(p_\tau=1-\bigvee_is(\tau_i)\).

(2) Let \(0\neq x\in M_+\) and \(q=c(x)\). Choose \(q'\) as in the hypothesis, and let \(F=\{i:q's(\tau_i)\neq0\}\), a finite set. Since \(0\neq q'\leq c(x)\), \(xq'\neq0\), and \(xq'\leq x\) by Proposition 2.2(5). For \(i\notin F\), \(\tau_i\) vanishes on \((Mq')_+\), because \(y\leq\|y\|q'\leq\|y\|(1-s(\tau_i))\) there. If \(F\) is empty, \(y=xq'\) has \(\tau(y)=0\). Otherwise write \(F=\{i_1,\dots,i_m\}\). Semifiniteness of \(\tau_{i_1}\) gives \(0\neq y_1\leq xq'\) with \(\tau_{i_1}(y_1)<\infty\); semifiniteness of \(\tau_{i_2}\) gives \(0\neq y_2\leq y_1\) with \(\tau_{i_2}(y_2)<\infty\); and so on. Put \(y=y_m\). Then \(0\neq y\leq x\), \(y\in(Mq')_+\), \(\tau_{i_k}(y)\leq\tau_{i_k}(y_k)<\infty\) for each \(k\), and \(\tau_i(y)=0\) for \(i\notin F\). So \(\tau(y)<\infty\). For finite \(I\) take \(q'=q\). For orthogonal supports, take \(q'=qs(\tau_i)\) if this is nonzero for some \(i\) (then \(q's(\tau_j)=0\) for \(j\neq i\)), and \(q'=q\) otherwise. \(\square\)

**Example 3.6** (A sum of semifinite traces that is not semifinite). On \(M=\mathbb C\), let \(\tau_n(t)=t\) for \(n\in\mathbb N\). Each \(\tau_n\) is finite, hence semifinite, but \(\sum_n\tau_n(t)=\infty\) for \(t>0\), so the sum is not semifinite. All supports equal \(1\), so the hypothesis of Proposition 3.5(2) fails. Any finite subfamily has a semifinite sum.

### The semifinite part of a trace

**Proposition 3.7** (The semifinite part). Let \(\tau\) be any trace on \(M\); normality is not needed. There is a unique central projection \(z\) such that \(\tau\) is semifinite on \(Mz\) and \(\tau(x)=\infty\) for every nonzero \(x\in M_+(1-z)\). The \(\sigma\)-weak closures of \(\mathfrak n_\tau\) and of \(\mathfrak m_\tau\) are both \(Mz\). Moreover, the elements \(e_a=a(1+a)^{-1}\) (\(a\in F_\tau\)) form an increasing net of positive contractions in \(F_\tau\) with \(e_a\uparrow z\).

*Reference:* [Takesaki I, Lemma V.2.13], for a normal trace. Its proof takes an increasing net in \(\mathfrak n_\tau\) that converges to \(z\); Remark 3.8 shows that such a net does not suffice.

**Proof.** With the notation of (2.2), \(\mathfrak n_\tau\) is a two-sided ideal by Lemma 2.4(1). Multiplication by a fixed element is \(\sigma\)-weakly continuous, so the \(\sigma\)-weak closure of \(\mathfrak n_\tau\) is again a two-sided ideal, now closed. By the description of \(\sigma\)-weakly closed ideals, it equals \(Mz\) for a unique central projection \(z\).

Order \(F_\tau\) by the operator order. It is directed, since \(a+b\) is an upper bound of \(a\) and \(b\). The map \(a\mapsto e_a=1-(1+a)^{-1}\) is increasing, because inversion reverses the order of invertible positive operators. Also \(0\leq e_a\leq1\) and \(e_a\leq a\), so \(e_a\in F_\tau\). Let \(p=\sup_ae_a\).

\(p\leq z\): for \(a\in F_\tau\), \(a^{1/2}\in\mathfrak n_\tau\subseteq Mz\), so \(a=az\) and \(e_a\leq s(a)\leq z\).

\(z\leq p\): let \(x\in\mathfrak n_\tau\) and \(b=x^*x\in F_\tau\). For \(t>0\), \(tb\in F_\tau\), and \(e_{tb}=tb(1+tb)^{-1}\uparrow s(b)\) as \(t\to\infty\), by the spectral theorem. So \(s(b)\leq p\). The right support of \(x\) is \(s(x^*x)=s(b)\), so \(xp=x\). Thus \(\mathfrak n_\tau\subseteq Mp\). As \(Mp\) is \(\sigma\)-weakly closed, \(Mz\subseteq Mp\), and \(z\leq p\).

Semifinite on \(Mz\): let \(0\neq x\in(Mz)_+\). Since \(e_a\uparrow z\) strongly and \(x^{1/2}z=x^{1/2}\), \(x^{1/2}e_ax^{1/2}\to x\) strongly, so some \(y=x^{1/2}e_ax^{1/2}\) is nonzero. Then \(y\leq x\), since \(e_a\leq1\). With \(w=e_a^{1/2}x^{1/2}\), (2.1) gives \(\tau(y)=\tau(w^*w)=\tau(ww^*)=\tau(e_a^{1/2}xe_a^{1/2})\leq\|x\|\tau(e_a)<\infty\).

Infinite on \(M_+(1-z)\): if \(x\in M_+(1-z)\) and \(\tau(x)<\infty\), then \(x\in F_\tau\), so \(x=xz\) as shown above; together with \(x=x(1-z)\) this gives \(x=0\).

Closure of \(\mathfrak m_\tau\): \(\mathfrak m_\tau\subseteq\mathfrak n_\tau\subseteq Mz\), and for \(x\in Mz\), \(e_axe_a\in\mathfrak m_\tau\) tends to \(zxz=x\), as in the proof of (d)\(\Rightarrow\)(e) in Proposition 2.5.

Uniqueness: let \(z'\) be another such projection. A nonzero \(x\in(Mz(1-z'))_+\) would majorize, by semifiniteness on \(Mz\), a nonzero \(y\) of finite trace, and \(y\in M_+(1-z')\) contradicts the choice of \(z'\). So \(z(1-z')=0\), and by symmetry \(z=z'\). \(\square\)

**Remark 3.8.** The net \((e_a)\) lies inside \(F_\tau\) on purpose. Let \((e_i)\) be an increasing net of positive elements of \(\mathfrak n_\tau\) that converges strongly to \(z\), and let \(x\in(Mz)_+\). Then \(e_ix^{1/2}\in\mathfrak n_\tau\) gives only \(\tau(x^{1/2}e_i^2x^{1/2})<\infty\), not \(\tau(x^{1/2}e_ix^{1/2})<\infty\), and the second can fail. In \(B(\ell^2(\mathbb N))\) with the usual trace, the diagonal operators \(u_n=\operatorname{diag}(1,\dots,1,\tfrac1{n+1},\tfrac1{n+2},\dots)\) (\(n\) ones) are positive, lie in \(\mathfrak n_\tau\), increase and converge strongly to \(1=z\), but \(\tau(u_n)=\infty\); take \(x=1\). With such a net one can still use \(x^{1/2}e_i^2x^{1/2}\), which is \(\leq x\) and nonzero for some \(i\).

## 4. Finite algebras have many finite normal traces

Two lemmas about sequences of projections prepare the main theorem of this section, Theorem 4.7.

### Increasing sequences under one projection

**Lemma 4.1.** Let \(e_1\leq e_2\leq\cdots\) be finite projections and \(f\) a projection with \(e_n\precsim f\) for all \(n\). Then \(e=\bigvee_ne_n\precsim f\).

**Proof.** Put \(p_0=e_1\) and \(p_n=e_{n+1}-e_n\) for \(n\geq1\). These are mutually orthogonal, and \(\sum_{n\geq0}p_n=e\) strongly. We construct mutually orthogonal projections \(q_0,q_1,\ldots\leq f\) with \(q_n\sim p_n\); then \(e\precsim f\) by Lemma 1.1.

Choose \(q_0\leq f\) with \(q_0\sim p_0=e_1\). Suppose \(q_0,\dots,q_{n-1}\) are chosen (\(n\geq1\)). Put \(f_n=q_0+\cdots+q_{n-1}\). By Lemma 1.1, \(f_n\sim p_0+\cdots+p_{n-1}=e_n\), so \(f_n\) is finite by Lemma 1.2. Choose a partial isometry \(w\) with \(w^*w=e_{n+1}\) and \(ww^*\leq f\), and put \(f'_{n+1}=ww^*\) and \(f'_n=we_nw^*\). Then \(f'_n\leq f'_{n+1}\leq f\), \(f'_n\sim e_n\sim f_n\) (through \(we_n\)), and \(f'_{n+1}-f'_n=wp_nw^*\sim p_n\) (through \(wp_n\)). In the corner \(fMf\), the projections \(f_n\) and \(f'_n\) are finite and equivalent. So the complement theorem for equivalent finite projections, applied in \(fMf\), gives \(f-f_n\sim f-f'_n\). Let \(v\) be a partial isometry with \(v^*v=f-f'_n\) and \(vv^*=f-f_n\), and put \(q_n=v(f'_{n+1}-f'_n)v^*\). Since \(f'_{n+1}-f'_n\leq f-f'_n\), \(q_n\) is a projection below \(f-f_n\), orthogonal to \(q_0,\dots,q_{n-1}\), and \(q_n\sim f'_{n+1}-f'_n\sim p_n\). \(\square\)

**Theorem 4.2** (Finiteness is not needed). Let \(e_1\leq e_2\leq\cdots\) be any projections and \(f\) a projection with \(e_n\precsim f\) for all \(n\). Then \(\bigvee_ne_n\precsim f\).

*Reference:* [Takesaki I, Lemma V.2.2] assumes the \(e_n\) finite; that case is Lemma 4.1.

**Proof.** By the type decomposition, \(f=f_1+f_2\) with \(f_1\) finite, \(f_2\) properly infinite (either may be zero) and \(c(f_1)c(f_2)=0\). Put \(c=c(f_1)\). Then \(fc=f_1\) and \(f(1-c)=f_2\). Let \(e=\bigvee_ne_n\) and let \(p_n\) be as in the proof of Lemma 4.1.

On \(c\): by Lemma 1.2, \(e_nc\precsim fc=f_1\), so each \(e_nc\) is finite, and the \(e_nc\) increase to \(ec\). Lemma 4.1 gives \(ec\precsim f_1\).

On \(1-c\): if \(f_2=0\), then \(e_n(1-c)=0\) for all \(n\) and \(e(1-c)=0\). Otherwise \(f_2\) is properly infinite, and so is the algebra \(f_2Mf_2\) by Lemma 1.5. Halving the properly infinite algebra \(f_2Mf_2\) gives \(g_1\leq f_2\) with \(g_1\sim f_2-g_1\sim f_2\). The projection \(r_1=f_2-g_1\) is equivalent to \(f_2\), hence properly infinite by Lemma 1.2, so halving in \(r_1Mr_1\) gives \(g_2\leq r_1\) with \(g_2\sim r_1-g_2\sim r_1\sim f_2\). Continuing, we get mutually orthogonal \(g_1,g_2,\ldots\leq f_2\), each equivalent to \(f_2\). Now \(p_n(1-c)\leq e_{n+1}(1-c)\precsim f_2\sim g_{n+1}\), so \(p_n(1-c)\precsim g_{n+1}\), and Lemma 1.1 gives \(e(1-c)=\sum_np_n(1-c)\precsim\sum_ng_{n+1}\leq f_2\).

Adding the two central pieces with Lemma 1.1 gives \(e\precsim fc+f(1-c)=f\). \(\square\)

**Remark.** The index set must be countable, even for finite projections: see Example 4.3.

**Example 4.3** (Countability is needed). Let \(H\) have an orthonormal basis \((\varepsilon_\gamma)_{\gamma\in\Gamma}\) with \(|\Gamma|=\aleph_1\), \(M=B(H)\), and \(f\) the projection onto the closed span of countably infinitely many basis vectors. For finite \(F\subseteq\Gamma\) let \(e_F\) be the projection onto the span of \(\{\varepsilon_\gamma:\gamma\in F\}\). The \(e_F\) form an increasing net of finite projections, each \(\precsim f\), with supremum \(1\). But \(1\precsim f\) would give an isometry of \(H\) into \(fH\), which is impossible because \(H\) has Hilbert dimension \(\aleph_1\) and \(fH\) has dimension \(\aleph_0\). So sequences cannot be replaced by nets in Lemma 4.1 and Theorem 4.2, even for finite projections.

### Orthogonal sequences in finite algebras

**Lemma 4.4.** Let \(M\) be finite, let \((e_n)_{n\geq1}\) be mutually orthogonal projections, and let \(f_n\sim e_n\). Then \(f_n\to0\) \(\sigma\)-strongly.

**Proof.** *Step 1.* If \(p_1\precsim q_1\), \(p_2\precsim q_2\) and \(q_1q_2=0\), then \(p_1\vee p_2\precsim q_1+q_2\). Indeed, by the parallelogram law (Lemma 1.3), \(p_1\vee p_2-p_2\sim p_1-p_1\wedge p_2\leq p_1\precsim q_1\), and \(p_1\vee p_2=(p_1\vee p_2-p_2)+p_2\); apply Lemma 1.1.

*Step 2.* By induction, \(f_m\vee\cdots\vee f_n\precsim e_m+\cdots+e_n\) for \(m\leq n\). For fixed \(m\) these projections increase in \(n\) and are finite, since \(M\) is. Lemma 4.1 gives \(P_m:=\bigvee_{k\geq m}f_k\precsim\sum_{k\geq m}e_k\).

*Step 3.* Put \(e_0=1-\sum_{k\geq1}e_k\). If \(P_m\sim P'\leq\sum_{k\geq m}e_k\), the complement theorem for equivalent finite projections gives \(1-P_m\sim1-P'\geq1-\sum_{k\geq m}e_k=e_0+e_1+\cdots+e_{m-1}\).

*Step 4.* The \(P_m\) decrease; let \(P=\bigwedge_mP_m\). Then \(e_0+\cdots+e_{m-1}\precsim1-P_m\leq1-P\) for all \(m\). These projections increase to \(1\), so Lemma 4.1 gives \(1\precsim1-P\). As \(M\) is finite, \(1-P=1\) and \(P=0\).

*Step 5.* \(0\leq f_m\leq P_m\downarrow0\). For vectors \(\xi_k\) with \(\sum_k\|\xi_k\|^2<\infty\), \(\sum_k\|f_m\xi_k\|^2=\sum_k\langle f_m\xi_k,\xi_k\rangle\leq\sum_k\langle P_m\xi_k,\xi_k\rangle\to0\) by dominated convergence. \(\square\)

**Theorem 4.5** (Only \(\sum_ne_n\) needs to be finite). Let \(M\) be any von Neumann algebra, \((e_n)\) mutually orthogonal projections whose sum \(e\) is finite, and \(f_n\sim e_n\). Then \(f_n\to0\) \(\sigma\)-strongly.

**Proof.** Steps 1 and 2 of the proof of Lemma 4.4 do not use finiteness of \(M\). They give \(f_1\vee\cdots\vee f_n\precsim e_1+\cdots+e_n\leq e\), so these projections are finite by Lemma 1.2, and Lemma 4.1 gives \(g:=\bigvee_nf_n\precsim e\). So \(g\) is finite, and \(h:=e\vee g\) is finite because finite projections form a lattice. The finite algebra \(hMh\) contains every \(e_n\), every \(f_n\), and the partial isometries \(v_n=f_nv_ne_n\) that implement \(e_n\sim f_n\). Apply Lemma 4.4 in \(hMh\). \(\square\)

**Remark.** Finiteness of \(\sum_ne_n\) cannot be dropped: see Example 4.6.

**Example 4.6** (The sum must be finite). In \(B(\ell^2(\mathbb N))\), with orthonormal basis \((\varepsilon_n)\), let \(e_n\) be the projection onto \(\mathbb C\varepsilon_n\) and \(f_n=e_1\) for every \(n\). The \(e_n\) are orthogonal and \(f_n\sim e_n\), but \(f_n\) does not tend to \(0\). Here \(\sum_ne_n=1\) is infinite.

### Separating families of finite normal traces

A family of traces *separates* \(M_+\) if every nonzero \(x\in M_+\) has \(\tau(x)\neq0\) for some member \(\tau\). One also says that there are *sufficiently many* traces in the family.

**Theorem 4.7.** For a von Neumann algebra \(M\) the following are equivalent:

- (i) \(M\) is finite;
- (ii) the finite normal traces on \(M\) separate \(M_+\);
- (iii) the finite traces on \(M\) separate \(M_+\) (normality not required).

Moreover, let \(M\) be finite and \(\varphi\in M_*^+\). Then the norm-closed convex hull \(K_\varphi\) of \(\{\varphi(u^*\cdot u):u\in\mathcal U(M)\}\) contains a finite normal trace \(\tau_\varphi\), and \(\tau_\varphi=\varphi\) on \(\mathcal Z\).

*Reference:* [Yeadon 1971].

**Proof.** (ii)\(\Rightarrow\)(iii) is trivial. (iii)\(\Rightarrow\)(i): let \(u^*u=1\). For every finite trace \(\tau\), \(\tau(uu^*)=\tau(u^*u)=\tau(1)\), so \(\tau(1-uu^*)=0\). As \(1-uu^*\geq0\), separation gives \(uu^*=1\). So \(1\sim f\leq1\) forces \(f=1\), which is finiteness.

(i)\(\Rightarrow\)(ii). Let \(M\) be finite and \(\varphi\in M_*^+\). For a unitary \(u\) and \(\psi\in M_*\) write \((u\cdot\psi)(x)=\psi(u^*xu)\). Then \(u\cdot(v\cdot\psi)=(uv)\cdot\psi\), each map \(\psi\mapsto u\cdot\psi\) is a linear isometry of \(M_*\) onto itself, and it preserves \(M_*^+\). Let \(Q_\varphi=\{u\cdot\varphi:u\in\mathcal U(M)\}\) and let \(K_\varphi\) be its norm-closed convex hull. Then \(K_\varphi\subseteq M_*^+\), every \(u\cdot\) maps \(K_\varphi\) into itself, and \(\|\psi\|=\psi(1)=\varphi(1)\) on \(K_\varphi\).

*Step 1 (uniform smallness).* For every sequence \((e_n)\) of mutually orthogonal projections, \(\sup_{\psi\in K_\varphi}\psi(e_n)\to0\). It suffices to prove this for \(\psi\in Q_\varphi\): the supremum over convex combinations is the same, and a norm limit changes \(\psi(e_n)\) by at most the norm distance. Suppose instead that \(\delta>0\), indices \(n_1<n_2<\cdots\) and unitaries \(u_k\) satisfy \(\varphi(u_k^*e_{n_k}u_k)\geq\delta\). The projection \(f_k=u_k^*e_{n_k}u_k\) is equivalent to \(e_{n_k}\) through \(e_{n_k}u_k\), and the \(e_{n_k}\) are mutually orthogonal. Since \(M\) is finite, Lemma 4.4 gives \(f_k\to0\) \(\sigma\)-strongly, so \(\varphi(f_k)\to0\), a contradiction.

*Step 2 (weak compactness).* Let \(p_n\downarrow0\) be projections. We claim \(\sup_{\psi\in K_\varphi}\psi(p_n)\to0\). These suprema decrease in \(n\). If they stayed at least \(\delta>0\), choose \(\psi_1\in K_\varphi\) and \(n_1\) with \(\psi_1(p_{n_1})>\delta/2\); normality of \(\psi_1\) gives \(n_2>n_1\) with \(\psi_1(p_{n_2})<\delta/4\). Choose \(\psi_2\in K_\varphi\) with \(\psi_2(p_{n_2})>\delta/2\) and \(n_3>n_2\) with \(\psi_2(p_{n_3})<\delta/4\); and so on. The projections \(e_k=p_{n_k}-p_{n_{k+1}}\) are mutually orthogonal and \(\psi_k(e_k)>\delta/4\), against Step 1. Since \(K_\varphi\) is bounded, Akemann's criterion shows that \(K_\varphi\) is relatively \(\sigma(M_*,M)\)-compact. It is norm closed and convex, hence weakly closed by Mazur's theorem, and the weak topology of \(M_*\) is \(\sigma(M_*,M)\) because \((M_*)^*=M\). So \(K_\varphi\) is \(\sigma(M_*,M)\)-compact.

*Step 3 (fixed point).* The maps \(\psi\mapsto u\cdot\psi\) form a group of linear isometries of \(M_*\) that leave the weakly compact convex set \(K_\varphi\) invariant. By the fixed point theorem of Ryll-Nardzewski there is \(\tau_\varphi\in K_\varphi\) with \(u\cdot\tau_\varphi=\tau_\varphi\) for every unitary \(u\).

*Step 4 (\(\tau_\varphi\) is a trace).* \(\tau_\varphi\) is a normal positive functional with \(\tau_\varphi(u^*xu)=\tau_\varphi(x)\) for all \(u\) and \(x\). By Proposition 2.2(6) it is a finite normal trace. For \(a\in\mathcal Z\), \((u\cdot\psi)(a)=\psi(a)\); this passes to convex combinations and norm limits, so \(\tau_\varphi(a)=\varphi(a)\).

*Step 5 (separation).* Let \(0\neq x\in M_+\). Choose \(\xi\) with \(x\xi\neq0\), put \(\eta=x\xi\) and \(\varphi=\langle\,\cdot\,\eta,\eta\rangle\in M_*^+\), and let \(s=s(\tau_\varphi)\), a central projection by Proposition 3.2. Since \(\tau_\varphi(1-s)=0\) and \(1-s\in\mathcal Z\), Step 4 gives \(\|(1-s)\eta\|^2=\varphi(1-s)=0\). So \(sx\xi=x\xi\neq0\), and \(sx=x^{1/2}sx^{1/2}\) is a nonzero positive element of \(Ms\), where \(\tau_\varphi\) is faithful. Hence \(\tau_\varphi(x)\geq\tau_\varphi(sx)>0\). \(\square\)

**Remark.** The proof uses two results that are not proved here: Akemann's criterion and the fixed point theorem of Ryll-Nardzewski. The minimal-norm argument that constructs the center-valued trace in Section 5 does not replace them. Every \(\psi\in K_\varphi\) has the same norm \(\varphi(1)\), and that argument would need a unitarily invariant strictly convex norm on \(M_*\), which is not at hand before a trace exists.

## 5. The center-valued trace

### Construction of the center-valued trace

For \(x\in M\) let
\[
K(x)=\text{the }\sigma\text{-weakly closed convex hull of }\{uxu^*:u\in\mathcal U(M)\}.
\tag{5.1}
\]

**Lemma 5.1** (Averaging with a faithful trace). Let \(\tau\) be a faithful normal finite trace on \(M\), extended to \(M\) as in Proposition 2.2(6). For each \(x\in M\), with \(K(x)\) as in (5.1):

1. \(K(x)\) is \(\sigma\)-weakly compact, lies in the ball of radius \(\|x\|\), and \(uK(x)u^*=K(x)\) for every unitary \(u\).
2. \(\tau(ay)=\tau(ax)\) for all \(a\in\mathcal Z\) and \(y\in K(x)\).
3. \(K(x)\cap\mathcal Z\) has exactly one element, \(T(x)\). It is the only \(z\in\mathcal Z\) with \(\tau(az)=\tau(ax)\) for all \(a\in\mathcal Z\).

**Proof.** (1) The ball of radius \(\|x\|\) is convex, \(\sigma\)-weakly compact, and contains the unitary orbit of \(x\), so it contains \(K(x)\) as a closed subset. The map \(y\mapsto uyu^*\) is affine, \(\sigma\)-weakly continuous and maps the orbit onto itself, so it maps \(K(x)\) onto \(K(x)\).

(2) By Proposition 2.2(6), \(\tau\in M_*\), so \(y\mapsto\tau(ay)\) is \(\sigma\)-weakly continuous and linear. On the orbit, \(\tau(auxu^*)=\tau(u(ax)u^*)=\tau(ax)\), since \(a\) is central and \(\tau(uwu^*)=\tau(w)\) for all \(w\in M\) (Proposition 2.2(2) and linearity). So this functional is constant on \(K(x)\).

(3) Put \(N(y)=\tau(y^*y)\). It comes from the positive sesquilinear form \((y_1,y_2)\mapsto\tau(y_2^*y_1)\), so it satisfies the parallelogram identity \(N(y_1+y_2)+N(y_1-y_2)=2N(y_1)+2N(y_2)\).

\(N\) is \(\sigma\)-weakly lower semicontinuous on bounded sets. Indeed, let \(y_i\to y\) \(\sigma\)-weakly with bounded norms. The functional \(y'\mapsto\tau(y^*y')\) lies in \(M_*\), so \(\tau(y^*y_i)\to N(y)\), and \(|\tau(y^*y_i)|\leq N(y)^{1/2}N(y_i)^{1/2}\) by Cauchy–Schwarz. Hence \(N(y)\leq N(y)^{1/2}\liminf_iN(y_i)^{1/2}\), that is, \(N(y)\leq\liminf_iN(y_i)\).

*A minimizer exists.* Let \(\mu=\inf_{K(x)}N\). The sets \(\{y\in K(x):N(y)\leq\mu+1/k\}\) are nonempty, \(\sigma\)-weakly closed by lower semicontinuity, and decreasing. By compactness they have a common point \(y_0\), and \(N(y_0)=\mu\).

*It is unique.* If \(y_1,y_2\in K(x)\) both give \(\mu\), then \((y_1+y_2)/2\in K(x)\), and the parallelogram identity gives \(N((y_1+y_2)/2)=\mu-N(y_1-y_2)/4\). So \(N(y_1-y_2)=0\), and \(y_1=y_2\) by faithfulness.

*It is central.* \(N(uyu^*)=\tau(uy^*yu^*)=N(y)\), and \(uK(x)u^*=K(x)\). So \(uy_0u^*\) is also a minimizer, hence \(uy_0u^*=y_0\) for every unitary \(u\). By Lemma 1.4, \(y_0\in\mathcal Z\).

Finally, if \(z\in\mathcal Z\) satisfies \(\tau(az)=\tau(ax)\) for all \(a\in\mathcal Z\) (by (2) this holds for every \(z\in K(x)\cap\mathcal Z\)), then \(\tau(a(z-y_0))=0\) for all \(a\in\mathcal Z\). With \(a=(z-y_0)^*\), faithfulness gives \(z=y_0\). \(\square\)

**Theorem 5.2** (The center-valued trace). For a von Neumann algebra \(M\) the following are equivalent:

- (i) \(M\) is finite;
- (ii) there is a linear map \(T:M\to\mathcal Z\) such that, for \(x\in M\) and \(a\in\mathcal Z\),
\[
\text{(a) }T(x^*x)=T(xx^*)\geq0,\quad
\text{(b) }T(ax)=aT(x),\quad
\text{(c) }T(1)=1,\quad
\text{(d) }T(x^*x)\neq0\text{ if }x\neq0.
\tag{5.2}
\]

If \(M\) is finite, one such \(T\) is normal and \(\sigma\)-weakly continuous, satisfies \(\|T(x)\|\leq\|x\|\) and \(T(a)=a\) for \(a\in\mathcal Z\) (so it maps onto \(\mathcal Z\)), and has \(T(x)\in K(x)\) for every \(x\). For (ii)\(\Rightarrow\)(i), properties (a) and (d) suffice. Theorem 5.5 shows that \(T\) is unique, even among linear maps with only (a), (b), (c).

**Proof.** (ii)\(\Rightarrow\)(i): if \(u^*u=1\), then \(T(1-uu^*)=T(u^*u)-T(uu^*)=0\) by (a). Since \(1-uu^*=(1-uu^*)^*(1-uu^*)\), (d) gives \(uu^*=1\).

(i)\(\Rightarrow\)(ii). *Step 1: \(M\) has a faithful normal finite trace \(\tau\).* Define \(T(x)\) as in Lemma 5.1. It is the unique central \(z\) with \(\tau(az)=\tau(ax)\) for all \(a\in\mathcal Z\), and this description is linear in \(x\); so \(T\) is linear. (b): \(aT(x)\) is central and \(\tau(b\,aT(x))=\tau(ba\,x)\) for \(b\in\mathcal Z\), so \(T(ax)=aT(x)\). (c) and \(T(a)=a\) for \(a\in\mathcal Z\) are clear. Positivity: if \(x\geq0\), the orbit lies in the \(\sigma\)-weakly closed convex cone \(M_+\), so \(K(x)\subseteq M_+\) and \(T(x)\geq0\). (a): for \(a\in\mathcal Z_+\), (2.1) gives \(\tau(ax^*x)=\tau((xa^{1/2})^*(xa^{1/2}))=\tau((xa^{1/2})(xa^{1/2})^*)=\tau(axx^*)\). By linearity this holds for all \(a\in\mathcal Z\), so \(T(x^*x)=T(xx^*)\). (d): \(\tau(x^*x)=\tau(1\cdot T(x^*x))\), so \(T(x^*x)=0\) forces \(x=0\). The bound \(\|T(x)\|\leq\|x\|\) and \(T(x)\in K(x)\) come from Lemma 5.1.

*Normality.* Let \(x_i\uparrow x\). The \(T(x_i)\) increase and are bounded, so they have a supremum \(c\in\mathcal Z_+\) with \(c\leq T(x)\). For \(a\in\mathcal Z_+\), the functional \(\tau(a\,\cdot\,)=\tau(a^{1/2}\cdot a^{1/2})\) is normal, so \(\tau(ac)=\sup_i\tau(aT(x_i))=\sup_i\tau(ax_i)=\tau(ax)\). By linearity \(\tau(ac)=\tau(ax)\) for all \(a\in\mathcal Z\), and Lemma 5.1(3) gives \(c=T(x)\).

*\(\sigma\)-weak continuity.* For \(\omega\in\mathcal Z_*^+\), \(\omega\circ T\) is a normal positive functional, so it lies in \(M_*\), because the two notions of normality agree (see "Normal functionals" in the background list). Every \(\omega\in\mathcal Z_*\) is a combination of four elements of \(\mathcal Z_*^+\), by the positive parts of normal functionals. So \(\omega\circ T\in M_*\) for all \(\omega\in\mathcal Z_*\).

*Step 2: general finite \(M\).* By Zorn's lemma, let \((\tau_i)_{i\in I}\) be a maximal family of nonzero finite normal traces with mutually orthogonal supports \(s_i=s(\tau_i)\), which are central by Proposition 3.2. Suppose \(w=1-\sum_is_i\neq0\). Theorem 4.7 gives a finite normal trace \(\tau\) with \(\tau(w)>0\). Then \(\tau_w(x)=\tau(xw)\) is a finite normal trace (Proposition 2.2(5)) with \(\tau_w(w)>0\) and \(\tau_w(1-w)=0\), so \(0\neq s(\tau_w)\leq w\), against maximality. So \(\sum_is_i=1\). On the von Neumann algebra \(Ms_i\), with unit \(s_i\) and center \(\mathcal Zs_i\), \(\tau_i\) is a faithful normal finite trace, and Step 1 gives \(T_i:Ms_i\to\mathcal Zs_i\). The elements \(T_i(xs_i)\) lie in the orthogonal pieces \(\mathcal Zs_i\) and have norm at most \(\|x\|\), so \(T(x)=\sum_iT_i(xs_i)\) converges strongly, lies in \(\mathcal Z\), and satisfies \(T(x)s_i=T_i(xs_i)\). Each listed property holds on every piece, hence for \(T\). For instance, if \(x_\alpha\uparrow x\), then \(T(x_\alpha)s_i\uparrow T(x)s_i\) for every \(i\), so \(T(x_\alpha)\uparrow T(x)\); and \(\sigma\)-weak continuity follows from normality as in Step 1.

*\(T(x)\in K(x)\) in general.* For a finite set \(F\subseteq I\) put \(s_F=\sum_{i\in F}s_i\). A unitary \(U=\sum_{i\in F}u_i+(1-s_F)\), with \(u_i\in\mathcal U(Ms_i)\), gives \(UxU^*=\sum_{i\in F}u_ixs_iu_i^*+x(1-s_F)\). Averaging such unitaries with product weights shows that \(\sum_{i\in F}y_i+x(1-s_F)\in K(x)\) whenever each \(y_i\) is a convex combination of the orbit of \(xs_i\) in \(Ms_i\). By \(\sigma\)-weak continuity this extends to \(y_i\) in the corresponding hull \(K_i(xs_i)\), in particular to \(y_i=T_i(xs_i)\). So \(c_F=\sum_{i\in F}T_i(xs_i)+x(1-s_F)\in K(x)\). As \(F\) grows, \(c_F-T(x)=(x-T(x))(1-s_F)\to0\) strongly with bounded norms, hence \(\sigma\)-weakly, and \(T(x)\in K(x)\). \(\square\)

**Definition 5.3.** For finite \(M\), the map \(T\) of Theorem 5.2 is the *center-valued trace* of \(M\), written \(T_M\).

### Comparing projections through the center-valued trace

**Corollary 5.4** (Comparison). Let \(M\) be finite, and let \(T:M\to\mathcal Z\) be linear with (a), (b), (d) of (5.2). For projections \(e,f\),
\[
e\precsim f\iff T(e)\leq T(f),\qquad
e\sim f\iff T(e)=T(f),\qquad
e\prec f\iff T(e)\leq T(f)\ \text{and}\ T(e)\neq T(f).
\tag{5.3}
\]

**Proof.** If \(e\sim f\) through \(v\), (a) gives \(T(e)=T(v^*v)=T(vv^*)=T(f)\). If \(e\sim f'\leq f\), then \(T(e)=T(f')\leq T(f)\) by positivity. Conversely, suppose \(T(e)\leq T(f)\). By the comparison theorem there is a central projection \(h\) with \(he\precsim hf\) and \((1-h)f\precsim(1-h)e\); say \((1-h)f\sim g\leq(1-h)e\). By (a) and (b), \(T(g)=T((1-h)f)=(1-h)T(f)\geq(1-h)T(e)=T((1-h)e)\). So \(T((1-h)e-g)\leq0\). But \((1-h)e-g\) is a projection, so \(T((1-h)e-g)\geq0\); hence it is \(0\), and (d) gives \((1-h)e=g\sim(1-h)f\). By Lemma 1.1, \(e=he+(1-h)e\precsim hf+(1-h)f=f\). The second equivalence follows from the first and Schröder–Bernstein for projections, and the third from the first two. \(\square\)

### Finite traces factor through the center

**Theorem 5.5.** Let \(M\) be finite with center-valued trace \(T\). Every finite trace \(\sigma\) on \(M\), normal or not, satisfies
\[
\sigma(x)=\sigma(T(x))\qquad(x\in M).
\tag{5.4}
\]
Consequently:

1. \(\sigma\mapsto\sigma|_{\mathcal Z}\) is a bijection from the finite traces on \(M\) onto the positive linear functionals on \(\mathcal Z\), with inverse \(\psi\mapsto\psi\circ T\). It maps the finite normal traces onto \(\mathcal Z_*^+\).
2. (*Uniqueness of the center-valued trace.*) If \(T':M\to\mathcal Z\) is linear and satisfies (a), (b), (c) of (5.2), then \(T'=T\). In particular such a \(T'\) is automatically normal and faithful.

The proof uses two lemmas. Throughout, \(\sigma\) is a finite trace on \(M\), extended linearly (Proposition 2.2(6)).

**Lemma 5.6** (Homogeneous pieces). Let \(q\) be a central projection, and let \(g_1,\dots,g_n\) be orthogonal abelian projections with \(c(g_j)=q\) and \(g_1+\cdots+g_n=q\). Then \(\sigma(eq)=\sigma(T(e)q)\) for every projection \(e\).

**Proof.** Since abelian projections are smallest, \(g_j\precsim g_k\) for all \(j,k\), and Schröder–Bernstein for projections makes the \(g_j\) mutually equivalent. For a central projection \(w\leq q\), the projections \(g_jw\) are mutually equivalent (Lemma 1.2) with sum \(w\), so \(T(g_1w)=w/n\) and \(\sigma(g_1w)=\sigma(w)/n\).

Put \(h=T(e)q\), so \(0\leq h\leq q\). Let \(q_k=1_{[k/n,(k+1)/n)}(h)\,q\) for \(0\leq k<n\) and \(q_n=1_{\{1\}}(h)\,q\). These are orthogonal central projections with sum \(q\), and \(T(eq_k)=T(e)q_k=hq_k\).

Fix \(k<n\) and put \(G=(g_1+\cdots+g_k)q_k\). Then \(T(G)=(k/n)q_k\leq hq_k=T(eq_k)\), so (5.3) gives \(G\sim G'\) for some projection \(G'\leq eq_k\). Let \(d=eq_k-G'\). Then \(T(d)=hq_k-(k/n)q_k\leq(1/n)q_k=T(g_{k+1}q_k)\), so \(d\precsim g_{k+1}q_k\) by (5.3). Hence \(d\) is abelian: it is equivalent to a subprojection \(d'\) of the abelian projection \(g_{k+1}\), the algebra \(d'Md'\subseteq g_{k+1}Mg_{k+1}\) is commutative, and \(dMd\cong d'Md'\). Since \(c(d)\leq q_k\leq q\), we have \(c(g_1c(d))=c(g_1)c(d)=c(d)\). As abelian projections are smallest, \(d\precsim g_1c(d)\) and \(g_1c(d)\precsim d\), and Schröder–Bernstein for projections gives \(d\sim g_1c(d)\). By the first paragraph, \(T(d)=c(d)/n\). Multiplying \(T(eq_k)=(k/n)q_k+T(d)\) by \(c(d)\) gives \(hc(d)=((k+1)/n)\,c(d)\). So \(c(d)\) lies below the spectral projection \(1_{\{(k+1)/n\}}(h)\). But \(c(d)\leq q_k\leq1_{[k/n,(k+1)/n)}(h)\), which is orthogonal to it. Hence \(c(d)=0\) and \(d=0\). So \(eq_k=G'\sim G\); in particular \(T(e)q_k=T(eq_k)=T(G)=(k/n)q_k\), and
\[
\sigma(eq_k)=\sigma(G)=k\,\sigma(g_1q_k)=\tfrac kn\sigma(q_k)=\sigma\bigl(\tfrac kn q_k\bigr)=\sigma(T(e)q_k).
\]
For \(k=n\): \(T(eq_n)=hq_n=q_n=T(q_n)\), so \(T(q_n-eq_n)=0\), and (d) gives \(eq_n=q_n\); thus \(\sigma(eq_n)=\sigma(q_n)=\sigma(T(e)q_n)\). Summing over the finitely many \(k\) gives the claim. \(\square\)

**Lemma 5.7** (Approximate pieces). Let \(q\) be a central projection and \(K\geq1\). Suppose \(q=P_1+\cdots+P_K+R\) with orthogonal projections, \(P_j\sim P_1\) for all \(j\), and \(R\precsim P_1\). Then \(|\sigma(eq)-\sigma(T(e)q)|\leq2\sigma(q)/K\) for every projection \(e\).

**Proof.** Put \(t=T(P_1)\) and \(r=T(R)\), both in \(\mathcal Z_+\). Then \(Kt+r=q\), and \(0\leq r\leq t\) because \(R\sim R'\leq P_1\). Hence \(Kt\leq q\leq(K+1)t\), and \(t\) is invertible in the abelian algebra \(\mathcal Zq\). Let \(h=T(e)q\,t^{-1}\), the inverse taken in \(\mathcal Zq\). Then \(0\leq h\leq(K+1)q\). Put \(w_k=1_{[k,k+1)}(h)\,q\) for \(0\leq k<K\) and \(w_K=1_{[K,K+1]}(h)\,q\). These are orthogonal central projections with sum \(q\), and on each of them
\[
k\,t\,w_k\leq T(e)w_k\leq(k+1)\,t\,w_k .
\]
Put \(s_k=\sigma(P_1w_k)\). Since \(P_jw_k\sim P_1w_k\), the projection \((P_1+\cdots+P_m)w_k\) has trace \(ms_k\).

(i) \(T((P_1+\cdots+P_k)w_k)=ktw_k\leq T(ew_k)\), so Corollary 5.4 gives \((P_1+\cdots+P_k)w_k\precsim ew_k\), and \(ks_k\leq\sigma(ew_k)\).

(ii) For \(k<K\), \(T(ew_k)\leq(k+1)tw_k=T((P_1+\cdots+P_{k+1})w_k)\), so \(\sigma(ew_k)\leq(k+1)s_k\). For \(k=K\), \(\sigma(ew_K)\leq\sigma(w_K)=Ks_K+\sigma(Rw_K)\leq(K+1)s_K\), because \(Rw_K\precsim P_1w_K\).

(iii) By positivity of \(\sigma\), \(k\,\sigma(tw_k)\leq\sigma(T(e)w_k)\leq(k+1)\,\sigma(tw_k)\).

(iv) \(Ks_k+\sigma(Rw_k)=\sigma(w_k)\) with \(0\leq\sigma(Rw_k)\leq s_k\), and \(K\sigma(tw_k)+\sigma(rw_k)=\sigma(w_k)\) with \(0\leq\sigma(rw_k)\leq\sigma(tw_k)\). So both \(s_k\) and \(\sigma(tw_k)\) lie in \([\sigma(w_k)/(K+1),\,\sigma(w_k)/K]\).

(v) By (i)–(iv), \(\sigma(ew_k)\) and \(\sigma(T(e)w_k)\) both lie in the interval \([\,k\sigma(w_k)/(K+1),\,(k+1)\sigma(w_k)/K\,]\), whose length is \(\sigma(w_k)\,(k+K+1)/(K(K+1))\leq\sigma(w_k)\,(2K+1)/(K(K+1))\leq2\sigma(w_k)/K\).

(vi) Summing over \(k\): \(|\sigma(eq)-\sigma(T(e)q)|\leq\sum_k2\sigma(w_k)/K=2\sigma(q)/K\). \(\square\)

**Proof of Theorem 5.5.** *Reduction.* Both sides of (5.4) are linear and norm continuous in \(x\) (\(\sigma\) is bounded and \(\|T(x)\|\leq\|x\|\)), and projections span a norm-dense subspace of \(M\) by the spectral theorem. So it suffices to prove (5.4) for a projection \(e\).

*Decomposition.* By Proposition 1.6(a), \(1=\sum_{n\geq1}z_n+z_{{\rm II}_1}\), where \(z_n\) is a sum of \(n\) orthogonal abelian projections \(g^{(n)}_1,\dots,g^{(n)}_n\) with central support \(z_n\), and \(Mz_{{\rm II}_1}\) has no direct summand of type I. Fix \(m\geq1\) and put \(K=2^m\). Let \(q_{\rm s}=\sum_{n<K^2}z_n\) and \(q_{\rm l}=1-q_{\rm s}=\sum_{n\geq K^2}z_n+z_{{\rm II}_1}\).

*Small degrees.* By Lemma 5.6, applied to each of the finitely many \(z_n\) with \(n<K^2\), \(\sigma(eq_{\rm s})=\sigma(T(e)q_{\rm s})\).

*Large degrees and type II\(_1\).* For \(n\geq K^2\) write \(n=Ka_n+r_n\) with \(0\leq r_n<K\); then \(a_n\geq K>r_n\). Split \(g^{(n)}_1,\dots,g^{(n)}_n\) into \(K\) consecutive blocks of \(a_n\) projections and a remainder of \(r_n\) projections, and let \(P^{(n)}_j\) be the sum over the \(j\)-th block and \(R^{(n)}\) the sum over the remainder. The \(g^{(n)}_j\) are mutually equivalent, as in the proof of Lemma 5.6. So Lemma 1.1 gives \(P^{(n)}_j\sim P^{(n)}_1\), and \(R^{(n)}\) is equivalent to the sum of the first \(r_n\) projections of the first block, so \(R^{(n)}\precsim P^{(n)}_1\). On \(z_{{\rm II}_1}\), halving applied \(m\) times gives orthogonal equivalent projections \(Q_1,\dots,Q_K\) with sum \(z_{{\rm II}_1}\): if \(z_{{\rm II}_1}=a+b\) with \(a\sim b\) through \(v\), halve \(a=a_1+a_2\) and use \(b_i=va_iv^*\), and repeat. Put \(P_j=\sum_{n\geq K^2}P^{(n)}_j+Q_j\) and \(R=\sum_{n\geq K^2}R^{(n)}\). By Lemma 1.1, \(P_j\sim P_1\) and \(R\precsim P_1\), and \(P_1+\cdots+P_K+R=q_{\rm l}\). Lemma 5.7 gives \(|\sigma(eq_{\rm l})-\sigma(T(e)q_{\rm l})|\leq2\sigma(1)/2^m\).

Adding the two parts, \(|\sigma(e)-\sigma(T(e))|\leq2\sigma(1)/2^m\) for every \(m\), which proves (5.4).

*Consequence 1.* By (5.4), \(\sigma\) is determined by \(\sigma|_{\mathcal Z}\). For a positive functional \(\psi\) on \(\mathcal Z\), \(\psi\circ T\) is positive, satisfies \(\psi(T(x^*x))=\psi(T(xx^*))\), and restricts to \(\psi\) on \(\mathcal Z\); so it is a finite trace with restriction \(\psi\). If \(\sigma\) is normal, so is \(\sigma|_{\mathcal Z}\); if \(\psi\) is normal, so is \(\psi\circ T\), since \(T\) is normal (Theorem 5.2).

*Consequence 2.* Let \(\psi\) be a positive functional on \(\mathcal Z\). By (a), \(\psi\circ T'\) is a finite trace, and by (b), (c), \(T'(T(x))=T(x)T'(1)=T(x)\). Applying (5.4) to \(\sigma=\psi\circ T'\) gives \(\psi(T'(x))=\psi(T'(T(x)))=\psi(T(x))\). The vector functionals \(\langle\,\cdot\,\xi,\xi\rangle\) separate the points of \(\mathcal Z\), so \(T'=T\). \(\square\)

**Remark.** Lemmas 5.6 and 5.7 compare \(\sigma\) with \(\sigma\circ T\) uniformly over all projections, so the proof needs no normality, neither of \(\sigma\) nor of \(T'\). Normality of finite traces then comes out as a consequence, in Theorem 5.9.

**Example 5.8** (Matrices over an abelian algebra). Let \(A\) be an abelian von Neumann algebra and \(M=M_n(A)\), acting on \(H^n\). The center is \(\{a1:a\in A\}\), and \(T(x)=\frac1n\sum_kx_{kk}\), read as a scalar matrix, satisfies (5.2): for instance \(\sum_{k,l}x_{lk}^*x_{lk}=\sum_{k,l}x_{lk}x_{lk}^*\) because \(A\) is commutative. By Theorem 5.5(2) it is \(T_M\). For \(n=2\) and \(A=\mathbb C\), take \(e=e_{11}\) and \(f\) the projection onto \((1,1)/\sqrt2\). Then \(T(e)=T(f)=\tfrac12\), so \(e\sim f\) by Corollary 5.4, although \(ef\neq fe\).

### When a finite trace is normal

**Theorem 5.9** (Normality of finite traces). Let \(M\) be any von Neumann algebra, \(\tau\) a finite trace on it, and \(1=z_f+z_\infty\) the splitting of Proposition 1.6(b).

1. \(\tau(xz_\infty)=0\) for every \(x\in M\). In particular a properly infinite algebra has no nonzero finite trace.
2. \(\tau(x)=\tau(T_f(xz_f))\) for \(x\in M\), where \(T_f\) is the center-valued trace of the finite algebra \(Mz_f\).
3. \(\tau\) is normal exactly when \(\tau|_{\mathcal Z}\) is normal. In particular, on a factor every finite trace is normal: it is \(\tau(1)T_M\) if the factor is finite, and \(0\) otherwise.

**Proof.** (1) Suppose \(z_\infty\neq0\). Halving the properly infinite algebra \(Mz_\infty\) gives \(p\leq z_\infty\) with \(p\sim z_\infty-p\sim z_\infty\). By Proposition 2.2(3), \(\tau(z_\infty)=\tau(p)+\tau(z_\infty-p)=2\tau(z_\infty)\), and since \(\tau(z_\infty)<\infty\), \(\tau(z_\infty)=0\). By Cauchy–Schwarz, \(|\tau(xz_\infty)|^2\leq\tau(xx^*)\tau(z_\infty)=0\).

(2) The restriction of \(\tau\) to \(Mz_f\) is a finite trace on a finite algebra with center \(\mathcal Zz_f\), and Theorem 5.5 gives \(\tau(y)=\tau(T_f(y))\) for \(y\in Mz_f\). With (1), \(\tau(x)=\tau(xz_f)=\tau(T_f(xz_f))\).

(3) If \(\tau\) is normal, so is its restriction to \(\mathcal Z\). Conversely, if \(\tau|_{\mathcal Z}\) is normal, then by (2) \(\tau\) is the composite of the normal maps \(x\mapsto xz_f\), \(T_f\) and \(\tau|_{\mathcal Zz_f}\). For a factor, \(\mathcal Z=\mathbb C1\) and \(\tau|_{\mathcal Z}\) is normal. If the factor is finite, Theorem 5.5(1) gives \(\tau=\tau(1)T_M\); otherwise \(z_f=0\) and \(\tau=0\) by (1). \(\square\)

**Remark.** Finiteness of \(\tau\) is needed: see Example 5.10.

**Example 5.10** (An infinite trace with normal restriction to the center). On \(M=B(\ell^2(\mathbb N))\) put \(\tau(x)=\operatorname{Tr}(x)\) if \(x\in M_+\) has finite rank, and \(\tau(x)=\infty\) otherwise. This is a trace: finite-rank positive operators add to finite-rank ones, a positive operator of infinite rank stays of infinite rank when a positive operator is added, and \(z^*z\) and \(zz^*\) have equal rank. Its restriction to \(\mathcal Z=\mathbb C1\) is normal, since \(\tau(t1)=\infty\) for \(t>0\). But \(\tau\) is not normal: the finite-rank truncations of \(x=\operatorname{diag}(1/k^2)\) increase to \(x\) and have traces tending to \(\pi^2/6\), while \(\tau(x)=\infty\).

### Countable decomposability of finite algebras

**Lemma 5.11.** \(M\) is \(\sigma\)-finite if and only if it has a faithful normal state.

The same lemma is proved in [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-13).

**Proof.** Let \(\varphi\) be a faithful normal state and \((p_k)\) orthogonal nonzero projections. Then \(\sum_k\varphi(p_k)=\varphi(\sum_kp_k)\leq1\) with every \(\varphi(p_k)>0\), so the family is countable. Conversely, let \(M\) be \(\sigma\)-finite. By Zorn's lemma choose a maximal family of normal states \(\omega_k\) with mutually orthogonal supports \(s_k\) (Lemma 3.1(4)); it is countable. If \(r=1-\sum_ks_k\neq0\), a unit vector \(\xi\in rH\) gives the normal state \(\langle\,\cdot\,\xi,\xi\rangle\), which vanishes at \(1-r\), so its support lies below \(r\), against maximality. So \(\sum_ks_k=1\). Put \(\varphi=c\sum_k2^{-k}\omega_k\), with \(c>0\) chosen so that \(\varphi(1)=1\); the series converges in norm, so \(\varphi\in M_*^+\). If \(x\geq0\) and \(\varphi(x)=0\), then \(\omega_k(x)=0\) for all \(k\). By Lemma 3.1(3)–(4), \(s_kxs_k=0\), so \(x^{1/2}s_k=0\), and \(x^{1/2}=x^{1/2}\sum_ks_k=0\). \(\square\)

**Corollary 5.12** (\(\sigma\)-finiteness of finite algebras). Let \(M\) be finite with center-valued trace \(T\).

1. \(M\) is \(\sigma\)-finite if and only if \(\mathcal Z\) is. In that case \(\varphi\circ T\) is a faithful normal finite trace for every faithful normal state \(\varphi\) of \(\mathcal Z\).
2. There are orthogonal central projections \(z_k\) with \(\sum_kz_k=1\) and every \(Mz_k\) \(\sigma\)-finite.
3. A finite factor is \(\sigma\)-finite.

**Proof.** (1) An orthogonal family of central projections is an orthogonal family in \(M\), so \(\mathcal Z\) is \(\sigma\)-finite when \(M\) is. Conversely, if \(\mathcal Z\) is \(\sigma\)-finite, Lemma 5.11 gives a faithful normal state \(\varphi\) of \(\mathcal Z\). Then \(\varphi\circ T\) is a normal finite trace (Theorem 5.2) and a state. If \(\varphi(T(x))=0\) with \(x\geq0\), then \(T(x)=0\) and \(x=0\) by (d). So \(\varphi\circ T\) is a faithful normal state, and Lemma 5.11 gives \(\sigma\)-finiteness of \(M\).

(2) In the abelian von Neumann algebra \(\mathcal Z\), choose a maximal family of normal states with orthogonal supports \(z_k\), taken in \(\mathcal Z\). As in the proof of Lemma 5.11, \(\sum_kz_k=1\), and \(\mathcal Zz_k\) has a faithful normal state, so it is \(\sigma\)-finite. The algebra \(Mz_k\) is finite with center \(\mathcal Zz_k\); apply (1).

(3) The center is \(\mathbb C1\). \(\square\)

**Example 5.13** (Finite but not \(\sigma\)-finite). Let \(\Gamma\) be uncountable and \(M=\ell^\infty(\Gamma)\). It is finite, with \(T=\mathrm{id}\). The singletons form an uncountable orthogonal family, so \(M\) is not \(\sigma\)-finite, and by Lemma 5.11 it has no faithful normal state and no faithful normal finite trace. Still, the point evaluations form a separating family of finite normal traces (Theorem 4.7), and the decomposition of Corollary 5.12(2) can be taken to be the one into one-point pieces.

### Counting equivalent finite projections

A properly infinite semifinite algebra decomposes into pieces \(Mz_\alpha\cong N_\alpha\bar\otimes B(H_\alpha)\), with \(N_\alpha\) finite and \(\dim H_\alpha=\alpha\) (see "Properly infinite semifinite algebras" in the background list). We prove a counting theorem and derive from it that this decomposition is unique.

**Theorem 5.14.** Let \((e_i)_{i\in I}\) and \((f_j)_{j\in J}\) be infinite families of nonzero projections in \(M\). Suppose the \(e_i\) are mutually orthogonal, mutually equivalent and finite, that the same holds for the \(f_j\), and that \(\sum_ie_i=\sum_jf_j\). Then \(|I|=|J|\).

*Reference:* the counting step in the proof of [Takesaki I, Proposition V.1.40], which omits the hypothesis that the projections are nonzero.

**Proof.** Let \(p=\sum_ie_i\). All the projections and the partial isometries between them lie in \(pMp\), so we may assume \(p=1\). The \(e_i\) have one central support (Lemma 1.2), which majorizes \(\sum_ie_i=1\); so \(c(e_i)=1\), and likewise \(c(f_j)=1\).

Take any normal state of \(\mathcal Z\), for instance a vector state, and let \(z\) be its support in \(\mathcal Z\). Then \(z\neq0\), and \(\mathcal Zz\) has a faithful normal state, so it is \(\sigma\)-finite (Lemma 5.11). Fix \(i\in I\). The projection \(ze_i\) is finite and nonzero, since \(c(ze_i)=zc(e_i)=z\). By Lemma 1.5, the center of \(N_i=(ze_i)M(ze_i)\) is isomorphic to \(\mathcal Zc(ze_i)=\mathcal Zz\), so it is \(\sigma\)-finite. By Corollary 5.12(1), the finite algebra \(N_i\) has a faithful normal finite trace \(\tau_i\).

Since \(\sum_jf_j=1\), the positive elements \(ze_if_je_iz\) of \(N_i\) have sum \(ze_i\), and normality gives
\[
\tau_i(ze_i)=\sum_{j\in J}\tau_i(ze_if_je_iz)<\infty .
\]
So \(J_i=\{j:\tau_i(ze_if_je_iz)>0\}\) is countable. As \(\tau_i\) is faithful and \(ze_if_je_iz=(f_je_iz)^*(f_je_iz)\), \(J_i=\{j:zf_je_i\neq0\}\). For each \(j\), \(zf_j\neq0\) because \(c(f_j)=1\), and \(zf_j=\sum_izf_je_i\); so \(j\in J_i\) for some \(i\). Hence \(J=\bigcup_{i\in I}J_i\) and \(|J|\leq\aleph_0|I|=|I|\), since \(I\) is infinite. By symmetry \(|I|\leq|J|\), and the Cantor–Bernstein theorem gives \(|I|=|J|\). \(\square\)

**Corollary 5.15** (Uniqueness of the decomposition). Let \((z_\alpha)\) and \((z'_\beta)\) be families of orthogonal central projections, indexed by infinite cardinals, each with sum \(1\), with \(Mz_\alpha\cong N_\alpha\bar\otimes B(H_\alpha)\) and \(Mz'_\beta\cong N'_\beta\bar\otimes B(H'_\beta)\), where \(N_\alpha,N'_\beta\) are finite, \(\dim H_\alpha=\alpha\) and \(\dim H'_\beta=\beta\). Then \(z_\alpha=z'_\alpha\) for every \(\alpha\).

**Proof.** Let \(\alpha\neq\beta\) and suppose \(w=z_\alpha z'_\beta\neq0\). Under the first isomorphism, the projections \(1\otimes e_{kk}\), where \(e_{kk}\) runs over the rank-one projections of a basis of \(H_\alpha\), correspond to \(\alpha\) orthogonal, mutually equivalent projections \(E_k\in Mz_\alpha\) with sum \(z_\alpha\). They are finite, since each corner \(E_kME_k\) is isomorphic to \(N_\alpha\). The projections \(E_kw\) are orthogonal, mutually equivalent and finite, with sum \(w\); they are nonzero, because they are mutually equivalent and add up to \(w\neq0\). The second isomorphism gives \(\beta\) such projections with sum \(w\). Theorem 5.14 gives \(\alpha=\beta\), a contradiction. So \(z_\alpha z'_\beta=0\) for \(\alpha\neq\beta\), and \(z_\alpha=z_\alpha\sum_\beta z'_\beta=z_\alpha z'_\alpha=z'_\alpha\sum_\gamma z_\gamma=z'_\alpha\). \(\square\)

**Remarks.** (1) The projections in Theorem 5.14 must be nonzero: if all of them are \(0\), the sums agree for any \(I,J\). (2) Finiteness of the projections is necessary: see Example 5.16. (3) For finite families the count is not determined: in \(M_6(\mathbb C)\), \(1\) is the sum of two equivalent projections of rank \(3\) and of three equivalent projections of rank \(2\).

**Example 5.16** (Counting needs finite projections). With \(H\) and \(\Gamma\) as in Example 4.3, write \(\Gamma\) as a disjoint union of \(\aleph_0\) sets of size \(\aleph_1\), and also as a disjoint union of \(\aleph_1\) sets of size \(\aleph_1\). The coordinate projections give two orthogonal families, of sizes \(\aleph_0\) and \(\aleph_1\), of mutually equivalent infinite projections, both with sum \(1\). By Theorem 5.14 this cannot happen with finite projections.

## 6. Semifinite algebras

### Extending a normal trace from a corner

**Lemma 6.1.** Let \(e\) be a projection. There are partial isometries \((v_j)_{j\in J}\) in \(M\) with \(v_jv_j^*\leq e\), such that the projections \(f_j=v_j^*v_j\) are mutually orthogonal and \(\sum_jf_j=c(e)\).

**Proof.** By Zorn's lemma take a maximal family of mutually orthogonal projections \(f_j\) with \(f_j\precsim e\), and choose \(v_j\) with \(v_j^*v_j=f_j\) and \(v_jv_j^*\leq e\). By Lemma 1.2, \(f_j\leq c(f_j)\leq c(e)\). Suppose \(r=c(e)-\sum_jf_j\neq0\). Then \(c(r)\leq c(e)\), so \(c(r)c(e)=c(r)\neq0\), and the equivalent-pieces fact gives nonzero \(r'\leq r\) and \(e'\leq e\) with \(r'\sim e'\). Then \(r'\) could be added to the family, against maximality. So \(\sum_jf_j=c(e)\). \(\square\)

**Theorem 6.2** (Extension from a corner). Let \(\tau_0\) be a normal trace on \(eMe\), and let \((v_j)\) be as in Lemma 6.1. Then
\[
\tau(x)=\sum_{j\in J}\tau_0(v_jxv_j^*)\qquad(x\in M_+)
\tag{6.1}
\]
defines a normal trace on \(M\) with the following properties.

1. \(\tau(x)=\tau_0(x)\) for \(x\in(eMe)_+\), and \(\tau(1-c(e))=0\).
2. \(\tau\) is the only normal trace on \(M\) with (1). In particular it does not depend on the choice of \((v_j)\).
3. \(\tau\) is faithful on \(Mc(e)\) if and only if \(\tau_0\) is faithful; \(\tau\) is semifinite if and only if \(\tau_0\) is semifinite.

Normality of \(\tau_0\) cannot be dropped, even for the trace identity: see Example 6.6.

**Proof.** Each \(v_jxv_j^*\) lies in \((eMe)_+\), so (6.1) makes sense. Additivity and homogeneity are clear, and normality follows as in the proof of Proposition 3.5(1).

*Trace identity.* Let \(y\in M\) and put \(w_{kj}=v_kyv_j^*\in eMe\). Since \(v_j^*\) has range in \(f_jH\subseteq c(e)H\) and \(c(e)\) is central, the vector \(yv_j^*\eta\) lies in \(c(e)H=\bigl(\sum_kf_k\bigr)H\) for every \(\eta\). So \(v_jy^*yv_j^*=\sum_kv_jy^*f_kyv_j^*=\sum_kw_{kj}^*w_{kj}\), a strongly convergent sum of positive elements. Normality and the trace identity of \(\tau_0\) give
\[
\tau(y^*y)=\sum_j\sum_k\tau_0(w_{kj}^*w_{kj})=\sum_j\sum_k\tau_0(w_{kj}w_{kj}^*).
\]
In the same way \(v_kyy^*v_k^*=\sum_jv_kyf_jy^*v_k^*=\sum_jw_{kj}w_{kj}^*\), so \(\tau(yy^*)=\sum_k\sum_j\tau_0(w_{kj}w_{kj}^*)\). A double sum of numbers in \([0,\infty]\) does not depend on the order of summation, so \(\tau(y^*y)=\tau(yy^*)\).

(1) Let \(x\in(eMe)_+\). Then \(v_jx^{1/2}\in eMe\), and by the trace identity of \(\tau_0\), \(\tau_0(v_jxv_j^*)=\tau_0(x^{1/2}f_jx^{1/2})\). The finite partial sums of \(x^{1/2}f_jx^{1/2}\) increase to \(x^{1/2}c(e)x^{1/2}=x\), so normality gives \(\tau(x)=\tau_0(x)\). Also \(v_j(1-c(e))=0\), so \(\tau(1-c(e))=0\).

(2) Let \(\tau'\) be a normal trace with (1), and \(x\in M_+\). Then \(x(1-c(e))\leq\|x\|(1-c(e))\), so \(\tau'(x(1-c(e)))=0\). The finite partial sums of \(x^{1/2}f_jx^{1/2}\) increase to \(x^{1/2}c(e)x^{1/2}=xc(e)\), and \(x^{1/2}f_jx^{1/2}=(v_jx^{1/2})^*(v_jx^{1/2})\). Normality and (2.1) give
\[
\tau'(x)=\tau'(xc(e))=\sum_j\tau'(v_jxv_j^*)=\sum_j\tau_0(v_jxv_j^*)=\tau(x).
\]

(3) *Faithfulness.* If \(\tau\) is faithful on \(Mc(e)\), so is its restriction \(\tau_0\), because \(eMe\subseteq Mc(e)\). Conversely, let \(\tau_0\) be faithful, \(x\in(Mc(e))_+\) and \(\tau(x)=0\). Then \(v_jxv_j^*=0\) for all \(j\), so \(x^{1/2}v_j^*=0\), \(x^{1/2}f_j=0\), and \(x^{1/2}=x^{1/2}c(e)=0\).

*Semifiniteness.* First let \(\tau\) be semifinite, and let \(0\neq x\in(eMe)_+\). Some \(0\neq y\leq x\) has \(\tau(y)<\infty\). Then \(y=eye\in eMe\), since \(0\leq y\leq x\leq\|x\|e\), and \(\tau_0(y)=\tau(y)<\infty\) by (1). So \(\tau_0\) is semifinite.

Conversely, let \(\tau_0\) be semifinite. We check condition (e) of Proposition 2.5, the density of \(\mathfrak m_\tau\).

- Since \(\tau\) vanishes on \(M_+(1-c(e))\), \(\mathfrak m_\tau\supseteq M(1-c(e))\).
- Let \(a\in\mathfrak n_{\tau_0}\) and \(e_k=v_kv_k^*\). In (6.1) for \(v_k^*a^*av_k\), only the term \(j=k\) survives, so
\(\tau((av_k)^*(av_k))=\tau_0(e_ka^*ae_k)=\tau_0(ae_ka^*)\leq\tau_0(aa^*)=\tau_0(a^*a)<\infty\).
So \(av_k\in\mathfrak n_\tau\). Hence \(v_j^*b^*av_k=(bv_j)^*(av_k)\in\mathfrak m_\tau\) for \(a,b\in\mathfrak n_{\tau_0}\); that is, \(v_j^*\mathfrak m_{\tau_0}v_k\subseteq\mathfrak m_\tau\).
- For \(x\in Mc(e)\) and a finite set \(F\subseteq J\) put \(f_F=\sum_{j\in F}f_j\). Then \(f_Fxf_F=\sum_{j,k\in F}v_j^*(v_jxv_k^*)v_k\), with \(v_jxv_k^*\in eMe\). Since \(\tau_0\) is semifinite, Proposition 2.5(e) makes each \(v_jxv_k^*\) a \(\sigma\)-weak limit of elements of \(\mathfrak m_{\tau_0}\). So \(f_Fxf_F\) lies in the \(\sigma\)-weak closure of \(\mathfrak m_\tau\).
- As \(F\) grows, \(f_F\uparrow c(e)\), so \(f_Fxf_F\to x\) \(\sigma\)-weakly.

Every element of \(M\) is \(xc(e)+x(1-c(e))\), so \(\mathfrak m_\tau\) is \(\sigma\)-weakly dense in \(M\). \(\square\)

**Example 6.3** (All normal traces on \(B(H)\)). For \(c\in[0,\infty]\), \(c\operatorname{Tr}\) is a normal trace on \(B(H)\), with \(0\cdot\infty=0\) and \(c\cdot\infty=\infty\) for \(c>0\). Every normal trace \(\tau\) on \(B(H)\) has this form. Indeed, let \(e\) be the projection onto \(\mathbb C\varepsilon_{i_0}\) for an orthonormal basis \((\varepsilon_i)\). The corner \(eB(H)e=\mathbb Ce\) carries the normal trace \(te\mapsto ct\) with \(c=\tau(e)\), and \(c(e)=1\) because \(B(H)\) is a factor. With \(v_j\) the rank-one partial isometry \(\varepsilon_j\mapsto\varepsilon_{i_0}\), Theorem 6.2(2) gives \(\tau(x)=\sum_jc\langle x\varepsilon_j,\varepsilon_j\rangle=c\operatorname{Tr}(x)\). The edge cases: for \(c=\infty\), \(\tau\) is faithful and normal but not semifinite, and Proposition 3.7 gives \(z=0\); for \(c=0\), the support is \(0\) (Proposition 3.2) and \(\tau\) is semifinite; for \(0<c<\infty\), \(\tau\) is faithful, normal and semifinite, and finite exactly when \(\dim H<\infty\). If \(\dim H=\infty\), then \(B(H)\) is properly infinite, and Theorem 5.9(1) says it has no nonzero finite trace at all, normal or not.

### Amplification by a type I factor

Let \(N\) be a von Neumann algebra on \(H\), and \(K\) a Hilbert space with orthonormal basis \((\varepsilon_i)_{i\in I}\). Let \(V_i:H\to H\otimes K\), \(V_i\xi=\xi\otimes\varepsilon_i\), and for \(x\in B(H\otimes K)\) put \(x_{ij}=V_i^*xV_j\). Let \(e_{ij}\in B(K)\) be the matrix units, \(e_{ij}\varepsilon_k=\delta_{jk}\varepsilon_i\). The von Neumann tensor product \(N\bar\otimes B(K)\) is the von Neumann algebra generated by the operators \(a\otimes b\).

**Lemma 6.4.** \(N\bar\otimes B(K)=\{x\in B(H\otimes K):x_{ij}\in N\text{ for all }i,j\}\).

**Proof.** A direct computation gives \((y(1\otimes e_{ij}))_{kl}=\delta_{jl}y_{ki}\) and \(((1\otimes e_{ij})y)_{kl}=\delta_{ik}y_{jl}\). If \(y\) commutes with every \(1\otimes e_{ij}\), comparing these entries gives \(y_{ki}=0\) for \(k\neq i\) and \(y_{ii}=y_{jj}\), so \(y=y_0\otimes1\). If \(y\) also commutes with \(N\otimes1\), then \(y_0\in N'\). So \((N\otimes B(K))'=N'\otimes1\), the other inclusion being clear, and by the bicommutant theorem \(N\bar\otimes B(K)=(N'\otimes1)'\). Finally \(x\) commutes with \(b\otimes1\) (\(b\in N'\)) exactly when \(x_{ij}b=bx_{ij}\) for all \(i,j\), that is, when every \(x_{ij}\) lies in \(N''=N\). \(\square\)

**Proposition 6.5** (Amplification). Let \(\tau\) be a normal trace on \(N\) and \(M=N\bar\otimes B(K)\). Put
\[
\tilde\tau(x)=\sum_{i\in I}\tau(x_{ii})\qquad(x\in M_+).
\tag{6.2}
\]

1. \(\tilde\tau\) is a normal trace on \(M\), and it does not depend on the orthonormal basis.
2. \(\tilde\tau\) is the only normal trace on \(M\) with \(\tilde\tau(y\otimes p)=\tau(y)\) for all \(y\in N_+\), for one (equivalently, every) rank-one projection \(p\in B(K)\).
3. \(\tilde\tau\) is faithful if and only if \(\tau\) is, and semifinite if and only if \(\tau\) is. Its support is \(s(\tilde\tau)=s(\tau)\otimes1\).
4. If \(B\) is any factor of type I, then \(N\bar\otimes B\cong N\bar\otimes B(K)\) for some \(K\), and transporting \(\tilde\tau\) gives a normal trace on \(N\bar\otimes B\) with the same properties. In particular, if \(N\) has a faithful semifinite normal trace, so has \(N\bar\otimes B\).

**Proof.** Fix \(i_0\in I\) and put \(e=1\otimes e_{i_0i_0}\). By Lemma 6.4, \(eMe=\{y\otimes e_{i_0i_0}:y\in N\}\), and \(y\mapsto y\otimes e_{i_0i_0}\) is a \(*\)-isomorphism of \(N\) onto \(eMe\) that preserves order and suprema. So \(\tau_0(y\otimes e_{i_0i_0})=\tau(y)\) is a normal trace on \(eMe\). The partial isometries \(v_j=1\otimes e_{i_0j}\) satisfy \(v_jv_j^*=e\), \(v_j^*v_j=1\otimes e_{jj}\) and \(\sum_jv_j^*v_j=1\); so \(c(e)=1\), and Theorem 6.2 applies. Since \(v_jxv_j^*=x_{jj}\otimes e_{i_0i_0}\), formula (6.1) is exactly (6.2). Theorem 6.2 now shows that \(\tilde\tau\) is a normal trace, gives uniqueness in (2) for \(p=e_{i_0i_0}\), and gives the faithfulness and semifiniteness equivalences in (3).

For a unit vector \(\eta\in K\) with rank-one projection \(p_\eta\), \((y\otimes p_\eta)_{ii}=|\langle\varepsilon_i,\eta\rangle|^2y\), so \(\tilde\tau(y\otimes p_\eta)=\tau(y)\sum_i|\langle\varepsilon_i,\eta\rangle|^2=\tau(y)\). If \((\varepsilon'_k)\) is another basis, the trace built from it agrees with \(\tau\) on the corner of \(1\otimes p_{\varepsilon'_{k_0}}\), by its construction, and so does \(\tilde\tau\), by this computation. That corner also has central support \(1\), so Theorem 6.2(2) makes the two traces equal. This proves (1) and (2).

Support: \(s(\tau)\otimes1\) is a central projection of \(M\). If \(x\in M_+(1-s(\tau)\otimes1)\), every \(x_{ii}\) lies in \(N_+(1-s(\tau))\), so \(\tilde\tau(x)=0\). If \(x\in(M(s(\tau)\otimes1))_+\) and \(\tilde\tau(x)=0\), then \(\tau(x_{ii})=0\) with \(x_{ii}\in N_+s(\tau)\), so \(x_{ii}=0\) for every \(i\); hence \(x^{1/2}V_i=0\) for every \(i\), and \(x=0\). By Proposition 3.2, \(s(\tilde\tau)=s(\tau)\otimes1\).

(4) A factor of type I is \(*\)-isomorphic to some \(B(K)\). Tensoring this isomorphism with the identity map on \(N\) gives \(N\bar\otimes B\cong N\bar\otimes B(K)\) (see "Tensor products of isomorphisms" in the background list). A \(*\)-isomorphism preserves order, suprema and the identity (2.1). \(\square\)

**Example 6.6** (Normality is needed in Theorem 6.2 and Proposition 6.5). Let \(N=\ell^\infty(\mathbb N)\) with the finite trace \(\tau\) of Example 3.4, which is not normal, and \(M=N\bar\otimes B(\ell^2(\mathbb N))\). Let \(x\in M\) have entries \(x_{k1}=1_{\{k\}}\) for \(k\geq1\) and all other entries \(0\); it is a partial isometry. Then \(x^*x=1\otimes e_{11}\) and \(xx^*=\sum_k1_{\{k\}}\otimes e_{kk}\). Formula (6.2), which is (6.1) for the corner of \(1\otimes e_{11}\), gives \(\tilde\tau(x^*x)=\tau(1)=1\) but \(\tilde\tau(xx^*)=\sum_k\tau(1_{\{k\}})=0\). So without normality the formula does not define a trace.

### Faithful semifinite normal traces on semifinite algebras

**Theorem 6.7.** For a von Neumann algebra \(M\) the following are equivalent:

- (i) \(M\) is semifinite;
- (ii) \(M\) has a faithful semifinite normal trace;
- (ii\('\)) \(M\) has a faithful semifinite trace (normality not required).

**Proof.** (ii)\(\Rightarrow\)(ii\('\)) is trivial. (ii\('\))\(\Rightarrow\)(i): let \(\tau\) be faithful and semifinite. If \(\tau(e)<\infty\) for a projection \(e\), then \(\tau\) restricted to \((eMe)_+\) is a faithful finite trace on \(eMe\). A single faithful trace separates \((eMe)_+\), so \(eMe\) is finite by Theorem 4.7 ((iii)\(\Rightarrow\)(i)), and \(e\) is finite by Lemma 1.5. By Proposition 2.5(b), below each nonzero projection lies a nonzero projection of finite trace, and that projection is finite. So \(M\) is semifinite by Proposition 1.6(c).

(i)\(\Rightarrow\)(ii). *Step 1: every nonzero central projection \(z\) majorizes the support of some nonzero semifinite normal trace.* By Proposition 1.6(c) there is a finite projection \(0\neq e\leq z\). The algebra \(eMe\) is finite and nonzero, so Theorem 4.7 gives a finite normal trace \(\tau_0\) on \(eMe\) with \(\tau_0(e)>0\). Its support \(s_0\) is a nonzero central projection of \(eMe\) (Proposition 3.2), and \(\tau_0\) is faithful on \(s_0Ms_0=s_0(eMe)s_0\). Apply Theorem 6.2 to the corner \(s_0\) and the faithful finite normal trace \(\tau_0|_{s_0Ms_0}\). It gives a normal trace \(\tau_z\) on \(M\), semifinite because \(\tau_0\) is finite, faithful on \(Mc(s_0)\) and zero on \(M(1-c(s_0))\). By Proposition 3.2, \(s(\tau_z)=c(s_0)\), which is nonzero and lies below \(c(e)\leq z\).

*Step 2.* By Zorn's lemma, choose a maximal family \((\tau_k)\) of nonzero semifinite normal traces whose supports are pairwise orthogonal. If \(w=1-\sum_ks(\tau_k)\neq0\), Step 1 with \(z=w\) contradicts maximality. So \(\sum_ks(\tau_k)=1\). By Proposition 3.5, \(\tau=\sum_k\tau_k\) is a semifinite normal trace with \(s(\tau)=\bigvee_ks(\tau_k)=1\); that is, \(\tau\) is faithful. \(\square\)

## 7. The trace norm

Let \(\tau\) be a trace on \(M\). As agreed after Lemma 2.4, \(\tau(x)\) means \(\dot\tau(x)\) for \(x\in\mathfrak m_\tau\).

**Proposition 7.1.** For \(x\in\mathfrak m_\tau\) and \(y\in M\):

1. \[
|\tau(yx)|^2\leq\tau(|y^*|\,|x|)\,\tau(|y|\,|x^*|),
\tag{7.1}
\]
where both factors on the right are finite and nonnegative.
2. \[
|\tau(yx)|\leq\tau(|yx|)\leq\|y\|\,\tau(|x|),\qquad \tau(|x^*|)=\tau(|x|).
\tag{7.2}
\]
3. \[
\tau(|x|)=\sup\{|\tau(yx)|:y\in M,\ \|y\|\leq1\}.
\tag{7.3}
\]
4. \(\|x\|_1:=\tau(|x|)\) is a seminorm on \(\mathfrak m_\tau\), and a norm if \(\tau\) is faithful. It satisfies \(\|yx\|_1\leq\|y\|\,\|x\|_1\), \(\|xy\|_1\leq\|y\|\,\|x\|_1\), \(\|x^*\|_1=\|x\|_1\) and \(|\tau(x)|\leq\|x\|_1\).
5. If \(\tau\) is normal, then \(\omega_x=\tau(\,\cdot\,x)\) lies in \(M_*\) and \(\|\omega_x\|=\|x\|_1\).
6. If \(\tau\) is faithful, semifinite and normal, \(\{\omega_x:x\in\mathfrak m_\tau\}\) is norm dense in \(M_*\). Hence the completion \(L^1(M,\tau)\) of \((\mathfrak m_\tau,\|\cdot\|_1)\) is isometrically isomorphic to \(M_*\) through \(x\mapsto\omega_x\), and \(\tau\) and the maps \(x\mapsto yx\), \(x\mapsto xy\) (\(y\in M\)) extend by continuity to \(L^1(M,\tau)\).

**Proof.** Let \(x=u|x|\) and \(y=v|y|\) be polar decompositions. By Lemma 2.4(4), \(|x|\in F_\tau\) and \(|x|^{1/2}\in\mathfrak n_\tau\). Put \(A=|x|^{1/2}v|y|^{1/2}\) and \(B=|y|^{1/2}u|x|^{1/2}\). Both lie in \(\mathfrak n_\tau\), since it is a two-sided ideal.

(1) By (2.3), \(\tau(yx)=\tau\bigl((v|y|u|x|^{1/2})\,|x|^{1/2}\bigr)=\tau(|x|^{1/2}v|y|u|x|^{1/2})=\tau(AB)\). The form \((a,b)\mapsto\tau(b^*a)\) on \(\mathfrak n_\tau\) is positive semidefinite, so \(|\tau(AB)|^2\leq\tau(AA^*)\,\tau(B^*B)\). Now \(AA^*=|x|^{1/2}\,v|y|v^*\,|x|^{1/2}=|x|^{1/2}|y^*||x|^{1/2}\) and \(B^*B=|x|^{1/2}u^*|y|u|x|^{1/2}\). By (2.3), \(\tau(AA^*)=\tau(|y^*||x|)\) and \(\tau(B^*B)=\tau(|y|\,u|x|u^*)=\tau(|y||x^*|)\). Both are traces of elements of \(F_\tau\).

(2) Since \(|y^*|\leq\|y\|\), \(\tau(AA^*)\leq\|y\|\tau(|x|)\). Likewise \(\tau(B^*B)=\tau(|x^*|^{1/2}|y||x^*|^{1/2})\leq\|y\|\tau(|x^*|)\), and \(\tau(|x^*|)=\tau(u|x|u^*)=\tau(|x|u^*u)=\tau(|x|)\). With (1), \(|\tau(yx)|\leq\|y\|\tau(|x|)\). Applied to \(1\) and \(yx\in\mathfrak m_\tau\), this gives \(|\tau(yx)|\leq\tau(|yx|)\). If \(yx=w|yx|\), then \(\tau(|yx|)=\tau(w^*yx)\leq\|w^*y\|\tau(|x|)\leq\|y\|\tau(|x|)\).

(3) \(\tau(|x|)=\tau(u^*x)\) with \(\|u^*\|\leq1\), and (2) gives the reverse inequality.

(4) By (3), \(\|\cdot\|_1\) is a supremum of absolute values of linear functionals, hence a seminorm. If \(\tau\) is faithful and \(\|x\|_1=0\), then \(|x|=0\) and \(x=0\). The first bound is (7.2); the second follows from \(\|xy\|_1=\tau(|(xy)^*|)=\tau(|y^*x^*|)\), from (2) and from \(\tau(|x^*|)=\tau(|x|)\); and \(|\tau(x)|=|\tau(1\cdot x)|\leq\tau(|x|)\).

(5) Let \(x\in F_\tau\) and \(y_\alpha\uparrow y\) in \(M_+\). By (2.3) and normality, \(\omega_x(y_\alpha)=\tau(x^{1/2}y_\alpha x^{1/2})\uparrow\tau(x^{1/2}yx^{1/2})=\omega_x(y)\). So \(\omega_x\) is a normal positive functional, and it lies in \(M_*\) because the two notions of normality agree. As \(\mathfrak m_\tau=\operatorname{span}F_\tau\), \(\omega_x\in M_*\) for every \(x\in\mathfrak m_\tau\). By (3), \(\|\omega_x\|=\|x\|_1\).

(6) Let \(y\in M\) with \(\omega_x(y)=0\) for all \(x\in\mathfrak m_\tau\); we show \(y=0\). Suppose \(y\neq0\) and let \(y=v|y|\). If \(s|y|s=0\) for all \(s\in F_\tau\), then \(|y|^{1/2}s=0\) for all \(s\in F_\tau\), so \(|y|^{1/2}\mathfrak m_\tau=0\). Since \(\mathfrak m_\tau\) is \(\sigma\)-weakly dense (Proposition 2.5(e)) and multiplication is \(\sigma\)-weakly continuous, \(|y|^{1/2}=0\), a contradiction. So some \(s\in F_\tau\) has \(s|y|s\neq0\). Put \(x=s^2v^*\in\mathfrak m_\tau\). By (2.3), \(\omega_x(y)=\tau(ys^2v^*)=\tau(s^2v^*y)=\tau(s^2|y|)=\tau(s|y|s)>0\), by faithfulness, another contradiction. So the subspace \(\{\omega_x\}\) of \(M_*\) has zero annihilator in \((M_*)^*=M\), and it is norm dense by the Hahn–Banach theorem. The map \(x\mapsto\omega_x\) is an isometry from \((\mathfrak m_\tau,\|\cdot\|_1)\) onto a dense subspace of the Banach space \(M_*\), so it extends to an isometric isomorphism of the completion onto \(M_*\). The functional \(\tau\) and the maps \(x\mapsto yx\), \(x\mapsto xy\) are \(\|\cdot\|_1\)-bounded by (4), so they extend. \(\square\)

**Remark.** For \(a\in M\), (2.3) gives \(\omega_{ax}(y)=\omega_x(ya)\) and \(\omega_{xa}(y)=\omega_x(ay)\). By continuity these identities persist on \(L^1(M,\tau)\).

## Exercises

**Exercise 1** (An \(\ell^\infty\)-sum of matrix algebras). Let \(M=\bigoplus_{n\geq1}M_n(\mathbb C)\), the bounded sequences \(x=(x_n)\) with \(x_n\in M_n(\mathbb C)\). (a) Find \(T_M\). (b) Describe all finite normal traces on \(M\). (c) Give a finite trace that is not normal, and check (5.4) for it. (d) Show that \(e\precsim f\) exactly when \(\operatorname{rank}e_n\leq\operatorname{rank}f_n\) for all \(n\).

*Solution.* (a) The center is the algebra of bounded scalar sequences. Let \(\operatorname{tr}_n\) be the normalized trace of \(M_n(\mathbb C)\) and \(T(x)=(\operatorname{tr}_n(x_n))_n\). Then \(T(x^*x)=T(xx^*)\geq0\), \(T\) is linear, \(T(ax)=aT(x)\) for central \(a\), \(T(1)=1\), and \(T(x^*x)=0\) forces every \(x_n=0\). By Theorem 5.5(2), \(T=T_M\). (b) By Theorem 5.5(1), the finite normal traces are \(\psi\circ T\) with \(\psi\) normal and positive on \(\ell^\infty(\mathbb N)\), that is, \(\psi(a)=\sum_nc_na_n\) with \(c_n\geq0\) and \(\sum_nc_n<\infty\). So they are \(\tau(x)=\sum_nc_n\operatorname{tr}_n(x_n)\). (c) For a free ultrafilter \(\omega\), \(\tau(x)=\lim_\omega\operatorname{tr}_n(x_n)\) is a positive functional with \(\tau(x^*x)=\tau(xx^*)\), hence a finite trace. It vanishes on each summand while \(\tau(1)=1\), so it is not normal. It equals \(\psi\circ T\) with \(\psi=\lim_\omega\), which is (5.4). (d) \(T(e)\leq T(f)\) means \(\operatorname{tr}_n(e_n)\leq\operatorname{tr}_n(f_n)\) for all \(n\), that is, \(\operatorname{rank}e_n\leq\operatorname{rank}f_n\); apply Corollary 5.4.

**Exercise 2** (A projection of finite trace need not be finite). Let \(M=\mathbb C\oplus B(\ell^2(\mathbb N))\) and \(\tau(a\oplus x)=a\). Show that \(\tau\) is a finite normal trace, that \(1\) is an infinite projection, and that \(\tau(1)<\infty\). Which step of the proof of (ii\('\))\(\Rightarrow\)(i) in Theorem 6.7 uses faithfulness?

*Solution.* \(\tau\) is a normal positive functional, and \(\tau(z^*z)=|z_1|^2=\tau(zz^*)\) for \(z=z_1\oplus z_2\). With the unilateral shift \(S\), the isometry \(u=1\oplus S\) has \(u^*u=1\) and \(uu^*=1\oplus SS^*\neq1\), so \(1\) is infinite, while \(\tau(1)=1\). The step "\(\tau\) restricted to \(eMe\) is a faithful finite trace, so \(e\) is finite" needs faithfulness; here \(\tau\) vanishes on the infinite summand.

**Exercise 3** (Finite sums of semifinite traces). (a) Show that \(\tau_1+\tau_2\) is semifinite whenever \(\tau_1,\tau_2\) are semifinite traces, normal or not. (b) Explain, with Example 3.6, why the argument does not extend to countable sums.

*Solution.* (a) Let \(0\neq x\in M_+\). Semifiniteness of \(\tau_1\) gives \(0\neq y_1\leq x\) with \(\tau_1(y_1)<\infty\), and semifiniteness of \(\tau_2\) gives \(0\neq y_2\leq y_1\) with \(\tau_2(y_2)<\infty\). Then \(\tau_1(y_2)\leq\tau_1(y_1)<\infty\), so \((\tau_1+\tau_2)(y_2)<\infty\). (b) The argument shrinks \(x\) once for each trace; with infinitely many traces no single nonzero element need survive all the shrinking with a finite total. In Example 3.6 every nonzero \(y\) has \(\sum_n\tau_n(y)=\infty\).

**Exercise 4** (The trace norm in a matrix algebra). In \(M_2(\mathbb C)\) with \(\tau=\operatorname{Tr}\), compute \(\|x\|_1\) for \(x=e_{12}+2e_{21}\), and find \(y\) with \(\|y\|\leq1\) and \(|\operatorname{Tr}(yx)|=\|x\|_1\).

*Solution.* \(x^*=e_{21}+2e_{12}\), so \(x^*x=e_{21}e_{12}+4e_{12}e_{21}=e_{22}+4e_{11}\) and \(|x|=2e_{11}+e_{22}\). Hence \(\|x\|_1=3\). The polar decomposition is \(x=u|x|\) with \(u=e_{12}+e_{21}\), since \(u|x|=2e_{21}+e_{12}\). Take \(y=u^*=e_{12}+e_{21}\), of norm \(1\): \(\operatorname{Tr}(yx)=\operatorname{Tr}(u^*u|x|)=\operatorname{Tr}(|x|)=3\), as in (7.3).

**Exercise 5** (No center-valued trace on \(B(\ell^2)\)). Show that there is no linear map \(T:B(\ell^2(\mathbb N))\to\mathbb C\) with properties (a), (b), (c) of (5.2).

*Solution.* Property (b) is automatic, since the center is \(\mathbb C1\). By (a), \(T\) is a positive linear functional with \(T(x^*x)=T(xx^*)\), that is, a finite trace, and \(T(1)=1\) by (c). But \(B(\ell^2(\mathbb N))\) is properly infinite, so Theorem 5.9(1) forces \(T=0\), a contradiction. This does not conflict with Theorem 5.2, because \(B(\ell^2(\mathbb N))\) is not finite.

## Where this leads

- The trace norm is the first step of integration with respect to a trace. The next steps are the duality between \(M\) and \(L^1(M,\tau)\), the Hilbert space \(L^2(M,\tau)\) with the standard representation of \(M\) on it, measurable operators, and the spaces \(L^p(M,\tau)\). Measurable operators and integration with respect to a trace are treated in the lesson *Measurable operators and the integral for a trace*.
- For a finite algebra, \(T(x)\) lies even in the norm-closed convex hull of the unitary orbit of \(x\). This is Dixmier's approximation theorem; Section 5 needs only the \(\sigma\)-weakly closed hull.
- A semifinite algebra has an extended center-valued trace, with values in the extended positive part of the center.
- Many results above hold for traces that are not normal. Such traces, Dixmier traces for example, have a theory of their own.
- Normal weights drop the identity \(\tau(z^*z)=\tau(zz^*)\). They are the subject of the course *Modular Theory and Weights*.

## References

- [Kostecki] R. P. Kostecki, *W\*-algebras and noncommutative integration*, arXiv:1307.4818. https://arxiv.org/abs/1307.4818
- [Namioka–Asplund 1967] I. Namioka and E. Asplund, *A geometric proof of Ryll-Nardzewski's fixed point theorem*, Bull. Amer. Math. Soc. 73 (1967), 443–445. https://doi.org/10.1090/S0002-9904-1967-11779-8
- [Yeadon 1971] F. J. Yeadon, *A new proof of the existence of a trace in a finite von Neumann algebra*, Bull. Amer. Math. Soc. 77 (1971), 257–260. https://doi.org/10.1090/S0002-9904-1971-12708-8
- [Ryll-Nardzewski 1967] C. Ryll-Nardzewski, *On fixed points of semigroups of endomorphisms of linear spaces*, Proc. Fifth Berkeley Sympos. Math. Statist. and Probability, Vol. II, Part 1, Univ. of California Press, 1967, 55–61. https://digitalassets.lib.berkeley.edu/math/ucb/text/math_s5_v2_p1_article-05.pdf
- [Akemann 1967] C. A. Akemann, *The dual space of an operator algebra*, Trans. Amer. Math. Soc. 126 (1967), 286–302. https://doi.org/10.1090/S0002-9947-1967-0206732-8
- [Dixmier 1949] J. Dixmier, *Les anneaux d'opérateurs de classe finie*, Ann. Sci. École Norm. Sup. 66 (1949), 209–261. https://doi.org/10.24033/asens.970
- [Dixmier 1953] J. Dixmier, *Formes linéaires sur un anneau d'opérateurs*, Bull. Soc. Math. France 81 (1953), 9–39. https://doi.org/10.24033/bsmf.1436
- [Murray–von Neumann 1937] F. J. Murray and J. von Neumann, *On rings of operators. II*, Trans. Amer. Math. Soc. 41 (1937), 208–248. https://www.ams.org/journals/tran/1937-041-02/S0002-9947-1937-1501899-4/S0002-9947-1937-1501899-4.pdf
- [Nelson 1974] E. Nelson, *Notes on non-commutative integration*, J. Funct. Anal. 15 (1974), 103–116. https://doi.org/10.1016/0022-1236(74)90014-7
- [Takesaki I] M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979.
