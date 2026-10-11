# Semifinite conjugations and vector supports

A conjugation can exchange an algebra with its commutant without selecting a positive cone. Its action on the center has a strong consequence: a vector and its conjugate have equivalent support projections in the algebra. We prove that assertion before introducing traces. In a semifinite algebra it gives an equality between the center-valued sizes of the two cyclic subspaces associated with a vector.

Throughout, \(M\subseteq B(H)\) is a unital von Neumann algebra and \(Z=M\cap M'\). Inner products are linear in the first variable. Neither the Hilbert dimension nor the algebra is assumed countable. For a set of vectors, brackets denote its closed linear span. Equivalence and subequivalence of projections are always taken in the algebra explicitly specified.

## Conjugations and the order of multiplication

An antiunitary involution \(J\) on \(H\) is a conjugate-linear map with
\[
 \begin{gathered}
 J^2=1,\\
 \langle J\xi,J\eta\rangle
   =\langle\eta,\xi\rangle.
 \end{gathered}
 \tag{SJ.1}
\]
We require in addition
\[
 \begin{gathered}
 JMJ=M',\\
 JaJ=a^*\quad(a\in Z).
 \end{gathered}
 \tag{SJ.2}
\]
These are the conjugation hypotheses in this lesson. They also give \(JM'J=M\). The isometry in (SJ.1) is essential; conjugate linearity and the equation \(J^2=1\) alone do not assert it.

There are two related maps on bounded operators:
\[
 \begin{gathered}
 \kappa(x)=JxJ,\\
 j(x)=Jx^*J.
 \end{gathered}
 \tag{SJ.3}
\]
The first is conjugate-linear and multiplicative. Indeed \(JxyJ=(JxJ)(JyJ)\), by inserting \(J^2=1\). The inner-product identity gives \(\kappa(x^*)=\kappa(x)^*\). Thus the second map is complex-linear and reverses products. Both preserve adjoints. In particular \(j:M\to M'\) is a linear star anti-isomorphism, whereas \(\kappa:M\to M'\) preserves the order of multiplication.

Writing a positive operator as a square shows that \(\kappa\) preserves positivity and order. Its inverse is itself, so it preserves any existing supremum of an ordered family of self-adjoint operators. It also preserves strong convergence: for each \(\xi\),
\[
 \|\kappa(x_i-x)\xi\|
   =\|(x_i-x)J\xi\|.
\]
It carries projections to projections and partial isometries to partial isometries, with their initial and final projections carried by the same map. Consequently it preserves equivalence and subequivalence while moving them from \(M\) to \(M'\), or conversely.

On the center, \(\kappa(a)=a^*\) and \(j(a)=a\). In particular, \(\kappa\) fixes central positive elements and central projections. For a central projection \(z\), we therefore have \(Jz=zJ\). No cone has been chosen in these hypotheses.

## The two supports of a vector

For \(\xi\in H\), let
\[
 \begin{gathered}
 e_\xi H=[M'\xi],\\
 e_\xi\in M,\\
 e'_\xi H=[M\xi],\\
 e'_\xi\in M'.
 \end{gathered}
 \tag{SJ.4}
\]
The membership assertions follow because each subspace reduces the algebra generating it, followed by the bicommutant theorem. These are the least projections in the respective algebras fixing \(\xi\): if \(p\in M\) fixes \(\xi\), then it fixes \(M'\xi\), and the converse is immediate. This is also the cyclic support construction.

The vector functional \(\omega_\xi(x)=\langle x\xi,\xi\rangle\) on \(M\) is normal and positive. Its support is \(e_\xi\): for a projection \(p\in M\),
\(\omega_\xi(1-p)=\|(1-p)\xi\|^2\), so vanishing is equivalent to \(p\xi=\xi\). The same argument on \(M'\) gives support \(e'_\xi\). Normality and the general functional support characterization are proved in CP07 and CP12.

Since \(J\) is an onto isometry and exchanges the two algebras,
\[
 \begin{gathered}
 J[M'\xi]=[MJ\xi],\\
 J[M\xi]=[M'J\xi].
 \end{gathered}
\]
For example \(Jx'\xi=(Jx'J)J\xi\), and every element of \(M\) arises as \(Jx'J\). Taking closures is legitimate because \(J\) is an isometry. Conjugating the orthogonal projections onto these spaces gives
\[
 \begin{gathered}
 Je_\xi J=e'_{J\xi},\\
 Je'_\xi J=e_{J\xi}.
 \end{gathered}
 \tag{SJ.5}
\]

For a central projection \(z\), the range of the projection \(z e_\xi\) is the closure of \(M'z\xi\). Hence
\[
 \begin{gathered}
 e_{z\xi}=ze_\xi,\\
 e'_{z\xi}=ze'_\xi,\\
 Jz\xi=zJ\xi.
 \end{gathered}
 \tag{SJ.6}
\]
This is the point at which the action of \(J\) on central projections will enter the comparison argument.

The corresponding identity for functionals is
\[
 \begin{gathered}
 \omega_{J\xi}(x)=\omega'_\xi(j(x)),\\
 x\in M,
 \end{gathered}
 \tag{SJ.7}
\]
where \(\omega'_\xi\) is the vector functional on \(M'\). Indeed,
\(\langle Jx^*J\xi,\xi\rangle=\langle J\xi,x^*J\xi\rangle=\langle xJ\xi,J\xi\rangle\). The adjoint in \(j\) makes this an equality of linear functionals. For the zero vector both supports and both functionals are zero.

## Moving a vector into the other cyclic subspace

We first prove a comparison fact that needs no conjugation and no trace. For any \(\xi,\eta\in H\),
\[
 \begin{gathered}
 e_\eta\precsim e_\xi\text{ in }M\\
 \Longleftrightarrow\\
 e'_\eta\precsim e'_\xi\text{ in }M'.
 \end{gathered}
 \tag{SJ.8}
\]
The proof uses the normal functional polar decomposition, NF02, with its specified left and right support conventions.

First assume \(\eta\in[M\xi]\), and put \(\varphi(x)=\langle x\eta,\xi\rangle\). This is a normal functional by polarization of vector functionals. Write its polar decomposition in the convention
\[
 \begin{gathered}
 \varphi(x)=\omega(xv),\qquad \omega\geq0,\\
 p=v^*v=s(\omega),\qquad q=vv^*.
 \end{gathered}
\]
The earlier theorem gives \(\varphi(xq)=\varphi(x)\), and the support identity \(\omega(xp)=\omega(x)\) gives
\[
 \psi(x):=\varphi(xv^*)=\omega(x).
\]
Both \(q\eta\) and \(\eta\) belong to \([M\xi]\). Their difference is orthogonal to every \(x^*\xi\), because
\(\langle x(q\eta-\eta),\xi\rangle=0\). Thus \(q\eta=\eta\).

Set \(\theta=v^*\eta\) and \(e=e_\xi\). Then \(\theta\in[M\xi]\) and \(\psi(x)=\langle x\theta,\xi\rangle\). Since \(e\xi=\xi\), we have \(\psi(ex)=\psi(x)\). Positivity makes \(\psi\) Hermitian, so taking adjoints also gives \(\psi(xe)=\psi(x)\). Therefore
\(\langle x(\theta-e\theta),\xi\rangle=0\) for every \(x\in M\). Both terms lie in \([M\xi]\), so \(\theta=e\theta\). We have moved \(\eta\), by a partial isometry in \(M\), into \([M'\xi]\).

The least-projection characterization in SJ02 gives \(e_\eta\leq q\). Consequently \(w=v^*e_\eta\in M\) is a partial isometry whose initial projection is \(e_\eta\). Its final range is
\[
 v^*[M'\eta]=[M'\theta].
\]
To justify equality including closures, \(v^*\) is an isometry on \(qH\), the space \([M'\eta]\) lies in \(qH\), and \(v^*\) commutes with \(M'\). The final projection is therefore \(e_\theta\leq e_\xi\). We have proved
\[
 \begin{gathered}
 \eta\in[M\xi]\\
 \Longrightarrow e_\eta\precsim e_\xi.
 \end{gathered}
 \tag{SJ.9}
\]
If \(\varphi=0\), orthogonality and \(\eta\in[M\xi]\) already force \(\eta=0\); the same conclusion holds with \(v=0\).

Now suppose \(e'_\eta\precsim e'_\xi\). Choose \(u\in M'\) with \(u^*u=e'_\eta\) and \(uu^*\leq e'_\xi\), and put \(\eta_1=u\eta\). Then \(\eta_1\in[M\xi]\). Moreover \(\eta_1=u\eta\) and \(\eta=u^*\eta_1\) imply
\([M'\eta_1]=[M'\eta]\), so \(e_{\eta_1}=e_\eta\). Equation (SJ.9) proves \(e_\eta\precsim e_\xi\). Apply this same argument to the von Neumann algebra \(M'\), whose commutant is \(M\), to obtain the converse and hence (SJ.8).

## A vector and its conjugate have equivalent supports

Under (SJ.1)–(SJ.2), every vector satisfies
\[
 e_\xi\sim e_{J\xi}\quad\text{in }M.
 \tag{SJ.10}
\]
Use central comparison of projections, CT01 to choose a central projection \(z\) such that
\[
 \begin{gathered}
 ze_\xi\precsim ze_{J\xi},\\
 (1-z)e_{J\xi}\precsim(1-z)e_\xi.
 \end{gathered}
\]
Let \(\alpha=z\xi\). Equations (SJ.6) identify the first inequality as \(e_\alpha\precsim e_{J\alpha}\). By (SJ.8) it gives \(e'_\alpha\precsim e'_{J\alpha}\) in \(M'\). Conjugating its witnessing partial isometry by \(J\), and using (SJ.5) and \(J^2=1\), reverses the roles of the vectors:
\[
 e_{J\alpha}\precsim e_\alpha.
\]
Mutual subequivalence implies equivalence by the explicit projection Schröder–Bernstein argument in PE07. Thus the two supports are equivalent on \(zH\). Apply the same reasoning with the vectors interchanged on \((1-z)H\).

The partial isometries witnessing these two equivalences have orthogonal initial projections and orthogonal final projections, because they belong to complementary central corners. Their sum is therefore a partial isometry from \(e_\xi\) to \(e_{J\xi}\). This proves (SJ.10), including the zero vector. Notice that no semifiniteness, faithful vector, or positive cone was used.

## The center-valued trace identity

Now assume that \(M\) is semifinite. Let \(T\) be a normal extended center-valued trace on \(M\), in the sense of EC03. Define a map on \(M'_+\) by
\[
 T'(y)=T(JyJ).
 \tag{SJ.11}
\]
The centers of \(M\) and \(M'\) are the same algebra \(Z\), so both maps take values in the same extended positive center.

This map is again a normal extended center-valued trace. Additivity and nonnegative homogeneity follow from SJ01. For \(a\in Z_+\), the center rule gives \(\kappa(ay)=a\kappa(y)\), whence \(T'(ay)=aT'(y)\). The trace identity follows, for \(b\in M'\), from
\[
 \begin{aligned}
 T'(b^*b)
   &=T(\kappa(b)^*\kappa(b))\\
   &=T(\kappa(b)\kappa(b)^*)\\
   &=T'(bb^*).
 \end{aligned}
\]
An increasing bounded net in \(M'_+\) is carried to an increasing net with the corresponding supremum in \(M_+\). Normality of \(T\) then proves normality of \(T'\). Faithfulness, when assumed for \(T\), transfers because \(\kappa(y)=0\) precisely when \(y=0\). No faithfulness assumption is needed in the identity below.

For every \(\xi\in H\),
\[
 T(e_\xi)=T'(e'_\xi).
 \tag{SJ.12}
\]
Indeed a partial isometry from SJ04 gives \(T(e_\xi)=T(e_{J\xi})\), by the trace identity. Equation (SJ.5) identifies \(e_{J\xi}=Je'_\xi J\), and (SJ.11) gives the result. This argument allows infinite central values: it uses equality under equivalence, with no subtraction or cancellation of infinities. It also proves the assertion whenever two given normal extended center-valued traces obey (SJ.11).

## The conjugation supplied by a semifinite scalar trace

Let \(\tau\) be a faithful normal semifinite scalar trace on a von Neumann algebra \(N\). The tracial Hilbert space construction, TI15 completes the bounded square-integrable ideal and extends
\[
 J_\tau x=x^*
\]
to an antiunitary involution on \(L^2(N,\tau)\). Write \(L_a x=ax\) and \(R_a x=xa\) on the bounded trace ideal, with their bounded extensions to this Hilbert space. The complete tracial action theorem, TA02 gives
\[
 \begin{gathered}
 L(N)'=R(N),\\
 R(N)'=L(N),\\
 J_\tau L_aJ_\tau=R_{a^*}.
 \end{gathered}
 \tag{SJ.13}
\]
For \(a\in Z(N)\), left and right multiplication by \(a^*\) agree on the dense bounded trace ideal and hence on all of \(L^2(N,\tau)\). Thus \(J_\tau L_aJ_\tau=L_{a^*}\). The faithful representation \(L\) identifies \(Z(N)\) with \(Z(L(N))\): an element \(L_a\) commutes with every \(L_b\) exactly when \(ab=ba\) for every \(b\), by faithfulness. Consequently \(J_\tau\) satisfies all the hypotheses (SJ.1)–(SJ.2) for \(M=L(N)\).

These facts concern the entire tracial Hilbert space. They do not presume that \(1\) belongs to \(L^2(N,\tau)\), or that the trace is finite, or that the algebra is countably decomposable. The two supports of any tracial \(L^2\)-vector therefore satisfy (SJ.10) and, for traces related by (SJ.11), (SJ.12).

## Four tests of the hypotheses

**Equivalent need not mean equal.** Let \(N=M_2(\mathbb C)\), let \(H\) be its Hilbert–Schmidt space, and use \(M=L(N)\) and \(JX=X^*\). For \(\xi=E_{12}\), direct multiplication by matrix units gives
\[
 \begin{gathered}
 e_\xi=L_{E_{11}},\qquad
 e_{J\xi}=L_{E_{22}},\\
 e'_\xi=R_{E_{22}}.
 \end{gathered}
\]
The first two projections are distinct. The partial isometry \(L_{E_{21}}\) witnesses their equivalence. With the normalized matrix traces on the two algebras, (SJ.12) gives the common value \(1/2\).

**The center condition is necessary.** Represent \(M=\mathbb C\oplus\mathbb C\) diagonally on \(\mathbb C^2\), so \(M'=M\). The map
\[
 J(s,t)=(\overline t,\overline s)
\]
is an antiunitary involution and exchanges the algebra with its commutant. But it sends the diagonal operator \((a,b)\) to \((\overline b,\overline a)\), rather than to \((\overline a,\overline b)\). For \(\xi=(1,0)\), the supports \(e_\xi=(1,0)\) and \(e_{J\xi}=(0,1)\) are inequivalent: in an abelian algebra \(v^*v=vv^*\), so equivalent projections must be equal.

**A conjugation does not specify the usual positive cone.** In the matrix Hilbert–Schmidt example, put \(J_\theta=e^{i\theta}J\). Antilinearity gives \(J_\theta^2=1\), and its conjugation of every linear operator is the same as that of \(J\). Hence (SJ.1)–(SJ.2) still hold. If \(e^{i\theta}\ne1\), however, \(J_\theta I=e^{i\theta}I\ne I\). Thus it does not fix the usual cone of positive matrices pointwise. This makes no assertion against choosing a different cone; it shows why that extra datum cannot be silently inserted into the hypotheses here.

**There need not be a faithful vector.** Let \(I\) be uncountable and let \(M=\ell^\infty(I)\) act diagonally on \(\ell^2(I)\). An operator commuting with every coordinate projection must act by a scalar on each coordinate line; boundedness makes those scalars a member of \(\ell^\infty(I)\). Thus \(M'=M\). Coordinatewise complex conjugation satisfies (SJ.1)–(SJ.2). Both supports of \(\xi\) are the diagonal indicator of \(\{i:\xi_i\ne0\}\). This set is countable: for each positive integer \(n\), only finitely many coordinates can have modulus at least \(1/n\), by square summability. No vector has full support when \(I\) is uncountable. Nevertheless all the conjugation and support assertions hold, and the normal center-valued trace \(T(x)=x\) on positive diagonal operators verifies (SJ.12) directly.

**Source.** M. Takesaki, *Theory of Operator Algebras I*, Chapter V, §3, Definition 3.3, Lemma 3.4 and Corollary 3.5, p. 337. The cyclic-space comparison used here is proved in SJ03 from the earlier normal functional polar decomposition; SJ04 keeps the support conclusion at arbitrary von Neumann algebra generality.
