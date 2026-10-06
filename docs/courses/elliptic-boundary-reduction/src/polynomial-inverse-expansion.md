# Polynomial inverse expansion with ordered matrix coefficients

This lesson proves the finite inverse expansion for the polynomial and cutoff specified below. It keeps the original tangential and normal frequency coordinates, the leading coefficient \(I_d\), and the order of every matrix product. All position-variable estimates are uniform on the original \(\mathbb R_x^n\). No pseudodifferential composition theorem is used.

[Inverting mixed symbols without commuting matrix factors](mixed-symbol-inversion.md) supplies the ordered inverse derivative identity and cutoff inverse used below.

## 1. Exact setting and both weight presentations

Fix \(n,d\geq1\) and an integer \(m\geq1\). Write
\[
 x\in\mathbb R^n,\quad \xi=(\eta,\zeta)\in\mathbb R^{n-1}\times\mathbb R,\quad
 h=\langle\eta\rangle=(1+|\eta|^2)^{1/2},\quad
 Q=\langle\xi\rangle=(1+|\eta|^2+\zeta^2)^{1/2}.
 \tag{PI1}
\]
Keep also the original weights
\[
 R=1+|\xi|,\qquad T=1+|\eta|,\qquad
 \Xi=\zeta+ih,\qquad |\Xi|=Q,\quad 1\leq h\leq Q.
 \tag{PI2}
\]
The equality \(|\Xi|=Q\) is exact. It follows by squaring the modulus; there is no rescaling of a frequency coordinate.

For real \(u,v\), a smooth matrix function \(f\) is in the bracket presentation of \(S^{u,v}\) when all seminorms
\[
 [f]_{u,v;\beta,\alpha,r}
 =\sup_{x,\eta,\zeta}
 \frac{\|\partial_x^\beta\partial_\eta^\alpha\partial_\zeta^r f\|}
 {Q^{u-r}h^{v-|\alpha|}}
 \tag{PI3}
\]
are finite, where \(\beta\in\mathbb N_0^n\), \(\alpha\in\mathbb N_0^{n-1}\), \(r\in\mathbb N_0\). Matrices carry their Euclidean operator norm. The original presentation replaces the denominator by \(R^{u-r}T^{v-|\alpha|}\), and its seminorm is written \([f]^o_{u,v;\beta,\alpha,r}\).

For each \(s\geq0\),
\(1+s^2\leq(1+s)^2\leq2(1+s^2)\).
Thus \(R/Q,T/h\in[1,\sqrt2]\). If \(a=u-r\), \(b=v-|\alpha|\), and \(a_\pm=\max(\pm a,0)\), \(b_\pm=\max(\pm b,0)\), then
\[
 2^{-(a_-+b_-)/2}Q^ah^b
 \leq R^aT^b
 \leq2^{(a_++b_+)/2}Q^ah^b.
 \tag{PI4}
\]
For a negative exponent this follows by taking the reciprocal of the corresponding positive-exponent inequality; hence it covers all real orders and every derivative shift. Dividing by these positive weights gives
\[
 [f]^o_{u,v;\beta,\alpha,r}
 \leq2^{(a_-+b_-)/2}[f]_{u,v;\beta,\alpha,r},\qquad
 [f]_{u,v;\beta,\alpha,r}
 \leq2^{(a_++b_+)/2}[f]^o_{u,v;\beta,\alpha,r}.
 \tag{PI5}
\]
The identity on actual functions is therefore the exact continuous linear bijection between the two presentations. It commutes with every derivative and preserves multiplication in its original order. In particular the proof below with \(Q,h\) proves the assertion with \(R,T\), with constants (PI5), including when either differentiated exponent is negative.

A tangential symbol \(b(x,\eta)\in S^s_{\mathrm{tan}}\), for real \(s\), means
\[
 |b|_{s;\beta,\alpha}
 =\sup_{x,\eta}
 \frac{\|\partial_x^\beta\partial_\eta^\alpha b(x,\eta)\|}
 {h^{s-|\alpha|}}<\infty.
 \tag{PI6}
\]
Its \(T\)-weight presentation satisfies the one-factor version of (PI4)–(PI5), with exponent \(s-|\alpha|\).

