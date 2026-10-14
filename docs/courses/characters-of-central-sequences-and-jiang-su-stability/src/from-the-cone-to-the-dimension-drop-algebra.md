# From the cone to the dimension-drop algebra

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lesson [A full cone in a tensor power](a-full-cone-in-a-tensor-power.md) produced a unital homomorphism \(\eta\) from the matrix cone
\[
C=\{f\in C([0,1],M_2):f(0)\in\mathbb C1\}
\]
into a tensor power \(P\) of \(D\) whose first matrix corner \(\eta(\iota e_{11})\) is full. This lesson builds, in a further tensor power of \(P\), an orthogonal pair of exactly equivalent positive elements whose defect lies below the first element cut at \(1/2\) (Proposition 3.1). The Rørdam–Winter criterion of [The Rørdam–Winter criterion](the-rordam-winter-criterion.md) then gives a unital homomorphism from \(I(2,3)\), and the finite theorem follows (Section 4).

- Tensor powers of the cone as functions on a cube (Lemma 1.1).
- A simplex of matrix embeddings (Lemma 2.1).
- From a full cone to the criterion (Proposition 3.1).
- Proof of the finite theorem (Section 4).

The lesson follows [OpenAI-KRC, Sections 5 and 6]. All tensor products of C\*-algebras are maximal. \(M_2^{\otimes k}\) is the matrix algebra \(M_{2^k}\), with Kronecker products; the Kronecker products of the matrix units of \(M_2\) are the matrix units of \(M_{2^k}\). For subspaces \(E_i\subseteq M_2\), \(E_1\otimes\cdots\otimes E_k\subseteq M_2^{\otimes k}\) is the span of the products \(x_1\otimes\cdots\otimes x_k\), \(x_i\in E_i\). Here \(\iota(t)=t\), and Cuntz comparison is that of [Cuntz comparison and order-zero maps](cuntz-comparison-and-order-zero-maps.md), Lemma 1.2.

## 1. Tensor powers of the cone

For \(s\in[0,1]\) let \(E(s)=M_2\) if \(s>0\) and \(E(0)=\mathbb C1\). For \(k\ge1\) let
\[
\begin{aligned}
\mathcal C_k=\{f\in{}&C([0,1]^k,M_2^{\otimes k}):\\
&f(t)\in E(t_1)\otimes\cdots\otimes E(t_k)\\
&\text{for all }t\}.
\end{aligned}
\]
It is a C\*-subalgebra of \(C([0,1]^k,M_2^{\otimes k})\), since each \(E(t_1)\otimes\cdots\otimes E(t_k)\) is a C\*-subalgebra of \(M_2^{\otimes k}\).

**Lemma 1.1** (the cube; [OpenAI-KRC, Lemma 5.1]). There is a \(*\)-isomorphism \(\Gamma\colon C^{\otimes k}\to\mathcal C_k\) with
\[
\begin{aligned}
&\Gamma(F_1\otimes\cdots\otimes F_k)(t)\\
&\quad=F_1(t_1)\otimes\cdots\otimes F_k(t_k).
\end{aligned}
\]

*Proof.* *The homomorphism.* For \(i=1,\dots,k\), the formula \(\theta_i(F)(t)=1\otimes\cdots\otimes F(t_i)\otimes\cdots\otimes1\), with \(F(t_i)\) in position \(i\), defines unital \(*\)-homomorphisms \(\theta_i\colon C\to C([0,1]^k,M_2^{\otimes k})\) with commuting ranges. By the universal property ([Central sequences and the character criterion](central-sequences-and-the-character-criterion.md), Lemma 3.1(1)) they define a unital \(*\)-homomorphism \(\Gamma\) with the displayed formula. It maps elementary tensors, and hence everything, into the closed subalgebra \(\mathcal C_k\).

