# Matrix blocks and approximate product states

A normal positive functional that almost satisfies a modular relation at one matrix unit is close to a product functional on the matrix block and its commutant. We construct the relevant product directly, prove quantitative bounds, and explain how the estimates combine for commuting matrix blocks.

The matrix-unit orientation determines the weights. Throughout this lesson, \(u=e_{12}\), so \(uu^*=e_{11}\) and \(u^*u=e_{22}\). The functional relation \(\varphi u=\lambda u\varphi\) corresponds to matrix weights \(\lambda/(1+\lambda)\) and \(1/(1+\lambda)\), in that order.

We use the bounded operator and positivity facts proved in Bounded operator kernel, the normality and norm of vector functionals and bounded module actions, and, for the vector consequence, the standard-cone norm inequality. All sums defining the matrix coordinates and expectations below are finite.

## 1. Matrix coordinates over the commutant

Let \(M\ne0\) be a von Neumann algebra and let \(u\in M\) be a partial isometry with


\[
u^*u+uu^*=1.
\]


Put \(e=u^*u\), \(f=uu^*\). These projections are complementary, so \(u= fue\) and \(u^2=0\). The elements


\[
e_{11}=f,\quad e_{12}=u,\quad
e_{21}=u^*,\quad e_{22}=e
\]


