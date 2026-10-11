# Global assembly of approximate intertwiners

A local approximate intertwiner can occupy an arbitrarily small corner. To use such operators globally, we must fill the identity, control the vector components between different pieces, and prevent all the mass from disappearing as more functionals are tested. We prove these three steps separately.

Except in Section 6, let \(M\) be a type III factor with a faithful normal state \(\varphi_0\), and let \((M,H,J,P)\) be its standard form. Write \(\theta\xi=U_\theta\xi\) for the canonical action of an automorphism \(\theta\) on \(H\), and \(\xi a=Ja^*J\xi\) for the right action. Thus \(\theta(a\xi b)=\theta(a)(\theta\xi)\theta(b)\).

We assume that \(\theta\) is locally approximately inner in the precise sense of LC04: for every finite family \(\xi_j\in P\) and every \(s>0\), some \(x\ne0\) satisfies


\[
\sum_j\|x\xi_j-(\theta\xi_j)x\|^2
\leq s^2\sum_j\|x\xi_j\|^2.
\tag{1}
\]


Our local input is the compression theorem LC05, with the fixed mass constant


\[
d=\frac1{12800}.
\]


We also use inner perturbations and fixed corners, standard forms of corners, positive representatives, and the concrete predual. The equivalence of nonzero projections in a countably decomposable type III factor is the earlier programme result used in OH06.

The faithful state implies countable decomposability. Indeed, if \((p_i)\) are orthogonal nonzero projections, each \(\varphi_0(p_i)>0\); for each integer \(m\), at most \(m\) of these values can exceed \(1/m\). Their union over \(m\) contains the entire family. No separability of \(M_*\) is assumed until the sequence conclusion in Section 5.

## 1. Local pieces in any residual corner

Fix \(\xi_1,\ldots,\xi_n\in P\), \(\tau>0\), and a nonzero projection \(q\). Put \(\eta_j=q\xi_jq\). These vectors belong to the natural cone of \(qMq\), by the standard-form corner theorem.

**Lemma 1.1.** There are a nonzero projection \(e\leq q\) and a contraction \(x\in\theta(e)Me\) such that


\[
\begin{aligned}
\sum_j\|x\eta_j\|^2
&\geq d\sum_j\|e\eta_j\|^2,\\
\sum_j\|[e,\eta_j]\|^2
&\leq\tau^2\sum_j\|e\eta_j\|^2,\\
\sum_j\|x\eta_j-(\theta\eta_j)x\|^2
&\leq\tau^2\sum_j\|x\eta_j\|^2.
\end{aligned}
\tag{2}
\]


**Proof.** If \(q=1\), apply LC05 directly. Otherwise \(q,1-q,\theta(q),1-\theta(q)\) are all nonzero and hence equivalent in the countably decomposable type III factor. Choose partial isometries from \(\theta(q)\) to \(q\) and from \(1-\theta(q)\) to \(1-q\). Their sum \(w\) is unitary: the initial projections are orthogonal and sum to one, as do the final projections. Thus \(w\theta(q)w^*=q\).

The automorphism \(\alpha=\operatorname{Ad}(w)\circ\theta\) is locally approximately inner and fixes \(q\). Since \(q\sim1-q\), LC06 makes \(\alpha_q\) locally approximately inner on \(qMq\). Its standard-form action on \(qHq\) is the restriction of \(U_\alpha\), by cone-preserving implementation and its uniqueness.

Apply LC05 in this corner to \(\eta_j\). It gives \(e\ne0\), \(e\leq q\), and a contraction \(y=\alpha(e)ye\). Set \(x=w^*y\). Then \(x=\theta(e)xe\), and left multiplication by \(w^*\) preserves all relevant norms. In particular


\[
w^*\bigl(y\eta_j-(\alpha\eta_j)y\bigr)
=x\eta_j-(\theta\eta_j)x,
\]


