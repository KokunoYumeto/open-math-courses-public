# Traces, residues and vector bundles on the projective line

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The next lesson studies the curve \(C\) of genus 21 through its degree-four map \(f:C\to\mathbb P^1\): it pushes a line bundle forward to a vector bundle of rank four on \(\mathbb P^1\), equips it with a pairing defined by a trace, and reads off a two-dimensional quadratic space from the splitting of that bundle into line bundles. This lesson proves the four general tools used there, for a finite map \(f:C\to\mathbb P^1\) from a curve of any genus: the trace and its local form at ramification points (Section 1), the residue theorem (Section 2), the description of realizable principal parts by residues (Section 3), and Grothendieck's theorem that every vector bundle on \(\mathbb P^1\) is a direct sum of line bundles (Section 4). Section 5 combines them into a perfect trace pairing.

**Prerequisites.** [*A curve of genus 21 with a fourth root of its canonical bundle*](a-curve-of-genus-21-with-a-fourth-root-of-its-canonical-bundle.md), Lemma 3.1 (the dimension formula). From the course *Cohomology of quasi-coherent sheaves* (AG-QC): [*Cohomology of projective space*](course:AG-QC/cohomology-of-projective-space), Theorem 2.2; [*Serre's theorems on projective schemes*](course:AG-QC/serres-theorems-on-projective-schemes), Theorem 2.1; [*Dualizing sheaves and Serre duality for projective schemes*](course:AG-QC/dualizing-sheaves-and-serre-duality-for-projective-schemes), Theorem 4.2; [*Complex analytic spaces and analytification*](course:AG-QC/complex-analytic-spaces-and-analytification), Lemma 2.2 (holomorphic inverse functions); [*Serre's comparison theorems and Chow's theorem*](course:AG-QC/serres-comparison-theorems-and-chows-theorem), Theorem 3.1; [*The theorem on formal functions*](course:AG-QC/the-theorem-on-formal-functions), Theorem 5.2 (a proper morphism with finite fibres is finite). From *Commutative algebra for geometry* (AG-CA): [*Discrete valuation rings, normal rings and Serre's criterion*](course:AG-CA/discrete-valuation-rings-normal-rings-and-serres-criterion). From *Complex analytic spaces and coherent sheaves*: [*Holomorphic functions of several variables*](course:complex-analytic-spaces-and-coherent-sheaves/holomorphic-functions-of-several-variables), Theorem 4.2 (Riemann extension). Laurent series, residues and contour integrals in one variable as in the core course [*Complex Analysis*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50) (Lebl, *Guide to Cultivating Complex Analysis*).

Throughout, \(C\) is a smooth connected projective curve over \(\mathbb C\), \(f:C\to\mathbb P^1\) is a nonconstant morphism, and \(x\) is the affine coordinate on \(\mathbb P^1\). Where convenient, \(C\) is regarded as a compact Riemann surface; by Serre's comparison theorem, algebraic and holomorphic sections of line bundles and their cohomology agree.

## 1. The trace

The morphism \(f\) is proper, and its fibres are proper closed subsets of the irreducible curve \(C\), hence finite; so \(f\) is finite by Theorem 5.2 of the lesson on formal functions. The local rings of \(\mathbb P^1\) are discrete valuation rings, and \(f_*\mathcal O_C\) is a coherent torsion-free \(\mathcal O_{\mathbb P^1}\)-module, hence locally free; the same holds for \(f_*B\) for every line bundle \(B\) on \(C\). The rank \(n\) of \(f_*\mathcal O_C\) is the *degree* of \(f\). For a point \(x_0\in\mathbb P^1\), the fibre \((f_*\mathcal O_C)\otimes\kappa(x_0)=\mathcal O_C/\mathfrak m_{x_0}\mathcal O_C\) has dimension \(n\), so the divisor \(f^*(x_0)=\sum_{p\mapsto x_0}e_pp\) has degree \(n\); here \(e_p\), the *ramification index*, is the order of vanishing at \(p\) of a local coordinate at \(x_0\). The point \(p\) is a *ramification point* if \(e_p\ge2\), and \(f(p)\) is then a *branch value*. Since \(f^*\mathcal O(1)\) has the divisor \(f^*(x_0)\), \(\deg f^*\mathcal O(1)=n\).

