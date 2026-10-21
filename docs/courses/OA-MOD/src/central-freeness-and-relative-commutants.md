# Central freeness and relative commutants

An automorphism which moves a central sequence must remain outer on every nonzero invariant corner of the central sequence algebra. Merely finding one moved element does not prove this: the algebra may have a center, and the motion might appear to miss a whole central summand. We prove a localized reindexing identity which rules that out. We then show that tracial absorption supplies full matrix units in every corner of each countable relative commutant.

## 1. The finite sequence algebra and the assertions

Throughout, \(M\ne0\) is a factor with separable predual, \(\varphi\) is a faithful normal state, and \(\omega\) is a free ultrafilter on \(\mathbb N\). Use the functional actions

\[
(x\psi)(a)=\psi(ax),\qquad
(\psi x)(a)=\psi(xa),\qquad
[x,\psi]=x\psi-\psi x.
\]

Write

\[
\|x\|_{\varphi,\#}
 =\bigl(\varphi(x^*x)+\varphi(xx^*)\bigr)^{1/2}.
\tag{CFR.1}
\]

The normalization in (CFR.1) is \(\sqrt2\) times the normalized seminorm used in the sequence-algebra prerequisite. Both describe the same bounded strong* topology.

We use the complete construction in [Central sequence algebras and exact lifts, Sections 1–4](https://github.com/KokunoYumeto/open-math-courses-public/blob/main/docs/courses/OA-APPROX/src/central-sequence-algebras-and-exact-lifts.md#2-the-sequence-algebra-and-its-trace). Its definitions are

\[
\begin{aligned}
C_\omega(M)&=\{(x_n)\in\ell^\infty(M):
 \|[x_n,\psi]\|\longrightarrow_\omega0
 \text{ for every }\psi\in M_*\},\\
J_\omega&=\{(x_n)\in C_\omega(M):
 \|x_n\|_{\varphi,\#}\longrightarrow_\omega0\},\\
F=M_\omega&=C_\omega(M)/J_\omega,\qquad
\pi_\omega:C_\omega(M)\longrightarrow F.
\end{aligned}
\tag{CFR.2}
\]

The earlier theorem proves that \(F\) is already a finite von Neumann algebra and that

\[
\tau(\pi_\omega(x_n))
 =\lim_{n\to\omega}\varphi(x_n)
\tag{CFR.3}
\]

is its faithful normal tracial state. Every bounded centralizing sequence has a scalar ultraweak ultralimit, which makes (CFR.3) independent of the chosen normal state. Contractions have contraction representatives, and projections have exact projection representatives. No assertion that \(F\) is a factor is part of this input.

Every normal automorphism \(\alpha\) induces the normal trace-preserving automorphism

\[
\alpha_\omega(\pi_\omega(x_n))
 =\pi_\omega(\alpha(x_n)).
\tag{CFR.4}
\]

For completeness, the identity

\[
[\alpha(x),\psi]
 =[x,\psi\circ\alpha]\circ\alpha^{-1}
\tag{CFR.5}
\]

preserves \(C_\omega(M)\); bounded strong* continuity preserves \(J_\omega\). Scalar ultraweak limits give trace preservation. For an increasing bounded positive net \(X_i\uparrow X\), let \(Y=\sup_i\alpha_\omega(X_i)\le\alpha_\omega(X)\). Normality and faithfulness of \(\tau\) imply

\[
\tau(\alpha_\omega(X)-Y)
 =\tau(X)-\sup_i\tau(X_i)=0.
\]

Thus \(\alpha_\omega(X)=Y\). This proves normality directly, and the same argument applies to its inverse.

Call \(\alpha\) **centrally trivial** if

\[
\alpha(x_n)-x_n\longrightarrow0\quad\text{strongly*}
\tag{CFR.6}
\]

for every bounded ordinary centralizing sequence. Denote this class by \(\operatorname{Cnt}(M)\).

We prove three assertions.

1. \(\ker(\alpha\mapsto\alpha_\omega)=\operatorname{Cnt}(M)\), independently of \(\omega\).
2. If \(\alpha\notin\operatorname{Cnt}(M)\), then \(\alpha_\omega\) is properly outer. More precisely, there is no nonzero \(a\in F\) such that

   \[
   aX=\alpha_\omega(X)a\qquad(X\in F).
   \tag{CFR.7}
   \]

   Its restriction to any nonzero invariant corner is not inner.
3. If \(M\cong M\bar\otimes R\), where \(R\) is the tracial binary product, then for every countable self-adjoint subset \(\mathcal S\subset F\), every nonzero corner of \(\mathcal S'\cap F\) contains a unital copy of \(M_2(\mathbb C)\). In particular this relative commutant is finite of type II, with its center retained.

The first two assertions require no tracial-absorption hypothesis. The third has no hypothesis on an automorphism.

Besides (CFR.2), we use the bounded centralizing-sequence estimates, ECA02, faithful-state control of the bounded strong* topology, CDS02, and the complete tracial absorption criterion, CTA03.

## 2. The kernel does not depend on the ultrafilter

Fix a sequence \((\psi_j)\) norm dense in the normal state space. Its complex linear span is norm dense in \(M_*\), by the positive decomposition in CP07. Thus uniformly bounded sequences centralize every normal functional if they centralize all \(\psi_j\). The estimate used in passing to the dense set is

\[
\|[x,\psi-\eta]\|\le2\|x\|\|\psi-\eta\|.
\tag{CFR.8}
\]


Suppose first that \(\alpha_\omega=\operatorname{id}\), but (CFR.6) fails for an ordinary centralizing sequence \(x_n\). Faithful-state control of bounded strong* convergence gives a subsequence \(x_{k(n)}\) and \(\varepsilon>0\) with

\[
\|\alpha(x_{k(n)})-x_{k(n)}\|_{\varphi,\#}
 \ge\varepsilon\qquad(n\ge1).
\tag{CFR.9}
\]

The subsequence is still ordinary centralizing, hence belongs to \(C_\omega(M)\). Its difference in (CFR.9) does not belong to \(J_\omega\). This contradicts \(\alpha_\omega=\operatorname{id}\).

Conversely, suppose \(\alpha\in\operatorname{Cnt}(M)\). If a representative \(x=(x_n)\in C_\omega(M)\) had
\(\alpha_\omega(\pi_\omega x)\ne\pi_\omega x\), then for some \(\varepsilon>0\) the set

\[
A=\{n:\|\alpha(x_n)-x_n\|_{\varphi,\#}>\varepsilon\}
\tag{CFR.10}
\]

would belong to \(\omega\). For each \(r\), the set

\[
A\cap\bigcap_{j\le r}
 \{n:\|[x_n,\psi_j]\|<1/r\}
\]

belongs to \(\omega\), so is infinite. Choose an increasing \(k(r)\) in these sets. The sequence \(x_{k(r)}\) is ordinary centralizing by (CFR.8), but its difference under \(\alpha\) stays larger than \(\varepsilon\). This contradicts central triviality.

We have proved the kernel identity. Composition in (CFR.4) is exact, so this kernel is a normal subgroup of \(\operatorname{Aut}(M)\). It contains every inner automorphism: ECA02 proves that a bounded centralizing sequence commutes strongly* with each fixed implementing unitary. Both the kernel and this conclusion are independent of the free ultrafilter.

This proof distinguishes an ordinary subsequence from an arbitrary reindexing of an \(\omega\)-central sequence. The latter need not remain centralizing. We used finite intersections of \(\omega\)-large sets when the original sequence was only centralizing along \(\omega\).

## 3. A scalar amount of motion

Assume \(\alpha\notin\operatorname{Cnt}(M)\). We first produce self-adjoint contractions \(y_k\), centralizing in the ordinary sense, for which

\[
d_k=\alpha(y_k)-y_k=d_k^*,\qquad
d_k^2\longrightarrow t1\quad\text{ultraweakly},
\qquad t>0.
\tag{CFR.11}
\]


Start with a bounded ordinary centralizing sequence violating (CFR.6). If \(b=a+ic\), with \(a,c\) self-adjoint, then

\[
b^*b+bb^*=2(a^2+c^2).
\tag{CFR.12}
\]

Apply this to the difference under \(\alpha\). After choosing a subsequence, one of the real and imaginary parts has a fixed positive lower bound for its squared \(\varphi\)-seminorm. Real and imaginary parts remain centralizing. A fixed scalar rescaling therefore gives self-adjoint contractions \(y_k\) and \(\delta>0\) such that

\[
\varphi(d_k^2)\ge\delta\qquad(k\ge1).
\tag{CFR.13}
\]

Since \(\|d_k\|\le2\), these numbers lie in \([\delta,4]\). Pass to an ordinary subsequence on which they converge to some \(t\ge\delta\).

The sequence \(d_k^2\) is bounded and centralizing. Indeed fixed automorphisms preserve centralizing sequences by (CFR.5), and such sequences form a *-algebra by ECA02.

Every ultraweak cluster point of \(d_k^2\) is scalar. To see this, let \(b\) be such a cluster point. Passing the functional commutators to their scalar pairings gives \([b,\psi]=0\) for every \(\psi\in M_*\). Evaluating at arbitrary \(a\in M\) gives
\(\psi(ab-ba)=0\) for every normal functional. These separate points by CP04–06, so \(b\in Z(M)=\mathbb C1\). Since \(\varphi(d_k^2)\to t\), that scalar is \(t\).

The bounded operator ball is ultraweakly compact. A net in a compact space whose only cluster point is \(t1\) converges to \(t1\): otherwise a subnet lying outside one neighborhood has a cluster point outside that neighborhood. Apply this to the sequence. This proves (CFR.11), including ordinary ultraweak convergence, rather than convergence only along a chosen ultrafilter.

The factor hypothesis enters exactly in making the energy \(d_k^2\) tend to a scalar. This will make its motion visible in every nonzero quotient corner.

## 4. Reindexing with a prescribed corner

**Localized reindexing lemma.** Fix a countable set \(X_1,X_2,\ldots\in F\) and a nonzero projection \(E\in F\). There is a self-adjoint contraction \(Y\in F\) such that

\[
[Y,X_j]=0\quad(j\ge1),\qquad [Y,E]=0,
\tag{CFR.14}
\]

and, writing \(D=\alpha_\omega(Y)-Y\),

\[
\tau(ED^2)=t\,\tau(E)>0,
\tag{CFR.15}
\]

where \(t\) is the fixed number in (CFR.11).

Choose bounded representatives \(x_j(n)\) and an exact projection representative \(e_n\) of \(E\). The latter exists by the fully proved projection-lifting lemma in the sequence-algebra prerequisite. Add \(E\) to the countable list if necessary.

For each fixed coordinate \(n\), the operators
\(x_1(n),\ldots,x_n(n),e_n\) are fixed elements of \(M\). Because \(y_k\) is ordinary centralizing, ECA02 gives

\[
[y_k,x_j(n)]\longrightarrow0,\qquad
[y_k,e_n]\longrightarrow0
\quad\text{strongly* as }k\to\infty.
\tag{CFR.16}
\]

Also, the map \(b\mapsto\varphi(e_nbe_n)\) is a fixed normal functional. Equation (CFR.11) therefore gives

\[
\varphi(e_nd_k^2e_n)\longrightarrow t\varphi(e_n).
\tag{CFR.17}
\]


Choose \(k(n)\ge n\), increasing if desired, so that

\[
\begin{aligned}
\|[y_{k(n)},x_j(n)]\|_{\varphi,\#}&<1/n
 &&(j\le n),\\
\|[y_{k(n)},e_n]\|_{\varphi,\#}&<1/n,\\
|\varphi(e_nd_{k(n)}^2e_n)-t\varphi(e_n)|&<1/n.
\end{aligned}
\tag{CFR.18}
\]

All tests at coordinate \(n\) are finite in number, so (CFR.16)–(CFR.17) permit this choice. The sequence \(y_{k(n)}\) is ordinary centralizing, since \(k(n)\to\infty\). Set

\[
Y=\pi_\omega(y_{k(n)}).
\]

The first two lines of (CFR.18) prove (CFR.14). The last gives

\[
\begin{aligned}
\tau(ED^2E)
 &=\lim_{n\to\omega}\varphi(e_nd_{k(n)}^2e_n)\\
 &=t\lim_{n\to\omega}\varphi(e_n)
 =t\tau(E).
\end{aligned}
\tag{CFR.19}
\]

Traciality identifies \(\tau(ED^2E)=\tau(ED^2)\). Faithfulness and \(E\ne0\) make this strictly positive.

The representative \(e_n\) varies with \(n\), but the convergence in (CFR.17) is used only after \(n\) has been fixed. Thus the proof does not replace ultraweak convergence by an unjustified estimate against a moving normal functional.

## 5. Proper outerness and asymptotic periods

Suppose \(a\in F\), \(a\ne0\), satisfied (CFR.7). Let \(E=s(aa^*)\) be the support projection of \(aa^*\). Apply Section 4 with the countable list containing \(a\) and \(E\). For its \(Y\),

\[
\alpha_\omega(Y)a=aY=Ya,
\]

so \(Da=0\), where \(D=\alpha_\omega(Y)-Y=D^*\). Hence \(Daa^*=0\), and the spectral support limit gives \(DE=0\). Explicitly,
\(aa^*(aa^*+\varepsilon)^{-1}\to E\) strongly and every such operator is killed by \(D\). It follows that

\[
\tau(ED^2)=\tau(ED^2E)=0,
\]

contradicting (CFR.15). Thus every intertwiner in (CFR.7) is zero.

We also verify the invariant-corner formulation directly, without assuming \(F\) is a factor. Suppose \(E\ne0\), \(\alpha_\omega(E)=E\), and the restriction to \(EFE\) were implemented by a unitary \(v\in EFE\), so

\[
\alpha_\omega(X)=vXv^*\qquad(X\in EFE).
\tag{CFR.20}
\]

Choose \(Y\) from Section 4 commuting with \(E\) and \(v\). Since \(EYE\in EFE\),

\[
E\alpha_\omega(Y)E
 =\alpha_\omega(EYE)=v(EYE)v^*=EYE.
\]

Both \(Y\) and \(\alpha_\omega(Y)\) commute with \(E\), because \(Y\) commutes with \(E\) and \(\alpha_\omega(E)=E\). Consequently \(DE=0\), again contradicting (CFR.15). There is no inner restriction to any nonzero invariant corner. In particular there is no inner restriction to a nonzero invariant central summand: \(\alpha_\omega\) is properly outer.

Conversely, if \(\alpha\in\operatorname{Cnt}(M)\), then Section 2 makes \(\alpha_\omega\) the identity on the nonzero algebra \(F\). It is implemented by \(1\), hence is not properly outer. We have proved

\[
\alpha\notin\operatorname{Cnt}(M)
\quad\Longleftrightarrow\quad
\alpha_\omega\text{ is properly outer}.
\tag{CFR.21}
\]


The set

\[
\{k\in\mathbb Z:\alpha^k\in\operatorname{Cnt}(M)\}
\]

is a subgroup of \(\mathbb Z\), by Section 2. If it is nonzero, let \(p_a(\alpha)\) be its least positive element; otherwise put \(p_a(\alpha)=0\). The kernel identity and (CFR.21), applied separately to each power, give

\[
p_a(\alpha)=0
\quad\Longleftrightarrow\quad
\alpha_\omega^k\text{ is properly outer for every }k\ne0.
\tag{CFR.22}
\]

This is central freeness of the induced integer action. It holds for one free ultrafilter exactly when it holds for every free ultrafilter.

The outer period instead uses powers lying in \(\operatorname{Int}(M)\). Since \(\operatorname{Int}(M)\subseteq\operatorname{Cnt}(M)\), (CFR.22) implies that no nonzero power is inner. The converse is not supplied by that inclusion and is not used here.

## 6. Matrix units in every relative corner

Assume now

\[
M\cong M\bar\otimes R.
\tag{CFR.23}
\]

CTA03's complete absorption criterion supplies an ordinary centralizing sequence of full halving partial isometries \(v_k\). Define

\[
f_{12}(k)=v_k,\quad f_{21}(k)=v_k^*,\quad
f_{11}(k)=v_kv_k^*,\quad f_{22}(k)=v_k^*v_k.
\tag{CFR.24}
\]

These are full \(2\)-by-\(2\) matrix units at every coordinate. They are all centralizing, by the *-algebra property in ECA02, and commute strongly* with each fixed element of \(M\).

Let \(\mathcal S=\{X_1,X_2,\ldots\}\subset F\) be closed under adjoints, choose bounded representatives \(x_j(n)\), and let \(E\ne0\) be a projection in

\[
C=\mathcal S'\cap F.
\]

The self-adjointness of the set makes \(C\) a von Neumann algebra. Choose an exact projection representative \(e_n\) of \(E\).

For each \(n\), choose \(k(n)\ge n\) so late that

\[
\begin{aligned}
\|[f_{ab}(k(n)),x_j(n)]\|_{\varphi,\#}&<1/n
 &&(j\le n,\ 1\le a,b\le2),\\
\|[f_{ab}(k(n)),e_n]\|_{\varphi,\#}&<1/n
 &&(1\le a,b\le2).
\end{aligned}
\tag{CFR.25}
\]

The tests at each coordinate are finite. Ordinary centrality provides their simultaneous satisfaction. Set

\[
F_{ab}=\pi_\omega(f_{ab}(k(n))).
\]

They remain exact full matrix units, lie in \(C\), and commute with \(E\). Therefore

\[
G_{ab}=EF_{ab}
\tag{CFR.26}
\]

are matrix units in \(ECE\) with

\[
G_{11}+G_{22}=E.
\]

They are nonzero. If one diagonal unit vanished, the identities
\(G_{12}G_{21}=G_{11}\) and \(G_{21}G_{12}=G_{22}\) would force both diagonal units to vanish, contrary to \(E\ne0\).

In particular \(ECE\) is noncommutative: its two nonzero orthogonal diagonal units are the distinct products \(G_{12}G_{21}\) and \(G_{21}G_{12}\). Thus \(C\) has no nonzero abelian projection. It is finite, since the faithful normal finite trace of \(F\) restricts to it. A finite von Neumann algebra with no nonzero abelian projections is of type II. This gives the stated conclusion with arbitrary center.

If \(P\subset F\) has separable predual, it has a countable set generating it as a von Neumann algebra. Here is the needed countability argument. On its ultraweakly compact unit ball, choose a norm-dense sequence \((\eta_j)\) in the unit ball of \(P_*\). The metric

\[
d(x,y)=\sum_{j=1}^{\infty}2^{-j}|\eta_j(x-y)|
\]

gives the ultraweak topology there: norm density and the uniform bound \(\|x-y\|\le2\) identify convergence against all normal functionals with convergence against the \(\eta_j\). A compact metric space has a countable dense subset, obtained by taking a finite \(1/n\)-net for each \(n\). Adjoin the adjoints of this subset. Its commutant is ultraweakly closed and equals \(P'\cap F\), so the preceding conclusion applies. The dual-space and normal-functional identifications used here are CP04–06.

One can also obtain countably many mutually commuting full \(M_2\) systems inside \(C\): at each finite stage add all preceding matrix units to the countable list and repeat (CFR.25) with \(E=1\). For the type II assertion, the stronger fact needed was that every nonzero corner admits a full system, already proved in (CFR.26).

## 7. Exact models and necessary hypotheses

**A finite factor has scalar central sequence algebra.** Let \(M=M_d(\mathbb C)\). For matrix units \(e_{ij}\),

\[
\frac1d\sum_{i,j}e_{ji}xe_{ij}
 =\operatorname{tr}_d(x)\,1.
\tag{CFR.27}
\]

Subtracting \(x\) gives the finite sum
\(d^{-1}\sum e_{ji}[x,e_{ij}]\). A bounded centralizing sequence commutes strongly* with every \(e_{ij}\). In finite dimension strong* convergence agrees with norm convergence, so its distance from the scalar matrices tends to zero, also along \(\omega\). Bounded scalar sequences have scalar ultralimits. Hence \(M_\omega=\mathbb C\), and every automorphism is centrally trivial. Section 6 does not apply: a finite matrix algebra does not absorb \(R\), since that would supply a noncommutative central sequence algebra.

**Moving one central component is insufficient without factoriality of \(M\).** Take \(M=\mathbb C^3\) and let

\[
\alpha(z_1,z_2,z_3)=(z_2,z_1,z_3).
\tag{CFR.28}
\]

Every bounded sequence is centralizing. Coordinatewise compactness identifies its ultrafilter quotient with \(\mathbb C^3\), and the induced automorphism is (CFR.28). It moves \((1,0,0)\), so is not centrally trivial, but it is the identity on the third nonzero central corner. Thus (CFR.21) fails if the original factor hypothesis is dropped. In this example the motion has zero mass in that third corner; it cannot satisfy (CFR.15).

**A periodic centrally free generator need not have centrally free powers.** On the tracial binary product \(R\), take the automorphism \(\beta_{-1}\) from ECA01 and ECA08. On each leg it is implemented by \(\operatorname{diag}(-1,1)\). The tail sequence

\[
y_n=e_{12}^{(n)}+e_{21}^{(n)}
\]

is self-adjoint, unitary and centralizing, while

\[
\beta_{-1}(y_n)=-y_n,\qquad
(\beta_{-1}(y_n)-y_n)^2=4\,1.
\tag{CFR.29}
\]

Thus \(p_a(\beta_{-1})=2\). Its induced automorphism is properly outer, but its square is the identity. Testing only the first power would not prove (CFR.22).

**Why reindexing matters.** In that same model put \(X=\pi_\omega(e_{11}^{(n)})\). Using \(y_n\) at the same coordinate gives

\[
[y_n,e_{11}^{(n)}]
 =e_{21}^{(n)}-e_{12}^{(n)},\qquad
\|[y_n,e_{11}^{(n)}]\|_{2}=1.
\tag{CFR.30}
\]

It does not commute with \(X\) in the quotient. For this one specified sequence, using \(y_{2n}\) instead gives exact commutation because the two legs differ. If \(E=X\), then \(\tau(E)=1/2\), and (CFR.29) gives

\[
\tau\!\left(E(\beta_{-1,\omega}(\pi_\omega(y_{2n}))
                    -\pi_\omega(y_{2n}))^2\right)=2
 =4\,\tau(E).
\tag{CFR.31}
\]

For a general countable family of moving representatives, a predetermined shift such as \(2n\) need not work. The finite tests in (CFR.18) choose the reindexing from the actual family.

## 8. From central freeness to towers and cocycles

Let \(\gamma=\alpha_\omega\) and suppose \(p_a(\alpha)=0\). The factor \(M\) still has separable predual. The algebra \(F=M_\omega\) has its faithful normal tracial state \(\tau\), but may have a center and may have nonseparable predual. Sections 1 and 5 prove that every nonzero power of \(\gamma\) is properly outer. These are exactly the hypotheses of the following earlier programme theorem.

**The finite-algebra input.** Cyclic towers in finite algebras, Theorem 1.1 proves that for every integer \(n\ge1\) and every \(\varepsilon>0\), there is a projection partition \(Q_0,\ldots,Q_{n-1}\) of \(1\) in \(F\) with

\[
\|\gamma(Q_j)-Q_{j+1}\|_{2,\tau}<\varepsilon,
\qquad j\in\mathbb Z/n\mathbb Z.
\tag{CFR.32}
\]

Its proof in Sections 2–6 includes the proper-outerness cutting argument, orthogonalization of orbit projections, the small-cycle construction, maximal filling, and the decomposition over periodic and aperiodic parts of the center. Thus it applies to this finite algebra, without a factor or separability assumption on \(F\). No equality of the traces of the approximate levels is assumed.

**Exact relative towers.** Central towers and unitary cocycles, Theorem 3.1 proves that if \(P\subset F\) has separable predual, then there are projections

\[
\begin{gathered}
E_0+\cdots+E_{n-1}=1,\\
E_jE_k=0\quad(j\ne k),\\
E_j\in P'\cap F,\\
\gamma(E_j)=E_{j+1}.
\end{gathered}
\tag{CFR.33}
\]

There is no invariance condition on \(P\). To identify the precise proof used, its Section 3 first applies (CFR.32), lifts each approximate partition to an exact coordinate partition using the partition-lifting theorem, Section 6, and chooses a new coordinate in each approximation row. At each step the finitely many representatives of \(P\) are fixed while the row coordinate is chosen. This yields exact covariance and relative commutation in the quotient. The cited section contains that complete selection argument, rather than an appeal to the definition of asymptotic period.

Because \(\tau\circ\gamma=\tau\), all the traces in (CFR.33) are equal. Their sum is one, so

\[
\tau(E_j)=1/n.
\tag{CFR.34}
\]

Neither (CFR.32) nor (CFR.33) requires \(M\cong M\bar\otimes R\). Strong stability was used in Section 6 to place full matrix units in every relative corner; it is not an extra hypothesis for these tower conclusions.

**The prescribed unitary equation.** Central towers and unitary cocycles, Theorem 5.1 proves

\[
\text{for every }u\in\mathcal U(F),\quad
\text{there is }v\in\mathcal U(F)
\text{ with }\gamma(v)=uv.
\tag{CFR.35}
\]

The complete proof occupies its Sections 4–5. Section 4 uses a tower commuting with \(u\) and a corner recursion to produce a unitary \(V\) satisfying

\[
\|\gamma(V)-uV\|_{2,\tau}\le2/\sqrt n.
\tag{CFR.36}
\]

Only the closing level contributes to this error, and it has trace \(1/n\). Section 5 lifts unitaries by Section 5 of the lifting prerequisite, with both endpoints equal to \(1\), and selects the approximation row along decreasing sets belonging to \(\omega\). The representative \(u_k\) of the given unitary retains its original coordinate. Reindexing \(u_k\) at that step could change \(u\) and would prove a different equation. The trace-null criterion then makes the error vanish strongly*, including its adjoint. These are exact earlier programme proofs of (CFR.35), with (CFR.36) as their intermediate estimate.

**Left cocycles and the adjoint convention.** A left cocycle for \(\gamma\) is a family of unitaries satisfying

\[
 w_{r+s}=w_r\gamma^r(w_s),\qquad
 w_0=1\quad(r,s\in\mathbb Z).
\tag{CFR.37}
\]

Set \(a=w_1\). Apply (CFR.35) to \(u=a^*\). Since \(\gamma(v)=a^*v\), adjointing gives \(\gamma(v^*)=v^*a\), and therefore

\[
 a=v\gamma(v^*).
\tag{CFR.38}
\]

For a positive integer \(r\), repeated use of (CFR.37) gives the ordered product

\[
 w_r=a\gamma(a)\cdots\gamma^{r-1}(a)
     =v\gamma^r(v^*).
\tag{CFR.39}
\]

The last equality follows by cancelling each adjacent pair \(\gamma^j(v^*)\gamma^j(v)=1\); it does not reorder noncommuting factors. Also (CFR.37) with \(s=-r\) gives \(w_{-r}=\gamma^{-r}(w_r^*)\). Substitution in (CFR.39) proves the same formula for negative \(r\), and it holds at zero. Thus every left cocycle is a coboundary. In the original equation (CFR.35), the left-cocycle generator is \(u^*\), not \(u\).

In particular the cocycle perturbation is conjugate to the original quotient action by an inner automorphism:

\[
 \operatorname{Ad}(a)\circ\gamma
 =\operatorname{Ad}(v)\circ\gamma
      \circ\operatorname{Ad}(v^*).
\tag{CFR.40}
\]

Indeed, its right side sends \(x\) to
\(v\gamma(v^*)\gamma(x)\gamma(v)v^*=a\gamma(x)a^*\), by (CFR.38). This is a conclusion about automorphisms of \(F\). It does not assert that an arbitrary unitary cocycle in \(M\) itself has an exact coboundary there.

**A finite-period check.** The all-powers hypothesis cannot be replaced by proper outerness of the generator. If \(\gamma^p=\mathrm{id}\) and \(\gamma(v)=zv\) for a scalar \(z\in\mathbb T\), iteration gives \(v=z^pv\), hence \(z^p=1\). For the period-two quotient action in Section 7, the unitary \(u=i1\) consequently has no solution in (CFR.35), although \(\gamma\) itself is properly outer. This makes the role of \(p_a(\alpha)=0\) visible in the equation.

The subsequent outer-conjugacy construction for approximately inner automorphisms is written in Comparing asymptotically aperiodic automorphisms. It uses additional finite-model, perturbation and tensor-splitting arguments. Equations (CFR.32)–(CFR.40) supply the tower and cohomology part of that route; they are not a substitute for those further proofs.

## Source

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVII, Section 2, Lemmas 2.1–2.2, printed pp.261–262. The proof here supplies explicit localization in every nonzero quotient corner, excludes all nonzero intertwiners, and shows that the central-freeness assertion itself does not require strong stability. The approximate-inner outer-conjugacy theorem appears in Section 3, Theorem 3.1, printed pp.270–282; its strong-aperiodicity hypothesis is the condition in (CFR.22).
