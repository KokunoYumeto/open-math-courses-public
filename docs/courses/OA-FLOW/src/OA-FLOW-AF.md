# Inputs for action frequencies and norm continuity

*Proof restoration and local completion, Codex (OpenAI), 5 October 2026. New expression is dedicated under CC0 to the extent of rights held. Human review is not asserted.*

The earlier inputs are BS0–5, LF0–7, scalar singleton synthesis, [CF1/2/4](OA-FLOW-CF.md#oa-flow.cf.1), [SC0–8](OA-FLOW-SC.md#sc-00), [HR3 finite densities](OA-FLOW-HR.md#hr-03), [L24 translations and vector integration](OA-FLOW-L24.md#oa-flow.grp.vectorintegration), [CC0 circle Fourier completeness](OA-FLOW-CC.md#cc-0), and [RF1 smooth bumps](OA-FLOW-RF.md#oa-flow.rf.1). The individual passages actually used are bound separately. None of the arguments below uses a general spectral-transfer theorem.

<a id="af-0"></a>

## AF0. The positive frequency convention and both Banach settings

Let \(G\) be an arbitrary LCH abelian group, \(H=\widehat G\), with the Haar convention of L24. Write \((t,p)=p(t)\). Use either BS's ordinary Banach setting **(B)** (norm-continuous orbits) or its specified dual setting **(D)** (\(X=Y^*\), normal operators and norm-continuous predual orbits). In both, \(C_\alpha=\sup_t\|\alpha_t\|<\infty\). Put \(\tau=\|\cdot\|\) in \(B\) and \(\tau=\sigma(X,Y)\) in \(D\).

The preserved lessons use the positive transform and filters

<a id="equation-af1"></a>

\[
 f(p)=\mathcal F_+a(p)=\int_G a(t)(t,p)\,dt,
 \qquad \alpha_f=T_a^\alpha,
 \qquad \|f\|_A=\|a\|_1.
 \tag{AF1}
\]
For the negative transform of BS/LF, \(Jf(\gamma)=f(-\gamma)\) is exactly \(\mathcal F_-a(\gamma)\). Reflection \(p\mapsto-p\) is a homeomorphism of the dual group, and \(J\) is an isometric algebra identification. Thus the positive action and vector spectra are the reflections of BS's spectra, and all ideal, localization and essentiality results transport with their exact closed supports and topologies. In particular,

<a id="equation-af2"></a>

\[
 \alpha_f\alpha_g=\alpha_{fg},\qquad
 \alpha_t\alpha_f=\alpha_{m_tf},\quad m_tf(p)=(t,p)f(p),\qquad
 \|\alpha_f\|\leq C_\alpha\|f\|_A.
 \tag{AF2}
\]
Here \(m_tf=\mathcal F_+(L_ta)\), \(L_ta(u)=a(u-t)\); L24 proves norm continuity of \(t\mapsto L_ta\). For any \(E\subset H\), write \(X_\alpha(E)=\{x:\operatorname{Sp}_\alpha(x)\subset E\}\). For open \(U\), this is distinct from BS4's closed filtered-span space \(X_\alpha^0(U)\); only its inclusion into \(X_\alpha(\overline U)\) is used below. A compactly supported filter in \(U\) has its range in \(X_\alpha(U)\) by BS3. A filter equal to one near a vector spectrum fixes that vector (BS3). A filter vanishing near that spectrum annihilates it. Compact-frequency filtered vectors have bounded \(\tau\)-dense cores (BS2–3). If the action spectrum is empty, essentiality and LF6 imply \(X=0\).

The sequence-space examples have the stated full dual. A bounded functional on \(\ell^1(\mathbb N)\) has coordinates \(y_n=\ell(e_n)\) with \(\sup_n|y_n|\leq\|\ell\|\); finite-support density and the absolutely convergent sum give \(\ell(a)=\sum_n a_n y_n\). Conversely every bounded coordinate sequence defines this functional, with norm \(\sup_n|y_n|\). SC7 proves completeness. A diagonal unit-modulus action with frequencies \(r_n\) is normal on \(\ell^\infty\): its preadjoint multiplies \(\ell^1\) by the same phases. Splitting the \(\ell^1\) sum into a finite part and its arbitrarily small tail proves norm continuity of every predual orbit, for arbitrary \(r_n\).

The dual of discrete \(\mathbb Z\) is \(\mathbb T\), with \((n,z)=z^n\): a character is determined by its value \(z\) at one, and these formulas give every character. Compact subsets of \(\mathbb Z\) are finite, so convergence at one is exactly compact-open convergence. In the real examples, the identification of all characters with \(t\mapsto e^{itq}\) is proved in AF4 below.

<a id="af-1"></a>

## AF1. Finite complex measures and the complete measure-filter domain

A finite complex regular Borel measure \(\mu\) means a countably additive complex measure whose total variation

<a id="equation-af3"></a>

\[
 \rho(E)=|\mu|(E)=\sup\left\{\sum_{j=1}^m|\mu(E_j)|:
                 (E_j)\text{ a finite Borel partition of }E\right\}
 \tag{AF3}
\]
is finite on \(G\) and Radon regular. Write \(\|\mu\|=\rho(G)\). The variation is a positive measure: on a disjoint union \(E=\bigcup_nE_n\), partitions of finitely many \(E_n\) give \(\rho(E)\geq\sum_n\rho(E_n)\). Conversely, for a finite partition \(A_j\) of \(E\), countable additivity and the triangle inequality give

<a id="equation-af4"></a>

\[
 \sum_j|\mu(A_j)|\leq\sum_n\sum_j|\mu(A_j\cap E_n)|
                 \leq\sum_n\rho(E_n).
 \tag{AF4}
\]
Taking the supremum proves equality. Also \(|\mu(E)|\leq\rho(E)\), and every \(\rho\)-null Borel set and all its Borel subsets are \(\mu\)-null. Passing to the completion defines \(\mu\) on completed sets independently of their Borel representatives.

For a simple \(E\)-valued function \(F=\sum_j1_{A_j}v_j\), \(E\) any Banach space, define \(\int F\,d\mu=\sum_j\mu(A_j)v_j\). Refinement proves independence, linearity, bounded-map compatibility and

<a id="equation-af5"></a>

\[
 \left\|\int F\,d\mu\right\|\leq\int\|F\|\,d\rho.
 \tag{AF5}
\]
Finite simple functions are dense among strongly measurable functions with finite norm integral. Here is the required construction on this finite measure space: truncate the norm, use a countable \(1/n\)-net in the separable essential range to partition by the first suitable point, then retain a finite part of that countable partition whose omitted measure is small. The bounded range error and omitted measure bound give \(L^1(\rho,E)\) approximation. The summable-difference argument of L24 Proposition4.1, now with the finite measure \(\rho\), proves completeness: SC4 makes the sum of pointwise norm differences finite a.e.; Banach completeness supplies the pointwise limit outside one common null set. All the ranges lie in one separable closed span; distances from a countable dense set are measurable pointwise limits, so the same finite-partition construction proves strong measurability of the limit. SC5 bounds its \(L^1\) tails. Thus (AF5) extends to every such \(F\), independently of approximants. Bounded linear maps still pass through the integral by the same bound.

Every bounded norm-continuous \(F:G\to E\) is eligible. Regularity gives increasing compact \(K_n\) with \(\rho(G\setminus K_n)<2^{-n}\). Their union is a full-measure sigma compact carrier. Each compact image \(F(K_n)\) has finite \(1/k\)-nets, hence is separable; their union lies in one separable closed span. Its continuous norm distances are Borel, so the preceding approximation proves strong measurability on the carrier. This argument does not require \(G\) or \(E\) to be separable.

Define

<a id="equation-af6"></a>

\[
 \widehat\mu(p)=\int_G\overline{(t,p)}\,d\mu(t),\qquad
 \alpha_\mu x=\int_G\alpha_{-t}x\,d\mu(t).
 \tag{AF6}
\]
In \(B\) this is the norm integral on every \(x\). In \(D\), integrate the norm-continuous orbit \(t\mapsto a_{-t}y\) on the actual predual \(Y\), obtaining \(B_\mu y\), and define \(\alpha_\mu=B_\mu^*\). Bounded-map compatibility yields the scalar weak-star integral in (AF6). In either setting,

<a id="equation-af7"></a>

\[
 \|\alpha_\mu\|\leq C_\alpha\|\mu\|,
 \qquad \alpha_\mu\text{ is normal in (D)}.
 \tag{AF7}
\]
For \(a\in L^1(G)\), choose L24 Lemma 2.2’s Borel representative vanishing outside a sigma compact carrier. Then \(d\mu(t)=a(-t)\,dt\), using the outer regular Haar measure, is a finite regular measure. Its integral is the same finite-exponent integral as in the locally determined convention. Two such representatives differ on a globally null set: their difference has a sigma compact carrier and is compact-locally null, so L24 Lemma 2.2 gives global nullity. Thus the finite measure and all its filters are independent of this representative choice. Indeed its variation is \(\int_E|a(-t)|\,dt\): the upper bound follows from the integral inequality; finite partitions according to a finite net of unit phases give the reverse bound arbitrarily closely, by making \(\operatorname{Re}(\zeta_j a)\geq(1-\epsilon)|a|\) on each partition set. HR3 proves that this finite density is Radon. Haar inversion preserves measure because \(G\) is abelian (L24). Hence \(\widehat\mu=\mathcal F_+a\) and \(\alpha_\mu=\alpha_f\), with the signs in (AF1)/(AF6).

The full measure-module law can be proved without a complex product-measure assumption. For \(f=\mathcal F_+a\), define in the Banach space \(L^1(G)\)

<a id="equation-af8"></a>

\[
 b=\int_G L_{-t}a\,d\mu(t),\quad
 \|b\|_1\leq\|\mu\|\|a\|_1,
 \qquad \mathcal F_+b=\widehat\mu f.
 \tag{AF8}
\]
Translation is norm continuous by L24, so the preceding vector integral applies. Fourier evaluation is a bounded linear functional on \(L^1\); moving it through the integral gives the last identity, since \(\mathcal F_+(L_{-t}a)(p)=\overline{(t,p)}f(p)\). The bounded linear integration map \(a\mapsto T_a^\alpha\) also passes through this norm integral in \(\mathcal B(X)\). Its integrand \(T_{L_{-t}a}^\alpha=\alpha_{-t}\alpha_f\) is operator-norm continuous. Pairing with every bounded functional in \(B\), or every actual predual vector in \(D\), identifies its integral with \(\alpha_\mu\alpha_f\). Consequently

<a id="equation-af9"></a>

\[
 \alpha_\mu\alpha_f=\alpha_{\widehat\mu f},\qquad
 \widehat\mu f\in A(H),\quad
 \|\widehat\mu f\|_A\leq\|\mu\|\|f\|_A.
 \tag{AF9}
\]
It follows that if \(\widehat\mu=1\) on an open neighbourhood of the action spectrum, then \(\alpha_\mu=I\). For \(f\in A_c(H)\), \((\widehat\mu-1)f\) has compact support missing the spectrum; LF6–7 put it in the annihilator ideal. Equation (AF9) makes \(\alpha_\mu\alpha_f=\alpha_f\). LF5 density extends this to every \(f\), and BS2 essentiality, with bounded normal maps in \(D\) or bounded maps and norm density in \(B\), proves the identity on all \(X\).

Dirac translations require no general measure convolution theorem. For \((\delta_r*\mu)(E)=\mu(E-r)\), homeomorphic translation transports regularity and gives

<a id="equation-af10"></a>

\[
 \alpha_{\delta_r*\mu}=\alpha_{-r}\alpha_\mu,\qquad
 \widehat{\delta_r*\mu}(p)=\overline{(r,p)}\widehat\mu(p).
 \tag{AF10}
\]
Finite linear combinations obey the same rule. A series \(\sum_jc_j\delta_{r_j}\) with \(\sum_j|c_j|<\infty\) defines a finite regular complex measure and the corresponding norm-convergent operator series. To verify regularity, its variation is dominated by the finite positive measure \(\sum_j|c_j|\delta_{r_j}\). Finite partial sums are Radon and have uniformly small complementary mass; their compact/open approximants prove Radon regularity of the sum. Domination transfers those same approximants to the variation. Repeated locations \(r_j\) cause no difficulty.

<a id="af-2"></a>

## AF2. All convolution characters, including the nonunital case

The following is the valid translation argument already written at (S3d) of the preserved module lesson, now with complete current inputs. First, an algebraic nonzero character \(\ell\) (a complex linear multiplicative functional) of any complex Banach algebra is automatically bounded with \(|\ell(b)|\leq\|b\|\). In the forced algebraic unitization with norm \(|z|+\|b\|\), extend it by \(\widetilde\ell(z,b)=z+\ell(b)\). If \(|\ell(b)|>\|b\|\), the Neumann inverse of \(1-b/\ell(b)\) would have character value zero, impossible for an invertible element. No continuity of the character was assumed in this argument.

Let \(\ell\ne0\) be a multiplicative functional on \(L^1(G)\), and choose \(a\) with \(\ell(a)\ne0\). Set \(c(t)=\ell(L_ta)/\ell(a)\). Since \((L_ta)*b=a*(L_tb)\), applying \(\ell\) proves \(\ell(L_tb)=c(t)\ell(b)\) for every \(b\). This also proves independence of \(a\). Translation continuity gives continuity of \(c\), and the group law gives \(c(s+t)=c(s)c(t)\), \(c(0)=1\). Its absolute value is uniformly bounded by \(\|\ell\|\|a\|_1/|\ell(a)|\). Positive and negative integer powers therefore force \(|c(t)|=1\). Thus \(c\in H\).

For \(b\in L^1(G)\),

<a id="equation-af11"></a>

\[
 b*a=\int_G b(t)L_ta\,dt\quad\text{in }L^1(G),\qquad
 \ell(b)=\int_G b(t)c(t)\,dt.
 \tag{AF11}
\]
The norm integral exists on the sigma compact carrier of \(b\). Its equality with convolution follows first for \(a,b\in C_c(G)\), by L24's qualified Fubini, then for all \(a,b\) by the \(L^1\) convolution bound and norm approximation. Moving \(\ell\) through the integral and cancelling \(\ell(a)\) proves the second formula. Conversely every \(c\in H\) gives this bounded multiplicative functional by L24 convolution; it is nonzero since shrinking nonnegative mass-one bumps have integrals against \(c\) tending to one. Uniqueness follows from the translation formula defining \(c(t)\).

Therefore every nonzero character of \(A(H)\) is evaluation at exactly one point. The forced unitization has, in addition, exactly the scalar quotient character: a character restricting nontrivially to \(A(H)\) is \(z+f(p)\), and one restricting to zero is \(z\). This statement does not adjoin a point to the character space of a nonunital filter algebra.

<a id="af-3"></a>

## AF3. The circle series and the reciprocal used for one operator

Use normalized circle measure \(d\theta/(2\pi)\), as CC0 with period \(P=2\pi\). If \(F(e^{i\theta})\) is twice continuously differentiable and periodic, put

<a id="equation-af12"></a>

\[
 a_n=\frac1{2\pi}\int_0^{2\pi}F(e^{i\theta})e^{-in\theta}\,d\theta.
 \tag{AF12}
\]
Two integrations by parts, with periodic endpoint values, give \(|a_n|\leq(2\pi n^2)^{-1}\int|\partial_\theta^2F|\) for \(n\ne0\). The sum over positive indices \(n\geq2\) converges by comparison on \([n-1,n]\) with \(u^{-2}\) and SC8. Reindexing the negative tail by \(m=-n\) gives the identical convergent sum, and only the two remaining nonzero indices \(n=\pm1\) need to be added. Thus \(\sum_n|a_n|<\infty\), and \(H(e^{i\theta})=\sum_na_ne^{in\theta}\) converges uniformly to a continuous function. Termwise integration is legitimate by the uniform norm bound and SC8; it gives the same coefficients for \(H\) as for \(F\). CC0's complete Fourier basis on normalized \(L^2(\mathbb R/2\pi\mathbb Z)\) makes \(F-H=0\) a.e. A nonzero continuous value would stay bounded away from zero on an arc of positive measure, contradicting that equality. Hence \(F=H\) everywhere. This proves the full series reconstruction, not just coefficient decay.

For a compact \(K\subset\mathbb T\setminus\{\lambda\}\), choose a small arc around \(\lambda\) disjoint from \(K\). RF1 supplies a nonnegative smooth mass-one bump \(b\) in a smaller real interval. The function \(c(\theta)=\int_{-2r}^{2r}b(\theta-u)\,du\), with \(\operatorname{supp}b\subset[-r,r]\), is smooth, equals one for \(|\theta|\leq r\), takes values in \([0,1]\), and is zero for \(|\theta|\geq3r\). Differentiation follows from uniform difference quotients on the compact integration interval; all derivatives of \(b\) are continuous there. Translate to an argument of \(\lambda\), choose \(r\) small enough, and periodize. The resulting smooth circle cutoff equals one near \(\lambda\) and zero near \(K\). Thus

<a id="equation-af13"></a>

\[
 F(z)=\frac{1-c(z)}{z-\lambda}\quad(z\ne\lambda),\qquad
 F=0\text{ near }\lambda
 \tag{AF13}
\]
is a smooth periodic reciprocal, agreeing with \((z-\lambda)^{-1}\) on a neighbourhood of \(K\). Its absolutely convergent Fourier expansion is furnished by (AF12).

The irrational-rotation statement used in the example is also elementary. For irrational \(\theta\), two of \(0,\theta,\ldots,N\theta\) modulo one lie in the same one of \(N\) intervals, giving \(q>0\) and a nonzero signed distance \(q\theta-k\) to an integer of absolute value less than \(1/N\). Positive multiples of this rotation make a grid around the circle with gap at most that distance (in either orientation). Choosing at most its reciprocal plus one multiples places one within that distance of any prescribed point. Letting \(N\to\infty\) proves that the positive powers of \(e^{2\pi i\theta}\) are dense in \(\mathbb T\).

<a id="af-4"></a>

## AF4. Logarithm identities and exponential spectral mapping

Absolute Banach-algebra series and their products are proved in CF1. In any unital Banach algebra define \(L(b)=\sum_{n\geq1}(-1)^{n+1}b^n/n\) for \(\|b\|<1\). On \(0\leq s\leq1\) the series for \(L(sb)\) and its derivative converge uniformly, and

<a id="equation-af14"></a>

\[
 \frac{d}{ds}L(sb)=b(1+sb)^{-1}.
 \tag{AF14}
\]
Every element here is a series in \(b\), so they commute. Differentiating \(e^{L(sb)}(1+sb)^{-1}\), using the uniformly differentiable exponential series and the derivative of the inverse from its product identity, gives zero. Its initial value is one, so CF1's fundamental theorem proves \(e^{L(b)}=1+b\).

The Neumann inverse used here and in L93 needs no normalization of the identity: if \(\|v\|<1\), the series \(1+\sum_{n\geq1}v^n\) converges by its geometric norm tail. Multiplying its finite partial sums on either side by \(1-v\) gives \(1-v^{N+1}\), which tends to the identity. Thus it is a two-sided inverse in the original norm even when \(\|1\|\ne1\).

For \(\|z\|<1/4\), \(\|e^{sz}-1\|\leq e^{\|z\|}-1<1\) on \([0,1]\). For example \(e^{1/4}\leq\sum_{n\geq0}4^{-n}=4/3<2\). The logarithm derivative series at \(b(s)=e^{sz}-1\) is uniformly convergent and commutes with \(b'(s)\); its derivative is \((1+b(s))^{-1}b'(s)=z\). It starts at zero. Hence

<a id="equation-af15"></a>

\[
 L(e^z-1)=z\quad(\|z\|<1/4).
 \tag{AF15}
\]
The scalar derivative in (AF14) also proves \(\sum_{n\geq1}r^n/n=-\log(1-r)\), by integrating \(1/(1-r)\) from zero. In particular \(-\log(9/10)\leq1/9<1/8\). These are the exact branch and norm bounds used in the preserved logarithm construction.

For a continuous character \(c:\mathbb R\to\mathbb T\), choose a neighbourhood on which \(|c(t)-1|<1/10\). The preceding two identities make \(l(t)=L(c(t)-1)\) locally continuous and additive whenever \(s,t,s+t\) lie in that neighbourhood: its two candidate values have norm less than \(1/4\), and applying (AF15) to their equal exponentials proves equality. Fix a small \(u>0\). Repeated local addition proves \(l(qu)=q l(u)\) for rational \(q\) with \(|qu|\) in the interval; every intermediate partial sum remains there. Rational density and continuity give \(l(t)=kt\) locally. For arbitrary \(t\), use \(c(t)=c(t/n)^n\) to obtain \(c(t)=e^{kt}\). Its unit modulus forces \(\operatorname{Re}k=0\). Thus \(c(t)=e^{itq}\) for a unique real \(q\), the uniqueness following from its derivative at zero.

This identification \(\mathbb R\to\widehat{\mathbb R}\) is a homeomorphism. If \(q_i\to q\), the estimate \(|e^{itq_i}-e^{itq}|\leq |t|\,|q_i-q|\), obtained by integrating its derivative, gives uniform convergence on each compact time set. Conversely put \(r_i=q_i-q\). For \(0<\epsilon<\pi\), if \(|r_i|\geq\pi\), take \(t=\pi/|r_i|\in[0,1]\) to obtain an error of two. If \(\epsilon\leq|r_i|<\pi\), take \(t=1\); the error is at least \(2\sin(\epsilon/2)>0\). Compact-uniform convergence on \([0,1]\) therefore forces \(|r_i|<\epsilon\) eventually, for every such \(\epsilon\). This is a net argument and proves the exact dual topology used in the real examples.

Finally, for every element \(h\) of a complex unital Banach algebra and real \(t\),

<a id="equation-af16"></a>

\[
 \sigma(e^{th})=\{e^{t\lambda}:\lambda\in\sigma(h)\}.
 \tag{AF16}
\]
The zero algebra is immediate. If its identity norm is not one, replace the norm by the equivalent complete norm \(\|a\|'=\|L_a\|_{\mathcal B(A)}\): \(\|a\|'\leq\|a\|\leq\|1\|\|a\|'\). It is submultiplicative, its identity has norm one, and algebraic spectra and norm convergence are unchanged. CF2/4 now apply exactly.

For \(\lambda\in\sigma(h)\), the absolutely convergent series factorization

<a id="equation-af17"></a>

\[
 e^{th}-e^{t\lambda}1=(h-\lambda1)
 \sum_{n\geq1}\frac{t^n}{n!}\sum_{j=0}^{n-1}h^{n-1-j}\lambda^j
 \tag{AF17}
\]
has commuting factors. Its norm convergence follows by bounding the inner sum by \(nM^{n-1}\), \(M=\max(\|h\|',|\lambda|)\), with the zero case interpreted directly. If the product were invertible, each commuting factor would be invertible by CF2, a contradiction. This proves one inclusion.

For the other inclusion let \(C\subset A\) be the closed unital algebra generated by \(h\) and every \((h-z1)^{-1}\) for \(z\notin\sigma_A(h)\). These generators commute: an inverse of a commuting invertible element still commutes, by multiplying the commutation identity by its inverse. Thus \(C\) is a commutative Banach algebra. Every character \(\chi\) of \(C\) has \(\chi(h)\in\sigma_A(h)\), since otherwise the included inverse of \(h-\chi(h)1\) would have zero character value. Continuity and the exponential series give \(\chi(e^{th})=e^{t\chi(h)}\). If \(w\) lies outside the displayed right side of (AF16), every character is nonzero on \(e^{th}-w1\). CF4's proved maximal-ideal characterization therefore makes this element invertible in \(C\), hence in \(A\). This proves the reverse inclusion without importing holomorphic functional calculus or an external spectral-mapping theorem.

These are bounded prerequisites for the restored lessons. They do not prove the separate general operator spectral-transfer theorem, arbitrary closed-set synthesis, or the remaining Connes-spectrum/cohomology programme.

The mathematical comparison for the restored results is M. Takesaki, *Theory of Operator Algebras II*, Lemmas XI.1.11–1.13, Corollaries XI.1.14–1.16 and Lemma XI.1.17, printed pages 321–325 ([edition record](https://doi.org/10.1007/978-3-662-10451-4)). The full supporting arguments above use the stated earlier programme proofs; this citation is not a replacement for them.
