# Zero cases, kernel support and real spectral receiving maps

*Original contributions by GPT-6.1 Sol (OpenAI) and OpenAI Codex, October 2026. Dedicated to CC0 1.0 to the extent rights exist.*

The prerequisite proofs are the existing Spectral measures with the original operator domain retained, Sections 2–4 and 6.1. Those inherited proofs retain their GFDL licence. The following four additions are available under CC0.

**The zero-space case.** If \(H=\{0\}\), the operator algebra has just one element: the map sending zero to zero. Its norm, defined using the closed unit ball, is zero. The preceding definition using unit vectors therefore needs a separate value in this case: set \(\beta=0\). This gives both assertions of (BS5), since every vector and every value of \(B\) is zero.

There is exactly one projection-valued measure on this space. All its projections are zero, which is also the identity of the zero space. Every scalar measure is the zero measure. Thus every Borel moment is zero, every finite-valued Borel multiplier has domain \(H\), and every integral operator is zero. The spectral essential bound, defined as the infimum of the nonnegative \(c\) for which \(E(\{|f|>c\})=0\), is consequently zero. Statements proved by choosing a unit vector in a nonzero projection range have no case to check here. These observations include the zero space without assigning a real supremum to an empty unit sphere.

**The zero-vector case in the unbounded estimate.** Sesquilinearity gives \(\mu_{x,0}(B)=0\) for every Borel set \(B\). Its variation is therefore the zero measure, and

\[
 \int_K h\,d|\mu_{x,0}|=0
\]

for every nonnegative Borel \(h\). This conclusion also holds when the \(h^2\)-moment of \(\mu_x\) is infinite. In (BS24), the bound for \(y=0\) is accordingly stated as zero; an expression \(0\cdot\infty\) is not evaluated.

For \(y\ne0\), the bound in (BS24) has its usual extended-real meaning. To see all cases explicitly, put \(M=\int_Kh^2\,d\mu_x\). If \(M=\infty\), the right side is infinite because \(\|y\|>0\). If \(M<\infty\), apply the finite-partition estimate (BS23) to a nonnegative simple \(q=\sum_j c_j1_{B_j}\leq h\). Scalar Cauchy–Schwarz gives

\[
 \int q\,d|\mu_{x,y}|
 \leq \sum_j c_j\mu_x(B_j)^{1/2}\mu_y(B_j)^{1/2}
 \leq \left(\int q^2\,d\mu_x\right)^{1/2}\|y\|
 \leq M^{1/2}\|y\|.
\]

The nonnegative integral is the supremum over these simple functions, so the same bound holds for \(h\). This proves the estimate with its finite, infinite and zero-vector cases separated.

**Keeping a nonzero kernel.** Now let \(S\) be any bounded positive self-adjoint contraction on the same complex Hilbert space, allowing a nontrivial kernel. The injective theorem above applies after the following orthogonal decomposition.

Set \(\mathcal N=\ker S\) and \(\mathcal M=\mathcal N^\perp\). The kernel is closed because \(S\) is bounded. The closed-subspace decomposition in Section 6.1 gives \(H=\mathcal N\oplus\mathcal M\). For \(m\in\mathcal M\) and \(n\in\mathcal N\), self-adjointness gives \((Sm,n)=(m,Sn)=0\); hence \(\mathcal M\) is invariant. Its restriction \(S_{\mathcal M}\) is a positive self-adjoint contraction and is injective. Indeed a vector in both \(\mathcal M\) and \(\ker S\) must vanish. On the other summand \(S\) is zero.

Apply Sections 3.2–3.9 to \(S_{\mathcal M}\), including the preceding zero-space case if \(\mathcal M=0\). Write \(E_{\mathcal M}\) for its PVM. Define, for Borel \(B\subseteq[0,1]\),

\[
 E(B)(n+m)=1_B(0)n+E_{\mathcal M}(B)m
 \qquad(n\in\mathcal N,\ m\in\mathcal M).
\]

The two summands are orthogonal. Projection multiplication and adjoints follow on each summand; countable additivity follows in norm from that of \(E_{\mathcal M}\) and ordinary additivity of the indicator at zero. The coordinate integral is \(0\oplus S_{\mathcal M}=S\). For \(u=n+m\), the scalar measure is

\[
 \mu_u=\|n\|^2\delta_0+\mu_m^{\mathcal M}.
\]

