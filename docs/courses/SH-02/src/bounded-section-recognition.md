# Bounded section recognition from injective mapping complexes

This proof concerns ordinary infinity-sheaves on the open-set site of an
arbitrary topological space \(X\), with coefficients
\(D_\infty(k)\), for any commutative unital ring \(k\). Every module sheaf
is allowed. There is no dimension, countability, constructibility,
finite-global-dimension or perfection hypothesis.

The categorical floor is the ordinary module-sheaf infinity-category and its
standard t-structure: in cohomological notation its \(\geq a\) part consists
of objects whose section complexes on **every** open have lower bound \(a\),
and its \(\leq b\) part is characterized by vanishing cohomology sheaves
above \(b\). Its heart is the ordinary category of \(k\)-module sheaves.
These precise properties and existence of the t-structure are the
specialization of DAG VIII, Proposition 2.1.3 and Remark 2.1.5. Ordinary
spectral sheafification, the differential graded nerve and coefficient
spectra are also part of this categorical floor. The proof does not assume
a general derived-heart realization theorem or left completeness of the
entire ordinary sheaf category.

The classical floor consists of bounded-below injective resolutions, their
mapping complexes, enough injectives, and exact coproducts and filtered
colimits of module sheaves. The required sequential derived colimit is
constructed below by a mapping telescope, rather than assumed from a
general unbounded derived-category existence theorem.

*Written by GPT-6.1 Sol (OpenAI). Self-checked by the writing AI. CC0 1.0.*

The injective mapping complexes give full faithfulness, and a mapping telescope realizes every sheaf with the stated lower section bound.

## SH02-BSR-1 — The actual functor {#SH02-BSR-1}

Choose a bounded-below injective resolution \(K\to I\) and set

\[
T_XK(U)=\Gamma(U;I).
\tag{BSR.1}
\]

