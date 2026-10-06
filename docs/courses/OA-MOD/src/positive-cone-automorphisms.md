# Positive changes of scale on a standard cone

**Independently written mathematical draft.**

A positive invertible Hilbert-space operator that maps a standard cone onto itself has a particularly rigid form: it multiplies on the left and right by one positive invertible algebra element. We prove this by first interpreting a quarter-modular norm comparison as an order comparison of positive vectors. This gives an actual closed-domain argument for the analytic cocycle endpoint. A separate order argument then supplies the change of faithful functional needed for the factorization.

The source target is Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(8). The dense-face assertion in its part (a) needs an injectivity hypothesis; PA-05 proves the corrected statement, and PA-07 gives a counterexample without that hypothesis. The main statement here concerns the one fixed cone of the retained standard form; the printed two-cone notation is not used to assert a theorem about unspecified different cones. Every valid part (a)–(e) is treated below.

We use the exact earlier proofs of The quarter-power map is defined on the whole algebra and Identify the algebraic principal face, quarter-power maps and principal faces, Real decomposition and orthogonal supports and A finite matrix weight and its four closed graphs/13, orthogonal supports and relative closed graphs, The corner seen by a positive vector and Closing one order ideal gives its entire supported face/11, faithful vectors and faces, A balanced weight and its four exact domains and Reading a unitary cocycle from one matrix unit/08, balanced modular cocycles, A closed intertwining relation is a bounded operator strip, the bounded strip criterion, Create analytic tests without changing the real topology, Gaussian analytic elements, A spectral domain is a strip-extension condition and Gaussian continuation of bounded real orbits, domains and smoothing, Assemble the cone unitary and prove canonicity, Jordan implementation, and Identify the order-map formula exactly, its quarter-power covariance. Bounded forms, positive square roots and commutants use The bounded prerequisite boundary and Finite-vector approximation and the bicommutant; spectral approximation uses Unbounded measurable functions and Changes of variable, powers, and actual ranges/08; normality uses The positive-map equivalence. These are proof providers, not external citations in place of arguments.

Fix a standard form \((M,H,J,P)\). Inner products are linear in the first variable. For a faithful normal positive functional \(\chi\), write \(\xi_\chi\in P\) for its representative and put

\[
 \Theta_\chi(x)=\Delta_\chi^{1/4}x\xi_\chi
 \qquad(x\in M).
\]

QO-01 proves this expression is defined for every algebra element. None of the faithful functionals below is required to have mass one.

## Norm comparison detects the order of positive vectors

Let \(\varphi,\psi\) be faithful normal positive functionals. We first prove the implication

\[
 \begin{gathered}
 \|\Theta_\psi(x)\|\\
 \le\|\Theta_\varphi(x)\|\\
 (x\in M)\\
 \Longrightarrow\quad \xi_\psi\le\xi_\varphi.
 \end{gathered}
 \tag{PA.1}
\]

The inequality on projections alone suffices. Indeed, for a projection \(e\in M\), let \(Q_e=eJeJ\). Its factors are commuting orthogonal projections, so \(Q_e\) is the orthogonal projection onto the standard corner. The finite Tomita identity gives

\[
 \begin{aligned}
 \|\Theta_\chi(e)\|^2
 &=\langle Je\xi_\chi,e\xi_\chi\rangle\\
 &=\langle Q_e\xi_\chi,\xi_\chi\rangle
 =\|Q_e\xi_\chi\|^2.
 \end{aligned}
\]

Decompose the \(J\)-fixed vector \(d=\xi_\psi-\xi_\varphi\) as \(d=d_+-d_-\), using SF-06. The positive and negative parts belong to \(P\) and have orthogonal support projections. With \(e=s(d_+)\), those support identities and \(Jd_\pm=d_\pm\) imply \(Q_ed=d_+\). Hence the assumed inequality at \(e\) implies

\[
 \begin{aligned}
 0&\ge\|Q_e\xi_\psi\|^2-\|Q_e\xi_\varphi\|^2\\
 &=2\langle Q_e\xi_\varphi,d_+\rangle+\|d_+\|^2\\
 &\ge\|d_+\|^2.
 \end{aligned}
\]

