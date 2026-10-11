# Integrating variables and reading formal expansions

Complete companion to [Unit 18](../established-approaches-and-open-problems.html). These are independent educational derivations of familiar finite-dimensional facts. They make no novelty claim. Every integral, coordinate, source, determinant and additive constant used below is specified. None of the three comparisons establishes a Yang–Mills spectral statement.

## G0. Coordinates, units and the elementary Gaussian integral

Let \(p,q\geq1\) be integers. The coordinates \(x\in\mathbb R^p\) and \(y\in\mathbb R^q\) are dimensionless, with the specified reference measures \(dx=\prod_{i=1}^p dx_i\) and \(dy=\prod_{j=1}^qdy_j\). Fix an action unit. The parameter \(\hbar>0\), each entry of the matrices \(A,B,C\), each entry of the source vectors \(J_x,J_y\), and the real number \(S_0\) have action units. Thus every term in the action below has action units and every exponential has a dimensionless exponent. An energy convention instead requires a specified time scale; it is not introduced here.

For completeness, write \(I=\int_{\mathbb R}e^{-t^2/2}\,dt\). This is finite because \(e^{-t^2/2}\leq e^{-|t|/2}\) when \(|t|\geq1\). Tonelli's theorem for the nonnegative product, followed by polar coordinates on disks and monotone convergence, gives


\[
I^2=\int_{\mathbb R^2}e^{-(s^2+t^2)/2}\,ds\,dt
=\int_0^{2\pi}\int_0^\infty e^{-r^2/2}r\,dr\,d\theta=2\pi.
\tag{G0.1}
\]


Since \(I>0\), \(I=\sqrt{2\pi}\). The absolute first and second moments are finite by exponential decay. Oddness gives \(\int t e^{-t^2/2}\,dt=0\). Integration by parts on \([-R,R]\), with \(t e^{-t^2/2}\to0\) at both ends, gives \(\int t^2e^{-t^2/2}\,dt=\sqrt{2\pi}\).

We also recall a direct triangular factorization proof. If a real symmetric positive-definite \(n\times n\) matrix is written as


\[
H=\begin{pmatrix}a&b^T\\b&D\end{pmatrix},
\]


then \(a>0\), and for \(w\ne0\)


\[
w^T(D-bb^T/a)w=(-b^Tw/a,w)^TH(-b^Tw/a,w)>0.
\]


Induction starting with \(n=1\) factors \(D-bb^T/a=R_2^TR_2\), where \(R_2\) is upper triangular with positive diagonal. Then


\[
R=\begin{pmatrix}\sqrt a&b^T/\sqrt a\\0&R_2\end{pmatrix},
\qquad H=R^TR.
\tag{G0.2}
\]


Consequently \(R\) is invertible, \(\det R>0\), and \(\det H=(\det R)^2>0\). With action units on \(H\), fix an arbitrary \(m\in\mathbb R^n\), and let \(z\) range over \(\mathbb R^n\). The substitution


\[
t=R(z-m)/\sqrt\hbar,
\qquad z=m+\sqrt\hbar R^{-1}t,
\qquad dz=\frac{\hbar^{n/2}}{\det R}\,dt
\tag{G0.3}
\]


is a bijection of the indicated Euclidean spaces. The determinant is the absolute Jacobian. Applying G0.1 separately to all coordinates proves


\[
\int_{\mathbb R^n}\exp\!\left[-\frac{(z-m)^TH(z-m)}{2\hbar}\right]dz
=\frac{(2\pi\hbar)^{n/2}}{\sqrt{\det H}}.
\tag{G0.4}
\]


In the probability density obtained by dividing the integrand by G0.4, the mean is \(m\) and the covariance is


\[
\hbar R^{-1}R^{-T}=\hbar H^{-1}.
\tag{G0.5}
\]


Indeed the transformed coordinates \(t_i\) have product density \((2\pi)^{-n/2}e^{-\sum_i t_i^2/2}\). Their means vanish; their diagonal second moments are one; their off-diagonal second moments vanish by the one-dimensional odd integrals. Transforming these moments by G0.3 proves G0.5. The polynomial moments used here are absolutely integrable, so each use of Fubini is valid.

## G1. Eliminate \(y\), keeping all factors

Assume


\[
M=\begin{pmatrix}A&B\\B^T&C\end{pmatrix}>0,
\quad A=A^T\in\mathbb R^{p\times p},\quad C=C^T\in\mathbb R^{q\times q},
\quad B\in\mathbb R^{p\times q},
\tag{G1.1}
\]


where \(>0\) means \(z^TMz>0\) for every nonzero real column \(z\). The source vectors are arbitrary \(J_x\in\mathbb R^p,J_y\in\mathbb R^q\), and


