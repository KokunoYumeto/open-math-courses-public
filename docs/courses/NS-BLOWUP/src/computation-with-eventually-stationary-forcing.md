# Computation with a force that becomes stationary

*NS-BLOWUP N8.1. Exposition by GPT-6 Astra (OpenAI). This independent exposition is dedicated to CC0.*

The preceding lessons construct a singular solution with smooth forcing. Here we use the same forced equations for a different purpose: construct an explicit global smooth solution whose material particle records an arbitrary finite machine and input. The force becomes stationary after time one. Whether one specified particle ever reaches one fixed open set is exactly the machine’s halting question.

The construction proceeds from a finite instruction table to a reversible recorder, from its tape to two exact radix coordinates, and from each instruction to a compact divergence-free motion. A third spatial coordinate supplies the clock. The full Navier–Stokes residual then supplies the force at the prescribed viscosity. Each of these maps is proved below. No simulation or decision about whether the machine halts is needed to construct the force.

This lesson proves OpenAI’s [*Universal Computation with Eventually Stationary Navier–Stokes Forcing*](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/build/main.tex), with its original seven instruction rows, coordinate rectangles, detector and clock. ST1–ST7 contain the entire construction and theorem proof. ST8 treats the stated slow clock and its exact consequences. ST9 contains five solved exercises, including a finite-time detector tolerance and sharp time-integrability thresholds for those same clocks. The separate constructions with rapidly decreasing forcing and velocity-field detection have their own later lessons.

Fix \(\nu>0\), the flat torus \(\mathbb T^3=\mathbb R^3/\mathbb Z^3\), and
\[
P=(1/4,1/4,0),\qquad
\mathcal O=\{(X,Y,Z):1/32<Y<1/8\}.
\tag{ST0.1}
\]
Given a deterministic Turing machine and finite word, we construct a smooth force, with zero spatial mean, that is stationary for \(t\ge1\). Its zero-data Navier–Stokes solution is global, smooth, bounded in kinetic energy, and unique in the classical class. The material particle from \(P\) enters \(\mathcal O\) if and only if the machine halts. Every mixed force derivative is bounded. A finite program evaluates those derivatives and their bounds when \(\nu\) is computable; the same formulas are effective relative to a name for any other fixed positive \(\nu\).

The equation and pressure convention are
\[
U_t+(U\cdot\nabla)U=-\nabla p+\nu\Delta U+f,
\qquad \nabla\cdot U=0,\quad U(0)=0,\quad\int_{\mathbb T^3}p=0.
\tag{ST0.2}
\]
Here classical means that \(U,U_t,D_xU,D_x^2U,p,\nabla p\) are continuous on every closed finite time cylinder. All fields constructed below are smooth. Exact observation is essential: the result supplies no fixed tolerance for an indefinitely long computation. ST8 also proves two editorial consequences, retaining every coefficient: a family of slower clocks with explicit time integrability, and a strictly positive work requirement for the stationary force. Neither is a claim of novelty.

![The original detector, tracked corridor, spatial clock and force map.](../assets/eventually-stationary-computation.svg)

The [figure generator](../assets/eventually-stationary-computation.py) supplies the editable diagram. The coordinate panel shows the exact fixed sets, not a sampled fluid trajectory.

## ST1. Effective smooth functions and the exact fluid receiver

