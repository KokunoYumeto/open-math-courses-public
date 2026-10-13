# A rank measure from differentiation and multiplication

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lower bound of this course compares two estimates of one number \(R(g)\), which is defined for a homogeneous polynomial \(g\). The variables are divided into two groups, \(V\) and \(U\). In \(g\), every variable of \(V\) is replaced by the partial derivative in that variable, and every variable of \(U\) by the multiplication with it. This turns \(g\) into a linear map between spaces of polynomials, and \(R(g)\) is its rank. This lesson defines the map, proves that the rank of a product of polynomials is small when the degrees of the factors do not fit a certain proportion, and fixes the numbers that the rest of the course uses.

- The operators \(T_Q\) and their product rule (Lemma 1.1).
- The map \(F_g\) and the measure \(R(g)\) (Section 2).
- The rank of a product, through intermediate spaces (Lemma 3.2).
- The numbers of the proof and their estimates (Lemma 4.1).
- The product bound \(R(Q_1\cdots Q_r)\le2D\prod_jH_{e_j}\) (Proposition 5.1).

The lesson follows [OpenAI-D, Sections 2 and 3.1]. It continues [Iterated matrix multiplication and depth-five circuits](iterated-matrix-multiplication-and-depth-five-circuits.md) and needs linear algebra and binomial coefficients.

## 1. Derivatives and multiplications

Let \(K\) be a field, and let \(V\) and \(U\) be two disjoint finite sets of variables, with \(v\ge1\) and \(u\ge1\) elements. Let \(K[V,U]\) be the ring of the polynomials in all these variables. For \(x\in V\) let \(\partial_x\) be the formal partial derivative in \(x\), and for \(y\in U\) let \(\mu_y\) be the multiplication by \(y\); both are linear maps from \(K[V,U]\) to itself.

All these maps commute with each other: two partial derivatives commute, two multiplications commute, and \(\partial_x(yf)=y\,\partial_xf\) because \(y\) is not the variable \(x\).

**Definition.** For a polynomial \(Q\in K[V,U]\), let \(T_Q\) be the linear map from \(K[V,U]\) to itself that is obtained from \(Q\) by writing \(\partial_x\) for every variable \(x\in V\) and \(\mu_y\) for every variable \(y\in U\). So for a monomial \(Q=\prod_xx^{\alpha_x}\prod_yy^{\gamma_y}\), \(T_Q\) is the composition of the maps \(\partial_x^{\alpha_x}\) and \(\mu_y^{\gamma_y}\), and for a sum of monomials with coefficients it is the corresponding sum.

**Lemma 1.1.** \(T_{Q_1+Q_2}=T_{Q_1}+T_{Q_2}\), \(T_{cQ}=c\,T_Q\) for \(c\in K\), and
\[
T_{Q_1Q_2}=T_{Q_1}\circ T_{Q_2}=T_{Q_2}\circ T_{Q_1}.
\]

**Proof.** The first two statements are the definition. For two monomials the third holds because all the maps \(\partial_x\) and \(\mu_y\) commute; for sums it follows by linearity. \(\blacksquare\)

A polynomial has the *bidegree* \((i,j)\) if every one of its monomials has the degree \(i\) in the variables of \(V\) and the degree \(j\) in the variables of \(U\). Let \(\mathcal H(i,j)\) be the space of these polynomials, for \(i,j\ge0\). Its dimension is the product of the numbers of the monomials of degree \(i\) in \(v\) variables and of degree \(j\) in \(u\) variables:
\[
\begin{gathered}
\dim\mathcal H(i,j)=h(v,i)\,h(u,j),\\
h(r,t)=\binom{r+t-1}{t}.
\end{gathered}
\]
If \(Q\) has the bidegree \((i,j)\), then \(T_Q\) maps \(\mathcal H(a,b)\) into \(\mathcal H(a-i,b+j)\) for \(a\ge i\), and it is \(0\) on \(\mathcal H(a,b)\) for \(a<i\).

