# Finite Adams-tower detection of a missing homotopy stem

<a id="DG-CHAR-13F-detection.proof"></a>

This argument supplies the detection step for the odd-primary oriented-bordism calculation. It does not presume strong convergence of an infinite spectral sequence. It proves the precise implication needed: vanishing of an entire Ext stem forces divisibility by every power of the prime. For a finite bordism group this detects its primary component.

Let \(p\) be prime, \(k=\mathbb F_p\), \(E=Hk\), and \(A=H^*(E;k)\), with its action by composition of stable cohomology operations. Assume that every graded piece of \(A\) is finite dimensional. Let \(X\) be a connective spectrum whose mod-\(p\) homology is finite dimensional in each degree. Its homotopy groups need not be finite, and no finiteness conclusion about them is assumed in Sections 1-4.

**Finite-detection theorem.** If, for some integer \(n\geq0\),

\[
\operatorname{Ext}^{s,n+s}_A(H^*(X;k),k)=0
\quad\text{for every }s\geq0,
\tag{1}
\]

then

\[
\pi_nX=p^r\pi_nX\quad\text{for every }r\geq1.
\tag{2}
\]

The proof below uses only finitely many stages to deduce (2) for a specified \(r\). In fact stages \(s<2r(n+1)\) in (1) suffice for that conclusion. An unrestricted claim that \(\pi_nX=0\) would be false without an additional group-theoretic hypothesis; \(X=H\mathbb Q\) is a counterexample.

## 1. The tower and its free cohomology resolution

Let \(\bar E\to S\xrightarrow{\eta}E\) be the fibre sequence of the unit of the mod-\(p\) Eilenberg-Mac Lane ring spectrum. Since \(S\to E\) is onto on \(\pi_0\), \(\bar E\) is connective. Define

\[
X_s=\bar E^{\wedge s}\wedge X,
\qquad I_s=E\wedge X_s,
\quad X_0=X.
\]

There are exact triangles

\[
X_{s+1}\xrightarrow{j_s}X_s
\xrightarrow{u_s}I_s
\xrightarrow{\delta_s}\Sigma X_{s+1}.
\tag{3}
\]

Write \(j_s^{[a]}:X_{s+a}\to X_s\) for the composite of \(a\) successive \(j\)'s, with \(j_s^{[0]}=1\). All these spectra are connective. Each is also of finite mod-\(p\) homology type: \(H_*(E;k)\) is degreewise dual to \(A\), the fibre sequence gives the same property for \(\bar E\), and the field Kunneth formula preserves it under each finite smash product. Connectiveness ensures only finitely many degree splittings contribute to a fixed total degree.

Any map \(f:Z\to M\) into an \(E\)-module factors through the unit map of \(Z\):

\[
Z\xrightarrow{\eta\wedge1}E\wedge Z
\xrightarrow{1\wedge f}E\wedge M
\xrightarrow{\mu_M}M.
\tag{4}
\]

The composite equals \(f\) by naturality and the unit law. Apply this to \(M=\Sigma^q E\). Every cohomology class of \(X_s\) extends to \(I_s\), so \(u_s^*:H^*(I_s;k)\to H^*(X_s;k)\) is onto. The long exact sequence of (3) therefore reduces in all degrees to

\[
0\longrightarrow H^*(\Sigma X_{s+1};k)
\xrightarrow{\delta_s^*}H^*(I_s;k)
\xrightarrow{u_s^*}H^*(X_s;k)\longrightarrow0.
\tag{5}
\]

Each \(I_s\) is an \(E\)-module and splits, as an \(E\)-module, into a wedge of suspensions of \(E\). This claim follows directly from its homotopy groups: choose a \(k\)-basis in each \(\pi_dI_s\), lift each basis element to an \(E\)-module map \(\Sigma^dE\to I_s\) by the free-module adjunction, and form their wedge. Its map to \(I_s\) is an isomorphism on every homotopy group, hence an equivalence. There are finitely many summands of each degree, and none of negative degree. Consequently

\[
R_s=H^*(\Sigma^sI_s;k)
\]

is a free graded left \(A\)-module. In a fixed cohomological degree only finitely many of the summands contribute, so cohomology of this wedge is the graded direct sum of the corresponding shifted copies of \(A\), not an unexamined product completion.

