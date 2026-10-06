# Comparing global parametrices through a compact middle

A global inverse can send a compact test to a smooth function with noncompact support. Composing three such kernels without a support argument can therefore lose an entire smooth term. We insert one compact middle cutoff, prove the exact wavefront bound for that composition, and then remove the cutoff on a prescribed compact set. This proves uniqueness of signed parametrices without requiring their kernels to be properly supported.

The nonzero-endpoint kernel maps and half-density conventions are proved in Kernels, adjoints and clean composition, Sections 1–3. The tensor wavefront inclusion and the full smooth-map pullback construction are proved in Sections 18.4–18.5 of Detecting regularity without choosing coordinates. We use those complete proofs for one explicit embedding and prove the required fiber integration here. The latter provider retains GFDL 1.2 without invariant sections or cover texts; the receiving arguments and exercises below are independently written. Compact return and the closed characteristic relation are proved in Global solvability through characteristic excursions and Global time and the bicharacteristic relation.

All orders may be real. Work with scalar half-density kernels on smooth manifolds without boundary. A finite bundle version follows componentwise with the same order of matrix multiplication. We use the reflected-input convention
\[
\operatorname{WF}'(A)=\{(x,\xi;y,\eta):(x,y;\xi,-\eta)\in\operatorname{WF}(K_A)\}.
\tag{CM1}
\]
The condition of having no zero endpoint means that both \(\xi\) and \(\eta\) are nonzero at every kernel wavefront point. It is a condition in the full punctured product cotangent space, including directions in which only one component would be nonzero.

## 1. Constructing the product with a compact middle cutoff

Let \(A_1\) have kernel on \(Y\times Z\), and \(A_2\) kernel on \(X\times Y\). Suppose both kernels have no zero endpoint. For \(\phi\in C_c^\infty(Y)\), there is a kernel
\[
K_{A_2\phi A_1}(x,z)=\int_Y K_{A_2}(x,y)\phi(y)K_{A_1}(y,z)\,dy.
\tag{CM2}
\]
The integral notation means the following actual distribution construction.

Form the tensor product \(K_{A_2}\otimes K_{A_1}\) on \(X\times Y\times Y\times Z\). Apply the proved pullback theorem to the embedding
\[
j(x,y,z)=(x,y,y,z).
\tag{CM3}
\]
In scalar coordinate frames its normal covectors have the form
\[
(x,y,y,z;0,\theta,-\theta,0),\qquad\theta\ne0.
\tag{CM4}
\]
The tensor wavefront inclusion cannot contain one of these covectors. A nonzero covector of the first factor with external component zero would be a forbidden endpoint of \(K_{A_2}\); the same holds for the second factor. If a factor contributes its zero covector over its support, its middle component is also zero. Both factors therefore have zero covectors, contrary to \(\theta\ne0\). Thus the precise pullback transversality condition holds.

Multiply this pullback by \(\phi(y)\) and push it forward under \(\pi(x,y,z)=(x,z)\). The pushforward exists: over a compact external test support the remaining variable belongs to the fixed compact \(\operatorname{supp}\phi\). In charts it is the pairing with a test independent of \(y\), multiplied by a compact cutoff equal to one on that middle support. The result is independent of this cutoff because its difference vanishes near the distribution's support. Every derivative of the external test remains an external derivative, and the compact finite-order distribution estimate proves continuity. Partitions of unity give the same definition on overlapping charts by the distributional change-of-variables formula.

The two half densities at the middle endpoint multiply to a density. Its fiber integral leaves the external half density. More explicitly one may choose a positive smooth density \(dy\) on each middle chart, divide the two kernel frames by their appropriate factors of \(|dy|^{1/2}\), apply the scalar construction, and restore the external frames. Changing that density cancels the two middle half-density factors against the integration density. Hence (CM2) defines the invariant kernel with the stated order of its factors.

This kernel agrees with operator composition on compact smooth inputs. The nonzero-endpoint theorem sends \(A_1 f\) into \(C^\infty(Y)\); multiplication by \(\phi\) puts it in \(C_c^\infty(Y)\), on which \(A_2\) acts. To check equality of kernels, first regularize the two compactly localized scalar kernels by Cartesian Gaussians. The pullback construction in the cited proof gives exactly the limit of their tensor product restricted by (CM3). For any external test, the normal directions have the rapid Fourier estimates just used, while the complementary directions have the nonstationary estimates of that construction. The Gaussian Fourier factors are bounded by one, so its integrable test bounds apply uniformly. Dominated convergence and the compact middle integration pass the smooth kernel pairing to its distributional limit. For a product external test the smooth pairing is the iterated operator pairing, and the nonzero-endpoint map is the same smooth-approximation extension. The kernel correspondence identifies the resulting kernels. No unrestricted three-factor associativity is used.

