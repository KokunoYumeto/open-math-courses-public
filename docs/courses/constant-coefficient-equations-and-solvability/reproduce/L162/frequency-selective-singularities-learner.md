# Frequency-selective singularities and smooth convolutions

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

A function can be continuous, fail to have a continuous first derivative at one point, and still have extremely small Fourier transform outside chosen neighborhoods. Its remaining Fourier activity can be used to decide whether convolution smooths a nonsmooth factor. The main difficulty is to retain the singularity while enforcing all the exterior decay estimates at once.

Basic references are Tao's *245B, Notes 9* and *246B, Notes 2*, and Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. The exact earlier inputs are Joint logarithmic-frequency limits, for proper and collapsed profiles and joint extraction; Locating singularities through logarithmic Fourier strips, Section 4, for the convex singular hull; Convolution and joint frequency carriers, for proper sums and collapsed products; and Changing centers in Fourier windows, Theorem 3.1, for neighborhood transport. The [complete proof](frequency-selective-singularities-formal.md) provides every kernel estimate, the complete-space and Baire arguments, and the smoothing equivalence.

## 1. A criterion for smoothing a nonsmooth factor

Use
\(F_u(\zeta)=\langle u,e^{-ix\cdot\zeta}\rangle\) and
\(L_u(z,c)=\log|F_u(c+z\log|c|)|/\log|c|\), for real \(|c|>2\).
Functions and distributions may be complex valued.

Theorem 1.1 of the complete proof says that the following are equivalent for a compact distribution \(u\):

- \(L_u\) collapses to \(-\infty\), uniformly on complex parameter compact sets, along some escaping real frequency sequence.
- At every prescribed point \(x_0\), and in every prescribed small support ball about it, there is a compact continuous \(w\notin C^1\), singular exactly at \(x_0\), whose convolution \(u*w\) is smooth.
- Some compact nonsmooth distribution \(w\) has smooth convolution \(u*w\).

The last condition allows a distributional factor; it does not assume continuity. The middle condition yields the stronger continuous factor with exactly one singular point.

The forward argument divides escaping frequencies into two regions. Choose logarithmic neighborhoods where \(L_u\) collapses. Construct \(w\) whose normalized logarithms collapse on their exterior. The exact product identity gives

\[
 L_{u*w}(z,c)=L_u(z,c)+L_w(z,c).
 \tag{S1}
\]

On either region one summand collapses, while the other has a uniform upper bound on the fixed parameter compact set. Thus the sum collapses along all escaping frequencies. The earlier singular-hull theorem then makes the convolution smooth.

Conversely, a nonsmooth compact \(w\) has a proper profile somewhere. Extract a profile of \(u\) along that same sequence. Two proper profiles have a proper sum. A smooth compact convolution has only collapsed profiles, so the \(u\) profile must be collapsed. The shared sequence is indispensable.

## 2. Concentrating the transform without enlarging the support

Let real \(c_j\) escape, \(Q_j=|c_j|\), and \(R_j\to\infty\). On a tail with \(Q_j>e^2\), set

\[
 k_j=\lfloor\log Q_j\rfloor,\qquad
 E=\bigcup_j\{\xi:|\xi-c_j|<R_j\log Q_j\}.
 \tag{S2}
\]

The exterior may be bounded. The construction imposes no small-relative-radius assumption.

Take a smooth nonnegative probability density \(\psi\) supported in a small ball about zero. Set
\(\psi_k(x)=k^n\psi(kx)\), let \(v_k\) be its \(k\)-fold convolution, and modulate by \(e^{ic_j\cdot x}\). Then

\[
 u_j(x)=e^{ic_j\cdot x}v_{k_j}(x),\qquad
 F_{u_j}(\zeta)=
       [F_\psi((\zeta-c_j)/k_j)]^{k_j}.
 \tag{S3}
\]

The \(k\) supports each have radius divided by \(k\), so their sum stays inside the original support ball. Every factor has mass one. Consequently \(F_{u_j}(c_j)=1\), while
\(\|u_j\|_\infty\leq k_j^n\|\psi\|_\infty\).
These are smooth test functions, rather than the nonsmooth function eventually selected.

