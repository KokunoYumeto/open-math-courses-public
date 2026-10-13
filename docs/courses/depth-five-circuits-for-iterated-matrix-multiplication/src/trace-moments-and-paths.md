# Trace moments and paths

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson begins the proof that the measure \(R\) of \(f=\operatorname{IMM}_{n,n}\) is almost as large as it can be: \(R(f)\ge D\,e^{-6\sqrt n}\). The rank of the map \(F_f\) is estimated from below by two traces, \(T=\operatorname{tr}(F_f^*F_f)\) and \(T_2=\operatorname{tr}((F_f^*F_f)^2)\). In a suitable basis the matrix of \(F_f\) is described by the paths of the polynomial. The first trace is a sum over paths, and the second is a sum over certain quadruples of paths. The lesson computes the first and reduces the second to a sum over words in two letters, which the last lesson estimates.

- The division of the layers into \(V\) and \(U\) (Section 1).
- \(\operatorname{rank}F\ge T^2/T_2\) (Lemma 2.1).
- The matrix of \(F_f\) and the first trace as a sum over paths (Lemma 3.1).
- Moments of a random composition and of geometric variables (Lemmas 4.1 and 4.2).
- \(T\ge D\,n^{n-1}\mu\,e^{-6/\sqrt n}\) (Proposition 5.1).
- Four paths, the two types of a layer, and the reduction of \(T_2\) (Proposition 7.1).

The lesson follows [OpenAI-D, Section 4]. It uses the numbers and the map \(F_g\) from [A rank measure from differentiation and multiplication](a-rank-measure-from-differentiation-and-multiplication.md), and the adjoint, the trace and orthogonal projections from linear algebra ([Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40), core course). In this lesson and the next the field is \(\mathbb C\).

## 1. The division of the layers

The numbers \(s,k,m\) satisfy \(k+m=n\) and \(m=k+s\), and \(0<s<k\) for large \(n\). For \(1\le i\le k\) put
\[
l_i=1+\Bigl\lfloor\frac{is}k\Bigr\rfloor-\Bigl\lfloor\frac{(i-1)s}k\Bigr\rfloor .
\]
Since \(0<\tfrac sk<1\), every \(l_i\) is \(1\) or \(2\), and \(l_1+\dots+l_k=k+s=m\). The layers \(1,\dots,n\) are divided into \(k\) *chunks* of consecutive layers; the chunk \(i\) consists of one layer for \(V\) followed by \(l_i\) layers for \(U\):
\[
V\,U^{l_1}\ V\,U^{l_2}\ \cdots\ V\,U^{l_k}.
\]
All \(n^2\) variables of a layer belong to the group of the layer. So \(V\) has \(v=kn^2\) variables and \(U\) has \(u=mn^2\). We say *\(V\) layer* and *\(U\) layer*.

Three properties are used: the layer \(1\) is a \(V\) layer and the layer \(n\) is a \(U\) layer; no two \(V\) layers are adjacent; and the \(V\) layers are spread evenly, which is made precise and used in the last lesson.

Put \(f=\operatorname{IMM}_{n,n}\). Every monomial of \(f\) contains one variable of each layer, so \(f\) has the bidegree \((k,m)\), and \(F_f\) is the restriction of \(T_f\) to \(\mathcal H(a,b)\). By the definition of \(T\) and by the sum over the paths,
\[
T_f=\sum_P\prod_{t\in L_V}\partial_{E_t(P)}\prod_{t\in L_U}\mu_{E_t(P)},
\]
where \(L_V\) is the set of the \(V\) layers and \(L_U\) the set of the \(U\) layers. We refer to this formula as (1.1).

## 2. Two traces bound the rank

