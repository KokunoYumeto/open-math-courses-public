# Algebraization

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The preceding lesson produced a normal complex surface germ \((X,x)\), singular only at \(x\), whose derivations form a free module of rank two. This lesson replaces it by an affine algebraic surface with the same completed local ring, and deduces the main theorem of the course. Approximating the defining equations of the germ by algebraic ones does not by itself keep their relations, and so need not keep the complete local ring. The remedy, in Section 1, is to approximate the equations and a matrix of their relations together: an exact relation between the approximations, together with closeness of sufficiently high order, forces the same complete local ring. Freeness of the derivations then descends from the completion (Section 3).

**Prerequisites.** [*Derivations and the Lipman–Zariski problem*](derivations-and-the-lipman-zariski-problem.md), Lemmas 1.2 and 1.3 and Proposition 3.4; [*Analytic realization and contraction*](analytic-realization-and-contraction.md), Proposition 4.1. From *Commutative algebra for geometry* (AG-CA): [*Noetherian and Artinian rings*](course:AG-CA/noetherian-and-artinian-rings), Theorems 5.1 and 6.1 (Artin–Rees, Krull intersection); [*Completion*](course:AG-CA/completion), Theorems 3.1, 3.2 and 4.1; [*Henselian local rings and henselization*](course:AG-CA/henselian-local-rings-and-henselization), Theorem 4.2; [*Discrete valuation rings, normal rings and Serre's criterion*](course:AG-CA/discrete-valuation-rings-normal-rings-and-serres-criterion), Corollary 4.5; [*Smooth algebras over a field and the Jacobian criterion*](course:AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion), Corollary 2.2. From *Complex analytic spaces and coherent sheaves*: [*Analytic germs, local parametrization and the Nullstellensatz*](course:complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz), Theorem 5.1, and [*Coherent sheaves and Oka's theorem*](course:complex-analytic-spaces-and-coherent-sheaves/coherent-sheaves-and-okas-theorem).

## 1. Finite determinacy of equations with relations

Put \(P=\mathbb C[[x_1,\ldots,x_e]]\) with maximal ideal \(\mathfrak n\). Let \(f=(f_1,\ldots,f_s)\in\mathfrak nP^s\) be a row, \(I=(f_1,\ldots,f_s)\), \(R=P/I\) with maximal ideal \(\mathfrak m_R=\mathfrak nR\), and write a bar for reduction modulo \(I\). Choose an \(s\times t\) matrix \(D\) whose columns generate all relations among \(f_1,\ldots,f_s\), so that
\[
P^t\xrightarrow{\ D\ }P^s\xrightarrow{\ f\ }I\longrightarrow0
\tag{1.1}
\]
is exact, the first map sending a column \(c\in P^t\) to \(Dc\) and the second sending \(c\in P^s\) to \(fc=\sum_if_ic_i\). Define
\[
\begin{gathered}
\psi:R^s\to R^t,\ v\mapsto v\bar D,\qquad K=\ker\psi,\\
J=\sum_{j=1}^eR\,\overline{\partial_jf}\subset R^s .
\end{gathered}
\]
Differentiating \(fD=0\) gives \((\partial_jf)D+f\,\partial_jD=0\), hence \(\overline{\partial_jf}\,\bar D=0\) and \(J\subset K\). Tensoring (1.1) with \(R\) gives the presentation \(R^t\to R^s\to I/I^2\to0\), and dualizing,
\[
\begin{gathered}
K=\operatorname{Hom}_R(I/I^2,R),\\
T^1=K/J .
\end{gathered}
\tag{1.2}
\]