![A smooth compact probability bump and numerical samples of its exact transform powers show how convolution powers concentrate frequency mass while the physical support stays fixed.](figures/compact-kernels-and-transform-peaks.png)

*Figure 1.* The seed is the normalized function \(\exp[-1/(1-4x^2)]\) on \(|x|<1/2\), extended by zero. The right panel samples \(|F_\psi(w)|^k\), for \(k=4,16,64\), by quadrature. In the modulated construction this equals \(|F_{u_j}(c_j+k_jw)|\) when \(k=k_j\). Every peak has exact value one at \(w=0\); physical support remains inside the original small ball. These curves depict smooth test kernels, without an assertion that they are the final nonsmooth function. Proof locators: complete proof, (2.4)–(2.5) and Lemma 2.2. Background: Tao and Hörmander.

To express exterior decay, the proof uses

\[
 P_{N,m}(v)=
 \sup_{\substack{\xi\notin E,\ |\xi|\geq2\\
                 |\zeta-\xi|\leq m\log|\xi|}}
 (1+|\zeta|)^N|F_v(\zeta)|.
 \tag{S4}
\]

For every fixed \(N,m\), these seminorms of \(u_j\) tend to zero. The proof makes the complex estimate explicit. With \(w=(\zeta-c_j)/k_j\), exterior membership forces \(|w|>R_j/2\) eventually; the complex tube also gives
\(e^{|\operatorname{Im}w|}\leq[B_m(1+|w|)]^m\).
Whole-complex smooth decay of \(F_\psi\) therefore dominates both this imaginary growth and the polynomial weight. The resulting bound is

\[
 P_{N,m}(u_j)\leq
 [H_{N,m,\psi}(1+R_j/2)^{-2}]^{k_j}\longrightarrow0.
 \tag{S5}
\]

The constants may depend on \(N,m,\psi\), but not on \(j\) or the exterior frequency point.

## 3. Why a nonsmooth function must exist

Let \(\mathcal F\) be the space of continuous functions in the fixed support ball, smooth away from zero, with every seminorm (S4) finite. Its topology includes the uniform norm, all derivatives on compact annuli away from zero, and all exterior seminorms. Lemma 3.1 of the complete proof shows that this space is complete: uniform limits give continuity, local derivative limits give smoothness away from zero, and weighted transform limits preserve the exterior estimates.

Set

\[
 t_j=e^{\sqrt{\log Q_j}}.
 \tag{S6}
\]

This weight grows faster than every power of \(\log Q_j\), but slower than \(Q_j\). If the quantities \(t_jF_v(c_j)\) were bounded for every \(v\in\mathcal F\), Baire's theorem would bound all these evaluations by one finite seminorm \(p_l(v)\).

Choose the smooth kernels supported so close to zero that all their derivatives vanish on that seminorm's annulus. Their remaining seminorm is at most \(k_j^n\|\psi\|_\infty+o(1)\). Yet their evaluation has size \(t_j\), which grows faster than \(k_j^n\). This is impossible. Thus some \(v\in\mathcal F\) has unbounded \(t_j|F_v(c_j)|\).

Such a \(v\) cannot be \(C^1\): compact \(C^1\) functions have \(|F_v(c)|\leq C/|c|\), making the weighted evaluations tend to zero. Since \(v\) is smooth off zero, its singular support is exactly \(\{0\}\).

Choose centers where \(t_j|F_v(c_j)|\geq1\). There

\[
 -\frac1{\sqrt{\log Q_j}}
 \leq L_v(0,c_j)
 \leq\frac{\log\|v\|_1}{\log Q_j}.
 \tag{S7}
\]

Both endpoints tend to zero. This prevents collapsed extractions, but does not alone identify a whole profile. To finish, cut \(v\) into a continuous part supported arbitrarily close to zero and a smooth remainder. The first contributes at most \(\varepsilon|\operatorname{Im}z|+o(1)\); the second has arbitrary smooth decay. Every proper extracted profile is therefore at most zero. Ball averages recover its value zero at the origin from (S7), and the submean inequality forces it to be the constant-zero function. Compactness then gives local \(L^1\) convergence to zero along the selected centers.

![Exact growth ratios for the Baire evaluation weight and the selected-center lower bound illustrate how the test-kernel contradiction and zero-profile recovery fit together.](figures/evaluation-weights-and-zero-profiles.png)

