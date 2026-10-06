# Every bounded functional becomes normal in one representation

The exact theorem and prerequisites follow. OA-MOD-UB-02–09 build the canonical structure, normal extension, central kernel and functorial maps. The current prerequisite binding, normal-inverse details and supported-representation example are by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0. Earlier course authorship is retained.

Let \(A\) be any complex C*-algebra, including a nonunital or zero algebra.
Write \(j_A:A\to A^{**}\) for the Banach evaluation embedding,
\(j_A(a)(f)=f(a)\), \(f\in A^*\). There is a canonical C*-algebra structure
on this Banach bidual making it a von Neumann algebra with predual \(A^*\).
The embedding is an isometric *-homomorphism with ultraweakly dense image.
For every \(\omega\in A^*_+\), its canonical normal extension is

\[
 \widehat\omega(X)=X(\omega),\qquad X\in A^{**}.
 \tag{UB.1}
\]

It is positive and has the same norm. Both multiplication with one variable
fixed and the involution are continuous for \(\sigma(A^{**},A^*)\), the
involution being conjugate linear.

Every nondegenerate *-representation \(\pi:A\to B(K)\) extends uniquely to
a normal onto *-homomorphism

\[
 \overline\pi:A^{**}\longrightarrow\pi(A)'',
 \qquad\overline\pi\,j_A=\pi.
 \tag{UB.2}
\]

There is a central projection \(z\in A^{**}\) with

\[
 \ker\overline\pi=A^{**}(1-z),\qquad
 \overline\pi|_{zA^{**}}:zA^{**}\ \xrightarrow{\;\cong\;}\ \pi(A)'',
 \tag{UB.3}
\]

and this isomorphism and its inverse are normal. We also prove the precise
supported version for degenerate representations and functoriality for
arbitrary C*-homomorphisms.

The exact mathematical inputs are as follows.

* The unitization construction and the \(f(0)=0\) functional-calculus
  consequence in Continuous functions and the quotient supply an isometric ideal
  \(A\subset\widetilde A\). Unital continuous functional calculus is the
  written abstract calculus and positive-order theorem, AC1–4. No representation theorem is used to construct
  this unitization.
* Positive complexification and its norm through Passage to a nonunital algebra supplies positive functionals which detect the norm
  of every positive element and a decomposition of each \(f\in A^*\) as
  a complex linear combination of four bounded positive functionals.
  Its inputs are unitization, Hahn--Banach, locally convex separation,
  and Banach--Alaoglu. Jordan uniqueness is not required here.
* An approximate identity indexed by finite sets through Cyclicity, normalization and nondegeneracy supply the nonunital cyclic GNS representation for a
  bounded positive functional, its coefficient vector and exact vector
  norm, and nondegeneracy. The finite GNS construction is The algebra of finite elements through The GNS quotient and its exact domain restricted to a bounded functional. BK01 proves Hilbert completion, bounded extensions, Riesz representation and adjoints, including the completion used for the direct sum below.
* Why self-adjoint weak density gives strong density through Contractive approximation from a nonunital algebra, with the nonunital density proof in The generated algebra and its commutant, supply
  strong* density of the contractive ball of any nondegenerate
  *-subalgebra in its bicommutant. These exact selected proofs do not
  depend on modular theory or on a universal-bidual theorem.
* Its dual is exactly B(H) through Positive functionals, closed cones and norm closure supply the concrete predual, \(M=(M_*)^*\) isometrically,
  bounded-form duality, and normal vector functionals. Corners have exactly their inherited predual supplies the
  inherited predual of a concrete corner, used for the normal inverse in
  OA-MOD-UB-08. OA-MOD-BK-03--OA-MOD-BK-04
  supply fixed multiplication, bounded strong-to-ultraweak convergence
  and increasing projection suprema; OA-MOD-BK-06 gives support projections,
  and OA-MOD-BK-08 gives the unitary test for centrality.
* AB05 proves Banach–Alaoglu for the specified real or complex dual unit ball; AB04 proves the compact-image and Hausdorff-closedness facts used in UB08. AB01 proves the Banach-adjoint identities, norm equality, weak* continuity of second adjoints and the annihilator range of an inclusion. NP1 proves real and complex Hahn–Banach with norm preservation. These statements have full written proofs; none is an unproved external contract.