**Lemma 1.1 (finite determinacy with a relation matrix).** Suppose \(T^1\) has finite length. There are integers \(N,n_0\), depending only on \(f\) and \(D\), with the following property. If a row \(g\in P^s\) and an \(s\times t\) matrix \(B\) over \(P\) satisfy
\[
\begin{gathered}
gB=0,\qquad g-f\in\mathfrak n^{n_0}P^s,\\
B-D\in\mathfrak n^NP^{s\times t},
\end{gathered}
\]
then there are a continuous \(\mathbb C\)-algebra automorphism \(\Phi\) of \(P\), with \(\Phi(x_j)\equiv x_j\pmod{\mathfrak n^2}\), and a matrix \(U\in GL_s(P)\), with \(U\equiv1\pmod{\mathfrak n}\), such that \(f=\Phi(g)\,U\). In particular \(P/(g)\cong P/(f)\) as complete local \(\mathbb C\)-algebras.

**Proof.** *Constants.* For a map \(u:M\to M'\) of finite modules over a Noetherian local ring with maximal ideal \(\mathfrak a\), the Artin–Rees lemma applied to \(\operatorname{im}u\subset M'\) gives \(a\ge0\) with \(\operatorname{im}u\cap\mathfrak a^rM'\subset\mathfrak a^{r-a}\operatorname{im}u=u(\mathfrak a^{r-a}M)\) for \(r\ge a\). Choose \(\alpha,\beta,d\ge0\) such that, whenever the exponents are nonnegative,
\[
\begin{gathered}
\operatorname{im}\psi\cap\mathfrak m_R^rR^t\subset\psi(\mathfrak m_R^{r-\alpha}R^s),\\
K\cap\mathfrak m_R^rR^s\subset\mathfrak m_R^{r-\beta}K,
\end{gathered}
\]
\[
I^{\oplus s}\cap\mathfrak n^rP^s\subset\{fC:\ C\in\mathfrak n^{r-d}P^{s\times s}\},
\]
the last from Artin–Rees for \(P^{s\times s}\to P^s\), \(C\mapsto fC\), whose image is \(I^{\oplus s}\). Since \(K/J\) has finite length, choose \(\ell\) with \(\mathfrak m_R^\ell K\subset J\). Put
\[
\begin{gathered}
c_0=\beta+\ell,\quad c=c_0+d,\quad N\ge\alpha+1,\\
n_0\ge\max\{c+N,\ c+2,\ 2c+1\}.
\end{gathered}
\]

*One step.* Let \(n\ge n_0\), \(h=g-f\in\mathfrak n^nP^s\), \(B-D\in\mathfrak n^N\), \(gB=0\). Reducing modulo \(I\), where \(\bar g=\bar h\),
\[
\begin{aligned}
\bar h\bar D&=\bar g\bar D=-\bar g(\bar B-\bar D)\\
&=-\bar h(\bar B-\bar D)\in\mathfrak m_R^{n+N}R^t .
\end{aligned}
\]
So there is \(\bar\epsilon\in\mathfrak m_R^{n+N-\alpha}R^s\subset\mathfrak m_R^{n+1}R^s\) with \(\psi(\bar\epsilon)=\psi(\bar h)\), and
\[
\begin{aligned}
\kappa=\bar h-\bar\epsilon&\in K\cap\mathfrak m_R^nR^s\\
&\subset\mathfrak m_R^{n-\beta}K\subset\mathfrak m_R^{n-c_0}J .
\end{aligned}
\]
Write \(\kappa=\sum_j\bar a_j\overline{\partial_jf}\) with \(\bar a_j\in\mathfrak m_R^{n-c_0}\), lift to \(a_j\in\mathfrak n^{n-c_0}\), and lift \(\bar\epsilon\) to \(\epsilon\in\mathfrak n^{n+1}P^s\). Then \(w=h-\sum_ja_j\partial_jf-\epsilon\) reduces to zero, so \(w\in I^{\oplus s}\cap\mathfrak n^{n-c_0}P^s\), and \(w=fC\) with \(C\in\mathfrak n^{n-c}P^{s\times s}\). Thus
\[
\begin{gathered}
h=\sum_{j=1}^ea_j\,\partial_jf+fC+\epsilon,\\
a_j,C\in\mathfrak n^{n-c},\quad \epsilon\in\mathfrak n^{n+1}P^s .\qquad(1.3)
\end{gathered}
\]
(The derivative combination may have lower order than \(h\), because a derivative of an equation can be a unit; this is why only \(n-c\) is claimed.) Put \(q=n-c\); the choice of \(n_0\) gives \(q\ge\max\{N,2\}\) and \(2q\ge n+1\). Define
\[
\begin{gathered}
\phi(x_j)=x_j-a_j,\\
g_{\mathrm{new}}=\phi(g)(1+C)^{-1},\\
B_{\mathrm{new}}=(1+C)\,\phi(B).
\end{gathered}
\]
Since \(a_j\in\mathfrak n^2\), \(\phi\) is an automorphism with identity linear part, and \(1+C\) is invertible. Substitution moves every power series by an element of the ideal \((a_1,\ldots,a_e)\subset\mathfrak n^q\). Taylor expansion gives \(\phi(f)-f+\sum_ja_j\partial_jf\in\mathfrak n^{2q}P^s\), and, \(h\) having order at least \(n\), \(\phi(h)-h\in\mathfrak n^{n+q-1}P^s\). With (1.3) and \(2q\ge n+1\), \(n+q-1\ge n+1\),
\[
\begin{aligned}
\phi(g)&=\phi(f)+\phi(h)\\
&\equiv f-\sum_ja_j\partial_jf+h\\
&\equiv f(1+C)\pmod{\mathfrak n^{n+1}P^s},
\end{aligned}
\]
so \(g_{\mathrm{new}}-f\in\mathfrak n^{n+1}P^s\). Exactly, \(g_{\mathrm{new}}B_{\mathrm{new}}=\phi(g)\phi(B)=\phi(gB)=0\). Finally
\[
\begin{aligned}
B_{\mathrm{new}}-D&=C\phi(B)+(\phi(B)-B)\\
&\quad+(B-D)\in\mathfrak n^NP^{s\times t},
\end{aligned}
\]
since \(q\ge N\). The equation precision has grown from \(n\) to \(n+1\), and the relation precision \(N\) is kept.

*Iteration.* Start with \((g,B)\) at \(n=n_0\) and repeat. With \(\phi_n,M_n=(1+C_n)^{-1}\) the corrections at stage \(n\), put \(\Phi_{n_0}=\mathrm{id}\), \(U_{n_0}=1\), \(\Phi_{n+1}=\phi_n\circ\Phi_n\), \(U_{n+1}=\phi_n(U_n)M_n\); then \(g_n=\Phi_n(g)U_n\) at every stage. Since \(\phi_n\) moves every series into \(\mathfrak n^{n-c}\) and \(M_n-1\in\mathfrak n^{n-c}\), the \(\Phi_n(x_j)\) and the \(U_n\) converge in the complete ring \(P\) to \(\Phi(x_j)\) and \(U\). The limit substitution \(\Phi\) has identity linear part, hence is an automorphism, and \(U\equiv1\pmod{\mathfrak n}\) is invertible. Since \(g_n-f\in\mathfrak n^n\), passing to the limit gives \(f=\Phi(g)U\). Then \(\Phi\) maps \((g)\) onto \((f)\) and induces \(P/(g)\cong P/(f)\). \(\square\)

The matrix \(D\) must generate all relations, so that (1.2) holds; the approximating matrix \(B\) need not: its exact product \(gB=0\) and its closeness to \(D\) suffice.

## 2. Two results from the literature

**A1 (Artin's approximation theorem).** Let \(H\) be the henselization of \(\mathbb C[x_1,\ldots,x_e]\) at the origin, whose completion is \(P\). If a finite system of polynomial equations with coefficients in \(H\) has a solution in \(P\), then for every \(c\) it has a solution in \(H\) agreeing with the given one modulo \(\mathfrak n^c\). [M. Artin, *Algebraic approximation of structures over complete local rings*, Publ. Math. IHÉS 36 (1969), Theorem 1.10; freely readable on Numdam.]

**A2 (completions of analytic local rings).** If \(S\) is a normal complex analytic local ring, its completion \(\widehat S\) is a normal domain. [The ring \(\mathbb C\{T_1,\ldots,T_n\}\) of convergent power series is excellent: A. Grothendieck, *Éléments de géométrie algébrique* IV, Remark (7.8.4)(v), proved in §18. Quotients of excellent rings are excellent, and an excellent local ring is normal if and only if its completion is: Scholium (7.8.3)(ii) and (v) there. EGA IV is freely readable on Numdam (Publ. Math. IHÉS 24, 28, 32), and an English edition is at github.com/KokunoYumeto/ega-en. A normal local ring is a domain.]

## 3. The algebraic neighbourhood

**Proposition 3.1 (algebraization of an isolated germ).** Assume A1 and A2. Let \((X,x)\) be a normal complex analytic germ of dimension \(d\ge1\), smooth away from \(x\), whose module of derivations is free of rank \(d\). There are a finitely generated normal integral \(\mathbb C\)-algebra \(A\) and a maximal ideal \(\mathfrak p\) with
\[
\begin{gathered}
\dim A=d,\qquad A/\mathfrak p=\mathbb C,\\
\widehat{A_{\mathfrak p}}\cong\widehat{\mathcal O_{X,x}},\qquad \operatorname{Der}_{\mathbb C}(A)\cong A^d,
\end{gathered}
\]
and \(\operatorname{Spec}A\) smooth away from \(\mathfrak p\). If \(x\) is a singular point, \(A_{\mathfrak p}\) is not regular.

**Proof.** *The completed presentation.* Embed the germ in \((\mathbb C^e,0)\) and write \(S=\mathcal O_{X,x}=\mathbb C\{x_1,\ldots,x_e\}/I_{\mathrm{an}}\). Choose a row \(f\) generating \(I_{\mathrm{an}}\) and a matrix \(D\) generating its relations over the convergent power series ring, which is Noetherian. Completion is exact on finite modules (Theorem 3.1 of the lesson on completion), so \(f,D\) give (1.1) over \(P\), with \(R=\widehat S=P/(f)\). By A2, \(R\) is a normal domain, and by Theorem 4.1 of the lesson on completion, \(\dim R=\dim S=d\), and \(R\) is regular if and only if \(S\) is.

*Finite length of \(T^1\).* The analytic version of (1.2), \(T^1_{\mathrm{an}}=\operatorname{Hom}_S(I_{\mathrm{an}}/I_{\mathrm{an}}^2,S)/J_{\mathrm{an}}\), is the stalk at \(x\) of a coherent sheaf on \(X\). At a smooth point \(y\ne x\), the ideal of \(X\) is generated near \(y\) by \(e-d\) functions with independent differentials, the given generators \(f\) generate the same ideal near \(y\) (coherence of the ideal sheaf), and the cokernel of the Jacobian map vanishes at \(y\). So the support of the coherent sheaf lies in \(\{x\}\), and by the analytic Nullstellensatz its stalk is a finite module annihilated by a power of \(\mathfrak m_x\): it has finite length. Since \(\operatorname{Hom}\) of a finitely presented module commutes with the flat base change \(S\to R\) (Lemma 1.3 of the first lesson), \(T^1=T^1_{\mathrm{an}}\otimes_SR\), of finite length. So Lemma 1.1 applies to \(f,D\).

*Derivations of the completion.* As in the proof of Proposition 4.1 of the preceding lesson, the derivations of \(S\) are the \(v\in S^e\) with \(\sum_jv_j\,\overline{\partial_jf_i}=0\) for all \(i\); by hypothesis this module is free of rank \(d\). Flat base change gives
\[
\begin{aligned}
&\operatorname{Der}^{\mathrm{cont}}_{\mathbb C}(R)\\
&\quad=\Bigl\{v\in R^e:\ \sum_jv_j\overline{\partial_jf_i}=0\\
&\qquad\text{for all }i\Bigr\}\cong R^d,\qquad(3.1)
\end{aligned}
\]
the module of derivations continuous for the \(\mathfrak m_R\)-adic topology: such a derivation is determined by its values on the \(x_j\), and the displayed equations say that it descends from \(P\).

*Approximation.* Let \(H\) be the henselization of \(\mathbb C[x_1,\ldots,x_e]\) at the origin. The system \(\sum_iG_iB_{i\nu}=0\), \(1\le\nu\le t\), in the entries of a row \(G\) and a matrix \(B\), has the solution \((f,D)\) in \(P\). By A1 it has a solution \((g,B)\) in \(H\) agreeing with \((f,D)\) modulo \(\mathfrak n^{\max(n_0,N)}\). By Lemma 1.1, \(P/(g)\cong R\).

*An étale neighbourhood.* By Theorem 4.2 of the lesson on henselization, \(H\) is the filtered colimit of the local rings of pointed étale neighbourhoods of the origin, with residue field \(\mathbb C\). The finitely many entries of \(g\) and \(B\), and the finitely many identities \(gB=0\), are therefore defined and valid on one affine étale neighbourhood \(\operatorname{Spec}E\to\mathbb A^e\) with a marked point \(\mathfrak q\) over the origin; its completed local ring is \(P\). Put \(A'=E/(g)\), \(\mathfrak p'=\mathfrak q/(g)\), \(T=A'_{\mathfrak p'}\). Then \(\widehat T=P/(g)\cong R\).

*Descent.* Since \(E\) is étale over \(\mathbb A^e\), \(\Omega_{E/\mathbb C}\) is free on \(dx_1,\ldots,dx_e\) near \(\mathfrak q\), and \(\Omega_{T/\mathbb C}\) has the Jacobian presentation by the \(dg_i\). Completing gives the continuous Jacobian presentation of \(P/(g)\), and through \(P/(g)\cong R\) and (3.1),
\[
\operatorname{Der}_{\mathbb C}(T)\otimes_T\widehat T\cong\operatorname{Der}^{\mathrm{cont}}_{\mathbb C}(\widehat T)\cong\widehat T^d
\]
(Lemma 1.3 of the first lesson). Let \(M=\operatorname{Der}_{\mathbb C}(T)\). Its fibre \(M/\mathfrak m_TM\) has dimension \(d\); lifting a basis gives, by Nakayama's lemma, a surjection \(T^d\to M\), which becomes a surjection between free modules of rank \(d\) over \(\widehat T\), hence an isomorphism; by faithful flatness of completion (Theorem 3.2 of the lesson on completion), \(M\cong T^d\). The ring \(T\) injects into the domain \(\widehat T\), so it is a domain. It is normal: if \(a/b\) is integral over \(T\), it is integral over the normal domain \(\widehat T\), so \(a\in b\widehat T\cap T=bT\), the last equality by faithful flatness. Completion preserves dimension and regularity, so \(\dim T=d\), and \(T\) is not regular if \(S\) is not.

*The singular locus.* Let \(\mathfrak j_{\mathrm{an}}\subset S\) be the ideal of \((e-d)\)-minors of the Jacobian matrix of \(f\), the \(d\)-th Fitting ideal of the module of differentials of \(S\). At a smooth point \(y\ne x\), the differentials of the generators \(f\) span a space of dimension \(e-d\), as above; so the zero set of \(\mathfrak j_{\mathrm{an}}\) on \(X\) is contained in \(\{x\}\), and by the analytic Nullstellensatz \(\mathfrak m_S^b\subset\mathfrak j_{\mathrm{an}}\) for some \(b\). Fitting ideals are defined by minors of presentation matrices, so they commute with base change; through the completed presentations and faithful flatness,
\[
\mathfrak m_T^b\subset\operatorname{Fitt}_d(\Omega_{T/\mathbb C}).
\]

*The affine surface.* Since \(T\) is a domain, exactly one irreducible component of \(\operatorname{Spec}A'\) passes through \(\mathfrak p'\), and the support of the nilradical of \(A'\) does not contain \(\mathfrak p'\). Remove the other components and that support: the result is reduced and irreducible, of dimension \(d\), since its marked point is closed with local ring of dimension \(d\). By the Jacobian criterion (Theorem 2.1 and Corollary 2.2 of the lesson on smooth algebras), applied to the presentation of its differentials by the \(dx_j\) and the \(dg_i\), its nonsmooth locus is the zero set of \(\operatorname{Fitt}_d\) of its differentials, a closed set which by the containment above meets a neighbourhood of \(\mathfrak p'\) only in \(\mathfrak p'\); remove its components not containing \(\mathfrak p'\). The module of derivations is finite and localizes to \(M\cong T^d\) at \(\mathfrak p'\); a basis at \(\mathfrak p'\) is defined after inverting an element outside \(\mathfrak p'\), and the map from a free module of rank \(d\) has kernel and cokernel with closed supports avoiding \(\mathfrak p'\); remove these supports too. Choose a principal affine open neighbourhood \(\operatorname{Spec}A\) of \(\mathfrak p'\) inside all these opens and let \(\mathfrak p\) be the marked point. Then \(A\) is a finitely generated domain of dimension \(d\), smooth away from \(\mathfrak p\), with \(A_{\mathfrak p}=T\) and \(\operatorname{Der}_{\mathbb C}(A)\cong A^d\).

\(A\) is normal by Serre's criterion (Corollary 4.5 of the lesson on Serre's criterion). At a prime \(\mathfrak P\ne\mathfrak p\), \(A_{\mathfrak P}\) is a local ring of a smooth point, hence regular (Theorem 2.1 of the lesson on smooth algebras), so regular in codimension one and of depth \(\min(2,\dim A_{\mathfrak P})\) or more; at \(\mathfrak p\), \(A_{\mathfrak p}=T\) is normal of dimension \(d\), so it satisfies \((S_2)\). \(\square\)