\[
S(x,y)=\frac12x^TAx+x^TBy+\frac12y^TCy-J_x^Tx-J_y^Ty+S_0.
\tag{G1.2}
\]


The principal matrix \(C\) is positive definite because \(y^TCy=(0,y)^TM(0,y)>0\) for \(y\ne0\). Thus it is invertible. Define the exact retained coefficients


\[
K=A-BC^{-1}B^T,\qquad j=J_x-BC^{-1}J_y,
\qquad c=S_0-\frac12J_y^TC^{-1}J_y,
\qquad m_y(x)=C^{-1}(J_y-B^Tx).
\tag{G1.3}
\]


The matrix \(K\) is positive definite: for \(x\ne0\), the vector \((x,-C^{-1}B^Tx)\) is nonzero and its \(M\)-quadratic form is precisely \(x^TKx\). In particular \(K^{-1}\) exists. Direct expansion, retaining the cross term and the complete source square, gives


\[
S(x,y)=\frac12(y-m_y(x))^TC(y-m_y(x))
+\frac12x^TKx-j^Tx+c.
\tag{G1.4}
\]


For clarity, the added \(x\)-dependent term from completing the \(y\)-square is


\[
-\frac12(J_y-B^Tx)^TC^{-1}(J_y-B^Tx)
=-\frac12J_y^TC^{-1}J_y+x^TBC^{-1}J_y
-\frac12x^TBC^{-1}B^Tx.
\tag{G1.5}
\]


Translation \(y\mapsto y-m_y(x)\), for fixed \(x\), is a bijection of \(\mathbb R^q\) with Jacobian one. G0.4 therefore proves the finite positive partial integral


\[
W(x):=\int_{\mathbb R^q}e^{-S(x,y)/\hbar}\,dy
=\frac{(2\pi\hbar)^{q/2}}{\sqrt{\det C}}
\exp\!\left[-\frac{\frac12x^TKx-j^Tx+S_0-\frac12J_y^TC^{-1}J_y}{\hbar}\right].
\tag{G1.6}
\]


Relative to the specified dimensionless Lebesgue measure \(dy\), define the effective action by the equality \(W(x)=e^{-S_{\rm eff}(x)/\hbar}\). It is exactly


\[
S_{\rm eff}(x)=\frac12x^TKx-j^Tx+S_0-\frac12J_y^TC^{-1}J_y
+\frac\hbar2\log\det\!\left(\frac{C}{2\pi\hbar}\right).
\tag{G1.7}
\]


Here \(C/(2\pi\hbar)\) is a dimensionless positive-definite matrix, so its determinant is a positive dimensionless real number. In particular the logarithm is not the logarithm of a dimensional determinant by itself. The last term is exactly \(-\hbar\log((2\pi\hbar)^{q/2}/\sqrt{\det C})\). The reference measure matters: replacing \(dy\) by \(r_y\,dy\), for a dimensionless constant \(r_y>0\), multiplies G1.6 by \(r_y\) and changes G1.7 by \(-\hbar\log r_y\). No such change is made here.

## G2. Determinant, inverse, full partition and probability laws

The linear map


\[
T(x,y)=(x,y+C^{-1}B^Tx),\qquad
T=\begin{pmatrix}I_p&0\\C^{-1}B^T&I_q\end{pmatrix}
\tag{G2.1}
\]


is invertible, with inverse obtained by changing the off-diagonal sign; both determinants are one. Matrix multiplication proves the congruence, its determinant, and its inverse:


\[
M=T^T\begin{pmatrix}K&0\\0&C\end{pmatrix}T,
\qquad \det M=\det C\det K,
\tag{G2.2}
\]



\[
M^{-1}=T^{-1}\begin{pmatrix}K^{-1}&0\\0&C^{-1}\end{pmatrix}T^{-T}
=\begin{pmatrix}
K^{-1}&-K^{-1}BC^{-1}\\
-C^{-1}B^TK^{-1}&C^{-1}+C^{-1}B^TK^{-1}BC^{-1}
\end{pmatrix}.
\tag{G2.3}
\]


These equations prove the exact relation between the full quadratic form and the retained one. Conversely \(C>0\) and \(K>0\) imply \(M>0\) by G2.2, since \(T\) maps a nonzero vector to a nonzero vector. Thus this condition is also sufficient.

Set \(J=(J_x,J_y)^T\), \(z=(x,y)^T\), and


\[
\mu=M^{-1}J,\qquad
\mu_x=K^{-1}j,\qquad
\mu_y=C^{-1}(J_y-B^T\mu_x).
\tag{G2.4}
\]