*Injectivity.* Let \(\pi\) be an irreducible representation of \(C^{\otimes k}\) on \(H\), and \(\pi_1,\dots,\pi_k\) its restrictions to the legs, unital with commuting ranges. The element \(\iota1\) is central in \(C\), so \(\pi_i(\iota1)\) commutes with \(\pi(C^{\otimes k})\) and is a scalar \(\tau_i\in[0,1]\) by Schur's lemma. Then \(\pi_i(g1)=g(\tau_i)\) for \(g\in C([0,1])\), by the functional calculus. If \(F\in C\) and \(F(\tau_i)=0\), put \(g_n(t)=\min\{1,n|t-\tau_i|\}\); then \(\|F-Fg_n\|\to0\) and \(\pi_i(Fg_n)=\pi_i(F)g_n(\tau_i)=0\), so \(\pi_i(F)=0\). Hence \(\pi_i(F)=\rho_i(F(\tau_i))\) for a unital \(*\)-homomorphism \(\rho_i\colon E(\tau_i)\to B(H)\); it is well defined because evaluation at \(\tau_i\) maps \(C\) onto \(E(\tau_i)\). The \(\rho_i\) have commuting ranges, so
\[
\rho(x_1\otimes\cdots\otimes x_k)=\rho_1(x_1)\cdots\rho_k(x_k)
\]
defines a \(*\)-homomorphism \(\rho\) on the finite-dimensional C\*-algebra \(E(\tau_1)\otimes\cdots\otimes E(\tau_k)\), a matrix algebra; it is contractive. On elementary tensors, \(\pi(x)=\rho(\Gamma(x)(\tau))\); by linearity and continuity this holds on \(C^{\otimes k}\). So \(\|\pi(x)\|\le\|\Gamma(x)\|\). As the norm of \(x\) is the supremum of \(\|\pi(x)\|\) over irreducible representations ([Building representations from positive functionals](course:foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark), Theorem 8.5), \(\|x\|\le\|\Gamma(x)\|\), and \(\Gamma\) is injective.

*Surjectivity.* The range of \(\Gamma\) is closed ([Order, local units and quotients of C\*-algebras](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones), Corollary 15.4). It contains the scalar functions \(g_1(t_1)\cdots g_k(t_k)1=\Gamma(g_11\otimes\cdots\otimes g_k1)\), whose span is dense in \(C([0,1]^k)\) by the Stone–Weierstrass theorem; so it contains \(g1\) for every \(g\in C([0,1]^k)\). Choose the basis \(b_0=1\), \(b_1=e_{12}\), \(b_2=e_{21}\), \(b_3=e_{11}-e_{22}\) of \(M_2\), and for \(\alpha\in\{0,1,2,3\}^k\) let \(b_\alpha=b_{\alpha_1}\otimes\cdots\otimes b_{\alpha_k}\). These form a basis of \(M_2^{\otimes k}\), and \(E(t_1)\otimes\cdots\otimes E(t_k)\) is spanned by the \(b_\alpha\) with \(\alpha_i=0\) whenever \(t_i=0\). Write \(f\in\mathcal C_k\) as \(f(t)=\sum_\alpha f_\alpha(t)b_\alpha\) with continuous scalar \(f_\alpha\). With \(S_\alpha=\{i:\alpha_i\ne0\}\) and \(p_\alpha(t)=\prod_{i\in S_\alpha}t_i\) (empty product \(1\)), the condition on \(f\) says that \(f_\alpha=0\) on the zero set of \(p_\alpha\). Then
\[
f_\alpha\,\frac{p_\alpha}{p_\alpha+\varepsilon}\longrightarrow f_\alpha\quad\text{uniformly as }\varepsilon\downarrow0 :
\]
given \(\eta>0\), the compact set \(\{|f_\alpha|\ge\eta\}\) misses the zero set of \(p_\alpha\), so \(p_\alpha\ge\kappa>0\) on it for some \(\kappa\), and the difference is at most \(\|f_\alpha\|\varepsilon/\kappa\) there and less than \(\eta\) elsewhere. Now
\[
f_\alpha\frac{p_\alpha}{p_\alpha+\varepsilon}\,b_\alpha=\Bigl(\frac{f_\alpha}{p_\alpha+\varepsilon}1\Bigr)\cdot p_\alpha b_\alpha ,
\]
where the first factor is a scalar function, and \(p_\alpha b_\alpha=\Gamma(F_1\otimes\cdots\otimes F_k)\) with \(F_i=\iota b_{\alpha_i}\) for \(i\in S_\alpha\) and \(F_i=1\) otherwise. So each \(f_\alpha b_\alpha\), and hence \(f\), lies in the range of \(\Gamma\). \(\blacksquare\)