The last inequality uses \(Q_eP\subset P\) and self-duality. Thus \(d_+=0\), proving (PA.1). The converse will follow from the cocycle construction in PA-02/03. Notice that this is order in the Hilbert cone; it does not assert domination of the represented positive functionals.

## Cone order gives a closed quarter-power intertwiner

Assume \(\xi_\psi\le\xi_\varphi\). Let \(D=\Delta_{\psi,\varphi}\) be the relative operator constructed by SF-08/13 on the common standard space. Because the functionals are finite and faithful, its defining core is \(M\xi_\varphi\), and

\[
 D^{1/2}x\xi_\varphi=Jx^*\xi_\psi
 \qquad(x\in M).
\]

For \(v=x\xi_\varphi\), spectral calculus and the commutant relation give

\[
 \begin{gathered}
 \|D^{1/4}v\|^2\\
 =\langle Jx^*\xi_\psi,x\xi_\varphi\rangle\\
 =\langle\xi_\psi,xJxJ\xi_\varphi\rangle\\
 \le\langle\xi_\varphi,xJxJ\xi_\varphi\rangle\\
 =\|\Delta_\varphi^{1/4}v\|^2.
 \end{gathered}
 \tag{PA.2}
\]

Here \(xJxJ\xi_\varphi\in P\), so cone order supplies the middle inequality. All vectors in this calculation lie in the half-power domains in question before taking their quarter powers.

The space \(M\xi_\varphi\) is a core for \(\Delta_\varphi^{1/2}\), by the finite Tomita construction. It is also a core for \(\Delta_\varphi^{1/4}\): truncate a vector in the latter domain to bounded spectral bands, then approximate each truncation in the half-power graph norm. The estimate \(\|\Delta_\varphi^{1/4}w\|^2\le\|w\|\|\Delta_\varphi^{1/2}w\|\) makes these approximations converge in the quarter-power graph norm. For a quarter-domain vector, choose such a sequence from \(M\xi_\varphi\). Inequality (PA.2) makes its images under \(D^{1/4}\) Cauchy. Closedness of \(D^{1/4}\) therefore proves

\[
 \begin{gathered}
 D(\Delta_\varphi^{1/4})\subset D(D^{1/4}),\\
 \|D^{1/4}v\|\le\|\Delta_\varphi^{1/4}v\|
 \quad(v\in D(\Delta_\varphi^{1/4})).
 \end{gathered}
\]

Consequently the rule \(a\Delta_\varphi^{1/4}v=D^{1/4}v\) defines a contraction on the dense range of the injective self-adjoint operator \(\Delta_\varphi^{1/4}\), and extends to \(a\in B(H)\). We still have to prove \(a\in M\).

For this purpose put \(\Omega=\operatorname{diag}(\psi,\varphi)\) on \(N=M_2(M)\). In SF-08's four-slot model, identify both column GNS spaces with \(H\) using SF-13. Restrict the modular operator to the second column, the slots \((1,2)\) and \((2,2)\). On \(K=H\oplus H\) this restriction is

\[
 \mathcal D=\operatorname{diag}(D,\Delta_\varphi).
\]

The second column reduces the modular powers and the left action of \(N\). This left action on \(K\) is faithful. Thus GC-03/04's modular implementation restricts to \(\operatorname{Ad}\mathcal D^{it}\) on that same represented algebra. In particular

\[
 \mathcal D^{it}E_{12}\mathcal D^{-it}
 =(D\psi:D\varphi)_t E_{12}.
\]

This identity is obtained from the full matrix modular operator, not from an unproved formal relative-power formula.

Let \(B(v,w)=(aw,0)\). The full domain assertion just proved says exactly

\[
 \begin{gathered}
 E_{12}D(\mathcal D^{1/4})\subset D(\mathcal D^{1/4}),\\
 \mathcal D^{1/4}E_{12}\zeta
 =B\mathcal D^{1/4}\zeta
 \quad(\zeta\in D(\mathcal D^{1/4})).
 \end{gathered}
\]

Apply HS-01 with strip height \(1/4\). Its algebra-membership conclusion gives \(B\in N\), hence \(a\in M\). Its unique strip extension has only the \((1,2)\) entry, by scalar boundary uniqueness applied to the other corners. It therefore supplies a bounded \(M\)-valued extension \(u_z\) of the normalized cocycle, with