## 2. The exact matching wavefront bound

We first prove the fiber-integration assertion needed above. If a distribution \(h\) on \(X\times Y\times Z\) has support proper over \(X\times Z\), then
\[
\operatorname{WF}(\pi_*h)\subset
\{(x,z;\xi,\zeta):\text{some }y\text{ has }(x,y,z;\xi,0,\zeta)\in\operatorname{WF}(h)\}.
\tag{CM5}
\]
Only nonzero external pairs are included on the right. To prove it, localize the external variables near a fixed external base point. Properness gives one compact middle set for that localization. If an external direction is outside the displayed set, its joint direction with zero middle component is regular at every relevant middle point. A finite cover of this compact middle set and smaller regular base/cone neighborhoods gives one conic neighborhood of that joint direction on which each compactly localized piece of \(h\) has arbitrary Fourier decay. Cutoffs equal to one near each smaller piece retain these estimates by the proved cutoff theorem. Sum the finitely many pieces. In Euclidean coordinates the exact transform of the fiber integral is
\[
\widehat{\pi_*h}(\xi,\zeta)=\widehat h(\xi,0,\zeta).
\tag{CM6}
\]
Evaluating the rapid joint estimate at middle frequency zero proves rapid external decay. Smooth changes of coordinates use the exact covector transformation and integrated density. This proves (CM5).

The tensor inclusion, pullback bound and (CM5) now give
\[
\begin{aligned}
\operatorname{WF}'(A_2\phi A_1)\subset\{(x,\xi;z,\zeta):\ &\exists(y,\eta),\quad y\in\operatorname{supp}\phi,\\
& (x,\xi;y,\eta)\in\operatorname{WF}'(A_2),\\
& (y,\eta;z,\zeta)\in\operatorname{WF}'(A_1)\}.
\end{aligned}
\tag{CM7}
\]
Indeed the joint covector before fiber integration is \((\xi,\eta_2-\eta_1,-\zeta)\), where \(\eta_1\) is the input covector of \(A_2\) and \(\eta_2\) the output covector of \(A_1\). Its middle component is zero exactly when \(\eta_1=\eta_2\). Terms in the tensor inclusion in which just one factor contributes a singular covector would require that factor's middle covector to be zero, which is forbidden. Thus both factors must contribute actual wavefront covectors, and both external covectors are nonzero.

There is no omitted closure in (CM7). Over compact external base sets and the compact middle set, each kernel's closed unit wavefront slice excludes its zero endpoints. Compactness gives uniform comparability of its two endpoint lengths. For a matched pair this bounds \(|\eta|\) above and below by positive multiples of \(|(\xi,\zeta)|\). A sequence of matches whose external covectors converge to a nonzero pair therefore has a convergent subsequence of middle base points and covectors, and its limit is still a match. The same comparison rules out an external endpoint becoming zero. This proves local closedness and the nonzero-endpoint assertion for the composite.

One may replace the fixed compact middle support by a support set proper over the external variables: every preceding argument is local on a compact external set and then uses its compact middle preimage. In particular it applies to a properly supported pseudodifferential kernel acting on either side. A compactly supported middle kernel can also be inserted between the two kernels. Apply (CM7) twice; its two middle base variables range over the compact projections of that kernel's support.

If either outside kernel in (CM2) is smooth, the composite is smooth. In the tensor inclusion the smooth factor contributes only its zero covector; pushforward would force the singular factor's middle endpoint to be zero. There is consequently no nonzero external wavefront. This proves, in particular, smoothing of both \(A\phi R\) and \(R\phi A\) for any smooth kernel \(R\) and any no-zero-endpoint kernel \(A\). It uses compact middle support, rather than a proper-support assertion about \(A\) or \(R\).

## 3. A commutator cannot pass through the return cutoff