Consequently a finite-valued Borel \(f\) has exactly the domain and action

\[
 D(f(S))=\mathcal N\oplus D(f(S_{\mathcal M})),\qquad
 f(S)(n+m)=f(0)n+f(S_{\mathcal M})m.
\]

This is the moment domain (BS3), because its squared moment is \(|f(0)|^2\|n\|^2+\int|f|^2\,d\mu_m^{\mathcal M}\). The first summand is an everywhere-defined bounded scalar operator. Density, closedness and the adjoint identity on the entire domain therefore follow from the corresponding statements on \(\mathcal M\): a convergent graph sequence converges on both orthogonal components, and testing the adjoint separately against each component gives exactly their two adjoint domains. The product domain, sum domain and closures are likewise those of Section 3.8 on \(\mathcal M\), together with the full summand \(\mathcal N\). Thus (BS49)–(BS54), including their precise moment intersections and kernel formula, extend to this \(S\).

For completeness, this PVM is unique. Given another PVM \(Q\) with coordinate integral \(S\), bounded simple-function multiplication and strong limits give \(\|Su\|^2=\int t^2\,d(Q(t)u,u)\). A vector annihilated by \(S\) has zero measure on every \([1/j,1]\), and hence equals \(Q(\{0\})u\). Conversely the coordinate integral annihilates \(Q(\{0\})H\). Thus \(Q(\{0\})\) is exactly the projection onto \(\mathcal N\). Since all projections of \(Q\) commute, this decomposes \(Q\) into point mass at zero on \(\mathcal N\) and a PVM representing \(S_{\mathcal M}\) on \(\mathcal M\). Injective uniqueness there gives \(Q=E\).

Use the function \(r_0\) in (BS57), including its value zero at zero. With \(N\) denoting the projection onto \(\mathcal N\), put

\[
 N=E(\{0\}),\qquad P=I-N=E((0,1]),\qquad
 R=T_{r_0},\qquad
 D(R)=\left\{u:\int_{(0,1]}t^{-2}\,d\mu_u<\infty\right\}.
 \tag{SE1}
\]

On the orthogonal components this is \(R=0\oplus S_{\mathcal M}^{-1}\). The inverse on \(\mathcal M\) is the densely defined closed self-adjoint operator already constructed in (BS58), on \(\operatorname{Ran}S_{\mathcal M}\). Hence \(R\) has those same properties on \(H\), its squared norm is the full integral in (SE1), and its kernel is \(\mathcal N\). The two inverse products on \(\mathcal M\) are the identity, whereas both products vanish on \(\mathcal N\). Keeping their domains gives

\[
 RS=P\quad\hbox{on }H,\qquad
 SR=P\quad\hbox{on }D(R).
 \tag{SE2}
\]

Every \(Su\) lies in \(\mathcal M\), and its component belongs to the inverse domain. Conversely, if \(u\in D(R)\), then \(Pu=S(Ru)\) belongs to \(\operatorname{Ran}S\), while \(Nu\in\mathcal N\). These facts give

\[
 D(R)=\operatorname{Ran}S\oplus NH,
 \qquad \overline{\operatorname{Ran}S}=PH.
 \tag{SE3}
\]

The closure assertion also follows directly: \(v\perp\operatorname{Ran}S\) means \((Sx,v)=0\) for all \(x\), which is equivalent to \(Sv=0\). Taking orthogonal complements gives the second equality in (SE3). It does not make \(\operatorname{Ran}S\) closed. The restriction \(S:PH\to\operatorname{Ran}S\) is bijective, with inverse \(R\) on that range. In particular \(R(D(R))\subseteq PH\); its norm is the stated moment, and no bound \(S\geq cI\) with \(c>0\) follows.

**Solved example.** On \(H=\ell^2(\mathbb N_0)\), define \((Su)_0=0\) and \((Su)_j=u_j/j\) for \(j\geq1\). The coordinate estimates give \(\|Su\|\leq\|u\|\), the inner-product sum gives self-adjointness and positivity, and \(Se_1=e_1\) shows that the norm is one. Let \(E(B)\) keep coordinate zero when \(0\in B\), and coordinate \(j\geq1\) when \(1/j\in B\). These are orthogonal projections. For disjoint \(B_k\), the squared remainder after the first \(l\) projections is a subseries of \(\sum_j|u_j|^2\) whose indicators decrease to zero; convergence of that series makes the remainder tend to zero. Thus this is a strongly countably additive PVM. Its coordinate integral is \(S\), so the uniqueness just proved identifies it with the constructed PVM. Formula (SE1) now becomes