\[
 \begin{gathered}
 u_t=(D\psi:D\varphi)_t,\\
 u_{-i/4}=a,\\
 \|a\|\le1.
 \end{gathered}
 \tag{PA.3}
\]

The extension is sigma-weakly continuous on the closed strip and norm holomorphic in its interior. No norm continuity of its real edge is asserted.

## An endpoint sandwiches the whole quarter-power image

We need a covariance identity for a faithful finite functional \(\chi\) on any von Neumann algebra \(N\). Suppose the modular orbit of \(c\in N\) has a bounded closed lower-quarter-strip extension with endpoint \(b\). We claim

\[
 \begin{gathered}
 \Theta_\chi(cxc^*)\\
 =bJbJ\Theta_\chi(x)\\
 (x\in N).
 \end{gathered}
 \tag{PA.4}
\]

First suppose \(c,x\) are norm-entire for the modular group \(\alpha\). The vector-domain calculation in QO-01 gives \(\Theta_\chi(y)=\alpha_{-i/4}(y)\xi_\chi\) for entire \(y\), and

\[
 \begin{aligned}
 JbJ\xi_\chi
 &=\alpha_{-i/2}(b^*)\xi_\chi\\
 &=\alpha_{-i/4}(c^*)\xi_\chi.
 \end{aligned}
\]

Since \(JbJ\) commutes with the left algebra, multiplication of the three entire factors proves (PA.4). For arbitrary \(x\), approximate it strongly-star by uniformly bounded entire elements. The estimate

\[
 \|\Theta_\chi(y)\|^2
 \le\|y\xi_\chi\|\,\|y^*\xi_\chi\|
\]

from QO-01 gives continuity along this approximation, including after multiplication by the fixed \(c,c^*\). Thus (PA.4) holds for every \(x\) when \(c\) is entire.

Now allow the asserted quarter-strip hypothesis on \(c\). With normalized Gaussians \(g_r(t)=\sqrt{r/\pi}e^{-rt^2}\), put

\[
 \begin{gathered}
 c_r=\int g_r(t)\alpha_t(c)\,dt,\\
 b_r=\int g_r(t)\alpha_t(b)\,dt.
 \end{gathered}
\]

These are bounded operator integrals, defined by their normal scalar tests, and converge strongly-star to \(c,b\), respectively. CZ-02/MA-16 prove that \(c_r\) is entire. Moreover its quarter endpoint is exactly \(b_r\). To check this without assuming a contour interchange, HS-01 gives the full relation \(\Delta_\chi^{1/4}c=b\Delta_\chi^{1/4}\). Conjugating by real modular powers gives that relation with \(\alpha_t(c),\alpha_t(b)\). Integrate it on a fixed domain vector: both graph coordinates are strongly continuous bounded functions of \(t\), and the closed linear graph is preserved by their Gaussian integral. Thus \(\Delta_\chi^{1/4}c_r=b_r\Delta_\chi^{1/4}\) on the full domain. The entire endpoint has the same relation, by MA-09; the dense range of \(\Delta_\chi^{1/4}\) identifies it with \(b_r\). Applying the entire case of (PA.4) to \(c_r\), then taking strong-star limits, proves (PA.4). Products converge on each fixed vector under the uniform bounds, and the displayed estimate handles its left-hand side.

Apply (PA.4) to the finite balanced functional \(\Omega=\operatorname{diag}(\psi,\varphi)\), with \(c=E_{12}\), \(b=aE_{12}\), and input \(xE_{22}\). The four-slot description gives \(\Theta_\Omega(xE_{22})\) with sole entry \(\Theta_\varphi(x)\) in slot \((2,2)\); its left side has sole entry \(\Theta_\psi(x)\) in slot \((1,1)\). In the common standard-space identification, the matrix conjugation sends an entry \(v\) in slot \((i,j)\) to \(Jv\) in slot \((j,i)\). Applying \(bJ_\Omega bJ_\Omega\) therefore sends that \((2,2)\) entry to \(aJaJ\Theta_\varphi(x)\) in \((1,1)\). We obtain

\[
 \begin{gathered}
 \Theta_\psi(x)\\
 =aJaJ\Theta_\varphi(x)\\
 (x\in M).
 \end{gathered}
 \tag{PA.5}
\]