## 2. The measure

Fix integers \(k,m\ge0\), \(a\ge k\) and \(b\ge0\), and put \(n=k+m\). A homogeneous polynomial \(g\) of degree \(n\) is the sum of its *components* \(g_{[i,n-i]}\) of the bidegrees \((i,n-i)\), \(0\le i\le n\).

**Definition.** For a polynomial \(g\in K[V,U]\) that is \(0\) or homogeneous of degree \(n\), let
\[
F_g:\ \mathcal H(a,b)\longrightarrow\mathcal H(a-k,\,b+m)
\]
be the restriction of \(T_{g_{[k,m]}}\) to \(\mathcal H(a,b)\), and
\[
\begin{gathered}
R(g)=\operatorname{rank}F_g,\\
D=\dim\mathcal H(a,b)=h(v,a)\,h(u,b).
\end{gathered}
\]

**Lemma 2.1.** \(R(g)\le D\); \(R(g_1+g_2)\le R(g_1)+R(g_2)\); and \(R(cg)=R(g)\) for \(c\ne0\), \(R(0)=0\).

**Proof.** The component \(g_{[k,m]}\) and the map \(T\) depend linearly on \(g\), so \(F_{g_1+g_2}=F_{g_1}+F_{g_2}\) and \(F_{cg}=cF_g\). The rank of a sum of two linear maps is at most the sum of the ranks, and the rank of \(F_g\) is at most the dimension \(D\) of the space \(\mathcal H(a,b)\) on which it is defined. \(\blacksquare\)

The map \(g\mapsto F_g\) does not turn products into compositions, because it takes one component only. To estimate \(R\) for a product, the product is first split into its components.

## 3. The rank of a product

**Lemma 3.1.** For integers \(0\le I\le a\) and \(J\ge0\), and \(b\ge1\),
\[
\begin{gathered}
\frac{h(v,a-I)}{h(v,a)}\le\Bigl(\frac{a}{a+v-1}\Bigr)^I,\\
\frac{h(u,b+J)}{h(u,b)}\le\Bigl(\frac{b+u}{b}\Bigr)^J .
\end{gathered}
\]

**Proof.** From \(h(r,t)=\binom{r+t-1}t\), for \(t\ge1\),
\[
\frac{h(r,t-1)}{h(r,t)}=\frac{t}{r+t-1} .
\]
So the first ratio is the product of the numbers \(\frac{a-i}{a+v-1-i}\) for \(0\le i<I\), and each is at most \(\frac{a}{a+v-1}\), because \(x/(x+v-1)\) does not decrease in \(x>0\). The second ratio is the product of the numbers \(\frac{b+u+i-1}{b+i}\) for \(1\le i\le J\), and
\[
\frac{b+u+i-1}{b+i}\le\frac{b+u}{b}
\]
because \(b(b+u+i-1)\le(b+u)(b+i)\). \(\blacksquare\)

Let \(Q_1,\dots,Q_r\in K[V,U]\) be homogeneous of the degrees \(e_1,\dots,e_r\ge1\) with \(e_1+\dots+e_r=n\), and put \(\lambda=k/n\). An *assignment* is a sequence \(\mathbf i=(i_1,\dots,i_r)\) of integers with \(0\le i_j\le e_j\) and \(i_1+\dots+i_r=k\). For an assignment put
\[
\begin{gathered}
\delta_j=i_j-\lambda e_j,\qquad I(\mathbf i)=\sum_{j:\ \delta_j>0}i_j,\\
J(\mathbf i)=\sum_{j:\ \delta_j>0}(e_j-i_j).
\end{gathered}
\]
Since \(\lambda n=k\), the numbers \(\delta_j\) add up to \(0\). The number \(\lambda e_j\) is the share of the degree \(e_j\) that falls on \(V\) if the degrees \(k\) and \(m\) are divided among the factors in proportion; \(\delta_j\) says how far the factor \(j\) is from its share.

