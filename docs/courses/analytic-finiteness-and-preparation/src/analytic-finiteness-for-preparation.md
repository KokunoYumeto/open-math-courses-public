# Analytic finiteness for preparation

*Human treatment: Guillaume Valette, [On subanalytic geometry](https://arxiv.org/abs/2507.23622v1), arXiv:2507.23622v1, 31 July 2025, §1.3.2, §§1.4–1.5, the preliminaries in §1.6.1, Proposition 1.6.12, Lemma 1.6.13, Proposition 1.6.14, the dimension induction and cell/preparation theorems in §§1.7–1.8, and the one-variable and parameterized Puiseux results. Adapted by GPT-6.1 Sol (OpenAI), Ultra, October 2026. This adapted component is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); Guillaume Valette remains the author of the underlying exposition. Changes: notation and Markdown/MathML formatting; the algebra prerequisites and degree-zero case are proved; the module and prescribed-jet versions of the formal linear argument are expanded; real Noetherianity is obtained from the course's existing division proof; the normalizing parameters are allowed either sign, and the uniform derivative bound is proved. Further additions prove independent-variable convergence of the analytic split, localize on the actual compact image, and give a signed balanced-coordinate substitution under the stated cell-induction inputs. Further proof expansions give bounded-monomial unit representations, compact-domain substitution, common translations, dominance, positive and negative power-coordinate pullbacks, and the complete ordinary polynomial reduction. The simultaneous dimension induction is completed below. Further expansions specify the projective product convention, prove elementary witness operations and the bounded local comparison, and supply parameter convergence and the two-sided even-power substitution. These changes imply no endorsement.*

The preparation argument for subanalytic functions needs more than the preparation of a single regular germ. A function \(\psi(u,z)\) can vanish identically in \(z\) on some parameter fibres. We prove that finitely many coefficient germs nevertheless control it:

\[
\psi(u,z)=\sum_{i=0}^{d}c_i(u)(z-z_0)^i A_i(u,z),
\qquad A_i(u_0,z_0)=1.
\]

The \(c_i\) are its actual Taylor coefficients in \(z-z_0\), and the \(A_i\) are convergent analytic units. We then normalize this finite family to obtain an analytic family whose order in \(z\) is uniformly bounded. The later sections prove the unit and coordinate preliminaries and ordinary nondegenerate analytic preparation, with the lower-dimensional induction explicit. The later sections complete the two-coordinate assembly, joint dimension induction, global cell and preparation theorems, complement theorem and convergent Puiseux results.

## Real analytic division and finite generation

Write

\[
R_n=\mathbb R\{x_1,\ldots,x_n\},\qquad
\mathfrak m_n=(x_1,\ldots,x_n).
\]

These are germs at zero; translation gives the same statements at any real point. A germ is a unit precisely when its constant term is nonzero. One direction follows by evaluation. In the other direction the reciprocal of a nonvanishing analytic representative is analytic. Thus \(R_n\) is local, with maximal ideal \(\mathfrak m_n\). The displayed generators of this ideal follow by grouping a convergent series with zero constant term according to the first variable appearing in each monomial; the resulting \(n\) series converge on a smaller polydisc.

The course already contains the full complex preparation and Cauchy division argument, adapted from Jean-Pierre Demailly, in [Preparation by the zeros in one fibre](../weierstrass-preparation-and-division.html#preparation-by-the-zeros-in-one-fibre) and [Division, finite generation and elementary algebra](../weierstrass-preparation-and-division.html#division-finite-generation-and-elementary-algebra). Demailly's treatment remains under his [custom OpenContent grant](https://www-fourier.univ-grenoble-alpes.fr/~demailly/documents.html), as identified in that lesson. We reuse that existing provider by reference.

Here is the additional real argument. Complexify the convergent real series. If a real germ is regular of order \(s\) in the last variable, complex preparation gives its unique monic Weierstrass polynomial \(P\) and unit. Conjugating every coefficient gives another preparation of the same germ. Uniqueness makes both factors real. Similarly, the unique division

\[
f=qP+\sum_{j=0}^{s-1}r_j(x')x_n^j
\]

is fixed by coefficient conjugation when \(f\) and \(P\) are real. It therefore supplies division in \(R_n\), with \(r_j\in R_{n-1}\). A nonzero real homogeneous polynomial has a real vector at which it is nonzero: successive consideration as a polynomial in one variable proves that a polynomial vanishing everywhere on \(\mathbb R^n\) has every coefficient zero. Choose such a vector for the first nonzero homogeneous term. A real linear change of coordinates then makes the germ regular in the last variable.

We record the module argument used here and below. Over a Noetherian ring \(R\), every submodule of \(R^s\) is finitely generated. Induct on \(s\). Project a submodule onto its last coordinate. The image is a finitely generated ideal; lift a finite set of its generators. The kernel is a submodule of \(R^{s-1}\) and has finite generators by induction. Those lifts together with the kernel generators generate the original submodule. Any finite \(R\)-module is a quotient of \(R^s\), so the inverse image under this quotient proves the same assertion for its submodules.

**Noetherianity of real convergent germs.** Induct on \(n\), starting with the field \(R_0=\mathbb R\). If \(J\subset R_n\) is a nonzero ideal, choose a nonzero element, make it regular by a real coordinate change, and prepare it. Its unit is invertible, so its monic polynomial \(P\) belongs to \(J\). Division by this *fixed* polynomial sends \(J\) to an \(R_{n-1}\)-submodule of \(R_{n-1}^s\). Choose finitely many remainders \(r_1,\ldots,r_k\) generating that submodule. Each remainder is in \(J\), since it is \(f-qP\) for an \(f\in J\). For any \(f\in J\), express its remainder as an \(R_{n-1}\)-linear combination of these \(r_i\). The division identity then writes \(f\) in the ideal generated by \(P,r_1,\ldots,r_k\). The zero ideal needs no generators. Hence every ideal of \(R_n\) is finitely generated. \(\square\)

Using a single regular polynomial and division is essential to this proof. Preparation of individual germs in a preassigned direction alone does not justify generation of an arbitrary ideal by polynomials in that direction.

## Polynomial rings and stable filtrations

First we supply the algebra used in Valette's finiteness proof.

**Hilbert basis theorem.** If \(R\) is Noetherian, so is \(R[T]\).

**Proof.** Let \(J\) be a nonzero polynomial ideal. Its leading coefficients, together with zero, form an ideal of \(R\): to add two of them, multiply the corresponding polynomials by powers of \(T\) to align their degrees. Choose polynomials \(f_1,\ldots,f_k\in J\) whose leading coefficients generate this ideal, and put \(d=\max\deg f_i\). For \(f\in J\) of degree \(N\ge d\), subtract an \(R\)-linear combination of \(T^{N-\deg f_i}f_i\) with the same leading coefficient. This lowers the degree. Repetition terminates with a polynomial of degree less than \(d\). The polynomials in \(J\) of degree less than \(d\) form a submodule of \(R^d\), and hence have finitely many module generators \(h_j\). The \(f_i,h_j\) generate \(J\) as an ideal. If \(d=0\), the reduction has zero remainder. The zero ideal is already finite. Induction proves the assertion for finitely many polynomial variables. Any quotient of such a ring is also Noetherian, by taking inverse images of ideals. \(\square\)

Let now \(R\) be Noetherian, \(I\) an ideal, and \(M\) a finite \(R\)-module. An **\(I\)-filtration** is a decreasing sequence of submodules \(M_i\subset M\), indexed by \(i\ge0\), with \(IM_i\subset M_{i+1}\). It is **stable** if \(IM_i=M_{i+1}\) for all sufficiently large \(i\). Introduce the Rees ring and module

\[
\mathcal R(I)=\bigoplus_{i\ge0} I^iT^i,\qquad
\mathcal R(M_*)=\bigoplus_{i\ge0} M_iT^i .
\]

Here \(I^0=R\), and each element has finitely many homogeneous terms. If \(a_1,\ldots,a_\ell\) generate \(I\), the map

\[
R[Z_1,\ldots,Z_\ell]\longrightarrow \mathcal R(I),
\qquad Z_j\longmapsto a_jT
\]

is surjective. The Hilbert basis theorem makes \(\mathcal R(I)\) Noetherian.

**Stable-filtration criterion.** \(\mathcal R(M_*)\) is a finite \(\mathcal R(I)\)-module if and only if \(M_*\) is stable.

**Proof.** A finite set of polynomial generators can be replaced by all its homogeneous components. Those components are still in the Rees module, include a generating set, and are finite in number. Let their degrees be at most \(d\). Compare homogeneous terms of degree \(i+1\), where \(i\ge d\). A generator \(aT^e\), \(e\le d\), has coefficient in \(I^{i+1-e}\) in such an expression. Because

\[
I^{i+1-e}=I\,I^{i-e},\qquad I^{i-e}M_e\subset M_i,
\]

its contribution is in \(IM_i\). Hence \(M_{i+1}\subset IM_i\), and the reverse inclusion is the filtration condition.

Conversely, if \(IM_i=M_{i+1}\) for \(i\ge d\), then \(M_j=I^{j-d}M_d\) for \(j>d\). Each \(M_i\) is finite, by the module argument above. Choose its generators in every degree \(0,\ldots,d\). They generate the entire Rees module. Degree zero is included also when stability starts immediately. \(\square\)

If \(N\subset M\) and \(M_*\) is stable, then

\[
\mathcal R((N\cap M_i)_i)\subset\mathcal R(M_*)
\]

is a submodule over the Noetherian ring \(\mathcal R(I)\). It is finite, so the criterion proves that \((N\cap M_i)_i\) is stable. Taking \(M_i=I^iM\) gives the following form of **Artin–Rees**:

\[
N\cap I^{i+1}M=I(N\cap I^iM)\qquad(i\ge d)
\]

for some \(d\). In particular,

\[
N\cap I^iM=I^{i-d}(N\cap I^dM)\qquad(i\ge d).
\]

This argument works for every ideal \(I\) of a Noetherian ring. Valette uses the case of the maximal ideal of a Noetherian local ring.

## Krull intersection for modules

Assume now that \(R\) is Noetherian and local, with maximal ideal \(\mathfrak m\). If a finite module \(L\) satisfies \(L=\mathfrak m L\), then \(L=0\). Indeed, if \(L\ne0\), choose a generating set \(e_1,\ldots,e_p\) of least possible size. Express

\[
e_1=\sum_{j=1}^p b_je_j,\qquad b_j\in\mathfrak m.
\]

The coefficient \(1-b_1\) is a unit: otherwise both it and \(b_1\) would belong to the unique maximal ideal, forcing \(1\in\mathfrak m\). The displayed relation then eliminates \(e_1\), contradicting minimality. This proves the needed form of Nakayama's lemma.

**Krull intersection.** For a finite \(R\)-module \(M\),

\[
\bigcap_{i\ge0}\mathfrak m^iM=0.
\]

**Proof.** Put \(L=\bigcap_i\mathfrak m^iM\). It is a finite submodule of \(M\). Artin–Rees applied to \(L\subset M\) says, for sufficiently large \(i\),

\[
L=L\cap\mathfrak m^{i+1}M
 =\mathfrak m(L\cap\mathfrak m^iM)=\mathfrak m L.
\]

Nakayama gives \(L=0\). \(\square\)

Apply this to \(M/N\). Its powers \(\mathfrak m^i(M/N)\) are the images of \(\mathfrak m^iM\), so

\[
\bigcap_{i\ge0}(N+\mathfrak m^iM)=N.
\]

Every submodule of a finite module is therefore closed for the \(\mathfrak m\)-adic topology. In particular, for an ideal \(J\subset R\),

\[
\bigcap_{i\ge0}(J+\mathfrak m^i)=J.
\]

Locality matters in this conclusion. In \(\mathbb R[x]\), the ideals \(J=(x-1)\) and \(I=(x)\) satisfy \(J+I^i=\mathbb R[x]\) for every positive \(i\), although \(J\) is proper. This is why the local hypothesis cannot be dropped when interpreting the last intersection formula.

## Formal linear solutions have convergent replacements

Let \(R=R_n\), \(\widehat R=\mathbb R[[x_1,\ldots,x_n]]\), and let

\[
H:R^a\longrightarrow R^b
\]

be an \(R\)-linear map, represented by a matrix of convergent series. Suppose \(v\in R^b\), and the corresponding formal equation has a solution \(\widehat f\in\widehat R^a\):

\[
H\widehat f=v.
\]

**Linear convergence theorem.** There is an \(f\in R^a\) with \(Hf=v\). Moreover, for each prescribed integer \(q\ge0\), \(f\) can be chosen with the same Taylor coefficients as \(\widehat f\) in every degree less than \(q\).

**Proof of existence.** Truncate each \(\widehat f_j\) to degree at most \(k\), obtaining a polynomial \(p_{j,k}\). Then

\[
v-H(p_{1,k},\ldots,p_{a,k})\in\mathfrak m^{k+1}R^b.
\]

The reason is coefficientwise: multiplying by a convergent series cannot lower the degree of the omitted formal terms. The difference on the left is convergent, and a convergent series whose terms of degree less than \(k+1\) vanish belongs to \(\mathfrak m^{k+1}\). To see the latter assertion, assign each monomial to a degree-\((k+1)\) monomial dividing it, and factor that monomial out. There are finitely many divisors of this degree, and the remaining series converge on a smaller polydisc.

Thus \(v\) belongs to \(H(R^a)+\mathfrak m^{k+1}R^b\) for every \(k\). Submodule closedness gives \(v\in H(R^a)\), proving existence.

**Proof with a prescribed jet.** For \(q>0\), let \(p_j\) be the Taylor polynomial of \(\widehat f_j\) in degrees less than \(q\). A formal series of order at least \(q\) can be grouped by the finitely many degree-\(q\) monomials:

\[
\widehat f_j-p_j
 =\sum_{|\alpha|=q}x^\alpha\widehat g_{j,\alpha}.
\]

Consequently the finite linear equation

\[
\sum_{j=1}^a\sum_{|\alpha|=q}
 x^\alpha H(e_j)\,g_{j,\alpha}=v-H(p)
\]

has a formal solution. The existence argument already proved gives convergent solutions \(g_{j,\alpha}\). Set \(f_j=p_j+\sum_{|\alpha|=q}x^\alpha g_{j,\alpha}\). This has the required jet and solves \(Hf=v\). For \(q=0\), use existence alone. \(\square\)

The theorem gives a *replacement* solution. It does not say that the originally chosen formal series converge. It is a statement about finite **linear** systems; a nonlinear approximation theorem has not been used.

## A finite Taylor family with analytic units

Let \(\psi\) be a real analytic germ at \(y_0=(u_0,z_0)\in\mathbb R^{n-1}\times\mathbb R\). Translating, suppose \(y_0=0\), and write its convergent expansion

\[
\psi(u,z)=\sum_{j\ge0}c_j(u)z^j.
\]

Each \(c_j\) is a convergent analytic germ in \(u\). Noetherianity says that the ideal generated by all the \(c_j\) is generated by a finite subfamily. Enlarging that finite subfamily, choose an initial segment \(c_0,\ldots,c_d\) generating the ideal. For \(j>d\), choose convergent germs \(b_{i,j}(u)\) with

\[
c_j(u)=\sum_{i=0}^d b_{i,j}(u)c_i(u).
\]

There is no assertion that the infinitely many \(b_{i,j}\) share a convergence estimate. Instead, work formally. Put

\[
\widehat F_i(U,Z)=\sum_{j>d}b_{i,j}(U)Z^{j-i-1}.
\]

Every exponent of \(Z\) is nonnegative. For any fixed total degree only finitely many \(j\) can contribute, so this is a well-defined formal series. Coefficient comparison gives

\[
\psi(U,Z)=\sum_{i=0}^d c_i(U)Z^i(1+Z\widehat F_i(U,Z)).
\]

Equivalently, the **finite linear equation**

\[
\sum_{i=0}^d c_i(U)Z^{i+1}F_i
 =\psi(U,Z)-\sum_{i=0}^d c_i(U)Z^i
\]

has a formal solution. The linear convergence theorem, applied in \(n\) variables, supplies convergent solutions \(G_i\). Define

\[
A_i(u,z)=1+zG_i(u,z).
\]

Then \(A_i(0,0)=1\), and

\[
\psi(u,z)=\sum_{i=0}^d c_i(u)z^i A_i(u,z).
\]

On a sufficiently small common neighbourhood all \(A_i\) are nonzero. After undoing translation, this proves the announced finite Taylor-unit decomposition. If \(\psi=0\), take \(d=0,c_0=0,A_0=1\). A coefficient that happens to vanish identically may likewise be retained with unit \(1\). \(\square\)

This is Valette's Proposition 1.3.11, using Corollary 1.3.10. The linear-convergence step is what makes the decomposition analytic; purely formal manipulation of the infinite coefficients would not suffice.

## Signed normalization and a uniform order bound

Here is the precise normalization used in the next preparation step. Suppose on a neighbourhood of \((u_0,z_0)\) that

\[
\psi(u,z)=\sum_{i=0}^d c_i(u)(z-z_0)^i A_i(u,z),
\qquad A_i(u_0,z_0)\ne0.
\]

For \(m\in\{0,\ldots,d\}\), let

\[
K_m=\{t\in[-1,1]^{d+1}:t_m=1\},\qquad
Q(t,u,z)=\sum_{i=0}^d t_i(z-z_0)^iA_i(u,z).
\]

**Uniform regularity.** There is a neighbourhood \(V\) of \((u_0,z_0)\) and a constant \(\delta>0\) such that

\[
\max_{0\le k\le m}|\partial_z^k Q(t,u,z)|\ge\delta
\qquad(t\in K_m,\ (u,z)\in V).
\]

In particular the order of \(Q\) in \(z\), at each such point, is at most \(m\).

**Proof.** At \((u_0,z_0)\), the derivatives of \((z-z_0)^iA_i(u,z)\) of orders \(k<i\) vanish, and its derivative of order \(i\) is \(i!A_i(u_0,z_0)\ne0\). Therefore the linear map from \((t_0,\ldots,t_m)\) to the derivatives of \(Q\) of orders \(0,\ldots,m\) at this point is triangular with nonzero diagonal. The higher \(t_i\), \(i>m\), do not enter these derivatives. Because \(t_m=1\), these derivatives cannot all vanish. Their maximum is continuous and positive on the compact set \(K_m\), so it has a positive minimum, say \(2\delta\). Uniform continuity of the finitely many derivatives on a compact product \(K_m\) times a small closed box supplies \(V\) on which that maximum remains at least \(\delta\). \(\square\)

If \(\phi:B\to\mathbb R^{n-1}\) is a parameter map, set \(g_i=c_i\circ\phi\). On any piece where \(g_m\ne0\) and \(|g_i|\le |g_m|\) for all \(i\),

\[
\psi(\phi(x),z)
 =g_m(x)\,Q\!\left(
 \frac{g_0(x)}{g_m(x)},\ldots,
 \frac{g_d(x)}{g_m(x)},\phi(x),z\right).
\]

The normalizing vector lies in \(K_m\), including when some ratios are negative. On the piece where every \(g_i=0\), the function is identically zero and needs no normalization. Ordering these coefficient functions into suitable analytic cells belongs to the dimension induction in the full preparation proof; it has not been assumed in proving the uniform bound.

For a function analytic near a compact parameter-image closure, first choose finitely many smaller boxes where the Taylor-unit decomposition and this bound hold. Such boxes exist by the local statements and compactness. Their preimages provide a finite cover. The compatible refinement for that cover is supplied by the cell induction below.

## How this supplies the geometric argument

The written chain is now

\[
\begin{gathered}
\text{real analytic division}\ \Longrightarrow\
\text{Noetherian convergent germs},\\
\text{Rees finiteness}\ \Longrightarrow\
\text{Artin--Rees}\ \Longrightarrow\
\text{Krull submodule closedness},\\
\text{formal linear solvability}\ \Longrightarrow\
\text{convergent replacements}\ \Longrightarrow\
\text{finite Taylor units}\ \Longrightarrow\
\text{uniform signed regularity}.
\end{gathered}
\]

The already written [curve-selection and Łojasiewicz treatment](../curve-selection-and-lojasiewicz.html) additionally needs finite analytic cell decomposition and convergent Puiseux preparation. The later sections complete its reduction, complement and Puiseux providers under the explicitly specified projective product definition.


## A convergent split before restricting to a hyperbola

Let \(\psi(u,z,w)\) be real analytic near \((a,0,0)\), where \(u\in\mathbb R^k\). Its real series complexifies. Choose \(R>0\) such that this complexification is holomorphic on a neighborhood of the closed polydisc of common radius \(R\), centered at \((a,0,0)\), and bounded there by \(M\). Write

\[
\psi(u,z,w)=
\sum_{\alpha\in\mathbb N^k,\ i,j\ge0}
b_{\alpha i j}(u-a)^\alpha z^i w^j .
\]

Repeated one-variable Cauchy coefficient estimates give

\[
|b_{\alpha i j}|\le M R^{-|\alpha|-i-j}.
\]

Define, using an independent variable \(c\),

\[
\begin{aligned}
\psi_+(u,c,z)&=
\sum_{\alpha,\ i>j\ge0}
b_{\alpha i j}(u-a)^\alpha c^j z^{i-j-1},\\
\psi_-(u,c,w)&=
\sum_{\alpha,\ j\ge i\ge0}
b_{\alpha i j}(u-a)^\alpha c^i w^{j-i}.
\end{aligned}
\]

These series converge as functions of independent variables. In the first one set \(i=j+\ell+1\). Its absolute terms are bounded by

\[
\frac{M}{R}
\left(\prod_{\nu=1}^k
\left(\frac{|u_\nu-a_\nu|}{R}\right)^{\alpha_\nu}\right)
\left(\frac{|c|}{R^2}\right)^j
\left(\frac{|z|}{R}\right)^\ell .
\]

Summing them gives the finite bound

\[
\frac{M}{R}
\prod_{\nu=1}^k
\frac{1}{1-|u_\nu-a_\nu|/R}
\frac{1}{1-|c|/R^2}
\frac{1}{1-|z|/R}
\]

whenever every displayed ratio is less than one. In the second series put \(j=i+\ell\); its analogous bound is

\[
M
\prod_{\nu=1}^k
\frac{1}{1-|u_\nu-a_\nu|/R}
\frac{1}{1-|c|/R^2}
\frac{1}{1-|w|/R}.
\]

On each strictly smaller closed polydisc these bounds are uniform geometric majorants. Thus the series define holomorphic functions of \((u,c,z)\) and \((u,c,w)\), respectively, on the indicated open polydiscs. Their real restrictions are analytic. In particular, both functions are analytic on neighborhoods of compact boxes with

\[
|u_\nu-a_\nu|\le R/2,\qquad
|c|\le R^2/4,\qquad |z|,\ |w|\le R/2.
\]

Now impose \(c=zw\). An \(i>j\) term becomes

\[
z\,c^jz^{i-j-1}=z^iw^j,
\]

and a \(j\ge i\) term becomes \(c^iw^{j-i}=z^iw^j\). Absolute convergence permits the two subseries to be recombined. Therefore

\[
\boxed{\ \psi(u,z,w)
   =z\,\psi_+(u,zw,z)+\psi_-(u,zw,w)\ } .
\]

For \(z\ne0\), putting \(w=c/z\) gives Valette's Lemma 1.6.13 splitting identity with fully convergent functions. For \(z=0\), the identity with independent \(w\) still holds, so no division is needed for the limiting statement. No sign restriction on \(z,w,c\) has been imposed.

For example, for \(\psi(z,w)=1+z+w+zw+z^2w\), the construction gives

\[
\psi_+(c,z)=1+c,\qquad
\psi_-(c,w)=1+w+c.
\]

Hence \(z(1+c)+(1+w+c)=1+z+w+zw+z^2w\) when \(c=zw\). The equality includes the mixed diagonal \(zw\) in the minus series and the off-diagonal \(z^2w\) in the plus series, as required by the index convention.

## Localize on the actual image, rather than a larger product

Suppose \(\Phi(x)=(\phi(\widetilde x),z,c(\widetilde x)/z)\) is well defined and bounded on a set \(C\), and \(\psi\) is analytic on an open neighborhood \(U\) of

\[
K=\overline{\Phi(C)}.
\]

Then \(K\) is compact. Write \(w=c/z\), so \(c=zw\) on \(C\). There are three local descriptions, covering every \(p=(a,z_0,w_0)\in K\).

If \(z_0\ne0\), define

\[
F_z(u,c,z)=\psi(u,z,c/z)
\]

on the inverse image of \(U\) under the analytic map \((u,c,z)\mapsto(u,z,c/z)\), with \(z\ne0\). It is analytic on a neighborhood of \((a,z_0w_0,z_0)\). Choose a small closed box \(B_z\) about that point whose neighborhood lies in this inverse image, and on which \(|z|\ge |z_0|/2\). By continuity, there is a neighborhood \(V_p\) of \(p\) such that

\[
(u,z,w)\in V_p
\quad\Longrightarrow\quad
(u,zw,z)\in\operatorname{int}B_z.
\]

Consequently, on the portion of \(C\) mapping into \(V_p\), the original function is \(F_z(\phi,c,z)\), analytic in its last coordinate \(z\) on the required compact box.

If \(w_0\ne0\), instead define

\[
F_w(u,c,w)=\psi(u,c/w,w).
\]

The same argument gives a compact box \(B_w\) where \(F_w\) is analytic on a neighborhood and \(|w|\ge |w_0|/2\), and a neighborhood \(V_p\) whose images \((u,zw,w)\) lie in its interior. Here the original function is analytic in the coordinate \(w=c/z\). Notice that \(c\ne0\) on this portion of the original domain because \(z\ne0\) there and \(w\) is bounded away from zero; the fibre-coordinate change can therefore be inverted.

If \(z_0=w_0=0\), then \((a,0,0)\) is an *actual point of \(K\)*. The function \(\psi\) is analytic near this point, so the convergent splitting just proved applies. Choose a smaller neighborhood \(V_p\) such that its points satisfy the splitting bounds and both compact maps

\[
(u,z,w)\longmapsto(u,zw,z),\qquad
(u,z,w)\longmapsto(u,zw,w)
\]

fit in the interiors of the respective boxes of analyticity.

The \(V_p\) cover \(K\); extract a finite subcover. Their preimages under \(\Phi\) cover \(C\). This proves the finite analytic localization without any cell theorem. In the full induction, the finite two-coordinate localization below turns these finitely many preimages into compatible cells before applying cell reductions.

The existence of \(\psi\) near \(K\) does not imply analyticity near \((a,0,0)\) for *every* \(a\in\overline{\phi(B)}\). Those points can lie outside \(K\). The proof uses the split only at the third type of point, and uses the two nonsingular-coordinate descriptions at the other points. No analytic extension to a larger parameter product is required.

## The signed balanced-coordinate calculation

The following calculation is the remaining analytic mechanism in Valette's balanced case, conditional on the stated nondegenerate reductions and translation dichotomy from the preceding cell induction.

Work on a piece where \(z\ne0,c\ne0\) and both split contributions

\[
X_+=z\,\psi_+(\phi,c,z),\qquad
X_-=\psi_-(\phi,c,c/z)
\]

are nonzero and comparable in absolute value, with constants uniform on the piece. Suppose that the ordinary analytic preparation step has supplied, with nonzero base coefficients \(a_+,a_-\), nonnegative rational exponents \(r,s\), and uniformly bounded nonvanishing units,

\[
\begin{aligned}
|X_+|&\asymp |z|\,|a_+|\,
 |z-\theta_+|^r,\\
|X_-|&\asymp |a_-|\,
 |c/z-\theta_-|^s.
\end{aligned}
\]

Here the coefficients and translations depend only on the base variables. The preceding translation dichotomy has three possibilities.

If \(|z|\asymp|\theta_+|\), take \(b=|\theta_+|>0\). If \(|c/z|\asymp|\theta_-|\), take \(b=|c/\theta_-|>0\). In either case \(|z|\asymp b\).

If neither comparison holds and the dichotomy supplies reductions with both translations zero, comparability gives

\[
|a_+|\,|z|^{r+1}
\asymp |a_-|\,|c|^s|z|^{-s}.
\]

Therefore take

\[
b=
\left(\frac{|a_-|\,|c|^s}{|a_+|}\right)^{1/(r+s+1)}>0.
\]

The denominator exponent is positive because \(r,s\ge0\). Again \(|z|\asymp b\). No positive-sign assumption on \(X_+,X_-,c,z\) was needed.

Set

\[
q=z/b,\qquad d=c/b,\qquad
\Psi(x)=(\phi(\widetilde x),b(\widetilde x),
d(\widetilde x),q(x)).
\]

The ratio \(q\) is bounded and bounded away from zero. Since \(z\) and \(c/z\) are bounded, comparability bounds \(b\), and

\[
d=(c/z)q
\]

is bounded as well. Thus \(\Psi(C)\) is bounded. Define

\[
\widetilde\psi(u,b,d,q)=\psi(u,bq,d/q).
\]

On the open set \(q\ne0\), this is analytic wherever the inner map lands in \(U\). That condition holds on a neighborhood of \(\overline{\Psi(C)}\): at each of its points, \(q\ne0\), and continuity maps it into \(K\), since the equality

\[
(\phi,bq,d/q)=(\phi,z,c/z)
\]

holds on \(C\). The open inverse image of \(U\) therefore contains the compact closure. Hence the original function is a restricted analytic composition in the last coordinate \(q\), with base parameters \((\phi,b,d)\). Pulling back the resulting preparation through \(q=z/b\) uses the power-coordinate result proved below, including its zero-scale and sign cases and its explicit lower-dimensional induction input.

If \(c=0\), the original function is \(\psi(\phi,z,0)\) and belongs directly to the ordinary analytic-composition case. If one split contribution vanishes, the other is the whole function. The balanced calculation is used only after these cases are separated.

This proves the analytic splitting, actual-compact-image localization and signed balanced substitution. The sections below prove the compatible endpoint refinements, ordinary nondegenerate reduction, translation dichotomy, analytic unit representations and coordinate pullbacks using the lower-dimensional induction. The later sections complete the full two-coordinate assembly and joint dimension induction.


## Analytic units and the lower-dimensional induction

This section adapts Valette's definitions in §§1.4–1.5 and the preliminaries in §1.6.1. The additional bounded-monomial construction and compact-image arguments supply the unit representations used in the source's abbreviated calculations.

An \(\mathcal L\)-function is obtained by finitely many sums, products and compositions from restricted real analytic functions and rational powers, on domains where these expressions are defined. A restricted analytic function is analytic on a neighborhood of a compact cube. Its restriction and all the expressions below retain their stated domains. We consider such functions on \(\mathcal L\)-cells: inductively, graphs and open bands of analytic \(\mathcal L\)-functions over lower-dimensional cells, with infinite band endpoints allowed.

Fix a dimension \(n\), write \(x\) for the first \(n-1\) coordinates and \(z\) for the last, and work in the dimension induction. The **lower-dimensional package** says that finitely many \(\mathcal L\)-functions on supplied lower-dimensional cells can be made analytic, of constant sign and pairwise ordered on a common finite cell refinement. Their domains and any finitely many supplied cells can be respected by that refinement. These are the induction hypotheses in dimensions less than \(n\); the full preparation and arbitrary-set cell theorem in dimension \(n\) are not being assumed here.

For a cell \(C\) with base \(B\), take an analytic base translation \(\theta:B\to\mathbb R\) with its graph disjoint from \(C\), and put \(y=|z-\theta(x)|>0\). An **analytic \(\mathcal L\)-unit** in \(y\) has the form

\[
U(x,z)=\Psi\bigl(
\beta(x),u(x)y^{1/s},v(x)y^{-1/s}\bigr),
\qquad s\in\mathbb Z_{>0}.
\]

The base functions are analytic \(\mathcal L\)-functions, the whole argument map is bounded, and \(\Psi\) is analytic and nonzero on a neighborhood of its compact image closure. Shrinking that neighborhood if necessary is permitted. A **reduced function** is

\[
f(x,z)=a(x)y^rU(x,z),\qquad r\in\mathbb Q,
\]

with analytic \(\mathcal L\)-coefficient \(a\). The zero coefficient is allowed. A unit is uniformly bounded and bounded away from zero on \(C\), by compactness. In the arguments below we prove the requisite analytic representation; uniform bounds alone are not used as a substitute for it.

Cells are connected. For a graph this follows from connectedness of the base. A finite band has a continuous parametrization from \(B\times(0,1)\) using its endpoints. A one-sided band is parametrized from \(B\times(0,\infty)\), and a band with both endpoints infinite is \(B\times\mathbb R\). Induction proves connectedness in all cases. Hence a continuous nonzero unit has constant sign on a cell.

## Finite endpoint refinements

Given finitely many cells in \(\mathbb R^n\), together with finitely many analytic \(\mathcal L\)-functions on their bases, there is a finite cylindrical refinement respecting the supplied cells and any graphs or bands cut out by these functions.

**Proof in the dimension induction.** Refine the bases with the lower-dimensional package so that every relevant function is analytic and every pairwise difference has constant sign. Include all finite endpoints defining the original cells. On a fixed base cell, two of these functions are either identical or strictly ordered everywhere. Remove repeated identical endpoints and list the others in order. Their graphs and the intervening bands, including the two outer infinite bands, partition that whole cylinder. They are analytic \(\mathcal L\)-cells. Each supplied cell is a union of these cells, because its base and all its endpoints were respected. There are finitely many bases and endpoints. \(\square\)

This also supplies a common refinement of finitely many existing cell decompositions. It does not assume that an arbitrary globally subanalytic set has a cell decomposition.

A graph cell \(z=\zeta(x)\) can be handled entirely in the lower dimension. Substituting \(\zeta\) into a well-defined finite \(\mathcal L\)-expression gives an \(\mathcal L\)-function of \(x\). Make it analytic on a lower-dimensional refinement. On the graph choose \(\theta=\zeta-1\), so \(y=1\), take \(r=0,U=1\), and use that base function as coefficient. In particular graph cells require no inverse last-coordinate map.

A base function on a band is also reduced after cutting at \(z=0\): on the nonzero bands take \(\theta=0,r=0,U=1\); handle the possible graph \(z=0\) as just described. The finite endpoint refinement supplies these pieces even when the original band has both endpoints infinite.

If \(f=a|z-\theta|^rU\) is already reduced, refine the base so \(a\) has constant sign. The distance is positive, and the unit is continuous and nonzero. Thus \(f\) has constant sign on each resulting cell. All these sign refinements use only the lower-dimensional package.

## Collecting bounded monomials into two coordinates

Let \(t>0\) on a cell with base \(B\). Suppose that a finite family

\[
M_i(x,t)=b_i(x)t^{q_i},\qquad q_i\in\mathbb Q,
\]

is bounded on the cell, with \(\mathcal L\)-coefficients \(b_i\). There may also be finitely many bounded base parameters. After a lower-dimensional refinement, all these arguments can be written as polynomials of bounded base parameters and just two bounded arguments

\[
Z=u(x)t^{1/s},\qquad W=v(x)t^{-1/s},
\]

where \(s>0\) is an integer and \(u,v\) are nonnegative analytic \(\mathcal L\)-functions. Either of \(u,v\) may be identically zero.

**Proof.** Choose \(s\) so every \(a_i=sq_i\) is an integer. Refine the base so each \(b_i\) is analytic and identically zero, strictly positive or strictly negative. For \(a_i>0\), put \(u_i=|b_i|^{1/a_i}\); order these finitely many functions on the base and choose their largest, \(u\). If this family is empty or all its coefficients vanish, put \(u=0\). Otherwise \(u>0\). In that case

\[
M_i=\operatorname{sign}(b_i)
\left(\frac{u_i}{u}\right)^{a_i}Z^{a_i}
\qquad(a_i>0),
\]

where \(u_i/u\in[0,1]\). Moreover

\[
Z=\max_{a_i>0}|M_i|^{1/a_i},
\]

so \(Z\) is bounded. With \(u=0\), all these \(M_i\) are zero and their representation is immediate.

For \(a_i=-d_i<0\), similarly put \(v_i=|b_i|^{1/d_i}\), choose the largest \(v\), and obtain

\[
M_i=\operatorname{sign}(b_i)
\left(\frac{v_i}{v}\right)^{d_i}W^{d_i}.
\]

The ratios lie in \([0,1]\), and \(W=\max_{a_i<0}|M_i|^{1/d_i}\) is bounded. If all negative-exponent coefficients vanish, put \(v=0\). For \(a_i=0\), the argument is the base function \(b_i\), which is bounded on \(B\): every base point has a nonempty fibre. Include these and the original bounded base parameters among the new base parameters. All roots, ratios and choices are \(\mathcal L\)-functions and are analytic after the lower-dimensional refinement. This proves the claim. \(\square\)

There is a useful compact-domain consequence. Let \(\Gamma=(\eta(x),Z,W)\) be the new bounded argument map, and let \(P\) be the polynomial map recovering all old arguments. Then

\[
P\bigl(\overline{\Gamma(C)}\bigr)
\subset\overline{P(\Gamma(C))}.
\]

Indeed every point of the left-hand domain is the limit of a sequence of new argument values, and polynomial continuity recovers the limit of the old ones. Thus, if an outer analytic function was given only near the old compact image, its composite with \(P\) is analytic near the new compact image: take the open inverse image of its domain. No extension to a larger parameter box has been assumed. If the old function was nonzero on that image closure, the composite is nonzero on the new one as well.

Consequently a finite list of bounded monomial arguments can be used in a unit representation without requiring one separate forward or inverse coordinate for each exponent.

## Closure and substitution for analytic units

**Products, reciprocals and powers.** Finitely many units with the same distance \(y\) have a common two-coordinate argument map. Apply the bounded-monomial construction to their finitely many original forward/inverse arguments and concatenate the bounded base parameters. The recovered old maps are polynomial maps of the new arguments. Compose the outer analytic functions with these maps. Their product is analytic and nonzero near the new compact closure. The same holds for reciprocals.

For a rational power of the absolute value of a unit, first fix its sign on the cell. The signed analytic outer function is positive on the compact image and hence on a smaller neighborhood. Its real rational power is analytic there. Thus \(|U|^\lambda\) is a unit for every \(\lambda\in\mathbb Q\). Integer powers retain the corresponding constant sign if desired.

**Change of distance.** Suppose \(h>0\) is another distance, and on a cell it has a reduction

\[
h=A(x)y^eW(x,y),
\]

where \(A>0\), \(e\in\mathbb Q\), and \(W\) is a positive unit in \(y\). Every unit originally expressed in \(h\) becomes a unit in \(y\).

To prove this rather than infer it from bounds, write each original bounded monomial argument as

\[
b(x)h^q=b(x)A(x)^q y^{eq}W(x,y)^q.
\]

Since \(W\) and its reciprocal are uniformly bounded, the monomial \(bA^qy^{eq}\) is bounded whenever the original argument is bounded. Collect these finitely many monomials, together with the bounded monomial arguments representing \(W\), into two coordinates. Recover \(W\) by its analytic outer function, take its positive analytic rational powers, and multiply by the recovered monomials. These operations define an analytic map near the new compact closure. On the actual cell the resulting map is exactly the old argument map, so its closure maps into the old compact closure. The old analytic outer function can therefore be composed on a neighborhood of that new compact closure. It remains nonzero there. This is the required unit representation.

In particular if \(a h^r U(h)\) was reduced in \(h\), it becomes

\[
(aA^r)y^{er}\bigl(W^rU(h)\bigr)
\]

reduced in \(y\). The unit in parentheses has just been proved to have the required analytic form.

## A common translation for finitely many reductions

Suppose \(f_1,\ldots,f_k\) are reduced on a cell \(C\), with translations \(\theta_1,\ldots,\theta_k\), each disjoint from \(C\). After a finite endpoint refinement, all \(f_i\) are reduced with one common translation.

**Proof.** First fix signs and order the base functions as necessary. Comparing the distances \(|z-\theta_i|\) and \(|z-\theta_j|\) only requires cutting at their midpoint: the squared-distance difference is

\[
(z-\theta_i)^2-(z-\theta_j)^2
 =(\theta_j-\theta_i)(2z-\theta_i-\theta_j).
\]

The finite endpoint refinement therefore makes these distance comparisons constant on each piece. Choose an index \(j\) with

\[
y=|z-\theta_j|\le |z-\theta_i|\qquad(1\le i\le k)
\]

throughout the piece. This distance is strictly positive because \(\theta_j\)'s graph is outside the original cell.

For a fixed \(i\), put \(d=z-\theta_j\) and \(\delta=\theta_j-\theta_i\). If \(\delta=0\) identically, the two distances are equal. Otherwise refine at the endpoints \(\theta_j\pm|\delta|\), and fix the sign of \(d\).

On \(|d|\le|\delta|\), put \(\tau=d/\delta\). The nearest-distance condition says \(|\tau|\le|1+\tau|\). Squaring gives \(\tau\ge-1/2\). Hence

\[
-\tfrac12\le\tau\le1,\qquad
|z-\theta_i|=|\delta|(1+\tau).
\]

The argument \(\tau=(\operatorname{sign}d/\delta)y\) is a bounded forward monomial, and \(1+\tau\) is positive and at least \(1/2\) on its compact closure. Thus this is a reduced distance with exponent zero and an explicit unit in \(y\).

On \(|d|\ge|\delta|\), put \(\tau=\delta/d\). Now \(\tau\in[-1,1]\), and the nearest-distance condition gives \(1\le|1+\tau|\). Since \(1+\tau\ge0\), it follows that \(0\le\tau\le1\). Therefore

\[
|z-\theta_i|=y(1+\tau),
\qquad \tau=\operatorname{sign}(d)\,\delta\,y^{-1}.
\]

This is a bounded inverse monomial and a positive analytic unit. The case \(\delta=0\) is included by taking the unit \(1\).

We have expressed each old distance as \(A_i y^{e_i}W_i\), with \(e_i=0\) or \(1\), positive \(A_i\), and an explicit positive unit. The distance-substitution result converts each complete reduction, including its old unit, to the common translation \(\theta_j\). There are only finitely many indices and endpoints. \(\square\)

Products of reducible functions are now reducible: use a common refinement and translation, multiply the base coefficients, add the rational exponents, and multiply the units. A quotient is handled similarly on its stated domain where the denominator is nonzero. Its nonzero base coefficient can be inverted after the base sign refinement. No zero denominator is silently included.

## Dominant and comparable pieces

Let \(f,g\) be reduced, and let \(\epsilon>0\). There is a finite endpoint refinement on which one of

\[
|f|\le\epsilon|g|,\qquad
|g|\le\epsilon|f|,\qquad
|f|\asymp|g|
\]

holds on every piece, with uniform positive comparability constants in the last case.

**Proof.** Give the functions a common translation. Their zero base coefficients are separated first. Where both are nonzero, write

\[
f=a y^rU,\qquad g=b y^sV.
\]

The compact unit bounds give constants \(0<C_1\le C_2\) such that

\[
C_1h\le |f/g|\le C_2h,\qquad
h=|a/b|y^{r-s}.
\]

Choose \(\eta=\min(\epsilon,1/2)\). Cut at the two levels

\[
h=\eta/C_2,\qquad h=1/(\eta C_1).
\]

They are ordered because \(C_1\le C_2\). Below the first, \(|f/g|\le\eta\le\epsilon\). Above the second, \(|g/f|\le\eta\le\epsilon\). Between them the displayed unit bounds give a fixed positive lower bound and a fixed finite upper bound on \(|f/g|\).

If \(r=s\), these cuts involve only base functions and use the lower-dimensional package. Otherwise each positive level \(L\) corresponds to

\[
y=(L|b/a|)^{1/(r-s)}.
\]

This is a positive analytic \(\mathcal L\)-function of the base on the nonzero-coefficient pieces. The endpoints \(\theta\pm(L|b/a|)^{1/(r-s)}\) give the needed finite refinement. A negative exponent merely reverses the ordering of the inequalities. The threshold graphs are included as separate cells. If one function is zero, the corresponding dominance assertion is immediate; if both vanish, both inequalities hold. \(\square\)

## Zero translation or comparison with the coordinate

After a finite refinement, a given reduction with translation \(\theta\) can be arranged so that either \(\theta=0\), or \(|z|\asymp|\theta|\) and \(z,\theta\) have the same sign.

**Proof.** Graph cells are handled in the lower dimension. On nonzero-coordinate bands, cut at \(z=0\), fix the sign of \(\theta\), and compare \(|z|\) with \(|\theta|/2\) and \(2|\theta|\). These are finite base endpoints. If \(\theta=0\), there is nothing to change.

If \(|\theta|\le |z|/2\), put \(t=|z|\). Then

\[
|z-\theta|=t(1-\theta/z),
\qquad |\theta/z|\le1/2.
\]

The ratio is a bounded inverse monomial in \(t\), and its analytic unit is positive. If \(|z|\le|\theta|/2\), then

\[
|z-\theta|=|\theta|(1-z/\theta),
\qquad |z/\theta|\le1/2.
\]

This is a base factor times a unit of a bounded forward monomial in \(t\). In both cases the distance-substitution theorem changes the full reduction to translation zero.

In the remaining comparable case, if signs are opposite then

\[
|z-\theta|=t(1+|\theta|/t),
\qquad 1/2\le|\theta|/t\le2.
\]

Again the inverse argument and analytic unit are explicit, so use translation zero. With the same sign retain the old translation, which satisfies the claimed comparison. \(\square\)

## Pullback through a power coordinate

Consider

\[
H(x,z)=\bigl(x,c(x)|z|^{1/p}\bigr),
\qquad p\in\mathbb Z\setminus\{0\},
\]

on a cell where it is well defined. If a function is reducible on the image cells of \(H\), its composite with \(H\) is reducible after a finite refinement.

First handle graph cells as above. Refine the base into constant-sign pieces for \(c\), and cut at \(z=0\). If \(c=0\), the image lies in the graph of zero; evaluating the expression on that graph is a lower-dimensional \(\mathcal L\)-function. Its pullback is a base function, handled by the graph/band rule. If \(z=0\) is in the domain, it is already a graph cell. For \(p<0\), such points are excluded by the stated domain.

It remains to work with \(c\ne0\) and \(z\ne0\), with both signs fixed. The fibre map is analytic and strictly monotone. With \(v=c|z|^{1/p}\) and \(\sigma=\operatorname{sign}z\), its inverse on the branch is

\[
z=\sigma(v/c)^p,\qquad v/c>0.
\]

Thus the image of a graph or band is a graph or band, and the preimage of an image cell is again such a cell. Its finite endpoints are analytic \(\mathcal L\)-functions after lower-dimensional refinement; zero and infinite endpoints are interpreted by one-sided limits. In particular a supplied finite image refinement pulls back to finitely many cells.

On one such image piece a reduction has an old positive distance \(|v-\theta(x)|\). Its pullback is

\[
h=|c|\,\bigl|t^{1/p}-\xi(x)\bigr|,
\qquad t=|z|,\quad \xi=\theta/c.
\]

We give explicit reductions of this distance.

For \(p=m>0\), put \(T=t^{1/m}\).

If \(\xi=0\), then \(h=|c|t^{1/m}\). If \(\xi<0\), put \(a=|\xi|>0\) and cut at \(t=a^m\). On \(T\ge a\),

\[
h=|c|t^{1/m}(1+a/T);
\]

on \(T\le a\),

\[
h=|c|a(1+T/a).
\]

In each case the ratio lies in \([0,1]\), is a bounded monomial in \(t\), and \(1+\) that ratio is a positive analytic unit. These are reductions with translation zero.

If \(\xi>0\), cut at \(T=\xi/2\) and \(T=2\xi\), using the base endpoints \(t=(\xi/2)^m,(2\xi)^m\). The two outer regions give respectively

\[
h=|c|\xi(1-T/\xi),\qquad
h=|c|t^{1/m}(1-\xi/T),
\]

with the ratios in \([0,1/2]\). On the middle region \(1/2\le T/\xi\le2\), use

\[
T-\xi=
\frac{t-\xi^m}
 {\xi^{m-1}P_m(T/\xi)},\qquad
P_m(v)=1+v+\cdots+v^{m-1}.
\]

This polynomial is positive on \([1/2,2]\). The numerator vanishes precisely at \(z=\sigma\xi^m\), which is outside the pulled-back image piece because the old distance was positive there. Put

\[
y=|z-\sigma\xi^m|,\qquad
\kappa=\operatorname{sign}(t-\xi^m),\qquad
\delta=y/\xi^m.
\]

Split at that numerator's graph if necessary. On each nonzero piece,

\[
T/\xi=(1+\kappa\delta)^{1/m}.
\]

For \(\kappa=1\), \(0\le\delta\le2^m-1\). For \(\kappa=-1\), \(0\le\delta\le1-2^{-m}<1\). Thus \(1+\kappa\delta\) stays strictly positive on its compact argument interval, and

\[
h=|c|\xi^{1-m}y
\left[P_m\bigl((1+\kappa\delta)^{1/m}\bigr)\right]^{-1}
\]

is an explicit reduction with translation \(\sigma\xi^m\). Its last factor is analytic and nonzero near that compact interval; \(\delta=\xi^{-m}y\) is a bounded forward argument. This proves the required unit representation even near the new translation. For \(m=1\), \(P_1=1\), and the same formula holds.

For \(p=-m<0\), if \(\xi=0\) the distance is simply \(|c|t^{-1/m}\). Otherwise,

\[
h=|c\xi|t^{-1/m}
\bigl|t^{1/m}-1/\xi\bigr|.
\]

The positive-power distance on the right has just been reduced. The additional factor \(t^{-1/m}\) is reduced with translation zero. Give the two factors a common translation and multiply their reductions. This reduces \(h\) for negative \(p\) as well.

Finally substitute the reduction of \(h\) into the *whole* original reduction: the distance-substitution theorem proves that the old unit remains a unit in the new distance. Coefficients and exponents transform accordingly. This proves the pullback assertion. With \(p>0\), a nonnegative original exponent stays nonnegative: the positive-power distance reductions have exponents \(0,1/m\) or \(1\). No such claim is needed or made for negative \(p\).

## Bounded arguments of a general analytic composition

Let \(g_1,\ldots,g_\ell\) be reduced on a cell, and assume \(G=(g_1,\ldots,g_\ell)\) is bounded. Let \(F\) be analytic near \(\overline{G(C)}\). After a common translation and refinement, the composite \(F(G)\) has the form

\[
\psi\bigl(\beta(x),u(x)y^{1/s},v(x)y^{-1/s}\bigr),
\]

where the complete argument map is bounded and \(\psi\) is analytic near its actual compact image closure.

**Proof.** Write \(g_i=a_i y^{r_i}U_i\). Each monomial \(a_i y^{r_i}\) is bounded because \(g_i\) is bounded and \(U_i\) is bounded away from zero. Collect these monomials and every unit's bounded monomial arguments by the two-coordinate construction. Recover every \(U_i\) by its analytic outer function, then every \(g_i\) by multiplication. The compact-image consequence ensures that this analytic recovery map is defined near the whole new compact closure and maps it into \(\overline{G(C)}\). Composing with \(F\) therefore gives the claimed \(\psi\). Zero coefficients are allowed and cause no division. \(\square\)

If \(u>0\), the power-coordinate change \(Z=u y^{1/s}\) gives

\[
W=\frac{uv}{Z}.
\]

The base product \(uv\) is bounded: it equals \(ZW\) on the cell, and every base point has a fibre. Thus the general composition is precisely the two-coordinate analytic form in the previously proved splitting/localization argument. The power-coordinate pullback just proved justifies returning to the original distance.

If \(u=0,v>0\), only the inverse coordinate remains; use \(W=v y^{-1/s}\) and ordinary analytic preparation in that coordinate, followed by the negative-power pullback. If \(u=v=0\), the function depends only on the base and uses the lower-dimensional package. These are separate cases, so normalizing a zero forward coefficient to one is never required.

This completes the explicit unit, translation, dominance, power-coordinate and bounded-argument preliminaries in the dimension induction. The next section proves the ordinary nondegenerate polynomial reduction. The subsequent two-coordinate proof and joint dimension induction complete these remaining steps.

## Ordinary analytic preparation without a cell-theorem assumption

We now prove Valette's Proposition 1.6.12, including its polynomial reduction. Throughout this section, only the lower-dimensional package in the preceding unit and refinement arguments is assumed. The induction on the analytic order below is a separate induction in the fixed ambient dimension. It does not assume preparation of arbitrary functions in that dimension.

**Ordinary preparation statement.** Let \(C\subset\mathbb R^n\) be an \(\mathcal L\)-cell with base \(B\). Suppose

\[
\Phi(x,z)=(\phi_1(x),\ldots,\phi_k(x),z)
\]

is bounded on \(C\), where the \(\phi_i\) are \(\mathcal L\)-functions on \(B\). Let \(\psi\) be analytic on an open neighborhood of \(K=\overline{\Phi(C)}\). Then \(\psi\circ\Phi\) has a finite cell refinement on which it is reduced with a nonnegative rational exponent. The coefficient is allowed to vanish identically. We call such a reduction **nondegenerate**.

All local analytic functions used below are restricted to closed boxes contained in their domains. Composing a function analytic near a compact base image with that base map gives a lower-dimensional \(\mathcal L\)-function after a finite localization: take a finite box cover, refine the base at the finitely many coordinate bounds using the lower-dimensional package, and on each resulting piece use its box's restricted analytic function. Thus coefficient compositions and changes of base coordinates below use only the established lower-dimensional induction.

### Finite localization and signed normalization

First make the \(\phi_i\) analytic by the lower-dimensional package. A graph cell is treated in that dimension, as in the graph rule. We can therefore work with bands.

At every point \((u_0,z_0)\in K\), the finiteness theorem already proved gives, on a sufficiently small box,

\[
\psi(u,z)=\sum_{i=0}^{d}c_i(u)(z-z_0)^i A_i(u,z),
\qquad A_i(u_0,z_0)=1.
\]

Shrink the box so its closed closure lies in the domain of this identity and in the neighborhood on which the signed uniform-regularity argument applies. These smaller open boxes cover \(K\). Choose a finite subcover. Membership in the inverse image of such a box is specified by bounds on the base functions \(\phi_i\) and by constant bounds on \(z\). Lower-dimensional base refinements followed by finite endpoint refinements respect all these inverse images. Every resulting piece of \(C\) fits inside one of the selected closed boxes. This construction uses no cell decomposition for arbitrary subanalytic sets.

On one such piece, put \(g_i=c_i\circ\phi\). Refine the base so every \(g_i\) has constant sign and the functions \(|g_i|\) are ordered. If all vanish, the displayed identity makes the function zero. Otherwise choose an index \(m\) where their maximum is attained. Then \(g_m\ne0\) and

\[
t_i=g_i/g_m\in[-1,1],\qquad t_m=1.
\]

With

\[
Q(t,u,z)=\sum_{i=0}^{d}t_i(z-z_0)^i A_i(u,z),
\qquad
\Theta=(t_0,\ldots,t_d,\phi,z),
\]

we have \(\psi\circ\Phi=g_m Q\circ\Theta\).

The previously proved signed normalization shows that, after the stated shrinking, \(Q\) is regular in \(z\) of order at most \(m\) on the entire compact normalized parameter set in question. In particular the same bound holds on \(\overline{\Theta(C)}\), even if \(g_m\) tends to zero: the normalized parameters stay in \([-1,1]\) and the coordinate \(t_m\) remains exactly one on that closure. Multiplication by the base coefficient \(g_m\) preserves a nonnegative last-coordinate exponent. It remains to prove the statement for an analytic function with a uniform finite regularity bound on its actual compact image.

### Induction on the regularity bound

Suppose an analytic function is regular in its last coordinate at every point of the relevant compact image, with order at most \(d\). We prove the nondegenerate preparation statement by induction on \(d\).

For \(d=0\), the function is nonzero on the compact image. It is therefore an analytic unit after a finite box localization. On a nonzero-coordinate band, write the bounded last coordinate as \(z=\sigma |z|\), with \(\sigma=\pm1\). Its analytic outer function, evaluated at the bounded arguments \((\phi,\sigma |z|)\), is a unit with translation zero and exponent zero. The graph \(z=0\) is handled in the lower dimension. The same argument applies to any analytic nonvanishing factor arising below.

For \(d>0\), at every compact-image point Weierstrass preparation supplies an analytic nonvanishing factor and a monic polynomial in the last coordinate, of degree \(e\le d\). Translate a constant local last-coordinate center into the polynomial's coefficients. Take closed boxes inside these preparation neighborhoods, extract a finite cover, and refine their inverse images by the same base-bound and endpoint construction as before.

Fix a resulting band. Up to its nonvanishing analytic factor, the function is

\[
P(x,z)=z^e+a_1(x)z^{e-1}+\cdots+a_e(x),
\]

where all coefficients are analytic \(\mathcal L\)-functions of the base and bounded there. Boundedness follows from continuity on the selected compact parameter box and the nonempty fibres over the base. Degree zero is already the unit case.

For \(e\ge1\), set

\[
w=z+a_1(x)/e.
\]

The inverse substitution \(z=w-a_1/e\) cancels the coefficient of \(w^{e-1}\), leaving

\[
\widehat P(x,w)=w^e+\sum_{i=2}^{e}b_i(x)w^{e-i}.
\]

The graph or band is carried to a graph or band with translated endpoints. All \(b_i\) are bounded analytic \(\mathcal L\)-functions of the base. If \(e=1\), or if all \(b_i\) vanish, this polynomial is \(w^e\). Its zero graph uses the lower-dimensional rule; off that graph it is \(\operatorname{sign}(w)^e|w|^e\).

Otherwise refine the base so each \(b_i\) has constant sign and the roots \(|b_i|^{1/i}\) are ordered. Choose a maximizing index \(j\), and put

\[
q=|b_j|^{1/j}>0,\qquad |b_i|\le q^i.
\]

The function \(q\) is bounded and analytic on this base piece. Refine at \(w=0\) and \(w=\pm2q\), including the resulting graphs. On any graph, substitution gives a lower-dimensional function, with exponent zero. The two types of remaining bands are handled as follows.

### Outside the scale: an explicit polynomial unit

Where \(|w|\ge2q\), the polynomial satisfies

\[
\widehat P
=w^e\left(1+\sum_{i=2}^{e}\frac{b_i}{w^i}\right),
\qquad
\left|\sum_{i=2}^{e}\frac{b_i}{w^i}\right|
\le\sum_{i=2}^{e}2^{-i}
=\frac12-2^{-e}<\frac12.
\]

Fix the sign \(\sigma=\operatorname{sign}(w)\). Every argument \(\sigma^{-i}b_i|w|^{-i}\) is bounded. The bounded-monomial collection writes the finite family using two bounded unit arguments. The analytic outer function \(1+\sum_i M_i\) is at least \(1/2+2^{-e}\) on the actual compact argument closure. It is therefore nonzero on a neighborhood of that closure and is an analytic \(\mathcal L\)-unit. Thus this is a reduction with translation zero and exponent \(e\), including the correct constant sign \(\sigma^e\).

Uniform bounds by themselves would not have supplied the unit representation. The preceding collection argument supplies the representation and its analytic domain.

### Inside the scale: the analytic order strictly decreases

Where \(0<|w|\le2q\), use the nonzero fibre coordinate \(v=w/q\). Its image is a cell after the previously proved nonzero-scale power-coordinate construction, with \(p=1\) and scale \(\operatorname{sign}(w)/q\) on each sign branch. Put

\[
\beta_i=b_i/q^i,\qquad
R(\beta,v)=v^e+\sum_{i=2}^{e}\beta_i v^{e-i}.
\]

Then

\[
\widehat P=q^e R(\beta,w/q),\qquad
|\beta_i|\le1,\quad \beta_j=\operatorname{sign}(b_j)\in\{-1,1\},
\quad |v|\le2.
\]

The full parameter map \((\beta,v)\) is bounded. Its compact image closure still satisfies \(\beta_j=\pm1\) with the fixed sign, so not every \(\beta_i\) is zero there.

At every point of this closure, the order of \(R\) in \(v\) is at most \(e-1\). Indeed, if the derivatives of orders \(0,\ldots,e-1\) all vanished, then

\[
\partial_v^{\,e-1}R=e!\,v
\]

would first give \(v=0\). At zero, for every \(i=2,\ldots,e\),

\[
\partial_v^{\,e-i}R(\beta,0)=(e-i)!\,\beta_i.
\]

All these coefficients would vanish, contradicting \(\beta_j=\pm1\). This calculation proves the strict decrease throughout the compact closure, including its boundary; mere nonvanishing on the open cell would not suffice.

The induction hypothesis for analytic order, applied to \(R\) and this bounded map, now gives a nondegenerate reduction in \(v\). Pull it back through \(v=w/q\). The positive-power pullback theorem preserves a nonnegative exponent. Multiply by the base factor \(q^e\). This proves a nondegenerate reduction of \(\widehat P\) on the inner bands as well.

### Restore the analytic factor and the coordinate

The Weierstrass factor is nonzero near its actual compact image. In the coordinate \(w\), its bounded original arguments are recovered analytically from bounded base parameters and \(w\); on a fixed sign band \(w=\sigma|w|\). It is consequently a unit with translation zero. Give its reduction and the polynomial's reduction a common translation using the explicit distance-substitution theorem, then multiply.

The common-translation construction replaces a distance by a positive base factor times either the zeroth or first power of the new distance times a positive unit. Hence nonnegative exponents remain nonnegative. This point also covers the nonvanishing factor, whose exponent was zero.

Finally pull back the affine change \(w=z+a_1/e\). A translation \(\eta(x)\) in \(w\) becomes \(\eta(x)-a_1(x)/e\) in \(z\), and the positive distance is unchanged exactly:

\[
|w-\eta|=|z-(\eta-a_1/e)|.
\]

The bounded unit argument map is therefore the same map after substitution. The new center's graph is disjoint from the pulled-back cell because the old center's graph was disjoint from the image cell. Coefficients, unit domains and nonnegative exponents all persist.

There were finitely many normalization boxes, finitely many Weierstrass boxes and finitely many scale and sign pieces. In the inner case the integer analytic-order bound strictly decreased; in the outer case the polynomial reduced immediately. The induction terminates. Multiplying back the signed normalizing coefficient \(g_m\) completes the ordinary preparation statement. \(\square\)

This proves ordinary nondegenerate preparation with the lower-dimensional induction as its sole cell input. Together with the unit, translation, dominance, power-coordinate and bounded-argument proofs, it discharges those particular inputs in the preceding splitting and balanced calculation. The next sections conclude the full two-coordinate assembly and joint dimension induction, and then prove arbitrary \(\mathcal L\)-preparation and globally subanalytic cell decomposition.


## Full analytic reduction in a coordinate and its inverse

We complete Valette's Proposition 1.6.14 using the analytic split, actual-image localization, unit arguments and ordinary preparation already proved. The cell input throughout this section remains the explicit lower-dimensional package.

**Two-coordinate preparation.** Let \(C\subset\mathbb R^n\) be an \(\mathcal L\)-cell on which \(z\ne0\), with base \(B\). Let \(c,\phi_1,\ldots,\phi_k\) be \(\mathcal L\)-functions on \(B\), and suppose

\[
\Phi(x,z)=(\phi(x),z,c(x)/z)
\]

is bounded on \(C\). If \(\psi\) is analytic near \(K=\overline{\Phi(C)}\), then \(\psi\circ\Phi\) is reducible on a finite cell refinement.

The base function \(c\) is bounded: writing \(w=c/z\), we have \(c=zw\), and every base point has a nonempty fibre. Make all base functions analytic by the lower-dimensional package. Graph cells use lower-dimensional substitution. Separate \(c=0\), where the function is the ordinary analytic composition \(\psi(\phi,z,0)\). On the remaining bands \(c\) and \(z\) are nonzero, with fixed signs.

### The finite localization really has compatible cells

At a point of \(K\) where \(z\ne0\), the function

\[
F_z(u,c,z)=\psi(u,z,c/z)
\]

is analytic near the corresponding point \((u,zw,z)\). Choose a closed box inside this domain, bounded away from \(z=0\). Its inverse image is described by finitely many bounds on the base functions \((\phi,c)\) and constant bounds on \(z\). Thus the lower-dimensional package and finite endpoint refinement make it a union of cells. Ordinary preparation applies on those cells.

At a point where \(w\ne0\), use instead

\[
F_w(u,c,w)=\psi(u,c/w,w).
\]

The map \(H(x,z)=(x,c(x)/z)\) is an analytic monotone fibre map on the nonzero fixed-sign branches. It is the power-coordinate map with \(p=-1\) and scale \(\operatorname{sign}(z)c\). Its image is a cell. Choose a closed analytic-domain box for \(F_w\), bounded away from \(w=0\); refine its inverse image in the \(w\)-coordinate by base bounds and constant endpoints. Pull the resulting cells back with the proved power-coordinate construction. Ordinary preparation in \(w\), followed by that pullback, reduces the original function on these pieces.

Only actual points \((a,0,0)\in K\) need the convergent splitting lemma. Around such a point choose a closed \(u\)-box and sufficiently small closed \(z,w\)-intervals, so the identity

\[
\psi(u,z,w)=z\psi_+(u,zw,z)+\psi_-(u,zw,w)
\]

holds, with both outer functions analytic on neighborhoods of the compact argument boxes. Bounds on \(\phi,z,w\) again give compatible finite refinements: the first bounds are lower-dimensional, the second are constant endpoints, and the last pull back constant endpoints under \(H\). The independent \(c\)-radius in the convergence proof contains \(c=zw\) on these chosen boxes.

These neighborhoods form an open cover of the actual compact image \(K\); extract a finite subcover and take a common refinement of their inverse images. This proves the required localization without assuming preparation of arbitrary sets in the current dimension and without extending \(\psi\) to a larger product of parameter closures.

### Keep the two nondegenerate reductions before changing coordinates

On a splitting piece set

\[
X_+=z\psi_+(\phi,c,z),\qquad
X_-=\psi_-(\phi,c,c/z).
\]

Ordinary preparation supplies a nondegenerate reduction of \(\psi_+(\phi,c,z)\) in \(z\) and of \(\psi_-(\phi,c,w)\) in \(w\). The latter is then pulled back through \(w=c/z\). Hence both \(X_+\) and \(X_-\) are reducible.

Retain their original ordinary reductions as well as their pulled-back reductions. On finite refinements these give

\[
|X_+|\asymp |z|\,|a_+(x)|\,|z-\theta_+(x)|^r,
\qquad
|X_-|\asymp |a_-(x)|\,|c/z-\theta_-(x)|^s,
\qquad r,s\ge0.
\]

The nonnegative exponents refer to the respective \(z\) and \(w\) reductions, before the inverse-coordinate pullback. That pullback is not asserted to preserve them. Restricting these formulas to further cells preserves their compact unit bounds.

Separate zero coefficients first. If either contribution vanishes, the other is the whole function. Otherwise apply the dominance refinement with \(\epsilon=1/2\) to their pulled-back reductions. Each resulting piece is dominant in one direction or has \(|X_+|\asymp|X_-|\).

### Dominance gives an analytic unit, not just bounds

Suppose \(|X_+|\le |X_-|/2\) and \(X_-\ne0\). Give the two functions a common translation and write their ratio as

\[
R=X_+/X_-=A(x)y^\lambda V(x,y),
\qquad |R|\le1/2,
\]

where \(V\) is an analytic unit. The monomial \(A y^\lambda\) is bounded because \(V\) is bounded away from zero. Collect this monomial together with all bounded arguments representing \(V\) into two coordinates. Their analytic recovery map represents \(R\) by an analytic outer function near the new compact argument closure.

On that closure the recovered ratio lies in \([-1/2,1/2]\), by continuity and approximation from actual argument values. Consequently \(1+R\) is represented by an analytic function taking values in \([1/2,3/2]\) there. It remains nonzero on a neighborhood of the compact closure and is an analytic \(\mathcal L\)-unit in \(y\). Thus

\[
X_++X_-=X_-(1+R)
\]

is reduced. This proves the needed analytic unit representation rather than inferring it from uniform nonvanishing alone. Interchanging the two contributions handles the other dominant case. A zero denominator in this calculation was already separated.

### The balanced scale completes the analytic reduction

Now suppose both contributions are nonzero and comparable. Apply the zero-translation/comparison dichotomy to the retained ordinary reductions in \(z\) and in \(w\). Pull the latter refinements back through \(H\) and take a common refinement. Graph pieces are lower-dimensional cases. The nondegenerate exponents in the respective ordinary coordinates remain nonnegative, since that dichotomy replaces each distance by a base factor times either the zeroth or first power of the new distance times a unit.

If \(|z|\asymp|\theta_+|\), choose \(b=|\theta_+|>0\). If \(|w|\asymp|\theta_-|\), choose \(b=|c|/|\theta_-|>0\). In either case \(|z|\asymp b\). In the remaining case both translations are zero. Comparability then says

\[
|a_+|\,|z|^{r+1}
\asymp |a_-|\,|c|^s|z|^{-s},
\]

so take

\[
b=
\left(\frac{|a_-|\,|c|^s}{|a_+|}\right)^{1/(r+s+1)}.
\]

This is a positive analytic base \(\mathcal L\)-function on the refined piece; \(r+s+1>0\). No sign of a contribution, \(c\), or \(z\) has been discarded.

As in the signed balanced calculation already proved, set

\[
q=z/b,\qquad d=c/b,\qquad
\Gamma=(\phi,b,d,q).
\]

The complete map is bounded, and \(q\) is bounded away from zero. In fact \(b\asymp|z|\) and \(d=(c/z)q\). The analytic recovery map

\[
(u,b,d,q)\longmapsto(u,bq,d/q)
\]

maps \(\overline{\Gamma(C)}\) into \(K\): it is continuous there and agrees with \(\Phi\) on the actual cell. Therefore

\[
\widetilde\psi(u,b,d,q)=\psi(u,bq,d/q)
\]

is analytic near the entire transformed compact image closure. Ordinary preparation applies with last coordinate \(q\) and base parameters \((\phi,b,d)\). Pull it back through \(q=z/b\), the \(p=1\) power-coordinate map with nonzero scale on the fixed-sign branch. This reduces the original function in the balanced case.

All cases and covers are finite. This proves the full two-coordinate preparation statement. \(\square\)

## Closure under bounded analytic composition

Let \(g_1,\ldots,g_m\) be reducible on an \(\mathcal L\)-cell \(C\), assume \(G=(g_1,\ldots,g_m)\) is bounded, and let \(F\) be analytic near \(\overline{G(C)}\). Then \(F(G)\) is reducible.

Take a common finite refinement and translation, put \(y=|z-\theta|>0\), and use the bounded-argument collection proved earlier. It writes the composite as

\[
\psi\bigl(\beta(x),u(x)y^{1/s},v(x)y^{-1/s}\bigr),
\]

with \(u,v\ge0\), a bounded complete argument map, and an analytic outer function near its actual compact image closure. On each fixed-sign branch, the affine distance coordinate \(y\) carries the cell bijectively to an \(\mathcal L\)-cell with positive last coordinate.

If \(u>0\), put \(Z=u y^{1/s}\) and \(c=uv\). Both \(Z\) and \(W=v y^{-1/s}\) are bounded, and \(c=ZW\) is a bounded base function. The composite has precisely the form \(\psi(\beta,Z,c/Z)\). Apply full two-coordinate preparation in \(Z\), then the proved power-coordinate pullback with \(p=s\).

If \(u=0,v>0\), only \(W=v y^{-1/s}\) remains. Apply ordinary analytic preparation in \(W\), then the negative-power pullback with \(p=-s\). If \(u=v=0\), the composite depends only on the base and uses the lower-dimensional package, with a finite analytic box localization if needed. Thus a zero forward coefficient is never normalized to one.

Return from the distance coordinate to \(z\): on a branch with sign \(\sigma=\operatorname{sign}(z-\theta)\), a center \(\eta(x)\) in \(y\) becomes \(\theta(x)+\sigma\eta(x)\), and

\[
|y-\eta|=|z-(\theta+\sigma\eta)|.
\]

The unit argument map and disjoint-center condition are unchanged under this bijective substitution. Graph cells throughout use lower-dimensional evaluation. This proves the claimed closure. \(\square\)

## Close the dimension induction for finite expressions

We make explicit the simultaneous induction package that was used above.

In dimension \(n\), the package consists of:

1. A finite list of \(\mathcal L\)-expressions well defined on supplied \(\mathcal L\)-cells has a finite cell refinement on which every expression is reduced.
2. Such a list can be made analytic, of constant sign, and pairwise ordered.
3. Finitely many supplied cells and existing finite cell refinements admit a common finite cylindrical refinement; their finite expression domains and sign conditions are respected.

Here a finite expression uses coordinate functions and constants, restricted analytic functions on their stated compact cubes, sums, products, and rational powers on their stated real domains. General finite compositions can be expanded into such an expression. Restriction to a supplied cell does not assert a cell theorem for an arbitrary subset of its domain.

The package is immediate in dimension zero, where a cell is a point and well-defined functions have constant values. Assume it in all smaller dimensions. The preceding unit, endpoint, power-coordinate, ordinary-order and two-coordinate arguments then apply in dimension \(n\), and give bounded analytic composition closure there.

Coordinate functions are reduced. A base coordinate uses the base-function rule. The last coordinate, off its zero graph, is \(\operatorname{sign}(z)|z|\), with translation zero, exponent one and unit one; its zero graph uses the lower-dimensional rule. Constants are base functions.

Products are reduced by common translation and unit multiplication. A rational power of a nonzero reduced function is reduced on its stated real branch: fix the signs, take the corresponding rational power of the base absolute value and of the positive absolute unit, and multiply the exponent by that rational number. The unit power is analytic on a neighborhood of its positive compact image. Integer powers include their constant sign factor. Zero pieces are treated only where the power is defined; positive powers extended to zero give zero, while negative powers exclude zero. The exponent-zero function is the constant one on its stated domain. No convention about an undefined \(0^0\) or a negative noninteger branch is introduced.

For a sum \(f+g\), the dominance/comparability refinement supplies pieces where, after possibly exchanging \(f,g\), \(|f|\le M|g|\) for a fixed finite \(M\). Separate \(g=0\), which then also forces \(f=0\). Otherwise \(R=f/g\) is reduced and bounded. Bounded analytic composition, applied to the analytic function \(h(t)=1+t\), reduces \(1+R\), including all its cancellation zeros. Multiplication by \(g\) reduces \(f+g\). In this argument \(1+R\) is not claimed to be a unit: it may vanish.

A restricted analytic composition of already reduced inputs is reduced by the bounded analytic composition theorem, since its well-defined inputs lie in its stated compact cube. If a generator is defined to be zero outside that cube, first refine using the coordinate bounds on its already treated inputs. Use the sum case just proved to reduce their differences from the constant cube endpoints: both terms are already reduced. Those differences have constant sign after base refinement. On each resulting piece either the input is in the cube, including its boundary, or the generator is the constant zero. Thus the usual zero-extended convention causes no extra arbitrary-set assumption. Induction on the finite expression complexity proves assertion 1 without an assumption about arbitrary current-dimensional cell decomposition.

A reduced function is analytic on its cell: its positive distance, rational powers and bounded analytic unit arguments are analytic there. Refine its base so its coefficient has constant sign, using the lower-dimensional package. The distance is positive and the nonvanishing continuous unit has constant sign on the connected cell. Thus the function has constant sign. Apply the already proved expression result to the finitely many pairwise differences to order any finite list. This proves assertion 2.

For assertion 3, first use the smaller-dimensional package to refine all bases of the finitely many supplied cells, then order their finite endpoint functions there. Their distinct graphs and intervening bands form the required finite cylindrical refinement, with outer infinite bands included. Apply this also to the finitely many cells in all the expression refinements just obtained. A reduction restricts to a subcell: its old center remains disjoint, its bounded image closure is a subset of the old closure, and its analytic base coefficients restrict analytically. Sign conditions, hence the stated finite expression domains, remain respected. This proves assertion 3.

The simultaneous dimension induction closes. Every finite \(\mathcal L\)-expression on an \(\mathcal L\)-cell is reducible, and the analytic/sign/order/common-refinement package is now a theorem in every dimension. Its proof has used neither an arbitrary-set cell theorem nor a complement theorem as an induction input. \(\square\)

## The global definition and its elementary set operations

We now give the arbitrary-set cell theorem and global preparation, completing the dimension argument above. We use the classical convention of Jean-Marie Lion and Jean-Philippe Rolin, [Théorème de préparation pour les fonctions logarithmico-exponentielles](https://www.numdam.org/item/10.5802/aif.1583.pdf), §0.1: embed \(\mathbb R^n\) in the product \(P^n\), where \(P=\mathbb P^1(\mathbb R)\); require a global semianalytic set to be locally semianalytic at every point of that compact product; define global subanalytic sets by coordinate projections of global semianalytic sets.

This specifies the compactification used in the proof. Valette's printed radial map \(x/\sqrt{1+|x|^2}\) has open-ball image, while its stated target is a cube. We therefore make the product convention explicit and prove the required product and projection facts in its actual coordinate charts. No comparison across a ramified compactification boundary is an input.

Semianalytic means a finite Boolean combination of analytic equalities and strict inequalities in a neighborhood of every ambient point. Non-strict inequalities can be expressed as a strict inequality or an equality. The product \(P^n\) has standard coordinate charts using \(x_i\) or \(1/x_i\) in each coordinate. Each is a product of analytic one-dimensional charts; \(P^n\) is compact.

The following elementary constructions use only these definitions.

**Polynomial sign sets are globally semianalytic.** In a chart with inverted coordinates indexed by \(I\), a polynomial becomes a rational expression in the chart coordinates \(u_i\). On the part belonging to \(\mathbb R^n\), all \(u_i\) for \(i\in I\) are nonzero. Choose a sufficiently large even exponent in each such coordinate and multiply the expression by the positive monomial

\[
D(u)=\prod_{i\in I}u_i^{2d_i}>0.
\]

The result is a polynomial in \(u\), and its sign and zero locus agree with the original expression on this part. Add the analytic conditions \(u_i^2>0\) for the inverted coordinates; these exclude points at infinity. Every finite polynomial sign formula thus has a semianalytic description in every projective product chart. This proves the assertion without using a polynomial projection theorem.

**Finite unions, intersections and products of global semianalytic sets are global semianalytic.** Near each product-chart point, take the finitely many analytic formulas for the factors, pull them back under the coordinate projections, and combine them by the relevant Boolean operation. Cylinders are included: \(\mathbb R\subset P\) is semianalytic, with condition \(u\ne0\) near its point at infinity. Coordinate permutations are analytic on the product, so preserve this property.

Let \(A=\pi Z\subset\mathbb R^n\) and \(B=\pi W\subset\mathbb R^n\) be global subanalytic sets, with witness variables \(u\in\mathbb R^p\) and \(v\in\mathbb R^q\). Then

\[
\begin{aligned}
A\cup B
&=\pi_{x}\{(x,u,v):(x,u)\in Z\ \text{or}\ (x,v)\in W\},\\
A\cap B
&=\pi_{x}\{(x,u,v):(x,u)\in Z\ \text{and}\ (x,v)\in W\}.
\end{aligned}
\]

The witness sets are globally semianalytic by the cylinder constructions. Products use the product witness followed by a coordinate permutation. Further coordinate projections simply concatenate the forgotten witness variables. Hence global subanalytic sets are closed under finite unions, intersections, products and coordinate projections, before any complement theorem has been proved.

For a globally subanalytic map, its graph and these operations give images and inverse images of global subanalytic subsets by graph intersection followed by projection. They also give joint graphs, composition and restrictions of such maps. For example, a sum or product of two functions is described by their two graphs and the polynomial relation \(v=s+t\) or \(v=st\), with \(s,t\) projected out. Rational-power graphs on their stated positive real branches are polynomial sign sets: for \(q=a/b\), \(b>0\), use \(t,y>0\) and \(y^b=t^a\) if \(a\ge0\), or \(y^bt^{-a}=1\) if \(a<0\). Defined zero or integer branches are added by their corresponding polynomial conditions.

A restricted analytic function on a compact cube has a bounded graph. It is semianalytic near that cube by the analytic graph equation and the cube inequalities. Its compact graph closure avoids every point at infinity, so near those points the graph is empty. Its graph is therefore globally semianalytic. These primitive graphs and the graph constructions show that every finite \(\mathcal L\)-expression, restricted to a globally subanalytic domain on which it is defined, has a globally subanalytic graph.

The same conclusion holds for an analytic outer function defined only near a compact argument image: cover that image by finitely many closed boxes inside the analytic domain, use the restricted analytic graph on each box, and take the finite union of the resulting restricted graphs. Their values agree on overlaps. This does not require an analytic extension outside the given neighborhood.

Induction now shows that every \(\mathcal L\)-cell is globally subanalytic. Its base is such a set; the graph case uses the endpoint's graph, and the band case uses the endpoints' joint graphs and polynomial order inequalities followed by projection. Infinite endpoints omit the corresponding inequality. These facts provide the set-theoretic input independently of the expression preparation theorem.

## Finite analytic cells for arbitrary globally subanalytic sets

**Cell theorem.** For any finite list of globally subanalytic subsets of \(\mathbb R^n\), there is a finite cylindrical decomposition of \(\mathbb R^n\) into analytic \(\mathcal L\)-cells compatible with every set in the list.

We first treat a globally semianalytic set \(Z\subset\mathbb R^N\), considered as a subset of \(P^N\). Around every point of \(P^N\), choose a standard product chart and an open neighborhood on which a finite analytic sign formula defines \(Z\). Inside it choose a closed coordinate box whose interior contains the point and whose closure remains inside the analytic domain and chart. Compactness supplies a finite such box cover.

On the finite part of one selected chart, write

\[
\chi_i(x)=x_i\quad\text{or}\quad\chi_i(x)=1/x_i.
\]

The latter requires \(x_i\ne0\). These chart domains first have a finite \(\mathcal L\)-cell refinement by cuts at the coordinate zero hyperplanes. On each such cell all \(\chi_i\) are well-defined \(\mathcal L\)-expressions.

For a chosen closed box \(Q\), its finite-chart trace \(W=\chi^{-1}(Q)\) is described by finitely many sign conditions on \(\chi_i-\alpha_i\) and \(\beta_i-\chi_i\), together with the chart-domain conditions. Apply the now proved analytic/sign/common-refinement package for finite expressions. This gives a finite cell decomposition compatible with \(W\). Take a common refinement for all the selected boxes. They cover all of \(\mathbb R^N\); on every resulting cell choose a box containing its chart image.

Inside that box the local defining analytic functions for \(Z\) are restricted analytic functions. Their composites with \(\chi\) are well-defined \(\mathcal L\)-expressions on the chosen cell. Prepare them and refine to make every defining sign constant. The local sign formula is then either true throughout a cell or false throughout it. Thus \(Z\) is a union of cells in a finite \(\mathcal L\)-cell decomposition of \(\mathbb R^N\). Every analytic function has stayed inside its selected box's actual domain.

For a global subanalytic set \(A\subset\mathbb R^n\), take a globally semianalytic witness \(Z\subset\mathbb R^{n+p}\) with \(A=\pi Z\). Apply the result just proved to \(Z\). In a cylindrical decomposition, projection of a cell onto its first coordinates is its parent cell; each graph or band has a nonempty fibre over every point of that parent. Repeated projection therefore gives the induced decomposition of \(\mathbb R^n\), after removing duplicate projected cells. Since \(Z\) is a union of cells, \(A\) is a union of cells in this induced decomposition.

Finally, for finitely many \(A_i\), take a common finite refinement of the finitely many constructed \(\mathcal L\)-cell decompositions, using the already closed expression package. This proves the full cell theorem, including unbounded sets and simultaneous compatibility. \(\square\)

## Full global preparation and the complement theorem

Let \(f:E\to\mathbb R\) be a globally subanalytic function; no continuity is assumed. Its graph has a finite \(\mathcal L\)-cell decomposition in \(\mathbb R^{n+1}\). The induced base decomposition is compatible with \(E\), since \(E\) is the graph's projection.

Over a base cell \(C\subset E\), a cell included in the graph cannot be a band: it would give several values at each base point. It must be a graph cell, and there is exactly one such graph over \(C\): at least one exists because the projection contains \(C\), and two would contradict the single-valuedness of \(f\). Its endpoint is an analytic \(\mathcal L\)-function equal to \(f\) on \(C\). Apply expression preparation on these finitely many base cells and take a common refinement.

Thus every globally subanalytic function is reducible, with the complete analytic unit form defined earlier. This is the full preparation theorem, not just ordinary nondegenerate preparation. The exponent may be negative. \(\square\)

If \(A\subset\mathbb R^n\) is globally subanalytic, apply the cell theorem compatible with \(A\). Its complement is the union of the other finitely many cells, and each cell is globally subanalytic by the elementary graph constructions. This proves Gabrielov's complement theorem for the stated global class.

Closure and interior also belong to this class. Indeed

\[
x\in\overline A
\quad\Longleftrightarrow\quad
\text{for every }\epsilon>0\text{ there exists }y\in A
\text{ with }\sum_i(x_i-y_i)^2<\epsilon^2.
\]

The existential condition is a projection of a global subanalytic set using a polynomial inequality. Its failure for some positive \(\epsilon\) is obtained by complement, intersection with \(\epsilon>0\), and projection. Taking the final complement gives \(\overline A\). Then \(\operatorname{int}A=\mathbb R^n\setminus\overline{\mathbb R^n\setminus A}\), and the same operations give its boundary and locally closed differences.

Cells are connected by the graph and band parametrizations already proved. Every connected component of a finite union of cells is a union of whole cells: a connected cell meeting that component is contained in it. Consequently a globally subanalytic set has finitely many connected components, each globally subanalytic.

## Local subanalytic sets and bounded charts

For clarity we prove the comparison used by the course's local analytic geometry. A locally subanalytic set is, near every finite ambient point, the projection of a relatively compact semianalytic witness whose compact closure lies in its analytic domain.

**Compact witness observation.** Such a witness, after a closed base-box restriction inside that neighborhood, has a globally semianalytic representative. Cover its compact closure by finitely many closed boxes lying inside local analytic formula neighborhoods. In each box intersect its finite sign formula with the closed-box inequalities. This gives a bounded semianalytic set in the whole Euclidean ambient space, empty near infinity. The finite union of these sets is exactly the restricted witness. It is therefore globally semianalytic in the projective product convention.

Suppose a bounded set \(A\subset\mathbb R^n\) is locally subanalytic at every point of its ambient closure. Its closure is compact. Cover it by finitely many smaller closed base boxes inside subanalytic witness neighborhoods. The compact witness observation makes each \(A\)-trace on such a box a projection of a globally semianalytic witness. Their finite union is \(A\). Hence \(A\) is globally subanalytic.

Conversely let \(A=\pi Z\) be globally subanalytic, and fix a closed bounded base box \(Q\). The product \(Q\times P^p\) is compact. Cover it by finitely many semianalytic formula boxes for \(Z\), using the ordinary coordinates on the finite base and standard projective charts on the witness coordinates. In each chart the witness variables have bounded chart coordinates \(u\); for an inverted witness coordinate require \(u_i\ne0\), so it corresponds to an actual finite witness. Keep the base condition \(x\in Q\). Each resulting witness is bounded semianalytic with compact closure in its formula domain. Projection onto the unchanged base coordinates gives \(A\cap Q\); the finite union of these projections is locally subanalytic. Thus every global subanalytic set is locally subanalytic at every finite point.

In particular local subanalytic sets in a chart restricted to a compact box contained in their analytic neighborhood can use the global cell and preparation theorems just proved. This comparison concerns the relevant bounded chart traces; it makes no global definability assertion about an arbitrary unbounded analytic manifold or map.

## Uniform finiteness in families

Let \(A\subset\mathbb R^{m+n}\) be globally subanalytic and write \(A_t=\{x:(t,x)\in A\}\). Choose a cylindrical decomposition with the parameter coordinates first, compatible with \(A\).

After fixing \(t\), each cell has either an empty fibre or a graph or band cell in the remaining coordinates. This follows inductively from the cell definition: specialise its endpoints on each parent fibre, and keep its nonempty intervals or graphs. The specialised endpoints are analytic on their specialised analytic base cells. The resulting nonempty cells form a finite decomposition of \(\mathbb R^n\) compatible with \(A_t\), with at most the total number \(N\) of original cells.

Each such fibre cell is connected. Therefore the number of connected components of \(A_t\) is at most \(N\), independently of \(t\). Each component is a finite union of these globally subanalytic fibre cells.

For a globally subanalytic family of maps \(f_t:A_t\to B_t\), regard its graph with coordinates ordered as \((t,b,x)\). The sets \(f_t^{-1}(b)\) are fibres of that one globally subanalytic graph over \((t,b)\). The same argument bounds their number of connected components by one finite constant independent of both parameters. This retains the joint definability requirement on a family, rather than treating an arbitrary collection of individually definable fibres as a definable family.

## Convergent Puiseux expansions

We prove the one-variable and parameterized statements in Valette's Propositions 1.8.4, 1.8.6 and 1.8.7 from the full preparation theorem. Convergence, the domain of the analytic outer function, and the choice of a two-sided substitution are part of the proof.

### One variable

Let \(f:(0,\epsilon)\to\mathbb R\) be globally subanalytic. After reducing \(\epsilon\), preparation gives one band next to zero and a formula

\[
f(t)=a|t-\theta|^r
\psi\bigl(\beta,u|t-\theta|^{1/s},v|t-\theta|^{-1/s}\bigr),
\qquad r\in\mathbb Q,\quad s\in\mathbb Z_{>0},
\]

where the base quantities are constants, the complete argument map is bounded, and \(\psi\) is an analytic unit near its actual compact image closure. We may take \(u,v\ge0\). If \(a=0\), the zero series suffices.

If \(\theta=0\), boundedness of \(v t^{-1/s}\) as \(t\downarrow0\) forces \(v=0\). The point \((\beta,0,0)\) lies in the actual image closure. Thus

\[
\psi(\beta,uT,0)=\sum_{j=0}^{\infty}b_jT^j
\]

is a genuinely convergent power series for \(|T|\) small. Multiplication by \(a t^r\), with \(T=t^{1/s}\), gives a convergent Puiseux series. Choose a positive integer \(p\) divisible by \(s\) and by the denominator of \(r\); its exponents are integers divided by \(p\), with only finitely many negative exponents.

If \(\theta\ne0\), shrink the interval so \(t<|\theta|/2\). The distance \(|t-\theta|\) is a positive analytic function of \(t\) across zero. Its rational powers and the forward and inverse unit arguments are analytic there. Their value at zero is in the actual compact image closure, so the analytic domain of \(\psi\) includes it. Hence \(f\) has an ordinary convergent Taylor series in this case.

Combining the cases proves

\[
f(t)=\sum_{i=m}^{\infty}a_i t^{i/p},
\qquad m\in\mathbb Z,\quad p\in\mathbb Z_{>0},
\]

on a smaller positive interval. If \(f\) is bounded, a lowest nonzero negative power would make it unbounded, so no such power occurs. If \(f(t)\to0\), its constant coefficient is also zero.

For finitely many bounded functions choose a common denominator \(L\) for all series. The substitution \(t=\tau^{2L}\) gives analytic functions across \(\tau=0\): all cleared exponents are even nonnegative integers, so their series agree with the actual functions for both signs of \(\tau\). Merely saying that the substitution exponent is even is insufficient; for example, \(\sqrt{\tau^2}=|\tau|\), whereas \(\sqrt{\tau^4}=\tau^2\). \(\square\)

### A compact analytic Taylor observation

We will also need convergence with parameters, not merely formal coefficients. Let \(H(b,T)\) be real analytic on a neighborhood of \(K_0\times\{0\}\), with \(K_0\) compact. There is a \(\delta>0\) such that

\[
H(b,T)=\sum_{j\ge0}H_j(b)T^j,\qquad
H_j(b)=\frac{1}{j!}\partial_T^jH(b,0),
\]

for \(b\) in a real neighborhood of \(K_0\) and \(|T|<\delta\), after possibly shrinking that neighborhood. Every \(H_j\) is analytic there. On compact subsets of a smaller parameter neighborhood the series converges uniformly for \(|T|\le\delta/2\).

To see this, at each \((b_0,0)\) the convergent real analytic series has a holomorphic extension on a complex product polydisc. Shrink its parameter polydisc and take a smaller closed disc in \(T\); the extension is bounded there. The one-variable Cauchy estimate gives a geometric majorant for the Taylor series on a still smaller \(T\)-disc, uniformly for those real parameters. Finitely many parameter neighborhoods cover \(K_0\); take the least of their positive radii. The Taylor coefficients on overlaps agree, because they are the displayed derivatives of the same real analytic function. The resulting real series therefore agree without requiring a single chosen complex extension on all the parameter neighborhoods.

The rational power \((1-\sigma T)^q\), for \(\sigma=\pm1\) and \(q\in\mathbb Q\), is analytic for real \(T\) sufficiently close to zero and has the branch with value one there. It can be used in this observation on any compact parameter set.

### Continuous functions with parameters

Let \(A\subset\mathbb R^n\) be globally subanalytic. Suppose \(f\) is continuous and globally subanalytic on a relatively open neighborhood \(U\) of \(A\times\{0\}\) in \(A\times\mathbb R_{\ge0}\). Then there is a finite partition of \(A\) into globally subanalytic analytic manifolds \(C\), and one even positive integer \(p\), such that

\[
(x,\tau)\longmapsto f(x,\tau^p)
\]

is real analytic on a neighborhood of \(C\times\{0\}\) in \(C\times\mathbb R\). This is a neighborhood in the analytic manifold \(C\); its width in \(\tau\) may depend on \(x\).

Apply cylindrical preparation with the \(x\)-coordinates first, compatible with \(U\) and \(A\times\{0\}\). Over each resulting base cell \(C\subset A\), the graph \(t=0\) is a cell. The adjacent positive band belongs to \(U\): every point \((x,0)\) has a positive interval in \(U\), and compatibility makes membership constant on that band. Shrink an infinite upper endpoint to one if necessary. On this band, after further base refinement, write

\[
f(x,t)=a(x)|t-\theta(x)|^r
\psi\bigl(\beta(x),u(x)|t-\theta(x)|^{1/s},
v(x)|t-\theta(x)|^{-1/s}\bigr).
\]

All base functions are analytic on \(C\); make \(a\) either identically zero or nowhere zero, and \(\theta\) either identically zero or of one fixed nonzero sign.

If \(a=0\), the formula and continuity give the zero function also at \(t=0\).

If \(a\ne0\) and \(\theta=0\), boundedness of the argument map for every fixed \(x\) forces \(v(x)=0\). Nonvanishing of the unit at the limit point, together with continuity of \(f\), forces \(r\ge0\). Choose \(p\) divisible by \(2s\) and by twice the denominator of \(r\). The integers \(p/s\) and \(pr\) are even and nonnegative, so

\[
f(x,\tau^p)
=a(x)\tau^{pr}
\psi\bigl(\beta(x),u(x)\tau^{p/s},0\bigr).
\]

At each \((x_0,0)\), the limiting argument \((\beta(x_0),0,0)\) lies in the original compact closure. Its analytic neighborhood and the analytic base functions give a neighborhood on which this formula is jointly analytic in \(x,\tau\). It agrees with \(f(x,\tau^p)\) when \(\tau\ne0\), for both signs of \(\tau\); continuity gives equality at zero.

If \(\theta\ne0\), put \(T(x)=|\theta(x)|>0\) and \(\sigma=\operatorname{sign}\theta\). For \(0\le t<T(x)/2\),

\[
|t-\theta(x)|=T(x)\bigl(1-\sigma t/T(x)\bigr).
\]

All powers and unit arguments are jointly analytic near each \((x_0,0)\). The limiting argument at that point belongs to the actual compact closure, so composition with \(\psi\) is legitimate. This gives an analytic extension in \(t\) across zero, agreeing at zero by continuity. Its composition with any even power of \(\tau\) gives the required extension.

There are finitely many pieces. Choose one \(p\) divisible by twice every \(s\) and every rational-exponent denominator appearing on them. The local analytic formulas agree where their neighborhoods overlap within a given piece, since they agree on the positive-\(t\) side and hence by analytic uniqueness. Their union is the claimed neighborhood. \(\square\)

### Parameterized Laurent–Puiseux series without continuity

Let \(A\) be globally subanalytic, let \(\zeta:A\to(0,\infty)\) be globally subanalytic, and let \(f\) be globally subanalytic on

\[
E=\{(x,t):x\in A,\ 0<t<\zeta(x)\}.
\]

There is a finite partition of \(A\) into globally subanalytic analytic manifolds \(C\), one positive integer \(p\), and on each \(C\) a positive continuous globally subanalytic function \(\xi\), with \(0<\xi\le\zeta\), such that

\[
f(x,t)=\sum_{i=m_C}^{\infty}a_i(x)t^{i/p},
\qquad 0<t<\xi(x).
\]

Each coefficient \(a_i\) is analytic on \(C\). The series converges there; on compact parameter subsets and a sufficiently smaller positive radius it converges locally uniformly in the root variable. Neither continuity at \(t=0\) nor a common positive radius over an unbounded parameter cell is assumed.

Prepare \(f\), refining so \(\zeta\) is analytic on each base cell. As above, over every \(C\) there is a bottom band \(0<t<\eta(x)\) contained in \(E\), where \(\eta>0\) is analytic and \(\eta\le\zeta\). Retain the prepared formula just displayed and separate the same zero/nonzero coefficient and center cases.

Suppose first \(\theta=0\) and \(a\ne0\). Again \(v=0\), but \(r\) may now be negative. The map \(\beta\) is bounded. Moreover

\[
K_0=\overline{\beta(C)}\times\{0\}\times\{0\}
\subset \overline{\{(\beta(x),u(x)t^{1/s},0):
x\in C,\ 0<t<\eta(x)\}}.
\]

Indeed for any sequence of parameter points with \(\beta(x_j)\) convergent, choose \(t_j<\eta(x_j)\) sufficiently small that \(u(x_j)t_j^{1/s}\to0\). Thus \(\psi\) is analytic near the compact set \(K_0\). The compact Taylor observation supplies a single \(\delta>0\) and analytic coefficients \(b_j(\beta)\) for

\[
\psi(\beta,W,0)=\sum_{j\ge0}b_j(\beta)W^j.
\]

Consequently

\[
f(x,t)=\sum_{j\ge0}
a(x)b_j(\beta(x))u(x)^j\,t^{r+j/s}.
\]

All coefficients are analytic on \(C\). Choose

\[
\xi(x)=\min\left\{\frac{\eta(x)}2,\
\left(\frac{\delta}{2(1+|u(x)|)}\right)^s\right\}.
\]

This is positive, continuous and globally subanalytic, and keeps the analytic argument within the smaller convergence disc. A common denominator for \(r\) and \(1/s\) gives the stated integer indexing, filling absent exponents with zero. The lower index is finite, even when \(r<0\).

Suppose next \(\theta\ne0\), and retain \(T=|\theta|>0\) and its fixed sign \(\sigma\). Set

\[
U_0(x)=u(x)T(x)^{1/s},\qquad
V_0(x)=v(x)T(x)^{-1/s}.
\]

These functions, together with \(\beta\), are bounded: for fixed \(x\) they are limits as \(t\downarrow0\) of the bounded complete argument map, with the same global bounds. The compact closure of \((\beta,U_0,V_0)(C)\) lies in the original argument closure. To verify this also for varying \(x\), choose for each \(x_j\) a sufficiently small \(t_j<\eta(x_j)\) so the actual argument is within \(1/j\) of its limiting argument.

The analytic function

\[
H(\beta,U_0,V_0,\tau)
=(1-\sigma\tau)^r
\psi\bigl(\beta,U_0(1-\sigma\tau)^{1/s},
V_0(1-\sigma\tau)^{-1/s}\bigr)
\]

is defined near that compact parameter closure at \(\tau=0\). Its argument recovery map is continuous there and at zero takes values in the original compact closure. Choose a uniform small radius \(\delta>0\) by the compact Taylor observation, reducing it below \(1/2\). Then

\[
f(x,t)=\sum_{j\ge0}
a(x)T(x)^{r-j}H_j(\beta(x),U_0(x),V_0(x))\,t^j
\]

for

\[
0<t<\xi(x):=
\min\{\eta(x)/2,\ \delta T(x)/2\}.
\]

This is an ordinary Taylor series with analytic parameter coefficients and positive continuous globally subanalytic radius. The coefficient-zero case uses the zero series and \(\xi=\eta/2\).

Finally take one denominator \(p\) for the finitely many pieces. The chosen radii are globally subanalytic by their explicit formulas and the already proved closure operations. On a compact subset of a base cell, the analytic base factors are bounded, and the Taylor majorants above give uniform convergence after reducing the root radius. A finite number of negative powers merely gives a finite Laurent part on the punctured interval. This proves the full parameterized Laurent–Puiseux assertion. \(\square\)

The [curve-selection and Łojasiewicz treatment](../curve-selection-and-lojasiewicz.html) can now use the cell, complement and Puiseux results as proved providers. Its existing choice and curve arguments remain the single treatment of those steps.

## Dimension, fibrewise closure and the frontier

*This section adapts Guillaume Valette's [On subanalytic geometry](https://arxiv.org/abs/2507.23622v1), §2.3, from its native editable source under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The dimension and frontier arguments are expanded below. The empty-set convention is separated from strict decrease; the parameter-continuity proof uses an injective bounded transform and relative closed graphs. These changes imply no endorsement.*

We first work with globally subanalytic subsets of Euclidean space in the projective product convention established above. “Definable” in this section means globally subanalytic. The finite analytic cell theorem, complement theorem, preparation and definable choice are already proved in this component and its linked curve-selection treatment. No uniformization, resolution or analytic regular-locus theorem is used here.

For a nonempty definable set \(A\subset\mathbb R^n\), choose a finite analytic cell decomposition compatible with \(A\) and define

\[
\dim A=\max\{\dim C:C\text{ is a cell contained in }A\}.
\tag{D1}
\]

Set \(\dim\varnothing=-1\). Cell dimension is its ordinary manifold dimension: a graph preserves the dimension of its parent, and a band adds one. We write

\[
\operatorname{fr}A=\overline A\setminus A,
\qquad
\partial A=\overline A\setminus\operatorname{int}A.
\tag{D2}
\]

These are different sets. The frontier in the first formula is the one for which strict dimension decrease holds. All closures and interiors in the Euclidean statements use the ambient Euclidean topology.

### Why cell dimension is intrinsic

We use the following elementary fact about differentiable manifolds: a nonempty open subset of a \(d\)-dimensional manifold cannot be covered by finitely, or even countably, many differentiable submanifolds of smaller dimension that are contained in it. Here is the volume argument. Work in one manifold coordinate chart. A smaller-dimensional submanifold has a countable cover by parameter charts and then by compact parameter boxes on which the parameter map into \(\mathbb R^d\) has bounded derivative, hence is Lipschitz. Cover one \(k\)-dimensional box by at most \(c\delta^{-k}\) boxes of side \(\delta\). Their images are contained in \(d\)-dimensional boxes of side at most \(c'\delta\). Their total outer volume is at most

\[
c''\delta^{d-k}\longrightarrow0\qquad(k<d).
\tag{D3}
\]

Thus each compact chart image, and then their countable union, has zero \(d\)-dimensional outer volume. A nonempty open set contains a box of positive volume. Countable subadditivity gives the asserted impossibility. This argument uses only coverings by Euclidean boxes; it requires no Sard theorem.

If differentiable manifolds \(D\subset C\) are embedded in the same Euclidean space, then \(\dim D\le\dim C\). Indeed every tangent vector of \(D\) is the derivative of a curve in \(D\), hence in \(C\), giving an inclusion of tangent spaces. The inclusion into \(C\) is differentiable in its local manifold coordinates, so the volume argument also applies to smaller-dimensional manifolds contained in \(C\).

Now refine any two compatible finite cell decompositions to a common finite analytic cell decomposition. Every refined cell inside an old cell \(C\) has dimension at most \(\dim C\). They cover \(C\); if all had smaller dimension they would contradict the preceding volume argument in a coordinate neighborhood of \(C\). At least one has dimension \(\dim C\). Consequently the maximum in (D1) does not change under refinement and is independent of the chosen decomposition. In particular

\[
A\subset B\Longrightarrow\dim A\le\dim B,
\qquad
\dim(A_1\cup\cdots\cup A_s)=\max_i\dim A_i.
\tag{D4}
\]

The same reasoning shows that a differentiable definable manifold has its manifold dimension as its definable dimension. Permuting Euclidean coordinates, or applying a definable differentiable diffeomorphism, preserves dimension: it carries the finitely many manifold cells to manifolds of the same dimensions, and a compatible cell refinement of their images has the same maximum by the argument just given.

### Images, graphs and fibre dimensions

**Image inequality.** For any definable map \(f:A\to\mathbb R^p\), including a discontinuous map, and definable \(E\subset A\),

\[
\dim f(E)\le\dim E.
\tag{D5}
\]

**Proof.** Decompose the graph \(G=\Gamma_{f|E}\) cylindrically, with the \(x\)-coordinates first. Over a base cell contained in \(E\), each succeeding output coordinate must be a graph rather than a band, since there is exactly one complete value of \(f\) over each \(x\). At each stage there is exactly one such graph over that parent: there is at least one by existence of \(f(x)\), and two would violate uniqueness. Thus every graph cell has the same dimension as its \(x\)-base and \(\dim G=\dim E\).

Reorder the coordinates with the output first, and take a compatible cylindrical decomposition there. A coordinate projection of a cell removes successive graph or band coordinates and cannot increase its dimension. The image is the finite union of the projected cells, so its dimension is at most \(\dim G\). Coordinate reordering has preserved \(\dim G\), proving (D5). The empty case is immediate. \(\square\)

Applying (D5) to a definable bijection and its inverse proves dimension invariance under arbitrary definable bijections; continuity is not needed. In particular every definable cell can be replaced by its definable analytic coordinates without changing dimensions. Those coordinates can be obtained by forgetting its graph coordinates: its remaining free coordinates range over an open definable subset of \(\mathbb R^d\), and successive analytic graph functions reconstruct the cell.

For \(A\subset\mathbb R^{m+n}\), put

\[
A_t=\{x\in\mathbb R^n:(t,x)\in A\},
\qquad A_B=A\cap(B\times\mathbb R^n).
\tag{D6}
\]

A cylindrical decomposition with the \(t\)-coordinates first has finitely many base cells \(B\). Over each \(B\), the fibre dimension is constant whenever its fibres are nonempty: each cell of \(A_B\) has a nonempty fibre over every \(t\in B\), and its fibre dimension is its total dimension minus \(\dim B\). Taking the largest such cell gives

\[
\dim A_B=\dim B+\dim A_t\quad(t\in B, A_t\ne\varnothing).
\tag{D7}
\]

A base cell with empty fibres contributes nothing. Thus \(\dim A\) is the maximum of these sums. In particular, if \(\dim A\le m\), then its fibres over every full \(m\)-dimensional base cell are finite or empty. A zero-dimensional definable set is finite because its cell decomposition consists of finitely many points.

### Closure commutes with fibres after partitioning the base

**Generic closure lemma.** Given definable \(A\subset\mathbb R^{m+n}\), there is a dense definable \(B\subset\mathbb R^m\) such that

\[
(\overline A)_t=\overline{A_t}\qquad(t\in B).
\tag{D8}
\]

**Proof.** The inclusion \(\overline{A_t}\subset(\overline A)_t\) always holds. Define the exceptional set where the inclusion is strict. It is definable: closure has the distance-and-quantifier description proved above, and the complement/projection operations express the existence of a point in the set difference.

Suppose that exceptional set contained a full-dimensional cell. It is open. Definable choice selects on it a point \(a(t)\in(\overline A)_t\) and a radius \(r(t)>0\) with \(B(a(t),r(t))\cap A_t=\varnothing\). Preparation makes these finitely many coordinate functions continuous on a finite analytic cell refinement. At least one cell of the refinement is still full-dimensional, by dimension invariance. Denote this open cell by \(C\). Then

\[
U=\{(t,x):t\in C,\ |x-a(t)|<r(t)\}
\tag{D9}
\]

is open in the whole product, is disjoint from \(A\), and contains \((t,a(t))\in\overline A\). This contradicts the definition of closure. The exceptional set therefore has dimension less than \(m\), and in particular contains no nonempty open set. Its complement is the required dense definable \(B\). For \(m=0\), there is no exceptional fibre. \(\square\)

**Partitioned closure lemma.** There is a finite definable partition \(\mathcal P\) of \(\mathbb R^m\) such that

\[
(\overline{A_B})_t=\overline{A_t}
\qquad(B\in\mathcal P, t\in B).
\tag{D10}
\]

Here the closure on the left is the ambient closure of the *restricted* family. It is not generally the fibre of \(\overline A\) at exceptional parameters.

**Proof.** Induct on the dimension of the base. In the dense good set from (D8), any cell \(C\) has the asserted property, by the inclusions

\[
\overline{A_t}\subset(\overline{A_C})_t
\subset(\overline A)_t=\overline{A_t}\qquad(t\in C).
\tag{D11}
\]

Every cell in the exceptional set has smaller dimension. Identify such a cell \(C\) with its open definable analytic coordinate domain \(V\subset\mathbb R^d\), \(d<m\), and pull the family back to \(V\times\mathbb R^n\). Apply the induction hypothesis in \(\mathbb R^d\), taking empty fibres off \(V\). Transfer the resulting finite partition back to \(C\). At a point \(t\in C\), closure in the product restricted to \(C\) is the same as ambient closure tested at that point, and the coordinate homeomorphism preserves this local closure. This gives (D10) there.

Finally refine all the finitely many resulting pieces if necessary. The property survives refinement: for \(C\subset B\) and \(t\in C\), squeeze \((\overline{A_C})_t\) between \(\overline{A_t}\) and \((\overline{A_B})_t\). The induction terminates in dimension zero. \(\square\)

### Strict frontier decrease

**Frontier theorem.** For every nonempty definable set \(A\),

\[
\dim(\overline A\setminus A)<\dim A,
\qquad \dim\overline A=\dim A.
\tag{D12}
\]

For the empty set, both dimensions are \(-1\); only the equality is asserted. This small convention matters in dimension-zero induction arguments.

**Proof.** Put \(k=\dim A\) and suppose a cell \(D\subset\overline A\setminus A\) had dimension \(m\ge k\). Near one point, \(D\) is an analytic graph over an open set in \(\mathbb R^m\). Shrink to a bounded analytic coordinate neighborhood with compact closure inside that graph chart. Subtracting its analytic graph function is a definable analytic change of coordinates there; its graph on the selected compact chart is semianalytic, so the bounded-chart comparison proved above supplies definability. In the new coordinates a nonempty open patch of \(D\) is

\[
V\times\{0\}\subset\overline{A'}\setminus A'.
\tag{D13}
\]

Here \(A'\) is the transformed, restricted set. Its dimension is at most \(k\), by (D5) and the restriction inequality. Every point of the displayed patch is still a limit of \(A'\), since the selected coordinate neighborhood is open around that point.

Decompose \(A'\) cylindrically over \(\mathbb R^m\). Exclude its finitely many lower-dimensional base cells; their union has empty interior. Over any remaining full-dimensional base cell its fibre dimension is at most \(k-m\le0\), by (D7). The fibres there are consequently finite or empty, hence closed. Also exclude the exceptional parameters of (D8). The union of these two exceptional sets has dimension less than \(m\), by (D4), so it cannot contain the nonempty open \(V\). Choose \(t\in V\) outside it. We obtain

\[
0\in(\overline{A'})_t=\overline{A'_t}=A'_t,
\tag{D14}
\]

contradicting (D13). If \(m=0\), there are no lower-dimensional nonempty base cells or exceptional parameters, and the same argument uses the unique base point. Thus every frontier cell has dimension less than \(k\). Since \(\overline A=A\cup\operatorname{fr}A\), (D4) gives the equality in (D12). \(\square\)

It follows that a definable \(A\subset\mathbb R^n\) is nowhere dense precisely when \(\dim A<n\). In one direction, an \(n\)-dimensional cell is open and precludes nowhere density. In the other, its closure has the same smaller dimension by (D12) and hence contains no open cell or open set.

The topological boundary always has dimension less than the *ambient* dimension:

\[
\dim\partial A<n.
\tag{D15}
\]

Indeed \(A\setminus\operatorname{int}A\) has no \(n\)-dimensional cell: any such cell is open and contained in \(A\), hence in its interior. The other part of the boundary is \(\operatorname{fr}A\), whose dimension is also less than \(n\). Their finite union proves (D15). However \(\dim\partial A<\dim A\) is false in general; a closed line in \(\mathbb R^2\) has itself as topological boundary and empty frontier.

### Fibrewise continuous functions become jointly continuous on base pieces

**Parameter-continuity theorem.** Let \(f:A\to\mathbb R\) be definable, where \(A\subset\mathbb R^{m+n}\). If every fibre function \(f_t:A_t\to\mathbb R\) is continuous in its relative topology, there is a finite definable partition \(\mathcal P\) of the base such that \(f|_{A_B}\) is continuous for every \(B\in\mathcal P\).

**Proof.** Use the definable analytic homeomorphism

\[
\psi:\mathbb R\longrightarrow(-1,1),\qquad
\psi(s)=\frac{s}{\sqrt{1+s^2}},\qquad
\psi^{-1}(u)=\frac{u}{\sqrt{1-u^2}}.
\tag{D16}
\]

The positive square roots have semialgebraic graphs, so both maps are definable. Set \(h=\psi\circ f\). It is bounded and its fibre functions are continuous. Apply (D10) to \(\Gamma_h\), with \(t\) as base and \((x,u)\) as fibre coordinates.

Fix \((t,x)\in A_B\) and a sequence \((t_j,x_j)\in A_B\) tending to it. Each subsequence of the bounded values \(h(t_j,x_j)\) has a convergent further subsequence in \([-1,1]\). Write its limit as \(u\). Then

\[
(x,u)\in(\overline{(\Gamma_h)_B})_t
=\overline{\Gamma_{h_t}}.
\tag{D17}
\]

Since \(x\in A_t\) and \(h_t\) is continuous there, its graph is closed *relative to* \(A_t\times\mathbb R\). Thus \(u=h_t(x)\). Every convergent further subsequence has that same limit, which implies convergence of the whole bounded sequence. This proves continuity of \(h\) on \(A_B\). Composing with \(\psi^{-1}\), continuous at the attained value in \((-1,1)\), proves continuity of \(f\). \(\square\)

Relative closedness in this argument cannot be replaced by ambient closedness: \(A_t\) itself need not be closed. Nor can one use a noninjective bounded function as a substitute for (D16); continuity of that composite need not recover continuity of \(f\).

### Transfer to local analytic geometry

In an analytic manifold chart, restrict a locally subanalytic set to a smaller closed box contained in its analytic witness neighborhood. The bounded-chart comparison above makes that trace globally subanalytic. Apply (D12) there and restrict back to the interior of the box. Near a given interior point, its frontier agrees with the frontier of the original trace. Analytic coordinate changes preserve local dimension by (D5) applied on bounded charts in both directions.

More explicitly, the dimension of a set germ is the eventual value of the dimensions of its intersections with shrinking chart balls. These integer values are nonincreasing and stabilize; the same is true for the frontier germ. Choose one small ball after both have stabilized and inside a bounded witness chart. The preceding frontier theorem gives

\[
\dim_x(\overline A\setminus A)<\dim_x A
\tag{D18}
\]

whenever the germ of \(A\) is nonempty. If the frontier germ is empty, its dimension is \(-1\). Empty germs are treated separately. This is the strict dimension drop needed when successively adjoining lower-dimensional boundary pieces in the relative triangulation construction.

Similarly (D5) applies locally to analytic or locally subanalytic maps whose restricted graphs lie in bounded witness charts. A proper map permits compact preimage localization when its images are considered near a compact target box. This supplies the precise dimension nonincrease after such localization; arbitrary unbounded graphs are not silently declared globally subanalytic.

These arguments supply the dimension, frontier and closure providers. They do not yet prove the analytic regular-locus, uniformization or constant-rank partition theorems. Those remain distinct prerequisites rather than consequences asserted from a dimension count.

### Exercises with complete solutions

**Exercise D1 (basic: two boundaries).** In \(\mathbb R^2\), calculate the frontier and topological boundary of the unit circle \(S^1\) and of the open unit disc. Give their dimensions and identify which strict inequality applies.

**Solution.** The circle is closed with empty interior in \(\mathbb R^2\). Therefore \(\operatorname{fr}S^1=\varnothing\), of dimension \(-1\), and \(\partial S^1=S^1\), of dimension one. Its own dimension is one, so strict frontier decrease holds while strict decrease of topological boundary relative to the set fails. The open disc has dimension two; its closure is the closed disc and both its frontier and its topological boundary are the circle, of dimension one. In both examples the topological boundary has dimension less than the ambient dimension two.

**Exercise D2 (intermediate: the exceptional parameter).** Let \(A=\{(t,x):t>0,\ x=t\}\subset\mathbb R^2\). Determine exactly where \((\overline A)_t=\overline{A_t}\) fails. Give a base partition satisfying (D10), and explain why restricting before taking closure matters.

**Solution.** For \(t>0\), both sets are \(\{t\}\); for \(t<0\), both are empty. At \(t=0\), \(A_0=\varnothing\) but \((\overline A)_0=\{0\}\), so this is the unique exception. Use the partition \(( -\infty,0),\{0\},(0,\infty)\). On its first two pieces the restricted family is empty, and its closure is empty. On the positive piece the fibre equality holds at each parameter in that piece. Although its closure accumulates at parameter zero, zero is not a parameter of that positive piece. Thus (D10) asserts equality on each piece only after restricting the family; it does not assert that the original ambient closure commutes with all fibres.

**Exercise D3 (advanced: continuity and bounded transforms).** Define

\[
f(t,x)=
\begin{cases}
\dfrac{tx}{t^2+x^2},&(t,x)\ne(0,0),\\
0,&(t,x)=(0,0).
\end{cases}
\]

Show that every \(x\)-fibre is continuous although \(f\) is not jointly continuous. Find a base partition making it continuous on the corresponding product pieces. Finally show why \(s/(1+s^2)\) cannot replace the injective transform (D16).

**Solution.** For \(t\ne0\) the denominator is everywhere positive, so the fibre is continuous. For \(t=0\) the function is identically zero, including at \(x=0\), so that fibre is continuous too. Along \(x=t\ne0\) its value is \(1/2\), whereas at the origin its value is zero. Thus it is not jointly continuous. The partition \(( -\infty,0),\{0\},(0,\infty)\) works: on either open parameter half-line the same positive-denominator formula is continuous jointly; on the zero piece the function is zero. For the last claim let \(g(0)=1/2\) and \(g(t)=2\) when \(t\ne0\). This definable function is discontinuous at zero, but \(g/(1+g^2)=2/5\) everywhere. Continuity of the bounded composite therefore does not imply continuity of \(g\). The inverse in (D16) is precisely what prevents this loss of information.
