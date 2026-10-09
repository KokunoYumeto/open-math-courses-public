# Bézout's inequality for isolated zeros

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(g_1,\dots,g_n\) be polynomials in \(n\) variables of degrees at most \(d_1,\dots,d_n\). Their common zero set may have positive-dimensional components, but each isolated zero \(P\) carries a finite multiplicity \(\mu_P\), the dimension of the local algebra \(\mathcal O_P/(g_1,\dots,g_n)\). Bézout's inequality says that the multiplicities of all isolated zeros add up to at most \(d_1\cdots d_n\). This lesson proves it by deforming the system into one with exactly \(d_1\cdots d_n\) solutions: the local algebra at an isolated zero becomes, after completion, a free module of rank \(\mu_P\) over the power series ring in the deformation parameter, and these free modules embed into the generic fibre of the deformation. A weighted version, for polynomials of bounded weighted degree, follows by a substitution. The weighted version is an input to the zero estimates in the course on the irrationality exponent of \(\pi\).

We use from commutative algebra: the Nullstellensatz; completion of Noetherian local rings and its exactness on finite modules, Theorems 3.1 and 4.1 of [Completion](course:AG-CA/completion#3-noetherian-exactness-tensoring-and-flatness); that one element cuts the dimension of a Noetherian local ring by at most one, Theorem 3.2 of [Dimension theory of Noetherian local rings](course:AG-CA/dimension-theory-of-noetherian-local-rings#3-how-much-can-one-equation-cut); and from [Regular sequences, depth and Cohen–Macaulay modules](course:AG-CA/regular-sequences-depth-and-cohen-macaulay-modules#4-when-dimension-detects-regularity): regular local rings are Cohen–Macaulay (Theorem 6.1), in a Cohen–Macaulay local ring a sequence that cuts the dimension by its length is regular (Theorem 4.2) and its quotient is Cohen–Macaulay (Corollary 6.2), and every system of parameters of a Cohen–Macaulay module is a regular sequence (Corollary 4.3).

Throughout, \(k\) is an algebraically closed field. For a point \(P\in k^n\), \(\mathcal O_P\) is the local ring of \(k[x_1,\dots,x_n]\) at the maximal ideal \(\mathfrak m_P\) of \(P\).

**Definition.** A point \(P\) of the zero set \(V(g_1,\dots,g_n)\subseteq k^n\) is *isolated* if \(\{P\}\) is an irreducible component of it, equivalently if \((g_1,\dots,g_n)\mathcal O_P\) is \(\mathfrak m_P\)-primary. Its *multiplicity* is \(\mu_P=\dim_k\mathcal O_P/(g_1,\dots,g_n)\), which is finite exactly for isolated points.

## 1. Systems without zeros at infinity

For a polynomial \(f\) of degree \(d\), its *leading form* is its homogeneous part of degree \(d\).

**Lemma 1.1** (Koszul relations). Let \(\varphi_1,\dots,\varphi_n\) be a regular sequence in a commutative ring \(R\). If \(\sum_ic_i\varphi_i=0\), there are \(b_{ij}=-b_{ji}\) in \(R\) with \(c_i=\sum_jb_{ij}\varphi_j\) for all \(i\). If \(R\) is graded, the \(\varphi_i\) are homogeneous and the relation is homogeneous, the \(b_{ij}\) can be taken homogeneous.

**Proof.** Induction on \(n\). For \(n=1\), \(c_1\varphi_1=0\) forces \(c_1=0\). In general \(c_n\varphi_n\in(\varphi_1,\dots,\varphi_{n-1})\), and \(\varphi_n\) is a nonzerodivisor modulo that ideal, so \(c_n=\sum_{j<n}e_j\varphi_j\). Then \(\sum_{i<n}(c_i+e_i\varphi_n)\varphi_i=0\), and induction gives antisymmetric \(b'_{ij}\) (\(i,j<n\)) with \(c_i+e_i\varphi_n=\sum_{j<n}b'_{ij}\varphi_j\). Put \(b_{ij}=b'_{ij}\) for \(i,j<n\), \(b_{in}=-e_i\), \(b_{ni}=e_i\), \(b_{nn}=0\). In the graded case take homogeneous components of the appropriate degrees throughout. \(\square\)

**Theorem 1.2** (Macaulay). Let \(F\) be a field and \(f_1,\dots,f_n\in F[x_1,\dots,x_n]\) of degrees \(d_1,\dots,d_n\ge1\), with leading forms \(\varphi_1,\dots,\varphi_n\). If the \(\varphi_i\) have no common zero other than \(0\) over an algebraic closure of \(F\), then

\[
\dim_FF[x_1,\dots,x_n]/(f_1,\dots,f_n)=d_1\cdots d_n .
\]

**Proof.** Write \(R=F[x_1,\dots,x_n]\), graded by degree, with irrelevant ideal \(\mathfrak m=(x_1,\dots,x_n)\).

*The leading forms are a regular sequence.* Over the algebraic closure, the Nullstellensatz gives \(x_i^N\in(\varphi_1,\dots,\varphi_n)\) for some \(N\). The condition that \(x_i^N\) is a combination of the \(\varphi_j\) with polynomial coefficients of bounded degree is a linear system with coefficients in \(F\); being solvable over the closure, it is solvable over \(F\). So \(R/(\varphi)\) has finite length. In the local ring \(R_{\mathfrak m}\), regular of dimension \(n\), the \(n\) elements \(\varphi_i\) generate an \(\mathfrak m\)-primary ideal, so they form a system of parameters, hence a regular sequence. They also form a regular sequence in \(R\). Indeed, if some \(\varphi_i\) were a zero divisor on the graded module \(M=R/(\varphi_1,\dots,\varphi_{i-1})\), it would annihilate a nonzero homogeneous \(u\in M\). The annihilator of \(u\) is a proper homogeneous ideal, hence contained in \(\mathfrak m\), so \(u\) stays nonzero in \(M_{\mathfrak m}\), and \(\varphi_i\) would be a zero divisor there.

*Hilbert series.* For a graded module \(M\) with finite-dimensional pieces and a homogeneous nonzerodivisor \(\varphi\) of degree \(e\), the sequence \(0\to M(-e)\xrightarrow\varphi M\to M/\varphi M\to0\) gives \(H_{M/\varphi M}(t)=(1-t^e)H_M(t)\) for the Hilbert series \(H_M(t)=\sum_j\dim M_j\,t^j\). Starting from \(H_R=(1-t)^{-n}\),

\[
H_{R/(\varphi)}(t)=\prod_{i=1}^n\frac{1-t^{d_i}}{1-t}=\prod_{i=1}^n(1+t+\dots+t^{d_i-1}),
\]

so \(\dim_FR/(\varphi)=H_{R/(\varphi)}(1)=d_1\cdots d_n\).

*Leading forms of the ideal.* Let \(I=(f_1,\dots,f_n)\). We claim that the leading form of every nonzero \(h\in I\) lies in \((\varphi)\). Write \(h=\sum_ia_if_i\) with \(\delta=\max_i(\deg a_i+d_i)\) as small as possible. If \(\delta=\deg h\), the leading form of \(h\) is \(\sum_i\bar a_i\varphi_i\), where \(\bar a_i\) is the homogeneous part of \(a_i\) of degree \(\delta-d_i\). If \(\delta>\deg h\), then \(\sum_i\bar a_i\varphi_i=0\), and Lemma 1.1 gives homogeneous antisymmetric \(b_{ij}\) of degree \(\delta-d_i-d_j\) with \(\bar a_i=\sum_jb_{ij}\varphi_j\). Then \(a_i'=a_i-\sum_jb_{ij}f_j\) satisfies \(\sum_ia_i'f_i=h-\sum_{i,j}b_{ij}f_jf_i=h\), and \(\deg a_i'<\delta-d_i\), since the part of degree \(\delta-d_i\) cancels. This contradicts the minimality of \(\delta\).

*Comparison of dimensions.* Let \(R_{\le N}\) be the polynomials of degree at most \(N\). By the claim, the leading forms of elements of \(I\cap R_{\le N}\) of degree exactly \(j\) form the space \((\varphi)_j\), so \(\dim(I\cap R_{\le N})=\sum_{j\le N}\dim(\varphi)_j\), and the image of \(R_{\le N}\) in \(R/I\) has dimension \(\sum_{j\le N}\dim(R/(\varphi))_j\). As \(N\to\infty\) these images exhaust \(R/I\), and the dimensions increase to \(d_1\cdots d_n\). \(\square\)

**Lemma 1.3** (a deformation with no zeros at infinity). Let \(g_1,\dots,g_n\in k[x_1,\dots,x_n]\) with \(\deg g_i\le d_i\), \(d_i\ge1\), and put

\[
G_i=(1-t)\,g_i+t\,(x_i^{d_i}-1)\in k[t][x_1,\dots,x_n].
\]

Over the field \(K=k(t)\), each \(G_i\) has degree exactly \(d_i\), and

\[
\dim_KK[x_1,\dots,x_n]/(G_1,\dots,G_n)=d_1\cdots d_n .
\]

**Proof.** The coefficient of \(x_i^{d_i}\) in \(G_i\) is \(t\) plus \((1-t)\) times a constant, a nonzero element of \(K\); so \(\deg G_i=d_i\), with leading form \(\varphi_i=(1-t)g_i^{[d_i]}+t\,x_i^{d_i}\), where \(g_i^{[d_i]}\) is the degree-\(d_i\) part of \(g_i\) (possibly zero). Put \(N_0=\sum_i(d_i-1)+1\) and consider the \(K\)-linear map

\[
\bigoplus_iK[x]_{N_0-d_i}\to K[x]_{N_0},\qquad(a_i)\mapsto\sum_ia_i\varphi_i ,
\]

between spaces of homogeneous polynomials. Its matrix in the monomial bases has entries in \(k[t]\). At \(t=1\) it becomes \((a_i)\mapsto\sum_ia_ix_i^{d_i}\), which is surjective: a monomial of degree \(N_0\) has some exponent \(e_i\ge d_i\). So some maximal minor is a polynomial in \(t\) that is nonzero at \(t=1\), hence nonzero in \(K\), and the map is surjective over \(K\). Thus \((\varphi_1,\dots,\varphi_n)\) contains every monomial of degree \(N_0\), and the \(\varphi_i\) have no common zero except \(0\) over \(\overline K\). Theorem 1.2 applies. \(\square\)

## 2. Isolated zeros as free modules

Keep \(g_i\), \(G_i\) as in Lemma 1.3, and put

\[
B=k[t,x_1,\dots,x_n]/(G_1,\dots,G_n).
\]

Since \(G_i(0,x)=g_i(x)\), the fibre of \(B\) over \(t=0\) is \(k[x]/(g)\).

**Proposition 2.1.** Let \(P\) be an isolated zero of \(g_1,\dots,g_n\), and let \(\widehat B_P\) be the completion of \(B\) at the maximal ideal of \((0,P)\). Then \(\widehat B_P\) is a free \(k[[t]]\)-module of rank \(\mu_P\). Moreover, if \(e_1,\dots,e_{\mu_P}\) are polynomials whose images form a basis of \(\mathcal O_P/(g)\), their images form a basis of \(\widehat B_P\) over \(k[[t]]\).

**Proof.** Write \(y=x-P\). The completion of \(k[t,x]\) at \((t,y)\) is \(k[[t,y]]\), and by exactness of completion \(\widehat B_P=k[[t,y]]/(G_1,\dots,G_n)\).

*The special fibre.* \(\widehat B_P/t\widehat B_P=k[[y]]/(g_1,\dots,g_n)\). The ideal \((g)\mathcal O_P\) is \(\mathfrak m_P\)-primary, so \(\mathcal O_P/(g)\) is Artinian and equal to its own completion; hence \(k[[y]]/(g)\cong\mathcal O_P/(g)\) has dimension \(\mu_P\).

*Dimension and depth.* The ring \(k[[t,y]]\) is regular local of dimension \(n+1\). Dividing by the \(n\) elements \(G_i\) lowers the dimension by at most \(n\), so \(\dim\widehat B_P\ge1\); dividing further by \(t\) gives an Artinian ring, so \(\dim\widehat B_P\le1\). Hence \(\dim\widehat B_P=1=(n+1)-n\), the \(G_i\) form a regular sequence in the Cohen–Macaulay ring \(k[[t,y]]\), and \(\widehat B_P\) is Cohen–Macaulay of dimension one. The element \(t\) is a system of parameters of \(\widehat B_P\), hence a nonzerodivisor.

*Finite generation.* Let \(b\in\widehat B_P\). Write \(b=\sum_ic_i^{(0)}e_i+tb_1\) with \(c_i^{(0)}\in k\), then \(b_1=\sum_ic_i^{(1)}e_i+tb_2\), and so on. For every \(L\),

\[
b-\sum_i\Bigl(\sum_{l<L}c_i^{(l)}t^l\Bigr)e_i=t^Lb_L .
\]

The right side lies in the \(L\)-th power of the maximal ideal, and \(\widehat B_P\) is complete and separated, so \(b=\sum_ic_ie_i\) with \(c_i=\sum_lc_i^{(l)}t^l\in k[[t]]\) (the action of \(k[[t]]\) on the complete ring is continuous). So the \(e_i\) generate \(\widehat B_P\) over \(k[[t]]\).

*Freeness.* A finitely generated torsion-free module over the discrete valuation ring \(k[[t]]\) is free; its rank equals \(\dim_k\widehat B_P/t\widehat B_P=\mu_P\), and \(\mu_P\) generators of a free module of rank \(\mu_P\) form a basis. \(\square\)

## 3. The inequality for isolated zeros

**Theorem 3.1** (Bézout's inequality). Let \(g_1,\dots,g_n\in k[x_1,\dots,x_n]\) with \(\deg g_i\le d_i\), \(d_i\ge1\). Then the isolated zeros \(P\) of \(g_1,\dots,g_n\) are finite in number, and

\[
\sum_{P\ \text{isolated}}\mu_P\le d_1\cdots d_n .
\]

**Proof.** Let \(P_1,\dots,P_s\) be distinct isolated zeros; we show \(\sum_j\mu_{P_j}\le d_1\cdots d_n\), which also bounds their number. Let \(B\), \(G_i\) be as above, \(A'=k[[t]]\otimes_{k[t]}B=k[[t]][x]/(G)\), and \(\widehat B_j=\widehat B_{P_j}\). Each completion map \(B\to\widehat B_j\) is a \(k[t]\)-algebra map into a \(k[[t]]\)-algebra, so it extends to \(A'\to\widehat B_j\). Consider

\[
\Psi:A'\to\prod_{j=1}^s\widehat B_j .
\]

*\(\Psi\) is surjective.* Choose \(N\) such that \(\mathfrak m_{P_j}^N\mathcal O_{P_j}\subseteq(g)\mathcal O_{P_j}\) for every \(j\) (the local algebras are Artinian). The ideals \(\mathfrak m_{P_j}^N\subset k[x]\) are pairwise comaximal, so the Chinese remainder theorem gives polynomials \(\pi_j\) with \(\pi_j\equiv1\) modulo \(\mathfrak m_{P_j}^N\) and \(\pi_j\equiv0\) modulo \(\mathfrak m_{P_l}^N\) for \(l\ne j\). For each \(j\) choose polynomials \(e_{j,1},\dots,e_{j,\mu_{P_j}}\) giving a basis of \(\mathcal O_{P_j}/(g)\). The images of the polynomials \(\pi_je_{j,i}\) in \(\prod_l\widehat B_l/t\widehat B_l=\prod_l\mathcal O_{P_l}/(g)\) are the basis vectors \(e_{j,i}\) in the factor \(j\) and \(0\) in the other factors. So the \(k[[t]]\)-submodule \(N'\) generated by their images satisfies \(N'+t\prod_l\widehat B_l=\prod_l\widehat B_l\), and the argument of Proposition 2.1 (finite generation) gives \(N'=\prod_l\widehat B_l\). As \(N'\) lies in the image of \(\Psi\), \(\Psi\) is surjective.

*Counting over the generic point.* Inverting \(t\), which is exact, \(\Psi\) induces a surjection

\[
k((t))[x]/(G_1,\dots,G_n)\longrightarrow\prod_j\widehat B_j[t^{-1}]\cong\prod_jk((t))^{\mu_{P_j}},
\]

by Proposition 2.1. The left side is \(K[x]/(G)\otimes_Kk((t))\) with \(K=k(t)\subset k((t))\), of dimension \(d_1\cdots d_n\) by Lemma 1.3. Hence \(\sum_j\mu_{P_j}\le d_1\cdots d_n\). \(\square\)

The proof shows a little more: if the system has no zeros at infinity, that is, if its leading forms have only the trivial common zero, then all zeros are isolated and Theorem 1.2 gives equality. In general, zeros escaping to infinity and positive-dimensional components only lower the left side.

**Corollary 3.2** (weighted Bézout inequality). Assume that \(k\) has characteristic zero. Give the variables positive rational weights \(\rho_1,\dots,\rho_n\), and let the weighted degree of \(x^\alpha\) be \(\sum_a\rho_a\alpha_a\). If \(g_1,\dots,g_n\) have weighted degree at most \(N>0\), then

\[
\sum_{P\ \text{isolated}}\mu_P\le\frac{N^n}{\rho_1\cdots\rho_n}.
\]

**Proof.** Choose a positive integer \(M_0\) with \(r_a=M_0\rho_a\in\mathbb Z\) for all \(a\), and constants \(\lambda_a\in k\) different from the \(a\)-th coordinates of the finitely many isolated zeros (possible since \(k\) is infinite). Consider the morphism \(\sigma:k^n\to k^n\), \(\sigma(z)_a=\lambda_a+z_a^{r_a}\), and the polynomials \(\tilde g_i=g_i\circ\sigma\). A monomial \(x^\alpha\) of weighted degree at most \(N\) becomes a polynomial of ordinary degree at most \(\sum_ar_a\alpha_a\le M_0N\), so \(\deg\tilde g_i\le M_0N\).

Let \(P\) be an isolated zero of the \(g_i\). For each \(a\), the equation \(z_a^{r_a}=P_a-\lambda_a\) with nonzero right side has exactly \(r_a\) distinct solutions in the algebraically closed field \(k\) of characteristic zero, and the derivative \(r_az_a^{r_a-1}\) does not vanish at them. So \(P\) has exactly \(\prod_ar_a\) preimages \(Q\), and at each of them the Jacobian of \(\sigma\) is invertible; hence \(\sigma\) induces an isomorphism of completed local rings \(k[[x-P]]\to k[[z-Q]]\), carrying the ideal \((g)\) to \((\tilde g)\). Each \(Q\) is therefore an isolated zero of the \(\tilde g_i\), with \(\mu_Q=\mu_P\), since both are the dimensions of the isomorphic Artinian quotients. Distinct \(P\) have disjoint sets of preimages. Theorem 3.1 for the \(\tilde g_i\) gives \(\bigl(\prod_ar_a\bigr)\sum_P\mu_P\le(M_0N)^n\), and \(\prod_ar_a=M_0^n\rho_1\cdots\rho_n\). \(\square\)

## 4. Exercises

**Exercise 4.1.** Compute \(\mu_0\) for \(g_1=y-x^2\), \(g_2=y\) in \(k[x,y]\), and compare with Theorem 3.1.

**Exercise 4.2.** Show that \(g_i=x_i^{d_i}-1\) has exactly \(d_1\cdots d_n\) zeros in \(k^n\) when the characteristic of \(k\) does not divide the \(d_i\), each of multiplicity one.

**Exercise 4.3.** Let \(g_1=x(y-1)\), \(g_2=x(x-1)\) in \(k[x,y]\). Find the zero set, its isolated points and their multiplicities, and compare with \(d_1d_2=4\).

**Exercise 4.4.** With weights \(\rho_x=1\), \(\rho_y=3\), let \(g_1=y-x^3\) and \(g_2=y\). Show that the origin has multiplicity \(3\) and that Corollary 3.2 with \(N=3\) is an equality.

**Exercise 4.5.** Show that the bound of Theorem 3.1 is attained by \(g_i=x_i^{d_i}\), which has a single zero, of multiplicity \(d_1\cdots d_n\).

## 5. Solutions

**4.1.** \(k[x,y]/(y-x^2,y)\cong k[x]/(x^2)\) has dimension \(2\), and the origin is the only zero. Theorem 3.1 gives \(2\le2\cdot1\).

**4.2.** The zeros are the tuples of \(d_i\)-th roots of unity, \(d_1\cdots d_n\) of them. The Jacobian matrix is diagonal with entries \(d_ix_i^{d_i-1}\ne0\) there, so each local algebra is \(k\) and \(\mu=1\).

**4.3.** \(V=\{x=0\}\cup\{(1,1)\}\). The line \(x=0\) is a positive-dimensional component; the only isolated point is \((1,1)\). There \(x\) is a unit, so the local algebra is \(\mathcal O/(y-1,x-1)=k\) and \(\mu=1\le4\).

**4.4.** \(k[x,y]/(y-x^3,y)\cong k[x]/(x^3)\) has dimension \(3\). Both polynomials have weighted degree \(3\), and \(N^2/(\rho_x\rho_y)=9/3=3\).

**4.5.** The only zero is the origin, and \(k[x]/(x_1^{d_1},\dots,x_n^{d_n})\) has the monomials \(x^\alpha\) with \(\alpha_i<d_i\) as a basis, \(d_1\cdots d_n\) of them. The local algebra at the origin is the same, since the quotient is already local.

## References

- [Mondal] P. Mondal, How many zeroes? Counting the number of solutions of systems of polynomials via geometry at infinity, arXiv:1806.05346 (book draft). https://arxiv.org/abs/1806.05346
- [Vakil] R. Vakil, The Rising Sea: Foundations of Algebraic Geometry, public draft of 21 October 2025. https://math.stanford.edu/~vakil/216blog/