The spanning statement used here concerns the whole Banach dual, as proved in OA-MOD-ST-02–07; the concrete-predual result OA-MOD-CP-03–07 alone does not provide it.

Mathematical antecedents: Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979: Chapter III, §2, Proposition 2.1, Lemma 2.2, Definition 2.3 and Theorem 2.4, printed pp. 120–123, for positive decomposition, universal extensions and the bidual realization; Chapter II, §4, Theorem 4.8, printed pp. 82–84, for Kaplansky density. The exact edition has been checked. HAP04–05 gives the complete alternative density proof using self-adjoint resolvents and a two-by-two matrix argument. Below we prove multiplicativity of the extension, central-kernel reduction, normality of the inverse, and the supported version for degenerate representations explicitly.

## Elementary facts about homomorphisms

An algebraic *-homomorphism \(\theta:A\to C\) is contractive. Indeed it
extends to a unital algebraic *-homomorphism between forced unitizations
by \((a,\lambda)\mapsto(\theta(a),\lambda)\). Square-root factorization in
the domain shows that this map preserves positivity. Therefore

\[
 0\leq \theta(a)^*\theta(a)\leq\|a\|^2 1
\]

in the target unitization, proving \(\|\theta(a)\|\leq\|a\|\).
This argument does not presume continuity of the homomorphism.

An injective *-homomorphism is isometric. For \(a\geq0\), suppose
\(\|\theta(a)\|<\|a\|\). Choose a continuous real function \(g\) on
\([0,\|a\|]\), zero on \([0,\|\theta(a)\|]\) and at zero, with
\(g(\|a\|)\ne0\). Unital functional calculus and the unitization
\(g(0)=0\) rule give \(g(a)\in A\) and \(g(a)\ne0\).
Polynomial approximation with the constant term removed, and the
contractivity just proved, give
\(\theta(g(a))=g(\theta(a))=0\), a contradiction.
Thus norms agree on positive elements. The C*-identity gives agreement
on every \(a\):

\[
 \|\theta(a)\|^2=\|\theta(a^*a)\|=\|a^*a\|=\|a\|^2.
 \tag{UB.4}
\]

The zero algebra causes no exception. The range of any *-homomorphism
will be used below only as a *-subalgebra, until its closedness is proved.

## The universal representation is indexed by all states

Suppose first \(A\ne0\), and let \(S(A)\) be the set of bounded positive
functionals of norm one. ST's norm detection makes this set nonempty.
For every \(\omega\in S(A)\), BG supplies
\((H_\omega,\pi_\omega,\xi_\omega)\) such that

\[
 \omega(a)=\langle\pi_\omega(a)\xi_\omega,\xi_\omega\rangle,\qquad
 \|\xi_\omega\|=1,\qquad
 \overline{\pi_\omega(A)\xi_\omega}=H_\omega.
 \tag{UB.5}
\]

Inner products are linear in their first variable. Put

\[
 H_u=\bigoplus_{\omega\in S(A)}H_\omega,\qquad
 \pi_u(a)=\bigoplus_{\omega\in S(A)}\pi_\omega(a),\qquad
 M=\pi_u(A)''\subseteq B(H_u).
 \tag{UB.6}
\]

The Hilbert direct sum is the completion of finitely supported vector
families for the sum of squared norms. The uniform estimate
\(\|\pi_\omega(a)\|\leq\|a\|\) defines a bounded operator on it.
Products and adjoints hold first on finite families and then by density,
so \(\pi_u\) is a *-representation.

It is nondegenerate: a vector supported in one summand is approximated
there by vectors of the form \(\pi_\omega(a)\xi_\omega\), which are
\(\pi_u(a)\) applied to the vector \(\xi_\omega\) in that summand.
Finite sums of these vectors are dense in \(H_u\).

For \(a\geq0\), ST and (UB.5) give

\[
 \|a\|=\sup_{\omega\in S(A)}\omega(a)\leq\|\pi_u(a)\|\leq\|a\|.
 \tag{UB.7}
\]