The last two equations follow from G2.3; equivalently they solve the two original equations \(A\mu_x+B\mu_y=J_x\) and \(B^T\mu_x+C\mu_y=J_y\). Multiplying the inverse in G2.3 by \(J\) on both sides also gives


\[
J^TM^{-1}J=J_y^TC^{-1}J_y+j^TK^{-1}j.
\tag{G2.5}
\]


Indeed the right side expands to


\[
J_x^TK^{-1}J_x-2J_x^TK^{-1}BC^{-1}J_y
+J_y^T(C^{-1}+C^{-1}B^TK^{-1}BC^{-1})J_y,
\]


which is the left side from G2.3. Completing the remaining square, or completing the full original square, gives


\[
S(x,y)=\frac12(z-\mu)^TM(z-\mu)+S_0-\frac12J^TM^{-1}J.
\tag{G2.6}
\]


The full partition integral exists and is


\[
\begin{split}
Z&:=\int_{\mathbb R^p}\int_{\mathbb R^q}e^{-S(x,y)/\hbar}\,dy\,dx\\
&=\frac{(2\pi\hbar)^{(p+q)/2}}{\sqrt{\det M}}
\exp\!\left[-\frac{S_0}{\hbar}+\frac{J^TM^{-1}J}{2\hbar}\right]\\
&=\frac{(2\pi\hbar)^{q/2}}{\sqrt{\det C}}
\frac{(2\pi\hbar)^{p/2}}{\sqrt{\det K}}
\exp\!\left[-\frac{S_0}{\hbar}
+\frac{J_y^TC^{-1}J_y}{2\hbar}+\frac{j^TK^{-1}j}{2\hbar}\right].
\end{split}
\tag{G2.7}
\]


The equality to the finite expression follows from G0.4 and G2.6. Tonelli applies before finiteness because the integrand is nonnegative; the resulting finiteness also justifies Fubini. This addresses the order of integration without any assumption on the signs of \(S_0\) or the sources.

The probability density relative to \(dx\,dy\), obtained by dividing \(e^{-S/\hbar}\) by \(Z\), is


\[
p_{X,Y}(x,y)=\frac{\sqrt{\det M}}{(2\pi\hbar)^{(p+q)/2}}
e^{-(z-\mu)^TM(z-\mu)/(2\hbar)}.
\tag{G2.8}
\]


Its marginal relative to \(dx\) and conditional density relative to \(dy\) are


\[
p_X(x)=\frac{\sqrt{\det K}}{(2\pi\hbar)^{p/2}}
e^{-(x-\mu_x)^TK(x-\mu_x)/(2\hbar)},
\tag{G2.9}
\]



\[
p_{Y\mid X=x}(y)=\frac{\sqrt{\det C}}{(2\pi\hbar)^{q/2}}
e^{-(y-C^{-1}(J_y-B^Tx))^TC(y-C^{-1}(J_y-B^Tx))/(2\hbar)}.
\tag{G2.10}
\]


To prove these are the asserted laws, divide G1.6 by G2.7 and complete the \(x\)-square for G2.9. The quotient of G2.8 by the strictly positive G2.9 equals G2.10 by G1.4. G0.4 makes G2.10 integrate to one for every \(x\). Its coefficients depend continuously on \(x\), so it defines a measurable probability kernel. The exact density identity \(p_{X,Y}=p_Xp_{Y\mid X=x}\), together with Tonelli on measurable rectangles, proves the defining conditional-probability identity. Thus the formula is a conditional version valid at every \(x\), even though conditional versions are generally only determined almost everywhere.

G0.5 now proves


\[
\mathbb E[X]=\mu_x,\quad \operatorname{Cov}(X)=\hbar K^{-1},\qquad
\mathbb E[Y\mid X=x]=C^{-1}(J_y-B^Tx),\quad
\operatorname{Cov}(Y\mid X=x)=\hbar C^{-1}.
\tag{G2.11}
\]


There is also an explicit product-coordinate map. Put


\[
\xi=x-\mu_x,\qquad
\eta=y-\mu_y+C^{-1}B^T(x-\mu_x).
\tag{G2.12}
\]


Its inverse is \(x=\mu_x+\xi, y=\mu_y-C^{-1}B^T\xi+\eta\), and its Jacobian is one by G2.1. The transformed joint density is exactly the product of the centered \(K\) and \(C\) Gaussian densities. Therefore \(\xi,\eta\) are independent, their covariances are respectively \(\hbar K^{-1},\hbar C^{-1}\), and direct multiplication gives every block of the full covariance:


