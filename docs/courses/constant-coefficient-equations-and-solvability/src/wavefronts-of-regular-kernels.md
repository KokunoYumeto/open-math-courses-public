# Wavefronts of regular kernels

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Localization at infinity controls where a fundamental solution can be singular and in which covector directions. There are two different conclusions. The canonical averaging construction has an upper bound determined by the active subspaces of its limiting symbols. Every regular fundamental solution, however chosen, must carry the support of an inverse of each limiting symbol in the corresponding wavefront direction. We prove both statements and keep their quantifiers distinct.

Read [Symbols at infinity](symbols-at-infinity.md) and [Regular kernels and changes in the equation](regular-kernels-and-parameter-changes.md). We use the compactness theorem in [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md), Theorem 4.1. Basic distribution references are Grubb [Grubb] and Melrose [Melrose]; Hörmander's survey [Hormander] discusses the fundamental-solution method.

Our Fourier transform is \(\widehat u(\xi)=\int e^{-ix\cdot\xi}u(x)\,dx\), and \(D=-i\partial\). The wavefront set has its Fourier definition: \((x_0,\theta_0)\notin\operatorname{WF}(u)\) if some smooth compact cutoff equal to one near \(x_0\) has a Fourier transform decreasing faster than every power in an open cone about \(\theta_0\ne0\). We use the usual cutoff stability of this definition and the fact that its projection onto \(x\)-space is the singular support.

For a nonzero polynomial \(P\), let \(S_P\), \(\mathcal L_\theta(P)\), \(N_Q\), and \(V_Q=N_Q^\perp\) have the meanings of the preceding lesson. Let \(\mathcal Z_P\) consist of all pairs \((x,\theta)\), \(\theta\ne0\), for which some \(Q\in\mathcal L_\theta(P)\) satisfies \(x\in V_Q\). Define
\[
\mathcal F_P=\overline{\mathcal Z_P}.
\tag{1}
\]
where closure is in \(\mathbb R^n\times(\mathbb R^n\setminus\{0\})\).

This is a closed conic set. Its projection \(\mathcal F_{P,1}\) onto \(x\)-space is closed: normalize the covectors to length one and use their compactness when a sequence of base points converges. The inactive-direction theorem gives
\[
x\cdot\theta=0\quad\text{on }\mathcal F_P.
\tag{2}
\]
The same equation holds on the closure by continuity.

The holomorphic polynomial averaging used to construct the inverse is the exact planned prerequisite stated in [Regular kernels and changes in the equation](regular-kernels-and-parameter-changes.md). [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md) proves the disk estimates and compact-contour calculus.

## Extracting an inverse from a high-frequency limit

**Theorem 1.1.** Let \(E\) be a regular fundamental solution of \(P(D)\). For every normalized \(Q\in\mathcal L_\theta(P)\) there is a regular fundamental solution \(G\) of \(Q(D)\) such that
\[
\begin{gathered}
\operatorname{supp}G\times\{\theta\}
\subset\operatorname{WF}(E),\\
\operatorname{supp}G\subset\operatorname{sing\,supp}E.
\end{gathered}
\tag{3}
\]
No temperedness of \(E\) is assumed.

**Proof.** Choose centers \(\eta_j\) tending to infinity with directions tending to \(\theta/|\theta|\) and \(T_P(\eta_j)\to Q\). Put
\[
\begin{gathered}
P_j=T_P(\eta_j),\\
E_j=S_P(\eta_j)e^{-ix\cdot\eta_j}E.
\end{gathered}
\tag{4}
\]
The modulation identity and the value of the exponential at zero give
\[
P_j(D)E_j=\delta_0.
\tag{5}
\]

For each \(\chi\in C_c^\infty\), regularity says that
\[
|\widehat{\chi E}(\zeta)|\leq C_\chi/S_P(\zeta).
\]
The moderate shift estimate from the weighted-spaces lesson implies
\[
\begin{aligned}
|\widehat{\chi E_j}(\xi)|
&\leq C_\chi
\frac{S_P(\eta_j)}{S_P(\eta_j+\xi)}\\
&\leq C_\chi'(1+|\xi|)^m.
\end{aligned}
\tag{6}
\]
The constants do not depend on \(j\). The distributions \(\chi E_j\) have a fixed compact support. Apply the compactness theorem with weights
\[
\begin{gathered}
k_2(\xi)=(1+|\xi|)^{-m},\\
k_1(\xi)=(1+|\xi|)^{-m-1}.
\end{gathered}
\tag{7}
\]
Their ratio tends to zero, so a subsequence converges in \(B_{\infty,k_1}\), including uniform convergence of its Fourier transforms on every compact frequency set.