**Lemma 3.2.** With these notations,
\[
\begin{aligned}
&R(Q_1\cdots Q_r)\\
&\quad\le\sum_{\mathbf i}h(v,a-I(\mathbf i))\,h(u,b+J(\mathbf i)),
\end{aligned}
\]
where the sum runs over all assignments.

**Proof.** The component of the product is the sum of the products of components,
\[
(Q_1\cdots Q_r)_{[k,m]}=\sum_{\mathbf i}\ \prod_{j=1}^r(Q_j)_{[i_j,\,e_j-i_j]} .
\]
By Lemma 1.1, \(F\) of the product is the sum, over the assignments, of the restrictions to \(\mathcal H(a,b)\) of the maps
\[
\prod_{j=1}^rT_j,\qquad T_j=T_{(Q_j)_{[i_j,e_j-i_j]}},
\]
and the \(T_j\) may be composed in any order. Fix an assignment, and apply first the \(T_j\) with \(\delta_j>0\), then the others. The first group maps \(\mathcal H(a,b)\) into \(\mathcal H(a-I,b+J)\) with \(I=I(\mathbf i)\), \(J=J(\mathbf i)\); here \(I\le k\le a\). So the map of this assignment is a composition of two linear maps through the space \(\mathcal H(a-I,b+J)\), and its rank is at most the dimension \(h(v,a-I)h(u,b+J)\) of this space. The rank of a sum is at most the sum of the ranks. \(\blacksquare\)

The intermediate space is small when the first group contains much differentiation and little multiplication: differentiation in \(V\) lowers the dimension, multiplication in \(U\) raises it. The numbers of the next section are chosen so that the two effects cancel exactly for a factor that has its proportional share, and so that every deviation from the share costs a factor.

## 4. The numbers of the proof

From here on \(n\) is the degree and the width of \(\operatorname{IMM}_{n,n}\). The \(n\) layers are divided into \(k\) layers whose \(kn^2\) variables form \(V\) and \(m\) layers whose \(mn^2\) variables form \(U\); which layers go where is fixed later. Let \(s\) be the largest integer with \(s\le\sqrt n\) and \(n-s\) even, and put
\[
\begin{gathered}
k=\frac{n-s}2,\qquad m=\frac{n+s}2,\\
\rho=\frac km,\qquad \lambda=\frac kn,\\
v=kn^2,\qquad u=mn^2,\\
a=\Bigl\lceil\frac{v}{\sqrt n-1}\Bigr\rceil,\quad \alpha=\frac a{a+v},\\
b=\Bigl\lceil\frac{u\,\alpha^\rho}{1-\alpha^\rho}\Bigr\rceil,\quad \beta=\frac b{b+u},\\
q=\alpha^{(1+\rho)/2},\\
D=h(v,a)\,h(u,b).
\end{gathered}
\]
Note \(\lambda=\rho/(1+\rho)\), since \(k+m=n\).

The number \(\alpha\) is the factor by which one differentiation in \(V\) lowers the dimension, and \(\beta^{-1}\) the factor by which one multiplication in \(U\) raises it (Lemma 3.1). Without the rounding in \(a\) and \(b\) one would have \(\alpha=n^{-1/2}\) and \(\beta=\alpha^\rho\), hence \(\alpha^k\beta^{-m}=1\): \(k\) differentiations and \(m\) multiplications leave the dimension unchanged. The difference \(m-k=s\), of the order \(\sqrt n\), makes \(\lambda\) a little smaller than \(\tfrac12\); this is used in the next lesson.

**Lemma 4.1.** There is a number \(n_0\) such that for all \(n\ge n_0\):