The *trace* \(\operatorname{Tr}:f_*\mathcal O_C\to\mathcal O_{\mathbb P^1}\) sends a section \(h\) over \(f^{-1}(U)\) to the trace of multiplication by \(h\) on the locally free \(\mathcal O_U\)-module \(f_*\mathcal O_C|_U\). On function fields it is the trace of the field extension \(\mathbb C(C)/\mathbb C(x)\), of degree \(n\), and it extends to meromorphic functions on \(C\), which are rational by Serre's comparison theorem.

**Lemma 1.1 (local form).** Let \(x_0\in\mathbb P^1\), and let \(t\) be a local coordinate at \(x_0\) with \(t(x_0)=0\).

1. There are a disc \(\Delta\) around \(x_0\), disjoint discs \(\Delta_p\) around the points \(p\in f^{-1}(x_0)\) with \(f^{-1}(\Delta)=\bigsqcup_p\Delta_p\), and coordinates \(w_p\) on \(\Delta_p\) with \(t\circ f=w_p^{e_p}\).
2. For \(h\) holomorphic on \(f^{-1}(\Delta)\), \(\operatorname{Tr}(h)(t)=\sum_{y\in f^{-1}(t)}h(y)\) for \(t\ne0\), the sum over the \(n\) points of the fibre. In particular, on the component \(\Delta_p\), with \(e=e_p\) and \(w=w_p\),
\[
\begin{gathered}
\operatorname{Tr}(w^k)=e\,t^{k/e}\ \text{ if }e\mid k,\\
\operatorname{Tr}(w^k)=0\ \text{ if }e\nmid k,\qquad(1.1)
\end{gathered}
\]
for every integer \(k\), and the same holds for meromorphic \(h\).

**Proof.** (1) Near \(p\), choose a coordinate \(v\) with \(v(p)=0\). Then \(t\circ f=v^{e}u(v)\) with \(u(0)\ne0\); a holomorphic \(e\)-th root \(u_1\) of \(u\) near \(0\) gives the coordinate \(w=vu_1(v)\), by the holomorphic inverse function theorem (Lemma 2.2 of the lesson on complex analytic spaces), with \(t\circ f=w^e\). Since \(f\) is finite, the preimage of a small enough disc around \(x_0\) lies in the union of small discs around the points of \(f^{-1}(x_0)\), and shrinking gives (1).

(2) For \(t\ne0\) small, \(t\) is not a branch value, so the fibre of \(f_*\mathcal O_C\) at \(t\) is the algebra \(\mathbb C^{n}\) of functions on the \(n\) points of \(f^{-1}(t)\), on which \(h\) acts diagonally; its trace is the sum of the values. On \(\Delta_p\), the points over \(t\) are \(w=\zeta s\), where \(s^e=t\) and \(\zeta\) runs over the \(e\)-th roots of unity, and \(\sum_\zeta(\zeta s)^k\) equals \(es^k=e\,t^{k/e}\) if \(e\mid k\) and \(0\) otherwise. For meromorphic \(h\), apply this to \(h\cdot t^N\) for large \(N\). \(\square\)

A meromorphic function \(h\) on \(C\) that is holomorphic on \(f^{-1}(\Delta)\) has \(\operatorname{Tr}(h)\) holomorphic on \(\Delta\): it is a sum of bounded functions on \(\Delta\setminus\{x_0\}\), hence extends.

**Trace of differentials.** Every meromorphic differential \(\nu\) on \(C\) is \(\nu=h\,f^*(dx)\) for a unique meromorphic function \(h\), since \(f^*(dx)\ne0\). Put
\[
\operatorname{Tr}(\nu)=\operatorname{Tr}(h)\,dx ,
\]
a rational differential on \(\mathbb P^1\). Away from the branch values, \(\operatorname{Tr}(\nu)\) is the sum of the pullbacks of \(\nu\) along the \(n\) local inverses of \(f\), by Lemma 1.1(2); so the definition does not depend on the coordinate \(x\).

## 2. The residue theorem

The *residue* of a meromorphic differential \(\nu\) at \(p\) is the coefficient of \(w^{-1}\,dw\) in its Laurent expansion in a local coordinate \(w\); it equals \(\frac1{2\pi i}\oint\nu\) over a small circle around \(p\), so it does not depend on the coordinate.

**Lemma 2.1 (residues and traces).** For a meromorphic differential \(\nu\) on \(C\) and a point \(x_0\in\mathbb P^1\),
\[
\operatorname{Res}_{x_0}\operatorname{Tr}(\nu)=\sum_{p\in f^{-1}(x_0)}\operatorname{Res}_p\nu .
\]

