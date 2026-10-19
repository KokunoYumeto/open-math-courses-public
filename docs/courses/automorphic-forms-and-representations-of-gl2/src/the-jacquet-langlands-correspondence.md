# The Jacquet–Langlands correspondence

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A quaternion division algebra has fewer conjugacy classes than a matrix algebra, but it retains exactly the regular elliptic ones. Its representations therefore offer a compact setting in which to study part of the spectrum of \(\mathrm{GL}_2\). We prove the local Jacquet–Langlands correspondence over every nonarchimedean local field and over \(\mathbb R\), with its elliptic character sign, twisted factors, formal degrees and smooth transfer. We then prove the global quaternion correspondence over \(\mathbb Q\) by a trace comparison, including quotient volumes, singular and continuous terms, residual characters and multiplicities. The calculations at levels eleven and thirty-seven connect the correspondence to explicit weight-two eigenforms. Section 6 states the distinct higher-degree extensions and their remaining proof scope.

We use Lesson 17 for quaternion groups and Brandt operators, Lesson 18 for their trace formula, and Lesson 15 for multiplicity one. A discrete series means an irreducible **unitary** representation square-integrable modulo the centre. Removing the unitary condition requires the term *essentially discrete series*: a character twist of a discrete series. At a finite place the discrete series of \(\mathrm{GL}_2\) are unitary Steinberg twists and unitary supercuspidals. At a real place they are the discrete series described in Lesson 11.

## 1. Match classes by their quadratic polynomial

Let \(F\) be a nonarchimedean local field, or \(\mathbb R\), and let \(D\) be the quaternion division algebra over \(F\). Set \(G=\mathrm{GL}_2(F)\), \(G'=D^\times\). An element of \(G\) is regular elliptic when its characteristic polynomial is separable and irreducible over \(F\). For \(b\in D\), use the reduced polynomial
\[
P_b(T)=T^2-\operatorname{trd}(b)T+\operatorname{nrd}(b).
\tag{1.1}
\]
Regular means that this polynomial has distinct roots over an algebraic closure. In positive characteristic, irreducibility alone does not ensure separability.

We import two algebraic facts. Every separable quadratic extension of a nonarchimedean local field embeds in its quaternion division algebra, by the quadratic-embedding lemma in Lesson 18, Section 5; it uses the written finite splitting criterion and the local Brauer invariant and degree-two restriction rule proved in Brauer groups of local and global fields, Theorem 24.2. The original reference is Voight, Corollary 13.4.5. Over \(\mathbb R\) this is the embedding \(\mathbb C\subset\mathbb H\). Any two embeddings of the same quadratic field are conjugate by an invertible element, by Skolem–Noether [NOE-HYP-04, Theorem 2.1]. The centralizer of that field in a quaternion algebra is the field itself [NOE-HYP-04, Theorem 3.1].

**Theorem 1.1 — the matching bijection.** Equality of characteristic polynomials gives a bijection
\[
\{\text{regular elliptic classes in }G\}
\longleftrightarrow
\{\text{regular classes in }G'\}.
\tag{1.2}
\]
For a matched pair \(g,b\), both centralizers identify with \(K^\times\), where \(K=F[T]/(P_g)\). Moreover \(\det g=\operatorname{nrd}b\) and \(\operatorname{tr}g=\operatorname{trd}b\).

**Proof.** Write a separable irreducible polynomial as \(P(T)=T^2-tT+n\). Its constant term is nonzero. If \(g\) has this polynomial, then for every nonzero \(v\in F^2\), the vectors \(v,gv\) are independent: dependence would give an eigenvalue in \(F\). In this basis, Cayley–Hamilton gives
\[
g\sim\begin{pmatrix}0&-n\\1&t\end{pmatrix}.
\tag{1.3}
\]
Thus \(P\) determines exactly one matrix class, and every such \(P\) occurs.

Embed \(K=F[T]/(P)\) in \(D\), and let \(b\) be the image of \(T\). Its minimal polynomial has degree two and divides (1.1), so (1.1) equals \(P\). Different embeddings give conjugate elements by Skolem–Noether. Conversely, if a noncentral regular \(b\in D\) had a reducible reduced polynomial, its distinct linear factors would satisfy
\((b-r)(b-s)=0\). A division algebra has no zero divisors; hence \(b=r\) or \(b=s\), a contradiction. Therefore its polynomial is irreducible, and \(F[b]\) is a separable quadratic field. Two elements with the same polynomial define two embeddings of the same \(K\); Skolem–Noether conjugates one to the other.

Finally a matrix commuting with \(g\) is determined by its value on \(v\) in the cyclic basis \(v,gv\). Every such value is \((a+cg)v\), so its algebra centralizer is \(F[g]\). The quaternion centralizer is \(F[b]\) by the stated double-centralizer theorem. Taking units gives the assertion about group centralizers. The trace and norm identities are the coefficients of the common polynomial. \(\square\)

The matching includes the two conjugate generators of \(K\): its nontrivial automorphism extends by Skolem–Noether to conjugation in \(D\). There is no extra choice of a root in (1.2).

For measures, choose corresponding Haar measures on the centralizers \(K^\times\), and compatible group and quotient measures. The regular orbital integral is
\[
O_g(f)=\int_{G_g\backslash G}f(x^{-1}gx)\,dx.
\tag{1.4}
\]
One may multiply it by the square root of the Weyl discriminant. That discriminant is the same for matched pairs: both adjoint actions have the same two nontrivial eigenvalue ratios. Thus matching the normalized integrals or the integrals (1.4) amounts to the same condition, once the measures are paired.

The **test-function transfer theorem**, proved below at both finite and real places, says that a smooth Hecke test \(f'\) on \(D^\times\) has a test \(f\) on \(G\) whose regular elliptic orbital integrals match those of \(f'\), and whose regular split orbital integrals vanish. Transfer determines orbital integrals, rather than a unique function. Theorem 2.10 proves its existence over every nonarchimedean local field by explicit orbital coordinates, and Lemma 2.11 proves the scalar-value constraint for every matching pair. Theorem 2.22 proves the real construction and scalar identity, and Corollary 2.31 gives finite spectral transfer. Arthur, §25, Theorem 25.1(a), is a broader reference. Equation (1.2) supplies the regular classes on which to impose the conditions.

## 2. The local representation theorem and its sign

For an admissible representation \(\pi\), its character distribution is
\[
f\longmapsto\operatorname{tr}\pi(f),\qquad
\pi(f)=\int f(g)\pi(g)\,dg.
\tag{2.1}
\]
At finite places Theorem 2.7 below proves, in either characteristic and every residue characteristic, that on the regular set (2.1) is integration against a conjugation-invariant locally constant function \(\Theta_\pi\). Proposition 2.8 gives the finite elliptic compact-type sum, and the division-side argument following it proves the ordinary trace statement for \(D^\times\). These results suffice for the regular character tests below. For real discrete series, Lemma 2.4 below proves the representing character function on the regular elliptic set directly from the disk model. Arthur, Theorem 25.1(b), is the broader real transfer reference.

**Theorem 2.1 — local Jacquet–Langlands.** Fix a unitary central character \(\omega:F^\times\to\mathbb C^\times\). There is a unique bijection
\[
\operatorname{JL}_F:
\operatorname{Irr}_\omega(D^\times)
\xrightarrow{\ \sim\ }
\operatorname{DS}_\omega(\mathrm{GL}_2(F))
\tag{2.2}
\]
characterized by
\[
\Theta_{\operatorname{JL}_F(\tau)}(g)
=-\Theta_\tau(b)
\qquad(g\leftrightarrow b\text{ regular elliptic}).
\tag{2.3}
\]
Here the source consists of irreducible unitary smooth representations at finite places, and irreducible unitary representations at the real place. The central character is preserved. Twisting is compatible:
\[
\operatorname{JL}_F\bigl(\tau\otimes(\chi\circ\operatorname{nrd})\bigr)
=\operatorname{JL}_F(\tau)\otimes(\chi\circ\det).
\tag{2.4}
\]
Unitary \(\chi\) keeps (2.2) within discrete series. Allowing arbitrary smooth quasicharacters gives the corresponding bijection onto essentially discrete series.

Theorem 2.14 and Corollary 2.15 below prove the entire depth-zero local correspondence and all determinant/norm twists of that family, in every residue characteristic. Theorem 2.16 also proves the formal degree of every compact-induction model, and Proposition 2.18 computes both positive-level subgroup volumes in every residue characteristic. Sections 2.8–2.10 construct all positive-level images and prove the character identity, paired dimensions and bijection. Lemma 2.27 gives character integration through the singular set. For nonarchimedean \(F\) of characteristic zero, the exact references are Jacquet–Langlands, Theorem 15.1 and Proposition 15.5; Deligne, §3.2.8 gives the same sign and paired formal-degree normalization. Badulescu, Theorem 1.1 supplies the positive-characteristic theorem, including all residue characteristics. Arthur, Theorem 25.1(b) gives the tempered inner-form formulation, including the real place.

At a finite place, the one-dimensional cases are
\[
\chi\circ\operatorname{nrd}
\longmapsto\mathrm{St}\otimes(\chi\circ\det).
\tag{2.5}
\]
In particular the trivial representation transfers to \(\mathrm{St}\). Higher-dimensional representations transfer to supercuspidals: the remaining discrete series are supercuspidal by Lesson 7, and (2.5) accounts for every special representation. This is a correspondence of isomorphism classes; it is not an identification of representation spaces or of dimensions.

At the real place, write \(\mathbb H^\times=\mathbb R_{>0}\mathrm{SU}(2)\). With trivial positive central character, let \(\tau_m\) restrict to \(\operatorname{Sym}^m(\mathbb C^2)\), \(m\ge0\). Then
\[
\tau_m\longmapsto D_{m+2}.
\tag{2.6}
\]
The right side is the discrete series for the **full** group \(\mathrm{GL}_2(\mathbb R)\). On the positive-determinant component it contains the holomorphic and antiholomorphic ladders; negative determinant exchanges them. The common value on \(-1\) is \((-1)^m=(-1)^{m+2}\), and positive central twists must also agree. Thus the real trivial representation transfers to weight-two discrete series, rather than to the finite-place representation in (2.5).

For example, on \(b=\cos\theta+i\sin\theta\), \(0<\theta<\pi\), the \(\mathrm{SU}(2)\) weights give
\[
\Theta_{\tau_m}(b)
=\sum_{j=0}^{m}e^{i(m-2j)\theta}
=\frac{\sin((m+1)\theta)}{\sin\theta}.
\tag{2.7}
\]
The character of \(D_{m+2}\) on the matching rotation is proved directly to be the negative of (2.7) in Theorem 2.5; it is not inferred from (2.3). There is no quaternion division algebra at a complex place.

### 2.1. Prove the trivial/Steinberg case directly

**Proposition 2.2.** For nonarchimedean \(F\),
\[
\Theta_{\mathrm{St}}(g)=-1
\qquad(g\text{ regular elliptic}).
\tag{2.8}
\]

**Proof.** The unnormalized induced representation \(M=C^\infty(\mathbb P^1(F))\) has the exact sequence
\[
0\longrightarrow\mathbf1\longrightarrow M
\longrightarrow\mathrm{St}\longrightarrow0.
\tag{2.9}
\]
This is the exceptional induction sequence proved in Lesson 7, Theorem 4.2. An elliptic element fixes no point of \(\mathbb P^1(F)\): a fixed line would give an eigenvalue in \(F\).

Let \(f\) have compact support \(S\) contained in the regular elliptic set. Put \(X=\mathbb P^1(F)\). The compact set
\[
\{(x,gx):x\in X,\ g\in S\}\subset X\times X
\]
is disjoint from the diagonal. For each \(x\), choose a sufficiently small compact open neighborhood \(U_x\) so that no \(g\in S\) takes a point of \(U_x\) into \(U_x\). Such a neighborhood exists: otherwise successively smaller neighborhoods and compactness of \(S\) give a limit \(g\) fixing \(x\). A finite subcover, refined by all intersections and differences, gives a finite compact open partition with that same exclusion property.

Choose a compact open subgroup \(K\) for which \(f\) is bi-invariant and which preserves every cell of this partition. To obtain the latter condition, continuity of the action and compactness of each cell give a neighborhood of the identity preserving that cell; intersect the finitely many neighborhoods and choose a compact open subgroup inside. The \(K\)-orbits in \(X\) are open because \(K\) is open in the transitive group \(G\), and there are finitely many because \(X\) is compact. They refine the partition.

The image of \(M(f)\) lies in \(M^K\). In its basis of orbit indicators, a diagonal entry, evaluated at a representative \(x_i\) of its orbit \(C_i\), is
\[
\int_G f(g)1_{C_i}(g^{-1}x_i)\,dg=0.
\]
Indeed \(g^{-1}x_i\in C_i\) would put a point and its image under \(g\) in the same partition cell. Hence \(\operatorname{tr}M(f)=0\). Taking \(K\)-invariants is exact by compact averaging, so traces add in (2.9). On constants the trace is \(\int f\). Therefore
\[
\operatorname{tr}\mathrm{St}(f)=-\int_G f(g)\,dg.
\]
The character function is locally constant on the regular set. Testing on arbitrarily small compact open neighborhoods of each elliptic regular element proves (2.8). The trivial character of \(D^\times\) is one, so this proves (2.3) for the trivial representation without assuming the full correspondence. \(\square\)

### 2.2. Prove the real correspondence from the disk model

The real case of Theorem 2.1 can be proved within the models of Lesson 11, without assuming a character-transfer theorem. We give the square-integrability exclusion as well as the character calculation: constructing some discrete series would not by itself prove surjectivity.

**Lemma 2.3 — the real square-integrable list.** Among the irreducible admissible unitary representations of the full real group, the square-integrable representations modulo the centre are precisely
\[
D_k\otimes|\det|^{i\lambda/2},\qquad k\ge2,\quad\lambda\in\mathbb R.
\tag{2.10}
\]
Here a positive scalar \(aI\) acts as \(a^{i\lambda}\), and \(-I\) acts as \((-1)^k\).

**Proof.** Lesson 11, Sections 3 and 4, proves the admissible classification, the unitary list and its Hilbert models. Its disk calculation proves that every fixed pair of monomials in \(D_k^+\) has coefficient bounded by a constant times \(\cosh(u/2)^{-k}\) on the Cartan element
\(a_u=\operatorname{diag}(e^{u/2},e^{-u/2})\), \(u\ge0\). The radial Haar density modulo the centre is a constant times \(\sinh u\,du\). Consequently these coefficients are square-integrable for \(k>1\). The same calculation proves that \(D_1\) has no nonzero square-integrable coefficient. We must still exclude the principal and complementary series in the unitary list.

Use the compact induced model (3.1) of Lesson 11, with its parameter \(s\) and its parity \(\epsilon\). A central unitary twist does not change the absolute value of a coefficient modulo the centre. Select the weight \(n=0\) for even parity and \(n=1\) for odd parity, and normalize its vector to norm one. Since distinct compact weights are orthogonal in every invariant Hilbert norm, its diagonal coefficient is the \(n\)-th Fourier coefficient in the compact model, including for the complementary series.

Put \(c=\cosh(u/2)\) and \(r=\tanh(u/2)\). The bottom row of \(r_\theta a_u\) is
\((-e^{u/2}\sin\theta,e^{-u/2}\cos\theta)\). Its squared length is
\[
D=e^u\sin^2\theta+e^{-u}\cos^2\theta
=c^2|1-r e^{2i\theta}|^2.
\]
The compact angle \(\phi\) in its upper-triangular-times-rotation decomposition satisfies
\[
e^{i(\phi-\theta)}
=\frac{1-r e^{-2i\theta}}{|1-r e^{2i\theta}|}.
\]
Inserting this and the factor \(D^{-(1+s)/2}\) from normalized induction gives the coefficient
\[
\begin{aligned}
\varphi_n(s,u)
&=\frac{c^{-1-s}}{2\pi}\int_0^{2\pi}
(1-r e^{2i\theta})^{-(1+s+n)/2}
(1-r e^{-2i\theta})^{-(1+s-n)/2}\,d\theta\\
&=c^{-1-s}\,{}_2F_1\left(\frac{1+s+n}{2},
\frac{1+s-n}{2};1;r^2\right).
\end{aligned}
\tag{2.11}
\]
The branches in the integral are the power-series branches at \(r=0\). For \(r<1\), both binomial series converge absolutely and uniformly in \(\theta\); integrating selects their equal exponents. This proves the second equality directly from
\({}_2F_1(a,b;1;x)=\sum_{j\ge0}(a)_j(b)_j x^j/(j!)^2\).

We record the continuation needed at \(r=1\), with its derivation. This series solves
\[
x(1-x)y''+[1-(a+b+1)x]y'-ab y=0.
\]
When \(a+b=1+s\) and \(s\notin\mathbb Z\), its two solutions at \(x=1\), normalized by their leading terms, are
\[
{}_2F_1(a,b;1+s;1-x),\qquad
(1-x)^{-s}{}_2F_1(1-a,1-b;1-s;1-x).
\]
Substitution verifies the differential equation, and their distinct exponents make them independent. Their coefficients in the solution normalized at zero are
\[
A=\frac{\Gamma(-s)}{\Gamma(1-a)\Gamma(1-b)},
\qquad B=\frac{\Gamma(s)}{\Gamma(a)\Gamma(b)}.
\tag{2.12}
\]
Here is a way to establish these constants, rather than assume a connection formula. Expanding \((1-xt)^{-a}\) in the beta integral gives
\[
{}_2F_1(a,b;1;x)
=\frac{1}{\Gamma(b)\Gamma(1-b)}
\int_0^1 t^{b-1}(1-t)^{-b}(1-xt)^{-a}\,dt
\]
first for \(0<\Re b<1\). If \(\Re(1-a-b)>0\), its value at \(x=1\) is the beta integral
\(\Gamma(1-a-b)/(\Gamma(1-a)\Gamma(1-b))\). Absolute convergence of the defining series at one extends this value holomorphically throughout that half-space in \((a,b)\). It gives \(A\) when \(\Re s<0\), since the second local solution then tends to zero. Substitution in the differential equation and uniqueness of its analytic solution at zero also give Euler's transformation
\[
{}_2F_1(a,b;1;x)=(1-x)^{-s}
{}_2F_1(1-a,1-b;1;x).
\]
The same value-at-one argument applied to the right side gives \(B\) when \(\Re s>0\). The coefficients of the two local solutions depend meromorphically on the parameters: this follows by solving the two-by-two system of their values and derivatives at any interior point. Analytic continuation therefore proves both expressions (2.12) for every nonintegral \(s\). This also covers \(n=1\), where an Euler integral with the original parameters alone would not cover both half-planes.

Since \(1-r^2=c^{-2}=4e^{-u}(1+O(e^{-u}))\), equations (2.11)–(2.12), and the power series of the local solutions, now give
\[
\varphi_n(s,u)=e^{-u/2}\left(C_n(s)e^{-su/2}
+C_n(-s)e^{su/2}\right)
+O\left(e^{-(3-|\Re s|)u/2}\right),
\tag{2.13}
\]
for fixed nonintegral \(s\), where the gamma duplication identity simplifies the constants to
\[
C_0(s)=\frac{\Gamma(-s/2)}{\sqrt\pi\,\Gamma((1-s)/2)},
\qquad
C_1(s)=\frac{\Gamma((1-s)/2)}{\sqrt\pi\,\Gamma(1-s/2)}.
\tag{2.14}
\]
All error estimates here are ordinary convergent-series estimates at \(1-r^2=0\); no boundary interchange in (2.11) is needed.

For a principal series, \(s=it\), \(t\ne0\). The gamma function has no zeros, and none of the arguments in (2.14) is a pole; equivalently this follows from the Euler product for \(1/\Gamma\). Thus both coefficients are nonzero. They are complex conjugates. The integral over \([0,T]\) of the squared absolute value of
\(C_n(it)e^{-itu/2}+C_n(-it)e^{itu/2}\)
 equals \(2|C_n(it)|^2T+O(1)\). Multiplying (2.13) squared by \(\sinh u\) changes this by an integrable error and a factor tending to \(1/2\). The coefficient is not square-integrable.

At \(s=0\) in even parity, the poles \(C_0(s)=-2/(\pi s)+O(1)\) and \(C_0(-s)=2/(\pi s)+O(1)\) coalesce. Taking the limit in the convergent local expansions gives
\[
\varphi_0(0,u)=e^{-u/2}\left(\frac{2u}{\pi}+O(1)\right).
\tag{2.15}
\]
Indeed the pole parts in (2.13) combine as
\(4\sinh(su/2)/(\pi s)\); subsequent series terms are bounded by \(O((1+u)e^{-u})\) inside the parentheses. This coefficient is again not square-integrable. Odd parity at \(s=0\) is \(D_1\), already excluded by the disk calculation.

For a complementary series choose \(0<s<1\), using the equivalence of the parameters \(s\) and \(-s\) proved in Lesson 11. It has even parity. The coefficient of the slower term in (2.13) is
\[
C_0(-s)=\frac{\Gamma(s/2)}{\sqrt\pi\,\Gamma((1+s)/2)}>0.
\]
Thus \(|\varphi_0(s,u)|^2\sinh u\) grows as a positive constant times \(e^{su}\). A unitary finite-dimensional member of the real list is one-dimensional, and its coefficient has constant absolute value; the group modulo the centre has infinite volume, so it too is excluded.

For completeness, a nonintegrable coefficient of the chosen compact weight excludes the existence of *any* nonzero square-integrable coefficient. In an irreducible unitary representation every nonzero vector is cyclic. If \(\langle\pi(g)v,w\rangle\) were a nonzero square-integrable coefficient, choose translates of \(v,w\) whose projections onto the selected one-dimensional compact weight are nonzero. Such translates exist by cyclicity. The two compact projections express the new coefficient as left and right compact averages of translates of the old one. These operations preserve \(L^2\) by Minkowski's inequality. The new coefficient is a nonzero scalar multiple of \(\varphi_n\), contradicting the calculations above. For the full group, translates may use either component; its compact weight spaces are still one-dimensional in the principal and complementary models. The Haar integral on the positive component already diverges. Together with the full unitary list of Lesson 11, this proves (2.10). \(\square\)

**Lemma 2.4 — the disk trace on the elliptic set.** Write \(D_k^+\), \(k\ge2\), for the positive ladder on \(\mathrm{SL}_2(\mathbb R)\), with rotation weights \(k+2j\), \(j\ge0\). On its regular elliptic set the character distribution is represented by the smooth function which, at a rotation, is
\[
\Theta_k^+(r_\theta)=\frac{e^{ik\theta}}{1-e^{2i\theta}},
\qquad\theta\notin\pi\mathbb Z.
\tag{2.16}
\]
The negative ladder has the same formula with \(\theta\) replaced by \(-\theta\).

**Proof.** We use precisely the disk Hilbert space and inverse-pullback action constructed in Lesson 11, Section 4.1. Its orthonormal basis and action are
\[
e_j(z)=\sqrt{\frac{(k)_j}{j!}}z^j,\qquad
\sigma_k(g)f(z)=j_g(z)^{-k}f(\phi_g(z)),
\]
where \(\phi_g\) is the disk automorphism associated with \(g^{-1}\) and \(j_g(z)\) is its linear denominator. The multiplier has no zero or pole in the disk. For \(0<r<1\), the dilation operator
\[
R_r e_j=r^j e_j,\qquad (R_r f)(z)=f(rz),
\qquad \|R_r\|_1=(1-r)^{-1}
\tag{2.17}
\]
is trace class. In particular \(R_r\sigma_k(g)\) is trace class. It is weighted composition with
\(\Psi_{r,g}(z)=\phi_g(rz)\) and weight \(w_{r,g}(z)=j_g(rz)^{-k}\).

The map \(\Psi_{r,g}\) has a unique fixed point \(z_{r,g}\) in the disk. To see this, use the complete hyperbolic disk metric. A disk automorphism is an isometry, whereas multiplication by \(r\) has hyperbolic differential norm
\[
\frac{r(1-|z|^2)}{1-r^2|z|^2}\le r<1.
\]
The contraction theorem gives the fixed point. Conjugate weighted composition by a unitary disk automorphism taking that fixed point to zero. The new symbol fixes zero, its derivative there is \(\Psi_{r,g}'(z_{r,g})\), and its new weight at zero is \(w_{r,g}(z_{r,g})\); the conjugating multipliers cancel at a fixed point. The diagonal coefficient on \(e_j\) is therefore
\(w_{r,g}(z_{r,g})\Psi_{r,g}'(z_{r,g})^j\). Trace invariance under unitary conjugacy and the absolute convergence of a trace-class diagonal give
\[
\operatorname{tr}(R_r\sigma_k(g))
=\frac{j_g(rz_{r,g})^{-k}}
{1-r\phi_g'(rz_{r,g})}.
\tag{2.18}
\]
The denominator is nonzero since the fixed-point derivative has absolute value at most \(r\).

If \(g\) is regular elliptic, \(\phi_g\) has an interior fixed point \(z_g\) and its derivative there differs from one. The implicit function theorem applied to
\(z-\phi_g(rz)=0\) proves that \(z_{r,g}\) tends to \(z_g\) smoothly as \(r\uparrow1\), uniformly when \(g\) ranges over a compact subset of the regular elliptic set. Uniqueness of the contraction fixed point identifies this local solution with \(z_{r,g}\). Thus (2.18) has a uniform smooth limit on each such compact subset. Conjugating \(g\) to \(r_\theta\) computes this limit: at zero its multiplier is \(e^{ik\theta}\), and its symbol derivative is \(e^{2i\theta}\). The limiting expression is conjugation invariant because a conjugating multiplier again cancels at the fixed point. This proves the candidate function (2.16).

It remains to identify the limit with the character distribution, rather than a merely formal sum of weights. For \(f\in C_c^\infty(\mathrm{SL}_2(\mathbb R))\), integrating by parts in the left and right rotation variables gives, for every \(N\),
\[
|\langle\sigma_k(f)e_j,e_i\rangle|
\le C_{f,N}(k+2i)^{-N}(k+2j)^{-N}.
\tag{2.19}
\]
The constant can be taken to be the \(L^1\)-norm of the corresponding derivatives of \(f\): coefficients of unitary operators between unit vectors are at most one. For \(N>1\) the matrix entries are absolutely summable. Its sum of rank-one matrix operators converges in trace norm and agrees with \(\sigma_k(f)\) on all basis vectors. Hence \(\sigma_k(f)\) is trace class.

The bounded operators \(R_r\) tend strongly to the identity and have norm at most one. Finite-rank approximation of a trace-class operator then gives
\(\|R_r\sigma_k(f)-\sigma_k(f)\|_1\to0\). For each fixed \(r<1\), the trace-class bound in (2.17) permits integration of (2.18) against \(f\). If the support of \(f\) is regular elliptic, its uniform limit just proved gives
\[
\operatorname{tr}\sigma_k(f)
=\lim_{r\uparrow1}\int f(g)\operatorname{tr}(R_r\sigma_k(g))\,dg
=\int f(g)\Theta_k^+(g)\,dg.
\tag{2.20}
\]
This proves the assertion as a distribution on the entire regular elliptic set. Complex conjugation gives the negative ladder. \(\square\)

**Theorem 2.5 — real local Jacquet–Langlands, proved.** The real case of (2.2)–(2.4) is the unique map
\[
a^{i\lambda}\operatorname{Sym}^m(\mathbb C^2)
\longmapsto D_{m+2}\otimes|\det|^{i\lambda/2},
\qquad a>0,\quad m\ge0.
\tag{2.21}
\]
In particular it includes every real discrete series in the stated admissible category, with both ladders for the full group.

**Proof.** An irreducible unitary representation of a compact group is finite-dimensional: averaging a rank-one orthogonal projection over the group gives a nonzero positive compact operator commuting with the representation; a positive eigenspace is finite-dimensional and invariant, hence is the entire irreducible representation. Norm continuity of the translated rank-one projections makes this average a compact operator, and its trace is one, so it is nonzero. The positive scalar group in \(\mathbb H^\times\) acts by a character, by the unitary Schur lemma. Its \(\mathrm{SU}(2)\) restriction is irreducible, since that character is scalar.

For clarity, the compact classification used here follows from the finite-dimensional \(\mathfrak{sl}_2\) calculation. Choose a highest-weight vector \(v\) of weight \(m\). Then
\(EF^jv=j(m-j+1)F^{j-1}v\). If \(F^Nv\ne0\) and \(F^{N+1}v=0\), this identity forces \(m=N\ge0\); the span of these vectors is invariant and hence is the whole representation. It is \(\operatorname{Sym}^m(\mathbb C^2)\), with weights \(m,m-2,\ldots,-m\). A connected group representation is determined by its derivative, so this also identifies the \(\mathrm{SU}(2)\) representation. Its value at \(-1\) is \((-1)^m\).

Lemma 2.3 now makes (2.21) a bijection preserving the entire central character. For a matching elliptic pair, remove its positive scalar \(a\) and conjugate its unit part to \(\cos\theta+i\sin\theta\), or to the matching rotation. By Lemma 2.4 and the two-ladder decomposition in Lesson 11,
\[
\begin{aligned}
\Theta_{D_k}(r_\theta)
&=\frac{e^{ik\theta}}{1-e^{2i\theta}}
+\frac{e^{-ik\theta}}{1-e^{-2i\theta}}\\
&=-\frac{\sin((k-1)\theta)}{\sin\theta}
=-\sum_{j=0}^{k-2}e^{i(k-2-2j)\theta}.
\end{aligned}
\tag{2.22}
\]
The same integration-by-parts proof gives trace-class test operators on the full real group, using its two sets of compact weights. On the negative-determinant component the representation exchanges the ladders, so the smoothed diagonal trace is zero; on the positive component it is the sum used in (2.22). A positive scalar multiplies the character by \(a^{i\lambda}\). Equation (2.22) is exactly the negative of (2.7) with \(m=k-2\), as required. The distinct Laurent polynomials in (2.22) show uniqueness among the discrete series with the fixed positive central character.

Twisting on either side multiplies the matched character by the same value \(\chi(\operatorname{nrd}b)=\chi(\det g)\). A sign determinant twist is isomorphic on the full two-ladder representation, as proved in Lesson 11, and \(\operatorname{nrd}\) on \(\mathbb H^\times\) is positive. This proves (2.4), and arbitrary quasicharacter twists give the essentially discrete-series extension. \(\square\)

![The weights in the real correspondence, shown for m=2 and k=4.](figures/real-jl.png)

*Figure 1.* For \(m=2\), the compact character has weights \(-2,0,2\), whereas \(D_4\) has the two infinite ladders starting at \(\pm4\). Equation (2.17) makes their traces convergent before passing to the limit. Equation (2.22), for \(0<\theta<\pi\), leaves the negative of the three compact weights. The displayed ladders are truncated schematically; the trace identity is exact. The mechanism and analytic justification are Lemma 2.4 and Theorem 2.5, using the disk action proved in Lesson 11, Section 4.1. A human-source comparison for that realization is Gazeau–del Olmo–Pejhan, [Section II, equations (8)–(9)](https://arxiv.org/html/2504.03901v1), with \(2\eta=k\); their opposite rotation convention must be reversed when comparing their equation (22).

The real formal degrees can also be compared with explicit measures. Give each component of \(G/Z\) the Cartan integration formula with probability measures on its two compact angular variables and radial density \(\sinh u\,du\). Give the compact group \(\mathbb H^\times/\mathbb R^\times\) volume \(2\). For a unit vector of lowest positive weight in \(D_k\), the coefficient on \(a_u\) is \(\cosh(u/2)^{-k}\) and it is zero on the other component. Hence
\[
\int_{G/Z}|\langle D_k(g)v,v\rangle|^2\,dg
=\int_0^\infty\sinh u\,\cosh(u/2)^{-2k}\,du
=2\int_1^\infty x^{-k}\,dx=\frac{2}{k-1}.
\tag{2.23}
\]
This does give the formal degree, rather than just one coefficient norm. Define the coefficient map \(T\) into the centrally covariant \(L^2(G/Z)\) space on its maximal domain, consisting of vectors whose coefficients are square-integrable. This domain contains the dense finite-weight vectors. The map is closed: an \(L^2\)-convergent sequence has an almost-everywhere convergent subsequence, whereas convergence of the input vectors gives pointwise convergence of their coefficients. Its domain is invariant under the group, because translation preserves the coefficient norm, and the closed map intertwines the unitary actions. The spectral projections of its positive operator \(T^*T\) commute with the irreducible representation, so it is scalar; the norm of the coefficient in (2.23) determines that scalar. Inversion of \(g\) exchanges the two vectors in the absolute-square integral, giving the same constant times the squared norm of an arbitrary second vector. This proves the full Schur orthogonality constant. On the compact quaternion quotient the finite-dimensional Schur average gives coefficient norm \(2/(m+1)\). Thus these explicit measures give
\[
d(D_k)=\frac{k-1}{2}=d(\operatorname{Sym}^{k-2}\mathbb C^2).
\tag{2.24}
\]
This calculation concerns formal degrees. At finite places Lemma 2.11 below proves the identity-value relation for every matching pair of tests. Its real counterpart remains the scalar-germ transfer input in Section 3.2.

### 2.3. Prove the finite-place character theorem on the regular set

We now prove the regular-set character statement used in (2.1), for every nonarchimedean local field, including residue characteristic two and positive characteristic. This proof concerns the restriction of the distribution to the regular set. Section 2.4 separately proves smooth orbital transfer and the scalar orbital germ. It does not identify the character distribution globally across the singular set.

Write \(\mathcal O\) for the valuation ring, \(\mathfrak p=(\varpi)\), and \(v(\varpi)=1\). The lattice tree \(\mathcal T\) has vertices the homothety classes of rank-two \(\mathcal O\)-lattices in \(F^2\). Two vertices are adjacent if representatives satisfy
\(\varpi L\subset L'\subset L\), with \(L'/\varpi L\) a line over the residue field. Each vertex has \(q+1\) neighbors. The metric is the number of edges in a path, rather than a Euclidean metric on a drawing.

Here are the elementary tree facts we will use. Elementary divisors, proved by the row and column elimination in Lesson 6, equation (5.4), put any pair of vertices in the form
\([\mathcal O^2]\), \([\mathcal O\varpi^N e_1+\mathcal Oe_2]\), \(N\ge0\). Their path consists of the intermediate exponents. At a vertex other than the initial one, reduction of the elementary-divisor basis modulo \(\mathfrak p\) identifies exactly one neighbor whose distance to the initial vertex decreases; the other \(q\) increase it. Induction gives the unique path, so the graph is a locally finite tree. Its ends are \(\mathbb P^1(F)\): a ray starting at \([\mathcal O^2]\) specifies compatible primitive line data modulo every \(\mathfrak p^N\), and completeness gives its unique limiting line. Conversely a primitive vector on a line gives these data and a ray. The usual action of \(G\) on the ends is the action on lines; it is continuous. The tree with its ends is compact after adjoining the ends: a sequence escaping every finite ball has a subsequence with each finite initial path fixed, by a diagonal selection in the finite branching tree.

For a vertex \(x=[L]\), and an integer \(m\ge1\), set
\[
U_x(m)=1+\mathfrak p^m\operatorname{End}_{\mathcal O}(L),
\qquad e_x=\frac{1_{U_x(m)}}{\operatorname{vol}U_x(m)},
\qquad V_x=e_xV.
\tag{2.25}
\]
The order, group and average do not depend on the representative of the homothety class. We use the same symbol \(e_x\) for the convolution operator on a representation. For an edge \(a=\{x,z\}\), put \(e_a=e_xe_z\) and \(V_a=e_aV\).

**Lemma 2.6 — the exact tree complex and its finite projection.** For any smooth representation, the averages at adjacent vertices commute. If \(z\) is the first neighbor of \(x\) on the path to \(y\ne x\), then
\[
e_xe_z=e_ze_x,\qquad e_xe_ze_y=e_xe_y.
\tag{2.26}
\]
For a finite subtree \(\Sigma\), the operator
\[
u_\Sigma=\sum_{x\in\Sigma^{(0)}}e_x
-\sum_{a\in\Sigma^{(1)}}e_a
\tag{2.27}
\]
is an idempotent with image \(S_\Sigma=\sum_{x\in\Sigma^{(0)}}V_x\), and acts as the identity on that image. With an arbitrary orientation for each edge, the sequence
\[
0\longrightarrow\bigoplus_{a\in\Sigma^{(1)}}V_a
\xrightarrow{\partial}\bigoplus_{x\in\Sigma^{(0)}}V_x
\xrightarrow{\mathrm{sum}}S_\Sigma\longrightarrow0
\tag{2.28}
\]
is exact. The edge boundary is its inclusion at the terminal vertex minus its inclusion at the initial vertex. If an irreducible smooth representation has \(V_{x_0}\ne0\), the sum of all \(V_x\) is the entire representation.

**Proof.** Conjugate a pair and its path to
\(x=[\mathcal O^2]\), \(z=[t_1\mathcal O^2]\), \(y=[t_N\mathcal O^2]\), where \(t_j=\operatorname{diag}(\varpi^j,1)\) and \(N\ge1\). In this basis \(U_z(m)\) has diagonal entries in \(1+\mathfrak p^m\), upper entries in \(\mathfrak p^{m+1}\), and lower entries in \(\mathfrak p^{m-1}\). It is contained in \(\mathrm{GL}_2(\mathcal O)\), so it normalizes \(U_x(m)\). Conversely \(t_1^{-1}U_x(m)t_1\) is integral, so \(U_x(m)\) normalizes \(U_z(m)\). Their product is therefore a compact subgroup, and either order of averaging is its normalized average. Its fixed space is \(V_x\cap V_z\), which proves the first identity and the assertion about \(V_a\).

Gaussian elimination in \(U_z(m)\) factors an element into upper root, diagonal and lower root elements with precisely those entry bounds. The upper root and diagonal elements lie in \(U_x(m)\); the lower root lies in \(U_y(m)\), because \(\mathfrak p^{m-1}\subset\mathfrak p^{m-N}\). The first two act trivially on \(e_xe_yV\). The last also acts trivially there: it normalizes \(U_x(m)\), so commutes with \(e_x\), and it acts trivially on \(e_yV\). Thus \(e_ze_xe_y=e_xe_y\). The adjacent commutation gives the second identity in (2.26). These arguments are identities of compact averaging operators and do not assume unitarity. Inverting the compact measures gives the reversed identity \(e_ye_ze_x=e_ye_x\).

Prove (2.27) by adding a leaf \(x\), with neighbor \(z\), to a smaller subtree \(\Sigma'\). Put \(p_x=e_x(1-e_z)\). Adjacent commutation makes \(p_x\) an idempotent. For every vertex \(y\in\Sigma'\), equation (2.26) gives \(p_xe_y=e_yp_x=0\), and the same holds with each edge average of \(\Sigma'\). Hence \(u_{\Sigma'}p_x=p_xu_{\Sigma'}=0\) and
\(u_\Sigma=u_{\Sigma'}+p_x\) is an idempotent. It is the identity on every old \(V_y\). On \(V_x\), use \(e_xe_zV\subset V_z\), where \(u_{\Sigma'}\) is the identity, and \(u_{\Sigma'}p_x=0\), to obtain \(u_\Sigma e_x=e_x\). Every summand in (2.27) has image in \(S_\Sigma\), proving the claimed image. This starts with a one-vertex tree.

For exactness, suppose finitely many vertex vectors sum to zero. At a leaf \(x\), apply \(p_x\) to this sum; every other vertex term is killed, so \(p_xv_x=0\). Thus \(v_x=e_zv_x\in V_x\cap V_z=V_a\). Subtract the boundary of this edge vector, with the appropriate sign, to remove the leaf term and transfer it to \(z\). Repeat on the smaller tree. This proves exactness in the middle. An edge cycle is zero by inspecting a leaf, where its unique incident edge vector must vanish, and then removing the leaf. Surjectivity is the definition of \(S_\Sigma\). Finally a nonzero \(V_{x_0}\) generates an irreducible representation; its translates lie in the corresponding \(V_{gx_0}\). \(\square\)

Every irreducible smooth representation permits an \(m\ge1\) with \(V_{[\mathcal O^2]}\ne0\), by smoothness of a nonzero vector. Admissibility, proved in Lesson 6, Theorem 5.4, makes all the vertex and edge spaces finite-dimensional. We fix such an \(m\) from now on. For a general coefficient-system comparison, see Meyer–Solleveld, Definition 2.1, Lemma 2.6 and Theorem 2.12. The rank-two group identities and leaf proof needed here have just been supplied explicitly.

**Theorem 2.7 — finite-place regular characters, proved.** For every irreducible smooth complex representation \(\pi\) of \(\mathrm{GL}_2(F)\), the character distribution on the regular set is integration against a unique conjugation-invariant locally constant function \(\Theta_\pi\). This holds in either characteristic, with no restriction on residue characteristic.

**Proof.** First consider an element compact modulo the centre. It fixes a vertex or an edge midpoint of \(\mathcal T\). For split eigenvalues of equal absolute value this follows by scaling them to units in a diagonal basis. For an irreducible quadratic polynomial, its field \(E=F[g]\) has the integral lattice \(\mathcal O_E\). Multiplication by a unit preserves that lattice; if the ramification index is two, an element of odd \(E\)-valuation instead exchanges the lattice classes of \(\mathcal O_E\) and \(\mathfrak p_E\). Scaling by \(F^\times\) reduces the valuation to these cases. This is also the compact-adjoint criterion of Lesson 10, Lemma 7.1.

Choose a fixed point \(c\) that is a vertex or an edge midpoint, and let \(C=G_c\) be its stabilizer. This is an open subgroup, compact modulo the centre. Finite balls \(\Sigma_N\) about \(c\), including their edges, are invariant under \(C\). If \(f\) is a compactly supported smooth function in \(C\), its operator has finite rank by admissibility. Its image lies in some \(S_{\Sigma_{N_0}}\), because Lemma 2.6 exhausts \(V\). For \(N\ge N_0\), the exact finite sequence (2.28) is equivariant for \(C\); traces add along it. Therefore
\[
\begin{aligned}
\operatorname{tr}\pi(f)&=\int_C f(h)\,T_N(h)\,dh,\\
T_N(h)&=\sum_{\substack{x\in\Sigma_N^{(0)}\\hx=x}}
\operatorname{tr}(\pi(h)|_{V_x})
-\sum_{\substack{a\in\Sigma_N^{(1)}\\ha=a}}
\varepsilon(h,a)\operatorname{tr}(\pi(h)|_{V_a}).
\end{aligned}
\tag{2.29}
\]
Here \(\varepsilon(h,a)=1\) if both endpoints are fixed and \(-1\) if they are exchanged. An edge orientation contributes that sign to the chain action. For a cell moved to a different cell the diagonal block on the direct sum is zero. This proves (2.29) without a character theorem. The threshold \(N_0\) may initially depend on \(f\).

For a regular elliptic \(g\), the set of its fixed vertices and edges is finite. Otherwise their geometric fixed-point set contains a ray, since it is convex in a locally finite tree; its end would be an \(F\)-eigenline. Such a line cannot exist for an elliptic element. This fixed-cell set is uniformly bounded on a neighborhood of \(g\). Indeed, if \(g_j\to g\) fixed cells escaping every finite ball, a subsequence of their centres would converge to an end \(\ell\). Continuity of the action on the tree and its ends gives \(g\ell=\ell\), again an eigenline. This reasoning also applies to inverted edges, by using their midpoints. A neighborhood of \(g\) consists of elliptic elements: the set of matrices fixing a line is closed, since \(\mathbb P^1(F)\) is compact. Shrink it to be regular as well and to lie in \(C\).

Within the resulting bounded ball, further shrinking makes the permutation of all cells constant and makes every relevant finite-dimensional matrix trace constant. For the latter, \(g^{-1}h\) may be taken in all the finitely many compact groups \(U_x(m)\) involved, so acts trivially on their fixed spaces; edge spaces are subspaces of their endpoint spaces. Thus for all sufficiently large \(N\), \(T_N\) is the same locally constant finite sum on this neighborhood. Equation (2.29), applied to arbitrary tests there, proves the character assertion at \(g\).

Compact split elements require more care: their fixed set is infinite, and an unqualified infinite vertex sum is not a character formula. After conjugation and a scalar translation, let
\(g=\operatorname{diag}(a,b)\), \(a,b\in\mathcal O^\times\), \(a\ne b\). Put \(\delta=a/b\) and \(r=v(\delta-1)\ge0\). Let \(A\) be the diagonal apartment, with vertices
\(A_n=[\mathcal O\varpi^ne_1+\mathcal Oe_2]\), \(n\in\mathbb Z\).

Every vertex has a unique presentation
\[
L(n,x)=\mathcal O\varpi^ne_1+\mathcal O(e_2+xe_1),
\qquad x\in F/\mathfrak p^n.
\]
To obtain it, scale the projection of a lattice to the second coordinate to \(\mathcal O\); its intersection with the first coordinate is \(\mathfrak p^ne_1\), and a lift of \(e_2\) gives \(x\) modulo that ideal. For \(x=0\), this is \(A_n\). Otherwise choose its representative with \(v(x)=l<n\). The successive lattices \(L(j,x)\), \(l\le j\le n\), give its path from \(A_l\), with the first step off the apartment. The two apartment directions at \(A_l\) are the coordinate lines, whereas this first step has both coordinates nonzero after scaling. Thus its distance from \(A\) is \(d=n-l\). Direct multiplication shows
\[
gL(n,x)=L(n,x)
\ \Longleftrightarrow\ (\delta-1)x\in\mathfrak p^n
\ \Longleftrightarrow\ d\le r.
\tag{2.30}
\]
Its fixed vertices are exactly the tube of radius \(r\) about \(A\); its fixed edges have both endpoints in that tube. There is no edge inversion, since the determinant valuation is even.

Consider \(t=\operatorname{diag}(1+u,1+w)\), with \(u,w\in\mathfrak p^M\), \(M\ge m+r\). In the basis \(\varpi^ne_1,e_2+xe_1\), its only off-diagonal entry is
\((u-w)x\varpi^{-n}\), of valuation at least \(M-d\). Consequently \(t\in U_{L(n,x)}(m)\) for every vertex fixed by \(g\), and it is the identity on every corresponding edge space too. Require also \(M>r\). For all sufficiently small changes \(a',b'\) of the two eigenvalues, their ratio has the same \(r\), and \(\operatorname{diag}(a',b')=gt\) with such a \(t\). Equations (2.29)–(2.30) therefore give
\[
T_N(\operatorname{diag}(a',b'))=T_N(g)
\qquad\text{for every }N.
\tag{2.31}
\]
The use of \(M\ge m+r\) is uniform along the infinite apartment.

Every sufficiently near matrix \(h\) is conjugate to such a diagonal matrix by an element of \(\mathrm{GL}_2(\mathcal O)\) near the identity. For completeness, write its monic characteristic polynomial as \(P\). Near \(a\), choose a radius \(\rho<|a-b|\) and shrink the matrix perturbation so that \(|P(a)|\le\rho|P'(a)|\) and \(|P'(a)|=|a-b|\). The equation for a root \(a+z\) is \(z=-P(a)/P'(a)-z^2/P'(a)\). On \(|z|\le\rho\) this map preserves the ball and strictly contracts it. Successive approximation gives a unique root there; the same argument near \(b\) gives the other root. Taking \(\rho\) arbitrarily small proves their continuous dependence. The projectors
\((h-b')/(a'-b')\) and \((h-a')/(b'-a')\), applied to \(e_1,e_2\), then give an eigenbasis near the original one. This argument divides by \(a'-b'\), never by two, so it works in characteristic two. Conjugating by an integral element preserves every ball about \(A_0\) and transports all the fixed-vector spaces. Hence (2.31) holds on one neighborhood \(U\) of \(g\) in \(C=G_{A_0}\), for every \(N\).

Choose a test \(f_0\) supported in \(U\), with integral one. Equation (2.29) gives \(T_N(g)=\operatorname{tr}\pi(f_0)\) for all sufficiently large \(N\). Thus these constants stabilize, and do so uniformly on \(U\). For any other test \(f\) supported there, take \(N\) larger than both its finite-image threshold and the threshold for \(f_0\). Then (2.29) is the claimed integration against the same constant on \(U\). This establishes local constancy and the distributional identity at every compact split regular element, rather than only convergence of an averaged expression.

It remains to treat split elements with unequal absolute values. Supercuspidals have zero character distribution on a neighborhood of each such element by Lesson 10, Theorem 7.3. By the classification in Lesson 7, the other irreducibles are principal series, Steinberg twists and determinant characters. We supply the principal-series calculation on the entire regular set.

In the chart with representative \(\overline n(x)=\begin{pmatrix}1&0\\x&1\end{pmatrix}\) for the row line \((x,1)\), a normalized induced representation \(I(\mu_1,\mu_2)\) acts by weighted composition. For \(h=\begin{pmatrix}A&B\\C&D\end{pmatrix}\), put
\[
\phi_h(x)=\frac{Ax+C}{Bx+D},\qquad
w_h(x)=\mu_1\left(\frac{\det h}{Bx+D}\right)
\mu_2(Bx+D)\left|\frac{\det h}{(Bx+D)^2}\right|^{1/2}.
\tag{2.32}
\]
These formulas follow by multiplying \(\overline n(x)h\) and performing its upper-triangular-times-\(\overline n\) decomposition. Other charts give the same induced line bundle, with their usual transition multipliers.

A compactly supported smooth group test gives a locally constant integral kernel on each pair of small projective charts. To see this directly, in (2.32) use \(y=\phi_h(x)\) and
\(C=(Bx+D)y-Ax\) as a group coordinate. With additive measures, Haar measure is a constant times
\(|\det h|^{-2}\,dA\,dB\,dC\,dD\), and \(dC=|Bx+D|\,dy\). On a sufficiently small chart the denominator is nonzero and bounded away from zero over the compact group support. The resulting integrand is locally constant in \((x,y)\), uniformly over a compact parameter set. Integrating in \((A,B,D)\) gives the claimed kernel. Finitely many such charts cover \(\mathbb P^1(F)\). Refining their clopen partitions makes the kernel constant on each pair of cells; the matrix trace is therefore its diagonal integral, since each diagonal entry is the diagonal kernel value times the measure of its cell.

Near \(g=\operatorname{diag}(a,b)\), \(a\ne b\), only its two fixed projective points can contribute to that diagonal trace. On the compact complement of small neighborhoods of those points, \(g\) fixes no line, and the same exclusion holds for all sufficiently near \(h\). In the chart near zero the diagonal condition is
\(C=Bx^2+(D-A)x\). Its derivative in \(x\) is \(D-A+2Bx\), of fixed nonzero absolute value on a sufficiently small neighborhood. Here the change of variables can be checked without a general inverse function theorem. Choose the ball about zero with radius \(\rho\) so that \(|B|\rho<|D-A|\). On it the equation \(C=(D-A)x+Bx^2\) is solved by the strict contraction \(x=C/(D-A)-Bx^2/(D-A)\). Differences satisfy \(|C(x)-C(y)|=|D-A|\,|x-y|\); successive approximation proves bijectivity onto the ball of radius \(|D-A|\rho\), and this exact scaling of subballs proves the Jacobian. Thus \(x\) is a unique coordinate for the corresponding \(C\)-ball. The Jacobian in the diagonal integral is consequently
\[
\frac{|Bx+D|}{|D-A+2Bx|}
=\frac{1}{|1-\phi_h'(x)|},
\tag{2.33}
\]
since at a fixed point \(\phi_h'(x)=(A-Bx)/(D+Bx)\). All these substitutions are in compact chart integrals. They remain valid in characteristic two, where the derivative term \(2Bx\) is simply zero. The chart at infinity gives the other fixed point. The two fixed-point multipliers and derivatives for the diagonal matrix are
\(\mu_1(a)\mu_2(b)|a/b|^{1/2},a/b\) and
\(\mu_1(b)\mu_2(a)|b/a|^{1/2},b/a\). Thus
\[
\Theta_{I(\mu_1,\mu_2)}(\operatorname{diag}(a,b))
=\frac{\mu_1(a)\mu_2(b)+\mu_1(b)\mu_2(a)}
{|1-a/b|^{1/2}|1-b/a|^{1/2}}.
\tag{2.34}
\]
The same local eigenbasis argument as before proves that this function represents the distribution on a neighborhood, and is locally constant there. On the elliptic set there is no fixed projective point, so the diagonal kernel is zero and the principal-series character is zero.

Taking traces in the exact induced sequence (2.9), which is exact on every compact fixed space, gives the remaining explicit characters. In particular
\[
\begin{aligned}
\Theta_{\chi\circ\det}(h)&=\chi(\det h),\\
\Theta_{\mathrm{St}\otimes(\chi\circ\det)}(\operatorname{diag}(a,b))
&=\chi(ab)\left(\frac{|a|+|b|}{|a-b|}-1\right),\\
\Theta_{\mathrm{St}\otimes(\chi\circ\det)}(h)
&=-\chi(\det h)\qquad(h\text{ regular elliptic}).
\end{aligned}
\tag{2.35}
\]
These expressions and supercuspidal support handle every noncompact split element. They also agree with the compact argument by uniqueness of a representing function: testing on arbitrarily small open sets identifies any two locally constant representatives. Conjugation invariance of the character distribution then gives conjugation invariance of the unique function. This proves the theorem on the entire regular set. \(\square\)

![The exact fixed tube for diag(3,1) in a radius-two ball of the Q2 lattice tree.](figures/finite-character-tree.png)

*Figure 2.* This is the complete ball of radius two about \(A_0\) in the \(q=2\) lattice tree. For \(g=\operatorname{diag}(3,1)\) over \(\mathbb Q_2\), \(r=v_2(3-1)=1\). The blue vertices are exactly those fixed by \(g\) in the displayed ball, by (2.30); the two gray depth-two vertices are exchanged. The apartment extends in both directions beyond the drawing. Distances count edges. For the trivial coefficient system the trace is \(8-7=1\), the fixed vertices minus the fixed edges in (2.29). For general representations their finite-dimensional traces replace these ones. The fixed-set calculation and the uniform bound \(M\ge m+r\), together with admissibility, are the mechanism of Theorem 2.7. For the general coefficient-system method, compare Meyer–Solleveld, Theorem 2.12 and Proposition 4.1; the illustration is independently drawn.

**Proposition 2.8 — the finite elliptic compact-type character sum.** Let
\(\pi=\mathrm{c\!-\!Ind}_J^G\tau\), where \(J\) is open, contains the centre and is compact modulo the centre, and \(\tau\) is finite-dimensional. Assume \(\pi\) is irreducible. For a regular elliptic element \(g\),
\[
\Theta_\pi(g)=\sum_{\substack{Jx\in J\backslash G\\xgx^{-1}\in J}}
\operatorname{tr}\tau(xgx^{-1}).
\tag{2.36}
\]
The sum is finite and is uniformly a finite sum on a neighborhood of \(g\). Every supercuspidal has this description by Lesson 10, Theorem 7.8, including residue characteristic two.

**Proof.** The compact group \(J/Z\) has a finite orbit on the vertices of the locally finite tree. The convex hull of that orbit is finite; its centre is a vertex or edge midpoint fixed by all of \(J\). Call it \(c_J\). The index \([G_{c_J}:J]\) is finite, since \(J\) is open and both groups contain \(Z\), while \(G_{c_J}/Z\) is compact.

If \(xgx^{-1}\in J\), then \(g\) fixes \(x^{-1}c_J\). The fixed vertices and edge midpoints for an elliptic element are finite and uniformly bounded on a neighborhood, as proved in Theorem 2.7. For each possible point, the fibre of
\(Jx\mapsto x^{-1}c_J\) has at most \([G_{c_J}:J]\) elements: after selecting one \(x\) it is a translate of \(J\backslash G_{c_J}\). This proves both finiteness assertions. Membership in the open subgroup \(J\) and the finite-dimensional smooth trace of \(\tau\) are locally constant for this finite list.

The compact-induction space is the algebraic direct sum of copies of the space of \(\tau\), indexed by \(J\backslash G\). Right translation by \(h\) has a diagonal block at \(Jx\) exactly when \(xhx^{-1}\in J\), and that block is \(\tau(xhx^{-1})\). For a test supported in the chosen elliptic neighborhood only the uniformly finite list can contribute. Its integrated operator has finite rank by admissibility, so its trace is the integral of that finite diagonal sum. This is (2.36), identified with Theorem 2.7's representative. \(\square\)

On the division side no infinite-dimensional character analysis is needed. If a smooth irreducible representation of \(D^\times\) has a scalar central character, choose a nonzero vector fixed by an open subgroup \(U\). Compactness of \(D^\times/F^\times\) makes \(F^\times\backslash D^\times/U\) finite, so the orbit of that vector spans a finite-dimensional space. Irreducibility makes it the whole space. A common open stabilizer of a finite basis makes its ordinary trace function locally constant on all of \(D^\times\), and integrating its matrices gives its character distribution. This proves the division-side regular character statement too.

### 2.4. Construct finite-place transferred tests and their scalar values

We prove smooth test transfer over every nonarchimedean local field. The construction includes characteristic two. It uses an Euler test for the scalar part and an explicit orbital-coordinate lift for the remainder; no character correspondence or density theorem enters it. In the orbital-coordinate construction, elliptic means that the quadratic polynomial is irreducible; the calculations also cover inseparable nonscalar classes. The correspondence itself uses the separable regular elliptic classes.

Put \(H=G/Z\), \(H'=D^\times/F^\times\), and normalize the common central Haar measure by \(\operatorname{vol}\mathcal O^\times=1\). For \(H\), give a vertex stabilizer \(K\) of the lattice tree volume one. Let \(I\) fix the two endpoints of an edge, and let \(J\) be its full setwise stabilizer. The edge orientation character is \(\epsilon:J\to\{1,-1\}\). A representative \(\begin{pmatrix}0&\varpi\\1&0\end{pmatrix}\) exchanges the endpoints; its square is scalar. Since \(K/I\) has \(q+1\) elements,
\[
\begin{gathered}
\operatorname{vol}I=\frac1{q+1},\qquad
\operatorname{vol}J=\frac2{q+1},\qquad
\operatorname{vol}H'=\frac2{q-1},\\
f_{\rm EP}=\frac{1_K}{\operatorname{vol}K}
-\frac{\epsilon\,1_J}{\operatorname{vol}J},\qquad
e'=\frac1{\operatorname{vol}H'},\qquad
f_{\rm EP}(1)=-\frac{q-1}{2}=-e'(1).
\end{gathered}
\tag{2.37}
\]
The two functions in this display are on the projective groups. A class-invariant cutoff below will give compactly supported functions on the full groups.

These group measures are paired by the reduced trace convention. With additive measure of volume one on \(\mathcal O\), the split measure is
\(\kappa|\det x|^{-2}d^4x\), where
\(\kappa=((1-q^{-1})(1-q^{-2}))^{-1}\). Indeed the additive volume of \(\mathrm{GL}_2(\mathcal O)\) is \((1-q^{-1})(1-q^{-2})\). In the quaternion model of Lesson 17, equation (1.2), the trace pairing on
\(\mathcal O_L\oplus\mathcal O_Lj\) has one perfect quadratic block and one block multiplied by \(\varpi\). Its four-dimensional determinant has valuation two. Thus additive self-dual measure for that pairing gives \(\mathcal O_D\) volume \(q^{-1}\). This is the block calculation of Lesson 17, Section 4, and works over any residue field. The unit fraction is \(1-q^{-2}\), because the residue field of \(\mathcal O_D\) has \(q^2\) elements. Consequently the paired measure
\(\kappa|\operatorname{nrd}x|^{-2}dx\) gives \(\mathcal O_D^\times\) volume \(1/(q-1)\). Its projective image has index two in \(H'\), by the valuation parity in Lesson 17, proving the volume in (2.37). Equivalently, these formulas specify the measures directly.

**Lemma 2.9 — the Euler orbital integrals.** Pair the centralizer measures under the polynomial matching. If \(T\) is an elliptic centralizer, write \(v_T=\operatorname{vol}(T/Z)\), with that measure. Then
\[
O_g(f_{\rm EP})=\frac1{v_T}=O_b(e')
\quad(g\leftrightarrow b),\qquad
O_g(f_{\rm EP})=0\quad(g\text{ split regular}).
\tag{2.38}
\]
The quotients defining these orbital integrals are unchanged when the common centre is removed.

**Proof.** Right compact cosets for a vertex stabilizer are the vertices. Decomposing its orbital integral into \(T\)-orbits gives, for each vertex fixed by \(g\), the weight \(1/\operatorname{vol}(T_x/Z)\). For the signed edge function the analogous weight is
\(\epsilon(g,a)/\operatorname{vol}(T_a/Z)\). This follows directly by integrating over the double coset \(T xK\), or \(T xJ\): its quotient volume is the compact subgroup volume divided by the centralizer stabilizer volume, and the normalized test cancels the former.

For elliptic \(g\) the invariant cells form a finite set by Theorem 2.7. Since \(T/Z\) is compact, an orbit of size \(d\) has weight \(d/v_T\). Their signed Euler sum is one. If vertices are fixed, they and their connecting edges form a nonempty finite tree, with one more vertex than edge. If no vertex is fixed, \(g\) exchanges the endpoints of its unique fixed edge; that edge contributes \(0-(-1)=1\). There cannot be two such edges, since their connecting path would force a fixed vertex. These are all cases, because \(g\) fixes a vertex or midpoint. Thus the first integral is \(1/v_T\). On \(H'\) the constant test gives
\(\operatorname{vol}(H')/(\operatorname{vol}(H')v_T)=1/v_T\).

A split element with unequal eigenvalue absolute values fixes no vertex or midpoint and meets neither support. For a compact split element the fixed vertices are the tube of radius \(r=v(a/b-1)\) about its apartment, by (2.30). Its split centralizer \(T/Z\) preserves the apartment ends and acts transitively on its vertices and on its edges. Both stabilizers are the same compact unit subgroup \(T_0\); these two orbital weights cancel. Every vertex off the apartment has a unique parent toward it. Sending that vertex to its parent edge is a \(T\)-equivariant bijection between the off-apartment fixed vertices and edges, with equal stabilizers and equal weights. These cancel too. There are only finitely many orbits: a fundamental apartment vertex has finitely many branches of depth at most \(r\). Hence the argument is a finite cancellation, not subtraction of divergent orbital integrals. The split centralizer never inverts an apartment edge, and an edge off the apartment has its parent distinguished; all signs here are positive. This proves the second assertion. \(\square\)

We next prove the lift away from scalars. For a monic irreducible quadratic polynomial \(P(X)=X^2-tX+n\), including an inseparable one in characteristic two, put
\[
S(t,n)=\begin{pmatrix}0&-n\\1&t\end{pmatrix},\qquad
M(t,n;A,C)=
\begin{pmatrix}
A&(tA-A^2-n)/C\\ C&t-A
\end{pmatrix}\quad(C\ne0).
\tag{2.39}
\]
Every matrix with this polynomial has \(C\ne0\), since an upper triangular matrix would give a root in \(F\). Thus \((A,C)\in F\times F^\times\) parameterizes its entire orbit.

Use on its centralizer \(E^\times\), \(E=F[S]\), Haar measure
\(|N(\alpha+\beta S)|^{-1}d\alpha\,d\beta\), and use the identical measure under the quaternion embedding. No division by the discriminant occurs in this choice. The exact orbital formula is
\[
O_{S(t,n)}(f)
=\kappa\int_{F\times F^\times}
f(M(t,n;A,C))\,\frac{dA\,dC}{|C|}.
\tag{2.40}
\]
To verify the measure, every group element has a unique factorization
\(h(\alpha+\beta S)\), \(h=\begin{pmatrix}u&v\\0&1\end{pmatrix}\), \(u\ne0\). Its bottom row determines \(\beta,\alpha\), and this element of \(E\) is nonzero, hence invertible. The multiplication map has additive Jacobian \(|N(\alpha+\beta S)|\), while its determinant is \(uN(\alpha+\beta S)\). Dividing the group Haar measure by the stated centralizer measure leaves
\(\kappa|u|^{-2}du\,dv\). In \(hSh^{-1}\), \(C=1/u\), \(A=v/u\); the change of variables has absolute Jacobian \(|C|^{-3}\), yielding (2.40). These are algebraic identities in either characteristic.

Here is the quaternion-side local constancy needed in that lift. It concerns every nonscalar \(b\), even an inseparable one. The differentials of its trace and norm are
\[
X\longmapsto
\bigl(\operatorname{trd}X,\,
\operatorname{trd}((t-b)X)\bigr).
\tag{2.41}
\]
The reduced trace pairing is nondegenerate: after a splitting extension it is the matrix trace pairing, whose matrix-unit dual bases prove this assertion in every characteristic; nondegeneracy descends. The two linear forms in (2.41) are independent because \(b\) is nonscalar. Select two coordinate directions on which their matrix is invertible, and fix the other two coordinates. The trace-norm map then has a continuous local section \(b(t,n)\). One can prove this assertion directly: after applying the inverse linear matrix, its equations are a linear map plus a quadratic remainder. On a sufficiently small coordinate ball, the difference of the remainder has Lipschitz constant less than one. For parameter changes in the corresponding small ball, solving by successive approximation gives the unique section, continuously. No derivative of a quadratic root and no division by two is used.

The polynomial of a nonscalar quaternion is irreducible. A factorization over \(F\) would give \((b-a)(b-d)=0\), even for a repeated root, and force \(b\) scalar. Irreducibility is open also at an inseparable polynomial: roots of nearby quadratics, if any, lie in a common bounded ball by the quadratic equation; compactness of that ball would give a root of the limiting polynomial. The section can therefore be chosen over a neighborhood consisting entirely of irreducible polynomials.

Each such trace-norm fibre is one quaternion conjugacy class, without a separability restriction. For \(b,c\) with the same nonscalar polynomial, \(x=b+c-t\) satisfies \(xb=cx\); if nonzero it is invertible. If it is zero, use a nonzero commutator \(x=by-yb\), with \(y\) not commuting with \(b\). The polynomial identity gives \(xb+bx=tx\), so again \(xb=cx\). For \(c=b\) one can simply use \(x=1\).

The centralizer is \(F[b]^\times\). After a splitting extension, a nonscalar two-by-two matrix has two-dimensional centralizer by the cyclic-basis calculation. The subalgebra \(F[b]\) already has that dimension, so equality descends. Its projective group is compact. The following explicit volume formula also proves continuous local constancy for the varying centralizer measure:
\[
v_T=(1-q^{-1})\left(
\int_{\mathcal O}\frac{ds}{|1+ts+ns^2|}
+\int_{\mathfrak p}\frac{ds}{|s^2+ts+n|}
\right).
\tag{2.42}
\]
The two projective charts represent \((\alpha,\beta)=(1,s)\), \(s\in\mathcal O\), and \((s,1)\), \(s\in\mathfrak p\); they partition \(\mathbb P^1(F)\). Writing the remaining scalar coordinate as \(z\), additive Jacobian \(|z|\) cancels one of the two norm powers, leaving \(dz/|z|\). The central normalization supplies \(1-q^{-1}\). Since the polynomial is irreducible, both denominators are nonzero on their compact chart domains. Their absolute values are uniformly unchanged by sufficiently small parameter changes. The volume is therefore finite, positive and locally constant, including at an inseparable quadratic.

For a compact smooth test \(f'\), integration over the compact group \(H'\) gives
\[
O_{b(t,n)}(f')
=\frac1{v_T}\int_{H'}f'(x^{-1}b(t,n)x)\,dx.
\tag{2.43}
\]
The integrand is uniformly locally constant in \((t,n)\): cover the compact \(H'\) by finitely many neighborhoods and use smoothness of \(f'\) and continuity of the section. The numerator and (2.42) are locally constant. This proves the required assertion without a regular-character theorem.

If \(f'\) is supported away from the centre, its trace-norm image is a compact set of irreducible polynomials disjoint from the scalar curve. The function \(V(t,n)=O_{b(t,n)}(f')\) just proved is locally constant on the irreducible locus, supported in that compact set. Extend it by zero outside that locus. This extension is a compactly supported smooth function: the compact support lies in an open irreducible neighborhood. Choose \(\phi\in C_c^\infty(F\times F^\times)\) with
\(\kappa\int\phi(A,C)dA\,dC/|C|=1\), and define
\[
f_0\begin{pmatrix}A&B\\C&D_0\end{pmatrix}
=V(A+D_0,AD_0-BC)\phi(A,C)\quad(C\ne0),
\tag{2.44}
\]
and zero otherwise. Its support is compact: \(A,C,t,n\) are bounded and \(C,n\) are bounded away from zero; (2.39) bounds the remaining entries. It is smooth also across \(C=0\), since \(\phi\) is supported away from zero. Formula (2.40) gives precisely \(O_g(f_0)=V(t,n)\). Its split orbital integrals vanish because \(V\) is zero there, and it vanishes at every scalar matrix. For example \(\phi=(1-q^{-2})1_{\mathcal O\times\mathcal O^\times}\) has the required integral with the present \(\kappa\).

**Theorem 2.10 — finite-place smooth transfer, proved.** With the measures above, every \(f'\in C_c^\infty(D^\times)\) has an \(f\in C_c^\infty(G)\) such that
\[
\begin{aligned}
O_g(f)&=O_b(f')&&\text{on matching regular elliptic classes},\\
O_g(f)&=0&&\text{on regular split classes},\\
f(zI)&=-f'(z)&&\text{for every }z\in F^\times.
\end{aligned}
\tag{2.45}
\]
This construction holds for every nonarchimedean local field, in either characteristic.

**Proof.** The scalar curve in the trace-norm plane is
\(z\mapsto(2z,z^2)\), \(z\ne0\). It is closed and is a proper homeomorphism onto its image. For characteristic different from two the first coordinate supplies its inverse; for characteristic two,
\(|z-w|^2=|z^2-w^2|\) supplies continuity of the inverse. Bounds on the nonzero norm give properness. Hence the compact smooth function \(c(z)=f'(z)/e'(1)\) extends to some
\(a\in C_c^\infty(F\times F^\times)\). To see the extension without a general topological theorem, cover the compact scalar support by finitely many compact open parameter neighborhoods on which \(c\) has a single value and which miss scalar points with other values. Refine their overlaps to disjoint compact open pieces. Set that value there and zero elsewhere. Closedness and properness of the scalar curve ensure that these neighborhoods can be chosen compact and avoid its zero-value part.

Pull the projective functions of (2.37) back to the full groups, and put
\[
F'(b)=a(\operatorname{trd}b,\operatorname{nrd}b)e'([b]),
\qquad
F(g)=a(\operatorname{tr}g,\det g)f_{\rm EP}([g]).
\tag{2.46}
\]
Both have compact support. Their projective supports are compact, and the norm cutoff bounds the scalar valuation in both directions; the remaining central units are compact. They are smooth. Multiplication by the class-invariant cutoff preserves (2.38), and (2.37) gives \(F(zI)=-F'(z)\). By construction \(F'(z)=f'(z)\).

The compact smooth remainder \(r'=f'-F'\) vanishes on an open neighborhood of the centre. Its compact support is therefore disjoint from the centre. Apply (2.44) to it, obtaining \(r\) with the matching elliptic integrals, zero split integrals and zero scalar values. Then \(f=F+r\) proves all three identities in (2.45). In characteristic two, the remainder's support may contain nonscalar inseparable elements; (2.41)–(2.43) explicitly include them, so no support has been discarded. \(\square\)

**Lemma 2.11 — the scalar orbital germ and the value of every matching pair.** Fix \(z\in F^\times\), and put \(u_z=\begin{pmatrix}z&0\\1&z\end{pmatrix}\). Continue to use the centralizer measure with basis \(1,g\) from (2.40). For each compact smooth test \(f\), all sufficiently close regular parameters \((t,n)\) to \((2z,z^2)\) satisfy
\[
O_g(f)=O_{u_z}(f)+\Gamma_z(g)f(zI),\qquad
\Gamma_z(g)=
\begin{cases}
0,&g\text{ split},\\
-\operatorname{vol}(H')/v_{G_g},&g\text{ elliptic}.
\end{cases}
\tag{2.47}
\]
The first term is the nontrivial unipotent orbital integral; its coefficient is exactly one in this normalization. In particular, every matching pair with zero regular split orbital integrals satisfies \(f(zI)=-f'(z)\).

**Proof.** First extend (2.40) to every nonscalar cyclic class, including a repeated-root class. The factorization \(G=hF[g]^\times\) used there misses only matrices whose bottom-row norm is zero. For a split or repeated-root quadratic these rows lie in at most two proper linear subspaces and have additive measure zero. This set is right-centralizer invariant; the quotient integration formula therefore gives it orbital measure zero as well. The same Jacobian computation applies on the complement. Thus (2.40) remains valid.

An orbital integral of a compact smooth test supported away from the scalar matrices is locally constant in \((t,n)\), even at a repeated-root parameter. Indeed every nonscalar matrix has a conjugate with lower-left entry nonzero. Cover the compact support by finitely many such fixed conjugate charts, and partition the test by compact open subsets on which that entry is bounded away from zero. In each chart (2.40) integrates a locally constant function over a fixed compact domain in \((A,C)\). Smoothness is uniform there. Conjugation preserves the integral and the centralizer normalization. This proves the assertion also at \(u_z\).

Choose \(m\) large enough that \(U=zI+\mathfrak p^mM_2(\mathcal O)\) lies in \(G\) and \(f\) is constant on \(U\). Multiply by a compact open trace-norm cutoff equal to one near \((2z,z^2)\). The cutoff can be chosen so that all scalar points in its support lie in \(U\), by the proper inverse of the scalar curve used in Theorem 2.10. The remainder after subtracting \(f(zI)1_U\) then has compact support away from all scalars. Its orbital integral is constant near this parameter and equals its value at \(u_z\).

Here is the remaining integral, with all constants visible. Write
\(t=2z+s\), \(n=z^2+zs+d\), and take \(s\in\mathfrak p^m\), \(d\in\mathfrak p^{2m}\). Set \(S=s/\varpi^m\), \(N=d/\varpi^{2m}\). Substituting \(A=z+\varpi^m a\), \(C=\varpi^m c\) into (2.39), membership in \(U\) is equivalent to
\(a,c\in\mathcal O\), \(c\ne0\), and \(v(a^2-Sa+N)\ge v(c)\). Each shell for \(c\) has \(dc/|c|\)-volume \(1-q^{-1}\), while \(dA=q^{-m}da\). Consequently
\[
\begin{aligned}
O_g(1_U)&=\kappa q^{-m}(1-q^{-1})
\int_{\mathcal O}\bigl(1+v(a^2-Sa+N)\bigr)\,da,\\
\Gamma_z(g)&=\kappa q^{-m}(1-q^{-1})
\int_{\mathcal O}\bigl(v(a^2-Sa+N)-2v(a)\bigr)\,da.
\end{aligned}
\tag{2.48}
\]
At \(u_z\) the polynomial is \(a^2\). All these integrals are finite. For an irreducible polynomial its value is nonzero on the compact domain; for split polynomials each linear-factor valuation is integrable. Values at the finitely many zeros do not affect the integrals. The same observations justify summing the shells by monotone integration.

For a nearby split polynomial its two roots \(\alpha,\beta\) lie in \(\mathcal O\). Translation invariance and the residue balls give
\(\int_{\mathcal O}v(a-\alpha)\,da=\sum_{j\ge1}q^{-j}=1/(q-1)\), and likewise for \(\beta\). Thus the second line of (2.48) is zero on split classes, in every characteristic. The germ is independent of an eligible \(m\): the difference of two corresponding indicators vanishes near the centre, so its orbital integral is constant and equals its unipotent value.

To identify the elliptic germ, multiply the projective Euler test by a trace-norm cutoff equal to one near this scalar parameter. Its scalar value is \(-(q-1)/2=-1/\operatorname{vol}(H')\). Its split orbital integrals vanish by Lemma 2.9. The already proved expansion and the split value of the germ force its unipotent integral to be zero. On elliptic classes Lemma 2.9 gives orbital integral \(1/v_{G_g}\). Substitution into the expansion yields exactly the elliptic value in (2.47).

Finally let \(f,f'\) be any matching pair with zero split integrals. The split part of (2.47) forces \(O_{u_z}(f)=0\). Compactness of \(H'\) implies that, for every quaternion \(b\) sufficiently close to \(z\), its entire conjugacy orbit lies in the neighborhood where \(f'\) equals \(f'(z)\). Hence on matching nearby elliptic classes,
\[
-\frac{\operatorname{vol}(H')}{v_{G_g}}f(zI)
=O_g(f)=O_b(f')
=\frac{\operatorname{vol}(H')}{v_{G_g}}f'(z).
\tag{2.49}
\]
There are arbitrarily close such classes: take \(b=z+\varpi^k x\) with a nonscalar integral generator \(x\) of the unramified quadratic subfield. The volume factor is finite and positive, and cancels. This proves the scalar identity for every matching pair. No division by two, separability of the parameter polynomial, or characteristic-zero germ theorem was used. \(\square\)

This is an actual scalar-germ calculation, including the nontrivial unipotent term and the universal scalar-value identity. The representation bijection and global trace comparison remain separate tasks. For a primary comparison of Euler tests in higher rank, see Cohen, Section 8.2.1, Proposition 8.6. The tree proof here uses the full signed edge stabilizer, including inverted edges; it does not restrict the determinant valuation to zero.


**Proposition 2.12 — the special formal degree.** For these paired measures and every unitary \(\chi\),
\[
d\bigl(\mathrm{St}\otimes(\chi\circ\det)\bigr)
=\frac{q-1}{2}
=d(\chi\circ\operatorname{nrd}).
\tag{2.50}
\]

**Proof.** Steinberg unitarity and square-integrability were proved in Lesson 7, Section 7. In its boundary model \(C^\infty(\mathbb P^1(F))/\mathbb C\), an oriented edge \(a\) determines the class \(v_a\) of the indicator of the ends on its terminal side. Reversing orientation gives \(-v_a\); the outward indicators at a vertex sum to the constant one, so their classes sum to zero. The two endpoint-fixing Iwahori orbits on the ends give an invariant space of dimension two before removing constants, hence one after. The full edge stabilizer acts on that line by its orientation sign.

Normalize the vector for a base edge to length one. The stabilizer is transitive on the edges at each distance \(l\ge1\) from it, after allowing endpoint exchange: there are \(2q^l\) such edges. This transitivity can be checked with primitive row coordinates. Fixing a finite initial lattice path, the appropriate upper or lower root subgroup varies the next residue digit arbitrarily; induction reaches each of its \(q\) forward branches. The edge flip exchanges the two initial sides. The outward sum relation at the first endpoint gives coefficient absolute value \(1/q\) on the first sphere. At every subsequent endpoint it gives the preceding coefficient divided by \(q\): the path stabilizer fixes the base vector and permutes its \(q\) forward branches. Orientation may change the sign, but
\(|\langle\mathrm{St}(g)v,v\rangle|=q^{-l}\) when the base edge and its translate have distance \(l\).

Each right \(J\)-coset has volume \(2/(q+1)\). Therefore
\[
\int_H|\langle\mathrm{St}(g)v,v\rangle|^2\,dg
=\frac2{q+1}
\left(1+\sum_{l\ge1}2q^l q^{-2l}\right)
=\frac2{q-1}.
\tag{2.51}
\]
The closed coefficient-map argument accompanying (2.24) applies here unchanged: its dense domain contains the smooth vectors by the proved square-integrability, its positive operator commutes with the irreducible unitary action, and inversion exchanges the vectors. Thus this is the full Schur constant, and its inverse is the formal degree. A unitary twist does not change any absolute coefficient. On the compact quaternion quotient a one-dimensional unitary norm character has constant absolute coefficient one, so its squared norm is \(\operatorname{vol}H'=2/(q-1)\). This proves (2.50). \(\square\)

![Exact Euler orbital-integral examples and the finite-place paired identity values.](figures/finite-test-transfer.png)

*Figure 3.* The examples are over \(\mathbb Q_2\). The elliptic matrix \(\begin{pmatrix}0&2\\1&0\end{pmatrix}\) fixes only the midpoint of its inverted edge: no vertex is fixed, and its orientation sign is \(-1\), giving \(0-(-1)=1\). For \(\operatorname{diag}(3,1)\), the radius-one fixed tube modulo its split centralizer has one apartment vertex, one branch vertex, one apartment loop and one branch edge. All four stabilizer volumes agree in this \(q=2\) example; its Euler sum is \(2-2=0\). The diagram suppresses their common inverse-volume factor. Graph placements are schematic, with edge count as the metric. The actual orbital identities, all-field scalar construction and paired special formal degree are Lemma 2.9, Theorem 2.10, Lemma 2.11 and Proposition 2.12, equations (2.37)–(2.51). Cohen, Section 8.2.1, Proposition 8.6, supplies a human-source comparison for Euler test transfer; no source image is copied.

### 2.5. Prove the depth-zero correspondence and every twist of it

The following argument proves a complete family of the finite local correspondence in every residue characteristic. It includes both the bijection and the negative character identity, rather than just a comparison of dimensions. Theorem 2.30 includes positive-level representations that cannot be reduced to this family by a norm or determinant twist.

Use the local model of Lesson 17, equation (1.2), and write \(\Pi=j\), \(k_2=\mathcal O_L/\mathfrak p_L\), and
\[
U_D^1=1+\Pi\mathcal O_D,\qquad
H_D=F^\times\mathcal O_D^\times,\qquad
K^1=1+\mathfrak pM_2(\mathcal O).
\tag{2.52}
\]
The group \(U_D^1\) is normal in \(D^\times\). The quotient \(\mathcal O_D^\times/U_D^1\) is \(k_2^\times\), conjugation by \(\Pi\) induces \(\lambda\mapsto\lambda^q\), and \(\Pi^2=\varpi\). A division-side representation is called depth zero here if it is trivial on \(U_D^1\); a split-side irreducible is depth zero if it has a nonzero \(K^1\)-fixed vector. These are the concrete depth-zero conditions being compared.

**Lemma 2.13 — every division-side depth-zero representation.** Let \(\theta:k_2^\times\to\mathbb C^\times\) be regular, meaning \(\theta\ne\theta^q\), and let \(A\in\mathbb C^\times\). Extend \(\theta\) to \(H_D\) by
\(\widetilde\theta(\varpi^r u)=A^r\theta(\bar u)\), and put
\(T_{\theta,A}=\operatorname{Ind}_{H_D}^{D^\times}\widetilde\theta\).
It is irreducible of dimension two. Its isomorphism class is determined by \(A\) and the unordered pair \(\{\theta,\theta^q\}\). The other depth-zero irreducibles are exactly \(\chi\circ\operatorname{nrd}\) with \(\chi\) trivial on \(1+\mathfrak p\).

**Proof.** The decomposition defining \(\widetilde\theta\) is unique, since \(v_D(\varpi)=2\), and the residue character already prescribes scalar-unit values. The subgroup \(H_D\) has index two. In the two coset copies, its unit and uniformizer actions can be written
\[
T_{\theta,A}(u)=
\begin{pmatrix}\theta(\bar u)&0\\0&\theta(\bar u^q)\end{pmatrix},
\qquad
T_{\theta,A}(\Pi)=\begin{pmatrix}0&A\\1&0\end{pmatrix}.
\tag{2.53}
\]
The relations above verify this representation directly. Finite-character averaging projects onto its two distinct unit-character lines, and \(\Pi\) exchanges them. Any nonzero invariant subspace therefore contains both lines. The same lines and the central value at \(\varpi\) prove the stated uniqueness.

Conversely, the division-side argument following Proposition 2.8, or Lesson 17, Theorem 1.1, makes an irreducible smooth representation finite-dimensional. If it is trivial on \(U_D^1\), decompose its units under the finite abelian group \(k_2^\times\). The operator \(\Pi\) exchanges Frobenius-related eigenspaces and its square is the central scalar \(A\). Irreducibility leaves one Frobenius orbit. For an orbit of length two, a vector and its \(\Pi\)-translate span a stable two-dimensional space, giving (2.53). For a fixed character, \(\Pi\) acts on one weight space and satisfies \(X^2-A\). Its two distinct nonzero complex roots give an invariant line, so irreducibility forces dimension one.

A Frobenius-fixed character is \(\eta\circ N_{k_2/k}\), by the cyclic finite-field calculation in RT-FIN-17, Lemma 1.1. If its \(\Pi\)-value is \(c\), define the tame character \(\chi\) by \(\chi|_{\mathcal O^\times}=\eta\) on residues and \(\chi(\varpi)=c/\eta(-1)\). Since \(\operatorname{nrd}\Pi=-\varpi\), its norm character has the required values on units and \(\Pi\), hence everywhere. This gives exactly the remaining representations. \(\square\)

Let \(\rho_\theta\) be the finite cuspidal representation of \(\mathrm{GL}_2(k)\), of dimension \(q-1\), whose character values are (5.1) of Lesson 10. Its full construction, including even \(q\), is the exact finite-field prerequisite just linked, Lemma 3.1, equation (13), and Theorems 4.1 and 5.1. Extend its inflation to \(ZK\) with scalar-uniformizer value \(A\), as in Lesson 10, (3.1), and set
\(P_{\theta,A}=\mathrm{c\!-\!Ind}_{ZK}^{G}\widetilde\rho_{\theta,A}\).

**Theorem 2.14 — the complete depth-zero local bijection.** The assignments
\(T_{\theta,A}\mapsto P_{\theta,A}\) and
\(\chi\circ\operatorname{nrd}\mapsto\mathrm{St}\otimes(\chi\circ\det)\)
give a bijection from division-side depth-zero irreducibles onto split-side depth-zero essentially discrete series. They preserve the whole central character and have the negative character relation on every matching regular elliptic class. For unitary representations their formal degrees agree in the paired measures (2.37).

**Proof of construction and exhaustion.** Lesson 10, Theorem 3.1, proves that \(P_{\theta,A}\) is irreducible supercuspidal; its proof uses the finite cuspidal table and unipotent averaging, including \(q=2\). The cross-type Cartan calculation and finite Schur orthogonality distinguish precisely the unordered parameters above. Lemma 7.6 and the level-zero case of Theorem 7.8 there prove that these exhaust the supercuspidals with \(K^1\)-fixed vectors. The whole split-side discrete-series list is Lesson 7's special/supercuspidal list. The special twists with \(K^1\)-invariants are exactly the tame twists: the subgroup \(K^1\cap\mathrm{SL}_2(F)\) acts transitively on each residue ball of \(\mathbb P^1(F)\), using the upper or lower root subgroup with parameter in \(\mathfrak p\). Its invariant space in the boundary model is therefore the \(q+1\) residue indicators modulo constants. The action of \(K^1\) on this space is trivial, so a determinant character can give an invariant only if it kills \(\det K^1=1+\mathfrak p\). Exactness of compact averaging justifies taking this quotient invariant space. This proves exhaustion on both sides. The dimensions separate the norm and regular families on the division side, while special and supercuspidal representations are distinct on the split side. Both regular models have central values \(A\) at \(\varpi\) and \(\theta(a)\) at a residue scalar \(a\).

**Proof of the full elliptic character identity.** Proposition 2.8 identifies the character of the compact induction with the finite sum over fixed vertices: \(ZK\backslash G\) indexes the lattice vertices, and the diagonal block at a fixed vertex is \(\rho_\theta\) of the integral action there. Take a matching pair \(g\leftrightarrow b\). If \(v_D(b)=v_F(\det g)\) is odd, no conjugate of \(g\) lies in \(ZK\), whose determinant valuations are even. The split character is zero. Equation (2.53) makes the division character zero on the odd coset as well.

If the valuation is \(2r\), scale both elements by \(\varpi^{-r}\). Then \(b\) is a unit, and let \(\lambda\in k_2^\times\) be its residue. The common reduced polynomial is integral and has unit norm. On the split side it preserves an integral lattice. Its fixed vertices form a nonempty finite tree by the elliptic fixed-set argument of Theorem 2.7; the even determinant valuation prevents edge inversion. At any fixed vertex, fixed adjacent vertices correspond exactly to eigenlines of the reduction on its two-dimensional residue lattice.

If \(\lambda\notin k\), the residue polynomial is irreducible. There is no such eigenline, so the connected fixed tree is one vertex. The finite character there is \(-\theta(\lambda)-\theta(\lambda^q)\), whereas (2.53) gives its opposite on the division side. If \(\lambda\in k^\times\), every residue action has that repeated eigenvalue. It is either scalar, with all \(q+1\) neighbors fixed, or a nontrivial Jordan block, with exactly one neighbor fixed. Write \(i\) and \(l\) for the numbers of these interior vertices and leaves. Since a finite tree has one fewer edge than vertex,
\[
(q+1)i+l=2(i+l-1),\qquad
(q-1)i-l=-2.
\tag{2.54}
\]
The finite character sum is consequently
\((q-1)i\theta(\lambda)-l\theta(\lambda)=-2\theta(\lambda)\).
On the division side it is \(2\theta(\lambda)\). Restoring the common central factor \(A^r\) proves, in all cases,
\[
\Theta_{P_{\theta,A}}(g)=-\operatorname{tr}T_{\theta,A}(b)
=\begin{cases}
0,&v_D(b)\text{ odd},\\
-A^r\bigl(\theta(\lambda)+\theta(\lambda^q)\bigr),&\lambda\notin k,\\
-2A^r\theta(\lambda),&\lambda\in k^\times.
\end{cases}
\tag{2.55}
\]
Here the last two cases have \(v_D(b)=2r\). This includes arbitrarily deep elliptic elements whose residue is scalar. For the norm characters, Proposition 2.2 supplies the sign, multiplied by the common factor \(\chi(\det g)=\chi(\operatorname{nrd}b)\).

**Proof of formal degrees.** For \(|A|=1\), the finite unitary type gives the invariant sum-of-squares norm on the compact induction. Admissibility and compact averaging make its Hilbert completion irreducible: a nonzero closed invariant subspace has a nonzero averaged vector in a finite-dimensional smooth fixed space, and algebraic irreducibility then gives the whole dense space. Take a unit vector supported on the base coset. Its coefficient is zero off \(ZK\), and on that coset it is the finite type's coefficient. Finite Schur averaging on \(ZK/Z\), of volume one, gives
\[
\int_{G/Z}|\langle P_{\theta,A}(g)v,v\rangle|^2dg
=\frac1{q-1},\qquad
d(P_{\theta,A})=q-1
=\frac{2}{\operatorname{vol}(D^\times/F^\times)}
=d(T_{\theta,A}).
\tag{2.56}
\]
The closed coefficient-map argument of (2.24) makes this the full Schur constant. Division-side finite Schur averaging gives volume divided by dimension, hence the last equality. Proposition 2.12 proves the same equality for all unitary special/norm pairs. \(\square\)

**Corollary 2.15 — every determinant/norm twist of this family.** The depth-zero bijection extends unambiguously to the families of all smooth norm twists on the division side and all smooth determinant twists on the split side. The character sign, central character and twisting identity (2.4) hold throughout these families; unitary twists preserve (2.56).

**Proof.** Multiplication by \(\chi\circ\det\), or \(\chi\circ\operatorname{nrd}\), gives the character and central identities immediately. The point requiring proof is independence of a presentation as a twist. If a twist of a depth-zero compact induction has \(K^1\)-fixed vectors, its support-by-Cartan calculation forces those vectors onto the base coset: at every positive Cartan position the intersection with \(K^1\) contains a full residue unipotent group; its determinant is one and finite cuspidality kills its average. On the base coset the original type is trivial on \(K^1\), so \(\chi\) must kill \(1+\mathfrak p\). Thus the only twists taking a depth-zero supercuspidal to another depth-zero supercuspidal are tame. The boundary argument in Theorem 2.14 gives the same assertion for special representations.

On the division side, the unit norm image satisfies \(\operatorname{nrd}(U_D^1)=1+\mathfrak p\). Containment follows by reducing the norm modulo \(\mathfrak p\). Surjectivity already holds on \(1+\mathfrak p\mathcal O_L\): at each depth \(m\),
\(N(1+\varpi^m x)=1+\varpi^m\operatorname{Tr}(x)\pmod{\mathfrak p^{m+1}}\), and the unramified residue trace is onto. Choose the next digit successively; completeness gives a norm lift of each principal unit. This works in characteristic two as well. Hence a norm twist of a depth-zero representation is depth zero exactly when the twist is tame.

For a tame twist both regular parameters change by the identical rule
\[
(\theta,A)\longmapsto
\bigl(\theta\,\bar\chi\circ N_{k_2/k},\ A\chi(\varpi)^2\bigr).
\tag{2.57}
\]
Frobenius orbits and their uniqueness agree on both sides. Comparing two arbitrary twist presentations and taking their quotient twist reduces to this rule, proving independence and bijectivity of the extended assignment. For norm/special pairs it is simply multiplication of their character parameter; uniqueness follows from the surjectivity of reduced norm and determinant and the special parameter list. The unitary coefficient absolute values are unchanged. \(\square\)

![The complete fixed tree and exact character sum for a depth-zero Q2 Jacquet–Langlands pair.](figures/depth-zero-jl.png)

*Figure 4.* Over \(\mathbb Q_2\), use \(b=1+2\Pi\) and \(g=\begin{pmatrix}1&4\\2&1\end{pmatrix}\), with \(\Pi^2=2\). Their trace and norm are \(2\) and \(-7\). For the regular pair of characters of \(\mathbb F_4^\times\), the finite \(\mathrm{GL}_2(\mathbb F_2)\) type is the one-dimensional sign representation. The two blue interior vertices have scalar reduction, contributing \(+1\) each, and all four gray leaves have nontrivial Jordan reduction, contributing \(-1\) each. The six shown vertices and five edges are the entire fixed tree: each displayed leaf has exactly one fixed neighbor, so no unseen branch continues it. Lattice labels specify actual integral bases up to homothety; Euclidean placements are schematic and distances count edges. The sum \(2-4=-2\) is the negative of the division trace \(2\), and both formal degrees are \(1\). The proof is Lemma 2.13, Theorem 2.14 and Corollary 2.15, (2.52)–(2.57). For human-source comparison see Jacquet–Langlands, Section 15, Proposition 15.5; the finite character construction is compared with Etingof et al., Section 4.24.4, in the exact RT-FIN-17 prerequisite. No source image is copied.

### 2.6. The formal degree of every compact-induction model

Let \(F\) be any nonarchimedean local field, \(G=\mathrm{GL}_2(F)\), \(Z=F^\times\), and normalize Haar measure on \(G/Z\) by \(\operatorname{vol}(ZK/Z)=1\), \(K=\mathrm{GL}_2(\mathcal O_F)\). Let \(J\supseteq Z\) be open and compact modulo \(Z\), and let \(\lambda\) be a finite-dimensional irreducible smooth representation of \(J\), with unitary central character \(\omega\). Assume
\[
\pi=\mathrm{c\!-\!Ind}_J^G\lambda
\]
is irreducible and admissible. These hypotheses are proved for every supercuspidal in Lesson 10, Theorems 2.1 and 7.8. The inducing subgroup may be \(ZK\) or \(E^\times U_{\mathfrak A}^{l}\); it is not restricted to the depth-zero family or odd residue characteristic. Inner products are linear in the first variable.

The representation \(\lambda\) can be made unitary: average any positive definite Hermitian form over \(J/Z\). The integrand is independent of the representative because \(|\omega|=1\); right translation preserves the compact quotient Haar measure. Irreducibility is unchanged.

Put \(d=\dim\lambda\) and \(v_J=\operatorname{vol}(J/Z)\). The Hilbert model is the space of functions \(u:G\to V_\lambda\) with \(u(jg)=\lambda(j)u(g)\) and
\[
\|u\|^2=\sum_{Jx\in J\backslash G}\|u(x)\|^2<\infty.
\]
Right translation is unitary. The finite-support smooth subspace is the original compact induction. Admissibility ensures that its compact-open fixed spaces remain the same finite-dimensional spaces in the completion: averaging the dense smooth subspace has that finite-dimensional closed image. If a nonzero closed invariant subspace exists, sufficiently small compact-open averaging produces a nonzero vector in one of those fixed spaces. Smooth irreducibility then includes the whole dense smooth representation, so the closed subspace is the full Hilbert space. Thus this is an irreducible unitary completion.

**Theorem 2.16 — every compact-induction formal degree.** In the preceding hypotheses, the unitary representation has formal degree \(d_\pi=\dim\lambda/\operatorname{vol}(J/Z)\). In particular this computes the degree of every supercuspidal in Lesson 10, Theorem 7.8, in every residue characteristic.

**Proof.**

For \(w\in V_\lambda\), let \(f_w\) be supported on \(J\), with \(f_w(j)=\lambda(j)w\). Its norm is \(\|w\|\). For any vector \(u\) of the Hilbert model,
\[
\langle\pi(g)u,f_w\rangle=\langle u(g),w\rangle.
\tag{2.58}
\]
Finite-dimensional projective Schur averaging on \(J/Z\) gives
\[
\int_{J/Z}|\langle\lambda(j)a,w\rangle|^2\,dj
=\frac{v_J}{d}\|a\|^2\|w\|^2.
\tag{2.59}
\]
Here conjugation of a rank-one operator by \(\lambda(j)\) is independent of the central representative. Its average commutes with \(\lambda(J)\), hence is scalar by finite-dimensional Schur; its trace supplies exactly \(1/d\). This proves (2.59) and fixes its constant.

The quotient \(G/Z\) is the disjoint union of the open sets \((J/Z)x\). Their measures use the same \(dj\), because \(G/Z\) is unimodular and right translation preserves Haar measure. Applying (2.58) and (2.59), with the sum justified by nonnegative integration, gives for every Hilbert vector \(u\)
\[
\int_{G/Z}|\langle\pi(g)u,f_w\rangle|^2\,dg
=\frac{v_J}{d}\|u\|^2\|w\|^2.
\tag{2.60}
\]
Thus the coefficient map with a base-coset test vector is bounded on the entire completion, with its exact norm. No closed-graph or unbounded-intertwiner assertion is needed.

Let \(z\) now be any finite-support smooth vector. It is a finite sum of translates of base-coset vectors, so
\[
T_z u(g)=\langle\pi(g)u,z\rangle
\]
is a bounded map to the central-character \(L^2\) space, by (2.60) and the triangle inequality. It intertwines right translation. Consequently \(A_z=T_z^*T_z\) commutes with \(\pi(G)\). To justify scalarity directly, \(A_z\) preserves every compact-open fixed space. Choose one nonzero such finite-dimensional space and an eigenvector of \(A_z\) there. The eigenspace on the smooth representation is nonzero and invariant under \(G\), so smooth irreducibility makes it the whole smooth representation. Density and boundedness give \(A_z=c_z I\) on the Hilbert completion.

For a base-coset vector \(f_a\), unitarity and inversion, which preserves Haar measure on \(G/Z\), show
\[
\begin{aligned}
c_z\|a\|^2
&=\int_{G/Z}|\langle\pi(g)f_a,z\rangle|^2\,dg\\
&=\int_{G/Z}|\langle\pi(g)z,f_a\rangle|^2\,dg
=\frac{v_J}{d}\|z\|^2\|a\|^2.
\end{aligned}
\tag{2.61}
\]
Thus \(c_z=(v_J/d)\|z\|^2\). This uniform norm bound extends the coefficient maps continuously from the dense finite-support test vectors to every Hilbert test vector. On compact sets their pointwise coefficients also converge uniformly, by the unitary Cauchy–Schwarz bound, so the extension is the actual coefficient function. Polarizing (2.60)–(2.61) in the two vectors proves the full mixed Schur relation and identifies the positive formal degree as
\[
d_\pi=\frac{\dim\lambda}{\operatorname{vol}(J/Z)}.
\tag{2.62}
\]
All changes of measure are explicit: multiplying \(dg\) by \(c>0\) multiplies \(v_J\) by \(c\) and divides \(d_\pi\) by \(c\).

\(\square\)

**Corollary 2.17 — the paired compact-type degree identity.** For the paired division measure, every unitary division representation has degree \((q-1)\dim T/2\). Thus equality for a proposed compact-induction pair is exactly (2.64) below.

**Proof.**

For every irreducible representation \(T\) of the quaternion division group with unitary central character, Lesson 17, Theorem 1.1 and the same finite-dimensional averaging give
\[
d_T=\frac{\dim T}{\operatorname{vol}(D^\times/Z)}.
\]
In the paired measures (2.37),
\[
\operatorname{vol}(D^\times/Z)=\frac2{q-1},\qquad
d_T=\frac{q-1}{2}\dim T.
\tag{2.63}
\]
Therefore for a proposed positive-level pair \((\mathrm{c\!-\!Ind}_J^G\lambda,T)\), degree equality is exactly the arithmetic identity
\[
2\dim\lambda=(q-1)\operatorname{vol}(J/Z)\dim T.
\tag{2.64}
\]
This equivalence alone does not construct \(T\) or prove its character relation; Theorem 2.30 establishes the bijection and equality for every corresponding pair. For depth zero, \(J=ZK\), \(\dim\lambda=q-1\), and \(\dim T=2\), so it recovers the proved equality \(d_\pi=q-1=d_T\).

Every unitary determinant or norm twist leaves coefficient absolute values unchanged, hence preserves the degrees. If an essentially unitary compact type has nonunitary central character, its absolute value is trivial on scalar units and is determined by the scalar uniformizer. An unramified positive determinant twist can cancel that value, since the determinant of a scalar uniformizer has valuation two. This supplies a unitary representative. Formula (2.62) applies to that representative; it does not attach a positive Hilbert formal degree to a nonunitary realization.

\(\square\)

**Proposition 2.18 — the two positive-level subgroup volumes.** In the compact-induction exhaustion of Lesson 10, Lemmas 7.6–7.7, write \(J=E^\times U_{\mathfrak A}^l\), \(l\ge1\). Use the same normalization \(\operatorname{vol}(ZK/Z)=1\). Then
\[
\begin{array}{c|c|c}
\mathfrak A,E&\operatorname{vol}(J/Z)&d_\pi\\ \hline
M_2(\mathcal O),\ E/F\text{ unramified}
&\dfrac{q^{1-2l}}{q-1}
&(q-1)q^{2l-1}\dim\lambda\\[5pt]
\mathfrak I,\ E/F\text{ ramified}
&\dfrac{2q^{1-l}}{q^2-1}
&\dfrac{(q^2-1)q^{l-1}}2\dim\lambda.
\end{array}
\tag{2.65}
\]
The formulas include residue characteristic two. Theorem 2.30 identifies the dimensions for every corresponding pair without requiring a quadratic-character description of every inducing type.

**Proof.** In the unramified case \(E^\times=F^\times\mathcal O_E^\times\), and \(\mathcal O_E^\times\cap K(l)=1+\mathfrak p_E^l\). The finite reduction map has kernel \(K(l)\), and
\[
|\mathrm{GL}_2(\mathcal O/\mathfrak p^l)|
=q^{4(l-1)}q(q-1)^2(q+1),\qquad
|\mathcal O_E^\times/(1+\mathfrak p_E^l)|
=(q^2-1)q^{2(l-1)}.
\]
Their ratio is \(q^{2l-1}(q-1)\). Scalar units already lie in the embedded torus, so this is precisely the index of \(J/Z\) in \(ZK/Z\). Inverting the index gives the first volume.

In the ramified case let \(I=\mathfrak I^\times\) and \(U_{\mathfrak I}^r=1+\mathfrak P^r\) for \(r\ge1\). The pointwise edge stabilizer \(ZI/Z\) has volume \(1/(q+1)\), since its vertex stabilizer acts transitively on the \(q+1\) adjacent edges. The quotient \(I/U_{\mathfrak I}^1\) is \(k^\times\times k^\times\). Each layer \(U_{\mathfrak I}^r/U_{\mathfrak I}^{r+1}\) has order \(q^2\): the radical of the explicit two-by-two Iwahori order has two entry coordinates at each successive layer, and multiplication modulo the next layer is addition. Hence
\[
[I:U_{\mathfrak I}^l]=(q-1)^2q^{2(l-1)}.
\]
The ramified field has the same lattice chain, so \(\mathcal O_E^\times\cap U_{\mathfrak I}^l=1+\mathfrak p_E^l\), and the torus quotient has order \((q-1)q^{l-1}\). The index of \(\mathcal O_E^\times U_{\mathfrak I}^l\) in \(I\) is therefore \((q-1)q^{l-1}\). The full \(E^\times\) contributes exactly two equal-measure cosets modulo \(F^\times\mathcal O_E^\times\), by its ramification index two. Its odd valuation exchanges the two vertices of the edge, while units preserve them, so these two cosets are distinct in \(G/Z\). Multiplying the unit-subgroup volume by two gives the second volume. Apply (2.62) to both volumes for the degree column. All residue-group and lattice-chain counts work in every characteristic. \(\square\)

### 2.7. Real smooth transfer, including the scalar value

The calculation in Lemma 2.4 was initially made on the regular elliptic set. We now identify the character distribution on arbitrary tests, construct smooth transfers with common compact support, and prove the scalar identity for every matching pair.

First remove the positive unitary central character by the twist in (2.10), and let \(\kappa\in\{0,1\}\) be its parity at \(-I\). Tests transform by \(\omega^{-1}\) under the centre and are compactly supported modulo it. Keep the measures of (2.23)–(2.24): each component of \(G/Z\) has probability compact angular measures and radial density \(\sinh u\,du\); \(D^\times/Z\) has volume \(2\). Give matching compact centralizers \(T/Z\) the same volume \(v_T\). One may set \(v_T=1\); retaining it clarifies the scalar calculation. Restore the positive central twist afterwards.

**Lemma 2.19 — the real character distribution across the singular set.** The ladder characters in Lemma 2.4 are locally integrable on the entire group, and give the trace on every smooth compact test. On \(a_u=\operatorname{diag}(e^{u/2},e^{-u/2})\), \(u>0\), each ladder has character
\[
\Theta_k^\pm(a_u)=\frac{e^{-(k-1)u/2}}{2\sinh(u/2)}.
\tag{2.66}
\]
The elliptic values remain (2.16). A negative scalar multiplies the character by \((-1)^k\). For the full \(D_k\), add the ladders on the positive-determinant component and use zero on the other component.

**Proof.** Use \(R_r\), its fixed point and trace formula (2.17)–(2.19). Write the matrix inducing the inverse disk action as
\[
\begin{pmatrix}a&b\\\bar b&\bar a\end{pmatrix},
\qquad |a|^2-|b|^2=1,\qquad a=x+iy.
\]
The weighted symbol of \(R_r\sigma_k(g)\) comes from this matrix with its first column multiplied by \(r\). At its interior fixed point \(z=z_{r,g}\), put \(\lambda=r\bar b z+\bar a\). The eigenvalues of that matrix are \(\lambda,r/\lambda\). Thus
\[
\begin{aligned}
\lambda^2-(ra+\bar a)\lambda+r&=0,\\
\operatorname{tr}(R_r\sigma_k(g))
&=\frac{\lambda^{1-k}}{\lambda-r/\lambda},\\
\Delta_r&=((1+r)x-i(1-r)y)^2-4r.
\end{aligned}
\tag{2.67}
\]
The fixed-point disk identity gives
\[
|\lambda|^2=\frac{1-r^2|z|^2}{1-|z|^2}\ge1.
\]
Therefore the absolute trace is at most \(|\Delta_r|^{-1/2}\).

Put \(p=1+r,q=1-r,X=x^2,Y=y^2\). Direct expansion gives
\[
|\Delta_r|^2=(p^2X+q^2Y-4r)^2+16rq^2Y.
\tag{2.68}
\]
On a fixed compact set \(Y\le M\), and \(X+Y\ge1\). For \(X\ge1\), the first parenthesis is \(p^2(X-1)+q^2(1+Y)\), so its absolute value is at least \(p^2(X-1)\). For \(X<1\), write \(d=1-X\); then \(Y\ge d\). Either \(q^2(1+Y)\le p^2d/2\), giving absolute value at least \(p^2d/2\) in the first parenthesis, or
\(q^2Y\ge p^2d^2/(2(1+M))\), and the second summand supplies the bound. Uniformly for \(r\ge1/2\),
\[
|\operatorname{tr}(R_r\sigma_k(g))|
\le C_M|x^2-1|^{-1/2}
\tag{2.69}
\]
off a Haar-null set. The constant is independent of \(r\).

This majorant is locally integrable. At a noncentral unipotent element, \(x\) is a submersion coordinate; its transverse inverse square root is integrable. Near either scalar, use \((\Re b,\Im b,y)\) and solve for \(x\) with its fixed sign. The exact identity
\(x^2-1=|b|^2-y^2\) reduces the question to a quadratic cone. In polar coordinates the majorant is
\(\rho^{-1}|Q(\vartheta)|^{-1/2}\), and the volume factor is \(\rho^2\,d\rho\,d\vartheta\). The angular zero set of the nondegenerate quadratic form is smooth on the sphere; its transverse inverse square root is integrable. The radial integral is finite as well.

The elliptic limit was proved in Lemma 2.4. At a split element the fixed point tends to the attracting boundary fixed point and its multiplier tends to \(e^{u/2}\), giving (2.66). Conjugation gives the same split-class value; negative scalars introduce their weight sign. Dominated convergence by (2.69), together with the trace-norm convergence in (2.19)–(2.20), now identifies the distribution on every test. There is no additional singular-supported distribution. Complex conjugation gives the second ladder. On the full group the other component exchanges the ladders and has zero diagonal trace after smoothing too. \(\square\)

The principal trace on arbitrary tests follows directly from the compact induced model of Lesson 11, (3.1). Its smoothed kernel on the circle of real lines is obtained by integrating the test over the stabilizer of a line, and is smooth. Its diagonal integral is the trace. At a regular matrix the diagonal condition selects its two real eigenlines in the split case and none in the elliptic case. The Jacobian at an eigenline is \(|1-t_1/t_2|\), with the half-density already present in normalized induction. Hence
\[
\Theta_{I_\epsilon(s)}(\pm a_u)
=(\pm1)^\epsilon
\frac{e^{su/2}+e^{-su/2}}{2|\sinh(u/2)|},
\qquad u\ne0,
\tag{2.70}
\]
and the character is zero on regular elliptic classes.

There is no omission at repeated eigenvalues in this kernel calculation. Parameterize the stabilizer by its diagonal ratio and unipotent coordinate before taking the line integral. The map from a group element and a line to its image line is a submersion: an infinitesimal lower unipotent moves any line in a suitable affine chart. The diagonal integral is consequently a smooth-kernel integral with no singular-supported term. Changing variables to the eigenline solutions gives (2.70) almost everywhere. In these diagonal-kernel coordinates the repeated-eigenvalue locus has diagonal ratio one, a codimension-one set of measure zero in the line-times-stabilizer integral; its pushforward contributes no singular measure. Absolute convergence is also verified by the quadratic-cone calculation: on a compact set the character is bounded by a constant times the inverse square root of the discriminant. This proves the formula on arbitrary tests. It holds for complex \(s\), since the compact test integral is entire in that parameter. The full-group eigenline calculation on the other component is identical in principle and is supported on split classes there too.

**Lemma 2.20 — the real scalar germ for every matching pair.** If \(f,f'\) have equal orbital integrals on matching regular elliptic classes, and all regular split orbital integrals of \(f\) vanish, then
\[
f'(z)=-f(zI)\qquad(z\in\mathbb R^\times).
\tag{2.71}
\]

**Proof.** Work first at \(1\). In the traceless real algebra choose coordinates with determinant \(z_0^2-x_0^2-y_0^2\), and compact generator \((0,0,1)\). Its full-group conjugates are
\((\sinh u\cos\phi,\sinh u\sin\phi,\pm\cosh u)\). The two signs come from the two components; the quotient measure on either sheet is
\(v_T^{-1}\sinh u\,du\,d\phi/(2\pi)\), by the Cartan normalization.

Denote the angular average of \(f(cI+X)\) by \(F(c,\rho^2,z_0)\), where \(\rho^2=x_0^2+y_0^2\). It is smooth in \(\rho^2\ge0\): at \(\rho=0\), Taylor expansion removes the odd linear term on averaging and bounds the second-derivative remainder; applying the same argument to derivatives gives the smooth radial assertion. A compact smooth extension to a neighborhood of the determinant-one section can be used for these estimates.

For \(s=\sin\theta>0,c=\cos\theta\), change variables \(t=s\cosh u\). This gives exactly
\[
O_{r_\theta}(f)=\frac1{v_Ts}
\int_s^\infty
[F(c,t^2-s^2,t)+F(c,t^2-s^2,-t)]\,dt.
\tag{2.72}
\]
Compact support on the determinant-one section bounds \(t\) uniformly for small \(\theta\). Write
\(I_0=\int_0^\infty[F(1,t^2,t)+F(1,t^2,-t)]\,dt\).
On \(t\ge s\), the change in the integrand is \(O(s^2)\), by radial smoothness and \(c-1=O(s^2)\). The omitted interval has integral \(2s f(1)+O(s^2)\). Therefore
\[
O_{r_\theta}(f)=\frac{I_0}{v_T\sin\theta}
-\frac{2f(1)}{v_T}+O(\theta).
\tag{2.73}
\]

A positive split orbit of radius \(h=\sinh(u/2)\) has
\(\rho^2=z_0^2+h^2\). Its fixed invariant orbit measure is a nonzero positive constant times \(h^{-1}dz_0\,d\phi\). To see the radius factor, write Euclidean volume as
\(\rho\,d\rho\,d\phi\,dz_0=\tfrac12\,d(\rho^2-z_0^2)\,d\phi\,dz_0\).
Scaling the orbit coordinates by \(h\) scales this coarea measure by \(h\), while the quotient measure on the conjugating group is fixed; the latter must therefore be a fixed multiple of \(h^{-1}dz_0\,d\phi\). Invariance determines the constant, independently of \(h\). Thus \(h\,O_{a_u}(f)\) tends to a nonzero constant times \(I_0\). Vanishing of split orbital integrals forces \(I_0=0\).

On the compact quaternion side every conjugate of
\(\cos\theta+\sin\theta\,i\) tends uniformly to \(1\), and its orbital measure has total volume \(2/v_T\). Its limiting orbital integral is \(2f'(1)/v_T\). Equate this with (2.73), now with \(I_0=0\), to obtain \(f'(1)=-f(1)\). Central translation proves the assertion at every scalar; centrally covariant tests acquire the same scalar factor on both sides. \(\square\)

**Example — an exact rapidly decreasing orbital model.** On the determinant-one section write a matrix as \(cI+X\) in the coordinates above and take
\[
f(cI+X)=e^{-(\rho^2+z_0^2)}(1-4z_0^2),
\]
with zero on the other component. This test is smooth and rapidly decreasing on the central quotient. For a split orbit its orbital numerator is proportional to
\(e^{-h^2}\int_{\mathbb R}e^{-2t^2}(1-4t^2)\,dt=0\), because the integrand is the derivative of \(t e^{-2t^2}\). For an elliptic orbit, (2.72) gives
\[
\frac{2e^{s^2}}{v_Ts}\int_s^\infty e^{-2t^2}(1-4t^2)\,dt
=-\frac{2}{v_T}e^{-s^2}.
\]
It therefore matches the compact quaternion class test
\(f'(\cos\theta+\sin\theta\,i)=-e^{-\sin^2\theta}\).
At the identity its values are \(f(1)=1\) and \(f'(1)=-1\). All displayed improper integrals converge absolutely. The compact-support existence assertion will instead follow from the next construction.

**Lemma 2.21 — compact smooth tests selecting adjacent real weights.** For each \(k\ge2\) of parity \(\kappa\), there is a centrally covariant smooth test \(p_k\), supported in the positive-determinant component, such that
\[
\operatorname{tr}D_n(p_k)=\delta_{nk},\qquad
\operatorname{tr}I_\kappa(s)(p_k)=0.
\tag{2.74}
\]
All \(p_k\) have one common compact support modulo the centre. For each smooth derivative \(D\),
\(\|Dp_k\|_\infty\le C_D(1+k)^{N_D}\), with constants independent of \(k\).

**Proof.** The real ladder operators of Lesson 11 satisfy
\[
\Omega=H^2-2H+4EF,\qquad E^*=-F,\qquad A=-\Omega-1.
\]
On weight \(j\),
\[
A_j=4F_j^*F_j-(j-1)^2,
\tag{2.75}
\]
where \(F_j\) lowers the weight by two. This is elliptic on the homogeneous line bundle over the hyperbolic plane. Its positive principal symbol is the hyperbolic metric, up to a fixed scale; its connection and potential coefficients on fixed charts are polynomial in \(j\). The factorization gives \(A_j\ge-(j-1)^2\).

We give the analytic construction needed here. The shifted positive quadratic form on compact smooth sections gives a self-adjoint Friedrichs operator. Completeness of the hyperbolic plane makes the extension unique: multiply a deficiency solution by radial cutoffs with gradient tending to zero and use integration by parts. The real potential is bounded below, and the cutoff errors tend to zero; the positive shifted energy then forces that solution to vanish. The wave equation
\(\partial_t^2v+A_jv=0\) has propagation speed bounded independently of \(j\). Integrate its energy outside an expanding metric ball. The principal boundary flux is nonpositive at the metric propagation speed. Connection terms preserve that principal flux, while a sufficiently large \(j\)-dependent multiple of \(|v|^2\) absorbs the potential terms. Gronwall's inequality implies that initially zero exterior energy stays zero. Approximation gives the same support assertion for distributional initial data. The energy constant may depend on \(j\); the speed does not.

Let \(e_j\) be the probability compact-group idempotent selecting weight \(j\). The wave kernel with initial value \(e_j\) is the convolution distribution
\(e_j\cos(t\sqrt A)\). For a negative spectral value this denotes the entire function \(\cosh(t\sqrt{-A})\). Its support projects into a metric ball of radius a fixed constant times \(|t|\).

Choose \(R=3\) and nonzero nonnegative \(b\in C_c^\infty((1,2))\). Set
\[
\begin{aligned}
\phi_k(t)&=b(k(R-|t|)),\\
\Phi_k(a)&=\int_{\mathbb R}\phi_k(t)\cos(t\sqrt a)\,dt,\\
B_k&=\Phi_k(-(k-1)^2)>0,\\
p_k&=B_k^{-1}(e_k-e_{k-2})\Phi_k(A).
\end{aligned}
\tag{2.76}
\]
The last expression denotes its convolution kernel. The time bump is smooth and supported where \(R-2/k<|t|<R-1/k\), away from zero.

For \(a\ge0\), integration by parts \(2N\) times bounds the time integral using
\(\|\phi_k^{(2N)}\|_1\le C_Nk^{2N-1}\). For
\(-(k-1)^2\le a\le0\), use \(|\cos(t\sqrt a)|\le e^{R(k-1)}\). Together these give
\[
\sup_{a\ge-(k-1)^2}
(1+|a|)^N|\Phi_k(a)|
\le C_Nk^{2N+1}e^{R(k-1)},\qquad
B_k\ge c\,k^{-1}e^{R(k-1)}.
\tag{2.77}
\]
For the lower bound substitute \(v=k(R-t)\) in the positive-time integral. On the support of \(b\),
\(e^{-(k-1)v/k}\ge e^{-2}\), and
\(\cosh((k-1)t)\ge \tfrac12e^{(k-1)t}\).
The constants are independent of \(k\). Both weights \(k\) and \(k-2\) have spectral lower bound in the interval in (2.77).

Consequently every power of the positive elliptic shift
\(1+A_j+C(1+j^2)\), applied to the normalized integrated wave operator, has operator norm bounded by a polynomial in \(k\). Its local Sobolev estimates have constants polynomial in \(j\). Indeed derive the first estimate by integration by parts, absorbing connection coefficients of size \(C(1+|j|)\); differentiate and iterate, since their chart derivatives have the same polynomial bounds. A point mass and its derivatives have fixed negative Sobolev order with polynomial bounds in \(j\). Applying the operator estimates followed by these elliptic estimates shows that the kernel has every smooth derivative bounded polynomially in \(k\). The adjoint argument gives the other kernel variable as well. This proves smoothness and the stated seminorm bounds. Finite propagation places all kernels in one ball of fixed radius proportional to \(R\); its compact angular fibres give common compact support modulo the centre. Extending by zero to the other component is smooth.

To calculate traces, no Plancherel theorem is needed. Apply the compactly supported wave distribution to a compact-weight vector of any admissible representation. Its operator solves the ordinary wave equation with initial projection \(\pi(e_j)\); uniqueness gives
\[
\pi(e_j\Phi_k(A))
=\Phi_k(-\pi(\Omega)-1)\pi(e_j).
\]
This holds for complex principal parameters too, by the same equation or analytic continuation. In a principal series the two adjacent weight dimensions are both one, so their traces cancel. In the full \(D_n\), the positive weight \(j\) occurs once precisely when \(j\ge n\) with the correct parity. The difference of weights \(k,k-2\) is therefore one exactly for \(n=k\). Its Casimir is \(n(n-2)\), so the surviving multiplier is \(B_k/B_k=1\). This proves (2.74). \(\square\)

This is a rank-one adjacent-weight version of the Euler–Poincaré construction; compare Deitmar, [Section 4](https://arxiv.org/abs/math/0201233). Here the wave multiplier is explicit, its support is proved, and shrinking time bumps give the polynomial bounds required for a smooth infinite sum.

**Theorem 2.22 — complete real smooth and spectral transfer.** Every smooth compact centrally covariant quaternion test \(f'\) has a smooth compact centrally covariant split transfer \(f\):
\[
O_g(f)=O_b(f')\text{ on matching regular elliptic classes},
\qquad O_g(f)=0\text{ on regular split classes}.
\tag{2.78}
\]
Every pair satisfying these identities satisfies (2.71) and
\[
\operatorname{tr}D_{m+2}(f)
=-\operatorname{tr}\operatorname{Sym}^m(f'),\qquad
\operatorname{tr}I_\kappa(s)(f)=0.
\tag{2.79}
\]
A determinant character with the prescribed central character has trace equal to that of the corresponding norm character against \(f'\). The same transfer existence holds for ordinary compact smooth tests on the groups before taking the central quotient.

**Proof.** First determine the orbital integrals of \(p_k\). Weyl integration is valid by the locally integrable character formulas above. On split classes its Jacobian is \(4\sinh^2(u/2)\). Formula (2.70) expresses the principal trace as the Fourier cosine transform of a fixed constant times
\(|\sinh(u/2)|O_{a_u}(p_k)\).
This is even, integrable and compactly supported in \(u\), since eigenvalue ratios are bounded on the test's support. The bound \(O_{a_u}(p_k)=O(1/|u|)\) near zero follows from the one-sheeted calculation in Lemma 2.20. Fourier uniqueness and (2.74) give zero split orbital integrals. On the other component they vanish because the test is zero there.

At elliptic classes the two groups have the same Weyl Jacobian \(4\sin^2\theta\), Weyl order two and torus measures. The constants really agree: the real Cartan normalization gives tangent density \(2/\pi^2\) in the three coordinates of Lemma 2.20; the compact quaternion quotient of volume \(2\) has that same density in its three imaginary coordinates. The conjugation Jacobian is the stated discriminant on each side. Dividing by the paired centralizer measure gives identical Weyl measures on the matching torus.

The compact target for \(p_k\) is the class function
\(-\Theta_{\operatorname{Sym}^{k-2}}/2\).
With compact volume \(2\), its trace in \(\operatorname{Sym}^m\) is
\(-\delta_{m,k-2}\), by Schur orthogonality. Use (2.22) and (2.74) in the elliptic Weyl integral. The difference between the two orbital integrals is orthogonal to every compact character of the given parity, with weight \(\sin^2\theta\,d\theta\). It lies in this weighted \(L^2\) space: (2.72) gives endpoint growth at most \(C/|\sin\theta|\). The characters are complete there, since multiplication by \(\sin\theta\) sends
\(\Theta_{\operatorname{Sym}^m}\) to \(\sin((m+1)\theta)\), the ordinary Fourier sine basis; restricting central parity restricts to the corresponding reflection parity. Thus the difference is zero almost everywhere and hence everywhere on the regular set by smoothness. This proves transfer for \(p_k\).

Conjugation-average \(f'\); this changes none of its orbital integrals, traces or scalar values. Put
\(a_m=\operatorname{tr}\operatorname{Sym}^m(f')\).
Compact character expansion gives
\[
f'_{\rm av}=\frac12
\sum_{\substack{m\ge0\\m\equiv\kappa\ (2)}}
a_m\Theta_{\operatorname{Sym}^m}.
\tag{2.80}
\]
The coefficients decrease faster than every power of \(m\): integrate by parts repeatedly with the compact Casimir, whose eigenvalue grows quadratically. Additional compact derivatives give convergence in \(C^\infty\).

Set \(f=-\sum_m a_m p_{m+2}\). The polynomial seminorm bounds and common support in Lemma 2.21 make this a convergent compact smooth sum. Orbital integration on a fixed compact support is continuous at each regular class, so the sum has exactly the orbital integrals in (2.78). For every matching pair, the same Weyl formulas and character identities prove (2.79), and Lemma 2.20 proves its scalar identity.

A one-dimensional determinant character is constant on each determinant fibre. Its split contribution is zero. Its elliptic Weyl integral equals the compact Weyl integral of the norm character, with positive sign. This proves the one-dimensional assertion and distinguishes it from the negative discrete-series relation.

Finally, ordinary compact tests require no assumption of a fixed positive central character. Write each quaternion as \(c u\), \(c>0\), with unit quaternion \(u\), split the \(u\)-test into its two parities under \(u\mapsto-u\), and apply the preceding construction for each \(c\). The coefficients \(a_m(c)\) and all their \(c\)-derivatives decrease rapidly, uniformly on the compact \(c\)-support. The common support and polynomial bounds therefore give a compact smooth split test depending smoothly on \(c\), extended by zero to negative determinant. Orbital matching is pointwise at each \(c\). For fixed centrally covariant tests restore their positive central twist on both sides. \(\square\)

The next three sections supply the finite all-level correspondence and its spectral transfer. The full global trace comparison remains a separate argument.

### 2.8. Construct every division-side local image

This section constructs a split representation from every irreducible quaternion representation, without restricting its level or using a quadratic-character classification of supercuspidals. The bijection, elliptic character comparison and paired degrees will require the orthogonality argument following the construction.

Let \(F\) be any nonarchimedean local field, \(D\) its quaternion division algebra, \(N=\operatorname{nrd}\), \(\tau=\operatorname{trd}\), and \(\iota(x)=\tau(x)-x\). Put \(D^1=\ker N\). Use the additive Fourier transform
\[
\widehat\Phi(y)=\int_D\Phi(x)\psi(\tau(xy))\,dx
\]
with self-dual measure. The polar transform of the quadratic norm is
\(\mathcal F_Q\Phi(y)=\widehat\Phi(y^\iota)\), since
\(N(x+y)-N(x)-N(y)=\tau(xy^\iota)\).
It is nondegenerate in characteristic two as well. Involution preserves measure, and
\(\mathcal F_Q^2\Phi(x)=\Phi(-x)\).

**Lemma 2.23 — the quaternion norm operators, in every characteristic.** If \(T\) is an irreducible smooth representation of \(D^\times\) on \(U\), with central character \(\eta\), the space
\[
\mathcal S(D,T)=
\{\Phi\in\mathcal S(D,U):
 \Phi(xu)=T(u)^{-1}\Phi(x),\ u\in D^1\}
\tag{2.81}
\]
carries a smooth admissible representation \(r_T\) of \(\mathrm{GL}_2(F)\). Its formulas are
\[
\begin{aligned}
r_T(n(b))\Phi(x)&=\psi(bN(x))\Phi(x),\\
r_T(m(a))\Phi(x)&=|a|^2\Phi(ax),\\
r_T(w_0)\Phi(x)&=-\widehat\Phi(x^\iota),\\
r_T(d(Nh))\Phi(x)&=|Nh|\,T(h)\Phi(xh).
\end{aligned}
\tag{2.82}
\]
Here \(m(a)=\operatorname{diag}(a,a^{-1})\),
\(d(t)=\operatorname{diag}(t,1)\), and
\(w_0=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\).
A scalar \(aI\) acts by \(\eta(a)\).

**Proof.** The quaternion structure in Lesson 17 lets us write
\(D=E\oplus E\Pi\), with \(E/F\) unramified quadratic,
\(\Pi^2=\varpi\), and \(\Pi z=z^\sigma\Pi\). Thus
\(N(x+y\Pi)=N_E(x)-\varpi N_E(y)\).
The norm maps \(D^\times\) onto \(F^\times\): norms from the unramified units give every unit, and \(N(\Pi)=-\varpi\) gives valuation one. Its kernel is compact.

The exact norm Gaussian in Lesson 10, Lemmas 6.1–6.2, applies to both summands. If \(\eta_E\) is the unramified quadratic norm character and \(\lambda=\epsilon(1/2,\eta_E,\psi)\), then
\(\lambda^2=\eta_E(-1)\), and scaling the second summand's character by \(-\varpi\) changes its phase to \(\eta_E(-\varpi)\lambda\). Their product is
\(\eta_E(-1)\eta_E(-\varpi)=\eta_E(\varpi)=-1\).
Use the product of the corresponding self-dual measures; it is precisely the measure for the polar pairing of \(N\). Multiplying the two Gaussian identities gives
\[
\int_D^{\rm st}\psi(bN(x))\,dx=-|b|^{-2},
\qquad
\mathcal F_Q(\psi(bN))(y)=-|b|^{-2}\psi(-N(y)/b).
\tag{2.83}
\]
These are distributional identities, established on compact tests; no division by two is involved.

The upper-triangular relations, Fourier scaling and
\(w_0^2=m(-1)\) follow directly from (2.82). For the remaining Bruhat relation
\[
w_0n(b)w_0=
n(-b^{-1})m(-b^{-1})w_0n(-b^{-1})
\quad(b\ne0),
\]
(2.83) gives the same kernel and phase on both sides. The amplitude has absolute value \(|b|^{-2}\); on the left the two Weyl signs combine with the negative Gaussian sign, agreeing with the single Weyl sign on the right. The two Bruhat cells give a presentation exactly as in Lesson 10, Theorem 6.3, so these operators define the norm representation of \(\mathrm{SL}_2(F)\).

The operators preserve (2.81). For the polar transform, its covariance follows by substituting \(x\mapsto xu\) and using \(N(u)=1\). More explicitly, the trace-pair Fourier transform of a right-covariant test is left-covariant:
\(\widehat\Phi(uy)=T(u)\widehat\Phi(y)\), \(u\in D^1\); applying involution changes this to the required right covariance.

The last operator in (2.82) is independent of the chosen \(h\). Replacing \(h\) by \(hu\), \(u\in D^1\), cancels \(T(u)\) by (2.81). Products have the required determinant product. It conjugates \(n(b)\) to \(n(Nh\,b)\), and commutes with \(m(a)\). Fourier change of variables, whose additive Jacobian is \(|Nh|^2\), verifies the Weyl relation. To track noncommutativity explicitly, for \(t=Nh\) the composition of the determinant operator, the polar transform and the determinant operator has argument \(xh^2/t\). This factor \(h^2/t\) has norm one; covariance cancels \(T(h)^2\) and leaves \(T(t)\). It follows that
\(r_T(d(t))r_T(w_0)r_T(d(t))=\eta(t)r_T(w_0)\),
the relation \(d(t)w_0d(t)=t w_0\).
Together with \(d(a^2)m(a^{-1})=aI\), these checks give the full group and its stated central action.

Smoothness follows from compact support, local constancy and the openness of the norm on arbitrarily small unit neighborhoods. For that last assertion, at the identity the norm polynomial has differential \(\tau\), which is nonzero: the unramified separable subfield already has surjective residue trace. Solving along that direction by a contraction on a sufficiently small ideal proves openness, in characteristic two too. A small upper-unipotent fixes \(\Phi\); apply the same assertion to its polar transform to obtain a small lower-unipotent fixing subgroup. Small diagonal units fix it by the determinant formula. Gaussian elimination near the identity gives an open group fixing \(\Phi\).

Finally, vectors fixed by an upper-unipotent group \(n(\mathfrak p^a)\) have support in one bounded fractional quaternion ideal: if \(\psi\) has annihilator \(\mathfrak p^{-\ell}\), its norm valuations must be at least \(-a-\ell\). Fixing the opposite unipotent bounds the polar Fourier support in the same way. Fourier orthogonality then makes such a test constant on cosets of the annihilator of that bounded Fourier-support ideal. It is a function on a finite quotient of a bounded ideal, with values in finite-dimensional \(U\). Every sufficiently small compact-open fixed space is contained in such a finite-dimensional space. This proves admissibility. \(\square\)

A unitary \(T\) makes all operators in (2.82) unitary on their subspace of \(L^2(D,U)\): the determinant Jacobian cancels \(|Nh|^2\), and the polar Fourier operator is an isometry. Every \(T\) with unitary central character can be made unitary by averaging over \(D^\times/F^\times\), as in Lesson 17.

**Lemma 2.24 — the complete division-side matrix functional equation.** If \(\dim T>1\), put
\[
Z_D(s,\Phi,T)=
\int_{D^\times}|Nx|^{s+1/2}T(x)\Phi(x)\,d^\times x.
\tag{2.84}
\]
For all vector tests this is an entire Laurent polynomial in \(q^{-s}\). There is a nonzero monomial \(\epsilon_D(s,T,\psi)\) such that
\[
\int_{D^\times}|Ny|^{3/2-s}T(y)^{-1}\widehat\Phi(y)\,d^\times y
=-\epsilon_D(s,T,\psi)Z_D(s,\Phi,T).
\tag{2.85}
\]
These statements hold after every norm-character twist. Scalar tests and a dual vector give the corresponding matrix-coefficient equation; its Euler factors are \(L_D(s,T)=L_D(s,T^\vee)=1\).

**Proof.** First \(D^1\) is the commutator subgroup. If \(x\in D^1\) is not central, \(x^\iota=x^{-1}\) and its reduced polynomial \(X^2-\tau(x)X+1\) is separable. In characteristic two, a repeated root would force \((x-1)^2=0\), impossible in a division algebra unless \(x=1\). In other characteristics, repetition similarly makes \(x=\pm1\). Thus \(x\) lies in a separable quadratic subfield; central \(x=\pm1\) lies in the unramified one. Hilbert 90 gives \(x=y/y^\iota\) in that field. The quadratic embedding and conjugation result in Section 1 supplies \(j\) inducing its nontrivial involution. Hence \(x=yjy^{-1}j^{-1}\). Conversely every commutator has norm one. Therefore a representation with a \(D^1\)-fixed vector, by normality and irreducibility, is a character of \(D^\times/D^1=F^\times\), and is one-dimensional.

Average a test to
\(\Phi_1(x)=\int_{D^1}T(u)\Phi(xu)\,du\),
with probability measure. It belongs to (2.81), leaves (2.84) unchanged, and has \(\Phi_1(0)=0\) when \(\dim T>1\). Thus it vanishes in a neighborhood of zero. Its Fourier transform is left-covariant and also vanishes near zero. Both projected tests have compact support in \(D^\times\), so their zeta integrals are finite sums of powers of \(q^{-s}\). This also proves the assertion for arbitrary tests and for the left side of (2.85).

We prove its scalar proportionality, rather than assume a local correspondence. On scalar tests in \(\mathcal S(D^\times)\), let \(A_s(\phi)\) be the operator obtained from the right side of (2.84), and \(B_s(\phi)\) the operator obtained from the integral on the left of (2.85). For
\(\lambda(h)\phi(x)=\phi(h^{-1}x)\),
\(\rho(h)\phi(x)=\phi(xh)\), direct change of variables gives
\[
\begin{aligned}
A_s(\lambda(h)\phi)&=|Nh|^{s+1/2}T(h)A_s(\phi),\\
A_s(\rho(h)\phi)&=|Nh|^{-s-1/2}A_s(\phi)T(h)^{-1}.
\end{aligned}
\tag{2.86}
\]
Fourier transformation exchanges these two translations and supplies the factor \(|Nh|^{\pm2}\). Consequently \(B_s\) has exactly the same two identities.

Here is the distributional uniqueness in this assertion. On the open homogeneous space \(D^\times\), smooth equivariance under left translations identifies the distribution with the integral of a locally constant matrix density: average over a compact open subgroup on which \(T\) and the norm character are trivial, then translate its cosets. Its density is determined by its value at the identity. The right-translation identity forces that value to commute with every \(T(h)\), hence to be scalar by Schur. Thus \(B_s=c_sA_s\). The conclusion extends from \(\mathcal S(D^\times)\) to \(\mathcal S(D)\) by the \(D^1\) projections above; both projections vanish near zero, so a distribution at zero cannot supply an extra term. Define \(c_s=-\epsilon_D(s,T,\psi)\).

For \(u\in U\), the test
\(\Phi_u(x)=T(x)^{-1}u\,\mathbf1_{\mathcal O_D^\times}(x)\)
has \(Z_D(s,\Phi_u,T)=v_Du\), where
\(v_D=\operatorname{vol}(\mathcal O_D^\times)\), independent of \(s\).
Evaluating (2.85) on such tests shows that \(\epsilon_D\) is a Laurent polynomial. Transpose the matrix equation to use \(T^\vee\), apply it twice and use \(\widehat{\widehat\phi}(x)=\phi(-x)\). This gives
\[
\epsilon_D(s,T,\psi)
\epsilon_D(1-s,T^\vee,\psi)=\eta(-1).
\tag{2.87}
\]
The same test for \(T^\vee\) shows that the second factor is a Laurent polynomial. A Laurent polynomial with a Laurent-polynomial inverse is a nonzero monomial: its highest and lowest powers add under multiplication, so the width of each factor must be zero. This proves (2.85), its nonvanishing, and attainment of the Euler factor one. A norm twist preserves the absence of \(D^1\)-fixed vectors, so the entire argument applies to it. \(\square\)

**Theorem 2.25 — a supercuspidal image for every noncharacter \(T\).** If \(\dim T=d>1\), then \(r_T\) is a direct sum of \(d\) copies of a single irreducible admissible supercuspidal \(\pi_T\), with central character \(\eta\). Every norm twist and dual has the corresponding determinant twist and dual, and
\[
L(s,\pi_T\otimes\chi)=1,\qquad
\epsilon(s,\pi_T\otimes\chi,\psi)
=\epsilon_D(s,T\otimes(\chi\circ N),\psi)
\tag{2.88}
\]
for every smooth quasicharacter \(\chi\). If \(T\) is unitary, so is \(\pi_T\).

**Proof.** Every test in (2.81) vanishes near zero, by Lemma 2.24. For \(a=Nh\), define
\[
f_\Phi(a)=|a|T(h)\Phi(h).
\tag{2.89}
\]
It is independent of the norm-fibre representative. It gives a bijection
\(\mathcal S(D,T)\to\mathcal S(F^\times,U)\):
the inverse is
\(\Phi(x)=|Nx|^{-1}T(x)^{-1}f(Nx)\), with zero at zero.
Properness of the quaternion norm and its open compact fibres prove compact support and local constancy in both directions. The upper Borel acts by
\[
r_T(n(b))f(a)=\psi(ab)f(a),\qquad
r_T(d(t))f(a)=f(at),
\]
and the central character is already \(\eta\).

For \(g=r_T(w_0)f\), multiplicative Mellin transformation of (2.89), followed by \(y=h^\iota\), gives
\[
\int g(a)\chi(a)^{-1}\eta(a)^{-1}|a|^{1/2-s}\,d^\times a
=\epsilon_D(s,T\otimes(\chi\circ N),\psi)
 \int f(a)\chi(a)|a|^{s-1/2}\,d^\times a.
\tag{2.90}
\]
Indeed \(h=a(h^\iota)^{-1}\) implies
\(T(h)=\eta(a)T(h^\iota)^{-1}\); it cancels the displayed \(\eta^{-1}\), and the minus sign in \(r_T(w_0)\) cancels the minus in (2.85). Use probability norm-one fibre measure in (2.84); any common positive multiplicative normalization cancels. These checks track the exact phase and both exponents.

Every linear subspace \(U_0\subset U\) is therefore preserved in
\(\mathcal S(F^\times,U_0)\) by the Weyl operator. Apply a linear functional annihilating \(U_0\) to (2.90); every Mellin transform of the resulting compact function is zero, so compact-unit Fourier orthogonality and the finite valuation support give the function zero. The upper Borel preserves that subspace as well. Hence each line of \(U\) gives an invariant scalar copy \(\mathcal S(F^\times)\).

The affine action on this scalar space is irreducible. From a nonzero compact locally constant function, additive-character averaging in \(n(b)\) isolates a nonzero constant value on a sufficiently small multiplicative ball. Diagonal translations give every translate of that ball. Repeating the character projections makes it arbitrarily small; its translates span all compact locally constant functions on \(F^\times\). A nonzero invariant subspace must therefore be the entire scalar space. This proves irreducibility under the upper Borel, and hence under the full group. Admissibility follows from Lemma 2.23. The scalar space is exactly the compact Kirillov space; the Jacquet quotient is zero by those same character projections. The compact-Kirillov supercuspidal criterion proved in Lessons 6–7 identifies it as supercuspidal and gives \(L(s,\pi_T\otimes\chi)=1\).

Equation (2.90) is precisely the local functional equation in Lesson 9, with its normalized Mellin exponent \(s-1/2\). It proves (2.88). The scalar Weyl operator is determined by these Mellin equations, so the copies for different lines are all equivalent. A basis of \(U\) now gives the stated direct sum.

For a norm twist, its zeta equation is obtained by multiplying the test by \(\chi(Nx)\); the resulting central character is \(\eta\chi^2\). Its Euler and epsilon data agree with the determinant twist. Equation (2.87), together with the corresponding split duality identity in Lesson 9, gives the same data for \(\pi_{T^\vee}\) and \(\pi_T^\vee\). The local converse theorem of that lesson, with their central characters and every character twist, identifies these representations. No existence or surjectivity statement from a local Langlands correspondence is used.

For unitary \(T\), norm-fibre disintegration of additive measure gives
\(dx=C|a|^2\,d^\times a\,du\). In (2.89) the factor \(|a|\) cancels this density:
\(\|\Phi\|_{L^2(D,U)}^2=C\int\|f(a)\|^2\,d^\times a\).
Thus each scalar copy inherits a unitary Hilbert norm from (2.82). \(\square\)

**Lemma 2.26 — norm characters give the special representation and its factors.** Every one-dimensional \(T\) is \(\chi\circ N\), and its construction is the special representation
\(\mathrm{St}\otimes(\chi\circ\det)\). Its division matrix factors and the split factors agree after every twist:
\[
L_D(s,\chi\circ N)=L_F(s+1/2,\chi),\qquad
L_D(s,T^\vee)=L_F(s+1/2,\chi^{-1}),
\tag{2.91}
\]
with the same epsilon factor and the division Fourier minus sign. If \(B_D(1-s,\Phi,T^\vee)\) denotes the left integral of (2.85), the precise normalized equation in this case is
\[
\frac{B_D(1-s,\Phi,T^\vee)}{L_D(1-s,T^\vee)}
=-\epsilon_D(s,T,\psi)
 \frac{Z_D(s,\Phi,T)}{L_D(s,T)}.
\]
For noncharacters both denominators are one, so this reduces exactly to (2.85).

**Proof.** The commutator calculation in Lemma 2.24 gives the first assertion. In this case (2.81) consists of scalar norm-fibre-constant tests. Its image (2.89) contains \(\mathcal S(F^\times)\) and has one additional small-\(a\) germ, \(\chi(a)|a|\) times \(\Phi(0)\). Thus the compact subspace has codimension one. Any nonzero invariant subspace contains a nonzero compact vector: apply \(n(b)-1\), which kills the germ sufficiently near zero and is nonzero for a suitable \(b\). The affine irreducibility argument includes the whole compact subspace. A nonnegative, nonzero test supported on a unit shell has nonzero Fourier value at zero. The Weyl operator consequently sends a compact vector to one with nonzero germ. The invariant subspace is the whole space. This proves irreducibility.

Its unique Jacquet germ transforms under \(d(t)\) by \(\chi(t)|t|\). The normalized induction classification in Lesson 7 identifies this irreducible generic module as
\(\mathrm{St}\otimes\chi\), with inducing characters
\(\chi|\cdot|^{1/2},\chi|\cdot|^{-1/2}\).
The central character is \(\chi^2\), consistent with (2.82).

A scalar test is constant near zero. Its unramified small-ball norm-shell tail is a geometric series in
\(\chi(\varpi)q^{-s-1/2}\), giving (2.91); if \(\chi\) is ramified, averaging over the surjective unit norm kills that tail. Unit-shell tests attain the normalized factor. Under (2.89), this is the split Kirillov Mellin integral with exponent \(s-1/2\). The polar Weyl operator is the same as before, including its minus sign. Its Mellin equation and the exact special functional equation in Lesson 9 therefore identify the epsilon factor too. Scalar tests are reduced to norm-fibre-constant ones by probability averaging over \(D^1\), so the equality holds for every matrix zeta test, rather than only a radial sample. \(\square\)


**Computed example — the Steinberg phase from the quaternion integer ring.** Choose \(\psi\) of conductor \(\mathcal O_F\) and an unramified \(\chi\), with \(\alpha=\chi(\varpi)\). The trace-dual of \(\mathcal O_D=\mathcal O_E\oplus\mathcal O_E\Pi\) is
\(\mathfrak P_D^{-1}=\mathcal O_E\oplus\varpi^{-1}\mathcal O_E\Pi\). Its self-dual volume is \(q^{-1}\), hence
\(\widehat{\mathbf1_{\mathcal O_D}}=q^{-1}\mathbf1_{\mathfrak P_D^{-1}}\).
Writing \(v_D=\operatorname{vol}(\mathcal O_D^\times)\) and summing norm-valuation shells gives
\[
Z_D(s,\mathbf1_{\mathcal O_D},\chi\circ N)
=\frac{v_D}{1-\alpha q^{-s-1/2}},
\qquad
B_D(1-s,\mathbf1_{\mathcal O_D},(\chi\circ N)^\vee)
=\frac{\alpha q^{1/2-s}v_D}{1-\alpha^{-1}q^{s-3/2}}.
\]
The normalized division minus sign therefore gives
\(\epsilon_D(s,\chi\circ N,\psi)=-\alpha q^{1/2-s}\), precisely the Steinberg factor of Lesson 9. This computes the phase, its exponent and both half-unit shifts directly, in every residue characteristic.

The construction covers every irreducible \(T\) in every residue and field characteristic, with its full central character, all twisted factors and a unitary discrete-series image. The next two sections prove injectivity and surjectivity by Fourier comparison and elliptic orthogonality.

### 2.9. Character integration through the finite singular set

The regular character theorem does not by itself give the trace of a test whose support meets singular classes. We prove that extension now. This is also where characteristic two needs its own estimate: the unmodified inverse square root of the Weyl discriminant is not a suitable integrable bound there.

Choose an additive character of conductor \(\mathcal O_F\) for this proof; changing it rescales the measures by positive constants. Put \(K=\mathrm{GL}_2(\mathcal O_F)\), and let \(C_R\subset G/Z\) consist of the classes with elementary-divisor gap at most \(R\). These are compact, exhaust \(G/Z\), and are invariant under multiplication by \(K\) on both sides. For a separable quadratic field \(E/F\), let \(d_E\) be its discriminant exponent and \(c_E=q^{-d_E/2}\). On the regular set put
\[
\delta(g)=\left|\frac{(\alpha-\beta)^2}{\alpha\beta}\right|,
\qquad
\xi(g)=
\begin{cases}
\delta(g)^{-1/2},&\alpha,\beta\in F,\\
c_E\delta(g)^{-1/2},&F[g]=E.
\end{cases}
\tag{2.92}
\]
The unspecified value on the singular set is irrelevant to integration. That set has measure zero: its equation is the nonzero polynomial \(\operatorname{tr}(g)^2-4\det g=0\), which in characteristic two becomes \(\operatorname{tr}(g)=0\). A nonzero polynomial has a null zero set, by induction on its variables and Fubini.

**Lemma 2.27 — an integrable majorant and every finite-place trace.** The function \(\xi\) is locally integrable on \(G\) and \(G/Z\), and is bounded below by a positive number on a compact set. For every irreducible smooth \(\pi\), the regular character of Theorem 2.7 is locally bounded by a multiple of \(\xi\) and
\[
\operatorname{tr}\pi(f)=\int_G f(g)\Theta_\pi(g)\,dg
\qquad(f\in C_c^\infty(G)).
\tag{2.93}
\]
There is no additional distribution supported on singular classes. This includes local fields of characteristic two.

**Proof: orbital bounds.** We first establish the estimates that will justify dominated convergence. Use self-dual trace measure \(dx_E\) on the quadratic algebra and \(d^\times b=dx_E/|N_Eb|\), with the same central measure for all tori. The conjugation map
\((T\backslash G)\times T_{\mathrm{reg}}\to G\) has Jacobian \(\delta(b)\) and degree two. Its differential on the two root directions is \(1-\alpha/\beta\) and \(1-\beta/\alpha\). Local inverse charts follow from the contraction argument for simple roots in Theorem 2.7; compact-open partitions and change of variables give Weyl integration. It holds for nonnegative measurable functions by monotone convergence, also when the disjoint union of quadratic tori is infinite.

For an anisotropic torus, regard \(F^2\) as \(E\). Every lattice, up to multiplication by \(E^\times\), is an order
\(R_j=\mathcal O_F+\mathfrak p^j\mathcal O_E\), \(j\ge0\). Here is the elementary lattice argument. Scale a lattice by an element of minimal \(E\)-valuation; it then contains 1 and lies in \(\mathcal O_E\). Its quotient by \(\mathcal O_F\) is torsion free, so it has basis \(1,y\). Integrality gives \(y^2\in\mathcal O_F+\mathcal O_Fy\), hence it is an order. Using an integral basis \(1,\omega\) of \(\mathcal O_E\), its second generator gives exactly \(R_j\). Two such orders are homothetic only if their multiplier orders, and therefore their \(j\)'s, agree.

The number of vertices in the \(E^\times\)-orbit of this lattice is
\[
[E^\times:F^\times R_j^\times]=
\begin{cases}
1,&E/F\text{ unramified},\ j=0,\\
(q+1)q^{j-1},&E/F\text{ unramified},\ j>0,\\
2q^j,&E/F\text{ ramified}.
\end{cases}
\tag{2.94}
\]
Indeed units modulo \(\mathfrak p^j\mathcal O_E\), modulo the image of \(\mathcal O_F^\times\), give the displayed unit indices; valuations add the ramification index two in the ramified case. The same formulas follow by successive quotients: each step after the first has index \(q\).

If \(\gamma\in E\setminus F\) is integral, write \(\mathcal O_F[\gamma]=R_{j(\gamma)}\). Comparing the discriminants of the bases \(1,\gamma\) and \(1,\omega\) gives
\[
|\gamma-\gamma^\sigma|_E^{1/2}
=q^{-j(\gamma)}c_E.
\tag{2.95}
\]
Our absolute value on \(E\) is \(|N_{E/F}(\cdot)|_F\). This identity is valid for wild quadratic extensions as well.

Let \(m=v_F(N_E\gamma)\), and \(s=\lfloor(R-m)/2\rfloor\). The elementary-divisor condition for multiplication by \(\gamma\) on a lattice is equivalent to \(\varpi^s\gamma\) preserving that lattice. Consequently only \(R_j\) containing \(\varpi^s\gamma\) occur, and (2.94) bounds their total vertex count by
\(Cq^{j(\varpi^s\gamma)}\). If the scaled element is not integral there is no contribution. Equation (2.95) gives
\[
q^{j(\varpi^s\gamma)}
=q^{s+m/2}\xi(\gamma)\le q^{R/2}\xi(\gamma).
\]
Decomposing \(G/Z\) into vertex cosets therefore proves
\[
\int_{G/Z}\mathbf1_{C_R}(x^{-1}bx)\,dx
\le A_R\xi(b)\quad(b\text{ elliptic regular}).
\tag{2.96}
\]
All constants are independent of the quadratic field.

The volume \(v_E=\operatorname{vol}(E^\times/F^\times)\) is
\(1+q^{-1}\) if \(E/F\) is unramified and \(2c_E\) if it is ramified, for these trace measures. To check this, \(\operatorname{vol}(\mathcal O_E)=c_E\), from the trace-dual lattice \(\mathfrak D_E^{-1}\); divide the unit volume by \(\operatorname{vol}(\mathcal O_F^\times)=1-q^{-1}\), and count the valuation cosets. Thus (2.96), divided by \(v_E\), bounds the orbital integral by \(A'_R\delta(b)^{-1/2}\).

For the split torus the same bound follows directly from Iwasawa coordinates. Conjugating \(\operatorname{diag}(\alpha,\beta)\) by \(n(x)\) gives upper entry \((\alpha-\beta)x\). With \(v(\alpha)=l\le m=v(\beta)\), the condition to be in \(C_R\) bounds \(v(x)\) below by \((m-l-R)/2\) after the substitution \(x\mapsto(1-\beta/\alpha)x\). Its measure is at most
\(A_R|1-\beta/\alpha|^{-1}q^{-(m-l)/2}=A_R\delta(b)^{-1/2}\).
Integration over \(K\) changes only the constant.

**Proof: integrability, including the infinite quadratic family.** Apply Weyl integration to \(\mathbf1_{C_R}\xi\). On the split torus its determinant ratios range in a fixed compact subset of \(F^\times\). The product of its orbital bound, \(\xi\), and \(\delta\) is bounded, so this term is finite. On the elliptic tori those three factors leave at most \(A_Rc_E\), and integration over the torus quotient gives
\[
\int_{C_R}\xi(g)\,dg\le B_R
\left(1+\sum_{E/F\ \text{quadratic separable}}q^{-d_E}\right).
\tag{2.97}
\]
In odd characteristic there are finitely many square classes. In characteristic zero there are finitely many too: sufficiently deep units are squares by successive approximation in \((1+x)^2\); take a depth exceeding \(2v_F(2)\). Thus these cases cause no problem, even at residue characteristic two.

In characteristic two write \(F=k((\varpi))\). Artin–Schreier representatives for separable quadratic fields can be reduced to a constant, modulo \(z^2-z\) in \(k\), plus finitely many negative odd powers of \(\varpi\). Positive powers are removed by contraction for \(z^2-z\), and a negative even power is removed using its coefficient's square root in the finite perfect residue field. If the largest pole is odd \(m\), the extension is ramified and has discriminant exponent \(m+1\). Indeed, for a root \(y\) of \(y^2-y=a\),
\(\beta=\varpi^{(m+1)/2}y\) has an Eisenstein quadratic polynomial, is a uniformizer, and
\(\beta-\beta^\sigma=\varpi^{(m+1)/2}\). The discriminant of its integral basis \(1,\beta\) therefore has valuation \(m+1\). There are at most \(2q^{(m+1)/2}\) reduced choices with largest pole at most \(m\). Their contribution to (2.97) is bounded by a geometric series in \(q^{-(m+1)/2}\). There is also the single unramified quadratic field. This proves integrability.

For the lower bound on a compact matrix set, scale its entries to be integral and bound its determinant below. The split discriminant is bounded above. In an elliptic field, (2.95) gives
\(\xi(g)=|\det g|^{1/2}q^{j(g)}\ge |\det g|^{1/2}\).
The assertion follows. Central disintegration transfers all these statements between \(G\) and \(G/Z\).

**Proof: supercuspidal traces.** A quasicharacter twist reduces to unitary central character and only multiplies the claimed bound by a locally bounded factor. Take a smooth unit vector \(u\) in a unitary supercuspidal \(\pi\), and put
\[
A_R(h)=\int_{C_R}\langle\pi(x^{-1}hx)u,u\rangle\,dx.
\tag{2.98}
\]
Its coefficient has compact support modulo \(Z\), by the compact-coefficient criterion in Lesson 6. Schur orthogonality, with formal degree \(d_\pi\), gives
\[
\operatorname{tr}\pi(f)=d_\pi\lim_{R\to\infty}
\int_G f(h)A_R(h)\,dh.
\tag{2.99}
\]
To verify this iterated formula, choose an orthonormal basis adapted to the finite-dimensional compact-open fixed space containing both the image of \(\pi(f)\) and that of its adjoint. Its matrix has only finitely many nonzero entries. Insert those entries into
\(\langle\pi(f)\pi(x)u,\pi(x)u\rangle\), integrate the products of two coefficients, and use their \(L^2\) Schur relation. Each product is integrable by Cauchy–Schwarz. For finite \(R\), compactness permits reversing the integrations. This proves (2.99), without yet reversing an infinite integral.

On elliptic regular elements, (2.96) bounds \(|A_R|\) by a constant times \(\xi\). Conjugators taking a compact elliptic set into a fixed compact set modulo the centre stay in a compact subset of \(G/Z\). One direct proof uses \(K\)-Cartan coordinates: on the compact elliptic set and all its \(K\)-conjugates, both off-diagonal entries are bounded below, since a zero entry would give an \(F\)-eigenline. Conjugation by \(\operatorname{diag}(\varpi^n,1)\) scales one of them by \(\varpi^{-n}\); bounded target entries force \(n\) bounded. Determinants restrict the central rescaling to a compact set. Hence (2.98) stabilizes uniformly on compact elliptic subsets.

Here is the additional cancellation on split classes. On a compact regular split subset write
\(h=k^{-1}n(-x)\operatorname{diag}(\alpha,\beta)n(x)k\), with \(k\in K\), \(x\) bounded and \(\alpha,\beta\) in compact subsets of \(F^\times\). Such a presentation follows by choosing an integral primitive eigenvector and completing it to an integral basis; the upper entry divided by \(\alpha-\beta\) gives \(x\). On a larger compact set \(x\) need not be bounded, but the estimate below is independent of \(x\).

Average \(u\)'s finitely many \(K\)-translates modulo its stabilizer, writing them as \(u_i\). In Iwasawa coordinates a conjugator is
\(\operatorname{diag}(\gamma,1)n(z)k\), with quotient measure a constant times \(dz\,d^\times\gamma\,dk\). Put
\(B=1-\beta/\alpha\), \(t=v(B)\), \(m=v(\gamma)\), and substitute \(y=Bz\). The conjugated coefficient is
\[
\langle\pi(\operatorname{diag}(\alpha,\beta)
 n(\gamma^{-1}Bx+y))u_i,u_i\rangle,
\]
and there is the outer factor \(|B|^{-1}\). The elementary-divisor condition for
\(\left(\begin{smallmatrix}\gamma&\gamma y/B\\0&1\end{smallmatrix}\right)\)
is exactly
\[
-R\le m\le R,\qquad
v(y)\ge L=\left\lceil t-\frac{R+m}{2}\right\rceil.
\tag{2.100}
\]
Indeed its smaller elementary-divisor valuation is
\(\min(m,m+v(y)-t,0)\); subtracting twice this from its determinant valuation \(m\) proves both inequalities.

The zero Jacquet module gives an integer \(s_0\) for which
\(\int_{\mathfrak p^{s_0}}\pi(n(y))u_i\,dy=0\) for every \(i\). Averaging over any larger additive ball also gives zero. This is exactly the compact-unipotent criterion proved in Lesson 6; it may also be read immediately in the compact Kirillov model by additive Fourier orthogonality. Consequently the inner integral vanishes if \(L\le s_0\), irrespective of its translate \(\gamma^{-1}Bx\). Set \(j=m+R\). Only
\(0\le j<2(t-s_0)\) remain. Their absolute inner integrals are at most a fixed constant times \(q^{-t+j/2}\), so
\[
|A_R(h)|\le C|B|^{-1}
\sum_{0\le j<2(t-s_0)}q^{-t+j/2}
\le C'|B|^{-1}.
\tag{2.101}
\]
If the upper endpoint is nonpositive the sum is empty. The bound is independent of \(R,t,x\). On a compact matrix set, \(|\alpha|,|\beta|\) are bounded above and below, so it is a constant times \(\xi(h)\).

For convergence on a compact regular split subset, \(t\) takes finitely many values. For each remaining \(j\), write
\(\gamma=\varpi^{j-R}\varepsilon\). The translated term
\(\gamma^{-1}Bx=\varpi^{R-j}\varepsilon^{-1}Bx\) tends uniformly to zero. The integration ball in (2.100) is fixed after \(j,t\) are fixed. Smoothness makes the coefficient eventually equal to its unshifted value on this compact parameter set. Thus \(A_R\) converges uniformly there as well.

The local integrable bound and dominated convergence in (2.99) now give a locally integrable representing character on all tests. On the regular set it is the unique function in Theorem 2.7. Its elliptic value is in particular
\[
\Theta_\pi(b)=d_\pi
\int_{G/Z}\langle\pi(x^{-1}bx)u,u\rangle\,dx.
\tag{2.102}
\]
No assertion that a supercuspidal character vanishes on all split compact classes is made or needed: it is the complete unipotent integral of a compact matrix coefficient that vanishes.

**Proof: the other representations.** In normalized principal induction, a smooth test has the finite-rank compact-picture kernel already constructed in Theorem 2.7. Its diagonal trace, now without a regular-support restriction, is the Iwasawa integral
\[
\int_K\int_{F^\times\times F^\times}\int_F
 f(k^{-1}\operatorname{diag}(\alpha,\beta)n(x)k)
 \mu_1(\alpha)\mu_2(\beta)|\alpha/\beta|^{1/2}
\,dx\,d^\times\alpha\,d^\times\beta\,dk,
\]
with the compatible quotient normalization. For \(\alpha\ne\beta\), substitute
\(x=(1-\beta/\alpha)y\). Weyl integration identifies this with (2.34), zero on elliptic classes. The set \(\alpha=\beta\) is null in these two multiplicative variables. The absolute value of (2.34) is locally bounded by \(C\xi\), so the equality is integrable and no discarded singular term occurs. Determinant characters are locally bounded, and special characters are the difference of the induced and one-dimensional traces in the exact sequence (2.9). Admissibility makes this exact on each compact fixed space, so trace additivity proves (2.93) for them too. The classification of Lesson 7 completes the proof. \(\square\)

This lemma establishes finite character integration across the singular locus. The factor \(c_E\), the lattice count (2.94) and the characteristic-two quadratic count in (2.97) are essential to the all-field assertion; replacing them by a characteristic-zero argument would leave that scope unproved.

### 2.10. Fourier comparison and the full finite correspondence

Use the same additive character on both algebras. On \(M_2(F)\) and \(D\) take self-dual measure for \(\psi(\operatorname{tr}(xy))\) and \(\psi(\operatorname{trd}(xy))\), respectively, and multiplicative measure \(|\det x|^{-2}dx\) and \(|Nx|^{-2}dx\). Fix the same central and quadratic-torus measures. These are paired inner-form measures. To verify the pairing concretely, write each algebra as \(E\oplus Eu\), with \(u^2=1\) in the split algebra and \(u^2=\varpi\) in the division algebra. After scalar extension to \(E\), the coordinate algebra \(E\otimes_F E\) is \(E\times E\). The element \(h=(\varpi,1)\) has \(hh^\sigma=\varpi\). Multiplication of the second coordinate by \(h\) gives the cyclic-algebra isomorphism and multiplies its two-dimensional volume form by \(\varpi\). This works in characteristic two without adjoining a square root. The trace pairing on that coordinate likewise has coefficient \(\varpi\), so its self-dual measure acquires exactly \(|\varpi|\). Thus the transported invariant multiplicative forms and the self-dual constructions agree. We will keep their exact relative constant.

**Lemma 2.28 — split and division matrix Fourier identities.** Let \(T\) be a noncharacter division representation and \(\pi=\pi_T\) from Theorem 2.25. Write \(W=\pi(w_0)\). For \(\phi\in\mathcal S(F^\times)\), a vector \(v\) and a smooth dual vector \(v^*\), put
\[
\Phi_G(g)=\phi(\det g)|\det g|^{-1}
 \langle\pi(g^{-1})v,v^*\rangle,
\]
with zero on singular matrices. Then \(\Phi_G\in\mathcal S(M_2(F))\), and
\[
\widehat\Phi_G(g)=
 (W\phi)(\det g)|\det g|^{-1}\eta(\det g)^{-1}
 \langle\pi(g)v,v^*\rangle.
\tag{2.103}
\]
The right side is zero on singular matrices. With \(u\in U\), \(u^*\in U^*\), define
\(\Phi_D(x)=\phi(Nx)|Nx|^{-1}\langle T(x^{-1})u,u^*\rangle\), zero at zero. Then
\[
\widehat\Phi_D(x)=
 -(W\phi)(Nx)|Nx|^{-1}\eta(Nx)^{-1}
 \langle T(x)u,u^*\rangle.
\tag{2.104}
\]
Both identities include every test, exact measures and phase, and either field characteristic.

**Proof of the division identity.** The vector-valued test
\(\phi(Nx)|Nx|^{-1}T(x)^{-1}u\) belongs to (2.81). Its norm-fibre Kirillov image is exactly \(\phi(a)u\). Equations (2.82), (2.89) and scalarity of the Weyl action give
\(-|Nh|T(h)\widehat\Phi(h^\iota)=(W\phi)(Nh)u\).
Set \(x=h^\iota\) and use \(T(h)=\eta(Nx)T(x)^{-1}\). Pairing with \(u^*\) is (2.104). The projected Fourier test vanishes near zero by Lemma 2.24. This proof uses the constructed representation, rather than an assumed character identity.

**Proof of the split identity.** Compactness modulo the centre of a supercuspidal coefficient, and the compact norm support of \(\phi\), make \(\Phi_G\) compactly supported away from the singular set. The zero Jacquet module says that every integral of a translated coefficient along the full upper unipotent is zero. Hence its Fourier transform vanishes at a rank-one matrix: by left and right translation reduce to \(\operatorname{diag}(a,0)\), and integrate first over right \(n(x)\). The determinant and the Fourier kernel are constant in this variable, while its coefficient integral is zero. The same argument gives zero at the zero matrix. All integrals here can be made over compact cutoffs and then the compact coefficient support removes the cutoff.

It suffices to compute \(\widehat\Phi_G(I)\). We give the unit-shell calculation to determine its exact constant. In the compact Kirillov model use the pairing of Lesson 9, equation (2.2),
\(\langle f,f^*\rangle=\int f(a)f^*(-a)\,d^\times a\), with unit volume one. Let \(f,f^*,\phi\) have supports \(\varpi^{n_1}\mathcal O^\times\), \(\varpi^{n_2}\mathcal O^\times\), \(\varpi^n\mathcal O^\times\), and values there \(\gamma_1^{-1},\gamma_2^{-1},\nu^{-1}\). Such functions form bases of their Schwartz spaces. Put \(\eta(\varepsilon\varpi^r)=\eta_0(\varepsilon)z^r\), and write \(C_r^\mu\) for the Weyl coefficients in Lesson 9, equation (2.3). Unit Fourier inversion gives
\[
\langle f,f^*\rangle
=\mathbf1_{n_1=n_2}\mathbf1_{\gamma_1\gamma_2=1}\gamma_2(-1),
\quad
(W\phi)(1)=z^{-n}C_n^{\nu^{-1}\eta_0^{-1}}.
\tag{2.105}
\]
The product condition on the two unit characters in this formula is essential.

Set \(c=\operatorname{vol}_{dx}(\mathcal O^\times)\), and
\(G_\rho(t)=\int_{\mathcal O^\times}\rho(\varepsilon)\psi(\varepsilon t)\,d^\times\varepsilon\).
Fourier inversion of a unit-shell function gives
\[
\int_F G_\rho(\varpi^j x)\psi(bx)\,dx
=\begin{cases}
c^{-1}|\varpi|^{-j}\rho(-\varepsilon),&b=\varpi^j\varepsilon,\\
0,&v(b)\ne j.
\end{cases}
\tag{2.106}
\]
For \(j=0\), this is the Fourier inversion of the function \(c^{-1}\rho\mathbf1_{\mathcal O^\times}\); dilation gives the general case.

The big cell has coordinates
\[
g=bI\,n(-x)d(a)w_0n(y),\quad
\det g=b^2a,\quad \operatorname{tr}g=b(x-y),
\]
and its exact additive Jacobian is
\(dg=c^2|b|^4|a|\,d^\times b\,d^\times a\,dx\,dy\).
Indeed its entries are \(bx,b(a+xy),-b,-by\); the additive Jacobian before converting \(da,db\) to multiplicative measures is \(|b|^3\). This accounts for the constant often suppressed in this calculation.

Write \(a=\zeta\varpi^r\). Apply the Weyl coefficient formula to
\(\pi(w_0^{-1}d(a^{-1})n(x))f\), pair it with \(\pi^\vee(n(y))f^*\), and integrate in \(\zeta\). Unit orthogonality selects \(\mu=\nu^{-1}\eta_0^{-1}\). The integrand remaining for \(\widehat\Phi_G(I)\), summed over \(r\), is
\[
\begin{aligned}
c^2\eta(b)^{-1}|b|^2\nu(-1)z^{-r-n_1}
\phi(b^2\varpi^r)C_{r+n_1+n_2}^{\nu^{-1}\eta_0^{-1}}\qquad\qquad\\
\cdot G_{\nu\gamma_1^{-1}}(\varpi^{n_1}x)
G_{\nu\eta_0\gamma_2^{-1}}(\varpi^{n_2}y)
\psi(b(x-y))\,d^\times b\,dx\,dy.
\end{aligned}
\tag{2.107}
\]
This displayed expression can also be checked by expanding the two compact-unit Fourier series: the dilation contributes \(z^{-r-n_1}\), their valuation pairing selects the Weyl coefficient \(r+n_1+n_2\), and their unit pairing gives the two \(G\)'s.

Formula (2.106) first forces \(v(b)=n_1=n_2\). Then \(\phi(b^2\varpi^r)\) forces \(r+2n_1=n\). The two additive inversions give \(c^{-2}|\varpi|^{-2n_1}\), canceling both \(c^2\) and \(|b|^2\). Write \(b=\varpi^{n_1}\varepsilon\). The remaining unit factor is
\(\gamma_1(-1)^{-1}\gamma_1(\varepsilon)^{-1}\gamma_2(\varepsilon)^{-1}\), and its unit integral is zero unless \(\gamma_1\gamma_2=1\). In that case its sign is \(\gamma_2(-1)\). The power of \(z\) is \(z^{-r-2n_1}=z^{-n}\). Thus (2.107) is exactly the product in (2.105), with constant one.

The calculation is legitimate on compact cutoffs in the big cell. For each smooth unit character, \(G_\rho\) is compactly supported: sufficiently oscillatory additive integration on a unit coset is zero. After the unit-character selection, (2.106) restricts \(b\) to a fixed shell and \(r\) to a single value. Increasing the cutoffs therefore leaves the resulting integrals unchanged. The original compact matrix test permits dominated convergence back to the big cell; its complement is null. This justifies the expansions as finite unit-quotient Fourier calculations, rather than an unproved interchange of infinite series.

Finally replace \(\Phi_G(g)\) by \(\Phi_G(h^{-1}g)\). Its new scalar test is
\(\phi_h(a)=|\det h|\phi(a/\det h)\), and its new vector is \(\pi(h)v\). Fourier change of variables supplies \(|\det h|^2\). The identity
\(w_0d(a^{-1})=a^{-1}I\,d(a)w_0\) gives
\((W\phi_h)(1)=|a|\eta(a)^{-1}(W\phi)(a)\), \(a=\det h\).
The identity at \(I\) therefore proves (2.103) at every invertible matrix. Together with the singular calculation, it proves the lemma. \(\square\)

Let \(\mathcal C\) be the space of regular elliptic conjugacy classes: the disjoint union, over the separable quadratic fields, of \((E^\times/F^\times)_{\mathrm{reg}}\) modulo \(b\sim b^\sigma\). Functions in the elliptic space must be invariant under that involution; integration of their torus lifts uses the twofold Weyl measure
\[
d\mu_{\rm ell}=\frac12\,v_E^{-1}\delta(b)\,d^\times b\bmod F^\times.
\tag{2.108}
\]
For a fixed unitary central character, functions on these tori have the corresponding central covariance. This defines their elliptic \(L^2\) space.

**Lemma 2.29 — the two orthogonality statements, without a correspondence input.** Division characters with a fixed unitary central character form an orthonormal basis of this elliptic \(L^2\) space. Split discrete-series characters form an orthonormal family in the same space.

**Proof.** On \(D^\times/F^\times\), finite-dimensional unitary Schur orthogonality, normalized by its total volume, gives orthonormal division characters. Division Weyl integration turns this normalized inner product into (2.108): the quotient orbit has volume \(\operatorname{vol}(D^\times/F^\times)/v_E\). Completeness follows from finite-group Fourier theory. After a unitary unramified norm twist, the central character can be made one on \(\varpi\), so work on the compact group \(D^\times/\varpi^{\mathbb Z}\). Its smooth class functions with the chosen central covariance are exhausted by functions on finite quotients: average over the normal groups \(1+\mathfrak P_D^m\). Finite-group irreducible characters are a basis on each quotient and on each central isotype. These averages converge in \(L^2\), since locally constant functions are dense. Weyl integration identifies the class-function space with the stated elliptic space; singular elements have measure zero. This proves the basis assertion, including an infinite family of tori in characteristic two.

For a unitary supercuspidal \(\pi_1\), choose a smooth unit vector \(u\) and the compact-mod-centre test
\(f_1(g)=d_{\pi_1}\langle\pi_1(g^{-1})u,u\rangle\).
Schur orthogonality for square-integrable representations gives
\(\pi_2(f_1)=0\) for a different discrete series, and the projection onto \(\mathbb Cu\) for \(\pi_2=\pi_1\). To recall the cross-representation argument, integrate a rank-one coefficient against the second representation, first on compact sets. Products of its two square-integrable coefficients are absolutely integrable by Cauchy–Schwarz. Translating the integral makes it an intertwiner; irreducibility and Schur force zero between inequivalent representations and a scalar in the equal case. Taking a unit coefficient determines that scalar to be \(d_{\pi_1}^{-1}\). Applying it to arbitrary smooth vectors gives the stated operator and trace.

Lemma 2.27 now represents this trace by an actual convergent character integral. For an elliptic \(b\), (2.102) gives
\[
O_b(f_1)=v_E^{-1}\overline{\Theta_{\pi_1}(b)}.
\tag{2.109}
\]
For a regular split \(b\), Iwasawa coordinates express the orbital integral as a \(K\)-average of
\(\int_F\langle\pi_1(bn(x))v,v\rangle\,dx\), up to its nonzero root Jacobian. It is zero by the zero Jacquet module. The full coefficient is compact on the unipotent parameter; the integral and this substitution are absolutely convergent. Weyl integration therefore gives
\[
\int_{\mathcal C}\Theta_{\pi_2}(b)
 \overline{\Theta_{\pi_1}(b)}\,d\mu_{\rm ell}
=\mathbf1_{\pi_1\simeq\pi_2}.
\tag{2.110}
\]
Absolute integrability follows before the substitution from the compact-mod-centre support of \(f_1\) and Lemma 2.27; its orbital version dominates the absolute value of the displayed product. In particular a supercuspidal has elliptic norm one and is orthogonal to every different supercuspidal and every special representation.

For two special representations, their elliptic characters are
\(-\chi(N_Eb)\) by Proposition 2.2 and twisting. They are the negatives of the characters of the corresponding one-dimensional division representations. Division orthogonality proves their remaining inner products and their norm one. The finite discrete-series classification in Lesson 7 leaves exactly these special representations and the supercuspidals. This proves the second assertion. \(\square\)

**Theorem 2.30 — full finite Jacquet–Langlands, all fields and all levels.** The construction \(T\mapsto\pi_T\), with norm characters treated in Lemma 2.26, is the bijection in Theorem 2.1. It has the elliptic sign (2.3), commutes with every norm/determinant twist and dual, and preserves all twisted local \(L\)- and epsilon factors. For paired Haar measures its formal degrees are equal:
\[
d_{\pi_T}=d_T.
\quad\text{In the normalization }\operatorname{vol}(KZ/Z)=1:
\qquad d_{\pi_T}=\frac{q-1}{2}\dim T.
\tag{2.111}
\]
In particular the dimension-volume identity (2.64) holds for every positive-level compact-induction realization, including primitive types in residue characteristic two.

**Proof of the character and degree identities.** First let \(T\) be a noncharacter, and choose unit vectors on both sides. Evaluate (2.103)–(2.104) at \(\lambda I\), \(\lambda\in F^\times\). In multiplicative measures this says
\[
\begin{aligned}
\int_G\phi(\det g)|\det g|
 \langle\pi_T(g^{-1})u,u\rangle
 \psi(\lambda\operatorname{tr}g)\,d^\times g
&=(W\phi)(\lambda^2)\eta(\lambda)^{-1}|\lambda|^{-2},\\
\int_{D^\times}\phi(Nx)|Nx|
 \langle T(x^{-1})u',u'\rangle
 \psi(\lambda\operatorname{trd}x)\,d^\times x
&=-(W\phi)(\lambda^2)\eta(\lambda)^{-1}|\lambda|^{-2}.
\end{aligned}
\tag{2.112}
\]
The vectors need not identify their representation spaces; only their norms are one. Both integrands are compactly supported in the algebra, so their trace-pushforward Fourier transforms are locally constant at \(\lambda=0\) as well. Since \(F^\times\) is dense in \(F\), the opposite-value identity extends to zero.

For completeness, we describe how this identity isolates each elliptic class. Apply Weyl integration and average the coefficient on its conjugacy orbit. The split-torus term is zero as in Lemma 2.29. On an elliptic torus the two averaged coefficients are
\(\Theta_{\pi_T}(b^{-1})/(d_{\pi_T}v_E)\) and
\(\Theta_T(b^{-1})/(d_Tv_E)\), respectively. The former is (2.102); the latter is finite-dimensional Schur averaging on the compact division quotient. Thus (2.112) says that the Fourier transform in the common trace variable of the sum of these two densities is zero, after multiplying by every compact norm test \(\phi\).

Fix \(b_0\in E^\times\) regular, with trace \(t_0\) and norm \(a_0\). A sufficiently small product neighborhood of \((t_0,a_0)\) has both polynomial roots in \(E\), one near \(b_0\), the other near \(b_0^\sigma\), by the simple-root contraction used in Theorem 2.7. Their common quadratic algebra is \(E\). Shrink it so that both characters, \(|a|\) and \(\delta\) are constant on these root neighborhoods. The map
\(b\mapsto(\operatorname{Tr}_E b,N_Eb)\) has nonzero Jacobian there: in the two eigenvalue coordinates its determinant is \(b-b^\sigma\). This statement uses separability and never divides by two.

Take \(\phi\) to be the indicator of the chosen norm ball. Integrate (2.112) in \(\lambda\) against the normalized additive Fourier test of the chosen trace ball, with the phase \(\psi(-\lambda t_0)\). Additive orthogonality restricts the trace to that ball. All other tori disappear, and the two root neighborhoods have equal positive measure. Their common, nonzero factor \(|a_0|\delta(b_0)/(2v_E)\), and their common Jacobian, cancel. We obtain
\[
\frac{\Theta_{\pi_T}(b_0^{-1})}{d_{\pi_T}}
=-\frac{\Theta_T(b_0^{-1})}{d_T}.
\tag{2.113}
\]
This argument uses compact tests throughout, so the trace/norm localization is justified even for wild extensions and characteristic two.

Both characters have elliptic norm one by Lemma 2.29. Since the formal degrees are positive, (2.113) forces \(d_{\pi_T}=d_T\), then \(\Theta_{\pi_T}=-\Theta_T\). Norm-character cases already have this sign, and their degree equality follows from the explicit Steinberg degree and division volume in Section 2.5.

To check the numerical normalization in (2.111), the split self-dual measure gives
\(\operatorname{vol}(K)=(1-q^{-1})(1-q^{-2})\), hence \(\operatorname{vol}(KZ/Z)=1-q^{-2}\).
For \(D=E\oplus E\Pi\), \(\Pi^2=\varpi\), the self-dual additive volume of \(\mathcal O_D\) is \(q^{-1}\). Its unit volume is \(q^{-1}(1-q^{-2})\), since its residue field has size \(q^2\). Divide by the central unit volume \(1-q^{-1}\) and count the two valuation cosets modulo \(F^\times\). The division quotient volume is \(2(q+1)/q^2\). Rescaling both group measures by \((1-q^{-2})^{-1}\) gives exactly
\(\operatorname{vol}(D^\times/F^\times)=2/(q-1)\).
Finite-dimensional Schur orthogonality gives \(d_T=\dim T/\operatorname{vol}(D^\times/F^\times)\), proving (2.111). Combine it with Theorem 2.16 to get (2.64) for every compact type, without assuming a classification by quadratic characters.

**Proof of bijectivity and uniqueness.** If two different division representations had the same image, their elliptic characters would be equal. Their orthogonality contradicts that equality. The images of all division characters form an orthonormal basis of the elliptic space, by Lemma 2.29 and the sign just proved. If a split discrete series were absent from the image, its elliptic character would be orthogonal to that whole basis by the split orthogonality statement. It would be zero in this Hilbert space, contrary to its norm one. Thus the map is surjective. The same orthogonality proves that the sign characterizes its image uniquely.

The construction's norm/determinant twist and dual comparisons were proved in Theorem 2.25, with every twisted factor in (2.88); Lemma 2.26 handles the special cases. A unitary central character makes every division representation unitary by compact averaging, and Theorem 2.25 gives unitary supercuspidals. The special construction gives the unitary Steinberg twists. Removing a nonunitary central modulus by a norm/determinant quasicharacter twist gives the essentially discrete-series statement with the same identities. This completes Theorem 2.1 at finite places, including all positive levels and residue characteristic two. \(\square\)

**Corollary 2.31 — every finite matching pair has the spectral identities.** For every matching pair \((f,f')\) in Theorem 2.10, not merely a specially chosen pair, and every division irreducible \(T\),
\[
\operatorname{tr}\pi_T(f)=-\operatorname{tr}T(f').
\tag{2.114}
\]
Every principal-series trace of \(f\) is zero. For a norm character the accompanying one-dimensional split trace has the opposite sign to the special trace:
\[
\operatorname{tr}(\chi\circ\det)(f)
=\operatorname{tr}(\chi\circ N)(f'),\qquad
\operatorname{tr}(\mathrm{St}\otimes\chi)(f)
=-\operatorname{tr}(\chi\circ N)(f').
\tag{2.115}
\]
The scalar constraint is \(f'(z)=-f(zI)\), as in Lemma 2.11.

**Proof.** Lemma 2.27 represents every split trace by integration against its character; the division trace is ordinary finite-dimensional integration. Weyl integration has identical elliptic discriminants, torus measures and orbital matching. The split orbital integrals of \(f\) are zero, so only elliptic classes contribute. Insert the negative character identity of Theorem 2.30 to obtain (2.114). The principal character is zero on elliptic classes and the split orbital terms vanish, so its trace is zero. The one-dimensional split and division characters are both \(\chi\) of the common norm and have positive equality; the special sign gives (2.115). The value at a scalar is the already proved every-pair germ, not a consequence of neglecting that class in Weyl integration. No extra singular-supported character term is present, by Lemma 2.27. \(\square\)

The construction proves finite local existence, uniqueness, the character distribution, formal degrees and smooth/scalar/spectral transfer. For the Fourier route compare Jacquet–Langlands, Lemma 13.1.1 and Proposition 4.5; for the elliptic pairing compare Lemmas 15.3–15.4 and Proposition 15.5. The construction and all-field singular estimates above are written here, including the characteristic-two counting argument. Global automorphic realization still requires the full comparison below.

## 3. The global correspondence and the trace comparison

Let \(D\) be a nonsplit quaternion algebra over \(\mathbb Q\), and let \(S=\operatorname{Ram}(D)\), including the real place when appropriate. Fix a unitary idele-class character \(\omega\). By Lesson 17, the central quotient of the automorphic domain for \(D^\times\) is compact; its automorphic representations belong to the discrete spectrum. The one-dimensional constituents have the form \(\chi\circ\operatorname{nrd}\), with \(\chi^2=\omega\).

**Theorem 3.1 — global Jacquet–Langlands.** On excluding those one-dimensional constituents, there is an injection
\[
\operatorname{JL}_D:
\operatorname{Aut}_\omega(D^\times)_{\dim>1}
\longrightarrow
\operatorname{Cusp}_\omega(\mathrm{GL}_2(\mathbb A)).
\tag{3.1}
\]
It satisfies
\[
\pi_v=\begin{cases}
\pi'_v,&v\notin S,\\
\operatorname{JL}_{\mathbb Q_v}(\pi'_v),&v\in S,
\end{cases}
\qquad\pi=\operatorname{JL}_D(\pi').
\tag{3.2}
\]
At split places we fix an algebra isomorphism to \(M_2(\mathbb Q_v)\); another choice differs by inner conjugation and gives the same representation class. The image of (3.1) is exactly the cuspidal representations with discrete-series local components at every place of \(S\). Every automorphic irreducible of \(D^\times\) has multiplicity one. Equality at almost all places implies equality globally.

A modern reference allowing real ramification is Badulescu–Renard, §18.1, Theorem 18.1(a)–(b) in the consulted author preprint; its introductory Theorem 1.4 states the same result. That theorem is formulated for the entire discrete spectrum and the extended unitary local transfer. In degree two, its noncuspidal split-side constituents are the determinant characters, as in Lesson 16, Theorem 5.3. They correspond to the quaternion norm characters. Removing these leaves the cuspidal assertion (3.1). For cuspidal representations, the local genericity from Lesson 14, Theorem 2.1 makes extended compatibility at division places precisely the discrete-series condition of (3.2). We do not assert that every cuspidal representation of a higher-rank inner form transfers to a cuspidal representation.

The original references are Jacquet–Langlands, Theorems 14.4 and 16.1. Theorem 14.4 has a split-place infinite-dimensional hypothesis, while §16 explicitly presents the analytic trace comparison with formal qualifications. Those qualifications are not a proof of the general analytic theorem. Sections 3.3–3.6 give the rational quaternion proof: Poisson summation computes the paired volumes, rank-one truncation gives the trace comparison, and positive outside trace sums give existence and multiplicity.

If \(D=M_2(\mathbb Q)\), the correspondence on **cuspidal** automorphic representations is simply the identity. The restriction is essential: an infinite-dimensional Eisenstein representation is not made cuspidal by an identity map.

### 3.1. What the comparison must accomplish

For trivial central character, put \(H'=D^\times/\mathbb G_m\) and \(\Gamma'=H'(\mathbb Q)\). Its adelic quotient is compact. For a factorizable projective test, Lesson 18 writes its trace as
\[
\sum_{\pi'}m(\pi')\operatorname{tr}\pi'(f')
=\sum_{[\gamma']}\operatorname{vol}
\bigl(\Gamma'_{\gamma'}\backslash H'_{\gamma'}(\mathbb A)\bigr)
O_{\gamma'}(f'),
\tag{3.3}
\]
where the classes are in \(\Gamma'\), and orbital integrals and centralizers are projective. A prescribed nontrivial central character uses the corresponding equivariant kernel on the central quotient, as in Lesson 17. The corresponding split quotient is noncompact. Its trace formula requires truncation, the continuous-spectrum terms and the residual terms of Lesson 16. One cannot apply the compact formula to that quotient unchanged.

The comparison has four jobs. First choose transferred local tests, using (1.2) and the analytic transfer theorem. Next compare geometric terms, including the singular terms determined by regular orbital-integral germs. Then compare the resulting spectral distributions: local character relations identify the division-place contributions, and the norm-character terms must be accounted for separately. Finally vary the spherical tests outside a finite set. Their eigenvalues specify the unramified components; strong multiplicity one separates the global representations. The converse theorem gives an alternative route in settings where the transferred twisted \(L\)-functions satisfy its analytic hypotheses. Neither route reduces to just an equality of finite-dimensional traces.

Arthur, §25, especially Theorems 25.5–25.6 and equation (25.28), explains the invariant geometric and spectral comparisons. Theorem 3.4 proves the noncompact trace identity used here, and Theorem 3.5 compares it with the compact formula.

### 3.2. Identity values and the minus sign

The identity is singular, so it is not a regular elliptic class in (1.2). Nevertheless, the regular transfer theorem also constrains the **value of a transferred test function at the identity**. With the paired measures used in Arthur, §25, the identity preceding the Plancherel argument in the proof of Lemma 25.2 is, in our notation,
\[
f'(1)=e(D^\times)f(1)=-f(1).
\tag{3.4}
\]
Here \(e(D^\times)=(-1)^{1-0}=-1\): the semisimple split ranks of the split group and the division group differ by one. The corresponding spectral identity in Theorem 25.1(b) is
\[
\operatorname{tr}\pi(f)=-\operatorname{tr}\pi'(f').
\tag{3.5}
\]
At finite places, (3.4) is proved directly for every matching pair in Lemma 2.11, with the paired measures calculated in (2.37). The full scalar germ (2.47) includes the nontrivial unipotent orbital integral; it is not just an evaluation on a specially chosen transfer. The real instance of (3.4) and the general spectral identity (3.5) still use the transfer and Plancherel/formal-degree normalization theorem. Proposition 2.12 independently verifies the special representation's formal degree, and Theorem 2.16 with Proposition 2.18 gives every compact-induction degree and the two positive-level subgroup volumes. Corollary 2.17 identifies the exact dimension equality still needed for a proposed positive-level pair. Independent Haar choices must be reconciled with these explicit paired measures; the compact trace formula alone does not establish these relations.

The compact formula makes the relevance of (3.4) visible: its identity contribution is \(\operatorname{vol}(X)f(1)\), by Lesson 18, equation (3.10). The locally transferred value therefore has the same relative sign as the spectral transfer. Globally, quaternion reciprocity makes \(|S|\) even, so
\[
\prod_{v\in S}e(D_v^\times)=(-1)^{|S|}=1.
\tag{3.6}
\]
This explains how local negative character relations fit a global correspondence with positive multiplicities.

### 3.3. A volume identity from two theta integrals

We first fix the measures needed by the global comparison. This is a comparison over \(\mathbb Q\); the finite local results above retain their full local-field generality. Let \(\psi\) be the standard character of \(\mathbb Q\backslash\mathbb A\), with real component \(e^{2\pi i x}\). On either four-dimensional algebra use the self-dual additive measure for \((x,y)\mapsto\psi(\operatorname{trd}(xy))\). Put
\[
 d^\times x_v=\alpha_v|\operatorname{nrd}x_v|_v^{-2}\,dx_v,
 \quad
 \alpha_p=((1-p^{-1})(1-p^{-2}))^{-1},
 \quad\alpha_\infty=(2\pi^2)^{-1}.
\tag{3.7}
\]
Use the same scalar-subgroup measures on both sides: \(\mathbb Z_p^\times\) has multiplicative volume one, and the real scalar measure is \(dz/|z|\). These are the paired measures of (2.37) and (2.23)–(2.24). At a finite division place they give projective volume \(2/(p-1)\); at a real division place they give volume two. At split finite places \(\mathrm{GL}_2(\mathbb Z_p)\) has volume one. The real split measure is \(1/(2\pi)\) times the quotient normalization of Lesson 1, Section 2. Thus that lesson's volume \(\pi/3\) becomes \(1/6\).

**Lemma 3.2 — equal global quotient volumes.** For every nonsplit quaternion algebra \(D/\mathbb Q\), in (3.7)'s measures,
\[
 \operatorname{vol}\bigl(D^\times(\mathbb Q)Z(\mathbb A)
             \backslash D^\times(\mathbb A)\bigr)
 =\operatorname{vol}\bigl(G(\mathbb Q)Z(\mathbb A)
             \backslash G(\mathbb A)\bigr)=\frac16.
\tag{3.8}
\]

**Proof.** We will compare residues of scalar matrix integrals; this avoids using a quaternion Tamagawa-number formula as a prerequisite. On \(M_2(\mathbb A)\), take
\(\Phi_M=\prod_{i,j}\phi(x_{ij})\), where \(\phi_p=1_{\mathbb Z_p}\) and \(\phi_\infty(x)=e^{-\pi x^2}\). Its additive integral and its value at zero are both one. Write
\[
 \Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
 Z_M(s)=\int_{G(\mathbb A)}\Phi_M(g)
                           |\det g|^{s+1/2}d^\times g.
\]
For \(\operatorname{Re}s>3/2\), Iwasawa integration gives
\[
 Z_M(s)=\frac1{2\pi}\Lambda(s-1/2)\Lambda(s+1/2),
 \qquad\operatorname*{Res}_{s=3/2}Z_M(s)=\frac1{12}.
\tag{3.9}
\]
Here is the measure calculation. Write \(g=n(x)\operatorname{diag}(a,b)k\), with compact Haar measure of total mass one. The matrix test is right compact invariant. The integral in \(x\) is
\(\int\phi(xb)dx=|b|^{-1}\), and the lower-left entry contributes \(\phi(0)=1\). The Iwasawa modulus is \(|a/b|^{-1}\). The resulting powers of \(|a|,|b|\) are \(s-1/2,s+1/2\), giving the two scalar Tate integrals. The finite Iwasawa constants are one, since the multiplicative units and the matrix compact subgroup both have volume one. At the real place the additive Jacobian of
\((x,a,b,\theta)\mapsto n(x)\operatorname{diag}(a,b)r(\theta)\)
is \(|b|^2\). Allowing both signs of \(a,b\) and both components of \(\mathrm O(2)\), its fourfold diagonal-sign redundancy makes the raw matrix Iwasawa constant \(\pi\) when compact measure is probability measure. Multiplication by \(\alpha_\infty\) gives \(1/(2\pi)\). This proves the first formula. The scalar Poisson proof of the Tate integral gives \(\operatorname{Res}_{u=1}\Lambda(u)=1\), and \(\Lambda(2)=\pi/6\); hence the residue is \(1/12\). These scalar identities are also the ones used in Lesson 16, Proposition 5.1.

Choose an adelic Schwartz function \(\Phi_D\) on \(D(\mathbb A)\). At a split place use \(\Phi_M\) after fixing an algebra isomorphism. At a finite division place use \(1_{\mathcal O_D}\). If the real place is division, use \(e^{-2\pi\operatorname{nrd}x}\). In quaternion coordinates the trace pairing has determinant of absolute value sixteen, so its self-dual additive measure is four times ordinary four-dimensional Lebesgue measure. The last Gaussian consequently has integral one. At a finite division place \(\mathcal O_D\) has self-dual additive volume \(p^{-1}\), as calculated in the integer-ring example following Lemma 2.26. Therefore
\[
 H_D:=\widehat\Phi_D(0)=\prod_{p\in\operatorname{Ram}_f(D)}p^{-1}>0.
\]
Initially define
\(Z_D(s)=\int_{D^\times(\mathbb A)}\Phi_D(x)
|\operatorname{nrd}x|^{s+1/2}d^\times x\).
The Euler products for \(Z_D\) and \(Z_M\) differ at only the ramified places. Each local integral is holomorphic in a neighborhood of \(s=3/2\). For our matrix tests the local Iwasawa calculation in (3.9) gives convergence for \(\operatorname{Re}s>1/2\): the two scalar exponents are \(s-1/2\) and \(s+1/2\). At a finite division place, shell integration converges for \(\operatorname{Re}s>-1/2\); at the real division place the radial Gaussian integral has the same region. These calculations also justify differentiation in a neighborhood of \(3/2\). At the critical point the norm weight in the additive integral disappears, so exactly
\[
 Z_{D,v}(3/2)=\alpha_v\widehat\Phi_{D,v}(0),
 \qquad Z_{M,v}(3/2)=\alpha_v\widehat\Phi_{M,v}(0).
\]
For the finite division test, shell integration gives
\[
 Z_{D,p}(s)=\frac{1}{(p-1)(1-p^{-(s+1/2)})},
 \quad
 \frac{Z_{D,p}(s)}{Z_{M,p}(s)}
       =\frac{1-p^{-(s-1/2)}}{p-1}.
\]
At a real division place radial integration gives
\(Z_{D,\infty}(s)=2(2\pi)^{-s-1/2}\Gamma(s+1/2)\).
The split integral in (3.9) and the gamma duplication identity give
\(Z_{D,\infty}(s)/Z_{M,\infty}(s)=s-1/2\).
These formulas verify the critical ratios directly, including the real one. The denominator is positive at the critical point. Thus the finite product of local ratios is holomorphic near this point, has value \(H_D\), and (3.9) implies
\[
 \operatorname*{Res}_{s=3/2} Z_D(s)=\frac{H_D}{12}.
\tag{3.10}
\]
No division representation or correspondence is used in this calculation.

We now compute that same residue by unfolding. Put
\(X_D=D^\times(\mathbb Q)Z(\mathbb A)\backslash D^\times(\mathbb A)\).
It is compact by Lesson 17, Theorem 3.3. The fibre of
\(D^\times(\mathbb Q)\backslash D^\times(\mathbb A)\to X_D\)
is \(C=\mathbb Q^\times\backslash\mathbb A^\times\). With the scalar measures above, its norm-one subgroup has volume one and its norm measure is \(dt/t\). This follows directly by making each finite valuation zero with a rational number and then using the real sign to divide by \(-1\); the remaining finite units carry probability measure. A compact set of representatives for \(X_D\) exists: choose finitely many relatively compact local sections of the quotient and take their union. We may therefore write the unfolded integral as an integral over representatives \(h\) in such a compact set and over \(z\in C\), with integrand
\[
 |\operatorname{nrd}h|^{s+1/2}|z|^{2s+1}
       \sum_{\gamma\in D(\mathbb Q),\ \gamma\ne0}\Phi_D(z\gamma h).
\tag{3.11}
\]
Unfolding is absolute in the initial half-plane. Every nonzero rational quaternion is invertible, which is precisely where the division hypothesis is used.

Poisson summation on the four-dimensional rational vector space \(D\) gives, as \(t=|z|\to0\),
\[
 \sum_{\gamma\ne0}\Phi_D(z\gamma h)
 =t^{-4}|\operatorname{nrd}h|^{-2}H_D-\Phi_D(0)
       +O_A(t^A)
\tag{3.12}
\]
for every \(A\), uniformly for the compact representatives \(h\) and the compact norm-one part of \(z\). Indeed right multiplication by \(h\) has additive determinant \(|\operatorname{nrd}h|^2\). The rational lattice has covolume one in the global self-dual trace measure: in any rational basis the determinant is rational, and the product formula cancels its local changes of covolume. The nonzero dual-lattice terms decrease rapidly; a common finite denominator lattice and the real Schwartz bounds prove uniformity on the two compact sets. The same lattice bounds give rapid decrease of the original nonzero sum as \(t\to\infty\).

Split the norm integral at one. All terms except the first in (3.12) are holomorphic near \(s=3/2\); the large-norm part is entire there. The first gives
\[
 \operatorname*{Res}_{s=3/2}Z_D(s)
 =\frac12 H_D\operatorname{vol}(X_D),
\tag{3.13}
\]
since \(\int_0^1t^{2s-3}dt/t=(2s-3)^{-1}\) and
\(|\operatorname{nrd}h|^{s-3/2}=1\) at the pole. Equating (3.10) and (3.13) and cancelling \(H_D\) proves (3.8). The argument applies equally to definite and indefinite quaternion algebras. \(\square\)

### 3.4. Removing the cusp boundary

A test in the fixed-central-character algebra satisfies
\(f_v(zg)=\omega_v(z)^{-1}f_v(g)\) and has compact support modulo the centre. At infinity it is smooth and finite under left and right \(\mathrm O(2)\); at finite places it is locally constant. Measures on compact groups in this subsection are probability measures. Define its averaged constant term by
\[
 C_{f_v}(a)=\int_{K_v}\int_{F_v}
                   f_v(k^{-1}a n(x)k)\,dx\,dk,
 \qquad a=\operatorname{diag}(\alpha,\beta).
\tag{3.14}
\]
The integral is smooth, or locally constant, as a function of the diagonal entries away from zero. On a compact set of such entries, compact support bounds \(x\) uniformly. This proves the assertion also at \(\alpha=\beta\).

**Lemma 3.3 — transfer has zero averaged constant term.** Every split test matching a division test at a ramified place satisfies \(C_{f_v}(a)=0\) for every \(a\).

**Proof.** For \(\alpha\ne\beta\), conjugation by \(n(x)\) sends \(a\) to
\(a n((1-\beta/\alpha)x)\), up to replacing \(x\) by its negative. The Iwasawa integration formula for the split-torus quotient therefore expresses its ordinary orbital integral as a nonzero measure constant times
\(|1-\beta/\alpha|^{-1}C_{f_v}(a)\). That orbital integral is zero by the definition of matching. Hence the constant term is zero on all distinct diagonal entries. Continuity gives zero at equal entries too. This applies at the real place without an assertion about individual unipotent matrices. \(\square\)

We next prove the precise trace formula needed here. Write \(X=G(\mathbb Q)Z(\mathbb A)\backslash G(\mathbb A)\). For an elliptic rational matrix \(\gamma\), let \(E_\gamma=\mathbb Q[\gamma]\) and \(T_\gamma=E_\gamma^\times\). Use the same quotient measure on this torus in the split and quaternion groups. Set
\[
 a(\gamma)=\frac{\operatorname{vol}
  (T_\gamma(\mathbb Q)Z(\mathbb A)\backslash T_\gamma(\mathbb A))}
 {s(\gamma)},\qquad
 s(\gamma)=|\{c\in\mathbb Q^\times:c\gamma\text{ is conjugate to }\gamma\}|.
\tag{3.15}
\]
The denominator is one if \(\operatorname{tr}\gamma\ne0\), and two if its trace is zero. Indeed equal characteristic polynomials imply respectively \(c=1\), or \(c^2=1\); a trace-zero quadratic field generator is conjugate to its negative. This factor prevents double counting when ordinary conjugacy classes are taken modulo rational scalars. It also describes the possible disconnected projective centralizer correctly. The elliptic sum below uses one representative for each such class.

**Theorem 3.4 — the trace formula with two vanishing constant terms.** Let \(f=\bigotimes_v f_v\), spherical outside a finite set, and suppose (3.14) vanishes at two different places. Then
\[
 \begin{aligned}
 \operatorname{tr}R_{\mathrm{disc}}(f)
 &=\sum_{\pi\ \mathrm{cuspidal}}m(\pi)\operatorname{tr}\pi(f)
       +\sum_{\chi^2=\omega}\operatorname{tr}(\chi\circ\det)(f)\\
 &=\operatorname{vol}(X)f(1)
       +\sum_{\gamma\ \mathrm{elliptic}}a(\gamma)O_\gamma(f).
 \end{aligned}
\tag{3.16}
\]
The spectral sum is absolutely convergent; only finitely many elliptic classes contribute. The continuous spectrum, the split semisimple boundary and the unipotent finite part contribute zero.

**Proof.** We give the convergence argument along with the two boundary calculations. Work at a finite level fixing every finite test and at the finitely many real compact weights occurring in \(f\). Lessons 1 and 4 realize this as a finite collection of congruence quotients with finitely many cusp collars. At sufficiently large height their translates are disjoint, by the lower-left-entry reduction estimate in Lesson 4, Lemma 1.2. Write \(X_T\) for the core obtained by deleting height \(y>e^T\) in each collar.

We use the piecewise orthogonal truncation \(P_T\): on each outer collar it subtracts the additive constant term, and on the core it is the identity. The disjoint collar coordinates make this a self-adjoint projection on \(L^2(X,\omega)\). On Eisenstein series it is exactly the truncation of Lesson 16, Lemma 6.3. On cusp forms it is the identity. On a residual character its norm tends to the full norm, since the removed constant tail has volume \(O(e^{-T})\).

Here are the two estimates needed for traces. First the cuspidal Casimir has polynomial eigenvalue count, not merely compact resolvent. To check this directly, fix a rotation weight \(m\), set \(u=\log y\), and remove the \(y^{1/2}\) half-density. The nonconstant cusp Fourier modes of the weight Laplacian are
\(-\partial_u^2+c_n^2e^{2u}+b_ne^u+1/4\), with
\(|c_n|\ge c|n|\) and \(|b_n|\le C_m|c_n|\).
Completing the square bounds them below by
\(-\partial_u^2+\tfrac12c_n^2e^{2u}-C_m\).
Neumann bracketing first separates the compact core and collars and then divides each collar into unit \(u\)-intervals. The core is covered by finitely many coordinate rectangles; uniform ellipticity and the elementary Neumann Fourier basis on rectangles bound its eigenvalue count by \(C(1+\lambda)\). On the interval beginning at \(j\), the radial Neumann frequencies are proportional to \(k\ge0\), so the remaining count is bounded by
\[
 C\sum_{j\ge0}\#\{(n,k):n\ne0,\ k\ge0,
           1+k^2+n^2e^{2j}\le C(1+\lambda)\}
 \le C'(1+\lambda).
\tag{3.17}
\]
Indeed there are at most \(C\sqrt{1+\lambda}e^{-j}\) nonzero \(n\)'s and at most \(C\sqrt{1+\lambda}\) \(k\)'s; the sum of \(e^{-j}\) is bounded. Shifted cusp frequencies from a unitary phase have the same bound. The cusp condition excludes the zero frequency. The comparison is valid on the quadratic-form domain: separating intervals relaxes boundary matching and can only lower eigenvalues. The fixed weight's lower-order terms were absorbed in \(C_m\). Tensoring the finitely many compact fibres changes only the constant. Thus a sufficiently large inverse power of the positive shifted Casimir is trace class. Integrating by parts in the real test proves absolute cuspidal trace convergence and continuity in its smooth seminorms. The residual sum is finite at this level by Lesson 16, Theorems 5.3 and 6.1.

Second, truncated periodized kernels have a rapid nonconstant tail. For two points sufficiently far out in collars, the arithmetic support estimate of Lesson 4, Lemma 2.1 forces every contributing matrix to carry one cusp to the other. Its lower-left entry is zero; the compact finite support permits only finitely many diagonal ratios. If no such cusp correspondence exists the kernel is zero. For each remaining ratio the height quotient is bounded above and below by the real support. The upper-right rational entries then form a fixed translation lattice. Their periodization is a sum of the form
\(\sum_{r\in\ell\mathbb Z}\varphi((r+x'-x)/y)\),
with \(y\) comparable to both heights, a fixed \(\ell>0\), and \(\varphi\) in a bounded family of smooth compact functions. Poisson summation makes its nonzero frequencies
\((y/\ell)\widehat\varphi(ky/\ell)\), \(k\ne0\).
Repeated integration by parts gives their summed absolute value at most \(C_N y^{1-N}\) for every \(N\). The same bound holds for derivatives and for the finitely many matrix entries of the compact fibres. Truncation removes precisely the zero frequency. The kernel vanishes unless the two deep heights are comparable, so integration against the two cusp densities \(dx\,dy/y^2\) proves that
\(P_T R(h_1)\) and \(R(h_2)P_T\) are Hilbert–Schmidt for smooth compact tests. Their product is trace class. On its diagonal the part outside \(X_T\) is bounded by \(C_N y^{1-N}\) and has integral \(O(e^{-NT})\). This proves, without a uniform unsmoothed Eisenstein bound, that the geometric trace of \(P_T R(f)P_T\) differs from the core integral of \(K_f(x,x)\) by a quantity tending to zero.

Initially take \(f\) to be a convolution of two smooth compact tests. The product-kernel identity in Lesson 18, Lemma 3.1 now applies to \(P_T R(f)P_T\), on the entire quotient. The spectral decomposition of Lesson 16, Theorem 6.1 computes the same trace. For a positive convolution all spectral interchanges follow from its Hilbert–Schmidt norm and Tonelli; polarization gives a general product. At this level only finitely many compact torus labels and compact-model basis vectors occur. We may first restrict \(|t|\le A\) and then remove the restriction using that Hilbert–Schmidt bound. The continuous term is exactly the pairing of the truncated Eisenstein series, with no replacement of a core norm by an unproved tail estimate. The cuspidal trace is unchanged, and the residual trace tends to its full value. This is a justified kernel calculation, rather than a formal subtraction of infinite traces.

We compute the geometric core integral. Separate scalar, elliptic, split semisimple and nontrivial unipotent rational classes. Scalar matrices give \(\operatorname{vol}(X_T)f(1)\), tending to the first term on the right of (3.16). Elliptic classes unfold to the orbital integral and the coefficient (3.15). Their torus quotient is compact by the bounded-lattice proof of Lesson 17, Theorem 3.3 applied to the quadratic field \(E_\gamma\). For clarity, replace the rank-four order there by a rank-two order in \(E_\gamma\), and replace reduced norm by field norm. Multiplication now has determinant equal to that norm rather than its square. On the module-one group the lattices still have fixed covolume, and the product formula still bounds their shortest nonzero vector away from zero. Bounded bases give finitely many integral right-action tuples; their commutants are left multiplications, and a nonzero rational field element proves rationality of the comparing multiplier. Thus \(E_\gamma^\times(\mathbb Q)\backslash E_\gamma^\times(\mathbb A)^1\) has compact representatives. A scalar idele adjusts any module by its square, so its quotient by \(Z(\mathbb A)\) is compact too. For a fixed regular matrix, the conjugacy orbit is closed and its parametrization by the torus quotient is proper on the support of a compact test: a cyclic vector gives a local inverse in trace/norm coordinates, and finitely many such charts cover that support. This also proves local orbital-integral continuity in the test.

There are only finitely many contributing rational polynomials up to scalar. Outside a fixed finite set, integrality of a representative in the projective maximal compact group forces the determinant valuation to be even. Multiply by a rational scalar to put the determinant in one of finitely many signed squarefree classes supported in that finite set. The finite support conditions then bound denominators of the trace in a fixed rational lattice; the real support bounds its absolute value. Thus only finitely many traces occur. The same argument bounds split rational eigenvalue ratios. At almost every place each of these regular polynomials has integral unit discriminant and its local orbital integral is the compact-unit orbital integral. The remaining conjugator supports are compact modulo their torus. This proves absolute convergence of each elliptic contribution, and allows its truncated integral to tend to its full value.

For a split semisimple element \(a=\operatorname{diag}(\alpha,\beta)\), \(\alpha\ne\beta\), there are two rational eigenlines. In Iwasawa coordinates, deleting their two cusp ends leaves a radial interval whose length is
\(2T-\sum_v\log\lambda_v(n_v)\), up to a fixed constant depending only on the choice of initial collars. Here \(\lambda_v(n_v)\) is the absolute-value ratio of the diagonal entries in the Iwasawa decomposition of \(w n_v\), where \(w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\). To verify the interval, the first end is \(|a_1/a_2|>e^T\); the second is \(|a_1/a_2|<e^{-T}\prod_v\lambda_v(n_v)\). Integrating \(d\log|a_1/a_2|\) between them gives exactly the stated length. The fixed collar constant multiplies the ordinary orbital integral.

After the remaining \(n,k\) integrals are factored, the length term is a constant times
\(T\prod_v U_v(a,f_v)\), and its finite part is a sum of terms
\[
 W_v(a,f_v)\prod_{w\ne v}U_w(a,f_w),
\quad
 U_v(a,f_v)=\int_{K_v,N_v}f_v(k^{-1}n^{-1}a n k)\,dn\,dk.
\tag{3.18}
\]
The local \(W_v\) includes the one logarithmic weight \(\log\lambda_v(n)\). For this fixed regular \(a\), compact support bounds \(n\), so these local weighted integrals are finite. Changing \(n\) to \((1-\beta/\alpha)n\) identifies \(U_v\) with a nonzero constant times \(C_{f_v}(a)\). At the two assumed places it is zero. Every term in (3.18), and the length term, consequently vanishes. This argument includes the two eigenlines' rational interchange; its factor of two multiplies zero.

For the unipotent part put
\(\varphi_v(x)=\int_{K_v}f_v(k^{-1}n(x)k)dk\).
It is an additive Schwartz function, and
\(\int\varphi_v(x)dx=C_{f_v}(1)=0\) at the same two places. Unfolding the unique rational nontrivial unipotent class and making the change \(x=(a_1/a_2)^{-1}\) gives the Mellin integral
\[
 U_f(z)=\prod_v Z_v(1+z,\varphi_v)
       =\Lambda(1+z)\prod_v\theta_v(z),\qquad
 \theta_v(z)=\frac{Z_v(1+z,\varphi_v)}{L_v(1+z,1)}.
\tag{3.19}
\]
A fixed positive measure constant from the Iwasawa coordinates is immaterial here. Almost all \(\theta_v\) are one. At zero, \(L_v(1,1)\) is finite and nonzero, so
\(\theta_v(0)\) is a nonzero measure constant times \(C_{f_v}(1)\). All local functions are holomorphic near zero. For finite places this follows by summing the constant small-ball part as a geometric series; at infinity it follows from the compact smooth integral at exponent one.

To relate (3.19) to the height cutoff, unfold its multiplicative integral as
\(\int_C\sum_{r\in\mathbb Q^\times}\varphi(rz)|z|^{1+z_0}d^\times z\), with \(z_0\) the Mellin parameter. Poisson summation gives its small-norm sum as
\(|z|^{-1}\widehat\varphi(0)-\varphi(0)\) plus a rapidly decreasing remainder. The zero Fourier term is the sole pole at \(z_0=0\); truncating the norm integral subtracts that pole and adds its coefficient times the logarithmic cutoff. Thus the remaining unipotent term is the finite part of (3.19) at zero. If
\(\Lambda(1+z)=\lambda_{-1}/z+\lambda_0+O(z)\), that finite part is
\[
 \lambda_0\prod_v\theta_v(0)
 +\lambda_{-1}\sum_v\theta_v'(0)
                          \prod_{w\ne v}\theta_w(0).
\tag{3.20}
\]
Both expressions are zero because there are two zero factors. The pole coefficient is zero too. The subtracted \(\varphi(0)\) term has an integrable norm tail tending to zero. Repeated integration by parts in the real additive Fourier transform bounds all nonzero Poisson tails by an arbitrarily large inverse power of the cutoff; the finite lattice denominators remain fixed. This justifies the limit, including the non-absolutely convergent raw unipotent sum. There is no surviving distribution supported at the scalar set.

We finally compute the spectral boundary. The common constant rescaling of the quotient measure in (3.7) scales the truncated pairing and the spectral-kernel coefficient reciprocally; it cancels in the trace. Use Lesson 16, Lemma 6.3 with \(s=r=it\), its unitary scattering and its full-axis packet measure \(dt/(4\pi)\). The limit of the first two boundary terms is
\(2T\,1-M(it)^{-1}M'(it)\). The mixed terms are the two reflected exponentials divided by \(2it\). The first term multiplies \(\operatorname{tr}I(it,f)\). The compact-model diagonal-kernel formula is its multiplicative Fourier transform of (3.14); hence every local principal-series trace is zero at either of the specified places. The linear term is therefore identically zero.

Normalize the local intertwiners as in Lesson 16, Theorem 4.2 and the explicit local factors in Lessons 7 and 11, and write
\(M(s)=m(s)\bigotimes_v R_v(s)\) on each inducing pair. The scalar \(m\) is meromorphic, unitary and nonzero on the unitary axis after removable points are filled. Differentiating this finite nontrivial tensor product gives
\[
 \begin{aligned}
 \operatorname{tr}(M^{-1}M'I(f))
 &=\frac{m'}m\prod_v\operatorname{tr}I_v(f_v)\\
 &\quad+\sum_v
 \operatorname{tr}(R_v^{-1}R_v'I_v(f_v))
                 \prod_{w\ne v}\operatorname{tr}I_w(f_w).
 \end{aligned}
\tag{3.21}
\]
Only finitely many local derivative terms occur: the normalized spherical intertwiner is the identity on the spherical line at every other place. The identity holds first away from possible local removable points and then there by continuity. Each term is exactly zero, with two vanishing local traces. We cancel it before removing a spectral cutoff, so no unproved growth bound for a global logarithmic derivative is required.

For completeness the reflected terms really have the claimed limit. On the finite compact-model space, unitarity gives \(\|M(it)\|=1\). Integration by parts in the compact real test with the scalar Casimir eigenvalue \(1/4+t^2\) gives
\(\|I(it,f)\|\le C_N(1+t^2)^{-N}\) for every \(N\). Thus the reflected trace amplitude is integrable. Away from zero, divide by \(t\) and apply Fourier inversion or the Riemann–Lebesgue lemma. Near zero, it is smooth by the proved regularity of \(M\); subtract its value at zero. The remaining quotient is integrable. The only limiting contribution is the familiar integral of \(\sin(2Tt)/t\), times the trace of \(M(0)I(0,f)\), with its factor \(1/4\). That trace is zero. The exchanged inducing labels have no diagonal block unless they are equal. On an equal pair, \(I_v(\chi_v,\chi_v)\) is irreducible at every place, by Lessons 7 and 11; its normalized self-intertwiner is scalar, by Schur's lemma. The global trace then factors into scalar multiples of the same local principal traces, at least two of which vanish. This proves cancellation of the endpoint as well as of the derivative integral. The truncated-kernel and absolute discrete-trace estimates above justify the spectral limit as the discrete trace, with no omitted continuous or residual part. The residual part has been retained on the left of (3.16).

To remove the initial convolution restriction, at the finitely many real weights convolve with a common approximate identity obtained from a smooth compactly supported Fourier multiplier of the shifted Casimir. Finite propagation and the smooth estimates in Lemma 2.21 give compact kernels, with uniformly bounded support, converging to the identity on smooth vectors. Choose the same multiplier on every selected weight. On every principal series it is the same scalar times the selected compact-type projection. The local principal trace remains zero; multiplicative Fourier inversion of its compact-model diagonal kernel consequently preserves (3.14). Finite-place factors stay fixed. The resulting tests are convolutions, converge to \(f\) in every smooth seminorm, and retain the two zero constant terms. Absolute discrete trace convergence follows from the first estimate, and the finite geometric sum is continuous by the orbit-chart argument. Taking the limit proves (3.16) for the stated test class. \(\square\)

This proof uses the complete spectral decomposition already established in Lesson 16 and proves the geometric truncation and its cancellation here. Jacquet–Langlands, §16, printed pages 273–290, supplies the historical boundary-term comparison. The formal qualifications of that exposition are not being used as a substitute for these kernel, norm and limiting arguments.

### 3.5. Equality of the two discrete traces

**Theorem 3.5 — global trace transfer.** At every \(v\in S\) choose a matching pair \((f_v,f'_v)\) from Theorems 2.10 and 2.22. At every other place use the same test through the chosen split algebra isomorphism. Assume the real test is compact-group finite. Then
\[
 \operatorname{tr}R_{\mathrm{disc}}(f)
                  =\operatorname{tr}R_D(f').
\tag{3.22}
\]
The division trace includes norm characters, and the split discrete trace includes determinant characters.

**Proof.** A quaternion division algebra over \(\mathbb Q\) has a nonempty even ramification set, by Lesson 17, Section 2. Hence it has at least two ramified places. Lemma 3.3 gives the two zero constant terms required by Theorem 3.4. The compact formula of Lesson 18, Theorem 3.2 applies on the division side, with the same fixed-central-character kernel.

Consider a contributing elliptic polynomial \(P\) on the split side, with field \(E=\mathbb Q[T]/(P)\). If \(E\otimes\mathbb Q_v\) is split at a ramified place, its split orbital integral is zero. Otherwise \(E\) embeds in \(D\), by Lesson 18, Section 5, the quadratic-embedding lemma and its exact Brauer prerequisite. The two matrices then correspond to the same element of \(E\); their rational conjugacy classes are unique by the same cyclic-basis and Skolem–Noether argument as in Theorem 1.1, now over the rational field. Their torus is \(E^\times\), with identical adelic measure and identical rational lattice. Thus their coefficient \(a(\gamma)\), including the scalar-stabilizer factor in (3.15), agrees. Local matching makes their orbital integrals equal at ramified places, and the algebra isomorphisms do so at all other places. This identifies every noncentral geometric term in both directions.

Every rational nonscalar quaternion has a quadratic field as centralizer. There are no split semisimple or unipotent quaternion classes to add. The scalar-value identity at each ramified place is \(f'_v(1)=-f_v(1)\), by Lemmas 2.11 and 2.20. The evenness of \(|S|\) makes their global product positive. Lemma 3.2 identifies the two global volumes. Consequently the identity terms agree too. Equation (3.16) and the compact trace formula now give (3.22). All sums and limits have the convergence established in Theorem 3.4 and Lesson 18. \(\square\)

### 3.6. From traces to representations

We explain why the trace equality implies existence and both multiplicity assertions, including tuples consisting only of local norm characters. Merely separating spherical eigenvalues would not by itself establish that existence.

Fix an irreducible unitary division representation \(T_v\) with central character \(\omega_v\) at every \(v\in S\). Put
\[
 f'_v(g)=-\frac{\overline{\Theta_{T_v}(g)}}{V_v},
 \qquad V_v=\operatorname{vol}(D_v^\times/F_v^\times).
\tag{3.23}
\]
Character orthogonality on the compact central quotient gives
\(\operatorname{tr}T'_v(f'_v)=-\delta_{T_v,T'_v}\).
The function is smooth; at finite places it factors through a finite quotient, and at the real place it is a compact-character test. Choose a split transfer. Corollary 2.31 and Theorem 2.22 give
\[
 \begin{array}{ll}
 \operatorname{tr}\pi_v(f_v)=\delta_{\pi_v,\operatorname{JL}(T_v)},
       &\pi_v\text{ a discrete series},\\
 \operatorname{tr}I_v(f_v)=0,
       &I_v\text{ a principal series},\\
 \operatorname{tr}(\chi_v\circ\det)(f_v)
       =-\delta_{T_v,\chi_v\circ\operatorname{nrd}}.
 \end{array}
\tag{3.24}
\]
These are trace projectors: the split test need not be an operator projector. At infinity the finite adjacent-weight wave test in Lemma 2.21 transfers (3.23), so it has the compact finiteness required above. We normalize no multiplicity by an unproved formal degree.

Let \(G^S=\prod'_{v\notin S}G(\mathbb Q_v)\), and write \(\pi^S\) for the outside tensor product. Define two unitary Hilbert sums of representations of this group:
\[
 \begin{aligned}
 M_T^D&=\bigoplus_{\pi':\ \pi'_v=T_v\ (v\in S)}
                         m_D(\pi')\,\pi'^S,\\
 M_T^G&=\bigoplus_{\substack{\pi\ \mathrm{cuspidal}\\
                    \pi_v=\operatorname{JL}(T_v)\ (v\in S)}}
                         m_G(\pi)\,\pi^S
 \ \oplus\bigoplus_{\substack{\chi^2=\omega\\
                    T_v=\chi_v\circ\operatorname{nrd}\ (v\in S)}}
                         (\chi\circ\det)^S.
 \end{aligned}
\tag{3.25}
\]
Every summand's multiplicity is nonnegative. The restricted tensor-product theorem of Lesson 12 makes each outside summand irreducible. Applying (3.22) to any outside test \(a\), and using (3.23)–(3.24), gives
\[
 \operatorname{tr}M_T^D(a)=\operatorname{tr}M_T^G(a).
\tag{3.26}
\]
The products of the local negative traces on the division side and on the split character side are \((-1)^{|S|}=1\). The cuspidal products are one. Thus (3.26) compares positive representation traces; there is no subtraction of a hypothetical missing constituent.

**Lemma 3.6 — separation of the outside representation sums.** The two sums in (3.25) are unitarily equivalent, with their irreducible multiplicities.

**Proof.** If infinity lies in \(S\), fix a compact open subgroup \(J\) outside \(S\). The \(J\)-fixed spaces of both sums are finite dimensional. On the division side this follows from compactness and smooth finite-level arithmetic finiteness, with the fixed real compact type. On the split side the fixed real discrete series has fixed Casimir; choose one of its nonzero compact weights, and at every finite ramified place choose a subgroup fixing a nonzero vector of \(\operatorname{JL}(T_v)\). Then each summand embeds, with its multiplicity, into the finite-dimensional space of Lesson 4, Section 4 at this level, weight and Casimir. The residual lines are finite in number. The operators of the \(J\)-corner Hecke algebra consequently act on two finite-dimensional spaces, and (3.26) says their traces agree for every element.

The following finite-dimensional fact applies. A unital complex algebra closed under adjoints in a finite-dimensional Hilbert space is a direct sum of full matrix algebras on its simple modules. One can see this without a representation classification: diagonalize a self-adjoint element, take its spectral projections by polynomial interpolation, and refine these projections until the invariant blocks are irreducible. On an irreducible block, a nonzero minimal projection \(e\) has rank one. Indeed \(eAe=\mathbb C e\); if orthogonal nonzero \(v,w\) lay in its range, then \(\langle av,w\rangle=\langle eae v,w\rangle=0\) for every \(a\), contradicting cyclicity of \(v\) on an irreducible block. Products with the rank-one projection give every matrix unit, because its range is cyclic. Different irreducible blocks are separated by central sums of these minimal projections. Their traces count module multiplicities. Apply this to the image algebra on the direct sum of our two spaces. Equal traces on the two halves force equal multiplicities of every simple corner module.

The corner remembers any irreducible unitary representation that it meets. Indeed, let \(e\) denote compact averaging onto its \(J\)-fixed space. A nonzero corner-invariant subspace \(W\) generates a dense group-invariant subspace by irreducibility. But \(e\pi(g)e\) preserves \(W\), so its projection back to the finite-dimensional corner is \(W\) itself. Hence \(W\) is the whole corner. If two such corner modules are unitarily equivalent, their compressed matrix coefficients \(e\pi(g)e\) agree, by approximating the group element with smooth convolution tests. For corner vectors \(v,w\), this gives equality of \(\langle\pi(g)v,w\rangle\). The map \(\pi(g)v\mapsto\rho(g)Uv\) is then isometric on their dense spans, since inner products are coefficients at \(g^{-1}h\); it extends to a unitary intertwiner. Thus distinct irreducibles cannot have isomorphic nonzero corner modules. Increasing \(J\) therefore identifies the complete irreducible sums and multiplicities.

If infinity is outside \(S\), first fix a finite level \(J\) and a finite real compact-type projection \(Q\). At these types choose a common constant \(c\) so that \(L=\Delta+c\) is positive on every unitary representation having one of them; the local classification in Lesson 11 gives a uniform lower bound. The spectra of this operator in both sums are discrete with finite multiplicities and polynomial count. On the split side this is (3.17), together with the finite residual part; fixing nonzero vectors at the finite ramified types embeds the sum into that finite-level spectrum. On the division side the corresponding finite-level real quotient is compact; the coordinate-rectangle elliptic comparison used above gives the same polynomial count there. It also proves finite multiplicity in a bounded spectral interval.

For any smooth compact outside test \(a\), multiply its \(J,Q\)-corner operator by a smooth even Fourier multiplier of \(\sqrt L\). Finite propagation and the weight-bundle construction of Lemma 2.21 realize every multiplier with compactly supported smooth time transform as another compact outside test. Equation (3.26) thus identifies the distributions
\(\sum_\lambda\operatorname{tr}(a|_{\lambda,J,Q})\delta_{\sqrt\lambda}\)
on the two sides. To isolate a bounded spectral interval, take a smooth function supported in that interval's square-root image and approximate its inverse Fourier transform by compact time cutoffs. The multiplier converges in all Schwartz seminorms. The polynomial eigenvalue count and \(\|a\|\le\|a\|_1\) dominate the traces, so their equalities pass to the limit. On each bounded interval both discrete spectra contain finitely many points. For each point choose a smooth multiplier equal to one there and zero at every other point of the union in a slightly larger interval, with support in that larger interval. The Schwartz convergence just proved isolates its finite-dimensional eigenspace. Adding finitely many such multipliers gives equality of all corner traces in any bounded spectral window whose endpoints avoid the spectra. These spectral projections commute with the outside group action because the Casimir is central. The finite-dimensional argument just proved, now with the compact-type and level projection \(e=Qe_J\), applies unchanged. Smooth averaging of \(e\pi(g)e\) recovers its compressed coefficients. Increasing the type packet, the level and the spectral interval proves equivalence of the entire sums. This proves the lemma in both cases. \(\square\)

**Proof of Theorem 3.1.** Start with an automorphic irreducible \(\pi'\) of the division group and take its tuple \(T\). Lemma 3.6 gives at least one summand of \(M_T^G\) with the same outside representation. If this summand is a determinant character, (3.25) forces every \(T_v\) to be its corresponding norm character. All local factors of \(\pi'\) are then those of \(\chi\circ\operatorname{nrd}\). The tensor-product uniqueness in Lesson 12 identifies \(\pi'\) with that one-dimensional representation. A non-one-dimensional \(\pi'\) must therefore give a cuspidal \(\pi\), with exactly the factors (3.2).

Conversely a cuspidal \(\pi\) with discrete-series components at every ramified place has a unique inverse local tuple by Theorems 2.5 and 2.30. Its occurrence in \(M_T^G\) implies occurrence of \(\pi^S\) in \(M_T^D\). The resulting \(\pi'\) cannot be one dimensional: a one-dimensional split local factor outside \(S\) has no Whittaker model, whereas a cuspidal factor has one by Lesson 14, Theorem 2.1. It is the required preimage.

Strong multiplicity one for split cusp forms, proved in Lesson 15, Theorem 3.1, says that two cuspidal summands with this outside representation are the same. Their multiplicity is one by the Whittaker multiplicity proof in Lesson 14. A split determinant character cannot share that outside representation: at any good finite place it is nongeneric. Distinct determinant characters with the same outside data are also equal, since weak approximation makes \(\mathbb Q^\times\) dense in the product of the finitely many remaining local multiplicative groups. On the division side fixed outside factors and fixed \(T\) determine the full tensor product. Equality of the multiplicities in Lemma 3.6 therefore gives \(m_D(\pi')=1\).

The same argument handles the one-dimensional part rather than assuming its classification. Any one-dimensional automorphic \(\pi'\) has one-dimensional split factors outside \(S\), so the corresponding summand in \(M_T^G\) cannot be cuspidal. It must be a determinant character, forcing \(\pi'=\chi\circ\operatorname{nrd}\), \(\chi^2=\omega\), at every place. Conversely each such Hecke character defines that automorphic norm function. Its right-equivariant line has multiplicity one: a function with that right transformation rule is a scalar multiple of it. Thus the residual and norm character lines correspond exactly.

Finally, if two non-one-dimensional division constituents agree at almost all places, their cuspidal images agree there and hence everywhere by split strong multiplicity one. The local bijections recover their ramified factors, and tensor-product uniqueness recovers the division constituents. A norm character cannot agree almost everywhere with a non-one-dimensional constituent, since their split factors would contradict genericity. Two norm characters agreeing almost everywhere agree by the character argument above. This proves strong multiplicity one on the entire division spectrum, the image assertion, and every claim in Theorem 3.1. \(\square\)

The argument proves the quaternion global theorem over \(\mathbb Q\), with arbitrary unitary central character and with or without real ramification. The higher-degree number-field and function-field assertions in Section 6 retain their separate scope; they are not consequences of the rank-two truncation proved here.

## 4. Weight two and the dimension equality

Take \(D=B_{p,\infty}\), ramified at the prime \(p\) and at infinity, and a maximal order \(\mathcal O\). Let \(I_1,\ldots,I_h\) represent its right ideal classes, with left orders \(\mathcal O_i\), and put
\[
w_i=|\mathcal O_i^\times|/2,\qquad
M(\mathcal O)=\mathbb C^{\operatorname{Cls}(\mathcal O)},\qquad
\langle x,y\rangle=\sum_{i=1}^{h}\frac{x_i\overline{y_i}}{w_i}.
\tag{4.1}
\]
These are the column-function and row-sum Brandt conventions of Lesson 17. Write \(M^0(\mathcal O)=\mathbf1^\perp\). Its dimension is \(h-1\).

**Corollary 4.1 — the classical specialization.** From the stated global correspondence one obtains a Hecke-module isomorphism
\[
M^0(\mathcal O)\simeq S_2(\Gamma_0(p)),
\qquad B(\ell)\longleftrightarrow T_\ell\quad(\ell\ne p).
\tag{4.2}
\]
The right side consists entirely of newforms. This is the prime-level instance of Eichler's basis problem and the Jacquet–Langlands–Shimizu correspondence.

**Deduction from Theorem 3.1.** Lesson 17, Section 4 identifies \(M(\mathcal O)\) with automorphic functions invariant under \(\widehat{\mathcal O}^{\times}\) and the real quaternion group, with trivial centre. The only norm character in this space is constant: its idele-class character is unramified at every finite prime and trivial on \(\mathbb R_{>0}\), and the idele decomposition for \(\mathbb Q\) from Lesson 1 forces it to be trivial. Removing constants therefore removes precisely the excluded constituent of Theorem 3.1.

At infinity, the trivial quaternion type transfers to \(D_2\). At \(p\), a representation with \(\mathcal O_p^\times\)-invariants factors through \(D_p^\times/\mathcal O_p^\times\), an infinite cyclic group, and is an unramified norm character. It transfers to an unramified Steinberg twist. That twist has conductor one and a one-dimensional level-one fixed space by Lesson 8, Theorems 2.1 and 3.2. At other primes the spherical space is one-dimensional by Lesson 13, Theorem 3.2. Global multiplicity one and the classical dictionary of Lesson 8, Theorem 5.1 and Lesson 2, Theorem 4.1 therefore identify one line on each side.

Conversely, a weight-two newform of prime level and trivial character has a conductor-one component at \(p\). The principal-series conductor formula rules out a ramified principal series: trivial central character makes the two ramified unit characters inverse, hence their conductor sum is at least two. Supercuspidals also have conductor at least two. Thus its local component is an unramified Steinberg twist, and Theorem 3.1 transfers it back. Level-one weight-two cusp forms vanish [LG-MF-06, Theorem 4.1], so there are no oldforms to add. At a good prime the weight-two scaling factor in Lesson 13, Theorem 4.1 is one; the operators agree as asserted. \(\square\)

We now prove the assigned dimension check by a separate calculation. It checks (4.2) without using (4.2) to count dimensions. For compactified modular curves we use [LG-MF-03, Lemma 3.1 and Proposition 3.2]: \(X(1)\) is a sphere, the only branching is over its order-two and order-three elliptic points and its cusp, and the local indices are the stabilizer quotients and cusp widths. Riemann–Hurwitz is stated in that lesson's Section 3. The weight-two differential dictionary and \(h^0(\Omega^1)=g\) are [LG-MF-06, Theorems 2.1 and 4.1].

**Theorem 4.2 — the dimension check, for every prime.**
\[
\dim S_2(\Gamma_0(p))=h(\mathcal O)-1.
\tag{4.3}
\]

**Proof.** Reduction maps \(\mathrm{SL}_2(\mathbb Z)\) onto \(\mathrm{SL}_2(\mathbb F_p)\). Indeed, elementary row operations over the field express a determinant-one matrix as a product of elementary unipotents, and each such factor lifts integrally. The preimage of the upper triangular subgroup is \(\Gamma_0(p)\). Thus the cosets are the \(p+1\) lines of \(\mathbb F_p^2\), and the degree of \(X_0(p)\to X(1)\) is \(N=p+1\).

The order-two element \(S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\) has fixed lines represented by \((x,1)\) satisfying \(x^2+1=0\). The order-three element \(ST=\left(\begin{smallmatrix}0&-1\\1&1\end{smallmatrix}\right)\) has fixed lines satisfying \(x^2+x+1=0\). Neither fixes the line \((1,0)\). Hence their fixed counts are
\[
e_2=1+s_4,\quad e_3=1+s_3,\qquad
s_4=\left(\frac{-4}{p}\right),\quad
s_3=\left(\frac{-3}{p}\right),
\tag{4.4}
\]
with Kronecker symbols. For odd primes other than the relevant discriminant divisor, completing the square gives the usual quadratic-residue counts. Directly at \(2\), the counts are \(1,0\); at \(3\), they are \(0,1\), agreeing with (4.4).

There are exactly two cusps. Write a rational cusp as \(a/c\) with \(\gcd(a,c)=1\). If \(p\mid c\), complete \((a,c)\) to a determinant-one matrix in \(\Gamma_0(p)\), showing equivalence to \(\infty\). If \(p\nmid c\), solve \(xc-ay=1\). Replacing \((x,y)\) by \((x+at,y+ct)\) makes \(p\mid y\), so \(\left(\begin{smallmatrix}x&a\\y&c\end{smallmatrix}\right)\in\Gamma_0(p)\) sends \(0\) to \(a/c\). The two cases are distinct because the property \(p\mid c\) is preserved under \(\Gamma_0(p)\). The widths are one at \(\infty\) and \(p\) at \(0\), as follows by conjugating \(T^n\) by \(S\).

The coset action of \(S\) has \(e_2\) fixed points and \((N-e_2)/2\) two-cycles. The latter contribute \((N-e_2)/2\) to Riemann–Hurwitz. Similarly, the order-three contribution is \(2(N-e_3)/3\). The two cusps contribute \((1-1)+(p-1)=N-2\). There is no other branching, so
\[
2g-2=-2N+\frac{N-e_2}{2}
+\frac{2(N-e_3)}{3}+N-2,
\qquad
g=\frac{p+1}{12}-\frac{e_2}{4}-\frac{e_3}{3}.
\tag{4.5}
\]
By the differential dictionary, \(\dim S_2=g\). Concretely, \(f(z)dz\) is invariant; at a cusp of width \(h\), \(dz=h\,dq/(2\pi i q)\), so the vanishing constant term is exactly the condition that the differential extends holomorphically. The elliptic descent and the reverse pullback are included in LG-MF-06, Theorem 2.1.

The class-number evaluation proved from the Eichler trace formula in Lesson 18, equation (6.3), is
\[
h(\mathcal O)=\frac{p-1}{12}
+\frac{1-s_4}{4}+\frac{1-s_3}{3}.
\tag{4.6}
\]
Its mass input is \(\sum_i1/w_i=(p-1)/12\), proved in Lesson 17, Theorem 4.3. Substituting (4.4) in (4.5) and subtracting one from (4.6) give the same quantity, since
\(1/4+1/3-1=-5/12\). This proves (4.3), including \(p=2,3\). \(\square\)

## 5. Two levels computed from the quaternion side

### 5.1. Level eleven

For \(p=11\), \(s_4=s_3=-1\). Equations (4.5)–(4.6) give
\[
g=12/12=1,\qquad h=10/12+1/2+2/3=2.
\]
In the class ordering of Lesson 17, Section 5.2,
\[
B(2)=\begin{pmatrix}1&2\\3&0\end{pmatrix},
\qquad (w_1,w_2)=(2,3).
\tag{5.1}
\]
The constant column has eigenvalue \(3\). The column \((2,-3)^t\) is orthogonal to constants for (4.1), since \(2/2-3/3=0\), and direct multiplication gives eigenvalue \(-2\). Thus (4.2) identifies the unique normalized weight-two level-eleven newform with \(a_2=-2\). This also agrees with the coefficient calculation in Lesson 2, Section 7. The weighted pairing is essential: the matrix in (5.1) is not symmetric in the ordinary Euclidean pairing.

### 5.2. A maximal order at level thirty-seven

Let
\[
D=\left(\frac{-2,-37}{\mathbb Q}\right),\qquad
i^2=-2,\quad j^2=-37,\quad k=ij=-ji.
\]
At \(37\) its Hilbert symbol is \(\left(\frac{-2}{37}\right)=-1\); at infinity both parameters are negative. Every other odd prime has Hilbert symbol one because both parameters are units there. Hilbert reciprocity, proved by the quaternion classification deduction of Lesson 17, Section 2 and its written Brauer provider, then makes the symbol at \(2\) one. Thus \(D=B_{37,\infty}\).

Put
\[
\beta=(1+i+j)/2,\qquad \gamma=(2+i+k)/4,
\qquad \mathcal O=\mathbb Z\{1,i,\beta,\gamma\}.
\tag{5.2}
\]
The complete products apart from multiplication by \(1\) are
\[
\begin{array}{lll}
i^2=-2,&\beta^2=\beta-10,&\gamma^2=\gamma-5,\\
i\beta=2\gamma-2,&\beta i=i-2\gamma,&i\gamma=i-\beta,\\
\gamma i=\beta-1,&\beta\gamma=5i,&
\gamma\beta=\beta+\gamma-1-5i.
\end{array}
\tag{5.3}
\]
Each identity follows by expanding (5.2) and using \(ji=-ij\). They show that this lattice is an order. For further verification its reduced-trace pairing has matrix
\[
\bigl(\operatorname{trd}(e_re_s)\bigr)_{r,s}
=\begin{pmatrix}
2&0&1&1\\
0&-4&-2&-1\\
1&-2&-19&0\\
1&-1&0&-9
\end{pmatrix},\qquad\det=-37^2,
\tag{5.4}
\]
in the ordered basis \(1,i,\beta,\gamma\). Hence its reduced discriminant is \(37\). An order whose reduced discriminant equals the algebra discriminant is maximal, by the order/discriminant criterion used in Lesson 17, Section 5.2.

The norm, expanded in that basis, is
\[
\begin{aligned}
\operatorname{nrd}(a+bi+c\beta+d\gamma)
&=(a+c/2+d/2)^2
+2(b+c/2+d/4)^2\\
&\quad+37c^2/4+74d^2/16.
\end{aligned}
\tag{5.5}
\]
For norms at most three, its last two summands force \(c=d=0\). The units are therefore \(\pm1\), the norm-two elements are \(\pm i\), and the norm-three elements are \(\pm1\pm i\). Their counts are \(2,2,4\).

At \(37\), both symbols in (4.4) equal one. Thus \(h=3\), and the mass is \((37-1)/12=3\). Each \(1/w_i\le1\); three such terms can sum to three only if all \(w_i=1\). Every Brandt matrix is consequently symmetric in the ordinary pairing.

### 5.3. Determine both eigenforms

The diagonal norm-count formula of Lesson 17 gives \(B(2)_{11}=2/2=1\). The Eichler formula of Lesson 18, Theorem 5.3 gives \(\operatorname{tr}B(2)=1\). To see this explicitly, the possible quadratic discriminants are \(-8,-7,-4\): at \(37\) their local multipliers \(1-(d/37)\) are respectively \(2,0,0\). Only the \(t=0,d=-8\) term contributes, with value \(\tfrac12\cdot1\cdot2=1\).

The other two diagonal entries are nonnegative integers and must be zero. Write the off-diagonal entries as \(x,y,z\). All row sums are \(3\), so \(x+y=2\), \(x+z=y+z=3\). Hence \(x=y=1,z=2\), and
\[
B(2)=\begin{pmatrix}1&1&1\\1&0&2\\1&2&0\end{pmatrix}.
\tag{5.6}
\]
Its three eigenvectors and eigenvalues are
\[
\begin{array}{c|c|c}
\text{column}&B(2)\text{ eigenvalue}&\text{space}\\\hline
(1,1,1)^t&3&\text{constants}\\
v_A=(0,1,-1)^t&-2&M^0\\
v_B=(-2,1,1)^t&0&M^0.
\end{array}
\tag{5.7}
\]
Since these eigenvalues are distinct, every commuting Hecke operator preserves each line.

Similarly \(B(3)_{11}=4/2=2\). In the trace formula the discriminants from \(t=0,\pm1,\pm2,\pm3\) are \(-12,-11,-8,-3\), with the additional overorder \(-3\) for \(-12\). Only the two \(-8\) terms have nonzero local multiplier; each contributes one. Thus \(\operatorname{tr}B(3)=2\). Its constant eigenvalue is \(4\). If \(a,b\) are its eigenvalues on \(v_A,v_B\), their orthogonal projections have first diagonal entries \(0,2/3\); the constant projection has first diagonal entry \(1/3\). Therefore
\[
2=4/3+2b/3,\qquad 2=4+a+b,
\quad\text{so }b=1,\ a=-3.
\tag{5.8}
\]
Reconstructing the matrix gives
\[
B(3)=\begin{pmatrix}2&1&1\\1&0&3\\1&3&0\end{pmatrix}.
\tag{5.9}
\]
Its multiplication with (5.6) commutes, which checks the reconstruction directly.

By (4.2), the two cusp lines give exactly two normalized newforms \(f_A,f_B\), with
\[
(a_2(f_A),a_3(f_A))=(-2,-3),\qquad
(a_2(f_B),a_3(f_B))=(0,1).
\tag{5.10}
\]
One can compute further coefficients without identifying elliptic curves. For \(n\) prime to \(37\), let \(N_n\) be the number of norm-\(n\) elements in (5.5), \(d_n=N_n/2\), and \(t_n=\operatorname{tr}B(n)\), computed by the Eichler formula. The constant eigenvalue is \(\sigma_1(n)=\sum_{d\mid n}d\). The same projections as in (5.8) give
\[
b_n=\frac{3d_n-\sigma_1(n)}2,
\qquad a_n=t_n-\sigma_1(n)-b_n.
\tag{5.11}
\]
Here \(a_n,b_n\) are the coefficients of \(f_A,f_B\). The first twelve inputs and outputs are:

| \(n\) | \(N_n\) | \(t_n\) | \(a_n\) | \(b_n\) |
|---:|---:|---:|---:|---:|
| 1 | 2 | 3 | 1 | 1 |
| 2 | 2 | 1 | −2 | 0 |
| 3 | 4 | 2 | −3 | 1 |
| 4 | 2 | 7 | 2 | −2 |
| 5 | 4 | 4 | −2 | 0 |
| 6 | 8 | 18 | 6 | 0 |
| 7 | 4 | 6 | −1 | −1 |
| 8 | 10 | 15 | 0 | 0 |
| 9 | 6 | 17 | 6 | −2 |
| 10 | 12 | 22 | 4 | 0 |
| 11 | 12 | 10 | −5 | 3 |
| 12 | 12 | 20 | −6 | −2 |

For a reproducible finite count, multiply (5.5) by sixteen:
\[
16n=(4a+2c+2d)^2+2(4b+2c+d)^2+148c^2+74d^2.
\tag{5.12}
\]
Every solution with \(n\le12\) satisfies \(|c|\le1,|d|\le1,|a|\le4,|b|\le3\), by bounding each nonnegative summand of (5.5) and then its shifted coordinates. Enumerating those integer ranges in (5.12) produces the displayed \(N_n\). The Eichler sum ranges over \(t^2<4n\) and the positive square divisors of \(t^2-4n\), so the \(t_n\) column is also a finite calculation with no spectral input. For instance the Hecke checks \(a_4=a_2^2-2\), \(a_6=a_2a_3\), \(a_9=a_3^2-3\), and the same identities for \(b\), agree with the table.

## 6. Higher degree and geometric realizations

For a nonarchimedean local field \(F\), a central division algebra \(D_0/F\) of degree \(d\), and \(n=rd\), the local correspondence is a bijection between essentially square-integrable representations of \(\mathrm{GL}_r(D_0)\) and \(\mathrm{GL}_n(F)\). On matching regular classes its character relation has sign
\[
\Theta_\pi(g)=(-1)^{n-r}\Theta_{\pi'}(g').
\tag{6.1}
\]
This is the local theorem of Deligne–Kazhdan–Vignéras and Rogawski in characteristic zero; Arthur, Theorem 25.1 states it. Badulescu 2002, Theorem 1.1 gives (6.1) in positive characteristic. The full proof of that local theorem is not reproduced here.

Over number fields, Badulescu–Renard, Theorem 18.1 gives an injection of the inner form's discrete automorphic spectrum into the split discrete spectrum, onto the locally compatible representations, with multiplicity one and strong multiplicity one. Its transfer uses the **extended unitary** local correspondence; global discrete spectrum need not mean local discrete series everywhere. This distinction includes the norm/determinant characters already encountered in degree two.

For a central division algebra of degree \(n\) over a global function field, the analogous discrete-spectrum bijection with the locally compatible split representations, and multiplicity one, are Badulescu–Roche, Theorems 3.2–3.3. Compatibility uses their local unitary transfer, Theorem 2.5; their Sections 3.2–3.3 explain the central degree quotient and its relation to fixed central characters. This global positive-characteristic result is separate from Badulescu's 2002 local theorem. [Badulescu–Roche's paper](https://arxiv.org/html/1302.5289v2#S3.SS4).

There is also a geometric question: can a correspondence between automorphic representations be realized by a relation between cohomology classes? Ichino–Prasanna's introduction studies such Hodge and cohomological realizations for quaternionic Shimura varieties. Their work assumes the relevant Jacquet–Langlands transfer; it is not the source of the basic existence theorem (3.1). The introduction distinguishes its Hodge-class construction from arithmetic cycle assertions requiring additional conjectural input. Those finer realizations are beyond this lesson.

### 6.1. Which regular classes match in higher degree?

The class comparison in Section 1 extends to matrix algebras over a division algebra, with a divisibility condition on every irreducible factor. We prove that condition before using higher-degree character identities. Throughout this subsection, \(F\) is a nonarchimedean local field of either characteristic, \(D_0/F\) is a central division algebra of degree \(d\), \(A=M_r(D_0)\), and \(n=rd\).

We use the local invariant and restriction rule proved in Brauer groups of local and global fields, Proposition 24.1 and Theorem 24.2. The algebraic facts that a Brauer class has a unique division representative, and that a split central simple algebra acts on its column module, are proved in Central simple algebras and the Brauer group, Sections 1–4.

**Lemma 6.1 — the splitting degree of a local division algebra.** The invariant of \(D_0\) has denominator exactly \(d\). For a finite separable extension \(E/F\),
\[
 D_0\otimes_F E\simeq M_d(E)
 \quad\Longleftrightarrow\quad d\mid[E:F].
\tag{6.2}
\]

**Proof.** Write a Brauer invariant in lowest terms as \(a/e\). Choose the unramified extension \(L/F\) of degree \(e\), with arithmetic Frobenius \(\sigma\). Its cyclic algebra
\[
 C=\bigoplus_{j=0}^{e-1}L u^j,
 \qquad ux=\sigma(x)u,\qquad u^e=\varpi^a
\]
has invariant \(a/e\) by Proposition 24.1. If the invariant is nonzero take \(1\le a<e\); for the zero class take \(e=1,a=0\).

For a nonzero element set
\[
 v_C\left(\sum_jx_ju^j\right)
       =\min_{x_j\ne0}\{e\,v_L(x_j)+aj\}.
\]
When \(e>1\), coprimality makes the nonzero terms' displayed valuations distinct modulo \(e\), so the minimum is unique. In a product, the two minimal terms give one nonzero term of valuation the sum of the two minima. Reducing powers with \(u^e=\varpi^a\) preserves that valuation. Every other product term has strictly larger valuation and cannot cancel it; Frobenius preserves the valuation of coefficients. Thus \(v_C(xy)=v_C(x)+v_C(y)\), so \(C\) has no zero divisors. A finite-dimensional algebra without zero divisors is division: left multiplication by a nonzero element is injective and hence surjective, producing an inverse. The case \(e=1\) is the field itself.

This constructs a division representative of dimension \(e^2\) for every invariant. Uniqueness of the division representative makes its degree \(e\) equal to \(d\) for the class of \(D_0\). Restriction to \(E\) multiplies the invariant by \([E:F]\). It is zero exactly when \(d\) divides that degree, and zero Brauer class for this degree-\(d\) algebra means \(M_d(E)\). This proves (6.2). \(\square\)

**Theorem 6.2 — the regular matching criterion.** Let
\(P=\prod_{i=1}^sP_i\in F[X]\) be monic and separable of degree \(n\), with nonzero constant term and distinct monic irreducible factors \(P_i\). A regular semisimple element of \(\mathrm{GL}_n(F)\) with polynomial \(P\) matches an element of \(\mathrm{GL}_r(D_0)\) if and only if
\[
 d\mid\deg P_i\qquad\text{for every }i.
\tag{6.3}
\]
When it exists, the matching conjugacy class is unique. Both centralizers are
\(\prod_i E_i^\times\), with \(E_i=F[X]/(P_i)\).

**Proof: necessity.** Regard \(A\) as the endomorphism algebra of the right \(D_0\)-space \(V=D_0^r\). For a regular semisimple \(x\in A\), the minimal polynomial equals its reduced characteristic polynomial: after a separable splitting extension its matrix has \(n\) distinct eigenvalues, all of which a polynomial annihilating it must contain. Thus
\(F[x]\simeq\prod_i E_i\). Its idempotents decompose \(V=\bigoplus_iV_i\) into right \(D_0\)-subspaces. Put \(r_i=\dim_{D_0}V_i\).

After splitting \(D_0\), a rank-\(r_i\) idempotent has matrix rank \(dr_i\). It selects exactly the roots of \(P_i\) in the reduced characteristic polynomial. Consequently \(\deg P_i=dr_i\), proving (6.3). For completeness, this rank calculation follows by applying a primitive matrix idempotent to the right \(M_d\)-module \(M_d^{r_i}\): the resulting vector space has dimension \(dr_i\), and the induced endomorphism is the corresponding block of the split degree-\(n\) matrix.

**Proof: existence.** Suppose (6.3), and write \(m_i=\deg P_i=dr_i\). Lemma 6.1 gives
\(E_i\otimes_F D_0^{\mathrm{op}}\simeq M_d(E_i)\). Its column module \(W_i=E_i^d\) is therefore an \(E_i\)-space with a commuting right \(D_0\)-action. Its \(F\)-dimension is \(m_id=r_id^2\), so its right \(D_0\)-dimension is \(r_i\). The element \(X\bmod P_i\) acts on \(W_i\) by an invertible right-\(D_0\)-linear map.

On \(W=\bigoplus_iW_i\), of right dimension \(r\), these maps give \(x\in A^\times\). Its ordinary \(F\)-linear characteristic polynomial is \(\prod_iP_i^d=P^d\). For any element of \(A\), this ordinary characteristic polynomial is the \(d\)-th power of its reduced characteristic polynomial: after splitting, the right module is the space of \(n\)-by-\(d\) matrices, and left multiplication acts by the same degree-\(n\) matrix on each of its \(d\) columns. Both sides descend to \(F\). Unique factorization of monic polynomials now gives the reduced polynomial \(P\). This remains valid when the characteristic divides \(d\); equality of positive powers in \(F[X]\) still determines a monic polynomial.

**Proof: uniqueness and centralizers.** If \(x,y\in A\) have reduced polynomial \(P\), consider the \(F\)-vector space
\(U=\{c\in A:cx=yc\}\). Over a separable splitting field the two regular matrices diagonalize with the same distinct eigenvalues, so \(U\) contains an invertible matrix. The reduced norm, restricted to \(U\), is consequently a nonzero polynomial over \(F\). Since \(F\) is infinite it cannot vanish on all of \(U(F)\): choose coordinates and use induction on the number of variables, with the finite root bound in one variable. Hence some \(c\in U(F)\) is invertible, and \(y=cxc^{-1}\).

The algebra centralizer of \(x\) has dimension \(n\), as is seen after splitting from the diagonal matrices commuting with \(n\) distinct eigenvalues. It contains the \(n\)-dimensional algebra \(F[x]\), so it equals \(\prod_iE_i\). Taking units proves the centralizer assertion. On the split side the companion matrix gives existence and the same intertwiner argument gives uniqueness. \(\square\)

For example, take \(F=\mathbb Q_3\), \(d=r=2\), and let \(D_0\) be quaternion division. The separable polynomial
\((X^2+1)(X^2-2)\) has two distinct irreducible quadratic factors, since both reduce to an irreducible quadratic modulo three. It therefore occurs in \(M_2(D_0)\). In contrast,
\((X-1)(X^3-X-1)\) has irreducible factor degrees one and three: its cubic has no root modulo three. Its companion matrix in \(\mathrm{GL}_4(\mathbb Q_3)\) has no matching class in \(\mathrm{GL}_2(D_0)\).

Finally, on a matched regular class the adjoint discriminants agree. After splitting they are both
\(\prod_{i\ne j}(1-\alpha_i/\alpha_j)\), where the \(\alpha_i\) are the distinct roots of \(P\); this symmetric expression lies in \(F\) and its absolute value gives the quotient conjugation Jacobian. The relative split ranks modulo the centre are \(n-1\) and \(r-1\), so their difference is \(n-r\), the exponent in (6.1). The matching criterion and discriminant calculation supply the algebraic comparison in all degrees. The representation bijection and global discrete-spectrum assertions above require their additional character and trace arguments.

### 6.2. Parabolic induction on matching regular classes

Write \(G_A=\mathrm{GL}_r(D_0)\), where \(\deg D_0=d\), and put \(n=rd\). A standard parabolic \(P=MN\) is specified by an ordered partition \(r=r_1+\cdots+r_k\); its Levi is \(M=\prod_a\mathrm{GL}_{r_a}(D_0)\). Set \(n_a=dr_a\). The split group has the corresponding parabolic with block sizes \(n_1,\ldots,n_k\). We establish the character calculation before using it to compare induced representations. It applies in either characteristic and requires no classification by quadratic parameters.

The valuation ring used here is available from Lemma 6.1. Its cyclic division model has the complete discrete valuation
\(v(\sum_jx_ju^j)=\min_j\{d\,v_L(x_j)+aj\}\), with \(\gcd(a,d)=1\).
The same least-term product calculation proves multiplicativity. Its values fill \(\mathbb Z\), by Bézout applied to \(a,d\); choose an element \(\Pi\) of value one. The nonnegative part \(\mathcal O_{D_0}\) is a finite \(\mathcal O_F\)-lattice in this displayed basis, hence compact and complete. Every nonzero right or left ideal in it is generated by an element of least valuation: division by that element leaves nonnegative valuation. An element of value zero and its inverse both belong to the ring. These facts prove the valuation-ring and lattice properties below, rather than assuming a split matrix lattice for a division algebra. When \(d=1\), this is the usual field valuation.

For a smooth representation \(\sigma\) of \(M\), its normalized induction is the space of locally constant functions \(s:G_A\to V_\sigma\) satisfying
\[
 \begin{gathered}
 s(mug)=\delta_P(m)^{1/2}\sigma(m)s(g),\\
 (I_P(\sigma)(h)s)(g)=s(gh).
 \end{gathered}
\tag{6.4}
\]
Here \(u\in N\), and \(\delta_P(m)\) is the absolute determinant of conjugation by \(m\) on the upper off-diagonal block space \(\operatorname{Lie}N\). This definition fixes the direction of the modulus. For any regular semisimple \(g\in G_A\), define
\[
 \Delta_{G_A}(g)=
 \left|\det_F(1-\operatorname{Ad}(g)
       \mid\operatorname{Lie}G_A/\operatorname{Lie}G_{A,g})\right|_F.
\tag{6.5}
\]
The same definition gives \(\Delta_M\) on the Levi regular set.

**Lemma 6.3 — the fixed flags and their derivative.** Let the reduced polynomial of \(g\) be the separable polynomial \(P_g=\prod_iP_i\), and put \(m_i=\deg P_i\). The \(g\)-fixed flags in \(P\backslash G_A\) are in bijection with ordered partitions \((S_1,\ldots,S_k)\) of its irreducible factors such that
\[
 \sum_{i\in S_a}m_i=n_a\quad(1\le a\le k).
\tag{6.6}
\]
Each fixed flag has a diagonal representative \(m=(g_1,\ldots,g_k)\in M\), where \(g_a\) has reduced polynomial \(\prod_{i\in S_a}P_i\). On the flag tangent space the right action of \(g\) has no eigenvalue one. Its determinant is
\[
 \begin{gathered}
 J_P(m)=\prod_{a<b}\left|\det_F(1-T_{ab})\right|_F,\\
 T_{ab}:\operatorname{Hom}_{D_0}(V_a,V_b)
             \longrightarrow\operatorname{Hom}_{D_0}(V_a,V_b),\\
 T_{ab}(X)=g_b^{-1}Xg_a.
 \end{gathered}
\tag{6.7}
\]
Furthermore
\[
 \frac{\delta_P(m)^{1/2}}{J_P(m)}
       =\frac{\Delta_M(m)^{1/2}}{\Delta_{G_A}(m)^{1/2}}.
\tag{6.8}
\]

**Proof.** A point of \(P\backslash G_A\) is a flag of right \(D_0\)-subspaces, with the specified dimensions; using inverse representatives changes left flags to this right quotient without changing fixed points. The spectral idempotents in \(F[g]=\prod_iE_i\) decompose \(V=D_0^r\) as \(\bigoplus_iV_i\). By Theorem 6.2, \(E_i\otimes_FD_0^{\mathrm{op}}\simeq M_d(E_i)\), and \(V_i\) is its column module. It is simple: the matrix units send any nonzero column to every coordinate column. A subspace stable under both \(g\) and the right \(D_0\)-action is stable under this full algebra, so intersects \(V_i\) in either zero or \(V_i\). The idempotents then show that it is a sum of whole \(V_i\)'s. Since \(\dim_{D_0}V_i=m_i/d\), the flags are exactly (6.6). This proves finiteness and gives their diagonal representatives. The split case is the identical argument with \(d=1\).

Near the flag of \(m\), use lower block-unitriangular coordinates \(1+X\), with diagonal blocks one. Such coordinates describe an open flag cell: block elimination writes a matrix with invertible leading block minors uniquely as an upper block-triangular matrix times a lower unitriangular matrix. The elimination uses only inversion and multiplication in matrices over \(D_0\), so gives analytic coordinates over \(F\), with no exponential map. In the identity
\((1+X)m=m(1+m^{-1}Xm)\), the linear term on its \((b,a)\)-block is \(g_b^{-1}X_{ba}g_a\). This proves (6.7). After a separable field splitting all blocks, its eigenvalues are the ratios \(\alpha/\beta\), with \(\alpha\) an eigenvalue in block \(a\), \(\beta\) in block \(b\). The blocks have disjoint spectra, so none is one. Determinants computed after scalar extension are the same polynomials over \(F\); in particular the derivative is invertible even if the characteristic divides \(d\).

Let \(T\) be the sum of these lower-block operators. The upper-block conjugation operator is its transpose under the reduced-trace pairing \((X,Y)\mapsto\operatorname{Trd}(XY)\): cyclicity moves the two block matrices across the pairing. This pairing is nondegenerate, since after splitting it is the ordinary matrix trace pairing, whose matrix units are dual. The adjoint action on the lower blocks is \(T^{-1}\). Consequently
\[
 \begin{gathered}
 \delta_P(m)=|\det T|_F,\\
 \frac{\Delta_{G_A}(m)}{\Delta_M(m)}
 =|\det(1-T)|_F|\det(1-T^{-1})|_F,\\
 |\det(1-T)|_F|\det(1-T^{-1})|_F
 =\frac{J_P(m)^2}{\delta_P(m)}.
 \end{gathered}
\]
This proves (6.8), including the square root and its direction. \(\square\)

**Theorem 6.4 — normalized induced characters.** Suppose \(\sigma\) is smooth and admissible, and its trace on tests supported in the Levi regular set is represented by a locally constant function \(\Theta_\sigma\). Then \(I_P(\sigma)\) is admissible. Its trace on tests supported in the group regular set is represented by the locally constant function
\[
 \Theta_{I_P(\sigma)}(g)
 =\sum_{\mathcal F\in(P\backslash G_A)^g}
       \frac{\Delta_M(m_{\mathcal F})^{1/2}}
            {\Delta_{G_A}(g)^{1/2}}
       \Theta_\sigma(m_{\mathcal F}).
\tag{6.9}
\]
An empty sum is zero. The hypothesis on the inducing trace is explicit; this theorem constructs the induced trace function from it and does not assume the general higher-degree character theorem.

**Proof: compact flags and finite trace.** Put \(K=\mathrm{GL}_r(\mathcal O_{D_0})\). Every flag has an integral adapted basis. Here is the lattice argument. A subspace intersects \(\mathcal O_{D_0}^r\) in a saturated submodule: if a nonzero integral scalar multiple of a lattice vector belongs to the subspace, so does the vector. A submodule of a finite free module over this valuation ring is free, by successive coordinate elimination: project onto the first nonzero coordinate, choose an element whose projected coordinate has least valuation, and use its right divisibility to clear that coordinate in every other element. Repeat in the remaining coordinates. For a saturated submodule the diagonal factors are units, since a nonunit factor would leave torsion in the quotient. Its basis therefore extends to a lattice basis. Apply this successively in the quotients along the flag. Thus \(K\) acts transitively and \(G_A=PK\). In particular the flag space is compact.

If \(J\) is compact open, shrink it to a subgroup of \(K\). It contains a normal congruence subgroup of \(K\). The compact space \(P\backslash G_A/J\) is therefore finite. On each of its orbits a \(J\)-invariant section is determined by a vector fixed by an open compact subgroup of \(M\), namely the Levi projection of the corresponding conjugate intersection with \(P\). The modulus is one on this compact subgroup. Admissibility of \(\sigma\) makes every such space finite-dimensional. Hence \(I_P(\sigma)^J\) is finite-dimensional. For a bi-\(J\)-invariant test the convolution operator has image in this space, so its trace is an ordinary finite-dimensional trace.

**Proof: the local diagonal calculation.** Fix regular \(g\). Its fixed flags are finite by Lemma 6.3. Choose disjoint small coordinate balls around them. On the compact complement, the graph of the right action is disjoint from the diagonal. A finite cover and continuity give a neighbourhood \(B\) of \(g\) for which every convolution kernel from a test supported in \(B\) has zero diagonal there. Thus only these coordinate balls contribute to the trace.

We spell out the kernel calculation at one of them. Write a local section of the quotient as \(s(x)\). For a group element \(h\), the unique factorization
\[
 s(x)h=p(x,h)s(y(x,h))
\]
puts its action on a section in the form
\(\delta_P(p(x,h))^{1/2}\sigma(p_M(x,h))s(y(x,h))\).
Convolve against the test and take the diagonal \(y=x\). The displacement derivative in the quotient variable at \((0,g)\) is \(T-1\), whose determinant has absolute value \(J_P(m)\). Eliminating that variable therefore contributes \(J_P(m)^{-1}\). The fibre contributes \(\delta_P(m)^{1/2}\Theta_\sigma(m)\), so the resulting trace density on \(B\) is
\[
 \frac{\delta_P(m_{\mathcal F(h)})^{1/2}}
      {J_P(m_{\mathcal F(h)})}
       \Theta_\sigma(m_{\mathcal F(h)}),
 \qquad h\in B.
\tag{6.10}
\]
Here \(\mathcal F(h)\) is the unique fixed flag in this ball. The fibre trace is used only on Levi regular elements: the distinct block spectra persist after shrinking \(B\).

For precision, the two local operations in this calculation have elementary finite versions. First, a convergent analytic map with invertible derivative is a bijection on sufficiently small balls after its linear change of variables. Write it as \(Ax+R(x)\), and shrink the ball until \(A^{-1}R\) has Lipschitz constant less than one. Successive substitution solves every equation uniquely by completeness. It maps small subballs to translates of \(A\) times those subballs; subdivision and Haar translation show that its measure factor is \(|\det A|_F\). This proves the change of variables and the persistence of one fixed flag in each ball without a characteristic restriction. Second, refine a compact-open partition of the flag balls until the test kernel and its fibre coefficients are constant on the relevant cells, and use a sufficiently small compact-open averaging projector on the inducing space. Its image is finite-dimensional by admissibility. The trace is the sum of diagonal cell kernels: a cell of measure \(v\) has averaging kernel \(v^{-1}\), so the partition-cell volume cancels. Substituting the preceding local factorization and change of variables gives (6.10); the remaining Levi integral is its actual trace distribution, to which the assumed \(\Theta_\sigma\) applies. The finite-dimensional averaging step is uniform on the compact coefficient sets: the orbit of each fixed vector under a compact set is finite, because its stabilizer is open; intersecting the stabilizers of finitely many such orbit vectors gives one projector that works on every relevant cell. Refining the partition or shrinking the averaging group leaves the finite-rank operator and its trace unchanged. Thus no trace of an individual infinite-dimensional operator \(\sigma(m)\) is being asserted.

All integrals just used have compact support in finitely many quotient charts. Haar measures for the parabolic and quotient can be taken in the disintegration of Haar measure on \(G_A\). Rescaling a coordinate measure rescales its diagonal kernel inversely, so (6.10) is independent of that auxiliary choice. Summing over the fixed-flag balls and applying (6.8) proves (6.9) as an equality of trace distributions on \(B\). These neighbourhoods cover the regular set. The same local factorization, together with local constancy of the inducing trace, proves local constancy of the displayed density. This finishes the proof. \(\square\)

**Corollary 6.5 — compatibility with induction and the transfer sign.** Suppose, for every \(a\), representations \(\sigma_a\) of \(\mathrm{GL}_{n_a}(F)\) and \(\sigma'_a\) of \(\mathrm{GL}_{r_a}(D_0)\) have regular trace functions satisfying
\[
 \Theta_{\sigma_a}(h_a)=(-1)^{n_a-r_a}
                  \Theta_{\sigma'_a}(h'_a)
 \quad(h_a\leftrightarrow h'_a).
\tag{6.11}
\]
Assume their product inducing representations are admissible, with these trace functions. Their normalized parabolic inductions satisfy
\[
 \Theta_{I_P(\boxtimes_a\sigma_a)}(g)
       =(-1)^{n-r}
         \Theta_{I_{P'}(\boxtimes_a\sigma'_a)}(g')
 \quad(g\leftrightarrow g').
\tag{6.12}
\]
If a split parabolic has even one block size not divisible by \(d\), every normalized induction from it with the hypotheses of Theorem 6.4 has character zero on all classes matching \(G_A\). For \(k>1\), every such induced character vanishes on the elliptic regular set of its own group.

**Proof.** Theorem 6.2 makes every factor degree of a matching polynomial divisible by \(d\). Lemma 6.3 consequently identifies the fixed-flag index sets on the two sides of (6.12), with identical ordered block polynomials. The adjoint discriminants agree on each block and on the full group: after splitting they are the same products of \(1-\alpha_i/\alpha_j\). Thus the coefficients in (6.9) agree term by term. The fibre traces are the products of the block traces. To justify this trace assertion, a compact-open test on a product group is a finite sum of product tests; finite-rank tensor traces multiply, so their trace distributions are represented by the product of the block trace functions on the regular product set. Formula (6.11) then contributes the sign
\(\prod_a(-1)^{n_a-r_a}=(-1)^{n-r}\), proving (6.12).

For a nondivisible split block, (6.6) has no solution, because every sum of the matching polynomial's irreducible factor degrees is divisible by \(d\). The empty sum in (6.9) proves vanishing. On an elliptic regular element the polynomial has a single irreducible factor: its centralizer modulo the centre is compact exactly in this case. Indeed a product of at least two field factors has a noncompact valuation direction in \(\prod E_i^\times/F^\times\); for a single field its valuation quotient is finite and its units modulo base units are compact. No proper positive-block partition can allocate that single factor. Again (6.9) is empty. \(\square\)

For example, if \(D_0\) is quaternion division and \(r=2\), a matching polynomial with two distinct irreducible quadratic factors has two fixed flags for the parabolic of sizes \(1+1\). They correspond to the two orders of those factors, exactly the flags for split block sizes \(2+2\). A matching irreducible quartic has no such flag. Split induction from block sizes \(1+3\) has zero character on both kinds of matching polynomial. The sign for two block correspondences is \((-1)^{2-1}(-1)^{2-1}=1=(-1)^{4-2}\). None of these assertions identifies a constituent of a reducible induction: that further step is required for the extended unitary correspondence.

Badulescu's free 2002 article, printed pp. 735–737, gives the corresponding Levi and Jacquet-module comparison framework, with additional exponent hypotheses for Jacquet restriction. The argument above concerns normalized **induction** and proves its fixed-flag trace formula directly. It does not infer that an arbitrary character identity automatically passes to Jacquet modules, nor use an elliptic induced character to prove the existence of discrete-series transfer.

### 6.3. Elliptic tori, Weyl measure and the comparison space

The parabolic vanishing just proved leaves the elliptic regular set as the natural place for a discrete-series character comparison. We now identify its measure on the two groups. This does not assume character orthogonality.

**Lemma 6.6 — elliptic tori in an inner form.** The conjugacy classes of elliptic regular-centralizer tori in \(G_A=\mathrm{GL}_r(D_0)\) are in bijection with the \(F\)-isomorphism classes of separable field extensions \(E/F\) of degree \(n=rd\). The torus is \(T_E=E^\times\), embedded in \(M_r(D_0)^\times\). Its rational Weyl group is
\[
 W_E=N_{G_A}(E^\times)/E^\times
       \simeq\operatorname{Aut}_F(E).
\tag{6.13}
\]
Its quotient by the centre \(Z=F^\times\) is compact. The same fields and Weyl groups occur in \(\mathrm{GL}_n(F)\).

**Proof.** The regular centralizers of Theorem 6.2 are the multiplicative groups of the separable algebras \(\prod E_i\). This group modulo \(F^\times\) is compact exactly when there is one factor, by the valuation-direction argument in Corollary 6.5. For a field of degree \(n\), Lemma 6.1 says that it splits \(D_0\), since \(d\mid n\); the column-module construction in Theorem 6.2 embeds it as a maximal commutative subalgebra of \(M_r(D_0)\). Thus every field in the assertion occurs.

An embedded separable algebra of dimension \(n\) is self-centralizing: after a separable splitting field it is the diagonal algebra in \(M_n\), and the centralizer equations are linear over \(F\). The tori used in this subsection are these regular centralizers, so the compactness test makes their elliptic cases precisely the fields. The formula below only integrates regular elements; all of its tori arise this way. Conjugate embeddings give isomorphic fields. For the converse, choose a primitive element \(t\) in one field and its image in the other. Theorem 6.2 gives a conjugating matrix for these two elements, and it consequently conjugates every polynomial in them. This proves uniqueness of the torus class.

Here a primitive element can be found without a choice of an algebraic closure coordinate: the finite normal closure of a finite separable extension has a finite Galois group, hence finitely many intermediate fields. Each proper one is a proper \(F\)-linear subspace of \(E\). A finite union of proper subspaces cannot cover a vector space over the infinite field \(F\): choose a nonzero linear functional vanishing on each subspace; their product is a nonzero polynomial, which cannot vanish everywhere by the one-variable root bound and induction on the number of variables. An element outside their union generates \(E\).

An element normalizing \(E^\times\) normalizes its \(F\)-linear span \(E\), so acts by an \(F\)-automorphism. The kernel is its centralizer \(E^\times\). Every \(F\)-automorphism \(\tau\) is realized by conjugation, by applying the same regular-class argument to \(t\) and \(\tau(t)\). This proves (6.13); its order is finite, at most \(n\), because an automorphism is determined by the image of \(t\), which is a root of its degree-\(n\) polynomial. This order is generally not \(n!\).

Finally \(v_E(F^\times)=e(E/F)\mathbb Z\). Every class in \(E^\times/F^\times\) consequently has a representative of valuation in \(\{0,\ldots,e-1\}\). The corresponding finite union of translates of \(\mathcal O_E^\times\) is compact and maps onto the quotient. The centre is closed, so the quotient is a compact Hausdorff group. The split case of the proof is \(d=1\). \(\square\)

Fix one Haar measure \(dz\) on \(F^\times\). On every \(T_E\), use the Haar measure \(dt\) for which the quotient measure \(d\bar t=dt/dz\) on \(T_E/Z\) has total volume one. Field isomorphisms preserve these measures: they fix \(F\), and their pushforward quotient Haar measure has the same total mass. On either group fix Haar measure \(dg\), and let \(d\dot x=dg/dt\) on \(T_E\backslash G_A\). The quotient \(G_A/Z\) has measure \(d\bar g=dg/dz\).

**Theorem 6.7 — the elliptic Weyl formula.** If \(\phi\) is a compactly supported locally constant function on the elliptic regular part of \(G_A/Z\), then
\[
 \int_{G_A/Z}\phi(\bar g)\,d\bar g
 =\sum_{[E:F]=n}\frac1{|\operatorname{Aut}_F(E)|}
   \int_{T_{E,\mathrm{reg}}/Z}\Delta_{G_A}(t)
      \int_{T_E\backslash G_A}
          \phi(\overline{x^{-1}tx})\,d\dot x\,d\bar t.
\tag{6.14}
\]
The sum is over field isomorphism classes. It is at most countable, is finite on any one such compact regular support, and the formula also holds for nonnegative measurable functions by increasing approximation, allowing infinite values.

**Proof: the local change of variables.** Put \(A=M_r(D_0)\). The explicit measure
\(dg=|\operatorname{Nrd}(g)|_F^{-n}da\), up to a positive constant, is both left and right Haar measure: left and right multiplication on \(A\) each has determinant \(\operatorname{Nrd}(g)^n\), as follows after splitting from the \(n\) matrix columns or rows. The additive measure \(da\) transforms by the absolute value of that determinant. Thus the group is unimodular. The torus is abelian and unimodular too, so the indicated quotient Haar measures exist.

For \(t\in E^\times\) regular, the linear map \(1-\operatorname{Ad}(t)\) has kernel \(E\). After separable splitting, its image is the off-diagonal matrix space and its kernel the diagonal space; hence
\(A=E\oplus(1-\operatorname{Ad}(t))A\) over \(F\) as well. In local matrix coordinates, the conjugation map
\[
 (T_E\backslash G_A)\times T_{E,\mathrm{reg}}
       \longrightarrow G_A,
 \qquad (T_Ex,t)\longmapsto x^{-1}tx
\tag{6.15}
\]
has derivative given by the identity on the torus direction and by
\(1-\operatorname{Ad}(t)\) on \(A/E\), after tangent translation to the identity. It is invertible. The inverse/change-of-variables argument in Theorem 6.4 therefore applies, in either characteristic, and its absolute determinant is precisely \(\Delta_{G_A}(t)\). Passing to the central quotients removes the same one-dimensional tangent and Haar factor from the torus and target, so leaves this determinant unchanged.

To check the measure normalization, choose additive coordinates on \(E\) and a complement in \(A\). Calibrate the quotient coordinate measure at the identity by \(dg=dt\,d\dot x\). Right translation then gives the same calibration at every \(t\). This cancels the torus-coordinate determinant against the torus Haar density; the remaining determinant on the complement is exactly the one in (6.5). Rescaling \(dt\) rescales \(d\dot x\) inversely. Consequently no independent scalar or maximal-compact volume is left in (6.14).

**Proof: the covering and its multiplicity.** If two points in (6.15) give the same regular element, their torus elements have the same minimal polynomial. The conjugator normalizes the field they generate. Lemma 6.6 makes all the resulting identifications exactly the rational Weyl group \(\operatorname{Aut}_F(E)\), acting on the torus and the left cosets together. Its action on this product is free, because a normalizer element fixing a left coset belongs to the torus. Every fibre has that group's order. The same count holds after quotienting the target and torus by \(Z\): choose representatives giving equality before quotienting by absorbing their central scalar into the torus representative. The derivative calculation gives local inverse charts for this finite covering. Integrating on these charts and dividing by the covering degree proves (6.14) for a function supported in one chart.

Every point in the elliptic regular set has such a chart. In particular the union of the conjugates of \(T_{E,\mathrm{reg}}\) is open. Different field isomorphism classes give disjoint open unions, since a regular element generates its field. The group is second countable: balls in a finite-dimensional \(F\)-coordinate space have a countable basis, obtained from finite residue digits and integral powers of a uniformizer; matrix inversion restricts this to \(G_A\), and the quotient map to \(G_A/Z\) is open. A disjoint family of nonempty open sets in a second-countable space is countable, by assigning a distinct basis element contained in each. Thus the field sum is countable even in positive characteristic. We do not assume that there are finitely many extensions of degree \(n\).

A compact subset of the elliptic regular set is covered by finitely many of these inverse-chart images. Compact-open refinement gives a finite disjoint partition subordinate to the cover, so adding the chart formula proves the displayed assertion and gives only finitely many field types on that support. Finally, both sides define positive measures agreeing on compact-open chart sets. Those sets have a countable basis closed under finite intersections, so disjoint refinement gives agreement on open sets; closure under relative complements and disjoint countable unions gives agreement on their generated Borel sets. Exhaust by compact-open sets to handle infinite total mass. Approximate a nonnegative measurable function from below by simple functions and apply monotone convergence. This proves the last assertion. \(\square\)

**Corollary 6.8 — the elliptic comparison is an isometry.** Let \(\omega\) be a unitary character of \(F^\times\). For locally constant conjugacy-invariant functions \(f,h\) on the elliptic regular set satisfying \(f(zg)=\omega(z)f(g)\), define
\[
 \langle f,h\rangle_{\mathrm{ell},G_A}
 =\sum_{[E:F]=n}\frac1{|\operatorname{Aut}_F(E)|}
   \int_{T_{E,\mathrm{reg}}/Z}
      \Delta_{G_A}(t)f(t)\overline{h(t)}\,d\bar t,
\tag{6.16}
\]
whenever their squared norms are finite. The centre condition makes the integrand well defined. Pulling a function between matching elliptic regular classes gives an isometric bijection between these spaces for \(G_A\) and \(\mathrm{GL}_n(F)\). Multiplying that map by \((-1)^{n-r}\) is also an isometry. Thus a proved character relation transports an orthogonality identity; the isometry alone asserts no character relation or existence theorem.

**Proof.** Theorem 6.2 identifies the two elliptic class sets by their irreducible separable degree-\(n\) polynomials. Lemma 6.6 identifies their field tori, rational Weyl groups and normalized torus measures. Their discriminants agree: over a separable splitting field, both adjoint quotients have the eigenvalues \(\alpha_i/\alpha_j\), \(i\ne j\), so (6.5) is the absolute value of the same element \(\prod_{i\ne j}(1-\alpha_i/\alpha_j)\in F\). Every summand in (6.16) is therefore the same. Cauchy–Schwarz on the disjoint union of the weighted torus measure spaces gives absolute convergence for the mixed pairing from the two finite squared norms.

The class pullback preserves local constancy in both directions: the inverse charts of (6.15) make it the same regular torus function in a neighbourhood, while conjugacy invariance fixes its other coordinates. It preserves the central character because the same scalar multiplies the polynomial roots on both sides. The inverse class matching is its inverse. This proves the isometry and surjectivity. A sign of absolute value one changes neither pairing nor norm.

For completeness this is a positive definite pairing on these locally constant functions. Its density is strictly positive on each regular torus. A nonzero locally constant value persists on a nonempty open subset of such a torus and hence has positive norm; the local inverse chart ensures that every nonzero class function has such a restriction. The nonregular elements of a torus have measure zero: their discriminant is a nonzero polynomial in its \(F\)-coordinates, and the zero set of a nonzero polynomial has additive Haar measure zero, by induction on the number of variables, the finite one-variable root bound and Fubini. On compact open multiplicative charts, additive and multiplicative Haar measures differ by a bounded nonzero density. The exceptional set is central-invariant; quotient Haar integration on a compact central neighbourhood therefore gives measure zero in \(T_E/Z\) as well. Thus omitting this set introduces no measure defect. Completing the two finite-norm spaces gives isometric Hilbert spaces as well. \(\square\)

For a cubic field with no nontrivial \(F\)-automorphism the weight in (6.16) is one, whereas for a cyclic cubic it is \(1/3\). These are rational Weyl groups, not the six permutations of the roots in a splitting field. In residue characteristic dividing \(n\), the trace of the identity matrix can vanish; the determinant argument still uses the off-diagonal quotient, on which all \(1-\alpha_i/\alpha_j\) are nonzero. No division by \(n\) entered the proof.

The comparison space and torus normalization can be compared with Badulescu 2002, Appendix 6, printed pp. 745–746. The proofs above supply the field/normalizer identification, the actual change of variables, countability and the measure matching. The higher-degree discrete-series orthogonality and completeness assertions remain separate from this geometric measure calculation.

### 6.4. Division-group characters: orthogonality, completeness and test functions

Continue with the nonarchimedean field of Section 6.1. Take \(r=1\), put \(D=D_0\), and write \(d=\deg D\), \(G=D^\times\), \(Z=F^\times\). This subsection proves the representation-theoretic assertions for the division group in every degree and either characteristic. The elliptic measure remains that of Section 6.3. The noncompact groups \(\mathrm{GL}_r(D)\), \(r>1\), require their additional discrete-series argument.

**Lemma 6.9 — finite quotients and every smooth irreducible.** Every irreducible smooth complex representation of \(D^\times\) is finite-dimensional and has a smooth central character. It becomes a representation of a finite group after an unramified reduced-norm twist. For every smooth unitary character \(\omega\) of \(F^\times\), there are irreducible representations with central character \(\omega\); all of them are unitarizable and square-integrable modulo the centre.

**Proof: the finite quotient.** Use the valuation of Section 6.2, normalized by \(v_D(D^\times)=\mathbb Z\) and \(v_D|_{F^\times}=d v_F\). Its ring \(\mathcal O_D\) is compact. For \(m\ge1\), put
\[
 U_m=1+\mathfrak p_D^m,
 \qquad H_m=D^\times/(U_m\langle\varpi_F\rangle).
\tag{6.17}
\]
The geometric series proves that \(U_m\) is a group. The valuation identity
\(v_D(gxg^{-1})=v_D(x)\) makes it normal in \(D^\times\), and these groups form a neighbourhood basis of the identity. The quotient \(H_m\) is finite: modulo the central \(\varpi_F\) every element has valuation in \(\{0,\ldots,d-1\}\), and the unit quotient \(\mathcal O_D^\times/U_m\) is finite by compactness. The same valuation representatives prove that \(G/Z\) is compact.

Let \(V\) be any smooth irreducible. A nonzero vector is fixed by some \(U_m\). Normality makes its fixed space \(G\)-invariant, hence equal to \(V\). Thus \(U_m\) acts trivially. Let \(t\) denote the action of the central \(\varpi_F\), and set \(R=\mathbb C[t,t^{-1}]\). The group algebra of \(G/U_m\) is a finite module over this central ring, because \(\langle\varpi_F\rangle\) has finite index. Irreducibility makes \(V\) cyclic over the group algebra, so it is finitely generated over \(R\).

Its \(R\)-torsion is a \(G\)-submodule. If it were zero, \(V\) would be a nonzero finite free \(R\)-module. Here is the elementary module fact being used: Laurent-polynomial ideals are principal, by clearing a power of \(t\) and using polynomial division. The same Euclidean row and column operations diagonalize a finite presentation matrix; whenever a pivot does not divide an entry, division replaces it by a remainder of smaller degree. Termination gives a direct sum of a free module and cyclic torsion modules. A submodule of \(R^N\) is finitely generated by the coordinate-ideal induction, so a finitely generated module has such a finite presentation. This proves the asserted freeness in the torsion-free case. But then \((t-1)V\) would be a nonzero proper \(G\)-submodule: multiplication is injective on a free module and its quotient has positive complex dimension. This contradicts irreducibility. The torsion is therefore nonzero, hence all of \(V\). Finitely many generators are killed by one nonzero Laurent polynomial. Its quotient ring is finite-dimensional over \(\mathbb C\), proving \(\dim V<\infty\).

Every central operator on this finite-dimensional irreducible is scalar: choose one eigenvalue and use the invariant nonzero eigenspace. Its scalars give a character \(\omega\); smoothness of the representation makes the character smooth. Choose an unramified character \(\eta:F^\times\to\mathbb C^\times\) with
\(\eta(\varpi_F)^d=\omega(\varpi_F)\), and put
\(\pi_0=\pi\otimes(\eta\circ\operatorname{Nrd})^{-1}\).
The reduced norm of a central scalar is its \(d\)-th power. Hence \(\pi_0(\varpi_F)=1\), and the unramified twist is trivial on \(U_m\). Indeed left multiplication by a unit preserves the integral lattice, so its determinant \(\operatorname{Nrd}(u)^d\) is a base-field unit; hence \(\operatorname{Nrd}(u)\) is a unit as well. Thus \(\pi_0\) factors through the actual finite group \(H_m\). This proves the finite-image assertion, including when the residue characteristic divides \(d\).

**Proof: a fixed unitary central character.** Fix \(\omega\) unitary, choose the root \(\eta(\varpi_F)\) on the unit circle, and write
\(\omega_0=\omega\,\eta^{-d}\). Then \(\omega_0(\varpi_F)=1\).
For sufficiently large \(m\), it is trivial on \(Z\cap U_m\), and hence defines a character of the finite central subgroup
\(C_m=Z/(Z\cap U_m\langle\varpi_F\rangle)\) of \(H_m\).
This character occurs in a representation of \(H_m\): functions satisfying
\(s(ch)=\omega_0(c)s(h)\) form a nonzero finite-dimensional induced representation, and any irreducible summand has that central character. The finite group is completely reducible, since averaging a positive inner product makes invariant orthogonal complements available. Twisting such a summand by \(\eta\circ\operatorname{Nrd}\) constructs a representation of \(G\) with central character \(\omega\).

Conversely every irreducible with this character factors through such an \(H_m\) after the same unitary twist, by the first part. Averaging an inner product over the finite group and restoring the unitary twist makes it unitary. Its matrix coefficients have bounded absolute value, and the absolute value is defined on the compact quotient \(G/Z\). They are square-integrable there. For a nonunitary central character, the same construction removes its modulus by a real unramified norm power; thus every smooth irreducible of \(D^\times\) is essentially square-integrable. \(\square\)

Fix for the moment quotient Haar measure of total mass one on \(G/Z\). For functions with central transformation \(\omega\), their inner products mean integrals of the central-invariant products on this quotient; the functions themselves need not descend to the quotient.

**Theorem 6.10 — character orthogonality and the complete elliptic basis.** For the fixed smooth unitary \(\omega\), the characters \(\chi_\pi\) of all irreducible smooth representations with that central character form a complete orthonormal basis of the Hilbert completion of the elliptic class-function space in (6.16). In particular
\[
 \langle\chi_\pi,\chi_\tau\rangle_{\mathrm{ell},D^\times}
       =\begin{cases}1,&\pi\simeq\tau,\\0,&\pi\not\simeq\tau.\end{cases}
\tag{6.18}
\]
Their characters are ordinary finite-dimensional traces and extend to locally constant functions on the entire group. For an arbitrary quotient Haar volume \(v>0\), their formal degrees are
\[
 d(\pi)=\frac{\dim\pi}{v}.
\tag{6.19}
\]

**Proof: Schur orthogonality with the fixed centre.** Put \(N=\dim\pi\). For an operator \(A:V_\tau\to V_\pi\), average
\[
 \int_{G/Z}\pi(g)A\tau(g)^{-1}\,d\bar g.
\tag{6.20}
\]
The common central character cancels, so this is well defined. Haar invariance makes it an intertwiner. It is zero for inequivalent irreducibles: a nonzero intertwiner has invariant kernel and image and is an isomorphism. For \(\tau=\pi\), every intertwiner is scalar by the eigenspace argument in Lemma 6.9; taking traces makes (6.20) equal to \(\operatorname{tr}(A)I/N\). Apply this to matrix units and sum the diagonal coefficient identities. It gives
\(\int_{G/Z}\chi_\pi(g)\overline{\chi_\tau(g)}d\bar g=\delta_{\pi\tau}\).
For a quotient of volume \(v\), the same calculation gives
\[
 \int_{G/Z}|\langle\pi(g)u,w\rangle|^2d\bar g
 =\frac{v}{N}\|u\|^2\|w\|^2,
\tag{6.21}
\]
which is exactly the formal-degree assertion.

**Proof: the elliptic integral is the quotient integral.** Every regular semisimple element of a division algebra has irreducible reduced polynomial. Its minimal polynomial is irreducible because the subalgebra it generates is a field; regularity makes this polynomial have degree \(d\). Thus its regular set is elliptic. The complement has measure zero: the reduced discriminant is a nonzero polynomial on the algebra, since the degree-\(d\) separable field embeddings of Lemma 6.6 give a point where it is nonzero. The polynomial-zero-set argument in Corollary 6.8 applies to additive Haar measure, and hence to multiplicative Haar measure on compact charts. Its central quotient has measure zero by quotient integration.

For a torus \(T_E\), the normalized measures have
\(\operatorname{vol}(G/Z)=\operatorname{vol}(T_E/Z)=1\), so
\(\operatorname{vol}(T_E\backslash G)=1\), by integrating the constant function in quotient stages. For a conjugacy-invariant integrand the inner orbital integral in (6.14) is therefore the function itself. The Weyl formula identifies (6.16) with the ordinary quotient inner product just computed. It also identifies their finite-norm completions: a class function on the regular set extends by zero on its null complement. This proves (6.18).

**Proof: completeness, including the singular boundary.** We give the approximation argument; local constancy on the regular set alone need not give boundedness near the singular set. Let \(f\) have finite norm, extend it by zero as above, and average on the right:
\[
 A_mf(g)=\frac1{\operatorname{vol}(U_m)}
             \int_{U_m}f(gu)\,du.
\tag{6.22}
\]
For large \(m\), \(\omega\) is trivial on \(Z\cap U_m\). These are contractions in quotient \(L^2\), by the integral Cauchy–Schwarz inequality and Haar invariance. Normality of \(U_m\), and invariance of its normalized Haar measure under conjugation, preserve the class-function condition; central equivariance is preserved as well. The average is right \(U_m\)-invariant.

Moreover \(A_mf\to f\) in \(L^2\). To check this without a pointwise boundary assertion, choose \(m_0\) with \(\omega|_{Z\cap U_{m_0}}=1\). The finitely many cosets \(g_iZU_{m_0}\) cover \(G\). On each one, a central-equivariant function is exactly a function on the compact profinite quotient \(U_{m_0}/(Z\cap U_{m_0})\), by the rule \(f(g_i zu)=\omega(z)f_i(u)\). It is independent of the representative because \(\omega\) is trivial on that intersection. Its \(L^2\) measure is a fixed multiple of quotient Haar measure on this chart.

The finite coset partitions given by the images of \(U_m\), \(m\ge m_0\), form a countable basis and generate its Borel sets. Step functions on these partitions are dense in \(L^2\). For the elementary measure justification, the sets approximable in measure by finite unions of partition cells include the cells, are closed under complements, and are closed under countable unions: first take a sufficiently large finite union, using continuity of a finite measure, then approximate its finitely many terms in one common partition. They therefore include every Borel set. Simple-function approximation proves the asserted density. There are only finitely many charts. Extend these step functions by their central rule; each is right invariant by one common sufficiently small \(U_m\), and all its later averages equal itself. The contractions in (6.22) now give convergence for every \(f\). No value or bound at a singular element is used.

Use the one fixed unitary twist \(\eta\) of Lemma 6.9. The function
\(f_m^0(g)=(\eta\circ\operatorname{Nrd})(g)^{-1}A_mf(g)\)
is invariant under \(U_m\) and the central \(\varpi_F\); it is therefore a class function on the finite group \(H_m\), with central character \(\omega_0\) on \(C_m\). Finite-group irreducible characters with that central character form a basis of this finite class-function space. Here is the finite completeness step. Averaging an inner product proves complete reducibility of the regular representation. Every irreducible is a quotient of the regular representation, by sending its identity basis vector to a nonzero generating vector. Schur orthogonality shows that its multiplicity in the regular representation is its dimension. Hence the squared dimensions sum to the group order. The action of the group algebra on the sum of all irreducibles is injective, because an element annihilating them annihilates the decomposed regular representation. The dimension equality therefore makes this action the full direct sum of matrix algebras. Equivalently all their matrix coefficients span all functions. Averaging these functions under conjugation kills the nonscalar matrix components and leaves precisely the irreducible characters. Finally the central projection
\(|C_m|^{-1}\sum_{c\in C_m}\omega_0(c)^{-1}R_c\), where \((R_cf)(h)=f(ch)\),
keeps exactly their \(\omega_0\)-parts. This proves the fixed-centre character basis without assuming a compact-group completeness theorem.

Restoring \(\eta\circ\operatorname{Nrd}\) shows that every \(A_mf\) is a finite linear combination of the characters of \(G\) with central character \(\omega\). Their union is dense by (6.22). There are at most countably many such irreducibles, because for this one fixed twist they occur in the finite groups \(H_m\), \(m\ge1\). Schur orthogonality therefore gives the asserted complete orthonormal basis. In particular Parseval's identity follows by finite orthogonal projection and this convergence. \(\square\)

**Proposition 6.11 — actual central projectors and trace-one tests.** Let the quotient Haar volume be \(v\). In the central Hecke space of locally constant functions \(a(zg)=\omega(z)^{-1}a(g)\), compact modulo \(Z\), define
\[
 e_\pi(g)=\frac{\dim\pi}{v}\overline{\chi_\pi(g)},
 \qquad p_\pi(g)=\frac1v\overline{\chi_\pi(g)}.
\tag{6.23}
\]
These are genuine test functions. For every irreducible \(\tau\) with central character \(\omega\),
\[
 \tau(e_\pi)=\delta_{\pi\tau}I_{V_\tau},
 \qquad
 \operatorname{tr}\tau(p_\pi)=\delta_{\pi\tau},
 \qquad
 e_\pi*e_\tau=\delta_{\pi\tau}e_\pi.
\tag{6.24}
\]
Convolution and operator integrals are over \(G/Z\). The inverse central transformation of a test makes every integrand independent of its quotient representative.

**Proof.** Characters are locally constant on the entire group by Lemma 6.9, and \(G/Z\) is compact. Thus (6.23) satisfies all the stated test conditions. The matrix-unit identities from (6.20) give
\(\int_{G/Z}\overline{\chi_\pi(g)}\tau(g)d\bar g
=\delta_{\pi\tau}vI/\dim\pi\).
This proves the first two formulas, with all dimension factors shown. Applying that same identity to the translated character in the convolution gives the last formula. Alternatively the two sides are central test functions at one common finite level; their finite Fourier transforms agree at every irreducible, so finite completeness in Theorem 6.10 makes them equal. Notice that the projector's trace on \(\pi\) is \(\dim\pi\); the trace-one test is \(p_\pi\), not \(e_\pi\). \(\square\)

**Corollary 6.12 — a complete transferred elliptic basis, with its exact limit.** On the split elliptic regular set of \(\mathrm{GL}_d(F)\), define
\[
 b_\pi(g)=(-1)^{d-1}\chi_\pi(g'),
 \qquad g\leftrightarrow g'\in D^\times.
\tag{6.25}
\]
For fixed unitary \(\omega\), these functions form a complete orthonormal basis of the finite-norm elliptic class-function completion for \(\mathrm{GL}_d(F)\).

**Proof.** Apply the isometry and surjectivity of Corollary 6.8 to the complete basis of Theorem 6.10. The sign has absolute value one and is the required division-group sign in (6.1). This proves the assertion as a theorem about class functions. It does not prove that each \(b_\pi\) is the character of a square-integrable representation of \(\mathrm{GL}_d(F)\). That representation-existence step, its every-regular-class character identity, and the noncompact inner forms' orthogonality remain required for the full higher-degree local correspondence. \(\square\)

**Corollary 6.13 — the actual minimal-parabolic character in every rank.** Let \(\rho_1,\ldots,\rho_r\) be arbitrary irreducible smooth representations of \(D^\times\). The normalized induction from the upper triangular parabolic in \(\mathrm{GL}_r(D)\) is admissible and has a locally constant trace function on the entire regular set. It is zero unless the reduced polynomial has exactly \(r\) distinct irreducible factors of degree \(d\). In that case choose \(x_i\in D^\times\) with the polynomial of the \(i\)-th factor. Its trace is
\[
 \begin{gathered}
 \Theta_{I_B(\boxtimes_a\rho_a)}(g)
 =\left(\frac{\prod_{i=1}^r\Delta_{D^\times}(x_i)}
                    {\Delta_{\mathrm{GL}_r(D)}(g)}\right)^{1/2}
       \sum_{s\in S_r}\prod_{a=1}^r\chi_{\rho_a}(x_{s(a)}).
 \end{gathered}
\tag{6.26}
\]
No unitary or irreducibility hypothesis on the induced representation is required.

**Proof.** Lemma 6.9 gives finite-dimensional smooth inducing representations and their actual everywhere trace functions, so all the inducing hypotheses of Theorem 6.4 hold. Every factor degree of a regular polynomial in \(\mathrm{GL}_r(D)\) is divisible by \(d\), by Theorem 6.2. Allocating it to \(r\) blocks each of reduced size \(d\), as in Lemma 6.3, is therefore possible precisely when each block receives one factor of degree \(d\). Those allocations are the \(r!\) permutations. Their Levi discriminants are the same product \(\prod_i\Delta_{D^\times}(x_i)\). Formula (6.9) gives (6.26), and gives zero when there are no allocations. This is the trace of the whole induction. It does not separate its irreducible subquotients or assert a discrete-series transfer. \(\square\)

For a concrete fixed-centre example, let \(F=\mathbb Q_3\) and let \(D\) be quaternion division. In its unramified cyclic model choose \(\Pi^2=3\). Reduction of units modulo \(U_1\) gives \(\mathbb F_9^\times\), cyclic of order eight: if \(i^2=-1\) in this field, \((1+i)^4=-1\) and \((1+i)^8=1\), so \(1+i\) is a generator. Conjugation by \(\Pi\) is the cube map. Hence
\(H_1=D^\times/(U_1\langle3\rangle)=\langle a,b:a^8=b^2=1,\ bab^{-1}=a^3\rangle\), and the residual centre is \(C=\langle a^4\rangle\).
For trivial central character it factors further to the dihedral group of order eight: there are four lines and one irreducible of dimension two. For the character taking \(a^4\) to \(-1\), there are two irreducibles of dimension two. To verify the latter directly, the nonfixed character orbits of \(\langle a\rangle\) under multiplication by three are
\(\{1,3\},\{2,6\},\{5,7\}\) modulo eight. Induction from a line on this cyclic subgroup gives dimension two; the two coset weights are distinct and exchanged, so it is irreducible. The first and third orbits have the negative central character, and the middle one has the positive character. The fixed weights zero and four each extend with \(b\mapsto\pm1\), giving the four positive-central lines. The sum of squared dimensions is \(4+3\cdot4=16=|H_1|\), so finite completeness gives every irreducible. In each central-character space the squared dimensions sum to eight, and (6.19), (6.23) and (6.24) have exactly the stated factors. This finite level illustrates the fixed-centre construction; Lemma 6.9 and Theorem 6.10 use every level.

Badulescu 2002, Appendix 6, printed p. 745, identifies the compact-mod-centre division case of the elliptic character theory. The finite-quotient and fixed-centre constructions above give the orthogonality, completeness and projector formulas, including the approximation at the singular boundary.

### 6.5. Noncompact coefficient orthogonality and compact trace tests

Put \(G=\mathrm{GL}_r(D_0)\) and \(Z=F^\times\), with no restriction on \(r\), the degree of \(D_0\), or the characteristic of \(F\). Fix a smooth unitary central character \(\omega\) and quotient Haar measure \(d\bar g\) on \(G/Z\). Theorem 6.7 proves unimodularity. Write \(\mathcal L_\omega\) for the Hilbert space of measurable functions \(f(zg)=\omega(z)f(g)\) with finite quotient squared norm. Products defining its inner product descend to \(G/Z\). Both translations are unitary. All Hilbert inner products below are linear in the first variable.

Here an admissible unitary representation means a strongly continuous unitary representation on a Hilbert space \(H_\pi\), with finite-dimensional \(H_\pi^K\) for every compact open \(K\). Smooth vectors are dense: averaging over sufficiently small compact open subgroups converges to the identity, by strong continuity. We work with irreducible such representations. An admissible smooth irreducible with an invariant positive inner product has an irreducible Hilbert completion. The fixed spaces in the completion equal the original ones: averaging the dense original space is dense in each completed fixed space, and its original fixed space is finite-dimensional and therefore closed. Indeed a closed invariant subspace has a commuting orthogonal projection; this projection preserves every finite-dimensional fixed space, hence the smooth vectors. Its kernel and image there are invariant, and smooth irreducibility makes the projection zero or the identity.

**Lemma 6.14 — a closed coefficient map is bounded.** Let \(\pi\) be irreducible and admissible unitary. Fix \(v\in H_\pi\), and define
\[
 \begin{gathered}
 T_vu(g)=\langle\pi(g)u,v\rangle,\\
 \mathcal D_v=\{u\in H_\pi:T_vu\in\mathcal L_\omega\}.
 \end{gathered}
\tag{6.27}
\]
If this domain contains a nonzero vector with nonzero coefficient, then \(\mathcal D_v=H_\pi\), and \(T_v\) is bounded with \(T_v^*T_v=a_vI\) for some \(a_v>0\).

**Proof.** The domain is linear and invariant: \(T_v\pi(h)u=R_hT_vu\). Its closure is a nonzero invariant subspace, hence all of \(H_\pi\). The map is closed. In fact, if \(u_j\to u\) and \(T_vu_j\to f\) in \(L^2\), choose a subsequence with the sum of squared \(L^2\) errors finite. Integrating that sum shows convergence to \(f\) almost everywhere. On the other hand the coefficients converge uniformly to \(T_vu\), since their difference is bounded by \(\|u_j-u\|\|v\|\). Thus \(f=T_vu\) almost everywhere, as required.

Give \(\mathcal D_v\) its graph inner product
\(\langle u,w\rangle_T=\langle u,w\rangle+\langle T_vu,T_vw\rangle\).
It is complete by closedness. For \(x\in H_\pi\), there is a unique \(Rx\in\mathcal D_v\) satisfying
\[
 \langle Rx,y\rangle+\langle T_vRx,T_vy\rangle
       =\langle x,y\rangle\qquad(y\in\mathcal D_v).
\tag{6.28}
\]
Here the functional on the right is bounded in graph norm. The Hilbert representation fact used to obtain \(Rx\) has the following elementary proof. A closed subspace has a nearest point: the parallelogram identity makes any minimizing sequence Cauchy, and completeness supplies its limit; the minimizing difference is orthogonal to the subspace. For a nonzero bounded antilinear functional, project onto its closed kernel. Its orthogonal complement is one-dimensional, since subtracting a suitable multiple of any vector outside the kernel sends every vector into the kernel. The value on that one dimension gives its unique representing vector. Apply this in the graph Hilbert space.

Setting \(y=Rx\) gives \(\|Rx\|\le\|x\|\), and the same identity gives positivity. Applying (6.28) with \(y=Rz\), and conjugating the equation with \(x,z\) exchanged, gives self-adjointness of \(R\) on \(H_\pi\). It is injective: if \(Rx=0\), then \(x\) is orthogonal to the dense domain. Graph-inner-product invariance makes \(R\) commute with \(\pi\).

Every bounded operator commuting with this representation is scalar. To see this directly, choose a nonzero fixed space \(H_\pi^K\); the operator preserves it and has an eigenvector there over \(\mathbb C\). Its eigenspace in \(H_\pi\) is nonzero, closed and invariant, so is the entire Hilbert space. Apply this to \(R\): it equals \(\lambda I\), where \(0<\lambda\le1\). Its range is contained in \(\mathcal D_v\), so the domain is all of \(H_\pi\). Equation (6.28) now gives
\(\langle T_vu,T_vw\rangle=(\lambda^{-1}-1)\langle u,w\rangle\).
The coefficient was nonzero, so \(\lambda<1\). This proves the assertion without an assumption that an unbounded invariant form is bounded. The same proof applies to the linear map \(w\mapsto\overline{\langle\pi(g)u,w\rangle}\), which intertwines with left translation on \(\mathcal L_{\omega^{-1}}\). \(\square\)

**Theorem 6.15 — full matrix-coefficient Schur orthogonality.** Suppose an irreducible admissible unitary \(\pi\) has one nonzero coefficient in \(\mathcal L_\omega\). Every Hilbert matrix coefficient is then square-integrable modulo the centre. There is a unique \(d_\pi>0\) such that
\[
 \int_{G/Z}\langle\pi(g)u,v\rangle
       \overline{\langle\pi(g)u',v'\rangle}\,d\bar g
 =\frac{\langle u,u'\rangle\langle v',v\rangle}{d_\pi}.
\tag{6.29}
\]
Coefficients of inequivalent such representations with the same central character are orthogonal. Multiplying quotient Haar measure by \(c>0\) replaces \(d_\pi\) by \(d_\pi/c\).

**Proof.** Start with the nonzero coefficient of \(u_0,v_0\). Lemma 6.14 makes the coefficient map with fixed \(v_0\) bounded on all of \(H_\pi\), with norm identity
\(\|T_{v_0}u\|_2^2=a_{v_0}\|u\|^2\).
For every nonzero \(u\), the conjugate-coefficient map with this \(u\) has \(v_0\) in its domain and is nonzero. The last assertion of the lemma makes it bounded and scalar in norm on all \(v\). Evaluating that norm at \(v_0\) gives
\(\|T_vu\|_2^2=a_{v_0}\|u\|^2\|v\|^2/\|v_0\|^2\).
Polarize first in \(u\), then in \(v\). This proves (6.29), with
\(d_\pi=\|v_0\|^2/a_{v_0}>0\).

For inequivalent \(\pi,\tau\), their bounded coefficient maps with fixed second vectors take values in the same \(\mathcal L_\omega\) and intertwine right translation. Thus \((T_w^\tau)^*T_v^\pi\) is a bounded intertwiner from \(H_\pi\) to \(H_\tau\). A nonzero such intertwiner would be a scalar multiple of a unitary isomorphism: its adjoint times itself is a positive scalar by the bounded Schur argument just proved, so its range is closed, nonzero and invariant. Irreducibility makes that range all of \(H_\tau\). Inequivalence therefore makes the intertwiner zero, which is the asserted cross orthogonality. The measure statement follows directly from (6.29). \(\square\)

In particular, the functions \(\sqrt{d_\pi}\langle\pi(g)e_i,e_j\rangle\), for orthonormal bases of \(H_\pi\), form an orthonormal basis of their own closed coefficient space. The space has been defined as the closed span of these coefficients; no assertion that these spaces exhaust the full regular representation is needed. For \(r=1\), comparison with (6.21) recovers \(d_\pi=\dim\pi/\operatorname{vol}(G/Z)\).

**Proposition 6.16 — the smoothed character as a weak conjugation average.** Let \(\pi\) satisfy Theorem 6.15. For every finite-rank operator \(A\) on \(H_\pi\),
\[
 \int_{G/Z}\pi(x)A\pi(x)^{-1}\,d\bar x
             =\frac{\operatorname{tr}A}{d_\pi}I
\tag{6.30}
\]
is an absolutely convergent weak integral: after pairing with any two vectors, the scalar integral is absolutely convergent. Consequently, for every smooth compact-mod-centre test \(f(zg)=\omega(z)^{-1}f(g)\) and every nonzero \(u\),
\[
 \operatorname{tr}\pi(f)
  =\frac{d_\pi}{\|u\|^2}
    \int_{G/Z}\langle\pi(x)\pi(f)\pi(x)^{-1}u,u\rangle\,d\bar x.
\tag{6.31}
\]

**Proof.** Write a rank-one operator as \(Aw=\langle w,b\rangle a\). Its conjugate paired with \(u,v\) is
\(\langle u,\pi(x)b\rangle\langle\pi(x)a,v\rangle\).
These two coefficients are in \(L^2\), so their product is in \(L^1\). Formula (6.29) evaluates its integral as
\(d_\pi^{-1}\langle a,b\rangle\langle u,v\rangle\).
The scalar \(\langle a,b\rangle\) is the rank-one trace. Sum over a finite-rank expression to prove (6.30).

A smooth test with compact support modulo the centre is bi-invariant under some compact open \(K\). Indeed choose finitely many locally constant neighbourhoods over its compact quotient support, intersect their left and right stabilizing subgroups, and use smoothness of \(\omega\) on the central overlaps. Compactness gives one subgroup; the resulting finite union of double cosets also stabilizes the zero extension off the support. Averaging over this \(K\) gives \(\pi(f)=P_K\pi(f)P_K\), where \(P_K\) is projection onto \(H_\pi^K\). Admissibility makes its rank finite. Its quotient operator integral exists since the integrand is central-invariant and the test is integrable there. Apply (6.30) to this operator and pair with \(u,u\). This proves (6.31). In (6.31) the test is integrated first. The proposition asserts this ordered integral; exchanging it with an unregularized conjugation integral for individual group elements requires an additional absolute-integrability argument. \(\square\)

**Theorem 6.17 — compact tests separating any finite discrete-series family.** Let \(\pi_1,\ldots,\pi_s\) be pairwise inequivalent irreducible admissible unitary square-integrable representations of \(G\), with central character \(\omega\). There are smooth compact-mod-centre tests \(f_1,\ldots,f_s\), of inverse central character, such that
\[
 \operatorname{tr}\pi_j(f_i)=\delta_{ji}\qquad(1\le i,j\le s).
\tag{6.32}
\]
One can construct them with a common compact open subgroup and a common compact support modulo the centre.

**Proof: the square-integrable tests and their exact transforms.** Choose one common compact open \(K\) with \(m_i=\dim H_{\pi_i}^K>0\): intersect the stabilizers of one nonzero smooth vector in each representation. Let \(P_i\) be the orthogonal projection onto that space, and put
\[
 p_i(g)=\frac{d_{\pi_i}}{m_i}
                 \overline{\operatorname{tr}(\pi_i(g)P_i)}.
\tag{6.33}
\]
The trace is a finite sum of coefficients of an orthonormal fixed-space basis. These functions are locally constant, bi-\(K\)-invariant and centrally covariant with character \(\omega^{-1}\). Theorem 6.15 gives
\[
 \begin{gathered}
 \|p_i\|_2^2=\frac{d_{\pi_i}}{m_i},\\
 \pi_j(p_i)=
 \begin{cases}P_i/m_i,&j=i,\\0,&j\ne i.\end{cases}
 \end{gathered}
\tag{6.34}
\]
The second formula is initially a weak integral. It is absolutely convergent on each pair of vectors by Cauchy–Schwarz and (6.29), and that formula evaluates it as the displayed bounded operator. It does not assume that \(p_i\) has compact support.

**Proof: compact cutoffs with trace bounds.** The double-coset set \(ZK\backslash G/K\) is countable. The field-coordinate countable basis from Theorem 6.7 makes \(G\) second countable, and its disjoint open double cosets can be assigned distinct basis elements. Their images in \(G/Z\) are compact and open: they are images of \(K\times K\), and \(K\) is open. Enumerate them and let \(\Omega_R\) be the union of the first \(R\), including any repetitions only once. Their union is \(G/Z\). Put \(p_{i,R}=\mathbf1_{\Omega_R}p_i\). These are actual compact-mod-centre bi-\(K\) tests. Monotone convergence for \(|p_i|^2\) gives \(\|p_i-p_{i,R}\|_2\to0\).

Write \(d_j=d_{\pi_j}\). Applying (6.29) to a pair of unit vectors gives an operator-norm error at most \(d_j^{-1/2}\|p_i-p_{i,R}\|_2\). For the trace use the whole finite coefficient
\(q_j(g)=\operatorname{tr}(\pi_j(g)P_j)\), whose squared \(L^2\) norm is \(m_j/d_j\). Both transforms act in the fixed-space corner, and their traces are precisely the corresponding integrals against \(q_j\). Hence
\[
 \left|\operatorname{tr}\pi_j(p_{i,R})-\delta_{ji}\right|
       \le\sqrt{\frac{m_j}{d_j}}\,
                     \|p_i-p_{i,R}\|_2.
\tag{6.35}
\]
The comparison here is with the finite-rank weak transform in (6.34); no continuity of trace on arbitrary bounded operators is being used.

**Proof: exact finite trace separation.** Set \(A_R=(\operatorname{tr}\pi_j(p_{i,R}))_{j,i}\). Equation (6.35) makes this matrix tend entrywise to the identity. Choose one common \(R\) making every entry error smaller than \(1/(2s)\). The row-sum norm of \(I-A_R\) is then less than \(1/2\); its geometric series gives an inverse. Define
\[
 f_i=\sum_{k=1}^s p_{k,R}(A_R^{-1})_{ki}.
\tag{6.36}
\]
Taking traces multiplies the matrix \(A_R\) by its inverse and proves (6.32). All tests have the same fixed subgroup and support inside \(\Omega_R\). This proves the assertion for every finite family in every rank. \(\square\)

For two representations the final algebra is particularly explicit. If the trace matrix is \(\begin{pmatrix}a&b\\c&e\end{pmatrix}\), then
\(f_1=(e p_{1,R}-c p_{2,R})/(ae-bc)\) and
\(f_2=(-b p_{1,R}+a p_{2,R})/(ae-bc)\).
Thus approximate diagonal traces give exact finite separation after one finite matrix inversion.

**A noncompact cutoff computed in full.** Take \(G=\mathrm{GL}_2(F)\), the Steinberg representation, and the measures of Proposition 2.12. Let \(I\) fix the two endpoints of an edge, let \(v\) span the unit \(I\)-fixed line, and let \(J\) be the full edge stabilizer modulo the centre. In the notation of that proof,
\(d_{\mathrm{St}}=(q-1)/2\), \(\operatorname{vol}J=2/(q+1)\), and the coefficient has absolute value \(q^{-l}\) at edge distance \(l\). There are \(2q^l\) right \(J\)-cosets for \(l\ge1\). These counts and coefficient values were proved there by the outward-sum relation and the successive residue-digit action. Choose \(\Omega_R\) to contain the edges of distance at most \(R\). It is a finite union of compact open double cosets modulo the centre. For \(p=d_{\mathrm{St}}\overline{\langle\mathrm{St}(g)v,v\rangle}\), the full tail and cutoff trace are
\[
 \begin{gathered}
 \|p-p_R\|_2^2
 =d_{\mathrm{St}}^2\frac2{q+1}
        \sum_{l>R}2q^{-l}
 =\frac{q-1}{q+1}q^{-R},\\
 \operatorname{tr}\mathrm{St}(p_R)
       =1-\frac2{q+1}q^{-R}.
 \end{gathered}
\tag{6.37}
\]
The second equality integrates \(p_R\) against the one-dimensional fixed-space coefficient, so it is \(d_{\mathrm{St}}\) times the retained coefficient squared norm. For one prescribed representation, division by this positive trace already gives a compact trace-one test. Formula (6.36) gives simultaneous separation for a finite family. In particular this construction includes a discrete series whose coefficients are not compact modulo the centre.

Casselman's freely available Chapter II, §§9–10, gives the square-integrability and formal-degree conventions used here. The closed-domain argument, weak finite-rank averaging and compact cutoff construction above prove the stated assertions directly. Matrix-coefficient orthogonality on \(G/Z\), finite trace separation, and elliptic-character orthogonality are distinct assertions. The latter requires the regular character and orbital-integral comparison; (6.31) specifies the smoothing and order of integration before that comparison.

### 6.6. Compact matrix coefficients, Jacquet modules and elliptic characters

Keep \(G=\mathrm{GL}_r(D_0)\), \(A=M_r(D_0)\), \(n=r\deg D_0\), and \(Z=F^\times\), in either characteristic. This subsection proves an orbital and character formula for every irreducible admissible unitary representation having a nonzero smooth matrix coefficient with compact support modulo the centre. The compactness hypothesis on the coefficient is part of the assertion. No classification of all discrete series by such coefficients is assumed.

For a regular semisimple \(t\), write \(E=F[t]\) and \(T=E^\times\). Section 6.1 identifies \(E\) as a product of separable fields, its centralizer as \(E\), and the degrees of its factors as \(d r_i\), where \(d=\deg D_0\) and \(\sum r_i=r\). Use quotient Haar measure on \(T\backslash G\). For elliptic \(t\), fix the convention of Section 6.3: \(\operatorname{vol}(T/Z)=1\), with the same central measure used to define \(d_\pi\).

**Lemma 6.18 — proper regular orbital coordinates.** The map
\[
 T\backslash G\longrightarrow G,
       \qquad Ty\longmapsto y^{-1}ty
\tag{6.38}
\]
is proper. In particular the orbital integral of a smooth function with compact support modulo \(Z\) is absolutely convergent at every regular semisimple element. With torus measures transported by conjugation, these orbital integrals are locally constant on the regular set. In the elliptic case there is a stronger uniform statement: for compact subsets \(B,C\subset G\), with every element of \(B\) elliptic regular, the set
\[
 \{(x,\bar y)\in B\times G/Z:y^{-1}xy\in C\}
\tag{6.39}
\]
is compact.

**Proof: each simple block has no smaller invariant division subspace.** Let \(e_i\) be the field-factor idempotents of \(E\), and \(W_i=e_iD_0^r\). If a nonzero right \(D_0\)-subspace of \(W_i\) is stable under \(t\), the restriction has minimal polynomial equal to the irreducible factor \(p_i\). Its reduced characteristic polynomial has degree \(d\) times its division dimension and is divisible by this minimal polynomial, by Cayley–Hamilton. Since \(\deg p_i=d r_i\), that dimension is at least \(r_i\). The subspace is therefore \(W_i\). This uses the reduced characteristic-polynomial argument of Theorem 6.2 and works in positive characteristic as well.

**Proof: normalize the rows by the centralizer.** Fix a compact target set \(C\) in (6.38). For any \(y\) with \(y^{-1}ty\in C\), multiply its \(i\)-th component \(e_i y\) by a scalar \(\lambda_i\in F^\times\) making its coordinate maximum norm one. Such scalars exist because that norm takes integral powers of the field absolute value. Left multiplication by \(h=\sum_i\lambda_i e_i\in T\) does not change the image in (6.38). These normalized representatives lie in a bounded subset of the finite-dimensional \(F\)-space \(A\), hence in a compact set.

We show that their closure contains only invertible matrices. For a convergent sequence of representatives \(y_j\to y_0\), pass to a subsequence with \(y_j^{-1}ty_j\to c_0\in C\). The intertwining equation gives \(ty_0=y_0c_0\). The reduced polynomial of \(c_0\) equals that of \(t\), by continuity, so is still separable. Its factor idempotents \(e_i'\) satisfy \(e_i y_0=y_0e_i'\), by polynomial functional calculus and the Chinese remainder identity. Each left side is nonzero, since its norm is one. On the corresponding right \(D_0\)-subspaces, this is a nonzero intertwiner onto \(W_i\), by the preceding irreducibility argument. Domain and target have the same division dimension \(r_i\), so it is an isomorphism. Their sum makes \(y_0\) invertible. The normalized representatives consequently have compact closure inside \(G\). Its image in \(T\backslash G\) contains the closed preimage of \(C\), proving properness.

The same argument works uniformly for \(t\) in a compact neighbourhood inside \(E\) whose elements still generate \(E\) and are regular. The idempotents \(e_i\) are fixed, and every limit has the same block dimensions. Such a neighbourhood exists: invertibility of the coordinate matrix of \(1,t,\ldots,t^{n-1}\), and the reduced discriminant, are open conditions. Thus the inverse images of one compact target set are contained in a common compact subset of \(T\backslash G\).

**Proof: central supports and local constancy.** A compact subset of \(G/Z\) has compact representatives in \(G\). Indeed a matrix coordinate which is nonzero can be scaled to one; the resulting projective coordinate charts identify \(G/Z\) with the open invertible part of the projective space of \(A\), and a compact set is covered by finitely many relatively compact such charts. If the support of \(c\) is compact modulo \(Z\), choose these representatives \(C_0\). A conjugate of \(t\) has the fixed absolute reduced norm \(|\operatorname{Nrd}(t)|\). If it is \(zc_0\), \(c_0\in C_0\), then \(|z|^n|\operatorname{Nrd}(c_0)|=|\operatorname{Nrd}(t)|\). The possible \(z\)'s lie in a compact annulus. Hence the part of the support met by the orbit is contained in an actual compact subset of \(G\). Properness now proves absolute convergence of its orbital integral.

For \(t\) in the compact neighbourhood just chosen, the same annulus and uniform properness apply. The integrands are locally constant on the product of that neighbourhood and the common compact orbital support. A finite cover gives one neighbourhood of \(t\) on which their values agree at every orbital coordinate. Their integrals are therefore constant there. To pass from the torus to the regular set, use the local conjugation coordinates of Theorem 6.7. Its derivative argument applies also to a product of fields: after separable splitting the centralizer is the diagonal algebra and \(1-\operatorname{Ad}(t)\) is invertible on the off-diagonal quotient. The same inverse-function argument gives the required local charts. This proves local constancy, with the fixed torus measure on each chart.

Finally, in the elliptic case there is one simple block. Normalize \(y\) by a single scalar, rather than by \(E^\times\), and allow \(x\) to vary in the compact elliptic set \(B\). Every limiting equation \(x_0y_0=y_0c_0\) has nonzero \(y_0\); the one-block argument makes it invertible. The normalized matrices again have compact closure in \(G\). Their central classes contain (6.39), which is closed. This proves the uniform assertion. \(\square\)

**Proposition 6.19 — compact coefficients force zero proper Jacquet modules.** Let \(\pi\) be irreducible admissible unitary, with a nonzero smooth coefficient compact modulo \(Z\). Every smooth matrix coefficient then has compact support modulo \(Z\). For every proper parabolic \(P=MN\), its smooth representation \(V\) has \(V_N=0\). Consequently, for every smooth coefficient \(c\) and every \(a_0\in G\),
\[
                 \int_N c(a_0n)\,dn=0.
\tag{6.40}
\]
The integral is absolutely convergent. Here \(V_N\) denotes algebraic coinvariants; a normalized Jacquet-module twist does not change their vanishing.

**Proof: one compact coefficient supplies every smooth pair.** The smooth vectors of an irreducible admissible unitary representation are algebraically irreducible. A nonzero invariant smooth subspace is dense in the Hilbert space. Its average over any compact open subgroup is dense in the finite-dimensional fixed space and is contained in the subspace; hence it equals that entire fixed space. The union of those spaces is \(V\). Thus each of the two nonzero smooth vectors of the given coefficient generates \(V\) by finite linear combinations of translates. Every smooth coefficient is a finite sum of left and right translates of the given one, so has compact support modulo \(Z\). Boundedness and compact support also give square-integrability; Theorem 6.15 supplies its formal degree.

**Proof: the positive projection identity.** After conjugating \(P\), use an upper block parabolic, with opposite unipotent group \(\overline N\). For \(m\ge1\), let \(K_m=1+M_r(\mathfrak p_{D_0}^m)\), and put \(K_+=K_m\cap N\), \(K_-=K_m\cap\overline N\), \(K_M=K_m\cap M\). Block Gaussian elimination gives
\[
 K_m=K_+K_MK_-,\qquad
 a=\operatorname{diag}(\varpi_F^{b_1}I_{r_1},\ldots,
                         \varpi_F^{b_s}I_{r_s}),
 \quad b_1>\cdots>b_s.
\tag{6.41}
\]
The factorization is unique. At each elimination step the pivot is an identity matrix plus entries in \(\mathfrak p_{D_0}^m\), hence invertible by the geometric series; its Schur complement has the same property. This proves the assertion over the division ring. Reducing these unique coordinates modulo deeper radical powers shows that the product of normalized Haar probabilities on the three factors is Haar probability on \(K_m\): each finite congruence quotient has exactly the corresponding product coordinates.

Write \(E_+,E_M,E_-\) for their averaging operators and \(P_m\) for projection onto \(V^{K_m}\). Thus \(P_m=E_+E_ME_-\). Conjugation by \(a\) contracts \(K_+\), and conjugation by \(a^{-1}\) contracts \(K_-\); \(a\) commutes with \(K_M\). For \(T_a=P_m\pi(a)P_m\), these inclusions give
\[
 T_aT_{a^k}
 =P_m\pi(a)E_+E_ME_-\pi(a^k)P_m
 =P_m\pi(a^{k+1})P_m,
 \qquad
 T_a^k=P_m\pi(a^k)P_m.
\tag{6.42}
\]
For the middle equality, move \(E_+\) to the left of \(\pi(a)\), where its contracted subgroup is absorbed by \(P_m\); move \(E_-\) to the right of \(\pi(a^k)\), where its contracted subgroup is absorbed by \(P_m\); move \(E_M\) across \(\pi(a^k)\) and absorb it too. Every average has total mass one. Thus (6.42) uses probability projections, with no double-coset index left over.

**Proof: nilpotence and coinvariants.** The powers \(a^k\) escape every compact subset modulo \(Z\): ratios of two different block scales tend to zero or infinity, whereas an invertible projective limit would keep their relative scales bounded. A finite basis of \(V^{K_m}\) has compactly supported matrix coefficients. Thus every entry of \(P_m\pi(a^k)P_m\) is zero for all sufficiently large \(k\). Equation (6.42) makes \(T_a\) nilpotent on this fixed space.

Let \(j:V\to V_N\) be the coinvariant quotient, with the unnormalized \(M\)-action. For \(v\in V^{K_m}\), \(E_-\pi(a)v=\pi(a)v\), since \(a^{-1}K_-a\subset K_-\); the same holds for \(E_M\). The quotient kills the remaining \(N\)-average. Hence
\[
 j(T_av)=a\cdot j(v),\qquad
 j(T_a^kv)=a^k\cdot j(v).
\tag{6.43}
\]
The action of \(a\) on coinvariants is invertible. Nilpotence therefore gives \(j(v)=0\). The groups \(K_m\) form a neighbourhood basis, so every smooth vector has zero image. This proves \(V_N=0\). If normalized Jacquet notation is used, the first right side of (6.43) is \(\delta_P(a)^{1/2}\pi_N(a)j(v)\); the conclusion is unchanged.

Finally a coefficient restricted to \(a_0N\) has compact support. Its absolute reduced norm is fixed, so the compact-annulus argument in Lemma 6.18 applies, and \(N\) is a closed subgroup with trivial intersection with \(Z\). Write its input vector, using \(V_N=0\), as a finite sum \(\sum_l(\pi(n_l)w_l-w_l)\). Integrating the corresponding coefficients gives zero by right translation on \(N\). Haar measure on this upper unipotent group is two-sided: in ordered block-entry coordinates both translations are triangular with diagonal one. This proves absolute convergence and (6.40). \(\square\)

**Theorem 6.20 — the nonelliptic orbital integrals vanish.** For every smooth coefficient \(c\) in Proposition 6.19,
\[
                         O_t^G(c)=0
        \qquad(t\text{ regular semisimple and nonelliptic}).
\tag{6.44}
\]
This is a vanishing statement for orbital integrals of the coefficient, not a pointwise vanishing statement for its representation character on nonelliptic classes.

**Proof.** The field-factor decomposition has at least two blocks. Conjugate \(t\) into the corresponding proper Levi \(M\), and let \(P=MN\). Put \(K_0=\mathrm{GL}_r(\mathcal O_{D_0})\). Then \(G=PK_0\). Indeed the intersection of a division subspace with the standard lattice is saturated; a primitive vector extends to an integral basis by a unit-coordinate elimination. Inducting on the flag gives an adapted lattice basis, so \(K_0\) is transitive on the flag space. Taking inverses gives the asserted decomposition.

For clarity the needed quotient integration can be normalized exactly. Use Haar probability on \(K_0\), and choose \(dm\,dn\) on \(MN\), in this order, with \(\operatorname{vol}(M\cap K_0)\operatorname{vol}(N\cap K_0)=\operatorname{vol}_G(K_0)\). This product is left Haar on \(P\): left multiplication by \(M\) translates the first coordinate, and left multiplication by \(N\) translates the second coordinate at each fixed \(m\). The equality \(G/K_0=P/(P\cap K_0)\) proves the integration formula by summing right compact-open cosets, then averaging a general integrand on \(K_0\). Dividing the \(M\)-integral by the fixed Haar measure on \(T\subset M\) gives integration over \(T\backslash G\) in coordinates \((Tm,n,k)\).

Write \(t_m=m^{-1}tm\). The change of variables
\[
 \Phi_{t_m}:N\longrightarrow N,\qquad
 n\longmapsto t_m^{-1}n^{-1}t_m n
\tag{6.45}
\]
is a polynomial bijection with constant absolute Jacobian
\(J_N(t_m)=|\det_F(1-\operatorname{Ad}(t_m)^{-1})_{\mathfrak n}|_F>0\).
In increasing block height, its new \((i,j)\)-entry has leading term
\(X_{ij}-t_i^{-1}X_{ij}t_j\), with other terms depending only on smaller heights. This linear map is invertible: after separable splitting its eigenvalues are \(1-\alpha_j/\alpha_i\), and the two blocks have disjoint reduced-polynomial roots. Solving successively gives a polynomial inverse and the displayed triangular Jacobian. Conjugation by \(m\) preserves \(\mathfrak n\), so \(J_N(t_m)=J_N(t)\).

Since \(n^{-1}t_m n=t_m\Phi_{t_m}(n)\), quotient integration gives
\[
 O_t^G(c)=\frac1{J_N(t)}
   \int_{T\backslash M}\int_{K_0}\int_N
      c(k^{-1}m^{-1}tm\,n k)\,dn\,dk\,d\dot m.
\tag{6.46}
\]
Lemma 6.18 proves absolute convergence before this substitution; the bijective change of variables proves it after substitution too. Fubini is therefore valid. For fixed \(m,k\), the inner integral is the constant term at \(t_m\) of the smooth coefficient \(h\mapsto c(k^{-1}hk)\). It is zero by (6.40). This proves (6.44), with the same argument in every residue and field characteristic. \(\square\)

For a concrete three-block calculation, take \(F=\mathbb Q_5\), \(t=\operatorname{diag}(1,2,3)\), and write \(n(x,y,z)\) for the upper unipotent matrix with entries \(n_{12}=x\), \(n_{23}=y\), \(n_{13}=z\). Direct multiplication gives
\[
       \Phi_t(x,y,z)=(-x,-y/2,-2z+xy).
\]
The inverse sends \((X,Y,Z)\) to \((-X,-2Y,XY-Z/2)\). Its triangular derivative has determinant \(-1\), so its absolute Haar Jacobian is one. The quadratic term is needed; successive block-height solving handles it directly.

**Theorem 6.21 — the actual elliptic character formula.** Let \(\pi\) satisfy Proposition 6.19, and choose a nonzero smooth vector \(u\). On the elliptic regular set put \(c_u(g)=\langle\pi(g)u,u\rangle\). Then
\[
       \Theta_\pi(g)=\frac{d_\pi}{\|u\|^2}\,O_g(c_u)
\tag{6.47}
\]
is locally constant, independent of \(u\), and represents the restriction of its actual character distribution to this set. In particular every smooth inverse-central-character test supported compactly there modulo \(Z\) satisfies
\[
                \operatorname{tr}\pi(f)
                    =\int_{G/Z}f(g)\Theta_\pi(g)\,d\bar g.
\tag{6.48}
\]

**Proof.** Local constancy of the proposed function follows from Lemma 6.18. Apply (6.31) to \(f\). To justify interchanging its two integrals, choose compact representatives for the quotient support of \(f\), all elliptic regular. The absolute reduced norms on this compact set stay in a compact annulus. Compact support modulo \(Z\) of \(c_u\), and the reduced-norm calculation in Lemma 6.18, put every conjugate meeting that coefficient support in one actual compact target set. The uniform assertion (6.39) consequently puts all the contributing central conjugator classes in one compact subset of \(G/Z\). The absolute integrand is bounded on the resulting compact product. It is integrable, so Fubini applies.

Invert the conjugation variable, using unimodularity, in that ordered formula. The inner integral is
\(\int_{G/Z}c_u(x^{-1}gx)d\bar x\).
The quotient in stages through \(T_g/Z\) makes it
\(\operatorname{vol}(T_g/Z)O_g(c_u)=O_g(c_u)\), with exactly the torus normalization fixed above. Formula (6.31) now proves (6.48) and (6.47).

Two choices of \(u\) give locally constant centrally covariant functions inducing the same distribution on this open set. They coincide: if their difference were nonzero at one point, choose a sufficiently small compact-open central quotient neighbourhood and multiply its indicator by the conjugate of that difference. This is an allowed inverse-central-character test, and its integral against the difference is strictly positive, a contradiction. Thus the formula is independent of the chosen smooth vector and represents the actual elliptic character. \(\square\)

For comparison, Casselman's Chapter II, §§7–8, discusses compact matrix coefficients, and Chapter III, §§3–5, discusses Jacquet coinvariants and positive Hecke operators. The proofs here give the division-matrix Gaussian factorization, its probability normalization, the nilpotence argument, proper orbital coordinates and the elliptic character integral. For a discrete series without compactly supported coefficients, the compact-conjugator bound in Theorem 6.21 is no longer supplied by this hypothesis. Section 6.15 proves absolute unipotent integration and vanishing constant terms, and reduces nonelliptic orbital convergence to elliptic estimates in the primary blocks. The remaining elliptic convergence estimate is still needed for this coefficient formula.

### 6.7. Jacquet modules and the full square-integrability criterion

Let \(G=\mathrm{GL}_r(D_0)\), \(d=\deg D_0\), and \(Z=F^\times\), over either kind of nonarchimedean local field. Put \(K_0=\mathrm{GL}_r(\mathcal O_{D_0})\) and \(K_m=1+M_r(\mathfrak p_{D_0}^m)\), \(m\ge1\). These principal groups are normal in \(K_0\) and form a neighbourhood basis. A compact-group average on a smooth representation is a finite linear combination on each vector. Thus the projection identities of Section 6.6 apply to smooth admissible representations without a unitary inner product as well.

**Lemma 6.22 — the finite fixed space computes the Jacquet fixed space.** Let \(V\) be smooth admissible, \(P=MN\) a standard parabolic, and \(a\) a strictly contracting central element of \(M\) as in (6.41). Write \(P_m\) for averaging on \(K_m\), \(T_a=P_m\pi(a)P_m\) on \(V^{K_m}\), and \(j:V\to V_N\) for unnormalized coinvariants. The stable kernel of \(T_a\) is \(V^{K_m}\cap V(N)\). For all sufficiently large \(L\), its stable image \(\operatorname{im}T_a^L\) maps isomorphically onto \((V_N)^{K_m\cap M}\). In particular the Jacquet module is admissible.

**Proof: the kernel.** Put \(K_+=K_m\cap N\). The same probability factorization as in (6.42), followed by moving the upper average across \(a^k\), gives, for \(v\in V^{K_m}\),
\[
 \begin{gathered}
 T_a^kv=\pi(a^k)E_{U_k}v,\\
 U_k=a^{-k}K_+a^k.
 \end{gathered}
\tag{6.49}
\]
The groups \(U_k\) are nested compact open subgroups of \(N\) with union \(N\): each upper block entry is expanded by a strictly positive power of the uniformizer. A vector belongs to \(V(N)\) if and only if \(E_{U_k}v=0\) for some \(k\). For the forward direction, express it as a finite sum \(\sum_i(\pi(n_i)w_i-w_i)\), put all \(n_i\) in one \(U_k\), and use right invariance of Haar probability there. Conversely, \(v-E_{U_k}v\) is a finite linear combination of differences of translates of \(v\). Thus
\[
 \bigcup_{k\ge1}\ker T_a^k
                 =V^{K_m}\cap V(N).
\tag{6.50}
\]
Finite dimension makes the kernels and images stationary. For a sufficiently large \(L\), the kernel of \(T_a^L\) and its image are complementary: an element of their intersection is \(T_a^Lw\) with \(T_a^{2L}w=0\), and stationarity makes it zero. Their dimensions add to the whole dimension. The operator is invertible on its stable image. It follows that \(j\) identifies that image with \(j(V^{K_m})\).

**Proof: surjectivity.** The image \(J_m=j(V^{K_m})\) lies in \((V_N)^{K_m\cap M}\). The relation \(j(T_av)=a\cdot j(v)\) from (6.43) makes \(J_m\) stable under \(a\). This action is injective, since it is induced by an invertible group element on coinvariants. On the finite-dimensional \(J_m\) it is therefore bijective.

Take \(u\in(V_N)^{K_m\cap M}\), lift it to \(V\), and average the lift over \(K_m\cap M\). Call the result \(v\). It is fixed by this compact group and by some sufficiently small \(K_l\): normality of \(K_l\) in \(K_0\) preserves that property under the preceding average. For large \(k\), \(a^{-k}(K_m\cap\overline N)a^k\subset K_l\). Consequently the lower and middle factors of \(P_m\) fix \(\pi(a^k)v\), and its upper factor disappears in coinvariants. Hence \(j(P_m\pi(a^k)v)=a^k u\), which belongs to \(J_m\). Invertibility of \(a\) on \(J_m\) now gives \(u\in J_m\). We have proved
\[
 \operatorname{im}T_a^L\ \xrightarrow[\ j\ ]{\ \sim\ }
       (V_N)^{K_m\cap M}.
\tag{6.51}
\]
These compact subgroups form a neighbourhood basis in \(M\), so every compact-open fixed space of \(V_N\) is finite-dimensional. This proves admissibility. The same argument after conjugation covers every parabolic. \(\square\)

For the remaining assertions let \(\pi\) be irreducible admissible unitary with smooth unitary central character \(\omega\), and let \(V\) be its smooth vectors. Norms and absolute integrals are on \(G/Z\). Let \(q_F\) be the residue cardinality. For \(1\le j<r\), define
\[
 \begin{gathered}
 a_j=\operatorname{diag}(\varpi_F I_j,I_{r-j}),\qquad
 t_{\ell}=\prod_{j=1}^{r-1}a_j^{\ell_j},\quad
                         \ell\in\mathbb Z_{\ge0}^{r-1},\\
 P_j=M_jN_j,\qquad
 M_j=\mathrm{GL}_j(D_0)\times\mathrm{GL}_{r-j}(D_0).
 \end{gathered}
\tag{6.52}
\]
Here \(P_j\) is upper block triangular. Its modulus at this element is
\[
 \delta_j=\delta_{P_j}(a_j)
          =q_F^{-d^2j(r-j)}.
\tag{6.53}
\]
Indeed conjugation scales each of its \(j(r-j)\) upper division entries by \(\varpi_F\), and each entry has \(F\)-dimension \(d^2\).

**Lemma 6.23 — Cartan coordinates, positive products and their volumes.** For fixed \(m\), put \(T_c=P_m\pi(c)P_m\). If \(c,c'\) are diagonal field scalars with nonincreasing entry valuations, then
\[
 T_cT_{c'}=T_{cc'},\qquad
 T_{t_{\ell}}=\prod_{j=1}^{r-1}T_{a_j}^{\ell_j}.
\tag{6.54}
\]
If \(\overline K_m\) is the image in \(G/Z\), the sets \(\overline K_m t_{\ell}\overline K_m\) for distinct \(\ell\) are disjoint and
\[
 \operatorname{vol}(\overline K_m t_{\ell}\overline K_m)
       =\operatorname{vol}(\overline K_m)
                           \prod_j\delta_j^{-\ell_j}.
\tag{6.55}
\]
There is a finite set \(B\) of diagonal division matrices such that \(G=\bigcup_{\ell,b\in B} ZK_0t_{\ell}bK_0\). More precisely, for any fixed \(m\) one can choose a finite set \(D\subset K_0\) with
\[
 G=\bigcup_{\ell,\ b\in B,\ k_1,k_2\in D}
                 Zk_1bK_m t_{\ell}K_m k_2.
\tag{6.56}
\]
The number of translates for each \(\ell\) is bounded independently of \(\ell\).

**Proof: the matrix decomposition.** Choose a division uniformizer \(\Pi\). Integral row and column operations diagonalize an invertible division matrix. Choose an entry of least valuation as a pivot; its ratios with all entries in its row and column are integral, so those operations eliminate that row and column. Repeat on the remaining invertible minor, and sort the resulting powers of \(\Pi\) by permutation matrices. Unit factors are absorbed in \(K_0\). Thus every matrix belongs to \(K_0\operatorname{diag}(\Pi^{h_1},\ldots,\Pi^{h_r})K_0\), with \(h_1\ge\cdots\ge h_r\).

These sorted integers are unique. If \(L=\mathcal O_{D_0}^r\), the lengths of \(L/(L\cap(gL)\Pi^s)\), for integral \(s\), are invariant under both integral basis changes. On the displayed diagonal they are \(\sum_i\max(h_i+s,0)\); successive differences recover the multiset of integers. Multiplying by a central scalar shifts every \(h_i\) by the same multiple of \(d\).

Write \(h_i=dq_i+\epsilon_i\), \(0\le\epsilon_i<d\). Since \(\Pi^d/\varpi_F\) is a division unit commuting with \(\Pi\), the diagonal units can again be absorbed in \(K_0\). The remaining diagonal is \(\operatorname{diag}(\varpi_F^{q_i})b\), where \(b=\operatorname{diag}(\Pi^{\epsilon_i})\) belongs to a finite set \(B\). The \(q_i\) are nonincreasing. Remove the common central power \(q_r\); the result is \(t_{\ell}\) with \(\ell_j=q_j-q_{j+1}\). This proves the asserted covering. It also proves the disjointness in (6.55), because these scalar diagonals have division valuations \(dq_i\) with smallest value zero, so no nonzero common central shift identifies two of them.

**Proof: probabilities and volumes.** Use the factorization of \(K_m\) for the minimal upper triangular parabolic. Every positive scalar diagonal contracts the upper factor, its inverse contracts the lower factor, and it commutes with the diagonal factor. The probability-average calculation of (6.42) applies to any pair \(c,c'\) in this cone, proving (6.54), including commutativity.

Uniqueness of the same Gaussian coordinates identifies \(K_m\cap tK_mt^{-1}\) with the product of \(tK_+t^{-1}\), the unchanged diagonal factor, and \(K_-\). The finite index is therefore the index of the contracted upper group. Its coordinate Haar Jacobian is the minimal-parabolic modulus \(\delta_B(t)\), so that index is \(\delta_B(t)^{-1}\). At \(t=t_{\ell}\), this is \(\prod_j\delta_j^{-\ell_j}\).

The same index computes the central quotient double coset. In fact, if \(k=ztk't^{-1}\), with \(k,k'\in K_m\), comparison of a diagonal entry gives \(z\in1+\mathfrak p_{D_0}^m\). Thus \(z\in Z\cap K_m\) and can be absorbed into \(k'\); passing to the central quotient has not enlarged the intersection. Counting the right compact-open cosets proves (6.55).

Finally choose a principal \(H\subset K_0\) contained in \(K_m\cap bK_mb^{-1}\) for every \(b\in B\), and choose representatives \(D\) of \(K_0/H\). If \(k_i\in D\) and \(h_i\in H\), then
\(k_1h_1t_{\ell}bh_2k_2=k_1b(b^{-1}h_1b)t_{\ell}h_2k_2\), since \(b\) commutes with \(t_{\ell}\). This belongs to the indicated translate in (6.56). Every translate is contained in \(G\), and the preceding Cartan covering proves equality. All indexing sets except \(\ell\) are finite. \(\square\)

**Theorem 6.24 — the complete Jacquet compactness criterion.** For \(\pi\) as above, the following are equivalent:
\[
 \begin{gathered}
 \text{every smooth matrix coefficient is compact modulo }Z;\\
 V_{N_j}=0\quad(1\le j<r);\\
 V_N=0\quad\text{for every proper parabolic }MN.
 \end{gathered}
\tag{6.57}
\]
One nonzero compact smooth coefficient already implies these conditions.

**Proof.** Proposition 6.19 proves the first-to-third implication and the assertion about one coefficient; the third implies the second. Suppose the second holds. Lemma 6.22 makes every \(T_{a_j}\) nilpotent on every finite \(V^{K_m}\). By (6.54), \(T_{t_{\ell}}=0\) as soon as any one \(\ell_j\) exceeds its nilpotence bound at this level.

For given smooth vectors \(u,v\), choose \(m_0\) fixing them, and then choose \(m\ge m_0\) large enough that \(bK_mb^{-1}\subset K_{m_0}\) for every \(b\in B\). For every \(k_1,k_2\in K_0\), both \(\pi(k_2)u\) and \(\pi(b^{-1}k_1^{-1})v\) are fixed by \(K_m\); here normality of the principal groups in \(K_0\) is used. On a translate in (6.56) their coefficient is consequently an entry of \(T_{t_{\ell}}\). It vanishes outside a finite box of \(\ell\)'s. The corresponding finite union of Cartan sets is compact modulo \(Z\). This proves compact support for every smooth pair. For \(r=1\) there are no proper parabolics and the Cartan covering is already compact modulo the centre, so the same conclusion holds. \(\square\)

**Theorem 6.25 — the full \(L^p\) criterion.** Fix \(1\le p<\infty\). All smooth matrix coefficients of \(\pi\) belong to \(L^p(G/Z)\) if and only if, for every \(m\ge1\) and every \(1\le j<r\), the finite-dimensional operator
\[
       S_{j,p}=\delta_j^{-1/p}T_{a_j}
                       \quad\text{on }V^{K_m}
\tag{6.58}
\]
has spectral radius strictly less than one. Equivalently, every eigenvalue \(\lambda\) of the normalized Jacquet action of \(a_j\) on \((V_{N_j})^{K_m\cap M_j}\) satisfies
\[
                    |\lambda|\,\delta_j^{1/2-1/p}<1.
\tag{6.59}
\]
An empty fixed space imposes no condition. This includes every matrix rank and division degree, in either field characteristic.

**Proof: necessity, including the strict boundary.** Choose an orthonormal basis of \(V^{K_m}\). Its coefficients are constant in absolute value on each central double coset in (6.55). Restricting their \(p\)-th-power integrals to these disjoint double cosets shows that, for every matrix entry,
\(\sum_{\ell}\prod_j\delta_j^{-\ell_j}|(T_{t_{\ell}})_{ab}|^p<\infty\).
Restrict further to one coordinate ray. Every entry of \(S_{j,p}^k\) is then \(p\)-summable in \(k\). If it had an eigenvalue \(\alpha\) with \(|\alpha|\ge1\), its operator norm would be at least \(|\alpha|^k\) on that eigenvector. In dimension \(h\), this norm is at most \(h\) times the largest matrix entry. The sum of the \(p\)-th powers of its entries could not be summable. Thus the spectral radius is strictly below one, including exclusion of the equality case.

**Proof: sufficiency on the entire group.** A finite matrix of spectral radius less than one has a bound \(\|S^k\|\le C\rho^k\) for some \(\rho<1\). To see the bound, on each Jordan block expand \((\alpha I+N)^k\) as the finite binomial sum in \(N\). A fixed polynomial in \(k\) times \(|\alpha|^k\) is bounded by \(C\rho^k\) after choosing \(|\alpha|<\rho<1\); a zero-eigenvalue block is eventually zero. The required finite Jordan decomposition follows from the elementary polynomial-module argument used in Lemma 6.9. Applying these bounds to all the commuting operators in (6.58) gives
\[
 \sum_{\ell\in\mathbb Z_{\ge0}^{r-1}}
       \left(\prod_j\delta_j^{-\ell_j}\right)
                         \|T_{t_{\ell}}\|^p
  =\sum_{\ell}\left\|\prod_jS_{j,p}^{\ell_j}\right\|^p
  <\infty.
\tag{6.60}
\]
Indeed submultiplicativity bounds it by a constant times a product of convergent geometric series.

For any smooth \(u,v\), choose \(m\) as in the proof of Theorem 6.24. On each translate in (6.56), the coefficient is constant in absolute value on the central \(K_m\)-double coset, and is bounded by \(\|u\|\|v\|\|T_{t_{\ell}}\|\). Left and right translation preserve quotient Haar measure, by unimodularity. Equations (6.55), (6.56) and (6.60), with only finitely many translates per \(\ell\), prove the \(L^p\) bound on all of \(G/Z\). Overlap between those translated sets only increases this upper bound. This proves sufficiency for arbitrary smooth vectors.

Finally Lemma 6.22 identifies the stable image of \(T_{a_j}\) with the Jacquet fixed space. Its stable kernel is nilpotent, so contributes only the eigenvalue zero. On the quotient, \(T_{a_j}\) acts as unnormalized \(a_j\), which is \(\delta_j^{1/2}\) times normalized Jacquet action. This gives exactly (6.59). \(\square\)

**Corollary 6.26 — square integrability and the \(L^{2+\epsilon}\) boundary.** In normalized Jacquet notation, square integrability modulo the centre and membership of all smooth coefficients in every \(L^{2+\epsilon}\), \(\epsilon>0\), are respectively
\[
 \begin{gathered}
 \text{Square integrability: }|\lambda|<1;\\
 \text{Every }L^{2+\epsilon},\ \epsilon>0:
                       |\lambda|\le1;\\
 \text{for every }m\ge1,\quad1\le j<r.
 \end{gathered}
\tag{6.61}
\]
For the first line, all Hilbert coefficients are square-integrable as well. One nonzero smooth coefficient satisfying an \(L^p\) condition with \(p\ge1\) already implies that condition for all smooth coefficients.

**Proof.** The first line is (6.59) at \(p=2\), and Theorem 6.15 passes from one nonzero square-integrable coefficient to all Hilbert coefficients. If \(|\lambda|\le1\), then for every \(p>2\) the factor \(\delta_j^{1/2-1/p}\) is strictly less than one, giving the second line by Theorem 6.25. Conversely, if (6.59) holds for every \(p>2\), let \(p\) decrease to two for each fixed eigenvalue; it gives \(|\lambda|\le1\). The smooth vectors are algebraically irreducible by Proposition 6.19. Every smooth pair is therefore obtained by finite linear combinations of left and right translates of any fixed nonzero smooth coefficient. These translations preserve \(L^p\), and \(L^p\) is a vector space for \(p\ge1\). This proves the last assertion. \(\square\)

For an explicit boundary calculation, take \(G=\mathrm{GL}_2(F)\) and the Steinberg unit edge vector of Proposition 2.12. Its coefficient has absolute value \(q^{-l}\) on the sphere with \(2q^l\) right edge-stabilizer cosets, each of volume \(2/(q+1)\). Thus, for \(p>1\),
\[
 \int_{G/Z}|\langle\mathrm{St}(g)v,v\rangle|^p\,d\bar g
 =\frac2{q+1}\left(1+2\sum_{l\ge1}q^{(1-p)l}\right)
 =\frac2{q+1}\left(1+
                \frac{2q^{1-p}}{1-q^{1-p}}\right).
\tag{6.62}
\]
At \(p=1\) this sum diverges; at \(p=2\) it is \(2/(q-1)\), as in (2.51). The algebraic cyclicity just proved makes every smooth Steinberg coefficient belong to every \(L^p\), \(p>1\). This example exhibits both an integrability boundary and square integrability with noncompact coefficient support.

Casselman's freely available 1995 draft, Theorem 4.4.6, gives the general reductive square-integrability criterion, and §§5.2–5.3 give the compact-coefficient criterion. The arguments above prove the full division-matrix version through Jacquet fixed spaces, explicit Cartan coordinates, exact quotient double-coset volumes and finite-dimensional power bounds. No character orthogonality or transfer-existence assertion is inferred from this coefficient criterion.

### 6.8. The canonical Jacquet pairing and full cone asymptotics

Let \(V\) be any smooth admissible complex representation of \(G=\mathrm{GL}_r(D_0)\), in either field characteristic. Write \(V^\vee\) for its smooth contragredient and use the bilinear evaluation pairing \(\langle v,\widetilde v\rangle=\widetilde v(v)\). Fix a standard parabolic \(P=MN\), with opposite \(\overline P=M\overline N\). The maps \(j_P:V\to V_N\) and \(j_{\overline P}:V^\vee\to(V^\vee)_{\overline N}\) first mean the underlying coinvariant quotients. We explicitly distinguish the unnormalized \(M\)-action from the normalized action \(\pi_P(m)=\delta_P(m)^{-1/2}\pi_N^{\mathrm{un}}(m)\). The modulus of the opposite parabolic is \(\delta_{\overline P}=\delta_P^{-1}\).

**Lemma 6.27 — dual fixed spaces and common stable ranges.** For each principal \(K_m\), evaluation identifies
\[
                   (V^\vee)^{K_m}\simeq(V^{K_m})^*.
\tag{6.63}
\]
In particular the contragredient is admissible. Choose a strictly contracting central scalar-block element \(a\) of \(M\), and set \(T_a=P_m\pi(a)P_m\) on \(U_m=V^{K_m}\). Its transpose is the positive operator for the opposite parabolic:
\[
          T_a^t=\widetilde P_m\pi^\vee(a^{-1})\widetilde P_m.
\tag{6.64}
\]
Their stable ranges \(W_m\) and \(\widetilde W_m\) pair perfectly and identify with the two Jacquet fixed spaces by Lemma 6.22. These ranges are independent of the chosen strictly contracting central element.

**Proof.** A \(K_m\)-invariant functional is exactly a functional factoring through the average \(P_m\); conversely any functional on \(U_m\) composed with \(P_m\) is smooth and \(K_m\)-invariant. This proves (6.63). The compact subgroups are cofinal, so admissibility follows. Compact Haar probability is invariant under inversion, which makes the transpose of \(P_m\) equal to \(\widetilde P_m\). The definition of contragredient gives (6.64).

Let \(L_m=U_m\cap V(N)\). By Lemma 6.22 it is the stable kernel of \(T_a\), and \(U_m=L_m\oplus W_m\). The stable kernel of the transpose annihilates \(W_m\); its stable range is the annihilator of \(L_m\). Therefore evaluation restricts to a perfect pairing on \(W_m\times\widetilde W_m\), and Lemma 6.22 for \(\overline P\) gives
\[
 \begin{gathered}
 j_P:W_m\xrightarrow{\sim}(V_N)^{K_m\cap M},\\
 j_{\overline P}:\widetilde W_m
       \xrightarrow{\sim}((V^\vee)_{\overline N})^{K_m\cap M}.
 \end{gathered}
\tag{6.65}
\]
For another strictly contracting central \(b\), the probability calculation in (6.42) gives \(T_aT_b=T_{ab}=T_bT_a\). Thus \(T_b\) preserves \(L_m\) and \(W_m\). Its stable kernel is the same \(L_m\), so it is nilpotent there and injective, hence invertible, on \(W_m\). Its stable range is consequently \(W_m\). Applying this to the transpose proves the other assertion. \(\square\)

The inverses in (6.65) are denoted \(s_m\) and \(\widetilde s_m\). A lift may depend on \(m\). We next prove that its pairing gives a value independent of \(m\).

**Lemma 6.28 — exact central-cone coefficients and independence of level.** Put
\[
 B_{P,m}(u,\widetilde u)
           =\langle s_mu,\widetilde s_m\widetilde u\rangle.
\tag{6.66}
\]
These pairings agree on the common domains at different principal levels and define a bilinear form \(B_P\) on \(V_N\times(V^\vee)_{\overline N}\). Let the Levi blocks have sizes \(r_1,\ldots,r_s\), put \(h_m=\max(1,\dim U_m)\), and take
\(c=\operatorname{diag}(c_1I_{r_1},\ldots,c_sI_{r_s})\), \(c_i\in F^\times\).
For \(v\in V^{K_m}\), \(\widetilde v\in(V^\vee)^{K_m}\), one has
\[
 \begin{gathered}
 v_F(c_i/c_{i+1})\ge h_m\quad(1\le i<s)\quad\Longrightarrow\\
 \langle\pi(c)v,\widetilde v\rangle
   =B_P(c\cdot j_Pv,j_{\overline P}\widetilde v)\\
   =\delta_P(c)^{1/2}
          B_P(\pi_P(c)j_Pv,j_{\overline P}\widetilde v).
 \end{gathered}
\tag{6.67}
\]
The first action on the right is unnormalized. The threshold is uniform for the entire pair of finite fixed spaces.

**Proof: the uniform range.** Choose \(a\) with consecutive block valuations \(s-1,s-2,\ldots,0\). The nilpotent part of its finite operator is killed by the \(h_m\)-th power. If the displayed inequalities hold, \(b=a^{-h_m}c\) has nonincreasing block valuations. The probability identity gives \(T_c=T_a^{h_m}T_b\). The operators commute. On the common stable range, \(T_b\) is invertible: its Jacquet action is the invertible action of \(b\), and (6.65) identifies that action with its restriction. It follows that \(T_c\) kills \(L_m\), has image \(W_m\), and its action there is the canonical lift of unnormalized \(c\).

Pair with \(\widetilde v\). The stable-kernel component of \(v\) has been killed, and the stable-kernel component of \(\widetilde v\) annihilates \(W_m\). Removing these two components gives (6.67) with \(B_{P,m}\), first in unnormalized form and then with the displayed modulus. For \(P=G\) this is just ordinary evaluation, with trivial coinvariants and no inequalities.

**Proof: comparing levels.** If \(l\ge m\), the canonical lifts at level \(m\) are also \(K_l\)-fixed. Choose bases of the two Jacquet fixed spaces at level \(m\) and their level-\(m\) lifts. Apply the formula just proved at both levels to these finitely many pairs, with \(c=a^k\) and one sufficiently large \(k\). The two pairings agree on all \((a^ku,\widetilde u)\) from those bases. Since \(a^k\) acts invertibly on the first Jacquet fixed space, these vectors span that space as well. The pairings agree on their entire common finite domain. The union of these domains is the whole pair of smooth Jacquet modules, so \(B_P\) is well defined. This also proves (6.67) for that form. \(\square\)

**Theorem 6.29 — the canonical pairing and opposite Jacquet duality.** The form \(B_P\) is nondegenerate and \(M\)-invariant for unnormalized actions. It is characterized uniquely by (6.67) for sufficiently contracting central elements and arbitrary smooth lifts. In normalized notation it gives the natural isomorphism
\[
             (\pi_P)^\vee\simeq(\pi^\vee)_{\overline P},
\tag{6.68}
\]
where both Jacquet representations are normalized. The assertions hold for every parabolic, by transport under conjugation.

**Proof: uniqueness and invariance.** Any two forms with the coefficient property agree. Fix one finite pair of Jacquet fixed spaces, choose lifts of bases, and apply their coefficient properties at a common sufficiently large \(a^k\). Invertibility of \(a^k\) on the first finite space proves equality there, exactly as in the level comparison. The union of the finite domains proves uniqueness globally.

For \(m_0\in M\), the form \((u,\widetilde u)\mapsto B_P(m_0u,m_0\widetilde u)\) has the same coefficient property. Indeed apply (6.67) to \(\pi(m_0)v\) and \(\pi^\vee(m_0)\widetilde v\). A central \(c\) commutes with \(m_0\), so evaluation invariance makes the left side equal to \(\langle\pi(c)v,\widetilde v\rangle\). Uniqueness makes this transformed form equal to \(B_P\). This proves \(M\)-invariance without an assumption that \(m_0\) normalizes the chosen principal subgroup. The perfect pairings (6.65) prove nondegeneracy on the full modules.

**Proof: the entire smooth dual.** A vector of the opposite Jacquet module gives a smooth functional on \(V_N\): an open subgroup fixing it also fixes that functional, by invariance. Conversely let a smooth functional be fixed by \(K_m\cap M\). It factors through the compact average onto the finite fixed space. The perfect pairing there represents it by a unique vector of the opposite fixed space. Invariance under the same compact group makes the equality hold on every vector after averaging, proving surjectivity onto the smooth dual. Nondegeneracy gives injectivity.

Normalization multiplies the two unnormalized actions by \(\delta_P^{-1/2}\) and \(\delta_{\overline P}^{-1/2}=\delta_P^{1/2}\). Their factors cancel in the bilinear form, proving the normalized equivariance in (6.68). Conjugating a standard parabolic transports its coefficient property; uniqueness makes the resulting form independent of the conjugating choice. \(\square\)

**Theorem 6.30 — the formula on every positive chamber face.** Retain the vectors and \(h_m\) above. Let \(J\subset\{1,\ldots,r-1\}\) be the block boundaries of \(P\). For any positive scalar diagonal \(t=\operatorname{diag}(t_1,\ldots,t_r)\), suppose
\[
 \begin{gathered}
 v_F(t_i/t_{i+1})\ge0\quad\text{for every }i,\\
 v_F(t_j/t_{j+1})\ge h_m\quad(j\in J).
 \end{gathered}
\tag{6.69}
\]
Then the exact coefficient identity is
\[
 \langle\pi(t)v,\widetilde v\rangle
     =\delta_P(t)^{1/2}
          B_P(\pi_P(t)j_Pv,j_{\overline P}\widetilde v).
\tag{6.70}
\]
Inside a Levi block the remaining gaps can be any nonnegative integers. Thus the assertion includes all the boundary directions of the full Cartan chamber.

**Proof.** Let \(a_P=\prod_{j\in J}a_j\), with the fundamental diagonals from (6.52). It is strictly contracting and central for this Levi. By (6.69), \(b=a_P^{-h_m}t\) is still positive in the full scalar chamber. Equation (6.54) gives \(T_t=T_{a_P}^{h_m}T_b\); both factors commute. Hence \(T_t\) takes \(U_m\) into the canonical range \(W_m\) and kills its Jacquet kernel.

The unipotent probability factors of \(P_m\) give a slightly different identity because \(t\) can vary inside the Levi blocks:
\[
 j_P(T_tv)=E_{K_m\cap M}
                         \pi_N^{\mathrm{un}}(t)j_Pv.
\tag{6.71}
\]
To verify it, use \(P_m=E_+E_ME_-\). The lower factor is absorbed across \(\pi(t)\) because \(t^{-1}K_-t\subset K_-\); the quotient removes the upper factor. The middle factor remains as precisely the displayed \(M\)-average. No commutation with this middle factor is asserted.

Pair \(T_tv\) with \(\widetilde v\) and replace its second vector by its canonical opposite lift, since the other component annihilates \(W_m\). Equation (6.71) then represents this pairing by \(B_P\). Its second Jacquet vector is \(K_m\cap M\)-fixed, so \(M\)-invariance removes the remaining average in the first variable. Finally replace unnormalized action by \(\delta_P(t)^{1/2}\pi_P(t)\). This proves (6.70). The case \(J=\varnothing\), \(P=G\), is ordinary evaluation. \(\square\)

**Corollary 6.31 — finite exponential-polynomial expansions with every face included.** Fix a smooth matrix coefficient and the scalar Cartan elements \(t_{\ell}\) of (6.52). There is an integer \(h\ge1\) such that the nonnegative chamber is a finite union of faces specified by
\(\ell_j\ge h\) for \(j\in J\), with the other coordinates fixed in \(\{0,\ldots,h-1\}\). On each face, with its parabolic \(P_J\), the coefficient is exactly of the form
\[
 \delta_{P_J}(t_{\ell})^{1/2}
       \sum_{\alpha} Q_{\alpha}(\ell_J)
                         \prod_{j\in J}\alpha_j^{\ell_j}.
\tag{6.72}
\]
There are finitely many terms; every \(\alpha_j\ne0\); and \(Q_{\alpha}\) is a polynomial. These are finite-level Jacquet exponents for this coefficient. Together with the finite translated Cartan cover of Lemma 6.23, this gives finite families of such expansions covering the whole group modulo the centre.

**Proof.** Choose a principal level fixing both vectors and use \(h=h_m\). For each \(\ell\), take \(J=\{j:\ell_j\ge h\}\); the other coordinates have only finitely many possible values. Write \(t_{\ell}=t_Jt_b\), where \(t_J\) uses the unbounded coordinates and \(t_b\) the bounded ones. Theorem 6.30 applies. The finitely many vectors \(\pi_{P_J}(t_b)j_Pv\), together with the fixed second Jacquet vectors, have a common compact-open stabilizer in \(M_J\). Its fixed spaces are finite-dimensional by Lemma 6.22. The central elements \(a_j\), \(j\in J\), preserve them and act by commuting invertible operators.

Successively decompose into generalized eigenspaces for these operators; commutation preserves each previously obtained decomposition. On a resulting joint block write an operator as \(\alpha_j I+N_j\), where \(N_j\) is nilpotent. Its powers are
\(\alpha_j^{\ell_j}\sum_{\nu=0}^{d_j-1}\binom{\ell_j}{\nu}\alpha_j^{-\nu}N_j^\nu\).
Multiplying these finite sums and pairing the two vectors gives (6.72). Nilpotent parts therefore contribute polynomial factors and have not been discarded. For \(J=\varnothing\) there are only finitely many coefficient values. For the full group use the first Cartan covering in Lemma 6.23. A fixed smooth vector has finite \(K_0\)-orbit: its open stabilizer has finite index in the compact group. The finite division residues send those finitely many vectors to another finite set. Choose one principal subgroup fixing all these transformed pairs and apply the proof to that finite family. \(\square\)

**Example 6.32 — the spherical coefficient with a repeated parameter.** Take \(G=\mathrm{GL}_2(F)\), \(q=q_F\), and normalized \(\pi=I(1,1)\). Lesson 7, Theorems 4.2 and 7.1, proves irreducibility and unitarity. The compact induced model has a one-dimensional \(K_0\)-fixed space, represented by the function \(v\) equal to one on \(K_0\); use Haar probability there, so \(\|v\|=1\). Its central character is trivial. Put \(a=\operatorname{diag}(\varpi_F,1)\), and normalize \(\operatorname{vol}(K_0Z/Z)=1\).

The neighbour double coset has \(q+1\) right \(K_0\)-cosets, represented by
\[
 g_b=\begin{pmatrix}\varpi_F&b\\0&1\end{pmatrix}
       \quad(b\in\mathcal O/\varpi_F),\qquad
 g_{\infty}=\begin{pmatrix}1&0\\0&\varpi_F\end{pmatrix}.
\tag{6.73}
\]
This is the list of index-one lattice neighbours from Section 2.3. Evaluating the normalized induced section at these upper triangular matrices gives \(q^{-1/2}\) at each \(g_b\) and \(q^{1/2}\) at \(g_{\infty}\). Thus the probability neighbour operator acts on the fixed line by \(\eta=2\sqrt q/(q+1)\).

The coefficient \(x_k=\langle\pi(a^k)v,v\rangle\) is radial on the tree. For \(k\ge1\), one neighbour is inward and \(q\) are outward, while all \(q+1\) neighbours of the base vertex have distance one. Consequently
\[
 \begin{gathered}
 x_0=1,\qquad x_1=\frac{2\sqrt q}{q+1},\\
 qx_{k+1}+x_{k-1}=2\sqrt q\,x_k\quad(k\ge1).
 \end{gathered}
\tag{6.74}
\]
Multiplying by \(q^{k/2}\) turns this into zero second differences. The initial values therefore give the exact spherical coefficient
\[
             x_k=q^{-k/2}
                        \left(1+\frac{q-1}{q+1}k\right).
\tag{6.75}
\]
It is positive. The vertex sphere has \((q+1)q^{k-1}\) right compact cosets for \(k\ge1\). Writing \(\beta=(q-1)/(q+1)>0\), its full coefficient integral, for \(1\le p<\infty\), is
\[
 \|x\|_p^p
    =1+\frac{q+1}{q}
             \sum_{k\ge1}q^{(1-p/2)k}(1+\beta k)^p.
\tag{6.76}
\]
It converges exactly for \(p>2\). For \(p=2\) the summands grow quadratically; for \(p<2\) their exponential factor grows. For \(p>2\) the decaying geometric factor dominates the polynomial. Corollary 6.26 then gives every smooth coefficient in every \(L^{2+\epsilon}\), while (6.76) prevents square integrability.

The polynomial term also proves that normalized Jacquet action in this example has a nontrivial generalized eigenspace at eigenvalue one. Apply (6.67) to the fixed vector and its smooth unitary-dual functional. Since \(\delta_B(a^k)^{1/2}=q^{-k/2}\), it gives
\[
 B_B\bigl(\pi_B(a)^k j_Bv,
                  j_{\overline B}\widetilde v\bigr)=1+\beta k
                         \quad\text{for all sufficiently large }k.
\tag{6.77}
\]
Let \(p(X)\) annihilate \(\pi_B(a)\) on the relevant finite Jacquet fixed space. Applying the corresponding shift polynomial to this eventual sequence gives
\(p(1)(1+\beta k)+\beta p'(1)=0\).
Because \(\beta\ne0\), both \(p(1)\) and \(p'(1)\) are zero. Its minimal polynomial therefore has a repeated root at one. Treating all repeated-parameter terms as semisimple would lose this coefficient and its correct boundary behaviour.

Casselman 1995, §§4.1–4.3, especially Proposition 4.2.3, Theorem 4.2.4, Corollary 4.2.5 and Theorem 4.3.3, gives a free source comparison for the canonical pairing and cone formula. The proofs here include level independence, the full smooth opposite dual, the modulus factors, every chamber face and its nilpotent polynomial terms.

### 6.9. Decay, matrix units and the discrete part of Plancherel

Fix a smooth unitary central character \(\omega\). In this section a discrete series means an irreducible admissible unitary representation with central character \(\omega\) and a nonzero square-integrable coefficient modulo \(Z\). Theorems 6.15 and 6.25 characterize precisely this condition. Inner products remain linear in their first variable.

**Lemma 6.33 — an intrinsic length and a translation bound.** Let
\(g\in K_0\operatorname{diag}(\Pi^{h_1},\ldots,\Pi^{h_r})K_0\), with \(h_1\ge\cdots\ge h_r\), as in Lemma 6.23. Define
\[
 \begin{gathered}
 \sigma(g)=h_1-h_r,\\
 D_C(g)=q_F^{-d\sum_{i<j}(h_i-h_j)}.
 \end{gathered}
\tag{6.78}
\]
These functions descend to \(G/Z\), are invariant under inversion, and are locally constant. The sets \(\{\sigma\le R\}\) are compact and open in \(G/Z\). One has
\(\sigma(gh)\le\sigma(g)+\sigma(h)\). For fixed \(a,b\in G\), there are constants \(C\ge1\), \(L\ge0\) such that, for every \(g\),
\[
 \begin{gathered}
 |\sigma(agb)-\sigma(g)|\le L,\\
 C^{-1}D_C(g)\le D_C(agb)\le C D_C(g).
 \end{gathered}
\tag{6.79}
\]

**Proof.** Give \(D_0^r\) its maximum norm, using the multiplicative division norm with \(|\Pi|_{D_0}=q_{D_0}^{-1}\), where \(q_{D_0}=q_F^d\). Integral invertible matrices are isometries. Thus
\(q_{D_0}^{\sigma(g)}=\|g\|\|g^{-1}\|\). Submultiplicativity of operator norms proves the length inequality; applying it also to \(g=a^{-1}(agb)b^{-1}\) proves the first bound in (6.79).

Here is a bound for every elementary divisor, which also controls \(D_C\). Put the singular numbers in decreasing order, so they are \(s_i(g)=q_{D_0}^{-h_{r+1-i}}\). They have the elementary minimax description
\[
 s_i(g)=\inf_{\dim_{D_0} W=r-i+1}\ 
             \sup_{0\ne v\in W}\frac{\|gv\|}{\|v\|}.
\tag{6.80}
\]
Reduce by the two integral isometries to a diagonal matrix with decreasing singular numbers. The span of its last \(r-i+1\) coordinates gives the upper bound \(s_i\). Every subspace of that dimension intersects the span of the first \(i\) coordinates nontrivially; any nonzero vector in the intersection has norm ratio at least \(s_i\). This proves the reverse bound and (6.80).

Choose an integer \(M\) with all four operator norms of \(a,a^{-1},b,b^{-1}\) at most \(q_{D_0}^{M}\). Multiplication on the left changes every ratio in (6.80) by factors between \(q_{D_0}^{-M}\) and \(q_{D_0}^M\). For multiplication on the right, replace \(W\) by \(bW\) and use the same comparison for the denominator. Consequently each sorted \(h_i(agb)\) differs from \(h_i(g)\) by at most \(2M\). Summing the resulting bounds for \(h_i-h_j\) proves the second assertion in (6.79).

A central multiplication shifts every \(h_i\) by the same integer multiple of \(d\); inversion reverses and negates them. This proves the stated invariances. Local constancy follows because each integral double coset is open. If \(\sigma\le R\), remove a common central shift so that \(0\le h_r<d\). There are then only finitely many possible sorted integer tuples, all in \([0,R+d-1]\). Their compact double cosets cover the indicated quotient set. Its complement is a union of the remaining open double cosets, so the set is also open and closed. \(\square\)

**Theorem 6.34 — uniform exponential decay and weighted square integrability.** For each discrete series \(\pi\) there is \(\eta_\pi>0\), independent of the smooth vectors, such that every smooth coefficient satisfies
\[
 |\langle\pi(g)u,v\rangle|
       \le C_{u,v}D_C(g)^{1/2}e^{-\eta_\pi\sigma(g)}.
\tag{6.81}
\]
There is also \(\epsilon_\pi>0\), independent of \(u,v\), such that
\[
 \int_{G/Z}|\langle\pi(g)u,v\rangle|^2
            e^{2\epsilon_\pi\sigma(g)}\,d\bar g<\infty.
\tag{6.82}
\]
In particular, for a constant depending on the vectors, the unweighted squared tail over \(\sigma>R\) is at most \(C_{u,v}e^{-2\epsilon_\pi R}\). Every polynomial weight in \(\sigma\) is square-integrable against the squared coefficient as well.

**Proof: one smooth pair.** Suppose first \(r>1\), and choose a principal level as in the full covering argument of Theorem 6.25, fixing the finitely many rotations and division residues of one nonzero smooth pair. At this level every matrix
\(S_j=\delta_j^{-1/2}T_{a_j}\) has spectral radius less than one. Choose \(\rho<1\) larger than all these radii. The finite Jordan expansion used in that theorem gives \(\|S_j^k\|\le C_j\rho^k\), after increasing \(\rho\) slightly if necessary. Equations (6.54)–(6.56) therefore bound the coefficient on every translated cone by
\[
 C\left(\prod_j\delta_j^{\ell_j/2}\right)
                            \rho^{\sum_j\ell_j}.
\tag{6.83}
\]
All the translating sets are finite. In the Cartan covering the residue matrix \(b=\operatorname{diag}(\Pi^{\epsilon_i})\), \(0\le\epsilon_i<d\), has bounded elementary divisors. For \(t_\ell\),
\(\sigma(t_\ell)=d\sum_j\ell_j\) and
\(D_C(t_\ell)=\prod_j\delta_j^{\ell_j}\).
Lemma 6.33 shows that adding those fixed residues changes the length by a bounded amount and \(D_C\) by bounded factors. The compact rotations change neither. Equation (6.83) proves (6.81) for this pair with some \(\eta>0\).

For the integral, the volume factor in (6.55) cancels the squared modulus factor in (6.83). Since \(\sigma\le d\sum\ell_j+C\), choose \(\epsilon>0\) with \(\rho e^{\epsilon d}<1\). The weighted integral is bounded by a constant times
\[
 \sum_{\ell\in\mathbb Z_{\ge0}^{r-1}}
                  (\rho e^{\epsilon d})^{2\sum_j\ell_j}
       =\bigl(1-\rho^2e^{2\epsilon d}\bigr)^{-(r-1)}.
\tag{6.84}
\]
The translated covering may overlap; summing its integrals is an upper bound, which suffices. This proves (6.82) for this pair. If \(r=1\), the central quotient is compact and \(\sigma=0\), so both assertions hold directly.

**Proof: the same exponents for all smooth pairs.** Fix the preceding nonzero coefficient. Smooth algebraic irreducibility, proved in Proposition 6.19, expresses any other smooth coefficient as a finite linear combination of its left and right translates. The two weights in (6.81) are comparable under each fixed translation by (6.79). Thus the same \(\eta\) works for every such finite combination. For (6.82), translation changes \(\sigma\) by at most a constant and preserves quotient Haar measure; the same \(\epsilon\) works for each translate and their finite sums, by the finite Cauchy–Schwarz inequality. These choices give \(\eta_\pi,\epsilon_\pi\).

On \(\sigma>R\) the exponential weight is at least \(e^{2\epsilon_\pi R}\), giving the tail bound. Finally every polynomial is bounded on \([0,\infty)\) by a constant times \(e^{2\epsilon_\pi\sigma}\). This gives the last assertion. \(\square\)

The exponent is common to the representation; the constants need not be uniform over its smooth vectors. Equation (6.81) is a bound by the explicit Cartan weight in (6.78). Corollary 6.83 places these coefficients in the Schwartz algebra and proves rapid approximation by compact cutoffs in each Schwartz norm.

Let \(\mathscr H_{\omega^{-1}}\) be the Hilbert space of measurable functions with
\(f(zg)=\omega(z)^{-1}f(g)\) and finite quotient squared norm. Write \(\mathscr D_\omega\) for its smooth compact-mod-centre test functions. Left translation is \(\lambda(h)f(g)=f(h^{-1}g)\). These tests are dense: in compact quotient charts, smoothness of \(\omega\) trivializes the central rule on sufficiently small compact-open cosets. Their successive finite partitions generate the Borel sets. Approximation of indicators in measure, then of simple functions in squared norm, proves density on a compact set; exhaustion by compact sets proves density in the whole space. The same argument gives a countable dense set, because \(G/Z\) is second countable.

For a discrete series and Hilbert vectors put
\[
 E^\pi_{u,v}(g)=d_\pi\langle u,\pi(g)v\rangle.
\tag{6.85}
\]
These functions lie in \(\mathscr H_{\omega^{-1}}\). Denote their closed span by \(\mathscr C_\pi\).

**Theorem 6.35 — the discrete Fourier blocks and Bessel inequality.** The discrete series with fixed \(\omega\) form an at most countable set of equivalence classes. For \(f\in\mathscr D_\omega\), put
\(A_\pi(f)=\int_{G/Z}f(g)\pi(g)\,d\bar g\). This map extends to every \(f\in\mathscr H_{\omega^{-1}}\), with Hilbert–Schmidt values, and
\[
 \sum_\pi d_\pi\|A_\pi(f)\|_{\mathrm{HS}}^2
                      \le\|f\|_2^2.
\tag{6.86}
\]
The orthogonal projection onto \(\mathscr C_\pi\) is
\[
 P_\pi f=\sum_{i,j}(A_\pi(f))_{ij}E^\pi_{e_i,e_j},
 \qquad
 \|P_\pi f\|_2^2=d_\pi\|A_\pi(f)\|_{\mathrm{HS}}^2,
\tag{6.87}
\]
where \((e_i)\) is any orthonormal Hilbert basis. All sums in this formula converge in \(L^2\). The map
\(u\otimes\overline v\mapsto d_\pi^{-1/2}E^\pi_{u,v}\) identifies
\(H_\pi\widehat\otimes\overline{H_\pi}\) unitarily with \(\mathscr C_\pi\), with left translation acting as \(\pi\) on the first factor.

**Proof.** By Theorem 6.15, the functions
\(d_\pi^{-1/2}E^\pi_{e_i,e_j}\), over all \(i,j\) and inequivalent \(\pi\), are orthonormal. Each coefficient space is nonzero. An orthonormal set in a separable Hilbert space is countable: distinct vectors have disjoint open balls of radius less than \(1/\sqrt2\), and every ball contains a different point of a countable dense set. Choosing one unit coefficient in each space proves the class-countability assertion. Admissibility and the increasing principal fixed spaces also give a countable smooth orthonormal basis of each \(H_\pi\).

For compact tests the Fourier coefficient along this orthonormal family is
\[
 \left\langle f,d_\pi^{-1/2}E^\pi_{e_i,e_j}\right\rangle_{L^2}
            =\sqrt{d_\pi}\,(A_\pi(f))_{ij}.
\tag{6.88}
\]
For a finite orthonormal set, subtract its orthogonal projection from \(f\); expanding the nonnegative squared norm gives Bessel's inequality. Taking increasing finite subsets gives (6.86). It also makes the series (6.87) Cauchy and identifies its limit as the indicated orthogonal projection. Density extends these formulas to all \(L^2\) functions. More explicitly every entry is still the absolutely convergent scalar integral
\(\int f(g)\langle\pi(g)e_j,e_i\rangle\,d\bar g\), by Cauchy–Schwarz and (6.29). Inequality (6.86) makes those entries a Hilbert–Schmidt operator, independently of basis. Applying (6.29) to finite tensor sums proves the asserted isometry; completing its domain gives precisely its closed coefficient span. The formula for left translation follows directly from (6.85). \(\square\)

For a compact open \(K\) with \(\omega|_{K\cap Z}=1\), put
\(n_\pi(K)=\dim H_\pi^K\), and give \(\overline K=KZ/Z\) its quotient volume. The test supported on \(ZK\), of value \(1/\operatorname{vol}(\overline K)\) on \(K\) and extended by \(\omega^{-1}\), acts as the compact projection on every \(\pi\). Its squared norm is \(\operatorname{vol}(\overline K)^{-1}\). Consequently (6.86) gives the useful mass bound
\[
          \sum_\pi d_\pi n_\pi(K)
                   \le\operatorname{vol}(\overline K)^{-1}.
\tag{6.89}
\]
This does not require a lower bound for formal degrees.

**Theorem 6.36 — absolutely convergent matrix units and the full discrete projection.** For functions with the central rule above use
\((f*h)(x)=\int_{G/Z}f(y)h(y^{-1}x)\,d\bar y\). For Hilbert vectors and discrete series with central character \(\omega\), every convolution of two functions (6.85) converges absolutely at every \(x\), and
\[
 \begin{gathered}
 E^\pi_{u,v}*E^\pi_{a,b}
                       =\langle a,v\rangle E^\pi_{u,b},\\
 E^\pi_{u,v}*E^\tau_{a,b}=0\quad(\pi\not\simeq\tau),\qquad
 (E^\pi_{u,v})^*=E^\pi_{v,u},
 \end{gathered}
\tag{6.90}
\]
where \(f^*(g)=\overline{f(g^{-1})}\). Left convolution by \(E^\pi_{u,v}\) extends to a bounded operator \(L^\pi_{u,v}\) on \(\mathscr H_{\omega^{-1}}\), of norm \(\|u\|\|v\|\). It acts on the first tensor factor of \(\mathscr C_\pi\) as \(w\mapsto\langle w,v\rangle u\) and annihilates its orthogonal complement. For an orthonormal basis,
\[
                    P_\pi=\sum_i L^\pi_{e_i,e_i}
                         \quad\text{strongly}.
\tag{6.91}
\]
The orthogonal sum of these coefficient spaces is exactly the closed span of all irreducible admissible unitary subrepresentations of the left regular representation. Thus (6.86) is an equality on this discrete subspace; its orthogonal complement is the common kernel of all \(A_\pi\).

**Proof: convolution and boundedness.** Two \(L^2\) functions have an absolutely convergent convolution at each fixed \(x\), since its absolute integral is at most their two \(L^2\) norms by Cauchy–Schwarz and unimodularity. The integrand has trivial central covariance in the integration variable, so it is a quotient integral. In the first convolution of (6.90), the two factors inside it, after removing \(d_\pi^2\), are
\(\overline{\langle\pi(y)v,u\rangle}\) and
\(\langle\pi(y)a,\pi(x)b\rangle\).
Schur orthogonality evaluates their integral as
\(d_\pi^{-1}\langle a,v\rangle\langle u,\pi(x)b\rangle\).
This proves the first identity; cross orthogonality proves the second. Inversion and conjugation give the adjoint identity directly.

For arbitrary \(f\in L^2\), a change of variable \(y=xz^{-1}\) gives the pointwise formula
\[
 E^\pi_{u,v}*f=E^\pi_{u,A_\pi(f)^*v}.
\tag{6.92}
\]
Indeed the right side is
\(d_\pi\int f(z)\langle u,\pi(xz^{-1})v\rangle\,d\bar z\); its scalar integral is absolutely convergent. Equation (6.29) and (6.86) give
\(\|E^\pi_{u,v}*f\|_2\le\|u\|\|v\|\|f\|_2\).
The matrix-unit formula shows that the bound is attained on the appropriate unit coefficient when both vectors are nonzero. Equation (6.87) shows that it vanishes on \(\mathscr C_\pi^\perp\). On \(\mathscr C_\pi\) it is the asserted tensor operator. Orthogonal partial sums of the rank-one projections on the first factor now prove (6.91). This also proves the operator adjoint assertions without exchanging any triple integral.

**Proof: all discrete subrepresentations are included.** Let \(T:H_\tau\to\mathscr H_{\omega^{-1}}\) be a nonzero bounded intertwiner for an irreducible admissible unitary \(\tau\). Average its output on the right over a sufficiently small principal \(K\), writing \(Q_KT\). Such averages converge strongly to the identity on \(L^2\), first for locally constant compact tests and then by density and their contraction bound. Some \(Q_KT\) is therefore nonzero. Evaluation at the identity after this average is a bounded functional:
\[
 |(Q_KTv)(1)|\le
       \operatorname{vol}(\overline K)^{-1/2}\|T\|\|v\|.
\tag{6.93}
\]
This is just Cauchy–Schwarz on \(\overline K\), choosing \(K\) with trivial central character on \(K\cap Z\). By the Hilbert representation argument of Lemma 6.14 it equals \(\langle v,u_K\rangle\) for a Hilbert vector \(u_K\). Intertwining with left translation consequently gives
\((Q_KTv)(g)=\langle v,\tau(g)u_K\rangle\).
Right-\(K\)-invariance makes these averaged functions well defined on each open coset, so the identity also specifies their \(L^2\) representatives. Nonzero \(Q_KT\) supplies a nonzero square-integrable coefficient of \(\tau\). Theorem 6.15 makes \(\tau\) a discrete series. Each \(Q_KTv\) then belongs to \(\mathscr C_\tau\). Letting \(K\) decrease proves \(T(H_\tau)\subset\mathscr C_\tau\), since that space is closed. Conversely, the tensor description of Theorem 6.35 expresses \(\mathscr C_\pi\) as a Hilbert sum of copies of \(\pi\) under left translation. Both inclusions follow. The projection identities give the remaining norm and kernel assertions. \(\square\)

**Corollary 6.37 — simultaneous compact trace approximation.** Choose a smooth unit vector \(u\in H_\pi^K\), and set
\[
 E=E^\pi_{u,u},\qquad E_R=\mathbf1_{\{\sigma\le R\}}E.
\tag{6.94}
\]
These are smooth compact-mod-centre tests \(E_R\), all bi-\(K\)-invariant after taking \(K\subset K_0\). There are constants \(C,\epsilon>0\) such that
\[
 \begin{gathered}
 \|E_R-E\|_2^2\le Ce^{-2\epsilon R},\\
 \sum_{\tau:\,n_\tau(K)>0}
    \frac{d_\tau}{n_\tau(K)}
       \left|\operatorname{tr}\tau(E_R)
                           -\mathbf1_{\tau\simeq\pi}\right|^2
                  \le\|E_R-E\|_2^2.
 \end{gathered}
\tag{6.95}
\]
The sum runs over all discrete series with central character \(\omega\). It is one bound for the entire family.

**Proof.** The compactness and local constancy assertions follow from Lemma 6.33 and smoothness of the coefficient. Theorem 6.34 gives its tail bound, including the factor \(d_\pi^2\). For a bi-\(K\) function, \(A_\tau(f)\) has both its domain and range compressed to \(H_\tau^K\). This follows first by the two compact averages for tests, and then for \(L^2\) functions by continuity of \(A_\tau\). Theorem 6.35 and (6.90) give
\(A_\tau(E)=0\) for \(\tau\not\simeq\pi\), and
\(A_\pi(E)w=\langle w,u\rangle u\), of trace one. For an operator on an \(n\)-dimensional space, Cauchy–Schwarz on its diagonal gives
\(|\operatorname{tr}A|^2\le n\|A\|_{\mathrm{HS}}^2\).
Apply it to each block of \(E_R-E\), multiply by \(d_\tau/n_\tau(K)\), and sum using (6.86). This is exactly (6.95). Blocks with \(n_\tau(K)=0\) vanish and require no division. \(\square\)

**Example 6.38 — the Steinberg truncation with its exact error.** Keep the unit edge vector and volume normalization of (6.62). Its formal degree is \(d=(q-1)/2\). Let \(E=d\,\overline{\langle\mathrm{St}(g)u,u\rangle}\), and, for an integer \(R\ge0\), truncate this time to edge distance \(l\le R\). The edge spheres used in (6.62) give
\[
 \|E-E_R\|_2^2
   =d^2\frac4{q+1}\sum_{l>R}q^{-l}
   =\frac{q-1}{q+1}q^{-R}.
\tag{6.96}
\]
These tests are bi-invariant under the Iwahori subgroup \(I\) fixing the two endpoints of the base edge. Its invariant space in Steinberg is one-dimensional. Indeed \(I\) has two orbits on the boundary: in the usual projective coordinate they are \(\mathcal O_F\) and its complement. Translations act transitively on the first; after inversion the second is \(\mathfrak p_F\), where the corresponding lower translations act transitively. The boundary function model modulo constants therefore has invariant dimension \(2-1=1\); compact averaging makes passing to this quotient exact. Consequently
\[
 \operatorname{tr}\mathrm{St}(E_R)
    =d\int_{l\le R}|\langle\mathrm{St}(g)u,u\rangle|^2d\bar g
    =1-\frac2{q+1}q^{-R}.
\tag{6.97}
\]
The proof of (6.95) applies to this bi-\(I\) cutoff as well. For every other discrete series the trace tends to zero, with the simultaneous squared error in (6.95) bounded by the exact expression (6.96), taking \(K=I\). The volume \(2/(q+1)\) in the sphere computation is that of the full unoriented edge stabilizer; the smaller \(I\) fixes the vector and suffices for the trace compression. No invariance under an edge reversal is needed.

The discrete projection above concerns coefficient spaces in \(L^2(G/Z)\). Elliptic character orthogonality and completeness concern the different torus-weighted space (6.16). Passing from the first space to the second still requires orbital convergence and the corresponding character comparison.

### 6.10. Contracting elements and character descent

We use ordinary Haar measure on \(G\) in this section. For a smooth admissible complex representation \(V\), its trace distribution is
\(D_V(f)=\operatorname{tr}\pi(f)\), \(f\in C_c^\infty(G)\). The operator has finite rank by the two compact averages in Proposition 6.16. A local character density on an open set means a locally constant function \(\Theta_V\) satisfying \(D_V(f)=\int f\Theta_V\) for every test supported there. The assertions below specify where such a density is proved to exist.

**Lemma 6.39 — the slope parabolic and an adapted order.** Every \(\gamma\in\mathrm{GL}_r(D_0)\) has a canonical decomposition of its right division vector space
\[
 W=\bigoplus_{i=1}^s W_i,\qquad
       \nu_1>\nu_2>\cdots>\nu_s,
\tag{6.98}
\]
where all algebraic eigenvalues of \(\gamma_i=\gamma|_{W_i}\) have extended \(F\)-valuation \(\nu_i\). Let \(M=\prod_i\mathrm{GL}_{D_0}(W_i)\), and let \(P=MN\) be upper block triangular in this ordering. There is a compact open unital \(\mathcal O_F\)-order \(\mathfrak A\subset\operatorname{End}_{D_0}(W)\), with these block projections, such that, for \(K_m=1+\varpi_F^m\mathfrak A\), \(m\ge1\),
\[
 \begin{gathered}
 K_m=(K_m\cap N)(K_m\cap M)(K_m\cap\overline N),\\
 \gamma(K_m\cap N)\gamma^{-1}\subset K_m\cap N,\\
 \gamma(K_m\cap M)\gamma^{-1}=K_m\cap M,\\
 \gamma^{-1}(K_m\cap\overline N)\gamma\subset K_m\cap\overline N.
 \end{gathered}
\tag{6.99}
\]
Conjugation by positive powers of \(\gamma\) contracts \(N\), and negative powers contract \(\overline N\). These assertions remain true, with the same \(K_m\), for \(\gamma t\) whenever \(t\in1+\varpi_F\mathfrak A_M\), where \(\mathfrak A_M\) is its block diagonal part. All \(K_m\) are normal in \(\mathfrak A^\times\).

Moreover, \(s=1\) if and only if the cyclic subgroup generated by \(\gamma Z\) has compact closure in \(G/Z\). No semisimplicity or separability of \(\gamma\) is required.

**Proof: the slopes.** Factor the minimal polynomial of \(\gamma\) into powers of irreducible polynomials over \(F\). By Extensions of complete valued fields, Theorem 1.2, the absolute value extends uniquely to algebraic extensions, including inseparable ones. Every root of one irreducible polynomial therefore has the same valuation. The norm formula in that theorem makes this valuation rational. Group the primary factors by this value. Bézout identities for the pairwise coprime grouped polynomials give their projection idempotents as polynomials in \(\gamma\): the identities give the direct sum of their kernels, and each projection is identity on its kernel and zero on the others. These are right-\(D_0\)-linear idempotents, proving (6.98). This also proves uniqueness of the decomposition.

Choose \(e\ge1\) with \(a_i=e\nu_i\in\mathbb Z\), and put \(u_i=\varpi_F^{-a_i}\gamma_i^e\). All roots of the ordinary \(F\)-linear characteristic polynomial of \(u_i\) are units. Its coefficients are integral and its constant coefficient is a unit. Cayley–Hamilton consequently expresses both \(u_i\) and \(u_i^{-1}\) integrally in the finite span of its powers. Starting with any \(\mathcal O_F\)-lattice, its sum of these finitely many power translates is stable under \(u_i^{\pm1}\). Close it under right \(\mathcal O_{D_0}\)-multiplication, using a finite \(\mathcal O_F\)-basis of that ring. The result is a full division lattice \(L_i\) still stable under \(u_i^{\pm1}\), because the operator is division-linear.

Put \(L=\bigoplus L_i\), \(\mathfrak A_0=\operatorname{End}_{\mathcal O_{D_0}}(L)\), and
\[
              \mathfrak A=\bigcap_{j=0}^{e-1}
                      \gamma^j\mathfrak A_0\gamma^{-j}.
\tag{6.100}
\]
This finite intersection is a compact open unital order. Each block projection lies in every intersectand. On the upper block \(\operatorname{Hom}_{D_0}(W_j,W_i)\), \(i<j\), conjugation by \(\gamma^e\) takes its \(\mathfrak A_0\)-lattice onto \(\varpi_F^{a_i-a_j}\) times that lattice. Here the \(u_i\) preserve \(L_i\), and \(a_i-a_j\ge1\). The inverse action has the corresponding contracting property on lower blocks. On diagonal blocks conjugation by \(\gamma^e\) preserves \(\mathfrak A_0\).

Intersecting as in (6.100) shows that one step preserves the upper lattice, its inverse preserves the lower lattice, and one step preserves the diagonal order in both directions. For example the upper intersectands after one step have indices \(1,\ldots,e\); the last is contained in the missing index-zero lattice. For the lower assertion use its inverse step: the index-minus-one intersectand is contained in the missing index-\(e-1\) lattice, since the \(e\)-th positive step expands the lower lattice. The \(e\)-th contracting steps take the resulting upper and lower lattices into \(\varpi_F\) times themselves. This proves contraction and cofinality.

Block Gaussian elimination in \(1+\varpi_F^m\mathfrak A\) gives the factorization (6.99). Pivots \(1+\varpi_F^m X\) have inverses by their convergent geometric series in the order; Schur complements stay in their block lattices because \(\mathfrak A\) is closed under multiplication. Induction on the blocks proves existence and uniqueness. The same argument in each finite quotient modulo \(\varpi_F^l\mathfrak A\) proves that the product of the three Haar probabilities is the Haar probability of \(K_m\). Equivalently, one can count the unique Gaussian coordinates in that finite quotient and then pass to the inverse limit. Normality in \(\mathfrak A^\times\) follows directly from the two-sided ideal \(\varpi_F^m\mathfrak A\).

A block diagonal \(t\in1+\varpi_F\mathfrak A_M\) normalizes the order lattices, and its conjugation is identity modulo \(\varpi_F\) on them. Thus the upper action of \(\gamma t\) has the same reduction as that of \(\gamma\), whose \(e\)-th power is zero there. Its \(e\)-th power also contracts by at least \(\varpi_F\). The inverse lower action has the same property; the middle order remains normalized. This proves all assertions for these perturbations.

If all slopes coincide, \(\gamma^e=\varpi_F^{a_1}u\) for an integral lattice automorphism \(u\). The powers of \(\gamma\) modulo \(Z\) lie in a finite union of translates of \(\operatorname{GL}_{\mathcal O_{D_0}}(L)\), so their closure is compact. If two slopes differ, conjugation by \(\gamma\) on the corresponding off-diagonal homomorphisms has eigenvalues with nonzero valuation. Indeed after splitting the division algebra and triangularizing the matrices, those eigenvalues are the ratios of their eigenvalues on the two blocks. Positive or negative powers of this operator are unbounded. A compact closure of the powers in \(G/Z\) would have bounded image under the continuous adjoint action, a contradiction. \(\square\)

In these coordinates \(P=P_\gamma\) is the slope parabolic. If \(r_i=\dim_{D_0}W_i\), its modulus is
\[
 \delta_P(\gamma)
   =q_F^{-d^2\sum_{i<j}r_i r_j(\nu_i-\nu_j)}.
\tag{6.101}
\]
To prove this, conjugation on the \(i,j\) block has \(F\)-dimension \(d^2r_i r_j\), and all its eigenvalues have valuation \(\nu_i-\nu_j\). Taking the determinant and multiplying the block factors gives exactly (6.101).

**Lemma 6.40 — finite generation of Jacquet modules.** If \(V\) is generated by finitely many smooth vectors, then \(V_N\) is finitely generated as an \(M\)-representation. If \(V\) is also admissible and every block of \(M\) has division dimension one, then \(V_N\) is finite-dimensional.

**Proof.** In a division basis, \(G=PK_0\). Here is a direct Iwasawa proof. In the last row of a matrix, move an entry of least division valuation to the last position. Its left ratios with the other row entries are integral. Integral column operations therefore kill those other entries. The remaining upper-left matrix is invertible; repeat on it. Right multiplication by the resulting integral invertible matrix makes the original matrix upper triangular. This proves \(G=BK_0\), hence \(G=PK_0\).

The orbit of a smooth vector under compact \(K_0\) is finite, since its open stabilizer has finite index. For a finite generating set, take the finitely many such orbit vectors and project to \(V_N\). Iwasawa and the trivial action of \(N\) on coinvariants show that their \(M\)-translates span \(V_N\). This proves finite generation.

Admissibility of \(V_N\) was proved in Lemma 6.22. If \(M=(D_0^\times)^s\), the products of \(1+\mathfrak p_{D_0}^l\) form compact open subgroups normal in all of \(M\). Choose one fixing the finitely many generators just found. Normality makes it fix all their \(M\)-translates, hence the entire Jacquet module. Admissibility makes this fixed space finite-dimensional. \(\square\)

**Theorem 6.41 — the exact contracting trace identity.** Let \(V\) be any smooth admissible representation, \(\gamma\in G\), and use the parabolic and compact groups of Lemma 6.39. Write \(J=V_N\) with its unnormalized \(M\)-action \(\rho\), \(P_m\) for averaging on \(K_m\), and
\(T=P_m\pi(\gamma)P_m\) on \(U_m=V^{K_m}\). Then the stable kernel is \(U_m\cap V(N)\), and the stable image maps isomorphically to \(J^{K_m\cap M}\). In particular, for every integer \(n\ge1\),
\[
 \begin{gathered}
 \operatorname{tr}_{U_m} T^n
       =\operatorname{tr}\bigl(\pi(\gamma^n)P_m\bigr)\\
       =\operatorname{tr}\left(
           \rho(\gamma^n)|_{J^{K_m\cap M}}\right).
 \end{gathered}
\tag{6.102}
\]
The same assertions hold for \(\gamma t\), \(t\in1+\varpi_F\mathfrak A_M\), with the same sequence of groups. The traces in (6.102) require no eventual-power restriction.

**Proof: positive products and kernel.** Put \(K_+=K_m\cap N\). For \(v\in U_m\), the middle and lower factors in the Gaussian average fix \(\pi(\gamma)v\), by (6.99). Thus \(Tv=E_{K_+}\pi(\gamma)v\). Since \(\gamma K_+\gamma^{-1}\subset K_+\), multiplying these probability operators gives
\[
 T^n v=E_{K_+}\pi(\gamma^n)v
      =\pi(\gamma^n)E_{\gamma^{-n}K_+\gamma^n}v.
\tag{6.103}
\]
The expanded compact subgroups in the last average are nested and exhaust \(N\). The finite difference argument of Lemma 6.22, repeated here, says that a vector lies in \(V(N)\) exactly when one of these averages kills it. For a sum of differences, put all its finitely many unipotent translations in one expanded subgroup. Conversely the difference between a smooth vector and its compact average is a finite sum of such differences. Equation (6.103) therefore identifies the stable kernel as asserted.

Finite-dimensional stabilization splits \(U_m\) into that kernel and the stable image of \(T\), with \(T\) invertible on the latter. Projection to coinvariants identifies its image with \(j(U_m)\), because its kernel is exactly the stable kernel. Moreover
\(j(Tv)=\rho(\gamma)j(v)\): the upper average disappears, and \(\gamma\) normalizes \(K_m\cap M\).

**Proof: the entire fixed space.** The finite image \(j(U_m)\) is stable under the invertible group action of \(\gamma\). Its restriction there is injective and hence bijective. Given \(w\in J^{K_m\cap M}\), average a smooth lift over this middle group. For large \(k\), \(\gamma^{-k}(K_m\cap\overline N)\gamma^k\) fixes that lift, by contraction and smoothness. The middle group also fixes its \(\gamma^k\)-translate, since \(\gamma\) normalizes it. Averaging that translate on \(K_m\) consequently has coinvariant image \(\rho(\gamma)^k w\). This belongs to \(j(U_m)\); bijectivity of \(\gamma\) on that finite image puts \(w\) there as well. This proves the stable-image isomorphism.

On the stable kernel, \(T\) is nilpotent, so every positive power has trace zero. On its stable image it is identified with \(\rho(\gamma)\). This proves the first-to-last equality in (6.102). Equation (6.103) also identifies \(T^n\) with \(P_m\pi(\gamma^n)P_m\) on \(U_m\). The finite-rank trace of \(\pi(\gamma^n)P_m\) equals the trace of this compression: choose a basis of \(U_m\) and extend it to the whole vector space. The diagonal coefficients outside its finite domain are zero. This proves the middle equality. Lemma 6.39 gives the same contraction and normalization for \(\gamma t\), so the proof applies to it unchanged. At power zero the two fixed-space dimensions may differ; no equality at that power is asserted. \(\square\)

Thus the normalized average of the trace distribution on the right coset \(\gamma K_m\) is exactly the normalized Jacquet trace at this level. We next prove when these averages define an actual locally constant character.

**Theorem 6.42 — local descent from a Levi density.** Suppose \(D_J\), for the unnormalized Jacquet module in Theorem 6.41, has a locally constant density \(\Theta_J\) in a neighbourhood of \(\gamma\) in \(M\). Then \(D_V\) has a locally constant density near \(\gamma\) in \(G\), and
\[
              \Theta_V(\gamma)=\Theta_J(\gamma)
                   =\delta_P(\gamma)^{1/2}
                                \Theta_{\pi_P}(\gamma),
\tag{6.104}
\]
where the last character uses normalized Jacquet action. If \(P=G\), this is the identity assertion; it supplies no new character-regularity conclusion in that case.

**Proof: a local conjugacy chart.** Let \(\mathfrak s\) be the sum of the off-diagonal blocks. The map, for small \(X\in\mathfrak s\), \(Y\in\mathfrak m\), is
\[
 (X,Y)\longmapsto
       (1+X)^{-1}\gamma(1+Y)(1+X).
\tag{6.105}
\]
After left translation by \(\gamma^{-1}\), its derivative at zero is
\(Y+X-\gamma^{-1}X\gamma\).
On each off-diagonal block every eigenvalue of \(\operatorname{Ad}(\gamma^{-1})\) has nonzero valuation, by the slope calculation. None is one. Thus this derivative is an invertible \(F\)-linear map from \(\mathfrak s\oplus\mathfrak m\) to the full algebra.

For completeness, the local inverse assertion follows by contraction and works in positive characteristic too. Compose a power-series map with its inverse linear derivative. On a sufficiently small complete lattice ball it has the form \(z\mapsto z+R(z)\), where the higher terms have Lipschitz constant less than one and map the ball into itself. For any target in that ball, the iteration \(z\mapsto y-R(z)\) converges to its unique preimage. Its successive differences shrink geometrically, and completeness proves both existence and uniqueness. Applied to the rational map (6.105), whose matrix inverse is a convergent geometric series near zero, this gives an open image containing \(\gamma\).

Shrink these balls so that \(1+X\in\mathfrak A^\times\), and so that \(1+Y\) belongs to \(1+\varpi_F^a\mathfrak A_M\) for a chosen \(a\ge1\). Every \(x\) in some neighbourhood \(U\) of \(\gamma\) therefore has the form
\(x=k^{-1}\gamma t k\), with \(k\in\mathfrak A^\times\) and \(t\in1+\varpi_F^a\mathfrak A_M\). All these \(k\) normalize every \(K_m\).

**Proof: one common partition, not a limit of unrelated averages.** Choose \(a\) large enough that \(\Theta_J\) is constant, of value \(c\), on \(\gamma(1+\varpi_F^a\mathfrak A_M)\). For every \(m\ge a\) and every such \(t\), Theorem 6.41 and the defining density property on \(M\) give
\[
 \frac{D_V(\mathbf1_{\gamma tK_m})}{\operatorname{vol}_G(K_m)}
       =\frac{D_J(\mathbf1_{\gamma t(K_m\cap M)})}
                    {\operatorname{vol}_M(K_m\cap M)}=c.
\tag{6.106}
\]
Conjugation invariance of the finite-rank trace, and normalization of \(K_m\) by \(k\), give the same first average on \(xK_m\). Conjugation by this compact-group element preserves Haar measure. Shrink \(U\) to \(\gamma K_b\) contained in the chart. For every sufficiently large \(m\), its right-\(K_m\) cosets thus all have average \(c\).

Any smooth compact test supported in this \(U\) is, for one sufficiently large \(m\), a finite linear combination of indicators of those right cosets. Compactness and local constancy give that common level. Equation (6.106) then gives \(D_V(f)=c\int f\). This proves an actual locally constant density on \(U\), without assuming regularity of \(D_V\). Normalization twists the Levi action by \(\delta_P^{-1/2}\). This character is locally constant and equals its value at \(\gamma\) on a sufficiently small neighbourhood, giving the second equality in (6.104). \(\square\)

**Corollary 6.43 — support for zero proper Jacquet modules.** Suppose \(V_N=0\) for every proper parabolic. Its trace distribution vanishes on the open set of elements whose cyclic subgroup modulo \(Z\) does not have compact closure. This includes nonsemisimple elements and, in positive characteristic, elements with inseparable primary factors.

**Proof.** For every such \(\gamma\), Lemma 6.39 gives a proper \(P_\gamma\). Its Jacquet module is zero, whose trace distribution has zero density everywhere. Theorem 6.42 proves that \(D_V\) vanishes on a neighbourhood of \(\gamma\). These neighbourhoods cover the indicated open set, and a compactly supported locally constant test has a finite compact-open partition subordinate to them, so its trace is zero. In the unitary irreducible category Theorem 6.24 makes the hypothesis equivalent to compact support modulo the centre of all smooth coefficients. The conclusion concerns the trace distribution; it asserts no vanishing on compact split regular elements. \(\square\)

**Corollary 6.44 — the minimal slope-Levi character is an ordinary finite trace.** Suppose every \(W_i\) in (6.98) has division dimension one, and \(V\) is finitely generated and admissible. Then \(D_V\) has a locally constant density near \(\gamma\), with
\[
                    \Theta_V(\gamma)
                         =\operatorname{tr}(\rho(\gamma)|_{V_N}).
\tag{6.107}
\]
The same conclusion holds whenever this Jacquet module is known directly to be finite-dimensional.

**Proof.** Lemma 6.40 gives finite dimension. A finite-dimensional smooth representation is trivial on some common open subgroup: intersect the stabilizers of a basis. Hence \(m\mapsto\operatorname{tr}\rho(m)\) is locally constant everywhere and is its trace density, by integrating the finite matrix entries. Theorem 6.42 applies and gives (6.107). \(\square\)

**Example 6.45 — principal series and Steinberg on all noncompact split classes of \(\mathrm{GL}_2(F)\).** Write \(\gamma=\operatorname{diag}(a,b)\), \(0<|a/b|<1\). The two-cell calculation in Lesson 6, Theorem 4.1, gives the two normalized Jacquet constituents of \(I(\mu_1,\mu_2)\), without assuming that the extension splits. Trace is additive on an invariant subspace and its quotient. Thus Corollary 6.44 gives the actual character value
\[
 \Theta_{I(\mu_1,\mu_2)}(\gamma)
    =|a/b|^{1/2}
       \bigl(\mu_1(a)\mu_2(b)+\mu_2(a)\mu_1(b)\bigr).
\tag{6.108}
\]
For equal parameters \(\mu_1=\mu_2=1\), this is \(2|a/b|^{1/2}\). At \(\operatorname{diag}(\varpi_F^k,1)\), \(k\ge1\), it is \(2q_F^{-k/2}\), whereas the spherical coefficient of (6.75) has its nonzero linear polynomial. Trace removes the nilpotent part; the coefficient need not do so.

For \(\tau=C^\infty(\mathbb P^1(F))=I(|\cdot|^{-1/2},|\cdot|^{1/2})\), constants and its Steinberg quotient give
\(0\to\mathbf1\to\tau\to\mathrm{St}\to0\).
The exact coinvariant argument in Lesson 6, Proposition 2.2, and its two-cell calculation make \(\tau_N\) have unnormalized constituents \(1,\delta_B\). Constants supply the first line, so \(\mathrm{St}_N=\delta_B\). Therefore
\[
              \Theta_{\mathrm{St}}(\gamma)=|a/b|,
 \qquad
 \Theta_{\mathrm{St}\otimes(\chi\circ\det)}(\gamma)
                         =\chi(ab)|a/b|.
\tag{6.109}
\]
For \(\tau\), (6.108) gives \(1+|a/b|\), agreeing with the sum of the constant and Steinberg characters. This also exhibits why Corollary 6.43 cannot be applied to every discrete series: Steinberg has a nonzero proper Jacquet module and a nonzero character here. Swapping \(a,b\) covers the opposite ordering. The formulas cover precisely the split regular classes with unequal absolute values.

**Example 6.46 — a fractional slope, including characteristic two.** Take \(D_0=F\) and
\[
 C=\begin{pmatrix}0&\varpi_F\\1&0\end{pmatrix},\qquad
 \gamma=\operatorname{diag}(C,1)\in\mathrm{GL}_3(F).
\tag{6.110}
\]
Its slope blocks have dimensions \(2,1\) and slopes \(1/2,0\). Here \(e=2\), \(C^2=\varpi_F I_2\), and (6.100) gives
\[
 \mathfrak A=
 \begin{pmatrix}
 \mathcal O_F&\varpi_F\mathcal O_F&\varpi_F\mathcal O_F\\
 \mathcal O_F&\mathcal O_F&\mathcal O_F\\
 \mathcal O_F&\mathcal O_F&\mathcal O_F
 \end{pmatrix}.
\tag{6.111}
\]
Indeed conjugating an integral two-by-two block by \(C\) gives entries \((d,\varpi_F c;b/\varpi_F,a)\); intersection with the integral block yields its displayed order. The upper off-diagonal lattice is \(\varpi_F\mathcal O_F\oplus\mathcal O_F\). Multiplication by \(C\) preserves it and its square multiplies it by \(\varpi_F\). The lower lattice is \(\mathcal O_F^2\); its inverse-conjugation action is right multiplication by \(C\), with the same two-step contraction. On the upper radical the determinant is \(-\varpi_F\), so \(\delta_P(\gamma)=q_F^{-1}\), also obtained from (6.101). The trace identity (6.102) consequently uses the normalized factor \(q_F^{-1/2}\) at its first power, and \(q_F^{-n/2}\) at its \(n\)-th power. In characteristic two, \(X^2-\varpi_F\) is inseparable, but all the displayed lattice, probability and descent arguments still hold. No diagonalization, division by two or exponential map was used.

Casselman's freely accessible 1977 article, §§2–5, gives the contracting trace and character–Jacquet comparison. The slope-order construction and local descent above supply the matrix-group arguments used here. For a larger slope Levi, Theorem 6.42 retains its stated Levi-density hypothesis. Character densities in the remaining compact-mod-centre blocks, the orbital estimates and elliptic character completeness still require their own arguments.

### 6.11. Lattice enclosures and finite support projections

Let \(G=\mathrm{GL}_r(D)\), with the valuation conventions of Section 6.7. Thus \(D\) has degree \(d\), \(v_D(\Pi)=1\), and \(v_D(\varpi_F)=d\). All representations and averaging operators in this subsection have complex coefficients. We construct finite support projections in every rank. The final proposition concerns a finite alternating trace on the elliptic regular set; identifying that trace with the representation's character requires the additional exactness statement specified below.

**Lemma 6.47 — lattice apartments and their enclosure.** A vertex is a homothety class of full right \(\mathcal O_D\)-lattices in \(D^r\). A simplex is a chain
\[
 L_0\supsetneq L_1\supsetneq\cdots\supsetneq L_k
       \supsetneq L_0\Pi.
 \qquad
 L(a)=\bigoplus_{i=1}^r e_i\Pi^{a_i}\mathcal O_D,
 \quad a\in\mathbb Z^r/\mathbb Z(1,\ldots,1).
\tag{6.112}
\]
The coordinate lattices for one \(D\)-basis form an apartment. A vertex \(x\) and a simplex \(\tau\) lie in a common apartment. Their enclosure \(H(x,\tau)\), defined as the intersection of all such apartments, is the following finite subcomplex of any one of them:
\[
 \begin{aligned}
 \min_{v\in\{x\}\cup\tau^0}(a_i^v-a_j^v)&\le b_i-b_j,\\
 b_i-b_j&\le\max_{v\in\{x\}\cup\tau^0}(a_i^v-a_j^v)
 \quad(1\le i,j\le r).
 \end{aligned}
\tag{6.113}
\]
Here \(\tau^0\) denotes the vertices. A linear automorphism preserving the actual lattices representing \(x\) and \(\tau\) fixes this enclosure pointwise. A full subcomplex is called convex here if it contains \(H(x,\tau)\) whenever it contains \(x\) and \(\tau\).

**Proof.** Lattice elementary divisors follow by the valuation elimination used in Section 6.7: choose a matrix entry of smallest valuation, clear its row and column with integral operations, and repeat on the smaller matrix. These operations work on either side over the division valuation ring. Consequently two lattices have simultaneous diagonal form. Apply this first to \(x\) and \(L_0\). The lattices \(x\Pi^n\) induce a finite filtration on \(L_0/L_0\Pi\); the chain representing \(\tau\) induces a flag on the same residue vector space. Two flags have a common adapted basis: successively choose bases of their intersection quotients, lift these choices, and extend within each step. To lift the resulting change of residue basis while preserving \(x\), order the elementary-divisor exponents. A residue entry forbidden by the filtration is zero; choose its lift zero. Lift the remaining block triangular entries integrally, with invertible diagonal blocks. This matrix and its inverse preserve both diagonal lattices. The lifted residue flag then diagonalizes every lattice in \(\tau\), proving the common-apartment assertion.

Normalize the coordinates of \(x\) to zero. Write \(a^0,\ldots,a^k\) for a chain representing \(\tau\); each coordinate stays fixed until it increases once by one. The relative profiles of these coordinates are intrinsic. Indeed, the residue dimensions
\(\dim_{\kappa_D}((L_j\cap x\Pi^n+x\Pi^{n+1})/x\Pi^{n+1})\)
are \(\#\{i:a_i^j\le n\}\). Their differences as \(j\) increases count the coordinates of each initial exponent that increase at each step. They therefore determine the multiplicities of all coordinate profiles. Bases for two common apartments can be relabelled to have the same profiles. The basis change \(h\) then preserves \(x\) and every actual lattice in \(\tau\).

Put \(c_{ij}=\max_{v\in\{x\}\cup\tau^0}(a_i^v-a_j^v)\). Preservation of these diagonal lattices gives
\[
 \begin{aligned}
 v_D(h_{ij}),\ v_D((h^{-1})_{ij})&\ge c_{ij},\\
 b_i-b_j\le c_{ij}&\ \Longrightarrow\ hL(b)=L(b).
 \end{aligned}
\tag{6.114}
\]
Thus every vertex satisfying (6.113) belongs to every common apartment, using the preceding alignment of bases. The same entry argument proves the asserted pointwise fixing.

Conversely, if \(b_i-b_j>c_{ij}\), the transvection \(u=1+E_{ij}\Pi^{c_{ij}}\) fixes \(x\) and \(\tau\). The lattice \(u^{-1}L(b)\) is not coordinate: its projection to \(e_iD\) has exponent \(\min(b_i,c_{ij}+b_j)<b_i\), whereas its intersection with that line has exponent \(b_i\). Projection and intersection agree for a coordinate lattice. Hence \(L(b)\) does not belong to the common apartment \(uA\). Exchanging \(i,j\) gives the other bound. The walls \(b_i-b_j=n\) subdivide an apartment into its simplices. Their half-apartments are subcomplexes, so the same description holds for simplices and their real realizations, not only vertices. After setting \(b_r=0\), the bounds allow finitely many integer vectors. This proves finiteness. The case \(r=1\) consists of a single vertex. \(\square\)

The local finiteness used below is also concrete. Simplices at a vertex are flags in the finite vector space \(L/L\Pi\). Every chamber is obtained from a full residue flag, and a lifted adapted basis carries it to the standard chain. Thus \(G\) has finitely many simplex orbits. Two coordinate vertices are adjacent precisely when the spread of their coordinate difference is at most one: one can then translate all its entries into \(\{0,1\}\). Pairwise adjacent vertices form a chain by ordering their corresponding residue subspaces.

**Lemma 6.48 — compact averages and the face identity.** Fix \(m\ge1\). For a vertex \(x=[L]\), put
\[
 \begin{aligned}
 U_x&=1+\varpi_F^m\operatorname{End}_{\mathcal O_D}(L),\\
 e_x&=\frac{1_{U_x}}{\operatorname{vol}(U_x)},\\
 U_\sigma&=\prod_{y\in\sigma^0}U_y,\qquad
 e_\sigma=\prod_{y\in\sigma^0}e_y.
 \end{aligned}
\tag{6.115}
\]
Endomorphisms here are \(D\)-linear endomorphisms preserving \(L\). These definitions are independent of homothety and equivariant under \(G\). The vertex groups in a simplex mutually normalize, their product is a compact open subgroup, and \(e_\sigma\) is its probability average. In particular \(e_\sigma V=\bigcap_{y\in\sigma^0}V^{U_y}\). If \(z\) is adjacent to every vertex of \(\tau\) and \(z\in H(x,\tau)\), then
\[
 \begin{aligned}
 e_z e_\tau e_x&=e_\tau e_x,\\
 e_x e_\tau e_z&=e_x e_\tau,\\
 \tau\preceq\sigma\subset H(x,\tau)
 &\ \Longrightarrow\ e_xe_\sigma=e_xe_\tau.
 \end{aligned}
\tag{6.116}
\]
The reverse-order version of the last identity holds as well.

**Proof.** A \(D\)-linear map preserves \(L\Pi^a\) exactly when it preserves \(L\), which proves homothety independence; geometric series prove that the displayed sets are groups. At adjacent vertices, normalize one lattice to \(\mathcal O_D^r\) and the other to exponents in \(\{0,1\}\). Since \(dm\ge1\), each congruence group fixes the other lattice. Each therefore normalizes the other's endomorphism order and congruence group. The product of mutually normalizing compact subgroups is a compact subgroup. The convolution of their probability measures is its invariant probability measure, in either order: invariance under each generating subgroup proves this assertion. The range is their common fixed space.

For the face assertion choose a common apartment and normalize \(x\) to zero. If \(a^y\) are the coordinates of the vertices of \(\tau\), and \(b\) those of \(z\), (6.113) implies
\(b_i-b_j\ge\min(0,\min_{y\in\tau^0}(a_i^y-a_j^y))\).
Gaussian elimination after conjugating the standard congruence group shows that \(U_z\) is generated by diagonal units \(1+\varpi_F^m\mathcal O_D\) and root transvections with entry valuation at least \(dm+b_i-b_j\). To see that there is no generation assumption here, eliminate a near-identity matrix in the standard order using its unit diagonal pivots. The remaining diagonal matrix still has diagonal entries congruent to one modulo \(\varpi_F^m\); conjugate the resulting finite factorization back.

Every root generator so obtained lies either in \(U_x\cap U_z\) or in \(U_y\cap U_z\) for some vertex \(y\) of \(\tau\). Diagonal generators lie in all these groups. Since \(U_z\) normalizes \(U_\tau\), so does \(U_x\cap U_z\). Reordering the finite generator word therefore writes each element of \(U_z\) as \(u_\tau u_x\), with \(u_\tau\in U_\tau\), \(u_x\in U_x\cap U_z\). It fixes \(e_\tau e_xv\): commute \(u_x\) past the \(U_\tau\)-average and use \(u_xe_x=e_x\). Averaging over \(U_z\) proves the first identity. Inversion of group measures reverses convolution and fixes every subgroup probability measure; since \(e_z\) commutes with \(e_\tau\), it proves the second. Apply that second identity successively to the vertices of \(\sigma\) to obtain the final assertion. All multiplication and elimination arguments are valid over noncommutative \(D\). \(\square\)

**Lemma 6.49 — face intervals towards a vertex.** For a fixed vertex \(x\) and any simplex \(\sigma\), there is a unique smallest nonempty face \(m_x(\sigma)\) such that \(\sigma\subset H(x,m_x(\sigma))\). For a finite convex subcomplex \(\Sigma\) containing \(x\), every nonempty fibre of \(m_x\) is an interval of faces \([\tau,\omega]\). Its alternating sum is zero unless \(\tau=\omega=x\), when it is one.

**Proof.** Handle \(\sigma=\{x\}\) first: its minimal nonempty face is itself. Otherwise choose an apartment for \(x,\sigma\). Choose a chamber \(\Delta\) containing \(\sigma\) whose local cone at an interior point of \(\sigma\) contains the direction towards \(x\). This is possible by taking the simplex traversed by a sufficiently short initial segment in that direction and extending it to a chamber. Write its affine simple roots as \(a_0,\ldots,a_{r-1}\), normalized by \(\sum a_j=1\). In type \(A\), they can be written, after ordering coordinates, as successive coordinate differences and \(1-a_1-\cdots-a_{r-1}\). They are integer-valued at vertices. The chamber choice gives \(a_j(x)\ge0\) whenever \(a_j\) vanishes on \(\sigma\). Set
\[
 I=\{j:a_j|_\sigma=0\text{ or }a_j(x)>0\},
 \qquad \tau=\Delta\cap\bigcap_{j\in I}\{a_j=0\}.
\tag{6.117}
\]
This is a nonempty face of \(\sigma\). Indeed \(I\) cannot contain every index. If \(\sigma\) has positive dimension, at least two of its simple coordinates are nonzero, and positivity of both integer values at \(x\) would contradict \(\sum a_j(x)=1\); the other values in \(I\) are nonnegative. If \(\sigma\) is a vertex, the same sum would force \(x=\sigma\), the case already handled.

If a face \(\eta\) of \(\sigma\) fails to contain \(\tau\), some \(j\notin I\) vanishes on \(\eta\). Then \(a_j(x)\le0\) while \(a_j\) is positive in the interior of \(\sigma\); its wall excludes \(\sigma\) from \(H(x,\eta)\). Conversely, consider any affine root \(\beta\) nonnegative on \(x\) and \(\tau\). A root has constant sign in the interior of a simplex. Thus it is nonnegative on \(\sigma\) unless it vanishes on \(\tau\) but not on \(\sigma\). Write \(\beta=\sum\lambda_j a_j\) with coefficients all nonnegative or all nonpositive. This elementary type-\(A\) root description follows by writing a coordinate difference as a consecutive sum of simple roots, adding full cycles for its integer constant, or taking the negative of such an expression. Vanishing on \(\tau\) forces \(\lambda_j=0\) for \(j\notin I\). Some nonzero coefficient has \(a_j|_\sigma\ne0\), hence \(a_j(x)>0\); every other \(a_j(x)\) in \(I\) is nonnegative. The inequality \(\beta(x)\ge0\) therefore rules out all coefficients being nonpositive. Hence \(\beta\ge0\) on \(\sigma\). Formula (6.113), equivalently the affine-root half-apartment description, proves \(\sigma\subset H(x,\tau)\). This proves the claimed minimality and uniqueness.

Next, the cofaces of any \(\tau\) contained in \(H(x,\tau)\) have a unique largest member \(\omega\). They all lie in one common apartment. If two did not span a simplex, an affine wall through \(\tau\) would place their interiors on opposite sides: in the coordinate-wall subdivision, compatible wall signs are exactly faces of one chamber. The enclosure lies on the side containing \(x\), or in the wall if \(x\) lies there, giving a contradiction. Their union consequently spans a simplex; there are finitely many cofaces at \(\tau\), so their total span is \(\omega\).

If \(m_x(\tau)=\tau\ne x\), this maximum strictly contains \(\tau\). Follow the segment from \(x\) to an interior point of \(\tau\). If its final short part is outside \(\tau\), its carrier is already a larger coface in \(H(x,\tau)\). If its final part is in \(\tau\), prolong it to a proper boundary face \(\eta\). The enclosure \(H(x,\eta)\) contains the segment and hence an interior point of \(\tau\); being a subcomplex, it contains all of \(\tau\), contrary to minimality. Convexity puts \(\omega\) in \(\Sigma\). Minimality is idempotent, and gives
\[
 \begin{aligned}
 \{\sigma\in\Sigma:m_x(\sigma)=\tau\}&=[\tau,\omega],\\
 \sum_{\tau\preceq\sigma\preceq\omega}(-1)^{\dim\sigma}
 &=(-1)^{\dim\tau}(1-1)^{|\omega^0\setminus\tau^0|}.
 \end{aligned}
\tag{6.118}
\]
The only singleton interval is \(\tau=\omega=x\); here its sum is one. This also proves the assertion in rank one directly. \(\square\)

**Theorem 6.50 — the finite support projection.** For every smooth \(V\) and finite convex \(\Sigma\), the finite operator
\[
 u_\Sigma=\sum_{\sigma\in\Sigma}(-1)^{\dim\sigma}e_\sigma
\tag{6.119}
\]
is an idempotent with
\[
 \begin{aligned}
 \operatorname{im}u_\Sigma&=\sum_{x\in\Sigma^0}V^{U_x},\\
 \ker u_\Sigma&=\bigcap_{x\in\Sigma^0}\ker e_x,\\
 e_xu_\Sigma&=u_\Sigma e_x=e_x\quad(x\in\Sigma^0).
 \end{aligned}
\tag{6.120}
\]
It has finite rank when \(V\) is admissible, and \(\pi(g)u_\Sigma\pi(g)^{-1}=u_{g\Sigma}\). If \(\Sigma_+,\Sigma_-\), their union \(\Sigma\), and their intersection \(\Sigma_0\) are finite convex subcomplexes, then, with the zero operator for an empty intersection,
\[
 \begin{aligned}
 u_{\Sigma_+}u_{\Sigma_-}&=u_{\Sigma_-}u_{\Sigma_+}=u_{\Sigma_0},\\
 \operatorname{im}u_{\Sigma_+}\cap\operatorname{im}u_{\Sigma_-}
       &=\operatorname{im}u_{\Sigma_0}.
 \end{aligned}
\tag{6.121}
\]

**Proof.** Fix \(x\in\Sigma^0\) and group the terms of \(e_xu_\Sigma\) by \(\tau=m_x(\sigma)\). Lemma 6.48 gives \(e_xe_\sigma=e_xe_\tau\) throughout a fibre. Lemma 6.49 cancels every fibre except the vertex \(x\), whose contribution is \(e_x\). Reverse all convolution products to obtain \(u_\Sigma e_x=e_x\). Since each \(e_\sigma\) is a product of vertex idempotents, \(u_\Sigma^2=u_\Sigma\) follows term by term. Its image is contained in the indicated sum and it is the identity on that sum. Every vector in the indicated intersection of kernels is killed term by term, while \(u_\Sigma v=0\) implies \(e_xv=e_xu_\Sigma v=0\). This proves (6.120). Admissibility makes the finite sum of fixed spaces finite-dimensional; equivariance follows from (6.115).

For a nested pair, the image and kernel descriptions give \(u_0u_+=u_+u_0=u_0\), and likewise for the minus sign. Inclusion and exclusion of cells gives \(u_\Sigma=u_++u_--u_0\). Put \(P=u_+-u_0\), \(Q=u_--u_0\). These are idempotents and \(P+Q=u_\Sigma-u_0\) is idempotent. Hence \(PQ+QP=0\). Multiplication by \(P\) on both sides gives \(2PQP=0\); multiplication on just the left or right then gives \(PQ=QP=0\). Our coefficients are complex, so division by two is legitimate even when \(F\) has characteristic two. Expanding proves (6.121). \(\square\)

**Proposition 6.51 — cofinal finite convex subcomplexes.** Let \(L\) represent a base vertex and put \(K_l=1+\varpi_F^l\operatorname{End}_{\mathcal O_D}(L)\), \(l\ge1\). The full subcomplex \(\Sigma_l\) on its fixed vertices is finite and convex, and these subcomplexes exhaust the building. In an apartment obtained by elementary divisors relative to \(L\), its fixed vertices satisfy exactly
\[
 \max_i a_i-\min_i a_i\le dl.
\tag{6.122}
\]
There is also such an exhaustion invariant under the stabilizer of any fixed simplex. If \(V\) is irreducible smooth and \(V^{U_x}\ne0\) for one vertex at the chosen \(m\), then \(u_{\Sigma_l}v=v\) for all sufficiently large \(l\), for each \(v\in V\).

**Proof.** The group \(K_l\) is normal in the integral base stabilizer, so elementary divisors reduce the fixed-vertex question to diagonal lattices. Its root entries have valuation at least \(dl\); preservation of \(L(a)\) is equivalent to \(dl\ge a_i-a_j\) for every pair. Fixing the class is the same as preserving the actual lattice here, since \(|\operatorname{Nrd}(k)|=1\) for \(k\in K_l\): a nonzero homothety shift changes lattice covolume. This proves (6.122). Normalize \(\min a_i=0\). Only finitely many exponent tuples remain; each has finite orbit under the compact integral stabilizer, because its stabilizer is open. Thus there are finitely many vertices and, by local finiteness, finitely many simplices. Every element of \(K_l\) preserving the vertices of \(x,\tau\) fixes their enclosure by Lemma 6.47; hence the fixed subcomplex is convex. Every finite set of lattices is preserved by all sufficiently small \(K_l\), proving exhaustion.

For a simplex \(\eta\), use the order \(A_\eta=\bigcap_{y\in\eta^0}\operatorname{End}_{\mathcal O_D}(L_y)\). Its full stabilizer permutes these orders, including when it permutes the vertices, so normalizes \(1+\varpi_F^l A_\eta\). These groups contain sufficiently small base congruence groups and have reduced norm of absolute value one. The same argument proves finiteness, convexity, exhaustion and stabilizer invariance. Finally all vertices are \(G\)-conjugate; the sum of all \(V^{U_y}\) is a nonzero invariant subspace and thus equals \(V\). Every vector is a finite sum from these fixed spaces. A sufficiently large \(\Sigma_l\) contains those vertices, and (6.120) fixes that vector. \(\square\)

**Proposition 6.52 — finite elliptic fixed simplices.** Every element with compact cyclic closure modulo \(Z\) stabilizes a simplex. On a compact subset \(B\) of the elliptic regular set there are only finitely many simplices stabilized by any element of \(B\). For an admissible smooth \(V\), the finite expression
\[
 L_{V,m}(g)=\sum_{g\sigma=\sigma}(-1)^{\dim\sigma}
       \operatorname{sgn}(g|\sigma^0)
       \operatorname{tr}(\pi(g)|V^{U_\sigma})
\tag{6.123}
\]
is locally constant on the elliptic regular set. The permutation sign is essential even if a stabilized simplex has no fixed vertex.

**Proof: existence of a stabilized simplex.** Lemma 6.39 supplies a common slope \(\nu\), an integer \(e\) with \(e\nu=a\in\mathbb Z\), and a lattice \(L\) preserved by \(u=\varpi_F^{-a}g^e\). Let \(\alpha_L\) be the minimum coordinate valuation in a lattice basis and define
\[
 \begin{aligned}
 \alpha(v)&=\min_{0\le j<e}
       \bigl(\alpha_L(g^jv)-jd\nu\bigr),\\
 \Lambda_t&=\{v:\alpha(v)\ge t\}.
 \end{aligned}
\tag{6.124}
\]
Both \(u\) and its inverse preserve every \(L\Pi^n\). Shifting the index in the minimum, and using \(\alpha_L(g^ev)=\alpha_L(v)+ed\nu\), gives \(\alpha(gv)=\alpha(v)+d\nu\). Also \(\alpha(vb)=\alpha(v)+v_D(b)\) and \(\alpha(v+w)\ge\min(\alpha(v),\alpha(w))\). Each \(\Lambda_t\) is a finite intersection of full lattices and is therefore a full lattice; \(\Lambda_{t+1}=\Lambda_t\Pi\). The finitely many jumps in a period give a periodic lattice chain, with at most \(r\) strict steps since its residue flags lie in an \(r\)-dimensional space. Translation of \(t\) by \(d\nu\) permutes its lattice classes. Their simplex is stabilized by \(g\).

**Proof: uniform finiteness.** A vertex stabilizer is compact modulo \(Z\): an element takes \(L\) to \(L\Pi^k\); there are only \(d\) possible shifts modulo central \(\varpi_F\), and each shift is a coset of the compact actual-lattice stabilizer. A simplex stabilizer \(C_\eta\) has a finite permutation action on its vertices, with kernel in a vertex stabilizer. It too is compact modulo \(Z\), and it is open. Choose representatives \(\eta\) for the finitely many simplex types. If \(x\in B\) stabilizes \(h\eta\), then \(h^{-1}xh\in C_\eta\). The absolute reduced norms of \(B\) stay in a compact annulus. The part of \(C_\eta\) in this annulus is an actual compact set: take compact representatives modulo \(Z\) and bound the central valuation using \(|\operatorname{Nrd}(z)|=|z|^{rd}\). Lemma 6.18, specifically its uniform elliptic assertion (6.39), now puts all such \(hZ\) in a compact subset of \(G/Z\). Its image in the discrete space \(G/C_\eta\) is finite. There are therefore only finitely many possible \(h\eta\), uniformly for \(x\in B\).

**Proof: local constancy.** Around an elliptic regular \(g\), choose a compact open neighbourhood \(B\) contained in that set; its openness was proved in the local charts of Theorem 6.7. Let \(S\) be the finite set of simplices just obtained. Choose an open subgroup \(H\) fixing all their vertices. For \(h\in H\) with \(gh\in B\), a simplex is stabilized by \(gh\) exactly when it is stabilized by \(g\), and its vertex permutation is the same. Shrink \(H\) further to fix a basis of each of the finitely many spaces \(V^{U_\sigma}\), \(\sigma\in S\). This is possible by smoothness and admissibility. The restrictions of \(\pi(gh)\) and \(\pi(g)\) on every stabilized fixed space then agree. All terms in (6.123) are constant on this neighbourhood. \(\square\)

**Example 6.53 — an enclosure and a face that cannot be replaced by a vertex.** In a rank-three apartment the enclosure of \((0,0,0)\) and \((3,1,0)\) has vertices
\[
 \begin{gathered}
 (0,0,0),\ (1,0,0),\ (2,0,0),\\
 (1,1,0),\ (2,1,0),\ (3,1,0).
 \end{gathered}
\tag{6.125}
\]
These are exactly the solutions of \(0\le b_1\le3\), \(0\le b_2\le1\), \(0\le b_1-b_2\le2\), with \(b_3=0\). The support projection is the sum of their six vertex averages minus the edge averages plus the triangle averages, with edges determined by spread at most one. The cancellation in Lemma 6.49 computes the projector without requiring distant vertex averages to commute.

For rank four put \(x=(0,0,0,0)\), \(y=(4,2,2,0)\), and
\[
 \begin{gathered}
 z_1=(4,2,1,0),\quad z_2=(4,3,2,0),\\
 y\in H(x,[z_1,z_2]),\\
 y\notin H(x,z_1)\cup H(x,z_2).
 \end{gathered}
\tag{6.126}
\]
The two \(z\)'s are adjacent because their difference has spread one. Checking the six coordinate differences in (6.113) puts \(y\) in the face enclosure. But \(y_3-y_4=2\) exceeds the bound one from \(x,z_1\), while \(y_1-y_2=2\) exceeds the bound one from \(x,z_2\). Thus a face enclosure cannot in general be reduced to one of its vertex enclosures. Lemma 6.48 proves precisely the face identity needed in (6.119).

Theorem 6.50 describes the image and kernel of the support operator. The global cellular exactness is Theorem 6.56, and the finite convex assertion at \(dm\ge2\) is Theorem 6.63. The finite trace formula and Theorem 6.65 identify (6.123) with the actual character on the elliptic regular set; Theorems 6.69–6.70 supply stabilized finite traces and the character on the entire regular semisimple set. The freely available Meyer–Solleveld paper, §§2.3–2.5 and Proposition 4.1, treats support projections and character traces separately. The lattice enclosure, face consistency, support projection, exhaustion and elliptic finiteness used in this subsection have been proved above.


### 6.12. Global cellular resolutions and Euler–Poincaré tests

Keep the groups \(U_x,U_\sigma\) of (6.115), at one fixed depth \(m\ge1\), and denote the lattice building by \(\mathcal B\). Orient its simplices. For a smooth complex representation \(V\), put
\[
 \begin{aligned}
 C_q(\mathcal B,V)&=\bigoplus_{\dim\sigma=q}
          \mathbb C[\sigma]\otimes V^{U_\sigma},\\
 \partial([\sigma]\otimes v)&=
       \sum_{\eta\prec\sigma}[\sigma:\eta][\eta]\otimes v.
 \end{aligned}
\tag{6.127}
\]
The sum in the boundary is over codimension-one faces, with their incidence signs. Opposite orientations negate \([\sigma]\). Face inclusions of the fixed spaces make this well defined. Cancellation of the two orders of deleting vertices proves \(\partial^2=0\). The augmentation in degree zero sends \([x]\otimes v\) to \(v\). We prove global exactness and construct actual trace tests. We do not assume a regular-character theorem in doing so.

**Lemma 6.54 — a scalar contraction with enclosure support.** Fix a vertex \(o\) and let \(K_0\) be its compact actual-lattice stabilizer. The augmented scalar complex \(C_*(\mathcal B,\mathbb C)\to\mathbb C\) has a \(K_0\)-equivariant contraction \(h\) such that \(h_{-1}(1)=[o]\) and
\[
 \begin{gathered}
 \partial h+h\partial=1,\\
 \operatorname{supp}h([\sigma])\subset H(o,\sigma).
 \end{gathered}
\tag{6.128}
\]
Every individual image is a finite chain. No uniform bound on its size is asserted.

**Proof: scalar exactness inside an apartment.** A finite root-convex subcomplex \(P\) of an apartment has an exact augmented scalar complex. Here is a direct proof. If \(P\) is a simplex, prepend a fixed vertex to an oriented face not already containing it, with the sign given by that ordering, and send a face containing it to zero. The two boundary expansions give a contraction. Otherwise some affine root wall separates two points of \(P\) strictly. Indeed, if no wall did, the interior wall signs of all its cells would be compatible, placing them in one simplex; convexity and fullness would then make \(P\) a face. The two closed half-polytopes \(P_+,P_-\) and their intersection \(P_0\) are nonempty proper root-convex subcomplexes. Each has fewer cells. Degree by degree their augmented complexes have the exact sequence given by the maps \(c\mapsto(c,-c)\) and \((a,b)\mapsto a+b\).

For clarity, exactness passes across this sequence without a topological theorem. Lift a cycle in \(P\) to \(a+b\). The boundaries of \(a,b\) are opposite copies of a cycle in \(P_0\). Fill that cycle there, subtract its filling from \(a\) and add it to \(b\); the two resulting cycles fill in \(P_+,P_-\). The same argument in degree zero uses the augmentation on \(P_0\), which is onto. Their fillings add to a filling of the original cycle. Induction on the number of cells proves the assertion. These cuts take place only in the single apartment. By Lemma 6.47 they apply in particular to every finite enclosure \(H(o,\sigma)\).

**Proof: equivariant construction.** Suppose \(h\) has been defined in lower degrees, beginning with \(h_{-1}\). For an oriented \(q\)-simplex \(\sigma\), the finite chain \([\sigma]-h\partial[\sigma]\) is a cycle in \(H(o,\sigma)\): the induction identity proves that its boundary is zero, and every face enclosure is contained in that enclosure. Fill it there by the preceding paragraph. Average a filling over the compact stabilizer of the underlying simplex in \(K_0\), multiplying by its orientation character in this average. That stabilizer preserves the finite enclosure, so the average is a finite linear combination and its boundary is still the required cycle. The averaged filling has exactly the orientation equivariance needed to extend it to the \(K_0\)-orbit of \(\sigma\). Choose one representative per orbit and continue in degree. This constructs (6.128). It also constructs a map on constant chains with coefficients in any complex vector space by tensoring with the identity. \(\square\)

**Lemma 6.55 — the invariant-chain contraction.** Put \(K=U_o\). The contraction of Lemma 6.54, tensored with the identity of \(V\), preserves
\[
 C_*(\mathcal B,V)^K\longrightarrow V^K
\tag{6.129}
\]
and contracts this augmented complex, naturally in every smooth \(V\).

**Proof: the matrix factorization needed for averaging.** For simplices \(\sigma\) and \(\tau\subset H(o,\sigma)\), let \(K_\tau\) be the subgroup of \(K\) fixing the vertices of \(\tau\). We claim
\[
 U_\tau\subset K_\tau U_\sigma.
\tag{6.130}
\]
Choose a common apartment with \(o=\mathcal O_D^r\). Order its coordinates so that \(a_1^y\ge\cdots\ge a_r^y\) at every vertex \(y\) of \(\sigma\). Such an ordering exists because a simplex does not cross a coordinate wall through \(o\). For a simplex \(\eta\), define
\[
 c_{ij}(\eta)=\min_{y\in\eta^0}(a_i^y-a_j^y),
 \qquad q_{ij}(\eta)=dm+c_{ij}(\eta)\quad(i\ne j).
\tag{6.131}
\]
The group \(U_\eta\) has a Gaussian factorization, in the order upper triangular, diagonal, lower triangular, whose root entries have thresholds \(q_{ij}(\eta)\) and whose diagonal entries belong to \(1+\varpi_F^m\mathcal O_D\). We verify this also for a face, rather than only a vertex. A root difference on a simplex has integer vertex values differing by at most one. Equivalently, its minimum is the floor of its value at an interior point. Thus
\(c_{ij}+c_{jk}\ge c_{ik}-1\) and \(c_{ij}+c_{ji}\ge-1\). Since \(dm\ge1\), elimination preserves all the off-diagonal thresholds, and every diagonal correction has valuation at least \(dm\). Conjugating one vertex lattice to the standard lattice makes all off-diagonal thresholds nonnegative; their zero-threshold positions are strictly triangular after ordering the residue flag. Matrices in question are therefore invertible, with unit pivots congruent to one modulo \(\varpi_F^m\). Elimination gives the stated factors and their inverses. Each root threshold is attained at a vertex of \(\eta\), so each such root factor belongs to one of the vertex groups. Conversely every vertex group satisfies these thresholds. This proves that the factored group is exactly their product \(U_\eta\).

By (6.113), the coordinates of \(\tau\) have the same weak ordering. Its upper root factors have entry valuation at least \(dm\), so belong to \(K\). They preserve every lattice in \(\tau\), since \(dm+c_{ij}(\tau)\ge\max_{y\in\tau^0}(a_i^y-a_j^y)\). Thus the entire upper factor belongs to \(K_\tau\). For a lower root, (6.113) gives \(c_{ij}(\tau)\ge c_{ij}(\sigma)\), because the latter is nonpositive. Consequently the lower factor belongs to \(U_\sigma\), as does the diagonal factor. This proves (6.130), including over noncommutative \(D\).

**Proof: coefficients after averaging.** The group \(K_\tau\) normalizes \(U_\tau\). If \(v\in V^{U_\sigma}\), (6.130) gives
\[
 \begin{aligned}
 e_{K_\tau}\pi(u)v&=e_{K_\tau}v\quad(u\in U_\tau),\\
 e_{K_\tau}v&=e_{K_\tau}e_\tau v\\
            &=e_\tau e_{K_\tau}v\in V^{U_\tau}.
 \end{aligned}
\tag{6.132}
\]
Here every \(e_H\) is the invariant probability average, so there is no index or volume factor missing in this identity.

Every invariant chain is a sum of vectors \(e_K([\sigma]\otimes v)\). Apply the scalar \(h\) to this expression. Its \(K\)-equivariance writes the result as the \(K\)-average of finitely many terms \([\tau]\otimes v\), with \(\tau\subset H(o,\sigma)\). At an image cell \(k\tau\), the coefficient of such a term is the appropriate orbit-mass scalar times \(\pi(k)e_{K_\tau}v\), with its orientation sign. Formula (6.132) puts this coefficient in \(V^{U_{k\tau}}\).

One may use the vertex-fixing stabilizer in this orbit computation. Indeed \(K\) preserves the type given by lattice covolume modulo \(r\); the vertices of a simplex have distinct types. Thus a member of \(K\) stabilizing the simplex fixes all its vertices and its orientation. All orbit averages are finite, since a compact group has finite orbit on a discrete cell set. This proves preservation of (6.129). Identity (6.128) now proves contraction there, and \(h_{-1}v=[o]\otimes v\) is allowed because \(V^K=V^{U_o}\). The construction commutes with equivariant maps of \(V\). \(\square\)

**Theorem 6.56 — exactness on the whole division-lattice building.** Define
\[
 \begin{gathered}
 \Phi_m(V)=\sum_{x\in\mathcal B^0}V^{U_x},\\
 0\longrightarrow C_{r-1}(\mathcal B,V)\longrightarrow\cdots
 \longrightarrow C_0(\mathcal B,V)\longrightarrow\Phi_m(V)
 \longrightarrow0.
 \end{gathered}
\tag{6.133}
\]
The functor \(\Phi_m\) on smooth representations is exact, and the displayed augmented complex is exact. In particular it resolves every \(V\) generated by \(V^{U_o}\). Every finitely generated smooth representation has this property for sufficiently large \(m\).

**Proof: the exact functor.** For an invariant subspace \(W\subset V\),
\[
 \Phi_m(W)=W\cap\Phi_m(V).
\tag{6.134}
\]
Only the reverse inclusion needs proof. Express a vector in the right side as a finite sum from vertex fixed spaces. Proposition 6.51 supplies a finite convex \(\Sigma\) containing those vertices. Theorem 6.50 gives \(u_\Sigma v=v\). Since \(u_\Sigma\) is a finite expression in group averages, it preserves \(W\) and puts this vector in \(\sum_{x\in\Sigma^0}e_xW\). This proves (6.134). Compact averaging also makes \(V^{U_x}\to(V/W)^{U_x}\) onto: average any lift. Therefore \(\Phi_m\) is exact. The representations equal to their \(\Phi_m\) are closed under subobjects, quotients and extensions; the extension assertion follows immediately by lifting the quotient's generated vectors and applying (6.134) to the kernel.

**Proof: invariant homology detects all homology.** The complex (6.133) is a smooth \(G\)-complex. Each elementary tensor in a cell summand is fixed by \(U_x\) for any vertex of that cell: this group fixes the cell pointwise as well as its coefficient. All vertices are \(G\)-conjugate, so every chain module is generated by its \(K=U_o\)-fixed vectors. Hence its homology, a subquotient, also equals its \(\Phi_m\), by the preceding paragraph. Taking \(K\)-fixed vectors is exact by compact averaging, and commutes with homology: average a primitive of an invariant boundary to make it invariant. Lemma 6.55 shows that the invariant augmented complex is contractible. All augmented homology groups therefore have zero \(K\)-fixed space. A representation generated by such a space is zero. This proves exactness in every degree, including the kernel of augmentation. Finally finitely many smooth generators are fixed by one sufficiently small base congruence group \(U_o\); their \(G\)-span is then generated by \(V^{U_o}\). \(\square\)

Theorem 6.56 concerns the full building. Its proof does not assert exactness for an arbitrary finite convex subcomplex: such a subcomplex need not be preserved by the vertex averages used to detect homology. The scalar assertion inside an apartment in Lemma 6.54 and the global coefficient assertion have different proofs. The finite convex assertion at \(dm\ge2\), used for the trace application, is Theorem 6.63.

**Theorem 6.57 — projectivity with a fixed central character.** Let \(V\) be smooth admissible with smooth central character \(\omega\), and choose \(m\) such that \(V=\Phi_m(V)\). For a simplex \(\sigma\), write \(C_\sigma=\{g:g\sigma=\sigma\}\), let \(\epsilon_\sigma\) be its vertex-permutation sign, and put \(\rho_\sigma=\epsilon_\sigma\otimes V^{U_\sigma}\). In the category of smooth representations with central character \(\omega\), (6.133) is a projective resolution with
\[
 C_q(\mathcal B,V)=\bigoplus_{[\sigma],\,\dim\sigma=q}
              \operatorname{c\!-!Ind}_{C_\sigma}^{G}\rho_\sigma.
\tag{6.135}
\]
There are finitely many summands. For any smooth admissible \(W\) with that central character, all \(\operatorname{Ext}^q_{G,\omega}(V,W)\) are finite-dimensional and vanish for \(q\ge r\).

**Proof.** The simplex stabilizer is open and compact modulo \(Z\) by Proposition 6.52. Its action on a cell summand is exactly \(\rho_\sigma\); the orientation factor records the action on \([\sigma]\). Decomposing finitely supported chains into their finitely many \(G\)-orbits proves (6.135). The fixed spaces are finite-dimensional by admissibility.

Every finite-dimensional smooth \(C_\sigma\)-representation \(\rho\) with character \(\omega\) is projective in the fixed-central-character category. Indeed, lift a linear map from \(\rho\) through a surjection, then average the lift by \(c\mapsto\pi(c)A\rho(c^{-1})\) over \(C_\sigma/Z\). Central scalars cancel. Smoothness of finitely many images makes this a finite locally constant average on that compact quotient. Its image is an equivariant lift, since normalized Haar averaging is invariant. This proves exactness of \(\operatorname{Hom}_{C_\sigma}(\rho,-)\). The compact-induction adjunction is explicit here: prescribe the image of the function supported on \(C_\sigma\), then translate it and add over the finite support in \(G/C_\sigma\). It gives
\(\operatorname{Hom}_G(\operatorname{c\!-!Ind}_{C_\sigma}^G\rho,W)=\operatorname{Hom}_{C_\sigma}(\rho,W)\), so proves projectivity of each summand.

These Hom spaces are finite-dimensional for admissible \(W\). Choose an open normal subgroup of \(C_\sigma\) fixing \(\rho\) pointwise; its common fixed space in \(W\) is finite-dimensional. Such a subgroup exists by intersecting the stabilizers of a basis and then their finitely many conjugates modulo \(Z\). Taking it compact and sufficiently small does not affect this conclusion. The Hom space embeds into the maps from \(\rho\) to that fixed space. Apply \(\operatorname{Hom}_G(-,W)\) to the finite projective resolution. Its cohomology computes the stated Ext groups and proves both assertions. Independence of the resolution follows directly by lifting comparison maps degree by degree through the surjections onto cycles; lifting their differences in the same way gives a chain homotopy. This is also the usual projective-resolution definition of Ext. \(\square\)

**Corollary 6.58 — an actual Euler–Poincaré trace test.** Use compatible Haar measures on \(G\), \(Z\), and \(G/Z\). The function
\[
 f_{V,m}(g)=\sum_{[\sigma]}(-1)^{\dim\sigma}
   \frac{1_{C_\sigma}(g)}{\operatorname{vol}(C_\sigma/Z)}
                       \operatorname{tr}\rho_\sigma(g^{-1})
\tag{6.136}
\]
is smooth, compactly supported modulo \(Z\), and satisfies \(f_{V,m}(zg)=\omega(z)^{-1}f_{V,m}(g)\). For every smooth admissible \(W\) of central character \(\omega\), its finite-rank integrated action satisfies
\[
 \begin{aligned}
 \operatorname{tr}\pi_W(f_{V,m})
 &=\sum_q(-1)^q\dim\operatorname{Ext}_{G,\omega}^q(V,W),\\
 \pi_W(f)&=\int_{G/Z}f(g)\pi_W(g)\,d\bar g.
 \end{aligned}
\tag{6.137}
\]
No unitarity of \(\omega\) or complex conjugation of a character is needed in this formula.

**Proof.** Smoothness and central covariance follow term by term. A finite-dimensional smooth \(\rho_\sigma\) has an open kernel; its character on \(C_\sigma\) is invariant on both sides by a sufficiently small compact open subgroup. Intersect those groups over the finitely many summands. Thus the integrated operator has image in one admissible fixed space and finite rank. For one summand, choose a compact open normal subgroup \(J\) of \(C_\sigma\) acting trivially on \(\rho_\sigma\), as in Theorem 6.57, and work in the finite-dimensional \(C_\sigma\)-invariant space \(W^J\). On \(\operatorname{Hom}_{\mathbb C}(\rho_\sigma,W^J)\) the normalized operator
\(A\mapsto\int_{C_\sigma/Z}\pi_W(c)A\rho_\sigma(c^{-1})\,d\bar c/\operatorname{vol}(C_\sigma/Z)\)
is the projection onto its equivariant maps. Its trace is their dimension. The trace of each integrand is \(\operatorname{tr}\pi_W(c)\operatorname{tr}\rho_\sigma(c^{-1})\) on that finite space; hence the corresponding summand of (6.136) has trace \(\dim\operatorname{Hom}_{C_\sigma}(\rho_\sigma,W)\). The same summand equals its composition with \(e_J\), so this finite-space trace is its trace on \(W\). The alternating sum is the Euler characteristic of the finite Hom complex in Theorem 6.57. For any finite complex this is the Euler characteristic of its cohomology: in each degree split off boundaries and a complement of cycles; the differential identifies the latter with the next boundaries, whose two contributions cancel. This proves (6.137). \(\square\)

**Proposition 6.59 — elliptic orbital integrals of the trace test.** For elliptic regular \(\gamma\), normalize \(T=G_\gamma\) as in Section 6.3, with \(\operatorname{vol}(T/Z)=1\). Then the absolutely convergent orbital integral is
\[
 O_\gamma(f_{V,m})=L_{V,m}(\gamma^{-1}).
\tag{6.138}
\]
For every regular \(\gamma\) with noncompact cyclic closure modulo \(Z\), this orbital integral is zero. These are assertions about the test function, not an identification of \(L_{V,m}\) with the character of \(V\).

**Proof.** All conjugates of \(\gamma\) in the support of (6.136) have its fixed absolute reduced norm. The compact-annulus argument of Lemma 6.18 turns that part of the support into an actual compact target. Proper regular orbital coordinates from the same lemma prove absolute convergence. For a fixed simplex representative \(\sigma\), the contributing double cosets \(ThC_\sigma\) correspond precisely to \(T\)-orbits of simplices \(\kappa=h\sigma\) stabilized by \(\gamma\). This is a finite set by Proposition 6.52. On such a double coset the character factor is constant, by conjugacy invariance in \(C_\sigma\), and quotient Haar integration gives its contribution
\[
 \frac{(-1)^{\dim\kappa}\epsilon_\kappa(\gamma)
              \operatorname{tr}(\pi_V(\gamma^{-1})|V^{U_\kappa})}
      {\operatorname{vol}((T\cap C_\kappa)/Z)}.
\tag{6.139}
\]
Indeed the volume of this double coset in \(T\backslash G\) is \(\operatorname{vol}(C_\sigma/Z)/\operatorname{vol}((T\cap C_\kappa)/Z)\), which cancels the denominator in (6.136). The reciprocal remaining volume is exactly the size of the \(T\)-orbit of \(\kappa\), since \(T/Z\) has volume one. Its finite orbit has the same trace and sign at every simplex. Summing (6.139) over orbits and simplex types gives (6.123), at \(\gamma^{-1}\); inversion leaves its permutation sign unchanged. Finally an element of any \(C_\sigma\) has compact cyclic closure modulo \(Z\). A noncompact-cyclic \(\gamma\) consequently has no conjugate in the support, proving zero there. \(\square\)

**Example 6.60 — an edge stabilized without a fixed vertex.** For \(G=\mathrm{GL}_2(F)\) with \(\operatorname{char}F\ne2\), take
\[
 \gamma=\begin{pmatrix}0&\varpi_F\\1&0\end{pmatrix},
 \qquad \gamma^2=\varpi_F I.
\tag{6.140}
\]
Its Eisenstein polynomial is separable, so it is elliptic regular. It exchanges the vertices represented by \(\mathcal O_F^2\) and \(\varpi_F\mathcal O_F\oplus\mathcal O_F\). Its type shift is odd, so it fixes no vertex. This edge is the only stabilized edge: two distinct fixed midpoints in a tree would force the intervening path, including a vertex, to be fixed. The path assertion follows by uniqueness of the simple path, already proved for the lattice tree in Section 2.3. For the trivial representation, (6.123) consequently gives \((-1)^1(-1)\cdot1=1\), and (6.138) gives \(O_\gamma(f_{1,m})=1\). Omitting the orientation sign would give the wrong value.

Section 6.13 proves the finite cellular trace formula and identifies the finite alternating trace with the actual elliptic character at \(dm\ge2\). Formula (6.138) consequently agrees there with \(\Theta_V(\gamma^{-1})\). Theorems 6.69–6.70 prove the regular-character theorem on compact nonelliptic classes and the entire regular semisimple set. Elliptic character orthogonality and completeness, and the full representation transfer require further arguments. The invariant-chain averaging can be compared with Opdam–Solleveld, Section 2, Theorem 2.2; the enclosure contraction, exact generated-subrepresentation functor and trace-test arguments used here have been supplied explicitly.


### 6.13. Finite convex resolutions and elliptic characters

Choose the level in (6.115) so that \(dm\ge2\). This can always be done while retaining generation of a finitely generated smooth representation. We prove the finite convex statement needed to turn the cellular trace into an actual character on the elliptic regular set, using local lattice intersections.

**Lemma 6.61 — a lattice-height ordering.** Fix a base lattice \(L_o\). Each vertex \(x\) has a unique representative \(L_x\) such that
\[
 \begin{gathered}
 L_o\subset L_x,\qquad L_o\Pi^{-1}\not\subset L_x,\\
 L_x=\bigoplus_i e_i\Pi^{-a_i}\mathcal O_D,\\
 a_i\ge0,\qquad\min_i a_i=0.
 \end{gathered}
\tag{6.141}
\]
The basis in this formula is an \(L_o\)-basis. Define \(i(x)\) to be the decreasing rearrangement of the \(a_i\), with one terminal zero omitted, and order these tuples lexicographically. These coordinates are the negatives of the apartment exponents in (6.112), with homothety normalized as displayed. Distinct adjacent vertices have distinct heights. On any simplex, increasing height orders its canonical lattices into an increasing periodic chain.

Let \(\eta=(x_1,\ldots,x_k)\) be ordered by increasing height and let \(\Sigma\) be a convex subcomplex containing \(o\) and \(\eta\). The finite set
\[
 M_\eta=\{z\in\Sigma^0:\{z\}\cup\eta\text{ is a simplex},
                                    \ i(z)<i(x_1)\}
\tag{6.142}
\]
is stable under intersection of its canonical lattices: if \(z,z'\in M_\eta\), then \(L_z\cap L_{z'}\) represents another member of \(M_\eta\). Its lattice is comparable with each of \(L_z,L_{z'}\), so its vertex is adjacent to each distinct one.

**Proof.** Elementary divisors relative to \(L_o\) prove (6.141), uniqueness and the independence of the sorted tuple from the chosen basis. To compare adjacent \(x,y\), use Lemma 6.47 to put \(o\) and the edge in one apartment. Before normalizing, their coordinate difference can be taken in \(\{0,1\}^r\). Normalizing its minimum to zero either leaves a coordinatewise increase, or subtracts one from every entry and leaves a coordinatewise decrease. A strict coordinatewise increase strictly increases the sorted tuple, and a decrease strictly decreases it. Thus increasing height is exactly increasing inclusion of the canonical lattices for adjacent vertices. The same comparison at every pair of vertices of a simplex gives the increasing periodic chain.

In particular, every vertex \(z\) adjacent to \(x\) with smaller height satisfies
\(L_o+L_x\Pi\subset L_z\subsetneq L_x\). In the displayed coordinates, the first lattice has exponents \(\max(a_i-1,0)\). It strictly contains \(L_x\Pi\), since normalization says \(L_o\not\subset L_x\Pi\).

For \(z,z'\in M_\eta\), it follows that
\[
 L_{x_k}\Pi\subsetneq L_o+L_{x_k}\Pi
 \subset L_z\cap L_{z'}\subsetneq L_{x_1}.
\tag{6.143}
\]
The intersection still contains \(L_o\) and does not contain \(L_o\Pi^{-1}\), so is canonical. It represents a vertex incident to every vertex of \(\eta\), and to \(z,z'\), by the chain inequalities. Its height is at most \(i(z)\): put its incident pair with \(z\) and the base vertex in an apartment and apply the inclusion comparison just proved.

Finally the intersection vertex belongs to \(H(z,z')\). Diagonalize the two actual lattices simultaneously. Their intersection has the coordinatewise maximum of their ordinary lattice exponents. For any two vectors \(a,b\), the difference between two coordinates of \(\max(a,b)\) lies between the corresponding differences for \(a\) and \(b\): the upper bound follows from \(a_i\le a_j+C\), \(b_i\le b_j+C\), and the lower bound follows the same way. Formula (6.113) proves the enclosure assertion. Convexity puts this vertex in \(\Sigma\); (6.143) and its height put it in \(M_\eta\). Local finiteness makes \(M_\eta\) finite. \(\square\)

**Lemma 6.62 — exact local relations.** At \(dm\ge2\), vertex groups associated to two neighbours of the same vertex mutually normalize, so their averages commute. For \(\eta,M_\eta\) as in Lemma 6.61, the following sequence is exact at its middle term, with the usual boundary signs:
\[
 \begin{gathered}
 \bigoplus_{\substack{z,z'\in M_\eta\\\{z,z'\}\text{ an edge}}}
       V^{U_{\{z,z'\}\cup\eta}}\longrightarrow\\
 \bigoplus_{z\in M_\eta}V^{U_{\{z\}\cup\eta}}
 \longrightarrow V^{U_\eta}.
 \end{gathered}
\tag{6.144}
\]
This holds for every smooth complex \(V\).

**Proof: normalization.** Represent two neighbours \(x,y\) of \(t\) by lattices between \(L_t\Pi\) and \(L_t\). Then
\(L_y\Pi\subset L_x\subset L_y\Pi^{-1}\), and conversely. If \(A\) preserves \(L_x\), the inclusion \(L_y\subset L_x\Pi^{-1}\) shows that
\(\varpi_F^m A L_y\subset L_x\Pi^{dm-1}\subset L_y\Pi^{dm-2}\subset L_y\).
Every element of \(U_x\), and its inverse, consequently preserves \(L_y\). It normalizes \(U_y\). The symmetric argument gives mutual normalization and the probability-average argument of Lemma 6.48 gives commutation. All vertices of \(M_\eta\) are neighbours of \(x_1\), so their averages commute with one another and with \(e_\eta\).

**Proof: the relation complex.** Work on \(W=V^{U_\eta}\). Decompose this vector space by the finitely many commuting projections \(e_z\), \(z\in M_\eta\): for a subset \(S\subset M_\eta\), take the image of the product of \(e_z\) for \(z\in S\) and \(1-e_z\) for \(z\notin S\). The products are mutually orthogonal and sum to one. On that image the local middle term is one copy of the image for each \(z\in S\), and the left term has a copy at each edge with both ends in \(S\).

If this image is nonzero and \(z,z'\in S\), their intersection vertex \(w\) from Lemma 6.61 belongs to \(S\). Indeed \(w\in H(z,z')\) and is adjacent to \(z\); (6.116) gives \(e_z e_w e_{z'}=e_z e_{z'}\). Commutativity makes \(e_w\) the identity on the simultaneous image in question. A nonempty \(S\) is therefore closed under finite intersections. Its smallest lattice, the intersection of all its lattices, represents a member of \(S\) adjacent to every other member. The graph on \(S\) is connected. Its edge differences generate precisely the tuples whose sum is zero: subtract along the edges from that smallest vertex to the other vertices. This proves exactness on each simultaneous image. If \(S\) is empty the middle term is zero. Adding the finitely many images proves (6.144). Orienting each \((z,\eta)\) with \(z\) first identifies its last map with this sum; the two relevant faces of \((z,z',\eta)\) give the edge differences. \(\square\)

**Theorem 6.63 — finite convex exactness.** Let \(dm\ge2\) and let \(\Sigma\) be finite convex. Then \(C_*(\Sigma,V)\) has zero homology in positive degrees for every smooth \(V\). If \(V\) is admissible, its augmentation gives an exact finite-dimensional complex
\[
 0\longrightarrow C_{r-1}(\Sigma,V)\longrightarrow\cdots
 \longrightarrow C_0(\Sigma,V)\longrightarrow u_\Sigma V
 \longrightarrow0.
\tag{6.145}
\]

**Proof: eliminating a positive-degree cycle.** Choose \(o\in\Sigma\) and the height of Lemma 6.61. In every simplex, all heights are distinct. For a \(q\)-simplex \(\sigma\), \(q\ge1\), let \(\sigma^-\) be the face obtained by omitting its least-height vertex. Order the height tuples of these faces lexicographically, listing each face's vertices in increasing height. For a finite \(q\)-cycle \(c\), take a largest such face tuple occurring in its support, and fix a face \(\eta\) with that tuple.

The only nonzero components of \(c\) contributing to its boundary at \(\eta\) have the form \(\{z\}\cup\eta\) with \(z\in M_\eta\). Adding a vertex of height larger than the least vertex of \(\eta\) would produce a strictly larger tuple for \(\sigma^-\), whose component is zero by choice. Since \(c\) is a cycle, the remaining components satisfy the last relation of (6.144). Fill this relation by its first term, using \((q+1)\)-simplices \(\{z,z'\}\cup\eta\). They belong to \(\Sigma\), which is full. Subtract their boundary from \(c\). This kills all components with \(\sigma^-=\eta\). Every other affected face contains both \(z,z'\), and hence has strictly smaller tuple for its minus face. Thus it changes no other face at the current maximal tuple and introduces no larger one.

Process the finitely many faces at that tuple and continue downwards. Since \(\Sigma\) is finite, this terminates. The resulting cycle is zero, and the accumulated fillings express the original cycle as a boundary. This proves positive-degree vanishing without a dimension assumption on the fixed spaces.

**Proof: the augmented assertion.** For admissible \(V\), every chain space is finite-dimensional. Theorem 6.50 and its explicit idempotent give
\[
 \dim u_\Sigma V=\operatorname{tr}u_\Sigma
 =\sum_{\sigma\in\Sigma}(-1)^{\dim\sigma}\dim V^{U_\sigma}.
\tag{6.146}
\]
Positive-degree vanishing identifies the right side with \(\dim H_0(\Sigma,V)\). Augmentation maps this last space onto \(\sum_{x\in\Sigma^0}V^{U_x}=u_\Sigma V\); boundaries augment to zero. The two finite dimensions agree, so this map is an isomorphism. This proves (6.145). An empty \(\Sigma\) gives the zero complex. For \(r=1\), the nonempty building has one vertex and the assertion is immediate. \(\square\)

**Proposition 6.64 — the finite cellular trace formula.** Let \(V\) be smooth admissible and generated by \(V^{U_o}\) at a level with \(dm\ge2\). Let \(C\) be the full stabilizer of a simplex. For every \(f\in C_c^\infty(C)\), there is a finite convex \(C\)-invariant \(\Sigma_0\) such that every finite convex \(C\)-invariant \(\Sigma\supset\Sigma_0\) satisfies
\[
 \begin{aligned}
 \operatorname{tr}\pi_V(f)&=\int_C f(g)L_\Sigma(g)\,dg,\\
 L_\Sigma(g)&=
   \sum_{\sigma\in\Sigma,\ g\sigma=\sigma}
    (-1)^{\dim\sigma}\epsilon_\sigma(g)
             \operatorname{tr}(\pi_V(g)|V^{U_\sigma}).
 \end{aligned}
\tag{6.147}
\]
Here \(f\) is compactly supported in the actual group, so no central-character hypothesis or quotient integral is needed.

**Proof.** The operator \(\pi_V(f)\) has finite rank by admissibility. Express a basis of its image as finite sums from vertex fixed spaces. The \(C\)-invariant finite convex exhaustion in Proposition 6.51 supplies \(\Sigma_0\) containing these vertices. The operator \(u_\Sigma\) is the identity on the image, and \(C\)-invariance makes \(u_\Sigma V\) stable under \(C\). Thus the trace on \(V\) equals the trace on this finite-dimensional invariant space; the operator induced on the quotient has zero image.

Apply (6.145) to \(\Sigma\). It is a finite exact complex of \(C\)-representations. Additivity of trace across invariant subspaces gives the trace of \(f\) on its augmentation as the alternating trace on its chain spaces. To verify that additivity directly, choose a basis of an invariant subspace and extend it; the resulting block triangular matrix has trace the sum of its two diagonal-block traces. Apply this to boundaries and cycles in the exact complex; the boundary contributions cancel in adjacent degrees.

In a chain space, \(g\) sends the summand at \(\sigma\) to the one at \(g\sigma\). Its diagonal block is zero unless the simplex is stabilized. For a stabilized simplex it is \(\epsilon_\sigma(g)\pi_V(g)\) on its coefficient space. There are finitely many summands. Integrating these finite-dimensional traces against \(f\) proves (6.147). \(\square\)

**Theorem 6.65 — an actual elliptic character.** Every finitely generated smooth admissible \(V\) has a locally constant character density on the elliptic regular set. For any generating level with \(dm\ge2\), it is
\[
 \begin{aligned}
 \Theta_V(\gamma)&=L_{V,m}(\gamma),\\
 L_{V,m}(\gamma)&=\sum_{\gamma\sigma=\sigma}(-1)^{\dim\sigma}
       \epsilon_\sigma(\gamma)
                  \operatorname{tr}(\pi_V(\gamma)|V^{U_\sigma}).
 \end{aligned}
\tag{6.148}
\]
The sum is finite. Its value is independent of that generating level and is conjugacy invariant. If \(V\) has central character \(\omega\), then \(\Theta_V(z\gamma)=\omega(z)\Theta_V(\gamma)\).

**Proof.** A sufficiently deep level generates \(V\), by Theorem 6.56. An elliptic regular \(\gamma\) stabilizes a simplex by Proposition 6.52; its full stabilizer \(C\) is open. Choose a compact open neighbourhood \(B\) of \(\gamma\) contained in \(C\) and in the elliptic regular set. Proposition 6.52 supplies a common finite set \(S\) containing every simplex stabilized by any \(g\in B\).

For a test function supported in \(B\), enlarge the finite \(C\)-invariant convex subcomplex used in Proposition 6.64 to contain \(S\). This is possible using the same exhaustive subcomplexes of Proposition 6.51. The finite inner sum in (6.147) is then precisely the full finite sum \(L_{V,m}(g)\), for every \(g\) in the support. Hence
\[
 \operatorname{tr}\pi_V(f)=\int_B f(g)L_{V,m}(g)\,dg
                    \qquad(f\in C_c^\infty(B)).
\tag{6.149}
\]
Proposition 6.52 already proves local constancy of this function. Thus (6.149) proves, rather than assumes, that it is the character density on \(B\). The neighbourhoods cover the elliptic regular set. Two locally constant densities defining the same distribution agree pointwise: integrate their constant difference over a sufficiently small compact open neighbourhood. This proves independence of level. Conjugation carries the finite fixed-simplex set and its coefficient spaces bijectively to the corresponding set for the conjugate, preserving all traces and signs. A central element fixes every simplex, and acts on its coefficient by \(\omega(z)\), proving the last assertion. \(\square\)

Together with Proposition 6.59, the normalized Euler–Poincaré test therefore satisfies
\[
 O_\gamma(f_{V,m})=\Theta_V(\gamma^{-1})
             \qquad(\gamma\text{ elliptic regular}),
\tag{6.150}
\]
when \(V\) also has the central character required in (6.136). The torus measure remains \(\operatorname{vol}(G_\gamma/Z)=1\). This identifies an orbital function with the actual elliptic character. It asserts no completeness of these characters in the elliptic comparison space.

**Example 6.66 — a cyclic chamber in every split rank.** Let \(D=F\), let \(\operatorname{char}F\) not divide \(r\), and define \(\gamma e_i=e_{i+1}\) for \(i<r\), \(\gamma e_r=\varpi_F e_1\). Then
\[
 \begin{gathered}
 \gamma^r=\varpi_F I,\qquad
 \det\gamma=(-1)^{r-1}\varpi_F,\\
 L_j=\varpi_F\mathcal O_F^{\,j}\oplus
                         \mathcal O_F^{\,r-j}\quad(0\le j<r).
 \end{gathered}
\tag{6.151}
\]
The polynomial \(T^r-\varpi_F\) is irreducible: every root has valuation \(1/r\), so a monic factor of degree \(s\) would have constant term of valuation \(s/r\); for \(0<s<r\) this is not an integer. Its derivative \(rT^{r-1}\) is nonzero at every root, so it is separable. Thus \(\gamma\) is elliptic regular. It cycles the displayed standard chamber. Its action adds one to vertex type modulo \(r\). Any stabilized simplex must consequently have all \(r\) types, so is a chamber, and its vertex permutation is an \(r\)-cycle. Every term's orientation and dimension factors multiply to \((-1)^{r-1}(-1)^{r-1}=1\).

Apply (6.148) to the trivial representation. Its character is directly the constant function one, so the formula says that the number of stabilized chambers is one. Thus the standard chamber is the unique one. For a smooth determinant character, choose a generating level which fixes that character on every \(U_x\); the same chamber contributes \(\chi((-1)^{r-1}\varpi_F)\), as the direct one-dimensional character calculation requires. When the field characteristic divides \(r\), the displayed polynomial is inseparable; the elliptic regular theorem is not applied to it.

The lattice-height criterion has a related formulation in Grosse-Klönne, Sections 1 and 3 of the free author preprint. The bound \(dm\ge2\) is used in the common-neighbour normalization in Lemma 6.62. Section 6.14 proves the ordinary regular-character assertion on compact nonelliptic classes and on the entire regular semisimple set. Discrete-series elliptic orthogonality and completeness, and the full representation transfer require their further arguments.


### 6.14. Regular characters and stable cellular traces

The fixed simplices of a compact nonelliptic element need not form a finite set. They can nevertheless be controlled by finitely many orbits under its regular centralizer. This supplies the regular-set character theorem from the finite trace formula. Throughout, coefficients are complex, and \(G_{\mathrm{reg}}\) means the regular semisimple set.

**Lemma 6.67 — products and the finite trace formula.** The finite resolution and trace argument of Section 6.13 also apply to
\(H=\prod_{j=1}^sG_j\), \(G_j=\mathrm{GL}_{r_j}(D)\), using product subcomplexes \(\Sigma=\prod_j\Sigma_j\), product cell groups and a level with \(dm\ge2\). If \(V\) is smooth admissible, the total cellular complex resolves
\[
 u_\Sigma V=\Bigl(\prod_j u_{\Sigma_j}\Bigr)V,
 \qquad
 V_\sigma=V^{\prod_jU_{\sigma_j}},
 \quad \dim\sigma=\sum_j\dim\sigma_j.
\tag{6.152}
\]
The action of \(H\) does not permute the factors, so the orientation sign is the product of their orientation signs. If \(V\) is generated by its product-vertex fixed space, Proposition 6.64 holds for tests in \(C=\prod_jC_j\), with each \(C_j\) a simplex stabilizer and with sufficiently large finite convex \(C_j\)-invariant factors \(\Sigma_j\).

**Proof.** For two factors, form the double complex whose \((p,q)\)-term is the sum of \(V^{U_{\sigma_1}\times U_{\sigma_2}}\) over the corresponding cells, with the second differential multiplied by \((-1)^p\). For a fixed cell in the second factor, \(V^{U_{\sigma_2}}\) is admissible for the first: its compact-open fixed spaces are fixed spaces for compact-open product groups in \(H\). Theorem 6.63 therefore makes the first augmented direction exact, with image \(u_{\Sigma_1}V^{U_{\sigma_2}}\). The latter equals \((u_{\Sigma_1}V)^{U_{\sigma_2}}\), since operators from different factors commute.

The space \(u_{\Sigma_1}V\), as a representation of the second factor, is admissible. It is a finite sum of spaces fixed by first-factor vertex groups, and taking any second-factor compact-open invariants puts it in a finite sum of admissible product fixed spaces. Apply Theorem 6.63 in the second direction. These two exact augmented directions prove exactness of the total complex. Explicitly, project the total complex to the second complex with coefficient \(u_{\Sigma_1}V\). In its kernel each first augmented row is exact. A cycle in that kernel can be filled starting with its largest second degree: first-direction exactness removes that component, introducing components only in smaller second degree. This terminates, so the kernel is acyclic. The projected complex is exact in positive degrees with the stated augmentation. This proves the two-factor assertion; induction proves (6.152).

Admissibility makes every final product-cell space finite-dimensional. The operators \(u_{\Sigma_j}\) commute, and their product is the identity on every product-vertex fixed vector once its vertices occur in the chosen factors. Generation and a finite basis of the image of a test operator therefore give the same finite-image containment as in Proposition 6.64. The exact total complex is invariant under \(C\). Taking its finite alternating trace proves the product trace formula. A finitely generated smooth \(H\)-representation is generated at a sufficiently deep product level, by intersecting the stabilizers of finitely many generators. \(\square\)

**Lemma 6.68 — uniform toral control of fixed cells.** Let \(\gamma\in G_{\mathrm{reg}}\), \(E=F[\gamma]\) and \(T=E^\times\). There is a compact toral neighbourhood \(B_T\) of \(\gamma\), all of whose elements generate \(E\) and are regular, and a finite set of simplices \(S\) such that
\[
 \{\sigma:y\sigma=\sigma\text{ for some }y\in B_T\}
                  \subset T S.
\tag{6.153}
\]
For any chosen level \(m\), there is a compact open subgroup \(U\subset T\) such that \(\gamma U\subset B_T\), and, for every \(t\in U\),
\[
 \mathcal B^{\gamma t}_{\mathrm{cells}}
          =\mathcal B^\gamma_{\mathrm{cells}},
 \qquad
 \pi(t)|V^{U_\sigma}=1
       \quad(\gamma\sigma=\sigma).
\tag{6.154}
\]
The permutations of the vertices also agree. This assertion about coefficient spaces holds for every smooth \(V\). The same conclusions hold for a finite product \(H\), with \(E=\prod_jF[\gamma_j]\) and \(T=\prod_jF[\gamma_j]^\times\); no distinct-spectrum condition between different factors is required.

**Proof: finite centralizer orbits.** Lemma 6.18 proves uniform properness of \(T\backslash G\to G\) as the toral element varies in a sufficiently small compact \(B_T\) whose elements generate the fixed algebra \(E\). Recall why its uniform assertion applies: the field-factor idempotents in \(E\) stay fixed, normalizing the corresponding rows by centralizer scalars bounds them, and every limit intertwiner is invertible on each simple block. The condition that the powers of the toral element span \(E\) is open, so this argument supplies the required neighbourhood without changing the centralizer.

Choose representatives \(\eta\) of the finitely many simplex types. If \(y\in B_T\) stabilizes \(h\eta\), then \(h^{-1}yh\in C_\eta\). Restricting \(C_\eta\) to the compact annulus of absolute reduced norms occurring in \(B_T\) gives an actual compact set, since \(C_\eta/Z\) is compact. Uniform properness puts every such \(Th\) in a common compact subset of \(T\backslash G\). Its image in the discrete space \(T\backslash G/C_\eta\) is finite. Thus the possible cells have finitely many \(T\)-orbits, proving (6.153). For a product use the component reduced norms and the component properness assertions; their compact sets have compact product.

**Proof: a common small torus subgroup.** Choose \(U\) small enough that \(\gamma U\subset B_T\) and \(U\subset\bigcap_{\sigma\in S}U_\sigma\). Such a subgroup exists because this is a finite intersection of open identity neighbourhoods in \(T\). Each \(t\in U\) fixes these simplices pointwise and is the identity on their coefficient spaces. Since \(T\) is abelian and \(U_{a\sigma}=aU_\sigma a^{-1}\), the same statements hold on every cell in \(TS\). Every cell stabilized by \(\gamma t\), and every one stabilized by \(\gamma\), lies in \(TS\). Hence \(\gamma t\) stabilizes a cell exactly when \(\gamma\) does, with the same vertex permutation; and their coefficient actions coincide there. This proves (6.154). All steps apply to product cells and product groups too. \(\square\)

**Theorem 6.69 — compact-mod-centre regular characters.** Let \(V\) be a finitely generated smooth admissible representation of \(G\), or of a finite product \(H\) as in Lemma 6.67. At every regular \(\gamma\) with compact cyclic closure modulo the group's own centre, its trace distribution has a locally constant density on a neighbourhood of \(\gamma\). Choose a generating level with \(dm\ge2\), a simplex stabilizer \(C\) containing \(\gamma\), and put
\[
 L_\Sigma(g)=\sum_{g\sigma=\sigma,\ \sigma\in\Sigma}
      (-1)^{\dim\sigma}\epsilon_\sigma(g)
                  \operatorname{tr}(\pi(g)|V_\sigma).
\tag{6.155}
\]
For sufficiently large finite convex \(C\)-invariant \(\Sigma\), this finite sum at \(\gamma\) is independent of \(\Sigma\) and equals that density at \(\gamma\). In a product, take the cofinal product subcomplexes of Lemma 6.67. No sum over all fixed cells is required.

**Proof: constancy before stabilization.** Proposition 6.52 supplies a simplex stabilized by \(\gamma\), factor by factor in a product. Take its full stabilizer \(C\), which is open, and the small subgroup \(U\subset T\) from Lemma 6.68. Since \(\gamma\)'s stabilized simplex belongs to \(TS\), this \(U\) fixes it; hence \(\gamma U\subset C\). For every finite \(C\)-invariant \(\Sigma\), (6.154) gives \(L_\Sigma(\gamma t)=L_\Sigma(\gamma)\) for \(t\in U\). Also \(L_\Sigma\) is invariant under conjugation by \(C\): conjugation permutes the finite cell summands and identifies their coefficient spaces and orientation signs.

There is an open neighbourhood \(W\subset C\) of \(\gamma\) such that every \(x\in W\) has the form
\[
 x=k^{-1}\gamma t k,\qquad k\in K\subset C,
                         \quad t\in U,
\tag{6.156}
\]
where \(K\) is compact open. To prove this chart, write \(A=E\oplus\mathfrak s\), with \(\mathfrak s=(1-\operatorname{Ad}(\gamma^{-1}))A\). After separable splitting, these are the diagonal and off-diagonal matrix spaces, so \(1-\operatorname{Ad}(\gamma^{-1})\) is invertible on \(\mathfrak s\). These statements descend as linear equations over \(F\). The derivative of
\((X,Y)\mapsto(1+X)^{-1}\gamma(1+Y)(1+X)\), with \(X\in\mathfrak s\), \(Y\in E\), becomes \(Y+X-\gamma^{-1}X\gamma\) after left translation. It is invertible. The complete-ball contraction proof in Theorem 6.42 gives an open inverse chart. Shrink its domain so that \(1+X\in K\subset C\) and \(1+Y\in U\). For a product do this componentwise. Consequently every \(L_\Sigma\), before any size condition on \(\Sigma\), is constant on this one \(W\), of value \(L_\Sigma(\gamma)\).

**Proof: stabilization from one test.** Shrink \(W\) to a compact open neighbourhood and let \(f_0=1_W/\operatorname{vol}(W)\). The finite trace formula supplies \(\Sigma_0\) such that, for every invariant finite \(\Sigma\supset\Sigma_0\),
\[
 L_\Sigma(\gamma)=\int f_0(g)L_\Sigma(g)\,dg
                         =\operatorname{tr}\pi(f_0)=:c.
\tag{6.157}
\]
This is eventual equality, with no exchange of an infinite sum and an integral. For any \(f\in C_c^\infty(W)\), choose a larger invariant finite subcomplex that also accommodates its finite-rank image as in Proposition 6.64 or Lemma 6.67. Its trace formula and (6.157) give
\[
                    \operatorname{tr}\pi(f)=c\int_W f(g)\,dg.
\tag{6.158}
\]
This proves the actual locally constant density and the stabilized value. Uniqueness follows by testing the constant difference of two such densities on a small compact open neighbourhood. \(\square\)

**Theorem 6.70 — the character on the entire regular set.** Every finitely generated smooth admissible \(V\) of \(G=\mathrm{GL}_r(D)\), in either field characteristic, has a unique locally constant trace density \(\Theta_V\) on \(G_{\mathrm{reg}}\). If \(P_\gamma=M_\gamma N_\gamma\) is the slope parabolic of Lemma 6.39, then
\[
 \Theta_V(\gamma)=\Theta_{V_{N_\gamma}}(\gamma)
       =\delta_{P_\gamma}(\gamma)^{1/2}
                         \Theta_{\pi_{P_\gamma}}(\gamma).
\tag{6.159}
\]
The middle term uses the unnormalized Jacquet action; the last one uses normalized action. Precisely, the density assertion means
\[
 \operatorname{tr}\pi(f)=\int_{G_{\mathrm{reg}}}
                   f(g)\Theta_V(g)\,dg
          \qquad(f\in C_c^\infty(G_{\mathrm{reg}})).
\tag{6.160}
\]
It does not assert extension of this integral identity to tests meeting the singular set.

**Proof.** In each slope block, all eigenvalues have the same valuation. Lemma 6.39 shows that \(\gamma\) has compact cyclic closure modulo the centre of that block. It is regular in each block, since the full reduced polynomial is separable. The Levi is a finite product of division matrix groups. Its Jacquet module is admissible by Lemma 6.22 and finitely generated by Lemma 6.40. Theorem 6.69 therefore proves a locally constant density for its trace near \(\gamma\), with no irreducibility or fixed-central-character requirement. Theorem 6.42 applies and proves (6.159) and local regularity in \(G\). If there is just one slope, Theorem 6.69 already gives the assertion directly.

These open regular neighbourhoods cover \(G_{\mathrm{reg}}\). Their densities agree on overlaps by uniqueness against compact-open tests. Any compactly supported test in this regular set has a finite compact-open partition subordinate to this cover. Adding the local identities proves (6.160) and uniqueness on the whole regular set. The same reasoning gives the regular-set assertion for finite products when needed. \(\square\)

**Corollary 6.71 — point traces and character operations.** For regular \(\gamma\) and every sufficiently small compact open \(J\),
\[
 \Theta_V(\gamma)=\operatorname{tr}(\pi(\gamma)e_J)
        =\operatorname{tr}\bigl(e_J\pi(\gamma)e_J|V^J\bigr).
\tag{6.161}
\]
Thus these normalized coset traces are eventually constant. The character is conjugacy invariant, additive on short exact sequences of finitely generated admissible representations, and has central covariance \(\Theta_V(zg)=\omega(z)\Theta_V(g)\) when \(V\) has central character \(\omega\). For irreducible admissible \(V\), its smooth contragredient satisfies
\[
 \Theta_{\widetilde V}(g)=\Theta_V(g^{-1}),
 \qquad
 \Theta_V(g^{-1})=\overline{\Theta_V(g)}
                          \quad\text{if }V\text{ is unitary}.
\tag{6.162}
\]
The Levi trace hypothesis in Theorem 6.4 is now proved for every finitely generated smooth admissible inducing module, so its normalized induction formula applies to all such modules.

**Proof.** Choose \(J\) so that \(\gamma J\) is contained in a constant-density neighbourhood. Apply (6.160) to its normalized indicator to obtain the first equality in (6.161). A finite-rank operator with finite-dimensional domain projection has the trace of its compression, proving the second. Conjugation carries such averages to the conjugated compact group and preserves their finite-rank traces. Central covariance follows from the scalar action on the same averages. Additivity follows by choosing a compact-open averaging group for the test and using exactness of its invariants; finite-dimensional traces on the resulting exact sequence add, and uniqueness of locally constant densities gives the pointwise identity.

For completeness, the natural pairing gives \(\widetilde V^J=(V^J)^*\): extend any functional on \(V^J\) by composing with \(e_J\). It is smooth and gives the required functional, while averaging proves nondegeneracy. The smooth contragredient of an irreducible admissible \(V\) is irreducible. A nonzero invariant subspace of it has invariant annihilator in \(V\), hence zero annihilator. Averaging on \(J\) shows that its \(J\)-fixed part separates the finite-dimensional \(V^J\), so equals \((V^J)^*\); taking the union over \(J\) proves irreducibility. It is admissible and finitely generated, so Theorem 6.70 applies. The two compressed operators at \(g\) and \(g^{-1}\) are transposes under this pairing, proving the first formula in (6.162). In the unitary case they are Hilbert adjoints, proving the second. The last assertion is Theorem 6.70 on the product Levi, inserted into the proved hypothesis of Theorem 6.4. \(\square\)

**Example 6.72 — compact split characters near a singular element.** For \(\gamma=\operatorname{diag}(a,b)\) with \(|a|=|b|\) and \(a\ne b\), Theorem 6.4 has two fixed lines and gives
\[
 \Theta_{I(\mu_1,\mu_2)}(\gamma)
 =\frac{\mu_1(a)\mu_2(b)+\mu_1(b)\mu_2(a)}{|1-a/b|}.
\tag{6.163}
\]
Indeed \(\Delta_G(\gamma)^{1/2}=|a-b|/|ab|^{1/2}=|1-a/b|\), while the torus discriminant is one. For \(\tau=I(|\cdot|^{-1/2},|\cdot|^{1/2})\), both numerator terms are one. Its exact sequence with constants and Steinberg therefore gives \(\Theta_{\mathrm{St}}(\gamma)=2/|1-a/b|-1\). In particular, if \(b=1+\varpi_F^s u\), \(s\ge1\), \(u\) a unit, then
\[
 \Theta_{I(1,1)}(\operatorname{diag}(1,b))=2q_F^s,
 \qquad
 \Theta_{\mathrm{St}}(\operatorname{diag}(1,b))=2q_F^s-1.
\tag{6.164}
\]
These are locally constant at every displayed regular element, although their values grow as the elements approach the nonregular identity. The regular-set theorem and the additional analytic assertions about behaviour across the singular set are distinct statements.

Meyer–Solleveld, Section 7 of the free author preprint, gives related local-constancy and Jacquet results with quantitative neighbourhoods. The finite centralizer-orbit argument above uses the uniform orbital coordinates of Lemma 6.18 and finite cellular exactness. Section 6.15 proves absolute unipotent integration and vanishing constant terms for every discrete series, together with positive nonelliptic orbital descent. General elliptic orbital convergence, elliptic orthogonality and completeness, and the full representation transfer remain separate assertions.


### 6.15. Unipotent integration and cuspidal constant terms

Discrete-series coefficients need not be compactly supported modulo the centre. Their decay nevertheless makes every translated unipotent constant term absolutely convergent, and that constant term is zero. We prove this in every matrix rank and division degree, in either characteristic. We also give the positive orbital estimate that reduces nonelliptic convergence to elliptic convergence in smaller blocks.

Write \(G=\mathrm{GL}_r(D)\), \(q_D=q_F^d\), \(K=\mathrm{GL}_r(\mathcal O_D)\), and \(|\Pi|_D=q_D^{-1}\). Let \(B\) be the upper triangular subgroup. Iwasawa decomposition, proved by the adapted-basis argument in Theorem 6.4, writes \(g=bk\). Put
\[
 e(g)=\delta_B(b)^{1/2},\qquad
 W_\alpha(g)=D_C(g)^{1/2}e^{-\alpha\sigma(g)}
                         \quad(\alpha>0).
\tag{6.165}
\]
The first function is well defined because the modulus is one on \(B\cap K\). The second uses the intrinsic Cartan functions of Lemma 6.33. All unipotent Haar measures below may be fixed arbitrarily; constants change with their normalization.

**Lemma 6.73 — lattice heights for Iwasawa coordinates.** Give \(\mathcal O_D^i\) volume one. Let \(R_i(g)\) be the volume of the image lattice obtained by projecting \(g\mathcal O_D^r\) to its last \(i\) coordinates, and let \(v(g)=\operatorname{vol}(g\mathcal O_D^r)\). Then
\[
 e(g)=\frac{v(g)^{(r-1)/2}}{\prod_{i=1}^{r-1}R_i(g)},
                   \qquad D_C(g)^{1/2}\le e(g).
\tag{6.166}
\]
For a lower unitriangular \(n\), define \(h(n)=-\log_{q_D}e(n)^2\). This is a nonnegative integer. If \(r>1\),
\[
 h(n)=2\sum_{i=1}^{r-1}\log_{q_D}R_i(n),\qquad
 h(n)\le r(r-1)\sigma(n),\qquad
 \sigma(n)\le \frac r2h(n).
\tag{6.167}
\]

**Proof.** For upper triangular \(b\), the projected bottom lattice has volume the product of the absolute division norms of its last \(i\) diagonal entries. Right multiplication by \(K\) does not change any image lattice. Multiplying these products proves the first identity in (6.166).

The product of the largest \(i\) singular numbers of \(g\) bounds \(R_i(g)\). Here singular numbers mean the powers of \(q_D\) given by integral row and column diagonalization. The same diagonalization applies to a rectangular surjective matrix; its image-lattice volume is the product of its nonzero singular numbers. Its \(j\)-th singular number has the minimax proof of (6.80), with domain dimension \(r-j+1\). A coordinate projection has operator norm one, so this minimax description bounds each singular number of the projected map by the corresponding one of \(g\). Multiply these bounds. In the Cartan diagonal case the expression on the right of (6.166), with these largest-singular-number products in its denominator, is exactly \(D_C(g)^{1/2}\). This proves the inequality, without determinants of matrices over a noncommutative ring.

For lower unitriangular \(n\), each bottom projected lattice contains the lattice generated by its bottom-right square block. That triangular block has volume one, so \(R_i(n)\ge1\). For an entry \(n_{ab}\), \(b<a\), select the bottom \(r-a+1\) rows and columns \(b,a+1,\ldots,r\). The resulting square matrix has first row \((n_{ab},0,\ldots,0)\) and a unitriangular remaining diagonal. Its column lattice has volume \(|n_{ab}|_D\), and lies in that projected lattice. Consequently every entry of \(n\) has norm at most \(\max_iR_i(n)\). The finite expansion of \((1+(n-1))^{-1}\) bounds \(\|n^{-1}\|\) by \(\|n\|^{r-1}\). Thus \(\sigma(n)\le r\log_{q_D}\|n\|\le rh(n)/2\). Conversely \(R_i(n)\le\|n\|^i\) by the rectangular singular-number bound, and \(\log_{q_D}\|n\|\le\sigma(n)\), since both triangular matrices have a diagonal entry one. Summing proves (6.167). \(\square\)

**Lemma 6.74 — a polynomial spherical bound.** The normalized minimal principal series \(I_B^G(1)\) is unitary and admissible. Its spherical vector is \(e\), of norm one in the compact model. Its coefficient
\[
 \Xi(g)=\langle I_B^G(1)(g)e,e\rangle
       =\int_K e(kg)\,dk
       \le C D_C(g)^{1/2}(1+\sigma(g))^b
\tag{6.168}
\]
is positive and \(K\)-bi-invariant, for some \(C,b\) depending only on the group.

**Proof: the needed principal-series Jacquet calculation.** For a standard \(P=MN\), the normalized Jacquet module of \(I_B^G(1)\) has a finite filtration whose quotients are copies of \(I_{B\cap M}^M(1)\). In particular the action of the field-scalar centre \(A_M\) of each block is unipotent, with a common finite nilpotence bound.

Here are the support and measure details. Successive pivots over \(D\) put a full flag relative to the fixed partial flag into a unique permutation position, up to permutations within the Levi blocks. At each pivot, the nonpivot entries give free division coordinates; the imposed earlier zero entries give its stratum. Rank conditions on initial row and column rectangles specify the closures: they are closed because the corresponding ranks of \(F\)-linear maps are specified by vanishing minors. Ordering these finitely many strata by their closures gives an open support filtration of the induced space. Restriction to a closed remaining stratum is onto: a compactly supported locally constant section extends on finitely many compact-open coordinate sets. Thus its successive quotients are the compactly supported sections on the individual strata.

Choose a permutation \(w\) increasing within each Levi block. Its stratum is \(B wP\). Its unipotent fibre is \(H_w\backslash N\), where \(H_w=N\cap w^{-1}Bw\); its Levi base is \((B\cap M)\backslash M\). Fibre integration computes the \(N\)-coinvariant quotient. To verify its kernel, exhaust \(N\) by compact subgroups. For a compactly supported locally constant function on \(H_w\backslash N\), choose one subgroup large enough to contain representatives of its support. Averaging over that subgroup is its integral times the normalized constant function on its compact orbit. Thus an integral-zero function is a finite sum of translation differences. For sections over the Levi base the same argument works on a finite compact-open partition, with one common subgroup. It also proves surjectivity, by choosing fibre functions of integral one on each part. Taking \(N\)-coinvariants is exact: its relation space is the increasing union of the compact-subgroup relation spaces, and averaging makes each compact-group coinvariant functor exact. Every relation or kernel witness involves finitely many vectors, hence occurs at one compact stage. Thus these fibre quotients give a filtration of the actual Jacquet module.

For completeness, let \(V_w=\operatorname{Lie}(N)/\operatorname{Lie}(H_w)\), and let \(\delta_{V_w}(z)\) be the absolute determinant of conjugation by \(z\in B\cap M\) on that quotient. The fibre-integrated function is
\(\delta_P(m)^{-1/2}\int_{H_w\backslash N} f(w n m)\,dn\).
Its transformation under \(z\) is \(\delta_{B\cap M}(z)^{1/2}\), because
\[
 \delta_B(wzw^{-1})\delta_{V_w}(z)^2
                    =\delta_P(z)\delta_{B\cap M}(z).
\tag{6.169}
\]
Indeed each cross-block division entry either stays upper triangular after \(w\), contributing to \(H_w\), or becomes lower triangular, contributing to \(V_w\). Its modulus factor occurs with exponent \(+1\) or \(-1\) in the first term; multiplying by the square of the second factor makes both exponents \(+1\). Internal block factors give \(\delta_{B\cap M}\). This uses ordinary \(F\)-linear determinants on division-entry spaces and holds in both characteristics. The normalized Levi action is consequently exactly the stated induced action. On its block centre that action is trivial. A filtration of length \(l\) with trivial central actions on its quotients gives \((a-1)^l=0\) for every \(a\in A_M\), as asserted. Inserting inducing characters in the same fibre formula carries their permutation by \(w\) to the quotient. In rank two the two normalized minimal Jacquet quotients therefore have characters \(\mu_1\otimes\mu_2\) and \(\mu_2\otimes\mu_1\).

**Proof: the coefficient bound.** The normalized compact-model pairing is invariant. On a Gaussian flag chart, right action followed by triangular refactorization has coordinate Jacobian \(\delta_B(b)\): its tangent action on the lower entry coordinates is conjugation by \(b^{-1}\). The two normalized fibre factors contribute this same modulus, so change of variables preserves their integral. A finite compact-open chart partition proves invariance on all flags; the non-open pivot loci have measure zero, since a nonzero polynomial over a local field has a zero set of measure zero, by induction on its variables and Fubini. This proves unitarity directly. Admissibility was proved in Theorem 6.4.

Apply the exact every-face coefficient formula, Theorem 6.30 and Corollary 6.31, to the spherical pair. On each face its unbounded coordinates are the central positive elements of the corresponding Levi. The calculation above makes all their normalized Jacquet eigenvalues one, with only nilpotent polynomial factors. The bounded coordinates take finitely many values. Their modulus factors differ from the full Cartan modulus by bounded constants. The finite division-residue cover in Lemma 6.23 therefore bounds every face by \(C D_C(g)^{1/2}(1+\sigma(g))^b\). Taking the maximum of the finitely many degrees and constants gives (6.168). Positivity follows from the displayed integral of the positive function \(e\). \(\square\)

**Theorem 6.75 — absolute unipotent integration.** Let \(P=MN\) be standard, and let \(\overline N\) be its opposite radical. There are constants \(C,b\) such that
\[
 \int_{\overline N,\ h(n)\le H} e(n)\,dn
                 \le C(1+H)^b\quad(H\ge0).
\tag{6.170}
\]
Consequently \(\int_{\overline N}e(n)e^{-\alpha\sigma(n)}dn<\infty\) for every \(\alpha>0\). In particular \(W_\alpha\) is integrable on every unipotent radical. Every smooth discrete-series coefficient is absolutely integrable on every translate \(g_1Ng_2\).

**Proof.** For \(a\in A_M\) the open flag cell gives
\[
                \Xi(a)=c_P\int_{\overline N}e(na)e(n)\,dn,
                       \qquad c_P>0.
\tag{6.171}
\]
We justify this formula before using it for convergence. Induction in stages is the explicit map \(f\mapsto F\), where \(F(g)(m)=\delta_P(m)^{-1/2}f(mg)\), from \(I_B^G(1)\) to \(I_P^G(I_{B\cap M}^M(1))\). Its covariance follows by multiplication, and its compact pairing agrees with the original pairing. In the open cell \(\overline N\) of \(P\backslash G\), that pairing is a constant times
\(\int_{\overline N}\int_{K\cap M}e(kna)e(kn)\,dk\,dn\).
The coordinate Jacobian is the same lower-block determinant calculation as in Lemma 6.74. A finite atlas on the compact partial flag space proves finiteness of this pairing; the omitted pivot loci have measure zero by the polynomial argument there. Since \(a\) commutes with \(K\cap M\), right \(K\)-invariance and the change \(n\mapsto knk^{-1}\) remove the inner average. Its Jacobian is one for compact \(k\). This proves (6.171), including its convergence, without an advance estimate on \(e\) over \(\overline N\).

Let the blocks of \(P\) have sizes \(r_1,\ldots,r_s\). Choose \(L=\lceil H/(2d)\rceil\) and \(a=\operatorname{diag}(\varpi_F^{L(s-1)}I_{r_1},\ldots,I_{r_s})\). Lemma 6.73 bounds every entry of an \(n\) with \(h(n)\le H\) by \(q_D^{H/2}\). Conjugation by \(a^{-1}\) contracts all its nonzero lower cross-block entries by at least \(q_D^{-dL}\); hence \(a^{-1}na\in K\). On this height ball, \(e(na)=e(a)=\delta_B(a)^{1/2}\). Positivity in (6.171), followed by (6.168), cancels that last factor and proves (6.170), since \(\sigma(a)\le C_0(H+1)\).

On the shell \(h(n)=j\), (6.167) gives \(\sigma(n)\ge j/(r(r-1))\). The integral with exponential weight is therefore bounded by a constant times
\(\sum_{j\ge0}(1+j)^b\exp(-\alpha j/(r(r-1)))\), which converges. The case of a trivial radical is immediate. Inequality (6.166) proves the assertion for \(W_\alpha\). Permutation conjugation in \(K\) treats the upper radicals; the adapted-basis argument conjugates any parabolic to a standard one by an element of \(K\). Finally (6.81) bounds a discrete-series coefficient by a constant times some \(W_\alpha\), and (6.79) compares this weight under any fixed left and right translation. This proves the last assertion. \(\square\)

**Proposition 6.76 — uniform decay after unipotent integration.** Let \(D_{C,M}\) be the product of the Cartan weights of the Levi blocks. For every \(\alpha>0\),
\[
 \delta_P(m)^{-1/2}\int_{\overline N}W_\alpha(mn)\,dn
 \le C_\alpha D_{C,M}(m)^{1/2}
                          e^{-\alpha\sigma(m)/2}
                          \quad(m\in M).
\tag{6.172}
\]
For the upper radical the factor on the left is \(\delta_P(m)^{1/2}\). The length on the right is the ambient length in \(G\), including relative central scales between the blocks.

**Proof.** Cartan decomposition in each block, \(K\)-bi-invariance of \(W_\alpha\), and conjugation invariance of Haar measure under \(K\cap M\) reduce to diagonal \(m\), sorted within its blocks. Triangularity of \(mn\) and its inverse shows \(\sigma(mn)\ge\sigma(m)\). Submultiplicativity gives \(\sigma(n)\le\sigma(m)+\sigma(mn)\le2\sigma(mn)\). Consequently
\[
 \begin{gathered}
 \sigma(mn)\ge\tfrac12\sigma(m)+\tfrac14\sigma(n),\\
 D_C(mn)^{1/2}\le e(mn)=\delta_B(m)^{1/2}e(n).
 \end{gathered}
\tag{6.173}
\]
Integrate these bounds and apply Theorem 6.75 with exponent \(\alpha/4\). For the sorted block diagonal, \(\delta_B(m)=\delta_P(m)D_{C,M}(m)\), giving (6.172). Applying the same proof with the opposite minimal subgroup and parabolic gives the upper-radical version. \(\square\)

**Theorem 6.77 — vanishing discrete-series constant terms.** If \(c(g)=\langle\pi(g)v,w\rangle\) is a smooth coefficient of any discrete series and \(P=MN\) is proper, then
\[
                       \int_N c(g_1ng_2)\,dn=0
                                  \quad(g_1,g_2\in G).
\tag{6.174}
\]
These are absolute integrals. This assertion does not say that the proper Jacquet modules are zero.

**Proof.** Theorem 6.75 gives absolute convergence for every pair of smooth vectors. Define the Hermitian form
\[
                       B_N(v,w)=\int_N\langle\pi(n)v,w\rangle\,dn.
\tag{6.175}
\]
It is positive semidefinite. Indeed exhaust \(N\) by compact open subgroups \(N_j\). The integral on each is \(\operatorname{vol}(N_j)\langle P_{N_j}v,w\rangle\), whose value on \((v,v)\) is nonnegative. Absolute convergence gives the limit. Inversion gives Hermitian symmetry. Translation and unitarity make the form invariant under \(N\) in either variable, so it factors through \(V_N\).

Conjugation by \(m\in M\) changes Haar measure by \(\delta_P(m)\). Thus \(B_N(\pi(m)v,\pi(m)w)=\delta_P(m)B_N(v,w)\), and the induced form on the normalized Jacquet module is \(M\)-invariant. Let \(a_P\) be the product of the fundamental positive diagonals at the block boundaries of \(P\). On every finite Jacquet fixed space, its normalized powers tend to zero. To check this consequence precisely, use the canonical fixed-space identification of Lemma 6.22 at a sufficiently small principal level. The unnormalized operator there is \(T_{a_P}=\prod_{j\in J}T_{a_j}\). Since \(a_P\) is block central, \(\delta_P(a_P)=\prod_{j\in J}\delta_j\). Hence its normalized operator is \(\prod_{j\in J}\delta_j^{-1/2}T_{a_j}\). Theorem 6.25 makes each commuting factor have spectral radius less than one. Their powers, and therefore the product powers, tend to zero by the finite Jordan estimate in that theorem.

Any vector of \(V_N\) belongs to such a finite-dimensional fixed space, stable under the central \(a_P\), by admissibility. The form restricted to this finite space is continuous. Its invariance therefore makes its value on a vector equal to the limit of its value on the powers just shown to tend to zero. That value is zero. Polarization makes the whole form zero. Finally \(c(g_1ng_2)\) is the coefficient with input \(\pi(g_2)v\) and second vector \(\pi(g_1^{-1})w\). This proves (6.174). \(\square\)

**Proposition 6.78 — positive orbital descent.** Let \(\gamma\) be regular nonelliptic, and let \(M=\prod_{i=1}^sG_i\), \(s\ge2\), be its primary-factor Levi. Write \(\gamma=(\gamma_i)\) and \(T=\prod_iT_i\). Every \(\gamma_i\) is elliptic regular in \(G_i\). With the same positive weights on each block,
\[
 O_\gamma^G(W_\alpha)
       \le C_{\gamma,\alpha}
                   \prod_{i=1}^s
                O_{\gamma_i}^{G_i}(W_{\alpha/(2s)}^{G_i}).
\tag{6.176}
\]
Both sides are interpreted as nonnegative extended integrals. If the factors on the right are finite, every smooth discrete-series coefficient has an absolutely convergent orbital integral at \(\gamma\), and that orbital integral is zero. In particular this conclusion holds when every primary block has division rank one; it includes all split regular classes in \(\mathrm{GL}_r(F)\).

**Proof.** The quotient integration and polynomial unipotent change of variables in the proof of Theorem 6.20 apply to a nonnegative function by Tonelli, without an advance convergence assumption. Since \(W_\alpha\) is \(K\)-bi-invariant, they give
\[
 O_\gamma^G(W_\alpha)=J_N(\gamma)^{-1}
       \int_{T\backslash M}\int_N
           W_\alpha(m^{-1}\gamma m n)\,dn\,d\dot m.
\tag{6.177}
\]
The upper-radical bound in (6.172) applies. Its parabolic modulus at \(m^{-1}\gamma m\) equals its fixed value at \(\gamma\), which enters the constant. The Levi Cartan weight is the product of the block weights. The ambient length is at least each block length and hence at least their sum divided by \(s\). The remaining integral is bounded by the product in (6.176), by product quotient integration and Tonelli.

Finiteness of those factors proves absolute convergence for a coefficient by (6.81). The now absolutely convergent version of (6.177) for that coefficient is (6.46); its innermost integrals vanish by Theorem 6.77. If every block has division rank one, \(G_i/F^\times\) is compact, as proved in Section 6.4, and therefore so is \(T_i\backslash G_i\). Its displayed weight is bounded, proving finiteness. Section 6.16 constructs the Schwartz algebra and its tempered trace action. Section 6.17 proves nilpotent orbital measures, unipotent orbital continuity and vanishing of nontrivial unipotent orbitals of discrete-series coefficients. General elliptic semisimple orbital estimates in higher division rank, elliptic orthogonality and completeness, and the full representation transfer still require their own arguments. \(\square\)

**Example 6.79 — the Steinberg unipotent integral.** Normalize additive measure by \(\operatorname{vol}(\mathcal O_F)=1\). Let \(v\) be the Steinberg unit vector of the edge between \(L_0=\mathcal O_F^2\) and \(L_1=\mathcal O_Fe_1+\varpi_F\mathcal O_Fe_2\), as in Proposition 2.12. For \(n(x)=\begin{pmatrix}1&x\\0&1\end{pmatrix}\),
\[
 \langle\mathrm{St}(n(x))v,v\rangle=
 \begin{cases}
 1,&|x|\le1,\\
 -q_F^{-(2l-1)},&|x|=q_F^l,\quad l\ge1.
 \end{cases}
\tag{6.178}
\]
Indeed \(n(x)\) fixes \(L_j=\mathcal O_Fe_1+\varpi_F^j\mathcal O_Fe_2\) exactly for \(j\ge l\), so the two edge paths first meet at \(L_l\) and have gallery distance \(2l-1\). The sign can also be checked directly: the average over either vertex stabilizer kills the edge vector, because the Steinberg vertex-fixed space is zero. Its \(q_F\) other edge cosets therefore have normalized average \(-v/q_F\). Alternating the two vertex moves follows the unique gallery without backtracking, so its coefficient is \((-1/q_F)^{2l-1}\). Root-group transitivity on these galleries, proved in Proposition 2.12, identifies this averaged coefficient with each individual one. For \(x\in\mathcal O_F\) the edge is fixed pointwise.

Consequently
\[
 \begin{gathered}
 \int_{\varpi_F^{-L}\mathcal O_F}
       \langle\mathrm{St}(n(x))v,v\rangle\,dx
       =1-(q_F-1)\sum_{l=1}^Lq_F^{-l}=q_F^{-L},\\
 \int_F|\langle\mathrm{St}(n(x))v,v\rangle|\,dx=2,
 \qquad
 \int_F\langle\mathrm{St}(n(x))v,v\rangle\,dx=0.
 \end{gathered}
\tag{6.179}
\]
The normalized Jacquet module of Steinberg is nonzero. Indeed the two-cell calculation in Lemma 6.74 applied to \(\tau=I(|\cdot|^{-1/2},|\cdot|^{1/2})\) gives successive characters \(\delta_B^{-1/2}\) and \(\delta_B^{1/2}\). The constant subrepresentation of \(\tau\) has normalized Jacquet character \(\delta_B^{-1/2}\). Exactness of Jacquet coinvariants in \(0\to1\to\tau\to\mathrm{St}\to0\) leaves the one-dimensional quotient of character \(\delta_B^{1/2}\). Thus a vanishing, absolutely convergent constant term is compatible with a nonzero Jacquet module; it is the integrated positive form (6.175) that vanishes.

Waldspurger, Lemma II.1.1 and §§II.3–II.4 of the freely accessible Plancherel article, gives related spherical and unipotent estimates. Bernstein–Zelevinsky, §5 and §6.4 of the freely accessible first induced-representations paper, gives the general support-filtration method. The lattice-volume bounds, principal-series filtration and its modulus factors, unipotent estimates, positive-form vanishing and orbital descent needed here have been proved above.


### 6.16. The Schwartz algebra and tempered trace operators

We now construct the function algebra on which discrete-series coefficients and tempered traces coexist. This supplies the analytic setting for the remaining orbital estimates. Throughout, \(\omega\) is a smooth unitary central character, \(Q=G/Z\) has the fixed quotient Haar measure, and functions in the algebra transform by \(\omega^{-1}\). All integrals of such functions are taken only when their full integrands descend to \(Q\).

**Lemma 6.80 — spherical convolution and weighted integrability.** For the positive spherical coefficient of Lemma 6.74 there are \(c,C>0\) and an integer \(b\ge0\) such that
\[
 \begin{gathered}
 cD_C(g)^{1/2}\le\Xi(g)\le C D_C(g)^{1/2}(1+\sigma(g))^b,\\
 \Xi(g^{-1})=\Xi(g),\qquad
 \int_K\Xi(xky)\,dk=\Xi(x)\Xi(y).
 \end{gathered}
\tag{6.180}
\]
Haar measure on \(K\) in this formula is probability measure. In particular
\[
 C_s:=\int_Q\Xi(x)^2(1+\sigma(x))^{-s}\,d\bar x<\infty
                      \qquad(s>2b+r-1).
\tag{6.181}
\]

**Proof.** For a Cartan diagonal \(a\) with decreasing division valuations, choose a fixed principal subgroup \(H\subset K\) with its upper-diagonal-lower factorization. Since \(a^{-1}(H\cap\overline N_B)a\subset K\), every \(h\in H\) satisfies \(ha\in N_B(H\cap M_B)aK\). Thus \(e(ha)=\delta_B(a)^{1/2}=D_C(a)^{1/2}\). Integrating the positive compact-model formula for \(\Xi\) over \(H\) proves the lower bound uniformly in \(a\). The Cartan decomposition proves it on all of \(G\); the upper bound is Lemma 6.74.

The compact model has a one-dimensional \(K\)-fixed space, spanned by the unit vector \(e\). Hence its averaging projector sends \(\pi(y)e\) to \(\Xi(y)e\). Pairing after applying \(\pi(x)\) proves the product formula. Unitarity and positivity give \(\Xi(g^{-1})=\overline{\Xi(g)}=\Xi(g)\). Its central character is trivial, so all these weights descend to \(Q\).

Use the finite translated Cartan covering and exact volume bound (6.55)–(6.56). For each nonnegative tuple \(\ell\), its volume is bounded by a constant times \(D_C(t_\ell)^{-1}\), and \(\sigma\) differs from \(d\sum\ell_j\) by bounded constants. The finite division residues change \(D_C\) by bounded factors, by Lemma 6.33. The squared spherical bound cancels this volume weight. The integral is therefore bounded by a constant times \(\sum_{\ell\ge0}(1+\sum\ell_j)^{2b-s}\). The number of tuples of total \(n\) is at most \((1+n)^{r-2}\) times a fixed constant when \(r>1\), by choosing the first \(r-2\) coordinates. The resulting series converges for the stated \(s\). For \(r=1\), \(Q\) is compact and \(\sigma=0\), so convergence is immediate. \(\square\)

For a compact open \(J\subset K\), define \(\mathcal S_{\omega,J}\) to consist of the smooth \(J\)-bi-invariant functions with central rule \(\omega^{-1}\) for which all the norms
\[
 p_N(f)=\sup_{g\in G}|f(g)|\Xi(g)^{-1}(1+\sigma(g))^N
                      \quad(N=0,1,2,\ldots)
\tag{6.182}
\]
are finite. If \(\omega\) is nontrivial on \(J\cap Z\), this space is zero; sufficiently small \(J\) avoid that issue. Put \(\mathcal S_\omega=\bigcup_J\mathcal S_{\omega,J}\). Any compact open subgroup can be replaced by its intersection with \(K\), so these levels cover every smooth function with a compact-open left and right stabilizer satisfying the norms.

**Theorem 6.81 — the Schwartz convolution algebra.** Each \(\mathcal S_{\omega,J}\) is a complete Fréchet space for (6.182), and its compact-mod-centre tests are dense. The union \(\mathcal S_\omega\) is an associative convolution algebra with involution \(f^*(g)=\overline{f(g^{-1})}\). Every convolution integral is absolute. For every integer \(s>2b+r-1\),
\[
                     p_N(f_1*f_2)
                   \le C_s p_{N+s}(f_1)p_N(f_2).
\tag{6.183}
\]
This gives joint continuity between any fixed pair of levels, with target their intersection level. If \(f_R=1_{\{\sigma\le R\}}f\), then
\[
                  p_N(f-f_R)\le(1+R)^{-A}p_{N+A}(f)
                                  \quad(A,N\ge0).
\tag{6.184}
\]
Every \(\mathcal S_{\omega,J}\) embeds continuously in the corresponding centrally covariant \(L^2(Q)\) space.

**Proof: the integral estimate.** Tonelli and the spherical product formula give the exact positive identity
\[
 \int_Q\Xi(x)\Xi(x^{-1}g)(1+\sigma(x))^{-s}\,d\bar x
                                  =C_s\Xi(g).
\tag{6.185}
\]
Indeed replace \(x\) by \(kx\) and average in \(k\in K\). The first weight is unchanged; the average of \(\Xi(x^{-1}k^{-1}g)\) is \(\Xi(x)\Xi(g)\). The right side is finite by (6.181), so this argument also proves convergence of the original positive integral.

Submultiplicativity of the length gives \(1+\sigma(g)\le(1+\sigma(x))(1+\sigma(x^{-1}g))\). Bound \(f_1\) by its \(p_{N+s}\)-norm and \(f_2\) by its \(p_N\)-norm, multiply by \((1+\sigma(g))^N\), and apply (6.185). This proves (6.183) and absolute convergence. The convolution is left invariant under the first level and right invariant under the second, so is bi-invariant under their intersection. Its central transformation is \(\omega^{-1}\): changing a central factor in the integration variable cancels between the two factors, while a central factor in \(g\) remains in the second factor.

Applying the same estimate twice, with sufficiently many powers of decay, makes the absolute double integral for a triple convolution finite. Fubini therefore proves associativity. Inversion preserves the weights and quotient Haar measure, so \(p_N(f^*)=p_N(f)\); changing variables in the absolute convolution integral gives \((f_1*f_2)^*=f_2^**f_1^*\). The bilinear bound proves joint continuity on each pair of fixed levels.

**Proof: completeness and approximation.** A sequence Cauchy in all the norms has a pointwise limit and converges uniformly after multiplication by each fixed weight: this is completeness of the supremum norm, proved by taking pointwise limits in its Cauchy inequality. The limit keeps the central rule and the \(J\)-bi-invariance, hence is smooth. Applying the Cauchy inequality in every \(p_N\) proves that the limit lies in the space and that convergence holds there. The countable norms give a complete metrizable locally convex topology, for example through the metric \(\sum_N2^{-N}\min(1,p_N(f-g))\).

The length balls are compact and open modulo the centre by Lemma 6.33, and \(\sigma\) is \(K\)-bi-invariant. Thus \(f_R\) is a test at the same level. On its omitted support \((1+\sigma)^{-A}\le(1+R)^{-A}\), proving (6.184) and density. Finally \(\|f\|_2^2\le p_N(f)^2C_{2N}\) whenever \(2N>2b+r-1\). This proves the continuous Hilbert-space inclusion. \(\square\)

Here *tempered* means an irreducible admissible unitary representation whose smooth coefficients belong to every \(L^{2+\epsilon}(Q)\), \(\epsilon>0\). Corollary 6.26 proves its equivalent finite Jacquet eigenvalue criterion \(|\lambda|\le1\). This definition and criterion apply in both field characteristics.

**Theorem 6.82 — tempered operators and traces on the Schwartz algebra.** Let \(\pi\) be tempered with central character \(\omega\). There is an integer \(a_\pi\ge0\) such that every smooth coefficient satisfies
\[
 |\langle\pi(g)u,v\rangle|
                 \le C_{u,v}\Xi(g)(1+\sigma(g))^{a_\pi}.
\tag{6.186}
\]
For \(f\in\mathcal S_\omega\), the integrals
\[
 \langle\pi(f)u,v\rangle
       =\int_Q f(g)\langle\pi(g)u,v\rangle\,d\bar g
\tag{6.187}
\]
converge absolutely for smooth \(u,v\) and define a finite-rank operator. They extend the compact-test action. The resulting action is a \(*\)-representation of the algebra, and at each fixed level its operator and trace are continuous. In particular, for suitable \(M\) and a constant depending on \(\pi,J\),
\[
 \begin{gathered}
 \pi(f_1*f_2)=\pi(f_1)\pi(f_2),\qquad
 \pi(f^*)=\pi(f)^*,\\
 \|\pi(f)\|+|\operatorname{tr}\pi(f)|
                         \le C_{\pi,J}p_M(f)
                     \quad(f\in\mathcal S_{\omega,J}).
 \end{gathered}
\tag{6.188}
\]
Its compact cutoffs obey, for any prescribed \(A\),
\[
 \|\pi(f)-\pi(f_R)\|
   +|\operatorname{tr}\pi(f)-\operatorname{tr}\pi(f_R)|
              \le C_{\pi,J}(1+R)^{-A}p_{M+A}(f).
\tag{6.189}
\]

**Proof: coefficient growth.** At a principal level, the commuting normalized positive operators \(\delta_j^{-1/2}T_{a_j}\) have eigenvalues of absolute value at most one by Corollary 6.26. Their finite Jordan expansions are bounded by polynomials in their nonnegative powers. The exact product identity (6.54) therefore bounds any fixed coefficient on the scalar chamber by its Cartan square root times a polynomial in the chamber coordinates. The finite translated covering of Lemma 6.23 treats all directions and division residues. This proves such a bound for one smooth pair. Algebraic irreducibility expresses every other smooth coefficient as a finite sum of its left and right translates, as proved in Proposition 6.19. Lemma 6.33 preserves the polynomial degree under each fixed translation. Thus one degree works for the representation, though its constants depend on the pair. The lower bound in (6.180) converts this bound to (6.186).

**Proof: the actual operator.** Combining (6.186) with \(p_M(f)\), for \(M>a_\pi+2b+r-1\), bounds the absolute integral in (6.187) by a constant times \(p_M(f)C_{M-a_\pi}\). If \(f\) is \(J\)-bi-invariant, averaging each smooth input over \(J\) does not change that integral. These averages are finite sums on smooth vectors, so this use of averaging preserves absolute convergence. The pairing therefore factors through the finite-dimensional \(V^J\) in each variable. Its matrix in an orthonormal basis defines \(\pi(f)=P_J\pi(f)P_J\), a bounded finite-rank operator, and proves the bound in (6.188). This definition is independent of the chosen level, since (6.187) specifies every smooth matrix entry. It agrees with the ordinary integrated action on compact tests. Density then proves uniqueness of the continuous extension at each level.

To justify multiplication, first use smooth \(u,v\). The absolute double integral with integrand \(f_1(x)f_2(y)\langle\pi(xy)u,v\rangle\) is finite. In fact the coefficient bound and \(1+\sigma(xy)\le(1+\sigma(x))(1+\sigma(y))\) reduce it, using sufficiently high seminorms, to the positive integral of
\(\Xi(x)\Xi(y)\Xi(xy)(1+\sigma(x))^{-s}(1+\sigma(y))^{-s}\).
Integration in \(y\) by (6.185), with inversion if needed, gives \(C_s\Xi(x)\); the remaining integral is \(C_s^2\). Fubini is consequently valid and gives the first identity in (6.188). Unitarity and inversion give the second. Finite-dimensional compression extends these identities to the Hilbert operators. Applying the operator bound to (6.184) gives (6.189). These statements concern trace operators; they do not presume a character integral for tests meeting the singular set. \(\square\)

**Corollary 6.83 — discrete-series matrix units and individual Fourier blocks.** For smooth vectors of a discrete series, the matrix-unit functions \(E^\pi_{u,v}\) of (6.85) belong to \(\mathcal S_\omega\). At a level fixing the vectors their compact cutoffs satisfy
\[
 p_N\bigl(E^\pi_{u,v}-1_{\{\sigma\le R\}}E^\pi_{u,v}\bigr)
                           \le C_{N,u,v}e^{-\eta_\pi R/2}.
\tag{6.190}
\]
The exact convolution identities of Theorem 6.36 thus hold within this Schwartz algebra. If \(f\in\mathcal S_{\omega,J}\) and \(u_1,\ldots,u_h\) is an orthonormal basis of \(V_\pi^J\), its orthogonal \(\pi\)-coefficient projection is
\[
 P_\pi f(g)=d_\pi\operatorname{tr}
                   \bigl(\pi(g)^{-1}\pi(f)\bigr)
   =\sum_{i,j=1}^h
       \langle\pi(f)u_i,u_j\rangle E^\pi_{u_j,u_i}(g).
\tag{6.191}
\]
It belongs to the same Schwartz level and depends continuously on \(f\). These projections are idempotent, and projections for inequivalent discrete series are orthogonal. No assertion about convergence of the sum of all these blocks in the Schwartz norms is made here.

**Proof.** Divide the exponential coefficient bound (6.81) by the lower spherical bound in (6.180). It bounds the weighted matrix-unit norm by a constant times \(e^{-\eta_\pi\sigma}(1+\sigma)^N\). On \(\sigma>R\), absorb the polynomial into half the exponential; this proves (6.190), including membership. The algebra products are the absolute products already computed in Theorem 6.36, now between elements of \(\mathcal S_\omega\).

The Schwartz function is in \(L^2\) by Theorem 6.81. Schur orthogonality gives \(\|E^\pi_{u_j,u_i}\|_2^2=d_\pi\) and
\(\langle f,E^\pi_{u_j,u_i}\rangle_{L^2}=d_\pi\langle\pi(f)u_i,u_j\rangle\).
Left and right \(J\)-averaging make every coefficient involving the orthogonal complement of \(V_\pi^J\) vanish. The orthogonal Hilbert-space projection is consequently the finite sum in (6.191). Expanding its finite trace gives the first formula. Each matrix entry is continuous by Theorem 6.82, and each displayed matrix unit lies at the same level, proving Schwartz continuity of this individual projection. Idempotence and cross orthogonality are those of the Hilbert coefficient spaces proved in Theorem 6.15. \(\square\)

**Example 6.84 — the spherical borderline in rank two.** In the split rank-two normalization \(\operatorname{vol}(KZ/Z)=1\), Example 6.32 gives \(\Xi(a_k)=(1+\beta k)q^{-k/2}\), where \(\beta=(q-1)/(q+1)\) and \(a_k=\operatorname{diag}(\varpi_F^k,1)\). The \(k\)-th vertex sphere has \((q+1)q^{k-1}\) elements for \(k\ge1\): the first step has \(q+1\) choices and every later nonbacktracking step has \(q\). Hence
\[
 \int_Q\Xi(g)^2(1+\sigma(g))^{-s}\,d\bar g
       =1+\frac{q+1}{q}\sum_{k\ge1}
                        (1+\beta k)^2(1+k)^{-s}.
\tag{6.192}
\]
The integral converges exactly when \(s>3\). In particular \(\Xi\) itself is not square-integrable, while its every \(L^{2+\epsilon}\) norm is finite: the remaining radial exponential is \(q^{-\epsilon k/2}\), which dominates its polynomial factor. This explains the role of the extra polynomial weights in (6.181).

The product estimate and Schwartz action can be compared with Waldspurger, Lemmas II.1.3–II.1.5, §III.6 and the opening of §III.7 in the free Plancherel article. Section 6.17 gives the orbital bound for every unipotent class. Orbital integrals at a fixed higher-rank elliptic regular semisimple element still need their own bound in these seminorms. The Schwartz algebra and its tempered trace operators alone do not establish that bound, the character integral across the singular set or elliptic completeness.


### 6.17 Nilpotent measures and unipotent orbital integrals

Let \(A=M_r(D)=\operatorname{End}_D(V)\), where \(V\) is a right \(D\)-space of dimension \(r\), and let \(d^2=[D:F]\). A partition \(\lambda\) of \(r\) records the lengths of nilpotent Jordan chains over \(D\). Write \(c_i=\#\{j:\lambda_j\ge i\}\) for its column lengths, stopping at \(c_s>0\). Let \(P_\lambda\) stabilize the standard flag of dimensions \(c_1,c_1+c_2,\ldots,r\); its Lie algebra and strict upper block radical are \(\mathfrak p_\lambda\) and \(\mathfrak n_\lambda\). Put \(N_\lambda=1+\mathfrak n_\lambda\). The measures in this subsection are defined explicitly; they are not the measures on regular semisimple tori in the Weyl formula.

**Lemma 6.85 — Jordan chains and the kernel flag.** Nilpotent conjugacy classes in \(A\) are classified by the partitions of \(r\). For type \(\lambda\),
\[
 \begin{gathered}
 \dim_D\ker X^i=\sum_{j\le i}c_j,\qquad
 \dim_F A_X=d^2\sum_i c_i^2,\\
 \dim_F\mathcal O_\lambda
       =d^2\left(r^2-\sum_i c_i^2\right)
       =2\dim_F(G/P_\lambda).
 \end{gathered}
\tag{6.193}
\]
Here \(A_X=\{a:aX=Xa\}\), and \(\mathcal O_\lambda\) is the conjugacy orbit. For such an \(X\), the only flag of the indicated dimensions satisfying \(XF_i\subset F_{i-1}\) is \(F_i=\ker X^i\). The elements of type \(\lambda\) form an open subset of full additive measure in \(\mathfrak n_\lambda\).

**Proof.** Put \(V_i=\ker X^i\). The map induced by \(X\) from \(V_{i+1}/V_i\) to \(V_i/V_{i-1}\) is injective: an image zero means \(Xv\in V_{i-1}\), hence \(v\in V_i\). Thus the successive dimensions \(c_i\) decrease. Starting with a basis of the highest nonzero quotient, take its iterated images in the lower quotients. At each lower stage extend these independent images to a basis and choose lifts for the new vectors. The new lifts and their iterated images, together with the previously chosen chains, give bases in every successive quotient. Their union is a basis of \(V\). This constructs the Jordan chains over the division ring. Their lengths are determined by the \(c_i\), so the partition is unique; two resulting matrices with the same chains are conjugate over \(D\).

A commuting map from a chain of length \(a\) to one of length \(b\) is specified by the image of its top vector, which can be any vector killed by \(X^a\). It has \(D\)-dimension \(\min(a,b)\). Summing over ordered pairs of chains gives
\(\sum_{a,b}\min(\lambda_a,\lambda_b)=\sum_i c_i^2\).
The group centralizer is the open unit subset of this finite-dimensional \(F\)-algebra, so it is a smooth analytic group of that dimension. Gaussian elimination on a fixed choice of Jordan-chain pivots gives local analytic conjugating matrices: compute the kernel graphs on constant-rank charts, keep the chosen complementary top vectors, and take their successive images as in the chain construction above. To compute the quotient dimension, choose an \(F\)-linear complement \(E\) to \(A_X\) in \(A\). Multiplication \((Y,h)\mapsto(1+Y)h\), for \(Y\in E\) and \(h\in G_X\) near the identity, has derivative \((Y,H)\mapsto Y+H\), an isomorphism. The inverse-function argument of Theorem 6.2 gives local quotient coordinates of dimension \(\dim_F A-\dim_F A_X\). The flag has \(F\)-dimension \(d^2\sum_{i<j}c_ic_j\), proving (6.193).

Iterating \(XF_i\subset F_{i-1}\) gives \(F_i\subset\ker X^i\). Their dimensions agree, proving uniqueness. Every element of \(\mathfrak n_\lambda\) kills \(F_i\) under its \(i\)-th power, and hence has \(\operatorname{rank}_D X^i\le r-\sum_{j\le i}c_j\). A Jordan matrix adapted to its kernel flag attains all these bounds. Attaining them is an open condition. In a fixed \(F\)-basis of \(A\), failure of any one bound is contained in the zero set of an \(F\)-polynomial minor that is nonzero at this Jordan matrix. The zero set of a nonzero polynomial over \(F\) has additive measure zero: induction on the number of coordinates, followed by Fubini, reduces this to the finite root set of a nonzero one-variable polynomial. A finite union of these exceptional sets still has measure zero. The ranks determine the partition by the first formula, proving the last assertion. \(\square\)

**Theorem 6.86 — an explicit nilpotent orbital measure.** Give \(K=\mathrm{GL}_r(\mathcal O_D)\) probability measure and \(\mathfrak n_\lambda\) additive measure with \(\mathfrak n_\lambda\cap M_r(\mathcal O_D)\) of volume one. The formula
\[
 \mu_\lambda(\phi)=
       \int_K\int_{\mathfrak n_\lambda}
                  \phi(kXk^{-1})\,dX\,dk
               \qquad(\phi\in C_c^\infty(A))
\tag{6.194}
\]
defines a locally finite invariant measure supported on the nilpotent cone and concentrated on \(\mathcal O_\lambda\). Its restriction to that orbit is a nonzero invariant orbital measure. The corresponding measure on the unipotent orbit \(1+\mathcal O_\lambda\) is
\[
 U_\lambda(f)=\int_K\int_{N_\lambda}
                   f(knk^{-1})\,dn\,dk,
                 \qquad f\in C_c^\infty(G),
\tag{6.195}
\]
where \(N_\lambda\cap K\) has volume one. An orbital measure obtained from any other fixed Haar measure on the centralizer differs by a positive constant.

**Proof.** The pairing \((Y,X)\mapsto\operatorname{Trd}(YX)\) on \(A\) is nondegenerate by the matrix-unit splitting argument of Section 6.3. Its annihilator of \(\mathfrak p_\lambda\) is exactly \(\mathfrak n_\lambda\), as is seen by pairing opposite blocks and then diagonal blocks. Thus the cotangent bundle of the flag space is
\[
 \begin{gathered}
 T^*(G/P_\lambda)=G\mathbin{\times^{P_\lambda}}\mathfrak n_\lambda,
 \qquad [g,X]\longmapsto gXg^{-1},\\
 Y_\lambda^\circ\xrightarrow{\ \sim\ }\mathcal O_\lambda,
 \qquad
 X\longmapsto\bigl((\ker X^i)_i,X\bigr)
                       \text{ for the inverse.}
 \end{gathered}
\tag{6.196}
\]
Here \(Y_\lambda^\circ\) means the part over matrices of type \(\lambda\). The equivalence in the associated bundle is \((g,X)\sim(gp,p^{-1}Xp)\). Lemma 6.85 proves the displayed bijection. On any fixed nonzero pivot minor, kernels of matrices of constant rank are graphs whose entries are obtained by elimination and inversion of that minor. These are analytic coordinates for the inverse. The forward map is polynomial in matrix charts. This proves the analytic isomorphism in (6.196), including in positive characteristic.

For clarity, the invariant density on a cotangent bundle needs no division by a factorial. In local flag coordinates \(x_1,\ldots,x_m\), with dual fibre coordinates \(\xi_1,\ldots,\xi_m\), take the product additive density \(dx\,d\xi\), using paired Haar measures. If the base coordinates change with derivative \(B\), the fibre derivative is \(B^{-\mathrm t}\); the full derivative is block triangular. Its absolute determinant is one. The densities consequently agree on overlapping charts. The cotangent lift of any analytic base automorphism preserves them by the same calculation. In particular this density is \(G\)-invariant in every field characteristic.

The Iwasawa decomposition makes \(K\) transitive on \(G/P_\lambda\). The compact stabilizer \(K\cap P_\lambda\) preserves additive measure on \(\mathfrak n_\lambda\): its determinant and its inverse both have absolute value at most one, so that determinant has absolute value one. Probability measure on the flag space and these transported fibre measures therefore give the product integral in (6.194). This density is a constant multiple of the cotangent density. Indeed both are translation invariant along each cotangent fibre, so their ratio depends only on the base; both are \(K\)-invariant, and \(K\) is transitive there. As a direct check on the cancellation, a refactorization by \(p\in P_\lambda\) has base determinant \(\delta_{P_\lambda}(p)^{-1}\) on \(\mathfrak g/\mathfrak p_\lambda\), and fibre determinant \(\delta_{P_\lambda}(p)\) on \(\mathfrak n_\lambda\). Their product is one. Hence (6.194) is \(G\)-invariant.

The exceptional fibre set has measure zero by Lemma 6.85 and Fubini, so (6.196) transports this measure onto the single orbit. It is nonzero on every sufficiently small open orbit chart. If \(\phi\) has compact support, compactness of \(K\) puts every \(X\) contributing to (6.194) in a bounded subset of \(\mathfrak n_\lambda\); its additive measure is finite. This proves local finiteness even near smaller nilpotent orbits in the closure. Invariant measures on a transitive orbit differ by a positive scalar: in a local section of the orbit map, disintegrate a Haar measure on \(G\) along a Haar measure on \(G_X\); left invariance fixes the resulting density up to that scalar. Existence of the invariant density also gives unimodularity of \(G_X\), since \(G\) is unimodular.

Finally \(X\mapsto1+X\) is equivariant and has the same centralizer. It identifies \(\mathfrak n_\lambda\) with \(N_\lambda\), preserving the indicated measures. To check the last statement without an exponential map, write all strict upper block entries in order of increasing block distance. Multiplication by a fixed \(1+Y\) is affine triangular in these coordinates with identity diagonal: an entry of \(YX\) or \(XY\) uses strictly shorter distances. Left and right translations have determinant one. Thus additive coordinate measure is Haar measure on \(N_\lambda\), and (6.195) follows. \(\square\)

**Lemma 6.87 — polynomially weighted radical integration.** There is an integer \(a_G\), depending only on \(G\) and the chosen length, such that for every standard parabolic \(P\),
\[
       B_P=\int_{N_P}\Xi(n)(1+\sigma(n))^{-a_G}\,dn<\infty.
\tag{6.197}
\]
The same assertion holds for an opposite radical.

**Proof.** For the opposite radical, Theorem 6.75 gives \(e\)-mass at most \(C(1+H)^{b_P}\) on \(h\le H\). On \(h=j\), Lemma 6.73 gives \(\sigma(n)\ge j/(r(r-1))\) if \(r>1\). Consequently
\(\int e(n)(1+\sigma(n))^{-t}dn\)
is bounded by a constant times \(\sum_{j\ge0}(1+j)^{b_P-t}\), and is finite for \(t>b_P+1\). Lemmas 6.73 and 6.74 give
\(\Xi(n)\le C D_C(n)^{1/2}(1+\sigma(n))^b\le C e(n)(1+\sigma(n))^b\).
Choose \(a_G>b+b_P+1\). There are only finitely many standard block parabolics, so one integer works for all of them. Conjugation by the reversing permutation in \(K\) changes an upper radical into the opposite radical of the reversed block parabolic; \(\Xi\) and \(\sigma\) are \(K\)-bi-invariant. This proves the upper-radical assertion with its Haar normalization. A trivial radical has mass one and needs no estimate; this also treats \(r=1\). \(\square\)

**Theorem 6.88 — unipotent orbital continuity on the Schwartz algebra.** For any smooth unitary central character and every partition \(\lambda\), formula (6.195) is absolutely convergent for each \(f\in\mathcal S_\omega\). It extends the compact-support orbital measure and satisfies
\[
 \begin{gathered}
 |U_\lambda(f)|\le B_{P_\lambda}p_{a_G}(f),\\
 |U_\lambda(f-f_R)|
       \le B_{P_\lambda}(1+R)^{-A}p_{a_G+A}(f),
 \qquad f_R=1_{\{\sigma\le R\}}f,\quad A\ge0.
 \end{gathered}
\tag{6.198}
\]
The constants here use precisely (6.195); changing an orbital measure multiplies its bounds by the same fixed positive scalar. The cutoff estimate holds for every nonnegative integer exponent. The estimates hold on every fixed Schwartz level.

**Proof.** By \(K\)-bi-invariance of the two weights,
\(|f(knk^{-1})|\le p_{a_G}(f)\Xi(n)(1+\sigma(n))^{-a_G}\).
Integrate and use (6.197). On the tail \(\sigma(n)>R\), use the higher seminorm and take out \((1+R)^{-A}\). This gives the second estimate directly and proves convergence of the compact cutoffs to the integral. For \(\lambda=(1^r)\), the radical is trivial and \(U_\lambda(f)=f(1)\), consistent with both assertions. Central-character functions need only be compactly supported modulo the centre for their cutoffs; the absolute formula defines their orbital integral without choosing a representative of a central coset. \(\square\)

**Corollary 6.89 — discrete-series coefficients on unipotent orbits.** Let \(c(g)=\langle\pi(g)v,w\rangle\) be any smooth coefficient of a discrete series of \(G\). Then
\[
 U_\lambda(c)=
 \begin{cases}
 \langle v,w\rangle,&\lambda=(1^r),\\
 0,&\lambda\ne(1^r).
 \end{cases}
\tag{6.199}
\]
These are absolute orbital integrals with normalization (6.195).

**Proof.** Corollary 6.83 places \(c\) in the Schwartz space for its central character (use the inverse label in the definition of \(\mathcal S_\omega\) when necessary). Theorem 6.88 proves absolute convergence and permits Fubini. If the orbit is nontrivial, its column partition has at least two nonzero columns, so \(P_\lambda\) is proper. For each \(k\), the inner integral in (6.195) is zero by Theorem 6.77, applied to the conjugated smooth vectors. For the trivial orbit the assertion is evaluation at the identity. This uses the vanishing integrated constant term, not the assertion that the proper Jacquet module vanishes. \(\square\)

**Proposition 6.90 — Fourier transforms of the nilpotent measures.** Fix a nontrivial continuous additive character \(\psi\) of \(F\). Use self-dual Haar measure on \(A\) for the reduced-trace pairing and set
\(\widehat\phi(X)=\int_A\phi(Y)\psi(\operatorname{Trd}(XY))dY\).
Choose the measure \(dY\) on \(\mathfrak p_\lambda=\mathfrak n_\lambda^\perp\) dual to the already specified measure on \(\mathfrak n_\lambda\). Then, as distributions on \(A\),
\[
 \widehat\mu_\lambda(\phi):=\mu_\lambda(\widehat\phi)
       =\int_K\int_{\mathfrak p_\lambda}
                    \phi(kYk^{-1})\,dY\,dk.
\tag{6.200}
\]
For \(\lambda\ne(1^r)\), this distribution vanishes on the open elliptic regular set of \(A\), where elliptic means that the element preserves no proper nonzero right \(D\)-subspace.

**Proof.** Here is the needed subspace Fourier identity. Choose an \(F\)-linear complement to \(\mathfrak n_\lambda\), and dual coordinates in \(A\) under the trace pairing. For a compactly supported locally constant test, integrate first over an increasing sequence of compact additive lattices \(L\) in \(\mathfrak n_\lambda\). The character integral over \(L\) is \(\operatorname{vol}(L)\) when the dual coordinate is trivial on \(L\), and zero otherwise: translating by an element on which the character is nontrivial proves the zero assertion. For sufficiently large \(L\), the dual shrinking lattice is contained in the constancy lattice of the test in that coordinate. Its volume is \(\operatorname{vol}(L)^{-1}\) in the paired measures. The integral therefore equals the integral of the test on the zero dual coordinate. The other coordinates give exactly
\[
             \int_{\mathfrak n_\lambda}\widehat\phi(X)dX
                         =\int_{\mathfrak n_\lambda^\perp}\phi(Y)dY.
\tag{6.201}
\]
The Fourier transform of such a test is again compactly supported and locally constant: invariance under a compact open lattice forces its transform into the compact annihilator, while compact support forces a common constancy lattice for the transform. Thus these integrals are finite. Conjugation preserves the trace pairing and additive Haar measure on \(A\). Indeed the determinants of left and right multiplication by the same matrix cancel in their conjugation action. Apply (6.201) to \(\phi\circ\operatorname{Ad}(k)\) and integrate over compact \(K\). This proves (6.200).

Every element of \(k\mathfrak p_\lambda k^{-1}\) preserves the corresponding flag. The union of these subspaces is closed: if \(k_jY_jk_j^{-1}\) converges, compactness of \(K\) gives a convergent subsequence of the \(k_j\), and then of the bounded \(Y_j\); the limit remains in \(\mathfrak p_\lambda\). If \(P_\lambda\) is proper, an elliptic regular element belongs to none of these subspaces. A test supported in that elliptic open set consequently has zero integral in (6.200). No local character expansion or regularity theorem for this Fourier distribution was used or is inferred. \(\square\)

For the split group, Kivinen–Tsai, Definition 2.1 and equations (2.1)–(2.2) in their free author preprint, use the normalization (6.194)–(6.195). The kernel-flag and coordinate-density proof above supplies this formula for division matrix groups and in both field characteristics. It also proves the unipotent Schwartz estimates and coefficient vanishing directly. Section 6.18 proves the compact-support nilpotent and unipotent germ expansions and their scalar homogeneity. The corresponding higher-rank elliptic **semisimple** Schwartz orbital bound, singular-set character integration and elliptic completeness require further arguments.


### 6.18 Compact-support orbital germs and scalar homogeneity

Continue with \(A=M_r(D)\), \(n=rd\), and the nilpotent measures of (6.194). Write \(\mathcal N\) for the nilpotent cone and \(A_{\mathrm{reg}}\) for the regular semisimple set. The reduced characteristic polynomial is
\[
 \operatorname{ch}_X(T)=T^n+a_1(X)T^{n-1}+\cdots+a_n(X),
 \qquad \chi(X)=(a_1(X),\ldots,a_n(X)).
\tag{6.202}
\]
Its coefficients are continuous polynomial functions, \(\chi^{-1}(0)=\mathcal N\), and \(a_i(tX)=t^ia_i(X)\). These statements follow from the splitting-matrix definition and Cayley–Hamilton used in Section 6.1; they require no separability of a nilpotent element. For regular \(X\), use
\(O_X(\phi)=\int_{G_X\backslash G}\phi(g^{-1}Xg)d\dot g\), with \(\operatorname{vol}(K)=1\) and Haar measure on the étale torus \(G_X=F[X]^\times\) giving its maximal compact subgroup volume one. In particular \(X\) and \(tX\), for \(t\ne0\), have exactly the same centralizer and Haar measure. These regular measures and the nilpotent measures remain different normalizations.

**Lemma 6.91 — restriction to a closed fibre.** Let \(q:X\to Y\) be a continuous map of locally compact totally disconnected Hausdorff spaces, and let a group \(H\) act continuously on \(X\), preserving its fibres. For a function \(v\), use \((hv)(x)=v(h^{-1}x)\), and let \(C_c^\infty(X)_H\) be the quotient by the span of \(hv-v\). Suppose \(v\in C_c^\infty(X)\) has zero class after restriction to \(X_y=q^{-1}(y)\). There is a compact open neighborhood \(W\) of \(y\) such that
\[
       1_{q^{-1}(W)}v=\sum_{j=1}^m(h_jv_j-v_j),
                   \qquad v_j\in C_c^\infty(q^{-1}(W)).
\tag{6.203}
\]
For every closed subset \(Z\subset X\), restriction \(C_c^\infty(X)\to C_c^\infty(Z)\) is surjective, with kernel the extension by zero of \(C_c^\infty(X\setminus Z)\).

**Proof.** To prove the restriction assertion, partition the compact support of a test on \(Z\) into finitely many compact open subsets on which it is constant. Each such subset is the intersection with \(Z\) of a compact open subset of \(X\): choose small compact open neighborhoods of its points avoiding the remaining closed part of \(Z\), take a finite cover, and then make the cover disjoint by successive differences. Their characteristic functions extend the test. If an ambient locally constant test is zero on \(Z\), its compact support is disjoint from \(Z\), giving the kernel assertion.

The hypothesis about \(v\) means, by the definition of a linear span, that its restriction is a *finite* sum \(\sum_j(h_jw_j-w_j)\), with \(w_j\in C_c^\infty(X_y)\). Extend each \(w_j\) to a test \(\widetilde w_j\) on \(X\). The test
\(v-\sum_j(h_j\widetilde w_j-\widetilde w_j)\)
vanishes on \(X_y\). Its support \(S\) is compact, so \(q(S)\) is compact and does not contain \(y\). Choose compact open \(W\) disjoint from \(q(S)\). Multiplication by \(1_{q^{-1}(W)}\) commutes with every \(h_j\). The asserted identity follows with \(v_j=1_{q^{-1}(W)}\widetilde w_j\). Their supports are compact because \(q^{-1}(W)\) is closed. \(\square\)

**Lemma 6.92 — all invariant distributions on the nilpotent cone.** With the topology inherited from \(A\),
\[
 \bigl(C_c^\infty(\mathcal N)_G\bigr)^*
          =\bigoplus_{\lambda\vdash r}\mathbb C\mu_\lambda.
\tag{6.204}
\]
Thus the nilpotent orbital measures are a basis of the invariant linear functionals, and the coinvariant space has dimension equal to the number of partitions of \(r\). The same assertions hold for the unipotent cone \(1+\mathcal N\), with the measures \(U_\lambda\).

**Proof.** Theorem 6.86 gives locally finite extensions of all the orbit measures to \(\mathcal N\). This point matters: existence of a measure only on each open orbit would not suffice for the following subtraction argument.

The rank vector \((\operatorname{rank}_D X^i)_{1\le i\le r}\) determines the partition by Lemma 6.85. Rank can only drop in a limit, since rank lower bounds are open minor conditions. Among any remaining finite set of types, pick one whose rank vector is maximal in the coordinatewise order. Its orbit is open in the union of the remaining types: for each other type some rank is smaller, and requiring the selected ranks as lower bounds excludes it. Remove this orbit and repeat. At each stage the remainder is closed in the previous space.

An invariant linear functional on a single homogeneous orbit with an invariant measure is a scalar multiple of that measure. To justify this for all linear functionals, identify the orbit with \(G/H\) and use the averaging map \(p_!F(gH)=\int_HF(gh)dh\) from compact tests on \(G\) to tests on the orbit. Compactly supported local sections, obtained from the Gaussian quotient charts in Lemma 6.85, and a compact test on \(H\) of integral one show that this map is surjective. It commutes with left translation. Composing an invariant functional with it gives a left-invariant functional on compact tests on \(G\). Such a functional is a scalar Haar integral: its values on translates of a compact open subgroup are equal, finite-index subdivisions give their ratios for nested subgroups, and finite coset partitions cover every compact test. Quotient integration then gives the same scalar orbital integral on the surjective image of \(p_!\). The needed centralizer unimodularity and invariant orbit measure were proved in Theorem 6.86.

Restrict an invariant functional on the remaining cone to its selected open orbit, subtract that scalar multiple of \(\mu_\lambda\), and continue on the closed remainder. Lemma 6.91 identifies a functional zero on the open part with a functional on the closed remainder. Finitely many steps express it as a sum of the orbital measures. Applying this procedure to a zero sum proves their linear independence as well. Their common pairing with the coinvariant space separates its points, since every linear functional on that quotient is invariant. Thus that space injects into a finite-dimensional space with these coordinates. Independence makes the coordinate map surjective, so its dimension is precisely the number of partitions. Translation \(X\mapsto1+X\) proves the group assertion. \(\square\)

**Theorem 6.93 — the compact-support germ expansion.** There are conjugation-invariant locally constant functions \(g_\lambda\) on \(A_{\mathrm{reg}}\) such that, for each \(\phi\in C_c^\infty(A)\), a compact open neighborhood \(W_\phi\) of \(0\) in \(F^n\) satisfies
\[
 O_X(\phi)=\sum_{\lambda\vdash r}
                    g_\lambda(X)\mu_\lambda(\phi)
       \quad\bigl(X\in A_{\mathrm{reg}},\ \chi(X)\in W_\phi\bigr).
\tag{6.205}
\]
The functions' germs near the nilpotent fibre are uniquely determined. One neighborhood works for every test in any given finite-dimensional test space.

**Proof.** By Lemmas 6.91–6.92 choose tests \(\phi_\lambda\in C_c^\infty(A)\) with \(\mu_\kappa(\phi_\lambda)=\delta_{\kappa\lambda}\). Define \(g_\lambda(X)=O_X(\phi_\lambda)\).

These regular orbital integrals are finite and locally constant. To obtain this assertion from the proved group version rather than assume it for the Lie algebra, fix a compact test support and a small neighborhood of the chosen \(X\). Choose \(b\in F^\times\) small enough that \(1+bY\) is invertible for every matrix in that support and neighborhood. Then
\(\phi(Y)=f(1+bY)\)
for the compact group test \(f(g)=\phi((g-1)/b)\), extended by zero. The centralizers of \(X\) and \(1+bX\) agree. The properness and uniform fixed-torus assertion of Lemma 6.18, together with the local conjugacy charts of Theorem 6.2, prove the assertion. Explicitly, uniform properness puts all contributing quotient representatives in one compact set; smoothness of \(f\) makes its values unchanged on a sufficiently small torus neighborhood uniformly over that set. The conjugacy chart then gives a neighborhood in the whole regular set. This also proves conjugation invariance with the chosen torus normalization.

Subtract the finite test
\(\sum_\lambda\mu_\lambda(\phi)\phi_\lambda\)
from \(\phi\), and call the difference \(v\). Every nilpotent orbital integral of \(v\) is zero. Lemma 6.92 says precisely that its restriction to \(\mathcal N\) is zero in the coinvariant space. Apply Lemma 6.91 to \(q=\chi\), whose zero fibre is \(\mathcal N\). On \(\chi^{-1}(W_\phi)\), the test \(v\) is a finite sum of conjugation differences. Integration over a regular orbit in that set kills each difference, proving (6.205). All these integrations are of compact tests, so no Schwartz convergence assertion has entered.

If another family gives (6.205), insert the finitely many dual tests \(\phi_\lambda\). It agrees with \(g_\lambda\) on some common neighborhood of the zero fibre in the regular set. This is uniqueness of germs; it does not assert linear independence of their restrictions as functions. Finally intersect the finitely many neighborhoods belonging to a basis of a finite-dimensional test space and use linearity. \(\square\)

**Theorem 6.94 — homogeneous representatives of the germs.** Put
\[
 m_\lambda=\dim_F\mathfrak n_\lambda
       =\frac{d^2}{2}\left(r^2-\sum_i c_i^2\right).
\tag{6.206}
\]
Each germ in Theorem 6.93 has a unique globally defined homogeneous representative \(\Gamma_\lambda\) on \(A_{\mathrm{reg}}\). It is conjugation invariant, locally constant, and satisfies
\[
 \begin{gathered}
 \mu_\lambda(\phi(t\,\cdot))
                     =|t|_F^{-m_\lambda}\mu_\lambda(\phi),\\
 \Gamma_\lambda(tX)=|t|_F^{-m_\lambda}\Gamma_\lambda(X)
                                      \qquad(t\in F^\times).
 \end{gathered}
\tag{6.207}
\]
Formula (6.205) holds with \(\Gamma_\lambda\) in place of \(g_\lambda\), after shrinking its neighborhood if necessary. The exponent uses the half dimension of the orbit; no square root of a scalar in \(F\) is required.

**Proof.** The first identity follows immediately by the change of variables \(Y=tX\) in the radical integral (6.194). Regular orbital measures instead satisfy
\(O_{tX}(\phi)=O_X(\phi(t\,\cdot))\),
since their centralizers and Haar measures are identical. Let \(\varpi=\varpi_F\) and \(q=q_F\). Apply (6.205) to each \(\phi_\lambda(\varpi\,\cdot)\). Their nilpotent integrals are \(q^{m_\lambda}\delta_{\kappa\lambda}\), giving
\(g_\lambda(\varpi X)=q^{m_\lambda}g_\lambda(X)\)
on one sufficiently small common neighborhood.

We also need a neighborhood uniform over all units. Each \(\phi_\lambda\) is supported in a lattice \(M\) and invariant under translation by a smaller lattice \(L\). For sufficiently large \(h\), every \(u\in1+\varpi^h\mathcal O_F\) has \((u-1)M\subset L\) and preserves \(M\). It therefore fixes \(\phi_\lambda\) under scalar substitution, including outside \(M\). The family \(\{\phi_\lambda(u\,\cdot):u\in\mathcal O_F^\times\}\) is consequently finite. Apply (6.205) to this finite family. The first identity of (6.207) makes its dual integrals unchanged, so \(g_\lambda(uX)=g_\lambda(X)\) for every unit on a single common neighborhood.

Inside that neighborhood choose
\(U=\{X:|a_i(X)|_F\le\epsilon^i\text{ for every }i\}\)
for a sufficiently small positive power \(\epsilon\) of \(|\varpi|_F\). It is invariant under units and stable under multiplication by \(\varpi\). The two identities just proved imply the required scalar rule whenever both endpoints lie in \(U\): intermediate powers of \(\varpi\) then stay in \(U\), and negative powers are obtained by reversing the same identities.

For arbitrary regular \(X\), take \(k\) large enough that \(\varpi^kX\in U\), and define
\[
          \Gamma_\lambda(X)=q^{-km_\lambda}
                                      g_\lambda(\varpi^kX).
\tag{6.208}
\]
The relation for one power of \(\varpi\) makes this independent of all sufficiently large \(k\). The unit relation gives (6.207) for every scalar. A fixed \(k\) works on a neighborhood of any given regular \(X\), proving local constancy; conjugation invariance follows likewise. On \(U\) this equals \(g_\lambda\). Any homogeneous function with that germ agrees everywhere after scaling into \(U\), proving uniqueness and independence of the chosen dual tests. \(\square\)

**Corollary 6.95 — group germs, finite packets and a scalar ray.** For each compact group test \(f\), on a sufficiently small invariant neighborhood of the unipotent fibre,
\[
 O_g(f)=\sum_{\lambda\vdash r}
               \Gamma_\lambda(g-1)U_\lambda(f)
                             \qquad(g\in G_{\mathrm{reg}}).
\tag{6.209}
\]
For fixed regular \(X\) and fixed additive compact test \(\phi\), all sufficiently large integers \(k\) satisfy the exact equality
\[
 O_{\varpi^kX}(\phi)=\sum_{\lambda\vdash r}
                q^{km_\lambda}\Gamma_\lambda(X)\mu_\lambda(\phi).
\tag{6.210}
\]
A common neighborhood, or a common sufficiently large \(k\), works for a finite-dimensional space of tests. In particular it works for tests with a common compact support bound and a common additive constancy lattice.

**Proof.** The function \(\phi(Y)=f(1+Y)\), extended by zero where \(1+Y\) is singular, is compactly supported and locally constant on \(A\). The support of \(f\) is a compact subset of the open set \(G\), so this extension is locally zero at the boundary. Equation (6.195) gives \(\mu_\lambda(\phi)=U_\lambda(f)\). The centralizers of \(g\) and \(g-1\) agree. Apply (6.205) to \(\phi\) and use Theorem 6.94. This proves (6.209) without an exponential map. Equation (6.210) follows by scaling into the neighborhood of (6.205) and then applying (6.207). The finite-packet assertion is the last part of Theorem 6.93. A common compact support bound meets only finitely many cosets of a fixed additive lattice, so the specified test space is finite dimensional. \(\square\)

**Example 6.96 — quadratic orders and the rank-two germs.** Let \(D=F\), \(r=2\), and keep precisely the measures above. There are two nilpotent types, \(0=(1,1)\) and \(\mathrm{nil}=(2)\), with \(m_0=0\), \(m_{\mathrm{nil}}=1\). For a split \(X\), let \(x,y\in F\) be its distinct eigenvalues. The three regular types have the following germs:
\[
 \begin{array}{c|c|c}
 &\Gamma_0(X)&\Gamma_{\mathrm{nil}}(X)\\ \hline
 \text{split}&0&|x-y|_F^{-1}\\
 E/F\text{ unramified quadratic}
    &-2/(q-1)&(q+1)|b|_F^{-1}/(q-1)\\
 E/F\text{ ramified quadratic}
    &-1/(q-1)&q|b|_F^{-1}/(q-1)
 \end{array}
\tag{6.211}
\]
In the field cases write \(X=a+b\theta\) in \(E\), where \(\mathcal O_E=\mathcal O_F+\mathcal O_F\theta\), taking \(\theta\) to be a residue-field generator in the unramified case and a uniformizer in the ramified case. Then \(b\ne0\). The formulas hold for separable quadratic fields, including wildly ramified fields and residue characteristic two.

**Proof.** Put \(\phi_R=1_{\varpi^{-R}M_2(\mathcal O_F)}\). From (6.194), \(\mu_0(\phi_R)=1\) and \(\mu_{\mathrm{nil}}(\phi_R)=q^R\). Consequently
\(\phi_{\mathrm{nil}}=(\phi_1-\phi_0)/(q-1)\)
and \(\phi_{0}^\vee=(q\phi_0-\phi_1)/(q-1)\)
are dual tests for the two measures.

In the split case, Gaussian Iwasawa coordinates on \(T\backslash G\) give integration over \(n(z)k\), with \(dz\) of integral volume one and \(dk\) probability measure. The modulus cancels when the diagonal is placed before the upper radical, as in the quotient integration in (6.46). Conjugating \(\operatorname{diag}(x,y)\) by \(n(z)\) gives upper entry \((x-y)z\). Thus, whenever \(\varpi^Rx\) and \(\varpi^Ry\) are integral,
\(O_X(\phi_R)=q^R|x-y|_F^{-1}\).
The two dual tests give the first row near zero, and homogeneity gives it everywhere.

Here is a direct lattice count for the field cases. The stated integral bases exist without a tameness assumption. In the unramified case, independence of \(1,\overline\theta\) over the residue field prevents cancellation of their lowest valuations. In the ramified quadratic case the valuations of \(a\) and \(b\theta\) have different parity, so the same assertion holds with the ramified valuation. These observations show that integral elements have integral coordinates in the respective bases.

Every \(\mathcal O_F\)-lattice in \(E\), up to multiplication by \(E^\times\), is
\(L_i=\mathcal O_F+\varpi^i\mathcal O_F\theta\), for a unique \(i\ge0\). Indeed scale its \(\mathcal O_E\)-saturation to \(\mathcal O_E\), then choose a unit in the lattice and scale it to \(1\). The quotient of the resulting lattice by \(\mathcal O_F\) is an ideal in the rank-one free module \(\mathcal O_E/\mathcal O_F\); subtracting an integral scalar from a lift of its generator gives the displayed form. Its ring of multipliers is \(\mathcal O_i=\mathcal O_F+\varpi^i\mathcal O_E=L_i\): a multiplier must lie there by evaluation on \(1\), and this module is itself a ring. Distinct \(i\) give distinct multiplier rings, proving uniqueness.

The double coset in \(E^\times\backslash G/K\) belonging to \(L_i\) has quotient measure \([\mathcal O_E^\times:\mathcal O_i^\times]\). This follows by quotient integration from \(\operatorname{vol}(K)=\operatorname{vol}(\mathcal O_E^\times)=1\) and stabilizer \(\mathcal O_i^\times\). The index is one at \(i=0\). For \(i\ge1\), reduction modulo \(\varpi^i\mathcal O_E\) gives respectively
\[
 [\mathcal O_E^\times:\mathcal O_i^\times]
   =\frac{(q^2-1)q^{2i-2}}{(q-1)q^{i-1}}
       =(q+1)q^{i-1},
 \qquad
   \frac{(q-1)q^{2i-1}}{(q-1)q^{i-1}}=q^i.
\]
These are just unit counts in the unramified and ramified quotient rings; the ramified residue field has size \(q\), even in the wild case.

Let \(l=v_F(b)\) and take \(R\) large enough that \(\varpi^Ra\) is integral and \(M=R+l\ge0\). The condition \(\varpi^RX L_i\subset L_i\) is exactly \(i\le M\), by the multiplier ring. Therefore
\[
 O_X(\phi_R)=
 \begin{cases}
 1+(q+1)\displaystyle\sum_{i=1}^{M}q^{i-1}
       =\bigl((q+1)q^M-2\bigr)/(q-1),&E/F\text{ unramified},\\
 1+\displaystyle\sum_{i=1}^{M}q^i
       =\bigl(q^{M+1}-1\bigr)/(q-1),&E/F\text{ ramified}.
 \end{cases}
\]
For small \(X\), the dual tests above read off the last two rows of (6.211), since \(q^l=|b|_F^{-1}\). The global homogeneous extension proves the formulas for every regular \(X\) of those types. The two elliptic constant terms differ because the torus Haar measure gives its maximal compact subgroup volume one; it does not give \(E^\times/F^\times\) volume one in both cases. \(\square\)

Kottwitz, §§6.1–6.4 and Lemma 27.1 in the freely accessible Clay article, treats the compact-support localization method. The argument here proves the needed finite-commutator identity and nilpotent-measure input for \(\mathrm{GL}_r(D)\), and derives its scalar factors and group passage directly. Neither the finite-packet neighborhood nor the fixed-ray formula is a uniform assertion for all Schwartz cutoffs. Higher-rank elliptic semisimple Schwartz orbital bounds, singular-set character integration, elliptic completeness and the full higher-degree representation transfer still require proofs.


## 7. Exercises with complete solutions

**Exercise 7.1 — an unramified quadratic field.** Let \(K/\mathbb Q_p\) be the unramified quadratic extension. Choose \(\xi\in\mathcal O_K^\times\) whose residue generates \(\mathbb F_{p^2}/\mathbb F_p\). Write explicitly the matching matrix and quaternion class, and their centralizers.

**Solution 7.1.** Let \(\sigma\) be the nontrivial automorphism, \(t=\xi+\sigma\xi\), and \(n=\xi\sigma\xi\). The reduction of \(T^2-tT+n\) is irreducible and separable, so its lift is irreducible over \(\mathbb Q_p\). In the cyclic model
\[
D_p=K\oplus K\Pi,\qquad \Pi^2=p,\qquad
\Pi a=\sigma(a)\Pi,
\]
the element \(\xi\) has that reduced polynomial. The matching matrix is \(\left(\begin{smallmatrix}0&-n\\1&t\end{smallmatrix}\right)\), the matrix of multiplication by \(\xi\) on \(K\) in the basis \(1,\xi\). Its centralizer is the multiplication copy of \(K^\times\); the quaternion centralizer is also \(K^\times\), by Theorem 1.1. Conjugation by \(\Pi\) exchanges \(\xi\) and \(\sigma\xi\), so either root defines the same class. This remains valid at \(p=2\), because unramified residue extensions are separable.

**Exercise 7.2 — check the Steinberg character.** Verify (2.3) for the trivial representation of \(D^\times\) and the Steinberg representation of \(G\), including an unramified unitary character twist.

**Solution 7.2.** An elliptic matrix has no invariant \(F\)-line. Proposition 2.2 consequently gives zero character for \(C^\infty(\mathbb P^1(F))\) on the elliptic regular set. Subtracting the character one of its constant subrepresentation gives \(\Theta_{\mathrm{St}}=-1\). The trivial quaternion character is one, proving the required minus sign. Under a twist, the left side becomes \(-\chi(\det g)\), while the quaternion side becomes \(\chi(\operatorname{nrd}b)\). The determinants and norms match by Theorem 1.1, so the negative relation persists. The central characters are both \(\chi(z^2)\). The same computation in fact works for any quasicharacter; unitarity only ensures that the twist belongs to the discrete-series set in (2.2).

**Exercise 7.3 — three dimensions.** Evaluate both sides of (4.3) for \(p=11,13,37\), showing the mass and elliptic corrections.

**Solution 7.3.** The complete substitutions are:

| \(p\) | \((s_4,s_3)\) | mass \((p-1)/12\) | class-number corrections | \(h\) | genus \((p+1)/12-e_2/4-e_3/3\) |
|---:|:---:|---:|:---:|---:|:---:|
| 11 | \((-1,-1)\) | \(5/6\) | \(1/2+2/3\) | 2 | \(1-0-0=1\) |
| 13 | \((1,1)\) | \(1\) | \(0+0\) | 1 | \(7/6-1/2-2/3=0\) |
| 37 | \((1,1)\) | \(3\) | \(0+0\) | 3 | \(19/6-1/2-2/3=2\) |

In each row the last column is \(h-1\), and equals \(\dim S_2\) by the differential dictionary. In particular the level-thirteen quaternion class space consists only of constants and has no cusp line.

**Exercise 7.4 — what transfers at the identity?** Explain how the local minus sign fits the identity contribution of the compact trace formula. Specify the analytic transfer input and why global multiplicities remain positive.

**Solution 7.4.** A scalar has a repeated characteristic-polynomial root and is not regular. Thus the identity conjugacy class is outside Theorem 1.1 and cannot be used as an extra regular matching class. What the transfer theorem provides is the identity-*value* relation (3.4): with its paired Haar measures, \(f'(1)=-f(1)\). Lemmas 2.11 and 2.20 prove this identity-value relation for every finite and real matching pair in the explicit paired measures. Theorem 2.22 and Corollary 2.31 prove the real and finite negative spectral identity (3.5), respectively; Lemmas 2.19 and 2.27 justify integration on tests meeting singular classes. Arthur, Lemma 25.2 and Theorem 25.1(b), provides a source comparison.

For a compact quotient, Lesson 18 gives the identity term \(\operatorname{vol}(X)f(1)\). The orbital integral itself is \(f(1)\), while the quotient volume is its geometric coefficient; they must not be conflated. Replacing the locally transferred identity value introduces the sign prescribed by (3.4). This accounts for that contribution once transfer has been established; the compact formula alone does not establish transfer or force a local sign. Proposition 2.2 independently checks the sign in the simplest representation. Lemma 3.2 proves that the two global quotient volumes in these paired measures both equal \(1/6\). At two ramified places, Lemma 3.3 gives zero averaged constant term. Theorem 3.4 then cancels the split semisimple weighted terms, the unipotent finite part, the continuous logarithmic derivative and its reflected endpoint. Determinant characters remain in the split discrete trace and correspond to norm characters in Section 3.6. Finally, the ramification set has even cardinality. The product of the local minus signs is one, by (3.6); Theorem 3.5 gives an equality of full discrete traces and Lemma 3.6 gives positive equal multiplicities.

**Exercise 7.5 — an explicit Schwartz convolution constant.** In Example 6.84 put \(Z_j=\sum_{n\ge1}n^{-j}\), \(j=2,3,4\), and \(\beta=(q-1)/(q+1)\). Express \(C_4\) in these three convergent series. Give a numerical upper bound for the error after truncating its radial integral at \(\sigma\le R\), and state the resulting convolution estimate.

**Solution 7.5.** Set \(n=k+1\) in (6.192). Then \(1+\beta k=\beta n+(1-\beta)\), so direct expansion gives
\[
 C_4=1+\frac{q+1}{q}\left[
 \beta^2(Z_2-1)+2\beta(1-\beta)(Z_3-1)
                         +(1-\beta)^2(Z_4-1)\right].
\]
Each series converges by comparison with \(\int_1^\infty x^{-j}dx\). Its omitted terms start at \(n>R+1\). For integer \(R\ge0\), monotonicity of \(x^{-j}\) bounds that series tail by \((R+1)^{1-j}/(j-1)\). Therefore, writing \(C_4(R)\) for the integral on \(\sigma\le R\),
\[
 0\le C_4-C_4(R)\le\frac{q+1}{q}\left[
 \frac{\beta^2}{R+1}+\frac{\beta(1-\beta)}{(R+1)^2}
                       +\frac{(1-\beta)^2}{3(R+1)^3}\right].
\]
Theorem 6.81 now reads \(p_N(f_1*f_2)\le C_4p_{N+4}(f_1)p_N(f_2)\) in this rank-two normalization. Any computed partial sum plus the displayed error is an explicit admissible upper bound for that constant; no evaluation of the \(Z_j\) in terms of other constants is needed.


**Exercise 7.6 — a kernel flag and orbital homogeneity.** Take \(r=6\) and nilpotent Jordan type \(\lambda=(3,2,1)\) over \(D\). Find the flag in Theorem 6.86, the centralizer and orbit dimensions over \(F\), and the dimension of its cotangent fibre. For \(a\in F^\times\), determine \(\mu_\lambda(\phi(a\,\cdot))\) and \(\widehat\mu_\lambda(\phi(a\,\cdot))\). Evaluate the corresponding unipotent orbital integral of a smooth discrete-series coefficient.

**Solution 7.6.** The columns are \((3,2,1)\), so the flag dimensions over \(D\) are \(3,5,6\). The flag is exactly \(\ker X\subset\ker X^2\subset\ker X^3=V\): if any flag of those dimensions is lowered by \(X\), its \(i\)-th space lies in \(\ker X^i\) and has the same dimension. The commuting algebra has \(F\)-dimension \((3^2+2^2+1^2)d^2=14d^2\), and its unit group is the centralizer. The orbit dimension is \((36-14)d^2=22d^2\). The flag and its cotangent fibre both have dimension \((3\cdot2+3\cdot1+2\cdot1)d^2=11d^2\).

Changing variables \(Y=aX\) in (6.194) gives
\[
 \mu_\lambda(\phi(a\,\cdot))=|a|_F^{-11d^2}\mu_\lambda(\phi).
\]
The parabolic Lie algebra in (6.200) has dimension \((36-11)d^2=25d^2\). Changing variables there gives
\[
 \widehat\mu_\lambda(\phi(a\,\cdot))
                =|a|_F^{-25d^2}\widehat\mu_\lambda(\phi).
\]
These exponents come from additive \(F\)-dimensions; they require no exponential map or factorial. Finally the parabolic has three blocks and is proper. Equations (6.195), (6.197) and Theorem 6.77 show that the coefficient's orbital integral is absolutely convergent and zero, with any Haar normalization on this nontrivial orbit. \(\square\)


**Exercise 7.7 — equal homogeneity degrees.** In \(M_6(D)\), compare the nilpotent types \(\lambda=(3,3)\) and \(\nu=(4,1,1)\). Compute their column partitions, centralizer dimensions and scalar homogeneity degrees. Can scalar dilates of one compact test distinguish the two orbital functionals? Explain what tests the germ construction supplies instead.

**Solution 7.7.** The columns are \((2,2,2)\) and \((3,1,1,1)\). Both squared sums are \(12\), so both centralizers have \(F\)-dimension \(12d^2\), both orbits have dimension \((36-12)d^2=24d^2\), and both degrees in (6.206) are \(12d^2\). They are distinct orbits: their first kernel dimensions are \(2\) and \(3\), respectively.

For any one test \(\phi\), its scalar dilates have the two orbital coordinates
\[
 \bigl(\mu_\lambda(\phi(t\,\cdot)),\mu_\nu(\phi(t\,\cdot))\bigr)
      =|t|_F^{-12d^2}
                         \bigl(\mu_\lambda(\phi),\mu_\nu(\phi)\bigr).
\]
Thus the coordinate vectors of all such dilates span a space of dimension at most one. Scalar sampling of that test cannot recover two independent orbital coordinates. If both coordinates vanish, it recovers neither. If they do not both vanish, the nonzero invariant functional
\(\mu_\nu(\phi)\mu_\lambda-\mu_\lambda(\phi)\mu_\nu\)
annihilates every scalar dilate, while Lemma 6.92 shows that this functional is not zero.

Theorem 6.93 instead supplies a finite collection of dual tests, including tests with coordinates \((1,0)\) and \((0,1)\) on these two measures and zero on every other nilpotent type. The compact-support expansion is uniform on their finite span. The coincidence of the two homogeneity degrees does not collapse these orbital coordinates and does not prove or disprove linear independence of the regular germ functions. \(\square\)


## 8. Proofs and prerequisites

The class matching is fully proved in Theorem 1.1, the trivial/Steinberg character calculation in Proposition 2.2, the complete real local correspondence in Lemmas 2.3–2.4 and Theorem 2.5, and the all-prime dimension equality in Theorem 4.2. Lemma 2.6, Theorem 2.7 and Proposition 2.8 prove the finite-place regular character theorem, including compact split elements, in all characteristics. They include the exact tree complex, uniform fixed-tube trace stabilization, principal/special character formulas and finite elliptic compact-type sum. Section 2.4 proves finite-place smooth transfer, including the inseparable support needed in characteristic two, by the signed Euler test and the exact orbital-coordinate lift. Lemma 2.11 proves the full two-term scalar orbital germ and the negative scalar-value identity for every matching pair. Proposition 2.12 proves the paired formal degree for special representations. Lemma 2.13, Theorem 2.14 and Corollary 2.15 prove the whole depth-zero local bijection, its negative character identity on every regular elliptic class, paired formal degrees, and every determinant/norm twist of that family. The finite-tree character argument includes deep scalar-residue classes and all residue characteristics. Theorem 2.16 proves the full Schur constant for every irreducible admissible compact induction, Corollary 2.17 computes the division degree and reduces equality to an explicit dimension-volume identity, and Proposition 2.18 calculates the unramified and ramified inducing volumes in every characteristic. Theorem 2.30 proves the all-level bijection, character identity and paired type dimensions by the quaternion construction and elliptic orthogonality. Lemmas 2.19–2.21 and Theorem 2.22 prove real character integration across the singular set, the scalar-value identity for every matching pair, and real smooth/spectral transfer with common-support polynomially bounded wave tests. The Gaussian orbital example computes the scalar sign directly. Sections 2.8–2.10 supply the full finite representation construction, arbitrary-test character integration, Fourier comparison, elliptic orthogonality, all-level bijection, full factor and formal-degree equality, and every-pair spectral transfer. Sections 3.3–3.6 prove the full global quaternion correspondence over \(\mathbb Q\): equal paired volumes, absolute discrete traces, the truncated-kernel comparison, cancellation of the split/unipotent/continuous terms, the residual characters, and positive outside trace separation. The real proof includes the principal/complementary square-integrability exclusions, a trace-class regularization of the disk character and explicit paired formal degrees (2.23)–(2.24). Both level examples, the order calculation, the Brandt matrices and all seven exercise solutions include their computations. Sections 6.16–6.18 give the Schwartz trace calculus, explicit nilpotent and unipotent orbital measures, unipotent orbital continuity, compact-support germ expansions and scalar homogeneity. Exercises 7.6–7.7 compute division-matrix kernel flags and explain coincident homogeneity degrees. Corollary 4.1 is deduced from the proved global theorem and earlier course results; the independent dimension calculation is not substituted for the theorem.

The following references specify the prerequisites and related treatments:

- Local quadratic embedding: Voight, Corollary 13.4.5; Skolem–Noether and double centralizer: NOE-HYP-04, Theorems 2.1 and 3.1. The real quadratic embedding is explicit in \(\mathbb H\).
- Local Jacquet–Langlands: Jacquet–Langlands, Theorem 15.1 and Proposition 15.5; Deligne, §3.2.8; positive characteristic: Badulescu, Theorem 1.1. The finite-place regular character theorem, recalled in Badulescu–Roche, §2.5 before Theorem 2.5, is proved here in Theorem 2.7. The real/tempered transfer formulation is Arthur, §25, Theorem 25.1. Theorem 2.14 and Corollary 2.15 prove the finite local bijection and paired formal degrees for the entire depth-zero family and all its determinant/norm twists; Proposition 2.12 proves the special case. Theorem 2.16 and Proposition 2.18 prove every compact-induction formal degree and both positive-level inducing volumes. Sections 2.8–2.10 prove all positive-level cases, their general correspondence, full elliptic character identity and the dimension identity (2.64), including primitive residue-characteristic-two types. Lemma 2.27 proves the full finite character distribution, not only its regular restriction. The real local bijection and formal degrees are proved in Section 2.2.
- Finite-place smooth test transfer and scalar identity values are proved in Theorem 2.10 and Lemma 2.11 in every characteristic. Real smooth/scalar/spectral transfer and real arbitrary-test character integration are proved in Lemmas 2.19–2.21 and Theorem 2.22. Arthur, Theorem 25.1(a)–(b) and Lemma 25.2, gives a related treatment; Corollary 2.31 supplies the finite general spectral assertion using the full own character proof. The invariant comparison reference is Theorems 25.5–25.6 and equation (25.28). Our Theorem 3.4 proves the needed noncompact comparison through the piecewise truncated kernel and the exact Maass–Selberg identity; Theorem 3.5 combines it with the compact formula.
- The full global discrete-spectrum theorem, with real ramification: Badulescu–Renard, §18.1, Theorem 18.1, with introductory Theorem 1.4, in the author preprint. Its residual-spectrum discussion is Proposition 18.2. Historical quaternion references are Jacquet–Langlands, Theorems 14.4 and 16.1, with the qualifications described in Section 3. The rational-field quaternion theorem used here is proved in Lemmas 3.2–3.3, Theorems 3.4–3.5 and Lemma 3.6. The higher-degree scope of the modern theorem remains separately assigned in Section 6.
- Genus-zero \(X(1)\), branching and Riemann–Hurwitz: Modular curves and their genus, Lemma 3.1, Proposition 3.2 and Section 3; holomorphic differentials and their dimension: Dimension formulas for congruence subgroups, Theorems 2.1 and 4.1. General Riemann–Hurwitz and Riemann–Roch are background theorems stated there.
- Quaternion reciprocity, orders, ideal classes and the norm-count/Hecke rules: Lesson 17, Sections 2–5. The mass formula is proved in Lesson 17, Theorem 4.3; the full-norm Eichler expression and class-number evaluation were proved in Lesson 18, Theorem 5.3 and equation (6.3).
- Classical/adelic and local fixed-line inputs: Lesson 2, Theorem 4.1; Lesson 8, Theorems 2.1, 3.2, 4.3 and 5.1; Lesson 11, Theorem 7.1; Lesson 13, Theorems 3.2 and 4.1. The discrete spectrum, global genericity and multiplicity inputs are Lessons 12, 14 and 15. The exceptional induction sequence used in (2.9) is Lesson 7, Theorem 4.2.
- Higher-degree local transfer: Arthur, Theorem 25.1; Badulescu 2002, Theorem 1.1. Function-field global transfer and multiplicity one: Badulescu–Roche, Theorems 2.5, 3.2–3.3, with the central quotient explained in §§3.2–3.3. Hodge/cohomological realizations are discussed, rather than proved or used, in Ichino–Prasanna's introduction.

## References

- R. E. Kottwitz, “Harmonic Analysis on Reductive p-adic Groups and Lie Algebras,” in *Harmonic Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics Proceedings 4 (2005), 393–522, §§6.1–6.4 and Lemma 27.1. [Freely accessible Clay volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip04c.pdf). Section 6.18 proves the required compact-support localization and germ expansions, and derives scalar homogeneity and the group passage for division matrix groups in either field characteristic.

- O. Kivinen and C.-C. Tsai, “Shalika germs for tamely ramified elements in GL_n,” arXiv:2209.02509v3, Definition 2.1 and equations (2.1)–(2.2). [Free author preprint](https://arxiv.org/html/2209.02509v3). Section 6.17 proves the orbital-measure formula and the required unipotent bounds directly for division matrix groups in both field characteristics.

- H. Jacquet and R. P. Langlands, *Automorphic Forms on GL(2)*, LNM 114, 1970, §§14–16, especially Theorems 14.4, 15.1, 16.1 and Proposition 15.5. [IAS edition](https://publications.ias.edu/sites/default/files/automorphic-forms-on-gl2_rpl.pdf).
- J. Voight, *Quaternion Algebras*, GTM 288, 2021, Chapters 25 and 41; Corollary 13.4.5, Theorem 25.3.15, §§41.1–41.5. [Open-access book](https://jvoight.github.io/quat.html).
- J. Arthur, “An introduction to the trace formula,” in *Harmonic Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics Proceedings 4, 2005, §25. [Clay volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip04c.pdf).
- P. Deligne, “Formes modulaires et représentations de GL(2),” 1973, §3.2.8. [IAS author archive](https://publications.ias.edu/node/366). Its paired measures and character normalization agree with Section 2.
- A. I. Badulescu, “Correspondance de Jacquet–Langlands pour les corps locaux de caractéristique non nulle,” *Annales scientifiques de l'École Normale Supérieure* **35** (2002), 695–747, introduction and Theorem 1.1. [Journal article](https://www.numdam.org/item/ASENS_2002_4_35_5_695_0/).
- A. I. Badulescu and D. Renard, “Unitary dual of GL(n) at archimedean places and global Jacquet–Langlands correspondence,” *Compositio Mathematica* **146** (2010), 1111–1161. The theorem numbers here refer to the author preprint, §§16–19, especially Theorems 1.4 and 18.1. [Author preprint](https://arxiv.org/abs/0905.4143).
- A. I. Badulescu and P. Roche, “Global Jacquet–Langlands correspondence for division algebras in characteristic p,” revised preprint, 2014, §§2.5 and 3.2–3.4. [Full text](https://arxiv.org/html/1302.5289v2).
- A. Ichino and K. Prasanna, *Hodge classes and the Jacquet–Langlands correspondence*, introduction. Its geometric realizations use an already established automorphic correspondence. [Author preprint](https://arxiv.org/abs/1806.10563).

- J.-P. Gazeau, M. A. del Olmo and H. Pejhan, “Holomorphic Discrete Series of SU(1,1): Orthogonality Relations, Character Formulas, and Multiplicities in Tensor Product Decompositions,” 2025, Section II, equations (8)–(9), and Section IV, equation (22). [Author preprint](https://arxiv.org/html/2504.03901v1). Used for a source comparison of the disk model and the opposite rotation convention; Section 2.2 supplies its own trace-class proof.

- R. Meyer and M. Solleveld, “Resolutions for representations of reductive p-adic groups via their buildings,” 2009 author preprint, Definition 2.1, Lemma 2.6, Theorems 2.4 and 2.12, and Proposition 4.1. [Author PDF](https://www.math.ru.nl/~solleveld/Resolutions.pdf); [arXiv record](https://arxiv.org/abs/0902.4856). Section 2.3 gives the rank-two group identities and exact tree argument directly, and proves uniform compact-split stabilization before deducing the regular character function. Section 6.11 proves the all-rank division-lattice enclosure, face identities, finite support projections, cofinal convex exhaustions and uniform elliptic fixed-simplex finiteness; its finite alternating trace is distinguished from the character-density assertion.

- J. Cohen, “Transfer of Representations and Orbital Integrals for Inner Forms of GL_n,” *Canadian Journal of Mathematics* **70** (2018), 595–627, Section 8.2.1, Proposition 8.6. [Publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/701F58A4E45B1986A4CF2EC8DF09097F/S0008414X00055346a.pdf/transfer-of-representations-and-orbital-integrals-for-inner-forms-of-gln.pdf). This supplies a higher-rank Euler-test comparison. Section 2.4 independently proves the rank-two full signed-edge version with its own explicit paired measures.

- A. Deitmar, “Euler–Poincaré functions,” Section 4. [Author preprint](https://arxiv.org/abs/math/0201233). The adjacent-weight construction in Section 2.7 includes its wave kernel and support estimates.

- W. Casselman, *Introduction to admissible representations of p-adic groups*, Chapter II, “Smooth representations,” revision of 16 June 2019, §§9–10, especially Proposition II.10.2 and Lemma II.10.4. [Author notes](https://personal.math.ubc.ca/~cass/research/pdf/Smooth.pdf). Section 6.5 proves its coefficient, formal-degree and finite trace-test assertions directly.

- W. Casselman, *Introduction to admissible representations of p-adic groups*, Chapter III, “Induced representations and the Jacquet module,” revision of 29 April 2019, §§3–5, especially Lemmas III.5.2–III.5.4. [Author notes](https://personal.math.ubc.ca/~cass/research/pdf/Jacquet.pdf). Section 6.6 gives the Gaussian factorization, normalized projection, Jacquet-vanishing and orbital arguments used here.

- W. Casselman, *Introduction to the Theory of Admissible Representations of p-adic Reductive Groups*, draft of 1 May 1995, §§4.1–4.4, especially Proposition 4.2.3, Theorem 4.2.4, Corollary 4.2.5, Theorems 4.3.3 and 4.4.6, and §§5.2–5.3. [Freely available author draft](https://personal.math.ubc.ca/~cass/research/pdf/p-adic-book.pdf). Sections 6.7–6.8 prove the Jacquet, compactness and integrability criteria, canonical pairing and coefficient asymptotics for division matrix groups directly.

- W. Casselman, “Characters and Jacquet Modules,” *Mathematische Annalen* **230** (1977), 101–105, §§2–5. [Freely accessible article](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0230/LOG_0024.pdf). Section 6.10 proves the adapted-order construction, exact positive-power traces and local character descent, including the zero-Jacquet and minimal-Levi applications.

- E. Opdam and M. Solleveld, “Resolutions of tempered representations of reductive p-adic groups,” arXiv:1203.1237v2, Section 2, Theorem 2.2 and formulas (7)–(11). [Free author preprint](https://arxiv.org/html/1203.1237v2). Section 6.12 supplies its scalar enclosure contraction and invariant-chain argument, and proves the global resolution and fixed-central-character Euler–Poincaré trace and orbital identities.

- E. Grosse-Klönne, “Acyclic coefficient systems on buildings,” arXiv:1408.3349v1, Sections 1 and 3, especially Theorem 1.7 and Lemma 3.1/Theorem 3.2. [Free author preprint](https://arxiv.org/html/1408.3349v1). Section 6.13 proves the division-lattice height and intersection statements, local commuting-average relations, finite convex exactness and the elliptic character trace formula.

- R. Meyer and M. Solleveld, “Characters and growth of admissible representations of reductive p-adic groups,” author preprint, arXiv0908.1489v3, 2016, Section 7, especially Theorems 7.2–7.5. [Free full text](https://arxiv.org/html/0908.1489v3). Section 6.14 proves regular-set local constancy by uniform centralizer-orbit control and finite cellular traces, and supplies the Jacquet descent and character operations used here.

- J.-L. Waldspurger, “La formule de Plancherel pour les groupes p-adiques, d’après Harish-Chandra,” *Journal of the Institute of Mathematics of Jussieu* **2** (2003), 235–333, Lemmas II.1.1, II.1.3–II.1.5, §§II.3–II.4, §III.6 and the opening of §III.7. [Freely accessible full text](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FF540ECB59B31AFC0A7874C87F54EE0A/S1474748003000082a.pdf/la-formule-de-plancherel-pour-les-groupes-p-adiques-dapres-harish-chandra.pdf). Section 6.15 supplies the lattice-height, spherical and unipotent estimates used here; Section 6.16 proves the Schwartz calculus and tempered trace extension.

- I. N. Bernstein and A. V. Zelevinsky, “Induced representations of reductive p-adic groups. I,” *Annales scientifiques de l’École Normale Supérieure*, fourth series, **10** (1977), 441–472, §5 and §6.4. [Author-hosted full text](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BZ-induced-1.pdf). Lemma 6.74 gives the required principal-series support filtration, fibre integration and modulus factors.