The injectivity argument uses no nuclearity of \(C\): every irreducible representation of \(C^{\otimes k}\) factors through evaluation at a point of the cube.

## 2. A simplex of matrix embeddings

Let \(\Delta_{k-1}=\{r\in[0,1]^k:\sum_ir_i=1\}\). For \(r\in\Delta_{k-1}\) let \(E^r_i=M_2\) if \(r_i>0\) and \(E^r_i=\mathbb C1\) if \(r_i=0\).

**Lemma 2.1** (matrix simplex; [OpenAI-KRC, Lemma 5.2]). For every \(k\ge1\) there are unital \(*\)-homomorphisms \(\theta_r\colon M_2\to M_2^{\otimes k}\), \(r\in\Delta_{k-1}\), such that:

1. \(r\mapsto\theta_r(a)\) is continuous for every \(a\in M_2\);
2. \(\theta_r(M_2)\subseteq E^r_1\otimes\cdots\otimes E^r_k\);
3. at the \(j\)-th vertex of \(\Delta_{k-1}\), \(\theta_r(a)=1\otimes\cdots\otimes a\otimes\cdots\otimes1\), with \(a\) in position \(j\).

*Proof.* Let \(S\in M_2\otimes M_2\) be the flip, so \(S(a\otimes1)S=1\otimes a\), and
\[
\begin{gathered}
U(s)=\tfrac12(1+S)+e^{i\pi s}\tfrac12(1-S),\\
0\le s\le1,
\end{gathered}
\]
a continuous path of unitaries with \(U(0)=1\) and \(U(1)=S\). We argue by induction on \(k\); for \(k=1\), \(\theta\) is the identity. Let \(k\ge2\). For \(r_k<1\), let \(\tau\colon M_2\to M_2^{\otimes(k-1)}\) be the map given by induction for the point \((r_1,\dots,r_{k-1})/(1-r_k)\) of \(\Delta_{k-2}\), and put
\[
\theta_r(a)=(\tau\otimes\mathrm{id})\bigl(U(r_k)(a\otimes1)U(r_k)^*\bigr);
\]
for \(r_k=1\), put \(\theta_r(a)=1^{\otimes(k-1)}\otimes a\). Here \(\tau\otimes\mathrm{id}\colon M_2\otimes M_2\to M_2^{\otimes(k-1)}\otimes M_2\) is a unital \(*\)-homomorphism, so each \(\theta_r\) is one.

(1) As \(M_2\) is finite-dimensional, continuity of \(r\mapsto\tau_r(a)\) for each \(a\) gives continuity of \(r\mapsto\tau_r\) in operator norm, and likewise for \(\tau_r\otimes\mathrm{id}\) on \(M_2\otimes M_2\). So \(\theta_r(a)\) is continuous where \(r_k<1\). Near \(r_k=1\), since \(\tau\otimes\mathrm{id}\) is contractive and maps \(S(a\otimes1)S=1\otimes a\) to \(1^{\otimes(k-1)}\otimes a\), with \(U=U(r_k)\),
\[
\begin{aligned}
&\bigl\|\theta_r(a)-1^{\otimes(k-1)}\otimes a\bigr\|\\
&\quad\le\bigl\|U(a\otimes1)U^*-S(a\otimes1)S\bigr\|\\
&\quad\le2\|a\|\,\|U-S\| ,
\end{aligned}
\]
which tends to \(0\) as \(r_k\to1\), whatever the preceding weights do.