because \(\alpha\eta_j=w(\theta\eta_j)w^*\). The projection commutators are unchanged, proving (2). The local theorem allows \(x=0\) if all the selected corner mass is zero, but always gives \(e\ne0\). \(\square\)

## 2. Exhaustion and the vector blocks it removes

Apply Lemma 1.1 successively in residual corners. A limit stage needs to be part of this construction: a countable collection of chosen pieces need not yet sum to one.

Here is an explicit exhaustion argument. By transfinite recursion over the countable ordinals, put


\[
q_\alpha=1-\bigvee_{\beta<\alpha}e_\beta.
\tag{3}
\]


If \(q_\alpha\ne0\), choose \(e_\alpha,x_\alpha\) by Lemma 1.1 with the vectors \(q_\alpha\xi_jq_\alpha\) and the same tolerance \(\tau\). At a limit ordinal, the join in (3) exists and is the strong supremum of the finite partial sums, by bounded monotone convergence. If the construction continued through every countable ordinal, it would produce an uncountable orthogonal family of nonzero projections, contradicting the faithful-state argument above. Therefore it stops at a countable ordinal \(\kappa\), with


\[
\sum_{\alpha<\kappa}e_\alpha=1,
\qquad q_\alpha=\sum_{\beta\geq\alpha}e_\beta.
\tag{4}
\]


All sums from now on have countably many terms; orthogonality makes their limits independent of an enumeration. The order on the indices is retained to specify the residuals.

For \(\xi\in P\), the vectors \(e_\alpha\xi e_\beta\) form its orthogonal block decomposition. Indeed, left multiplication by \(e_\alpha\) and right multiplication by \(e_\beta\) are commuting projections; their products are mutually orthogonal. The finite left and right partial sums tend strongly to the identity, so their product does too. Hence


\[
\xi=\sum_{\alpha,\beta<\kappa}e_\alpha\xi e_\beta
\quad\text{in Hilbert norm}.
\tag{5}
\]


Define its diagonal part and the upper rows by


\[
\xi^{\mathrm d}=\sum_\alpha e_\alpha\xi e_\alpha,
\qquad a_\alpha=e_\alpha\xi q_{\alpha+1}.
\tag{6}
\]


Each diagonal summand belongs to \(P\), so \(\xi^{\mathrm d}\in P\) by norm convergence and closedness. Since \(J\xi=\xi\), applying \(J\) to a block exchanges its indices. The upper blocks \(\alpha<\beta\) and lower blocks \(\alpha>\beta\) thus have equal total squared norm. For the first three indices the arrangement is


\[
\begin{pmatrix}
e_0\xi e_0&e_0\xi e_1&e_0\xi e_2\\
e_1\xi e_0&e_1\xi e_1&e_1\xi e_2\\
e_2\xi e_0&e_2\xi e_1&e_2\xi e_2
\end{pmatrix}.
\]


The first upper row is part of \(a_0\), the next of \(a_1\); their reflected lower entries are in \(Ja_0,Ja_1\). All these off-diagonal blocks are orthogonal. Thus


\[
\|\xi-\xi^{\mathrm d}\|^2
=2\sum_\alpha\|a_\alpha\|^2.
\tag{7}
\]


With \(\eta_\alpha=q_\alpha\xi q_\alpha\), direct multiplication gives


\[
[e_\alpha,\eta_\alpha]
=a_\alpha-Ja_\alpha,
\qquad
\|[e_\alpha,\eta_\alpha]\|^2=2\|a_\alpha\|^2.
\tag{8}
\]


These identities remain valid across limit stages: (4) identifies each residual with the sum of every later block, and all rearrangements concern nonnegative squared norms of the orthogonal decomposition (5).

## 3. A global contraction with quantitative mass

Write


\[
\Phi=\sum_j\omega_{\xi_j},\qquad
A(z)^2=\sum_j\|z\xi_j\|^2,
\qquad
D(z)^2=\sum_j\|z\xi_j-(\theta\xi_j)z\|^2.
\]