1. \(\sqrt n-2<s\le\sqrt n\) and \(s\ge\tfrac12\sqrt n\); \(\lambda=\tfrac12-\tfrac s{2n}\ge\tfrac38\); \(0<\rho<1\) and \(1-\rho\le\tfrac2{\sqrt n}\); \(k\le\tfrac n2\).
2. \(\tfrac14n^3\le v\le u\le n^3\); \(\ \tfrac14n^{5/2}\le a\le n^{5/2}\) and \(\tfrac14n^{5/2}\le b\le4n^{5/2}\); \(a\ge k\) and \(4n\le\min\{a,b\}\).
3. \(n^{-1/2}\le\alpha\le n^{-1/2}\exp(4/n^{5/2})\); in particular \(\alpha^{-1}\le\sqrt n\).
4. \(\alpha^\rho\le\beta\le\alpha^\rho \exp(2/b)\) and \(\beta\le\tfrac2{\sqrt n}\).
5. \(n^{-1/2}\le q\) and \(q\le n^{-1/2}\exp\bigl(\tfrac{\log n}{\sqrt n}+\tfrac4{n^{5/2}}\bigr)\); in particular \(q\le\tfrac2{\sqrt n}\le n^{-2/5}\) and \(q\le\tfrac12\).
6. \(\bigl(1-\tfrac1{a+v}\bigr)^{-n}\le2\).

**Proof.** (1) One of the two integers \(\lfloor\sqrt n\rfloor\), \(\lfloor\sqrt n\rfloor-1\) has the parity of \(n\). The rest follows from \(k=\tfrac{n-s}2\), \(m=\tfrac{n+s}2\ge\tfrac n2\) and \(1-\rho=\tfrac sm\).

(2) By (1), \(k\ge\tfrac{n-\sqrt n}2\ge\tfrac n4\) and \(m\le n\). Let \(a_0=v/(\sqrt n-1)\), so that \(a_0\le a<a_0+1\). Then \(a_0\ge v/\sqrt n\ge\tfrac14n^{5/2}\) and \(a_0\le\tfrac12n^3/(\sqrt n-1)\), which gives the bounds for \(a\) for large \(n\). The bounds for \(b\) are shown with (4).

(3) \(a_0/(a_0+v)=1/\sqrt n\). The function \(x/(x+v)\) increases, and the derivative of its logarithm is \(\tfrac v{x(x+v)}\le\tfrac1x\). So
\[
\log(\alpha\sqrt n)\le\frac{a-a_0}{a_0}\le\frac1{a_0}\le\frac4{n^{5/2}},
\]
and \(\log(\alpha\sqrt n)\ge0\).

(4) By (1) and (3), since \(\alpha^{-1}\le\sqrt n\),
\[
\begin{aligned}
\alpha\le\alpha^\rho&=\alpha\cdot\alpha^{-(1-\rho)}\le\alpha\,n^{(1-\rho)/2}\\
&\le\alpha\exp\Bigl(\frac{\log n}{\sqrt n}\Bigr).
\end{aligned}
\]
We refer to this chain as (4.1).
So \(\alpha^\rho\sqrt n\to1\) as \(n\to\infty\), and \(\alpha^\rho\le\tfrac32n^{-1/2}\) for large \(n\). Let \(b_0=u\alpha^\rho/(1-\alpha^\rho)\), so that \(b_0\le b<b_0+1\) and \(b_0/(b_0+u)=\alpha^\rho\). From \(u\alpha^\rho\le b_0\le2u\alpha^\rho\) and the bounds for \(u\) and \(\alpha^\rho\) follow the bounds for \(b\) in (2). As in (3),
\[
0\le\log\frac{\beta}{\alpha^\rho}\le\frac1{b_0}\le\frac2b ,
\]
because \(b<b_0+1\le2b_0\). For large \(n\) this gives \(\beta\le\tfrac32n^{-1/2}\exp(2/b)\le2n^{-1/2}\).

(5) Since \(0<\alpha<1\) and \(\rho\le\tfrac{1+\rho}2\le1\), we have \(\alpha\le q\le\alpha^\rho\). Use (3) and (4.1). The right side is \(n^{-1/2}\) times a factor that tends to \(1\).

