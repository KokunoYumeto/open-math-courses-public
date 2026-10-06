# Resolved corner kernels and their exact inverse

These connected components retain AN03-U032, *Totally characteristic operators on the half space*, Sections 2–5, Section 6 through Example 6.7, and Sections 7–13. Original author: Claude Opus 5.5 (Anthropic), September 2026; editorial additions: Codex, September 2026. Both were dedicated to the public domain (CC0). Current prerequisite connections and proof clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, also CC0. The selected components retain every mathematical display, the full scalar and finite-matrix hypotheses, and all five original solved exercises.

The approved mathematical antecedent is Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1, Section 18.3. Its use and ordinary citation are valid. Complete proofs are supplied in the components and the exact earlier programme proofs. The earlier linked components retain their individual licences.

The four components, in proof order, are [Boundary tests, lacunary symbols and all normal jets](boundary-tests-and-lacunary-symbols.md), [Resolved corner kernels and their exact inverse](resolved-corner-kernels.md), [Boundary adjoints, complete composition and distributional action](boundary-adjoints-composition-and-distributions.md), [Boundary operator bounds, conormal action and the residual obstruction](boundary-bounds-and-conormal-action.md). Original section and equation numbers are retained across them. Sections 6.8 (polyhomogeneous corner characterization) and 14 (arbitrary positive-order Sobolev loss) are separate unadopted obligations; the theorems below do not substitute for those results or for the global compressed wave-front calculus.

The symbol class, Fourier-kernel construction, conventions and exact prerequisites are in [Sections 1–5](boundary-tests-and-lacunary-symbols.md). This component proves all uniform estimates at the resolved corner, their converse and the finite negative-order Schur kernel bound.

## 6. Kernels near the corner

### Coordinates at the corner

Kernels of totally characteristic operators live on
\[
Q=\{(x,y)\in\mathbb R^{2n}:x_n\geq0,\ y_n\geq0\},\qquad \partial_2Q=\{(x,y):x_n=y_n=0\},
\]
the quarter space and its distinguished boundary. Near \(\partial_2Q\) we use
\[
t=\frac{x_n+y_n}2,\qquad r=\frac{x_n-y_n}t\quad(t>0);\qquad x_n=t\Big(1+\frac r2\Big),\quad y_n=t\Big(1-\frac r2\Big).
\tag{6.1}
\]

**Proposition 6.1** (Blow-up coordinates). Write \(\Phi(t,r)=(t(1+r/2),t(1-r/2))\).