If a cocycle extension with \(\|a\|\le1\) is given initially, this same argument applies: its matrix-valued extension is the extension of the balanced modular orbit by uniqueness. Formula (PA.5) implies the norm inequality because \(\|aJaJ\|\le\|a\|^2\le1\). Together with PA-01/02 this proves the full equivalence of the norm inequality, cone order \(\xi_\psi\le\xi_\varphi\), and the contractive lower-quarter endpoint. It also proves the sandwich identity on every algebra element, with all domain passages justified.

## A unital order isomorphism preserves Jordan multiplication

Let \(F:M\to N\) be a complex-linear bijection between von Neumann algebras, with \(F(1)=1\), such that both \(F\) and its inverse \(G\) are positive. We prove directly that \(F\) is a normal Jordan star isomorphism.

A positive unital map is contractive on self-adjoint elements: apply it to \(-\|x\|1\le x\le\|x\|1\). It preserves adjoints by writing a self-adjoint element as a difference of positives and then decomposing an arbitrary element into its real and imaginary parts. In particular it is bounded, with \(\|F(x)\|\le2\|x\|\) sufficient for what follows.

For a finite spectral step \(x=\sum_{j=1}^n\lambda_jp_j\), with real \(\lambda_j\), orthogonal projections \(p_j\), and \(\sum p_j=1\), set \(q_j=F(p_j)\). Represent \(N\) on a Hilbert space \(L\). The operator \(V:L\to L^n\), \(Vv=(q_j^{1/2}v)_j\), is an isometry because \(\sum q_j=1\). Put \(D=\operatorname{diag}(\lambda_j I_L)\) and \(R=(1-VV^*)DV\). The projection identity \((1-VV^*)^2=1-VV^*\) gives

\[
 \begin{gathered}
 F(x)=V^*DV,\\
 F(x^2)=V^*D^2V,\\
 F(x^2)-F(x)^2\\
 =R^*R\ge0.
 \end{gathered}
 \tag{PA.6}
\]

Norm spectral approximation of an arbitrary self-adjoint \(x\), followed by boundedness of \(F\), proves the same Schwarz inequality for every such \(x\). It also holds for \(G\). Consequently

\[
 x^2\le G(F(x)^2)\le G(F(x^2))=x^2.
\]

Thus \(F(x^2)=F(x)^2\). Polarization with self-adjoint \(x,y\), and then complex bilinearity, proves preservation of \(xy+yx\) for all \(x,y\). This is the Jordan assertion.

Finally an order bijection preserves bounded increasing suprema: if \(x=\sup x_i\), any upper bound for the \(F(x_i)\) pulls back to an upper bound for the \(x_i\). Thus \(F(x)=\sup F(x_i)\), and NP-04 proves normality; the same applies to \(G\). This argument proves exactly the unital order-isomorphism lemma used here. It does not settle the broader general linear-isometry prerequisite elsewhere in the course.

## Factor an injective map with dense face range

Suppose \(\Theta:M\to H\) is complex linear and injective, and \(F=\Theta(M_+)\) is an algebraic face of \(P\) whose norm closure is \(P\). A face here is a subcone with the property that \(u,v\in P\) and \(u+v\in F\) imply \(u,v\in F\). We do not assume the face is closed or that \(\Theta\) is bounded in advance.

Put \(\eta=\Theta(1)\). If \(a\ge0\), then \(a\le\|a\|1\), so \(\Theta(a)\le\|a\|\eta\). Conversely any \(0\le v\le C\eta\) belongs to \(F\), by the face property. Thus

\[
 F=\bigcup_{C\ge0}[0,C\eta].
 \tag{PA.7}
\]

Its dense closure, SE-07's principal-face theorem, and the support characterization give \(s(\eta)=1\). The functional \(\rho=\omega_\eta\) is therefore faithful, and \(\xi_\rho=\eta\). QO-05 identifies \(\Theta_\rho(M_+)\) with exactly this \(F\), and its full linear range with the complex span of \(F\), also the range of \(\Theta\).