Let \(P\in\Psi^m(X)\) be properly supported with real homogeneous principal symbol. Assume **global real principal type** and compact return, with the full maximal-strip and all-interval quantifiers stated in the two preceding geometry lessons. Signed characteristic relations are unchanged by the positive degree-one normalization used there. Write
\[
\mathcal R_+=\Delta^*\cup C^+,\qquad\mathcal R_-=\Delta^*\cup C^-.
\tag{CM8}
\]
Here \(\Delta^*\) is the full nonzero cotangent diagonal, while \(C^\pm\) are the strict forward/backward characteristic relations. The unions in (CM8) are closed in the full punctured product cotangent space. A limit of strict signed characteristic pairs remains on the closed characteristic relation; the global time difference has the weak corresponding sign. If it is zero, the two characteristic points coincide and lie on \(\Delta^*\). If it is nonzero, the limit remains in the strict relation. The full characteristic relation and the full diagonal both exclude zero endpoints.

Fix a compact \(K\subset X\). Compact return supplies a compact \(K'\supset K\) containing the base projection of every characteristic interval with both endpoint base points in \(K\). Choose \(\phi\in C_c^\infty(X)\) equal to one on a neighborhood of \(K'\). Define
\[
B=[\phi,P]=\phi P-P\phi.
\tag{CM9}
\]
Its kernel has compact support. Proper support of \(P\) makes both the portion above the compact output support of \(\phi\) and the portion above its compact input support compact; their union contains the support of this difference. It also has
\[
\operatorname{WF}'(B)\subset
\{(v,\nu;v,\nu):v\in\operatorname{supp}d\phi,\ \nu\ne0\}.
\tag{CM10}
\]
For its actual kernel is \((\phi(v)-\phi(w))K_P(v,w)\). Away from the diagonal, the pseudodifferential kernel is smooth. In a neighborhood where \(d\phi\) vanishes, \(\phi\) is locally constant, and that coefficient vanishes on a product neighborhood of each diagonal point. This proves (CM10) without discarding any lower symbol term.

Let \(A_1,A_2\) have wavefront relations contained in the same \(\mathcal R_+\). By the preceding compact-kernel extension their product through \(B\) exists. If it had a wavefront point whose two endpoint base points are in \(K\), (CM7) applied twice and (CM10) would give a middle characteristic point \((v,\nu)\) with base outside the neighborhood where \(\phi=1\). If one of the outside matches is diagonal, this middle base point is an endpoint in \(K\subset K'\), already impossible. If both are strict, the same characteristic trajectory runs from the input endpoint to \((v,\nu)\) and then to the output endpoint. Uniqueness of the bicharacteristic flow places \(v\) on the actual intervening characteristic interval. Compact return puts it in \(K'\), again impossible. Consequently
\[
\operatorname{WF}(A_2[\phi,P]A_1)\text{ has no point over }K\times K.
\tag{CM11}
\]
The backward argument reverses both strict time inequalities and proves exactly the same statement for \(\mathcal R_-\). This is a smoothness assertion over the compact external set; the commutator kernel need not vanish there after composition.

![An exact flat trajectory shows why the middle commutator cannot carry an endpoint singularity.](figures/compact-middle-return-cutoff.svg)

The diagram uses the model \(p=\tau\), with one fixed characteristic trajectory \(z=0,\tau=0,\zeta\ne0\). Its compact endpoint set is \(K=[-1,1]\times\{0\}\), and \(K'=[-2,2]\times\{0\}\). A transverse cutoff is one near \(z=0\); the displayed time cutoff is \(\phi(t)=\theta(t+3)\theta(3-t)\), where \(\theta(u)=h(u)/(h(u)+h(1-u))\) and \(h(u)=e^{-1/u}\) for \(u>0\), zero otherwise. Thus \(\phi=1\) on \([-2,2]\) and \(\operatorname{supp}\phi'=[-3,-2]\cup[2,3]\). A forward match has \(s\le v\le t\); endpoints in \([-1,1]\) force \(v\) into the plateau. This is an exact single-trajectory example of (CM9)–(CM11), not a coordinate representation of every manifold trajectory.

## 4. Full uniqueness with one left and one right parametrix

Suppose
\[
\begin{aligned}
PE_1&=I+R_1,& E_2P&=I+R_2,\\
R_1,R_2&\text{ have smooth kernels},& \operatorname{WF}'(E_j)&\subset\mathcal R_+.
\end{aligned}
\tag{CM12}
\]
Then \(E_1-E_2\) has a smooth kernel on \(X\times X\). No proper support of either \(E_j\) is assumed.

