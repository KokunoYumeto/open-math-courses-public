# The trace form and the residue data

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The vector fields of the next lesson are prescribed to first order by a pair \(P=(P_1,P_2)\) of meromorphic sections of the line bundle \(\theta=2L\) on the curve \(C\) of genus 21, with simple poles at the six marked points. Their residues must satisfy a pointwise normalization at each point and one identity summed over all six. This lesson constructs \(P\) (Proposition 3.2). The constraint on the residues comes from a quadratic space \(\mathcal W\) of dimension two, defined by the trace form of the degree-four map \(f:C\to\mathbb P^1\) (Section 1). Section 2 identifies \(\mathcal W\), with its scalar and sign, with the quadratic space \(H^0(\Gamma,\Phi)\) of the elliptic curve, through principal parts at the contact points; the six vectors chosen on the elliptic curve then prescribe the residues.

**Prerequisites.** [*An elliptic curve on the quadric*](an-elliptic-curve-on-the-quadric.md), [*A curve of genus 21 with a fourth root of its canonical bundle*](a-curve-of-genus-21-with-a-fourth-root-of-its-canonical-bundle.md) and [*Traces, residues and vector bundles on the projective line*](traces-residues-and-vector-bundles-on-the-projective-line.md), with their notation; in particular Proposition 3.3 of the second and Lemma 3.1, Proposition 3.2, Theorem 4.2 and Proposition 5.1 of the third.

**Setting.** The curve \(C\subset\Sigma\), the divisor \(Z=q_1+\cdots+q_6\), the canonical section \(\xi\) of \(\mathcal O_C(Z)\), the line bundles \(H\), \(L=H+Z\), \(\theta=2L\), the isomorphism \(4L\cong K_C\) normalized by (2.3) of the lesson on the curve of genus 21, and the basis \(u=(u_1,u_2)\) of \(H^0(C,H)\) of Proposition 3.3 there. Put
\[
\begin{gathered}
\Lambda=\theta+H=3H+2Z,\\
f:C\to\mathbb P^1\ \text{the map defined by }u,\\
\eta_C=u_1\,du_2-u_2\,du_1\\
\in H^0(C,K_C+2H).
\end{gathered}
\]
The fixed isomorphism \(2\Lambda=2H+4L\cong K_C+2H\) is used throughout; through it, for local sections \(T_1,T_2\) of \(\Lambda\), \(T_1T_2/\eta_C\) is a meromorphic function. On \(\Gamma\) there are the logarithmic form \(\Omega\), its residue \(\omega\), the section \(\eta_\Gamma\), the quadratic form \(Q\) on \(H^0(\Gamma,\Phi)^*\), the section \(\beta\) of \(M\) with divisor \(Z\), and the vectors \(w_j\).

## 1. A two-dimensional quadratic space

**Lemma 1.1 (the trace form).** Let \(E=f_*\Lambda\), a vector bundle of rank four on \(\mathbb P^1\).

1. The pairing \(B(T_1,T_2)=\operatorname{Tr}(T_1T_2/\eta_C)\) is a perfect symmetric pairing \(E\otimes E\to\mathcal O_{\mathbb P^1}\).
2. \(E\cong\mathcal O(3)\oplus\mathcal O^{\oplus2}\oplus\mathcal O(-3)\). Multiplication by \(\xi^2\), \(\mathcal O(3)\to E\), \(s\mapsto\xi^2f^*s\), maps \(\mathcal O(3)\) isomorphically onto a subbundle \(\mathcal P\) that is a summand of this type, and \(H^0(\mathcal P)=\xi^2H^0(C,3H)\).
3. On global sections \(B\) takes constant values; its radical is \(\xi^2H^0(C,3H)\), and it induces a nondegenerate symmetric form \(\langle\ ,\ \rangle\) on
\[
\begin{gathered}
\mathcal W=H^0(C,\Lambda)/\xi^2H^0(C,3H),\\
\dim\mathcal W=2 .
\end{gathered}
\]
For every \(x\in\mathbb P^1\), evaluation is an isometry of \(\mathcal W\) onto \((\mathcal P^\perp/\mathcal P)_x\).
4. Let \(q\in Z\). Choose a local frame \(\mathfrak f\) of \(H\), a local frame \(\tau\) of \(\Lambda\) and a parameter \(z\) at \(q\), and write \(\tau^2=s(z)\,dz\,\mathfrak f^2\) and \(\eta_C=\mathcal E(z)\,dz\,\mathfrak f^2\). The functional \(\ell_q:T\mapsto(T/\tau)(q)\) on \(H^0(C,\Lambda)\) descends to \(\mathcal W\), and for the dual form on \(\mathcal W^*\)
\[
\ell_q^2=\frac{\mathcal E(q)}{s(q)}\ne0 .
\tag{1.1}
\]

