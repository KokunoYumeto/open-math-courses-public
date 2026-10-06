# The theorem on formal functions

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Independent portions are public domain (CC0). Appendix Z adapts the Stacks project authors’ free conductor and strong-transcendence proofs and retains GFDL-1.2-or-later. See the course notice for authorship and component terms.*

A fiber remembers a family at one parameter. Its successive infinitesimal neighborhoods remember powers of that parameter's maximal ideal. Formal functions identifies the inverse limit of their cohomology with the completion of a finite cohomology module. The individual comparison maps can fail to be isomorphisms; what makes the theorem work is a uniform bound on how long their errors persist.

We use [proper coherent direct images](proper-morphisms-and-coherent-direct-images.md), [affine cohomology and Serre's criterion](affine-cohomology-and-serres-criterion.md), and [flat base change](base-change-and-the-grothendieck-complex.md). Completion, Theorems 3.1–3.3 supplies exact completion of finite modules over Noetherian rings and faithful flatness when the completion ideal lies in the Jacobson radical, including maximal-ideal completion of a Noetherian local ring. The dimension consequences in Section 5 use Cohomological dimension and the Künneth formula, Lemma 7.1, the full Noetherian topological vanishing proof for arbitrary abelian sheaves. No flatness assumption on the coherent sheaf is imposed in this lesson.

## 0. A normality input in the algebraic Zariski Main proof

The quasi-finite input used in Section 5 has an algebraic Zariski Main proof whose supporting coefficient argument requires polynomial normality over an arbitrary normal domain. A proof for polynomial rings over fields alone would not suffice. We supply the general statement here. The valuation existence input is the written Valuation rings and separatedness, Theorem 2.1; it gives a valuation ring in a specified field dominating a specified local subring, without a Noetherian hypothesis or a discrete-value assumption.

**Lemma 0.1 (polynomial normality).** If \(R\) is an integrally closed domain, then \(R[x_1,\ldots,x_n]\) is an integrally closed domain for every finite \(n\).

**Proof.** Put \(F=\operatorname{Frac}R\). First we prove that \(R\) is the intersection of all valuation subrings of \(F\) containing \(R\). If \(z\in F\setminus R\), then \(z\) is not integral over \(R\). In the ring \(R[z^{-1}]\), the element \(z^{-1}\) is not a unit: an equation
\[
1=z^{-1}(a_0+a_1z^{-1}+\cdots+a_mz^{-m})
\]
would yield a monic polynomial equation for \(z\) over \(R\), after multiplication by \(z^{m+1}\). Choose a maximal ideal containing \(z^{-1}\) and localize at it. The earlier valuation theorem gives a valuation ring \(V\subset F\) dominating this local ring. Thus \(R\subset V\), while \(z^{-1}\) is in its maximal ideal and \(z\notin V\). This separates every \(z\notin R\) from the intersection and proves the assertion.

For such a valuation ring, let \(v:F^*\to\Gamma\) be its ordered value group, with \(V=\{0\}\cup\{a:v(a)\geq0\}\). This group can be constructed as \(F^*/V^*\), ordered by divisibility in \(V\). For a nonzero polynomial \(h=\sum a_ix^i\in F[x]\), define
\[
w(h)=\min_i v(a_i),
\]
ignoring zero coefficients. We have \(w(hg)=w(h)+w(g)\): divide each polynomial by a coefficient of least value. The resulting polynomials have coefficients in \(V\) and nonzero reductions in \((V/\mathfrak m_V)[x]\); their product has nonzero reduction because this polynomial ring over a field is a domain. Also \(w(h+g)\geq\min(w(h),w(g))\), with equality when the two values differ. Consequently a sum with a unique term of strictly least value cannot vanish.

Let \(u\in F(x)\) be integral over \(R[x]\). It is integral over \(F[x]\), so \(u\in F[x]\). To justify this last assertion directly, write \(u=a/b\) with coprime polynomials in the Euclidean domain \(F[x]\). A monic integral equation implies that \(b\) divides \(a^m\). Bézout's identity for \(a,b\) forces \(b\) to be a unit. Thus \(u\) is a polynomial.

For every valuation ring \(V\) above, write its integral equation as
\[
u^m+c_1(x)u^{m-1}+\cdots+c_m(x)=0,
\qquad c_i(x)\in R[x]\subset V[x].
\]
If \(w(u)<0\), the term \(u^m\) has value \(m w(u)\), strictly less than the value of every other nonzero term, since \(w(c_i)\geq0\). This contradicts the least-value property. Hence every coefficient of \(u\) belongs to \(V\). The intersection assertion puts all coefficients in \(R\), proving that \(R[x]\) is integrally closed. Induction on the number of variables proves the lemma. \(\square\)

This proof supplies the polynomial-normality step of the supporting algebraic argument. It does not certify all its other inputs; their exact earlier proof locations and remaining audit boundaries are recorded in the prerequisite record.

## 1. The completion map

Let \(A\) be Noetherian, \(I\subset A\) an ideal, \(f:X\to\operatorname{Spec}A\) proper, and \(F\) coherent. For \(n\geq1\), put
\[
X_n=X\times_A\operatorname{Spec}(A/I^n),\qquad F_n=F|_{X_n}.
\]
The closed immersion \(i_n:X_n\hookrightarrow X\) has
\(i_{n*}F_n=F/I^nF\). Since closed immersion pushforward is exact and has no positive direct images, we may compute
\[
H^q(X_n,F_n)=H^q(X,F/I^nF).
\]
Set \(M^q=H^q(X,F)\), a finite \(A\)-module by proper finiteness. The quotient map on sheaves induces
\[
M^q/I^nM^q\longrightarrow H^q(X_n,F_n),
\]
because \(I^n\) annihilates the target. These maps are compatible with reduction from \(n+1\) to \(n\). We seek an isomorphism from
\[
\widehat{M^q}=\varprojlim_n M^q/I^nM^q
\]
to the inverse limit of the right-hand terms. Completion here is with respect to \(I\); neither \(A\) nor \(M^q\) is assumed complete in advance.

The theorem is not a claim that every finite-level map is an isomorphism. For example, the extension bundle on \(\mathbf P^1_{k[t]}\) with class \(t\) has \(H^0(X,E)=0\), but has a nonzero section on the fiber \(t=0\). We will return to its infinitesimal neighborhoods in Exercise 7.6.

## 2. All powers at once

The **Rees algebra** is
\[
R=\bigoplus_{n\geq0}I^nT^n\subset A[T],\qquad R_0=A.
\]
If \(I=(a_1,\ldots,a_r)\), then \(R\) is generated by the degree-one elements \(a_iT\), hence is a quotient of a polynomial algebra in finitely many variables over \(A\). It is Noetherian. The symbol \(T\) records degree; it need not itself belong to \(R\).

**Lemma 2.1 (graded cohomological finiteness).** For each \(q\geq0\), the graded module
\[
Q^q=\bigoplus_{n\geq0}H^q(X,I^nF)T^n
\]
is finite over \(R\).

**Proof.** Form \(X_R=X\times_A\operatorname{Spec}R\), with affine projection \(\pi:X_R\to X\). On \(X\), the graded sheaf \(\bigoplus I^nF\) is a module over \(\mathcal O_X\otimes_A R\): a degree-\(d\) element acts by multiplication into the degree shifted by \(d\). It is a quotient of \(F\otimes_A R\), by the degreewise maps \(F\otimes_A I^n\to I^nF\). The affine module/sheaf correspondence gives a coherent sheaf \(G\) on \(X_R\) with
\[
\pi_*G=\bigoplus_{n\geq0}I^nF.
\]
Coherence follows because \(X_R\) is Noetherian and this sheaf is locally a finite module, generated by a finite set of degree-zero generators of \(F\).

The map \(X_R\to\operatorname{Spec}R\) is proper by base change. Proper cohomology finiteness makes \(H^q(X_R,G)\) finite over \(R\). Affine pushforward and Leray identify it with \(H^q(X,\pi_*G)\). Finally cohomology of quasi-coherent sheaves on the quasi-compact, quasi-separated scheme \(X\) commutes with filtered colimits, by the third lesson. A direct sum is the filtered colimit of finite partial sums, so
\[
H^q(X,\pi_*G)=\bigoplus_{n\geq0}H^q(X,I^nF).
\]
The identifications preserve multiplication and grading. This is the asserted finite graded module. \(\square\)

We next extract two consequences. Write
\[
J_n^q=\operatorname{im}\bigl(H^q(X,I^nF)\to M^q\bigr),
\qquad K_n^q=\ker\bigl(H^q(X,I^nF)\to M^q\bigr).
\]
Both collections respect graded multiplication. Indeed inclusion of ideal powers commutes with multiplying a section or cohomology class by an element of \(I^d\). Thus \(\bigoplus J_n^qT^n\) is a finite graded image module of \(Q^q\), and \(\bigoplus K_n^qT^n\) is a finite graded submodule, using Noetherianness of \(R\).

**Lemma 2.2 (bounds on the image and kernel).** There are integers \(c_J,c_K\geq0\) such that
\[
I^nM^q\subset J_n^q\subset I^{n-c_J}M^q\quad(n\geq c_J),
\]
and the transition map \(K_m^q\to K_n^q\) is zero whenever \(m\geq n+c_K\).

**Proof.** Multiplication by an element of \(I^n\) factors as \(F\to I^nF\to F\), proving the first inclusion. Choose finitely many homogeneous generators of the image module, all in degrees at most \(c_J\). The degree-\(n\) part is a sum of \(I^{n-d}J_d^q\) over generator degrees \(d\leq c_J\). Each is contained in \(I^{n-c_J}M^q\), proving the second inclusion. This is the cohomological analogue of an Artin–Rees bound.

Choose homogeneous kernel generators \(k_\ell\in K_{d_\ell}^q\) with \(d_\ell\leq c_K\). An element of \(K_m^q\) is a sum of products \(a_\ell k_\ell\), with \(a_\ell\in I^{m-d_\ell}\). If \(m\geq n+c_K\), each such coefficient is a sum of products \(ba'\), where \(b\in I^n\) and \(a'\in I^{m-d_\ell-n}\). Under transition to \(H^q(X,I^nF)\), its product with \(k_\ell\) is computed by first including \(I^{d_\ell}F\) into \(F\), then multiplying by \(a'\), then by \(b\) into \(I^nF\). The initial inclusion sends \(k_\ell\) to zero, by definition of the kernel. Hence every product maps to zero. This proves the uniform transition bound. \(\square\)

A system whose sufficiently distant transition maps to each fixed term are zero is called **pro-zero**. Its individual terms may be nonzero; its inverse limit is zero because each coordinate of a compatible family is the image of a distant, necessarily zero, transition. Lemma 2.2 supplies this stronger, bounded form of disappearance for the kernel system.

## 3. Stabilization of the thickened cohomology

The short exact sequence \(0\to I^nF\to F\to F/I^nF\to0\) gives the exact sequence
\[
0\to M^q/J_n^q\longrightarrow H^q(X_n,F_n)\longrightarrow K_n^{q+1}\to0.
\tag{1}
\]
It is a sequence of inverse systems. The left transitions are surjective because \(J_m^q\subset J_n^q\) for \(m\geq n\). The right system is pro-zero by Lemma 2.2 in degree \(q+1\).

**Proposition 3.1 (the Mittag–Leffler bound).** For fixed \(q\), choose \(c\) as the kernel bound in degree \(q+1\). Then for \(m\geq n+c\),
\[
\operatorname{im}\bigl(H^q(X_m,F_m)\to H^q(X_n,F_n)\bigr)
=\operatorname{im}\bigl(M^q\to H^q(X_n,F_n)\bigr).
\]
Consequently the thickened-cohomology system is Mittag–Leffler.

**Proof.** In diagram (1) for indices \(m,n\), the right transition is zero. Therefore the middle transition lands in the left submodule \(M^q/J_n^q\). It contains all of that submodule: the left transition \(M^q/J_m^q\to M^q/J_n^q\) is onto, and these left modules inject into the respective middle terms. Thus its image is exactly the claimed submodule. The image is independent of all sufficiently large \(m\), which is the Mittag–Leffler condition. \(\square\)

We can now take the limit without an unexplained exchange of limits and cohomology. If \((u_n)\) is a compatible family of middle classes in (1), its images in \(K_n^{q+1}\) form a compatible family in a pro-zero system, so are all zero. Thus each \(u_n\) lies in the injective left term, with a unique preimage. These preimages are automatically compatible. We obtain the canonical identification
\[
\varprojlim_n H^q(X_n,F_n)=\varprojlim_n M^q/J_n^q.
\tag{2}
\]
This also proves why a transient class on a small thickening need not define a class in the inverse limit. Compatibility with every higher thickening is a real constraint.

## 4. Global and stalk forms of formal functions

**Theorem 4.1 (formal functions).** Under the hypotheses of Section 1, the canonical maps give an isomorphism
\[
\widehat{H^q(X,F)}\xrightarrow{\sim}\varprojlim_n H^q(X_n,F_n).
\]
It is an isomorphism of \(\widehat A\)-modules and a homeomorphism for their inverse-limit topologies.

**Proof.** Combine (2) with the inclusions from Lemma 2.2:
\[
I^nM^q\subset J_n^q,\qquad J_{n+c_J}^q\subset I^nM^q.
\]
They say that the two descending filtrations \((I^nM^q)\) and \((J_n^q)\) are cofinal. The identification (2) also preserves the limit topologies: each left term is a discrete submodule of the corresponding middle term, and its unique coordinate preimage is continuous on that submodule. The first inclusions give the canonical continuous map between the inverse limits of the corresponding quotients. The second give its inverse by taking the cofinal shifted indices \(n+c_J\). The two composites are the usual transitions and hence induce the identity on limits. Both maps are continuous for the quotient limit topologies, proving the homeomorphism. The maps arise from \(A\)-linear maps at all levels, where \(I^n\) annihilates the cohomology of \(F_n\), and so preserve the induced \(\widehat A\)-action. \(\square\)

**Corollary 4.2 (the stalk form).** Let \(f:X\to S\) be proper, \(S\) locally Noetherian, \(F\) coherent, and \(s\in S\). Put \(A_s=\mathcal O_{S,s}\), with maximal ideal \(\mathfrak m_s\), and
\[
X_n=X\times_S\operatorname{Spec}(A_s/\mathfrak m_s^n),\qquad F_n=F|_{X_n}.
\]
Then
\[
\widehat{(R^qf_*F)_s}\cong\varprojlim_n H^q(X_n,F_n)
\]
as \(\widehat{A_s}\)-modules.

**Proof.** The canonical map \(\operatorname{Spec}A_s\to S\) is flat: on an affine neighborhood it is localization. Flat base change and the affine description of quasi-coherent direct images identify the stalk with \(H^q(X\times_S\operatorname{Spec}A_s,F|_{X\times_S\operatorname{Spec}A_s})\). The local ring is Noetherian, the changed morphism proper, and the changed sheaf coherent. Apply Theorem 4.1 with ideal \(\mathfrak m_s\). Its thickenings are precisely the displayed \(X_n\), since their parameter maps factor through \(\operatorname{Spec}A_s\). \(\square\)

## 5. Dimension and finiteness consequences

**Theorem 5.1 (vanishing above a fiber's dimension).** For the morphism of Corollary 4.2,
\[
(R^qf_*F)_s=0\quad\text{if }q>\dim X_s.
\]

**Proof.** Each \(X_n\) has the same underlying topological space as \(X_s\): the extra ideal is nilpotent and therefore belongs to every prime. That space is Noetherian, of finite dimension \(d\), because \(X_s\) is of finite type over a field. The Noetherian topological vanishing theorem, Cohomological dimension and the Künneth formula, Lemma 7.1, gives \(H^q(X_n,F_n)=0\) for \(q>d\). Formal functions makes the completed stalk zero. The uncompleted stalk is finite by proper coherence. For a finite module over a Noetherian local ring, completion preserves the residue-field quotient; zero completion implies \(M/\mathfrak mM=0\), and Nakayama implies \(M=0\). This proves the assertion. An empty fiber gives empty thickenings and the same conclusion in every degree. \(\square\)

The vanishing is a statement about the whole stalk, stronger than a statement about its tensor with the residue field. In particular, if all fiber dimensions are at most \(d\), then \(R^qf_*F=0\) for \(q>d\), without a flatness assumption.

**Theorem 5.2 (proper with finite fibers is finite).** A proper morphism over a locally Noetherian base whose fibers have finitely many points is finite.

**Proof.** Its fibers are finite type over fields. Such schemes with finitely many points are zero-dimensional by Noether normalization. Indeed an affine chart admits a finite integral surjection onto affine space of its dimension; a positive-dimensional affine space over any field has infinitely many points, so a finite-point chart cannot have positive dimension. Their zero-dimensional coordinate rings are finite-dimensional by Noether normalization. Thus Theorem 5.1 makes \(R^1f_*G=0\) for every coherent \(G\).

Work over an affine Noetherian neighborhood \(S=\operatorname{Spec}A\). Its inverse image \(X\) is Noetherian, separated and quasi-compact. Any finite type ideal \(J\subset\mathcal O_X\) is coherent, and Leray over the affine base gives
\[
H^1(X,J)=\Gamma(S,R^1f_*J)=0.
\]
Here affine vanishing eliminates the other Leray terms, since the direct images are quasi-coherent. The finite-ideal version of Serre's affine criterion from the third lesson now implies that \(X\) is affine. Its function ring \(H^0(X,\mathcal O_X)\) is a finite \(A\)-module by proper cohomology finiteness. Hence \(X\to\operatorname{Spec}A\) is finite. This is local on the base and proves the theorem. \(\square\)

A quasi-finite proper morphism over a locally Noetherian base is therefore finite. The existing earlier *Zariski's Main Theorem* lesson in *Morphisms of schemes* gives another route; the present route uses formal functions and the cohomological affine criterion.

**Corollary 5.3 (a finite fiber has a finite neighborhood).** If \(f:X\to S\) is proper, \(S\) is locally Noetherian, and \(X_s\) is a finite set, then \(f\) is finite over an open neighborhood of \(s\).

**Proof.** The quasi-finite locus is open by the existing earlier *Zariski's Main Theorem*, Theorem 3.1. It contains the entire finite fiber: the pointwise finite-fiber test is proved in *Quasi-finite morphisms and Chevalley*, Theorem 1.1. Its closed complement has closed image in \(S\), by properness, and that image misses \(s\). Remove the image. The restricted map has only finite fibers, and Theorem 5.2 makes it finite. \(\square\)

**Lemma 5.4 (cartesian nilpotent thickenings).** Let \(Y_0\hookrightarrow Y\) be defined by an ideal \(J\) with \(J^N=0\), let \(f:X\to Y\), and put \(X_0=X\times_Y Y_0\). If \(f_0:X_0\to Y_0\) is of finite type, a closed immersion, or proper, respectively, then so is \(f\).

**Proof.** First a nilpotent thickening \(T\) of an affine scheme \(T_0\) is affine. Their topological spaces coincide, so \(T\) is quasi-compact and quasi-separated. For every quasi-coherent \(M\) on \(T\), its finite filtration by powers of the nilpotent ideal has layers which are quasi-coherent on \(T_0\). Affine acyclicity and the cohomology sequences give \(H^1(T,M)=0\). The Serre affine criterion proved in the affine-cohomology lesson now gives affineness.

Work over an affine of \(Y\), and cover \(X_0\) by finitely many affines if \(f_0\) is of finite type. The corresponding open thickenings in \(X\) are affine by the preceding argument. On one of them, write the ring map \(B\to C\). If \(C/JC\) is generated over \(B/J\) by finitely many elements, lift them and let \(D\subset C\) be the \(B\)-subalgebra they generate. Then \(C=D+JC\); iteration gives \(C=D+J^NC=D\). This proves finite type. If \(f_0\) is a closed immersion, \(X_0\) over this affine is affine, hence \(X\) is affine. Surjectivity modulo \(J\) gives \(C=\operatorname{im}(B)+JC\); the same iteration makes \(B\to C\) surjective, proving closed immersion. These affine conclusions are local on the target.

If \(f_0\) is proper, finite type was just proved. Its diagonal is a closed immersion; the diagonal of \(f_0\) is the cartesian nilpotent-base restriction of the diagonal of \(f\), so the closed-immersion result makes \(f\) separated. Finally, after every base change, both the source and target have the same underlying spaces as their nilpotent-base restrictions. Images of closed subsets are therefore closed, because the base change of \(f_0\) is closed. This proves universal closedness and hence properness. \(\square\)

## 6. The blow-up of a plane point

Let \(b:X\to\mathbf A^2_k\) be the blow-up of the origin and \(E\cong\mathbf P^1_k\) its exceptional curve. Its two charts are
\[
U=\operatorname{Spec}k[x,v],\quad y=xv,
\qquad V=\operatorname{Spec}k[u,y],\quad x=uy.
\]
They identify the blow-up with the closed incidence scheme in \(\mathbf A^2\times\mathbf P^1\), so \(b\) is projective and proper. Off the origin it is an isomorphism. The pulled-back origin ideal \(\mathfrak m=(x,y)\) is generated by \(x\) on \(U\) and by \(y\) on \(V\), and is the invertible ideal \(J=\mathcal O_X(-E)\). On the overlap \(y=vx\), so its conormal restriction is \(\mathcal O_E(1)\). Consequently
\[
J^j/J^{j+1}\cong\mathcal O_E(j)\quad(j\geq0).
\]
The positive sign is essential: the normal bundle of \(E\) is \(\mathcal O_E(-1)\), whereas the successive ideal layers use its dual.

The thickened fiber \(X_n\) is defined by \(J^n\). For \(n\geq2\),
\[
0\to\mathcal O_E(n-1)\to\mathcal O_{X_n}\to\mathcal O_{X_{n-1}}\to0.
\]
Projective-line cohomology gives \(H^1(E,\mathcal O_E(j))=0\) for every \(j\geq0\). The long exact sequences, starting with \(X_1=E\), give \(H^1(X_n,\mathcal O_{X_n})=0\) for all \(n\). By formal functions and Nakayama, \((R^1b_*\mathcal O_X)_0=0\). Away from zero the morphism is an isomorphism, so
\[
R^1b_*\mathcal O_X=0.
\]
All still higher direct images vanish by the fiber-dimension bound, because the largest fiber dimension is one.

We can also see the completed degree-zero comparison explicitly. The canonical polynomial map
\[
k[x,y]/(x,y)^n\longrightarrow H^0(X_n,\mathcal O_{X_n})
\]
is an isomorphism. For \(n=1\) both sides are \(k\). At the induction step, its map on the leftmost ideal layers is
\[
(x,y)^{n-1}/(x,y)^n\xrightarrow{\sim}H^0(E,\mathcal O_E(n-1)),
\]
the monomial basis identification from projective-space cohomology. Both the polynomial quotient sequence and the section sequence are short exact, the latter because the layer has zero \(H^1\). Induction proves the isomorphism. Their limits give \(k[[x,y]]\). The unit map from the base local ring to \((b_*\mathcal O_X)_0\) becomes an isomorphism after completion. Exactness and faithful flatness of completion for finite modules make it an isomorphism before completion; off the origin the same holds directly. Thus \(b_*\mathcal O_X=\mathcal O_{\mathbf A^2}\), as well as higher vanishing.

## 7. Exercises with solutions

**Exercise 7.1 (easy: completed constants).** State and prove the completed-stalk formula for \(f_*\mathcal O_X\) at a point of a locally Noetherian base.

**Solution.** For proper \(f\), Corollary 4.2 in degree zero gives
\(\widehat{(f_*\mathcal O_X)_s}=\varprojlim_n H^0(X_n,\mathcal O_{X_n})\), with \(X_n\) defined over \(\mathcal O_{S,s}/\mathfrak m_s^n\). Localization is flat, so identifies the stalk with degree-zero cohomology over the local ring; global formal functions for that ring and ideal gives the formula. All maps preserve multiplication, since they are restriction maps of structure sheaves. Hence it is an isomorphism of complete algebras, not only of modules.

**Exercise 7.2 (medium: the exceptional layers).** Compute the ideal layers of the exceptional curve in the plane blow-up and deduce \(R^1b_*\mathcal O_X=0\).

**Solution.** The local ideal frames are \(x\) and \(y\), related by \(y=vx\); their restriction has the transition of \(\mathcal O_{\mathbf P^1}(1)\). Since the ideal is invertible, its \(j\)-th layer is its restricted \(j\)-th tensor power, \(\mathcal O_{\mathbf P^1}(j)\). Their \(H^1\) groups vanish for \(j\geq0\), so induction on the exact thickening sequences gives zero \(H^1\) on every \(X_n\). Formal functions gives zero completed stalk at the origin, and finite-module Nakayama gives zero stalk. Off the origin the map is an isomorphism, proving the global assertion.

**Exercise 7.3 (medium: finite fibers).** Derive finiteness of a proper morphism with finite fibers using only formal functions, affine cohomology and Serre's criterion.

**Solution.** Every fiber and thickening has dimension zero, so its positive cohomology is zero. Formal functions and Nakayama annihilate \(R^1f_*J\) for every coherent ideal. Over an affine Noetherian base, Leray and affine vanishing give \(H^1(X,J)=0\). The finite-ideal affine criterion makes \(X\) affine. Proper finiteness makes its coordinate algebra finite over the base algebra, which is exactly finiteness of the morphism. This also covers empty fibers.

**Exercise 7.4 (medium: a uniform dimension bound).** If \(\dim X_s\leq d\) for every \(s\), prove \(R^qf_*F=0\) for \(q>d\). Can \(\dim X\) replace the fiber calculation in the proof without further assumptions?

**Solution.** Theorem 5.1 kills every stalk in the stated degrees, hence kills the sheaf. The proof works on the Noetherian topology of each thickened fiber and does not require a dimension bound on the total space. A locally Noetherian base can have unbounded or infinite Krull dimension, so a total-space bound might be unavailable and would in any event miss the sharper relative assertion.

**Exercise 7.5 (hard: the inverse-limit step).** Prove the stabilization and limit claims from (1), without assuming the middle transitions are surjective.

**Solution.** The right transition \(K_m^{q+1}\to K_n^{q+1}\) is zero for \(m\geq n+c\), so the middle image lies in \(M^q/J_n^q\). The left transition is onto, so the middle image contains this entire submodule. Equality proves Mittag–Leffler stabilization. A compatible family in the middle maps to a compatible family in the pro-zero right system. Each of its right coordinates is the image of a sufficiently distant zero transition, so is zero. Each middle coordinate therefore has a unique preimage in the injective left term, and uniqueness forces compatibility of those preimages. Thus the two limits agree. Finally \(I^nM^q\subset J_n^q\) and \(J_{n+c_J}^q\subset I^nM^q\) identify the left limit continuously with the adic completion. Every assertion is justified without finite-level surjectivity of the middle system.

**Exercise 7.6 (challenging: transient infinitesimal sections).** For the extension with class \(t\) on \(\mathbf P^1_{k[t]}\), compute \(H^0\) on every thickening \(B_n=k[t]/(t^n)\), its transition maps, and its inverse limit.

**Solution.** Its Grothendieck complex is \([A\xrightarrow{t}A]\) in degrees zero and one. Over \(B_n\), the kernel of multiplication by \(t\) is \(k\,t^{n-1}\), including \(k\) when \(n=1\). Reduction \(B_{n+1}\to B_n\) sends its kernel generator \(t^n\) to zero. Thus all adjacent transitions on degree-zero cohomology are zero, and its inverse limit is zero. This agrees with the completion of \(H^0(X,E)=0\), although every finite thickening has a nonzero section. In degree one, the cokernel is \(k\) at every level and the transitions are identities; its limit agrees with the completion of \(A/(t)\). This exhibits both the transient error and the persistent cohomology in one family.

## 8. Ampleness near a fiber

**Theorem 8.1.** If \(f:X\to S\) is proper with \(S\) locally Noetherian and \(L|_{X_s}\) is ample, then \(L\) is relatively ample over an open neighborhood of \(s\).

**Proof.** Work first over \(A=\mathcal O_{S,s}\), with maximal ideal \(\mathfrak m\). Put \(X_n=V(\mathfrak m^n\mathcal O_X)\). The layers \(D_n=\mathfrak m^n\mathcal O_X/\mathfrak m^{n+1}\mathcal O_X\) form a finite graded module over \(\mathcal O_{X_1}\otimes_{A/\mathfrak m}\operatorname{gr}_{\mathfrak m}A\): multiplication gives a surjection from that ring onto their direct sum, generated in degree zero. The associated graded ring is Noetherian and finite type. Apply the Serre vanishing theorem to this finite module on the base change of the proper fiber \(X_1\), with the pulled-back ample \(L_1\). Affine pushforward and the finite affine-cover complex split its cohomology by graded degree. Thus one \(d_0\) gives \(H^1(X_1,D_n\otimes L_1^d)=0\) for every \(n\) and every \(d\ge d_0\). The exact thickening sequences consequently lift each section of \(L_1^d\) successively to all \(X_n\). Formal functions identifies the compatible lift with an element of the completion of the finite module \(H^0(X,L^d)\). Its reduction modulo \(\mathfrak m\) comes from that module itself, so the original section lifts to an actual section on \(X\).

Choose \(d\ge d_0\) for which finitely many sections embed the fiber in projective space, using the ample embedding lemma in the Serre lesson. Lift them as above. The local-base cohomology localization proved in the affine lesson represents the finite collection over an affine neighborhood of \(s\). Their evaluation cokernel is coherent; its proper closed support has closed image missing \(s\). Shrink away from that image. They now generate \(L^d\) and define a morphism \(h:X\to\mathbf P^r_S\), proper by the closed-graph factorization, whose fiber at \(s\) is a closed immersion. The quasi-finite open of \(h\) contains all of \(X_s\). Its closed complement has closed image in \(S\), since \(X/S\) is proper. Shrinking once more makes \(h\) quasi-finite everywhere. Theorem 5.2 makes it finite, checked on affine opens of its target. The inverse images of standard affine projective charts are now affine; these are exactly the section opens for the pulled-back coordinate sections of \(L^d=h^*\mathcal O(1)\). They yield an affine basis after allowing all powers of the line bundle. Indeed, on one such affine inverse image \(X_{s_i}\), take any principal open \(D(a)\). Lemma 1.1 of the Serre lesson extends \(a\) to a section \(t\) of a power of \(L^d\), with \(a=t/s_i^b\) on that chart. Multiplying \(t\) once more by \(s_i\) forces its nonvanishing open to be contained in that chart, and that open is exactly \(D(a)\). These principal opens form a basis. Hence \(L^d\) is relatively ample. The positive-power criterion proved in the Serre lesson makes \(L\) relatively ample. \(\square\)

## References

- **[Stacks]** The Stacks project authors, *The Stacks project*, in its AI Integrated Stacks Project edition: graded powers [Tag 02O8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-cohomology-powers-ideal-times-F); filtration consequences [Tag 02OA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-cohomology-powers-ideal-application); Mittag–Leffler [Tag 02OB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-ML-cohomology-powers-ideal); formal functions [Tag 02OC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-theorem-formal-functions); stalk form [Tag 02OD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-formal-functions-stalk).
- Dimension bound [Tag 02V7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-higher-direct-images-zero-above-dimension-fibre), using the open topological theorem [Tag 02UZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-proposition-vanishing-Noetherian); finiteness [Tag 02OG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-characterize-finite). The additional ampleness proof is [Tag 0D2M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-ample-on-fibre) and [Tag 0D2N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-ample-in-neighbourhood).
- These open reference treatments retain GNU FDL 1.2. The independently authored sections, examples and solutions retain CC0; the adapted Appendix Z retains its stated GFDL-1.2-or-later terms.  Sections 2–5 prove the assigned formal-functions, vanishing and finiteness results; the completion algebra belongs to the named prerequisite, and Section 8 proves the additional ampleness consequence.

## Appendix Z. Conductor coefficients and strong transcendence

This appendix supplies the conductor and strong-transcendence arguments used in the algebraic Zariski Main proof. The proofs are written here, at the point where this lesson uses that argument. All rings are commutative with identity and all ring maps preserve identity. “Finite” means finite as a module. The notation \(R[X]\) denotes a polynomial ring in a formal variable; \(R[x]\subset S\) denotes the image algebra generated by an element \(x\in S\). No Noetherian hypothesis is imposed. Reducedness and the domain hypotheses enter only where stated.

*Adapted from The Stacks Project Authors, Johan de Jong and contributors, by GPT-6.1 Sol (OpenAI) in Codex at Ultra effort, October 2026. Copyright (C) 2005–2025 Johan de Jong. This adapted appendix is licensed under the GNU Free Documentation License, version 1.2 or any later version, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. A copy of the license is supplied in COPYING-GFDL-1.2.txt. The lesson’s general CC0 notice does not replace this appendix’s GFDL notice.*

The earlier algebra proofs we use are Integral extensions: lying over, going up and going down, Theorems 1.1–1.2 and Proposition 1.3, for the determinant test, closure and transitivity of integrality, and finite base change; its Theorem 3.2 for lying over and Theorem 4.3 for going down over an arbitrary normal domain; Localization, local properties and support, Section 1 and Theorems 3.1–3.2, for the fraction zero test, prime correspondence and residue-field fibres; Spectra of rings, Theorem 1.2, Theorem 5.2 and Corollary 5.3, for radicals as intersections of primes, clopen subsets and products; and Noetherian and Artinian rings, Lemma 4.1 and Theorem 4.2, for Artinian spectra. The pointwise quasi-finite test, including finiteness of the residue extension and of the local fibre algebra, is proved in Quasi-finite morphisms and Chevalley’s theorem, Theorem 1.1. Polynomial normality over an arbitrary normal domain is Lemma 0.1 of this lesson.

### Z.1. Integral closure and localization

**Lemma Z.1.** Let \(A\to B\) be a ring map, let \(T\subset A\) be multiplicative, and let \(B^{\mathrm{int}}\subset B\) be the subalgebra of elements integral over \(A\). The integral closure of \(T^{-1}A\) in \(T^{-1}B\) is \(T^{-1}B^{\mathrm{int}}\), viewed as a subring of \(T^{-1}B\).

**Proof.** Localization of the inclusion \(B^{\mathrm{int}}\subset B\) is still injective: if a fraction from the first ring becomes zero in the second, a member of \(T\) kills its numerator already in \(B^{\mathrm{int}}\). A monic equation for \(b\in B^{\mathrm{int}}\), divided by the appropriate powers of \(s\in T\), gives a monic equation for \(b/s\) over \(T^{-1}A\). This proves one inclusion.

For the converse write an integral element as \(z=b/s\), with \(b\in B\), \(s\in T\), and choose an equation
\[
z^d+\sum_{i=1}^d \frac{a_i}{t_i}z^{d-i}=0,
\qquad a_i\in A,\quad t_i\in T.
\]
Put \(t=\prod_i t_i\) and \(y=tb\). Multiplication by \((st)^d\) gives, in \(T^{-1}B\),
\[
g(y)=y^d+\sum_{i=1}^d c_i y^{d-i}=0,
\qquad c_i=a_i s^i t^{\,i-1}\prod_{j\ne i}t_j\in A.
\]
Here and below coefficients act through the given ring map. The equation in the localization means that some \(v\in T\) satisfies \(v g(y)=0\) in \(B\). Consequently
\[
(vy)^d+\sum_{i=1}^d v^i c_i (vy)^{d-i}
=v^d g(y)=0
\]
in \(B\). This is a monic equation over \(A\), so \(vy\in B^{\mathrm{int}}\), and \(z=vy/(vts)\) belongs to \(T^{-1}B^{\mathrm{int}}\). No cancellation or nonzero-divisor hypothesis was used. \(\square\)

### Z.2. Removing a monic denominator

**Lemma Z.2.** Let \(\varphi:R[X]\to S\) be a ring map and let \(t\in S\) be integral over \(R[X]\). Suppose that for some monic \(p\in R[X]\) the element \(t\varphi(p)\) belongs to \(\operatorname{im}\varphi\). There is \(q\in R[X]\) such that \(t-\varphi(q)\) is integral over \(R\).

**Proof.** If \(S\) is the zero ring, take \(q=0\), so assume otherwise. Choose \(r\in R[X]\) with \(t\varphi(p)=\varphi(r)\). Division by a monic polynomial works over every ring: if the current dividend has degree at least \(\deg p\), subtract its leading coefficient times the appropriate power of \(X\) times \(p\); its degree decreases, and finitely many repetitions give \(r=qp+r'\) with \(\deg r'<\deg p\). If \(p=1\), take \(q=r\); the difference is zero. Otherwise put \(\tau=t-\varphi(q)\). Integral elements form a subalgebra by the earlier Theorem 1.2, so \(\tau\) is still integral over \(R[X]\), and
\[
\tau\varphi(p)=\varphi(r').
\]
In \(S_\tau\) this becomes \(\varphi(p)-\tau^{-1}\varphi(r')=0\). Since \(p\) is monic and \(r'\) has smaller degree, this is a monic equation for \(x=\varphi(X)\) over the subring \(D=\varphi(R)[1/\tau]\subset S_\tau\). Thus \(D[x]\) is integral over \(D\). The original integral equation for \(\tau\), now regarded in \(S_\tau\), also shows that \(\tau\) is integral over \(D[x]\). Transitivity, proved in the earlier Theorem 1.2, makes \(\tau\) integral over \(D\). We can therefore write
\[
\tau^d+\sum_{i<d}\left(\sum_{j=0}^{n_i}
\frac{\varphi(b_{ij})}{\tau^j}\right)\tau^i=0
\quad\text{in }S_\tau,
\qquad b_{ij}\in R.
\]
Choose an integer \(N\) large enough to clear all displayed negative powers and to kill the resulting localization error. More explicitly, first clear those powers; the resulting element of \(S\) becomes zero in \(S_\tau\), so some further power of \(\tau\) kills it. Combining the two powers gives
\[
\tau^{d+N}+\sum_{i<d}\sum_{j=0}^{n_i}
\varphi(b_{ij})\tau^{i+N-j}=0
\quad\text{in }S.
\]
Every lower exponent is nonnegative and strictly less than \(d+N\). This is a monic equation for \(\tau\) over \(R\), even when \(\tau\) is a zero divisor. \(\square\)

### Z.3. Clearing a leading coefficient

**Lemma Z.3.** Let \(\varphi:R[X]\to S\) be a ring map, let \(t\in S\) be integral over \(R[X]\), and let
\[
p=\sum_{i=0}^k a_iX^i\in R[X]
\]
satisfy \(t\varphi(p)\in\operatorname{im}\varphi\). Then there are an integer \(n\geq0\) and \(q\in R[X]\) such that \(\varphi(a_k)^n t-\varphi(q)\) is integral over \(R\).

**Proof.** Write \(a=a_k\). If \(a\) is nilpotent in \(R\), choose a power \(a^n=0\) and take \(q=0\). Otherwise localize \(R\) at \(a\), and \(S\) at \(\varphi(a)\). The polynomial \(p/a\in R_a[X]\) is monic, so Lemma Z.2 gives \(q'\in R_a[X]\) for which \(t-\varphi_a(q')\) is integral over \(R_a\). Choose \(e\geq0\) and \(q_0\in R[X]\) such that \(q_0/1=a^e q'\). Multiplication by \(a^e\) preserves integrality, since integral elements form an \(R_a\)-subalgebra. Hence the image in \(S_{\varphi(a)}\) of
\[
\delta=\varphi(a)^e t-\varphi(q_0)
\]
is integral over \(R_a\).

By Lemma Z.1, this image can be written as \(c/\varphi(a)^j\), where \(c\in S\) is integral over \(R\). Equality of these two fractions means that for some \(\ell\geq0\),
\[
\varphi(a)^\ell\bigl(\varphi(a)^j\delta-c\bigr)=0
\quad\text{in }S.
\]
Thus \(\varphi(a)^{j+\ell}\delta=\varphi(a)^\ell c\) is integral over \(R\). Taking \(n=e+j+\ell\) and \(q=a^{j+\ell}q_0\) proves the assertion. This last step explicitly clears the possible localization error. \(\square\)

### Z.4. The conductor setup

**Situation Z.4.** Let \(\varphi:R[X]\to S\) be finite, put \(A=\varphi(R)\), \(x=\varphi(X)\), and \(C=A[x]=\operatorname{im}\varphi\). Assume that \(A\) is integrally closed in \(S\): every element of \(S\) integral over \(A\) belongs to \(A\). This condition concerns this inclusion; it does not require \(A\) to be a domain. Define the conductor
\[
J=\{g\in S:gS\subset C\}.
\]
It is an ideal of \(S\): sums preserve the defining condition, and \(hgS\subset gS\) for \(h\in S\). Also \(J\subset C\), by evaluating on \(1\).

Choose \(C\)-module generators \(t_1,\ldots,t_r\) of \(S\), adding \(1\) if needed. For \(g\in S\), we have \(g\in J\) exactly when \(gt_i\in C\) for all \(i\). Indeed, this condition makes every \(C\)-linear combination of the \(gt_i\) belong to \(C\). These observations also cover the zero ring.

### Z.5. The leading coefficient enters the conductor

**Lemma Z.5.** In Situation Z.4, let \(u\in S\) and \(p=\sum_{i=0}^k a_iX^i\in R[X]\). If \(u\varphi(p)\in J\), there is \(m\geq0\) such that \(u\varphi(a_k)^m\in J\).

**Proof.** For each module generator \(t_i\), the element \(ut_i\in S\) is integral over \(R[X]\), because \(S\) is finite over \(R[X]\) and the earlier determinant test proves finite algebras integral. Moreover
\[
(ut_i)\varphi(p)=(u\varphi(p))t_i\in C.
\]
Lemma Z.3 gives \(n_i\geq0\) and \(q_i\in R[X]\) such that
\[
\varphi(a_k)^{n_i}ut_i-\varphi(q_i)
\]
is integral over \(R\), equivalently over its image \(A\). The integral-closedness assumption puts this difference in \(A\subset C\); hence \(\varphi(a_k)^{n_i}ut_i\in C\). With \(m=\max_i n_i\), multiplication by additional powers of \(\varphi(a_k)\in C\) gives \(u\varphi(a_k)^m t_i\in C\) for every \(i\). The generator characterization in Situation Z.4 now gives \(u\varphi(a_k)^m\in J\). \(\square\)

### Z.6. Every coefficient enters the radical

**Lemma Z.6.** In Situation Z.4, if \(u\varphi(p)\in\sqrt J\), where \(u\in S\) and \(p=\sum_{i=0}^k a_iX^i\), then \(u\varphi(a_i)\in\sqrt J\) for every \(i\).

**Proof.** Choose \(N\geq1\) with \(u^N\varphi(p^N)\in J\). The coefficient of \(X^{kN}\) in \(p^N\) is \(a_k^N\), so Lemma Z.5 gives
\[
u^N\varphi(a_k)^{Nm}\in J
\]
for some \(m\geq0\). Increase \(m\) to at least \(1\), which is allowed because \(J\) is an ideal. Then
\[
(u\varphi(a_k))^{Nm}
=u^{N(m-1)}\bigl(u^N\varphi(a_k)^{Nm}\bigr)\in J.
\]
Thus \(u\varphi(a_k)\in\sqrt J\). Subtracting the term \(u\varphi(a_k)x^k\) from \(u\varphi(p)\) leaves \(u\varphi(p-a_kX^k)\in\sqrt J\). Induction on the chosen top index \(k\) proves the assertion for all coefficients; for \(k=0\) the first step already proves it. \(\square\)

### Z.7. Strong transcendence and the conductor quotient

**Definition Z.7.** For an inclusion \(R\subset S\), an element \(x\in S\) is **strongly transcendental over \(R\)** if every equation
\[
u\sum_{i=0}^k a_ix^i=0,
\qquad u\in S,\quad a_i\in R,
\]
implies \(ua_i=0\) for every \(i\). If \(R\subset S\) are domains, this is equivalent to ordinary transcendence: the case \(u=1\) gives injectivity of \(R[X]\to S\), and conversely a nonzero \(u\) can be cancelled in a domain.

In Situation Z.4 put
\[
S_0=S/\sqrt J,\qquad A_0=A/(A\cap\sqrt J)\subset S_0,
\]
and let \(x_0\) be the image of \(x\). Then \(A_0\) and \(S_0\) are reduced, \(S_0\) is finite over \(A_0[x_0]\), and \(x_0\) is strongly transcendental over \(A_0\).

**Proof of the assertion.** The displayed map from \(A_0\) is injective by its definition. The ring \(S_0\) is reduced because the quotient ideal is radical; its subring \(A_0\) is therefore reduced. The images of the finite \(C\)-module generators of \(S\) generate \(S_0\) over the image \(A_0[x_0]\).

Given a relation \(u_0\sum_i\bar a_i x_0^i=0\), lift \(u_0\) to \(u\in S\), the \(\bar a_i\) to \(a_i\in A\), and these coefficients to \(r_i\in R\) with \(\varphi(r_i)=a_i\). The relation says \(u\varphi(\sum_i r_iX^i)\in\sqrt J\). Lemma Z.6 gives \(ua_i\in\sqrt J\) for every \(i\), which is precisely \(u_0\bar a_i=0\) in \(S_0\). \(\square\)

### Z.8. Quasi-finiteness in a four-ring diagram

**Lemma Z.8.** Consider a commutative square of rings
\[
\begin{array}{ccc}
R&\longrightarrow&S\\
\downarrow&&\downarrow\\
R'&\longrightarrow&S'.
\end{array}
\]
Let \(\mathfrak q'\subset S'\) contract to \(\mathfrak q\subset S\) and \(\mathfrak p'\subset R'\); write \(\mathfrak p=\mathfrak q\cap R=\mathfrak p'\cap R\). Suppose \(R\to S\) is of finite type and the canonical map \(S\otimes_R R'\to S'\) is surjective. If \(R\to S\) is quasi-finite at \(\mathfrak q\), then \(R'\to S'\) is quasi-finite at \(\mathfrak q'\).

**Proof.** Put \(k=\kappa(\mathfrak p)\), \(k'=\kappa(\mathfrak p')\), \(F=S\otimes_R k\), and \(F'=S'\otimes_{R'}k'\). The contractions give field inclusions \(k\subset k'\) and \(\kappa(\mathfrak q)\subset\kappa(\mathfrak q')\). The fibre prime corresponding to \(\mathfrak q\) is isolated by quasi-finiteness, and is closed by the earlier pointwise test. Its singleton is consequently clopen in \(\operatorname{Spec}F\).

The clopen-idempotent theorem and product decomposition proved in the earlier spectra lesson give
\[
F=F_1\times F_2,
\]
with the singleton as \(\operatorname{Spec}F_1\). The ring \(F_1\) has only one prime, which is its unique maximal ideal. Elements outside this ideal are units, so localization at it does not change \(F_1\). Thus \(F_1\) is the local fibre ring at \(\mathfrak q\), and the earlier pointwise test makes \(F_1\) finite-dimensional over \(k\).

Tensoring the assumed surjection with \(k'\) gives a surjection
\[
F\otimes_k k'\longrightarrow F'.
\]
The complementary idempotents of \(F\) give \(F'=F'_1\times F'_2\), with surjections \(F_i\otimes_k k'\to F'_i\). In particular \(F'_1\) is finite-dimensional over \(k'\). The composite \(F\to F'\to\kappa(\mathfrak q')\) factors through \(\kappa(\mathfrak q)\): it is induced by the ring map and the contraction \(\mathfrak q'\cap S=\mathfrak q\). Therefore it kills the \(F_2\) idempotent, just as \(F\to\kappa(\mathfrak q)\) does. The point \(\mathfrak q'\) consequently belongs to \(\operatorname{Spec}F'_1\).

A finite-dimensional algebra over a field is Artinian, since a descending chain of ideals is a descending chain of vector subspaces. The earlier Artinian theorem makes its spectrum a finite set of closed points, hence discrete: the complement of each point is a finite union of closed points. Thus \(\mathfrak q'\) is isolated in \(\operatorname{Spec}F'_1\), and in \(\operatorname{Spec}F'\), because this factor is open and closed. Finally \(R'\to S'\) is of finite type: \(S'\) is a quotient of the finite type \(R'\)-algebra \(S\otimes_R R'\). This verifies both parts of the quasi-finite condition. \(\square\)

### Z.9. Passage to a minimal prime

**Lemma Z.9.** Let \(R\subset S\) be an inclusion of reduced rings, let \(x\in S\) be strongly transcendental over \(R\), and let \(\mathfrak q\) be a minimal prime of \(S\). Put \(\mathfrak p=R\cap\mathfrak q\). The image of \(x\) in \(S/\mathfrak q\) is strongly transcendental over \(R/\mathfrak p\).

**Proof.** We first justify the local fact used here without a Noetherian assumption. The localization \(S_{\mathfrak q}\) is reduced. Indeed, if \((y/s)^n=0\), then some \(v\notin\mathfrak q\) satisfies \(vy^n=0\); hence \((vy)^n=0\) and reducedness of \(S\) gives \(vy=0\), so \(y/s=0\). Prime correspondence identifies the primes of \(S_{\mathfrak q}\) with primes of \(S\) contained in \(\mathfrak q\). Minimality leaves only \(\mathfrak qS_{\mathfrak q}\). The intersection-of-primes description of the nilradical, together with reducedness, therefore gives \(\mathfrak qS_{\mathfrak q}=0\). This local ring has zero maximal ideal, so is a field.

Now suppose \(u\sum_i a_ix^i\in\mathfrak q\), with \(u\in S\) and \(a_i\in R\). This element becomes zero in \(S_{\mathfrak q}\), so there is \(v\notin\mathfrak q\) such that \(vu\sum_i a_ix^i=0\) in \(S\). Strong transcendence gives \(vua_i=0\) for every \(i\). Since \(\mathfrak q\) is prime and \(v\notin\mathfrak q\), we get \(ua_i\in\mathfrak q\) for every \(i\). These are exactly the required coefficient equalities after quotienting. The induced map \(R/\mathfrak p\to S/\mathfrak q\) is an inclusion by the contraction defining \(\mathfrak p\). \(\square\)

### Z.10. Transcendence excludes quasi-finite points for domains

**Lemma Z.10.** Suppose \(R\subset S\) are domains, \(x\in S\) is transcendental over \(R\), and \(S\) is finite over \(R[x]\). Then \(R\to S\) is not quasi-finite at any prime of \(S\).

**Proof.** The map \(R\to S\) is of finite type: the element \(x\), together with a finite list of \(R[x]\)-module generators of \(S\), generates \(S\) as an \(R\)-algebra.

First assume \(R\) is normal, meaning integrally closed in its fraction field. Transcendence identifies \(R[x]\) with \(R[X]\); Lemma 0.1 above proves that it is normal. Fix \(\mathfrak q\subset S\), put \(\mathfrak p=R\cap\mathfrak q\) and \(\mathfrak r=R[x]\cap\mathfrak q\), and suppose for contradiction that \(R\to S\) is quasi-finite at \(\mathfrak q\). The earlier pointwise test gives a finite field extension \(\kappa(\mathfrak p)\subset\kappa(\mathfrak q)\). The intermediate field
\[
\kappa(\mathfrak p)\subset\kappa(\mathfrak r)
\subset\kappa(\mathfrak q)
\]
is therefore finite over \(\kappa(\mathfrak p)\). The containment \(\mathfrak pR[x]\subset\mathfrak r\) must be strict: equality would give \(\kappa(\mathfrak r)=\kappa(\mathfrak p)(X)\), a transcendental extension.

The inclusion \(R[x]\subset S\) is integral, by its finiteness. The earlier going-down theorem for an integral inclusion of domains with normal base gives a prime \(\mathfrak q_0\subset\mathfrak q\) of \(S\) contracting to \(\mathfrak pR[x]\). It is distinct from \(\mathfrak q\), because their contractions to \(R[x]\) differ. Both primes contract to \(\mathfrak p\) in \(R\), so they are distinct points of the same fibre, with \(\mathfrak q_0\) specializing to \(\mathfrak q\). Every open containing a point contains its generizations, as is seen on the basic opens \(D(f)\). Thus \(\mathfrak q\) cannot be isolated in that fibre. This contradicts quasi-finiteness.

For arbitrary \(R\), put \(K=\operatorname{Frac}R\), \(L=\operatorname{Frac}S\), let \(R'\) be the integral closure of \(R\) in \(K\), and let \(S'\subset L\) be the subring generated by \(S\) and \(R'\). These are domains. The ring \(R'\) is normal: an element of \(K\) integral over \(R'\) is integral over \(R\) by transitivity, and hence belongs to \(R'\). Its fraction field is \(K\), because \(R\subset R'\subset K\).

The element \(x\) remains transcendental over \(R'\). Any relation over \(R'\subset K\), after multiplying by a common nonzero denominator from \(R\), would give a relation over \(R\). By construction \(S\otimes_R R'\to S'\) is surjective. If \(t_1,\ldots,t_r\) generate \(S\) over \(R[x]\), their images generate \(S'\) over \(R'[x]\): they generate the tensor product over \(R[x]\otimes_R R'=R'[X]\), and therefore its quotient \(S'\). Hence \(S'\) is finite over \(R'[x]\).

Every element of \(R'\) is integral over \(S\), since its monic equation has coefficients in \(R\subset S\). Closure of integral elements under algebra generation makes \(S\subset S'\) integral. Lying over, in the earlier Theorem 3.2, gives a prime \(\mathfrak q'\subset S'\) above any prescribed prime \(\mathfrak q\subset S\). If \(R\to S\) were quasi-finite at \(\mathfrak q\), Lemma Z.8 applied to \(R,S,R',S'\) would make \(R'\to S'\) quasi-finite at \(\mathfrak q'\), contradicting the normal case. This uses neither finiteness of \(R'\) over \(R\) nor Noetherianity. \(\square\)

### Z.11. Strong transcendence excludes quasi-finite points

**Lemma Z.11.** Suppose \(R\subset S\) are reduced rings, \(x\in S\) is strongly transcendental over \(R\), and \(S\) is finite over \(R[x]\). Then \(R\to S\) is not quasi-finite at any prime of \(S\).

**Proof.** Again \(R\to S\) is of finite type. Fix a prime \(\mathfrak q\subset S\) and choose a minimal prime \(\mathfrak q_0\subset\mathfrak q\). Such a prime exists without Noetherianity: order the primes contained in \(\mathfrak q\) by reverse inclusion. A nonempty chain has an upper bound given by its intersection, which is a proper prime ideal contained in \(\mathfrak q\). To check primality, if neither \(a\) nor \(b\) belongs to that intersection, choose members of the chain omitting each; the smaller of these two prime ideals omits both and therefore omits \(ab\). The empty chain is bounded by \(\mathfrak q\). Zorn’s lemma now gives a minimal prime.

Put \(\mathfrak p_0=R\cap\mathfrak q_0\), \(R_0=R/\mathfrak p_0\), and \(S_0=S/\mathfrak q_0\). The induced inclusion \(R_0\subset S_0\) is an inclusion of domains. By Lemma Z.9, the image \(x_0\) is strongly transcendental, and hence transcendental, over \(R_0\). The quotient \(S_0\) remains finite over \(R_0[x_0]\), by the images of the same module generators. Lemma Z.10 says that \(R_0\to S_0\) is not quasi-finite at \(\mathfrak q/\mathfrak q_0\).

The square \(R,S,R_0,S_0\) satisfies the hypotheses of Lemma Z.8: its tensor-product map is surjective, because \(S\otimes_R R_0=S/\mathfrak p_0S\) surjects onto \(S/\mathfrak q_0\). If \(R\to S\) were quasi-finite at \(\mathfrak q\), that lemma would make \(R_0\to S_0\) quasi-finite at \(\mathfrak q/\mathfrak q_0\), a contradiction. This proof does not require finitely many minimal primes. \(\square\)

### Z.12. The conductor is avoided at a quasi-finite point

**Corollary Z.12.** In Situation Z.4, if \(A\to S\) is quasi-finite at a prime \(\mathfrak q\subset S\), then \(J\not\subset\mathfrak q\).

**Proof.** Suppose \(J\subset\mathfrak q\). Then \(\sqrt J\subset\mathfrak q\). Use the reduced rings \(A_0\subset S_0=S/\sqrt J\) and the strongly transcendental element \(x_0\) constructed in Z.7. They satisfy the hypotheses of Lemma Z.11, so \(A_0\to S_0\) is not quasi-finite at \(\mathfrak q/\sqrt J\).

On the other hand \(A\to S\) is of finite type, because \(S\) is finite over \(A[x]\). The square \(A,S,A_0,S_0\) has surjective tensor-product map: the quotient \(S/(A\cap\sqrt J)S\) surjects onto \(S/\sqrt J\). Lemma Z.8 therefore transfers quasi-finiteness at \(\mathfrak q\) to quasi-finiteness at \(\mathfrak q/\sqrt J\), giving the contradiction. \(\square\)

For the finite-over-one-generator step of Zariski’s Main Theorem, Section 2, Lemma 2.1, this corollary supplies precisely the conductor element outside the chosen prime. Lemma Z.6 supplies the preceding coefficient assertion, and Lemma Z.11 supplies the reduced strong-transcendence assertion. These are the two supporting arguments required there; the earlier lesson contains the separate monogenic argument and the main induction.

**Source and license record.** The arguments adapted here are the bodies with Stacks tags 0307, 00PT, 00PV, 00PW (the situation), 00PX, 00PY, 00PN, 00Q0, 00Q1 and 00Q2, together with the definition labelled “definition-strongly-transcendental”, in the [frozen AI Integrated Stacks Project algebra source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex). Tags identify the adapted bodies and their authorship; the mathematical dependencies in this appendix are the written proofs above and the exact earlier programme lessons identified in its opening paragraph. The source’s GFDL authorship and license conditions remain attached to this adapted text.