## 4. The main theorem

**Theorem 4.1.** Assume N1–N5 of the preceding lesson and A1, A2. There are a finitely generated normal integral \(\mathbb C\)-algebra \(A\) of dimension two and a maximal ideal \(\mathfrak p\) with \(\operatorname{Der}_{\mathbb C}(A)\cong A^2\) and \(A_{\mathfrak p}\) not regular; \(\operatorname{Spec}A\) is smooth away from \(\mathfrak p\).

**Proof.** Proposition 4.1 of the preceding lesson gives a normal complex surface germ \((X,x)\), singular at \(x\) and smooth elsewhere, with free derivations of rank two. Apply Proposition 3.1 with \(d=2\). \(\square\)

The results N1–N5 and A1, A2 are established theorems of the literature; granted them, Theorem 4.1 shows that the Lipman–Zariski conjecture fails in characteristic zero.

By Proposition 3.4 of the first lesson, \(A[t_1,\ldots,t_n]\) is then a normal domain of dimension \(n+2\) with free derivation module and nonregular primes forming a closed set of codimension two.

**Two consequences, stated with references.** The free derivation module restricts to a trivial tangent bundle on the smooth locus \(U\) of \(\operatorname{Spec}A\). A theorem of Biswas, Gurjar and Kolte (*On the Zariski–Lipman conjecture for normal algebraic surfaces*, J. Lond. Math. Soc. 90 (2014), Theorem 0.1(1); arXiv:1403.5613) shows that a normal affine surface whose smooth locus has trivial tangent bundle and logarithmic Kodaira dimension at most one is smooth; so the smooth locus of the surface of Theorem 4.1 has logarithmic Kodaira dimension two. And since \(\operatorname{Der}_{\mathbb C}(A)\) is already free, the blowup of \(\operatorname{Spec}A\) along its module of derivations, which is universal for making the pullback of that module locally free modulo torsion, is \(\operatorname{Spec}A\) itself: iterating it, with or without normalization, never resolves the singular point. These two statements are not used elsewhere in the course.