Take the given polynomial
\[
 p(x,\eta,\zeta)=\sum_{k=0}^{m}p_k(x,\eta)\zeta^k,\qquad
 p_m=I_d,\qquad p_k\in S^{m-k}_{\mathrm{tan}}.
 \tag{PI7}
\]
Let \(\chi\in C_c^\infty(\mathbb R_\xi^n;\mathbb C)\) be the fixed frequency cutoff, \(\theta=1-\chi\), and \(\mathcal V=\operatorname{supp}\theta\). The meaning of the cutoff inverse hypothesis is that \(p(x,\xi)\) is invertible at every \((x,\xi)\) with \(\xi\in\mathcal V\), and
\[
 \|p(x,\xi)^{-1}\|\leq C_0Q^{-m}\quad(\xi\in\mathcal V).
 \tag{PI8}
\]
If the given invertibility statement is formulated outside a fixed compact set, the cutoff is chosen equal to one on a neighborhood of that set, exactly as required to define its cutoff inverse. No invertibility is required where \(\theta\) vanishes on a neighborhood. Define the original function
\[
 \tau(x,\xi)=\theta(\xi)p(x,\xi)^{-1}\quad(\xi\in\mathcal V),
 \qquad \tau(x,\xi)=0\quad(\xi\notin\mathcal V).
 \tag{PI9}
\]
The expansion below concerns this same \(\tau\), without alteration of \(p\) or \(\chi\).

## 2. All derivatives of the scalar weights and complex powers

We first provide constants valid even when the displayed symbol order becomes negative. For a real number \(s\) and nonnegative integer \(j\), let
\((s)_{\underline j}=s(s-1)\cdots(s-j+1)\), with empty product one.
For a tangential multiindex \(\alpha\), differentiation of \(h^s=(1+|\eta|^2)^{s/2}\) gives the exact finite identity
\[
 \partial_\eta^\alpha h^s
 =\sum_{k+2\ell=\alpha}
 \frac{\alpha!}{k!\ell!}
 (s/2)_{\underline{|k|+|\ell|}}
 (2\eta)^k
 (1+|\eta|^2)^{s/2-|k|-|\ell|}.
 \tag{PI10}
\]
Here \(k,\ell\) are tangential multiindices and their equation is componentwise. To prove it, expand the finite Taylor polynomial of the scalar function \(z^{s/2}\) at \(z=1+|\eta|^2>0\), substitute
\(z+2\eta\cdot y+|y|^2\), and compare the coefficient of \(y^\alpha\). Only terms through total degree \(|\alpha|\) can contribute, so the calculation is a finite Taylor identity for derivatives and does not require convergence of an infinite series.

Since \(|\eta_j|\leq h\), each summand is bounded by a constant times \(h^{s-|\alpha|}\). Explicitly put
\[
 K(s,\alpha)=
 \sum_{k+2\ell=\alpha}
 \frac{\alpha!}{k!\ell!}
 |(s/2)_{\underline{|k|+|\ell|}}|\,2^{|k|}.
 \tag{PI11}
\]
Then \(|\partial_\eta^\alpha h^s|\leq K(s,\alpha)h^{s-|\alpha|}\), for every real \(s\); \(K(s,0)=1\). For \(n=1\) the tangential multiindices are empty, \(h=1\), and the same formulas have their empty-index meanings.

Since \(\Xi\) is in the open upper half-plane, define \(\Xi^s=\exp(s\log\Xi)\) with its argument in \((0,\pi)\), for every real \(s\). Its modulus is \(Q^s\). Normal differentiation yields
\(\partial_\zeta^r\Xi^s=(s)_{\underline r}\Xi^{s-r}\).
For tangential derivatives, the finite Taylor chain rule gives, when \(|\alpha|>0\),
\[
 \partial_\eta^\alpha\Xi^{s-r}
 =\sum_{\ell=1}^{|\alpha|}
 \frac{(s-r)_{\underline\ell}i^\ell}{\ell!}
 \sum_{\substack{\nu_1+\cdots+\nu_\ell=\alpha\\|\nu_i|>0}}
 \frac{\alpha!}{\nu_1!\cdots\nu_\ell!}
 \Xi^{s-r-\ell}\prod_{i=1}^\ell\partial_\eta^{\nu_i}h.
 \tag{PI12}
\]
The inner lists are ordered. The factor \(1/\ell!\) is the scalar Taylor factor; the multinomial coefficient comes from multiplying the \(\ell\) positive-degree Taylor polynomials of \(h\). Thus no multiplicity has been suppressed.

Let the sum on the right below have its single value one at \(\alpha=0,\ell=0\), and otherwise only the displayed positive partitions:
\[
 H(s;r,\alpha)=
 |(s)_{\underline r}|
 \sum_{\ell=0}^{|\alpha|}
 \frac{|(s-r)_{\underline\ell}|}{\ell!}
 \sum_{\substack{\nu_1+\cdots+\nu_\ell=\alpha\\|\nu_i|>0}}
 \frac{\alpha!}{\nu_1!\cdots\nu_\ell!}
 \prod_i K(1,\nu_i).
 \tag{PI13}
\]
Combining (PI11)–(PI12) with \(h/Q\leq1\) proves
\[
 |\partial_\eta^\alpha\partial_\zeta^r\Xi^s|
 \leq H(s;r,\alpha)Q^{s-r}h^{-|\alpha|}.
 \tag{PI14}
\]
Indeed a term before the last comparison has weight
\(Q^{s-r-\ell}h^{\ell-|\alpha|}\), whose ratio to the displayed weight is \((h/Q)^\ell\leq1\). This works for all real \(s\), including every negative exponent used in the expansion.