**Proof.** Use the return cutoff just constructed for any compact \(K\). The two middle kernels \(\phi P\) and \(P\phi\) have compact support by properness. All their products with the \(E_j\) therefore exist. On a compact smooth input \(f\), the function \(E_1f\) is smooth. The expressions \(E_2\phi P(E_1f)\) and \(E_2P(\phi E_1f)\) act on compact smooth inputs at their last step. The actual operator identities in (CM12) hence give the kernel identities
\[
E_2\phi PE_1=E_2\phi+E_2\phi R_1,
\qquad
E_2P\phi E_1=\phi E_1+R_2\phi E_1.
\tag{CM13}
\]
The two error products are smooth by Section 2. Subtract the identities, retaining the commutator sign:
\[
E_2\phi-\phi E_1
=E_2[\phi,P]E_1-E_2\phi R_1+R_2\phi E_1.
\tag{CM14}
\]
The right side has no wavefront over \(K\times K\), by (CM11) and the smooth error products. On a neighborhood of this compact external set, \(\phi\) equals one at both endpoints, so the left kernel is exactly \(E_2-E_1\). Each point of \(X\times X\) lies in \(K\times K\) for some compact \(K\): take relatively compact neighborhoods of its two base points and their compact closures. This proves smoothness everywhere. The same proof with \(\mathcal R_-\) proves backward uniqueness. ∎

Thus any right parametrix with the specified sign agrees modulo a smooth kernel with any left parametrix with that sign. Once both sides exist, this also compares two right parametrices by a common left one, and two left parametrices by a common right one. The argument does not infer existence of an opposite-sided parametrix from a single given one.

## 5. How adjoints supply the missing side

Suppose right parametrices with both signs have been constructed for every operator in the class, including \(P^*\). The adjoint has the same real principal symbol as \(P\). If \(F_-\) is the backward right parametrix for \(P^*\), then
\[
P^*F_-=I+S_-,\qquad L_+=F_-^*,\qquad L_+P=I+S_-^*,
\qquad \operatorname{WF}'(L_+)\subset\mathcal R_+.
\tag{CM15}
\]
The last inclusion follows from the complete kernel adjoint theorem: it interchanges the relation's endpoints, and the inverse of the backward relation is the forward relation. Its diagonal remains the same. Both \(L_+\) and its residual are actual kernels, and \(S_-^*\) is smooth. Apply Section 4 to the forward right parametrix \(E_+\) and this forward left parametrix. Their difference \(D_+=E_+-L_+\) is smooth. Proper support of \(P\) permits its action on either variable of a smooth kernel and preserves smoothness locally; every compact output set involves a compact integration set and every differentiated kernel pairing remains a smooth parameter family. Therefore
\[
E_+P-I=(L_+P-I)+D_+P\in C^\infty(X\times X).
\tag{CM16}
\]
Its right identity was already constructed. It is now two-sided. The forward right parametrix for \(P^*\) similarly supplies the backward left parametrix for \(P\). This proves both-sidedness and uniqueness conditional on the two signed right constructions. It does not supply their local diagonal construction, Sobolev gain or elliptic difference.

## 6. Exercises with complete solutions

**1. A smooth term exposes the associativity gap (intermediate).** On the line put \(P=D_t=-i\partial_t\), \(E_1(t,s)=iH(t-s)\), and \(E_2(t,s)=iH(t-s)+1\). Prove that both are exact two-sided inverses on compact tests. Explain the two formally grouped kernels \((E_2P)E_1\) and \(E_2(PE_1)\). For any \(\phi\in C_c^\infty(\mathbb R)\), compute \(E_2[\phi,P]E_1\) exactly.

**Solution.** Differentiation of \(iH(t-s)\) by \(-i\partial_t\) gives \(\delta(t-s)\); integration by parts in \(s\) gives the same right action on a compact test. The constant kernel has zero derivative in either variable and kills the integral of the derivative of a compact test. Thus both two-sided identities hold, although their difference is the nonzero smooth kernel \(1\). Each pair \(E_2P\) and \(PE_1\) equals the identity kernel. Composing these collapsed pairs with the remaining kernel yields respectively \(E_1\) and \(E_2\). They differ. The uncut three-factor kernel cannot be freely associated: \(E_1f\) is generally noncompact, outside the original test domain of \(E_2P\). Extending that already-collapsed identity to smooth functions supplies a different grouping, without establishing a common triple product.

