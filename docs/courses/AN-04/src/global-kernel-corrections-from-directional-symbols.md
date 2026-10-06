# From directional symbols to global kernel corrections

Solving the symbol equation is the first step of a kernel correction. We must realize its solution by an actual distribution, keep the closed directional wavefront bound at every lower order, and preserve that bound when the infinitely many corrections are summed. This lesson supplies those steps for the normalized degree-one scalar problem.

The geometry and global time coordinates are proved in Global time and the bicharacteristic relation, Sections 1–6. The symbol-line solution and closed reflexive hull are proved in Directional transport for characteristic symbols, Sections 1–3. We use the complete frequency-graph criterion and the intersection of all orders in Recognizing a Lagrangian distribution intrinsically, Sections 2–3; the invariant symbol isomorphism and its surjectivity in Gaussian lines, densities and invariant symbols, Sections 6–7; the full scalar product proof in Hamilton fields and subprincipal transport, Sections 1–7; and Fourier-symbol reduction in Oscillatory distributions and their order, Section 4. The underlying symbol summation, including every differentiated remainder, is already proved in Section 2 of Symbols, operators and Sobolev scales. We use that proof and add the wavefront controls needed here.

The symbol-summation provider carries GFDL 1.2, without invariant sections or cover texts. The additional kernel arguments below are independently written.

## 1. Realizing a symbol with its closed microsupport

Let \(Y\) have dimension \(d\), let \(\Lambda\subset T^*Y\setminus0\) be a closed smooth conic Lagrangian, and let \(K\subset\Lambda\) be conic and closed in the full punctured cotangent space. Work with ordinary symbols, locally over compact base sets. The invariant symbol line is \(L=M_\Lambda\otimes\Omega_\Lambda^{1/2}\). A symbol section of intrinsic order \(r+d/4\) is the symbol of an order-\(r\) distribution.

**Controlled realization lemma.** If \(a\in S^{r+d/4}(\Lambda;L)\) has microsupport contained in \(K\), there is
\[
A\in I^r(Y,\Lambda;\Omega_Y^{1/2}),\qquad
\sigma(A)=a\pmod{S^{r+d/4-1}},\qquad
\operatorname{WF}(A)\subset K.
\tag{KC1}
\]
The construction can use one fixed locally finite family of relatively compact base and direction boxes for all later orders.

**Proof.** Use the graph cones and homogeneous partition in the complete symbol-surjectivity proof just cited. Choose their closed supports inside their graph domains and locally finite in the ambient cosphere. Their base boxes can also be chosen locally finite: exhaust the base by relatively compact sets, cover each intervening compact cosphere band by finitely many smaller graph cones, and take the supports inside the corresponding enlarged band. A compact base set then meets only finitely many boxes. This uses closedness of \(\Lambda\) to make its unit-covector part over a compact base set compact.