\[
 D(R)=\left\{u:\sum_{j=1}^{\infty}j^2|u_j|^2<\infty\right\},
 \qquad (Ru)_0=0,\qquad (Ru)_j=ju_j\ (j\geq1).
 \tag{SE4}
\]

A vector \(v\) lies in \(\operatorname{Ran}S\) exactly when \(v_0=0\) and \(\sum_{j\geq1}j^2|v_j|^2<\infty\): necessity follows by writing \(v=Su\), and sufficiency by taking \(u_j=jv_j\) and \(u_0=0\). Finite sequences in \(PH\) lie in this range and are dense there. But \(v_0=0,\ v_j=1/j\) belongs to \(PH\) and not to the range. Indeed \(\sum_{j\geq1}j^{-2}\) converges, since for \(j\geq2\) its terms are bounded by \(1/(j-1)-1/j\), while \(\sum j^2|v_j|^2=\sum1\) diverges. This proves nonclosedness. Finally \(e_0\ne0\) and both products in (SE2) send it to zero, so replacing \(P\) by \(I\) would be incorrect. For the injective \(S\) in Section 4, \(N=0\), and (SE1)–(SE3) reduce to the existing inverse theorem without changing its domain or constants.

**Receiving maps for an original real Hilbert space.** Let \(H_{\mathbb R}\) be a real Hilbert space with its given inner product \([x,u]\). Use the pair vector space and scalar law

\[
 H_{\mathbb C}=H_{\mathbb R}\times H_{\mathbb R},\qquad
 (a+ib)(x,y)=(ax-by,bx+ay),\qquad
 ((x,y),(u,v))=[x,u]+[y,v]+i([y,u]-[x,v]).
 \tag{SE5}
\]

This is a complex Hilbert space with the convention that the first variable is linear. Additivity and real homogeneity follow from the four real pairings. Substitution of \(i(x,y)=(-y,x)\) gives \((iz,w)=i(z,w)\); conjugate symmetry then gives conjugate-linearity in the second variable. On the diagonal the imaginary part cancels, leaving \(\|x\|^2+\|y\|^2\), positive unless both components vanish. If \(w\ne0\), expansion of \((z-\alpha w,z-\alpha w)\) with \(\alpha=(z,w)/(w,w)\) proves scalar Cauchy–Schwarz; if \(w=0\), that inequality is immediate. Applying it to the cross term proves the triangle inequality. A Cauchy sequence of pairs has Cauchy original components, whose limits converge in the sum of squares. Thus completeness and the original inner product are retained, without a separability assumption. This pair construction also appears as (BC8) in Banach estimates, quotient spaces and compact parameter arguments.

Write \(\iota x=(x,0)\), \(\operatorname{Re}(x,y)=x\), and \(C(x,y)=(x,-y)\). The injection is isometric and both coordinate projections are contractions. Direct substitution in (SE5) gives \(C^2=I\) and \((Cz,Cw)=\overline{(z,w)}\). Its fixed vectors are precisely \(\iota H_{\mathbb R}\).

For a densely defined real-linear \(L:D(L)\subseteq H_{\mathbb R}\to K_{\mathbb R}\), define \(L_{\mathbb C}(x,y)=(Lx,Ly)\) with domain \(D(L)\times D(L)\). Coordinate approximation proves density of this domain. If \(L\) is closed, convergence of a pair and its image gives each real graph limit, so \(L_{\mathbb C}\) is closed. Conversely apply complex closedness to a real graph sequence \((x_j,0)\) and its image to conclude closedness of \(L\).

The real adjoint domain consists of those \(u\) for which there is \(p\in H_{\mathbb R}\) satisfying \([Lx,u]_K=[x,p]_H\) for all \(x\in D(L)\); its value is this uniquely determined \(p\). The complex and real adjoints have exactly

\[
 D(L_{\mathbb C}^*)=D(L^*)\times D(L^*),\qquad
 L_{\mathbb C}^*(u,v)=(L^*u,L^*v).
 \tag{SE6}
\]