The pointwise product rule gives, for arbitrary real orders,
\[
 \begin{split}
 [fg]_{u+u',v+v';\beta,\alpha,r}
 \leq
 \sum_{\substack{\gamma\leq\beta,\ \epsilon\leq\alpha\\0\leq l\leq r}}
 \binom{\beta}{\gamma}\binom{\alpha}{\epsilon}\binom rl
 [f]_{u,v;\gamma,\epsilon,l}
 [g]_{u',v';\beta-\gamma,\alpha-\epsilon,r-l}.
 \end{split}
 \tag{PI15}
\]
Each term preserves the order \(fg\). Its first weight exponents add to \(u+u'-r\), and its second to \(v+v'-|\alpha|\), as literal equalities. Also, for every real \(a\geq0\),
\[
 S^{u-a,v+a}\subset S^{u,v},\qquad
 [f]_{u,v;\beta,\alpha,r}\leq[f]_{u-a,v+a;\beta,\alpha,r}.
 \tag{PI16}
\]
This follows from the exact weight ratio \((h/Q)^a\leq1\), and remains valid for negative differentiated exponents.

## 3. The original polynomial and its cutoff inverse estimates

Set \(P_{k;\beta,\alpha}=|p_k|_{m-k;\beta,\alpha}\), finite by hypothesis. Since \(\partial_\zeta^r\zeta^k=(k)_{\underline r}\zeta^{k-r}\) for \(r\leq k\) and vanishes otherwise, (PI7) gives
\[
 \|\partial_x^\beta\partial_\eta^\alpha\partial_\zeta^r p\|
 \leq A_{\beta,\alpha,r}Q^{m-r}h^{-|\alpha|},\qquad
 A_{\beta,\alpha,r}
 =\sum_{k=r}^{m}(k)_{\underline r}P_{k;\beta,\alpha}.
 \tag{PI17}
\]
For \(r>m\) the sum and derivative are zero. To verify the bound term by term, divide
\(h^{m-k-|\alpha|}|\zeta|^{k-r}\)
by \(Q^{m-r}h^{-|\alpha|}\). The quotient is
\((h/Q)^{m-k}(|\zeta|/Q)^{k-r}\leq1\).
Thus the actual polynomial belongs to \(S^{m,0}\).

For clarity all inverse constants can now be written with the bracket weights. Use a combined derivative multiindex \(\mu=(\beta,\alpha,r)\). Section 2 of [Inverting mixed symbols without commuting matrix factors](mixed-symbol-inversion.md), formula (MSI6), proves the exact finite inverse derivative formula
\[
 \partial^\mu p^{-1}
 =\sum_{k=1}^{|\mu|}(-1)^k
 \sum_{\substack{\mu_1+\cdots+\mu_k=\mu\\|\mu_i|>0}}
 \frac{\mu!}{\mu_1!\cdots\mu_k!}
 p^{-1}(\partial^{\mu_1}p)p^{-1}\cdots
 (\partial^{\mu_k}p)p^{-1}
 \tag{PI18}
\]
for \(\mu\ne0\), on the open set of invertible matrices. It is obtained by taking the finite Taylor polynomial of \(p\), inverting its constant part, and using the finite geometric identity in the nilpotent positive-degree Taylor terms. That finite algebra proof does not commute matrix factors.

Define
\[
 V_0=C_0,\qquad
 V_\mu=
 \sum_{k=1}^{|\mu|}
 \sum_{\substack{\mu_1+\cdots+\mu_k=\mu\\|\mu_i|>0}}
 \frac{\mu!}{\mu_1!\cdots\mu_k!}
 C_0^{k+1}\prod_i A_{\mu_i}
 \quad(\mu\ne0).
 \tag{PI19}
\]
Equations (PI8), (PI17), and (PI18) prove
\[
 \|\partial_x^\beta\partial_\eta^\alpha\partial_\zeta^r p^{-1}\|
 \leq V_{\beta,\alpha,r}Q^{-m-r}h^{-|\alpha|}
 \quad(\xi\in\mathcal V).
 \tag{PI20}
\]
The \(k+1\) inverse factors and \(k\) polynomial derivative factors give exponent
\(-(k+1)m+km-r=-m-r\); the tangential exponents sum to \(-|\alpha|\). All orders and constants are therefore retained.

