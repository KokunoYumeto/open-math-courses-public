# The restricted tilting theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem 5.2 of Lesson 1: for every embedding \(\iota\colon E_r=(\mathbb Z/p)^r\to U(k)\) and every finite-dimensional \(kE_r\)-module \(D\), the module \(R_\iota(\operatorname{St}_{r-1})\otimes D\) is the restriction of a tilting \(\mathrm{SL}_2\)-module. Lesson 3 produced an equivariant vector bundle \(\mathcal M\) on the plane whose fibre at \(e_1=(1,0)\) restricts to \(D\) and whose fibre at the origin has small highest weights. After tensoring with \(\operatorname{St}_{r-1}\) the origin fibre becomes tilting. The key step is Lemma 3.1: for an equivariant bundle whose origin fibre \(T\) is tilting, the fibre at \(e_1\) is \(T\) restricted to \(U\). Extensions between tilting modules vanish, so the bundle can be trivialized equivariantly on every infinitesimal neighbourhood of the origin; the comparison with \(e_1\) then uses the line through \(e_1\), which \(U\) fixes pointwise, and a torus element defined over the field of Laurent series.

**Prerequisites.** [*Rational representations of SL₂ and tilting modules*](rational-representations-of-sl2-and-tilting-modules.md), Sections 3 to 5, and [*Lifting representations of elementary abelian groups to the plane*](lifting-representations-of-elementary-abelian-groups-to-the-plane.md). Completions of local rings and Nakayama's lemma.

## 1. Graded pieces at the origin

We keep the notation of Lessons 2 and 3: \(G=\mathrm{SL}_2\), \(U=\{u(t)\}\), \(V=k^2\), and \(\mathbb A^2=\operatorname{Spec}A\) with \(A=k[x,y]\). The group \(G\) acts on \(A\) by \((g\cdot f)(v)=f(g^{-1}v)\), so the linear forms span a copy of \(V^*\), the homogeneous polynomials of degree \(j\) form \(\operatorname{Sym}^j(V^*)=\nabla(j)\), and the maximal ideal \(\mathfrak m=(x,y)\) of the origin is \(G\)-stable.

Let \(\mathcal N\) be a \(G\)-equivariant vector bundle on \(\mathbb A^2\) of rank \(n\), with module of global sections \(N=\Gamma(\mathbb A^2,\mathcal N)\), a finitely generated projective \(A\)-module on which \(G\) acts compatibly with its action on \(A\). Its fibre at the origin is \(T=N/\mathfrak mN\), a rational \(G\)-module. The quotients \(N/\mathfrak m^jN\) are finite-dimensional rational \(G\)-modules.

**Lemma 1.1.** For every \(j\ge0\) multiplication induces an isomorphism of \(G\)-modules
\[
\operatorname{Sym}^j(V^*)\otimes_kT\xrightarrow{\ \sim\ }\mathfrak m^jN/\mathfrak m^{j+1}N .
\]

*Proof.* The map \((\mathfrak m^j/\mathfrak m^{j+1})\otimes_k(N/\mathfrak mN)\to\mathfrak m^jN/\mathfrak m^{j+1}N\), \(\bar f\otimes\bar m\mapsto\overline{fm}\), is well defined and \(G\)-equivariant. Both sides only depend on the localization of \(N\) at \(\mathfrak m\), which is free of rank \(n\); for a free module \(A_{\mathfrak m}^n\) the map is the identity of \((\mathfrak m^j/\mathfrak m^{j+1})^n\). \(\square\)

## 2. Equivariant trivialization at every finite order

**Lemma 2.1.** Suppose \(T\) is a tilting \(G\)-module. There are \(G\)-equivariant isomorphisms of \(A/\mathfrak m^j\)-modules
\[
\Psi_j\colon(A/\mathfrak m^j)\otimes_kT\xrightarrow{\sim}N/\mathfrak m^jN\quad(j\ge1),
\]
compatible with the reductions from \(j+1\) to \(j\), with \(\Psi_1\) the identity of \(T\). Here \(G\) acts diagonally on \((A/\mathfrak m^j)\otimes T\).

