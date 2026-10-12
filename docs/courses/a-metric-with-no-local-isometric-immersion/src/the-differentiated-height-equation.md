# The differentiated height equation

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The height equation \(H_{xx}H_{yy}-H_{xy}^2=KE\) is elliptic where the curvature \(K\) is positive and hyperbolic where it is negative. To control a solution across a curve where \(K\) changes its sign, the proof of [OpenAI-I] differentiates the equation many times in one direction and studies the linear equation satisfied by the derivative. This lesson derives that linear equation exactly. Its form is the point: in suitable coordinates \(t,s\) the derivative \(u=\partial_y^lz\) satisfies
\[
u_{tt}+Au_{ss}+Bu_t+Cu_s=R,
\]
where \(A\) is the curvature times a positive function, and the coefficient \(C\) of the first derivative across is \((l+1)A_s\) up to a multiple of \(K\). So \(C\) is tied to the derivative of the curvature, with a factor that grows with the number of differentiations.

- The equation solved for \(z_{xx}\), and the derivatives of the right side with respect to the derivatives of \(z\) (Lemma 1.1).
- The third derivatives of a function on a surface commute up to the curvature (Lemma 2.2).
- The drift identity: the vector field \(D=\partial_x-q\,\partial_y\) along which the Hessian degenerates turns at a rate given by \(K_y\) (Theorem 3.1).
- The equation for \(u=\partial_y^lz\) (Theorem 5.1), and its form in coordinates in which \(D=\partial_t\) (Theorem 6.2).

The lesson follows [OpenAI-I, Section 3, the lemmas on the curvature drift and on the high derivative equation], with the terms that are written \(O(K)\) there made explicit. It continues [Heights of an immersed surface](heights-of-an-immersed-surface.md) and uses its notation. Nothing in this lesson is an estimate; all statements are identities.

## 1. The solved equation

Let \(g\) be a metric on an open set \(U\) of the plane with the coordinates \(x,y\), also numbered \(1,2\); indices that occur twice are summed. Let \(z\) be a smooth function on \(U\) with the covariant Hessian \(H_{ij}=z_{ij}-\Gamma^r_{ij}z_r\), where \(z_i,z_{ij}\) are partial derivatives, and
\[
E=\det g\,(1-g^{ij}z_iz_j).
\]
Suppose that \(z\) solves the height equation \(H_{xx}H_{yy}-H_{xy}^2=KE\) on \(U\) and that \(H_{yy}\ne0\) on \(U\). Put
\[
\begin{gathered}
q=\frac{H_{xy}}{H_{yy}},\qquad D=\partial_x-q\,\partial_y,\\
G=\frac E{H_{yy}^2},\qquad a=KG .
\end{gathered}
\]
For vectors \(v,w\) let \(H(v,w)=H_{ij}v_iw_j\). We write \(D\) also for the vector \((1,-q)\) and \(Y\) for the vector \((0,1)\). By the definition of \(q\) and the height equation,
\[
\begin{gathered}
H(Y,D)=H_{xy}-qH_{yy}=0,\\
H(D,D)=H_{xx}-q^2H_{yy}=aH_{yy},
\end{gathered}
\]
and therefore \(H(\partial_x,D)\), which is \(H(D,D)+qH(Y,D)\), equals \(aH_{yy}\). So \(D\) is the direction in which the Hessian is small where the curvature is small.

The height equation, solved for \(z_{xx}\), is
\[
z_{xx}=P,\qquad P=\Gamma^r_{xx}z_r+\frac{H_{xy}^2+KE}{H_{yy}} .
\]
Here \(P\) is regarded as a function of the point \((x,y)\) and of four independent variables \(z_x,z_y,z_{xy},z_{yy}\), through \(H_{xy}=z_{xy}-\Gamma^r_{xy}z_r\), \(H_{yy}=z_{yy}-\Gamma^r_{yy}z_r\) and \(E\); it is defined where \(H_{yy}\ne0\). For \(i\in\{x,y\}\) let
\[
\Gamma^i_{DD}=\Gamma^i_{xx}-2q\,\Gamma^i_{xy}+q^2\,\Gamma^i_{yy}.
\]