Splicing the shifted short exact sequences (5) gives the free resolution

\[
\cdots\longrightarrow R_2\longrightarrow R_1
\longrightarrow R_0\longrightarrow H^*(X;k)\longrightarrow0.
\tag{6}
\]

The arrow \(R_{s+1}\to R_s\) is pullback along

\[
\Sigma^s I_s\xrightarrow{\Sigma^s\delta_s}
\Sigma^{s+1}X_{s+1}\xrightarrow{\Sigma^{s+1}u_{s+1}}
\Sigma^{s+1}I_{s+1}.
\tag{7}
\]

Its consecutive composites are zero by (3). Exactness of (6) follows from (5), without a spectral-sequence convergence assertion.

Maps from a sphere give a natural isomorphism

\[
\pi_{t-s}I_s\cong
\operatorname{Hom}^{-t}_A(R_s,k).
\tag{8}
\]

To verify it, first take one summand \(I_s=\Sigma^dE\). The two sides are \(k\) when \(t=s+d\) and zero otherwise; the nonzero comparison is evaluation of the fundamental class. The wedge decomposition just proved gives (8) in general, degree by degree. Its naturality follows by viewing a sphere map as the induced map on cohomology into \(H^*(S^t;k)=\Sigma^t k\).

Put \(D_1^{s,t}=\pi_{t-s}I_s\). Under (8), the differential on \(\operatorname{Hom}_A(R_\bullet,k)\) becomes

\[
d_1=(u_{s+1})_*\,\delta_{s*}:
\pi_{t-s}I_s\longrightarrow\pi_{t-s-1}I_{s+1}.
\tag{9}
\]

Thus the homology in bidegree \((s,t)\) of this explicitly defined complex is exactly \(\operatorname{Ext}^{s,t}_A(H^*(X;k),k)\). These are the usual first and second Adams pages, but the rest of the proof needs only (3), (6), (8) and (9).

## 2. Zero Ext classes allow each finite lift

Suppose (1) holds. We claim that any \(x\in\pi_nX\) lies in the image of \(\pi_nX_s\to\pi_nX\) for every finite \(s\).

Begin with \(x_0=x\). Given a lift \(x_s\in\pi_nX_s\), its image \(u_{s*}x_s\in D_1^{s,n+s}\) is a \(d_1\)-cycle, since \(\delta_su_s=0\). For \(s=0\), there is no incoming boundary. The vanishing in (1) therefore implies \(u_{0*}x_0=0\), and exactness of (3) gives a lift to \(X_1\).

For \(s\geq1\), (1) says that there is

\[
a\in D_1^{s-1,n+s}=\pi_{n+1}I_{s-1}
\quad\text{with}\quad
(u_s)_*(\delta_{s-1})_*a=(u_s)_*x_s.
\]

Replace \(x_s\) by

\[
x'_s=x_s-(\delta_{s-1})_*a.
\tag{10}
\]

The correction maps to zero in \(\pi_nX_{s-1}\), by the preceding exact triangle, so \(x'_s\) still maps to the original \(x\) in \(\pi_nX\). Its image under \(u_s\) is now zero. Exactness of (3) lifts \(x'_s\) to \(x_{s+1}\). This induction proves the claim. Compatible choices in an inverse limit are neither asserted nor required: for any prescribed finite depth the construction supplies a lift to that depth.

Define the tower filtration by

\[
F^s\pi_nX=\operatorname{im}\bigl(\pi_nX_s\xrightarrow{(j_0^{[s]})_*}\pi_nX\bigr).
\]

We have proved \(\pi_nX=F^s\pi_nX\) for every \(s\) if (1) holds.

## 3. Finite targets detect divisibility