1. \(\Phi\) maps \((0,\infty)\times\mathbb R\) diffeomorphically onto \(\{x_n+y_n>0\}\), with \(|\det\Phi'|=t\); hence \(dx_n\,dy_n=t\,dt\,dr\).
2. \(Q\setminus\{x_n=y_n=0\}\) corresponds to \(t>0\), \(|r|\leq2\). The face \(\{x_n=0<y_n\}\) is \(r=-2\), the face \(\{y_n=0<x_n\}\) is \(r=2\), the diagonal \(x_n=y_n\) is \(r=0\), and \(y_n/x_n=(2-r)/(2+r)\).
3. \(\Phi\) extends smoothly to \([0,\infty)\times\mathbb R\) and maps the whole line \(t=0\) to the corner: the corner is blown up into the *front face* \(t=0\), of which the segment \(|r|\leq2\) lies over \(Q\).
4. Normal dilations \((x_n,y_n)\mapsto\lambda(x_n,y_n)\) are \((t,r)\mapsto(\lambda t,r)\), and the radial field is \(x_n\partial_{x_n}+y_n\partial_{y_n}=t\partial_t\).
5. On \(Q\), \(|w|/2\leq t\leq|w|\) for \(w=(x_n,y_n)\); \(r\) is homogeneous of degree 0, so \(|\partial_w^\beta r|\leq C_\beta|w|^{-|\beta|}\) on \(\{x_n+y_n>0\}\cap\{|r|\leq3\}\).
6. The rescaled normal variable in (4.4) is a function of \(r\) alone: \((x_n-y_n)/x_n=2r/(2+r)\).

**Proof.** The Jacobian matrix of \(\Phi\) has rows \((1+\tfrac r2,\tfrac t2)\) and \((1-\tfrac r2,-\tfrac t2)\), with determinant \(-t\); the inverse is (6.1). Parts 2–4 and 6 are direct substitutions. For part 5, \(x_n+y_n\geq|w|\) when both are nonnegative, and \(x_n+y_n\leq\sqrt2|w|\). The set \(\{|r|\leq3\}=\{|x_n-y_n|\leq\tfrac32(x_n+y_n)\}\) is a closed cone that meets the line \(x_n+y_n=0\) only at the origin; its intersection with the unit circle is a compact subset of the open set where \(r\) is smooth. The derivatives of order \(k\) of \(r\) are homogeneous of degree \(-k\), so they are bounded by \(C_k|w|^{-k}\) on that cone. \(\square\)

The point of these coordinates is part 6. The kernel formula (4.4) involves \(x_n^{-1}\) and a function of \((x_n-y_n)/x_n\), and neither is smooth at the corner. But \(tK\) becomes a smooth function of \((t,r)\), as Theorem 6.2 shows.

### Residual kernels

**Theorem 6.2** (Residual kernels).

(a) Let \(a\in S^{-\infty}_{\mathrm{la}}\) and \(A(x,z)=(2\pi)^{-n}\int e^{iz\cdot\xi}a(x,\xi)\,d\xi\). Then \(A\in C^\infty(\overline{\mathbb R}{}^n_+\times\mathbb R^n)\), \(A=0\) for \(z_n\geq1\), and for all \(\alpha,\beta,N\)
\[
|\partial_x^\alpha\partial_z^\beta A(x,z)|\leq C_{\alpha\beta N}(1+|z|)^{-N}(1+x_n)^{-N},
\tag{6.2}
\]
with \(C_{\alpha\beta N}\) bounded by seminorms of \(a\). Conversely every \(A\in C^\infty(\overline{\mathbb R}{}^n_+\times\mathbb R^n)\) satisfying (6.2) and vanishing for \(z_n>1\) comes in this way from exactly one \(a\in S^{-\infty}_{\mathrm{la}}\), namely \(a(x,\xi)=\int e^{-iz\cdot\xi}A(x,z)\,dz\).

(b) For \(a\in S^{-\infty}_{\mathrm{la}}\) the kernel of \(T_a\) is the locally integrable function
\[
K(x,y)=x_n^{-1}A\Big(x,\,x'-y',\,\frac{x_n-y_n}{x_n}\Big)\quad(x_n>0),\qquad K(x,y)=0\quad(x_n<0).
\tag{6.3}
\]
For \(x_n>0\) and \(u\in\mathcal S\), \(T_au(x)=\int K(x,y)u(y)\,dy\), and \(\int|K(x,y)|\,dy=\int|A(x,z)|\,dz\leq C(1+x_n)^{-N}\). Moreover \(\operatorname{supp}K\subset Q\) and \(K\in C^\infty(\mathbb R^{2n}\setminus\partial_2Q)\).

(c) The function \(F(x',y',t,r)=t\,K(x',t(1+\tfrac r2),y',t(1-\tfrac r2))\), \(t>0\), extends to a \(C^\infty\) function on \(\{t\geq0\}\times\mathbb R^{n-1}_{x'}\times\mathbb R^{n-1}_{y'}\times\mathbb R_r\), which vanishes for \(|r|\geq2\). For all \(\alpha,\beta,\tau,\rho,\nu\) and \(r>-2\),
\[
|D^\alpha_{x'}D^\beta_{y'}D^\tau_tD^\rho_rF|\leq C(1+|x'-y'|+t)^{-\nu}(2+r)^{\nu},
\tag{6.4}
\]
and in particular
\[
|D^\alpha_{x'}D^\beta_{y'}D^\tau_tD^\rho_rF|\leq C'(1+|x'-y'|+t)^{-\nu}.
\tag{6.5}
\]
On the front face,
\[
F(x',y',0,r)=\frac{2}{2+r}\,A\Big(x',0,\,x'-y',\,\frac{2r}{2+r}\Big)\quad(r>-2).
\tag{6.6}
\]

(d) Conversely, let \(K\in L^1_{\mathrm{loc}}(\mathbb R^{2n})\) with \(\operatorname{supp}K\subset Q\), and suppose that the function \(F\) of (c) agrees almost everywhere on \(t>0\) with a function in \(C^\infty(\{t\geq0\})\) that vanishes for \(|r|\geq2\) and satisfies (6.5). Then \(K\) is, almost everywhere, the kernel of \(T_a\) for exactly one \(a\in S^{-\infty}_{\mathrm{la}}\).

**Proof.** (a) For \(a\in S^{-\infty}_+\), integration by parts gives
\(z^\gamma\partial^\beta_z\partial^\alpha_xA=(2\pi)^{-n}\int e^{iz\cdot\xi}(-D_\xi)^\gamma[(i\xi)^\beta\partial^\alpha_xa]\,d\xi\), with an integrand bounded by \(C(1+|\xi|)^{-n-1}(1+x_n)^{-N}\). This proves smoothness and (6.2). For fixed \((x,\xi')\), \(a(x,\xi',\cdot)\in\mathcal S(\mathbb R)\), so \(\mathcal F_na\) is a continuous function; by (4.5) it vanishes for \(t<-1\). Since \(A(x,z)=(2\pi)^{-n}\int e^{iz'\cdot\xi'}(\mathcal F_na)(x,\xi',-z_n)\,d\xi'\), \(A=0\) for \(z_n>1\), and by continuity for \(z_n\geq1\). Conversely, if \(A\) satisfies (6.2), then \(\xi^\gamma\partial_\xi^\beta\partial_x^\alpha a=\int e^{-iz\cdot\xi}D_z^\gamma[(-iz)^\beta\partial_x^\alpha A]\,dz\) is bounded by \(C(1+x_n)^{-N}\), so \(a\in S^{-\infty}_+\); Fourier inversion recovers \(A\) from \(a\); and \(\mathcal F_na(x,\xi',t)=2\pi\int e^{-iz'\cdot\xi'}A(x,z',-t)\,dz'\) vanishes for \(t<-1\). Uniqueness is Fourier inversion.

(b) For \(x_n>0\) fixed, \(a^\flat(x,\cdot)\in\mathcal S(\mathbb R^n)\), because \(a\) decreases rapidly in \((\xi',x_n\xi_n)\). So \(K(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a^\flat(x,\xi)d\xi\) converges absolutely, and the substitution \(\eta_n=x_n\xi_n\) gives (6.3). Fubini gives \(T_au(x)=\int K(x,y)u(y)dy\). The change of variables \(z=(x'-y',(x_n-y_n)/x_n)\), \(dy=x_n\,dz\), gives \(\int|K(x,y)|dy=\int|A(x,z)|dz\). Hence \((T_au,v)=\iint K(x,y)u(y)\overline{v(x)}\,dy\,dx\) for \(u,v\in\mathcal S\), with absolute convergence; so \(K\), which is locally integrable, is the Schwartz kernel. If \(x_n<0\), \(K=0\). If \(x_n>0>y_n\), then \((x_n-y_n)/x_n>1\) and \(A=0\). So \(K\) vanishes outside \(Q\), up to the null set \(x_n=0\).

Smoothness off \(\partial_2Q\). Near a point with \(x_n>0\), (6.3) is smooth. Near a point with \(x_n<0\), or with \(x_n=0\) and \(y_n<0\), \(K=0\). Let \(x^0_n=0<y^0_n\). For \(x_n>0\) small and \(y_n\) near \(y^0_n\), the normal argument \(z_n=(x_n-y_n)/x_n\) satisfies \(|z_n|\geq y^0_n/(2x_n)\). By the chain rule, a derivative of order \(|\gamma|\) of \(K\) is a finite sum of terms \(x_n^{-k}y_n^l(\partial A)(x,z)\) with \(k\leq1+2|\gamma|\), \(l\leq|\gamma|\), and \(|\partial A|\leq C_M(1+|z_n|)^{-M}\leq C_M(2x_n/y^0_n)^M\). So \(K\) and all its derivatives tend to 0 as \(x_n\to0+\), uniformly near the point. Since \(K=0\) for \(x_n\leq0\), \(K\) is smooth there.

(c) For \(t>0\) and \(r>-2\) we have \(x_n=t(1+r/2)>0\), \((x_n-y_n)/x_n=2r/(2+r)\) and \(t/x_n=2/(2+r)\). So by (6.3)
\[
F=\frac2{2+r}\,A\Big(x',\,t\big(1+\tfrac r2\big),\,x'-y',\,\frac{2r}{2+r}\Big)=:G .
\tag{6.7}
\]
The right side is smooth on \(\{t\geq0,\ r>-2\}\), because \(A\) is smooth up to \(x_n=0\). It vanishes for \(r\geq2\), where \(2r/(2+r)\geq1\). For \(t>0\), \(r<-2\) we have \(x_n<0\) and \(F=0\).

Now let \(-2<r<2\) and write \(z_n=2r/(2+r)\), \(z'=x'-y'\), \(x_n=t(2+r)/2\). Then
\[
\frac1{2+r}\leq\frac{1+|z_n|}2,\qquad t=\frac{2x_n}{2+r}\leq x_n(1+|z_n|).
\tag{6.8}
\]
The first inequality holds because \(1+|z_n|\geq1\geq2/(2+r)\) when \(r\geq0\), and \(1+|z_n|=(2-r)/(2+r)\geq2/(2+r)\) when \(r<0\). By the chain rule, \(D^\alpha_{x'}D^\beta_{y'}D^\tau_tD^\rho_rG\) is a finite sum of terms \(c\,t^k(2+r)^{-l}(\partial_x^\mu\partial_z^\kappa A)(x',x_n,z',z_n)\) with \(0\leq k\leq\rho\) and \(l\leq1+2\rho\): an \(r\)-derivative may hit \((2+r)^{-l}\), the argument \(t(1+r/2)\) (factor \(t/2\)) or the argument \(2r/(2+r)\) (factor \(4/(2+r)^2\)); a \(t\)-derivative brings the factor \((2+r)/2\). By (6.8) and (6.2), each term is at most
\[
C\,x_n^k(1+|z_n|)^{k+l_+}(1+|z|)^{-M}(1+x_n)^{-M}.
\]
On the other hand \(1+|x'-y'|+t\leq(1+|z'|)(1+x_n)(1+|z_n|)\leq(1+|z|)^2(1+x_n)\) and \((2+r)^{-\nu}\leq(1+|z|)^\nu\). Choosing \(M\) large gives (6.4) for \(-2<r<2\); for \(r\geq2\) the left side vanishes. In particular every derivative of \(G\) tends to 0 as \(r\downarrow-2\), locally uniformly (also at \(t=0\)); so \(G\), extended by 0 to \(r\leq-2\), is smooth, and it equals \(F\). Since \(2+r\leq4\) on the support, (6.4) implies (6.5). Formula (6.6) is (6.7) at \(t=0\).

(d) Taylor's formula at \(r=-2\), where \(F\) vanishes to infinite order, turns (6.5) into (6.4): \(|\partial_r^\rho F(r)|\leq\sup_{[-2,r]}|\partial_r^{\rho+\nu}F|\,(r+2)^\nu/\nu!\). Define, for \(x\in\overline{\mathbb R}{}^n_+\),
\[
A(x,z)=\frac2{2-z_n}\,F\Big(x',\,x'-z',\,\frac{x_n(2-z_n)}2,\,\frac{2z_n}{2-z_n}\Big)\quad(z_n<2),\qquad A(x,z)=0\quad(z_n>1).
\tag{6.9}
\]
On \(1<z_n<2\) both definitions give 0, because then \(2z_n/(2-z_n)>2\); so \(A\) is smooth. For \(z_n\leq1\) put \(r=2z_n/(2-z_n)\in(-2,2]\) and \(t=x_n(2-z_n)/2\). Then \(r+2=4/(2-z_n)\leq8/(1+|z_n|)\) and \(x_n/2\leq t\leq x_n(1+|z_n|)\). Every derivative of \(A\) is a finite sum of terms (polynomial in \(x_n\)) \(\times\) (smooth function of \(z_n\) growing at most polynomially on \(z_n\leq1\)) \(\times\) (a derivative of \(F\) at the displayed point). By (6.4) such a term is at most \(C(1+x_n)^{k}(1+|z_n|)^{k}(1+|z'|+x_n/2)^{-\nu}(1+|z_n|)^{-\nu}\), and choosing \(\nu\) large gives (6.2). By (a), \(A\) comes from a unique \(a\in S^{-\infty}_{\mathrm{la}}\). Finally, for \(x_n>0<y_n\), inserting \(z=(x'-y',(x_n-y_n)/x_n)\) into (6.9) gives \(2/(2-z_n)=x_n/t\), \(x_n(2-z_n)/2=t\) and \(2z_n/(2-z_n)=r\), so the kernel (6.3) of \(T_a\) equals \(F/t=K\) almost everywhere; for \(y_n<0\) both vanish. \(\square\)

**Remark 6.3** (Singular kernels of order \(-\infty\)). For an ordinary pseudodifferential operator of order \(-\infty\) the kernel is smooth. Here, by (c), \(K=F/t\) near the corner, and the leading part \(F(x',y',0,r)/t\) is homogeneous of degree \(-1\) in \((x_n,y_n)\). It is not smooth, and not even bounded, unless \(F\) vanishes on the front face. This singularity is what makes residual operators fail to improve regularity in Section 12.

### A kernel bound at finite negative order

**Proposition 6.4** (A kernel bound). Let \(a\in S^{-n-2}_{\mathrm{la}}\). Then the kernel of \(T_a\) is a function, and
\[
|K_a(x,y)|\leq C\,(1+|x'-y'|)^{-n}\,\frac{x_ny_n}{(x_n+y_n)^3}\quad(x_n,y_n>0),\qquad K_a=0\ \text{elsewhere},
\tag{6.10}
\]
with \(C\) bounded by a seminorm of \(a\). Consequently \(\sup_x\int|K_a(x,y)|dy\) and \(\sup_y\int|K_a(x,y)|dx\) are at most \(\tfrac12C\int_{\mathbb R^{n-1}}(1+|z'|)^{-n}dz'\).

**Proof.** For \(x_n>0\), \(|a^\flat(x,\xi)|\leq C(1+|(\xi',x_n\xi_n)|)^{-n-2}\) is integrable in \(\xi\), so \(K_a(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a^\flat d\xi\) converges absolutely, \(T_au(x)=\int K_a(x,y)u(y)dy\), and (6.3) holds with the bounded continuous function \(A(x,z)=(2\pi)^{-n}\int e^{iz\cdot\xi}a(x,\xi)d\xi\). As in Theorem 6.2(a), \(\mathcal F_na\) is now a continuous function, so \(A=0\) for \(z_n\geq1\). Integration by parts gives \(|z^\gamma A|\leq C\) for \(|\gamma|\leq n+2\), because \(|\partial_\xi^\gamma a|\leq C(1+|\xi|)^{-n-2-|\gamma|}\) is integrable; so \((1+|z'|)^n(1+|z_n|)^2|A|\leq C\). Likewise \(\partial_{z_n}A=(2\pi)^{-n}\int e^{iz\cdot\xi}i\xi_na\,d\xi\) and \(|z'^\gamma\partial_{z_n}A|\leq C\) for \(|\gamma|\leq n\). Since \(A(x,z',1)=0\), the mean value theorem gives \(|A(x,z)|\leq C(1+|z'|)^{-n}|1-z_n|\) for \(z_n\leq1\).

If \(0<x_n\leq y_n\), then \(z_n=(x_n-y_n)/x_n\leq0\), \(1+|z_n|=y_n/x_n\), and \(|K_a|\leq x_n^{-1}C(1+|z'|)^{-n}(x_n/y_n)^2=C(1+|z'|)^{-n}x_n/y_n^2\leq8C(1+|z'|)^{-n}x_ny_n/(x_n+y_n)^3\), because \(x_n+y_n\leq2y_n\). If \(0<y_n<x_n\), then \(|1-z_n|=y_n/x_n\) and \(|K_a|\leq C(1+|z'|)^{-n}y_n/x_n^2\leq8C(1+|z'|)^{-n}x_ny_n/(x_n+y_n)^3\). For the marginals, \(\int_{\mathbb R^{n-1}}(1+|z'|)^{-n}dz'<\infty\) and \(\int_0^\infty x_ny_n(x_n+y_n)^{-3}dy_n=\int_0^\infty s(1+s)^{-3}ds=\tfrac12\); the bound is symmetric in \(x_n,y_n\). \(\square\)

The two cases correspond to the two sides of the diagonal: for \(y_n\geq x_n\) the decay of \(A\) in \(z_n\) is used, for \(y_n<x_n\) the vanishing of \(A\) at \(z_n=1\), that is, lacunarity.

### Examples of residual kernels

**Example 6.5** (Without lacunarity the operator sees below the boundary). Let \(0\leq h\in C_0^\infty(\mathbb R^n)\) be supported near \((0,\tfrac32)\), with \(h(0,\tfrac32)>0\), and \(a=e^{-x_n}\widehat h(\xi)\in S^{-\infty}_+\). Then \(A=e^{-x_n}h\) does not vanish on \(z_n>1\), so \(a\) is not lacunary. For \(0\leq u\in C_0^\infty(\mathbb R^n_-)\) supported near \((0,-\tfrac12)\), with \(u(0,-\tfrac12)>0\), formula (6.3), whose derivation for \(x_n>0\) in Theorem 6.2(b) does not use lacunarity, gives \(T_au(0,1)=e^{-1}\int h(-y',1-y_n)u(y)\,dy>0\), since \(1-y_n\) is near \(\tfrac32\) there. So \(T_au\neq0\) in \(\mathbb R^n_+\) although \(u=0\) in \(\mathbb R^n_+\): lacunarity cannot be dropped from Theorem 5.1(a), in accordance with Proposition 4.3.

**Example 6.6** (A residual kernel in one dimension). Let \(n=1\), \(0\neq h\in C_0^\infty((-\tfrac12,\tfrac12))\) and \(a(x,\xi)=e^{-x}\widehat h(\xi)\). Then \(K(x,y)=e^{-x}x^{-1}h((x-y)/x)\) for \(x>0\), and
\[
T_au(x)=e^{-x}\int h(1-s)\,u(xs)\,ds,\qquad F(t,r)=\frac{2e^{-t(1+r/2)}}{2+r}\,h\Big(\frac{2r}{2+r}\Big).
\]
The kernel vanishes unless \(\tfrac12<y/x<\tfrac32\), and \(F\) vanishes unless \(-\tfrac25<r<\tfrac23\). Along the diagonal \(K(x,x)=e^{-x}h(0)/x\), which is unbounded if \(h(0)\neq0\): a symbol of order \(-\infty\) with an unbounded kernel. \(T_a\) is bounded on \(L^2(0,\infty)\) by Proposition 6.4 and gains no derivative by Theorem 12.1. The model \(T_0u(x)=\int h(1-s)u(xs)ds\) on the front face (so \(T_a=e^{-x}T_0\)) is not in the class, since its symbol does not decay in \(x\). It commutes with the unitary dilations \(u\mapsto\lambda^{1/2}u(\lambda\,\cdot)\) of \(L^2(0,\infty)\), and Minkowski's inequality gives \(\|T_0u\|\leq\int|h(1-s)|s^{-1/2}ds\,\|u\|\), since \(\|u(\cdot\,s)\|=s^{-1/2}\|u\|\).

**Example 6.7** (The resolved kernel near \(r=-2\)). In Example 6.6, \(F\) vanishes identically near \(r=-2\) because \(h\) has compact support. For a lacunary but not strongly lacunary symbol, take \(n=1\) and \(A(x,z)=e^{-x}g(z)\) with \(g\in\mathcal S(\mathbb R)\) vanishing for \(z\geq1\) but not near \(-\infty\), for instance \(g(z)=e^{-1/(1-z)}e^{-z^2}\) for \(z<1\) and \(g(z)=0\) for \(z\geq1\). Then \(F(t,r)=\tfrac2{2+r}e^{-t(1+r/2)}g(\tfrac{2r}{2+r})\), and as \(r\downarrow-2\) the argument \(2r/(2+r)\to-\infty\), where \(g\) decreases rapidly; this is the flatness at \(r=-2\) used in (6.4). At \(r=2\) the argument tends to 1, where \(g\) vanishes to infinite order.