**Lemma 1.1.** The partial derivatives of \(P\) with respect to its four variables are
\[
\begin{gathered}
P_{z_{xy}}=2q,\qquad P_{z_{yy}}=-q^2-a,\\
P_{z_i}=\Gamma^i_{DD}+K\Bigl(\frac{E_{z_i}}{H_{yy}}+\frac{E\,\Gamma^i_{yy}}{H_{yy}^2}\Bigr),
\end{gathered}
\]
where \(E_{z_i}=-2\det g\,g^{ij}z_j\).

**Proof.** \(P_{z_{xy}}=2H_{xy}/H_{yy}\) and \(P_{z_{yy}}=-(H_{xy}^2+KE)/H_{yy}^2\). The variable \(z_i\) occurs in \(\Gamma^r_{xx}z_r\), in \(H_{xy}\) and \(H_{yy}\) with the derivatives \(-\Gamma^i_{xy}\) and \(-\Gamma^i_{yy}\), and in \(E\). So
\[
\begin{aligned}
P_{z_i}&=\Gamma^i_{xx}-\frac{2H_{xy}\Gamma^i_{xy}}{H_{yy}}+\frac{KE_{z_i}}{H_{yy}}\\
&\quad+\frac{(H_{xy}^2+KE)\,\Gamma^i_{yy}}{H_{yy}^2},
\end{aligned}
\]
and \((H_{xy}^2+KE)/H_{yy}^2=q^2+KE/H_{yy}^2\). \(\blacksquare\)

## 2. Third derivatives

For a metric \(g\) let
\[
\begin{aligned}
R_{kji}{}^m&=\partial_k\Gamma^m_{ji}-\partial_j\Gamma^m_{ki}\\
&\quad+\Gamma^m_{kr}\Gamma^r_{ji}-\Gamma^m_{jr}\Gamma^r_{ki}.
\end{aligned}
\]
The definition of the curvature in the lesson on heights says \(K\det g=g_{1m}R_{122}{}^m\).

**Lemma 2.1.** In dimension two, \(R_{kji}{}^m=K\bigl(\delta^m_k\,g_{ji}-\delta^m_j\,g_{ki}\bigr)\), where \(\delta^m_k\) is \(1\) for \(m=k\) and \(0\) otherwise.

**Proof.** Let \(R_{kjis}=g_{sm}R_{kji}{}^m\) and \(\Gamma_{ki,s}=g_{sm}\Gamma^m_{ki}\), which is \(\tfrac12(\partial_kg_{is}+\partial_ig_{ks}-\partial_sg_{ki})\), so that \(\partial_kg_{is}=\Gamma_{ki,s}+\Gamma_{ks,i}\). Then \(g_{sm}\partial_k\Gamma^m_{ji}=\partial_k\Gamma_{ji,s}-(\Gamma_{ks,m}+\Gamma_{km,s})\Gamma^m_{ji}\), and inserting this and the same formula with \(k,j\) exchanged gives
\[
\begin{aligned}
R_{kjis}&=\partial_k\Gamma_{ji,s}-\partial_j\Gamma_{ki,s}\\
&\quad-\Gamma_{ks,m}\Gamma^m_{ji}+\Gamma_{js,m}\Gamma^m_{ki}.
\end{aligned}
\]
Add the same expression with \(i,s\) exchanged. The first derivatives give \(\partial_k\partial_jg_{is}-\partial_j\partial_kg_{is}=0\). The products cancel in pairs, because \(\Gamma_{ks,m}\Gamma^m_{ji}=g_{mn}\Gamma^n_{ks}\Gamma^m_{ji}\) is unchanged if the pairs \((k,s)\) and \((j,i)\) are exchanged. So \(R_{kjis}=-R_{kjsi}\), and \(R_{kjis}=-R_{jkis}\) by the definition. The expression \(g_{ks}g_{ji}-g_{js}g_{ki}\) has the same two properties. In dimension two, a quantity with four indices that changes its sign under each of these two exchanges is determined by its value for \((k,j,i,s)=(1,2,2,1)\). There, \(R_{1221}=K\det g\) and the other expression is \(\det g\). So \(R_{kjis}=K(g_{ks}g_{ji}-g_{js}g_{ki})\); multiplying by the inverse matrix of \(g\) gives the statement. \(\blacksquare\)

