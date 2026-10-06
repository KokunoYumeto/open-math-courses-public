# Commuting coordinates for long-range evolution


*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*


**Working question: Which moving coordinates keep the evolution energy controlled?** Removing a long-range phase changes the natural position coordinates of a packet. Coordinates that commute with the free part expose the remaining coefficient as a product of real factors. Energy control depends on the adjoint defect of each product, so a bound only for their sum cannot justify the required evolution estimate.


A first-order equation has a useful energy estimate when the integral of its adjoint defect is finite. A long-range phase supplies coordinates that commute with its free part. Factoring the remaining coefficient through those coordinates produces an evolution equation whose energy stays uniformly controlled. The individual factor products matter: each must have a small adjoint defect.


We first prove the evolution principle. We then construct commuting coordinates, obtain real factors by the fundamental theorem of calculus, and count every derivative needed for their operator estimates. Read [Energy-shell factors and outgoing equations](energy-shell-factors-and-outgoing-equations.md) for the perturbed energy root, and [Generating functions and the end of a localized force](generating-functions-and-the-end-of-a-localized-force.md) for the full generating-function estimates. Our calculus foundation is the programme proof [The separate moving-coordinate metric, Theorem 7.1](../providers/analysis/finite-weighted-calculus.md#moving-coordinate-calculus). Section 3 explains its application and the normalization correspondence with Lerner's free author chapter [L]; Sections 4–5 derive the factor estimates. Teschl's free preliminary text [O] provides the Picard and integrating-factor correspondence, whose operator-valued proofs are written here. Yafaev's free lecture paper [Y], Teschl's free author edition [T], and Hörmander's freely readable general-polynomial paper [H] place modified waves in context. Theorem 3.9 of [H] has stronger coefficient and Hessian hypotheses than the generality retained here; its proof does not replace ours.


Our convention is \(D=-i\partial\), with left quantization. All Hilbert inner products are linear in the first entry. Fourier inversion and Plancherel are proved in [Fourier facts](../providers/analysis/finite-derivative-l2.md#fourier-normalization). The exact Bochner integral, norm primitive, product and variation arguments are proved in [Hilbert-valued integration for the evolution equations](../providers/analysis/hilbert-valued-integration.md).


## 1. Evolution with an integrable adjoint defect


**Theorem 1.1.** Let \(M(s)\) be a norm-continuous family of bounded operators on a Hilbert space \(\mathcal H\), locally bounded for \(s\ge s_0\). Suppose


\[

 \begin{gathered}

 \omega(s)=\|M(s)-M(s)^*\|,\\

 \int_{s_0}^{\infty}\omega(s)\,ds<\infty.

 \end{gathered}

 \tag{1}

\]


For every \(h\in L^1_{\mathrm{loc}}([s_0,\infty);\mathcal H)\) and \(v_0\in\mathcal H\), there is a unique continuous distributional solution of


\[

 (D_s-M(s))v=h,\qquad v(s_0)=v_0.

 \tag{2}

\]


It is locally absolutely continuous. A constant independent of the terminal time gives


\[

 \|v(s)\|\le C\left(\|v_0\|

                  +\int_{s_0}^s\|h(t)\|\,dt\right).

 \tag{3}

\]


The homogeneous propagator has a uniform bound in both time directions.


**Proof.** Fix a finite interval and a time \(t\) in it. Starting with \(U_0(s,t)=I\), define
\(U_{j+1}(s,t)=i\int_t^s M(q)U_j(q,t)\,dq\).
If \(\|M(q)\|\le K\) on that interval, induction on the integral gives
\(\|U_j(s,t)\|\le K^j|s-t|^j/j!\).
Consequently \(U=\sum_{j\ge0}U_j\) converges uniformly in operator norm and solves
\(U(s,t)=I+i\int_t^s M(q)U(q,t)\,dq\).
For two solutions of this integral equation, iterating the equation for their difference gives the same factorial bound times the uniform norm of that difference; letting the iteration order tend to infinity proves uniqueness. This calculation works when \(s<t\) as well. Uniqueness gives
\(U(s,q)U(q,t)=U(s,t)\), and hence \(U(s,t)^{-1}=U(t,s)\).
This is the norm-valued Picard argument; the scalar and finite-dimensional version is explained in [O], Theorem 2.5 and Corollary 2.6.


For a homogeneous solution,


\[

 \left|\frac{d}{ds}\|v(s)\|^2\right|

       \le\omega(s)\|v(s)\|^2.

 \tag{4}

\]


Indeed its derivative is \(2\operatorname{Re}(iM(s)v,v)=((iM-iM^*)v,v)\), whose absolute value is bounded by \(\omega(s)\|v\|^2\). Multiply the forward differential inequality by \(\exp(-\int_t^s\omega)\); the resulting derivative is nonpositive. The reverse inequality gives the same bound with the endpoints exchanged. Thus


\[

 \|U(s,t)\|\le

 \exp\left(\frac12\int_{\min(s,t)}^{\max(s,t)}

                                      \omega(q)\,dq\right)\le C.

 \tag{5}

\]


The local propagators concatenate to every finite interval. Variation of constants gives


\[

 v(s)=U(s,s_0)v_0

           +i\int_{s_0}^s U(s,t)h(t)\,dt,

 \tag{6}

\]


which is locally absolutely continuous and proves (3). Conversely, a continuous distributional solution has derivative \(i(Mv+h)\), which is locally integrable. Subtract its Bochner primitive; every scalar pairing of the difference has zero distributional derivative and is constant. Thus the solution is locally absolutely continuous, and the variation formula proves uniqueness. \(\square\)


## 2. Coordinates adapted to a real phase


Write \(x=(s,z)\), with \(z\in\mathbb R^d\), and use \(\eta\) for transverse frequency. Throughout the construction \(s\ge s_0\ge1\). Choose


\[

 \begin{gathered}

 0<\delta<1/3,\\

 c=(1-\delta)/2,\quad r=(1+\delta)/2,\\

 X=(1+s^2+|z|^2)^{1/2},\\

 \mu(k)=

 \begin{cases}

 \delta+k,&0\le k\le2,\\

 1+rk,&k\ge2.

 \end{cases}

 \end{gathered}

 \tag{7}

\]


The two formulas at \(k=2\) coincide. Before frequency extension, the real energy root \(a\), free root \(E\), and real generator \(G\) satisfy on a fixed frequency chart


\[

 \begin{aligned}

 G_s(s,\eta)&=a(s,-G_\eta(s,\eta),\eta),\\

 |\partial_{s,z}^{\beta}\partial_\eta^\alpha(a-E)|

       &\le C_{\alpha\beta}X^{-\mu(|\beta|)},\\

 |\partial_s^u\partial_\eta^\alpha(G-sE)|

       &\le C_{u\alpha}s^{1+|\alpha|-\mu(u+|\alpha|)}.

 \end{aligned}

 \tag{8}

\]


These are the hypotheses proved in the linked energy-root and generating-function lessons. Multiply \(G,a,E\) by the same real compact transverse frequency cutoff \(\psi\). We retain their names for these extensions. Their estimates persist by the product rule. The graph identity is used where \(\psi=1\). In particular \(N=G_s-a\) has cancellation of its free \(\psi E\) term everywhere.


Set


\[

 \begin{aligned}

 A_0&=D_s-G_s(s,D_z),\\

 A_j(s)&=z_j+G_{\eta_j}(s,D_z),\qquad 1\le j\le d.

 \end{aligned}

 \tag{9}

\]


These operators commute on Schwartz tests:


\[

 [A_0,A_j]=0,\qquad [A_j,A_k]=0.

 \tag{10}

\]


For the first identity, \([D_s,G_{\eta_j}]=-iG_{s\eta_j}\) and \([-G_s(D_z),z_j]=iG_{s\eta_j}\) cancel. For the second, \([z_j,G_{\eta_k}(D_z)]=iG_{\eta_j\eta_k}(D_z)\), and the reversed term has the negative sign. The symmetry of the Hessian gives zero.


For each fixed \(s\), \(G_{\eta_j}(s,D_z)\) is bounded and self-adjoint. Thus \(A_j\) is self-adjoint on the domain of coordinate multiplication. One can check this bounded-perturbation assertion directly: the adjoint of \(z_j+K\), with bounded self-adjoint \(K\), has domain \(\mathcal D(z_j^*)=\mathcal D(z_j)\) and equals \(z_j+K\).


The phase removes these coordinates exactly:


\[

 z_j e^{-iG(s,D_z)}v

              =e^{-iG(s,D_z)}A_j(s)v.

 \tag{11}

\]


Fourier transformation makes this the product rule for \(i\partial_{\eta_j}(e^{-iG}\widehat v)\). It extends to the coordinate domain by smooth approximation.


## 3. The moving metric and the calculus we use


For fixed \(s\), put


\[

 \begin{aligned}

 g_s&=X^{-2r}|dz|^2+X^{2c}|d\eta|^2,\\

 g_s^\sigma&=X^{-2c}|dz|^2+X^{2r}|d\eta|^2,\\

 h_s&=X^{-\delta}\le1.

 \end{aligned}

 \tag{12}

\]


The coordinate meaning of \(f\in S(w,g_s)\) is


\[

 |\partial_\eta^\alpha\partial_z^\beta f|

       \le C_{\alpha\beta}w X^{c|\alpha|-r|\beta|}.

 \tag{13}

\]


All constants below are uniform in \(s\). The metric is slowly varying: a small metric displacement has \(|z-y|\le\rho X(y)^r\), and \(r<1\), so the brackets are comparable. For dual temperateness let \(Q=g_{s,(y,\theta)}^\sigma((z,\eta)-(y,\theta))\). Then \(|z-y|\le X(y)^c\sqrt Q\), and


\[

 \frac{X(z)}{X(y)}\le1+\sqrt Q.

 \tag{14}

\]


For \(t=X(y)/X(z)\), the same Lipschitz inequality gives \(t\le1+t^c\sqrt Q\). If \(t\ge2\), then \(t^{1-c}\le2\sqrt Q\); otherwise it is bounded. Thus both bracket ratios have polynomial bounds in \(1+Q\). Comparing the coefficients in (12) proves dual temperateness. The same argument proves local continuity and temperateness of every fixed power of \(X\), including its products with a constant power of \(s\). Reflection of the frequency directions leaves the metric unchanged. These verifications give common structural constants for the linked calculus.


The proof of the calculus for (12) is given in the earlier programme provider [The separate moving-coordinate metric, Theorem 7.1](../providers/analysis/finite-weighted-calculus.md#moving-coordinate-calculus). Its weights are every fixed real power \(s^aX^b\), including all weights and derivative weights used here. That proof treats arbitrary smooth symbols in (13), without a frequency-support restriction. It proves the oscillatory-integral estimates, finite Taylor remainders, exact Schwartz and distribution identities, and the uniform \(L^2\) bound. It is a separate argument from that provider's metric with decreasing frequency-derivative scale.

For comparison with the free source [L], that source uses the Fourier kernel \(e^{2\pi iz\cdot\xi}\) and \(D_z=(2\pi i)^{-1}\partial_z\). Put \(\eta=2\pi\xi\) and \(\widetilde f(z,\xi)=f(z,2\pi\xi)\). Our operator with symbol \(f\) is exactly its operator with symbol \(\widetilde f\), by the frequency Jacobian. Use in its phase space the metric
\[
 \widetilde g_s=(2\pi)^{-1}X^{-2r}|dz|^2
                         +(2\pi)X^{2c}|d\xi|^2.
\]
This is a fixed positive scalar times the pullback of (12), so its derivative seminorms and structural constants are equivalent with constants independent of \(s\). The product of its two coordinate coefficients is \(X^{-2\delta}\); hence its inverse uncertainty weight \(\lambda_{\widetilde g_s}^{-1}\) in [L] is exactly \(h_s\le1\). Reflection holds, and the preceding bracket-ratio proof gives all its admissibility and weight conditions. The fixed scaling is useful: a frequency substitution alone would introduce a factor \(2\pi\) into that uncertainty weight.

Here is the exact quantization correspondence, also obtained by substitution in the kernels in the linked proof. In our convention write
\(T_\tau=\exp(i\tau\langle D_z,D_\eta\rangle)\).
Kernel substitution gives
\(\operatorname{Op}_L(f)=(T_{-1/2}f)^w\), so the exact left product is
\[
 f\circ_Lq
     =T_{1/2}\big((T_{-1/2}f)\#(T_{-1/2}q)\big).
\]
The symbol \(f\circ_Lq\) is proved directly by the integral \((2\pi)^{-d}\operatorname{Os}\iint e^{-iy\cdot\theta}f(z,\eta+\theta)q(z+y,\eta)\,dy\,d\theta\). Taylor-expand the second factor in \(y\) to order \(K-1\). Transferring each factor of \(y\) onto the first symbol contributes \(-i\partial_\eta\), giving exactly \(\partial_\eta^\alpha f D_z^\alpha q/\alpha!\). The integral remainder is the explicit formula (M11) in the provider. At the fixed output point its scaling \(y=X^cu\), \(\theta=X^{-c}v\) and the two bracket-ratio inequalities (M7) give a finite-seminorm bound uniform in \(s\). Each paired derivative contributes \(X^{c-r}=h_s\). This proves, for every finite \(K\),


\[

 \begin{gathered}

 f\circ_L q=

 \sum_{|\alpha|<K}

       \frac{\partial_\eta^\alpha f\,D_z^\alpha q}{\alpha!}

       +\mathcal R_K,\\

 \mathcal R_K\in S(w_f w_q h_s^K,g_s).

 \end{gathered}

 \tag{15}

\]


The adjoint kernel has exact right symbol \(\overline f\). Converting it to a left symbol uses \(T_1\overline f\). Its finite expansion gives the paired derivatives \(D_z^\alpha\partial_\eta^\alpha\overline f/\alpha!\), with remainder in \(S(w_fh_s^K,g_s)\). The provider proves that remainder by the same integral Taylor formula, with both derivatives on the translated single symbol, in (M12). Thus the real-symbol adjoint rule used below has a programme proof with all the required seminorms.

The uniform \(L^2\) bound is proved in (M13)–(M16) of the provider. Partition the output into \(X\asymp2^j\), dilate position by \(2^{jc}\), and apply the earlier finite-derivative \(L^2\) theorem to each piece. The nearby input pieces sum by finite overlap. For the distant input pieces every Taylor coefficient vanishes; their exact remainders have norms \(O(2^{-jrK})\), which sum for \(K\ge1\). This proves the bound for \(S(1,g_s)\) uniformly in \(s\). For the weight below, \(s^{1+\delta}q\in S(1,g_s)\) because \(s/X\le1\). Therefore


\[

 \begin{gathered}

 q\in S(s^{-\delta}X^{-1},g_s)\\

 \Longrightarrow\quad\|q(s,z,D_z)\|\le Cs^{-1-\delta}.

 \end{gathered}

 \tag{16}

\]


The exact kernel formulas and product theorem give these identities on Schwartz functions. Here their domains can also be checked directly. Each factor symbol is compactly supported in frequency and its derivative of order \(k\) in frequency grows at most like a fixed power of \(X\) times \(X^{ck}\), where \(c<1\). In its kernel, integrate by parts \(k\) times in frequency away from \(|z-y|=0\). For \(|y|<|z|/2\), the factor \(|z-y|^{-k}\) then dominates \(X^{ck}\); choosing \(k\) large gives any requested power of decay in \(z\). For \(|y|\ge|z|/2\), use the arbitrary decay of the Schwartz input in \(y\), with enough seminorms to absorb the finite symbol growth and the integral. Derivatives in the output variable obey the same estimate. This proves that each such operator preserves Schwartz space continuously.

For the adjoint kernel interchange \(z\) and \(y\). In the region \(|y|<|z|/2\), integration by parts again gives any inverse power of \(|z|\), while its symbol growth is a finite power of \(y\) absorbed by a Schwartz seminorm of the input. In the other region that input already has arbitrary decay. Thus the adjoints preserve Schwartz space too, and transposition extends the operators and their compositions to tempered distributions. Coordinate operators themselves act by multiplication plus a smooth compact-frequency multiplier. All our compositions therefore have their indicated domains before bounded extension. Only finite expansions will be used.


## 4. Real factors from coordinate differences


Let \(A=z+G_\eta\), \(z^0=-G_\eta\). Let \(Y^0=z\), and obtain \(Y^j\) by replacing the first \(j\) coordinates of \(z\) by those of \(z^0\). Define


\[

 \begin{aligned}

 F_j^{\,n}&=a(s,Y^j,\eta)-a(s,Y^{j-1},\eta),\\

 C_j&=-\int_0^1

       a_{z_j}(s,Y^{j-1}-tA_je_j,\eta)\,dt.

 \end{aligned}

 \tag{17}

\]


To see the factor identity without dividing by a coordinate that might vanish, put
\(p_j(t)=Y^{j-1}-tA_je_j\).
Its endpoints are \(Y^{j-1}\) and \(Y^j\), and
\(\frac d{dt}a(s,p_j(t),\eta)=-A_j a_{z_j}(s,p_j(t),\eta)\).
The fundamental theorem of calculus therefore gives \(F_j^{\,n}=C_jA_j\), including at \(A_j=0\). Summing the endpoint differences gives
\(\sum_jF_j^{\,n}=a(s,-G_\eta,\eta)-a(s,z,\eta)\).
On \(\psi=1\), the graph identity makes this exactly \(N=G_s-a\).


Choose a real smooth \(\phi_0\), equal to one on the unit ball and zero outside the ball of radius two. Put \(\Phi=\phi_0(A/s)\). Away from \(|A|<s\), define


\[

 \begin{aligned}

 D_j&=N A_j/|A|^2,\qquad

 F_j^{\,f}=N A_j^2/|A|^2,\\

 B_j&=\Phi C_j+(1-\Phi)D_j,\\

 F_j&=B_jA_j=\Phi F_j^{\,n}+(1-\Phi)F_j^{\,f}.

 \end{aligned}

 \tag{18}

\]


The far factors are used only where their denominator is nonzero. All expressions extend smoothly and are real. They are compactly supported in transverse frequency. The exact identity is


\[

 N=\sum_{j=1}^d B_jA_j

                        \quad\text{where }\psi=1.

 \tag{19}

\]


**Theorem 4.1 (full factor estimates).** For \(|\alpha_0+\beta_0|\le1\),


\[

 \begin{aligned}

 \partial_\eta^{\alpha_0}\partial_z^{\beta_0}A_j

       &\in S(X^{1-|\beta_0|},g_s),\\

 \partial_\eta^{\alpha_0}\partial_z^{\beta_0}B_j

       &\in S(s^{-\delta}X^{-1-|\beta_0|},g_s).

 \end{aligned}

 \tag{20}

\]


These assertions include every further metric derivative. Moreover,


\[

 \begin{aligned}

 F_j,\ \partial_\eta F_j&\in S(s^{-\delta},g_s),\\

 \partial_zF_j,\ \partial_z\partial_\eta F_j

       &\in S(s^{-\delta}X^{-1},g_s).

 \end{aligned}

 \tag{21}

\]


**Proof: the derivative budget near the graph.** First derive the size of every inner derivative from (8). A derivative of order \(k\ge1\) of \(G_\eta\) differentiates \(G\) \(k+1\) times. The contribution from \(sE\) is \(O(s)\). The remaining contribution is \(O(s^{k+2-\mu(k+1)})\). Since \(\mu(k+1)=1+r(k+1)\), including its consistent value at \(k+1=2\), this gives


\[

 \begin{gathered}

 |\partial_\eta^k G_\eta|\le C_k s^{a(k)},\\

 a(k)=\max(1,c(k+1)),\quad k\ge1.

 \end{gathered}

 \tag{22}

\]


Here \(a(1)=1\), and \(a(k)=c(k+1)\) at \(k\ge2\), since \(\delta<1/3\). A repeated chain rule differentiates the outer function a finite number of times and partitions the derivatives that fall on its inner map into positive blocks. Write their orders as \(k_1,\ldots,k_q\), put \(K=\sum_i k_i\), and let \(e\) count the blocks with \(k_i\ge2\). A block of order one has exponent \(c+r=1\); a larger block has exponent \(ck_i+r-\delta\), since \(r-\delta=c\). Adding these exponents gives the exact accounting identity


\[

 \sum_i a(k_i)=cK+rq-\delta e.

 \tag{23}

\]


On \(|A|\le2s\), both \(z=-G_\eta+A\) and \(-G_\eta\) have size \(O(s)\), so every path point \(p_j(t)\) has bracket comparable to \(s\), uniformly for \(0\le t\le1\). These path maps are affine in \(z\); their first physical derivatives are bounded constants, and all higher ones vanish. Thus at physical order \(b\) and frequency order \(k\), a term differentiating \(a_{z_j}(s,p_j(t),\eta)\) through \(q\ge1\) inner frequency blocks uses an outer physical derivative of order \(b+1+q\). Its remaining \(k-K\) frequency derivatives fall directly on \(a\), and have no cost in the root estimate. By (23) its exponent is


\[

 \begin{gathered}

 cK+rq-\delta e-\mu(b+1+q)\\

 =cK-1-r(b+1)-\delta e\\

 \le ck-1-r(b+1).

 \end{gathered}

 \tag{24}

\]


For \(q=0\), the bound is \(s^{-\mu(b+1)}\). It is at most the last bound in (24) when \(k\ge1\), because
\(\mu(b+1)\ge1+r(b+1)-c\).
Integration over \(t\) preserves all these estimates. In particular the complete derivative table for the near factors is
\[
 |\partial_z^b\partial_\eta^k C_j|\le C_{bk}
 \begin{cases}
 s^{-\mu(b+1)},&k=0,\\
 s^{ck-1-r(b+1)},&k\ge1.
 \end{cases}
\]
Here and below an order denotes any multi-index of that length. This table proves every further derivative of the three prefixes in (20): the frequency prefix uses \(k+1\), with exponent \(ck-rb-1-\delta\); the physical prefix uses \(b+1\), with exponent \(ck-rb-2-\delta\). The zero-frequency cases follow from
\(\mu(b+1)\ge1+\delta+rb\) and
\(\mu(b+2)\ge2+\delta+rb\).
The zeroth prefix is weaker than these bounds since \(r\ge\delta\).

For the individual difference \(F_j^{\,n}\), the free \(E\) term cancels even at physical order zero. If \(b\ge1\) and \(k\ge1\), a term with inner blocks uses outer physical order \(b+q\ge2\), and (23) gives exponent
\(cK+rq-\delta e-\mu(b+q)=cK-1-rb-\delta e\).
Terms with \(q=0\) use \(s^{-\mu(b)}\), bounded by the same expression because \(\mu(b)\ge1+rb-c\) for \(b\ge1\). Therefore


\[

 |\partial_z^b\partial_\eta^k F_j^{\,n}|

                       \le C s^{ck-1-rb}.

 \tag{25}

\]


For \(b=0\), no inner block gives \(s^{-\delta}\). One block of order one gives the same bound; one larger block gives \(s^{c(k_1+1)-1-\delta}\). Two or more blocks give \(s^{cK-1-\delta e}\). Since \(2c\le1\) and \(c+\delta=r<1\), all these terms are at most \(s^{c(k-1)-\delta}\) when \(k\ge1\). Together with the direct zero-frequency estimates, the full table is
\[
 |\partial_z^b\partial_\eta^k F_j^{\,n}|\le C_{bk}
 \begin{cases}
 s^{-\delta},&b=k=0,\\
 s^{c(k-1)-\delta},&b=0, k\ge1,\\
 s^{-\mu(b)},&b\ge1, k=0,\\
 s^{ck-1-rb},&b\ge1, k\ge1.
 \end{cases}
\]
To check (21), increase \(k\) by one for a frequency prefix and \(b\) by one for a physical prefix. With both increases the last exponent becomes exactly \(ck-rb-1-\delta\), using \(c-r=-\delta\). Without the frequency increase use \(r\ge\delta\); the zero-frequency physical cases use \(\mu(b+1)\ge1+\delta+rb\). The remaining two prefixes follow from the first two rows. This establishes all jets, including the mixed prefix, directly from (8).


**Proof: far factors and transition.** Since \(G_\eta=O(s)\), on \(|A|\ge s\) one has \(X\asymp|A|\). Equation (8) gives


\[

 \begin{aligned}

 N,\ \partial_\eta N&\in S(s^{-\delta},g_s),\\

 \partial_zN,\ \partial_z\partial_\eta N

       &\in S(s^{-\delta}X^{-1},g_s).

 \end{aligned}

 \tag{26}

\]


At positive frequency order \(k\), the zero-physical-order bound for \(N\) is \(s^{c(k+1)-1}\), and at order zero it is \(s^{-\delta}\). Its frequency prefix has exponent \(ck-\delta\) for each further order \(k\). Positive physical derivatives come only from \(a\); use \(\mu(q+1)\ge1+\delta+rq\) and \(X\ge s\).


Equation (22) and \(s\le X\) give the first line of (20). More precisely, every positive frequency jet of order \(k\) of \(A\) is at most \(CX^{1+c(k-1)}\), since \(a(k)\le1+c(k-1)\). A physical derivative of \(A\) is constant, and higher or mixed physical derivatives vanish.

The needed ratio estimates can now be counted explicitly. Let \(R(A)\) denote either \(A_j/|A|^2\), homogeneous of degree \(\ell=-1\), or \(A_j^2/|A|^2\), homogeneous of degree \(\ell=0\). Its derivative of order \(q+b\) in \(A\) is bounded by \(C|A|^{\ell-q-b}\) on \(A\ne0\). For \(b\) physical derivatives and \(q\) positive frequency blocks of total order \(k\), the chain rule therefore gives
\[
 |\partial_z^b\partial_\eta^k R(A)|
       \le C X^{\ell-b+c(k-q)}.
\]
If \(k=0\), take \(q=0\); if \(k>0\), every term has \(q\ge1\). A frequency prefix uses total order \(k+1\), so its exponent is at most \(\ell-b+ck\). A physical prefix uses \(b+1\), so its weight has one more factor \(X^{-1}\); since \(r<1\), any further physical derivatives are also sufficient for (13). A mixed prefix enjoys both facts. With \(\ell=-1\), (26) and the product rule prove the far bounds in (20). With \(\ell=0\), they prove all four far bounds in (21).


On the transition \(X\asymp s\). Every positive frequency jet of \(A/s\) of order \(k\) is at most \(Cs^{c(k-1)}\), and every physical derivative contributes \(s^{-1}\). A term in \(\partial_z^b\partial_\eta^k\phi_0(A/s)\) with \(q\) positive frequency blocks is therefore bounded by \(Cs^{-b+c(k-q)}\); all derivatives of \(\phi_0\) are bounded. The same prefix count as for the ratios shows that \(\Phi\) and its frequency prefix have weight one, while its physical and mixed prefixes have weight \(s^{-1}\). The product rule for \(\Phi C_j\), \((1-\Phi)D_j\), and their corresponding products now proves (20)–(21) globally. Only the compact transition uses both constructions. \(\square\)


## 5. Individual operator defects


Write \(\mathcal B_j=B_j(s,z,D_z)\), and let \(\mathcal C_j=\mathcal B_jA_j\), initially on Schwartz space. Exact right multiplication gives


\[

 \mathcal C_j=F_j(s,z,D_z)

                     -i(\partial_{\eta_j}B_j)(s,z,D_z).

 \tag{27}

\]


In particular \(\mathcal C_j\) extends boundedly, with norm \(O(s^{-\delta})\). Define


\[

 \begin{aligned}

 \mathcal T&=-i\sum_j(\partial_{\eta_j}B_j)(s,z,D_z),\\

 \mathcal R_{kj}&=[A_k,\mathcal B_j],\\

 \mathcal Q_j&=\mathcal C_j-\mathcal C_j^*.

 \end{aligned}

 \tag{28}

\]


**Theorem 5.1.** All these defects extend boundedly to \(L^2(\mathbb R^d)\), and


\[

 \begin{gathered}

 \|\mathcal T\|+\sum_{k,j}\|\mathcal R_{kj}\|

 +\sum_j(\|\mathcal B_j\|+\|\mathcal Q_j\|)\\

 \le Cs^{-1-\delta}.

 \end{gathered}

 \tag{29}

\]


**Proof.** The symbols of \(\mathcal T\) and \(\mathcal B_j\) already have the weight in (16). For \([A_k,\mathcal B_j]\), subtract the two finite expansions in (15). The scalar zeroth products cancel. At the first paired derivative, \(\partial_\eta A_k\,D_zB_j\) has weight
\(X\cdot s^{-\delta}X^{-2}=s^{-\delta}X^{-1}\), and
\(\partial_\eta B_j\,D_z A_k\) has weight
\(s^{-\delta}X^{-1}\cdot1=s^{-\delta}X^{-1}\).
For total paired order \(l\ge1\), leave one such derivative on each factor and apply the remaining \(l-1\) frequency and physical derivatives in (13). They contribute
\(X^{c(l-1)-r(l-1)}=h_s^{l-1}\).
In the second product the terms with \(l\ge2\) in fact vanish because \(A_k\) is affine in \(z\). Thus every retained nonzero term has the required weight. The original product weight is \(X\cdot s^{-\delta}X^{-1}=s^{-\delta}\). Choose a finite \(K\) with \(K\delta\ge1\); each remainder then lies in
\(S(s^{-\delta}X^{-K\delta},g_s)\subset S(s^{-\delta}X^{-1},g_s)\).

For the individual adjoint defect of \(\operatorname{Op}_L(F_j)\), its real zeroth symbol cancels. The first paired derivative has weight \(s^{-\delta}X^{-1}\) by the mixed prefix in (21). Each additional paired derivative contributes \(h_s\). The adjoint remainder starts with the original weight \(s^{-\delta}\) and has the same \(h_s^K\) bound. This proves the asserted weight for every term of
\(\operatorname{Op}_L(F_j)-\operatorname{Op}_L(F_j)^*\).
By (27), the remaining two terms in \(\mathcal Q_j\) are the derivative correction and its adjoint; (16) bounds both, since taking an operator adjoint preserves its norm. Applying (16) to each finite term and remainder proves (29). The identities start on Schwartz tests, and their bounded extensions are unique by density. The proof treats each \(j\) separately, as required. \(\square\)


One further bound will control transverse moments. Put


\[

 \begin{aligned}

 M(s)&=G_s(s,D_z)-\sum_j\mathcal C_j(s),\\

 \mathcal L&=D_s-M(s)

             =A_0+\sum_j\mathcal B_jA_j.

 \end{aligned}

 \tag{30}

\]


Then \(M\) is uniformly bounded, norm continuous locally in \(s\), and


\[

 \begin{aligned}

 \|M-M^*\|&\le C s^{-1-\delta},\\

 \|[z_k,M]\|&\le C,\qquad 1\le k\le d.

 \end{aligned}

 \tag{31}

\]


The first follows from (29) and the reality of \(G_s\). For the second, \([z_k,q(s,z,D_z)]=i(\partial_{\eta_k}q)(s,z,D_z)\). The frequency prefix of \(F_j\) has weight \(s^{-\delta}\). The second frequency derivative of \(B_j\) has weight \(s^{-\delta}X^{c-1}\), bounded by a constant since \(c<1\) and \(X\ge s\). Finally \(G_{s\eta_k}(s,D_z)\) is uniformly bounded by (8). The linked \(L^2\) theorem proves (31).


For local norm continuity, on a compact \(s\) interval all frequency jets of the explicit near and far factors and of their \(s\) derivatives are uniformly bounded in \(z\). The far denominators satisfy \(|A|\ge s\), and the transition occupies a bounded \(z\) region. Compact frequency support therefore gives kernels bounded by \(C_N(1+|z-y|)^{-N}\), for every finite \(N\), with the same bounds for their \(s\) derivatives. For \(N>d\), integration in either variable gives the Schur bound. It proves local norm continuity of \(\mathcal B_j\), its frequency-derivative operators, (27), \(\mathcal T\), and \(M\). Finally
\(\mathcal R_{kj}=i\operatorname{Op}_L(\partial_{\eta_k}B_j)+[G_{\eta_k}(s,D_z),\mathcal B_j]\)
is locally norm continuous because every operator in this formula is bounded and locally norm continuous. The formula for \([z_k,M]\) just used has the same property.


## 6. The factored Cauchy equation


**Corollary 6.1.** For every \(h\in L^1_{\mathrm{loc}}([s_0,\infty);L^2_z)\) and \(v_0\in L^2_z\), the equation


\[

 \mathcal Lv=h,\qquad v(s_0)=v_0

 \tag{32}

\]


has a unique continuous distributional solution. It is locally absolutely continuous and satisfies (3), with one constant for all \(s\ge s_0\).


**Proof.** Apply Theorem 1.1 to (30)–(31). \(\square\)


If a frequency-localized solution satisfies \((D_s-a(s,z,D_z))v=g\) and its Fourier support is in \(\psi=1\), (19) and (27) give exactly


\[

 \mathcal Lv=g+\mathcal Tv.

 \tag{33}

\]


A bounded-slice outgoing solution and \(g\in L^1(ds;L^2_z)\) therefore give an integrable right side on this half-line, by (29). This is the equation whose phase-corrected amplitudes will be studied next.


For \(d=0\), the transverse factors are absent. The graph identity is \(G_s=a\), and all statements reduce to the real scalar equation; sums of transverse defects are zero.


### Use the conclusion


Check each factor's operator and adjoint defect in the moving metric. Compare the abstract integrable-defect evolution with the exact factored Cauchy equation before transferring the bound to an amplitude.


## 7. Exercises with complete solutions


**Exercise 1 — Foundation: the phase and the direction of translation.** In the exact translation model \(G(s,\eta)=s\,b\cdot\eta\), with fixed \(b\in\mathbb R^d\), solve \((D_s-b\cdot D_z)v=0\), \(v(s_0)=v_0\). Compute \(e^{-iG(s,D_z)}v(s)\) and verify (11). This explicit model does not require a frequency extension.


**Solution 1.** Fourier transformation gives \(\widehat v(s,\eta)=e^{i(s-s_0)b\cdot\eta}\widehat v_0(\eta)\), so


\[

 \begin{aligned}

 v(s,z)&=v_0(z+(s-s_0)b),\\

 e^{-iG(s,D_z)}v(s,z)&=v_0(z-s_0b).

 \end{aligned}

 \tag{34}

\]


A packet moves toward \(-b\). Here \(A_j=z_j+sb_j\). Applying the translation by \(-sb\) to \(A_jv\) gives \(z_jv_0(z-s_0b)\), exactly the left side of (11). The identities first hold on Schwartz functions; unitary translations extend the solution to every \(L^2\) datum.


**Exercise 2 — Intermediate: a bounded ordering error.** In one transverse dimension let \(A=z+g(s,D_z)\), with real bounded smooth \(g\), and \(\mathcal B=q(s)p(D_z)\), where \(p\) is real, smooth and compactly supported and \(q(s)=s^{-1-\delta}\). Compute \(\mathcal BA-\operatorname{Op}(BA)\) and \(\mathcal BA-A\mathcal B^*\) on Schwartz tests. Give their exact operator norms.


**Solution 2.** Right multiplication by \(g(D_z)\) has no correction. Right coordinate multiplication has the correction \(-i\partial_\eta B\). Since \(\mathcal B^*=\mathcal B\) and the Fourier multipliers commute, both requested differences are


\[

 -i q(s)p'(D_z).

 \tag{35}

\]


Plancherel gives norm \(s^{-1-\delta}\|p'\|_\infty\) for each. Although \(\mathcal BA\) itself can be unbounded in this model, its displayed differences have bounded extensions. This distinction is why operator identities involving coordinates are first proved on Schwartz tests.


**Exercise 3 — Intermediate: how many finite terms are needed?** Take \(\delta=1/4\). Find \(c,r,h_s\), and the smallest integer \(K\) that puts a remainder with original weight \(s^{-\delta}\) into the weight in (16). Explain why one fewer order would permit a nonintegrable time bound.


**Solution 3.** We have \(c=3/8\), \(r=5/8\), \(h_s=X^{-1/4}\). The required inequality is \(K\delta\ge1\), so the smallest choice is \(K=4\). Its weight is \(s^{-1/4}X^{-1}\), giving time norm \(Cs^{-5/4}\). At \(K=3\) the weight is only \(s^{-1/4}X^{-3/4}\); at \(X=s\) this permits \(Cs^{-1}\). Its integral diverges logarithmically. Increasing the finite order uses the full symbol jets, without claiming convergence of an infinite expansion.


**Exercise 4 — Advanced: why the far patch is needed.** On a frequency patch use \(G=sE_0-e^{-s}\), with constant \(E_0\), and

\(a(s,z)=E_0+e^{-s}e^{-z_1^2}(1+z_2)e^{-z_2^2}\). Compute the two coordinate-difference factors with \(z^0=0\). Show that they factor \(G_s-a\) exactly, but the second near factor alone does not obey a global \(X^{-1}\) bound.


**Solution 4.** Here \(A_j=z_j\), and


\[

 \begin{aligned}

 F_1^{\,n}

   &=e^{-s}(1-e^{-z_1^2})(1+z_2)e^{-z_2^2},\\

 F_2^{\,n}

   &=e^{-s}\bigl(1-(1+z_2)e^{-z_2^2}\bigr).

 \end{aligned}

 \tag{36}

\]


Their sum is \(e^{-s}(1-e^{-z_1^2}(1+z_2)e^{-z_2^2})=G_s-a\). Divide the first by \(z_1\), and the second by \(z_2\), to obtain \(C_1,C_2\). Both quotients extend smoothly: their numerators vanish at zero, and the integral formula (17) gives the extensions. In particular \(C_1=0\) at \(z_1=0\), while \(C_2=-e^{-s}\) at \(z_2=0\).


Fix \(s\) and \(z_2=0\), and let \(|z_1|\to\infty\). The value \(C_2=-e^{-s}\) remains nonzero, whereas \(X^{-1}\to0\). The near factor cannot have the required global bound. Formula (18) replaces it outside the near region by a ratio whose denominator measures the full vector \(A\). The example has all needed root and generator decay on the patch, since the spatial derivatives are Gaussian and the time dependence is exponential.


**Exercise 5 — Advanced: sharpness of the integrable defect.** On \(\mathcal H=\mathbb C\), take \(M(s)=\beta(s)+i a(1+s)^{-1-\delta}\), with bounded real continuous \(\beta\) and real \(a\). Find the homogeneous propagator and its norm. What changes if the last exponent is \(-1\)?


**Solution 5.** The propagator is


\[

 \begin{gathered}

 U(s,t)=\exp(i\Theta(s,t)-aJ_\delta(s,t)),\\

 \Theta(s,t)=\int_t^s\beta(q)\,dq,\\

 J_\delta(s,t)=\int_t^s(1+q)^{-1-\delta}\,dq.

 \end{gathered}

 \tag{37}

\]


Its norm is the exponential of \(-aJ_\delta(s,t)\). The integral over the whole half-line is finite, so the norms in both orientations are bounded by

\(\exp(|a|(1+s_0)^{-\delta}/\delta)\). The adjoint defect is \(2|a|(1+s)^{-1-\delta}\), agreeing exactly with (5). At exponent \(-1\) the norm becomes \(((1+s)/(1+t))^{-a}\). For \(a<0\) it grows without bound forward; for \(a>0\) it grows without bound backward. Thus the uniform two-direction estimate requires the integrable decay gap.


## References


- [Y] Dmitri Yafaev, *Lectures on scattering theory*, lecture notes prepared by Andrew Hassell, arXiv:math/0403213v1, 12 March 2004. [Free lecture paper](https://arxiv.org/pdf/math/0403213v1).
- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, freely readable author edition of the second edition, 2014, Chapter 12. [Free author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
- [L] Nicolas Lerner, *Metrics on the Phase Space and Non-Selfadjoint Pseudodifferential Operators*, freely available author Chapter 2. Theorem 2.3.7, printed pp. 91–92; Theorems 2.3.18–2.3.19, p. 100; Theorem 2.5.1 and its proof, pp. 111–112. [Free author chapter](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf).
- [O] Gerald Teschl, *Ordinary Differential Equations and Dynamical Systems*, author's preliminary version, 2012. Theorem 2.5 and Corollary 2.6, pp. 40–41, give Picard iteration; Lemma 2.7, pp. 42–43, gives the integrating-factor estimate. [Author's online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
- [H] Lars Hörmander, “The existence of wave operators in scattering theory,” *Mathematische Zeitschrift* **146** (1976), 69–91. [Digitized paper](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf).
