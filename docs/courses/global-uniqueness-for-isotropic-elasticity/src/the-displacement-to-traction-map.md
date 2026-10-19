# The displacement-to-traction map

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An elastic body occupies a bounded region \(\Omega\subset\mathbb R^3\). Its material is described by two functions, the Lamé moduli \(\lambda\) and \(\mu\). Prescribing the displacement of the boundary determines the displacement inside, and the forces that the body then exerts on its boundary are the tractions. The inverse problem asks whether the map from boundary displacements to boundary tractions determines both moduli everywhere inside. This course presents OpenAI's proof that it does, for smooth moduli on a bounded connected domain with smooth boundary, under the two positivity conditions that make the elastic energy positive [OpenAI-EL]. For the scalar conductivity equation this question was posed by Calderón [Calderón 1980]. For elasticity, Tan and Liu proved that the boundary map determines all derivatives of both moduli on the boundary [Tan–Liu 2023], and Imanuvilov and Yamamoto proved uniqueness of both moduli in two dimensions [Imanuvilov–Yamamoto 2015].

This lesson defines the map and states the theorem.

- The Lamé system and its energy (Section 1).
- Weak solutions and the Dirichlet problem (Section 2).
- The displacement-to-traction map (Section 3).
- The theorem, and the plan of the course (Section 4).

