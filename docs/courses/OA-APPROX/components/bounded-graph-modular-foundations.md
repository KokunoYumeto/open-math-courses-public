# Modular normalization and fullification from bounded graph projections

This proof concerns an arbitrary complex Hilbert space. No cyclic vector,
faithful state, countability or finiteness assumption is made. Inner products
are linear in the first variable. The new exposition is dedicated under
CC0-1.0 to the extent of rights held. The freely readable human proof method is
credited to Marc A. Rieffel and Alfons Van Daele, *A bounded operator approach
to Tomita–Takesaki theory*, Pacific Journal of Mathematics 69 (1977),
187–221, especially Proposition 2.2, Proposition 3.1, Lemmas 5.4–5.12,
Theorems 5.13–5.15 and the appendix:
<https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf>.
The article and its images retain their human authors' rights; this dedication
does not apply to them. A correction to the existence argument in Lemma 5.6
is included below.

The prerequisites are [orthogonal projections and full bounded/unbounded spectral calculus](../../OA-FLOW/OA-FLOW-SF.html#oa-flow.shared-foundations.sf-0), [bicommutant and positive-contraction density in the original algebra](../../OA-FLOW/OA-FLOW-BD.html#oa-flow.bd.1), and [vectorwise integration, the scalar hyperbolic kernel and continuous Fourier uniqueness](../../OA-FLOW/OA-FLOW-MF-SB.html#oa-flow.mf-sb.2). The latter uses the explicit [scalar measure and integration construction](../../OA-FLOW/OA-FLOW-SC.html), [elementary Banach, Hilbert and continuous calculus](../../OA-FLOW/OA-FLOW-CF.html), [real-Borel interchange and Gaussian Fourier construction](../../OA-FLOW/OA-FLOW-FF.html#oa-flow.ff.1), and [rectangle Cauchy proof](../../OA-FLOW/OA-FLOW-SF.html#oa-flow.sf4.rectangle-cauchy). All Hilbert spaces and left Hilbert algebras retain their full stated generality.

The following diagram records the bounded objects used in BG1–6. The graph projection E is a projection in H ⊕ H; its entries p and b are operators on H. The spectral inversions in BG4 are performed on finite bands of R. The conclusion in BG6 identifies complete closed domains.

<svg xmlns="http://www.w3.org/2000/svg" width="1140" height="610" viewBox="0 0 1140 610">
<rect width="1140" height="610" fill="#f9fbff"/>
<defs><marker id="bg-arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#254b6d"/></marker></defs>
<g font-family="Arial, sans-serif" fill="#17344c">
<text x="45" y="46" font-size="27" font-weight="bold">Bounded data recover the complete modular graphs</text>
<text x="45" y="79" font-size="19">Any left Hilbert algebra A ⊂ H; no cyclic vector or countability assumption</text>
<g fill="white" stroke="#254b6d" stroke-width="2"><rect x="45" y="110" width="475" height="145" rx="10"/><rect x="620" y="110" width="475" height="145" rx="10"/><rect x="45" y="340" width="475" height="145" rx="10"/><rect x="620" y="340" width="475" height="145" rx="10"/></g>
<g font-size="21"><text x="65" y="144" font-weight="bold">Real subspace K and projections P, Q</text><text x="65" y="179">R = P + Q; T² = R(2 − R)</text><text x="65" y="213">P − Q = JT; V = (iK)⊥ = JK  [BG1]</text>
<text x="640" y="144" font-weight="bold">Closed graph-subspace projection E</text><text x="640" y="179">Re λ = 1: p ≥ (1 + ∥Lξ∥²)⁻¹I</text><text x="640" y="213">p, b ∈ M′; Bη = p⁻¹b  [BG2–3]</text>
<text x="65" y="374" font-weight="bold">Finite-band inversion and scalar kernels</text><text x="65" y="409">Uₜ = (2 − R)ⁱᵗ R⁻ⁱᵗ; JMJ = M′</text><text x="65" y="443">Uₜ M U₋ₜ = M  [BG4–5]</text>
<text x="640" y="374" font-weight="bold">Fullification and whole closed graphs</text><text x="640" y="409">A′ = Br ∩ D(F); A″ = Bl ∩ D(S)</text><text x="640" y="443">S = JΔ½; F = JΔ−½  [BG6]</text></g>
<g stroke="#254b6d" stroke-width="3" fill="none" marker-end="url(#bg-arrow)"><path d="M525 182H610"/><path d="M850 263L850 288L285 288L285 330"/><path d="M525 413H610"/></g>
<text x="45" y="535" font-size="21">D(S) = K + iK; D(F) = V + iV; Δ = (2 − R)/R with its full spectral domain.</text>
<text x="45" y="569" font-size="18">Human proof method: Rieffel–Van Daele (1977), §5 and appendix; explicit coercivity correction in BG2.</text>
</g>
</svg>

<a id="bg1"></a>

## BG1. The real subspace determines bounded modular data

Let A be a dense complex algebra in H with conjugate-linear involution #,
with A² dense, bounded left multipliers L_a, the identity
⟨ab,c⟩=⟨b,a#c⟩, and closable #. Write M=L(A)''. The representation is
nondegenerate since A² is dense, and L_{a#}=L_a*. Its common kernel is zero.
It is faithful: L_a=0 gives b#a#=0 for all b, hence a#=0 by nondegeneracy.

Let K be the closed real span of a#a, and let Q be the real orthogonal
projection onto iK; P is the real projection onto K. Polarization says
K+iK contains A² and is dense. Every vector in K lies in the graph closure
of # with value itself: approximate it by real finite sums of a#a. Every
vector in iK has value its negative. Closability therefore gives K∩iK=0.
Put

\[
 R=P+Q,\qquad T=[R(2-R)]^{1/2},\qquad C=P-Q.
\tag{BG1}
\]

Both R and 2−R are injective: their kernels are respectively
K⊥∩(iK)⊥ and K∩iK. They are positive real operators with 0≤R≤2.
The identities C²=R(2−R), C P=(1−Q)C and C Q=(1−P)C follow by
multiplying the projections. Also C² commutes with P and Q. Consequently
T does too. Define J on the dense range of T by J(Tu)=Cu.
The equality ||Cu||=||Tu|| makes it an isometry; its range is dense because
C is self-adjoint and injective. Thus it extends to a self-adjoint real
orthogonal operator, with J²=1, C=JT=TJ, and

\[
 JP=(1-Q)J,\quad JQ=(1-P)J,\quad JR=(2-R)J.
\tag{BG2}
\]

Here cancellation of T is valid by its injectivity, rather than by a bounded
inverse. Multiplication by i interchanges P and Q, so R and T are complex
linear and C and J are conjugate-linear. J is an antiunitary. In particular
J K=(iK)⊥. Set V=(iK)⊥ and define, by bounded Borel calculus,

\[
 U_t=(2-R)^{it}R^{-it}\quad(t\in\mathbb R).
\tag{BG3}
\]

The endpoint spectral masses vanish by injectivity. Scalar dominated
convergence proves strong continuity and the group law. Anti-linearity in
(BG2) gives J U_t J=U_t, not U_{−t}. The group preserves K, iK and V:
it commutes with R and C=TJ, hence with P=(R+C)/2 and Q=(R−C)/2 as real
operators. No unbounded product is being taken in (BG3).

<a id="bg2"></a>

## BG2. A graph projection supplies a bounded dual vector

Define A' to consist of η∈H for which bounded B_η and a vector ηᵇ satisfy

\[
 B_\eta a=L_a\eta,\qquad B_\eta^*a=L_a\eta^\flat
 \quad(a\in A).
\tag{BG4}
\]

Both are unique by density and nondegeneracy. Associativity on A shows
B_η∈M'. One has (ηᵇ)ᵇ=η. A' is an algebra with product
η∘ζ=B_ηζ, B_{η∘ζ}=B_ηB_ζ, and
(η∘ζ)ᵇ=ζᵇ∘ηᵇ. To verify membership, test on a∈A, move B_η and B_ζ
past L_a, and use the same identities with B_ζ*B_η*. This also proves
⟨η∘ζ,θ⟩=⟨ζ,ηᵇ∘θ⟩. Self-adjoint elements of A' lie in V: for ηᵇ=η,
⟨η,a#a⟩=⟨B_ηa,a⟩ is real, and then use real span and closure.

For any η∈H take the closure N of
{(a,L_aη):a∈A} in H⊕H. This is a closed subspace, whether or not the
initial multiplier map has yet been proved closable. It reduces the
diagonal left representation: invariance follows from associativity, and
invariance under adjoints from L_a*=L_{a#}. Write its orthogonal projection

\[
 E=\begin{pmatrix}p&b\\b^*&c\end{pmatrix}.
\]

Its entries belong to M'. The projection identities and E(a,L_aη)=(a,L_aη)
give

\[
 \begin{split}
 &0\le p,c\le1,\quad bb^*=p(1-p),\quad b^*b=c(1-c),\quad
 bc=(1-p)b,\\
 &L_a b\eta=(1-p)a,\qquad L_a(1-c)\eta=b^*a.
 \end{split}
\tag{BG5}
\]

If η∈V, the quadratic form ⟨L_aη,a⟩ is real. Polarization makes
⟨L_aη,d⟩=⟨a,L_dη⟩. Thus (L_aη,−a) is orthogonal to N, and E kills it.
Its two components give

\[
 L_a p\eta=ba,\qquad L_a b^*\eta=ca.
\tag{BG6}
\]

The first diagonal block p is injective: pu=0 implies b*u=0 by
bb*=p(1−p); E(u,0)=0 then implies ⟨u,a⟩=0 for every a∈A.
This is a statement about a graph projection, with no assumed multiplier
adjoint core.

We next solve a real equation. For λ with Re λ>0, define on the real Hilbert
space V the bounded real operator D_λ=pr_V(λ·)|_V. It has
⟨D_λu,u⟩_real=(Re λ)||u||², hence ||D_λu||≥(Re λ)||u||.
Its range is closed. Its adjoint has the same coercivity, so has zero kernel;
the range is dense and therefore all of V. In particular D_λ is invertible.
Equivalently D_λ=(Re λ)I+(Im λ)pr_V(i·)|_V and its second term is
skew-adjoint. It need not be a scalar-product operator. This supplies the
missing justification in the article's Lemma 5.6.

For ξ∈K there is consequently a unique η∈V with

\[
 \langle\xi,z\rangle=\operatorname{Re}\bigl(\lambda
 \langle\eta,z\rangle\bigr)\quad(z\in V).
\tag{BG7}
\]

The left side is real since V=(iK)⊥. If also ξ∈A, this η belongs to A'
and is self-adjoint there. Here are the full boundedness estimates; normalize
Re λ=1 by dividing both ξ and λ by Re λ. For a spectral projection e of p,
the vectors z=e bb*η and zᵇ=b*e bη belong to A'. Indeed their multipliers
are e(1−p)b and its adjoint b*e(1−p), by (BG5)–(BG6). Decomposing any
element of A' into its real and imaginary parts extends (BG7) to

\[
 2\langle\xi,z\rangle=\lambda\langle\eta,z\rangle+
 \overline\lambda\langle z^\flat,\eta\rangle\quad(z\in A').
\tag{BG8}
\]

Apply (BG8) to zᵇ and take real parts. Both quadratic expressions on its
right are real. The inequality 2 Re⟨e bξ,e bη⟩≤||e bξ||²+||e bη||²
cancels one of them and leaves

\[
 \langle e p(1-p)\eta,\eta\rangle\le\|e b\xi\|^2
 =\|L_\xi e p\eta\|^2\le\|L_\xi\|^2\|e p\eta\|^2.
\tag{BG9}
\]

For \(e=1_{[0,\varepsilon]}(p)\), the left side is at least
(1−ε)⟨e pη,η⟩ and the right at most ||L_ξ||² ε⟨e pη,η⟩.
Thus e pη=0 when ε<(1+||L_ξ||²)⁻¹. Equation (BG6) and density of A give
e b=0; hence e p(1−p)=0 and e p=0. Injectivity of p makes e=0.
It follows that p≥(1+||L_ξ||²)⁻¹ I. The bounded operator p⁻¹b satisfies
(p⁻¹b)a=L_aη. Its quadratic form on a∈A is real because η∈V, so it is
self-adjoint. It and η satisfy (BG4), with ηᵇ=η. Moreover
||p⁻¹b||²=||(1−p)/p||≤||L_ξ||² in the normalized equation.

Taking λ=1 in (BG7) gives η=(1−Q)ξ=TJξ for ξ∈K∩A. Polarization of a#a
therefore gives

\[
 TJ A^2\subset A',\qquad (TJ a)^\flat=TJ a^\#\quad(a\in A^2).
\tag{BG10}
\]

For a∈A² one also has TJ a=(2−R)a#: verify it first on a#a using
Pa=a, and extend using conjugate-linearity. For η∈A', TJη=Rηᵇ:
verify on its self-adjoint real and imaginary parts, which lie in V.

<a id="bg3"></a>

## BG3. The two bounded equations

Fix ξ∈A∩K and λ with Re λ>0. Apply (BG7) with ξ/2 in place of ξ. Thus
η∈A', ηᵇ=η and

\[
 \langle\xi,z\rangle=\lambda\langle\eta,z\rangle+
 \overline\lambda\langle z^\flat,\eta\rangle\quad(z\in A').
\tag{BG11}
\]

Let B=B_η. The following are identities of bounded operators and vectors:

\[
 \begin{split}
 T J L_\xi J T&=\lambda(2-R)BR+\overline\lambda R B(2-R),\\
 T J\xi&=[\lambda(2-R)+\overline\lambda R]\eta.
 \end{split}
\tag{BG12}
\]

For clarity the testing identities that prove them are given explicitly.
For x,y∈A² put w=TJx and z=TJy. Substitute zᵇ∘w into (BG11), use
B_η a=L_aη and the adjoint multiplication identity, and move the two
antiunitaries through the inner-product pairing. The resulting equality is

\[
 \langle x,TJ L_\xi TJ y\rangle
 =\lambda\langle x,TJ(z\circ\eta)\rangle+
 \overline\lambda\langle TJ(w\circ\eta),y\rangle.
\]

Here TJ(z∘η)=R B zᵇ=R B(2−R)y and the same formula holds for w.
Taking the adjoint of R B(2−R) in the second term, and remembering that a
coefficient in the second inner-product variable is conjugated, gives the
first line of (BG12). A² is dense, so no graph extension is needed.
For the second line take x∈A²∩K and put z=TJx in (BG11). The same
antiunitary pairing yields
⟨x,TJξ⟩=λ⟨x,TJη⟩+bar λ⟨TJx,η⟩.
Now TJη=Rη and TJx=(2−R)x. Complex span of these x is dense, proving
the second line. The norm bound above is ||B||≤||L_ξ||/(2 Re λ).

<a id="bg4"></a>

## BG4. Solve the equations with scalar kernels, without unbounded products

Write w(t)=1/(2 cosh πt). For any complex s with |Im s|<π,

\[
 \int_{\mathbb R}e^{ist}w(t)\,dt={1\over2\cosh(s/2)}.
\tag{BG13}
\]

The single-pole proof of MF-SB, SB-2, works for this whole strip: on the
rectangle [−N,N]+i[0,1] the vertical edges have bound
O(exp(−(π−|Im s|)N)). There is just the pole i/2. Subtract
\(e^{-s/2}/[2\pi i(z-i/2)]\); its continuous extension follows from the exponential
Taylor remainder. Four-rectangle cancellation proves its integral zero,
and the small square integral of 1/(z−i/2) is 2πi. The top horizontal
integrand is \(-e^{-s}\) times the bottom integrand; its reversed orientation
therefore contributes \(+e^{-s}\) times the bottom integral. Consequently
\((1+e^{-s})I(s)=e^{-s/2}\). The denominator is nonzero for |Im s|<π.
All tails are absolutely integrable, so this proves (BG13) with its constants.

Set \(\lambda=e^{i\varphi/2}\), \(-\pi<\varphi<\pi\), and \(h_\varphi(t)=e^{-\varphi t}w(t)\). The inverse formulas for
(BG12) are

\[
 \begin{split}
 B&=\int_{\mathbb R}h_\varphi(t)U_t J L_\xi J U_{-t}\,dt,\\
 \eta&=\int_{\mathbb R}h_\varphi(t)U_t J\xi\,dt.
 \end{split}
\tag{BG14}
\]

These are continuous vectorwise improper integrals. They have norm majorant
h_φ, whose integral is 1/(2 cos(φ/2)) by (BG13) at s=iφ.
Here is a bounded proof of the operator inversion. Let
\(e_n=1_{[1/n,2-1/n]}(R)\), n≥2. On e_nH, D=(2−R)/R is bounded, positive
and boundedly invertible. Compress the first equation in (BG12) and cancel
the boundedly invertible factors \(R^{1/2}\); it reads

\[
 C=\lambda D^{1/2}B D^{-1/2}+\overline\lambda D^{-1/2}B D^{1/2},
 \qquad C=e_n J L_\xi J e_n.
\]

For a finite spectral step operator D=Σ d_j E_j, each (j,k) matrix block
is multiplied by λ√(d_j/d_k)+bar λ√(d_k/d_j). Its inverse is
\(\int h_\varphi(t)(d_j/d_k)^{it}\,dt\) by (BG13). Thus
\(B=\int h_\varphi(t)D^{it}C D^{-it}\,dt\). Approximate a general D uniformly by finite
positive spectral step operators on a fixed compact interval [m,M]⊂(0,∞).
The square-root maps and imaginary-power maps converge in norm, the latter
at each fixed t. Dominated convergence with bound h_φ||C|| proves both
inverse identities in operator norm, and hence the assertion for the actual
compressed B. Finally e_n→1 strongly; continuous vector integrals and their
common bound h_φ||L_ξ|| let n tend to infinity, giving the first line of
(BG14). The scalar multiplier √d/(λd+bar λ) gives the second line directly
by (BG13), or by the same spectral compression. All cancellations were on
the finite spectral bands. No global unbounded operator sandwich was used.

<a id="bg5"></a>

## BG5. Recover individual vectors and the full commutant

Take ξ=a#a. Since B_ηd=L_dη for every d∈A, subtract the two formulas in
(BG14) after applying them to d. For all −π<φ<π,

\[
 \int e^{-\varphi t}w(t)
 [L_dU_tJ\xi-U_t J L_\xi J U_{-t}d]\,dt=0.
\tag{BG15}
\]

The bracket is continuous and bounded in H. Pair it with any vector to
get a bounded continuous scalar g. The transform
\(F(z)=\int e^{-zt}w(t)g(t)\,dt\) has, on |Re z|<π, a locally convergent power
series obtained by expanding the exponential under its integrable
majorant. Its vanishing on the real interval makes all coefficients at
zero vanish. Overlapping disks along the imaginary axis propagate this
zero power series to every point is. Thus the Fourier transform of wg
is zero. Continuous L¹ Fourier uniqueness (MF-SB, SB-3) gives wg=0
almost everywhere, hence everywhere by continuity. Since w>0, g=0.
All pairings vanish, so the bracket in (BG15) is zero for every t.
Its right-hand operator is self-adjoint. Definition (BG4) now gives

\[
 U_tJ\xi\in A',\quad (U_tJ\xi)^\flat=U_tJ\xi,\quad
 B_{U_tJ\xi}=U_tJ L_\xi J U_{-t}\quad(\xi=a^\#a).
\tag{BG16}
\]

Choose positive contractions a_i∈A with L_{a_i}→1 strongly, using BD's
nondegenerate contraction density, and replace them if needed by a_i#a_i.
Then c_i=B_{J(a_i#a_i)}=J L_{a_i#a_i}J are positive contractions
converging strongly to 1. The dual algebra A' is dense, and (A')² is
dense, since c_iH lies in the closure of A' and c_i A'⊂(A')².
More explicitly J A²⊂A' follows from polarization of (BG16) at t=0,
so A' itself is already dense; then c_iη→η for η∈A' proves the assertion
about products.

For x∈M' and η,ζ∈A', the vector B_η x ζ belongs to A', with multiplier
B_η x B_ζ and adjoint partner B_ζ* x*ηᵇ. Both statements follow by testing
on d∈A and commuting L_d past operators in M'. Hence c_i x c_i belongs
to B(A') and converges strongly to x. We have proved

\[
 B(A')''=M'.
\tag{BG17}
\]

The closure K' of real span of ηᵇ∘η equals V. First K'⊂V, since the
vectors are self-adjoint. The image TJ K is dense in V: J K=V,
T reduces V and has zero kernel, so its restriction has dense range.
Equation (BG10) therefore makes self-adjoint elements of A' dense in V.
Each such element η is itself in K'. Indeed let f be the range support
projection of B_η. For d∈A,
L_d(fη−η)=(f−1)B_ηd=0, and the common kernel of L(A) is zero. Thus fη=η.
Real polynomials p_n with p_n(0)=0 can approach f strongly on B_η;
p_n(B_η)η is a real sum of products of self-adjoint elements and belongs
to the real span of squares by real polarization. It tends to η.
This proves K'=V, without assuming a closed unbounded multiplier.

The involution on A' is closable. If η_n→0 and η_nᵇ→v, then
⟨η_n,d#a⟩=⟨a#d,η_nᵇ⟩ for d,a∈A, by (BG4); density of A² gives v=0.
Thus A' is another left Hilbert algebra satisfying the hypotheses of BG1.
Its projections are P'=1−Q and Q'=1−P, so R'=2−R, T'=T, J'=J and
U'_t=U_{−t}. Apply the already proved BG16 to this algebra and use
(BG17). At t=0 it gives J M' J⊂M. The original BG16 gives J M J⊂M'.
Together these give J M J=M'. For arbitrary t, BG16 gives
U_t J M J U_{−t}⊂M'; therefore U_tM'U_{−t}⊂M'. Replacing t by −t
makes this equality, and taking commutants proves

\[
 J M J=M',\qquad U_t M U_{-t}=M.
\tag{BG18}
\]

<a id="bg6"></a>

## BG6. Every algebra vector, fullification, and full closed graphs

For self-adjoint ξ∈A, the range support f of L_ξ satisfies fξ=ξ. This
time test with every B_η from A'; their representation is nondegenerate,
and B_η(fξ−ξ)=(f−1)L_ξη=0. Put m≥||L_ξ||, m>0, and
p_n(r)=1−(1−r²/m²)^n. Then p_n(L_ξ)→f strongly, with norm≤1.
The vectors ξ_n=p_n(L_ξ)ξ lie in the real span of a#a (real polarization
of the commuting self-adjoint powers), converge to ξ, and their multipliers
L_{ξ_n}=p_n(L_ξ)L_ξ converge strongly to L_ξ with a common norm bound.
Apply (BG16), extended by real linearity to this span, and pass to the
limit in each identity tested on d∈A. Both vector and adjoint identities
survive. For general ξ, split it into its self-adjoint real and imaginary
parts, keeping the minus sign when J crosses i. The result is

\[
 \begin{split}
 &U_tJ\xi\in A',\qquad (U_tJ\xi)^\flat=U_tJ\xi^\#,\\
 &B_{U_tJ\xi}=U_tJ L_\xi J U_{-t}\quad(\xi\in A).
 \end{split}
\tag{BG19}
\]

Define A'' as the dual of A' by (BG4), and subsequent primes likewise.
For ξ∈A and η∈A', L_ξη=B_ηξ and L_ξ*η=L_{ξ#}η=B_ηξ#,
so A⊂A'' with the
same multiplier and involution. Restricting the defining tests of A'''
to A proves A'''⊂A'; the general inclusion B⊂B'' applied to B=A'
proves the reverse inclusion. Hence A'''=A' and A''''=A''.
Equation (BG17) applied to A' says the left algebra of A'' is M.
Thus A'' is full and enlarges A without changing M. A' is full too.

All these are genuine Hilbert algebras: their real subspaces successively
are K, V=(iK)⊥ and K again, by the proved K'=V calculation applied to
the successive algebras. They therefore have the same J, with U_t
reversed exactly on the odd dual. Applying (BG19) to A'' and to A'
gives J A''=A', U_t A''=A'', and, for ξ∈A'',

\[
 L_{U_t\xi}=U_tL_\xi U_{-t},\qquad B_{J\xi}=J L_\xi J.
\tag{BG20}
\]

For the first identity compose the two dual identities; J U_t=U_t J
and J²=1 remove the two antiunitaries. If the original algebra is full,
A=A'', these assertions hold on the original algebra. For the right
Hilbert-algebra convention, take the opposite product on A': ηζ=B_ζη.
Its right multiplier is B_η, its involution is still ᵇ, and (BG20)
is the corresponding left/right bounded-vector covariance. This explains
the product reversal rather than silently identifying the two conventions.

Finally identify the full closed involution. A self-adjoint ξ∈A was just
shown to be in K, so K is the closure of A's self-adjoint real part.
The operator

\[
 S(k+i\ell)=k-i\ell,\quad D(S)=K+iK
\tag{BG21}
\]

is closed: a graph-convergent pair determines convergent k and ℓ separately,
and K is closed. Approximation of k and ℓ by self-adjoint elements of A
shows its graph is exactly the closure of # on A. The same argument shows
that # on A'' has this whole graph, and ᵇ on A' has the graph
F(v+iw)=v−iw, D(F)=V+iV. To check F=S*, apply the real adjoint test to
k+iℓ and use V=(iK)⊥; conversely the adjoint test with ℓ=0 and k=0
forces a vector into V+iV. Equivalently in the real Hilbert space
the adjoint domain is (iK)⊥+K⊥=V+iV. Both operators are
conjugate-linear, so this real adjoint test is also their conjugate-linear
complex adjoint test: test with x and ix to recover both real and imaginary
parts. Also F=JSJ by (BG2). These are equalities of domains and values.

The approximants ξ_n above show that A² is a whole graph core for S:
approximate the self-adjoint real and imaginary parts of an algebra vector
by these self-adjoint product vectors, then use that A is a graph core.
This identifies the dual with the bounded-vector convention used by the
weight applications. If η∈A', its pairing identity
⟨η,d#a⟩=⟨a#d,ηᵇ⟩ on products extends on this whole core to the
conjugate-linear adjoint criterion, giving η∈D(F), Fη=ηᵇ. Conversely,
if the map a↦L_aη is bounded and η∈D(F), then
⟨L_aη,d⟩=⟨η,a#d⟩=⟨d#a,Fη⟩=⟨a,L_dFη⟩ for a,d∈A.
Thus its bounded adjoint on d is L_dFη, exactly (BG4). Therefore

\[
 A'=B_r\cap D(F),\qquad \eta^\flat=F\eta,
 \qquad A''=B_l\cap D(S),
\tag{BG21a}
\]

where B_l is defined using the nondegenerate right representation B(A').
The last equality is the same universal adjoint criterion applied to the
dual algebra, whose whole closed involution is F and whose adjoint is S.
It preserves the entire bounded-vector and full-domain contract.

Let Δ be the positive spectral multiplier (2−r)/r of R, with its full
square-integrability domain. For x∈D(S), direct substitution of k+iℓ
gives (2−R)Sx=JT x. Since JR=(2−R)J, this implies
R J Sx=T x. On [1/n,2−1/n] spectral bands,
\(JSx=\Delta^{1/2}x\). Passing to the scalar spectral limit shows
\(x\in D(\Delta^{1/2})\) and the same identity on the full domain. The real adjoint
identity F=JSJ gives (JS)*=S*J=FJ=JS; JS is complex-linear self-adjoint.
The inclusion \(JS\subset\Delta^{1/2}\) between self-adjoint operators is therefore
equality, with equality of their domains. Taking adjoints proves

\[
 S=J\Delta^{1/2},\qquad F=J\Delta^{-1/2},\qquad
 J\Delta J=\Delta^{-1},\qquad U_t=\Delta^{it}.
\tag{BG22}
\]

The self-adjoint maximality used here has a short domain proof: if A⊂B
and both are self-adjoint, adjoint reversal gives B=B*⊂A*=A. Thus it
introduces no additional modular theorem. Equation (BG22) uses the stated
spectral full-domain input; none of its graph equalities assumes a
separating vector, a finite weight, an unproved adjoint core, or an
unbounded globally defined sandwich. This finishes the bounded route at
the declared earlier foundations.

[Continue with fixed modular corners](fixed-modular-corners-from-whole-graphs.md) · [Return to constant CAR states](../src/constant-car-states-and-the-periodic-core.md).
