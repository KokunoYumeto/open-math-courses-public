# Entropy differences and log-determinants

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The next lesson compares the entropy of a Gram matrix \(MM^*\) of a block matrix \(M\) with the entropies of its blocks. This lesson provides the analytic tools. An entropy difference is an integral of differences of log-determinants (Lemma 1.1). A certain log-determinant of a Schur complement is jointly convex (Lemma 2.1), which is proved twice, by a contraction and by a sum of squares. A scalar function \(F\), the deficit that the block inequality will leave, is concave and superadditive (Proposition 4.1), which is also proved twice. Finally, the entropy \(g\) of a two-level state as a function of its determinant has a convexity property needed in the fourth lesson (Lemma 5.2).

- Entropy as an integral of log-determinants (Lemma 1.1).
- Joint convexity by a contraction (Lemma 2.1).
- A second proof by a sum of squares (Section 3).
- The scalar deficit: homogeneity, concavity, superadditivity (Proposition 4.1).
- Entropy as a function of the determinant: derivatives of \(g\) and convexity of \(s\mapsto g(s^2)\) (Lemmas 5.1 and 5.2).
- A second proof of the concavity of the deficit (Section 6).

The lesson follows [OpenAI-GAD, Section 2 and Appendix A]. Notation is that of [Quantum channels and Holevo information](quantum-channels-and-holevo-information.md): \(S(P)=-\operatorname{Tr}P\ln P\) for \(P\ge0\), \(\eta(t)=-t\ln t\), the Shannon entropy \(H\), the binary entropy \(h\) and the function \(g(u)=h\bigl((1+\sqrt{1-4u})/2\bigr)\) on \([0,\frac14]\).

## 1. Entropy as an integral of log-determinants

**Lemma 1.1** ([OpenAI-GAD, Lemma 2.2]). Let \(U\ge0\) and \(V\ge0\) be matrices, possibly of different sizes, with \(\operatorname{Tr}U=\operatorname{Tr}V\). Then
\[
\begin{aligned}
S(U)-S(V)&=\int_0^\infty\frac{f(r)}{r^2}\,dr,\\
f(r)&=\ln\det(I+rU)\\
&\quad-\ln\det(I+rV),
\end{aligned}
\]
and the integral converges absolutely.

*Proof.* Let \(a_1,\dots,a_p\) and \(b_1,\dots,b_q\) be the positive eigenvalues of \(U\) and \(V\), with multiplicity, so that \(\sum_ia_i=\sum_jb_j\); zero eigenvalues contribute nothing to either side. Then
\[
f(r)=\sum_i\ln(1+ra_i)-\sum_j\ln(1+rb_j).
\]
Near \(r=0\), \(\ln(1+ra)=ra+O(r^2)\), and the first-order terms cancel by the equal traces, so \(f(r)=O(r^2)\). For large \(r\), \(\ln(1+ra)=\ln r+\ln a+O(1/r)\), so \(f(r)=(p-q)\ln r+O(1)\). Hence \(f(r)/r^2\) is bounded near \(0\) and \(O(\ln r/r^2)\) at infinity, and the integral converges absolutely.