The C*-identity gives \(\|\pi_u(a)\|=\|a\|\) for all \(a\).
Thus \(\pi_u\) is faithful. There is no countable selection of states in
this construction. If \(A=0\), use the empty direct sum \(H_u=0\),
\(\pi_u=0\), and \(M=0\); all the following maps are the unique zero maps.

OA-MOD-HAP-05 now gives, for every \(x\in M\) with \(\|x\|\leq1\), a net
\(a_i\in A\) with

\[
 \|a_i\|\leq1,\qquad \pi_u(a_i)\longrightarrow x
 \quad\hbox{strongly* and ultraweakly}.
 \tag{UB.8}
\]

HAP produces contractions in \(\pi_u(A)\), and its faithful isometry
gives their unique contractive lifts. OA-MOD-BK-03 supplies the ultraweak limit
from the explicitly bounded net. No bound is inferred from convergence
of an arbitrary net.

## The restriction of the concrete predual is an onto isometry

By OA-MOD-CP-06, \(M_*\) is a Banach space with \((M_*)^*=M\) isometrically.
Define the bounded complex-linear restriction map

\[
 R:M_*\longrightarrow A^*,\qquad R(\rho)=\rho\circ\pi_u.
 \tag{UB.9}
\]

It is contractive. For \(x\) in the unit ball of \(M\), take (UB.8).
Ultraweak continuity gives

\[
 |\rho(x)|=\lim_i|\rho(\pi_u(a_i))|\leq\|R\rho\|.
\]

Taking the supremum over that ball proves

\[
 \|R\rho\|=\|\rho\|.
 \tag{UB.10}
\]

In particular \(R\) is injective.

It is onto, for the following reason. If \(\omega\in A^*_+\) is nonzero,
write \(c=\|\omega\|\) and \(\omega_0=\omega/c\in S(A)\). On \(M\) the
vector functional belonging to \(\sqrt c\,\xi_{\omega_0}\), supported
in its one summand of \(H_u\), is positive and normal, and restricts to
\(\omega\). Zero has the zero extension. ST writes an arbitrary
\(f\in A^*\) as a linear combination of four such positive functionals;
the same combination of their normal extensions is an element of
\(M_*\) mapped to \(f\). Uniqueness follows from injectivity.

Consequently

\[
 R^{-1}:A^*\longrightarrow M_*
 \tag{UB.11}
\]

is an onto isometry, and it sends positive functionals to positive
normal functionals. Its restriction is not an arbitrary Hahn--Banach
extension: uniqueness on the whole \(M\) has just been proved.

## Transfer of the algebra structure to the Banach bidual

Take the Banach adjoint of (UB.9), followed by CP's concrete duality:

\[
 U=R^*:A^{**}\longrightarrow (M_*)^*=M.
 \tag{UB.12}
\]

Because \(R\) is an onto isometry, \(U\) is an onto isometry as well:
the adjoint of \(R^{-1}\) is its inverse. It is a homeomorphism for the
respective weak-star topologies, directly from evaluation.
For every \(a\in A\) and \(\rho\in M_*\),

\[
 \rho(Uj_A(a))=j_A(a)(R\rho)=\rho(\pi_u(a)).
\]

Since the predual separates points, \(Uj_A(a)=\pi_u(a)\).
Define

\[
 XY=U^{-1}(U(X)U(Y)),\qquad
 X^*=U^{-1}(U(X)^*),\qquad 1_{A^{**}}=U^{-1}(1_M).
 \tag{UB.13}
\]

The Banach norm already on \(A^{**}\) is unchanged. Transporting the
concrete C*-identities proves all algebra and C*-norm axioms.
The map \(j_A\) is an isometric *-homomorphism. Transporting the
ultraweak topology proves that this is a von Neumann algebra with
the specified predual \(A^*\).
The dense image assertion follows from (UB.8) and the homeomorphism \(U\).

For \(\omega\in A^*_+\), put \(\rho=R^{-1}\omega\in M_*^+\). Equation
(UB.12) reads

\[
 X(\omega)=\rho(U(X)).
\]

This proves positivity, normality and the norm equality in (UB.1).
Its uniqueness among ultraweakly continuous extensions follows from
the density of \(j_A(A)\).