Here the *dual form* on \(\mathcal W^*\) is \(\lambda\cdot\mu=\langle\lambda^\sharp,\mu^\sharp\rangle\), where \(\lambda^\sharp\in\mathcal W\) is defined by \(\langle\lambda^\sharp,\cdot\rangle=\lambda\); we write \(\lambda^2=\lambda\cdot\lambda\). The reciprocal in (1.1) reflects the passage from \(\langle\ ,\ \rangle\) to the dual form.

**Proof.** (1) This is Proposition 5.1 of the lesson on traces, with \(n=4\).

(2) By Theorem 4.2 of the lesson on traces, \(E\cong\bigoplus_i\mathcal O(a_i)\), and since \(E\cong E^\vee\) by (1), the \(a_i\) occur in pairs \(\{a,-a\}\). By the projection formula, \(E(-k)=f_*(\Lambda-kH)\), and \(H^0(\mathbb P^1,f_*B)=H^0(C,B)\). Proposition 3.3 of the lesson on the curve of genus 21 gives
\[
\begin{gathered}
h^0(E(-1))=h^0(C,\theta)=3,\\
h^0(E(-2))=h^0(C,H+2Z)=2 .
\end{gathered}
\]
A summand \(\mathcal O(a)\) with \(a>0\) contributes \(a\) to the first number and \(a-1\) to the second, and a summand with \(a\le0\) contributes nothing to either. Hence there is exactly one positive \(a_i\), equal to \(3\); by the pairing there is exactly one negative one, \(-3\), and the remaining two are \(0\). The map \(\mathcal O(3)\to E\) given by \(\xi^2\) is nonzero. Its components into \(\mathcal O\) and \(\mathcal O(-3)\) vanish, since \(\operatorname{Hom}(\mathcal O(3),\mathcal O(b))=H^0(\mathcal O(b-3))=0\) for \(b\le0\), and its component into \(\mathcal O(3)\) is a nonzero constant. So its image \(\mathcal P\) is the summand \(\mathcal O(3)\), a subbundle. The pullback \(H^0(\mathbb P^1,\mathcal O(3))\to H^0(C,3H)\) is injective, and both spaces have dimension four (Proposition 3.3(3) there), so \(H^0(\mathcal P)=\xi^2H^0(C,3H)\).

(3) The pairing of \(\mathcal P\) with itself is a map \(\mathcal O(6)\to\mathcal O\), hence zero, and the pairing of \(\mathcal P\) with the summands \(\mathcal O\) is a map \(\mathcal O(3)\to\mathcal O\), hence zero. By perfection, \(\mathcal P^\perp=\ker(E\to\mathcal P^\vee)\) is a subbundle of rank three; it contains the rank-three subbundle \(\mathcal P\oplus\mathcal O^{\oplus2}\), so they are equal, the quotient of one by the other being a torsion subsheaf of the torsion-free sheaf \(E/(\mathcal P\oplus\mathcal O^{\oplus2})\). Since \(\mathcal P\) is isotropic and \((\mathcal P^\perp)^\perp=\mathcal P\), the form induced on \(\mathcal P^\perp/\mathcal P\cong\mathcal O^{\oplus2}\) is perfect; it is a nondegenerate constant symmetric matrix, because \(\operatorname{Hom}(\mathcal O,\mathcal O)=\mathbb C\). The quotient \(E/\mathcal P^\perp\cong\mathcal O(-3)\) has no global sections, so \(H^0(E)=H^0(\mathcal P^\perp)\); and \(H^1(\mathcal P)=0\). Hence
\[
\begin{aligned}
\mathcal W&=H^0(E)/H^0(\mathcal P)\\
&=H^0(\mathcal P^\perp/\mathcal P)\cong\mathbb C^2 ,
\end{aligned}
\]
the values of \(B\) on global sections are constants, \(H^0(\mathcal P)\) lies in the radical, and the induced form on \(\mathcal W\) is the constant nondegenerate form, which evaluation at any \(x\) carries isometrically to the fibre.

(4) Let \(x=f(q)\). By Lemma 1.1 of the lesson on traces, the fibre \(E_x\) is the direct sum of its pieces at the points over \(x\), and \(B_x\) is the orthogonal sum of their forms. Since \(f\) is unramified at \(q\) (Proposition 3.3(2) of the lesson on the curve of genus 21), the piece at \(q\) is the line \(\Lambda_q\), with form
\[
B(t_1\tau,t_2\tau)=t_1t_2\,\frac{s(q)}{\mathcal E(q)} .
\]
The functional \(\ell_q\) on \(E_x\) is the coefficient at \(q\), zero on the other pieces. Its metric dual is \(v=(\mathcal E(q)/s(q))\,\tau(q)\), since \(B(v,\tau(q))=1\), and \(B(v,v)=\mathcal E(q)/s(q)\). The functional \(\ell_q\) vanishes on \(\mathcal P_x\), whose elements are \(\xi^2\) times sections and vanish at \(q\); so \(v\in\mathcal P_x^\perp\), and \(\ell_q\) descends to \((\mathcal P^\perp/\mathcal P)_x\), with metric dual the class of \(v\) and the same square. Through the isometry of (3), this is (1.1) on \(\mathcal W\). Finally \(\mathcal E(q)\ne0\) because \(\eta_C\) vanishes only at ramification points (Section 5 of the lesson on traces), and \(s(q)\ne0\) because \(\tau^2\) is a frame. \(\square\)