Choose \(M\geq1\) such that \(\operatorname{supp}\chi\subset\{|\xi|\leq M\}\), and put \(H_M=(1+M^2)^{1/2}\). For a frequency multiindex \(\delta=(\epsilon,l)\), write
\[
 t_\delta=\sup_\xi|\partial_\eta^\epsilon\partial_\zeta^l\theta(\xi)|,\qquad
 L_\delta=\begin{cases}1,&\delta=0,\\H_M^{|\epsilon|+l},&\delta\ne0.\end{cases}
\]
The derivative of \(\theta\) is supported in this ball whenever \(\delta\ne0\). Leibniz' rule and (PI20) give
\[
 [\tau]_{-m,0;\beta,\alpha,r}
 \leq U_{\beta,\alpha,r}
 :=\sum_{\epsilon\leq\alpha,\ 0\leq l\leq r}
 \binom\alpha\epsilon\binom rl
 t_{(\epsilon,l)}L_{(\epsilon,l)}
 V_{\beta,\alpha-\epsilon,r-l}.
 \tag{PI21}
\]
The weight correction on a nonzero cutoff derivative is exactly
\(Q^lh^{|\epsilon|}\leq H_M^{l+|\epsilon|}\).

The function in (PI9) is smooth globally. Outside \(\mathcal V\), \(\theta\) is locally zero. At a point of \(\mathcal V\), the invertible matrix \(p\) has a smooth local inverse by the determinant formula; its product with \(\theta\) agrees with (PI9) on that neighborhood, including points outside \(\mathcal V\). This proves smoothness at its boundary and makes (PI21) a global estimate. It also proves the global exact identities
\[
 p\tau=\tau p=\theta I_d.
 \tag{PI22}
\]

## 4. Re-expression in the unchanged complex normal coordinate

Substitute the literal identity \(\zeta=\Xi-ih\) into the polynomial:
\[
 \begin{split}
 p&=\sum_{j=0}^{m}P_j(x,\eta)\Xi^j,\\
 P_j&=\sum_{k=j}^{m}\binom kj\,p_k(x,\eta)(-ih)^{k-j},\qquad
 P_m=I_d.
 \end{split}
 \tag{PI23}
\]
The scalar \(h\) commutes with matrices, so this binomial expansion does not move one matrix past another. Each \(P_j\) has tangential order \(m-j\). In fact
\[
 |P_j|_{m-j;\beta,\alpha}
 \leq
 \sum_{k=j}^{m}\binom kj
 \sum_{\epsilon\leq\alpha}\binom\alpha\epsilon
 P_{k;\beta,\epsilon}\,K(k-j,\alpha-\epsilon).
 \tag{PI24}
\]
The weight exponent in each term is
\((m-k-|\epsilon|)+(k-j-|\alpha-\epsilon|)=m-j-|\alpha|\), including all its possibly negative values.

Write
\[
 A_\ell=P_{m-\ell}\in S^\ell_{\mathrm{tan}},\quad1\leq\ell\leq m,\qquad
 p=\Xi^m\left(I_d+\sum_{\ell=1}^{m}A_\ell\Xi^{-\ell}\right).
 \tag{PI25}
\]
Let \(a_{\ell;\beta,\alpha}\) denote the explicit right side of (PI24) with \(j=m-\ell\). It is a finite bound for every tangential derivative seminorm of \(A_\ell\).

Define matrices \(\tau_j(x,\eta)\) recursively by
\[
 \tau_0=I_d,\qquad
 \tau_j=-\sum_{\ell=1}^{\min(m,j)}A_\ell\tau_{j-\ell}
 \quad(j\geq1).
 \tag{PI26}
\]
This specifies the multiplication order. A closed finite expression for the same coefficient is
\[
 \tau_j=
 \sum_{k=1}^{j}(-1)^k
 \sum_{\substack{\ell_1+\cdots+\ell_k=j\\1\leq\ell_i\leq m}}
 A_{\ell_1}\cdots A_{\ell_k}\quad(j\geq1).
 \tag{PI27}
\]
To prove it, group each ordered list by its first entry in the right side; the resulting sum is exactly (PI26). Grouping by its last entry also proves the different, compatible recursion
\[
 \tau_j=-\sum_{\ell=1}^{\min(m,j)}\tau_{j-\ell}A_\ell.
 \tag{PI28}
\]
This equality is a sum identity obtained from the same ordered lists; it does not assert pairwise commutation of its factors.