In one graph chart, write \(\Lambda=\{(H'(\theta),\theta)\}\). In the graph Maslov frame the partitioned section has coefficient \(b(\theta)\) relative to \(|d\theta|^{1/2}\), of order
\[
\mu=r-d/4.
\tag{KC2}
\]
Its angular support is closed inside the chart cone. Extend it by zero outside that cone, and extend the homogeneous \(H\) smoothly on a slightly larger cone and through bounded frequencies. Use \((2\pi)^{d/4}\mathcal F^{-1}(e^{-iH}b)|dy|^{1/2}\), multiplied by a compact base cutoff equal to one near the graph's base image. This is the normalized graph inverse from the symbol-surjectivity proof: its integral prefactor is \((2\pi)^{-3d/4}\), and before the base cutoff its normalized Fourier coefficient is exactly \(b\). Fourier reduction gives the prescribed symbol modulo one lower order after that cutoff; the frequency-graph converse gives order \(r\).

Here is the extra wavefront control in that construction. If \(b\) is rapidly decreasing with every derivative in a direction neighborhood, multiplication of the resulting distribution by a compact smooth function has Fourier transform given by convolution with the rapidly decreasing transform of that function. Split the frequency integral into a smaller neighborhood of that direction and its complement. In the first part \(b\) has arbitrary decay. In the second, for output frequency in the still smaller cone,
\[
|\eta-\theta|\geq c(|\eta|+|\theta|).
\tag{KC3}
\]
Rapid decrease of the cutoff transform absorbs the polynomial growth of \(b\) and the frequency measure. This proves arbitrary decay in \(\eta\). Differentiated versions insert bounded powers of the compact base variable and obey the same estimate.

There is no additional wavefront away from the critical graph. For \(y\) near a point different from \(H'(\theta_0)\), restrict to a small angular neighborhood of \(\theta_0\). The vector \(y-H'(\theta)\) is bounded away from zero. Integrate the graph phase by parts with
\[
\frac{y-H'(\theta)}{i|y-H'(\theta)|^2}\cdot\partial_\theta.
\tag{KC4}
\]
Each application lowers the ordinary amplitude order by one: a frequency derivative of \(H'\) has inverse-radius decay. After any specified number of base derivatives, take sufficiently many applications to make the integral absolutely convergent. The angular-cutoff derivatives have the same inverse-radius bounds. Frequencies outside that angular neighborhood are excluded from the output cone by the estimate (KC3). Thus every possible wavefront point is the graph point of a direction where \(b\) is not rapidly decreasing. That set is precisely the local microsupport of the section, and is contained in \(K\).

Low-frequency changes have smooth inverse transforms. Smooth changes of frames and the chosen partition do not enlarge microsupport. Each local realization therefore has wavefront in \(K\); the locally finite sum has the same property and the prescribed symbol. This proves (KC1). Fixing the boxes, partition, base cutoffs and graph phases gives the last assertion. ∎

We have not asserted physical support in the projection of \(K\). A smooth kernel can extend outside that projection. The assertion is the exact wavefront inclusion needed for the correction.

## 2. Asymptotic sums that retain wavefront exclusion

Suppose the successive kernels \(A_j\in I^{r-j}(Y,\Lambda)\) are constructed using the fixed family in Section 1. In each box their graph coefficients are \(b_{\ell j}\in S^{\mu-j}\), and their microsupports lie in the local copy of \(K\). Then there is a kernel \(A\) with
\[
A\in I^r(Y,\Lambda),\qquad
A-\sum_{j=0}^{J}A_j\in I^{r-J-1}(Y,\Lambda)\quad(J\geq0),
\qquad \operatorname{WF}(A)\subset K.
\tag{KC5}
\]

**Proof.** Work first in one fixed graph box and suppress \(\ell\). Use the high-frequency cutoff \(1-\chi(\theta/R_j)\) of the exact AN-03 summation proof. Enlarge its radii as necessary. In addition to that proof's order-\(\mu-j+1\) seminorm bound, impose the following finite conditions at stage \(j\).

Choose a countable collection of compact angular sets contained in the complement of \(K\) in this graph cone, with their interiors covering that complement. Such a collection comes from closed smaller balls in a countable coordinate basis, with closure still outside the closed set. On each of these sets every \(b_j\) is rapidly decreasing. Require, on the first \(j\) such sets and for derivatives of order at most \(j\),
\[
\big\|(1-\chi(\theta/R_j))b_j\big\|_{S^{-j},\,j}\leq2^{-j}.
\tag{KC6}
\]
The notation restricts the ordinary weighted derivative seminorm to the indicated set. Choose each set inside a slightly larger compact set still outside \(K\), so its bound follows from the definition of microsupport. Every demand in (KC6) is attainable. Rapid decay provides more than the required power; derivatives of the radial cutoff are bounded by a constant times \(\langle\theta\rangle^{-k}\) on their support. There are only finitely many demands at this stage. Their maximum threshold and the preceding radius give one adequate increasing \(R_j\).

Set
\[
b=\sum_{j\geq0}(1-\chi(\theta/R_j))b_j.
\tag{KC7}
\]
The sum is locally finite in frequency. The ordinary symbol and remainder bounds are exactly those in the cited complete summation proof: the extra conditions only enlarge the permissible radii. For a fixed angular set outside \(K\), a derivative order \(L\), and a decay power \(N\), the tail with \(j\geq\max(L,N,\text{index of the set})\) is bounded in the \(S^{-N}\) seminorm by \(\sum_j2^{-j}\). Each of the finitely many earlier terms is rapidly decreasing there. Thus \(b\) is rapidly decreasing with every derivative outside \(K\), and its microsupport is contained in \(K\).

Perform this construction separately in each fixed graph box. The inverse graph integrals and base cutoffs give the kernels and the exact inclusion (KC1). The local remainder after \(J+1\) terms has scalar order \(\mu-J-1\), hence distribution order \(r-J-1\). Only finitely many boxes meet any compact base set, so the local sums are distributions, their differentiated order estimates give the actual local \(I^{r-J-1}\) membership, and their wavefront remains in \(K\). This proves (KC5). ∎

The extra demands (KC6) are essential to the asserted closed wavefront bound. Termwise smoothness, or local finiteness in frequency alone, does not control an infinite sum's singularities; Exercise 2 gives an explicit failure.

## 3. Ordinary order-zero coefficients in transport

The previous directional lesson assumed a homogeneous degree-zero coefficient. The kernel iteration also works with an ordinary \(S^0\) coefficient. This retains lower terms without imposing a homogeneous expansion on them.

In its coordinates \((q,t,s,R)\), let \(c\in S^0\) be smooth with
\[
|\partial_{q,t,s}^{\alpha}\partial_R^k c|\leq C_{\alpha k}R^{-k},\qquad R\geq1,
\tag{KC8}
\]
on compact relation-coordinate sets. For \(g\in S^r\), define
\[
C(q,t,s,R)=\int_s^t c(q,b,s,R)\,db,\qquad
u=i e^{-iC(q,t,s,R)}\int_s^t e^{iC(q,b,s,R)}g(q,b,s,R)\,db.
\tag{KC9}
\]
Then \((1/i)\partial_tu+cu=g\), \(u|_{t=s}=0\), and \(u\in S^r\) with every differentiated estimate. Its forward and backward microsupport bounds are the same closed reflexive hulls as before.

**Proof.** The compact interpolation segments in the preceding geometric proof stay in a compact subset of their actual open domain. Writing each integral with \(b=s+\theta(t-s)\), \(0\leq\theta\leq1\), proves (KC8) for \(C\). The exponential is bounded there because \(|C|\) is uniformly bounded, even when \(c\) is complex. Each differentiated exponential is a finite sum of products of derivatives of \(C\) times that exponential. The total number of radial derivatives is the sum in each product, so a term with \(k\) radial derivatives has factor \(R^{-k}\). Base and moving-endpoint derivatives have bounded coefficients. Differentiating the integral therefore gives order \(r-k\) after \(k\) radial derivatives. Differentiation in \(t\) verifies the equation and initial condition, with exactly the signs displayed. The integrating factor proves uniqueness. In time-parallel symbol-line frames the transition is independent of \(t\) and has degree zero; multiplying the local scalar solution by that transition proves gluing by uniqueness. Outside the closed hull, the finite cover of the compact interpolation image makes \(g\) rapidly decreasing with every derivative. The bounded exponential estimates preserve that arbitrary decay. This proves every assertion. ∎

For completeness, the scalar product formula needed with these lower terms is also valid in the ordinary class. Let \(P\) be properly supported on half densities, with degree-one homogeneous principal symbol \(p\) and full local left symbol \(p+r_0\), where \(r_0\in S^0\). Suppose \(p\) vanishes on the first projection of the characteristic relation. Both endpoint covectors are nonzero; on each compact graph angular box, the first frequency is comparable to the full joint frequency. Thus the \(S^0\) estimates for \(r_0(x,\xi)\) give the required ordinary estimates in the joint graph variables. The full proof in Sections 5–7 of the transport lesson applies with \(r_0\) in place of its homogeneous lower term. The principal Taylor integral and integration by parts are unchanged. The additional amplitude is \(r_0b\), of the same next order; every further Fourier reduction lowers it by one because every frequency derivative of \(r_0\) loses one order. Consequently
\[
PA\in I^r(X\times X,C'),\qquad
\sigma(PA)=\frac1i\mathcal L_V\sigma(A)+c\sigma(A)
\pmod{S^{r+n/2-1}},
\quad c=r_0+\frac i2\sum_jp_{x_j\xi_j}\quad\text{on }C.
\tag{KC10}
\]

The coefficient defines an intrinsic scalar class. The symbol of \(PA\) and the Maslov-valued Lie derivative are intrinsic by the programme symbol theorem. Their difference is multiplication by the locally computed \(c\). At each point, controlled realization supplies an elliptic local symbol section; comparing its two representations shows that the scalar coefficients on overlapping charts differ by \(S^{-1}\). A locally finite partition of the conic quotient therefore gives a global ordinary \(S^0\) representative of this class. Replacing \(c\) by another such representative changes (KC10) by precisely the one-lower-order denominator. This is sufficient for every step of the correction, and (KC9) solves the equation for whichever global representative was chosen. These arguments retain arbitrary ordinary order-zero lower terms.

## 4. The complete directional kernel correction

Assume the global real-principal-type and compact-return hypotheses of the two preceding lessons. Use a normalized degree-one homogeneous principal symbol and the ordinary scalar half-density operator in (KC10). Its properly supported action is defined even on kernels that are not proper. Write \(n=\dim X\), and let \(C'\) include the negative input covector convention. If the characteristic set is empty, every \(I^r(X\times X,C')\) kernel is smooth and the assertion below is vacuous with \(A=0\).

**Kernel correction theorem.** Let \(F\in I^r(X\times X,C')\) and let its wavefront relation \(S=\operatorname{WF}'(F)\) be contained in \(C^+\). Define the closed reflexive hull
\[
K=\mathcal H_+(S)=(\Delta^*\cup C^+)\circ S\subset C^+.
\tag{KC11}
\]
Then there is
\[
A\in I^r(X\times X,C'),\qquad PA-F\in C^\infty(X\times X),\qquad
\operatorname{WF}'(A)\subset K.
\tag{KC12}
\]
The backward assertion holds with \(\mathcal H_-\) and \(C^-\). The order is the original real \(r\), without a gain or loss in this normalized correction.

**Proof.** The preceding lesson proves that \(K\) is closed in the full ambient punctured product cotangent space and is contained in \(C^+\). In coordinates, its membership means that some forcing time \(b\) satisfies \(s<b\leq t\). If a point lies in \(\mathcal H_+(K)\), choose its intermediate time \(v\in[s,t]\), and then a forcing witness \(b\in[s,v]\). The inequalities combine to \(s<b\leq t\). Conversely the zero-time part of the hull includes every point of \(K\). Thus
\[
\mathcal H_+(K)=K.
\tag{KC13}
\]

The principal symbol of \(F\) has a representative with microsupport in \(S\). Indeed in each graph chart take the full compactly localized Fourier coefficient in the symbol theorem. Wavefront exclusion gives rapid decay off \(S\); multiplying by the symbol-line transitions and a partition preserves that exclusion. Their locally finite sum represents the same principal class and still has microsupport in \(S\).

Solve the zero-diagonal symbol equation for that representative by (KC9), in the degree-\(n/2\), time-parallel frame constructed in the preceding lesson. The intrinsic symbol order is \(r+n/2\). Its solution \(a_0\) has the same order and microsupport in \(K\). Apply controlled realization, with \(Y=X\times X\) of dimension \(2n\), to obtain \(A_0\in I^r(C')\) and \(\operatorname{WF}'(A_0)\subset K\). Formula (KC10) and the exact kernel of the principal-symbol map give
\[
F-PA_0\in I^{r-1}(C').
\tag{KC14}
\]
Pseudolocality of the properly supported first-factor operator and the initial inclusion \(S\subset K\) give wavefront in \(K\) for this residual.

Repeat this argument with the actual residual, retaining its sign. If \(A_0,\ldots,A_{j-1}\) have already been chosen, put
\[
F_j=F-P\sum_{k<j}A_k\in I^{r-j}(C').
\tag{KC15}
\]
Choose a representative of its principal symbol with microsupport in \(K\), using the same graph argument. Its zero-diagonal transport solution has microsupport in \(\mathcal H_+(K)=K\) and order \(r-j+n/2\). Use the same fixed graph boxes and controlled realization to choose \(A_j\in I^{r-j}(C')\), with wavefront in \(K\). The next residual is \(F_j-PA_j\in I^{r-j-1}\), again with wavefront in \(K\). This proves the induction at every integer \(j\); the initial order \(r\) may be any real number.

Use the controlled kernel summation (KC5) for this actual sequence. It gives \(A\in I^r\), with wavefront in \(K\), and each required lower-order remainder. For every \(J\), subtract the finite sum in (KC15). The product formula sends its \(I^{r-J-1}\) remainder into the same class, because the degree-one principal symbol vanishes on \(C'\). The finite residual is already in that class. Thus \(PA-F\in I^{r-J-1}\) for every \(J\). The complete intersection-of-orders theorem in the intrinsic lesson gives a smooth kernel. This proves (KC12). Reversing the time orientation gives the backward proof, with the same signs in the differential equation and the oriented integral (KC9). ∎

This proves the corrected support-controlled content of the normalized correction lemma. The strict composition \(C^+\circ S\) can omit a forcing boundary, as the preceding exact kernel example proves. The reflexive hull retains it and stays within the prescribed open signed relation.

## 5. Exercises with complete solutions

**1. Idempotence and the two time orientations (introductory).** In one full-time trajectory chart take \(S=\{(q_0,b,s,R):b\in[0,1],\ s\in[-2,-1],\ R>0\}\). Compute its reflexive forward hull, its strict forward composition, and the hull of its reflexive hull. State the corresponding result after reversing time.

**Solution.** A source witness is any \(b\in[0,1]\) with \(b\leq t\). Such a witness exists exactly when \(t\geq0\). Hence the reflexive hull is \(\{(q_0,t,s,R):t\geq0,\ s\in[-2,-1],\ R>0\}\). The strict composition requires \(b<t\), so exists exactly when \(t>0\). The zero-time boundary is lost in the latter. Taking a further reflexive hull gives a witness \(v\geq0\) with \(v\leq t\), again equivalent to \(t\geq0\). This proves idempotence in the example. In the full proof the nested inequalities \(s<b\leq v\leq t\) prove the same assertion on incomplete trajectories. Reversing time sends the forcing interval to \([-1,0]\), input times to \([1,2]\), and the correction to output times \(t\leq0\); strict backward travel retains only \(t<0\). A second reflexive backward hull is unchanged. All these sets are closed in their ambient punctured trajectory coordinates, and the negative or positive gap between input and source excludes the characteristic diagonal.

**2. An infinite sum of smooth kernels can be singular (advanced).** Choose \(\psi\in C_c^\infty((1,2))\), equal to one near \(3/2\), and let
\[
b_j(\xi)=\psi(\xi/4^j),\qquad b=\sum_{j\geq1}b_j,\qquad u=\mathcal F^{-1}b
\tag{KC16}
\]
on the line. Prove that every \(\mathcal F^{-1}b_j\) is smooth, that \(b\in S^0\), and that \(\operatorname{WF}(u)=\{(0,\xi):\xi>0\}\). Explain why this sum is not an asymptotic sum of the smoothing terms.

**Solution.** Each \(b_j\) is smooth with compact frequency support, so its inverse transform is Schwartz. The annuli \((4^j,2\cdot4^j)\) are disjoint. At any high frequency at most one term contributes, and a derivative of order \(k\) is bounded by \(C_k4^{-jk}\leq C'_k\langle\xi\rangle^{-k}\). The sum is locally finite, hence smooth, and these bounds give \(S^0\). It is also the distributional sum of the inverse transforms: pairing with a Schwartz test bounds the sum of the absolute frequency integrals by the integral of its rapidly decreasing transform over the disjoint annuli, times the uniform bound for \(b_j\). It vanishes at negative frequency. The graph inverse criterion with \(H=0\) puts \(u\) in \(I^{1/4}(\mathbb R,T^*_0\mathbb R)\), so there is no wavefront away from zero. Negative directions are rapidly decreasing after compact spatial localization: in the convolution formula positive input frequency and negative output frequency have separation comparable to their combined sizes, and the cutoff transform absorbs every power.

For a compact smooth \(\chi\) with \(\chi(0)\ne0\), the exact Fourier formula is
\[
\widehat{\chi u}(\eta)=(2\pi)^{-1}\int\widehat\chi(v)b(\eta-v)\,dv.
\tag{KC17}
\]
At \(\eta_j=(3/2)4^j\), the factor \(b(\eta_j-v)\) is one whenever \(|v|\leq\delta4^j\), for a fixed sufficiently small \(\delta>0\). Everywhere it is uniformly bounded. Rapid decrease of \(\widehat\chi\) makes the remaining integral tend to zero, with arbitrary inverse powers of \(4^j\). Therefore \(\widehat{\chi u}(\eta_j)\to(2\pi)^{-1}\int\widehat\chi(v)\,dv=\chi(0)\ne0\). Every positive conic neighborhood has these frequencies, so the positive covectors at zero belong to the wavefront set. This proves the exact equality. If the displayed sum were asymptotic to its smoothing terms in orders tending to minus infinity, its remainder after every finite sum would have every successively prescribed lower order; because each finite sum is smoothing, this would make \(b\) rapidly decreasing. The values \(b(\eta_j)=1\) contradict that conclusion. Local finiteness supplied a distribution but not the asymptotic estimates or wavefront control.

**3. A coefficient with no homogeneous limit (intermediate).** For \(R\geq2\), put \(c(R)=\sin(\log R)\), extended smoothly at smaller positive radii. Solve
\[
\frac1i\partial_tu+c(R)u=R^r,\qquad u(s,s,R)=0,
\tag{KC18}
\]
for arbitrary real \(r\), and prove all ordinary radial symbol bounds through the infinitely many zeros of \(c\).

**Solution.** Every \(k\)-th radial derivative of \(c\) is \(R^{-k}\) times a bounded linear combination of sine and cosine. Thus \(c\in S^0\); its oscillation as \(R\to\infty\) precludes a homogeneous degree-zero leading limit. With \(d=t-s\), the solution is
\[
u=R^r\frac{1-e^{-ic(R)d}}{c(R)}
=iR^r\int_0^d e^{-ic(R)(d-b)}\,db.
\tag{KC19}
\]
The integral defines the removable value \(iR^rd\) at every zero of \(c\). Differentiation gives \((1/i)\partial_tu=R^re^{-icd}\); adding \(cu=R^r(1-e^{-icd})\) proves the equation, and \(d=0\) proves the initial condition. On bounded time intervals all derivatives of the integral with respect to \(c\) and \(d\) are bounded. Applying the full chain rule, a term with \(k\) radial derivatives has products of derivatives of \(c\) of total radial order at most \(k\), and derivatives of \(R^r\) of the complementary order. It is bounded by \(C_kR^{r-k}\). Mixed time derivatives satisfy the same radial loss. These estimates hold uniformly at the zeros; using the quotient without its removable integral expression would falsely suggest a singular coefficient. This is an ordinary-symbol transport solution, without a homogeneous lower expansion.

## 6. The remaining global parametrix construction

The kernel correction theorem is now supplied with its actual distribution realization and infinite sum. The complete global parametrix theorem additionally requires local inverses near the diagonal with the precise signed residual order, compact-middle composition and uniqueness for kernels that are not properly supported, conversion of a one-sided construction into both identities, the exact all-real Sobolev gain, and nonvanishing of the difference symbol on the entire characteristic relation. General real operator order also requires the exact positive elliptic reduction, and disconnected characteristic components require the stated sign choices. These remain substantive owned construction steps.

## References and scope

Hörmander IV, Lemma 26.1.16, printed 72–73/PDF 83–84, is the consulted antecedent for the normalized iterative correction. The preceding directional lesson supplies the exact kernel qualification of its literal strict support bound. The ordinary symbol summation proof is supplied by the programme AN-03 lesson cited above, under its recorded licence; the added microsupport conditions and kernel argument are supplied here. The remaining full global parametrix construction is described in Section 6.