For \(0<\varepsilon<R\), integration by parts gives
\[
\begin{aligned}
\int_\varepsilon^R\frac{f(r)}{r^2}\,dr&=\Bigl[-\frac{f(r)}r\Bigr]_\varepsilon^R\\
&\quad+\int_\varepsilon^R\frac{f'(r)}r\,dr ,
\end{aligned}
\]
and the boundary terms tend to \(0\) as \(\varepsilon\to0\) and \(R\to\infty\). For \(a>0\),
\[
\frac{a}{r(1+ra)}=\frac ar-\frac{a^2}{1+ra}
\]
has the primitive \(a\ln\bigl(r/(1+ra)\bigr)\). So the last integral is \(\Phi(R)-\Phi(\varepsilon)\), with
\[
\begin{aligned}
\Phi(r)&=\sum_ia_i\ln\frac r{1+ra_i}\\
&\quad-\sum_jb_j\ln\frac r{1+rb_j}.
\end{aligned}
\]
As \(r\to\infty\), \(a\ln\bigl(r/(1+ra)\bigr)\) tends to \(-a\ln a=\eta(a)\), so \(\Phi(R)\to S(U)-S(V)\). As \(r\to0\), the coefficient of \(\ln r\) in \(\Phi(r)\) is \(\sum_ia_i-\sum_jb_j=0\), and the remaining terms \(-a\ln(1+ra)\) tend to \(0\), so \(\Phi(\varepsilon)\to0\). \(\blacksquare\)

## 2. Joint convexity by a contraction

**Lemma 2.1** ([OpenAI-GAD, Lemma 2.3]). For a fixed \(Z\in\mathbb C^{N\times N}\), the function
\[
\begin{aligned}
G_Z(D,E)&=\ln\det(D+ZE^{-1}Z^*)\\
&\quad-\ln\det D
\end{aligned}
\]
is jointly convex on the set of pairs \((D,E)\) of positive definite \(N\times N\) matrices.

*Proof.* The matrix \(D+ZE^{-1}Z^*\) is positive definite, so its determinant is positive. Put
\[
\mathcal D=\begin{pmatrix}D&0\\0&E\end{pmatrix},\qquad\mathcal C=\begin{pmatrix}D&Z\\-Z^*&E\end{pmatrix}.
\]
Elimination of the lower left block gives \(\det\mathcal C=\det E\cdot\det(D+ZE^{-1}Z^*)>0\), so
\[
G_Z(D,E)=\ln\det\mathcal C-\ln\det\mathcal D ,
\]
where \(\ln\) is the real logarithm of a positive number, although \(\mathcal C\) is not Hermitian.

Fix a pair \((D,E)\) and Hermitian directions \(P,Q\), and consider \(s\mapsto G_Z(D+sP,E+sQ)\) on an interval around \(0\) where both arguments stay positive definite. With \(\mathcal H=\operatorname{diag}(P,Q)\), the two block matrices become \(\mathcal D+s\mathcal H\) and \(\mathcal C+s\mathcal H\). For an invertible matrix \(X\) and any \(H\), write \(X_s=X+sH\). Then \(\det X_{s+\epsilon}=\det X_s\,\det(I+\epsilon X_s^{-1}H)\) and \(\det(I+\epsilon K)=1+\epsilon\operatorname{Tr}K+O(\epsilon^2)\); so, wherever \(\det X_s\) is positive,
\[
\frac{d}{ds}\ln\det X_s=\operatorname{Tr}(X_s^{-1}H),
\]
and, since \(\frac d{ds}X_s^{-1}=-X_s^{-1}HX_s^{-1}\),
\[
\begin{aligned}
&\frac{d^2}{ds^2}\ln\det X_s\\
&\qquad=-\operatorname{Tr}(X_s^{-1}HX_s^{-1}H).
\end{aligned}
\]
At \(s=0\) this gives
\[
\begin{aligned}
G''&=\operatorname{Tr}(\mathcal D^{-1}\mathcal H\mathcal D^{-1}\mathcal H)\\
&\quad-\operatorname{Tr}(\mathcal C^{-1}\mathcal H\mathcal C^{-1}\mathcal H).
\end{aligned}
\]
Put
\[
\begin{gathered}
L=\mathcal D^{-1/2}\mathcal H\mathcal D^{-1/2},\\
K=\mathcal D^{-1/2}(\mathcal C-\mathcal D)\mathcal D^{-1/2}.
\end{gathered}
\]
Then \(L\) is Hermitian, and \(K\) is skew-Hermitian because \(\mathcal C-\mathcal D=\bigl(\begin{smallmatrix}0&Z\\ -Z^*&0\end{smallmatrix}\bigr)\) is. For every vector \(w\), \(\langle w,Kw\rangle\) is purely imaginary, so
\[
\|(I+K)w\|^2=\|w\|^2+\|Kw\|^2\ge\|w\|^2 .
\]
Hence \(I+K\) is invertible and \(R=(I+K)^{-1}\) has operator norm at most \(1\). Since \(\mathcal C=\mathcal D^{1/2}(I+K)\mathcal D^{1/2}\), we have \(\mathcal C^{-1}=\mathcal D^{-1/2}R\mathcal D^{-1/2}\), and cyclicity of the trace gives
\[
G''=\|L\|_{\mathrm{HS}}^2-\operatorname{Tr}\bigl((RL)^2\bigr),
\]
where \(\|B\|_{\mathrm{HS}}^2=\sum_{i,j}|B_{ij}|^2\). The left side is real, so the trace is real. For every square matrix \(B\), the Cauchy–Schwarz inequality gives \(|\operatorname{Tr}(B^2)|=\bigl|\sum_{i,j}B_{ij}B_{ji}\bigr|\le\|B\|_{\mathrm{HS}}^2\). Therefore
\[
\begin{aligned}
\operatorname{Tr}\bigl((RL)^2\bigr)&\le\|RL\|_{\mathrm{HS}}^2\\
&\le\|R\|^2\|L\|_{\mathrm{HS}}^2\le\|L\|_{\mathrm{HS}}^2 ,
\end{aligned}
\]
and \(G''\ge0\). So \(G_Z\) has a nonnegative second derivative along every line, at every point of the convex domain; its restriction to every segment is convex, and \(G_Z\) is jointly convex. \(\blacksquare\)

Tang, Zhu, Bai and Wang proved that \(G\mapsto\ln|\det(G+J)|-\ln\det G\) is convex on positive definite matrices for every fixed skew-Hermitian \(J\) [TZBW, Lemma A.1]; Lemma 2.1 is the case of block-diagonal \(G=\mathcal D\) and \(J=\mathcal C-\mathcal D\).

## 3. A second proof by a sum of squares

This proof diagonalizes \(Z\) and writes the second derivative as a sum of squares ([OpenAI-GAD, Appendix A.2]).

*Reduction.* Fix positive definite \(D_0,E_0\). The substitution
\[
\begin{gathered}
D=D_0^{1/2}\tilde DD_0^{1/2},\\
E=E_0^{1/2}\tilde EE_0^{1/2},\\
W=D_0^{-1/2}ZE_0^{-1/2}
\end{gathered}
\]
gives \(ZE^{-1}Z^*=D_0^{1/2}W\tilde E^{-1}W^*D_0^{1/2}\), so the factors \(\det D_0\) cancel and \(G_Z(D,E)=G_W(\tilde D,\tilde E)\). This linear change of variables maps lines to lines and \((D_0,E_0)\) to \((I,I)\). Next, write \(W=U_1YU_2^*\) with unitaries \(U_1,U_2\) and \(Y=\operatorname{diag}(v_1,\dots,v_N)\), \(v_i\ge0\) (a singular value decomposition). Then \(G_W(\tilde D,\tilde E)=G_Y(U_1^*\tilde DU_1,U_2^*\tilde EU_2)\). It therefore suffices to prove that, for all Hermitian \(P,Q\),
\[
\frac{d^2}{ds^2}\Big|_{s=0}G_Y(I+sP,I+sQ)\ge0 .
\]

*Expansion.* For \(H>0\) and Hermitian \(K,K_2\),
\[
\begin{aligned}
&\ln\det(H+sK+s^2K_2)\\
&\quad=\ln\det H+s\operatorname{Tr}(H^{-1}K)\\
&\qquad+s^2\operatorname{Tr}(H^{-1}K_2)\\
&\qquad-\tfrac{s^2}2\operatorname{Tr}(H^{-1}KH^{-1}K)\\
&\qquad+O(s^3).
\end{aligned}
\]
Indeed, factoring \(H^{1/2}\) on both sides reduces this to \(H=I\). For a small Hermitian \(A\) with eigenvalues \(\alpha_i\), \(\ln\det(I+A)=\sum_i\ln(1+\alpha_i)\), which is \(\operatorname{Tr}A-\frac12\operatorname{Tr}A^2+O(\|A\|^3)\); take \(A=sK+s^2K_2\). With \((I+sQ)^{-1}=I-sQ+s^2Q^2+O(s^3)\),
\[
\begin{aligned}
&I+sP+Y(I+sQ)^{-1}Y\\
&\quad=(I+Y^2)+s(P-YQY)\\
&\qquad+s^2YQ^2Y+O(s^3).
\end{aligned}
\]
Put \(R=(I+Y^2)^{-1}\) and \(N_0=P-YQY\). Since \(\ln\det(I+sP)\) equals \(s\operatorname{Tr}P-\frac{s^2}2\operatorname{Tr}P^2+O(s^3)\), the second derivative is
\[
G''=\operatorname{Tr}\bigl(P^2+2RYQ^2Y-RN_0RN_0\bigr).
\]

*Entries.* Write
\[
\begin{gathered}
r_i=\frac1{1+v_i^2},\qquad s_i=\frac{v_i^2}{1+v_i^2}=1-r_i,\\
c_i=\frac{v_i}{1+v_i^2},
\end{gathered}
\]
so that \(r_iv_i^2=s_i\), \(r_ir_jv_i^2v_j^2=s_is_j\) and \(r_ir_jv_iv_j=c_ic_j\). In entries, \(\operatorname{Tr}P^2=\sum_{i,j}|P_{ij}|^2\), \(\operatorname{Tr}(RYQ^2Y)=\sum_is_i\sum_j|Q_{ij}|^2\), and, since \(N_0\) is Hermitian with \((N_0)_{ij}=P_{ij}-v_iv_jQ_{ij}\),
\[
\begin{aligned}
&\operatorname{Tr}(RN_0RN_0)\\
&\quad=\sum_{i,j}r_ir_j\bigl|P_{ij}-v_iv_jQ_{ij}\bigr|^2 .
\end{aligned}
\]
Collecting terms,
\[
\begin{aligned}
G''=\sum_{i,j}\Bigl[&(1-r_ir_j)|P_{ij}|^2\\
&+2c_ic_j\operatorname{Re}\bigl(P_{ij}\overline{Q_{ij}}\bigr)\\
&+(2s_i-s_is_j)|Q_{ij}|^2\Bigr].
\end{aligned}
\]
Since \(|Q_{ij}|=|Q_{ji}|\), the coefficient of \(|Q_{ij}|^2\) may be replaced by its average over \((i,j)\) and \((j,i)\), which is \(s_i+s_j-s_is_j=1-r_ir_j\), also for \(i=j\). Completing the square,
\[
\begin{aligned}
G''=\sum_{i,j}\Bigl[&(1-r_ir_j-c_ic_j)\\
&\times\bigl(|P_{ij}|^2+|Q_{ij}|^2\bigr)\\
&+c_ic_j|P_{ij}+Q_{ij}|^2\Bigr],
\end{aligned}
\]
and every coefficient is nonnegative: \(c_ic_j\ge0\), and
\[
\begin{aligned}
&1-r_ir_j-c_ic_j\\
&\quad=\frac{(v_i-v_j)^2+v_iv_j+v_i^2v_j^2}{(1+v_i^2)(1+v_j^2)}\ge0 .
\end{aligned}
\]
This proves \(G''\ge0\) again, including for singular \(Z\). \(\blacksquare\)

## 4. The scalar deficit

For \(x,y,z\ge0\) put
\[
\begin{gathered}
m=x+y+z,\\
\lambda_\pm=\frac{m\pm\sqrt{m^2-4yz}}2,\\
F(x,y,z)=\eta(x)+\eta(y)+\eta(z)\\
-\eta(\lambda_+)-\eta(\lambda_-).
\end{gathered}
\]
Here \(m^2\ge(y+z)^2\ge4yz\), and \(\lambda_\pm\ge0\) have sum \(m\) and product \(yz\). The function \(F\) is continuous on \([0,\infty)^3\). On the simplex \(x+y+z=1\), \(\lambda_\pm=(1\pm\sqrt{1-4yz})/2\) and \(\eta(\lambda_+)+\eta(\lambda_-)=g(yz)\), so
\[
F(x,y,z)=H(x,y,z)-g(yz).
\]
The scalar matrix \(\bigl(\begin{smallmatrix}\sqrt x&\sqrt y\\ \sqrt z&0\end{smallmatrix}\bigr)\) has the squared singular values \(\lambda_\pm\) when \(x+y+z=1\), so \(g(yz)\) is the entropy of its Gram matrix; the next lesson explains the role of \(F\).

**Proposition 4.1** ([OpenAI-GAD, Lemma 2.4]). The function \(F\) is positively homogeneous of degree one and concave on \([0,\infty)^3\). For every finite family of triples in \([0,\infty)^3\),
\[
\begin{aligned}
&\sum_iF(x_i,y_i,z_i)\\
&\qquad\le F\Bigl(\sum_ix_i,\sum_iy_i,\sum_iz_i\Bigr).
\end{aligned}
\]
In particular \(F\) is concave on the simplex.

*Proof.* *An integral.* The lists \((x,y,z)\) and \((\lambda_+,\lambda_-)\) have the same sum, so Lemma 1.1, applied to the diagonal matrices with these entries, gives
\[
F(x,y,z)=\int_0^\infty\frac{\phi(r)}{r^2}\,dr ,
\]
where
\[
\begin{aligned}
\phi(r)&=\ln\bigl((1+rx)(1+ry)(1+rz)\bigr)\\
&\quad-\ln\bigl((1+r\lambda_+)(1+r\lambda_-)\bigr).
\end{aligned}
\]
Since \((1+r\lambda_+)(1+r\lambda_-)=1+rm+r^2yz\), which is \((1+ry)(1+rz)+rx\),
\[
\begin{aligned}
\phi(r)&=\ln(1+rx)\\
&\quad-\ln\Bigl(1+\frac{rx}{(1+ry)(1+rz)}\Bigr).
\end{aligned}
\]

*Concavity at \(x=1\).* For \(x=1\), \(\phi(r)=\ln(1+r)-G_{\sqrt r}(1+ry,1+rz)\), where \(G\) is the function of Lemma 2.1 for \(N=1\): indeed \(G_{\sqrt r}(d,e)=\ln\bigl(1+r/(de)\bigr)\). By Lemma 2.1 and the affine dependence of \((1+ry,1+rz)\) on \((y,z)\), \(\phi(r)\) is concave in \((y,z)\in[0,\infty)^2\) for every \(r>0\). Integrating the concavity inequalities, which is allowed because all the integrals converge absolutely, shows that \(F(1,\cdot,\cdot)\) is concave on \([0,\infty)^2\).

*Homogeneity.* Scaling \((x,y,z)\) by \(s>0\) scales \(\lambda_\pm\) by \(s\). Since \(\eta(st)=s\eta(t)-st\ln s\), the terms with \(\ln s\) contribute \(-s\ln s\,(x+y+z-\lambda_+-\lambda_-)=0\), so \(F(sx,sy,sz)=sF(x,y,z)\); for \(s=0\) both sides are \(0\).

*Superadditivity.* Consider first triples with all \(x_i>0\), and let \(x=\sum_ix_i\). Homogeneity and the concavity of \(F(1,\cdot,\cdot)\), with the weights \(x_i/x\), give
\[
\begin{aligned}
&\sum_iF(x_i,y_i,z_i)\\
&\quad=x\sum_i\frac{x_i}xF\Bigl(1,\frac{y_i}{x_i},\frac{z_i}{x_i}\Bigr)\\
&\quad\le xF\Bigl(1,\frac{\sum_iy_i}x,\frac{\sum_iz_i}x\Bigr)\\
&\quad=F\Bigl(x,\sum_iy_i,\sum_iz_i\Bigr).
\end{aligned}
\]
In general, replace every \(x_i\) by \(x_i+\varepsilon\) and let \(\varepsilon\to0\); continuity of \(F\) gives the inequality, also when every \(x_i\) vanishes.

*Concavity.* For triples \(a,b\) and \(0\le\theta\le1\), superadditivity for the two triples \(\theta a\) and \((1-\theta)b\), and homogeneity, show that \(F(\theta a+(1-\theta)b)\) is at least \(\theta F(a)+(1-\theta)F(b)\). \(\blacksquare\)

## 5. Entropy as a function of the determinant

**Lemma 5.1** (derivatives of \(g\)). For \(0<u<\frac14\), put \(t=\sqrt{1-4u}\) and \(L=\operatorname{atanh}(t)/t\), where \(\operatorname{atanh}t=\frac12\ln\frac{1+t}{1-t}\). Then
\[
\begin{gathered}
g'(u)=2L,\qquad g''(u)=\frac{4L-1/u}{t^2},\\
ug''(u)+\tfrac12g'(u)=\frac{L-1}{t^2}\ge0 .
\end{gathered}
\]

*Proof.* With \(q=(1+t)/2\) we have \(g(u)=h(q)\), \(h'(q)=\ln\frac{1-q}q\), and \(\frac{dq}{du}=\frac12\frac{dt}{du}=-\frac1t\). So
\[
\begin{aligned}
g'(u)&=\frac1t\ln\frac q{1-q}\\
&=\frac1t\ln\frac{1+t}{1-t}=2L .
\end{aligned}
\]
Since \(\frac{d}{dt}\operatorname{atanh}t=(1-t^2)^{-1}\), \(\frac{dL}{dt}=\frac1{t(1-t^2)}-\frac Lt\), and with \(1-t^2=4u\),
\[
\begin{aligned}
g''(u)&=2\frac{dL}{dt}\frac{dt}{du}=-\frac4t\frac{dL}{dt}\\
&=\frac{4L}{t^2}-\frac1{ut^2}.
\end{aligned}
\]
Then
\[
\begin{aligned}
ug''+\tfrac12g'&=\frac{4uL-1}{t^2}+L\\
&=\frac{4uL-1+L(1-4u)}{t^2}\\
&=\frac{L-1}{t^2}.
\end{aligned}
\]
Finally \(\operatorname{atanh}t\ge t\), because both sides vanish at \(0\) and \((\operatorname{atanh}t)'=(1-t^2)^{-1}\ge1\); so \(L\ge1\). \(\blacksquare\)

**Lemma 5.2** ([OpenAI-GAD, Lemma 2.5]). The function \(s\mapsto g(s^2)\) is nondecreasing and convex on \([0,\frac12]\).

*Proof.* For \(0<s<\frac12\) put \(u=s^2\). Lemma 5.1 gives
\[
\begin{gathered}
\frac{d}{ds}g(s^2)=2s\,g'(u)\ge0,\\
\frac{d^2}{ds^2}g(s^2)=4ug''(u)+2g'(u)\ge0 ,
\end{gathered}
\]
the last because \(4ug''+2g'=4\bigl(ug''+\frac12g'\bigr)\). A continuous function on \([0,\frac12]\) that is nondecreasing and convex on the open interval has both properties on the closed interval. \(\blacksquare\)

## 6. A second proof of the concavity of the deficit

On the simplex \(F(x,y,z)=H(x,y,z)-g(yz)\), and its concavity can be checked through the Hessian ([OpenAI-GAD, Appendix A.1]). This gives a second proof of Proposition 4.1.

*Second proof of Proposition 4.1.* Homogeneity was proved directly. In the interior of the simplex put \(x=1-y-z\) and \(u=yz\); then \(0<u<\frac14\), because \(yz\le\frac14(y+z)^2\) and \(y+z<1\). The negative Hessian of \((y,z)\mapsto F(1-y-z,y,z)\) is the symmetric matrix \(J\) with the entries
\[
\begin{gathered}
J_{11}=\frac1y+\frac1x+z^2g'',\\
J_{22}=\frac1z+\frac1x+y^2g'',\\
J_{12}=J_{21}=\frac1x+g'+ug'',
\end{gathered}
\]
with \(g',g''\) evaluated at \(u\). Expanding, and using \(\frac1{yz}+\frac1{xy}+\frac1{xz}=\frac1{xu}\) and \(x(y+z)+(y-z)^2=y+z-4u\),
\[
\begin{aligned}
\det J&=\frac1{xu}+\frac{y+z-4u}xg''\\
&\quad-\frac2xg'-g'^2-2ug'g'' .
\end{aligned}
\]
Substitute Lemma 5.1, with \(y+z-4u=t^2-x\). The terms with \(1/x\) cancel, and
\[
\begin{aligned}
\det J&=\frac{1/u-16uL^2}{t^2}-4L^2\\
&=\frac{1-4uL^2}{ut^2}.
\end{aligned}
\]
This is positive: \(4uL^2<1\) means \(\operatorname{atanh}t<t/\sqrt{1-t^2}\), which holds for \(0<t<1\) because both sides vanish at \(0\) and their derivatives are \((1-t^2)^{-1}<(1-t^2)^{-3/2}\). Moreover
\[
\begin{aligned}
&\begin{pmatrix}y&z\end{pmatrix}J\begin{pmatrix}y\\ z\end{pmatrix}\\
&\quad=\frac{y+z}x+4u\Bigl(ug''+\tfrac12g'\Bigr)>0 .
\end{aligned}
\]
A real symmetric \(2\times2\) matrix with positive determinant has two eigenvalues of the same sign, and a positive value of its quadratic form makes them positive. So \(J\) is positive definite, \(F\) is concave in the interior of the simplex, and by continuity on the closed simplex.

Superadditivity follows. Omit zero triples, put \(m_i=x_i+y_i+z_i>0\) and \(m=\sum_im_i\); homogeneity and concavity on the simplex give
\[
\begin{aligned}
&\sum_iF(x_i,y_i,z_i)\\
&\quad=m\sum_i\frac{m_i}mF\Bigl(\frac{x_i}{m_i},\frac{y_i}{m_i},\frac{z_i}{m_i}\Bigr)\\
&\quad\le F\Bigl(\sum_ix_i,\sum_iy_i,\sum_iz_i\Bigr),
\end{aligned}
\]
and concavity on \([0,\infty)^3\) follows from superadditivity and homogeneity (Exercise 7.5). \(\blacksquare\)

## 7. Exercises

**7.1.** Check Lemma 1.1 for \(U=(1)\) and \(V=\operatorname{diag}(\frac12,\frac12)\): show that
\[
\int_0^\infty\Bigl(\ln(1+r)-2\ln\Bigl(1+\frac r2\Bigr)\Bigr)\frac{dr}{r^2}
\]
equals \(-\ln2\).

**7.2.** For \(N=1\), \(G_z(d,e)=\ln\bigl(1+|z|^2/(de)\bigr)\). Compute its Hessian in \((d,e)\) and verify directly that it is positive semidefinite.

**7.3.** Show that \(F(0,y,z)=0\) and \(F(x,y,0)=(x+y)\,h\bigl(\frac x{x+y}\bigr)\) for \(x+y>0\).

**7.4.** Show that \(g'(u)\to\infty\) as \(u\to0\) and \(g'(u)\to2\) as \(u\to\frac14\).

**7.5.** Let \(\Phi\) be a continuous function on \([0,\infty)^3\) that is positively homogeneous of degree one. Show that \(\Phi\) is concave if and only if it is superadditive.

## 8. Solutions

**7.1.** In the proof of Lemma 1.1, \(\Phi(r)=\ln\frac r{1+r}-\ln\frac r{1+r/2}\), that is \(\ln\frac{1+r/2}{1+r}\), which tends to \(\ln\frac12\) as \(r\to\infty\) and to \(0\) as \(r\to0\). So the integral is \(-\ln2=S(U)-S(V)\).

**7.2.** With \(w=de+c\), \(c=|z|^2\): \(\partial_d^2G=\frac1{d^2}-\frac{e^2}{w^2}\), \(\partial_e^2G=\frac1{e^2}-\frac{d^2}{w^2}\) and \(\partial_d\partial_eG=\frac c{w^2}\). The diagonal entries are \(\ge0\) because \(w\ge de\). With \(p=de\), the determinant is
\[
\begin{aligned}
&\frac{(w^2-p^2)^2-p^2c^2}{p^2w^4}\\
&\qquad=\frac{c^2(p+c)(3p+c)}{p^2w^4}\ge0 ,
\end{aligned}
\]
since \(w^2-p^2=c(2p+c)\).

**7.3.** For \(x=0\), \(m=y+z\) and \(\lambda_\pm\) are \(\max(y,z)\) and \(\min(y,z)\), so the four \(\eta\) terms cancel. For \(z=0\), \(\lambda_+=m=x+y\) and \(\lambda_-=0\), so \(F=\eta(x)+\eta(y)-\eta(x+y)\), which is \((x+y)h\bigl(\frac x{x+y}\bigr)\).

**7.4.** As \(u\to0\), \(t\to1\) and \(\operatorname{atanh}t\to\infty\), so \(g'=2L\to\infty\). As \(u\to\frac14\), \(t\to0\) and \(L\to1\), so \(g'\to2\).

**7.5.** If \(\Phi\) is concave, then \(\Phi(a+b)=2\Phi(\frac12a+\frac12b)\), which is at least \(\Phi(a)+\Phi(b)\). If \(\Phi\) is superadditive, then \(\Phi(\theta a+(1-\theta)b)\ge\Phi(\theta a)+\Phi((1-\theta)b)\), and by homogeneity the right side is \(\theta\Phi(a)+(1-\theta)\Phi(b)\).

## References

- [OpenAI-GAD] OpenAI, *Classical capacity and entropy inequalities for generalized amplitude damping*, OpenAI Math Release preprint, 24 September 2026, Section 2 and Appendix A. https://github.com/openai/math/tree/main/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026
- [TZBW] Z. Tang, C. Zhu, G. Bai and X. Wang, *Classical capacity and entanglement cost of the amplitude damping channel*, arXiv:2609.28592 (2026). https://arxiv.org/abs/2609.28592