For a function \(z\) with the covariant Hessian \(H\), let
\[
T_{ijk}=\partial_kH_{ij}-\Gamma^r_{ki}H_{rj}-\Gamma^r_{kj}H_{ir} .
\]
It is symmetric in \(i,j\). For vector fields \(v,w\) and a vector \(e\), with \(\nabla_ev=e_k(\partial_kv_r+\Gamma^r_{km}v_m)\) in the component \(r\), the definition gives the rule
\[
\begin{aligned}
&e_k\partial_k\bigl(H(v,w)\bigr)\\
&\quad=T_{ijk}v_iw_je_k+H(\nabla_ev,w)\\
&\qquad+H(v,\nabla_ew).
\end{aligned}
\]

**Lemma 2.2.** \(T_{ijk}-T_{ikj}=K\,(g_{ik}z_j-g_{ij}z_k)\).

**Proof.** In \(T_{ijk}-T_{ikj}\) the third derivatives of \(z\) cancel, and so do the terms \(\Gamma^r_{kj}H_{ir}\). There remain
\[
\begin{aligned}
&-\partial_k\Gamma^m_{ji}z_m+\partial_j\Gamma^m_{ki}z_m\\
&\quad-\Gamma^r_{ji}z_{kr}+\Gamma^r_{ki}z_{jr}\\
&\quad-\Gamma^r_{ki}\bigl(z_{jr}-\Gamma^m_{jr}z_m\bigr)\\
&\quad+\Gamma^r_{ji}\bigl(z_{kr}-\Gamma^m_{kr}z_m\bigr).
\end{aligned}
\]
The second derivatives of \(z\) cancel, and the rest is \(-R_{kji}{}^mz_m\). By Lemma 2.1 this is \(-K(g_{ji}z_k-g_{ki}z_j)\). \(\blacksquare\)

## 3. The drift identity

**Theorem 3.1.** In the situation of Section 1,
\[
Dq-q\,\Gamma^x_{DD}-\Gamma^y_{DD}=K_yG+K\rho_1,
\]
where \(Dq=q_x-qq_y\), \(K_y=\partial_yK\), and
\[
\begin{aligned}
H_{yy}\,\rho_1&=\partial_y\Bigl(\frac E{H_{yy}}\Bigr)-\bigl(\Gamma^x_{xy}-q\Gamma^x_{yy}\bigr)\frac E{H_{yy}}\\
&\quad-g(D,Y)\,Dz+g(D,D)\,z_y .
\end{aligned}
\]
Here \(g(D,Y)=g_{xy}-qg_{yy}\), \(g(D,D)=g_{xx}-2qg_{xy}+q^2g_{yy}\) and \(Dz=z_x-qz_y\). Consequently
\[
Dq-P_{z_x}q-P_{z_y}=K_yG+K(\rho_1-\rho_2),
\]
with
\[
\begin{aligned}
\rho_2&=q\Bigl(\frac{E_{z_x}}{H_{yy}}+\frac{E\,\Gamma^x_{yy}}{H_{yy}^2}\Bigr)\\
&\quad+\frac{E_{z_y}}{H_{yy}}+\frac{E\,\Gamma^y_{yy}}{H_{yy}^2}.
\end{aligned}
\]

**Proof.** Apply the rule before Lemma 2.2 to \(H(Y,D)=0\) in the direction \(e=D\):
\[
\begin{aligned}
0&=T(Y,D;D)+H(\nabla_DY,D)\\
&\quad+H(Y,\nabla_DD),
\end{aligned}
\]
where \(T(v,w;e)=T_{ijk}v_iw_je_k\). We compute the three terms.

*Third term.* The component \(r\) of \(\nabla_DD\) is \(D(D_r)+\Gamma^r_{DD}\), that is \(\Gamma^x_{DD}\) for \(r=x\) and \(-Dq+\Gamma^y_{DD}\) for \(r=y\). Since \(H(Y,\partial_x)=qH_{yy}\),
\[
\begin{aligned}
&H(Y,\nabla_DD)\\
&\quad=H_{yy}\bigl(q\,\Gamma^x_{DD}+\Gamma^y_{DD}-Dq\bigr).
\end{aligned}
\]