satisfy \(e_{ij}e_{kl}=\delta_{jk}e_{il}\), \(e_{ij}^*=e_{ji}\), and \(e_{11}+e_{22}=1\). They span a unital copy \(B\) of \(M_2(\mathbb C)\). Let \(N=B'\cap M\).

For \(x\in M\), define


\[
C_{ij}(x)=\sum_{k=1}^2e_{ki}xe_{jk}.
\tag{1}
\]


Each coefficient belongs to \(N\). Indeed, for every matrix unit,


\[
e_{ab}C_{ij}(x)=e_{ai}xe_{jb}=C_{ij}(x)e_{ab}.
\]


Moreover,


\[
x=\sum_{i,j=1}^2C_{ij}(x)e_{ij},
\qquad C_{ij}(ne_{rs})=\delta_{ir}\delta_{js}n
\quad(n\in N).
\tag{2}
\]


Both identities follow by multiplying the matrix units in (1). They prove existence and uniqueness of the expansion of \(x\) over \(N\).

The coefficient maps are contractions. To see this without an unspecified tensor norm, represent \(M\) faithfully on \(H\) and put \(K=fH\). The map


\[
W:H\longrightarrow K\oplus K,\qquad
W\eta=(f\eta,u\eta)
\]


is unitary, with inverse \((\alpha,\beta)\mapsto\alpha+u^*\beta\). For \(n\in N\), \(WnW^*\) is the diagonal matrix with both entries \(n|_K\). This representation of \(N\) on \(K\) is faithful and isometric: the two diagonal restrictions of \(n\) to \(fH\) and \(eH\) are unitarily equivalent through \(u\), and their maximum norm is \(\|n\|\). Direct calculation gives


\[
WxW^*=[C_{ij}(x)|_K]_{i,j=1}^2.
\]


Compression to a matrix entry therefore proves


\[
\|C_{ij}(x)\|\leq\|x\|.
\tag{3}
\]


Multiplication in (2) shows that \(x\mapsto[C_{ij}(x)]\) is a star isomorphism from \(M\) onto \(M_2(N)\). Its inverse is the finite sum in (2). Both maps are normal, since multiplication by fixed bounded operators is normal. This realizes the multiplication isomorphism \(N\bar\otimes B\cong M\) explicitly.

## 2. The weighted expectation and its product functional

Fix \(\lambda>0\), and put


\[
p_\lambda=\frac{\lambda}{1+\lambda},\qquad
q_\lambda=\frac1{1+\lambda}.
\]


Let \(\omega_\lambda\) be the state on \(B\) with diagonal weights \(p_\lambda,q_\lambda\) and zero off-diagonal values. Define


\[
E_\lambda(x)
=p_\lambda C_{11}(x)+q_\lambda C_{22}(x).
\tag{4}
\]


This is a faithful normal completely positive conditional expectation from \(M\) onto \(N\), of norm one. Here are the details. Each diagonal map in (1) is a sum of maps \(x\mapsto a^*xa\), hence is completely positive: its matrix amplification sends a positive matrix \([x_{rs}]\) to a sum of matrices \([a^*x_{rs}a]\), each positive by the defining quadratic-form test. Also \(C_{ii}(1)=1\), and \(C_{ii}(n)=n\) for \(n\in N\). Thus (4) is unital and fixes \(N\). Equations (1) and (3) give normality, contractivity and the bimodule identity


\[
E_\lambda(n_1xn_2)=n_1E_\lambda(x)n_2
\qquad(n_1,n_2\in N).
\]


Its norm is exactly one because it fixes the identity. For faithfulness, if \(x\geq0\) and \(E_\lambda(x)=0\), both positive terms \(C_{ii}(x)\) vanish. Their defining sums include \(e_{ii}xe_{ii}\), so \(x^{1/2}e_{ii}=0\) for \(i=1,2\). As the projections sum to one, \(x=0\).

For any \(\varphi\in M_*^+\), let


\[
\psi=\varphi\circ E_\lambda.
\tag{5}
\]


It is normal and positive, has the same value at the identity as \(\varphi\), and agrees with \(\varphi\) on \(N\). Furthermore


\[
\psi(nb)=\varphi(n)\omega_\lambda(b)
\qquad(n\in N,\ b\in B).
\tag{6}
\]


Indeed, (4) gives \(E_\lambda(ne_{ij})=\omega_\lambda(e_{ij})n\). The expansion (2) then proves (6), as well as uniqueness of the functional with those product values. Thus \(\psi\) is precisely \(\varphi|_N\otimes\omega_\lambda\) under the multiplication isomorphism. Its construction does not assume that \(\varphi\) is faithful or normalized. If \(\varphi\) is faithful, faithfulness of \(E_\lambda\) makes \(\psi\) faithful too.

## 3. Bounding the distance by one modular defect

Our functional actions are


\[
(\varphi u)(x)=\varphi(ux),\qquad
(u\varphi)(x)=\varphi(xu).
\]


Set


\[
F=\varphi u-\lambda u\varphi,\qquad \delta=\|F\|.
\]


For \(n\in N\), evaluation at \(nu^*\) gives


\[
F(nu^*)=\varphi(nf)-\lambda\varphi(ne).
\]


Consequently


\[
\begin{aligned}
|\varphi(nf)-p_\lambda\varphi(n)|
&\leq\frac{\delta}{1+\lambda}\|n\|,\\
|\varphi(ne)-q_\lambda\varphi(n)|
&\leq\frac{\delta}{1+\lambda}\|n\|.
\end{aligned}
\tag{7}
\]


For the off-diagonal terms there are two useful choices of test element. If \(0<\lambda<1\), then


\[
F(n)=(1-\lambda)\varphi(nu),
\]


so \(|\varphi(nu)|\leq\delta\|n\|/(1-\lambda)\). Positivity of \(\varphi\) gives
\(\varphi(nu^*)=\overline{\varphi(n^*u)}\), so the same bound holds with \(u^*\).

Now expand \(x=\sum n_{ij}e_{ij}\) using (2), with \(\|n_{ij}\|\leq\|x\|\). Its difference from the product functional is


\[
\begin{aligned}
(\varphi-\psi)(x)
={}&\varphi(n_{11}f)-p_\lambda\varphi(n_{11})\\
&+\varphi(n_{22}e)-q_\lambda\varphi(n_{22})\\
&+\varphi(n_{12}u)+\varphi(n_{21}u^*).
\end{aligned}
\]


The four coefficient bounds prove


\[
\|\varphi-\psi\|
\leq\left(\frac2{1+\lambda}+\frac2{1-\lambda}\right)\delta
=\frac4{1-\lambda^2}\delta,
\qquad 0<\lambda<1.
\tag{8}
\]


There is also a bound that remains finite at \(\lambda=1\). Test on the two diagonal compressions instead:


\[
F(ne)=\varphi(nu),\qquad
F(nf)=-\lambda\varphi(nu).
\]


These identities give, for every \(\lambda>0\),


\[
|\varphi(nu)|,\ |\varphi(nu^*)|
\leq\frac{\delta}{\max\{1,\lambda\}}\|n\|.
\tag{9}
\]


Repeating the four-term estimate yields


\[
\begin{gathered}
\|\varphi-\varphi|_N\otimes\omega_\lambda\|
\leq C_\lambda\|\varphi u-\lambda u\varphi\|,\\
C_\lambda=\frac2{1+\lambda}+\frac2{\max\{1,\lambda\}}.
\end{gathered}
\tag{10}
\]


For \(0<\lambda<1\), this improves the sufficient constant in (8); at \(\lambda=1\), it gives \(C_1=3\). No optimality of (10) is asserted. Both proofs apply to every bounded normal positive functional, including zero, in an arbitrary von Neumann algebra containing the specified matrix block.

## 4. Exact balance, stability and positive vectors

The product functional \(\psi\) in (5) satisfies the exact relation


\[
\psi u=\lambda u\psi.
\tag{11}
\]


For a direct check, if \(x=[n_{ij}]\), the weighted diagonal maps give


\[
E_\lambda(ux)=p_\lambda n_{21},\qquad
E_\lambda(xu)=q_\lambda n_{21}.
\]


Since \(p_\lambda=\lambda q_\lambda\), applying \(\varphi\) proves (11). It follows from (10) that


\[
\varphi u=\lambda u\varphi
\quad\Longleftrightarrow\quad
\varphi=\varphi|_N\otimes\omega_\lambda.
\tag{12}
\]


Moreover, bounded module actions and (11) give the complementary estimate


\[
\frac{\|\varphi u-\lambda u\varphi\|}{1+\lambda}
\leq\|\varphi-\psi\|
\leq C_\lambda\|\varphi u-\lambda u\varphi\|.
\tag{13}
\]


Indeed, \(F=(\varphi-\psi)u-\lambda u(\varphi-\psi)\), and \(\|u\|=1\). The correction map \(\varphi\mapsto\varphi E_\lambda\) is contractive on the whole predual and idempotent, since \(E_\lambda\) is a contractive projection. Its positive fixed points are exactly the balanced positive functionals in (12).

In any standard form, the representing positive vectors satisfy


\[
\|\xi_\varphi-\xi_\psi\|^2
\leq\|\varphi-\psi\|
\leq C_\lambda\delta.
\tag{14}
\]


The first inequality is the standard-cone norm inequality cited in the introduction, applicable also to nonfaithful functionals. Thus the correction is quantitative both in the predual and in its positive-vector realization.

For a finite family \(\varphi_j\), the same \(u\), \(N\) and \(E_\lambda\) work simultaneously, with each error controlled by its own defect. Combined with modular halving, this supplies simultaneous product approximations for the families appearing there.

## 5. Commuting blocks and accumulated errors

Let \(B_1,\ldots,B_r\subseteq M\) be mutually commuting unital matrix blocks. For each \(k\), choose a halving matrix unit \(u_k=e_{12}^{(k)}\), a parameter \(\lambda_k>0\), and the expectation \(E_k\) onto \(N_k=B_k'\cap M\) constructed above.

The maps \(E_k\) commute. Their explicit formulas (1) and (4) are finite sums of two-sided multiplications by elements of \(B_k\); the multipliers for different blocks commute, so the corresponding maps commute term by term. Their composition


\[
Q_r=E_1\cdots E_r
\]


is a normal unital completely positive projection of norm one onto


\[
N^{(r)}=\bigcap_{k=1}^rN_k.
\]


Indeed, commuting idempotents have a composition fixed by every factor, and every element in the intersection is fixed by the composition. The bimodule identities over \(N^{(r)}\) follow from those of each \(E_k\).

Each new block lies in the preceding commutant. Repeated application of the explicit coordinate isomorphism in Section 1 therefore identifies


\[
M\cong N^{(r)}\bar\otimes B_1\bar\otimes\cdots\bar\otimes B_r.
\]


On elementary products, \(Q_r\) applies the state \(\omega_{\lambda_k}\) to each block. Hence


\[
\varphi Q_r
=\varphi|_{N^{(r)}}\otimes
\omega_{\lambda_1}\otimes\cdots\otimes\omega_{\lambda_r}.
\tag{15}
\]


Put \(\delta_k=\|\varphi u_k-\lambda_ku_k\varphi\|\), measured against the original functional \(\varphi\). With \(Q_0=\mathrm{id}\), commutativity gives the telescoping identity


\[
\varphi-\varphi Q_r
=\sum_{k=1}^r(\varphi-\varphi E_k)Q_{k-1}.
\]


Every \(Q_{k-1}\) is contractive. Applying (10) to the original functional at each step proves


\[
\|\varphi-\varphi Q_r\|
\leq\sum_{k=1}^r C_{\lambda_k}\delta_k.
\tag{16}
\]


No estimate on a changed intermediate functional is required.

There is a useful limited infinite consequence. If the blocks form a sequence and


\[
\sum_{k=1}^\infty C_{\lambda_k}\delta_k<\infty,
\]


the same telescoping identity between indices \(r<s\) gives


\[
\|\varphi Q_s-\varphi Q_r\|
\leq\sum_{k=r+1}^sC_{\lambda_k}\delta_k.
\]


Thus \(\varphi Q_r\) converges in the Banach predual to a normal positive functional \(\psi_\infty\) with \(\psi_\infty(1)=\varphi(1)\). Positivity follows by evaluating the norm limit on positive elements. For every fixed \(k\), \(\psi_\infty E_k=\psi_\infty\), by passing to the limit from \(r\geq k\). For a fixed \(\lambda\), summability of the defects \(\delta_k\) alone is sufficient, because the coefficient \(C_\lambda\) is constant.

If \(N^{(\infty)}=\bigcap_kN_k\), \(n\in N^{(\infty)}\), and \(b\) belongs to the algebra generated by finitely many of the blocks, then


\[
\psi_\infty(nb)=\varphi(n)\omega(b),
\]


where \(\omega(b)\) is the finite product of the specified block states. For sufficiently large \(r\), the equality already holds for \(\varphi Q_r\), by (15). This proves the asserted limit relation. It does not assert that \(M\) is generated by \(N^{(\infty)}\) and the matrix blocks, or that \(\psi_\infty\) is faithful; neither follows from this norm-limit argument alone.

## 6. An exact two-dimensional calculation

Take \(M=M_2(\mathbb C)\), \(u=e_{12}\), and


\[
\varphi(x)=\operatorname{Tr}(hx),\qquad
h=\begin{pmatrix}a&z\\\overline z&b\end{pmatrix}\geq0.
\]


Then \(N=\mathbb C1\), and the product correction has density


\[
h_0=\frac{a+b}{1+\lambda}
\begin{pmatrix}\lambda&0\\0&1\end{pmatrix}.
\]


Set \(t=a-\lambda b\). The difference density is


\[
h-h_0=
\begin{pmatrix}t/(1+\lambda)&z\\\overline z&-t/(1+\lambda)\end{pmatrix}.
\]


Its eigenvalues are \(\pm\sqrt{t^2/(1+\lambda)^2+|z|^2}\), so


\[
\|\varphi-\varphi E_\lambda\|
=2\sqrt{\frac{t^2}{(1+\lambda)^2}+|z|^2}.
\]


The defect functional has density


\[
d=hu-\lambda uh
=\begin{pmatrix}-\lambda\overline z&t\\0&\overline z\end{pmatrix}.
\]


For a two-by-two matrix, the sum of its singular values satisfies
\((\operatorname{Tr}|d|)^2=\operatorname{Tr}(d^*d)+2|\det d|\). This follows by writing its two nonnegative singular values as \(s_1,s_2\), using \(s_1^2+s_2^2=\operatorname{Tr}(d^*d)\) and \(s_1s_2=|\det d|\). Consequently


\[
\|\varphi u-\lambda u\varphi\|
=\sqrt{t^2+(1+\lambda)^2|z|^2}.
\]


Here the norm of a matrix functional with density \(d\) is \(\operatorname{Tr}|d|\). To check it, diagonalize \(d^*d\); the normalized images under \(d\) of eigenvectors with positive eigenvalues are orthonormal, and completing them to an orthonormal basis gives \(d=U\operatorname{diag}(s_1,s_2)V^*\) with unitaries \(U,V\). Cyclicity of the finite matrix trace bounds \(|\operatorname{Tr}(dx)|\) by \((s_1+s_2)\|x\|\), and \(x=VU^*\) attains that bound. We therefore have the exact identity


\[
\|\varphi-\varphi E_\lambda\|
=\frac2{1+\lambda}
\|\varphi u-\lambda u\varphi\|.
\tag{17}
\]


In particular, at \(\lambda=1\) the two norms are equal. The singularity of the sufficient constant in (8) is a feature of that particular estimate, not an obstruction to product approximation at equal matrix weights. Formula (17) also checks both the orientation and normalization of the product state.