We use the Riesz–Fréchet representation theorem from the core course [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20) (Erdman, *Functional Analysis and Operator Algebras: An Introduction*, [Theorem 4.5.2](https://web.pdx.edu/~erdman/FAOA/functional_analysis_operator_algebras_pdf.pdf)), and Lebesgue integration and the Cauchy–Schwarz inequality.

## 1. The Lamé system and its energy

Throughout the course, \(\Omega\subset\mathbb R^3\) is a bounded connected open set with \(C^\infty\) boundary: every point of \(\partial\Omega\) has a neighbourhood \(W\) in which, after a rotation of coordinates, \(\Omega\cap W=\{x\in W:x_3<g(x_1,x_2)\}\) for a \(C^\infty\) function \(g\). A function on \(\overline\Omega\) is *smooth*, written \(f\in C^\infty(\overline\Omega)\), if it is the restriction of a \(C^\infty\) function on \(\mathbb R^3\). (For a domain with smooth boundary this agrees with the requirement that all derivatives on \(\Omega\) extend continuously to \(\overline\Omega\), by Seeley's extension theorem; the course uses only the definition by restriction.)

Let \(\lambda,\mu\in C^\infty(\overline\Omega)\) be real. For a vector field \(u=(u_1,u_2,u_3)\) write \(\nabla u\) for the matrix with entries \(\partial_ju_i\), and define the *strain*, the *stress* and the *Lamé operator* by
\[
\begin{aligned}e(u)&=\tfrac12\bigl(\nabla u+(\nabla u)^{\mathsf T}\bigr),\\ \sigma(u)&=\lambda(\operatorname{div}u)I\\&\quad+2\mu\,e(u),\\ (Lu)_i&=\sum_{j=1}^3\partial_j\sigma(u)_{ij}.\end{aligned}\tag{1.1}
\]
For two matrices put \(A:B=\operatorname{tr}(A^{\mathsf T}B)=\sum_{i,j}A_{ij}B_{ij}\) and \(|A|^2=\sum_{i,j}A_{ij}^2\). The moduli are assumed to satisfy
\[
\begin{gathered}\mu>0,\quad3\lambda+2\mu>0\\ \text{on }\overline\Omega .\end{gathered}\tag{1.2}
\]
Here \(\mu\) is the shear modulus and \(\lambda+\frac23\mu\) the bulk modulus. The next lemma shows that (1.2) makes the energy density positive.

**Lemma 1.1** (positive energy). Let \(\mu>0\) and \(3\lambda+2\mu>0\) be real numbers. For every real symmetric \(3\times3\) matrix \(A\),
\[
\begin{gathered}\lambda(\operatorname{tr}A)^2+2\mu|A|^2\ge c\,|A|^2,\\ c=\min(2\mu,\,3\lambda+2\mu)>0 .\end{gathered}
\]

*Proof.* Write \(A=\frac13(\operatorname{tr}A)I+A_0\), where \(A_0\) has trace zero. Since \(I:A_0=\operatorname{tr}A_0=0\), \(|A|^2=\frac13(\operatorname{tr}A)^2+|A_0|^2\). Hence
\[
\begin{aligned}&\lambda(\operatorname{tr}A)^2+2\mu|A|^2\\&\quad=\frac{3\lambda+2\mu}3(\operatorname{tr}A)^2+2\mu|A_0|^2\\&\quad\ge c\Bigl(\frac13(\operatorname{tr}A)^2+|A_0|^2\Bigr)\\&\quad=c|A|^2 .\qquad\square\end{aligned}
\]

As \(\overline\Omega\) is compact and the moduli are continuous, the number \(c_0=\min_{\overline\Omega}\min(2\mu,3\lambda+2\mu)\) is positive. The conditions (1.2) also give \(\lambda+\mu>\mu/3>0\), since \(\lambda>-\frac23\mu\).

## 2. Weak solutions and the Dirichlet problem

Let \(H^1(\Omega;\mathbb R^3)\) be the space of fields \(u\in L^2(\Omega;\mathbb R^3)\) whose distributional first derivatives \(\partial_ju\) belong to \(L^2(\Omega;\mathbb R^3)\), with the norm \(\|u\|_{H^1}^2=\|u\|_{L^2}^2+\|\nabla u\|_{L^2}^2\). It is a Hilbert space: if \(u_n\to u\) and \(\partial_ju_n\to w_j\) in \(L^2\), then integration against a test function shows \(\partial_ju=w_j\). Let \(H^1_0(\Omega;\mathbb R^3)\) be the closure of \(C^\infty_c(\Omega;\mathbb R^3)\) in \(H^1\). On \(H^1(\Omega;\mathbb R^3)\) define the bounded symmetric bilinear form
\[
\begin{aligned}&B(u,v)\\&\ =\int_\Omega\bigl[\lambda(\operatorname{div}u)(\operatorname{div}v)\\&\qquad+2\mu\,e(u):e(v)\bigr]\,dx .\end{aligned}\tag{2.1}
\]
If \(u\) is \(C^2\) on a neighbourhood of \(\overline\Omega\) and \(\varphi\in C^\infty_c(\Omega;\mathbb R^3)\), then, as \(\sigma(u)\) is symmetric, \(\sigma(u):\nabla\varphi=\sigma(u):e(\varphi)\), which equals \(\lambda(\operatorname{div}u)(\operatorname{div}\varphi)+2\mu\,e(u):e(\varphi)\), and integration by parts gives
\[
\begin{aligned}&B(u,\varphi)\\&\quad=\int_\Omega\sigma(u):\nabla\varphi\,dx\\&\quad=-\int_\Omega(Lu)\cdot\varphi\,dx .\end{aligned}\tag{2.2}
\]
Accordingly, \(u\in H^1(\Omega;\mathbb R^3)\) is a *weak solution* of \(Lu=0\) if \(B(u,\varphi)=0\) for all \(\varphi\in C^\infty_c(\Omega;\mathbb R^3)\), and then, by continuity, for all \(\varphi\in H^1_0(\Omega;\mathbb R^3)\).

**Lemma 2.1** (Korn's identity with zero boundary values). For \(\varphi\in H^1_0(\Omega;\mathbb R^3)\),
\[
\begin{aligned}\int_\Omega|\nabla\varphi|^2\,dx&=2\int_\Omega|e(\varphi)|^2\,dx\\&\quad-\int_\Omega(\operatorname{div}\varphi)^2\,dx .\end{aligned}
\]

*Proof.* Both sides are continuous on \(H^1\), so it suffices to take \(\varphi\in C^\infty_c\). Expanding the square, \(2|e(\varphi)|^2=|\nabla\varphi|^2+\sum_{i,j}\partial_j\varphi_i\,\partial_i\varphi_j\). Two integrations by parts give \(\int\partial_j\varphi_i\,\partial_i\varphi_j=\int\partial_i\varphi_i\,\partial_j\varphi_j\), and summing over \(i,j\) gives \(\int(\operatorname{div}\varphi)^2\). \(\square\)

**Lemma 2.2** (Poincaré inequality). If \(\Omega\subset\{x:|x_1|<\rho\}\), then \(\|\varphi\|_{L^2}\le2\rho\|\partial_1\varphi\|_{L^2}\) for \(\varphi\in H^1_0(\Omega;\mathbb R^3)\).

*Proof.* For \(\varphi\in C^\infty_c(\Omega)\), extended by zero, \(\varphi(x)=\int_{-\rho}^{x_1}\partial_1\varphi(t,x_2,x_3)\,dt\), so by Cauchy–Schwarz \(|\varphi(x)|^2\le2\rho\int_{-\rho}^{\rho}|\partial_1\varphi(t,x_2,x_3)|^2dt\). Integrating over \(|x_1|<\rho\) and over \((x_2,x_3)\) gives \(\|\varphi\|^2\le4\rho^2\|\partial_1\varphi\|^2\). Both sides are continuous on \(H^1\). \(\square\)

**Proposition 2.3** (the Dirichlet problem). Let \(v\in H^1(\Omega;\mathbb R^3)\). There is exactly one weak solution \(u\) of \(Lu=0\) with \(u-v\in H^1_0(\Omega;\mathbb R^3)\). It depends only on the class of \(v\) modulo \(H^1_0\), and \(\|u\|_{H^1}\le C\|v\|_{H^1}\) with \(C\) independent of \(v\).

*Proof.* For \(\varphi\in H^1_0\), Lemma 1.1 applied pointwise to \(A=e(\varphi)\), then Lemma 2.1 and Lemma 2.2 give
\[
\begin{aligned}B(\varphi,\varphi)&\ge c_0\|e(\varphi)\|_{L^2}^2\\&\ge\frac{c_0}2\|\nabla\varphi\|_{L^2}^2\ge c_1\|\varphi\|_{H^1}^2,\\ c_1&=\frac{c_0}{2(1+4\rho^2)} .\end{aligned}
\]
So \(B\) is an inner product on \(H^1_0\) whose norm is equivalent to the \(H^1\) norm, and \(H^1_0\) is a Hilbert space for it. The functional \(\varphi\mapsto-B(v,\varphi)\) is bounded on this space, and the Riesz–Fréchet theorem gives \(w\in H^1_0\) with \(B(w,\varphi)=-B(v,\varphi)\) for all \(\varphi\in H^1_0\). Then \(u=v+w\) is a weak solution with \(u-v\in H^1_0\). If \(u'\) is another one, \(z=u-u'\in H^1_0\) satisfies \(B(z,\varphi)=0\) for all \(\varphi\in H^1_0\), and \(\varphi=z\) gives \(z=0\). If \(v'-v\in H^1_0\), the solution for \(v'\) also differs from \(v\) by an element of \(H^1_0\), so it equals \(u\). Finally \(c_1\|w\|_{H^1}^2\le B(w,w)=-B(v,w)\), and \(-B(v,w)\le C_B\|v\|_{H^1}\|w\|_{H^1}\), where \(C_B\) bounds \(B\). \(\square\)

## 3. The displacement-to-traction map

The space of *boundary displacements* is the quotient Hilbert space
\[
\mathcal T=H^1(\Omega;\mathbb R^3)/H^1_0(\Omega;\mathbb R^3).
\]
The class \([v]\) of a field \(v\) records its behaviour at the boundary: two fields have the same class exactly when their difference is a limit of fields vanishing near \(\partial\Omega\). For \(f\in\mathcal T\) let \(u_f\) be the weak solution of Proposition 2.3 with \(u_f\in f\).

**Definition 3.1.** The *displacement-to-traction map* \(\Lambda=\Lambda_{\lambda,\mu}\) is the bounded linear map from \(\mathcal T\) to its dual given by, for any \(v\in g\),
\[
\begin{aligned}&\langle\Lambda f,g\rangle=B(u_f,v)\\&\ =\int_\Omega\bigl[\lambda(\operatorname{div}u_f)(\operatorname{div}v)\\&\qquad+2\mu\,e(u_f):e(v)\bigr]\,dx .\end{aligned}\tag{3.1}
\]
The right side does not depend on the choice of \(v\in g\), since two choices differ by an element of \(H^1_0\) and \(u_f\) is a weak solution. It is bounded by \(C_B\,C\,\|f\|\,\|v\|_{H^1}\), and taking the infimum over \(v\in g\) bounds it by a constant times \(\|f\|\,\|g\|\). Taking \(v=u_g\) shows that \(\langle\Lambda f,g\rangle=B(u_f,u_g)=\langle\Lambda g,f\rangle\).

If \(u_f\) is \(C^2\) up to the boundary and \(v\in g\) is \(C^1\) up to the boundary, the divergence theorem gives
\[
\langle\Lambda f,g\rangle=\int_{\partial\Omega}\bigl(\sigma(u_f)n\bigr)\cdot v\,dS ,
\]
with \(n\) the outward unit normal: \(\Lambda f\) is the boundary force, the traction, exerted by the displacement \(u_f\). This interpretation is not used in the proofs.

The trace theorem for a domain with smooth boundary identifies \(\mathcal T\) with the Sobolev space \(H^{1/2}(\partial\Omega;\mathbb R^3)\), the class \([v]\) of a field that is continuous up to the boundary corresponding to its boundary values \(v|_{\partial\Omega}\), and the dual of \(\mathcal T\) with \(H^{-1/2}(\partial\Omega;\mathbb R^3)\). In this form \(\Lambda\) is the displacement-to-traction map \(H^{1/2}(\partial\Omega;\mathbb R^3)\to H^{-1/2}(\partial\Omega;\mathbb R^3)\), and its equality for two pairs of moduli means the same in either description. The course works with \(\mathcal T\) and does not use this identification.

All identities in the course are extended complex-linearly to complex fields. In particular \(B\) and \(\Lambda\) extend complex-bilinearly to \(H^1(\Omega;\mathbb C^3)=H^1(\Omega;\mathbb R^3)\oplus iH^1(\Omega;\mathbb R^3)\), and two real maps \(\Lambda\) agree exactly when their complex-linear extensions agree. Products of complex vectors such as \(a\cdot b=\sum_ia_ib_i\) are complex bilinear; Hermitian inner products are used only for norms.

## 4. The theorem, and the plan of the course

**Theorem 4.1** ([OpenAI-EL, Theorem 1.1]). Let \(\Omega\subset\mathbb R^3\) be a bounded connected open set with \(C^\infty\) boundary. For \(j=1,2\) let \(\lambda_j,\mu_j\in C^\infty(\overline\Omega)\) be real with \(\mu_j>0\) and \(3\lambda_j+2\mu_j>0\) on \(\overline\Omega\). If \(\Lambda_{\lambda_1,\mu_1}=\Lambda_{\lambda_2,\mu_2}\), then \(\lambda_1=\lambda_2\) and \(\mu_1=\mu_2\) on \(\overline\Omega\).

The moduli need not be analytic or close to constants, and agreement near the boundary is not assumed. The proof is given in [The null conic and the recovery of the moduli](the-null-conic-and-the-recovery-of-the-moduli.md). Four results from the literature enter as named hypotheses, each stated where it is used: the determination of the boundary derivatives of the moduli [Tan–Liu 2023], interior regularity for elliptic systems, a Carleman estimate for the Laplacian [Salo–Tzou 2009], and the existence of holomorphic frames over a disk.

Diao and Durdiev proved the same theorem independently [Diao–Durdiev 2026, Theorem 1.1]. Both proofs reduce the comparison of the two pairs of moduli to the comparison of transport equations over the null directions, but they reach it differently. Diao and Durdiev derive complete families of holomorphically weighted \(3\times3\) matrix moments from Betti's reciprocity identity for exact elastic solutions, and build the relative transport from these moments by a Cauchy–Plemelj factorization; the course, following [OpenAI-EL], transfers solutions from one pair of moduli to the other and passes to weak limits [Diao–Durdiev 2026, Section 1.2]. Section 1.2 of [Diao–Durdiev 2026] also surveys the earlier three-dimensional results, which assume the shear modulus close to a constant or a special structure of it.

The course follows the proof in six further steps.

- [Boundary jets and the transfer of solutions](boundary-jets-and-the-transfer-of-solutions.md): the boundary map determines the moduli to infinite order at the boundary, so both pairs extend to \(\mathbb R^3\) with the same values outside \(\Omega\); every solution for the first pair near \(\overline\Omega\) then has a solution for the second pair that agrees with it outside \(\Omega\).
- [An augmented system and a Carleman estimate](an-augmented-system-and-a-carleman-estimate.md): adjoining the divergence \(d=\operatorname{div}u\) as an unknown turns \(L\) into a system with principal part the Laplacian, which satisfies an estimate with the weight \(e^{\tau\theta\cdot x}\) for a complex vector \(\theta\) with \(\theta\cdot\theta=0\).
- [Planar transport equations](planar-transport-equations.md): equations \(\partial_{\bar z}V=AV\) on disks, their invertible solutions, and a uniqueness and estimate theorem for solutions with compact support.
- [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md): solutions \(u=e^{\tau\theta\cdot x}(a_0+O(\tau^{-1}))\) of \(Lu=0\), whose leading displacement and divergence \((a_0,b_0)\) solve a transport equation and can be prescribed as any local solution of it.
- [Matching the transports](matching-the-transports.md): transferring these solutions to the second pair and passing to the limit \(\tau\to\infty\) compares the two transport equations by a field \(G\) that depends holomorphically on the direction \(\theta\).
- [The null conic and the recovery of the moduli](the-null-conic-and-the-recovery-of-the-moduli.md): the directions form a conic in the complex projective plane, the geometry of a bundle over it forces \(G\) to be the identity, and equality of the transport equations determines both moduli.

## 5. Exercises

**5.1.** Show that for constant \(\lambda,\mu\), \(Lu=\mu\Delta u+(\lambda+\mu)\nabla(\operatorname{div}u)\).

**5.2.** Show that Lemma 1.1 fails for \(A=I\) when \(3\lambda+2\mu<0\).

**5.3.** For \(u(x)=(x_2,-x_1,0)\) compute \(e(u)\) and \(\sigma(u)\). Why does this not contradict Lemma 2.1 and Proposition 2.3?

**5.4.** Show that \(\langle\Lambda f,f\rangle\ge0\) for real \(f\), with equality exactly when \(f\) is the class of a rigid motion \(x\mapsto Mx+b\), \(M\) antisymmetric. (You may use that \(e(u)=0\) on a connected open set forces \(u(x)=Mx+b\) with \(M\) antisymmetric.)

**5.5.** Show that the trace of a weak solution determines it: if \(u_1,u_2\) are weak solutions of \(Lu=0\) with \(u_1-u_2\in H^1_0\), then \(u_1=u_2\).

## 6. Solutions

**5.1.** For constant moduli,
\[
\begin{aligned}\sum_j\partial_j\sigma(u)_{ij}&=\lambda\partial_i\operatorname{div}u\\&\quad+\mu\sum_j(\partial_j^2u_i+\partial_i\partial_ju_j)\\&=\mu\Delta u_i+(\lambda+\mu)\partial_i\operatorname{div}u .\end{aligned}
\]

**5.2.** For \(A=I\), \(\operatorname{tr}A=3\) and \(|A|^2=3\), so the left side is \(9\lambda+6\mu=3(3\lambda+2\mu)\), which is negative, while \(c|A|^2\) would have to be positive.

**5.3.** \(\nabla u=\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}\) is antisymmetric, so \(e(u)=0\), \(\operatorname{div}u=0\) and \(\sigma(u)=0\). This field does not vanish on \(\partial\Omega\), so it is not in \(H^1_0\), and Lemma 2.1 does not apply to it. It is the weak solution of Proposition 2.3 for its own class, with \(\Lambda[u]=0\).

**5.4.** \(\langle\Lambda f,f\rangle=B(u_f,u_f)\ge c_0\|e(u_f)\|^2\ge0\) by Lemma 1.1. Equality forces \(e(u_f)=0\), so \(u_f(x)=Mx+b\) with \(M\) antisymmetric, and \(f=[u_f]\) is the class of a rigid motion. Conversely, a rigid motion \(r\) has \(e(r)=0\) and \(\operatorname{div}r=0\), so \(B(r,v)=0\) for every \(v\); thus \(r\) is a weak solution, \(u_{[r]}=r\), and \(\langle\Lambda[r],[r]\rangle=B(r,r)=0\).

**5.5.** \(z=u_1-u_2\in H^1_0\) satisfies \(B(z,\varphi)=0\) for all \(\varphi\in H^1_0\), and \(\varphi=z\) with the coercivity in the proof of Proposition 2.3 gives \(z=0\).

## References

- [OpenAI-EL] OpenAI, *Global uniqueness for the smooth isotropic elasticity inverse problem*, OpenAI Math Release preprint, 24 September 2026, Section 1. https://github.com/openai/math/tree/main/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026
- [Calderón 1980] A. P. Calderón, *On an inverse boundary value problem*, Seminar on Numerical Analysis and its Applications to Continuum Physics, Sociedade Brasileira de Matemática, 1980, 65–73; reprinted in Comput. Appl. Math. 25 (2006), no. 2–3, 133–138. https://doi.org/10.1590/S0101-82052006000200002
- [Tan–Liu 2023] X. Tan, G. Liu, *Determining Lamé coefficients by elastic Dirichlet-to-Neumann map on a Riemannian manifold*, Inverse Problems 39 (2023), no. 9, 095004. https://arxiv.org/abs/2211.06650
- [Imanuvilov–Yamamoto 2015] O. Yu. Imanuvilov, M. Yamamoto, *Global uniqueness in inverse boundary value problems for the Navier–Stokes equations and Lamé system in two dimensions*, Inverse Problems 31 (2015), no. 3, 035004. https://arxiv.org/abs/1309.1694
- [Salo–Tzou 2009] M. Salo, L. Tzou, *Carleman estimates and inverse problems for Dirac operators*, Math. Ann. 344 (2009), no. 1, 161–184. https://arxiv.org/abs/0709.2282
- [Diao–Durdiev 2026] H. Diao, U. Durdiev, *Unique determination of the Lamé parameters in three dimensions*, arXiv:2610.14741 (October 2026). https://arxiv.org/abs/2610.14741