*Second term.* \(Y\) is constant, so the component \(r\) of \(\nabla_DY\) is \(\Gamma^r_{xy}-q\Gamma^r_{yy}\). Since \(H(\partial_y,D)=0\) and \(H(\partial_x,D)=aH_{yy}\),
\[
H(\nabla_DY,D)=\bigl(\Gamma^x_{xy}-q\Gamma^x_{yy}\bigr)\,aH_{yy}.
\]

*First term.* By the symmetry of \(T\) in its first two indices and by Lemma 2.2,
\[
\begin{aligned}
&T(Y,D;D)-T(D,D;Y)\\
&\quad=K\bigl(g(D,D)\,z_y-g(D,Y)\,Dz\bigr).
\end{aligned}
\]
Apply the rule to \(H(D,D)=aH_{yy}\) in the direction \(Y\). The component \(r\) of \(\nabla_YD\) is \(\partial_y(D_r)+\Gamma^r_{yx}-q\Gamma^r_{yy}\), and \(\partial_y(D_r)\) is not zero only for \(r=y\), where \(H(\partial_y,D)=0\). So
\[
\begin{aligned}
&T(D,D;Y)\\
&\ =\partial_y(aH_{yy})-2H(\nabla_YD,D)\\
&\ =\partial_y(aH_{yy})-2\bigl(\Gamma^x_{xy}-q\Gamma^x_{yy}\bigr)aH_{yy}.
\end{aligned}
\]
Finally \(aH_{yy}=KE/H_{yy}\), so \(\partial_y(aH_{yy})=K_yE/H_{yy}+K\,\partial_y(E/H_{yy})\).

Adding up and dividing by \(H_{yy}\) gives the first identity. The second follows from Lemma 1.1, since \(P_{z_x}q+P_{z_y}=q\Gamma^x_{DD}+\Gamma^y_{DD}+K\rho_2\). \(\blacksquare\)

At the points where \(K=0\) the identity says that \(Dq-q\Gamma^x_{DD}-\Gamma^y_{DD}=K_yG\). The left side measures how the field \(D\) fails to be parallel along itself, in the direction of \(y\); it is governed by the derivative of the curvature across.

## 4. Derivatives of a composite function

**Lemma 4.1.** Let \(F(y,p)\) be a smooth function of a real variable \(y\) and of \(p=(p_1,\dots,p_N)\), and let \(p(y)\) be a smooth curve in the domain of \(F\). For \(l\ge3\),
\[
\begin{aligned}
&\frac{d^l}{dy^l}F(y,p(y))\\
&\quad=\sum_iF_{p_i}\,p_i^{(l)}\\
&\qquad+l\sum_i\frac d{dy}\bigl[F_{p_i}\bigr]\,p_i^{(l-1)}+G_l,
\end{aligned}
\]
where \(F_{p_i}\) is taken at \((y,p(y))\), \(\tfrac d{dy}[F_{p_i}]\) is the derivative of the function \(y\mapsto F_{p_i}(y,p(y))\), and \(G_l\) is a sum of terms of the form
\[
\begin{gathered}
c\cdot p_{i_1}^{(k_1)}\cdots p_{i_n}^{(k_n)},\\
1\le k_j\le l-2,\qquad k_1+\dots+k_n\le l,
\end{gathered}
\]
with \(n\ge0\), in which \(c\) is an integer multiple of a partial derivative of \(F\) of order at most \(l\) at \((y,p(y))\).