**Theorem 3.1.** For every \(\tau>0\) there is a contraction \(X\in M\) such that


\[
A(X)^2\geq\frac{d}{1+\tau^2/2}\Phi(1),
\qquad D(X)\leq3\tau\Phi(1)^{1/2}.
\tag{9}
\]


**Proof.** Use the exhaustion from Section 2 and put


\[
\begin{aligned}
\eta_{\alpha j}&=q_\alpha\xi_jq_\alpha,\\
S&=\sum_{\alpha,j}\|e_\alpha\eta_{\alpha j}\|^2,\\
T&=\sum_j\|\xi_j-\xi_j^{\mathrm d}\|^2.
\end{aligned}
\]


The squared norms defining \(S\) include exactly the diagonal and upper blocks in (5). Consequently, by (7),


\[
S=\Phi(1)-T/2.
\tag{10}
\]


Sum (8) and the middle estimate in (2). They give \(T\leq\tau^2S\). Therefore


\[
\frac{\Phi(1)}{1+\tau^2/2}\leq S\leq\Phi(1),
\qquad T\leq\tau^2\Phi(1).
\tag{11}
\]


Define \(X=\sum_\alpha x_\alpha\). This sum converges strongly, as does its adjoint sum. To check this, the initial supports of its summands lie in the mutually orthogonal \(e_\alpha\), their final supports lie in the mutually orthogonal \(\theta(e_\alpha)\), and each summand is a contraction. For every \(h\in H\),


\[
\Bigl\|\sum_{\alpha\in F}x_\alpha h\Bigr\|^2
=\sum_{\alpha\in F}\|x_\alpha e_\alpha h\|^2
\leq\sum_{\alpha\in F}\|e_\alpha h\|^2.
\]


The tail of the last orthogonal sum tends to zero. The analogous estimate with final supports treats adjoints. Strong closedness of \(M\) gives \(X\in M\), and the same inequality gives \(\|X\|\leq1\). We have \(Xe_\alpha=x_\alpha=\theta(e_\alpha)X\).

The final supports also give


\[
\begin{aligned}
A(X)^2
&=\sum_{\alpha,j}\|x_\alpha\xi_j\|^2\\
&\geq\sum_{\alpha,j}\|x_\alpha\eta_{\alpha j}\|^2
\geq dS.
\end{aligned}
\tag{12}
\]


For the first inequality, \(x_\alpha\eta_{\alpha j}=x_\alpha\xi_jq_\alpha\), and right multiplication by \(q_\alpha\) is a contraction. Equations (11)–(12) prove the mass estimate.

It remains to control the defect. On the diagonal vectors it decomposes as


\[
X\xi_j^{\mathrm d}-(\theta\xi_j^{\mathrm d})X
=\sum_\alpha b_{\alpha j},
\]


where


\[
\begin{aligned}
b_{\alpha j}
&=x_\alpha e_\alpha\xi_je_\alpha
-\theta(e_\alpha)(\theta\xi_j)\theta(e_\alpha)x_\alpha\\
&=\theta(e_\alpha)
\bigl(x_\alpha\eta_{\alpha j}
 -(\theta\eta_{\alpha j})x_\alpha\bigr)e_\alpha.
\end{aligned}
\tag{13}
\]


These vectors belong to the mutually orthogonal blocks \(\theta(e_\alpha)He_\alpha\). Their squared norms therefore add. Both compressions in the last line are contractions, and the last inequality in (2) gives


\[
\sum_j\|X\xi_j^{\mathrm d}-(\theta\xi_j^{\mathrm d})X\|^2
\leq\tau^2\sum_{\alpha,j}\|x_\alpha\eta_{\alpha j}\|^2
\leq\tau^2 S.
\tag{14}
\]


Finally compare \(\xi_j\) with \(\xi_j^{\mathrm d}\) in the direct sum of the vector spaces. Left and right multiplication by \(X\) are contractions, and \(U_\theta\) is unitary. Hence