**Proof.** Use the coordinates of Lemma 1.1. On \(\Delta_p\) write \(\nu=h(w)\,d(w^e)\) with \(h(w)=\sum_kh_kw^k\), a Laurent series with finitely many negative terms; this is possible because \(d(w^e)=f^*(dt)\). Then \(\operatorname{Res}_p\nu\) is the residue at \(w=0\) of \(\sum_kh_kew^{k+e-1}\,dw\), that is \(eh_{-e}\). The contribution of \(\Delta_p\) to \(\operatorname{Tr}(\nu)=\operatorname{Tr}(h)\,dt\) is \(\sum_{e\mid k}h_k\,e\,t^{k/e}\,dt\) by (1.1), whose residue at \(t=0\) is \(e\,h_{-e}\). Summing over \(p\) gives the claim. \(\square\)

**Theorem 2.2 (residue theorem).** For every meromorphic differential \(\nu\) on \(C\), \(\sum_{p\in C}\operatorname{Res}_p\nu=0\).

**Proof.** By Lemma 2.1, the sum equals \(\sum_{x_0\in\mathbb P^1}\operatorname{Res}_{x_0}\mu\) for the rational differential \(\mu=\operatorname{Tr}(\nu)=g(x)\,dx\). Write \(g\) in partial fractions, \(g=P(x)+\sum_{a,k\ge1}c_{a,k}(x-a)^{-k}\) with a polynomial \(P\). The finite residues of \(\mu\) are the \(c_{a,1}\). At infinity, with \(x=1/s\) and \(dx=-s^{-2}ds\): the term \(x^m\,dx=-s^{-m-2}ds\), \(m\ge0\), has residue \(0\); the term \((x-a)^{-1}dx=-s^{-1}(1-as)^{-1}ds\) has residue \(-1\); and \((x-a)^{-k}dx=-s^{k-2}(1-as)^{-k}ds\), \(k\ge2\), is holomorphic at \(s=0\). So \(\operatorname{Res}_\infty\mu=-\sum_ac_{a,1}\), and the total is zero. \(\square\)

## 3. Principal parts and duality

Let \(B\) be a line bundle and \(D=\sum_pm_pp\) an effective divisor on \(C\). Put
\[
\begin{gathered}
\mathrm{PP}_D(B)=H^0\bigl(C,B(D)/B\bigr),\\
\mathrm J_D(K_C-B)=H^0\bigl(D,(K_C-B)|_D\bigr),
\end{gathered}
\]
the *principal parts* of sections of \(B(D)\) and the *jets* along \(D\) of sections of \(K_C-B\). Both have dimension \(\deg D\). The *residue pairing*
\[
\begin{gathered}
\mathrm{PP}_D(B)\times\mathrm J_D(K_C-B)\to\mathbb C,\\
(a,s)\mapsto\sum_p\operatorname{Res}_p(as),
\end{gathered}
\]
is well defined, because changing \(a\) by a local section of \(B\), or \(s\) by a local section of \((K_C-B)(-D)\), changes \(as\) by a holomorphic differential.

**Lemma 3.1.** The residue pairing is perfect.

**Proof.** It is the sum over \(p\) of local pairings. In a coordinate \(z\) at \(p\) and dual frames of \(B\) and \(K_C-B\) (whose product is \(dz\)), a principal part is \(\sum_{i=1}^{m}a_{-i}z^{-i}\) and a jet is \(\sum_{j=0}^{m-1}s_jz^j\), with \(m=m_p\); the pairing is \(\sum_{i=1}^ma_{-i}s_{i-1}\), with an anti-diagonal matrix of ones. \(\square\)

**Proposition 3.2 (realizable principal parts).** The image of the principal-part map \(\mathrm{pp}:H^0(C,B(D))\to\mathrm{PP}_D(B)\), whose kernel is \(H^0(C,B)\), is the annihilator, for the residue pairing, of the image of restriction \(H^0(C,K_C-B)\to\mathrm J_D(K_C-B)\).

**Proof.** If \(T\in H^0(C,B(D))\) and \(s\in H^0(C,K_C-B)\), then \(Ts\) is a meromorphic differential with poles only on \(D\), and its residues sum to zero by Theorem 2.2; so the image lies in the annihilator. Let \(\rho\) be the rank of restriction \(H^0(K_C-B)\to\mathrm J_D(K_C-B)\). By Lemma 3.1 the annihilator has dimension \(\deg D-\rho\), and by the dimension formula (Lemma 3.1 of the lesson on the curve of genus 21) the image has dimension \(h^0(B+D)-h^0(B)=\deg D-\rho\). \(\square\)