Each \(\tau_j\) is in \(S^j_{\mathrm{tan}}\). Explicit constants that prove every derivative bound are obtained as follows. Put \(b_{0;0,0}=1\) and \(b_{0;\beta,\alpha}=0\) for \((\beta,\alpha)\ne(0,0)\). For \(j\geq1\), set
\[
 b_{j;\beta,\alpha}=
 \sum_{\ell=1}^{\min(m,j)}
 \sum_{\substack{\gamma\leq\beta\\\epsilon\leq\alpha}}
 \binom\beta\gamma\binom\alpha\epsilon
 a_{\ell;\gamma,\epsilon}
 b_{j-\ell;\beta-\gamma,\alpha-\epsilon}.
 \tag{PI29}
\]
Induction using the tangential Leibniz identity shows
\[
 \|\partial_x^\beta\partial_\eta^\alpha\tau_j\|
 \leq b_{j;\beta,\alpha}h^{j-|\alpha|}.
 \tag{PI30}
\]
The exponent is \(\ell-|\epsilon|+j-\ell-|\alpha-\epsilon|=j-|\alpha|\), so the induction is valid at every derivative order without assuming a nonnegative exponent.

## 5. Exact residual coefficients and the next cancellation

For an integer \(N\geq1\), let
\[
 q_N=\sum_{j=0}^{N-1}\tau_j\Xi^{-m-j}.
 \tag{PI31}
\]
Multiplying (PI25) by this sum on the right gives constant coefficient \(I_d\), and all coefficients of \(\Xi^{-k}\) for \(1\leq k<N\) vanish by (PI26). The complete remaining finite polynomial in \(\Xi^{-1}\) is
\[
 \begin{split}
 p q_N&=I_d+R_N,\\
 R_N&=\sum_{s=0}^{m-1}\rho_{N,s}\Xi^{-N-s},\\
 \rho_{N,s}
 &=\sum_{\substack{1\leq\ell\leq m,\ 0\leq j<N\\\ell+j=N+s}}
 A_\ell\tau_j.
 \end{split}
 \tag{PI32}
\]
An empty sum is zero. The largest possible total index is \(m+N-1\), which explains the precise last value \(s=m-1\). Each coefficient has the exact asserted order
\[
 \rho_{N,s}\in S^{N+s}_{\mathrm{tan}},\qquad
 \tau_N=-\rho_{N,0}.
 \tag{PI33}
\]
For the second assertion, the constraint \(\ell+j=N\), \(j<N\), is exactly \(j=N-\ell\) and \(1\leq\ell\leq\min(m,N)\), which is the recursion for \(-\tau_N\).

The explicit all-derivative constants for these residual coefficients are
\[
 c_{N,s;\beta,\alpha}=
 \sum_{\substack{1\leq\ell\leq m,\ 0\leq j<N\\\ell+j=N+s}}
 \ \sum_{\substack{\gamma\leq\beta\\\epsilon\leq\alpha}}
 \binom\beta\gamma\binom\alpha\epsilon
 a_{\ell;\gamma,\epsilon}
 b_{j;\beta-\gamma,\alpha-\epsilon}.
 \tag{PI34}
\]
Then
\[
 \|\partial_x^\beta\partial_\eta^\alpha\rho_{N,s}\|
 \leq c_{N,s;\beta,\alpha}h^{N+s-|\alpha|}.
 \tag{PI35}
\]
In particular this proves the required coefficient order \(S^{N+s}\), not merely a bound after multiplication by a power of \(\Xi\).

The other product has its own ordered residual:
\[
 q_Np=I_d+\widetilde R_N,\qquad
 \widetilde R_N=\sum_{s=0}^{m-1}\widetilde\rho_{N,s}\Xi^{-N-s},
 \qquad
 \widetilde\rho_{N,s}
 =\sum_{\substack{1\leq\ell\leq m,\ 0\leq j<N\\j+\ell=N+s}}
 \tau_jA_\ell.
 \tag{PI36}
\]
It follows by (PI28), not by commuting any coefficient in (PI32). The same derivative argument gives the same orders, with constants obtained by interchanging the written factors and their derivative allocations in (PI34).

## 6. The global expansion and every remainder derivative

The exact global algebra identity follows from (PI22) and (PI32):
\[
 \tau(pq_N)=\theta q_N=\tau+\tau R_N.
\]
Subtract \(q_N\) and use \(\theta-1=-\chi\). The result is
\[
 \boxed{\quad
 \tau=q_N+\rho_N,\qquad
 \rho_N=-\tau R_N-\chi q_N.
 \quad}
 \tag{PI37}
\]
Every factor here is a globally smooth function already constructed. This avoids use of \(p^{-1}\) in the discarded region. On the invertible region, the first term is precisely
\(-(1-\chi)p^{-1}\sum_s\rho_{N,s}\Xi^{-N-s}\).
The ordered alternative is
\[
 \rho_N=-\widetilde R_N\tau-\chi q_N,
 \tag{PI38}
\]
obtained from (PI36). Both formulas equal the same actual difference \(\tau-q_N\), although their matrix factors occupy different sides.