## 2. Identification by principal parts

**Lemma 2.1 (comparison with the elliptic curve).** There is an isomorphism
\[
\iota:\mathcal W\xrightarrow{\ \sim\ }H^0(\Gamma,\Phi)
\]
such that, for every \(T\in H^0(C,\Lambda)\), the principal parts of \(T/\xi^2\) on \(C\) along \(2Z\) and of \(\iota([T])/\beta^2\) on \(\Gamma\) along \(2Z\) define the same functional on the common jet space \(H^0(2Z,(\Gamma+F)|_{2Z})\) through residues. It carries the projective evaluation at each \(q_j\) on \(\mathcal W\) to the projective evaluation at \(q_j\) on \(H^0(\Gamma,\Phi)\). Its dual \(\iota^*:H^0(\Gamma,\Phi)^*\to\mathcal W^*\) is an isometry from \(Q\) to the dual trace form.

**Proof.** *The common jet space.* Put \(N_\Sigma=\Gamma+F=\mathcal O(3,2)\), \(N_\Gamma=N_\Sigma|_\Gamma\), and \(D=2Z\). By Proposition 1.4 of the lesson on the curve of genus 21, \(D\) is the same subscheme of length twelve of \(\Sigma\) whether regarded on \(C\) or on \(\Gamma\); put \(\mathcal J=H^0(D,N_\Sigma|_D)\), of dimension twelve. The adjunction isomorphism \(\mathcal O(6,2)|_C\cong K_C\) gives \(N_\Sigma|_C\cong K_C-3H\), and \(\omega\) trivializes \(K_\Gamma\), so \(K_\Gamma+N_\Gamma\cong N_\Gamma\). Both jet spaces \(\mathrm J_D(K_C-3H)\) and \(\mathrm J_D(K_\Gamma+N_\Gamma)\) are thereby \(\mathcal J\).

*Principal parts.* By Lemma 3.1 of the lesson on traces, the residue pairings identify both
\[
\begin{gathered}
\mathrm{PP}^C=\mathrm{PP}_D(3H)\ \text{on }C\quad\text{and}\\
\mathrm{PP}^\Gamma=\mathrm{PP}_D(-N_\Gamma)\ \text{on }\Gamma
\end{gathered}
\]
with \(\mathcal J^*\). This defines an isomorphism \(\Psi:\mathrm{PP}^C\to\mathrm{PP}^\Gamma\) without any choice of coordinates or frames.

*The adjoint jets.* Restriction from \(H^0(\Sigma,N_\Sigma)\) to \(C\) has kernel \(H^0(\mathcal O(-5,-2))=0\) and cokernel inside \(H^1(\mathcal O(-5,-2))=0\); restriction to \(\Gamma\) has cokernel inside \(H^1(\mathcal O(1,0))=0\) (Lemma 1.1 of the lesson on the elliptic curve). So the images \(A\subset\mathcal J\) of \(H^0(C,K_C-3H)\) and of \(H^0(\Gamma,N_\Gamma)\) both equal the image of \(H^0(\Sigma,N_\Sigma)\). Moreover \(\dim A=10\): \(h^0(\Gamma,N_\Gamma)=10\), and restriction to \(D\) is injective on it because \(\deg(N_\Gamma-2Z)=10-12<0\).

*The two global spaces.* By Proposition 3.2 of the lesson on traces, applied on \(C\) with \(B=3H\), the map \(T\mapsto\mathrm{pp}(T/\xi^2)\) from \(H^0(C,\Lambda)=H^0(C,3H+D)\) to \(\mathrm{PP}^C\) has kernel \(\xi^2H^0(C,3H)\) and image the annihilator \(A^\perp\subset\mathcal J^*\). On \(\Gamma\), \(\Phi=2M-N_\Gamma\) by (2.3) of the lesson on the elliptic curve, and \(\beta^2\) is a section of \(2M\) with divisor \(D\), so \(\widetilde T\mapsto\widetilde T/\beta^2\) identifies \(H^0(\Gamma,\Phi)\) with \(H^0(\Gamma,-N_\Gamma+D)\). Proposition 3.2 there, with \(B=-N_\Gamma\), shows that \(\widetilde T\mapsto\mathrm{pp}(\widetilde T/\beta^2)\) has kernel \(H^0(\Gamma,-N_\Gamma)=0\), since \(\deg N_\Gamma=10>0\), and image \(A^\perp\). Composing gives \(\iota\), characterized by \(\mathrm{pp}(\iota([T])/\beta^2)=\Psi(\mathrm{pp}(T/\xi^2))\). Both spaces have dimension \(12-10=2\).