We first specify the truncation and layers used below. For a connective spectrum \(Y\), kill its homotopy groups above degree \(n\) successively. At degree \(j>n\), choose sphere maps representing generators of \(\pi_j\), and take the cofiber of their map \(\bigvee S^j\to Y\). The long exact sequence kills \(\pi_j\) and preserves all lower groups. Repeat at the next degree, including any higher classes introduced by the preceding cell attachment, and take the telescope. Compactness of spheres makes its homotopy groups the colimits; hence the resulting \(\tau_{\leq n}Y\) agrees with \(Y\) through degree \(n\) and has no higher homotopy. Maps into a spectrum with no homotopy above \(n\) extend uniquely in the homotopy category through these attachments, because both the obstruction and ambiguity groups in degrees \(j,j+1>n\) vanish. This gives the transition maps \(\tau_{\leq j}Y\to\tau_{\leq j-1}Y\).

The fibre of this transition has only one homotopy group, \(\pi_jY\) in degree \(j\), so it is \(\Sigma^jH\pi_jY\). One can verify the Eilenberg-Mac Lane identification without a splitting assumption: present an abelian group \(G\) as a cokernel of a map of free groups, form the corresponding cofiber of a map between wedges of sphere spectra, and kill its positive homotopy groups by the preceding procedure with \(n=0\). This constructs \(HG\). The same presentation maps to any connective spectrum with only \(\pi_0=G\); the relations are nullhomotopic, and the subsequent extensions have no higher obstruction or ambiguity. It gives an isomorphism on all homotopy groups and hence an equivalence. Maps between these spectra are determined by their homomorphisms on \(\pi_0\). A short exact sequence \(0\to G'\to G\to G''\to0\) therefore gives the triangle \(HG'\to HG\to HG''\): its cofiber has \(\pi_0=G''\) and no other homotopy, by the long exact sequence. These constructions justify the finite Postnikov layers and the group-extension triangles used here; they do not assume that the layers split.

