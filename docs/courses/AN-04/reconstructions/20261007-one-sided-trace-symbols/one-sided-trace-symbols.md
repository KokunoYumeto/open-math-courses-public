# Complete symbols of one-sided boundary traces

The half-space companion proves that the finite inverse acts on the entire boundary source and that its layers have one-sided traces. Here we identify those traces as actual tangential operators. The calculation retains the full tangential composition, every coefficient derivative in the source, every output normal derivative, and both finite inverse errors. A principal symbol alone would not specify these operators.

This original exposition is CC0. The mathematical antecedent is the Hörmander III, Springer 2007, ISBN 978-3-540-49938-1, Section 20.1. The existing AN-03 *Fredholm boundary problems with first-order Calderón defects*, Section 21, gives a related treatment of the full trace and measurement formulas. We use the finite model already proved in HM to obtain the normal integral directly. The proof map records the exact earlier proofs and source versions. Linked components retain their own licences.

## 1. The precise normal integral problem

Retain the product collar, inward normal \(r\), convention \(D_r=-i\partial_r\), and frequencies \((\eta,\kappa)\). Write
\[
 T=1+|\eta|,\qquad R=1+|(\eta,\kappa)|,\qquad
 \lambda=\sqrt{1+|\eta|^2},\qquad q=\sqrt{\lambda^2+\kappa^2}.
 \tag{TS1}
\]
The Fourier inverse coefficient is \((2\pi)^{-d-1}\), where \(d\) is the tangential dimension. All localizations retain the actual input density and distinct source and target bundle frames. Preferred changes leave the normal coordinate fixed, as in GC:T1–T2.

Throughout this companion \(\Psi^s\) denotes ordinary tangential \(S^s_{1,0}\) quantization with the full kernel retained. The homogeneous leading expansion of the specific finite inverse belongs to the subsequent stable-symbol calculation.

Let \(h(y,r,\eta,\kappa)\) be a matrix symbol, with integer normal degree \(\mu\) and real tangential order \(\ell\). Assume the full mixed estimates and the common two-tail expansion
\[
 \begin{aligned}
 |\partial_{y,r}^{\beta}\partial_\eta^\alpha\partial_\kappa^v h|
    &\le C R^{\mu-v}T^{\ell-|\alpha|},\\
 \left|\partial_{y,r}^{\beta}\partial_\eta^\alpha\partial_\kappa^v
   \left(h-\sum_{n<L}h_n(y,r,\eta)\kappa^{\mu-n}\right)\right|
    &\le C_L|\kappa|^{\mu-L-v}T^{\ell+L-|\alpha|}
                    \quad (|\kappa|\ge CT),\\
 h_n&\in S_{\rm tan}^{\ell+n}.
 \end{aligned}
 \tag{TS2}
\]
Every derivative and every finite length \(L\ge1\) is included. The same coefficients are required on the positive and negative tails. All constants are uniform on the fixed collar localization. They may depend on the requested derivatives and length.

The [half-space proof](../20261007-halfspace-layers/halfspace-layers.md), HM:M1–M3, constructs the needed model when \(\ell=0\). Its full argument extends to TS2 with a fixed factor \(T^\ell\); we give the estimates below. The [mixed calculus](../20261007-mixed-boundary-calculus/mixed-boundary-calculus.md), MB:E1–F1, provides actual Fourier kernels and their distributional domains. The [paired composition proof](../20261007-paired-normal-composition/paired-normal-composition.md), PN:T1 and its weighted tangential calculation, and the [global collar proof](../20261007-global-collar-inverse/global-collar-inverse.md), GC:T1–H1, supply the complete products and coordinate transport. MH:TR1–TR3 and HM:T1 supply the already proved one-sided trace bounds.

## 2. A subtraction with a known support direction