Take cutoffs \(\chi_l\) equal to one on successive compact sets exhausting \(\mathbb R^n\). A diagonal subsequence makes every \(\chi_lE_j\) converge in this weighted space. Distributional convergence makes the limits agree where the cutoffs are one. They define \(G\in\mathcal D'(\mathbb R^n)\), and \(E_j\to G\) locally in distributions. Passing to the limit in (5) is valid because the coefficients of \(P_j\) converge and the differential orders are bounded. Hence \(Q(D)G=\delta_0\).

For any compact cutoff \(\chi\), choose an exhausting cutoff equal to one on its support. Multiplication by \(\chi\) is continuous in \(B_{\infty,k_1}\), so \(\chi E_j\to\chi G\) in that space. Its Fourier transform converges pointwise. Since
\[
\frac{S_P(\eta_j+\xi)}{S_P(\eta_j)}
=S_{P_j}(\xi)\longrightarrow S_Q(\xi),
\tag{8}
\]
the first inequality of (6) gives
\[
|\widehat{\chi G}(\xi)|\leq C_\chi/S_Q(\xi).
\tag{9}
\]
The limit \(G\) is regular.

Suppose \((x_0,\theta)\notin\operatorname{WF}(E)\). Choose a cutoff \(\chi\) equal to one near \(x_0\) with rapid Fourier decrease in a cone about \(\theta\). For \(\xi\) in any fixed compact set, \(\eta_j+\xi\) lies in that cone for large \(j\). Also \(S_P(\eta_j)\leq C(1+|\eta_j|)^m\). Therefore
\[
S_P(\eta_j)\widehat{\chi E}(\eta_j+\xi)
\longrightarrow0
\tag{10}
\]
uniformly on each such set. But this is the Fourier transform of \(\chi E_j\), whose limit is \(\widehat{\chi G}\). Consequently \(\chi G=0\), and \(x_0\notin\operatorname{supp}G\). This proves the first inclusion in (3). Projecting the wavefront set gives the second. \(\square\)

The extraction may select different inverses for different \(Q\). It does not say that all of \(V_Q\) must occur in the wavefront set of an arbitrary regular inverse.

## The canonical upper bound

Fix the averaging construction from the regular-kernels lesson. Its function
\[
A(q,z)=\Phi(q,z)/q(z)
\]
is smooth for nonzero coefficient vectors, has a fixed compact \(z\)-support, and is homogeneous of degree \(-1\) under positive real scaling. The corresponding fundamental solution is
\[
\begin{aligned}
\langle E_\rho(P),\phi\rangle
&=(2\pi)^{-n}\int\!\!\int\\
&\quad\widehat\phi(-\xi-z)A(P_\xi,z)\\
&\quad d\lambda(z)\,d\xi.
\end{aligned}
\tag{11}
\]
where \(P_\xi(w)=P(\xi+w)\). The integrals range over \(\xi\in\mathbb R^n\) and \(z\in\mathbb C^n\). All \(z\)'s lie in a fixed ball. The earlier lemma bounds \(A\) and its coefficient differentials on this compact set.

**Theorem 2.1.** For this fundamental solution,
\[
\begin{gathered}
\operatorname{WF}(E_\rho(P))\subset\mathcal F_P,\\
\operatorname{sing\,supp}E_\rho(P)\subset\mathcal F_{P,1}.
\end{gathered}
\tag{12}
\]

We prove the wavefront inclusion; the singular-support statement then follows by projection.

### A partition whose windows grow slowly

Choose a nonnegative \(\psi\in C_c^\infty(B(0,1))\) of integral one. For \(0<\epsilon<1\), to be chosen below, set
\[
\begin{gathered}
\langle\xi\rangle=(1+|\xi|^2)^{1/2},\\
y_\epsilon(\xi,\eta)
=\langle\xi\rangle^{-n\epsilon}
\psi\big((\eta-\xi)\langle\xi\rangle^{-\epsilon}\big).
\end{gathered}
\tag{13}
\]
Then
\[
\int_{\mathbb R^n}y_\epsilon(\xi,\eta)\,d\eta=1.
\tag{14}
\]
On its support, \(|\eta-\xi|\leq\langle\xi\rangle^\epsilon\). For large \(|\eta|\), the two frequency lengths are comparable, and
\[
\begin{gathered}
|\xi-\eta|\leq C\langle\eta\rangle^\epsilon,\\
|\partial_\xi^\alpha y_\epsilon(\xi,\eta)|
\leq C_\alpha
\langle\eta\rangle^{-(n+|\alpha|)\epsilon}.
\end{gathered}
\tag{15}
\]
To check the derivative estimate, each derivative of the argument of \(\psi\) costs at most \(\langle\xi\rangle^{-\epsilon}\): differentiation of \(\eta-\xi\) gives that factor, while differentiation of the scale gives \(\langle\xi\rangle^{-1}\) times a bounded argument on the support. Further derivatives obey the same bound because \(\epsilon<1\). Differentiating the prefactor only improves it. The support in \(\xi\), for fixed large \(\eta\), has volume at most \(C\langle\eta\rangle^{n\epsilon}\).

Define the smooth function of \(x\)
\[
\begin{aligned}
E_\eta(x)&=(2\pi)^{-n}\int\!\!\int\\
&\quad e^{ix\cdot(\xi+z)}y_\epsilon(\xi,\eta)\\
&\quad\cdot A(P_\xi,z)\,d\lambda(z)\,d\xi.
\end{aligned}
\tag{16}
\]
For fixed \(\eta\), the \(\xi\)-set in this integral is compact. For tests of compact support the rapid decrease of their entire Fourier transforms, uniformly on the compact \(z\)-set, and \(S_P(\xi)\geq c_P>0\) justify Fubini. Equations (11) and (14) give, in distributions,
\[
E_\rho(P)=\int E_\eta\,d\eta.
\tag{17}
\]

### Frequency centers away from the observed cone

Fix \((x_0,\theta_0)\notin\mathcal F_P\). Choose a relatively compact neighborhood \(\Omega\) of \(x_0\), and open cones
\[
\Gamma\Subset\Gamma_a\Subset\Gamma_b\Subset\Gamma_0
\tag{18}
\]
about \(\theta_0\), such that \(\overline\Omega\times\overline{\Gamma_0}\) avoids \(\mathcal F_P\). Closure and compact inclusion of cones here refer to their unit-sphere sections. Put \(K=\overline\Omega\).

Let \(\phi\in C_c^\infty(\Omega)\). When \(\eta\notin\Gamma_b\) is large and \((\xi,\eta)\) belongs to the support of \(y_\epsilon\), (15) implies \(\xi\notin\Gamma_a\). Angular separation then gives
\[
|\tau-\xi|\geq c(|\tau|+|\xi|)
\quad(\tau\in\overline\Gamma).
\tag{19}
\]
The transform of \(\phi E_\eta\) is obtained from (16) by replacing its exponential with \(\widehat\phi(\tau-\xi-z)\). Compact support of \(\phi\) gives arbitrary power decrease in the real part of this argument, uniformly in \(z\). Bound \(A(P_\xi,z)\) by \(C/S_P(\xi)\leq C_P\). Its integral against \(y_\epsilon\) is uniformly bounded, by the amplitude and volume estimates (15). Equation (19) thus gives, for every \(N\),
\[
|\widehat{\phi E_\eta}(\tau)|
\leq C_N(1+|\tau|+|\eta|)^{-N}
\tag{20}
\]
for these large centers. For bounded centers, the \(\xi\)-set is bounded, and the same argument gives arbitrary decrease in \(\tau\) uniformly over that bounded set. Integrating the part with \(\eta\notin\Gamma_b\) therefore gives rapid decrease on \(\Gamma\).

### Derivatives in a direction the nearby symbol loses

The graph approximation theorem in the symbols-at-infinity lesson gives \(b>0\) and, for each sufficiently large \(\eta\in\Gamma_b\), a unit \(\omega_\eta\) and \(Q_\eta\in\mathcal L_{\omega_\eta}(P)\) such that
\[
\begin{gathered}
T_P(\eta)=Q_\eta+R_\eta,\\
|R_\eta|_J\leq C|\eta|^{-b},\\
\left|\omega_\eta-\frac{\eta}{|\eta|}\right|\leq C|\eta|^{-b}.
\end{gathered}
\tag{21}
\]
Increasing the lower bound on \(|\eta|\) ensures \(\omega_\eta\in\Gamma_0\). There is a constant \(\delta>0\) such that
\[
\operatorname{dist}(x,V_{Q_\eta})\geq\delta
\quad(x\in K).
\tag{22}
\]
Indeed, if these distances tended to zero, choose nearest points in \(V_{Q_\eta}\) to points of \(K\), and convergent subsequences of the base points and unit directions. Their limits would lie in \(\mathcal F_P\) and \(K\times\overline{\Gamma_0}\), a contradiction. This uses the closure in (1); no continuity of \(Q\mapsto V_Q\) is needed.

Choose
\[
0<\epsilon<1,\qquad 2m\epsilon\leq b.
\tag{23}
\]
For \(m=0\), only the first inequality is needed. Write \(\partial_t=t\cdot\partial_\xi\) for a real vector \(t\in N_{Q_\eta}\). When \(j\geq1\), \(\partial_t^jQ_\eta=0\). The finite Taylor formula applied to \(R_\eta\), at \(u=\xi-\eta\), gives for \(1\leq j\leq m\)
\[
\begin{aligned}
\left|\partial_t^j P_\xi\right|_J
&\leq C_j S_P(\eta)|t|^j\\
&\quad\cdot|\eta|^{-b}(1+|u|)^{m-j}.
\end{aligned}
\tag{24}
\]
Here the left side is the coefficient norm of the polynomial obtained by differentiating \(P_\xi\) with respect to its center. Higher \(j\)'s give zero. The moderate reverse shift estimate gives
\[
S_P(\eta)\leq
C S_P(\xi)(1+|u|)^m.
\tag{25}
\]
For \(|u|\leq C\langle\eta\rangle^\epsilon\), (23)–(25) imply, for every \(j\geq1\),
\[
\left|\partial_t^j P_\xi\right|_J
\leq C_j S_P(\xi)|t|^j
\langle\eta\rangle^{-j\epsilon}.
\tag{26}
\]
The exponent before using (23) is \(-b+(2m-j)\epsilon\), which is at most \(-j\epsilon\). This is why a power rate in (21) was needed.

Apply the homogeneous-function lemma, Lemma 7.1 of the symbols-at-infinity lesson, to the curve \(s\mapsto P_{\xi+st}\) and the coefficient function \(A(q,z)\), of degree \(-1\). Its constants are uniform on the compact \(z\)-set. Equation (26) gives
\[
\begin{gathered}
|\partial_t^j A(P_\xi,z)|\\
\leq C_j S_P(\xi)^{-1}|t|^j\langle\eta\rangle^{-j\epsilon},
\qquad j\geq0.
\end{gathered}
\tag{27}
\]
For \(j=0\) this is the original averaging bound. Combining with (15) and using \(S_P(\xi)^{-1}\leq C_P\), we obtain
\[
|\partial_t^j(y_\epsilon A)(\xi,\eta,z)|
\leq C_j |t|^j
\langle\eta\rangle^{-(n+j)\epsilon}.
\tag{28}
\]

### Integration by parts and the spatial exclusion

Multiplication of the exponential in (16) by \(t\cdot x\) is its derivative in \(\xi\), up to a factor of \(i\). Integrating by parts \(j\) times in that direction, with no boundary term because the amplitude has compact \(\xi\)-support, gives
\[
\begin{gathered}
|(t\cdot x)^j E_\eta(x)|
\leq C_{K,j}|t|^j\langle\eta\rangle^{-j\epsilon},\\
x\in K.
\end{gathered}
\tag{29}
\]
The factor \(\langle\eta\rangle^{-n\epsilon}\) in (28) is canceled by the support volume. The imaginary part of the exponential is bounded uniformly for \(x\in K\) and \(z\) in its compact set.

The same argument applies after an arbitrary spatial derivative \(\partial_x^\alpha\). It inserts a polynomial \((i(\xi+z))^\alpha\), bounded by \(C_\alpha\langle\eta\rangle^{|\alpha|}\). When integration by parts differentiates this factor \(l\) times, it costs at most \(C|t|^l\langle\eta\rangle^{|\alpha|-l}\), or gives zero. Since \(\epsilon<1\), this is bounded by \(C|t|^l\langle\eta\rangle^{|\alpha|-l\epsilon}\). The full Leibniz sum therefore gives
\[
\begin{aligned}
|(t\cdot x)^j\partial_x^\alpha E_\eta(x)|
&\leq C_{K,\alpha,j}|t|^j\\
&\quad\cdot\langle\eta\rangle^{|\alpha|-j\epsilon}.
\end{aligned}
\tag{30}
\]

For each \(x\in K\), choose a unit \(t\in N_{Q_\eta}\) maximizing \(|t\cdot x|\). It equals the length of the orthogonal projection of \(x\) onto \(N_{Q_\eta}\), namely \(\operatorname{dist}(x,V_{Q_\eta})\). By (22) it is at least \(\delta\). We may choose this vector separately at each point after taking the spatial derivative; we never differentiate that choice. Thus
\[
|\partial_x^\alpha E_\eta(x)|
\leq C_{K,\alpha,j}\delta^{-j}
\langle\eta\rangle^{|\alpha|-j\epsilon}.
\tag{31}
\]
Taking \(j\epsilon>|\alpha|+n\) makes this integrable in \(\eta\). Consequently the integral over the large centers in \(\Gamma_b\) is smooth on \(\Omega\), with every derivative given by its absolutely convergent integral. Bounded centers also give a smooth function there.

Multiply this smooth part by \(\phi\); its transform is rapidly decreasing everywhere. The remaining part is rapidly decreasing in \(\Gamma\) by (20). This proves \((x_0,\theta_0)\notin\operatorname{WF}(E_\rho(P))\), and completes Theorem 2.1. \(\square\)

The proof controls every derivative order by increasing the number of integrations by parts. A single integrable estimate for \(E_\eta\) would establish continuity, but would not establish the required smoothness.

## A regular inverse outside the canonical bound

The restriction to the averaging construction in Theorem 2.1 is essential. In two variables take \(P(\xi)=\xi_1\), so \(P(D)=-i\partial_1\). Then
\[
E=iH(x_1)\otimes\delta_0(x_2)
\tag{32}
\]
is a regular fundamental solution. After any compact cutoff, its transform is independent of \(\xi_2\) and is \(O((1+|\xi_1|)^{-1})\), by one integration by parts on the half-line. This is exactly the regular weight \(S_P(\xi)=\sqrt{1+\xi_1^2}\).

The distribution
\[
w(x_1,x_2)=1\otimes\delta_1(x_2)
\tag{33}
\]
satisfies \(P(D)w=0\) and is regular. Its localized Fourier transform decreases rapidly in \(\xi_1\), uniformly in \(\xi_2\), since its amplitude along \(x_2=1\) is smooth and compactly supported. Thus \(E+w\) is another regular fundamental solution.

For this symbol all \(V_Q\)'s are either \(\{0\}\) or the axis \(x_2=0\), so \(\mathcal F_{P,1}\subset\{x_2=0\}\). Yet \(E+w\) is singular on \(x_2=1\): near that line it equals \(w\), a delta distribution in its normal variable. Its wavefront covectors there are \((0,\theta_2)\), \(\theta_2\ne0\). The universal lower statement of Theorem 1.1 remains valid, while the canonical upper statement need not hold for this choice.

## Exercises with complete solutions

**Exercise 1. A constant limiting symbol.** Suppose \(Q=c\ne0\) belongs to \(\mathcal L_\theta(P)\). What does Theorem 1.1 force at the origin? Apply this to \(P(\xi)=1+|\xi|^2\).

**Solution.** The only fundamental solution of the scalar operator \(c\) is \(G=c^{-1}\delta_0\); multiplication by \(c\) is invertible on distributions. Its support is \(\{0\}\), so \((0,\theta)\in\operatorname{WF}(E)\) for every regular fundamental solution \(E\) of \(P\). For \(1+|\xi|^2\), Exercise 1 of the symbols-at-infinity lesson gives the constant localization \(1\) in every direction. Thus all nonzero covectors occur over the origin. The canonical upper bound has \(\mathcal F_{P,1}=\{0\}\), so its kernel is smooth away from zero.

**Exercise 2. The product symbol.** Compute \(\mathcal F_P\) for \(P(\xi_1,\xi_2)=\xi_1\xi_2\).

**Solution.** In a direction with both components nonzero the normalized limit is a nonzero constant, since the quadratic undifferentiated term has order \(|\eta|^2\) and every derivative has smaller order. Along the second axis the nonconstant limits are nonzero scalar multiples of \(a+\xi_1\), as in Exercise 2 of the preceding lesson; their active subspace is the first axis. Along the first axis the active subspace is the second axis. Constants also occur in the axial directions. These sets are already closed after including the origin for every covector, so
\[
\begin{aligned}
\mathcal F_P={}&\{0\}\times(\mathbb R^2\setminus\{0\})\\
&\cup(\mathbb R e_1)\times(\mathbb R e_2\setminus\{0\})\\
&\cup(\mathbb R e_2)\times(\mathbb R e_1\setminus\{0\}).
\end{aligned}
\tag{34}
\]
Thus the canonical kernel is smooth off the two axes; away from their intersection, only covectors normal to the relevant axis are permitted by this bound.

**Exercise 3. A quantitative derivative calculation.** Let \(m=3\), let the graph approximation error be \(O(|\eta|^{-1/2})\), and choose \(\epsilon=1/16\). Verify (26) for \(j=1,2,3\). For \(n=2\) and a spatial derivative of order four, how many integrations by parts suffice in (31)?

**Solution.** Here \(2m\epsilon=3/8\leq1/2=b\). The unreduced exponent \(-b+(2m-j)\epsilon\) is respectively \(-3/16,-4/16,-5/16\). Each is at most the required \(-j/16\). A derivative of order four is integrable if \(j/16>4+2=6\), so any integer \(j\geq97\) suffices. There is no upper restriction on the number of amplitude differentiations; although the polynomial path has only three nonzero derivative orders, the smooth reciprocal averaging function can be differentiated arbitrarily many times.

**Exercise 4. Why directions must also be approximated.** Explain where the direction estimate in (21) is used, and why coefficient approximation by some \(Q\in\mathcal L(P)\) without a directional restriction is insufficient.

**Solution.** The estimate ensures that, for centers in \(\Gamma_b\), the chosen localization direction belongs to the larger cone \(\Gamma_0\). The exclusion \(K\times\overline{\Gamma_0}\cap\mathcal F_P=\varnothing\) then gives the uniform spatial separation (22). A coefficient approximation with no direction control could choose a localization whose active subspace meets \(K\), giving zero separation and preventing division by \(t\cdot x\). The proof therefore needs the joint graph estimate rather than just distance to \(\mathcal L(P)\).

**Exercise 5. Compactness at the supremum endpoint.** In Theorem 1.1, why is convergence in \(B_{\infty,k_1}\) stronger than just distributional convergence, and which two later steps use that extra information?

**Solution.** The weighted norm gives uniform convergence of Fourier transforms on every compact frequency set. Distributional convergence alone would not give their pointwise values. Pointwise convergence is used in (8)–(9) to pass the regular estimate to \(G\). It is also used after (10), where the same transforms tend locally uniformly to zero on frequency space; identifying this limit with \(\widehat{\chi G}\) proves \(\chi G=0\). The compactness theorem supplies this convergence even for \(p=\infty\), because the weakened weight has a ratio tending to zero.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures on distributions and Fourier analysis. [Author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- **[Melrose]** Richard Melrose, *Introduction to Microlocal Analysis*, distribution and wavefront-set chapters. [MIT notes](https://math.mit.edu/~rbm/iml/).
- **[Hormander]** Lars Hörmander, “On the existence and the regularity of solutions of linear pseudo-differential equations,” *L'Enseignement Mathématique* 17 (1971), 99–163. [e-periodica scan](https://www.e-periodica.ch/digbib/view?pid=ens-001:1971:17::213).