(2) If \(r_k=0\), then \(U(0)=1\) and \(\theta_r(a)=\tau(a)\otimes1\). If \(r_i=0\) for some \(i<k\), the \(i\)-th factor is scalar throughout the range of \(\tau\), by induction, and \(\tau\otimes\mathrm{id}\) keeps it scalar. If \(r_k=1\), all \(r_i\) with \(i<k\) vanish, and \(\theta_r(a)=1^{\otimes(k-1)}\otimes a\).

(3) At the \(k\)-th vertex this is the definition. At the \(j\)-th vertex with \(j<k\), \(r_k=0\) and \(\theta_r(a)=\tau(a)\otimes1\), with \(\tau\) at the \(j\)-th vertex of \(\Delta_{k-2}\). \(\blacksquare\)

## 3. From a full cone to the criterion

**Proposition 3.1** ([OpenAI-KRC, Proposition 5.3]). Let \(P\) be a nonzero unital C\*-algebra and \(\eta\colon C\to P\) a unital \(*\)-homomorphism such that \(\eta(\iota e_{11})\) is full. Then for some \(m\ge1\) the tensor power \(B=P^{\otimes m}\) contains orthogonal positive contractions \(b_1,b_2\) and an element \(v_B\) with
\[
\begin{gathered}
b_1=v_B^*v_B,\qquad b_2=v_Bv_B^*,\\
1_B-b_1-b_2\precsim(b_1-1/2)_+ .
\end{gathered}
\]
Consequently there is a unital \(*\)-homomorphism \(I(2,3)\to P^{\otimes m}\).

*Proof.* *Step 1: a full cut and a comparison constant.* Put \(b=\eta(\iota e_{11})\). By fullness ([A full cone in a tensor power](a-full-cone-in-a-tensor-power.md), Lemma 1.1) there are \(h_i,l_i\in P\), \(1\le i\le N\), with \(\|1-\sum_ih_ibl_i\|<1/2\). Choose \(0<\delta<1\) so small that \(\delta\sum_i\|h_i\|\|l_i\|<1/2\), and put
\[
\begin{gathered}
c=(b-\delta)_+=\eta(q),\\
q=(\iota-\delta)_+e_{11}\in C .
\end{gathered}
\]
As \(\|b-c\|\le\delta\), the element \(S=\sum_ih_icl_i\) satisfies \(\|1-S\|<1\) and is invertible. With the row \(T=(h_1c^{1/2},\dots,h_Nc^{1/2})\), the column \(Z=(c^{1/2}l_1,\dots,c^{1/2}l_N)^{\mathrm T}\) and \(d=Z^*Z=\sum_il_i^*cl_i\), we have \(S=TZ\), so
\[
S^*S=Z^*T^*TZ\le\|T\|^2d .
\]
Since \(S^*S\) is invertible and positive, so is \(d\). The column \(V=(l_1d^{-1/2},\dots,l_Nd^{-1/2})^{\mathrm T}\) satisfies
\[
V^*\operatorname{diag}(c,\dots,c)V=d^{-1/2}dd^{-1/2}=1_P,
\]
so that
\[
[1_P]\le N[c]. \tag{3.1}
\]