\[
D(X)\leq\tau\sqrt S+2\sqrt T
\leq3\tau\sqrt S\leq3\tau\sqrt{\Phi(1)}.
\]


This proves (9), including families of zero mass. No orthogonality of the uncompressed defects was assumed; it holds for the diagonal blocks in (13), and the removed components were estimated separately. \(\square\)

## 4. A dense set controlled by one faithful state

This section applies to any von Neumann algebra with faithful normal state \(\varphi_0\). Let \(\zeta=\xi_{\varphi_0}\) and put


\[
\mathcal D=\{\psi\in M_*^+:
\psi\leq C\varphi_0\text{ for some finite }C\geq1\}.
\tag{15}
\]


**Lemma 4.1.** The set \(\mathcal D\) is norm dense in \(M_*^+\).

**Proof.** First \(M'\zeta\) is dense in \(H\). The projection \(p\) onto its closure commutes with \(M'\), since the subspace is invariant under every element of \(M'\) and its adjoint. The bicommutant theorem gives \(p\in M\). As \(p\zeta=\zeta\), faithfulness gives \(\varphi_0(1-p)=0\), hence \(p=1\).

For \(a'\in M'\), the normal positive vector functional \(\psi_{a'}=\omega_{a'\zeta}\) satisfies, for \(b\geq0\),


\[
\begin{aligned}
\psi_{a'}(b)
&=\|b^{1/2}a'\zeta\|^2
=\|a'b^{1/2}\zeta\|^2\\
&\leq\|a'\|^2\varphi_0(b).
\end{aligned}
\]


Thus \(\psi_{a'}\in\mathcal D\). Every \(\psi\in M_*^+\) has a cone vector \(\xi_\psi\). Approximate it in Hilbert norm by vectors \(a'\zeta\). For arbitrary Hilbert vectors \(u,v\), expansion of their vector functionals and Cauchy–Schwarz give


\[
\|\omega_u-\omega_v\|
\leq(\|u\|+\|v\|)\|u-v\|.
\tag{16}
\]


Indeed, at a contraction \(b\) their difference is
\(\langle b(u-v),u\rangle+\langle bv,u-v\rangle\). Equation (16) proves \(\psi_{a'}\to\psi\) in predual norm. The approximating vectors need not themselves belong to \(P\); their positive functionals have the canonical cone representatives supplied by SF10. \(\square\)

If \(M_*\) is separable, we may choose a sequence in \(\mathcal D\) dense in \(M_*^+\). To justify this explicitly, a subset of a separable metric space has a countable base and a countable dense subset, obtained by choosing a point from each nonempty basic open set. Approximate each point of such a dense subset of \(M_*^+\) by points of \(\mathcal D\) to accuracy \(1/k\), for every integer \(k\). The resulting countable family is dense in the whole positive cone.

## 5. Bounded approximate intertwiners that do not vanish

For a normal functional write \(\theta\psi=\psi\circ\theta^{-1}\). Our module convention is
\((\psi x)(a)=\psi(xa)\), \((x\psi)(a)=\psi(ax)\).

**Theorem 5.1.** Let \(M\) be a type III factor with faithful normal state \(\varphi_0\), and suppose \(\theta\) is locally approximately inner. There is a net of contractions \((X_i)\) such that


\[
\begin{gathered}
\varphi_0(X_i^*X_i)\geq\frac d3=\frac1{38400},\\
\|X_i\psi-(\theta\psi)X_i\|\longrightarrow0
\quad(\psi\in M_*).
\end{gathered}
\tag{17}
\]


If \(M_*\) is separable, a sequence has these properties. In particular that sequence does not converge to zero sigma-strongly.

**Proof.** For each nonzero \(\psi\in\mathcal D\), fix a finite \(C_\psi\geq1\) with \(\psi\leq C_\psi\varphi_0\). Given a finite set \(F\) of these functionals, put


\[
\begin{aligned}
w_\psi&=\frac1{\max(1,|F|)C_\psi}\quad(\psi\in F),\\
b_F&=\min\bigl(\{1\}\cup\{\sqrt{w_\psi}:\psi\in F\}\bigr),\\
\Phi_F&=\varphi_0+\sum_{\psi\in F}w_\psi\psi.
\end{aligned}
\]


These definitions also apply when \(F\) is empty. They give


\[
\varphi_0\leq\Phi_F\leq2\varphi_0,
\qquad 1\leq\Phi_F(1)\leq2.
\tag{18}
\]


For an integer \(m\geq1\), apply Theorem 3.1 to the positive vectors


\[
\zeta,\quad \sqrt{w_\psi}\,\xi_\psi\ (\psi\in F),
\qquad \tau=\frac{b_F}{3\sqrt2\,m}\leq1.
\]


Let \(X_{F,m}\) be the resulting contraction. Its aggregate weighted defect is at most \(b_F/m\). Therefore, for every \(\psi\in F\),


\[
\|X_{F,m}\xi_\psi-(\theta\xi_\psi)X_{F,m}\|
\leq\frac{b_F}{m\sqrt{w_\psi}}\leq\frac1m.
\tag{19}
\]


The same bound holds for \(\zeta\). The mass estimate, \(\tau\leq1\), and (18) give


\[
2\varphi_0(X_{F,m}^*X_{F,m})
\geq\Phi_F(X_{F,m}^*X_{F,m})
\geq\frac{2d}{3}\Phi_F(1)\geq\frac{2d}{3}.
\tag{20}
\]


This is a bound in the same fixed state for every \(F,m\).

Order the pairs \((F,m)\) by inclusion of the finite sets and the usual order on the integers. This is directed. For each fixed \(\psi\in\mathcal D\), (19) tends to zero eventually on this directed set. The two-functional estimate AI01 gives


\[
\|X\psi-(\theta\psi)X\|
\leq2\psi(1)^{1/2}
\|X\xi_\psi-(\theta\xi_\psi)X\|.
\tag{21}
\]


Here the representative of \(\theta\psi\) is \(\theta\xi_\psi\), and the sign of the difference in AI01 does not affect its norm. Thus the second line of (17) holds on \(\mathcal D\).

For any two normal functionals \(\rho,\psi\) and any contraction \(X\), the module norm bounds give


\[
\begin{aligned}
\|X\rho-(\theta\rho)X\|
&\leq2\|\rho-\psi\|
+\|X\psi-(\theta\psi)X\|.
\end{aligned}
\tag{22}
\]


The automorphism acts isometrically on the predual because composition maps the operator unit ball bijectively to itself. Lemma 4.1 and (22) extend convergence to every normal positive functional. Every normal functional is a linear combination of four positive ones, with a full proof in CP07; linearity extends it to all of \(M_*\).

If \(M_*\) is separable, choose a countable dense family \((\psi_k)\) in \(\mathcal D\) as in Section 4, omitting zeros. Apply the construction with \(F_n=\{\psi_1,\ldots,\psi_n\}\) and \(m=n\). Equations (19), (21), and (22) prove the required convergence for this sequence. This uses norm density, not a claim that these finite sets are cofinal among all finite subsets of \(\mathcal D\).

Finally, \(x\mapsto\varphi_0(x^*x)^{1/2}\) is one of the sigma-strong seminorms, by CP08. Equation (20) prevents it from tending to zero, completing the proof. \(\square\)

## 6. What the local condition says without a faithful state

Here \(M\) is a factor with no faithful normal state; no type assumption is needed. The local condition (1), by itself, then holds for every automorphism.

We first prove the elementary corner fact required for this statement. If \(r,s\) are nonzero projections in a factor, then \(sMr\ne0\). Otherwise \(sur=0\) for every unitary \(u\in M\). The projection


\[
z=\bigvee_{u\in\mathcal U(M)}uru^*
\]


exists by bounded monotone convergence and finite projection joins, as proved in NW03. Conjugation by any unitary permutes its defining family, so \(z\) commutes with every unitary. The unitary spanning formula makes \(z\) central. Since \(z\geq r\ne0\) and \(M\) is a factor, \(z=1\). But \(sur=0\) implies that \(s\) annihilates the range of every \(uru^*\), and hence the closed span of all those ranges, which is \(zH=H\). This contradicts \(s\ne0\).

Now fix \(\xi_1,\ldots,\xi_n\in P\), and let \(p\) be the support of \(\rho=\sum_j\omega_{\xi_j}\). The bounded support theorem shows that \(\rho\) is faithful on \(pMp\). If \(p=1\), normalization of \(\rho\) would give a faithful normal state on \(M\), contrary to hypothesis. Thus \(p<1\), including \(p=0\) when every vector is zero. Also


\[
(1-p)\xi_j=0,\qquad \xi_j(1-p)=0;
\]


the first equality follows by summing their squared norms to \(\rho(1-p)=0\), and the second follows by applying \(J\).

Both \(r=1-p\) and \(s=1-\theta(p)\) are nonzero. Choose any nonzero \(x\in sMr\), using the corner fact. Then


\[
x\xi_j=0=(\theta\xi_j)x\quad\text{for every }j.
\tag{23}
\]


Thus (1) has a nonzero operator witness with zero mass for every finite family and every tolerance. This observation does not assert that every such automorphism is approximately inner. It identifies precisely why the bare local criterion supplies no mass control in this generality. The fixed faithful state in Theorem 5.1 prevents this zero-mass mechanism.

## 7. Two quantitative checks

**Problem 1.** In the Hilbert–Schmidt standard form of \(M_2(\mathbb C)\), take \(\theta=\mathrm{id}\), \(0<a<1\), and


\[
\xi=\begin{pmatrix}1&a\\a&1\end{pmatrix},
\qquad X=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]


Why is an estimate on diagonal blocks alone insufficient?

**Solution.** The vector \(\xi\) is positive, since its eigenvalues are \(1\pm a\). Pinching by the coordinate projections gives \(\xi^{\mathrm d}=I\), and \([X,\xi^{\mathrm d}]=0\). Nevertheless


\[
[X,\xi]=\begin{pmatrix}0&2a\\-2a&0\end{pmatrix},
\qquad\|[X,\xi]\|_{\mathrm{HS}}^2=8a^2.
\]


Here \(\|\xi-\xi^{\mathrm d}\|_{\mathrm{HS}}^2=2a^2\). The comparison bound \(\|[X,\xi]\|\leq2\|\xi-\xi^{\mathrm d}\|\) is an equality. This is the off-diagonal contribution retained in the last step of Theorem 3.1.

**Problem 2.** Suppose \(\psi_1\leq4\varphi_0\) and \(\psi_2\leq9\varphi_0\). Give the weights and tolerance in the finite-test construction for an error target \(1/m\).

**Solution.** The weights are \(w_1=1/8\), \(w_2=1/18\), so


\[
\Phi_F=\varphi_0+\tfrac18\psi_1+\tfrac1{18}\psi_2
\leq2\varphi_0.
\]


We have \(b_F=1/\sqrt{18}\) and \(\tau=1/(18m)\). Theorem 3.1 gives aggregate weighted defect at most \(1/(\sqrt{18}m)\). Dividing by \(\sqrt{w_j}\) bounds each original vector defect by \(1/m\). Independently of \(m\), (20) gives \(\varphi_0(X_{F,m}^*X_{F,m})\geq1/38400\). A growing unweighted sum of unrelated test functionals would not provide this same fixed-state bound.

**Reference.** M. Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, Lemma 4.11, printed pp.377–379. The sequence conclusion above supplies the bounded, nonvanishing approximate intertwiners used there under separable predual, and the directed version requires only a faithful normal state. The proof separates the orthogonal block identity, the global mass estimate, and the domination by a single state. Turning these contractions into implementing unitaries is a further step; it is not a consequence of strong convergence of the sums alone.