**Proof.** First, by induction on \(l\ge1\), the derivative of order \(l\) is a sum of terms \(c\cdot p_{i_1}^{(k_1)}\cdots p_{i_n}^{(k_n)}\) in which \(c\) is an integer multiple of a partial derivative of \(F\) with \(\alpha\) differentiations in \(y\) and \(n\) in \(p\), and \(\alpha+k_1+\dots+k_n=l\) with all \(k_j\ge1\): differentiating such a term once either raises \(\alpha\) by one, or adds a factor \(p_i'\), or raises one \(k_j\) by one.

For \(l=2\) the derivative is \(\sum_iF_{p_i}p_i''+G\) with \(G=F_{yy}+2\sum_iF_{yp_i}p_i'+\sum_{i,j}F_{p_ip_j}p_i'p_j'\). Differentiating once more, the terms that contain a second derivative of \(p\) are \(\tfrac d{dy}[F_{p_i}]p_i''\) from the first sum and \(2(F_{yp_i}+\sum_jF_{p_ip_j}p_j')p_i''=2\tfrac d{dy}[F_{p_i}]p_i''\) from \(G\). This is the statement for \(l=3\). If the statement holds for \(l\ge3\), differentiate it: the first sum gives \(\sum F_{p_i}p_i^{(l+1)}+\sum\tfrac d{dy}[F_{p_i}]p_i^{(l)}\); the second gives \(l\sum\tfrac d{dy}[F_{p_i}]p_i^{(l)}\) and terms with derivatives of \(p\) of order at most \(l-1\); and the derivative of \(G_l\) has derivatives of \(p\) of order at most \(l-1\). With the first paragraph this is the statement for \(l+1\). \(\blacksquare\)

## 5. The equation for a derivative of high order

**Theorem 5.1.** In the situation of Section 1, let \(l\ge3\) and \(u=\partial_y^lz\). Then
\[
\begin{aligned}
&D^2u+a\,u_{yy}+B\,Du\\
&\quad+\bigl((l+1)K_yG+K\rho\bigr)u_y=R_l,
\end{aligned}
\]
where \(D^2u=D(Du)\),
\[
\begin{gathered}
B=-P_{z_x}-2l\,q_y,\\
\rho=\rho_1-\rho_2+l\,G_y,
\end{gathered}
\]
and
\[
\begin{aligned}
R_l&=l\,\partial_y[P_{z_x}]\,\partial_y^{l-1}z_x\\
&\quad+l\,\partial_y[P_{z_y}]\,\partial_y^{l-1}z_y+G_l .
\end{aligned}
\]
Here \(\partial_y[\,\cdot\,]\) is the derivative in \(y\) of the function of \((x,y)\) obtained by inserting the solution, and \(G_l\) is the sum of Lemma 4.1 for \(F=P\) and \(p=(z_x,z_y,z_{xy},z_{yy})\), with \(x\) as a parameter. In \(R_l\) all derivatives of \(z\) have order at most \(l\).

**Proof.** Differentiate \(z_{xx}=P(x,y,z_x,z_y,z_{xy},z_{yy})\) \(l\) times in \(y\) and use Lemma 4.1. The derivatives of order \(l\) of the four variables are \(u_x,u_y,u_{xy},u_{yy}\), and those of order \(l-1\) are \(\partial_y^{l-1}z_x,\partial_y^{l-1}z_y,u_x,u_y\). With Lemma 1.1,
\[
\begin{aligned}
u_{xx}&=2q\,u_{xy}-(q^2+a)\,u_{yy}\\
&\quad+P_{z_x}u_x+P_{z_y}u_y+2l\,q_y\,u_x\\
&\quad-l\,(q^2+a)_y\,u_y+R_l .
\end{aligned}
\]
For every function \(w\),
\[
\begin{aligned}
D^2w&=w_{xx}-2q\,w_{xy}+q^2w_{yy}\\
&\quad-(Dq)\,w_y,
\end{aligned}
\]
by expanding \((\partial_x-q\partial_y)(w_x-qw_y)\). So \(u_{xx}-2qu_{xy}+q^2u_{yy}=D^2u+(Dq)u_y\). Insert this and \(u_x=Du+qu_y\):
\[
\begin{aligned}
&D^2u+a\,u_{yy}-(P_{z_x}+2lq_y)\,Du\\
&\quad+\bigl(Dq-P_{z_x}q-P_{z_y}+l\,a_y\bigr)u_y=R_l .
\end{aligned}
\]
The terms \(-2lqq_y\) and \(l(q^2)_y\) have cancelled. By Theorem 3.1 and \(a_y=K_yG+KG_y\), the coefficient of \(u_y\) is \((l+1)K_yG+K(\rho_1-\rho_2+lG_y)\). \(\blacksquare\)