*Figure 2.* With \(\ell=\log Q\) and \(k=\lfloor\ell\rfloor\), left: \(\log_{10}(e^{\sqrt\ell}/k^n)\), for \(n=1,2,3\). Middle: \(\log_{10}(e^{\sqrt\ell}/Q)\). Right: the exact lower-bound function \(-1/\sqrt\ell\) from (S7), approaching the reference value zero. The upper error in (S7) also tends to zero. The plots show these explicit comparison functions; no transform of the Baire-selected function is plotted. Proof locators: complete proof, (4.1)–(4.6). Background: Tao's Baire notes and Hörmander.

## 4. Four worked examples

### Example 1: a one-sided neighborhood union requires complex values

In dimension one take \(c_j=e^{j^2}\), \(R_j=j\), for \(j\geq2\). The neighborhoods have radii \(j^3\). Each lies in positive frequencies because \(e^{j^2}>j^3\): at \(j=2\), \(4>3\log2\), and the derivative of \(s^2-3\log s\) is positive for \(s\geq2\).

Theorem 4.1 constructs a continuous \(v\notin C^1\), singular only at zero, whose normalized transform collapses outside this union and has zero profile along selected positive centers. It cannot be real valued. A real compact function obeys
\(F_v(-c)=\overline{F_v(c)}\).
But all negative selected centers \(-c_j\) are outside \(E\). Their central normalized logarithms would both tend to \(-\infty\), by exterior collapse, and tend to zero, by conjugate symmetry and (S7). This contradiction explains the complex-valued convention.

### Example 2: the smooth test family on an explicit scale

For the same centers, \(k_j=j^2\), so
\[
 F_{u_j}(c_j+j^2w)=F_\psi(w)^{j^2},\qquad
 \|u_j\|_\infty\leq j^{2n}\|\psi\|_\infty,\qquad
 t_j=e^j.
 \tag{S8}
\]
For each exterior seminorm, (S5) becomes
\([H_{N,m,\psi}(1+j/2)^{-2}]^{j^2}\to0\).
Eventually its base is at most \(1/2\), so it is bounded by \(2^{-j^2}\). Meanwhile \(e^j/j^{2n}\to\infty\), since \(j-2n\log j\to\infty\).

The kernels are supported arbitrarily close to zero and individually smooth. Their Fourier value at the chosen center is one. These facts contradict an assumed common evaluation bound and force the existence of a different, nonsmooth function in the complete space. No claim that the displayed kernels themselves converge to that function is needed.

### Example 3: a differentiated point mass cannot smooth a compact singularity

Let \(u=D^2\delta_b\) on \(\mathbb R\). Then
\(F_u(\zeta)=(i\zeta)^2e^{-ib\zeta}\).
On each compact parameter set, factor
\(c+z\log|c|=c[1+z\log|c|/c]\).
The second term in the bracket tends uniformly to zero. Using
\(|\log|1+w||\leq2|w|\) for \(|w|\leq1/2\), one obtains
\[
 L_u(z,c)\longrightarrow2+b\operatorname{Im}z
 \quad\text{uniformly on parameter compact sets}.
 \tag{S9}
\]
Every escaping frequency sequence has this proper profile; none collapses. Theorem 1.1 consequently excludes a compact nonsmooth \(w\) with smooth \(u*w\).

This also follows from the nonzero-polynomial singular-hull theorem in Locating singularities through logarithmic Fourier strips, Theorem 5.1: \(u*w=D^2(\tau_bw)\), so a smooth output forces the translated compact factor, hence \(w\), to be smooth. Compact support and the nonzero derivative polynomial are both part of that theorem.

### Example 4: crossed singular factors and the stronger continuous replacement

Let \(f\) be a smooth compact probability density on \(\mathbb R\), and in dimension two put
\[
 p=\delta_0\otimes f,\qquad q=f\otimes\delta_0,\qquad
 p*q=f\otimes f.
 \tag{S10}
\]
Both factors are singular distributions: \(p\) is concentrated on a vertical segment and \(q\) on a horizontal segment. Their convolution is a smooth function, as the product identity or direct distribution pairing shows.

