# The heavy list and the two decoders

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A labeling that satisfies the test of the game with a probability of at least \(\varepsilon\) leads, by the lesson on two accepted levels, to an inequality: on an event \(J\), the upper value of the answer of the right player at the lower level \(i\) is the vector \(Mz_0+\hat y^*\) more often than a fixed fraction of the time. This lesson turns the inequality into two procedures, the *decoders*. The left decoder sees the functions on the original questions; the right decoder sees the functions on the projected questions and one bit less of the array at \(D_i\). Each outputs a bilinear form, and the two forms agree on the projected space with a probability that depends only on \(\varepsilon\) and on the number of rows at the upper level.

The two sides are connected through a part \(X\) of the upper matrix that neither decoder sees. Its law is known on the right side and has a small bias. A computation with characters shows that the prediction \(X\mapsto Xz'+k_0\) must correlate with one of a short list of characters, and the list can be computed on the right side without the knowledge of \(z_0\).

- The hidden part of the upper matrix, its law and the function \(G\) (Lemma 1.1).
- The list of heavy characters (Lemma 2.1).
- The two decoders (Proposition 3.1).

The lesson follows [OpenAI-G, Sections 5.3 to 5.5]. It continues [Two accepted levels and the upper response](two-accepted-levels-and-the-upper-response.md) and uses its notation: the levels \(i<j\), the law \(\mathbb P_i\), \(H=H_{D_j}(E)\), \(K=K_j\), \(\ell=\ell_j\), \(M=M_{D_j}\), the background \(\Gamma\), the advice with the row map \(A\), the witness \(q_b,t_b,t_*\), the functionals \(z_0+Z\), the events \(I\subset J\), the vector \(\mathsf R\), and the numbers \(\kappa,\alpha,r,h_0,g_0,\rho,b_0\). The bias bound is Proposition 5.1 of [Changing the law of the tests](changing-the-law-of-the-tests.md).

## 1. The hidden part of the upper matrix

Work under \(\mathbb P_i\). Let
\[
\begin{gathered}
H'=H_{D_j}(O),\\
H_i=H_{D_i}(E),\qquad H_i'=H_{D_i}(O),
\end{gathered}
\]
and \(S=M_{D_i}\). The spaces with a prime are subspaces of those without, and products are preserved. Let \(W\subset K\) be the kernel of the row map \(A:K\to\mathbb F^r\); its codimension is at most \(r\). Split the upper matrix by its buckets:
\[
\begin{aligned}
M&=M_{\mathrm{kn}}+X,\\
M_{\mathrm{kn}}&=\sum_{v\notin W}v\otimes h_v,\\
X&=\sum_{v\in W\setminus\{0\}}v\otimes h_v .
\end{aligned}
\]
Under \(\mathbb P_i\) the buckets lie in \(H'\), so \(X\in W\otimes H'\), and \(AM=AM_{\mathrm{kn}}\). We read \(X\) also as the linear map \((H')^*\to W\), \(q\mapsto Xq=\sum_vq(h_v)\,v\).

**The data of the two sides.**

- The *left data* \(\mathcal D_L\): the family \(E\), the path to \(D_i\), the map \(A\), the arrays at all nodes other than \(D_j\), and the buckets \(h_v\) with \(v\notin W\); all functions are given on \(\Omega(E)\).
- The *right data* \(\mathcal D_R\): the family \(O\), the path to \(D_i\), the map \(A\), the vector \(a_i\), the arrays at all nodes other than \(D_j\) and \(D_i\), the class of \(S\) modulo \(a_i\), and the buckets \(h_v\) with \(v\notin W\); all functions are given on \(\Omega(O)\).

The left data contain neither \(a_i\) nor the marks, the family \(O\) or the edges chosen at the marked leaves. The right data contain no function on \(\Omega(E)\) and only the class of \(S\) modulo \(a_i\). Neither contains \(X\). The left data determine the background \(\Gamma\) and \(A\bar M=\pi(AM_{\mathrm{kn}})\), hence whether the advice \((\Gamma,A,A\bar M)\) is good, and for a good advice the witness, \(Z\) and \(z_0\).

**The function \(G\).** For given right data and \(X\in W\otimes H'\), take the array family on \(O\) with \(M_{\mathrm{kn}}+X\) at \(D_j\), the arrays of the right data at the other nodes, and at \(D_i\) any array in the given class modulo \(a_i\). The function \(\Theta_{D_i,a_i}\circ\Psi_{O,\mathbf M}\) does not depend on the choice at \(D_i\). Let
\[
G(X)\in K
\]
be the component at \(D_j\) of the restored value of the label that the labeling gives at the right key of this function. This defines a function \(G:W\otimes H'\to K\) for all \(X\), computed from the right data and the labeling.

**Lemma 1.1.** Let \(\mathcal D\) consist of \(E\), the marks, \(O\) with the edges chosen at the marked leaves, the path to \(D_i\), \(A\), \(a_i\), the arrays at all nodes other than \(D_j\), and the buckets \(h_v\) with \(v\notin W\). Under \(\mathbb P_i\):

1. given \(\mathcal D\), the buckets \(h_v\), \(v\in W\setminus\{0\}\), are independent calls at \(D_j\); the conditional law \(\mu\) of \(X\) depends only on \(O\), the path to \(D_i\) and \(W\), so it is computed from the right data;
2. if \(R_k\ge6\) for all \(k\) and \((\tfrac78)^{R_j}\le\lambda\), every nonzero linear functional on \(W\otimes H'\) has a bias of at most \(\lambda\) under \(\mu\);
3. \(\mathsf R=G(X)\).

**Proof.** (1) By the rule for the calls under \(\mathbb P_i\) (Section 2 of the lesson on two accepted levels), given \(E\), the marks, \(O\) and the path, the buckets of \(M\) are independent calls, and they are independent of the arrays at the other nodes; \(A\) and \(a_i\) are independent of everything. A call at \(D_j\) is formed from uniform functions at children off the path, whose spaces are the same for \(E\) and \(O\), from products, and from uniform functions in \(H_i'\); so its law depends only on \(O\) and the path. (2) This is the last statement of Proposition 5.1 of the lesson on changing the law. (3) The constraint of \((E,\mathbf M,D_i,a_i)\) has the right key of \(\Theta_{D_i,a_i}\circ\Psi_{E,\mathbf M}\), which by Lemma 4.3 of the lesson on the tree of function spaces is the right key of the same function on \(O\), with the same restored values. \(\blacksquare\)

So \(\mathcal D\) contains the data of both sides, and still the law of \(X\) given \(\mathcal D\) is the law \(\mu\) that the right side can compute.

## 2. The list of heavy characters

This section is linear algebra and counting over \(\mathbb F\); it does not use the game. Let \(K=\mathbb F^\ell\), let \(W\subset K\) be a subspace of codimension at most \(r\), let \(H'\) be a vector space and \(V=W\otimes H'\). An element \(X\in V\) is also a linear map \((H')^*\to W\). The dual space is \(V^*=W^*\otimes(H')^*\): for \(\omega\in W^*\) and \(z\in(H')^*\),
\[
(\omega\otimes z)(X)=\omega(Xz).
\]
For \(\Phi\in V^*\) and \(w\in W\) let \(\Phi(w)\in(H')^*\) be the functional \(x\mapsto\Phi(w\otimes x)\); then \((\omega\otimes z)(w)=\omega(w)\,z\). The *character* of \(\Phi\) is \(\chi_\Phi(X)=(-1)^{\Phi(X)}\).

**Lemma 2.1.** Let \(\mu\) be a law on \(V\) with \(|\mathbb E_\mu\chi_\Phi|\le\lambda\) for every nonzero \(\Phi\in V^*\). Let \(G:V\to K\) be a function, \(0<\rho\le1\),
\[
h_0=2^{-r\ell},\qquad\tau=\frac{\rho h_0}4,
\]
and assume
\[
2^{-(\ell-r)}<\frac\rho8,\qquad\lambda\le\min\Bigl\{\frac{h_0}2,\frac{\tau^2}2\Bigr\}.
\]
For \(\sigma\in K^*\) let \(g_\sigma(X)=(-1)^{\sigma(G(X))}\) and
\[
\mathcal H_\sigma=\bigl\{\Phi\in V^*:\ |\mathbb E_\mu(g_\sigma\chi_\Phi)|\ge\tau\bigr\}.
\]

1. Every list \(\mathcal H_\sigma\) has at most \(2/\tau^2\) elements.
2. Let \(Q\subset(H')^*\) be a subspace of dimension at most \(r\), \(t_Q:Q\to W\) a linear map, and \(\mathcal C\) the set of the \(X\in V\) with \(Xq=t_Q(q)\) for all \(q\in Q\). Then \(\mu(\mathcal C)\ge h_0/2\).
3. In addition let \(z'\in(H')^*\) and \(k_0\in K\) be such that
\[
\mathbb P_\mu\bigl(G(X)=Xz'+k_0\mid\mathcal C\bigr)\ge\rho .
\]
Then there are \(\sigma\in K^*\) with \(\sigma|_W\ne0\) and \(\Phi\in\mathcal H_\sigma\) with
\[
\Phi\in(\sigma|_W)\otimes z'+W^*\otimes Q .
\]
For every \(w\in W\) with \(\sigma(w)=1\), such a \(\Phi\) satisfies \(\Phi(w)\in z'+Q\).

The lists depend on \(\mu\), \(G\) and \(\tau\). They do not depend on \(Q\), \(t_Q\), \(z'\), \(k_0\).

**Proof.** (2) Let \(L=W^*\otimes Q\subset V^*\). It has at most \(2^{\ell r}=1/h_0\) elements. An element \(Y\in V\) satisfies \(\Psi(Y)=0\) for all \(\Psi\in L\) exactly if \(\omega(Yq)=0\) for all \(\omega\) and \(q\), that is, \(Yq=0\) for all \(q\in Q\). The set \(\mathcal C\) is not empty, because every linear map \(Q\to W\) extends to \((H')^*\). Fix \(X_0\in\mathcal C\). For every \(X\),
\[
\frac1{|L|}\sum_{\Psi\in L}\chi_\Psi(X_0)\,\chi_\Psi(X)=\mathbf 1_{\mathcal C}(X),
\]
because the left side is the mean of \((-1)^{\Psi(X-X_0)}\) over the subspace \(L\), which is \(1\) if all \(\Psi\in L\) vanish at \(X-X_0\) and \(0\) otherwise. Take the mean under \(\mu\). The term \(\Psi=0\) gives \(1/|L|\), and each of the others at most \(\lambda/|L|\) in absolute value. So
\[
\mu(\mathcal C)\ge\frac1{|L|}-\lambda\ge h_0-\lambda\ge\frac{h_0}2 .
\]

(3) For \(k\in K\), the mean of \((-1)^{\sigma(k)}\) over \(\sigma\in K^*\) is \(1\) if \(k=0\) and \(0\) otherwise. Apply this to \(k=G(X)+Xz'+k_0\), and note \(\sigma(Xz')=((\sigma|_W)\otimes z')(X)\):
\[
\begin{aligned}
&\mathbb P_\mu\bigl(G(X)=Xz'+k_0\mid\mathcal C\bigr)\\
&\quad=2^{-\ell}\sum_{\sigma\in K^*}(-1)^{\sigma(k_0)}\,e_\sigma,\\
&e_\sigma=\mathbb E_\mu\bigl(g_\sigma\,\chi_{(\sigma|_W)\otimes z'}\mid\mathcal C\bigr).
\end{aligned}
\]
Every \(|e_\sigma|\) is at most \(1\). The \(\sigma\) that vanish on \(W\) are a fraction \(2^{-\dim W}\le2^{-(\ell-r)}<\rho/8\) of all \(\sigma\). So the other \(\sigma\) contribute at least \(\rho-\rho/8\) to the mean, and one of them has \(|e_\sigma|\ge\tfrac78\rho\ge\tfrac12\rho\). Fix it. Multiply by \(\mu(\mathcal C)\ge h_0/2\) and insert the formula for \(\mathbf 1_{\mathcal C}\):
\[
\begin{aligned}
\tau&\le\bigl|\mathbb E_\mu\bigl(g_\sigma\,\chi_{(\sigma|_W)\otimes z'}\,\mathbf 1_{\mathcal C}\bigr)\bigr|\\
&\le\frac1{|L|}\sum_{\Psi\in L}\bigl|\mathbb E_\mu\bigl(g_\sigma\,\chi_{(\sigma|_W)\otimes z'+\Psi}\bigr)\bigr| .
\end{aligned}
\]
So one \(\Psi\in L\) has a term of at least \(\tau\), and \(\Phi=(\sigma|_W)\otimes z'+\Psi\) lies in \(\mathcal H_\sigma\). For \(w\in W\) with \(\sigma(w)=1\) we get \(\Phi(w)=z'+\Psi(w)\), and \(\Psi(w)\in Q\).

(1) Let \(\Phi_1,\dots,\Phi_m\) be different elements of \(\mathcal H_\sigma\), and choose signs \(s_a=\pm1\) such that \(s_a\,\mathbb E_\mu(g_\sigma\chi_{\Phi_a})\ge\tau\). By the inequality of Cauchy and Schwarz and \(g_\sigma^2=1\),
\[
\begin{aligned}
m^2\tau^2&\le\Bigl(\mathbb E_\mu\Bigl(g_\sigma\sum_as_a\chi_{\Phi_a}\Bigr)\Bigr)^2\\
&\le\mathbb E_\mu\Bigl(\sum_as_a\chi_{\Phi_a}\Bigr)^2\\
&=\sum_{a,a'}s_as_{a'}\,\mathbb E_\mu\chi_{\Phi_a+\Phi_{a'}}\\
&\le m+m^2\lambda .
\end{aligned}
\]
For \(a\ne a'\) the functional \(\Phi_a+\Phi_{a'}\) is not zero, which gives the bound \(\lambda\) for these terms. With \(\lambda\le\tau^2/2\) this is \(m^2\tau^2/2\le m\), so \(m\le2/\tau^2\). \(\blacksquare\)

The lemma does not say that \(\mu\) is close to the uniform law in total variation; it uses only the means of the characters under \(\mu\). The bound on the lists does not contain the dimension of \(V\).

## 3. The two decoders

**Proposition 3.1.** Assume (GE). Let the labeling satisfy the test with a probability of at least \(\varepsilon\), let \(d\varepsilon\ge4\), and let \(i<j\) be the levels of Lemma 1.1 of the lesson on two accepted levels. Let \(\ell=\ell_j\ge\ell_0\) with \(2^{-(\ell-r)}<\rho/8\), let \(\delta_{ij}\le\alpha g_0/16\), let \(\tau=\rho h_0/4\), let \(R_k\ge6\) for all \(k\), and
\[
\Bigl(\frac78\Bigr)^{R_j}\le\min\Bigl\{\frac{h_0}2,\frac{\tau^2}2\Bigr\} .
\]
Then there are a random bilinear form \(F_L\) on \(H_i\), computed from the left data and independent random choices, and a random bilinear form \(F_R\) on \(H_i'\), computed from the right data and independent random choices, such that
\[
\begin{gathered}
\mathbb P_i\bigl(F_R=F_L\text{ on }H_i'\times H_i'\bigr)\ \ge\ \gamma_j,\\
\gamma_j=b_0\cdot2^{-\ell}\cdot\frac{\tau^2}2\cdot2^{-r} .
\end{gathered}
\]
Every value of \(F_L\) has the form \(F_L(x,y)=z(xy)\) with a linear functional \(z\) on \(H\) with \(z(1)=1\), and the matrix \(\bigl(F_L(S_u,S_v)\bigr)_{u,v}\) of its values on the rows of \(S\) has a rank of at most one.

The number \(\gamma_j\) depends only on \(\varepsilon\) and \(\ell_j\). It does not depend on \(\ell_i\), on the numbers of children, on the formula, or on the numbers \(R_k\).

**The left decoder.** Compute \(\Gamma\) and \(A\bar M\) from the left data. If the advice \((\Gamma,A,A\bar M)\) is good, draw \(z\) uniformly in \(z_0+Z\). If it is not good, let \(z\) be the evaluation at a point of \(\Omega_{D_j}(E)\) chosen by a fixed rule. Output
\[
F_L(x,y)=z(xy)\qquad(x,y\in H_i).
\]
The products \(xy\) lie in \(H_i^2\subset H\), by Lemma 2.1 of the lesson on the tree of function spaces. In the first case \(z(1)=1\) and \(z(S_uS_v)=(y^*_{D_i})_u(y^*_{D_i})_v\), by Lemma 5.2 of the lesson on two accepted levels for the node \(D_i\in\mathcal N\). In the second case \(z(1)=1\) and \(z(S_uS_v)\) is the product of the values of \(S_u\) and \(S_v\) at the point. In both cases the matrix has a rank of at most one.

**The right decoder.** Compute from the right data the law \(\mu\) and the function \(G\) of Section 1, and the lists \(\mathcal H_\sigma\) of Lemma 2.1 for them. Draw \(\sigma\in K^*\) uniformly. If \(\sigma|_W\ne0\) and \(\mathcal H_\sigma\) is not empty, draw \(\Phi\) uniformly in \(\mathcal H_\sigma\), let \(w_\sigma\) be the first vector of \(W\), in a fixed order, with \(\sigma(w_\sigma)=1\), put \(z_R=\Phi(w_\sigma)\in(H')^*\), and output
\[
F_R(x,y)=z_R(xy)\qquad(x,y\in H_i').
\]
Here \((H_i')^2\subset H'\). In all other cases output \(F_R=0\).

The left decoder does not use \(a_i\), and the right decoder uses nothing from the left decoder: no witness, no \(z_0\).

**Proof of the agreement.** Let \(\mathcal D\) be as in Lemma 1.1. It determines the left data and the right data, hence goodness, the witness, \(Z\), \(z_0\), and \(M_{\mathrm{kn}}\). By Lemma 1.1 the law of \(X\) given \(\mathcal D\) is \(\mu\), with the bias bound \(\lambda=(\tfrac78)^{R_j}\), and \(\mathsf R=G(X)\).

*The slice.* Let the advice be good. Let \(q'_b\) be the restriction of \(q_b\) to \(H'\), let \(Q\subset(H')^*\) be the span of the \(q'_b\), and \(z'\) the restriction of \(z_0\). Since \(X\) has its buckets in \(H'\),
\[
\begin{gathered}
Mq_b=M_{\mathrm{kn}}q_b+Xq'_b,\\
Mz_0=M_{\mathrm{kn}}z_0+Xz' .
\end{gathered}
\]
So, given \(\mathcal D\), the event \(J\) is the event that \(X\) lies in the set \(\mathcal C_{\mathcal D}\) of the \(X\in W\otimes H'\) with \(Xq'_b=t_b-M_{\mathrm{kn}}q_b\) for all \(b\). If this set is not empty, one of its elements \(X_0\) defines the linear map \(t_Q(q)=X_0q\) on \(Q\), and \(\mathcal C_{\mathcal D}\) is the set \(\mathcal C\) of Lemma 2.1 for \(Q\) and \(t_Q\); the dimension of \(Q\) is at most \(m\le r\). The prediction of Proposition 6.1 of the lesson on two accepted levels is
\[
\begin{gathered}
Mz_0+\hat y^*=Xz'+k_0,\\
k_0=M_{\mathrm{kn}}z_0+\hat y^* .
\end{gathered}
\]

*Favourable data.* Let \(p(\mathcal D)=\mu(\mathcal C_{\mathcal D})\) if the advice is good, and \(0\) otherwise. If \(p(\mathcal D)>0\), let \(\varrho(\mathcal D)\) be the conditional probability under \(\mu\), given \(X\in\mathcal C_{\mathcal D}\), that \(G(X)=Xz'+k_0\); otherwise let \(\varrho(\mathcal D)=0\). Then
\[
\begin{aligned}
\mathbb P_i(J)&=\mathbb E_i\,p(\mathcal D),\\
\mathbb P_i\bigl(J,\ \mathsf R=Mz_0+\hat y^*\bigr)&=\mathbb E_i\,p(\mathcal D)\,\varrho(\mathcal D),
\end{aligned}
\]
and Proposition 6.1 of that lesson reads
\[
\mathbb E_i\bigl[p(\mathcal D)\,(\varrho(\mathcal D)-\rho)\bigr]\ge b_0 .
\]
The quantity in the brackets is at most \(1\), and it is positive only if the advice is good, \(p(\mathcal D)>0\) and \(\varrho(\mathcal D)>\rho\). Call such \(\mathcal D\) *favourable*. So \(\mathcal D\) is favourable with a probability of at least \(b_0\).

*The hit.* Let \(\mathcal D\) be favourable. Lemma 2.1 (3), for \(\mu\), \(G\), \(Q\), \(t_Q\), \(z'\), \(k_0\), gives \(\sigma\) with \(\sigma|_W\ne0\) and \(\Phi\in\mathcal H_\sigma\) with \(\Phi(w_\sigma)\in z'+Q\). The right decoder draws this \(\sigma\) with the probability \(2^{-\ell}\) and then this \(\Phi\) with a probability of at least \(\tau^2/2\), by Lemma 2.1 (1). Its output is then \(z_R=z'+q\) with some \(q\in Q\). The restriction to \(H'\) maps \(Z\) onto \(Q\), so it maps the uniform law on \(z_0+Z\) to the uniform law on \(z'+Q\). The choice of the left decoder is independent of the choices of the right decoder, so the restriction of \(z\) to \(H'\) is equal to \(z_R\) with the probability \(2^{-\dim Q}\ge2^{-r}\). If it is, then \(F_L(x,y)=z(xy)=z_R(xy)=F_R(x,y)\) for \(x,y\in H_i'\), because \(xy\in H'\). So, given a favourable \(\mathcal D\), the forms agree with a probability of at least \(2^{-\ell}\cdot\tfrac{\tau^2}2\cdot2^{-r}\). \(\blacksquare\)

The right decoder computes one family of lists from its own data. For different left data that are compatible with the same right data, different elements of the same lists can be the ones that lead to agreement. The bound was proved for each favourable \(\mathcal D\) separately, so no factor for the number of possible witnesses appears.

The decoders are fixed procedures. The right decoder always computes its lists with the law \(\mu\) of Lemma 1.1, also when it is run on inputs with another law.

**What is proved.** The left form \(F_L\) comes from a functional \(z\) on the big space \(H\). On the rows of \(S\) that the labeling sees at the node \(D_i\), its matrix has a rank of at most one: this is the trace of the fact that an answer at \(D_i\) is one vector \(y_{D_i}\). It is not proved here that \(F_L\) has a rank of at most one as a form on \(H_i\). [OpenAI-G] derives a statement of this kind from the agreement of \(F_L\) and \(F_R\) when the number \(\ell_i\) of rows at the lower level is large; this uses that \(\gamma_j\) does not depend on \(\ell_i\). That step is not part of this lesson.

## 4. Exercises

**4.1.** Let \(W=K=\mathbb F^2\), \(H'=\mathbb F\), so \(V=\mathbb F^2\), and let \(Q=(H')^*\), \(t_Q(q)=(1,0)\) for the nonzero \(q\). Write the set \(\mathcal C\), the space \(L\), and check the formula for \(\mathbf 1_{\mathcal C}\) at \(X=(1,0)\) and at \(X=(1,1)\).

**4.2.** Let \(\mu\) be the uniform law on \(V\). Show that every list \(\mathcal H_\sigma\) has at most \(1/\tau^2\) elements.

**4.3.** In Lemma 2.1 (3), why is it necessary to exclude the \(\sigma\) that vanish on \(W\)? What would the right decoder output for such a \(\sigma\)?

**4.4.** Show that the restriction of functionals to \(H'\) maps \(Z\) onto \(Q\), and that the image of the uniform law on \(z_0+Z\) is the uniform law on \(z'+Q\).

**4.5.** Compute \(\tau\) and \(\gamma_j/b_0\) in terms of \(\rho\), \(r\), \(\ell\).

## 5. Solutions

**4.1.** \(X\in V\) is a vector of \(\mathbb F^2\), and \(Xq=X\) for the nonzero \(q\). So \(\mathcal C=\{(1,0)\}\). \(L=W^*\otimes Q=V^*\) has four elements \(\Psi\), and \(X_0=(1,0)\). At \(X=(1,0)\) all four terms are \(\chi_\Psi(X_0)^2=1\), and the mean is \(1\). At \(X=(1,1)\) the terms are \((-1)^{\Psi(0,1)}\), which is \(1\) for two of the \(\Psi\) and \(-1\) for the other two; the mean is \(0\).

**4.2.** For the uniform law the characters are orthonormal, so \(\sum_\Phi(\mathbb E_\mu(g_\sigma\chi_\Phi))^2=\mathbb E_\mu g_\sigma^2=1\). At most \(1/\tau^2\) of the terms are at least \(\tau^2\). This is the case \(\lambda=0\), where the proof of the lemma gives \(m\tau^2\le1\).

**4.3.** If \(\sigma|_W=0\), then \((\sigma|_W)\otimes z'=0\): the character does not contain \(z'\), and there is no \(w\in W\) with \(\sigma(w)=1\), so \(z'\) cannot be recovered from \(\Phi\). The decoder outputs the form \(0\) for such a \(\sigma\). The assumption \(2^{-(\ell-r)}<\rho/8\) makes these \(\sigma\) too few to carry the correlation.

**4.4.** \(Z\) is spanned by the \(q_b\) and \(Q\) by their restrictions \(q'_b\), so the restriction, which is linear, maps \(Z\) onto \(Q\), and \(z_0+Z\) onto \(z'+Q\). A linear map onto a space has fibres of equal size, so the uniform law is mapped to the uniform law.

**4.5.** \(\tau=\rho\,2^{-r\ell-2}\), so \(\tau^2/2=\rho^2\,2^{-2r\ell-5}\). Multiplying by \(2^{-\ell}\) and \(2^{-r}\) gives \(\gamma_j/b_0=\rho^2\,2^{-2r\ell-\ell-r-5}\).

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026