For a finite length \(L\), define the complete coefficient symbols
\[
 u_0=h_0,\qquad
 u_n=h_n-\sum_{j<n}\binom{\mu-j}{n-j}
                       u_j(i\lambda)^{n-j},\qquad
 v_L=\sum_{j<L}u_j(\kappa+i\lambda)^{\mu-j}.
 \tag{TS3}
\]
The coefficients are matrices and their order is fixed. Multiplication by the scalar factor is on the right; it represents the exact right tangential Fourier multiplier, so it creates no omitted composition terms. Induction gives \(u_j\in S_{\rm tan}^{\ell+j}\) with every base derivative.

The coefficient of \(\kappa^{\mu-n}\) in TS3 is exactly \(h_n\). To control the remainder, apply the real-parameter Taylor integral to \((1+tz)^{\mu-j}\), with \(z=i\lambda/\kappa\), \(0\le t\le1\), and \(|z|\le1/2\). Derivatives of this rational function are bounded because \(|1+tz|\ge1/2\); nonnegative exponents give the same finite polynomial calculation. Before multiplying by \(u_j\), the length-\(L-j\) remainder has bound \(C|\kappa|^{\mu-L-v}T^{L-j-|\alpha|}\). The product rule and the order \(\ell+j\) of \(u_j\) therefore give
\[
 g_L=h-v_L\in S^{\mu-L,\ell+L},\qquad
 |\partial_{y,r}^{\beta}\partial_\eta^\alpha\partial_\kappa^v g_L|
       \le C R^{\mu-L-v}T^{\ell+L-|\alpha|}.
 \tag{TS4}
\]
This proves the estimate on both high-normal cones. On the remaining region \(|\kappa|\le C'T\), use \(|\kappa+i\lambda|=q\) and comparability of \(R,T,q,\lambda\) there. Every differentiated original or model term is bounded by \(CT^{\mu+\ell-v-|\alpha|}\), exactly TS4 on that region. The bounds for derivatives of \(\lambda\) are MH:B2. Thus every derivative in TS4 is proved globally. Each full model summand also has order \((\mu,\ell)\), since
\(R^{\mu-j-v}T^{\ell+j-|\alpha|}\le R^{\mu-v}T^{\ell-|\alpha|}\).

At fixed \((y,r,\eta)\), every model summand has inverse normal Fourier support in \(\theta\le0\), where \(\theta\) denotes output minus input normal. For negative powers the exact kernel is HM18:
\[
 \mathcal F_\kappa^{-1}[(\kappa+i\lambda)^{-h}](\theta)
       =\frac{(-i)^h}{(h-1)!}
          1_{\theta<0}(-\theta)^{h-1}e^{\lambda\theta},
                 \qquad h\ge1.
 \tag{TS5}
\]
For nonnegative powers it is the corresponding finite sum of normal delta derivatives at zero. This is an actual tested Fourier identity, proved by the convergent Laplace integral in HM:M2. Coefficient multiplication and any finite normal differentiation preserve the support relation. We will use the zero restriction on \(\theta>0\), not a chosen value of those model distributions at zero.

## 3. The integral and all tangential estimates

Choose an integer \(L\ge1\) with \(L>\mu+1\). Define the unnormalized positive normal integral and its trace symbol by
\[
 \mathcal J_+(h)(y,r,\eta)
       =\int_{\mathbb R}(h-v_L)(y,r,\eta,\kappa)\,d\kappa,
 \qquad
 \operatorname{tr}_+h(y,\eta)
       =(2\pi)^{-1}\mathcal J_+(h)(y,0,\eta).
 \tag{TS6}
\]
These are ordinary absolutely convergent integrals after the stated subtraction. They are not symmetric principal values of \(h\).

From TS4 and the comparison of smooth and original weights, each requested base and tangential derivative is bounded by
\[
 C\lambda^{\ell+L-|\alpha|}
     \int_{\mathbb R}(\lambda^2+\kappa^2)^{(\mu-L)/2}\,d\kappa
   =C c_{\mu-L}\lambda^{\mu+\ell+1-|\alpha|},
 \quad
 c_p=\int_{\mathbb R}(1+z^2)^{p/2}\,dz<\infty\quad(p<-1).
 \tag{TS7}
\]
The equality is \(\kappa=\lambda z\), including its Jacobian. Integrability follows from \(p<-1\) on the two tails. On a compact set of the parameters, TS4 supplies an integrable majorant for every prescribed derivative, so differentiation under the integral is justified by P3:M4 and domination. Estimate TS7 then holds at every parameter value. In particular
\[
 \mathcal J_+(h)\in S_{\rm tan}^{\mu+\ell+1}
 \quad\text{uniformly with every }y,r\text{ derivative},
 \qquad
 \operatorname{tr}_+h\in S_{\rm tan}^{\mu+\ell+1}.
 \tag{TS8}
\]
The bounds use finitely many of the original seminorms for each requested seminorm. No derivative of \(1+|\eta|\) is taken. If there is no tangential variable, \(\lambda=1\) and the same one-dimensional integral proves the statement.

The definition is independent of \(L\). Indeed, for two admissible lengths the difference of their model symbols is integrable in \(\kappa\), because each differs from \(h\) by an integrable function. Its inverse Fourier transform is continuous in \(\theta\), by dominated convergence, and has support in \(\theta\le0\) by TS5. Its value at zero is therefore zero. Fourier inversion for this integrable function identifies that value with \((2\pi)^{-1}\) times its integral. The two integrals in TS6 agree. This also proves independence if \(\lambda\) in the model is replaced everywhere by \(c\lambda\), for any fixed \(c>0\): TS3–TS5 and the integrable-difference argument remain valid, with constants depending on \(c\).

More generally, an integrable difference from \(h\) may be formed with any finite polynomial or rational model whose inverse normal transform is supported on the negative side. Its integral gives the same value whenever the difference between that model and a TS3 model is integrable. This follows from the same continuous-kernel argument. It covers multiplication of a model by powers of \(\kappa\) and differentiation of its coefficient parameters, exactly the operations needed below.

The construction is linear. For different declared integer normal degrees, first raise them to a common degree by inserting zero leading coefficients. Those leading zeros are forced by the two-tail expansion and its uniqueness at fixed parameters. Recursion TS3 then just shifts the index, producing the same model after the corresponding shift of its length. Thus linearity does not depend on an arbitrary choice of a larger declared order. When \(h\) itself is absolutely integrable in the normal frequency, its inverse kernel is continuous at zero. The model is then integrable too and has zero integral by TS5, so TS6 agrees with the ordinary integral.

## 4. Why this is the actual one-sided trace

Consider the inverse normal transform at input normal zero, initially as a tempered distribution. For \(r>0\), the exact model part vanishes, even though its coefficients depend on the output parameter \(r\). Therefore its actual value there is
\[
 K_h(y,r,\eta)
     =(2\pi)^{-1}\int_{\mathbb R}e^{ir\kappa}
                       g_L(y,r,\eta,\kappa)\,d\kappa.
 \tag{TS9}
\]
The integrable majorant in TS7 and parameter continuity give the limit at \(r\downarrow0\) as \(\operatorname{tr}_+h\). The same proof gives local smooth dependence on \(y,\eta\) and bounds in the order shown in TS8, uniformly for \(0\le r\le\varepsilon\).

For any integer \(k\ge0\), choose the length larger, with \(L>\mu+k+1\). Differentiating the actual kernel with \(D_r=-i\partial_r\) gives the full Leibniz expression
\[
 D_r^kK_h(y,r,\eta)
    =(2\pi)^{-1}\int e^{ir\kappa}
       \sum_{v=0}^{k}\binom{k}{v}
              \kappa^vD_r^{k-v}g_L(y,r,\eta,\kappa)\,d\kappa
              \qquad(r>0).
 \tag{TS10}
\]
Every integral and requested tangential derivative is dominated: the largest normal growth is \(\mu-L+k<-1\). The differentiated model still has zero positive restriction. The alternative-subtraction argument following TS8 applies to each \(\kappa^vD_r^{k-v}v_L\). Consequently the exact one-sided derivative is
\[
 (D_r^kK_h)|_{0+}
   =\frac1{2\pi}\sum_{v=0}^{k}\binom{k}{v}
        \left.\mathcal J_+\bigl(\kappa^vD_r^{k-v}h\bigr)\right|_{r=0},
 \qquad
 \mathcal J_+(\kappa^vD_r^{k-v}h)
          \in S_{\rm tan}^{\mu+\ell+v+1}.
 \tag{TS11}
\]
No derivative of the coefficient symbol is omitted. A polynomial normal term may be a distribution at the boundary; its positive restriction and every positive-side derivative are zero, as the argument requires.

For a smooth compactly supported tangential input, its Fourier transform decreases faster than any polynomial. The uniform bounds just proved, also after output tangential derivatives, permit the tangential Fourier integral and all these one-sided limits to be interchanged by domination. Thus TS9–TS11 are actual smooth one-sided layer values on such inputs, not merely formal coefficient identities. We claim local parameter convergence with uniform symbol bounds, not convergence in the same global symbol seminorm at all frequencies: even \(e^{-r\lambda}\to1\) fails to converge uniformly in \(\eta\) as \(r\downarrow0\). The smooth-input argument and the earlier HM trace bounds provide the required operator interpretation.

## 5. Complete tangential composition before the trace

Let \(Q_N:F_Y\to E_Y\) be the actual finite inverse from GC:F1, with exact localized left symbol \(q_N\), paired normal degree \(-m\), and complete normal coefficient operators \(C_n(r)\in\Psi^n(F_Y,E_Y)\). Let \(F:E_Y\to F_Y\) be an actual boundary tangential operator of order \(f\), with symbol \(f_F\). Extend this boundary operator constantly in the input normal when forming the layer. Its coefficient derivatives have already been included in the boundary source; introducing another variable-normal extension here would change that source.

The complete symbol of the composition is \(q_N\#_{\rm tan}f_F\), and it satisfies TS2 with
\[
 \mu=-m,\qquad \ell=f,\qquad
 \text{complete normal coefficient }C_n(r)F\in\Psi^{n+f}.
 \tag{TS12}
\]
Here is the exact estimate. On a localized chart, Fourier transform the compact tangential base variable of the right factor as in PN3. The absolute product formula is
\[
 (q_N\#_{\rm tan}f_F)(y,r,\eta,\kappa)
  =(2\pi)^{-d}\int q_N(y,r,\eta+\zeta,\kappa)
       \widehat f_{F,y}(\zeta;\eta)\,d\zeta.
 \tag{TS13}
\]
The transformed factor has arbitrarily large inverse powers of \(1+|\zeta|\), with its original order \(T^f\) and every requested derivative, by compact-base integration by parts. The two weight comparisons in PN5 transfer shifted weights to \((\eta,\kappa)\) with only polynomial powers of the shift. Their product is integrable after sufficiently many integrations by parts, giving the low mixed bound \(R^{-m-v}T^{f-|\alpha|}\) and differentiation under the integral.

On a high-normal cone split the shift at \(|\zeta|=\varepsilon|\kappa|\). After increasing the cone constant, both unshifted and shifted frequencies satisfy the normal expansion on the smaller region. Inserting a length-\(L\) expansion gives remainder \(|\kappa|^{-m-L-v}T^{f+L-|\alpha|}\), by the same weight comparisons. Restoring the removed coefficient tails yields the full tangential product \(C_nF\), since the coefficient integral is exactly the ordinary tangential composition. On the complementary shift region, take more compact-base integrations by parts than the desired normal decay, dimension, polynomial shift growth and prescribed derivative count. Its integral over \(|\zeta|\ge c|\kappa|\) then gives an arbitrary inverse normal power. This bounds both the original product tail and each restored coefficient tail. Derivatives of the splitting cutoff live in that same region and introduce further inverse normal powers. These are precisely the weighted tangential estimates proved in PN:T1; the displayed argument identifies their original factor \(T^f\) and every complete coefficient here.

Input cutoffs and density factors remain inside the exact right factor of TS13. Off the tangential diagonal, use the finite intermediate partition from PN:T1. A separated factor has a smooth kernel with arbitrary inverse tangential powers; high intermediate tangential frequencies give arbitrary inverse normal powers, and low frequencies give the same complete coefficient and remainder bounds. Thus the separated normal amplitudes are smooth in the two independent tangential variables and retain the full coefficients \(C_nF\). A smooth full-kernel term in \(Q_N\) is included in its exact left symbol or retained separately as its actual kernel; it is never dropped from the composition.

## 6. Every term of the original boundary source

Use the original polynomial \(P_c=\sum_{\ell=0}^m A_\ell(r)D_r^\ell:E_Y\to F_Y\), where \(A_\ell\in\Psi^{m-\ell}\). HM:S1–S2 proved the complete source with all coefficient derivatives. Write its terms as
\[
 \begin{aligned}
 F_{ba}^{(q)}&=i^{q-1}\binom{b+q}{q}
          (\partial_r^q A_{a+b+q+1})(0):E_Y\to F_Y,\\
 C_PU&=\sum_{\substack{a,b,q\ge0\\a+b+q\le m-1}}
                    F_{ba}^{(q)}U_a\otimes D_r^b\delta_0,
 \qquad
 \operatorname{ord}F_{ba}^{(q)}\le m-a-b-q-1.
 \end{aligned}
 \tag{TS14}
\]
The \(q=0\) part is the source with coefficients frozen at zero; the higher \(q\) parts are the full supported source defect. The inverse itself is not frozen.

For a term in TS14, transpose the input distribution against the exact kernel of \(Q_NF_{ba}^{(q)}\). The equality \(\langle D_s^b\delta_0,\phi\rangle=i^b\phi^{(b)}(0)\), together with the phase \(e^{-is\kappa}\), gives \(\kappa^b\). In an exact left normal representation, no other input-normal derivative is present. Now differentiate the positive output \(k\) times and apply TS11. The complete local trace symbol is
\[
 G_{kba}^{(N,q)}(y,\eta)
    =\frac1{2\pi}\sum_{v=0}^{k}\binom{k}{v}
       \left.\mathcal J_+\!\left(
         \kappa^{b+v}D_r^{k-v}
              (q_N\#_{\rm tan}f_{F_{ba}^{(q)}})
       \right)\right|_{r=0}(y,\eta).
 \tag{TS15}
\]
The order of the two tangential factors is literal. The operator \(F_{ba}^{(q)}\) is the fixed boundary coefficient from TS14; hence \(D_r\) in this formula differentiates the actual inverse and its output parameter factors.

For the summand indexed by \(v\), TS12 gives normal degree \(b+v-m\) and tangential order \(m-a-b-q-1\). TS8 therefore gives
\[
 \operatorname{ord}_{\rm tan}\text{(that summand)}
       \le v-a-q,\qquad
 G_{kba}^{(N,q)}\in S_{\rm tan}^{k-a-q}.
 \tag{TS16}
\]
This is valid for every integer \(k\ge0\). The inverse correction length \(N\) and subtraction length \(L\) are independent: each fixed actual \(Q_N\) has an expansion to every finite normal length. In fact \(L\ge k+1\) suffices for all terms of TS14, since \(b\le m-1\) and \(-m+b+k-L<-1\). There is no artificial restriction \(k<N\).

## 7. Exact kernels across the coordinate pieces

The local formula includes every smooth full-kernel contribution. In a common chart, take the exact left symbol obtained from the whole localized kernel, including its smoothing part; P2:OP4–OP5 and the mixed representation in MB:E2 identify that actual symbol. A smooth contribution has an absolutely convergent normal integral after every derivative and is covered directly by TS6. If it is stored separately, its boundary trace is added as its actual smooth tangential kernel.

A normal properness cutoff is identically one near \(r=s\). For an input supported at \(s=0\), all its derivatives vanish when \(r>0\) is sufficiently close to zero. It therefore contributes no lost cutoff terms to the one-sided boundary formula. This observation applies only to changes vanishing near the normal diagonal. It does not justify discarding an arbitrary smooth kernel near \((r,s)=(0,0)\).

For separated tangential chart pieces, use the left normal amplitudes from PN:C2, including their complete smooth two-point coefficients and all base derivatives. The fixed-pole version of TS3, with \(\lambda=1\), makes the remainder integrable after any prescribed source and output derivatives. The resulting normal integral is smooth in both tangential variables, with every derivative bounded on the compact piece. It is an actual smooth tangential kernel. If one works first with an unreduced amplitude \(a(y,z,r,s,\kappa)\), the input derivative must instead be expanded as
\[
 i^b\partial_s^b\bigl(e^{-is\kappa}a\bigr)\big|_{s=0}
     =\sum_{t=0}^{b}\binom bt\kappa^{b-t}
                          (i\partial_s)^t a\big|_{s=0}.
 \tag{TS17}
\]
Every term is retained before the exact left normal reduction. The defining all-base estimates in PN:C2 apply to them, and the preceding integrable-remainder argument gives the same smooth tangential trace. Thus input-amplitude derivatives are accounted for rather than silently suppressed.

Preferred coordinate, frame and density transfers are independent of the normal variable, so they commute with taking the one-sided normal limit on smooth inputs. GC:T1–T2 identifies their exact kernel transport, including the two distinct bundle matrices. A finite partition gives a global tangential operator for each term in TS15. Its common-chart symbols have order TS16, and its different-chart pieces are the smooth kernels just proved. HM:T1 bounds the same one-sided trace on the relevant rough data. Equality on smooth data, followed by density in the boundary Sobolev spaces, identifies the global tangential operator with that already constructed trace.

## 8. Cauchy data, measurements and the original orders

For \(0\le k,a<m\), define the actual finite-layer Cauchy matrix by
\[
 (\mathsf C_N)_{ka}
      =\gamma_k r^+Q_NC_P\big|_{U_a}
      =\sum_{b=0}^{m-1-a}\sum_{q=0}^{m-1-a-b}
                         G_{kba}^{(N,q)}.
 \tag{TS18}
\]
The symbols and separate smooth kernels in the right side are interpreted as their complete global operators. The preceding sections prove equality, not just equality modulo lower order. Its entry order is at most \(k-a\). Keeping only \(q=0\) defines the source-frozen matrix \(\mathsf C_N^{\rm src}\) for the same \(Q_N\), and
\[
 (\mathsf C_N-\mathsf C_N^{\rm src})_{ka}
     =\sum_{\substack{b\ge0,\ q\ge1\\a+b+q\le m-1}}
                        G_{kba}^{(N,q)}
       \in\Psi^{k-a-1}(Y;E_Y).
 \tag{TS19}
\]
Every individual \(q\)-part has the sharper order \(k-a-q\). Empty sums are zero, especially when \(m=1\); cancellations can make an order smaller still.

Keep the original boundary measurements
\[
 B_j=\sum_{k=0}^{m-1}B_{jk}\gamma_k,
       \qquad B_{jk}\in\Psi^{m_j-k}(E_Y,G_j),
       \qquad m_j\in\mathbb Z.
 \tag{TS20}
\]
There is no imposed upper bound on \(m_j\). The measured layer is
\[
 (\mathsf M_N)_{ja}
      =\sum_{k=0}^{m-1}B_{jk}(\mathsf C_N)_{ka},\qquad
 (\mathsf M_N-\mathsf M_N^{\rm src})_{ja}
      =\sum_{k=0}^{m-1}B_{jk}
                    (\mathsf C_N-\mathsf C_N^{\rm src})_{ka}
        \in\Psi^{m_j-a-1}(E_Y,G_j).
 \tag{TS21}
\]
Every \(B_{jk}\) remains on the left. Exact tangential composition is P2:OP3–OP6; the \(q\)-part has order \(m_j-a-q\).

For every real \(\sigma\), set
\[
 \mathcal U_\sigma=\bigoplus_{a=0}^{m-1}H^{\sigma-a-1/2}(Y,E_Y),
       \qquad
 \mathcal D_\sigma=\bigoplus_jH^{\sigma-m_j-1/2}(Y,G_j).
 \tag{TS22}
\]
The proved tangential Sobolev map at each entry gives
\[
 \mathsf C_N:\mathcal U_\sigma\to\mathcal U_\sigma,\qquad
 \mathsf M_N:\mathcal U_\sigma\to\mathcal D_\sigma,\qquad
 \mathsf M_N-\mathsf M_N^{\rm src}:\mathcal U_\sigma\to\mathcal D_{\sigma+1}.
 \tag{TS23}
\]
Finite sums and the exact exponents in TS16 prove these bounds directly. They concern boundary data fed into the finite layer. No trace of an arbitrary low-regularity volume distribution is inferred from them.

## 9. What changing the finite inverse can change

Suppose \(Q_N\) and \(\widetilde Q_M\) are two actual finite inverses for the same cylinder operator, with the two corresponding errors of paired degrees \(-N\) and \(-M\). GC:F1 gives the ordered identity
\[
 \widetilde Q_M-Q_N
   =Q_N(P_c\widetilde Q_M-I_F)
                -(Q_NP_c-I_E)\widetilde Q_M
      \in\mathcal L^{-m-K},\qquad K=\min(N,M).
 \tag{TS24}
\]
The algebra follows by expanding the two products; PN:T1 gives the stated class without commuting factors. Applying the complete trace proof with normal degree \(-m-K\) gives, for each original source part,
\[
 \operatorname{ord}\bigl(
   \gamma_k r^+(\widetilde Q_M-Q_N)
       (F_{ba}^{(q)}\,\cdot\,\otimes D_r^b\delta_0)\bigr)
             \le k-a-q-K.
 \tag{TS25}
\]
Thus the two Cauchy matrices differ entrywise by order at most \(k-a-K\); their measured matrices differ by order at most \(m_j-a-K\). In particular their leading weighted symbols agree. This is a finite-order independence statement for a fixed original \(P_c\), not an exact identity of all finite inverses or a claim about a different collar.

The two interior identities remain
\[
 Q_NP_c=I_E-(-\mathcal R_E)^N,\qquad
 P_cQ_N=I_F-(-\mathcal R_F)^N.
 \tag{TS26}
\]
Neither TS18 nor these distinct error identities proves that \(\mathsf C_N\) is an exact projection. Identifying the stable principal subspace and proving the appropriate projection and boundary inverse statements are the next mathematical steps.

## 10. Four complete examples

**1. A symmetric principal value loses the one-sided term.** Let \(\lambda>0\) be fixed and \(h(\kappa)=\kappa/(\kappa^2+\lambda^2)\). Its leading normal term is \(\kappa^{-1}\). The length-one model \((\kappa+i\lambda)^{-1}\) is sufficient because
\[
 h-(\kappa+i\lambda)^{-1}
       =\frac{i\lambda}{\kappa^2+\lambda^2},\qquad
 \mathcal J_+(h)=i\pi,\qquad
 \operatorname{tr}_+h=\frac i2.
 \tag{TS27}
\]
The integral follows by \(\kappa=\lambda\tan\theta\), \(-\pi/2<\theta<\pi/2\). In contrast every symmetric finite integral of the odd function \(h\) is zero. To see the one-sided value directly, split \((\kappa^2+\lambda^2)^{-1}\) into its two simple fractions and use TS5 and its reflection. Its inverse kernel is \(e^{-\lambda|r|}/(2\lambda)\). Applying \(D_r\) gives the inverse of \(h\): \((i/2)\operatorname{sgn}(r)e^{-\lambda|r|}\) away from zero. The positive limit is \(i/2\), while the negative limit is \(-i/2\). No point value at zero is assigned to this discontinuous representative.

**2. A full output derivative includes the derivative of the inverse coefficient.** Take, near \(r=0\),
\[
 q_*(r,\eta,\kappa)=\frac{1+c r}{\kappa^2+\lambda(\eta)^2},
               \qquad c\in\mathbb R.
 \tag{TS28}
\]
A compact output cutoff equal to one near zero supplies global base bounds, and a normal properness cutoff equal to one near the diagonal leaves the boundary calculation unchanged. This is an example in \(\mathcal L^{-2}\), without an assertion that it is a specified polynomial's inverse. Its layer for input \(f\delta_0\) has positive normal multiplier \((1+cr)e^{-\lambda r}/(2\lambda)\). Hence
\[
 D_rK_{q_*}|_{0+}=\frac i2-\frac{ic}{2\lambda}.
 \tag{TS29}
\]
Formula TS11 gives exactly the same answer: \((2\pi)^{-1}\mathcal J_+(\kappa q_*|_0)=i/2\), while \((2\pi)^{-1}\mathcal J_+(D_rq_*|_0)=-ic/(2\lambda)\). Dropping the coefficient derivative would erase the second, lower-order but nonzero, part of the complete trace symbol.

**3. The tangential composition is an actual shifted symbol.** On the Euclidean tangential line let
\[
 A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 B=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
 h(\eta,\kappa)=\frac{\eta}{\kappa^2+1+\eta^2}A,
           \qquad F(y)=e^{iy}B.
 \tag{TS30}
\]
The Fourier transform of \(e^{iy}u\) is \(\widehat u(\eta-1)\). Substitution in the full Fourier formula, on Schwartz inputs, gives the exact tangential product
\[
 (h\#_{\rm tan}F)(y,\eta,\kappa)
     =e^{iy}\frac{\eta+1}{\kappa^2+1+(\eta+1)^2}AB,
 \quad
 \operatorname{tr}_+(h\#_{\rm tan}F)
     =e^{iy}\frac{\eta+1}{2\sqrt{1+(\eta+1)^2}}AB.
 \tag{TS31}
\]
The normal integral here converges ordinarily. At \(\eta=0\) the last expression is \(e^{iy}AB/(2\sqrt2)\), whereas pointwise multiplication of the unshifted symbols would give zero. Moreover \(AB=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\) and \(BA=\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\) differ. This global Fourier example tests the exact composition and factor order, rather than asserting a particular compact-boundary inverse.

**4. Higher polynomial growth does not permit symmetric truncation.** For \(h_3(\kappa)=\kappa^3/(\kappa^2+\lambda^2)\), the first three coefficients are \(1,0,-\lambda^2\) at powers \(\kappa^1,\kappa^0,\kappa^{-1}\). TS3 gives the length-three model \(v_3=\kappa-\lambda^2/(\kappa+i\lambda)\). Therefore
\[
 h_3-v_3=-\frac{i\lambda^3}{\kappa^2+\lambda^2},\qquad
 \mathcal J_+(h_3)=-i\pi\lambda^2,
       \qquad \operatorname{tr}_+h_3=-\frac{i\lambda^2}{2}.
 \tag{TS32}
\]
The positive kernel is also \(D_r^3(e^{-\lambda r}/(2\lambda))\), giving the same boundary value. For a pure polynomial, such as \(\kappa^2\), the sufficiently long TS3 model is that polynomial itself; its positive trace is zero. These facts keep the polynomial distributions at zero separate from the nonzero one-sided contribution of the inverse-power tail.

## 11. The two limits in the picture

![At lambda one, the real frequency symbol is odd and has symmetric principal value zero. Subtracting the model leaves imaginary part one over one plus kappa squared. Its integral is pi. The actual inverse kernel has imaginary one-sided limits plus and minus one half.](figures/one-sided-trace.svg)

Both panels concern the exact scalar example TS27 at \(\lambda=1\). Curves are sampled representations of its proved formulas. The finite plotted frequency window omits tails, which remain part of the full integral \(\pi\). Open endpoints on the normal plot indicate the two limits, not assigned values at zero. The figure explains why the positive trace is \(i/2\), despite the zero symmetric principal value. The general trace and source formulas are TS15–TS25; stable-space projection and elliptic boundary regularity remain separate obligations.