*Step 2: an auxiliary tensor power.* Put \(c_1=c\) and \(c_2=\eta((\iota-\delta)_+e_{22})\), and \(\nu=\eta\bigl((\iota-\delta)_+^{1/2}e_{21}\bigr)\). Then \(\nu^*\nu=c_1\), \(\nu\nu^*=c_2\), \(c_1c_2=0\), and \(c_1+c_2=\eta((\iota-\delta)_+1)\) is a positive contraction. Choose \(L\ge1\) with \(2^L\ge N\), and put
\[
R=P^{\otimes L},\qquad e=c^{\otimes L},\qquad k=N^L .
\]
For \(\sigma\in\{1,2\}^L\) let \(c_\sigma=c_{\sigma_1}\otimes\cdots\otimes c_{\sigma_L}\). With \(u_l=c^{1/2}\) if \(\sigma_l=1\) and \(u_l=\nu\) if \(\sigma_l=2\), the element \(w_\sigma=u_1\otimes\cdots\otimes u_L\) has \(w_\sigma^*w_\sigma=e\) and \(w_\sigma w_\sigma^*=c_\sigma\), so \([c_\sigma]=[e]\). The \(2^L\) elements \(c_\sigma\) are pairwise orthogonal, since two of them differ in a position where \(c_1c_2=0\). Hence, by Lemma 1.2(3) and (5) of the Cuntz lesson, and by dropping summands,
\[
N[e]\le2^L[e]=\Bigl[\sum_\sigma c_\sigma\Bigr]\le[1_R].
\]
Tensoring (3.1) \(L\) times gives \(1_R=W^*\operatorname{diag}(e,\dots,e)W\) with the column \(W=V^{\otimes L}\) of length \(N^L\). Together:
\[
N[e]\le[1_R]\le k[e]. \tag{3.2}
\]

*Step 3: an orthogonal pair in the cube.* Work in \(\mathcal C_k\cong C^{\otimes k}\) (Lemma 1.1), with scalar functions read as multiples of \(1\). Put
\[
\begin{gathered}
g(s)=(1-2s/\delta)_+,\\
H(t)=1-\prod_{j=1}^kg(t_j).
\end{gathered}
\]
Then \(0\le H\le1\) and \(H(0)=0\). For \(t\ne0\) let \(d(t)=\max_jt_j\) and
\[
r_i(t)=\frac{(t_i/d(t)-1/2)_+}{\sum_{j=1}^k(t_j/d(t)-1/2)_+} .
\]
The denominator is at least \(1/2\), so \(r\colon[0,1]^k\setminus\{0\}\to\Delta_{k-1}\) is continuous. With \(\theta_r\) from Lemma 2.1, define for \(t\ne0\)
\[
\begin{gathered}
a_i(t)=H(t)\,\theta_{r(t)}(e_{ii})\quad(i=1,2),\\
v(t)=H(t)^{1/2}\,\theta_{r(t)}(e_{21}),
\end{gathered}
\]
and \(a_1(0)=a_2(0)=v(0)=0\). As \(\|a_i(t)\|\le H(t)\) and \(\|v(t)\|\le H(t)^{1/2}\), these functions are continuous. If \(t\ne0\) and \(t_j=0\), then \(r_j(t)=0\), and the \(j\)-th factor of their values is scalar by Lemma 2.1(2). So \(a_1,a_2,v\in\mathcal C_k\), and pointwise
\[
\begin{gathered}
v^*v=a_1,\quad vv^*=a_2,\\
a_1a_2=0,\\
a_1+a_2=H1 .
\end{gathered} \tag{3.3}
\]
So \(a_1,a_2\) are orthogonal positive contractions, and their defect is \(X=1-a_1-a_2=\prod_jg(t_j)1\), that is, \(X=\Gamma(g1\otimes\cdots\otimes g1)\).

For \(1\le j\le k\) put
\[
y_j=\Gamma\bigl((g1)^{\otimes(j-1)}\otimes q\otimes(g1)^{\otimes(k-j)}\bigr).
\]
The \(y_j\) are positive and pairwise orthogonal, because \(qg=0\): \(q\) vanishes on \([0,\delta]\) and \(g\) on \([\delta/2,1]\). Moreover
\[
a_1y_j=y_j\qquad(1\le j\le k). \tag{3.4}
\]
Indeed, where \(y_j(t)\ne0\), \(t_j>\delta\) and \(t_i<\delta/2\) for \(i\ne j\). Then \(d(t)=t_j\), \(t_i/d(t)<1/2\) for \(i\ne j\), so \(r(t)\) is the \(j\)-th vertex, and \(H(t)=1\) since \(g(t_j)=0\). By Lemma 2.1(3), \(a_1(t)\) is \(e_{11}\) in position \(j\) and \(1\) elsewhere, which acts as the identity on \(y_j(t)\), whose \(j\)-th factor is a multiple of \(e_{11}\). Where \(y_j(t)=0\), (3.4) is trivial.