The [injective spectral Čech calculation](../modern-proper-support-construction.html#SH02-SXM-8) proves descent for
this coefficient complex. It also proves that an injective sheaf \(J\),
viewed as a heart object, has section values \(J(U)[0]\). The differential
graded section functors respect composition, differentials and mapping
complexes, so (BSR.1) is an enhanced functor rather than a selection of
objects and cohomology groups. Bounded-below injective complexes model the
classical derived infinity-category; replacing a resolution by a
chain-homotopy equivalent one gives the same functor.

Cones, shifts and zero objects are computed in this model, so \(T_X\) is
exact. Its stalk is the original stalk complex, since filtered colimits of
modules are exact. It is t-exact for the stated t-structures: a classical
lower bound has an injective resolution with that same lower term bound,
whereas a classical upper cohomology-sheaf bound is detected on its stalks.
In particular it identifies the ordinary hearts.

## SH02-BSR-2 — A bounded stalk comparison without recognition {#SH02-BSR-2}

**Lemma.** If \(E\) is an ordinary module-valued infinity-sheaf with a
single lower section bound \(a\), and all its stalk complexes are zero,
then \(E=0\).

**Proof.** Shift to \(a=0\). The presheaf
\(U\mapsto H^0(E(U))\) is already an ordinary sheaf. To see this, use
covering descent for \(E\). Its Čech totalization has section degree and
Čech degree both nonnegative; total degree zero is exactly the equalizer
of the degree-zero groups in Čech degrees zero and one. Products commute
with degree-zero cohomology for bounded-below complexes of modules. Thus
the ordinary sheaf gluing equation holds. The same argument is valid for
any open cover, not just a finite one.

Its stalk is \(H^0(E_x)\), because filtered coefficient colimits are
exact. Hence it is the zero ordinary sheaf, and \(H^0(E(U))=0\) on every
open. The section lower bound has improved to one. Shift by one and repeat.
After the \(n\)-th repetition all section cohomology through degree
\(n-1\) is zero. There were no negative groups to begin with, so every
section complex is zero. This is an objectwise equivalence to the zero
sheaf. \(\square\)

Consequently a stalk equivalence between two objects with a common lower
section bound is an equivalence: its fibre retains that lower bound, has
zero stalks, and the lemma applies. This lemma supplies the bounded
separation needed below without invoking bounded recognition circularly.

## SH02-BSR-3 — Spectral Ext into a heart injective {#SH02-BSR-3}

Let \(J\) be an injective ordinary module sheaf, regarded as a heart
object of the infinity-sheaf category. For every ordinary module sheaf
\(M\),

\[
\operatorname{Hom}(M,J[q])=
\begin{cases}
\operatorname{Hom}_{k_X}(M,J),&q=0,\\
0,&q\ne0.
\end{cases}
\tag{BSR.2}
\]

Negative degrees vanish by the t-structure, and degree zero is the heart
identification. Here is a proof for all positive degrees, including the
local-to-global step.

For an open \(U\), the free local module \(k_U\), extended by zero,
represents sections in the spectral module-sheaf category. This follows
directly by sheafifying the free coefficient presheaf on the open
representable. It is a heart object: its stalk is \(k\) in \(U\) and
zero outside, and spectral sheafification retains its section lower bound
zero. Mapping it to \(J[q]\) gives \(H^q(J(U)[0])\), hence zero for
\(q>0\).

There is an epimorphism

\[
P=\bigoplus_{(U,s),\ s\in M(U)}k_U\longrightarrow M.
\tag{BSR.3}
\]

It is stalkwise surjective: every stalk element has a section
representative. The coproduct is the coproduct of these heart objects,
also in the spectral category. For clarity, its section lower bound zero
is preserved by the coproduct and sheafification; its stalks are the
direct sums of the degree-zero stalks and have no other cohomology. It is
therefore the same ordinary heart coproduct. Maps out of that coproduct
are products of the maps from its summands. Thus
\(\operatorname{Hom}(P,J[q])=0\) for every \(q>0\).

Let \(N\) be the kernel in (BSR.3). The short exact heart sequence gives
the fibre sequence \(N\to P\to M\). For \(q=1\), its long exact
mapping sequence identifies \(\operatorname{Hom}(M,J[1])\) with the
cokernel of \(\operatorname{Hom}(P,J)\to\operatorname{Hom}(N,J)\),
which is zero by ordinary injectivity of \(J\). For \(q\geq2\), it
identifies \(\operatorname{Hom}(M,J[q])\) with
\(\operatorname{Hom}(N,J[q-1])\). Induction on \(q\), applied to all
ordinary sheaves at once, proves (BSR.2).

## SH02-BSR-POSTNIKOV — The bounded sheaf colimit {#SH02-BSR-POSTNIKOV}

If an ordinary infinity-sheaf \(E\) has one actual section lower bound \(a\), its finite cohomological truncations \(E_n=\tau_{\leq n}E\), \(n\geq a\), retain that bound. Their colimit \(E'=\operatorname{colim}_n E_n\) in the ordinary infinity-sheaf category retains it too. Indeed this is the sheafification of the pointwise filtered colimit; the filtered-colimit and sheafification stability of this t-structure part is the stated categorical floor, DAG VIII, Proposition 2.1.3(7), with grading reversed. One may also use the plus construction: its covering limits, filtered colimits and transfinite iterations preserve the same lower section bound.

The canonical map \(E'\to E\) is a stalk equivalence: stalks preserve sheaf colimits, coefficient filtered colimits are exact, and every fixed stalk cohomology group has stabilized in the finite truncations. BSR-2 therefore makes this actual map an equivalence. This proves bounded Postnikov-colimit convergence before full faithfulness or recognition is used. It makes no assertion that derived sections on an arbitrary open commute with a filtered colimit.

For \(E=T_XK\), exactness and t-exactness in BSR-1 give the canonical comparisons \(E_n=T_X(\tau_{\leq n}K)\), including their truncation maps. Thus the preceding sheaf-category colimit calculation applies to precisely these classical finite truncations.

## SH02-BSR-4 — Full faithfulness on mapping spectra {#SH02-BSR-4}

First take a target consisting of one injective \(J\) in degree zero.
For any \(K\in D^+(k_X)\) the natural comparison gives

\[
\begin{gathered}
\operatorname{Hom}(T_XK,J[q])\\
\simeq\operatorname{Hom}_{k_X}(H^{-q}K,J)\\
\simeq H^q\operatorname{Hom}^{\bullet}(K,J).
\end{gathered}
\tag{BSR.4}
\]

First take \(K_n=\tau_{\leq n}K\), which has a finite cohomological filtration. BSR-3 applies to every heart quotient and gives

\[
 \operatorname{Hom}(T_XK_n,J[q])
 =\operatorname{Hom}_{k_X}(H^{-q}K_n,J).
 \tag{BSR.4a}
\]

The filtration's long exact mapping sequences, or its finite spectral sequence with only the injective row, give this equality with the actual comparison induced by \(T_X\). It agrees on the heart, and its finite extension calculation is natural in the truncation maps.

We now justify passage to the possibly unbounded-above source. BSR-POSTNIKOV proves \(T_XK=\operatorname{colim}_n T_XK_n\) in the sheaf category, without recognition. Mapping that colimit into \(J\) gives the inverse limit of the spectra \(M_n=\operatorname{Map}(T_XK_n,J)\). For every integer \(t\), the finite calculation gives

\[
 \pi_t M_n=\operatorname{Hom}_{k_X}(H^tK_n,J).
 \tag{BSR.4b}
\]

This group tower and its maps are eventually constant, with value \(\operatorname{Hom}_{k_X}(H^tK,J)\). The homotopy inverse limit is the fibre of \(1-\mathrm{shift}\) on the product of the spectra \(M_n\). On each homotopy-group tower the same map is surjective: in the isomorphism tail choose one starting coordinate and solve recursively forwards by the inverse transition maps, then solve backwards through the finite initial segment. Every coordinate uses only finitely many operations. The resulting long exact homotopy sequence has zero cokernel term from the next homotopy-group tower, and hence

\[
\begin{gathered}
\pi_t\operatorname{Map}(T_XK,J)=\lim_n\pi_t M_n\\
=\operatorname{Hom}_{k_X}(H^tK,J).
\end{gathered}
\tag{BSR.4c}
\]

The compatible finite comparisons induce this identification, so it is the original natural comparison on every homotopy group. This is a limit calculation for mapping spectra, with no exactness of products or inverse limits of arbitrary sheaves. It supplies the first equality of (BSR.4) for the full source range. No orthogonality from a high-degree source to a low-degree target is presumed.

The second equality is the ordinary exactness of
\(\operatorname{Hom}_{k_X}(-,J)\). Running this calculation for every
shift \(q\), including after shifting the source, proves equivalence of
the whole mapping spectra into \(J\). Their homotopy groups are these
shifted morphism groups; a map of spectra inducing all these isomorphisms
is an equivalence.

Now let \(L\) have a bounded-below injective resolution \(I\), with
\(I^m=0\) for \(m<b\). Its finite *term* truncations
\(I_{\leq n}\) retain terms through \(n\) and set the higher terms
to zero. Their projection maps form an inverse tower. Each finite
truncation is made from shifted injectives by finitely many cones, so
exactness and the preceding mapping-spectrum calculation show that

\[
\begin{gathered}
\operatorname{Map}_{D^+_\infty(k_X)}(K,I_{\leq n})\\
\xrightarrow{\sim}\operatorname{Map}_{\operatorname{Shv}(X;D_\infty(k))}(T_XK,T_XI_{\leq n}).
\end{gathered}
\tag{BSR.5}
\]

The limit of the right-hand target tower is \(T_XI\), objectwise on
every open. In each complex degree the term truncations are eventually
constant. More explicitly the homotopy inverse limit is the fibre of
\(1-\mathrm{shift}\) on the product of the tower. That map is degreewise
surjective, and its kernel is the original section complex, giving the
claimed limit.

The same limit calculation holds for the classical mapping complexes.
For a bounded-below representative of \(K\), a fixed degree in
\(\operatorname{Hom}^\bullet(K,I_{\leq n})\) is a finite product of
module Hom groups. Projection drops the new components, and the inverse
limit is the full product defining \(\operatorname{Hom}^\bullet(K,I)\).
The projection tower is degreewise surjective, so the fibre-of-
\(1-\mathrm{shift}\) calculation again proves that this is the homotopy
limit. This is a calculation on mapping complexes of abelian groups;
no exactness of products or inverse limits of arbitrary module sheaves
has been assumed.

Mapping out of a fixed object commutes with limits. Taking the limit in
(BSR.5) proves full faithfulness of \(T_X\) on its actual enhanced
mapping spectra.

## SH02-BSR-5 — Essential image with one uniform section bound {#SH02-BSR-5}

Every object in the image has a lower section bound from (BSR.1). Conversely
let \(E\) be an ordinary infinity-sheaf with section lower bound \(a\).
Use the standard sheaf t-structure to form its finite cohomological
truncations \(E_n=\tau_{\leq n}E\), for \(n\geq a\). They retain
the actual section lower bound \(a\), and have cohomology sheaves only
in \([a,n]\).

Each \(E_n\) lies in the image of \(T_X\). For a single heart quotient
this is (BSR.1) applied to the corresponding ordinary sheaf. Induct on
the number of nonzero cohomological degrees. The finite truncation
triangle attaches the last shifted heart object by a connecting map.
Full faithfulness from BSR-4 lifts that connecting map to the enhanced
classical category; taking its fibre realizes the required extension.
This proves the finite step with its maps.

Full faithfulness also lifts the entire diagram of maps
\(E_n\to E_{n+1}\): a fully faithful infinity-functor identifies the
full diagram categories whose vertices are in its image. Thus there is a
coherent diagram \(K_n\) with \(T_XK_n\simeq E_n\), and all its
objects have the same classical lower bound \(a\). Its successive arrows
can be represented by chain maps between injective resolution models
starting in degree \(a\). The index category is the free category on this
successive chain; compositions give a strict diagram with those arrows,
equivalent to the coherent sequential diagram in the differential graded
nerve. Define its mapping telescope

\[
\begin{gathered}
K=\operatorname{cofib}\bigl(\\
1-\mathrm{shift}:\bigoplus_n K_n\longrightarrow\bigoplus_n K_n\\
\bigr).
\end{gathered}
\tag{BSR.6a}
\]

The coproduct is the termwise coproduct of the common-bounded complexes.
It has the enhanced coproduct universal property: mapping into a
bounded-below injective target is the product of the individual mapping
complexes. Applying that calculation to the cone in (BSR.6a) gives the
homotopy limit of the corresponding inverse mapping diagram, which is
exactly the sequential colimit universal property. The map
\(1-\mathrm{shift}\) is degreewise monic. This can be checked on stalks:
an element of the direct sum has finite support, and its first component
must vanish in the kernel, then its next, and so on. Its cokernel is the
termwise filtered colimit of the complexes. Thus the telescope is
quasi-isomorphic to that termwise colimit. Exactness of filtered
module-sheaf colimits now gives

\[
\begin{gathered}
H^q(K)=\operatorname*{colim}_n H^q(K_n),\\
K\in D^{\geq a}(k_X).
\end{gathered}
\tag{BSR.6}
\]

BSR-POSTNIKOV identifies the actual ordinary sheaf-category colimit \(E'=\operatorname{colim}_n E_n\) with \(E\), retaining the common section lower bound. This is precisely the colimit and canonical comparison proved there; it is independent of whether \(T_X\) preserves any unrestricted sectionwise filtered colimit.

The maps \(K_n\to K\) give a compatible cone
\(E_n=T_XK_n\to T_XK\). The universal property of the **sheaf-category**
colimit supplies

\[
E\simeq E'\longrightarrow T_XK.
\tag{BSR.7}
\]

Its stalk map is an equivalence by (BSR.6) and the stabilized cohomology
of the truncations. The target again has lower section bound \(a\).
BSR-2 makes (BSR.7) an equivalence. This proves the claimed essential
image, with no unrestricted section-colimit interchange and no
completeness assertion for arbitrary unbounded ordinary sheaves.

## SH02-BSR-6 — What this proof establishes {#SH02-BSR-6}

At the stated coefficient, sheaf-t-structure and classical resolution floors,
the actual section functor (BSR.1) is fully faithful and its image is the
union of the uniformly bounded-below section subcategories. This is the
topological constant-ring specialization of DAG VIII, Proposition 2.1.8.
The general 1-localic spectrally ringed infinity-topos theorem has wider
parameters and is not claimed here.

This proof replaces the general derived-heart *recognition criterion* for
the actual topological all-module bridge. It does not prove the coefficient
Morita equivalence with \(Hk\)-module spectra, the existence of the usual
module-sheaf t-structure, or the entire differential graded nerve and
sheafification theories. Their exact categorical roles remain the stated
floor. Modern arbitrary-coefficient proper base change and the
external-product theorem are also separate results.

## SH02-BSR-SOURCES — Exact references {#SH02-BSR-SOURCES}

The comparison with the classical bounded category is due to Jacob Lurie,
[*Derived Algebraic Geometry VIII*](https://www.math.ias.edu/~lurie/papers/DAG-VIII.pdf),
November 5, 2011, Proposition 2.1.8 and Lemmas 2.1.9–2.1.10,
pages 32–35. Proposition 2.1.3 and Remark 2.1.5, pages 31–32,
supply the precise ambient module-sheaf t-structure and heart.
The general derived-heart criterion has its 2017 treatment in Lurie's
[*Higher Algebra*](https://www.math.ias.edu/~lurie/papers/HA.pdf),
September 18, 2017, Proposition 1.3.3.7, pages 99–101.
The direct proof above gives its bounded topological specialization using
injective mapping complexes; it does not reproduce that source's general
realization construction or its exposition.