\[
\operatorname{Cov}(X,Y)=\hbar M^{-1}
=\hbar\begin{pmatrix}
K^{-1}&-K^{-1}BC^{-1}\\
-C^{-1}B^TK^{-1}&C^{-1}+C^{-1}B^TK^{-1}BC^{-1}
\end{pmatrix}.
\tag{G2.13}
\]


In G2.13, \(\operatorname{Cov}(X,Y)\) denotes the covariance of the concatenated column \((X,Y)^T\). The cross-covariance block itself is \(-\hbar K^{-1}BC^{-1}\).

## G3. A \(2\times2\) example with both sources present

Take \(p=q=1, \alpha>0\), with \(\alpha\) in action units, and


\[
A=3\alpha,\quad B=\alpha,\quad C=2\alpha,\qquad
S(x,y)=\frac{3\alpha}{2}x^2+\alpha xy+\alpha y^2-J_xx-J_yy+S_0.
\tag{G3.1}
\]


Assume \(J_x\ne0,J_y\ne0\). Here \(C=2\alpha>0\) and \(K=5\alpha/2>0\), proving \(M>0\) by G2.2. All retained quantities are


\[
\begin{gathered}
\det M=5\alpha^2,\qquad
M^{-1}=\frac1{5\alpha}\begin{pmatrix}2&-1\\-1&3\end{pmatrix},\\
j=J_x-\frac{J_y}{2},\qquad c=S_0-\frac{J_y^2}{4\alpha},\qquad
m_y(x)=\frac{J_y}{2\alpha}-\frac x2,\\
\mu_x=\frac{2J_x-J_y}{5\alpha},\qquad
\mu_y=\frac{-J_x+3J_y}{5\alpha}.
\end{gathered}
\tag{G3.2}
\]


The partial and full integrals, with their additive terms, are


\[
W(x)=\sqrt{\frac{\pi\hbar}{\alpha}}
\exp\!\left[-\frac{\frac{5\alpha}{4}x^2-(J_x-J_y/2)x+S_0-J_y^2/(4\alpha)}{\hbar}\right],
\tag{G3.3}
\]



\[
S_{\rm eff}(x)=\frac{5\alpha}{4}x^2-(J_x-J_y/2)x+S_0-\frac{J_y^2}{4\alpha}
+\frac\hbar2\log\frac{\alpha}{\pi\hbar},
\tag{G3.4}
\]



\[
Z=\frac{2\pi\hbar}{\sqrt5\,\alpha}
\exp\!\left[-\frac{S_0}{\hbar}
+\frac{2J_x^2-2J_xJ_y+3J_y^2}{10\alpha\hbar}\right].
\tag{G3.5}
\]


The marginal and conditional densities are explicitly


\[
p_X(x)=\sqrt{\frac{5\alpha}{4\pi\hbar}}
\exp\!\left[-\frac{5\alpha}{4\hbar}(x-\mu_x)^2\right],\qquad
p_{Y\mid X=x}(y)=\sqrt{\frac{\alpha}{\pi\hbar}}
\exp\!\left[-\frac\alpha\hbar\left(y-\frac{J_y}{2\alpha}+\frac x2\right)^2\right].
\tag{G3.6}
\]


Their variances are \(2\hbar/(5\alpha)\) and \(\hbar/(2\alpha)\), respectively. The full covariance is \(\hbar(5\alpha)^{-1}\begin{pmatrix}2&-1\\-1&3\end{pmatrix}\).

For the particular nonzero choices \(J_x=\alpha,J_y=-2\alpha\), the means are \(\mu_x=4/5,\mu_y=-7/5\), the retained source is \(j=2\alpha\), and \(c=S_0-\alpha\). Thus


\[
W(x)=\sqrt{\frac{\pi\hbar}{\alpha}}
e^{-[5\alpha x^2/4-2\alpha x+S_0-\alpha]/\hbar},\qquad
Z=\frac{2\pi\hbar}{\sqrt5\,\alpha}e^{-S_0/\hbar+9\alpha/(5\hbar)}.
\tag{G3.7}
\]


Every expression in G3 follows by substitution into G1–G2; G3.2 also checks directly by multiplying the displayed inverse with the original matrix.

## G4. Elimination in two stages is associative

Let \(x\in\mathbb R^p,u\in\mathbb R^r,v\in\mathbb R^s\), with positive integer dimensions, dimensionless coordinates and the same action-unit convention. Start with the full original data


\[
\mathcal M=\begin{pmatrix}A&B&E\\B^T&C&F\\E^T&F^T&G\end{pmatrix}>0,
\qquad \mathcal J=\begin{pmatrix}J_x\\J_u\\J_v\end{pmatrix},
\tag{G4.1}
\]



