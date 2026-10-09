# Affine approximation and quasi-state spaces

*GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Public domain (CC0 1.0).*

A self-adjoint element of a C*-algebra is determined by its values on positive functionals. Those values form a continuous affine function on a compact convex space. Passing to the bidual allows bounded affine functions that need not be continuous. This distinction gives a way to describe intermediate classes of operators by semicontinuity.

We prove the convex approximation results needed for that description. They work in a Hausdorff locally convex real vector space, with no metrizability or separability assumption. We then identify the continuous and bounded affine functions on the quasi-state space of an arbitrary C*-algebra. A nonunital example shows why its state space alone would lose compactness.

The separation theorem needed below is proved in the next subsection. We use compactness of the dual unit ball and the [complete compact-face proof of Krein–Milman](../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#OA-FND-WT-06), Lemma 1.1, stated there for every Hausdorff locally convex space. The bidual and its positive normal functionals are supplied by [The universal enveloping von Neumann algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-03), Theorem 3.3. For the norm-additive Jordan decomposition of a hermitian functional, we use the full proof in [Polar decomposition and absolute value of functionals](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-03), Corollary 2.8, applied to the predual of the bidual. Positivity and state norming are covered by [Representations and positive functionals](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html). The Hahn–Banach proof below uses only the well-ordering theorem from the earlier programme; the strict separation proof works directly with continuous seminorms. Both apply without countability assumptions.

## Convex separation in the topology being used

**Lemma 0.1 (Algebraic Hahn–Banach).** Let \(V\) be a real vector space, \(D\subset V\) a subspace, and \(p:V\to\mathbb R\) sublinear. Every linear \(g:D\to\mathbb R\) satisfying \(g\leq p\) extends to a linear functional on \(V\) still dominated by \(p\).

**Proof.** Sublinearity means \(p(u+v)\leq p(u)+p(v)\) and \(p(tv)=tp(v)\) for \(t\geq0\); in particular \(p(0)=0\). We begin with a construction that applies to any dominated linear functional \(h:S\to\mathbb R\) on a subspace \(S\). Define
\[
q_h(v)=\inf_{s\in S}\bigl(p(v+s)-h(s)\bigr)
\quad(v\in V).
\]
This is finite: sublinearity and domination give
\[
h(s)\leq p(s)\leq p(v+s)+p(-v),
\qquad
-p(-v)\leq q_h(v)\leq p(v),
\]
where the upper bound uses \(s=0\). For \(t>0\), substituting \(s=tu\) in the infimum gives \(q_h(tv)=tq_h(v)\). Also \(q_h(0)=0\) by the displayed bounds. To check subadditivity, choose \(s,u\in S\) making the two values in the infima at \(v,w\) within \(\varepsilon\) of their respective infima. Then
\[
\begin{aligned}
q_h(v+w)
&\leq p(v+w+s+u)-h(s+u)\\
&\leq p(v+s)-h(s)+p(w+u)-h(u)\\
&<q_h(v)+q_h(w)+2\varepsilon.
\end{aligned}
\]
Let \(\varepsilon\) decrease to zero. Thus \(q_h\) is sublinear. Changing the variable of the infimum by an element \(s_0\in S\) also gives the exact translation identity
\[
q_h(v+s_0)=q_h(v)+h(s_0).
\]

If \(v\notin S\), then \(0=q_h(0)\leq q_h(v)+q_h(-v)\). Choose
\[
\beta=\tfrac12\bigl(q_h(v)-q_h(-v)\bigr),
\qquad -q_h(-v)\leq\beta\leq q_h(v),
\]
and define \(h_1(s+tv)=h(s)+t\beta\) on \(S+\mathbb Rv\). The decomposition is unique, so \(h_1\) is well defined and linear. If \(t>0\), positive homogeneity and the translation identity yield
\[
h_1(s+tv)\leq h(s)+tq_h(v)=q_h(s+tv)\leq p(s+tv).
\]
If \(t<0\), the lower bound on \(\beta\) instead gives
\[
t\beta\leq(-t)q_h(-v),
\qquad
h_1(s+tv)\leq h(s)+(-t)q_h(-v)=q_h(s+tv)\leq p(s+tv).
\]
At \(t=0\), domination is the assumption on \(h\). This constructs a dominated extension to one larger subspace.

Well-order the underlying set of \(V\), using Theorem 8.5 of Hahn–Banach, Baire and the basic theorems on Banach spaces. Starting with \(g\) on \(D\), proceed along that well-order. At each successor step retain the current functional if the next vector already belongs to its domain; otherwise adjoin that vector by the construction above. At a limit step take the union of the preceding functionals. Their domains are nested subspaces and their values agree, so the union is well defined. Any two vectors in the union occur together in an earlier domain; hence the union is linear, and domination holds there for each vector. Transfinite recursion therefore gives a dominated extension whose domain contains every vector of \(V\). It is the required functional. \(\square\)

**Lemma 0.2 (Strict convex separation).** Let \(E\) be a Hausdorff locally convex real vector space. If \(C\subset E\) is nonempty compact convex and \(D\subset E\) is nonempty closed convex, with \(C\cap D=\varnothing\), then there are a continuous real linear functional \(\ell\) and \(d\in\mathbb R\) such that
\[
\ell(c)<d<\ell(y)
\quad(c\in C,\ y\in D).
\]

**Proof.** In a locally convex space, neighborhoods are described by finitely many continuous seminorm inequalities, as in Section 6 of Hahn–Banach, Baire and the basic theorems on Banach spaces. Because \(D\) is closed and misses \(c\in C\), choose a continuous seminorm \(q_c\) with
\[
c+\{x:q_c(x)<2\}\subseteq E\setminus D.
\]
Such a seminorm is obtained by rescaling and taking the maximum of the finitely many seminorms defining a neighborhood of \(c\) disjoint from \(D\). The smaller neighborhoods \(c+\{q_c<1\}\) cover \(C\). Choose a finite subcover with centers \(c_1,\ldots,c_m\) and seminorms \(q_1,\ldots,q_m\), and put \(q=\max_i q_i\). This is a continuous seminorm.

If \(c\in C\), choose \(i\) with \(q_i(c-c_i)<1\). Every \(y\in D\) satisfies \(q_i(y-c_i)\geq2\), so
\[
q(y-c)\geq q_i(y-c)
\geq q_i(y-c_i)-q_i(c-c_i)>1.
\]
Consequently the nonempty convex set \(F=D-C\) satisfies \(q(f)\geq1\) for all \(f\in F\).

Construct a real-valued function on all of \(E\) by
\[
b(x)=\inf_{t\geq0,\ f\in F}\bigl(q(x+tf)-t\bigr).
\]
For every candidate in this infimum, the seminorm inequality gives
\[
q(x+tf)-t\geq tq(f)-q(x)-t\geq-q(x).
\]
Taking \(t=0\) gives the upper bound. Thus
\[
-q(x)\leq b(x)\leq q(x),\qquad b(0)=0.
\]
For \(\lambda>0\), replacing \(t\) by \(\lambda t\) in the infimum proves \(b(\lambda x)=\lambda b(x)\). For subadditivity, take candidates \((t,f)\) at \(x\) and \((s,g)\) at \(z\). If \(t+s>0\), convexity puts \((tf+sg)/(t+s)\) in \(F\), and hence
\[
\begin{aligned}
b(x+z)
&\leq q(x+z+tf+sg)-(t+s)\\
&\leq \bigl(q(x+tf)-t\bigr)+\bigl(q(z+sg)-s\bigr).
\end{aligned}
\]
When \(t=s=0\), the same inequality follows by using \(t=0\) in the definition of \(b(x+z)\) and the triangle inequality for \(q\). Choose each candidate within \(\varepsilon\) of its finite infimum and let \(\varepsilon\) decrease to zero. This proves \(b(x+z)\leq b(x)+b(z)\), so \(b\) is sublinear.

Apply Lemma 0.1 to the zero functional on \(\{0\}\), dominated by \(b\). Its extension \(\ell:E\to\mathbb R\) satisfies \(\ell(x)\leq b(x)\leq q(x)\). Applying this inequality to \(-x\) shows \(|\ell(x)|\leq q(x)\), so \(\ell\) is continuous. For \(f\in F\), the candidate \(t=1\) with that same \(f\) shows \(b(-f)\leq-1\). Therefore
\[
\ell(f)=-\ell(-f)\geq1,
\qquad
\ell(y)-\ell(c)\geq1
\quad(y\in D,\ c\in C).
\]
Continuity and compactness give \(M=\max_{c\in C}\ell(c)\), attained at a point \(c_0\in C\). Every \(y\in D\) then satisfies \(\ell(y)\geq\ell(c_0)+1=M+1\). Taking \(d=M+1/2\) gives \(\ell(c)\leq M<d<\ell(y)\) for all the required points. \(\square\)

## 1. Supporting affine functions

Let \(E\) be a Hausdorff locally convex real vector space and \(K\subset E\) a nonempty compact convex set. Write \(\operatorname{Aff}(K;E)\) for the restrictions to \(K\) of continuous real affine functions on \(E\). Such a function on \(E\) has the form
\[
g(x)=\ell(x)+c,\qquad \ell\in E',\quad c\in\mathbb R.
\]
Here \(E'\) is the continuous real dual. A finite real function \(f\) on \(K\) is lower semicontinuous when \(\{x:f(x)>r\}\) is relatively open for every real \(r\). It is convex when
\[
f(tx+(1-t)y)\le t f(x)+(1-t)f(y),
\qquad 0\le t\le1.
\]
It is affine when this inequality is always an equality.

**Theorem 1.1 — affine supports.** If \(f:K\to\mathbb R\) is lower semicontinuous and convex, then
\[
f(x)=\sup\{g(x):g\in\operatorname{Aff}(K;E),\ g\le f\text{ on }K\}.
\tag{1.1}
\]
The same supremum is obtained by requiring \(g<f\) everywhere on \(K\).

**Proof.** The epigraph
\[
M=\{(y,t)\in E\times\mathbb R:y\in K,\ t\ge f(y)\}
\]
is closed and convex. Closedness uses both lower semicontinuity and the fact that compact \(K\) is closed in \(E\).

Fix \(x\in K\) and \(b<f(x)\). Geometric Hahn–Banach separates the point \((x,b)\) strictly from \(M\). Thus some continuous \(\ell\in E'\), scalar \(c\), and real \(d\) satisfy
\[
\ell(x)+cb<d<\ell(y)+ct
\quad((y,t)\in M).
\tag{1.2}
\]
The arbitrarily large vertical coordinates in \(M\) force \(c\ge0\). If \(c=0\), taking \(y=x\) contradicts (1.2). Hence \(c>0\). Set
\[
g(y)=\frac{d-\ell(y)}{c}.
\]
Taking \(t=f(y)\) in (1.2) gives \(g(y)<f(y)\) for every \(y\in K\), while its left inequality gives \(g(x)>b\). Since \(b\) can approach \(f(x)\) from below, (1.1) follows. \(\square\)

**Theorem 1.2 — increasing approximation.** If \(f\) is lower semicontinuous and affine on \(K\), there is an increasing net \((g_i)\) in \(\operatorname{Aff}(K;E)\) such that
\[
g_i<f\text{ on }K,\qquad g_i(x)\uparrow f(x)\quad(x\in K).
\tag{1.3}
\]

**Proof.** Let \(I\) be the family of continuous ambient affine functions strictly below \(f\) on \(K\), ordered by their restrictions. Theorem 1.1 gives the desired pointwise supremum. We must prove that \(I\) is directed.

Take \(g_1,g_2\in I\). After adding a common constant to these functions and to \(f\), assume \(g_1,g_2>0\) on \(K\). Put
\[
C_j=\{(y,t):y\in K,\ 0\le t\le g_j(y)\},\qquad j=1,2.
\]
Each \(C_j\) is compact and convex. Their convex hull \(C\) is compact: it is the image of \([0,1]\times C_1\times C_2\) under the continuous convex-combination map.

Every point of \(C\) has vertical coordinate strictly below \(f\) at its horizontal coordinate. Indeed, if
\((y,t)=s(y_1,t_1)+(1-s)(y_2,t_2)\), then affinity gives
\[
t\le s g_1(y_1)+(1-s)g_2(y_2)
<s f(y_1)+(1-s)f(y_2)=f(y),
\]
with the same strict conclusion at the endpoints. Thus \(C\) is disjoint from the closed convex epigraph \(M\).

Strict separation of a compact convex set from a disjoint closed convex set gives \(\ell,c,d\) with
\[
\ell(y)+ct<d\quad((y,t)\in C),\qquad
d<\ell(y)+ct\quad((y,t)\in M).
\]
Comparing \((y,g_j(y))\in C\) with \((y,f(y))\in M\) shows \(c>0\). Consequently \(g=(d-\ell)/c\) satisfies
\[
g_1,g_2<g<f\quad\text{on }K.
\]
Undo the common translation. Hence \(I\) is directed, and the net indexed by \(I\) proves (1.3). \(\square\)

**Corollary 1.3 — uniform approximation of continuous affine functions.** If \(f\) is continuous and affine on \(K\), an increasing sequence in \(\operatorname{Aff}(K;E)\) converges uniformly to \(f\).

**Proof.** For \(\varepsilon>0\), the open sets
\[
\{x:g_i(x)>f(x)-\varepsilon\},\qquad i\in I,
\]
cover \(K\). A finite subcover and directedness give one \(g_i\) with
\(0<f-g_i<\varepsilon\) everywhere. Choose such functions for \(\varepsilon=1/n\), and recursively choose an upper bound in \(I\) of the previous function and the newly chosen one. The resulting increasing sequence converges uniformly. This argument does not require that \(K\) be metrizable. \(\square\)

**Proposition 1.4 — an extreme minimizer.** A lower semicontinuous affine real function on \(K\) takes its minimum at an extreme point of \(K\).

**Proof.** Lower semicontinuity and compactness give a finite minimum \(m\) and a nonempty compact minimizer set
\[
F_m=\{x\in K:f(x)=m\}.
\]
It is convex. If \(tx+(1-t)y\in F_m\) with \(0<t<1\), affinity and \(f\ge m\) force \(f(x)=f(y)=m\). Thus \(F_m\) is a face of \(K\). By Krein–Milman it has an extreme point, and every extreme point of a face is extreme in \(K\). \(\square\)

## 2. Approximation on a split face

A convex subset \(F\) of \(K\) is a face if a nontrivial convex combination in \(F\) has both endpoints in \(F\). Faces \(F,G\) are complementary split faces when every \(x\in K\) has a decomposition
\[
x=\lambda y+(1-\lambda)z,
\qquad y\in F,\quad z\in G,\quad 0\le\lambda\le1,
\tag{2.1}
\]
with unique weight and unique components having nonzero weights. Unused components at the endpoints are immaterial. The weight function
\(e(x)=\lambda\) is affine: combining two decompositions and normalizing the resulting \(F\) and \(G\) components proves this by uniqueness. It satisfies \(e|_F=1\) and \(e|_G=0\).

Assume \(e\) is lower semicontinuous. Then \(G=\{e=0\}\) is closed; \(F\) need not be closed.

**Theorem 2.1 — supports along the face.** Let \(a:K\to\mathbb R\) be bounded and affine, with \(a|_F\) lower semicontinuous in the relative topology of \(F\). There is a net \((b_i)\) in \(\operatorname{Aff}(K;E)\) such that
\[
b_i\le a\text{ on }K,\qquad b_i(y)\longrightarrow a(y)\quad(y\in F).
\tag{2.2}
\]
The net is not asserted to be increasing.

**Proof.** Let \(M\) be the closure of the epigraph of \(a\) in \(E\times\mathbb R\). It is closed and convex. We first show that if \(y\in F\) and \((y,t)\in M\), then \(t\ge a(y)\).

Choose \((x_j,t_j)\to(y,t)\) with \(t_j\ge a(x_j)\), and decompose \(x_j\) as in (2.1). Lower semicontinuity of \(e\) gives
\[
1=e(y)\le\liminf_j e(x_j)\le1,
\]
so \(\lambda_j\to1\). Eventually \(\lambda_j>0\). The corresponding \(F\) components \(y_j\) converge to \(y\):
\[
y_j-x_j=(1-\lambda_j)(y_j-z_j)\longrightarrow0,
\]
because the compact set \(K-K\) is bounded in every continuous seminorm. Boundedness of \(a\) also gives
\[
a(x_j)-a(y_j)=(1-\lambda_j)(a(z_j)-a(y_j))\longrightarrow0.
\]
Lower semicontinuity on \(F\) therefore yields
\(a(y)\le\liminf_j a(x_j)\le t\).

Now fix a nonempty finite set \(B\subset F\) and \(\varepsilon>0\). Let \(L\) be the compact convex hull of
\[
\{(y,a(y)-\varepsilon):y\in B\}.
\]
Affinity says every point of \(L\) is of the form \((y,a(y)-\varepsilon)\) with \(y\in F\). The preceding paragraph shows \(L\cap M=\varnothing\).

Separate \(L\) and \(M\) strictly. The coefficient of the vertical coordinate is positive, since \((y,a(y)-\varepsilon)\in L\) and \((y,a(y))\in M\). The separating hyperplane is thus the graph of a continuous ambient affine function \(b_{B,\varepsilon}\) satisfying
\[
b_{B,\varepsilon}\le a\text{ on }K,\qquad
a(y)-\varepsilon<b_{B,\varepsilon}(y)\quad(y\in B).
\]
Order the pairs \((B,\varepsilon)\) by inclusion of \(B\) and decreasing \(\varepsilon\). These bounds prove (2.2). \(\square\)

**Corollary 2.2 — a singleton complement.** Suppose \(G=\{x_0\}\), \(a(x_0)=0\), and the other hypotheses of Theorem 2.1 hold. There are continuous ambient affine \(c_i\) with \(c_i(x_0)=0\) and scalars \(\alpha_i\le0\) such that
\[
c_i+\alpha_i e\le a\text{ on }K,
\qquad (c_i+\alpha_i e)(x)\longrightarrow a(x)\quad(x\in K).
\tag{2.3}
\]

**Proof.** Take \(b_i\) from Theorem 2.1 and put
\(\alpha_i=b_i(x_0)\le a(x_0)=0\), \(c_i=b_i-\alpha_i\).
On \(F\), \(c_i+\alpha_i e=b_i\le a\). At \(x_0\) it is zero. Both functions in this inequality are affine, so the inequality extends to every decomposition (2.1). Pointwise convergence follows in the same way from convergence on \(F\) and equality at \(x_0\). \(\square\)

## 3. The compact space of positive functionals

Let \(A\) be a C*-algebra, possibly nonunital. Write \(A_{\mathrm{sa}}\) for its self-adjoint real Banach space and \(A^*_{\mathrm{sa}}\) for the hermitian functionals. Define
\[
Q(A)=\{\varphi\in A^*_+:\|\varphi\|\le1\},
\qquad S(A)=\{\varphi\in A^*_+:\|\varphi\|=1\}.
\tag{3.1}
\]
Give \(Q(A)\) the weak* topology inherited from \(A^*\). It is compact and convex: the dual unit ball is compact, and positivity is the closed condition \(\varphi(a^*a)\ge0\) for all \(a\in A\). It lies in the locally convex real space
\[
E=(A^*_{\mathrm{sa}},\sigma(A^*_{\mathrm{sa}},A_{\mathrm{sa}})).
\]
The continuous real linear functionals on \(E\) are exactly evaluations at elements of \(A_{\mathrm{sa}}\). Indeed, continuity at zero bounds such a functional in terms of finitely many evaluations; it vanishes on their common kernel, so it factors through their finite-dimensional range and is a real linear combination of them.

For \(a\in A_{\mathrm{sa}}\), write
\[
\widehat a(\varphi)=\varphi(a).
\]
State norming gives
\[
\|a\|=\sup_{\varphi\in Q(A)}|\widehat a(\varphi)|.
\tag{3.2}
\]

**Theorem 3.1 — continuous affine functions.** Evaluation is an isometric real linear bijection
\[
A_{\mathrm{sa}}\ \longrightarrow\
\{f\in C(Q(A),\mathbb R): f\text{ affine},\ f(0)=0\}.
\tag{3.3}
\]

**Proof.** Only surjectivity remains. Corollary 1.3 uniformly approximates \(f\) by restrictions of continuous ambient affine functions, hence by functions
\[
f_n(\varphi)=\varphi(a_n)+c_n,
\qquad a_n\in A_{\mathrm{sa}}.
\]
Since \(f(0)=0\), uniform convergence gives \(c_n=f_n(0)\to0\). Thus \(\widehat a_n=f_n-c_n\) converges uniformly to \(f\). Formula (3.2) makes \((a_n)\) a norm Cauchy sequence. Its limit \(a\in A_{\mathrm{sa}}\) satisfies \(\widehat a=f\). \(\square\)

**Theorem 3.2 — bounded affine functions.** Evaluation is an isometric real linear bijection
\[
A^{**}_{\mathrm{sa}}\ \longrightarrow\
\{f:Q(A)\to\mathbb R:f\text{ bounded and affine},\ f(0)=0\}.
\tag{3.4}
\]
The evaluation pairing here is between \(A^{**}\) and its predual \(A^*\).

**Proof.** Evaluation gives a bounded affine function vanishing at zero. Positive normal functionals norm self-adjoint elements of \(A^{**}\), so it is isometric.

Conversely, put \(C=\sup_{Q(A)}|f|\). For \(\varphi\in A^*_+\setminus\{0\}\), define
\[
L(\varphi)=\|\varphi\| f\left(\frac{\varphi}{\|\varphi\|}\right),
\qquad L(0)=0.
\tag{3.5}
\]
Affinity with \(f(0)=0\) makes this agree with \(f\) on \(Q(A)\). It is positively homogeneous. The norm of positive functionals is additive. Hence, for positive nonzero \(\varphi,\psi\), applying affinity to
\[
\frac{\varphi+\psi}{\|\varphi\|+\|\psi\|}
=\frac{\|\varphi\|}{\|\varphi\|+\|\psi\|}
 \frac{\varphi}{\|\varphi\|}
+\frac{\|\psi\|}{\|\varphi\|+\|\psi\|}
 \frac{\psi}{\|\psi\|}
\]
proves \(L(\varphi+\psi)=L(\varphi)+L(\psi)\).

Every hermitian functional is a difference of positive ones. Set
\(L(\varphi-\psi)=L(\varphi)-L(\psi)\). This is well-defined: two such expressions imply \(\varphi+\psi'=\varphi'+\psi\), and additivity on the positive cone gives the same difference. It is real linear. The norm-additive Jordan decomposition gives
\[
|L(h)|\le C(\|h_+\|+\|h_-\|)=C\|h\|
\quad(h\in A^*_{\mathrm{sa}}).
\]
Complexify this bounded real functional. Since every \(\varphi\in A^*\) has the unique decomposition \(\varphi=h+ik\) with hermitian \(h,k\), and \(\|h\|,\|k\|\le\|\varphi\|\), the extension is bounded, with bound \(2C\). It therefore defines \(x\in A^{**}\). Its real values on hermitian functionals mean \(x=x^*\). By construction \(\widehat x=f\); the already established isometry gives \(\|x\|=C\). \(\square\)

In particular, a bounded affine function vanishing at zero corresponds to an element of \(A\) exactly when it is continuous on \(Q(A)\).

## 4. States, zero, and the bidual identity

For \(A\ne\{0\}\), the faces \(S(A)\) and \(\{0\}\) are complementary split faces of \(Q(A)\). Every nonzero \(\varphi\in Q(A)\) has the unique decomposition
\[
\varphi=\|\varphi\|\frac{\varphi}{\|\varphi\|}
+(1-\|\varphi\|)0.
\tag{4.1}
\]
Positivity makes \(\{0\}\) a face. The norm is affine on positive functionals and at most one on \(Q(A)\), so \(S(A)\) is also a face. Its split weight is
\[
e(\varphi)=\|\varphi\|=\widehat1(\varphi),
\tag{4.2}
\]
where \(1\) is the identity of \(A^{**}\). The norm is weak* lower semicontinuous; alternatively,
\(e(\varphi)=\sup_i\varphi(u_i)\) for a positive contractive approximate identity of \(A\). Thus Corollary 2.2 applies.

The extreme points of \(Q(A)\) are zero and the pure states. A nonzero functional of norm strictly less than one has the nontrivial decomposition (4.1). A state is extreme in \(Q(A)\) exactly when it is extreme in \(S(A)\), because any convex decomposition of a norm-one positive functional into elements of \(Q(A)\) has both endpoint norms equal to one. Consequently Proposition 1.4 says that any lower semicontinuous affine function on \(Q(A)\) has an extreme minimizer among zero and the pure states. If its value is negative somewhere and its value at zero is zero, a pure state attains a negative minimum.

**Example 4.1 — the identity seen through a nonunital algebra.** For \(A=c_0(\mathbb N)\),
\[
A^*=\ell^1(\mathbb N),\qquad A^{**}=\ell^\infty(\mathbb N),
\qquad Q(A)=\left\{p_n\ge0:\sum_n p_n\le1\right\}.
\]
Evaluation at \(1\in\ell^\infty\) is \(e(p)=\sum_n p_n\). The point masses \(\delta_n\) converge weak* to zero, since each element of \(c_0\) vanishes at infinity. Yet \(e(\delta_n)=1\) and \(e(0)=0\). Thus \(e\) is lower semicontinuous and affine, but not continuous; it corresponds to the bidual identity, which is outside \(c_0\). The state face is not closed. The finite sums \(\sum_{n=1}^N p_n\) are continuous affine functions increasing pointwise to \(e\).

## 5. Graded exercises with solutions

**Exercise 5.1 — introductory: an affine matrix observable.** Identify \(Q(M_2(\mathbb C))\) with positive matrices \(d\) satisfying \(\operatorname{Tr}(d)\le1\), via \(\varphi_d(a)=\operatorname{Tr}(da)\). For \(h=\operatorname{diag}(-2,3)\), compute the supremum of \(|\varphi_d(h)|\), its minimum, and one extreme minimizer. Determine the split weight and explain why it is continuous in this example.

**Solution.** In the eigenbasis of \(h\),
\[
\varphi_d(h)=-2d_{11}+3d_{22},\qquad
d_{11},d_{22}\ge0,\quad d_{11}+d_{22}\le1.
\]
Its range is \([-2,3]\): the inequalities follow from the trace bound, and the endpoints are attained at the two rank-one coordinate projections. The supremum of the absolute value is \(3=\|h\|\), and the minimum is \(-2\), attained by the pure state with density \(\operatorname{diag}(1,0)\). The split weight is \(\operatorname{Tr}(d)=\varphi_d(1_2)\), a continuous affine evaluation because the identity belongs to \(M_2\). Thus its state face is closed here.

**Exercise 5.2 — intermediate: pointwise approximation without uniform approximation.** In Example 4.1 let \(u_N\in c_0\) be the indicator of \(\{1,\dots,N\}\). Show that \(\widehat u_N\uparrow e\) pointwise, but
\[
\sup_{p\in Q(c_0)}|e(p)-\widehat u_N(p)|=1
\quad\text{for every }N.
\]
Apply Corollary 2.2 to \(a(p)=\sum_n p_n\) and explicitly give suitable \(c_N,\alpha_N\). Explain why \(e\) cannot be uniformly approximated by continuous affine functions on \(Q(c_0)\).

**Solution.** For each fixed \(p\in\ell^1_+\), its partial sums increase to its total sum. The difference is the tail mass, at most one, and \(p=\delta_{N+1}\) makes it one. Take
\[
c_N=\widehat u_N,\qquad \alpha_N=0.
\]
They vanish at zero, lie below \(a=e\), and converge pointwise on the whole quasi-state space. A uniform limit of continuous functions on a topological space is continuous, whereas \(e(\delta_n)=1\) along the weak* convergent sequence \(\delta_n\to0\). Hence no uniform continuous approximation exists. Theorem 3.2 identifies \(e\) with \(1\in\ell^\infty\); Theorem 3.1 correctly excludes it from \(c_0\).

**Exercise 5.3 — advanced: why convexity does not give directed supports.** On \(Q(M_2)\), put \(h=\operatorname{diag}(1,-1)\) and
\[
f(\varphi)=|\varphi(h)|,\qquad
g_+(\varphi)=\varphi(h)-\tfrac14,\qquad
g_-(\varphi)=-\varphi(h)-\tfrac14.
\]
Show that \(f\) is continuous and convex, and that \(g_+,g_-<f\) everywhere. Prove that there is no affine \(g\) with \(g\ge g_+,g_-\) and \(g\le f\). Relate this to Theorems 1.1 and 1.2.

**Solution.** Absolute value is continuous and convex, so its composition with the real continuous linear evaluation has those properties. For every real \(t\), \(t-1/4<|t|\) and \(-t-1/4<|t|\), proving both strict inequalities.

Let \(\varphi_+\) and \(\varphi_-\) be the coordinate pure states. Their \(h\) values are \(1\) and \(-1\). An affine common majorant would satisfy
\[
g(\varphi_+)\ge\tfrac34,\qquad g(\varphi_-)\ge\tfrac34,
\]
and hence \(g((\varphi_++\varphi_-)/2)\ge3/4\). But \(f\) is zero at that midpoint. This contradicts \(g\le f\). Thus affine minorants still give the pointwise supremum in Theorem 1.1, but they cannot be organized as the increasing family of Theorem 1.2. Affinity of \(f\) is essential for that directedness assertion.

## References

[Erdman] John M. Erdman, [*Functional Analysis and Operator Algebras: An Introduction*](https://web.pdx.edu/~erdman/FAOA/functional_analysis_operator_algebras_pdf.pdf), 2015, Chapter 5, “The Hahn–Banach Theorems,” Theorem HBTI. Further reading on dominated extension.