## 4. Vector bundles on the projective line

A *vector bundle* is a locally free sheaf of finite rank. A *line subbundle* of a vector bundle \(E\) on a curve is a subsheaf \(L\) of rank one with \(E/L\) locally free; then \(L\) is a line bundle.

**Lemma 4.1 (saturation).** Let \(E\) be a vector bundle on a smooth curve \(X\) and \(\varphi:N\to E\) a nonzero map from a line bundle. There is a line subbundle \(L\subset E\) containing \(\varphi(N)\), with \(\deg L\ge\deg N\).

**Proof.** The image \(\varphi(N)\) is a rank-one subsheaf, isomorphic to \(N\) since \(N\) is torsion-free of rank one and \(\varphi\ne0\). Let \(L\) be the kernel of \(E\to Q/Q_{\mathrm{tors}}\), where \(Q=E/\varphi(N)\) and \(Q_{\mathrm{tors}}\) is its torsion subsheaf. Then \(E/L\cong Q/Q_{\mathrm{tors}}\) is torsion-free, hence locally free over the discrete valuation rings of \(X\), and \(L/\varphi(N)\cong Q_{\mathrm{tors}}\) is a torsion sheaf. So \(L\) has rank one, is torsion-free, hence a line bundle, and \(N\cong\varphi(N)\subset L\) with torsion quotient of finite length \(\delta\ge0\). Comparing divisors of a meromorphic section, \(\deg L=\deg N+\delta\). \(\square\)

**Theorem 4.2 (Grothendieck, 1957).** Every vector bundle \(E\) of rank \(r\) on \(\mathbb P^1\) is isomorphic to \(\mathcal O(a_1)\oplus\cdots\oplus\mathcal O(a_r)\), and the integers \(a_1\ge\cdots\ge a_r\) are determined by \(E\).

**Proof.** Uniqueness: by Theorem 2.2 of the lesson on cohomology of projective space, \(h^0(\mathcal O(a)(k))=\max(a+k+1,0)\), so \(h^0(E(k))=\sum_i\max(a_i+k+1,0)\) for all \(k\), and these numbers determine the \(a_i\): the number of \(i\) with \(a_i\ge m\) is \(h^0(E(-m))-h^0(E(-m-1))\).

Existence, by induction on \(r\). For \(r=1\), let \(E\) have degree \(d\); Riemann–Roch on \(\mathbb P^1\), of genus zero, gives \(h^0(E(-d))\ge1\), and a nonzero section of the degree-zero line bundle \(E(-d)\) has no zeros, so \(E\cong\mathcal O(d)\). By Theorem 2.1 of the lesson on Serre's theorems, \(E(d)\) is globally generated for large \(d\), so there is a nonzero map \(\mathcal O(-d)\to E\). For large \(k\), \(H^0(E(-k))=0\): by Serre duality (Theorem 4.2 of the lesson on dualizing sheaves, with \(\omega_{\mathbb P^1}=\mathcal O(-2)\)), \(h^0(E(-k))=h^1(E^\vee(k-2))\), which vanishes for large \(k\) by Theorem 2.1 of the lesson on Serre's theorems. So the degrees of line subbundles of \(E\) are bounded above, and there are line subbundles; let \(L\cong\mathcal O(a)\) be one of maximal degree. By induction, \(E/L\cong\bigoplus_{i=2}^r\mathcal O(b_i)\).

Each \(b_i\le a\). Indeed, a nonzero section of \(E(-a-1)\) would give a nonzero map \(\mathcal O(a+1)\to E\), and by Lemma 4.1 a line subbundle of degree at least \(a+1\); so \(H^0(E(-a-1))=0\). The sequence \(0\to\mathcal O(-1)\to E(-a-1)\)\(\to(E/L)(-a-1)\to0\) and \(H^1(\mathcal O(-1))=0\) give \(H^0((E/L)(-a-1))=0\), that is, \(b_i-a-1<0\).

The extension \(0\to\mathcal O(a)\to E\to\bigoplus_i\mathcal O(b_i)\to0\) splits: its class lies in \(\operatorname{Ext}^1\bigl(\bigoplus_i\mathcal O(b_i),\mathcal O(a)\bigr)\), which is \(\bigoplus_iH^1(\mathcal O(a-b_i))\) and vanishes because \(a-b_i\ge0\). Explicitly, applying \(H^0\) to the sequence twisted by \(\mathcal O(-b_i)\) shows that the inclusion of each summand \(\mathcal O(b_i)\) lifts to \(E\), since \(H^1(\mathcal O(a-b_i))=0\); the lifts define a splitting. \(\square\)

