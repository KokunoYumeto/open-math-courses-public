# Gluing vector fields: higher orders and the determinant

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The preceding lesson matched the two vector fields through order two, with \(A\wedge B=t^2+O(t^3)\) on every chart. This lesson continues the matching through order seven. From order three on, each step must extend the fields and also the determinant they are required to have, because the gluing changes of order four and higher do not preserve the two-form \(\sigma\). The output, Proposition 3.1, is the finite jet that the next lesson lifts to actual vector fields on a surface.

**Prerequisites.** [*Gluing vector fields: the first two orders*](gluing-vector-fields-the-first-two-orders.md), with its notation: the cover \(U_0=C\setminus Z\), \(U_1,\ldots,U_6\); compatible charts; the bundles \(\mathcal E_k\) and the sequence (1.3); the modifications (2.1), Lemma 2.1 and the splitting Lemma 2.2. [*A curve of genus 21 with a fourth root of its canonical bundle*](a-curve-of-genus-21-with-a-fourth-root-of-its-canonical-bundle.md), Proposition 3.3(4) and Corollary 3.4(2).

## 1. Determinant targets

On each chart we impose
\[
\begin{gathered}
A\wedge B=t^2G,\\
G=1+G_1t+G_2t^2+\cdots,\qquad(1.1)
\end{gathered}
\]
for a *target* \(G\) chosen order by order. By (1.5) of the preceding lesson, (1.1) says \(v_1\wedge v_2=G\,\sigma^{-1}\), where \(\sigma^{-1}=t^5\partial_t\wedge\partial_z\) is the bivector dual to \(\sigma\). So the target is the bivector \(G\sigma^{-1}\), and the coefficient \(G_k\) is the coefficient of a section of \(L^k\): \(\sigma\) is invariant under the changes (1.1) of the preceding lesson, and \(\widetilde t=gt\) changes \(G_k\) into \(g^{-k}G_k\).