Apply the unital \(*\)-homomorphism \(\eta^{\otimes k}\colon C^{\otimes k}\to P^{\otimes k}\) (Lemma 3.1(4) of the first lesson), and keep the names \(a_1,a_2,v,X,y_j\) for the images; (3.3) and (3.4) persist. Put \(Y=\sum_jy_j\) and \(G=\eta(g1)\). Then \(X=G^{\otimes k}\) and \(y_j=G^{\otimes(j-1)}\otimes c\otimes G^{\otimes(k-j)}\). By (3.1), \([G]\le[1_P]\le N[c]\). Tensoring with \(G\) in the other \(k-1\) positions (Lemma 1.2(4) of the Cuntz lesson, on both sides) gives \([X]\le N[y_j]\) for each \(j\). Adding these \(k\) comparisons and using \(\sum_j[y_j]=[Y]\) (orthogonality),
\[
k[X]\le N[Y]. \tag{3.5}
\]

*Step 4: absorbing the defect.* Let \(B=P^{\otimes k}\otimes R=P^{\otimes(k+L)}\), \(b_i=a_i\otimes1_R\) and \(v_B=v\otimes1_R\). By (3.4), \(a_1Y=Y\), and taking adjoints \(Ya_1=Y\); so \(a_1\) commutes with \(Y\) and acts as the identity on \(Y^{1/2}\), and \((a_1-1/2)_+Y^{1/2}=\frac12Y^{1/2}\). With \(z=(2Y)^{1/2}\otimes1_R\),
\[
z^*(b_1-1/2)_+z=Y\otimes1_R .
\]
Now, in matrices over \(B\),
\[
\begin{aligned}
[X\otimes1_R]&\le k[X\otimes e]\\
&\le N[Y\otimes e]\\
&\le[Y\otimes1_R]\\
&\le[(b_1-1/2)_+] .
\end{aligned}
\]
The first comparison tensors \([1_R]\le k[e]\) from (3.2) with \(X\) on the left, the second tensors (3.5) with \(e\) on the right, the third tensors \(N[e]\le[1_R]\) with \(Y\) on the left, and the last is the exact witness \(z\). Witnesses in matrices compress to witnesses in \(B\) (Lemma 1.2(1) of the Cuntz lesson), so
\[
\begin{aligned}
1_B-b_1-b_2&=X\otimes1_R\\
&\precsim(b_1-1/2)_+\quad\text{in }B .
\end{aligned}
\]
By (3.3), \(b_1,b_2\) are orthogonal positive contractions with \(b_1=v_B^*v_B\) and \(b_2=v_Bv_B^*\). Proposition 1.1 of [The Rørdam–Winter criterion](the-rordam-winter-criterion.md), with \(\varepsilon=1/2\), gives a unital \(*\)-homomorphism \(I(2,3)\to B\). Take \(m=k+L\). \(\blacksquare\)

The integers play different roles: \(N\) is the comparison constant from fullness, \(k=N^L\) the number of cube coordinates, and the auxiliary power \(R\) removes the unequal multiplicities \(k\) and \(N\) in (3.5) without any cancellation in the Cuntz order. This use of a tensor factor with \(N[e]\le[1_R]\le k[e]\) follows Robert and Rørdam [RR, Lemma 6.1(i)].

## 4. Proof of the finite theorem