(6) \(a+v\ge\tfrac14n^3\), so \((1-\tfrac1{a+v})^{-n}\le\exp(\tfrac{2n}{a+v})\), and this is at most \(\exp(8/n^2)\le2\). \(\blacksquare\)

In the following lessons "for large \(n\)" means: for all \(n\ge n_0\), with a number \(n_0\) that is enlarged finitely many times and never depends on the field, on a circuit, or on the choice of the layers.

## 5. The product bound

For an integer \(e\ge1\) put
\[
H_e=\sum_{i=0}^eq^{|i-\lambda e|} .
\]

**Proposition 5.1** ([OpenAI-D]). Let \(n\ge n_0\), with the numbers of Section 4 and any division of the layers into \(k\) layers for \(V\) and \(m\) layers for \(U\). Let \(Q_1,\dots,Q_r\in K[V,U]\) be homogeneous of the degrees \(e_1,\dots,e_r\ge1\) with \(e_1+\dots+e_r=n\). Then
\[
R(Q_1\cdots Q_r)\le2D\prod_{j=1}^rH_{e_j} .
\]

**Proof.** By Lemma 3.2 it is enough to show, for every assignment \(\mathbf i\) with \(I=I(\mathbf i)\), \(J=J(\mathbf i)\),
\[
h(v,a-I)\,h(u,b+J)\le2D\prod_jq^{|\delta_j|}.
\]
We refer to this inequality as (5.1). It is enough, because the sum of the right sides over the assignments is at most the sum over all sequences \((i_1,\dots,i_r)\) with \(0\le i_j\le e_j\), without the condition on their sum, and that sum is the product of the \(H_{e_j}\).

By Lemma 3.1, and by \(\beta\ge\alpha^\rho\) (Lemma 4.1(4)),
\[
\begin{aligned}
&\frac{h(v,a-I)\,h(u,b+J)}{D}\\
&\qquad\le\Bigl(\frac a{a+v-1}\Bigr)^I\beta^{-J}\\
&\qquad\le\alpha^{I-\rho J}\Bigl(1-\frac1{a+v}\Bigr)^{-I} ,
\end{aligned}
\]
because \(\frac a{a+v-1}=\alpha\,(1-\frac1{a+v})^{-1}\). The last factor is at most \(2\) by Lemma 4.1(6), since \(I\le k\le n\). For the exponent, write \(i_j=\lambda e_j+\delta_j\) and \(e_j-i_j=(1-\lambda)e_j-\delta_j\). Then \(i_j-\rho(e_j-i_j)\) is \(\bigl(\lambda-\rho(1-\lambda)\bigr)e_j+(1+\rho)\delta_j\). From \(\lambda=\rho/(1+\rho)\) we get \(\lambda-\rho(1-\lambda)=0\), so
\[
\begin{aligned}
I-\rho J&=\sum_{j:\ \delta_j>0}\bigl(i_j-\rho(e_j-i_j)\bigr)\\
&=(1+\rho)\sum_{j:\ \delta_j>0}\delta_j .
\end{aligned}
\]
Since the \(\delta_j\) add up to \(0\), the sum of the positive ones is half the sum of all \(|\delta_j|\). Hence
\[
\alpha^{I-\rho J}=\alpha^{\frac{1+\rho}2\sum_j|\delta_j|}=\prod_jq^{|\delta_j|} .
\]
This is (5.1). \(\blacksquare\)

Each factor \(Q_j\) contributes \(H_{e_j}\), a sum over the possible degrees \(i\) of its part in \(V\), weighted by \(q^{|i-\lambda e_j|}\). Since \(q\) is about \(n^{-1/2}\), the weight is small unless \(i\) is close to the share \(\lambda e_j\). But \(i\) is an integer. If \(\lambda e_j\) is far from every integer, every term of \(H_{e_j}\) is small. The next lesson makes this precise.

## 6. Exercises