To check necessity, take \((u,v)\) in the complex adjoint domain with value \((p,q)\). Test its defining identity against \((x,0)\). Formula (SE5) gives \([Lx,u]-i[Lx,v]=[x,p]-i[x,q]\), so its real and imaginary parts place \(u,v\) in the two real adjoint domains with the displayed values. For sufficiency, these two real identities applied first to \(x\) and then to \(y\) give all four terms of the complex adjoint identity against every \((x,y)\in D(L)\times D(L)\). This proves the whole adjoint domain. It assumes no density of \(D(L^*)\) for a general \(L\); applying the statement to \(L^*\) requires that density separately.

Suppose the original \(A=A^*\) on \(H_{\mathbb R}\) is densely defined and satisfies \([Ax,x]\geq a\|x\|^2\). Equation (SE6) makes \(A_{\mathbb C}\) self-adjoint on exactly \(D(A)\times D(A)\). Moreover

\[
 (A_{\mathbb C}(x,y),(x,y))
 =[Ax,x]+[Ay,y]+i([Ay,x]-[Ax,y])
 =[Ax,x]+[Ay,y]\geq a(\|x\|^2+\|y\|^2).
 \tag{SE7}
\]

The vanishing imaginary term uses the symmetry of the given real \(A\). Choose exactly \(\rho\geq1+\max(0,-a)\) and \(\delta=a+\rho\geq1\), and set \(T=A+\rho I\) on \(D(A)\), as in (LB2). Real Cauchy–Schwarz and \([Tv,v]\geq\delta\|v\|^2\) give \(\|Tv\|\geq\delta\|v\|\), with the zero-vector case immediate. Section 4 applied to \(A_{\mathbb C}\) gives the bijection \(T_{\mathbb C}\) and inverse norm at most \(\delta^{-1}\). For a right-hand side \((x,0)\), write its inverse as \((u,v)\). Then \(Tu=x\), \(Tv=0\); the real lower estimate forces \(v=0\). Hence \(T\) is onto its original real Hilbert space. It is injective by the same estimate. Its real inverse \(S\) obeys \(\|S\|\leq\delta^{-1}\), and the complex inverse is precisely \(S_{\mathbb C}\). The upper bound \(\|S_{\mathbb C}\|\leq\|S\|\) follows from the two squared component estimates; testing on \(\iota x\) gives the reverse inequality. Thus the norms agree. For \(x=Tu,\ y=Tv\), the identities \([Sx,y]=[u,Tv]=[Tu,v]=[x,Sy]\) and \([Sx,x]=[u,Tu]\geq0\) prove real self-adjointness and positivity. Both inverse products keep the domains in (LB3).

We also need the PVM of the complexification of any real bounded positive contraction \(S\), whether injective or not. Equation (SE6) gives self-adjointness of \(S_{\mathbb C}\); the component norm estimate gives the same norm, and its quadratic form is \([Sx,x]+[Sy,y]\geq0\). Use the bounded theorem and (SE1)–(SE4) to construct \(E\) for \(S_{\mathbb C}\). For each Borel \(B\), the operator \(CE(B)C\) is complex-linear because the two conjugations cancel scalar conjugation. It is a projection, and the identity \((Cz,Cw)=\overline{(z,w)}\) proves its self-adjointness. Products and strong countable sums are preserved by the norm isometry \(C\). Thus \(B\mapsto CE(B)C\) is another orthogonal PVM. Its coordinate integral is \(CS_{\mathbb C}C=S_{\mathbb C}\): this is immediate for real simple approximations of the coordinate function and passes to their uniform limit. Uniqueness, including the noninjective case proved above, yields \(CE(B)C=E(B)\).

The real range of \(\iota\) is therefore invariant under every \(E(B)\). Define

\[
 E_{\mathbb R}(B)x=\operatorname{Re}(E(B)\iota x),\qquad
 E(B)\iota=\iota E_{\mathbb R}(B),\qquad
 E(B)(x,y)=(E_{\mathbb R}(B)x,E_{\mathbb R}(B)y).
 \tag{SE8}
\]

The last identity follows from \((x,y)=\iota x+i\iota y\) and complex-linearity. The second identity transfers projection products, real self-adjointness, normalization and strong countable additivity through the isometry \(\iota\). Hence \(E_{\mathbb R}\) is a real orthogonal PVM. Expanding its scalar pairing with (SE5), its symmetry cancels the two cross terms and gives \(\mu_{(x,y)}=\mu_x^{\mathbb R}+\mu_y^{\mathbb R}\), where \(\mu_x^{\mathbb R}(B)=[E_{\mathbb R}(B)x,x]\).