*Proof of Theorem 2.2 of [Central sequences and the character criterion](central-sequences-and-the-character-criterion.md).* Let \(D\) be a nonzero unital C\*-algebra without characters. Proposition 3.1 of [A full cone in a tensor power](a-full-cone-in-a-tensor-power.md) gives \(m_0\ge1\) and a unital \(*\)-homomorphism \(\eta\colon C\to P=D^{\otimes m_0}\) with \(\eta(\iota e_{11})\) full. Proposition 3.1 above gives a unital \(*\)-homomorphism \(I(2,3)\to P^{\otimes m}\), and regrouping (Lemma 3.1(3) of the first lesson) identifies \(P^{\otimes m}\) with \(D^{\otimes m_0m}\). \(\blacksquare\)

Theorem 2.1 and Corollary 2.3 of the first lesson follow from the finite theorem and the two named hypotheses (KR) and (DT), by Section 5 there.

## 5. Exercises

**5.1.** For \(k=2\), which values can \(f(t)\) take for \(f\in\mathcal C_2\) at \(t=(0,1/2)\) and at \(t=(0,0)\)?

**5.2.** For \(k=2\) and \(r=(1/2,1/2)\), show that \(\theta_r(a)=\frac12(a\otimes1+1\otimes a)+\frac i2[a\otimes1,S]\).

**5.3.** Let \(R\) be a unital C\*-algebra with a positive \(e\) such that \(N[e]\le[1_R]\le k[e]\). Show that \(k[x]\le N[y]\) for positive \(x,y\) over a unital \(A\) implies \([x\otimes1_R]\le[y\otimes1_R]\) over \(A\otimes R\).

**5.4.** Where does the proof of Proposition 3.1 use that \(\eta(\iota e_{11})\) is full, and where that \(\delta\) is small?

**5.5.** Check (3.4) directly for \(k=2\) at the point \(t=(2\delta,0)\), assuming \(2\delta\le1\).

## 6. Solutions

**5.1.** At \((0,1/2)\), \(f(t)\in\mathbb C1\otimes M_2\); at \((0,0)\), \(f(t)\in\mathbb C1\).

**5.2.** For \(k=2\), \(\tau\) is the identity and \(\theta_r(a)=U(a\otimes1)U^*\) with \(U=\frac12\bigl((1+i)1+(1-i)S\bigr)\). Expanding, using \(S^2=1\) and \(S(a\otimes1)S=1\otimes a\), gives
\[
\begin{aligned}
\tfrac14\bigl(&2(a\otimes1)+2(1\otimes a)\\
&+2i(a\otimes1)S-2iS(a\otimes1)\bigr).
\end{aligned}
\]

**5.3.** \([x\otimes1_R]\le k[x\otimes e]\), then \(k[x\otimes e]\le N[y\otimes e]\), then \(N[y\otimes e]\le[y\otimes1_R]\), tensoring \([1_R]\le k[e]\) with \(x\), then \(k[x]\le N[y]\) with \(e\), then \(N[e]\le[1_R]\) with \(y\).

**5.4.** Fullness gives the elements \(h_i,l_i\) and hence the comparison \([1_P]\le N[c]\) of (3.1). Small \(\delta\) keeps \(S\) invertible after \(b\) is replaced by its cut \(c\), which vanishes near \(t=0\); this vanishing makes \(c\) orthogonal to \(g\) and puts \(c\) where the cube construction has \(a_1=1\).

**5.5.** At \(t=(2\delta,0)\), \(d(t)=2\delta\), \(r(t)=(1,0)\), \(H(t)=1-g(2\delta)g(0)=1\), \(a_1(t)=e_{11}\otimes1\), and \(y_1(t)=\delta e_{11}\otimes1\), since \(q(2\delta)=\delta e_{11}\) and \(g(0)=1\). So \(a_1(t)y_1(t)=y_1(t)\), while \(y_2(t)=g(2\delta)1\otimes q(0)=0\).

## References

- [OpenAI-KRC] OpenAI, *The Kirchberg–Rørdam character criterion*, OpenAI Math Release preprint, 25 September 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026
- [RR] L. Robert and M. Rørdam, *Divisibility properties for C\*-algebras*, arXiv:1106.5523v2, Lemma 6.1. https://arxiv.org/abs/1106.5523