For full quantitative estimates, (PI14) and (PI30) imply
\[
 [q_N]_{-m,0;\beta,\alpha,r}\leq
 Q_{N;\beta,\alpha,r}
 :=\sum_{j=0}^{N-1}\sum_{\epsilon\leq\alpha}\binom\alpha\epsilon
 b_{j;\beta,\epsilon}H(-m-j;r,\alpha-\epsilon).
 \tag{PI39}
\]
Before applying (PI16), the \(j\)-th differentiated term has weight
\(Q^{-m-j-r}h^{j-|\alpha|}\).
Its ratio to the displayed target weight is \((h/Q)^j\), exactly.

Likewise,
\[
 [R_N]_{-N,N;\beta,\alpha,r}\leq
 D_{N;\beta,\alpha,r}
 :=\sum_{s=0}^{m-1}\sum_{\epsilon\leq\alpha}\binom\alpha\epsilon
 c_{N,s;\beta,\epsilon}H(-N-s;r,\alpha-\epsilon).
 \tag{PI40}
\]
The pre-comparison weight is
\(Q^{-N-s-r}h^{N+s-|\alpha|}\);
its ratio to \(Q^{-N-r}h^{N-|\alpha|}\) is \((h/Q)^s\leq1\).
Thus \(R_N\in S^{-N,N}\), with every derivative and every negative exponent controlled.

For the inverse term in (PI37), the product bound (PI15) gives
\[
 [\tau R_N]_{-m-N,N;\beta,\alpha,r}\leq
 F_{N;\beta,\alpha,r},
\]
where the explicit finite constant is
\[
 F_{N;\beta,\alpha,r}
 =\sum_{\substack{\gamma\leq\beta,\ \epsilon\leq\alpha\\0\leq l\leq r}}
 \binom\beta\gamma\binom\alpha\epsilon\binom rl
 U_{\gamma,\epsilon,l}
 D_{N;\beta-\gamma,\alpha-\epsilon,r-l}.
 \tag{PI41}
\]
In particular the inverse contribution has precisely the required mixed order, with the rightmost coefficient factors never interchanged with \(\tau\).

The cutoff contribution is better than required in every mixed order. Put
\(\chi_{\epsilon,l}=\sup_\xi|\partial_\eta^\epsilon\partial_\zeta^l\chi|\).
For arbitrary real \(u,v\), direct Leibniz differentiation of \(\chi q_N\), using (PI39), yields
\[
 \begin{split}
 [\chi q_N]_{u,v;\beta,\alpha,r}
 \leq K_{N;u,v;\beta,\alpha,r}
 :=\sum_{\epsilon\leq\alpha,\ 0\leq l\leq r}
 \binom\alpha\epsilon\binom rl
 \chi_{\epsilon,l}Q_{N;\beta,\alpha-\epsilon,r-l}\\
 {}\times H_M^{(-m-u+l)_+ +(-v+|\epsilon|)_+}.
 \end{split}
 \tag{PI42}
\]
To verify this exponent exactly, divide the differentiated \(q_N\) weight
\(Q^{-m-r+l}h^{-|\alpha|+|\epsilon|}\)
by the requested \(Q^{u-r}h^{v-|\alpha|}\).
The quotient is \(Q^{-m-u+l}h^{-v+|\epsilon|}\). On the support of each cutoff derivative, \(1\leq h\leq Q\leq H_M\), so any negative power is at most one and any positive power is bounded by its corresponding power of \(H_M\). This proves (PI42) for real \(u,v\) without discarding negative derivative shifts.

