# Intersection numbers of line bundles

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On a proper scheme over a field, the Euler characteristic of a coherent sheaf twisted by several line bundles is a polynomial in the twisting exponents. Its top mixed coefficients are integers, the intersection numbers. For two line bundles on a surface they count intersection points of curves; for a line bundle on a curve they give its degree. This lesson proves the polynomial property and the basic rules for intersection numbers: multilinearity, reduction to integral components, restriction to a divisor, pullback along generically finite maps, and positivity for ample bundles. The next lessons use them to state and prove numerical criteria for ampleness.

We use the following results on coherent cohomology. The Euler characteristic \(\chi(F)=\sum_q(-1)^q\dim_kH^q(X,F)\) of a coherent sheaf on a proper \(k\)-scheme is defined and additive in short exact sequences, and for a proper morphism \(f\) one has \(\chi(Y,G)=\sum_q(-1)^q\chi(X,R^qf_*G)\): Propositions 1.1 and 1.2 of [Euler characteristics and Hilbert polynomials](course:AG-QC/euler-characteristics-and-hilbert-polynomials#1-the-finite-alternating-sum). The polynomial property for one line bundle and the positivity of its leading coefficient for ample bundles are Theorems 2.1 and 3.1 there. Every coherent sheaf has a finite filtration whose quotients are nonzero coherent ideals \(I\subseteq\mathcal O_V\) on integral closed subschemes \(V\), pushed forward to \(X\): Theorem 2.2 of [Coherence of higher direct images under proper morphisms](course:AG-QC/proper-morphisms-and-coherent-direct-images#2-integral-supports-and-coherent-filtrations); maps defined on a dense open extend after multiplying by a power of an ideal, Lemma 1.2 there; and higher direct images under proper morphisms are coherent, Theorem 4.1 there.

Throughout, \(k\) is a field, \(X\) is a proper \(k\)-scheme, and the dimension of a coherent sheaf \(F\) is \(\dim\operatorname{Supp}F\), with \(\dim0=-\infty\). For an invertible sheaf \(L\) and an integer \(n\), \(L^n\) is its \(n\)-th tensor power, and \(L^{-1}\) is the dual. For line bundles \(L_1,\dots,L_r\) and \(\mathbf n\in\mathbb Z^r\) we write \(L^{\mathbf n}=L_1^{n_1}\otimes\dots\otimes L_r^{n_r}\).

## 1. The polynomial of several twists

**Lemma 1.1** (discrete integration). Let \(d\ge0\) and let \(\varphi:\mathbb Z^r\to\mathbb Q\) be a function such that for each \(j\), the difference \(\varphi(\mathbf n+e_j)-\varphi(\mathbf n)\) is given by a polynomial in \(\mathbf n\) of total degree at most \(d-1\) (the zero polynomial if \(d=0\)). Then \(\varphi\) is given by a polynomial of total degree at most \(d\).

**Proof.** Induction on \(r\); for \(r=0\) there is nothing to prove. For a polynomial \(p(t,\mathbf m)\) of total degree at most \(d-1\), there is a polynomial \(P(t,\mathbf m)\) of total degree at most \(d\) with \(P(t+1,\mathbf m)-P(t,\mathbf m)=p(t,\mathbf m)\) and \(P(0,\mathbf m)=0\): write \(p\) in the basis \(\binom tl\mathbf m^\beta\) and use \(\binom{t+1}{l+1}-\binom t{l+1}=\binom tl\). Apply this to the first difference \(p_1(n_1,\mathbf m)\), \(\mathbf m=(n_2,\dots,n_r)\). The function \(\varphi(\mathbf n)-P(n_1,\mathbf m)\) is unchanged when \(n_1\) increases by one, so it equals \(\psi(\mathbf m)=\varphi(0,\mathbf m)\) for all \(n_1\in\mathbb Z\). The differences of \(\psi\) in the remaining directions are the restrictions of the polynomials \(p_j\) to \(n_1=0\), of degree at most \(d-1\), so \(\psi\) is a polynomial of degree at most \(d\) by induction. \(\square\)

**Theorem 1.2** (Snapper). Let \(F\) be coherent on \(X\) and let \(L_1,\dots,L_r\) be invertible. There is a unique polynomial \(P_F\in\mathbb Q[n_1,\dots,n_r]\) with

\[
P_F(\mathbf n)=\chi\bigl(F\otimes L^{\mathbf n}\bigr)\qquad(\mathbf n\in\mathbb Z^r),
\]

and its total degree is at most \(\dim F\).

**Proof.** A polynomial vanishing on \(\mathbb Z^r\) is zero, which gives uniqueness. We prove existence and the bound by induction on \(d=\dim F\). If \(F=0\), take \(P_F=0\). If \(d=0\), the support of \(F\) is finite and \(F\) lives on a finite closed subscheme, a finite product of local Artinian schemes, on which every invertible sheaf is trivial; then \(F\otimes L^{\mathbf n}\cong F\) and \(\chi\) is constant.

Let \(d\ge1\). By the filtration theorem and additivity of \(\chi\), it suffices to treat \(i_*I\), where \(i:V\to X\) is an integral closed subscheme with \(\dim V\le d\) and \(I\subseteq\mathcal O_V\) is a nonzero coherent ideal; closed pushforward preserves cohomology, so we compute on \(V\). Fix \(j\). At the generic point \(\eta\) of \(V\), the stalks \(I_\eta\) and \((I\otimes L_j)_\eta\) are one-dimensional over the function field; choose an isomorphism between them. It is defined on a dense open \(U\subseteq V\). By the extension lemma there are a coherent ideal \(J\) defining the complement of \(U\) and an exponent \(a\) such that the map extends to \(E=J^aI\to I\otimes L_j\). Both this map and the inclusion \(E\subseteq I\) are injective: their kernels are subsheaves of the torsion-free sheaf \(E\) on the integral scheme \(V\) that vanish at \(\eta\). Their cokernels \(Q_j\) and \(Q_j'\) are supported on the proper closed subset \(V\setminus U\), so they have dimension at most \(\dim V-1\le d-1\). Twisting the two exact sequences

\[
0\to E\to I\to Q_j\to0,\qquad0\to E\to I\otimes L_j\to Q_j'\to0
\]

by \(L^{\mathbf n}\) and subtracting gives

\[
\chi(I\otimes L^{\mathbf n+e_j})-\chi(I\otimes L^{\mathbf n})=\chi(Q_j'\otimes L^{\mathbf n})-\chi(Q_j\otimes L^{\mathbf n}),
\]

a polynomial of degree at most \(d-1\) by induction. Lemma 1.1 completes the proof. \(\square\)

For \(r=1\) this is Theorem 2.1 of the Euler-characteristic lesson; the proof is the same, applied in each direction separately.

## 2. Intersection numbers

**Definition 2.1.** Let \(F\) be coherent with \(\dim F\le d\), and let \(L_1,\dots,L_d\) be invertible. The *intersection number* \((L_1\cdots L_d\cdot F)\) is the coefficient of \(n_1n_2\cdots n_d\) in the polynomial \(\chi(F\otimes L_1^{n_1}\otimes\dots\otimes L_d^{n_d})\). For a closed subscheme \(Z\) with \(\dim Z\le d\) put \((L_1\cdots L_d\cdot Z)=(L_1\cdots L_d\cdot\mathcal O_Z)\). Repeated factors are written as powers: \((L^d\cdot Z)\), \((L^i\cdot M^{d-i}\cdot Z)\).

Since \(\mathcal O_Z\otimes L_i=i_*(L_i|_Z)\), the number \((L_1\cdots L_d\cdot Z)\) can be computed on \(Z\) with the restricted bundles.

**Lemma 2.2.** With \(\dim F\le d\),

\[
(L_1\cdots L_d\cdot F)=\sum_{S\subseteq\{1,\dots,d\}}(-1)^{|S|}\,\chi\Bigl(F\otimes\bigotimes_{i\in S}L_i^{-1}\Bigr).
\]

In particular it is an integer.

**Proof.** Let \(\nabla_i\) be the backward difference \(\nabla_ip(\mathbf n)=p(\mathbf n)-p(\mathbf n-e_i)\). The right side is \((\nabla_1\cdots\nabla_dP_F)(0)\). For a monomial \(\mathbf n^\alpha\) of total degree at most \(d\), \(\nabla_1\cdots\nabla_d\mathbf n^\alpha=0\) unless every \(\alpha_i\ge1\), which forces \(\alpha=(1,\dots,1)\); and \(\nabla_1\cdots\nabla_d(n_1\cdots n_d)=1\). \(\square\)

**Proposition 2.3.** Let \(\dim F\le d\) and let \(L_1,\dots,L_d\), \(L_1'\) be invertible.

1. *(Symmetry and multilinearity.)* \((L_1\cdots L_d\cdot F)\) is symmetric in the \(L_i\), and \((L_1\otimes L_1'\cdot L_2\cdots L_d\cdot F)=(L_1\cdot L_2\cdots L_d\cdot F)+(L_1'\cdot L_2\cdots L_d\cdot F)\).
2. *(Small support.)* If \(\dim F\le d-1\), then \((L_1\cdots L_d\cdot F)=0\).
3. *(Additivity.)* For an exact sequence \(0\to F'\to F\to F''\to0\) of sheaves of dimension at most \(d\), \((L_1\cdots L_d\cdot F)=(L_1\cdots L_d\cdot F')+(L_1\cdots L_d\cdot F'')\).
4. *(Components.)* Let \(V_1,\dots,V_s\) be the irreducible components of \(\operatorname{Supp}F\) of dimension \(d\), with reduced structure and generic points \(\eta_i\), and let \(\ell_i\) be the length of \(F_{\eta_i}\) over \(\mathcal O_{X,\eta_i}\). Then \((L_1\cdots L_d\cdot F)=\sum_i\ell_i\,(L_1\cdots L_d\cdot V_i)\).

**Proof.** (1) Symmetry is clear. Consider the polynomial \(Q(a,b,n_2,\dots,n_d)=\chi(F\otimes L_1^a\otimes L_1'^b\otimes L_2^{n_2}\cdots)\), of total degree at most \(d\) by Theorem 1.2. Setting \(b=0\), its coefficient of \(an_2\cdots n_d\) is \((L_1\cdot L_2\cdots\cdot F)\); setting \(a=0\), its coefficient of \(bn_2\cdots n_d\) is \((L_1'\cdot L_2\cdots\cdot F)\). Setting \(a=b=n_1\), the monomials of degree at most \(d\) that produce \(n_1n_2\cdots n_d\) are exactly \(an_2\cdots n_d\) and \(bn_2\cdots n_d\).

(2) The polynomial has degree at most \(d-1\). (3) \(\chi\) is additive after every twist.

(4) Filter \(F\) by the filtration theorem, with quotients \(i_*I_j\) on integral \(V_j'\). By (2) and (3), only factors with \(\dim V_j'=d\) contribute, and \((L\cdots\cdot I_j)=(L\cdots\cdot\mathcal O_{V_j'})\), because \(\mathcal O_{V_j'}/I_j\) has dimension at most \(d-1\). A factor with \(\dim V_j'=d\) has \(V_j'=V_i\) for some \(i\), since \(V_j'\) is an irreducible closed subset of \(\operatorname{Supp}F\) of maximal dimension. Localizing the filtration at \(\eta_i\) gives a filtration of \(F_{\eta_i}\) whose nonzero quotients are the stalks \((I_j)_{\eta_i}\) with \(V_j'=V_i\), each equal to the residue field; so exactly \(\ell_i\) factors have \(V_j'=V_i\). \(\square\)

**Proposition 2.4** (restriction to a divisor). Let \(V\subseteq X\) be a closed subscheme of dimension at most \(d\), \(d\ge1\), and let \(s\) be a section of \(L_1|_V\) such that multiplication by \(s\) is injective on \(\mathcal O_V\); for integral \(V\) this means \(s\ne0\). Let \(D\subseteq V\) be its zero scheme. Then \(\dim D\le d-1\) and

\[
(L_1\cdot L_2\cdots L_d\cdot V)=(L_2\cdots L_d\cdot D).
\]

**Proof.** Injectivity gives the exact sequence \(0\to L_1^{-1}|_V\to\mathcal O_V\to\mathcal O_D\to0\). If \(D\) contained an irreducible component of \(V\), with generic point \(\eta\), then \(s_\eta\) (in a trivialization) would lie in the maximal ideal of the Artinian local ring \(\mathcal O_{V,\eta}\), hence be nilpotent, contradicting injectivity of multiplication by \(s\) at \(\eta\). So \(D\) contains no component of \(V\), and \(\dim D\le d-1\). Twisting by \(L^{\mathbf n}=L_1^{n_1}\otimes\dots\otimes L_d^{n_d}\),

\[
\chi(\mathcal O_V\otimes L^{\mathbf n})-\chi(\mathcal O_V\otimes L^{\mathbf n-e_1})=\chi(\mathcal O_D\otimes L^{\mathbf n}).
\]

The left side is the backward difference in \(n_1\) of a polynomial of total degree at most \(d\). Among its monomials, only \(n_1n_2\cdots n_d\) contributes to the coefficient of \(n_2\cdots n_d\) after the difference: a monomial \(n_1^an_2^{b_2}\cdots\) contributes only if every \(b_i\ge1\), and then \(a\le1\) by the degree bound, while \(a=0\) is killed by the difference. So the coefficient of \(n_2\cdots n_d\) on the left is \((L_1\cdots L_d\cdot V)\). The right side is a polynomial of total degree at most \(d-1\); its monomials divisible by \(n_2\cdots n_d\) have degree \(d-1\) and cannot involve \(n_1\), so its coefficient of \(n_2\cdots n_d\) is that of \(\chi(\mathcal O_D\otimes L_2^{n_2}\otimes\dots\otimes L_d^{n_d})\), namely \((L_2\cdots L_d\cdot D)\). \(\square\)

**Corollary 2.5** (curves). Let \(C\) be an integral closed curve in \(X\) and \(L\) invertible. Then \((L\cdot C)=\chi(L|_C)-\chi(\mathcal O_C)\). If \(L|_C\) has a nonzero section with zero scheme \(D\), then \((L\cdot C)=\dim_kH^0(D,\mathcal O_D)\ge0\), with equality only if the section has no zeros.

**Proof.** For \(d=1\), \(\chi(L^n|_C)\) is a polynomial of degree at most one, and its \(n\)-coefficient is \(\chi(L|_C)-\chi(\mathcal O_C)\). The second statement is Proposition 2.4 with \(d=1\): \(D\) is finite, and \((\ \cdot D)\) with no line bundles is \(\chi(\mathcal O_D)=\dim H^0(\mathcal O_D)\). \(\square\)

We write \(\deg(L|_C)=(L\cdot C)\) for an integral curve \(C\).

## 3. Pullback and positivity

**Proposition 3.1** (pullback). Let \(f:Y\to X\) be a morphism of proper \(k\)-schemes, \(W\subseteq Y\) an integral closed subscheme of dimension \(d\), and \(L_1,\dots,L_d\) invertible on \(X\). If \(\dim f(W)<d\), then \((f^*L_1\cdots f^*L_d\cdot W)=0\). If \(\dim f(W)=d\), then

\[
(f^*L_1\cdots f^*L_d\cdot W)=e\,(L_1\cdots L_d\cdot f(W)),\qquad e=[k(W):k(f(W))],
\]

where \(f(W)\) carries its reduced structure and \(k(\cdot)\) denotes function fields.

**Proof.** Replace \(Y\) by \(W\) and \(X\) by \(T=f(W)\), a closed integral subscheme since \(f\) is proper; let \(g:W\to T\). By the projection formula \(R^qg_*(\mathcal O_W\otimes g^*M)\cong R^qg_*\mathcal O_W\otimes M\) for invertible \(M\), and the Leray formula for \(\chi\),

\[
\chi(W,g^*L^{\mathbf n})=\sum_q(-1)^q\chi\bigl(T,R^qg_*\mathcal O_W\otimes L^{\mathbf n}\bigr).
\]

The sheaves \(R^qg_*\mathcal O_W\) are coherent on \(T\). If \(\dim T<d\), all have dimension less than \(d\), and Proposition 2.3(2) gives \(0\). If \(\dim T=d\), the morphism \(g\) is dominant between integral schemes of the same dimension, so its fibre over the generic point of \(T\) has dimension \(0\) (Theorem 4.1 of [Dimension of fibres](course:AG-MO/dimension-of-fibres#4-dominant-families-of-varieties)), and \(k(W)\) is a finitely generated extension of \(k(T)\) of transcendence degree \(0\), hence finite of some degree \(e\). The quasi-finite locus of \(g\) is open (Theorem 3.1 of [Zariski's Main Theorem](course:AG-MO/zariskis-main-theorem#3-from-local-equalities-to-finite-affine-completions)) and contains the generic fibre; its complement \(Z\) is closed, and \(g(Z)\) is closed in \(T\) and misses the generic point. Over the dense open \(U=T\setminus g(Z)\) the morphism \(g\) is proper and quasi-finite, hence finite (Theorem 5.1 there). Finite morphisms are affine, so \(R^qg_*\mathcal O_W\) vanishes on \(U\) for \(q\ge1\); these sheaves have dimension less than \(d\) and contribute nothing. Finally \(g_*\mathcal O_W\) has generic stalk \(k(W)\), of length \(e\) over \(k(T)\), and Proposition 2.3(4) gives \(e\,(L_1\cdots L_d\cdot T)\). \(\square\)

**Corollary 3.2** (normalization of a curve). Let \(C\) be an integral curve, \(\nu:\widetilde C\to C\) its normalization, and \(L\) invertible. Then \(\deg(L|_C)=\deg(\nu^*L)\).

**Proof.** The normalization is finite and birational, so Proposition 3.1 applies with \(e=1\). \(\square\)

On a normal integral proper curve \(\widetilde C\), the local rings at closed points are discrete valuation rings. For a nonzero rational function \(\varphi\) on \(\widetilde C\), the divisor of zeros \(D_0\) and the divisor of poles \(D_\infty\) are effective Cartier divisors, with \(\operatorname{div}\varphi=D_0-D_\infty\). Corollary 2.5 applied to two sections of one line bundle gives the following classical fact.

**Corollary 3.3.** A nonzero rational function on a normal integral proper curve over \(k\) has as many zeros as poles, counted with multiplicities \(\dim_k\mathcal O_P/(\varphi)\) at each zero (and similarly for \(1/\varphi\) at each pole). In particular a nonconstant rational function has at least one zero and one pole.

**Proof.** Let \(L=\mathcal O(D_0)\). Its canonical section \(s_0\) has zero scheme \(D_0\); the section \(\varphi^{-1}s_0\) is regular, since \(\varphi^{-1}\) has poles exactly where \(\varphi\) has zeros, and its zero scheme is \(D_\infty\). Corollary 2.5 gives \(\deg L=\dim H^0(\mathcal O_{D_0})=\dim H^0(\mathcal O_{D_\infty})\). If \(\varphi\) has no pole, it is a regular function on a proper integral scheme, hence algebraic over \(k\), hence a constant of the finite extension \(H^0(\widetilde C,\mathcal O)\) of \(k\), and then it has no zero either. \(\square\)

**Theorem 3.4** (positivity). Let \(L\) be ample on \(X\) and \(Z\subseteq X\) a closed subscheme of dimension \(d\ge0\). Then \((L^d\cdot Z)>0\).

**Proof.** By Theorem 3.1 of the Euler-characteristic lesson, \(\chi(\mathcal O_Z\otimes L^n)\) has degree exactly \(d\) with positive leading coefficient \(c\). Its coefficient of \(n^d\) is \(c\), and expanding \(\chi(\mathcal O_Z\otimes L^{n_1+\dots+n_d})\), a polynomial in \(n_1+\dots+n_d\), its coefficient of \(n_1\cdots n_d\) is \(d!\,c\). \(\square\)

**Proposition 3.5** (hyperplane sections). Let \(k\) be infinite, \(H\) very ample on \(X\), \(V\subseteq X\) integral of dimension \(d\ge1\), and \(L_2,\dots,L_d\) invertible. For a general section \(s\in H^0(X,H)\), \(s|_V\ne0\), the zero scheme \(D=V\cap Z(s)\) has dimension \(d-1\), and

\[
(H\cdot L_2\cdots L_d\cdot V)=\sum_j m_j\,(L_2\cdots L_d\cdot D_j),
\]

where the \(D_j\) are the \((d-1)\)-dimensional components of \(D\) and \(m_j\ge1\) their multiplicities.

**Proof.** The sections vanishing identically on \(V\) form a proper subspace, since \(H\) restricted to \(V\) is very ample and \(V\ne\varnothing\); so a general \(s\) is nonzero on \(V\). Proposition 2.4 gives \((H\cdot L_2\cdots\cdot V)=(L_2\cdots\cdot D)\) and \(\dim D\le d-1\); Proposition 2.3(4) expands the right side. That \(D\) is nonempty of dimension exactly \(d-1\) follows from Theorem 3.4: \((H^d\cdot V)>0\) forces \((H^{d-1}\cdot D)\ne0\). \(\square\)

Iterating Proposition 3.5, \((H^{d-i}\cdot L_1\cdots L_i\cdot V)\) is a combination with positive integer coefficients of numbers \((L_1\cdots L_i\cdot W)\) over integral \(W\subseteq V\) of dimension \(i\). In particular, for \(i=1\), \((H^{d-1}\cdot L\cdot V)=\sum_jm_j\deg(L|_{C_j})\) for integral curves \(C_j\subseteq V\) and integers \(m_j\ge1\).

## 4. Examples

On \(\mathbf P^n_k\), \(\chi(\mathcal O(m))=\binom{m+n}n\) for all integers \(m\), so \(\chi(\mathcal O(m_1+\dots+m_n))\) has coefficient \(1\) at \(m_1\cdots m_n\): \((\mathcal O(1)^n\cdot\mathbf P^n)=1\). By multilinearity \((\mathcal O(a_1)\cdots\mathcal O(a_n)\cdot\mathbf P^n)=a_1\cdots a_n\). Let \(f_1,\dots,f_n\) be forms of degrees \(a_1,\dots,a_n\) such that each \(f_{i}\) is a nonzerodivisor on the coordinate ring of \(Z(f_1)\cap\dots\cap Z(f_{i-1})\). Then Proposition 2.4, applied \(n\) times, identifies \(a_1\cdots a_n\) with \(\chi\) of the finite scheme \(Z(f_1)\cap\dots\cap Z(f_n)\), that is, with its total length over \(k\). This is Bézout's theorem for hypersurfaces in general position; an inequality for isolated points of arbitrary intersections is proved in [Bézout's inequality for isolated zeros](bezouts-inequality-for-isolated-zeros.md).

On \(\mathbf P^1\times\mathbf P^1\) with \(A=\mathcal O(1,0)\) and \(B=\mathcal O(0,1)\), Künneth gives \(\chi(\mathcal O(a,b))=(a+1)(b+1)\), so \((A^2)=(B^2)=0\) and \((A\cdot B)=1\). The bundle \(A\) is nonnegative on every curve but not ample: its square is zero.

## 5. Exercises

**Exercise 5.1.** Compute \((L^2\cdot X)\) for \(X=\mathbf P^1\times\mathbf P^1\) and \(L=\mathcal O(a,b)\), and determine for which \((a,b)\) the bundle \(L\) has positive degree on every integral curve.

**Exercise 5.2.** Let \(C\subset\mathbf P^2\) be an integral curve of degree \(e\), that is, the zero scheme of an irreducible form of degree \(e\). Show that \((\mathcal O(1)\cdot C)=e\).

**Exercise 5.3.** Show that \((L_1\cdots L_d\cdot F)\) depends only on the isomorphism classes of the \(L_i\), and that \((L^{-1}\cdot L_2\cdots\cdot F)=-(L\cdot L_2\cdots\cdot F)\).

**Exercise 5.4.** Let \(f:Y\to X\) be the blow-up of \(\mathbf P^2\) at a point, \(E\) the exceptional curve and \(H\) the pullback of \(\mathcal O(1)\). Assuming that \(\mathcal O_Y(E)|_E\cong\mathcal O_{\mathbf P^1}(-1)\), compute \((H^2)\), \((H\cdot E)\), \((E^2)\) using Propositions 2.4 and 3.1.

**Exercise 5.5.** Show that if \(L\) is ample, then \(\deg(L|_C)>0\) for every integral curve \(C\subseteq X\). Show that on \(\mathbf P^1\times\mathbf P^1\) the converse holds for the bundles \(\mathcal O(a,b)\).

## 6. Solutions

**5.1.** By multilinearity \((L^2)=a^2(A^2)+2ab(A\cdot B)+b^2(B^2)=2ab\). The curves \(\mathbf P^1\times\{p\}\) and \(\{p\}\times\mathbf P^1\) have \((A\cdot\mathbf P^1\times p)=0\), \((B\cdot\mathbf P^1\times p)=1\), so \(L\) has degrees \(b\) and \(a\) on them; positivity on all curves needs \(a,b>0\). Conversely for \(a,b>0\) the bundle is very ample (Segre embedding composed with Veronese), so it is positive on every curve by Theorem 3.4.

**5.2.** Apply Proposition 2.4 to \(V=\mathbf P^2\) twice. With the defining form of \(C\), a section of \(\mathcal O(e)\), it gives \((\mathcal O(e)\cdot\mathcal O(1)\cdot\mathbf P^2)=(\mathcal O(1)\cdot C)\). With a linear form, whose zero scheme is a line \(\ell\cong\mathbf P^1\), it gives \((\mathcal O(1)\cdot\mathcal O(e)\cdot\mathbf P^2)=(\mathcal O(e)\cdot\ell)=e\). Alternatively, \(\chi(\mathcal O_C(n))=en-e(e-3)/2\) from the Euler-characteristic lesson, with \(n\)-coefficient \(e\).

**5.3.** Isomorphic sheaves have equal Euler characteristics. For the second claim use multilinearity with \(L\otimes L^{-1}\cong\mathcal O\), and \((\mathcal O\cdot L_2\cdots\cdot F)=0\) since the polynomial does not depend on the corresponding variable.

**5.4.** \((H^2)=(\mathcal O(1)^2\cdot\mathbf P^2)=1\) by Proposition 3.1 with \(e=1\). \((H\cdot E)=0\) since \(f(E)\) is a point. For \((E^2)=(\mathcal O_Y(E)\cdot\mathcal O_Y(E)\cdot Y)\), apply Proposition 2.4 to the canonical section of \(\mathcal O_Y(E)\), whose zero scheme is \(E\): \((E^2)=(\mathcal O_Y(E)\cdot E)=\deg(\mathcal O_Y(E)|_E)=-1\).

**5.5.** The first claim is Theorem 3.4 for \(d=1\). For \(\mathcal O(a,b)\), positivity on the two rulings means \(a,b>0\), which makes the bundle very ample (Exercise 5.1).

## References

- [Vakil] R. Vakil, The Rising Sea: Foundations of Algebraic Geometry, public draft of 21 October 2025. https://math.stanford.edu/~vakil/216blog/
- [Stacks] The Stacks project authors, The Stacks project, chapter Varieties, section Numerical intersections. https://stacks.math.columbia.edu/tag/0BEL
- [AI-Stacks] AI Integrated Stacks Project, varieties chapter, section Numerical intersections. https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-section-num