This algebra structure is canonical. Any two separately weak-star
continuous bilinear products extending the product on \(j_A(A)\) agree
first when their second input is in \(j_A(A)\), by approximation of the
first input, and then on both arbitrary inputs by approximation of the
second. The analogous one-limit argument applies to a weak-star
continuous conjugate-linear involution. Thus (UB.13) is independent of
the chosen realizations of the cyclic GNS spaces. This is a uniqueness
argument for the specified algebra structure, not a theorem about
uniqueness of all possible Banach preduals.

## Extension of a representation by its coefficient functionals

Let \(\pi:A\to B(K)\) be any *-representation, initially possibly
degenerate. It is contractive by OA-MOD-UB-02. The concrete predual of \(B(K)\)
from CP defines a bounded map

\[
 S:B(K)_*\longrightarrow A^*,\qquad S(\rho)=\rho\circ\pi.
\]

Its Banach adjoint, under the two established dualities, defines

\[
 T=S^*:A^{**}\longrightarrow B(K).
 \tag{UB.14}
\]

Thus \(T\) is bounded and ultraweakly continuous, and \(Tj_A=\pi\).
Equivalently, all its vector coefficients are specified by

\[
 \langle T(X)\xi,\eta\rangle
   =X\big(a\mapsto\langle\pi(a)\xi,\eta\rangle\big).
 \tag{UB.15}
\]

These bounded coefficient forms are another direct description through
the Hilbert bounded-form theorem.

We verify multiplicativity, rather than infer it from the adjoint
construction. For \(a\in A\) and \(X\in A^{**}\), choose
\(j_A(b_i)\to X\) weak-star. Fixed multiplication in each von Neumann
algebra is ultraweakly continuous, so

\[
 T(Xj_A(a))=\lim_i\pi(b_i a)=T(X)\pi(a).
 \tag{UB.16}
\]

The analogous argument proves \(T(j_A(a)X)=\pi(a)T(X)\).
For arbitrary \(Y\), approximate it by \(j_A(a_i)\) in (UB.16).
Again fixed multiplication is continuous, giving

\[
 T(XY)=T(X)T(Y).
\]

Continuity of the involution and a one-variable approximation give
\(T(X^*)=T(X)^*\). Hence \(T\) is a normal *-homomorphism.
No joint ultraweak continuity of multiplication has been used.

If \(\pi\) is nondegenerate, the projection \(T(1)\) satisfies
\(T(1)\pi(a)=\pi(a)\) and is therefore the identity on the dense span
of \(\pi(A)K\). Thus \(T(1)=I_K\).
The range is contained in \(\pi(A)''\), because every \(T(X)\) is an
ultraweak limit of elements \(\pi(a_i)\), and that bicommutant is
ultraweakly closed. Its surjectivity is proved in OA-MOD-UB-08.

Uniqueness holds before surjectivity: two ultraweakly continuous
extensions agree on the dense subspace \(j_A(A)\).

## An ultraweakly closed two-sided ideal is central

Let \(N\) be a concrete von Neumann algebra and \(I\) an ultraweakly
closed two-sided *-ideal. For \(b\in I_+\), the elements

\[
 b(b+\varepsilon1)^{-1}\in I,\qquad \varepsilon>0,
\]

are bounded by one and increase strongly to the support \(s(b)\) as
\(\varepsilon\) decreases to zero, by OA-MOD-BK-06. Hence \(s(b)\in I\).
For two positive elements, the null space of their sum is the
intersection of their null spaces: evaluate its nonnegative quadratic
form. Therefore
\(s(b+c)=s(b)\vee s(c)\).
The supports of the positive elements of \(I\) form an upward-directed
family of projections. Their supremum \(p\) belongs to \(I\), by bounded
monotone convergence and ultraweak closedness. Include the support of
zero, so this assertion also covers \(I=0\).

For every unitary \(v\in N\), conjugation carries \(I_+\) onto itself
and \(s(vbv^*)=vs(b)v^*\), so \(vpv^*=p\). By OA-MOD-BK-08, \(p\) commutes
with all of \(N\): it is central.
For \(a\in I\), both \(a^*a\) and \(aa^*\) lie in \(I_+\), and their
supports are at most \(p\). Since
\(\|a(1-p)\xi\|^2=\langle a^*a(1-p)\xi,(1-p)\xi\rangle=0\),
one has \(a=ap\); similarly \(a=pa\).
Conversely \(p\in I\) and the ideal property give \(Np\subseteq I\).
Thus