Set \(u=-m-N\), \(v=N\) in (PI42). Equations (PI37), (PI41), and (PI42) prove
\[
 \begin{split}
 \|\partial_x^\beta\partial_\eta^\alpha\partial_\zeta^r\rho_N\|
 &\leq
 \left(F_{N;\beta,\alpha,r}
 +K_{N;-m-N,N;\beta,\alpha,r}\right)
 Q^{-m-N-r}h^{N-|\alpha|},\\
 \rho_N&\in S^{-m-N,N}.
 \end{split}
 \tag{PI43}
\]
Together with (PI30), (PI31), and (PI37), this is the required expansion for every \(N\geq1\):
\[
 \tau=\sum_{j=0}^{N-1}\tau_j(x,\xi')\Xi^{-m-j}+\rho_N,\qquad
 \tau_j\in S^j_{\mathrm{tan}},\quad
 \rho_N\in S^{-m-N,N}.
 \tag{PI44}
\]
The constants use only finitely many indicated seminorms of the actual \(p_k\), the given \(C_0\), the actual cutoff derivatives and radius, and the fixed derivative orders, dimension, \(m,N\). The same coefficient sequence works for every truncation. These finite expansions need not be a convergent infinite series.

For \(N=0\), the sum is empty and \(\rho_0=\tau\in S^{-m,0}\) by (PI21). Thus this value is covered when the phrase “every \(N\)” includes zero. If the polynomial degree is \(m=0\), then \(p=I_d\), \(\tau=(1-\chi)I_d\), and one takes \(\tau_0=I_d\), \(\tau_j=0\) for \(j\geq1\). For \(N\geq1\), \(q_N=I_d\), \(\rho_N=-\chi I_d\); the same compact-support proof as (PI42) puts it in every real mixed order. This handles the degenerate polynomial case as well.

If a later application prescribes a real number \(s\) or \(\nu\), an integer \(N\geq\max(0,s)\), or \(N\geq\max(0,\nu)\), can be chosen because (PI44) holds for every nonnegative integer. For example the choices \(N=\max(0,\lceil s\rceil)\) and \(N=\max(0,\lceil\nu\rceil)\) are exact. The mapping estimates themselves require their stated one-sided operator arguments; the present result supplies their full expansion at every such chosen truncation.

## 7. A complete noncommuting polynomial example

Take \(d=2\), any \(n\geq1\), and
\[
 U=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 V=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
 W=U+V,\quad
 UV=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 VU=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
 \tag{PI45}
\]
Here \(U^2=V^2=0\), \(W^2=I_2\), and \(UV\ne VU\). Each of \(U,V,UV,VU\) has operator norm one, as follows by applying it to \((z_1,z_2)\) and computing the Euclidean norm. The same is true of \(W\), which exchanges the two coordinates.

Keep \(h=\langle\eta\rangle\) and \(\Xi=\zeta+ih\). Define the actual degree-two polynomial, independent of \(x\), by
\[
 \begin{split}
 p&=(\Xi I_2+ihU)(\Xi I_2+ihV)\\
  &=\zeta^2I_2+ih(2I_2+W)\zeta-h^2(I_2+W+UV).
 \end{split}
 \tag{PI46}
\]
Thus \(p_2=I_2\), \(p_1=ih(2I_2+W)\in S^1_{\mathrm{tan}}\), and
\(p_0=-h^2(I_2+W+UV)\in S^2_{\mathrm{tan}}\).
These membership assertions include every derivative: all positive-order \(x\) derivatives vanish, and (PI11) gives
\[
 \|\partial_\eta^\alpha p_1\|
 \leq3K(1,\alpha)h^{1-|\alpha|},\qquad
 \|\partial_\eta^\alpha p_0\|
 \leq3K(2,\alpha)h^{2-|\alpha|}.
 \tag{PI47}
\]
The coefficient matrices themselves do not commute:
\[
 [p_1,p_0]
 =-ih^3[W,UV]
 =-ih^3(V-U)\ne0.
 \tag{PI48}
\]
Indeed \(WUV=V\), \(UVW=U\), by the displayed matrices.

Nilpotence gives exact inverses of the two factors:
\[
 (\Xi I_2+ihU)^{-1}
 =\Xi^{-1}I_2-ih\Xi^{-2}U,\qquad
 (\Xi I_2+ihV)^{-1}
 =\Xi^{-1}I_2-ih\Xi^{-2}V.
 \tag{PI49}
\]
For instance multiplying the first expression by \(\Xi I_2+ihU\) on either side cancels the two linear \(U\)-terms and leaves a multiple of \(U^2=0\). Since \(|\Xi|=Q\geq h\), each inverse has norm at most \(2Q^{-1}\). The original \(p\) is consequently invertible everywhere and obeys
\[
 \|p^{-1}\|\leq4Q^{-2}.
 \tag{PI50}
\]
The ordered product of those inverses is
\[
 \begin{split}
 p^{-1}
 &=(\Xi I_2+ihV)^{-1}(\Xi I_2+ihU)^{-1}\\
 &=\Xi^{-2}I_2-ihW\Xi^{-3}-h^2VU\Xi^{-4}.
 \end{split}
 \tag{PI51}
\]
Every coefficient and sign follows from multiplication in that written order; the final coefficient is \(VU\), not \(UV\).

In the notation of (PI25),
\[
 A_1=ihW,\qquad A_2=-h^2UV.
 \tag{PI52}
\]
The recursion gives
\[
 \begin{split}
 \tau_0&=I_2,\qquad \tau_1=-ihW,\\
 \tau_2&=A_1^2-A_2=-h^2I_2+h^2UV=-h^2VU,\\
 \tau_3&=-A_1\tau_2-A_2\tau_1
 =ih^3WVU-ih^3UVW=ih^3U-ih^3U=0.
 \end{split}
 \tag{PI53}
\]
Next \(\tau_4=-A_1\tau_3-A_2\tau_2=0\), since \(UVVU=U(V^2)U=0\). The two-step recursion then gives \(\tau_j=0\) for every \(j\geq3\). This recovers (PI51) by the actual recursive coefficients rather than assuming it from the factorization.

Take first the admissible cutoff \(\chi=0\), so \(\tau=p^{-1}\). The remainders are exactly
\[
 \rho_1=-ihW\Xi^{-3}-h^2VU\Xi^{-4}\in S^{-3,1},\qquad
 \rho_2=-h^2VU\Xi^{-4}\in S^{-4,2},\qquad
 \rho_N=0\quad(N\geq3).
 \tag{PI54}
\]
All derivative estimates follow explicitly from (PI11) and (PI14), followed, for the second term of \(\rho_1\), by the factor \(h/Q\leq1\). This matches the target orders \(S^{-m-N,N}\) with \(m=2\). The finite expansion terminates here because of the particular nilpotent factors; no termination claim is made in the general theorem.

For any other allowed compact frequency cutoff \(\chi\), the coefficients \(\tau_j\) stay exactly those in (PI53), because they depend on \(p\) rather than the cutoff. For \(N\geq3\) the exact remainder is then
\[
 \rho_N=-\chi p^{-1}.
 \tag{PI55}
\]
It belongs to every mixed order by (PI42). Thus even a terminating inverse series does not make the actual cutoff remainder vanish unless the cutoff term vanishes.

## 8. Solved exercise detecting an invalid matrix reversal

**Exercise.** For (PI46), compute the polynomial inverse and the first three inverse-series coefficients at \(\eta=0,\zeta=0\). Compare the true inverse with the expression obtained by reversing the two inverse factors in (PI51). Verify the residual coefficient identity \(\tau_2=-\rho_{2,0}\) before substituting this frequency.

**Solution.** At \(\eta=0\), \(h=1\); at \(\zeta=0\), \(\Xi=i\). These are the original frequency values. Equation (PI46) gives
\[
 p=-(I_2+U)(I_2+V)
 =\begin{pmatrix}-2&-1\\-1&-1\end{pmatrix},\qquad
 p^{-1}=\begin{pmatrix}-1&1\\1&-2\end{pmatrix}.
 \tag{PI56}
\]
Their product in either order is \(I_2\), by direct entry multiplication. The coefficients at this frequency are
\[
 \tau_0=I_2,\qquad
 \tau_1=-i\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 \tau_2=-\begin{pmatrix}0&0\\0&1\end{pmatrix}.
 \tag{PI57}
\]
Since \(i^{-2}=-1\), \(i^{-3}=i\), and \(i^{-4}=1\), their terms add to
\(-I_2+W-VU\), which is the inverse matrix in (PI56).

Reversing the inverse factors instead gives the different symbol
\[
 q_{\mathrm{wrong}}
 =\Xi^{-2}I_2-ihW\Xi^{-3}-h^2UV\Xi^{-4}.
 \tag{PI58}
\]
At the selected frequency its value and left product with \(p\) are
\[
 q_{\mathrm{wrong}}=
 \begin{pmatrix}-2&1\\1&-1\end{pmatrix},\qquad
 p q_{\mathrm{wrong}}=
 \begin{pmatrix}3&-1\\1&0\end{pmatrix}\ne I_2.
 \tag{PI59}
\]
The error is exactly the replacement of the ordered matrix \(VU\) by \(UV\); scalar powers and frequency coordinates were unchanged.

For \(N=2\), the residual coefficient constraints in (PI32) give
\[
 \begin{split}
 \rho_{2,0}
 &=A_1\tau_1+A_2\tau_0
 =h^2W^2-h^2UV=h^2VU,\\
 \rho_{2,1}
 &=A_2\tau_1=ih^3UVW=ih^3U.
 \end{split}
 \tag{PI60}
\]
Thus \(\tau_2=-\rho_{2,0}\), with tangential orders \(2\) and \(3\) for the two residual coefficients. The other product has
\(\widetilde\rho_{2,0}=h^2VU\) and
\(\widetilde\rho_{2,1}=\tau_1A_2=ih^3V\).
The highest residual coefficients differ, confirming why (PI32) and (PI36) have to retain their separate multiplication orders. Each still yields the same actual inverse remainder through its corresponding formula (PI37) or (PI38).

## References

The finite ordered inverse derivative identity is [Inverting mixed symbols without commuting matrix factors](mixed-symbol-inversion.md), (MSI6), restated in (PI18); its cutoff estimates are supplied above in the exact notation needed here. The separate one-sided operator mapping estimates use this construction in subsequent units.