\[
\mathcal S(x,u,v)=\frac12x^TAx+x^TBu+x^TEv
+\frac12u^TCu+u^TFv+\frac12v^TGv
-J_x^Tx-J_u^Tu-J_v^Tv+S_0.
\tag{G4.2}
\]


All off-diagonal matrices have the dimensions indicated by their occurrences. Define


\[
\begin{gathered}
\widetilde A=A-EG^{-1}E^T,\qquad
\widetilde B=B-EG^{-1}F^T,\qquad
\widetilde C=C-FG^{-1}F^T,\\
\widetilde J_x=J_x-EG^{-1}J_v,\qquad
\widetilde J_u=J_u-FG^{-1}J_v,\qquad
\widetilde S_0=S_0-\frac12J_v^TG^{-1}J_v.
\end{gathered}
\tag{G4.3}
\]


G1 applied with retained coordinate \((x,u)\) proves \(G>0\) and


\[
\widetilde M=\begin{pmatrix}\widetilde A&\widetilde B\\
\widetilde B^T&\widetilde C\end{pmatrix}>0.
\tag{G4.4}
\]


In particular \(\widetilde C>0\). Eliminating \(v\) first produces precisely the factor \((2\pi\hbar)^{s/2}/\sqrt{\det G}\), the quadratic/source data G4.3–G4.4, and no additional suppressed term. Eliminating \(u\) next gives


\[
\begin{gathered}
K_*=\widetilde A-\widetilde B\widetilde C^{-1}\widetilde B^T>0,\qquad
j_*=\widetilde J_x-\widetilde B\widetilde C^{-1}\widetilde J_u,\\
c_*=S_0-\frac12J_v^TG^{-1}J_v
-\frac12\widetilde J_u^T\widetilde C^{-1}\widetilde J_u,
\end{gathered}
\tag{G4.5}
\]


and hence


\[
\int_{\mathbb R^r}\int_{\mathbb R^s}e^{-\mathcal S(x,u,v)/\hbar}\,dv\,du
=\frac{(2\pi\hbar)^{s/2}}{\sqrt{\det G}}
\frac{(2\pi\hbar)^{r/2}}{\sqrt{\det\widetilde C}}
e^{-[x^TK_*x/2-j_*^Tx+c_*]/\hbar}.
\tag{G4.6}
\]


We now prove exact agreement with a single elimination of \((u,v)\), including its inverse and constants. Put


\[
Q=\begin{pmatrix}C&F\\F^T&G\end{pmatrix},\qquad
H=\begin{pmatrix}B&E\end{pmatrix},\qquad
J_w=\begin{pmatrix}J_u\\J_v\end{pmatrix}.
\tag{G4.7}
\]


The principal matrix \(Q\) is positive definite. Applying G2.2–G2.3 directly gives


\[
\det Q=\det G\det\widetilde C,
\quad
Q^{-1}=\begin{pmatrix}
\widetilde C^{-1}&-\widetilde C^{-1}FG^{-1}\\
-G^{-1}F^T\widetilde C^{-1}&G^{-1}+G^{-1}F^T\widetilde C^{-1}FG^{-1}
\end{pmatrix}.
\tag{G4.8}
\]


Multiplying out this displayed matrix, with the matrices in their original order, proves all three identities


\[
HQ^{-1}H^T=EG^{-1}E^T+\widetilde B\widetilde C^{-1}\widetilde B^T,
\tag{G4.9}
\]



\[
HQ^{-1}J_w=EG^{-1}J_v+\widetilde B\widetilde C^{-1}\widetilde J_u,
\tag{G4.10}
\]



\[
J_w^TQ^{-1}J_w=J_v^TG^{-1}J_v+
\widetilde J_u^T\widetilde C^{-1}\widetilde J_u.
\tag{G4.11}
\]


For example G4.9 expands to 


\[
B\widetilde C^{-1}B^T-B\widetilde C^{-1}FG^{-1}E^T-EG^{-1}F^T\widetilde C^{-1}B^T+EG^{-1}E^T+EG^{-1}F^T\widetilde C^{-1}FG^{-1}E^T
\]


; this is precisely its right side. Replacing the rightmost \(B^T,E^T\) by \(J_u,J_v\) gives G4.10, and replacing the remaining left factors by \(J_u^T,J_v^T\) gives G4.11.

Consequently the single-elimination data are exactly


\[
A-HQ^{-1}H^T=K_*,\qquad J_x-HQ^{-1}J_w=j_*,\qquad
S_0-\frac12J_w^TQ^{-1}J_w=c_*.
\tag{G4.12}
\]