For a vector bundle \(E\) on \(\mathbb P^1\) with a perfect symmetric pairing \(E\otimes E\to\mathcal O_{\mathbb P^1}\), that is, an isomorphism \(E\cong E^\vee\), the multiset \(\{a_i\}\) equals \(\{-a_i\}\), by uniqueness in Theorem 4.2.

## 5. A perfect trace pairing

Let \(f\) have degree \(n\), let \(u=(u_1,u_2)\) be the pullback of a basis of \(H^0(\mathbb P^1,\mathcal O(1))\), \(H=f^*\mathcal O(1)\), and
\[
\begin{aligned}
\eta_C&=u_1\,du_2-u_2\,du_1\\
&\in H^0(C,K_C+2H),
\end{aligned}
\]
defined as in the lesson on the elliptic curve: in a local frame \(e\) of \(H\) with \(u_i=f_ie\), it is \((f_1\,df_2-f_2\,df_1)\,e^2\). If \(u\) is the pullback of \((X_0,X_1)\), then in the frame \(u_1\) one has \(\eta_C=f^*(dx)\,u_1^2\). So \(\eta_C\) vanishes exactly at the ramification points, to order \(e_p-1\) at \(p\).

**Proposition 5.1 (trace pairing).** Let \(\Lambda\) be a line bundle on \(C\) with an isomorphism \(2\Lambda\cong K_C+2H\). Then
\[
\begin{gathered}
f_*\Lambda\otimes f_*\Lambda\longrightarrow\mathcal O_{\mathbb P^1},\\
(T_1,T_2)\longmapsto\operatorname{Tr}\Bigl(\frac{T_1T_2}{\eta_C}\Bigr),
\end{gathered}
\]
where \(T_1T_2/\eta_C\) is the meromorphic function obtained through the given isomorphism, is a perfect symmetric pairing of vector bundles of rank \(n\).

**Proof.** The pairing is symmetric and \(\mathcal O_{\mathbb P^1}\)-bilinear; it remains to check, near each \(x_0\in\mathbb P^1\), that it takes holomorphic values and has a unit determinant. Use the coordinates of Lemma 1.1 with \(t=x-x_0\) (or \(t=1/x\) at infinity, with the roles of \(u_1,u_2\) exchanged); the pairing is the orthogonal sum of its restrictions to the components \(\Delta_p\). On \(\Delta_p\), with \(e=e_p\) and \(w=w_p\), \(\eta_C=e\,w^{e-1}dw\,u_1^2\) up to the sign of the exchange. Choose a frame \(\tau\) of \(\Lambda\); then \(\tau^2=a(w)\,dw\,u_1^2\) with \(a\) a unit, and for \(T_i=b_i(w)\tau\),
\[
\frac{T_1T_2}{\eta_C}=\frac{a\,b_1b_2}{e\,w^{e-1}} .
\]
The sections of \(f_*\Lambda\) over \(\Delta\) restricted to \(\Delta_p\) form a free module over the holomorphic functions of \(t\), with basis \(w^i\tau\), \(0\le i<e\). For \(a=1\), by (1.1),
\[
\begin{gathered}
\operatorname{Tr}\Bigl(\frac{w^{i}w^{j}}{e\,w^{e-1}}\Bigr)=\frac1e\operatorname{Tr}\bigl(w^{i+j-e+1}\bigr)\\
=\begin{cases}1,&i+j=e-1,\\0,&\text{otherwise},\end{cases}\quad 0\le i,j<e,
\end{gathered}
\]
because \(-e<i+j-e+1<e\). This anti-diagonal matrix has unit determinant. For general \(a\), the pairing is \((b_1,b_2)\mapsto\langle ab_1,b_2\rangle_1\), where \(\langle\ ,\ \rangle_1\) is the pairing with \(a=1\), and multiplication by the unit \(a\) is an automorphism of the free module; so it is again perfect. Its values are holomorphic: for holomorphic \(b_1,b_2\), \(ab_1b_2=\sum_{k\ge0}d_kw^k\), and \(\operatorname{Tr}(w^{k-e+1})/e\) is \(t^{(k-e+1)/e}\) with \((k-e+1)/e\ge0\) when \(e\mid k-e+1\), and zero otherwise. \(\square\)

