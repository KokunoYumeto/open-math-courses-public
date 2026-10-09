# Exact cusp-product multiplicities

Take the three-dimensional analytic space

\[
H=\{(x,z,y_1,y_2,w):z^2=x^3,\ w=0\}\subset\mathbb C^5,
\qquad Y=\{x=z=w=0\}.
\tag{PMF1}
\]

Its normalization is \((t,y_1,y_2)\mapsto(t^2,t^3,y_1,y_2,0)\). The left panel shows only the real section \(y_2=w=0\). The map \(u=(y_1,y_2,x)\) has degree two: at \(x=1/16\) the two points have \(t=\pm1/4\) and \(z=\pm1/64\). They meet over \(x=0\). The horizontal and vertical plotting intervals are display windows, not bounds asserted by the theorem.

The associated graded ring at a point of \(Y\) is \(\mathbb C[x,z,y_1,y_2]/(z^2)\). Every monomial has a unique representative with exponent zero or one in \(z\). Counting monomials of total degree less than \(n\) gives

\[
\operatorname{length}(R/\mathfrak m^n)
=\binom{n+2}{3}+\binom{n+1}{3}
=\frac{n(n+1)(2n+1)}6.
\tag{PMF2}
\]

Thus the plotted normalized lengths are exactly \(2+3/n+1/n^2\) at the integer samples, tending to two. On the general surface section \(y_1=0\), the same count gives \(\binom{n+1}{2}+\binom n2=n^2\), again multiplicity two.

For the higher polar indices, a general projection to three coordinates has full rank on the punctured normalization near the marked stratum, and a general projection to two coordinates is already of full rank on its two parameter directions. Hence the higher polar germs are empty and \((m_0,m_1,m_2)=(2,0,0)\) along \(Y\). [MD0–MD4, GM3–GM5 and EQ3–EQ6](../polar-multiplicity-in-sections.html) prove the three general mechanisms illustrated here. 

Mathematical antecedents: Teissier, [*Variétés polaires II*](https://webusers.imj-prg.fr/~bernard.teissier/documents/VarPol2.pdf), IV.6.2.1 and V.1.2. Figure and calculation: CC0 1.0.
