<span id="banach-holomorphy-generators-and-resolvent-limits"></span>
# Banach holomorphy, generators, and resolvent limits

<span id="oa-mod-sg-04--stones-theorem-with-the-derivative-domain"></span>
<span id="OA-MOD-SG-04"></span>
<span id="oa-mod-sg-04"></span>
## OA-MOD-SG-04 — Stone's theorem with the derivative domain

**Theorem.** Let \(U:\mathbb R\to B(H)\) be a strongly continuous unitary
group. There is a unique self-adjoint operator \(A\) such that

\[
 U_t=e^{itA}\qquad(t\in\mathbb R).
\tag{SG.8}
\]

Its domain and action are exactly

\[
 \begin{aligned}
 D(A)&=\left\{x:\lim_{h\to0}\frac{U_hx-x}{h}
                    \text{ exists in }H\right\},\\
 iAx&=\lim_{h\to0}\frac{U_hx-x}{h}.
 \end{aligned}
\tag{SG.9}
\]

Conversely, the spectral group of every self-adjoint \(A\) is strongly
continuous and has (SG.9) as its derivative domain.

**Proof.** Define \(A\) by (SG.9). For \(\varepsilon>0\), set

\[
 T_\varepsilon x=\frac1\varepsilon\int_0^\varepsilon U_t x\,dt.
\tag{SG.10}
\]

A difference quotient and translation of the integral give

\[
 T_\varepsilon H\subseteq D(A),\qquad
 iAT_\varepsilon=\frac{U_\varepsilon-I}{\varepsilon}.
\tag{SG.11}
\]

Strong continuity gives \(T_\varepsilon x\to x\), so \(D(A)\) is dense.
For \(x\in D(A)\), the group law gives

\[
 \frac d{dt}U_tx=iU_tAx=iAU_tx.
\tag{SG.12}
\]

If \(x_j\to x\) and \(Ax_j\to y\), integrate (SG.12) and pass to the limit:

\[
 U_tx-x=i\int_0^tU_sy\,ds.
\]

The derivative at zero puts \(x\in D(A)\) and gives \(Ax=y\). Thus \(A\) is
closed. Differentiating \(\langle U_tx,U_ty\rangle\) at zero shows

\[
 \langle Ax,y\rangle=\langle x,Ay\rangle
 \quad(x,y\in D(A)),
\]

so \(A\) is symmetric.

The two norm integrals

\[
 B_+x=i\int_0^\infty e^{-t}U_{-t}x\,dt,
 \qquad
 B_-x=-i\int_0^\infty e^{-t}U_tx\,dt
\tag{SG.13}
\]

exist and have norm at most one. Changing variables in the difference
quotients gives

\[
 \frac{U_hB_+x-B_+x}{h}\longrightarrow-B_+x+ix,
 \qquad
 \frac{U_hB_-x-B_-x}{h}\longrightarrow B_-x+ix.
\]

Therefore

\[
 (A-i)B_+=I,\qquad (A+i)B_-=I.
\tag{SG.14}
\]

Both \(A-i\) and \(A+i\) are onto. If \(y\in D(A^*)\), choose
\(x\in D(A)\) with
\((A-i)x=(A^*-i)y\). Then
\(y-x\in\ker(A^*-i)=\operatorname{ran}(A+i)^\perp=0\). Hence
\(D(A^*)\subseteq D(A)\), and symmetry gives \(A=A^*\).

Let \(V_t=e^{itA}\), using the spectral calculus. Both \(U_t\) and \(V_t\)
preserve \(D(A)\), commute there with \(A\), and have derivative \(iA\). For
\(x\in D(A)\), differentiation of \(U_{t-s}V_sx\) with respect to \(s\)
gives zero. Thus \(U_tx=V_tx\); density proves (SG.8) on all of \(H\).

Conversely, scalar dominated convergence proves strong continuity of
\(e^{itA}\). It also gives the derivative \(iAx\) for \(x\in D(A)\). If the
difference quotient converges for an arbitrary \(x\), its norms are bounded
along a sequence \(h\to0\). Fatou's lemma applied to

\[
 \left|\frac{e^{ih\lambda}-1}{h}\right|^2
 \longrightarrow\lambda^2
\]

puts \(x\) in the spectral domain of \(A\). This proves the converse domain
in (SG.9). Uniqueness follows from that formula. \(\square\)

