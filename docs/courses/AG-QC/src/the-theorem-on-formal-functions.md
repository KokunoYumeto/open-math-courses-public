# The theorem on formal functions

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026; Appendix Z by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Original text: public domain (CC0). See the course notice for authorship.*

A fiber remembers a family at one parameter. Its successive infinitesimal neighborhoods remember powers of that parameter's maximal ideal. Formal functions identifies the inverse limit of their cohomology with the completion of a finite cohomology module. The individual comparison maps can fail to be isomorphisms; what makes the theorem work is a uniform bound on how long their errors persist.

We use proper coherent direct images, [affine cohomology and Serre's criterion](affine-cohomology-and-serres-criterion.md), and [flat base change](base-change-and-the-grothendieck-complex.md). Completion, Theorems 3.1–3.3 supplies exact completion of finite modules over Noetherian rings and faithful flatness when the completion ideal lies in the Jacobson radical, including maximal-ideal completion of a Noetherian local ring. The dimension consequences in Section 5 use Cohomological dimension and the Künneth formula, Lemma 7.1, the full Noetherian topological vanishing proof for arbitrary abelian sheaves. No flatness assumption on the coherent sheaf is imposed in this lesson.

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

This proof supplies the polynomial-normality step of the supporting algebraic argument. Not all of the other inputs of that argument are proved here.

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
- The linked Stacks Project texts are under GNU FDL 1.2. Sections 2–5 prove the assigned formal-functions, vanishing and finiteness results; the completion algebra belongs to the named prerequisite, and Section 8 proves the additional ampleness consequence.

## Appendix Z. Conductor coefficients and strong transcendence

Lemma 2.1 of Zariski’s Main Theorem, Section 2, treats an algebra that is finite over one generator. It needs two facts about a finite algebra over a polynomial ring: the coefficients of a polynomial that lands in the radical of the conductor land there one by one, and a strongly transcendental element rules out quasi-finite points. This appendix proves both, together with the lemmas they rest on. Rings are commutative with \(1\), ring maps preserve \(1\), and “finite” means finite as a module. We write \(R[X]\) for a polynomial ring and \(R[x]\subset S\) for the subalgebra generated by an element \(x\in S\). No ring is assumed Noetherian; reducedness and integrality hypotheses are stated where they are used.

We rely on these earlier results. From Integral extensions: lying over, going up and going down: the determinant test and the closure and transitivity of integrality (Theorems 1.1–1.2, Proposition 1.3), lying over (Theorem 3.2) and going down over a normal domain (Theorem 4.3). From Localization, local properties and support, Section 1 and Theorems 3.1–3.2: when a fraction is zero, the correspondence of primes, and fibres as spectra of residue-field base changes. From Spectra of rings, Theorem 1.2, Theorem 5.2 and Corollary 5.3: the nilradical as the intersection of primes, and open-and-closed subsets as product decompositions. From Noetherian and Artinian rings, Lemma 4.1 and Theorem 4.2: spectra of Artinian rings. A prime of a finite type algebra is a quasi-finite point exactly when its residue field and its local fibre algebra are finite over the residue field below; this pointwise criterion is Quasi-finite morphisms and Chevalley’s theorem, Theorem 1.1. Polynomial rings over a normal domain are normal by Lemma 0.1 above.

### Z.1. Integral closure and localization

**Lemma Z.1.** For a ring map \(A\to B\) and a multiplicative subset \(T\subset A\), write \(B^{\mathrm{int}}\subset B\) for the subring of elements integral over \(A\). Inside \(T^{-1}B\), the integral closure of \(T^{-1}A\) equals \(T^{-1}B^{\mathrm{int}}\).

**Proof.** Localization is exact, so \(T^{-1}B^{\mathrm{int}}\) is a subring of \(T^{-1}B\). If \(b\) satisfies \(b^d+a_1b^{d-1}+\cdots+a_d=0\) with \(a_i\in A\), then dividing by \(s^d\), for \(s\in T\), gives the monic equation \((b/s)^d+(a_1/s)(b/s)^{d-1}+\cdots+a_d/s^d=0\) over \(T^{-1}A\). So \(T^{-1}B^{\mathrm{int}}\) is integral over \(T^{-1}A\).

Conversely, suppose \(z=b/s\) satisfies \(z^d+\sum_{i=1}^d(a_i/t_i)z^{d-i}=0\) with \(a_i\in A\) and \(t_i\in T\). Put \(t=t_1\cdots t_d\) and \(y=tb\). Multiplying the equation by \((ts)^d\) turns it into

\[
g(y)=y^d+\sum_{i=1}^dc_iy^{d-i}=0\ \text{ in }T^{-1}B,\qquad c_i=a_i\,\frac{t}{t_i}\,t^{\,i-1}s^i\in A .
\]

So some \(v\in T\) has \(vg(y)=0\) in \(B\), and then \(0=v^dg(y)=(vy)^d+\sum_iv^ic_i(vy)^{d-i}\). Hence \(vy\in B^{\mathrm{int}}\), and \(z=vy/(vts)\) lies in \(T^{-1}B^{\mathrm{int}}\). Zero divisors cause no difficulty here, since the factor \(v\) has been absorbed into the element. \(\square\)

### Z.2. Removing a monic denominator

**Lemma Z.2.** Suppose \(\varphi:R[X]\to S\) is a ring map and \(t\in S\) is integral over \(R[X]\). If \(t\varphi(p)\in\operatorname{im}\varphi\) for a monic \(p\in R[X]\), then \(t-\varphi(q)\) is integral over \(R\) for some \(q\in R[X]\).

**Proof.** Write \(t\varphi(p)=\varphi(r)\). Long division by the monic \(p\) works over any ring and gives \(r=qp+r'\) with \(\deg r'<\deg p\). Put \(\tau=t-\varphi(q)\); then \(\tau\varphi(p)=\varphi(r')\), and \(\tau\) is integral over \(R[X]\) because integral elements form a subring. If \(\deg p=0\), then \(p=1\), \(r'=0\) and \(\tau=0\). Let \(\deg p=n\ge1\) and pass to \(S_\tau\), where \(\tau\) is a unit. There \(x=\varphi(X)\) satisfies

\[
p(x)-\tau^{-1}r'(x)=0,
\]

a monic equation of degree \(n\) over the subring \(D=\varphi(R)[\tau^{-1}]\), because \(\deg r'<n\). So \(D[x]\) is integral over \(D\). The image of \(\tau\) in \(S_\tau\) is integral over the image of \(R[X]\), which lies in \(D[x]\), and by transitivity \(\tau\) is integral over \(D\). Write such an equation as \(\tau^m+\sum_{i<m}d_i\tau^i=0\) with \(d_i=\sum_{j=0}^{N}\varphi(b_{ij})\tau^{-j}\), \(b_{ij}\in R\). Multiplying by \(\tau^N\) gives an equation in \(S_\tau\) with only nonnegative powers of \(\tau\), and multiplying by a further power \(\tau^M\) makes it hold in \(S\):

\[
\tau^{m+N+M}+\sum_{i<m}\sum_{j=0}^{N}\varphi(b_{ij})\,\tau^{\,i+N+M-j}=0 .
\]

All exponents in the sum are smaller than \(m+N+M\), so this is a monic equation for \(\tau\) over \(R\). If \(\tau\) is nilpotent, then \(S_\tau=0\) and \(\tau\) is integral over \(R\) anyway. \(\square\)

### Z.3. Clearing a leading coefficient

**Lemma Z.3.** Suppose again that \(\varphi:R[X]\to S\) is a ring map and \(t\in S\) is integral over \(R[X]\), and let

\[
p=\sum_{i=0}^ka_iX^i\in R[X]
\]

with \(t\varphi(p)\in\operatorname{im}\varphi\). For some \(n\ge0\) and \(q\in R[X]\), the element \(\varphi(a_k)^nt-\varphi(q)\) is integral over \(R\).

**Proof.** Put \(a=a_k\). If \(a\) is nilpotent, \(a^n=0\) for some \(n\) and \(q=0\) works. Otherwise invert \(a\) in \(R\) and \(\varphi(a)\) in \(S\). Over \(R_a\) the polynomial \(a^{-1}p\) is monic, and the images of \(t\) and of \(t\varphi(a^{-1}p)\) satisfy the hypotheses of Lemma Z.2 for \(R_a[X]\to S_{\varphi(a)}\). That lemma gives \(q'\in R_a[X]\) with \(t-\varphi(q')\) integral over \(R_a\). Write \(a^eq'=q_0\) with \(q_0\in R[X]\). The image of \(\delta=\varphi(a)^et-\varphi(q_0)\) in \(S_{\varphi(a)}\) is \(\varphi(a)^e\) times an integral element, so it is integral over \(R_a\). By Lemma Z.1 for \(R\to S\) and the powers of \(a\), it equals \(c/\varphi(a)^j\) for some \(c\in S\) integral over \(R\). Equality of fractions gives \(\ell\ge0\) with \(\varphi(a)^{\ell}(\varphi(a)^j\delta-c)=0\) in \(S\). Then \(\varphi(a)^{j+\ell}\delta=\varphi(a)^\ell c\) is integral over \(R\), which is the assertion with \(n=e+j+\ell\) and \(q=a^{j+\ell}q_0\). \(\square\)

### Z.4. The conductor setup

**Situation Z.4.** Let \(\varphi:R[X]\to S\) be a finite ring map. Put \(A=\varphi(R)\), \(x=\varphi(X)\) and \(C=A[x]=\varphi(R[X])\). Assume that \(A\) is integrally closed in \(S\), that is, every element of \(S\) integral over \(A\) lies in \(A\); \(A\) need not be a domain. The **conductor** of \(C\subset S\) is

\[
J=\{g\in S:\ gS\subset C\}.
\]

It is an ideal of \(S\) and is contained in \(C\), since \(g=g\cdot1\). Fix \(C\)-module generators \(t_1,\ldots,t_r\) of \(S\). Then \(g\in J\) if and only if \(gt_i\in C\) for every \(i\), because every element of \(gS\) is a \(C\)-combination of the \(gt_i\). Nothing here excludes \(S=0\).

### Z.5. The leading coefficient enters the conductor

**Lemma Z.5.** Assume Situation Z.4, and take \(u\in S\) and \(p=\sum_{i=0}^ka_iX^i\in R[X]\). If \(u\varphi(p)\in J\), then \(u\varphi(a_k)^m\in J\) for some \(m\ge0\).

**Proof.** Each product \(ut_i\) is integral over \(R[X]\): \(S\) is a finite \(R[X]\)-algebra, and finite algebras are integral by the determinant test. Also \((ut_i)\varphi(p)=(u\varphi(p))t_i\in C=\operatorname{im}\varphi\). Lemma Z.3 gives \(n_i\ge0\) and \(q_i\in R[X]\) with \(\varphi(a_k)^{n_i}ut_i-\varphi(q_i)\) integral over \(R\), that is, over \(A\). By the hypothesis on \(A\) this element lies in \(A\subset C\), so \(\varphi(a_k)^{n_i}ut_i\in C\). For \(m=\max_in_i\), multiplying by further powers of \(\varphi(a_k)\in C\) gives \(u\varphi(a_k)^mt_i\in C\) for all \(i\), so \(u\varphi(a_k)^m\in J\). \(\square\)

### Z.6. Every coefficient enters the radical

**Lemma Z.6.** Assume Situation Z.4, with \(u\in S\) and \(p=\sum_{i=0}^ka_iX^i\in R[X]\). If \(u\varphi(p)\in\sqrt J\), then \(u\varphi(a_i)\in\sqrt J\) for every \(i\).

**Proof.** We induct on \(k\). Choose \(N\ge1\) with \(u^N\varphi(p)^N\in J\). The polynomial \(p^N\), written with top index \(kN\), has coefficient \(a_k^N\) there, so Lemma Z.5 gives \(m\ge1\) with \(u^N\varphi(a_k)^{Nm}\in J\); enlarging \(m\) keeps this true, as \(J\) is an ideal. It follows that \((u\varphi(a_k))^{Nm}=u^{N(m-1)}\cdot u^N\varphi(a_k)^{Nm}\in J\), so \(u\varphi(a_k)\in\sqrt J\). Hence \(u\varphi(p-a_kX^k)=u\varphi(p)-u\varphi(a_k)x^k\in\sqrt J\), and the induction hypothesis applies to \(p-a_kX^k\), whose top index is \(k-1\). For \(k=0\) the first step is the whole proof. \(\square\)

### Z.7. Strong transcendence and the conductor quotient

**Definition Z.7.** Let \(R\subset S\) be rings. An element \(x\in S\) is **strongly transcendental over \(R\)** if, whenever \(u\in S\) and \(a_0,\ldots,a_k\in R\) satisfy \(u\sum_ia_ix^i=0\), every product \(ua_i\) is zero. For domains \(R\subset S\) this is ordinary transcendence: \(u=1\) gives transcendence, and in a domain a nonzero \(u\) can be cancelled.

In Situation Z.4, let

\[
S_0=S/\sqrt J,\qquad A_0=A/(A\cap\sqrt J),
\]

with \(x_0\) the class of \(x\) in \(S_0\). Then \(A_0\subset S_0\) are reduced rings, \(S_0\) is a finite \(A_0[x_0]\)-module, and over \(A_0\) the element \(x_0\) is strongly transcendental.

**Proof.** The map \(A_0\to S_0\) is injective by construction. The ideal \(\sqrt J\) is radical, so \(S_0\) and its subring \(A_0\) are reduced. The images of \(t_1,\ldots,t_r\) generate \(S_0\) over \(A_0[x_0]\). Now let \(u_0\sum_i\bar a_ix_0^i=0\) in \(S_0\), with \(u_0\in S_0\) and \(\bar a_i\in A_0\). Choose \(u\in S\) lifting \(u_0\) and \(r_i\in R\) with \(\varphi(r_i)\) lifting \(\bar a_i\). Then \(u\varphi(\sum_ir_iX^i)\in\sqrt J\), and Lemma Z.6 gives \(u\varphi(r_i)\in\sqrt J\) for every \(i\), that is, \(u_0\bar a_i=0\). \(\square\)

### Z.8. Quasi-finiteness in a four-ring diagram

**Lemma Z.8.** Let

\[
\begin{array}{ccc}
R&\longrightarrow&S\\
\downarrow&&\downarrow\\
R'&\longrightarrow&S'
\end{array}
\]

be a commutative square of rings in which \(R\to S\) is of finite type and \(S\otimes_RR'\to S'\) is surjective. Let \(\mathfrak q'\subset S'\) be a prime, with contractions \(\mathfrak q\subset S\), \(\mathfrak p'\subset R'\) and \(\mathfrak p\subset R\). Quasi-finiteness of \(R\to S\) at \(\mathfrak q\) implies quasi-finiteness of \(R'\to S'\) at \(\mathfrak q'\).

**Proof.** Since \(S\otimes_RR'\) is of finite type over \(R'\) and maps onto \(S'\), the map \(R'\to S'\) is of finite type. Let \(k=\kappa(\mathfrak p)\), \(k'=\kappa(\mathfrak p')\), and let \(F=S\otimes_Rk\) and \(F'=S'\otimes_{R'}k'\) be the two fibre rings. By the pointwise criterion, the point \(\mathfrak q\) of \(\operatorname{Spec}F\) is closed as well as isolated. So \(\{\mathfrak q\}\) is open and closed, and \(F=F_1\times F_2\) with \(\operatorname{Spec}F_1=\{\mathfrak q\}\). The ring \(F_1\) has a single prime ideal, so it equals its localization there, which is the local fibre algebra at \(\mathfrak q\). The pointwise criterion makes it finite over \(k\).

Tensoring the surjection \(S\otimes_RR'\to S'\) with \(k'\) over \(R'\) gives a surjection \(F\otimes_kk'\to F'\). The image of the idempotent of \(F_1\) splits \(F'=F_1'\times F_2'\), where \(F_1'\) is a quotient of \(F_1\otimes_kk'\) and hence finite over \(k'\). The map \(F\to F'\to\kappa(\mathfrak q')\) factors through \(\kappa(\mathfrak q)\), because \(\mathfrak q'\) contracts to \(\mathfrak q\). So it sends the idempotent of \(F_1\) to \(1\), and \(\mathfrak q'\) lies in \(\operatorname{Spec}F_1'\). A finite algebra over a field is Artinian, since its ideals are subspaces, so it has finitely many primes, all maximal, and its spectrum is discrete. Thus \(\mathfrak q'\) is isolated in the open and closed subset \(\operatorname{Spec}F_1'\) of \(\operatorname{Spec}F'\), and so in its fibre. \(\square\)

### Z.9. Passage to a minimal prime

**Lemma Z.9.** Suppose \(R\subset S\) are reduced and \(x\in S\) is strongly transcendental over \(R\). For a minimal prime \(\mathfrak q\) of \(S\) with \(\mathfrak p=R\cap\mathfrak q\), the class of \(x\) in \(S/\mathfrak q\) is strongly transcendental over \(R/\mathfrak p\).

**Proof.** First, \(\mathfrak qS_{\mathfrak q}=0\). The ring \(S_{\mathfrak q}\) is reduced: if \((y/s)^n=0\), then \(wy^n=0\) for some \(w\notin\mathfrak q\), so \((wy)^n=0\), \(wy=0\) by reducedness of \(S\), and \(y/s=0\). Its primes correspond to the primes of \(S\) inside \(\mathfrak q\), and by minimality only \(\mathfrak qS_{\mathfrak q}\) remains. The nilradical is the intersection of all primes, so \(\mathfrak qS_{\mathfrak q}\) is the nilradical, which is zero.

Let \(u\in S\) and \(a_i\in R\) with \(u\sum_ia_ix^i\in\mathfrak q\). This element vanishes in \(S_{\mathfrak q}\), so \(wu\sum_ia_ix^i=0\) for some \(w\notin\mathfrak q\). Strong transcendence gives \(wua_i=0\), and since \(w\notin\mathfrak q\), each \(ua_i\) lies in \(\mathfrak q\). This is the required property for the images in \(S/\mathfrak q\), and \(R/\mathfrak p\to S/\mathfrak q\) is injective by the choice of \(\mathfrak p\). \(\square\)

### Z.10. Transcendence excludes quasi-finite points for domains

**Lemma Z.10.** Let \(x\in S\) be transcendental over \(R\), where \(R\subset S\) are domains and \(S\) is a finite \(R[x]\)-module. Then \(R\to S\) has no quasi-finite point.

**Proof.** Generators of \(S\) as an \(R[x]\)-module, together with \(x\), generate \(S\) as an \(R\)-algebra, so \(R\to S\) is of finite type.

*Case 1: \(R\) is normal.* Then \(R[x]\cong R[X]\) is a normal domain by Lemma 0.1. Let \(\mathfrak q\subset S\) be a prime, with \(\mathfrak p=R\cap\mathfrak q\) and \(\mathfrak r=R[x]\cap\mathfrak q\), and suppose \(R\to S\) is quasi-finite at \(\mathfrak q\). Then \(\kappa(\mathfrak q)\) is finite over \(\kappa(\mathfrak p)\), and so is the intermediate field \(\kappa(\mathfrak r)\). The prime \(\mathfrak pR[x]\) has residue field \(\kappa(\mathfrak p)(X)\), which is not finite over \(\kappa(\mathfrak p)\); hence \(\mathfrak pR[x]\subsetneq\mathfrak r\). The extension \(R[x]\subset S\) is integral, \(S\) is a domain and \(R[x]\) is normal, so going down gives a prime \(\mathfrak q_0\subset\mathfrak q\) with \(R[x]\cap\mathfrak q_0=\mathfrak pR[x]\). Then \(\mathfrak q_0\ne\mathfrak q\), while \(R\cap\mathfrak q_0=\mathfrak p\). So \(\mathfrak q_0\) lies in the fibre over \(\mathfrak p\) and specializes to \(\mathfrak q\). Every open set containing \(\mathfrak q\) contains its generization \(\mathfrak q_0\), so \(\mathfrak q\) is not isolated in the fibre, a contradiction.

*Case 2: general \(R\).* Let \(K\) and \(L\) be the fraction fields of \(R\) and \(S\), let \(R'\subset K\) be the integral closure of \(R\), and let \(S'\) be the subring of \(L\) generated by \(S\) together with \(R'\). The domain \(R'\) is normal with fraction field \(K\): if an element of \(K\) satisfies a monic equation over \(R'\), transitivity makes it integral over \(R\), so it lies in \(R'\). The element \(x\) is transcendental over \(R'\), since clearing denominators turns a relation over \(R'\) into one over \(R\). The map \(S\otimes_RR'\to S'\) is surjective, and the images of \(R[x]\)-module generators of \(S\) generate \(S'\) over \(R'[x]\). So \(R'\subset S'\) satisfy the hypotheses of Case 1. The ring \(S'\) is generated over \(S\) by elements of \(R'\), which are integral over \(R\subset S\), so \(S\subset S'\) is integral. By lying over, a given prime \(\mathfrak q\subset S\) is the contraction of some prime \(\mathfrak q'\subset S'\). If \(R\to S\) were quasi-finite at \(\mathfrak q\), Lemma Z.8 for the square \(R,S,R',S'\) would make \(R'\to S'\) quasi-finite at \(\mathfrak q'\), contradicting Case 1. Neither finiteness of \(R'\) over \(R\) nor Noetherianity is used. \(\square\)

### Z.11. Strong transcendence excludes quasi-finite points

**Lemma Z.11.** Let \(R\subset S\) be reduced, with \(x\in S\) strongly transcendental over \(R\) and \(S\) a finite \(R[x]\)-module. Then \(R\to S\) has no quasi-finite point.

**Proof.** As before, \(R\to S\) is of finite type. Let \(\mathfrak q\subset S\) be a prime. It contains a minimal prime \(\mathfrak q_0\) of \(S\), by Zorn’s lemma for the primes inside \(\mathfrak q\) ordered by reverse inclusion. The hypothesis of Zorn’s lemma holds because the intersection of a chain of primes is prime: if \(ab\) lies in it while \(a\) and \(b\) do not, choose members of the chain missing \(a\) and missing \(b\). The smaller of the two misses both, yet contains \(ab\).

Let \(\mathfrak p_0=R\cap\mathfrak q_0\), \(R_0=R/\mathfrak p_0\) and \(S_0=S/\mathfrak q_0\). These are domains with \(R_0\subset S_0\). By Lemma Z.9 the image \(x_0\) of \(x\) is strongly transcendental over \(R_0\), hence transcendental. The ring \(S_0\) is finite over \(R_0[x_0]\). By Lemma Z.10, \(R_0\to S_0\) is not quasi-finite at \(\mathfrak q/\mathfrak q_0\). Lemma Z.8 applies to the square \(R,S,R_0,S_0\), since \(S\otimes_RR_0=S/\mathfrak p_0S\) maps onto \(S/\mathfrak q_0\). So \(R\to S\) is not quasi-finite at \(\mathfrak q\). There may be infinitely many minimal primes; the argument uses only one. \(\square\)

### Z.12. The conductor is avoided at a quasi-finite point

**Corollary Z.12.** Assume Situation Z.4. If \(\mathfrak q\) is a prime of \(S\) at which \(A\to S\) is quasi-finite, the conductor \(J\) is not contained in \(\mathfrak q\).

**Proof.** Suppose \(J\subset\mathfrak q\), so \(\sqrt J\subset\mathfrak q\). Z.7 and Lemma Z.11, applied to \(A_0\subset S_0\), which are reduced, and to \(x_0\), which is strongly transcendental over \(A_0\), show that \(A_0\to S_0\) is not quasi-finite at \(\mathfrak q/\sqrt J\). But \(A\to S\) is of finite type, \(S\) being finite over \(A[x]\), and Lemma Z.8 applies to the square \(A,S,A_0,S_0\), since \(S\otimes_AA_0=S/(A\cap\sqrt J)S\) maps onto \(S/\sqrt J\). That lemma carries quasi-finiteness of \(A\to S\) at \(\mathfrak q\) to quasi-finiteness of \(A_0\to S_0\) at \(\mathfrak q/\sqrt J\), a contradiction. \(\square\)

For Lemma 2.1 of Zariski’s Main Theorem, Corollary Z.12 provides the conductor element outside the given prime. The two supporting facts behind it are Lemma Z.6, on coefficients, and Lemma Z.11, on reduced rings with a strongly transcendental element. The monogenic argument and the main induction are in that lesson.

The statements of this appendix correspond to the Stacks Project, *Algebra*, Tags 0307, 00PT, 00PV, 00PW, 00PX, 00PY, 00PZ (strong transcendence), 00Q0, 00Q1, 00Q2 and 00PN, in the AI Integrated Stacks Project edition pinned at [revision 565b10e9](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex).