## 5. Exercises

**5.1** (easy). Show that \(J\subset K\) and that \(K=\operatorname{Hom}_R(I/I^2,R)\) in the setting of Section 1.

**5.2** (medium). For the single equation \(f=x_1^2+x_2^3\) in \(\mathbb C[[x_1,x_2]]\), which has no relations (\(t=0\)), compute \(T^1\) and the least \(\ell\) with \(\mathfrak m_R^\ell K\subset J\).

**5.3** (medium). Show by an example that approximating the equations alone, without their relations, can change the complete local ring: take \(f=(x_1x_2,\ x_1x_3)\) and \(g=(x_1x_2,\ x_1x_3+x_2^k)\).

**5.4** (medium). Show that a domain \(T\) with normal completion is normal, using only faithful flatness of completion.

## 6. Solutions

**5.1.** Differentiate \(fD=0\): \((\partial_jf)D+f\,(\partial_jD)=0\); modulo \(I\) the second term vanishes. For \(K\): applying \(\operatorname{Hom}_R(-,R)\) to the presentation \(R^t\xrightarrow{\bar D}R^s\to I/I^2\to0\) identifies \(\operatorname{Hom}_R(I/I^2,R)\) with the rows \(v\in R^s\) such that \(v\bar D=0\).

**5.2.** Since \(f\) is a nonzerodivisor, \(I/I^2\cong R\) and \(K=\operatorname{Hom}_R(R,R)=R\). The derivatives give \(J=(\overline{2x_1},\overline{3x_2^2})\), so \(T^1=\mathbb C[[x_1,x_2]]/(x_1^2+x_2^3,\,x_1,\,x_2^2)\), which is \(\mathbb C[x_2]/(x_2^2)\), of length two. Since \(\mathfrak m_R^2=(x_1^2,x_1x_2,x_2^2)\subset J\) while \(x_2\notin J\), the least \(\ell\) is \(2\).