The single determinant prefactor equals the product in G4.6 by G4.8. The additive logarithm in its effective action is exactly


\[
\frac\hbar2\log\det\!\left(\frac{Q}{2\pi\hbar}\right)
=\frac\hbar2\log\det\!\left(\frac{G}{2\pi\hbar}\right)
+\frac\hbar2\log\det\!\left(\frac{\widetilde C}{2\pi\hbar}\right).
\tag{G4.13}
\]


All logarithms have positive dimensionless arguments. Positivity and the ordinary real logarithm justify adding them.

The complete inverse, so also the full source response and covariance, agrees exactly:


\[
\mathcal M^{-1}=\begin{pmatrix}
K_*^{-1}&-K_*^{-1}HQ^{-1}\\
-Q^{-1}H^TK_*^{-1}&Q^{-1}+Q^{-1}H^TK_*^{-1}HQ^{-1}
\end{pmatrix},
\tag{G4.14}
\]


where the bottom-right block is on the original ordered coordinate \((u,v)\) and G4.8 gives each of its internal blocks. To verify that the two stages produce this same inverse by actual maps, define


\[
T_1=\begin{pmatrix}I_p&0&0\\0&I_r&0\\G^{-1}E^T&G^{-1}F^T&I_s\end{pmatrix},\qquad
T_2=\begin{pmatrix}I_p&0&0\\\widetilde C^{-1}\widetilde B^T&I_r&0\\0&0&I_s\end{pmatrix}.
\tag{G4.15}
\]


These have determinant one, with inverses obtained by negating their off-diagonal entries. Multiplication, or the two square completions, gives


\[
\mathcal M=T_1^TT_2^T\operatorname{diag}(K_*,\widetilde C,G)T_2T_1,
\quad
\mathcal M^{-1}=T_1^{-1}T_2^{-1}
\operatorname{diag}(K_*^{-1},\widetilde C^{-1},G^{-1})T_2^{-T}T_1^{-T}.
\tag{G4.16}
\]


Both G4.14 and G4.16 multiply \(\mathcal M\) on either side to the identity, which proves their equality: a left inverse \(U\) and a right inverse \(V\) satisfy \(U=U(\mathcal MV)=(U\mathcal M)V=V\). Thus no covariance block can depend on the elimination grouping. The source identity is also explicit:


\[
\mathcal J^T\mathcal M^{-1}\mathcal J
=J_v^TG^{-1}J_v+\widetilde J_u^T\widetilde C^{-1}\widetilde J_u
+j_*^TK_*^{-1}j_*.
\tag{G4.17}
\]


It follows from G2.5 with \(Q\), followed by G4.11–G4.12. The full determinant is \(\det\mathcal M=\det G\det\widetilde C\det K_*\), so the full partition is


\[
\frac{(2\pi\hbar)^{(p+r+s)/2}}
{\sqrt{\det G\det\widetilde C\det K_*}}
\exp\!\left[-\frac{S_0}{\hbar}+\frac{J_v^TG^{-1}J_v+
\widetilde J_u^T\widetilde C^{-1}\widetilde J_u+j_*^TK_*^{-1}j_*}{2\hbar}\right].
\tag{G4.18}
\]


For fixed \(x\), G0.4 with \(Q\) proves that the integral over \((u,v)\) is finite. Tonelli and then Fubini prove equality of the two iterated orders and the single product-space integral. The full integral over \(x,u,v\) is finite by G0.4 with \(\mathcal M\). For any bounded measurable observable \(O(x,u,v)\), its absolute weighted integral is at most \(\|O\|_\infty\) times G4.18, so Fubini also permits each integration order for expectations. This is the exact measure-theoretic content of associativity here. For more than two eliminated groups, applying this two-group identity successively proves associativity of every parenthesization; each retained matrix remains positive definite by G1. This is a finite-dimensional assertion with the stated Lebesgue measures.

## F. A smooth positive function invisible to its Taylor coefficients

Let \(g\in\mathbb R\) and \(a>0\) be dimensionless. Fix \(E_*>0\) in energy units and define the real energy-valued function


\[
f(g)=\begin{cases}E_*e^{-a/g^2},&g\ne0,\\0,&g=0.\end{cases}
\tag{F.1}
\]


For \(g\ne0\), set \(t=1/g\). Define polynomials recursively by


\[
P_0(t)=1,\qquad P_{n+1}(t)=2at^3P_n(t)-t^2P_n'(t).
\tag{F.2}
\]


The chain and product rules, including \(dt/dg=-t^2\), prove by induction


\[
f^{(n)}(g)=E_*e^{-a/g^2}P_n(1/g)\qquad(g\ne0).
\tag{F.3}
\]