*Proof.* By Lemma 1.1 there are exact sequences of \(G\)-modules
\[
\begin{gathered}
0\to\operatorname{Sym}^j(V^*)\otimes T\to N/\mathfrak m^{j+1}N\\
\to N/\mathfrak m^jN\to0 .
\end{gathered}
\]
The module \(\operatorname{Sym}^j(V^*)\otimes T=\nabla(j)\otimes T\) has a good filtration by Proposition 3.5 of Lesson 2, and \(T\) has a Weyl filtration, so
\[
\operatorname{Ext}^1_G\bigl(T,\operatorname{Sym}^j(V^*)\otimes T\bigr)=0
\]
by Lemma 3.2 of Lesson 2. Start with the identity \(s_1\colon T\to N/\mathfrak mN\). Given a \(G\)-map \(s_j\colon T\to N/\mathfrak m^jN\), the pullback of the sequence along \(s_j\) is an extension of \(T\) by \(\operatorname{Sym}^j(V^*)\otimes T\), hence split; a splitting is a \(G\)-map \(s_{j+1}\colon T\to N/\mathfrak m^{j+1}N\) lifting \(s_j\). Put \(\Psi_j(a\otimes\tau)=a\,s_j(\tau)\). It is \(A\)-linear and \(G\)-equivariant, and the \(\Psi_j\) are compatible. Both sides are free \(A/\mathfrak m^j\)-modules of rank \(n\), the right side because \(N\) is locally free, and \(\Psi_j\) reduces modulo \(\mathfrak m\) to the identity of \(T\). By Nakayama's lemma \(\Psi_j\) is surjective, and a surjection between free modules of the same finite rank over \(A/\mathfrak m^j\) is an isomorphism, since both have the same finite dimension over \(k\). \(\square\)

## 3. Comparison with the fibre at the first basis vector

**Lemma 3.1** (comparison with a tilting origin fibre [OpenAI-208, Lemma 3.4]). Let \(\mathcal N\) be a \(G\)-equivariant vector bundle on \(\mathbb A^2\) whose fibre \(T=\mathcal N_0\) at the origin is a tilting \(G\)-module. Then the fibre \(\mathcal N_{e_1}\), with the action of the stabilizer \(U\) of \(e_1\), is isomorphic to the restriction of \(T\) to \(U\).

*Proof.* *Step 1: the \(U\)-fixed line.* The element \(u(t)\) acts on functions by \((u(t)\cdot f)(x,y)=f(x-ty,y)\). So \(U\) preserves the ideal \((y)\) and acts trivially on \(A/(y)=k[x]\): the line \(\ell=\{y=0\}\) is fixed by \(U\) scheme-theoretically. Reducing the isomorphisms \(\Psi_j\) of Lemma 2.1 modulo \(y\) gives compatible \(U\)-equivariant isomorphisms
\[
k[x]/(x^j)\otimes_kT\xrightarrow{\ \sim\ }N/(x^j,y)N ,
\]
where \(U\) acts on the left through \(T\) alone.

*Step 2: matrices.* The \(k[x]\)-module \(N/yN=\Gamma(\ell,\mathcal N|_\ell)\) is finitely generated and projective, hence free because \(k[x]\) is a principal ideal domain. In a basis, the action of \(U\) on it is a matrix \(C(x,t)\in\mathrm{GL}_n(k[x,t])\), and in a basis of \(T\) the action of \(U\) on \(T\) is a matrix \(B(t)\in\mathrm{GL}_n(k[t])\). The compatible isomorphisms of Step 1 form a matrix \(\Phi(x)\in\mathrm{GL}_n(k[[x]])\) with
\[
\begin{gathered}
C(x,t)\,\Phi(x)\equiv\Phi(x)\,B(t)\pmod{x^j}\\
\text{for all }j .
\end{gathered}
\]
The degrees in \(t\) of \(C\) and \(B\) are bounded, so comparing the coefficients of each power of \(t\) gives \(C(x,t)\Phi(x)=\Phi(x)B(t)\) in the ring \(k[[x]][t]\) of matrices. Let \(K=k((x))\). The matrix \(C(x,t)\), viewed over \(K\), is the action of \(U_K\) on the fibre \(\mathcal N_{xe_1}\) of \(\mathcal N\) at the \(K\)-point \(xe_1=(x,0)\) of \(\ell\). So \(\Phi\) defines an isomorphism of rational \(U_K\)-modules
\[
\varphi\colon T_K\xrightarrow{\ \sim\ }\mathcal N_{xe_1},\qquad T_K=T\otimes_kK .
\]