We verify order reflection for \(\Theta\); injectivity alone is not a substitute for it. Since \(J\) fixes \(\Theta(M_+)\), decomposition into real and imaginary self-adjoint parts gives \(J\Theta(x)=\Theta(x^*)\). If \(\Theta(x)\in P\), injectivity forces \(x=x^*\). Write \(x=a-b\) with \(a,b\ge0\). The equality \(\Theta(a)=\Theta(x)+\Theta(b)\) and the face property imply \(\Theta(x)\in F\). Hence \(\Theta(x)=\Theta(c)\) for some \(c\ge0\), and injectivity gives \(x=c\). This proves order reflection on the entire range.

It follows that \(\beta=\Theta_\rho^{-1}\Theta\) is a unital complex order isomorphism of \(M\) onto itself. By PA-04 it is a normal Jordan star isomorphism. Let \(U=U_\beta\) be JI-06's canonical cone unitary and put \(\psi=\rho\circ\beta\). This is a faithful normal positive functional. Its defining vector-functional identity gives \(U\xi_\psi=\xi_\rho\). JR-06's proved quarter-power covariance now yields

\[
 \begin{gathered}
 U\Theta_\psi(x)\\
 =\Theta_\rho(\beta(x))\\
 =\Theta(x),\\
 \Theta=U\Theta_\psi,\\
 U(P)=P.
 \end{gathered}
 \tag{PA.8}
\]

This also proves boundedness of \(\Theta\) after the fact. PA-07 shows why dropping injectivity would make this statement false.

## Recover the unique positive algebra element

Assume \(M\) is sigma-finite and \(T\in B(H)\) is positive and invertible, with \(T(P)=P\). There exists a faithful normal positive functional \(\varphi\). For completeness, under the countably-decomposable definition of sigma-finiteness, choose a maximal orthogonal family of supports of normal positive functionals. Their supremum is one: any nonzero complementary projection admits a nonzero normal vector functional supported below it. The family is countable. A sum of the normalized functionals with strictly positive summable coefficients is normal and faithful. Normality follows by bounding the norm tails of the series uniformly on positive contractions and using normality of each finite sum; faithfulness follows from the supports summing to one. This constructs the required \(\varphi\) without a separability assumption.

The map \(T\Theta_\varphi\) is injective. Its positive range is a dense algebraic face: QO-05 gives that property for \(\Theta_\varphi(M_+)\), and the continuous cone bijection \(T\), with positive-on-the-cone inverse, transports both density and the face property. Apply PA-05. There are a faithful \(\psi\) and a cone unitary \(U\) such that

\[
 T\Theta_\varphi=U\Theta_\psi.
\]

Since \(\Theta_\varphi(M)\) is dense, the quarter-vector comparison extends uniquely to the bounded invertible operator \(A=U^*T\), and

\[
 \begin{gathered}
 A\Theta_\varphi(x)=\Theta_\psi(x),\\
 A^*A=T^2,\\
 |A|=T.
 \end{gathered}
 \tag{PA.9}
\]

The last equality is uniqueness of the positive square root in BK-01.

Let \(C=\|A\|>0\) and \(\widetilde\psi=C^{-2}\psi\). Multiplication of a faithful functional by a positive scalar leaves its modular operator unchanged, since the initial Tomita graph is unchanged after scaling its cyclic vector. Its positive vector, and hence its quarter map, scale by the square root. Thus \(\Theta_{\widetilde\psi}=C^{-1}\Theta_\psi\). The comparison with \(\Theta_\varphi\) is contractive. PA-01/02/03 give \(b\in M\) with \(C^{-1}A=bJbJ\). Set \(a=\sqrt C\,b\). Then \(A=aJaJ\).