Here \([\phi,D_t]=i\phi'\). Its compact middle support makes the actual triple integral legitimate. The two contributions are
\[
-iH(t-s)\int_s^t\phi'(v)\,dv
-\int_s^\infty\phi'(v)\,dv
=iH(t-s)(\phi(s)-\phi(t))+\phi(s).
\tag{CM17}
\]
For \(t<s\) the first term is zero; for \(t=s\) its continuous primitive is zero, so the formula is independent of the value assigned to \(H(0)\). This is exactly \(E_2\phi-\phi E_1\). When \(\phi=1\) near the two endpoints, the result equals \(1\), which is smooth but nonzero. Thus the proof correctly establishes equality modulo a smooth kernel, rather than equality of the two global inverses.

**2. Compact support does not repair a forbidden endpoint (advanced).** Let \(Y=\mathbb R\), and in scalar frames take \(K_2(x,y)=1_x\otimes\delta_0(y)\) and \(K_1(y,z)=\delta_0(y)\otimes1_z\). For a middle cutoff equal to one near zero, identify the failed transversality condition and compute the Gaussian regularization's divergence.

**Solution.** The first kernel has wavefront \((x,0;0,\eta)\), \(\eta\ne0\), and the second \((0,\theta;z,0)\), \(\theta\ne0\). The tensor inclusion contains the normal (CM4) by taking \(\theta=-\eta\). Thus (CM3) has a forbidden normal covector; its restriction would require \(\delta_0^2\). With \(g_\epsilon(y)=(4\pi\epsilon)^{-1/2}e^{-y^2/(4\epsilon)}\), the middle integral is
\[
\int\phi(y)g_\epsilon(y)^2\,dy
=(8\pi\epsilon)^{-1/2}+O(\epsilon^{-1}e^{-c/\epsilon})
\quad(\epsilon\downarrow0)
\tag{CM18}
\]
for some \(c>0\), since \(\phi=1\) on a fixed interval about zero and its complement has positive distance from zero. Pairing with an external product test whose two integrals have product one gives this same divergent value. There is no distributional limit of these regularized kernels. A compact middle cutoff supplies integration support; it does not supply the missing wavefront transversality.

**3. The adjoint must reverse the chosen sign (introductory).** For the flat degree-one operator \(D_t\) on \(\mathbb R_t\times\mathbb R^{n-1}_z\), \(n\ge2\), use the two signed kernels \(E_\pm\) of the directional-symbol lesson. Determine which right inverse for \(P^*\) supplies a forward left inverse for \(P\), and explain why using the other one cannot establish forward uniqueness.

**Solution.** Here \(P^*=P\), \(E_+=iH(t-s)\delta(z-w)\), and \(E_-=-iH(s-t)\delta(z-w)\). Complex conjugation followed by endpoint interchange gives \(E_-^*=E_+\) and \(E_+^*=E_-\). Thus the backward right inverse supplies the forward left inverse. The other choice has relation \(\Delta^*\cup C^-\), outside the common forward-sign hypothesis of Section 4. Moreover \(E_+-E_-=i\delta(z-w)\) has every nonzero transverse conormal along all time pairs. It is elliptic of order \(-1/2\) on the complete characteristic relation, by the exact normalization already proved in that lesson; for \(n\ge2\) it is not smooth. No same-sign uniqueness statement can compare these opposite choices modulo a smooth kernel. After the correct choice, (CM14) gives a smooth difference and (CM16) gives the missing identity.

## 7. The remaining global construction

The compact-middle comparison, same-sign uniqueness and conditional adjoint conversion are now proved. The signed right parametrices must still be constructed near the diagonal and assembled with their exact residual orders; the complete directional correction supplies the subsequent kernel correction. The full theorem also requires the exact every-real Sobolev gain, global nonvanishing of the difference symbol, positive elliptic reduction for arbitrary real operator order and the stated sign choices on disconnected characteristic components. These remain substantive steps of the owned propagation programme.

## References and scope

Hörmander IV, Theorem 26.1.14, printed 70–71/PDF 81–82, supplies the antecedent for the compact-middle uniqueness comparison and adjoint reduction. The tensor and pullback proofs are the exact written programme providers cited above. The fiber-integration estimate, explicit compact-support justification, complete relation matching and solved examples here are independently written. This lesson proves the stated comparison and conditional conversion; it makes no full global-parametrix completion or novelty claim.