*Step 3: a torus element over \(K\).* The fibre \(\mathcal N_{xe_1}\) lies over the point \(xe_1\), not over \(e_1\). Put \(h=\operatorname{diag}(x,x^{-1})\in G(K)\); then \(he_1=xe_1\) and
\[
h\,u(t)\,h^{-1}=u(x^2t).
\]
Let \(b_h\colon\mathcal N_{e_1}\otimes_kK\to\mathcal N_{xe_1}\) be the action of \(h\) on fibres, and write \(\rho_{e_1},\rho_x,\rho_T\) for the actions of \(U\) on \(\mathcal N_{e_1}\), on \(\mathcal N_{xe_1}\) and on \(T\). Equivariance of the bundle and of \(T\) gives
\[
\begin{aligned}
b_h\,\rho_{e_1}(u(t))&=\rho_x(u(x^2t))\,b_h,\\
\rho_T(h)\,\rho_T(u(t))&=\rho_T(u(x^2t))\,\rho_T(h).
\end{aligned}
\]
Put \(f=b_h^{-1}\circ\varphi\circ\rho_T(h)\colon T_K\to\mathcal N_{e_1}\otimes K\). Using that \(\varphi\) intertwines \(\rho_T\) and \(\rho_x\),
\[
\begin{aligned}
f\,\rho_T(u(t))&=b_h^{-1}\varphi\,\rho_T(u(x^2t))\,\rho_T(h)\\
&=b_h^{-1}\rho_x(u(x^2t))\,\varphi\,\rho_T(h)\\
&=\rho_{e_1}(u(t))\,f .
\end{aligned}
\]
So \(f\) is an isomorphism of \(U_K\)-modules \(T_K\to\mathcal N_{e_1}\otimes K\) for the original actions.

*Step 4: descent to \(k\).* In bases over \(k\), the space \(L=\operatorname{Hom}_U(T,\mathcal N_{e_1})\) is the set of matrices \(F\) with \(\rho_{e_1}(u(t))F=F\rho_T(u(t))\), a system of linear equations over \(k\), one for each power of \(t\) and each entry. Its solutions over \(K\) are \(L\otimes_kK\), and \(f\) is one of them. The determinant is a polynomial function on \(L\) that does not vanish at \(f\), so it is not the zero polynomial. Since \(k\) is infinite, it does not vanish at some \(F\in L\), and \(F\) is an isomorphism of \(U\)-modules \(T\to\mathcal N_{e_1}\). \(\square\)

The formal trivialization of Lemma 2.1 is not claimed to come from a trivialization of \(\mathcal N\) on the plane.

## 4. Proof of the restricted tilting theorem

**Theorem 4.1** (Theorem 5.2 of Lesson 1). Let \(r\ge1\), \(\iota\colon E_r\to U(k)\) injective, and \(D\) a finite-dimensional \(kE_r\)-module. There is a tilting \(G\)-module \(T\) with \(R_\iota(\operatorname{St}_{r-1})\otimes D\cong R_\iota(T)\).

*Proof.* Proposition 4.2 of Lesson 3 gives a \(G\)-equivariant vector bundle \(\mathcal M\) on \(\mathbb A^2\) whose fibre at \(e_1\) restricts along \(\iota\) to \(D\), and whose origin fibre \(\mathcal M_0\) has all composition factors \(L(h)\) with \(h<p^r\). Let \(\mathcal N=\operatorname{St}_{r-1}\otimes_k\mathcal M\), the tensor product with the constant bundle with fibre \(\operatorname{St}_{r-1}\), with the diagonal action. Its origin fibre \(T=\operatorname{St}_{r-1}\otimes\mathcal M_0\) is tilting by Lemma 5.1 of Lesson 2 with \(m=r-1\). By Lemma 3.1, \(\mathcal N_{e_1}=\operatorname{St}_{r-1}\otimes\mathcal M_{e_1}\) is isomorphic to \(T\) as a \(U\)-module. Restricting along \(\iota\) gives \(R_\iota(\operatorname{St}_{r-1})\otimes D\cong R_\iota(T)\). For \(r=1\) the Steinberg factor is \(\operatorname{St}_0=k\). \(\square\)

Coulembier and Flake proved this statement for rank one, for \(p=r=2\), and, for every rank, for modules of Loewy length at most two and Carlson modules and the subcategory they generate [CFS, Theorems 2 and 3]; the vector bundle argument treats every module \(D\) at once.

## 5. Exercises

**5.1.** Let \(r=1\) and let \(\iota\) send a generator of \(\mathbb Z/p\) to \(u(1)\). Show directly that \(R_\iota(L(i-1))\) is the Jordan block representation \(J_i\) for \(1\le i\le p\), and deduce the case \(r=1\) of Theorem 4.1 without Lemma 3.1.

**5.2.** Compute \(h\,u(t)\,h^{-1}\) for \(h=\operatorname{diag}(x,x^{-1})\), and derive from it the two identities displayed in Step 3 of the proof of Lemma 3.1.