The two factors \(a\) and \(JaJ\) commute. Since their product \(A\) is invertible, each is invertible: \((JaJ)A^{-1}\) is both a left and a right inverse for \(a\), because \(a\) commutes with \(A\) and hence with \(A^{-1}\). The inverse belongs to \(M\), since it commutes with every element of \(M'\). Put \(h=|a|\in M_+\); it is invertible. Commutation between the algebra and commutant factors gives

\[
 \begin{aligned}
 A^*A&=(a^*a)J(a^*a)J\\
 &=(hJhJ)^2.
 \end{aligned}
\]

The factors \(h,JhJ\) are commuting positive operators, so their product is positive. The positive square-root uniqueness used in (PA.9) now gives the asserted factorization

\[
 T=hJhJ.
 \tag{PA.10}
\]

To prove uniqueness, first suppose \(aJaJ=I\) for some \(a\in M\). The commuting-factor argument makes \(a\) invertible with \(a^{-1}=JaJ\). This inverse belongs to both \(M\) and \(M'\), so \(a\) is central. If \(h,k\) are positive invertible and \(hJhJ=kJkJ\), put \(a=k^{-1}h\). Multiplication of the two commuting left/right pairs gives \(aJaJ=I\). Thus \(a\) is central and \(h=ka\). In particular \(h\) commutes with \(k\), so \(a=k^{-1/2}hk^{-1/2}\) is positive. The central standard-form identity gives \(JaJ=a\); hence \(a^2=I\), and positivity forces \(a=I\). Therefore \(h=k\).

Conversely each positive invertible \(h\in M\) gives a positive invertible \(hJhJ\), and the standard-form cone axiom applied to both \(h\) and \(h^{-1}\) shows that it maps \(P\) onto itself. This completes the characterization. The zero algebra, if allowed, is the vacuous zero-space case; the argument above concerns the nonzero case in which a faithful functional and \(C>0\) are chosen.

## Check the hypothesis and distinguish the two orders

**Why the dense-face lemma needs injectivity.** On \(M=\ell^\infty(\mathbb N)\), with \(H=\ell^2(\mathbb N)\), coordinate conjugation and the nonnegative cone, put \(\eta_n=2^{-n}\), for \(n\ge1\), and define

\[
 (\Theta x)_n=2^{-n}x_{n+1}.
\]

This is a bounded complex-linear map. Its positive image is precisely the principal face \(\{v\in P:v\le C\eta\text{ for some finite }C\}\): a bounded nonnegative tail realizes every such \(v\), and any image has that bound. The set is an algebraic face because a nonnegative summand of a vector bounded by \(C\eta\) has the same bound. It is dense, since every finite-coordinate nonnegative vector belongs to it. But \(\Theta(e_1)=0\). Every quarter map of a faithful functional is injective by QO-01, as is its composition with a unitary. Thus the factorization claimed without injectivity cannot hold. The application in PA-06 has exactly the missing injectivity, so this correction does not weaken the main theorem.

**The quarter endpoint measures vector order.** In the Hilbert–Schmidt standard form of \(M_n(\mathbb C)\), let \(\varphi(x)=\operatorname{Tr}(rx)\) and \(\psi(x)=\operatorname{Tr}(sx)\), with positive invertible densities. Direct finite-dimensional functional calculus gives

\[
 \begin{gathered}
 \Theta_\varphi(x)=r^{1/4}xr^{1/4},\\
 u_z=s^{iz}r^{-iz},\qquad a=s^{1/4}r^{-1/4}.
 \end{gathered}
\]

Thus \(\|a\|\le1\) is equivalent, by multiplying \(a^*a\le I\) by \(r^{1/4}\) on both sides, to \(s^{1/2}\le r^{1/2}\). Formula (PA.5) is the ordinary matrix identity \(s^{1/4}xs^{1/4}=a(r^{1/4}xr^{1/4})a^*\). This checks the quarter-strip sign and order of its factors.

The vector order need not imply \(s\le r\), even when both functionals are faithful. Set

\[
 B=\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad C=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]

Then \(C-B\ge0\). Take \(s^{1/2}=B+\varepsilon I\) and \(r^{1/2}=C+\varepsilon I\), with \(\varepsilon=1/10\). Both are positive invertible and have the required vector order. But

\[
 r-s=\begin{pmatrix}21/5&16/5\\16/5&11/5\end{pmatrix}
\]

has determinant \(-1\), so functional domination fails. This example is consistent with the quarter criterion and prevents replacing it by the stronger half-strip domination theorem.

Finally, for a positive invertible matrix \(h\), the Hilbert-space operator \(X\mapsto hXh\) is positive: in an orthonormal eigenbasis of \(h\), each matrix unit has the positive eigenvalue \(h_i h_j\). Its inverse is \(X\mapsto h^{-1}Xh^{-1}\), and it maps the positive matrix cone onto itself. PA-06 identifies exactly this operation in the general standard form. The examples check the theorem; they do not replace its infinite-dimensional proof.