The transform of \(p\) is \(F_f(\zeta_2)\). Along centers \(c_j=(0,Q_j)\), the smooth estimate (2.3) applied to the second coordinate makes \(L_p\) collapse on every complex parameter compact set. Theorem 1.1 therefore supplies more than the displayed distributional factor \(q\): at any chosen point, inside any chosen small support ball, it gives a continuous \(w\notin C^1\), singular only at that point, for which \(p*w\) is smooth.

This conclusion does not assert that \(q\) is continuous or singular at only one point. It is a separate consequence of the full frequency-selective construction. The concrete pairing in (S10) and the existence of the stronger replacement illustrate the two different regularity requirements in Theorem 1.1.

## Exercises with complete solutions

The exercises total 100 points.

### Exercise 1: scaling, support and modulation (8 points)

Starting from a nonnegative smooth probability density supported in \(B_b(0)\), derive (S3), its value at the center, and the support and uniform-norm bounds.

*Solution.* Substitution \(y=kx\) gives
\(F_{\psi_k}(\zeta)=F_\psi(\zeta/k)\) and \(\|\psi_k\|_1=1\).
Convolution multiplies transforms, so \(F_{v_k}(\zeta)=F_\psi(\zeta/k)^k\).
Multiplication by \(e^{ic_j\cdot x}\) replaces \(\zeta\) by \(\zeta-c_j\), yielding (S3) and \(F_{u_j}(c_j)=F_\psi(0)^{k_j}=1\).
The sum of \(k\) vectors in \(B_{b/k}(0)\) has norm less than \(b\), proving the support assertion. Finally, each convolution with a probability density preserves the upper uniform norm; since \(\|\psi_k\|_\infty=k^n\|\psi\|_\infty\), the claimed bound follows. Modulation has modulus one on physical real space and changes neither support nor this norm.

### Exercise 2: an explicit complex-tube constant (8 points)

Take \(m=2\). Derive the bound \(2\log q\leq q/2+C_2\), and give constants controlling \(q\) and \(|\operatorname{Im}w|\) when \(w=(\zeta-c_j)/k_j\).

*Solution.* The function \(2\log q-q/2\) has derivative \(2/q-1/2\) and maximum at \(q=4\), with value \(2\log4-2\). Thus the larger constant \(C_2=2\log4+2\) works for all \(q>0\).
Set \(A_2=2(e+1+C_2)\) and \(B_2=eA_2\).
The triangle inequality gives
\(q\leq Q_j+k_j|w|+2\log q\).
Absorb \(q/2\), use \(Q_j<e^{k_j+1}\) and \(k_j\leq e^{k_j}\), and obtain
\(q\leq A_2e^{k_j}(1+|w|)\).
Then
\[
 |\operatorname{Im}w|\leq2\log q/k_j
 \leq2\log[B_2(1+|w|)].
 \tag{S11}
\]
The last step uses \(k_j\geq1\) and \(\log[A_2(1+|w|)]\geq0\). Exponentiation gives the polynomial bound needed to absorb imaginary growth.

### Exercise 3: a finite exclusion radius (8 points)

For \(m=1\), use the constants in (2.7) of the complete proof. Show that \(R_j=100\) forces \(|w|>50\) at an admissible exterior point.

*Solution.* Here \(C_1=\log2+1<2\), so
\(A_1=2(e+1+C_1)<12\), using \(e<3\), and \(B_1=eA_1<36\).
If \(|w|\leq50\), equation (2.10) would give
\[
 100\leq50+\log(B_1\cdot51)
 <50+\log1836
 <50+\log2048
 =50+11\log2<61.
 \tag{S12}
\]
This contradiction proves the claim. The calculation is a sufficient finite threshold; the general proof only needs such exclusions for all sufficiently large \(R_j\).

### Exercise 4: the smooth-decay order (10 points)

For \(N=3\), \(m=2\), and seed support radius at most one, choose a derivative order proving (S5). Explain why no specified speed of \(R_j\to\infty\) is required.