**5.3.** Let \(L\) be a finite-dimensional space of linear maps \(T\to W\) between vector spaces of the same dimension over an infinite field \(k\), and let \(K\supset k\) be a field. Show that if some element of \(L\otimes_kK\) is invertible, then some element of \(L\) is invertible. Show that this fails over \(\mathbb F_2\): let \(L\) be the \(\mathbb F_2\)-span of \(\operatorname{diag}(1,0,1)\) and \(\operatorname{diag}(0,1,1)\), and \(K=\mathbb F_2((x))\).

**5.4.** In Step 2, explain why the identity \(C\Phi=\Phi B\) in \(k[[x]][t]\) follows from the congruences modulo \(x^j\).

## 6. Solutions

**5.1.** By Lemma 4.1 of Lesson 2, \(L(i-1)=\operatorname{Sym}^{i-1}(V)\) for \(i\le p\). On it \(u(1)\) sends \(e_1^ae_2^{b}\) to \(e_1^a(e_2+e_1)^b\), so \(u(1)-1\) lowers the power of \(e_2\) and maps \(e_1^{a}e_2^{b}\) to \(b\,e_1^{a+1}e_2^{b-1}\) plus terms with smaller powers of \(e_2\). The coefficients \(b\le i-1<p\) are nonzero in \(k\), so \((u(1)-1)^{i-1}e_2^{i-1}=(i-1)!\,e_1^{i-1}\ne0\), and \(u(1)\) is a single unipotent Jordan block of size \(i\): \(R_\iota(L(i-1))\cong J_i\). Every representation of \(\mathbb Z/p\) is a direct sum of modules \(J_i\) with \(i\le p\), and \(L(i-1)=T(i-1)\) is tilting by Lemma 4.1 of Lesson 2. With \(\operatorname{St}_0=k\), this is Theorem 4.1 for \(r=1\).

**5.2.** \(\operatorname{diag}(x,x^{-1})\bigl(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\bigr)\operatorname{diag}(x^{-1},x)=\bigl(\begin{smallmatrix}1&x^2t\\0&1\end{smallmatrix}\bigr)\). For \(m\in\mathcal N_{e_1}\otimes K\), equivariance of the bundle gives \(u(x^2t)\cdot(h\cdot m)\)\(=h\cdot(h^{-1}u(x^2t)h)\cdot m\)\(=h\cdot u(t)\cdot m\), which is the first identity; the second is the same computation in \(T\).

**5.3.** Choose a basis \(F_1,\dots,F_d\) of \(L\). The function \(\det(\sum_ic_iF_i)\) is a polynomial in \(c_1,\dots,c_d\) with coefficients in \(k\). An invertible element \(\sum_ic_iF_i\) with \(c_i\in K\) shows that this polynomial is not zero, and a nonzero polynomial over an infinite field has a nonzero value at a point with coordinates in \(k\). Over \(\mathbb F_2\), the four elements of the given \(L\) are \(0\), \(\operatorname{diag}(1,0,1)\), \(\operatorname{diag}(0,1,1)\) and \(\operatorname{diag}(1,1,0)\), all singular: the determinant polynomial \(c_1c_2(c_1+c_2)\) vanishes at every point of \(\mathbb F_2^2\). Over \(K\) the element \(\operatorname{diag}(1,0,1)+x\operatorname{diag}(0,1,1)\)\(=\operatorname{diag}(1,x,1+x)\) has determinant \(x(1+x)\ne0\).

**5.4.** Write \(C\Phi-\Phi B=\sum_lQ_l(x)t^l\) with \(Q_l\in M_n(k[[x]])\), a finite sum because \(C\) and \(B\) have bounded degree in \(t\). The congruence modulo \(x^j\) says that every \(Q_l\) lies in \(x^jM_n(k[[x]])\). This holds for all \(j\), and \(\bigcap_jx^jk[[x]]=0\), so every \(Q_l=0\).

## Sources

- [OpenAI-208] OpenAI, *Fiber functors for finite symmetric tensor categories in positive characteristic*, OpenAI Math Release preprint, 24 September 2026, Section 3.3 (Lemma 3.4 and the proof of Theorem 3.1). https://github.com/openai/math/tree/main/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026
- [CF] K. Coulembier and J. Flake, *Towards higher Frobenius functors for symmetric tensor categories*, Selecta Math. 32 (2026), numbering of arXiv:2405.19506v2: Conjecture 5.4.2 and Remark 5.4.4. https://arxiv.org/abs/2405.19506v2
- [CFS] K. Coulembier and J. Flake, *A conjecture on the tensor ideal for an elementary p-group generated by the restriction of a Steinberg module*, arXiv:2507.02722v1, Theorems 2 and 3. https://arxiv.org/abs/2507.02722v1