**5.3.** \(P/(f)\) defines the union of the plane \(x_1=0\) and the line \(x_2=x_3=0\), of dimension two. For \(g\), on \(x_1=0\) the second equation gives \(x_2^k=0\), so \(x_2=0\): the line \(x_1=x_2=0\); where \(x_1\ne0\), the first gives \(x_2=0\) and then the second gives \(x_3=0\): the line \(x_2=x_3=0\). So \(P/(g)\) has dimension one for every \(k\), although \(g-f\in\mathfrak n^k\). The relation \(x_3f_1-x_2f_2=0\) of \(f\) has no exact counterpart for \(g\): \(x_3g_1-x_2g_2=-x_2^{k+1}\).

**5.4.** If \(a/b\) with \(a,b\in T\), \(b\ne0\), is integral over \(T\), it is integral over \(\widehat T\) and lies in its fraction field, so it lies in \(\widehat T\) by normality: \(a\in b\widehat T\). Faithful flatness gives \(b\widehat T\cap T=bT\), so \(a\in bT\) and \(a/b\in T\).

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Section 6: finite determinacy with relations, algebraization, the main theorem, and the two consequences. The method of determining a complete local ring by its equations together with their relations goes back to H. Hironaka and is used in Artin's algebraization of isolated singularities (Publ. Math. IHÉS 36, 1969, Theorems 3.8–3.9).
- M. Artin, *Algebraic approximation of structures over complete local rings*, Publ. Math. IHÉS 36 (1969), 23–58; freely readable on Numdam. Result A1. A complete proof of a more general approximation theorem is in the Stacks project, Tag 07QY.
- A. Grothendieck, *Éléments de géométrie algébrique* IV, Publ. Math. IHÉS 24 (1965) and 32 (1967), freely readable on Numdam; English edition at github.com/KokunoYumeto/ega-en. Result A2.