\[
 I=Np.
 \tag{UB.17}
\]

The projection is unique, because it is the identity of that ideal.

Apply this result to \(\ker T\) from OA-MOD-UB-06, after the concrete
identification \(A^{**}\cong M\). Set \(z=1-p\). Then

\[
 T(X)=T(zX),\qquad \ker(T|_{zA^{**}})=0.
 \tag{UB.18}
\]

OA-MOD-UB-02 makes this restriction isometric.

## Surjectivity uses a compact ball and the exact density theorem

Assume again that \(\pi\) is nondegenerate and put \(N=\pi(A)''\).
The central corner \(zA^{**}\) is weak-star closed, since multiplication
by \(z\) is weak-star continuous. Its closed unit ball is compact:
it is the intersection of the compact unit ball of \(A^{**}=(A^*)^*\)
with the closed conditions \(X=zX\). Here Banach--Alaoglu is applied
to that particular dual ball.

Since \(T\) is continuous and isometric on the corner, the set

\[
 D=T\big(\{X\in zA^{**}:\|X\|\leq1\}\big)
 \tag{UB.19}
\]

is ultraweakly compact, hence closed in the Hausdorff space \(N\).
It contains every contraction \(b\in\pi(A)\).
Indeed choose \(a\) with \(\pi(a)=b\). Then
\(T(zj_A(a))=b\), and the isometry in (UB.18) gives
\(\|zj_A(a)\|=\|b\|\leq1\). We did not require a contractive lift in \(A\).

OA-MOD-HAP-05 applied to the nondegenerate *-subalgebra \(\pi(A)\) says that
every contraction in \(N\) is a strong* limit of contractions in
\(\pi(A)\). This bounded net also converges ultraweakly, so its limit
lies in \(D\). Hence \(D\) is exactly the unit ball of \(N\).
Scaling proves \(T(A^{**})=N\) and proves (UB.2)--(UB.3).

For completeness, the inverse is normal by a direct predual argument.
Write \(C=zA^{**}\), with its inherited concrete corner predual from
OA-MOD-CP-11, and let \(V=T|_C:C\to N\).
Ultraweak continuity gives the bounded map

\[
 V_*:N_*\longrightarrow C_*,\qquad V_*\rho=\rho V.
 \tag{UB.19a}
\]

Because \(V\) maps the unit ball onto the unit ball isometrically,
\(\|V_*\rho\|=\|\rho\|\). Its range is therefore norm closed, since
\(N_*\) is complete.
The annihilator of that range in \((C_*)^*=C\) is zero:
if \(\rho(Vc)=0\) for every \(\rho\in N_*\), predual separation
gives \(Vc=0\), and injectivity gives \(c=0\).
If a norm-closed linear subspace of \(C_*\) were proper,
Hahn--Banach, applied to the quotient or to a point outside that subspace,
would supply a nonzero bounded linear functional annihilating it.
Here is the annihilator step explicitly. If \(W\subset C_*\) is a proper norm-closed subspace, choose \(u\notin W\) and set \(d=\operatorname{dist}(u,W)>0\). The functional

\[
 f(w+\lambda u)=\lambda
 \quad(w\in W,\ \lambda\in\mathbb C)
\]

is well-defined and satisfies \(|f(w+\lambda u)|\leq\|w+\lambda u\|/d\): for \(\lambda\ne0\), factor out \(\lambda\) and use the distance to \(W\); the zero case is immediate. NP1 extends this nonzero functional to \(C_*\), contradicting the zero-annihilator assertion. Thus \(V_*\) is onto. Its inverse is an isometry, and the Banach
adjoint of \(V_*^{-1}\), under concrete duality, is \(V^{-1}\).
As an adjoint, that inverse is weak-star continuous. This proves global
normality without an order-normality criterion, weight theory, or an
unjustified norm bound on arbitrary convergent nets.