*Solution.* Choose \(L=N+m+2=7\) in (2.3). On the scaled tube,
\(e^{|\operatorname{Im}w|}\leq[B_2(1+|w|)]^2\).
Hence
\(|F_\psi(w)|\leq C_7B_2^2(1+|w|)^{-5}\).
Multiplication by the weight factor \((eD)^3(1+|w|)^3\) gives
\(H(1+|w|)^{-2}\), with \(H=(eD)^3C_7B_2^2\).
Exterior separation gives \(|w|>R_j/2\), so the weighted power is at most
\([H(1+R_j/2)^{-2}]^{k_j}\).
Since \(R_j\to\infty\), the base is eventually less than \(1/2\), regardless of the rate. The upper bound is then \(2^{-k_j}\to0\). The frequency norm and its logarithmic power can grow independently of the slow radius sequence.

### Exercise 5: preserving an exterior seminorm in a limit (10 points)

Suppose \(v_r\) converges uniformly on the fixed support ball and is Cauchy in \(P_{N,m}\). Prove that the limit has finite \(P_{N,m}\), and that \(P_{N,m}(v_r-v)\to0\). Why does pointwise transform convergence suffice here?

*Solution.* Uniform convergence gives, for each fixed complex \(\zeta\),
\[
 |F_{v_r-v}(\zeta)|
 \leq\operatorname{vol}(B_a)e^{a|\operatorname{Im}\zeta|}
                              \|v_r-v\|_\infty\to0.
 \tag{S13}
\]
For a given \(\varepsilon>0\), Cauchyness gives \(P_{N,m}(v_r-v_s)\leq\varepsilon\) for all \(r,s\geq r_0\).
At every admissible pair \((\xi,\zeta)\), let \(s\to\infty\) in its weighted inequality. The result is
\((1+|\zeta|)^N|F_{v_r-v}(\zeta)|\leq\varepsilon\) for all such pairs. Taking their supremum gives \(P_{N,m}(v_r-v)\leq\varepsilon\). Finally
\(P_{N,m}(v)\leq P_{N,m}(v-v_{r_0})+P_{N,m}(v_{r_0})<\infty\).
The uniform Cauchy bound applies on the entire unbounded tube before passage to the limit; pointwise convergence is used only to identify its limiting values. There is no unproved interchange of an arbitrary limit and supremum.

### Exercise 6: extracting one boundedness seminorm (8 points)

Suppose \(\sup_j|\Lambda_j(v)|<\infty\) for every \(v\in\mathcal F\). If Baire's theorem gives
\(v_0+\{v:p_l(v)<\varepsilon\}\subset\{v:\sup_j|\Lambda_j(v)|\leq s\}\),
derive a bound valid for every \(v\).

*Solution.* The center \(v_0\) belongs to the displayed closed boundedness set. For \(p_l(v)<\varepsilon\), subtracting its values from those at \(v_0+v\) gives
\(\sup_j|\Lambda_j(v)|\leq2s\).
For \(p_l(v)>0\), apply this to \(\varepsilon v/(2p_l(v))\) and use linearity. The resulting bound is
\(\sup_j|\Lambda_j(v)|\leq(4s/\varepsilon)p_l(v)\).
If \(p_l(v)=0\), its uniform-norm term forces \(v=0\), so the same bound holds. This finite-seminorm estimate is precisely what the smooth peaked kernels contradict.

### Exercise 7: the evaluation weight (10 points)

For \(Q_j=e^{j^2}\), compute the weight \(t_j\), its ratio to the test-kernel height, and its ratio to \(Q_j\). Explain why a fixed power of \(\log Q_j\) does not serve every dimension.

*Solution.* We have \(k_j=j^2\), \(t_j=e^j\),
\(t_j/k_j^n=e^j/j^{2n}\to\infty\), and
\(t_j/Q_j=e^{j-j^2}\to0\).
The logarithmic weight also satisfies \(\log t_j/\log Q_j=1/j\to0\). It therefore forces unbounded evaluations against the polynomial-height kernels, excludes \(C^1\) functions, and supplies the vanishing central lower error in (S7).
For a proposed weight \((\log Q_j)^r=j^{2r}\), its ratio to \(k_j^n\) is \(j^{2(r-n)}\). It fails to tend to infinity when \(n\geq r\). The exponential square-root weight dominates all fixed logarithmic powers, so the same choice works in every fixed dimension.

### Exercise 8: a zero local \(L^1\) limit with moving zeros (12 points)