Say that a spectrum has \(E\)-extension length at most one if it is an \(E\)-module (suspensions are allowed). Lengths add under exact triangles: a triangle \(T'\to T\to T''\) with lengths at most \(a,b\) assigns \(T\) length at most \(a+b\). Only a finite construction with these rules is being asserted, not a general classification of spectra.

**Vanishing of composites.** If \(T\) is so constructed with length at most \(N\), every map \(f:X_s\to T\) satisfies \(f\,j_s^{[N]}=0\).

For an \(E\)-module this follows from (4) and \(u_sj_s=0\). For the inductive step, project \(f\) to \(T''\). After \(b\) tower maps it is zero, so exactness of the target triangle lifts \(f\,j_s^{[b]}\) to a map \(X_{s+b}\to T'\). Another \(a\) tower maps kill that lift. This proves the assertion for \(N=a+b\). The argument uses an actual lift in the homotopy category and does not assert that vanishing of a composite makes the original map zero.

If an abelian group \(G\) is killed by \(p^e\), its Eilenberg-Mac Lane spectrum \(HG\) has length at most \(e\). Use the finite filtration

\[
G\supset pG\supset\cdots\supset p^eG=0.
\]

Each quotient is a \(k\)-vector space. Its Eilenberg-Mac Lane spectrum is an \(E\)-module (choose a basis and take a wedge of copies of \(E\)). Short exact sequences of groups give exact triangles of their Eilenberg-Mac Lane spectra, so the filtration proves the bound. No assumption that \(G\) is finite is needed.

Fix \(r\geq1\). Let \(X/p^r\) be the cofiber of \(p^r:X\to X\), and set

\[
T=\tau_{\leq n}(X/p^r),\qquad
q:X\longrightarrow X/p^r\longrightarrow T.
\tag{11}
\]

The cofiber and its truncation are connective. The homotopy long exact sequence gives, for \(0\leq j\leq n\),

\[
0\longrightarrow\pi_jX/p^r\pi_jX
\longrightarrow\pi_j(X/p^r)
\longrightarrow(\pi_{j-1}X)[p^r]\longrightarrow0.
\tag{12}
\]

Both outer terms are killed by \(p^r\), so the middle term is killed by \(p^{2r}\). The finite Postnikov construction of \(T\) has \(n+1\) layers \(\Sigma^jH\pi_j(X/p^r)\), for \(0\leq j\leq n\). The preceding paragraph bounds the length of each layer by \(2r\). Thus \(T\) has \(E\)-extension length at most

\[
N=2r(n+1).
\tag{13}
\]

The vanishing-of-composites assertion applied to \(q\) gives \(q\,j_0^{[N]}=0\). Since truncation in (11) is an isomorphism on \(\pi_n\), exactness of the cofiber sequence gives

\[
F^{2r(n+1)}\pi_nX\subseteq\ker q_*
=p^r\pi_nX.
\tag{14}
\]

Combining (14) with Section 2 proves (2). To obtain this for a fixed \(r\), only the lifts through stage \(N\), and therefore the Ext vanishings for \(0\leq s<N\), were used.

There is also a useful reverse comparison. The map \(p:S\to S\) lifts to \(\bar E\), because its composite with \(\eta\) is zero in \(\pi_0E=k\). Smashing \(s\) copies of such a lift with \(X\) gives a map \(X\to X_s\) whose composite to \(X\) is \(p^s\). Consequently

\[
p^s\pi_nX\subseteq F^s\pi_nX,
\qquad F^{2r(n+1)}\pi_nX\subseteq p^r\pi_nX.
\tag{15}
\]

The two filtrations are cofinal. On a finitely generated \(p\)-local abelian group they are separated, since the elementary decomposition into a finite-rank free \(\mathbb Z_{(p)}\)-module and finite \(p\)-power torsion makes \(\bigcap_r p^rG=0\). For the finite-detection theorem and the application below, however, the finite containment (14) already suffices; no exchange of an inverse limit and a homotopy group is involved.

## 4. Why the hypotheses and the conclusion matter

The conclusion is divisibility, not automatic vanishing. For example \(X=H\mathbb Q\) has trivial mod-\(p\) cohomology, so (1) holds in degree zero, whereas \(\pi_0X=\mathbb Q\ne0\). It does satisfy (2). This example prohibits promoting an empty Ext stem to zero homotopy without the additional argument.

Connectiveness was used in two places: the free resolution has locally finite graded pieces, and the target \(\tau_{\leq n}(X/p^r)\) has finitely many nonzero Postnikov layers. For a spectrum bounded below in degree \(b\), the same proof after suspension uses \(2r(n-b+1)\) in place of (13). No statement here covers an arbitrary unbounded-below spectrum.

Finite type was used to identify the free cohomology modules and graded Hom complexes without an unaccounted product or continuity condition. The filtration containment (14) itself only uses the tower, connectiveness and the finite-length target construction.

## 5. Application to oriented seven-dimensional bordism

The Thom-space construction makes \(MSO\) connective. The stable cohomology calculation in *The odd-primary Thom module*, Section 3, shows finite mod-\(p\) type at every odd prime. The full operation-algebra input **O** is proved in the [one-group companion](odd-primary-one-group-cohomology.md), Section 9. The Thom-module proof, Sections 2–5, and the [exterior resolution](odd-primary-exterior-resolution.md) therefore give

\[
\operatorname{Ext}^{s,7+s}_A(H^*(MSO;k),k)=0
\quad(s\geq0).
\]

The finite-detection theorem with \(n=7,r=1\) therefore shows

\[
\Omega_7^{SO}=p\Omega_7^{SO}
\quad\text{for every odd prime }p.
\tag{16}
\]

Depth sixteen in the tower suffices for each instance of (16). The geometric comparison and finite-generation/rational-rank argument show that \(\Omega_7^{SO}\) is a finite group of odd order. These facts, together with (16), force it to be zero. Indeed a nonzero element of order \(d>1\) would give an element of order \(p\) for some odd prime divisor \(p\mid d\). Multiplication by \(p\) would then have a nonzero kernel and hence would not be surjective on the finite group, contrary to (16).

This finite detection argument supplies the homotopy implication required here. It makes no general strong-convergence claim. The operation-algebra computation and the finite-odd-order theorem are separate proved inputs, not consequences of an empty Ext stem alone.

Haynes Miller, [*Notes on Cobordism*](https://math.mit.edu/~hrm/papers/cobordism.pdf), Chapter 2, Section 10, and [*Notes on the Adams Spectral Sequence*](https://math.mit.edu/~hrm/papers/notes-adams-spectral-sequence.pdf), p. 25, describe the relative-resolution route. Sections 2–3 above prove the finite obstruction correction and Postnikov-target argument explicitly.
