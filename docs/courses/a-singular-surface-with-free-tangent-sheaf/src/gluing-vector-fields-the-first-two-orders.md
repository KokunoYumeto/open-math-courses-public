# Gluing vector fields: the first two orders

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The singular surface is obtained by contracting the curve \(C\) of genus 21 in a surface \(Y\) that contains it with self-intersection \(-10\). The surface \(Y\) is built from the total space of the line bundle \(L^{-1}\) by changing how a neighbourhood of each marked point \(q_j\) is glued to the rest. The aim is to make room for two vector fields \(v_1,v_2\) tangent to \(C\), vanishing along it, whose wedge vanishes to order exactly five along \(C\). This lesson sets up the coordinates, the vector fields and the gluing changes, and carries out the construction through the first two orders in the distance to \(C\). The second order contains the one genuine obstruction; the residue data of the preceding lesson make it vanish. The next lesson continues to all orders needed.

**Prerequisites.** [*The trace form and the residue data*](the-trace-form-and-the-residue-data.md), Proposition 3.2 and equation (3.2), with the notation there; [*Traces, residues and vector bundles on the projective line*](traces-residues-and-vector-bundles-on-the-projective-line.md), Theorem 2.2 and Proposition 3.2; [*A curve of genus 21 with a fourth root of its canonical bundle*](a-curve-of-genus-21-with-a-fourth-root-of-its-canonical-bundle.md), Proposition 3.3. From AG-QC: [*Affine cohomology and Serre's criterion*](course:AG-QC/affine-cohomology-and-serres-criterion) (vanishing of higher cohomology of quasi-coherent sheaves on affine schemes). From *Complex analytic spaces and coherent sheaves*: [*Holomorphic functions of several variables*](course:complex-analytic-spaces-and-coherent-sheaves/holomorphic-functions-of-several-variables) for power series in two variables. Existence and uniqueness of flows of holomorphic vector fields.

For rows \(X=(X_1,X_2)\), \(Y=(Y_1,Y_2)\) put \(X\wedge Y=X_1Y_2-X_2Y_1\), and \(\epsilon_{12}=1\), \(\epsilon_{21}=-1\), \(\epsilon_{11}=\epsilon_{22}=0\).

## 1. Coordinates, orders and the fields

Let \(Y_0\) be the total space of \(L^{-1}\), with projection \(\pi:Y_0\to C\) and zero section \(C\); the conormal bundle of \(C\) in \(Y_0\) is \(L\), and \(C\cdot C=-\deg L=-10\). A local frame \(\ell\) of \(L\) is the same as a fibre-linear function \(t\) on \(Y_0\) vanishing exactly on the zero section. A pair \((z,t)\) of a coordinate \(z\) on an open set of \(C\) and such a function is a *split chart*; it is *compatible* if \(\ell^4\) corresponds to \(dz\) under \(L^4\cong K_C\). Compatible charts exist near every point, by taking a fourth root of a unit, and two compatible charts are related by
\[
\begin{gathered}
\widetilde z=\psi(z),\qquad \widetilde t=g(z)\,t,\\
g^4=\psi' .
\end{gathered}
\tag{1.1}
\]
Write \(E_t=t\,\partial_t\) and \(a=g'/g\). In the new chart \(\widetilde E_t=E_t\) and \(\partial_z=\psi'\partial_{\widetilde z}+a\,\widetilde E_t\). The meromorphic two-form
\[
\sigma=t^{-5}\,dt\wedge dz
\]
is the same in all compatible charts, since
\[
\begin{aligned}
\widetilde t^{-5}d\widetilde t\wedge d\widetilde z&=g^{-5}t^{-5}\,g\,dt\wedge\psi'dz\\
&=t^{-5}dt\wedge dz .
\end{aligned}
\]

**Homogeneous terms.** The group \(\mathbb C^*\) acts on \(Y_0\) by scaling the fibres. A vector field on \(\pi^{-1}(U)\), \(U\subset C\) open, is *homogeneous of index \(k\)* if, in a split chart, it has the form
\[
t^{k+1}\bigl(A_k\,E_t+B_k\,\partial_z\bigr)
\]
with functions \(A_k,B_k\) of \(z\); such a field is tangent to \(C\) and vanishes along it to order \(k+1\). Under (1.1),
\[
\begin{gathered}
\widetilde A_k=g^{-(k+1)}(A_k+aB_k),\\
\widetilde B_k=g^{-(k+1)}\psi'B_k=g^{3-k}B_k .\qquad(1.2)
\end{gathered}
\]
So \(B_k\) is the coefficient of a section of \(L^{k+1}\otimes T_C\cong L^{k-3}\), and when \(B_k=0\), \(A_k\) is the coefficient of a section of \(L^{k+1}\). The homogeneous fields of index \(k\) are the sections of an algebraic vector bundle \(\mathcal E_k\) of rank two on \(C\), the weight-\((k+1)\) part of \(\pi_*\) of the logarithmic tangent sheaf of \(Y_0\) along \(C\), and there is an exact sequence
\[
0\to L^{k+1}\to\mathcal E_k\to L^{k-3}\to0,\qquad(1.3)
\]
where the first map is \(A\mapsto t^{k+1}AE_t\) and the second takes the horizontal coefficient \(B_k\). The splitting given by a split chart depends on the chart, through the term \(aB_k\) in (1.2).

**The cover.** Let \(U_0=C\setminus Z\), an affine curve, since \(Z\) is a divisor of positive degree on the projective curve \(C\) and a suitable multiple of it is very ample. Let \(U_1,\ldots,U_6\) be disjoint discs around \(q_1,\ldots,q_6\), each with a compatible chart \((z,t)=(z_j,t_j)\) centred at \(q_j\), the one used in the preceding lesson. The *annuli* \(U_0\cap U_j=U_j\setminus\{q_j\}\) are punctured discs. On \(\pi^{-1}(U_0)\) we work with algebraic data: sections over \(U_0\) of the bundles \(L^m\) and \(\mathcal E_k\). In the chart of \(U_j\), such a section has coefficients that are meromorphic at \(q_j\), since it is a rational section on \(C\) regular on \(U_0\). On \(\pi^{-1}(U_j)\) we work with holomorphic coefficients on the disc.

Since \(U_0\) is affine, every section of \(L^{k-3}\) over \(U_0\) lifts to a section of \(\mathcal E_k\) over \(U_0\), and two lifts differ by a section of \(L^{k+1}\) (Affine cohomology lesson: \(H^1(U_0,L^{k+1})=0\)).

**The fields.** On each chart we seek two vector fields, written as rows,
\[
\begin{gathered}
v=t\bigl(A(t,z)E_t+B(t,z)\partial_z\bigr),\\
A=\sum_{k\ge0}A_kt^k,\quad B=\sum_{k\ge0}B_kt^k,\\
A_0=r,\quad B_0=0,\qquad(1.4)
\end{gathered}
\]
where \(r=\xi u\) is the basis of \(H^0(C,L)\) with common zero divisor \(Z\). Subscripts \(k\) are orders; the two entries of a row are the two fields. In the chart,
\[
\begin{gathered}
\sigma(v_1,v_2)=t^{-2}(A\wedge B),\\
v_1\wedge v_2=t^2(A\wedge B)\,E_t\wedge\partial_z .\qquad(1.5)
\end{gathered}
\]
Indeed, \(v_i=t^2A_i\partial_t+tB_i\partial_z\), and \(dt\wedge dz(v_1,v_2)=t^3(A\wedge B)\). The goal is \(A\wedge B=t^2(1+O(t))\), so that
\[
\begin{aligned}
v_1\wedge v_2&=t^4(1+O(t))E_t\wedge\partial_z\\
&=t^5(1+O(t))\,\partial_t\wedge\partial_z .
\end{aligned}
\]

## 2. Changing the gluing

On the annulus \(U_0\cap U_j\) the two charts are compared through the split identification of \(\pi^{-1}(U_0\cap U_j)\). We modify this identification by time-one flows of vector fields
\[
\begin{gathered}
D=t^k\bigl(b\,E_t+h\,\partial_z\bigr),\\
k\ge1,
\end{gathered}
\tag{2.1}
\]
with \(b,h\) holomorphic on the annulus, in the disc coordinate; in all applications they are meromorphic at \(q_j\). The time-one flow of \(-D\) acts on vector fields by \(\exp(\operatorname{ad}D)\), where \(\operatorname{ad}D(V)=[D,V]\): if \(\phi_s\) is the flow of \(D\), then \(\frac{d}{ds}\phi_s^*V=\phi_s^*[D,V]\), so \(\phi_1^*V=\exp(\operatorname{ad}D)V\) as formal series. Since \(\operatorname{ad}D\) raises the index by \(k\), only finitely many terms contribute through any given index. On a compact subannulus, \(D\) is holomorphic near the zero section and vanishes there, so its time-one flow and the inverse exist on a neighbourhood of the zero section over the subannulus. The flow fixes \(C\) pointwise and changes \(t\) by \(t\mapsto t+O(t^{k+1})\), so \(C\) and its conormal bundle \(L\) are preserved. Successive modifications are composed, and all formulas are written in the disc chart on the annulus; there are no triple overlaps, since the discs are disjoint.

**Lemma 2.1 (brackets).** For \(D\) as in (2.1) and \(V=t^{\ell+1}(AE_t+B\partial_z)\), with primes denoting \(z\)-derivatives,
\[
\begin{aligned}
&[D,V]=t^{k+\ell+1}\Bigl(\bigl((\ell+1-k)bA\\
&\quad+hA'-Bb'\bigr)E_t+\bigl((\ell+1)bB\\
&\quad+hB'-khA-Bh'\bigr)\partial_z\Bigr).
\end{aligned}
\]
Moreover \(\mathcal L_D\sigma=t^k\bigl((k-4)b+h'\bigr)\sigma\); for \(k\ne4\), the choice \(b=h'/(4-k)\) preserves \(\sigma\). The leading action of \(D\) on the fields (1.4) is
\[
\begin{gathered}
\Delta A_k=(1-k)\,b\,r+h\,r',\\
\Delta B_k=-k\,h\,r .
\end{gathered}
\tag{2.2}
\]

**Proof.** Use \(E_t(t^c)=ct^c\), \([E_t,\partial_z]=0\), and expand both components. For the divergence, the coefficient of \(dt\wedge dz\) in \(\sigma\) is \(t^{-5}\), so
\[
\begin{aligned}
&\operatorname{div}_\sigma D\\
&=t^5\bigl(\partial_t(t^{k-4}b)+\partial_z(t^{k-5}h)\bigr)\\
&=t^k\bigl((k-4)b+h'\bigr).
\end{aligned}
\]
For (2.2), take \(\ell=0\), \(A=r\), \(B=0\). \(\square\)

The check script of this course verifies the bracket, the divergence and (2.2) for arbitrary functions \(b,h,A,B\) and symbolic \(k,\ell\).

**Lemma 2.2 (splitting along the marked points).** Let \(\mathcal B\) be a line bundle on \(C\), and for each \(j\) let \(c_j\) be a section of \(\mathcal B\) on the annulus \(U_0\cap U_j\), meromorphic at \(q_j\). There are a section \(a\) of \(\mathcal B\) over \(U_0\) and holomorphic sections \(a_j\) over \(U_j\) with \(c_j=a_j-a\) on every annulus if and only if
\[
\begin{gathered}
\sum_{j=1}^6\operatorname{Res}_{q_j}(c_j\,s)=0\\
\text{for every }s\in H^0(C,K_C-\mathcal B).
\end{gathered}
\]
The section \(a\) is then a rational section regular on \(U_0\).

**Proof.** Suppose \(a\) and \(a_j\) exist. For \(s\in H^0(K_C-\mathcal B)\), \(as\) is a meromorphic differential on \(C\) with poles only on \(Z\), so \(\sum_j\operatorname{Res}_{q_j}(as)=0\) by the residue theorem, and \(\operatorname{Res}_{q_j}(a_js)=0\); hence \(\sum_j\operatorname{Res}_{q_j}(c_js)=0\). Conversely, choose \(n\) so that every \(c_j\) has a pole of order at most \(n\), and let \(\mathrm{pp}\in\mathrm{PP}_{nZ}(\mathcal B)\) be the family of principal parts of the \(-c_j\). The hypothesis says that \(\mathrm{pp}\) annihilates the jets of all sections of \(K_C-\mathcal B\), so by Proposition 3.2 of the lesson on traces there is \(a\in H^0(C,\mathcal B(nZ))\) with principal parts \(\mathrm{pp}\). Then \(a_j=a+c_j\) has no principal part at \(q_j\), so it extends holomorphically over \(q_j\). \(\square\)

## 3. The first order

On the disc \(U_j\), with the compatible coordinate of the preceding lesson and its data \(c=c_j\), \(m=c/z\), \(R=mr=cu\) and \(p=P-mr'\), choose the order-one rows as follows, and use the order-one modification on the annulus with
\[
h=m,\qquad b=\tfrac13m' :
\]
\[
\begin{array}{c|cc}
&A_1&B_1\\\hline
U_j&p&m\,r\\
U_0&P&0
\end{array}
\tag{3.1}
\]
On the disc, \(mr=cu\) and \(p\) are holomorphic (Proposition 3.2 of the preceding lesson). On \(U_0\), \(P\) is a pair of sections of \(\theta=L^2\), the type of \(A_1\) when \(B_1=0\). By (2.2) with \(k=1\), the modification adds \((mr',-mr)\) to the inside rows at index one, giving \((p+mr',0)=(P,0)\): the rows match at index one. The modification preserves \(\sigma\), since \(b=h'/3\). The coefficient of \(t\) in \(A\wedge B\) is \(r\wedge B_1\), which is \(r\wedge mr=0\) inside and \(0\) outside.

## 4. The second order

**Horizontal rows.** Write \(U=B_2\). The coefficient of \(t^2\) in \(A\wedge B\) must be \(1\):
\[
r\wedge U=1-A_1\wedge B_1 .
\tag{4.1}
\]
On \(U_0\), the right side is \(1\). The row \(u\) generates \(H\) at every point, and \(\xi\) is invertible on \(U_0\); since \(U_0\) is affine, there is a row \(w\) of sections of \(L^{-1}\) over \(U_0\) with \(r\wedge w=1\) (the map \((x,y)\mapsto r_1y-r_2x\) from \((L^{-1})^{\oplus2}\) onto \(\mathcal O\) is surjective on \(U_0\), and its kernel has no first cohomology there), and \(U=w\) solves (4.1). On the disc, \(r=z\rho\) with \(\rho=u\) nowhere zero after shrinking, and the right side is
\[
1-p\wedge mr=1-c\,(p\wedge u),
\]
which vanishes at \(z=0\) because \(c\,(p\wedge u)(0)=p(0)\wedge R(0)=1\). So (4.1) becomes \(\rho\wedge U=(1-c\,p\wedge u)/z\), with holomorphic right side, solvable because \(\rho\) is nowhere zero.

After the order-one modification, the inside and outside fields agree at index \(\le1\), and both satisfy (4.1); the modification preserves \(\sigma\), so the transported inside fields still have \(\sigma(v_1,v_2)=1+O(t)\). The coefficient of \(t^2\) in \(A\wedge B\) is \(r\wedge B_2+A_1\wedge B_1=r\wedge B_2\) on both sides, so the transported inside row and the outside row \(U\) differ by a row \(\varphi r\), with \(\varphi\) holomorphic on the annulus and meromorphic at \(q_j\), since \(r\) has no zero on the annulus. An order-two modification with \(h=\varphi/2\) and \(b=h'/2\), which preserves \(\sigma\), removes it, since its horizontal effect is \(-2hr\) by (2.2). The outside row \(U\) stays fixed.

**Vertical rows.** After the horizontal rows match, the vertical rows at index two differ on each annulus by a row \(\delta_j\) of sections of \(L^3\), meromorphic at \(q_j\) (difference of two lifts in (1.3) with the same horizontal coefficient). By Lemma 2.2, changing the vertical lifts on \(U_0\) and on the discs makes them match if and only if
\[
\sum_{j=1}^6\operatorname{Res}_{q_j}\bigl(r_i\,\delta_{j,\iota}\bigr)=0\qquad(i,\iota\in\{1,2\}),
\]
since \(H^0(K_C-L^3)=H^0(C,L)\) has basis \(r_1,r_2\); here \(\delta_{j,\iota}\) is the \(\iota\)-th entry, and \(r_i\delta_{j,\iota}\) is a section of \(L^4=K_C\), written \(r_i\delta_{j,\iota}\,dz\) in the compatible chart.

**Lemma 4.1 (the second-order obstruction vanishes).** These four sums are zero.

**Proof.** Write \(D^{(2)}=A_2\) for the vertical row at index two (this is not a modification). For \(i,\iota\in\{1,2\}\) set
\[
\Psi_{i\iota}=\Bigl(r_iD^{(2)}_\iota+\tfrac14r_i'U_\iota+\tfrac34r_\iota'U_i\Bigr)dz .
\]
Once the horizontal rows match, the difference of \(\Psi_{i\iota}\) computed with the transported inside rows and with the outside rows is \(r_i\delta_{\iota}\,dz\). So it suffices to show that \(\sum_{q\in Z}\operatorname{Res}_q\Psi_{i\iota}\) is the same for both.

*The outside total.* Under a change (1.1) of compatible chart, (1.2) gives \(\widetilde r_i=g^{-1}r_i\), \(d\widetilde r_i/d\widetilde z=g^{-5}(r_i'-ar_i)\), \(\widetilde U_i=gU_i\) and \(\widetilde D^{(2)}_i=g^{-3}(D^{(2)}_i+aU_i)\). Substituting and using \(d\widetilde z=g^4dz\),
\[
\begin{aligned}
\widetilde\Psi_{i\iota}-\Psi_{i\iota}&=\tfrac34\,(r_iU_\iota-r_\iota U_i)\,\frac{dg}{g}\\
&=\tfrac34\,\epsilon_{i\iota}\,(r\wedge U)\,\frac{dg}{g}.
\end{aligned}
\]
On \(U_0\), \(r\wedge U=1\). The coefficient of the section \(r_1\) of \(L\) changes by \(\widetilde r_1=g^{-1}r_1\), so \(\Psi_{i\iota}+\frac34\epsilon_{i\iota}\,dr_1/r_1\) is a differential on \(U_0\) independent of the chart. It is meromorphic on \(C\): at \(Z\), because the outside data are rational, and on \(U_0\) its only poles are those of \(dr_1/r_1\), simple with residue \(\frac34\epsilon_{i\iota}\) at the four zeros of \(u_1\). At each \(q\in Z\), \(r_1=\xi u_1\) has a simple zero, so \(\operatorname{Res}_q(dr_1/r_1)=1\). The residue theorem (Theorem 2.2 of the lesson on traces) gives
\[
\begin{aligned}
\sum_{q\in Z}\operatorname{Res}_q\Psi^{\mathrm{out}}_{i\iota}&=-\tfrac34\epsilon_{i\iota}\,(6+4)\\
&=-\tfrac34\epsilon_{i\iota}\deg L .\qquad(4.2)
\end{aligned}
\]

*The transported inside total.* Before transport, \(\Psi_{i\iota}\) is holomorphic on the disc, with residue zero. The order-two modification changes the rows at index two by its action on \(trE_t\), namely \(\delta D^{(2)}=hr'-\tfrac12h'r\) and \(\delta U=-2hr\) by Lemma 2.1; this changes \(\Psi_{i\iota}\) by the exact differential \(-\tfrac12\,d(h\,r_ir_\iota)\), with residue zero. The order-one modification \(D=t(\tfrac13m'E_t+m\partial_z)\) acts through \(\exp(\operatorname{ad}D)\). Its index-two effect comes from \([D,t^2(pE_t+mr\partial_z)]\) and from \(\tfrac12[D,[D,trE_t]]\); by Lemma 2.1,
\[
\begin{aligned}
\Delta A_2&=\tfrac13m'p+mp'+\tfrac23mm'r'\\
&\quad+\tfrac12m^2r''-\tfrac16mm''r,\\
\Delta U&=-mp+\tfrac13mm'r .\qquad(4.3)
\end{aligned}
\]
Substitute \(m=c/z\) and \(r=zR/c\):
\[
\begin{aligned}
\Delta A_2&=-\frac{cR}{z^3}+\frac{cR'}{3z^2}+\frac{cR''}{2z}\\
&\quad-\frac{cp}{3z^2}+\frac{cp'}{z},\\
\Delta U&=-\frac{cp}{z}-\frac{cR}{3z^2}.
\end{aligned}
\]
Expanding \(R\) and \(p\) in Taylor series, with all coefficients on the right evaluated at \(0\),
\[
\begin{aligned}
F_{i\iota}&:=\operatorname{Res}_0(r_i\Delta A_{2,\iota}\,dz)\\
&=-\tfrac13R_ip_\iota-\tfrac23R_iR_\iota'-R_i'R_\iota,\\
H_{i\iota}&:=\operatorname{Res}_0(r_i'\Delta U_\iota\,dz)\\
&=-R_ip_\iota-\tfrac13R_iR_\iota'-\tfrac23R_i'R_\iota .
\end{aligned}
\]
For example, \(r_i\Delta A_{2,\iota}\) contains \(-R_iR_\iota/z^2\), whose residue \(-R_i'R_\iota-R_iR_\iota'\) accounts for both derivative terms of the second kind. Hence the residue at \(q_j\) of the change of \(\Psi_{i\iota}\) is
\[
\begin{aligned}
T_{i\iota}&=F_{i\iota}+\tfrac14H_{i\iota}+\tfrac34H_{\iota i}\\
&=-\tfrac7{12}R_ip_\iota-\tfrac9{12}R_\iota p_i\\
&\quad-\tfrac54R_iR_\iota'-\tfrac{17}{12}R_i'R_\iota .
\end{aligned}
\]
Its symmetric and alternating parts are
\[
\begin{aligned}
\tfrac12(T_{i\iota}+T_{\iota i})&=-\tfrac23\bigl(R_ip_\iota+R_\iota p_i\\
&\qquad+2R_iR_\iota'+2R_i'R_\iota\bigr),\\
\tfrac12(T_{i\iota}-T_{\iota i})&=\tfrac1{12}\epsilon_{i\iota}\bigl((R\wedge p)(0)\\
&\qquad+(R\wedge R')(0)\bigr).
\end{aligned}
\]
By (3.2) of the preceding lesson, \(P=R(0)/z+p(0)+2R'(0)+O(z)\), and \(P_iP_\iota\) is a meromorphic section of \(L^4=K_C\) with poles only on \(Z\); its residue at \(q_j\) is \(R_ip_\iota+R_\iota p_i+2R_iR_\iota'+2R_i'R_\iota\). By the residue theorem, the symmetric parts sum to zero over the six points. By Proposition 3.2(3) of the preceding lesson, \((R\wedge p)(0)=-1\) and \((R\wedge R')(0)=W_j\), so the alternating parts sum to
\[
\tfrac1{12}\epsilon_{i\iota}\sum_{j=1}^6(W_j-1)=-\tfrac34\epsilon_{i\iota}\deg L .
\]
So \(\sum_{q\in Z}\operatorname{Res}_q\Psi^{\mathrm{in}}_{i\iota}=-\tfrac34\epsilon_{i\iota}\deg L\), equal to (4.2) for all four pairs \((i,\iota)\). \(\square\)

The check script of this course verifies (4.3) as the index-two part of \(\exp(\operatorname{ad}D)\), the residues \(F\), \(H\), the matrix \(T\), its two parts, the residue of \(P_iP_\iota\), the transformation law of \(\Psi\) and the exactness of the order-two change, for generic Taylor coefficients.

By Lemmas 2.2 and 4.1, holomorphic vertical corrections on the discs and an algebraic correction on \(U_0\) make the rows match through index two. Both modifications used so far preserve \(\sigma\), and on every chart
\[
A\wedge B=t^2+O(t^3).
\]

## 5. Exercises

**5.1** (easy). Verify (1.2) from \(\partial_z=\psi'\partial_{\widetilde z}+aE_t\) and \(E_t=\widetilde E_t\).

**5.2** (easy). Show that a modification (2.1) with \(k\ge1\) fixes every point of \(C\) and induces the identity on the conormal bundle \(L\).

**5.3** (medium). Show that the order-one modification of Section 3 cannot be replaced by one with \(b=0\) without changing \(\sigma\), and compute \(\mathcal L_D\sigma\) for \(D=t\,m\,\partial_z\).

**5.4** (medium). Show that Lemma 2.2 with \(\mathcal B=L^3\) needs exactly the two sections \(r_1,r_2\), that is, \(h^0(C,K_C-L^3)=2\).

**5.5** (hard). Suppose the residue data satisfied \(\sum_j(W_j-1)=-9\deg L+12\) instead. Which of the four sums in Lemma 4.1 would fail, and by how much?

## 6. Solutions

**5.1.**
\[
\begin{aligned}
&t^{k+1}(A_kE_t+B_k\partial_z)\\
&\quad=t^{k+1}\bigl((A_k+aB_k)\widetilde E_t+\psi'B_k\partial_{\widetilde z}\bigr),
\end{aligned}
\]
and \(t^{k+1}=g^{-(k+1)}\widetilde t^{k+1}\). With \(\psi'=g^4\), \(g^{-(k+1)}\psi'=g^{3-k}\).

**5.2.** \(D=t^{k+1}b\,\partial_t+t^kh\,\partial_z\) vanishes on \(t=0\), so its flow fixes \(C\) pointwise. Along the flow, \(\dot t=t^{k+1}b\), so \(t\circ\phi_1=t+O(t^{k+1})\) and the differential of \(t\) along \(C\) is unchanged; this is the identity on the conormal bundle.

**5.3.** By Lemma 2.1 with \(k=1\), \(\mathcal L_D\sigma=t(-3b+h')\sigma\), which vanishes only for \(b=h'/3\). For \(D=tm\,\partial_z\), \(\mathcal L_D\sigma=t\,m'\sigma\), nonzero since \(m=c/z\).

**5.4.** \(K_C-L^3=L\), and \(h^0(C,L)=2\) by Proposition 3.3(3) of the lesson on the curve of genus 21.

**5.5.** The outside totals (4.2) do not involve the residue data. The inside alternating parts would sum to \(\frac1{12}\epsilon_{i\iota}(-9\deg L+12)\), that is \(-\frac34\epsilon_{i\iota}\deg L+\epsilon_{i\iota}\). The symmetric sums are unchanged. So the sums for \((1,2)\) and \((2,1)\) would be \(+1\) and \(-1\) instead of zero, while \((1,1)\) and \((2,2)\) would still vanish: the obstruction would be a nonzero class, and the vertical rows could not be matched.

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Section 4: coordinates, transitions and the first two orders. There the outside chart is treated analytically, using that \(C\setminus Z\) is Stein; here the outside data are algebraic over the affine curve \(C\setminus Z\), which keeps every cocycle meromorphic at the marked points and reduces the splitting problems to Proposition 3.2 of the lesson on traces.