On \(\mathbb C\) consider \(f_j(z)=j^{-1}\log|z-1/j|\). Prove local \(L^1\) convergence to zero and convergence \(f_j(0)\to0\), while uniform convergence on a compact neighborhood of zero fails.

*Solution.* Each \(f_j\) is a proper PSH function. At zero it equals \(-\log j/j\to0\).
On \(|z|\leq R\), translation \(w=z-1/j\) gives
\[
 \int_{|z|\leq R}|f_j(z)|\,dA(z)
 \leq\frac{2\pi}{j}\int_0^{R+1}r|\log r|\,dr.
 \tag{S14}
\]
The integral is finite: near zero, \(r|\log r|\) is integrable, and on every positive compact interval the integrand is continuous. This proves convergence in \(L^1\) on every fixed disk.
For any disk about zero, the point \(z=1/j\) is inside it for large \(j\), and \(f_j(1/j)=-\infty\). Uniform convergence to the finite function zero is impossible.
This is a PSH model illustrating the convergence distinction. It is not asserted to be the Fourier profile sequence of one fixed compact distribution. In the constructed Fourier sequence the full proof likewise claims local \(L^1\) convergence, without claiming uniform convergence to zero.

### Exercise 9: two isolated nonsmooth factors in one dimension (12 points)

Use the positive neighborhood union of Example 1. Show that there exist compact continuous functions \(v,w\), each not \(C^1\), singular respectively at zero and at any chosen \(x_0\), whose convolution is smooth. Their support balls may be prescribed arbitrarily small.

*Solution.* Theorem 4.1 gives \(v\) in the prescribed small ball about zero, singular exactly there and not \(C^1\). Negative frequencies \(-c_j\) lie outside \(E\) and escape. Therefore \(L_v(\cdot,-c_j)\) collapses uniformly locally, so condition 1 of Theorem 1.1 holds for \(v\).
Condition 2 then gives a continuous \(w\notin C^1\), singular exactly at the chosen \(x_0\), supported in its prescribed small ball, with \(v*w\) smooth. Both are compact functions, so their convolution is also compactly supported.
At least \(v\) must have complex values by Example 1. The construction supplies existence with complete regularity and frequency guarantees; it does not supply a closed formula for the Baire-selected functions. There is no contradiction with Example 3: these functions are not differentiated point masses with a fixed nonzero polynomial transform.

### Exercise 10: the converse needs the same sequence (14 points)

Suppose \(w\) is a compact nonsmooth distribution and \(u*w\) is smooth. Prove that \(u\) has a collapsed profile. Address the zero-factor case and explain why separately chosen profiles would not suffice.

*Solution.* If \(u=0\), its normalized logarithms are identically \(-\infty\), so the conclusion is immediate. Otherwise, the earlier singular-hull theorem ensures a proper profile of \(w\) along some escaping real sequence; if all profiles were collapsed, the convex singular hull would be empty and \(w\) would be smooth.
Keep that sequence and extract a proper or collapsed profile of \(u\) on a further subsequence. The already converging \(w\) profile is unchanged. If the \(u\) limit were proper, the two limits would be locally integrable and their sums would converge in local \(L^1\) to their proper PSH sum:
\[
 \|(L_u+L_w)-(V_u+V_w)\|_{L^1(B)}
 \leq\|L_u-V_u\|_{L^1(B)}+\|L_w-V_w\|_{L^1(B)}\to0.
 \tag{S15}
\]
The sum is finite almost everywhere and therefore proper. The exact Fourier product makes it a proper profile of \(u*w\), contradicting the uniform complex-parameter collapse of a smooth compact function. The \(u\) limit must be collapsed.
Profiles chosen separately need not coexist on any common frequency sequence. Their formal sum would then not describe the transform product along a sequence at all. The retained \(w\) sequence and the further extraction are what make the contradiction valid. The case \(w=0\) is excluded by its assumed nonsmoothness.

## References

- Terence Tao, [245B, Notes 9: The Baire category theorem and its Banach space consequences](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/), 2009.
- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), 2021. The Fourier normalization differs from this chapter.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Springer, 1983, Chapter XVI. The full frequency-selective construction and smoothing equivalence are proved in the complete proof above.