The first values, retaining every term, are


\[
P_1=2at^3,\quad P_2=4a^2t^6-6at^4,\quad
P_3=8a^3t^9-36a^2t^7+24at^5.
\tag{F.4}
\]


For every \(n\geq0\), \(P_n\) has degree \(3n\) and leading coefficient \((2a)^n\): F.2 adds a leading term of degree \(3n+3\), whereas its derivative term has degree at most \(3n+1\), so cancellation at the leading degree cannot occur. This supplies a finite polynomial bound for every derivative away from zero.

Here is the required limit for every real \(m\geq0\):


\[
|g|^{-m}e^{-a/g^2}\longrightarrow0\quad(g\to0).
\tag{F.5}
\]


Put \(u=a/g^2\to+\infty\). The expression is \(a^{-m/2}u^{m/2}e^{-u}\). For an integer \(k>m/2\), the nonnegative exponential series gives \(e^u\geq u^k/k!\) for \(u>0\), and hence


\[
0\leq a^{-m/2}u^{m/2}e^{-u}
\leq a^{-m/2}k!u^{m/2-k}\longrightarrow0.
\]


Define \(D_n(g)=E_*e^{-a/g^2}P_n(1/g)\) for \(g\ne0\) and \(D_n(0)=0\). F.5 applied to the finitely many powers in \(P_n\) proves continuity of \(D_n\) at zero. Moreover \(D_n(g)/g\to0\), again by F.5 with each exponent increased by one; therefore \(D_n\) is differentiable at zero with derivative zero. Away from zero F.2 gives \(D_n'=D_{n+1}\). Since \(D_{n+1}\) is continuous everywhere, \(D_n\in C^1(\mathbb R)\). Induction starting from \(f=D_0\) proves


\[
f\in C^\infty(\mathbb R),\qquad f^{(n)}(0)=0\text{ for every }n\geq0.
\tag{F.6}
\]


At every \(g\ne0\), F.1 is strictly positive. Its Taylor series at zero is the zero series and does not represent \(f\) on any neighborhood of zero. More precisely, for every nonnegative integer \(N\), F.5 gives \(f(g)=o(|g|^N)\). Thus the identically zero function and \(f\) have both the same complete Taylor data and the same zero power-series asymptotic expansion. For any smooth function \(h\) with energy units and any dimensionless constant \(c\), \(h\) and \(h+cf\) have identical Taylor coefficients at zero. This proves a precise ambiguity of formal series without further function-class assumptions. It defines no Hamiltonian, state, spectrum or gap and therefore makes no spectral claim.

## C. An exact weighted identity on a finite circle

The circle is \(\mathbb R/(2\pi\mathbb Z)\), represented by \(0\leq\theta\leq2\pi\) with endpoints identified. The angle and \(\beta\in\mathbb R\) are dimensionless; \(\hbar>0\) has action units; \(D>0\) has units of inverse auxiliary time. Define the periodic action


\[
S(\theta)=\hbar\beta(1-\cos\theta),\qquad
I_0(\beta):=\frac1{2\pi}\int_0^{2\pi}e^{\beta\cos\theta}\,d\theta.
\tag{C.1}
\]


The symbol \(I_0\) is defined by this integral; no special-function theorem is needed. The bounds \(e^{-|\beta|}\leq e^{\beta\cos\theta}\leq e^{|\beta|}\) prove \(0<I_0(\beta)<\infty\). Relative to Lebesgue angle measure, the complete partition factor and probability density are


\[
Z_{S,d\theta}=\int_0^{2\pi}e^{-S(\theta)/\hbar}\,d\theta
=2\pi e^{-\beta}I_0(\beta),\qquad
q(\theta)=\frac{e^{-S(\theta)/\hbar}}{Z_{S,d\theta}}
=\frac{e^{\beta\cos\theta}}{2\pi I_0(\beta)}.
\tag{C.2}
\]


The factor \(e^{-\beta}\) cancels in the probability density but remains in the original partition. If the reference measure is instead \(d\lambda=d\theta/(2\pi)\), the corresponding quantities are \(Z_{S,\lambda}=e^{-\beta}I_0(\beta)\) and \(q_\lambda=e^{\beta\cos\theta}/I_0(\beta)\), with \(q\,d\theta=q_\lambda\,d\lambda\). Both conventions and the map between them are thus explicit.

Let \(C^2_{\rm per}\) be the complex-valued twice continuously differentiable functions on the circle; in interval coordinates, \(f,f',f''\) extend periodically. Define a differential expression \(L:C^2_{\rm per}\to C^0_{\rm per}\) by


\[
Lf=D(f''-\beta\sin\theta\,f').
\tag{C.3}
\]


Differentiation of C.2 gives \(q'=-\beta\sin\theta\,q\). Since \(q>0\), the exact divergence identity is


\[
Lf=Dq^{-1}(qf')'.
\tag{C.4}
\]


For \(f,g\in C^2_{\rm per}\), define


\[
\langle f,g\rangle_q=\int_0^{2\pi}\overline{f(\theta)}g(\theta)q(\theta)\,d\theta
=\frac1{2\pi I_0(\beta)}\int_0^{2\pi}\overline f g\,e^{\beta\cos\theta}\,d\theta.
\tag{C.5}
\]


Integration by parts, with every endpoint contribution displayed, gives


\[
\begin{split}
\langle f,Lg\rangle_q
&=\frac{D}{2\pi I_0(\beta)}
\left[\overline f\,g' e^{\beta\cos\theta}\right]_{0}^{2\pi}
-\frac{D}{2\pi I_0(\beta)}
\int_0^{2\pi}\overline{f'}g'e^{\beta\cos\theta}\,d\theta\\
&=-\frac{D}{2\pi I_0(\beta)}
\int_0^{2\pi}\overline{f'}g'e^{\beta\cos\theta}\,d\theta.
\end{split}
\tag{C.6}
\]


The boundary term vanishes because \(f(0)=f(2\pi)\), \(g'(0)=g'(2\pi)\), and both endpoint exponentials equal \(e^\beta\). Complex conjugation of C.6 with \(f,g\) interchanged proves \(\langle f,Lg\rangle_q=\langle Lf,g\rangle_q\). Taking \(f=1\) proves infinitesimal stationarity,


\[
\int_0^{2\pi}Lg(\theta)q(\theta)\,d\theta=0.
\tag{C.7}
\]


Taking \(g=f\) proves the exact nonnegative identity


\[
\langle f,-Lf\rangle_q
=\frac{D}{2\pi I_0(\beta)}\int_0^{2\pi}|f'(\theta)|^2e^{\beta\cos\theta}\,d\theta
=D\int_0^{2\pi}|f'|^2q\,d\theta\geq0.
\tag{C.8}
\]


Equality holds exactly when \(f\) is constant. To prove the only-if direction, positivity and continuity of the weight and of \(|f'|^2\) imply \(f'=0\) everywhere: if it were nonzero at one point, a neighborhood would contribute a positive integral. The fundamental theorem of calculus on the connected interval then makes \(f\) constant; periodicity identifies the endpoint values.

A second integration-by-parts calculation gives the differential expression on periodic \(C^2\) densities relative to \(d\theta\):


\[
L^*r=D\bigl(r''+\beta(\sin\theta\,r)'\bigr),\qquad
\int_0^{2\pi}(Lf)r\,d\theta=\int_0^{2\pi}f(L^*r)\,d\theta.
\tag{C.9}
\]


Indeed integrating \(f''r\) twice contributes the boundary values \([f'r-fr']_0^{2\pi}\), and integrating \(-\beta\sin\theta f'r\) once contributes \([-\beta\sin\theta fr]_0^{2\pi}\); both vanish by periodicity (and the sine values). The remaining integrand is exactly C.9. The identity \(q'+\beta\sin\theta q=0\) proves \(L^*q=0\).

There is a useful exact strengthening within this differential setting: \(q\) is the only real periodic \(C^2\) function \(r\) with \(L^*r=0\) and \(\int_0^{2\pi}r\,d\theta=1\). To prove it, C.9 and \(D>0\) give \(r'+\beta\sin\theta r=k\), where \(k\) is a real constant. The integrating factor is \(e^{-\beta\cos\theta}\), and


\[
\bigl(e^{-\beta\cos\theta}r\bigr)'=k e^{-\beta\cos\theta}.
\tag{C.10}
\]


Integrating over a period gives \(0=k\int_0^{2\pi}e^{-\beta\cos\theta}\,d\theta\). The integral is strictly positive, so \(k=0\). Then \(r=c e^{\beta\cos\theta}\), and normalization forces \(c=(2\pi I_0(\beta))^{-1}\). This proof even avoids a prior positivity assumption on \(r\); the uniquely normalized solution is positive.

Equations C.3–C.10 concern the explicitly defined differential expressions and test functions. They prove no assertion about existence of a stochastic process, a closed self-adjoint operator, a Markov semigroup, or a spectral gap. Such constructions are not needed for any identity proved here.


The measure, Tonelli and Fubini prerequisites are proved in the [included measure chapter](../analysis-measure-prerequisites.html). These complete finite derivations make no novelty claim.