For the lower-bounded \(A\), use the unchanged \(J=(0,\delta^{-1}]\) and \(\kappa(t)=t^{-1}-\rho\). Define \(F_{\mathbb R}(B)=E_{\mathbb R}(\{t\in J:\kappa(t)\in B\})\). The complex \(F\) in (LB7) is its componentwise complexification. In the following real-line formulas, \(\mu_x^{\mathbb R}(B)\) means \([F_{\mathbb R}(B)x,x]\) for Borel \(B\subseteq\mathbb R\); it is the pushforward of the interval measure. If \(f:\mathbb R\to\mathbb R\) is finite-valued and Borel, each bounded truncation \(f1_{\{|f|\leq n\}}(A_{\mathbb C})\) preserves the fixed space of \(C\): real simple multipliers do so by (SE8), and the bounded spectral limits preserve it as well. The full graph limit therefore restricts to a real operator. Its domain and action are

\[
 D(f(A)_{\mathbb R})=\left\{x:\int |f(\lambda)|^2\,d\mu_x^{\mathbb R}<\infty\right\},
 \qquad f(A)\iota x=\iota f(A)_{\mathbb R}x.
 \tag{SE9}
\]

Here \(f(A)\) on the left of the second identity means the complex spectral operator for \(A_{\mathbb C}\). Because the moment of a pair is the sum of its two nonnegative component moments, its entire complex domain is the product of the two real domains in (SE9). On that domain its action is the componentwise complexification of the real action, first for bounded truncations and then by graph convergence. The real projections \(F_{\mathbb R}(\{|f|\leq n\})\) show that the real domain is dense. A real graph limit is a complex graph limit after \(\iota\), proving closedness. Applying (SE6) to this dense real operator, and using the full complex self-adjoint identity for a real multiplier, gives real self-adjointness with exactly the domain (SE9).

For real Borel \(f,g\), a vector \(x\) belongs to the real product domain precisely when \(\iota x\) belongs to the complex product domain: (SE9) and its action identify both the input and intermediate-vector requirements. Thus (LB15) gives the exact real domain \(D(g(A)_{\mathbb R})\cap D((fg)(A)_{\mathbb R})\), with product action \((fg)(A)_{\mathbb R}\). The real sum starts on \(D(f(A)_{\mathbb R})\cap D(g(A)_{\mathbb R})\). Common real spectral cutoffs, followed by the same graph limits, give its closure as \((f+g)(A)_{\mathbb R}\), and the closure of the product as \((fg)(A)_{\mathbb R}\). No larger initial domain is substituted. The coordinate multiplier equals the original real \(A\), since its complexification equals \(A_{\mathbb C}\) on \(D(A)\times D(A)\) by (LB13). Induction on the exact product domain consequently gives \(D(A^q)=\{x:\int|\lambda|^{2q}\,d\mu_x^{\mathbb R}<\infty\}\) and the original recursive power action for every integer \(q\geq1\). The inverse identities, closed endpoints in (LB17), and all constants in (LB18)–(LB19) transfer through the isometry \(\iota\). Real uniqueness follows too: complexifying a competing real PVM would give a competing complex PVM for \(A_{\mathbb C}\), which the preceding theorem excludes.

Finally let \(f=f_1+if_2\) be complex-valued and finite-valued Borel, with \(f_1,f_2\) real. The appropriate map on a real input takes values in the pair space, and is exactly

\[
 f(A)\iota x=(f_1(A)_{\mathbb R}x,f_2(A)_{\mathbb R}x),\qquad
 D(f(A)\iota)=D(f_1(A)_{\mathbb R})\cap D(f_2(A)_{\mathbb R}).
 \tag{SE10}
\]

The domain equality follows from \(|f|^2=f_1^2+f_2^2\): finiteness of the sum of the two nonnegative moments is equivalent to finiteness of each. On \(F_{\mathbb R}(\{|f|\leq n\})x\), bounded scalar linearity gives the displayed pair action. These vectors converge in both component graph norms whenever the two moments are finite. The closed complex operator then yields that action for the entire displayed domain. Formula (SE5) gives its squared norm as the sum of the two squared real-output norms. In particular \(i\) is not treated as a real scalar operator on \(H_{\mathbb R}\); the real input, complex receiving space and full domain are all specified.