At a point \(x_0\) that is not a branch value, the fibre of \(f_*\Lambda\) is \(\bigoplus_{p\mapsto x_0}\Lambda_p\), and the pairing is the orthogonal sum of the one-dimensional forms \((T_1,T_2)\mapsto(T_1T_2/\eta_C)(p)\).

## 6. Exercises

**6.1** (easy). Show that \(\operatorname{Tr}(1)=n\) and that \(\operatorname{Tr}(f^*g\cdot h)=g\operatorname{Tr}(h)\) for a function \(g\) on \(\mathbb P^1\).

**6.2** (medium). Deduce from Theorem 2.2 that a nonzero meromorphic function on \(C\) has as many zeros as poles, counted with multiplicity.

**6.3** (medium). Let \(E\) be a vector bundle of rank two on \(\mathbb P^1\) with \(h^0(E)=3\) and \(h^0(E(-1))=1\). Determine \(E\).

**6.4** (medium). For \(f:\mathbb P^1\to\mathbb P^1\), \(x\mapsto x^2\), compute \(f_*\mathcal O_{\mathbb P^1}\) as a sum of line bundles.

**6.5** (medium). In the setting of Proposition 5.1 with \(\Lambda\) and \(n\), show that if \(f_*\Lambda\cong\bigoplus_i\mathcal O(a_i)\), then \(\sum_ia_i=0\), and that \(h^0(C,\Lambda)-h^1(C,\Lambda)=n\).

## 7. Solutions

**6.1.** Multiplication by \(1\) is the identity of a free module of rank \(n\), with trace \(n\). Multiplication by \(f^*g\cdot h\) is \(g\) times multiplication by \(h\), and the trace is linear over the functions on \(\mathbb P^1\).

**6.2.** For a meromorphic function \(h\ne0\) on \(C\), the differential \(dh/h\) has residue \(\operatorname{ord}_p(h)\) at each \(p\): in a coordinate, \(h=w^mv\) with \(v(0)\ne0\), and \(dh/h=m\,dw/w+dv/v\). Theorem 2.2 gives \(\sum_p\operatorname{ord}_p(h)=0\).

**6.3.** Write \(E=\mathcal O(a_1)\oplus\mathcal O(a_2)\), \(a_1\ge a_2\). Then \(\max(a_1+1,0)+\max(a_2+1,0)=3\) and \(\max(a_1,0)+\max(a_2,0)=1\). The second equation gives \(a_1=1\) and \(a_2\le0\), or \(a_1\le0\) which contradicts the first. With \(a_1=1\), the first gives \(\max(a_2+1,0)=1\), so \(a_2=0\). Hence \(E\cong\mathcal O(1)\oplus\mathcal O\).

**6.4.** \(f_*\mathcal O_{\mathbb P^1}\) has rank two and contains \(\mathcal O_{\mathbb P^1}\) (functions pulled back), so it is \(\mathcal O(a_1)\oplus\mathcal O(a_2)\) with \(h^0=h^0(\mathbb P^1,\mathcal O)=1\). Over the chart \(x\ne\infty\), the module is \(\mathbb C[y]\) with \(x=y^2\), free on \(1,y\); over \(x\ne0\) it is free on \(1,y^{-1}\). The section \(y\) of the first chart equals \(x\cdot y^{-1}\), so the second summand is \(\mathcal O(-1)\): \(f_*\mathcal O_{\mathbb P^1}\cong\mathcal O\oplus\mathcal O(-1)\), consistent with \(h^0=1\) and \(h^1=0\).

**6.5.** The pairing identifies \(f_*\Lambda\) with its dual, so the \(a_i\) occur in pairs \(\{a,-a\}\) (Section 4), and \(\sum a_i=0\). Then \(\chi(\mathbb P^1,f_*\Lambda)=\sum_i(a_i+1)=n\), and \(\chi(C,\Lambda)=\chi(\mathbb P^1,f_*\Lambda)\) because \(f\) is finite, so \(H^q(C,\Lambda)=H^q(\mathbb P^1,f_*\Lambda)\) (compute both by the Čech complex of the affine cover pulled back from the two charts of \(\mathbb P^1\)). As a check, Riemann–Roch gives \(\chi(\Lambda)=\deg\Lambda+1-g\), and \(2\deg\Lambda=2g-2+2n\).

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Section 3 uses the trace pairing with its local computation (Lemma 3.1 there), Grothendieck's splitting theorem and residue duality.