Let \(X\) and \(Y\) be finite-dimensional complex vector spaces with inner products, and \(F:X\to Y\) a linear map with the adjoint \(F^*:Y\to X\). Put
\[
T=\operatorname{tr}(F^*F),\qquad T_2=\operatorname{tr}\bigl((F^*F)^2\bigr).
\]
If \((F_{yx})\) is the matrix of \(F\) in orthonormal bases of \(X\) and \(Y\), then \(F^*F\) has the entries \(\sum_y\overline{F_{yx}}F_{yx'}\), and
\[
\begin{gathered}
T=\sum_{x,y}|F_{yx}|^2,\\
T_2=\sum_{x,x'}\Bigl|\sum_y\overline{F_{yx}}F_{yx'}\Bigr|^2 .
\end{gathered}
\]
We refer to these two formulas as (2.1). The second formula holds because \(F^*F\) is self-adjoint: the trace of the square of a self-adjoint matrix is the sum of the squares of the absolute values of its entries.

**Lemma 2.1.** If \(T>0\), then
\[
\operatorname{rank}F\ge\frac{T^2}{T_2}.
\]

**Proof.** Put \(H=F^*F\). Then \(\langle Hx,x\rangle=\|Fx\|^2\), so \(H\) and \(F\) have the same kernel and the same rank \(\rho\). Let \(\Pi\) be the orthogonal projection of \(X\) onto the image of \(H\). Then \(\Pi H=H\), \(\Pi^*=\Pi=\Pi^2\) and \(\operatorname{tr}\Pi=\rho\). On the linear maps from \(X\) to \(X\), \(\langle A,B\rangle=\operatorname{tr}(A^*B)\) is an inner product; in an orthonormal basis it is \(\sum_{i,j}\overline{A_{ij}}B_{ij}\). By the Cauchy–Schwarz inequality for it,
\[
\begin{aligned}
T&=\operatorname{tr}(\Pi^*H)\\
&\le\sqrt{\operatorname{tr}(\Pi^*\Pi)}\,\sqrt{\operatorname{tr}(H^*H)}\\
&=\sqrt\rho\,\sqrt{T_2}.
\end{aligned}
\]
Here \(T_2>0\) because \(H\ne0\). So \(\rho\ge T^2/T_2\). \(\blacksquare\)

If \(H\) has \(\rho\) eigenvalues that are all equal, and the others \(0\), the lemma holds with equality. The lemma gives a good bound when the eigenvalues of \(F^*F\) are of the same order.

## 3. The matrix of \(F_f\)

An *index* is a function \(M\) that assigns to every variable \(z\) of \(V\cup U\) an integer \(M_z\ge0\), with the sum \(a\) over the variables of \(V\) and the sum \(b\) over the variables of \(U\). There are \(D\) indices. For an index put
\[
\begin{gathered}
z^M=\prod_zz^{M_z},\qquad M!=\prod_zM_z!,\\
b_M=\frac{z^M}{\sqrt{M!}} .
\end{gathered}
\]
The \(b_M\) are a basis of \(\mathcal H(a,b)\). We give \(\mathcal H(a,b)\) the inner product for which they are orthonormal, and we do the same for \(\mathcal H(a-k,b+m)\), whose indices have the sums \(a-k\) and \(b+m\). For a variable \(z\) let \(\mathbf e_z\) be the function that is \(1\) at \(z\) and \(0\) elsewhere. Then
\[
\begin{gathered}
\partial_z\,b_M=\sqrt{M_z}\ b_{M-\mathbf e_z},\\
z\cdot b_M=\sqrt{M_z+1}\ b_{M+\mathbf e_z},
\end{gathered}
\]
where the first expression means \(0\) if \(M_z=0\). We refer to these two formulas as (3.1). Indeed \(\partial_zz^M=M_zz^{M-\mathbf e_z}\) and \(M!=M_z\cdot(M-\mathbf e_z)!\); and \((M+\mathbf e_z)!=(M_z+1)\,M!\).

For a path \(P\) put
\[
\epsilon_P=-\sum_{t\in L_V}\mathbf e_{E_t(P)}+\sum_{t\in L_U}\mathbf e_{E_t(P)},
\]
\[
\begin{aligned}
\phi_P(M)={}&\prod_{t\in L_V}M_{E_t(P)}\\
&\cdot\prod_{t\in L_U}\bigl(M_{E_t(P)}+1\bigr),
\end{aligned}
\]
and \(c_P(M)=\phi_P(M)^{1/2}\).

**Lemma 3.1.** (1) For every index \(M\),
\[
F_f\,b_M=\sum_Pc_P(M)\,b_{M+\epsilon_P},
\]
where a term with \(c_P(M)=0\) is left out.

(2) Different paths have different \(\epsilon_P\). So the entry of the matrix of \(F_f\) at \((M',M)\) is \(c_P(M)\) if \(M'=M+\epsilon_P\) for a path \(P\), and \(0\) if there is no such path.

(3) Let \(\mathbb E\) be the mean over the \(D\) indices \(M\). Then
\[
T=D\sum_P\mathbb E\,\phi_P(M).
\]

**Proof.** (1) The coordinates \(E_t(P)\) of a path in different layers are different variables. So by (3.1) the term of \(P\) in (1.1) maps \(b_M\) to \(c_P(M)\,b_{M+\epsilon_P}\); if \(M_{E_t(P)}=0\) for a \(V\) layer \(t\), both sides are \(0\).

(2) \(\epsilon_P\) determines the coordinate \(E_t(P)\) of the path in every layer, and the coordinates determine the path.

(3) By (2.1) and (2), \(T=\sum_M\sum_Pc_P(M)^2\). \(\blacksquare\)

Under the uniform distribution on the indices, the restriction of \(M\) to \(V\) is uniformly distributed among the functions on \(V\) with the sum \(a\), the restriction to \(U\) among those on \(U\) with the sum \(b\), and the two restrictions are independent.

## 4. Moments of compositions

A *composition* of an integer \(t\ge0\) into \(r\ge1\) parts is a sequence \((M_1,\dots,M_r)\) of integers \(\ge0\) with the sum \(t\). There are \(\binom{t+r-1}t\) of them. For integers \(d\ge0\) write
\[
(z)_d=z(z-1)\cdots(z-d+1),
\]
the *falling factorial*, with \((z)_0=1\). For integers \(r\ge1\) and \(h\ge0\) write
\[
r^{\overline h}=r(r+1)\cdots(r+h-1),
\]
with \(r^{\overline 0}=1\).

**Lemma 4.1.** Let \(M\) be uniformly distributed among the compositions of \(t\) into \(r\) parts. For integers \(d_1,\dots,d_r\ge0\) with the sum \(h\),
\[
\mathbb E\prod_{i=1}^r(M_i)_{d_i}=\frac{(t)_h}{r^{\overline h}}\prod_{i=1}^rd_i! .
\]

**Proof.** In formal power series in \(y\),
\[
\sum_{j\ge0}(j)_d\,y^j=\frac{d!\,y^d}{(1-y)^{d+1}} ,
\]
because \((j)_d=d!\binom jd\) and \(\sum_{j\ge d}\binom jdy^j=y^d(1-y)^{-(d+1)}\).
Multiply these series for \(d=d_1,\dots,d_r\). The coefficient of \(y^t\) in the product is the sum of \(\prod_i(M_i)_{d_i}\) over all compositions of \(t\); on the other side it is the coefficient of \(y^{t-h}\) in \(\prod_id_i!\cdot(1-y)^{-(h+r)}\), which is \(\prod_id_i!\cdot\binom{t+r-1}{t-h}\), and \(0\) if \(h>t\). Dividing by \(\binom{t+r-1}t\) gives
\[
\begin{aligned}
\frac{\binom{t+r-1}{t-h}}{\binom{t+r-1}t}&=\frac{t!\,(r-1)!}{(t-h)!\,(r+h-1)!}\\
&=\frac{(t)_h}{r^{\overline h}}
\end{aligned}
\]
for \(h\le t\); for \(h>t\) both sides of the lemma are \(0\). \(\blacksquare\)

A random variable \(Z\) with values in the integers \(\ge0\) is *geometric with the mean \(G>0\)* if
\[
\Pr(Z=j)=\frac1{1+G}\Bigl(\frac G{1+G}\Bigr)^j
\]
for all integers \(j\ge0\).
With \(y=\tfrac G{1+G}\), so that \(\tfrac y{1-y}=G\), the series above gives
\[
\begin{aligned}
\mathbb E(Z)_d&=(1-y)\frac{d!\,y^d}{(1-y)^{d+1}}\\
&=d!\,G^d .
\end{aligned}
\]
We refer to this formula as (4.1). In particular \(\mathbb EZ=G\) and \(\mathbb EZ^2=\mathbb E(Z)_2+\mathbb EZ=2G^2+G\).

A polynomial \(p(z_1,\dots,z_r)\) is *factorially positive* if it is a sum of products \(\prod_i(z_i)_{d_i}\) with coefficients \(\ge0\). The largest number \(d_1+\dots+d_r\) that occurs is its *order*. Sums and products of factorially positive polynomials in disjoint sets of variables are factorially positive. Examples in one variable:
\[
\begin{gathered}
z=(z)_1,\qquad z+1=(z)_1+1,\\
z^2=(z)_2+(z)_1,\\
(z+1)^2=(z)_2+3(z)_1+1 .
\end{gathered}
\]

**Lemma 4.2.** Let \(M\) be as in Lemma 4.1 with \(t\ge1\), and let \(Z_1,\dots,Z_r\) be independent geometric variables with the mean \(G=t/r\). Let \(p\) be factorially positive. Then
\[
\mathbb E\,p(M)\le\mathbb E\,p(Z).
\]
If the order of \(p\) is at most \(h_0\) and \(h_0\le t/2\), then also
\[
\mathbb E\,p(M)\ge\exp\Bigl(-\frac{h_0^2}t-\frac{h_0^2}{2r}\Bigr)\,\mathbb E\,p(Z).
\]

**Proof.** It is enough to treat \(p=\prod_i(z_i)_{d_i}\) with \(h=\sum_id_i\). By (4.1) and the independence, \(\mathbb Ep(Z)=\prod_id_i!\cdot(t/r)^h\). By Lemma 4.1,
\[
\begin{aligned}
\frac{\mathbb E\,p(M)}{\mathbb E\,p(Z)}&=\frac{(t)_h\,r^h}{t^h\,r^{\overline h}}\\
&=\prod_{j=0}^{h-1}\frac{1-j/t}{1+j/r} .
\end{aligned}
\]
Every factor lies between \(0\) and \(1\) (for \(h>t\) one factor is \(0\)). This is the first statement. For \(h\le h_0\le t/2\) use \(\log(1-x)\ge-2x\) for \(0\le x\le\tfrac12\) and \(\log(1+x)\le x\): the logarithm of the product is at least
\[
-\sum_{j=0}^{h-1}\Bigl(\frac{2j}t+\frac jr\Bigr)\ge-\frac{h^2}t-\frac{h^2}{2r}. \qquad\blacksquare
\]

The parts of a random composition are not independent. The lemma compares them with independent variables only for the means of factorially positive polynomials.

## 5. The first trace

Put
\[
\begin{gathered}
A=\frac av,\qquad B=\frac bu,\\
\mu=A^k(1+B)^m .
\end{gathered}
\]
From \(\alpha=\tfrac a{a+v}\) and \(\beta=\tfrac b{b+u}\),
\[
\frac{A+1}A=\alpha^{-1},\qquad\frac B{B+1}=\beta .
\]
We refer to these two equations as (5.1).

**Proposition 5.1.** For large \(n\),
\[
T\ge D\,n^{n-1}\,\mu\,e^{-6/\sqrt n}>0 .
\]

**Proof.** Fix a path \(P\). The polynomial \(\phi_P\) of Lemma 3.1 is a product \(p_V\cdot p_U\). The factor \(p_V\) is the product of \(k\) different variables of \(V\); it is factorially positive of the order \(k\). The factor \(p_U\) is the product of \(z+1\) over \(m\) different variables of \(U\); it is factorially positive of the order \(m\). By the independence of the two restrictions of \(M\), the mean of the product is the product of the means. For independent geometric variables with the means \(A\) on \(V\) and \(B\) on \(U\), the means are \(A^k\) and \((1+B)^m\). By Lemma 4.2, applied to the compositions of \(a\) into \(v\) parts and of \(b\) into \(u\) parts, \(\mathbb E[p_Vp_U]\ge\mu\,e^{-\theta}\) with
\[
\theta=\frac{k^2}a+\frac{k^2}{2v}+\frac{m^2}b+\frac{m^2}{2u}.
\]
The conditions \(k\le\tfrac a2\) and \(m\le\tfrac b2\) hold because \(4n\le\min\{a,b\}\) (Lemma 4.1 of the lesson on the rank measure, also for the next estimates). With \(k\le\tfrac n2\), \(m\le n\), \(a,b\ge\tfrac14n^{5/2}\) and \(v,u\ge\tfrac14n^3\), the four terms of \(\theta\) are at most \(n^{-1/2}\), \(\tfrac1{2n}\), \(4n^{-1/2}\) and \(\tfrac2n\); so \(\theta\le6n^{-1/2}\). There are \(n^{n-1}\) paths. \(\blacksquare\)

## 6. Four paths

By (2.1) and Lemma 3.1(2), the entry of \(F_f^*F_f\) at \((M,M')\) is the sum of \(c_P(M)\,c_Q(M')\) over the pairs of paths \((P,Q)\) with \(M+\epsilon_P=M'+\epsilon_Q\). Squaring and adding,
\[
\begin{aligned}
T_2=\sum_M\ \sum_{(P,Q,R,S)}&c_P(M)\,c_Q(M')\\
&\cdot c_R(M)\,c_S(M'),
\end{aligned}
\]
where \(M'=M+\epsilon_P-\epsilon_Q\), and the inner sum runs over the quadruples of paths with
\[
\epsilon_P-\epsilon_Q=\epsilon_R-\epsilon_S
\]
for which \(M'\) is an index, that is, has no negative value. We refer to the formula for \(T_2\) as (6.1) and to the condition on the four paths as (6.2). The quadruples with (6.2) are called *compatible*.

**Lemma 6.1.** A quadruple is compatible if and only if every layer \(t\) has one of the following two types:

- type \(\mathcal N\): \(E_t(P)=E_t(Q)\) and \(E_t(R)=E_t(S)\);
- type \(\mathcal D\): \(E_t(P)=E_t(R)\) and \(E_t(Q)=E_t(S)\), and \(E_t(P)\ne E_t(Q)\).

The two types exclude each other.

**Proof.** Let \(c_1,c_2,c_3,c_4\) be the coordinates of \(P,Q,R,S\) in the layer \(t\). The variables of different layers are different, so (6.2) holds if and only if \(\mathbf e_{c_1}-\mathbf e_{c_2}=\mathbf e_{c_3}-\mathbf e_{c_4}\) in every layer. If this function is \(0\), then \(c_1=c_2\) and \(c_3=c_4\). Otherwise \(c_1\ne c_2\), the function is \(1\) at \(c_1\) and \(-1\) at \(c_2\), and so \(c_3=c_1\) and \(c_4=c_2\). \(\blacksquare\)

So a compatible quadruple has a *type word* \(\tau\in\{\mathcal N,\mathcal D\}^n\). In a layer of the type \(\mathcal N\) let \(i\) be the common coordinate of \(P,Q\) and \(j\) the common coordinate of \(R,S\). In a layer of the type \(\mathcal D\) let \(i\) be the common coordinate of \(P,R\) and \(j\) the common coordinate of \(Q,S\).

**Lemma 6.2.** Let \((P,Q,R,S)\) be a compatible quadruple and \(M\) an index. If \(M'\) is an index, the product of the four numbers in (6.1) is the product over the layers of the following polynomials in \(M_i\) and \(M_j\):

| | type \(\mathcal N\) | type \(\mathcal D\) |
|---|---|---|
| \(V\) layer | \(M_iM_j\) | \(M_i(M_j+1)\) |
| \(U\) layer | \((M_i+1)(M_j+1)\) | \((M_i+1)M_j\) |

If \(M'\) has a negative value, the product of these polynomials is \(0\).

**Proof.** Each of the four numbers is the square root of a product over the layers, and the factor of a layer depends only on the value of \(M\) or \(M'\) at the coordinate of the path in this layer. In a layer of the type \(\mathcal N\), \(M'\) and \(M\) agree on the variables of the layer. So \(P\) and \(Q\) both give \(\sqrt{M_i}\), and \(R\) and \(S\) both give \(\sqrt{M_j}\), in a \(V\) layer; in a \(U\) layer they give \(\sqrt{M_i+1}\) and \(\sqrt{M_j+1}\). In a \(V\) layer of the type \(\mathcal D\), \(M'=M-\mathbf e_i+\mathbf e_j\) on the variables of the layer; \(P\) and \(R\) give \(\sqrt{M_i}\) each, and \(Q\) and \(S\) give \(\sqrt{M'_j}=\sqrt{M_j+1}\) each. In a \(U\) layer of the type \(\mathcal D\), \(M'=M+\mathbf e_i-\mathbf e_j\); \(P\) and \(R\) give \(\sqrt{M_i+1}\), and \(Q\) and \(S\) give \(\sqrt{M'_j+1}=\sqrt{M_j}\).

\(M'\) can have a negative value only in a layer of the type \(\mathcal D\): the value \(M_i-1\) in a \(V\) layer with \(M_i=0\), or the value \(M_j-1\) in a \(U\) layer with \(M_j=0\). In both cases the polynomial of the table is \(0\). \(\blacksquare\)

So (6.1) becomes
\[
T_2=D\ \mathbb E\sum_{\mathrm{compatible}}\ \prod_{t=1}^n\pi_t(M),
\]
where the sum runs over the compatible quadruples and \(\pi_t\) is the polynomial of the table for the layer \(t\). We refer to this formula as (6.3).

**Lemma 6.3.** For a compatible quadruple,
\[
\mathbb E\prod_t\pi_t(M)\le\mu^2\prod_t\omega_t,
\]
with the following numbers \(\omega_t\):

| | type \(\mathcal N\), \(i\ne j\) | type \(\mathcal N\), \(i=j\) | type \(\mathcal D\) |
|---|---|---|---|
| \(V\) layer | \(1\) | \(1+\alpha^{-1}\) | \(\alpha^{-1}\) |
| \(U\) layer | \(1\) | \(1+\beta\) | \(\beta\) |

**Proof.** The polynomials of different layers contain different variables. Each \(\pi_t\) is factorially positive: for \(i\ne j\) it is a product of \(z\) or \(z+1\) in two different variables, and for \(i=j\), which occurs only in the type \(\mathcal N\), it is \(z^2\) or \((z+1)^2\). So the product over the \(V\) layers and the product over the \(U\) layers are factorially positive, and by Lemma 4.2, used for \(V\) and for \(U\), the mean is at most the mean for independent geometric variables with the means \(A\) on \(V\) and \(B\) on \(U\). That mean is the product over the layers of

- \(A^2\), \(2A^2+A\), \(A(A+1)\) in a \(V\) layer, for the three columns of the table;
- \((1+B)^2\), \(2B^2+3B+1\), \((B+1)B\) in a \(U\) layer.

Here \(\mathbb E(Z+1)^2=2B^2+B+2B+1\). Divide by \(A^2\) in the \(V\) layers and by \((1+B)^2\) in the \(U\) layers, and use (5.1): \(\tfrac{2A^2+A}{A^2}=1+\tfrac{A+1}A\), and \(\tfrac{2B^2+3B+1}{(1+B)^2}=\tfrac{2B+1}{B+1}=1+\tfrac B{B+1}\). The divisors multiply to \(A^{2k}(1+B)^{2m}=\mu^2\). \(\blacksquare\)

A layer of the type \(\mathcal D\) in \(V\) costs the factor \(\alpha^{-1}\), about \(\sqrt n\); in \(U\) it gains the factor \(\beta\), about \(n^{-1/2}\) to the power \(\rho\). A layer of the type \(\mathcal N\) is neutral, except when the two coordinates agree.

## 7. Type words

We count the compatible quadruples of a given type word, together with their numbers \(\omega_t\).

For a path \(P\) write \(P(t)\) for its value at the position \(t\), \(0\le t\le n\), so that \(E_t(P)=x^{(t)}_{P(t-1),P(t)}\). Two paths have the same coordinate in the layer \(t\) if and only if they agree at the positions \(t-1\) and \(t\). The positions \(1,\dots,n-1\) are the *inner* positions; at the positions \(0\) and \(n\) all paths have the value \(1\).

For a word \(\tau\in\{\mathcal N,\mathcal D\}^n\), a quadruple is *\(\tau\)-admissible* if in every layer of the type \(\mathcal N\) in \(\tau\) the paths \(P,Q\) have the same coordinate and \(R,S\) have the same coordinate, and in every layer of the type \(\mathcal D\) the paths \(P,R\) have the same coordinate and \(Q,S\) have the same coordinate. A compatible quadruple is admissible for its type word. The condition \(p\ne q\) of the type \(\mathcal D\) is dropped, so a \(\tau\)-admissible quadruple need not have the type word \(\tau\). To a \(\tau\)-admissible quadruple and a layer \(t\) we assign the number \(\omega_t^\tau\) of the table of Lemma 6.3 for the type \(\tau_t\), with \(i=E_t(P)\) and \(j=E_t(R)\) in the type \(\mathcal N\). For a compatible quadruple with the type word \(\tau\) these are the numbers \(\omega_t\).

Let \(w(\tau)\) be the number of the *switches* of \(\tau\): the positions \(t\in\{1,\dots,n-1\}\) with \(\tau_t\ne\tau_{t+1}\).

**Lemma 7.1.** The \(\tau\)-admissible quadruples are obtained by choosing independently at every inner position \(t\):

- if \(\tau_t=\tau_{t+1}=\mathcal N\): values with \(P(t)=Q(t)\) and \(R(t)=S(t)\) (\(n^2\) choices);
- if \(\tau_t=\tau_{t+1}=\mathcal D\): values with \(P(t)=R(t)\) and \(Q(t)=S(t)\) (\(n^2\) choices);
- if \(\tau_t\ne\tau_{t+1}\): values with \(P(t)=Q(t)=R(t)=S(t)\) (\(n\) choices).

Their number is \(n^{2(n-1)-w(\tau)}\).

**Proof.** The condition of a layer \(t\) is a condition at its two end positions \(t-1\) and \(t\): the type \(\mathcal N\) requires there that \(P,Q\) agree and that \(R,S\) agree, the type \(\mathcal D\) that \(P,R\) agree and that \(Q,S\) agree. At the positions \(0\) and \(n\) this holds for all paths. An inner position \(t\) is an end position of the layers \(t\) and \(t+1\), and it receives the conditions of both. There are \(w(\tau)\) inner positions with \(n\) choices and \(n-1-w(\tau)\) with \(n^2\) choices. \(\blacksquare\)

For a layer \(t\) with \(\tau_t=\mathcal N\) let \(h_t\) be the number of its end positions that are inner positions and whose other layer also has the type \(\mathcal N\) in \(\tau\). So \(h_t\in\{0,1,2\}\).

**Lemma 7.2.** Choose a \(\tau\)-admissible quadruple uniformly at random, and let \(t\) be a layer with \(\tau_t=\mathcal N\). Then \(E_t(P)=E_t(R)\) with the probability \(n^{-h_t}\). For layers no two of which are adjacent, these events are independent.

**Proof.** \(E_t(P)=E_t(R)\) means that \(P\) and \(R\) agree at both end positions of the layer. At an end position \(0\) or \(n\), and at an inner end position whose other layer has the type \(\mathcal D\), this holds for all admissible quadruples (Lemma 7.1). At an inner end position whose other layer has the type \(\mathcal N\), the values of \(P\) and \(R\) are independent and uniformly distributed, so they agree with the probability \(\tfrac1n\). By Lemma 7.1 the choices at different positions are independent, and layers that are not adjacent have no common end position. \(\blacksquare\)

For a word \(\tau\) let \(d_V(\tau)\) and \(d_U(\tau)\) be the numbers of the \(V\) layers and of the \(U\) layers of the type \(\mathcal D\), and \(N_V(\tau)\) the set of the \(V\) layers of the type \(\mathcal N\). Put
\[
\begin{aligned}
W(\tau)={}&n^{-w(\tau)}\,\alpha^{-d_V(\tau)}\,\beta^{d_U(\tau)}\\
&\cdot\prod_{t\in N_V(\tau)}\bigl(1+\alpha^{-1}n^{-h_t}\bigr).
\end{aligned}
\]

**Proposition 7.1** ([OpenAI-D]). For large \(n\),
\[
T_2\le D\,n^{2(n-1)}\,\mu^2\,(1+\beta)^m\sum_\tau W(\tau),
\]
where the sum runs over all words \(\tau\in\{\mathcal N,\mathcal D\}^n\).

**Proof.** By (6.3) and Lemma 6.3,
\[
\begin{aligned}
\frac{T_2}{D\mu^2}&\le\sum_{\mathrm{compatible}}\ \prod_t\omega_t\\
&\le\sum_\tau\ \sum_{\tau\text{-admissible}}\ \prod_t\omega_t^\tau ,
\end{aligned}
\]
because every compatible quadruple occurs on the right side for its type word, with the same numbers, and all other terms are \(\ge0\). Fix \(\tau\). The inner sum is the number \(n^{2(n-1)-w(\tau)}\) of the \(\tau\)-admissible quadruples times the mean of \(\prod_t\omega^\tau_t\) for a uniformly chosen one. In this product the layers of the type \(\mathcal D\) give \(\alpha^{-d_V(\tau)}\beta^{d_U(\tau)}\). Every \(U\) layer of the type \(\mathcal N\) gives at most \(1+\beta\), and there are at most \(m\) of them. A \(V\) layer \(t\) of the type \(\mathcal N\) gives \(1+\alpha^{-1}\) if \(E_t(P)=E_t(R)\), and \(1\) otherwise. No two \(V\) layers are adjacent, so by Lemma 7.2 the mean of the product of these factors is
\[
\prod_{t\in N_V(\tau)}\bigl(1+\alpha^{-1}n^{-h_t}\bigr). \qquad\blacksquare
\]

The sum of the \(W(\tau)\) is estimated in [The sum over type words and the lower bound](the-sum-over-type-words-and-the-lower-bound.md). For the word \(\mathcal N^n\), in which every layer has the type \(\mathcal N\), the layer \(1\) has \(h_1=1\) and the other \(V\) layers have \(h_t=2\), so
\[
\begin{aligned}
W(\mathcal N^n)={}&\bigl(1+\alpha^{-1}n^{-1}\bigr)\\
&\cdot\bigl(1+\alpha^{-1}n^{-2}\bigr)^{k-1},
\end{aligned}
\]
which is close to \(1\). The last lesson shows that the sum over all \(2^n\) words is at most \(e^{3\sqrt n}\).

## 8. Exercises

**8.1.** Let \(n=12\), \(s=2\), \(k=5\), \(m=7\). Compute \(l_1,\dots,l_5\) and write down the division of the layers.

**8.2.** Check (3.1) for one variable: \(\partial_z\) and the multiplication by \(z\) on the polynomials in \(z\) with the orthonormal basis \(z^j/\sqrt{j!}\). Show that the multiplication by \(z\) is the adjoint of \(\partial_z\).

**8.3.** Let \(M\) be uniformly distributed among the compositions of \(t=2\) into \(r=2\) parts. Compute \(\mathbb EM_1\), \(\mathbb EM_1M_2\) and \(\mathbb E(M_1)_2\) directly and with Lemma 4.1, and compare with the geometric variables of Lemma 4.2.

**8.4.** Give an example of a linear map \(F\) with \(\operatorname{rank}F=2\) and \(T^2/T_2\) as close to \(1\) as you like.

**8.5.** For \(n=3\) and the word \(\tau=\mathcal N\mathcal D\mathcal N\), describe the \(\tau\)-admissible quadruples and count them. Which of them are compatible with the type word \(\tau\)?

## 9. Solutions

**8.1.** \(\lfloor2i/5\rfloor\) for \(i=0,\dots,5\) is \(0,0,0,1,1,2\). So \(l=(1,1,2,1,2)\), with the sum \(7\), and the division is \(VU\,VU\,VUU\,VU\,VUU\).

**8.2.** \(\partial_z\tfrac{z^j}{\sqrt{j!}}=\tfrac{j\,z^{j-1}}{\sqrt{j!}}=\sqrt j\,\tfrac{z^{j-1}}{\sqrt{(j-1)!}}\) and \(z\cdot\tfrac{z^j}{\sqrt{j!}}=\sqrt{j+1}\,\tfrac{z^{j+1}}{\sqrt{(j+1)!}}\). The matrix of \(\partial_z\) has the entry \(\sqrt j\) at (row \(j-1\), column \(j\)), the matrix of the multiplication has the entry \(\sqrt{j+1}\) at (row \(j+1\), column \(j\)), that is \(\sqrt j\) at (row \(j\), column \(j-1\)). The two matrices are transposes of each other and real.

**8.3.** The compositions are \((2,0),(1,1),(0,2)\). \(\mathbb EM_1=1\), \(\mathbb EM_1M_2=\tfrac13\), \(\mathbb E(M_1)_2=\tfrac23\). Lemma 4.1: \(\tfrac{(2)_1}2=1\); \(\tfrac{(2)_2}{2\cdot3}\cdot1=\tfrac13\); \(\tfrac{(2)_2}{2\cdot3}\cdot2!=\tfrac23\). Geometric variables with the mean \(G=1\): \(1\), \(1\) and \(2\). The means for the composition are smaller, by the factors \(1\), \(\tfrac13\), \(\tfrac13\), which are \(\prod_{j<h}\tfrac{1-j/2}{1+j/2}\) for \(h=1,2,2\).

**8.4.** The diagonal matrix with the entries \(1\) and \(\varepsilon\): \(T=1+\varepsilon^2\), \(T_2=1+\varepsilon^4\), and \(T^2/T_2\to1\) for \(\varepsilon\to0\).

**8.5.** The inner positions are \(1\) and \(2\), and both are switches. So the four paths agree at the positions \(1\) and \(2\): all four paths are equal, and there are \(n^2=9\) admissible quadruples, in agreement with \(n^{2\cdot2-2}\). In the layer \(2\) the paths \(P\) and \(Q\) have the same coordinate, so none of the quadruples has the type \(\mathcal D\) there; none is compatible with the type word \(\tau\). Their type word is \(\mathcal N\mathcal N\mathcal N\). The relaxation counts them for \(\tau\) as well, with the weight \(\beta\) or \(\alpha^{-1}\) of the middle layer.

## References

- [OpenAI-D] OpenAI, *Homogeneous depth-five lower bounds for iterated matrix multiplication*, OpenAI Math Release preprint, 25 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026