*Local form.* Fix \(q\in Z\). Choose holomorphic coordinates \((y,z)\) on \(\Sigma\) near \(q\), a frame \(\mathfrak g\) of \(\Gamma=\mathcal O(2,2)\) and a frame \(\mathfrak f\) of \(F\), such that
\[
\begin{gathered}
G=y\,\mathfrak g,\qquad e(0,z)=1,\\
\Omega=e(y,z)\,\frac{dy}{y}\wedge dz .
\end{gathered}
\]
This is possible: take a local equation \(y\) of \(\Gamma\) and \(\mathfrak g=G/y\); then \(\Omega=h\,dy\wedge dz_0/y\) for a coordinate \(z_0\) and a unit \(h\), and the function \(z=\int_0^{z_0}h(0,\zeta)\,d\zeta\) of \(z_0\) alone gives \(\Omega=(h/h(0,z_0))\,dy\wedge dz/y\). Then \(\omega=\operatorname{Res}_\Gamma\Omega=dz\) on \(\Gamma\). Let \(\mathfrak m\) be a frame of \(M\) near \(q\) on \(\Gamma\) with \(\mathfrak m^4=\mathfrak g^2\mathfrak f^4|_\Gamma\) under the identification \(4M\cong(2\Gamma+4F)|_\Gamma\) (a fourth root of a unit), and write
\[
K=k(y,z)\,\mathfrak g^2\mathfrak f^4,\qquad \beta=b(z)\,\mathfrak m .
\]
Since \(K|_\Gamma=\beta^4\), \(k(0,z)=b(z)^4\); moreover \(b(0)=0\), \(b'(0)\ne0\), and \(k_y(0,0)\ne0\) because \(C\) is smooth at \(q\). Put \(\kappa(z)=k_y(0,z)\). On \(C\), where \(y=O(z^4)\), the equation \(k=0\) gives
\[
\begin{gathered}
y|_C=-\frac{b(z)^4}{\kappa(z)}+O(z^8),\\
e|_C=1+O(z^4),\\
k_y|_C=\kappa(z)+O(z^4).
\end{gathered}
\tag{2.1}
\]
The adjunction isomorphism (2.3) of the lesson on the curve of genus 21 sends the frame \(\mathfrak g\mathfrak f^4\) of \(\mathcal O(6,2)\) to
\[
\begin{aligned}
&\operatorname{Res}_C\Bigl(\frac{\mathfrak g\mathfrak f^4\cdot G\,\Omega}{K}\Bigr)\\
&\quad=\operatorname{Res}_C\Bigl(\frac{e\,dy\wedge dz}{k}\Bigr)\\
&\quad=\frac{e|_C}{k_y|_C}\,dz,
\end{aligned}
\tag{2.2}
\]
because \(dk\wedge dz=k_y\,dy\wedge dz\).

Let \(a=\xi/z\), a frame of \(\mathcal O_C(Z)\) near \(q\), and \(\tau=\mathfrak f^3a^2\), a frame of \(\Lambda\). The identification \(4\mathcal O_C(Z)\cong\Gamma|_C\), \(\xi^4\mapsto G|_C\), sends \(a^4\) to \((y|_C/z^4)\,\mathfrak g\). With (2.2),
\[
\begin{gathered}
\tau^2=s(z)\,dz\,\mathfrak f^2,\\
s(z)=\frac{e|_C\,y|_C}{z^4\,k_y|_C},\\
s(0)=-\frac{b'(0)^4}{\kappa(0)^2}.
\end{gathered}
\tag{2.3}
\]

Write \(T=\pi(z)\tau\) near \(q\), and \(\widetilde T=\iota([T])=\widetilde\pi(z)\widetilde\tau\) in the frame \(\widetilde\tau=\mathfrak m^2/(\mathfrak g\mathfrak f)\) of \(\Phi=2M-(\Gamma+F)|_\Gamma\). Then \(T/\xi^2=\pi\mathfrak f^3/z^2\) and \(\widetilde T/\beta^2=\widetilde\pi/(b^2\,\mathfrak g\mathfrak f)\). A jet in \(\mathcal J\) at \(q\) is represented by \(A(y,z)\,\mathfrak g\mathfrak f\), modulo \((y,z^2)\); on \(C\) it is the section \(A|_C\,(e|_C/k_y|_C)\,dz\,\mathfrak f^{-3}\) of \(K_C-3H\), by (2.2), and on \(\Gamma\) the section \(A(0,z)\,\mathfrak g\mathfrak f\) of \(N_\Gamma\). The two residue functionals are
\[
\begin{gathered}
A\mapsto\operatorname{Res}_{z=0}\Bigl(\frac{A|_C\,\pi\,e|_C}{k_y|_C\,z^2}\,dz\Bigr),\\
A\mapsto\operatorname{Res}_{z=0}\Bigl(\frac{A(0,z)\,\widetilde\pi}{b(z)^2}\,dz\Bigr).
\end{gathered}
\]
Since \(A|_C=A(0,z)+O(z^4)\) and by (2.1), they agree for all \(A\) exactly when
\[
\begin{aligned}
&\mathrm{pp}\Bigl(\frac{\pi}{\kappa(z)z^2}\Bigr)\\
&\quad=\mathrm{pp}\Bigl(\frac{\widetilde\pi}{b(z)^2}\Bigr).
\end{aligned}
\tag{2.4}
\]
Writing \(b=b_1z+b_2z^2+O(z^3)\), \(\kappa=\kappa_0+\kappa_1z+O(z^2)\), \(\pi=\pi_0+\pi_1z+O(z^2)\), and comparing the coefficients of \(z^{-2}\) and \(z^{-1}\),
\[
\begin{aligned}
\widetilde\pi_0&=\frac{b_1^2}{\kappa_0}\pi_0,\\
\widetilde\pi_1&=\frac{b_1^2}{\kappa_0}\pi_1\\
&\quad+\Bigl(\frac{2b_1b_2}{\kappa_0}\\
&\qquad-\frac{b_1^2\kappa_1}{\kappa_0^2}\Bigr)\pi_0 .
\end{aligned}
\tag{2.5}
\]
This invertible triangular transformation is the local expression of \(\iota\). In particular \(\ell_q\circ\iota^{-1}\) and evaluation in \(\widetilde\tau\) at \(q\) are proportional, which is the statement about projective evaluations.

*The metric.* Write \(\eta_C=\mathcal E_C\,dz\,\mathfrak f^2\) on \(C\) and \(\eta_\Gamma=\mathcal E_\Gamma\,dz\,\mathfrak f^2\) on \(\Gamma\). The curves are tangent at \(q\), \(z\) is a parameter on both, and \(u_1,u_2\) are sections on \(\Sigma\); so \(\mathcal E_C(0)=\mathcal E_\Gamma(0)\). Let \(\ell\) be evaluation in \(\tau\) on \(\mathcal W\) and \(\widetilde\ell\) evaluation in \(\widetilde\tau\) on \(H^0(\Gamma,\Phi)\). By (2.5), \(\iota^*\widetilde\ell=\alpha\ell\) with \(\alpha=b_1^2/\kappa_0\), and by (1.1) and (2.3),
\[
\begin{aligned}
(\iota^*\widetilde\ell)^2&=\alpha^2\frac{\mathcal E_C(0)}{s(0)}\\
&=\frac{b_1^4}{\kappa_0^2}\cdot\frac{\mathcal E_C(0)\,\kappa_0^2}{-b_1^4}=-\mathcal E_\Gamma(0).
\end{aligned}
\]
On the other side, \(\widetilde\tau^2=\mathfrak m^4/(\mathfrak g^2\mathfrak f^2)\) corresponds to \(\mathfrak f^2\) under the identifications (2.2) of the lesson on the elliptic curve, which all come from powers of \(\zeta\) and are compatible. The section defining \(Q\) multiplies to \(-\eta_\Gamma/\omega=-\mathcal E_\Gamma\,\mathfrak f^2\), so by (3.1) of that lesson \(Q(\widetilde\ell)=-\mathcal E_\Gamma(0)\). Thus the quadratic forms \(Q\) and \(\lambda\mapsto(\iota^*\lambda)^2\) on \(H^0(\Gamma,\Phi)^*\) agree on the evaluations at \(q_1,\ldots,q_6\), which lie in three distinct directions. Their difference is a binary quadratic form vanishing in three distinct directions, hence zero. \(\square\)

The exact check script of this course verifies (2.1), the value \(s(0)\), the solution (2.5) of (2.4), and the scalar identity above, for generic Taylor coefficients.

## 3. Meromorphic sections with the required residues

**Compatible coordinates.** At \(q_j\), choose a parameter \(z_j\) on a small disc and a frame \(\ell_j\) of \(L\) whose fourth power corresponds to \(dz_j\) under \(4L\cong K_C\); starting from any frame \(\ell^0\) with \((\ell^0)^4\mapsto h\,dz_j\), take \(\ell_j=h^{-1/4}\ell^0\) for a holomorphic fourth root of the unit \(h\). Put
\[
a_j=\xi/z_j,\quad \mathfrak f_j=\ell_j/a_j,\quad \tau_j=\ell_j^2\,\mathfrak f_j,
\]
frames of \(\mathcal O_C(Z)\), \(H=L-Z\) and \(\Lambda=2L+H\). For \(r=\xi u\), a basis of \(H^0(C,L)\), the coefficient row of \(r\) in \(\ell_j\) is \(z_ju\), where \(u\) denotes the coefficient row of \(u\) in \(\mathfrak f_j\). Since \(\tau_j^2=\ell_j^4\mathfrak f_j^2\) corresponds to \(dz_j\,\mathfrak f_j^2\), Lemma 1.1(4) with \(s=1\) gives, for evaluation \(l_j\) in \(\tau_j\),
\[
l_j^2=(u_1u_2'-u_2u_1')(0),
\tag{3.1}
\]
where primes denote \(z_j\)-derivatives on the disc, as in the rest of this section.

**Lemma 3.1 (changing compatible coordinates).** Let \(\zeta=\psi(z)\), \(\psi(0)=0\), be another parameter at \(q_j\), with compatible frame \(g(z)\ell_j\), so that \(g^4=\psi'\); put \(g_0=g(0)\). Then evaluation changes by \(l_j^{\mathrm{new}}=g_0^{-7}l_j\), coefficient rows of sections of \(L\) by \(r^{\mathrm{new}}=g^{-1}r\), and coefficient rows of sections of \(\theta\) by \(P^{\mathrm{new}}=g^{-2}P\).

**Proof.** The new frames are \(a^{\mathrm{new}}=(z/\psi)a_j\), \(\mathfrak f^{\mathrm{new}}=g(\psi/z)\mathfrak f_j\) and \(\tau^{\mathrm{new}}=g^3(\psi/z)\tau_j\); at \(z=0\), \(g^3\psi/z\) equals \(g_0^3\psi'(0)=g_0^7\). The other two statements are the changes of the frames \(\ell\) and \(\ell^2\). \(\square\)

**Proposition 3.2 (residue data).** Put \(v_j^*=\iota^*w_j\in\mathcal W^*\) and \(V=\sum_{j=1}^6v_j^*\). For disjoint compatible coordinate discs at \(q_1,\ldots,q_6\) there are nonzero constants \(c_j\) and a pair
\[
P=(P_1,P_2)\in H^0(C,\theta+Z)^{\oplus2}
\]
with the following properties.

1. \(c_jl_j=v_j^*\), \(V^2=90=9\deg L\), and \((v_j^*)^2+v_j^*\cdot V=1\).
2. On the disc at \(q_j\), with coefficient rows in the frames above, put
\[
\begin{gathered}
m_j=\frac{c_j}{z_j},\qquad R_j=m_jr,\\
W_j=R_j(0)\wedge R_j'(0),\\
p_j=P-m_jr' .
\end{gathered}
\]
The coefficient row of \(P\) in \(\ell_j^2\) has principal part \(R_j(0)/z_j\); the rows \(R_j\) and \(p_j\) are holomorphic, and \(R_j(0)\ne0\).
3. \(W_j=(v_j^*)^2\), \(p_j(0)\wedge R_j(0)=1\), and \(\sum_{j=1}^6(W_j-1)=-9\deg L\).
4. \(J=u\wedge P=u_1P_2-u_2P_1\) lies in \(H^0(C,\Lambda)\), and \(\langle[J],[T]\rangle=-V([T])\) for every \(T\in H^0(C,\Lambda)\). Changing \(P\) by a pair of holomorphic sections of \(\theta\) does not change \([J]\).

The prescription is consistent under changes of compatible coordinates (Exercise 4.4).

**Proof.** (1) By Lemma 2.1, \(\iota^*\) is an isometry, so the identities (4.1) of the lesson on the elliptic curve for the \(w_j\) give those for the \(v_j^*\). The vector \(w_j\) has the direction of evaluation at \(q_j\), so \(v_j^*\) has the direction of \(\ell_{q_j}\), that is, of \(l_j\); since \(w_j\ne0\) and \(l_j\ne0\), there is a unique \(c_j\ne0\) with \(c_jl_j=v_j^*\).

(2) and the first part of (3). On the disc, \(r=z_ju\), so \(R_j=c_ju\) is holomorphic with \(R_j(0)=c_ju(0)\ne0\), as \(u\) has no base point. By (3.1),
\[
\begin{aligned}
W_j&=c_j^2\,(u_1u_2'-u_2u_1')(0)\\
&=c_j^2l_j^2=(v_j^*)^2 .
\end{aligned}
\]
To construct \(P\), apply Proposition 3.2 of the lesson on traces to \(B=\theta\) and \(D=Z\): a family of simple principal parts at \(Z\) is realized by a section of \(\theta+Z\) exactly when it annihilates the values at \(Z\) of the sections of \(K_C-\theta=\theta\). Every section of \(\theta\) vanishes on \(Z\) (Proposition 3.3(3) of the lesson on the curve of genus 21), so every family is realized. Doing this for each entry gives \(P\) with principal parts \(R_j(0)/z_j\). Since \(r'=u+z_ju'\), the row \(m_jr'=c_ju/z_j+c_ju'\) has the same principal part \(c_ju(0)/z_j\) as \(P\), so \(p_j\) is holomorphic.

(4) Near \(q_j\), \(P=c_ju(0)/z_j+O(1)\), so \(u\wedge P=c_j\,u(z_j)\wedge u(0)/z_j+O(1)\), and \(u(z_j)\wedge u(0)=O(z_j)\). Hence \(J\) has no pole, and \(J\in H^0(C,H+\theta)=H^0(C,\Lambda)\). Fix \(T\in H^0(C,\Lambda)\) and consider the meromorphic differential
\[
\begin{gathered}
\nu=\frac{P_1T}{u_1},\\
(\theta+Z)+\Lambda-H=2\theta+Z=K_C+Z .
\end{gathered}
\]
Its poles lie in \(Z\) and in the zero divisor of \(u_1\), a fibre \(f^{-1}(x_\infty)\) of four distinct points disjoint from \(Z\) over a value \(x_\infty\) that is not a branch value. At \(q_j\), with \(T=t(z_j)\tau_j\), the product of the frames \(\ell_j^2\cdot\tau_j/\mathfrak f_j=\ell_j^4\) corresponds to \(dz_j\), and
\[
\begin{aligned}
&\operatorname{Res}_{q_j}\nu\\
&=\operatorname{Res}_{z_j=0}\Bigl(\frac{c_ju_1(0)}{z_j}\cdot\frac{t(z_j)}{u_1(z_j)}\,dz_j\Bigr)\\
&=c_jt(0)=c_jl_j(T),
\end{aligned}
\]
where \(u_1(0)\ne0\). At a zero \(q\) of \(u_1\), the section \(u_2\) does not vanish, \(J(q)=-u_2(q)P_1(q)\) and \(\eta_C(q)=-u_2(q)\,du_1(q)\); hence, \(u_1\) having a simple zero,
\[
\operatorname{Res}_q\nu=\frac{P_1(q)T(q)}{du_1(q)}=\frac{J(q)T(q)}{\eta_C(q)} ,
\]
a ratio of two vectors in the fibre of \(K_C+2H\) at \(q\). By Lemma 1.1(2) of the lesson on traces, the sum of these four residues is \(\operatorname{Tr}(JT/\eta_C)(x_\infty)=B(J,T)=\langle[J],[T]\rangle\), a constant by Lemma 1.1. The residue theorem (Theorem 2.2 of the lesson on traces) gives
\[
\langle[J],[T]\rangle=-\sum_jc_jl_j(T)=-V([T]).
\]
If \(P\) is changed by \(S\in H^0(C,\theta)^{\oplus2}\), then \(S=\xi^2S'\) with \(S'\in H^0(C,2H)^{\oplus2}\) (Proposition 3.3(3) there), so \(u\wedge S=\xi^2(u\wedge S')\in\xi^2H^0(C,3H)\), and \([J]\) is unchanged.

(3), remaining parts. On the disc at \(q_j\), drop the subscript. Since \(r=zu\), \(P=p+mr'=p+cu/z+cu'\), and
\[
\begin{aligned}
cJ&=c\,u\wedge p+c\,u\wedge\frac{cu}{z}\\
&\quad+c\,u\wedge cu'=R\wedge p+R\wedge R' .
\end{aligned}
\]
The coefficient of \(J\) in \(\tau_j=\mathfrak f_j\ell_j^2\) at \(q_j\) is \((u\wedge P)(0)\), so
\[
c_jl_j(J)=R_j(0)\wedge p_j(0)+W_j .
\]
By (4), \([J]\) is the metric dual of \(-V\), so
\[
\begin{aligned}
c_jl_j(J)&=v_j^*([J])=-v_j^*\cdot V\\
&=(v_j^*)^2-1=W_j-1 .
\end{aligned}
\]
Hence \(R_j(0)\wedge p_j(0)=-1\), that is \(p_j(0)\wedge R_j(0)=1\). Summing \(W_j-1=-v_j^*\cdot V\) over \(j\) gives \(-V^2=-90=-9\deg L\). \(\square\)

In the same notation,
\[
\begin{aligned}
P&=\frac{R_j(0)}{z_j}+p_j(0)\\
&\quad+2R_j'(0)+O(z_j),
\end{aligned}
\tag{3.2}
\]
since \(cu/z=R(z)/z\), which is \(R(0)/z+R'(0)+O(z)\), and \(cu'=R'(0)+O(z)\).

## 4. Exercises

**4.1** (easy). Show that \(\xi^2u_1^3,\ \xi^2u_1^2u_2,\ \xi^2u_1u_2^2,\ \xi^2u_2^3\) form a basis of the radical of \(B\) on \(H^0(C,\Lambda)\).

**4.2** (medium). Show that \(\dim\mathcal W=2\) also follows from Lemma 1.1(2) alone, without Proposition 3.2 of the lesson on traces.

**4.3** (medium). Verify (2.5) from (2.4) by expanding both principal parts to order \(z^{-1}\).

**4.4** (medium). Using Lemma 3.1, show that a change of compatible coordinates at \(q_j\) replaces \(c_j\) by \(g_0^7c_j\), \(R_j(0)\) by \(g_0^2R_j(0)\), leaves the principal part prescription satisfied by the same \(P\), and leaves \(W_j\) and \(p_j(0)\wedge R_j(0)\) unchanged.

**4.5** (medium). Show that \(V\ne0\) and that \(J\notin\xi^2H^0(C,3H)\).

## 5. Solutions

**4.1.** By Lemma 1.1(3) the radical is \(\xi^2H^0(C,3H)\). The four cubic monomials in \(u_1,u_2\) are pullbacks of a basis of \(H^0(\mathbb P^1,\mathcal O(3))\), and pullback \(H^0(\mathbb P^1,\mathcal O(3))\to H^0(C,3H)\) is an isomorphism (proof of Lemma 1.1(2)); multiplication by \(\xi^2\) is injective.

**4.2.** \(H^0(C,\Lambda)=H^0(\mathbb P^1,E)\) has dimension \(4+1+1+0=6\) by the splitting \(E\cong\mathcal O(3)\oplus\mathcal O^{\oplus2}\oplus\mathcal O(-3)\), and \(\xi^2H^0(C,3H)=H^0(\mathcal P)\) has dimension four. So \(\dim\mathcal W=2\).

**4.3.** \(1/\kappa=\kappa_0^{-1}-\kappa_1\kappa_0^{-2}z+O(z^2)\), so \(\pi/(\kappa z^2)\) has principal part \(\pi_0\kappa_0^{-1}z^{-2}+(\pi_1\kappa_0^{-1}-\kappa_1\pi_0\kappa_0^{-2})z^{-1}\). Also \(b^{-2}=b_1^{-2}z^{-2}(1-2b_2b_1^{-1}z+O(z^2))\), so \(\widetilde\pi/b^2\) has principal part \(\widetilde\pi_0b_1^{-2}z^{-2}+(\widetilde\pi_1b_1^{-2}-2b_2\widetilde\pi_0b_1^{-3})z^{-1}\). Equating the coefficients of \(z^{-2}\) gives the first formula of (2.5); substituting it into the coefficients of \(z^{-1}\) gives the second.

**4.4.** By Lemma 3.1, \(l^{\mathrm{new}}=g_0^{-7}l\), so the same \(v^*\) gives \(c^{\mathrm{new}}=g_0^7c\). Since \(r^{\mathrm{new}}=g^{-1}r\) and \(m^{\mathrm{new}}=c^{\mathrm{new}}/\zeta\) with \(\zeta=\psi'(0)z+O(z^2)=g_0^4z+O(z^2)\), \(R^{\mathrm{new}}(0)=g_0^7c\,g_0^{-1}u(0)/g_0^4=g_0^2R(0)\). The row \(P^{\mathrm{new}}=g^{-2}P\) has \(\zeta^{-1}\)-coefficient \(g_0^{-2}\psi'(0)R(0)=g_0^2R(0)\), the new prescription. Near \(0\), \(R^{\mathrm{new}}=\lambda R\) with \(\lambda=g_0^7z/(\psi g)\), \(\lambda(0)=g_0^2\), so
\[
\begin{aligned}
&W^{\mathrm{new}}=\lambda(0)R(0)\\
&\quad\wedge\frac{\lambda'(0)R(0)+\lambda(0)R'(0)}{\psi'(0)}\\
&=\frac{g_0^4W}{g_0^4}=W .
\end{aligned}
\]
Finally \(p^{\mathrm{new}}=P^{\mathrm{new}}-m^{\mathrm{new}}\,dr^{\mathrm{new}}/d\zeta\) is holomorphic, and \(p^{\mathrm{new}}(0)\wedge R^{\mathrm{new}}(0)=1\): the proof of Proposition 3.2(3) uses only the principal parts of \(P\) and property (4), and both hold in the new coordinates. (The check script of this course also verifies \(p^{\mathrm{new}}(0)\wedge R^{\mathrm{new}}(0)=p(0)\wedge R(0)\) directly from the transformation rules, for generic Taylor coefficients.)

**4.5.** \(V^2=90\ne0\), so \(V\ne0\). By Proposition 3.2(4), \(\langle[J],\cdot\rangle=-V\ne0\), so \([J]\ne0\) in \(\mathcal W\), that is \(J\notin\xi^2H^0(C,3H)\).

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Section 3: the trace form, the identification by full principal parts, and the residue data.