A modification \(D\) transports fields by \(\exp(\operatorname{ad}D)\), and bivectors in the same way. With \(q=\operatorname{div}_\sigma D=t^k((k-4)b+h')\) from Lemma 2.1 there, the Lie derivative is
\[
\begin{aligned}
&\mathcal L_D(G\sigma^{-1})\\
&\quad=\bigl(D(G)-qG\bigr)\sigma^{-1},
\end{aligned}
\tag{1.2}
\]
since \(\mathcal L_D\sigma^{-1}=-q\sigma^{-1}\). So transport replaces \(G\) by \(\exp(D-q)G\), where \(D-q\) is the operator \(f\mapsto D(f)-qf\). A modification of order \(k\) changes a target \(1+O(t)\) first in degree \(k\), by \(-((k-4)b+h')\). Modifications that preserve \(\sigma\) and act on \(G=1\) leave it equal to \(1\).

**Compatibility.** Targets are *compatible through degree \(n\)* if the transported inside target and the outside target agree on every annulus modulo \(t^{n+1}\). If the fields on both charts satisfy (1.1) through degree \(k\) of \(A\wedge B\), match at all indices below \(k\), and the targets are compatible through degree \(k-2\), then the coefficients of \(t^k\) in \(A\wedge B\) agree on the annuli after transport; indeed transport preserves orders of vanishing along \(C\) and carries \(v_1\wedge v_2-G\sigma^{-1}\) to the corresponding difference. Since \(B_0=0\) and the rows agree at indices below \(k\), the difference of these coefficients is \(r\wedge\delta B_k\), where \(\delta B_k\) is the difference of the horizontal rows at index \(k\).

**The order of the choices.** Because of the factor \(t^2\) in (1.1) and \(B_0=0\), changes of the fields at step \(k\) first affect the determinant equations of the following degrees in \(A\wedge B\), with the target coefficients they use:
\[
\begin{array}{c|c|c}
\text{change}&\text{degree}&\text{target}\\\hline
A_{k-1}\ (\text{global})&k&G_{k-2}\\
B_k&k&G_{k-2}\\
A_k&k+1&G_{k-1}
\end{array}
\]
A target coefficient \(G_k\) is chosen only after the fields match through index \(k\); its equation is imposed at degree \(k+2\).

**The invariant.** After step \(n\ge2\): the rows match through index \(n\); (1.1) holds through degree \(n\) of \(A\wedge B\) on every chart; and \(G_0=1,G_1,\ldots,G_n\) are chosen, holomorphic on the discs and algebraic on \(U_0\), and compatible through degree \(n\). The preceding lesson establishes it for \(n=2\) with \(G=1\): both modifications used there preserve \(\sigma\).

## 2. The induction step

Let \(k\ge3\) and assume the invariant after step \(k-1\). On each chart the horizontal row at index \(k\) must solve
\[
\begin{aligned}
r\wedge B_k&=G_{k-2}\\
&\quad-\sum_{a=1}^{k-1}A_a\wedge B_{k-a},
\end{aligned}
\tag{2.1}
\]
an equation in \(L^{k-2}\): under (1.2) of the preceding lesson, the right side changes only by multiples of \(\sum_{a=1}^{k-1}B_a\wedge B_{k-a}=0\), whose terms cancel in pairs.

**(a) Divisibility at \(Z\).** Add to the vertical row at index \(k-1\), on every chart, the same global row \(a\in H^0(C,L^k)^{\oplus2}\), that is, the homogeneous term \(t^kaE_t\). Rows at indices below \(k\) still match, because every modification has positive order and moves this term to indices \(\ge k\). The determinant equations already imposed are unchanged, because the first contribution of \(a\) to \(A\wedge B\) is \(a\wedge B_1\), in degree \(k\). At index \(k\), the order-one modification adds, by Lemma 2.1 there,
\[
\begin{gathered}
\delta A_k=\tfrac{k-1}3\,m'a+ma',\\
\delta B_k=-ma,
\end{gathered}
\tag{2.2}
\]
to the transported inside rows; these terms are kept in the comparisons below. On the disc at \(q_j\), the right side of (2.1) changes by \(-a\wedge B_1=-a\wedge R_j\), and \(R_j(0)\ne0\). By Proposition 3.3(4) of the lesson on the curve of genus 21, restriction \(H^0(C,L^k)\to H^0(Z,L^k|_Z)\) is surjective for \(k\ge3\), so the values \(a(q_j)\) can be prescribed arbitrarily; since \(x\mapsto x\wedge R_j(0)\) is onto \(\mathbb C\), \(a\) can be chosen so that the right side of (2.1) vanishes at every \(q_j\).

**(b) The horizontal rows.** On a disc, \(r=z\rho\) with \(\rho\) nowhere zero, and the right side of (2.1) is divisible by \(z\), so (2.1) becomes \(\rho\wedge B_k=(\text{right side})/z\), which has holomorphic solutions. On \(U_0\), with a row \(w\) of sections of \(L^{-1}\) over \(U_0\) satisfying \(r\wedge w=1\) (Section 4 of the preceding lesson), \(B_k=(\text{right side})\,w\) is an algebraic solution.

**(c) Matching the horizontal rows.** Choose vertical rows \(A_k\): holomorphic on the discs, and on \(U_0\) an algebraic lift to \(\mathcal E_k\), which exists because \(U_0\) is affine. Transport the inside rows by the modifications so far. By Section 1, \(r\wedge\delta B_k=0\) on each annulus, since the targets are compatible through degree \(k-2\). So \(\delta B_k=\varphi r\) with \(\varphi\) meromorphic at \(q_j\). A modification of order \(k\) with \(h=\varphi/k\) removes it, by (2.2) of the preceding lesson; take \(b=h'\) if \(k=3\), so that \(\sigma\) is preserved, and \(b=0\) if \(k\ge4\). It changes the target first in degree \(k\), so the comparison in degree \(k-2\) is not affected.

**(d) Matching the vertical rows.** After (c), the vertical rows at index \(k\) differ on each annulus by a row of sections of \(L^{k+1}\), meromorphic at \(q_j\). By Lemma 2.2 of the preceding lesson, the test sections are \(H^0(C,K_C-L^{k+1})=H^0(C,L^{3-k})\).

- For \(k\ge4\), \(L^{3-k}\) has negative degree, there are no tests, and holomorphic and algebraic corrections make the vertical rows match. They do not change the determinant equation of degree \(k\), because \(B_0=0\).
- For \(k=3\), the tests are the constants: the two entries of \(\sum_j\operatorname{Res}_{q_j}\delta_j\) must vanish, \(\delta_j\) being a row of differentials. Use the following freedom. On the \(j\)th annulus replace \(h\) by \(h+\lambda_j/z\) in the order-three modification, keeping \(b=h'\), and add \(3\lambda_jr/z=3\lambda_j\rho\) to the inside row \(B_3\), keeping the inside \(A_3\). By Lemma 2.1 of the preceding lesson the new term \(t^3(-\lambda_jz^{-2}E_t+\lambda_jz^{-1}\partial_z)\) acts on \(trE_t\) by
\[
\begin{gathered}
\Delta A_3=\lambda_j\Bigl(\frac{r'}z+\frac{2r}{z^2}\Bigr),\\
\Delta B_3=-\frac{3\lambda_jr}z,
\end{gathered}
\]
so the horizontal rows still match, \(r\wedge3\lambda_j\rho=0\) leaves (2.1) intact, and the vertical difference changes by \(\Delta A_3\), whose residue is \(3\lambda_jr'(q_j)\) since \(r=zu\). Its action on the terms of positive index, and the transport of the new inside term, affect only indices \(\ge4\). By Corollary 3.4(2) of the lesson on the curve of genus 21, the six rows \(r'(q_j)\) span \(\mathbb C^2\); so the \(\lambda_j\) can be chosen to cancel both entries of the obstruction, and the vertical rows can then be matched. The new term in \(B_3\) may change the coefficient of \(t^4\) in \(A\wedge B\); that equation, with target \(G_2\), is imposed only at step four. The modified order-three generator still has \(b=h'\) and preserves \(\sigma\).

**(e) Extending the target.** It remains to choose \(G_k\) so that the targets are compatible through degree \(k\).

- \(k=3\): all modifications so far preserve \(\sigma\), so \(G=1\) remains compatible; \(G_3=0\).
- \(k=4\): the modifications of orders one to three preserve \(\sigma\), and the order-four modification has \(b=0\), so by (1.2) the transported inside target is \(1-h't^4+O(t^5)\). The coefficient \(h\) of an order-four generator transforms by \(\widetilde h=g^{4-k}h=h\): it is a function, and \(h'\,dz=dh\) is an exact differential on the annulus with residue zero. Lemma 2.2 of the preceding lesson, with \(\mathcal B=L^4=K_C\) and the constant test section, gives \(G_4\), holomorphic on the discs and algebraic on \(U_0\), absorbing the discrepancy; \(G_1=G_2=G_3=0\).
- \(k\ge5\): once \(G_0,\ldots,G_{k-1}\) are compatible, the leading discrepancy is a section of \(L^k\) on the annuli, and the test sections \(H^0(C,L^{4-k})\) vanish; Lemma 2.2 there gives \(G_k\).

In each case \(G_k\) enters only the equation of degree \(k+2\), so the equations already imposed are unchanged. This establishes the invariant after step \(k\). \(\square\)

## 3. The finite jet

Each row of index \(k\) carries the factor \(t^{k+1}\), so it has degree \(k+1\) in the logarithmic frame \((E_t,\partial_z)\). Matching through index seven prescribes the fields modulo terms of degree at least nine.

**Proposition 3.1 (finite compatible jets).** For the curve and the residue data of the preceding lessons there are finitely many modifications of the gluing along the six annuli, each a time-one flow of a field (2.1) of the preceding lesson of order between one and seven, and rows \(A_k,B_k\), \(0\le k\le7\), holomorphic on the discs and algebraic on \(U_0\), such that:

1. the modifications fix \(C\) pointwise and induce the identity on its conormal bundle \(L\);
2. the fields (1.4) of the preceding lesson match through index seven;
3. \(A\wedge B=t^2(1+O(t))\) on every chart, so \(v_1\wedge v_2=t^4(1+O(t))\,E_t\wedge\partial_z\), that is \(t^5(1+O(t))\,\partial_t\wedge\partial_z\).

**Proof.** Perform the first two orders as in the preceding lesson, then the induction step of Section 2 for \(k=3,\ldots,7\). Each modification is a flow of a field holomorphic on the annulus near the zero section, defined after shrinking in the direction transverse to \(C\) (Section 2 of the preceding lesson), and there are finitely many. Property 1 holds for each, hence for their composites. Property 3 is the degree-two equation together with (1.5) of the preceding lesson. \(\square\)

In terms of a surface \(Y\) containing \(C\) and glued by these modifications, with \(\mathcal I=\mathcal O_Y(-C)\) and \(\mathcal F=\mathcal T_Y(-\log C)\) the vector fields tangent to \(C\), the rows define two sections of \(\mathcal F/\mathcal I^9\mathcal F\), lying in \(\mathcal I\mathcal F/\mathcal I^9\mathcal F\), whose wedge has leading term \(t^5\partial_t\wedge\partial_z\) with coefficient one. The next lesson constructs \(Y\) and lifts these sections. The bound nine is where lifting becomes unobstructed: the successive quotients of the unprescribed part are extensions of \(L^{n-4}\) by \(L^n\), by (1.3) of the preceding lesson, and \(H^1(C,L^m)\cong H^0(C,L^{4-m})^*=0\) for \(m\ge5\), which covers both bundles once \(n\ge9\).

## 4. Exercises

**4.1** (easy). Show that at step \(k\) the global addition \(a\) does not change the determinant equations of degrees \(\le k-1\).

**4.2** (medium). Show that the order-four modification cannot be chosen to preserve \(\sigma\) unless \(h\) is constant on the annulus, and compute the first change of the target for \(D=t^4h\,\partial_z\).

**4.3** (medium). At step three, show that without the \(\lambda_j\) the vertical obstruction is a vector \(v\in\mathbb C^2\), and that \(\lambda\mapsto\sum_j3\lambda_jr'(q_j)\) maps \(\mathbb C^6\) onto \(\mathbb C^2\) with a four-dimensional kernel.

**4.4** (medium). Why does step three need the extra freedom while steps four to seven do not? Answer in terms of the degrees of \(L^{3-k}\).

**4.5** (hard). Suppose the matching stopped at index six. Which graded piece of the unprescribed part would then have nonzero first cohomology, and of what dimension?

## 5. Solutions

**4.1.** The new term is \(t^kaE_t\), at index \(k-1\). In \(A\wedge B\) it pairs with \(B_j\), \(j\ge0\), in degree \(k-1+j\); since \(B_0=0\), the first contribution is \(a\wedge B_1\) in degree \(k\).

**4.2.** By Lemma 2.1 of the preceding lesson with \(k=4\), \(\mathcal L_D\sigma=t^4h'\sigma\), independent of \(b\); it vanishes only if \(h'=0\). For \(D=t^4h\,\partial_z\), \(q=t^4h'\), and by (1.2) the target \(1\) becomes \(1-h't^4+O(t^5)\).

**4.3.** The obstruction is the pair of sums of residues of the two entries of the vertical difference, a vector \(v\in\mathbb C^2\). The map \(\lambda\mapsto\sum_j3\lambda_jr'(q_j)\) is linear from \(\mathbb C^6\) to \(\mathbb C^2\), and its image contains the six vectors \(3r'(q_j)\), which span \(\mathbb C^2\); so it is onto, with kernel of dimension \(6-2=4\). Choose \(\lambda\) with image \(-v\).

**4.4.** The tests at step \(k\) are the sections of \(L^{3-k}\). For \(k=3\) this is \(\mathcal O_C\), with the constants as sections; for \(k\ge4\), \(\deg L^{3-k}=10(3-k)<0\), and there are no sections.

**4.5.** Stopping at index six leaves the quotients of degrees \(n\ge8\) unprescribed; the quotient of degree \(8\) is an extension of \(L^4=K_C\) by \(L^8\). Since \(H^1(C,L^8)=0\) and \(H^2\) vanishes on a curve, the cohomology sequence of the extension gives \(H^1\cong H^1(C,K_C)\cong\mathbb C\) for this quotient; for the two fields, \(\mathbb C^2\). Matching index seven prescribes this quotient.

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Section 4: higher orders, determinant targets and the finite compatible jets.