## 6. Flow coordinates

Let \(W\) be an open rectangle in a plane with the coordinates \(t,s\) that contains a point with \(t=0\), and suppose that there is a smooth function \(y(t,s)\) on \(W\) with
\[
y_t(t,s)=-q(t,y(t,s)),\qquad y(0,s)=s,
\]
such that \(\Phi(t,s)=(t,y(t,s))\) maps \(W\) into \(U\). The curves \(s=\text{const}\) are the integral curves of \(D\).

**Lemma 6.1.** \(y_s=\exp\bigl(-\int_0^tq_y(r,y(r,s))\,dr\bigr)>0\), and \(\Phi\) is a diffeomorphism from \(W\) onto an open subset of \(U\). For a function \(w\) on \(U\), with \(\sigma=1/y_s\),
\[
\begin{aligned}
\partial_t(w\circ\Phi)&=(Dw)\circ\Phi,\\
\sigma\,\partial_s(w\circ\Phi)&=w_y\circ\Phi,\\
w_{yy}\circ\Phi&=\sigma^2\,\partial_s^2(w\circ\Phi)\\
&\quad+\sigma\sigma_s\,\partial_s(w\circ\Phi).
\end{aligned}
\]

**Proof.** Differentiating the equation for \(y\) in \(s\) gives \((y_s)_t=-q_y(t,y)\,y_s\) with \(y_s(0,s)=1\); this linear equation has the stated solution. For fixed \(t\), \(s\mapsto y(t,s)\) is strictly increasing, so \(\Phi\) is injective; its matrix of first derivatives has the determinant \(y_s>0\), so it is a diffeomorphism onto an open set. By the chain rule \(\partial_t(w\circ\Phi)=(w_x+y_tw_y)\circ\Phi\), which is \((Dw)\circ\Phi\), and \(\partial_s(w\circ\Phi)=y_s\,w_y\circ\Phi\). Applying the second formula twice gives the last one. \(\blacksquare\)

In these coordinates \(D\) is \(\partial_t\) and \(\partial_y\) is \(\sigma\,\partial_s\). The function \(\sigma\) is the derivative of \(s\) in the direction of \(y\).

**Theorem 6.2.** In the situation of Theorem 5.1, the function \(u\circ\Phi\) on \(W\), again written \(u\), satisfies
\[
u_{tt}+A\,u_{ss}+B\,u_t+C\,u_s=R_l,
\]
where \(B\) and \(R_l\) are the functions of Theorem 5.1 composed with \(\Phi\), and, with \(K,G,\rho\) composed with \(\Phi\),
\[
\begin{gathered}
A=G_1K,\qquad G_1=G\sigma^2,\\
C=(l+1)A_s+K\rho_3,\\
\rho_3=\sigma\rho+G\,\sigma\sigma_s-(l+1)(G_1)_s .
\end{gathered}
\]

**Proof.** By Lemma 6.1, \(D^2u=u_{tt}\), \(Du=u_t\), \(u_y=\sigma u_s\) and \(u_{yy}=\sigma^2u_{ss}+\sigma\sigma_su_s\). So Theorem 5.1 becomes the stated equation with \(A=a\sigma^2=KG\sigma^2\) and
\[
C=KG\,\sigma\sigma_s+\sigma\bigl((l+1)K_yG+K\rho\bigr).
\]
By Lemma 6.1, \(K_y\circ\Phi=\sigma\,\partial_s(K\circ\Phi)\). Hence \(A_s=G_1K_s+K(G_1)_s\), which is \(G\sigma K_y+K(G_1)_s\), so \((l+1)\sigma GK_y\) equals \((l+1)A_s-(l+1)K(G_1)_s\). \(\blacksquare\)

Where \(K>0\) the operator \(\partial_t^2+A\,\partial_s^2\) is elliptic, and where \(K<0\) it is hyperbolic, because \(G_1>0\) as long as \(E>0\). On the curve \(K=0\) the equation reduces to
\[
u_{tt}+B\,u_t+(l+1)A_s\,u_s=R_l .
\]
The estimate of [OpenAI-I, Section 3] uses the sign of \(A_s\) on this curve, which is the sign of \(K_y\), and the factor \(l+1\).