Retain
\[
E(t)=\begin{cases}e^{-1/t},&t>0,\\0,&t\le0,\end{cases}
\qquad \beta(t)=\frac{E(t)}{E(t)+E(1-t)}.
\tag{ST1.1}
\]
If \(E^{(j)}(t)=P_j(1/t)e^{-1/t}\) for \(t>0\), differentiation gives
\[
P_0(y)=1,\qquad P_{j+1}(y)=y^2\big(P_j(y)-P_j'(y)\big).
\tag{ST1.2}
\]
For nonnegative integers \(m,k\), the exponential series implies
\(y^me^{-y}\le(m+k)!y^{-k}\). Thus every derivative tends to zero at the origin, with a computable modulus. For a global derivative bound use \(y^me^{-y}\le m!\) term by term in the finite polynomial. At least one of \(t,1-t\) is at least \(1/2\), so the denominator in ST1.1 is at least \(e^{-2}\). Repeated quotient differentiation gives effective derivative bounds for \(\beta\), including all endpoint derivatives. It is zero on \(( -\infty,0]\), one on \([1,\infty)\), and
\[
\beta(t)+\beta(1-t)=1.
\tag{ST1.3}
\]
Evaluation at a computable real does not require deciding whether that real equals an endpoint: use a rational enclosure and the derivative bounds to control evaluation error; near zero the preceding vanishing estimate controls the entire uncertain contribution.

For \(a<b<c<d\),
\[
\beta\!\left(\frac{t-a}{b-a}\right)
\beta\!\left(\frac{d-t}{d-c}\right)
\tag{ST1.4}
\]
is one on \([b,c]\) and zero off \((a,d)\). Products over coordinates give the required rational-box cutoffs. Finite products and compositions retain explicit computable bounds by Leibniz' rule and the chain rule.

A compactly supported smooth profile \(F_0\) on \((0,1)\), extended by zero, can be periodized effectively without taking the integer part of a computable real. Given \(|q-s|<1\) with rational \(q\), use
\[
F_{\rm per}^{(j)}(s)=
\sum_{k=\lfloor q\rfloor-2}^{\lceil q\rceil+2}F_0^{(j)}(s-k).
\tag{ST1.5}
\]
Every nonzero summand has \(k\in[s-1,s]\), which is contained in the displayed finite range. Coordinate products give the same procedure for compact spatial charts. All floors and ceilings are applied to rationals.

For any explicitly supplied smooth, divergence-free periodic velocity \(U\) vanishing initially, define
\[
\mathcal R_\nu[U]=U_t+(U\cdot\nabla)U-\nu\Delta U.
\tag{ST1.6}
\]
Then \((U,0)\) satisfies ST0.2 by substitution. To prove uniqueness, let \((v,p)\) be another classical solution with the same force and datum and put \(w=v-U\). The exact difference equation is
\[
w_t+(v\cdot\nabla)w+(w\cdot\nabla)U-\nu\Delta w+\nabla p=0.
\tag{ST1.7}
\]
Periodicity and zero divergence remove the integrated transport and pressure terms. Therefore
\[
\frac12\frac d{dt}\|w\|_2^2+\nu\|\nabla w\|_2^2
=-\int_{\mathbb T^3}w\cdot (w\cdot\nabla)U
\le\|\nabla U\|_{\mathrm{op},\infty}\|w\|_2^2.
\tag{ST1.8}
\]
On \([0,T]\) the coefficient is finite. Multiplication by \(\exp(-2\int_0^t\|\nabla U\|_{\mathrm{op},\infty})\) proves \(w=0\). The equation then makes \(\nabla p=0\), and the imposed mean gives \(p=0\). This proves uniqueness for every finite \(T\), hence on the whole half-line. Smooth periodic velocities are bounded and Lipschitz on each such cylinder, so their material ODEs have unique solutions on it and continue through every finite time. Finally
\[
\int\mathcal R_\nu[U]=\frac d{dt}\int U
\tag{ST1.9}
\]
because \((U\cdot\nabla)U_i=\sum_j\partial_j(U_jU_i)\). Thus zero spatial mean of \(U\) gives zero mean of its force. This argument proves the needed comparison directly; it does not invoke a global theorem for arbitrary forcing.

## ST2. The complete finite recorder and its inverse

The original machine has a tape on \(\mathbb Z\), finite alphabet \(\Gamma\), a blank symbol, one head, and moves \(-1,0,1\). The word occupies cells \(0,\ldots,r-1\); the head starts at zero. Redirect missing instructions and halting states to a single halting state \(q_{\rm H}\) with no outgoing rules, completing the table elsewhere. Add \(q_{\rm start}\): it preserves the read symbol and head and enters the old initial state. This finite transformation preserves halting, including immediate halting, while ensuring that the initialized state is nonterminal.

Let \(Q\) be the augmented state set. For each
\(\tau=(q,a)\in\mathcal T=(Q\setminus\{q_{\rm H}\})\times\Gamma\), write the instruction as \((q_\tau^+,a_\tau^+,d_\tau)\). Use exactly
\[
\mathcal L=\{\bot,E\}\sqcup\mathcal T,
\qquad \Sigma=\Gamma\times\{0,1\}\times\mathcal L.
\tag{ST2.1}
\]
The three tracks hold data, a marker, and history. States are \(R_q,C_q,L_q\) for \(q\in Q\) and \(A_\tau,F_\tau\) for \(\tau\in\mathcal T\), distinguished by type and subscript. Only \(R_{q_{\rm H}}\) is the terminal state reached by an initialized computation. Initially the control is \(R_{q_{\rm start}}\), the data and head are the original input, all markers are zero, and history is \(E\) at cell 2 and \(\bot\) elsewhere. The full blank is \((\mathrm{blank},0,\bot)\).

The entire partial table, expanded over all displayed symbol choices, is
\[
\begin{array}{lll}
(R_q,(a,0,\ell))&\mapsto(A_\tau,(a_\tau^+,0,\ell),d_\tau)
&q\ne q_{\rm H},\ \tau=(q,a),\ \ell\ne E,\\
(A_\tau,(a,0,\ell))&\mapsto(F_\tau,(a,1,\ell),1)&\ell\ne E,\\
(F_\tau,(a,0,\ell))&\mapsto(F_\tau,(a,0,\ell),1)&\ell\ne E,\\
(F_\tau,(a,0,E))&\mapsto(C_{q_\tau^+},(a,0,\tau),1),&\\
(C_q,(a,0,\bot))&\mapsto(L_q,(a,0,E),-1),&\\
(L_q,(a,0,\ell))&\mapsto(L_q,(a,0,\ell),-1)&\ell\ne E,\\
(L_q,(a,1,\ell))&\mapsto(R_q,(a,0,\ell),0)&\ell\ne E.
\end{array}
\tag{ST2.2}
\]
At the ready checkpoint after \(n\) augmented steps, the data and head are those of the original computation, \(|h|\le n\), all markers vanish, history cells \(2,\ldots,n+1\) contain the successive instruction tags, cell \(n+2\) contains \(E\), and other history cells contain \(\bot\). This is true for \(n=0\). Row 1 executes the next data instruction and moves to \(h'=h+d_\tau\), where \(h'\le n+1<n+2\). Row 2 marks \(h'\) and starts a rightward scan. Rows 3–4 reach the finite frontier \(n+2\), replace \(E\) by \(\tau\), and move right. Row 5 writes \(E\) at \(n+3\) and turns left. Rows 6–7 find the unique mark, erase it and enter the new ready state at \(h'\). None of the forbidden symbols is read in these steps. The exact number of table transitions is
\[
1+1+(n+1-h')+1+1+(n+2-h')+1
=4+2(n+2-h').
\tag{ST2.3}
\]
The invariant therefore holds at the next checkpoint. Halting of the augmented machine is exactly arrival at \(R_{q_{\rm H}}\); otherwise this finite cycle repeats indefinitely.

The map on all configurations in the table's domain is injective, not only on the initialized run. A destination \(A_\tau\) identifies the old \((q,a)\); the written history letter recovers the remaining old symbol. Into \(F_\tau\), both incoming moves are right, and the written marker distinguishes the arrival from \(A_\tau\) from its scan loop. Into \(C_q\), the right move and written tag identify \(\tau\), while the written data letter recovers the old data letter. Into \(L_q\), both moves are left, and the written history \(E\) distinguishes arrival from \(C_q\) from the loop. Into \(R_q\), only row 7 arrives and its displacement is zero. Thus the destination state fixes the incoming displacement, and that state together with the full written symbol identifies a unique expanded row and its old read symbol. The predecessor head is the new head minus this displacement. Restore the old symbol at that cell and retain every other tape cell. This gives the exact inverse on the image.

## ST3. Original radix coordinates and all branch maps

Let \(K=|\Sigma|\), \(B=2K+2\), and assign distinct odd digits
\(c(a)\in\{1,3,\ldots,2K-1\}\). Keep
\[
C(a_1,a_2,\ldots)=\sum_{k\ge1}c(a_k)B^{-k},
\quad I_a=\frac{c(a)+[0,1]}B,
\quad I_{a,b}=\frac{c(a)+I_b}B.
\tag{ST3.1}
\]
The code lies in \([1/(B-1),(2K-1)/(B-1)]\subset(0,1)\). Distinct first digits have gap at least \(1/B\) between their closed intervals. For a fixed first digit, distinct second digits have gap at least \(1/B^2\); different first digits retain their first-level gap. A code lies in the interior of its own first-symbol interval because its tail lies strictly between zero and one. Recovering that digit and multiplying by \(B\) after subtracting it recovers the tail, proving uniqueness of the sequence code.

For state \(i\), head \(h\), and tape \((a_k)\), use
\[
x=C(a_{h-1},a_{h-2},\ldots),\qquad
y=C(a_h,a_{h+1},\ldots).
\tag{ST3.2}
\]
The initialized codes \(x_0,y_0\) are rational: the finite nonblank prefixes are followed by constant-symbol geometric series. Let \(m\) be the number of compiled states. Count each right or stationary rule once and each left rule \(K\) times, obtaining \(N\ge1\). Set
\[
\lambda=\frac1{100(m+N+1)},\quad a_* =1/4-\lambda x_0,
\quad \Psi_i(x,y)=(a_*+\lambda x,b_i+\lambda y),
\tag{ST3.3}
\]
where
\[
b_i=\begin{cases}
1/4-\lambda y_0,&i=R_{q_{\rm start}},\\
1/16,&i=R_{q_{\rm H}},\\
1/3+\ell/[12(m+1)],&i\text{ is the }\ell\text{th other state}.
\end{cases}
\tag{ST3.4}
\]
The separation of the remaining state heights exceeds \(\lambda\); the initial and terminal squares lie in disjoint lower bands. All nonterminal squares satisfy
\(1/4-\lambda\le Y<1/2\), and the terminal square satisfies
\(1/16\le Y\le1/16+\lambda\). The initial code maps exactly to \((1/4,1/4)\).

For an expanded rule \((i,a)\mapsto(j,b,d)\), retain all three cases:
\[
\begin{array}{c|c|c|c}
d&\text{domain}&(x',y')&\text{image}\\\hline
1 &[0,1]\times I_a&((c(b)+x)/B,\ By-c(a))&I_b\times[0,1]\\
0 &[0,1]\times I_a&(x,\ y+(c(b)-c(a))/B)&[0,1]\times I_b\\
-1&I_e\times I_a&(Bx-c(e),\ c(e)/B+(c(b)+By-c(a))/B^2)
 &[0,1]\times I_{e,b}.
\end{array}
\tag{ST3.5}
\]
The left case is expanded over every \(e\in\Sigma\). A right move prefixes \(b\) to the left stack and removes \(a\) from the right one. A left move removes \(e\) from the left stack and prefixes \(e,b\) to the old right tail. A stationary move replaces only the first right digit. These operations prove every formula in ST3.5 directly from ST3.1; the linear parts are respectively \(\operatorname{diag}(B^{-1},B)\), identity, and \(\operatorname{diag}(B,B^{-1})\). Their determinants are one.

Apply \(\Psi_i\) to the domain and \(\Psi_j\) to its image. Enumerate the resulting actual rectangles as \(D_r,H_r\), with centers \(\mathbf d_r,\mathbf h_r\). The resulting map is exactly
\[
F_r(\mathbf w)=\mathbf h_r+A_r(\mathbf w-\mathbf d_r),
\quad A_r=\operatorname{diag}(\mu_r,\mu_r^{-1}),
\quad\mu_r=B^{-d}.
\tag{ST3.6}
\]
Each side has length at most \(\lambda\). The source rectangles are pairwise disjoint: states separate squares, deterministic read symbols separate digit intervals, and the left branches have separated \(I_e\). Target states determine the common incoming displacement by ST2. Distinct incoming rules have different full written symbols. For displacements 0 and 1, these separate their \(I_b\) factors; for displacement \(-1\), the ordered pairs \((e,b)\) separate \(I_{e,b}\). Thus the targets too are pairwise disjoint. Source and target families may overlap each other; the following construction treats that possibility explicitly.

## ST4. Full Hamiltonian motions and the collision check

For a slot \([s_0,s_1]\), put
\[
\theta(s)=\beta\!\left(\frac{3(s-s_0)}{s_1-s_0}-1\right).
\tag{ST4.1}
\]
It is constant on neighborhoods of both ends. Let \(J\) be the rational swept bounding rectangle of a desired motion, disjoint from all other currently tracked rectangles and from the chart boundary. Let \(\delta\) be one third of its minimum sup-norm distance to these sets. For each coordinate interval \([a,b]\) of \(J\), use
\[
\beta\!\left(\frac{u-a+\delta}{\delta/2}\right)
\beta\!\left(\frac{b+\delta-u}{\delta/2}\right).
\tag{ST4.2}
\]
Their product \(\chi\) is one on the \(\delta/2\) coordinate enlargement of \(J\), zero outside its \(\delta\) enlargement, and zero on neighborhoods of every held rectangle. All clearances are positive rationals. For a potential \(G\), the pulse is
\[
V(s,X,Y)=\theta'(s)
\big(\partial_Y(\chi G),-\partial_X(\chi G)\big).
\tag{ST4.3}
\]
Its divergence is zero by equality of mixed derivatives. Its two component integrals vanish because each is a derivative of a compactly supported function, then periodically extended. It therefore has zero planar mean.

For translation by \(\mathbf u=(u_1,u_2)\), choose \(G=u_1Y-u_2X\). On the active plateau the exact path is \(\mathbf w+\theta(s)\mathbf u\). For reciprocal scaling about \(\boldsymbol\pi\), choose
\[
G=(\log\mu)(X-\pi_1)(Y-\pi_2),\quad
\mathbf w(s)=\boldsymbol\pi+
\operatorname{diag}(\mu^{\theta(s)},\mu^{-\theta(s)})(\mathbf w-\boldsymbol\pi).
\tag{ST4.4}
\]
Differentiation proves both ODE identities, with the signs in ST4.3 unchanged. The paths remain in the one-plateau by the definition of \(J\). ODE uniqueness identifies them with the actual pulse flow. Held rectangles remain fixed because the pulse vanishes near them.

Use the original parking centers
\[
\boldsymbol\pi_r=(1/2+r/[4(N+1)],\ 3/4),\qquad 1\le r\le N,
\tag{ST4.5}
\]
and \(5N\) equal phase slots. First, in decreasing source horizontal-center order, move each source right to its parking column and then vertically to its center. Second, scale each parked rectangle by \(A_r\). Third, in increasing target horizontal-center order, move each parked rectangle vertically to its target height and then left to its target. Break equal centers by branch index. This is exactly \(2N+N+2N\) motions.

Here is the full clearance argument, including unequal rectangles. For a horizontal extraction, any remaining source with overlapping vertical projection has a disjoint horizontal interval. Its center is no larger than the active center; its horizontal interval therefore lies entirely to the left. Equal horizontal centers can occur only with disjoint vertical intervals. Thus no unextracted source intersects the swept box. Already parked boxes lie near \(Y=3/4\), while every source lies below \(1/2\). A vertical extraction stays in one parking column. Columns are separated by \(1/[4(N+1)]>\lambda\), and all state squares lie near \(X=1/4\), to the left of them. It therefore avoids both remaining sources and parked boxes.

During scaling, each coordinate side length varies monotonically between its initial and final lengths, each at most \(\lambda\). The swept box lies in \(\boldsymbol\pi_r+[-\lambda/2,\lambda/2]^2\); it avoids all other columns. In a vertical insertion the same column clearance applies, and all already inserted targets are near \(X=1/4\). For the final leftward move, remaining parked boxes are above all targets. An already inserted target whose vertical interval meets the current target has smaller horizontal center, and its disjoint horizontal interval lies entirely to the left of the current target. The active swept box stops at that target and therefore does not hit the earlier one. These arguments apply to closed rectangles and give strictly positive distances.

All swept boxes are contained in the open unit square; their endpoints are rational, including the bound for reciprocal scaling. Thus ST4.2 applies at every slot. Induction through the ordered motions proves that the period map sends every full \(D_r\) by exactly \(F_r\). All sources have left the state region before target insertion starts, so source–target overlaps create no simultaneous obstacles.

This equality holds on an effective positive neighborhood of each full rectangle. Minimize, over all slots and all tracked rectangles, the active path's clearance from the complement of its one-plateau and the held path's clearance from the pulse support, obtaining a positive computable lower bound \(m_0\). Let \(M_0\ge1\) bound every partial affine product along every branch, including intermediate reciprocal scalings. Such a bound is finite and computable: translations have linear part identity and all scaling parameters lie between their endpoint values. Choose rational
\[
0<\rho<m_0/(2M_0).
\tag{ST4.6}
\]
For an initial perturbation of norm less than \(\rho\), induction through the slots gives displacement from the corresponding tracked path at most \(M_0\rho<m_0/2\). It stays in the same active or held region and follows the same affine formula. This proves neighborhood action even at the rectangle boundaries.

## ST5. Exact observations, global derivative bounds and flow estimates

Join the pulses and repeat them with phase period one. Since every pulse vanishes near its slot endpoints, all derivatives match at joints and at integers. Periodic extension of the compact chart potentials gives a smooth Hamiltonian field \(V(s,X,Y)\), compactly supported in the open square in its planar variables, with zero divergence and mean. All its derivatives have effective uniform bounds. Indeed there are finitely many slots and rational cutoffs; ST1 bounds every cutoff derivative, while the only additional constants, such as \(\log B\), are computable. No branch of the chosen execution is needed to construct these bounds or evaluate the field.

At integer phase times, ST3.5 and induction give the next compiled configuration from the initialized point \((1/4,1/4)\). The sequence code is inside the appropriate branch rectangle, including the left-symbol subdivision. Ready checkpoints recover the augmented machine. The history block begins at absolute cell 2, so the recorded tags and frontier also recover the absolute head from the two head-relative stacks when that information is required.

All tracked paths obey the original bounds
\[
1/4-\lambda\le X\le3/4+\lambda/2,
\qquad 1/16\le Y\le3/4+\lambda/2,
\qquad (X,Y)\in J_*=[1/8,7/8]\times[1/32,7/8].
\tag{ST5.1}
\]
For a branch with nonterminal endpoints, the stronger lower bound is \(Y\ge1/4-\lambda>3/16\). Horizontal moves preserve height; vertical moves interpolate nonterminal heights and the parking height; the scaling occurs at height \(3/4\) with sides at most \(\lambda\). This proves the lower bound throughout the whole period, including intermediate and held times. A nonhalting run therefore never reaches \(H=\{1/32<Y<1/8\}\). If the run halts, an integer-phase point enters the terminal square, whose distance from both boundaries of \(H\) is at least \(1/32\), because \(\lambda<1/32\). This proves the event equivalence at all phase times. The field is globally defined after a halt; no absorbing rule is required for an event that asks whether entry occurs at least once.

Choose an effective \(L\ge1\) bounding both \(\|D_{X,Y}V\|\) and \(\|D^2_{X,Y}V\|\). For the transition map over any phase interval of length \(s\ge0\), its first variational equation and the initial identity matrix give
\[
\|D\Phi_s\|\le e^{Ls}.
\tag{ST5.2}
\]
The second derivative initially vanishes. Its inhomogeneous term is \(D^2V[D\Phi,D\Phi]\), so variation of constants gives
\[
\|D^2\Phi_s\|
\le\int_0^s e^{L(s-r)}L e^{2Lr}\,dr
=e^{2Ls}-e^{Ls}.
\tag{ST5.3}
\]
The inverse transition from initial phase \(s_0\) is the length-\(s\) flow of \(-V(s_0+s-r,\cdot)\), \(0\le r\le s\). It has the same first and second spatial derivative bounds, so ST5.2–ST5.3 apply to the inverse as well. For two lifted trajectories the difference satisfies the Lipschitz integral inequality, hence the distance is at most \(e^{Ls}\) times the initial distance. In particular an initial perturbation less than \(\eta e^{-Ls}\) stays within \(\eta\) up to phase \(s\). This is a finite-time estimate; its radius decreases with the length of computation.

## ST6. The original mean-zero spatial clock and stationary force

Choose an effective cutoff \(\chi_*\), one near the exact \(J_*\) of ST5.1 and compactly supported in the open square. Periodize its compact products. Retain the source's field
\[
g(X,Y)=\partial_X(X\chi_*(X,Y)),\qquad
W(X,Y,Z)=(V_1(Z,X,Y),V_2(Z,X,Y),g(X,Y)).
\tag{ST6.1}
\]
This formula uses the chart coordinate \(X\) only inside its compact product; it therefore defines a smooth periodic function. The planar divergence of \(V\) is zero and \(\partial_Zg=0\), so \(\operatorname{div}W=0\). All component integrals vanish by the derivative representations. On a neighborhood of \(J_*\), \(g=1\). Its mean-zero compensation outside that region does not alter the tracked path.

For each computational phase interval, the path
\[
s\longmapsto\big(\Phi_s^V(1/4,1/4),\ s\bmod1\big)
\tag{ST6.2}
\]
solves the \(W\) equation as long as the corresponding compiled segment is being followed: ST5.1 keeps the planar component where \(g=1\). The periodic smooth field has a global flow; boundedness and the uniform spatial Lipschitz bound prevent finite-time failure of its ODE. Uniqueness identifies ST6.2 with that flow, period by period. For a nonhalting run this holds at every finite phase. For a halting run it holds through terminal entry, which suffices. Thus its event at \(P\) is exactly the machine's halting event.

Now use the fixed ramp and full residual
\[
\alpha(t)=\beta(2t-1),\quad U(t,x)=\alpha(t)W(x),
\tag{ST6.3}
\]
\[
f(t,x)=\alpha'(t)W(x)+\alpha(t)^2(W\cdot\nabla)W(x)
-\nu\alpha(t)\Delta W(x),\qquad p=0.
\tag{ST6.4}
\]
The ramp vanishes for \(t\le1/2\) and is one for \(t\ge1\). Thus the initial data are zero, every mixed force derivative is bounded, and the force is exactly stationary after one. Equation ST1.6 proves the PDE with its original \(\nu\); ST1.9 proves zero mean; ST1.8 proves uniqueness. Its energy satisfies
\[
\frac12\|U(t)\|_2^2=\frac{\alpha(t)^2}{2}\|W\|_2^2
\le\frac12\|W\|_2^2.
\tag{ST6.5}
\]
The material curve is the autonomous \(W\) curve at
\[
s(t)=\int_0^t\alpha(r)\,dr,
\quad s(1)=\frac12\int_0^1\beta(u)\,du=\frac14,
\quad s(t)=t-\frac34\quad(t\ge1).
\tag{ST6.6}
\]
The middle equality uses ST1.3. The clock is continuous, nondecreasing, finite at every finite time and onto \([0,\infty)\). Consequently the event transfers in both directions, with every positive integer phase \(n\) reached at physical time \(n+3/4\). All transitions, rational coordinates, orders, margins, cutoffs and potentials came from the finite table and word. Evaluation of ST6.4 at late time does not require computing the intervening machine run. This completes the eventually stationary theorem with all its stated assertions.

## ST7. Periodic forcing, effective projection and undecidability

For the periodic alternative retain
\[
U_{\mathrm{per}}(t,X,Y,Z)=(V_1(t,X,Y),V_2(t,X,Y),0),
\quad f_{\mathrm{per}}=\partial_tU_{\mathrm{per}}+(U_{\mathrm{per}}\cdot\nabla)U_{\mathrm{per}}-\nu\Delta U_{\mathrm{per}}.
\tag{ST7.1}
\]
Because \(V\) vanishes near integer phases, the initial velocity is zero. Both fields are smooth, mean zero and period one, with bounded mixed derivatives. The solution is exactly \((U_{\mathrm{per}},0)\), unique by ST1.8. Its third particle coordinate remains zero and its first two are precisely the planar processor trajectory. ST5 proves the same fixed event. The bounded spatial and temporal periods also give a uniform kinetic-energy bound.

For either force \(F\), its solenoidal version is \(F-\nabla\phi\), where in the basis \(e^{2\pi i k\cdot x}\)
\[
\widehat\phi(k)=-\frac{i k\cdot\widehat F(k)}{2\pi|k|^2}\ (k\ne0),
\qquad \widehat\phi(0)=0.
\tag{ST7.2}
\]
Then \(\Delta\phi=\operatorname{div}F\) and the multiplier for \(\nabla\phi\) is \(kk^{\mathsf T}/|k|^2\), with norm one. For a spatial multi-index \(\mu\), set \(r=|\mu|\). Integration by parts \(r+5\) times in a coordinate with \(|k_i|\ge|k|/\sqrt3\) gives, retaining the Fourier factors,
\[
|(2\pi i k)^\mu\widehat{\partial_t^h\nabla\phi}(k)|
\le (2\pi)^{-5}3^{(r+5)/2}|k|^{-5}
\max_i\|\partial_t^h\partial_{x_i}^{r+5}F\|_\infty.
\tag{ST7.3}
\]
Group lattice points by \(j=\|k\|_\infty\). There are exactly \((2j+1)^3-(2j-1)^3=24j^2+2\), and \(|k|\ge j\). Hence the total coefficient bound is finite, and the tail after \(\|k\|_\infty\le M\), for integer \(M\ge1\), is bounded by the derivative factor in ST7.3 times
\[
\sum_{j>M}(24j^2+2)j^{-5}
\le 26\sum_{j>M}j^{-3}\le13M^{-2}.
\tag{ST7.4}
\]
This proves absolute convergence of every differentiated series, with effective tails and derivative bounds. Fourier coefficients on the unit cube are evaluated by Riemann sums with the computable first derivative bounds. Thus the force and all derivatives can be evaluated effectively. The zero Fourier mode remains zero. The fixed multiplier commutes with time differentiation and preserves stationarity, periodicity and the weighted temporal estimates proved below, at the explicitly required higher spatial orders. Pressure changes to \(p-\phi\), because
\[
-\nabla(p-\phi)+(F-\nabla\phi)=-\nabla p+F.
\tag{ST7.5}
\]
The velocity and particle event remain exactly unchanged.

Finally, a decision procedure for the fixed event on every constructed force would decide machine halting by first executing the finite compiler. Halting is undecidable: if a total algorithm \(H(e,w)\) correctly decided whether program \(e\) halts on input \(w\), construct a program \(D\) that, on input \(e\), runs forever when \(H(e,e)\) says “halts” and halts when it says “does not halt.” Applied to the code of \(D\) itself, either output contradicts the stipulated correctness of \(H\). This diagonal argument is the classical obstruction, and the proved event equivalence transfers it to the fixed fluid experiment. It is an exact decision result, not a claim about finite precision measurements.

## ST8. Full slow-clock coefficients and necessary stationary work

The original slow clock is
\[
a_1(t)=\frac{\beta(2t-1)}{1+t},\quad
U_1=a_1W,\quad F_1=a_1'W+a_1^2(W\cdot\nabla)W-\nu a_1\Delta W.
\tag{ST8.1}
\]
For \(t\ge1\), \(s_1(t)=s_1(1)+\log((1+t)/2)\), which is onto. The same chain rule as ST6.6 proves the event equivalence. Derivatives of the first two force coefficients decay as \((1+t)^{-2-h}\), and those of the last as \((1+t)^{-1-h}\). The bounded initial interval contributes a finite enlarged constant. Thus every mixed derivative of velocity and force is bounded by \(C_{h,\mu}(1+t)^{-1-h}\), and its spatial supremum belongs to \(L^2_t\). This proves the paper's stated slow-clock proposition for its actual constructed clock.

There is a precise further range with the same construction. For \(0<\sigma\le1\), retain
\[
a_\sigma(t)=\beta(2t-1)(1+t)^{-\sigma},
\quad U_\sigma=a_\sigma W,\quad
F_\sigma=a_\sigma'W+a_\sigma^2C-\nu a_\sigma\Delta W,
\quad C=(W\cdot\nabla)W.
\tag{ST8.2}
\]
With \((b)_0=1\) and \((b)_h=b(b+1)\cdots(b+h-1)\), every term for \(t\ge1\) is exactly
\[
\partial_t^h\partial_x^\mu U_\sigma
=(-1)^h(\sigma)_h(1+t)^{-\sigma-h}\partial_x^\mu W,
\tag{ST8.3}
\]
\[
\begin{aligned}
\partial_t^h\partial_x^\mu F_\sigma
={}&(-1)^{h+1}(\sigma)_{h+1}(1+t)^{-\sigma-h-1}\partial_x^\mu W\\
&+(-1)^h(2\sigma)_h(1+t)^{-2\sigma-h}\partial_x^\mu C\\
&-\nu(-1)^h(\sigma)_h(1+t)^{-\sigma-h}\partial_x^\mu\Delta W.
\end{aligned}
\tag{ST8.4}
\]
These follow by differentiating all three separate coefficient functions; no viscous or nonlinear term is removed. The phase is
\[
s_\sigma(t)=s_\sigma(1)+
\begin{cases}
\big((1+t)^{1-\sigma}-2^{1-\sigma}\big)/(1-\sigma),&0<\sigma<1,\\
\log((1+t)/2),&\sigma=1.
\end{cases}
\tag{ST8.5}
\]
It is unbounded. All finite phases are reached, so ST6's event and uniqueness proof applies to these exact fields. The coefficients and cutoff bounds give
\[
\|\partial_t^h\partial_x^\mu U_\sigma(t)\|_\infty+
\|\partial_t^h\partial_x^\mu F_\sigma(t)\|_\infty
\le C_{h,\mu,\sigma,\nu}(1+t)^{-\sigma-h}.
\tag{ST8.6}
\]
For every \(1\le q<\infty\) with \(q(\sigma+h)>1\), these supremum norms are in \(L^q(0,\infty)\); integrate the displayed power and include the compact initial interval. For \(h=0\), every \(q>1/\sigma\) is therefore available. All derivative orders are in \(L^2_t\) when \(1/2<\sigma\le1\). The projected versions retain these statements by ST7.3–ST7.4. Computable \(\sigma\) gives the same effective construction. This proves a range of integrability claims, not rapid decrease faster than every inverse power; that separate theorem requires another memory construction.

The stationary force also has a necessary nonzero work rate. For \(t\ge1\), write
\[
F_\infty=C-\nu\Delta W.
\]
Periodic integration gives
\[
\int F_\infty\cdot W
=\int (W\cdot\nabla)(|W|^2/2)-\nu\int\Delta W\cdot W
=\nu\|\nabla W\|_2^2>0.
\tag{ST8.7}
\]
Strict positivity follows without a new dynamical assumption: if \(\nabla W=0\), smoothness makes \(W\) constant on the connected torus; zero mean makes it zero, contradicting \(g=1\) near \(J_*\). Also \(\|W\|_2>0\), so
\[
\|F_\infty\|_2\ge
\frac{\nu\|\nabla W\|_2^2}{\|W\|_2}>0.
\tag{ST8.8}
\]
The projected force has the same pairing, since \(\int\nabla\phi\cdot W=0\), so the same lower bound applies. In particular an eventually stationary force of this construction cannot have finite \(L^q_tL^2_x\) norm for any finite \(q\). This exact energy comparison explains why the slow-clock alternatives are distinct forcing constructions.


## ST9. Five solved exercises

### Exercise 1. Retain the infinite blank tail

An encoded half-tape consists of the finite prefix \(a_1,\ldots,a_m\) followed by the full blank symbol \(a_\square\). Give its exact rational code and the exact tail after removing the first symbol. Explain why replacing the blank tail by zero changes the encoded point.

**Solution.** With the original base \(B=2K+2\) and digit assignment \(c\), the geometric series gives
\[
C(a_1,\ldots,a_m,a_\square,a_\square,\ldots)
=\sum_{j=1}^m c(a_j)B^{-j}
 +\frac{c(a_\square)B^{-m}}{B-1}.
\tag{ST9.1}
\]
The same formula holds for \(m=0\), with an empty finite sum. The blank digit is one of the positive odd digits, so the last summand is strictly positive. It is part of the original code. In particular an entirely blank half-tape has code \(c(a_\square)/(B-1)\), not zero.

Multiplying the defining series by \(B\) and subtracting its first digit proves
\[
BC(a_1,a_2,\ldots)-c(a_1)=C(a_2,a_3,\ldots).
\tag{ST9.2}
\]
Conversely prefixing a symbol \(b\) sends a code \(x\) to \((c(b)+x)/B\). These exact identities, with the unchanged infinite tails, give the right, left and stationary formulas in ST3.5. The finite history-marker track changes some prefix symbols but leaves a constant blank tail on each side, so the initialized codes used in ST3.3 are rational.

### Exercise 2. Count the actual recorder transitions and physical time

Suppose the augmented machine reaches its terminal state after \(q\ge1\) data instructions. Bound the number of transitions of the seven-row recorder needed to reach the corresponding ready checkpoint. Translate this into a finite upper bound for the time at which the fluid particle has entered the detector.

**Solution.** After \(n\) augmented instructions, the original head position has absolute value at most \(n\). After the next move, \(-n-1\le h'\le n+1\). The exact transition count in ST2.3 is
\[
d_n=4+2(n+2-h'),\qquad 6\le d_n\le4n+10.
\tag{ST9.3}
\]
Every term counts a row of the actual recorder, including both scans, writing the new frontier, erasing the marker and entering the ready state. Consequently its terminal checkpoint occurs at the integer phase
\[
M=\sum_{n=0}^{q-1}d_n,\qquad
6q\le M\le\sum_{n=0}^{q-1}(4n+10)=2q^2+8q.
\tag{ST9.4}
\]
Each recorder transition is one full period of the planar processor. By ST6.6, physical time \(M+3/4\) realizes phase \(M\), at which the particle is in the terminal square. Thus there is a detector visit by time
\[
t\le2q^2+8q+3/4.
\tag{ST9.5}
\]
Entry can occur during the final continuous motion, before that checkpoint; no equality for the first entry time is asserted. The initial extra state is part of the augmented machine, so immediate halting of the original machine is covered by a positive \(q\). This bound uses the number of executed instructions as a mathematical parameter; the finite force compiler does not have to determine it.

### Exercise 3. Verify every term in the energy balance for a clock

Let \(a\) be a smooth scalar clock amplitude and use the unchanged mean-zero field \(W\) from ST6. Set
\[
U_a=aW,\qquad
F_a=a'W+a^2(W\cdot\nabla)W-\nu a\Delta W.
\tag{ST9.6}
\]
Prove the full energy identity and identify exactly where the derivative, nonlinear and viscous force terms enter it.

**Solution.** Write \(K_W=\|W\|_2^2\) and \(G_W=\|\nabla W\|_2^2\). Both are positive by ST8. Periodicity and divergence zero give
\[
\int_{\mathbb T^3}(W\cdot\nabla)W\cdot W
=\frac12\int_{\mathbb T^3}\operatorname{div}(W|W|^2)=0,
\qquad
\int_{\mathbb T^3}\Delta W\cdot W=-G_W.
\tag{ST9.7}
\]
The nonlinear force term is retained in the field and has zero pairing by this exact identity. Therefore
\[
\int F_a\cdot U_a=aa'K_W+\nu a^2G_W
=\frac d{dt}\left(\frac{a^2K_W}{2}\right)
 +\nu\|\nabla U_a\|_2^2.
\tag{ST9.8}
\]
For the original ramp, the first term supplies the changing kinetic energy and the second supplies the dissipation. After time one the first term is zero, while the work rate remains \(\nu G_W>0\). If the force is projected as in ST7, its removed gradient has zero pairing with \(U_a\); the same identity and all its coefficients survive exactly.

### Exercise 4. Prove a finite-time observation tolerance

Fix an integer phase \(M\ge1\). Let the initial planar point change from \((1/4,1/4)\) to a point at Euclidean distance less than
\[
\delta_M=\frac{e^{-LM}}{64},
\tag{ST9.9}
\]
with the same initial third coordinate zero. When the recorder first reaches its terminal checkpoint at phase \(M\), prove that this detector observation persists under the perturbation. Also show that a nonhalting run remains outside the detector through phase \(M\). State the dependence on the time horizon precisely.

**Solution.** For the periodic planar field, ST5.2 and the two-trajectory estimate give distance less than \(1/64\) throughout \([0,M]\). Every unperturbed tracked path is in the rectangle from ST5.1. Its distance from the boundary of \(J_*\) is at least \(1/32\): the lower vertical margin is \(1/16-1/32\); the other margins are larger because \(\lambda<1/32\). The perturbed planar path consequently remains inside \(J_*\). Hence \(g=1\) on that path, so the spatial clock also runs at exactly unit phase speed. ODE uniqueness identifies the perturbed three-dimensional path with this planar path and the third coordinate \(s\bmod1\), through the stated horizon.

At a terminal checkpoint the unperturbed height belongs to \([1/16,1/16+\lambda]\). Its distance from each boundary of \((1/32,1/8)\) is at least \(1/32\), so the perturbation of size less than \(1/64\) preserves detector membership. For a nonhalting run the original height is at least \(1/4-\lambda>3/16\) throughout the horizon. The perturbed height is therefore greater than \(3/16-1/64=11/64>1/8\). The ramp reparametrization transfers these conclusions through physical time \(M+3/4\).

The tolerance is \(\delta_M\), which tends to zero as \(M\) increases. This proves the finite-horizon statements without asserting a single positive tolerance for every possible length of computation.

### Exercise 5. Determine the exact time-integrability threshold of the slow clocks

For the fields \(U_\sigma,F_\sigma\) in ST8.2, with \(0<\sigma\le1\), integer \(h\ge0\) and \(1\le q<\infty\), prove the exact criteria
\[
\partial_t^hU_\sigma\in L^q(0,\infty;L^2(\mathbb T^3))
\quad\Longleftrightarrow\quad q(\sigma+h)>1,
\tag{ST9.10}
\]
\[
\partial_t^hF_\sigma\in L^q(0,\infty;L^2(\mathbb T^3))
\quad\Longleftrightarrow\quad q(\sigma+h)>1.
\tag{ST9.11}
\]
Prove the same force criterion after the projection in ST7. Keep every force coefficient.

**Solution.** For \(t\ge1\), ST8.3 gives the exact velocity norm
\[
\|\partial_t^hU_\sigma(t)\|_2
=(\sigma)_h(1+t)^{-\sigma-h}\sqrt{K_W}.
\tag{ST9.12}
\]
Both constants are positive. The compact initial interval contributes a finite integral, so direct integration of \((1+t)^{-q(\sigma+h)}\) proves ST9.10, including logarithmic divergence at equality.

For the force, pair the full three-term expression ST8.4 with \(W\). The exact identities ST9.7 remove the convection pairing and retain the viscous pairing with its sign. Thus
\[
\begin{aligned}
\langle\partial_t^hF_\sigma,W\rangle
={}&(-1)^{h+1}(\sigma)_{h+1}(1+t)^{-\sigma-h-1}K_W\\
&+(-1)^h(2\sigma)_h(1+t)^{-2\sigma-h}\cdot0\\
&+\nu(-1)^h(\sigma)_h(1+t)^{-\sigma-h}G_W\\
={}&(-1)^h(\sigma)_h(1+t)^{-\sigma-h}
\left(\nu G_W-\frac{(\sigma+h)K_W}{1+t}\right).
\end{aligned}
\tag{ST9.13}
\]
For
\[
t\ge T_h=\max\left\{1,\frac{2(\sigma+h)K_W}{\nu G_W}-1\right\},
\tag{ST9.14}
\]
the bracket is at least \(\nu G_W/2\). Cauchy–Schwarz therefore gives the lower bound
\[
\|\partial_t^hF_\sigma(t)\|_2
\ge\frac{\nu(\sigma)_hG_W}{2\sqrt{K_W}}
(1+t)^{-\sigma-h}\qquad(t\ge T_h).
\tag{ST9.15}
\]
The upper bound ST8.6 and the lower bound ST9.15 prove ST9.11, again including the critical equality. Projection preserves the upper bound by ST7.3–ST7.4. It preserves the pairing because every differentiated pressure gradient integrates to zero against divergence-free \(W\), so the same lower bound holds for the projected force. In particular none of these clocks has force in \(L^1_tL^2_x\) when \(h=0\), although all have finite \(L^q_tL^2_x\) norm for \(q>1/\sigma\).

This is an exact consequence for the specified stationary-field clocks. It makes no assertion about the different, rapidly decreasing construction or the signed velocity-detector bursts. No novelty claim is made.


## Sources and proof scope

The proof above covers the original eventually stationary theorem, complete planar processor, periodic alternative, projection and stated slow clock. Its primary locators are the pinned author TeX: analytic tools, lines 191–300; recorder, 302–422; planar processor and full routing, 424–819; spatial clock and main proof, 821–908; periodic and projected forces, 910–937; slow clock and undecidability, 940–1013. No source error was established in this reading. ST8.2–ST8.8 are separate editorial consequences.

The source bibliography credits Alan Turing for undecidability, Rolf Landauer and Charles Bennett for retention of computation history, Cristopher Moore for generalized shifts, and Jean Leray for the classical difference-energy method. Their bibliographic details are retained in the [author bibliography](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/build/references.bib). This lesson proves the particular recorder, geometric realization and comparison it uses. Reading that bibliography does not constitute reading or validating all the cited works, nor does this lesson assert a novelty comparison with them.

The rapidly vanishing-force, velocity-field detection and companion constructions have separate hypotheses and proof dependencies. This lesson makes no validation claim for those theorems or their Lean developments. Its mathematical scope is the eventually stationary construction and the alternatives and consequences proved in ST1–ST8.


The complete supplying [written proof](../audits/eventually-stationary-computation-audit.md), SC0–SC8, is retained here with lesson labels ST0–ST8. The original theorem and construction are in the cited author source, lines 1–1017. ST9.10–ST9.15 strengthen the stated sufficient time-integrability bounds to exact criteria for the specified slow-clock family; their full argument is in Exercise 5. This is separate editorial exposition, with no change to the original author text and no novelty claim.