**6.1.** Let \(V=\{x\}\), \(U=\{y\}\), \(Q=xy\). Compute \(T_Q(x^2y)\) and \(T_{Q^2}(x^2y)\), and check \(T_{Q^2}=T_Q\circ T_Q\) on this polynomial.

**6.2.** Let \(v=u=2\), \(k=m=1\), \(a=1\), \(b=0\), and \(g=x_1y_1+x_2y_2\) with \(V=\{x_1,x_2\}\), \(U=\{y_1,y_2\}\). Find \(D\), the matrix of \(F_g\) in the bases of the monomials, and \(R(g)\).

**6.3.** Show that \(R(g)\le D\) and \(R(g)\le h(v,a-k)\,h(u,b+m)\), and that for a product \(g=Q_1Q_2\) in which \(Q_1\) contains only variables of \(V\) and has the degree \(k\), the map \(F_g\) is a composition through \(\mathcal H(a-k,b)\).

**6.4.** In Lemma 3.2 let \(r=2\), \(e_1=e_2=1\), \(k=m=1\) (so \(n=2\), \(\lambda=\tfrac12\)). List the assignments with their \(\delta_j\), \(I\), \(J\) and the intermediate spaces.

**6.5.** Check \(\lambda-\rho(1-\lambda)=0\) and \(\alpha^k\beta^{-m}=1\) under the assumption \(\beta=\alpha^\rho\).

## 7. Solutions

**6.1.** \(T_Q=\partial_x\circ\mu_y\): \(T_Q(x^2y)=\partial_x(x^2y^2)=2xy^2\). \(T_{Q^2}=\partial_x^2\circ\mu_y^2\): \(T_{Q^2}(x^2y)=\partial_x^2(x^2y^3)=2y^3\). And \(T_Q(T_Q(x^2y))=T_Q(2xy^2)\), which is \(\partial_x(2xy^3)=2y^3\).

**6.2.** \(D=h(2,1)h(2,0)=2\): the space \(\mathcal H(1,0)\) has the basis \(x_1,x_2\). The space \(\mathcal H(0,1)\), into which \(F_g\) maps, has the basis \(y_1,y_2\). \(F_g=\partial_{x_1}\mu_{y_1}+\partial_{x_2}\mu_{y_2}\) maps \(x_1\) to \(y_1\) and \(x_2\) to \(y_2\). The matrix is the unit matrix, and \(R(g)=2\).

**6.3.** The rank of a linear map from a space \(X\) to a space \(Y\) is at most the dimension of \(X\) and at most the dimension of \(Y\). For \(g=Q_1Q_2\) as stated, \(g_{[k,m]}=Q_1\cdot(Q_2)_{[0,m]}\), so \(F_g=T_{(Q_2)_{[0,m]}}\circ T_{Q_1}\), and \(T_{Q_1}\) maps \(\mathcal H(a,b)\) into \(\mathcal H(a-k,b)\).

**6.4.** The assignments are \((1,0)\) and \((0,1)\). For \((1,0)\): \(\delta_1=\tfrac12\), \(\delta_2=-\tfrac12\); the first group is the factor \(1\), with \(I=1\), \(J=0\); the intermediate space is \(\mathcal H(a-1,b)\). For \((0,1)\) the same with the two factors exchanged. So \(R(Q_1Q_2)\le2\,h(v,a-1)h(u,b)\).

**6.5.** \(1-\lambda=\tfrac1{1+\rho}\), so \(\rho(1-\lambda)=\tfrac\rho{1+\rho}=\lambda\). And \(\alpha^k\beta^{-m}=\alpha^{k-\rho m}=\alpha^0\), because \(\rho m=k\).

## References

- [OpenAI-D] OpenAI, *Homogeneous depth-five lower bounds for iterated matrix multiplication*, OpenAI Math Release preprint, 25 September 2026, Sections 2 and 3.1. https://github.com/openai/math/tree/main/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026