## 7. Exercises

**7.1.** Let \(g\) be the Euclidean metric \(dx^2+dy^2\) and \(z=\tfrac12y^2\). Check that the assumptions of Section 1 hold, and compute \(q\), \(D\), \(G\), \(P\) and both sides of the identities of Lemma 1.1 and Theorem 3.1.

**7.2.** Show that \(D^2w=w_{xx}-2qw_{xy}+q^2w_{yy}-(Dq)w_y\) for every function \(w\), and that in the equation of Theorem 5.1 the second-order part is \(u_{xx}-2qu_{xy}+(q^2+a)u_{yy}\). For which sign of \(K\) is this part elliptic?

**7.3.** Let \(l\ge7\). Show that in every term of the sum \(G_l\) of Lemma 4.1 at most one of the numbers \(k_j\) is larger than \(l/2\), and that at most one is at least \(l-3\).

**7.4.** Verify Lemma 2.2 for the metric \(dX^2+f^2\,dY^2\) with \(f=\cosh X\) and the function \(z=Y\), for \((i,j,k)=(1,1,2)\).

## 8. Solutions

**7.1.** All Christoffel symbols vanish and \(K=0\). \(H\) is the matrix of the second derivatives: \(H_{yy}=1\), the other entries are \(0\). The height equation reads \(0=0\). \(E=1-y^2\). \(q=0\), \(D=\partial_x\), \(G=1-y^2\), \(a=0\), and \(P=z_{xy}^2/z_{yy}\) with \(P_{z_{xy}}=2z_{xy}/z_{yy}=0=2q\), \(P_{z_{yy}}=-z_{xy}^2/z_{yy}^2=0\), \(P_{z_i}=0\). In Theorem 3.1 both sides are \(0\).

**7.2.** Expanding gives
\[
\begin{aligned}
&(\partial_x-q\partial_y)(w_x-qw_y)\\
&\quad=w_{xx}-q_xw_y-qw_{xy}\\
&\qquad-qw_{xy}+qq_yw_y+q^2w_{yy},
\end{aligned}
\]
and \(-q_x+qq_y=-Dq\). The second-order part of \(D^2u+a\,u_{yy}\) is therefore \(u_{xx}-2qu_{xy}+(q^2+a)u_{yy}\). Its determinant is \((q^2+a)-q^2=a=KG\), so it is elliptic where \(K>0\), if \(G>0\).

**7.3.** The \(k_j\) are at least \(1\) and their sum is at most \(l\), so two of them cannot both be larger than \(l/2\). If two were at least \(l-3\), the sum would be at least \(2l-6>l\) for \(l\ge7\).

**7.4.** With the coordinates \(X,Y\) numbered \(1,2\): \(z_1=0\), \(z_2=1\), \(K=-1\), and the Christoffel symbols of Lemma 3.1 of the lesson on heights are \(\Gamma^1_{22}=-ff'\), \(\Gamma^2_{12}=f'/f\), \(\Gamma^2_{22}=0\). So \(H_{ij}=-\Gamma^2_{ij}\): \(H_{11}=0\), \(H_{12}=-f'/f\), \(H_{22}=0\). Then
\[
\begin{aligned}
T_{112}&=\partial_2H_{11}-2\,\Gamma^r_{21}H_{r1}\\
&=-2\,\Gamma^2_{21}H_{21}=\frac{2f'^2}{f^2},\\
T_{121}&=\partial_1H_{12}-\Gamma^r_{11}H_{r2}-\Gamma^r_{12}H_{1r}\\
&=-\frac{f''f-f'^2}{f^2}-\Gamma^2_{12}H_{12}\\
&=-\frac{f''}f+\frac{2f'^2}{f^2}.
\end{aligned}
\]
The difference is \(T_{112}-T_{121}=f''/f=1\). The right side of Lemma 2.2 for \((i,j,k)=(1,1,2)\) is \(K(g_{12}z_1-g_{11}z_2)=-K=1\).

## References

- [OpenAI-I] OpenAI, *A smooth metric with no local isometric immersion into three-space*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026