For a degenerate \(\pi\), let \(q\) project onto
\(K_0=\overline{\operatorname{span}\pi(A)K}\).
This is a reducing subspace, since \(\pi(A)\) is self-adjoint; \(\pi\)
vanishes on \(K_0^\perp\). Indeed, for \(\eta\in K_0^\perp\) and \(\xi\in K\),

\[
 \langle\pi(a)\eta,\xi\rangle
 =\langle\eta,\pi(a^*)\xi\rangle=0,
\]

because \(\pi(a^*)\xi\in K_0\). Hence \(\pi(A)K=\pi(A)K_0\), whose linear span is dense in \(K_0\) by its definition. This proves nondegeneracy of the restricted representation, including \(K_0=0\). Apply the preceding theorem to its
nondegenerate restriction on \(K_0\). Formula (UB.15) then shows that
the full \(T\) is this extension on \(K_0\), direct-summed with zero on
\(K_0^\perp\), and \(T(1)=q\).
Its range is the represented von Neumann algebra on \(K_0\), extended
by zero. It is not in general the full ambient \(\pi(A)''\).
For example, the zero representation on a nonzero Hilbert space
extends to the zero map, whereas the bicommutant of its zero image
contains the ambient identity.

**A nonzero supported example.** Let \(A=\mathbb C\), \(K=\mathbb C^2\), and

\[
 \pi(\lambda)=\begin{pmatrix}\lambda&0\\0&0\end{pmatrix},
 \qquad q=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Every functional on \(\mathbb C\) is multiplication by a scalar, so the evaluation embedding identifies \(A^{**}\) with \(\mathbb C\). Its normal extension is exactly \(T(\lambda)=\lambda q\), with range \(\mathbb Cq\). A two-by-two matrix commutes with \(q\) precisely when its off-diagonal entries vanish. Therefore \(\pi(A)'\) is the diagonal algebra. An operator commuting with every diagonal matrix is again diagonal, giving

\[
 \pi(A)''=\left\{\begin{pmatrix}s&0\\0&t\end{pmatrix}:
 s,t\in\mathbb C\right\}.
\]

This strictly contains \(\mathbb Cq\), since it contains \(1-q\). On \(K_0=\mathbb C\oplus0\), the represented algebra is \(\mathbb C\) and the extension is onto, as the supported statement requires.

## Second adjoints preserve homomorphisms and composition

Let \(\alpha:A\to C\) be any C*-homomorphism, without a unitality or
nondegeneracy assumption. Its Banach second adjoint

\[
 \alpha^{**}:A^{**}\longrightarrow C^{**}
 \tag{UB.20}
\]

is weak-star continuous and satisfies
\(\alpha^{**}j_A=j_C\alpha\).
The same two successive one-variable limits used in OA-MOD-UB-06 prove
multiplicativity; one limit proves preservation of the involution.
Thus it is a normal *-homomorphism for the structures just constructed.
Banach adjoints give

\[
 (\beta\alpha)^{**}=\beta^{**}\alpha^{**},\qquad
 (\operatorname{id}_A)^{**}=\operatorname{id}_{A^{**}}.
 \tag{UB.21}
\]

These statements include the zero map and zero algebras.

If \(j:B\hookrightarrow A\) is an isometric C*-subalgebra inclusion,
Hahn--Banach makes \(j^*:A^*\to B^*\) onto with norm-preserving lifts.
Consequently \(j^{**}\) is an isometry: the supremum over the unit ball
of \(A^*\) in its dual norm equals the supremum over the unit ball of
\(B^*\). Its range is

\[
 j^{**}(B^{**})=(B^\perp)^\perp\subseteq A^{**}.
 \tag{UB.22}
\]

To see surjectivity onto this annihilator, an \(X\in(B^\perp)^\perp\)
defines \(Y(f)=X(\widetilde f)\) on \(B^*\), where \(\widetilde f\)
is any extension to \(A\). Two such extensions differ in \(B^\perp\);
norm-preserving lifts give \(|Y(f)|\leq\|X\|\|f\|\).
Thus \(Y\in B^{**}\) and \(j^{**}Y=X\).
The annihilator is weak-star closed. This is the precise functorial
bidual input used by the hereditary-corner proof HF-05 and ND-02.
